# 工程化脚本

本目录提供仓库一致性维护工具链。所有脚本仅依赖 Python 3 标准库，无需安装依赖。

## 脚本一览

| 脚本 | 作用 | 用法 |
|------|------|------|
| `check_consistency.py` | 校验章节/附录计数、index.html 宣传数据、侧边栏断链、manifest 文件存在性、多语言缺口 | `python3 scripts/check_consistency.py` |
| `generate_index.py` | 从 `languages.json` 渲染 index.html 中标记为 `AUTOGEN:languages-{版本}` 的多语言卡片块 | `python3 scripts/generate_index.py`（写入）/ `--check`（仅校验同步） |
| `rename_to_langcode.py` | 一次性迁移脚本：将历史混乱文件名统一为 `{语言代码}.html` 并同步引用 | `--apply` 执行 / 默认 dry-run |
| `languages.json` | 多语言清单（语言元数据 + 各版本文件映射 + 卡片样式 + 翻译优先级） | 数据文件，被上述脚本读取 |

## 标准工作流

### 新增一种语言翻译

1. 把翻译好的 HTML 放到对应版本目录，命名为 `{语言代码}.html`（如 `v1.7/en.html`）。
2. 编辑 `scripts/languages.json`，在 `versions[版本]` 中添加 `"语言代码": "文件名"`。
3. （可选）在 `language_descriptions[版本]` 补充卡片底部描述文本。
4. 运行 `python3 scripts/generate_index.py` 重新生成入口页卡片。
5. 运行 `python3 scripts/check_consistency.py` 确认全绿。

### 发布新版本

1. 新建 `{版本}/` 目录，放入各语言 HTML（命名 `{语言代码}.html`）。
2. 在 `languages.json` 的 `versions` 和 `version_meta` 中添加该版本条目。
3. 在 `index.html` 中为该版本添加 `AUTOGEN:languages-{版本} START/END` 标记对。
4. 运行 `generate_index.py` 和 `check_consistency.py`。
5. 更新 `README.md` 的版本链接。

### 修改章节/附录结构

1. 编辑对应版本 HTML（新增/删除 `content-section` 块、侧边栏条目、附录G速查索引）。
2. 同步更新 `index.html` 的目录区（contents section）。
3. 运行 `check_consistency.py`——它会自动校验章节数、附录数、断链。

## CI 自动检查

`.github/workflows/ci.yml` 会在每次 push/PR 时自动运行：
- `check_consistency.py`：确保章节计数、附录、断链、manifest 文件存在性正确。
- `generate_index.py --check`：确保 index.html 的多语言卡片块与 manifest 同步（防止手改后漂移）。

任一检查失败会阻断合并。本地提交前建议先跑一遍：

```bash
python3 scripts/check_consistency.py && python3 scripts/generate_index.py --check
```

## 设计原则

- **单一数据源**：语言清单只在 `languages.json` 维护，入口页卡片由生成器渲染，避免多处手写漂移。
- **标记隔离**：`AUTOGEN` 标记之间的内容是机器生成的，标记以外的 HTML（hero、stats、目录、归档区）保持手写自由度。
- **幂等**：生成器重复运行结果一致；检查脚本无副作用。
- **零依赖**：仅用 Python 标准库，CI 环境开箱即用。
