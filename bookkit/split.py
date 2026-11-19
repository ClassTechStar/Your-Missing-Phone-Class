"""split：分章化构建——每章一页 + 书首页 + sitemap/JSON-LD。

单文件 353.8 万字的 DOM 规模（约 8.8 万标签）在低端机上是白屏/锚点漂移
事故的根源；分章化让每页 DOM 缩小两个数量级，同时拿到章节级 URL
（SEO/分享），离线承诺由 Service Worker 的缓存策略继续承担。

产物（--out，默认 dist/site）：
  <out>/<version>/<lang>/index.html        书首页（全书目录 + Book JSON-LD）
  <out>/<version>/<lang>/<chapter-id>.html 章节页（单章 + 侧栏目录 + 上一章/下一章 + Chapter JSON-LD + canonical）
  <out>/sitemap.xml                        站点地图（首页 + 全部章节页）

页面由单文件构建产物按节点跨度精确切片而成（与 build 同源），
页间差异只在：目录/正文锚点改写为页链接、标题与 JSON-LD/canonical、
章节页裁掉书首页顶部区（hero/学习路径/仪表盘）。
"""

import json
import re
from pathlib import Path

from . import build as B
from . import htmlparse as H

# 分章页性能预算（manifest 版本级 budget 之外的页级护栏；分章化的目标口径）
PAGE_BUDGET = {"max_html_kb": 300, "max_dom_tags": 5000}

RE_TITLE = re.compile(r'<title>[\s\S]*?</title>')
RE_HREF = re.compile(r'href="#([\w:.-]+)"')
RE_STYLE = re.compile(r'<style[\s\S]*?</style>')
RE_SCRIPT = re.compile(r'<script(?![^>]*\bsrc=)[^>]*>[\s\S]*?</script>')
RE_SCRIPT_BODY = re.compile(r'<script[^>]*>([\s\S]*?)</script>')

# 单文件里的相对路径比站点根深一层，分章页再深一层
PATH_FIXES = [('../sw.js', '../../sw.js'),
              ('../manifest.webmanifest', '../../manifest.webmanifest'),
              ('../icons/', '../../icons/'),
              ('../announcements.json', '../../announcements.json'),
              ('../errata.html', '../../errata.html'),
              ('../languages.html', '../../languages.html')]

# SW 注册：脚本路径 + scope
RE_SW_REGISTER = re.compile(
    r"(navigator\.serviceWorker\.register\(\s*)(['\"])([^'\"]*sw\.js)\2"
    r"(\s*,\s*\{\s*scope:\s*)(['\"])([^'\"]*)\5")


def fix_sw_scope(html: str) -> str:
    """把 Service Worker 的 scope 对齐到 sw.js 所在目录。

    scope 必须覆盖 sw.js 脚本自身，否则浏览器直接拒绝注册
    （SecurityError: the script is not under the scope），离线阅读随之失效；
    而且注册失败只会被 .catch 里的 console.warn 吞掉，冒烟测试抓不到。
    脚本在站点根时 scope='./'，在 v1.9/ 时 '../'，在 v1.9/zh-CN/ 时 '../../'。
    """
    def sub(m):
        script = m.group(3)
        depth = script.count('/')          # 'sw.js'→0；'../sw.js'→1；'../../sw.js'→2
        scope = './' if depth == 0 else '../' * depth
        return (f'{m.group(1)}{m.group(2)}{script}{m.group(2)}'
                f'{m.group(4)}{m.group(5)}{scope}{m.group(5)}')
    return RE_SW_REGISTER.sub(sub, html)


def _externalize(page: str, assets: dict) -> str:
    """把大块 <style>/<script> 抽到共享资产（外置后浏览器跨页复用缓存）。"""
    def style_sub(m):
        inner = re.sub(r'^<style[^>]*>', '', m.group(0))
        inner = re.sub(r'</style>$', '', inner)
        assets['book.css'] = assets.get('book.css', '') + inner + '\n'
        return ''
    page = RE_STYLE.sub(style_sub, page)

    def script_sub(m):
        raw = m.group(0)
        body_m = RE_SCRIPT_BODY.match(raw)
        body = body_m.group(1) if body_m else ''
        if len(body) < 2048:          # 小脚本（no-js shim 等）保持内联
            return raw
        assets['book.js'] = assets.get('book.js', '') + body + '\n'
        return ''
    page = RE_SCRIPT.sub(script_sub, page)
    return page


def _book_chapter_order(book: dict) -> list:
    """章节阅读顺序 = book.json 的 chapters 顺序。"""
    return [c['id'] for c in book['chapters']]


