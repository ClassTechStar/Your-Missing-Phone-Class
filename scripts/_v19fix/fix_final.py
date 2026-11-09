# -*- coding: utf-8 -*-
"""18 语言终修：
A) emoji 标题剥离 v2（兼容 CR/CR/LF 换行，非行首锚定）
B) SVG 对齐：md 章内 <svg> 块 ← 发布 HTML 对应章的块（build 原样传递 fence，
   两端字节一致）；aria/style 形式以发布 HTML 为准。
每语言 build 一次拿 REB 与 struct-diff 章清单。"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, os.getcwd())
from bookkit import htmlparse as H

LANGS = ['zh-TW', 'yue', 'en', 'ko', 'ja', 'ru', 'it', 'pt', 'es',
         'fr', 'de', 'ar', 'he', 'th', 'id', 'ms', 'el', 'lzh']
ROOT = Path('.')

EMOJI_PAT = (
    r'(^|[\r\n])(#{1,6})[ \t]*'
    r'(?:(?:[\U0001F5A5\U0001F4E6\U0001F512\U0001F527\U0001F4E5\u2699\U0001F4BB'
    r'\U0001F393\U0001F4DA\U0001F4C1\U0001F4DD\U0001F6E0\U0001F680\u2728\U0001F3AF'
    r'\U0001F4A1\U0001F916\U0001F4CA\u2705\u274C\u26A0]\uFE0F?|[\U0001F300-\U0001FAFF'
    r'\u2600-\u27BF][\uFE0F]?)\s*)+'
)

def strip_emojis(md: str):
    def rep(m):
        return m.group(1) + m.group(2) + ' '
    out, n = re.subn(EMOJI_PAT, rep, md)
    return out, n

def sections(html):
    tree = H.parse(html)
    return {n.get('id'): n.inner_raw() for n in tree.find_all('div')
            if 'content-section' in n.classes}

def md_path_for(lang, cid):
    book = json.loads((ROOT / 'source/translations' / lang / 'book.json')
                      .read_text(encoding='utf-8'))
    for c in book['chapters']:
        if c['id'] == cid:
            # book.json 的 file 字段已含 chapters/ 前缀
            p = ROOT / 'source/translations' / lang / c['file']
            return p if p.is_file() else None
    return None

total_emoji = 0
for L in LANGS:
    # ---- A) emoji 剥离（幂等）----
    for p in (ROOT / 'source/translations' / L / 'chapters').glob('*.md'):
        md = p.read_text(encoding='utf-8')
        md2, n = strip_emojis(md)
        if n:
            p.write_text(md2, encoding='utf-8', newline='')
            total_emoji += n
            print(f'{L} emoji x{n}: {p.name}')
    # ---- B) SVG 对齐 ----
    r = subprocess.run(['py', '-m', 'bookkit', 'build', '--lang', L,
                        '--out', f'scripts/_v19fix/_reb_{L}.html'],
                       capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    if '结论' not in (r.stdout + r.stderr) and r.returncode != 0:
        print(L, 'BUILD FAIL', (r.stdout + r.stderr)[-300:])
        continue
    pub = (ROOT / 'v1.8' / f'{L}.html').read_text(encoding='utf-8', newline='')
    reb = (ROOT / 'scripts/_v19fix' / f'_reb_{L}.html').read_text(encoding='utf-8', newline='')
    A, B = sections(pub), sections(reb)
    # struct diff 章：简单重算
    from bookkit import markdown as M
    diff_ch = [cid for cid, raw in A.items()
               if M.normalize(raw) != M.normalize(B.get(cid, ''))]
    if not diff_ch:
        print(L, 'no struct diff (emoji fixed?)')
        continue
    for cid in diff_ch:
        mp = md_path_for(L, cid)
        if mp is None:
            print(L, cid, 'md not found')
            continue
        md = mp.read_text(encoding='utf-8')
        pub_svgs = re.findall(r'<svg[\s\S]*?</svg>', A[cid])
        md_svgs = re.findall(r'<svg[\s\S]*?</svg>', md)
        if len(pub_svgs) != len(md_svgs):
            print(L, cid, f'svg count mismatch pub={len(pub_svgs)} md={len(md_svgs)}')
            continue
        new_md = md
        for old, new in zip(md_svgs, pub_svgs):
            if old != new:
                new_md = new_md.replace(old, new, 1)
        if new_md != md:
            mp.write_text(new_md, encoding='utf-8', newline='')
            print(L, cid, 'svg aligned', len(pub_svgs))
print('total emoji stripped:', total_emoji)
