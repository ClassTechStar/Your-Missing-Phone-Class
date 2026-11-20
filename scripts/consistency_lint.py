#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""consistency_lint.py — 元数据单一真源核对（优化方案 §4）。

用法: python scripts/consistency_lint.py
退出码: 0 全部一致 / 1 发现不一致

真源（谁也不许跟它不一致）：
  - 章数 / 篇数：source/v1.9/book.json（最新中文版的结构清单）
  - 字数：v1.9/zh-CN.html 的可见文本（构建产物，与 bookkit check --claims 同口径）

消费方（数字只允许出现在这些地方，且必须与真源一致）：
  README.md / manifest.webmanifest / site-landing.html（站点首页）/
  index.html（仓库入口页）/ announcements.json / languages.html

统一口径（方案 §4.3）：「N 章 · N 篇 · N 万字」，弃用「个内容区块」——
「内容区块」读者不感知。篇数 = book.json 里带中文数字编号且标题含「篇」的部分
（专题与附录不计）；万字 = 可见文本去空白字符数 ÷ 10000，一位小数。

站点基建（robots / sitemap 覆盖 / OG 每章唯一 / 死链）不归本脚本，
见 scripts/site_lint.py。本脚本的价值不在这一次修对，而在 v2.0 扩写
下一批章节时，CI 会拦住「改了 book.json 忘了改首页」这类事故——
2026-11-20 的三处数字矛盾就是这种事故的存量。
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))          # 复用 bookkit 的可见文本提取（零外部依赖）
from bookkit import textutil as T      # noqa: E402

BOOK_REL = Path('source') / 'v1.9' / 'book.json'
BASELINE_HTML = Path('v1.9') / 'zh-CN.html'

# 中文数字编号（「一、基础篇」的「一」）
RE_NUMERAL = re.compile(r'^[一二三四五六七八九十]+、')


