---
id: di-si-shi-er-zhang
num: 42
part: ai-biancheng-pian
nav: 第四十二章：大模型全景与API实战
toc: default
kind: chapter
---

### 第四十二章：大模型全景与API实战

{class="chapter-intro mb-4"}
前面几章讲的都是"怎么和 AI 协作"，本章解决一个更基础的问题："用哪个 AI？怎么用？"2026 年 8 月的大模型格局已经极其丰富，国际有 GPT、Claude、Gemini 三强争霸，国内有 DeepSeek、通义千问、GLM、Kimi和豆包百花齐放。每个模型都有自己的性格和特长：选对了省一半力气，选错了事倍功半。<strong>11 月更新</strong>：OpenAI 的 GPT-6 Sol/Luna 已于 9 月下旬发布（价格约为 GPT-5.6 的一半），旗舰为 GPT-6 Astra；Anthropic 新主力是 Claude Opus 5.5，下表保留 8 月快照，供理解格局演变，价格以各家官网现价为准。本章不仅带你认识这些模型，还会教你如何通过 API 将它们接入自己的应用，以及如何根据自己的需求选择合适的 Token Plan（用量套餐）。

::: div .quick-read
##### 本章速读（5 分钟版）
前面几章讲的是"怎么和 AI 协作"，这一章解决更基础的问题：用哪个 AI、怎么把它接进你自己的东西里。国际上 GPT、Claude、Gemini 三强各有性格，国内 DeepSeek、通义千问、GLM、Kimi和豆包百花齐放；后半章带你从零走一遍 API 调用和 Token 套餐的选择。先把本章的约定记住：这里的价格表是"格局的快照"，不是今天的报价单，型号和价格以各家官网现价为准，保鲜期比牛奶长不了多少。
最关键的有三件事。第一，选模型看<strong>性格</strong>不看跑分：GPT 是全能均衡的"闭眼选不会错"，Claude 是编程与长文档的主场、幻觉率约 1% 全网最低，适合"错一个字就要命"的场景，Gemini 是多模态之王、200 万 Token 上下文最大，图文视频解析几乎没对手。国产这边 DeepSeek 是性价比之王，Kimi 擅长超长文本，各家差价能到几十倍：够用的就是最好的，让大模型干小活是最大的浪费。第二，API 入门就几样东西：Token 是计量单位，去官网注册拿 API Key，一次调用就是发一个 messages 列表；输出价格通常是输入的数倍，所以<strong>让模型"少说话"比让它"少读"更省钱</strong>。第三，买套餐之前先在免费层做判断题：拿二十个你的真实任务跑一遍，记下哪些答得好、哪些答得勉强，带着清单去对照付费档位，先付费再试错，是新手最常见的浪费。
今天就能做的最小动作：拿手头一个真实问题，在两家的免费模型上各问一遍，对比答案质量和说话的口吻。半小时就有自己的判断，比看任何测评都准；顺手把两家的官网价格页存个书签，以后立项前花五分钟刷一遍。
最大的坑有四个：拿本章的快照价格做预算；信跑分（基准污染、选择性汇报，而且你的任务可能根本不在考纲里）；在新旧模型交替的当口锁死长期选择（新项目直接上新一代，老项目观察几天再迁，迁移成本其实很低）；以及把不该交给大模型的活交出去，需要"当下"信息的、需要精确与审计的、责任落在你头上的活，AI 只能打下手。最后记牢一句话：它说得很笃定，和它说对了，是两回事，关键场景一律人工核对。
##### 速查表
- 选模型看性格：GPT 全能均衡、Claude 编程与长文档最稳、Gemini 多模态最强
- 国产之选：DeepSeek 性价比之王、Kimi 超长文本强、通义千问偏企业级场景
- 省钱要诀：输出价是输入的数倍，让模型少说话比少读更省
- 购买顺序：先免费层跑二十个真实任务，再对照档位，别先付费再试错
- 价格纪律：以官网现价为准，别拿快照做预算，换代期别锁死长期选择
- API 入门：拿 API Key、发 messages，多轮对话的历史是你自己维护的
- 读跑分：防基准污染、防选择性汇报，你的任务可能不在考纲里
- 三不交：当下信息、精确审计、责任在你的活，别全丢给大模型
:::

<div class="version-anchor">本章界面路径按 iOS 18.x / HarmonyOS 5.x / Android 15 核对（2026 年 11 月）。你的机型或系统版本不同，菜单名字和位置可能对不上——以你手机上显示的为准。</div>


#### 一、国际主流大模型：三强格局

2026 年 8 月的国际大模型市场，形成了 OpenAI（GPT 系列）、Anthropic（Claude 系列）、Google（Gemini 系列）三强鼎立的格局。每家都有自己鲜明的特色，咱们一个一个认识。

先给一个阅读建议：这一节别去背价格。价格每个月都在动，榜单每周都在刷，真正值得记住的是每家模型的"性格"，它擅长什么、看重什么、在什么场景下会让你惊喜或者失望。下面的价格表照旧放在这里，但请把它们当成"格局的快照"，而不是"今天的报价单"。

##### 1. OpenAI GPT-5.6 系列：全能均衡的六边形战士

OpenAI 是大模型浪潮的开启者，GPT 系列至今仍是全球使用最广泛的模型。2026 年 7 月发布的 GPT-5.6 系列采用三档定位策略：旗舰款 GPT-5.6 Sol 面向高端推理需求，均衡款 GPT-5.6 Terra 面向日常开发，轻量款 GPT-5.6 Luna 面向高并发低成本场景。三款模型共享约 100 万 Token 的上下文窗口，都支持图像输入、函数调用和结构化输出。

"三档定位"为什么值得认真看？因为过去很多服务商只有一个模型，你要么忍受慢和贵，要么忍受笨。分档的意义是把"这活儿配得上多聪明的脑子"变成一个可选参数：旗舰 Sol 啃硬骨头，复杂推理、架构决策、长链条任务；均衡的 Terra 是日常主力，大多数开发任务它都接得住；轻量的 Luna 负责跑量，分类、提取、格式转换这类不需要深思的活儿。

