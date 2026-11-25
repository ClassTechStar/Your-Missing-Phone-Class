# -*- coding: utf-8 -*-
"""W6 补测：split 跨语言/hreflang、tm 增量回环、latex 转义与块渲染、i18n 标点门禁。

这些是"一出静默 bug 就 128 个已发布页面一起错"的核心逻辑；此前只有
markdown/split 链接改写等少量边界用例，这里按方案 W6 把 split/tm/latex
的关键函数补到 3-5 个断言一组。
"""
import json

import pytest

from bookkit import claims as C
from bookkit import htmlparse as H
from bookkit import i18n as I
from bookkit import latex as L
from bookkit import split as S
from bookkit import tm as TM
from bookkit.model import ERROR


# ---------------------------------------------------------------- split

class TestSplitHelpers:
    def test_fix_sw_scope_root(self):
        html = "<script>navigator.serviceWorker.register('sw.js', { scope: './' });</script>"
        assert "register('sw.js', { scope: './' })" in S.fix_sw_scope(html)

    def test_fix_sw_scope_nested(self):
        html = ("<script>navigator.serviceWorker.register('../../sw.js', "
                "{ scope: './' });</script>")
        assert "scope: '../../'" in S.fix_sw_scope(html)

    def test_hreflang_block_needs_two_alternates(self):
        assert S.hreflang_block({'zh-CN': 'https://x/a'}) == ''
        block = S.hreflang_block({'zh-CN': 'https://x/a', 'en': 'https://x/b'},
                                 x_default='https://x/a')
        assert 'hreflang="zh-CN"' in block
        assert 'hreflang="en"' in block
        assert 'hreflang="x-default"' in block
        assert block.count('<link') == 3

    def test_language_index_reads_v19_and_translations(self, tmp_path):
        (tmp_path / 'source' / 'v1.9').mkdir(parents=True)
        (tmp_path / 'source' / 'v1.9' / 'book.json').write_text(json.dumps({
            'version': 'v1.9', 'chapters': [{'id': 'a'}, {'id': 'b'}]}),
            encoding='utf-8')
        en = tmp_path / 'source' / 'translations' / 'en'
        en.mkdir(parents=True)
        (en / 'book.json').write_text(json.dumps({
            'version': 'v1.8', 'chapters': [{'id': 'a'}]}), encoding='utf-8')
        idx = S.language_index(tmp_path)
        assert idx['zh-CN']['version'] == 'v1.9'
        assert idx['zh-CN']['ids'] == {'a', 'b'}
        assert idx['en']['version'] == 'v1.8'
        assert idx['en']['ids'] == {'a'}

    def test_language_index_without_v19_or_translations(self, tmp_path):
        assert S.language_index(tmp_path) == {}

    def test_page_budget_contract(self):
        assert S.PAGE_BUDGET['max_html_kb'] == 300
        assert S.PAGE_BUDGET['max_dom_tags'] == 5000


# ---------------------------------------------------------------- tm

def _make_book(root, version, chapters):
    base = root / 'source' if version == 'v1.8' else root / 'source' / version
    base.mkdir(parents=True, exist_ok=True)
    (base / 'book.json').write_text(json.dumps({
        'version': version,
        'chapters': [{'id': cid, 'file': f'chapters/{cid}.md'} for cid in chapters],
    }, ensure_ascii=False), encoding='utf-8')
    (base / 'chapters').mkdir(exist_ok=True)
    for cid, text in chapters.items():
        (base / 'chapters' / f'{cid}.md').write_text(text, encoding='utf-8')
    return base


