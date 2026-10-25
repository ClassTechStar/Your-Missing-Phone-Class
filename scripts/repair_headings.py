"""章节标题修复：损坏回填 + 编号风格统一。

用法：
  python scripts/repair_headings.py            # 干跑，输出变更报告
  python scripts/repair_headings.py --apply    # 写盘

修复内容：
1. 损坏回填：h3 被正文片段顶替的章节，从同语言 v1.6/v1.5 回填
   h3/导语/h4/h5 标题文本（数量与 zh 结构一致时）；无来源时用侧栏标题兜底 h3。
2. 编号统一：词形数字 → 阿拉伯数字（ru/ar/he/fr/pt/en/el/th）；
   ja 按文件多数派统一（第4章 ↔ 第四章）；ko 补 제 前缀与冒号空格；
   各语言"章附"前缀统一为该语言多数形式。
"""
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from bookkit import htmlparse as H  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from translation_overrides import OVERRIDES, V_OVERRIDES  # noqa: E402

APPLY = '--apply' in sys.argv
VERSIONS = [a for a in sys.argv[1:] if re.match(r'^v1\.[5-8]$', a)] or ['v1.8']

# ---------------------------------------------------------------- 分类

NUM = r'(?:[0-9０-９]+|[零〇一二三四五六七八九十百两]+)'
CH_PAT = [
    r'第\s*%s\s*[章回]' % NUM,
    r'제\s*(?:[0-9]+|[영일이삼사오육칠팔구십백]+)\s*장',
    r'(?:Chapter|Capitolo|Cap[íi]tulo|Chapitre|Kapitel|Глава|Chương|Κεφάλαιο|บทที่|Bab|الفصل|פרק)\s*'
    r'(?:[0-9٠-๙]+|[A-Za-zА-Яа-яёЁΑ-Ωα-ωάέήίόύώ]{2,20})?',
    r'Cap[íi]tulo\s*[0-9]+',
]
SUP_PAT = [
    r'^(第\s*%s\s*章)?\s*(附|附錄|附録|付録|附录)' % NUM,
    r'^(Chapter|Kapitel|Capitolo|Cap[íi]tulo|Chapitre|Глава|บทที่)\s*[0-9]?\s*'
    r'(Appendix|Appendice|Anhang|Annexe|Ap[áàâãéêe]ndice|Anexo|Приложение|Supplement|ภาคผนวก)',
    r'^(Appendix|Appendice|Anhang|Annexe|Ap[áàâãéêe]ndice|Anexo|Приложение|נספח|الملحق|ملحق|ภาคผนวก|'
    r'Lampiran|Tambahan|Παράρτημα|부록|Parannos|Phụ lục|附錄|付録|附录)',
    r'^(Epilog|Epilogue|Conclusion|Conclusão|Conclusi|Ep[íi]logo|結び|おわりに|맺음말|Επίλογος|'
    r'خاتمة|סיום|דברי סיכום|บทส่งท้าย|Penutup|Nachwort|结语|結語|后记|後記|Заключение|Kết luận)',
]
RE_CH = re.compile(r'^(?:%s)' % '|'.join(CH_PAT))
RE_SUP = re.compile(r'^(?:%s)' % '|'.join(SUP_PAT))


def classify(t: str) -> str:
    t = (t or '').strip()
    if not t:
        return 'empty'
    if RE_SUP.match(t):
        return 'supplement'
    if RE_CH.match(t):
        return 'title'
    return 'other'


def plain(s: str) -> str:
    import html as hm
    return re.sub(r'\s+', ' ', hm.unescape(re.sub(r'<[^>]+>', '', s))).strip()

# ---------------------------------------------------------------- 数字表


