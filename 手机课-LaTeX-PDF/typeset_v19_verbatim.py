#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""v1.9 逐字保真 LaTeX 排版流水线（分段编译、逐章核对）。

与旧 typeset.py 的差别：
- 按 120 个 <div class="mb-10 content-section"> 自行切分，不依赖 <section> 篇归属
  （旧版在这份 v1.9 上只识别出 69 章）。
- 禁止一切文字改写：不配对引号、不删 emoji、不替换符号、不压缩特殊空格。
- LaTeX 不产生任何额外可提取文本：无页码页眉、章节/列表无自动编号、代码无行号。
- emoji/变体选择符用 accsupp 的 ActualText 保留在 PDF 文本层，视觉用替代字形。

用法：
    python typeset_v19_verbatim.py build                 # 切章 + 生成基准与全部 tex
    python typeset_v19_verbatim.py chapter 0 1          # 编译指定章（0-based）
    python typeset_v19_verbatim.py verify 0 1           # 逐章 pdftotext 核对
    python typeset_v19_verbatim.py all                  # 全量编译（后续批次）
    python typeset_v19_verbatim.py merge                # 合并成品 PDF
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import unicodedata
from html.parser import HTMLParser
from pathlib import Path

REPO = Path(r'C:\Users\18948\Documents\GitHub\Your-Missing-Phone-Class')
HTML = REPO / '你缺失的那门手机课V1.9Fixed.html'
BASE = Path(r'C:\Users\18948\AppData\Local\Temp\v19verbatim')
OUT_PDF = REPO / '手机课-LaTeX-PDF' / 'pdf' / 'v1.9-verbatim'
MIKTEX = r'C:\Program Files\MiKTeX\miktex\bin\x64'
XELATEX = str(Path(MIKTEX) / 'xelatex.exe')
PDFTOTEXT = str(Path(MIKTEX) / 'pdftotext.exe')
PDFUNITE = str(Path(MIKTEX) / 'pdfunite.exe')

VOID = {'br', 'img', 'hr', 'input', 'meta', 'link', 'source', 'wbr', 'area', 'base', 'col', 'embed', 'param', 'track'}
SKIP = {'script', 'style', 'button', 'nav', 'svg', 'i', 'select', 'option', 'textarea'}
EMOJI = re.compile(r'[\U0001F000-\U0001FAFF\u2600-\u27BF]')
# 字体 cmap 易被 pdftotext 误映射的符号：用 ActualText 锁定文本层
ACC = re.compile(r'[\u2190-\u21FF\u2300-\u23FF\u2460-\u25FF]')


# ---------------- DOM ----------------
class Node:
    __slots__ = ('tag', 'attrs', 'kids')

    def __init__(self, tag, attrs=None):
        self.tag = tag
        self.attrs = attrs or {}
        self.kids = []

    @property
    def classes(self):
        return self.attrs.get('class', '').split()


class Builder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node('#root')
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        n = Node(tag, dict(attrs))
        self.stack[-1].kids.append(n)
        if tag not in VOID:
            self.stack.append(n)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1].kids.append(Node(tag, dict(attrs)))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        self.stack[-1].kids.append(data)


def parse(html: str) -> Node:
    b = Builder()
    b.feed(html)
    return b.root


def text_of(n) -> str:
    if isinstance(n, str):
        return n
    if n.tag in SKIP or n.tag == '#root':
        return ''.join(text_of(k) for k in n.kids) if n.tag == '#root' else ''
    return ''.join(text_of(k) for k in n.kids)


# ---------------- 逐字保真转义 ----------------
SPECIAL = {
    '\\': r'\textbackslash{}', '&': r'\&', '%': r'\%', '$': r'\$',
    '#': r'\#', '_': r'\_', '{': r'\{', '}': r'\}',
    '~': r'\textasciitilde{}', '^': r'\textasciicircum{}',
    '"': r'\textquotedbl{}', "'": r'\textquotesingle{}',
}
RE_SPECIAL = re.compile(r'[\\&%$#_{}~^"\']')


BREAK = '\x00'
RTL = re.compile(r'[\u0590-\u08ff\ufb50-\ufdff\ufe70-\ufeff]+')


