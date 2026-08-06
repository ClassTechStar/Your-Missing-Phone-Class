#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
仓库一致性检查脚本（方向 D 工程化基础）

校验内容：
  1. v1.7 最新版实际的章节/附录数量
  2. index.html 入口页宣传的章节数 / 语言数 / 附录列表是否与实际一致
  3. v1.7 侧边栏 #锚点 是否都能在正文中找到目标（断链检测）
  4. 多语言覆盖：v1.6 有但 v1.7 缺失的语言（方向 B 缺口）

仅依赖 Python 标准库。用法：python3 scripts/check_consistency.py
退出码：0=全部通过，1=发现不一致。
"""
import os
import re
import sys
import json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V17 = os.path.join(ROOT, "v1.7", "zh-CN.html")
INDEX = os.path.join(ROOT, "index.html")
MANIFEST = os.path.join(ROOT, "scripts", "languages.json")

# 中文数字 -> 阿拉伯数字（用于章节 id 解析）
CN_NUM = {
    "ling": 0, "yi": 1, "er": 2, "san": 3, "si": 4, "wu": 5,
    "liu": 6, "qi": 7, "ba": 8, "jiu": 9, "shi": 10,
}

problems = []


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def chapter_num_from_id(cid):
    """di-san-shi-si-zhang -> 34 ; di-yi-zhang -> 1 ; 失败返回 None"""
    m = re.match(r"di-(.+)-zhang(?:-|$)", cid)
    if not m:
        return None
    parts = m.group(1).split("-")
    # 处理 "san-shi-si" = 34, "shi" = 10, "yi" = 1, "shi-yi" = 11
    total = 0
    for p in parts:
        if p in CN_NUM:
            if p == "shi":
                # "shi" 单独是 10；前面有数字则 ×10
                if total == 0:
                    total = 10
                else:
                    total = total * 10
            else:
                if total >= 10:
                    total += CN_NUM[p]
                else:
                    total = CN_NUM[p]
        else:
            return None
    return total if total > 0 else None


def check_v17_counts():
    html = read(V17)
    # 所有 content-section 块的 id
    ids = re.findall(r'<div id="([\w-]+)" class="mb-10 content-section">', html)
    main_chapters = set()
    appendices = set()
    for cid in ids:
        if re.match(r"fu-lu-[a-h]$", cid):
            appendices.add(cid)
        elif cid.startswith("di-"):
            # 章节 id 可能带后缀，如 di-qi-zhang-jichu / di-er-shi-zhang-jinjie
            n = chapter_num_from_id(cid)
            if n is not None and 1 <= n <= 36:
                main_chapters.add(n)
    missing = sorted(set(range(1, 37)) - main_chapters)
    print(f"[v1.7] 主章节 1-36: 实际 {len(main_chapters)}/36", end="")
    if missing:
        print(f"  缺失: {missing}")
        problems.append(f"v1.7 缺失主章节: {missing}")
    else:
        print(" ✓")
    print(f"[v1.7] 附录 A-H: 实际 {len(appendices)}/8  {sorted(appendices)}")
    if len(appendices) != 8:
        problems.append(f"v1.7 附录数量异常: {sorted(appendices)}")
    return html, ids


def check_index(html_v17, v17_ids):
    html = read(INDEX)
    # stats 区章节数（hero 手机模型里的 "N 章" + stats 卡片数字）
    hero_m = re.search(r'<p class="text-lg font-bold mb-1">(\d+) 章</p>', html)
    stat_m = re.search(r'<p class="text-4xl[^"]*mb-2">(\d+)</p>\s*<p class="text-blue-200 text-sm">章节内容</p>', html)
    print("\n[index.html] 宣传数据:")
    if hero_m:
        ok = hero_m.group(1) == "36"
        print(f"  hero 章节数 = {hero_m.group(1)} (应为 36) {'✓' if ok else '✗'}")
        if not ok:
            problems.append(f"index.html hero 章节数={hero_m.group(1)} 应为 36")
    if stat_m:
        ok = stat_m.group(1) == "36"
        print(f"  stats 章节内容 = {stat_m.group(1)} (应为 36) {'✓' if ok else '✗'}")
        if not ok:
            problems.append(f"index.html stats 章节数={stat_m.group(1)} 应为 36")
    # 附录列表（contents 区 "附 X"）
    appx = re.findall(r'<span class="text-stone-500[^"]*">附 ([A-H])</span>', html)
    print(f"  目录附录列表 = {appx} (应为 A-H 共 8 个)")
    if len(appx) != 8 or set(appx) != set("ABCDEFGH"):
        problems.append(f"index.html 附录列表={appx} 应为 A-H")
    # 侧边栏断链检测
    anchors = set(re.findall(r'href="#([\w-]+)"', html_v17))
    body_targets = set(re.findall(r'id="([\w-]+)"', html_v17))
    broken = sorted(a for a in anchors if a not in body_targets)
    print(f"\n[v1.7] 侧边栏锚点断链检测: {len(anchors)} 个锚点", end="")
    if broken:
        print(f"  断链 {len(broken)} 个: {broken}")
        problems.append(f"v1.7 侧边栏断链: {broken}")
    else:
        print("  全部有效 ✓")


def check_languages():
    print("\n[多语言覆盖] 各版本 html 文件数:")
    versions = ["v1.7", "v1.6", "v1.5"]
    for v in versions:
        d = os.path.join(ROOT, v)
        if not os.path.isdir(d):
            continue
        n = len([f for f in os.listdir(d) if f.endswith(".html")])
        print(f"  {v}: {n} 个语言文件")
    # 读取 manifest 并校验声明文件存在性
    if not os.path.isfile(MANIFEST):
        print("  (未找到 scripts/languages.json，跳过 manifest 校验)")
        return
    with open(MANIFEST, encoding="utf-8") as f:
        manifest = json.load(f)
    print("\n[manifest] 校验声明文件存在性:")
    missing_files = []
    for ver, langs in manifest.get("versions", {}).items():
        for lang, fname in langs.items():
            path = os.path.join(ROOT, ver, fname)
            if not os.path.isfile(path):
                missing_files.append(f"{ver}/{lang}: {fname}")
    if missing_files:
        print(f"  ✗ {len(missing_files)} 个声明文件不存在:")
        for m in missing_files:
            print(f"    - {m}")
        problems.append(f"manifest 声明文件缺失 {len(missing_files)} 个")
    else:
        total = sum(len(v) for v in manifest["versions"].values())
        print(f"  ✓ 全部 {total} 个声明文件均存在")
    # v1.7 缺口：v1.6 有但 v1.7 缺失的语言
    v17 = set(manifest["versions"].get("v1.7", {}).keys())
    v16 = set(manifest["versions"].get("v1.6", {}).keys())
    gap = sorted(v16 - v17)
    print(f"\n[方向 B 缺口] v1.7 仅 {len(v17)} 种语言，相对 v1.6 缺失 {len(gap)} 种:")
    if gap:
        names = manifest["languages"]
        for g in gap:
            print(f"    - {g}  {names.get(g, {}).get('name', g)}")


def main():
    print("=" * 60)
    print("仓库一致性检查")
    print("=" * 60)
    html_v17, v17_ids = check_v17_counts()
    check_index(html_v17, v17_ids)
    check_languages()
    print("\n" + "=" * 60)
    if problems:
        print(f"发现 {len(problems)} 处不一致:")
        for p in problems:
            print(f"  ✗ {p}")
        sys.exit(1)
    print("一致性检查通过 ✓")
    sys.exit(0)


if __name__ == "__main__":
    main()
