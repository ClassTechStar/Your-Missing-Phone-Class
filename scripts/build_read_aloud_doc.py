#!/usr/bin/env python3
"""build_read_aloud_doc.py — 生成朗读体检问题清单（方案 §6.3）。

方案 §6.3 的原话：

    1. 每章终稿用 TTS 朗读（或自己出声读）；
    2. 边听边标记：拗口、喘不上气、听了走神的三处，必改；
    3. 改完重听一遍，通过才进发布分支。

**这是最后一道无法自动化的门禁，人的语感是终点裁判。**
但 120（v1.9）+ 84（v1.8）+ 1512（18 语译文）= 1716 章逐章人工朗读
不是一次会话能做完的。所以做法是：

1. 把三项变成**可检测的信号**（scripts/voice_read_test.py）；
2. 阈值按**每种语言自身的分布**定（不是拍脑袋）；
3. 机器标出可疑处 → 逐条改 → 改完复测；
4. 改不动的（译文里需要母语判断的）**如实留在清单上**，不假装修完了。

用法：
  py -3 scripts/build_read_aloud_doc.py
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "deai" / "READ_ALOUD.md"

SOURCES = [
    ("v1.9 中文（120 章）", ROOT / "state" / "read_v19.json",
     ROOT / "state" / "read_v19_after.json"),
    ("v1.8 中文（84 章）", ROOT / "state" / "read_v18.json",
     ROOT / "state" / "read_v18_after.json"),
    ("18 语译文（1512 章）", ROOT / "state" / "read_all_tr_before.json",
     ROOT / "state" / "read_all_tr.json"),
]

KIND_DESC = {
    "R1": ("喘不上气", "一口气读不完的无标点连续段，或一句里塞了太多分句"),
    "R2": ("拗口", "流程箭头串、连续顿号、同词重复、括号嵌套、中英数混排"),
    "R3": ("听了走神", "段内连续几句长度几乎相同、连续同开头、一句里抽象词堆叠"),
}


def main() -> int:
    lines: list[str] = []
    lines.append("# 朗读体检问题清单（方案 §6.3）\n")
    lines.append("> 这一页是**机器标出的可疑处**，不是判决书。")
    lines.append("> 方案 §6.3 说得很清楚：人的语感是终点裁判。\n")
    lines.append("> 生成方式：`py -3 scripts/build_read_aloud_doc.py`；")
    lines.append("> 检测器：`scripts/voice_read_test.py`；原始数据：`state/read_*.json`。\n")

    lines.append("## 一、怎么测的\n")
    lines.append("三项信号各有可复跑的判据：\n")
    lines.append("| 编号 | 类别 | 判据 |")
    lines.append("| --- | --- | --- |")
    for rid, (name, desc) in KIND_DESC.items():
        lines.append(f"| **{rid}** | {name} | {desc} |")
    lines.append("")
    lines.append("**阈值按每种语言自身的分布定**，不是拍脑袋。实测全书每种语言"
                 "「无标点连续段」长度的 P99.5（超过它，才是这门语言里读起来真的别扭的少数句子）：\n")
    lines.append("| 语言 | P99.5 | 采用阈值 | | 语言 | P99.5 | 采用阈值 |")
    lines.append("| --- | --- | --- | --- | --- | --- | --- |")
    rows = [
        ("中文（v1.9/v1.8）", 27, 45), ("繁体 / 粤语 / 文言", "24-27", 45),
        ("日文", 43, 45), ("韩文", 44, 46),
        ("英文", 134, 135), ("俄文", 137, 140), ("意大利文", 151, 155),
        ("葡萄牙文", 146, 150), ("西班牙文", 144, 148), ("法文", 152, 155),
        ("德文", 159, 160), ("希腊文", 180, 185), ("阿拉伯文", 228, 230),
        ("希伯来文", 107, 110), ("泰文", 348, 350),
        ("印尼文", 134, 138), ("马来文", 140, 145),
    ]
    half = (len(rows) + 1) // 2
    for i in range(half):
        a = rows[i]
        b = rows[i + half] if i + half < len(rows) else ("", "", "")
        lines.append(f"| {a[0]} | {a[1]} | {a[2]} | | {b[0]} | {b[1]} | {b[2]} |")
    lines.append("")
    lines.append("> 中文用 45 而不是 27：中文的段长单位是「字数」，西文是「字符数」，两者不可直接比。\n")

    lines.append("## 二、问题点总账\n")
    lines.append("| 语料 | 章数 | 改前 R1 | 改前 R2 | 改前 R3 | 改前合计 | 改后合计 | 降幅 |")
    lines.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
    for label, path, after_path in SOURCES:
        if not path.is_file():
            continue
        rows = json.loads(path.read_text(encoding="utf-8"))
        c = defaultdict(int)
        for r in rows:
            for i in r["issues"]:
                c[i["id"]] += 1
        before = sum(c.values())
        after_txt = "—"
        delta_txt = "—"
        if after_path and after_path.is_file():
            arows = json.loads(after_path.read_text(encoding="utf-8"))
            ac = defaultdict(int)
            for r in arows:
                for i in r["issues"]:
                    ac[i["id"]] += 1
            after = sum(ac.values())
            after_txt = f"**{after}**"
            delta_txt = f"−{(1 - after / before) * 100:.0f}%" if before else "—"
        lines.append(f"| {label} | {len(rows)} | {c['R1']} | {c['R2']} | {c['R3']} | "
                     f"**{before}** | {after_txt} | {delta_txt} |")
    lines.append("")

    lines.append("## 三、逐语种剩余问题点（18 语译文，改造后）\n")
    tr = ROOT / "state" / "read_all_tr.json"
    if tr.is_file():
        rows = json.loads(tr.read_text(encoding="utf-8"))
        per = defaultdict(lambda: defaultdict(int))
        chapters = defaultdict(int)
        for r in rows:
            parts = Path(r["path"]).parts
            lg = parts[parts.index("translations") + 1] if "translations" in parts else "?"
            chapters[lg] += 1
            for i in r["issues"]:
                per[lg][i["id"]] += 1
        lines.append("| 语言 | 章数 | R1 | R2 | R3 | 合计 | 每章 |")
        lines.append("| --- | --- | --- | --- | --- | --- | --- |")
        for lg in sorted(per, key=lambda x: -sum(per[x].values())):
            t = sum(per[lg].values())
            lines.append(f"| {lg} | {chapters[lg]} | {per[lg]['R1']} | {per[lg]['R2']} | "
                         f"{per[lg]['R3']} | {t} | {t / max(chapters[lg], 1):.1f} |")
        lines.append("")

    lines.append("## 四、一处被否决的机械修复（记录下来，免得以后重踩）\n")
    lines.append("朗读体检最初打算配一个脚本，把「A → B → C → D → E」这种流程箭头串"
                 "机械地改成编号列表（箭头是通用符号，编号列表是通用排版，理论上对所有语言成立）。\n")
    lines.append("**实测否决**：本书的箭头链大多是**嵌在句中的操作路径**"
                 "（`【设置】→【更多设置】→【内存】`），后面还跟着正文。"
                 "加上四道护栏后只剩 4 处候选，逐条看下来**全部不安全**：\n")
    lines.append("- 把 `旧机进：微信 → 我 → 设置 → …` 拆开，会在编号列表项里再嵌一个编号列表，"
                 "Markdown 列表结构直接坏掉；\n"
                 "- 把 `…→【关于手机】或【运存与存储】里，名字也可能叫…` 拆开，"
                 "后半句正文会被甩到列表外面；\n"
                 "- `路线：第十一章 → 第三十一章 → …` 是**章节导航表**，拆成列表反而更难一眼扫完。\n")
    lines.append("结论：**这一类只能靠人判断**。方案 §6.3 说的「人的语感是终点裁判」，"
                 "在流程箭头这件事上表现得最具体。相关工具已删除，不留在仓库里当陷阱。\n")

    lines.append("## 五、这一轮改了什么、还剩什么\n")
    lines.append("### 已改\n")
    lines.append("- **v1.9 中文（120 章）**：R1/R2/R3 逐条改，重点是把「段内三句等长」的"
                 "机器节奏打散（把其中一句拆出短句单独成段）。\n"
                 "- **v1.8 中文（84 章）**：同上一套，另加证据注入与附录 E 制作说明。\n"
                 "- **18 语译文**：跑了**语言无关的结构层**手术（破折号降频 10779 处、"
                 "列表收尾统一 357 处、段首连接词去重），以及标题模板破除。\n")
    lines.append("### 还剩（如实交代）\n")
    lines.append("- **18 种译文的 R1/R3**：这些改动需要母语判断（在哪里断句、哪句该改短、"
                 "哪个词换成大白话），本轮没有做。清单在上面，逐条可查。\n"
                 "  译文本来的分级就是 ★★（机翻 + 抽查，质量不承诺），"
                 "见 `languages.html`。\n"
                 "- **TTS 真人朗读**：本轮**没有**真的用 TTS 播放并逐段听。"
                 "检测器只能标出「最可能读不顺」的地方，"
                 "真正的语感判断仍然要人来下结论。\n")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[+] 已生成 {OUT.relative_to(ROOT)}（{len(lines)} 行）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
