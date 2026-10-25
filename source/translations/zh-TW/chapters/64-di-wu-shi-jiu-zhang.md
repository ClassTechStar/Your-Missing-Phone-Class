---
id: di-wu-shi-jiu-zhang
num: 59
part: ios-kai-fa-pian
nav: 第五十九章：認識iOS——蘋果生態與開發生態
toc: default
kind: chapter
---

### 第五十九章：認識 iOS——蘋果生態與開發生態

{class="chapter-intro mb-4"}
恭喜你做出這個決定——從"用 iPhone 的人"變成"給 iPhone 寫應用的人"。在動手之前，咱們先把地圖攤開：iOS 從哪裡來？蘋果的"圍牆花園"對開發者意味著什麼？一個 App 從你的手指敲鍵盤到使用者手機上，中間都發生了什麼？

#### 一、iOS 的身世：一部手機改變一個行業

2007 年 1 月，喬布斯在發佈會上掏出了第一代 iPhone。當時它連第三方應用都不支援——直到 2008 年，蘋果推出 App Store 和 iPhone SDK，允許全世界開發者給 iPhone 寫軟體。那一刻，"應用經濟"誕生了：到今天，App Store 上有數百萬個應用，為開發者累計分成超過數千億美元。

系統本身也在進化：最初叫 iPhone OS，2010 年更名 iOS；版本號一路走到 iOS 17（2023），然後在 2025 年，蘋果把命名改為跟隨年份——iOS 26 於 2025 年發佈，2026 年 8 月的當前版本是 iOS 27。命名會變，但一件事沒變過：iOS 的使用者付費習慣和軟體品質口碑，是移動生態裡公認最好的——同樣的 App，iOS 端的收入往往顯著高於安卓端。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">節點</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">年份</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">對開發者重要的事</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">App Store 上線</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2008</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第三方開發生態開啟</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift 發佈</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2014</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">現代 iOS 開發語言登場</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI 發佈</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2019</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">宣告式介面框架，本書主線</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">iOS 26（改名元年）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2025</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">命名跟隨年份；Apple Intelligence 全面整合</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">iOS 27</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2026</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">當前最新版（本書基準）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
iOS 開發大事記（截至 2026 年 8 月）

#### 二、圍牆花園：蘋果生態的"規矩"與"紅利"

蘋果生態常被形容為 "圍牆花園"（Walled Garden）——規則多、管得嚴：App 必須稽核才能上架、開發必須用 Mac 和 Xcode、分發主要走 App Store。聽起來憋屈？但對開發者，這套規矩換來了真金白銀的紅利：

- 裝置碎片化極小：iPhone 型號就那麼幾款，螢幕尺寸、系統版本高度統一——你適配 5 臺機型，就覆蓋了 95% 的使用者（安卓可能要適配幾十款）；
- 系統版本更新率極高：新系統發佈幾周內就有七八成使用者升級，新 API 可以大膽用，不用照顧"五年前的老系統"；
- 使用者付費習慣好：App Store 使用者更願意為應用和內購花錢；
- 稽核雖然嚴格，但商店乾淨：山寨、流氓軟體少，好產品更容易被看見。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：先說清楚成本

{class="mt-1"}
iOS 開發有硬門檻：必須有一臺 Mac（Xcode 是 macOS 獨佔），上架需要 99 美元/年的開發者帳號（個人開發者免費帳號可以本地真機除錯，但不能上架）。想清楚這筆投入再啟程——不過好訊息是，學習階段用免費帳號完全夠用，第 60 章會講。
:::

#### 三、用什麼語言寫：Objective-C 還是 Swift？

iOS 開發歷史上也有兩位"主角"。Objective-C 是開國元老——從 2008 年用到 2014 年；Swift 是蘋果 2014 年發佈的新語言，此後一路進化到 Swift 6（2024 年發佈，引入嚴格併發檢查），到 2026 年，新專案幾乎全部用 Swift。

