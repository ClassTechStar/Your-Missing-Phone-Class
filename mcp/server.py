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
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from bookkit import content as C  # noqa: E402  （P1-1：数据访问统一走门面）

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


# ---------------------------------------------------------------- 工具实现（P1-1：转调 bookkit.content 门面）


def t_list_parts(_):
    parts = C.parts()
    for part in parts:
        part['chapters'] = [m['id'] for m in C.chapters() if m['part'] == part['title']]
    return parts


def t_list_chapters(args):
    return C.chapters(lang=args.get('lang', 'zh-CN'), part=args.get('part'))


def t_get_chapter(args):
    return C.load_chapter(args['chapter_id'], args.get('lang', 'zh-CN'))


def t_search(args):
    return {'query': args['query'], 'lang': args.get('lang', 'zh-CN'),
            'hits': C.search(args['query'], args.get('lang', 'zh-CN'),
                             args.get('in_body', False))}


def t_stats(_):
    st = C.stats()
    st['pdf_releases'] = ['latex-pdf-v1.8-final', 'latex-pdf-v1.7',
                          'latex-pdf-v1.6', 'latex-pdf-v1.5']
    return st



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
