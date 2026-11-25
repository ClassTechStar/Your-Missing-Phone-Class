#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复翻译源稿里两处「尾巴被烤进错误文件」的提取缺陷。

缺陷 1：模板 {{BODY}} 之后的残留
---------------------------------
source/translations/*/template/shell.html 在生成时把最后一章的尾巴烤进了模板：
{{BODY}} 后面粘着一段正文残片 + 若干闭合标签（</p> </div> </div> </section>）。
zh-CN 模板是干净的。后果：构建产物末尾重复出现这段残片，且多出闭合标签。

缺陷 2：附录篇文件吞掉了整个附录
---------------------------------
source/translations/*/parts/10-fu-lu.md 正常应该只有篇首语（13 行，与 zh-CN/en 一致），
但 12 种语言的文件有 587 行 —— 把附录 A~H 全部内容也吞了进去。
而 book.json 里这些章节又是单独编排的，于是**整个附录被渲染两遍**
（一遍带 id、一遍不带 id，构建产物多出 8 个无 id 的 content-section）。

用法：
    python scripts/fix_templates.py            # 干跑
    python scripts/fix_templates.py --apply    # 写盘
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ZH = ROOT / 'source' / 'template' / 'shell.html'
TEMPLATES = sorted((ROOT / 'source' / 'translations').glob('*/template/shell.html'))
PART_NAME = '10-fu-lu.md'
# 正确的篇文件结构：frontmatter(7) + {class=...} + ## 标题 + {class=导读} + 导读正文
PART_KEEP_LINES = 13


# ---------------------------------------------------------------- 缺陷 1

def clean_template(text: str):
    """返回 (清理后文本, 被删除的行数, 残片预览)；无需修复时返回 (None, 0, 原因)。"""
    lines = text.splitlines(keepends=True)
    idx = next((i for i, l in enumerate(lines) if '{{BODY}}' in l), None)
    if idx is None:
        return None, 0, '未找到 {{BODY}}'
    line = lines[idx]
    tail = line.split('{{BODY}}', 1)[1]
    if not tail.strip():
        return None, 0, '已是干净的'
    frag = tail.strip()[:60]
    lines[idx] = line.split('{{BODY}}', 1)[0] + '{{BODY}}\n'
    removed = 0
    j = idx + 1
    while j < len(lines):
        cur = lines.pop(j)
        removed += 1
        if '</section>' in cur:
            break
    return ''.join(lines), removed, frag


# ---------------------------------------------------------------- 缺陷 2

def clean_part(text: str):
    """把篇文件截到「篇首语」为止。返回 (新文本, 删除行数, 说明)。

    正向判定：被删的第一行必须是 `::: div`（被吞进来的附录正文以它开头），
    而不是靠「末行是否有句号」判断 —— 泰文等语言句末常无标点。
    """
    lines = text.splitlines(keepends=True)
    if len(lines) <= PART_KEEP_LINES:
        return None, 0, f'已正常（{len(lines)} 行）'
    head = ''.join(lines[:PART_KEEP_LINES])
    if '{class="chapter-intro' not in head:
        return None, 0, '结构与预期不符，跳过'
    # 待删部分的第一行非空内容（篇首语后可能还有空行）
    first_removed = next((l.strip() for l in lines[PART_KEEP_LINES:] if l.strip()), '')
    if not first_removed.startswith('::: div'):
        return None, 0, f'待删首行不是 ::: div（{first_removed[:24]!r}），跳过'
    return head, len(lines) - PART_KEEP_LINES, f'{len(lines)} 行 → {PART_KEEP_LINES} 行'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()
    changed = 0

    print('缺陷 1：模板 {{BODY}} 残留')
    for p in [ZH] + TEMPLATES:
        rel = p.relative_to(ROOT)
        new, n, frag = clean_template(p.read_text(encoding='utf-8'))
        if new is None:
            print(f'  · {rel}: {frag}')
            continue
        print(f'  OK {rel}: 删除 {n} 行，残片 = {frag!r}')
        changed += 1
        if args.apply:
            p.write_text(new, encoding='utf-8', newline='')

    print('\n缺陷 2：附录篇文件吞掉正文')
    for p in sorted((ROOT / 'source' / 'translations').glob(f'*/parts/{PART_NAME}')):
        rel = p.relative_to(ROOT)
        new, n, why = clean_part(p.read_text(encoding='utf-8'))
        if new is None:
            print(f'  · {rel}: {why}')
            continue
        print(f'  OK {rel}: {why}')
        changed += 1
        if args.apply:
            p.write_text(new, encoding='utf-8', newline='')

    print(f'\n待修复 {changed} 处' + ('（已写盘）' if args.apply else '（干跑，未写盘）'))
    if not args.apply:
        return

    print('\n自检 1：模板 div 开闭平衡')
    bad = 0
    for p in [ZH] + TEMPLATES:
        t = p.read_text(encoding='utf-8')
        o, c = len(re.findall(r'<div\b', t)), len(re.findall(r'</div>', t))
        if o != c:
            bad += 1
            print(f'  !! {p.relative_to(ROOT)}: 开{o} 闭{c}')
    print('  全部平衡' if not bad else f'  {bad} 个仍不平衡')

    print('自检 2：篇文件行数')
    bad2 = 0
    for p in sorted((ROOT / 'source' / 'translations').glob(f'*/parts/{PART_NAME}')):
        n = len(p.read_text(encoding='utf-8').splitlines())
        if n > PART_KEEP_LINES:
            bad2 += 1
            print(f'  !! {p.relative_to(ROOT)}: {n} 行')
    print('  全部正常' if not bad2 else f'  {bad2} 个仍超长')
    if bad or bad2:
        sys.exit(1)


if __name__ == '__main__':
    main()
