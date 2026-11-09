#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 GaN 适配器正式章节注入 v1.9 两个 HTML 副本（第十五章）。

步骤：
  1. 在 h4「四、电池新技术：硅碳负极电池」之前插入新 h4「四、氮化镓（GaN）适配器」；
  2. 原 h4 四、五顺延为五、六（目录/侧边栏只引用章 id 与 kuichong 锚点，安全）；
  3. 校验第十五章 h4 编号连续为 一~六；
  4. 两个副本归一化后正文一致。

内容见 scripts/v19_gan_section.py。带标记注释保证幂等。

用法：
    python scripts/inject_gan_section.py            # 干跑
    python scripts/inject_gan_section.py --apply    # 写盘
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from v19_gan_section import SECTION_HTML, ANCHOR, MARK, RENUMBER  # noqa: E402

FILES = [ROOT / 'v1.9' / 'zh-CN.html',
         ROOT / '你缺失的那门手机课V1.9Fixed.html']


def chapter_span(s):
    """返回第十五章内容区间 [start, end)。"""
    i = s.find('id="di-shi-wu-zhang"')
    nxt = s.find('class="mb-10 content-section"', i + 50)
    j = s.rfind('<div', 0, nxt) if nxt > 0 else len(s)
    return i, j


def h4_titles(s):
    i, j = chapter_span(s)
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
        i, j = chapter_span(s)
        pos = s.find(ANCHOR)
        n = s.count(ANCHOR)
        kc = s.find('id="di-shi-wu-zhang-kuichong"')
        warn = s.find('快充安全提示', i, j)
        in_chapter = i < pos < j
        after_protocols = kc < pos
        after_warning = i < warn < pos
        print(f'  锚点 {n} 处；位于第十五章: {in_chapter}；'
              f'在「快充协议」之后: {after_protocols}；在「快充安全提示」之后: {after_warning}')
        bad_renum = [(a[:36], s.count(a)) for a, _ in RENUMBER if s.count(a) != 1]
        print(f'  待顺延标题命中异常: {bad_renum or "无"}')
        if n != 1 or not (in_chapter and after_protocols and after_warning) or bad_renum:
            print('  !! 前置检查失败，停止')
            return 1
        print(f'  插入前 h4: {[t[:14] for t in h4_titles(s)]}')
        if not do_apply:
            continue

        s2 = s[:pos] + MARK + '\n' + SECTION_HTML.strip() + '\n' + s[pos:]
        for old, new in RENUMBER:
            s2 = s2.replace(old, new)
        after = h4_titles(s2)
        print(f'  插入后 h4: {[t[:16] for t in after]}')
        got = [t[0] for t in after]
        if got != ['一', '二', '三', '四', '五', '六']:
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