def cjk_num(n: int) -> str:
    digits = '零一二三四五六七八九'
    if n < 10:
        return digits[n]
    if n == 10:
        return '十'
    if n < 20:
        return '十' + digits[n - 10]
    tens = ['', '', '二十', '三十', '四十', '五十', '六十', '七十', '八十', '九十']
    return tens[n // 10] + (digits[n % 10] if n % 10 else '')

CJK_OF_DIGIT = {str(i): cjk_num(i) for i in range(0, 70)}

RU_ORD = {
    1: 'первая', 2: 'вторая', 3: 'третья', 4: 'четвёртая', 5: 'пятая', 6: 'шестая',
    7: 'седьмая', 8: 'восьмая', 9: 'девятая', 10: 'десятая', 11: 'одиннадцатая',
    12: 'двенадцатая', 13: 'тринадцатая', 14: 'четырнадцатая', 15: 'пятнадцатая',
    16: 'шестнадцатая', 17: 'семнадцатая', 18: 'восемнадцатая', 19: 'девятнадцатая',
    20: 'двадцатая', 21: 'двадцать первая', 22: 'двадцать вторая', 23: 'двадцать третья',
    24: 'двадцать четвёртая', 25: 'двадцать пятая', 26: 'двадцать шестая',
    27: 'двадцать седьмая', 28: 'двадцать восьмая', 29: 'двадцать девятая',
    30: 'тридцатая', 31: 'тридцать первая', 32: 'тридцать вторая', 33: 'тридцать третья',
    34: 'тридцать четвёртая', 35: 'тридцать пятая', 36: 'тридцать шестая',
}

def _ar_units():
    u = {1: 'الحادي', 2: 'الثاني', 3: 'الثالث', 4: 'الرابع', 5: 'الخامس',
         6: 'السادس', 7: 'السابع', 8: 'الثامن', 9: 'التاسع'}
    return u

AR_FORMS = {'الصفري': 0, 'الأول': 1, 'الثاني': 2, 'الثالث': 3, 'الرابع': 4,
            'الخامس': 5, 'السادس': 6, 'السابع': 7, 'الثامن': 8, 'التاسع': 9,
            'العاشر': 10,
            'الحادي عشر': 11, 'الثاني عشر': 12, 'الثالث عشر': 13, 'الرابع عشر': 14,
            'الخامس عشر': 15, 'السادس عشر': 16, 'السابع عشر': 17, 'الثامن عشر': 18,
            'التاسع عشر': 19}
for _t, (_n10, _n10g) in {20: ('العشرون', 'العشرين'), 30: ('الثلاثون', 'الثلاثين'),
                          40: ('الأربعون', 'الأربعين'), 50: ('الخمسون', 'الخمسين'),
                          60: ('الستون', 'الستين')}.items():
    AR_FORMS[_n10] = _t
    AR_FORMS[_n10g] = _t
    for _u, _w in _ar_units().items():
        n = _t + _u
        AR_FORMS[f'{_w} و{_n10}'] = n
        AR_FORMS[f'{_w} و{_n10g}'] = n

HE_FORMS = {'ראשון': 1, 'שני': 2, 'שלישי': 3, 'רביעי': 4, 'חמישי': 5,
            'שישי': 6, 'שביעי': 7, 'שמיני': 8, 'תשיעי': 9, 'עשירי': 10}
FR_FORMS = {'zéro': 0, 'un': 1, 'deux': 2, 'trois': 3, 'quatre': 4, 'cinq': 5,
            'six': 6, 'sept': 7, 'huit': 8, 'neuf': 9, 'dix': 10, 'onze': 11,
            'douze': 12, 'treize': 13, 'quatorze': 14, 'quinze': 15, 'seize': 16,
            'vingt': 20, 'trente': 30}
PT_FORMS = {'Zero': 0, 'Um': 1, 'Dois': 2, 'Três': 3, 'Quatro': 4, 'Cinco': 5,
            'Seis': 6, 'Sete': 7, 'Oito': 8, 'Nove': 9, 'Dez': 10, 'Onze': 11,
            'Doze': 12, 'Vinte': 20, 'Trinta': 30}
TH_FORMS = {'ศูนย์': 0, 'หนึ่ง': 1, 'สอง': 2, 'สาม': 3, 'สี่': 4, 'ห้า': 5,
            'หก': 6, 'เจ็ด': 7, 'แปด': 8, 'เก้า': 9, 'สิบ': 10, 'ยี่สิบ': 20}

# 词形 → 数字： (语言 → (正则, 替换函数))
WORD_PATTERNS = {
    'ru': (re.compile(r'([Гг]лав[аыоеу])\s+(%s)' % '|'.join(sorted(
        (re.escape(v) for v in RU_ORD.values()), key=len, reverse=True))),
        lambda m: f"{m.group(1)} {next(k for k, v in RU_ORD.items() if v == m.group(2))}"),
    'ar': (re.compile(r'(الفصل)\s+(%s)' % '|'.join(sorted(
        (re.escape(v) for v in AR_FORMS), key=len, reverse=True))),
        lambda m: f"{m.group(1)} {AR_FORMS[m.group(2)]}"),
    'he': (re.compile(r'(פרק)\s+(%s)' % '|'.join(sorted(
        (re.escape(v) for v in HE_FORMS), key=len, reverse=True))),
        lambda m: f"{m.group(1)} {HE_FORMS[m.group(2)]}"),
    'fr': (re.compile(r'([Cc]hapitre)\s+(%s)\b' % '|'.join(FR_FORMS)),
           lambda m: f"{m.group(1)} {FR_FORMS[m.group(2)]}"),
    'pt': (re.compile(r'([Cc]ap[íi]tulo)\s+(%s)\b' % '|'.join(PT_FORMS)),
           lambda m: f"{m.group(1)} {PT_FORMS[m.group(2)]}"),
    'en': (re.compile(r'(Chapter)\s+Zero\b'), lambda m: f"{m.group(1)} 0"),
    'el': (re.compile(r'(Κεφάλαιο)\s+Μηδέν\b'), lambda m: f"{m.group(1)} 0"),
    'th': (re.compile(r'(บทที่)\s*(%s)' % '|'.join(TH_FORMS)),
           lambda m: f"{m.group(1)} {TH_FORMS[m.group(2)]}"),
}

# 各语言「章附」前缀统一： (正则, 替换) —— 作用于 h3 与侧栏标题文本
SUPPL_RE = {
    'en': [(re.compile(r'^Chapter (\d+) Supplement:\s*'), r'Chapter \1 Appendix: ')],
    'de': [(re.compile(r'^Anhang zu Kapitel (\d+):\s*'), r'Kapitel \1 Anhang: ')],
    'fr': [(re.compile(r'^Chapitre (\d+) [Aa]nnexe\s*:\s*'), r'Chapitre \1 Annexe : '),
           (re.compile(r'^Annexe chapitre (\d+)\s*:\s*'), r'Chapitre \1 Annexe : '),
           (re.compile(r'^Annexe au [Cc]hapitre (\d+)\s*:\s*'), r'Chapitre \1 Annexe : ')],
    'es': [(re.compile(r'^Ap[ée]ndice Cap (\d+)\s*:\s*'), r'Anexo del Capítulo \1: '),
           (re.compile(r'^Anexo al capítulo (\d+)\s*:\s*'), r'Anexo del Capítulo \1: ')],
    'it': [(re.compile(r'^Appendice Capitolo (\d+)\s*:\s*'), r'Appendice al Capitolo \1: ')],
    'el': [(re.compile(r'^Παράρτημα Κεφαλαίου (\d+)\s*:\s*'), r'Κεφάλαιο \1 Παράρτημα: ')],
    'th': [(re.compile(r'^ภาคผนวกบทที่\s*(\d+)\s*:\s*'), r'บทที่ \1 ภาคผนวก: ')],
}

# 小修：冒号空格等
PUNCT_FIX = {
    'ko': [(re.compile(r'제(\d+)장\s*：\s*'), r'제\1장: '),
           (re.compile(r'제(\d+)장부록'), r'제\1장 부록'),
           (re.compile(r'(맺음말):(?=\S)'), r'\1: ')],
    'th': [(re.compile(r'(บทส่งท้าย):(?=\S)'), r'\1: ')],
}

# zh 源稿重复标题修复对应到各语言的位置：删除空壳 / 保留正文顺号 +1
DUP_DELETE = {('di-wu-shi-san-zhang', 5), ('di-wu-shi-si-zhang', 5),
              ('di-wu-shi-wu-zhang', 4), ('di-wu-shi-ba-zhang', 4),
              ('di-liu-shi-zhang', 4), ('di-liu-shi-zhang', 7),
              ('di-liu-shi-jiu-zhang', 3)}
DUP_RENUM = {('di-wu-shi-san-zhang', 6), ('di-wu-shi-si-zhang', 6),
             ('di-wu-shi-wu-zhang', 5), ('di-wu-shi-ba-zhang', 5),
             ('di-liu-shi-zhang', 8), ('di-liu-shi-jiu-zhang', 4)}
DUP_DELETE_BY_SID = {}
for _s, _k in DUP_DELETE:
    DUP_DELETE_BY_SID.setdefault(_s, []).append(_k)

def _h4_has_body(raw, base, m, h4re):
    """该 h4 到下一个 h4/h3 之间是否有可见文本。"""
    nxt = h4re.search(raw, m.end())
    seg = raw[m.end(): nxt.start() if nxt else m.end() + 4000]
    seg = re.split(r'<h[34][\s>]', seg)[0]
    txt = re.sub(r'<[^>]+>', '', seg)
    import html as _h
    return bool(_h.unescape(txt).strip())

def bump_number(text: str, new_val: int) -> str:
    """把标题首部编号改为 new_val（保持原编号风格）。"""
    t = plain(text)
    t = re.sub(r'[ً-ْٰـ]', '', t)
    m = re.match(r'^([0-9]{1,2})(\.(?!\d)|[、）)，,])', t)
    if m:
        return text.replace(t[:m.end(1)], str(new_val), 1)
    m = re.match(r'^([IVX]{1,5})\.', t)
    if m:
        inv = {v: k for k, v in ROMAN.items()}
        return text.replace(m.group(1), inv.get(new_val, m.group(1)), 1)
    m = re.match(r'^([零〇一二三四五六七八九十]{1,3})[、，,]', t)
    if m:
        return text.replace(m.group(1), cjk_num(new_val), 1)
    m = re.match(r'^(أولا|ثانيا|ثالثا|رابعا|خامسا|سادسا|سابعا|ثامنا|تاسعا|عاشرا|صفر)(\s*[:：])', t)
    if m:
        inv = {v: k for k, v in AR_ORD.items() if k in ('اولا','ثانيا','ثالثا','رابعا','خامسا','سادسا','سابعا','ثامنا','تاسعا','عاشرا','صفر')}
        old = {1:'أولا',2:'ثانيا',3:'ثالثا',4:'رابعا',5:'خامسا',6:'سادسا',7:'سابعا',8:'ثامنا',9:'تاسعا',10:'عاشرا',0:'صفر'}
        return text.replace(m.group(1), old.get(new_val, m.group(1)), 1)
    m = re.match(r'^(Erstens|Zweitens|Drittens|Viertens|Fünftens|Sechstens|Siebtens|Achtens|Neuntens)\.', t)
    if m:
        order = ['Null','Erstens','Zweitens','Drittens','Viertens','Fünftens','Sechstens','Siebtens','Achtens','Neuntens','Zehntens']
        return text.replace(m.group(1), order[new_val] if new_val < len(order) else m.group(1), 1)
    m = re.match(r"^(Α|Β|Γ|Δ|Ε|ΣΤ|Ζ|Η|Θ|Ι|Κ)\.", t)
    if m:
        letters = ['Α','Β','Γ','Δ','Ε','ΣΤ','Ζ','Η','Θ','Ι','Κ','Λ']
        return text.replace(m.group(1), letters[new_val-1] if new_val <= len(letters) else m.group(1), 1)
    m = re.match(r'^(일|이|삼|사|오|육|칠|팔|구|십)[,，、]', t)
    if m:
        order = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구', '십']
        return text.replace(m.group(1), order[new_val] if new_val < len(order) else m.group(1), 1)
    m = re.match(r'^(Satu|Dua|Tiga|Empat|Lima|Enam|Tujuh|Lapan|Sembilan|Sepuluh)(\s*[,，])', t)
    if m:
        words = ['Satu','Dua','Tiga','Empat','Lima','Enam','Tujuh','Lapan','Sembilan','Sepuluh']
        return text.replace(m.group(1), words[new_val-1] if new_val <= len(words) else m.group(1), 1)
    return text

CH3_RENUM = {
    'ja': ('五、', '六、'), 'zh-TW': ('五、', '六、'), 'yue': ('五、', '六、'),
    'lzh': ('五、', '六、'), 'ko': ('5.', '6.'), 'id': ('5.', '6.'), 'th': ('5.', '6.'),
    'fr': ('5.', '6.'), 'en': ('V.', 'VI.'), 'es': ('V.', 'VI.'), 'pt': ('V.', 'VI.'),
    'el': ('V.', 'VI.'), 'de': ('Fünf.', 'Sechs.'), 'ru': ('5.', '6.'), 'it': ('5.', '6.'),
    'he': ('5.', '6.'), 'id': ('5.', '6.'), 'ms': ('5.', '6.'),
}

H3_RE = re.compile(r'<h3 class="text-xl font-bold text-dark dark:text-gray-200 mb-4"\s*>(.*?)</h3>', re.S)
INTRO_RE = re.compile(r'<p class="chapter-intro mb-4">(.*?)</p>', re.S)
H4_RE = re.compile(r'<h4 class="text-lg font-semibold (?:mt-4|mt-6) mb-2">(.*?)</h4>', re.S)
H5_RE = re.compile(r'<h5 class="font-semibold mt-\d mb-1">(.*?)</h5>', re.S)
SEC_RE = re.compile(r'<div[^>]*\bid="([a-z0-9-]+)"[^>]*\bclass="[^"]*content-section[^"]*"[^>]*>')
SB_ANCHOR_RE = lambda sid: re.compile(
    r'(<a[^>]*href="#%s"[^>]*>\s*(?:<span[^>]*>[^<]*</span>\s*)?)([^<]*)(</a>)' % re.escape(sid))

PROTECT_RE = re.compile(
    r'(<pre\b.*?</pre>|<code\b.*?</code>|<script\b.*?</script>|<style\b.*?</style>)', re.S | re.I)

# ---------------------------------------------------------------- h4 编号值解析

ROMAN = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8,
         'IX': 9, 'X': 10, 'XI': 11, 'XII': 12}
