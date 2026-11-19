"""build：从 source/ 生成单文件 HTML（目录、速查索引的锚点、版本徽章均由数据推导）。

用法：
  python -m bookkit build --lang zh-CN --out dist/v1.8/zh-CN.html
  python -m bookkit build --lang en    --out v1.8/en.html   # 翻译源稿
  python -m bookkit build --lang zh-CN --verify      # 与已发布成品做等价性比对

语言解析：zh-CN 用 source/book.json；其余语言用
source/translations/<lang>/book.json（缺省回退主源稿）。
"""

import json
import re
from pathlib import Path

from . import manifest as MF
from . import markdown as M

DEFAULT_BOOK = 'source/book.json'
TRANSLATIONS = 'source/translations'


def book_path_for(root: Path, lang: str, book_path: Path = None) -> Path:
    """按语言解析 book.json 路径。显式传入 book_path 时优先。"""
    if book_path:
        return Path(book_path)
    if lang and lang != 'zh-CN':
        cand = root / TRANSLATIONS / lang / 'book.json'
        if cand.is_file():
            return cand
    return root / DEFAULT_BOOK

TOC_HEAD = '{comment}\n' \
           '                    <li class="toc-parent" data-group="{group}">\n' \
           '                        <div class="flex items-center justify-between w-full px-3 py-2 rounded-md group/toc">\n' \
           '                            <a href="#{pid}" class="flex-1 text-gray-700 dark:text-gray-300 font-medium group-hover/toc:text-primary transition-colors">{nav}</a>\n' \
           '                            <button class="toc-toggle-btn" type="button" aria-label="展开/收起{short}" data-target="child-{group}">\n' \
           '                                <i class="fas fa-chevron-down toc-toggle-icon text-xs transition-transform duration-300"></i>\n' \
           '                            </button>\n' \
           '                        </div>\n' \
           '                        <ul id="child-{group}" class="toc-child open pl-4 space-y-0.5 mt-1">\n'

TOC_ITEM = ('                            <li><a href="#{cid}" class="toc-item block px-3 py-1.5 rounded-md '
            'hover:bg-light dark:hover:bg-gray-700 {cls}"><span class="{num_cls}">{num}</span>{label}</a></li>\n')

TOC_TAIL = '                        </ul>\n                    </li>\n'

CLASS_ITEM = 'text-gray-600 dark:text-gray-400'
CLASS_SUB = 'text-gray-500 dark:text-gray-500 pl-6 text-xs'
NUM_ITEM = 'mr-1.5 text-xs text-gray-400 font-mono'
NUM_SUB = 'mr-1.5 text-xs text-gray-300 font-mono'

