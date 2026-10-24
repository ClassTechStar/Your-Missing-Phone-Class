# -*- coding: utf-8 -*-
"""列出所有"不在篇 <section> 内"的章节 div（按 DOM 父链判定，含 main/包装 div 挂载）。

用法：python scripts/find_orphan_sections.py [版本...]
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from bookkit import htmlparse as H  # noqa: E402


def ancestors(node):
    out = []
    p = node.parent
    while p is not None:
        out.append(p)
        p = p.parent
    return out

def main():
    vers = sys.argv[1:] or ['v1.5', 'v1.6', 'v1.7', 'v1.8']
    for ver in vers:
        for p in sorted((ROOT / ver).glob('*.html')):
            if p.stem == 'index' or (ver, p.stem) == ('v1.7', 'lzh'):
                continue
            tree = H.parse(p.read_text(encoding='utf-8'))
            secs = {n.get('id') for n in tree.find_all('section')}
            bad = []
            for n in tree.find_all('div'):
                if 'content-section' not in n.classes:
                    continue
                anc = ancestors(n)
                in_part = False
                for a in anc:
                    if getattr(a, 'tag', '') == 'section' and a.get('id') in secs:
                        in_part = True
                        break
                    if getattr(a, 'tag', '') == 'main':
                        break          # 到 main 都没遇到 section → 孤儿
                if not in_part:
                    bad.append(n.get('id'))
            if bad:
                print(f'{ver}/{p.stem}: {bad}')

if __name__ == '__main__':
    main()
