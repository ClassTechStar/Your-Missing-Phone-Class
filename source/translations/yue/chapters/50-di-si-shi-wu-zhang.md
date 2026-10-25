---
id: di-si-shi-wu-zhang
num: 45
part: ai-biancheng-pian
nav: 第四十五章：質量保障——令AI代碼可靠
toc: default
kind: chapter
---

### 第四十五章：質素保障——令AI寫嘅代碼可靠

{class="chapter-intro mb-4"}
AI 寫嘅代碼有一個特點：佢通常「睇落好啱」——變數命名規範、註解齊全、邏輯清晰。但「睇落啱」唔等於「真係啱」。AI 代碼入面隱藏嘅問題往往比手寫代碼更難發現，因為佢嘅表面質素太高，容易令人放鬆戒備。本章教你點樣為 AI 代碼建立有效嘅質素保障體系——用測試、審查、版本控制三道防線，將「睇落啱」變成「真係啱」。

#### 一、測試驅動：叫 AI 寫測試

測試係 AI 編程質素保障嘅第一道防線。好消息係：叫 AI 寫測試比叫佢寫功能代碼更容易、更可靠——因為測試嘅預期行為係明確嘅，冇咁容易產生「睇落啱但實際唔啱」嘅代碼。

測試驅動嘅 AI 編程流程係：先叫 AI 寫功能代碼，驗證基本功能通過之後，即刻叫佢寫測試用例。測試用例應該覆蓋正常路徑、邊界情況同異常情況。然後再叫 AI 根據測試回饋修正功能代碼。呢個流程嘅好處係：測試一寫好，就係持續嘅驗證工具——之後任何修改都可以透過行測試嚟確認冇引入回歸問題。

::: div .code-block
:::inline div .code-head
<span>畀 AI 嘅指令：寫測試</span><span class="dots">···</span>
:::

```
請爲 calculate_discount 函數編寫單元測試。
測試用例應覆蓋：
1. 正常路徑：
   - 100元商品打8折 -> 80
   - 200元商品打5折 -> 100
2. 邊界情況：
   - 0元商品打8折 -> 0
   - 100元商品打0折 -> 100（不打折）
   - 100元商品打10折 -> 100（全價）
3. 異常情況：
   - 負數價格 -> 應拋出錯誤
   - 折扣率 > 1 -> 應拋出錯誤
   - 非數字輸入 -> 應拋出錯誤
使用Vitest框架，畀出完整測試檔案。
```
:::

留意呢個指令嘅特點：佢明確列出咗三類測試用例（正常、邊界、異常），唔畀空間 AI 自由發揮去「選擇性測試」。AI 有時會齋寫正常路徑嘅測試嚟「快快手手交差」，明確列出所有類別就可以避免呢個問題。

#### 二、代碼審查技巧

就算有測試覆蓋，你仍然需要對 AI 產出嘅代碼做人工審查。代碼審查唔係逐行去讀——咁樣太嘥時間，亦都太依賴你嘅編程水平。有效嘅 AI 代碼審查應該留意以下幾個關鍵維度：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">審查維度</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">留意乜嘢</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">常見問題</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">安全性</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">輸入驗證、金鑰處理、SQL注入防護</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI 成日唔記得驗證輸入，金鑰寫死喺代碼入面</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">錯誤處理</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">異常有冇被捕獲，錯誤資訊合唔合理</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI 鍾意用空catch塊或者齋console.log</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">效能</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">有冇明顯嘅效能問題，例如N+1查詢、無限循環</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI 有時會寫出O(n²)嘅演算法</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可維護性</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">代碼結構清唔清晰，命名有冇意義</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI 間中會產生過度抽象嘅代碼</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">依賴管理</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">引入嘅依賴係咪必要，版本係咪明確</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI 傾向引入唔必要嘅函式庫</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
AI 代碼審查嘅關鍵維度

審查時唔使自己逐項檢查——可以叫 AI 幫你做第一輪審查。指令可以係：「請審查呢段代碼嘅安全性、錯誤處理同效能，指出潛喺問題。」AI 嘅自我審查能力不斷提升，雖然唔可以完全取代人工審查，但可以幫你過濾走大部分明顯問題。

#### 三、版本控制：Git 喺 AI 編程入面嘅角色

Git 喺 AI 編程入面嘅角色比喺傳統編程入面更加重要。因為 AI 每次修改都可能引入不可預知嘅變化，你需要一個可靠嘅「後悔藥」——版本控制就係嗰個後悔藥。

