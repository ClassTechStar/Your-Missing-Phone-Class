# -*- coding: utf-8 -*-
"""让 tests/ 无论从哪个目录启动都能 import bookkit。"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
