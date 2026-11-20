# -*- coding: utf-8 -*-
"""把 criwits 风格对齐层注入 20 份 shell 模板（v1.8 ×19 + v1.9 ×1）。

- 皮肤 CSS：主色靛蓝→蓝、标题字重 400、提示盒左缘粗线、表格/顶栏/侧栏/快捷按钮素色化、渐变卡换蓝调
- 顺带修复 v1.9 模板里 --accent-* 被引用却从未定义的潜在失效样式（皮肤补上定义）
- favicon / theme-color 内联 indigo → 蓝；更新横幅底色同步
用法：py scripts/inject_criwits_skin.py
"""
import glob

SKIN = """<style id="criwits-skin">
/* 风格对齐层：《你缺失的那门计算机课》纸面风 —— 蓝 accent、轻字重、左缘提示盒、素色界面 */
:root{
  --accent-book:#0074d9;
  --accent-deep:#0d4a8f;
  --accent-soft:#66b5f2;
  --accent-wash:rgba(0,116,217,.07);
  --cw-border:#e9ecef;
  --cw-surface:#f1f2f3;
  --cw-head:#f8f9fa;
}
.dark{
  --accent-book:#66b5f2;
  --accent-deep:#0b3050;
  --accent-soft:#66b5f2;
  --accent-wash:rgba(102,181,242,.10);
  --cw-border:#374151;
  --cw-surface:#1f2937;
  --cw-head:#111827;
}
.text-primary{color:#0074d9!important}
.dark .text-primary{color:#66b5f2!important}
.bg-primary{background-color:#0074d9!important}
.dark .bg-primary{background-color:#1b6ac9!important}
.border-primary{border-color:#0074d9!important}
.dark .border-primary{border-color:#66b5f2!important}
.hover\:text-primary:hover{color:#0074d9!important}
.dark .hover\:text-primary:hover{color:#66b5f2!important}
.content-section a,.markdown a{color:#0074d9}
.content-section a:hover,.markdown a:hover{text-decoration:underline}
.dark .content-section a,.dark .markdown a{color:#66b5f2}
.content-section h3,.content-section h4,.content-section h5,.content-section h6{font-weight:400}
.info-box,.tip-box,.success-box,.warning-box,.danger-box,.practice-box,.quote-box,.case-box{
  border:1px solid var(--cw-border)!important;
  border-inline-start-width:.25rem!important;
  border-inline-start-style:solid!important;
  border-radius:.25rem!important;
  background:var(--cw-surface)!important;
}
.info-box,.tip-box,.case-box{border-inline-start-color:#0074d9!important}
.success-box{border-inline-start-color:#2ecc71!important}
.practice-box{border-inline-start-color:#2ecc71!important;background:#f0faf4!important}
.warning-box{border-inline-start-color:#ffc266!important;background:#fff8ec!important}
.danger-box{border-inline-start-color:#f44!important;background:#fdf0ef!important}
.quote-box{border-inline-start-color:#116699!important}
.dark .info-box,.dark .tip-box,.dark .case-box,.dark .quote-box{background:#1f2937!important;border-color:#374151!important}
.dark .warning-box{background:#2d2413!important}
.dark .danger-box{background:#3d1a1a!important}
.dark .practice-box,.dark .success-box{background:#12241c!important}
.content-section table th{background:var(--cw-head)!important}
.content-section table th,.content-section table td{border-color:var(--cw-border)!important}
.dark .content-section table th{background:#111827!important}
#navbar{background:#fff!important;box-shadow:none!important;border-bottom:1px solid var(--cw-border)!important}
.dark #navbar{background:#111827!important;border-bottom-color:#374151!important}
#sidebar{background:#fff!important}
.dark #sidebar{background:#111827!important}
.quick-tool-btn{background:#fff!important;color:#495057!important;border:1px solid var(--cw-border)!important;box-shadow:0 1px 4px rgba(0,0,0,.06)!important}
.dark .quick-tool-btn{background:#1f2937!important;color:#adb5bd!important;border-color:#374151!important}
.restore-position-toast,#streak-toast{background:#0074d9!important;border:none!important}
[class*="from-indigo-6"],[class*="from-indigo-7"],[class*="from-purple-6"],[class*="from-purple-7"]{background-image:linear-gradient(135deg,#0074d9,#2b5cad)!important}
[class*="from-indigo-5"],[class*="from-indigo-4"],[class*="from-indigo-3"],[class*="from-purple-5"],[class*="from-purple-4"],[class*="from-purple-3"],[class*="from-indigo-50"]{background-image:linear-gradient(135deg,#f2f8fd,#eef4fb)!important}
.dark [class*="from-indigo-5"],.dark [class*="from-indigo-4"],.dark [class*="from-indigo-3"],.dark [class*="from-purple-5"],.dark [class*="from-purple-4"],.dark [class*="from-purple-3"]{background-image:linear-gradient(135deg,#16233a,#101a2c)!important}
[class*="bg-clip-text"]{background-image:none!important;color:#0074d9!important;-webkit-text-fill-color:#0074d9!important}
.dark [class*="bg-clip-text"]{color:#66b5f2!important;-webkit-text-fill-color:#66b5f2!important}
</style>"""

shells = ['source/template/shell.html', 'source/v1.9/template/shell.html']
shells += sorted(glob.glob('source/translations/*/template/shell.html'))

for p in shells:
    t = open(p, encoding='utf-8').read()
    if 'criwits-skin' in t:
        print('skip (already injected):', p)
        continue
    assert t.count('</head>') == 1, p
    t = t.replace('</head>', SKIN + '</head>')
    # favicon / theme-color / meta 内联靛蓝 → 蓝
    t = t.replace('%234f46e5', '%230074d9')
    t = t.replace('#4f46e5', '#0074d9')
    # 更新横幅底色同步
    t = t.replace('background:#4f46e5', 'background:#0074d9')
    open(p, 'w', encoding='utf-8', newline='').write(t)
    print('injected:', p)
print('done, shells:', len(shells))
