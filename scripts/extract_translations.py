# -*- coding: utf-8 -*-
"""把 v1.8 的 18 种非中文语言反解为 source/translations/<lang>/ 源稿。

每语言：
1. extract --no-strict → chapters/*.md + parts/ + book.json + template/
2. build --book → 重建 HTML
3. 逐章比对（84 个 content-section 的 normalize 后 inner_html 必须一致）

用法：python scripts/extract_translations.py [--langs a,b,c]
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from bookkit import markdown as M  # noqa: E402

LANGS = ['zh-TW', 'yue', 'lzh', 'ja', 'ko', 'en', 'ru', 'it', 'pt', 'es',
         'fr', 'de', 'ar', 'he', 'th', 'id', 'ms', 'el']
UL_DEFAULT = 'list-disc pl-6 mb-3 space-y-1'
SEC = re.compile(r'<div[^>]*\bid="([a-z0-9-]+)"[^>]*\bclass="[^"]*content-section[^"]*"[^>]*>')

def canon(node):
    """把顶层连续裸 <li> 包进合成 <ul>（翻译稿历史损伤的 DOM 归一，两侧同构后可比）。"""
    from bookkit import htmlparse as H
    out, run = [], []
    for c in node.children:
        if isinstance(c, H.Node) and c.tag == 'li':
            run.append(c)
            continue
        if isinstance(c, str) and not c.strip() and run:
            continue
        if run:
            raw = '<ul class="' + UL_DEFAULT + '">'
            u = H.Node('ul', [], raw)
            u.children, run = run, []
            for li in u.children:
                li.parent = u
            out.append(u)
        out.append(c)
    if run:
        raw = '<ul class="' + UL_DEFAULT + '">'
        u = H.Node('ul', [], raw)
        u.children = run
        for li in u.children:
            li.parent = u
        out.append(u)
    node.children = out

def sections_of(path: Path):
    from bookkit import htmlparse as H
    raw = path.read_text(encoding='utf-8')
    out = {}
    ms = list(SEC.finditer(raw))
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(raw)
        tree = H.parse(raw[m.start():end])
        div = next((n for n in tree.children
                    if isinstance(n, H.Node) and n.tag == 'div'), None)
        if div is None:
            out[m.group(1)] = M.normalize(raw[m.start():end])
            continue
        canon(div)
        inner = ''.join(H.serialize_child(c) for c in div.children)
        out[m.group(1)] = M.normalize(inner)
    return out

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, shell=True, cwd=ROOT)
    return r.returncode, (r.stdout + r.stderr).strip()

def main():
    langs = sys.argv[sys.argv.index('--langs') + 1].split(',') if '--langs' in sys.argv else LANGS
    report = {}
    for lang in langs:
        tdir = ROOT / 'source' / 'translations' / lang
        print(f'== {lang}', flush=True)
        rc, out = run(f'python -m bookkit extract --version v1.8 --lang {lang} '
                      f'--out source/translations/{lang} --no-strict')
        if rc != 0:
            report[lang] = f'EXTRACT FAIL: {out[-200:]}'
            continue
        built = ROOT / 'dist' / f'_verify_{lang}.html'
        rc, out = run(f'python -m bookkit build --lang {lang} '
                      f'--book source/translations/{lang}/book.json '
                      f'--out dist/_verify_{lang}.html')
        if rc != 0:
            report[lang] = f'BUILD FAIL: {out[-200:]}'
            continue
        pub = sections_of(ROOT / 'v1.8' / f'{lang}.html')
        new = sections_of(built)
        diff = [sid for sid in pub if pub.get(sid) != new.get(sid)]
        report[lang] = f'{len(pub) - len(diff)}/{len(pub)} 章一致' + (f'，差异: {diff[:5]}' if diff else '')
        built.unlink(missing_ok=True)
    print('\n===== 反解验证报告 =====')
    bad = 0
    for lang, r in report.items():
        ok = r.startswith('84/') or r.split('章')[0].endswith('/84')
        if not ok:
            bad += 1
        print(f'{"✓" if ok else "✗"} {lang}: {r}')
    print(f'全保真语言: {len(report) - bad}/{len(report)}')

if __name__ == '__main__':
    main()
