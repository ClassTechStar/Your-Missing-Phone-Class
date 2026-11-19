#!/usr/bin/env python3
"""inject_version_anchor.py — 给含操作路径的章节加版本锚点（方案 §5.4）。

手机 UI 每年一换，AI 训练数据滞后，"连点七次版本号"这类路径可能对不上当前系统。
版本锚点不是装饰，是**时效声明**：读者据此判断这条路径还新鲜吗。

只在真正含操作路径的章节加——纯概念章（编程思维、AI 原理）加"本章界面路径按
iOS 18.x 核对"是假话。

用法：
  py -3 scripts/inject_version_anchor.py            # dry-run
  py -3 scripts/inject_version_anchor.py --fix
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS = ROOT / "source" / "v1.9" / "chapters"

ANCHOR = (
    '<div class="version-anchor">本章界面路径按 iOS 18.x / HarmonyOS 5.x / Android 15 '
    '核对（2026 年 11 月）。你的机型或系统版本不同，菜单名字和位置可能对不上'
    "——以你手机上显示的为准。</div>"
)

# 章节里出现这些，才算"有界面路径可核对"
PATH_MARKERS = (
    "【设置】", "【相册】", "【存储】", "【电池】", "【隐私】", "【通用】",
    "设置 →", "设置→", "设置 >", "打开设置", "进入设置", "菜单路径",
    "系统设置", "手机设置",
)


def has_paths(text: str) -> bool:
    body = text.split("---", 2)[-1]
    return any(m in body for m in PATH_MARKERS)


def inject(text: str) -> str | None:
    """把锚点插到正文第一个 #### 小节之前（速读层之后）。

    放在速读层后面：速读层是"五分钟版"，版本锚点是技术性时效声明，
    放在详细正文开始处更自然，也不会打断开篇的阅读流。
    没有 #### 的章，退回 chapter-intro 之后。
    """
    if "version-anchor" in text:
        return None
    lines = text.split("\n")

    # 首选：第一个 #### 小节之前
    target = None
    for i, ln in enumerate(lines):
        if ln.startswith("#### "):
            target = i
            break

    if target is None:
        # 退回：chapter-intro 之后
        for i, ln in enumerate(lines):
            if "chapter-intro" in ln:
                target = i + 1
                while target < len(lines) and lines[target].strip():
                    target += 1
                break
    if target is None:
        return None

    insert_at = target
    # 往前吞掉紧邻的空行，让锚点紧贴小节标题
    while insert_at > 0 and not lines[insert_at - 1].strip():
        insert_at -= 1
    out = lines[:insert_at] + ["", ANCHOR, ""] + lines[insert_at:]
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description="版本锚点注入")
    ap.add_argument("--fix", action="store_true")
    ap.add_argument("--report", default=None)
    args = ap.parse_args()

    hits, skipped = [], []
    for p in sorted(CHAPTERS.glob("*.md")):
        t = p.read_text(encoding="utf-8")
        if not has_paths(t):
            skipped.append(p.name)
            continue
        new = inject(t)
        if new is None:
            skipped.append(p.name)
            continue
        hits.append(p.name)
        if args.fix:
            p.write_text(new, encoding="utf-8")

    print(f"[i] 加版本锚点：{len(hits)} 章" + ("" if args.fix else "（dry-run）"))
    print(f"[i] 跳过（无操作路径 / 已有锚点）：{len(skipped)} 章")
    if args.report:
        rp = Path(args.report)
        rp.parent.mkdir(parents=True, exist_ok=True)
        rp.write_text("\n".join(hits) + "\n", encoding="utf-8")
        print(f"[+] 清单：{rp}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