def _id_page_map(tree, pos, chapter_spans: dict) -> dict:
    """所有 id → 所属页面（章节 id → 自身；区块内锚点 → 所在章节页；其余 → index）。"""
    idmap = {}
    for n in tree.find_all():
        nid = n.get('id')
        if not nid:
            continue
        sp = pos.get(id(n))
        if sp is None:
            continue
        owner = 'index'
        for cid, (s, e) in chapter_spans.items():
            if s <= sp[0] < e:
                owner = cid
                break
        idmap[nid] = owner
    return idmap


def _rewrite_hrefs(html: str, idmap: dict, page: str, part_ids=frozenset()) -> str:
    """把页内锚点改写为跨页链接；本页锚点（含每页都有的 #top）保持 #x。"""
    def sub(m):
        anchor = m.group(1)
        if anchor == 'top':
            return 'href="#top"'
        if anchor in part_ids:          # 篇锚点 → 该篇第一章页
            return f'href="{idmap.get(anchor, "index")}.html"'
        owner = idmap.get(anchor, 'index')
        if owner == page:
            return f'href="#{anchor}"'
        if anchor == owner:
            return f'href="{anchor}.html"'
        return f'href="{owner}.html#{anchor}"'
    return RE_HREF.sub(sub, html)


def _json_ld(data: dict) -> str:
    return ('<script type="application/ld+json">'
            + json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
            + '</script>')


