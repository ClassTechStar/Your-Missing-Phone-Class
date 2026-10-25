---
id: di-si-shi-zhang
num: 40
part: ai-biancheng-pian
nav: 第四十章：需求工程——將諗法變成AI指令
toc: default
kind: chapter
---

### 第四十章：需求工程——將想法變成 AI 可執行嘅指令

{class="chapter-intro mb-4"}
如果話上下文工程解決嘅係「令 AI 瞭解背景」，咁需求工程解決嘅係「令 AI 知道今次具體要做乜嘢」。呢個係 AI 編程中最能夠體現人同人差距嘅環節——同樣嘅工具、同樣嘅模型，有人能夠做出令人驚艷嘅項目，有人只能夠做出平庸嘅玩具。區別往往唔喺技術能力，而喺需求表達能力。

#### 一、由模糊想法到結構化需求

每個項目都始於一個模糊嘅想法——「我想做一個記帳 App」「我想做個個人網站」「我想做個待辦清單工具」。呢啲想法本身冇問題，但如果你直接將佢丟畀 AI，產出嘅質量完全取決於運氣。需求工程嘅目標，就係將呢個模糊嘅想法，變成一個 AI 能夠精確執行嘅結構化需求。

好消息係：結構化需求唔需要你寫一份幾十頁嘅 PRD。佢只需要你回答五個問題，我哋稱之為「需求五要素」：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要素</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">問題</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">示例：記帳 App</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">畀邊個用？</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">個人使用，記錄日常收支</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">做乜嘢？</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一個能夠記錄每筆收支、按月匯總、可視化嘅應用</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">點解做？</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">想了解自己嘅消費結構，搵出不必要嘅支出</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">大致點樣做？</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">前端用 React，數據存瀏覽器本地，先唔做後端同登入</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">有乜嘢限制？</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">單人開發，2 週內完成，唔需要上線部署</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
需求五要素及示例

呢五個要素唔需要寫成正式文檔，甚至喺腦海中快速過一次就足夠。關鍵係養成「先想清楚再開口」嘅習慣。你會發現，當你能夠清晰咁回答呢五個問題時，你嘅需求描述自然就變咗結構化。

#### 二、需求拆解嘅分層藝術

對於較大嘅項目，一個需求描述係唔夠嘅。你需要將大需求拆解成細嘅、可獨立驗證嘅子需求。呢個過程叫做「需求拆解」，核心原則係：每個子需求都應該能夠獨立完成、獨立驗證、獨立交付。

以「做一個個人記帳 App」為例，一個合理嘅拆解方式係：

1. 實現基礎嘅收支記錄功能（能夠添加、查看、刪除記錄）；
2. 添加分類功能（畀每筆記錄打上餐飲、交通等標籤）；
3. 實現月度匯總功能（按月統計收支情況）；
4. 添加數據可視化（用圖表展示消費結構）。

每一步都係一個可以獨立運行同驗證嘅功能增量。

:::inline div .quote-line
需求拆解嘅黃金法則：每一步做完之後，個項目都應該係一件"用得嘅嘢"——就算功能好簡陋都好。千祈唔好令個項目停留喺"乜嘢都做咗一半但乜嘢都用唔到"嘅狀態。
:::

呢種拆解方式有兩個好處。首先，佢令你始終能夠睇到進展——每完成一步，你嘅 App 就多咗一個功能，呢種正反饋對於長期項目至關重要（人都係需要成就感㗎嘛）。其次，佢令 AI 嘅每次任務都足夠細，降低咗「AI 理解偏差」嘅風險——任務越細，AI 嘅理解越準確，產出質量越高。

#### 三、PRD 寫作模板同實踐

對於較大嘅項目（例如一個有前後端、多個功能模組嘅全棧應用），僅憑需求五要素可能唔夠。呢時你需要寫一份更正式嘅項目需求文檔（PRD）。一個容易誤解嘅點係：PRD 唔係寫畀 AI 睇嘅——佢係寫畀你自己嘅，幫你理清思路，然後你先能夠畀 AI 提供更精確嘅指令。

一份好嘅 PRD 唔需要好長，但應該包含六個部分：項目概述（一段話講清楚做乜嘢）、功能列表（每個功能點係乜嘢）、技術方案（用乜嘢技術棧、大致架構）、數據模型（核心數據結構）、介面描述（主要頁面係點樣嘅）、開發計劃（分幾步完成）。