def esc(t: str) -> str:
    """只做 LaTeX 语法转义，绝不做任何文字改写。

    长 ASCII 串（无空格）每 10 字符插一个零宽断点 \\allowbreak{}，
    防止中文段落里的长标识符/h 堆栈顶出页面右边界被裁。
    """
    t = re.sub(r'([A-Za-z0-9.:/()]{10})(?=[A-Za-z0-9.:/()])', r'\1' + BREAK, t)
    out = []
    i = 0
    while i < len(t):
        ch = t[i]
        if ch == BREAK:
            out.append(r'\allowbreak{}')
            i += 1
            continue
        if '\u0590' <= ch <= '\u08ff':
            # 阿拉伯/希伯来：挂 Script=Arabic 字体，保证 shaping 与 ToUnicode 正常
            j = i + 1
            while j < len(t) and '\u0590' <= t[j] <= '\u08ff':
                j += 1
            # 前后各放一个 U+200E（LRM），把 LTR 边界钉住，
            # 否则相邻中文顿号会被卷进 RTL run 并重排（比对时 LRM 两侧均剔除）。
            out.append('\u200e' + r'{\arabicfont ' + t[i:j] + '}' + '\u200e')
            i = j
            continue
        if EMOJI.match(ch) or ch == '\ufe0f':
            j = i + 1
            while j < len(t) and (EMOJI.match(t[j]) or t[j] == '\ufe0f'):
                j += 1
            raw = t[i:j]
            # 字体分工：彩色 emoji 用 Segoe UI Emoji；其余符号（➜ ✅ ⚠ ✓ ★ 等）
            # 用 Segoe UI Symbol——实测后者 ToUnicode 完整，前者缺 ➜ 字形。
            font = r'\emojifont' if ord(t[i]) >= 0x1F000 else r'\symfont'
            out.append('{' + font + ' ' + raw + '}')
            i = j
            continue
        if ACC.match(ch):
            out.append(r'{\symfont ' + ch + '}')
            i += 1
            continue
        # Times New Roman 的 ";" 映射成 U+037E、Consolas 的 "-" 映射成 U+2010；
        # << / >> 是 TeX ligature；行首 [..] 会被当成命令可选参数吞掉。
        if ch in '-;':
            out.append(r'{\symfont ' + ch + '}')
            i += 1
            continue
        if ch in '<>':
            out.append(r'\textless{}' if ch == '<' else r'\textgreater{}')
            i += 1
            continue
        if ch in '[]':
            out.append('{[}' if ch == '[' else '{]}')
            i += 1
            continue
        out.append(SPECIAL.get(ch, ch))
        i += 1
    return ''.join(out)


# ---------------- LaTeX 生成 ----------------
HEADING = {'h1': r'\chapter*', 'h2': r'\chapter*', 'h3': r'\chapter*',
           'h4': r'\section*', 'h5': r'\subsection*', 'h6': r'\subsubsection*'}
BOX = {'tip-box': ('tip', '4C8DAE'), 'info-box': ('info', '3E7B9E'),
       'warning-box': ('warn', 'C98A2B'), 'success-box': ('ok', '3E8E6E'),
       'practice-box': ('tip', '4C8DAE'), 'danger-box': ('warn', 'C98A2B')}


def inline(n, out: list) -> None:
    if isinstance(n, str):
        out.append(esc(n))
        return
    tag = n.tag
    if tag in SKIP:
        return
    if tag == 'br':
        out.append(r'\newline{}')
        return
    if tag in ('strong', 'b'):
        out.append(r'\textbf{')
    elif tag in ('em', 'i2'):
        out.append(r'\emph{')
    elif tag in ('code', 'kbd', 'samp'):
        out.append(r'\texttt{')
    elif tag == 'a':
        out.append('')
    else:
        out.append('')
    opened = tag in ('strong', 'b', 'em', 'i2', 'code', 'kbd', 'samp')
    for k in n.kids:
        inline(k, out)
    if opened:
        out.append('}')


def _alltt(code: str) -> str:
    """代码块：alltt 原样输出，只转义 \\ { }，并把 - ; 交给 ToUnicode 正常的字体。"""
    o = []
    for ch in code:
        if ch == '\\':
            o.append(r'\\')
        elif ch == '{':
            o.append(r'\{')
        elif ch == '}':
            o.append(r'\}')
        elif ch in '-;':
            o.append(r'{\symfont ' + ch + '}')
        else:
            o.append(ch)
    return ''.join(o)


def _wrap_code(code: str, width: int = 72) -> str:
    """代码块硬折行：listings 的 breaklines 对超长行不总是生效，
    溢出页边的内容会被裁掉。按宽度折行不改变文字（去空白比对无影响）。"""
    out = []
    for line in code.split('\n'):
        while len(line) > width:
            cut = line.rfind(' ', 0, width + 1)
            if cut < width // 2:
                cut = width
            out.append(line[:cut])
            line = line[cut:]
        out.append(line)
    return '\n'.join(out)


