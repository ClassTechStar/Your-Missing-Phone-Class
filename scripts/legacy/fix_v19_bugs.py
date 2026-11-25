#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v1.9 全量 bug 修复（2026-11-07）。

修复项（均为核实过的真实问题）：
  1. hero 宣称「69 章 + 8 附录」→「105 章 + 8 附录」（v1.8 遗留）
  2. 「学习路径：五步」但实际列 8 步 → 改「八步打基础」+ 注释
  3. 学习路径末尾补一句：第 33–36 章专题与第 70–105 章可按兴趣跳读
  4. 「共分十五篇」但列举只有 14 个 → 补「展望与车联」
  5. 5 处「补记」悬空引用（补记已整合进正文，读者找不到该小节）
  6. og:image / twitter:image 指向已删除的 cover-og.png（实测 404）
     → 指向站点真实存在的 icons/icon-512.png，宽高同步改 512
  7. 仅根目录副本：SW 注册 `../sw.js` + scope `../` 与同目录 index.html
     的写法不一致 → 改 `sw.js` + scope `./`

两个文件其余内容保持一致（根目录副本的 icons/manifest 路径降级保留）。

用法：
    python scripts/fix_v19_bugs.py            # 干跑，打印命中数
    python scripts/fix_v19_bugs.py --apply    # 写盘
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUB = ROOT / 'v1.9' / 'zh-CN.html'
DUP = ROOT / '你缺失的那门手机课V1.9Fixed.html'

OLD_IMG = 'https://classtechstar.github.io/Yihggh.github.io/cover-og.png'
NEW_IMG = 'https://classtechstar.github.io/Yihggh.github.io/icons/icon-512.png'

# (说明, 旧串, 新串, 期望命中数)
COMMON = [
    ('hero 章数', '69 章 + 8 附录', '105 章 + 8 附录', 1),
    ('学习路径注释', '<!-- 学习路径五步走 -->', '<!-- 学习路径八步走 -->', 1),
    ('学习路径标题', '学习路径：五步成为手机达人', '学习路径：八步打基础', 1),
    ('阅读路线列举补展望篇',
     '基础→软件→进阶→超越→实战→AI编程→安卓→iOS→鸿蒙→可穿戴→旅行→健康→AI短视频→短剧',
     '基础→软件→进阶→超越→实战→展望与车联→AI编程→安卓→iOS→鸿蒙→可穿戴→旅行→健康→AI短视频→短剧', 1),
    ('补记悬空引用 A', '第二十六章补记的三问判断', '第二十六章的三问判断', 2),
    ('补记悬空引用 B',
     '各章补记已按 2026 年 11 月的公开信息校订过一轮',
     '各章内容已按 2026 年 11 月的公开信息校订过一轮', 1),
    ('补记悬空引用 C',
     '四大部分与全章补记统一按 2026 年末的公开事实校订',
     '四大部分与全书各章统一按 2026 年末的公开事实校订', 1),
    ('补记悬空引用 D', '多语言版本的补记翻译', '多语言版本的内容翻译', 1),
    ('og:image 死链', OLD_IMG, NEW_IMG, 2),
    ('og:image 宽', '<meta property="og:image:width" content="1200">',
     '<meta property="og:image:width" content="512">', 1),
    ('og:image 高', '<meta property="og:image:height" content="630">',
     '<meta property="og:image:height" content="512">', 1),
]

PATH_NOTE_OLD = '''                    </a>
                </div>
            </section>

            <!-- 章节地图速查表 -->'''
PATH_NOTE_NEW = '''                    </a>
                </div>
                <p class="text-sm text-gray-600 dark:text-gray-400 mt-3">第 33–36 章是「展望与车联」「儿童与手机」两个专题；第 70–105 章是鸿蒙开发与五大生活创作篇。这些篇章彼此独立，按兴趣直接跳读即可，不必按顺序。</p>
            </section>

            <!-- 章节地图速查表 -->'''

# 仅根目录副本
DUP_ONLY = [
    ('SW 注册路径', "navigator.serviceWorker.register('../sw.js', { scope: '../' })",
     "navigator.serviceWorker.register('sw.js', { scope: './' })", 1),
]


def check(name, s, fixes):
    ok = True
    print(f'  [{name}]')
    for label, old, new, expect in fixes:
        n = s.count(old)
        flag = 'OK  ' if n == expect else 'FAIL'
        if n != expect:
            ok = False
        print(f'    {flag} {label}: 命中 {n} / 期望 {expect}')
    return ok


def apply(s, fixes):
    for label, old, new, _ in fixes:
        s = s.replace(old, new)
    return s


def main():
    do_apply = '--apply' in sys.argv
    a = SUB.read_text(encoding='utf-8')
    b = DUP.read_text(encoding='utf-8')

    # 根目录副本的 icons/manifest 已降级，先把这些差异归一化后与子目录版比对
    norm = (b.replace('href="icons/', 'href="../icons/')
             .replace('href="manifest.webmanifest"', 'href="../manifest.webmanifest"'))
    if a != norm:
        print('!! 两副本归一化后仍不一致，停止修复')
        return 1
    print('前置检查：两副本除路径降级外正文一致 ✓\n')

    fixes_a = COMMON + [('学习路径末尾引导', PATH_NOTE_OLD, PATH_NOTE_NEW, 1)]
    ok = check('v1.9/zh-CN.html', a, fixes_a)
    ok &= check('V1.9Fixed.html（仅通用项）', b, COMMON)
    ok &= check('V1.9Fixed.html（专属项）', b, DUP_ONLY)
    # 引导块在根目录副本里也应有（正文一致）
    if b.count(PATH_NOTE_OLD) != 1:
        print('    FAIL 根目录副本缺学习路径引导锚点')
        ok = False
    if not ok:
        print('\n!! 有命中数不符，未写盘')
        return 1
    if not do_apply:
        print('\n（干跑，未写盘）')
        return 0

    a2 = apply(a, fixes_a)
    b2 = apply(b, COMMON + [('学习路径末尾引导', PATH_NOTE_OLD, PATH_NOTE_NEW, 1)] + DUP_ONLY)
    SUB.write_text(a2, encoding='utf-8', newline='')
    DUP.write_text(b2, encoding='utf-8', newline='')
    print('\n已写盘：两个 v1.9 HTML')
    return 0


if __name__ == '__main__':
    sys.exit(main())
