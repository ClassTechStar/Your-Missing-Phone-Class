---
id: di-san-shi-ba-zhang
num: 38
part: ai-biancheng-pian
nav: 第三十八章：AI程式設計五大思維原則
toc: default
kind: chapter
---

### 第三十八章：AI程式設計五大思維原則

{class="chapter-intro mb-4"}
如果這本書只能讓你記住一章，那必須是這一章。五大思維原則是全書的心臟，後面所有章節——上下文、需求、對話、品質——都是這五條原則在不同場景下的展開。放心，每一條都不難懂，但每一條都值得你用幾個專案去"長進肌肉裡"。

故事的起點很有意思：Andrej Karpathy 在開源他的專案時，附了一份僅 70 行的 CLAUDE.md 檔案，總結了與 AI 協作的四條核心原則。這份檔案在 GitHub 上獲得了超過 70,000 個 Star，成為全球 AI 程式設計實踐者最廣泛引用的準則。這四條原則不是空洞的口號，而是從大量實踐中提煉出的、可操作的思維習慣。本書在其基礎上補充了第五條——迭代驗證——構成完整的五大原則體系。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
70 行檔案為什麼這麼值錢？

{class="mt-1"}
70,000 個 Star 是什麼概念？GitHub 上絕大多數專案一輩子都到不了這個數字。一個 70 行的文字檔案能獲得它，恰恰證明瞭一件事：AI 時代最稀缺的不是程式碼，而是"想清楚"的能力。這 70 行，就是"想清楚"的濃縮版。
:::

#### 一、原則一：Think Before Coding（先思考，再編碼）

這是五條原則中最反直覺的一條。既然 AI 能幫我們寫程式碼，為什麼還要"先思考"？答案很簡單：AI 的產出品質與你的輸入品質正相關。你自己都沒想清楚要做什麼，AI 給出的答案只會讓你陷入無休止的"改了又改"迴圈——俗稱"AI 陪你一起迷路"。

"先思考"意味著在給 AI 下達指令之前，你需要回答三個問題，它們構成一個缺一不可的"思考三角"：

1. 我要解決什麼問題？（目標）
2. 我期望的結果長什麼樣？（驗收標準）
3. 有哪些約束條件需要遵守？（邊界）

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">思考維度</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">模糊輸入（差）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">清晰輸入（好）</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">問題定義</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">幫我做個網站</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">幫我做一個個人工具站，展示 3 個 AI 小工具的入口卡片</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">期望結果</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">好看一點</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">響應式佈局，暗色主題，卡片有懸停動畫，移動端可用</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">約束條件</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">（未說明）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不使用框架，純 HTML+CSS+JS，單檔案部署，不需要後端</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
同一需求的模糊輸入與清晰輸入對比

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：先思考 ≠ 先寫完美檔案

{class="mt-1"}
"先思考"不等於"寫一份完美的 PRD 再開始"。它是一個快速但有條理的思考過程——花 30 秒想清楚上面三個問題，遠比花 30 分鐘在對話中反覆修改來得高效。小任務三問可以很短；大專案可以把它們擴充套件成完整的需求檔案（詳見第四十章）。
:::

#### 二、原則二：Simplicity First（簡單至上）

AI 程式設計最大的陷阱不是"做不出來"，而是"做得太多"。當你對 AI 說"做一個使用者管理系統"，它可能會生成認證、權限、角色、審計日誌、資料匯出等一整套功能——但你現在可能只需要一個簡單的登入頁面。過度生成，是 AI 程式碼膨脹的主要原因。

"簡單至上"要求你在每次下達指令時都遵循"最小可行"原則：用最少的程式碼實現核心功能，用最簡單的方案解決問題，用最少的功能驗證想法。Karpathy 對此有個精闢的比喻："如果你要計算一個折扣價格，你不需要一個電商引擎。"

在實踐中，"簡單至上"意味著幾個具體的操作習慣：

