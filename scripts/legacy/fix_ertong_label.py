# -*- coding: utf-8 -*-
"""er-tong 篇标签范围更新：v1.8 → 第35-36章；v1.7 视实际内容 → 35-36 / 35-41。

用法：python scripts/fix_ertong_label.py [--apply]
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

APPLY = '--apply' in sys.argv

# 语言 → (旧 token 正则, 36 版替换, 41 版替换)
TABLE = {
    'zh-CN': (r'（第35章）', '（第35-36章）', '（第35-41章）'),
    'zh-TW': (r'（第35章）', '（第35-36章）', '（第35-41章）'),
    'yue':   (r'（第35章）', '（第35-36章）', '（第35-41章）'),
    'lzh':   (r'（第35章）', '（第35-36章）', '（第35-41章）'),
    'ja':    (r'（第三十五章）', '（第三十五・三十六章）', '（第三十五〜四十一章）'),
    'ko':    (r'\(제35장\)', '(제35-36장)', '(제35-41장)'),
    'en':    (r'\(Chapter 35\)', '(Chapters 35-36)', '(Chapters 35-41)'),
    'ru':    (r'\(Глава 35\)', '(Главы 35–36)', '(Главы 35–41)'),
    'de':    (r'\(Kapitel 35\)', '(Kapitel 35-36)', '(Kapitel 35-41)'),
    'fr':    (r'\(Chapitre 35\)', '(Chapitres 35-36)', '(Chapitres 35-41)'),
    'es':    (r'\(Capítulo 35\)', '(Capítulos 35-36)', '(Capítulos 35-41)'),
    'pt':    (r'\(Capítulo 35\)', '(Capítulos 35-36)', '(Capítulos 35-41)'),
    'it':    (r'\(Capitolo 35\)', '(Capitoli 35-36)', '(Capitoli 35-41)'),
    'el':    (r'\(Κεφάλαιο 35\)', '(Κεφάλαια 35-36)', '(Κεφάλαια 35-41)'),
    'ar':    (r'\(الفصل 35\)', '(الفصول 35-36)', '(الفصول 35-41)'),
    'he':    (r'\(פרק 35\)', '(פרקים 35-36)', '(פרקים 35-41)'),
    'th':    (r'\(บทที่ 35\)', '(บทที่ 35-36)', '(บทที่ 35-41)'),
    'id':    (r'\(Bab 35\)', '(Bab 35-36)', '(Bab 35-41)'),
    'ms':    (r'\(Bab 35\)', '(Bab 35-36)', '(Bab 35-41)'),
}

H2_RE = re.compile(
    r'(<section id="er-tong-pian"[^>]*>\s*<h2[^>]*>)(.*?)(</h2>)', re.S)
SB_RE = re.compile(r'(<a href="#er-tong-pian"[^>]*>)([^<]*)(</a>)')

def section_chapters(raw):
    m = re.search(r'<section id="er-tong-pian".*?</section>', raw, re.S)
    if not m:
        return []
    return re.findall(r'<div id="([a-z0-9-]+)" class="mb-10 content-section"', m.group(0))

def fix(path: Path):
    raw = path.read_text(encoding='utf-8')
    chs = section_chapters(raw)
    if not chs:
        return None
    lang = path.stem
    if lang not in TABLE:
        return f'{path}: 无替换表'
    pat, r36, r41 = TABLE[lang]
    has41 = 'di-si-shi-yi-zhang' in chs
    rep = r41 if has41 else r36
    n = 0
    m = H2_RE.search(raw)
    if m and re.search(pat, m.group(2)):
        raw = H2_RE.sub(lambda mm: mm.group(1) + re.sub(pat, rep, mm.group(2)) + mm.group(3), raw, count=1)
        n += 1
    m = SB_RE.search(raw)
    if m and re.search(pat, m.group(2)):
        raw = SB_RE.sub(lambda mm: mm.group(1) + re.sub(pat, rep, mm.group(2)) + mm.group(3), raw, count=1)
        n += 1
    if n and APPLY:
        path.write_text(raw, encoding='utf-8', newline='')
    return f'{path.parent.name}/{path.name}: {chs[-1][-3:]}… {n} 处 → {rep}'

def main():
    for ver in ['v1.7', 'v1.8']:
        for p in sorted((ROOT / ver).glob('*.html')):
            if p.stem == 'index' or (ver, p.stem) == ('v1.7', 'lzh'):
                continue
            r = fix(p)
            if r:
                print(r)
    # 根目录 zh 源文件
    p = ROOT / '你缺失的那门手机课V1.8Fixed.html'
    if p.exists():
        print(fix(p))
    print('APPLY =', APPLY)

if __name__ == '__main__':
    main()
