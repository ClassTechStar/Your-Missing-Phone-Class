"""claims：校验 README / index.html 中"宣称的数字与链接"是否与真实内容一致。

对应勘误报告中的 ERR-05（index 统计与目录过期）与 ERR-21（文档宣称漂移）。
"""

import json
import re
from pathlib import Path

from . import textutil as T
from .model import ERROR, Issue

RE_README_HEADLINE = re.compile(
    r'最新版本\s*\((?P<ver>v[\d.]+)\)\s*[—\-–]\s*(?P<langs>\d+)\s*种语言\s*[·、]\s*(?P<sections>\d+)\s*章')
RE_README_LANG_LINK = re.compile(r'\[[^\]]*\]\((?:\./)?(?P<ver>v[\d.]+)/(?P<code>[\w-]+)\.html\)')
RE_APK = re.compile(r'releases/download/(?P<ver>v[\d.]+)/(?P<asset>[\w.\-]+\.apk)')
RE_INDEX_STAT = re.compile(
    r'<p class="text-4xl md:text-5xl font-black mb-2">([^<]+)</p>')
RE_INDEX_AUTOGEN = re.compile(r'AUTOGEN:languages-(?P<ver>v[\d.]+)\s+(?P<kind>START|END)')

# docs/ 也纳入宣称值门禁（方案 W6）：竞赛材料长期停在 v1.8 口径，
# 与 manifest 的语言分级互相打架。这里校验总量、篇数、字数与禁用旧口径。
RE_DOC_INTRO = re.compile(r'—\s*(\d+)\s*章[、,]\s*([\d.]+)\s*万字')
RE_DOC_BODY = re.compile(r'\*\*(\d+)\s*篇\s*·\s*(\d+)\s*个内容区块\s*·\s*([\d.]+)\s*万字\*\*')
RE_DOC_BADGE = re.compile(r'(\d+)\s*区块\s*/\s*(v[\d.]+)\s*/\s*(\d+)\s*语言')
RE_DOC_DATA_BLOCK = re.compile(r'\| 内容区块（简体中文基准） \| (\d+) \|')
RE_DOC_DATA_WAN = re.compile(r'\| 正文字数（简体中文，可见文本） \| ≈ ([\d.]+) 万字 \|')
RE_DOC_DATA_PARTS = re.compile(r'\| 篇章结构 \| (\d+) 篇')
DOC_FORBIDDEN = [
    (re.compile(r'\b84\s*章'), '84 章（v1.8 旧口径）'),
    (re.compile(r'18\.1\s*万字'), '18.1 万字（v1.8 旧口径）'),
    (re.compile(r'非机器翻译直出'), '「非机器翻译直出」与语言分级矛盾'),
    (re.compile(r'19\s*种语言全量翻译'), '「19 种语言全量翻译」与语言分级矛盾'),
    (re.compile(r'19\s*种语言同一质量'), '「19 种语言同一质量」与语言分级矛盾'),
]


def _stats(mf, root: Path, version: str) -> dict:
    """从真实内容计算：语言数、内容区块数。"""
    files = mf.html_files(version)
    baseline = root / version / f"{mf.baseline_lang(version)}.html"
    sections = 0
    if baseline.is_file():
        sections = len(T.section_ids(baseline.read_text(encoding='utf-8')))
    return {"languages": len(files), "sections": sections, "codes": [c for c, _ in files]}


