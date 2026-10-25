---
id: di-si-shi-wu-zhang
num: 45
part: ai-biancheng-pian
nav: 第四十五章：品質保障——讓AI程式碼可靠
toc: default
kind: chapter
---

### 第四十五章：品質保障——讓AI寫的程式碼可靠

{class="chapter-intro mb-4"}
AI 寫的程式碼有一個特點：它通常"看起來很對"——變數命名規範、註釋齊全、邏輯清晰。但"看起來對"不等於"真的對"。AI 程式碼中隱藏的問題往往比手寫程式碼更難發現，因為它的表面品質太高了，容易讓人放鬆警惕。本章教你如何為 AI 程式碼建立有效的品質保障體系——用測試、審查、版本控制三道防線，把"看起來對"變成"真的對"。

#### 一、測試驅動：讓 AI 寫測試

測試是 AI 程式設計品質保障的第一道防線。好訊息是：讓 AI 寫測試比讓它寫功能程式碼更容易、更可靠——因為測試的預期行為是明確的，不太容易產生"看起來對但實際不對"的程式碼。

測試驅動的 AI 程式設計流程是：先讓 AI 寫功能程式碼，驗證基本功能透過後，立即讓它寫測試用例。測試用例應覆蓋正常路徑、邊界情況和異常情況。然後再讓 AI 根據測試反饋修正功能程式碼。這個流程的好處是：測試一旦寫好，就是持續的驗證工具——後續任何修改都可以透過執行測試來確認沒有引入迴歸問題。

::: div .code-block
:::inline div .code-head
<span>給 AI 的指令：寫測試</span><span class="dots">···</span>
:::

```
請為 calculate_discount 函式編寫單元測試。
測試用例應覆蓋：
1. 正常路徑：
   - 100元商品打8折 -> 80
   - 200元商品打5折 -> 100
2. 邊界情況：
   - 0元商品打8折 -> 0
   - 100元商品打0折 -> 100（不打折）
   - 100元商品打10折 -> 100（全價）
3. 異常情況：
   - 負數價格 -> 應丟擲錯誤
   - 折扣率 > 1 -> 應丟擲錯誤
   - 非數字輸入 -> 應丟擲錯誤
使用Vitest框架，給出完整測試檔案。
```
:::

注意這個指令的特點：它明確列出了三類測試用例（正常、邊界、異常），不給 AI 自由發揮的空間去"選擇性測試"。AI 有時候會只寫正常路徑的測試來"快速交差"，明確列出所有類別可以避免這個問題。

#### 二、程式碼審查技巧

即使有測試覆蓋，你仍然需要對 AI 產出的程式碼進行人工審查。程式碼審查不是逐行閱讀——那太耗時也太依賴你的程式設計水準。有效的 AI 程式碼審查應該關注以下幾個關鍵維度：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">審查維度</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">關注什麼</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">常見問題</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">安全性</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">輸入驗證、金鑰處理、SQL隱碼攻擊防護</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI經常忘記驗證輸入，金鑰硬編碼在程式碼中</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">錯誤處理</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">異常是否被捕獲，錯誤資訊是否合理</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI喜歡用空catch塊或只console.log</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">效能</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">是否有明顯的效能問題，如N+1查詢、無限迴圈</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI有時會寫出O(n²)的演演算法</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可維護性</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">程式碼結構是否清晰，命名是否有意義</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI偶爾會生成過度抽象的程式碼</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">相依性管理</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">引入的依賴是否必要，版本是否明確</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI傾向於引入不必要的函式庫</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
AI 程式碼審查的關鍵維度

審查時不必自己逐一檢查——可以讓 AI 幫你做第一輪審查。指令如："請審查這段程式碼的安全性、錯誤處理和效能，指出潛在問題。"AI 的自我審查能力在不斷提升，雖然不能完全替代人工審查，但能幫你過濾掉大部分明顯問題。

#### 三、版本控制：Git 在 AI 程式設計中的角色

Git 在 AI 程式設計中的角色比在傳統程式設計中更加重要。因為 AI 的每次修改都可能引入不可預知的變化，你需要一個可靠的"後悔藥"——版本控制就是那個後悔藥。

