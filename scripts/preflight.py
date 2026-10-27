#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""发布预检（P2-4，借鉴 CW2 崩溃处理/单实例思路的聚合闸门）。

聚合全部质量闸门 + Release 外链抽检，输出 dist/preflight.html 与终端摘要。
全绿才发版——launch.md 的"第 0 步"收敛为一条命令。

用法：python scripts/preflight.py [--fast]（--fast 跳过 web_smoke 与 PDF 审计）
"""
import io
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'dist' / 'preflight.html'

STEPS = [
    ('bookkit lint', ['python', '-m', 'bookkit', 'lint', '--all-versions']),
    ('bookkit check', ['python', '-m', 'bookkit', 'check', '--claims', '--index']),
    ('build verify', ['python', '-m', 'bookkit', 'build', '--verify']),
    ('quiz lint', ['python', 'scripts/quiz_lint.py']),
    ('html audit', ['python', 'scripts/html_audit.py']),
    ('pdf toc audit', ['python', 'scripts/verify_pdf_toc.py']),
    ('translation fidelity', ['python', 'scripts/extract_translations.py']),
]
FAST_SKIP = {'pdf toc audit', 'translation fidelity'}


def run(label, cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True,
                       cwd=str(ROOT), encoding='utf-8', errors='replace')
    out = (r.stdout or '') + (r.stderr or '')
    tail = '\n'.join(out.strip().splitlines()[-6:])
    return {'label': label, 'cmd': ' '.join(cmd), 'rc': r.returncode, 'tail': tail}


def link_check() -> list:
    """README 引用的 Release tag 抽检（经 gh 验证存在性；凭据来自 git credential）。"""
    import os
    problems = []
    env = dict(os.environ)
    if not env.get('GH_TOKEN'):
        cred_in = 'protocol=https\nhost=github.com\n\n'
        cred = subprocess.run('git credential fill', input=cred_in,
                              capture_output=True, text=True, cwd=str(ROOT))
        m = re.search(r'^password=(.+)$', cred.stdout, re.M)
        if m:
            env['GH_TOKEN'] = m.group(1).strip()
    readme = (ROOT / 'README.md').read_text(encoding='utf-8')
    seen = set()
    for m in re.finditer(r'releases/(?:tag|download)/([\w.\-]+)', readme):
        tag = m.group(1)
        if tag in seen:
            continue
        seen.add(tag)
        r = subprocess.run(['gh', 'release', 'view', tag, '--json', 'tagName'],
                           capture_output=True, text=True, cwd=str(ROOT), env=env)
        if r.returncode != 0:
            problems.append(f'Release 不可访问：{tag}')
    return problems


def main():
    fast = '--fast' in sys.argv
    results = []
    for label, cmd in STEPS:
        if fast and label in FAST_SKIP:
            results.append({'label': label, 'rc': None, 'tail': 'SKIPPED (--fast)'})
            continue
        print(f'… {label}', flush=True)
        results.append(run(label, cmd))
    print('… release link check', flush=True)
    link_problems = link_check()

    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    ok = all(r['rc'] in (0, None) for r in results) and not link_problems

    rows = []
    for r in results:
        state = '✅' if r['rc'] == 0 else ('⏭' if r['rc'] is None else '❌')
        rows.append(f"<tr><td>{state} {r['label']}</td><td><code>{r.get('cmd', '')}</code></td></tr>")
    if link_problems:
        rows.append(f"<tr><td>❌ Release 链接</td><td>{'<br>'.join(link_problems)}</td></tr>")

    html = f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<title>发布预检 · {now}</title><style>
body{{font-family:system-ui,sans-serif;max-width:900px;margin:24px auto;padding:0 16px;
line-height:1.6}}
h1{{font-size:1.4rem}} table{{border-collapse:collapse;width:100%}}
td{{border:1px solid #e5e7eb;padding:8px 12px;font-size:.9rem}}
code{{background:#f3f4f6;padding:1px 5px;border-radius:4px;font-size:.85rem}}
.banner{{padding:12px 18px;border-radius:10px;font-weight:700;margin-bottom:14px}}
.ok{{background:#dcfce7;color:#166534}} .bad{{background:#fee2e2;color:#991b1b}}
pre{{background:#f8f8f8;padding:10px;border-radius:8px;overflow:auto;font-size:.78rem}}
</style></head><body>
<h1>发布预检报告</h1>
<p>{now} · {'--fast' if fast else '全量'}</p>
<div class="banner {'ok' if ok else 'bad'}">{'✅ 全部通过，可以发布' if ok else '❌ 存在失败项，禁止发布'}</div>
<table>{''.join(rows)}</table>
{'<h2>失败详情</h2>' + ''.join(f'<h3>{r["label"]}</h3><pre>{r["tail"]}</pre>'
                                for r in results if r['rc'] not in (0, None))}
</body></html>"""
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(html, encoding='utf-8', newline='\n')
    print(f'\n{"✅ 可发布" if ok else "❌ 禁止发布"} → 报告: {OUT}')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
