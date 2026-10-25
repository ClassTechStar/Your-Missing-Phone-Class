#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 v1.8/zh-CN.html 同步到 GitHub Pages 站点仓库（Yihggh.github.io）。

站点根目录与本书 `v1.8/` 目录层级不同：
    书页  <站点根>/v1.8/zh-CN.html   →  ../sw.js  ../manifest.webmanifest  ../icons/
    站点  <站点根>/index.html        →   sw.js     manifest.webmanifest     icons/
所以复制时必须把这三处相对路径降一级，否则 Service Worker 注册 404、
manifest 与图标全不可达（PWA 静默失效）。

用法：
    python scripts/sync_site.py                       # 用默认站点路径
    python scripts/sync_site.py --dest <站点仓库路径>
    python scripts/sync_site.py --dry-run             # 只报告不写盘
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DEST = Path.home() / 'Documents' / 'GitHub' / 'Yihggh.github.io'
# 站点根要带的 PWA 资产
ASSETS = ['sw.js', 'manifest.webmanifest']
ASSET_DIRS = ['icons']

# 书页 → 站点根，路径降一级
REWRITES = [
    ('../sw.js', 'sw.js'),
    ('../manifest.webmanifest', 'manifest.webmanifest'),
    ('../icons/', 'icons/'),
]


def rewrite(html: str) -> str:
    for a, b in REWRITES:
        html = html.replace(a, b)
    return html


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dest', type=Path, default=DEFAULT_DEST)
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()
    dest = args.dest

    if not (dest / '.git').is_dir():
        print(f'目标不是 git 仓库：{dest}')
        return 1

    src_html = ROOT / 'v1.8' / 'zh-CN.html'
    if not src_html.is_file():
        print(f'源文件缺失：{src_html}')
        return 1

    html = rewrite(src_html.read_text(encoding='utf-8'))
    left = [a for a, _ in REWRITES if a in html]
    if left:
        print(f'!! 仍有未降级的相对路径：{left}')
        return 1

    plan = [('index.html', f'{len(html):,} 字符')]
    for a in ASSETS:
        if not (ROOT / a).is_file():
            print(f'!! 缺少资产：{a}')
            return 1
        plan.append((a, '复制'))
    for d in ASSET_DIRS:
        n = len(list((ROOT / d).glob('*'))) if (ROOT / d).is_dir() else 0
        plan.append((d + '/', f'{n} 个文件'))

    for name, note in plan:
        print(f'  → {name:24s} {note}')
    if args.dry_run:
        print('（dry-run，未写盘）')
        return 0

    (dest / 'index.html').write_text(html, encoding='utf-8', newline='')
    for a in ASSETS:
        shutil.copy2(ROOT / a, dest / a)
    for d in ASSET_DIRS:
        tgt = dest / d
        if tgt.exists():
            shutil.rmtree(tgt)
        shutil.copytree(ROOT / d, tgt)

    # 自检：站点 index.html 里不能再出现 ../
    out = (dest / 'index.html').read_text(encoding='utf-8')
    bad = [a for a, _ in REWRITES if a in out]
    if bad:
        print(f'!! 写盘后仍有未降级路径：{bad}')
        return 1
    print(f'\n已同步到 {dest}')
    print('下一步：git add -A && git commit && git push（走 SSH，见维护手册）')
    return 0


if __name__ == '__main__':
    sys.exit(main())
