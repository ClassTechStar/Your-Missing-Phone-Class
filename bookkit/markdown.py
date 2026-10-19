"""章节源稿的 Markdown 方言：块级结构用 Markdown，行内格式保留原始 HTML。

设计取舍（详见 scripts/README.md）：
- 块级（标题/段落/列表/容器）转成 Markdown，便于翻译与校对；
- 行内（strong/em/a/code/i/span/br）原样保留为内联 HTML，避免转义带来的文本损毁；
- 表格、SVG 等复杂子树整体以 ```html 代码块原样保留，保真优先。

渲染是转换的逆运算，`bookkit build --verify` 会用文本摘要与结构摘要做等价性校验。
"""

import re

from .htmlparse import Comment, Node, serialize_child

INLINE_TAGS = {
    'span', 'a', 'strong', 'em', 'b', 'i', 'code', 'br', 'img', 'small',
    'sup', 'sub', 'kbd', 'mark', 'u', 's', 'del', 'ins', 'abbr', 'time', 'label',
}

DEFAULT_CLASSES = {
    'h3': 'text-xl font-bold text-dark dark:text-gray-200 mb-4',
    'h4': 'text-lg font-semibold mt-4 mb-2',
    'h5': 'font-semibold mt-3 mb-1',
    'h6': 'font-semibold mt-2 mb-1',
    'p': 'mb-2',
    'ul': 'list-disc pl-6 mb-3 space-y-1',
    'ol': 'list-decimal pl-6 mb-3 space-y-1',
}

BLOCK_CONTAINERS = {
    'div', 'section', 'article', 'aside', 'header', 'footer', 'figure',
    'details', 'blockquote', 'nav', 'main', 'dl', 'dd', 'dt', 'form', 'fieldset',
}

RAW_BLOCKS = {'table', 'svg', 'canvas', 'iframe', 'video', 'audio', 'object', 'noscript'}


# ---------------------------------------------------------------- HTML → Markdown

def _is_inline_only(node: Node) -> bool:
    for c in node.children:
        if isinstance(c, Comment):
            return False
        if isinstance(c, Node) and c.tag not in INLINE_TAGS:
            return False
    return True


def _squash(text: str) -> str:
    return re.sub(r'\s*\n\s*', ' ', text).strip()


def _attrs_of(node, default_class=None):
    """返回需要保留的属性列表；class 等于该标签默认值时省略。"""
    attrs = []
    for k, v in node.attrs:
        v = '' if v is None else v
        if '"' in v or '\n' in v:
            return None
        if k == 'class' and default_class is not None and v == default_class:
            continue
        attrs.append((k, v))
    return attrs


def _attr_line(attrs) -> str:
    if not attrs:
        return ''
    inner = ' '.join(f'{k}="{v}"' for k, v in attrs)
    return '{' + inner + '}'


def _fence(text: str, info: str = '') -> str:
    """用比内容更长的围栏包裹，避免内容含 ``` 时截断。"""
    longest = max((len(m.group(0)) for m in re.finditer(r'`+', text)), default=0)
    fence = '`' * max(3, longest + 1)
    body = text if text.endswith('\n') else text + '\n'
    return f'{fence}{info}\n{body}{fence}'


def to_markdown(node: Node, depth: int = 0) -> str:
    """把一组子节点转成 Markdown 文本。"""
    blocks = []
    for child in node.children:
        block = _block_to_md(child, depth)
        if block:
            blocks.append(block)
    return '\n\n'.join(blocks)