读这张价格表还有个门道：看输入和输出的差价。输出价格通常是输入的数倍，也就是说，<strong>让模型"少说话"比让它"少读"更省钱</strong>。记住这一点，后面讲成本优化时你会用到。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">型号</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">定位</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">输入(/百万Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">输出(/百万Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">上下文窗口</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Sol</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">旗舰推理</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$5.00 (约36元)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$30.00 (约217元)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">105万Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Terra</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">均衡日常</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$2.50 (约18元)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$15.00 (约109元)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">105万Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Luna</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">轻量低成本</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$1.00 (约7元)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$6.00 (约44元)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">105万Token</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
OpenAI GPT-5.6 系列定价（2026 年 8 月）

GPT 系列的核心优势在于"均衡"。推理、编程、写作、多模态，没有明显短板。加上 OpenAI 庞大的插件生态和开发者社区，适配文档和工具链最为完善。对于"不知道选什么"的场景，GPT 是"闭眼选都不会错"的默认答案。但它的短板是：国内访问需要特殊网络，中文表达偶尔有"翻译腔"，API 价格处于中高水平。

"翻译腔"是什么感觉？它不是错别字。它是一种微妙的违和——句子都通顺，但"这无疑是一个值得深入思考的问题"这种表达，中国人自己写东西时不会这么说。日常问答影响不大，如果你要用它批量生成面向中文用户的文案，建议在提示里明确要求口语化，或者生成后加一道人工润色。

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-rocket mr-2"></i>好消息

{class="mt-1"}
OpenAI 在 2026 年 8 月宣布免费用户默认模型升级为 GPT-5.6 Luna，并开放无限量文本聊天。这意味着你可以零成本体验 GPT 的基础能力，只有在需要更强推理或 API 调用时才需要付费。
:::

免费额度要这么用才不亏：把"我要不要付费"的判断题放到免费层做。拿二十个你的真实任务在免费模型上跑一遍，记下哪些答得好、哪些答得勉强，带着这份清单去对照付费档位，比看任何测评都准。反过来的顺序（先付费再试错）是新手最常见的浪费。

##### 换代进行时：GPT-6 的 Sol、Luna 与 Astra

就在这一章更新前后，OpenAI 完成了一次换代：2026 年 9 月 22 日，GPT-6 系列正式发布，首发 Sol 与 Luna 两档，旗舰型号为 Astra：价格大约是 GPT-5.6 同档的一半。命名延续了 5.6 时代的思路：Sol 扛旗舰推理，Luna 守轻量高频，Astra 站在整条产品线的最高点。

这次不是"又变强了"，是价格。旗舰级能力以一半左右的价格开放，意味着"用最好的模型"这件事的门槛又降了一截。行业里这种幅度的降价通常有两个来源：推理效率的优化，和竞争对手给的压力。无论哪个原因，受益的都是按 Token 付费的开发者。

实操建议只有一条：<strong>价格和型号以官网现价为准，别拿本章的快照做预算</strong>。每次立项前花五分钟刷一遍各家价格页，是个值得养成的习惯，这个市场的价格表，保鲜期比牛奶长不了多少。

换代期还有一条心法：<strong>别在新旧交替的当口锁死长期选择</strong>。老模型稳定、文档全、社区答案多，新模型便宜、上限高，最优解往往是"新项目直接上新一代，跑了一周以上的老项目观察几天再迁"。好在迁移成本极低：换成 API 之后，改两行代码的事。那些在新品发布当天就把生产系统全量切换的团队，后来大多花了成倍的时间填坑。

##### 2. Anthropic Claude 系列：编程与严谨的天花板

如果说 GPT 是全能选手，那 Claude 就是编程领域的"天花板"。Anthropic 的 Claude 系列长期是编程场景的主力选手，代码生成质量和工程级项目落地能力在第一梯队（SWE-bench 各版本成绩几度轮换领先，看趋势别背单个数字）。更难得的是，Claude 的幻觉率（生成虚假信息的概率）全网最低，仅约 1%，这使它特别适合学术、法务等高精度场景。

"幻觉率低"这件事值得多说两句。生成虚假信息的概率低，意味着它在不熟悉的领域倾向于说"我不确定"，而不是硬编一个听起来很合理的答案。学术综述、合同条款、法规引用这类"错一个字都要命"的场景，这个特性比跑分重要得多。但注意，低不等于零——任何模型的输出在关键场景都要人工核对。"它说得很笃定"和"它说对了"，是两回事。

Claude 的另一个杀手锏是超长上下文：支持 100 万 Token 的上下文窗口，能一次性"读完"几百页的合同或整个代码库不漏细节。这在代码重构、长文档分析等场景中几乎无可替代。Claude Code 作为终端 AI 编程工具，到 2026 年中期年化收入已达 25 亿美元，这是 Claude 编程能力最受认可的证据。

Claude Code 那个收入数字背后有个朴素的逻辑：开发者是最精明的付费群体，他们只为自己天天用、确实提效的工具掏钱。一个命令行工具能做出这个量级，基本等于编程圈用钱包投了一次票。这也是为什么后面讲国产模型时，你会反复看到"兼容 Claude 的 API"，大家都在对齐这套被验证过的能力。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">型号</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">定位</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">输入(/百万Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">输出(/百万Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">上下文窗口</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Fable 5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">旗舰款</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$10.00 (约72元)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$50.00 (约362元)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">100万Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Opus 4.8</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">专业款</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$5.00 (约36元)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$25.00 (约181元)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">100万Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Sonnet 5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">性价比款</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$2.00 (约14元)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$10.00 (约72元)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">100万Token</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Anthropic Claude 系列定价（2026 年 8 月，Sonnet 5 为优惠价）

Claude 的短板是价格，Fable 5 的输出价格是所有模型中最高的，每百万 Token 要 50 美元。多模态能力（图像、视频理解）也相对较弱。对于预算有限的个人开发者，Sonnet 5 在优惠期内的性价比非常突出。

按惯例交代一下时效：到本章 11 月更新时，Anthropic 的主力型号已推进到 Opus 5.5，上表是 8 月的快照。型号在变、价格在变，但 Claude 系列的定位一直很稳，编程与长文档是它的主场，多模态是它的客场。这个"主场客场"的判断法，比记任何一张价格表都耐用。

什么信号出现时该想到 Claude？三个。你的任务核心是"读懂一大堆代码再动手"；你的场景里错一个字代价很大，宁可它啰嗦也要它稳；你已经在用以 Claude 为核心的工具链（比如各类编程智能体），上下文和工具都是现成的。三条中两条，就值得给它一个试用的机会。

##### 3. Google Gemini 系列：多模态的王者

Google 的 Gemini 系列在 2026 年已迭代至 3.1 Pro 版本。Gemini 的最大杀手锏是原生多模态，图文解析精准、OCR 表格识别无误、视频帧提取高效，还支持音视频深度解析。它与 Google 生态（搜索、邮箱、云服务）深度绑定，在实时信息检索和跨模态理解上表现突出。Gemini 还支持 <strong>200 万 Token</strong> 的超长上下文输入，是目前上下文窗口最大的模型。

"原生多模态"四个字值得拆开讲。早期的多模态是拼接式的：一个视觉模型负责看图，把看到的内容翻译成文字，再交给语言模型处理，中间那次"翻译"就是信息损耗。原生多模态是图像和文字从一开始就在同一个模型里一起训练，模型"看"图表不需要经过转述。落到体验上，就是问它一张复杂表格里的数据关系，它不会把数字看串行。

Gemini 的定位是"科学推理和多模态场景的首选"。如果你的项目涉及大量图像分析、视频理解或科学计算，Gemini 几乎没有对手。但它在纯文本代码生成上略逊于 Claude，中文表达也不如国产模型自然。

还有一点值得提醒：Gemini 与安卓手机的整合很深。在 Google 服务可用的市场，新手机上语音助手、相册搜索背后往往都是它：模型离你的拇指越近，你用它的频率就越高。这也是"选模型也是选生态"的一个例子，下一节会展开这个话题。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">对比项</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GPT-5.6</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Claude Fable 5</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Gemini 3.1 Pro</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">综合得分</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">94.8</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">95.0</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">92.1</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">编程能力(SWE-bench)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">74.9%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">64.3% (Pro)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">中等</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">上下文窗口</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">105万Token</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">100万Token</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">200万Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多模态能力</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">均衡</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">较弱</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最强</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">幻觉率</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">较低</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最低(约1%)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">较低</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">国内可用性</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需特殊网络</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需特殊网络</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需特殊网络</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API 生态</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最完善</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">成长中</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Google 生态绑定</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
国际三大模型横向对比（2026 年 8 月）

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>注意：国内使用的现实门槛

{class="mt-1"}
对于国内开发者来说，GPT、Claude、Gemini 的核心障碍是网络访问。虽然可以通过 Azure 代理、API 聚合平台等方式间接使用，但稳定性和合规性需要自行评估。如果你的项目对数据安全有严格要求，建议优先考虑国产模型。
:::

如果你还没亲手感过这三家的差别，送你一个一小时的体验方案，周末就能做。第一个二十分钟：打开能访问的任一家对话界面，把同一段你的真实任务（一段要改的文案、一段要调的报错）原样发给三家的免费档，把回答并排贴在一个文档里。第二个二十分钟：故意给一个刁钻问题，让它推荐一本不存在的书名相近的书、算一道多步应用题，观察谁会老实说"不确定"，谁在硬编。第三个二十分钟：用中文让它们各写一段面向国内用户的推广文案，感受"翻译腔"的差别。

做完这一小时，你对三强的理解会超过读十篇测评。因为测评是别人的任务，这一小时是你的任务，而你未来每天要服务的，恰恰是自己的任务。

#### 三强的技术路线差异：同一场比赛，三种跑法

看完三家的产品线，你可能会问：都是大模型，为什么用起来感觉完全不同？背后是三家公司在技术路线上实打实的分歧。这一节不带价格表，只讲"为什么"，理解了它，前面对比表里的每一行你都能看出来历。

##### 数据配方：模型的口味是喂出来的

各家训练数据的侧重点不同，具体配比是商业机密，但可以从行为反推个大概。GPT 的语料覆盖面广，从技术论坛到大众百科都有，所以它"什么都懂一点"，像博览群书的通才；Claude 在代码和长文档上的突出表现，业内普遍认为与其训练数据里工程语料的占比有关，像个科班出身、基本功扎实的工程师；Gemini 站在 Google 的搜索索引和产品数据之上，实时信息和跨语言检索是别人短期学不来的。

顺便提醒一句：网上时不时出现所谓"训练数据配方泄露"，听听就好。真实配方没人会公开验证，你唯一能依赖的证据是模型在你任务上的实际表现。

##### 性格养成：对齐方式决定它"敢不敢说"

同样一个问题，三家的回答风格差别明显，这来自对齐阶段的策略分歧。Claude 偏严谨保守：不确定就说不确定，给出答案时常附带边界说明：代价是有时显得啰嗦。GPT 走均衡路线，配合度高、风格百搭。Gemini 的安全策略曾经翻过车：2024 年它的人物图像生成因历史人物失真引发争议，官方随后收缩了策略，这个案例说明对齐不是"越严越好"，火候是一门手艺。

对齐没有标准答案。保守换来可靠，开放换来好用，各家付各自的代价。你能做的是按需选择：写法务函件，宁可要啰嗦但稳的；头脑风暴，要放得开的。

##### 思考方式：直觉派与深思派

近两年大模型最重要的技术分化，是"深思模式"的普及：让模型先在内部推理一长段，再给出答案，用更多计算换更准确的结论。三强都把"深思"做成了可选项——简单任务用快模型秒回，难任务开深思模式慢工出细活。

实用的判断标准：<strong>数学计算、复杂逻辑、多步规划，开深思；聊天、分类、改错别字，别开</strong>——又慢又贵，收益接近零。API 里这类开关各家叫法不同，有的叫思考预算，有的叫推理力度，参数名和取值范围以各家文档为准。新手常见错误是无脑全开深思，账单翻倍而效果没变化，月底才恍然大悟。

##### 生态入口：模型只是冰山一角

你选的不只是一个模型，还有它身后的一整套入口。ChatGPT 是一个超级应用：GPTs 商店、连接器、语音对话，像一个 AI 时代的操作系统。Claude 的重心在开发者侧：命令行工具、IDE 集成、MCP 协议，工具链深但普通用户感知不强。Gemini 长在 Google 全家桶和安卓系统里，搜索、邮箱、文档处处有它。

所以选型时多问自己一句：我每天的生产工具在哪一边？重度 Google 用户选 Gemini 顺理成章；以编程为生的开发者在 Claude 的工具链里如鱼得水；想要一个"什么都能干一点的 App"，ChatGPT 是舒服的选择。模型能力之争打成了生态入口之争，这跟手机厂商的打法，其实是一回事。

把前面几节的内容收成一张速查表，日常场景直接对号入座，记住这是"方向"不是"答案"，具体型号随行情变动。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">日常场景</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">首选方向</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">备选与说明</th></tr></thead><tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">日常聊天、翻译、查资料</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">任一国产 App 或免费档国际模型</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">差异不大，用得顺手最重要</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">编程开发</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude 系或 DeepSeek</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">预算敏感选 DeepSeek；配编程工具用更顺手</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">长文档、整库分析</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gemini、Kimi 或 Claude</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">看上下文窗口和检索能力</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">图表、票据、拍照理解</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gemini 或 Qwen 多模态档</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">中文票据国产更稳</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">高并发跑量（分类、提取）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek Flash、qwen-turbo 等轻量档</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">单价优先，质量要求放低</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">学生项目、原型验证</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">送免费额度的国产平台</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">先跑通，再谈升级</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">企业敏感数据</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">支持私有化部署的国产模型</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">合规先行，法务介入</td></tr>
</tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
日常场景选型速查（方向性建议，具体以现价与实测为准）

#### 二、国产主流大模型：百花齐放

2026 年的国产大模型已经从"追赶者"变成了"并跑者"，在某些领域甚至实现了"领跑"。与 2023 年"套壳"争议不同，2026 年的国产旗舰模型在逻辑推理、代码生成、中文理解等方面已经与国际一线模型旗鼓相当，差距缩小到个位数。更重要的是，国产模型在中文场景、价格成本和合规部署上有不可替代的优势。

对大多数国内用户来说，接触不是 API，是手机 App，豆包、Kimi、DeepSeek 的应用装上就能用，不需要特殊网络，这本身就是国产模型贴近用户的一种体现。不是"自己聊天"，是"让自己的程序会用 AI"，API 才是正门，这一章的后半部分会带你走进去。

这个变化是怎么发生的？时间线值得简单捋一遍。2023 年前后，国产模型与国际第一梯队的差距肉眼可见，"能聊天"和"能干活"之间隔着一道沟；2025 年初 DeepSeek-V3 用远低于同行的成本训练出接近一线的能力，把"强模型必须烧天量算力"的迷思打破了；到 2026 年，各家旗舰在推理、代码、中文理解上已经和国际三强互有胜负。差距从"代际"缩小到"个别项"，这是本轮格局最大的变化。

##### 1. DeepSeek V4：性价比之王

DeepSeek（深度求索）是国产大模型中现象级的存在。2025 年初，DeepSeek-V3 以"比 GPT 便宜十分之一但能力相当"的定位震撼市场，被业内称为"通用 AI 大模型斩杀线"<strong>比它便宜的没它好用，比它贵的没它量大管饱</strong>。到 2026 年 8 月，DeepSeek V4-Pro 正式版发布：1.6 万亿参数 MoE 架构，激活约 49B，支持 100 万无损上下文，代码性价比被广泛认为是全球天花板。

"MoE 架构"这个词出现了，值得用一句话讲明白。MoE（混合专家）可以想成一家大医院的会诊制度：模型内部有一大群"专科医生"，每个问题只请最相关的几位出场，其余休息。1.6 万亿参数是全院编制，激活约 49B 是这次实际出诊的人数<strong>编制大，出诊少，这就是便宜的秘密</strong>。理解了这一点，你就理解了为什么各家旗舰纷纷转向 MoE：能力要堆，成本要省，只能这样设计。

DeepSeek V4 在 Agent 能力上实现了大幅跃升——DeepSWE 基准从 12.8 跳至 62.7（+390%），NL2Repo 从 38.5 升至 61.5。API 新增了 Responses API 与 Anthropic API 双协议支持，已兼容 Codex 和 Claude Code 等主流编程工具。这意味着你可以用 DeepSeek 的 API 替代 Claude 的 API，在 Claude Code 中使用<strong>成本降低数倍，体验几乎一致</strong>。

双协议兼容这件事，再给你一个具体画面：你不需要改写任何业务代码，只要在编程工具的配置里把接口地址换成 DeepSeek 提供的兼容端点、钥匙换成 DeepSeek 的 Key：同一个工具，脑子换成了更便宜的那颗。国产厂商争着做这种兼容，是因为切换成本每低一分，用户流动就多一分。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">型号</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">定位</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">输入(/百万Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">输出(/百万Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">上下文窗口</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek V4 Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">旗舰推理</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3元 (约US$0.43)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6元 (约US$0.87)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">100万Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek V4 Flash</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">轻量快速</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1元 (约US$0.14)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2元 (约US$0.28)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">100万Token</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
DeepSeek V4 系列定价（2026 年 8 月，促销价）

价格对比：同样 100 万 Token 的输入 + 100 万 Token 的输出，DeepSeek V4 Flash 花费约 0.42 美元，GPT-5.6 Sol 花费约 35 美元，Claude Fable 5 花费约 60 美元。<strong>差距高达 80-140 倍</strong>。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>避坑提醒：DeepSeek 要涨价了

{class="mt-1"}
DeepSeek 官方已于 2026 年 8 月 6 日公告"计划近期大幅上调 API 定价"，促销价可能不会持续太久。调价已于 2026 年 8 月中旬落地：输入、输出、缓存全面上调（涨幅 50%–1100%，缓存命中涨幅最大），峰谷定价的规则是"低谷半价"而非"高峰翻倍"，现价以 api-docs.deepseek.com 的价格页为准。
:::

涨价落地之后怎么办？三个动作。第一，重新读一遍峰谷规则：低谷时段半价，批处理、跑评测这类不看钟点的任务挪到低谷跑，能省不少，具体时段以官方文档为准。第二，把缓存用足，固定前缀的任务缓存命中价格仍远低于普通输入。第三，做一次比价：调价之后 DeepSeek 相对国产同档的价位优势是否还成立，答案要每个月重算，别用老印象做决定。

##### 2. 通义千问 Qwen3.7 Max：阿里云的企业级选择

阿里云的通义千问（Qwen）系列依托阿里云生态，在企业级部署上有天然优势。2026 年 7 月的 Qwen3.7 Max 是当前旗舰：235B 参数稠密模型，256K 原生上下文，可扩展至 1M。Qwen 的核心优势在于：开源生态成熟（从 7B 到 235B 全系列开源）、中文场景理解精准、与阿里云基础设施深度集成。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">型号</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">输出价格(/百万Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">适用场景</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen-turbo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">0.6元</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">极简问答、文本分类、高并发</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen-long</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.0元</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">10M 超长上下文处理</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen3.7-flash</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">7.2元</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">通用对话、内容生成</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen3.7-plus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">12.0元</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多模态（图片+视频）、中文创作</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen3.7-max</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">36.0元</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">旗舰中文能力、复杂任务</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
通义千问 Qwen 系列阶梯定价（2026 年 8 月）

Qwen 的定价采用阶梯策略，从极低成本的 qwen-turbo（输出 0.6 元/百万 Token）到旗舰 qwen3.7-max（输出 36 元/百万 Token），覆盖从轻量问答到复杂推理的全场景需求。对于已经在使用阿里云的企业，Qwen 是最顺手的集成选择。

阶梯定价的用法一句话概括：<strong>让任务和模型门当户对</strong>。分类、打标签这种活儿交给 turbo，成本几乎可以忽略；超长文档交给 qwen-long，别硬塞给旗舰；真正需要深度推理的决策类任务再上 max。不少人图省事所有调用都用 max，月底账单会替他补课。另外 Qwen 的开源版本可以在自己的服务器上部署：数据不出内网，这对很多公司是"能用"与"不能用"的分界线。

##### 3. 智谱 GLM-5.1：国产 SWE-bench 第一

智谱 AI 的 GLM 系列在 2026 年表现亮眼。GLM-5.1 在 SWE-bench 上拿下<strong>国产第一</strong>的成绩：744B MoE 稠密混合架构，支持 100 万上下文。它的特点是中文语义理解精准，支持国内合规私有化部署，这对数据安全要求高的金融、政务场景非常重要。GLM-5.1 的定价为输入 6 元、输出 24 元每百万 Token，处于国产模型中游水平。

看这个"国产第一"要带两个前提。其一，这是 8 月快照的成绩，榜单月月在变，冠军常换人，你该记住的是"GLM 在编程上处于国产第一梯队"这个量级判断，而不是那个名次。其二，SWE-bench 测的是"修复真实仓库 bug"的能力，它强不代表写新功能也强，评测和你的任务之间永远隔着一层，本章后面会专门讲怎么自己做小评测。私有化部署对金融、政务客户是硬需求：数据不出门，这条 GLM 一直守得住。

##### 4. Kimi K3：超长文本之王

月之暗面的 Kimi 系列以超长文本处理能力著称。2026 年 7 月发布的 Kimi K3 拥有 2.8 万亿参数规模，在多项复杂任务评测中进入全球第一梯队。Kimi 的核心场景是长代码库分析和长文档检索增强，它能处理整本书的文本或整个项目的代码，在"大海捞针"式检索任务中表现卓越。Kimi 的定价相对较高（输出约 12-20 元/百万 Token），但在长文本场景的性价比无人能及。

"大海捞针"是个什么测试？把一句话藏进几万字的文档深处，然后问模型这句话，它考的是长文本里"找得到"和"读得懂"两件事。Kimi 从出名的那天起就是这项技能的代表。适合它的典型任务：把一整个代码仓库丢给它做架构分析；几百页的研报让它交叉比对数据；一部小说让它梳理人物关系。反过来，如果你只是问"明天穿什么"，用它属于杀鸡用牛刀。

##### 5. 豆包 Doubao：字节跳动的全能选手

字节跳动的豆包系列在 2026 年表现稳定。Doubao Seed 2.1 Pro 是火山引擎旗舰模型，256K 上下文，在实测中综合发挥稳定，中文场景体验突出。豆包的优势在于：<strong>注册即送大量免费 Token</strong>，火山引擎生态集成完善，注册即送大量免费 Token，体验零门槛。对于想要快速体验 AI 编程的初学者，豆包是零门槛的入门选择。

"注册即送大量免费 Token"对初学者的意义，值得单独说一句。你第一次接 API 时会犯各种各样的错：Key 放错位置、参数拼错、消息格式写反，这些学费如果有免费额度替你交，心态会完全不一样。很多人的第一次"调通了"就发生在豆包或另一家送额度的平台上。先跑通再优化，是正经的工程顺序，这一点都不丢人。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">对比项</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">DeepSeek V4</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Qwen3.7 Max</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GLM-5.1</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kimi K3</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">豆包 2.1 Pro</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">综合得分</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">87.5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">89.7</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">90.5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">88+</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">85+</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">编程能力</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">极强</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">强</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">国产SWE第一</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">强</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">中上</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">中文理解</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">优秀</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">优秀</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">精准</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">优秀</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">优秀</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">上下文窗口</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">100万</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256K-1M</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">100万</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">超长</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256K</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">输出价格(元/M)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">36</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">24</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">12-20</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">30</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">开源</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MIT协议</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全系列开源</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">部分开源</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">闭源</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">闭源</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">私有化部署</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">支持</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">支持</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">支持</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不支持</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不支持</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
国产五大模型横向对比（2026 年 8 月）

一个重要的趋势是：<strong>国产模型与 GPT/Claude 的"代差感"已经消失</strong>。在逻辑推理和数学竞赛上，国产旗舰与 GPT-5 的分差基本在个位数。在系统化架构思维和复杂工程推理上，Claude 仍然领先：它能给出更有"灵气"的架构方案，而国产模型有时显得"教条"。但在中文场景、成本控制和合规部署上，国产模型有压倒性优势。

::: div .figure
```html
<svg aria-hidden="true" style="max-width:100%;height:auto" width="620" height="290" viewBox="0 0 620 290" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="620" height="290" rx="8" style="fill:var(--ink-inverse)" />
      <line x1="70" y1="230" x2="590" y2="230" stroke-width="1.5" style="stroke:var(--muted)" />
      <line x1="70" y1="230" x2="70" y2="20" stroke-width="1.5" style="stroke:var(--muted)" />
      <line x1="70" y1="60" x2="590" y2="60" stroke-width="1" stroke-dasharray="4,4" style="stroke:var(--line)" />
      <line x1="70" y1="116" x2="590" y2="116" stroke-width="1" stroke-dasharray="4,4" style="stroke:var(--line)" />
      <line x1="70" y1="173" x2="590" y2="173" stroke-width="1" stroke-dasharray="4,4" style="stroke:var(--line)" />
      <text x="62" y="234" font-size="10" text-anchor="end" style="fill:var(--muted-2)">0</text>
      <text x="62" y="120" font-size="10" text-anchor="end" style="fill:var(--muted-2)">50</text>
      <text x="62" y="64" font-size="10" text-anchor="end" style="fill:var(--muted-2)">100</text>
      <text x="340" y="262" font-size="10.5" text-anchor="middle" style="fill:#374151">输出价格（元/百万Token）</text>
      <!-- bars: price -->
      <rect x="95" y="218" width="60" height="12" style="fill:var(--accent-book)" /><text x="125" y="212" font-size="9" text-anchor="middle" style="fill:#374151">6</text><text x="125" y="248" font-size="9.5" text-anchor="middle" style="fill:#374151">DeepSeek</text>
      <rect x="195" y="146" width="60" height="84" style="fill:var(--accent-book)" /><text x="225" y="140" font-size="9" text-anchor="middle" style="fill:#374151">36</text><text x="225" y="248" font-size="9.5" text-anchor="middle" style="fill:#374151">Qwen</text>
      <rect x="295" y="182" width="60" height="48" style="fill:var(--accent-book)" /><text x="325" y="176" font-size="9" text-anchor="middle" style="fill:#374151">24</text><text x="325" y="248" font-size="9.5" text-anchor="middle" style="fill:#374151">GLM</text>
      <rect x="395" y="200" width="60" height="30" style="fill:var(--accent-book)" /><text x="425" y="194" font-size="9" text-anchor="middle" style="fill:#374151">16</text><text x="425" y="248" font-size="9.5" text-anchor="middle" style="fill:#374151">Kimi</text>
      <rect x="495" y="170" width="60" height="60" style="fill:var(--accent-book)" /><text x="525" y="164" font-size="9" text-anchor="middle" style="fill:#374151">30</text><text x="525" y="248" font-size="9.5" text-anchor="middle" style="fill:#374151">豆包</text>
      <!-- scores -->
      <circle cx="125" cy="118" r="5" style="fill:var(--gold)" /><text x="140" y="114" font-size="9" style="fill:#78350f">87.5</text>
      <circle cx="225" cy="110" r="5" style="fill:var(--gold)" /><text x="240" y="106" font-size="9" style="fill:#78350f">89.7</text>
      <circle cx="325" cy="105" r="5" style="fill:var(--gold)" /><text x="340" y="101" font-size="9" style="fill:#78350f">90.5</text>
      <circle cx="425" cy="112" r="5" style="fill:var(--gold)" /><text x="440" y="108" font-size="9" style="fill:#78350f">88+</text>
      <circle cx="525" cy="116" r="5" style="fill:var(--gold)" /><text x="540" y="112" font-size="9" style="fill:#78350f">85+</text>
      <rect x="90" y="30" width="12" height="12" style="fill:var(--accent-book)" /><text x="108" y="41" font-size="9.5" style="fill:#374151">输出价格(越低越好)</text>
      <circle cx="170" cy="36" r="5" style="fill:var(--gold)" /><text x="182" y="40" font-size="9.5" style="fill:#374151">综合得分(越高越好)</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
图 4：五款模型的价格与性能对比（价格越低越好，得分越高越好）
:::

这张图想让你记住的不是五个数字，而是一个形状：<strong>价格和性能在国产阵营里不是简单的正相关</strong>。最便宜的 DeepSeek 拿着不低的综合分，价格靠前的豆包分数反而排在后面：因为豆包的优势在体验和生态，不在裸分。选模型看"匹配"，不看"排名"，这是本节最想让你带走的一句话。

#### 国产模型的崛起与差异化竞争

把五家模型放在一起看，你会看到一个比"谁分高"更有意思的问题：在一个国际三强占据用户心智的市场里，国产模型靠什么站稳了脚跟？答案不是"弯道超车"这类口号。答案是几条实打实的差异化路线。

##### 这一轮追赶为什么快

三个原因凑到了一起。工程效率上，MoE 架构、训练技巧这些关键方法有大量公开论文和开源实现，后发者可以站在公开知识上少走弯路，把成本打下来。开源策略上，国产厂商比国际同行更舍得开放模型权重。全球开发者帮忙找问题、做衍生，生态像滚雪球一样起来。场景贴近上，中文互联网的语料、本土应用的交互习惯，本来就是国产厂商的主场，这里没有时差，没有文化折扣。

三件事叠加，结果就是你在上一节看到的：能力并跑、价格更低、场景更熟。这不是某一项技术的胜利，是路线选择的胜利。

##### 差异化的三张牌：价格、中文、合规

<strong>价格牌</strong>：即便 DeepSeek 调价落地，国产阵营的整体单价仍然显著低于国际旗舰——但差距的具体倍数在动态变化，别背旧数字。价格优势的来源也不神秘：更高效的架构、更激烈的国内竞争、以及"先用低价换生态"的策略。

<strong>中文牌</strong>：不只是"会说中文"，而是懂中文语境——公文腔、行业黑话、成语典故、网络热梗，国产模型的理解普遍更到位。还有一个容易被忽略的技术点：分词效率。同样的中文文本，在国产模型里通常消耗更少的 Token（各家分词器不同，具体比例有差异），这笔账直接反映在你的账单上。

<strong>合规牌</strong>：模型备案齐全、支持私有化部署、数据不出境——这三条在企业采购里是硬门槛，不是加分项。很多行业（政务、金融、医疗）的采购清单上，"是否可私有化"直接决定候选名单，国际模型在这一栏经常直接出局。

三张牌叠在一起，构成了国际模型短期内难以复制的护城河。这不是"国产吊打国际"或"国际遥遥领先"，是：在特定场景里，各有各的最优解。

顺手澄清几个流传很广的误区。<strong>误区一："国产模型都是套壳"</strong>——这是 2023 年的旧印象，如今国产旗舰在模型架构层面有自己的原创设计，国际同行的论文里也开始认真引用和分析它们，"套壳"叙事早该翻篇了。<strong>误区二："便宜等于低质"</strong>——国产模型价格低的主要来源是架构效率和激烈竞争，不是能力阉割，上一节的对比表就是证据。<strong>误区三："开源就是免费随便用"</strong>——开源的是模型权重，商用条款以仓库的 LICENSE 为准，官方托管服务照常收费。<strong>误区四："私有化部署买来就能用"</strong>——私有化意味着你还要自己准备算力、运维和升级，这笔账对中小团队未必划算，用官方托管服务往往是更现实的选择。

##### 开源与闭源：两条路线的分岔

"开源"两个字在模型圈的含义，和软件圈不完全一样，值得单独澄清。模型开源开放的是权重：你可以下载模型文件，部署在自己的服务器上，在允许的范围内微调。但它不等于"免费"，官方托管的 API 照常收费，商用许可、二次分发的条款以各仓库的 LICENSE 文本为准，用之前花两分钟读一遍，比出事后打官司便宜得多。

两条路线各有利弊。开源路线（Qwen 全系列、DeepSeek 的开源版本、GLM 的部分型号）换来的是可控：数据不出门、可以深度定制、不怕服务商停服。闭源路线（Kimi、豆包的旗舰）走的是在线迭代，能力上限通常更高、更新更快，但没有私有化选项。

给你的判断标准就三句话：数据敏感、有运维能力，开源自部署；追能力上限、要省心——闭源 API；既想要开源模型的能力又不想管机器，各家官方的托管服务（模型是那个模型，机器是厂商的）。

#### 多模态能力：从"能看图"到"能干活"

前面的对比表里有一行"多模态能力"，这一节把它展开讲透。多模态是大模型近两年变化最大的方向之一，也是普通人最容易感知到的变化，毕竟"发张图给 AI 看"比"写一段话描述它"自然多了。

##### 三代多模态，一代一个台阶

第一代是拼接式：视觉模型负责看，语言模型负责说，中间靠一次"翻译"衔接。它让"AI 能看图"成为可能，但翻译损耗大，看复杂图表经常串行。第二代是原生式，大约从 2024 年前后开始，主流旗舰陆续转向图文一体的训练方式，模型直接"看懂"图像，不再经过转述。第三代正在发生：从"看懂"到"动手"，图像生成、视频理解、屏幕操作（智能体直接操作界面完成任务）陆续落地，具体能力边界各家不同，以官方发布为准。

三代之间不是替代关系。今天的旗舰模型大多是"原生打底、动作能力往上加"，而拼接式的老思路仍然活在很多低成本方案里。你不需要记住三代的名字，只需要在选模型时问一句：我要的到底是"看得懂"还是"会动手"？前者看多模态理解评测，后者看智能体能力。

##### 现在真正好用的多模态场景

宣传里的多模态天花乱坠，实践里真正好用的场景是这几个。

- <strong>票据与表格 OCR</strong>：发票、快递单、报表拍照转结构化数据，成熟度最高，国产模型对中文票据的识别尤其稳。
- <strong>图表理解</strong>：把柱状图、折线图拍给模型，问趋势、问异常值，开会前快速摸清一份图表的神器。
- <strong>截图转代码</strong>：前端把设计稿截图发给模型，生成页面框架，细节要调，但八成骨架有了。
- <strong>手写识别</strong>：会议白板、课堂笔记拍照转文字，学生党和咨询顾问的高频刚需。
- <strong>视频要点提取</strong>：把一小时的录屏或课程压缩成几分钟的摘要，能力强但成本也高，适合重点内容，不适合日常跑量。

##### 多模态调用的成本与坑

坑主要有三个。第一，图片按 Token 计费，分辨率越高消耗越大，具体换算规则各家不同，以官方文档为准——"随手一张 4K 原图扔过去"是常见的账单刺客，能用压缩图就别用原图。第二，一次传多张图时顺序有讲究，"第一张""第二张"的引用依赖你上传的顺序，乱了张冠李戴。第三，视频理解的成本远高于图片，长视频先切片或抽帧再处理，别整段硬塞。

拿一个真实场景感受一下多模态的用法。一家小超市的老板娘，每天晚上十点关店后要整理当天的进货单据，过去是人工敲 Excel，一敲敲到十一点半。现在的做法：把单据一沓拍下来发给多模态模型，提示词就一句"把这些单据里的品名、数量、单价、金额整理成表格"，回来直接粘进记账表。准确率不是百分之百，但她养成了"数字对不上就人工复核那一条"的习惯，十分钟收工。这个案例里最值得学的不是模型多强，而是<strong>她给多模态输出留了复核环节</strong>——信任但抽查，是多模态落地的正确姿势。

还有一条红线必须写在这里：身份证、合同、病历这类含个人敏感信息的图片，上传前先想清楚数据流向。普通云模型的 API 调用意味着数据离开了你的设备；合规敏感的场景，用支持私有化部署的国产方案，或者干脆人工处理。

对这本书的读者来说，多模态还有一层特殊意义：手机是天然的采集器，"拍下来问 AI"是手机上最自然的使用入口。第 41 章讲过的各类 AI 编程工具、以及手机自带的 AI 功能，背后用的就是这一节讲的能力，理解了能力边界，你就知道哪些手机上的"AI 功能"是真有用，哪些只是发布会上的词。

#### 跑在手机里的模型：端侧的另一个战场

云端模型讲完了，还有一个和这本书主题最贴近的战场：跑在手机本地的端侧模型。前面讲的所有模型都长在数据中心里，你的请求要出门、要排队、要按 Token 付费；端侧模型就住在你的手机芯片里，不联网也能用。

##### 为什么手机厂商都在卷端侧

端侧模型的参数规模远小于云端旗舰，通常在几十亿参数量级上下（具体视机型与系统版本而定），靠手机芯片里的 NPU（神经网络处理单元）来跑。它有三个云端给不了的好处：<strong>隐私</strong>——数据不出手机，摘要一条刚收到的短信、分析一张本地相册的照片，厂商和模型服务商都碰不到内容；<strong>离线</strong>——飞行模式下不少 AI 功能照样能用；<strong>即时</strong>——没有网络延迟，也没有调用费用。

这也是为什么主流手机厂商这两年都在自研或合作训练端侧模型：它成了旗舰手机的新卖点，和当年的摄像头像素是一个位置。各家端侧模型的底细（自研还是合作、基于什么架构）发布会上学问很多，判断实际水平别听参数，直接用，让它现场摘要一段长文、改一封邮件，能力高低一试便知。

##### 端侧和云端怎么配合

现阶段几乎所有手机 AI 功能用的都是"端云混合"架构：系统先判断任务难度，简单、敏感、要求快的走端侧，复杂、创意、需要联网信息的走云端。你感知不到这条分界线，但有两个办法可以摸到它：一是看功能说明，标注"本地处理"或"离线可用"的就是端侧；二是开飞行模式试一下，还能用的自然是本地的。

这个配合关系对你有实际意义：涉及隐私的轻任务（通知摘要、照片搜索），优先确认它走的是端侧；真正吃能力的重任务（长文写作、代码生成），端侧小模型会露怯，该连云就连云。把端侧当"贴身随从"，把云端当"外请专家"，分工就顺了。

三个动作，摸清你手机的 AI 底细。第一步，翻设置：在系统设置里搜"智能助手""AI"或各家功能名，找说明文字里的"本地""端侧""离线可用"字样：厂商会写明哪些处理在设备上完成。第二步，开飞行模式实测：把 Wi-Fi 和移动数据都关掉，挨个试 AI 功能，还能用的就是端侧在干活。第三步，看响应速度：不联网还能秒回的，基本是本地小模型的功劳。各家入口和名称不同。视机型与系统版本而定，但这三个动作通吃所有品牌。

##### 给你的现实预期

别拿端侧模型的能力去衡量一部手机 AI 的上限：它天生是"小而快"的选手。同一部手机，同样的 AI 功能，连云之后的回答质量通常明显高一截，这不是你的手机不行，是那颗几亿到几十亿参数的小脑子确实装不下旗舰模型的本事。反过来，也别小看端侧：它让"AI 功能不联网也能用、隐私数据不出门"从口号变成了日常。

桌面这边，端侧的故事推进得更快。2026 年的苹果芯片 Mac 已经能在 Xcode 里下载并运行本地模型，Ollama、LM Studio 这类工具也把"在自己电脑上跑模型"的门槛降到了几条命令。本章第三节讲模型选择时会回到这个话题：本地模型已经是值得认真考虑的第五个选项。

#### 三、模型选择决策框架

了解了各模型的特点后，如何为自己的项目选模型？这里送你一套<strong>"四问决策法"</strong>——回答四个问题，就能锁定最适合你的模型。

四个问题各有讲究，逐个拆开说。第一问是部署地，它其实是在问合规与网络：你的用户在国内，就别把稳定性押在"特殊网络"上，国产模型是默认答案；项目本身面向海外市场，海外模型才有生态优势。第二问是任务类型，编程是当前各家差距最大的单项，值得单独挑模型；聊天、写作、翻译这类通用任务，各家差距不大，价格反而是更好的筛选器。第三问是上下文长度，很多新手高估了它，日常任务几万 Token 就够了，真要整库整书地读，才轮到 Gemini 和 Kimi 出场。第四问是预算，它的作用是把你从"旗舰信仰"里拉出来：先用便宜模型跑通，跑不通再升级，这个顺序反过来就是烧钱。

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-globe mr-1"></i> 你的项目在国内还是国际部署？</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">国内 → 选国产模型</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">国际 → 可选海外模型</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-laptop-code mr-1"></i> 核心任务是编程还是其他？</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">编程 → Claude 或 DeepSeek</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">其他 → 继续判断</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-book mr-1"></i> 需要超长上下文(&gt;50万Token)？</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">需要 → Gemini 或 Kimi</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">不需要 → 继续判断</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-coins mr-1"></i> 预算敏感吗？</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">敏感 → DeepSeek 或 Qwen-turbo</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">不敏感 → GPT-5.6 或 Claude</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
图 5：大模型选择四问决策法
:::

拿三个真实场景走一遍这套决策法，你感受一下它的用法。场景一：大学生做毕业设计，一个人写一个数据看板，没预算。四问答完，国内部署、任务是编程、上下文不需要超长、预算敏感，答案是 DeepSeek 或 GLM 的按量付费，加上各家赠送的免费额度做测试，几乎零成本。场景二：公司内网的知识库问答，数据敏感、不能出内网。第一问就直接锁死了答案：国产模型里支持私有化部署的那几家，具体选型看运维团队的技术栈。场景三：自媒体运营，每天要把视频转成图文。多模态是刚需，上下文不用超长，预算中等，Qwen 的多模态档或豆包，再配一个便宜的文本模型做后续润色。三个场景，没有一个需要买最贵的旗舰。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：组合策略

{class="mt-1"}
这个决策法不是教条：很多场景需要组合使用多个模型。一个常见的组合策略：用 DeepSeek 或 Qwen 做日常开发（成本低、中文好），用 Claude 做关键架构设计（推理强、幻觉低），用 Gemini 做多模态分析（图像视频处理）。按需切换模型，而不是"一个模型用到死"。
:::

组合策略再往深一层，是"按环节组合"：同一个项目里，数据清洗用便宜模型，核心逻辑用强模型，最终润色再用一次强模型。好比做菜，洗菜切菜不必请主厨，掌勺的那一步才值得。

还有一个低成本的配套习惯：给自己建一份"模型档案"。开个文档，每次换模型就记三行，任务是什么、用了哪个型号、效果和成本感受如何。三个月后回头看，你会发现自己项目的"主力模型"是怎么一步步选出来的，这份记录比任何外部榜单都贴合你的实际。

还有第五个选项：模型干脆不跑在云上。2026 年本地模型确实可用了，Apple 芯片的 Mac 上，Xcode 26 已支持下载并运行本地模型；Ollama、LM Studio 这类工具也让"代码不出本机"成为可选项。代价是速度和能力都逊于云端旗舰，换来的是隐私和零调用费。要处理敏感数据，或者只想离线跑个小任务时，值得一试。

对本地模型的预期也要摆正：普通笔记本能流畅跑的是几十亿参数量级的小模型，能力相当于旗舰的前几年水平，简单任务够用，复杂任务会露怯；真正接近旗舰能力的模型需要专业级显卡，那是另一笔预算。所以本地的正确定位是"隐私兜底"和"离线备胎"，不是主力。

#### 怎么读"跑分"：评测的能与不能

这一章出现了不少分数和名次，有必要专门提醒一句：<strong>评测是地图，不是领土</strong>。榜单能帮你缩小选择范围，但照着榜单选模型翻车的例子，每周都在发生。三个最常见的坑，都在这里。

##### 坑一：基准污染

基准测试的题目大多来自公开数据集，而模型训练时见过很多互联网文本，考题可能已经在训练数据里。就像考前背过题库，分数高不代表会做题。各家都在用更私有的动态题库缓解这个问题，但"分数虚高"的可能性始终存在。看到离谱的高分，先冷静半秒。

##### 坑二：刷榜与选择性汇报

发布会上的分数都是精心挑选的：挑自家最强的基准、最有利的版本，有时还是内部评测集。两家厂商各自宣布"第一"可以同时成立：因为他们考的卷子不一样。看到"某某第一"，先问三个问题：谁出的题、什么时间测的、和谁比的。这三个答案齐了，那个"第一"才有信息量。

##### 坑三：你的任务不在考纲里

SWE-bench 测的是修复真实仓库的 bug，不测写文档；长文本评测测"找得到"，不测"读完后的判断力"。榜单上分差在个位数以内的模型，在你的任务上体感可能是打平甚至反转。所以，<strong>别人卷别人的，你要自己考</strong>：拿十个你自己的真实任务，让候选模型各跑一遍，遮住名字盲看结果，五分钟的土办法，胜过任何榜单。这也正是前面 Claude 一节说"看趋势别背单个数字"的用意。

#### 四、API 调用入门：从零开始接入大模型

很多 AI 编程教程只教你怎么用对话界面，但真正的"AI 编程"：让你的应用调用大模型，需要通过 API。API（Application Programming Interface，应用程序编程接口）是程序之间的通信协议。通过 API，<strong>你的代码可以像调用一个函数一样，调用大模型的能力</strong>。

##### 1. 什么是 Token

在了解 API 之前，必须先理解 "Token" 这个概念。Token 是大模型计费的基本单位，可以理解为 <strong>"AI 的阅读和写作单位"</strong>。一个 Token 大约对应：英文中 0.75 个单词（4 个字符），中文中 0.5-1 个汉字。一段 1000 字的中文文本，大约消耗 1500-2000 个 Token。

Token 不是字数，也不是字符数。大模型使用专门的分词器（Tokenizer）将文本切分成 Token。同一个词在不同模型中的 Token 数量可能不同，比如"人工智能"在 GPT 中可能是 3 个 Token，在 DeepSeek 中可能是 2 个。大多数模型的 API 会返回实际消耗的 Token 数量，你可以在 API 响应中查看。

两个实务要点。第一，上下文窗口和计费是联动的：窗口 100 万 Token 意味着"装得下"，不代表"装下也便宜"，每次调用都按实际 Token 数计费，长文本一次就是一笔钱。第二，想知道一段文本到底多少 Token，不用猜：各家平台的开发者文档里都有 Token 计算器，粘贴进去直接显示，写代码前先算一遍，心里就有账了。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Token 成本快速估算

{class="mt-1"}
100 万字中文约等于 150 万 Token。用 DeepSeek V4 Flash 处理百万 Token 输入 + 百万 Token 输出，成本约 0.42 美元（约 3 元人民币）；用 Claude Fable 5 处理同样的量，成本约 60 美元（约 434 元人民币）。<strong>这就是为什么模型选择直接影响你的项目成本</strong>。
:::

##### 2. 获取 API Key

使用大模型 API 的第一步是获取 API Key，一串用于身份验证的密钥。每个模型提供商都有自己的 API 平台，你需要注册账号并创建 API Key。以下是主流模型的 API 平台入口和获取流程：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">模型</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">API 平台</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">获取流程</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">免费额度</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">platform.deepseek.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">注册 → 实名认证 → 创建 API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新用户赠送额度</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">通义千问</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">bailian.aliyun.com（百炼平台）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">阿里云账号登录 → 开通服务 → 创建 Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新用户免费试用</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">智谱GLM</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">open.bigmodel.cn</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">注册 → 实名认证 → 创建 API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新用户赠送额度</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kimi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">platform.moonshot.cn</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">注册 → 实名认证 → 创建 API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">有限免费额度</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">豆包</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">volcengine.com（火山引擎）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">注册 → 开通方舟 → 创建 API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">注册送大量 Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenAI GPT</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">platform.openai.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">注册 → 绑定信用卡 → 创建 API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">无免费额度(需付费)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Anthropic Claude</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">console.anthropic.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">注册 → 绑卡 → 创建 API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新用户少量额度</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
主流模型 API 平台及 Key 获取方式（2026 年 8 月）

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>安全提示：API Key = 钱包密码

{class="mt-1"}
API Key 等同于你的钱包密码，任何拿到 Key 的人都可以用你的额度调用模型。因此：<strong>永远不要把 API Key 写在代码中</strong>（用环境变量管理）；永远不要把含 Key 的代码提交到公开的 Git 仓库；永远不要在社交媒体分享含 Key 的截图；也别把 Key 贴进给模型的提示词，智能体有文件系统权限时，多检查一眼配置文件，别让它跟着上下文跑出去。如果 Key 泄露了，立即在平台上删除并重新创建。
:::

"用环境变量管理"具体怎么操作？两套系统各给你一条路。Windows：在开始菜单搜"编辑账户的环境变量"，新建一个变量，名字比如 DEEPSEEK_API_KEY，值粘贴你的 Key，确定后重开终端生效。macOS 或 Linux：在终端执行 export DEEPSEEK_API_KEY="你的Key"（写进 ~/.zshrc 或 ~/.bashrc 可以永久生效），然后用 echo $DEEPSEEK_API_KEY 验证。一次性花两分钟配好，之后所有代码都能安全地引用它：本节后面的示例代码，读的都是这个环境变量。

##### 3. 第一次 API 调用

获取 API Key 后，你可以用任何编程语言调用大模型 API。以下用 Python 演示一个最简单的调用，向 DeepSeek 发送一条消息并获取回复。

::: div .code-block
:::inline div .code-head
<span>PYTHON · 第一次 API 调用</span><span class="dots">···</span>
:::

```
# 安装SDK：pip install openai
# DeepSeek兼容OpenAI SDK格式，可以直接用
from openai import OpenAI
import os

# 1. 创建客户端（API Key从环境变量读取）
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 2. 发送请求
response = client.chat.completions.create(
    model="deepseek-chat",  # 指定模型
    messages=[
        {"role": "system", "content": "你是一个Python编程助手。"},
        {"role": "user", "content": "写一个快速排序函数。"}
    ]
)

# 3. 获取回复
print(response.choices[0].message.content)

# 4. 查看Token消耗
print(f"输入Token: {response.usage.prompt_tokens}")
print(f"输出Token: {response.usage.completion_tokens}")
print(f"总Token: {response.usage.total_tokens}")
```
:::

这段代码的核心逻辑是：<strong>创建客户端（携带 API Key 和模型地址）、构造消息列表（system 设定角色，user 是用户输入）、发送请求、获取回复</strong>。这个模式几乎适用于所有兼容 OpenAI 格式的模型，只需要更换 api_key 和 base_url 就能切换模型。这就是为什么很多国产模型选择兼容 OpenAI SDK 格式：开发者只需改两行代码就能切换模型，迁移成本极低。

以下是切换到其他模型的代码差异：注意只需要改两行：

::: div .code-block
:::inline div .code-head
<span>PYTHON · 切换模型只需改两行</span><span class="dots">···</span>
:::

```
# DeepSeek
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
# model="deepseek-chat"

# 通义千问（百炼平台）
client = OpenAI(
    api_key=os.environ.get("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
# model="qwen-plus"

# 智谱GLM
client = OpenAI(
    api_key=os.environ.get("GLM_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4"
)
# model="glm-4"

# OpenAI GPT
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    # base_url使用默认值即可
)
# model="gpt-5.6-terra"
```
:::

代码里那几个参数，单独说清楚。temperature（温度）控制输出的随机程度：低温度像严谨的会计，同样的输入给同样的输出，适合摘要、分类、代码；高温度像即兴的诗人，输出更有变化，适合创意写作。max_tokens 是输出长度的上限，既是成本闸门，也是防跑偏的缰绳。至于 messages 里的三种角色，system 是导演，在幕后定调；user 是用户的台词；assistant 是模型之前说过的话，多轮对话时由你负责把它重新递回去。这套角色机制，本节第 7 小节会再展开。

##### 4. 流式响应处理

在实际应用中，你通常不希望等 AI 写完所有内容才一次性显示：那会让用户等太久。流式响应（Streaming）可以让你在 AI 生成的同时逐字显示，大幅提升用户体验。就像打字机一样。字一个一个蹦出来，用户的感觉是完全不同的。

::: div .code-block
:::inline div .code-head
<span>PYTHON · 流式响应</span><span class="dots">···</span>
:::

```
# 流式响应：逐字输出
stream = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "写一个Python的冒泡排序教程"}
    ],
    stream=True  # 开启流式响应
)

# 逐块接收并打印
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)
# 输出会像打字机一样逐字显示
```
:::

流式的原理一句话：服务器把生成中的文字切成小块，通过一条持续的连接逐块推给你（技术上叫 SSE，服务器推送事件），你的代码收到一块显示一块。两个实战细节：一是断流处理，网络中途断开时，已收到的部分通常保留，未生成的作废，代码里要捕获异常、把已有内容存下来，别让用户盯着白屏；二是并非所有场景都需要流式，批处理任务关掉流式，代码反而更简单。

##### 5. 工具调用（Function Calling）与 MCP

前面几节里，模型都只是在"回文本"。2026 年的模型还有一个关键能力：<strong>工具调用（tool use / function calling）</strong>——你提前登记一批函数（查天气、读数据库、发邮件都行），模型不直接回答，而是返回"请帮我调用这个函数，参数是这些"，由你的代码执行后把结果喂回去。智能体就是靠这层机制从"聊天"变成"干活"的。

::: div .code-block
:::inline div .code-head
<span>PYTHON · 一次工具调用的完整循环</span><span class="dots">···</span>
:::

```
# 工具调用四步循环：登记 → 意图 → 执行 → 回填
# 第一步：登记工具（示意，具体字段以官方文档为准）
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "查询指定城市的当前天气",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "城市名"}
            },
            "required": ["city"]
        }
    }
}]

