---
id: di-san-shi-jiu-zhang
num: 39
part: ai-biancheng-pian
nav: 第三十九章：上下文工程——使AI理解爾之意圖
toc: default
kind: chapter
---

### 第三十九章：上下文之工——使 AI 解爾之意

{class="chapter-intro mb-4"}
爾有此驗乎：易一新對話之窗，AI 如失憶然，盡忘爾項目之概。此非 AI 故慍爾，乃其天性「健忘」。此章授爾為 AI 裝一套「長憶之系」，且識 2026 年至火開發範式之一——規範驅動之開發。

#### 一、項目記憶之檔：AI 之「長憶」

AI 之模型有一根本之限：其憶乃「短時」者。每對話之始，AI 於爾項目所知為零。爾須於對話中屢告之曰「吾儕用 React」「後端乃 Node.js」「數據之庫乃 PostgreSQL」「碼之風用雙引號」。此非惟低效，且易有遺——如日日為新至之同僚復作入職之訓。

解之之方，乃「項目記憶之檔」——置於項目根目錄之純文字之檔，AI 之器每於對話之始自讀之。異器異其命名之約：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">其器</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">檔之名</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cursorrules</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">CLAUDE.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitHub Copilot</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">copilot-instructions.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">通用之方</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">AGENTS.md</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
諸器項目記憶之檔命名之約

名雖異，理則一：以爾欲 AI「恆記」之訊，書於此檔。善之項目記憶檔當含：項目之概（此何項目）、技術之棧（用何技）、碼之規（命名、縮進、註之風）、目錄之構（碼何以組織）、開發之約（分支之策、提交之規、測試之求）。Karpathy 之 CLAUDE.md 惟 70 行，然要訊悉備——簡而完也。

::: div .code-block
:::inline div .code-head
<span>CLAUDE.md</span><span class="dots">···</span>
:::

```
# 項目：個人記賬應用
## 概述
此為一個全棧個人記賬應用，助用戶記日常收支。
## 技術棧
- 前端：React + TypeScript + Tailwind CSS
- 後端：Node.js + Express + TypeScript
- 數據庫：SQLite (開發) / PostgreSQL (生產)
- 測試：Vitest
## 代碼規範
- 用雙引號
- 縮進2個空格
- 函數名用camelCase
- 類型定義用PascalCase
- 每個函數必須有JSDoc註釋
## 目錄結構
/src
  /frontend  - 前端代碼
  /backend   - 後端代碼
  /shared    - 前後端共享之類型
  /tests     - 測試文件
## 開發約定
- 提交信息用中文
- 新功能必須先寫測試
- API返回統一用 { success, data, error } 格式
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
慎之：毋作「第二份需求之文」

{class="mt-1"}
留心此檔之長——毋作數十頁需求之文。項目記憶檔之旨，於「使 AI 速立背景之知」，非「詳述每功」。宜簡、宜有序、惟書「AI 所當知」。
:::

#### 二、規範驅動之開發（SDD）

Spec-Driven Development（SDD，規範驅動之開發）者，2026 年漸熟之開發範式也，其核之念一言：先作規範，後作碼。異乎舊 TDD（測試驅動之開發）者，SDD 之「規範」非惟測試之例，並含需求之述、接口之定、數據之模之屬。AI 據此規範以生碼，人之職，作與守規範也。

SDD 工作之流程，五步而行：

1. 以自然之語述需求之規範（書於一 .md 之檔）；
2. 定接口與數據之構（書於規範之檔）；
3. 使 AI 據規範生碼以實現之；
4. 行測試以驗所產副規範否；
5. 不副，則正其規範，或使 AI 正其碼。

此流程之中，規範之檔乃「唯一真理之源」——碼可復生，規範必先正。

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> 編寫規範文件</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> 審查規範為否完備？</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> 完備</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> AI 根據規範生成代碼</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> 運行測試驗證產出</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> 不完備 / 測試不過</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-tools mr-1"></i> 代碼問題 → 修正代碼；規範問題 → 修正規範</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> 回到驗證</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> 全部通過 → 交付</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖三：規範驅動之開發（SDD）工作之流程
:::

SDD 之長：規範之檔較碼為穩。底層模型或器有變，爾之規範檔依然有效，惟使新 AI 之器復生其碼可矣。此亦本書故重「方法論重於器」——規範之檔，即爾方法論之具載也。

#### 三、上下文之窗之管理

雖有項目記憶之檔，爾仍將於對話中遇「上下文不足」之患。AI 模型上下文之窗（能同時理之訊量）有限。對話過長、所引之檔過眾，AI 則「忘」其早訊，產之質遂降——如與友語六小時之久，彼早忘爾始言之首事矣。

理上下文之窗之核策，乃「分層而引」：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">上下文之層</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">其內</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">管理之法</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一層：項目之憶</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">技術之棧、規範、目錄之構</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">書於 CLAUDE.md 諸檔，自載入，毋須復述</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">二層：檔之引</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">今務所涉之碼檔</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">以 @ 之符精引之，毋粘全文於對話</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">三層：對話之上下文</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">今務之對話之史</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一務既畢，開新對話，免上下文之膨脹</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">四層：即時之令</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">此一步之具體之求</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">明、簡、有之，免冗長之述</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
上下文之窗分層管理之策

#### 四、上下文之工實踐之要

上下文之工，非一時之設，乃續而優之之程也。下數端，實踐中屢驗之要：

1. 記憶之檔，隨項目之演進而偕新。引新技或改架構，第一時新其記憶之檔，毋於對話中臨時言之。
2. 善用 @ 引，毋粘全文。AI 編程之器多支持 @file 或 @folder 之語法，會於幕後將檔之內容注入 AI 之上下文，較手粘尤效，且不穢對話。
3. 對話宜「短小精悍」。一對話惟理一務或一功能之點。畢則開新對話以理其次。長對話非惟耗上下文之窗，且使 AI「分心」。
4. 使 AI「觀」其果，毋徒「述」其果。遇 bug，則以誤之日誌徑以 @ 引予 AI，毋以己語述「若有某誤」。AI 觀原訊，勝於觀爾之轉述也。
5. 定期清而歸檔。既畢之對話與臨時之檔，佔工之空間。定期清無關之內容，保項目目錄之潔，亦助 AI 更效以解項目之構。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：為爾項目作一 70 行之記憶檔

{class="mt-1"}
擇一爾方為（或欲為）之項目，作一 CLAUDE.md：項目之概（2-3 語）、技術之棧（列之）、碼之規（3-5 條）、目錄之構（畫一樹）、開發之約（2-3 條）。限 70 行以內——既成，爾將覺於項目之解，明瞭多矣。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- AI 之憶乃「短時」者：每新對話，於項目所知為零
- 項目記憶之檔（CLAUDE.md 之屬）乃 AI 之「長憶」，每對話自載入
- 善之記憶檔 = 概述+技術之棧+規+目錄+約，70 行足矣
- SDD 規範驅動之開發：先規後碼，規範乃「唯一真理之源」，較碼尤穩
- 上下文分四層而理：項目之憶→@檔之引→對話之史→即時之令
- 實踐五要：偕時而新、@引、短對話、予原訊、定期而清
:::
