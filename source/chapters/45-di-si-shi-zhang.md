---
id: di-si-shi-zhang
num: 40
part: ai-biancheng-pian
nav: 第四十章：需求工程——把想法变成AI指令
toc: default
kind: chapter
---

### 第四十章：需求工程——把想法变成AI可执行的指令

{class="chapter-intro mb-4"}
如果说上下文工程解决的是"让 AI 了解背景"，那需求工程解决的是"让 AI 知道这次具体要做什么"。这是 AI 编程中最能体现人与人差距的环节——同样的工具、同样的模型，有人能做出令人惊艳的项目，有人只能做出平庸的玩具。区别往往不在技术能力，而在<strong>需求表达能力</strong>。

#### 一、从模糊想法到结构化需求

每个项目都始于一个模糊的想法——"我想做一个记账 App""我想做个个人网站""我想做个待办清单工具"。这些想法本身没有问题，但如果你直接把它丢给 AI，产出的质量完全取决于运气。需求工程的目标，就是把这个模糊的想法，变成一个 AI 能精确执行的结构化需求。

好消息是：结构化需求不需要你写一份几十页的 PRD。它只需要你回答五个问题，我们称之为<strong>"需求五要素"</strong>：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要素</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">问题</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">示例：记账 App</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">给谁用？</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">个人使用，记录日常收支</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">做什么？</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一个能记录每笔收支、按月汇总、可视化的应用</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">为什么做？</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">想了解自己的消费结构，找出不必要的支出</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">大致怎么做？</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">前端用 React，数据存浏览器本地，先不做后端和登录</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">有什么限制？</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">单人开发，2 周内完成，不需要上线部署</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
需求五要素及示例

这五个要素不需要写成正式文档，甚至在脑海中快速过一遍就足够了。关键是养成"先想清楚再开口"的习惯。你会发现，当你能清晰地回答这五个问题时，你的需求描述自然就变得结构化了。

#### 二、需求拆解的分层艺术

对于较大的项目，一个需求描述是不够的。你需要把大需求拆解成小的、可独立验证的子需求。这个过程叫做"需求拆解"，核心原则是：<strong>每个子需求都应该能独立完成、独立验证、独立交付</strong>。

以"做一个个人记账 App"为例，一个合理的拆解方式是：

1. 实现基础的收支记录功能（能添加、查看、删除记录）；
2. 添加分类功能（给每笔记录打上餐饮、交通等标签）；
3. 实现月度汇总功能（按月统计收支情况）；
4. 添加数据可视化（用图表展示消费结构）。

每一步都是一个可以独立运行和验证的功能增量。

:::inline div .quote-line
需求拆解的黄金法则：每一步完成后，项目都应该是一个"能用的东西"——哪怕功能很简陋。永远不要让项目停留在"什么都做了一半但什么都用不了"的状态。
:::

这种拆解方式有两个好处。首先，它让你始终能看到进展——每完成一步，你的 App 就多了一个功能，这种正反馈对于长期项目至关重要（人都是需要成就感的嘛）。其次，它让 AI 的每次任务都足够小，降低了"AI 理解偏差"的风险——任务越小，AI 的理解越准确，产出质量越高。

#### 三、PRD 写作模板与实践

对于较大的项目（比如一个有前后端、多个功能模块的全栈应用），仅凭需求五要素可能不够。这时你需要写一份更正式的项目需求文档（PRD）。一个容易误解的点是：<strong>PRD 不是写给 AI 看的——它是写给你自己的</strong>，帮你理清思路，然后你才能给 AI 提供更精确的指令。

一份好的 PRD 不需要很长，但应该包含六个部分：项目概述（一段话说清楚做什么）、功能列表（每个功能点是什么）、技术方案（用什么技术栈、大致架构）、数据模型（核心数据结构）、界面描述（主要页面长什么样）、开发计划（分几步完成）。

::: div .code-block
:::inline div .code-head
<span>PRD.md</span><span class="dots">···</span>
:::

