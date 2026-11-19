#!/usr/bin/env python3
"""add_lang_tiers.py — 语言选择页的诚实分级（方案 §7.2）。

AI 的恶习是假装 19 种语言同等完美。人会承认"我保证了哪个，没保证哪个"。
所以每张语言卡片上直接标出分级与含义，而不是让读者自己猜。

分级写入 manifest/languages.json（**单一真源**），由 `python -m bookkit index`
渲染进 index.html 的语言卡片。不要手改 index.html——那块是 AUTOGEN 的。

分级依据（与 manifest 现有语言清单对齐）：
  ★★★★★ 简体中文       人工审校版：12 章人工重写，路径库逐条核对，勘误公开
  ★★★   繁體/粵語/English 机翻 + 人工抽查（每篇抽 1 章）
  ★★    其余 15 种       机器翻译版，质量不承诺
  ☆     文言文           文化彩蛋，不承担教学

用法：
  py -3 scripts/add_lang_tiers.py            # dry-run
  py -3 scripts/add_lang_tiers.py --fix      # 写回 manifest
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "manifest" / "languages.json"

TIERS = {
    "zh-CN": {
        "stars": "★★★★★",
        "label": "人工审校版",
        "note": "作者逐章审校：12 个锚章节人工重写，操作路径登记在 path_db.json，勘误公开",
    },
    "zh-TW": {
        "stars": "★★★",
        "label": "机翻 + 人工抽查",
        "note": "繁体转换 + 人工抽查每篇 1 章；用词仍以简体中文版为准",
    },
    "yue": {
        "stars": "★★★",
        "label": "机翻 + 母语群友抽查",
        "note": "文白夹杂需要母语感，关键章由群内粤语读者过一遍",
    },
    "en": {
        "stars": "★★★",
        "label": "机翻 + 人工抽查",
        "note": "机器翻译 + 每篇抽 1 章人工校对；术语表已统一",
    },
    "lzh": {
        "stars": "☆",
        "label": "文化彩蛋",
        "note": "文言文版是语言表演，不承担教学用途；风格化本就是它的预期",
    },
}
DEFAULT_TIER = {
    "stars": "★★",
    "label": "机器翻译版，质量不承诺",
    "note": "机器翻译 + 术语表统一，未做逐章人工校对；请把中文版当作准本",
}

DISCLOSURE = (
    "本分级只标实际投入，不做「同等完美」的假装。本书的中文版是事实源，"
    "其余语言是翻译；翻译里保留一点工整是正常的，也是读者对翻译腔的合理容忍。"
)


def main() -> int:
    ap = argparse.ArgumentParser(description="语言诚实分级")
    ap.add_argument("--fix", action="store_true")
    args = ap.parse_args()

    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    langs = data["languages"]
    changed = 0
    for code, meta in langs.items():
        tier = dict(TIERS.get(code, DEFAULT_TIER))
        if meta.get("quality") != tier:
            meta["quality"] = tier
            changed += 1

    if not args.fix:
        print(f"[i] 将为 {changed} 种语言写入分级（dry-run）")
        for code, meta in sorted(langs.items(), key=lambda x: x[1].get("priority", 99)):
            q = meta["quality"]
            print(f"    {code:<6} {q['stars']}  {q['label']}")
        return 0

    data["language_quality_disclosure"] = DISCLOSURE
    MANIFEST.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"[+] 已为 {changed} 种语言写入分级 → {MANIFEST.name}")
    print("[i] 接着跑 `py -3 -m bookkit index` 让它渲染进 index.html")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
