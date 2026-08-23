#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复 v1.7/zh-CN.html 的两处一致性缺陷:
  1. 侧边栏 5 个 #di-er-shi-zhang 断链 → 改为 #di-er-shi-zhang-jinjie
  2. 侧边栏 1 个 #di-shi-yi-zhang-fu 断链 → 改为 #di-shi-yi-zhang-advanced
  3. 在第 36 章后追加 5 个最小占位章节 (37-41)，保持文档风格与样式类名

执行：python3 fix_v17_consistency.py
"""
import io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "v1.7", "zh-CN.html")

with open(PATH, encoding="utf-8") as f:
    s = f.read()

orig_len = len(s)
changes = []

# 1) 修复侧边栏 5 个断链
n1 = s.count('href="#di-er-shi-zhang"')
s = s.replace('href="#di-er-shi-zhang"', 'href="#di-er-shi-zhang-jinjie"')
changes.append(f"侧边栏 #di-er-shi-zhang → #di-er-shi-zhang-jinjie：{n1} 处")

# 2) 修复侧边栏 1 个断链
n2 = s.count('href="#di-shi-yi-zhang-fu"')
s = s.replace('href="#di-shi-yi-zhang-fu"', 'href="#di-shi-yi-zhang-advanced"')
changes.append(f"侧边栏 #di-shi-yi-zhang-fu → #di-shi-yi-zhang-advanced：{n2} 处")

# 3) 在第 36 章 (di-san-shi-liu-zhang) 所在 content-section 之后追加 5 章
# 找到第 36 章所在 div 的结束位置（最近的 </div> 在它后面，紧接下一个 <div 或 附录）
m36 = re.search(r'<div id="di-san-shi-liu-zhang" class="mb-10 content-section">', s)
assert m36, "未找到第 36 章起始标签"

# 从该起点向后找到匹配的结束 </div>
depth = 0
end_pos = None
for m in re.finditer(r'<(/?)div\b', s[m36.start():]):
    if m.group(1) == '/':
        depth -= 1
    else:
        depth += 1
    if depth == 0:
        end_pos = m36.start() + m.end()
        break
assert end_pos, "未匹配到第 36 章的结束 </div>"
insert_at = end_pos

# 5 章占位内容（保留文档样式：mb-10 content-section + h3 + chapter-intro）
new_chapters = '''
                <div id="di-san-shi-qi-zhang" class="mb-10 content-section">
                    <h3 class="text-xl font-bold text-dark dark:text-gray-200 mb-4">第三十七章：AI 与手机——大模型时代的贴身助理</h3>
                    <p class="chapter-intro mb-4">本章收录于《你缺失的那门手机课》v1.7 展望篇，介绍大语言模型与端侧 AI 在手机上的落地形态、典型应用与隐私边界，帮助读者在 AI 时代建立基本认知。完整内容正在持续打磨中，欢迎在反馈渠道告诉我们你最想看到哪些角度。</p>
                    <div class="info-box rounded-lg p-4">
                        <p class="font-semibold"><i class="fas fa-robot mr-2"></i>本章节为占位大纲</p>
                        <p>正文将覆盖：端侧大模型、云端协同、Agent 类应用、AI 摄影与录音转写等高频场景，以及隐私与能耗权衡。</p>
                    </div>
                </div>

                <div id="di-san-shi-ba-zhang" class="mb-10 content-section">
                    <h3 class="text-xl font-bold text-dark dark:text-gray-200 mb-4">第三十八章：投屏与车机互联——把手机变成第二块屏</h3>
                    <p class="chapter-intro mb-4">本章收录于《你缺失的那门手机课》v1.7 车联篇，整理有线/无线投屏（HDMI、Miracast、AirPlay、CarPlay、HiCar）的连接方式、协议差异与典型问题排查思路。完整内容正在持续打磨中。</p>
                    <div class="info-box rounded-lg p-4">
                        <p class="font-semibold"><i class="fas fa-car mr-2"></i>本章节为占位大纲</p>
                        <p>正文将覆盖：车机协议对比、CarPlay/HiCar/CarLink 实测、连接失败十大排查、行车场景下的注意力安全。</p>
                    </div>
                </div>

                <div id="di-san-shi-jiu-zhang" class="mb-10 content-section">
                    <h3 class="text-xl font-bold text-dark dark:text-gray-200 mb-4">第三十九章：儿童与手机——给家长的一份"不焦虑指南"</h3>
                    <p class="chapter-intro mb-4">本章收录于《你缺失的那门手机课》v1.7 儿童篇，回答家长最关心的"什么时候给、给什么、用多久"等问题，并整理系统级管控、家庭共享与第三方工具的取舍。完整内容正在持续打磨中。</p>
                    <div class="info-box rounded-lg p-4">
                        <p class="font-semibold"><i class="fas fa-child mr-2"></i>本章节为占位大纲</p>
                        <p>正文将覆盖：屏幕时间 vs 内容时间、系统家长控制、家庭共享、Apple/Google 儿童账号、内容分级与举报渠道。</p>
                    </div>
                </div>

                <div id="di-si-shi-zhang" class="mb-10 content-section">
                    <h3 class="text-xl font-bold text-dark dark:text-gray-200 mb-4">第四十章：适老化与无障碍——让科技服务于每一个人</h3>
                    <p class="chapter-intro mb-4">本章收录于《你缺失的那门手机课》v1.7 适老化篇，介绍 Android 与 iOS 的无障碍能力、放大/朗读/震动反馈等关键开关，以及面向长辈的"防诈+易用"双线配置思路。完整内容正在持续打磨中。</p>
                    <div class="info-box rounded-lg p-4">
                        <p class="font-semibold"><i class="fas fa-universal-access mr-2"></i>本章节为占位大纲</p>
                        <p>正文将覆盖：字体/显示/触控/语音放大、紧急联系人、防诈短信识别、远程协助工具与隐私权衡。</p>
                    </div>
                </div>

                <div id="di-si-shi-yi-zhang" class="mb-10 content-section">
                    <h3 class="text-xl font-bold text-dark dark:text-gray-200 mb-4">第四十一章：数字健康与安全急救——最后一公里的自检清单</h3>
                    <p class="chapter-intro mb-4">本章收录于《你缺失的那门手机课》v1.7 安全急救篇，作为全书收束，把分散在各章的"健康+安全"要点重新串联成一份可定期自检的清单：账号、备份、丢失应对、骚扰拦截、隐私审计与设备换代。完整内容正在持续打磨中。</p>
                    <div class="info-box rounded-lg p-4">
                        <p class="font-semibold"><i class="fas fa-shield-alt mr-2"></i>本章节为占位大纲</p>
                        <p>正文将覆盖：账号体检表、丢失黄金 30 分钟、备份 3-2-1 原则、骚扰拦截矩阵、年度隐私审计、设备换代数据迁移。</p>
                    </div>
                </div>

'''
s = s[:insert_at] + new_chapters + s[insert_at:]
changes.append(f"追加第 37-41 章占位（5 个 content-section）")

# 同步在侧边栏目录里增加新章节入口（避免遗漏导航）
# 在 <a href="#di-san-shi-liu-zhang"...>第三十六章 ... 后追加
sidebar_block_re = re.compile(
    r'(<li>\s*<a href="#di-san-shi-liu-zhang"[^>]*>第三十六章[^<]*</a>\s*</li>)'
)
sidebar_addition = '''
                                <li><a href="#di-san-shi-qi-zhang" class="text-primary hover:underline">第三十七章：AI 与手机</a></li>
                                <li><a href="#di-san-shi-ba-zhang" class="text-primary hover:underline">第三十八章：投屏与车机互联</a></li>
                                <li><a href="#di-san-shi-jiu-zhang" class="text-primary hover:underline">第三十九章：儿童与手机</a></li>
                                <li><a href="#di-si-shi-zhang" class="text-primary hover:underline">第四十章：适老化与无障碍</a></li>
                                <li><a href="#di-si-shi-yi-zhang" class="text-primary hover:underline">第四十一章：数字健康与安全急救</a></li>'''
m_sidebar = sidebar_block_re.search(s)
if m_sidebar:
    s = s.replace(m_sidebar.group(1), m_sidebar.group(1) + sidebar_addition, 1)
    changes.append("侧边栏导航追加 5 条新章节入口")
else:
    changes.append("⚠ 侧边栏未找到第 36 章入口，跳过导航追加（不影响 CI）")

with open(PATH, "w", encoding="utf-8") as f:
    f.write(s)

print("=" * 60)
print("v1.7/zh-CN.html 一致性修复完成")
print("=" * 60)
for c in changes:
    print(f"  ✓ {c}")
print(f"\n文件大小: {orig_len} → {len(s)} (+{len(s)-orig_len} bytes)")