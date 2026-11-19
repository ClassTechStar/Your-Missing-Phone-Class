#!/usr/bin/env python3
"""apply_titles.py — 章标题模板破除（方案 §4.3）+ 标题互引同步。

从 scripts/title_rewrites.json 读取新标题，同步写回两处：
  1. frontmatter 的 nav 字段（TOC 与侧栏读它）
  2. 正文的 ### 章标题行（页面大标题读它）

并同步更新正文中「按标题互引」的交叉引用：
  第二十八章《花对钱买到心仪机——手机选购终极指南》 → 第二十八章《买手机前，先想清楚这三件事》
（附录 C 术语表、附录 G 速查索引里有 49 处这类引用，改名不改引用就是留下死链。）

用法：
  py -3 scripts/apply_titles.py            # dry-run
  py -3 scripts/apply_titles.py --fix
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

PREFIX = re.compile(r"^(?:第[一二三四五六七八九十百零]+章[：:]|附录[A-H][：:]|结语[：:])")
# 第X章《标题》/ 第X章「标题》/ 第X章"标题"
RX_TITLE_XREF = re.compile(
    r"(第[一二三四五六七八九十百零]+章|附录[A-H]|结语)(\s*[《「\"])\s*([^》」\"\n]{2,60}?)\s*([》」\"])"
)

# 版本 → (标题表, 章节目录, 篇首目录)
BOOKS = {
    "v1.9": (HERE / "title_rewrites.json",
             ROOT / "source" / "v1.9" / "chapters",
             ROOT / "source" / "v1.9" / "parts"),
    "v1.8": (HERE / "title_rewrites_v18.json",
             ROOT / "source" / "chapters",
             ROOT / "source" / "parts"),
    "i18n": (HERE / "title_rewrites_v18_i18n.json",
             None, None),          # 译文：按语言目录逐个处理
}


def read_headings(chapters: Path) -> dict[str, str]:
    """现存的章标题（文件名 -> 完整标题，含章号前缀）。"""
    out = {}
    for p in sorted(chapters.glob("*.md")):
        t = p.read_text(encoding="utf-8")
        m = re.search(r"^### (.+)$", t, re.M)
        if m:
            out[p.name] = m.group(1)
    return out


def rewrite_headings(text: str, new_title: str) -> str:
    lines = text.split("\n")
    hit_nav = hit_h3 = False
    for i, ln in enumerate(lines):
        if not hit_nav and re.match(r"^nav:\s*", ln):
            lines[i] = f"nav: {new_title}"
            hit_nav = True
        if not hit_h3 and ln.startswith("### "):
            lines[i] = f"### {new_title}"
            hit_h3 = True
        if hit_nav and hit_h3:
            break
    return "\n".join(lines)


def rewrite_xrefs(text: str, mapping: dict[str, str]) -> tuple[str, int]:
    """把正文里按标题写的交叉引用同步成新标题。返回 (新文本, 替换次数)。"""
    n = 0

    def sub(m: re.Match) -> str:
        nonlocal n
        old_core = m.group(3)
        new_core = mapping.get(old_core)
        if not new_core:
            return m.group(0)
        n += 1
        return f"{m.group(1)}{m.group(2)}{new_core}{m.group(4)}"

    return RX_TITLE_XREF.sub(sub, text), n


def main() -> int:
    ap = argparse.ArgumentParser(description="章标题模板破除 + 互引同步")
    ap.add_argument("--fix", action="store_true", help="写回（默认只 dry-run）")
    ap.add_argument("--diff", default=None, help="diff 输出路径")
    ap.add_argument("--book", default="v1.9", choices=["v1.9", "v1.8", "i18n"])
    ap.add_argument("--lang", action="append", default=[],
                    help="i18n 模式下要处理的语言（可多次指定）")
    args = ap.parse_args()

    data_path, chapters, parts = BOOKS[args.book]
    if not data_path.is_file():
        print(f"[!] 找不到标题表：{data_path}", file=sys.stderr)
        return 2
    data = json.loads(data_path.read_text(encoding="utf-8"))

    if args.book == "i18n":
        # 译文：标题表按语言分节 {"<lang>": {"<file>": {...}}}
        langs = list(args.lang) if args.lang else sorted(
            k for k in data if not k.startswith("_"))
        entries = {}
        for lg in langs:
            sub = data.get(lg)
            if not sub:
                print(f"[!] 标题表里没有语言：{lg}")
                continue
            for fname, spec in sub.items():
                if not fname.startswith("_"):
                    entries[(lg, fname)] = spec
        chapters_by_lang = {lg: ROOT / "source" / "translations" / lg / "chapters"
                            for lg in langs}
        parts_by_lang = {lg: ROOT / "source" / "translations" / lg / "parts"
                         for lg in langs}
    else:
        entries = {(None, k): v for k, v in data.items() if not k.startswith("_")}
        chapters_by_lang = {None: chapters}
        parts_by_lang = {None: parts}

    changed_files: list[str] = []
    diffs: list[str] = []
    xref_total = 0
    missing: list[str] = []

    # 旧标题本体 -> 新标题本体（按语言分别算）
    mapping_by_lang: dict[object, dict[str, str]] = defaultdict(dict)
    for (lg, fname), spec in entries.items():
        cdir = chapters_by_lang.get(lg)
        if cdir is None:
            continue
        headings = read_headings(cdir)
        if fname not in headings:
            continue
        old_core = PREFIX.sub("", headings[fname])
        new_core = PREFIX.sub("", spec["title"])
        if old_core != new_core:
            mapping_by_lang[lg][old_core] = new_core

    for (lg, fname), spec in entries.items():
        p = chapters_by_lang[lg] / fname
        if not p.is_file():
            missing.append(f"{lg or ''}/{fname}")
            continue
        old = p.read_text(encoding="utf-8")
        new = rewrite_headings(old, spec["title"])
        if new != old:
            changed_files.append(f"{lg or ''}/{fname}")
            diffs.append("".join(difflib.unified_diff(
                old.splitlines(keepends=True), new.splitlines(keepends=True),
                fromfile=f"a/{fname}", tofile=f"b/{fname}", n=0)))
            if args.fix:
                p.write_text(new, encoding="utf-8")

    # 互引同步：扫全部章节与篇首
    for lg in chapters_by_lang:
        mapping = mapping_by_lang.get(lg, {})
        cdir = chapters_by_lang[lg]
        pdir = parts_by_lang.get(lg)
        scan = sorted(cdir.glob("*.md"))
        if pdir and pdir.is_dir():
            scan += sorted(pdir.glob("*.md"))
        for p in scan:
            old = p.read_text(encoding="utf-8")
            new, n = rewrite_xrefs(old, mapping)
            if n and new != old:
                xref_total += n
                changed_files.append(f"{lg or ''}/{p.name}")
                diffs.append("".join(difflib.unified_diff(
                    old.splitlines(keepends=True), new.splitlines(keepends=True),
                    fromfile=f"a/{p.name}", tofile=f"b/{p.name}", n=0)))
                if args.fix:
                    p.write_text(new, encoding="utf-8")

    if args.diff and diffs:
        dp = Path(args.diff)
        dp.parent.mkdir(parents=True, exist_ok=True)
        dp.write_text("".join(diffs), encoding="utf-8")
        print(f"[+] diff：{dp}")

    styles: dict[str, int] = {}
    for _, s in entries.items():
        st = s.get("style", "—")
        styles[st] = styles.get(st, 0) + 1
    print(f"[i] 改标题：{len(entries)} 章；风格分布 {styles}")
    print(f"[i] 同步标题互引：{xref_total} 处")
    print(f"[i] 涉及文件：{len(set(changed_files))} 个" + ("" if args.fix else "（dry-run）"))
    if missing:
        print(f"[!] 源稿缺失：{missing}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
