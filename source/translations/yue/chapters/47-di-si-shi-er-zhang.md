---
id: di-si-shi-er-zhang
num: 42
part: ai-biancheng-pian
nav: 第四十二章：大模型全景與API實戰
toc: default
kind: chapter
---

### 第四十二章：大模型全景同 API 實戰

{class="chapter-intro mb-4"}
前面幾章講嘅都係「點樣同 AI 協作」，本章解決一個更基礎嘅問題：「用邊個 AI？點樣用？」2026 年 8 月嘅大模型格局已經極其豐富——國際有 GPT、Claude、Gemini 三強爭霸，國內有 DeepSeek、通義千問、GLM、Kimi、豆包百花齊放。每個模型都有自己嘅性格同特長：揀啱咗事半功倍，揀錯咗事倍功半。本章唔單止帶你認識呢啲模型，仲會教你點樣透過 API 將佢哋接入自己嘅應用，以及點樣根據自己嘅需求揀合適嘅 Token Plan（用量套餐）。

#### 一、國際主流大模型：三強格局

2026 年 8 月嘅國際大模型市場，形成咗 OpenAI（GPT 系列）、Anthropic（Claude 系列）、Google（Gemini 系列）三強鼎立嘅格局。每家都有自己鮮明嘅特色——我哋一個一個認識。

##### 1. OpenAI GPT-5.6 系列：全能均衡嘅六邊形戰士

