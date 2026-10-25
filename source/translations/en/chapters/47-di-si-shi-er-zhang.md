---
id: di-si-shi-er-zhang
num: 42
part: ai-biancheng-pian
nav: Chapter 42: The Large-Model Landscape and Hands-On API Practice
toc: default
kind: chapter
---

### Chapter 42: LLM Landscape and API Practice

{class="chapter-intro mb-4"}
Previous chapters covered how to work with AI. This one answers a more basic question: which AI, and how? By August 2026 the LLM landscape is rich — globally GPT, Claude, and Gemini compete; in China DeepSeek, Tongyi Qianwen, GLM, Kimi, and Doubao bloom. Each model has its own personality and strengths: pick right and you fly; pick wrong and you drag. This chapter introduces the models, shows how to wire them into your apps via API, and how to choose a Token Plan that fits your usage.

#### 1. Global major LLMs: the big three

As of August 2026, the international LLM market is a three-way race: OpenAI (GPT), Anthropic (Claude), and Google (Gemini). Each has a distinct personality — let's meet them one by one.

##### 1. OpenAI GPT-5.6 series: the all-rounder

OpenAI kicked off the LLM wave, and GPT remains the world's most widely used model family. The GPT-5.6 series, released July 2026, comes in three tiers: flagship GPT-5.6 Sol for high-end reasoning, balanced GPT-5.6 Terra for daily development, and lightweight GPT-5.6 Luna for high-throughput, low-cost scenarios. All three share a 1.05 million-token context window and support image input, function calling, and structured output.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Model</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Positioning</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Input (/1M tokens)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Output (/1M tokens)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Context window</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Sol</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Flagship reasoning</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$5.00 (about ¥36)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$30.00 (about ¥217)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1.05M tokens</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Terra</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Balanced daily</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$2.50 (about ¥18)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$15.00 (about ¥109)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1.05M tokens</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Luna</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lightweight, low cost</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$1.00 (about ¥7)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$6.00 (about ¥44)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1.05M tokens</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
OpenAI GPT-5.6 series pricing (August 2026)

GPT's core strength is balance — reasoning, coding, writing, multimodal, no glaring weaknesses. Plus OpenAI's huge plugin ecosystem and developer community, with the most complete docs and tooling. When you don't know what to pick, GPT is the safe default. Weak spots: needs special network access in China, occasional translation-flavored Chinese, and mid-to-high API prices.

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Good news

{class="mt-1"}
In August 2026 OpenAI upgraded free users' default model to GPT-5.6 Luna and opened unlimited text chat. That means you can try GPT's basics at zero cost and only pay when you need stronger reasoning or API calls.
:::

##### 2. Anthropic Claude series: coding and rigor at the top

If GPT is the all-rounder, Claude is the coding ceiling. Anthropic's Claude series has long led SWE-bench (software engineering benchmark) by a wide margin, with top code quality and real-world engineering delivery. Even better, Claude's hallucination rate (chance of making things up) is the lowest online at about 1% — ideal for academic, legal, and other high-precision work.

Claude's other killer feature is long context: up to 1 million tokens, able to "read" hundreds of pages of contracts or a whole codebase without missing details. Nearly irreplaceable for refactors and long-document analysis. Claude Code, the terminal AI coding tool, hit $2.5 billion annualized revenue by mid-2026 — strong evidence of Claude's coding reputation.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Model</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Positioning</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Input (/1M tokens)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Output (/1M tokens)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Context window</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Fable 5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Flagship</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$10.00 (about ¥72)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$50.00 (about ¥362)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1M tokens</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Opus 4.8</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Professional</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$5.00 (about ¥36)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$25.00 (about ¥181)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1M tokens</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Sonnet 5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Value</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$2.00 (about ¥14)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$10.00 (about ¥72)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1M tokens</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Anthropic Claude series pricing (August 2026; Sonnet 5 at promotional rate)

Claude's downside is price — Fable 5 output is the most expensive of all models at $50 per million tokens. Multimodal (image/video understanding) is also relatively weak. For individual developers on a budget, Sonnet 5's promotional price is excellent value.

