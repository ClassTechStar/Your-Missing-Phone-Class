# -*- coding: utf-8 -*-
"""标题 emoji 窄剥离 v3：仅 18 集合（与发布 HTML pass2 口径一致），
CR/CR/LF 兼容 + fence 保护。只动 h 标题行行首。"""
import glob
import re

NARROW = ['🖥️', '📦', '🔒', '🔧', '📥', '⚙️', '💻', '🎓', '📚',
          '📁', '📝', '🛠️', '🚀', '✨', '🎯', '💡', '🤖', '📊']


def strip_narrow(md: str):
    # 拆行保留换行风格
    parts = re.split(r'(\r\n|\r|\n)', md)
    lines, seps = [], []
    for i, seg in enumerate(parts):
        (seps if i % 2 else lines).append(seg)
    out, n, in_fence = [], 0, False
    for line in lines:
        if line.lstrip().startswith('```'):
            in_fence = not in_fence
            out.append(line)
            continue
        if not in_fence:
            m = re.match(r'^(#{2,6}[ \t]+)(.*)$', line)
            if m:
                text, changed = m.group(2), False
                while True:
                    hit = next((e for e in NARROW if text.startswith(e)), None)
                    if hit is None:
                        break
                    text = text[len(hit):].lstrip()
                    changed = True
                if changed:
                    n += 1
                    line = m.group(1) + text
        out.append(line)
    # 重组：lines 与 seps 交替（seps 可能比 lines 少一）
    buf = []
    for i, line in enumerate(out):
        buf.append(line)
        if i < len(seps):
            buf.append(seps[i])
    return ''.join(buf), n


total = 0
for p in sorted(glob.glob('source/translations/*/chapters/*.md')):
    md = open(p, encoding='utf-8', newline='').read()
    md2, n = strip_narrow(md)
    if n:
        open(p, 'w', encoding='utf-8', newline='').write(md2)
        total += n
        print(f'{p}: x{n}')
print('total stripped:', total)
