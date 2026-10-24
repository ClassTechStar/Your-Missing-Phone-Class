# -*- coding: utf-8 -*-
"""修正脚本：v1.8 空壳重复 h4（正确偏移版）+ 旧版 ch3 末槽 5→6 + v1.5 el 粘连
+ v1.7 ms ch32 杂散 h4 降级 + v1.7 六语言侧栏补第34章锚点。

用法：python scripts/fix_corrective.py [--apply]
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / 'scripts'))
from repair_headings import (H3_RE, H4_RE, SEC_RE, SB_ANCHOR_RE,  # noqa: E402
                             h4_number, bump_number, plain, PROTECT_RE)

APPLY = '--apply' in sys.argv
DUP_SIDS = ['di-wu-shi-san-zhang', 'di-wu-shi-si-zhang', 'di-wu-shi-wu-zhang',
            'di-wu-shi-ba-zhang', 'di-liu-shi-zhang', 'di-liu-shi-jiu-zhang']

def sec_spans(raw):
    ms = list(SEC_RE.finditer(raw))
    return [(m.group(1), m.start(), ms[i + 1].start() if i + 1 < len(ms) else len(raw))
            for i, m in enumerate(ms)]

def load_zh_vals():
    raw = (ROOT / 'v1.8' / 'zh-CN.html').read_text(encoding='utf-8')
    out = {}
    for sid, a, b in sec_spans(raw):
        out[sid] = [h4_number(x) for x in H4_RE.findall(raw[a:b])]
    return out

ZH = load_zh_vals()
import html as hm

def visible(seg: str) -> str:
    t = hm.unescape(re.sub(r'<[^>]+>', ' ', seg))
    return re.sub(r'\s+', ' ', t).strip()

def fix_shells(path: Path, ver: str, lang: str):
    raw = path.read_text(encoding='utf-8')
    edits = []          # (abs_start, abs_end, replacement)
    notes = []
    for sid, a, b in sec_spans(raw):
        if sid not in DUP_SIDS:
            continue
        zh_vals = ZH[sid]
        h4ms = list(H4_RE.finditer(raw, a, b))
        texts = [plain(m.group(1)) for m in h4ms]
        # 文本骨架（去编号/空白）用于识别重复对
        def skeleton(t):
            return re.sub(r'^\s*([0-9]{1,2}\s*[.、）)，,]|[IVX]{1,5}\.|[零〇一二三四五六七八九十]{1,3}[、，,]'
                          r'|[ΑΒΓΔΕΣΤΖΗΘΙΚ]{1,2}\.|\S{1,8}?[,，、.:：]\s*)', '', t).strip().lower()[:24]
        skels = [skeleton(t) for t in texts]
        del_idx = set()
        for k in range(len(h4ms)):
            if k in del_idx:
                continue
            # 空正文 = 该 h4 到下一 h4（或节尾）之间无可见文本
            nxt = h4ms[k + 1].start() if k + 1 < len(h4ms) else b
            body = visible(raw[h4ms[k].end():nxt])
            if body:
                continue
            # 且骨架与相邻某个 h4 相同 → 空壳
            if any(k != j and skels[k] and skels[k] == skels[j]
                   for j in range(len(h4ms))):
                del_idx.add(k)
        if not del_idx:
            # 无空壳：仅校正编号
            keep = list(range(len(h4ms)))
        else:
            keep = [k for k in range(len(h4ms)) if k not in del_idx]
            for k in sorted(del_idx):
                edits.append((h4ms[k].start(), h4ms[k].end(), ''))
                notes.append(f'{sid} 删空壳 h4[{k}]: {texts[k][:34]}')
        # 按zh槽位顺号
        for i, k in enumerate(keep):
            want = zh_vals[i] if i < len(zh_vals) else None
            cur = h4_number(h4ms[k].group(1))
            if want is None or cur is None or cur == want:
                continue
            new_txt = bump_number(h4ms[k].group(1), want)
            if new_txt != h4ms[k].group(1):
                edits.append((h4ms[k].start(1), h4ms[k].end(1), new_txt))
                notes.append(f'{sid} h4[{k}] {cur}→{want}: {texts[k][:30]}')
    if edits:
        edits.sort()
        out, pos = [], 0
        for s0, e0, txt in edits:
            out.append(raw[pos:s0]); out.append(txt); pos = e0
        out.append(raw[pos:])
        if APPLY:
            path.write_text(''.join(out), encoding='utf-8', newline='')
        for n in notes:
            print(f'  [{ver}/{lang}] {n}')
        return len(edits)
    return 0

def fix_ch3_old(path: Path, ver: str, lang: str):
    """v1.5–v1.7 ch3 末槽 val=5 而 zh=6 → bump 6。"""
    raw = path.read_text(encoding='utf-8')
    zh_vals = None
    zh_path = ROOT / ver / 'zh-CN.html'
    zraw = zh_path.read_text(encoding='utf-8')
    for sid, a, b in sec_spans(zraw):
        if sid == 'di-san-zhang':
            zh_vals = [h4_number(x) for x in H4_RE.findall(zraw[a:b])]
    for sid, a, b in sec_spans(raw):
        if sid != 'di-san-zhang':
            continue
        h4ms = list(H4_RE.finditer(raw, a, b))
        n = 0
        for k, m in enumerate(h4ms):
            zv = zh_vals[k] if k < len(zh_vals) else None
            val = h4_number(m.group(1))
            if zv == 6 and val == 5:
                new = bump_number(m.group(1), 6)
                if new != m.group(1) and APPLY:
                    raw = raw[:a + m.start(1)] + new + raw[a + m.end(1):]
                    n += 1
                    print(f'  [{ver}/{lang}] ch3 h4[{k}] 5→6')
        if n and APPLY:
            path.write_text(raw, encoding='utf-8', newline='')
        return n
    return 0

def fix_el_v15():
    p = ROOT / 'v1.5' / 'el.html'
    t = p.read_text(encoding='utf-8')
    t2, n1 = re.subn(r'([α-ωάέήίόύώ]{2,})και(?=[\s,.;;:!?])', r'\1 και', t)
    t2, n2 = re.subn(r'([α-ωάέήίόύώ]{2,})και([α-ωάέήίόύω])', r'\1 και \2', t2)
    if n1 + n2 and APPLY:
        p.write_text(t2, encoding='utf-8', newline='')
    print(f'  v1.5/el και 粘连修复 {n1 + n2}')
    return n1 + n2

def fix_ms_v17_ch32():
    p = ROOT / 'v1.7' / 'ms.html'
    raw = p.read_text(encoding='utf-8')
    for sid, a, b in sec_spans(raw):
        if sid != 'di-san-shi-er-zhang':
            continue
        h4ms = list(H4_RE.finditer(raw, a, b))
        if not h4ms:
            return
        m = h4ms[0]
        t = plain(m.group(1))
        if h4_number(m.group(1)) == 5 and 'Privasi' in t:
            # 上一章遗留块：h4 降级为粗体段
            repl = f'<p class="font-semibold mb-2">{m.group(1)}</p>'
            if APPLY:
                p.write_text(raw[:m.start()] + repl + raw[m.end():], encoding='utf-8', newline='')
            print(f'  v1.7/ms ch32 h4[0] 降级: {t[:40]}')
        return

def fix_v17_sidebar():
    """it/ko/pt/ru/yue/zh-TW 的 v1.7 侧栏补 ch34 锚点（取 v1.8 同语言条目）。"""
    for lang in ['it', 'ko', 'pt', 'ru', 'yue', 'zh-TW']:
        p17 = ROOT / 'v1.7' / f'{lang}.html'
        p18 = ROOT / 'v1.8' / f'{lang}.html'
        if not (p17.exists() and p18.exists()):
            continue
        r17 = p17.read_text(encoding='utf-8')
        if re.search(r'<a href="#di-san-shi-si-zhang" class="toc-item', r17):
            continue
        r18 = p18.read_text(encoding='utf-8')
        m18 = re.search(r'<li[^>]*>\s*<a href="#di-san-shi-si-zhang" class="toc-item.*?</li>', r18, re.S)
        if not m18:
            print(f'  v1.7/{lang}: v1.8 也无 ch34 侧栏条目，跳过')
            continue
        li = m18.group(0)
        # 插到 v1.7 侧栏 di-san-shi-san-zhang 条目之后
        m17 = re.search(r'(<li[^>]*>\s*<a href="#di-san-shi-san-zhang" class="toc-item.*?</li>)', r17, re.S)
        if m17:
            r17 = r17[:m17.end(1)] + '\n                            ' + li + r17[m17.end(1):]
            if APPLY:
                p17.write_text(r17, encoding='utf-8', newline='')
            print(f'  v1.7/{lang}: 侧栏补 ch34 条目')
        else:
            print(f'  v1.7/{lang}: 未找到 ch33 锚点位置')

def main():
    print('== v1.8 空壳/顺号（六章）==')
    n = 0
    for p in sorted((ROOT / 'v1.8').glob('*.html')):
        if p.stem in ('index', 'zh-CN'):
            continue
        n += fix_shells(p, 'v1.8', p.stem)
    print(f'  合计 {n} 处')
    print('== v1.5–v1.7 ch3 末槽 5→6 ==')
    for ver in ['v1.5', 'v1.6', 'v1.7']:
        for p in sorted((ROOT / ver).glob('*.html')):
            if p.stem in ('index', 'lzh') or (ver, p.stem) == ('v1.7', 'lzh'):
                continue
            fix_ch3_old(p, ver, p.stem)
    print('== v1.5 el 粘连 ==')
    fix_el_v15()
    print('== v1.7 ms ch32 ==')
    fix_ms_v17_ch32()
    print('== v1.7 侧栏补 ch34 ==')
    fix_v17_sidebar()
    print('APPLY =', APPLY)

if __name__ == '__main__':
    main()
