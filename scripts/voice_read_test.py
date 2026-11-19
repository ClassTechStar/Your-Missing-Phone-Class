#!/usr/bin/env python3
"""voice_read_test.py — 朗读体检（方案 §6.3 的机器可执行版本）。

方案 §6.3 原文：

    1. 每章终稿用 TTS 朗读（或自己出声读）；
    2. 边听边标记：拗口、喘不上气、听了走神的三处，必改；
    3. 改完重听一遍，通过才进发布分支。

**这是最后一道无法自动化的门禁，人的语感是终点裁判。**
但 204 章（v1.9 的 120 + v1.8 的 84）加 18 种语言逐章人工朗读不是一次会话能做完的，
所以这里做两件事：

  1. 把"拗口 / 喘不上气 / 听了走神"三项**变成可检测的信号**，产出逐章问题清单；
  2. 清单进人工复核队列——机器只负责"标出可疑处"，改不改由人定。

三类信号的工程判据：

| 编号 | 类别 | 判据 | 校准依据 |
| --- | --- | --- | --- |
| R1 | 喘不上气 | 一口气要读完的连续段 > 45 字（中文约 30–40 字是一口气，逗号算半口） | 实测全书无标点连续段 P90=3 字、P99=1 字，只有流程箭头串与长排比段真正超标；46–60 字档 9428 处全是误报 |
| R2 | 拗口 | 流程箭头串 ≥4 段 / 顿号串 ≥4 / 同词重复 3 次 / 括号嵌套 2 层 / 中英数混排 ≥25 字符 | — |
| R3 | 听了走神 | 连续 3+ 句长度几乎相同 / 连续 3+ 句同开头 / 一句 3+ 抽象词堆叠 | — |

用法：
  py -3 scripts/voice_read_test.py --chapters source/v1.9/chapters
  py -3 scripts/voice_read_test.py --dir source/translations/en/chapters
  py -3 scripts/voice_read_test.py --chapters source/chapters --out state/read_v18.html
"""

from __future__ import annotations

import argparse
import json
import re
import statistics as st
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CJK_RE = re.compile(r"[぀-ヿ一-鿿가-힯]")
LATIN_RE = re.compile(r"[A-Za-z]")
RTL_RE = re.compile(r"[֐-ࣿ؀-ۿ]")
THAI_RE = re.compile(r"[฀-๿]")

# 抽象词：单个不���题，连续堆叠才走神
WALK_WORDS = ("提升", "优化", "打造", "构建", "赋能", "助力", "完善", "推动",
              "促进", "保障", "全方位", "多维度", "精细化", "智能化", "一体化")

ENUM_HEADS = re.compile(r"^(首先|其次|然后|最后|第[一二三四五六七八九十]|\d+[、.）)])")


def detect_lang(text: str) -> str:
    if len(THAI_RE.findall(text)) > 40:
        return "th"
    if len(CJK_RE.findall(text)) > 40:
        return "cjk"
    if len(RTL_RE.findall(text)) > 40:
        return "rtl"
    if len(LATIN_RE.findall(text)) > 40:
        return "latin"
    return "cjk"


# ---------------------------------------------------------------- 取正文

def prose_lines(text: str) -> list[str]:
    """取出真正会被朗读的行：去 frontmatter / 标题 / 表格 / 代码 / 围栏 / HTML。"""
    out: list[str] = []
    in_fence = False
    in_front = False
    seen_first = False
    for raw in text.split("\n"):
        s = raw.strip()
        if not seen_first:
            if s == "---":
                in_front = not in_front
                if not in_front:
                    seen_first = True
                continue
            if in_front:
                continue
            seen_first = True
        if s.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or not s:
            continue
        if s.startswith(":::"):
            continue
        if s.startswith("#"):
            continue
        if s.startswith("|"):
            continue
        if s.startswith("<!--"):
            continue
        if re.match(r"^<[a-zA-Z/!]", s):
            continue
        # 去掉行内标记
        s = re.sub(r"^\s*[-*+]\s+", "", s)
        s = re.sub(r"^\s*\d+\.\s+", "", s)
        s = re.sub(r"^\s*>\s?", "", s)
        s = re.sub(r"<[^>\n]{1,400}>", "", s)
        s = re.sub(r"`[^`\n]{1,120}`", "X", s)
        s = s.strip()
        if s:
            out.append(s)
    return out


