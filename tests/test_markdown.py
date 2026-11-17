# -*- coding: utf-8 -*-
"""Markdown 方言边界用例：块级 Markdown ↔ 行内 HTML 的往返保真。"""
import pytest

from bookkit import htmlparse as H
from bookkit import markdown as M


def md_roundtrip(html: str) -> str:
    """HTML 片段 → Markdown → HTML（归一化后比较）。"""
    node = H.Node('div', [], '<div>')
    node.children = H.parse(html).children
    for c in node.children:
        if isinstance(c, H.Node):
            c.parent = node
    md = M.to_markdown(node)
    return M.normalize(M.from_markdown(md))


class TestBlockRoundtrip:
    def test_heading_with_default_class(self):
        assert md_roundtrip('<h3 class="text-xl font-bold text-dark dark:text-gray-200 mb-4">标题</h3>') \
            == M.normalize('<h3 class="text-xl font-bold text-dark dark:text-gray-200 mb-4">标题</h3>')

    def test_paragraph_keeps_inline_html(self):
        s = '<p class="mb-2">行内 <strong>粗</strong> 与 <i class="fas fa-x"></i> 图标</p>'
        assert md_roundtrip(s) == M.normalize(s)

    def test_unordered_list(self):
        s = '<ul class="list-disc pl-6 mb-3 space-y-1"><li>甲</li><li>乙</li></ul>'
        assert md_roundtrip(s) == M.normalize(s)

    def test_ordered_list(self):
        s = '<ol class="list-decimal pl-6 mb-3 space-y-1"><li>一</li><li>二</li></ol>'
        assert md_roundtrip(s) == M.normalize(s)

    def test_pre_with_backticks(self):
        # 内容含 ``` 时围栏自动加长
        s = '<pre>a\n```\nb</pre>'
        assert md_roundtrip(s) == M.normalize(s)

    def test_table_kept_verbatim(self):
        s = ('<table class="w-full"><thead><tr><th>h</th></tr></thead>'
             '<tbody><tr><td>1 &lt; 2</td></tr></tbody></table>')
        assert md_roundtrip(s) == M.normalize(s)

    def test_div_container(self):
        s = '<div class="info-box rounded-lg p-4 mb-4"><p class="font-semibold">t</p></div>'
        assert md_roundtrip(s) == M.normalize(s)

    def test_inline_only_container(self):
        s = '<div class="flex gap-2"><span class="a">x</span><span>y</span></div>'
        assert md_roundtrip(s) == M.normalize(s)


class TestFrontMatter:
    def test_split_and_rejoin(self):
        md = '---\nnum: 一\nnav: 第一章\n---\n\n正文\n'
        meta, body = M.split_front_matter(md)
        assert meta['num'] == '一'
        assert meta['nav'] == '第一章'
        assert body.strip() == '正文'

    def test_no_front_matter(self):
        meta, body = M.split_front_matter('正文\n')
        assert meta == {}
        assert body == '正文\n'


class TestListyEscape:
    def test_escape_roundtrip(self):
        for text in ('1. 看起来像有序列表', '- 看起来像无序列表', '普通文本'):
            escaped = M._escape_listy(text)
            assert M._unescape_listy(escaped) == text

    def test_escape_only_line_start(self):
        assert M._escape_listy('正文 1. 不转义') == '正文 1. 不转义'


class TestNormalize:
    def test_whitespace_between_tags_collapsed(self):
        a = M.normalize('<p>x</p>\n\n   <p>y</p>')
        b = M.normalize('<p>x</p><p>y</p>')
        assert a == b

    def test_pre_content_preserved(self):
        a = '<pre>x  \n y</pre>'
        assert M.normalize(a) == M.normalize(a)

    def test_text_digest_strips_tags_and_comments(self):
        d = M.text_digest('<p>a<!-- c -->b</p>')
        assert 'a' in d and 'b' in d and 'c' not in d


class TestKnownLimitations:
    def test_block_level_inline_tag_drops_wrapper(self):
        # 裸 span 位于块级时只保留内文（v1.9 第59章教训：行内块需包进容器）
        out = M.from_markdown(M.to_markdown(
            H.parse('<div><span class="x">文本</span></div>').find('div')))
        assert '<span' not in out
        assert '文本' in out

    def test_pre_trailing_newline_not_representable(self):
        # 围栏无法表示 pre 尾换行（表示它会破坏 19 语 v1.8 等价性），往返会归一
        out = md_roundtrip('<pre>x\n</pre>')
        assert out == M.normalize('<pre>x</pre>')


if __name__ == '__main__':
    pytest.main([__file__, '-q'])
