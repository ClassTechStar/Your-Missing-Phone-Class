# -*- coding: utf-8 -*-
"""内容数据访问门面（P1-1，借鉴 CW2 分域 API 门面）。

唯一内容读取入口：MCP 服务器、quiz 生成、封面/站点同步等一律经由本模块，
避免各自实现解析逻辑。纯标准库，只读。

约定：
- 源稿根：source/（zh-CN）与 source/translations/<lang>/（其余语言）
- 语言代码：'zh-CN' 为主源稿；其余语言回退规则 = 翻译缺失时回退主源稿
- 标题来自各章 front matter 的 nav 行
"""
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_BOOK = json.loads((ROOT / 'source' / 'book.json').read_text(encoding='utf-8'))
_LANGS = json.loads((ROOT / 'manifest' / 'languages.json').read_text(encoding='utf-8'))['languages']


def src_root(lang: str) -> Path:
    """该语言的源稿根目录（翻译缺失时回退 zh-CN 主源稿）。"""
    cand = ROOT / 'source' / 'translations' / lang
    if lang != 'zh-CN' and cand.is_dir():
        return cand
    return ROOT / 'source'


def available_langs() -> list:
    out = ['zh-CN']
    t = ROOT / 'source' / 'translations'
    if t.is_dir():
        out += sorted(d.name for d in t.iterdir() if d.is_dir())
    return out


def parts() -> list:
    return [{'id': p['id'], 'title': p.get('nav', p['id'])} for p in _BOOK['parts']]


def part_label(pid: str) -> str:
    for p in _BOOK['parts']:
        if p['id'] == pid:
            return p.get('nav', pid)
    return pid


def chapter_meta(ch: dict, lang: str = 'zh-CN') -> dict:
    """章节元数据：id/篇/kind/标题（front matter nav）/extras/文件路径。"""
    path = src_root(lang) / ch['file']
    if not path.is_file():
        path = ROOT / 'source' / ch['file']
    title, extras = '', None
    if path.is_file():
        m = re.match(r'^---\s*\n(.*?)\n---', path.read_text(encoding='utf-8'), re.S)
        if m:
            nav = re.search(r'^nav:\s*(.+)$', m.group(1), re.M)
            if nav:
                title = nav.group(1).strip()
            em = re.search(r'^extras:\s*(\{.*?\})\s*$', m.group(1), re.M | re.S)
            if em:
                try:
                    extras = json.loads(em.group(1))
                except Exception:
                    extras = None
    return {'id': ch['id'],
            'part': part_label(ch.get('part') or ch.get('after_part')),
            'kind': ch.get('kind', 'chapter'),
            'title': title,
            'extras': extras,
            'file': str(path.relative_to(ROOT))}


def chapters(lang: str = 'zh-CN', part: str = None) -> list:
    out = []
    for ch in _BOOK['chapters']:
        meta = chapter_meta(ch, lang)
        if part and meta['part'] != part:
            continue
        out.append(meta)
    return out


def load_chapter(cid: str, lang: str = 'zh-CN') -> dict:
    ch = next((c for c in _BOOK['chapters'] if c['id'] == cid), None)
    if ch is None:
        return {'error': f'章节不存在：{cid}（用 chapters() 查询）'}
    meta = chapter_meta(ch, lang)
    path = ROOT / meta['file']
    if not path.is_file():
        return {'error': f'该语言暂无此章源稿：{lang}/{cid}'}
    return {'id': cid, 'lang': lang, 'part': meta['part'], 'kind': meta['kind'],
            'title': meta['title'], 'extras': meta['extras'],
            'file': meta['file'], 'markdown': path.read_text(encoding='utf-8')}


def _fold(s: str) -> str:
    return unicodedata.normalize('NFKC', s).lower()


def search(query: str, lang: str = 'zh-CN', in_body: bool = False) -> list:
    terms = [t for t in re.split(r'\s+', _fold(query)) if t]
    hits = []
    for ch in _BOOK['chapters']:
        meta = chapter_meta(ch, lang)
        matched = []
        if all(t in _fold(meta['title']) for t in terms):
            matched.append(meta['title'])
        if in_body:
            path = ROOT / meta['file']
            if path.is_file():
                for line in path.read_text(encoding='utf-8').splitlines():
                    f = _fold(line)
                    if all(t in f for t in terms):
                        matched.append(line.strip()[:120])
        if matched:
            hits.append({'chapter': meta['id'], 'title': meta['title'],
                         'matches': matched[:5]})
    return hits


def stats() -> dict:
    t = ROOT / 'source' / 'translations'
    trans = sorted(d.name for d in t.iterdir() if d.is_dir()) if t.is_dir() else []
    return {'title': _BOOK.get('title'), 'version': _BOOK.get('version'),
            'languages': len(_LANGS), 'chapters': len(_BOOK['chapters']),
            'parts': len(_BOOK['parts']), 'translation_sources': trans}
