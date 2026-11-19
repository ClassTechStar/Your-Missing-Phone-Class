#!/usr/bin/env python3
"""insert_making_note.py — 在附录 E 插入「这本书是怎么做出来的」一节。

这是方案 §8.1 的制作说明草稿。核心是**诚实披露**：
仓库根目录本来就有 `.claude/`，藏着 AI 参与才是雷，主动说清是加分项。

插入位置：在「三、我们怎么保证内容靠谱」之后。
**后续小节序号与正文里的「第X节」引用一并顺延**（十→十一、九→十…），
倒序改，避免把刚改过的号改两遍。

用法：
  py -3 scripts/insert_making_note.py --dry-run
  py -3 scripts/insert_making_note.py --fix
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "source" / "v1.9" / "chapters" / "115-fu-lu-e.md"

NEW_SECTION = """#### 四、这本书是怎么做出来的

这一节回答一个迟早会被问到的问题：**这本书是 AI 写的吗？**

答案是：**部分是。** 而且这件事没什么好藏的——本书的仓库里有一整个自动化写作管线，
工具链是公开的。你如果只拿到一本读起来很顺的书，却不知道它怎么来的，那才是问题。

所以我们把分工写清楚。

##### 谁做了什么

| 环节 | 谁做的 |
| --- | --- |
| 选题、章节结构、学习路径设计 | 人。哪些内容值得写、先写什么、给谁看，是作者定的。 |
| 初稿生成 | AI 辅助。120 个内容区块的初稿，由 AI 按结构与体例生成。 |
| 事实核对与路径登记 | 人 + 脚本。路径逐条登记进 `path_db.json`，与正文对账。 |
| 章节重写与声音统一 | 人。12 个锚章节逐句重写，其余章节向锚对齐。 |
| HTML / PDF 排版、翻译、质检 | 全自动。`bookkit` 一条流水线，产出可逐字校验。 |

##### 哪些章是人写的

这一版里，下面这些章节是**作者逐句重写**的，它们是全书的声音基准：

- **第零章（序言）**——第一印象，不能是机器腔
- **第十九章（手机故障排查）**——404 页把读者往这里导，质损直接伤信任
- **第二十章（数据备份与迁移）**——读者最怕的是"东西没了"
- **第三十二章（手机安全急救）**——出事的时候，写错一个字可能害死人
- **第九十四章（心率、血氧与慢病管理）**——涉及医学，最怕给出诊断结论
- **第二十七章（给爸妈调手机）**——作者最有感情的部分
- **结语**——一本书的最后一句话，值得人自己写

其余章节由 AI 生成初稿、人工审校与增补。**你读到的每一章都是人改过的**，
但改的深度不一样，我们如实标出来。

##### 操作路径是怎么保证的

手机 UI 每年换一次，AI 的训练数据是滞后的——"连点七次版本号"这类路径，
三年前是对的，现在可能就不对了。所以这一版做了三件事：

1. 每章开头加**版本锚点**：本章路径按 iOS 18.x / HarmonyOS 5.x / Android 15 核对，
   什么时候核对的、你的机型不一样怎么办，都写明。
2. 路径登记进 **`path_db.json`**（本书的单一真源），正文里的路径可以逐条查、逐条巡检。
3. 你报路径错，**改的是路径库**，不是把正文换个说法了事。

需要说清楚的是：**全书没有做逐台设备的逐条实机复测。** 版本锚点声明的是核对基准，
不是"每条路径都有人按过"。这条线我们不越——夸大会害到照着做的读者。

##### 多语言版本不是同样可靠的

中文版是人工审校版。其余 18 种语言是机器翻译 + 抽查，质量不承诺。
分级表在 <a href="languages.html">languages.html</a>，每种语言标了实际投入。
假装 19 种语言同样完美，是这本书最不该有的毛病。

##### 错了怎么办

勘误页 <a href="errata.html">errata.html</a>公开记录：已经确认并修好的问题、
还在修订中的问题、每一条的修订版本号。提 Issue 或直接找 QQ 群 1074995524 都可以。

我们的承诺：**勘误提交后中位 7 天内给出回应，每季度一个修订版。**

##### 署名

作者：**missile / ClassTechStar**（QQ 群 1074995524，B 站 @ClassTechStar）。
健康篇的医学审校尚在推进中，审校人到位后会署名——**在署名之前，这一篇请当参考，别当依据。**

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-quote-left mr-2"></i>为什么选择写出来

藏着一件不难，读者迟早会发现——仓库是公开的，管线是公开的。
写出来不难，因为这句话本身就在说清楚一件更重要的事：

**这本书的质量不靠"保证完美"，靠"每一步都说得清、错了改得动"。**

一句机器腔的空话，比一段有署名的承认糟糕得多。
:::

"""

CN = "一二三四五六七八九十"
# 倒序：十→十一、九→十、八→九、七→八、六→七、五→六、四→五
RENUMBER = [("十", "十一"), ("九", "十"), ("八", "九"), ("七", "八"),
            ("六", "七"), ("五", "六"), ("四", "五")]


def renumber(text: str) -> str:
    # 小节标题
    for old, new in RENUMBER:
        text = re.sub(rf"^#### {old}、", f"#### {new}、", text, flags=re.M)
    # 正文里的「第X节」引用
    for old, new in RENUMBER:
        text = text.replace(f"第{old}节", f"第{new}节")
    return text


def main() -> int:
    ap = argparse.ArgumentParser(description="插入附录 E 制作说明")
    ap.add_argument("--fix", action="store_true")
    args = ap.parse_args()

    text = TARGET.read_text(encoding="utf-8")
    if "这本书是怎么做出来的" in text:
        print("[i] 制作说明已存在，跳过")
        return 0

    # 先顺延旧小节（四→五 … 十→十一），再把新的一节插到"五、"之前
    text = renumber(text)
    anchor = "#### 五、这本书的使用许可"
    if anchor not in text:
        print(f"[!] 找不到插入锚点：{anchor}", file=__import__("sys").stderr)
        return 2
    i = text.index(anchor)
    new_text = text[:i] + NEW_SECTION + text[i:]

    # 校验：章节号不重不漏
    heads = re.findall(r"^#### ([一二三四五六七八九十]+)、", new_text, re.M)
    expect = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十", "十一"]
    ok = heads == expect
    print(f"[i] 小节序号：{heads}")
    if not ok:
        print(f"[!] 序号不连续，期望 {expect}")
        return 2

    # 校验：正文引用里没有指向不存在的小节号
    refs = sorted(set(re.findall(r"第([一二三四五六七八九十]+)节", new_text)))
    bad = [r for r in refs if r not in heads]
    if bad:
        print(f"[!] 引用了不存在的小节号：{bad}")
        return 2

    if args.fix:
        TARGET.write_text(new_text, encoding="utf-8")
        print(f"[+] 已写入 {TARGET.name}")
    else:
        print(f"[i] dry-run，未写回（将插入 {len(NEW_SECTION)} 字符）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
