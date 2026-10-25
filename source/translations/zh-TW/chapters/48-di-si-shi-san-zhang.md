---
id: di-si-shi-san-zhang
num: 43
part: ai-biancheng-pian
nav: 第四十三章：對話工程——高效對話技術
toc: default
kind: chapter
---

### 第四十三章：對話工程——與AI高效協作的對話技術

{class="chapter-intro mb-4"}
對話是 AI 程式設計的核心互動方式。但請注意："對話"不等於"聊天"——高效的 AI 程式設計對話是一種有結構的溝通技術，我們稱之為"對話工程"。它研究的是：如何用最少的對話輪次，獲得最高品質的程式碼產出。說白了，這一章就是教你怎麼和 AI"把話說清楚"。

#### 一、Prompt 分層策略

與 AI 的對話可以分為三個層次，每層承擔不同的功能。理解這三個層次，你就能像搭積木一樣組合出高效的 Prompt。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">層次</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">功能</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">示例</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">頻率</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系統層</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">設定AI的角色和全域性約束</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"你是一個React專家，程式碼必須用TypeScript"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">專案開始時設定一次</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">任務層</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">描述當前要做的具體任務</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"實現一個表單元件，包含使用者名稱和密碼欄位"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每個任務開始時給出</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">反饋層</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">對AI產出進行評價和修正</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"密碼欄位缺少顯示/隱藏切換，請新增"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">根據產出品質給出</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
對話 Prompt 的三個層次

系統層的 Prompt 通常寫在專案記憶檔案中（如 CLAUDE.md），不需要每次對話重複。任務層是你在對話中最常使用的——它應該包含"做什麼""用什麼技術""有什麼約束"三個要素。反饋層是最考驗功力的——好的反饋能讓 AI 精準修正，壞的反饋只會讓它重新猜測。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：反饋三板斧

{class="mt-1"}
一個實用的反饋模板是"指出問題 + 說明期望 + 提供上下文"。比如："第 25 行的錯誤處理只用了 console.log（指出問題），生產環境應該用統一的錯誤處理器並返回使用者友好提示（說明期望），專案裡有一個 handleError 函式可以用（提供上下文）"。這種反饋比"改一下錯誤處理"有效十倍。
:::

#### 二、除錯對話：如何描述錯誤讓 AI 快速定位

除錯是 AI 程式設計中最頻繁的場景之一。當你遇到 bug 時，如何向 AI 描述問題，直接決定了它能否快速幫你定位和修復。以下是除錯對話的四個要點：

1. 給 AI"看"原始資訊，而不是你的轉述。把錯誤日誌、異常堆疊、相關程式碼直接 @ 引用給 AI，而不是用"好像有個什麼報錯"來描述。AI 看到原始資訊比看到你的理解更準確。
2. 描述"期望行為"和"實際行為"的差異。"我期望點選按鈕後跳轉到首頁（期望），但實際點選後頁面沒有反應（實際）"——這種描述比"按鈕壞了"有用得多。
3. 提供復現步驟。"先輸入使用者名稱，然後點選登入按鈕，就會出現這個錯誤"——復現步驟讓 AI 能模擬你的操作路徑，更容易定位問題。
4. 說清楚你已經嘗試了什麼。"我已經檢查了網路請求，返回 200，資料正常"——這能幫 AI 排除已驗證的方向，不浪費時間重複排查。

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
差的除錯描述

{class="font-mono text-xs leading-relaxed"}
按鈕點選沒反應，幫我看看
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
好的除錯描述

{class="font-mono text-xs leading-relaxed"}
點選登入按鈕後頁面無反應。 期望行為：點選後跳轉到 /home 頁面 實際行為：點選後無任何反應，控制檯無報錯 復現步驟： 1. 在登入頁輸入使用者名稱admin和密碼123456 2. 點選"登入"按鈕 3. 頁面無反應 已排查： - 網路請求正常，返回200 - onClick事件已繫結 - 檢查了LoginButton元件的程式碼 相關檔案：@src/components/LoginButton.tsx @src/pages/Login.tsx
:::
:::

