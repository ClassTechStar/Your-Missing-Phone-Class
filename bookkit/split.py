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
from html import escape as _esc
from pathlib import Path

from . import build as B
from . import htmlparse as H

# 分章页性能预算（manifest 版本级 budget 之外的页级护栏；分章化的目标口径）
PAGE_BUDGET = {"max_html_kb": 300, "max_dom_tags": 5000}

RE_TITLE = re.compile(r'<title>[\s\S]*?</title>')
RE_HREF = re.compile(r'href="#([\w:.-]+)"')
RE_CANONICAL = re.compile(r'\s*<link rel="canonical"[^>]*>')
RE_STYLE = re.compile(r'<style[\s\S]*?</style>')
RE_SCRIPT = re.compile(r'<script(?![^>]*\bsrc=)[^>]*>[\s\S]*?</script>')
RE_SCRIPT_BODY = re.compile(r'<script[^>]*>([\s\S]*?)</script>')
# 单文件专用的整章懒渲染样式（方案 §5.1）：分章页每页只有一章、本来就秒出，
# 不需要此规则，反而带来正文占位高度的布局风险，生成章节页前剥掉。
RE_SINGLEFILE_STYLE = re.compile(r'<style id="singlefile-lazy">[\s\S]*?</style>')

# 单文件里的相对路径比站点根深一层，分章页再深一层。
# 字体例外：章节页把字体随页面树复制到 <page>/fonts/，HTML 里的预加载链接
# （href= 形式）要降到页内；CSS 里的 url('../fonts/…') 相对 assets/ 解析
# 本来就是对的，所以这里只匹配 href= 前缀，不动 url()。
PATH_FIXES = [('../sw.js', '../../sw.js'),
              ('../manifest.webmanifest', '../../manifest.webmanifest'),
              ('../icons/', '../../icons/'),
              ('../announcements.json', '../../announcements.json'),
              ('../errata.html', '../../errata.html'),
              ('../languages.html', '../../languages.html'),
              ('href="../fonts/', 'href="fonts/')]

# SW 注册：脚本路径 + scope
RE_SW_REGISTER = re.compile(
    r"(navigator\.serviceWorker\.register\(\s*)(['\"])([^'\"]*sw\.js)\2"
    r"(\s*,\s*\{\s*scope:\s*)(['\"])([^'\"]*)\5")

# ---- 章节级分享卡（方案 §6.2）----
# 章首导读 = 带 chapter-intro class 的段落（class 在 <p> 自身或外层 div 上）
RE_INTRO_P = re.compile(r'<p[^>]*class="chapter-intro[^"]*"[^>]*>([\s\S]*?)</p>')
RE_DIV_INTRO_P = re.compile(r'class="chapter-intro[^"]*"[\s\S]*?<p[^>]*>([\s\S]*?)</p>')
RE_FIRST_P = re.compile(r'<p[^>]*>([\s\S]*?)</p>')
RE_META_OG = {p: re.compile(r'(<meta property="%s" content=")[^"]*(")' % p)
              for p in ('og:title', 'og:description', 'og:type')}


def og_description(body: str) -> str:
    """章节分享描述 = 章首导读第一句（方案 §6.2「{本章导览首句或 60 字导读}」）。

    微信分享卡片此前全站共用一句通用文案，第 22 章分享出去没有章节信息；
    这里从章首 chapter-intro 段落取第一句（兜底：正文第一个 <p>），超长截断。
    """
    m = (RE_INTRO_P.search(body) or RE_DIV_INTRO_P.search(body)
         or RE_FIRST_P.search(body))
    if not m:
        return ''
    text = re.sub(r'<[^>]+>', '', m.group(1))
    text = re.sub(r'\s+', ' ', text).strip()
    for i, ch in enumerate(text):
        if ch in '。！？':
            text = text[:i + 1]
            break
    return (text[:78] + '…') if len(text) > 80 else text


def _set_og(html: str, og: dict) -> str:
    """章节页 OG 覆盖：og:title=章标题、og:description=导读首句、
    og:type=article、og:url=章节 URL。缺的标签就地补在 og:type 之前。"""
    for prop, content in og.items():
        if not content or prop == 'og:url':
            continue
        rx = RE_META_OG.get(prop)
        if rx and rx.search(html):
            html = rx.sub(lambda m, c=_esc(content, quote=True): m.group(1) + c + m.group(2),
                          html, count=1)
    if og.get('og:url') and 'property="og:url"' not in html:
        html = html.replace('<meta property="og:type"',
                            f'<meta property="og:url" content="{og["og:url"]}">'
                            f'<meta property="og:type"', 1)
    return html


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


