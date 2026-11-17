"""bookkit 命令行入口。

子命令：
  extract  成品 HTML → source/（源稿反解，一次性引导）
  build    source/ → 单文件 HTML（可 --verify 与已发布成品比对）
  lint     全版本结构/锚点/目录/版本串/lang/NUL/残留字检查
  check    README/index.html 宣称值校验（可加 --index 校验 AUTOGEN 是否最新）
  index    按 manifest 生成 index.html 的语言卡片块与统计区
  i18n     翻译覆盖率报告
  release  发布清单（SHA256SUMS + 每语言包名）
"""

import argparse
import json
import sys
from pathlib import Path

from . import __version__
from .claims import check_claims
from .lint import run_lint
from .manifest import ManifestError, load_manifest
from .model import ERROR, RANK, WARN


def _prepare_stdout():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def _report(issues, header: str, as_json: bool) -> None:
    if as_json:
        print(json.dumps({"header": header,
                          "issues": [i.to_dict() for i in issues]},
                         ensure_ascii=False, indent=2))
        return
    errors = [i for i in issues if i.severity == ERROR]
    warns = [i for i in issues if i.severity == WARN]
    infos = [i for i in issues if i.severity not in (ERROR, WARN)]
    print(f"== {header} ==")
    for group, rows in (("ERROR", errors), ("WARN", warns), ("INFO", infos)):
        if not rows:
            continue
        print(f"-- {group} ({len(rows)}) --")
        for i in rows:
            print("  " + i.render())
    print(f"-- 汇总：{len(errors)} error / {len(warns)} warn / {len(infos)} info")


def _exit_code(issues, fail_on: str) -> int:
    threshold = RANK[ERROR] if fail_on == "error" else RANK[WARN]
    return 1 if any(RANK[i.severity] >= threshold for i in issues) else 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="bookkit", description="本仓库内容一致性工具链")
    p.add_argument("--version", action="version", version=f"bookkit {__version__}")

    sub = p.add_subparsers(dest="cmd", required=True)

    def common(sp, fail_default="error"):
        sp.add_argument("--root", type=Path, default=None,
                        help="仓库根目录（默认自动向上查找 manifest/languages.json）")
        sp.add_argument("--json", action="store_true", help="以 JSON 输出结论")
        sp.add_argument("--fail-on", choices=["error", "warn", "never"], default=fail_default,
                        help="达到该等级即以非零码退出（默认 error）")
        return sp

    lt = common(sub.add_parser("lint", help="结构/锚点/目录/版本串/lang/NUL/残留字/覆盖率 检查"))
    lt.add_argument("--all-versions", action="store_true", help="检查全部版本（默认仅最新版）")
    lt.add_argument("--version-dir", action="append", default=[],
                    metavar="V", help="只检查指定版本目录（可重复）")

    ck = common(sub.add_parser("check", help="校验 README/index.html 的宣称值与真实内容是否一致"))
    ck.add_argument("--claims", action="store_true", help="（默认行为，显式声明用）")
    ck.add_argument("--index", action="store_true", help="同时校验 index.html 的 AUTOGEN 是否最新")

    ix = common(sub.add_parser("index", help="按 manifest 重新生成 index.html 卡片块与统计区"))
    ix.add_argument("--check", action="store_true", help="只检查是否需要重新生成，不写盘")

    bd = common(sub.add_parser("build", help="从 source/ 生成单文件 HTML"))
    bd.add_argument("--lang", default="zh-CN", help="目标语言（默认 zh-CN）")
    bd.add_argument("--out", type=Path, default=None,
                    help="输出路径（默认 dist/<version>/<lang>.html）")
    bd.add_argument("--book", type=Path, default=None, help="book.json 路径（默认 source/book.json）")
    bd.add_argument("--verify", action="store_true",
                    help="与已发布成品做逐章等价性比对并打印结论")

    sp_ = common(sub.add_parser("split", help="分章化构建：每章一页 + 书首页 + sitemap/JSON-LD"))
    sp_.add_argument("--lang", default="zh-CN", help="目标语言（默认 zh-CN）")
    sp_.add_argument("--book", type=Path, default=None, help="book.json 路径（默认 source/book.json）")
    sp_.add_argument("--out", type=Path, default=None, help="输出目录（默认 dist/site）")
    sp_.add_argument("--strict-budget", action="store_true",
                     help="超出页级性能预算（300KB / 5000 标签）时以非零码退出")

    ex = common(sub.add_parser("extract", help="成品 HTML → source/ 源稿反解"))
    ex.add_argument("--version", default=None, help="源版本目录（默认取 manifest 的最新版本）")
    ex.add_argument("--lang", default="zh-CN", help="源语言（默认 zh-CN）")
    ex.add_argument("--out", type=Path, default=None, help="源稿根目录（默认 source/）")
    ex.add_argument("--dry-run", action="store_true", help="只解析不写盘")
    ex.add_argument("--no-strict", action="store_true", help="跳过字节级往返断言（翻译反解用；提取按树位置，不受序列化差异影响）")

    i18 = common(sub.add_parser("i18n", help="翻译覆盖率报告"), fail_default="never")
    i18.add_argument("--report", type=Path, default=None, help="报告输出路径（Markdown）")

    tm = common(sub.add_parser("tm", help="翻译记忆库：build（构建）/ report（增量待译导出）/ import（译文合并）"))
    tm.add_argument("action", choices=["build", "report", "import"])
    tm.add_argument("--lang", default="ja", help="report/import 的目标语言（默认 ja）")
    tm.add_argument("--book", type=Path, default=None,
                    help="report 的源稿 book.json（默认 source/book.json；传 source/v1.9/book.json 查 v1.9）")
    tm.add_argument("--file", type=Path, default=None, help="import 的译文 JSON（{hash: 译文段}）")
    tm.add_argument("--out", type=Path, default=None, help="report 的待译段落输出目录（默认 dist/i18n）")

    qk = common(sub.add_parser("quick", help="派生《给爸妈的 20 分钟速读版》（速读层合集）"))
    qk.add_argument("--book", type=Path, default=None, help="book.json 路径（默认 source/book.json）")
    qk.add_argument("--out", type=Path, default=None, help="输出 HTML 路径（默认 dist/quick-read-<version>.html）")

    tx = common(sub.add_parser("latex", help="生成 LaTeX 书稿（HTML → LaTeX，供 XeLaTeX 编译）"))
    tx.add_argument("--lang", default="zh-CN", help="源语言（默认 zh-CN）")
    tx.add_argument("--tex-version", dest="tex_version", default=None,
                    help="源版本（默认 manifest 的最新版本）")
    tx.add_argument("--out", type=Path, default=None, help="输出目录（默认 latex/）")

    rl = common(sub.add_parser("release", help="生成发布清单与校验和"))
    rl.add_argument("--release-version", dest="rel_version", default=None,
                    help="发布版本（默认 manifest 的最新版本）")
    rl.add_argument("--out", type=Path, default=None, help="输出目录（默认 dist/release/）")

    return p