def _block_to_md(node, depth: int) -> str:
    if isinstance(node, Comment):
        return ''
    if isinstance(node, str):
        text = node.strip()
        return text if text else ''
    tag = node.tag

    if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
        level = int(tag[1])
        prefix = '#' * max(1, level)
        body = _heading_inner(node)
        attrs = _attrs_of(node, DEFAULT_CLASSES.get(tag))
        if attrs is None:
            return _fence(serialize_child(node), 'html')
        head = f'{prefix} {body}'
        line = _attr_line(attrs)
        return f'{line}\n{head}' if line else head

    if tag == 'p':
        inner = _squash(node.inner_raw())
        if not inner:
            return ''
        attrs = _attrs_of(node, DEFAULT_CLASSES['p'])
        if attrs is None:
            return _fence(serialize_child(node), 'html')
        line = _attr_line(attrs)
        return f'{line}\n{inner}' if line else inner

    if tag in ('ul', 'ol'):
        md = _list_to_md(node, depth)
        if md is None:
            return _fence(serialize_child(node), 'html')
        attrs = _attrs_of(node, DEFAULT_CLASSES[tag])
        if attrs is None:
            return _fence(serialize_child(node), 'html')
        line = _attr_line(attrs)
        return f'{line}\n{md}' if line else md

    if tag == 'hr':
        return '---'

    if tag == 'pre':
        return _fence(node.text(), '')

    if tag in RAW_BLOCKS:
        return _fence(serialize_child(node), 'html')

    if tag in BLOCK_CONTAINERS:
        classes = node.get('class')
        if _is_inline_only(node):
            inner = _squash(node.inner_raw())
            if not inner:
                return ''
            spec = ''.join(f' .{c}' for c in (classes.split() if classes else []))
            return f':::inline {tag}{spec}\n{inner}\n:::'
        spec = ''.join(f' .{c}' for c in (classes.split() if classes else []))
        body = to_markdown(node, depth).strip('\n')
        return f'::: {tag}{spec}\n{body}\n:::'

    if tag in INLINE_TAGS:
        inner = _squash(node.inner_raw())
        return inner if inner else ''

    # 未知块：整体保真
    return _fence(serialize_child(node), 'html')


def _heading_inner(node: Node) -> str:
    return _squash(node.inner_raw())


NESTED_LIST_CLASS = 'list-disc pl-6 mt-1 space-y-1'


def _list_to_md(node: Node, depth: int):
    """返回 Markdown 列表；遇到不支持的嵌套结构返回 None（调用方降级为原样保留）。"""
    if depth > 0 and (node.get('class') or '') != NESTED_LIST_CLASS:
        return None
    lines = []
    ordered = node.tag == 'ol'
    index = 1
    # 允许 ul/ol 直接含 li（本仓库如此）；若含其它块则不支持
    for child in node.children:
        if isinstance(child, str):
            if child.strip():
                return None
            continue
        if isinstance(child, Comment):
            continue
        if child.tag != 'li':
            return None

    for child in node.element_children():
        if child.tag != 'li':
            continue
        inline_parts = []
        nested = []
        ok = True
        for c in child.children:
            if isinstance(c, str):
                inline_parts.append(c)
            elif isinstance(c, Comment):
                inline_parts.append(c.raw)
            elif c.tag in INLINE_TAGS:
                inline_parts.append(serialize_child(c))
            elif c.tag in ('ul', 'ol'):
                nested.append(c)
            elif c.tag == 'p':
                inline_parts.append(c.inner_raw())
            else:
                ok = False
                break
        if not ok:
            return None
        text = _squash(''.join(inline_parts))
        marker = f'{index}. ' if ordered else '- '
        lines.append('  ' * depth + marker + text)
        index += 1
        for sub in nested:
            sub_md = _list_to_md(sub, depth + 1)
            if sub_md is None:
                return None
            lines.append(sub_md)
    return '\n'.join(lines)


# ---------------------------------------------------------------- Markdown → HTML

RE_FRONT = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.S)
RE_ATTR = re.compile(r'^\{(.+)\}\s*$')
RE_PAIR = re.compile(r'([\w:-]+)="([^"]*)"')
RE_DIRECTIVE = re.compile(r'^:::(inline)?\s*([\w-]+)?((?:\s+\.[^\s]+)*)\s*$')
RE_HEADING = re.compile(r'^(#{1,6})\s+(.*)$')
RE_UL = re.compile(r'^(\s*)[-*]\s+(.*)$')
RE_OL = re.compile(r'^(\s*)(\d+)\.\s+(.*)$')
RE_FENCE = re.compile(r'^(`{3,})([^\s`]*)\s*$')


