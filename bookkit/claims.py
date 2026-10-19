"""claims：校验 README / index.html 中"宣称的数字与链接"是否与真实内容一致。

对应勘误报告中的 ERR-05（index 统计与目录过期）与 ERR-21（文档宣称漂移）。
"""

import re
from pathlib import Path

from . import textutil as T
from .model import ERROR, Issue

RE_README_HEADLINE = re.compile(
    r'最新版本\s*\((?P<ver>v[\d.]+)\)\s*[—\-–]\s*(?P<langs>\d+)\s*种语言\s*[·、]\s*(?P<sections>\d+)\s*个内容区块')
RE_README_LANG_LINK = re.compile(r'\[[^\]]*\]\((?:\./)?(?P<ver>v[\d.]+)/(?P<code>[\w-]+)\.html\)')
RE_APK = re.compile(r'releases/download/(?P<ver>v[\d.]+)/(?P<asset>[\w.\-]+\.apk)')
RE_INDEX_STAT = re.compile(
    r'<p class="text-4xl md:text-5xl font-black mb-2">([^<]+)</p>')
RE_INDEX_AUTOGEN = re.compile(r'AUTOGEN:languages-(?P<ver>v[\d.]+)\s+(?P<kind>START|END)')


def _stats(mf, root: Path, version: str) -> dict:
    """从真实内容计算：语言数、内容区块数。"""
    files = mf.html_files(version)
    baseline = root / version / f"{mf.baseline_lang(version)}.html"
    sections = 0
    if baseline.is_file():
        sections = len(T.section_ids(baseline.read_text(encoding='utf-8')))
    return {"languages": len(files), "sections": sections, "codes": [c for c, _ in files]}


def check_claims(root: Path, mf) -> list:
    issues = []
    cfg = mf.data.get("claims", {})
    version = mf.latest_version()
    real = _stats(mf, root, version)
    expected_sections = mf.expect_sections(version) or real["sections"]

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
                                "README 未找到「最新版本 (vX) — N 种语言 · M 个内容区块」标题",
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
                                    f"README 宣称 {m.group('sections')} 个内容区块，实际 {expected_sections}",
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

    # ---------- index.html ----------
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
        if str(expected_sections) not in stats:
            issues.append(Issue("claims", ERROR,
                                f"index.html 统计区未标注内容区块数 {expected_sections}",
                                file=index_rel, detail=f"实测统计值={stats}"))
        if version not in stats:
            issues.append(Issue("claims", ERROR,
                                f"index.html 统计区未标注最新版本 {version}",
                                file=index_rel, detail=f"实测统计值={stats}"))
        if str(real["languages"]) not in stats:
            issues.append(Issue("claims", ERROR,
                                f"index.html 统计区未标注语言数 {real['languages']}",
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

    return issues
