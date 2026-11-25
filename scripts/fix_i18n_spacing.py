#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复 18 语翻译源稿的 ASCII 标点后缺空格（方案 W2）。

机翻流水线曾吞掉逗号/冒号后的空格（`markers,these`、`rush:sharpening`），
本脚本只碰散文：代码块、行内代码、HTML、URL、模板表达式、前置元数据不判；
数字千分位/时间、商品名（Termux:API）、chown user:group、堆栈
`at ... file:line` 记法都排除。少数"词内被塞逗号"（se,padan）直接还原成词。

用法：
    python scripts/fix_i18n_spacing.py            # 只报告，不改盘
    python scripts/fix_i18n_spacing.py --apply    # 写回 source/translations
    python scripts/fix_i18n_spacing.py --check    # CI 用：有缺陷即非零退出
"""

import argparse
import collections
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from bookkit import i18n as I  # noqa: E402


def _apply_words(text: str) -> tuple:
    n = 0
    for bad, good in I.WORD_FIXES.items():
        c = text.count(bad)
        if c:
            text = text.replace(bad, good)
            n += c
    return text, n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true', help='写回源稿')
    ap.add_argument('--check', action='store_true', help='有缺陷即退出 1（CI 门禁）')
    args = ap.parse_args()

    root = ROOT
    before = I.spacing_defects(root)
    counts = collections.Counter(d['lang'] for d in before)
    word_total = 0

    if args.apply:
        files = sorted({root / d['file'] for d in before})
        # 词内逗号先还原，再重扫（位置会变）
        for f in files:
            raw = f.read_text(encoding='utf-8')
            fixed, n = _apply_words(raw)
            if n:
                f.write_text(fixed, encoding='utf-8', newline='')
                word_total += n
        after_words = I.spacing_defects(root)
        by_file = collections.defaultdict(list)
        for d in after_words:
            by_file[root / d['file']].append(d)
        changed = 0
        for f, rows in by_file.items():
            lines = f.read_text(encoding='utf-8').split('\n')
            for d in sorted(rows, key=lambda x: (x['line'], x['col']), reverse=True):
                i = d['line'] - 1
                if i >= len(lines):
                    continue
                col = d['col'] - 1
                if lines[i][col:col + 1] != d['punct']:
                    continue          # 已被同批替换影响，跳过
                lines[i] = lines[i][:col + 1] + ' ' + lines[i][col + 1:]
                changed += 1
            f.write_text('\n'.join(lines), encoding='utf-8', newline='')
        after = I.spacing_defects(root)
        print(f'已修复：词内逗号 {word_total} 处；标点后加空格 {changed} 处')
    else:
        after = before

    counts_after = collections.Counter(d['lang'] for d in after)
    print(f'\n{"语言":6s} {"修复前":>6s} {"修复后":>6s}')
    for lang in sorted(set(counts) | set(counts_after)):
        print(f'{lang:6s} {counts.get(lang, 0):6d} {counts_after.get(lang, 0):6d}')
    print(f'{"合计":6s} {sum(counts.values()):6d} {sum(counts_after.values()):6d}')

    for d in after[:20]:
        print(f"  [{d['lang']}] {d['file']}:{d['line']}: {d['context']}")

    if args.check and after:
        return 1
    if not args.apply and after and not args.check:
        print('\n（未写盘；确认后加 --apply 修复）')
    return 0


if __name__ == '__main__':
    sys.exit(main())
