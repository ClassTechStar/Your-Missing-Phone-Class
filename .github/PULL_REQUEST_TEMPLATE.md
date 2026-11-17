## 这个 PR 做了什么

<!-- 一句话：修复/新增/翻译/工具链 -->

## 类型

- [ ] 内容（勘误 / 扩写 / 新章）
- [ ] 翻译（语言：______）
- [ ] 工具链（bookkit / scripts / mcp / 前端壳）
- [ ] 文档 / CI

## 内容类必填

- 改动章节（id 或章号）：
- 事实依据（官方文档 / 实测 / 来源链接；时效性内容注明核对时间）：
- 新章是否带速读层（`::: div .quick-read` 块 + 速查表）：[ ] 是 [ ] 不适用

## 翻译类必填

- [ ] 只翻译 `bookkit tm report` 导出的变更段（TM 未命中部分）
- [ ] 沿用 `manifest/glossary/<lang>.json` 的术语译法
- [ ] 保留 `<strong>` 等行内标签与列表结构（未使用 `**` / Markdown 表格 / 链接）
- [ ] `python scripts/extract_translations.py` 自检通过

## 自检

- [ ] `python -m bookkit lint --all-versions` 全绿
- [ ] `python -m pytest tests/ -q` 全绿
- [ ] 改了成品 HTML 必已回写源稿（`bookkit build --verify` 通过）
- [ ] 未直接提交构建产物 / 临时文件（dist/、*Fixed.html 等）