def main(argv=None) -> int:
    _prepare_stdout()
    args = build_parser().parse_args(argv)

    try:
        mf = load_manifest(args.root)
    except ManifestError as e:
        print(f"清单错误：{e}", file=sys.stderr)
        return 2

    issues = []

    if args.cmd == "lint":
        if args.version_dir:
            versions = args.version_dir
        elif args.all_versions:
            versions = list(mf.versions.keys())
        else:
            versions = [mf.latest_version()]
        issues = run_lint(mf.root, mf, versions)
        _report(issues, f"lint {'/'.join(versions)}", args.json)

    elif args.cmd == "check":
        issues = check_claims(mf.root, mf)
        if args.index:
            from .index import update_index
            issues += update_index(mf, check=True)
        _report(issues, "check", args.json)

    elif args.cmd == "index":
        from .index import update_index
        issues = update_index(mf, check=args.check)
        _report(issues, "index" + (" --check" if args.check else ""), args.json)

    elif args.cmd == "build":
        from . import build as B
        if args.verify:
            result = B.verify(mf.root, args.lang, args.book)
            ok = (result['ids_equal'] and result['toc_equal'] and result['text_equal']
                  and result['chapters_struct_identical'] == result['id_count'][0])
            if args.json:
                print(json.dumps(result, ensure_ascii=False, indent=2))
            else:
                print(f"== build --verify ({result['version'] if 'version' in result else args.lang}) ==")
                print(f"  区块 id 一致：{result['ids_equal']} {result['id_count']}")
                print(f"  目录一致：{result['toc_equal']} {result['toc_count']}")
                print(f"  可见文本一致：{result['text_equal']} {result['text_len']}")
                print(f"  逐章结构一致：{result['chapters_struct_identical']}/{result['id_count'][0]}")
                if result['struct_diff']:
                    print(f"  结构差异章节：{result['struct_diff']}")
                print("  结论：" + ("PASS（构建产物与已发布成品等价）" if ok else "FAIL"))
            return 0 if ok else 1
        out = args.out or (mf.root / 'dist' / mf.latest_version() / f'{args.lang}.html')
        result = B.build(mf.root, args.lang, out, args.book)
        if args.json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print(f"build {result['version']}/{args.lang}: {result['bytes']} 字节，"
                  f"{result['chapters']} 章，{result['toc_entries']} 个目录条目 → {result['out']}")
        return 0

    elif args.cmd == "split":
        from . import split as S
        result = S.split(mf.root, args.lang, args.book, args.out)
        over = result['over_budget']
        if args.json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print(f"split {result['version']}/{result['lang']}: {result['pages']} 页 → {result['out']}")
            print(f"  页级预算：{result['budget']['max_html_kb']}KB / "
                  f"{result['budget']['max_dom_tags']} 标签")
            for name, kb, tags in over:
                print(f"  !! 超预算 {name}: {kb}KB / {tags} 标签")
            print("  结论：" + ("PASS" if not over else f"FAIL（{len(over)} 页超预算）"))
        if args.strict_budget and over:
            return 1
        return 0

    elif args.cmd == "extract":
        from .extract import extract
        version = args.version or mf.latest_version()
        result = extract(mf.root, version, args.lang, args.out, args.dry_run,
                          strict=not args.no_strict)
        if args.json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print(f"extract {version}/{args.lang}: {result['chapters']} 章 / {result['parts']} 篇，"
                  f"骨架 {result['shell_bytes']} 字节"
                  + ("（dry-run，未写盘）" if args.dry_run else " → source/"))
        return 0

    elif args.cmd == "i18n":
        from . import i18n as I
        text = I.report(mf, args.report)
        if args.json:
            print(json.dumps(I.sync_status(mf), ensure_ascii=False, indent=2))
        else:
            print(text)
            if args.report:
                print(f"（报告已写入 {args.report}）")
        issues = I.issues(mf)
        if issues:
            print(f"-- 缺章告警：{len(issues)} 条（详见报告）")

    elif args.cmd == "quick":
        from . import quick as Q
        result = Q.build_quick(mf.root, args.book, args.out)
        if args.json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print(f"quick {result['version']}: {result['chapters']} 章速读层 → {result['out']}"
                  f"（{result['bytes'] // 1024}KB）")
            if result['missing']:
                print(f"  缺速读层：{result['missing'][:8]}")
        return 0

    elif args.cmd == "tm":
        from . import tm as TM
        if args.action == "build":
            result = TM.build_tm(mf.root)
            if args.json:
                print(json.dumps(result, ensure_ascii=False, indent=2))
            else:
                for lang, st in result.items():
                    print(f"tm build {lang}: {st['segments']} 段"
                          + (f"（同源冲突 {st['conflicts']}）" if st['conflicts'] else ""))
                print(f"→ manifest/tm/*.json（{len(result)} 个语言）")
        elif args.action == "report":
            book = args.book or (mf.root / 'source' / 'book.json')
            result = TM.report(mf.root, book, args.lang, args.out)
            if args.json:
                print(json.dumps(result, ensure_ascii=False, indent=2))
            else:
                print(f"tm report {args.lang}: 共 {result['total']} 段，"
                      f"TM 复用 {result['tm_hits']}（{result['coverage']}%），"
                      f"待译 {result['todo']} → {result['out']}")
        else:
            if not args.file:
                print("import 需要 --file 译文 JSON", file=sys.stderr)
                return 2
            result = TM.import_tm(mf.root, args.lang, args.file)
            if args.json:
                print(json.dumps(result, ensure_ascii=False, indent=2))
            else:
                print(f"tm import {args.lang}: 合并 {result['imported']} 段"
                      f"（新增 {result['new']}），TM 现有 {result['total']} 段")
        return 0

    elif args.cmd == "latex":
        from .latex import build as latex_build
        out = args.out or (mf.root / 'latex')
        version = args.tex_version or mf.latest_version()
        result = latex_build(mf.root, out, args.lang, version)
        if args.json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print(f"latex {version}/{args.lang}: {result['chapters']} 章，"
                  f"{len(result['figures'])} 张图 → {result['out']}")
            print("  编译：cd latex && xelatex main.tex（需跑两遍以生成目录）")
        return 0

    elif args.cmd == "release":
        from .release import build_release
        version = args.rel_version or mf.latest_version()
        manifest = build_release(mf.root, mf, version, args.out)
        if args.json:
            print(json.dumps(manifest, ensure_ascii=False, indent=2))
        else:
            out = args.out or (mf.root / 'dist' / 'release')
            print(f"release {version}: {manifest['count']} 个语言包 → {out}")
            print(f"  清单 release-{version}.json / 校验和 SHA256SUMS-{version}.txt")
        return 0

    if args.fail_on == "never":
        return 0
    return _exit_code(issues, args.fail_on)
