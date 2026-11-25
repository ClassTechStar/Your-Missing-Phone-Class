#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 v1.9/zh-CN.html 同步到 GitHub Pages 站点仓库（Yihggh.github.io）。

站点首页自 2026-11 起发布 v1.9 深编版（120 章），源必须用 v1.9；
曾经这里写死 v1.8，导致站点被降级回 84 章，勿再改回。

站点根目录与本书 `v1.9/` 目录层级不同：
    书页  <站点根>/v1.9/zh-CN.html   →  ../sw.js  ../manifest.webmanifest  ../icons/
    站点  <站点根>/index.html        →   sw.js     manifest.webmanifest     icons/
所以复制时必须把这三处相对路径降一级，否则 Service Worker 注册 404、
manifest 与图标全不可达（PWA 静默失效）。

Service Worker 的 scope 必须与 sw.js 脚本同深，否则浏览器直接拒绝注册
（SecurityError：脚本不在 scope 路径内），离线阅读随之失效；注册失败只被
.catch 里的 console.warn 吞掉，冒烟测试的「console 零 error」抓不到。
site 根页 scope 应为 './'，v1.9/ 单文件为 '../'，v1.9/zh-CN/ 分章页为 '../../'。

用法：
    python scripts/sync_site.py                       # 用默认站点路径
    python scripts/sync_site.py --dest <站点仓库路径>
    python scripts/sync_site.py --dry-run             # 只报告不写盘
