#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
入口页生成器（方向 D-2）

从 scripts/languages.json 渲染 index.html 中标记为
  <!-- AUTOGEN:languages-{版本} START --> ... <!-- AUTOGEN:languages-{版本} END -->
之间的多语言卡片块。标记以外的内容（hero、stats、目录、归档区等）保持手写不动。

新增/补齐某语言时：
  1. 在 languages.json 的 versions[版本] 中登记 lang->file
  2. （可选）在 language_descriptions[版本] 补卡片描述
  3. 运行 python3 scripts/generate_index.py
  4. 运行 python3 scripts/check_consistency.py 复核

用法：
  python3 scripts/generate_index.py          （默认：原地写入 index.html）
  python3 scripts/generate_index.py --check  （仅校验生成结果是否已同步，不写文件）
"""
import os
import sys
import json
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "index.html")
MANIFEST = os.path.join(ROOT, "scripts", "languages.json")

# 卡片渐变背景色（按语言代码分配，保证视觉差异）
LANG_GRADIENTS = {
    "zh-CN": "from-red-50 to-red-100",
    "zh-TW": "from-amber-50 to-amber-100",
    "yue":   "from-pink-50 to-pink-100",
    "en":    "from-blue-50 to-blue-100",
    "ko":    "from-violet-50 to-violet-100",
    "ja":    "from-rose-50 to-rose-100",
    "ru":    "from-sky-50 to-sky-100",
    "it":    "from-green-50 to-green-100",
    "pt":    "from-emerald-50 to-emerald-100",
    "es":    "from-yellow-50 to-yellow-100",
    "fr":    "from-indigo-50 to-indigo-100",
    "de":    "from-gray-50 to-gray-100",
    "ar":    "from-lime-50 to-lime-100",
    "he":    "from-teal-50 to-teal-100",
    "th":    "from-fuchsia-50 to-fuchsia-100",
    "vi":    "from-teal-50 to-teal-100",
    "id":    "from-orange-50 to-orange-100",
    "ms":    "from-cyan-50 to-cyan-100",
    "el":    "from-blue-50 to-indigo-100",
    "lzh":   "from-stone-50 to-stone-100",
}
DEFAULT_GRADIENT = "from-gray-50 to-gray-100"


def load_manifest():
    with open(MANIFEST, encoding="utf-8") as f:
        return json.load(f)


def render_card(ver, lang, fname, manifest):
    """渲染单张语言卡片 HTML。"""
    meta = manifest["languages"].get(lang, {})
    name = meta.get("name", lang)
    native = meta.get("native", lang)
    flag = meta.get("flag", "🌐")
    vmeta = manifest["version_meta"][ver]
    border = vmeta["card_border"]
    tag_text = vmeta["lang_tag_text"]
    tag_class = vmeta["lang_tag_class"]
    gradient = LANG_GRADIENTS.get(lang, DEFAULT_GRADIENT)
    # 卡片底部描述：优先 language_descriptions，否则用 native 名
    desc = manifest.get("language_descriptions", {}).get(ver, {}).get(lang, native)
    return f'''                <a href="{ver}/{fname}" class="lang-card block bg-gradient-to-br {gradient} {border} rounded-xl p-5 hover:shadow-lg">
                    <div class="flex items-center gap-3 mb-2">
                        <span class="text-3xl">{flag}</span>
                        <div>
                            <h4 class="font-bold text-dark">{native}</h4>
                            <p class="text-xs {tag_class} font-semibold">{tag_text}</p>
                        </div>
                    </div>
                    <p class="text-sm text-gray-600">{desc}</p>
                </a>'''


def render_block(ver, manifest):
    """渲染某个版本的整块（badge + grid + 卡片）。"""
    vmeta = manifest["version_meta"][ver]
    langs = manifest["versions"][ver]
    cards = "\n\n".join(render_card(ver, lang, fname, manifest)
                        for lang, fname in langs.items())
    return f'''            <div class="mb-12 fade-in">
                <div class="text-center mb-8">
                    <span class="inline-block px-4 py-1.5 {vmeta['badge_color']} rounded-full text-sm font-semibold">
                        <i class="fas {vmeta['badge_icon']} mr-1"></i>{vmeta['badge_text']}
                    </span>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">

{cards}

                </div>
            </div>'''


def replace_block(html, ver, new_block):
    """替换 START/END 标记之间的内容。标记行可能含额外说明文字。
    用函数式 replacement 避免 \1/\2 转义陷阱。"""
    pattern = re.compile(
        r"(<!-- AUTOGEN:languages-" + re.escape(ver) + r" START[^>]*-->)"
        r".*?"
        r"(<!-- AUTOGEN:languages-" + re.escape(ver) + r" END[^>]*-->)",
        re.DOTALL,
    )

    def repl(m):
        return m.group(1) + "\n" + new_block + "\n            " + m.group(2)

    new_html, n = pattern.subn(repl, html)
    if n == 0:
        print(f"  [警告] 未找到 {ver} 的 AUTOGEN 标记，跳过（需手动加标记）")
        return html, 0
    return new_html, n


def main():
    check_only = "--check" in sys.argv
    print("=" * 60)
    print(f"入口页生成器  ({'CHECK' if check_only else 'WRITE'})")
    print("=" * 60)
    manifest = load_manifest()
    with open(INDEX, encoding="utf-8") as f:
        html = f.read()
    original = html
    # 渲染顺序：v1.7 → v1.6 → v1.5（与 index.html 中标记出现顺序一致）
    for ver in ["v1.7", "v1.6", "v1.5"]:
        block = render_block(ver, manifest)
        html, n = replace_block(html, ver, block)
        status = "✓ 渲染" if n else "- 跳过(无标记)"
        print(f"  {ver}: {status} ({len(manifest['versions'][ver])} 种语言)")
    if html == original:
        print("\n无变更。")
        return
    if check_only:
        print("\n[CHECK] index.html 与 manifest 不同步，请运行 generate_index.py")
        sys.exit(1)
    with open(INDEX, "w", encoding="utf-8") as f:
        f.write(html)
    print("\n✓ index.html 已更新")


if __name__ == "__main__":
    main()