def render_block(n, out: list, depth: int = 0) -> None:
    if isinstance(n, str):
        s = n.strip()
        if s:
            out.append(esc(s))
        return
    tag = n.tag
    if tag in SKIP:
        return
    cls = n.classes
    if tag in HEADING:
        out.append(HEADING[tag] + '{' + ''.join(_flatten_inline(n.kids)) + '}')
        return
    if tag == 'p':
        out.append(''.join(_flatten_inline(n.kids)) + '\n')
        return
    if tag in ('ul', 'ol'):
        out.append(r'\begin{listless}')
        for li in n.kids:
            if isinstance(li, Node) and li.tag == 'li':
                out.append(r'\item ' + ''.join(_flatten_inline(li.kids)) + '\n')
            elif isinstance(li, str) and li.strip():
                out.append(r'\item ' + esc(li.strip()) + '\n')
        out.append(r'\end{listless}')
        return
    if tag == 'table':
        _table(n, out)
        return
    if tag in ('pre',):
        code = _wrap_code(text_of(n))
        # 代码块里的 emoji 用 escapeinside 开口插字体命令，否则 Consolas 无字形→U+FFFD
        code = EMOJI.sub(
            lambda m: '(*@' + (r'\emojifont' if ord(m.group(0)[0]) >= 0x1F000 else r'\symfont')
                      + ' ' + m.group(0) + '@*)', code)
        out.append(r'\begin{lstlisting}' + '\n' + code.rstrip('\n') + '\n' + r'\end{lstlisting}')
        return
    if tag == 'div' and any(c in BOX for c in cls):
        env, _ = next((BOX[c] for c in cls if c in BOX), ('tip', '4C8DAE'))
        out.append(r'\begin{vboxx}{' + env + '}')
        for k in n.kids:
            render_block(k, out, depth + 1)
        out.append(r'\end{vboxx}')
        return
    if tag in ('div', 'section', 'article', 'main', 'blockquote', 'figure', 'figcaption', 'span', 'li', 'tr', 'td', 'th', 'thead', 'tbody', 'ol', 'p'):
        for k in n.kids:
            render_block(k, out, depth)
        return
    for k in n.kids:
        render_block(k, out, depth)


def _flatten_inline(kids) -> list:
    o = []
    for k in kids:
        inline(k, o)
    return o


def _table(n, out: list) -> None:
    rows = []

    def collect(x):
        if isinstance(x, Node):
            if x.tag == 'tr':
                cells = []
                for c in x.kids:
                    if isinstance(c, Node) and c.tag in ('td', 'th'):
                        cells.append(''.join(_flatten_inline(c.kids)).replace(r'\newline{}', ' '))
                if cells:
                    rows.append(cells)
                return
            for k in x.kids:
                collect(k)
    collect(n)
    if not rows:
        return
    ncol = max(len(r) for r in rows)
    # 用 longtable：tabular 不跨页，长表格（如附录 C 术语表）超页内容会被裁掉。
    colw = r'p{\dimexpr\linewidth/' + str(ncol) + r'-2\tabcolsep\relax}'
    out.append(r'\par\small\begin{longtable}{' + colw * ncol + r'}\hline')
    for r in rows:
        cells = (r + [''] * ncol)[:ncol]
        out.append(' & '.join(cells) + r'\tabularnewline')
    out.append(r'\end{longtable}\par')


