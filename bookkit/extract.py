"""extract：把已发布的成品 HTML 反向拆解为单一事实源（source/）。

产物：
  source/book.json           书籍结构（篇/章顺序、TOC 元数据、孤儿章节归属）
  source/template/shell.html 页面骨架（head + 导航 + 侧栏 + 页脚 + 脚本）
  source/parts/NN-<id>.md    各篇导语
  source/chapters/NN-<id>.md 各章正文（Markdown + 行内 HTML）

依赖 htmlparse 的字节无损往返：抽取前会断言 parse→serialize 与原文完全一致。
"""

import json
import re
from pathlib import Path

from . import htmlparse as H
from .htmlparse import Comment, Node
from . import markdown as M

TOC_ID = 'toc-list'
SUPPLEMENT_SUFFIX = re.compile(r'-(memory|harmony|jinjie|termux|advanced)$')


def _find_by_id(root, node_id):
    for n in root.find_all():
        if n.get('id') == node_id:
            return n
    return None


def _toc_model(toc_node):
    """把侧栏目录解析成 parts / items 结构（含每个分组的注释原文）。"""
    parts, items = [], {}
    comments = {}
    pending_comment = None
    for child in toc_node.children:
        if isinstance(child, Comment):
            pending_comment = child.raw
            continue
        if not isinstance(child, Node) or 'toc-parent' not in child.classes:
            continue
        li = child
        if pending_comment:
            comments[id(li)] = pending_comment
        pending_comment = None
        head_a = li.find('a')
        if head_a is None:
            continue
        child_ul = next((ul for ul in li.find_all('ul')
                         if (ul.get('id') or '').startswith('child-')), None)
        entries = []
        if child_ul is not None:
            for sub_li in child_ul.element_children():
                if sub_li.tag != 'li':
                    continue
                a = sub_li.find('a')
                if a is None:
                    continue
                span = a.find('span')
                num = H.text_of(span).strip() if span else ''
                label = H.text_of(a)
                if num and label.startswith(num):
                    label = label[len(num):].strip()
                entry = {'id': (a.get('href') or '').lstrip('#'), 'num': num,
                         'label': label,
                         'toc': 'sub' if 'text-xs' in a.classes else 'default'}
                entries.append(entry)
                items[entry['id']] = entry
        button = li.find('button')
        aria = (button.get('aria-label') or '') if button else ''
        parts.append({
            'id': (head_a.get('href') or '').lstrip('#'),
            'group': li.get('data-group') or '',
            'nav': H.text_of(head_a),
            'short': re.sub(r'^展开/收起', '', aria) or H.text_of(head_a),
            'toc_comment': comments.get(id(li), ''),
            'chapters': [e['id'] for e in entries],
        })
    return parts, items


def _leading_comment(node) -> str:
    """取某节点紧邻的前置注释（可能连续多条），按原文顺序拼接。"""
    if node.parent is None:
        return ''
    siblings = node.parent.children
    try:
        idx = next(i for i, c in enumerate(siblings) if c is node)
    except StopIteration:
        return ''
    found = []
    for j in range(idx - 1, -1, -1):
        c = siblings[j]
        if isinstance(c, Comment):
            found.append(c.raw)
            continue
        if isinstance(c, str) and not c.strip():
            continue
        break
    return '\n'.join(reversed(found))


def _section_kind(cid: str) -> str:
    if cid.startswith('fu-lu'):
        return 'appendix'
    if cid.startswith('jie-yu'):
        return 'conclusion'
    if SUPPLEMENT_SUFFIX.search(cid):
        return 'supplement'
    return 'chapter'


def _front_matter(meta: dict) -> str:
    lines = ['---']
    for k, v in meta.items():
        if v is None or v == '':
            continue
        lines.append(f'{k}: {v}')
    lines.append('---')
    return '\n'.join(lines) + '\n'


