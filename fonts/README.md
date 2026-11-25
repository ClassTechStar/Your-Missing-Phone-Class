# 字体说明

- `MiSans-subset.woff2`（约 0.6MB，入库）：站点与单文件实际使用的子集字体，`bookkit split` 会把它分发到各语言页面。
- `MiSans-Normal.ttf`（约 7.8MB，不入库）：子集化母本。GitHub 历史中曾用 Git LFS 存储；Gitee 免费仓库不支持 LFS，因此两端统一改为按需下载，不再入库。

日常构建、测试与部署都不需要 TTF。若需要重新生成 woff2 子集：从 MiSans 官方发布页（以官方页面为准）下载 Normal 字重，放到本目录，再用 `pyftsubset` 按 `source/` 正文字符集生成 `MiSans-subset.woff2` 并提交。
