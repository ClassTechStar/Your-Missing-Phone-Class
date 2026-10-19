---
id: di-san-shi-ba-zhang
num: 38
part: ai-biancheng-pian
nav: 第三十八章：AI编程五大思维原则
toc: default
kind: chapter
---

### 第三十八章：AI编程五大思维原则

{class="chapter-intro mb-4"}
如果这本书只能让你记住一章，那必须是这一章。五大思维原则是全书的心脏，后面所有章节——上下文、需求、对话、质量——都是这五条原则在不同场景下的展开。放心，每一条都不难懂，但每一条都值得你用几个项目去"长进肌肉里"。

故事的起点很有意思：Andrej Karpathy 在开源他的项目时，附了一份仅 <strong>70 行</strong>的 CLAUDE.md 文件，总结了与 AI 协作的四条核心原则。这份文件在 GitHub 上获得了超过 70,000 个 Star，成为全球 AI 编程实践者最广泛引用的准则。这四条原则不是空洞的口号，而是从大量实践中提炼出的、可操作的思维习惯。<strong>本书在其基础上补充了第五条——迭代验证——构成完整的五大原则体系</strong>。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>70 行文件为什么这么值钱？

{class="mt-1"}
70,000 个 Star 是什么概念？GitHub 上绝大多数项目一辈子都到不了这个数字。一个 70 行的文本文件能获得它，恰恰证明了一件事：AI 时代最稀缺的不是代码，而是"想清楚"的能力。这 70 行，就是"想清楚"的浓缩版。
:::

#### 一、原则一：Think Before Coding（先思考，再编码）

这是五条原则中最反直觉的一条。既然 AI 能帮我们写代码，为什么还要"先思考"？答案很简单：<strong>AI 的产出质量与你的输入质量正相关</strong>。你自己都没想清楚要做什么，AI 给出的答案只会让你陷入无休止的"改了又改"循环——俗称"AI 陪你一起迷路"。

"先思考"意味着在给 AI 下达指令之前，你需要回答三个问题，它们构成一个缺一不可的"思考三角"：

1. <strong>我要解决什么问题？</strong>（目标）
2. <strong>我期望的结果长什么样？</strong>（验收标准）
3. <strong>有哪些约束条件需要遵守？</strong>（边界）

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">思考维度</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">模糊输入（差）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">清晰输入（好）</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">问题定义</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">帮我做个网站</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">帮我做一个个人工具站，展示 3 个 AI 小工具的入口卡片</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">期望结果</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">好看一点</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">响应式布局，暗色主题，卡片有悬停动画，移动端可用</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">约束条件</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">（未说明）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不使用框架，纯 HTML+CSS+JS，单文件部署，不需要后端</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
同一需求的模糊输入与清晰输入对比

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>注意：先思考 ≠ 先写完美文档

{class="mt-1"}
"先思考"不等于"写一份完美的 PRD 再开始"。它是一个快速但有条理的思考过程——花 30 秒想清楚上面三个问题，远比花 30 分钟在对话中反复修改来得高效。小任务三问可以很短；大项目可以把它们扩展成完整的需求文档（详见第四十章）。
:::

#### 二、原则二：Simplicity First（简单至上）

AI 编程最大的陷阱不是"做不出来"，而是<strong>"做得太多"</strong>。当你对 AI 说"做一个用户管理系统"，它可能会生成认证、权限、角色、审计日志、数据导出等一整套功能——但你现在可能只需要一个简单的登录页面。过度生成，是 AI 代码膨胀的主要原因。

"简单至上"要求你在每次下达指令时都遵循"最小可行"原则：<strong>用最少的代码实现核心功能，用最简单的方案解决问题，用最少的功能验证想法</strong>。Karpathy 对此有个精辟的比喻："如果你要计算一个折扣价格，你不需要一个电商引擎。"

在实践中，"简单至上"意味着几个具体的操作习惯：