# 第二步：发问，模型不直接回答，而是返回调用意图
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "北京今天适合跑步吗？"}],
    tools=tools
)
call = response.choices[0].message.tool_calls[0]
# call.function.name == "get_weather"
# call.function.arguments == '{"city": "北京"}'

# 第三步：你的代码执行真正的查询
weather = query_weather_api(city="北京")  # 你自己的函数

# 第四步：把结果回填给模型，让它组织成自然语言回答
messages = [
    {"role": "user", "content": "北京今天适合跑步吗？"},
    response.choices[0].message,
    {"role": "tool", "tool_call_id": call.id, "content": weather}
]
final = client.chat.completions.create(
    model="deepseek-chat", messages=messages, tools=tools
)
print(final.choices[0].message.content)
```
:::

盯住这段代码里最关键的认知：<strong>模型自己不执行任何函数</strong>。它只负责说"请帮我调用 get_weather，参数是北京"，真正动手的是你的代码。这个分工是安全设计的基石：模型有"意图"，你有"执行权"，危险的调用你可以审查、拦截、放行。所谓智能体，本质就是把第三步的执行权交得更彻底，同时配上更多安全审查。

再进一步，MCP（Model Context Protocol）把这件事统一了：工具按统一协议登记一次，Claude Code、Cursor 等多个智能体都能直接用，一次实现，处处接入。第三十九章已经把它当作上下文基础设施讲过，这里补上它在 API 层的样子。

补一句历史：MCP 这个协议 2024 年 11 月发布，之后迅速成为智能体生态的公共插座，各家编程工具、各家模型厂商纷纷接入。它的价值用充电口类比最好懂：以前每接一个新工具，要为每个智能体单独适配一遍；现在按统一协议登记一次，所有支持的智能体都能用。标准之争结束之后，所有人，包括你，都省下了重复造轮子的时间。

##### 6. System Prompt 优化：给模型立规矩的艺术

system prompt 是你唯一能"预先"影响模型所有输出的地方。写好它遵循一条朴素的原则：<strong>像写岗位说明书，而不是像许愿</strong>。一份够用的 system prompt 通常包含五个部分：角色（你是谁）、任务边界（管什么不管什么）、输出格式（长什么样）、约束（什么不能做）、示例（照这个样子来）。

给你一个可以直接改的骨架：「你是一个面向小商家的记账助手。只回答与记账、流水、库存相关的问题（边界）；每次回答先给结论，再给最多三条理由（格式）；不确定的数字必须标注"请以实际账目为准"，禁止编造（约束）。」几十个字到两三百个字，就够覆盖大多数场景。

三个优化手法。一是<strong>一次只改一处</strong>：同时改三处，效果变好了你也不知道是哪一处的功劳，下次没法复用。二是<strong>负面清单优于正面描述</strong>："禁止使用感叹号"比"请保持克制"有效得多，模型对明确禁令的执行远比对模糊形容词彻底。三是<strong>示例比形容词管用</strong>：与其写"简洁专业"，不如直接贴一段你理想中的输出。最后别忘了，system prompt 本身也占 Token：长提示放在消息列表开头，才能吃到缓存命中的折扣，这个联动下一节细讲。

##### 7. 多轮对话管理：messages 列表是你的责任

这是 API 时代新手最大的认知坑，值得用加粗体写：<strong>API 没有记忆</strong>。你以为模型"记得"前面的对话，实际上是你每次都把全部历史重新发送了一遍，messages 列表就是模型的全部记忆，它长什么样，模型就记得什么。理解这一点，很多"灵异现象"就都能解释了：为什么越聊越贵（历史越滚越长）、为什么模型忘了第一条约束（历史太长，早期内容被稀释）、为什么换个工具它就不认识了（那边的列表是新的）。

多轮管理的三板斧。第一斧，<strong>主动裁剪</strong>：保留 system、最近几轮完整对话、更早内容的摘要，把过时的工具返回结果（往往最占空间）替换成一行结论。第二斧，<strong>关键约束重复投放</strong>：每过几轮，把最重要的约束用一句话重新插进对话，对抗长上下文的稀释效应。第三斧，<strong>阶段切换时重开会话</strong>：一段任务做完，让模型自己总结进度和待办，新会话以这份总结开场——第四十三章讲的"总结-续接"技巧，在 API 层面就是重建 messages 列表。

##### 8. Token 优化：把每一分花在刀刃上

最后把 Token 优化的散装技巧收拢成一张清单，按见效快慢排序：

1. <strong>砍重复贴文</strong>：最常见的浪费是把同一段长文反复贴进对话。引用行号、贴摘要、用文件引用代替全文重贴。
2. <strong>约束输出格式</strong>：要求"只输出 JSON，不要解释"，输出单价比输入贵得多，省输出就是省大头。
3. <strong>历史摘要化</strong>：多轮对话里把十轮历史压成两段摘要（上一条讲的裁剪术）。
4. <strong>max_tokens 设闸</strong>：不需要长输出时显式限制，防止模型即兴发挥。
5. <strong>定期看用量面板</strong>：找出消耗 Token 前几名的调用，逐个优化，优化头部比优化长尾划算。

这套技巧的成本弹性很大：多数项目只做到前两条，账单就会明显下来一截。具体幅度取决于你的任务结构，别拿别人的百分比当自己的预期，你自己的用量面板才是唯一诚实的老师。

#### 五、Token Plan 购买指南

大多数模型提供商有两种计费方式：按量计费（Pay-as-you-go）和套餐订阅（Token Plan / Subscription）。理解这两种方式的区别，能帮你大幅降低使用成本。

##### 1. 按量计费 vs 套餐订阅

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">维度</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">按量计费(Pay-as-you-go)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">套餐订阅(Subscription)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">计费方式</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用多少Token付多少钱</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">预付固定费用，获得额度</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">适合场景</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">使用量不稳定、偶尔调用</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">使用量稳定、高频调用</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">价格优势</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">标准价</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">比按量低20%-50%</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">灵活性</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">随时可用，无需承诺</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需要预付，额度过期可能作废</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">超额处理</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自动按量计费</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">超出额度后转为按量计费</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">代表平台</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">各模型官方API平台</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenAI Plus/Pro, Claude Pro, Cursor Pro</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
两种计费方式的对比

对于初学者，建议<strong>从按量计费开始</strong>——不需要预付费用，用多少花多少。当你的月使用量稳定在一个水平后（比如每月超过 50 元），再考虑切换到套餐订阅以获得更低单价。

判断自己"用量形状"的方法很简单：按量用一个月，月底看两个数，总花费和调用次数。次数多、单次便宜，说明你是高频轻量型，套餐折扣对你友好；次数少、单次很贵，说明你在跑重任务，按量反而灵活。

##### 2. 主流订阅套餐一览

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">套餐</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">月费</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">包含内容</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">适合人群</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ChatGPT Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">免费</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Luna 无限文本对话</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">零基础体验</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ChatGPT Plus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$20/月</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Sol、图像生成、数据分析、GPTs 与连接器</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">中度使用者</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ChatGPT Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$200/月</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">无限制使用所有模型、优先访问新功能</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">重度专业用户</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">免费</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">有限次数Claude对话</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">零基础体验</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$20/月</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">无限制Claude使用、优先访问新模型</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">编程开发者</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">免费</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">有限次数AI补全和对话</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">初学者体验</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$20/月</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">无限AI补全；500次/月高级请求</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">日常开发者</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor Business</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$40/月/人</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">团队协作、管理后台、隐私模式</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">团队使用</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
主流 AI 工具订阅套餐（2026 年 8 月）

国内模型的订阅方案略有不同。DeepSeek 主要按量计费，没有月度订阅套餐，你充值后按实际使用量扣费。通义千问在百炼平台提供预付费资源包（购买一定量的 Token 额度，享受折扣价）。豆包在火山引擎上也有类似的预付费方案。对于国内开发者，最经济的组合通常是：<strong>DeepSeek 按量计费（日常开发）+ 豆包免费额度（体验测试）</strong>。

把视角拉高一点：订阅制、套餐含额度、按 token 计费、本地算力，是四种完全不同的账，别只盯着单价。重度使用智能体的人几乎都会撞到套餐额度上限，到时候的真实价格，是"超额后转按量"的那部分。建议先用一个真实项目跑一周。看清自己的用量形状，再决定上哪个档位。

订阅和 API 还有一个本质区别容易混淆：<strong>订阅买的是"交互使用权"，API 买的是"程序调用权"</strong>。你在 ChatGPT 网页上聊天，用订阅额度；你的程序半夜自动跑批，花 API 余额——两条线并行，互不通用。规划预算时把这两类需求分开列，能避免"为什么订阅了还要充 API"的困惑。

##### 3. API 聚合平台

如果你需要同时使用多个模型，API 聚合平台是一个省心的选择。聚合平台提供一个统一的 API Key，你就能调用全球几十种模型，无需在每个平台分别注册。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">平台</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">特点</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">价格优势</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">适合场景</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenRouter (openrouter.ai)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">海外聚合平台，一个Key调用全球模型</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">价格透明，支持实时比价</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需要灵活切换多个海外模型</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SiliconFlow (siliconflow.cn)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">国内聚合平台，提供多种国产模型API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">比官方低20%-30%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">国内开发者，多模型比价</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Azure OpenAI (微软代理)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">微软Azure代理的OpenAI API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Batch API可打5折</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">企业级OpenAI调用，大批量异步任务</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">百度千帆 (qianfan.baidubce.com)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">百度AI云平台，提供文心等模型</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新用户赠送额度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">百度生态用户</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
主流 API 聚合平台（2026 年 8 月）

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>避坑提醒：别买"共享 Key"

{class="mt-1"}
不要在淘宝、闲鱼等平台购买所谓的"共享 API Key"：这些 Key 通常来路不明，可能随时被封号，还有数据泄露风险。始终通过官方平台或正规聚合平台获取 API Key。
:::

聚合平台的便利背后也有三笔隐性成本。所有请求经过中间层，数据多一方经手，敏感业务要读清楚它的隐私条款；模型版本更新可能滞后于官方，"最新款"未必当天上架；出了问题多一个排查对象，是你的代码、官方模型还是聚合层的锅？个人开发者和小团队用聚合平台很划算，企业级敏感业务请走官方直连或私有化。

##### 4. 成本优化策略

选对模型只是第一步，如何"用得省钱"同样重要。以下是几个经过实践验证的成本优化策略：

1. <strong>善用缓存命中</strong>。很多模型提供"缓存"功能，当你的请求中包含之前已经处理过的内容（如系统提示词），这部分只按极低价格计费。DeepSeek 的缓存命中价格仅为普通价格的 1/60。把固定的系统提示放在消息列表开头，可以最大化缓存命中。
2. <strong>分级路由</strong>——用便宜模型处理简单任务，贵模型处理复杂任务。比如用 DeepSeek V4 Flash 做文本分类（输出 2 元/百万 Token），用 Claude 做架构设计（输出 181 元/百万 Token）。一个项目里 80% 的调用可以用便宜模型。
3. <strong>限制输出长度</strong>。API 按输出 Token 计费，输出越长越贵。在不需要长篇大论的场景中，设置 max_tokens 参数限制输出长度，避免 AI"废话太多"。
4. <strong>使用 Batch API 处理非实时任务</strong>。如果你有大量不需要即时响应的任务（如批量数据标注、文档摘要），使用 Batch API 可以享受 50% 折扣。OpenAI 和 Azure 都提供这个功能。
5. <strong>监控 Token 用量</strong>。大多数 API 平台提供用量统计面板。定期查看用量分布，找出消耗 Token 最多的调用，针对性优化。一个小小的 Prompt 调整（比如把"请详细解释"改成"请用 3 句话解释"）可能节省 50% 的 Token。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">优化策略</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">节省幅度</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">实施难度</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">说明</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">缓存命中</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最高98%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">低</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把固定内容放在消息开头</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分级路由</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">50%-80%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">中</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">简单任务用便宜模型</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">限制输出长度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">30%-60%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">低</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">设置max_tokens参数</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Batch API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">50%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">低</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">非实时任务用批处理</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prompt优化</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">20%-50%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">中</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">精简Prompt，减少冗余</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
成本优化策略及效果（2026 年 8 月）

五招的优先级怎么排？看项目阶段。刚起步：只做缓存和监控这两招，成本结构还没定型，别过早优化；日调用上了规模：加上分级路由和 max_tokens 闸门，这两招要改代码，晚改不如早改；手头有大量离线任务：Batch API 是白捡的折扣，不拿白不拿。最后提醒一句：优化本身也耗人力，<strong>别用一小时的工程去省一分钱的 Token</strong>。

#### 成本优化的完整策略：从单次调用到全年预算

上一节的五招是"招式"，这一节给你"内功"，把成本控制从一次调用扩展到整个项目、整年时间维度的完整框架。

##### 单次调用的账

一个请求的成本公式很简单：输入 Token × 输入单价 + 输出 Token × 输出单价，再减去缓存折扣。控制两头：输入侧砍冗余（上一节的 Token 优化清单），输出侧设上限（max_tokens 和"只要结论"式的要求）。有一招几乎零成本：在提示里加一句"直接给答案，不要前言和总结"，既省 Token 又省你的阅读时间，一分钱工程都不用做。

##### 项目架构的账

到了项目层面，省钱靠结构而不是靠抠。四个常用结构：<strong>路由器模式</strong>——入口处先判断任务难度（甚至可以让一个便宜模型当"分诊台"），再分发到不同档位的模型；<strong>缓存层</strong>——相同前缀的请求（system prompt、固定文档）吃缓存折扣；<strong>结果复用库</strong>——相同问题命中缓存直接返回，成本为零；<strong>评测护航</strong>——换模型、改提示词之前先跑一遍固定测试集，防止"钱省了、质量砸了"。这四个结构加起来的工程量不大，但它们决定了你的成本曲线是陡是缓。

##### 全年预算的账

时间维度上，三件事值得制度化。<strong>按项目分 Key</strong>：每个项目用独立的 API Key，账单天然分账，谁的用量异常一眼可见。<strong>设限额和告警</strong>：在平台上设置消费上限和告警阈值，这是防"意外账单"的唯一保险，尤其是有智能体在自动跑的场景。<strong>每月十五分钟复盘</strong>：看一次用量分布，问三个问题，头部调用是谁、哪些任务可以降档、哪些前缀可以进缓存。成本优化不是一次性动作，是每月十五分钟的例行公事。

#### 六、实战：在项目中接入大模型 API

本章用一个完整的实战收尾：创建一个 <strong>"AI 摘要生成器"</strong>：用户输入一段长文本，调用大模型 API 生成摘要。这个实战会展示 API 调用的完整流程：环境配置、API 调用、错误处理、成本控制。

::: div .code-block
:::inline div .code-head
<span>PYTHON · ai_summarizer.py</span><span class="dots">···</span>
:::

```
# ai_summarizer.py - AI摘要生成器
import os
from openai import OpenAI

