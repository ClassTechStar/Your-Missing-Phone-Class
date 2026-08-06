#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
一次性迁移脚本：统一 v1.6/v1.7 文件命名为 {语言代码}.html

背景：历史文件名风格混乱（中英混排、双点号、省略号、`he_スマホマスター` 误标日语后缀
      但内容实为希伯来语）。本脚本按 scripts/languages.json 中的版本映射重命名，
      并同步更新 README.md / index.html / languages.json / check_consistency.py 中的引用。

设计为幂等：重命名后再次运行应识别为"已完成"。
安全：先扫描所有引用，确认替换无歧义后才执行；不动 archive/ 目录。

用法：python3 scripts/rename_to_langcode.py          （预演，dry-run）
      python3 scripts/rename_to_langcode.py --apply  （实际执行）
"""
import os
import re
import sys
import json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "scripts", "languages.json")
# 需要同步替换引用的文件（在文件内容里搜旧文件名 → 替换为新文件名）
REF_FILES = [
    os.path.join(ROOT, "README.md"),
    os.path.join(ROOT, "index.html"),
    os.path.join(ROOT, "scripts", "languages.json"),
    os.path.join(ROOT, "scripts", "check_consistency.py"),
]


def load_manifest():
    with open(MANIFEST, encoding="utf-8") as f:
        return json.load(f)


def url_encode_path(name):
    """README/index.html 里中文路径用了 URL 编码（空格→%20），保留这个习惯。"""
    return name.replace(" ", "%20")


def build_plan(manifest, apply):
    """生成 (version, old_name, new_name) 计划，仅处理非 {lang}.html 形式的文件。"""
    plan = []
    for ver, langs in manifest["versions"].items():
        for lang, old in langs.items():
            new = f"{lang}.html"
            if old == new:
                continue
            old_path = os.path.join(ROOT, ver, old)
            new_path = os.path.join(ROOT, ver, new)
            if not os.path.isfile(old_path):
                # 可能已经重命名过
                if os.path.isfile(new_path):
                    continue
                print(f"  [跳过] {ver}/{old} 不存在（且 {new} 也不存在）")
                continue
            plan.append((ver, lang, old, new))
    return plan


def check_ref_conflicts(plan):
    """确保旧文件名在引用文件里只以"路径片段"形式出现，避免误伤。"""
    print("\n[2] 扫描引用文件中的旧文件名出现位置...")
    all_refs = {}
    for rf in REF_FILES:
        if not os.path.isfile(rf):
            continue
        with open(rf, encoding="utf-8") as f:
            content = f.read()
        # 同时考虑原始名和 URL 编码名
        for ver, lang, old, new in plan:
            variants = {old, url_encode_path(old)}
            hits = []
            for v in variants:
                if v and v in content:
                    hits.append(v)
            if hits:
                all_refs.setdefault((ver, old, new), []).append((rf, hits))
    for key, locs in all_refs.items():
        ver, old, new = key
        print(f"  {ver}/{old} → {new}:")
        for rf, hits in locs:
            print(f"    {os.path.relpath(rf, ROOT)}: {hits}")
    return all_refs


def apply_renames(plan, ref_map):
    print(f"\n[3] 重命名 {len(plan)} 个文件...")
    for ver, lang, old, new in plan:
        old_path = os.path.join(ROOT, ver, old)
        new_path = os.path.join(ROOT, ver, new)
        if os.path.exists(new_path):
            print(f"  [冲突] {ver}/{new} 已存在，跳过 {old}")
            continue
        os.rename(old_path, new_path)
        print(f"  ✓ {ver}/{old}  →  {new}")

    print(f"\n[4] 替换引用文件中的路径...")
    for rf in REF_FILES:
        if not os.path.isfile(rf):
            continue
        with open(rf, encoding="utf-8") as f:
            content = f.read()
        original = content
        for ver, lang, old, new in plan:
            # 替换原始名和 URL 编码名两种形式
            content = content.replace(old, new)
            content = content.replace(url_encode_path(old), new)
        if content != original:
            with open(rf, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✓ 更新 {os.path.relpath(rf, ROOT)}")
        else:
            print(f"  - {os.path.relpath(rf, ROOT)} 无需变更")


def verify_no_residual(plan):
    print(f"\n[5] 验证无残留旧名...")
    residual = []
    for rf in REF_FILES:
        if not os.path.isfile(rf):
            continue
        with open(rf, encoding="utf-8") as f:
            content = f.read()
        for ver, lang, old, new in plan:
            if old in content or url_encode_path(old) in content:
                residual.append((rf, old))
    if residual:
        print(f"  ✗ 发现 {len(residual)} 处残留:")
        for rf, old in residual:
            print(f"    {os.path.relpath(rf, ROOT)}: {old}")
        return False
    print("  ✓ 无残留旧名")
    return True


def main():
    apply = "--apply" in sys.argv
    print("=" * 60)
    print(f"文件名规范化迁移  ({'APPLY' if apply else 'DRY-RUN'})")
    print("=" * 60)
    manifest = load_manifest()
    plan = build_plan(manifest, apply)
    print(f"\n[1] 待重命名 {len(plan)} 个文件:")
    for ver, lang, old, new in plan:
        print(f"  {ver}/{lang}: {old}  →  {new}")
    if not plan:
        print("\n无需迁移，文件名已是规范形式。")
        return
    ref_map = check_ref_conflicts(plan)
    if not apply:
        print("\n[DRY-RUN] 未执行实际重命名。加 --apply 参数执行。")
        return
    apply_renames(plan, ref_map)
    ok = verify_no_residual(plan)
    print("\n" + "=" * 60)
    print("迁移完成" if ok else "迁移完成但存在残留，请手动检查")
    print("=" * 60)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
