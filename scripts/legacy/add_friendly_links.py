#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""在 v1.8（19 语源稿）与 v1.9（单文件 HTML）的附录 D 加入两个友情链接。

两个链接（均已实测 200 可达）：
  1. 《你缺失的那门计算机课》 https://www.criwits.top/missing/
  2. 计算机教育中缺失的那一课 / The Missing Semester of Your CS Education
     https://missing.csail.mit.edu/

字形约束（bookkit lint 的 residual 规则）：非中文语言不得出现汉字，
中文繁体/粤语/文言版不得残留简体字。因此
  - zh-CN / zh-TW / yue / lzh：书名用各自字形/文体；
  - 其余 15 语：条目名统一用英文描述（《你缺失的那门计算机课》没有官方英文名，
    不擅自编造译名），第二个用 MIT 官方英名。
两个链接的 URL 在所有语言中都保留。

v1.8 走源稿：改 md → bookkit build 重建 19 语（保持 build --verify 一致）。
v1.9 无源稿体系，直接改两个互为副本的 HTML（中文，保留原书名）。

用法：
    python scripts/add_friendly_links.py            # 干跑
    python scripts/add_friendly_links.py --apply    # 写盘（含剥离旧小节再重加）
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

U1 = 'https://www.criwits.top/missing/'
U2 = 'https://missing.csail.mit.edu/'
A_CLS = 'class="text-primary hover:underline" target="_blank" rel="noopener"'

T1_EN = 'An open-source Chinese primer on computing'
T2_EN = 'The Missing Semester of Your CS Education (MIT)'

