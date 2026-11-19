#!/usr/bin/env python3
"""tsv_to_i18n_titles.py — 把各语言标题 TSV 合成 title_rewrites_v18_i18n.json。

worker 填的是 TSV 第 4 列；这里校验并合成 apply_titles.py 需要的 JSON。

用法：
  py -3 scripts/tsv_to_i18n_titles.py            # 校验并合成
  py -3 scripts/tsv_to_i18n_titles.py --strict   # 有缺失就退出非零
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TSV_DIR = ROOT / "state" / "i18n_titles"
OUT = ROOT / "scripts" / "title_rewrites_v18_i18n.json"
ZH = ROOT / "scripts" / "title_rewrites_v18.json"


def main() -> int:
    ap = argparse.ArgumentParser(description="TSV → i18n 标题 JSON")
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    zh = json.loads(ZH.read_text(encoding="utf-8"))
    zh_entries = {k: v for k, v in zh.items() if not k.startswith("_")}

    out: dict = {
        "_meta": {
            "purpose": "v1.8 译文章标题（按文件位置与中文版一一对应）。",
            "source": "state/i18n_titles/<lang>.tsv（worker 填第 4 列）",
            "generated_by": "scripts/tsv_to_i18n_titles.py",
            "note": "章号前缀与分隔符按各语言现有译文的写法，勿改。",
        }
    }

    missing: list[str] = []
    for tsv in sorted(TSV_DIR.glob("*.tsv")):
        lang = tsv.stem
        rows = {}
        lines = tsv.read_text(encoding="utf-8").split("\n")
        for ln in lines:
            if not ln.strip() or ln.startswith("#"):
                continue
            cols = ln.split("\t")
            if len(cols) < 4:
                missing.append(f"{lang}: 列数不足（{len(cols)}）— {cols[0][:40]}")
                continue
            fname, zh_title, cur, new = cols[0], cols[1], cols[2], cols[3].strip()
            if not new:
                missing.append(f"{lang}: {fname} 第 4 列为空")
                continue
            rows[fname] = {"title": new, "zh_title": zh_title, "current": cur}
        # 完整性：与中文表对齐
        for f in zh_entries:
            if f not in rows:
                missing.append(f"{lang}: 缺 {f}")
        out[lang] = rows
        print(f"[i] {lang}: {len(rows)}/{len(zh_entries)} 条")

    if missing:
        print(f"[!] {len(missing)} 处缺失：")
        for m in missing[:25]:
            print(f"    {m}")
        if args.strict:
            return 1

    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"[+] 已生成 {OUT.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