# 每章页脚的「报告错误」入口（方案 §8.3：勘误入口三处之一）。
# 路径用 ../ 开头：书页在 v1.8/ 或 v1.9/ 下，勘误页在仓库根；
# 同步到站点后由 scripts/sync_site.py 降级为 ./。
#
# **必须逐语言本地化**：lint 的 residual 检查要求非中文语言版里汉字数为 0，
# 文言文版还必须是繁体字形。一段中文页脚塞进 18 种语言，
# 等于在每个外文页面里留下 3500 多个汉字。
ERRATA_FOOTER = {
    'zh-CN': ('发现这一章有错？到<a href="../errata.html" class="text-primary hover:underline">'
              '勘误页</a>报告（路径过时、事实有误、说不清，都欢迎提），'
              '或加 QQ 群 1074995524。本页路径版本见章首锚点。'),
    'zh-TW': ('發現這一章有錯？到<a href="../errata.html" class="text-primary hover:underline">'
              '勘誤頁</a>回報（路徑過時、事實有誤、說不清，都歡迎提），'
              '或加 QQ 群 1074995524。本頁路徑版本見章首錨點。'),
    'yue': ('呢一章有錯？去<a href="../errata.html" class="text-primary hover:underline">'
            '勘誤頁</a>講（路徑過時、事實唔啱、講唔明，都歡迎講），'
            '或者加 QQ 群 1074995524。本頁路徑版本見章首錨點。'),
    'lzh': ('此章有誤乎？往<a href="../errata.html" class="text-primary hover:underline">'
            '勘誤頁</a>言之（路徑過時、事實有訛、不能明言者，皆可言之），'
            '或入 QQ 群 1074995524。本頁路徑版本，見章首之錨。'),
    'ja': ('この章に誤りがありましたら、<a href="../errata.html" class="text-primary hover:underline">'
           '勘誤ページ</a>へ（古いパス、違う事実、読みにくい表現、すべて歓迎）。'
           'QQ グループ 1074995524 でも報告できます。'),
    'ko': ('이 장에 오류가 있으면 <a href="../errata.html" class="text-primary hover:underline">'
           '오류 신고 페이지</a>로 알려 주세요(오래된 경로, 잘못된 사실, 이해하기 어려운 설명 — 모두 환영). '
           'QQ 그룹 1074995524 로도 됩니다.'),
    'en': ('Found an error in this chapter? '
           '<a href="../errata.html" class="text-primary hover:underline">Report it on the errata page</a>'
           ' — outdated path, wrong fact, unclear wording, all welcome. '
           'You can also reach us on QQ group 1074995524.'),
    'ru': ('Нашли ошибку в этой главе? '
           '<a href="../errata.html" class="text-primary hover:underline">Сообщите на странице исправлений</a>'
           ' — устаревший путь, неверный факт, непонятная формулировка: всё приветствуется. '
           'Можно написать и в QQ-группу 1074995524.'),
    'it': ('Trovato un errore in questo capitolo? '
           '<a href="../errata.html" class="text-primary hover:underline">Segnalalo sulla pagina delle correzioni</a>'
           ' — percorso superato, fatto impreciso, frase poco chiara: tutto benvenuto. '
           'Puoi anche scrivere nel gruppo QQ 1074995524.'),
    'pt': ('Encontrou um erro neste capítulo? '
           '<a href="../errata.html" class="text-primary hover:underline">Reporte na página de erratas</a>'
           ' — caminho desatualizado, facto incorreto, frase confusa: tudo bem-vindo. '
           'Também pode escrever no grupo QQ 1074995524.'),
    'es': ('¿Has encontrado un error en este capítulo? '
           '<a href="../errata.html" class="text-primary hover:underline">Repórtalo en la página de erratas</a>'
           ' — ruta obsoleta, dato incorrecto, frase confusa: todo bienvenido. '
           'También puedes escribir en el grupo QQ 1074995524.'),
    'fr': ('Une erreur dans ce chapitre ? '
           '<a href="../errata.html" class="text-primary hover:underline">Signalez-la sur la page des errata</a>'
           ' — chemin obsolète, fait inexact, phrase confuse : tout est bienvenu. '
           'Vous pouvez aussi écrire dans le groupe QQ 1074995524.'),
    'de': ('Fehler in diesem Kapitel gefunden? '
           '<a href="../errata.html" class="text-primary hover:underline">Melden Sie ihn auf der Errata-Seite</a>'
           ' — veralteter Pfad, falsche Angabe, unklarer Satz: alles willkommen. '
           'Sie erreichen uns auch in der QQ-Gruppe 1074995524.'),
    'el': ('Βρήκατε λάθος σε αυτό το κεφάλαιο; '
           '<a href="../errata.html" class="text-primary hover:underline">Αναφέρετέ το στη σελίδα διορθώσεων</a>'
           ' — παλιός δρόμος, λανθασμένο γεγονός, ασαφής πρόταση: όλα ευπρόσδεκτα. '
           'Μπορείτε επίσης να γράψετε στην ομάδα QQ 1074995524.'),
    'ar': ('وجدت خطأً في هذا الفصل؟ '
           '<a href="../errata.html" class="text-primary hover:underline">أبلغ عنه في صفحة الأخطاء</a>'
           ' — مسار قديم، معلومة غير دقيقة، صياغة غامضة: كلها مقبولة. '
           'يمكنك الكتابة أيضًا في مجموعة QQ 1074995524.'),
    'he': ('מצאתם שגיאה בפרק זה? '
           '<a href="../errata.html" class="text-primary hover:underline">דיווחו בדף התיקונים</a>'
           ' — נתיב לא מעודכן, עובדה שגויה, ניסוח לא ברור: הכל קבל. '
           'אפשר גם לכתוב בקבוצת QQ 1074995524.'),
    'th': ('พบข้อผิดพลาดในบทนี้หรือไม่? '
           '<a href="../errata.html" class="text-primary hover:underline">แจ้งได้ที่หน้าแก้ไข</a>'
           ' — เส้นทางล้าสมัย ข้อเท็จจริงไม่ถูกต้อง ถ้อยคำกำกวม: ทั้งหมดยินดีรับ. '
           'แจ้งผ่านกลุ่ม QQ 1074995524 ก็ได้.'),
    'id': ('Menemukan kesalahan di bab ini? '
           '<a href="../errata.html" class="text-primary hover:underline">Laporkan di halaman koreksi</a>'
           ' — jalur yang usang, fakta yang keliru, kalimat yang membingungkan: semuanya diterima. '
           'Anda juga bisa menghubungi kami di grup QQ 1074995524.'),
    'ms': ('Jumpa ralat dalam bab ini? '
           '<a href="../errata.html" class="text-primary hover:underline">Laporkan di halaman ralat</a>'
           ' — laluan lapuk, fakta salah, ayat yang mengelirukan: semuanya dialtrexceka. '
           'Anda juga boleh menghubungi kami dalam kumpulan QQ 1074995524.'),
}
ERRATA_FOOTER_DEFAULT = ERRATA_FOOTER['en']


