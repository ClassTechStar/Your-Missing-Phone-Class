# 工程化脚本

> **当前状态：本目录暂为空文档位。** 历史上的一致性工具链已于提交 `7f58c0c`（Remove i18n build tooling）移除；本文件描述仓库当前真实的校验方式与覆盖盲区，以及工具链的重建计划。详见根目录 `README.md` 的「已知问题」。

## 一、当前一致性保障

`.github/workflows/ci.yml` 内联了一段 Python 校验（提交 `0869a74` 起，替代已删除的 `scripts/check_consistency.py`），在每次 push / PR 时对 **v1.8 目录** 执行以下检查：

| 检查项 | 判定 |
|--------|------|
| 内容区块计数 | 19 个文件各有 84 个 `class="mb-10 content-section"` 区块 |
| 目录锚点对齐 | 各语言侧边栏目录锚点序列与 `v1.8/zh-CN.html` 完全一致 |
| 语言标记 | `<html lang>` 与语言代码匹配（`pt` 例外为 `pt-BR`）；`ar` / `he` 必须有 `dir="rtl"`，其余不得有 |
| 文件完整性 | 无 NUL 字节、以 `</html>` 结尾、`index.html` 存在于仓库根 |
| 残留字符 | 非中文版本无残留汉字（`en` / `it` / `es` 允许 ≤ 6 个）；繁体目标无残留简体 |
| 源文件一致 | `v1.8/zh-CN.html` 与根目录 `你缺失的那门手机课V1.8Fixed.html` 归一换行后 SHA-256 一致 |

任一检查失败即阻断合并。

## 二、已知覆盖盲区

当前 CI **只守护 v1.8**，以下缺陷不会被发现（详见根目录「已知问题」）：

- 历史版本（v1.5 / v1.6 / v1.7 与 `archive/`）的结构、锚点、`lang`、NUL 均未校验；
- 各文件 `<title>` 中的版本串未与目录名比对；
- 正文互链（附录 G 速查索引等）的 `href="#id"` 未做双向闭合校验（仅校验侧边栏目录）；
- 跨语言的区块数缺口（如某语言少若干章）未比对；
- `README.md` / `index.html` 中宣称的数字（章数、区块数、语言数）未与真实内容比对。

## 三、本地自检（当前可用）

由于 `scripts/` 暂无脚本，可复用 CI 的等价判断自行校验。示例（Python 3 标准库，零依赖）：

```bash
# 统计某版本某语言的内容区块数
python3 - <<'EOF'
import re
from pathlib import Path
for f in sorted(Path('v1.8').glob('*.html')):
    raw = f.read_text(encoding='utf-8')
    n = len(re.findall(r'id="[\w-]+" class="mb-10 content-section"', raw))
    print(f.name, n)
EOF

# 检查页内锚点是否双向闭合（排除 JS 模板串）
python3 - <<'EOF'
import re
from pathlib import Path
for f in sorted(Path('v1.8').glob('*.html')):
    raw = f.read_text(encoding='utf-8')
    ids = set(re.findall(r'id="([\w-]+)"', raw))
    bad = sorted({a for a in re.findall(r'href="#([\w-]+)"', raw) if a not in ids})
    if bad:
        print(f.name, bad)
EOF
```

## 四、重建计划（工具链 `bookkit`）

原设计（单一数据源 `languages.json` + 生成器渲染 `AUTOGEN` 卡片块 + 检查脚本无副作用）方向正确，将按下述目标重建，并恢复本目录文档：

| 模块 | 职责 |
|------|------|
| `manifest/languages.json` | 语言元数据 + 各版本文件映射 + 卡片样式 + 翻译优先级（单一数据源） |
| `bookkit lint` | 全版本结构 / 锚点 / 版本串 / `lang` / 残留字 / NUL 校验 |
| `bookkit check` | README 与 index.html 宣称值 ↔ 真实内容比对 |
| `bookkit build` | Markdown 源 → 单文件 HTML（目录、速查索引、版本徽章注入） |
| `bookkit i18n` | 翻译覆盖率报告（缺失章节 id） |
| `bookkit release` | 发布清单与 APK 矩阵 |

重建后，CI 将由「仅 v1.8 内联脚本」升级为「全版本矩阵门禁 + 宣称值校验」，覆盖上述全部盲区。

## 五、设计原则（延续）

- **单一数据源**：语言清单只在 `languages.json` 维护，入口页卡片由生成器渲染，避免多处手写漂移。
- **标记隔离**：`AUTOGEN` 标记之间的内容是机器生成的；标记以外的 HTML（hero、stats、目录、归档区）保持手写自由度。
- **幂等**：生成器重复运行结果一致；检查脚本无副作用。
- **零依赖**：仅用 Python 标准库，CI 环境开箱即用。
