# -*- coding: utf-8 -*-
"""样例输出各语言 main.toc 章级条目。"""
import io
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for lang in ['zh-CN', 'ja', 'el', 'de', 'ru']:
    base = ROOT / 'latex' / ('' if lang == 'zh-CN' else lang)
    t = io.open(base / 'main.toc', encoding='utf-8').read()
    chs = re.findall(r'\\contentsline \{chapter\}\{(.+?)\}\{\d+\}', t)
    clean = [re.sub(r'\\[a-zA-Z]+ ?', '', c) for c in chs]
    print(f'== {lang} ({len(clean)} 章级条目) 前5条:')
    for c in clean[:5]:
        print('  ', c[:56])
    print('   末2条:')
    for c in clean[-2:]:
        print('  ', c[:56])