```
# 个人记账应用 PRD
## 项目概述
一个轻量级个人记账应用，支持收支记录、分类、月度汇总和数据可视化。
## 功能列表
1. 记录收支：金额、类型(收入/支出)、分类、备注、日期
2. 分类管理：预设餐饮、交通、购物、娱乐、其他
3. 月度汇总：按月统计总收入、总支出、结余
4. 消费可视化：饼图展示各分类占比
5. 数据导出：导出为CSV
## 技术方案
- 前端：React + TypeScript + Tailwind CSS
- 数据存储：localStorage（无需后端）
- 图表：使用Chart.js
- 构建：Vite
## 数据模型
Record {
  id: string
  amount: number
  type: 'income' | 'expense'
  category: string
  note: string
  date: string  // YYYY-MM-DD
}
## 开发计划
Step 1: 基础记录功能 (CRUD)
Step 2: 分类管理
Step 3: 月度汇总
Step 4: 数据可视化
Step 5: 数据导出
```
:::

注意这份 PRD 的写作风格：用简洁的列表和结构化的格式，而不是长篇大论。每个功能点都有明确的定义，数据模型用简单的类型描述。这种风格的 PRD 不仅你自己看得清楚，当你把它提供给 AI 时，AI 也能精确理解每个需求点。

#### 四、实战：从想法到方案的完整推演

纸上谈兵没意思，咱们用一个完整的例子走一遍需求工程的全过程。假设你的想法是：<strong>"我想做一个能追踪我每天学了什么的学习追踪器"</strong>。

<strong>第一步，过一遍需求五要素。</strong>

- Who：个人使用。
- What：一个能记录每天学习内容、追踪学习时长、回顾学习进度的工具。
- Why：想养成持续学习的习惯，看到自己的积累。
- How：先做一个网页版，数据存在浏览器本地。
- Constraint：零基础开发，1 周内完成核心功能。

<strong>第二步，拆解需求。</strong>

1. Step 1：实现"记录学习条目"功能（日期、内容、时长）；
2. Step 2：添加"学习时长统计"（今日、本周累计）；
3. Step 3：实现"学习日历"视图（像 GitHub 贡献图一样展示）；
4. Step 4：添加"学习回顾"功能（随机展示过去某天的学习记录，帮助复习）。

<strong>第三步，写一份简短 PRD。</strong>不需要长——上面的拆解本身就构成了 PRD 的主体。把它整理成一个 .md 文件，放在项目根目录，作为你和 AI 的共同参考。

<strong>第四步，开始第一步的开发。</strong>给 AI 的指令可以是：

::: div .code-block
:::inline div .code-head
<span>给 AI 的指令</span><span class="dots">···</span>
:::

```
我需要一个学习追踪器的第一个功能——记录学习条目。
用户可以添加一条学习记录，包含日期、学习内容、学习时长（分钟）。
数据存在localStorage。
前端用React + TypeScript。
请给出完整实现。
```
:::

注意这个指令的特点：它<strong>只描述当前这一步的目标</strong>（记录功能），不掺杂其他功能；它<strong>明确了技术约束</strong>（React、TypeScript、localStorage）；它给了足够的信息让 AI 知道"做什么"和"怎么做"，但具体实现由 AI 决定。这就是一个经过需求工程加工后的、高质量的 AI 编程指令。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：给你的"心头好"写一份五要素卡

{class="mt-1"}
选一个你酝酿已久的小项目，花 5 分钟填一张卡：Who / What / Why / How / Constraint，各一句话。然后把它拆成 3-5 个"每一步都能用"的步骤。你会发现：把想法写下来之后，它就从"白日梦"变成了"待办清单"。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 需求五要素：Who / What / Why / How / Constraint——想清楚再开口
- 需求拆解黄金法则：每一步完成后项目都是"能用的东西"
- PRD 是写给自己的：概述、功能列表、技术方案、数据模型、界面、计划
- 好指令 = 只描述当前一步 + 明确约束 + 说"做什么"不说"怎么做"
- 完整推演模板：五要素 → 拆解 → PRD → 给指令，四步走
:::
