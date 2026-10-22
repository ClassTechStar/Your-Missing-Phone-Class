"""latex：把成品 HTML 转排为 LaTeX 书稿（配合 XeLaTeX + ctex 编译）。

设计要点：
- 复用 htmlparse 的解析树（字节无损），按"块级映射"生成 LaTeX，不做文本改写；
- 行内 HTML（strong/em/code/a/br）映射为 LaTeX 命令，Font Awesome 图标与 emoji 丢弃；
- 表格 → tabularx，代码块 → lstlisting，提示框 → tcolorbox，SVG → PDF 后插入；
- 输出分为 main.tex + chapters/*.tex，便于单章调试与增量编译。
"""

import html as html_mod
import json
import re
from pathlib import Path

from . import htmlparse as H

# ---------------------------------------------------------------- 转义与行内

SPECIALS = {
    '\\': r'\textbackslash{}',
    '&': r'\&',
    '%': r'\%',
    '$': r'\$',
    '#': r'\#',
    '_': r'\_',
    '{': r'\{',
    '}': r'\}',
    '~': r'\textasciitilde{}',
    '^': r'\textasciicircum{}',
}

RE_SPECIAL = re.compile(r'[\\&%$#_{}~^]')
RE_EMOJI = re.compile(
    '[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0000FE00-\U0000FE0F'
    '\U00002190-\U000021FF\U00002B00-\U00002BFF]')


def unescape(text: str) -> str:
    """还原 HTML 实体（&nbsp; &amp; &lt; …）。"""
    return html_mod.unescape(text)


def esc(text: str) -> str:
    """转义 LaTeX 特殊字符；保留 CJK 与中文标点。"""
    return RE_SPECIAL.sub(lambda m: SPECIALS[m.group(0)], text)


def clean(text: str) -> str:
    """去实体 → 去 emoji → 压缩空白 → 转义。"""
    t = unescape(text)
    t = RE_EMOJI.sub('', t)
    t = re.sub(r'\s*\n\s*', ' ', t)
    t = re.sub(r'[ \t]{2,}', ' ', t)
    return symbols(esc(t.strip()))


# 西文字体缺字形的符号替换表（编译日志里出现 Missing character 时补充）
SYMBOL_MAP = {}
for _i in range(1, 21):
    SYMBOL_MAP[chr(0x245F + _i)] = f'({_i})'      # ① … ⑳
SYMBOL_MAP['\u24ea'] = '(0)'                      # ⓪
SYMBOL_MAP['\u2713'] = '\u221a'                  # ✓ → √
SYMBOL_MAP['\u2717'] = '\u00d7'                  # ✗ → ×
SYMBOL_MAP['\u2714'] = '\u221a'
SYMBOL_MAP['\u2718'] = '\u00d7'
SYMBOL_MAP['\u2605'] = '*'                        # ★
SYMBOL_MAP['\u2606'] = '*'                        # ☆
SYMBOL_MAP['\u27a1'] = '\u2192'                  # ➡ → →
SYMBOL_MAP['\u2b50'] = '*'
SYMBOL_MAP['\u2318'] = 'Cmd'                       # ⌘
SYMBOL_MAP['\u2325'] = 'Option'                    # ⌥
SYMBOL_MAP['\u2303'] = 'Ctrl'                      # ⌃
SYMBOL_MAP['\u21e7'] = 'Shift'                     # ⇧
SYMBOL_MAP['\u2502'] = '|'                         # │
SYMBOL_MAP['\u25b6'] = '>'                         # ▶
SYMBOL_MAP['\u25bc'] = 'v'                         # ▼
SYMBOL_MAP['\u25be'] = 'v'                         # ▾
SYMBOL_MAP['\u2260'] = '$\\neq$'                  # ≠
SYMBOL_MAP['\u2265'] = '$\\geq$'                  # ≥
SYMBOL_MAP['\u2264'] = '$\\leq$'                  # ≤
SYMBOL_MAP['\u00b1'] = '$\\pm$'                   # ±
SYMBOL_MAP['\u03bc'] = '$\\mu$'                   # μ
SYMBOL_MAP['\u2248'] = '$\\approx$'               # ≈
SYMBOL_MAP['\u221e'] = '$\\infty$'                # ∞
SYMBOL_MAP['\ufe0f'] = ''                          # 变体选择符