def extract(root: Path, version: str = 'v1.8', lang: str = 'zh-CN',
            src_dir: Path = None, dry_run: bool = False) -> dict:
    html_path = root / version / f'{lang}.html'
    raw = html_path.read_text(encoding='utf-8')
    tree = H.parse(raw)
    if H.serialize(tree) != raw:
        raise RuntimeError('解析器未能无损往返，拒绝据此生成源稿')
    pos = H.index_nodes(tree)

    main = _find_by_id(tree, 'content')
    if main is None:
        raise RuntimeError('未找到 <main id="content">')
    toc_node = _find_by_id(tree, TOC_ID)
    if toc_node is None:
        raise RuntimeError('未找到侧栏目录 #toc-list')

    parts, toc_items = _toc_model(toc_node)

    part_nodes = [n for n in main.find_all('section')
                  if n.find('div', cls='content-section') is not None]
    part_nodes.sort(key=lambda n: pos[id(n)][0])
    part_ids = {n.get('id') for n in part_nodes}

    # 正文块顺序：篇 + 不属于任何篇的"孤儿章节"（v1.8 第 36 章即如此）
    blocks = [('part', n) for n in part_nodes]
    for n in main.find_all('div'):
        if 'content-section' not in n.classes:
            continue
        parent = n.parent
        if parent is not None and parent.tag == 'section' and parent.get('id') in part_ids:
            continue
        blocks.append(('chapter', n))
    blocks.sort(key=lambda b: pos[id(b[1])][0])

    chapters_meta, chapter_files, part_files = [], {}, {}
    part_order = {p['id']: i for i, p in enumerate(parts)}
    part_open, part_comment = {}, {}
    state = {'part': None}

    def add_chapter(cnode, pid, comment=''):
        cid = cnode.get('id')
        item = toc_items.get(cid, {})
        meta = {
            'id': cid,
            'num': item.get('num', ''),
            'part': pid or '',
            'nav': item.get('label', ''),
            'toc': item.get('toc', 'default'),
            'kind': _section_kind(cid),
        }
        if not pid and state['part']:
            meta['after_part'] = state['part']
        idx = len(chapters_meta)
        rel = f'chapters/{idx:02d}-{cid}.md'
        chapter_files[rel] = _front_matter(meta) + '\n' + M.to_markdown(cnode).strip('\n') + '\n'
        chapters_meta.append({'id': cid, 'file': rel, 'part': pid or '',
                              'after_part': meta.get('after_part', ''),
                              'kind': meta['kind'], 'comment': comment})
        return cid

    for kind, node in blocks:
        if kind == 'part':
            pid = node.get('id')
            state['part'] = pid
            part_open[pid] = node.raw
            part_comment[pid] = _leading_comment(node)
            rest = H.Node('section', list(node.attrs), node.raw)
            pending = ''
            for child in node.children:
                if isinstance(child, Comment):
                    pending = child.raw
                    rest.children.append(child)
                    continue
                if isinstance(child, Node) and child.tag == 'div' and 'content-section' in child.classes:
                    add_chapter(child, pid, pending)
                    pending = ''
                elif isinstance(child, Node):
                    rest.children.append(child)
            meta = {'id': pid,
                    'group': next((p['group'] for p in parts if p['id'] == pid), ''),
                    'nav': next((p['nav'] for p in parts if p['id'] == pid), ''),
                    'short': next((p['short'] for p in parts if p['id'] == pid), ''),
                    'class': node.get('class', '')}
            pfile = f'parts/{part_order.get(pid, len(part_order)):02d}-{pid}.md'
            part_files[pfile] = _front_matter(meta) + '\n' + M.to_markdown(rest).strip('\n') + '\n'
        else:
            add_chapter(node, None, _leading_comment(node))

    # ---- 骨架：正文区间之前 / 之后 ----
    body_start = pos[id(blocks[0][1])][0]
    body_end = pos[id(blocks[-1][1])][1]
    head, tail = raw[:body_start], raw[body_end:]

    toc_start, toc_end = pos[id(toc_node)]
    inner_start = toc_start + len(toc_node.raw)
    inner_end = toc_end - len(toc_node.raw_close)
    head = head[:inner_start] + '{{TOC}}' + head[inner_end:]

    title_m = re.search(r'<title>(.*?)</title>', head, re.S)
    title = title_m.group(1).strip() if title_m else ''
    base_title = re.sub(r'\s*·\s*' + re.escape(version) + r'\s*$', '', title)
    head = head.replace(title, '{{TITLE}} · {{VERSION}}', 1)
    head = head.replace(f'数码必修课 · {version}', '数码必修课 · {{VERSION}}', 1)
    head = head.replace('69 章 + 8 附录', '{{CH_COUNT}} 章 + {{APP_COUNT}} 附录', 1)

    numbered = [c for c in chapters_meta
                if c['id'].startswith('di-') and not SUPPLEMENT_SUFFIX.search(c['id'])]
    app_count = len([c for c in chapters_meta if c['kind'] == 'appendix'])
    glossary = {'ch_count': max(0, len(numbered) - 1), 'app_count': app_count,
                'numbered_chapters': len(numbered)}

    part_entries = []
    chapter_ids = {c['id'] for c in chapters_meta}
    for p in parts:
        pid = p['id']
        part_entries.append({
            'id': pid, 'group': p['group'], 'nav': p['nav'], 'short': p['short'],
            'file': f'parts/{part_order[pid]:02d}-{pid}.md',
            'open_tag': part_open.get(pid, f'<section id="{pid}">'),
            'toc_comment': p.get('toc_comment', ''),
            'comment': part_comment.get(pid, ''),
            'chapters': [c['id'] for c in chapters_meta if c['part'] == pid],
            'orphans': [c['id'] for c in chapters_meta if c['after_part'] == pid],
            # 目录条目顺序（含非 content-section 的二级锚点，如"附：APK 打包"）
            'toc': p['chapters'],
            'toc_extra': [{'id': i, **toc_items[i]} for i in p['chapters']
                          if i not in chapter_ids and i in toc_items],
        })

    book = {
        'schema_version': 1,
        'version': version,
        'lang': lang,
        'title': base_title,
        'glossary': glossary,
        'template': 'template/shell.html',
        'parts': part_entries,
        'chapters': chapters_meta,
    }

    report = {'version': version, 'lang': lang, 'chapters': len(chapters_meta),
              'parts': len(parts), 'shell_bytes': len(head + tail), 'title': base_title,
              'glossary': glossary}
    if dry_run:
        return report

    src = Path(src_dir) if src_dir else (root / 'source')
    for sub in ('chapters', 'parts', 'template'):
        (src / sub).mkdir(parents=True, exist_ok=True)
    for old in list((src / 'chapters').glob('*.md')) + list((src / 'parts').glob('*.md')):
        old.unlink()

    for rel, content in {**chapter_files, **part_files}.items():
        (src / rel).write_text(content, encoding='utf-8', newline='\n')
    (src / 'template' / 'shell.html').write_text(head + '{{BODY}}' + tail,
                                                encoding='utf-8', newline='\n')
    (src / 'book.json').write_text(json.dumps(book, ensure_ascii=False, indent=2) + '\n',
                                   encoding='utf-8', newline='\n')
    return report
