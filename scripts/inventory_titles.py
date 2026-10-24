"""全量清单：各版本/语言 84 个 content-section 的 h3 标题分类与 h4 计数。

分类：title（章前缀正常）/ supplement（附/附录类前缀）/ other（疑似损坏）。
输出每文件的 (ok, supplement, corrupt) 计数与 corrupt 明细。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from bookkit import htmlparse as H  # noqa: E402

NUM = r'(?:[0-9０-９]+|[零〇一二三四五六七八九十百两]+|[0-9]+)'
CH = [
    r'第\s*%s\s*章' % NUM,                       # zh/ja/yue/lzh/zh-TW
    r'第\s*%s\s*回' % NUM,
    r'제\s*(?:[0-9]+|[영일이삼사오육칠팔구십백]+)\s*장',  # ko
    r'Chapter\s+(?:[0-9]+|Zero|One|Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten|Eleven|Twelve|Twenty|Thirty|[A-Z][a-z]+)',  # en
    r'Глава\s+[0-9]+',                            # ru
    r'Capitolo\s+[0-9]+',                         # it
    r'Cap[íi]tulo\s+[0-9]+',                      # pt/es
    r'Chapitre\s+(?:[0-9]+|zéro|un|deux|trois|quatre|cinq|six|sept|huit|neuf|dix)',  # fr
    r'Kapitel\s+[0-9]+',                          # de
    r'الفصل\s+(?:[0-9٠-٩]+|الأول|الثاني|الثالث|الرابع|الخامس|السادس|السابع|الثامن|التاسع|العاشر)',  # ar
    r'פרק\s+(?:[0-9]+|[אבגדהוזחטימש]+)',          # he
    r'บทที่\s*[0-9]+',                            # th
    r'Bab\s+[0-9]+',                              # id/ms
    r'Κεφάλαιο\s+(?:[0-9]+|Μηδέν|Ένα|Δύο|Τρία|Τέσσερα|Πέντε|Έξι|Επτά|Οκτώ|Εννέα|Δέκα)',  # el
    r'Chương\s+[0-9]+',                           # vi
]
SUP = [
    r'^(第\s*%s\s*章)?\s*(附|附錄|附録|付録|附录)' % NUM,
    r'^(Chapter|Kapitel|Capitolo|Cap[íi]tulo|Chapitre|Глава)\s*[0-9]?\s*(Appendix|Appendice|Anhang|Annexe|Ap[áàâãéêe]ndice|Anexo|Приложение|Supplement|Ergänzung)',
    r'^(Appendix|Appendice|Anhang|Annexe|Ap[áàâãéêe]ndice|Anexo|Приложение|נספח|الملحق|ملحق|ภาคผนวก|'
    r'Lampiran|Tambahan|Παράρτημα|부록|Phụ lục|App\.|附錄|付録|附录|Anexo)',
    r'^(Epilog|Epilogue|Conclusion|Conclusão|Ep[íi]logo|おわりに|맺음말|Επίλογος|'
    r'דברי סיכום|Заключение|Kết luận)',
    r'^(Epilog|Epilogue|Conclusion|Ep[íi]logo|結び|에필로그|Επίλογος|خاتمة|סיום|บทส่งท้าย|Penutup|Nachwort|结语|結語|后记|後記)',
    r'^(الخاتمة|الملحق)',
]
RE_CH = re.compile(r'^(?:%s)' % '|'.join(CH))
RE_SUP = re.compile(r'^(?:%s)' % '|'.join(SUP))

def classify(t: str) -> str:
    if not t:
        return 'empty'
    if RE_SUP.match(t):
        return 'supplement'
    if RE_CH.match(t):
        return 'title'
    return 'other'

def inventory(path: Path):
    html = path.read_text(encoding='utf-8')
    tree = H.parse(html)
    rows = []
    for n in tree.find_all('div'):
        if 'content-section' not in n.classes:
            continue
        h3 = n.find('h3')
        t = re.sub(r'\s+', ' ', h3.text()).strip() if h3 is not None else ''
        h4s = [re.sub(r'\s+', ' ', h.text()).strip() for h in n.find_all('h4')]
        rows.append((n.get('id'), t, classify(t), h4s))
    return rows

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    vers = args if args else ['v1.8']
    detail = '--detail' in sys.argv
    for v in vers:
        base = ROOT / v if not v.startswith('archive') else ROOT / v
        files = sorted(base.glob('*.html')) if (ROOT / v).is_dir() else []
        for p in files:
            if p.stem == 'index':
                continue
            rows = inventory(p)
            bad = [r for r in rows if r[2] in ('other', 'empty')]
            n_sup = sum(1 for r in rows if r[2] == 'supplement')
            print(f'{v}/{p.name}: {len(rows)} 节 | title={len(rows)-len(bad)-n_sup} supplement={n_sup} corrupt={len(bad)}')
            if detail:
                for sid, t, c, h4s in bad:
                    print(f'   [{c}] {sid}: {t[:60]}')

if __name__ == '__main__':
    main()
