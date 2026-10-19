"""检查结论的数据模型：统一的 Issue 结构贯穿 lint 与 claims。"""

from dataclasses import dataclass

OFF = "off"
INFO = "info"
WARN = "warn"
ERROR = "error"

RANK = {OFF: 0, INFO: 1, WARN: 2, ERROR: 3}


@dataclass(frozen=True)
class Issue:
    check: str          # 分类，如 structure / anchors / title_version / claims
    severity: str       # error | warn | info
    message: str
    file: str = ""
    line: int = 0
    detail: str = ""

    def render(self) -> str:
        loc = f"{self.file}:{self.line}" if self.line else self.file
        head = f"[{self.severity.upper():<5}] {self.check:<13} {loc}"
        tail = f"  — {self.detail}" if self.detail else ""
        return f"{head}  {self.message}{tail}"

    def to_dict(self) -> dict:
        return {
            "check": self.check, "severity": self.severity, "message": self.message,
            "file": self.file, "line": self.line, "detail": self.detail,
        }