def split_sentences(lines: list[str], lang: str) -> list[str]:
    sents: list[str] = []
    for ln in lines:
        if lang == "latin":
            parts = re.split(r"(?<=[.!?])\s+", ln)
        elif lang == "th":
            parts = [ln]
        else:
            parts = re.split(r"(?<=[。！？；…])\s*", ln)
        for p in parts:
            p = p.strip()
            if p:
                sents.append(p)
    return sents


def measure(s: str, lang: str) -> int:
    return len(CJK_RE.findall(s)) if lang in ("cjk", "rtl") else len(s)


# ---------------------------------------------------------------- 三类信号

# 各类语言的阈值。一口气能读多长，按"字数"换算：
#   中文约 30–40 字 / 句读点；西文约 15–18 词；泰文按空格分段。
#
# 阈值不是拍脑袋定的，是**按各语言自身的分布**定的：
# 实测全书每种语言"无标点连续段"长度的 P99.5 —— 超过它，才是这门语言里
# 读起来真的别扭的少数句子。（中文 P99.5=27、日文 43、韩文 44、西文 107–180、
# 阿拉伯文 228、泰文 348。中文用 45 而不是 27，是因为中文的段是"字数"、
# 西文是"字符数"，两者不可直接比较。）
THRESHOLDS = {
    #            R1a 无标点连续段  R1b 单句字数  R1b 分句数
    "cjk":   (45, 80, 5),
    "rtl":   (160, 200, 7),
    "th":    (200, 240, 8),
    "latin": (220, 260, 8),
}

# 按语言代码细调（值 = 该语言自身 P99.5 向上取整）
THRESHOLD_BY_CODE = {
    "zh-CN": (45, 80, 5), "zh-TW": (45, 80, 5), "yue": (45, 80, 5), "lzh": (45, 80, 5),
    "ja": (45, 80, 5), "ko": (46, 80, 5),
    "en": (135, 260, 8), "ru": (140, 270, 8), "it": (155, 280, 8), "pt": (150, 280, 8),
    "es": (148, 280, 8), "fr": (155, 280, 8), "de": (160, 290, 8), "el": (185, 300, 8),
    "ar": (230, 340, 9), "he": (110, 220, 8),
    "th": (350, 420, 10), "id": (138, 270, 8), "ms": (145, 275, 8),
}

_LANG_IN_PATH = re.compile(r"translations/([a-zA-Z-]+)/")


def thresholds_for(path_str: str, lang: str) -> tuple[int, int, int]:
    m = _LANG_IN_PATH.search(path_str.replace("\\", "/"))
    code = m.group(1) if m else None
    if code and code in THRESHOLD_BY_CODE:
        return THRESHOLD_BY_CODE[code]
    return THRESHOLDS.get(lang, THRESHOLDS["cjk"])


def check_r1_breath(paras: list[str], sents: list[str], lang: str,
                    limits: tuple[int, int, int] | None = None) -> list[dict]:
    """喘不上气：一口气要读完的连续段太长 / 一句里塞太多分句。"""
    out = []
    limit, sent_limit, comma_limit = limits or THRESHOLDS.get(lang, THRESHOLDS["cjk"])
    for para in paras:
        # 断句点必须包含 ASCII 标点——西文正文里的逗号是 ","，
        # 漏掉它会把整段当成"一个一口气读不完的长句"。
        for part in re.split(r"[。！？；，、：\n,;:!?.]", para):
            n = measure(part, lang)
            if n > limit:
                out.append({
                    "id": "R1", "kind": "喘不上气",
                    "metric": f"无标点连续 {n} 字 > {limit}",
                    "excerpt": part[:110],
                    "fix": "这段一口气读不完：中间补句号，或拆成两步分号。",
                })
    for s in sents:
        n = measure(s, lang)
        commas = s.count("，") + s.count(",")
        if n > sent_limit and commas >= comma_limit:
            out.append({
                "id": "R1", "kind": "喘不上气",
                "metric": f"单句 {n} 字、带 {commas} 个分句",
                "excerpt": s[:110],
                "fix": "一句里塞太多层意思：拆成两句。",
            })
    return out


