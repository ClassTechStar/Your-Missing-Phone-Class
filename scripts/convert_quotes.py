# -*- coding: utf-8 -*-
"""引号体例转换：将中文文本的弯引号/直引号统一为直角引号「」（嵌套用『』），对齐《你缺失的那门计算机课》体例。

规则：
- 只处理 markdown 正文：跳过 ``` 代码围栏、行内代码 `...`、HTML 标签 <...> 内部。
- 弯引号（“”）用栈配对：深度 1 → 「」，深度 2 → 『』；段内不配平则整段跳过并报告。
- 直引号（"）逐行 toggle 配对：奇数个则整行跳过并报告。
- 跳过 HTML 属性：直引号出现在 <...> 内不计数。
用法：py scripts/convert_quotes.py --apply   （缺省为 dry-run 报告）
"""
import re
import sys
import glob

APPLY = '--apply' in sys.argv

def convert_curly(text):
    """栈配对转换弯引号；返回 (新文本, 跳过标记)。以“段”为单位（按空行分段）。"""
    out_parts = []
    skipped = False
    for para in re.split(r'(\n\s*\n)', text):
        if re.match(r'\s*$', para):
            out_parts.append(para)
            continue
        stack = []
        buf = []
        i = 0
        in_code = 0
        n = len(para)
        while i < n:
            ch = para[i]
            if para.startswith('`', i):
                j = para.find('`', i + 1)
                if j == -1:
                    buf.append(para[i:]); break
                buf.append(para[i:j + 1]); i = j + 1; continue
            if ch == '\u201c':
                stack.append('\u201c'); buf.append('\u300c' if len(stack) == 1 else '\u300e'); i += 1; continue
            if ch == '\u201d':
                if not stack:
                    skipped = True; break
                stack.pop()
                buf.append('\u300d' if not stack else '\u300f'); i += 1; continue
            buf.append(ch); i += 1
        if skipped or stack:
            # 不配平：整段原样保留
            out_parts.append(para)
            skipped = True
        else:
            out_parts.append(''.join(buf))
    return ''.join(out_parts), skipped

TAG_RE = re.compile(r'<[a-zA-Z!/][^>\n]*>')

def convert_straight_line(line):
    """直引号逐行 toggle；跳过 HTML 标签与行内代码；奇数个返回 None。"""
    events = []
    for m in TAG_RE.finditer(line):
        events.append((m.start(), m.end()))
    def in_tag(pos):
        return any(a <= pos < b for a, b in events)
    parts = []
    i = 0
    n = len(line)
    opens = 0
    while i < n:
        ch = line[i]
        if line.startswith('`', i):
            j = line.find('`', i + 1)
            if j == -1:
                parts.append(line[i:]); break
            parts.append(line[i:j + 1]); i = j + 1; continue
        if ch == '"' and not in_tag(i):
            parts.append('\u300c' if opens == 0 else '\u300d')
            opens ^= 1
            i += 1; continue
        parts.append(ch); i += 1
    if opens != 0:
        return None
    return ''.join(parts)

def process_md(path):
    text = open(path, encoding='utf-8').read()
    # 分离代码围栏
    chunks = re.split(r'(```[\s\S]*?```|~~~[\s\S]*?~~~)', text)
    changed = 0; skipped = 0
    out = []
    for idx, chunk in enumerate(chunks):
        if idx % 2 == 1:  # 围栏
            out.append(chunk); continue
        is_curly = ('\u201c' in chunk or '\u201d' in chunk)
        if is_curly:
            new, skip = convert_curly(chunk)
            out.append(new); skipped += 1 if skip else 0
        else:
            lines = chunk.split('\n')
            newlines = []; line_skipped = False
            for ln in lines:
                if '"' in ln:
                    conv = convert_straight_line(ln)
                    if conv is None:
                        newlines.append(ln); line_skipped = True
                    else:
                        newlines.append(conv)
                else:
                    newlines.append(ln)
            out.append('\n'.join(newlines))
            skipped += 1 if line_skipped else 0
        if out[-1] != chunk: changed += 1
    new_text = ''.join(out)
    if APPLY and new_text != text:
        open(path, 'w', encoding='utf-8', newline='').write(new_text)
    return changed, skipped

targets = []
targets += sorted(glob.glob('source/v1.9/chapters/*.md'))
targets += sorted(glob.glob('source/v1.9/parts/*.md'))
targets += sorted(glob.glob('source/chapters/*.md'))
targets += sorted(glob.glob('source/parts/*.md'))

tot_c = tot_s = 0
files_changed = 0
for p in targets:
    c, s = process_md(p)
    tot_c += c; tot_s += s
    if c: files_changed += 1
mode = 'APPLY' if APPLY else 'DRY-RUN'
print(f'[{mode}] files={len(targets)} changed_chunks={tot_c} skipped_chunks={tot_s} files_touched={files_changed}')
