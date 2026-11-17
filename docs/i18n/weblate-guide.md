# 翻译增量管线与 Weblate 接入指南

v1.9 把中文正文扩写到 353.8 万字后，"全量翻译 ×18 语言"不再可行。本管线把成本压到
**只翻译变更段落**，并把 18 语言从"作者一人审计"变成社区分工。

## 一、管线组成

| 组件 | 位置 | 作用 |
|------|------|------|
| 翻译记忆库（TM） | `manifest/tm/<lang>.json` | 源段哈希 → 译文段；未变内容零成本复用 |
| 术语表 | `manifest/glossary/<lang>.json` | 锁定 SoC/NPU/Passkey/eSIM 等译法，机翻与人审共用 |
| 段落级分段 | `bookkit tm`（见下） | 章节 md 按空行切块，规范化哈希为稳定段 id |
| 待译导出 | `dist/i18n/<lang>-todo.json` | 机翻 + 人审 / Weblate 的流转单元 |

## 二、日常命令

```bash
# 1) 从 v1.8 中文源稿 + 18 语翻译源稿构建 TM（一次性/翻译源更新后重跑）
python -m bookkit tm build

# 2) 查 v1.9 的增量覆盖率，并导出待译段落（每语言一份 JSON）
python -m bookkit tm report --lang ja --book source/v1.9/book.json

# 3) 机翻/人审完成后，把译文段 JSON 合并回 TM
python -m bookkit tm import --lang ja --file dist/i18n/ja-done.json
```

待译 JSON 结构：`{"lang": "ja", "tm_hits": N, "todo": M, "segments": [{"chapter", "idx", "hash", "source"}]}`。
译文回传格式：`{"<hash>": "<译文段>"}`（或包一层 `{"segments": {...}}`）。

## 三、机翻 + 人审混合流（推荐顺序）

1. `tm report` 导出待译段落（只含 TM 未命中的变更段）；
2. 机翻产出结构化中间态（建议提示词中注入 `manifest/glossary/<lang>.json` 的术语对照，
   并要求保留 `<strong>` 等行内标签与 `- ` 列表格式）；
3. 用 `scripts/extract_translations.py` 的逐章等价校验思路做结构核验（标签/列表/段落数不丢）；
4. 人工抽查语义与术语一致性（重点：SoC/NPU/安全类术语、数字与阈值）；
5. `tm import` 合并入库，翻译源稿落盘 `source/translations/<lang>/` 后走既有保真门禁。

先跑通 2–3 种语言（建议 ja/ko/en）再铺开 18 种。

## 四、Weblate 自托管接入

Weblate 组件建议按"每语言一组件"挂载仓库，文件类型选 **JSON（嵌套键）**：

```yaml
# weblate 组件配置示例（Weblate 管理端或 .wlc.yaml）
file_format: json
file_mask: manifest/glossary/*.json        # 术语表先上（表面积小、收益大）
source_language: zh-CN
new_base: ""                                # 无单语基准文件；TM 导出文件可作第二组件
```

要点：

- **第一阶段**只挂 `manifest/glossary/`（18 × 23 条），让译者先校对术语表并锁死译法；
- **第二阶段**挂 `dist/i18n/*-todo.json` 派生的分段文件（把 segments 拍平为
  `{"<hash>": ""}` 的待填模板，译者填空后 `tm import` 回收）；
- 术语检查（glossary）在 Weblate 中开启"强制术语一致"，与仓库术语表双向同步；
- 校对流程：Weblate 提交 → PR 回仓库 → CI 跑 `bookkit tm import` + 保真校验；
- 备选：不用 Weblate 时按 [CONTRIBUTING.md](../../CONTRIBUTING.md) 的
  "翻译贡献" 一节走 GitHub PR 模板流程，同样以待译 JSON 为流转单元。

## 五、译文质量护栏（对应历史事故）

- **th 语 1992 处机翻损坏**：根因是逐词翻译破坏术语与标签——术语表 + 结构校验双保险；
- **v1.7 六语言缺章**：`bookkit lint --all-versions` 的 coverage 检查已在 CI 必过；
- **lzh NUL 字节**：lint 的 nul 检查已在 CI 必过；
- 翻译源稿改完务必跑 `python scripts/extract_translations.py`（18 语逐章保真）。