- 每次只让 AI 实现<strong>一个功能点</strong>，而不是一口气描述整个系统；
- 优先选择标准库和简单方案，而不是引入复杂的依赖；
- 能用 50 行代码解决的问题，不要让 AI 写 500 行；
- 当 AI 的产出超出预期范围时，勇敢地告诉它"<strong>砍掉多余的部分</strong>"。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">场景</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">过度方案（避免）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">简单方案（推荐）</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需要存储数据</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">搭建 MySQL 数据库 + ORM</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">先用 JSON 文件或 SQLite</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需要用户登录</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OAuth2.0 + JWT + 角色权限</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">先做简单的密码验证</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需要前端框架</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">React + Redux + Router</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">先试纯 HTML + 原生 JS</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需要部署上线</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Docker + CI/CD + K8s</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">先在本地跑通再说</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
常见场景的过度方案与简单方案对比

#### 三、原则三：Surgical Changes（精准修改）

当你在迭代一个已有项目时，每次修改都应该像外科手术一样精准——<strong>只动该动的地方，不碰不该碰的</strong>。这一点在 AI 编程中尤其重要，因为 AI 有"顺手改一下"的倾向：你让它修一个 bug，它可能顺便重构了半个文件。

"精准修改"的核心要求是：每次给 AI 的指令，都明确指定修改的范围和边界。告诉它"只修改 <code class="inline">calculate_discount</code> 函数""不要动其他部分""保持现有的代码风格"。当 AI 的修改超出了你要求的范围时，立即要求它回退多余的部分。

Karpathy 用一个 diff（差异对比）的例子说明了这一点。假设你让 AI 给购物车的折扣计算函数添加"会员价"逻辑：好的产出是只修改这一个函数、增加几行代码；坏的产出是把整个文件重构了一遍——虽然新代码可能更"优雅"，但你无法确定它有没有引入新 bug。<strong>在 AI 编程中，"看起来更好"永远不能成为偏离指令的理由</strong>。

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
<i class="fas fa-times-circle mr-1"></i> 差的指令（范围模糊）

{class="font-mono text-xs leading-relaxed"}
帮我优化这个项目的<br>折扣计算逻辑
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
<i class="fas fa-check-circle mr-1"></i> 好的指令（精准指定范围）

{class="font-mono text-xs leading-relaxed"}
只修改 cart.py 中的 calculate_discount 函数：<br>1. 在现有折扣基础上增加会员价逻辑<br>2. 会员用户额外享受 10% 折扣<br>3. 不要修改函数签名和其他函数<br>4. 保持现有的变量命名风格
:::
:::

#### 四、原则四：Goal-Driven Execution（目标驱动执行）

这条原则回答了一个关键问题：你应该给 AI 下达<strong>"怎么做"</strong>的指令，还是<strong>"做什么"</strong>的指令？Karpathy 的答案是后者。与其告诉 AI"先创建一个类，然后添加方法，然后写测试"，不如告诉它"我需要一个能解析 CSV 文件并统计每列唯一值数量的工具"。<strong>让 AI 自己决定实现路径，你负责验收结果</strong>。

"目标驱动"的好处是双重的。对 AI 来说，它获得了更大的自主空间，可以选择最优的实现路径，而不是被你的中间步骤束缚；对你来说，你把注意力从"怎么做"转移到了"做出来对不对"——这正是指挥官该做的事。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>注意：目标驱动 ≠ 放任不管

{class="mt-1"}
它需要你在 AI 执行后进行严格的验收：结果是否满足需求？边界情况是否处理了？是否有明显的过度设计？如果结果不符合预期，提供具体的反馈——不是"重写"，而是"这里的问题在于空列表输入会报 IndexError，请修改为添加空值检查"。
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">指令风格</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">示例</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">结果特点</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">命令式（怎么做）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"先创建一个 Python 类，叫 DataParser，加一个 parse 方法，接收 filename 参数，用 csv 模块读取…"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI 变成打字员，你的中间步骤可能不是最优路径</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">目标式（做什么）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"我需要一个工具：读取 CSV 文件，统计每列的唯一值数量，输出为 JSON 格式。请给出完整实现。"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI 自主选择最优路径，你负责验收结果</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
命令式指令与目标式指令的对比

#### 五、原则五：Iterate and Verify（迭代验证）

