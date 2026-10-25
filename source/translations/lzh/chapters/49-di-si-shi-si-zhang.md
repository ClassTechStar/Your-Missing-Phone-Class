---
id: di-si-shi-si-zhang
num: 44
part: ai-biancheng-pian
nav: 第四十四章：自0至1實戰——完整項目全流程
toc: default
kind: chapter
---

### 第四十四章：自0到1之實戰——完整項目全流程

{class="chapter-intro mb-4"}
理論學完了，而今為動手之時。本章不為簡單之「照著敲」教程，乃一套「何以想、何以問、何以驗」之實戰方法論。吾儕會用三個不同難度之項目，展示從需求到成品之完整思考過程。無論汝用哪個工具，此套流程皆適用。

#### 一、項目一：極簡個人工具站（入門級）

##### 1. 需求思考

目標：創建一個個人工具站網頁，展示3-4個實用小工具之入口。此乃一個純前端項目，不須後端與數據庫。重點不為工具本身有多複雜，乃體驗「從需求到成品」之完整流程。

按照需求五要素：Who——個人使用。What——一個展示工具入口之網頁。Why——將常用工具集中於一個頁面方便訪問。How——單檔案HTML+CSS+JS，不使用框架。Constraint——30分鐘內完成，不須部署。

##### 2. 下達指令

基於Think Before Coding原則，汝之指令應包含足夠之信息使AI理解目標，但不須指定每個實現細節：

::: div .code-block
:::inline div .code-head
<span>予 AI 之指令</span><span class="dots">···</span>
:::

```
請創建一個個人工具站網頁，要求：
1. 單文件HTML（內聯CSS與JS），不使用框架
2. 暗色主題，現代極簡風格
3. 展示4個工具入口卡片：
   - 文本摘要工具
   - 字數統計工具
   - 顏色選擇器
   - 二維碼生成器
4. 每個卡片有圖標、標題、簡短描述
5. 卡片有懸停動畫效果
6. 響應式佈局，手機上可用
7. 頂部有一個標題欄
請直接予出完整之HTML文件。
```
:::

##### 3. 驗收與迭代

AI予出代碼後，按照迭代驗證之三層檢查進行驗收。第一層功能驗證：檔案能否於瀏覽器中打開？4個卡片為否皆顯示了？懸停動畫為否正常？第二層邊界驗證：於手機屏幕尺寸下佈局為否正常？窗口甚窄時卡片為否會換行？第三層架構驗證：代碼為否可讀？CSS為否內聯於一個style標籤中？有無明顯之冗餘？

若某個工具卡片之功能也想實現（而不只為入口），可逐步添加——每次添加一個工具之功能，驗證後再添加下一個。此即「小步快跑」策略之實際應用。

#### 二、項目二：全棧記賬系統（進階級）

##### 1. 需求思考與PRD

目標：一個有前端、後端與數據庫之全棧記賬應用。此項目比第一個複雜得多，須用到第四十章之需求工程方法。

先寫PRD。按照第四十章第三節之模板，寫出項目概述、功能列表、技術方案、數據模型與開發計劃。技術方案之選擇要考慮Simplicity First原則——前端用React但不引入Redux等複雜狀態管理，後端用Node.js但不引入微服務，數據庫用SQLite而非PostgreSQL（開發階段）。

開發計劃拆解為5步：Step 1後端API骨架（Express服務器＋SQLite＋CRUD接口）；Step 2前端基礎頁面（記錄列表＋添加表單）；Step 3前後端聯調（API調用＋數據展示）；Step 4分類與篩選功能；Step 5月度彙總與簡單圖表。每步完成後皆為「能用之東西」。

##### 2. 設置項目記憶檔案

於開始編碼之前，先創建項目記憶檔案。此乃上下文工程之核心實踐——使AI於每次對話開始時皆瞭解項目背景。

::: div .code-block
:::inline div .code-head
<span>CLAUDE.md</span><span class="dots">···</span>
:::

```
# 項目：全棧記賬應用
## 概述
個人記賬應用，支持收支記錄、分類、月度彙總。
## 技術棧
- 前端：React + TypeScript + Vite
- 後端：Node.js + Express + TypeScript
- 數據庫：SQLite (通過 better-sqlite3)
- 前後端共享類型定義
## API約定
- 基礎路徑：/api
- 返回格式：{ success: boolean, data: any, error: string }
- RESTful風格
## 數據模型
Record { id, amount, type, category, note, date }
## 代碼規範
- TypeScript嚴格模式
- 縮進2空格
- 函數有JSDoc註釋
- 中文註釋與提交信息
```
:::