def pair_quotes(text: str) -> str:
    """把成对的英文双引号换成中文弯引号（奇数个时最后一个按右引号处理）。"""
    out = []
    open_next = True
    for ch in text:
        if ch == '"':
            out.append('\u201c' if open_next else '\u201d')
            open_next = not open_next
        else:
            out.append(ch)
    return ''.join(out)


def symbols(text: str) -> str:
    return ''.join(SYMBOL_MAP.get(ch, ch) for ch in text)


def inline(node, out: list) -> None:
    """把节点的内容按行内语义追加到 out。"""
    if isinstance(node, str):
        out.append(clean(node))
        return
    if isinstance(node, H.Comment):
        return
    tag = node.tag
    if tag == 'i' and 'fas' in (node.get('class') or '').split():
        return                                    # Font Awesome 图标：无文字语义
    if tag in ('strong', 'b'):
        out.append(r'\textbf{')
        for c in node.children:
            inline(c, out)
        out.append('}')
        return
    if tag in ('em',):
        out.append(r'\emph{')
        for c in node.children:
            inline(c, out)
        out.append('}')
        return
    if tag == 'code':
        out.append(r'\texttt{')
        out.append(clean(node.text()))
        out.append('}')
        return
    if tag == 'br':
        out.append(r'\newline ')
        return
    if tag == 'a':
        href = node.get('href') or ''
        if href.startswith('http'):
            out.append(r'\href{' + esc(href) + '}{')
            for c in node.children:
                inline(c, out)
            out.append('}')
        else:
            for c in node.children:
                inline(c, out)
        return
    if tag == 'img':
        return
    for c in node.children:
        inline(c, out)


def inline_text(node) -> str:
    out = []
    inline(node, out)
    return ''.join(out)


def inline_text_of_children(node) -> str:
    out = []
    for c in node.children:
        inline(c, out)
    return ''.join(out)


# ---------------------------------------------------------------- 块级

CALLOUTS = {
    'info-box': 'tcbinfo',
    'warning-box': 'tcbwarn',
    'practice-box': 'tcbpractice',
}


def _heading_level(ctx, tag: str) -> str:
    """根据上下文把 h3/h4/h5 映射为无编号层级（书稿标题自带中文序号）。"""
    if tag == 'h3':
        return ctx['top']
    if tag == 'h4':
        return r'\booksubsection' if ctx['top'] == r'\booksection' else r'\booksection'
    if tag == 'h5':
        return r'\subsubsection*' if ctx['top'] == r'\booksection' else r'\booksubsection'
    return r'\paragraph*'


def _list_env(node) -> str:
    return 'enumerate' if node.tag == 'ol' else 'itemize'


def _render_list(node, indent=0):
    lines = ['  ' * indent + r'\begin{' + _list_env(node) + '}']
    for li in node.element_children():
        if li.tag != 'li':
            continue
        parts = []
        nested = []
        for c in li.children:
            if isinstance(c, H.Node) and c.tag in ('ul', 'ol'):
                nested.append(c)
            elif isinstance(c, H.Node) and c.tag == 'p':
                parts.append(inline_text_of_children(c))
            else:
                inline(c, parts)
        body = ''.join(parts).strip()
        lines.append('  ' * (indent + 1) + r'\item ' + body)
        for sub in nested:
            lines.append(_render_list(sub, indent + 1))
    lines.append('  ' * indent + r'\end{' + _list_env(node) + '}')
    return '\n'.join(lines)



def _mono_paragraph(node):
    """<p class="font-mono">：按 <br> 拆行的等宽代码块。"""
    lines, buf = [], []
    for c in node.children:
        if isinstance(c, H.Node) and c.tag == 'br':
            lines.append(''.join(buf).strip())
            buf = []
            continue
        inline(c, buf)
    last = ''.join(buf).strip()
    if last:
        lines.append(last)
    code = '\n'.join(l for l in lines if l)
    if not code:
        return []
    return '\n'.join([r'\begin{lstlisting}', code, r'\end{lstlisting}'])


