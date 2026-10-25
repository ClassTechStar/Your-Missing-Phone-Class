# v1.9 新章计划（草稿，未并入 v1.8）

五份新章草稿已按 **第 70–74 章** 重编号（原占位号 37–41 与 v1.8 正式章节冲突）：

| 章 | id | 主题 |
|----|----|------|
| 第七十章 | di-qishizhang | 手机与可穿戴设备——手腕上的协同 |
| 第七十一章 | di-qishiyizhang | 旅行与手机——eSIM、流量与离线地图 |
| 第七十二章 | di-qishierzhang | 手机与健康管理——把数字变成行动 |
| 第七十三章 | di-qishisanzhang | AI 短视频创作——从一句话到一条片 |
| 第七十四章 | di-qishisizhang | 竖屏短剧入门——3 分钟一个钩子 |

## 并入 v1.9 的检查清单

1. 逐章补全「本章导览 / 动手练习 / 本章小结」结构（对齐 84 章既有版式）；
2. `source/book.json` 增补 5 章（part 归属：建议实战篇或新设「拓展篇」）；
3. `python -m bookkit build --verify` 通过后，再走 19 语言翻译流程
   （翻译源稿体系见 source/translations/，新章翻译后同路径落盘）；
4. 侧栏目录、附录 G 速查索引、index.html 卡片由 `bookkit index` 联动更新；
5. 全量质检：`python scripts/html_audit.py` + `pdf_audit.py` 双绿。

原始草稿（含写作备注）：[../v1.9-drafts.md](../v1.9-drafts.md)
