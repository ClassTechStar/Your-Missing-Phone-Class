"""HTML 文本工具：可见文本提取、结构统计、锚点/目录读取、字符集检查。"""

import re

# ---- 结构正则 ----
RE_SECTION = re.compile(r'id="([\w-]+)"\s+class="[^"]*content-section[^"]*"')
RE_ID = re.compile(r'id="([\w-]+)"')
RE_HREF_ANCHOR = re.compile(r'href="#([\w-]+)"')
RE_HTML_LANG = re.compile(r'<html[^>]*\slang="([^"]*)"', re.I)
RE_TITLE = re.compile(r'<title>([\s\S]{0,300}?)</title>', re.I)
RE_STRIP_BLOCK = re.compile(r'<script[\s\S]*?</script>|<style[\s\S]*?</style>|<!--[\s\S]*?-->', re.I)
RE_TAG = re.compile(r'<[^>]+>')
RE_CJK = re.compile(r'[\u3400-\u4dbf\u4e00-\u9fff]')

# 仅繁体目标用：明确的"仅简体"字形（繁体文档中出现即为漏翻）
# 基础集合沿用历史 CI 的黑名单，并补入 ERR-11 暴露的缺失字（与 礼 脑 话 装 学 门）
_SIMP_BASE = (
    '们后发经过还进远运说对车见贝页风飞马鸟龙长东两严丝买亏亚产亲仅从仓仪价会伞伟传伤佣伪侨办务动勋'
    '医华协单卖厅历厉压厌员响哑团园围图国圆冻结净凉减几凤击凭凯刘则刚创删剂剑剧劝势区归当录来现环'
    '确释触点济数献标题储体验证术极构桥联网络应软视频账记扫户计费划亿译书习库问块链汉语变质检测开闭'
    '观场据总线级万档卫报广签处罚监护锁银转扰诈骗举挂补遗嘱侦蓝连热浏览隐权许声动余询换缴罚识号拦骚'
    '属摄个为关内写军农冲况宁层币帮弃担扩毕毙沟浅灭灵烂猎猫画疗疯盖监离种积称笔笋简类紧线练组细终驻'
    '饶驱验驹鲁齐龄双叙叠号吕吗囤嘱悬柜桥桩梦检榄槟欢欧残殿泞炉焕'
)
SIMP_ONLY_HANT = frozenset(_SIMP_BASE + '与礼脑话装学门')

# 日文用：保守集合，排除与日文汉字同形的字（如 礼/与/学 等）
SIMP_VS_JA = frozenset(
    '们这说对边还给电忆记济证释储验术构桥联讯贴页风马鸟龙车见贝门书设络视账软录动发经过运进远输线绝维统圆场备复韩'
)

NON_CJK_SCRIPTS = frozenset({'Latn', 'Cyrl', 'Grek', 'Thai', 'Hang', 'Arab', 'Hebr'})


def visible_text(raw: str) -> str:
    """去掉脚本、样式、注释与标签后的可见文本。"""
    return RE_TAG.sub(' ', RE_STRIP_BLOCK.sub(' ', raw))


def line_of(raw: str, index: int) -> int:
    return raw[:index].count('\n') + 1


def section_ids(raw: str) -> list:
    """按出现顺序返回内容区块 id。"""
    return RE_SECTION.findall(raw)


def all_ids(raw: str) -> set:
    return set(RE_ID.findall(raw))


def href_anchors(raw: str) -> set:
    return set(RE_HREF_ANCHOR.findall(raw))


def toc_anchors(raw: str) -> list:
    """侧边栏目录（#toc-list 到 </nav>）中的锚点序列。"""
    i = raw.find('id="toc-list"')
    if i < 0:
        return []
    j = raw.find('</nav>', i)
    seg = raw[i:j if j > 0 else len(raw)]
    return RE_HREF_ANCHOR.findall(seg)


def html_lang(raw: str) -> str:
    m = RE_HTML_LANG.search(raw)
    return m.group(1) if m else ''


def title(raw: str) -> str:
    m = RE_TITLE.search(raw)
    return re.sub(r'\s+', ' ', m.group(1)).strip() if m else ''


def has_rtl_marker(raw: str, window: int = 400) -> bool:
    return 'dir="rtl"' in raw[:window]


def nul_count(raw_bytes: bytes) -> int:
    return raw_bytes.count(0)


def cjk_chars(text: str) -> list:
    return RE_CJK.findall(text)
