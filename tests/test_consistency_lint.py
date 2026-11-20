# -*- coding: utf-8 -*-
"""consistency_lint 的边界用例：中文数字换算、篇数口径、仓库集成全绿。"""
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location(
    'consistency_lint', ROOT / 'scripts' / 'consistency_lint.py')
cl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cl)


def test_cn2num():
    assert cl.cn2num('十') == 10
    assert cl.cn2num('十一') == 11
    assert cl.cn2num('十五') == 15
    assert cl.cn2num('二十') == 20
    assert cl.cn2num('九十九') == 99
    assert cl.cn2num('15') == 15


def test_count_pian_excludes_special_topic_and_appendix():
    book = {'parts': [
        {'nav': '一、基础篇（第0-7章）'},
        {'nav': '儿童与手机专题（第35-36章）'},
        {'nav': '十五、竖屏短剧入门篇（第101-105章）'},
        {'nav': '十六、附录'},
    ]}
    assert cl.count_pian(book) == 2


def test_count_pian_v19_is_fifteen():
    """「15 篇」口径的回归锚：专题与附录都不计为篇。"""
    book = json.loads((ROOT / 'source' / 'v1.9' / 'book.json').read_text(encoding='utf-8'))
    assert cl.count_pian(book) == 15


def test_consistency_lint_green_on_repo():
    """端到端：仓库当前状态必须全部一致（CI 门禁的本体）。"""
    r = subprocess.run([sys.executable, str(ROOT / 'scripts' / 'consistency_lint.py')],
                       capture_output=True, text=True, cwd=str(ROOT))
    assert r.returncode == 0, r.stdout + r.stderr