##### 3. Google Gemini series: the multimodal king

Google's Gemini series reached 3.1 Pro in 2026. Its biggest edge is native multimodal — precise image-text parsing, accurate OCR for tables, efficient video frame extraction, and deep audio/video analysis. Deeply tied to Google's ecosystem (Search, Gmail, cloud), it shines at real-time information retrieval and cross-modal understanding. Gemini also supports up to 2 million tokens of context — the largest window today.

Gemini positions itself as the first choice for scientific reasoning and multimodal work. If your project involves lots of image analysis, video understanding, or scientific computing, Gemini has few rivals. But pure-text code generation is slightly behind Claude, and its Chinese is less natural than domestic models.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Comparison item</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GPT-5.6</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Claude Fable 5</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Gemini 3.1 Pro</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Overall score</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">94.8</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">95.0</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">92.1</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Coding (SWE-bench)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">74.9%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">64.3% (Pro)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Medium</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Context window</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1.05M tokens</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1M tokens</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2M tokens</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Multimodal</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Balanced</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Weaker</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Strongest</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hallucination rate</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Relatively low</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lowest (~1%)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Relatively low</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Availability in China</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Needs special network</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Needs special network</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Needs special network</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API ecosystem</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Most complete</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Growing</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tied to Google ecosystem</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Side-by-Side Comparison of the Big Three International Models (August 2026)

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Note: Real-World Hurdles for Users in China

{class="mt-1"}
For developers in China, the core obstacle to GPT, Claude, and Gemini is network access. You can reach them indirectly through Azure proxies, API aggregation platforms, and the like, but you'll need to weigh stability and compliance yourself. If your project has strict data security requirements, we recommend looking at Chinese models first.
:::

#### 2. China's Major Large Models: A Hundred Flowers in Bloom

By 2026, China's large models have gone from 'chasers' to running neck and neck with the leaders, and in some areas they have even pulled ahead. Unlike the 'wrapper' controversies of 2023, the flagship Chinese models of 2026 are on par with top international models in logical reasoning, code generation, and Chinese-language understanding, with the gap narrowed to within 5%. More importantly, Chinese models have irreplaceable advantages in Chinese-language scenarios, cost, and compliant deployment.

##### 1. DeepSeek V4: The Best Bang for Your Buck

DeepSeek is a phenomenon among Chinese large models. In early 2025, DeepSeek-V3 shook the market with its positioning of 'one-tenth the price of GPT with comparable capability,' and the industry dubbed it the 'kill line' for general-purpose AI models — nothing cheaper works as well, and nothing more expensive gives you more. By August 2026, DeepSeek V4-Pro was officially released: a 1.6-trillion-parameter MoE architecture with about 49B parameters active, support for 1 million tokens of lossless context, and coding value widely seen as the best in the world.

DeepSeek V4 made a huge leap in agent capability — its DeepSWE benchmark score jumped from 12.8 to 62.7 (+390%), and NL2Repo rose from 38.5 to 61.5. The API now supports both the Responses API and the Anthropic API, so it works with mainstream coding tools like Codex and Claude Code. That means you can swap DeepSeek's API in for Claude's and use it inside Claude Code — cutting your costs several times over with a nearly identical experience.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Model</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Positioning</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Input (per 1M tokens)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Output (per 1M tokens)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Context Window</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek V4 Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Flagship reasoning</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3 yuan (approx. US$0.43)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6 yuan (approx. US$0.87)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1M tokens</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek V4 Flash</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lightweight and fast</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 yuan (approx. US$0.14)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2 yuan (approx. US$0.28)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1M tokens</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
DeepSeek V4 series pricing (August 2026, promotional prices)

Price comparison: for the same 1 million input tokens plus 1 million output tokens, DeepSeek V4 Flash costs about $0.42, GPT-5.6 Sol costs about $35, and Claude Fable 5 costs about $60. That is a gap of 80 to 140 times.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Watch Out: DeepSeek Is About to Raise Its Prices