class TestTmPipeline:
    def test_build_report_import_roundtrip(self, tmp_path):
        src = _make_book(tmp_path, 'v1.8', {'a': '第一段\n\n第二段\n', 'b': '另一章\n'})
        tr = tmp_path / 'source' / 'translations' / 'en'
        (tr / 'chapters').mkdir(parents=True)
        (tr / 'book.json').write_text(json.dumps({
            'version': 'v1.8',
            'chapters': [{'id': 'a', 'file': 'chapters/a.md'},
                         {'id': 'b', 'file': 'chapters/b.md'}]}), encoding='utf-8')
        (tr / 'chapters' / 'a.md').write_text('Para one\n\nPara two\n', encoding='utf-8')
        (tr / 'chapters' / 'b.md').write_text('Other chapter\n', encoding='utf-8')

        built = TM.build_tm(tmp_path)
        assert built['en']['segments'] == 3
        tm_file = tmp_path / 'manifest' / 'tm' / 'en.json'
        assert tm_file.is_file()
        assert json.loads(tm_file.read_text(encoding='utf-8'))['base_version'] == 'v1.8'

        # 目标版与 TM 同源：100% 命中
        r = TM.report(tmp_path, src / 'book.json', 'en', tmp_path / 'dist' / 'i18n')
        assert r['total'] == 3 and r['todo'] == 0 and r['coverage'] == 100.0

        # 目标版扩写：只导出新增段落
        v19 = _make_book(tmp_path, 'v1.9', {
            'a': '第一段\n\n第二段\n\n新增第三段\n', 'b': '另一章\n'})
        out = tmp_path / 'dist' / 'i18n2'
        r2 = TM.report(tmp_path, v19 / 'book.json', 'en', out)
        assert r2['total'] == 4 and r2['todo'] == 1 and r2['tm_hits'] == 3
        todo = json.loads((out / 'en-todo.json').read_text(encoding='utf-8'))
        assert todo['segments'][0]['source'] == '新增第三段'

        # 回填译文后命中率 100%
        payload = {todo['segments'][0]['hash']: 'New para three'}
        f = tmp_path / 'import.json'
        f.write_text(json.dumps(payload, ensure_ascii=False), encoding='utf-8')
        imported = TM.import_tm(tmp_path, 'en', f)
        assert imported['new'] == 1
        r3 = TM.report(tmp_path, v19 / 'book.json', 'en', out)
        assert r3['todo'] == 0 and r3['coverage'] == 100.0

    def test_build_tm_skips_missing_files(self, tmp_path):
        _make_book(tmp_path, 'v1.8', {'a': '甲\n', 'b': '乙\n'})
        tr = tmp_path / 'source' / 'translations' / 'en'
        (tr / 'chapters').mkdir(parents=True)
        (tr / 'book.json').write_text(json.dumps({
            'version': 'v1.8',
            'chapters': [{'id': 'a', 'file': 'chapters/a.md'},
                         {'id': 'b', 'file': 'chapters/b.md'}]}), encoding='utf-8')
        (tr / 'chapters' / 'a.md').write_text('A\n', encoding='utf-8')
        assert TM.build_tm(tmp_path)['en']['segments'] == 1

    def test_build_tm_conflict_keeps_first(self, tmp_path):
        _make_book(tmp_path, 'v1.8', {'a': '同一段\n\n同一段\n'})
        tr = tmp_path / 'source' / 'translations' / 'en'
        (tr / 'chapters').mkdir(parents=True)
        (tr / 'book.json').write_text(json.dumps({
            'version': 'v1.8', 'chapters': [{'id': 'a', 'file': 'chapters/a.md'}]}),
            encoding='utf-8')
        (tr / 'chapters' / 'a.md').write_text('Same\n\nDifferent\n', encoding='utf-8')
        built = TM.build_tm(tmp_path)
        assert built['en']['conflicts'] == 1
        tm = json.loads((tmp_path / 'manifest' / 'tm' / 'en.json')
                        .read_text(encoding='utf-8'))['segments']
        assert list(tm.values()) == ['Same']


# ---------------------------------------------------------------- latex

