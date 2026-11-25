#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""为全部 19 种语言构建分章站点（方案 W3-4）。

zh-CN 用 v1.9 源稿（120 章）；其余 18 语用 source/translations/<lang>/book.json
（v1.8，84 章）。产物：

    dist/site/v1.9/zh-CN/…       中文分章页
    dist/site/v1.8/<lang>/…      18 语分章页（每章 ≤300KB/5000 标签）
    dist/site/sitemap.xml        合并后的全语言 sitemap

此前只有中文分章，外语读者仍要下载 1–2.6MB 单体页；本脚本把
bookkit split 的页级预算门禁铺到全部语言，并让 sitemap 覆盖外语章页。

用法：
    python scripts/build_all_sites.py                 # 全量构建
    python scripts/build_all_sites.py --strict-budget # 超页级预算即失败（CI）
    python scripts/build_all_sites.py --langs en ja   # 只构建指定语言
"""

import argparse
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from bookkit import split as S  # noqa: E402


def jobs():
    out = [('zh-CN', ROOT / 'source' / 'v1.9' / 'book.json')]
    trans = ROOT / 'source' / 'translations'
    for d in sorted(p for p in trans.iterdir() if p.is_dir()):
        bp = d / 'book.json'
        if bp.is_file():
            out.append((d.name, bp))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', type=Path, default=ROOT / 'dist' / 'site')
    ap.add_argument('--strict-budget', action='store_true',
                    help='任一页超出 300KB/5000 标签即失败')
    ap.add_argument('--langs', nargs='*', help='只构建指定语言（默认全部 19 种）')
    args = ap.parse_args()

    if args.out.exists():
        shutil.rmtree(args.out)

    mf = json.loads((ROOT / 'manifest' / 'languages.json').read_text(encoding='utf-8'))
    site = (mf.get('site_url') or '').rstrip('/')
    selected = set(args.langs) if args.langs else None

    urls, over_budget, bad_canon = [], [], []
    total_pages = 0
    for lang, book_path in jobs():
        if selected and lang not in selected:
            continue
        result = S.split(ROOT, lang, book_path, args.out, write_sitemap=False)
        urls += result['urls']
        over_budget += [(lang, *row) for row in result['over_budget']]
        bad_canon += [(lang, *row) for row in result['bad_canonical']]
        total_pages += result['pages']
        print(f"  {lang:6s} {result['pages']:4d} 页  "
              f"{result['version']}/{lang}  "
              f"{'超预算 ' + str(len(result['over_budget'])) if result['over_budget'] else ''}")

    if site:
        top = [f'{site}/', f'{site}/errata.html', f'{site}/languages.html',
               f'{site}/quiz.html', f'{site}/pdf.html',
               f'{site}/v1.9/zh-CN/', f'{site}/v1.9/zh-CN.html']
        urls = list(dict.fromkeys(top + urls))
        sm = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
        sm += [f'  <url><loc>{u}</loc></url>' for u in urls]
        sm.append('</urlset>')
        (args.out / 'sitemap.xml').write_text('\n'.join(sm) + '\n',
                                              encoding='utf-8', newline='\n')
        print(f'  sitemap: {len(urls)} 条 URL')

    print(f'共 {total_pages} 页 → {args.out}')
    if bad_canon:
        print(f'!! canonical 异常 {len(bad_canon)} 页：{bad_canon[:5]}')
        return 1
    if over_budget:
        print(f'!! 超页级预算 {len(over_budget)} 页：{over_budget[:8]}')
        return 1 if args.strict_budget else 0
    if args.strict_budget:
        print('OK: 全部语言页级预算通过（≤300KB / ≤5000 标签）')
    return 0


if __name__ == '__main__':
    sys.exit(main())
