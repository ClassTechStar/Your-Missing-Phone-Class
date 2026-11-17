"""quick：从各章「速读层」派生《给爸妈的 20 分钟速读版》。

三层结构里速读层（`::: div .quick-read` 块，每章 800–1500 字 + 速查表）
本身就是为"5 分钟读完一章"设计的；把 120 个速读层按章序拼成一本轻量册子，
就是最贴近"写给爸妈"初衷的传播单品——正文层/参考层留给需要深读的读者。

产物：单文件 HTML（纯静态、内联样式、无脚本），可直接分发/打印。
"""

import json
import re
from pathlib import Path

from . import build as B
from . import markdown as M

RE_QUICK = re.compile(r'^::: div \.quick-read\s*\n([\s\S]*?)^:::\s*$', re.M)


def _quick_block(text: str) -> str:
    m = RE_QUICK.search(text)
    return m.group(1).strip() if m else ''


def build_quick(root: Path, book_path: Path = None, out: Path = None) -> dict:
    book = B.load_book(root, book_path, 'zh-CN')
    version = book.get('version') or 'v1.9'
    src = book_path.parent if book_path else (root / 'source')

    entries = []
    missing = []
    for ch in book['chapters']:
        f = src / ch['file']
        if not f.is_file():
            continue
        meta, body = M.split_front_matter(f.read_text(encoding='utf-8'))
        block = _quick_block(body)
        if not block:
            missing.append(ch['id'])
            continue
        title = meta.get('nav') or ch['id']
        entries.append((ch['id'], title, M.from_markdown(block)))

    toc = '\n'.join(
        f'<p class="toc"><a href="#{cid}">{title}</a></p>' for cid, title, _ in entries)
    secs = '\n'.join(
        f'<section id="{cid}">\n<h2>{title}</h2>\n{html}\n</section>'
        for cid, title, html in entries)

    doc = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>给爸妈的 20 分钟速读版 · 你缺失的那门手机课</title>
<meta name="description" content="《你缺失的那门手机课》速读版：{len(entries)} 章速读层合集，每章 5 分钟读完，含速查表。">
<style>
body {{ font-family: system-ui, "PingFang SC", "Microsoft YaHei", sans-serif;
       max-width: 42em; margin: 0 auto; padding: 1.5em 1em 4em; line-height: 1.8; color: #222; }}
h1 {{ font-size: 1.5em; }} h2 {{ font-size: 1.25em; margin-top: 2em;
     border-bottom: 2px solid #4f46e5; padding-bottom: .3em; }}
.toc a {{ color: #4f46e5; text-decoration: none; }}
.toc {{ margin: .3em 0; }}
ul {{ padding-left: 1.4em; }} li {{ margin: .3em 0; }}
strong {{ color: #111; }}
footer {{ margin-top: 3em; font-size: .85em; color: #777; }}
@media print {{ a {{ color: inherit; }} }}
</style>
</head>
<body>
<h1>给爸妈的 20 分钟速读版</h1>
<p>《你缺失的那门手机课》速读层合集——{len(entries)} 章，每章 5 分钟读完：
这章解决什么问题、最关键的几件事、今天就能做的动作、最大的坑，外加一张速查表。
想深读哪一章，再去翻全书对应章节。</p>
<h2>目录</h2>
{toc}
{secs}
<footer>派生自《你缺失的那门手机课》v{version} 速读层（bookkit quick）。</footer>
</body>
</html>
'''

    out = Path(out) if out else (root / 'dist' / f'quick-read-{version}.html')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding='utf-8', newline='\n')
    return {'version': version, 'chapters': len(entries), 'missing': missing,
            'bytes': len(doc.encode('utf-8')), 'out': str(out)}
