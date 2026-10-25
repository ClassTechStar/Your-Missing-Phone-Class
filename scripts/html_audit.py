# -*- coding: utf-8 -*-
"""HTML 全量质量审计：顺序 / 编号 / 排版产物 / 可读性。

用法：python scripts/html_audit.py [版本...]   # 默认 v1.5–v1.8
检查项：
  A 顺序：正文章节顺序 == 同版本 zh-CN；侧栏锚点顺序 == 正文；附录字母 A–H
  B 编号：h3 章前缀风格唯一；h4 序列严格递增；侧栏与正文风格一致
  C 排版：IGNORED/空标题/连续重复标题/冒号开头标题/el 粘连/双标点/超长标题
  D 方向：ar/he 的 dir=rtl 与 lang 属性
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / 'scripts'))
from bookkit import htmlparse as H  # noqa: E402
from repair_headings import h4_number  # noqa: E402

H3_RE = re.compile(r'<h3 class="text-xl font-bold text-dark dark:text-gray-200 mb-4"\s*>(.*?)</h3>', re.S)
H4_RE = re.compile(r'<h4 class="text-lg font-semibold (?:mt-4|mt-6) mb-2">(.*?)</h4>', re.S)
H5_RE = re.compile(r'<h5 class="font-semibold mt-\d mb-1">(.*?)</h5>', re.S)
SEC_RE = re.compile(r'<div[^>]*\bid="([a-z0-9-]+)"[^>]*\bclass="[^"]*content-section[^"]*"[^>]*>')
TOC_A = re.compile(r'<a href="#([a-z0-9-]+)"[^>]*class="[^"]*toc-[^"]*"|<a href="#([a-z0-9-]+)" class="toc-item[^"]*"')

WORD_CH = {  # 词形数字（应已转阿拉伯数字；出现即风格混用）
    'ru': r'[Гг]лава\s+(перв|втор|трет|четвёрт|пят|шест|седьм|восьм|девят|десят|одиннадцат|двенадцат|тринадцат|четырнадцат|пятнадцат|шестнадцат|семнадцат|восемнадцат|двадцат|тридцат|сороков|пятидесят|шестидесят)[а-яё]*\b',
    'ar': r'الفصل\s+(الأول|الثاني|الثالث|الرابع|الخامس|السادس|السابع|الثامن|التاسع|العاشر|الحادي|العشرون|الثلاثون|الأربعون|الخمسون|الستون)\b',
    'he': r'פרק\s+(שני|שלישי|רביעי|חמישי|שישי|שביעי|שמיני|תשיעי|עשירי)\b',
    'fr': r'Chapitre\s+(zéro|un|deux|trois|quatre|cinq|six|sept|huit|neuf|dix|onze|douze)\b',
    'pt': r'Cap[íi]tulo\s+(Zero|Um|Dois|Três|Quatro|Cinco|Seis|Sete|Oito|Nove|Dez|Onze|Doze|Vinte|Trinta)\b',
    'es': r'Cap[íi]tulo\s+(Cero|Uno|Dos|Tres|Cuatro|Cinco|Seis|Siete|Ocho|Nueve|Diez)\b',
    'en': r'Chapter\s+(Zero|One|Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten|Eleven|Twelve)\b',
    'th': r'บทที่\s*(ศูนย์|หนึ่ง|สอง|สาม|สี่|ห้า|หก|เจ็ด|แปด|เก้า|สิบ)\b',
    'ko': r'제\s*[영일이삼사오육칠팔구십백]+장',
}
DIGIT_CH = {  # ja/zh 系应全汉字；出现数字章号即混用
    'ja': r'第\s*[0-9]+\s*章',
}

def plain(html_fragment: str) -> str:
    import html as hm
    return re.sub(r'\s+', ' ', hm.unescape(re.sub(r'<[^>]+>', '', html_fragment))).strip()

def strip_code(html: str) -> str:
    return re.sub(r'(<pre\b.*?</pre>|<code\b.*?</code>|<script\b.*?</script>|<style\b.*?</style>)',
                  '⟦C⟧', html, flags=re.S | re.I)

def section_ids(raw: str):
    return [m.group(1) for m in SEC_RE.finditer(raw)]

def audit(path: Path, ver: str, zh_order: list):
    lang = path.stem
    raw = path.read_text(encoding='utf-8')
    issues, warns = [], []
    sids = section_ids(raw)
    # A1 正文章节顺序（相对同版本 zh 的子序列）
    zh_sub = [s for s in zh_order if s in set(sids)]
    mine_sub = [s for s in sids if s in set(zh_order)]
    if zh_sub != mine_sub:
        bad = [f'{a}≠{b}' for a, b in zip(zh_sub, mine_sub) if a != b][:3]
        issues.append(f'章节顺序与 zh 基准不一致（{len(zh_sub)} 节中首处 {bad}）')
    # A2 侧栏锚点顺序
    toc_ids = [a or b for a, b in TOC_A.findall(raw)]
    if not toc_ids:
        # v1.5 旧模板：侧栏在 <nav class="p-4"> 内，锚点无 toc- 类
        mnav = re.search(r'<nav class="p-4">.*?</nav>', raw, re.S)
        if mnav:
            toc_ids = re.findall(r'<a href="#([a-z0-9-]+)" class="block', mnav.group(0))
    seen, firsts = set(), []
    for t in toc_ids:
        if t not in seen:
            seen.add(t)
            firsts.append(t)
    toc_sec = [t for t in firsts if t in set(sids)]
    if toc_sec != mine_sub:
        issues.append(f'侧栏目录顺序与正文不一致（侧栏 {len(toc_sec)} vs 正文 {len(mine_sub)}）')
    # A3 附录字母顺序
    ap = [re.sub(r'.*?([A-H])[\s.．:：].*', r'\1', plain(m.group(1)))
          for m in H3_RE.finditer(raw)
          if re.match(r'^(付録|付錄|附録|附录|附錄|Anhang|Appendix|Appendice|Annexe|Ap[éêe]ndice|'
                     r'Anexo|Приложение|נספח|ملحق|ภาคผนวก|Lampiran|Tambahan|Παράρτημα|부록|Phụ lục)',
                      plain(m.group(1)))
          and re.search(r'\b[A-H]\b', plain(m.group(1)))]
    if ap and ap != sorted(ap):
        issues.append(f'附录字母顺序错乱：{ap}')
    # B1 h3 词形/异风格章号
    body = strip_code(raw)
    if lang in WORD_CH:
        n = len(re.findall(WORD_CH[lang], body))
        if n:
            issues.append(f'h3/正文残留词形章号 ×{n}')
    if lang in DIGIT_CH and ver != 'v1.5':
        n = len(re.findall(DIGIT_CH[lang], body))
        if n:
            issues.append(f'残留数字章号（应为汉字）×{n}')
    # B4 h4 序列严格递增（数值型）
    ms = list(SEC_RE.finditer(raw))
    for i, m in enumerate(ms):
        span = raw[m.start(): ms[i + 1].start() if i + 1 < len(ms) else len(raw)]
        vals = [h4_number(x) for x in H4_RE.findall(span)]
        nums = [v for v in vals if v is not None]
        dups = [(a, b) for a, b in zip(nums, nums[1:]) if b <= a]
        if dups:
            issues.append(f'{m.group(1)} h4 编号重复/回退 {len(dups)} 处（{dups[:3]}）')
    # B5 侧栏 vs h3 风格（ja 数字/汉字）
    if lang == 'ja' and ver != 'v1.5':
        h3_digit = len(re.findall(r'第[0-9]+章', body))
        if h3_digit:
            issues.append(f'全文件残留数字章号 ×{h3_digit}')
    # C 排版产物
    for m in H3_RE.finditer(raw):
        t = plain(m.group(1))
        if not t:
            issues.append(f'{m.group(0)[:0]}空 h3 标题')
        if re.match(r'^[：:，,、.]', t):
            issues.append(f'h3 以标点开头：{t[:30]}')
        if len(t) > 90:
            warns.append(f'h3 超长({len(t)}字)：{t[:40]}')
    h4s_all = [plain(m.group(1)) for m in H4_RE.finditer(raw)]
    if 'IGNORED' in raw:
        issues.append('残留 IGNORED 占位标题')
    for a, b in zip(h4s_all, h4s_all[1:]):
        if a and a == b:
            issues.append(f'连续重复 h4：{a[:36]}')
    if lang == 'el':
        n = len(re.findall(r'[α-ωάέήίόύώ]{2,}και(?=[\s,.])', strip_code(raw)))
        if n:
            issues.append(f'και 粘连 ×{n}')
    n_dp = len(re.findall(r'[。；，、]{2,}', strip_code(raw)))
    if n_dp:
        warns.append(f'连续同类标点 ×{n_dp}')
    # D 方向属性
    if lang in ('ar', 'he'):
        m = re.search(r'<html[^>]*>', raw)
        tag = m.group(0) if m else ''
        if 'dir="rtl"' not in tag and "dir='rtl'" not in tag:
            issues.append(f'html 标签缺 dir="rtl"：{tag[:60]}')
    return {'issues': issues, 'warns': warns, 'sections': len(sids)}

def main():
    vers = [a for a in sys.argv[1:] if a.startswith('v1.')] or ['v1.8']
    n_issue_files = 0
    for ver in vers:
        zh_path = ROOT / ver / 'zh-CN.html'
        zh_order = section_ids(zh_path.read_text(encoding='utf-8')) if zh_path.exists() else []
        for p in sorted((ROOT / ver).glob('*.html')):
            if p.stem == 'index' or (ver, p.stem) == ('v1.7', 'lzh'):
                continue
            try:
                r = audit(p, ver, zh_order)
            except Exception as e:
                print(f'✗ {ver}/{p.stem}: 审计失败 {e}')
                continue
            flag = '✗' if r['issues'] else '✓'
            if r['issues']:
                n_issue_files += 1
            print(f'{flag} {ver}/{p.stem} ({r["sections"]}节)')
            for i in r['issues']:
                print(f'    [问题] {i}')
            for w in r['warns'][:3]:
                print(f'    [提示] {w}')
    print(f'\n== 含问题文件 {n_issue_files} 个')

if __name__ == '__main__':
    main()
