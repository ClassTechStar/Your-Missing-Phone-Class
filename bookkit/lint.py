"""lint：跨版本结构与元数据一致性检查。

每个检查的等级由 manifest 中该版本的 ``checks`` 配置决定（error / warn / off）。
"""

import hashlib
import re
from pathlib import Path

from . import textutil as T
from .model import ERROR, Issue, OFF, WARN

CHECK_ORDER = [
    "structure", "coverage", "toc", "orphan", "anchors",
    "title_version", "lang", "nul", "residual", "source_sync", "social",
]


def _meta(raw: str, attr: str, key: str) -> str:
    """取 <meta attr="key" content="…"> 的取值（无则空串）。"""
    m = re.search(rf'<meta {attr}="{re.escape(key)}" content="([^"]*)"', raw)
    return m.group(1) if m else ''


def _rel(root: Path, p: Path) -> str:
    try:
        return p.relative_to(root).as_posix()
    except ValueError:
        return str(p)


def _norm_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes().replace(b'\r\n', b'\n')).hexdigest()


def _emit(issues, version, check, level, message, file="", line=0, detail=""):
    if level == OFF:
        return
    issues.append(Issue(check=check, severity=level, message=message,
                        file=file, line=line, detail=detail))


def lint_version(root: Path, mf, version: str) -> list:
    """检查单个版本目录下的全部语言文件。"""
    issues = []
    files = mf.html_files(version)
    if not files:
        lvl = mf.check_level(version, "structure")
        _emit(issues, version, "structure", lvl or WARN,
              f"{version}/ 目录不存在或无可识别的语言文件")
        return issues

    baseline_code = mf.baseline_lang(version)
    baseline_path = root / version / f"{baseline_code}.html"
    base_raw = baseline_path.read_text(encoding="utf-8") if baseline_path.is_file() else ""
    base_ids = T.section_ids(base_raw)
    base_toc = T.toc_anchors(base_raw)
    expect = mf.expect_sections(version)
    if expect is None:
        expect = len(base_ids)

    for code, path in files:
        rel = _rel(root, path)
        raw = path.read_text(encoding="utf-8", errors="replace")
        meta = mf.lang_meta(code)

        # --- structure：内容区块数量 ---
        lvl = mf.check_level(version, "structure")
        if lvl != OFF:
            n = len(T.section_ids(raw))
            if n != expect:
                _emit(issues, version, "structure", lvl,
                      f"{code} 内容区块数 {n}，期望 {expect}",
                      file=rel, detail=f"相差 {n - expect:+d}")

        # --- nul：NUL 字节 ---
        lvl = mf.check_level(version, "nul")
        if lvl != OFF:
            n = T.nul_count(path.read_bytes())
            if n:
                _emit(issues, version, "nul", lvl, f"{code} 含 {n} 个 NUL 字节", file=rel)

        # --- title_version：<title> 中的版本串 ---
        lvl = mf.check_level(version, "title_version")
        if lvl != OFF:
            t = T.title(raw)
            if not t:
                _emit(issues, version, "title_version", lvl, f"{code} 缺少 <title>", file=rel)
            elif not re.search(r'(^|[^\w])' + re.escape(version) + r'([^\w]|$)', t):
                found = re.findall(r'v\d+\.\d+', t)
                _emit(issues, version, "title_version", lvl,
                      f"{code} 标题不含 {version}",
                      file=rel, detail=f"标题={t[:60]!r} 其中版本串={found}")

        # --- lang：html lang 与 RTL 方向 ---
        lvl = mf.check_level(version, "lang")
        if lvl != OFF:
            want = meta.get("html_lang", "")
            got = T.html_lang(raw)
            if want and got != want:
                _emit(issues, version, "lang", lvl, f"{code} html lang={got!r}，期望 {want!r}", file=rel)
            want_rtl = meta.get("dir") == "rtl"
            if want_rtl != T.has_rtl_marker(raw):
                _emit(issues, version, "lang", lvl,
                      f"{code} dir=\"rtl\" {'缺失' if want_rtl else '不应存在'}", file=rel)

        # --- anchors：页内锚点双向闭合 ---
        lvl = mf.check_level(version, "anchors")
        if lvl != OFF:
            ids = T.all_ids(raw)
            for a in sorted(T.href_anchors(raw) - ids):
                idx = raw.find(f'href="#{a}"')
                _emit(issues, version, "anchors", lvl,
                      f"{code} 断链 #{a}", file=rel,
                      line=T.line_of(raw, idx) if idx >= 0 else 0)

        # --- toc：侧边栏目录与基线一致 ---
        lvl = mf.check_level(version, "toc")
        if lvl != OFF and base_toc:
            toc = T.toc_anchors(raw)
            missing = [a for a in base_toc if a not in toc]
            extra = [a for a in toc if a not in base_toc]
            if missing or extra:
                _emit(issues, version, "toc", lvl,
                      f"{code} 目录锚点与 {baseline_code} 不一致",
                      file=rel,
                      detail=f"缺 {len(missing)} 项{missing[:4]}，多 {len(extra)} 项{extra[:4]}")

        # --- orphan：章节存在但无任何入口 ---
        lvl = mf.check_level(version, "orphan")
        if lvl != OFF:
            refs = T.href_anchors(raw)
            orphans = [s for s in T.section_ids(raw) if s not in refs]
            if orphans:
                _emit(issues, version, "orphan", lvl,
                      f"{code} 有 {len(orphans)} 个区块无任何链接入口",
                      file=rel, detail=f"{orphans[:6]}")

        # --- coverage：相对基线的章节缺口 ---
        lvl = mf.check_level(version, "coverage")
        if lvl != OFF and base_ids:
            own = T.section_ids(raw)
            own_set = set(own)
            missing = [s for s in base_ids if s not in own_set]
            if missing and code != baseline_code:
                if len(own) >= len(base_ids):
                    # 区块数不缺，仅 id 命名与基线不同（如 v1.6/yue 使用 ch1 风格 id）
                    _emit(issues, version, "coverage", lvl,
                          f"{code} 有 {len(missing)} 个基线 id 未出现（区块数相同，疑为 id 命名差异）",
                          file=rel, detail=f"未出现的基线 id={missing[:6]}")
                else:
                    _emit(issues, version, "coverage", lvl,
                          f"{code} 相对 {baseline_code} 缺 {len(missing)} 个章节",
                          file=rel, detail=f"{missing[:6]}")

        # --- residual：残留字形 ---
        lvl = mf.check_level(version, "residual")
        if lvl != OFF:
            script = meta.get("script", "")
            text = T.visible_text(raw)
            if script in T.NON_CJK_SCRIPTS:
                leak = T.cjk_chars(text)
                allow = mf.cjk_allowance(code)
                if len(leak) > allow:
                    sample = ''.join(dict.fromkeys(leak))[:20]
                    _emit(issues, version, "residual", lvl,
                          f"{code} 可见文本含 {len(leak)} 个汉字（上限 {allow}）",
                          file=rel, detail=f"样例={sample}")
            elif script == "Jpan":
                bad = sorted({c for c in text if c in T.SIMP_VS_JA})
                if bad:
                    _emit(issues, version, "residual", lvl,
                          f"{code} 残留疑似简体字", file=rel, detail=f"{bad[:10]}")
            elif script == "Hant":
                bad = sorted({c for c in text if c in T.SIMP_ONLY_HANT})
                if bad:
                    _emit(issues, version, "residual", lvl,
                          f"{code} 残留仅简体字形", file=rel, detail=f"{bad[:10]}")

        # --- social：分享卡片元数据（og / twitter） ---
        # 渠道分发时用户只看到这张卡片：图缺了就没有缩略图，locale 错了会被推到错的地区，
        # 标题里的版本串旧了会指向不存在的版本（历史上 v3.2 / 69 章就是这么留下来的）。
        lvl = mf.check_level(version, "social")
        if lvl != OFF:
            og_img = _meta(raw, 'property', 'og:image')
            og_locale = _meta(raw, 'property', 'og:locale')
            og_title = _meta(raw, 'property', 'og:title')
            tw_img = _meta(raw, 'name', 'twitter:image')
            want = meta.get("og_locale", "")
            if not og_img.startswith(("https://", "http://")):
                _emit(issues, version, "social", lvl,
                      f"{code} og:image 缺失或非绝对地址", file=rel, detail=f"og:image={og_img!r}")
            if want and og_locale != want:
                _emit(issues, version, "social", lvl,
                      f"{code} og:locale={og_locale!r}，期望 {want!r}", file=rel)
            if og_title and version not in og_title:
                _emit(issues, version, "social", lvl,
                      f"{code} og:title 不含 {version}", file=rel, detail=f"og:title={og_title[:60]!r}")
            if not tw_img:
                _emit(issues, version, "social", lvl, f"{code} 缺 twitter:image", file=rel)

    # --- social：分享图必须真的在仓库里（部署脚本要把它拷到站点根） ---
    lvl = mf.check_level(version, "social")
    og_name = mf.data.get("og_image", "")
    if lvl != OFF and og_name:
        cover = root / "docs" / "promotion" / "assets" / og_name
        if not cover.is_file():
            _emit(issues, version, "social", lvl,
                  f"分享图不存在：{cover.relative_to(root).as_posix()}（先运行 python scripts/gen_cover.py）")

    # --- source_sync：根目录源文件与规范文件一致 ---
    lvl = mf.check_level(version, "source_sync")
    spec = mf.version_spec(version).get("source_sync") or {}
    if lvl != OFF and spec:
        canon = root / spec["canonical"]
        src = root / spec["source"]
        if not canon.is_file():
            _emit(issues, version, "source_sync", lvl, f"规范文件缺失：{spec['canonical']}")
        elif not src.is_file():
            _emit(issues, version, "source_sync", lvl, f"源文件缺失：{spec['source']}")
        elif _norm_hash(canon) != _norm_hash(src):
            _emit(issues, version, "source_sync", lvl,
                  "根目录源文件与规范文件不一致",
                  file=spec["source"], detail=f"应对齐 {spec['canonical']}")

    return issues


def run_lint(root: Path, mf, versions=None) -> list:
    """对指定（或全部）版本执行 lint。"""
    if versions is None:
        versions = list(mf.versions.keys())
    issues = []
    for v in versions:
        issues.extend(lint_version(root, mf, v))
    return issues
