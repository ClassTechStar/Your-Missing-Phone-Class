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
                          f'{body}\n                </div>')
        blocks.append('            </section>')
        # 未归属任何篇的章节：跟在篇的 </section> 之后（v1.8 第 36 章即如此）
        for cid in part.get('orphans', []):
            ch = next(c for c in book['chapters'] if c['id'] == cid)
            body = M.from_markdown(ch['_body']).rstrip('\n')
            comment = ch.get('comment') or ''
            if comment:
                blocks.append('            ' + comment)
            blocks.append(f'            <div id="{cid}" class="mb-10 content-section">\n'
                          f'{body}\n            </div>')

    body_html = '\n\n'.join(blocks)

    g = book.get('glossary', {})
    html = (shell
            .replace('{{TITLE}}', book.get('title', ''))
            .replace('{{VERSION}}', book.get('version', ''))
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
        out.write_text(html, encoding='utf-8', newline='\n')
        result['out'] = str(out)
    return {'html': html, **result}


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
