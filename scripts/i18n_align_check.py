#!/usr/bin/env python3
"""i18n_align_check.py — 跨语言结构对齐体检。

**为什么需要它**：仓库现有的翻译门禁只验「源稿 → HTML」和「HTML → 源稿」的往返，
**不验译文与中文源稿是否还对得上**。实测就发现西班牙语第三十五章
（中文：给孩子一部手机）的小节标题被换成了摄影、存储、翻译、外卖等别的章的内容——
译文里写着「Usa la cuadrícula para la composición」（构图用三分法），
而中文那一节讲的是几岁给孩子手机。

这类串稿不会被任何现有门禁拦住：往返校验是自洽的（错的译文重建出来还是错的译文）。

**怎么查**：按 `####` 小节切块，比较「每块字符数」这个形状向量。
译文和中文的形状应当高度相关（章节结构一一对应，只是文字长度按语言比例缩放）。
相关系数掉下来，就是这一章的译文被别的内容顶替了。

用法：
  py -3 scripts/i18n_align_check.py
  py -3 scripts/i18n_align_check.py --lang es --verbose
"""

from __future__ import annotations

import argparse
import json
import re
import statistics as st
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZH_DIR = ROOT / "source" / "chapters"

LANGS = ['zh-TW', 'yue', 'lzh', 'ja', 'ko', 'en', 'ru', 'it', 'pt', 'es',
         'fr', 'de', 'ar', 'he', 'th', 'id', 'ms', 'el']

RX_H4 = re.compile(r"^#### (.+)$", re.M)
# 每种语言相对中文的字符膨胀系数（粗略，用于把形状归一）
EXPAND = {
    'zh-TW': 1.0, 'yue': 1.0, 'lzh': 1.0, 'ja': 0.75, 'ko': 0.9,
    'en': 1.9, 'ru': 2.1, 'it': 1.9, 'pt': 1.9, 'es': 2.0, 'fr': 2.1,
    'de': 2.2, 'el': 2.1, 'ar': 1.6, 'he': 1.4, 'th': 1.7,
    'id': 2.0, 'ms': 2.0,
}


def section_lengths(text: str) -> list[int]:
    """按 #### 小节切块，返回每块的字符数。"""
    marks = list(RX_H4.finditer(text))
    if not marks:
        return []
    out = []
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        out.append(len(text[m.end():end].strip()))
    return out


def corr(a: list[float], b: list[float]) -> float:
    n = min(len(a), len(b))
    if n < 3:
        return 1.0
    a, b = a[:n], b[:n]
    if st.pstdev(a) == 0 or st.pstdev(b) == 0:
        return 1.0
    ma, mb = st.mean(a), st.mean(b)
    num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    den = (sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b)) ** 0.5
    return num / den if den else 1.0


def main() -> int:
    ap = argparse.ArgumentParser(description="跨语言结构对齐体检")
    ap.add_argument("--lang")
    ap.add_argument("--threshold", type=float, default=0.55, help="相关系数低于此值即告警")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--out", default=None, help="JSON 报告路径")
    args = ap.parse_args()

    zh = {}
    for p in sorted(ZH_DIR.glob("*.md")):
        zh[p.name] = section_lengths(p.read_text(encoding="utf-8"))

    langs = [args.lang] if args.lang else LANGS
    report = []
    bad = 0
    for lg in langs:
        d = ROOT / "source" / "translations" / lg / "chapters"
        if not d.is_dir():
            continue
        hits = []
        for p in sorted(d.glob("*.md")):
            base = p.name
            if base not in zh:
                continue
            zv = zh[base]
            tv = section_lengths(p.read_text(encoding="utf-8"))
            if len(zv) != len(tv):
                hits.append({"file": base, "reason": "小节数不符",
                             "zh_sections": len(zv), "tr_sections": len(tv),
                             "corr": None})
                continue
            if len(zv) < 3:
                continue
            c = corr(zv, tv)
            if c < args.threshold:
                hits.append({"file": base, "reason": "小节形状与中文对不上",
                             "zh_sections": len(zv), "tr_sections": len(tv),
                             "corr": round(c, 3)})
        report.append({"lang": lg, "hits": hits})
        bad += len(hits)
        flag = "OK " if not hits else "!! "
        print(f"{flag}{lg:<6} {len(hits):>3} 章可疑")
        if args.verbose or hits:
            for h in hits[:12]:
                extra = f" 相关系数 {h['corr']}" if h.get("corr") is not None else ""
                print(f"      {h['file']}: {h['reason']}（中文 {h['zh_sections']} 节 / "
                      f"译文 {h['tr_sections']} 节）{extra}")

    print()
    print(f"合计 {bad} 处可疑（阈值：相关系数 < {args.threshold}）")
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(json.dumps(report, ensure_ascii=False, indent=1),
                                  encoding="utf-8")
        print(f"[+] 报告：{args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
