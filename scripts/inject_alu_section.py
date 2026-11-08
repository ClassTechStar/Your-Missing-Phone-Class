#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 ALU 一节注入 v1.9 两个 HTML 副本（第一章 SoC 部分，ISP 小节之前）。

内容见 scripts/v19_alu_section.py。
两个文件除 PWA 路径降级外正文应保持一致，注入后仍保持一致。

用法：
    python scripts/inject_alu_section.py            # 干跑
    python scripts/inject_alu_section.py --apply    # 写盘
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from v19_alu_section import SECTION_HTML, ANCHOR, MARK  # noqa: E402

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
        # 锚点必须落在第一章内
        sec_start = s.find('id="di-yi-zhang"')
        sec_end = s.find('id="di-yi-zhang-memory"')
        pos = s.find(ANCHOR)
        in_first = sec_start < pos < sec_end
        print(f'  {name}: 锚点 {n} 处，位于第一章 {in_first}，插入位置 {pos}')
        if n != 1 or not in_first:
            print('  !! 锚点异常，停止')
            return 1
        if not do_apply:
            continue
        s2 = s[:pos] + MARK + '\n' + SECTION_HTML.strip() + '\n' + s[pos:]
        p.write_text(s2, encoding='utf-8', newline='')
        print(f'    已写盘（{len(s)} → {len(s2)} 字符）')
    if not do_apply:
        print('（干跑，未写盘）')
        return 0
    # 一致性：归一化路径后比对
    a = FILES[0].read_text(encoding='utf-8')
    b = FILES[1].read_text(encoding='utf-8')
    norm = (b.replace('href="icons/', 'href="../icons/')
             .replace('href="manifest.webmanifest"', 'href="../manifest.webmanifest"')
             .replace("register('sw.js', { scope: './' })",
                      "register('../sw.js', { scope: '../' })"))
    print('  两副本归一化后一致:', a == norm)
    return 0 if a == norm else 1


if __name__ == '__main__':
    sys.exit(main())