def _check_docs(root: Path, mf, newest: str, newest_real: dict,
                newest_wan: str, real: dict) -> list:
    """docs/ 与 ACCESSIBILITY.md 的对外口径必须与最新版实测一致。"""
    issues = []
    docs = sorted((root / 'docs').rglob('*.md')) if (root / 'docs').is_dir() else []
    acc = root / 'ACCESSIBILITY.md'
    if acc.is_file():
        docs.append(acc)
    parts = 0
    bp = root / 'source' / newest / 'book.json'
    if bp.is_file():
        book = json.loads(bp.read_text(encoding='utf-8'))
        parts = sum(1 for p in book.get('parts', [])
                    if p.get('chapters') and p.get('id') != 'fu-lu')

    def bad(rel, text, pos, msg):
        issues.append(Issue('claims-docs', ERROR, msg, file=rel,
                            line=T.line_of(text, pos) if pos is not None else 0))

    for path in docs:
        rel = str(path.relative_to(root)).replace('\\', '/')
        text = path.read_text(encoding='utf-8')
        for rx, label in DOC_FORBIDDEN:
            m = rx.search(text)
            if not m:
                continue
            # v1.8 的历史记述（如「v1.8（84 章）」）是事实，不算漂移；
            # 只有把旧口径当成当前口径才算过期。
            line_no = T.line_of(text, m.start())
            line = text.splitlines()[line_no - 1] if line_no else ''
            if ('84 章' in label or '18.1' in label) and \
                    ('v1.8' in line or '历史' in line or '译本' in line):
                continue
            bad(rel, text, m.start(), f'{rel} 含过期口径：{label}')
        if rel.endswith('项目说明书.md'):
            m = RE_DOC_INTRO.search(text)
            if not m:
                bad(rel, text, None, f'{rel} 未找到导语「N 章、X 万字」')
            else:
                if int(m.group(1)) != newest_real['sections']:
                    bad(rel, text, m.start(),
                        f'{rel} 导语宣称 {m.group(1)} 章，实测 {newest_real["sections"]}')
                if m.group(2) != newest_wan:
                    bad(rel, text, m.start(),
                        f'{rel} 导语宣称 {m.group(2)} 万字，实测 {newest_wan}')
            m = RE_DOC_BODY.search(text)
            if not m:
                bad(rel, text, None, f'{rel} 未找到「N 篇 · M 个内容区块 · X 万字」')
            else:
                for got, want, name in (
                        (m.group(1), parts, '篇数'),
                        (m.group(2), newest_real['sections'], '内容区块'),
                        (m.group(3), newest_wan, '字数')):
                    if str(got) != str(want):
                        bad(rel, text, m.start(),
                            f'{rel} {name}宣称 {got}，实测 {want}')
        if rel.endswith('数据与证据.md'):
            for rx, want, name in (
                    (RE_DOC_DATA_BLOCK, newest_real['sections'], '内容区块'),
                    (RE_DOC_DATA_WAN, newest_wan, '字数'),
                    (RE_DOC_DATA_PARTS, parts, '篇数')):
                m = rx.search(text)
                if not m:
                    bad(rel, text, None, f'{rel} 未找到{name}行')
                elif str(m.group(1)) != str(want):
                    bad(rel, text, m.start(),
                        f'{rel} {name}宣称 {m.group(1)}，实测 {want}')
        if rel.endswith('答辩演示脚本.md'):
            m = RE_DOC_INTRO.search(text)
            if not m:
                bad(rel, text, None, f'{rel} 未找到导语「N 章、X 万字」')
            else:
                if int(m.group(1)) != newest_real['sections']:
                    bad(rel, text, m.start(),
                        f'{rel} 导语宣称 {m.group(1)} 章，实测 {newest_real["sections"]}')
                if m.group(2) != newest_wan:
                    bad(rel, text, m.start(),
                        f'{rel} 导语宣称 {m.group(2)} 万字，实测 {newest_wan}')
            m = RE_DOC_BADGE.search(text)
            if not m:
                bad(rel, text, None, f'{rel} 未找到首屏徽章「M 区块 / vX / N 语言」')
            else:
                if int(m.group(1)) != newest_real['sections']:
                    bad(rel, text, m.start(),
                        f'{rel} 徽章区块 {m.group(1)}，实测 {newest_real["sections"]}')
                if m.group(2) != newest:
                    bad(rel, text, m.start(),
                        f'{rel} 徽章版本 {m.group(2)}，实际 {newest}')
                if int(m.group(3)) != real['languages']:
                    bad(rel, text, m.start(),
                        f'{rel} 徽章语言数 {m.group(3)}，实际 {real["languages"]}')
    return issues


