"""tm：翻译记忆库（TM）与增量翻译管线。

v1.8→v1.9 的中文正文扩写到 353.8 万字后，"全量人工翻译 ×18 语言"不再可行；
增量管线把翻译成本压到"只翻变更段落"：

- 段落级分段：章节 md 正文按空行切块为段落段（segment），规范化后哈希为稳定 id
- TM 构建（build）：zh-CN v1.8 源稿段落 ↔ 18 语翻译源稿段落逐段位置对齐，
  产出 manifest/tm/<lang>.json（源段哈希 → 译文段），未变内容零成本复用
- 增量报告（report）：对目标版本（如 v1.9）逐段查 TM，导出待译段落
  dist/i18n/<lang>-todo.json（含章 id/段序/源文），供机翻+人审或 Weblate 流转
- 导入（import）：译文 JSON（哈希 → 译文）合并回 TM

术语锁定由 manifest/glossary/<lang>.json 承担（见 scripts/gen_glossary.py）。
"""

import hashlib
import json
import re
from pathlib import Path

RE_FRONT = re.compile(r'^---\s*\n[\s\S]*?\n---\s*\n')


def _norm(text: str) -> str:
    return re.sub(r'\s+', ' ', text).strip()


def segments_of(path: Path) -> list:
    """章节 md → 段落段列表（跳过 front matter；按空行切块）。"""
    body = RE_FRONT.sub('', path.read_text(encoding='utf-8'))
    blocks = [b.strip() for b in re.split(r'\n\s*\n', body) if b.strip()]
    return blocks


def seg_hash(text: str) -> str:
    return hashlib.sha1(_norm(text).encode('utf-8')).hexdigest()[:16]


def _book_files(src_root: Path) -> list:
    book = json.loads((src_root / 'book.json').read_text(encoding='utf-8'))
    return [(c['id'], src_root / c['file']) for c in book['chapters']]


def build_tm(root: Path) -> dict:
    """从 v1.8 中文源稿 + 18 语翻译源稿构建 TM（manifest/tm/<lang>.json）。"""
    src_root = root / 'source'
    out = {}
    trans_dir = root / 'source' / 'translations'
    for lang_dir in sorted(p for p in trans_dir.iterdir() if p.is_dir()):
        lang = lang_dir.name
        tm = {}
        dup = 0
        for cid, src_file in _book_files(src_root):
            dst_file = lang_dir / src_file.relative_to(src_root)
            if not src_file.is_file() or not dst_file.is_file():
                continue
            src_segs, dst_segs = segments_of(src_file), segments_of(dst_file)
            for s, d in zip(src_segs, dst_segs):
                h = seg_hash(s)
                if h in tm and tm[h] != d:
                    dup += 1
                    continue
                tm[h] = d
        out[lang] = {'lang': lang, 'segments': len(tm), 'conflicts': dup}
        target = root / 'manifest' / 'tm' / f'{lang}.json'
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            json.dumps({'lang': lang, 'base_version': 'v1.8', 'segments': tm},
                       ensure_ascii=False, indent=1) + '\n',
            encoding='utf-8', newline='\n')
    return out


def _load_tm(root: Path, lang: str) -> dict:
    p = root / 'manifest' / 'tm' / f'{lang}.json'
    if not p.is_file():
        return {}
    return json.loads(p.read_text(encoding='utf-8')).get('segments', {})


def report(root: Path, book_path: Path, lang: str, out_dir: Path = None) -> dict:
    """目标版本逐段查 TM：命中可复用，未命中导出待译段落。"""
    src_root = book_path.parent
    tm = _load_tm(root, lang)
    todo, hit = [], 0
    for cid, f in _book_files(src_root):
        if not f.is_file():
            continue
        for i, seg in enumerate(segments_of(f)):
            h = seg_hash(seg)
            if h in tm:
                hit += 1
            else:
                todo.append({'chapter': cid, 'idx': i, 'hash': h, 'source': seg})
    out_dir = Path(out_dir) if out_dir else (root / 'dist' / 'i18n')
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f'{lang}-todo.json').write_text(
        json.dumps({'lang': lang, 'tm_hits': hit, 'todo': len(todo),
                    'segments': todo}, ensure_ascii=False, indent=1) + '\n',
        encoding='utf-8', newline='\n')
    total = hit + len(todo)
    return {'lang': lang, 'total': total, 'tm_hits': hit, 'todo': len(todo),
            'coverage': round(hit * 100 / total, 1) if total else 0.0,
            'out': str(out_dir / f'{lang}-todo.json')}


def import_tm(root: Path, lang: str, file: Path) -> dict:
    """译文 JSON（{"<hash>": "<译文段>"} 或 {"segments": {...}}）合并进 TM。"""
    data = json.loads(Path(file).read_text(encoding='utf-8'))
    segs = data.get('segments', data)
    tm = _load_tm(root, lang)
    added = sum(1 for h in segs if h not in tm)
    tm.update(segs)
    target = root / 'manifest' / 'tm' / f'{lang}.json'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps({'lang': lang, 'base_version': 'v1.8', 'segments': tm},
                   ensure_ascii=False, indent=1) + '\n',
        encoding='utf-8', newline='\n')
    return {'lang': lang, 'imported': len(segs), 'new': added, 'total': len(tm)}
