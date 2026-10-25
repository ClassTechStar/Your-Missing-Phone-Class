#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""浏览器冒烟测试（Playwright，零断言框架）。

本地起 http.server，逐页打开 index.html + v1.8 全部语言页，断言：
- 页面加载成功（200、无 crash）
- console 零 error
- 侧栏目录锚点全部可解析（getElementById 命中）
- 章节标题数量符合预期（v1.8 = 84）
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

    targets = ([('index.html', None), ('quiz.html', None)]
               + [(f'v1.8/{l}.html', EXPECT_H3) for l in LANGS])
    fails = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page()
        for path, expect_h3 in targets:
            errors = []
            page.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
            page.on('pageerror', lambda e: errors.append(str(e)))
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
                ok = (not errors) and (not missing) and (not pwa) \
                    and (expect_h3 is None or n_h3 == expect_h3)
                status = '✓' if ok else '✗'
                detail = []
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
            errors.clear()
        browser.close()
    print(f'\n== {len(targets)} 页，失败 {len(fails)}')
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
