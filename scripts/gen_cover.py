#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成传播用的三张封面（走 Playwright 渲染 HTML，文字是矢量排版而非 AI 生图）。

产物（提交入库，供 README 首屏、站点 og:image 与各渠道上传）：
    docs/promotion/assets/cover-og.png           1200×630   站点分享卡片 / GitHub 社交预览
    docs/promotion/assets/cover-xiaohongshu.png  1080×1440  小红书笔记封面（3:4）
    docs/promotion/assets/cover-bilibili.png     1920×1080  B 站视频封面（16:9）

设计约束：
  · 只用本机字体（微软雅黑 / PingFang / Noto），不依赖网络字体，离线可复现；
  · 文字全部来自本仓库的真实数据，不写死版本号以外的数字；
  · 同一套视觉语言：深蓝渐变 #0F172A→#1E3A5F→#165DFF，点缀色 #FF6B35。

用法：
    python scripts/gen_cover.py            # 生成三张
    python scripts/gen_cover.py --only og  # 只生成一张（og / xiaohongshu / bilibili）
"""

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / 'docs' / 'promotion' / 'assets'

TITLE_ZH = '你缺失的那门手机课'
TITLE_EN = 'YOUR MISSING PHONE CLASS'
TAGLINE = '从「手机芯片是什么」讲到「上架你的第一个 App」'
STATS = [('84', '章'), ('11', '篇'), ('19', '种语言'), ('74', '本 PDF')]
CHIPS = ['防诈骗', '适老化', 'AI 编程', '离线可读']
FOOTER = 'github.com/ClassTechStar/Your-Missing-Phone-Class · QQ 群 1074995524'

BASE_CSS = """
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { width: 100%; height: 100%; }
body {
  font-family: 'Microsoft YaHei UI', 'Microsoft YaHei', 'PingFang SC', 'Noto Sans SC', sans-serif;
  background: #0F172A;
  color: #fff;
  overflow: hidden;
  -webkit-font-smoothing: antialiased;
}
.stage {
  position: relative; width: 100%; height: 100%;
  background:
    radial-gradient(1200px 700px at 78% 12%, rgba(22, 93, 255, 0.55), transparent 62%),
    radial-gradient(900px 600px at 8% 96%, rgba(255, 107, 53, 0.22), transparent 60%),
    linear-gradient(135deg, #0F172A 0%, #1E3A5F 52%, #165DFF 130%);
}
/* 细网格：给深色底加一点"工程感"，透明度压到不抢字 */
.stage::before {
  content: ''; position: absolute; inset: 0;
  background-image:
    repeating-linear-gradient(0deg, rgba(255,255,255,0.045) 0 1px, transparent 1px 44px),
    repeating-linear-gradient(90deg, rgba(255,255,255,0.045) 0 1px, transparent 1px 44px);
  mask-image: radial-gradient(120% 100% at 50% 40%, #000 30%, transparent 88%);
}
.badge {
  display: inline-flex; align-items: center; gap: 10px;
  border: 1px solid rgba(190, 214, 255, 0.35);
  background: rgba(255, 255, 255, 0.07);
  color: #D6E4FF; border-radius: 999px;
  font-weight: 500; letter-spacing: 0.04em;
}
.dot { width: 8px; height: 8px; border-radius: 999px; background: #4ADE80; box-shadow: 0 0 12px #4ADE80; }
.title { font-weight: 900; line-height: 1.08; letter-spacing: -0.015em; text-shadow: 0 8px 30px rgba(0,0,0,0.35); }
.title-en { color: #8FB4FF; font-family: 'Segoe UI', Arial, sans-serif; letter-spacing: 0.24em; font-weight: 600; }
.rule { background: #FF6B35; border-radius: 999px; }
.tagline { color: #C9D8F0; }
.stats { display: flex; align-items: center; }
.stat-num { font-weight: 800; font-family: 'Segoe UI', Arial, sans-serif; }
.stat-label { color: #92A6C7; }
.stat-sep { background: rgba(255,255,255,0.16); }
/* 手机：不画真实 App，只表达"随身的一本书" */
.phone { position: relative; border-radius: 52px; background: linear-gradient(160deg, #0B1020, #131C33);
  border: 2px solid rgba(255,255,255,0.16);
  box-shadow: 0 50px 90px rgba(0,0,0,0.55), inset 0 0 0 8px rgba(10,16,30,0.9); }
.phone::before { content: ''; position: absolute; left: 50%; transform: translateX(-50%);
  width: 30%; height: 22px; background: #0B1020; border-radius: 0 0 16px 16px; }
.screen { position: absolute; inset: 14px; border-radius: 40px; overflow: hidden;
  background: linear-gradient(165deg, #165DFF 0%, #0E2A66 55%, #0A1735 100%);
  display: flex; flex-direction: column; justify-content: center; padding: 34px 30px; gap: 14px; }
.screen::after { content: ''; position: absolute; inset: 0;
  background: radial-gradient(400px 260px at 20% 0%, rgba(255,255,255,0.22), transparent 70%); }
.bar { height: 10px; border-radius: 999px; background: rgba(255,255,255,0.55); position: relative; z-index: 1; }
.pill { position: relative; z-index: 1; align-self: flex-start; background: #FF6B35; color: #fff;
  font-weight: 700; border-radius: 12px; box-shadow: 0 10px 24px rgba(255,107,53,0.35); }
.chip { position: absolute; background: rgba(8, 16, 34, 0.82); border: 1px solid rgba(150, 190, 255, 0.35);
  color: #DCE9FF; border-radius: 999px; font-weight: 600; backdrop-filter: blur(6px);
  box-shadow: 0 12px 30px rgba(0,0,0,0.35); white-space: nowrap; }
.footer { color: #7C90B4; letter-spacing: 0.02em; }
.version { position: absolute; color: #A9BEE0; font-family: 'Segoe UI', Arial, sans-serif; }
"""


def banner(scale: float, width: int, height: int) -> str:
    """横版：左文右图。og（1200×630）与 B 站（1920×1080）共用，靠 scale 缩放。"""
    s = scale
    stats = ''.join(
        f'<div class="stat"><div class="stat-num" style="font-size:{30 * s:.0f}px">{n}</div>'
        f'<div class="stat-label" style="font-size:{15 * s:.0f}px">{u}</div></div>'
        + (f'<div class="stat-sep" style="width:1px;height:{30 * s:.0f}px;margin:0 {18 * s:.0f}px"></div>'
           if i < len(STATS) - 1 else '')
        for i, (n, u) in enumerate(STATS))
    chips = ''
    spots = [(-13, 13), (84, 5), (-15, 68), (82, 52)]   # 相对手机宽高的百分比位置
    for (label, (x, y)) in zip(CHIPS, spots):
        chips += (f'<div class="chip" style="left:{x}%;top:{y}%;font-size:{16 * s:.0f}px;'
                  f'padding:{9 * s:.0f}px {18 * s:.0f}px">{label}</div>')
    return f"""
<div class="stage" style="display:flex;align-items:center;padding:{56 * s:.0f}px {64 * s:.0f}px">
  <div style="flex:1;min-width:0">
    <div class="badge" style="font-size:{16 * s:.0f}px;padding:{10 * s:.0f}px {20 * s:.0f}px">
      <span class="dot"></span>开源免费 · CC BY-NC-SA · 离线可读
    </div>
    <div class="title" style="font-size:{74 * s:.0f}px;margin-top:{30 * s:.0f}px">
      你缺失的<br>那门手机课
    </div>
    <div class="title-en" style="font-size:{19 * s:.0f}px;margin-top:{22 * s:.0f}px">{TITLE_EN}</div>
    <div class="rule" style="width:{58 * s:.0f}px;height:{6 * s:.0f}px;margin:{26 * s:.0f}px 0 {22 * s:.0f}px"></div>
    <div class="tagline" style="font-size:{23 * s:.0f}px">{TAGLINE}</div>
    <div class="stats" style="margin-top:{40 * s:.0f}px;gap:{16 * s:.0f}px">{stats}</div>
  </div>
  <div style="position:relative;width:{320 * s:.0f}px;height:{500 * s:.0f}px;margin-left:{44 * s:.0f}px">
    <div class="phone" style="position:absolute;inset:0">
      <div class="screen">
        <div style="position:relative;z-index:1;color:#BFD4FF;font-size:{15 * s:.0f}px;letter-spacing:.16em">V1.8 · 19 LANGUAGES</div>
        <div class="bar" style="width:78%;height:{16 * s:.0f}px"></div>
        <div class="bar" style="width:56%"></div>
        <div class="bar" style="width:66%"></div>
        <div class="pill" style="font-size:{16 * s:.0f}px;padding:{12 * s:.0f}px {22 * s:.0f}px;margin-top:{10 * s:.0f}px">开始阅读</div>
      </div>
    </div>
    {chips}
  </div>
</div>
"""


def portrait(scale: float) -> str:
    """竖版（小红书 3:4）：标题在上、手机在下，信息密度降一档以便缩略图可读。"""
    s = scale
    stats = ''.join(
        f'<div style="text-align:center"><div style="font-weight:800;font-size:{34 * s:.0f}px;'
        f'font-family:\'Segoe UI\',Arial,sans-serif">{n}</div>'
        f'<div style="color:#92A6C7;font-size:{17 * s:.0f}px;margin-top:{6 * s:.0f}px">{u}</div></div>'
        for n, u in STATS)
    chips = ''
    for label, (x, y) in zip(CHIPS, [(54, 2), (-8, 4), (-8, 78), (54, 86)]):
        chips += (f'<div class="chip" style="left:{x}%;top:{y}%;font-size:{22 * s:.0f}px;'
                  f'padding:{12 * s:.0f}px {24 * s:.0f}px">{label}</div>')
    return f"""
<div class="stage" style="display:flex;flex-direction:column;align-items:center;
     justify-content:center;padding:{64 * s:.0f}px {72 * s:.0f}px;gap:0">
  <div class="badge" style="font-size:{22 * s:.0f}px;padding:{12 * s:.0f}px {26 * s:.0f}px">
    <span class="dot"></span>开源免费 · 手机离线也能读
  </div>
  <div class="title" style="font-size:{86 * s:.0f}px;margin-top:{34 * s:.0f}px;text-align:center">
    你缺失的<br>那门手机课
  </div>
  <div class="title-en" style="font-size:{22 * s:.0f}px;margin-top:{24 * s:.0f}px">{TITLE_EN}</div>
  <div class="rule" style="width:{72 * s:.0f}px;height:{7 * s:.0f}px;margin:{28 * s:.0f}px 0 {20 * s:.0f}px"></div>
  <div class="tagline" style="font-size:{26 * s:.0f}px;text-align:center">{TAGLINE}</div>
  <div style="position:relative;width:{420 * s:.0f}px;height:{520 * s:.0f}px;margin-top:{40 * s:.0f}px">
    <div class="phone" style="position:absolute;inset:0">
      <div class="screen" style="gap:{16 * s:.0f}px">
        <div style="position:relative;z-index:1;color:#BFD4FF;font-size:{17 * s:.0f}px;letter-spacing:.16em">V1.8 · 84 CHAPTERS</div>
        <div class="bar" style="width:80%;height:{18 * s:.0f}px"></div>
        <div class="bar" style="width:58%"></div>
        <div class="bar" style="width:68%"></div>
        <div class="pill" style="font-size:{19 * s:.0f}px;padding:{14 * s:.0f}px {26 * s:.0f}px;margin-top:{12 * s:.0f}px">开始阅读</div>
      </div>
    </div>
    {chips}
  </div>
  <div style="display:flex;justify-content:space-between;width:100%;margin-top:{44 * s:.0f}px;
       border-top:1px solid rgba(255,255,255,.12);padding-top:{26 * s:.0f}px">
    {stats}
  </div>
  <div class="footer" style="font-size:{19 * s:.0f}px;margin-top:{24 * s:.0f}px;text-align:center">
    GitHub 搜「Your-Missing-Phone-Class」· 免费下载 PDF / App
  </div>
</div>
"""


PRESETS = {
    # name: (宽, 高, html)
    'og': (1200, 630, banner(1.0, 1200, 630)),
    'xiaohongshu': (1080, 1440, portrait(1.0)),
    'bilibili': (1920, 1080, banner(1.5, 1920, 1080)),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--only', choices=sorted(PRESETS), help='只生成指定的一张')
    args = ap.parse_args()

    from playwright.sync_api import sync_playwright

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    targets = {k: v for k, v in PRESETS.items() if not args.only or k == args.only}

    with sync_playwright() as p:
        browser = p.chromium.launch()
        for name, (w, h, body) in targets.items():
            page = browser.new_page(viewport={'width': w, 'height': h}, device_scale_factor=1)
            page.set_content(f'<!DOCTYPE html><html><head><meta charset="utf-8">'
                             f'<style>{BASE_CSS}</style></head><body>{body}</body></html>')
            page.wait_for_timeout(150)
            out = OUT_DIR / f'cover-{name}.png'
            page.screenshot(path=str(out))
            page.close()
            print(f'  → {out.relative_to(ROOT)}  {w}×{h}  {out.stat().st_size / 1024:.0f} KB')
        browser.close()
    return 0


if __name__ == '__main__':
    sys.exit(main())
