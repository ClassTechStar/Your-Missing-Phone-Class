"""index：从 manifest 生成 index.html 的语言卡片块与统计数字（AUTOGEN 区域）。

- 卡片、徽章、渐变、语言描述全部来自 manifest/languages.json，不再手写；
- 幂等：重复运行结果一致；
- --check 只比对不写盘，供 CI 做"文档漂移"门禁。
"""

import re
from pathlib import Path

from .model import ERROR, INFO, Issue

START = '            <!-- AUTOGEN:languages-{ver} START - 由 python -m bookkit index 生成，勿手改 -->'
END = '            <!-- AUTOGEN:languages-{ver} END -->'

BLOCK = """{start}
            <div class="mb-12 fade-in">
                <div class="text-center mb-8">
                    <span class="{badge_classes} rounded-full text-sm font-semibold">
                        <i class="{badge_icon} mr-1"></i>{badge_text}
                    </span>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">

{cards}
                </div>
            </div>
{end}"""

CARD = """                <a href="{ver}/{code}.html" class="lang-card block bg-gradient-to-br {gradient} {card_extra}">
                    <div class="flex items-center gap-3 mb-2">
                        <span class="text-3xl">{flag}</span>
                        <div>
                            <h4 class="font-bold text-dark">{name}</h4>
                            <p class="text-xs {label_classes} font-semibold">{label}</p>
                        </div>
                    </div>
                    <p class="text-sm text-gray-600">{desc}</p>
                </a>"""

RE_BLOCK = re.compile(r'[ \t]*<!-- AUTOGEN:languages-(?P<ver>v[\d.]+) START[^>]*-->'
                      r'[\s\S]*?<!-- AUTOGEN:languages-(?P=ver) END -->')
RE_STAT = re.compile(r'(<p class="text-4xl md:text-5xl font-black mb-2">)([^<]*)(</p>)')


def _card(mf, version: str, code: str) -> str:
    meta = mf.lang_meta(code)
    card = mf.data.get('cards', {}).get(version, {})
    desc = mf.data.get('language_descriptions', {}).get(version, {}).get(code)
    if desc is None:
        desc = f'{meta.get("name", code)} {version}'
    suffix = card.get('label_suffix', '')
    label = f'{version} {suffix}'.strip()
    return CARD.format(
        ver=version, code=code,
        gradient=meta.get('gradient', 'from-slate-50 to-slate-100'),
        card_extra=card.get('card_extra', 'border border-gray-200 rounded-xl p-5 hover:shadow-lg'),
        flag=meta.get('flag', '🌐'),
        name=meta.get('name', code),
        label_classes=card.get('label_classes', 'text-gray-500'),
        label=label, desc=desc)


def render_block(mf, version: str) -> str:
    card_cfg = mf.data.get('cards', {}).get(version, {})
    codes = mf.language_codes(version)
    cards = '\n\n'.join(_card(mf, version, c) for c in codes)
    return BLOCK.format(
        start=START.format(ver=version),
        badge_classes=card_cfg.get('badge_classes', 'inline-block px-4 py-1.5 bg-gray-100 text-gray-600'),
        badge_icon=card_cfg.get('badge_icon', 'fas fa-book'),
        badge_text=card_cfg.get('badge_text', version),
        cards=cards,
        end=END.format(ver=version))


def _stats(mf, version: str) -> list:
    files = mf.html_files(version)
    base = mf.version_dir(version) / f'{mf.baseline_lang(version)}.html'
    sections = 0
    if base.is_file():
        from . import textutil as T
        sections = len(T.section_ids(base.read_text(encoding='utf-8')))
    return [str(mf.expect_sections(version) or sections), version, str(len(files))]


def render_index(mf) -> str:
    path = mf.root / mf.data.get('claims', {}).get('index', 'index.html')
    html = path.read_text(encoding='utf-8')

    versions = [v for v in mf.versions if mf.html_files(v)]
    # 清除已下线版本的 AUTOGEN 块（目录移除/归档后卡片不应残留）
    for m in list(RE_BLOCK.finditer(html)):
        ver = m.group(1)
        if ver not in versions:
            start = html.rfind(chr(10), 0, m.start()) + 1
            html = html[:start] + html[m.end():]
    for ver in versions:
        block = render_block(mf, ver)
        pat = re.compile(r'[ \t]*<!-- AUTOGEN:languages-' + re.escape(ver) + r' START[^>]*-->'
                         r'[\s\S]*?<!-- AUTOGEN:languages-' + re.escape(ver) + r' END -->')
        if pat.search(html):
            html = pat.sub(lambda m: block, html, count=1)
        else:
            # 新版本：插在最后一个 AUTOGEN 块之后
            last = list(RE_BLOCK.finditer(html))
            if last:
                pos = last[-1].end()
                html = html[:pos] + '\n\n' + block + html[pos:]

    if versions:
        stats = _stats(mf, mf.latest_version())
        counter = {'i': 0}

        def sub(m):
            i = counter['i']
            counter['i'] += 1
            value = stats[i] if i < len(stats) else m.group(2)
            return m.group(1) + value + m.group(3)

        html = RE_STAT.sub(sub, html)
    return html


def update_index(mf, check: bool = False) -> list:
    path = mf.root / mf.data.get('claims', {}).get('index', 'index.html')
    crlf = b'\r\n' in path.read_bytes()
    current = path.read_text(encoding='utf-8')
    wanted = render_index(mf)

    if current == wanted:
        return [Issue('index', INFO, 'index.html 与 manifest 一致')]
    if check:
        # 指出第一处差异所在版本，便于定位
        lines_a = current.split('\n')
        lines_b = wanted.split('\n')
        at = next((i for i, (x, y) in enumerate(zip(lines_a, lines_b)) if x != y),
                  min(len(lines_a), len(lines_b)))
        return [Issue('index', ERROR,
                      'index.html 与 manifest 不一致（卡片/统计区需重新生成）',
                      file='index.html', line=at + 1,
                      detail='运行 python -m bookkit index 修复')]

    path.write_text(wanted, encoding='utf-8', newline='\r\n' if crlf else '\n')
    return [Issue('index', INFO, 'index.html 已按 manifest 重新生成')]