def split(root: Path, lang: str = 'zh-CN', book_path: Path = None,
          out: Path = None) -> dict:
    book = B.load_book(root, book_path, lang)
    version = book.get('version') or 'v1.9'
    built = B.build(root, lang=lang, book_path=book_path)['html']

    tree = H.parse(built)
    pos = H.index_nodes(tree)

    # 各 content-section 的跨度（章节页切片边界）
    chapter_spans = {}
    for n in tree.find_all('div'):
        if 'content-section' in n.classes and n.get('id'):
            chapter_spans[n.get('id')] = pos[id(n)]

    # 头/尾与书首页顶部区（hero/学习路径/仪表盘，位于首个区块之前）
    blocks_start = min(s for s, _ in chapter_spans.values())
    blocks_end = max(e for _, e in chapter_spans.values())
    head, tail = built[:blocks_start], built[blocks_end:]

    top_start = head.find('class="breadcrumb')
    top_start = head.find('</nav>', top_start)
    top_start = (top_start + len('</nav>')) if top_start >= 0 else 0
    head_slim, top_matter = head[:top_start], head[top_start:]

    idmap = _id_page_map(tree, pos, chapter_spans)
    order = [cid for cid in _book_chapter_order(book) if cid in chapter_spans]

    # 篇锚点（#ji-chu-pian 等）在分章页没有对应节点，指向该篇第一章页
    part_first = {}
    for ch in book['chapters']:
        pid = ch.get('part') or ch.get('after_part')
        if pid and pid not in part_first and ch['id'] in chapter_spans:
            part_first[pid] = ch['id']
    idmap.update(part_first)

    # 章节元数据（标题取 front matter nav）
    meta = {}
    for ch in book['chapters']:
        m, _ = B._read_md(root, ch['file'])
        meta[ch['id']] = {'title': m.get('nav') or ch['id']}

    site = ((json.loads((root / 'manifest' / 'languages.json').read_text(encoding='utf-8'))
             .get('site_url') or '').rstrip('/'))

    out = Path(out) if out else (root / 'dist' / 'site')
    page_dir = out / version / lang
    page_dir.mkdir(parents=True, exist_ok=True)
    assets = {}

    def page_shell(slim_head: str, title: str, canonical: str, ld: dict) -> str:
        h = RE_TITLE.sub(f'<title>{title}</title>', slim_head, count=1)
        h = h.replace('</head>',
                      f'<link rel="canonical" href="{canonical}">\n'
                      f'{_json_ld(ld)}\n'
                      f'<link rel="stylesheet" href="assets/book.css">\n</head>', 1)
        return h

    book_title = book.get('title') or '你缺失的那门手机课'
    pages = {}
    budget_bad = []

    # 共享壳层一次性外置 CSS/JS 与路径改写（所有页共用同一套资产）
    assets = {}
    head_slim = _externalize(head_slim, assets)
    top_matter = _externalize(top_matter, assets)
    tail = _externalize(tail, assets)
    for a, b in PATH_FIXES:
        head_slim = head_slim.replace(a, b)
        top_matter = top_matter.replace(a, b)
        tail = tail.replace(a, b)
    # SW scope 必须在路径降级之后算：scope 要与降级后的 sw.js 路径同深
    head_slim = fix_sw_scope(head_slim)
    top_matter = fix_sw_scope(top_matter)
    tail = fix_sw_scope(tail)
    tail = tail.replace('</body>',
                        '<script src="assets/book.js" defer></script>\n</body>', 1)
    (page_dir / 'assets').mkdir(exist_ok=True)
    for name, body in assets.items():
        for a, b in PATH_FIXES:      # 外置 JS 里的相对路径同样要降级
            body = body.replace(a, b)
        body = fix_sw_scope(body)
        (page_dir / 'assets' / name).write_text(body, encoding='utf-8', newline='\n')

    # 输出根 = 可直接部署的自包含站点树：补齐 PWA 资产（sw/manifest/图标/公告）
    # 以及勘误页与语言分级页（章末「报告错误」入口指向它们）
    import shutil
    for fname in ('sw.js', 'manifest.webmanifest', 'announcements.json',
                  'errata.html', 'languages.html'):
        src = root / fname
        if src.is_file():
            shutil.copy2(src, out / fname)
    if (root / 'icons').is_dir():
        if (out / 'icons').exists():
            shutil.rmtree(out / 'icons')
        shutil.copytree(root / 'icons', out / 'icons')

    def emit(name: str, html: str):
        (page_dir / name).write_text(html, encoding='utf-8', newline='\n')
        kb = len(html.encode('utf-8')) // 1024
        tags = len(re.findall(r'<[a-zA-Z][\w:-]*', html))
        pages[name] = (kb, tags)
        if kb > PAGE_BUDGET['max_html_kb'] or tags > PAGE_BUDGET['max_dom_tags']:
            budget_bad.append((name, kb, tags))
    # ---- 书首页：顶部区 + 全书目录 ----
    toc_lines = ['<section class="mb-12"><h2 class="text-2xl font-bold text-dark dark:text-gray-200 '
                 'mb-6 pb-2 border-b-2 border-primary">全书目录</h2>']
    for ch in book['chapters']:
        cid = ch['id']
        if cid not in chapter_spans:
            continue
        t = meta[cid]['title']
        toc_lines.append(f'<p class="mb-2"><a href="{cid}.html" '
                         f'class="text-primary hover:underline">{t}</a></p>')
    toc_lines.append('</section>')
    idx_url = f'{site}/{version}/{lang}/index.html' if site else ''
    idx_head = page_shell(head_slim, f'{book_title} · {version}',
                          idx_url,
                          {"@context": "https://schema.org", "@type": "Book",
                           "name": book_title, "inLanguage": lang,
                           "url": idx_url, "hasPart": len(order)})
    emit('index.html', _rewrite_hrefs(
        idx_head + top_matter + '\n' + '\n'.join(toc_lines) + tail,
        idmap, 'index', frozenset(part_first)))

    # ---- 章节页 ----
    for i, cid in enumerate(order):
        s, e = chapter_spans[cid]
        body = built[s:e]
        # 正文里的相对路径同样要降级（章末勘误入口 ../errata.html → ../../errata.html）
        for a, b in PATH_FIXES:
            body = body.replace(a, b)
        prev_id = order[i - 1] if i > 0 else None
        next_id = order[i + 1] if i + 1 < len(order) else None
        nav_bits = []
        if prev_id:
            nav_bits.append(f'<a href="{prev_id}.html" class="text-primary hover:underline">'
                            f'← {meta[prev_id]["title"]}</a>')
        if next_id:
            nav_bits.append(f'<a href="{next_id}.html" class="text-primary hover:underline">'
                            f'{meta[next_id]["title"]} →</a>')
        prevnext = ('\n<nav class="flex flex-wrap justify-between gap-4 mt-10 mb-6">'
                    + '<span></span>'.join(nav_bits) + '</nav>')
        title = f'{meta[cid]["title"]} · {book_title}'
        url = f'{site}/{version}/{lang}/{cid}.html' if site else ''
        ld = {"@context": "https://schema.org", "@type": "Chapter",
              "name": meta[cid]['title'], "url": url,
              "isPartOf": {"@type": "Book", "name": book_title, "inLanguage": lang}}
        page = page_shell(head_slim, title, url, ld) + '\n' + body + prevnext + tail
        page = _rewrite_hrefs(page, idmap, cid, frozenset(part_first))
        emit(f'{cid}.html', page)

    # ---- sitemap ----
    if site:
        urls = [f'{site}/{version}/{lang}/index.html'] + \
               [f'{site}/{version}/{lang}/{cid}.html' for cid in order]
        sm = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
        sm += [f'  <url><loc>{u}</loc></url>' for u in urls]
        sm.append('</urlset>')
        (out / 'sitemap.xml').write_text('\n'.join(sm) + '\n', encoding='utf-8', newline='\n')

    return {'version': version, 'lang': lang, 'pages': len(pages),
            'out': str(page_dir), 'budget': PAGE_BUDGET,
            'over_budget': budget_bad,
            'page_stats': pages}
