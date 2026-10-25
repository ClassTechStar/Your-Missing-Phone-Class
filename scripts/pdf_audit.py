# -*- coding: utf-8 -*-
"""全量 PDF 质量审计：书签顺序/风格、页码单调、正文异常、与最新 HTML 的时效性。

用法：python scripts/pdf_audit.py [--json out.json] [版本目录...]
默认审计 手机课-LaTeX-PDF/pdf 下全部版本。
"""
import io
import json
import re
import sys
from pathlib import Path

import unicodedata

import pymupdf

PDFROOT = Path('C:/Users/18948/Documents/手机课-LaTeX-PDF/pdf')

# 章级（outline level-2）前缀与"数字风格"判定；ja/zh 系应为汉字数字，其余为阿拉伯数字
CJK_NUM = r'[零〇一二三四五六七八九十百]+'
CH_PAT = {
    'ja':    (r'^第(%s)章' % CJK_NUM, r'^第[0-9]+章', '第N章 汉字'),   # v1.5 ja 例外：保持数字（audit 时特判）
    'zh-CN': (r'^第(%s)章' % CJK_NUM, r'^第[0-9]+章', '第N章 汉字'),
    'zh-TW': (r'^第(%s)章' % CJK_NUM, r'^第[0-9]+章', '第N章 汉字'),
    'yue':   (r'^第(%s)章' % CJK_NUM, r'^第[0-9]+章', '第N章 汉字'),
    'lzh':   (r'^第(%s)章' % CJK_NUM, r'^第[0-9]+章', '第N章 汉字'),
    'ko':    (r'^제\s*([0-9]+)장', r'^제\s*[영일이삼사오육칠팔구십백]+장', '제N장 数字'),
    'en':    (r'^Chapter\s+([0-9]+)', r'^Chapter\s+[A-Za-z]', 'Chapter N'),
    'ru':    (r'^Глава\s+([0-9]+)', r'^Глава\s+[а-яё]', 'Глава N'),
    'de':    (r'^Kapitel\s+([0-9]+)', r'^Kapitel\s+[A-ZÄÖÜ]', 'Kapitel N'),
    'el':    (r'^Κεφάλαιο\s+([0-9]+)', r'^Κεφάλαιο\s+[Α-Ωα-ω]', 'Κεφάλαιο N'),
    'it':    (r'^Capitolo\s+([0-9]+)', r'^Capitolo\s+[A-Za-z]', 'Capitolo N'),
    'pt':    (r'^Cap[íi]tulo\s+([0-9]+)', r'^Cap[íi]tulo\s+[A-Za-zÀ-ÿ]', 'Capítulo N'),
    'es':    (r'^Cap[íi]tulo\s+([0-9]+)', r'^Cap[íi]tulo\s+[A-Za-zÁÉÍÓÚá-ÿ]', 'Capítulo N'),
    'fr':    (r'^Chapitre\s+([0-9]+)', r'^Chapitre\s+[a-zà-ÿ]', 'Chapitre N'),
    'ar':    (r'^الفصل\s+([0-9٠-٩]+)', r'^الفصل\s+[أ-ي]', 'الفصل N'),
    'he':    (r'^פרק\s+([0-9]+)', r'^פרק\s+[א-ת]', 'פרק N'),
    'th':    (r'^บทที่\s*([0-9]+)', r'^บทที่\s*[ก-๙]', 'บทที่ N'),
    'id':    (r'^Bab\s+([0-9]+)', r'^Bab\s+[A-Za-z]', 'Bab N'),
    'vi':    (r'^Chương\s+([0-9]+)', r'^Chương\s+[A-Za-zÀ-ÿ]', 'Chương N'),
    'ms':    (r'^Bab\s+([0-9]+)', r'^Bab\s+[A-Za-z]', 'Bab N'),
}
SUP_PAT = (r'^(付録|付錄|附録|附录|附錄|附|Anhang|Appendix|Appendice|Annexe|Ap[éêe]ndice|Anexo|'
           r'Приложени|приложение|נספח|ملحق|ภาคผนวก|Lampiran|Tambahan|Παράρτημα|부록|Phụ lục)')

