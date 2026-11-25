# 贡献指南

感谢参与《你缺失的那门手机课》。这本书写给"存储满了不知道删什么"的爸妈，
也写给每一个普通人——贡献前请守住这个定位：**通俗、可操作、不吓人**。

## 贡献流程（先看这张图）

```text
发现错误 / 想认领翻译
        │
        ▼
GitHub Issue（勘误模板 / 翻译认领模板）
        │  作者确认范围，避免白做
        ▼
fork → 改 source/（不改成品 HTML）
        │
        ▼
本地门禁：pytest / lint / claims / build --verify / i18n --check-spacing
        │
        ▼
PR（一个主题）→ CI 全绿 → 合并
        │
        ▼
作者重建成品并部署站点（贡献者不需要动 v1.8/、v1.9/ 成品）
```

## 内容贡献（勘误 / 扩写 / 新章）

1. **单一事实源**：中文正文的唯一事实源是 `source/`（v1.8）与 `source/v1.9/`（最新中文版）。
   直接修改 `v1.9/zh-CN.html` 等成品 HTML 的 PR 会被 CI 的"源稿回写等价性"门禁阻断；
   正确做法是改源稿后重建成品：
   ```bash
   python -m bookkit build --book source/v1.9/book.json --out v1.9/zh-CN.html
   python -m bookkit build --book source/v1.9/book.json --verify   # 等价性自检
   ```
2. **写作规范**：口语化、第二人称"你"；具体数字要给出依据或写"以你的机型为准"；
   涉及安全/健康/硬件的硬结论请附来源或标注"需以官方信息为准"。
3. **三层结构**：每章 = 速读层（`::: div .quick-read` 块，800–1500 字 + 速查表）
   → 正文层 → 参考层（深编折叠块）。新章请带速读层；速查表用 `- 要点：做法` 列表
   （不要用 Markdown 表格/链接/`**` 加粗，加粗用 `<strong>`）。
4. **自检**：`python -m bookkit lint --all-versions`、`python -m pytest tests/ -q` 全绿再提 PR。
   HTML 结构类修改可先过 `python scripts/fix_v19_normalize.py`（幂等自检）。

## 翻译贡献

> 想直接认领一章：用 [「翻译认领」Issue 模板](https://github.com/ClassTechStar/Your-Missing-Phone-Class/issues/new?template=translation.yml)
> 写下语言 + 章节即可，不必先读完整个指南。

1. 先读 [docs/i18n/weblate-guide.md](docs/i18n/weblate-guide.md)：用
   `python -m bookkit tm report --lang <你的语言> --book source/v1.9/book.json`
   导出待译段落，只翻译变更段（TM 命中部分直接复用）。
2. **术语表是法律**：`manifest/glossary/<lang>.json` 已锁定 SoC/Passkey/eSIM 等译法，
   译文必须沿用；建议改进术语表本身（单独提 PR）。
3. 保留行内标签（`<strong>` 等）与列表结构；译文落盘 `source/translations/<lang>/` 后
   跑 `python scripts/extract_translations.py` 自检 v1.8 的 84/84 章一致，
   再跑 `python -m bookkit i18n --check-spacing --fail-on error` 确认没有标点空格回归。
   v1.9 译文按 TM 增量管线滚动推进，不要求一次补齐 120 章。
4. 回传译文也可以只交 `tm import` 用的 `{hash: 译文段}` JSON（见指南第三节）。

## 工具链贡献（bookkit / scripts / mcp / 前端壳）

- bookkit 保持**纯标准库零依赖**；开发依赖（pytest 等）只进 CI。
- 新检查/新命令请补 `tests/` 边界用例（`python -m pytest tests/ -q`）。
- 性能预算在 `manifest/languages.json` 的 `versions.<v>.budget` 与
  `bookkit split` 的页级预算（300KB / 5000 标签）内维护，上调预算需要在 PR 里说明理由。

## 提交与 PR

- 提交信息用 Conventional Commits（`fix(v1.9): …` / `feat(i18n): …` / `ci: …`）。
- 一个 PR 一个主题；内容 PR 请附"改了哪几章、事实依据"。
- CI 全绿（lint / claims / build --verify / 19 语分章预算 / 110 项单测 / 35 页浏览器冒烟）是合并前提。

## 许可

内容与代码当前采用 CC BY-NC-SA 4.0（见 [License](License)）。
双许可模式（正文 CC BY-SA + 代码 Apache-2.0）正在评估中，见
[docs/legal/dual-licensing-evaluation.md](docs/legal/dual-licensing-evaluation.md)——
在正式切换前，贡献即按现行许可授权。
