#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把新正式章节注入 v1.9 两个 HTML 副本（第一章 SoC 部分）。

步骤：
  1. 在原 h4「二、操作系统」之前插入新 h4「二、SoC 是怎么把一件活干完的」；
  2. 原 h4 二~六顺延为三~七（目录/侧边栏不引用这些文字，安全）；
  3. 校验第一章 h4 编号连续为 一~七；
  4. 两个副本归一化后正文一致。

内容见 scripts/v19_soc_mechanism.py。带标记注释保证幂等。

用法：
    python scripts/inject_soc_mechanism.py            # 干跑
    python scripts/inject_soc_mechanism.py --apply    # 写盘
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from v19_soc_mechanism import SECTION_HTML, ANCHOR, MARK, RENUMBER  # noqa: E402

FILES = [ROOT / 'v1.9' / 'zh-CN.html',
         ROOT / '你缺失的那门手机课V1.9Fixed.html']


def h4_titles(s):
    i = s.find('id="di-yi-zhang"')
    j = s.find('id="di-yi-zhang-memory"')
    seg = s[i:j]
    return [re.sub(r'<[^>]+>', '', m.group(1)).strip()
            for m in re.finditer(r'<h4[^>]*>(.*?)</h4>', seg, re.S)]


def main():
    do_apply = '--apply' in sys.argv
    for p in FILES:
        s = p.read_text(encoding='utf-8')
        name = p.relative_to(ROOT)
        print(f'=== {name} ===')
        if MARK in s:
            print('  · 已注入过，跳过')
            continue
        n = s.count(ANCHOR)
        i = s.find('id="di-yi-zhang"')
        j = s.find('id="di-yi-zhang-memory"')
        pos = s.find(ANCHOR)
        first = s.find('一、手机硬件')
        in_first = i < pos < j and first < pos
        print(f'  锚点 {n} 处，位于第一章且在「一、手机硬件」之后: {in_first}')
        bad_renum = [(a, s.count(a)) for a, _ in RENUMBER if s.count(a) != 1]
        print(f'  待顺延标题命中异常: {bad_renum or "无"}')
        if n != 1 or not in_first or bad_renum:
            print('  !! 前置检查失败，停止')
            return 1
        print(f'  插入前 h4: {h4_titles(s)}')
        if not do_apply:
            continue

        s2 = s[:pos] + MARK + '\n' + SECTION_HTML.strip() + '\n' + s[pos:]
        for old, new in RENUMBER:
            s2 = s2.replace(old, new)
        after = h4_titles(s2)
        print(f'  插入后 h4: {[t[:12] for t in after]}')
        expect = ['一', '二', '三', '四', '五', '六', '七']
        got = [t[0] for t in after]
        if got != expect:
            print(f'  !! 编号不连续: {got}')
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
