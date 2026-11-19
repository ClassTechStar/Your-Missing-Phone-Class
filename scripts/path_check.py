#!/usr/bin/env python3
"""path_check.py — 路径库巡检（方案 §5.1、§10 验收）。

路径库一旦存在，它就要对得起"单一真源"这个名号。本脚本做四件事：

  1. 字段完整性：date / verified_by / status 不得为空
  2. 覆盖率：带版本锚点的章，库里必须有条目（没登记 = 漏了）
  3. 过期巡检：needs-confirm 条目按检查周期提醒复查
  4. 一致性：库里登记的路径，正文里还找得到吗（读者照着做才找得到）

用法：
  py -3 scripts/path_check.py                    # 报告
  py -3 scripts/path_check.py --rebuild          # 先从源稿重建库再报告
  py -3 scripts/path_check.py --max-age-months 9 # 过期阈值
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS = ROOT / "source" / "v1.9" / "chapters"
DB_PATH = ROOT / "path_db.json"

REQUIRED = ("id", "file", "task", "path", "platform", "version_scope", "status", "date", "verified_by")


def load_db() -> dict:
    if not DB_PATH.is_file():
        print("[!] path_db.json 不存在，先跑 scripts/build_path_db.py", file=sys.stderr)
        raise SystemExit(2)
    return json.loads(DB_PATH.read_text(encoding="utf-8"))


def months_between(d1: date, d2: date) -> int:
    return (d2.year - d1.year) * 12 + (d2.month - d1.month)


def parse_ym(s: str) -> date | None:
    m = re.match(r"^(\d{4})-(\d{1,2})", s.strip())
    if not m:
        return None
    try:
        return date(int(m.group(1)), int(m.group(2)), 1)
    except ValueError:
        return None


def main() -> int:
    ap = argparse.ArgumentParser(description="路径库巡检")
    ap.add_argument("--rebuild", action="store_true", help="先从源稿重建 path_db.json")
    ap.add_argument("--max-age-months", type=int, default=9,
                    help="needs-confirm 条目的复查周期（月），默认 9")
    ap.add_argument("--strict", action="store_true", help="有问题时返回非零退出码")
    args = ap.parse_args()

    if args.rebuild:
        r = subprocess.run([sys.executable, str(ROOT / "scripts" / "build_path_db.py")],
                           cwd=ROOT, capture_output=True, text=True)
        print(r.stdout.strip())

    db = load_db()
    entries = db.get("entries", [])
    problems: list[str] = []

    # 1. 字段完整性
    for e in entries:
        for k in REQUIRED:
            if k not in e or e[k] in (None, "", []):
                problems.append(f"{e.get('id', '?')}: 字段 {k} 为空")
        if e.get("status") not in ("confirmed", "needs-confirm"):
            problems.append(f"{e.get('id')}: 未知 status {e.get('status')!r}")
        if parse_ym(str(e.get("date", ""))) is None:
            problems.append(f"{e.get('id')}: date 不是 YYYY-MM 格式")

    # 2. 覆盖率：带版本锚点的章，库里最好有条目
    #    实测结论：全书只有一部分章把路径写成箭头链（【设置】→【电池】），
    #    其余章用散文描述操作，或用箭头串**流程**（"点击→调出→改→留痕"）而不是菜单路径。
    #    所以覆盖率天然不满——这是**书稿的写法**，不是漏登记。这里如实分开报。
    sys.path.insert(0, str(ROOT / "scripts"))
    from build_path_db import RX_CHAIN, PATH_ROOTS, split_chain  # noqa: E402

    def has_ui_chain(text: str) -> bool:
        for m in RX_CHAIN.finditer(text):
            chain = split_chain(m.group(1))
            if 2 <= len(chain) <= 7 and chain[0].strip() in PATH_ROOTS:
                return True
        return False

    db_files = {e["file"] for e in entries}
    anchored, missing, prose_only = [], [], []
    for p in sorted(CHAPTERS.glob("*.md")):
        text = p.read_text(encoding="utf-8")
        if "version-anchor" not in text:
            continue
        anchored.append(p.name)
        if p.name not in db_files:
            missing.append(p.name)
            if not has_ui_chain(text):
                prose_only.append(p.name)

    # 3. 过期巡检
    today = date.today()
    stale = []
    for e in entries:
        if e.get("status") != "needs-confirm":
            continue
        d = parse_ym(str(e.get("date", "")))
        if d and months_between(d, today) >= args.max_age_months:
            stale.append(f"{e['id']} ({e['file']} / {e['task']})")

    # 4. 一致性：库里登记的路径，正文里还找得到吗
    body_by_file: dict[str, str] = {}
    for p in sorted(CHAPTERS.glob("*.md")):
        body_by_file[p.name] = p.read_text(encoding="utf-8")
    lost = []
    for e in entries:
        body = body_by_file.get(e["file"], "")
        if not body:
            continue
        if not any(step in body for step in e["path"]):
            lost.append(f"{e['id']} ({e['file']} / {'→'.join(e['path'])})")

    print("=" * 64)
    print("路径库巡检报告")
    print("=" * 64)
    print(f"库文件        ：{DB_PATH.name}")
    print(f"条目总数      ：{len(entries)}")
    print(f"覆盖章节      ：{len(db_files)} / {len(list(CHAPTERS.glob('*.md')))}")
    print(f"带版本锚点的章：{len(anchored)}")
    print()
    print(f"[1] 字段完整性    ：{'PASS' if not problems else f'{len(problems)} 项异常'}")
    for x in problems[:10]:
        print(f"      - {x}")
    print(f"[2] 锚点章路径登记  ：{len(anchored) - len(missing)}/{len(anchored)}"
          f"（{len(prose_only)} 章为散文式路径，未写成箭头链，不计漏登记）")
    for x in missing[:12]:
        if x not in prose_only:
            print(f"      - 有箭头链但未登记，需补：{x}")
    print(f"[3] 过期巡检      ：{len(stale)} 条 needs-confirm 超过 {args.max_age_months} 个月未复查")
    for x in stale[:10]:
        print(f"      - {x}")
    print(f"[4] 路径一致性    ：{len(entries) - len(lost)}/{len(entries)}"
          + ("  PASS" if not lost else ""))
    for x in lost[:10]:
        print(f"      - 路径在正文中已找不到：{x}")
    print()

    by_file: dict[str, int] = defaultdict(int)
    for e in entries:
        by_file[e["file"]] += 1
    if by_file:
        top = sorted(by_file.items(), key=lambda x: -x[1])[:8]
        print("登记最多的章：" + "、".join(f"{k.replace('.md', '')}({v})" for k, v in top))

    bad = bool(problems or lost)
    if bad and args.strict:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