AI 程式設計中 Git 的最佳實踐是"頻繁提交、小步快進"。每完成一個可驗證的功能點，就提交一次。這樣當 AI 的某次修改出了問題時，你可以精準回退到上一個可用狀態，而不需要推翻所有工作。

另一個實用技巧是"分支隔離"。對於不確定結果的 AI 修改（比如大步重構），先建立一個新分支來做。如果結果滿意，合併回主分支；如果不滿意，直接刪除分支，不影響主分支。這比在主分支上反覆修改安全得多。

1. 每次 AI 修改前，確保工作區是乾淨的（沒有未提交的更改）。這樣如果 AI 的修改不滿意，可以用 git checkout . 快速回退。
2. 每次 AI 修改後、驗證透過後，立即提交。提交資訊描述這次修改做了什麼，比如"feat: 新增使用者註冊功能"。
3. 對於大步重構，先建立分支：git checkout -b refactor/auth-system。在分支上完成修改，測試透過後再合併。
4. 養成檢視 diff 的習慣。每次 AI 修改後，用 git diff 檢視具體改了什麼。這不僅能幫你發現問題，還能幫你學習程式碼。

#### 四、常見陷阱與避坑指南

AI 程式設計中有幾個反覆出現的陷阱，幾乎所有初學者都會踩。提前知道它們，能幫你少走很多彎路。

##### 1. 陷阱一：信任陷阱

"AI 寫的程式碼看起來很專業，一定沒問題吧？"——這是最危險的陷阱。AI 生成的程式碼在表面上非常整潔——命名規範、註釋齊全、結構清晰——這種"表面專業感"會讓人放鬆警惕。但表面整潔不代表邏輯正確。解藥：永遠透過測試驗證，而非透過"看起來對不對"判斷。

##### 2. 陷阱二：膨脹陷阱

"既然 AI 能幫我寫程式碼，那不如把功能做得全面一點？"——這會導致程式碼膨脹。AI 很擅長"多給"：你讓它做一個登入頁面，它會給你一套完整的使用者管理系統。多餘的功能不僅增加複雜度，還增加了出 bug 的機率。解藥：嚴格遵循 Simplicity First 原則，明確告訴 AI"只做這個功能，不要額外新增"。

##### 3. 陷阱三：理解陷阱

"AI 應該理解我的意思吧？"——不一定。AI 的理解能力雖然很強，但對模糊的需求仍然會"猜"。當它猜錯了，產出的程式碼就是錯的。更麻煩的是，它猜錯的程式碼通常"看起來很合理"，讓你誤以為它理解了。解藥：在指令中提供足夠的具體細節，減少 AI 需要"猜"的空間。

##### 4. 陷阱四：上下文陷阱

"我在之前的對話裡說過了，AI 應該還記得吧？"——很可能不記得。隨著對話變長或開新會話，AI 會丟失早期上下文。如果某個關鍵約束沒有被寫入專案記憶檔案，它很可能在後續修改中被忽略。解藥：關鍵約束寫入專案記憶檔案，不要依賴對話記憶。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
四大陷阱速記

{class="mt-1"}
信任陷阱——別信"看起來對"；膨脹陷阱——AI 愛"多給"；理解陷阱——模糊需求它會"猜"；上下文陷阱——對話記憶會"忘"。對應的解藥分別是：測試驗證、砍掉多餘、給足細節、寫入記憶檔案。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：給你的專案建三道防線

{class="mt-1"}
如果你已經開始做專案一（工具站）：① 讓 AI 給核心函式寫 3 類測試用例；② 按五個維度審查一遍程式碼（安全性/錯誤處理/效能/可維護性/依賴）；③ 用 git 初始化專案，做第一次提交。三道防線齊了，你的專案才真正屬於你。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- AI 程式碼"看起來對"≠"真的對"——表面品質太高反而容易放鬆警惕
- 讓 AI 寫測試：明確列出正常/邊界/異常三類用例，防止"選擇性測試"
- 審查五維度：安全性、錯誤處理、效能、可維護性、相依性管理
- Git 是"後悔藥"：頻繁提交、小步快進、分支隔離、常看 diff
- 四大陷阱：信任（測試驗證）、膨脹（砍掉多餘）、理解（給足細節）、上下文（寫入記憶檔案）
:::
