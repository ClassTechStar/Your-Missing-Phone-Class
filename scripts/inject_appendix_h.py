#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把附录 H 的 2026 年 11 月修订注入 v1.9 两个 HTML 副本。

步骤：
  1. 校验插入锚点与 4 处待改文本在附录 H 区间内且各出现 1 次；
  2. 改写 h4 标题、两条清单、时效性说明；
  3. 在时效性 warning-box 之前插入「v1.9 深编修订」info-box（带幂等标记）；
  4. 校验 120 个内容区块不变、两副本归一化后一致。

内容见 scripts/v19_appendix_h.py。
归档版 v1.8（19 语）与 source/chapters/83-fu-lu-h.md 不在本次范围内。

用法：
    python scripts/inject_appendix_h.py            # 干跑
    python scripts/inject_appendix_h.py --apply    # 写盘
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from v19_appendix_h import MARK, ANCHOR, NEW_CARD, REPLACEMENTS  # noqa: E402

FILES = [ROOT / 'v1.9' / 'zh-CN.html',
         ROOT / '你缺失的那门手机课V1.9Fixed.html']


def span(s):
    i = s.find('id="fu-lu-h"')
    j = s.find('</main>', i)
    return i, j


def main():
    do_apply = '--apply' in sys.argv
    for p in FILES:
        s = p.read_text(encoding='utf-8')
        name = p.relative_to(ROOT)
        print(f'=== {name} ===')
        if MARK in s:
            print('  · 已更新过，跳过')
            continue
        i, j = span(s)
        checks = [('插入锚点', ANCHOR)] + [(label, old) for label, old, _ in REPLACEMENTS]
        bad = []
        for label, old in checks:
            n = s.count(old)
            pos = s.find(old)
            inside = i < pos < j
            if n != 1 or not inside:
                bad.append((label, n, inside))
        print(f'  待改文本 {len(checks)} 处，异常: {bad or "无"}')
        nsec = len(re.findall(r'class="mb-10 content-section"', s))
        print(f'  当前内容区块: {nsec}')
        if bad or nsec != 120:
            print('  !! 前置检查失败，停止')
            return 1
        if not do_apply:
            continue

        s2 = s
        for label, old, new in REPLACEMENTS:
            s2 = s2.replace(old, new, 1)
            print(f'  已改写：{label}')
        s2 = s2.replace(ANCHOR, MARK + '\n' + NEW_CARD.strip() + '\n' + ANCHOR, 1)

        n2 = len(re.findall(r'class="mb-10 content-section"', s2))
        print(f'  更新后内容区块: {n2}；幂等标记: {s2.count(MARK)}')
        if n2 != 120 or s2.count(MARK) != 1:
            print('  !! 后置检查失败，未写盘')
            return 1
        p.write_text(s2, encoding='utf-8', newline='')
        print(f'  已写盘（{len(s)} → {len(s2)} 字符）')

    if not do_apply:
        print('\n（干跑，未写盘）')
        return 0

    a = FILES[0].read_text(encoding='utf-8')
    b = FILES[1].read_text(encoding='utf-8')
    norm = (b.replace('href="icons/', 'href="../icons/')
             .replace('href="manifest.webmanifest"', 'href="../manifest.webmanifest"')
             .replace("register('sw.js', { scope: './' })",
                      "register('../sw.js', { scope: '../' })"))
    ok = a == norm
    print(f'\n两副本归一化后一致: {ok}')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