def _table(node):
    """HTML 表格 → tabularx（表头按 th 数量均分列宽）。"""
    rows = []
    for tr in node.find_all('tr'):
        cells = []
        for cell in tr.element_children():
            if cell.tag in ('th', 'td'):
                cells.append(inline_text_of_children(cell).strip())
        if cells:
            rows.append(cells)
    if not rows:
        return []
    ncol = max(len(r) for r in rows)
    spec = '|' + '|'.join(['X'] * ncol) + '|'

    def row_tex(cells, bold=False):
        vals = [r'\textbf{' + c + '}' if bold else c for c in cells]
        # 单元格以 [ 开头时，会被误读为换行命令的可选参数，用 {} 阻断
        vals = [('{}' + v) if v.startswith('[') else v for v in vals]
        while len(vals) < ncol:
            vals.append('')
        return ' & '.join(vals) + r' \tabularnewline'

    lines = [r'\begin{center}',
             r'\begin{tabularx}{\linewidth}{' + spec + '}',
             r'\hline']
    lines.append(row_tex(rows[0], bold=True))
    lines.append(r'\hline')
    for r in rows[1:]:
        lines.append(row_tex(r))
    lines.append(r'\hline')
    lines += [r'\end{tabularx}', r'\end{center}']
    return '\n'.join(lines)


def _code_block(node, ctx):
    """code-block（可能含 code-head）+ pre → lstlisting。"""
    head = None
    pre = None
    for c in node.element_children():
        if c.tag == 'div' and 'code-head' in c.classes:
            spans = c.find_all('span')
            if spans:
                head = clean(spans[0].text())
        elif c.tag == 'pre':
            pre = c
    if pre is None and node.tag == 'pre':
        pre = node
    if pre is None:
        return []
    code = symbols(RE_EMOJI.sub('', unescape(pre.text()))).replace('\ufe0f', '').rstrip('\n')
    lang = ''
    if head:
        low = head.lower()
        for key, name in (('kts', 'Kotlin'), ('kotlin', 'Kotlin'), ('gradle', 'Kotlin'),
                          ('swiftui', 'Swift'), ('swift', 'Swift'), ('python', 'Python'),
                          ('javascript', 'JavaScript'), ('jsx', 'JavaScript'),
                          ('typescript', 'TypeScript'),
                          ('java', 'Java'), ('html', 'HTML'), ('xml', 'HTML'),
                          ('bash', 'bash'), ('shell', 'bash'), ('sql', 'SQL')):
            if key in low:
                lang = name
                break
    opts = ''
    if lang:
        opts = f'[language={lang}]'
    return '\n'.join([r'\begin{lstlisting}' + opts, code, r'\end{lstlisting}'])


def _callout(node, ctx, env):
    """提示框：首段作为标题，其余作为正文。"""
    children = node.element_children()
    title = ''
    body_start = 0
    if children and children[0].tag == 'p':
        title = inline_text_of_children(children[0]).strip().rstrip('：:')
        body_start = 1
    lines = [r'\begin{' + env + '}{' + title + '}']
    for c in children[body_start:]:
        for b in blocks(c, ctx):
            lines.append(b)
            lines.append('')
    lines.append(r'\end{' + env + '}')
    return '\n'.join(lines)