::: div .code-block
:::inline div .code-head
<span>PRD.md</span><span class="dots">···</span>
:::

```
# 個人記賬應用 PRD
## 項目概述
一個輕量級個人記賬應用，支援收支記錄、分類、月度匯總同數據可視化。
## 功能列表
1. 記錄收支：金額、類型(收入/支出)、分類、備註、日期
2. 分類管理：預設餐飲、交通、購物、娛樂、其他
3. 月度匯總：按月統計總收入、總支出、結餘
4. 消費可視化：餅圖展示各分類佔比
5. 數據匯出：匯出為CSV
## 技術方案
- 前端：React + TypeScript + Tailwind CSS
- 數據儲存：localStorage（無需後端）
- 圖表：使用Chart.js
- 構建：Vite
## 數據模型
Record {
  id: string
  amount: number
  type: 'income' | 'expense'
  category: string
  note: string
  date: string  // YYYY-MM-DD
}
## 開發計劃
Step 1: 基礎記錄功能 (CRUD)
Step 2: 分類管理
Step 3: 月度匯總
Step 4: 數據可視化
Step 5: 數據匯出
```
:::

留意呢份 PRD 嘅寫作風格：用簡潔嘅列表同結構化嘅格式，而唔係長篇大論。每個功能點都有明確嘅定義，數據模型用簡單嘅類型描述。呢種風格嘅 PRD 唔單止你自己睇得清楚，當你將佢提供畀 AI 時，AI 亦能夠精確理解每個需求點。

#### 四、實戰：由想法到方案嘅完整推演

紙上談兵冇意思，我哋用一個完整嘅例子行一次需求工程嘅全過程。假設你嘅想法係：「我想做一個能夠追蹤我每日學咗乜嘢嘅學習追蹤器」。

第一步，過一次需求五要素。

- Who：個人使用。
- What：一個能夠記錄每日學習內容、追蹤學習時長、回顧學習進度嘅工具。
- Why：想養成持續學習嘅習慣，睇到自己嘅累積。
- How：先做一個網頁版，數據存喺瀏覽器本地。
- Constraint：零基礎開發，1 週內完成核心功能。

第二步，拆解需求。

1. Step 1：實現「記錄學習條目」功能（日期、內容、時長）；
2. Step 2：添加「學習時長統計」（今日、本週累計）；
3. Step 3：實現「學習日曆」視圖（好似 GitHub 貢獻圖咁樣展示）；
4. Step 4：添加「學習回顧」功能（隨機展示過去某日嘅學習記錄，幫助溫習）。

第三步，寫一份簡短 PRD。唔使好長——上面嘅拆解本身就構成咗 PRD 嘅主體。將佢整理成一個 .md 檔案，放喺項目根目錄，作為你同 AI 嘅共同參考。

第四步，開始第一步嘅開發。畀 AI 嘅指令可以係：

::: div .code-block
:::inline div .code-head
<span>畀 AI 嘅指令</span><span class="dots">···</span>
:::

```
我需要一個學習追蹤器嘅第一個功能——記錄學習條目。
用戶可以添加一條學習記錄，包含日期、學習內容、學習時長（分鐘）。
數據存在localStorage。
前端用React + TypeScript。
請畀出完整實現。
```
:::

留意呢個指令嘅特點：佢只描述當前呢一步嘅目標（記錄功能），唔摻雜其他功能；佢明確咗技術約束（React、TypeScript、localStorage）；佢畀咗足夠嘅資訊令 AI 知道「做乜嘢」同「點樣做」，但具體實現由 AI 決定。呢個就係一個經過需求工程加工後嘅、高質量嘅 AI 編程指令。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
嚟動手：畀你嘅「心頭好」寫一份五要素卡

{class="mt-1"}
揀一個你醞釀已久嘅小項目，花 5 分鐘填一張卡：Who / What / Why / How / Constraint，各一句話。然後將佢拆成 3-5 個「每一步都用得」嘅步驟。你會發現：將想法寫低之後，佢就由「白日夢」變成「待辦清單」。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 需求五要素：Who / What / Why / How / Constraint——想清楚再開口
- 需求拆解黃金法則：每一步完成後項目都係「用得嘅嘢」
- PRD 係寫畀自己嘅：概述、功能列表、技術方案、數據模型、介面、計劃
- 好指令 = 只描述當前一步 + 明確約束 + 講「做乜嘢」唔講「點樣做」
- 完整推演模板：五要素 → 拆解 → PRD → 畀指令，四步走
:::
