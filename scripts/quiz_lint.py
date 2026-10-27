#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""题库/结构数据 lint（P0-2）：quiz 包清单 + schema 校验，纯标准库。

- quiz/manifest.json：题库包清单（版本/语言清单与实际 JSON 对齐）
- quiz/*.json：schemaVersion 与题目结构（bookkit/schema.validate_quiz）
- source/book.json + source/translations/*/book.json：schema_version
失败时写入 quiz/_failures.json（CI artifact 可展示），退出码 1。
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from bookkit import schema as S  # noqa: E402

QUIZ_DIR = ROOT / 'quiz'


def main() -> int:
    problems = []

    # ---- 包清单 ----
    mf_path = QUIZ_DIR / 'manifest.json'
    mf = {}
    if not mf_path.is_file():
        problems.append('quiz/manifest.json 缺失（题库包清单）')
    else:
        try:
            mf = json.loads(mf_path.read_text(encoding='utf-8'))
            for key in ('name', 'version', 'languages'):
                if key not in mf:
                    problems.append(f'manifest 缺 {key!r}')
            langs = mf.get('languages') or []
            if isinstance(langs, str):
                langs = [langs]
            actual = sorted(f.stem for f in QUIZ_DIR.glob('*.json') if f.name != 'manifest.json')
            missing = [l for l in langs if l not in actual]
            extra = [a for a in actual if a not in langs]
            if missing:
                problems.append(f'manifest 声明了不存在的语言题库：{missing}')
            if extra:
                problems.append(f'存在未在 manifest 声明的题库：{extra}')
        except Exception as e:
            problems.append(f'manifest 解析失败：{e}')

    # ---- 各语言题库 schema ----
    for f in sorted(QUIZ_DIR.glob('*.json')):
        if f.name == 'manifest.json':
            continue
        problems.extend(S.validate_quiz_file(f))

    # ---- 失败留痕 ----
    out = ROOT / 'quiz' / '_failures.json'
    if problems:
        out.write_text(json.dumps({'problems': problems}, ensure_ascii=False, indent=1),
                       encoding='utf-8', newline='\n')
        print(f'✗ quiz lint：{len(problems)} 条问题')
        for pr in problems:
            print('   -', pr)
        return 1
    if out.exists():
        out.unlink()
    print('✓ quiz lint：全部通过')
    return 0


if __name__ == '__main__':
    sys.exit(main())