{class="mt-1"}
On August 6, 2026, DeepSeek officially announced that it 'plans to significantly raise API prices in the near future,' so the promotional prices may not last long. Some media reports speculate the increase could be as much as 30 times, and as of August 14 the company had not yet published its final pricing plan. On top of that, the official DeepSeek V4 release introduced peak/off-peak pricing — calls during peak hours cost exactly double. Keep an eye on the official announcements for the latest prices.
:::

##### 2. Tongyi Qianwen Qwen3.7 Max: Alibaba Cloud's Enterprise Choice

Alibaba Cloud's Qwen (Tongyi Qianwen) series leans on the Alibaba Cloud ecosystem, giving it a natural edge in enterprise deployment. Qwen3.7 Max, released in July 2026, is the current flagship: a dense 235B-parameter model with 256K of native context, expandable to 1M. Qwen's core strengths are a mature open-source ecosystem (the entire lineup from 7B to 235B is open source), precise understanding of Chinese-language scenarios, and deep integration with Alibaba Cloud infrastructure.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Model</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Output Price (per 1M tokens)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Use Case</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen-turbo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">0.6 yuan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Simple Q&A, text classification, high concurrency</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen-long</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.0 yuan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">10M ultra-long context processing</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen3.7-flash</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">7.2 yuan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">General conversation, content generation</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen3.7-plus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">12.0 yuan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Multimodal (images + video), Chinese content creation</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen3.7-max</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">36.0 yuan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Flagship Chinese capability, complex tasks</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Qwen (Tongyi Qianwen) series tiered pricing (August 2026)

Qwen's pricing is tiered — from the ultra-low-cost qwen-turbo (0.6 yuan per 1M output tokens) up to the flagship qwen3.7-max (36 yuan per 1M output tokens), covering everything from lightweight Q&A to complex reasoning. For companies already on Alibaba Cloud, Qwen is the most convenient integration choice.

##### 3. Zhipu GLM-5.1: Top Chinese Model on SWE-bench

Zhipu AI's GLM series shone in 2026. GLM-5.1 took first place among Chinese models on SWE-bench: a 744B hybrid MoE-dense architecture with support for 1 million tokens of context. Its hallmarks are precise Chinese semantic understanding and support for compliant private deployment in China — which matters a great deal for finance and government scenarios with strict data security requirements. GLM-5.1 is priced at 6 yuan for input and 24 yuan for output per 1M tokens, in the middle of the pack among Chinese models.

##### 4. Kimi K3: The King of Ultra-Long Text

Moonshot AI's Kimi series is known for its ultra-long text handling. Kimi K3, released in July 2026, has 2.8 trillion parameters and lands in the global top tier across many complex-task benchmarks. Kimi's core use cases are large codebase analysis and long-document retrieval augmentation — it can chew through the text of an entire book or the code of an entire project, and it excels at 'needle in a haystack' retrieval tasks. Kimi is relatively pricey (about 12-20 yuan per 1M output tokens), but in long-text scenarios nothing else matches its value for money.

##### 5. Doubao: ByteDance's All-Rounder

ByteDance's Doubao series has been steady in 2026. Doubao Seed 2.1 Pro is the flagship model on Volcano Engine, with 256K context and consistently solid results in real-world testing, standing out in Chinese-language scenarios. Doubao's advantages: a big bundle of free tokens the moment you register, well-polished integration with the Volcano Engine ecosystem, and pricing among the lowest tiers in China. For beginners who want a quick taste of AI coding, Doubao is a zero-barrier way in.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Comparison Item</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">DeepSeek V4</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Qwen3.7 Max</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GLM-5.1</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kimi K3</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Doubao 2.1 Pro</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Overall Score</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">87.5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">89.7</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">90.5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">88+</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">85+</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Coding Ability</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Extremely strong</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Strong</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">No. 1 in China on SWE</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Strong</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Above average</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Chinese Understanding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Excellent</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Excellent</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Precise</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Excellent</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Excellent</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Context Window</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1M</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256K-1M</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1M</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ultra-long</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256K</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Output Price (yuan per 1M)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">36</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">24</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">12-20</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">30</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Open Source</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MIT license</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Entire lineup open source</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Partially open source</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Closed source</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Closed source</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Private Deployment</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Yes</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Yes</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Yes</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">No</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">No</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Side-by-Side Comparison of China's Top Five Models (August 2026)

