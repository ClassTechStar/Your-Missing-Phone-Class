#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""浏览器冒烟测试（Playwright，零断言框架）。

本地起 http.server，逐页打开 index.html + v1.8 全部语言页 + v1.9 + 分章页，断言：
- 页面加载成功（200、无 crash）
- console 零 error
- 侧栏目录锚点全部可解析（getElementById 命中）
- 章节标题数量符合预期（v1.8 = 84；v1.9 = 120；章节页 = 1）
- PWA：manifest 可解析且图标齐全；Service Worker 注册成功并激活

用法：python scripts/web_smoke.py [--base http://127.0.0.1:8642]
退出码：0 全过；1 有失败页。
"""
import http.server
import socketserver
import sys
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
PORT = 8642
LANGS = sorted(p.stem for p in (ROOT / 'v1.8').glob('*.html'))
EXPECT_H3 = 84


def serve():
    class H(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(('127.0.0.1', PORT), H) as httpd:
        httpd.serve_forever()


def check_pwa(page, base):
    """PWA 断言：manifest 可解析、图标齐全、SW 注册并激活。"""
    problems = []
    href = page.evaluate(
        "() => { const l = document.querySelector('link[rel=manifest]'); return l && l.href; }")
    if not href:
        return ['缺少 <link rel="manifest">']
    try:
        resp = page.request.get(href)
        if resp.status != 200:
            problems.append(f'manifest HTTP {resp.status}')
        else:
            man = resp.json()
            for key in ('name', 'short_name', 'start_url', 'display', 'icons'):
                if key not in man:
                    problems.append(f'manifest 缺字段 {key}')
            for ic in man.get('icons', []):
                r = page.request.get(base + '/' + ic['src'].lstrip('./'))
                if r.status != 200:
                    problems.append(f"图标不可达 {ic['src']} ({r.status})")
    except Exception as e:
        problems.append(f'manifest 解析失败：{str(e)[:60]}')

    # SW 的 scope 必须与 sw.js 脚本同深：scope 比脚本浅时浏览器直接拒绝注册
    #（SecurityError），而注册失败只被 .catch 的 console.warn 吞掉，
    # 「console 零 error」与 navigator.serviceWorker.ready 都发现不了
    #（ready 是同源级的，别的页面注册成功就会让它 resolve）。
    swreg = page.evaluate("""async () => {
        const RE = /serviceWorker\\.register\\(\\s*['"]([^'"]*sw\\.js)['"]\\s*,\\s*\\{\\s*scope:\\s*['"]([^'"]*)['"]/;
        const html = document.documentElement.innerHTML || '';
        let m = html.match(RE);
        if (!m) {
            // 分章页把内联脚本外置到了 assets/book.js
            const s = document.querySelector('script[src*="book.js"]');
            if (s) {
                try { m = (await (await fetch(s.src)).text()).match(RE); } catch (e) {}
            }
        }
        if (!m) return {ok: true, note: 'no-explicit-scope'};
        const script = m[1], scope = m[2];
        const want = script.includes('/') ? '../'.repeat(script.split('/').length - 1) : './';
        if (scope !== want) return {ok: false, why: 'scope=' + scope + ' 应为 ' + want};
        // 真注册一次：scope 与脚本路径不匹配时浏览器会抛 SecurityError
        try {
            await navigator.serviceWorker.register(script, {scope: scope});
            return {ok: true};
        } catch (e) {
            return {ok: false, why: '注册被拒绝：' + (e && e.name ? e.name : String(e))};
        }
    }""")
    if not swreg.get('ok'):
        problems.append(f"SW scope：{swreg.get('why', '未知')}")

    sw = page.evaluate("""async () => {
        // SW 从注册到 active 需要几秒（安装 + 激活），不能加载完就查
        const race = new Promise((_, rej) =>
            setTimeout(() => rej(new Error('timeout')), 15000));
        try {
            const reg = await Promise.race([navigator.serviceWorker.ready, race]);
            return reg.active ? 'active'
                 : reg.installing ? 'installing'
                 : reg.waiting ? 'waiting' : 'registered';
        } catch (e) {
            const reg = await navigator.serviceWorker.getRegistration();
            return reg ? 'pending' : 'no-registration';
        }
    }""")
    if sw != 'active':
        problems.append(f'SW 状态：{sw}')
    return problems


def main():
    base = f'http://127.0.0.1:{PORT}'
    if '--base' in sys.argv:
        base = sys.argv[sys.argv.index('--base') + 1]
    else:
        threading.Thread(target=serve, daemon=True).start()

    targets = ([('index.html', None), ('quiz.html', None), ('v1.8/zh-CN.html?safe=1', None),
                ('v1.9/zh-CN.html', 120),
                # 治理页：勘误页、语言诚实分级页、PDF/离线分发页
                ('errata.html', None), ('languages.html', None), ('pdf.html', None)]
               + [(f'v1.8/{l}.html', EXPECT_H3) for l in LANGS])
    # 分章页（bookkit split 构建存在时纳入冒烟）：书首页 + 首个章节页
    if (ROOT / 'dist' / 'site' / 'v1.9' / 'zh-CN' / 'index.html').is_file():
        targets += [('dist/site/v1.9/zh-CN/index.html', None),
                    ('dist/site/v1.9/zh-CN/di-ling-zhang.html', 1),
                    # 策展路径页（方案 §7）：进度联动 JS 也要零 console error
                    ('dist/site/v1.9/zh-CN/gei-ba-ma-de-shi-zhang.html', None)]
    # 外语分章页（W3-4）：英语 + 阿拉伯语（RTL）+ 日语各抽一章
    for lang, cid in (('en', 'di-yi-zhang'), ('ar', 'di-yi-zhang'), ('ja', 'di-yi-zhang')):
        p = ROOT / 'dist' / 'site' / 'v1.8' / lang / f'{cid}.html'
        if p.is_file() and (ROOT / 'dist' / 'site' / 'v1.8' / lang / 'index.html').is_file():
            targets += [(f'dist/site/v1.8/{lang}/index.html', None),
                        (f'dist/site/v1.8/{lang}/{cid}.html', 1)]
    fails = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page()
        # 外部 CDN（tailwind/fontawesome 等）不参与冒烟：拦截并回 200 空 JS/CSS，
        # 避免本机网络对 CDN 的波动把 DOMContentLoaded 拖过 30s
        page.route('**/*', lambda route: route.fulfill(status=200, body='window.tailwind = window.tailwind || {};')
                   if route.request.url.startswith('http') and '127.0.0.1' not in route.request.url
                   else route.continue_())
        # console 监听只注册一次：闭包按名字晚绑定，循环里每页重复注册会让
        # 同一条错误被 N 个历史处理器各记一遍（第 20 页的一条 404 会显示 ×20）。
        current = {'errors': []}
        page.on('console', lambda m: current['errors'].append(m.text) if m.type == 'error' else None)
        page.on('pageerror', lambda e: current['errors'].append(str(e)))
        for path, expect_h3 in targets:
            errors = current['errors'] = []
            url = f'{base}/{path}'
            try:
                page.goto(url, wait_until='domcontentloaded', timeout=30000)
                page.wait_for_timeout(300)
                # 锚点解析
                missing = page.evaluate('''() => {
                    const miss = [];
                    document.querySelectorAll('#toc-list a[href^="#"]').forEach(a => {
                        if (!document.getElementById(a.getAttribute('href').slice(1)))
                            miss.push(a.getAttribute('href'));
                    });
                    return miss;
                }''')
                n_h3 = page.evaluate("document.querySelectorAll('.content-section > h3').length") \
                    if expect_h3 else None
                pwa = check_pwa(page, base)
                # 自测页的功能断言：题库 fetch 失败时页面不报错、只是空着，
                # 「console 零 error」看不出来，所以单独数章节卡片。
                quiz_bad = None
                if path.endswith('quiz.html'):
                    page.wait_for_timeout(600)
                    q = page.evaluate("""() => ({
                        chips: document.querySelectorAll('#grid .chip').length,
                        info: (document.getElementById('bankInfo') || {}).textContent || '',
                        grid: (document.getElementById('grid') || {}).textContent || ''
                    })""")
                    if q['chips'] < 50:
                        quiz_bad = f'题库未渲染（chips={q["chips"]}，{q["grid"][:40]}）'
                ok = (not errors) and (not missing) and (not pwa) and (not quiz_bad) \
                    and (expect_h3 is None or n_h3 == expect_h3)
                status = '✓' if ok else '✗'
                detail = []
                if quiz_bad:
                    detail.append(quiz_bad)
                if errors:
                    detail.append(f'console×{len(errors)}: {errors[0][:60]}')
                if missing:
                    detail.append(f'锚点缺失×{len(missing)}: {missing[:3]}')
                if expect_h3 and n_h3 != expect_h3:
                    detail.append(f'h3={n_h3}≠{expect_h3}')
                if pwa:
                    detail.append(f'PWA: {pwa[0]}')
                print(f'{status} {path}: {detail[0] if detail else "ok"}')
                if not ok:
                    fails.append(path)
            except Exception as e:
                print(f'✗ {path}: 加载失败 {str(e)[:80]}')
                fails.append(path)
        browser.close()
    print(f'\n== {len(targets)} 页，失败 {len(fails)}')
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