def blocks(node, ctx) -> list:
    """把一个块级节点转成 LaTeX 行列表。"""
    if isinstance(node, str):
        t = clean(node)
        return [t] if t else []
    if isinstance(node, H.Comment):
        return []

    tag = node.tag
    classes = node.classes

    if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
        lvl = _heading_level(ctx, tag)
        title = inline_text_of_children(node).strip()
        if tag in ('h4', 'h5'):
            title = re.sub(r'^\d+\s*[.、]\s*', '', title)
        if not title:
            return []
        return [f'{lvl}{{{pair_quotes(title)}}}']

    if tag == 'p':
        text = inline_text_of_children(node).strip()
        if not text:
            return []
        text = pair_quotes(text)
        if 'font-mono' in classes:
            return _mono_paragraph(node)
        if 'chapter-intro' in classes:
            return [r'\chapterintro{' + text + '}']
        if 'font-semibold' in classes:
            return [r'\textbf{' + text + r'}\par']
        if 'text-xs' in classes and 'text-gray-500' in classes:
            return [r'\begin{center}\small\color{gray}' + text + r'\end{center}']
        return [text]

    if tag in ('ul', 'ol'):
        return [_render_list(node)]

    if tag == 'table':
        return [_table(node)]

    if tag == 'pre' or (tag == 'div' and 'code-block' in classes):
        return [_code_block(node, ctx)]

    if tag == 'hr':
        return [r'\bigskip']

    if tag == 'div':
        if 'figure' in classes or node.find('svg') is not None:
            return [_figure(node, ctx)]
        if 'chapter-summary' in classes:
            return [_callout(node, ctx, 'tcbsummary')]
        for cls, env in CALLOUTS.items():
            if cls in classes:
                return [_callout(node, ctx, env)]
        if 'overflow-x-auto' in classes:
            out = []
            for c in node.children:
                out.extend(blocks(c, ctx))
            return out
        out = []
        for c in node.children:
            out.extend(blocks(c, ctx))
        return out

    if tag in ('section', 'article', 'aside', 'header', 'footer', 'blockquote',
               'nav', 'main', 'dl', 'dd', 'dt'):
        out = []
        for c in node.children:
            out.extend(blocks(c, ctx))
        return out

    if tag == 'details':
        out = []
        for c in node.children:
            if isinstance(c, H.Node) and c.tag == 'summary':
                out.append(r'\textbf{' + inline_text_of_children(c).strip() + r'}\par')
            else:
                out.extend(blocks(c, ctx))
        return out

    # 兜底：只取文本
    text = inline_text_of_children(node).strip()
    return [text] if text else []


# ---------------------------------------------------------------- 图形

def _figure(node, ctx):
    """SVG → PDF（需要 svglib + reportlab），失败则输出占位说明。"""
    svg = node.find('svg')
    if svg is None:
        out = []
        for c in node.children:
            out.extend(blocks(c, ctx))
        return '\n\n'.join(out)

    ctx['figure_seq'] += 1
    name = f"fig-{ctx['chapter_id']}-{ctx['figure_seq']}"
    outdir = ctx['figures_dir']
    outdir.mkdir(parents=True, exist_ok=True)
    pdf = outdir / f'{name}.pdf'
    if not pdf.exists() and ctx['svg_converter']:
        ok = ctx['svg_converter'](H.render(svg), pdf)
    else:
        ok = pdf.exists()
    caption = ''
    for p in node.find_all('p'):
        t = inline_text_of_children(p).strip()
        if t:
            caption = t
            break
    if ok:
        lines = [r'\begin{center}',
                 r'\includegraphics[width=0.92\linewidth]{figures/' + name + '}']
        if caption:
            lines.append(r'\\[2pt]\small ' + caption)
        lines.append(r'\end{center}')
        return '\n'.join(lines)
    if caption:
        return [r'\begin{center}\small 【图示：' + caption + r'，详见在线版】\end{center}']
    return []


