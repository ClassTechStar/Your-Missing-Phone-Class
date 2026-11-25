#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 44 章「2026 年末补记」注入 v1.9 的两个 HTML 副本。

只改 v1.9（无源稿体系）；v1.8 走 source/ 源稿不动。
注入点为每章 content-section div 的闭合标签之前，按偏移倒序插入以免失效。
用标记注释保证幂等：重复运行不会重复注入。

用法：
    python scripts/enrich_v19_dev.py            # 干跑，报告命中章节
    python scripts/enrich_v19_dev.py --apply    # 写盘
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

from v19_enrich_data_a import SECTIONS as A  # noqa: E402
from v19_enrich_data_b import SECTIONS as B  # noqa: E402

DATA = {**A, **B}
MARK = '<!-- v19-enrich-2026-11 -->'
SRC = ROOT / 'v1.9' / 'zh-CN.html'
DUP = ROOT / '你缺失的那门手机课V1.9Fixed.html'

TABLE_OPEN = ('<div class="overflow-x-auto">\n'
              '<table class="w-full border-collapse border border-gray-300 text-sm mb-3">\n')
TH = 'class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left"'
TD = 'class="border border-gray-300 dark:border-gray-600 px-3 py-2"'


def inline(t: str) -> str:
    """转义并把 `代码` 转成 <code>。"""
    t = html.escape(str(t), quote=False)
    return re.sub(r'`([^`]+)`', r'<code>\1</code>', t)


def render(d: dict) -> str:
    out = [MARK, f'<h4 class="text-lg font-semibold mt-4 mb-2">2026 年末补记 · {inline(d["h"])}</h4>']
    if d.get('p'):
        out.append(f'<p class="mb-3">{inline(d["p"])}</p>')
    if d.get('items'):
        out.append('<ul class="list-disc pl-6 mb-3 space-y-1">')
        for k, v in d['items']:
            out.append(f'  <li><strong>{inline(k)}</strong>：{inline(v)}</li>')
        out.append('</ul>')
    if d.get('table'):
        head, rows = d['table']
        out.append(TABLE_OPEN)
        out.append('<thead><tr class="bg-light dark:bg-gray-700">'
                   + ''.join(f'<th {TH}>{inline(c)}</th>' for c in head) + '</tr></thead>')
        out.append('<tbody>')
        for r in rows:
            out.append('<tr>' + ''.join(f'<td {TD}>{inline(c)}</td>' for c in r) + '</tr>')
        out.append('</tbody>\n</table>\n</div>')
    if d.get('note'):
        out.append('<div class="tip-box rounded-lg p-4 mb-3">'
                   '<p class="font-semibold"><i class="fas fa-lightbulb mr-2"></i>一句话记牢</p>'
                   f'<p class="mt-1">{inline(d["note"])}</p></div>')
    return '\n'.join(out) + '\n'


def bounds(s: str, cid: str):
    """返回 (章节 div 起始, 其闭合 </div> 起始)。"""
    i = s.find(f'id="{cid}" class="mb-10 content-section"')
    if i < 0:
        return None
    start = s.rfind('<div', 0, i)
    depth = 0
    for m in re.finditer(r'<div\b|</div>', s[start:]):
        if m.group().startswith('</'):
            depth -= 1
            if depth == 0:
                return start, start + m.start()
        else:
            depth += 1
    return None


def main():
    apply = '--apply' in sys.argv
    s = SRC.read_text(encoding='utf-8')
    if MARK in s:
        print('已注入过（检测到标记），跳过。')
        return 0

    all_ids = set(re.findall(r'id="([\w-]+)" class="mb-10 content-section"', s))
    hits = [(cid, d) for cid, d in DATA.items() if cid in all_ids]
    missing = [(cid, d) for cid, d in DATA.items() if cid not in all_ids]
    print(f'数据章节 {len(DATA)} 个，命中 {len(hits)} 个，未命中 {len(missing)} 个')
    if missing:
        print('  未命中:', [c for c, _ in missing])
    if len(hits) != 44:
        print(f'!! 预期 44 章，实际 {len(hits)} 章，请检查')
        return 1
    if not apply:
        print('（干跑，未写盘）')
        return 0

    inserts = []
    for cid, d in hits:
        b = bounds(s, cid)
        if not b:
            print(f'  !! 无法定位 {cid}')
            return 1
        inserts.append((b[1], render(d)))
    # 倒序插入，前面的偏移不受影响
    for pos, block in sorted(inserts, key=lambda x: x[0], reverse=True):
        s = s[:pos] + block + s[pos:]

    SRC.write_text(s, encoding='utf-8', newline='')
    DUP.write_text(s, encoding='utf-8', newline='')   # 两副本保持字节一致
    print(f'已注入 {len(inserts)} 章，写入两个 HTML 副本')
    return 0


if __name__ == '__main__':
    sys.exit(main())
