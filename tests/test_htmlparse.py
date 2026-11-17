# -*- coding: utf-8 -*-
"""htmlparse 边界用例：字节无损往返是 extract/build 等价性的地基。"""
import pytest

from bookkit import htmlparse as H


def roundtrip(html: str) -> str:
    return H.serialize(H.parse(html))


class TestRoundtrip:
    def test_nested_divs(self):
        s = '<div id="a" class="x y"><div><p>t</p></div></div>'
        assert roundtrip(s) == s

    def test_comment_between_blocks(self):
        s = '<p>1</p>\n<!-- 章节注释 -->\n<p>2</p>'
        assert roundtrip(s) == s

    def test_pre_keeps_angle_brackets(self):
        s = '<pre>if (a &lt; b) {  // &lt;Boolean&gt;\n}</pre>'
        assert roundtrip(s) == s

    def test_pre_raw_text_not_parsed(self):
        # pre 内容按纯文本保留：未转义的裸标签不会变成节点
        tree = H.parse('<pre><div>不是标签</div></pre>')
        pre = tree.find('pre')
        assert pre is not None
        assert pre.inner_raw() == '<div>不是标签</div>'
        assert tree.find('div') is None

    def test_void_and_self_closing(self):
        s = '<p>a<br>b<img src="x.png"><svg><path d="M0 0"/></svg></p>'
        assert roundtrip(s) == s

    def test_attr_quotes_and_gt_in_attr(self):
        s = '<a href="x?a=1&b=2" title="a > b" data-k=\'v\'>t</a>'
        assert roundtrip(s) == s

    def test_doctype_passthrough(self):
        s = '<!DOCTYPE html>\n<html><body><p>x</p></body></html>'
        assert roundtrip(s) == s

    def test_script_content_raw(self):
        s = '<script>if (1 < 2) { document.write("<div>x</div>"); }</script>'
        assert roundtrip(s) == s

    def test_listy_text_without_tags(self):
        # 纯文本里的 < 后跟非字母：整体当文本保留
        s = '<p>把 <<<<<<<、=======、>>>>>>> 删干净</p>'
        assert roundtrip(s) == s


class TestTreeApi:
    def test_find_all_and_classes(self):
        tree = H.parse('<div class="a b"><div class="c"></div></div>')
        assert len(tree.find_all('div')) == 2
        inner = tree.find('div', cls='c')
        assert inner is not None
        assert inner.classes == ['c']

    def test_get_attr(self):
        n = H.parse('<span id="x" data-v="1"></span>').find('span')
        assert n.get('id') == 'x'
        assert n.get('data-v') == '1'
        assert n.get('missing', 'd') == 'd'

    def test_text_of(self):
        tree = H.parse('<p>a<!-- c -->b<strong>c</strong></p>')
        assert H.text_of(tree.find('p')) == 'abc'

    def test_index_nodes_spans(self):
        raw = '<div id="a"><p>12</p></div>'
        tree = H.parse(raw)
        pos = H.index_nodes(tree)
        div = tree.find('div')
        start, end = pos[id(div)]
        assert raw[start:end] == raw


class TestErrorTolerance:
    def test_optional_p_close_is_force_closed(self):
        # <p> 缺 </p>：浏览器自动闭合，解析器在块级闭标签处代闭合，
        # 序列化会补出合成的 </p>（见 scripts/fix_v19_normalize.py 附录B 案例）
        s = '<div><p>文本\n<div class="x">t</div></div>'
        tree = H.parse(s)
        assert H.serialize(tree) != s
        assert len(tree.find_all('div')) == 2

    def test_stray_close_dropped(self):
        # 无匹配开标签的游离闭标签被丢弃（序列化不还原）——既定行为
        s = '<div>a</span></div>'
        assert H.serialize(H.parse(s)) == '<div>a</div>'


if __name__ == '__main__':
    pytest.main([__file__, '-q'])