- 每次只讓 AI 實現一個功能點，而不是一口氣描述整個系統；
- 優先選擇標準庫和簡單方案，而不是引入複雜的相依性；
- 能用 50 行程式碼解決的問題，不要讓 AI 寫 500 行；
- 當 AI 的產出超出預期範圍時，勇敢地告訴它"砍掉多餘的部分"。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">場景</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">過度方案（避免）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">簡單方案（推薦）</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需要儲存資料</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">搭建 MySQL 資料庫 + ORM</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">先用 JSON 檔案或 SQLite</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需要使用者登入</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OAuth2.0 + JWT + 角色權限</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">先做簡單的密碼驗證</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需要前端框架</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">React + Redux + Router</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">先試純 HTML + 原生 JS</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需要部署上線</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Docker + CI/CD + K8s</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">先在本地跑通再說</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
常見場景的過度方案與簡單方案對比

#### 三、原則三：Surgical Changes（精準修改）

當你在迭代一個已有專案時，每次修改都應該像外科手術一樣精準——只動該動的地方，不碰不該碰的。這一點在 AI 程式設計中尤其重要，因為 AI 有"順手改一下"的傾向：你讓它修一個 bug，它可能順便重構了半個檔案。

"精準修改"的核心要求是：每次給 AI 的指令，都明確指定修改的範圍和邊界。告訴它"只修改 calculate_discount 函式""不要動其他部分""保持現有的程式碼風格"。當 AI 的修改超出了你要求的範圍時，立即要求它回退多餘的部分。

Karpathy 用一個 diff（差異對比）的例子說明瞭這一點。假設你讓 AI 給購物車的折扣計算函式新增"會員價"邏輯：好的產出是隻修改這一個函式、增加幾行程式碼；壞的產出是把整個檔案重構了一遍——雖然新程式碼可能更"優雅"，但你無法確定它有沒有引入新 bug。在 AI 程式設計中，"看起來更好"永遠不能成為偏離指令的理由。

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
差的指令（範圍模糊）

{class="font-mono text-xs leading-relaxed"}
幫我最佳化這個專案的 折扣計算邏輯
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
好的指令（精準指定範圍）

{class="font-mono text-xs leading-relaxed"}
只修改 cart.py 中的 calculate_discount 函式： 1. 在現有折扣基礎上增加會員價邏輯 2. 會員使用者額外享受 10% 折扣 3. 不要修改函式簽名和其他函式 4. 保持現有的變數命名風格
:::
:::

#### 四、原則四：Goal-Driven Execution（目標驅動執行）

這條原則回答了一個關鍵問題：你應該給 AI 下達"怎麼做"的指令，還是"做什麼"的指令？Karpathy 的答案是後者。與其告訴 AI"先建立一個類，然後新增方法，然後寫測試"，不如告訴它"我需要一個能解析 CSV 檔案並統計每列唯一值數量的工具"。讓 AI 自己決定實現路徑，你負責驗收結果。

"目標驅動"的好處是雙重的。對 AI 來說，它獲得了更大的自主空間，可以選擇最優的實現路徑，而不是被你的中間步驟束縛；對你來說，你把注意力從"怎麼做"轉移到了"做出來對不對"——這正是指揮官該做的事。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：目標驅動 ≠ 放任不管

{class="mt-1"}
它需要你在 AI 執行後進行嚴格的驗收：結果是否滿足需求？邊界情況是否處理了？是否有明顯的過度設計？如果結果不符合預期，提供具體的反饋——不是"重寫"，而是"這裡的問題在於空列表輸入會報 IndexError，請修改為新增空值檢查"。
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">指令風格</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">示例</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">結果特點</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">命令式（怎麼做）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"先建立一個 Python 類，叫 DataParser，加一個 parse 方法，接收 filename 引數，用 csv 模組讀取…"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI 變成打字員，你的中間步驟可能不是最優路徑</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">目標式（做什麼）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"我需要一個工具：讀取 CSV 檔案，統計每列的唯一值數量，輸出為 JSON 格式。請給出完整實現。"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI 自主選擇最優路徑，你負責驗收結果</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
命令式指令與目標式指令的對比

#### 五、原則五：Iterate and Verify（迭代驗證）

