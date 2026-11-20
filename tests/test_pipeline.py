# -*- coding: utf-8 -*-
"""增量管线边界用例：tm 分段/哈希、quick 块提取、split 链接改写、extract 页脚剥离。"""
import pytest

from bookkit import quick as Q
from bookkit import split as S
from bookkit import tm as TM


class TestTm:
    def test_seg_hash_stable_and_whitespace_insensitive(self):
        assert TM.seg_hash('a  b\nc') == TM.seg_hash('a b c')

    def test_seg_hash_differs(self):
        assert TM.seg_hash('甲') != TM.seg_hash('乙')

    def test_segments_split_on_blank_lines(self, tmp_path):
        f = tmp_path / 'x.md'
        f.write_text('---\nnav: t\n---\n\n第一段\n\n第二段\n第二行\n\n\n第三段\n',
                     encoding='utf-8')
        segs = TM.segments_of(f)
        assert segs == ['第一段', '第二段\n第二行', '第三段']

    def test_segments_skip_front_matter(self, tmp_path):
        f = tmp_path / 'x.md'
        f.write_text('---\nnav: t\nid: a\n---\n正文\n', encoding='utf-8')
        assert TM.segments_of(f) == ['正文']


class TestQuick:
    def test_quick_block_extraction(self):
        md = ('---\nnav: 第一章\n---\n\n### 第一章\n\n导览\n\n'
              '::: div .quick-read\n##### 本章速读（5 分钟版）\n正文\n'
              '##### 速查表\n- a：b\n:::\n\n#### 一、小节\n')
        m = Q.RE_QUICK.search(md)
        assert m and '速查表' in m.group(1)

    def test_quick_block_missing(self):
        assert Q.RE_QUICK.search('没有任何速读块') is None

    def test_quick_block_matches_only_directive_form(self):
        md = '::: div .quick-read\nx\n:::\n\n::: div .chapter-summary\ny\n:::\n'
        m = Q.RE_QUICK.search(md)
        assert m.group(1).strip() == 'x'


class TestExtractErrataFooter:
    """反解必须剔除 build 注入的勘误页脚——否则重建翻倍，翻译对拍 84 章全失配。"""

    FOOTER_P = ('<p class="text-xs text-gray-500 dark:text-gray-400 mt-6 pt-3 '
                'border-t border-gray-200 dark:border-gray-700">报告错误</p>')

    def _section(self, inner):
        from bookkit import htmlparse as H
        tree = H.parse(f'<div id="x" class="mb-10 content-section">{inner}</div>')
        return H, next(n for n in tree.find_all('div'))

    def test_drop_errata_footer_removes_only_footer(self):
        from bookkit import extract as E
        H, div = self._section(f'<p>正文</p>{self.FOOTER_P}')
        E._drop_errata_footer(div)
        out = ''.join(H.serialize_child(c) for c in div.children)
        assert '报告错误' not in out
        assert '正文' in out

    def test_drop_errata_footer_keeps_normal_paragraphs(self):
        from bookkit import extract as E
        H, div = self._section('<p class="mt-6 pt-3">正文小尾巴</p>')
        E._drop_errata_footer(div)
        out = ''.join(H.serialize_child(c) for c in div.children)
        assert '正文小尾巴' in out

    def test_errata_footer_mark_matches_build(self):
        """build 注入的页脚形状变了，extract 的剥离标记必须跟着变。"""
        from bookkit import build as B
        from bookkit import extract as E
        assert E.ERRATA_FOOTER_MARK in B.errata_footer('en')


class TestSplitRewrite:
    MAP = {'di-a': 'di-a', 'di-b': 'di-b', 'sub-x': 'di-a', 'top': 'index'}

    def test_same_page_anchor_kept(self):
        out = S._rewrite_hrefs('<a href="#sub-x">', self.MAP, 'di-a')
        assert 'href="#sub-x"' in out

    def test_cross_page_anchor_rewritten(self):
        out = S._rewrite_hrefs('<a href="#sub-x">', self.MAP, 'di-b')
        assert 'href="di-a.html#sub-x"' in out

    def test_chapter_link_rewritten(self):
        out = S._rewrite_hrefs('<a href="#di-b">', self.MAP, 'di-a')
        assert 'href="di-b.html"' in out

    def test_top_anchor_always_local(self):
        out = S._rewrite_hrefs('<a href="#top">', self.MAP, 'di-b')
        assert 'href="#top"' in out

    def test_part_anchor_maps_to_first_chapter(self):
        m = {**self.MAP, 'ji-chu-pian': 'di-a'}
        out = S._rewrite_hrefs('<a href="#ji-chu-pian">', m, 'di-b',
                               frozenset({'ji-chu-pian'}))
        assert 'href="di-a.html"' in out

    def test_part_anchor_unmapped_falls_back(self):
        out = S._rewrite_hrefs('<a href="#ji-chu-pian">', self.MAP, 'di-b',
                               frozenset({'ji-chu-pian'}))
        assert 'href="index.html"' in out

    def test_unknown_anchor_goes_index(self):
        out = S._rewrite_hrefs('<a href="#whatever">', self.MAP, 'di-a')
        assert 'href="index.html#whatever"' in out


class TestSplitAssets:
    def test_externalize_moves_big_blocks_only(self):
        assets = {}
        page = ('<style>body{}</style><script>var x=1;</script>'
                + '<script>' + 'a' * 3000 + '</script>')
        out = S._externalize(page, assets)
        assert '<style>' not in out
        assert 'var x=1;' in out           # 小脚本保留内联
        assert 'book.css' in assets and 'book.js' in assets
        assert 'aaa' not in out

    def test_singlefile_lazy_style_stripped_for_chapter_pages(self):
        """单文件专用的整章懒渲染不进分章页（每页只有一章，不需要）。"""
        page = '<style id="singlefile-lazy">lazy{}</style><style>keep{}</style>'
        out = S.RE_SINGLEFILE_STYLE.sub('', page)
        assert 'singlefile-lazy' not in out
        assert 'lazy' not in out
        assert 'keep' in out


if __name__ == '__main__':
    pytest.main([__file__, '-q'])