AI 編程入面 Git 嘅最佳實踐係「頻密提交、小步快進」。每完成一個可以驗證嘅功能點，就提交一次。咁樣當 AI 某次修改出咗問題，你可以精準回退去上一個可用狀態，唔使將所有工作推倒重嚟。

另一個實用技巧係「分支隔離」。對於唔肯定結果嘅 AI 修改（例如大步重構），先開一個新分支嚟做。如果結果滿意，合併返入主分支；如果唔滿意，直接刪咗個分支，唔會影響主分支。咁樣比喺主分支度反覆修改安全得多。

1. 每次 AI 修改之前，確保工作區係乾淨嘅（冇未提交嘅更改）。咁樣如果 AI 嘅修改唔滿意，可以用 git checkout . 快速回退。
2. 每次 AI 修改完、驗證通過之後，即刻提交。提交資訊描述今次修改做咗乜嘢，例如「feat: 添加用戶註冊功能」。
3. 對於大步重構，先開分支：git checkout -b refactor/auth-system。喺分支上面完成修改，測試通過之後先合併。
4. 養成睇 diff 嘅習慣。每次 AI 修改完，用 git diff 睇嚇具體改咗乜嘢。咁樣唔單止幫你發現問題，仲幫你學習代碼。

#### 四、常見陷阱同避坑指南

AI 編程入面有幾個重複出現嘅陷阱，幾乎所有初學者都會踩。早啲知道佢哋，可以幫你少行好多冤枉路。

##### 1. 陷阱一：信任陷阱

「AI 寫嘅代碼睇落好專業，一定冇問題啩？」——呢個係最危險嘅陷阱。AI 產生嘅代碼喺表面上非常企理——命名規範、註解齊全、結構清晰——呢種「表面專業感」會令人放鬆戒備。但表面企理唔代表邏輯正確。解藥：永遠透過測試嚟驗證，而唔係靠「睇落啱唔啱」嚟判斷。

##### 2. 陷阱二：膨脹陷阱

「既然 AI 幫到我寫代碼，不如將功能做得全面啲？」——咁樣會令代碼膨脹。AI 好擅長「多畀你」：你叫佢整一個登入頁面，佢會畀你一套完整嘅用戶管理系統。多餘嘅功能唔單止增加複雜度，仲增加咗出 bug 嘅機會率。解藥：嚴格跟 Simplicity First 原則，明確話畀 AI 知「淨係做呢個功能，唔好額外添加」。

##### 3. 陷阱三：理解陷阱

「AI 應該明我嘅意思啩？」——唔一定。AI 嘅理解能力雖然好強，但對住含糊嘅需求仍然會「估」。當佢估錯咗，產出嘅代碼就係錯嘅。更麻煩嘅係，佢估錯嘅代碼通常「睇落好合理」，令你誤會佢明咗。解藥：喺指令入面畀足具體細節，減少 AI 需要「估」嘅空間。

##### 4. 陷阱四：上下文陷阱

「我喺之前嘅對話講過㗎喇，AI 應該仲記得啩？」——好大機會唔記得。隨住對話變長或者開新會話，AI 會唔見咗早期上下文。如果某個關鍵約束冇寫入項目記憶檔案，佢好大機會喺之後嘅修改入面被忽略。解藥：關鍵約束寫入項目記憶檔案，唔好依賴對話記憶。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
四大陷阱速記

{class="mt-1"}
信任陷阱——唔好信「睇落啱」；膨脹陷阱——AI 愛「多畀你」；理解陷阱——含糊需求佢會「估」；上下文陷阱——對話記憶會「唔記得」。對應嘅解藥分別係：測試驗證、斬走多餘、畀足細節、寫入記憶檔案。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
嚟動手：為你嘅項目建三道防線

{class="mt-1"}
如果你已經開始做項目一（工具站）：① 叫 AI 為核心函數寫 3 類測試用例；② 跟五個維度審查一遍代碼（安全性/錯誤處理/效能/可維護性/依賴）；③ 用 git 初始化項目，做第一次提交。三道防線齊咗，你嘅項目先至真正屬於你。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- AI 代碼「睇落啱」≠「真係啱」——表面質素太高反而容易放鬆戒備
- 叫 AI 寫測試：明確列出正常/邊界/異常三類用例，防止「選擇性測試」
- 審查五維度：安全性、錯誤處理、效能、可維護性、依賴管理
- Git 係「後悔藥」：頻密提交、小步快進、分支隔離、成日睇 diff
- 四大陷阱：信任（測試驗證）、膨脹（斬走多餘）、理解（畀足細節）、上下文（寫入記憶檔案）
:::
