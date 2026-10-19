"""manifest 读取与版本策略：语言元数据、各版本检查等级、发布文件发现。"""

import json
from dataclasses import dataclass
from pathlib import Path

from .model import ERROR, OFF, WARN

MANIFEST_REL = Path("manifest") / "languages.json"


class ManifestError(RuntimeError):
    pass


@dataclass
class Manifest:
    root: Path
    data: dict

    # ---- 语言 ----
    @property
    def languages(self) -> dict:
        return self.data.get("languages", {})

    def lang_meta(self, code: str) -> dict:
        return self.languages.get(code, {})

    def cjk_allowance(self, code: str) -> int:
        return int(self.data.get("cjk_allowance", {}).get(code, 0))

    # ---- 版本 ----
    @property
    def versions(self) -> dict:
        return self.data.get("versions", {})

    @property
    def default_version(self) -> str:
        return self.data.get("default_version", "")

    def version_spec(self, version: str) -> dict:
        return self.versions.get(version, {})

    def check_level(self, version: str, check: str) -> str:
        """返回该版本下某个检查的等级：error / warn / off。"""
        spec = self.version_spec(version)
        checks = spec.get("checks")
        if not checks:
            return OFF
        return checks.get(check, OFF)

    def expect_sections(self, version: str):
        return self.version_spec(version).get("expect_sections")

    def baseline_lang(self, version: str) -> str:
        return self.version_spec(version).get("baseline", "zh-CN")

    # ---- 发布内容发现 ----
    def version_dir(self, version: str) -> Path:
        return self.root / version

    def html_files(self, version: str) -> list:
        """按语言优先级的顺序返回该版本的 (语言代码, 路径) 列表。"""
        d = self.version_dir(version)
        if not d.is_dir():
            return []
        found = {}
        for f in sorted(d.glob("*.html")):
            code = f.stem
            if code in self.languages:
                found[code] = f
        return sorted(found.items(), key=lambda kv: self.lang_meta(kv[0]).get("priority", 999))

    def language_codes(self, version: str) -> list:
        return [c for c, _ in self.html_files(version)]

    def latest_version(self) -> str:
        """默认版本若存在则用它，否则取版本号最大的目录。"""
        dv = self.default_version
        if dv and self.version_dir(dv).is_dir():
            return dv
        cand = [v for v in self.versions if self.version_dir(v).is_dir()]
        if not cand:
            raise ManifestError("找不到任何版本目录")
        return max(cand, key=lambda v: [int(x) for x in v.lstrip("v").split(".")])


def find_root(start: Path = None) -> Path:
    """从 start 起向上查找含 manifest/languages.json 的仓库根。"""
    cur = (start or Path.cwd()).resolve()
    for p in [cur, *cur.parents]:
        if (p / MANIFEST_REL).is_file():
            return p
    raise ManifestError(f"未找到 {MANIFEST_REL}（从 {cur} 向上查找）")


def load_manifest(root: Path = None) -> Manifest:
    root = Path(root) if root else find_root()
    path = root / MANIFEST_REL
    if not path.is_file():
        raise ManifestError(f"清单不存在：{path}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise ManifestError(f"清单 JSON 解析失败：{e}") from e
    problems = validate_manifest(data)
    if problems:
        raise ManifestError("清单校验失败：" + "; ".join(problems))
    return Manifest(root=root, data=data)


def validate_manifest(data: dict) -> list:
    """清单自身的结构性校验。"""
    problems = []
    if data.get("schema_version") not in (2,):
        problems.append(f"schema_version 期望 2，实际 {data.get('schema_version')!r}")
    langs = data.get("languages")
    if not isinstance(langs, dict) or not langs:
        problems.append("languages 缺失或为空")
    else:
        for code, meta in langs.items():
            if not isinstance(meta, dict):
                problems.append(f"languages.{code} 必须是对象")
                continue
            if not meta.get("html_lang"):
                problems.append(f"languages.{code} 缺少 html_lang")
            if meta.get("dir") not in ("ltr", "rtl"):
                problems.append(f"languages.{code}.dir 必须是 ltr/rtl")
    versions = data.get("versions")
    if not isinstance(versions, dict) or not versions:
        problems.append("versions 缺失或为空")
    else:
        allowed = {ERROR, WARN, OFF}
        for ver, spec in versions.items():
            checks = (spec or {}).get("checks") or {}
            for name, lvl in checks.items():
                if lvl not in allowed:
                    problems.append(f"versions.{ver}.checks.{name} 非法等级 {lvl!r}")
    return problems
