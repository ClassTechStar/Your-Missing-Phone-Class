#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把书名统一为「你缺失的那门手机课」的各语言译名。

项目从未有过别的名字。书名出现在两处，都要改：
  1. book.json 的 title 字段（模板里的 {{TITLE}} 与 typeset.py 的 PDF 书名都取自它）
  2. 模板里硬编码的书名：meta description / og:image:alt / twitter:title /
     <title> / <h1 id="hero-title"> / 页内「回到首页」链接文字

英文名取项目文件夹名：Your-Missing-Phone-Class → Your Missing Phone Class。

用法：
    python scripts/rename_book.py            # 干跑
    python scripts/rename_book.py --apply    # 写盘
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# 「你缺失的那门手机课」各语言译名
TITLES = {
    'zh-CN': '你缺失的那门手机课',
    'en':    'Your Missing Phone Class',          # 项目文件夹名
    'zh-TW': '你缺失的那門手機課',
    'yue':   '你缺失嘅嗰堂手機課',
    'lzh':   '爾所缺之手機課',
    'ja':    'あなたに足りなかったスマホの授業',
    'ko':    '당신이 놓친 스마트폰 수업',
    'ar':    'درس الهاتف الذي فاتك',
    'he':    'שיעור הסמארטפון שהחסרת',
    'th':    'คาบเรียนมือถือที่คุณขาดไป',
    'ru':    'Урок смартфона, который вы пропустили',
    'el':    'Το μάθημα κινητού που σου έλειψε',
    'de':    'Der Smartphone-Kurs, der dir gefehlt hat',
    'fr':    'Le cours de smartphone qui vous manquait',
    'es':    'La clase de móvil que te faltaba',
    'it':    'La lezione di smartphone che ti è mancata',
    'pt':    'A aula de celular que você não teve',
    'id':    'Pelajaran ponsel yang Anda lewatkan',
    'ms':    'Kelas telefon yang anda tertinggal',
}

RE_HERO = re.compile(r'(<h1 id="hero-title"[^>]*>)([^<]*)(</h1>)')
# 「回到首页」链接：各语言的 aria-label 是本地化的（"Zur Startseite" /
# "ホームに戻る" / "العودة إلى الصفحة الرئيسية"…），只能靠固定的 class 组合定位
RE_HOME = re.compile(
    r'(<a href="#top" class="flex items-center gap-2 min-w-0" aria-label="[^"]*">)'
    r'([^<]*)(</a>)')


def sources(lang):
    if lang == 'zh-CN':
        return ROOT / 'source' / 'book.json', ROOT / 'source' / 'template' / 'shell.html'
    base = ROOT / 'source' / 'translations' / lang
    return base / 'book.json', base / 'template' / 'shell.html'


def old_names(lang, book, tpl_text):
    """收集该语言模板里出现过的全部旧书名（book.json title 与硬编码可能不同）。"""
    names = {book.get('title', '').strip()}
    m = RE_HERO.search(tpl_text)
    if m:
        names.add(m.group(2).strip())
    return {n for n in names if n and n != TITLES[lang]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()
    changed = 0

    for lang, new in TITLES.items():
        bpath, tpath = sources(lang)
        if not bpath.is_file() or not tpath.is_file():
            print(f'  跳过 {lang}：源稿缺失')
            continue
        book = json.loads(bpath.read_text(encoding='utf-8'))
        tpl = tpath.read_text(encoding='utf-8')
        olds = old_names(lang, book, tpl)
        # 「回到首页」链接文字往往是「旧书名 · 副标题」，未被 olds 覆盖
        m_home = RE_HOME.search(tpl)
        home_stale = bool(m_home) and m_home.group(2).strip() != new
        m_hero = RE_HERO.search(tpl)
        hero_stale = bool(m_hero) and m_hero.group(2).strip() != new

        if not olds and not home_stale and not hero_stale \
                and book.get('title') == new:
            print(f'  · {lang}: 已是「{new}」')
            continue

        print(f'  OK {lang}: → {new}')
        for o in sorted(olds, key=len, reverse=True):
            print(f'       替换旧名 {o[:52]}')
        if home_stale:
            print(f'       替换首页链接 {m_home.group(2).strip()[:52]}')
        if hero_stale:
            print(f'       替换 hero {m_hero.group(2).strip()[:52]}')
        changed += 1
        if not args.apply:
            continue

        # 1) book.json
        book['title'] = new
        bpath.write_text(json.dumps(book, ensure_ascii=False, indent=1) + '\n',
                         encoding='utf-8', newline='')
        # 2) 模板：长串先替，避免短串先命中造成残片
        for o in sorted(olds, key=len, reverse=True):
            tpl = tpl.replace(o, new)
        # 3) 页内「回到首页」短名（各语言写法不一，统一成书名）
        tpl = RE_HOME.sub(lambda m: m.group(1) + new + m.group(3), tpl)
        # 4) hero-title 兜底（若上面整串替换没覆盖到）
        tpl = RE_HERO.sub(lambda m: m.group(1) + new + m.group(3), tpl)
        tpath.write_text(tpl, encoding='utf-8', newline='')

    print(f'\n待改 {changed} 个语言' + ('（已写盘）' if args.apply else '（干跑）'))
    if not args.apply:
        return

    # 自检：所有 book.json 的 title 必须等于译名表
    bad = []
    for lang, new in TITLES.items():
        bpath, _ = sources(lang)
        b = json.loads(bpath.read_text(encoding='utf-8'))
        if b.get('title') != new:
            bad.append((lang, b.get('title')))
    if bad:
        print('!! 以下语言 title 仍未对齐：', bad)
        sys.exit(1)
    print('自检通过：19 个 book.json 的 title 全部对齐')


if __name__ == '__main__':
    main()
