# -*- coding: utf-8 -*-
"""生成 criwits 风格的站点门户 index.html（目录取自 v1.9 构建产物，AUTOGEN 区留位）。

用法：py scripts/build_portal.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# ── 从 v1.9 构建产物提取篇目结构 ──
book_html = (ROOT / 'v1.9' / 'zh-CN.html').read_text(encoding='utf-8')
groups = []          # [(part_id, part_title, [(sid, ch_title), ...])]
cur = None
# 顺序扫描：篇 section 开标签 / 章节开标签+标题
pat = re.compile(
    r'<section id="(?P<pid>[a-z0-9-]+)"[^>]*>\s*(?:<h2[^>]*>(?P<ptitle>[^<]+)</h2>)?'
    r'|<div id="(?P<sid>[a-z0-9-]+)" class="mb-10 content-section">\s*<h3[^>]*>(?P<ctitle>[^<]+)</h3>')
for m in pat.finditer(book_html):
    if m.group('pid'):
        cur = (m.group('pid'), (m.group('ptitle') or '').strip(), [])
        groups.append(cur)
    elif m.group('sid'):
        if cur is None:
            cur = ('standalone', '其他章节', [])
            groups.append(cur)
        cur[2].append((m.group('sid'), m.group('ctitle').strip()))
toc_entries = sum(len(g[2]) for g in groups)
assert toc_entries >= 120, f'目录提取异常：{toc_entries} 条'

toc_html = []
for pid, ptitle, chs in groups:
    toc_html.append(f'      <li class="toc-part">{ptitle or pid}</li>')
    for sid, ctitle in chs:
        toc_html.append(f'      <li><a href="v1.9/zh-CN.html#{sid}">{ctitle}</a></li>')
toc_html = '\n'.join(toc_html)

TOGGLE = """<script>
(function(){
  "use strict";
  var btns = document.querySelectorAll('.theme-toggle button');
  function mark(){
    var m = 'auto';
    try { m = localStorage.getItem('pc-theme') || 'auto'; } catch(e){}
    btns.forEach(function(b){ b.classList.toggle('on', b.getAttribute('data-t') === m); });
  }
  btns.forEach(function(b){
    b.addEventListener('click', function(){
      var v = b.getAttribute('data-t');
      try { localStorage.setItem('pc-theme', v); } catch(e){}
      var h = document.documentElement;
      h.classList.toggle('dark', v === 'dark');
      h.classList.toggle('light', v === 'light');
      mark();
    });
  });
  mark();
})();
</script>"""

PREPAINT = """<script>(function(){try{var m=localStorage.getItem('pc-theme');if(m==='dark')document.documentElement.classList.add('dark');else if(m==='light')document.documentElement.classList.add('light');}catch(e){}})();</script>"""

SWB = """<script>
/* Service Worker：门户与语言书离线可用。file:// 打开时跳过。 */
if ('serviceWorker' in navigator && location.protocol.startsWith('http')) {
    window.addEventListener('load', function () {
        navigator.serviceWorker.register('sw.js')
            .catch(function (err) { console.warn('SW 注册失败：', err); });
    });
}
</script>"""

UPDATER = """<script>
/* 更新检查：更新源 = GitHub Release（书版通道：v<数字> 开头的 tag）。 */
(function(){
"use strict";
var PAGE_VERSION="v1.9";
var REPO="ClassTechStar/Your-Missing-Phone-Class";
function cmpVer(a,b){a=String(a).replace(/^v/,"");b=String(b).replace(/^v/,"");var A=a.split(/[-.]/),B=b.split(/[-.]/),i,x,y;for(i=0;i<Math.max(A.length,B.length);i++){x=parseInt(A[i]||"0",10);y=parseInt(B[i]||"0",10);if(x!==y)return x-y;}return 0;}
function show(tag,url){
var b=document.createElement("div");
b.style.cssText="position:fixed;left:12px;bottom:12px;z-index:99990;background:#0074d9;color:#fff;padding:10px 14px;border-radius:999px;font:14px/1.4 system-ui,sans-serif;box-shadow:0 6px 20px rgba(0,0,0,.25);display:flex;gap:10px;align-items:center;max-width:92vw";
var t=document.createElement("span");t.textContent="New version "+tag+" is available";
var a=document.createElement("a");a.href=url;a.target="_blank";a.rel="noopener";
a.textContent="View update";a.style.cssText="color:#fff;text-decoration:underline;font-weight:600";
var x=document.createElement("button");x.type="button";x.textContent="\\u00d7";x.setAttribute("aria-label","Close");
x.style.cssText="background:rgba(255,255,255,.25);border:0;color:#fff;width:22px;height:22px;border-radius:50%;cursor:pointer;font-size:14px;line-height:1";
x.onclick=function(){b.remove();try{var s=JSON.parse(localStorage.getItem("pc-gh-update")||"{}");s.d=tag;localStorage.setItem("pc-gh-update",JSON.stringify(s));}catch(e){}};
b.appendChild(t);b.appendChild(a);b.appendChild(x);
document.body.appendChild(b);
setTimeout(function(){if(b.parentNode)b.parentNode.removeChild(b);},60000);
}
try{
if(location.protocol==="file:")return;
var st=null;try{st=JSON.parse(localStorage.getItem("pc-gh-update")||"null");}catch(e){}
var now=Date.now();
if(st&&st.v===PAGE_VERSION&&now-(st.t||0)<86400e3)return;
var done=function(){try{localStorage.setItem("pc-gh-update",JSON.stringify({t:now,v:PAGE_VERSION}));}catch(e){}};
fetch("https://api.github.com/repos/"+REPO+"/releases?per_page=30",{headers:{"Accept":"application/vnd.github+json"}}).then(function(r){return r.ok?r.json():[];}).then(function(list){
if(!Array.isArray(list))return done();
for(var i=0;i<list.length;i++){
var tag=String(list[i]&&list[i].tag_name||"");
if(/^v\\d/.test(tag)){
if(cmpVer(tag,PAGE_VERSION)>0&&(!st||st.d!==tag))show(tag,list[i].html_url||("https://github.com/"+REPO+"/releases/tag/"+tag));
break;
}
}
done();
}).catch(function(){done();});
}catch(e){}
})();
</script>"""

CSS = """  <style>
  :root{
    --link:#0074d9;--link-visited:#454db6;
    --g1:#f8f9fa;--g2:#e9ecef;--g3:#dee2e6;--g5:#adb5bd;--g8:#495057;
    --ink:#1a1a1a;--surface:#ffffff;
    --hint-bg:#f1f2f3;--hint-warn:#fff8ec;--hint-warn-line:#ffc266;
  }
  html.dark{
      --link:#66b5f2;--link-visited:#8f96e8;
      --g1:#111827;--g2:#1f2937;--g3:#374151;--g5:#6b7280;--g8:#d1d5db;
      --ink:#e5e7eb;--surface:#111827;
      --hint-bg:#1f2937;--hint-warn:#2d2413;
      color-scheme:dark;
  }
  @media (prefers-color-scheme:dark){
    html:not(.light):not(.dark){
      --link:#66b5f2;--link-visited:#8f96e8;
      --g1:#111827;--g2:#1f2937;--g3:#374151;--g5:#6b7280;--g8:#d1d5db;
      --ink:#e5e7eb;--surface:#111827;
      --hint-bg:#1f2937;--hint-warn:#2d2413;
      color-scheme:dark;
    }
  }
  html{font-size:16px;scroll-behavior:smooth}
  body{
    margin:0;background:var(--surface);color:var(--ink);
    font-family:inter,source han sans sc,source han sans cn,noto sans sc,MiSans,'PingFang SC','Microsoft YaHei',system-ui,sans-serif;
    letter-spacing:.33px;line-height:1.85;text-rendering:optimizeLegibility;
    -webkit-font-smoothing:antialiased;
  }
  header.top{
    border-bottom:1px solid var(--g2);background:var(--surface);
    position:sticky;top:0;z-index:10;
  }
  header.top .bar{
    max-width:46rem;margin:0 auto;padding:.7rem 1rem;
    display:flex;align-items:baseline;justify-content:space-between;gap:1rem;
  }
  header.top .brand{font-weight:600;color:var(--ink);text-decoration:none;font-size:1.02rem;line-height:1.3}
  header.top nav{display:flex;gap:1.2rem}
  header.top nav a{color:var(--g8);text-decoration:none;font-size:.92rem}
  header.top nav a:hover{color:var(--link)}
  .theme-toggle{display:flex;gap:.25rem;align-items:center}
  .theme-toggle button{
    border:1px solid var(--g2);background:var(--surface);color:var(--g8);
    border-radius:.375rem;width:1.9rem;height:1.7rem;cursor:pointer;
    font-size:.95rem;line-height:1;padding:0;
  }
  .theme-toggle button.on{background:var(--link);color:#fff;border-color:var(--link)}
  main{max-width:46rem;margin:0 auto;padding:2.6rem 1rem 4rem}
  h1{font-size:1.9rem;font-weight:600;line-height:1.35;margin:0 0 1rem}
  h2{font-size:1.3rem;font-weight:600;margin:2.6rem 0 .8rem;padding-bottom:.4rem;border-bottom:1px solid var(--g2)}
  h2 a.head-anchor{color:var(--g5);text-decoration:none;font-size:.85rem;margin-left:.4rem}
  h3{font-size:1.08rem;font-weight:600;margin:1.6rem 0 .5rem}
  p{margin:.9rem 0}
  a{color:var(--link)}
  a:hover{text-decoration:underline}
  ol.toc,ul.cw-cards,.plain-list{padding-inline-start:1.4rem;margin:.8rem 0}
  ol.toc li,.plain-list li{margin:.32rem 0}
  ol.toc li.toc-part{list-style:none;margin:1.1rem 0 .3rem;font-weight:600;color:var(--ink)}
  ol.toc{list-style:none;padding-inline-start:0}
  ol.toc li{margin:.28rem 0}
  ol.toc li.toc-part{border-bottom:1px solid var(--g2);padding-bottom:.25rem}
  ol.toc li a{text-decoration:none}
  ol.toc li a:hover{text-decoration:underline}
  .stats{display:flex;flex-wrap:wrap;gap:2.2rem;margin:1rem 0}
  .stat p{font-weight:600;margin:0;font-size:1.5rem;color:var(--ink)}
  .stat small{display:block;font-size:.8rem;font-weight:400;color:var(--g8);letter-spacing:0}
  .cw-versions{margin:1.4rem 0}
  .cw-versions h3{margin:1.5rem 0 .4rem}
  ul.cw-cards{list-style:none;padding:0;margin:.4rem 0}
  ul.cw-cards li{margin:.5rem 0;padding-bottom:.5rem;border-bottom:1px solid var(--g2)}
  ul.cw-cards li a{font-weight:600;text-decoration:none}
  ul.cw-cards li a:hover{text-decoration:underline}
  .cw-label{color:var(--g8);font-size:.85rem;margin-inline-start:.5rem}
  .cw-desc{margin:.2rem 0 0;font-size:.92rem;color:var(--g8)}
  .cw-tier{margin:.2rem 0 0;font-size:.82rem;color:#b58900}
  .note{
    background:var(--hint-bg);border-inline-start:.25rem solid var(--g5);
    border-radius:.25rem;padding:.6rem .9rem;margin:1rem 0;font-size:.95rem;
  }
  .note.warn{border-inline-start-color:var(--hint-warn-line);background:var(--hint-warn)}
  footer{
    border-top:1px solid var(--g2);color:var(--g8);
    max-width:46rem;margin:0 auto;padding:1.4rem 1rem 3rem;font-size:.9rem;
  }
  footer a{color:var(--link)}
  hr{border:0;border-top:1px solid var(--g2);margin:2.4rem 0}
  </style>"""

HEAD = f"""<!DOCTYPE html>
<html lang="zh-CN"><head>
<meta charset="UTF-8">
{PREPAINT}<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="你缺失的那门手机课 · 手机是用会的，不是看会的。120 个内容区块，353.8 万字，从找回误删照片讲到亲手做出第一个 App。">
<meta name="author" content="ClassTechStar">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#0074d9">
<meta property="og:type" content="website">
<meta property="og:title" content="你缺失的那门手机课 · 网页版">
<meta property="og:description" content="写给普通人的手机使用课程：零门槛、讲原理、能动手。v1.9 最新中文版 120 个内容区块，另有 19 种语言完整翻译版。">
<meta property="og:locale" content="zh_CN">
<meta name="twitter:card" content="summary">
<title>你缺失的那门手机课 · 网页版</title>
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%230074d9'/%3E%3Crect x='20' y='10' width='24' height='44' rx='4' fill='%23ffffff'/%3E%3Crect x='24' y='16' width='16' height='28' rx='2' fill='%230074d9'/%3E%3Ccircle cx='32' cy='49' r='2' fill='%230074d9'/%3E%3C/svg%3E">
<link rel="manifest" href="manifest.webmanifest">
{CSS}
{PREPAINT}
</head>
<body>
<header class="top"><div class="bar">
  <a class="brand" href="#top">你缺失的那门<br>手机课</a>
  <nav><a href="#top">首页</a><a href="#目录">目录</a><a href="#版本">版本</a><a href="#致敬">致敬</a><a href="#反馈">反馈</a></nav>
  <div class="theme-toggle" role="group" aria-label="主题切换">
    <button type="button" data-t="light" title="浅色">☀</button>
    <button type="button" data-t="auto" title="跟随系统">◐</button>
    <button type="button" data-t="dark" title="深色">☾</button>
  </div>
</div></header>
{TOGGLE}
<main id="top">
  <h1>你缺失的那门手机课（网页版）</h1>
  <p>这是一份写给普通人的手机使用课程。它平易近人，娓娓道来：从找回误删的照片、识破一条诈骗短信讲起，到把手机调成顺手的工具，再到亲手做出第一个 App——安卓、iOS、鸿蒙三个平台都走一遍。</p>
  <p>它也试图回答一些「手机课」之外的问题：AI 时代该怎样指挥机器干活，个人信息是怎样泄露的又该怎么守住，可穿戴设备和健康数据能帮我们做什么。零门槛、讲原理、能动手——这是本书从第一天起就坚持的三件事。</p>
  <p>最新中文版 v1.9 共 120 个内容区块、353.8 万字；另有 v1.8 完整翻译版，覆盖 19 种语言。</p>

  <h2 id="目录">目录 <a class="head-anchor" href="#目录">#</a></h2>
  <p>点击任一标题，即可跳到 v1.9 的对应章节。着急用的时候，也可以按「你现在遇到的事」直接翻——书里的附录 G 是一张全册速查索引。</p>
  <ol class="toc">
{toc_html}
  </ol>

  <h2 id="版本">本作品的各种版本 <a class="head-anchor" href="#版本">#</a></h2>
  <ul class="plain-list">
    <li><strong>网页版（最新中文版）</strong>：<a href="v1.9/zh-CN.html">v1.9 · zh-CN</a> —— 单文件，离线也能打开；本站首页即 v1.9。</li>
    <li><strong>多语言版本</strong>：<a href="v1.8/zh-CN.html">v1.8 · 简体中文</a> 等 19 种语言，见下方列表。</li>
    <li><strong>Android 应用</strong>：19 种语言各一个 APK，内置检查更新，见 <a href="https://github.com/ClassTechStar/Your-Missing-Phone-Class/releases/tag/apk-v1.8-r4">apk-v1.8-r4 Release</a>。</li>
    <li><strong>LaTeX 排版 PDF</strong>：五个 Release 共 93 本，见 <a href="https://github.com/ClassTechStar/Your-Missing-Phone-Class/releases">Releases</a>。</li>
    <li><strong>源代码</strong>：<a href="https://github.com/ClassTechStar/Your-Missing-Phone-Class">GitHub 仓库</a>（本页由 <code>bookkit index</code> 维护语言卡片与统计数字）。</li>
  </ul>
  <div class="note">应用与网页都内置了「检查更新」：更新源默认是本仓库的 GitHub Release。应用启动时会自动检查（一天最多一次），也可以随时点应用里的「更新」按钮手动查。</div>

  <!-- AUTOGEN:languages-v1.8 START - 由 python -m bookkit index 生成，勿手改 -->
  <!-- AUTOGEN:languages-v1.8 END -->

  <!-- AUTOGEN:languages-v1.9 START - 由 python -m bookkit index 生成，勿手改 -->
  <!-- AUTOGEN:languages-v1.9 END -->

  <h2 id="反馈">反馈与交流 <a class="head-anchor" href="#反馈">#</a></h2>
  <p>我们非常希望听到读者的声音。无论是对编写方向有想法，还是发现了叙述不正确或不严谨的地方，亦或是找到了一个错别字，都请告诉我们——每一条反馈都会认真对待。</p>
  <ul class="plain-list">
    <li><strong>GitHub Issues</strong>：<a href="https://github.com/ClassTechStar/Your-Missing-Phone-Class/issues">主仓库 · 提交问题</a>（勘误会被记录并公示）</li>
    <li><strong>QQ 交流群</strong>：1074995524</li>
    <li><strong>哔哩哔哩</strong>：<a href="https://space.bilibili.com/702063384">@ClassTechStar</a></li>
  </ul>

  <h2 id="作者">作者 <a class="head-anchor" href="#作者">#</a></h2>
  <p>ClassTechStar：白天写代码，晚上教爸妈用手机。教着教着发现，市面上要么是太浅的入门册子，要么是维修手册，把原理讲清楚的没几本——于是就有了这本。</p>

  <h2 id="致敬">感谢与致敬 <a class="head-anchor" href="#致敬">#</a></h2>
  <p>这本书的名字里带着「缺失」二字，而这个开头并不是我们首创——它来自两门同样以「缺失」为名的课。没有它们，就不会有这本书。</p>
  <ul class="plain-list">
    <li><strong>《你缺失的那门计算机课》</strong>（<a href="https://www.criwits.top/missing/">www.criwits.top/missing</a>）：中文开源的计算机通识读本，从文件管理一路讲到字符编码与 AI 对话，平易近人，娓娓道来。本书的理念、体例，乃至「你缺失的那门」这个名字，正是从它长出来的——如果你还没读过，请一定去读。</li>
    <li><strong>《计算机教育中缺失的一课》</strong>（The Missing Semester of Your CS Education · MIT，<a href="https://missing.csail.mit.edu/">missing.csail.mit.edu</a>）：MIT 的免费公开课，补的是 shell、Git、命令行这些学校不教、却天天要用的东西。「学校不教，一生受用」的思路，同样是我们写这本书的出发点。</li>
  </ul>
  <p>向这两门课的作者与维护者致以诚挚的感谢。教育这件事，总得有人把缺的那一门补上；我们做的，不过是把这套思路从电脑搬到了手机上。</p>

  <h2 id="修订记录">修订记录 <a class="head-anchor" href="#修订记录">#</a></h2>
  <p>本作品持续更新中，最近一次更新在 2026 年 11 月 21 日。</p>
  <ul class="plain-list">
    <li>Acknowledgements: 门户新增「感谢与致敬」，致谢两门「缺失」课 (26/11/21)</li>
    <li>Update check: 全端检查更新与自动更新，更新源 GitHub Release (26/11/21)</li>
    <li>Source write-back: v1.9 全部 120 个区块纳入 source/ 构建，站点基建 lint 上线 (26/11/20)</li>
    <li>Appendices: 附录 A–H 扩写至每章约 3 万字，全书达到 353.8 万字 (26/11/15)</li>
    <li>Full expansion: 111 章全部扩写至 29K+ 字符/章，43.5 万 → 331.7 万字 (26/11/14)</li>
    <li>Deep edit: 120 章按可核对的公开事实逐章深编 (26/11/07)</li>
    <li>更早的修订记录见 GitHub 提交历史。</li>
  </ul>

  <h2 id="统计信息">统计信息 <a class="head-anchor" href="#统计信息">#</a></h2>
  <div class="stats">
    <div class="stat"><p class="text-4xl md:text-5xl font-black mb-2">120</p><small>个内容区块</small></div>
    <div class="stat"><p class="text-4xl md:text-5xl font-black mb-2">v1.9</p><small>最新中文版</small></div>
    <div class="stat"><p class="text-4xl md:text-5xl font-black mb-2">19</p><small>种语言完整翻译</small></div>
    <div class="stat"><p class="text-4xl md:text-5xl font-black mb-2">∞</p><small>免费开源</small></div>
  </div>

  <h2 id="许可">著作权、许可与声明 <a class="head-anchor" href="#许可">#</a></h2>
  <p>《你缺失的那门手机课》· 版权所有 © 2026 ClassTechStar。</p>
  <p>本书的内容与代码以 <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh">知识共享署名—非商业性使用—相同方式共享 4.0 国际版（CC BY-NC-SA 4.0）</a> 授权。你可以在协议允许的范围内自由分享、复制本书内容并进行二次创作，但请注明出处并附上链接，且不得用于商业目的。</p>
  <p>本书所有内容「按原样」提供，不含任何明示或暗示的担保。我们不保证书中任何部分绝对正确——手机界面的按钮位置随版本而变，操作时请以你的设备实际显示为准。若你认为书中叙述与其他来源相悖，请遵循你自己的判断，并把差异反馈给我们。</p>
</main>
<footer>
  <p>《你缺失的那门手机课》网页版 · <a href="https://github.com/ClassTechStar/Your-Missing-Phone-Class">GitHub</a> · CC BY-NC-SA 4.0</p>
  <p>手机是用会的，不是看会的。</p>
</footer>
{UPDATER}
{SWB}
{TOGGLE}
</body>
</html>
"""

out = ROOT / 'index.html'
out.write_text(HEAD, encoding='utf-8', newline='\n')
print(f'index.html written: {len(HEAD)} chars, TOC groups={len(groups)}, entries={toc_entries}')
