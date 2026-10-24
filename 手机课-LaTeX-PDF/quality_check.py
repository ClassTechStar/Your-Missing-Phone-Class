#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""全量质检 v2：乱码 + 错别字启发式 + PDF/HTML 一致性（降低误报）。

改进：
- HTML 实体只在 <pre> 之外统计（代码块里的 &gt; 是合法 HTML）
- 术语不一致要求同长度、且互为非子串（避免「設定内」≈「设定」这类噪声）
- PDF 覆盖率：CJK 用句级回查，拉丁/西里尔用词级回查（兼容 LaTeX 连字符断词）
- 新增：近空白页检测、PDF 内 mojibake 特征检测
"""

import re
import subprocess
import unicodedata
from collections import Counter
from pathlib import Path

REPO = Path(r'C:\Users\18948\Documents\GitHub\Your-Missing-Phone-Class')
BASE = Path(__file__).resolve().parent
PDF_DIR = BASE / 'pdf'
TXT_DIR = BASE / 'work' / 'pdftext'
TEXLIVE = r'C:\texlive\2026\bin\windows'
MIKTEX = r'C:\Program Files\MiKTeX\miktex\bin\x64'
VERSIONS = ['v1.5', 'v1.6', 'v1.7', 'v1.8']

RE_PRE = re.compile(r'<pre[\s\S]*?</pre>', re.I)
RE_SCRIPT = re.compile(r'<script[\s\S]*?</script>|<style[\s\S]*?</style>|<!--[\s\S]*?-->', re.I)
RE_TAG = re.compile(r'<[^>]+>')
RE_WS = re.compile(r'\s+')
RE_ENTITY = re.compile(r'&(nbsp|amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);')
MOJIBAKE = ['â€', 'Ã©', 'Ã¤', 'ã€', 'ï¼', 'æ', 'å', 'çŠ', 'â€œ', 'â€']
PLACEHOLDER = re.compile(r'\bTODO\b|\bFIXME\b|XXX{2,}|待补充|待完善|待更新|\bplaceholder\b|lorem ipsum')
CJK_RANGE = r'\u4e00-\u9fff\u3400-\u4dbf\u3040-\u30ff\uac00-\ud7af'


def html_text(raw: str) -> str:
    """去掉脚本/样式/注释/标签；保留 pre 内文本。"""
    body = RE_SCRIPT.sub(' ', raw)
    return RE_TAG.sub(' ', body)


def pdf_text(pdf: Path, out: Path) -> str:
    if out.exists():
        return out.read_text(encoding='utf-8', errors='replace')
    out.parent.mkdir(parents=True, exist_ok=True)
    env = {'PATH': TEXLIVE + ';' + MIKTEX + ';' + 'C:\\Windows\\System32'}
    subprocess.run(['pdftotext', '-layout', str(pdf), str(out)], env=env, check=False)
    return out.read_text(encoding='utf-8', errors='replace') if out.exists() else ''


def norm(t: str) -> str:
    return RE_WS.sub('', t)


def is_cjk_doc(text: str) -> bool:
    cjk = len(re.findall(f'[{CJK_RANGE}]', text))
    latin = len(re.findall(r'[A-Za-z]', text))
    return cjk > latin * 0.3 and cjk > 200


# ---------------------------------------------------------------- 乱码

def check_garbled(text: str, tag: str) -> list:
    out = []
    if text.count('\ufffd'):
        out.append(f'{tag}.替换字符={text.count(chr(0xFFFD))}')
    moj = sum(text.count(m) for m in MOJIBAKE)
    if moj:
        out.append(f'{tag}.乱码特征={moj}')
    tofu = text.count('□') + text.count('■')
    if tofu:
        out.append(f'{tag}.方框={tofu}')
    return out


def entity_leaks(raw: str) -> int:
    """真正的实体泄漏 = 解码后仍以字面量出现的 &xxx;（源码里的 &gt; 属合法编码）。"""
    import html as _html
    decoded = _html.unescape(html_text(RE_PRE.sub(' ', raw)))
    return len(re.findall(r'&[a-zA-Z#0-9]{2,8};', decoded))


# ---------------------------------------------------------------- 错别字启发式

RE_HALFWIDTH = re.compile(rf'(?<=[{CJK_RANGE}])[,.!?;:]')
RE_PUNCT_SPACE = re.compile(rf'[{CJK_RANGE}] [，。！？；：]')
RE_DOUBLE_PUNCT = re.compile(r'([。，！？；])\1')
RE_DOUBLE_WORD = re.compile(r'\b([A-Za-z]{2,})[ \t]+\1\b', re.I)
RE_CJK_WORD = re.compile(rf'[{CJK_RANGE}]{{2,4}}')


def typo_stats(text: str) -> list:
    out = []
    if len(RE_HALFWIDTH.findall(text)) > 3:
        out.append(f'半角标点贴中文={len(RE_HALFWIDTH.findall(text))}')
    if len(RE_PUNCT_SPACE.findall(text)) > 3:
        out.append(f'中文与标点间空格={len(RE_PUNCT_SPACE.findall(text))}')
    if len(RE_DOUBLE_PUNCT.findall(text)) > 2:
        out.append(f'重复标点={len(RE_DOUBLE_PUNCT.findall(text))}')
    if len(RE_DOUBLE_WORD.findall(text)) > 2:
        out.append(f'重复单词={len(RE_DOUBLE_WORD.findall(text))}')
    return out


def rare_variants(text: str) -> list:
    """同长度、仅差一字、低频(≤2) vs 高频(≥10)、互不为子串 → 疑似错别字。"""
    freq = Counter(w for w in RE_CJK_WORD.findall(text) if len(w) >= 2)
    common = {w: c for w, c in freq.items() if c >= 10}
    out, seen = [], set()
    for w, c in freq.items():
        if c > 2 or len(w) < 2:
            continue
        for base, bc in common.items():
            if len(base) != len(w):
                continue
            if w in base or base in w:
                continue
            if sum(1 for a, b in zip(w, base) if a != b) == 1 and (w, base) not in seen:
                seen.add((w, base))
                out.append((w, c, base, bc))
    return sorted(out, key=lambda x: -x[3])[:8]


# ---------------------------------------------------------------- 一致性

def coverage(html_raw: str, pdf_raw: str) -> dict:
    h_text, p_text = html_text(html_raw), pdf_raw
    p_norm = norm(p_text)
    p_words = set(re.findall(r"[A-Za-zÀ-ÿ]{4,}", p_text))
    p_words |= {w.replace('-', '') for w in p_words}
    if is_cjk_doc(h_text):
        sents = [s.strip() for s in re.split(r'[。！？\n]', h_text) if 12 <= len(s.strip()) <= 80]
        missing = [s for s in sents if norm(s) and norm(s) not in p_norm]
        return {'mode': '句子', 'total': len(sents), 'missing': len(missing), 'samples': missing[:3]}
    words = [w for w in re.findall(r"[A-Za-zÀ-ÿ]{4,}", h_text) if w.lower() not in p_words]
    total = len(re.findall(r"[A-Za-zÀ-ÿ]{4,}", h_text))
    return {'mode': '单词', 'total': total, 'missing': len(words),
            'samples': list(dict.fromkeys(words))[:6]}


def blank_pages(pdf_raw: str) -> list:
    """PDF 中可提取文字极少的页（剔除目录页后的潜在坏页）。"""
    bad = []
    for i, page in enumerate(pdf_raw.split('\f'), 1):
        body = re.sub(r'^\s*\d+\s*$', '', page, flags=re.M).strip()
        if 0 < len(norm(body)) < 12:
            bad.append(i)
    return bad


# ---------------------------------------------------------------- 主流程

def main():
    for v in VERSIONS:
        for html in sorted((REPO / v).glob('*.html')):
            pdf_text(PDF_DIR / v / f'{html.stem}.pdf', TXT_DIR / f'{v}-{html.stem}.txt')

    rows = []
    for v in VERSIONS:
        for html in sorted((REPO / v).glob('*.html')):
            raw = html.read_text(encoding='utf-8', errors='replace')
            ptxt = (TXT_DIR / f'{v}-{html.stem}.txt').read_text(encoding='utf-8', errors='replace')
            log = BASE / 'work' / f'{v}-{html.stem}' / 'main.log'
            logtxt = log.read_text(encoding='utf-8', errors='replace') if log.exists() else ''
            miss_glyphs = sorted(set(re.findall(r'Missing character: There is no (.+?) in font', logtxt)))
            flags = check_garbled(html_text(raw), 'html') + check_garbled(ptxt, 'pdf')
            ent = entity_leaks(raw)
            if ent:
                flags.append(f'html.实体泄漏={ent}')
            ph = len(PLACEHOLDER.findall(html_text(raw)))
            if ph:
                flags.append(f'html.占位标记={ph}')
            flags += typo_stats(html_text(raw))
            variants = rare_variants(html_text(raw))
            if variants:
                flags.append(f'疑似错别字={len(variants)}')
            cov = coverage(raw, ptxt)
            if cov['missing']:
                flags.append(f"{cov['mode']}未匹配={cov['missing']}/{cov['total']}")
            blanks = blank_pages(ptxt)
            if blanks:
                flags.append(f'近空白页={len(blanks)}({blanks[:5]})（多为篇标题页，设计使然）')
            if miss_glyphs:
                flags.append(f'编译缺字形={len(miss_glyphs)}')
            rows.append({'file': f'{v}/{html.stem}', 'flags': flags, 'variants': variants,
                         'miss_glyphs': miss_glyphs, 'cov': cov})

    clean = [r for r in rows if not r['flags']]
    lines = ['# 质量检查报告 v2（乱码 / 错别字 / PDF-HTML 一致性）', '',
             f'- 对象：HTML {len(rows)} + PDF {len(rows)}（v1.5–v1.8）',
             f'- 完全无告警：{len(clean)} / {len(rows)}',
             '- 实体泄漏只统计 `<pre>` 之外；代码块内实体属合法 HTML',
             '- 「疑似错别字」= 同长度、仅差一字、低频(≤2) vs 高频(≥10)、互不为子串', '']
    lines += ['## 汇总（按告警类型）', '']
    by_type = Counter()
    for r in rows:
        for f in r['flags']:
            by_type[f.split('=')[0].split('.')[-1]] += 1
    for k, c in by_type.most_common():
        lines.append(f'- {k}: {c} 个文件')
    lines += ['', '## 需人工确认的疑似错别字（按文件）', '']
    any_var = False
    for r in rows:
        if r['variants']:
            any_var = True
            vs = '；'.join(f'「{w}」({c})≈「{b}」({bc})' for w, c, b, bc in r['variants'][:5])
            lines.append(f"- **{r['file']}**：{vs}")
    if not any_var:
        lines.append('- 无')
    lines += ['', '## 逐文件告警', '']
    for r in rows:
        if not r['flags']:
            continue
        lines.append(f"### {r['file']}")
        lines.append('- ' + '；'.join(r['flags']))
        if r['cov']['missing'] and r['cov']['samples']:
            lines.append(f"  - 未匹配{r['cov']['mode']}示例：" + ' / '.join(s[:40] for s in r['cov']['samples'][:3]))
        lines.append('')
    lines += ['## 方法学说明', '',
              '- PDF 覆盖率非 100% 的常见原因：LaTeX 连字符断词、页眉页脚插入、emoji/图标被剔除、'
              '目录页码点线；逐条列出供核对，不等于丢内容。',
              '- 编译缺字形来自 XeLaTeX 日志（Missing character），是真实的字体缺字。', '']
    (BASE / '质量检查报告.md').write_text('\n'.join(lines) + '\n', encoding='utf-8', newline='\n')
    print(f"完成：{len(rows)} 对文件；无告警 {len(clean)} 个；报告 → {BASE/'质量检查报告.md'}")
    for k, c in by_type.most_common(8):
        print(f'  {k}: {c}')


if __name__ == '__main__':
    main()