这是本书在 Karpathy 四原则基础上补充的第五条。它的核心信念是：<strong>AI 的第一次产出几乎永远不是最终版本</strong>。有效的 AI 编程是一个"生成-验证-修正"的迭代循环，而不是一次性的"指令-产出"。

"迭代验证"不是被动的"不对就再试"，而是一个有结构的验证流程。每次 AI 给出产出后，按三个层次进行验证：

- <strong>第一层·功能验证</strong>：它能不能跑？输入输出对不对？
- <strong>第二层·边界验证</strong>：空输入、超长输入、异常输入会怎样？
- <strong>第三层·架构验证</strong>：代码结构是否合理？有没有硬编码？是否便于后续扩展？

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-bullseye mr-1"></i> 定义目标</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> AI 生成代码</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> 功能验证</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> 通过</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> 边界验证</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> 通过</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-landmark mr-1"></i> 架构审查</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> 通过，进入下一步</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> 不通过</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> 提供具体反馈</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> 重新生成</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
图 2：AI 编程的迭代验证循环
:::

这个循环的关键在于"提供具体反馈"这一步。当验证不通过时，不要说"不对，重做"，而要说"函数在输入空列表时报 IndexError，请在第 15 行添加空值检查"。<strong>具体的反馈让 AI 能精准修正；模糊的反馈只会让它重新猜测你的意图</strong>。

#### 六、Harness Engineering：Agent = Model + Harness

2026 年中期，一个叫 <strong>Harness Engineering</strong> 的概念开始在 AI 编程社区流行。它的核心公式很简单：

:::inline div .quote-line .text-center .text-base .font-bold
<strong>Agent 的能力 = 模型能力 × Harness 质量</strong>
:::

模型能力是 AI 大脑的智力上限；Harness 是围绕模型搭建的"工作环境"——包括上下文管理、工具集成、流程编排、记忆系统等。

这个概念解释了一个常见的困惑：为什么同样用 GPT-4 或 Claude，有的人能做出惊艳的项目，有的人只能得到平庸的代码？<strong>区别不在模型，而在 Harness</strong>。一个好的 Harness 包括：清晰的项目规范文件、合理的工具集成、有条理的对话上下文、完善的验证流程。模型决定了智力上限，Harness 决定了你能多大程度地发挥这个上限。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>天才实习生比喻

{class="mt-1"}
你可以把模型想象成一个天才实习生——智商很高，但如果不给他项目背景文档、不告诉他用哪些工具、不给他设定期限和验收标准，他也做不出好东西。Harness Engineering 就是"如何给天才实习生搭好工作环境"的工程。
:::

本书的后续章节，本质上都在教你如何构建一个好的 Harness：第三十九章教你管理上下文（项目记忆系统），第四十章教你定义需求（PRD），第四十三章教你对话技术（Prompt 分层），第四十五章教你质量保障（验证流程）。这些组合起来，就是你的 Harness。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：用"思考三角"拆解你的下一个想法

{class="mt-1"}
挑一个你一直想做但没动手的小东西（比如一个倒数日网页、一个喝水提醒脚本）。花 3 分钟回答：① 它解决什么问题？② 做出来长什么样？③ 有什么约束（时间、技术、环境）？然后把答案写成一段话。恭喜你，你已经完成了人生第一次"Think Before Coding"——这段话就是一条合格的高质量指令。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 五大原则源自 Karpathy 70 行的 CLAUDE.md（70K+ Star），本书补充第五条"迭代验证"
- Think Before Coding：开口前回答三问——做什么？结果长啥样？有什么约束？
- Simplicity First：AI 最大的坑是"做得太多"——算折扣不需要电商引擎
- Surgical Changes：像外科手术一样精准修改，拒绝 AI 的"顺手改一下"
- Goal-Driven Execution：说"做什么"，不说"怎么做"，让 AI 自主选路径
- Iterate and Verify：三层验证（功能/边界/架构）+ 具体反馈，循环迭代
- Harness Engineering：能力 = 模型 × Harness，把 AI 当"天才实习生"来管理环境
:::
