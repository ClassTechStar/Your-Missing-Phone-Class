"""i18n：翻译覆盖率与版本同步状态（堵 ERR-01/07/12 这类"某语言少几章"的漏洞）。"""

from pathlib import Path

from . import textutil as T
from .model import ERROR, WARN, Issue


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