# 过期标记：PDF 若含 old（修复前）文本 → 快照过期；new 应存在
STALE = {
    'ja':    [(r'第\s*[0-9]+\s*章', '旧数字章号'), (r'第四章：アプリのインストールと管理', None)],
    'ru':    [(r'[Гг]лава\s+(перв|втор|трет|четвёрт|пят|шест|седьм|восьм|девят|десят|одиннадцат|двенадцат|тринадцат|четырнадцат|пятнадцат|шестнадцат|семнадцат|восемнадцат|двадцат|тридцат|сороков|пятидесят|шестидесят)[а-яё]*\b', '词形章号')],
    'he':    [(r'פרק\s+(שני|שלישי|רביעי|חמישי|שישי)\b', '词形章号')],
    'ar':    [(r'الفصل\s+(الثاني|الثالث|الرابع|الخامس|السادس|السابع)\s*:', '词形章号')],
    'fr':    [(r'Chapitre\s+(zéro|un|deux|cinq)\b', '词形章号')],
    'pt':    [(r'Cap[íi]tulo\s+(Zero|Um|Dois|Vinte|Trinta)\b', '词形章号')],
    'en':    [(r'Chapter\s+Zero\b', '词形章号')],
    'el':    [(r'[α-ωάέήίόύώ]{2,}και(?=[\s,.])', 'και 粘连')],
    'es':    [],   # es 附录C错标D 的判定改为下方专用逻辑（需出现≥2次才算过期）
    'zh-CN': [(r'五、个人热点：把手机变Wi-?Fi路由器', 'ch3 旧五号'), (r'IGNORED', '占位标题')],
}

def chapter_value(lang, title):
    """章标题 → 编号数值；附录用 100+序号。"""
    ok, bad, _ = CH_PAT.get(lang, (None, None, None))
    if ok:
        m = re.match(ok, title)
        if m:
            g = m.group(1)
            if lang in ('ja', 'zh-CN', 'zh-TW', 'yue', 'lzh'):
                table = {'零': 0, '〇': 0}
                for i, c in enumerate('一二三四五六七八九'):
                    table[c] = i + 1
                table['十'] = 10
                if g == '十':
                    return 10
                if len(g) == 2 and g[0] == '十':
                    return 10 + table.get(g[1], 0)
                if len(g) == 2 and g[1] == '十':
                    return table.get(g[0], 0) * 10
                if len(g) == 3 and g[1] == '十':
                    return table.get(g[0], 0) * 10 + table.get(g[2], 0)
                return table.get(g[0], None)
            if g.isdigit():
                return int(g)
            try:
                return int(g.translate({ord('٠') + i: str(i) for i in range(10)}))
            except ValueError:
                return None
    return None

