#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""为 v1.8 PDF 创建新的 GitHub Release 并上传 19 个资产。

Release 一旦发布即 immutable（不能追加资产、改标签名），所以流程固定为：
    草稿创建 → 逐个上传资产 → draft=false 发布

token 从 git credential 取，不写入任何文件。

用法：
    python scripts/publish_pdf_release.py            # 干跑，只打印计划
    python scripts/publish_pdf_release.py --apply    # 真正创建并上传
"""

import argparse
import json
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OWNER, REPO = 'ClassTechStar', 'Your-Missing-Phone-Class'
PDF_DIR = ROOT / '手机课-LaTeX-PDF' / 'pdf' / 'v1.8'
API = f'https://api.github.com/repos/{OWNER}/{REPO}'
UPLOAD = f'https://uploads.github.com/repos/{OWNER}/{REPO}'

TAG = 'latex-pdf-v1.8-20261028'
NAME = '手机课 · LaTeX 排版 PDF（v1.8 · 书名统一）'
BODY = """《你缺失的那门手机课》v1.8 排版 PDF，19 种语言各一本。

本次更新：
- 书名统一为《你缺失的那门手机课》（英文 Your Missing Phone Class，
  其余语言为对应译名）。此前只有简体中文版书名正确，其余 18 种语言
  的封面与元数据仍是各自旧名。
- 全部用最新 HTML 重新排版，与线上阅读内容一致。

XeLaTeX 排版，带目录书签，RTL 语言（阿拉伯语/希伯来语）已做从右到左。
CC BY-NC-SA 4.0，免费获取，禁止售卖。
"""


def token() -> str:
    out = subprocess.run(
        ['git', 'credential', 'fill'],
        input='protocol=https\nhost=github.com\n\n',
        capture_output=True, text=True, timeout=30).stdout
    for line in out.splitlines():
        if line.startswith('password='):
            return line.split('=', 1)[1]
    return ''


def api(tok, method, url, data=None, raw=None, ctype='application/json'):
    req = urllib.request.Request(url, method=method)
    req.add_header('Authorization', f'token {tok}')
    req.add_header('Accept', 'application/vnd.github+json')
    req.add_header('User-Agent', 'phoneclass-release')
    body = None
    if raw is not None:
        body = raw
        req.add_header('Content-Type', ctype)
    elif data is not None:
        body = json.dumps(data, ensure_ascii=False).encode()
        req.add_header('Content-Type', 'application/json')
    if body:
        req.data = body
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.loads(r.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f'  HTTP {e.code}: {e.read().decode()[:300]}')
        raise


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()

    pdfs = sorted(PDF_DIR.glob('*.pdf'))
    if len(pdfs) != 19:
        print(f'PDF 数量应为 19，实际 {len(pdfs)}')
        return 1
    total = sum(p.stat().st_size for p in pdfs)
    print(f'待上传 {len(pdfs)} 个 PDF，共 {total/1024/1024:.0f} MB')
    print(f'tag: {TAG}')
    if not args.apply:
        print('（干跑，未创建）')
        return 0

    tok = token()
    if not tok:
        print('未取到 token')
        return 1

    print('创建草稿 Release…')
    rel = api(tok, 'POST', f'{API}/releases', {
        'tag_name': TAG, 'name': NAME, 'body': BODY,
        'draft': True, 'prerelease': False,
    })
    rid = rel['id']
    print(f'  草稿已建 id={rid}')

    for p in pdfs:
        print(f'  上传 {p.name} …', end=' ', flush=True)
        api(tok, 'POST', f'{UPLOAD}/releases/{rid}/assets?name={p.name}',
            raw=p.read_bytes(), ctype='application/pdf')
        print('ok')

    print('发布…')
    api(tok, 'PATCH', f'{API}/releases/{rid}', {'draft': False})
    print(f'\n完成：https://github.com/{OWNER}/{REPO}/releases/tag/{TAG}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