def paren_depth(s: str) -> int:
    """真实括号嵌套层数（两个并列括号不是嵌套）。"""
    depth = best = 0
    for ch in s:
        if ch in "（(":
            depth += 1
            best = max(best, depth)
        elif ch in "）)":
            depth = max(0, depth - 1)
    return best


def is_chapter_ref_chain(s: str) -> bool:
    """整串都是章节引用（第六章 → 第十四章）——这是导航表，不是要朗读的散文。"""
    parts = [p.strip() for p in re.split(r"[→➔]|->", s) if p.strip()]
    if len(parts) < 2:
        return False
    hits = sum(1 for p in parts
               if re.match(r"^(第[一二三四五六七八九十百零]+章|附录\s*[A-H]|第[一二三四五六七八九十]+至)", p))
    return hits >= len(parts) - 1


def is_codeish(s: str) -> bool:
    """括号里装的是代码而不是说明（"Color(.systemGray6), .primary"）。"""
    inner = "".join(re.findall(r"[（(]([^（）()]*)[）)]", s))
    if not inner:
        return True
    # 代码特征：大写驼峰、点号路径、下划线、函数调用
    return bool(re.search(r"[A-Za-z_]{2,}\.[A-Za-z_]{2,}|\(\)|\{|\}|::|[a-z][A-Z]", inner))


def check_r2_tongue(paras: list[str], sents: list[str], lang: str) -> list[dict]:
    """拗口：流程串、顿号串、重复、括号嵌套、中英数混排。"""
    out = []
    for s in sents:
        arrows = s.count("→") + s.count("➔") + s.count("->")
        circled = len(re.findall(r"[①②③④⑤⑥⑦⑧⑨⑩]", s))
        if (arrows >= 4 or circled >= 4) and not is_chapter_ref_chain(s):
            out.append({
                "id": "R2", "kind": "拗口",
                "metric": f"流程串 {max(arrows, circled)} 段连排",
                "excerpt": s[:110],
                "fix": "连着念一串箭头会打结：改成编号列表，每步一行。",
            })
        # 顿号串：中文 4 个是正常枚举，6 个以上且整串偏长才真的拗口。
        # 日文/西文的「、」与逗号是正常分隔符，不适用这条。
        if lang == "cjk" and s.count("、") >= 6 and len(s) > 40:
            out.append({
                "id": "R2", "kind": "拗口",
                "metric": f"连续 {s.count('、')} 个顿号",
                "excerpt": s[:110],
                "fix": "顿号串太长：拆成列表，或用「和」收口。",
            })
        for w in ("这个", "那个", "然后", "就是", "所以", "但是", "而且", "或者"):
            if s.count(w) >= 3:
                out.append({
                    "id": "R2", "kind": "拗口",
                    "metric": f"「{w}」重复 {s.count(w)} 次",
                    "excerpt": s[:110],
                    "fix": f"重复的「{w}」删掉或换个说法。",
                })
                break
        if paren_depth(s) >= 2 and not is_codeish(s):
            out.append({
                "id": "R2", "kind": "拗口",
                "metric": "括号嵌套过多",
                "excerpt": s[:110],
                "fix": "括号只留一层，次要说明挪到句后。",
            })
        # 中英数混排：只对中文有意义——西文正文本身就是拉丁字母，
        # 对英/俄/西/阿等语言这条规则必然全量误报。
        if lang in ("cjk", "rtl"):
            for m in re.finditer(r"(?:[A-Za-z0-9][A-Za-z0-9 .,/_+-]*){6,}", s):
                seg = m.group(0)
                if len(seg) >= 40 and "(" not in s[max(0, m.start() - 2):m.start()] \
                        and "（" not in s[max(0, m.start() - 2):m.start()]:
                    out.append({
                        "id": "R2", "kind": "拗口",
                        "metric": f"中英数混排 {len(seg)} 字符连续",
                        "excerpt": s[:110],
                        "fix": "英文与代码单独成行，别塞在长句中间。",
                    })
                    break
    return out


