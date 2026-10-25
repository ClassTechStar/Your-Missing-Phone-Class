---
id: di-san-shi-jiu-zhang
num: 39
part: ai-biancheng-pian
nav: 第三十九章：上下文工程——畀AI理解你嘅意圖
toc: default
kind: chapter
---

### 第三十九章：上下文工程——令 AI 理解你嘅意圖

{class="chapter-intro mb-4"}
你有冇過呢種體驗：換個新對話視窗，AI 就好似失憶咗一樣，將你項目嘅基本情況全部唔記得？呢個唔係 AI 特意激你，而係佢天生「善忘」。呢一章教你畀 AI 裝上一套「長期記憶系統」，順便認識 2026 年最火嘅開發範式之一——規範驅動開發。

#### 一、項目記憶檔案：AI 嘅「長期記憶」

AI 模型有一個根本性限制：佢嘅記憶係「短時」嘅。每次對話開始時，AI 對你項目嘅瞭解為零。你需要喺對話中不斷話佢知「我哋用嘅係 React」「後端係 Node.js」「數據庫係 PostgreSQL」「代碼風格用雙引號」。呢個唔單止低效，而且容易遺漏——就好似每日都要重新畀新嚟嘅同事做入職培訓。

解決方案係「項目記憶檔案」——一個放喺項目根目錄嘅純文本檔案，AI 工具會喺每次對話開始時自動讀取佢。唔同嘅工具有唔同嘅命名約定：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">工具</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">檔案名</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cursorrules</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">CLAUDE.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitHub Copilot</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">copilot-instructions.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">通用方案</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">AGENTS.md</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
各工具嘅項目記憶檔案命名約定

雖然命名唔同，但原理一樣：將你希望 AI「始終記住」嘅資訊寫喺呢個檔案入面。一個好嘅項目記憶檔案應該包含：項目概述（呢個係乜嘢項目）、技術棧（用咗乜嘢技術）、代碼規範（命名、縮排、註釋風格）、目錄結構（代碼點樣組織嘅）、開發約定（分支策略、提交規範、測試要求）。Karpathy 嘅 CLAUDE.md 只有 70 行，但覆蓋咗所有關鍵資訊——簡潔但完備。

::: div .code-block
:::inline div .code-head
<span>CLAUDE.md</span><span class="dots">···</span>
:::