def check_claims(root: Path, mf) -> list:
    issues = []
    cfg = mf.data.get("claims", {})
    version = mf.latest_version()
    real = _stats(mf, root, version)
    expected_sections = mf.expect_sections(version) or real["sections"]

    # 双版本口径：default 版（v1.8）是 19 语言完整翻译版；仓库中版本号最大的
    # 目录（v1.9）是最新版（中文先行）。统计与字数宣称以最新版口径标注。
    ver_dirs = [p.name for p in root.iterdir()
                if p.is_dir() and re.fullmatch(r'v[\d.]+', p.name)]
    newest = max(ver_dirs,
                 key=lambda v: [int(x) for x in v.lstrip('v').split('.')]) if ver_dirs else version
    newest_real = _stats(mf, root, newest)
    newest_wan = ''
    nb = root / newest / f"{mf.baseline_lang(newest)}.html"
    if nb.is_file():
        chars = len(re.sub(r'\s+', '', T.visible_text(nb.read_text(encoding='utf-8'))))
        newest_wan = f'{round(chars / 10000, 1):g}'

    # ---------- README ----------
    readme_rel = cfg.get("readme", "README.md")
    readme_path = root / readme_rel
    if not readme_path.is_file():
        issues.append(Issue("claims", ERROR, f"{readme_rel} 不存在", file=readme_rel))
    else:
        rd = readme_path.read_text(encoding='utf-8')

        m = RE_README_HEADLINE.search(rd)
        if not m:
            issues.append(Issue("claims", ERROR,
                                "README 未找到「最新版本 (vX) — N 种语言 · M 章」标题",
                                file=readme_rel))
        else:
            if m.group('ver') != version:
                issues.append(Issue("claims", ERROR,
                                    f"README 宣称最新版本 {m.group('ver')}，实际 {version}",
                                    file=readme_rel))
            if int(m.group('langs')) != real["languages"]:
                issues.append(Issue("claims", ERROR,
                                    f"README 宣称 {m.group('langs')} 种语言，实际 {real['languages']}",
                                    file=readme_rel))
            if int(m.group('sections')) != expected_sections:
                issues.append(Issue("claims", ERROR,
                                    f"README 宣称 {m.group('sections')} 章，实际 {expected_sections}",
                                    file=readme_rel))

        # 语言表：每个链接必须存在，且数量与语言数一致
        lang_links = [(mm.group('ver'), mm.group('code')) for mm in RE_README_LANG_LINK.finditer(rd)]
        latest_links = [c for v, c in lang_links if v == version]
        for v, c in lang_links:
            if not (root / v / f"{c}.html").is_file():
                issues.append(Issue("claims", ERROR,
                                    f"README 链接指向不存在的文件 {v}/{c}.html", file=readme_rel))
        if len(set(latest_links)) != real["languages"]:
            issues.append(Issue("claims", ERROR,
                                f"README 语言表有 {len(set(latest_links))} 个 {version} 条目，"
                                f"实际有 {real['languages']} 种语言",
                                file=readme_rel))
        unknown = sorted(set(latest_links) - set(real["codes"]))
        if unknown:
            issues.append(Issue("claims", ERROR,
                                f"README 语言表含非本版本语言 {unknown}", file=readme_rel))

        # APK 链接：版本与数量
        apks = [mm.group('ver') for mm in RE_APK.finditer(rd)]
        if apks:
            wrong = sorted({v for v in apks if v != version})
            if wrong:
                issues.append(Issue("claims", ERROR,
                                    f"README 的 APK 链接指向旧版本 {wrong}，应为 {version}",
                                    file=readme_rel))
            if len(apks) != real["languages"]:
                issues.append(Issue("claims", ERROR,
                                    f"README 提供 {len(apks)} 个 APK 链接，实际 {real['languages']} 种语言",
                                    file=readme_rel))
        # 流水线示意图里残留旧 APK tag（链接检查抓不到纯文本）
        if 'apk-v1.8-r2' in rd:
            issues.append(Issue("claims", ERROR,
                                "README 流水线示意图仍指向旧 APK tag apk-v1.8-r2（应为 r4）",
                                file=readme_rel, line=T.line_of(rd, rd.find('apk-v1.8-r2'))))

        # 章数/字数宣称值：badge 与正文 ↔ 最新版基线实测（字数 = 可见文本去空白）
        for label, rx, want in (
            ('badge 章节数', re.compile(r'badge/章节-(\d+)%20章'), str(newest_real["sections"])),
            ('badge 字数', re.compile(r'badge/章节-\d+%20章·([\d.]+)%20万字'), newest_wan),
            ('v1.9 小节字数', re.compile(r'### v1\.9[^\n]*?([\d.]+)\s*万字'), newest_wan),
            ('导语字数', re.compile(r'共 \d+ 章 · \d+ 篇 · ([\d.]+) 万字'), newest_wan),
            ('仓库表字数', re.compile(r'（([\d.]+) 万字）'), newest_wan),
        ):
            if not want:
                continue
            got = [m.group(1) for m in rx.finditer(rd)]
            if not got:
                issues.append(Issue("claims", ERROR,
                                    f"README 未找到「{label}」宣称", file=readme_rel))
            for v in got:
                if v != want:
                    issues.append(Issue("claims", ERROR,
                                        f"README「{label}」宣称 {v}，实测 {want}",
                                        file=readme_rel))

    # ---------- index.html ----------
    # 统计区以最新版口径标注（ver_dirs / newest 已在上方按双版本口径计算）。
    index_rel = cfg.get("index", "index.html")
    index_path = root / index_rel
    if not index_path.is_file():
        issues.append(Issue("claims", ERROR, f"{index_rel} 不存在", file=index_rel))
    else:
        idx = index_path.read_text(encoding='utf-8')

        for s in cfg.get("forbidden_strings", {}).get("index", []):
            if s in idx:
                line = T.line_of(idx, idx.find(s))
                issues.append(Issue("claims", ERROR,
                                    f"index.html 含过期字符串 {s!r}", file=index_rel, line=line))

        stats = [s.strip() for s in RE_INDEX_STAT.findall(idx)]
        if newest not in stats:
            issues.append(Issue("claims", ERROR,
                                f"index.html 统计区未标注最新版本 {newest}",
                                file=index_rel, detail=f"实测统计值={stats}"))
        if str(newest_real["sections"]) not in stats:
            issues.append(Issue("claims", ERROR,
                                f"index.html 统计区未标注最新版章节数 {newest_real['sections']}",
                                file=index_rel, detail=f"实测统计值={stats}"))
        if str(real["languages"]) not in stats:
            issues.append(Issue("claims", ERROR,
                                f"index.html 统计区未标注完整翻译版语言数 {real['languages']}",
                                file=index_rel, detail=f"实测统计值={stats}"))

        marks = [(mm.group('ver'), mm.group('kind')) for mm in RE_INDEX_AUTOGEN.finditer(idx)]
        if (version, 'START') not in marks or (version, 'END') not in marks:
            issues.append(Issue("claims", ERROR,
                                f"index.html 缺少 AUTOGEN:languages-{version} START/END 标记对",
                                file=index_rel, detail=f"现有标记={marks}"))
        for v, kind in marks:
            if kind == 'START' and (v, 'END') not in marks:
                issues.append(Issue("claims", ERROR,
                                    f"index.html 的 AUTOGEN:languages-{v} 缺少 END",
                                    file=index_rel))

        # 卡片块：每个语言一个链接，且目标存在
        card_links = re.findall(r'<a href="(v[\d.]+)/([\w-]+)\.html"', idx)
        latest_cards = {c for v, c in card_links if v == version}
        if len(latest_cards) != real["languages"]:
            issues.append(Issue("claims", ERROR,
                                f"index.html 的 {version} 卡片块有 {len(latest_cards)} 张，"
                                f"实际 {real['languages']} 种语言",
                                file=index_rel))
        for v, c in card_links:
            if not (root / v / f"{c}.html").is_file():
                issues.append(Issue("claims", ERROR,
                                    f"index.html 卡片指向不存在的文件 {v}/{c}.html",
                                    file=index_rel))

    issues += _check_docs(root, mf, newest, newest_real, newest_wan, real)
    return issues