def check_r3_wander(paras: list[str], lang: str) -> list[dict]:
    """听了走神：节奏单调、开头雷同、抽象词堆叠。

    **必须在同一段内判断**——跨段比较两句话的长度没有意义
    （全书级比较会把不同章节的普通句子误判成"节奏单调"）。
    """
    out = []
    for para in paras:
        sents = split_sentences([para], lang)
        if len(sents) < 2:
            continue
        lens = [measure(s, lang) for s in sents]
        # 段内连续 3 句长度几乎相同
        i = 0
        while i + 2 < len(lens):
            win = lens[i:i + 3]
            if min(win) >= 18 and (st.pstdev(win) / max(st.mean(win), 1)) < 0.12:
                out.append({
                    "id": "R3", "kind": "听了走神",
                    "metric": f"段内连续 3 句长度几乎相同（{win}）",
                    "excerpt": sents[i][:110],
                    "fix": "把其中一句改成短句或加个具体细节，打断节奏。",
                })
                i += 3
                continue
            i += 1
        # 段内连续 3 句同开头
        for i in range(len(sents) - 2):
            heads = [s[:2] for s in sents[i:i + 3]]
            if len(set(heads)) == 1 and heads[0].strip() and not ENUM_HEADS.match(heads[0]):
                out.append({
                    "id": "R3", "kind": "听了走神",
                    "metric": f"段内连续 3 句同开头「{heads[0]}」",
                    "excerpt": sents[i][:110],
                    "fix": "换开头：把主语提前，或从场景切入。",
                })
                break
        # 抽象词堆叠
        for s in sents:
            hits = sum(s.count(w) for w in WALK_WORDS)
            if hits >= 3:
                out.append({
                    "id": "R3", "kind": "听了走神",
                    "metric": f"一句里 {hits} 个抽象词（{'/'.join(w for w in WALK_WORDS if w in s)[:40]}）",
                    "excerpt": s[:110],
                    "fix": "抽象词换成具体的东西：一个数字、一个操作、一句后果。",
                })
                break
        # 段内连续 5 行等长
        plens = [measure(ln, lang) for ln in para.split("\n")]
        i = 0
        while i + 4 < len(plens):
            win = plens[i:i + 5]
            if min(win) >= 12 and (st.pstdev(win) / max(st.mean(win), 1)) < 0.10:
                out.append({
                    "id": "R3", "kind": "听了走神",
                    "metric": f"连续 5 行长度几乎相同（{win}）",
                    "excerpt": para[:110],
                    "fix": "连续等长的行读起来像念清单：把其中一条改成短句。",
                })
                i += 5
                continue
            i += 1
    return out


# ---------------------------------------------------------------- 主流程

def analyse(text: str, path: str = "") -> tuple[str, list[dict], dict]:
    lines = prose_lines(text)
    lang = detect_lang("\n".join(lines))
    sents = split_sentences(lines, lang)
    limits = thresholds_for(path, lang)
    issues = (check_r1_breath(lines, sents, lang, limits)
              + check_r2_tongue(lines, sents, lang)
              + check_r3_wander(lines, lang))
    ml = [measure(s, lang) for s in sents] or [0]
    stats = {
        "lang": lang,
        "lines": len(lines),
        "sentences": len(sents),
        "avg_sentence": round(st.mean(ml), 1),
        "max_sentence": max(ml),
    }
    return lang, issues, stats


def analyse_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    lang, issues, stats = analyse(text, str(path))
    return {
        "file": path.name,
        "path": str(path),
        "issues": issues,
        "stats": stats,
        "by_id": dict(Counter(i["id"] for i in issues)),
    }