PREAMBLE = r'''\documentclass[11pt,a4paper,openany]{book}
\usepackage[UTF8,fontset=none]{ctex}
\usepackage{fontspec}
\usepackage{xeCJK}
\defaultfontfeatures{Ligatures=NoCommon,NoRare,NoDiscretionary,HyphenChar=None}
\setCJKmainfont[BoldFont=SimHei]{SimSun}
\setCJKsansfont{SimHei}
\setCJKmonofont{SimSun}
\setmainfont{Times New Roman}
\setsansfont{Arial}
\setmonofont{Consolas}
\newfontfamily\arabicfont[Script=Arabic]{Arial}
\newfontfamily\symfont{Segoe UI Symbol}
\newfontfamily\emojifont{Segoe UI Emoji}
\usepackage{geometry}
\geometry{a4paper,left=2.6cm,right=2.6cm,top=2.4cm,bottom=2.2cm}
\usepackage{xcolor}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{enumitem}
\usepackage{listings}
\lstset{basicstyle=\ttfamily\small,columns=fullflexible,breaklines=true,
breakatwhitespace=false,showstringspaces=false,xleftmargin=0pt,aboveskip=4pt,belowskip=4pt,
escapeinside={(*@}{@*)}}
\usepackage{longtable}
\usepackage{tcolorbox}
\tcbuselibrary{skins,breakable}
\usepackage{accsupp}
\makeatletter\ACCSUPP@unicodetrue\makeatother
\usepackage{titlesec}
\usepackage{hyperref}
\pagestyle{empty}
\makeatletter\let\ps@plain\ps@empty\makeatother
\hyphenpenalty=50
\exhyphenpenalty=50
\hyphenchar\font=-1
\emergencystretch=3em
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt plus 2pt}
\titleformat{\chapter}[display]{\normalfont\LARGE\bfseries\color[HTML]{0A1F3D}}{}{0pt}{}
\titleformat{\section}{\Large\bfseries\color[HTML]{0A1F3D}}{}{0pt}{}
\titleformat{\subsection}{\large\bfseries\color[HTML]{0A1F3D}}{}{0pt}{}
\newlist{listless}{itemize}{2}
\setlist[listless]{label={},leftmargin=1.6em,itemsep=2pt,topsep=3pt,parsep=0pt}
\newenvironment{tablebox}[1]{\par\small\begin{tabularx}{\linewidth}{#1}\hline}{\end{tabularx}\par}
\newenvironment{vboxx}[1]{\par\begin{tcolorbox}[breakable,colback=gray!6,colframe=gray!45,boxrule=0.4pt,arc=2pt,left=6pt,right=6pt,top=5pt,bottom=5pt]}{\end{tcolorbox}\par}
\newcommand{\bookpart}[1]{\chapter*{#1}}
\begin{document}
'''


def chapter_tex(body: str) -> str:
    return PREAMBLE + body + '\n\\end{document}\n'


# ---------------- 主流程 ----------------
def load_chapters():
    raw = HTML.read_text(encoding='utf-8')
    pat = re.compile(r'<div id="([^"]+)" class="mb-10 content-section">(.*?)(?=<div id="[^"]+" class="mb-10 content-section">|\Z)', re.S)
    out = []
    for cid, html in pat.findall(raw):
        html = re.sub(r'<script\b.*?</script>|<style\b.*?</style>', '', html, flags=re.S | re.I)
        root = parse(html)
        base = ''.join(text_of(k) for k in root.kids)
        out.append((cid, root, base))
    return out


def build():
    BASE.mkdir(parents=True, exist_ok=True)
    OUT_PDF.mkdir(parents=True, exist_ok=True)
    chs = load_chapters()
    manifest = []
    for i, (cid, root, base) in enumerate(chs):
        lines = []
        for k in root.kids:
            render_block(k, lines)
        tex = chapter_tex('\n\n'.join(lines))
        (BASE / f'ch{i:03d}-{cid}.tex').write_text(tex, encoding='utf-8', newline='\n')
        (BASE / f'ch{i:03d}-{cid}.base.txt').write_text(base, encoding='utf-8', newline='\n')
        manifest.append({'i': i, 'id': cid, 'chars': len(base),
                         'tex': f'ch{i:03d}-{cid}.tex'})
    (BASE / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'生成 {len(manifest)} 章 tex + 基准，基准总字符 {sum(m["chars"] for m in manifest)}')


def compile_one(i: int):
    mani = json.loads((BASE / 'manifest.json').read_text(encoding='utf-8'))
    m = mani[i]
    stem = Path(m['tex']).stem
    dst = OUT_PDF / (stem + '.pdf')
    # 不删除旧 PDF（批量重编会触发宿主批量删除保护）；改为覆盖写入 +
    # verify 阶段用时间戳校验新鲜度，同样能防编译失败时旧文件冒充。
    env = dict(os.environ)
    env['PATH'] = MIKTEX + os.pathsep + env.get('PATH', '')
    env['TEXINPUTS'] = str(BASE) + os.pathsep + env.get('TEXINPUTS', '')
    for _ in range(2):
        r = subprocess.run([XELATEX, '-interaction=nonstopmode', '-halt-on-error',
                            '-output-directory', str(BASE), m['tex']],
                           cwd=str(BASE), env=env, capture_output=True, text=True,
                           encoding='utf-8', errors='replace', timeout=900)
        if r.returncode != 0:
            log = (r.stdout or '')[-1500:]
            return {'i': i, 'id': m['id'], 'ok': False, 'err': log}
    pdf = BASE / (stem + '.pdf')
    if not pdf.exists():
        return {'i': i, 'id': m['id'], 'ok': False, 'err': 'no pdf'}
    dst = OUT_PDF / (stem + '.pdf')
    dst.write_bytes(pdf.read_bytes())
    return {'i': i, 'id': m['id'], 'ok': True, 'pdf': str(dst)}