def hreflang_block(alts: dict, x_default: str = '') -> str:
    """hreflang 互链块（方案 §6.3）：同一内容的各语言入口互链；不足 2 个不发。

    hreflang 语义要求互为翻译的等价页面，孤零零一条自我标注没有意义，
    所以备选不足时整块省略，等译文页面落地自然出现。
    """
    if len(alts) < 2:
        return ''
    lines = [f'<link rel="alternate" hreflang="{code}" href="{url}">'
             for code, url in alts.items()]
    if x_default:
        lines.append(f'<link rel="alternate" hreflang="x-default" href="{x_default}">')
    return '\n'.join(lines) + '\n'


def load_paths(root: Path, chapter_ids) -> list:
    """策展路径（方案 §7）：manifest/path.json 只存章 ID 与编辑定的文案，
    章标题/导读构建时从源稿取——零内容复制、零翻译分叉。

    章 ID 不在本书里直接报错（构建门禁），不静默跳过：路径是编辑决策，
    拼错 id 静默消失会让「给爸妈的 10 章」悄悄变成 9 章。
    """
    f = root / 'manifest' / 'path.json'
    if not f.is_file():
        return []
    paths = json.loads(f.read_text(encoding='utf-8'))
    for p in paths:
        for key in ('id', 'title', 'subtitle', 'audience', 'chapters'):
            if not p.get(key):
                raise ValueError(f"path.json 的「{p.get('id', '?')}」缺少字段 {key}")
        missing = [c for c in p['chapters'] if c not in chapter_ids]
        if missing:
            raise ValueError(f"path.json 的「{p['title']}」含未知章 id: {missing}")
        if len(set(p['chapters'])) != len(p['chapters']):
            raise ValueError(f"path.json 的「{p['title']}」含重复章 id")
    return paths


