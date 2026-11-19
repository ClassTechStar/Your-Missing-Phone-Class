#!/usr/bin/env python3
"""deai_gate.py — 去 AI 味改造的全量回归门禁。

一条命令跑完所有闸门，任何一项红就退出非零。可直接进 CI。

用法：
  py -3 scripts/deai_gate.py
  py -3 scripts/deai_gate.py --skip-i18n   # 跳过 18 语译文构建（慢）
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PY = sys.executable

I18N_LANGS = ['zh-TW', 'yue', 'lzh', 'ja', 'ko', 'en', 'ru', 'it', 'pt',
              'es', 'fr', 'de', 'ar', 'he', 'th', 'id', 'ms', 'el']


def gate(name: str, cmd: list[str]) -> tuple[bool, str]:
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=3600)
    out = (r.stdout or "") + (r.stderr or "")
    tail = "\n".join(out.strip().split("\n")[-6:])
    ok = r.returncode == 0
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if not ok:
        for line in tail.split("\n"):
            print(f"       {line}")
    return ok, tail


def main() -> int:
    ap = argparse.ArgumentParser(description="去 AI 味改造全量回归")
    ap.add_argument("--skip-i18n", action="store_true", help="跳过 18 语译文构建")
    args = ap.parse_args()

    results: list[tuple[str, bool]] = []

    # --- 源稿结构 ---
    for label, d in (("v1.9 源稿", "source/v1.9/chapters"),
                     ("v1.8 源稿", "source/chapters")):
        results.append(gate(f"结构体检 · {label}",
                            [PY, "scripts/deai_check.py", "--dir", d]))
    for lg in I18N_LANGS:
        results.append(gate(f"结构体检 · 译文 {lg}",
                            [PY, "scripts/deai_check.py", "--dir",
                             f"source/translations/{lg}/chapters"]))

    # --- 构建与等价性 ---
    results.append(gate("构建 + 逐章等价 · v1.9",
                        [PY, "-m", "bookkit", "build", "--book",
                         "source/v1.9/book.json", "--out", "v1.9/zh-CN.html"]))
    results.append(gate("等价性校验 · v1.9",
                        [PY, "-m", "bookkit", "build", "--book",
                         "source/v1.9/book.json", "--verify"]))
    results.append(gate("构建 + 逐章等价 · v1.8 zh-CN",
                        [PY, "-m", "bookkit", "build", "--lang", "zh-CN",
                         "--out", "v1.8/zh-CN.html"]))
    results.append(gate("等价性校验 · v1.8 zh-CN",
                        [PY, "-m", "bookkit", "build", "--lang", "zh-CN", "--verify"]))

    if not args.skip_i18n:
        for lg in I18N_LANGS:
            results.append(gate(f"构建 · {lg}",
                                [PY, "-m", "bookkit", "build", "--lang", lg,
                                 "--out", f"v1.8/{lg}.html"]))
            results.append(gate(f"等价性校验 · {lg}",
                                [PY, "-m", "bookkit", "build", "--lang", lg, "--verify"]))

    # --- 全局闸门 ---
    results.append(gate("结构 lint（全部版本）",
                        [PY, "-m", "bookkit", "lint", "--all-versions"]))
    results.append(gate("宣称值与死链",
                        [PY, "-m", "bookkit", "check", "--claims", "--index"]))
    results.append(gate("index 生成器最新",
                        [PY, "-m", "bookkit", "index", "--check"]))
    results.append(gate("HTML 全量审计", [PY, "scripts/html_audit.py"]))
    results.append(gate("路径库巡检", [PY, "scripts/path_check.py"]))
    results.append(gate("分章页预算",
                        [PY, "-m", "bookkit", "split", "--book",
                         "source/v1.9/book.json", "--strict-budget"]))
    results.append(gate("速读层派生",
                        [PY, "-m", "bookkit", "quick", "--book",
                         "source/v1.9/book.json"]))
    results.append(gate("单元测试", [PY, "-m", "pytest", "tests/", "-q"]))

    print()
    bad = [n for n, ok in results if not ok]
    print(f"{len(results) - len(bad)}/{len(results)} 项通过")
    if bad:
        print("未通过：")
        for n in bad:
            print(f"  - {n}")
        return 1
    print("全部通过")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
