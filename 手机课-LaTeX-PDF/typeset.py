#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""把 v1.5–v1.8 每个语言的 HTML 逐个排成 PDF（只读仓库，不在仓库内写任何文件）。

版式对标 Pro 级开源书（missing-2.0.pdf）：TikZ 封面、版权页、篇扉页、
章节 opener（眉标 + 大标题 + 青色分隔线 + 本章导读框）、四色提示框、
代码块深色标题栏、浅蓝表头表格、页眉页脚、带色底纹的篇目录。

用法：
    python typeset.py one     <html路径>            # 调试单个文件
    python typeset.py version <版本>               # 编译该版本全部语言
    python typeset.py book    <html路径> <输出pdf>  # 排成精品单行本
输出：
    pdf/<version>/<lang>.pdf
    work/<version>-<lang>/…（中间文件）
"""

import hashlib
import os
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(r'C:\Users\18948\Documents\GitHub\Your-Missing-Phone-Class')
sys.path.insert(0, str(REPO))
os.environ.setdefault('PYTHONDONTWRITEBYTECODE', '1')

from bookkit import htmlparse as H          # noqa: E402
from bookkit import latex as L              # noqa: E402

OUT = Path(__file__).resolve().parent
PDF_DIR = OUT / 'pdf'
WORK_DIR = OUT / 'work'
FONT_DIR = OUT / 'fonts'
MIKTEX = r'C:\Program Files\MiKTeX\miktex\bin\x64'

WIN = 'C:/Windows/Fonts/'
FDIR = str(FONT_DIR).replace('\\', '/') + '/'

CJK_LANGS = {'zh-CN', 'zh-TW', 'yue', 'lzh', 'ja', 'ko'}
# 用 Noto Sans SC 静态实例的语言：字形覆盖最全（假名、繁体、符号都有），
# 西文配 Segoe UI、代码配 Consolas，与中文的黑体风格统一。
NOTO_LANGS = {'zh-CN', 'zh-TW', 'yue', 'lzh', 'ja'}
# 需要 TrueType 脚本特性的语言：主字体必须自带该文字的字形
SCRIPT_FONTS = {
    'th': ('LEELAWAD.TTF', 'Script=Thai'),
    'ar': ('arial.ttf', 'Script=Arabic'),
    'he': ('arial.ttf', 'Script=Hebrew'),
}
# 需要连字符断词的语言（长复合词多，缺断词点会整行溢出页边）
# 语言名对应 polyglossia 的 gloss-*.ldf，内部载入 hyph-utf8 的断词模式
HYPHEN_LANGS = {
    'de': 'german',
    'ru': 'russian',
    'el': 'greek',
}


# ------------------------------------------------------------------ 符号映射
# bookkit 的 clean() 用 RE_EMOJI 剥符号、用 SYMBOL_MAP 换字；不同字体栈能显示的
# 字符不同，所以按语言组重设这两张表（在 build_file 开头生效）。

MATH_MAP = {
    '\u2260': '$\\neq$', '\u2265': '$\\geq$', '\u2264': '$\\leq$',
    '\u00b1': '$\\pm$', '\u03bc': '$\\mu$', '\u2248': '$\\approx$',
    '\u221e': '$\\infty$',
}
# Noto Sans SC 只缺 ➜ ↩ ⚙ ✅ ❤ ❄ ∙；→ ← ↑ ⇄ ⇧ ⚠ ★ ✓ ☎ ☀ 〇 ● ◆ 等全部自带
SYMBOL_NOTO = dict(MATH_MAP)
SYMBOL_NOTO.update({
    '\u279c': '\u2192',      # ➜ → →
    '\u21a9': '\u2190',      # ↩ → ←
    '\u2699': '\u203b',      # ⚙ → ※
    '\u2705': '\u2713',      # ✅ → ✓
    '\u2764': '\u2665',      # ❤ → ♥
    '\u2744': '',            # ❄ 无字形，与其它 emoji 一样丢弃
    '\u25be': '\u25bc',      # ▾ → ▼
    '\u2219': '\u00b7',      # ∙ → ·
    '\u30fb': '\u00b7',      # ・ → ·
    '\u301c': '\uff5e',      # 〜 → ～
    '\ufe0f': '',
})
# 圈号：Noto 只收了 ①，其余 ②–⑳ 缺字形 → 统一改成 (n)，与其它字体栈保持一致
for _i in range(1, 21):
    SYMBOL_NOTO[chr(0x245F + _i)] = f'({_i})'
SYMBOL_NOTO['\u24ea'] = '(0)'
# 其它字体栈：沿用 bookkit 旧替换表（★→*、✓→√、⌘→Cmd…），再补箭头
SYMBOL_OTHER = dict(L.SYMBOL_MAP)
SYMBOL_OTHER.update({
    '\u279c': '\u2192',      # ➜ → →
    '\u21a9': '\u2190',      # ↩ → ←
    '\u2699': '\u203b',      # ⚙ → ※
    '\u21c4': '\u2192',      # ⇄ → →（SimSun/SimHei 无 ↔，用单向箭头最稳）
    '\u2194': '\u2192',      # ↔ → →（同上）
    '\u2011': '\u2010',      # ‑ 不换行连字符 → ‐
    '\u30fb': '\u00b7',
    '\u301c': '\uff5e',
})

# 希腊语/西里尔语正文里 μ 是普通字母，不能替换成数学模式 `$\mu$`：
# 数学模式会打断连字符断词（αποκρυσμένο 变成 απο$\mu$ακρυσ$\mu$ένο 后无法断行），
# 导致整行溢出页边。这两种语言用 Segoe UI/Times，本身就有 μ 字形。
SYMBOL_GREEK = dict(SYMBOL_OTHER)
SYMBOL_GREEK['\u03bc'] = '\u03bc'

# 表情符号两组都无字形，一律剥离。Noto 组保留 2190–21FF 与 2600–27BF 里可显示的
# 符号（→ ★ ✓ ⚠ ▶ …）；其它组仍整段剥离（改用 SYMBOL_MAP 换字，与旧版一致）。
RE_EMOJI_NOTO = re.compile(
    '[\U0001F000-\U0001FAFF\U00002B00-\U00002BFF\U0000FE00-\U0000FE0F]')
RE_EMOJI_OTHER = re.compile(
    '[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0000FE00-\U0000FE0F'
    '\U00002B00-\U00002BFF]')

# 把西文字体缺字形的符号划入 CJK 类，交由中文字体渲染（两个字体栈分别覆盖）
CHARCLASS_NOTO = ('"26A0,"2756,"25B6,"2605,"2713,"203B,"2103,"2318,"21E7,'
                  '"2502,"251C,"2514,"21C4,"2192,"2190,"2191,"2194,'
                  '"25CF,"25C6,"25CB,"3007,"25B2,"25A0,"25BC,"2665,"2600,"260E')
CHARCLASS_OTHER = '"2192,"2190,"2191,"2194,"203B,"2103,"25C6,"25B2,"25CF,"25BC'


def lang_symbols(lang: str) -> None:
    """按语言切换 bookkit 的符号处理行为。"""
    if lang in NOTO_LANGS:
        L.SYMBOL_MAP = SYMBOL_NOTO
        L.RE_EMOJI = RE_EMOJI_NOTO
    elif lang in ('el', 'ru'):
        # 希腊/西里尔：μ 保持字母形态（数学模式会断掉连字符断词）
        L.SYMBOL_MAP = SYMBOL_GREEK
        L.RE_EMOJI = RE_EMOJI_OTHER
    else:
        L.SYMBOL_MAP = SYMBOL_OTHER
        L.RE_EMOJI = RE_EMOJI_OTHER


# bidi(polyglossia) 下 listings 的逐字读取会失败（Incomplete \iffalse），
# 阿拉伯语/希伯来语必须把代码块包进 bidi 的 LTR 环境
RTL_LANGS = {'ar', 'he'}
RTL_MODE = False


def _wrap_rtl(tex: str) -> str:
    return ('\\begin{LTR}\n' + tex + '\n\\end{LTR}') if RTL_MODE else tex


# ------------------------------------------------------------------ 图形字体
FIG_FONT = {
    'zh-CN': ('NotoSansSC-Regular.ttf', 'NotoSansSC-Bold.ttf'),
    'zh-TW': ('NotoSansSC-Regular.ttf', 'NotoSansSC-Bold.ttf'),
    'yue':   ('NotoSansSC-Regular.ttf', 'NotoSansSC-Bold.ttf'),
    'lzh':   ('NotoSansSC-Regular.ttf', 'NotoSansSC-Bold.ttf'),
    'ja':    ('NotoSansSC-Regular.ttf', 'NotoSansSC-Bold.ttf'),
    'ko':    (r'C:\Windows\Fonts\malgun.ttf', r'C:\Windows\Fonts\malgunbd.ttf'),
    'th':    (r'C:\Windows\Fonts\LEELAWAD.TTF', r'C:\Windows\Fonts\LEELAWAD.TTF'),
    'ar':    (r'C:\Windows\Fonts\arial.ttf', r'C:\Windows\Fonts\arialbd.ttf'),
    'he':    (r'C:\Windows\Fonts\arial.ttf', r'C:\Windows\Fonts\arialbd.ttf'),
}
FIG_DEFAULT = (r'C:\Windows\Fonts\segoeui.ttf', r'C:\Windows\Fonts\segoeuib.ttf')


def register_fig_font(lang: str) -> str:
    """用 svglib 的 register_font 注册 TTF（普通+粗体），返回该语言专属字体名。"""
    name = 'TypesetFig-' + re.sub(r'[^A-Za-z0-9]', '', lang)
    normal, bold = FIG_FONT.get(lang, FIG_DEFAULT)
    if name not in _FIG_REGISTERED:
        normal = str(FONT_DIR / normal) if not os.path.isabs(normal) else normal
        bold = str(FONT_DIR / bold) if not os.path.isabs(bold) else bold
        from svglib.svglib import register_font
        register_font(name, normal, 'normal', 'normal')
        register_font(name, bold, 'bold', 'normal')
        _FIG_REGISTERED.add(name)
    return name


_FIG_REGISTERED = set()


def make_svg_converter(lang: str):
    """SVG 文本 → PDF；文本统一走注册好的 TTF（避免 Helvetica 方框）。"""
    font = register_fig_font(lang)

    def convert(svg_text: str, pdf_path: Path) -> bool:
        try:
            from io import BytesIO
            from svglib.svglib import svg2rlg
            from reportlab.graphics import renderPDF
            # svglib 解析不了 style 里的 auto；再把字体统一成注册过的 TTF
            svg_text = re.sub(r'(<svg[^>]*?)\sstyle="[^"]*"', r'\1', svg_text, count=1)
            svg_text = re.sub(r'font-family="[^"]*"', 'font-family="' + font + '"', svg_text)
            svg_text = re.sub(r"font-family='[^']*'", "font-family='" + font + "'", svg_text)
            svg_text = re.sub(r'font-family:([^;"\']+)', 'font-family:' + font, svg_text)
            svg_text = re.sub(r'<text\b', '<text font-family="' + font + '"', svg_text)
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


# ---- 修复：bookkit.latex.clean() 会 strip 文本节点首尾空格，导致 </strong>/<code> 两侧粘连 ----
_ORIG_CLEAN = L.clean

# 正文里的长 ASCII 串（域名、包名、路径）在句点后可断行，否则整行硬撑出页边
RE_LONGRUN = re.compile(r'[A-Za-z0-9][A-Za-z0-9.\\_\-]{10,}')

# 希腊/西里尔文正文里，界面路径被拍平成 `标签.标签(标签)` 的形态，
# 标签之间没有空格，LaTeX 无处断行 → 整段溢出页边。
# 在「句点/右括号/斜杠/逗号 + 希腊或西里尔字母」处插 \allowbreak{}。
RE_GK_BREAK = re.compile(
    r'(?<=[\.,\)/])(?=[Ͱ-ϿЀ-ӿ])')


def _break_long_runs(tex: str) -> str:
    """长 ASCII 串（域名/标识符）加断点：句点之后、以及驼峰处。"""
    def repl(m):
        s = m.group(0)
        if '.' in s:
            s = s.replace('.', r'.\allowbreak{}')
        if len(s) >= 14 and s.isascii():
            s = RE_CAMEL.sub(lambda _m: r'\allowbreak{}', s)
        return s
    return RE_LONGRUN.sub(repl, tex)


def _clean_keep_boundary(text):
    out = _ORIG_CLEAN(text)
    if out:
        out = _break_long_runs(out)
        out = RE_GK_BREAK.sub(lambda m: r'\allowbreak{}', out)
        if text[:1].isspace():
            out = ' ' + out
        if text[-1:].isspace():
            out = out + ' '
    return out


L.clean = _clean_keep_boundary

# ---- 行内 <code>：URL、包名、命令等长串在标点后允许断行，避免溢出到页边 ----
_ORIG_INLINE = L.inline
RE_CODE_BREAK = re.compile(r'([/\\.?=&_%#:,+-])')
RE_CAMEL = re.compile(r'(?<=[a-z0-9])(?=[A-Z])')
# Consolas 缺不换行连字符等字形：行内 code 里统一换成 ASCII
CODE_CHARMAP = {'\u2010': '-', '\u2011': '-', '\u00a0': ' ', '\u2009': ' '}


def _code_tex(text: str) -> str:
    text = ''.join(CODE_CHARMAP.get(c, c) for c in text)
    out = []
    for part in RE_CODE_BREAK.split(text):
        if not part:
            continue
        if len(part) == 1 and RE_CODE_BREAK.fullmatch(part):
            out.append(L.esc(part) + r'\allowbreak{}')
            continue
        esc = L.esc(part)
        # 超长驼峰标识符（@EnvironmentObject）在小写→大写处允许断行
        if len(part) >= 12 and part.isascii():
            esc = RE_CAMEL.sub(lambda m: r'\allowbreak{}', esc)
        out.append(esc)
    return ''.join(out)


def inline_code(node, out):
    if isinstance(node, H.Node) and node.tag == 'code':
        txt = L.RE_EMOJI.sub('', L.unescape(node.text())).replace('\xa0', ' ')
        out.append(r'\texttt{' + _code_tex(txt) + '}')
        return
    _ORIG_INLINE(node, out)


L.inline = inline_code


def lang_of(html_path: Path, raw: str) -> str:
    m = re.search(r'<html[^>]*\slang="([^"]*)"', raw)
    code = (m.group(1) if m else '').lower()
    if not code:
        code = html_path.stem.lower()
    for known in list(NOTO_LANGS) + ['ko']:
        if code.startswith(known.lower()):
            return known
    for known in SCRIPT_FONTS:
        if code.startswith(known):
            return known
    return code or 'en'


# ------------------------------------------------------------------ 界面文案
UI = {
    'zh': {
        'cover_eyebrow': '开源 PDF 版',
        'cover_band': '开源图书 · 免费获取 · 禁止售卖',
        'cover_foot': 'ClassTechStar · GitHub 开源项目',
        'colophon': '版权与版本信息',
        'title': '书\\hspace{1.2em}名', 'version': '版\\hspace{1.2em}本',
        'chapters': '章\\hspace{1.2em}节', 'author': '作\\hspace{1.2em}者',
        'source': '源\\hspace{1.2em}码', 'license': '授\\hspace{1.2em}权',
        'ch_unit': '节', 'part_unit': '个部分', 'toc': '目录',
        'intro_label': '本章导读', 'date': '2026 年 10 月',
    },
    'ja': {
        'cover_eyebrow': 'オープンソース PDF 版',
        'cover_band': 'オープンソース・無料公開・転売禁止',
        'cover_foot': 'ClassTechStar · GitHub オープンソースプロジェクト',
        'colophon': '版権とバージョン情報',
        'title': '書\\hspace{1.2em}名', 'version': '版\\hspace{1.2em}本',
        'chapters': '章\\hspace{0.4em}節', 'author': '著\\hspace{1.2em}者',
        'source': 'ソース', 'license': 'ライセンス',
        'ch_unit': '節', 'part_unit': '部', 'toc': '目次',
        'intro_label': '本章ガイド', 'date': '2026 年 10 月',
    },
    'ko': {
        'cover_eyebrow': '오픈소스 PDF 판',
        'cover_band': '오픈소스 · 무료 공개 · 판매 금지',
        'cover_foot': 'ClassTechStar · GitHub 오픈소스 프로젝트',
        'colophon': '판권 및 버전 정보',
        'title': '제\\hspace{0.4em}목', 'version': '버\\hspace{0.4em}전',
        'chapters': '구\\hspace{0.4em}성', 'author': '저\\hspace{0.4em}자',
        'source': '소\\hspace{0.4em}스', 'license': '라이선스',
        'ch_unit': '절', 'part_unit': '부', 'toc': '목차',
        'intro_label': '이 장의 안내', 'date': '2026년 10월',
    },
    'ar': {
        'cover_eyebrow': 'نسخة PDF مفتوحة المصدر',
        'cover_band': 'مفتوح المصدر · مجاني · يُمنع البيع',
        'cover_foot': 'ClassTechStar · مشروع مفتوح المصدر على GitHub',
        'colophon': 'حقوق النشر ومعلومات الإصدار',
        'title': 'الكتاب', 'version': 'الإصدار', 'chapters': 'المحتوى',
        'author': 'المؤلف', 'source': 'المصدر', 'license': 'الترخيص',
        'ch_unit': 'قسمًا', 'part_unit': 'أجزاء', 'toc': 'المحتويات',
        'intro_label': 'دليل هذا الفصل', 'date': 'أكتوبر 2026',
    },
    'he': {
        'cover_eyebrow': 'מהדורת PDF בקוד פתוח',
        'cover_band': 'קוד פתוח · חינם · אסור למכירה',
        'cover_foot': 'ClassTechStar · פרויקט קוד פתוח ב-GitHub',
        'colophon': 'זכויות יוצרים ומידע על המהדורה',
        'title': 'שם הספר', 'version': 'מהדורה', 'chapters': 'תוכן',
        'author': 'מחבר', 'source': 'קוד מקור', 'license': 'רישיון',
        'ch_unit': 'פרקים', 'part_unit': 'חלקים', 'toc': 'תוכן העניינים',
        'intro_label': 'מדריך לפרק', 'date': 'אוקטובר 2026',
    },
    'th': {
        'cover_eyebrow': 'ฉบับ PDF โอเพนซอร์ส',
        'cover_band': 'โอเพนซอร์ส · ดาวน์โหลดฟรี · ห้ามจำหน่าย',
        'cover_foot': 'ClassTechStar · โครงการโอเพนซอร์สบน GitHub',
        'colophon': 'ลิขสิทธิ์และข้อมูลเวอร์ชัน',
        'title': 'ชื่อหนังสือ', 'version': 'เวอร์ชัน', 'chapters': 'เนื้อหา',
        'author': 'ผู้เขียน', 'source': 'ซอร์สโค้ด', 'license': 'สัญญาอนุญาต',
        'ch_unit': 'บท', 'part_unit': 'ภาค', 'toc': 'สารบัญ',
        'intro_label': 'แนะนำบทนี้', 'date': 'ตุลาคม 2026',
    },
    'en': {
        'cover_eyebrow': 'Open PDF Edition',
        'cover_band': 'Open source · Free of charge · Not for sale',
        'cover_foot': 'ClassTechStar · Open source on GitHub',
        'colophon': 'Copyright and Version',
        'title': 'Title', 'version': 'Version', 'chapters': 'Sections',
        'author': 'Author', 'source': 'Source', 'license': 'License',
        'ch_unit': ' sections', 'part_unit': ' parts', 'toc': 'Contents',
        'intro_label': 'Chapter Guide', 'date': 'October 2026',
    },
    'de': {
        'cover_eyebrow': 'Open-PDF-Ausgabe',
        'cover_band': 'Open Source · Kostenlos · Kein Verkauf',
        'cover_foot': 'ClassTechStar · Open Source auf GitHub',
        'colophon': 'Urheberrecht und Versionsangaben',
        'title': 'Titel', 'version': 'Version', 'chapters': 'Abschnitte',
        'author': 'Autor', 'source': 'Quellcode', 'license': 'Lizenz',
        'ch_unit': ' Kapitel', 'part_unit': ' Teile', 'toc': 'Inhaltsverzeichnis',
        'intro_label': 'Kapitelführung', 'date': 'Oktober 2026',
    },
    'es': {
        'cover_eyebrow': 'Edición PDF abierta',
        'cover_band': 'Código abierto · Gratis · No se vende',
        'cover_foot': 'ClassTechStar · Código abierto en GitHub',
        'colophon': 'Copyright y versión',
        'title': 'Título', 'version': 'Versión', 'chapters': 'Secciones',
        'author': 'Autor', 'source': 'Código fuente', 'license': 'Licencia',
        'ch_unit': ' capítulos', 'part_unit': ' partes', 'toc': 'Índice',
        'intro_label': 'Guía del capítulo', 'date': 'Octubre de 2026',
    },
    'fr': {
        'cover_eyebrow': 'Édition PDF ouverte',
        'cover_band': 'Open source · Gratuit · Interdit à la vente',
        'cover_foot': 'ClassTechStar · Open source sur GitHub',
        'colophon': 'Droits d’auteur et version',
        'title': 'Titre', 'version': 'Version', 'chapters': 'Sections',
        'author': 'Auteur', 'source': 'Code source', 'license': 'Licence',
        'ch_unit': ' chapitres', 'part_unit': ' parties', 'toc': 'Sommaire',
        'intro_label': 'Guide du chapitre', 'date': 'Octobre 2026',
    },
    'it': {
        'cover_eyebrow': 'Edizione PDF aperta',
        'cover_band': 'Open source · Gratuito · Non in vendita',
        'cover_foot': 'ClassTechStar · Open source su GitHub',
        'colophon': 'Copyright e versione',
        'title': 'Titolo', 'version': 'Versione', 'chapters': 'Sezioni',
        'author': 'Autore', 'source': 'Codice sorgente', 'license': 'Licenza',
        'ch_unit': ' capitoli', 'part_unit': ' parti', 'toc': 'Indice',
        'intro_label': 'Guida del capitolo', 'date': 'Ottobre 2026',
    },
    'pt': {
        'cover_eyebrow': 'Edição PDF aberta',
        'cover_band': 'Código aberto · Gratuito · Não à venda',
        'cover_foot': 'ClassTechStar · Código aberto no GitHub',
        'colophon': 'Copyright e versão',
        'title': 'Título', 'version': 'Versão', 'chapters': 'Seções',
        'author': 'Autor', 'source': 'Código-fonte', 'license': 'Licença',
        'ch_unit': ' capítulos', 'part_unit': ' partes', 'toc': 'Sumário',
        'intro_label': 'Guia do capítulo', 'date': 'Outubro de 2026',
    },
    'id': {
        'cover_eyebrow': 'Edisi PDF terbuka',
        'cover_band': 'Sumber terbuka · Gratis · Tidak dijual',
        'cover_foot': 'ClassTechStar · Sumber terbuka di GitHub',
        'colophon': 'Hak cipta dan versi',
        'title': 'Judul', 'version': 'Versi', 'chapters': 'Bagian',
        'author': 'Penulis', 'source': 'Kode sumber', 'license': 'Lisensi',
        'ch_unit': ' bab', 'part_unit': ' bagian', 'toc': 'Daftar isi',
        'intro_label': 'Panduan bab', 'date': 'Oktober 2026',
    },
    'ms': {
        'cover_eyebrow': 'Edisi PDF terbuka',
        'cover_band': 'Sumber terbuka · Percuma · Bukan untuk dijual',
        'cover_foot': 'ClassTechStar · Sumber terbuka di GitHub',
        'colophon': 'Hak cipta dan versi',
        'title': 'Tajuk', 'version': 'Versi', 'chapters': 'Bahagian',
        'author': 'Penulis', 'source': 'Kod sumber', 'license': 'Lesen',
        'ch_unit': ' bab', 'part_unit': ' bahagian', 'toc': 'Isi kandungan',
        'intro_label': 'Panduan bab', 'date': 'Oktober 2026',
    },
    'ru': {
        'cover_eyebrow': 'Открытое PDF-издание',
        'cover_band': 'Открытый код · Бесплатно · К продаже не предлагается',
        'cover_foot': 'ClassTechStar · Открытый проект на GitHub',
        'colophon': 'Авторские права и версия',
        'title': 'Название', 'version': 'Версия', 'chapters': 'Разделы',
        'author': 'Автор', 'source': 'Исходный код', 'license': 'Лицензия',
        'ch_unit': ' глав', 'part_unit': ' частей', 'toc': 'Содержание',
        'intro_label': 'Путеводитель по главе', 'date': 'Октябрь 2026',
    },
    'el': {
        'cover_eyebrow': 'Έκδοση PDF ανοιχτού κώδικα',
        'cover_band': 'Ανοιχτός κώδικας · Δωρεάν · Όχι προς πώληση',
        'cover_foot': 'ClassTechStar · Ανοιχτός κώδικας στο GitHub',
        'colophon': 'Πνευματικά δικαιώματα και έκδοση',
        'title': 'Τίτλος', 'version': 'Έκδοση', 'chapters': 'Ενότητες',
        'author': 'Συγγραφέας', 'source': 'Πηγαίος κώδικας', 'license': 'Άδεια',
        'ch_unit': ' κεφάλαια', 'part_unit': ' μέρη', 'toc': 'Πίνακας περιεχομένων',
        'intro_label': 'Οδηγός κεφαλαίου', 'date': 'Οκτώβριος 2026',
    },
}


def ui_of(lang: str) -> dict:
    if lang in ('zh-CN', 'zh-TW', 'yue', 'lzh'):
        return UI['zh']
    if lang in ('ja', 'ko', 'ar', 'he', 'th'):
        return UI[lang]
    # 拉丁/希腊/西里尔字母的欧洲语种：封面与版权页走本地化文案
    if lang in UI:
        return UI[lang]
    return UI['en']


# ------------------------------------------------------------------ 字体块

def font_block(lang: str) -> list:
    """字体设置：Noto 组按文件路径加载静态实例，其余沿用系统字体名。"""
    out = [r'\newcommand{\fontdir}{' + FDIR + '}',
           r'\newcommand{\windir}{' + WIN + '}']
    seg = (r'[Path=\windir,BoldFont=segoeuib.ttf,BoldFeatures={Path=\windir},'
           r'ItalicFont=segoeuii.ttf,ItalicFeatures={Path=\windir},'
           r'BoldItalicFont=segoeuiz.ttf,BoldItalicFeatures={Path=\windir}]')
    cons = (r'[Path=\windir,BoldFont=consolab.ttf,BoldFeatures={Path=\windir},'
            r'ItalicFont=consolai.ttf,ItalicFeatures={Path=\windir},'
            r'BoldItalicFont=consolaz.ttf,BoldItalicFeatures={Path=\windir}]')

    if lang in NOTO_LANGS:
        out += [
            r'\setCJKmainfont{NotoSansSC-Regular.ttf}[Path=\fontdir,'
            r'BoldFont=NotoSansSC-Bold.ttf,BoldFeatures={Path=\fontdir},'
            r'ItalicFont=simkai.ttf,ItalicFeatures={Path=\windir},'
            r'BoldItalicFont=simkai.ttf,BoldItalicFeatures={Path=\windir}]',
            r'\setCJKsansfont{NotoSansSC-Medium.ttf}[Path=\fontdir,'
            r'BoldFont=NotoSansSC-Bold.ttf,BoldFeatures={Path=\fontdir}]',
            r'\setCJKmonofont{NotoSansSC-Regular.ttf}[Path=\fontdir]',
            r'\setmainfont{segoeui.ttf}' + seg,
            r'\setsansfont{segoeui.ttf}' + seg,
            r'\setmonofont{consola.ttf}' + cons,
            r'\xeCJKDeclareCharClass{CJK}{' + CHARCLASS_NOTO + '}',
        ]
        return out

    if lang == 'ko':
        cjk = r'[Path=\windir,BoldFont=malgunbd.ttf,BoldFeatures={Path=\windir}]'
        out += [r'\setCJKmainfont{malgun.ttf}' + cjk,
                r'\setCJKsansfont{malgun.ttf}' + cjk,
                r'\setCJKmonofont{malgun.ttf}' + cjk]
    else:
        out += [r'\setCJKmainfont[BoldFont=SimHei,ItalicFont=KaiTi]{SimSun}',
                r'\setCJKsansfont{SimHei}',
                r'\setCJKmonofont{SimSun}']

    if lang in SCRIPT_FONTS:
        # Arial / Leelawadee 的斜体缺阿拉伯、泰文字形 → 斜体映射到正体
        fname, feat = SCRIPT_FONTS[lang]
        bold = 'arialbd.ttf' if lang in ('ar', 'he') else fname
        opt = (r'[Path=\windir,BoldFont=' + bold + r',BoldFeatures={Path=\windir},'
               r'ItalicFont=' + fname + r',ItalicFeatures={Path=\windir},'
               r'BoldItalicFont=' + bold + r',BoldItalicFeatures={Path=\windir},'
               + feat + ']')
        out += [r'\setmainfont{' + fname + '}' + opt,
                r'\setsansfont{' + fname + '}' + opt,
                r'\setmonofont{' + fname + '}' + opt]
    else:
        out += [r'\setmainfont{segoeui.ttf}' + seg,
                r'\setsansfont{segoeui.ttf}' + seg,
                r'\setmonofont{consola.ttf}' + cons]
    out.append(r'\xeCJKDeclareCharClass{CJK}{' + CHARCLASS_OTHER + '}')
    return out


# ------------------------------------------------------------------ 导言区

def preamble(lang: str, meta: dict) -> list:
    u = ui_of(lang)
    icon = ({'info': '\u2756', 'warn': '\u26a0', 'prac': '\u25b6', 'sum': '\u2605'}
            if lang in NOTO_LANGS else
            {'info': '\u25c6', 'warn': '\u25b2', 'prac': '\u25cf', 'sum': '\u203b'})
    P = []
    add = P.append

    add(r'\documentclass[11pt,a4paper,openany]{book}')
    add(r'\usepackage[UTF8,fontset=none]{ctex}')
    add(r'\usepackage{geometry}')
    add(r'\geometry{a4paper,left=2.55cm,right=2.55cm,top=2.55cm,bottom=2.45cm}')
    add(r'\usepackage[table]{xcolor}')
    add(r'\usepackage{graphicx}\usepackage{booktabs}\usepackage{tabularx}')
    add(r'\usepackage{xltabular}')
    add(r'\usepackage{enumitem}\usepackage{listings}')
    add(r'\usepackage{tcolorbox}')
    add(r'\tcbuselibrary{skins,breakable,listings}')
    add(r'\usepackage{fancyhdr}\usepackage{titlesec}\usepackage{titletoc}')
    add(r'\usepackage{needspace}\usepackage{fontspec}')
    add(r'\usepackage{tikz}')
    add(r'\usetikzlibrary{shapes.geometric,shadows}')
    if lang in ('ar', 'he'):
        add(r'\usepackage{polyglossia}')
        add(r'\setmainlanguage{' + ('arabic' if lang == 'ar' else 'hebrew') + '}')
        add(r'\setotherlanguage{english}')
    # 德/俄/希三种语言有大量长复合词（Wiederherstellungsschlüssel、
    # производительности…），不开连字符断词就会整行溢出页边。
    # polyglossia 载入 hyph-de-1996 / hyph-ru / hyph-el-monoton 模式。
    elif lang in HYPHEN_LANGS:
        add(r'\usepackage{polyglossia}')
        add(r'\setmainlanguage{' + HYPHEN_LANGS[lang] + '}')
        add(r'\setotherlanguage{english}')

    # ---- 配色（取自参考书采样值）----
    add(r'\definecolor{teal}{HTML}{11C6B5}')
    add(r'\definecolor{deepblue}{HTML}{1876C9}')
    add(r'\definecolor{mint}{HTML}{6BECCD}')
    add(r'\definecolor{slate}{HTML}{4A5568}')
    add(r'\definecolor{infobg}{HTML}{EAF6FE}')
    add(r'\definecolor{warnbg}{HTML}{FFF3E2}')
    add(r'\definecolor{pracbg}{HTML}{E7FAF5}')
    add(r'\definecolor{sumbg}{HTML}{F4F6F9}')
    add(r'\definecolor{codebg}{HTML}{F4F5F7}')
    add(r'\definecolor{codehead}{HTML}{2D3748}')
    add(r'\definecolor{tabheadbg}{HTML}{DCEDFB}')
    add(r'\definecolor{lightrule}{HTML}{D8DEE6}')

    P.extend(font_block(lang))
    add(r'\usepackage[colorlinks=true,linkcolor=black,urlcolor=deepblue]{hyperref}')

    # 泰文没有词间空格：开启 XeTeX 的泰文断行，否则整段无法折行、溢出页边
    if lang == 'th':
        add(r'\XeTeXlinebreaklocale "th"')
        add(r'\XeTeXlinebreakskip=0pt plus 0.5pt')

    # ---- 版式 ----
    add(r'\setlength{\parindent}{2em}' if lang in CJK_LANGS else r'\setlength{\parindent}{1.2em}')
    add(r'\setlength{\parskip}{2.5pt}')
    add(r'\linespread{1.18}')
    add(r'\emergencystretch=3em')
    add(r'\tolerance=2000')
    # 书籍常规排版约束：不留孤行（页首/页尾至少两行），提示框跨页时也不会甩出一行
    add(r'\clubpenalty=10000 \widowpenalty=10000 \displaywidowpenalty=10000')
    add(r'\pagestyle{fancy}\fancyhf{}')
    add(r'\renewcommand{\headrulewidth}{0pt}')
    add(r'\fancyhead[L]{\small\color{slate}\nouppercase{\rightmark}}')
    add(r'\fancyhead[R]{\small\color{slate}\nouppercase{\leftmark}}')
    add(r'\fancyfoot[R]{\small\color{slate}\thepage}')
    add(r'\setlength{\headheight}{14.5pt}')
    add(r'\fancypagestyle{chapteropen}{\fancyhf{}\fancyfoot[R]{\small\color{slate}\thepage}'
        r'\renewcommand{\headrulewidth}{0pt}}')

    # ---- 标题层级（书内标题自带中文序号 → 全部无编号）----
    add(r'\titleformat{name=\section,numberless}{\needspace{4\baselineskip}\bfseries\large}{}{0pt}{}')
    add(r'\titlespacing*{name=\section,numberless}{0pt}{14pt plus 2pt minus 2pt}{6pt}')
    add(r'\titleformat{name=\subsection,numberless}{\needspace{3\baselineskip}\bfseries\normalsize}{}{0pt}{}')
    add(r'\titlespacing*{name=\subsection,numberless}{0pt}{11pt plus 2pt minus 2pt}{4pt}')

    # ---- 章节 opener ----
    add(r'\newcommand{\bookchapter}[3]{%')
    add(r'  \clearpage\phantomsection')
    add(r'  \addcontentsline{toc}{chapter}{#3}%')
    add(r'  \markboth{#3}{}%')
    add(r'  \thispagestyle{chapteropen}%')
    add(r'  \vspace*{4pt}%')
    add(r'  \ifx\relax#1\relax\else')
    add(r'    {\color{teal}\sffamily\bfseries\small #1\par}%')
    add(r'    \vspace{4pt}%')
    add(r'  \fi')
    add(r'  {\raggedright\Huge\bfseries #2\par}%')
    add(r'  \vspace{9pt}%')
    add(r'  {\color{teal}\noindent\rule{\linewidth}{2.2pt}\par}%')
    add(r'  \vspace{13pt}%')
    add(r'}')
    add(r'\newcommand{\booksection}[1]{\section*{#1}\addcontentsline{toc}{section}{#1}\markright{#1}}')
    add(r'\newcommand{\booksubsection}[1]{\subsection*{#1}}')
    add(r'\newcommand{\chapterintro}[1]{%')
    add(r'  \begin{tcolorbox}[breakable,enhanced,colback=sumbg,colframe=teal,boxrule=0pt,')
    add(r'    leftrule=2.5pt,arc=1.5pt,left=10pt,right=10pt,top=7pt,bottom=7pt]')
    add(r'  {\color{teal}\sffamily\bfseries\small ' + u['intro_label'] + r'\par}\smallskip')
    add(r'  {\small #1}')
    add(r'  \end{tcolorbox}')
    add(r'  \vspace{5pt}%')
    add(r'}')

    # ---- 篇 opener ----
    add(r'\newcommand{\bookpart}[1]{%')
    add(r'  \clearpage\phantomsection')
    add(r'  \addcontentsline{toc}{part}{#1}%')
    add(r'  \markboth{#1}{}%')
    add(r'  \thispagestyle{chapteropen}%')
    add(r'  \vspace*{0.14\textheight}%')
    add(r'  {\color{teal}\noindent\rule{\linewidth}{2.2pt}\par}%')
    add(r'  \vspace{18pt}%')
    add(r'  {\raggedright\Huge\bfseries #1\par}%')
    add(r'  \vspace{20pt}%')
    add(r'}')
    add(r'\newenvironment{partintro}{%')
    add(r'  \begin{tcolorbox}[breakable,enhanced,colback=infobg,colframe=deepblue,boxrule=0pt,')
    add(r'    leftrule=3pt,arc=1.5pt,left=12pt,right=12pt,top=9pt,bottom=9pt]\small}')
    add(r'  {\end{tcolorbox}\par\vfill}')

    # ---- 四色提示框 ----
    for env, back, frame, col, ic in (
            ('tcbinfo', 'infobg', 'deepblue!35', 'deepblue', icon['info']),
            ('tcbwarn', 'warnbg', 'orange!65', 'orange!85!red', icon['warn']),
            ('tcbpractice', 'pracbg', 'teal!55', 'teal!80!black', icon['prac']),
            ('tcbsummary', 'sumbg', 'slate!40', 'slate', icon['sum'])):
        add(r'\newtcolorbox{' + env + r'}[1]{breakable,enhanced,colback=' + back + ',')
        add(r'  colframe=' + frame + r',boxrule=0pt,leftrule=3pt,arc=1.5pt,')
        add(r'  left=10pt,right=10pt,top=7pt,bottom=7pt,')
        add(r'  fonttitle=\bfseries\sffamily,')
        add(r'  title={\textcolor{' + col + '}{' + ic + r'}\hspace{0.35em}#1},coltitle=' + col + '}')

    # ---- 代码块 ----
    add(r'\lstdefinestyle{bookcode}{basicstyle=\ttfamily\small,breaklines=true,')
    add(r'  breakatwhitespace=false,columns=fullflexible,keepspaces=true,')
    add(r'  showstringspaces=false,tabsize=2,extendedchars=true,')
    add(r'  keywordstyle=\color{deepblue}\bfseries,commentstyle=\color{slate}\itshape,')
    add(r'  stringstyle=\color{teal!75!black}}')
    for name, kw in (
            ('Kotlin', 'fun,val,var,class,object,interface,when,if,else,return,for,while,'
                       'import,package,is,in,null,true,false,this,override,suspend,data,'
                       'private,composable'),
            ('Swift', 'func,let,var,class,struct,enum,protocol,import,if,else,return,for,in,'
                      'while,guard,switch,case,default,try,catch,self,init,nil,true,false,'
                      'some,any'),
            ('JavaScript', 'function,const,let,var,if,else,return,for,while,class,import,'
                           'export,from,async,await,new,try,catch,null,true,false,this'),
            ('TypeScript', 'function,const,let,var,if,else,return,for,while,class,import,'
                           'export,from,async,await,new,try,catch,null,true,false,this,'
                           'interface,type,enum,implements,extends,public,private,readonly,as')):
        add(r'\lstdefinelanguage{' + name + r'}{keywords={' + kw + r'},sensitive=true,')
        add(r'  comment=[l]{//},morecomment=[s]{/*}{*/},morestring=[b]"}')

    # ---- 流程图小方块 ----
    for name, back, frame in (('chipi', 'infobg', 'deepblue!55'), ('chipg', 'pracbg', 'teal!70'),
                              ('chipr', 'warnbg', 'red!55'), ('chipa', 'warnbg', 'orange!65'),
                              ('chips', 'sumbg', 'slate!45')):
        add('\\newtcbox{\\' + name + '}{on line,colback=' + back + ',colframe=' + frame + ',')
        add(r'  boxrule=0.6pt,arc=2.5pt,left=5pt,right=5pt,top=2.5pt,bottom=2.5pt,')
        add(r'  fontupper=\small}')

    # ---- 表格 ----
    add(r'\renewcommand{\arraystretch}{1.25}')
    add(r'\setlength{\tabcolsep}{5pt}')

    # ---- 目录 ----
    add(r'\makeatletter')
    add(r'\renewcommand*\l@part[2]{%')
    add(r'  \par\vspace{14pt}%')
    add(r'  \noindent\colorbox{deepblue}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{%')
    add(r'    \color{white}\sffamily\bfseries\large\strut #1\strut}}\par')
    add(r'  \nobreak\vskip 2pt')
    add(r'  \nobreak\hbox to\linewidth{\hfill #2}\par')
    add(r'  \vspace{3pt}}')
    add(r'\makeatother')
    add(r'\titlecontents{chapter}[0pt]{\addvspace{5pt}\bfseries}{}{}'
        r'{\titlerule*[0.6pt]{.}\thecontentspage}{}')
    add(r'\titlecontents{section}[1.7em]{\addvspace{1pt}\small\color{slate}}{}{}'
        r'{\titlerule*[0.6pt]{.}\thecontentspage}{}')

    add(r'\setlist{nosep,leftmargin=1.7em}')
    add(r'\setlist[itemize,1]{label=\textcolor{teal}{\textbullet}}')
    add(r'\setlist[enumerate,1]{label=\textcolor{deepblue}{\arabic*.}}')
    return P


# ------------------------------------------------------------------ 封面与版权页

def title_pieces(title: str) -> list:
    """书名按句末标点切段，作为封面大字的分段（段内由 LaTeX 自动换行）。"""
    pieces = [p.strip() for p in re.findall(r'[^！!。？?]+[！!。？?]?', title) if p.strip()]
    if not pieces:
        return [title.strip()]
    if len(pieces) > 3:
        pieces = pieces[:2] + [' '.join(pieces[2:])]
    return pieces


def cover_tex(meta: dict, u: dict) -> list:
    # 阿拉伯语/希伯来语：整体镜像——插画移到左侧，标题块靠右对齐
    rtl = meta['lang'] in RTL_LANGS
    cx = '-4.9cm' if rtl else '4.9cm'        # 聚光圈圆心
    px = '-10.5cm' if rtl else '4.9cm'       # 手机左下角
    if rtl:
        npre = r'\node[anchor=east,text=white,font=\sffamily\bfseries\small] at '
        pn = r'([xshift=-2.55cm,yshift=-0.55cm]current page.north east) {'
        ps = r'([xshift=-2.55cm,yshift=0.8cm]current page.south east) {'
    else:
        npre = r'\node[anchor=west,text=white,font=\sffamily\bfseries\small] at '
        pn = r'([xshift=2.55cm,yshift=-0.55cm]current page.north west) {'
        ps = r'([xshift=2.55cm,yshift=0.8cm]current page.south west) {'
    out = [r'\begin{titlepage}', r'\thispagestyle{empty}',
           r'\begin{tikzpicture}[remember picture,overlay]',
           r'  \fill[mint] (current page.north west) rectangle ([yshift=-2.6cm]current page.north east);',
           r'  \fill[teal] (current page.north west) rectangle ([yshift=-1.1cm]current page.north east);',
           '  ' + npre + pn + u['cover_band'] + '};',
           r'  \fill[teal] (current page.south west) rectangle ([yshift=1.6cm]current page.south east);',
           '  ' + npre + ps + u['cover_foot'] + '};',
           r'  \fill[mint!40] ([xshift=' + cx + r',yshift=1.3cm]current page.center) circle (6.4cm);',
           r'  \begin{scope}[shift={([xshift=' + px + r',yshift=1.3cm]current page.center)}]',
           r'    \fill[white,drop shadow,rounded corners=6pt] '
           r'(0,0) -- (5.6,0) -- (5.6,10.6) -- (0,10.6) -- cycle;',
           r'    \fill[teal!12] (0.35,0.35) rectangle (5.25,9.4);',
           r'    \fill[deepblue!80] (1.75,8.55) rectangle (3.85,8.75);',
           r'    \foreach \x in {0.75,1.85,2.95,4.05}{',
           r'      \foreach \y in {5.9,4.55,3.2}{',
           r'        \fill[deepblue!70,rounded corners=3.5pt] (\x,\y) rectangle (\x+0.85,\y+0.85);',
           r'      }',
           r'    }',
           r'    \fill[mint!85] (0.75,6.75) rectangle (1.6,7.6);',
           r'    \fill[teal!80] (2.95,5.2) rectangle (3.8,6.05);',
           r'    \fill[deepblue!40] (4.05,3.8) rectangle (4.9,4.65);',
           r'    \fill[slate!60] (2.15,0.62) rectangle (3.45,0.78);',
           r'  \end{scope}',
           r'\end{tikzpicture}',
           r'\vspace*{0.055\textheight}']
    # 标题块：LTR 靠左 6% 缩进；RTL 用 LTR 段落把 minipage 推到右侧，块内文本右对齐
    if rtl:
        out += [r'\begin{LTR}', r'\noindent\hfill\begin{minipage}{0.54\textwidth}',
                r'  \raggedleft']
    else:
        out += [r'\hspace*{0.055\textwidth}',
                r'\begin{minipage}{0.60\textwidth}',
                r'  \raggedright']
    out += [r'  {\color{teal}\sffamily\bfseries\large ' + u['cover_eyebrow'] + r'\par}',
            r'  \vspace{15pt}']
    pieces = title_pieces(meta['title'])
    for i, ln in enumerate(pieces):
        out.append(r'  {\fontsize{26}{33}\selectfont\bfseries ' + L.clean(ln) + r'\par}')
        out.append(r'  \vspace{6pt}' if i < len(pieces) - 1 else r'  \vspace{18pt}')
    if meta['subtitle']:
        out.append(r'  {\color{slate}\large ' + L.clean(meta['subtitle']) + r'\par}')
        out.append(r'  \vspace{12pt}')
    tail = meta['version'] + ' · ' + u['date']
    out += [r'  {\color{slate}\large ' + L.clean(tail) + r'\par}',
            r'\end{minipage}\par']
    if rtl:
        out.append(r'\end{LTR}')
    out += [r'\vfill', r'\clearpage', r'\end{titlepage}']
    return out


def colophon_tex(meta: dict, u: dict, lang: str) -> list:
    zh = lang in CJK_LANGS
    ver = meta['version'] + ('（' + u['date'] + '）' if zh else ' (' + u['date'] + ')')
    chap = (str(meta['nparts']) + ' ' + u['part_unit'].strip() + ' · ' +
            str(meta['nchap']) + ' ' + u['ch_unit'].strip())
    rows = [
        (u['title'], L.clean(meta['title'])),
        (u['version'], L.clean(ver)),
        (u['chapters'], L.clean(chap)),
        (u['author'], 'ClassTechStar'),
        (u['source'], r'\href{https://github.com/ClassTechStar/Your-Missing-Phone-Class}'
                     r'{github.com/ClassTechStar/Your-Missing-Phone-Class}'),
        (u['license'], L.clean(meta['license'])),
    ]
    out = [r'\thispagestyle{empty}',
           r'\vspace*{0.24\textheight}',
           r'{\LARGE\bfseries ' + u['colophon'] + r'\par}',
           r'\vspace{7pt}',
           r'{\color{teal}\noindent\rule{\linewidth}{2.2pt}\par}',
           r'\vspace{20pt}',
           r'\begin{tcolorbox}[enhanced,colback=sumbg,colframe=lightrule,boxrule=0.4pt,'
           r'arc=2pt,left=14pt,right=14pt,top=12pt,bottom=12pt]',
           r'\small',
           r'\begin{tabularx}{\linewidth}{@{}l X@{}}']
    for label, val in rows:
        out.append(r'\textbf{' + label + r'} & ' + val + r' \tabularnewline[3pt]')
    out += [r'\end{tabularx}', r'\end{tcolorbox}', r'\vfill', r'\clearpage']
    return out


# ------------------------------------------------------------------ 渲染补丁

KEYSYM = {'\u2303': 'Ctrl', '\u2325': 'Option', '\u2318': 'Cmd', '\u21e7': 'Shift',
          '\u21a9': 'Enter', '\u232b': 'Delete', '\u23ce': 'Enter'}
RE_KEYS = re.compile(r'^[\u2303\u2325\u2318\u21e7\u21a9\u232b\u23ceA-Za-z0-9+/=\-.]+$')


def key_notation(node):
    """快捷键格（⌃I、⌥⌘↩）→ Ctrl+I、Option+Cmd+Enter；不是快捷键则返回 None。"""
    raw = _raw_text(node).strip()
    if not raw or len(raw) > 14 or not RE_KEYS.match(raw):
        return None
    if not any(c in raw for c in KEYSYM):
        return None
    return '+'.join(KEYSYM.get(c, c.upper()) for c in raw)


BOX_CLASSES = ('info-box', 'warning-box', 'practice-box', 'chapter-summary', 'figure')


def _in_box(node) -> bool:
    """表格是否嵌在提示框／图形里（这些环境里不能用可断页的 longtable）。"""
    p = node.parent
    while p is not None:
        cl = getattr(p, 'classes', None) or []
        if any(k in cl for k in BOX_CLASSES):
            return True
        p = p.parent
    return False


def _table(node):
    """表格 → 浅蓝底表头 + booktabs 三线；长表用 xltabular 跨页并在续页重复表头。"""
    rows = []
    for tr in node.find_all('tr'):
        cells = []
        for c in tr.element_children():
            if c.tag not in ('th', 'td'):
                continue
            cells.append((key_notation(c) or L.inline_text_of_children(c).strip(), c.tag))
        if cells:
            rows.append(cells)
    if not rows:
        return []
    ncol = max(len(r) for r in rows)
    if ncol == 1:
        spec = r'@{}>{\raggedright\arraybackslash}X@{}'
    else:
        # 首列通常是「比较项」标签，德语/俄语里往往是很长的复合词
        # （Programmierfähigkeit、производительность），给首列更多宽度，
        # 窄列里的单词才不会撑破页边。
        first = 1.30 if ncol <= 3 else 1.05
        rest = (ncol - first) / (ncol - 1)
        spec = (r'@{}>{\hsize=' + f'{first:.4f}' + r'\hsize\linewidth=\hsize'
                r'\raggedright\arraybackslash}X')
        spec += ''.join(r' >{\hsize=' + f'{rest:.4f}' + r'\hsize\linewidth=\hsize'
                        r'\raggedright\arraybackslash}X' for _ in range(ncol - 1))
        spec += r'@{}'

    def row_tex(cells, header=False):
        vals = [L.pair_quotes(t) for t, _ in cells]
        if header:
            vals = [r'\textbf{' + v + '}' if v else '' for v in vals]
        # 单元格以 [ 开头时会被误读为换行命令的可选参数，用 {} 阻断
        vals = [('{}' + v) if v.startswith('[') else v for v in vals]
        while len(vals) < ncol:
            vals.append('')
        return ' & '.join(vals) + r' \tabularnewline'

    first_is_head = any(tag == 'th' for _, tag in rows[0])
    long_mode = len(rows) >= 9 and not _in_box(node)
    if long_mode:
        # 长表：longtable 机制可跨页，续页自动重复表头，避免整页留白
        head_tex = [r'\rowcolor{tabheadbg}', row_tex(rows[0], header=True), r'\midrule']
        out = [r'\begin{xltabular}{\linewidth}{' + spec + '}']
        if first_is_head:
            out += head_tex + [r'\endfirsthead'] + head_tex + [r'\endhead']
            body_rows = rows[1:]
        else:
            out += [row_tex(rows[0]), r'\midrule']
            body_rows = rows[1:]
        for r in body_rows:
            head = any(tag == 'th' for _, tag in r)
            if head:
                out.append(r'\rowcolor{tabheadbg}')
            out.append(row_tex(r, header=head))
        out += [r'\bottomrule', r'\end{xltabular}']
        return '\n'.join(out)

    out = [r'\begin{center}', r'\begin{tabularx}{\linewidth}{' + spec + '}']
    if first_is_head:
        out.append(r'\rowcolor{tabheadbg}')
    out.append(row_tex(rows[0], header=first_is_head))
    out.append(r'\midrule')
    for r in rows[1:]:
        head = any(tag == 'th' for _, tag in r)
        if head:
            out.append(r'\rowcolor{tabheadbg}')
        out.append(row_tex(r, header=head))
    out += [r'\bottomrule', r'\end{tabularx}', r'\end{center}']
    return '\n'.join(out)


CODE_LANGS = (('kts', 'Kotlin'), ('kotlin', 'Kotlin'), ('gradle', 'Kotlin'),
              ('swift', 'Swift'), ('python', 'Python'), ('javascript', 'JavaScript'),
              ('jsx', 'JavaScript'), ('typescript', 'TypeScript'), ('java', 'Java'),
              ('html', 'HTML'), ('xml', 'HTML'), ('bash', 'bash'), ('shell', 'bash'),
              ('sql', 'SQL'))


def _code_block(node, ctx):
    """code-block → tcblisting：深色标题栏 + 语法高亮。"""
    head, pre = None, None
    for c in node.element_children():
        if c.tag == 'div' and 'code-head' in c.classes:
            spans = c.find_all('span')
            if spans:
                head = L.clean(spans[0].text())
        elif c.tag == 'pre':
            pre = c
    if pre is None and node.tag == 'pre':
        pre = node
    if pre is None:
        return []
    code = L.unescape(pre.text()).replace('\xa0', ' ')
    code = RE_EMOJI_OTHER.sub('', code)
    code = re.sub(r'[ \t]+$', '', code, flags=re.M).rstrip('\n')
    if not code.strip():
        return []
    lang = ''
    if head:
        low = re.sub(r'\\[a-zA-Z]+|[{}$]', '', head).lower()
        for key, name in CODE_LANGS:
            if key in low:
                lang = name
                break
    common = (r'colback=codebg,colframe=lightrule,boxrule=0.4pt,arc=1.5pt,'
              r'left=8pt,right=8pt,top=5pt,bottom=5pt,listing only,breakable,enhanced,'
              r'listing options={style=bookcode,' +
              ('language=' + lang + ',' if lang else '') + r'}')
    if head:
        opts = (r'{title={' + head + r'},colbacktitle=codehead,coltitle=white,'
                r'fonttitle=\ttfamily\bfseries\small,' + common + r'}')
    else:
        opts = r'{' + common + r'}'
    return _wrap_rtl('\n'.join([r'\begin{tcblisting}' + opts, code, r'\end{tcblisting}']))


def _raw_text(node) -> str:
    out = []
    for c in node.children:
        if isinstance(c, H.Node):
            out.append(_raw_text(c) if c.children else L.unescape(c.text()))
        else:
            out.append(L.unescape(c))
    return ''.join(out)


def _mono_paragraph(node):
    """<p class="font-mono">：按 <br> 拆行的等宽块（按原文，不做 LaTeX 转义）。"""
    lines, buf = [], []
    for c in node.children:
        if isinstance(c, H.Node) and c.tag == 'br':
            lines.append(''.join(buf).strip())
            buf = []
            continue
        buf.append(_raw_text(c) if isinstance(c, H.Node) else L.unescape(c))
    last = ''.join(buf).strip()
    if last:
        lines.append(last)
    code = '\n'.join(l for l in lines if l).replace('\xa0', ' ')
    code = RE_EMOJI_OTHER.sub('', code)
    code = re.sub(r'[ \t]+$', '', code, flags=re.M)
    if not code.strip():
        return []
    return _wrap_rtl('\n'.join([r'\begin{tcblisting}{colback=codebg,colframe=lightrule,boxrule=0.4pt,'
                                r'arc=1.5pt,left=8pt,right=8pt,top=5pt,bottom=5pt,listing only,'
                                r'breakable,enhanced,listing options={style=bookcode}}',
                                code, r'\end{tcblisting}']))


CHIP_BY_CLASS = (('indigo', r'\chipi'), ('primary', r'\chipi'), ('green', r'\chipg'),
                 ('red', r'\chipr'), ('amber', r'\chipa'), ('gray', r'\chips'))
ARROWS = {'➜': r'\textcolor{teal}{\bfseries →}', '⇄': r'\textcolor{teal}{\bfseries ⇄}',
          '→': r'\textcolor{teal}{\bfseries →}', '←': r'\textcolor{teal}{\bfseries ←}',
          '↔': r'\textcolor{teal}{\bfseries ↔}', '│': r'\textcolor{slate}{│}'}


def _figure(node, ctx):
    """图形：SVG → 居中插图；纯文字流程图 → 圆角小方块 + 箭头；统一配图注。"""
    caption = ''
    for p in node.find_all('p'):
        t = L.inline_text_of_children(p).strip()
        if t:
            caption = t
            break

    svg = node.find('svg')
    ctx['figure_seq'] += 1
    if svg is not None:
        name = f"fig-{ctx['chapter_id']}-{ctx['figure_seq']}"
        outdir = ctx['figures_dir']
        outdir.mkdir(parents=True, exist_ok=True)
        pdf = outdir / f'{name}.pdf'
        ok = pdf.exists()
        if not ok and ctx['svg_converter']:
            ok = ctx['svg_converter'](H.render(svg), pdf)
        if ok:
            lines = [r'\begin{center}',
                     r'\includegraphics[width=0.9\linewidth]{figures_v2/' + name + '}']
            if caption:
                lines.append(r'\\[6pt]{\small\color{slate} ' + L.pair_quotes(caption) + r'}')
            lines.append(r'\end{center}')
            return '\n'.join(lines)
        if caption:
            return [r'\begin{center}\small\color{slate} 【图示：' +
                    L.pair_quotes(caption) + r'，详见在线版】\end{center}']

    # 纯文字流程图：每个 flex 行为一行，方块 = span，灰色 span = 箭头
    rows = []
    for row in node.element_children():
        if row.tag != 'div':
            continue
        items = []
        for span in row.element_children():
            if span.tag != 'span':
                continue
            txt = L.inline_text_of_children(span).strip()
            if not txt:
                continue
            cls = ' '.join(span.classes)
            if 'text-gray' in cls and txt in ARROWS:
                items.append(('arrow', ARROWS[txt]))
                continue
            box = r'\chipi'
            for key, macro in CHIP_BY_CLASS:
                if key in cls:
                    box = macro
                    break
            items.append(('chip', box + '{' + L.pair_quotes(txt) + '}'))
        if not items:
            continue
        # 把箭头并进它后面的方块（\mbox），换行只会发生在方块之前，不会留下孤立箭头
        parts, pending = [], []
        for kind, tex in items:
            if kind == 'arrow':
                pending.append(tex)
                continue
            if pending:
                parts.append(r'\mbox{' + r'\,'.join(pending) + r'\,' + tex + '}')
                pending = []
            else:
                parts.append(tex)
        if pending:
            parts.append(r'\ '.join(pending))
        rows.append(r'\begin{center}' + r'\ '.join(parts) + r'\end{center}')
    if caption:
        rows.append(r'\begin{center}{\small\color{slate} ' +
                    L.pair_quotes(caption) + r'}\end{center}')
    return '\n'.join(rows)


# ---- 章节标题拆分：h3「第X章：标题」→ 眉标 + 标题 + 目录项 ----
_ORIG_BLOCKS = L.blocks
RE_EYEBROW = re.compile(r'^([^：:]{1,12})[：:]\s*(\S.*)$', re.S)


def blocks_chapter(node, ctx):
    if isinstance(node, H.Node) and node.tag == 'h3' and ctx.get('kind') == 'chapter':
        title = L.inline_text_of_children(node).strip()
        m = RE_EYEBROW.match(title)
        if m and m.group(2):
            eb = L.pair_quotes(m.group(1).strip())
            rest = L.pair_quotes(m.group(2).strip())
        else:
            eb, rest = r'\relax', L.pair_quotes(title)
        return [r'\bookchapter{' + eb + '}{' + rest + '}{' + L.pair_quotes(title) + '}']
    res = _ORIG_BLOCKS(node, ctx)
    # bookkit 对 font-mono 段落返回的是字符串而不是列表；统一成列表，
    # 否则调用方的 extend() 会把它按字符拆开（曾导致整页竖排乱码）
    return [res] if isinstance(res, str) else res


L._table = _table
L._code_block = _code_block
L._mono_paragraph = _mono_paragraph
L._figure = _figure
L.blocks = blocks_chapter


# ------------------------------------------------------------------ 清理

GLYPH_FIX = {'\u30fb': '\u00b7', '\u301c': '\uff5e'}   # ・→·  〜→～


def _fix_glyphs(tex: str) -> str:
    """替换字体缺字形的字符；代码块内部保持原样。"""
    out, in_code = [], False
    for line in tex.split('\n'):
        st = line.strip()
        if st.startswith(r'\begin{lstlisting}') or st.startswith(r'\begin{tcblisting}'):
            in_code = True
        elif st.startswith(r'\end{lstlisting}') or st.startswith(r'\end{tcblisting}'):
            in_code = False
        if not in_code:
            for a, b in GLYPH_FIX.items():
                line = line.replace(a, b)
        out.append(line)
    return '\n'.join(out)


# ------------------------------------------------------------------ 主流程

def build_file(html_path: Path, work_dir: Path) -> dict:
    raw = html_path.read_text(encoding='utf-8')
    # 源文件存在的畸形闭合标签（如 v1.7/zh-CN.html 的 "</div " 缺少 ">"）会让后续开标签被吞掉，
    # 这里只在内存里修补，不改动仓库中的 HTML
    raw = re.sub(r'</(div|section|ul|ol|li|p)\s+(?=<)', r'</\1>', raw)
    tree = H.parse(raw)
    lang = lang_of(html_path, raw)
    lang_symbols(lang)
    global RTL_MODE
    RTL_MODE = lang in RTL_LANGS

    title_m = re.search(r'<title>([\s\S]{0,200}?)</title>', raw)
    title = re.sub(r'\s*·\s*v[\d.]+\s*$', '',
                   (title_m.group(1).strip() if title_m else html_path.stem))
    version = html_path.parent.name
    desc = ''
    for pat in (r'<meta[^>]*property="og:description"[^>]*content="([^"]{0,400})"',
                r'<meta[^>]*name="description"[^>]*content="([^"]{0,400})"'):
        m = re.search(pat, raw)
        if not m:
            continue
        first = re.split(r'[。！？.!?]', m.group(1))[0].strip()
        # 首句若只是书名的前缀（如“搞定手机”），做副标题没有信息量，跳过
        if 2 < len(first) <= 46 and first not in title and not title.startswith(first):
            desc = first
            break

    work_dir.mkdir(parents=True, exist_ok=True)
    (work_dir / 'figures_v2').mkdir(exist_ok=True)

    # 部分语言文件存在提前闭合，区块会落到 <main> 之外 → 统一按全树扫描
    scope = tree
    parts = [n for n in scope.find_all('section')
             if n.find('div', cls='content-section') is not None]
    part_ids = {n.get('id') for n in parts}
    secs = [n for n in scope.find_all('div') if 'content-section' in n.classes]
    # 按文档序单遍组织：章的篇归属 = 祖先链上的 <section>；
    # 个别文件因畸形标签被解析器挂到 main 下（坐标其实正常），
    # 这类章沿用前一章的篇归属，保持文档顺序，避免被甩到书尾。
    ordered = []
    last_pid = None
    for c in secs:
        pid = None
        a = c.parent
        while a is not None:
            if getattr(a, 'tag', '') == 'section' and a.get('id') in part_ids:
                pid = a.get('id')
                break
            a = a.parent
        if pid is None:
            pid = last_pid
        if pid is not None:
            ordered.append((pid, c))
            last_pid = pid

    u = ui_of(lang)
    meta = {'title': title, 'version': version, 'lang': lang,
            'date': '2026 年 10 月', 'date_en': 'October 2026',
            'nchap': len(ordered), 'nparts': len(parts),
            'license': 'CC BY-NC-SA 4.0', 'subtitle': desc}

    ctx = {'figure_seq': 0, 'chapter_id': 'x', 'kind': 'chapter', 'top': r'\bookchapter',
           'figures_dir': work_dir / 'figures_v2',
           'svg_converter': make_svg_converter(lang)}

    lines = preamble(lang, meta)
    lines.append(r'\hypersetup{pdftitle={' + L.clean(title) + ' ' + version + r'},'
                 r'pdfauthor={ClassTechStar},pdfcreator={XeLaTeX},bookmarksnumbered=false}')
    lines.append(r'\begin{document}')
    lines.extend(cover_tex(meta, u))
    lines.extend(colophon_tex(meta, u, lang))
    # 目录页眉标记要在 \tableofcontents 之前发出：放在之后会在目录恰好排满时多出一张空页
    lines.append(r'\renewcommand{\contentsname}{' + u['toc'] + '}')
    lines.append(r'\frontmatter')
    # book.cls 的 \tableofcontents 内部会 \@mkboth{目录}{目录}，导致页眉出现两遍；
    # 局部把 \@mkboth 变空，只保留上面那一次 \markright
    lines.append(r'\markright{' + u['toc'] + r'}')
    lines.append(r'\begingroup\makeatletter\let\@mkboth\@gobbletwo\makeatother')
    lines.append(r'\tableofcontents')
    lines.append(r'\endgroup')
    # 不用 \mainmatter：book 的 twoside \cleardoublepage 会在目录后插一张空白页
    lines.append(r'\clearpage\pagenumbering{arabic}')

    chapter_files = []
    current_part = None
    for i, (pid, node) in enumerate(ordered):
        if pid and pid != current_part:
            current_part = pid
            label = pid
            pnode = next((n for n in parts if n.get('id') == pid), None)
            if pnode is not None:
                for h in pnode.find_all('h2') + pnode.find_all('h1'):
                    txt = re.sub(r'\s+', ' ', H.text_of(h)).strip()
                    if txt:
                        label = txt
                        break
            lines.append(r'\bookpart{' + L.pair_quotes(L.clean(label)) + '}')
            if pnode is not None:
                intro_p = next((c for c in pnode.element_children() if c.tag == 'p'), None)
                if intro_p is not None:
                    intro_tex = L._flatten(L.blocks(intro_p, ctx))
                    if intro_tex:
                        lines.append(r'\begin{partintro}')
                        lines.extend(intro_tex)
                        lines.append(r'\end{partintro}')
        cid = node.get('id')
        ctx['chapter_id'] = cid
        ctx['kind'] = 'chapter'
        ctx['top'] = r'\bookchapter'
        ctx['figure_seq'] = 0
        # 少数章节的首段漏了 chapter-intro 类：仍按“本章导读”处理，保证 opener 一致
        kids = [c for c in node.children if isinstance(c, H.Node)]
        intro_node = None
        if not any(c.tag == 'p' and 'chapter-intro' in c.classes for c in kids):
            h3 = next((c for c in kids if c.tag == 'h3'), None)
            numbered = h3 is not None and re.match(
                r'^第[零一二三四五六七八九十百]+章', H.text_of(h3).strip())
            if numbered:
                i = kids.index(h3)
                nxt = kids[i + 1] if i + 1 < len(kids) else None
                if nxt is not None and nxt.tag == 'p':
                    plain = re.sub(r'\\[a-zA-Z]+|[{}$]', '',
                                   L.inline_text_of_children(nxt).strip())
                    if len(plain) >= 20:
                        intro_node = nxt
        chunks = []
        for c in node.children:
            if intro_node is not None and c is intro_node:
                chunks.append(r'\chapterintro{' +
                              L.pair_quotes(L.inline_text_of_children(intro_node).strip()) + '}')
                continue
            res = L.blocks(c, ctx)
            if isinstance(res, str):
                chunks.append(res)
            else:
                chunks.extend(res)
        body = L._flatten(chunks)
        rel = f'ch{i:02d}-{cid}.tex'
        (work_dir / rel).write_text(_fix_glyphs('\n\n'.join(body) + '\n'),
                                    encoding='utf-8', newline='\n')
        chapter_files.append(rel)
        lines.append(r'\input{' + rel + '}')

    lines.append(r'\end{document}')
    (work_dir / 'main.tex').write_text(_fix_glyphs('\n'.join(lines) + '\n'),
                                       encoding='utf-8', newline='\n')
    return {'work': str(work_dir), 'lang': lang, 'title': title, 'version': version,
            'chapters': len(chapter_files), 'parts': len(parts), 'subtitle': desc}


def _hash(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest() if path.exists() else ''


def compile_pdf(work_dir: Path, out_pdf: Path, max_passes: int = 4) -> dict:
    env = dict(os.environ)
    env['PATH'] = MIKTEX + os.pathsep + env.get('PATH', '')
    env['TEXINPUTS'] = str(work_dir) + os.pathsep + env.get('TEXINPUTS', '')
    prev = None
    for _ in range(max_passes):
        subprocess.run(['xelatex', '-interaction=nonstopmode', '-file-line-error', 'main.tex'],
                       cwd=str(work_dir), env=env, capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
        # 目录与交叉引用稳定后即停，避免多余编译
        cur = (_hash(work_dir / 'main.toc'), _hash(work_dir / 'main.aux'))
        if cur == prev:
            break
        prev = cur
    log_p = work_dir / 'main.log'
    log = log_p.read_text(encoding='utf-8', errors='replace') if log_p.exists() else ''
    m = re.search(r'Output written on main\.pdf \((\d+) pages', log)
    errors = len(re.findall(r'^! ', log, re.M))
    missing = sorted(set(re.findall(r'Missing character: There is no (.+?) in font', log)))
    out_pdf.parent.mkdir(parents=True, exist_ok=True)
    src = work_dir / 'main.pdf'
    if src.exists():
        out_pdf.write_bytes(src.read_bytes())
    return {'pdf': str(out_pdf), 'pages': int(m.group(1)) if m else 0, 'errors': errors,
            'missing_kinds': len(missing), 'missing': ' '.join(missing)[:40],
            'size': out_pdf.stat().st_size if out_pdf.exists() else 0}


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'one':
        html = Path(sys.argv[2])
        info = build_file(html, WORK_DIR / f"{html.parent.name}-{html.stem}")
        print(info, flush=True)
        out = PDF_DIR / html.parent.name / f'{html.stem}.pdf'
        print(compile_pdf(Path(info['work']), out), flush=True)
        return
    if cmd == 'book':
        html = Path(sys.argv[2])
        out = Path(sys.argv[3])
        info = build_file(html, WORK_DIR / f"book-{html.parent.name}-{html.stem}")
        print(info, flush=True)
        print(compile_pdf(Path(info['work']), out), flush=True)
        return
    if cmd == 'version':
        version = sys.argv[2]
        vdir = REPO / version
        files = sorted(vdir.glob('*.html'))
        print(f'{version}: {len(files)} 个文件', flush=True)
        for html in files:
            try:
                info = build_file(html, WORK_DIR / f'{version}-{html.stem}')
                out = PDF_DIR / version / f'{html.stem}.pdf'
                res = compile_pdf(Path(info['work']), out)
                print(f"  {html.stem:6s} lang={info['lang']:5s} 章={info['chapters']:3d} "
                      f"页={res['pages']:4d} 错误={res['errors']} 缺字形={res['missing_kinds']} "
                      f"{res['missing']} {res['size']//1024}KB", flush=True)
            except Exception as e:
                print(f"  {html.stem}: 失败 {e}", flush=True)
        return
    print(__doc__)


if __name__ == '__main__':
    main()