# lang -> (小节标题, 说明1, 说明2, 条目名1, 条目名2)
TEXT = {
    'zh-CN': ('友情链接 · 两门同样「缺失」的课',
              '中文开源计算机通识读本，本书的理念正是从它长出来的。',
              'MIT 的免费课，补的是 shell、Git、命令行这些学校不教、日常却天天要用的东西。',
              '《你缺失的那门计算机课》',
              '计算机教育中缺失的那一课（The Missing Semester of Your CS Education · MIT）'),
    'zh-TW': ('友情連結 · 兩門同樣「缺失」的課',
              '中文開源計算機通識讀本，本書的理念正是從它長出來的。',
              'MIT 開的免費課，補的是 shell、Git、命令列這些學校不教、日常卻天天要用的東西。',
              '《你缺失的那門計算機課》',
              '電腦教育中缺失的那一課（The Missing Semester of Your CS Education · MIT）'),
    'yue':   ('友情連結 · 兩堂同樣「缺失」嘅課',
              '中文開源電腦通識讀本，呢本書嘅理念正係由佢度生出嚟。',
              'MIT 嘅免費課，補嘅係 shell、Git、命令列呢啲學校唔教、但日日都要用嘅嘢。',
              '《你缺失嗰門電腦課》',
              '電腦教育中缺咗嗰課（The Missing Semester of Your CS Education · MIT）'),
    'lzh':   ('友誼之鏈 · 二課亦闕',
              '華文開源算學通識之書，此編之義，實自彼而生。',
              '麻省理工之免費課，補 shell、Git、命令行之學，庠序不授而日用不離者也。',
              '《爾所闕之算學課》',
              '算學教育所闕之一課（The Missing Semester of Your CS Education · MIT）'),
    'en':    ('Friendly Links · Two Other "Missing" Courses',
              'An open-source Chinese introduction to computing; the idea for this book grew out of it.',
              'A free MIT course on the shell, Git and the command line — things school rarely teaches but you use every day.',
              T1_EN, T2_EN),
    'ko':    ('추천 링크 · 또 다른 두 개의 "빠진" 수업',
              '중국어 오픈소스 컴퓨터 교양서로, 이 책의 아이디어가 여기서 나왔습니다.',
              'MIT의 무료 강의. 학교에서 잘 가르치지 않지만 매일 쓰는 셸·Git·명령줄을 다룹니다.',
              T1_EN, T2_EN),
    'ja':    ('関連リンク · もう二つの「足りない授業」',
              '中国語のオープンソース計算機入門。本書の構想はここから生まれました。',
              'MIT の無料講義。シェルや Git、コマンドラインなど、学校では教えないが毎日使うことを扱います。',
              T1_EN, T2_EN),
    'ru':    ('Полезные ссылки · Два других «пропущенных» курса',
              'Открытый китайский учебник по информатике — идея этой книги выросла из него.',
              'Бесплатный курс MIT о командной строке, shell и Git: в школе этому не учат, а без него не обходится ни один день.',
              T1_EN, T2_EN),
    'it':    ('Link utili · Altri due «corsi mancanti»',
              "Un'introduzione all'informatica open source in cinese: da qui è nata l'idea di questo libro.",
              'Un corso gratuito del MIT su shell, Git e riga di comando — cose che a scuola non si insegnano ma si usano ogni giorno.',
              T1_EN, T2_EN),
    'pt':    ('Links recomendados · Outros dois "cursos que faltavam"',
              'Uma introdução aberta à computação em chinês: a ideia deste livro nasceu dela.',
              'Um curso gratuito do MIT sobre shell, Git e linha de comando — o que a escola não ensina, mas você usa todo dia.',
              T1_EN, T2_EN),
    'es':    ('Enlaces recomendados · Otros dos "cursos que faltaban"',
              'Una introducción abierta a la informática en chino: de ahí nació la idea de este libro.',
              'Un curso gratuito del MIT sobre la terminal, Git y la línea de comandos: cosas que no se enseñan en la escuela pero se usan a diario.',
              T1_EN, T2_EN),
    'fr':    ('Liens utiles · Deux autres « cours manquants »',
              "Une introduction libre à l'informatique en chinois : c'est d'elle qu'est née l'idée de ce livre.",
              "Un cours gratuit du MIT sur le shell, Git et la ligne de commande — ce que l'école n'enseigne pas mais qu'on utilise chaque jour.",
              T1_EN, T2_EN),
    'de':    ('Weiterführende Links · Zwei weitere „fehlende“ Kurse',
              'Eine offene chinesische Einführung in die Informatik — aus ihrer Idee ist dieses Buch entstanden.',
              'Ein kostenloser MIT-Kurs über Shell, Git und Kommandozeile: Dinge, die die Schule nicht lehrt, die man aber täglich braucht.',
              T1_EN, T2_EN),
    'ar':    ('روابط مفيدة · دورسان آخران «ناقصان»',
              'كتاب مفتوح المصدر بالصينية عن أساسيات الحوسبة، ومن فكرته نشأ هذا الكتاب.',
              'دورة مجانية من MIT عن الطرفية و Git وسطر الأوامر: أشياء لا تُدرَّس في المدرسة لكنها تُستخدم كل يوم.',
              T1_EN, T2_EN),
    'he':    ('קישורים מועילים · עוד שני «קורסים שחסרים»',
              'ספר קוד פתוח בסינית על יסודות המחשוב; הרעיון לספר הזה צמח ממנו.',
              'קורס חינמי של MIT על מעטפת, Git ושורת הפקודה — דברים שלא מלמדים בבית הספר אבל משתמשים בהם כל יום.',
              T1_EN, T2_EN),
    'th':    ('ลิงก์ที่แนะนำ · อีกสอง «วิชาที่ขาดหาย»',
              'หนังสือคอมพิวเตอร์เบื้องต้นแบบโอเพนซอร์สภาษาจีน ซึ่งเป็นจุดเริ่มต้นของหนังสือเล่มนี้',
              'คอร์สฟรีจาก MIT เกี่ยวกับเชลล์ Git และบรรทัดคำสั่ง — สิ่งที่โรงเรียนไม่สอนแต่ใช้ทุกวัน',
              T1_EN, T2_EN),
    'id':    ('Tautan bermanfaat · Dua "kursus yang hilang" lainnya',
              'Buku pengantar komputasi open source berbahasa Tionghoa; ide buku ini berawal darinya.',
              'Kursus gratis dari MIT tentang shell, Git, dan baris perintah — hal yang tidak diajarkan di sekolah tetapi dipakai setiap hari.',
              T1_EN, T2_EN),
    'ms':    ('Pautan berguna · Dua lagi "kursus yang tertinggal"',
              'Buku pengenalan pengkomputeran sumber terbuka dalam bahasa Cina; idea buku ini berasal daripadanya.',
              'Kursus percuma daripada MIT tentang shell, Git dan baris arahan — perkara yang tidak diajar di sekolah tetapi digunakan setiap hari.',
              T1_EN, T2_EN),
    'el':    ('Χρήσιμοι σύνδεσμοι · Δύο ακόμη «μαθήματα που λείπουν»',
              'Ένα ανοιχτό κινεζικό εγχειρίδιο εισαγωγής στην πληροφορική· από την ιδέα του γεννήθηκε αυτό το βιβλίο.',
              'Ένα δωρεάν μάθημα του MIT για το κέλυφος, το Git και τη γραμμή εντολών — πράγματα που δεν διδάσκονται στο σχολείο αλλά χρησιμοποιούνται καθημερινά.',
              T1_EN, T2_EN),
}