def errata_footer(lang: str) -> str:
    return ('\n                <p class="text-xs text-gray-500 dark:text-gray-400 mt-6 pt-3 '
            'border-t border-gray-200 dark:border-gray-700">'
            + ERRATA_FOOTER.get(lang, ERRATA_FOOTER_DEFAULT)
            + '</p>\n            ')


class BookError(RuntimeError):
    pass


def load_book(root: Path, book_path: Path = None, lang: str = 'zh-CN') -> dict:
    path = book_path_for(root, lang, book_path)
    if not path.is_file():
        raise BookError(f'源稿清单不存在：{path}（先运行 python -m bookkit extract）')
    return json.loads(path.read_text(encoding='utf-8'))


_BOOK_ROOTS = {}

def _read_md(root: Path, rel: str):
    # 源稿根 = book.json 所在目录（source/ 或 source/translations/<lang>/）
    src = _BOOK_ROOTS.get(str(root), root / 'source')
    p = src / rel
    if not p.is_file() and src != root / 'source':
        p = (root / 'source') / rel      # 回退主源稿（共享件）
    if not p.is_file():
        raise BookError(f'源稿缺失：{src}/{rel}')
    meta, body = M.split_front_matter(p.read_text(encoding='utf-8'))
    return meta, body


def social_meta(root: Path, lang: str) -> tuple:
    """社交卡片元数据：og:locale 与绝对可访问的分享图地址。

    分享卡片是三件事的唯一交叉点——标题（book.json）、语言（manifest）、
    封面（docs/promotion/assets/cover-og.png 同步到站点根）。写死在模板里必然漂移
    （历史上前 18 语模板里的 v3.2 / 69 章就是这么烂掉的），所以统一由数据注入。
    """
    try:
        mf = MF.load_manifest(root)
    except MF.ManifestError:
        return lang.replace('-', '_'), ''
    meta = mf.lang_meta(lang)
    locale = meta.get('og_locale') or (meta.get('html_lang') or lang).replace('-', '_')
    site = (mf.data.get('site_url') or '').rstrip('/')
    image = f'{site}/{mf.data.get("og_image", "cover-og.png")}' if site else ''
    return locale, image


