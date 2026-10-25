# 工程工具链 `bookkit`

> 本文件描述的工具链**已落地可用**（Python 3 标准库，零第三方依赖）。历史上的 `scripts/check_consistency.py`、
> `scripts/generate_index.py`、`scripts/languages.json` 已在提交 `7f58c0c` 删除；其能力由 `bookkit/` 包与
> `manifest/languages.json` 取代，本节与之对齐。

## 一、一条命令看清全貌

```bash
python -m bookkit --version          # bookkit 1.0.0
python -m bookkit lint --all-versions # v1.5–v1.8 + archive：结构/锚点/目录/版本串/lang/NUL/残留字/覆盖率
python -m bookkit check --claims      # README 与 index.html 的宣称值 ↔ 真实内容
python -m bookkit build --verify      # source/ → HTML，并与已发布成品逐章比对
```

## 二、目录职责

| 路径 | 内容 | 谁写 |
| --- | --- | --- |
| `manifest/languages.json` | **单一数据源**：语言元数据（`html_lang`/`dir`/`script`/`flag`/`gradient`）、各版本检查等级与期望区块数、入口页卡片样式、每语言书名 | 手工维护 |
| `source/book.json` | 书籍结构：篇/章顺序、目录元数据、孤儿章节归属、篇 `open_tag` | `bookkit extract` 生成 |
| `source/chapters/NN-<id>.md` | 单章正文（Markdown + 行内 HTML），84 章 | `extract` 生成 / 手工编辑 |
| `source/parts/NN-<id>.md` | 各篇导语，11 篇 | 同上 |
| `source/template/shell.html` | 页面骨架：`<head>`、导航、侧栏容器、页脚、脚本；含 `{{TOC}} {{BODY}} {{TITLE}} {{VERSION}} {{CH_COUNT}} {{APP_COUNT}}` 占位 | `extract` 生成 |
| `source/legacy/` | 三份历史近重复源稿（只读留档），差异分析见 `source/legacy/MERGE-REPORT.md` | 归档 |
| `bookkit/` | 工具链本体：`htmlparse` / `markdown` / `extract` / `build` / `lint` / `claims` / `index` / `i18n` / `release` / `cli` | 代码 |
| `dist/` | 构建与发布产物（不入库，见 `.gitignore`） | `build` / `release` |

## 三、章节源稿的 Markdown 方言

块级结构用 Markdown，行内格式原样保留 HTML——这是为了让 19 种语言的既有译文**零损毁**地进入源稿体系。

```markdown
---
id: di-san-shi-qi-zhang
num: "37"
part: ai-biancheng
nav: 第三十七章：范式革命——从"写代码"到"指挥AI写代码"
toc: default          # default | sub（二级锚点，如"附：安卓手机内存拓展解析"）
kind: chapter         # chapter | supplement | appendix | conclusion
---

### 第三十七章：范式革命——从"写代码"到"指挥AI写代码"

{class="chapter-intro mb-4"}
恭喜你，翻开这本书的你……<strong>行内 HTML 原样保留</strong>。

#### 一、Vibe Coding 的诞生

::: info-box .rounded-lg .p-4 .mt-4
<p>容器用 <code>:::</code> 指令，属性以 <code>.类名</code> 书写</p>
:::

:::inline div .code-head
<span>PRD.md</span><span class="dots">···</span>
:::

```html
<!-- 表格、SVG 等复杂子树整体保真，构建时原样输出 -->
```
```

规则要点：

1. **属性行** `{class="…" id="…" style="…"}` 作用于紧随其后的段落/标题/列表；`class` 等于该标签默认值时可省略。
2. **容器指令** `::: tag .cls1 .cls2 … :::`；`:::inline` 表示子节点全为行内元素，整行原样输出。
3. **`html` 代码块** 表示"原样 HTML"，构建时逐字输出——用于表格、SVG、异常嵌套列表等。
4. 其余代码块渲染为 `<pre>`，内容逐字保留（示例代码中的 `<Boolean>` 不会被解析）。
5. 标题层级 `###`→`<h3>`（默认类 `text-xl font-bold …`），`####`→`<h4>`，`#####`→`<h5>`。

## 四、子命令

| 命令 | 作用 | 关键参数 |
| --- | --- | --- |
| `extract` | 成品 HTML → `source/`（先断言解析器字节无损往返，再反解） | `--version` `--lang` `--out` `--dry-run` |
| `build` | `source/` → 单文件 HTML（目录、版本徽章、书名由数据推导） | `--lang` `--out` `--verify` `--book` |
| `lint` | 全版本一致性；等级由 `manifest.versions.<v>.checks` 决定（error/warn/off） | `--all-versions` `--version-dir` `--fail-on` |
| `check` | README/index 宣称值校验；`--index` 追加 AUTOGEN 漂移检测 | `--claims` `--index` |
| `index` | 按 manifest 重生成 `index.html` 的 `AUTOGEN:languages-*` 块与统计区 | `--check`（只比对不写盘） |
| `i18n` | 翻译覆盖率报告（缺章清单、目录缺项、状态） | `--report coverage.md` |
| `release` | 发布清单：每语言 HTML 的 SHA-256 + 包名 + `SHA256SUMS` | `--release-version` `--out` |

全部子命令支持 `--root`（仓库根）、`--json`（机器可读）、`--fail-on {error,warn,never}`。

## 五、CI 门禁（`.github/workflows/ci.yml`）

