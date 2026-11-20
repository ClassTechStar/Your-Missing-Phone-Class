#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""deai_html.py — 方案 §4 第一层文本手术在 HTML 文本节点上的实现。

边界（严格按《手机课去AI味深度改造方案.md》）：
  · 只处理 v1.9 / v1.8 目录下的 .html，不碰任何非 HTML 文件
  · 规则复用 scripts/wordlists.json 与 scripts/voice_lint.py 的 Surgeon
    （S1–S6、S7、W-s/W-a），不自行扩展规则
  · 标签、属性、类名、id、链接、资源引用、script/style 原样保留
  · §7.1 中文真源原则：中文文件做全文手术；18 语按「翻译定位」只做通用
    S4/S7（标点与段首），不套中文专有规则
  · §4.3 T1 章标题模板破除：用 scripts/title_rewrites.json 的既有表，同步替换
    所有出现处（标题 + 目录 + 交叉引用）
  · §11.2 准确 > 文学性；不做堆语气词的「假人味」
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import voice_lint as VL  # noqa: E402

WL = json.loads((ROOT / "scripts" / "wordlists.json").read_text(encoding="utf-8"))
TITLES = json.loads((ROOT / "scripts" / "title_rewrites.json").read_text(encoding="utf-8"))

# 标签及属性整体保护；文本节点单独送进手术
RX_TAG = re.compile(r"<[^>]*>", re.S)
RX_SKIP = re.compile(r"<(script|style)\b[^>]*>.*?</\1>", re.S | re.I)
RX_COMMENT = re.compile(r"<!--.*?-->", re.S)
RX_ENTITY = re.compile(r"&[a-zA-Z]{1,12};|&#\d{1,7};")


def make_surgeon(lang: str, seed: int | None = None) -> VL.Surgeon:
    s = VL.Surgeon(WL, seed if seed is not None else WL["surgery"]["seed"], lang=lang)
    s.rules_enabled = {"S1", "S2", "S3", "S4", "S5", "S6", "S7", "W"}
    s.set_lang(lang)
    if lang in ("ja", "lzh"):
        # 方案 §7.3：文言文是文化彩蛋、日文标点体系独立——两者不强求去味。
        # 全部规则关闭，保持原样（处理器会跳过这两个文件）。
        s.rules_enabled.clear()
    return s


def transform_text(seg: str, surgeon: VL.Surgeon, chinese: bool, s5_budget: int) -> str:
    """处理单个文本节点（已确认不含标签/实体）。"""
    if not seg.strip() or not any("\u4e00" <= c <= "\u9fff" for c in seg) and chinese:
        # 中文文件里纯数字/西文节点也允许走 S4/S7（标点通用），但黑名单等跳过
        pass
    out = seg
    # 句级手术：S4 破折号 / S7 段首连接（各语言通用）
    if "S4" in surgeon.rules_enabled:
        out = surgeon.s4_dash(out)
    if "S7" in surgeon.rules_enabled:
        parts = out.split("\n")
        parts = surgeon.s7_connectors(parts)
        out = "\n".join(parts)
    if chinese:
        # S1 三连 / S2 不是…而是 / W 黑名单（中文专有）
        out = surgeon.prose_transform(out)
        # S3 段尾总结句
        out = surgeon.s3_closer_line(out)
        # S5 问句配额（每章 ≤2）
        surgeon._q_budget = s5_budget
        before = surgeon.hits.get("S5", 0)
        out = surgeon.s5_questions(out)
        s5_budget = surgeon._q_budget
    return out, s5_budget


