#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""site_lint.py — 站点基建核对（优化方案 §9）。

用法: python scripts/site_lint.py（需先 python -m bookkit split 生成 dist/site）
退出码: 0 全过 / 1 有失败项

检查项（对应方案 §9「站点基建 lint」与「死链检查」两行）：
  1. robots.txt 存在，Sitemap 坐标 = manifest site_url + sitemap.xml
  2. sitemap 覆盖：每种语言至少 1 个入口；路径页齐全；每条 URL 可映射到真实文件（无死链）
  3. OG 每章唯一：og:title/og:description/og:url/og:type=article 各恰 1 条
  4. prefetch：第 N 章的 prefetch 必须指向第 N+1 章
  5. hreflang：每条备选去掉 fragment 后可达
  6. 勘误页时效公示：公示条数 = 已修条目数，日期可解析
  7. 章节页内链死链检查：页内 href="*.html" 都指向存在的页面
"""
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE_DIR = ROOT / 'dist' / 'site'
PAGE_DIR = SITE_DIR / 'v1.9' / 'zh-CN'


def main() -> int:
    failures = []
    mf = json.loads((ROOT / 'manifest' / 'languages.json').read_text(encoding='utf-8'))
    site = (mf.get('site_url') or '').rstrip('/')
    book = json.loads((ROOT / 'source' / 'v1.9' / 'book.json').read_text(encoding='utf-8'))
    order = [c['id'] for c in book['chapters']]
    langs = mf.get('languages', {})

    def fail(msg):
        failures.append(f'[FAIL] {msg}')

    # ---- 1. robots.txt ----
    robots = ROOT / 'robots.txt'
    if not robots.is_file():
        fail('robots.txt 不存在（搜索引擎入口，方案 §6.4）')
    else:
        rt = robots.read_text(encoding='utf-8')
        if f'Sitemap: {site}/sitemap.xml' not in rt:
            fail(f'robots.txt 的 Sitemap 坐标应为 {site}/sitemap.xml')
        if 'Allow: /' not in rt:
            fail('robots.txt 缺少 Allow: /')

    # ---- 2. sitemap 覆盖与可达 ----
    sm = SITE_DIR / 'sitemap.xml'
    if not sm.is_file():
        fail('dist/site/sitemap.xml 不存在（先运行 python -m bookkit split）')
    else:
        locs = re.findall(r'<loc>([^<]+)</loc>', sm.read_text(encoding='utf-8'))
        if len(locs) != len(set(locs)):
            fail('sitemap 含重复 URL')
        # 每种语言至少 1 个入口
        missing_lang = [c for c in langs
                        if (ROOT / 'v1.8' / f'{c}.html').is_file()
                        and f'{site}/v1.8/{c}.html' not in locs]
        if missing_lang:
            fail(f'sitemap 缺语言入口: {missing_lang}')
        # 路径页
        for p in json.loads((ROOT / 'manifest' / 'path.json').read_text(encoding='utf-8')):
            if f'{site}/v1.9/zh-CN/{p["id"]}.html' not in locs:
                fail(f'sitemap 缺路径页 {p["id"]}')
        # 每条 URL 可映射到真实文件（死链检查）。
        # v1.8/ 下既有仓库里的单文件（v1.8/en.html），也有构建出的分章页
        # （v1.8/en/di-yi-zhang.html），两处都要找。
        for u in locs:
            rel = u[len(site):].lstrip('/')
            if not rel:                       # 站点根 = 落地页
                ok = (ROOT / 'site-landing.html').is_file()
            elif rel.endswith('/'):           # 目录 URL = 目录下的 index.html
                ok = ((SITE_DIR / rel / 'index.html').is_file()
                      or (ROOT / rel / 'index.html').is_file())
            else:
                ok = (SITE_DIR / rel).is_file() or (ROOT / rel).is_file()
            if not ok:
                fail(f'sitemap 死链: {u}')

    # ---- 3/4/5/7. 章节页：OG 唯一、prefetch、hreflang、内链 ----
    if PAGE_DIR.is_dir():
        files = sorted(p for p in PAGE_DIR.glob('*.html'))
        names = {p.name for p in files}
        for i, cid in enumerate(order):
            f = PAGE_DIR / f'{cid}.html'
            if not f.is_file():
                fail(f'章节页缺失: {cid}.html')
                continue
            h = f.read_text(encoding='utf-8')
            for prop in ('og:title', 'og:description', 'og:url'):
                n = len(re.findall(r'<meta property="%s"' % prop, h))
                if n != 1:
                    fail(f'{cid}.html: {prop} 有 {n} 条（应恰 1）')
            if 'content="article"' not in h:
                fail(f'{cid}.html: og:type 不是 article')
            m = re.search(r'<link rel="prefetch" href="([^"]+)"', h)
            want = f'{order[i + 1]}.html' if i + 1 < len(order) else None
            got = m.group(1) if m else None
            if got != want:
                fail(f'{cid}.html: prefetch={got} 应为 {want}')
            for code, url in re.findall(
                    r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"', h):
                target = url.split('#')[0][len(site):].lstrip('/')
                ok = (SITE_DIR / target).is_file() or (ROOT / target).is_file()
                if not ok:
                    fail(f'{cid}.html: hreflang={code} 指向不存在的 {url}')
            for href in re.findall(r'href="([^"#?][^"]*\.html)[^"]*"', h):
                if href.startswith(('http://', 'https://')):
                    continue
                if href not in names and not (PAGE_DIR / href).is_file():
                    fail(f'{cid}.html: 内链死链 {href}')
    else:
        fail('dist/site/v1.9/zh-CN/ 不存在（先运行 python scripts/build_all_sites.py）')

    # ---- 8. 外语分章页覆盖（W3-4）----
    # 18 语各 84 章：目录页、章页、sitemap 三处都要在，且首页 canonical 自指。
    trans = ROOT / 'source' / 'translations'
    n_foreign = 0
    if sm.is_file() and trans.is_dir():
        locs_set = set(re.findall(r'<loc>([^<]+)</loc>', sm.read_text(encoding='utf-8')))
        for d in sorted(p for p in trans.iterdir() if p.is_dir()):
            bp = d / 'book.json'
            if not bp.is_file():
                continue
            ids = [c['id'] for c in json.loads(bp.read_text(encoding='utf-8'))['chapters']]
            page_dir = SITE_DIR / 'v1.8' / d.name
            if not (page_dir / 'index.html').is_file():
                fail(f'{d.name}: 缺分章目录页 v1.8/{d.name}/index.html')
                continue
            missing = [cid for cid in ids if not (page_dir / f'{cid}.html').is_file()]
            if missing:
                fail(f'{d.name}: 缺 {len(missing)} 个章页（如 {missing[:3]}）')
            for u in [f'{site}/v1.8/{d.name}/index.html'] + \
                     [f'{site}/v1.8/{d.name}/{cid}.html' for cid in ids]:
                if u not in locs_set:
                    fail(f'{d.name}: sitemap 缺章页 {u}')
            h = (page_dir / f'{ids[0]}.html').read_text(encoding='utf-8')
            tags = re.findall(r'<link rel="canonical" href="([^"]+)"', h)
            want = f'{site}/v1.8/{d.name}/{ids[0]}.html'
            if tags != [want]:
                fail(f'{d.name}: 章页 canonical 应为 {want}，实际 {tags[:2]}')
            kb = len(h.encode('utf-8')) // 1024
            if kb > 300:
                fail(f'{d.name}: 章页 {ids[0]}.html 为 {kb}KB（超 300KB 预算）')
            for code, url in re.findall(
                    r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"', h):
                target = url.split('#')[0][len(site):].lstrip('/')
                if not ((SITE_DIR / target).is_file() or (ROOT / target).is_file()):
                    fail(f'{d.name}/{ids[0]}.html: hreflang={code} 指向不存在的 {url}')
            n_foreign += len(ids) + 1

    # ---- 6. 勘误页时效公示 ----
    errata = (ROOT / 'errata.html').read_text(encoding='utf-8')
    fixed = len(re.findall(r'<span class="tag ok">已修</span>', errata))
    m = re.search(r'累计已处理 <b>(\d+)</b> 条勘误 · 最近修订 <b>([\d-]+)</b>', errata)
    if not m:
        fail('errata.html 缺时效公示块（方案 §8-1）')
    else:
        if int(m.group(1)) != fixed:
            fail(f'勘误公示条数 {m.group(1)} ≠ 已修条目数 {fixed}')
        try:
            date.fromisoformat(m.group(2))
        except ValueError:
            fail(f'勘误最近修订日期不可解析: {m.group(2)}')

    if failures:
        print('\n'.join(failures))
        print(f'\n共 {len(failures)} 处站点基建问题')
        return 1
    print(f'OK: robots/sitemap/OG/prefetch/hreflang/勘误公示/内链全部通过'
          f'（中文 {len(list(PAGE_DIR.glob("*.html")))} 页 + 外语 {n_foreign} 页）')
    return 0


if __name__ == '__main__':
    sys.exit(main())
