#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 CMOS 一节注入 v1.9 两个 HTML 副本（第一章「6. 摄像头」内）。

插入位置：原有「像素数不是全部！」段之后、「潜望式长焦镜头」之前。

内容见 scripts/v19_cmos_section.py。带标记注释保证幂等，
注入后两个副本除 PWA 路径降级外正文保持一致。

用法：
    python scripts/inject_cmos_section.py            # 干跑
    python scripts/inject_cmos_section.py --apply    # 写盘
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from v19_cmos_section import SECTION_HTML, ANCHOR, MARK  # noqa: E402

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
        cam = s.find('>6. 摄像头', 140000)
        pixelnote = s.find('像素数不是全部', 140000)
        ok_pos = cam < pixelnote < pos
        print(f'  {name}: 锚点 {n} 处，位于「像素数不是全部」之后: {ok_pos}')
        if n != 1 or not ok_pos:
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
