#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""《你缺失的那门手机课》结构 MCP 服务器（stdio JSON-RPC，零依赖）。

让 AI 客户端（Claude Code / Claude Desktop 等）直连查询本书结构：
- list_parts / list_chapters / get_chapter / search / stats

用法（Claude Code）：
    claude mcp add phoneclass -- python mcp/server.py
或写入 .mcp.json：
    {"mcpServers": {"phoneclass": {"command": "python", "args": ["mcp/server.py"]}}}

协议：MCP（initialize / tools/list / tools/call），标准输入输出 JSON-RPC。
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = json.loads((ROOT / 'source' / 'book.json').read_text(encoding='utf-8'))
MANIFEST = json.loads((ROOT / 'manifest' / 'languages.json').read_text(encoding='utf-8'))

TOOLS = [
    {
        "name": "list_parts",
        "description": "列出全书 11 篇（篇名与章节范围）",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "list_chapters",
        "description": "列出章节（可按篇 part_id 过滤；返回 id/序号/篇/标题/文件）",
        "inputSchema": {
            "type": "object",
            "properties": {
                "part": {"type": "string",
                         "description": "篇 id（如 ji-chu-pian / ai-biancheng-pian / fu-lu）"},
            },
        },
    },
    {
        "name": "get_chapter",
        "description": "读取一章正文（Markdown 源稿）。chapter_id 可传章节 id、''第20章'' 或 ''20''；lang 可选，默认 zh-CN",
        "inputSchema": {
            "type": "object",
            "properties": {
                "chapter_id": {"type": "string",
                               "description": "章节 id，如 di-san-shi-qi-zhang / fu-lu-a"},
                "lang": {"type": "string", "description": "语言代码（默认 zh-CN）"},
            },
            "required": ["chapter_id"],
        },
    },
    {
        "name": "search",
        "description": "全文检索章节标题（OR 匹配 + 相关度排序，自然语言查询如''Termux 附录''可用）。设 in_body=true 同时检索正文",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "lang": {"type": "string", "description": "默认 zh-CN"},
                "in_body": {"type": "boolean",
                            "description": "同时检索正文（默认仅标题）"},
            },
            "required": ["query"],
        },
    },
    {
        "name": "stats",
        "description": "全书统计（语言数/章节数/篇数/PDF 版本）",
        "inputSchema": {"type": "object", "properties": {}},
    },
]

# ---------------------------------------------------------------- 数据访问

# 中文序号 → 阿拉伯数字（用于「第20章」「第二十章」这类查询）
CN_NUM = {'零': 0, '〇': 0, '一': 1, '二': 2, '两': 2, '三': 3, '四': 4, '五': 5,
          '六': 6, '七': 7, '八': 8, '九': 9, '十': 10}


def _cn_to_int(s):
    """中文数字转整数：十/十一/二十/二十一/一百。无法解析返回 None。

    同时接受「第20章」「第二十章」「20」这类带前后缀的写法。
    """
    if not s:
        return None
    s = str(s).strip()
    m = re.fullmatch(r'第\s*([零〇一二两三四五六七八九十百\d]+)\s*章', s)
    if m:
        s = m.group(1)
    else:
        # 「第二十章附」这类带后缀的写法：取出其中的「第X章」部分
        m = re.search(r'第\s*([零〇一二两三四五六七八九十百\d]+)\s*章', s)
        if m:
            s = m.group(1)
    if not s:
        return None
    if s.isdigit():
        return int(s)
    total, section, num = 0, 0, 0
    for ch in s:
        if ch in CN_NUM:
            d = CN_NUM[ch]
            if d == 10:
                section = (num or 1) * 10
                num = 0
            else:
                num = d
        elif ch == '百':
            section = (num or 1) * 100
            num = 0
        else:
            return None
    return section + num


def _chapter_number(meta, ch):
    """从 frontmatter 注释 / nav / 正文 H3 里提取章节序号（阿拉伯数字）。"""
    for text in (ch.get('comment') or '', meta.get('title') or ''):
        m = re.search(r'第\s*([零〇一二两三四五六七八九十百\d]+)\s*章', text)
        if m:
            n = _cn_to_int(m.group(1))
            if n is not None:
                return n
    return None


