#!/usr/bin/env python3
"""deai_check.py — 单章结构体检（改稿后自检用）。

检查项：
  1. YAML frontmatter 完整（--- 成对、id/num/part/kind 等键在）
  2. nav 字段与 ### 章标题一致（去 AI 味改造后要求一致）
  3. ### 章标题存在且以章号前缀开头
  4. ::: div 围栏成对
  5. ``` 围栏成对
  6. HTML 标签配平（strong/em/code/p/div/ul/ol/li/table/tr/td/th/span/a）
  7. 标点伪影（？。、。，等）
  8. 黑名单 S 级词为零
  9. 证据块合规：版本锚点 / 案例框 / 立场框 的标签闭合与来源标注

用法：
  py -3 scripts/deai_check.py source/v1.9/chapters/00-di-ling-zhang.md
  py -3 scripts/deai_check.py --dir source/v1.9/chapters
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
WL = json.loads((HERE / "wordlists.json").read_text(encoding="utf-8"))

ARTIFACTS = [
    (re.compile(r"[？!！][。．]"), "问号/叹号后接句号"),
    (re.compile(r"[。．][，、]"), "句号后接逗号"),
    (re.compile(r"，\s*，"), "重复逗号"),
    (re.compile(r"：\s*："), "重复冒号"),
    (re.compile(r"（\s*）"), "空全角括号"),
    (re.compile(r"^\s*[-*+]\s*$"), "空列表项"),
]

TAGS = ("strong", "em", "code", "p", "div", "ul", "ol", "li", "table", "tr", "td",
        "th", "span", "a", "details", "summary", "blockquote", "h3", "h4", "h5")

CHAPTER_PREFIX = re.compile(r"^(?:第[一二三四五六七八九十百零]+章[：:]|附录[A-H][：:]|结语[：:]|附[：:])")


def _extract_blocks(text: str, kind: str) -> list[str]:
    """按 div 深度配对抽出 kind 框的内容。

    框内还有 <div class="...-head">…</div> 这类子元素，
    用深度计数找配对的 </div>，不能用简单的行匹配。
    """
    out: list[str] = []
    open_tag = f'<div class="{kind}">'
    idx = 0
    while True:
        i = text.find(open_tag, idx)
        if i < 0:
            break
        j = i + len(open_tag)
        depth = 1
        while j < len(text) and depth > 0:
            nxt_open = text.find('<div', j)
            nxt_close = text.find('</div>', j)
            if nxt_close < 0:
                break
            if 0 <= nxt_open < nxt_close:
                depth += 1
                j = nxt_open + 4
            else:
                depth -= 1
                j = nxt_close + 6
        out.append(text[i + len(open_tag):j])
        idx = j
    return out


def check(text: str) -> list[str]:
    lines = text.split("\n")
    problems: list[str] = []

    # 1. frontmatter
    if not text.startswith("---\n"):
        problems.append("缺少 YAML frontmatter")
    else:
        end = None
        for i, ln in enumerate(lines[1:], 1):
            if ln.strip() == "---":
                end = i
                break
        if end is None:
            problems.append("frontmatter 未闭合")
        else:
            fm = "\n".join(lines[1:end])
            for key in ("id:", "kind:"):
                if not re.search(rf"^{key}", fm, re.M):
                    problems.append(f"frontmatter 缺 {key}")
            if not re.search(r"^(part|after_part):", fm, re.M):
                problems.append("frontmatter 既无 part: 也无 after_part:")

    # 2/3. nav 与 ### 标题
    h3 = re.search(r"^###\s*(.+)$", text, re.M)
    if not h3:
        problems.append("缺少 ### 章标题行")
    elif not CHAPTER_PREFIX.match(h3.group(1).strip()):
        problems.append(f"### 标题缺章号前缀：{h3.group(1)[:40]}")

    # 4/5. 围栏
    if text.count("```") % 2:
        problems.append("``` 围栏不配平")
    div_open = len(re.findall(r"^:::(?:inline)?\s+div", text, re.M))
    div_close = len(re.findall(r"^:::\s*$", text, re.M))
    if abs(div_open - div_close) > 1:
        problems.append(f"::: div 围栏明显不配平：开 {div_open} / 闭 {div_close}")

    # 6. HTML 标签配平
    for tag in TAGS:
        o = len(re.findall(rf"<{tag}[\s>]", text))
        c = len(re.findall(rf"</{tag}>", text))
        if o != c:
            problems.append(f"标签 <{tag}> 开合不配平：开 {o} / 闭 {c}")

    # 7. 标点伪影
    for rx, label in ARTIFACTS:
        if rx.search(text):
            line = text[:rx.search(text).start()].split("\n")[-1].strip()
            problems.append(f"{label}：{line[:80]}")

    # 8. 黑名单 S 级
    for w in WL["s_level"]:
        if w in text:
            problems.append(f"黑名单 S 级词：{w}")

    # 9. 证据块：逐框校验（数量对不上不算过）
    for kind in ("case-box", "stance-box"):
        blocks = _extract_blocks(text, kind)
        for i, blk in enumerate(blocks, 1):
            if f'{kind}-head' not in blk:
                problems.append(f"{kind} #{i} 缺 {kind}-head")
            if kind == "case-box":
                if 'case-box-quote' not in blk:
                    problems.append(f"case-box #{i} 缺 case-box-quote")
                if 'case-box-src' not in blk:
                    problems.append(f"case-box #{i} 缺 case-box-src（来源标注是硬要求）")
                elif '场景来源：' not in blk:
                    problems.append(f"case-box #{i} 的来源标注格式不对")
            else:
                if 'stance-box-note' not in blk:
                    problems.append(f"stance-box #{i} 缺 stance-box-note（利益声明是硬要求）")
    # 悬空的 head/quote/src（数量比框多，说明有框被写坏）
    for tag, owner in (("case-box-head", "case-box"), ("case-box-quote", "case-box"),
                       ("case-box-src", "case-box"), ("stance-box-head", "stance-box"),
                       ("stance-box-note", "stance-box")):
        n_tag = len(re.findall(rf'class="{tag}"', text))
        n_box = len(re.findall(rf'<div class="{owner}">', text))
        if n_tag != n_box:
            problems.append(f"{tag} 数量 {n_tag} ≠ {owner} 数量 {n_box}（框可能被写坏）")

    return problems


def git_head(rel: str) -> str | None:
    try:
        r = subprocess.run(["git", "show", f"HEAD:{rel}"], capture_output=True,
                           text=True, cwd=ROOT, timeout=20)
        return r.stdout if r.returncode == 0 else None
    except Exception:
        return None


def rel_path(p: Path) -> str:
    try:
        return p.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return p.as_posix()


def main() -> int:
    ap = argparse.ArgumentParser(description="单章结构体检")
    ap.add_argument("files", nargs="*")
    ap.add_argument("--dir")
    args = ap.parse_args()

    paths: list[Path] = []
    if args.dir:
        paths = sorted(Path(args.dir).glob("*.md"))
    for f in args.files:
        paths.append(Path(f))
    if not paths:
        print("用法：deai_check.py <文件…> | --dir <目录>", file=sys.stderr)
        return 2

    bad = 0
    for p in paths:
        if not p.is_file():
            print(f"[!] 不存在：{p}")
            bad += 1
            continue
        text = p.read_text(encoding="utf-8")
        probs = check(text)
        # 只报"新增"问题：拿 git HEAD 的版本做基线
        head = git_head(rel_path(p))
        if head is not None:
            base = set(check(head))
            probs = [x for x in probs if x.split("：")[0] not in {b.split("：")[0] for b in base}]
        if probs:
            bad += 1
            print(f"✗ {p.name}")
            for x in probs:
                print(f"    - {x}")
    print(f"\n{len(paths) - bad}/{len(paths)} 个文件通过（仅计相对 git HEAD 的新增问题）")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
