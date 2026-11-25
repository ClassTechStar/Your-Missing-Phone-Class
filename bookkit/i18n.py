"""i18n：翻译覆盖率与版本同步状态（堵 ERR-01/07/12 这类"某语言少几章"的漏洞）。"""

import re
from pathlib import Path

from . import textutil as T
from .model import ERROR, WARN, Issue

# ---- 译文标点空格缺陷（方案 W2）----
# 机翻流水线曾把 ASCII 逗号/冒号后的空格吞掉（en: "markers,these"），
# 18 个语种累计数百处。这里用"屏蔽保护 + 安全子集"扫描：
# 代码块/行内代码/HTML/URL/模板表达式/链接目标/前置元数据一律不判，
# 只认散文里"字母,字母"与"字母:字母"；数字千分位/时间、商品名
# （Termux:API 这类大写开头）、chown user:group、堆栈里的
# "at ... file:line" 记法都排除，避免改坏代码与专名。
RE_FENCE = re.compile(r'^\s*(?:```|~~~)')
RE_YAML_FRONT = re.compile(r'^---\s*$')
RE_YAML_KEY = re.compile(r'^\s*[\w-]+:\s')
RE_HTML = re.compile(r'<[^>]*>')
RE_INLINE = re.compile(r'`[^`\n]*`')
RE_URL = re.compile(r'(?:https?|ftp)://[^\s)>\]}"]+')
RE_TMPL = re.compile(r'\{[^{}]*\}')
RE_LINK = re.compile(r'\]\([^)]*\)')
RE_SPACING = re.compile(r'(?<=[\w\)\]\u201d\u2019])[,:](?=[^\W\d_])', re.UNICODE)
RE_STACK = re.compile(r'\bat\s+(?:\.\.\.|…)\s+\S*$')

# 只有这几处是"词内被塞了逗号"，加空格反而更错；修复脚本会直接还原成词。
WORD_FIXES = {
    'se,padan': 'sepadan',      # ms：sepadan 被劈开
    'se,dang': 'sedang',        # id：sedang 被劈开
    'เบสแ,บนด์': 'เบสแบนด์',      # th：เบสแบนด์（band）被劈开
}
SKIP_TOKENS = {'user:group'}


def _mask(line: str) -> str:
    """把受保护片段替换成等长空格，保持列号不变。"""
    for rx in (RE_INLINE, RE_URL, RE_HTML, RE_TMPL, RE_LINK):
        line = rx.sub(lambda m: ' ' * len(m.group(0)), line)
    return line


def _token(line: str, start: int, end: int) -> str:
    s, e = start, end
    while s > 0 and (line[s - 1].isalnum() or line[s - 1] in '_-'):
        s -= 1
    while e < len(line) and (line[e].isalnum() or line[e] in '_-'):
        e += 1
    return line[s:e]


def spacing_defects(root: Path, langs=None) -> list:
    """扫描 source/translations 的散文标点缺陷，返回逐处明细。"""
    base = Path(root) / 'source' / 'translations'
    if not base.is_dir():
        return []
    out = []
    targets = [base / l for l in langs] if langs else sorted(
        p for p in base.iterdir() if p.is_dir())
    for lang_dir in targets:
        if not lang_dir.is_dir():
            continue
        for md in sorted(lang_dir.rglob('*.md')):
            in_fence = in_front = False
            for lineno, raw in enumerate(md.read_text(encoding='utf-8').splitlines(), 1):
                if RE_FENCE.match(raw):
                    in_fence = not in_fence
                    continue
                if in_fence:
                    continue
                if not in_front and RE_YAML_FRONT.match(raw):
                    in_front = True
                    continue
                if in_front:
                    if RE_YAML_FRONT.match(raw):
                        in_front = False
                    continue
                if raw.startswith(('    ', '\t')) or raw.lstrip().startswith(':::'):
                    continue
                if RE_YAML_KEY.match(raw):
                    continue
                masked = _mask(raw)
                for m in RE_SPACING.finditer(masked):
                    before, after = masked[m.start() - 1], masked[m.end()]
                    if before.isdigit() and after.isdigit():
                        continue
                    if m.group() == ':' and after.isupper():
                        continue
                    token = _token(masked, m.start(), m.end())
                    if token in SKIP_TOKENS:
                        continue
                    if RE_STACK.search(masked[max(0, m.start() - 32):m.start()]):
                        continue
                    out.append({
                        'lang': lang_dir.name,
                        'file': str(md.relative_to(Path(root))),
                        'line': lineno,
                        'col': m.start() + 1,
                        'punct': m.group(),
                        'token': token,
                        'context': masked[max(0, m.start() - 28):m.end() + 28].strip(),
                    })
    return out


