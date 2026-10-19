"""极简容错 HTML 解析器：保留原始标签文本，保证 parse → serialize 字节无损。

只服务于本仓库的成品书 HTML（结构规整、无脚本生成 DOM），不追求完整 HTML5 规范。
"""

import re

VOID = {
    'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta',
    'param', 'source', 'track', 'wbr',
    # SVG 自闭合元素
    'path', 'circle', 'rect', 'line', 'polygon', 'polyline', 'ellipse', 'stop', 'use',
}

# pre 的内容按纯文本原样保留：示例代码里出现 <Boolean> 之类的尖括号时不会被误判为标签
RAW_TEXT = {'script', 'style', 'textarea', 'title', 'pre'}

RE_ATTR = re.compile(r'([:\w.-]+)(?:\s*=\s*("([^"]*)"|\'([^\']*)\'|([^\s>]+)))?')
RE_TAGNAME = re.compile(r'[a-zA-Z][\w:-]*')


class Node:
    """元素节点。raw 保留原始起始标签文本，使序列化字节无损。"""

    __slots__ = ('tag', 'attrs', 'raw', 'raw_close', 'children', 'parent', 'self_closing')

    def __init__(self, tag, attrs, raw, self_closing=False, parent=None):
        self.tag = tag
        self.attrs = attrs            # list[tuple[str, str|None]]，保持原顺序
        self.raw = raw
        self.raw_close = f'</{tag}>'
        self.children = []
        self.parent = parent
        self.self_closing = self_closing

    # ---- 便捷访问 ----
    def get(self, name, default=None):
        for k, v in self.attrs:
            if k == name:
                return '' if v is None else v
        return default

    @property
    def classes(self):
        return (self.get('class') or '').split()

    def element_children(self):
        return [c for c in self.children if isinstance(c, Node)]

    def find_all(self, tag=None, cls=None):
        """深度优先收集后代元素。"""
        out = []

        def walk(n):
            for c in n.children:
                if isinstance(c, Node):
                    if (tag is None or c.tag == tag) and (cls is None or cls in c.classes):
                        out.append(c)
                    walk(c)

        walk(self)
        return out

    def find(self, tag=None, cls=None):
        found = self.find_all(tag, cls)
        return found[0] if found else None

    def inner_raw(self):
        """子节点序列化（不含本节点标签）。"""
        return ''.join(serialize_child(c) for c in self.children)

    def text(self):
        return ''.join(text_of(c) for c in self.children)

    def __repr__(self):
        return f'<Node {self.tag} id={self.get("id")!r}>'


def text_of(node) -> str:
    if isinstance(node, str):
        return node
    if isinstance(node, Comment):
        return ''
    return node.text()


class Comment:
    __slots__ = ('raw',)

    def __init__(self, raw):
        self.raw = raw      # 含 <!-- --> 的完整原文


def _parse_attrs(seg: str):
    attrs = []
    for m in RE_ATTR.finditer(seg):
        name = m.group(1)
        if not name:
            continue
        val = m.group(3)
        if val is None:
            val = m.group(4)
        if val is None:
            val = m.group(5)
        attrs.append((name, val))
    return attrs


def parse(html: str) -> Node:
    root = Node('#root', [], '')
    stack = [root]
    i, n = 0, len(html)
    while i < n:
        lt = html.find('<', i)
        if lt < 0:
            stack[-1].children.append(html[i:])
            break
        if lt > i:
            stack[-1].children.append(html[i:lt])

        if html.startswith('<!--', lt):
            end = html.find('-->', lt + 4)
            end = n if end < 0 else end + 3
            stack[-1].children.append(Comment(html[lt:end]))
            i = end
            continue
        if html.startswith('<!', lt) or html.startswith('<?', lt):
            end = html.find('>', lt)
            end = n if end < 0 else end + 1
            stack[-1].children.append(html[lt:end])
            i = end
            continue

        # 扫描标签结束位置（尊重引号内的 >）
        j = lt + 1
        quote = None
        while j < n:
            ch = html[j]
            if quote:
                if ch == quote:
                    quote = None
            elif ch in '"\'':
                quote = ch
            elif ch == '>':
                break
            j += 1
        raw = html[lt:j + 1]
        inner = html[lt + 1:j]

        if inner.startswith('/'):
            name = inner[1:].strip().lower()
            for k in range(len(stack) - 1, 0, -1):
                if stack[k].tag == name:
                    stack[k].raw_close = raw
                    del stack[k:]
                    break
            i = j + 1
            continue

        m = RE_TAGNAME.match(inner)
        if not m:
            stack[-1].children.append(raw)
            i = j + 1
            continue
        name = m.group(0).lower()
        attrs = _parse_attrs(inner[m.end():])
        self_closing = inner.rstrip().endswith('/')
        node = Node(name, attrs, raw, self_closing, stack[-1])
        stack[-1].children.append(node)

        if name in VOID or self_closing:
            i = j + 1
            continue

        if name in RAW_TEXT:
            close = re.compile(r'</' + name + r'\s*>', re.I)
            cm = close.search(html, j + 1)
            if cm:
                if cm.start() > j + 1:
                    node.children.append(html[j + 1:cm.start()])
                node.raw_close = cm.group(0)
                i = cm.end()
            else:
                i = j + 1
            continue

        stack.append(node)
        i = j + 1
    return root


def serialize_child(node) -> str:
    if isinstance(node, str):
        return node
    if isinstance(node, Comment):
        return node.raw
    if node.self_closing or node.tag in VOID:
        return node.raw
    return node.raw + node.inner_raw() + node.raw_close


def serialize(node: Node) -> str:
    return node.inner_raw()


def index_nodes(root: Node) -> dict:
    """返回 {id(node): (start, end)} 的源码偏移表（依赖 parse/serialize 字节无损）。"""
    pos = {}
    counter = {'n': 0}

    def walk(node, start):
        counter['n'] += 1
        pos[id(node)] = (start, start)
        cur = start
        if node.tag != '#root':
            cur += len(node.raw)
        for c in node.children:
            if isinstance(c, Comment):
                cur += len(c.raw)
            elif isinstance(c, str):
                cur += len(c)
            else:
                cur = walk(c, cur)
        if node.tag != '#root' and not (node.self_closing or node.tag in VOID):
            cur += len(node.raw_close)
        pos[id(node)] = (start, cur)
        return cur

    walk(root, 0)
    return pos


def render(node: Node) -> str:
    """把节点序列化回 HTML（含自身标签）。"""
    return serialize_child(node)
