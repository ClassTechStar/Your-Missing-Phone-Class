# -*- coding: utf-8 -*-
"""第三段补丁（应用于 20 份 shell）：
1. criwits-skin-3：补全 v1.9 模板被引用却未定义的 28 个 CSS token（纸面风取值，含暗色），
   并强制蓝底元素（恢复进度 toast / hero 药丸）为白字。
2. 阅读时长 40-55 → 80-95（保留各语言单位后缀）。
"""
import glob

SKIN3 = """<style id="criwits-skin-3">
/* 补全 v1.9 模板引用却未定义的设计 token（纸面风取值） */
:root{
  --ink:#1a1a1a;--ink-2:#495057;--ink-inverse:#ffffff;
  --muted:#868e96;--muted-2:#adb5bd;--muted-3:#adb5bd;
  --line:#e9ecef;--line-2:#dee2e6;--line-3:#e9ecef;
  --surface-2:#f8f9fa;--surface-3:#f1f2f3;--surface-4:#f8f9fa;
  --surface-5:#f0faf4;--surface-6:#f8f9fa;--surface-7:#f8f9fa;
  --gold:#b8860b;--gold-2:#f1c40f;--ok:#2ecc71;
  --sky:#0074d9;--sky-deep:#0b5cad;--sky-wash:#f0f9ff;
  --wash-warm:#fff8ec;--wash-dark:#2d2413;
}
.dark{
  --ink:#e5e7eb;--ink-2:#d1d5db;--ink-inverse:#0b3050;
  --muted:#9ca3af;--muted-2:#6b7280;--muted-3:#6b7280;
  --line:#374151;--line-2:#4b5563;--line-3:#374151;
  --surface-2:#1f2937;--surface-3:#1f2937;--surface-4:#111827;
  --surface-5:#12241c;--surface-6:#111827;--surface-7:#16202e;
  --gold:#ffc266;--ok:#2ecc71;
  --sky:#66b5f2;--sky-deep:#66b5f2;--sky-wash:#0f1c2e;
  --wash-warm:#2d2413;--wash-dark:#0f1c2e;
}
/* 蓝底一律白字：恢复进度 toast / streak toast / hero 药丸 */
.restore-position-toast,#streak-toast{color:#fff!important}
.restore-position-toast .btn-dismiss,#streak-toast .btn-dismiss{color:#fff!important}
.restore-position-toast .btn-restore,#streak-toast .btn-restore{background:#fff!important;color:#0074d9!important}
.dark .restore-position-toast .btn-restore,.dark #streak-toast .btn-restore{background:#0b3050!important;color:#fff!important}
.hero-banner .stat-pill{color:#fff!important}
</style>"""

shells = ['source/template/shell.html', 'source/v1.9/template/shell.html']
shells += sorted(glob.glob('source/translations/*/template/shell.html'))

for p in shells:
    t = open(p, encoding='utf-8').read()
    changed = []
    if 'criwits-skin-3' not in t:
        assert t.count('</head>') == 1, p
        t = t.replace('</head>', SKIN3 + '</head>')
        changed.append('skin3')
    if '40-55' in t:
        n = t.count('40-55')
        t = t.replace('40-55', '80-95')
        changed.append(f'hours x{n}')
    open(p, 'w', encoding='utf-8', newline='').write(t)
    print(p.split('template')[-1], changed if changed else 'no-op')
print('done, shells:', len(shells))
