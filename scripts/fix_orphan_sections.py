# -*- coding: utf-8 -*-
"""把孤儿章（不在任何篇 <section> 内的 content-section div）移入文档序前一章所在 section。

策略（纯字符串手术，保持字节保真）：
- 深度计数定位每个 content-section div 块与其紧前的章节注释；
- 若外层是被该章独占的包装 div（如 content-col），连同包装一起摘除；
- 插入到目标 section 的 </section> 之前（按文档序逐个追加，保持章序）；
- 文件级校验：div/section 计数不变、章集合不变、孤儿清零。

用法：python scripts/fix_orphan_sections.py [--apply] [版本...]
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from bookkit import htmlparse as H  # noqa: E402

APPLY = '--apply' in sys.argv
VERS = [a for a in sys.argv[1:] if a.startswith('v1.')] or ['v1.5', 'v1.6', 'v1.7', 'v1.8']

DIV_OPEN = re.compile(r'<div\b')
DIV_CLOSE = re.compile(r'</div\s*>')
SEC_OPEN = re.compile(r'<section\b[^>]*\bid="([a-z0-9-]+)"[^>]*>')
SEC_CLOSE = re.compile(r'</section\s*>')
CH_OPEN = re.compile(r'<div[^>]*\bid="([a-z0-9-]+)"[^>]*\bclass="[^"]*content-section[^"]*"[^>]*>')
COMMENT = re.compile(r'<!--.*?-->', re.S)

def match_span(raw: str, open_start: int):
    """从某个开启标签位置出发，深度计数返回闭合后的整体 span (s, e)。"""
    m = re.compile(r'<(div|section)\b[^>]*?(/?)>').match(raw, open_start)
    if not m:
        return None
    if m.group(2) == '/':
        return (open_start, m.end())
    tag = m.group(1)
    depth = 1
    pos = m.end()
    for t in re.finditer(r'<(/?)(' + tag + r')\b[^>]*?(/?)>', raw[pos:]):
        if t.group(1) == '/':
            depth -= 1
        elif t.group(3) != '/':
            depth += 1
        if depth == 0:
            return (open_start, pos + t.end())
    return None

def line_start(raw, i):
    j = raw.rfind('\n', 0, i)
    return j + 1

def surgery(path: Path):
    raw = path.read_text(encoding='utf-8')
    secs = []            # (sid, span)
    for m in SEC_OPEN.finditer(raw):
        sp = match_span(raw, m.start())
        if sp:
            secs.append((m.group(1), sp))
    sec_close_pos = {sid: sp[1] for sid, sp in secs}
    sec_by_pos = sorted(secs, key=lambda x: x[1][0])
    secset = {sid for sid, _ in secs}

    chs = []             # (sid, span)
    for m in CH_OPEN.finditer(raw):
        sp = match_span(raw, m.start())
        if sp:
            chs.append((m.group(1), sp))

    # 判定孤儿：div 的祖先链中无 section（用"该 div 不在任何 section span 内"近似，
    # 因为本书 section 不嵌套 div-in-section 外层）
    def in_section(pos):
        return any(sp[0] <= pos < sp[1] for _, sp in secs)

    orphans = []
    placed = []          # (sid, sec_id or None)
    for sid, sp in chs:
        owner = next((s2 for s2, sp2 in secs if sp2[0] <= sp[0] < sp2[1]), None)
        placed.append((sid, owner))
        if owner is None:
            orphans.append((sid, sp))

    if not orphans:
        return None

    # 目标 section：文档序前一个"已有归属"章的 section（连续孤儿链随前一非孤儿）
    targets = {}
    last_owner = None
    for sid, owner in placed:
        if owner is not None:
            last_owner = owner
        else:
            targets[sid] = last_owner
            if last_owner is None:
                return f'!! {path}: 首章即孤儿，无目标 section：{sid}'

    # 收集编辑：从后往前摘除（保持偏移有效）
    edits = []           # (start, end, block_text)
    for sid, (s, e) in sorted(orphans, key=lambda x: -x[1][0]):
        # 紧前注释（独占行）
        seg_before = raw[:s]
        mcom = None
        for m in COMMENT.finditer(seg_before[max(0, s - 300):s]):
            mcom = m
        block_start = s
        if mcom:
            cs = max(0, s - 300) + mcom.start()
            if not raw[cs:s].strip() == mcom.group(0):
                cs = s
            between = raw[cs:s]
            if re.fullmatch(r'\s*<!--.*?-->\s*', between, re.S):
                block_start = line_start(raw, cs)
        # 包装 div：块前最近的 <div 开启，且开启后到块前仅空白；块后到其闭合仅空白
        wrap = None
        wopen = None
        for m in DIV_OPEN.finditer(raw[max(0, block_start - 400):block_start]):
            wopen = max(0, block_start - 400) + m.start()
        if wopen is not None:
            wsp = match_span(raw, wopen)
            if wsp and wsp[1] >= e:
                pre = raw[wsp[0]:block_start]
                post = raw[e:wsp[1]]
                open_tag_end = raw.find('>', wopen) + 1
                inner_pre = raw[open_tag_end:block_start]
                if re.fullmatch(r'(\s|<!--.*?-->)*', inner_pre, re.S) and \
                   re.fullmatch(r'\s*', post, re.S) and '<div' not in pre[:pre.rfind('<div')]:
                    wrap = wsp
        cut_s = wrap[0] if wrap else block_start
        cut_e = wrap[1] if wrap else e
        inner = raw[block_start:e].rstrip()
        edits.append((cut_s, cut_e, inner, sid))

    # 应用摘除
    out = []
    pos = 0
    removed = sorted(edits, key=lambda x: x[0])
    blocks_by_sid = {sid: inner for _, _, inner, sid in edits}
    order_of_removal = [sid for _, _, _, sid in removed]
    for cs, ce, inner, sid in removed:
        out.append(raw[pos:cs])
        pos = ce
    out.append(raw[pos:])
    new = ''.join(out)

    # 插入：按文档序（原本 placed 顺序）追加到各目标 section 的 </section> 前
    # 目标 section 的 </section> 位置在摘除后重新定位
    insert_plan = []     # (sid, target)
    for sid, owner in placed:
        if owner is None:
            insert_plan.append((sid, targets[sid]))
    # 同一目标的保持原相对顺序（placed 顺序即文档序）
    for sid, tgt in insert_plan:
        m = re.search(r'</section\s*>', new)
        # 定位目标 section：重新扫描
        tsec = None
        for m2 in SEC_OPEN.finditer(new):
            if m2.group(1) == tgt:
                sp = match_span(new, m2.start())
                if sp:
                    tsec = sp
        if tsec is None:
            return f'!! 目标 section 丢失 {tgt}'
        close = new.rfind('</section', tsec[0], tsec[1])
        indent_m = re.compile(r'\n([ \t]*)</section').match(new, close - (len(new) - close) + (close - new.rfind('\n', 0, close)))
        line_begin = new.rfind('\n', 0, close) + 1
        indent = re.match(r'[ \t]*', new[line_begin:close]).group(0)
        block = blocks_by_sid[sid]
        ins = ('\n' + indent + block) if not block.startswith('\n') else (block)
        # 对齐块内缩进（原块可能带原缩进，保持原样即可）
        new = new[:close] + ins + '\n' + indent + new[close:]

    # 校验：div/section/章集合不变
    def stats(s):
        return (len(DIV_OPEN.findall(s)), len(DIV_CLOSE.findall(s)),
                len(SEC_OPEN.findall(s)), sorted(CH_OPEN.findall(s)))
    if stats(raw) != stats(new):
        return (f'!! {path.name}: 结构统计变化 '
                f'{stats(raw)[:3]} -> {stats(new)[:3]}')
    if APPLY:
        path.write_text(new, encoding='utf-8', newline='')
    return f'{path.name}: 移入 {len(edits)} 章 -> {[f"{s}->{t}" for s, t in insert_plan]}'

def main():
    for ver in VERS:
        for p in sorted((ROOT / ver).glob('*.html')):
            if p.stem == 'index' or (ver, p.stem) == ('v1.7', 'lzh'):
                continue
            r = surgery(p)
            if r:
                print(f'[{ver}] {r}')
    print('APPLY =', APPLY)

if __name__ == '__main__':
    main()
