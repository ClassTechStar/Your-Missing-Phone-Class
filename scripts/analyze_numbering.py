"""扫描各版本 HTML 的章节标题编号样式，输出主流样式与离群项。

用法：python scripts/analyze_numbering.py [v1.8] [--all]
默认只扫 v1.8；--all 扫 v1.5–v1.8 与 archive。
"""
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from bookkit import htmlparse as H  # noqa: E402

# 中文/日文汉字数字、阿拉伯数字（含全角）、韩文数字统一抽象为 #
CJK_NUM = r'[零〇一二三四五六七八九十百两]+'
AR_NUM = r'[0-9０-９]+'

def norm_num(s: str) -> str:
    if re.fullmatch(AR_NUM, s):
        return '#'
    if re.fullmatch(CJK_NUM, s):
        return '#'
    return '#'

def prefix_pattern(title: str):
    """取标题第一段（到第一个冒号/破折号前）并抽象编号 → (pattern, prefix)。"""
    t = re.sub(r'\s+', ' ', title.strip())
    if not t:
        return None, ''
    head = re.split(r'[：:—–]| —— ', t, maxsplit=1)[0].strip()
    # CJK/日文：第 N 章 / 第 N 章付録 / 附録 …
    m = re.match(r'^(第)(%s|%s)(章|回)(.*)$' % (AR_NUM, CJK_NUM), head)
    if m:
        pat = m.group(1) + '#' + m.group(3) + ('*' if m.group(4).strip() else '')
        return pat, head
    m = re.match(r'^(第)(%s|%s)(.*)$' % (AR_NUM, CJK_NUM), head)
    if m and len(m.group(3).strip()) <= 4:   # 第N篇 / 第N部分 等
        pat = m.group(1) + '#' + '*' if m.group(3).strip() else m.group(1) + '#'
        return pat, head
    # 其他语言：前缀词 + 数字
    m = re.match(r'^([^\s\d]+)\s*(%s)(.*)$' % AR_NUM, head)
    if m and len(m.group(1)) <= 20:
        pat = m.group(1) + '#' + ('*' if m.group(3).strip() else '')
        return pat, head
    # 韩文 제N장（汉字数字）
    m = re.match(r'^(제)\s*(%s|%s)\s*(장)(.*)$' % (AR_NUM, r'[영일이삼사오육칠팔구십백]+'), head)
    if m:
        pat = m.group(1) + '#' + m.group(3) + ('*' if m.group(4).strip() else '')
        return pat, head
    return None, head

def section_titles(html: str):
    tree = H.parse(html)
    out = []
    for n in tree.find_all('div'):
        if 'content-section' not in n.classes:
            continue
        h3 = n.find('h3')
        t = re.sub(r'\s+', ' ', h3.text()).strip() if h3 is not None else ''
        out.append((n.get('id'), t))
    return out

def scan(path: Path, verbose=False):
    html = path.read_text(encoding='utf-8')
    secs = section_titles(html)
    pats = Counter()
    rows = []
    for sid, t in secs:
        pat, head = prefix_pattern(t)
        rows.append((sid, t, pat, head))
        pats[pat or '<none>'] += 1
    if not pats:
        return
    modal, _ = pats.most_common(1)[0]
    odd = [(sid, t, pat) for sid, t, pat, _ in rows if pat != modal and pat != '<none>']
    nones = [(sid, t) for sid, t, pat, _ in rows if pat == '<none>']
    tag = f'{path.parent.name}/{path.name}'
    print(f'== {tag}: {len(secs)} 节, 样式分布 {dict(pats.most_common(6))}')
    if verbose or (odd and len(odd) <= 30):
        for sid, t, pat in odd:
            print(f'   [离群 {pat}] {sid}: {t[:70]}')
    if nones:
        print(f'   [无编号 h3: {len(nones)} 个]')
        for sid, t in nones[:6]:
            print(f'      {sid}: {t[:70]}')

def main():
    verbose = '--verbose' in sys.argv
    targets = []
    if '--all' in sys.argv:
        for v in ('v1.5', 'v1.6', 'v1.7', 'v1.8'):
            targets += sorted((ROOT / v).glob('*.html'))
        for p in sorted((ROOT / 'archive').rglob('*.html')):
            targets.append(p)
    else:
        v = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('-') else 'v1.8'
        targets = sorted((ROOT / v).glob('*.html'))
        if len(sys.argv) > 2 and not sys.argv[2].startswith('-'):
            targets = [ROOT / v / f'{sys.argv[2]}.html']
    for p in targets:
        if p.name == 'index.html' or 'index' in p.stem:
            continue
        scan(p, verbose)

if __name__ == '__main__':
    main()
