#!/usr/bin/env python3
"""voice_lint.py — 第一层文本手术（方案 §4）。

把 AI 的三个恶习从字面上拆掉：
  S1 拆三连排比          —— 三连是 AI 的指纹，人最多连两次
  S2 「不是X，而是Y」降频 —— 保留三分之一，其余改直陈
  S3 删段尾总结句 50%     —— AI 每段都收束，人会留着劲儿写下一句
  S4 破折号频率降 70%     —— 破折号是 AI 中文的第一重灾区
  S5 问句配额 ≤2/章       —— 自问自答改成先答后问
  S6 铲平完美平行铺陈      —— 连续等长的列表/段落，改成散文打断
  W-* 黑名单替换           —— S 级删、A 级换口语、B 级只标记不自动改
  T1 章标题模板破除       —— 40% 的章换掉「主标题——副标题」

用法：
  py -3 scripts/voice_lint.py --dry-run                 # 只报告，不改
  py -3 scripts/voice_lint.py --fix --diff state/diff.txt
  py -3 scripts/voice_lint.py --report state/voice_report.json

设计约束（方案 §11.2 / §11.3）：
  * 准确 > 有用 > 诚实披露 > 文学性。口语不完美是手段不是目的。
  * 检测器是听诊器不是法官。规则可关、可调，报告按规则 ID 统计触发量。
  * 所有随机决策用固定 seed，保证可复跑。
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
WL_PATH = HERE / "wordlists.json"

CJK = r"\u4e00-\u9fff\u3000-\u303f\uff00-\uffef"


# =====================================================================
# 保护机制：代码 / HTML 标签 / 链接 / URL 不参与手术
# =====================================================================

PROTECT = [
    re.compile(r"`[^`\n]{0,300}`"),          # 行内代码
    re.compile(r"<[^>\n]{1,400}>"),           # HTML 标签
    re.compile(r"&[a-zA-Z]{1,10};|&#\d{1,7};"),  # HTML 实体（&lt; &gt; &amp; …）
    re.compile(r"\]\([^)\n]{1,400}\)"),       # 链接目标
    re.compile(r"https?://[^\s)\n]{1,400}"),  # 裸 URL
    re.compile(r"\{\{[^}\n]{1,200}\}\}"),     # 模板占位
]


def split_protected(line: str) -> list[tuple[bool, str]]:
    """把一行拆成 [(是否可编辑, 文本), ...]。

    默认整行可编辑；命中保护模式（代码 / HTML 标签 / 链接 / URL）的区间不可编辑。
    """
    marks = [True] * len(line)
    for rx in PROTECT:
        for m in rx.finditer(line):
            for i in range(m.start(), m.end()):
                marks[i] = False
    out: list[tuple[bool, str]] = []
    if not line:
        return out
    start = 0
    cur = marks[0]
    for i in range(1, len(line)):
        if marks[i] != cur:
            out.append((cur, line[start:i]))
            start, cur = i, marks[i]
    out.append((cur, line[start:]))
    return out


def map_editable(line: str, fn):
    """只对可编辑片段应用 fn，返回新行。fn 可返回 None 表示不改。"""
    parts = split_protected(line)
    if not any(ed for ed, _ in parts):
        return line
    buf = []
    for ed, seg in parts:
        if not ed:
            buf.append(seg)
            continue
        new = fn(seg)
        buf.append(seg if new is None else new)
    return "".join(buf)


# =====================================================================
# 行分类：哪些行是"正文散文"，值得动刀
# =====================================================================

class LineKind:
    FRONT = "front"        # YAML frontmatter
    HEADING = "heading"    # # / ## / ####
    TITLE = "title"        # ### 章标题
    FENCE = "fence"        # ``` 围栏行
    CODE = "code"          # 围栏内代码
    DIVMARK = "divmark"    # ::: 围栏标记
    TABLE = "table"        # | 表格行
    HTMLBLOCK = "htmlblock" # 纯 HTML 块行（<table>…）
    LIST = "list"          # - / * / 1. 列表行
    PROSE = "prose"        # 正文散文


def classify_lines(lines: list[str]) -> list[str]:
    kinds: list[str] = []
    in_front = False
    in_code = False
    for i, ln in enumerate(lines):
        s = ln.strip()
        if i == 0 and s == "---":
            in_front = True
            kinds.append(LineKind.FRONT)
            continue
        if in_front:
            kinds.append(LineKind.FRONT)
            if s == "---":
                in_front = False
            continue
        if s.startswith("```"):
            in_code = not in_code
            kinds.append(LineKind.FENCE)
            continue
        if in_code:
            kinds.append(LineKind.CODE)
            continue
        if s.startswith(":::"):
            kinds.append(LineKind.DIVMARK)
            continue
        if s.startswith("#"):
            kinds.append(LineKind.TITLE if s.startswith("### ") else LineKind.HEADING)
            continue
        if s.startswith("|"):
            kinds.append(LineKind.TABLE)
            continue
        if re.match(r"^<[a-zA-Z/!]", s):
            kinds.append(LineKind.HTMLBLOCK)
            continue
        if re.match(r"^([-*+]|\d+\.)\s", s):
            kinds.append(LineKind.LIST)
            continue
        if not s:
            kinds.append(LineKind.PROSE)
            continue
        kinds.append(LineKind.PROSE)
    return kinds


# =====================================================================
# 规则实现
# =====================================================================

class Surgeon:
    def __init__(self, wl: dict, seed: int = 20261119, lang: str = "zh"):
        self.wl = wl
        self.rng = random.Random(seed)
        self.surgery = wl["surgery"]
        self.hits: dict[str, int] = {}
        self.review: list[dict] = []
        self.rules_enabled: set[str] = set()
        self._q_budget = 0
        # 各语言的破折号与标点约定。翻译稿的标点体系不同，不能拿中文规则硬套。
        self.lang = lang
        self.is_chinese = lang in ("zh", "zh-TW", "yue")
        self.is_cjk = lang in ("zh", "zh-TW", "yue", "lzh", "ja")
        if self.is_cjk:
            self.dash_char = "——"
            self.comma, self.colon, self.sentence_end = "，", "：", "。"
            self.semi_terminator = "；"
        else:
            # 西文 / RTL / 泰文：em-dash + 逗号 + 冒号，句读点仍是各自体系
            self.dash_char = "—"
            self.comma, self.colon, self.sentence_end = ",", ":", "."
            self.semi_terminator = None

    def hit(self, rid: str, n: int = 1):
        self.hits[rid] = self.hits.get(rid, 0) + n

    # ---------------- S4 破折号降频 ----------------
    # AI 中文的第一重灾区。替换策略（方案 §4.1 手术 4）：能逗号就逗号，
    # 能冒号就冒号，能另起一句就另起一句——但绝不制造句子残片。
    # 各语言用自己的破折号约定：中文/日文用「——」，西文与 RTL 用「—」。
    def s4_dash(self, seg: str) -> str:
        dash = self.dash_char
        if dash not in seg:
            return seg
        out: list[str] = []
        i = 0
        while True:
            j = seg.find(dash, i)
            if j < 0:
                out.append(seg[i:])
                break
            out.append(seg[i:j])
            left = seg[:j]
            right = seg[j + len(dash):]
            left_has_space = left.endswith(" ")
            right_lead = len(right) - len(right.lstrip(" "))
            before = left.rstrip()
            after = right.lstrip()
            b_last = before[-1] if before else ""
            a_first = after[0] if after else ""

            if b_last in "？！":
                # 问号/叹号后的破折号是"引出答案"，换句号会造出 `？"。` 这种病句
                rep = dash
            elif a_first in "，、；：。！？,;:":
                rep = ""            # 后接标点，破折号纯属冗余，直接去掉
                self.hit("S4")
            elif b_last in "。！？；：.!?;:":
                rep = self.sentence_end
                self.hit("S4")
            else:
                r = self.rng.random()
                if r < 0.62:
                    rep = self.comma
                    self.hit("S4")
                elif r < 0.82:
                    rep = self.colon
                    self.hit("S4")
                else:
                    rep = dash   # 保留一部分，破折号本身不是罪

            if rep != dash:
                # 西文惯例破折号两侧带空格："a — b"。换掉时两侧空格要一起吃掉，
                # 否则会留下 "a ,  b" 这种西文里不存在的写法。
                # 但列表标记后的空格不能吃——"- — xxx" 少了空格就不是列表项了，
                # 列表会被劈成两段（结构校验会报"列表块数增加"）。
                if left_has_space and not re.search(r"(?:^|\s)(?:[-*+]|\d+\.)\s$", out[-1]):
                    out[-1] = out[-1].rstrip(" ")
                if right_lead and not self.is_cjk:
                    rep += " "
                out.append(rep)
                i = j + len(dash) + right_lead
            else:
                out.append(rep)
                i = j + len(dash)
        return "".join(out)

    # ---------------- S2 「不是X，而是Y」降频 ----------------
    # 保留三分之一（确有表达力的），其余改直陈。
    RX_NB = re.compile(
        r"(?P<sub>[^\s。！？；：，、]{0,10}?)不是(?P<a>[^。！？；\n]{2,24}?)"
        r"(?:，(?P<and2>也)?不是(?P<b>[^。！？；\n]{2,24}?))?[，、]而是(?P<y>[^。！？；\n]{2,40})"
    )

    def s2_notbut(self, seg: str) -> str:
        if "不是" not in seg or "而是" not in seg:
            return seg

        def repl(m: re.Match) -> str:
            if self.rng.random() >= self.surgery["not_but_keep_ratio"]:
                self.hit("S2")
                sub = m.group("sub") or ""
                a = m.group("a")
                b = m.group("b")
                y = m.group("y")
                # 有明确主语：拆成两句，主语重复一次
                if sub and 1 <= len(sub) <= 8 and not re.search(r"[的了着过]", sub[-1]):
                    head = sub
                    if b:
                        return f"{head}不是{a}，也不是{b}。{head}是{y}"
                    return f"{head}不是{a}。{head}是{y}"
                # 无主语：只拆后半段，丢掉"而"这个公式信号
                if b:
                    return f"不是{a}，也不是{b}。{y}"
                return f"不是{a}，是{y}"
            return m.group(0)

        return self.RX_NB.sub(repl, seg)

    # ---------------- S1 拆三连排比 ----------------
    # 只认全角「；」：半角分号会出现在 HTML 实体（&lt; &gt;）与代码里。
    RX_SEMI_TRIPLE = re.compile(
        r"(?P<a>[^。！？；\n]{8,}?)；(?!.*；)(?P<b>[^。！？；\n]{8,}?)；(?!.*；)(?P<c>[^。！？；\n]{6,}?)(?P<end>[。！？])"
    )
    RX_ORDERED_TRIPLE = re.compile(
        r"(?P<a>(?:第一|一、)[^。！？；\n]{2,}?)；"
        r"(?P<b>(?:第二|二、)[^。！？；\n]{2,}?)；"
        r"(?P<c>(?:第三|三、)[^。！？；\n]{2,}?)(?P<end>[。！？])"
    )

    def s1_triple(self, seg: str) -> str:
        def repl_ordered(m: re.Match) -> str:
            if self.rng.random() > 0.66:
                return m.group(0)
            self.hit("S1")
            return f"{m.group('a')}；{m.group('b')}。{m.group('c')}{m.group('end')}"

        def repl_semi(m: re.Match) -> str:
            if self.rng.random() > 0.66:
                return m.group(0)
            self.hit("S1")
            return f"{m.group('a')}，{m.group('b')}。{m.group('c')}{m.group('end')}"

        seg = self.RX_ORDERED_TRIPLE.sub(repl_ordered, seg)
        seg = self.RX_SEMI_TRIPLE.sub(repl_semi, seg)
        return seg

    # ---------------- S3 删段尾总结句 ----------------
    # 只动「段落最后一句」收在套话上的情况。词表刻意不含"可见"——它太容易撞上
    # "onStart 可见""屏幕可见"这类正常用法。
    S3_MARKERS = (
        "所以说", "这意味着", "不难发现", "总的来说", "综上所述", "由此可见",
        "因此可以看出", "我们可以看到", "由此我们得出", "换句话说", "也就是说",
        "总之", "简单来说",
    )
    RX_S3_TAIL = re.compile(
        r"(?P<sent>[^。！？\n]{6,120}?(?:" + "|".join(map(re.escape, S3_MARKERS)) + r"))"
        r"[，,]?\s*(?P<end>[。！？])\s*$"
    )

    def s3_closer_line(self, line: str) -> str:
        """段落末尾的套话收束句，按比例删掉。只看最后一句。"""
        if not any(m in line for m in self.S3_MARKERS):
            return line
        stripped = line.rstrip()
        m = self.RX_S3_TAIL.search(stripped)
        if not m:
            return line
        if self.rng.random() >= self.surgery["para_closer_delete_ratio"]:
            return line
        self.hit("S3")
        return stripped[:m.start()]

    # ---------------- S5 问句配额 ----------------
    VERB_OPEN = (
        "遇到", "遇到过", "试过", "用过", "关注过", "关注", "考虑过", "考虑", "想过",
        "担心", "担心过", "安装过", "安装", "购买", "买过", "学习过", "学习", "设置过",
        "设置", "清理过", "清理", "备份过", "备份", "迁移过", "迁移", "找过", "搜过",
        "问过", "加过", "删过", "开过", "关过", "误删", "中过", "踩过", "卡在",
    )

    RX_Q = [
        # 你是否+动词 → 不少人+动词
        (re.compile(r"你是否(?=" + "|".join(VERB_OPEN) + r")([^？?]{2,60})[？?]"), "不少人"),
        # 有没有+动词 → 不少人+动词
        (re.compile(r"有没有(?=" + "|".join(VERB_OPEN) + r")([^？?]{2,60})[？?]"), "不少人"),
        # 有没有+一般动词（兜底，动词性疑问）→ 不少人
        (re.compile(r"有没有(?!什么|没有)([^？?]{2,60})[？?]"), "不少人"),
        # 是不是 → 其实
        (re.compile(r"是不是([^？?]{2,60})[？?]"), "其实"),
        # 你知道/你想知道吗 → 先说一件事
        (re.compile(r"你知道吗[？?]"), "先说一件事。"),
        (re.compile(r"你想知道吗[？?]"), "先说一件事。"),
        (re.compile(r"为什么呢[？?]"), "为什么？"),
    ]

    def s5_questions(self, seg: str) -> str:
        if not re.search(r"(你是否|是不是|有没有|你知道吗|你想知道吗|为什么呢)", seg):
            return seg
        for rx, repl in self.RX_Q:
            def sub(m: re.Match) -> str:
                # 每章最多留 2 个反问句（配额内保留），其余改成陈述
                if self._q_budget > 0:
                    self._q_budget -= 1
                    return m.group(0)
                self.hit("S5")
                if repl.endswith("。"):
                    return repl
                if repl == "其实":
                    return f"其实{m.group(1)}。"
                return f"{repl}{m.group(1)}。"
            seg = rx.sub(sub, seg)
        return seg

    # ---------------- S6 铲平完美平行铺陈 ----------------
    # 实测结论（本仓 120 章）：
    #   · 列表项 19.7% 以「；」结尾——这是机器生成的铁证（全书 13301 个列表项里 2619 个）。
    #     人写的列表项不会一半用分号一半用句号、更不会用分号收尾。
    #   · 真正的「连续≥3 段同结构平行铺陈」只有 33 处，而且都是有意为之
    #     （"标尺一/二/三"、"很多人以为…"、"问：/答："），合并它们只会更糟。
    # 所以 S6 做两件安全的事：统一列表项收尾 + 组内收尾一致；不拆列表、不合段。
    def s6_flatten(self, lines: list[str], kinds: list[str]) -> list[str]:
        i = 0
        out = list(lines)
        n = len(lines)
        while i < n:
            if kinds[i] != LineKind.LIST:
                i += 1
                continue
            j = i
            while j < n and kinds[j] == LineKind.LIST:
                j += 1
            group = list(range(i, j))

            # S6a：列表项以「；」收尾 → 改句号（只在以「；」收尾的语言里有）
            if self.semi_terminator:
                for idx in group:
                    raw = out[idx].rstrip()
                    if raw.endswith(self.semi_terminator):
                        out[idx] = raw[:-1] + self.sentence_end
                        self.hit("S6a")

            # S6b：组内收尾一致（多数派说了算），消灭"一半分号一半句号"
            if len(group) >= 3:
                ends_dot = sum(1 for idx in group if out[idx].rstrip().endswith(self.sentence_end))
                ends_none = sum(1 for idx in group
                                if out[idx].rstrip() and out[idx].rstrip()[-1] not in self.sentence_end + "；：！？.!?")
                if ends_none > ends_dot and ends_none >= 0.6 * len(group):
                    for idx in group:
                        raw = out[idx].rstrip()
                        if raw.endswith(self.sentence_end):
                            out[idx] = raw[:-1]
                            self.hit("S6b")
                elif ends_dot > ends_none and ends_dot >= 0.6 * len(group):
                    for idx in group:
                        raw = out[idx].rstrip()
                        if raw and raw[-1] not in self.sentence_end + "；：！？.!?":
                            out[idx] = raw + self.sentence_end
                            self.hit("S6b")
            i = j
        return out

    # ---------------- S7 段首连接词去重 ----------------
    # AI 特别爱用"此外，…""Moreover, …"开头的句子，连着几句就露馅。
    # 同一段里同一个连接词开头的句子，第二句起把连接词去掉（句子本身完整才去）。
    CONNECTORS = {
        "zh": ("此外", "另外", "而且", "同时", "再者", "其次", "总之"),
        "zh-TW": ("此外", "另外", "而且", "同時", "再者", "其次", "總之"),
        "yue": ("此外", "另外", "而且", "同時", "再者", "其次", "總之"),
        "lzh": ("此外", "又", "且", "亦"),
        "ja": ("また", "さらに", "而且", "さらに", "总计"),
        "latin": ("Moreover", "Furthermore", "Additionally", "In addition", "Also"),
    }

    def s7_connectors(self, lines: list[str]) -> list[str]:
        conns = self.CONNECTORS.get(self.lang, ())
        if not conns:
            return lines
        out = list(lines)
        seen: set[str] = set()
        for i, ln in enumerate(out):
            s = ln.strip()
            for c in conns:
                for sep in ("，", ", "):
                    if s.startswith(c + sep):
                        if c in seen:
                            rest = s[len(c) + len(sep):]
                            # 去掉连接词后句子仍然完整才动手
                            if rest and rest[0].isupper() or rest and re.match(r"^[一-鿿]", rest):
                                out[i] = ln.replace(c + sep, "", 1)
                                self.hit("S7")
                        else:
                            seen.add(c)
                        break
                break
        return out

    # ---------------- W 黑名单 ----------------
    def w_blacklist(self, seg: str) -> str:
        changed = False
        for w in self.wl["s_level"]:
            if w in seg:
                n = seg.count(w)
                seg = seg.replace(w, "")
                self.hit("W-s")
                changed = True
        for w, rep in self.wl["a_level"].items():
            if w in seg:
                n = seg.count(w)
                seg = seg.replace(w, rep)
                self.hit("W-a")
                changed = True
        if changed:
            # 清理手术残留：重复标点与空格
            # （删词后会留下 "组合。值得注意的是，zRAM" → "组合。，zRAM" 这种残渣）
            seg = re.sub(r"。\s*，", "。", seg)
            seg = re.sub(r"，\s*。", "。", seg)
            seg = re.sub(r"，\s*，", "，", seg)
            seg = re.sub(r"。\s*。", "。", seg)
            seg = re.sub(r"[ \t]{2,}", " ", seg)
            seg = re.sub(r"^[，、；：]\s*", "", seg)
        return seg

    # ---------------- 组合 ----------------
    def set_lang(self, code: str) -> None:
        """按语言切换破折号与标点约定。翻译稿的标点体系不同，不能拿中文规则硬套。"""
        self.lang = code
        self.is_chinese = code in ("zh", "zh-TW", "yue")
        self.is_cjk = code in ("zh", "zh-TW", "yue", "lzh", "ja")
        if self.is_cjk:
            self.dash_char = "——"
            self.comma, self.colon, self.sentence_end = "，", "：", "。"
            self.semi_terminator = "；"
        else:
            self.dash_char = "—"
            self.comma, self.colon, self.sentence_end = ",", ":", "."
            self.semi_terminator = None

    def prose_transform(self, seg: str) -> str:
        if "S4" in self.rules_enabled:
            seg = self.s4_dash(seg)
        if "S1" in self.rules_enabled and self.is_chinese:
            seg = self.s1_triple(seg)
        if "S2" in self.rules_enabled and self.is_chinese:
            seg = self.s2_notbut(seg)
        if "W" in self.rules_enabled and self.is_chinese:
            seg = self.w_blacklist(seg)
        return seg


# =====================================================================
# B 级词扫描（只标记，不自动改）
# =====================================================================

def scan_b_level(text: str, wl: dict) -> dict[str, int]:
    hits: dict[str, int] = {}
    for w in wl["b_level"]:
        c = text.count(w)
        if c:
            hits[w] = c
    return hits


# =====================================================================
# 手术后结构校验：手术不能把排版改坏
# =====================================================================

ARTIFACT_PATTERNS = [
    (re.compile(r"[？!！][。．]"), "问号/叹号后接句号"),
    (re.compile(r"[。．][，、]"), "句号后接逗号"),
    (re.compile(r"，\s*，"), "重复逗号"),
    (re.compile(r"：\s*："), "重复冒号"),
    (re.compile(r"（\s*）"), "空全角括号"),
    (re.compile(r"[ \t]{2,}"), "多余空格"),
    (re.compile(r"^\s*[-*+]\s*$"), "空列表项"),
]


def validate(text: str) -> list[tuple[str, str]]:
    """返回结构问题列表 [(标签, 内容), ...]；空列表表示通过。

    不带行号，便于与手术前基线做内容级比对（行号会因手术位移而漂移）。
    """
    problems: list[tuple[str, str]] = []
    for rx, label in ARTIFACT_PATTERNS:
        for m in rx.finditer(text):
            line = text[:m.start()].split("\n")[-1].strip()
            problems.append((label, line[:110]))
    # 标签配平
    for tag in ("strong", "em", "code", "p", "div", "ul", "ol", "li", "table", "tr", "td", "th"):
        o = len(re.findall(rf"<{tag}[\s>]", text))
        c = len(re.findall(rf"</{tag}>", text))
        if o != c:
            problems.append((f"标签 <{tag}> 开合不配平", f"开 {o} / 闭 {c}"))
    return problems


def artifact_counts(text: str) -> dict[str, int]:
    """各条伪影的出现次数，用于与手术前基线做数量级比对。"""
    return {label: len(rx.findall(text)) for rx, label in ARTIFACT_PATTERNS}


def list_runs(text: str) -> int:
    """统计连续列表块的数量。手术不应让这个数字变大。"""
    runs = 0
    inside = False
    for line in text.split("\n"):
        s = line.strip()
        is_list = bool(re.match(r"^(?:[-*+]|\d+\.)\s", s))
        if is_list and not inside:
            runs += 1
        inside = is_list
    return runs


# =====================================================================
# 主流程
# =====================================================================

def process_file(path: Path, wl: dict, surgeon: Surgeon) -> tuple[str, dict]:
    raw = path.read_text(encoding="utf-8")
    nl = raw.endswith("\n")
    lines = raw.split("\n")
    if nl:
        lines = lines[:-1]
    kinds = classify_lines(lines)

    # 每章最多保留 2 个反问句，其余改陈述（方案 §4.1 手术 5）——只在中文体系适用
    if "S5" in surgeon.rules_enabled and surgeon.is_chinese:
        surgeon._q_budget = wl["surgery"]["max_questions_per_chapter"]

    # S6：先做（结构级），再做句级手术
    if "S6" in surgeon.rules_enabled:
        lines = surgeon.s6_flatten(lines, kinds)

    for i, ln in enumerate(lines):
        k = kinds[i]
        if k in (LineKind.FRONT, LineKind.CODE, LineKind.FENCE, LineKind.DIVMARK,
                 LineKind.TABLE, LineKind.HTMLBLOCK):
            continue
        if k == LineKind.TITLE:
            continue        # 标题交给 T1
        if k == LineKind.HEADING:
            continue        # 小节标题不动（目录锚点依赖）
        if k == LineKind.LIST:
            lines[i] = map_editable(ln, lambda s: surgeon.prose_transform(s))
            continue
        lines[i] = map_editable(ln, lambda s: surgeon.prose_transform(s))

    # S3：段尾套话收束句（行级操作，只看段落最后一句）——中文体系专用
    if "S3" in surgeon.rules_enabled and surgeon.is_chinese:
        for i, ln in enumerate(lines):
            k = kinds[i]
            if k in (LineKind.FRONT, LineKind.CODE, LineKind.FENCE, LineKind.DIVMARK,
                     LineKind.TABLE, LineKind.HTMLBLOCK, LineKind.TITLE, LineKind.HEADING):
                continue
            lines[i] = surgeon.s3_closer_line(ln)

    # S5 单独走一遍（需要章级配额）——中文体系专用
    if "S5" in surgeon.rules_enabled and surgeon.is_chinese:
        for i, ln in enumerate(lines):
            k = kinds[i]
            if k in (LineKind.FRONT, LineKind.CODE, LineKind.FENCE, LineKind.DIVMARK,
                     LineKind.TABLE, LineKind.HTMLBLOCK, LineKind.TITLE, LineKind.HEADING):
                continue
            lines[i] = map_editable(ln, lambda s: surgeon.s5_questions(s))

    # S7：段首连接词去重（各语言通用）
    if "S7" in surgeon.rules_enabled:
        lines = surgeon.s7_connectors(lines)

    out = "\n".join(lines) + ("\n" if nl else "")
    # 伪影：只报"新增"（按出现次数比对，手术前的存量问题不算手术的锅）
    before_counts = artifact_counts(raw)
    after_counts = artifact_counts(out)
    problems: list[str] = []
    for label, n_after in after_counts.items():
        n_before = before_counts.get(label, 0)
        if n_after > n_before:
            sample = next((txt for lab, txt in validate(out) if lab == label), "")
            problems.append(f"{label} ×{n_after - n_before}：{sample}")
    # 标签配平
    for tag in ("strong", "em", "code", "p", "div", "ul", "ol", "li", "table", "tr", "td", "th"):
        o = len(re.findall(rf"<{tag}[\s>]", out))
        c = len(re.findall(rf"</{tag}>", out))
        ob = len(re.findall(rf"<{tag}[\s>]", raw))
        cb = len(re.findall(rf"</{tag}>", raw))
        if o != c and not (o - ob == c - cb):
            problems.append(f"标签 <{tag}> 开合不配平：开 {o} / 闭 {c}")
    # 结构级校验：列表块数不得增加（= 列表被劈开）
    if list_runs(out) > list_runs(raw):
        problems.append(f"列表块数增加：{list_runs(raw)} → {list_runs(out)}（列表被劈开）")
    stats = {
        "file": path.name,
        "b_level": scan_b_level(out, wl),
        "changed": out != raw,
        "problems": problems,
    }
    return out, stats


def unified_diff(old: str, new: str, name: str) -> str:
    import difflib
    return "".join(difflib.unified_diff(
        old.splitlines(keepends=True), new.splitlines(keepends=True),
        fromfile=f"a/{name}", tofile=f"b/{name}", n=1))


def main() -> int:
    ap = argparse.ArgumentParser(description="第一层文本手术（方案 §4）")
    ap.add_argument("--chapters", default="source/v1.9/chapters")
    ap.add_argument("--parts", default="source/v1.9/parts")
    ap.add_argument("--fix", action="store_true", help="实际写回（默认只 dry-run）")
    ap.add_argument("--diff", help="diff 输出路径")
    ap.add_argument("--report", help="JSON 报告输出路径")
    ap.add_argument("--rules", default="S1,S2,S3,S4,S5,S6,S7,W",
                    help="启用的规则，逗号分隔")
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--lang", default="zh", help="语言标识：zh / zh-TW / yue / lzh / ja / latin")
    ap.add_argument("--all-translations", action="store_true",
                    help="对 source/translations/*/chapters 全部 18 种语言跑一遍")
    args = ap.parse_args()

    wl = json.loads(WL_PATH.read_text(encoding="utf-8"))
    seed = args.seed if args.seed is not None else wl["surgery"]["seed"]
    surgeon = Surgeon(wl, seed, lang=args.lang)
    surgeon.rules_enabled = {r.strip().upper() for r in args.rules.split(",") if r.strip()}

    # (语言代码, 章节目录, 篇首目录)
    targets: list[tuple[str, Path, Path]] = []
    if args.all_translations:
        for tdir in sorted((ROOT / "source" / "translations").iterdir()):
            if not tdir.is_dir():
                continue
            code = tdir.name
            targets.append((code, tdir / "chapters", tdir / "parts"))
    else:
        targets.append((args.lang, Path(args.chapters), Path(args.parts)))

    diffs: list[str] = []
    stats_all: list[dict] = []
    changed_files = 0

    for code, cdir, pdir in targets:
        surgeon.set_lang(code)
        paths = sorted(cdir.glob("*.md"))
        if pdir.is_dir():
            paths += sorted(pdir.glob("*.md"))
        if not paths:
            print(f"[!] 没找到源稿：{cdir}", file=sys.stderr)
            continue

        for p in paths:
            surgeon.hits = {}
            old = p.read_text(encoding="utf-8")
            new, st = process_file(p, wl, surgeon)
            st["lang"] = code
            st["hits"] = dict(surgeon.hits)
            stats_all.append(st)
            if new != old:
                changed_files += 1
                diffs.append(unified_diff(old, new, str(p)))
                if args.fix:
                    p.write_text(new, encoding="utf-8")
        agg = {}
        for s in stats_all:
            if s["lang"] != code:
                continue
            for k, v in s["hits"].items():
                agg[k] = agg.get(k, 0) + v
        print(f"[i] {code}: {len(paths)} 个文件，规则触发 {agg}")

    if args.diff and diffs:
        dp = Path(args.diff)
        dp.parent.mkdir(parents=True, exist_ok=True)
        dp.write_text("".join(diffs), encoding="utf-8")
        print(f"[+] diff：{dp}（{len(diffs)} 个文件，{sum(d.count(chr(10)) for d in diffs)} 行）")

    if args.report:
        rp = Path(args.report)
        rp.parent.mkdir(parents=True, exist_ok=True)
        agg: dict[str, int] = {}
        for s in stats_all:
            for k, v in s["hits"].items():
                agg[k] = agg.get(k, 0) + v
        rp.write_text(json.dumps({
            "seed": seed,
            "rules": sorted(surgeon.rules_enabled),
            "changed_files": changed_files,
            "rule_hits": agg,
            "per_file": stats_all,
            "review_queue": surgeon.review[:200],
        }, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[+] 报告：{rp}")

    agg: dict[str, int] = {}
    for s in stats_all:
        for k, v in s["hits"].items():
            agg[k] = agg.get(k, 0) + v
    print(f"[i] 规则触发合计：{agg}")
    print(f"[i] 变更文件：{changed_files}" + ("" if args.fix else "（dry-run，未写回）"))

    # 结构校验
    nprob = 0
    prob_files = []
    for s in stats_all:
        if s.get("problems"):
            nprob += len(s["problems"])
            prob_files.append(s["file"])
    if prob_files:
        print(f"[!] 结构校验：{nprob} 个问题，涉及 {len(prob_files)} 个文件")
        for s in stats_all:
            for p in s.get("problems", [])[:6]:
                print(f"    [{s.get('lang','?')}/{s['file']}] {p}")
    else:
        print("[✓] 结构校验通过")

    if surgeon.review:
        print(f"[i] 人工 review 队列：{len(surgeon.review)} 条")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