def audit_pdf(path: Path, lang: str):
    doc = pymupdf.open(path)
    r = {'file': str(path), 'pages': doc.page_count, 'issues': [], 'warn': []}
    toc = doc.get_toc()
    r['outline'] = len(toc)
    # ---- 章级顺序/风格 ----
    chs = [(unicodedata.normalize('NFC', t[1]), t[2]) for t in toc if t[0] == 2]
    ok, bad, name = CH_PAT.get(lang, (None, None, '?'))
    if lang == 'ja' and path.parent.name == 'v1.5':
        ok, bad, name = bad, ok, '第N章 数字（v1.5 约定）'
    n_style = n_badstyle = 0
    vals, pages_seq = [], []

    def is_sup(title):
        # 章内附（Kapitel 1 Anhang / 第一章付録 / Chapter 11 Appendix /
        # Capítulo 11 - Apêndice / Глава 1 (дополнение) / Κεφάλαιο 1 Συνημμένο / Chương 11 phụ…）
        t = unicodedata.normalize('NFC', title)
        return bool(re.match(SUP_PAT, t)
                    or re.search(r'(Anhang|Appendix|Appendice|Annexe|Ap[éêe]ndice|Anexo|'
                                 r'Приложени|дополнени|נספח|ملحق|ภาคผนวก|Lampiran|Tambahan|'
                                 r'Παράρτημα|Συνημμέν|부록|Phụ lục|phụ|付録|付錄|附録|附录|附錄|附[:：]?)', t))

    for title, pg in chs:
        if is_sup(title):
            continue
        if ok and re.match(ok, title):
            n_style += 1
            vals.append(chapter_value(lang, title))
            pages_seq.append(pg)
        elif ok and re.match(bad, title):
            n_badstyle += 1
            vals.append(None)
    r['chapters'] = n_style + n_badstyle
    if n_badstyle:
        r['issues'].append(f'章编号风格混用：规范 {n_style} 条 / 异风格 {n_badstyle} 条（期望全部 {name}）')
    good_vals = [v for v in vals if v is not None]
    desc = [a for a, b in zip(good_vals, good_vals[1:]) if b <= a]
    # v1.6/ru 出版时即缺第4、13章（见 README 已知问题），跳号属内容缺章
    if desc and (lang, path.parent.name) != ('ru', 'v1.6'):
        r['issues'].append(f'章号非严格递增 {len(desc)} 处（如 {good_vals[:12]}）')
    if pages_seq != sorted(pages_seq):
        r['issues'].append('章起始页码非单调递增（目录顺序错乱）')
    # 附录字母顺序（拉丁字母 A–H；ja/zh 系附录也带拉丁字母）
    sup_head = (r'^(?:付録|付錄|附録|附录|附錄|Anhang|Appendix|Appendice|Annexe|Ap[éêe]ndice|'
                r'Anexo|Приложение|נספח|ملحق|ภาคผนวก|Lampiran|Tambahan|Παράρτημα|부록|Phụ lục)'
                r'[\s:：]*([A-H])\b')
    aps = [m2.group(1) for t, _ in chs if is_sup(t)
           for m2 in [re.search(sup_head, unicodedata.normalize('NFC', t))] if m2]
    if aps and aps != sorted(aps):
        r['issues'].append(f'附录字母顺序错乱：{aps}')
    r['appendices'] = len(aps)
    # ---- 正文扫描 ----
    n_fffd = n_empty = n_vert = 0
    empty_pages, vert_pages = [], []
    for i, page in enumerate(doc):
        txt = page.get_text('text')
        if '\ufffd' in txt:
            n_fffd += txt.count('\ufffd')
        body = txt.strip()
        if len(body) < 8:
            n_empty += 1
            empty_pages.append(i + 1)
            continue
        lines = [l.strip() for l in txt.splitlines() if l.strip()]
        one = sum(1 for l in lines if len(l) == 1)
        if one > 30 and one > len(lines) * 0.5:   # 表格列名不算
            n_vert += 1
            vert_pages.append(i + 1)
    if n_fffd:
        r['issues'].append(f'替换字符 U+FFFD ×{n_fffd}')
    if n_empty > 15:
        r['warn'].append(f'近空白页 {n_empty} 页（如 {empty_pages[:6]}）')
    if n_vert:
        r['issues'].append(f'疑似竖排/单字成行页 {n_vert} 页（如 {vert_pages[:6]}）')
    # ---- 过期标记（正文全文本）----
    full = '\n'.join(doc[i].get_text('text') for i in range(min(doc.page_count, 60)))
    full += '\n' + '\n'.join(doc[i].get_text('text')
                             for i in range(0, doc.page_count, 7))   # 抽样正文
    stale = [] if (lang == 'ja' and path.parent.name == 'v1.5') else STALE.get(lang, [])
    for pat, label in stale:
        n = len(re.findall(pat, full))
        if n and label:
            r['issues'].append(f'过期标记[{label}] ×{n}')
    if lang == 'es':
        n = len(re.findall(r'Ap[éêe]ndice D: D[óo]nde encontrar recursos', full))
        if n >= 2:
            r['issues'].append(f'过期标记[附录C错标D] ×{n}（≥2 即重复）')
    # 元数据
    r['meta_title'] = doc.metadata.get('title', '')[:60]
    return r

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    json_out = None
    if '--json' in sys.argv:
        json_out = sys.argv[sys.argv.index('--json') + 1]
    vers = args or ['v1.8']
    report = {}
    for v in vers:
        d = PDFROOT / v
        if not d.is_dir():
            continue
        for p in sorted(d.glob('*.pdf')):
            lang = p.stem
            try:
                report[f'{v}/{lang}'] = audit_pdf(p, lang)
            except Exception as e:
                report[f'{v}/{lang}'] = {'file': str(p), 'issues': [f'解析失败: {e}']}
    # 汇总打印
    n_bad = 0
    for k, r in sorted(report.items()):
        flag = '✗' if r.get('issues') else '✓'
        print(f'{flag} {k}: {r.get("pages","?")}页 目录{r.get("outline",0)}条 章{r.get("chapters","?")} 附录{r.get("appendices","?")}')
        for i in r.get('issues', []):
            n_bad += 1
            print(f'    [问题] {i}')
        for w in r.get('warn', []):
            print(f'    [提示] {w}')
    print(f'\n== {len(report)} 个 PDF，含问题文件 {sum(1 for r in report.values() if r.get("issues"))} 个，问题条目 {n_bad} 条')
    if json_out:
        Path(json_out).write_text(json.dumps(report, ensure_ascii=False, indent=1),
                                  encoding='utf-8')

if __name__ == '__main__':
    main()
