#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把剩余 76 章的「2026 年末补记」注入 v1.9 的两个 HTML 副本。

上一轮（enrich_v19_dev.py）已给 44 章开发篇注入补记；本轮补齐其余 76 章，
使全书 120 个 content-section 全部有补记。数据分四个文件：
  v19_enrich_data_c1.py  序号 1–20    第 0–15 章
  v19_enrich_data_c2.py  序号 21–42   第 17–36 章
  v19_enrich_data_d.py   序号 87–111  第 81–105 章（v1.9 新增、原本最薄）
  v19_enrich_data_e.py   序号 112–120 附录 A–H 与结语

注入点为每章 content-section div 的闭合标签之前，按偏移倒序插入。
用独立标记注释保证幂等，且不会与上一轮的 44 章补记冲突。

用法：
    python scripts/enrich_v19_all.py            # 干跑
    python scripts/enrich_v19_all.py --apply    # 写盘
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

from v19_enrich_data_c1 import SECTIONS as C1  # noqa: E402
from v19_enrich_data_c2 import SECTIONS as C2  # noqa: E402
from v19_enrich_data_d import SECTIONS as D  # noqa: E402
from v19_enrich_data_e import SECTIONS as E  # noqa: E402

DATA = {**C1, **C2, **D, **E}
MARK = '<!-- v19-enrich-all-2026-11 -->'
SRC = ROOT / 'v1.9' / 'zh-CN.html'
DUP = ROOT / '你缺失的那门手机课V1.9Fixed.html'

TABLE_OPEN = ('<div class="overflow-x-auto">\n'
              '<table class="w-full border-collapse border border-gray-300 text-sm mb-3">\n')
TH = 'class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left"'
TD = 'class="border border-gray-300 dark:border-gray-600 px-3 py-2"'


def inline(t: str) -> str:
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


def already_enriched(s: str, cid: str) -> bool:
    """该章是否已有任一补记（上一轮的 44 章或本轮）。"""
    b = bounds(s, cid)
    if not b:
        return False
    return '2026 年末补记' in s[b[0]:b[1]]


def main():
    apply = '--apply' in sys.argv
    s = SRC.read_text(encoding='utf-8')
    if MARK in s:
        print('已注入过（检测到本轮标记），跳过。')
        return 0

    all_ids = re.findall(r'id="([\w-]+)" class="mb-10 content-section"', s)
    idset = set(all_ids)
    print(f'全书带 id 区块: {len(all_ids)} 个')
    print(f'已有补记: {sum(1 for c in all_ids if already_enriched(s, c))} 个')
    print(f'本轮数据章节: {len(DATA)} 个')

    missing = [c for c in DATA if c not in idset]
    dup_ = [c for c in DATA if c in idset and already_enriched(s, c)]
    todo = [c for c in DATA if c in idset and not already_enriched(s, c)]
    print(f'  未命中 {len(missing)} / 已有补记而跳过 {len(dup_)} / 待注入 {len(todo)}')
    if missing:
        print('  未命中:', missing[:6])
    if len(missing) or len(dup_):
        print('!! 数据与实际章节不一致，请检查后再执行')
        return 1
    if len(todo) != 76:
        print(f'!! 预期补齐 76 章，实际 {len(todo)} 章')
        return 1

    # 校验：注入完成后应当 120/120 章都有补记
    expected = set(all_ids) - set(todo)
    print(f'注入后覆盖: {len(expected)}（已有）+ {len(todo)}（本轮）= {len(expected) + len(todo)} / {len(all_ids)}')
    if not apply:
        print('（干跑，未写盘）')
        return 0

    inserts = []
    for cid in todo:
        b = bounds(s, cid)
        if not b:
            print(f'  !! 无法定位 {cid}')
            return 1
        inserts.append((b[1], render(DATA[cid])))
    for pos, block in sorted(inserts, key=lambda x: x[0], reverse=True):
        s = s[:pos] + block + s[pos:]

    SRC.write_text(s, encoding='utf-8', newline='')
    DUP.write_text(s, encoding='utf-8', newline='')
    print(f'已注入 {len(inserts)} 章，写入两个 HTML 副本')
    return 0


if __name__ == '__main__':
    sys.exit(main())