One important trend: the sense of a 'generation gap' between Chinese models and GPT/Claude has disappeared. In logical reasoning and math competitions, Chinese flagships trail GPT-5 by single digits. Claude still leads in systematic architectural thinking and complex engineering reasoning — it produces architecture plans with more 'flair,' while Chinese models can sometimes come across as 'by the book.' But in Chinese-language scenarios, cost control, and compliant deployment, Chinese models hold an overwhelming advantage.

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="620" height="290" viewBox="0 0 620 290" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="620" height="290" fill="#ffffff" rx="8"/>
      <line x1="70" y1="230" x2="590" y2="230" stroke="#9ca3af" stroke-width="1.5"/>
      <line x1="70" y1="230" x2="70" y2="20" stroke="#9ca3af" stroke-width="1.5"/>
      <line x1="70" y1="60" x2="590" y2="60" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="70" y1="116" x2="590" y2="116" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="70" y1="173" x2="590" y2="173" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="4,4"/>
      <text x="62" y="234" font-size="10" fill="#6b7280" text-anchor="end">0</text>
      <text x="62" y="120" font-size="10" fill="#6b7280" text-anchor="end">50</text>
      <text x="62" y="64" font-size="10" fill="#6b7280" text-anchor="end">100</text>
      <text x="340" y="262" font-size="10.5" fill="#374151" text-anchor="middle">Output price (yuan/million tokens)</text>
      <!-- bars: price -->
      <rect x="95" y="218" width="60" height="12" fill="#4f46e5"/><text x="125" y="212" font-size="9" fill="#374151" text-anchor="middle">6</text><text x="125" y="248" font-size="9.5" fill="#374151" text-anchor="middle">DeepSeek</text>
      <rect x="195" y="146" width="60" height="84" fill="#4f46e5"/><text x="225" y="140" font-size="9" fill="#374151" text-anchor="middle">36</text><text x="225" y="248" font-size="9.5" fill="#374151" text-anchor="middle">Qwen</text>
      <rect x="295" y="182" width="60" height="48" fill="#4f46e5"/><text x="325" y="176" font-size="9" fill="#374151" text-anchor="middle">24</text><text x="325" y="248" font-size="9.5" fill="#374151" text-anchor="middle">GLM</text>
      <rect x="395" y="200" width="60" height="30" fill="#4f46e5"/><text x="425" y="194" font-size="9" fill="#374151" text-anchor="middle">16</text><text x="425" y="248" font-size="9.5" fill="#374151" text-anchor="middle">Kimi</text>
      <rect x="495" y="170" width="60" height="60" fill="#4f46e5"/><text x="525" y="164" font-size="9" fill="#374151" text-anchor="middle">30</text><text x="525" y="248" font-size="9.5" fill="#374151" text-anchor="middle">Doubao</text>
      <!-- scores -->
      <circle cx="125" cy="118" r="5" fill="#d4a017"/><text x="140" y="114" font-size="9" fill="#78350f">87.5</text>
      <circle cx="225" cy="110" r="5" fill="#d4a017"/><text x="240" y="106" font-size="9" fill="#78350f">89.7</text>
      <circle cx="325" cy="105" r="5" fill="#d4a017"/><text x="340" y="101" font-size="9" fill="#78350f">90.5</text>
      <circle cx="425" cy="112" r="5" fill="#d4a017"/><text x="440" y="108" font-size="9" fill="#78350f">88+</text>
      <circle cx="525" cy="116" r="5" fill="#d4a017"/><text x="540" y="112" font-size="9" fill="#78350f">85+</text>
      <rect x="90" y="30" width="12" height="12" fill="#4f46e5"/><text x="108" y="41" font-size="9.5" fill="#374151">Output price (lower is better)</text>
      <circle cx="170" cy="36" r="5" fill="#d4a017"/><text x="182" y="40" font-size="9.5" fill="#374151">Overall score (higher is better)</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figure 4: Price vs. Performance of the Five Models (lower price is better, higher score is better)
