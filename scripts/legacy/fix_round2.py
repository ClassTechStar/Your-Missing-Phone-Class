# -*- coding: utf-8 -*-
"""第二轮修复：zh ch56 源稿双"五、" + v1.8 各语言 ch56/ar/he 残余顺号。

用法：python scripts/fix_round2.py [--apply]
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / 'scripts'))
from repair_headings import H4_RE, SEC_RE, h4_number, plain, cjk_num  # noqa: E402

APPLY = '--apply' in sys.argv

AR_DIAC = re.compile(r'[\u064B-\u0652\u0670\u0640]')
ROMAN = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10}
ROMAN_INV = {v: k for k, v in ROMAN.items()}
AR_SHOW = {0: 'صفر', 1: 'أولاً', 2: 'ثانيًا', 3: 'ثالثًا', 4: 'رابعًا', 5: 'خامسًا',
           6: 'سادسًا', 7: 'سابعًا', 8: 'ثامنًا', 9: 'تاسعًا', 10: 'عاشرًا'}
AR_STRIP2SHOW = {AR_DIAC.sub('', v): v for v in AR_SHOW.values()}
HE_LETTERS = 'אבגדהוזחטי'

def bump2(inner: str, target: int):
    """把 h4 inner HTML 的首部编号改为 target（保留原风格）；无法识别返回 None。"""
    t = plain(inner)
    ts = AR_DIAC.sub('', t)
    # 1) 数字 + 分隔
    m = re.match(r'^([0-9]{1,2})\s*([.、）)，,]\s*)', ts)
    if m:
        return inner.replace(t[:m.end(1)], str(target), 1)
    # 2) 罗马数字.
    m = re.match(r'^([IVX]{1,5})\.', ts)
    if m and target in ROMAN_INV:
        return inner.replace(m.group(1), ROMAN_INV[target], 1)
    # 3) 中文数字、
    m = re.match(r'^([零〇一二三四五六七八九十]{1,3})、', ts)
    if m:
        return inner.replace(m.group(1), cjk_num(target), 1)
    # 4) 希伯来字母 + geresh（ה' → ו'）
    m = re.match(r"^([א-ת])\s*['’ʼ]", ts)
    if m and target <= len(HE_LETTERS):
        return inner.replace(m.group(1), HE_LETTERS[target - 1], 1)
    # 5) 韩文汉字/本土数词
    ko = {'일': 1, '이': 2, '삼': 3, '사': 4, '오': 5, '육': 6, '칠': 7, '팔': 8, '구': 9, '십': 10,
          '하나': 1, '둘': 2, '셋': 3, '넷': 4, '다섯': 5, '여섯': 6, '일곱': 7, '여덟': 8, '아홉': 9}
    ko_inv = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구', '십']
    m = re.match(r'^(하나|둘|셋|넷|다섯|여섯|일곱|여덟|아홉|일|이|삼|사|오|육|칠|팔|구|십)\s*[,，、.]\s*', ts)
    if m and ko.get(m.group(1)) is not None:
        return inner.replace(m.group(1), ko_inv[target], 1)
    # 6) 阿拉伯序数（含发音符号形态）
    m = re.match(r'^([\u0621-\u064A][\u064B-\u0652\u0670]{0,2}(?:[\u0621-\u064A][\u064B-\u0652\u0670]{0,2}){0,8})\s*[:：]', t)
    if m and AR_DIAC.sub('', m.group(1)) in AR_STRIP2SHOW:
        return inner.replace(m.group(1), AR_SHOW[target], 1)
    # 7) 德语 Erstens. / 希腊字母. / 马来词表
    order_de = ['Null', 'Erstens', 'Zweitens', 'Drittens', 'Viertens', 'Fünftens', 'Sechstens',
                'Siebtens', 'Achtens', 'Neuntens', 'Zehntens']
    m = re.match(r'^(Erstens|Zweitens|Drittens|Viertens|Fünftens|Sechstens|Siebtens|Achtens|Neuntens)\.', ts)
    if m:
        return inner.replace(m.group(1), order_de[target], 1)
    el = ['Α', 'Β', 'Γ', 'Δ', 'Ε', 'ΣΤ', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ']
    m = re.match(r'^(Α|Β|Γ|Δ|Ε|ΣΤ|Ζ|Η|Θ|Ι|Κ)\.', ts)
    if m and target <= len(el):
        return inner.replace(m.group(1), el[target - 1], 1)
    ms_words = ['Satu', 'Dua', 'Tiga', 'Empat', 'Lima', 'Enam', 'Tujuh', 'Lapan', 'Sembilan', 'Sepuluh']
    m = re.match(r'^(Satu|Dua|Tiga|Empat|Lima|Enam|Tujuh|Lapan|Sembilan|Sepuluh)\s*[,，]', ts)
    if m:
        return inner.replace(m.group(1), ms_words[target - 1], 1)
    return None

def sec_spans(raw):
    ms = list(SEC_RE.finditer(raw))
    return [(m.group(1), m.start(), ms[i + 1].start() if i + 1 < len(ms) else len(raw))
            for i, m in enumerate(ms)]

def renumber_to(path: Path, lang: str, sid_targets: dict):
    raw = path.read_text(encoding='utf-8')
    edits, notes = [], []
    for sid, a, b in sec_spans(raw):
        if sid not in sid_targets:
            continue
        targets = sid_targets[sid]
        h4ms = list(H4_RE.finditer(raw, a, b))
        # 删除：空正文 且 与相邻标题同骨架（前缀归一化）
        def skel(x):
            t = AR_DIAC.sub('', plain(x)).lower()
            t = re.sub(r"^([0-9]{1,2}\s*[.、）)，,]|[ivx]{1,5}\.|[零〇一二三四五六七八九十]{1,3}[、，,]"
                       r"|[α-κστζηθ]['.]?\s*|[\u05d0-\u05ea]['’]\s*|[\u0621-\u064a\u064b-\u0652\u0670]{2,12}[:：]\s*)", '', t)
            return t[:22]
        skels = [skel(m.group(1)) for m in h4ms]
        import html as hm
        del_idx = set()
        for k, m in enumerate(h4ms):
            nxt = h4ms[k + 1].start() if k + 1 < len(h4ms) else b
            body = re.sub(r'\s+', ' ', hm.unescape(re.sub(r'<[^>]+>', ' ', raw[m.end():nxt]))).strip()
            if not body and any(k != j and skels[k] and skels[k] == skels[j] for j in range(len(h4ms))):
                del_idx.add(k)
        keep = [k for k in range(len(h4ms)) if k not in del_idx]
        for k in sorted(del_idx):
            edits.append((h4ms[k].start(), h4ms[k].end(), ''))
            notes.append(f'{sid} 删空壳[{k}] {plain(h4ms[k].group(1))[:30]}')
        for i, k in enumerate(keep):
            want = targets[i] if i < len(targets) else None
            cur = h4_number(h4ms[k].group(1))
            if want is None or cur is None or cur == want:
                continue
            new = bump2(h4ms[k].group(1), want)
            if new:
                edits.append((h4ms[k].start(1), h4ms[k].end(1), new))
                notes.append(f'{sid} [{k}] {cur}→{want} {plain(new)[:30]}')
            else:
                notes.append(f'{sid} [{k}] {cur}→{want} 无法bump: {plain(h4ms[k].group(1))[:34]}')
    if edits:
        edits.sort()
        out, pos = [], 0
        for s0, e0, txt in edits:
            out.append(raw[pos:s0]); out.append(txt); pos = e0
        out.append(raw[pos:])
        if APPLY:
            path.write_text(''.join(out), encoding='utf-8', newline='')
    return notes

def zh_targets(sids):
    raw = (ROOT / 'v1.8' / 'zh-CN.html').read_text(encoding='utf-8')
    out = {}
    for sid, a, b in sec_spans(raw):
        if sid in sids:
            out[sid] = [h4_number(x) for x in H4_RE.findall(raw[a:b])]
    return out

def main():
    # 1) zh 源稿 + 双 html：ch56 第二个"五、"→"六、"
    md = ROOT / 'source/chapters/61-di-wu-shi-liu-zhang.md'
    t = md.read_text(encoding='utf-8')
    old = '#### 五、性能优化与崩溃上报小清单'
    if t.count(old) == 1 and '#### 六、性能优化与崩溃上报小清单' not in t:
        t = t.replace(old, '#### 六、性能优化与崩溃上报小清单', 1)
        if APPLY:
            md.write_text(t, encoding='utf-8', newline='\n')
        print('zh md ch56 五→六')
    for f in ['v1.8/zh-CN.html', '你缺失的那门手机课V1.8Fixed.html']:
        p = ROOT / f
        t = p.read_text(encoding='utf-8')
        oldh = '<h4 class="text-lg font-semibold mt-4 mb-2">五、性能优化与崩溃上报小清单</h4>'
        if t.count(oldh) == 1:
            t = t.replace(oldh, '<h4 class="text-lg font-semibold mt-4 mb-2">六、性能优化与崩溃上报小清单</h4>', 1)
            if APPLY:
                p.write_text(t, encoding='utf-8', newline='')
            print(f'{f} ch56 五→六')
    # 2) 各语言顺号目标（zh 已含 ch56 修正）
    sid_set = {'di-wu-shi-liu-zhang', 'di-wu-shi-san-zhang', 'di-wu-shi-si-zhang',
               'di-wu-shi-wu-zhang', 'di-liu-shi-jiu-zhang'}
    targets = zh_targets(sid_set)
    print('zh targets:', {k: v for k, v in targets.items()})
    for p in sorted((ROOT / 'v1.8').glob('*.html')):
        if p.stem in ('index', 'zh-CN'):
            continue
        notes = renumber_to(p, p.stem, targets)
        for n in notes:
            print(f'  [{p.stem}] {n}')
    print('APPLY =', APPLY)

if __name__ == '__main__':
    main()