給零基礎的你一句實在話：直接學 Swift，Objective-C 連看都不用看——除非你入職後要維護十年前的遺產程式碼。Swift 的好處：語法清爽（沒有 C 語言時代的分號與標頭檔案包袱）、可選值（Optional）機制從語言層面消滅"空指標崩潰"、和 SwiftUI 無縫配合、還有 iPad 上的 Swift Playgrounds 可以邊玩邊學。

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Objective-C 風格（上古遺蹟）

{class="font-mono text-xs leading-relaxed"}
NSString *name = @"張三"; [name stringByAppendingString:@"你好"]; // 方括號 + 指標 + 分號三件套
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Swift 風格（現代清爽）

{class="font-mono text-xs leading-relaxed"}
var name = "張三" name += "你好" // 像自然語言一樣直白
:::
:::

#### 四、一個 App 是怎麼誕生的？

和所有平臺一樣，iOS App 的誕生也有一條流水線。但蘋果版多了兩道"安檢"：

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-lightbulb mr-1"></i> 想法</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center">📐 設計（介面+功能）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-keyboard mr-1"></i> 寫程式碼（Swift + SwiftUI）</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hammer mr-1"></i> 編譯簽名</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> 測試（模擬器+真機）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-stamp mr-1"></i> 蘋果稽核</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> 上架 App Store</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 1：一個 iOS App 從想法到上架的全流程（注意多出的"稽核"環節）
:::

流程裡的關鍵概念：

- 簽名（Signing）：每個 iOS App 都必須"簽名"才能安裝——證明"這個包出自你，沒被篡改"。學習階段 Xcode 用你的 Apple ID 自動簽名；上架時用開發者證書。第 67 章細講。
- 模擬器（Simulator）：Mac 上虛擬出的 iPhone，開發除錯的主戰場。它跑的是 Mac 的 CPU，所以特別流暢，比安卓模擬器體驗好一大截。
- TestFlight：蘋果官方的"內測分發"工具——上架前把測試版發給最多 10000 名測試使用者，他們用 TestFlight 應用安裝試用。這是 iOS 生態獨有的優雅。

#### 五、iOS 技術棧全景：你的"武器清單"

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">層次</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">主流選擇（2026）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">幹什麼用的</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">語言</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift 6</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">寫邏輯的語言</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">介面</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI + 蘋果設計規範（HIG）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用程式碼畫介面（本書主線）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">架構</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MVVM + @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把介面和邏輯分開</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">資料儲存</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData（資料庫）+ UserDefaults（配置）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把資料存進手機</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">網路</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession + async/await + Codable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">和伺服器對話</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">構建工具</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode Build System / xcodebuild</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把程式碼變成安裝包</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">開發環境</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode（macOS 獨佔）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">蘋果官方 IDE</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
2026 年 iOS 主流技術棧速覽

注意到沒：這套清單比安卓的短一截——因為蘋果把很多事都"包辦"了。封閉生態的代價是自由度，回報是省心：不用糾結選哪個網路庫、哪個資料庫，官方給的往往就是最優解。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：看看你手機的"蘋果戶口"

{class="mt-1"}
開啟 iPhone 的 [設定] → [通用] → [關於本機]，記下三樣：iOS 版本、機型名稱、可用容量。再去 App Store 的"今天"頁隨便逛逛，注意那些精品 App 的截圖和文案——從今天起，你逛商店的視角要從"使用者"切換到"開發者"了。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 2008 年 App Store 上線，"應用經濟"誕生；2026 年當前版本 iOS 27
- 圍牆花園的賬：規矩多，但裝置少、版本新、使用者肯花錢、商店乾淨
- 硬門檻：必須有 Mac；上架要 99 美元/年開發者帳號；學習階段免費帳號夠用
- 語言直接學 Swift；Objective-C 只屬於遺產程式碼
- 流水線比安卓多一環：蘋果稽核；TestFlight 是內測分發神器
- 2026 標準技術棧：Swift 6 + SwiftUI + MVVM + SwiftData + URLSession + Xcode
:::