這是本書在 Karpathy 四原則基礎上補充的第五條。它的核心信念是：AI 的第一次產出幾乎永遠不是最終版本。有效的 AI 程式設計是一個"生成-驗證-修正"的迭代迴圈，而不是一次性的"指令-產出"。

"迭代驗證"不是被動的"不對就再試"，而是一個有結構的驗證流程。每次 AI 給出產出後，按三個層次進行驗證：

- 第一層·功能驗證：它能不能跑？輸入輸出對不對？
- 第二層·邊界驗證：空輸入、超長輸入、異常輸入會怎樣？
- 第三層·架構驗證：程式碼結構是否合理？有沒有硬編碼？是否便於後續擴充套件？

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-bullseye mr-1"></i> 定義目標</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> AI 生成程式碼</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> 功能驗證</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> 透過</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> 邊界驗證</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> 透過</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-landmark mr-1"></i> 架構審查</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> 透過，進入下一步</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> 不透過</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> 提供具體反饋</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> 重新生成</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 2：AI 程式設計的迭代驗證迴圈
:::

這個迴圈的關鍵在於"提供具體反饋"這一步。當驗證不透過時，不要說"不對，重做"，而要說"函式在輸入空列表時報 IndexError，請在第 15 行新增空值檢查"。具體的反饋讓 AI 能精準修正；模糊的反饋只會讓它重新猜測你的意圖。

#### 六、Harness Engineering：Agent = Model + Harness

2026 年中期，一個叫 Harness Engineering 的概念開始在 AI 程式設計社群流行。它的核心公式很簡單：

:::inline div .quote-line .text-center .text-base .font-bold
<strong>Agent 的能力 = 模型能力 × Harness 質量</strong>
:::

模型能力是 AI 大腦的智力上限；Harness 是圍繞模型搭建的"工作環境"——包括上下文管理、工具整合、流程編排、記憶系統等。

這個概念解釋了一個常見的困惑：為什麼同樣用 GPT-4 或 Claude，有的人能做出驚豔的專案，有的人只能得到平庸的程式碼？區別不在模型，而在 Harness。一個好的 Harness 包括：清晰的專案規範檔案、合理的工具整合、有條理的對話上下文、完善的驗證流程。模型決定了智力上限，Harness 決定了你能多大程度地發揮這個上限。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
天才實習生比喻

{class="mt-1"}
你可以把模型想象成一個天才實習生——智商很高，但如果不給他專案背景檔案、不告訴他用哪些工具、不給他設定期限和驗收標準，他也做不出好東西。Harness Engineering 就是"如何給天才實習生搭好工作環境"的工程。
:::

本書的後續章節，本質上都在教你如何構建一個好的 Harness：第三十九章教你管理上下文（專案記憶系統），第四十章教你定義需求（PRD），第四十三章教你對話技術（Prompt 分層），第四十五章教你品質保障（驗證流程）。這些組合起來，就是你的 Harness。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：用"思考三角"拆解你的下一個想法

{class="mt-1"}
挑一個你一直想做但沒動手的小東西（比如一個倒數日網頁、一個喝水提醒指令碼）。花 3 分鐘回答：① 它解決什麼問題？② 做出來長什麼樣？③ 有什麼約束（時間、技術、環境）？然後把答案寫成一段話。恭喜你，你已經完成了人生第一次"Think Before Coding"——這段話就是一條合格的高品質指令。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 五大原則源自 Karpathy 70 行的 CLAUDE.md（70K+ Star），本書補充第五條"迭代驗證"
- Think Before Coding：開口前回答三問——做什麼？結果長啥樣？有什麼約束？
- Simplicity First：AI 最大的坑是"做得太多"——算折扣不需要電商引擎
- Surgical Changes：像外科手術一樣精準修改，拒絕 AI 的"順手改一下"
- Goal-Driven Execution：說"做什麼"，不說"怎麼做"，讓 AI 自主選路徑
- Iterate and Verify：三層驗證（功能/邊界/架構）+ 具體反饋，迴圈迭代
- Harness Engineering：能力 = 模型 × Harness，把 AI 當"天才實習生"來管理環境
:::