CJK_DIG = '零一二三四五六七八九十'
AR_ORD = {'صفر': 0, 'أولا': 1, 'ثانيا': 2, 'ثالثا': 3, 'رابعا': 4, 'خامسا': 5,
          'سادسا': 6, 'سابعا': 7, 'ثامنا': 8, 'تاسعا': 9, 'عاشرا': 10,
          'واحد': 1, 'اثنان': 2, 'ثلاثة': 3, 'أربعة': 4, 'خمسة': 5, 'ستة': 6,
          'سبعة': 7, 'ثمانية': 8, 'تسعة': 9}
HE_LET = {'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10}
HE_WORD = {'אחת': 1, 'שתיים': 2, 'שלוש': 3, 'ארבע': 4, 'אחד': 1, 'שניים': 2,
           'חמישה': 5, 'שישה': 6, 'שבעה': 7, 'שלושה': 3, 'ארבעה': 4,
           'חמש': 5, 'שש': 6, 'שבע': 7, 'שמונה': 8, 'תשעה': 9, 'עשרה': 10}
TH_WORD = {'ศูนย์': 0, 'หนึ่ง': 1, 'สอง': 2, 'สาม': 3, 'สี่': 4, 'ห้า': 5, 'หก': 6,
           'เจ็ด': 7, 'แปด': 8, 'เก้า': 9}
KO_WORD = {'하나': 1, '둘': 2, '셋': 3, '넷': 4, '다섯': 5, '여섯': 6, '일곱': 7, '여덟': 8, '아홉': 9}
KO_HANJA = {'일': 1, '이': 2, '삼': 3, '사': 4, '오': 5, '육': 6, '칠': 7, '팔': 8, '구': 9, '십': 10}
PT_H4 = {'Zero': 0, 'Um': 1, 'Dois': 2, 'Três': 3, 'Quatro': 4, 'Cinco': 5, 'Seis': 6,
         'Sete': 7, 'Oito': 8, 'Nove': 9, 'Dez': 10}
DE_WORD = {'Eins': 1, 'Zwei': 2, 'Drei': 3, 'Vier': 4, 'Fünf': 5, 'Sechs': 6,
           'Sieben': 7, 'Acht': 8, 'Neun': 9}
EL_WORD = {'Πρώτο': 1, 'Δεύτερο': 2, 'Τρίτο': 3, 'Τέταρτο': 4, 'Πέμπτο': 5,
           'Έκτο': 6, 'Έβδομο': 7, 'Όγδοο': 8, 'Ένατο': 9, 'Δέκατο': 10}
DE_ORD = {'Null': 0, 'Erstens': 1, 'Zweitens': 2, 'Drittens': 3, 'Viertens': 4, 'Fünftens': 5,
          'Sechstens': 6, 'Siebtens': 7, 'Achtens': 8, 'Neuntens': 9}
MS_WORD = {'Satu': 1, 'Dua': 2, 'Tiga': 3, 'Empat': 4, 'Lima': 5, 'Enam': 6,
           'Tujuh': 7, 'Lapan': 8, 'Delapan': 8, 'Sembilan': 9, 'Sepuluh': 10,
           'Sifar': 0, 'Kosong': 0}
EL_LET = {'Α': 1, 'Β': 2, 'Γ': 3, 'Δ': 4, 'Ε': 5, 'ΣΤ': 6, 'Ζ': 7, 'Η': 8,
          'Θ': 9, 'Ι': 10, 'Κ': 11}

def h4_number(text: str):
    """解析 h4 开头的编号值；无编号返回 None。版本号（1.6）不算编号。"""
    t = plain(text).translate({ord('０') + i: str(i) for i in range(10)})
    t = re.sub(r'[ً-ْٰـ]', '', t)   # 阿拉伯语发音符号归一
    m = re.match(r'^([0-9]{1,2})\.(?!\d)', t)
    if m:
        return int(m.group(1))
    m = re.match(r'^([0-9]{1,2})[、）)，,]', t)
    if m:
        return int(m.group(1))
    m = re.match(r'^([IVX]{1,5})\.', t)
    if m:
        return ROMAN.get(m.group(1))
    m = re.match(r'^([零〇一二三四五六七八九十]{1,3})[、，,]', t)
    if m:
        table = {'零': 0, '〇': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6,
                 '七': 7, '八': 8, '九': 9, '十': 10}
        return table.get(m.group(1))
    m = re.match(r'^บทที่\s*([0-9]+)', t)
    if m:
        return int(m.group(1))
    m = re.match(r'^(' + '|'.join(AR_ORD) + r')\s*[:：]', t)
    if m:
        return AR_ORD[m.group(1)]
    for table, pat in ((HE_WORD, r'^(%s)\b'), (TH_WORD, r'^(%s)(?=[ 0-9(、.,:：]|$)'),
                       (KO_WORD, r'^(%s)[,，]'), (DE_WORD, r'^(%s)\.'),
                       (EL_WORD, r'^(%s)\s*[:：]'), (KO_HANJA, r'^(%s)[,，、]'),
                       (PT_H4, r'^(%s)\.'), (DE_ORD, r'^(%s)\.'),
                       (MS_WORD, r'^(%s)\s*[,，]'), (EL_LET, r'^(%s)\s*\.')):
        m = re.match(pat % '|'.join(table), t)
        if m:
            return table[m.group(1)]
    m = re.match(r"^([אבגדהוזחטי])\s*[.'’]", t)
    if m:
        return HE_LET.get(m.group(1))
    return None


def protected_sub(text: str, regex, repl, report, tag):
    """跳过 pre/code/script/style 的全局替换。"""
    out, pos, n = [], 0, 0
    for m in PROTECT_RE.finditer(text):
        seg = text[pos:m.start()]
        seg, k = regex.subn(repl, seg)
        n += k
        out.append(seg)
        out.append(m.group(0))
        pos = m.end()
    out.append(text[pos:])
    new = ''.join(out)
    n += len(regex.findall(text[pos:])) * 0
    if n:
        report.append(f'    [{tag}] {n} 处')
    return new, n

# ---------------------------------------------------------------- 区段工具


def section_spans(raw: str):
    spans = []
    matches = list(SEC_RE.finditer(raw))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(raw)
        spans.append((m.group(1), m.start(), end))
    return spans


def extract_parts(span: str):
    h3 = H3_RE.search(span)
    intro = INTRO_RE.search(span)
    h4s = list(H4_RE.finditer(span))
    h5s = list(H5_RE.finditer(span))
    return h3, intro, h4s, h5s

# ---------------------------------------------------------------- 主流程


REPORT = []


def sidebar_title(raw: str, sid: str):
    m = SB_ANCHOR_RE(sid).search(raw)
    return plain(m.group(2)) if m else None


def source_section(src_raw: str, sid: str):
    for s, a, b in section_spans(src_raw):
        if s == sid:
            span = src_raw[a:b]
            h3, intro, h4s, h5s = extract_parts(span)
            if h3 is None:
                return None
            if classify(plain(h3.group(1))) not in ('title', 'supplement'):
                return None
            return {'h3': h3.group(1),
                    'intro': intro.group(1) if intro else None,
                    'h4': [m.group(1) for m in h4s],
                    'h5': [m.group(1) for m in h5s]}
    return None


def load_zh_reference(ver: str = 'v1.8'):
    """对应版本 zh 每节 h4 的编号值序列（v1.5/v1.6 书结构不同，须用各自基准）。"""
    base = ROOT / ver / 'zh-CN.html'
    if not base.exists():
        base = ROOT / 'v1.8' / 'zh-CN.html'
    ref = {}
    raw = base.read_text(encoding='utf-8')
    for sid, a, b in section_spans(raw):
        ref[sid] = [h4_number(x) for x in H4_RE.findall(raw[a:b])]
    return ref


ZH_REFS = {}


def restore_file(ver: str, lang: str, raw: str):
    """损坏回填（h3/导语/整组 h4/h5 + 逐槽 h4 修复）；返回 (新raw, 变更数)。"""
    if lang == 'zh-CN':
        return raw, 0                  # zh-CN 是基准，已单独修复
    if ver not in ZH_REFS:
        ZH_REFS[ver] = load_zh_reference(ver)
    zh_vals_all = ZH_REFS[ver]
    spans = section_spans(raw)
    edits = []          # (abs_start, abs_end, replacement, note)
    done_spans = []     # 第一层已占用的区段，第二层跳过
    for sid, a, b in spans:
        span = raw[a:b]
        h3, intro, h4s, h5s = extract_parts(span)
        if h3 is None:
            continue
        # ---- 第一层：h3 损坏 → 整体回填
        if classify(plain(h3.group(1))) not in ('title', 'supplement'):
            src = None
            chain = ('v1.6', 'v1.5', 'v1.8') if ver == 'v1.7' else ('v1.6', 'v1.5')
            for sv in chain:
                p = ROOT / sv / f'{lang}.html'
                if not p.exists():
                    continue
                cand = source_section(p.read_text(encoding='utf-8'), sid)
                if cand:
                    src = (sv, cand)
                    break
            ops = []
            if src:
                sv, c = src
                ops.append((h3.start(1), h3.end(1), c['h3'], f'h3←{sv}'))
                if intro and c['intro']:
                    ops.append((intro.start(1), intro.end(1), c['intro'], f'intro←{sv}'))
                if len(c['h4']) == len(h4s):
                    for m, txt in zip(h4s, c['h4']):
                        ops.append((m.start(1), m.end(1), txt, f'h4←{sv}'))
                if len(c['h5']) == len(h5s):
                    for m, txt in zip(h5s, c['h5']):
                        ops.append((m.start(1), m.end(1), txt, f'h5←{sv}'))
            else:
                sbt = sidebar_title(raw, sid)
                if sbt:
                    ops.append((h3.start(1), h3.end(1), sbt, 'h3←sidebar'))
                    REPORT.append(f'    [!] {ver}/{lang} {sid}: 无旧版来源，h3 用侧栏标题兜底')
                else:
                    REPORT.append(f'    [!!] {ver}/{lang} {sid}: 无来源且无侧栏标题，跳过')
            for s0, e0, txt, note in ops:
                edits.append((a + s0, a + e0, txt))
                done_spans.append((a + s0, a + e0))
                REPORT.append(f'    [回填] {ver}/{lang} {sid}: {note} → {plain(txt)[:46]}')
        # ---- 第二层：h4 逐槽校验（编号值须与 zh 同位置一致）
        zh_vals = zh_vals_all.get(sid)
        if zh_vals is None:
            continue
        h4s2 = list(H4_RE.finditer(raw[a:b]))
        # 整节无任何编号（该语言此节本就无编号风格）→ 不做逐槽修复
        if not any(h4_number(m.group(1)) is not None for m in h4s2):
            continue
        src_lists = []
        if any(h4_number(m.group(1)) != (zh_vals[k] if k < len(zh_vals) else None)
               for k, m in enumerate(h4s2)):
            chain = ('v1.6', 'v1.5', 'v1.8') if ver == 'v1.7' else ('v1.6', 'v1.5')
            for sv in chain:
                p = ROOT / sv / f'{lang}.html'
                if p.exists():
                    cand = source_section(p.read_text(encoding='utf-8'), sid)
                    if cand:
                        src_lists.append((sv, cand['h4']))
        # 语言版在节首多出编号 0 的导语节时，后续槽位整体左移一档
        shift0 = 0
        if (h4s2 and zh_vals and h4_number(h4s2[0].group(1)) == 0
                and zh_vals[0] == 1):
            shift0 = 1
        for k, m in enumerate(h4s2):
            if any(s0 <= a + m.start() < e0 for s0, e0 in done_spans):
                continue
            ov = (V_OVERRIDES.get((ver, lang, sid, k))
                  or OVERRIDES.get((lang, sid, k)))
            if ov is not None:
                edits.append((a + m.start(1), a + m.end(1), ov, 'override'))
                REPORT.append(f'    [译填] {ver}/{lang} {sid} h4[{k}]: {plain(ov)[:44]}')
                continue
            # zh 源稿曾存在的"空壳重复标题"：按位置删除（仅当确实无正文）
            if (sid, k) in DUP_DELETE:
                if not _h4_has_body(raw, a, m, H4_RE):
                    edits.append((a + m.start(), a + m.end(), '', '空壳标题删除'))
                    REPORT.append(f'    [删空壳] {ver}/{lang} {sid} h4[{k}]: {plain(m.group(1))[:36]}')
                    continue
            # zh 修复时的顺号：该槽编号需 +1
            if (sid, k) in DUP_RENUM:
                val0 = h4_number(m.group(1))
                if val0 is not None:
                    edits.append((a + m.start(1), a + m.end(1),
                                  bump_number(m.group(1), val0 + 1), '顺号 +1'))
                    REPORT.append(f'    [顺号] {ver}/{lang} {sid} h4[{k}]: {plain(m.group(1))[:34]} → {val0+1}')
                    continue
            val = h4_number(m.group(1))
            eff = k - shift0 - sum(1 for dk in DUP_DELETE_BY_SID.get(sid, ()) if dk < k)
            zv = zh_vals[eff] if eff < len(zh_vals) else None
            if zv is None:
                continue                      # zh 此槽本身无编号（参考文献等）
            if val is not None and (val == zv or val == k + 1 or val == 0):
                continue
            if (val is not None and val == zv + 1 and ver in ('v1.5', 'v1.6', 'v1.7')):
                continue          # 旧版允许"合并一节后顺延"的编号风格
            if k >= len(zh_vals):
                # zh 没有的多余 h4 且编号不符 → 降为段落
                edits.append((a + m.start(), a + m.end(),
                              '<p class="mb-2">' + m.group(1) + '</p>',
                              f'h4[{k}] 多余且损坏 → 段落'))
                REPORT.append(f'    [降级] {ver}/{lang} {sid} h4[{k}]: {plain(m.group(1))[:40]}')
                continue
            if sid == 'di-san-zhang' and k in (5, 6) and val == 5 and zv == 6:
                edits.append((a + m.start(1), a + m.end(1),
                              bump_number(m.group(1), 6), 'ch3 5→6'))
                REPORT.append(f'    [改号] {ver}/{lang} {sid} h4[{k}]: {plain(m.group(1))[:36]} → 6')
                continue
            hit = None
            for sv, lst in src_lists:
                if k < len(lst) and h4_number(lst[k]) == zv:
                    hit = (sv, lst[k])
                    break
            if hit:
                edits.append((a + m.start(1), a + m.end(1), hit[1],
                              f'h4[{k}]←{hit[0]}'))
                REPORT.append(f'    [槽修复] {ver}/{lang} {sid} h4[{k}]: '
                              f'{plain(m.group(1))[:30]} → {plain(hit[1])[:40]}')
            else:
                REPORT.append(f'    [待手修] {ver}/{lang} {sid} h4[{k}]: {plain(m.group(1))[:44]}')
    # 泄漏的占位标题 IGNORED（zh 源稿 bug，已同步到全部语言）→ 直接删除
    for m in re.finditer(r'<h4 class="text-lg font-semibold (?:mt-4|mt-6) mb-2">\s*IGNORED\s*</h4>', raw):
        edits.append((m.start(), m.end(), '', 'IGNORED 占位标题删除'))
        REPORT.append(f'    [删除] {ver}/{lang}: IGNORED 占位 h4')
    if not edits:
        return raw, 0
    edits.sort(key=lambda t: (t[0], t[1]))
    out, pos = [], 0
    for s0, e0, txt, *_ in edits:
        out.append(raw[pos:s0]); out.append(txt); pos = e0
    out.append(raw[pos:])
    return ''.join(out), len(edits)


def style_file(ver: str, lang: str, raw: str):
    """编号风格统一；返回 (新raw, 变更数)。"""
    n_total = 0
    # ja：v1.6+ 统一为汉字数字（对齐中文源稿与 v1.8 侧栏）；v1.5 保持其原本一致的数字风格
    if lang == 'ja':
        if ver == 'v1.5':
            REPORT.append(f'    [ja] {ver}/{lang}: 数字风格一致，保持不动')
        else:
            pat = re.compile(r'第\s*([0-9]{1,2})\s*章')
            raw, n = protected_sub(raw, pat, lambda m: f'第{CJK_OF_DIGIT[m.group(1)]}章',
                                   REPORT, 'ja 数字→汉字')
            n_total += n
    elif lang in WORD_PATTERNS:
        pat, repl = WORD_PATTERNS[lang]
        raw, n = protected_sub(raw, pat, repl, REPORT, '词形→数字')
        n_total += n
    if lang in SUPPL_RE:
        # h3 标题（只计真实变更）
        n = 0
        def sup_repl_h3(m):
            nonlocal n
            t = m.group(1)
            t2 = t
            for pat, r in SUPPL_RE[lang]:
                t2 = pat.sub(r, t2)
            if t2 != t:
                n += 1
                return m.group(0).replace(m.group(1), t2)
            return m.group(0)
        new, pos, out = [], 0, []
        for m in PROTECT_RE.finditer(raw):
            seg = raw[pos:m.start()]
            out.append(H3_RE.sub(sup_repl_h3, seg))
            out.append(m.group(0)); pos = m.end()
        out.append(raw[pos:])
        raw = ''.join(out)
        if n:
            REPORT.append(f'    [章附统一] {ver}/{lang}: {n} 处 h3')
        n_total += n
        # 侧栏标题
        n_sb = 0
        for sid, a, b in section_spans(raw):
            am = SB_ANCHOR_RE(sid).search(raw)
            if not am:
                continue
            t = am.group(2)
            t2 = t
            for pat, r in SUPPL_RE[lang]:
                t2 = pat.sub(r, t2)
            for pf, r in PUNCT_FIX.get(lang, []):
                t2 = pf.sub(r, t2)
            if t2 != t:
                raw = raw[:am.start(2)] + t2 + raw[am.end(2):]
                n_sb += 1
        if n_sb:
            REPORT.append(f'    [章附统一] {ver}/{lang}: {n_sb} 处侧栏')
        n_total += n_sb
    if lang in PUNCT_FIX:
        for pat, r in PUNCT_FIX[lang]:
            raw, k = protected_sub(raw, pat, r, REPORT, f'{lang} 标点')
            n_total += k
    if lang == 'ko':
        # 裸编号 h3/侧栏（"0장:" → "제0장:"），仅标题位置
        n_ko = 0

        def ko_bare(m):
            nonlocal n_ko
            t = m.group(1)
            t2 = re.sub(r'^([0-9]{1,2})장', r'제\1장', t)
            if t2 != t:
                n_ko += 1
                return m.group(0).replace(m.group(1), t2)
            return m.group(0)

        out, pos, segs = [], 0, []
        for mm in PROTECT_RE.finditer(raw):
            seg = raw[pos:mm.start()]
            segs.append(H3_RE.sub(ko_bare, seg))
            segs.append(mm.group(0))
            pos = mm.end()
        segs.append(raw[pos:])
        raw = ''.join(segs)
        for sid, a, b in section_spans(raw):
            am = SB_ANCHOR_RE(sid).search(raw)
            if am:
                t2 = re.sub(r'^([0-9]{1,2})장', r'제\1장', am.group(2))
                if t2 != am.group(2):
                    raw = raw[:am.start(2)] + t2 + raw[am.end(2):]
                    n_ko += 1
        if n_ko:
            REPORT.append(f'    [ko 编号] {ver}/{lang}: {n_ko} 处补 제')
        n_total += n_ko
    return raw, n_total


def verify(ver: str, lang: str, raw_old: str, raw_new: str):
    ok = True
    for tag, raw in (('旧', raw_old), ('新', raw_new)):
        spans = section_spans(raw)
        bad = []
        for sid, a, b in spans:
            m = H3_RE.search(raw[a:b])
            cls = classify(plain(m.group(1))) if m else 'empty'
            if cls in ('other', 'empty'):
                bad.append(sid)
        if tag == '新' and bad:
            ok = False
            REPORT.append(f'    [校验] {ver}/{lang}: 仍损坏 {bad}')
        if tag == '旧':
            REPORT.append(f'    [校验] {ver}/{lang}: 旧损坏={len(bad)}')
    # 结构守恒：节数/h4 总数/h5 总数
    for name, raw in (('旧', raw_old), ('新', raw_new)):
        spans = section_spans(raw)
        n4 = sum(len(H4_RE.findall(raw[a:b])) for _, a, b in spans)
        n5 = sum(len(H5_RE.findall(raw[a:b])) for _, a, b in spans)
        if name == '旧':
            base = (len(spans), n4, n5)
        else:
            if (len(spans), n4, n5) != base:
                # h4 多余槽降级为段落属预期修复，只提示不判失败
                REPORT.append(f'    [结构] {ver}/{lang}: {base} → {(len(spans), n4, n5)}'
                              f'（h4 降级属预期）')
    # 新文件中残留可疑的 h4/h5（句号结尾或超长），供人工复核
    raw = raw_new
    bad_h = []
    for sid, a, b in section_spans(raw):
        span = raw[a:b]
        for m in H4_RE.finditer(span):
            t = plain(m.group(1))
            if len(t) > 40 or re.search(r'[。！？]$', t):
                bad_h.append(('h4', sid, t[:36]))
        for m in H5_RE.finditer(span):
            t = plain(m.group(1))
            if len(t) > 40 or re.search(r'[。！？]$', t):
                bad_h.append(('h5', sid, t[:36]))
    if bad_h:
        REPORT.append(f'    [复核] {ver}/{lang}: 可疑 h4/h5 {len(bad_h)} 个:')
        for lv, sid, t in bad_h[:12]:
            REPORT.append(f'        {lv} {sid}: {t}')
    return ok


def main():
    total_files = 0
    for ver in VERSIONS:
        base = ROOT / ver
        for p in sorted(base.glob('*.html')):
            lang = p.stem
            if lang == 'index':
                continue
            if ver == 'v1.7' and lang == 'lzh':
                REPORT.append(f'-- 跳过 {p}（已知 NUL 损坏）')
                continue
            raw = p.read_text(encoding='utf-8')
            REPORT.append(f'== {ver}/{lang}.html')
            new, n1 = restore_file(ver, lang, raw)
            new, n2 = style_file(ver, lang, new)
            good = verify(ver, lang, raw, new)
            if (n1 or n2) and good and APPLY:
                p.write_text(new, encoding='utf-8', newline='')
                REPORT.append(f'    → 已写盘 (+{n1} 回填, +{n2} 风格)')
            elif n1 or n2:
                REPORT.append(f'    → 干跑 (+{n1} 回填, +{n2} 风格) 校验{"通过" if good else "失败"}')
            total_files += 1
    print(f'文件数: {total_files}; APPLY={APPLY}')
    print('\n'.join(REPORT))


if __name__ == '__main__':
    main()