WS = re.compile(r'\s+')


TRANS = str.maketrans({'\u2010': '-', '\u037e': ';', '\u2011': '-', '\u2012': '-', '\u2013': '-'})


def norm(s: str) -> str:
    """比对规范化（两侧同时施加，并在报告中明示）：
    1) 去空白、BOM；
    2) 去不可见变体选择符 U+FE0F 与双向控制符 U+200E/200F/202B/202C；
    3) 字体 ToUnicode 造成的「同字形异码位」归一：U+2010/2011/2012/2013 → ASCII '-'，
       U+037E（希腊问号，字形同分号）→ ASCII '; '。
    其余每个文字字符严格逐字比对，不做简繁转换、同义替换或标点改写。
    """
    t = WS.sub('', s).replace('\ufeff', '').replace('\ufe0f', '')
    for c in ('\u200e', '\u200f', '\u202b', '\u202c'):
        t = t.replace(c, '')
    t = t.translate(TRANS)
    # RTL 段 NFKC：PDF 文本层存的是 Arabic Presentation Forms（U+FBxx/FExx），
    # NFKC 会还原为逻辑字母与逻辑顺序；基准侧本身就是正常字母，规范化后不变。
    return RTL.sub(lambda m: unicodedata.normalize('NFKC', m.group(0)), t)


def verify_one(i: int):
    mani = json.loads((BASE / 'manifest.json').read_text(encoding='utf-8'))
    m = mani[i]
    stem = Path(m['tex']).stem
    pdf = OUT_PDF / (stem + '.pdf')
    base = (BASE / f'{stem}.base.txt').read_text(encoding='utf-8')
    if not pdf.exists():
        return {'i': i, 'id': m['id'], 'ok': False, 'reason': 'PDF 不存在'}
    # 新鲜度：PDF 必须晚于本轮 build 生成的 manifest，防止旧 PDF 冒充通过
    built_at = (BASE / 'manifest.json').stat().st_mtime
    if pdf.stat().st_mtime < built_at:
        return {'i': i, 'id': m['id'], 'ok': False, 'reason': 'PDF 早于本轮 build（陈旧产物）'}
    r = subprocess.run([PDFTOTEXT, '-raw', '-nopgbrk', str(pdf), '-'],
                       capture_output=True, timeout=300)
    got = r.stdout.decode('utf-8', 'replace')
    a, b = norm(base), norm(got)
    if a == b:
        return {'i': i, 'id': m['id'], 'ok': True, 'base_chars': len(a), 'pdf_chars': len(b)}
    k = next((j for j in range(min(len(a), len(b))) if a[j] != b[j]), min(len(a), len(b)))
    return {'i': i, 'id': m['id'], 'ok': False, 'base_chars': len(a), 'pdf_chars': len(b),
            'first_diff': k, 'base_ctx': a[max(0, k - 40):k + 60], 'pdf_ctx': b[max(0, k - 40):k + 60]}


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'build'
    if cmd == 'build':
        build()
    elif cmd == 'chapter':
        for x in sys.argv[2:]:
            print(json.dumps(compile_one(int(x)), ensure_ascii=False), flush=True)
    elif cmd == 'verify':
        for x in sys.argv[2:]:
            print(json.dumps(verify_one(int(x)), ensure_ascii=False), flush=True)
    elif cmd == 'all':
        n = len(json.loads((BASE / 'manifest.json').read_text(encoding='utf-8')))
        for i in range(n):
            print(json.dumps(compile_one(i), ensure_ascii=False), flush=True)
    elif cmd == 'merge':
        mani = json.loads((BASE / 'manifest.json').read_text(encoding='utf-8'))
        files = [str(OUT_PDF / (Path(m['tex']).stem + '.pdf')) for m in mani]
        files = [f for f in files if Path(f).exists()]
        out = OUT_PDF / '你缺失的那门手机课_v1.9_逐字保真版.pdf'
        subprocess.run([PDFUNITE] + files + [str(out)], check=True, timeout=1800)
        print(out)
    else:
        print(__doc__)


if __name__ == '__main__':
    main()
