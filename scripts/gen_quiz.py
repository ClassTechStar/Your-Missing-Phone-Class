#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从源稿生成章节自测题库（quiz/<lang>.json）。

思路：题目全部锚定书中真实内容，不手写、不编造。
每章从三类素材出题：
  1. 加粗术语定义  `<strong>CPU大小核设计</strong>：现代手机CPU…`
     → 真实定义句，用于「术语 → 定义」与「定义 → 术语」两型
  2. 定义型标题    `##### SoC：手机的"大脑+心脏"`
     → 副标题是精炼比喻，用于「哪项被这样形容」一型
  3. 章导读首句    → 凑不满每章题量时补一章主题题

用法：
    python scripts/gen_quiz.py                 # 生成 quiz/zh-CN.json
    python scripts/gen_quiz.py --lang en       # 生成 quiz/en.json
    python scripts/gen_quiz.py --per-chapter 3 --out quiz/zh-CN.json
"""

import argparse
import json
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'source'
TRANS = ROOT / 'source' / 'translations'
sys.path.insert(0, str(ROOT))
from bookkit import content as C  # noqa: E402  （P1-1：数据访问统一走门面）

# ---------------------------------------------------------------- 素材提取

RE_H5 = re.compile(r'^#####\s+(.+)$', re.M)
RE_STRONG_DEF = re.compile(r'<strong>([^<>{}\n]{2,24})</strong>：([^<\n]{12,})')
RE_INTRO = re.compile(r'\{class="chapter-intro[^}]*"\}\s*\n(.+)')
RE_NUM_PREFIX = re.compile(r'^\d+[.、)]\s*')
# HTML 表格：抽「行首列 → 某列」的事实型题目（AI 编程篇大量用表格讲概念）
RE_TABLE = re.compile(r'<table[^>]*>(.*?)</table>', re.S)
RE_TR = re.compile(r'<tr[^>]*>(.*?)</tr>', re.S)
RE_CELL = re.compile(r'<t[dh][^>]*>(.*?)</t[dh]>', re.S)
# 题库要排除的「术语」：模板占位符、Markdown 元描述、带句读的句子
RE_BAD_TERM = re.compile(r'[\[\]{}（）()，。；、！？!?;,]|^[<>]')
META_TERMS = {'加粗', '斜体', '高亮', '提示', '注意', '警告', '重点', '小贴士',
              '本章导读', '阅读路线', '动手练习', '小结', '总结', '引用', '链接'}
# 纯品牌/厂商名太泛，问「苹果指的是什么」没有意义
GENERIC_TERMS = {'苹果', '华为', '小米', '三星', '谷歌', '微软', '荣耀', '联想',
                 '安卓', '苹果手机', '国产', '厂商', '用户', '手机', '系统', '设置',
                 '数据', '应用', '软件', '硬件', '网络', '电池', '屏幕'}
# 这些词出现在「定义」里，说明它其实是产品事实/清单，不是定义
FACT_MARKERS = ('系列', '开始支持', '发布', '上市', '推出', '官网', '下载地址',
                '价格为', '售价', '元/月', '/月')
# UI 路径（[设置] > [隐私]）不是定义
RE_UI_PATH = re.compile(r'[\[>]')


def _clean(s: str) -> str:
    s = re.sub(r'<[^>]+>', '', s)
    s = (s.replace('&nbsp;', ' ').replace('&amp;', '&')
          .replace('&lt;', '<').replace('&gt;', '>'))
    return re.sub(r'\s+', ' ', s).strip(' ：:，,。；;')


def _first_clause(text: str, lo=12, hi=76) -> str:
    """取定义首句；不在括号/引号内部截断，超长才按逗号截。"""
    t = _clean(text)
    if not t:
        return ''
    depth = 0
    out = t
    for i, ch in enumerate(t):
        if ch in '（(【[':
            depth += 1
        elif ch in '）)】]':
            depth = max(0, depth - 1)
        elif depth == 0 and ch in '。；;':
            out = t[:i]
            break
        elif depth == 0 and ch in '，,' and i >= lo:
            out = t[:i]
            break
    out = out.strip(' ，,。；;：:')
    if len(out) < lo:
        return ''
    if len(out) > hi:
        out = out[:hi - 1].rstrip('，,、 ') + '…'
    return out


def _term_ok(term: str, md: str = '') -> bool:
    """术语是否够格出题。

    关键甄别是词频：真术语（SoC / CPU / 护眼模式）在正文里会反复出现；
    修辞式标题（「系统自己占了地方」）只在标题里出现一次。
    """
    if not (2 <= len(term) <= 14):
        return False
    if RE_BAD_TERM.search(term):
        return False
    if term in META_TERMS or any(m in term for m in META_TERMS):
        return False
    if term.endswith(('的', '了', '是')):
        return False
    if md and md.count(term) < 2:
        return False
    return True


def _def_ok(term: str, defn: str, md: str = '') -> bool:
    """这段「定义」能不能用来出题。

    `<strong>X</strong>：Y` 的 Y 既可能是定义（「CPU：负责处理绝大多数计算任务」），
    也可能是产品事实（「苹果：iPhone 14 系列及以后」）或 UI 路径
    （「小米：[设置] > [隐私保护]」）。后者拿来出题会问出「苹果是什么」这种怪题。
    """
    if term in GENERIC_TERMS:
        return False
    if any(k in defn for k in FACT_MARKERS):
        return False
    if RE_UI_PATH.search(defn):
        return False
    return True


def pairs_strong(md: str):
    """`<strong>术语</strong>：定义` → [(术语, 定义句)]，真实定义。"""
    out, seen = [], set()
    for m in RE_STRONG_DEF.finditer(md):
        term = _clean(m.group(1))
        d = _first_clause(m.group(2))
        if (_term_ok(term, md) and d and term not in seen
                and _def_ok(term, d, md)):
            seen.add(term)
            out.append((term, d))
    return out


def pairs_heading(md: str):
    """`##### 术语：副标题` → [(术语, 副标题)]，副标题是精炼比喻。"""
    out, seen = [], set()
    for m in RE_H5.finditer(md):
        head = _clean(m.group(1))
        if '：' not in head and ':' not in head:
            continue
        term, sub = re.split(r'[：:]', head, maxsplit=1)
        term = _clean(RE_NUM_PREFIX.sub('', term))
        sub = _clean(sub)
        if _term_ok(term, md) and len(sub) >= 6 and term not in seen:
            seen.add(term)
            out.append((term, sub))
    return out


def intro_of(md: str) -> str:
    """章导读首句；首句过短则续接下一句，保证能当选项。"""
    m = RE_INTRO.search(md)
    if not m:
        return ''
    t = _clean(m.group(1))
    if not t:
        return ''
    first = _first_clause(t, 14, 90)
    if first:
        return first
    # 首句太短：取前两句
    parts = re.split(r'(?<=[。！？])', t)
    joined = ''
    for p in parts:
        joined += p
        if len(joined) >= 16:
            break
    joined = joined.strip(' ，,。；;：:')
    if not (14 <= len(joined) <= 90):
        return ''
    return joined


def table_facts(md: str):
    """从 HTML 表格抽 (行首列, 表头列名, 该行该列的值)。

    只取「首列是短标签、目标列是短值」的行，避免把长段落当选项。
    """
    out = []
    for tm in RE_TABLE.finditer(md):
        rows = []
        for trm in RE_TR.finditer(tm.group(1)):
            cells = [_clean(c) for c in RE_CELL.findall(trm.group(1))]
            cells = [c for c in cells if c]
            if len(cells) >= 2:
                rows.append(cells)
        if len(rows) < 3:                 # 至少 3 行才凑得出干扰项
            continue
        head, body = rows[0], rows[1:]
        for r in body:
            if len(r) < 2 or not (2 <= len(r[0]) <= 16):
                continue
            for ci in range(1, min(len(head), len(r))):
                val = r[ci]
                if not (8 <= len(val) <= 40) or len(head[ci]) > 8:
                    continue
                out.append((r[0], head[ci], val, [x[ci] for x in body if x is not r and ci < len(x)]))
    return out


def load_chapters(lang: str):
    """返回 [(id, nav, md), ...]，按 book.json 顺序（P1-1：走 bookkit.content 门面）。"""
    out = []
    for m in C.chapters(lang):
        p = ROOT / m['file']
        if not p.is_file():
            continue
        md = p.read_text(encoding='utf-8')
        out.append((m['id'], m['title'], md))
    return out


# ---------------------------------------------------------------- 出题

def _mk_options(rng, correct, distractors):
    """组四个选项并打乱，返回 (options, answer_index)；不足四项返回 (None, -1)。"""
    uniq = [correct]
    for d in distractors:
        if d != correct and d not in uniq:
            uniq.append(d)
    opts = uniq[:4]
    if len(opts) < 4:
        return None, -1
    rng.shuffle(opts)
    return opts, opts.index(correct)


def _fill(rng, need, pool, exclude):
    """从 pool 里补足干扰项（去重、打乱后取前 need 个）。"""
    out = []
    cands = [x for x in pool if x not in exclude]
    rng.shuffle(cands)
    for x in cands:
        if len(out) >= need:
            break
        if x in out:
            continue
        out.append(x)
    return out


def _table_question(row: str, col: str) -> str:
    """表格题题干。列名本身已是疑问（「管什么」「谁来管」）时不再套「是什么」。"""
    if col.endswith(('什么', '啥', '吗', '哪', '谁', '怎么', '如何', '多少')):
        return f'「{row}」{col}？'
    return f'「{row}」的{col}是什么？'


def build(lang: str, per_chapter: int = 3):
    chapters = load_chapters(lang)
    strong_all, head_all, intro_all = {}, {}, {}
    for cid, nav, md in chapters:
        for t, d in pairs_strong(md):
            strong_all.setdefault(t, d)
        for t, d in pairs_heading(md):
            head_all.setdefault(t, d)
        if intro_of(md):
            intro_all[cid] = intro_of(md)

    # 跨章频次：出现在太多章里的词（「安卓」「苹果」「手机」）太泛，
    # 拿它出题等于问「苹果是什么」，一律剔除。
    spread = {}
    for cid, nav, md in chapters:
        for t in set(list(dict(pairs_strong(md))) + list(dict(pairs_heading(md)))):
            spread[t] = spread.get(t, 0) + 1
    GENERIC_MAX = 5

    def specific(t):
        return spread.get(t, 0) <= GENERIC_MAX

    out_chapters = []
    for cid, nav, md in chapters:
        rng = random.Random(f'{lang}:{cid}')
        sp, hp = pairs_strong(md), pairs_heading(md)
        qs = []

        # ---- A 型：术语 → 真实定义 ----
        for term, defn in sp:
            if len(qs) >= per_chapter:
                break
            if not specific(term):
                continue
            others = _fill(rng, 3, [d for t, d in sp if t != term and specific(t)], [defn])
            if len(others) < 3:
                others += _fill(rng, 3 - len(others),
                                [d for t, d in strong_all.items() if t != term],
                                others + [defn])
            opts, ans = _mk_options(rng, defn, others)
            if opts:
                qs.append({'q': f'「{term}」在书中指的是什么？',
                           'options': opts, 'answer': ans,
                           'explain': f'见「{nav}」：{defn}'})

        # ---- B 型：定义/比喻 → 术语 ----
        for term, clue in hp + sp:
            if len(qs) >= per_chapter:
                break
            if len(clue) < 16 or not specific(term):
                continue
            others = _fill(rng, 3, [t for t, d in hp + sp if t != term and specific(t)], [term])
            if len(others) < 3:
                pool = [t for t in list(head_all) + list(strong_all) if t != term]
                others += _fill(rng, 3 - len(others), pool, others + [term])
            opts, ans = _mk_options(rng, term, others)
            if opts:
                qs.append({'q': f'哪一项对应这个描述：「{clue}」',
                           'options': opts, 'answer': ans,
                           'explain': f'见「{nav}」：{term}'})

        # ---- C 型：章主题（导读首句）----
        if len(qs) < per_chapter and intro_all.get(cid):
            intro = intro_all[cid]
            others = _fill(rng, 3, [i for k, i in intro_all.items() if k != cid], [intro])
            opts, ans = _mk_options(rng, intro, others)
            if opts:
                qs.append({'q': f'下面哪一段是「{nav}」的开场导读？',
                           'options': opts, 'answer': ans,
                           'explain': f'回到「{nav}」开头看看。'})

        # ---- D 型：表格事实题 ----
        for row, col, val, siblings in table_facts(md):
            if len(qs) >= per_chapter:
                break
            others = _fill(rng, 3, siblings, [val])
            opts, ans = _mk_options(rng, val, others)
            if opts:
                qs.append({'q': _table_question(row, col),
                           'options': opts, 'answer': ans,
                           'explain': f'见「{nav}」的表格：{row} · {col} = {val}'})

        if qs:
            out_chapters.append({'id': cid, 'title': nav, 'questions': qs[:per_chapter]})

    nq = sum(len(c['questions']) for c in out_chapters)
    return {'schemaVersion': 1,
            'lang': lang,
            'note': '《你缺失的那门手机课》章节自测 · 由 scripts/gen_quiz.py 从源稿'
                    '自动生成，题目锚定书中真实内容（术语定义、标题比喻、章导读）。',
            'chapters': out_chapters}, nq


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lang', default='zh-CN')
    ap.add_argument('--per-chapter', type=int, default=3)
    ap.add_argument('--out', type=Path, default=None)
    args = ap.parse_args()
    out = args.out or (ROOT / 'quiz' / f'{args.lang}.json')
    data, nq = build(args.lang, args.per_chapter)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n',
                   encoding='utf-8', newline='\n')
    rel = out.relative_to(ROOT) if out.is_relative_to(ROOT) else out
    print(f'{rel}: {len(data["chapters"])} 章，{nq} 题')
    # 自检：选项数、答案索引、选项不重复、题干非空
    bad = []
    for c in data['chapters']:
        for q in c['questions']:
            if len(q['options']) != 4 or not (0 <= q['answer'] < 4):
                bad.append((c['id'], '选项/答案异常'))
            elif len(set(q['options'])) != len(q['options']):
                bad.append((c['id'], '选项重复'))
            elif not q['q'].strip() or not q['explain'].strip():
                bad.append((c['id'], '题干/解析为空'))
    if bad:
        print('!! 自检未过：', bad[:5])
        sys.exit(1)
    print('自检通过：每题 4 个不重复选项，答案索引有效')


if __name__ == '__main__':
    main()