def spacing_issues(root: Path, limit: int = 200) -> list:
    """把标点缺陷转成 Issue（ERROR），用于 CI 门禁。"""
    defects = spacing_defects(root)
    issues = [Issue('i18n-spacing', ERROR,
                    f'{d["lang"]} 译文 ASCII 标点后缺空格：{d["token"]}',
                    file=d['file'], line=d['line'], detail=d['context'])
              for d in defects[:limit]]
    if len(defects) > limit:
        issues.append(Issue('i18n-spacing', ERROR,
                            f'另有 {len(defects) - limit} 处未逐条列出',
                            detail='运行 scripts/fix_i18n_spacing.py 查看全部'))
    return issues


def _read(path: Path) -> str:
    return path.read_text(encoding='utf-8', errors='replace') if path.is_file() else ''


def coverage(mf, version: str) -> dict:
    """返回 {lang: {sections, missing, toc_missing, toc_extra, status}}。"""
    base_code = mf.baseline_lang(version)
    base_path = mf.version_dir(version) / f'{base_code}.html'
    base_raw = _read(base_path)
    base_ids = T.section_ids(base_raw)
    base_toc = T.toc_anchors(base_raw)
    expect = mf.expect_sections(version) or len(base_ids)

    out = {}
    for code, path in mf.html_files(version):
        raw = _read(path)
        ids = T.section_ids(raw)
        toc = T.toc_anchors(raw)
        missing = [i for i in base_ids if i not in set(ids)]
        toc_missing = [a for a in base_toc if a not in set(toc)]
        toc_extra = [a for a in toc if a not in set(base_toc)]
        if code == base_code:
            status = 'baseline'
        elif not missing and not toc_missing:
            status = 'full'
        else:
            status = 'partial'
        out[code] = {
            'sections': len(ids),
            'expected': expect,
            'missing': missing,
            'toc_missing': toc_missing,
            'toc_extra': toc_extra,
            'status': status,
        }
    return out


def sync_status(mf) -> dict:
    """全部版本的覆盖率快照。"""
    result = {}
    for version in mf.versions:
        if mf.html_files(version):
            result[version] = coverage(mf, version)
    return result


def issues(mf, versions=None) -> list:
    """缺章即报 Issue；等级取自 manifest 的 coverage 配置。"""
    issues = []
    versions = versions or [v for v in mf.versions if mf.html_files(v)]
    for version in versions:
        level = mf.check_level(version, 'coverage')
        if level in ('off', None):
            continue
        for code, cov in coverage(mf, version).items():
            if cov['missing']:
                issues.append(Issue(
                    'coverage', level,
                    f'{version}/{code}.html 缺 {len(cov["missing"])} 个章节',
                    file=f'{version}/{code}.html',
                    detail=f'{cov["missing"][:6]}'))
            elif cov['toc_missing']:
                issues.append(Issue(
                    'coverage', WARN,
                    f'{version}/{code}.html 目录缺 {len(cov["toc_missing"])} 个条目',
                    file=f'{version}/{code}.html',
                    detail=f'{cov["toc_missing"][:6]}'))
    return issues


def report(mf, path: Path = None) -> str:
    """生成 Markdown 覆盖率报告，返回文本（可选写盘）。"""
    lines = ['# 翻译覆盖率报告', '',
             f'数据来源：`manifest/languages.json`（最新版本 `{mf.latest_version()}`）；'
             '由 `python -m bookkit i18n` 生成。', '']
    for version in [v for v in mf.versions if mf.html_files(v)]:
        rows = coverage(mf, version)
        total = sum(1 for c in rows.values() if c['status'] in ('full', 'baseline'))
        lines += [f'## {version}', '',
                  f'- 语言数：{len(rows)}；完整对齐（含基准）：{total}；'
                  f'基准：`{mf.baseline_lang(version)}`；期望区块数：{next(iter(rows.values()))["expected"] if rows else 0}',
                  '', '| 语言 | 区块数 | 状态 | 缺章 | 目录缺项 |', '| --- | --- | --- | --- | --- |']
        for code, cov in rows.items():
            missing = '、'.join(cov['missing'][:3]) + ('…' if len(cov['missing']) > 3 else '')
            toc_missing = '、'.join(cov['toc_missing'][:3]) + ('…' if len(cov['toc_missing']) > 3 else '')
            lines.append(f'| `{code}` | {cov["sections"]}/{cov["expected"]} | {cov["status"]} | '
                         f'{missing or "—"} | {toc_missing or "—"} |')
        lines.append('')
    text = '\n'.join(lines) + '\n'
    if path:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        Path(path).write_text(text, encoding='utf-8', newline='\n')
    return text