"""

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from bookkit.split import fix_sw_scope  # noqa: E402

DEFAULT_DEST = Path.home() / 'Documents' / 'GitHub' / 'Yihggh.github.io'
# 站点根要带的 PWA 资产
# announcements.json 是页面运行时 fetch 的公告数据，缺了会在控制台打 404
# quiz.html + quiz/ 是章节自测页与题库，题库章节 id 是书页锚点，
# 必须与站点上发布的那一版书对齐（当前 v1.9）——错版会点进死链。
# robots.txt 是搜索引擎入口（方案 §6.4，sitemap 坐标写在里面）。
ASSETS = ['sw.js', 'manifest.webmanifest', 'announcements.json',
          'errata.html', 'languages.html', 'quiz.html', 'robots.txt']
ASSET_DIRS = ['icons', 'quiz']
# 字体只发布 woff2 子集（0.6MB）：7.8MB 的 TTF 母本只在仓库里留档，
# 不上网——CSS 双源声明下浏览器永远优先 woff2，省掉 90% 的字体流量。
FONT_SUBSET = 'MiSans-subset.woff2'
# 书页里的 og:image 是绝对地址（manifest 的 site_url + cover-og.png），
# 图必须一起部署到站点根，否则分享卡片抓不到图。
COVER = ('docs/promotion/assets/cover-og.png', 'cover-og.png')

# 书页 → 站点根，路径降一级
REWRITES = [
    ('../sw.js', 'sw.js'),
    ('../manifest.webmanifest', 'manifest.webmanifest'),
    ('../icons/', 'icons/'),
    ('../errata.html', 'errata.html'),
    ('../languages.html', 'languages.html'),
    ('../fonts/', 'fonts/'),   # MiSans 字体：书页 ../fonts/ → 站点根 fonts/
]


def rewrite(html: str) -> str:
    """书页 → 站点根：相对路径降一级，并把 SW scope 对齐到 sw.js 所在目录。"""
    for a, b in REWRITES:
        html = html.replace(a, b)
    return fix_sw_scope(html)


def site_base() -> str:
    """站点根 URL（manifest/languages.json 的 site_url，去尾斜杠）。"""
    man = ROOT / 'manifest' / 'languages.json'
    if not man.is_file():
        return ''
    try:
        return (json.loads(man.read_text(encoding='utf-8')).get('site_url') or '').rstrip('/')
    except Exception:
        return ''


def patch_sitemap(xml: str, base: str) -> str:
    """把站点顶层页补进 sitemap。

    bookkit split 只认识分章页，首页/勘误页/语言分级页/单文件书页不在其中；
    漏了它们，搜索引擎就看不到这几页。
    """
    if not base:
        return xml
    top = [f'{base}/',                       # 站点首页（书页本体）
           f'{base}/errata.html',             # 勘误页
           f'{base}/languages.html',         # 语言诚实分级页
           f'{base}/quiz.html',               # 章节自测页
           f'{base}/v1.9/zh-CN/',             # 分章目录（首页主入口）
           f'{base}/v1.9/zh-CN.html']        # 单文件整本书（离线备选）
    have = set(re.findall(r'<loc>([^<]+)</loc>', xml))
    add = [u for u in top if u not in have]
    if not add:
        return xml
    block = ''.join(f'  <url><loc>{u}</loc></url>\n' for u in add)
    if '</urlset>' not in xml:
        return xml
    return xml.replace('</urlset>', block + '</urlset>')


def fix_manifest(man_text: str, dest: Path) -> str:
    """按站点实际发布的内容裁剪 manifest 的快捷方式。

    题库自测页（quiz.html + quiz/）只在仓库里，站点没发布；manifest 里留着
    指向它的快捷方式，用户长按图标会跳到 404。保留的快捷方式必须真的在站点上存在。
    """
    try:
        data = json.loads(man_text)
    except Exception:
        return man_text
    scs = data.get('shortcuts') or []
    kept, dropped = [], []
    for s in scs:
        rel = (s.get('url') or '').split('#')[0]
        rel = rel[2:] if rel.startswith('./') else rel.lstrip('/')
        (kept if rel and (dest / rel).is_file() else dropped).append(s)
    for s in dropped:
        print(f'  ! manifest 快捷方式在站点上不可达，已移除：{s.get("name")} → {s.get("url")}')
    if not dropped:
        return man_text
    data['shortcuts'] = kept
    return json.dumps(data, ensure_ascii=False, indent=2) + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dest', type=Path, default=DEFAULT_DEST)
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()
    dest = args.dest

    if not (dest / '.git').is_dir():
        print(f'目标不是 git 仓库：{dest}')
        return 1

    # 站点首页发布 v1.9 深编版（120 章），不要用 v1.8（会把站点降级回 84 章）
    src_html = ROOT / 'v1.9' / 'zh-CN.html'
    if not src_html.is_file():
        print(f'源文件缺失：{src_html}')
        return 1

    # 首页是「分章优先」的落地页，不再是 13MB 单文件本身：
    # 主入口 → v1.9/zh-CN/（每章一页，首屏 ~180KB），单文件只作为离线备选。
    landing = ROOT / 'site-landing.html'
    if not landing.is_file():
        print(f'源文件缺失：{landing}')
        return 1
    landing_html = landing.read_text(encoding='utf-8')
    left = [a for a, _ in REWRITES if a in landing_html]
    if left:
        print(f'!! 落地页含未降级的相对路径：{left}')
        return 1

    plan = [('index.html', f'{len(landing_html):,} 字符（落地页）')]
    for a in ASSETS:
        if not (ROOT / a).is_file():
            print(f'!! 缺少资产：{a}')
            return 1
        plan.append((a, '复制'))
    # 分享卡片封面：推广物料目录可能已被清理，缺失时跳过而不是硬失败
    # （HTML 里的 og:image 仍指向站点 URL，图不在则分享卡片无缩略图，不影响阅读）
    if (ROOT / COVER[0]).is_file():
        plan.append((COVER[1], '分享卡片'))
    else:
        print(f'  ! 跳过封面 {COVER[0]}（文件不存在，如需恢复运行 scripts/gen_cover.py）')
    for d in ASSET_DIRS:
        n = len(list((ROOT / d).glob('*'))) if (ROOT / d).is_dir() else 0
        plan.append((d + '/', f'{n} 个文件'))
    if (ROOT / 'fonts' / FONT_SUBSET).is_file():
        plan.append(('fonts/' + FONT_SUBSET, '字体子集'))

    for name, note in plan:
        print(f'  → {name:24s} {note}')

    # 分章页（章节级 URL + sitemap/JSON-LD）：19 种语言全量构建后随站点发布
    import subprocess
    r = subprocess.run([sys.executable, 'scripts/build_all_sites.py',
                        '--out', 'dist/site', '--strict-budget'], cwd=ROOT)
    if r.returncode != 0:
        print('!! 分章化构建失败（超页级预算或构建错误），中止部署')
        return 1
    split_root = ROOT / 'dist' / 'site'
    n_cn = len(list((split_root / 'v1.9' / 'zh-CN').glob('*.html')))
    n_foreign = len(list((split_root / 'v1.8').glob('*/*.html')))
    plan.append((f'v1.9/zh-CN/（分章 {n_cn} 页）', '复制'))
    plan.append((f'v1.8/<lang>/（外语分章 {n_foreign} 页）', '复制'))
    plan.append(('sitemap.xml', '复制'))
    for name, note in plan[-3:]:
        print(f'  → {name:24s} {note}')

    if args.dry_run:
        print('（dry-run，未写盘）')
        return 0

    (dest / 'index.html').write_text(landing_html, encoding='utf-8', newline='')
    for a in ASSETS:
        if a == 'manifest.webmanifest':
            continue          # manifest 最后单独写（要按站点内容裁剪快捷方式）
        shutil.copy2(ROOT / a, dest / a)
    if (ROOT / COVER[0]).is_file():
        shutil.copy2(ROOT / COVER[0], dest / COVER[1])
    else:
        # 源已清理：把站点上残留的旧封面也一并清掉，避免新旧不一致
        stale = dest / COVER[1]
        if stale.is_file():
            stale.unlink()
            print(f'  ! 已删除站点上残留的旧封面 {COVER[1]}')
    for d in ASSET_DIRS:
        tgt = dest / d
        if tgt.exists():
            shutil.rmtree(tgt)
        shutil.copytree(ROOT / d, tgt)
    font_dir = dest / 'fonts'
    font_dir.mkdir(exist_ok=True)
    src_font = ROOT / 'fonts' / FONT_SUBSET
    if src_font.is_file():
        shutil.copy2(src_font, font_dir / FONT_SUBSET)
    # 旧的 TTF 若曾部署过，一并清掉（7.8MB 且浏览器不会下）
    stale_ttf = font_dir / 'MiSans-Normal.ttf'
    if stale_ttf.is_file():
        stale_ttf.unlink()
        print('  ! 已删除站点上的 7.8MB TTF 母本（浏览器用 woff2）')

    # 分章页与 sitemap：中文 v1.9 + 18 语 v1.8 章页
    shutil.copytree(split_root / 'v1.9', dest / 'v1.9', dirs_exist_ok=True)
    shutil.copytree(split_root / 'v1.8', dest / 'v1.8', dirs_exist_ok=True)

    # 单文件整本书（站点上 /v1.9/zh-CN.html）：它比站点根深一层，
    # ../sw.js、../errata.html 这类路径本来就是对的，只需修 SW scope。
    # 以前这里漏写，站点上留着上一版的旧书页（还带破损的嵌套 <p> 标记）。
    book_url = site_base() + '/v1.9/zh-CN.html'
    book_html = fix_sw_scope(src_html.read_text(encoding='utf-8'))
    # 首页改成落地页后，单文件不再是「站点根的副本」，canonical 必须指向自己
    book_html = re.sub(r'<link rel="canonical" href="[^"]*"',
                       f'<link rel="canonical" href="{book_url}"', book_html, count=1)
    (dest / 'v1.9' / 'zh-CN.html').write_text(book_html, encoding='utf-8', newline='')
    plan.append(('v1.9/zh-CN.html', '单文件整本书'))

    # sitemap：split 只写分章页与语言入口，顶层页在这里补进去
    sm = patch_sitemap((split_root / 'sitemap.xml').read_text(encoding='utf-8'),
                       site_base())
    (dest / 'sitemap.xml').write_text(sm, encoding='utf-8', newline='')

    # 19 种语言单文件入口（方案 §6.4：其余语言不能对搜索引擎 0 条、
    # 对读者不可读）：每语言一个完整单文件，hreflang 的备选也指向这里。
    v18_files = sorted((ROOT / 'v1.8').glob('*.html'))
    (dest / 'v1.8').mkdir(exist_ok=True)
    for f in v18_files:
        html = fix_sw_scope(f.read_text(encoding='utf-8'))
        (dest / 'v1.8' / f.name).write_text(html, encoding='utf-8', newline='')
    plan.append((f'v1.8/（{len(v18_files)} 语言单文件）', '复制'))
    print(f'  → v1.8/（{len(v18_files)} 语言单文件）           复制')

    # manifest：快捷方式按站点实际发布的内容裁剪（放在最后写，
    # 这样才能看到 v1.9/zh-CN.html 是否已就位）
    man = fix_manifest((ROOT / 'manifest.webmanifest').read_text(encoding='utf-8'), dest)
    (dest / 'manifest.webmanifest').write_text(man, encoding='utf-8', newline='')

    # 自检 1：站点 index.html 里不能再出现 ../
    out = (dest / 'index.html').read_text(encoding='utf-8')
    bad = [a for a, _ in REWRITES if a in out]
    if bad:
        print(f'!! 写盘后仍有未降级路径：{bad}')
        return 1

    # 自检 2：SW 的 scope 必须与 sw.js 脚本同深（否则浏览器拒绝注册）
    scope_bad = []
    for rel in ('index.html', 'v1.9/zh-CN.html',
                'v1.9/zh-CN/index.html', 'v1.9/zh-CN/di-ba-zhang.html'):
        f = dest / rel
        if not f.is_file():
            continue
        h = f.read_text(encoding='utf-8')
        m = re.search(r"serviceWorker\.register\(\s*['\"]([^'\"]*sw\.js)['\"]"
                      r"\s*,\s*\{\s*scope:\s*['\"]([^'\"]*)['\"]", h)
        if not m:
            scope_bad.append(f'{rel}: 未找到 SW 注册')
            continue
        script, scope = m.group(1), m.group(2)
        want = './' if '/' not in script else '../' * script.count('/')
        if scope != want:
            scope_bad.append(f'{rel}: scope={scope} 应为 {want}')
    if scope_bad:
        print('!! SW scope 不对：\n   ' + '\n   '.join(scope_bad))
        return 1

    # 自检 3：单文件书页必须与源一致（防止站点留着上一版旧书页）
    # canonical 由自检 5 单独校验（站点版指向自身、源版指向根），比对时剔除
    def _no_canon(h: str) -> str:
        return re.sub(r'<link rel="canonical" href="[^"]*">', '', h)
    src_sha = fix_sw_scope(src_html.read_text(encoding='utf-8'))
    if _no_canon((dest / 'v1.9' / 'zh-CN.html').read_text(encoding='utf-8')) != _no_canon(src_sha):
        print('!! v1.9/zh-CN.html 与源不一致')
        return 1

    # 自检 4：manifest 的快捷方式、start_url 在站点上都必须存在
    man = json.loads((dest / 'manifest.webmanifest').read_text(encoding='utf-8'))
    man_bad = []

    def _site_exists(rel: str) -> bool:
        """manifest 里的 URL 可能是目录（分章目录），按 index.html 判存在。"""
        t = dest / rel
        return t.is_file() or (t / 'index.html').is_file()

    for sc in man.get('shortcuts', []):
        r = (sc.get('url') or '').split('#')[0]
        r = r[2:] if r.startswith('./') else r.lstrip('/')
        if not r or not _site_exists(r):
            man_bad.append(f'快捷方式 {sc.get("name")} → {sc.get("url")}')
    for key in ('start_url',):
        r = (man.get(key) or '').split('#')[0]
        r = r[2:] if r.startswith('./') else r.lstrip('/')
        if r and not _site_exists(r):
            man_bad.append(f'{key} → {man.get(key)}')
    if man_bad:
        print('!! manifest 指向站点上不存在的页面：\n   ' + '\n   '.join(man_bad))
        return 1

    # 自检 5：canonical 必须在站点根与单文件书页上指向同一个规范 URL
    # （这两页是同一本书的两份副本，canonical 不统一 = 重复内容进索引）
    canon_root = site_base() + '/'
    canon_bad = []
    # 首页（落地页）指向站点根；单文件书页指向自身——两者已是不同内容，
    # 若仍让书页 canonical 指回根，搜索引擎会把 13MB 书页判成首页副本。
    for rel, want in (('index.html', canon_root),
                      ('v1.9/zh-CN.html', site_base() + '/v1.9/zh-CN.html')):
        f = dest / rel
        if not f.is_file():
            continue
        h = f.read_text(encoding='utf-8')
        tags = re.findall(r'<link rel="canonical" href="([^"]+)"', h)
        if len(tags) != 1:
            canon_bad.append(f'{rel}: canonical 有 {len(tags)} 个（必须恰好 1 个）')
        elif tags[0] != want:
            canon_bad.append(f'{rel}: canonical={tags[0]} 应为 {want}')
    # 分章页：每页恰好一个 canonical，且指向自己
    # （书页 head 里的 canonical 会被分章页继承，不清掉就会有两个，
    #   搜索引擎取第一个 —— 121 个章节页全被判成站点根的副本）
    split_dir = dest / 'v1.9' / 'zh-CN'
    n_checked = 0
    for f in sorted(split_dir.glob('*.html')):
        h = f.read_text(encoding='utf-8')
        tags = re.findall(r'<link rel="canonical" href="([^"]+)"', h)
        want = site_base() + '/v1.9/zh-CN/' + f.name
        if len(tags) != 1:
            canon_bad.append(f'v1.9/zh-CN/{f.name}: canonical 有 {len(tags)} 个')
        elif tags[0] != want:
            canon_bad.append(f'v1.9/zh-CN/{f.name}: canonical={tags[0]} 应为 {want}')
        n_checked += 1
    # 外语分章页：每语言抽查目录页与第一章，canonical 必须指向自己
    n_foreign = 0
    for lang_dir in sorted((dest / 'v1.8').iterdir()):
        if not lang_dir.is_dir():
            continue
        bp = ROOT / 'source' / 'translations' / lang_dir.name / 'book.json'
        if not bp.is_file():
            continue
        book = json.loads(bp.read_text(encoding='utf-8'))
        cid = book['chapters'][0]['id']
        for rel in (f'v1.8/{lang_dir.name}/index.html',
                    f'v1.8/{lang_dir.name}/{cid}.html'):
            f = dest / rel
            if not f.is_file():
                canon_bad.append(f'{rel}: 文件缺失')
                continue
            h = f.read_text(encoding='utf-8')
            tags = re.findall(r'<link rel="canonical" href="([^"]+)"', h)
            want = site_base() + '/' + rel
            if len(tags) != 1:
                canon_bad.append(f'{rel}: canonical 有 {len(tags)} 个')
            elif tags[0] != want:
                canon_bad.append(f'{rel}: canonical={tags[0]} 应为 {want}')
            n_foreign += 1
    if canon_bad:
        print('!! canonical 不统一：\n   ' + '\n   '.join(canon_bad[:10])
              + (f'\n   …共 {len(canon_bad)} 处' if len(canon_bad) > 10 else ''))
        return 1
    print(f'[canonical] 落地页 → {canon_root}；单文件书页 → {book_url}；'
          f'分章页 {n_checked} 页各自指向自己')

    # 自检 6：站点上的题库必须与站点发布的书同版，且章节 id 在书页里存在
    # （站点实供的语言必须对齐；其他语言的题库按各自版本对齐，但章节 id
    #   在站点这本 v1.9 里同样要能解析——否则读者点进去是死链）
    quiz_bad = []
    qm = dest / 'quiz' / 'manifest.json'
    if not qm.is_file():
        quiz_bad.append('quiz/manifest.json 缺失')
    else:
        banks = json.loads(qm.read_text(encoding='utf-8')).get('banks') or {}
        site_book = json.loads((ROOT / 'manifest' / 'languages.json')
                               .read_text(encoding='utf-8')).get('site_book') or {}
        book_html = dest / 'v1.9' / 'zh-CN.html'
        anchors = set()
        if book_html.is_file():
            anchors = set(re.findall(r'id="([^"]+)"',
                                     book_html.read_text(encoding='utf-8')))
        for lang, spec in banks.items():
            f = dest / 'quiz' / f'{lang}.json'
            if not f.is_file():
                quiz_bad.append(f'题库 {lang}.json 缺失')
                continue
            bank = json.loads(f.read_text(encoding='utf-8'))
            if bank.get('bookVersion') != spec.get('bookVersion'):
                quiz_bad.append(f'{lang}.json bookVersion={bank.get("bookVersion")} '
                                f'与 manifest 登记的 {spec.get("bookVersion")} 不一致')
            if lang == site_book.get('lang'):
                # 站点自测页加载的就是这一份，必须与站点发布的书同版
                if spec.get('bookVersion') != site_book.get('version'):
                    quiz_bad.append(f'{lang}.json 对齐 {spec.get("bookVersion")}，'
                                    f'但站点发布的是 {site_book.get("version")}')
            miss = [c.get('id') for c in bank.get('chapters') or []
                    if c.get('id') not in anchors]
            if miss:
                quiz_bad.append(f'{lang}.json 有 {len(miss)} 个章节 id 在书页里不存在')
    if quiz_bad:
        print('!! 题库与站点不一致：\n   ' + '\n   '.join(quiz_bad))
        return 1

    print(f'\n已同步到 {dest}')
    print('下一步：git add -A && git commit && git push（见维护手册）')
    return 0


if __name__ == '__main__':
    sys.exit(main())
