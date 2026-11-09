# -*- coding: utf-8 -*-
"""全自动收敛：REB↔PUB 逐章 diff 驱动 md emoji 增删，循环至 build --verify PASS。
REB 多的 emoji：裸行则整行删，否则删字符；PUB 多的 emoji：从 HEAD 补回。"""
import os
import re
import subprocess
import sys
import unicodedata

sys.path.insert(0, os.getcwd())
from bookkit import htmlparse as H, markdown as M

NARROW = ['🖥️', '📦', '🔒', '🔧', '📥', '⚙️', '💻', '🎓', '📚',
          '📁', '📝', '🛠️', '🚀', '✨', '🎯', '💡', '🤖', '📊']
EMOJI_RE = re.compile(r'(?:' + '|'.join(re.escape(e) for e in NARROW) + r')')


def sections(html):
    tree = H.parse(html)
    return {n.get('id'): n.inner_raw() for n in tree.find_all('div')
            if 'content-section' in n.classes}


def converge(lang, max_rounds=8):
    path = f'source/translations/{lang}/chapters/24-di-er-shi-zhang-termux.md'
    head = subprocess.run(['git', 'show', f'HEAD:{path}'], capture_output=True,
                          text=True, encoding='utf-8', errors='replace').stdout
    for rnd in range(max_rounds):
        r = subprocess.run(['py', '-m', 'bookkit', 'build', '--lang', lang,
                            '--verify'], capture_output=True, text=True,
                           encoding='utf-8', errors='replace')
        out = r.stdout + r.stderr
        if '结论：PASS' in out:
            print(lang, 'PASS at round', rnd)
            return True
        d = re.search(r'结构差异章节：\[([^\]]*)\]', out)
        if not d or not d.group(1).strip():
            print(lang, 'FAIL but no diff chapter:', out[-200:])
            return False
        cids = [c.strip().strip("'") for c in d.group(1).split(',') if c.strip()]
        pub = open(f'v1.8/{lang}.html', encoding='utf-8', newline='').read()
        r2 = subprocess.run(['py', '-m', 'bookkit', 'build', '--lang', lang,
                             '--out', f'scripts/_v19fix/_reb_{lang}.html'],
                            capture_output=True, text=True,
                            encoding='utf-8', errors='replace')
        reb = open(f'scripts/_v19fix/_reb_{lang}.html', encoding='utf-8', newline='').read()
        A, B = sections(pub), sections(reb)
        md = open(path, encoding='utf-8', newline='').read()
        changed = False
        for cid in cids:
            na, nb = M.normalize(A[cid]), M.normalize(B[cid])
            # diff 在词级别太粗：直接比较 emoji 实例（emoji+后文6）
            def instances(txt):
                s = set()
                for m in EMOJI_RE.finditer(txt):
                    s.add((m.group(0), txt[m.end():m.end()+6]))
                return s
            pi, bi = instances(na), instances(nb)
            # REB 多余实例 → md 删除
            for e, after in sorted(bi - pi):
                # 定位：md 中 emoji 后跟 after（normalize 空格折叠过，md 里空格可能多）
                pat = re.escape(e) + r'[\s]{0,3}' + re.escape(after[:3])
                m = re.search(pat, md)
                if m:
                    line_s = md.rfind('\n', 0, m.start()) + 1
                    line_e = md.find('\n', m.end())
                    line_e = len(md) if line_e == -1 else line_e
                    line = md[line_s:line_e]
                    stripped = EMOJI_RE.sub('', line).strip()
                    # 裸行（去 emoji 后内容在 PUB 中不存在）→ 整行删
                    if stripped and stripped[:6] not in na.replace(' ', ''):
                        md = md[:line_s] + md[line_e+1 if line_e < len(md) else line_e:]
                    else:
                        md = md[:m.start()] + md[m.end():]
                    changed = True
            # PUB 多余实例 → md 补回（从 head 取 emoji+后文）
            for e, after in sorted(pi - bi):
                hm = re.search(re.escape(e) + r'[\s]{0,3}' + re.escape(after[:3]), head)
                if hm and not re.search(re.escape(e) + r'[\s]{0,3}' + re.escape(after[:3]), md):
                    k = md.find(after[:3])
                    if k != -1:
                        md = md[:k] + hm.group(0) + md[k:]
                        changed = True
        if changed:
            open(path, 'w', encoding='utf-8', newline='').write(md)
            print(lang, 'round', rnd, 'changed')
        else:
            print(lang, 'stuck at round', rnd)
            return False
    return False


if __name__ == '__main__':
    for L in sys.argv[1:] or ['ja', 'id']:
        converge(L)