def make_svg_converter():
    """返回 svg 文本 → pdf 的转换函数；依赖缺失时返回 None。"""
    try:
        from io import BytesIO
        from svglib.svglib import svg2rlg
        from reportlab.graphics import renderPDF
    except Exception:
        return None

    def convert(svg_text: str, pdf_path: Path) -> bool:
        try:
            # svglib 无法解析 style 里的 auto 值（如 height:auto），先剥离行内样式
            svg_text = re.sub(r'(<svg[^>]*?)\sstyle="[^"]*"', r'\1', svg_text, count=1)
            # reportlab 默认字体无中文字形：把 SVG 文本的字体统一映射到内置 CID 中文字体
            from reportlab.pdfbase import pdfmetrics
            from reportlab.pdfbase.cidfonts import UnicodeCIDFont
            try:
                pdfmetrics.getFont('STSong-Light')
            except Exception:
                pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
            svg_text = re.sub(r'font-family="[^"]*"', 'font-family="STSong-Light"', svg_text)
            svg_text = re.sub(r"font-family='[^']*'", "font-family='STSong-Light'", svg_text)
            svg_text = re.sub(r'font-family:([^;"\']+)', 'font-family:STSong-Light', svg_text)
            # 文本元素未声明字体时 svglib 落到 Helvetica（无中文字形）→ 在根节点统一指定
            svg_text = svg_text.replace('<svg ', '<svg font-family="STSong-Light" ', 1)
            if not svg_text.lstrip().startswith('<?xml'):
                svg_text = '<?xml version="1.0" encoding="UTF-8"?>\n' + svg_text
            drawing = svg2rlg(BytesIO(svg_text.encode('utf-8')))
            if drawing is None:
                return False
            renderPDF.drawToFile(drawing, str(pdf_path))
            return pdf_path.is_file() and pdf_path.stat().st_size > 0
        except Exception:
            return False

    return convert


# ---------------------------------------------------------------- 章节与书稿

PARTS_LABEL = {
    'ji-chu-pian': '第一篇　基础篇',
    'ruan-jian-pian': '第二篇　软件篇',
    'jin-jie-pian': '第三篇　进阶篇',
    'chao-yue-pian': '第四篇　超越篇',
    'shi-zhan-pian': '第五篇　实战篇',
    'zhan-wang-pian': '第六篇　展望篇与车联篇',
    'er-tong-pian': '第七篇　儿童与手机专题',
    'ai-biancheng-pian': '第八篇　AI 编程实战篇',
    'an-zhuo-kai-fa-pian': '第九篇　安卓开发实战篇',
    'ios-kai-fa-pian': '第十篇　iOS 开发实战篇',
    'fu-lu': '附录',
}


def _flatten(items):
    """把嵌套列表摊平为字符串序列（防御性，抵住各分支返回类型不一致）。"""
    out = []
    for it in items:
        if isinstance(it, list):
            out.extend(_flatten(it))
        elif isinstance(it, str):
            out.append(it)
    return out


def chapter_blocks(cnode, ctx):
    """单个 content-section → LaTeX 行列表（首标题作为章/节命令）。"""
    kind = ctx['kind']
    ctx['top'] = r'\booksection' if kind == 'supplement' else r'\bookchapter'
    out = []
    for c in cnode.children:
        out.extend(blocks(c, ctx))
    ctx['top'] = r'\bookchapter'
    return '\n\n'.join(_flatten(out))