class TestLatexEscaping:
    @pytest.mark.parametrize('raw,want', [
        ('100%', r'100\%'),
        ('a&b', r'a\&b'),
        ('snake_case', r'snake\_case'),
        ('#1', r'\#1'),
        ('{x}', r'\{x\}'),
        ('a~b', r'a\textasciitilde{}b'),
        ('a^b', r'a\textasciicircum{}b'),
        ('中文，标点。', '中文，标点。'),
    ])
    def test_esc(self, raw, want):
        assert L.esc(raw) == want

    def test_clean_entities_emoji_and_symbols(self):
        out = L.clean('  A&nbsp;&amp;B 😀 ✓ ① ⌘ μ  ')
        assert r'A \&B' in out
        assert '😀' not in out
        assert '✓' not in out          # emoji 区间内的勾号直接移除
        assert '(1)' in out            # ① → (1)
        assert 'Cmd' in out            # ⌘ → Cmd
        assert r'$\mu$' in out         # μ → $\mu$

    def test_clean_collapses_whitespace(self):
        assert L.clean('a\n\n b\t\tc') == 'a b c'

    def test_pair_quotes_even_and_odd(self):
        assert L.pair_quotes('"a" "b"') == '“a” “b”'
        assert L.pair_quotes('"a') == '“a'

    def test_symbols_map(self):
        assert L.symbols('✓✗➡★') == '√×→*'

    def test_symbols_unknown_passthrough(self):
        assert L.symbols('abc中文') == 'abc中文'


class TestLatexBlocks:
    def _node(self, html):
        return H.parse(html)

    def test_table_header_bold_and_optional_arg_guard(self):
        tree = self._node('<table><tr><th>A</th><th>B</th></tr>'
                          '<tr><td>1</td><td>[x]</td></tr></table>')
        table = next(n for n in tree.find_all('table'))
        out = L._table(table)
        assert r'\begin{tabularx}' in out
        assert r'\textbf{A}' in out
        assert '{}[x]' in out
        assert out.count(r'\tabularnewline') == 2

    def test_table_ragged_rows_padded(self):
        tree = self._node('<table><tr><th>A</th><th>B</th></tr>'
                          '<tr><td>1</td></tr></table>')
        out = L._table(next(n for n in tree.find_all('table')))
        assert '1 & ' in out

    def test_mono_paragraph_br_lines(self):
        tree = self._node('<p class="font-mono">line1<br>line2</p>')
        p = next(n for n in tree.find_all('p'))
        out = L._mono_paragraph(p)
        assert r'\begin{lstlisting}' in out and 'line1\nline2' in out

    def test_code_block_language_detection(self):
        tree = self._node('<div class="code-block"><div class="code-head">'
                          '<span>main.kts</span></div><pre>fun main() {}</pre></div>')
        div = next(n for n in tree.find_all('div'))
        out = L._code_block(div, {'top': r'\booksection'})
        assert r'\begin{lstlisting}[language=Kotlin]' in out
        assert 'fun main() {}' in out

    def test_code_block_without_pre_returns_empty(self):
        tree = self._node('<div class="code-block"><span>x</span></div>')
        assert L._code_block(next(n for n in tree.find_all('div')),
                            {'top': r'\booksection'}) == []

    def test_list_env(self):
        tree = self._node('<ol><li>a</li></ol><ul><li>b</li></ul>')
        envs = [L._list_env(n) for n in tree.find_all()
                if n.tag in ('ol', 'ul')]
        assert envs == ['enumerate', 'itemize']

    def test_heading_levels(self):
        ctx = {'top': r'\booksection'}
        assert L._heading_level(ctx, 'h3') == r'\booksection'
        assert L._heading_level(ctx, 'h4') == r'\booksubsection'
        assert L._heading_level(ctx, 'h5') == r'\subsubsection*'
        ctx2 = {'top': r'\chapter'}
        assert L._heading_level(ctx2, 'h4') == r'\booksection'
        assert L._heading_level(ctx2, 'h5') == r'\booksubsection'


# ---------------------------------------------------------------- i18n spacing

