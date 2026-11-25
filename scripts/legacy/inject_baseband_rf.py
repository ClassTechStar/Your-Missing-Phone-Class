#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把「基带与射频」补充内容注入 v1.9 两个 HTML 副本。

插入位置：第一章 h4「六、基带与天线」的 4 个既有 h5 之后、
h4「七、你的手机，到底在扮演多少角色？」之前。

内容见 scripts/v19_baseband_rf.py。带标记注释保证幂等，
注入后两个副本除 PWA 路径降级外正文保持一致。

用法：
    python scripts/inject_baseband_rf.py            # 干跑
    python scripts/inject_baseband_rf.py --apply    # 写盘
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from v19_baseband_rf import SECTION_HTML, ANCHOR, MARK  # noqa: E402

FILES = [ROOT / 'v1.9' / 'zh-CN.html',
         ROOT / '你缺失的那门手机课V1.9Fixed.html']


def main():
    do_apply = '--apply' in sys.argv
    for p in FILES:
        s = p.read_text(encoding='utf-8')
        name = p.relative_to(ROOT)
        if MARK in s:
            print(f'  · {name}: 已注入过，跳过')
            continue
        n = s.count(ANCHOR)
        pos = s.find(ANCHOR)
        sec6 = s.find('>六、基带与天线')
        sec2 = s.find('>二、SoC 是怎么把一件活干完的')
        in_sec6 = sec6 < pos and sec2 < sec6  # 序号顺延后的位置
        print(f'  {name}: 锚点 {n} 处，位于「六、基带与天线」之后: {in_sec6}')
        if n != 1 or not in_sec6:
            print('  !! 前置检查失败，停止')
            return 1
        if not do_apply:
            continue
        s2 = s[:pos] + MARK + '\n' + SECTION_HTML.strip() + '\n' + s[pos:]
        p.write_text(s2, encoding='utf-8', newline='')
        print(f'    已写盘（{len(s)} → {len(s2)} 字符）')
    if not do_apply:
        print('（干跑，未写盘）')
        return 0
    a = FILES[0].read_text(encoding='utf-8')
    b = FILES[1].read_text(encoding='utf-8')
    norm = (b.replace('href="icons/', 'href="../icons/')
             .replace('href="manifest.webmanifest"', 'href="../manifest.webmanifest"')
             .replace("register('sw.js', { scope: './' })",
                      "register('../sw.js', { scope: '../' })"))
    ok = a == norm
    print(f'两副本归一化后一致: {ok}')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