def build(root: Path, out_dir: Path = None, lang: str = 'zh-CN',
          version: str = None, book_path: Path = None) -> dict:
    """生成 LaTeX 书稿：main.tex + chapters/*.tex + figures/*.pdf。"""
    book_rel = Path(book_path) if book_path else Path('source/book.json')
    book = json.loads((root / book_rel).read_text(encoding='utf-8'))
    version = version or book['version']
    out = Path(out_dir) if out_dir else (root / 'latex')
    (out / 'chapters').mkdir(parents=True, exist_ok=True)
    (out / 'figures').mkdir(parents=True, exist_ok=True)

    html_path = root / version / f'{lang}.html'
    raw = html_path.read_text(encoding='utf-8')
    tree = H.parse(raw)

    sections = {}
    for n in tree.find_all('div'):
        if 'content-section' in n.classes:
            sections[n.get('id')] = n

    ctx = {'figure_seq': 0, 'chapter_id': 'x', 'kind': 'chapter', 'top': r'\chapter',
           'figures_dir': out / 'figures', 'svg_converter': make_svg_converter()}

    order = []
    for ch in book['chapters']:
        cid = ch['id']
        node = sections.get(cid)
        if node is None:
            continue
        ctx['chapter_id'] = cid
        ctx['kind'] = ch.get('kind', 'chapter')
        ctx['figure_seq'] = 0
        body = chapter_blocks(node, ctx)
        rel = f'chapters/{Path(ch["file"]).stem}.tex'
        (out / rel).write_text(body.rstrip() + '\n', encoding='utf-8', newline='\n')
        order.append((ch, rel))

    # ---- main.tex ----
    parts = {p['id']: p for p in book['parts']}
    lines = []
    lines.append(r'\documentclass[11pt,a4paper,openany]{book}')
    lines.append(r'\usepackage[UTF8, fontset=windows]{ctex}')
    lines.append(r'\usepackage{geometry}')
    lines.append(r'\geometry{a4paper,left=2.6cm,right=2.6cm,top=2.6cm,bottom=2.4cm}')
    lines.append(r'\usepackage{xcolor}')
    lines.append(r'\usepackage{graphicx}')
    lines.append(r'\usepackage{booktabs}')
    lines.append(r'\usepackage{tabularx}')
    lines.append(r'\usepackage{enumitem}')
    lines.append(r'\usepackage{listings}')
    lines.append(r'\usepackage{tcolorbox}')
    lines.append(r'\tcbuselibrary{skins,breakable}')
    lines.append(r'\usepackage{fancyhdr}')
    lines.append(r'\usepackage[colorlinks=true,linkcolor=black,urlcolor=blue,citecolor=black]{hyperref}')
    lines.append(r'\usepackage{titlesec}')
    lines.append('')
    # 版式
    lines.append(r'\setCJKmainfont[BoldFont=SimHei,ItalicFont=KaiTi]{SimSun}')
    lines.append(r'\setCJKsansfont{SimHei}')
    lines.append(r'\setCJKmonofont{SimSun}')
    lines.append(r'\setlength{\parindent}{2em}')
    lines.append(r'\setlength{\parskip}{3pt}')
    lines.append(r'\renewcommand{\baselinestretch}{1.25}')
    lines.append(r'\pagestyle{fancy}')
    lines.append(r'\fancyhf{}')
    lines.append(r'\fancyhead[LE,RO]{\small\thepage}')
    lines.append(r'\fancyhead[RE]{\small\nouppercase{\leftmark}}')
    lines.append(r'\fancyhead[LO]{\small\nouppercase{\rightmark}}')
    lines.append(r'\setlength{\headheight}{14pt}')
    lines.append('')
    # 代码块样式
    lines.append(r'\definecolor{codebg}{gray}{0.96}')
    lines.append(r'\lstset{')
    lines.append(r'  basicstyle=\ttfamily\small,')
    lines.append(r'  backgroundcolor=\color{codebg},')
    lines.append(r'  frame=single,framerule=0.3pt,rulecolor=\color{gray!60},')
    lines.append(r'  breaklines=true,breakatwhitespace=false,')
    lines.append(r'  columns=fullflexible,keepspaces=true,')
    lines.append(r'  xleftmargin=6pt,xrightmargin=6pt,')
    lines.append(r'  aboveskip=6pt,belowskip=6pt,')
    lines.append(r'  showstringspaces=false,tabsize=2,')
    lines.append(r'  extendedchars=true,')
    lines.append(r'}')
    lines.append('')
    # 提示框
    for env, back, frame in (('tcbinfo', 'blue!5', 'blue!40'),
                             ('tcbwarn', 'orange!6', 'orange!55'),
                             ('tcbpractice', 'green!5', 'green!45'),
                             ('tcbsummary', 'gray!6', 'gray!45')):
        lines.append(r'\newtcolorbox{' + env + r'}[1]{breakable,enhanced,')
        lines.append(r'  colback=' + back + r',colframe=' + frame + r',')
        lines.append(r'  boxrule=0.4pt,left=6pt,right=6pt,top=4pt,bottom=4pt,')
        lines.append(r'  fonttitle=\bfseries,arc=2pt,title={#1}}')
    lines.append('')
    lines.append(r'\newcommand{\chapterintro}[1]{\textit{#1}\par\bigskip}')
    lines.append(r'\newcommand{\bookchapter}[1]{\chapter*{#1}\addcontentsline{toc}{chapter}{#1}\markboth{#1}{}}')
    lines.append(r'\newcommand{\booksection}[1]{\section*{#1}\addcontentsline{toc}{section}{#1}\markright{#1}}')
    lines.append(r'\newcommand{\booksubsection}[1]{\subsection*{#1}}')
    lines.append(r'\lstdefinelanguage{Kotlin}{keywords={fun,val,var,class,object,interface,when,if,else,return,for,while,do,try,catch,finally,import,package,is,in,null,true,false,this,super,override,suspend,data,sealed,companion,lazy,by},sensitive=true,comment=[l]{//},morecomment=[s]{/*}{*/},morestring=[b]",morestring=[b]\'}')
    lines.append(r'\lstdefinelanguage{Swift}{keywords={func,let,var,class,struct,enum,protocol,extension,import,if,else,return,for,in,while,guard,switch,case,default,try,catch,throw,throws,self,init,deinit,override,public,private,internal,static,mutating,async,await,nil,true,false,some,any},sensitive=true,comment=[l]{//},morecomment=[s]{/*}{*/},morestring=[b]"}')
    lines.append(r'\lstdefinelanguage{JavaScript}{keywords={function,const,let,var,if,else,return,for,while,class,import,export,from,async,await,new,try,catch,typeof,null,true,false,this,undefined},sensitive=true,comment=[l]{//},morecomment=[s]{/*}{*/},morestring=[b]",morestring=[b]\',morestring=[b]`}')
    lines.append(r'\lstdefinelanguage{TypeScript}{keywords={function,const,let,var,if,else,return,for,while,class,interface,type,import,export,from,async,await,new,try,catch,typeof,null,true,false,this,undefined,enum,implements,extends},sensitive=true,comment=[l]{//},morecomment=[s]{/*}{*/},morestring=[b]",morestring=[b]\',morestring=[b]`}')
    lines.append('')
    title = book.get('title', '你缺失的那门手机课')
    lines.append(r'\title{' + esc(title) + r'\\ \large ' + version + r'}')
    lines.append(r'\author{ClassTechStar}')
    lines.append(r'\date{}')
    lines.append('')
    lines.append(r'\hypersetup{pdftitle={' + esc(title) + ' ' + version + r'},')
    lines.append(r'  pdfauthor={ClassTechStar},pdfcreator={XeLaTeX + ctex},')
    lines.append(r'  pdfsubject={69 章 + 8 附录的智能手机使用指南},bookmarksnumbered=true}')
    lines.append(r'\begin{document}')
    lines.append(r'\begin{titlepage}')
    lines.append(r'\centering')
    lines.append(r'\vspace*{0.28\textheight}')
    lines.append(r'{\Huge\bfseries ' + esc(title) + r'\par}')
    lines.append(r'\vspace{1.2em}')
    lines.append(r'{\Large ' + version + r'\par}')
    lines.append(r'\vspace{3em}')
    lines.append(r'{\large 69 章 + 8 附录 \quad 从零基础到 App 开发者\par}')
    lines.append(r'\vfill')
    lines.append(r'{\large ClassTechStar\par}')
    lines.append(r'\end{titlepage}')
    lines.append(r'\frontmatter')
    lines.append(r'\tableofcontents')
    lines.append(r'\mainmatter')

    current_part = None
    for ch, rel in order:
        pid = ch.get('part') or ch.get('after_part')
        if pid and pid != current_part:
            current_part = pid
            label = PARTS_LABEL.get(pid) or (parts.get(pid, {}).get('nav', pid))
            if pid == 'fu-lu':
                lines.append(r'\appendix')
            lines.append(r'\part*{' + esc(label) + '}')
            if pid != 'fu-lu':
                lines.append(r'\addcontentsline{toc}{part}{' + esc(label) + '}')
        lines.append(r'\input{' + rel.replace('\\', '/') + '}')

    lines.append(r'\end{document}')
    (out / 'main.tex').write_text('\n'.join(lines) + '\n', encoding='utf-8', newline='\n')

    return {'out': str(out), 'chapters': len(order),
            'main': str(out / 'main.tex'),
            'figures': sorted(p.name for p in (out / 'figures').glob('*.pdf'))}