#### 三、迭代策略：小步快跑 vs 大步重構

AI 程式設計中的迭代有兩種基本策略，適用於不同場景。理解它們的區別，能幫你在不同情況下做出正確選擇。

"小步快跑"策略適用於功能開發和 bug 修復。它的核心是：每次讓 AI 只做一個小的修改，驗證透過後再做下一個。優勢是每一步都可驗證、可回退，風險可控；劣勢是速度較慢，需要頻繁的對話互動。適合：新功能開發、不確定最優方案時的探索、對 AI 產出不太放心時的謹慎迭代。

"大步重構"策略適用於明確知道目標的大規模修改。它的核心是：一次性描述完整的目標，讓 AI 自主規劃和執行整個修改。優勢是速度快，AI 能看到全域性圖景做出更優的架構決策；劣勢是風險高，如果 AI 理解偏差，修正成本大。適合：明確的架構升級、大規模程式碼遷移、有充分測試保障的重構。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">維度</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">小步快跑</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">大步重構</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每次修改量</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一個功能點或一個bug</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一個模組或一個架構層</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">驗證頻率</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每次修改後立即驗證</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全部修改完成後統一驗證</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">對話輪次</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多（5-10輪/功能）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">少（1-3輪/模組）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">風險</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">低，每步可回退</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">高，偏差修正成本大</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">適用場景</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新功能、探索性開發</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">明確目標的重構、遷移</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">前提條件</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">無特殊要求</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需要有測試覆蓋</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
兩種迭代策略的對比

實踐中，兩種策略常常組合使用。比如重構一個模組時，先用"大步重構"讓 AI 給出整體方案，審查方案後，再用"小步快跑"逐步執行。這樣既保證了全域性視角，又控制了執行風險。

#### 四、多輪對話的上下文管理

隨著對話輪次增加，你需要主動管理對話上下文，避免"AI 忘記了早期資訊"的問題。以下是幾個實用的上下文管理技巧。

第一，"錨定"關鍵資訊。在對話開始時，把關鍵約束寫清楚，並在後續對話中適時重申。比如"記住，我們的資料存在 localStorage，不能用資料庫"——在相關的修改請求中重申這個約束，防止 AI 遺忘。

第二，善用"總結-續接"技巧。當對話變得很長時，可以讓 AI"總結一下目前的進展和待辦事項"，然後開一個新對話，把這個總結作為起點。這樣既保留了關鍵上下文，又避免了長對話的退化。

第三，"一個對話一個任務"。這是最簡單也最有效的上下文管理策略。每個對話只處理一個任務或一個功能點，完成後開新對話處理下一個。這天然限制了對話長度，保持上下文清晰。

第四，利用工具的上下文管理功能。大多數 AI 程式設計工具都有"清除上下文"或"新會話"按鈕——當你感覺 AI 的回答品質下降時，不要猶豫，開一個新會話。丟失一些對話歷史比繼續在退化的上下文中掙扎要好得多。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：給你的 AI 當一次"病人"

{class="mt-1"}
故意在瀏覽器裡做一個小頁面，製造一個 bug（比如按鈕沒反應）。然後按本章"好的除錯描述"的格式，向 AI 完整描述一次：原始資訊、期望 vs 實際、復現步驟、已排查項。感受一下 AI 定位問題的速度差異——你會理解為什麼"描述問題"本身是門手藝。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- Prompt 三層：系統層（寫在記憶檔案）、任務層（做什麼+技術+約束）、反饋層（指出問題+期望+上下文）
- 除錯四要點：給原始資訊、期望vs實際、復現步驟、已排查項
- 小步快跑：低風險高輪次，適合新功能；大步重構：高風險低輪次，需要測試保障
- 上下文管理四招：錨定關鍵資訊、總結-續接、一個對話一個任務、果斷開新會話
:::