OpenAI 係大模型浪潮嘅開啟者，GPT 系列至今仍然係全球使用最廣泛嘅模型。2026 年 7 月發佈嘅 GPT-5.6 系列採用三檔定位策略：旗艦款 GPT-5.6 Sol 面向高端推理需求，均衡款 GPT-5.6 Terra 面向日常開發，輕量款 GPT-5.6 Luna 面向高並發低成本場景。三款模型共享 105 萬 Token 嘅上下文視窗，都支援圖像輸入、函數調用同結構化輸出。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">型號</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">定位</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">輸入(/百萬Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">輸出(/百萬Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">上下文視窗</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Sol</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">旗艦推理</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$5.00（約36蚊）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$30.00（約217蚊）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">105萬Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Terra</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">均衡日常</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$2.50（約18蚊）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$15.00（約109蚊）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">105萬Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Luna</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">輕量低成本</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$1.00（約7蚊）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$6.00（約44蚊）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">105萬Token</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
OpenAI GPT-5.6 系列定價（2026 年 8 月）

GPT 系列嘅核心優勢喺於「均衡」——推理、編程、寫作、多模態，冇明顯短板。加上 OpenAI 龐大嘅插件生態同開發者社區，適配文檔同工具鏈最為完善。對於「唔知揀乜嘢」嘅場景，GPT 係「盲揀都唔會錯」嘅預設答案。但佢嘅短板係：國內訪問需要特殊網絡，中文表達偶爾有「翻譯腔」，API 價格處於中高水平。

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
好消息

{class="mt-1"}
OpenAI 喺 2026 年 8 月宣佈免費用戶預設模型升級為 GPT-5.6 Luna，並開放無限量文本聊天。呢個意味住你可以零成本體驗 GPT 嘅基礎能力，只有喺需要更強推理或者 API 調用時先需要付費。
:::

##### 2. Anthropic Claude 系列：編程同嚴謹嘅天花板

如果話 GPT 係全能選手，咁 Claude 就係編程領域嘅「天花板」。Anthropic 嘅 Claude 系列喺 SWE-bench（軟件工程基準測試）上長期斷層領先，代碼生成質量同工程級項目落地能力業界第一。更難得嘅係，Claude 嘅幻覺率（生成虛假資訊嘅概率）全網最低，僅約 1%——呢個令佢特別適合學術、法務等高精度場景。

Claude 嘅另一個殺手鐧係超長上下文：支援 100 萬 Token 嘅上下文視窗，能夠一次性「讀完」幾百頁嘅合約或者成個代碼庫唔漏細節。呢個喺代碼重構、長文檔分析等場景中幾乎無可替代。Claude Code 作為終端 AI 編程工具，到 2026 年中期年化收入已達 25 億美元——呢個係 Claude 編程能力最受認可嘅證據。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">型號</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">定位</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">輸入(/百萬Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">輸出(/百萬Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">上下文視窗</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Fable 5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">旗艦款</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$10.00（約72蚊）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$50.00（約362蚊）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">100萬Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Opus 4.8</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">專業款</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$5.00（約36蚊）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$25.00（約181蚊）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">100萬Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Sonnet 5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">性價比款</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$2.00（約14蚊）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$10.00（約72蚊）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">100萬Token</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Anthropic Claude 系列定價（2026 年 8 月，Sonnet 5 為優惠價）

Claude 嘅短板係價格——Fable 5 嘅輸出價格係所有模型中最高嘅，每百萬 Token 要 50 美元。多模態能力（圖像、視像理解）亦相對較弱。對於預算有限嘅個人開發者，Sonnet 5 喺優惠期內嘅性價比非常突出。

##### 3. Google Gemini 系列：多模態嘅王者

Google 嘅 Gemini 系列喺 2026 年已迭代至 3.1 Pro 版本。Gemini 嘅最大殺手鐧係原生多模態——圖文解析精準、OCR 表格識別無誤、視像幀提取高效，仲支援音視像深度解析。佢同 Google 生態（搜尋、電郵、雲服務）深度綁定，喺即時資訊檢索同跨模態理解上表現突出。Gemini 仲支援 200 萬 Token 嘅超長上下文輸入，係目前上下文視窗最大嘅模型。

Gemini 嘅定位係「科學推理同多模態場景嘅首選」。如果你嘅項目涉及大量圖像分析、視像理解或者科學計算，Gemini 幾乎冇對手。但佢喺純文本代碼生成上略遜於 Claude，中文表達亦不如國產模型自然。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">對比項目</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GPT-5.6</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Claude Fable 5</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Gemini 3.1 Pro</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">綜合得分</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">94.8</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">95.0</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">92.1</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">編程能力(SWE-bench)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">74.9%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">64.3% (Pro)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">中等</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">上下文視窗</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">105萬Token</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">100萬Token</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">200萬Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多模態能力</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">均衡</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">較弱</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最強</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">幻覺率</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">較低</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最低(約1%)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">較低</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">國內可用性</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需特殊網絡</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需特殊網絡</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需特殊網絡</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API 生態</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最完善</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">成長中</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Google 生態綁定</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
國際三大模型橫向對比（2026 年 8 月）

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
留意：國內使用嘅現實門檻

{class="mt-1"}
對於國內開發者來說，GPT、Claude、Gemini 嘅核心障礙係網絡訪問。雖然可以透過 Azure 代理、API 聚合平臺等方式間接使用，但穩定性同合規性需要自行評估。如果你嘅項目對數據安全有嚴格要求，建議優先考慮國產模型。
:::

#### 二、國產主流大模型：百花齊放

2026 年嘅國產大模型已經由「追趕者」變成「並跑者」，喺某些領域甚至實現咗「領跑」。同 2023 年「套殼」爭議唔同，2026 年嘅國產旗艦模型喺邏輯推理、代碼生成、中文理解等方面已經同國際一線模型旗鼓相當，差距縮減到 5% 以內。更重要嘅係，國產模型喺中文場景、價格成本同合規部署上有不可替代嘅優勢。

##### 1. DeepSeek V4：性價比之王

DeepSeek（深度求索）係國產大模型中現象級嘅存在。2025 年初，DeepSeek-V3 以「比 GPT 平十分之一但能力相當」嘅定位震撼市場，被業內稱為「通用 AI 大模型斬殺線」——比佢平嘅冇佢好用，比佢貴嘅冇佢量大管飽。到 2026 年 8 月，DeepSeek V4-Pro 正式版發佈：1.6 萬億參數 MoE 架構，激活約 49B，支援 100 萬無損上下文，代碼性價比被廣泛認為係全球天花板。

DeepSeek V4 喺 Agent 能力上實現咗大幅躍升——DeepSWE 基準由 12.8 跳至 62.7（+390%），NL2Repo 由 38.5 升至 61.5。API 新增咗 Responses API 同 Anthropic API 雙協議支援，已兼容 Codex 同 Claude Code 等主流編程工具。呢個意味住你可以用 DeepSeek 嘅 API 替代 Claude 嘅 API，喺 Claude Code 中使用——成本降低數倍，體驗幾乎一致。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">型號</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">定位</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">輸入(/百萬Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">輸出(/百萬Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">上下文視窗</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek V4 Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">旗艦推理</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3蚊（約US$0.43）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6蚊（約US$0.87）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">100萬Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek V4 Flash</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">輕量快速</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1蚊（約US$0.14）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2蚊（約US$0.28）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">100萬Token</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
DeepSeek V4 系列定價（2026 年 8 月，促銷價）

價格對比：同樣 100 萬 Token 嘅輸入 + 100 萬 Token 嘅輸出，DeepSeek V4 Flash 花費約 0.42 美元，GPT-5.6 Sol 花費約 35 美元，Claude Fable 5 花費約 60 美元。差距高達 80-140 倍。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
避坑提醒：DeepSeek 要加價喇

{class="mt-1"}
DeepSeek 官方已於 2026 年 8 月 6 日公告「計劃近期大幅上調 API 定價」，促銷價可能唔會持續太久。部分媒體傳聞漲幅可能達 30 倍，截至 8 月 14 日官方尚未公佈最終調價方案。此外，DeepSeek V4 正式版引入咗峯谷定價機制——高峯時段調用價格直接翻倍。建議關注官方公告獲取最新定價。
:::

##### 2. 通義千問 Qwen3.7 Max：阿里雲嘅企業級選擇

阿里雲嘅通義千問（Qwen）系列依託阿里雲生態，喺企業級部署上有天然優勢。2026 年 7 月嘅 Qwen3.7 Max 係當前旗艦：235B 參數稠密模型，256K 原生上下文，可擴展至 1M。Qwen 嘅核心優勢喺於：開源生態成熟（由 7B 到 235B 全系列開源）、中文場景理解精準、同阿里雲基礎設施深度整合。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">型號</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">輸出價格(/百萬Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">適用場景</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen-turbo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">0.6蚊</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">極簡問答、文本分類、高並發</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen-long</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.0蚊</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">10M 超長上下文處理</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen3.7-flash</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">7.2蚊</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">通用對話、內容生成</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen3.7-plus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">12.0蚊</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多模態（圖片+視像）、中文創作</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen3.7-max</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">36.0蚊</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">旗艦中文能力、複雜任務</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
通義千問 Qwen 系列階梯定價（2026 年 8 月）

Qwen 嘅定價採用階梯策略——由極低成本嘅 qwen-turbo（輸出 0.6 蚊/百萬 Token）到旗艦 qwen3.7-max（輸出 36 蚊/百萬 Token），覆蓋由輕量問答到複雜推理嘅全場景需求。對於已經喺度用阿里雲嘅企業，Qwen 係最順手嘅整合選擇。

##### 3. 智譜 GLM-5.1：國產 SWE-bench 第一

智譜 AI 嘅 GLM 系列喺 2026 年表現亮眼。GLM-5.1 喺 SWE-bench 上攞到國產第一嘅成績：744B MoE 稠密混合架構，支援 100 萬上下文。佢嘅特點係中文語義理解精準，支援國內合規私有化部署——呢個對數據安全要求高嘅金融、政務場景非常重要。GLM-5.1 嘅定價為輸入 6 蚊、輸出 24 蚊每百萬 Token，處於國產模型中游水平。

##### 4. Kimi K3：超長文本之王

月之暗面嘅 Kimi 系列以超長文本處理能力著稱。2026 年 7 月發佈嘅 Kimi K3 擁有 2.8 萬億參數規模，喺多項複雜任務評測中進入全球第一梯隊。Kimi 嘅核心場景係長代碼庫分析同長文檔檢索增強——佢能夠處理成本書嘅文本或者成個項目嘅代碼，喺「大海撈針」式檢索任務中表現卓越。Kimi 嘅定價相對較高（輸出約 12-20 蚊/百萬 Token），但喺長文本場景嘅性價比無人能及。

##### 5. 豆包 Doubao：字節跳動嘅全能選手

字節跳動嘅豆包系列喺 2026 年表現穩定。Doubao Seed 2.1 Pro 係火山引擎旗艦模型，256K 上下文，喺實測中綜合發揮穩定，中文場景體驗突出。豆包嘅優勢喺於：註冊即送大量免費 Token，火山引擎生態整合完善，定價處於國內最低梯隊之一。對於想要快速體驗 AI 編程嘅初學者，豆包係零門檻嘅入門選擇。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">對比項目</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">DeepSeek V4</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Qwen3.7 Max</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GLM-5.1</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kimi K3</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">豆包 2.1 Pro</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">綜合得分</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">87.5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">89.7</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">90.5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">88+</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">85+</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">編程能力</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">極強</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">強</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">國產SWE第一</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">強</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">中上</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">中文理解</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">優秀</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">優秀</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">精準</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">優秀</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">優秀</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">上下文視窗</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">100萬</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256K-1M</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">100萬</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">超長</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256K</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">輸出價格(蚊/M)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">36</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">24</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">12-20</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">30</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">開源</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MIT協議</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全系列開源</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">部分開源</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">閉源</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">閉源</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">私有化部署</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">支援</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">支援</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">支援</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">唔支援</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">唔支援</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
國產五大模型橫向對比（2026 年 8 月）

一個重要嘅趨勢係：國產模型同 GPT/Claude 嘅「代差感」已經消失。喺邏輯推理同數學競賽上，國產旗艦同 GPT-5 嘅分差基本上喺個位數。喺系統化架構思維同複雜工程推理上，Claude 仍然領先——佢能夠畀出更有「靈氣」嘅架構方案，而國產模型有時顯得「教條」。但喺中文場景、成本控制同合規部署上，國產模型有壓倒性優勢。

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
      <text x="340" y="262" font-size="10.5" fill="#374151" text-anchor="middle">輸出價格（元/百萬Token）</text>
      <!-- bars: price -->
      <rect x="95" y="218" width="60" height="12" fill="#4f46e5"/><text x="125" y="212" font-size="9" fill="#374151" text-anchor="middle">6</text><text x="125" y="248" font-size="9.5" fill="#374151" text-anchor="middle">DeepSeek</text>
      <rect x="195" y="146" width="60" height="84" fill="#4f46e5"/><text x="225" y="140" font-size="9" fill="#374151" text-anchor="middle">36</text><text x="225" y="248" font-size="9.5" fill="#374151" text-anchor="middle">Qwen</text>
      <rect x="295" y="182" width="60" height="48" fill="#4f46e5"/><text x="325" y="176" font-size="9" fill="#374151" text-anchor="middle">24</text><text x="325" y="248" font-size="9.5" fill="#374151" text-anchor="middle">GLM</text>
      <rect x="395" y="200" width="60" height="30" fill="#4f46e5"/><text x="425" y="194" font-size="9" fill="#374151" text-anchor="middle">16</text><text x="425" y="248" font-size="9.5" fill="#374151" text-anchor="middle">Kimi</text>
      <rect x="495" y="170" width="60" height="60" fill="#4f46e5"/><text x="525" y="164" font-size="9" fill="#374151" text-anchor="middle">30</text><text x="525" y="248" font-size="9.5" fill="#374151" text-anchor="middle">豆包</text>
      <!-- scores -->
      <circle cx="125" cy="118" r="5" fill="#d4a017"/><text x="140" y="114" font-size="9" fill="#78350f">87.5</text>
      <circle cx="225" cy="110" r="5" fill="#d4a017"/><text x="240" y="106" font-size="9" fill="#78350f">89.7</text>
      <circle cx="325" cy="105" r="5" fill="#d4a017"/><text x="340" y="101" font-size="9" fill="#78350f">90.5</text>
      <circle cx="425" cy="112" r="5" fill="#d4a017"/><text x="440" y="108" font-size="9" fill="#78350f">88+</text>
      <circle cx="525" cy="116" r="5" fill="#d4a017"/><text x="540" y="112" font-size="9" fill="#78350f">85+</text>
      <rect x="90" y="30" width="12" height="12" fill="#4f46e5"/><text x="108" y="41" font-size="9.5" fill="#374151">輸出價格(越低越好)</text>
      <circle cx="170" cy="36" r="5" fill="#d4a017"/><text x="182" y="40" font-size="9.5" fill="#374151">綜合得分(越高越好)</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 4：五款模型嘅價格同性能對比（價格越低越好，得分越高越好）
:::

#### 三、模型選擇決策框架

瞭解咗各模型嘅特點之後，點樣為自己嘅項目揀模型？呢度送你一套「四問決策法」——回答四個問題，就能夠鎖定最適合你嘅模型。

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-globe mr-1"></i> 你個項目係喺國內定係國際部署？</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">國內 → 選國產模型</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">國際 → 可選海外模型</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-laptop-code mr-1"></i> 核心任務係編程定係其他？</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">編程 → Claude 或 DeepSeek</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">其他 → 繼續判斷</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-book mr-1"></i> 需要超長上下文(&gt;50萬Token)？</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">需要 → Gemini 或 Kimi</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">不需要 → 繼續判斷</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-coins mr-1"></i> 使唔使考慮預算？</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">敏感 → DeepSeek 或 Qwen-turbo</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">不敏感 → GPT-5.6 或 Claude</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 5：大模型選擇四問決策法
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：組合策略

{class="mt-1"}
呢個決策法唔係教條——好多場景需要組合使用多個模型。一個常見嘅組合策略：用 DeepSeek 或者 Qwen 做日常開發（成本低、中文好），用 Claude 做關鍵架構設計（推理強、幻覺低），用 Gemini 做多模態分析（圖像視像處理）。按需切換模型，而唔係「一個模型用到死」。
:::

#### 四、API 調用入門：由零開始接入大模型

好多 AI 編程教程只教你點樣用對話介面，但真正嘅「AI 編程」——令你嘅應用調用大模型——需要透過 API。API（Application Programming Interface，應用程序編程接口）係程序之間嘅通訊協議。透過 API，你嘅代碼可以好似調用一個函數一樣，調用大模型嘅能力。

##### 1. Token 係乜嘢

喺瞭解 API 之前，必須先理解「Token」呢個概念。Token 係大模型計費嘅基本單位，可以理解為「AI 嘅閱讀同寫作單位」。一個 Token 大約對應：英文中 0.75 個單詞（4 個字符），中文中 0.5-1 個漢字。一段 1000 字嘅中文文本，大約消耗 1500-2000 個 Token。

Token 唔係字數，亦唔係字符數。大模型使用專門嘅分詞器（Tokenizer）將文本切分成 Token。同一個詞喺唔同模型中嘅 Token 數量可能唔同——例如「人工智能」喺 GPT 中可能係 3 個 Token，喺 DeepSeek 中可能係 2 個。大多數模型嘅 API 會返回實際消耗嘅 Token 數量，你可以喺 API 響應中查看。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Token 成本快速估算

{class="mt-1"}
100 萬字中文約等於 150 萬 Token。用 DeepSeek V4 Flash 處理 100 萬字輸入 + 100 萬字輸出，成本約 0.42 美元（約 3 蚊人民幣）；用 Claude Fable 5 處理同樣嘅量，成本約 60 美元（約 434 蚊人民幣）。呢個就係點解模型選擇直接影響你嘅項目成本。
:::

##### 2. 取得 API Key

使用大模型 API 嘅第一步係取得 API Key——一串用嚟做身份驗證嘅密鑰。每個模型供應商都有自己嘅 API 平臺，你需要註冊帳號並創建 API Key。以下係主流模型嘅 API 平臺入口同獲取流程：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">模型</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">API 平臺</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">獲取流程</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">免費額度</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">platform.deepseek.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">註冊 → 實名認證 → 創建 API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新用戶贈送額度</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">通義千問</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">bailian.aliyun.com（百煉平臺）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">阿里雲帳號登入 → 開通服務 → 創建 Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新用戶免費試用</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">智譜GLM</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">open.bigmodel.cn</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">註冊 → 實名認證 → 創建 API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新用戶贈送額度</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kimi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">platform.moonshot.cn</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">註冊 → 實名認證 → 創建 API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">有限免費額度</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">豆包</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">volcengine.com（火山引擎）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">註冊 → 開通方舟 → 創建 API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">註冊送大量 Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenAI GPT</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">platform.openai.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">註冊 → 綁定信用卡 → 創建 API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">冇免費額度（要付費）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Anthropic Claude</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">console.anthropic.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">註冊 → 綁卡 → 創建 API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新用戶少量額度</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
主流模型 API 平臺同 Key 獲取方式（2026 年 8 月）

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
安全提示：API Key = 銀包密碼

{class="mt-1"}
API Key 等同於你嘅銀包密碼——任何拎到 Key 嘅人都可以用你嘅額度調用模型。因此：永遠唔好將 API Key 寫喺代碼中（用環境變數管理）；永遠唔好將含 Key 嘅代碼提交到公開嘅 Git 倉庫；永遠唔好喺社交媒體分享含 Key 嘅截圖。如果 Key 洩露咗，即刻喺平臺上刪除並重新創建。
:::

##### 3. 第一次 API 調用

取得 API Key 之後，你可以用任何編程語言調用大模型 API。以下用 Python 演示一個最簡單嘅調用——向 DeepSeek 發送一條訊息並攞回覆。

::: div .code-block
:::inline div .code-head
<span>PYTHON · 第一次 API 調用</span><span class="dots">···</span>
:::

```
# 安裝SDK：pip install openai
# DeepSeek兼容OpenAI SDK格式，可以直接用
from openai import OpenAI
import os

# 1. 建立客戶端（API Key從環境變數讀取）
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 2. 發送請求
response = client.chat.completions.create(
    model="deepseek-chat",  # 指定模型
    messages=[
        {"role": "system", "content": "你係一個Python編程助手。"},
        {"role": "user", "content": "寫一個快速排序函數。"}
    ]
)

# 3. 攞回覆
print(response.choices[0].message.content)

# 4. 睇Token消耗
print(f"輸入Token: {response.usage.prompt_tokens}")
print(f"輸出Token: {response.usage.completion_tokens}")
print(f"總Token: {response.usage.total_tokens}")
```
:::

呢段代碼嘅核心邏輯係：創建用戶端（帶住 API Key 同模型地址）→ 構造訊息列表（system 設定角色，user 係用戶輸入）→ 發送請求 → 攞回覆。呢個模式幾乎適用於所有兼容 OpenAI 格式嘅模型——只需要更換 api_key 同 base_url 就能夠切換模型。呢個就係點解好多國產模型揀兼容 OpenAI SDK 格式：開發者只需改兩行代碼就能夠切換模型，遷移成本極低。

以下係切換到其他模型嘅代碼差異——留意只需要改兩行：

::: div .code-block
:::inline div .code-head
<span>PYTHON · 切換模型只需改兩行</span><span class="dots">···</span>
:::

```
# DeepSeek
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
# model="deepseek-chat"

# 通義千問（百鍊平臺）
client = OpenAI(
    api_key=os.environ.get("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
# model="qwen-plus"

# 智譜GLM
client = OpenAI(
    api_key=os.environ.get("GLM_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4"
)
# model="glm-4"

# OpenAI GPT
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    # base_url使用預設值即可
)
# model="gpt-5.6-terra"
```
:::

##### 4. 流式響應處理

喺實際應用中，你通常唔希望等 AI 寫完所有內容先至一次性顯示——咁樣會令用戶等太耐。流式響應（Streaming）可以令你喺 AI 生成嘅同時逐字顯示，大幅提升用戶體驗。就好似打字機一樣，字一個一個彈出嚟，用戶嘅感覺係完全唔同嘅。

::: div .code-block
:::inline div .code-head
<span>PYTHON · 流式響應</span><span class="dots">···</span>
:::

```
# 串流回應：逐字輸出
stream = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "寫一個Python嘅冒泡排序教程"}
    ],
    stream=True  # 開啓流式響應
)

# 逐塊接收並打印
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)
# 輸出會好似打字機噉逐字顯示
```
:::

#### 五、Token Plan 購買指南

大多數模型供應商有兩種計費方式：按量計費（Pay-as-you-go）同套餐訂閱（Token Plan / Subscription）。理解呢兩種方式嘅區別，能夠幫你大幅降低使用成本。

##### 1. 按量計費 vs 套餐訂閱

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">維度</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">按量計費(Pay-as-you-go)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">套餐訂閱(Subscription)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">計費方式</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用幾多 Token 付幾多錢</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">預付固定費用，獲得額度</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">適合場景</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">使用量唔穩定、偶爾調用</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">使用量穩定、高頻調用</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">價格優勢</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">標準價</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">平過按量計20%-50%</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">靈活性</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">隨時可用，唔使承諾</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需要預付，額度過期可能作廢</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">超額處理</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自動按量計費</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">超出額度後轉為按量計費</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">代表平臺</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">各個模型嘅官方API平臺</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenAI Plus/Pro, Claude Pro, Cursor Pro</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
兩種計費方式嘅對比

對於初學者，建議由按量計費開始——唔需要預付費用，用幾多花幾多。當你嘅月使用量穩定喺一個水平之後（例如每月超過 50 蚊），再考慮切換到套餐訂閱以獲得更低單價。

##### 2. 主流訂閱套餐一覽

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">套餐</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">月費</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">包含內容</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">適合人羣</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ChatGPT Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">免費</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Luna 無限文本對話</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">零基礎體驗</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ChatGPT Plus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$20/月</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Sol、圖像生成、數據分析、插件訪問</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">中度用戶</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ChatGPT Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$200/月</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">無限制使用所有模型、優先訪問新功能</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">重度專業用戶</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">免費</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">有限次數Claude對話</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">零基礎體驗</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$20/月</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">無限制Claude使用、優先訪問新模型</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">編程開發者</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">免費</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">有限次數AI補全同對話</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">初學者體驗</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$20/月</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">無限AI補全、500次/月進階請求</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">日常開發者</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor Business</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$40/月/人</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">團隊協作、管理後臺、私隱模式</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">團隊使用</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
主流 AI 工具訂閱套餐（2026 年 8 月）

國內模型嘅訂閱方案略有唔同。DeepSeek 主要按量計費，冇月度訂閱套餐——你充值後按實際使用量扣費。通義千問喺百煉平臺提供預付費資源包（購買一定量嘅 Token 額度，享受折扣價）。豆包喺火山引擎上亦有類似嘅預付費方案。對於國內開發者，最經濟嘅組合通常係：DeepSeek 按量計費（日常開發）+ 豆包免費額度（體驗測試）。

##### 3. API 聚合平臺

如果你需要同時使用多個模型，API 聚合平臺係一個慳心嘅選擇。聚合平臺提供一個統一嘅 API Key，你就能夠調用全球幾十種模型，唔使喺每個平臺分別註冊。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">平臺</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">特點</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">價格優勢</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">適合場景</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenRouter (openrouter.ai)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">海外聚合平臺，一個Key調用全球模型</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">價格透明，支援即時比價</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需要靈活切換多個海外模型</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SiliconFlow (siliconflow.cn)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">國內聚合平臺，提供多種國產模型API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">平過官方20%-30%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">國內開發者，多模型比價</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Azure OpenAI（微軟代理）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">微軟Azure代理嘅OpenAI API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Batch API 可以打五折</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">企業級OpenAI調用，大批量非同步任務</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">百度千帆（qianfan.baidubce.com）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">百度AI雲平臺，提供文心等模型</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新用戶送額度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">百度生態用戶</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
主流 API 聚合平臺（2026 年 8 月）

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
避坑提醒：唔好買「共享 Key」

{class="mt-1"}
唔好喺淘寶、閒魚等平臺買啲所謂嘅「共享 API Key」——呢啲 Key 通常來路不明，隨時可能被封號，仲有資料外洩嘅風險。記住一定要經官方平臺或者正規聚合平臺攞 API Key。
:::

##### 4. 成本優化策略

揀啱模型只係第一步，點樣「用得慳錢」同樣重要。以下係幾個經過實踐驗證嘅成本優化策略：

1. 善用快取命中。好多模型都有「快取」功能——當你嘅請求包含之前處理過嘅內容（例如系統提示詞），呢部分只會用超低價錢計費。DeepSeek 嘅快取命中價錢只係普通價錢嘅 1/60。將固定嘅系統提示放喺訊息列表開頭，就可以令快取命中最大化。
2. 分級路由——用平價模型處理簡單任務，貴價模型處理複雜任務。例如用 DeepSeek V4 Flash 做文本分類（輸出 2 元/百萬 Token），用 Claude 做架構設計（輸出 181 元/百萬 Token）。一個項目入面 80% 嘅呼叫都可以用平價模型搞掂。
3. 限制輸出長度。API 係按輸出 Token 計費，輸出越長越貴。喺唔需要長篇大論嘅場景，設定 max_tokens 參數去限制輸出長度，免得 AI「廢話太多」。
4. 用 Batch API 處理非實時任務。如果你有大量唔需要即時回應嘅任務（例如批量數據標註、檔案摘要），用 Batch API 可以平一半。OpenAI 同 Azure 都有呢個功能。
5. 監察 Token 用量。大部分 API 平臺都有用量統計面板。定期睇嚇用量分佈，搵出消耗 Token 最多嘅呼叫，再針對性咁優化。小小一個 Prompt 調整（例如將「請詳細解釋」改成「請用 3 句話解釋」）隨時可以慳返 50% 嘅 Token。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">優化策略</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">慳到幾多</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">實施難度</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">說明</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">快取命中</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最高98%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">低</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">將固定內容放喺訊息開頭</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分級路由</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">50%-80%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">中</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">簡單任務用平價模型</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">限制輸出長度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">30%-60%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">低</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">設定max_tokens參數</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Batch API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">50%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">低</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">非實時任務用批處理</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prompt優化</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">20%-50%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">中</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">精簡Prompt，減少冗餘</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
成本優化策略及效果（2026 年 8 月）

#### 六、實戰：喺項目入面接入大模型 API

等我哋用一個完整嘅實戰嚟完結呢一章——整一個「AI 摘要產生器」：用戶輸入一段長文本，呼叫大模型 API 產生摘要。呢個實戰會展示 API 呼叫嘅完整流程：環境配置、API 呼叫、錯誤處理、成本控制。

::: div .code-block
:::inline div .code-head
<span>PYTHON · ai_summarizer.py</span><span class="dots">···</span>
:::

```
# ai_summarizer.py - AI摘要生成器
import os
from openai import OpenAI

# 1. 配置（API Key從環境變數讀取，絕不硬編碼）
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def summarize(text: str, max_length: int = 200) -> dict:
    """生成文本摘要

    Args:
        text: 要摘要嘅原文
        max_length: 摘要最大長度（Token數）

    Returns:
        dict: 包含摘要同Token消耗資訊
    """
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "system",
                    "content": "你係一個摘要生成器。"
                               "請用簡潔嘅中文總結用戶提供嘅文本。"
                               "摘要不超過3句話。"
                },
                {
                    "role": "user",
                    "content": f"請摘要以下文本:\n\n{text}"
                }
            ],
            max_tokens=max_length,  # 限制輸出長度
            temperature=0.3  # 低溫度=更穩定
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
    （粘貼一段長文本...）
    """

    result = summarize(long_text)

    if result["success"]:
        print(f"摘要: {result['summary']}")
        print(f"消耗Token: {result['total_tokens']}")
        # 估算成本：DeepSeek V4 Flash
        cost = result['total_tokens'] * 0.000004  # 約0.4分/千Token
        print(f"預估成本: {cost:.4f}元")
    else:
        print(f"出錯咗: {result['error']}")
```
:::

呢段代碼體現咗 API 呼叫嘅幾個最佳實踐：API Key 係透過環境變數讀取，絕對唔會寫死喺代碼入面；函數有清晰嘅文檔同類型提示；設定咗 max_tokens 去限制輸出長度；temperature 設做低值（0.3）等輸出更穩定；有完整嘅錯誤處理；仲會傳回 Token 消耗資訊用嚟追蹤成本。當你用 AI 嚟寫呢段代碼嗰陣，可以話畀佢知呢啲要求——佢完全有能力幫你實現。

:::inline div .quote-line
本章嘅最終啟示：模型係"彈藥"，方法論係"戰術"。揀啱彈藥可以令戰鬥順啲，但冇好戰術，幾勁嘅彈藥都打唔贏仗。瞭解到各模型嘅特點同 API 用法之後，你就有一個充足嘅"彈藥庫"——但係點樣打呢場仗，仲係要靠前幾章學到嘅思維方法論。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
嚟動手：搞掂你嘅第一次 API 呼叫

{class="mt-1"}
註冊一個國產模型平臺（推薦 DeepSeek 或者智譜，兩家都送新用戶額度），整一個 API Key，將佢寫入系統環境變數（唔好寫入代碼入面！），然後行嚇上面「第一次 API 呼叫」嘅代碼。睇到 AI 嘅回覆打印出嚟嗰一刻，你就跨過咗「用 AI」同「整 AI 應用」之間嘅分界線。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 國際三強：GPT-5.6（均衡全能）、Claude（編程天花板+幻覺率只係1%）、Gemini（多模態之王+200萬上下文）
- 國產五強：DeepSeek V4（性價比之王，留意加價公告）、Qwen3.7（企業級）、GLM-5.1（SWE國產第一）、Kimi K3（超長文本）、豆包（免費入門）
- 四問決策法：部署喺邊？編程定係其他？使唔使超長上下文？預算敏唔敏感？
- Token 係計費單位：中文 1 個字大約 1.5-2 Token；100萬字大約150萬Token
- API Key = 銀包密碼：用環境變數管理，絕對唔好寫死、唔好擺上Git
- 國產模型普遍都兼容 OpenAI SDK：轉模型只需改 api_key 同 base_url 兩行
- 慳錢五招：快取命中、分級路由、限制輸出、Batch API、監察用量
:::
