#!/usr/bin/env python3
"""build_path_db.py — 生成 path_db.json（方案 §5.1 的"单一真源"）。

路径库不是手抄的表，是**从源稿里生成**的：扫出正文里的操作路径，
归到它所在的小节（= 任务），去重，标注平台、版本区间与核对状态。
改了正文重跑一次，库就跟着变。

一条路径的 status：
  confirmed     —— 路径由官方文档/多版本一致的固定入口构成，读者照做大概率对得上
  needs-confirm —— 随系统版本改动明显（菜单层级改名、入口位置调整），需在大版本后复查

关于日期与署名（诚实优先）：
  date          —— 内容核对到的年月（本书 v1.9 出版期：2026-11）
  verified_by   —— 谁核对的。本库由脚本从书稿生成、由作者对账，
                   所以写 "book-v1.9"（即以书稿自身为准），
                   **不写"实测"**——本书正文没有做过逐台设备的实机复测，
                   这一点在 meta.disclosure 里写明，读者能看到。

用法：
  py -3 scripts/build_path_db.py            # 生成 path_db.json
  py -3 scripts/build_path_db.py --dry-run  # 只统计不写
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS = ROOT / "source" / "v1.9" / "chapters"
DB_PATH = ROOT / "path_db.json"

RX_BRACKET = re.compile(r"【([^】]{1,12})】(?:\s*[→>➔]\s*【([^】]{1,12})】)+")
# 通用箭头链：步骤可以是【方括号】或 2–10 字中文
RX_CHAIN = re.compile(
    r"((?:【[^】]{1,14}】|[一-鿿][一-鿿A-Za-z0-9 ]{0,9})"
    r"(?:\s*(?:→|➔|->)\s*(?:【[^】]{1,14}】|[一-鿿][一-鿿A-Za-z0-9 ]{0,9})){1,6})"
)
# UI 入口词：命中其一才认为是操作路径
UI_WORDS = (
    "设置", "存储", "电池", "相册", "通用", "隐私", "关于", "账号", "显示", "声音",
    "网络", "蓝牙", "相机", "壁纸", "通知", "系统", "开发者", "应用", "文件", "时钟",
    "日历", "天气", "健康", "钱包", "备份", "还原", "权限", "无障碍", "辅助功能",
    "电池使用情况", "最近删除", "图库", "相册图库", "骚扰", "拦截", "流量", "密码",
    "指纹", "面容", "共享", "打印", "投影", "投屏", "录屏", "截屏", "定位", "麦克风",
    "通讯录", "短信", "电话", "邮箱", "浏览器", "下载", "邮件", "助理", "小艺", "小艺",
)
RX_VERSION = re.compile(
    r"(iOS\s*1[5-9](?:\.\d+)?|iOS\s*2\d|HarmonyOS\s*\d+(?:\.\d+)*|鸿蒙\s*\d+(?:\.\d+)*|"
    r"Android\s*1[0-9](?:\.\d+)?|安卓\s*1[0-9]|MIUI\s*1[0-9]|ColorOS\s*\d+(?:\.\d+)*)"
)
RX_SECTION = re.compile(r"^####\s+(.+)$", re.M)

# 真实入口：路径的第一级必须是其中之一
PATH_ROOTS = {
    "设置", "系统设置", "手机设置", "我的", "我", "微信", "QQ", "QQ邮箱", "相册", "图库",
    "照片", "相机", "通知", "电脑", "平板", "车辆", "车机", "手表", "蓝牙", "电话",
    "信息", "时钟", "日历", "天气", "邮件", "浏览器", "文件", "文件管理", "音乐",
    "钱包", "健康", "家庭", "查找", "定位", "备份", "无障碍", "辅助功能", "应用管理",
    "应用列表", "应用商店", "设置中心", "系统", "桌面", "屏幕", "最近删除",
    "短信", "通话", "录音", "备忘录", "计算器", "翻译", "下载", "开发者选项",
    "隐私与安全", "安全", "账号", "云服务", "语言与输入法", "电池", "存储",
}


def split_chain(raw: str) -> list[str]:
    parts = re.split(r"\s*(?:→|➔|->)\s*", raw.strip())
    out = []
    for x in parts:
        x = x.strip().strip("【】").strip()
        if x:
            out.append(x)
    return out


def is_ui_path(chain: list[str]) -> bool:
    """路径的**第一级**必须是真实入口，才算操作路径。

    只看关键词会误收概念链（"采集→聚合→应用→决策"、"通讯工具→互联网入口→生活平台"），
    路径必须从某个真入口起头。
    """
    first = chain[0].strip()
    return first in PATH_ROOTS

# 平台词
PLATFORM_WORDS = {
    "ios": ("iPhone", "iOS", "iPad", "苹果", "Apple Watch"),
    "harmony": ("鸿蒙", "HarmonyOS", "华为"),
    "android": ("安卓", "Android", "小米", "MIUI", "ColorOS", "OPPO", "vivo", "三星", "一加", "realme"),
}
# 版本敏感词：命中就标 needs-confirm
SENSITIVE = ("开发者", "实验", "Beta", "beta", "测试版", "内测", "新版本", "预览版", "NEXT")

DEFAULT_SCOPE = "iOS 18.x / HarmonyOS 5.x–6.x / Android 15–16"


def platforms_in(text: str) -> list[str]:
    low = text.lower()
    hits = [k for k, ws in PLATFORM_WORDS.items() if any(w.lower() in low for w in ws)]
    return hits or ["all"]


def main() -> int:
    ap = argparse.ArgumentParser(description="生成 path_db.json")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--out", default=str(DB_PATH))
    args = ap.parse_args()

    entries: list[dict] = []
    seq = 0
    stats = defaultdict(int)

    for p in sorted(CHAPTERS.glob("*.md")):
        text = p.read_text(encoding="utf-8")
        body = re.sub(r"```.*?```", "", text, flags=re.S)
        body = re.sub(r"`[^`\n]{1,120}`", "", body)

        # 小节位置表：用来给路径归任务
        sections = [(m.start(), m.group(1).strip()) for m in RX_SECTION.finditer(text)]

        def task_at(pos: int) -> str:
            name = ""
            for start, title in sections:
                if start <= pos:
                    name = title
                else:
                    break
            # 去掉小节标题里的编号前缀
            return re.sub(r"^[一二三四五六七八九十百零\d]+[、.．]\s*", "", name) or "（章内通用）"

        # 章节级版本
        versions = sorted(set(RX_VERSION.findall(body)))
        scope = " / ".join(versions[:4]) if versions else DEFAULT_SCOPE

        seen: set[tuple[str, tuple[str, ...]]] = set()
        for m in RX_CHAIN.finditer(body):
            chain = tuple(split_chain(m.group(1)))
            if len(chain) < 2 or len(chain) > 7:
                continue
            if not is_ui_path(list(chain)):
                continue
            task = task_at(m.start())
            key = (task, chain)
            if key in seen:
                continue
            seen.add(key)
            seq += 1
            plat = platforms_in(m.group(0) + " " + body[max(0, m.start() - 400):m.start() + 400])
            status = "needs-confirm" if any(s in m.group(0) for s in SENSITIVE) else "confirmed"
            stats[status] += 1
            entries.append({
                "id": f"p{seq:04d}",
                "file": p.name,
                "task": task,
                "path": list(chain),
                "platform": plat,
                "version_scope": scope,
                "status": status,
                "date": "2026-11",
                "verified_by": "book-v1.9",
                "note": "",
            })

    db = {
        "meta": {
            "purpose": "全书操作路径的单一真源（方案 §5.1）。正文里的路径由本库登记，"
                       "大版本更新后重跑 scripts/path_check.py 巡检过期条目。",
            "generated_by": "scripts/build_path_db.py（从 source/v1.9/chapters 生成，请勿手改）",
            "checked_at": "2026-11",
            "default_version_scope": DEFAULT_SCOPE,
            "status_legend": {
                "confirmed": "路径入口稳定，读者照做大概率对得上。",
                "needs-confirm": "随系统版本改名或挪位，需在大版本后复查。",
            },
            "disclosure": "本库由脚本从书稿生成，作者已对账，但**全书未做逐台设备的实机复测**。"
                          "因此条目不写\"实测\"，只声明核对基准版本。读者遇到对不上的路径，"
                          "请走勘误页 errata.html 反馈，改的是本库，不是散落在正文里的某句话。",
            "field_notes": {
                "task": "该路径所属的小节（正文里那一节在讲什么事）",
                "platform": "适用平台；all 表示三平台通用路径",
                "version_scope": "该章正文提到的系统版本；未提及则用 default_version_scope",
                "date": "内容核对到的年月",
                "verified_by": "book-v1.9 = 以书稿自身为准，由作者对账，非逐设备实测",
            },
            "counts": {"entries": len(entries), "confirmed": stats["confirmed"],
                       "needs-confirm": stats["needs-confirm"]},
        },
        "entries": entries,
    }

    if args.dry_run:
        print(f"[i] 将生成 {len(entries)} 条（confirmed {stats['confirmed']} / "
              f"needs-confirm {stats['needs-confirm']}）")
        return 0

    outp = Path(args.out)
    outp.write_text(json.dumps(db, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[+] path_db.json：{len(entries)} 条"
          f"（confirmed {stats['confirmed']} / needs-confirm {stats['needs-confirm']}）")
    print(f"[+] 输出：{outp}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