def render_report(rows: list[dict], out: Path, label: str) -> None:
    import html as H
    total = sum(len(r["issues"]) for r in rows)
    cnt = Counter()
    for r in rows:
        for i in r["issues"]:
            cnt[i["id"]] += 1
    lines = [
        "<!DOCTYPE html><html lang='zh-CN'><head><meta charset='utf-8'>",
        f"<title>朗读体检 · {H.escape(label)}</title>",
        "<style>body{font-family:-apple-system,'Segoe UI','Microsoft YaHei',sans-serif;"
        "margin:24px;background:#fafafa;color:#222}h1{font-size:20px}"
        "table{border-collapse:collapse;font-size:12px;background:#fff}"
        "th,td{border:1px solid #e0e0e0;padding:5px 9px;text-align:left;vertical-align:top}"
        "th{background:#f5f5f5;position:sticky;top:0}"
        ".R1{background:#fff7e0}.R2{background:#ffeef0}.R3{background:#eef3ff}"
        ".ex{color:#555;font-size:11px}.fx{color:#047857;font-size:11px}"
        ".meta{color:#666;font-size:12px;margin-bottom:16px}</style></head><body>",
        f"<h1>朗读体检报告 · {H.escape(label)}</h1>",
        f"<div class='meta'>共 {len(rows)} 章，问题点 {total} 处"
        f"（R1 喘不上气 {cnt['R1']} / R2 拗口 {cnt['R2']} / R3 听了走神 {cnt['R3']}）"
        "<br><b>这是机器标出的可疑处，不是判决。</b>"
        "方案 §6.3 说得很清楚：人的语感是终点裁判。"
        "本工具只负责把最可能读不顺的地方捞出来，改不改由人定。</div>",
        "<table><tr><th>文件</th><th>语言</th><th>句数</th><th>均句长</th><th>最长句</th>"
        "<th>R1</th><th>R2</th><th>R3</th><th>问题点</th></tr>",
    ]
    for r in rows:
        s = r["stats"]
        lines.append(
            f"<tr><td>{H.escape(r['file'])}</td><td>{s['lang']}</td><td>{s['sentences']}</td>"
            f"<td>{s['avg_sentence']}</td><td>{s['max_sentence']}</td>"
            f"<td>{r['by_id'].get('R1',0)}</td><td>{r['by_id'].get('R2',0)}</td>"
            f"<td>{r['by_id'].get('R3',0)}</td><td>{len(r['issues'])}</td></tr>")
    lines.append("</table><h2>逐条问题</h2>")
    for r in rows:
        if not r["issues"]:
            continue
        lines.append(f"<h3>{H.escape(r['file'])}</h3><table><tr>"
                     "<th>类</th><th>类别</th><th>信号</th><th>原文</th><th>改法</th></tr>")
        for i in r["issues"]:
            lines.append(
                f"<tr class='{i['id']}'><td>{i['id']}</td><td>{i['kind']}</td>"
                f"<td>{H.escape(i['metric'])}</td>"
                f"<td class='ex'>{H.escape(i['excerpt'])}</td>"
                f"<td class='fx'>{H.escape(i['fix'])}</td></tr>")
        lines.append("</table>")
    lines.append("</body></html>")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="朗读体检（方案 §6.3）")
    ap.add_argument("--chapters", help="章节目录")
    ap.add_argument("--dir", action="append", default=[], help="章节目录（可多次）")
    ap.add_argument("--glob", default="*.md")
    ap.add_argument("--out", help="HTML 报告路径")
    ap.add_argument("--json-out", help="JSON 清单路径")
    ap.add_argument("--label", default="")
    args = ap.parse_args()

    dirs = list(args.dir)
    if args.chapters:
        dirs.append(args.chapters)
    if not dirs:
        print("用法：--chapters <目录> 或 --dir <目录>", file=__import__("sys").stderr)
        return 2

    rows = []
    for d in dirs:
        for p in sorted(Path(d).glob(args.glob)):
            rows.append(analyse_file(p))

    total = sum(len(r["issues"]) for r in rows)
    cnt = Counter()
    for r in rows:
        for i in r["issues"]:
            cnt[i["id"]] += 1
    print(f"[i] {len(rows)} 章，问题点 {total} 处"
          f"（R1 {cnt['R1']} / R2 {cnt['R2']} / R3 {cnt['R3']}）")
    for r in sorted(rows, key=lambda r: -len(r["issues"]))[:10]:
        if r["issues"]:
            print(f"    {len(r['issues']):>3}  {r['file']}  {r['by_id']}")

    if args.out:
        render_report(rows, Path(args.out), args.label or ", ".join(dirs))
        print(f"[+] 报告：{args.out}")
    if args.json_out:
        jp = Path(args.json_out)
        jp.parent.mkdir(parents=True, exist_ok=True)
        jp.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"[+] 清单：{jp}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
