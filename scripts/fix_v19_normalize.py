#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v1.9 结构归一化（2026-11-17，源稿回写前置修复）。

目标：让 v1.9/zh-CN.html 通过 htmlparse 严格往返，并与
bookkit Markdown 方言的规范形对齐，使 `bookkit extract` 能完整
反解 120 区块、`bookkit build --verify` 达成源稿↔成品等价。

修复项（均为核实过的真实缺陷）：
 1. 第 41 章：`把 <<<<<<<、=======、>>>>>>> 这些标记行……`（git 冲突
    标记示例）——可见文本里未转义的裸 `<` / `>`
 2. 第 63 章：`左上角自动出现"< 返回"`（iOS 返回按钮写法）——裸 `<`
    浏览器按 HTML5 规则把裸 `<` 渲染成文字，肉眼看不出异常；
    但 bookkit 的 htmlparse 做「引号感知」标签扫描时，`< 返回"` 的
    引号状态会一路漂移，把其后 2.7MB（第 64 章～结语，共 51 个区块）
    吞进同一个文本节点。
 3. 第 53/54 章之间：`<!-- 第54章 -->` 注释重复，且夹着损坏残片
    `<div\\n</div>`——开标签把 `</div>` 当自身结尾吞掉，其后第 54–58 章
    被裹进一个 273KB 的无名 div，序列化时凭空多出一个 `</div>`。
 4. 附录 B 练习打卡表：`<p class="mb-2">` 段落缺 `</p>` 直接跟了
    `<div class="overflow-x-auto">`——浏览器按可选结束标签规则自动闭合
    所以渲染正常，解析器则让这个 p 吞掉了后面 15KB。
 5. 六处 `<!-- v19-*-section -->` 注入脚本标记注释：位于章节块内部，
    Markdown 方言不表示块级注释，回写重建会丢失 → 作为工具残留清除。
 6. 第 59 章 iOS 流水线图：flex 行的 `</div>` 提前闭合，「提交审核 /
    App Store 上架」两个步骤芯片漏出行外（渲染掉行）——归位到 flex 行内。
 7. 第 61 章 pre 尾部多余换行：方言的 ``` 围栏无法表示 pre 尾换行
    （表示它会破坏 19 语 v1.8 等价性），归一去除。
 8. 第 31/32 章「本章小结」卡浮在章节 div 之外（各章常态是章内结尾）：
    反解会把它们并进篇导语、重建后跑到全篇开头 → 归位到所属章节内。

脚本幂等：已应用过的修复自动跳过。修复后自检：
  - htmlparse 严格往返（parse→serialize 字节无损）
  - content-section 区块数 = 120
  - 无游离 chapter-summary、无 v19 标记注释残留

用法：
    python scripts/fix_v19_normalize.py            # 干跑，打印命中数
    python scripts/fix_v19_normalize.py --apply    # 写盘
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from bookkit import htmlparse as H  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
SUB = ROOT / 'v1.9' / 'zh-CN.html'

# (说明, 旧串, 新串, 期望命中数)
FIXES = [
    ('git 冲突标记示例转义',
     '把 <<<<<<<、=======、>>>>>>> 这些标记行',
     '把 &lt;&lt;&lt;&lt;&lt;&lt;&lt;、=======、&gt;&gt;&gt;&gt;&gt;&gt;&gt; 这些标记行',
     1),
    ('iOS 返回按钮写法转义',
     '自动出现"< 返回"',
     '自动出现"&lt; 返回"',
     1),
    ('删除第54章重复注释与 <div\\n</div> 损坏残片',
     '<!-- 第54章 -->\n\n                <div\n</div>\n\n                <!-- 第54章 -->',
     '<!-- 第54章 -->',
     1),
    ('附录B 练习打卡表段落补闭合 </p>（浏览器自动闭合，解析器不闭合）',
     '仪式感很重要。\n<div class="overflow-x-auto">',
     '仪式感很重要。</p>\n<div class="overflow-x-auto">',
     1),
    ('清除注入标记注释 alu', '\n<!-- v19-alu-section -->', '', 1),
    ('清除注入标记注释 cmos', '\n<!-- v19-cmos-section -->', '', 1),
    ('清除注入标记注释 soc', '\n<!-- v19-soc-mechanism-chapter -->', '', 1),
    ('清除注入标记注释 baseband', '\n<!-- v19-baseband-rf-section -->', '', 1),
    ('清除注入标记注释 gan', '\n<!-- v19-gan-adapter-section -->', '', 1),
    ('清除注入标记注释 appendix-h', '\n<!-- v19-appendix-h-2026-11 -->', '', 1),
    ('清除 shell 区注入标记注释 first-chapter-visibility',
     '\n<!-- v19-first-chapter-visibility-fix -->', '', 1),
    ('第59章 flex 行：撤销过早闭合',
     '写代码（Swift + SwiftUI）</span></div><span class="text-gray-400 mx-1">➜</span>',
     '写代码（Swift + SwiftUI）</span><span class="text-gray-400 mx-1">➜</span>',
     1),
    ('第59章 flex 行：行尾补回闭合（带后缀锚，防重复命中）',
     'App Store 上架</span></div>\n<p class="mb-2">两道',
     'App Store 上架</span></div></div>\n<p class="mb-2">两道',
     1),
    ('第61章 pre 尾换行归一',
     '它每次都现算\n</pre>',
     '它每次都现算</pre>',
     1),
]


def move_summaries(tree) -> int:
    """游离的 chapter-summary 卡归位到所属章节 content-section 内（章尾）。"""
    moved = 0
    for n in tree.find_all('div'):
        if 'chapter-summary' not in n.classes:
            continue
        p = n.parent
        if p is not None and p.tag == 'div' and 'content-section' in p.classes:
            continue
        prev = None
        for c in p.children:
            if c is n:
                break
            if isinstance(c, H.Node) and c.tag == 'div' and 'content-section' in c.classes:
                prev = c
        if prev is None:
            continue
        p.children.remove(n)
        n.parent = prev
        prev.children.append(n)
        moved += 1
    return moved


def self_check(raw: str) -> bool:
    ok = True
    tree = H.parse(raw)
    if H.serialize(tree) != raw:
        print('  ! 严格往返仍不通过（还有解析脱轨点）')
        ok = False
    blocks = [n for n in tree.find_all('div') if 'content-section' in n.classes]
    if len(blocks) != 120:
        print(f'  ! content-section 区块数 {len(blocks)}，期望 120')
        ok = False
    floating = 0
    for n in tree.find_all('div'):
        if 'chapter-summary' in n.classes:
            p = n.parent
            if not (p is not None and p.tag == 'div' and 'content-section' in p.classes):
                floating += 1
    if floating:
        print(f'  ! 仍有 {floating} 个游离 chapter-summary')
        ok = False
    if 'v19-' in raw and '<!-- v19-' in raw:
        print('  ! 仍有 v19 标记注释残留')
        ok = False
    if ok:
        print('  ✓ 严格往返通过，content-section = 120，无游离小结/标记注释')
    return ok


def main():
    apply = '--apply' in sys.argv
    raw = SUB.read_text(encoding='utf-8')
    ok = True
    pending = []
    for note, old, new, want in FIXES:
        got = raw.count(old)
        if got == want:
            print(f'命中 {got}/{want}：{note}')
            pending.append((old, new))
        elif got == 0:
            print(f'已应用（跳过）：{note}')
        else:
            print(f'!! 命中数异常 {got}/{want}：{note}')
            ok = False
    if not ok:
        print('中止：先核对原文再调整期望命中数')
        return 1

    if not apply:
        tree = H.parse(raw)
        n = 0
        for d in tree.find_all('div'):
            if 'chapter-summary' in d.classes and not (
                    d.parent is not None and d.parent.tag == 'div'
                    and 'content-section' in d.parent.classes):
                n += 1
        print(f'游离 chapter-summary 待归位：{n} 个')
        print('（dry-run，未写盘；加 --apply 应用）')
        return 0

    for old, new in pending:
        raw = raw.replace(old, new)
    tree = H.parse(raw)
    moved = move_summaries(tree)
    raw = H.serialize(tree)
    SUB.write_text(raw, encoding='utf-8', newline='')
    print(f'已写盘：{SUB.relative_to(ROOT)}（字符串修复 {len(pending)} 项，小结归位 {moved} 个）')
    print('自检：')
    return 0 if self_check(raw) else 1


if __name__ == '__main__':
    sys.exit(main())
