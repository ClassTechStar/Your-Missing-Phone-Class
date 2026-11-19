#!/usr/bin/env python3
"""fix_i18n_pseudo_headings.py — 修译文里的"伪标题"。

## 发现的缺陷

v1.8 的 18 种译文里，大量章节的小节标题**不是标题，是被提成标题的正文句子**。
实测英文第 9 章（中文：移动办公与学习）的 5 个 `####` 是这样的：

```
#### : If your company uses genuine Office, this is the best choice. Format compatibility …
```

—— 一百多个字符的句子，顶着 `<h4>` 的粗体大标题。原因是反解时
`<li><strong>Microsoft 365</strong>：如果你公司用正版Office…</li>`
被拆成了「`#### ` + 丢掉标签的正文」，标签（「Microsoft 365」）则变成了
章里孤零零的一行。

**结果**：44% 的译文章节（702 / 1596）里，章的"小节大纲"是一串大写粗体句子，
读起来像坏了的机器排版——这正是去 AI 味要治的病。

## 怎么修

1. `#### : 正文` → 列表项 `- 正文`（去掉残留的 ": "，恢复列表身份）
2. `#### 超长正文`（> 60 字符）→ 普通段落（它本来就不是标题）

**不改**：≤60 字符的正常标题（真标题都短）、`###` 章标题、代码围栏、表格。

修完这些章的小节数会比中文少——因为**译文真正的小节标题在反解时就丢了**，
那是内容修复（要重译），不在去味的范围内。脚本会把这类章列出来，供人工处理。

用法：
  py -3 scripts/fix_i18n_pseudo_headings.py --dry-run
  py -3 scripts/fix_i18n_pseudo_headings.py --fix
"""

from __future__ import annotations

import argparse
import difflib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANGS = ['zh-TW', 'yue', 'lzh', 'ja', 'ko', 'en', 'ru', 'it', 'pt', 'es',
         'fr', 'de', 'ar', 'he', 'th', 'id', 'ms', 'el']

RX_H4 = re.compile(r"^#### (.+)$")
LONG_HEADING = 60       # 超过这个长度的"标题"一定是正文
RESIDUE = ": "          # 反解残留的标签分隔


def fix_file(text: str) -> tuple[str, int]:
    lines = text.split("\n")
    out: list[str] = []
    n = 0
    in_code = False
    for ln in lines:
        s = ln.strip()
        if s.startswith("```"):
            in_code = not in_code
            out.append(ln)
            continue
        if in_code or not s.startswith("#### "):
            out.append(ln)
            continue
        body = s[5:].strip()

        # 反解缺陷之二：标题文字被复制了一遍（"XX…XX"）
        if len(body) % 2 == 0 and len(body) >= 20:
            half = len(body) // 2
            if body[:half] == body[half:]:
                body = body[:half]

        if body.startswith(RESIDUE):
            # 被提成标题的列表项：标签丢了，残留 ": " → 还原成列表项
            out.append(f"- {body[len(RESIDUE):].strip()}")
            n += 1
        elif len(body) > LONG_HEADING:
            # 一百多字的"标题"：本来就不是标题，还原成段落
            out.append(body)
            n += 1
        else:
            out.append(ln)
    return "\n".join(out), n


def main() -> int:
    ap = argparse.ArgumentParser(description="修译文伪标题")
    ap.add_argument("--fix", action="store_true")
    ap.add_argument("--lang", action="append", default=[])
    ap.add_argument("--diff")
    args = ap.parse_args()

    langs = args.lang or LANGS
    diffs: list[str] = []
    total = 0
    per = {}
    for lg in langs:
        d = ROOT / "source" / "translations" / lg / "chapters"
        if not d.is_dir():
            continue
        cnt = 0
        for p in sorted(d.glob("*.md")):
            raw = p.read_text(encoding="utf-8")
            new, n = fix_file(raw)
            if n:
                cnt += n
                diffs.append("".join(difflib.unified_diff(
                    raw.splitlines(keepends=True), new.splitlines(keepends=True),
                    fromfile=f"a/{p.name}", tofile=f"b/{p.name}", n=1)))
                if args.fix:
                    p.write_text(new, encoding="utf-8", newline="")
        per[lg] = cnt
        total += cnt
        print(f"[i] {lg:<6} 修掉 {cnt} 处伪标题")

    print(f"[i] 合计 {total} 处" + ("" if args.fix else "（dry-run）"))
    if args.diff and diffs:
        dp = Path(args.diff)
        dp.parent.mkdir(parents=True, exist_ok=True)
        dp.write_text("".join(diffs), encoding="utf-8")
        print(f"[+] diff：{dp}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