class TestI18nSpacing:
    def _write(self, tmp_path, text):
        p = tmp_path / 'source' / 'translations' / 'en' / 'chapters' / 'x.md'
        p.parent.mkdir(parents=True)
        p.write_text(text, encoding='utf-8')
        return tmp_path

    def test_flags_missing_space_after_comma_and_colon(self, tmp_path):
        root = self._write(tmp_path, 'markers,these and rush:sharpening\n')
        d = I.spacing_defects(root)
        assert len(d) == 2
        assert {x['punct'] for x in d} == {',', ':'}

    @pytest.mark.parametrize('line', [
        'Termux:API plugin',            # 商品名（大写开头）
        'chown user:group',             # 代码参数
        'ratio 16:9 and 1,000 items',   # 数字:数字 / 千分位
        'at ... deineDatei:Zeilennummer',  # 堆栈记法
        '`a,b` and <span class="dark:text">',  # 行内代码/HTML
        'https://example.com/a,b',      # URL
        '```\ncode,here\n```',          # 代码块
        'nav: Kapitel 20',              # 前置元数据
    ])
    def test_protected_forms_not_flagged(self, tmp_path, line):
        root = self._write(tmp_path, line + '\n')
        assert I.spacing_defects(root) == []

    def test_word_fixes_are_flagged_before_fix(self, tmp_path):
        root = self._write(tmp_path, 'kata se,padan dan se,dang\n')
        toks = {d['token'] for d in I.spacing_defects(root)}
        assert 'se,padan' in toks and 'se,dang' in toks

    def test_spacing_issues_are_errors(self, tmp_path):
        root = self._write(tmp_path, 'a,b\n')
        issues = I.spacing_issues(root)
        assert issues and issues[0].severity == ERROR
        assert 'i18n-spacing' == issues[0].check

    def test_no_translations_dir_is_clean(self, tmp_path):
        assert I.spacing_defects(tmp_path) == []


# ---------------------------------------------------------------- claims docs

class TestClaimsDocs:
    """docs/ 口径门禁：旧口径要红，v1.8 历史记述要放行。"""

    def _issues(self, tmp_path, text):
        docs = tmp_path / 'docs'
        docs.mkdir()
        (docs / 'x.md').write_text(text, encoding='utf-8')
        return C._check_docs(tmp_path, None, 'v1.9',
                             {'sections': 120}, '371.7', {'languages': 19})

    def test_flags_v18_as_current(self, tmp_path):
        issues = self._issues(tmp_path, '全书 84 章、18.1 万字。\n')
        assert issues and all(i.severity == ERROR for i in issues)

    def test_allows_historical_v18_mention(self, tmp_path):
        assert self._issues(tmp_path, 'v1.8（84 章）是历史译本。\n') == []

    def test_flags_contradictory_translation_claim(self, tmp_path):
        issues = self._issues(tmp_path, '19 种语言全量翻译，非机器翻译直出。\n')
        assert len(issues) >= 1

    def test_project_brief_consistent_passes(self, tmp_path):
        comp = tmp_path / 'docs' / 'competition'
        comp.mkdir(parents=True)
        (tmp_path / 'source' / 'v1.9').mkdir(parents=True)
        parts = [{'id': f'p{i}', 'chapters': ['c']} for i in range(15)]
        parts.append({'id': 'fu-lu', 'chapters': ['c']})
        (tmp_path / 'source' / 'v1.9' / 'book.json').write_text(json.dumps({
            'version': 'v1.9', 'parts': parts, 'chapters': [{'id': 'c'}]}),
            encoding='utf-8')
        (comp / '项目说明书.md').write_text(
            '——120 章、371.7 万字\n\n全书 **15 篇 · 120 个内容区块 · 371.7 万字**\n',
            encoding='utf-8')
        issues = C._check_docs(tmp_path, None, 'v1.9',
                               {'sections': 120}, '371.7', {'languages': 19})
        assert issues == []
