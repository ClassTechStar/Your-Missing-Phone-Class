#!/usr/bin/env python3
"""rebuild_all_v18.py — 重建 v1.8 的全部 19 个语言 HTML。

改了源稿就要重建成品——这是本仓库的第一原则：**源稿是唯一事实源，
成品是构建产物**。直接改 HTML 会在下一次 `bookkit build --verify` 时被拦下。

用法：
  py -3 scripts/rebuild_all_v18.py            # 重建 + 逐语言等价性校验
  py -3 scripts/rebuild_all_v18.py --no-verify
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PY = sys.executable

LANGS = ['zh-CN', 'zh-TW', 'yue', 'lzh', 'ja', 'ko', 'en', 'ru', 'it', 'pt',
         'es', 'fr', 'de', 'ar', 'he', 'th', 'id', 'ms', 'el']


def run(args: list[str]) -> tuple[bool, str]:
    r = subprocess.run(args, cwd=ROOT, capture_output=True, text=True, timeout=3600)
    return r.returncode == 0, (r.stdout or "") + (r.stderr or "")


def main() -> int:
    ap = argparse.ArgumentParser(description="重建 v1.8 全部语言")
    ap.add_argument("--no-verify", action="store_true")
    ap.add_argument("--langs", default=",".join(LANGS))
    args = ap.parse_args()

    langs = [x.strip() for x in args.langs.split(",") if x.strip()]
    bad = []
    for lg in langs:
        out = ROOT / "v1.8" / f"{lg}.html"
        ok, log = run([PY, "-m", "bookkit", "build", "--lang", lg, "--out", str(out)])
        if not ok:
            print(f"✗ {lg} 构建失败")
            print("\n".join(log.strip().split("\n")[-6:]))
            bad.append(lg)
            continue
        print(f"[build] {lg}: {log.strip().splitlines()[-1] if log.strip() else 'ok'}")
        if not args.no_verify:
            ok2, log2 = run([PY, "-m", "bookkit", "build", "--lang", lg, "--verify"])
            verdict = "PASS" if ok2 else "FAIL"
            print(f"[verify] {lg}: {verdict}")
            if not ok2:
                for ln in log2.strip().split("\n")[-5:]:
                    print("    " + ln)
                bad.append(lg)

    if bad:
        print(f"\n未通过：{', '.join(bad)}")
        return 1
    print(f"\n{len(langs)} 个语言全部重建并通过等价性校验")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