def cn2num(s: str) -> int:
    """中文数字（一~九十九）→ int；纯数字串直接解析。

    README 里「十五篇」和「15 篇」混排，比对前统一转成整数。
    """
    s = s.strip()
    if s.isdigit():
        return int(s)
    d = {'零': 0, '一': 1, '二': 2, '三': 3, '四': 4,
         '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}
    if '百' in s:
        raise ValueError(f'cn2num：暂不支持百位以上（{s}）')
    if '十' in s:
        left, _, right = s.partition('十')
        tens = d.get(left, 1) if left else 1
        ones = d.get(right, 0) if right else 0
        return tens * 10 + ones
    if len(s) == 1:
        return d[s]
    raise ValueError(f'cn2num：无法解析（{s}）')


def count_pian(book: dict) -> int:
    """篇数 = 目录里带中文数字编号且标题含「篇」的部分。

    例：「一、基础篇」计数；「儿童与手机专题」「十六、附录」不计——
    专题不是篇，附录不是篇，这就是「15 篇」口径的定义。
    """
    n = 0
    for p in book.get('parts', []):
        nav = p.get('nav') or ''
        if RE_NUMERAL.match(nav) and '篇' in nav:
            n += 1
    return n


def wan_chars(root: Path) -> str:
    """字数（万字）= 已发布单文件的可见文本去空白字符数，与 claims.py 同口径。"""
    html = (root / BASELINE_HTML).read_text(encoding='utf-8')
    chars = len(re.sub(r'\s+', '', T.visible_text(html)))
    return f'{round(chars / 10000, 1):g}'


def read(rel) -> str:
    return (ROOT / rel).read_text(encoding='utf-8')


def check(failures: list, rel, pattern: str, expect, label: str,
          parse=None, all_matches: bool = False) -> None:
    """把文件里正则捕获的数字与真源比对。

    expect 为单值或与捕获组一一对应的列表；parse 为逐组转换（如 cn2num）。
    all_matches=True 时该模式的每一处宣称都要一致（多处提及时防漏改）。
    """
    text = read(rel)
    ms = re.findall(pattern, text)
    if not ms:
        failures.append(f'[FAIL] {label}: 未找到宣称位置（{rel}，模式 {pattern}）')
        return
    if not all_matches:
        ms = ms[:1]
    expects = expect if isinstance(expect, (list, tuple)) else [expect]
    for m in ms:
        got = m if isinstance(m, tuple) else (m,)
        for i, (g, want) in enumerate(zip(got, expects)):
            if parse:
                g = parse(g)
            if str(g) != str(want):
                failures.append(
                    f'[FAIL] {label}: 真源={want} 该文件={g} ({rel} 第 {i + 1} 组)')


def check_absent(failures: list, rel, needle: str, label: str) -> None:
    """读者可见处不允许出现的过期口径/旧数字。"""
    if needle in read(rel):
        failures.append(f'[FAIL] {label}: {rel} 仍含 {needle!r}')


def check_lang_registry(failures: list) -> int:
    """语言注册表 ↔ 实际语言版本一一对应，返回语言数。

    注册表里有、但既没有源稿也没有成品的语言是「假装有这个版本」——
    分级页会把它写成「机器翻译版」，而读者根本无从读起。
    """
    langs = json.loads(read(Path('manifest') / 'languages.json'))['languages']
    for code in langs:
        has_source = code == 'zh-CN' or (ROOT / 'source' / 'translations' / code / 'book.json').is_file()
        has_build = (ROOT / 'v1.8' / f'{code}.html').is_file()
        if not (has_source or has_build):
            failures.append(f'[FAIL] 语言注册表: {code} 无源稿也无成品（注册表不允许登记未发布的语言）')
    published = len(list((ROOT / 'v1.8').glob('*.html')))
    if len(langs) != published:
        failures.append(f'[FAIL] 语言数: 注册表={len(langs)} v1.8 成品={published}')
    return len(langs)


def main() -> int:
    book = json.loads(read(BOOK_REL))
    n_chapters = len(book['chapters'])
    n_pian = count_pian(book)
    wan = wan_chars(ROOT)
    failures = []
    n_langs = check_lang_registry(failures)

    # ---------- README.md：badge / 导语三连 / 小节标题 / 仓库表 ----------
    check(failures, 'README.md', r'badge/章节-(\d+)%20章·([\d.]+)%20万字',
          [n_chapters, wan], 'README badge 章数/字数')
    check(failures, 'README.md', r'badge/语言-(\d+)%20种', n_langs, 'README badge 语言数')
    check(failures, 'README.md', r'最新中文版 v1\.9 共 (\d+) 章 · (\d+) 篇 · ([\d.]+) 万字',
          [n_chapters, n_pian, wan], 'README 导语三连')
    check(failures, 'README.md', r'### v1\.9 · 最新中文版 — (\d+) 章 · ([\d.]+) 万字',
          [n_chapters, wan], 'README v1.9 小节')
    check(failures, 'README.md', r'全书([一二三四五六七八九十百零\d]+)篇',
          n_pian, 'README 篇数（散文）', parse=cn2num)
    check(failures, 'README.md', r'最新中文版：(\d+) 章，逐章约 [\d.]+ 万字（([\d.]+) 万字）',
          [n_chapters, wan], 'README 仓库表')
    for needle, label in (('个内容区块', '口径弃用'), ('353.7', '过期字数'), ('353.8', '过期字数')):
        check_absent(failures, 'README.md', needle, label)

    # ---------- manifest.webmanifest：安装到主屏幕时的第一句话 ----------
    check(failures, 'manifest.webmanifest', r'"description":\s*"(\d+) 章、(\d+) 篇、([\d.]+) 万字',
          [n_chapters, n_pian, wan], 'manifest description 三连')

    # ---------- site-landing.html（站点首页）----------
    check(failures, 'site-landing.html', r'<b>(\d+)</b> 章 · <b>(\d+)</b> 篇 · <b>([\d.]+)</b> 万字',
          [n_chapters, n_pian, wan], '站点首页 stats 三连')
    check(failures, 'site-landing.html', r'content="(\d+) 章、(\d+) 篇、(\d+) 种语言',
          [n_chapters, n_pian, n_langs], '站点首页 og:description')
    check(failures, 'site-landing.html', r'<b>(\d+)</b> 种语言', n_langs, '站点首页 语言数')
    for needle in ('353.7', '353.8'):
        check_absent(failures, 'site-landing.html', needle, '过期字数')

    # ---------- index.html（仓库入口页）----------
    check(failures, 'index.html', r'共 (\d+) 章 · ([\d.]+) 万字',
          [n_chapters, wan], 'index meta description', all_matches=True)
    check(failures, 'index.html', r'共 (\d+) 章、([\d.]+) 万字',
          [n_chapters, wan], 'index JSON-LD/页脚', all_matches=True)
    check(failures, 'index.html', r'— (\d+) 章 · ([\d.]+) 万字',
          [n_chapters, wan], 'index og:title')
    for needle, label in (('个内容区块', '口径弃用'), ('353.7', '过期字数'), ('353.8', '过期字数')):
        check_absent(failures, 'index.html', needle, label)

    # ---------- announcements.json / languages.html ----------
    check(failures, 'announcements.json', r'(\d+) 章、([\d.]+) 万字',
          [n_chapters, wan], '公告 章数/字数', all_matches=True)
    check(failures, 'languages.html', r'这本书有 (\d+) 个语言版本',
          n_langs, '语言分级页 语言数')

    # ---------- v1.9/zh-CN.html（书页分享卡文案）----------
    check(failures, Path('v1.9') / 'zh-CN.html',
          r'property="og:description" content="手机是用会的，不是看会的。(\d+) 章',
          n_chapters, '书页 og:description 章数')
    check_absent(failures, Path('v1.9') / 'zh-CN.html', '掌控你的数字生活', 'S 级黑名单句')
    check_absent(failures, 'site-landing.html', '掌控你的数字生活', 'S 级黑名单句')
    check_absent(failures, 'README.md', '掌控你的数字生活', 'S 级黑名单句')

    if failures:
        print('\n'.join(failures))
        print(f'\n共 {len(failures)} 处不一致——一律以 {BOOK_REL} 与 {BASELINE_HTML} 为准修复')
        return 1
    print(f'OK: README / manifest / 站点首页 / index / 公告 / 语言页一致 '
          f'（{n_chapters} 章 · {n_pian} 篇 · {wan} 万字 · {n_langs} 种语言）')
    return 0


if __name__ == '__main__':
    sys.exit(main())
