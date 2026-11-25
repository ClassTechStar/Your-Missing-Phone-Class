#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复全站「长内容被裁切 / 离屏占位失真」的 CSS 缺陷（2026-11-07）。

用户截图：第一章「一、手机硬件"五脏六腑"：深度解析」内文字行重叠、显示半截。

根因 1（直接致因）
    .collapsible-body { max-height: 5000px; overflow: hidden; }
    折叠框 JS 把「内容 > 800 字」的 h4 小节包成 .collapsible-body。
    v1.9 第一章新增 SoC/NPU/ISP 后，该折叠区实测 8596px，
    被硬裁到 5000px，尾部内容（含「多摄同步配准与计算光学」）显示异常。
    修法：展开态不限高、不裁切；仅折叠态收起并隐藏溢出。

根因 2（同源隐患，历史锚点漂移的同一规则）
    .content-section { content-visibility: auto; contain-intrinsic-size: 0 800px; }
    120 个区块全用固定 800px 占位，其中 57 个实际 > 3000px（第一章 9462px），
    滚动/锚点定位会跳。修法：改用 `auto 800px`，让浏览器记住真实尺寸，
    保留懒渲染性能。

作用范围（活跃文件，dist/ 与 scripts/_v19work/ 是未跟踪归档，不动）：
    - source/template/shell.html + source/translations/*/template/shell.html  (19)
    - v1.9/zh-CN.html 与 你缺失的那门手机课V1.9Fixed.html                  (2)
    - v1.8/*.html 由模板经 bookkit build 重建，不直接改

用法：
    python scripts/fix_collapsible_clip.py            # 干跑
    python scripts/fix_collapsible_clip.py --apply    # 写盘
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

OLD_BODY = '''        .collapsible-body {
            max-height: 5000px;
            overflow: hidden;
            transition: max-height 0.4s ease, opacity 0.3s ease;
            opacity: 1;
        }
        .collapsible-body.collapsed {
            max-height: 0;
            opacity: 0;
        }'''

NEW_BODY = '''        .collapsible-body {
            max-height: none;
            overflow: visible;
            transition: opacity 0.3s ease;
            opacity: 1;
        }
        .collapsible-body.collapsed {
            max-height: 0;
            overflow: hidden;
            opacity: 0;
        }'''

OLD_INTRINSIC = '            contain-intrinsic-size: 0 800px;'
NEW_INTRINSIC = '            contain-intrinsic-size: auto 800px;'


def targets():
    files = sorted(ROOT.glob('source/template/shell.html'))
    files += sorted(ROOT.glob('source/translations/*/template/shell.html'))
    files += [ROOT / 'v1.9' / 'zh-CN.html',
              ROOT / '你缺失的那门手机课V1.9Fixed.html']
    return files


def main():
    do_apply = '--apply' in sys.argv
    ok = True
    plan = []
    for p in targets():
        if not p.is_file():
            print(f'  !! 缺失 {p.relative_to(ROOT)}')
            ok = False
            continue
        s = p.read_text(encoding='utf-8')
        n1, n2 = s.count(OLD_BODY), s.count(OLD_INTRINSIC)
        flag = 'OK  ' if (n1 == 1 and n2 == 1) else 'FAIL'
        if flag == 'FAIL':
            ok = False
        print(f'  {flag} {p.relative_to(ROOT)}: body={n1} intrinsic={n2}')
        plan.append((p, s))
    if not ok:
        print('\n!! 命中数不符，未写盘')
        return 1
    print(f'\n共 {len(plan)} 个文件待修' + ('（干跑）' if not do_apply else ''))
    if not do_apply:
        return 0
    for p, s in plan:
        s = s.replace(OLD_BODY, NEW_BODY).replace(OLD_INTRINSIC, NEW_INTRINSIC)
        p.write_text(s, encoding='utf-8', newline='')
    print('已写盘。下一步：重建 v1.8 19 语 HTML（bookkit build --lang <L> --out v1.8/<L>.html）')
    return 0


if __name__ == '__main__':
    sys.exit(main())
