#!/usr/bin/env python3
"""build_languages_page.py — 生成 languages.html（多语言诚实分级页，方案 §7.2）。

分级数据来自 manifest/languages.json 的 quality 字段（单一真源），
所以改了 manifest 里的分级，重跑本脚本即可同步页面。

页面要求：**离线可读**。不引任何外部 CSS/JS/字体，断网也能看。

用法：
  py -3 scripts/build_languages_page.py
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "manifest" / "languages.json"
OUT = ROOT / "languages.html"

TIER_ORDER = {"★★★★★": 0, "★★★★": 1, "★★★": 2, "★★": 3, "★": 4, "☆": 5}


def esc(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;"))


CSS = """
:root{--ink:#1f2937;--muted:#6b7280;--line:#e5e7eb;--bg:#fafafa;--accent:#2563eb;
--warm:#fef3c7;--warm-line:#f59e0b;--ok:#059669}
*{box-sizing:border-box}
body{margin:0;padding:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",
"PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;
background:var(--bg);color:var(--ink);line-height:1.75}
.wrap{max-width:860px;margin:0 auto;padding:40px 20px 72px}
header{border-bottom:2px solid var(--ink);padding-bottom:18px;margin-bottom:26px}
h1{font-size:26px;margin:0 0 8px}
.sub{color:var(--muted);font-size:15px;margin:0}
h2{font-size:19px;margin:34px 0 10px;padding-left:10px;border-left:4px solid var(--accent)}
h3{font-size:16px;margin:22px 0 8px}
p{margin:10px 0}
a{color:var(--accent)}
table{width:100%;border-collapse:collapse;margin:16px 0;font-size:14px;background:#fff;
box-shadow:0 1px 3px rgba(0,0,0,.06)}
th,td{border:1px solid var(--line);padding:9px 11px;text-align:left;vertical-align:top}
th{background:#f4f4f5;font-weight:600;white-space:nowrap}
tr:nth-child(even) td{background:#fcfcfd}
.stars{color:var(--warm-line);letter-spacing:1px;white-space:nowrap}
.tier5 .stars{color:var(--ok)}
.pill{display:inline-block;font-size:12px;padding:1px 8px;border-radius:999px;
border:1px solid var(--line);background:#f4f4f5;color:var(--muted);white-space:nowrap}
.note{background:#fff;border:1px solid var(--line);border-left:4px solid var(--warm-line);
padding:14px 16px;border-radius:4px;margin:16px 0;font-size:14.5px}
.note strong{color:var(--ink)}
.quote{border-left:3px solid var(--line);padding:2px 0 2px 14px;color:var(--muted);
font-size:14.5px;margin:14px 0}
ol,ul{padding-left:22px}
li{margin:5px 0}
footer{margin-top:46px;padding-top:16px;border-top:1px solid var(--line);
color:var(--muted);font-size:13.5px}
code{background:#f1f2f4;padding:1px 5px;border-radius:3px;font-size:13px}
a.btn{display:inline-block;background:var(--accent);color:#fff;padding:7px 15px;
border-radius:6px;text-decoration:none;font-size:14px;margin-right:8px}
a.btn.gray{background:#4b5563}
"""


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    langs = data["languages"]
    disclosure = data.get("language_quality_disclosure", "")

    rows = []
    for code, meta in sorted(langs.items(),
                             key=lambda x: (TIER_ORDER.get(x[1].get("quality", {}).get("stars", "★"), 9),
                                            x[1].get("priority", 99))):
        q = meta.get("quality") or {}
        stars = q.get("stars", "")
        cls = "tier5" if stars == "★★★★★" else ""
        rows.append(
            f'<tr class="{cls}"><td><strong>{esc(meta.get("name", code))}</strong>'
            f'<br><span class="pill">{esc(code)}</span></td>'
            f'<td class="stars">{esc(stars)}</td>'
            f'<td>{esc(q.get("label", ""))}</td>'
            f'<td>{esc(q.get("note", ""))}</td></tr>'
        )

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>多语言版本分级 · 你缺失的那门手机课</title>
<meta name="description" content="《你缺失的那门手机课》各语言版本的实际审校程度：简体中文为人工审校版，其余为机翻 + 抽查。">
<style>{CSS}</style>
</head>
<body>
<div class="wrap">

<header>
  <h1>这本书有 20 个语言版本，它们不是同样可靠的</h1>
  <p class="sub">《你缺失的那门手机课》· 多语言审校分级 · 数据源：<code>manifest/languages.json</code></p>
</header>

<p>同一本书，简体中文版和阿拉伯语版，付出的功夫不一样。与其让你自己猜，不如写在明面上。</p>

<h2>分级表</h2>
<table>
<thead><tr><th>语言</th><th>分级</th><th>含义</th><th>依据</th></tr></thead>
<tbody>
{chr(10).join(rows)}
</tbody>
</table>

<div class="note">
<strong>为什么要这么分？</strong><br>
{esc(disclosure)}
</div>

<h2>一句话版本</h2>
<table>
<thead><tr><th>分级</th><th>你可以怎么用</th></tr></thead>
<tbody>
<tr><td class="stars">★★★★★</td><td>简体中文：可以当准本照着做。路径、版本、结论都有人对过账。</td></tr>
<tr><td class="stars">★★★</td><td>繁體中文 / 粵語 / English：结构完整，个别用词可能不如中文版顺。术语已统一。</td></tr>
<tr><td class="stars">★★</td><td>其余 15 种：机器翻译 + 术语表统一，<strong>没有逐章人工校对</strong>。当参考可以，当准本请回中文版。</td></tr>
<tr><td class="stars">☆</td><td>文言文：语言表演与文化彩蛋，不承担教学用途。</td></tr>
</tbody>
</table>

<h2>三个我们做过的选择</h2>

<h3>1. 去 AI 味只做中文真源</h3>
<p>这一版的去 AI 味改造（句式、案例、立场、版本锚点、勘误）全部落在中文版。
18 种外语是<strong>翻译</strong>，不是并行创作。翻译里保留一点工整是正常的——
读者对翻译腔的容忍度本来就高，硬把口语塞进 19 种语言里只会更糟。</p>

<h3>2. 不假装 19 种语言同等完美</h3>
<div class="quote">
最要命的不是机器味，是<strong>假装</strong>。<br>
一个训练有素的模型会自然地假设"我应该把每种语言都写好"，
于是 19 个版本看起来一样精致、一样完整——而其中 15 个从来没被母语者逐句读过。<br>
人不会这样。人会说：这 5 种我认真弄了，那 15 种我只能保证结构在、术语对。
</div>
<p>所以这张表是<strong>主动交代</strong>，不是免责声明。分级低不代表翻译差，
它只代表我们在那一版上投入的<strong>人工时间</strong>少。</p>

<h3>3. 分级会变，页面跟着变</h3>
<p>分级写在 <code>manifest/languages.json</code> 里，是这本书的单一数据源。
某个语言被母语群友认真校过一轮，星级就往上提一格，然后重新生成本页。
读者看到的永远是<strong>当下真实</strong>的分级。</p>

<h2>想帮忙改某一版？</h2>
<p>本书是开源的，任何语言的校对、术语订正、语病反馈都欢迎。</p>
<ul>
<li>GitHub Issue：<a href="https://github.com/ClassTechStar/Your-Missing-Phone-Class/issues">ClassTechStar/Your-Missing-Phone-Class</a></li>
<li>QQ 群 1074995524（作者 missile 在群里）</li>
</ul>
<p>反馈时请带上：语言代码、章节号或术语条目、原文、你的修改建议。
术语订正最省事——<code>manifest/glossary.json</code> 是全书共用的术语表，
改一处，所有语言一起受益。</p>

<h2>还有件事</h2>
<p>如果你发现中文版里有错，麻烦走
<a href="errata.html">勘误页</a>，而不是在评论里提一句就算了。
勘误会进版本记录，路径错误会改到路径库里，不是改散落在正文里的某一句话。</p>

<footer>
<p>《你缺失的那门手机课》· 作者 missile / ClassTechStar · QQ 群 1074995524 ·
本书按 CC BY-NC-SA 4.0 发布。<br>
本页数据来自 <code>manifest/languages.json</code>，由
<code>scripts/build_languages_page.py</code> 生成。</p>
</footer>

</div>
</body>
</html>
"""
    OUT.write_text(html, encoding="utf-8")
    print(f"[+] 已生成 {OUT.name}（{len(rows)} 种语言）")

    # 自检：标签配平 + 无外部依赖
    from html.parser import HTMLParser

    class P(HTMLParser):
        def __init__(self):
            super().__init__()
            self.stack = []
            self.bad = []

        def handle_starttag(self, tag, attrs):
            if tag not in ("meta", "br", "hr", "img", "link", "input"):
                self.stack.append(tag)

        def handle_endtag(self, tag):
            if self.stack and self.stack[-1] == tag:
                self.stack.pop()
            elif tag in self.stack:
                self.bad.append(tag)
                while self.stack and self.stack.pop() != tag:
                    pass

    p = P()
    p.feed(html)
    ext = [a for a in ("cdn", "http://", "https://fonts", "unpkg", "jsdelivr")
           if a in html.replace("https://github.com", "").replace("http://www.w3.org", "")]
    print(f"[{'✓' if not p.stack and not p.bad else '!'}] 标签配平"
          + (f" 未闭合 {p.stack}" if p.stack else "")
          + (f" 错配 {p.bad}" if p.bad else ""))
    print(f"[{'✓' if not ext else '!'}] 外部依赖：{ext or '无'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
