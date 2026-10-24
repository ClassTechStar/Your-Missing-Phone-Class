# -*- coding: utf-8 -*-
"""统计各语言 pass2.log 的 Overfull hbox 量级。"""
import io
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for lang in ['zh-CN', 'ja', 'el', 'de', 'ru']:
    base = ROOT / 'latex' / ('' if lang == 'zh-CN' else lang)
    log = base / 'pass2.log'
    if not log.exists():
        print(lang, 'no log')
        continue
    t = io.open(log, encoding='utf-8', errors='replace').read()
    h = [float(x) for x in re.findall(r'Overfull \\hbox \(([0-9.]+)pt too wide\)', t)]
    big = [x for x in h if x > 20]
    v = re.findall(r'Overfull \\vbox \(([0-9.]+)pt too high\)', t)
    print(f'{lang}: hbox overfull={len(h)} >20pt={len(big)} max={max(h) if h else 0:.1f}pt | vbox={len(v)}')