:::

#### 3. A Decision Framework for Choosing a Model

Now that you know each model's strengths, how do you pick one for your project? Here is a 'four-question decision method' — answer four questions, and you'll lock onto the model that fits you best.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-globe mr-1"></i> Is your project deployed in China or internationally?</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">China → choose a Chinese model</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">International → overseas models are an option</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-laptop-code mr-1"></i> Is the core task coding or something else?</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Coding → Claude or DeepSeek</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">Other → keep narrowing down</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-book mr-1"></i> Need extra-long context (&gt;500K tokens)?</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Yes → Gemini or Kimi</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">No → keep narrowing down</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-coins mr-1"></i> Is budget a concern?</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Yes → DeepSeek or Qwen-turbo</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">No → GPT-5.6 or Claude</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figure 5: The Four-Question Decision Method for Choosing a Large Model
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tip: The Combination Strategy

{class="mt-1"}
This decision method isn't dogma — many situations call for combining several models. One common strategy: use DeepSeek or Qwen for everyday development (cheap, good with Chinese), Claude for critical architecture design (strong reasoning, low hallucination), and Gemini for multimodal analysis (image and video processing). Switch models as needed instead of riding 'one model to the grave.'
:::

#### 4. Getting Started with API Calls: Connecting to a Large Model from Scratch

Many AI coding tutorials only teach you how to use the chat interface, but real 'AI programming' — having your application call a large model — goes through an API. An API (Application Programming Interface) is a communication protocol between programs. Through an API, your code can call on a large model's abilities as easily as calling a function.

##### 1. What Is a Token

Before APIs, you must first understand the concept of a 'token.' A token is the basic billing unit for large models — think of it as the AI's unit of reading and writing. One token is roughly 0.75 English words (4 characters), or 0.5-1 Chinese characters. A 1,000-character Chinese passage consumes about 1,500-2,000 tokens.

A token is not a word count, nor a character count. Large models use a dedicated tokenizer to split text into tokens. The same word can cost a different number of tokens in different models — 'artificial intelligence,' for instance, might be 3 tokens in GPT but 2 in DeepSeek. Most models' APIs return the actual number of tokens consumed, and you can check it in the API response.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Quick Token Cost Estimates

{class="mt-1"}
One million Chinese characters is roughly 1.5 million tokens. Processing 1 million characters of input plus 1 million characters of output with DeepSeek V4 Flash costs about $0.42 (around 3 yuan); the same volume with Claude Fable 5 costs about $60 (around 434 yuan). That is why your choice of model directly shapes your project's cost.
:::

##### 2. Getting an API Key

The first step in using a large model API is getting an API Key — a string used to verify your identity. Every model provider has its own API platform, where you register an account and create an API Key. Here are the API platform entry points for the mainstream models and the steps to get a key:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Model</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">API Platform</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">How to Get a Key</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Free Allowance</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">platform.deepseek.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sign up → identity verification → create API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Free allowance for new users</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Qwen (Tongyi Qianwen)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">bailian.aliyun.com (Bailian platform)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Log in with an Alibaba Cloud account → activate the service → create a Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Free trial for new users</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Zhipu GLM</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">open.bigmodel.cn</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sign up → identity verification → create API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Free allowance for new users</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kimi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">platform.moonshot.cn</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sign up → identity verification → create API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Limited free allowance</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Doubao</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">volcengine.com (Volcano Engine)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sign up → activate Volcano Ark → create API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Large free token grant just for signing up</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenAI GPT</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">platform.openai.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sign up → link a credit card → create API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">No free allowance (paid)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Anthropic Claude</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">console.anthropic.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sign up → link a card → create API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Small allowance for new users</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
API platforms for mainstream models and how to get a key (August 2026)

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Security Note: Your API Key Is Your Wallet Password

{class="mt-1"}
An API Key is the equivalent of your wallet password — anyone who gets hold of it can spend your quota calling the model. So: never write an API Key into your code (manage it with environment variables); never commit code containing a Key to a public Git repository; never share screenshots containing a Key on social media. If a Key leaks, delete it on the platform and create a new one immediately.
:::