# 路径内导航脚本（方案 §7.3）：?path=<路径 id> 进入时章尾上一章/下一章按路径顺序。
# __PATHS__ = {路径 id: {t: 路径名, c: [章 id…]}}；章标题从侧栏目录实时取，不重复存。
PATH_NAV_JS = '''<script>
(function () {
 var P = __PATHS__;
 var q = new URLSearchParams(location.search).get('path');
 if (!q || !P[q]) return;
 var list = P[q].c;
 var sec = document.querySelector('.content-section');
 if (!sec) return;
 var i = list.indexOf(sec.id);
 if (i < 0) return;
 var nav = document.getElementById('chapter-nav');
 if (!nav) return;
 function titleOf(id) {
 var a = document.querySelector('#toc-list a[href="#' + id + '"]');
 if (!a) return id;
 var t = a.cloneNode(true), s = t.querySelector('span');
 if (s) s.remove();
 return t.textContent.trim();
 }
 function ensure(kind) {
 var el = document.getElementById(kind + '-link');
 if (!el) {
 el = document.createElement('a');
 el.id = kind + '-link';
 el.className = 'text-primary hover:underline';
 if (kind === 'prev') nav.insertBefore(el, nav.firstChild);
 else nav.appendChild(el);
 }
 return el;
 }
 var prev = document.getElementById('prev-link');
 var next = document.getElementById('next-link');
 if (i > 0) {
 var a = ensure('prev');
 a.href = list[i - 1] + '.html?path=' + encodeURIComponent(q);
 a.textContent = '← ' + titleOf(list[i - 1]);
 } else if (prev) {
 prev.href = q + '.html';
 prev.textContent = '← 回到「' + P[q].t + '」';
 }
 if (i < list.length - 1) {
 var b = ensure('next');
 b.href = list[i + 1] + '.html?path=' + encodeURIComponent(q);
 b.textContent = titleOf(list[i + 1]) + ' →';
 } else if (next) {
 next.href = q + '.html';
 next.textContent = '读完「' + P[q].t + '」，回路径 →';
 }
})();
</script>'''


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
    # 书页 head 里带 canonical（指向站点根，因为书页在站点上与站点根是同一本书）。
    # 分章页是另外的 URL，必须换成指向自己——留着旧的会出现两个 canonical，
    # 搜索引擎取第一个，等于把 121 个章节页全判成站点根的副本。
    head_slim = RE_CANONICAL.sub('', head_slim)
    top_matter = RE_CANONICAL.sub('', top_matter)

    idmap = _id_page_map(tree, pos, chapter_spans)
    order = [cid for cid in _book_chapter_order(book) if cid in chapter_spans]

    # 篇锚点（#ji-chu-pian 等）在分章页没有对应节点，指向该篇第一章页
    part_first = {}
    for ch in book['chapters']:
        pid = ch.get('part') or ch.get('after_part')
        if pid and pid not in part_first and ch['id'] in chapter_spans:
            part_first[pid] = ch['id']
    idmap.update(part_first)

    # 章节元数据（标题取 front matter nav）与导读首句（路径页复用，方案 §7.3）
    meta = {}
    for ch in book['chapters']:
        m, _ = B._read_md(root, ch['file'])
        meta[ch['id']] = {'title': m.get('nav') or ch['id']}
    descs = {}
    paths = load_paths(root, set(order))
    path_nav_js = ''
    if paths:
        pdata = {p['id']: {'t': p['title'], 'c': p['chapters']} for p in paths}
        path_nav_js = PATH_NAV_JS.replace('__PATHS__',
                                          json.dumps(pdata, ensure_ascii=False))

    site = ((json.loads((root / 'manifest' / 'languages.json').read_text(encoding='utf-8'))
             .get('site_url') or '').rstrip('/'))

    # ---- hreflang 备选表（方案 §6.3）----
    # v1.9 的逐章译文尚在制作；现阶段备选指向 v1.8 各语言单文件的同 id 锚点
    # （v1.8 无此章或无该语言成品则不发），将来 v1.9/<lang>/ 章节页落地，
    # 把 alts_for 换成逐章 URL 即可，互链结构不变。
    _mf = json.loads((root / 'manifest' / 'languages.json').read_text(encoding='utf-8'))
    langs_meta = _mf.get('languages', {})
    v18_ids = {c['id'] for c in json.loads((root / 'source' / 'book.json')
                                           .read_text(encoding='utf-8'))['chapters']}
    v18_files = {c for c in langs_meta if (root / 'v1.8' / f'{c}.html').is_file()}

    def alts_for(cid: str = '') -> dict:
        out = {}
        for code, lm in langs_meta.items():
            hl = lm.get('html_lang') or code
            if code == lang:
                out[hl] = (f'{site}/{version}/{lang}/{cid}.html' if cid
                           else f'{site}/{version}/{lang}/index.html')
            elif code in v18_files and (not cid or cid in v18_ids):
                out[hl] = f'{site}/v1.8/{code}.html' + (f'#{cid}' if cid else '')
        return out

    out = Path(out) if out else (root / 'dist' / 'site')
    page_dir = out / version / lang
    page_dir.mkdir(parents=True, exist_ok=True)
    assets = {}

    def page_shell(slim_head: str, title: str, canonical: str, ld: dict,
                   prefetch: str = '', og: dict = None, hreflang: str = '') -> str:
        h = RE_TITLE.sub(f'<title>{title}</title>', slim_head, count=1)
        if og:
            h = _set_og(h, og)
        # 下一章 prefetch（方案 §5.2）：读完点「下一章」零网络等待。
        # iOS Safari 忽略 prefetch——回访场景由 SW 缓存兜住，收益在安卓/桌面。
        pre = f'<link rel="prefetch" href="{prefetch}">\n' if prefetch else ''
        h = h.replace('</head>',
                      f'<link rel="canonical" href="{canonical}">\n'
                      f'{_json_ld(ld)}\n'
                      f'{pre}{hreflang}'
                      f'<link rel="stylesheet" href="assets/book.css">\n</head>', 1)
        return h

    book_title = book.get('title') or '你缺失的那门手机课'
    pages = {}
    budget_bad = []
    canon_bad = []

    # 共享壳层一次性外置 CSS/JS 与路径改写（所有页共用同一套资产）
    assets = {}
    head_slim = RE_SINGLEFILE_STYLE.sub('', head_slim)
    top_matter = RE_SINGLEFILE_STYLE.sub('', top_matter)
    tail = RE_SINGLEFILE_STYLE.sub('', tail)
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
    import shutil
    (page_dir / 'assets').mkdir(exist_ok=True)
    # MiSans：CSS 里的 @font-face 用 ../fonts/ 相对路径，字体随页面树一起输出
    fonts_out = page_dir / 'fonts'
    # 正文字体：woff2 子集优先，TTF 仅作兜底（CSS 里双源声明，浏览器不会下 TTF）
    for name in ('MiSans-subset.woff2', 'MiSans-Normal.ttf'):
        src = root / 'fonts' / name
        if not src.is_file() and name.endswith('.ttf'):
            src = root / 'assets' / 'fonts' / name   # 兼容旧布局
        if src.is_file():
            fonts_out.mkdir(exist_ok=True)
            shutil.copy2(src, fonts_out / name)
    # 图标已全部改为文字，不再需要分发图标字体
    for name, body in assets.items():
        for a, b in PATH_FIXES:      # 外置 JS 里的相对路径同样要降级
            body = body.replace(a, b)
        body = fix_sw_scope(body)
        (page_dir / 'assets' / name).write_text(body, encoding='utf-8', newline='\n')

    # 输出根 = 可直接部署的自包含站点树：补齐 PWA 资产（sw/manifest/图标/公告）
    # 以及勘误页与语言分级页（章末「报告错误」入口指向它们）
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
        # 每页必须恰好一个 canonical：两个 canonical 时搜索引擎取第一个，
        # 会被书页继承来的那个（站点根）盖掉，章节页就被判成重复内容。
        n_canon = len(re.findall(r'<link rel="canonical"[^>]*>', html))
        if n_canon != 1:
            canon_bad.append((name, n_canon))
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
    # 策展路径卡片区（方案 §7.3）：放在全书目录之前——先回答「我该从哪读」
    path_cards = ''
    if paths:
        cards = []
        for p in paths:
            cards.append(
                f'<a href="{p["id"]}.html" class="path-step block focus-ring" '
                f'style="text-decoration:none;color:inherit;">'
                f'<h3 class="font-bold text-base mt-2 mb-1 text-primary">{p["title"]}</h3>'
                f'<p class="text-xs text-gray-500 dark:text-gray-400 mb-1">'
                f'{len(p["chapters"])} 章 · {p["audience"]}</p>'
                f'<p class="text-sm text-gray-700 dark:text-gray-300">{p["subtitle"]}</p></a>')
        path_cards = (
            '<section class="mb-8" aria-labelledby="curated-paths-title">'
            '<h2 id="curated-paths-title" class="text-xl font-bold text-dark '
            'dark:text-gray-200 mb-1">策展路径：按目标读</h2>'
            '<p class="text-sm text-gray-600 dark:text-gray-400 mb-3">'
            '不必从头读到尾。挑一条适合你的路线，路径里的「下一章」永远是你该读的下一章；'
            '读完路径尽头，就是完整目录。</p>'
            '<div class="learning-path">' + ''.join(cards) + '</div></section>\n')
    idx_url = f'{site}/{version}/{lang}/index.html' if site else ''
    idx_head = page_shell(head_slim, f'{book_title} · {version}',
                          idx_url,
                          {"@context": "https://schema.org", "@type": "Book",
                           "name": book_title, "inLanguage": lang,
                           "url": idx_url, "hasPart": len(order)},
                          hreflang=hreflang_block(alts_for(), x_default=idx_url))
    emit('index.html', _rewrite_hrefs(
        idx_head + top_matter + '\n' + path_cards + '\n'.join(toc_lines) + tail,
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
            nav_bits.append(f'<a id="prev-link" href="{prev_id}.html" class="text-primary hover:underline">'
                            f'← {meta[prev_id]["title"]}</a>')
        if next_id:
            nav_bits.append(f'<a id="next-link" href="{next_id}.html" class="text-primary hover:underline">'
                            f'{meta[next_id]["title"]} →</a>')
        prevnext = ('\n<nav id="chapter-nav" class="flex flex-wrap justify-between gap-4 mt-10 mb-6">'
                    + '<span></span>'.join(nav_bits) + '</nav>')
        title = f'{meta[cid]["title"]} · {book_title}'
        url = f'{site}/{version}/{lang}/{cid}.html' if site else ''
        ld = {"@context": "https://schema.org", "@type": "Chapter",
              "name": meta[cid]['title'], "url": url,
              "isPartOf": {"@type": "Book", "name": book_title, "inLanguage": lang}}
        # 章节级分享卡（方案 §6.2）：分享出去的是章标题 + 导读首句，不再是书名
        og = {'og:title': meta[cid]['title'],
              'og:description': og_description(body),
              'og:type': 'article',
              'og:url': url}
        descs[cid] = og['og:description']
        page = page_shell(head_slim, title, url, ld,
                          prefetch=f'{next_id}.html' if next_id else '', og=og,
                          hreflang=hreflang_block(alts_for(cid), x_default=url)) \
            + '\n' + body + prevnext + (path_nav_js if paths else '') + tail
        page = _rewrite_hrefs(page, idmap, cid, frozenset(part_first))
        emit(f'{cid}.html', page)

    # ---- 策展路径页（方案 §7.2-7.3）：顺序清单 + 每章一行导读 + 进度联动 ----
    # 进度与全书共用一套已读记录（phoneCourse_completed），按路径过滤显示 n/N——
    # 「读完路径尽头就是完整目录，升舱不降级」。
    path_progress_js = '''<script>
(function () {
 var ids = __IDS__;
 var KEY = 'phoneCourse_completed';
 var arr = [];
 try { arr = JSON.parse(localStorage.getItem(KEY) || '[]'); } catch (e) {}
 var n = 0;
 ids.forEach(function (id) { if (arr.indexOf(id) >= 0) n++; });
 var t = document.getElementById('path-progress-text');
 var b = document.getElementById('path-progress-bar');
 if (t) t.textContent = n + ' / ' + ids.length;
 if (b) b.style.transform = 'scaleX(' + (ids.length ? n / ids.length : 0) + ')';
})();
</script>'''
    for p in paths:
        pid, n = p['id'], len(p['chapters'])
        items = []
        for i, cid in enumerate(p['chapters'], 1):
            d = descs.get(cid, '')
            items.append(
                f'<li class="mb-4"><a href="{cid}.html?path={pid}" '
                f'class="text-primary hover:underline font-semibold">'
                f'{i:02d} · {meta[cid]["title"]}</a>'
                + (f'<p class="text-sm text-gray-600 dark:text-gray-400 mb-0">{d}</p>'
                   if d else '')
                + '</li>')
        pbody = (
            f'<section class="mb-8"><h2 class="text-2xl font-bold text-dark '
            f'dark:text-gray-200 mb-1">{p["title"]}</h2>'
            f'<p class="text-sm text-gray-600 dark:text-gray-400 mb-3">{p["subtitle"]}'
            f' · 适合：{p["audience"]}</p>'
            f'<div class="reading-guide-card">'
            f'<div class="flex items-center justify-between text-sm mb-2">'
            f'<span>路径进度</span>'
            f'<span id="path-progress-text" class="font-semibold text-primary">— / {n}</span></div>'
            f'<div class="toc-progress-bar" id="path-progress-bar" '
            f'style="transform:scaleX(0);" aria-hidden="true"></div>'
            f'<p class="text-xs text-gray-500 dark:text-gray-400 mt-2">'
            f'与全书进度共用一套记录：章节里点「标记已读」，这里就会累计。'
            f'读完路径尽头，就是完整目录。</p></div>'
            f'<ol class="mt-4">' + '\n'.join(items) + '</ol>'
            f'<p class="mt-6"><a href="index.html" class="text-primary hover:underline">'
            f'想换条路？完整目录在这里 →</a></p></section>')
        pbody += path_progress_js.replace('__IDS__',
                                          json.dumps(p['chapters'], ensure_ascii=False))
        purl = f'{site}/{version}/{lang}/{pid}.html' if site else ''
        pld = {"@context": "https://schema.org", "@type": "ItemList",
               "name": p['title'], "description": p['subtitle'],
               "numberOfItems": n, "url": purl}
        ppage = page_shell(head_slim, f'{p["title"]} · {book_title}', purl, pld) \
            + '\n' + pbody + tail
        emit(f'{pid}.html', _rewrite_hrefs(ppage, idmap, pid, frozenset(part_first)))

    # ---- sitemap ----
    if site:
        urls = [f'{site}/{version}/{lang}/index.html'] + \
               [f'{site}/{version}/{lang}/{cid}.html' for cid in order]
        # 各语言单文件入口（方案 §6.4：其余语言不能在 sitemap 里 0 条）；
        # 顶层壳页面（站点首页/勘误/语言页/quiz/单文件）由 sync_site 补入。
        urls += [f'{site}/v1.8/{c}.html' for c in sorted(v18_files)]
        # 策展路径页
        urls += [f'{site}/{version}/{lang}/{p["id"]}.html' for p in paths]
        sm = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
        sm += [f'  <url><loc>{u}</loc></url>' for u in urls]
        sm.append('</urlset>')
        (out / 'sitemap.xml').write_text('\n'.join(sm) + '\n', encoding='utf-8', newline='\n')

    return {'version': version, 'lang': lang, 'pages': len(pages),
            'out': str(page_dir), 'budget': PAGE_BUDGET,
            'over_budget': budget_bad,
            'bad_canonical': canon_bad,
            'page_stats': pages}