def split_front_matter(text: str):
    m = RE_FRONT.match(text)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if ':' not in line:
            continue
        k, v = line.split(':', 1)
        v = v.strip()
        if len(v) >= 2 and v[0] == v[-1] and v[0] in '"\'':
            v = v[1:-1]
        meta[k.strip()] = v
    return meta, text[m.end():]


def _classes_from_spec(spec: str):
    return [tok[1:] for tok in spec.split() if tok.startswith('.')]


def _parse_attr_line(text: str):
    return [(m.group(1), m.group(2)) for m in RE_PAIR.finditer(text)]


def _tag_open(tag: str, attrs, default_class=None) -> str:
    attrs = list(attrs or [])
    if not any(k == 'class' for k, _ in attrs) and default_class:
        attrs.insert(0, ('class', default_class))
    if not attrs:
        return f'<{tag}>'
    return f'<{tag} ' + ' '.join(f'{k}="{v}"' for k, v in attrs) + '>'


def from_markdown(text: str) -> str:
    lines = text.split('\n')
    out = []
    i = 0
    pending_attrs = None

    def flush_pending():
        nonlocal pending_attrs
        pending_attrs = None

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # 属性行
        m = RE_ATTR.match(stripped)
        if m:
            pending_attrs = _parse_attr_line(m.group(1))
            i += 1
            continue

        # 容器指令
        m = RE_DIRECTIVE.match(stripped)
        if m:
            inline_mode = bool(m.group(1))
            tag = m.group(2) or 'div'
            classes = _classes_from_spec(m.group(3) or '')
            classes_attr = [('class', ' '.join(classes))] if classes else None
            if pending_attrs is not None:
                classes_attr = pending_attrs
                flush_pending()
            i += 1
            body, i = _collect_directive_body(lines, i)
            if inline_mode:
                out.append(f'{_tag_open(tag, classes_attr)}{body.strip()}</{tag}>')
            else:
                rendered = from_markdown(body)
                out.append(f'{_tag_open(tag, classes_attr)}\n{rendered}\n</{tag}>')
            continue

        # 围栏代码块
        m = RE_FENCE.match(stripped)
        if m:
            fence = m.group(1)
            info = m.group(2)
            i += 1
            body = []
            while i < len(lines) and lines[i].strip() != fence:
                body.append(lines[i])
                i += 1
            i += 1  # 跳过结束围栏
            content = '\n'.join(body)
            if info == 'html':
                out.append(content)
            else:
                cls = f' class="{info}"' if info else ''
                out.append(f'<pre{cls}>{content}</pre>')
            continue

        # 标题
        m = RE_HEADING.match(stripped)
        if m:
            level = len(m.group(1))
            tag = f'h{min(level, 6)}'
            attrs = pending_attrs
            flush_pending()
            out.append(f'{_tag_open(tag, attrs, DEFAULT_CLASSES.get(tag))}{m.group(2)}</{tag}>')
            i += 1
            continue

        # 分隔线
        if stripped in ('---', '***', '___'):
            out.append('<hr class="my-6 border-gray-200 dark:border-gray-700">')
            continue

        # 列表
        if RE_UL.match(line) or RE_OL.match(line):
            block, i = _render_list(lines, i, pending_attrs)
            flush_pending()
            out.append(block)
            continue

        # 段落
        para = [line]
        i += 1
        while i < len(lines):
            nxt = lines[i]
            if not nxt.strip():
                break
            if (RE_ATTR.match(nxt.strip()) or RE_DIRECTIVE.match(nxt.strip())
                    or RE_FENCE.match(nxt.strip()) or RE_HEADING.match(nxt.strip())
                    or RE_UL.match(nxt) or RE_OL.match(nxt)):
                break
            para.append(nxt)
            i += 1
        attrs = pending_attrs
        flush_pending()
        out.append(f'{_tag_open("p", attrs, DEFAULT_CLASSES["p"])}{" ".join(x.strip() for x in para)}</p>')

    return '\n'.join(out)


