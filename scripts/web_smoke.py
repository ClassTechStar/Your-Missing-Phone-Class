#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""浏览器冒烟测试（Playwright，零断言框架）。

本地起 http.server，逐页打开 index.html + v1.8 全部语言页，断言：
- 页面加载成功（200、无 crash）
- console 零 error
- 侧栏目录锚点全部可解析（getElementById 命中）
- 章节标题数量符合预期（v1.8 = 84）

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


def main():
    base = f'http://127.0.0.1:{PORT}'
    if '--base' in sys.argv:
        base = sys.argv[sys.argv.index('--base') + 1]
    else:
        threading.Thread(target=serve, daemon=True).start()

    targets = [('index.html', None)] + [(f'v1.8/{l}.html', EXPECT_H3) for l in LANGS]
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
                ok = (not errors) and (not missing) and (expect_h3 is None or n_h3 == expect_h3)
                status = '✓' if ok else '✗'
                detail = []
                if errors:
                    detail.append(f'console×{len(errors)}: {errors[0][:60]}')
                if missing:
                    detail.append(f'锚点缺失×{len(missing)}: {missing[:3]}')
                if expect_h3 and n_h3 != expect_h3:
                    detail.append(f'h3={n_h3}≠{expect_h3}')
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
