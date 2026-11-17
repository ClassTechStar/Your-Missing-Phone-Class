# source/v1.9 —— v1.9 中文版源稿（单一事实源，已回写）

2026-11-17 起，v1.9 的源稿回写完成：`v1.9/zh-CN.html`（120 个内容区块）
可由本目录完整重建，并通过 `bookkit build --verify` 逐章等价性校验
（区块 id / 目录 / 可见文本 / 逐章结构 四项全一致）。

## 目录结构

| 路径 | 说明 |
|------|------|
| `book.json` | 书籍结构（17 篇、120 章块、TOC 元数据、孤儿章节归属） |
| `chapters/` | 120 个章节正文（Markdown + 行内 HTML） |
| `parts/` | 17 篇导语 |
| `template/shell.html` | 页面骨架（head + 导航 + 侧栏 + 页脚 + 脚本） |
| `drafts/` | 历史新章草稿（原第 70–74 章规划稿，编号已并入正式篇章，仅存档） |

## 日常工作流

```bash
# 改完 source/ 后重建成品（写回 v1.9/zh-CN.html）
python -m bookkit build --book source/v1.9/book.json --out v1.9/zh-CN.html

# 等价性校验（CI 必过门禁，直接改 HTML 不回写源稿会被阻断）
python -m bookkit build --book source/v1.9/book.json --verify

# 分章化构建：121 页（章节页 + 书首页）+ sitemap + JSON-LD（页级预算 300KB/5000 标签）
python -m bookkit split --book source/v1.9/book.json --strict-budget

# 派生《给爸妈的 20 分钟速读版》（速读层合集）
python -m bookkit quick --book source/v1.9/book.json

# 如需从成品反解（仅当成品是唯一改动源时）
python -m bookkit extract --version v1.9 --out source/v1.9
```

## 章节三层结构（2026-11-17 起）

| 层 | 标记 | 说明 |
|----|------|------|
| 速读层 | `::: div .quick-read` 块（章首，`####` 小节前） | 每章 800–1500 字 + 速查表，5 分钟读完；`bookkit quick` 由此派生速读版 |
| 正文层 | 默认正文 | 现有全部内容 |
| 参考层 | 深编折叠块（JS 自动折叠长小节） | 需要深读时展开 |

tier 标记以内容为准（front matter 由 extract 再生、不承载自定义键）：
`quick-read` 块即速读层，自动折叠的长小节即参考层，其余为正文层。
新章必须带速读层；写作规范见 [CONTRIBUTING.md](../../CONTRIBUTING.md)。

## 回写时修复的结构缺陷（2026-11-17）

成品历史上由手工/脚本直改，存在多处解析脱轨缺陷（详见
`scripts/fix_v19_normalize.py`）：正文裸 `<`（第 41/63 章）、损坏残片
`<div\n</div>`（第 53/54 章间）、附录 B 缺 `</p>`、第 59 章 flex 行过早闭合、
第 31/32 章「本章小结」游离于章节块外等。这些缺陷会让 htmlparse 把其后
数十万字符吞进单个文本节点，导致反解只能识别 69/120 区块——历史上的
「整章白屏与锚点漂移」事故同族。修复脚本幂等，可随时重放自检。