##### 3. 逐步實現

按照開發計劃，每一步用一個獨立之對話來完成。以下為第一步之指令示例：

::: div .code-block
:::inline div .code-head
<span>予 AI 之指令（Step 1）</span><span class="dots">···</span>
:::

```
吾需後端API之骨。
要求：
1. Express服務器，端口3001
2. SQLite數據庫，表名records
3. records表字段：
   id (TEXT PRIMARY KEY)
   amount (REAL)
   type (TEXT: 'income'|'expense')
   category (TEXT)
   note (TEXT)
   date (TEXT: YYYY-MM-DD)
4. CRUD接口：
   GET /api/records - 取所有記錄
   POST /api/records - 新增記錄
   PUT /api/records/:id - 更新記錄
   DELETE /api/records/:id - 刪除記錄
5. 錯誤處理中間件
請予完整之後端代碼結構。
```
:::

注意此指令之特點：它只描述當前此一步（後端骨架），不摻雜前端需求；它明確列出了字段與接口（予AI足夠之約束），但具體實現由AI決定；它遵循了Goal-Driven Execution原則——說「做何」而非「何以做」。

AI予出代碼後，立即驗證：運行服務器，用curl或Postman測試每個接口為否正常工作。確認無誤後，開新對話處理Step 2（前端基礎頁面）。每一步皆遵循「指令—驗證—新對話」之循環。

#### 三、項目三：AI增強應用（高級）

##### 1. 項目構思

目標：一個接入大模型API之應用——譬如一個「AI學習助手」，用戶輸入學習內容，AI生成摘要、關聯知識點、推薦學習資源。此項目之特殊之處於於：汝之應用本身就於調用AI，汝須處理API調用、prompt工程、錯誤處理等新問題。

此項目教會汝之最重要一課乃為：當汝「用AI來寫調用AI之代碼」時，汝須格外注意prompt工程。汝之應用調用大模型API時所用之prompt，也須遵循本指南所討論之原則——清晰、簡潔、目標驅動。

##### 2. 關鍵技術點

此項目涉及幾個汝於前兩個項目中沒遇到之技術點：

- API密鑰管理：密鑰絕不能硬編碼於代碼中，用環境變量管理；
- 流式響應處理：大模型之回覆通常為流式之，須逐字顯示；
- Token用量控制：大模型按token計費，須於應用層面控制用量；
- Prompt模板管理：不同功能用不同之prompt模板，須結構化管理。

此諸技術點皆可使AI助汝實現，但汝須理解每個技術點之「為何」——為何密鑰不能硬編碼？為何須流式響應？為何token用量須控制？理解了「為何」，汝才能判斷AI之方案為否合理。

#### 四、通用實戰流程清單

無論項目大小，以下為一個通用之AI編程實戰流程清單。每次開始新項目時，過一遍此清單，確保無遺漏關鍵步驟。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">階段</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">做何</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">對應原則</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1. 需求思考</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">過一遍需求五要素，想清楚要做何</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Think Before Coding</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2. 需求拆解</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">將大需求拆成可獨立驗證之小步驟</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Simplicity First</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3. 寫PRD</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">整理成結構化文檔，作為參考</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Goal-Driven</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">4. 設置記憶檔案</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">創建CLAUDE.md或同類檔案</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Harness Engineering</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">5. 逐步實現</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每步一個對話，指令—驗證—下一步</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Surgical Changes</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6. 測試驗證</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每步完成後立即測試功能之正確性</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">7. 代碼審查</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">檢查架構合理性、安全性、可維護性</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8. 迭代優化</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">根據測試與審查結果迭代改進</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
AI編程通用實戰流程清單

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
動手一試：本週完成「項目一」

{class="mt-1"}
將第四十四章第一節之「個人工具站」當成汝之第一個AI編程作業：花5分鐘過五要素，將指令發予AI（任何工具皆行），再按三層驗證驗收。30分鐘內完成它——汝之第一個AI編程作品就誕生了。做完記得將它存好，此乃汝從「讀者」變成「實踐者」之紀念品。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 項目一（入門）：純前端工具站——體驗完整流程，30分鐘能完成
- 項目二（進階）：全棧記賬系統——PRD＋記憶檔案＋5步逐步實現，每步「能用」
- 項目三（高級）：AI學習助手——用AI寫調用AI之代碼，注意prompt工程
- 通用流程八步：需求思考→拆解→PRD→記憶檔案→逐步實現→測試→審查→迭代
- 每一步皆遵循「指令—驗證—新對話」循環
:::
