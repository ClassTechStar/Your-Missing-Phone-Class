# -*- coding: utf-8 -*-
"""18 语言批量修复：SVG fill/stroke 属性并入 style（hex→var 与 zh 同映射）+
translations md 标题行 emoji 剥离。与 zh-CN 已验证流程同构，恢复 19 语言
build --verify 可复现性。"""
import glob
import re

HEX2VAR = {
    '#ffffff': 'var(--ink-inverse)', '#fff': 'var(--ink-inverse)',
    '#9ca3af': 'var(--muted)', '#e5e7eb': 'var(--line)',
    '#4f46e5': 'var(--accent-book)', '#818cf8': 'var(--accent-soft)',
    '#27ae60': 'var(--ok)', '#d4a017': 'var(--gold)', '#0ea5e9': 'var(--sky)',
    '#1f2937': 'var(--surface-dark)', '#e0f2fe': 'var(--sky-wash)',
    '#075985': 'var(--sky-deep)', '#111827': 'var(--ink-3)',
}

EMOJIS = ['🖥️', '📦', '🔒', '🔧', '📥', '⚙️', '💻', '🎓', '📚',
          '📁', '📝', '🛠️', '🚀', '✨', '🎯', '💡', '🤖', '📊']


def normalize_svg_attrs(html: str) -> tuple:
    n = 0
    def fix(m):
        nonlocal n
        tag = m.group(0)
        styles = {}
        sm = re.search(r'style="([^"]*)"', tag)
        base = sm.group(1) if sm else ''
        for prop in ('fill', 'stroke'):
            am = re.search(rf'{prop}="([^"]*)"', tag)
            if am:
                val = am.group(1)
                val = HEX2VAR.get(val.lower(), val)
                styles[prop] = val
                tag = tag.replace(f' {prop}="{am.group(1)}"', '')
                n += 1
        if styles:
            merged = base.rstrip(';')
            for k, v in styles.items():
                merged = f'{k}:{v};' + merged if not merged else f'{k}:{v};' + merged
            if 'style="' in tag:
                tag = re.sub(r'style="[^"]*"', 'style="' + merged + '"', tag, count=1)
            else:
                tag = tag[:-1] + ' style="' + merged + '">' if tag.endswith('>') else tag
        return tag
    out = re.sub(r'<(?:rect|line|path|circle|polygon|polyline|ellipse|g)\b[^>]*>', fix, html)
    return out, n


def strip_heading_emojis(md: str) -> tuple:
    out_lines = []
    n = 0
    for line in md.split('\n'):
        m = re.match(r'^(#{2,6}\s+)(.*)$', line)
        if m:
            text = m.group(2)
            changed = False
            while True:
                hit = None
                for e in EMOJIS:
                    if text.startswith(e):
                        hit = e
                        break
                if hit is None:
                    break
                text = text[len(hit):].lstrip()
                changed = True
            if changed:
                n += 1
                line = m.group(1) + text
        out_lines.append(line)
    return '\n'.join(out_lines), n


htmls = [p for p in sorted(glob.glob('v1.8/*.html')) if 'zh-CN' not in p]
mds = sorted(glob.glob('source/translations/*/chapters/*.md'))
print(f'htmls={len(htmls)} mds={len(mds)}')

for p in htmls:
    raw = open(p, encoding='utf-8', newline='').read()
    raw, n = normalize_svg_attrs(raw)
    open(p, 'w', encoding='utf-8', newline='').write(raw)
    print(p, 'svg x', n)

for p in mds:
    raw = open(p, encoding='utf-8', newline='').read()
    raw, nsvg = normalize_svg_attrs(raw)
    raw, nemo = strip_heading_emojis(raw)
    if nsvg or nemo:
        open(p, 'w', encoding='utf-8', newline='').write(raw)
        print(p, 'svg x', nsvg, '| heading emoji x', nemo)