| Job | 步骤 | 阻断 |
| --- | --- | --- |
| `lint` | `lint --all-versions`；`check --claims`；`index --check`；`i18n --report` | 前三项阻断，覆盖率报告仅出件 |
| `build` | `build --verify`（与成品等价）；两次构建字节一致；`book.json` 与章文件一一对应 | 阻断 |

覆盖的勘误项：ERR-01/07/12（覆盖率）、ERR-02/06（锚点与目录）、ERR-03（NUL）、ERR-04（版本串）、
ERR-05/09/21（宣称值）、ERR-13（lang）、ERR-16（CI 盲区）、ERR-10（源稿缺失）。

## 六、日常操作

```bash
# 修改某章正文
$EDITOR source/chapters/37-di-san-shi-qi-zhang.md
python -m bookkit build --verify      # 结构与文本等价性（改了正文会显示差异章节）
python -m bookkit lint                # 最新版本全项检查

# 新增一种语言
# 1) manifest/languages.json 的 languages 增加条目（html_lang/dir/script/flag/gradient/priority）
# 2) 放入 vX/<code>.html
python -m bookkit index               # 入口页卡片自动补上
python -m bookkit check --claims      # README 语言表需同步，否则报错

# 发布前
python -m bookkit release --release-version v1.8   # → dist/release/
```

## 七、设计原则（延续并落地）

- **单一数据源**：语言与卡片在 `manifest`，章节在 `source/`，HTML 由构建产生；README 与 `index.html` 的每个数字都能被脚本验证。
- **标记隔离**：`AUTOGEN:languages-*` 之间由机器生成，标记之外保持手写自由度。
- **幂等**：`extract`/`build`/`index` 重复运行结果一致（CI 用两次构建字节比对锁死）。
- **零依赖**：只用 Python 标准库，GitHub Actions 开箱即用。
- **保真优先**：无法安全转成 Markdown 的子树一律以 `html` 代码块原样保留，宁可少转，不可改字。

## 八、已知边界

- `bookkit build` 目前只覆盖**简体中文源稿**（`source/` 为 zh-CN 单一事实源）；其余 18 种语言仍以
  `v1.8/<lang>.html` 成品为准，由 `lint` 与 `i18n` 守护一致性。多语言构建（`source/translations/<lang>/`）
  属下一步，接口已在 `manifest` 预留 `language_descriptions`。
- `release` 只生成待打包清单与校验和；APK 打包仍依赖外部 Android 工具链，不在本仓库内。
- 历史版本（v1.5–v1.7）按"只修元数据、不重排内容"的归档策略处理，`lint` 对它们使用 warn 级门槛。

## 九、多语言章节标题与 PDF 管线（2026-10 增补）

| 脚本 | 作用 |
| --- | --- |
| `python scripts/inventory_titles.py [版本...]` | 全量体检：84 节 h3 的章前缀分类（title/supplement/corrupt），修完应为全 0（v1.7/lzh.html 除外，已知 NUL 损坏） |
| `python scripts/analyze_numbering.py v1.8` | 各文件章编号样式分布（多数派应唯一） |
| `python scripts/repair_headings.py [--apply] [版本...]` | 损坏标题回填（v1.6/v1.5 → 侧栏兜底）+ 编号统一 + 逐槽校验；翻译覆盖表在 `translation_overrides.py` |
| `python scripts/verify_pdf_toc.py [语言...]` | 校验 `latex/<lang>/main.toc` 章级目录风格唯一 |
| `bash scripts/build_pdfs.sh <语言...>` | `bookkit latex` 生成 + XeLaTeX 两遍编译（MiKTeX） |

编号约定（勿混用）：非中文语言一律阿拉伯数字（词形数字→数字）；**日语统一汉字数字**（第零章…第六十九章，
对齐中文源稿）；zh 系保持汉字。语言基准用同版本 `zh-CN.html`（v1.5/v1.6 书结构不同）。

`bookkit latex` 行为（2026-10 增补）：篇标题取自 HTML 各语言 `<section id>` 的 h2；书名取自
`manifest/languages.json` 的 `language_descriptions`；babel 连字（de/ru/el/fr/es/it/pt/id/vi）+
`\shorthandoff`（de/fr）；`\emergencystretch=3em` 与代码内 `.-_/-` 断行兜底长复合词/长标识符溢出。

## 十、门户 / 测验 / MCP / 冒烟（2026-10-25 增补）

| 命令 | 作用 |
| --- | --- |
| `python scripts/extract_translations.py` | 18 语言翻译反解到 `source/translations/<lang>/` 并逐章验证（应 18/18 全保真） |
| `python scripts/web_smoke.py` | Playwright 浏览器冒烟：20 页 console 零报错 + 侧栏锚点全解析 + h3 计数（曾抓到折叠丢 id 的真 bug） |
| `python scripts/gen_cover.py` | 生成传播封面三件套（OG 1200×630 / 小红书 1080×1440 / B 站 1920×1080），HTML 排版截图而非 AI 生图；改章数或版本号后要重跑 |
| `python scripts/sync_site.py` | 把 `v1.8/zh-CN.html` + PWA 资产 + 分享卡片 `cover-og.png` 同步到站点仓库（相对路径降一级）；`og:image` 指向站点根，漏拷就没有缩略图 |
| `python mcp/server.py` | 本书结构 MCP 服务器（list_parts / list_chapters / get_chapter / search / stats），`.mcp.json` 已配置 |
| `quiz.html` + `quiz/zh-CN.json` | 章节自测答题页与题库（基础篇 8 章 24 题，题库按语言扩展） |

CI 的 `audit` job 已包含 html_audit / verify_pdf_toc / extract_translations / web_smoke 四道闸门。