def _collect_directive_body(lines, i):
    """收集容器指令体：inline 指令整体作为不透明单元跳过。"""
    body = []
    depth = 1
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith(':::inline'):
            body.append(lines[i])
            i += 1
            while i < len(lines) and lines[i].strip() != ':::':
                body.append(lines[i])
                i += 1
            if i < len(lines):
                body.append(lines[i])
                i += 1
            continue
        if s == ':::':
            depth -= 1
            if depth == 0:
                return '\n'.join(body), i + 1
        elif RE_DIRECTIVE.match(s) and not RE_DIRECTIVE.match(s).group(1):
            depth += 1
        body.append(lines[i])
        i += 1
    return '\n'.join(body), i


def _render_list(lines, i, pending_attrs):
    first = lines[i]
    ordered = bool(RE_OL.match(first.strip()))
    tag = 'ol' if ordered else 'ul'
    attrs = pending_attrs
    items = []          # (depth, text)
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            break
        m = RE_UL.match(line)
        n = RE_OL.match(line)
        if m:
            depth = len(m.group(1)) // 2
            items.append((depth, m.group(2)))
        elif n:
            depth = len(n.group(1)) // 2
            items.append((depth, n.group(3)))
        else:
            break
        i += 1
    return _build_list_html(items, tag, attrs), i


def _build_list_html(items, tag, attrs) -> str:
    """items: [(depth, text)]，按缩进还原嵌套列表结构。"""
    roots = []
    stack = [(-1, roots)]
    for depth, text in items:
        node = {'text': text, 'children': []}
        while stack and stack[-1][0] >= depth:
            stack.pop()
        parent = stack[-1][1] if stack else roots
        parent.append(node)
        stack.append((depth, node['children']))

    def render(nodes, top_tag, top_attrs, depth):
        use = top_tag if depth == 0 else 'ul'
        pad = '  ' * (depth + 1)
        default = DEFAULT_CLASSES.get(top_tag) if depth == 0 else NESTED_LIST_CLASS
        lines = [_tag_open(use, top_attrs if depth == 0 else None, default)]
        for n in nodes:
            if n['children']:
                inner = render(n['children'], use, top_attrs, depth + 1)
                lines.append(f'{pad}<li>{n["text"]}\n{inner}\n{pad}</li>')
            else:
                lines.append(f'{pad}<li>{n["text"]}</li>')
        lines.append('</' + use + '>')
        return '\n'.join(lines)

    return render(roots, tag, attrs, 0)


# ---------------------------------------------------------------- 归一化比较

RE_BETWEEN_TAGS = re.compile(r'>\s+<')
RE_TAG = re.compile(r'<[^>]+>')


def normalize(html: str) -> str:
    """忽略无意义空白的结构归一化（<pre> 内容保持原样）。"""
    blocks = []

    def keep(m):
        blocks.append(m.group(0))
        return f'\x00{len(blocks) - 1}\x00'

    protected = re.sub(r'<pre[\s\S]*?</pre>', keep, html)
    collapsed = re.sub(r'\s+', ' ', protected).replace('> <', '><')
    return re.sub(r'\x00(\d+)\x00', lambda m: blocks[int(m.group(1))], collapsed).strip()


def text_digest(html: str) -> str:
    """可见文本（去标签、折叠空白）。"""
    body = re.sub(r'<script[\s\S]*?</script>|<style[\s\S]*?</style>|<!--[\s\S]*?-->', ' ', html)
    return re.sub(r'\s+', ' ', RE_TAG.sub(' ', body)).strip()
