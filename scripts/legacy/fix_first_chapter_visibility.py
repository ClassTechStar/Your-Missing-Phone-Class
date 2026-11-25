# -*- coding: utf-8 -*-
"""修复「第一章无法显示」：滚动入场观察器 + 超长章节占位。

根因（两条叠加，2026-11-09 实测）：
1. .content-section 默认 opacity:0，靠 IntersectionObserver 加 .visible；
   观察器用 threshold: 0.05。第一章经多轮扩充已达 26438px，
   5% = 1322px > 视口 860px，永远无法满足 → 整章保持 transparent。
2. .content-section 的 content-visibility:auto + contain-intrinsic-size: auto 800px
   让离屏章节按 800px 占位；scrollIntoView 到第一章时 y=2128（仍在视口外），
   去掉后 y=80。锚点跳转同样会偏。

修复（渐进增强，内容默认可见，动画只作为增强）：
- 去掉整章 content-visibility（保留表格/代码块局部懒渲染）
- CSS 默认 opacity:1；仅当脚本加 html.anim-ready 时才隐藏未进入视口的区块
- threshold: 0.05 → 0；回调同时接受 isIntersecting 或 intersectionRatio>0
- 观察器不可用时全部直接可见
- 2 秒兜底：无论观察器是否触发，强制全部 .visible，绝不白屏

作用范围（21 个文件，替换串均不含本地化注释）：
  v1.9 两个 HTML + source/template/shell.html + 18 个翻译模板；
  v1.8/*.html 由模板经 bookkit build 重建。

用法：
    python scripts/fix_first_chapter_visibility.py            # 干跑
    python scripts/fix_first_chapter_visibility.py --apply    # 写盘
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

R1_OLD = """        .content-section {
            content-visibility: auto;
            contain-intrinsic-size: auto 800px;
        }"""
R1_NEW = """        /* 整章不做 content-visibility:auto：超长章节离屏按 800px 占位，
           会让锚点跳转、scrollIntoView 与入场观察器全部失准。
           表格/代码块的局部懒渲染见下方 P2-2 规则，不受影响。 */"""

R2_OLD = """        .content-section {
            opacity: 0;
            transform: translateY(24px);
            transition: opacity 0.6s cubic-bezier(0.22, 1, 0.36, 1),
                        transform 0.6s cubic-bezier(0.22, 1, 0.36, 1);
        }"""
R2_NEW = """        /* 默认可见：观察器失效、脚本未运行、打印时都不会白屏 */
        .content-section {
            opacity: 1;
            transform: none;
        }
        /* 只有脚本确认可用后，才对尚未进入视口的区块启用入场动画 */
        html.anim-ready .content-section:not(.visible):not(.immediately-visible) {
            opacity: 0;
            transform: translateY(24px);
            transition: opacity 0.6s cubic-bezier(0.22, 1, 0.36, 1),
                        transform 0.6s cubic-bezier(0.22, 1, 0.36, 1);
        }"""

R3_OLD = """            const visibleObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                        visibleObserver.unobserve(entry.target);
                    }
                });
            }, { rootMargin: '0px 0px -40px 0px', threshold: 0.05 });"""
R3_NEW = """            // 渐进增强：只有观察器可用时才启用隐藏态，否则正文保持默认可见
            const supportsIO = 'IntersectionObserver' in window;
            if (supportsIO) html.classList.add('anim-ready');
            const visibleObserver = supportsIO ? new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting || entry.intersectionRatio > 0) {
                        entry.target.classList.add('visible');
                        visibleObserver.unobserve(entry.target);
                    }
                });
            }, { rootMargin: '0px 0px -40px 0px', threshold: 0 }) : null;
            // 阈值必须为 0：超长章节用 0.05 永远达不到，会整章白屏
            // 兜底：观察器若因任何原因未触发，2 秒后强制全部显示
            setTimeout(() => {
                sections.forEach(sec => sec.classList.add('visible'));
            }, 2000);"""

R4_OLD = "                if (rect.top < window.innerHeight) {"
R4_NEW = "                if (!visibleObserver || rect.top < window.innerHeight) {"

PAIRS = [(R1_OLD, R1_NEW), (R2_OLD, R2_NEW), (R3_OLD, R3_NEW), (R4_OLD, R4_NEW)]
MARK = '<!-- v19-first-chapter-visibility-fix -->'


def targets():
    return ([ROOT / 'v1.9' / 'zh-CN.html',
             ROOT / '你缺失的那门手机课V1.9Fixed.html']
            + sorted(ROOT.glob('source/template/shell.html'))
            + sorted(ROOT.glob('source/translations/*/template/shell.html')))


def main():
    do_apply = '--apply' in sys.argv
    ok = True
    for p in targets():
        s = p.read_text(encoding='utf-8')
        rel = p.relative_to(ROOT)
        if MARK in s:
            print(f'  · {rel}: 已修复过，跳过')
            continue
        counts = [s.count(old) for old, _ in PAIRS]
        flag = 'OK  ' if counts == [1, 1, 1, 1] else 'FAIL'
        if flag == 'FAIL':
            ok = False
        print(f'  {flag} {rel}: {counts}')
        if not do_apply or flag == 'FAIL':
            continue
        for old, new in PAIRS:
            s = s.replace(old, new)
        # 用注释标记幂等（插在 </head> 前，不影响渲染）
        s = s.replace('</head>', MARK + '\n</head>', 1)
        p.write_text(s, encoding='utf-8', newline='')
    if not ok:
        print('\n!! 有命中异常，未写盘')
        return 1
    print(f'\n共 {len(targets())} 个文件' + ('（干跑）' if not do_apply else '（已写盘）'))
    if not do_apply:
        return 0
    print('下一步：重建 v1.8 19 语 HTML（bookkit build --lang <L> --out v1.8/<L>.html）')
    return 0


if __name__ == '__main__':
    sys.exit(main())
