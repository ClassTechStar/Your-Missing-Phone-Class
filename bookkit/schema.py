# -*- coding: utf-8 -*-
"""结构化数据 schema 校验与迁移入口（P0-1）。

中央校验模块：book.json（zh/翻译）/ manifest / quiz 题库。
- validate_book(data)      schema_version=1
- validate_quiz(data)      schema_version=1
- manifest 校验仍在 manifest.validate_manifest（schema_version=2），此处做转发包装。

设计：纯标准库、只读校验（返回 problems 列表，不抛异常），
供 bookkit lint 与 scripts/quiz_lint.py 共用。
"""
from pathlib import Path

SCHEMA_BOOK = 1
SCHEMA_MANIFEST = 2
SCHEMA_QUIZ = 1

BOOK_REQUIRED_KEYS = ("version", "lang", "title", "template", "parts", "chapters")
CHAPTER_REQUIRED_KEYS = ("id", "file")
PART_REQUIRED_KEYS = ("id", "file", "nav")
QUIZ_REQUIRED_KEYS = ("lang", "chapters")
QUIZ_CHAPTER_KEYS = ("id", "title", "questions")
QUIZ_QUESTION_KEYS = ("q", "options", "answer")


def validate_book(data: dict, *, label: str = "book.json") -> list:
    """校验 book.json（zh-CN 与翻译版同构）。返回问题列表。"""
    problems = []
    if data.get("schema_version") != SCHEMA_BOOK:
        problems.append(f"{label}: schema_version 期望 {SCHEMA_BOOK}，"
                        f"实际 {data.get('schema_version')!r}")
        return problems
    for key in BOOK_REQUIRED_KEYS:
        if key not in data:
            problems.append(f"{label}: 缺少必填键 {key!r}")
    chapters = data.get("chapters")
    if not isinstance(chapters, list) or not chapters:
        problems.append(f"{label}: chapters 缺失或为空")
        chapters = []
    ids = [c.get("id") for c in chapters if isinstance(c, dict)]
    for i, c in enumerate(chapters):
        if not isinstance(c, dict):
            problems.append(f"{label}: chapters[{i}] 不是对象")
            continue
        for key in CHAPTER_REQUIRED_KEYS:
            if key not in c:
                problems.append(f"{label}: chapters[{i}] ({c.get('id', '?')}) 缺 {key!r}")
        for key in ("part", "after_part"):
            if c.get(key) and c.get(key) not in {p.get("id") for p in data.get("parts", [])}:
                problems.append(f"{label}: chapters[{i}] 的 {key}={c[key]!r} 不在 parts 中")
                break
    dup = sorted({x for x in ids if ids.count(x) > 1})
    if dup:
        problems.append(f"{label}: 章节id重复 {dup}")
    for i, p in enumerate(data.get("parts", [])):
        if isinstance(p, dict):
            for key in PART_REQUIRED_KEYS:
                if key not in p:
                    problems.append(f"{label}: parts[{i}] ({p.get('id', '?')}) 缺 {key!r}")
    return problems


def validate_quiz(data: dict, *, label: str = "quiz") -> list:
    """校验题库 JSON（schema_version=1）。返回问题列表。"""
    problems = []
    if data.get("schemaVersion") != SCHEMA_QUIZ and "schema_version" not in data:
        problems.append(f"{label}: 缺 schemaVersion={SCHEMA_QUIZ}")
        return problems
    for key in QUIZ_REQUIRED_KEYS:
        if key not in data:
            problems.append(f"{label}: 缺少必填键 {key!r}")
    for ci, ch in enumerate(data.get("chapters", [])):
        cid = ch.get("id", f"#{ci}")
        if not isinstance(ch, dict):
            problems.append(f"{label}: chapters[{ci}] 不是对象")
            continue
        for key in QUIZ_CHAPTER_KEYS:
            if key not in ch:
                problems.append(f"{label}: chapters[{ci}] ({cid}) 缺 {key!r}")
        qs = ch.get("questions", [])
        if not qs:
            problems.append(f"{label}: chapters[{ci}] ({cid}) 无题（题量偏好由 gen_quiz 自检提示）")
        for qi, q in enumerate(qs):
            if not isinstance(q, dict):
                problems.append(f"{label}: {cid} 第{qi + 1}题不是对象")
                continue
            for key in QUIZ_QUESTION_KEYS:
                if key not in q:
                    problems.append(f"{label}: {cid} 第{qi + 1}题缺 {key!r}")
            opts = q.get("options")
            ans = q.get("answer")
            if not isinstance(opts, list) or len(opts) < 2:
                problems.append(f"{label}: {cid} 第{qi + 1}题 options 不足 2 项")
            elif not isinstance(ans, int) or not (0 <= ans < len(opts)):
                problems.append(f"{label}: {cid} 第{qi + 1}题 answer 越界：{ans!r}")
    return problems


def validate_book_file(path) -> list:
    """读文件并校验 book.json；解析失败也返回问题列表。"""
    import json
    path = Path(path)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        return [f"{path.name}: JSON 解析失败 {e}"]
    return validate_book(data, label=str(path))


def validate_quiz_file(path) -> list:
    import json
    path = Path(path)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        return [f"{path.name}: JSON 解析失败 {e}"]
    return validate_quiz(data, label=str(path))


def list_translation_book_files(root: Path) -> list:
    src = root / "source" / "translations"
    if not src.is_dir():
        return []
    return sorted(src.glob("*/book.json"))


def migrate_book(data: dict) -> dict:
    """book.json 迁移入口。当前 schema=1 为初始版本，无历史版本需迁移；
    未来字段变更时在此按旧版本补齐缺省键并提升 schema_version。"""
    return data


def migrate_quiz(data: dict) -> dict:
    """题库迁移入口：补齐 schema_version（旧题库缺失时的最小升级）。"""
    if "schemaVersion" not in data:
        data["schemaVersion"] = SCHEMA_QUIZ
    return data
