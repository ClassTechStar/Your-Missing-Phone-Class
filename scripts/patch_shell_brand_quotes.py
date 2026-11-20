# -*- coding: utf-8 -*-
"""书页壳第二段补丁：
1. 品牌名旧书名 → 《你缺失的那门手机课》（含面包屑）
2. 模板自带正文（首页 hero 等）的直引号 → 「」（仅 CJK 前缀，逐行配对，奇数跳过）
3. criwits-skin-2：压平 hero 渐变与光晕、品牌图标渐变 → 蓝
仅作用于 source/template/shell.html 与 source/v1.9/template/shell.html（中文壳）。
"""
import re

SKIN2 = """<style id="criwits-skin-2">
.hero-banner{background:#0074d9!important;color:#fff!important}
.dark .hero-banner{background:#0d4a8f!important}
.hero-banner::before,.hero-banner::after{display:none!important}
.hero-banner h1{background:none!important;-webkit-background-clip:initial!important;-webkit-text-fill-color:#fff!important;color:#fff!important}
.hero-banner .stat-pill{background:rgba(255,255,255,.14)!important}
[class*="from-primary"],[class*="to-accent"]{background-image:none!important;background:#0074d9!important}
.hero-banner .text-white a,.hero-banner a{background:rgba(255,255,255,.92)!important;color:#075cad!important;border:none!important}
.hero-banner a:hover{background:#fff!important}
</style>"""

CJK = r'[\u4e00-\u9fff，。：；！？、（）【】《》…—]'

def convert_quotes(t):
    out = []
    n = 0
    for ln in t.split('\n'):
        if '"' not in ln:
            out.append(ln); continue
        # 跳过 HTML 标签内部
        spans = [(m.start(), m.end()) for m in re.finditer(r'<[a-zA-Z!/][^>\n]*>', ln)]
        def in_tag(p):
            return any(a <= p < b for a, b in spans)
        parts = []; i = 0; opens = 0; changed_here = False
        while i < len(ln):
            ch = ln[i]
            if ln.startswith('`', i):
                j = ln.find('`', i + 1)
                j = j if j != -1 else len(ln)
                parts.append(ln[i:j]); i = j; continue
            if ch == '"' and not in_tag(i):
                prev = ln[i-1] if i > 0 else ''
                if re.match(CJK, prev):
                    parts.append('「' if opens == 0 else '」')
                    opens ^= 1; changed_here = True; i += 1; continue
            parts.append(ch); i += 1
        if opens != 0:  # 奇数：整行回退
            out.append(ln)
        else:
            out.append(''.join(parts)); n += 1 if changed_here else 0
    return '\n'.join(out), n

for p in ['source/template/shell.html', 'source/v1.9/template/shell.html']:
    t = open(p, encoding='utf-8').read()
    # 1) 品牌名
    t = t.replace('搞定手机 · 数码必修课', '你缺失的那门手机课')
    t = t.replace('搞定手机·数码必修课', '你缺失的那门手机课')
    t = t.replace('数码必修课', '你缺失的那门手机课')
    # 2) 正文直引号
    t, n = convert_quotes(t)
    # 3) 第二段皮肤
    if 'criwits-skin-2' not in t:
        t = t.replace('</head>', SKIN2 + '</head>')
    open(p, 'w', encoding='utf-8', newline='').write(t)
    print(p, '-> quote lines converted:', n, '| brand fixed')
print('done')