def canonical_tag(root: Path, book: dict, lang: str) -> str:
    """生成 <link rel="canonical">，没有可信规范地址时返回空串（整段不输出）。

    为什么要有：站点根 index.html 与 /v1.9/zh-CN.html 是同一本书的逐字节副本
    （前者由 sync_site.py 从后者降级路径而来），两个 URL 都在索引里 = 重复内容。
    规范地址只能是站点根——它是 manifest 的 start_url，也是读者真正会分享的地址；
    /v1.9/zh-CN.html 是同书的单文件镜像，canonical 指回根。

    哪个版本/语言配发根地址，由 manifest 的 site_book 段声明（不在代码里写死）：
    没在站点上发布过的版本（例如 19 种译文的 v1.8 页面，站点上并不存在）一律不发
    canonical——指到一个 404 的 canonical 毫无意义，不如不发。
    """
    try:
        mf = MF.load_manifest(root)
    except MF.ManifestError:
        return ''
    sb = mf.data.get('site_book') or {}
    if not sb:
        return ''
    if book.get('version') != sb.get('version') or lang != sb.get('lang'):
        return ''
    site = (mf.data.get('site_url') or '').rstrip('/')
    if not site:
        return ''
    path = (sb.get('canonical') or '/').strip()
    url = site + '/' + path.lstrip('/') if path.strip('/') else site + '/'
    return f'<link rel="canonical" href="{url}">'


def render_toc(book: dict) -> str:
    chapters = {c['id']: c for c in book['chapters']}
    out = []
    for part in book['parts']:
        comment = part.get('toc_comment') or f'<!-- {part["short"]} -->'
        out.append(TOC_HEAD.format(comment=comment, group=part['group'], pid=part['id'],
                                   nav=part['nav'], short=part['short']))
        extra = {e['id']: e for e in part.get('toc_extra', [])}
        for cid in part.get('toc') or (part['chapters'] + part.get('orphans', [])):
            meta = chapters.get(cid) or extra.get(cid)
            if meta is None:
                continue
            num = meta.get('num', '')
            label = meta.get('nav') or meta.get('label', '')
            style = meta.get('toc', 'default')
            out.append(TOC_ITEM.format(
                cid=cid,
                cls=CLASS_SUB if style == 'sub' else CLASS_ITEM,
                num_cls=NUM_SUB if style == 'sub' else NUM_ITEM,
                num=num, label=label))
        out.append(TOC_TAIL)
    return ''.join(out)


def build(root: Path, lang: str = 'zh-CN', out: Path = None, book_path: Path = None) -> dict:
    book = load_book(root, book_path, lang)
    bp = book_path_for(root, lang, book_path)
    src = bp.parent
    _BOOK_ROOTS[str(root)] = src

    shell_path = src / book['template']
    if not shell_path.is_file():
        shell_path = (root / 'source') / book['template']
    shell = shell_path.read_text(encoding='utf-8')
    # canonical 注入在这里做，不走模板占位符：本书有 20 份模板副本
    # （每种语言一份，RTL/字体各不相同），改模板等于改 20 个文件，
    # 而真正需要 canonical 的只有站点上发布的那一版。
    canon = canonical_tag(root, book, lang)
    if canon:
        shell = shell.replace('</head>', f'    {canon}\n</head>', 1)

    # 章节 front matter 是 TOC 的唯一数据源：先全部读入，再渲染
    for ch in book['chapters']:
        meta, body = _read_md(root, ch['file'])
        ch['num'] = meta.get('num', '')
        ch['nav'] = meta.get('nav', '')
        ch['toc'] = meta.get('toc', 'default')
        ch['_body'] = body

    toc = render_toc(book)

    blocks = []
    for part in book['parts']:
        pmeta, pbody = _read_md(root, part['file'])
        open_tag = part.get('open_tag') or f'<section id="{part["id"]}" class="mb-12">'
        if part.get('comment'):
            blocks.append('            ' + part['comment'])
        blocks.append(open_tag)
        if pbody.strip():
            blocks.append(M.from_markdown(pbody).rstrip('\n'))
        for cid in part['chapters']:
            ch = next(c for c in book['chapters'] if c['id'] == cid)
            body = M.from_markdown(ch['_body']).rstrip('\n')
            comment = ch.get('comment') or ''
            if comment:
                blocks.append('                ' + comment)
            blocks.append(f'                <div id="{cid}" class="mb-10 content-section">\n'
                          f'{body}\n{errata_footer(lang)}\n                </div>')
        blocks.append('            </section>')
        # 未归属任何篇的章节：跟在篇的 </section> 之后（v1.8 第 36 章即如此）
        for cid in part.get('orphans', []):
            ch = next(c for c in book['chapters'] if c['id'] == cid)
            body = M.from_markdown(ch['_body']).rstrip('\n')
            comment = ch.get('comment') or ''
            if comment:
                blocks.append('            ' + comment)
            blocks.append(f'            <div id="{cid}" class="mb-10 content-section">\n'
                          f'{body}\n{errata_footer(lang)}\n            </div>')

    body_html = '\n\n'.join(blocks)

    g = book.get('glossary', {})
    og_locale, og_image = social_meta(root, lang)
    html = (shell
            .replace('{{TITLE}}', book.get('title', ''))
            .replace('{{VERSION}}', book.get('version', ''))
            .replace('{{OG_LOCALE}}', og_locale)
            .replace('{{OG_IMAGE}}', og_image)
            .replace('{{CH_COUNT}}', str(g.get('ch_count', '')))
            .replace('{{APP_COUNT}}', str(g.get('app_count', '')))
            .replace('{{TOC}}', toc)
            .replace('{{BODY}}', body_html))

    result = {'version': book.get('version'), 'lang': lang, 'bytes': len(html),
              'chapters': len(book['chapters']),
              'toc_entries': toc.count('<li><a href="#')}

    if out:
        out = Path(out)
        out.parent.mkdir(parents=True, exist_ok=True)
        _write_with_retry(out, html)
        result['out'] = str(out)
    return {'html': html, **result}


