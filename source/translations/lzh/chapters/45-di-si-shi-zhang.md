---
id: di-si-shi-zhang
num: 40
part: ai-biancheng-pian
nav: 第四十章：需求工程——化想法為AI指令
toc: default
kind: chapter
---

### 第四十章：需求之工——化念為 AI 可行之令

{class="chapter-intro mb-4"}
若上下文之工所解者「使 AI 知其背景」，則需求之工所解者「使 AI 知此次所作何事」。此 AI 編程至顯人我之差之節也——同器同模，有者能作令人驚豔之項目，有者徒得平庸之玩。其異往往不於技之能，而於述需之能。

#### 一、自晦之念至結構化之需求

每項目皆始於一晦之念——「吾欲作一記帳之 App」「吾欲作一個人網站」「吾欲作一待辦清單之器」。此念自無過，然爾徑擲與 AI，則產之質，全繫乎運。需求之工之之，即化此晦之念為 AI 能精行之結構化之需求也。

可喜者：結構化之需求，毋須爾作數十頁之 PRD。惟須爾答五問，吾儕謂之「需求五要」：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">其要</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">其問</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">其例：記帳 App</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">誰用之？</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自用之，記日用之收支</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">作何事？</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一能記每筆之收支、按月而總、可視之應用</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">何為而作？</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">欲知己消費之構，得其不必之支出</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">大致何以為？</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">前端用 React，數據存瀏覽器之本地，姑不作後端與登入</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">有何限制？</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一人為之，2 週而畢，毋須上線部署</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
需求五要與其例

此五要毋須作正式之文，即於腦中疾過一遍亦足矣。要於養「先思審而後言」之習。爾將見，能明答此五問，則爾述需自結構化矣。

#### 二、需求拆解分層之藝

項目之大者，一述需不足也。須拆大需為小而可獨驗之子需。此程謂之「需求之拆解」，其核之則：每子需求皆當能獨成、獨驗、獨付。

以「作一個人記帳 App」為例，合理之拆解如次：

1. 成基礎收支記錄之功（能增、觀、刪其錄）；
2. 增分類之功（予每筆之錄以飲食、交通等籤）；
3. 增月度彙總之功能（按月統計收支之況）；
4. 增資料可視化（以圖表展示消費結構）。

凡每一步，皆獨立可運行可驗證之功能增量也。

:::inline div .quote-line
需求拆解之金律：每步既畢，項目皆當為"可用之物"——縱功能至陋。慎勿使項目滯於"事事半而無一可用"之境。
:::

此拆解之法有二利。其一，使君恆能見進展——每成一步，君之 App 即多一功能，此正回饋於長期專案至要（人皆需成就感也）。其二，使 AI 每次任務皆足夠小，以降「AI 理解偏差」之風險——任務愈小，AI 理解愈準確，產出之質愈高。

#### 三、PRD 撰寫模板與實踐

較大之專案（如一有前後端、多功能模組之全棧應用），僅憑需求五要素或不足。此時君須撰一份更正式之專案需求文檔（PRD）。一易誤解之點：PRD 非寫予 AI 觀——乃寫予君自己，助君理清思路，而後君方能予 AI 更精確之指令。

一份善 PRD 不必甚長，然當含六部：專案概述（一段話說清所為）、功能列表（每功能點為何）、技術方案（用何技術棧、大致架構）、資料模型（核心資料結構）、界面描述（主要頁面之貌）、開發計畫（分幾步而成）。

::: div .code-block
:::inline div .code-head
<span>PRD.md</span><span class="dots">···</span>
:::

```
# 個人記賬應用 PRD
## 項目概述
一輕量個人記賬之應用，備收支記錄、分類、月度匯總與數據可視化。
## 功能列表
1. 記錄收支：金額、類型(收入/支出)、分類、備註、日期
2. 分類管理：預設餐飲、交通、購物、娛樂、其他
3. 月度彙總：按月計總收入、總支出、結餘
4. 消費可視化：餅圖展示各分類佔比
5. 數據導出：導出爲CSV
## 技術方案
- 前端：React + TypeScript + Tailwind CSS
- 數據存儲：localStorage（無需後端）
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
Step 3: 月度彙總
Step 4: 數據可視化
Step 5: 數據導出
```
:::

注意此 PRD 之撰寫風格：用簡潔之列表與結構化格式，而非長篇大論。每功能點皆有明確定義，資料模型以簡單型別描述。此風格之 PRD 不惟君自覽清楚，君予之於 AI 時，AI 亦能精確理解每需求之點。

#### 四、實戰：從想法到方案之完整推演

徒紙上談兵無味，吾儕以一完整之例遍走需求工程之全程。設君之念曰：「吾欲作一學習追蹤器，能追吾每日所學者何」。

第一步，遍核需求五要素。

- Who：個人使用。
- What：一器也，能記每日學習之內容、追學習之時長、顧學習之進度。
- Why：欲養持續學習之習，見己之所積。
- How：先作網頁版，資料存於瀏覽器本地。
- Constraint：零基礎開發，期一週內完成核心功能。

次步者，析其所求也。

1. Step 1：實現「記錄學習條目」之功能（日期、內容、時長）；
2. Step 2：增「學習時長統計」（今日、本週累計）；
3. Step 3：實現「學習日曆」視圖（如 GitHub 貢獻圖之展示）；
4. Step 4：增「學習回顧」之功能（隨機展示往日某天之學習記錄，以助複習）。

第三步，撰一份簡短 PRD。不必長——上之拆解本身即構成 PRD 之主體。整理之為 .md 之檔，置於專案根目錄，以為君與 AI 之共同參考。

第四步，始第一步之開發。予 AI 之指令可如為：

::: div .code-block
:::inline div .code-head
<span>予 AI 之指令</span><span class="dots">···</span>
:::

```
我須一個學習追蹤器之第一個功能——記錄學習條目。
用戶可添加一條學習記錄，包含日期、學習內容、學習時長（分鐘）。
數據存在localStorage。
前端用React + TypeScript。
請予出完整實現。
```
:::

注意此指令之特點：惟述當前此步之目標（記錄功能），不摻他功能；明技術約束（React、TypeScript、localStorage）；予足夠信息使 AI 知「何所為」與「何以致之」，而具體實現由 AI 自決。此即經需求工程加工之後高品質之 AI 編程指令也。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：為君之「心頭好」撰一份五要素卡

{class="mt-1"}
擇一君醞釀已久之小專案，費 5 分鐘填一卡：Who / What / Why / How / Constraint，各一句話。乃拆之為 3-5 個「每一步皆能用」之步驟。君將見：念既書之於紙，即自「白日夢」化為「待辦清單」。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 需求五要素：Who / What / Why / How / Constraint——思慮審明而後啟口
- 需求拆解黃金法則：每步既成，專案皆「能用之物」
- PRD 寫予自己：概述、功能列表、技術方案、資料模型、界面、計畫
- 善指令 = 惟述當前一步 + 明確約束 + 言「何所為」不言「何以致之」
- 完整推演模板：五要素 → 拆解 → PRD → 予指令，四步而行
:::
