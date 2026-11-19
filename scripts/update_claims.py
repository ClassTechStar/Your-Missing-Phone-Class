#!/usr/bin/env python3
"""update_claims.py — 把 README / index.html 里的字数宣称刷新成实测值。

宣称数字必须跟内容一起走。内容改完（去 AI 味改造每一轮都会改字数），
不刷新宣称值，`bookkit check --claims` 就会拦下来——这正是那个门禁的意义。

口径与 bookkit/claims.py 完全一致：最新版的**可见文本去掉空白**后的字符数，
换算成万字。

用法：
  py -3 scripts/update_claims.py            # dry-run，只报差异
  py -3 scripts/update_claims.py --fix
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from bookkit import textutil as T  # noqa: E402

RX_README = [
    (re.compile(r'badge/章节-\d+%20节·([\d.]+)%20万字'), 'badge 字数'),
    (re.compile(r'### v1\.9[^\n]*?([\d.]+)\s*万字'), 'v1.9 小节字数'),
    (re.compile(r'共 \d+ 个内容区块），([\d.]+) 万字'), '导语字数'),
    (re.compile(r'（([\d.]+) 万字）'), '仓库表字数'),
]
RX_INDEX = re.compile(r'([\d.]+)\s*万字')


def newest_html(root: Path) -> Path:
    dirs = [p for p in root.iterdir() if p.is_dir() and re.fullmatch(r'v[\d.]+', p.name)]
    if not dirs:
        raise SystemExit("[!] 找不到版本目录")
    ver = max(dirs, key=lambda v: [int(x) for x in v.name.lstrip('v').split('.')])
    return ver / 'zh-CN.html'


def _write(path: Path, text: str) -> bool:
    """写盘带重试：本机偶发 OSError [Errno 22]（索引器抢句柄）。"""
    import time
    for i in range(6):
        try:
            with open(path, 'w', encoding='utf-8', newline='') as f:
                f.write(text)
            return True
        except OSError:
            if i == 5:
                return False
            time.sleep(0.8 * (i + 1))
    return False


def main() -> int:
    ap = argparse.ArgumentParser(description="刷新字数宣称")
    ap.add_argument("--fix", action="store_true")
    args = ap.parse_args()

    hp = newest_html(ROOT)
    if not hp.is_file():
        raise SystemExit(f"[!] 找不到 {hp}，先跑 bookkit build")
    chars = len(re.sub(r'\s+', '', T.visible_text(hp.read_text(encoding='utf-8'))))
    wan = f"{round(chars / 10000, 1):g}"
    print(f"[i] 实测可见文本（去空白）：{chars:,} 字符 = {wan} 万字")

    changed = False

    # 找出当前文案里所有"全书字数"的宣称值（万字），凡不等于实测值的都换成实测值。
    # 不按固定清单硬编码——README/index 里的宣称点会随版本演进增减，
    # 硬编码的清单上次就漏掉了 4 处。
    #
    # 注意：必须要求**至少三位整数**。"约 3 万字"是"每章约 3 万字"，
    # "43.5 万"是"43.5 万 → 367.8 万字"里的起点，这两个都不是全书总数，不能换。
    RX_CLAIM = re.compile(r"(\d{3,}(?:\.\d+)?)(?=(?:%20)?\s*万字)")

    def refresh(text: str, label: str) -> tuple[str, int]:
        nonlocal changed
        n = 0
        seen: set[str] = set()

        def sub(m: re.Match) -> str:
            nonlocal n
            old = m.group(1)
            if old == wan:
                return m.group(0)
            # 同一个旧值可能在页面里出现多次（meta 描述、页脚…）——都要换。
            # re.sub 扫的是原串，每个位置只访问一次，不需要 seen 去重。
            n += 1
            print(f"[i] {label}：{old} → {wan}")
            return wan

        out = RX_CLAIM.sub(sub, text)
        if n:
            changed = True
        return out, n

    # README
    rp = ROOT / "README.md"
    rtext, rn = refresh(rp.read_text(encoding="utf-8"), "README")
    if args.fix and rn:
        rp.write_text(rtext, encoding="utf-8", newline="")
        print("[+] README 已刷新")

    # index.html（硬编码在静态 HTML 里，不随 bookkit index 生成）
    ip = ROOT / "index.html"
    itext = ip.read_text(encoding="utf-8")
    new_itext, in_ = refresh(itext, "index.html")
    if args.fix and in_:
        ip.write_text(new_itext, encoding="utf-8", newline="")
        print("[+] index.html 已刷新")

    if not args.fix:
        print("[i] dry-run，未写回")
    else:
        print("[+] 已刷新宣称值")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