def _chapter_meta(ch, lang='zh-CN'):
    base = ROOT / 'source' / 'translations' / lang
    src_dir = base if (lang != 'zh-CN' and base.is_dir()) else (ROOT / 'source')
    f = src_dir / ch['file']
    title = ''
    if f.is_file():
        m = re.match(r'^---\s*\n(.*?)\n---', f.read_text(encoding='utf-8'), re.S)
        if m:
            nav = re.search(r'^nav:\s*(.+)$', m.group(1), re.M)
            if nav:
                title = nav.group(1).strip()
    meta = {'id': ch['id'], 'part': ch.get('part') or ch.get('after_part'),
            'kind': ch.get('kind', 'chapter'), 'title': title, 'file': ch['file']}
    meta['number'] = _chapter_number(meta, ch)
    return meta


def _part_label(pid):
    for p in BOOK['parts']:
        if p['id'] == pid:
            return p.get('nav', pid)
    return pid


def _chapter_path(ch, lang):
    src = ROOT / 'source' / 'translations' / lang
    if not src.is_dir():
        src = ROOT / 'source'
    return src / ch['file']


def _fold(s):
    return unicodedata.normalize('NFKC', s).lower()


# ---------------------------------------------------------------- 工具实现


def t_list_parts(_):
    out = []
    for p in BOOK['parts']:
        chs = [c['id'] for c in BOOK['chapters']
               if (c.get('part') or c.get('after_part')) == p['id']]
        out.append({'id': p['id'], 'title': _part_label(p['id']), 'chapters': chs})
    return out


def t_list_chapters(args):
    part = args.get('part')
    out = []
    for ch in BOOK['chapters']:
        meta = _chapter_meta(ch)
        if part and meta['part'] != part:
            continue
        out.append(meta)
    return out


def t_get_chapter(args):
    cid = args['chapter_id']
    lang = args.get('lang', 'zh-CN')
    ch = next((c for c in BOOK['chapters'] if c['id'] == cid), None)
    if ch is None:
        # 允许用「第20章」「20」「第二十章附」按序号查
        n = _cn_to_int(str(cid).strip())
        if n is not None:
            cands = [c for c in BOOK['chapters'] if _chapter_number({'title': ''}, c) == n]
            if len(cands) > 1:
                # 同一章号可能对应正文 + 附录（如第20章与第20章附），列出候选
                return {'error': f'第 {n} 章对应 {len(cands)} 个区块，请指定 chapter_id',
                        'candidates': [
                            {'chapter_id': c['id'],
                             'title': _chapter_meta(c, lang)['title'],
                             'kind': c.get('kind')} for c in cands]}
            if cands:
                ch = cands[0]
    if ch is None:
        return {'error': f'章节不存在：{cid}（用 list_chapters 查询，也支持「第20章」这类序号）'}
    p = _chapter_path(ch, lang)
    if not p.is_file():
        return {'error': f'该语言暂无此章源稿：{lang}/{cid}'}
    return {'id': ch['id'], 'lang': lang,
            'part': _part_label(ch.get('part') or ch.get('after_part')),
            'file': str(p.relative_to(ROOT)), 'markdown': p.read_text(encoding='utf-8')}