def process_html(path: Path, lang: str, dry: bool = False) -> dict:
    raw = path.read_text(encoding="utf-8")
    chinese = lang in ("zh",)
    surgeon = make_surgeon(lang)
    hits_before = dict(surgeon.hits)

    # 0) 先抽出 script/style 与注释，占位保护
    stash: list[str] = []

    def keep(m: re.Match) -> str:
        stash.append(m.group(0))
        return f"\x00KEEP{len(stash)-1}\x00"

    # 0.5) T1 章标题模板破除：在标签完整时替换，覆盖标题 / 目录 / 交叉引用
    t1 = 0
    if chinese:
        for fname, rec in TITLES.items():
            if not fname.endswith(".md"):
                continue
            new = rec.get("title")
            if not new:
                continue
            m = re.match(r"^(第[一二三四五六七八九十百零]+章|附录[A-H]|结语)[：:]", new)
            if not m:
                continue
            prefix = m.group(1)
            pat = re.compile(r"(<h3[^>]*>)(" + re.escape(prefix) + r"[：:][^<]{2,80}?)(</h3>)")
            def rep(mm):
                nonlocal t1
                old = mm.group(2)
                if old == new or "——" not in old:
                    return mm.group(0)
                t1 += 1
                return mm.group(1) + new + mm.group(3)
            work_pre = pat.sub(rep, work) if False else None  # placeholder
        # 用函数统一替换
        def t1_sub(html: str) -> str:
            nonlocal t1
            for fname, rec in TITLES.items():
                if not fname.endswith(".md"): continue
                new = rec.get("title")
                if not new: continue
                m = re.match(r"^(第[一二三四五六七八九十百零]+章|附录[A-H]|结语)[：:]", new)
                if not m: continue
                pre = m.group(1)
                pat = re.compile(r"(<h3[^>]*>)(" + re.escape(pre) + r"[：:][^<]{2,80}?)(</h3>)")
                def rp(mm):
                    nonlocal t1
                    old = mm.group(2)
                    if old == new or "——" not in old: return mm.group(0)
                    t1 += 1
                    return mm.group(1) + new + mm.group(3)
                html = pat.sub(rp, html)
                # 目录与互引：章号《旧标题》→《新标题》
                old_title = None
                mm = re.search(r'<h3[^>]*>(' + re.escape(pre) + r'[：:]([^<]{2,80}?))</h3>', html)
                if mm: old_title = mm.group(2)
                if old_title and old_title != new:
                    html = html.replace('《' + old_title + '》', '《' + new + '》')
            return html
        raw = t1_sub(raw)
    work = RX_SKIP.sub(keep, raw)
    work = RX_COMMENT.sub(keep, work)

    # 1) 按标签切分：奇数位为标签（保护），偶数位为文本（可编辑）
    toks = RX_TAG.split(work)
    s5_budget = WL["surgery"]["max_questions_per_chapter"]
    out_toks: list[str] = []
    for idx, tok in enumerate(toks):
        if idx % 2 == 1 or not tok:
            out_toks.append(tok)
            continue
        # 文本里可能含实体，逐段保护
        pieces = RX_ENTITY.split(tok)
        # split 会把实体放在奇数位；复原时保持
        rebuilt = []
        for j, piece in enumerate(pieces):
            if j % 2 == 1:
                rebuilt.append(piece)
            else:
                r, s5_budget = transform_text(piece, surgeon, chinese, s5_budget)
                rebuilt.append(r)
        out_toks.append("".join(rebuilt))

    out = "".join(out_toks)
    # 3) 还原保护区
    for i, s in enumerate(stash):
        out = out.replace(f"\x00KEEP{i}\x00", s)

    # 4) 结构安全：标签配平、伪影不增加
    problems = []
    for tag in ("strong", "em", "code", "p", "div", "ul", "ol", "li", "table", "tr", "td", "th", "span", "a", "h3"):
        o = len(re.findall(rf"<{tag}[\s>]", out))
        c = len(re.findall(rf"</{tag}>", out))
        ob = len(re.findall(rf"<{tag}[\s>]", raw))
        cb = len(re.findall(rf"</{tag}>", raw))
        if o != c and (ob == cb):
            problems.append(f"<{tag}> 开合不配平 {o}/{c}")
    out = re.sub(r"([？!！])。", r"\1", out)
    a, b = VL.artifact_counts(raw), VL.artifact_counts(out)
    inc = {k: (v, b[k]) for k, v in a.items() if b[k] > v and k != "多余空格"}
    if inc:
        problems.append(f"伪影增加 {inc}")

    hits = {k: v - hits_before.get(k, 0) for k, v in surgeon.hits.items() if v > hits_before.get(k, 0)}
    if not dry and out != raw and not problems:
        path.write_text(out, encoding="utf-8")
    return {"file": str(path), "changed": out != raw, "hits": hits,
            "t1": t1, "problems": problems}


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--versions", default="v1.9,v1.8")
    args = ap.parse_args()
    report = []
    for v in args.versions.split(","):
        d = ROOT / v.strip()
        if not d.is_dir():
            continue
        for p in sorted(d.glob("*.html")):
            lang = "zh" if p.name == "zh-CN.html" else (
                p.stem if p.stem in ("zh-TW", "yue", "lzh", "ja", "ko", "en", "ru", "it", "pt",
                                     "es", "fr", "de", "ar", "he", "th", "id", "ms", "el") else "zh")
            if lang in ("ja", "lzh"):
                print(f"[SKIP] {v}/{p.name} — 方案 §7.3 特殊语言，保持原样")
                report.append({"file": str(p), "version": v, "changed": False,
                               "hits": {}, "t1": 0, "problems": [], "skip_reason": "方案 §7.3"})
                continue
            r = process_html(p, lang, dry=args.dry_run)
            r["version"] = v
            report.append(r)
            print(f"[{'DRY' if args.dry_run else 'FIX'}] {v}/{p.name} "
                  f"changed={r['changed']} hits={r['hits']} T1={r['t1']} problems={r['problems']}")
    out = ROOT / "state" / "deai_html_report.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"报告：{out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
