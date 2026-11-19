#!/usr/bin/env python3
"""extract_paths.py — 从源稿里扫出操作路径，生成 path_db.json 的候选条目。

路径库的作用（方案 §5.1）：正文里的操作路径不再是散落在 353 万字符里的某句话，
而是登记在册、可被脚本核对、可被版本巡检的数据。

用法：
  py -3 scripts/extract_paths.py --out state/path_candidates.json
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS = ROOT / "source" / "v1.9" / "chapters"

# 【设置】→【电池】 这类方括号路径
RX_BRACKET = re.compile(r"【([^】]{1,12})】(?:\s*[→>➔]\s*【([^】]{1,12})】)+")
# 设置 → 通用 → 关于本机  这类箭头路径
RX_ARROW = re.compile(r"([一-鿿A-Za-z][一-鿿A-Za-z0-9 ]{0,10})\s*→\s*([一-鿿A-Za-z][一-鿿A-Za-z0-9 ]{0,10})")
# "点击/打开/进入 + 名称"
RX_VERB = re.compile(r"(?:点击|打开|进入|选择|点开)\s*[「“\"']?(【[^】]{1,14}】|[一-鿿]{2,8})")

PLATFORM_HINTS = {
    "ios": ("iPhone", "iOS", "iPad", "苹果"),
    "harmony": ("鸿蒙", "HarmonyOS", "华为"),
    "android": ("安卓", "Android", "小米", "MIUI", "ColorOS", "OPPO", "vivo", "三星", "一加"),
}

VERSION_RX = re.compile(
    r"(iOS\s*1[5-9](?:\.\d+)?|iOS\s*2\d|HarmonyOS\s*\d+(?:\.\d+)*|鸿蒙\s*\d+(?:\.\d+)*|"
    r"Android\s*1[0-9](?:\.\d+)?|安卓\s*1[0-9]|MIUI\s*1[0-9]|ColorOS\s*\d+(?:\.\d+)*)"
)


def platform_of(text: str) -> list[str]:
    low = text.lower()
    return [k for k, words in PLATFORM_HINTS.items() if any(w.lower() in low for w in words)]


def main() -> int:
    ap = argparse.ArgumentParser(description="抽取操作路径候选")
    ap.add_argument("--out", default="state/path_candidates.json")
    args = ap.parse_args()

    per_chapter: dict[str, list[dict]] = defaultdict(list)

    for p in sorted(CHAPTERS.glob("*.md")):
        text = p.read_text(encoding="utf-8")
        # 去掉代码围栏，避免把命令行当路径
        body = re.sub(r"```.*?```", "", text, flags=re.S)
        body = re.sub(r"`[^`\n]{1,120}`", "", body)

        found: list[dict] = []
        seen: set[str] = set()

        for m in RX_BRACKET.finditer(body):
            chain = re.findall(r"【([^】]{1,12})】", m.group(0))
            key = "→".join(chain)
            if key not in seen and len(chain) >= 2:
                seen.add(key)
                found.append({"kind": "bracket", "path": chain, "raw": m.group(0)})

        for m in RX_ARROW.finditer(body):
            chain = [m.group(1).strip(), m.group(2).strip()]
            key = "→".join(chain)
            if key not in seen:
                seen.add(key)
                found.append({"kind": "arrow", "path": chain, "raw": m.group(0)})

        for m in RX_VERB.finditer(body):
            t = m.group(1)
            if t.startswith("【"):
                t = t.strip("【】")
            key = t
            if key not in seen and len(key) >= 2:
                seen.add(key)
                found.append({"kind": "verb", "path": [t], "raw": m.group(0)})

        if found:
            ctx_versions = sorted(set(VERSION_RX.findall(body)))
            per_chapter[p.name] = {
                "platforms": platform_of(body),
                "versions_mentioned": ctx_versions,
                "paths": found,
            }

    outp = Path(args.out)
    outp.parent.mkdir(parents=True, exist_ok=True)
    outp.write_text(json.dumps(per_chapter, ensure_ascii=False, indent=2), encoding="utf-8")

    total = sum(len(v["paths"]) for v in per_chapter.values())
    print(f"[+] 扫描 {len(list(CHAPTERS.glob('*.md')))} 章，{len(per_chapter)} 章含路径，共 {total} 条候选")
    print(f"[+] 输出：{outp}")
    for name, v in list(per_chapter.items())[:10]:
        print(f"    {name}: {len(v['paths'])} 条, 平台 {v['platforms']}, 版本 {v['versions_mentioned'][:3]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