##### 3. Your First API Call

Once you have an API Key, you can call a large model API from any programming language. Here is the simplest possible call, shown in Python — send one message to DeepSeek and get the reply back.

::: div .code-block
:::inline div .code-head
<span>PYTHON · Your first API call</span><span class="dots">···</span>
:::

```
# Install the SDK: pip install openai
# DeepSeek is compatible with the OpenAI SDK format — use it directly
from openai import OpenAI
import os

# 1. Create the client (the API key is read from an environment variable)
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 2. Send the request
response = client.chat.completions.create(
    model="deepseek-chat",  # pick the model
    messages=[
        {"role": "system", "content": "You are a Python coding assistant."},
        {"role": "user", "content": "Write a quicksort function."}
    ]
)

# 3. Get the reply
print(response.choices[0].message.content)

# 4. Check token usage
print(f"Input tokens: {response.usage.prompt_tokens}")
print(f"Output tokens: {response.usage.completion_tokens}")
print(f"Total tokens: {response.usage.total_tokens}")
```
:::

The core logic of this code: create a client (carrying the API Key and the model address) → build the message list (system sets the role, user is the human's input) → send the request → get the reply. This pattern works for nearly every OpenAI-compatible model — just swap the api_key and base_url to change models. That is why so many Chinese models choose to be OpenAI SDK compatible: developers can switch models by changing two lines of code, so the cost of migrating is almost nil.

Here is what changes when you switch to another model — note that only two lines need to change:

::: div .code-block
:::inline div .code-head
<span>PYTHON · Switching models takes just two lines</span><span class="dots">···</span>
:::

```
# DeepSeek
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
# model="deepseek-chat"

# Qwen (Tongyi Qianwen, Bailian platform)
client = OpenAI(
    api_key=os.environ.get("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
# model="qwen-plus"

# Zhipu GLM
client = OpenAI(
    api_key=os.environ.get("GLM_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4"
)
# model="glm-4"

# OpenAI GPT
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    # the default base_url is fine
)
# model="gpt-5.6-terra"
```
:::

##### 4. Streaming Responses

In a real application, you usually don't want to wait for the AI to finish everything before displaying it in one lump — that makes users wait far too long. Streaming responses let the text appear word by word as the AI generates it, which vastly improves the user experience. Like a typewriter with letters popping out one at a time — it feels completely different to the user.

::: div .code-block
:::inline div .code-head
<span>PYTHON · Streaming responses</span><span class="dots">···</span>
:::

```
# Streaming: output one character at a time
stream = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "Write a tutorial on bubble sort in Python"}
    ],
    stream=True  # enable streaming
)

# Receive chunk by chunk and print
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)
# The output appears character by character, like a typewriter
```
:::

#### 5. A Buyer's Guide to Token Plans

Most model providers offer two billing methods: pay-as-you-go and subscription plans (Token Plans). Understanding the difference between the two can cut your costs dramatically.

##### 1. Pay-As-You-Go vs. Subscription Plans

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Aspect</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Pay-as-you-go</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Subscription plan</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Billing Method</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pay only for the tokens you use</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pay a fixed amount up front and receive an allowance</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Best For</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Unsteady usage, occasional calls</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Steady usage, frequent calls</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Price Advantage</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Standard price</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">20%-50% cheaper than pay-as-you-go</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Flexibility</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Available anytime, no commitment</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Requires prepayment; unused allowance may expire</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Going Over Quota</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Automatically billed as you go</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Switches to pay-as-you-go once the allowance runs out</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Typical Platforms</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Each model's official API platform</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenAI Plus/Pro, Claude Pro, Cursor Pro</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Comparing the Two Billing Methods

For beginners, start with pay-as-you-go — no upfront cost, and you pay for exactly what you use. Once your monthly usage settles at a steady level (say, above 50 yuan a month), consider switching to a subscription plan for a lower unit price.

##### 2. Mainstream Subscription Plans at a Glance

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Plan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Monthly Fee</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">What's Included</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Best For</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ChatGPT Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Unlimited text chat with GPT-5.6 Luna</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Trying it out as a total beginner</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ChatGPT Plus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$20/month</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Sol, image generation, data analysis, plugin access</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Moderate users</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ChatGPT Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$200/month</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Unlimited use of all models, priority access to new features</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Heavy professional users</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A limited number of Claude chats</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Trying it out as a total beginner</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$20/month</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Unlimited Claude usage, priority access to new models</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Coders</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A limited number of AI completions and chats</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Getting started as a beginner</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$20/month</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Unlimited AI completions, 500 premium requests per month</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Everyday developers</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor Business</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$40/month per person</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team collaboration, admin console, privacy mode</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Teams</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Mainstream AI tool subscription plans (August 2026)

Chinese models handle subscriptions a little differently. DeepSeek is mainly pay-as-you-go, with no monthly subscription plan — you top up and get charged based on actual usage. Qwen offers prepaid resource packages on the Bailian platform (buy a fixed amount of tokens at a discounted price). Doubao has similar prepaid options on Volcano Engine. For developers in China, the most economical combination is usually: DeepSeek pay-as-you-go (daily development) plus Doubao's free allowance (trying things out).

##### 3. API Aggregation Platforms

If you need to use several models at once, an API aggregation platform is a hassle-free option. An aggregator gives you one unified API Key that can call dozens of models worldwide, with no need to register separately on each platform.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Platform</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Features</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Price Advantage</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Best For</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenRouter (openrouter.ai)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Overseas aggregator: one Key for models worldwide</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Transparent pricing with real-time comparison</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Flexibly switching among many overseas models</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SiliconFlow (siliconflow.cn)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">China-based aggregator offering APIs for many Chinese models</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">20%-30% below official prices</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Developers in China comparing model prices</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Azure OpenAI (Microsoft's proxy)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The OpenAI API proxied through Microsoft Azure</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">50% off with the Batch API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Enterprise-grade OpenAI calls; large asynchronous batches</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Baidu Qianfan (qianfan.baidubce.com)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Baidu's AI cloud platform, offering ERNIE and other models</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Free allowance for new users</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Users in Baidu's ecosystem</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Mainstream API Aggregation Platforms (August 2026)

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Watch Out: Don't Buy 'Shared Keys'

{class="mt-1"}
Do not buy so-called 'shared API Keys' on Taobao, Xianyu, or similar platforms — these Keys usually come from unclear sources, can be banned at any moment, and carry the risk of data leaks. Always get API Keys through official platforms or reputable aggregators.
:::

##### 4. Cost Optimization Strategies

Picking the right model is only the first step — knowing how to 'use it frugally' matters just as much. Here are a few cost optimization strategies proven in practice:

1. Make the most of cache hits. Many models offer 'caching' — when your request includes content that has been processed before (such as a system prompt), that portion is billed at a tiny fraction of the normal price. DeepSeek charges just 1/60 of the regular price for cache hits. Putting your fixed system prompt at the start of the message list maximizes cache hits.
2. Tiered routing — use a cheap model for simple tasks and an expensive one for complex tasks. For example, DeepSeek V4 Flash for text classification (2 yuan per 1M output tokens) and Claude for architecture design (181 yuan per 1M output tokens). In a typical project, 80% of calls can go to the cheap model.
3. Cap your output length. APIs bill by output tokens, so longer output costs more. In scenarios that don't call for long-winded answers, set the max_tokens parameter to limit output length and keep the AI from 'rambling on.'
4. Use the Batch API for non-real-time tasks. If you have lots of tasks that don't need instant responses (such as bulk data labeling or document summarization), the Batch API earns you a 50% discount. Both OpenAI and Azure offer this feature.
5. Monitor your token usage. Most API platforms provide a usage dashboard. Check the usage breakdown regularly, find the calls that burn the most tokens, and optimize them specifically. One small prompt tweak (say, changing 'please explain in detail' to 'please explain in 3 sentences') can save 50% of your tokens.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Strategy</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Savings</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Difficulty</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Notes</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cache hits</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Up to 98%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Low</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Put fixed content at the start of your messages</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tiered routing</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">50%-80%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mid</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Use a cheap model for simple tasks</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cap output length</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">30%-60%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Low</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Set the max_tokens parameter</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Batch API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">50%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Low</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Use batch processing for non-real-time tasks</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prompt optimization</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">20%-50%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mid</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Streamline prompts and trim redundancy</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Cost optimization strategies and their impact (August 2026)

#### 6. Hands-On: Wiring a Large Model API into a Project

Let's wrap up the chapter with a complete hands-on exercise — building an 'AI Summarizer': the user pastes in a long piece of text, and the app calls a large model API to produce a summary. This exercise walks through the full API workflow: environment setup, the API call, error handling, and cost control.

::: div .code-block
:::inline div .code-head
<span>PYTHON · ai_summarizer.py</span><span class="dots">···</span>
:::

```
# ai_summarizer.py - AI summarizer
import os
from openai import OpenAI

# 1. Configure (the API key is read from an environment variable — never hard-code it)
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def summarize(text: str, max_length: int = 200) -> dict:
    """Summarize a text

    Args:
        text: the original text to summarize
        max_length: maximum summary length (in tokens)

    Returns:
        dict: the summary plus token-usage info
    """
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "system",
                    "content": "You are a summarizer."
                               "Summarize the user's text concisely."
                               "Keep the summary to 3 sentences at most."
                },
                {
                    "role": "user",
                    "content": f"Summarize the following text:\n\n{text}"
                }
            ],
            max_tokens=max_length,  # cap the output length
            temperature=0.3  # low temperature = more stable
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

# 2. Usage example
if __name__ == "__main__":
    long_text = """
    (paste a long text here...)
    """

    result = summarize(long_text)

    if result["success"]:
        print(f"Summary: {result['summary']}")
        print(f"Tokens used: {result['total_tokens']}")
        # estimate the cost: DeepSeek V4 Flash
        cost = result['total_tokens'] * 0.000004  # about 0.4 fen per 1,000 tokens
        print(f"Estimated cost: {cost:.4f} yuan")
    else:
        print(f"Something went wrong: {result['error']}")
```
:::

This code embodies several API best practices: the API Key is read from an environment variable and never hardcoded; the function has clear documentation and type hints; max_tokens is set to cap the output length; temperature is set low (0.3) for more stable output; error handling is complete; and token consumption is returned for cost tracking. When you have the AI write this code, you can simply tell it these requirements — it is fully capable of implementing them.

:::inline div .quote-line
The final lesson of this chapter: models are the "ammunition," methodology is the "tactics." The right ammunition makes the battle smoother, but without good tactics even the best ammo loses the war. Now that you know each model's strengths and how to use the APIs, you have a well-stocked arsenal — but how you fight the battle still depends on the thinking methods from the earlier chapters.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Try It Yourself: Get Your First API Call Running

{class="mt-1"}
Register on a Chinese model platform (we recommend DeepSeek or Zhipu — both give new users a free allowance), create an API Key, put it into your system environment variables (not into your code!), and then run the 'first API call' code above. The moment you see the AI's reply print out, you have crossed the line between 'using AI' and 'building AI applications.'
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Chapter Recap

- The big three international models: GPT-5.6 (a balanced all-rounder), Claude (top-tier coding with a hallucination rate of just 1%), Gemini (king of multimodal with 2M context)
- China's top five: DeepSeek V4 (best value for money — watch for the price-increase announcement), Qwen3.7 (enterprise-grade), GLM-5.1 (No. 1 in China on SWE), Kimi K3 (ultra-long text), Doubao (a free way to start)
- The four-question decision method: Where will it be deployed? Coding or something else? Ultra-long context? Tight budget?
- Tokens are the billing unit: 1 Chinese character is about 1.5-2 tokens; 1 million characters is about 1.5 million tokens
- An API Key is your wallet password: manage it with environment variables, never hardcode it, never upload it to Git
- Chinese models are generally OpenAI SDK compatible: switching models means changing just two lines — api_key and base_url
- Five ways to save: cache hits, tiered routing, capping output, the Batch API, and monitoring usage
:::
