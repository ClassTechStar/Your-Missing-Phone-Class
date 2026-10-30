---
name: phoneclass-maintainer
description: |
  《你缺失的那门手机课》仓库维护手册：源稿体系、编号约定、质检闸门、发布流程。
  当任务涉及修改本书内容/翻译/标题/结构、构建 HTML/PDF、跑质检、发 Release 时使用。
  触发词：手机课仓库、bookkit、章节标题、翻译源稿、html_audit、pdf_audit、
  v1.8/v1.9、latex 重排、Release 资产。
metadata:
  maintainer: ClassTechStar
---

# 《你缺失的那门手机课》维护手册

单一事实源：**源稿（Markdown）→ 构建 → 成品 HTML/PDF**。改内容永远改源稿，不要手术成品。

## 一、仓库结构与数据流

```
source/chapters/*.md + parts/*.md + book.json   ← zh-CN 源稿（事实源）
source/translations/<lang>/…                    ← 18 语言翻译源稿（与 v1.8 成品逐章等价）
      │ python -m bookkit build [--book …]               生成 HTML
      │ python -m bookkit latex --lang X --out latex/X   生成 LaTeX（XeLaTeX×2 编译）
      ▼
v1.8/<lang>.html（成品，与 build --verify 逐章等价）
manifest/languages.json  ← 语言元数据/版本门禁/卡片（单一数据源）
```

- 主分支**只保留 v1.8**；v1.5–v1.7 HTML 在 Release `html-archive`，v1.3/v1.4 在 `legacy-html-archive`。
- 根目录 `你缺失的那门手机课V1.9Fixed.html` 必须与 `v1.8/zh-CN.html` 字节一致（lint source_sync 门禁）。

## 二、编号约定（勿混用！）

- **非中文语言**：章号一律阿拉伯数字（Глава 27、الفصل 23、פרק 5…）。
- **日语 ja**：v1.6+ 统一**汉字数字**（第零章…第六十九章）；v1.5 ja 例外保持数字。
- **zh 系**：汉字数字不动。
- 章内小节（h4）编号与 zh-CN 同槽位一致；zh 的原生跳号（如 ch15 缺三、ch58 的"零、"开头）按 zh 基准。
- 附录顺序 A–H；"章内附"前缀各语言统一（Anhang zu Kapitel N → Kapitel N Anhang 等）。

## 三、常用命令

```bash
python -m bookkit lint                    # 结构/锚点/目录/lang/NUL/残留字（v1.8）
python -m bookkit check --claims --index  # README/index 宣称值与死链
python -m bookkit build --verify          # zh 源稿 ↔ 成品逐章等价（84/84）
python scripts/extract_translations.py    # 18 语言反解 + 逐章验证（应 18/18 全保真）
python scripts/html_audit.py              # HTML 全量审计（应 0 问题）
python scripts/pdf_audit.py               # PDF 书签/编号/顺序审计（PDFROOT 指向 手机课-LaTeX-PDF/pdf）
python scripts/web_smoke.py               # 20 页浏览器冒烟（Playwright，console 零报错）
python mcp/server.py                      # 本书结构 MCP 服务器（stdio）
```

## 四、改稿流程

1. 改 `source/chapters/NN-*.md`（zh）或 `source/translations/<lang>/chapters/…`（译文）；
2. `python -m bookkit build --verify` 必须回到 PASS；
3. 若动了 zh：同步 `你缺失的那门手机课V1.9Fixed.html`（直接 cp）；
4. `lint` + `check --claims --index` + `html_audit.py` 三绿；
5. 重排 PDF：`bash scripts/build_pdfs.sh <lang>`（MiKTeX XeLaTeX）。

## 五、发布（Release）

- Release 一旦发布即 **immutable**（不能追加/改标签名）。流程：**草稿创建 → 上传资产 → `--draft=false` 发布**。
- 标签名被删掉的 Release 永久占用（历史教训：latex-pdf-v1.8 被占用 → 改用 -final）。
- gh 凭据：`git credential fill` 取 token 后 `export GH_TOKEN=…`。
- PDF 大资产不入 git；仓库内 `latex/<lang>/` 是源稿+产物例外（已在 .gitignore 排除编译瞬态）。

### 5.1 GitHub Pages 站点同步（`scripts/sync_site.py`）

站点仓库是 `ClassTechStar/Yihggh.github.io`，根目录的 `index.html` 就是本书中文版。
**层级不同，路径必须降级**：

| | 书页 `<root>/v1.8/zh-CN.html` | 站点 `<root>/index.html` |
|---|---|---|
| Service Worker | `../sw.js` | `sw.js` |
| Manifest | `../manifest.webmanifest` | `manifest.webmanifest` |
| 图标 | `../icons/` | `icons/` |

`python scripts/sync_site.py` 会复制 HTML 并改这三处，同时带上
`sw.js` / `manifest.webmanifest` / `icons/`。漏改的后果是 SW 注册 404、
manifest 与图标全不可达，PWA **静默失效**（页面照常能看，但装不了、离线不了）。

推送：`git -c http.proxy= -c https.proxy= push git@github.com:ClassTechStar/Yihggh.github.io.git main`
（本机 git 全局代理常失效，走 SSH 最稳；`gh` 未登录）。

### 5.2 PWA 相关约束

- `sw.js` 的预缓存清单**只放站点一定有的文件**。放过 `quiz.html` 会在站点根打出 404
  （站点仓库没带自测页），装 SW 时控制台一片红。
- 改缓存策略后要 bump `VERSION`，否则老客户端一直吃旧缓存。
- `scripts/web_smoke.py` 已含 PWA 断言（manifest 可解析 + 图标可达 + SW active），
  CI 会跑；本地跑需要 `pip install playwright && python -m playwright install chromium`。

## 六、md 方言要点（bookkit/markdown.py）

- 行内 HTML 原样保留；表格/SVG 用 ```html 围栏整体保真；
- 块级裸 `<li>` 连跑会合成列表（翻译稿历史损伤的兼容）；
- 段落行首 `N. ` / `- ` 有转义机制（`\.`），避免误判为列表；
- `normalize` 会折叠闭标签前空白（比较用，不改动正文）。

## 七、v1.9 计划

新章草稿在 `source/v1.9/chapters/70-74`（重编号已完成），并入检查清单见 `source/v1.9/README.md`。