# 1. 配置（API Key从环境变量读取，绝不硬编码）
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def summarize(text: str, max_length: int = 200) -> dict:
    """生成文本摘要

    Args:
        text: 要摘要的原文
        max_length: 摘要最大长度（Token数）

    Returns:
        dict: 包含摘要和Token消耗信息
    """
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "system",
                    "content": "你是一个摘要生成器。"
                               "请用简洁的中文总结用户提供的文本。"
                               "摘要不超过3句话。"
                },
                {
                    "role": "user",
                    "content": f"请摘要以下文本:\n\n{text}"
                }
            ],
            max_tokens=max_length,  # 限制输出长度
            temperature=0.3  # 低温度=更稳定
        )

        return {
            "success": True,
            "summary": response.choices[0].message.content,
            "input_tokens": response.usage.prompt_tokens,
            "output_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

# 2. 使用示例
if __name__ == "__main__":
    long_text = """
    （粘贴一段长文本...）
    """

    result = summarize(long_text)

    if result["success"]:
        print(f"摘要: {result['summary']}")
        print(f"消耗Token: {result['total_tokens']}")
        # 估算成本：DeepSeek V4 Flash
        cost = result['total_tokens'] * 0.000004  # 约0.4分/千Token
        print(f"预估成本: {cost:.4f}元")
    else:
        print(f"出错了: {result['error']}")
```
:::

这段代码体现了 API 调用的几个好办法：API Key 通过环境变量读取，绝不硬编码在代码中；函数有清晰的文档和类型提示；设置了 max_tokens 限制输出长度；temperature 设为低值（0.3）以获得更稳定的输出；有完整的错误处理；返回 Token 消耗信息用于成本追踪。当你用 AI 来写这段代码时，可以告诉它这些要求，它完全有能力帮你实现。

往下一步的路线图也给你画出来：这个脚本可以直接挂进定时任务，每天早上自动摘要你订阅的专栏；套一层 Web 框架就是一个在线服务；结合第 41 章的智能体工具，它还能升级成"自动读文件、自动发邮件"的完整智能体。每一步都不需要推翻重来，这就是先把 API 跑通的价值。

还有一句给"不会编程"读者的定心丸：这一整段代码你不用手写。把本节开头那句需求原样发给任意一个编程助手，它几分钟就能生成、解释并帮你调试：这个"让 AI 帮你接 AI"的过程，本身就是对前几章方法论的实战复习。

行文至此补一句观察：这两年各家模型的差距肉眼可见地缩小，"它能不能读到正确的上下文"反而成了效果的分水岭——这正好接回第三十九章讲的上下文工程。

#### 模型的边界：哪些活儿先别交给大模型

整章都在讲"选哪个、怎么用"，还有半句必须说完：哪些活儿暂时别交。知道边界不是泼冷水，恰恰是把模型用好的前提，用错地方的信任，比不用更危险。

##### 需要"当下"的活儿

模型的知识停在训练那一刻，今天的汇率、刚发布的政策、正在进行的比赛，它默认都不知道。除非你明确使用了联网搜索或检索工具，否则别问模型"现在怎么样"，它要么用过时信息回答，要么编一个。这条对国产国际一律适用。

##### 需要精确与审计的活儿

大数乘法、财务对账、合同条款的最终表述，模型可以打草稿，但最终数字和措辞要过人的手或传统的计算工具。它的计算错误有个讨厌的特点：错得很自信，格式漂亮、语气笃定，扫一眼根本看不出来。审计级的活儿，让模型当助手，别让它当签字的人。

##### 责任落在你头上的活儿

医疗判断、法律意见、投资决策。这三类有个共同点：出了事，承担责任的是人，不是模型。模型在这些领域的正确定位是帮你理解概念、整理问题、准备问诊提纲，而不是给结论。把"模型说的"当成"专业意见"去执行，是这个时代最常见也最贵的新错误。

##### 你的"不可替代清单"

反过来也值得列一列：哪些活儿无论模型多强都该留给自己？定方向、做取舍、承担后果的决策，以及一切需要"为结果负责"的签字。工具越强，越要有人握着方向盘。本章教你把模型接进项目，接下来的章节会教你把对话本身修炼成一门手艺，那是和模型协作的另一半功夫。

#### 常见问题：选型与 API 实战 FAQ

<strong>问：我完全不会编程，这章是不是可以直接跳过？</strong>

答：看目标。只想把 AI 用得更好，读完前三节就够，API 部分等你需要"让程序自动干活"再回来。但建议别跳过 API 的概念本身：理解程序怎么调模型，你才知道哪些事能自动化、哪些不能。

<strong>问：要不要一开始就买最贵的旗舰订阅？</strong>

答：先别。免费层加国产按量 API 能验证绝大多数需求，等你的用量形状稳定了再谈订阅：反过来操作的人，大多在为用不上的额度买单。

<strong>问：模型更新换代这么快，我写好的提示词和代码会不会作废？</strong>

答：接口层面基本不会，OpenAI 兼容格式已经成为事实标准，换模型改两行。提示词可能需要微调：新模型上跑一遍老任务，看效果退没退化，退化再调。这也是为什么建议把测试集攒起来。

<strong>问：DeepSeek 涨价了，还有便宜的用法吗？</strong>

答：有。低谷时段半价，把批处理挪过去；缓存用足，固定前缀的折扣还在；再定期做一次同档比价，国产阵营竞争激烈，价格格局几个月一变。

<strong>问：上下文窗口 100 万 Token，是不是意味着我可以随便塞？</strong>

答：装得下不等于用得起，更不等于用得好。长上下文按 Token 收费，塞满一次就是一笔钱；而且内容太多，关键信息反而被稀释。能裁剪就裁剪，"喂得准"永远好过"喂得多"。

<strong>问：API 会不会被盗用？怎么防？</strong>

答：按前面讲的三条纪律来：环境变量管理、不进公开仓库、不贴进提示词。再加一道保险，在平台上设置消费限额和告警，就算 Key 泄露，损失也封得住顶。

<strong>问：多家模型的 Key 都注册了，管理起来太乱怎么办？</strong>

答：给自己立三条规矩：Key 的命名带上平台和用途（比如 DEEPSEEK_SUMMARIZER）；全部走环境变量，代码里不出现第二处；每季度清理一次不再用的 Key。乱的主要根源是 Key 散落在各种脚本里，收拢到环境变量这一步做完，乱象就解决了大半。

:::inline div .quote-line
本章的最终启示：模型是"弹药"，方法论是"战术"。选对弹药能让战斗更顺利，但没有好的战术，再好的弹药也打不赢仗。了解了各模型的特点和 API 使用方法后，你就有了一个充足的"弹药库"，但怎么打这场仗，还是要靠前几章学到的思维方法论。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：跑通你的第一次 API 调用

{class="mt-1"}
注册一个国产模型平台（推荐 DeepSeek 或智谱，都送新用户额度），创建 API Key，把它写进系统环境变量（而不是代码里！），然后运行上面"第一次 API 调用"的代码。看到 AI 的回复打印出来的那一刻，你就跨过了"用 AI"和"造 AI 应用"之间的分界线。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 国际三强：OpenAI GPT-6/5.6 系列（均衡全能）、Claude（编程主力）、Gemini（多模态+长上下文）
- 国产五强：DeepSeek V4（性价比之王，注意涨价公告）、Qwen3.7（企业级）、GLM-5.1（SWE国产第一）、Kimi K3（超长文本）、豆包（免费入门）
- 四问决策法：部署地点？编程还是其他？超长上下文？预算敏感？
- Token 是计费单位：中文 1 字约 1.5-2 Token；100万字约150万Token
- API Key = 钱包密码：环境变量管理，绝不硬编码、不上传Git
- 国产模型普遍兼容 OpenAI SDK：换模型只需改 api_key 和 base_url 两行
- 省钱五招：缓存命中、分级路由、限制输出、Batch API、监控用量
:::
