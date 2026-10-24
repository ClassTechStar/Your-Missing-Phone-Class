# -*- coding: utf-8 -*-
"""校验各语言 PDF 的 main.toc：章节行编号必须同风格。"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STYLE = {
    'zh-CN': (r'^第[零〇一二三四五六七八九十百]+章', '第N章 汉字数字'),
    'zh-TW': (r'^第[零〇一二三四五六七八九十百]+章', '第N章 汉字数字'),
    'yue':   (r'^第[零〇一二三四五六七八九十百]+章', '第N章 汉字数字'),
    'lzh':   (r'^第[零〇一二三四五六七八九十百]+章', '第N章 汉字数字'),
    'ja':    (r'^第[零〇一二三四五六七八九十百]+章', '第N章 汉字数字'),
    'ko':    (r'^제\s*[0-9]+장', '제N장 数字'),
    'en':    (r'^Chapter\s+[0-9]+', 'Chapter N'),
    'ru':    (r'^Глава\s+[0-9]+', 'Глава N'),
    'de':    (r'^Kapitel\s+[0-9]+', 'Kapitel N'),
    'el':    (r'^Κεφάλαιο\s+[0-9]+', 'Κεφάλαιο N'),
    'it':    (r'^Capitolo\s+[0-9]+', 'Capitolo N'),
    'pt':    (r'^Cap[íi]tulo\s+[0-9]+', 'Capítulo N'),
    'es':    (r'^Cap[íi]tulo\s+[0-9]+', 'Capítulo N'),
    'fr':    (r'^Chapitre\s+[0-9]+', 'Chapitre N'),
    'ar':    (r'^الفصل\s+[0-9]', 'الفصل N'),
    'he':    (r'^פרק\s+[0-9]+', 'פרק N'),
    'th':    (r'^บทที่\s*[0-9]+', 'บทที่ N'),
    'id':    (r'^Bab\s+[0-9]+', 'Bab N'),
    'ms':    (r'^Bab\s+[0-9]+', 'Bab N'),
}

def main():
    langs = sys.argv[1:] or list(STYLE)
    for lang in langs:
        base = ROOT / 'latex' / ('' if lang == 'zh-CN' else lang)
        toc = base / 'main.toc'
        if not toc.exists():
            print(f'{lang}: main.toc 不存在')
            continue
        pat, name = STYLE[lang]
        chapters, odd = [], []
        for line in toc.read_text(encoding='utf-8').splitlines():
            m = re.search(r'\\contentsline \{chapter\}\{(.+?)\}\{[0-9]+\}', line)
            if not m:
                continue
            t = re.sub(r'\\[a-zA-Z]+ ?', '', m.group(1)).strip()
            chapters.append(t)
            if not (re.match(pat, t) or re.match(r'^(付録|付錄|附录|附|Anhang|Appendix|Appendice|'
                                                 r'Annexe|Ap[áàâãéêe]ndice|Appendice|Anexo|Приложение|נספח|الملحق|ملحق|'
                                                 r'ภาคผนวก|Lampiran|Παράρτημα|Παράρτη|부록|Epilog|Epilogue|'
                                                 r'Conclusion|Conclusão|Ep[íi]logo|おわりに|맺음말|'
                                                 r'Επίλογος|Заключение|סיום|דברי סיכום|خاتمة|'
                                                 r'บทส่งท้าย|Penutup|Nachwort|结语|結語|参考文献)', t)):
                odd.append(t)
        print(f'{lang}: 章级目录 {len(chapters)} 条，风格[{name}]，离群 {len(odd)}')
        for t in odd[:8]:
            print(f'    [离群] {t[:60]}')

if __name__ == '__main__':
    main()
