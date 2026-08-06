#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
v1.8 新章节整合脚本（方向 C）

读取 scripts/v1.8-chapters.json，把 5 个新章节（第37-41章）整合进 v1.7/zh-CN.html：
  1. 在第36章 content-section 之后、附录 section 之前插入 5 个新章节的 HTML
  2. 更新侧边栏"展望篇"分组：33-36 → 33-41，补齐 37-41 的导航条目
  3. 在附录G速查索引的对应字母分组中插入新章节的索引条目

设计为幂等：重复运行不会产生重复插入（先检查目标章节 id 是否已存在）。
用法：python3 scripts/integrate_v1.8.py
"""
import os
import re
import sys
import json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(ROOT, "v1.7", "zh-CN.html")
CHAPTERS_JSON = os.path.join(ROOT, "scripts", "v1.8-chapters.json")


def load_data():
    with open(CHAPTERS_JSON, encoding="utf-8") as f:
        return json.load(f)


def render_section_html(ch):
    """渲染单个章节的完整 content-section HTML 块。"""
    parts = []
    parts.append(f'            <div id="{ch["id"]}" class="mb-10 content-section">')
    parts.append(f'                <h3 class="text-xl font-bold text-dark dark:text-gray-200 mb-4">{ch["title"]}</h3>')
    parts.append(f'                <p class="chapter-intro mb-4">{ch["intro"]}</p>')
    for sec in ch["sections"]:
        parts.append(f'                <h4 class="text-lg font-semibold mt-4 mb-2">{sec["h"]}</h4>')
        if "p" in sec:
            parts.append(f'                <p class="mb-2">{sec["p"]}</p>')
        if "ul" in sec:
            parts.append('                <ul class="list-disc pl-6 mb-3 space-y-1">')
            for li in sec["ul"]:
                parts.append(f'                    <li>{li}</li>')
            parts.append('                </ul>')
        if "ol" in sec:
            parts.append('                <ol class="list-decimal pl-6 mb-3 space-y-1">')
            for li in sec["ol"]:
                parts.append(f'                    <li class="pl-1">{li}</li>')
            parts.append('                </ol>')
        if "p_after" in sec:
            parts.append(f'                <p class="mb-2">{sec["p_after"]}</p>')
        if "info_box" in sec:
            parts.append('                <div class="info-box rounded-lg p-4 mt-3">')
            parts.append(f'                    <p>{sec["info_box"]}</p>')
            parts.append('                </div>')
        if "table" in sec:
            t = sec["table"]
            parts.append('                <table class="w-full border-collapse border border-gray-300 text-sm mb-3">')
            parts.append('                    <thead>')
            parts.append('                        <tr class="bg-light dark:bg-gray-700">')
            for h in t["headers"]:
                parts.append(f'                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">{h}</th>')
            parts.append('                        </tr>')
            parts.append('                    </thead>')
            parts.append('                    <tbody>')
            for row in t["rows"]:
                parts.append('                        <tr>')
                for cell in row:
                    parts.append(f'                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">{cell}</td>')
                parts.append('                        </tr>')
            parts.append('                    </tbody>')
            parts.append('                </table>')
    # 动手练习
    parts.append('                <div class="bg-blue-50 dark:bg-gray-700 rounded-lg p-4 mt-4">')
    parts.append('                    <p class="font-semibold text-blue-700 dark:text-blue-300"><i class="fas fa-hand-pointer mr-2"></i>动手练习</p>')
    parts.append(f'                    <p class="mt-1 text-gray-700 dark:text-gray-300">{ch["practice"]}</p>')
    parts.append('                </div>')
    parts.append('            </div>')
    return "\n".join(parts)


def insert_chapters(html, data):
    """在第36章 content-section 结束后、附录 section 前插入新章节。"""
    # 幂等检查：若第41章已存在则跳过
    if 'id="di-si-shi-yi-zhang"' in html:
        print("  [跳过] 第41章已存在，章节插入似乎已完成")
        return html, 0
    # 定位插入点：附录 section 开始处
    marker = '            <!-- 七、附录 -->'
    if marker not in html:
        # 兜底：用附录 section 的 id
        marker = '<section id="fu-lu"'
    idx = html.find(marker)
    if idx == -1:
        print("  [错误] 找不到附录 section 插入点")
        return html, 0
    # 生成所有新章节 HTML
    blocks = []
    for ch in data["chapters"]:
        blocks.append(render_section_html(ch))
        blocks.append("")  # 空行分隔
    new_html_block = "\n".join(blocks)
    # 插入
    html = html[:idx] + new_html_block + "\n" + html[idx:]
    return html, len(data["chapters"])


def update_sidebar(html, data):
    """更新侧边栏展望篇分组：33-36 → 33-41，补齐 37-41 条目。"""
    # 更新分组标题
    html = html.replace(
        "六、展望篇（第33-36章）",
        "六、展望篇（第33-41章）"
    )
    # 在第36章侧边栏条目后插入 37-41 条目（幂等：检查侧边栏区域是否已有第37章条目）
    # 用 toc-item class 精确匹配侧边栏条目，避免被速查索引链接误判
    if 'href="#di-san-shi-qi-zhang" class="toc-item' in html:
        print("  [跳过] 侧边栏第37章条目已存在")
        return html
    # 找到第36章侧边栏条目行（一行内，含 span）
    pat = re.compile(
        r'(<li><a href="#di-san-shi-liu-zhang".*?</a></li>)',
        re.DOTALL
    )
    sidebar_entries = []
    for ch in data["chapters"]:
        num = ch["num"]
        title = ch["title"].split("：", 1)[1] if "：" in ch["title"] else ch["title"]
        sidebar_entries.append(
            f'<li><a href="#{ch["id"]}" class="toc-item block px-3 py-1.5 rounded-md hover:bg-light dark:hover:bg-gray-700 text-gray-600 dark:text-gray-400"><span class="mr-1.5 text-xs text-gray-400 font-mono">{num}</span>{ch["title"].split("：")[0]}：{title}</a></li>'
        )
    insertion = "\n                            ".join(sidebar_entries)
    html, n = pat.subn(lambda m: m.group(1) + "\n                            " + insertion, html)
    print(f"  侧边栏：插入 {n} 处条目组")
    return html


def update_index(html, data):
    """在附录G速查索引的对应分组插入新条目。"""
    # 幂等检查：速查索引的链接不带 toc-item class，用 text-primary 区分
    if 'href="#di-san-shi-qi-zhang" class="text-primary' in html:
        print("  [跳过] 速查索引第37章条目已存在")
        return html
    # 按分组聚合条目
    groups = {}
    for ch in data["chapters"]:
        for term in ch["index_terms"]:
            groups.setdefault(term["group"], []).append(
                f'<li>{term["term"]} → <a href="#{ch["id"]}" class="text-primary hover:underline">{ch["title"].split("：")[0]}</a></li>'
            )
    # 各分组的标识：A-J 分组的 <ul> 末尾插入 A-J 条目
    # 分组标题映射：A-J 对应实际标题可能是 "A-J" 或 "A-B"，统一用宽松匹配
    group_markers = {
        "A-J": [("A-J", "A-B"), ("C-D", None)],  # A-J 开头的词也常混在 C-D 块
        "S-Z": [("S-Z", None)],
    }
    # 简化策略：把所有 A-J 组的条目插到 C-D 块末尾（因为现有 A-J 词条实际在 C-D 块），
    # S-Z 组插到 S-Z 块末尾
    inserts = {"A-J": groups.get("A-J", []), "S-Z": groups.get("S-Z", [])}
    # 找到 "C-D" 分组块的 </ul>，在前面插入 A-J 条目
    for grp, entries in inserts.items():
        if not entries:
            continue
        if grp == "A-J":
            # C-D 块的 </ul>
            block_text = "C-D"
        else:
            block_text = "S-Z"
        # 找到该分组块：从 <h5>block_text</h5> 到下一个 </ul>
        pat = re.compile(
            r'(<h5 class="font-semibold mb-1">' + re.escape(block_text) + r'</h5>\s*<ul[^>]*>)(.*?)(</ul>)',
            re.DOTALL
        )
        new_entries = "\n                                ".join(entries)
        def repl(m):
            return m.group(1) + m.group(2) + new_entries + "\n                                " + m.group(3)
        html, n = pat.subn(repl, html)
        print(f"  速查索引 {grp}（块{block_text}）：插入 {n} 处，{len(entries)} 个条目")
    return html


def main():
    print("=" * 60)
    print("v1.8 新章节整合")
    print("=" * 60)
    data = load_data()
    with open(HTML, encoding="utf-8") as f:
        html = f.read()
    original = html

    print("\n[1] 插入章节 HTML...")
    html, n = insert_chapters(html, data)
    print(f"  插入 {n} 个章节")

    print("\n[2] 更新侧边栏...")
    html = update_sidebar(html, data)

    print("\n[3] 更新附录G速查索引...")
    html = update_index(html, data)

    if html == original:
        print("\n无变更（可能已整合过）。")
        return
    with open(HTML, "w", encoding="utf-8") as f:
        f.write(html)
    print("\n✓ v1.7/zh-CN.html 已更新")
    print("\n后续步骤：")
    print("  1. 更新 scripts/check_consistency.py 章节范围 36→41")
    print("  2. 更新 index.html 目录区章节数 36→41")
    print("  3. 运行 python3 scripts/check_consistency.py 验证")


if __name__ == "__main__":
    main()