def t_search(args):
    """全文检索（OR 匹配 + 相关度排序）。

    自然语言查询（如「Termux 附录」）里常混有同义词或虚词，
    严格 AND 会把正确结果过滤掉。这里按「命中几个关键词」排序，
    全部命中的排最前，部分命中的按命中比例随后。
    """
    q = _fold(args['query'])
    lang = args.get('lang', 'zh-CN')
    in_body = args.get('in_body', False)
    limit = int(args.get('limit', 20) or 20)
    terms = [t for t in re.split(r'[\s,，、]+', q) if t]
    if not terms:
        return {'query': args['query'], 'lang': lang, 'hits': []}
    hits = []
    for ch in BOOK['chapters']:
        meta = _chapter_meta(ch, lang)
        title_f = _fold(meta['title'])
        id_f = _fold(meta['id'])
        hit_title = sum(1 for t in terms if t in title_f)
        hit_id = sum(1 for t in terms if t in id_f)
        # 「第20章」「20」这类数字查询：命中章节序号也算标题命中
        for t in terms:
            n = _cn_to_int(t)
            if n is not None and meta.get('number') == n:
                hit_title += 1
        score = hit_title * 2 + hit_id
        if not score and not in_body:
            continue
        matched_lines = [meta['title']] if hit_title else []
        body_hits = 0
        if in_body:
            p = _chapter_path(ch, lang)
            if p.is_file():
                for line in p.read_text(encoding='utf-8').splitlines():
                    f = _fold(line)
                    if any(t in f for t in terms):
                        body_hits += 1
                        if len(matched_lines) < 5:
                            matched_lines.append(line.strip()[:120])
        if score or body_hits:
            hits.append({'score': score, 'chapter': meta['id'], 'title': meta['title'],
                         'number': meta.get('number'), 'kind': meta.get('kind'),
                         'body_matches': body_hits, 'matches': matched_lines[:5]})
    hits.sort(key=lambda h: (-h['score'], -(h['body_matches'] > 0), h['number'] or 999))
    return {'query': args['query'], 'lang': lang, 'terms': terms,
            'hits': hits[:limit]}


def t_stats(_):
    return {
        'title': BOOK.get('title'),
        'version': BOOK.get('version'),
        'languages': len(MANIFEST['languages']),
        'chapters': len(BOOK['chapters']),
        'parts': len(BOOK['parts']),
        'translation_sources': sorted(
            d.name for d in (ROOT / 'source' / 'translations').iterdir() if d.is_dir()
        ) if (ROOT / 'source' / 'translations').is_dir() else [],
        'pdf_releases': ['latex-pdf-v1.8-final', 'latex-pdf-v1.7',
                         'latex-pdf-v1.6', 'latex-pdf-v1.5'],
    }


IMPL = {'list_parts': t_list_parts, 'list_chapters': t_list_chapters,
        'get_chapter': t_get_chapter, 'search': t_search, 'stats': t_stats}


# ---------------------------------------------------------------- MCP 协议


def send(msg):
    sys.stdout.write(json.dumps(msg, ensure_ascii=False) + '\n')
    sys.stdout.flush()


def handle(req):
    method = req.get('method')
    rid = req.get('id')
    if method == 'initialize':
        send({'jsonrpc': '2.0', 'id': rid, 'result': {
            'protocolVersion': '2024-11-05',
            'capabilities': {'tools': {}},
            'serverInfo': {'name': 'phoneclass', 'version': '1.0.0'},
        }})
    elif method == 'notifications/initialized':
        pass
    elif method == 'tools/list':
        send({'jsonrpc': '2.0', 'id': rid, 'result': {'tools': TOOLS}})
    elif method == 'tools/call':
        name = req['params']['name']
        args = req['params'].get('arguments', {}) or {}
        fn = IMPL.get(name)
        if fn is None:
            send({'jsonrpc': '2.0', 'id': rid,
                  'error': {'code': -32601, 'message': f'unknown tool: {name}'}})
            return
        try:
            result = fn(args)
            text = json.dumps(result, ensure_ascii=False, indent=1)
            send({'jsonrpc': '2.0', 'id': rid, 'result': {
                'content': [{'type': 'text', 'text': text}]}})
        except Exception as e:
            send({'jsonrpc': '2.0', 'id': rid,
                  'error': {'code': -32603, 'message': str(e)}})
    elif method == 'ping':
        send({'jsonrpc': '2.0', 'id': rid, 'result': {}})
    elif rid is not None:
        send({'jsonrpc': '2.0', 'id': rid,
              'error': {'code': -32601, 'message': f'unknown method: {method}'}})


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            handle(json.loads(line))
        except json.JSONDecodeError:
            continue


if __name__ == '__main__':
    main()
