---
id: di-si-shi-san-zhang
num: 43
part: ai-biancheng-pian
nav: 第四十三章：对话工程——高效对话技术
toc: default
kind: chapter
---

### 第四十三章：对话工程——与AI高效协作的对话技术

{class="chapter-intro mb-4"}
对话是 AI 编程的核心交互方式。但请注意："对话"不等于"聊天"——高效的 AI 编程对话是一种有结构的沟通技术，我们称之为"对话工程"。它研究的是：如何用最少的对话轮次，获得最高质量的代码产出。说白了，这一章就是教你怎么和 AI"把话说清楚"。

#### 一、Prompt 分层策略

与 AI 的对话可以分为三个层次，每层承担不同的功能。理解这三个层次，你就能像搭积木一样组合出高效的 Prompt。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">层次</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">功能</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">示例</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">频率</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系统层</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">设定AI的角色和全局约束</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"你是一个React专家，代码必须用TypeScript"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">项目开始时设置一次</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">任务层</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">描述当前要做的具体任务</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"实现一个表单组件，包含用户名和密码字段"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每个任务开始时给出</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">反馈层</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">对AI产出进行评价和修正</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"密码字段缺少显示/隐藏切换，请添加"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">根据产出质量给出</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
对话 Prompt 的三个层次

系统层的 Prompt 通常写在项目记忆文件中（如 CLAUDE.md），不需要每次对话重复。任务层是你在对话中最常使用的——它应该包含<strong>"做什么""用什么技术""有什么约束"</strong>三个要素。反馈层是最考验功力的——好的反馈能让 AI 精准修正，坏的反馈只会让它重新猜测。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：反馈三板斧

{class="mt-1"}
一个实用的反馈模板是"指出问题 + 说明期望 + 提供上下文"。比如："第 25 行的错误处理只用了 console.log（指出问题），生产环境应该用统一的错误处理器并返回用户友好提示（说明期望），项目里有一个 handleError 函数可以用（提供上下文）"。这种反馈比"改一下错误处理"有效十倍。
:::

#### 二、调试对话：如何描述错误让 AI 快速定位

调试是 AI 编程中最频繁的场景之一。当你遇到 bug 时，如何向 AI 描述问题，直接决定了它能否快速帮你定位和修复。以下是调试对话的四个要点：

1. <strong>给 AI"看"原始信息，而不是你的转述</strong>。把错误日志、异常堆栈、相关代码直接 @ 引用给 AI，而不是用"好像有个什么报错"来描述。AI 看到原始信息比看到你的理解更准确。
2. <strong>描述"期望行为"和"实际行为"的差异</strong>。"我期望点击按钮后跳转到首页（期望），但实际点击后页面没有反应（实际）"——这种描述比"按钮坏了"有用得多。
3. <strong>提供复现步骤</strong>。"先输入用户名，然后点击登录按钮，就会出现这个错误"——复现步骤让 AI 能模拟你的操作路径，更容易定位问题。
4. <strong>说清楚你已经尝试了什么</strong>。"我已经检查了网络请求，返回 200，数据正常"——这能帮 AI 排除已验证的方向，不浪费时间重复排查。

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
<i class="fas fa-times-circle mr-1"></i> 差的调试描述

{class="font-mono text-xs leading-relaxed"}
按钮点击没反应，帮我看看
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
<i class="fas fa-check-circle mr-1"></i> 好的调试描述

{class="font-mono text-xs leading-relaxed"}
点击登录按钮后页面无反应。<br>期望行为：点击后跳转到 /home 页面<br>实际行为：点击后无任何反应，控制台无报错<br>复现步骤：<br>1. 在登录页输入用户名admin和密码123456<br>2. 点击"登录"按钮<br>3. 页面无反应<br>已排查：<br>- 网络请求正常，返回200<br>- onClick事件已绑定<br>- 检查了LoginButton组件的代码<br>相关文件：@src/components/LoginButton.tsx<br>　@src/pages/Login.tsx
:::
:::

#### 三、迭代策略：小步快跑 vs 大步重构

AI 编程中的迭代有两种基本策略，适用于不同场景。理解它们的区别，能帮你在不同情况下做出正确选择。

<strong>"小步快跑"</strong>策略适用于功能开发和 bug 修复。它的核心是：每次让 AI 只做一个小的修改，验证通过后再做下一个。优势是每一步都可验证、可回退，风险可控；劣势是速度较慢，需要频繁的对话交互。适合：新功能开发、不确定最优方案时的探索、对 AI 产出不太放心时的谨慎迭代。

<strong>"大步重构"</strong>策略适用于明确知道目标的大规模修改。它的核心是：一次性描述完整的目标，让 AI 自主规划和执行整个修改。优势是速度快，AI 能看到全局图景做出更优的架构决策；劣势是风险高，如果 AI 理解偏差，修正成本大。适合：明确的架构升级、大规模代码迁移、有充分测试保障的重构。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">维度</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">小步快跑</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">大步重构</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每次修改量</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一个功能点或一个bug</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一个模块或一个架构层</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">验证频率</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每次修改后立即验证</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全部修改完成后统一验证</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">对话轮次</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多（5-10轮/功能）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">少（1-3轮/模块）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">风险</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">低，每步可回退</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">高，偏差修正成本大</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">适用场景</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新功能、探索性开发</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">明确目标的重构、迁移</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">前提条件</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">无特殊要求</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需要有测试覆盖</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
两种迭代策略的对比

实践中，两种策略常常组合使用。比如重构一个模块时，先用"大步重构"让 AI 给出整体方案，审查方案后，再用"小步快跑"逐步执行。这样既保证了全局视角，又控制了执行风险。

#### 四、多轮对话的上下文管理

随着对话轮次增加，你需要主动管理对话上下文，避免"AI 忘记了早期信息"的问题。以下是几个实用的上下文管理技巧。

<strong>第一，"锚定"关键信息。</strong>在对话开始时，把关键约束写清楚，并在后续对话中适时重申。比如"记住，我们的数据存在 localStorage，不能用数据库"——在相关的修改请求中重申这个约束，防止 AI 遗忘。

<strong>第二，善用"总结-续接"技巧。</strong>当对话变得很长时，可以让 AI"总结一下目前的进展和待办事项"，然后开一个新对话，把这个总结作为起点。这样既保留了关键上下文，又避免了长对话的退化。

<strong>第三，"一个对话一个任务"。</strong>这是最简单也最有效的上下文管理策略。每个对话只处理一个任务或一个功能点，完成后开新对话处理下一个。这天然限制了对话长度，保持上下文清晰。

<strong>第四，利用工具的上下文管理功能。</strong>大多数 AI 编程工具都有"清除上下文"或"新会话"按钮——当你感觉 AI 的回答质量下降时，不要犹豫，开一个新会话。丢失一些对话历史比继续在退化的上下文中挣扎要好得多。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：给你的 AI 当一次"病人"

{class="mt-1"}
故意在浏览器里做一个小页面，制造一个 bug（比如按钮没反应）。然后按本章"好的调试描述"的格式，向 AI 完整描述一次：原始信息、期望 vs 实际、复现步骤、已排查项。感受一下 AI 定位问题的速度差异——你会理解为什么"描述问题"本身是门手艺。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- Prompt 三层：系统层（写在记忆文件）、任务层（做什么+技术+约束）、反馈层（指出问题+期望+上下文）
- 调试四要点：给原始信息、期望vs实际、复现步骤、已排查项
- 小步快跑：低风险高轮次，适合新功能；大步重构：高风险低轮次，需要测试保障
- 上下文管理四招：锚定关键信息、总结-续接、一个对话一个任务、果断开新会话
:::
