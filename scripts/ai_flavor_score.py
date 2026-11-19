#!/usr/bin/env python3
"""ai_flavor_score.py — 逐章 AI 味诊断（方案第〇层）。

用途：诊断排序（找最差的 40 章）。**【不用于验收】。**
理由：一旦本分数成为门禁，写作会开始为指标优化，产出分数全绿但一股
机灵假味的文本。听诊器，不是法官。

用法：
  py -3 scripts/ai_flavor_score.py source/v1.9/chapters --out state/flavor_report.html
  py -3 scripts/ai_flavor_score.py source/v1.9/chapters --worst 40 --out state/worst40.txt

输出：
  flavor_report.html — 120 章按分数升序（最差在前），含每指标明细
  worst40.txt        — 最差 N 章清单，作为第二层证据注入的作业范围

实现刻意保持朴素：正则 + 标准库，不依赖 NLP 模型。
朴素才可解释、可复跑、可进版本控制。
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
WL_PATH = HERE / "wordlists.json"

# ---------------------------------------------------------------- 词表加载

def load_wordlists(path: Path = WL_PATH) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


# ---------------------------------------------------------------- 基础切分

SENT_SPLIT = re.compile(r"[。！？；]")
# 行内 HTML / 围栏代码 / 表格行 不参与正文指标，避免把标记噪声算成人味信号
HTML_TAG = re.compile(r"<[^>]+>")
FENCE = re.compile(r"```.*?```", re.S)
INLINE_CODE = re.compile(r"`[^`\n]+`")


def strip_non_prose(text: str) -> str:
    text = FENCE.sub("", text)
    text = INLINE_CODE.sub("", text)
    text = HTML_TAG.sub("", text)
    return text


def split_sentences(text: str) -> list[str]:
    return [s.strip() for s in SENT_SPLIT.split(text) if s.strip()]


def split_paragraphs(text: str) -> list[str]:
    out = []
    for line in text.split("\n"):
        line = line.strip()
        if not line or line.startswith(("#", "|", "---", ":::", "::: ", "- ", "* ", "<!--")):
            continue
        if re.match(r"^\d+\.\s", line):
            continue
        out.append(line)
    return out


def git_commit() -> str:
    try:
        r = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, cwd=ROOT, timeout=10,
        )
        return r.stdout.strip() or "unknown"
    except Exception:
        return "unknown"


# ---------------------------------------------------------------- 指标计算

class Metrics:
    """七项指标。命名与方案 §3.1 一一对应。"""

    def __init__(self, wl: dict):
        self.wl = wl
        spec = wl["specificity_triggers"]
        self.rx_num = re.compile(spec["number_unit"])
        self.rx_device = re.compile(spec["device"])
        self.rx_version = re.compile(spec["version"])
        self.rx_price = re.compile(spec["price"])
        self.rx_date = re.compile(spec["date"])
        self.rx_not_but = re.compile(r"不是[^。！？；]{2,24}，(?:而)?是")
        self.rx_not_but_only = re.compile(r"不是[^。！？；]{2,24}，而是")
        self.rx_dash = re.compile(r"——")
        rhet = wl["rhetoric_patterns"]
        self.para_openers = rhet["para_openers"]
        self.para_closers = rhet["para_closers"]
        self.chapter_closers = rhet["chapter_closers"]
        self.black_s = wl["s_level"]
        self.black_a = list(wl["a_level"].keys())
        self.black_b = wl["b_level"]

    # --- 单章指标 ---
    def score_text(self, raw: str) -> dict:
        text = strip_non_prose(raw)
        sents = split_sentences(text)
        paras = split_paragraphs(text)
        n = max(len(text), 1)
        nk = 1000.0 / n          # 每千字
        n10k = 10000.0 / n       # 每万字

        short_ratio = (sum(1 for s in sents if len(s) < 8) / len(sents)) if sents else 0.0

        not_but = len(self.rx_not_but_only.findall(text))
        not_but_per_kchar = not_but * nk

        # 三连排比：同段内 "，" 分隔的并列项 ≥ 3，或"第一/第二/第三"式
        triple = 0
        for p in paras:
            if re.search(r"(?:第一|一、)[^\n]{0,40}(?:第二|二、)[^\n]{0,40}(?:第三|三、)", p):
                triple += 1
            else:
                items = [x for x in re.split(r"[，、]", p) if 2 <= len(x.strip()) <= 24]
                if len(items) >= 3 and p.count("是") + p.count("有") >= 3:
                    triple += 1
        rhetoric_per_kchar = (not_but + triple) * nk

        black_hits = 0
        black_detail: dict[str, int] = {}
        for w in self.black_s:
            c = text.count(w)
            if c:
                black_hits += c
                black_detail[w] = black_detail.get(w, 0) + c
        for w in self.black_a:
            c = text.count(w)
            if c:
                black_hits += c
                black_detail[w] = black_detail.get(w, 0) + c
        blacklist_per_10k = black_hits * n10k

        b_level_hits = {w: text.count(w) for w in self.black_b if text.count(w)}

        para_heads = [p[:2] for p in paras]
        para_start_dedup = (len(set(para_heads)) / len(para_heads)) if para_heads else 1.0

        spec_hits = (
            len(self.rx_num.findall(text))
            + len(self.rx_device.findall(text))
            + len(self.rx_version.findall(text))
            + len(self.rx_price.findall(text))
            + len(self.rx_date.findall(text))
        )
        specificity_per_kchar = spec_hits * nk

        # 直引语：中文弯引号 “ ” 与直角/ASCII 引号都算。
        # 实测：本仓库源稿全书用 ASCII 双引号（11 万+ 处），只认弯引号会把
        # 指标 7 恒读成 0——那不是"没有真话"，是检测器认错了引号。
        quotes = re.findall(r"“([^”]{4,120})”", text)
        quotes += re.findall(r'"([^"\n]{4,120})"', text)
        quotes_per_kchar = len(quotes) * nk

        dashes = len(self.rx_dash.findall(text))
        dash_per_kchar = dashes * nk

        opener_hits = sum(
            1 for p in paras
            if re.match(r"^(?:" + "|".join(map(re.escape, self.para_openers)) + r")[，,、：:]", p)
        )
        opener_per_kchar = opener_hits * nk

        closer_hits = sum(
            1 for p in paras
            if re.search(r"(?:" + "|".join(map(re.escape, self.para_closers)) + r")[。！？]?$", p)
        )
        closer_per_kchar = closer_hits * nk

        chap_closer = sum(text.count(c) for c in self.chapter_closers)

        return {
            "chars": len(text),
            "sentences": len(sents),
            "paragraphs": len(paras),
            "short_ratio": short_ratio,
            "not_but_per_kchar": not_but_per_kchar,
            "rhetoric_per_kchar": rhetoric_per_kchar,
            "blacklist_per_10k": blacklist_per_10k,
            "para_start_dedup": para_start_dedup,
            "specificity_per_kchar": specificity_per_kchar,
            "quotes_per_kchar": quotes_per_kchar,
            "dash_per_kchar": dash_per_kchar,
            "opener_per_kchar": opener_per_kchar,
            "closer_per_kchar": closer_per_kchar,
            "chapter_closer_hits": chap_closer,
            "blacklist_detail": black_detail,
            "b_level_hits": b_level_hits,
            "quote_samples": quotes[:5],
        }


# ---------------------------------------------------------------- 章长 CV

def chapter_cv(paths: list[Path], m: Metrics) -> tuple[float, dict[str, int]]:
    lens = {}
    for p in paths:
        lens[p.name] = len(strip_non_prose(p.read_text(encoding="utf-8")))
    values = list(lens.values())
    cv = statistics.pstdev(values) / statistics.mean(values) if len(values) > 1 else 0.0
    return cv, lens


# ---------------------------------------------------------------- 合成分数

def compose(metrics: dict, cv: float) -> float:
    """加权合成单一分数（方案 §3.2）。分数越高＝AI 味越重。

    指标 6（具体性）与 7（直引语）反向：越低越 AI。
    """
    def clamp(x, lo=0.0, hi=1.0):
        return max(lo, min(hi, x))

    cv_n = clamp(cv / 0.35)                      # 目标 CV > 0.25 视为健康
    short_n = clamp(metrics["short_ratio"] / 0.05)  # 目标 > 3%
    rhet_n = clamp(metrics["rhetoric_per_kchar"] / 3.0)
    black_n = clamp(metrics["blacklist_per_10k"] / 30.0)
    para_n = 1.0 - clamp((metrics["para_start_dedup"] - 0.3) / 0.5)
    spec_n = 1.0 - clamp((metrics["specificity_per_kchar"] - 2.0) / 12.0)
    quote_n = 1.0 - clamp(metrics["quotes_per_kchar"] / 1.5)
    dash_n = clamp(metrics["dash_per_kchar"] / 6.0)

    return round(
        0.15 * cv_n
        + 0.10 * short_n
        + 0.15 * rhet_n
        + 0.15 * black_n
        + 0.10 * para_n
        + 0.15 * spec_n
        + 0.05 * quote_n
        + 0.15 * dash_n,
        4,
    )


# ---------------------------------------------------------------- 报告

HTML_HEAD = """<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<title>AI 味诊断报告 · {commit}</title>
<style>
 body{{font-family:-apple-system,"Segoe UI","Microsoft YaHei",sans-serif;margin:24px;background:#fafafa;color:#222}}
 h1{{font-size:20px}} h2{{font-size:16px;margin-top:28px}}
 table{{border-collapse:collapse;font-size:12px;background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.08)}}
 th,td{{border:1px solid #e0e0e0;padding:5px 9px;text-align:right;white-space:nowrap}}
 th{{background:#f5f5f5;position:sticky;top:0}}
 td.l,th.l{{text-align:left}}
 .bad{{background:#ffe9e9}} .warn{{background:#fff7e0}} .good{{background:#eaf7ea}}
 .meta{{color:#666;font-size:12px;margin-bottom:18px}}
 code{{background:#f0f0f0;padding:1px 4px}}
</style></head><body>
<h1>《你缺失的那门手机课》AI 味诊断报告</h1>
<div class="meta">
 生成于 git <code>{commit}</code> ·
 语料 <code>{chapters}</code> 章 / {total_chars:,} 字符 ·
 章长 CV = <code>{cv:.4f}</code>（目标 &gt; 0.25）<br>
 <b>本分数仅用于诊断排序（找最差的章），不用于验收。</b>
 一旦变成门禁，写作会开始为指标优化，产出"分数全绿但一股机灵假味"的文本。
</div>
"""


def render_report(rows: list[dict], commit: str, cv: float, total_chars: int) -> str:
    out = [HTML_HEAD.format(commit=commit, chapters=len(rows), cv=cv, total_chars=total_chars)]
    out.append("<h2>一、逐章明细（分数升序，最差在前）</h2>\n")
    out.append(
        "<table><tr>"
        "<th class='l'>#</th><th class='l'>文件</th><th class='l'>标题</th>"
        "<th>分数</th><th>字符</th><th>短句%</th><th>修辞/千字</th><th>黑名单/万字</th>"
        "<th>段首去重</th><th>具体性/千字</th><th>引语/千字</th><th>破折号/千字</th>"
        "<th>段首套话</th><th>段尾套话</th><th>B级词</th>"
        "</tr>\n"
    )
    for i, r in enumerate(rows, 1):
        score = r["score"]
        cls = "bad" if score >= 0.6 else ("warn" if score >= 0.45 else "good")
        m = r["metrics"]
        out.append(
            f"<tr><td class='l'>{i}</td>"
            f"<td class='l'><code>{r['file']}</code></td>"
            f"<td class='l'>{r['metrics'].get('title','')}</td>"
            f"<td class='{cls}'>{score:.3f}</td>"
            f"<td>{m['chars']:,}</td>"
            f"<td>{m['short_ratio']*100:.1f}</td>"
            f"<td>{m['rhetoric_per_kchar']:.2f}</td>"
            f"<td>{m['blacklist_per_10k']:.1f}</td>"
            f"<td>{m['para_start_dedup']*100:.0f}%</td>"
            f"<td>{m['specificity_per_kchar']:.2f}</td>"
            f"<td>{m['quotes_per_kchar']:.2f}</td>"
            f"<td>{m['dash_per_kchar']:.1f}</td>"
            f"<td>{m['opener_per_kchar']:.2f}</td>"
            f"<td>{m['closer_per_kchar']:.2f}</td>"
            f"<td>{len(m['b_level_hits'])}</td>"
            "</tr>\n"
        )
    out.append("</table>\n")

    # 词表命中统计
    agg: dict[str, int] = {}
    for r in rows:
        for w, c in r["metrics"]["blacklist_detail"].items():
            agg[w] = agg.get(w, 0) + c
    out.append("<h2>二、黑名单命中统计（全库）</h2>\n<table><tr><th class='l'>词</th><th>命中</th></tr>\n")
    for w, c in sorted(agg.items(), key=lambda x: -x[1]):
        out.append(f"<tr><td class='l'>{w}</td><td>{c}</td></tr>\n")
    out.append("</table>\n")

    out.append("<h2>三、诊断结论</h2>\n")
    out.append(
        "<p>按方案 §11.1，检测器只用于找最差的章，不进 CI 门禁。"
        "下面三列是<b>定位</b>，不是<b>评分</b>。</p>\n"
    )
    out.append("</body></html>\n")
    return "".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description="逐章 AI 味诊断（排序用，非验收）")
    ap.add_argument("chapters_dir")
    ap.add_argument("--out", help="HTML 报告输出路径")
    ap.add_argument("--worst", type=int, default=40, help="输出最差 N 章清单")
    ap.add_argument("--worst-out", help="worst 清单输出路径")
    ap.add_argument("--json-out", help="指标 JSON 输出路径（供其它脚本消费）")
    args = ap.parse_args()

    wl = load_wordlists()
    m = Metrics(wl)
    cdir = Path(args.chapters_dir)
    paths = sorted(cdir.glob("*.md"))
    if not paths:
        print(f"[!] 没有找到章节：{cdir}", file=sys.stderr)
        return 2

    cv, lens = chapter_cv(paths, m)
    rows = []
    for p in paths:
        raw = p.read_text(encoding="utf-8")
        met = m.score_text(raw)
        title = ""
        for line in raw.split("\n"):
            if line.startswith("### "):
                title = line[4:].strip()
                break
        met["title"] = title
        rows.append({"file": p.name, "path": str(p), "metrics": met, "score": compose(met, cv)})

    rows.sort(key=lambda r: -r["score"])
    total_chars = sum(lens.values())
    commit = git_commit()

    if args.out:
        outp = Path(args.out)
        outp.parent.mkdir(parents=True, exist_ok=True)
        outp.write_text(render_report(rows, commit, cv, total_chars), encoding="utf-8")
        print(f"[+] 报告：{outp}")

    if args.worst_out or args.worst:
        wp = Path(args.worst_out or (Path(args.out).parent / f"worst{args.worst}.txt"))
        wp.parent.mkdir(parents=True, exist_ok=True)
        lines = [f"# AI 味最重 {args.worst} 章（方案 §5 第二层作业范围）",
                 f"# commit {commit}", ""]
        for i, r in enumerate(rows[:args.worst], 1):
            mm = r["metrics"]
            lines.append(
                f"{i:>2}. {r['file']}  score={r['score']:.3f}  {mm['title']}\n"
                f"    字符={mm['chars']:,} 黑名单/万字={mm['blacklist_per_10k']:.1f} "
                f"修辞/千字={mm['rhetoric_per_kchar']:.2f} 具体性/千字={mm['specificity_per_kchar']:.2f} "
                f"引语/千字={mm['quotes_per_kchar']:.2f} 段首套话={mm['opener_per_kchar']:.2f} "
                f"段尾套话={mm['closer_per_kchar']:.2f} 破折号/千字={mm['dash_per_kchar']:.1f}"
            )
        wp.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"[+] 最差清单：{wp}")

    if args.json_out:
        jp = Path(args.json_out)
        jp.parent.mkdir(parents=True, exist_ok=True)
        jp.write_text(
            json.dumps({"commit": commit, "cv": cv, "rows": rows}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"[+] 指标 JSON：{jp}")

    print(f"[i] 共 {len(rows)} 章，章长 CV={cv:.4f}，总分区间 "
          f"{min(r['score'] for r in rows):.3f}–{max(r['score'] for r in rows):.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