def md_block(lang):
    h, d1, d2, t1, t2 = TEXT[lang]
    return (f'\n\n#### {h}：\n\n'
            f'- <strong>{t1}</strong>：<a href="{U1}" {A_CLS}>www.criwits.top/missing/</a> — {d1}\n'
            f'- <strong>{t2}</strong>：<a href="{U2}" {A_CLS}>missing.csail.mit.edu</a> — {d2}\n')


def html_block():
    h, d1, d2, t1, t2 = TEXT['zh-CN']
    return (f'\n<h4 class="text-lg font-semibold mt-4 mb-2">{h}：</h4>\n'
            f'<ul class="list-disc pl-6 mb-3 space-y-1">\n'
            f'  <li><strong>{t1}</strong>：<a href="{U1}" {A_CLS}>www.criwits.top/missing/</a> — {d1}</li>\n'
            f'  <li><strong>{t2}</strong>：<a href="{U2}" {A_CLS}>missing.csail.mit.edu</a> — {d2}</li>\n'
            f'</ul>\n')


def md_path(lang):
    if lang == 'zh-CN':
        return ROOT / 'source' / 'chapters' / '78-fu-lu-d.md'
    return ROOT / 'source' / 'translations' / lang / 'chapters' / '78-fu-lu-d.md'


def strip_old(s):
    """剥掉上一次追加的小节（含 U1 的最后一个 #### 块）。"""
    marks = [m.start() for m in re.finditer(r'\n\n#### [^\n]*\n', s)
             if U1 in s[m.start():m.start() + 1200]]
    return s[:marks[-1]].rstrip() if marks else s.rstrip()


def do_v18_md(apply=True):
    changed = 0
    for lang in TEXT:
        p = md_path(lang)
        if not p.is_file():
            print(f'  跳过 {lang}: 无源稿')
            continue
        s = p.read_text(encoding='utf-8')
        base = strip_old(s)
        new = base + md_block(lang)
        if new == s:
            print(f'  · {lang}: 已是最新')
            continue
        changed += 1
        if apply:
            p.write_text(new, encoding='utf-8', newline='')
        print(f'  OK {lang}: {"重加" if base != s.rstrip() else "追加"}本地化链接小节')
    return changed


def do_v19_html(apply=True):
    for p in [ROOT / 'v1.9' / 'zh-CN.html', ROOT / '你缺失的那门手机课V1.9Fixed.html']:
        s = p.read_text(encoding='utf-8')
        if U1 in s and U2 in s:
            print(f'  · {p.name}: 已含两个链接')
            continue
        i, j = s.find('id="fu-lu-d"'), s.find('id="fu-lu-e"')
        if i < 0:
            print(f'  !! {p.name}: 找不到附录 D')
            continue
        m = re.search(r'<h4[^>]*>\s*安全自查', s[i:j])
        pos = i + m.start() if m else j
        s = s[:pos] + html_block() + s[pos:]
        if apply:
            p.write_text(s, encoding='utf-8', newline='')
        print(f'  OK {p.name}: 注入友情链接')


def main():
    apply = '--apply' in sys.argv
    print('=== v1.8 源稿（19 语）===')
    n = do_v18_md(apply)
    print(f'\n待改 {n} 个源稿' + ('（已写盘）' if apply else '（干跑）'))
    print('\n=== v1.9 HTML（2 个副本）===')
    do_v19_html(apply)
    print('\n下一步：重建 v1.8 19 语 HTML，再跑 lint 验证 residual')


if __name__ == '__main__':
    main()