def _write_with_retry(path: Path, text: str, tries: int = 6) -> None:
    """写盘带重试。

    Windows 上偶发 OSError [Errno 22]（索引器/杀软短暂抢占文件句柄）。
    13MB 的书页 HTML 命中率不低，重试几次就能稳定写出去。
    """
    import time
    last = None
    for i in range(tries):
        try:
            with open(path, 'w', encoding='utf-8', newline='\n') as f:
                f.write(text)
            return
        except OSError as e:
            last = e
            if i < tries - 1:
                time.sleep(0.8 * (i + 1))
    raise last


# ---------------------------------------------------------------- 等价性校验

def verify(root: Path, lang: str = 'zh-CN', book_path: Path = None) -> dict:
    """把构建产物与已发布成品逐章比对：区块 id、目录、可见文本、块结构。"""
    from . import htmlparse as H
    from . import textutil as T

    book = load_book(root, book_path, lang)
    built = build(root, lang=lang, book_path=book_path)['html']
    published_path = root / book['version'] / f'{lang}.html'
    published = published_path.read_text(encoding='utf-8')

    def sections(html):
        tree = H.parse(html)
        out = []
        for n in tree.find_all('div'):
            if 'content-section' in n.classes:
                out.append((n.get('id'), n))
        return out

    pub, own = sections(published), sections(built)
    pub_ids = [i for i, _ in pub]
    own_ids = [i for i, _ in own]
    pub_map, own_map = dict(pub), dict(own)

    struct_diff, text_diff = [], []
    for cid in pub_ids:
        a, b = pub_map.get(cid), own_map.get(cid)
        if b is None:
            struct_diff.append(cid)
            text_diff.append(cid)
            continue
        if M.normalize(a.inner_raw()) != M.normalize(b.inner_raw()):
            struct_diff.append(cid)
        if M.text_digest(a.inner_raw()) != M.text_digest(b.inner_raw()):
            text_diff.append(cid)

    pub_toc, own_toc = T.toc_anchors(published), T.toc_anchors(built)
    pub_text, own_text = M.text_digest(published), M.text_digest(built)

    return {
        'published': str(published_path),
        'ids_equal': pub_ids == own_ids,
        'id_count': (len(pub_ids), len(own_ids)),
        'toc_equal': pub_toc == own_toc,
        'toc_count': (len(pub_toc), len(own_toc)),
        'text_equal': pub_text == own_text,
        'text_len': (len(pub_text), len(own_text)),
        'chapters_struct_identical': len(pub_ids) - len(struct_diff),
        'chapters_text_identical': len(pub_ids) - len(text_diff),
        'struct_diff': struct_diff,
        'text_diff': text_diff,
    }
