# -*- coding: utf-8 -*-
"""按 REB↔PUB 差异定向收敛 md 的 emoji 状态（仅 24 章，4 语言）。
REB 有而 PUB 无的 emoji → 从 md 删除「emoji+紧随后文」；
PUB 有而 REB 无 → 从 HEAD 版本取「emoji+紧随后文」补回 md。"""
import os
import re
import subprocess
import sys
import unicodedata

sys.path.insert(0, os.getcwd())
from bookkit import htmlparse as H, markdown as M

LANGS = ['ja', 'he', 'id', 'ms']
CID = 'di-er-shi-zhang-termux'
MD = 'source/translations/{L}/chapters/24-di-er-shi-zhang-termux.md'


def sections(html):
    tree = H.parse(html)
    return {n.get('id'): n.inner_raw() for n in tree.find_all('div')
            if 'content-section' in n.classes}


def emoji_ctxs(text):
    """返回 [(emoji, 前文8, 后文8)]。"""
    out = []
    for m in re.finditer(r'[\U0001F300-\U0001FAFF\u2600-\u27BF]\uFE0F?', text):
        e = m.group(0)[0]
        if unicodedata.category(e) == 'So' or ord(e) >= 0x1F300 or 0x2600 <= ord(e) <= 0x27BF:
            out.append((m.group(0), text[max(0, m.start()-10):m.start()], text[m.end():m.end()+10]))
    return out


for L in LANGS:
    path = MD.format(L=L)
    subprocess.run(['git', 'checkout', '--', path], check=True)
    for round_i in range(6):
        r = subprocess.run(['py', '-m', 'bookkit', 'build', '--lang', L,
                            '--out', f'scripts/_v19fix/_reb_{L}.html'],
                           capture_output=True, text=True,
                           encoding='utf-8', errors='replace')
        pub = open(f'v1.8/{L}.html', encoding='utf-8', newline='').read()
        reb = open(f'scripts/_v19fix/_reb_{L}.html', encoding='utf-8', newline='').read()
        A, B = sections(pub), sections(reb)
        pa, pb = M.normalize(A[CID]), M.normalize(B[CID])
        pub_emo = emoji_ctxs(pa)
        reb_emo = emoji_ctxs(pb)
        # 多余：REB 有（按后文匹配）而 PUB 无
        pub_after = {after for _, _, after in pub_emo}
        reb_after = {after for _, _, after in reb_emo}
        extra = reb_after - pub_after
        missing_after = pub_after - reb_after
        if not extra and not missing_after:
            print(L, 'converged round', round_i)
            break
        md = open(path, encoding='utf-8', newline='').read()
        changed = False
        for after in sorted(extra):
            # md 中删「emoji + 空白 + after」——定位 emoji 与 after 相邻处
            for m in re.finditer(r'([\U0001F300-\U0001FAFF\u2600-\u27BF]\uFE0F?)(\s*)', md):
                tail = md[m.end():m.end()+len(after)]
                if tail.startswith(after[:6]):
                    md = md[:m.start()] + md[m.end():]
                    changed = True
                    break
        for after in sorted(missing_after):
            # HEAD 里找 emoji+after，补回 md（md 中搜 after 前插）
            head = subprocess.run(['git', 'show', f'HEAD:{path}'],
                                  capture_output=True, text=True,
                                  encoding='utf-8', errors='replace').stdout
            hm = re.search(r'([\U0001F300-\U0001FAFF\u2600-\u27BF]\uFE0F?\s*' +
                           re.escape(after[:6]) + r')', head)
            if hm:
                ins = hm.group(1)
                # md 中找 after 的位置（取 after 前 6 字）
                k = md.find(after[:6])
                if k != -1 and ins not in md:
                    md = md[:k] + ins + md[k:]
                    changed = True
        if changed:
            open(path, 'w', encoding='utf-8', newline='').write(md)
            print(L, 'round', round_i, 'extra:', len(extra), 'missing:', len(missing_after))
        else:
            print(L, 'no change possible, extra:', extra, 'missing:', missing_after)
            break