```
# 項目：個人記賬應用
## 概述
呢個係一個全棧個人記賬應用，幫用戶記錄日常收支。
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
  /shared    - 前後端共享嘅類型
  /tests     - 測試檔案
## 開發約定
- 提交資訊用中文
- 新功能必須先寫測試
- API返回統一用 { success, data, error } 格式
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
留意：唔好寫成「第二份需求文檔」

{class="mt-1"}
留意呢個檔案嘅長度——唔好寫成幾十頁嘅需求文檔。項目記憶檔案嘅目的係「令 AI 快速建立背景認知」，唔係「詳細描述每個功能」。保持簡潔、結構化、只寫「AI 需要知道嘅」。
:::

#### 二、規範驅動開發（SDD）

Spec-Driven Development（SDD，規範驅動開發）係 2026 年逐漸成熟嘅一種開發範式，核心理念一句話：先寫規範，再寫代碼。同傳統 TDD（測試驅動開發）唔同嘅係，SDD 嘅「規範」唔單止係測試用例，仲包括需求描述、接口定義、數據模型等。AI 根據呢啲規範嚟生成代碼，人類嘅職責係編寫同維護規範。

SDD 嘅工作流程五步走：

1. 用自然語言描述需求規範（寫喺一個 .md 檔案中）；
2. 定義接口同數據結構（寫喺規範檔案中）；
3. 等 AI 根據規範生成代碼實現；
4. 運行測試驗證產出係咪符合規範；
5. 如果唔符合，修正規範或者等 AI 修正代碼。

喺呢個流程中，規範檔案係「唯一真理源」——代碼可以重新生成，但規範必須先正確。

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> 編寫規範檔案</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> 審查規範係否完備？</span>
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
圖 3：規範驅動開發（SDD）嘅工作流程
:::

SDD 嘅優勢喺於：規範檔案比代碼更穩定。當底層模型或者工具變化時，你嘅規範檔案依然有效，只需要畀新嘅 AI 工具重新生成代碼就可以。呢個亦係點解本書強調「方法論比工具重要」——規範檔案就係你方法論嘅具體載體。

#### 三、上下文視窗管理

即使有咗項目記憶檔案，你仍然會喺對話中遇到「上下文唔夠用」嘅問題。AI 模型嘅上下文視窗（能夠同時處理嘅資訊量）係有限嘅。當對話太長、引用嘅檔案太多時，AI 會「唔記得」早期嘅資訊，導致產出質量下降——就好似你同一個朋友傾偈傾偈傾咗六個鐘，佢一早唔記得你開頭講嘅第一件事。

管理上下文視窗嘅核心策略係「分層引用」：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">上下文層次</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">內容</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">管理方式</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第一層：項目記憶</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">技術棧、規範、目錄結構</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">寫喺 CLAUDE.md 等檔案中，自動加載，唔使重複</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第二層：檔案引用</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">當前任務涉及嘅代碼檔案</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用 @ 符號精確引用，唔好貼全文到對話</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第三層：對話上下文</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">當前任務嘅對話歷史</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">完成一個任務後開新對話，避免上下文膨脹</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第四層：即時指令</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">當前呢一步嘅具體要求</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">清晰、簡潔、有針對性，避免冗長描述</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
上下文視窗嘅分層管理策略

#### 四、上下文工程嘅實踐要點

上下文工程唔係一次性嘅設定，而係一個持續優化嘅過程。以下係幾個喺實踐中被反覆驗證嘅要點：

1. 記憶檔案隨項目演進同步更新。引入新技術或者改變架構時，第一時間更新記憶檔案，而唔係喺對話中臨時說明。
2. 善用 @ 引用而唔係全文貼上。大多數 AI 編程工具支援 @file 或者 @folder 語法，佢會喺後臺將檔案內容注入 AI 嘅上下文，比手動貼上更高效而且唔會污染對話。
3. 對話要「短小精悍」。一個對話只處理一個任務或者一個功能點。完成後開新對話處理下一個。長對話唔單止消耗上下文視窗，仲會令 AI「分心」。
4. 畀 AI「睇」結果而唔係「描述」結果。遇到 bug 時，將錯誤日誌直接 @ 引用畀 AI，而唔係用自己嘅話描述「好似有個乜嘢錯誤」。AI 睇到原始資訊比睇到你嘅轉述更有效。
5. 定期清理同歸檔。已完成嘅對話同臨時檔案會佔用工作空間。定期清理無關內容，保持項目目錄整潔，亦有助於 AI 更高效咁理解項目結構。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
嚟動手：畀你嘅項目寫一份 70 行記憶檔案

{class="mt-1"}
揀一個你正在做（或者打算做）嘅項目，寫一份 CLAUDE.md：項目概述（2-3 句話）、技術棧（列出來）、代碼規範（3-5 條）、目錄結構（畫個樹）、開發約定（2-3 條）。控制喺 70 行以內——寫完你會發現自己對項目嘅理解都清晰咗好多。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- AI 嘅記憶係「短時」嘅：每次新對話，佢對項目嘅瞭解為零
- 項目記憶檔案（CLAUDE.md 等）係 AI 嘅「長期記憶」，每次對話自動加載
- 好嘅記憶檔案 = 概述 + 技術棧 + 規範 + 目錄 + 約定，70 行夠曬
- SDD 規範驅動開發：先寫規範再寫代碼，規範係「唯一真理源」，比代碼更穩定
- 上下文分四層管理：項目記憶 → @檔案引用 → 對話歷史 → 即時指令
- 五個實踐要點：同步更新、@引用、短對話、畀原始資訊、定期清理
:::
