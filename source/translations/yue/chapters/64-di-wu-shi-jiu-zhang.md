---
id: di-wu-shi-jiu-zhang
num: 59
part: ios-kai-fa-pian
nav: 第五十九章：認識iOS——蘋果生態與開發生態
toc: default
kind: chapter
---

### 第五十九章：認識 iOS——蘋果生態同開發生態

{class="chapter-intro mb-4"}
恭喜你做出呢個決定——由「用 iPhone 嘅人」變成「畀 iPhone 寫應用嘅人」。動手之前，我哋先攤開張地圖：iOS 由邊度嚟？蘋果嘅「圍牆花園」對開發者嚟講即係乜嘢？一個 App 由你隻手敲鍵盤去到用戶部手機，中間發生咗乜嘢事？

#### 一、iOS 嘅身世：一部手機改變一個行業

2007 年 1 月，喬布斯喺發布會上面攞咗第一代 iPhone 出嚟。嗰陣佢連第三方應用都唔支援——直到 2008 年，蘋果推出 App Store 同 iPhone SDK，准許全世界開發者畀 iPhone 寫軟件。嗰一刻，「應用經濟」就誕生咗：到今日，App Store 上面有幾百萬個應用，為開發者累計分帳超過幾千億美元。

系統本身都喺度進化：最初叫 iPhone OS，2010 年改名 iOS；版本號一路行到 iOS 17（2023），跟住喺 2025 年，蘋果將命名改做跟年份——iOS 26 於 2025 年發布，2026 年 8 月嘅當前版本係 iOS 27。命名會變，但有一件事冇變過：iOS 嘅用戶付費習慣同軟件質素口碑，係移動生態入面公認最好嘅——同一個 App，iOS 端嘅收入往往明顯高過安卓端。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">節點</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">年份</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">對開發者重要嘅事</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">App Store 上線</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2008</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第三方開發生態開啟</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift 發布</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2014</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">現代 iOS 開發語言登場</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI 發布</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2019</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">聲明式界面框架，本書主線</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">iOS 26（改名元年）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2025</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">命名跟年份；Apple Intelligence 全面整合</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">iOS 27</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2026</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">當前最新版（本書基準）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
iOS 開發大事記（截至 2026 年 8 月）

#### 二、圍牆花園：蘋果生態嘅「規矩」同「紅利」

蘋果生態成日畀人形容做「圍牆花園」（Walled Garden）——規則多、管得嚴：App 必須審核先可以上架、開發必須用 Mac 同 Xcode、分發主要行 App Store。聽落好似好屈？但對開發者嚟講，呢套規矩換到嚟真金白銀嘅紅利：

- 設備碎片化極細：iPhone 型號就得嗰幾款，屏幕尺寸、系統版本高度統一——你適配 5 部機型，就已經覆蓋咗 95% 嘅用戶（安卓可能要適配幾十款）；
- 系統版本更新率極高：新系統發布幾個禮拜之內就有七八成用戶升級，新 API 可以大膽用，唔使遷就「五年前嘅老系統」；
- 用戶付費習慣好：App Store 用戶更願意為應用同內購畀錢；
- 審核雖然嚴格，但商店乾淨：山寨、流氓軟件少，好產品更容易畀人睇到。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：先講清楚成本

{class="mt-1"}
iOS 開發有硬門檻：必須有一部 Mac（Xcode 係 macOS 獨佔），上架需要 99 美元/年嘅開發者賬號（個人開發者免費賬號可以本地真機除錯，但唔可以上架）。諗清楚呢筆投入先啟程——不過好消息係，學習階段用免費賬號完全夠用，第 60 章會講。
:::

#### 三、用乜嘢語言寫：Objective-C 定係 Swift？

iOS 開發歷史上都有兩位「主角」。Objective-C 係開國元老——由 2008 年用到 2014 年；Swift 係蘋果 2014 年發布嘅新語言，之後一路進化到 Swift 6（2024 年發布，引入嚴格並發檢查），到 2026 年，新項目幾乎全部用 Swift。

畀零基礎嘅你一句實在話：直接學 Swift，Objective-C 連睇都唔使睇——除非你入職之後要維護十年前嘅遺產代碼。Swift 嘅好處：語法清爽（冇 C 語言年代嘅分號同頭檔案包袱）、可選值（Optional）機制由語言層面消滅「空指標崩潰」、同 SwiftUI 無縫配合、仲有 iPad 上面嘅 Swift Playgrounds 可以邊玩邊學。

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Objective-C 風格（上古遺跡）

{class="font-mono text-xs leading-relaxed"}
NSString *name = @"张三"; [name stringByAppendingString:@"你好"]; // 方括號 + 指標 + 分號三件套
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Swift 風格（現代清爽）

{class="font-mono text-xs leading-relaxed"}
var name = "张三" name += "你好" // 似自然語言咁直白
:::
:::

#### 四、一個 App 係點樣誕生嘅？

同所有平臺一樣，iOS App 嘅誕生都有一條流水線。但蘋果版多咗兩道「安檢」：

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-lightbulb mr-1"></i> 想法</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center">📐 設計（界面+功能）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-keyboard mr-1"></i> 寫代碼（Swift + SwiftUI）</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hammer mr-1"></i> 編譯簽名</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> 測試（模擬器+真機）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-stamp mr-1"></i> 蘋果審覈</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> 上架 App Store</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 1：一個 iOS App 由諗法到上架嘅全流程（注意多出嘅「審核」環節）
:::

流程入面嘅關鍵概念：

- 簽名（Signing）：每個 iOS App 都必須「簽名」先可以安裝——證明「呢個包出自你手，冇畀人改過」。學習階段 Xcode 會用你嘅 Apple ID 自動簽名；上架嗰陣用開發者證書。第 67 章會詳細講。
- 模擬器（Simulator）：喺 Mac 上面虛擬出嚟嘅 iPhone，係開發除錯嘅主戰場。佢行嘅係 Mac 嘅 CPU，所以特別暢順，體驗好過安卓模擬器一大截。
- TestFlight：蘋果官方嘅「內測分發」工具——上架之前將測試版發畀最多 10000 名測試用戶，佢哋用 TestFlight 應用安裝試用。呢個係 iOS 生態獨有嘅優雅。

#### 五、iOS 技術棧全景：你嘅「武器清單」

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">層次</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">主流選擇（2026）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">用嚟做乜嘢</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">語言</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift 6</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">寫邏輯嘅語言</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">界面</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI + 蘋果設計規範（HIG）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用代碼畫界面（本書主線）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">架構</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MVVM + @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">將界面同邏輯分開</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">數據存儲</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData（數據庫）+ UserDefaults（配置）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">將數據存入手機</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">網絡</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession + async/await + Codable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">同服務器對話</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">構建工具</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode Build System / xcodebuild</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">將代碼變成安裝包</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">開發環境</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode（macOS 獨佔）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">蘋果官方 IDE</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
2026 年 iOS 主流技術棧速覽

注意到未：呢套清單比安卓嘅短一截——因為蘋果將好多嘢都「包辦」咗。封閉生態嘅代價係自由度，回報係省心：唔使糾結揀邊個網絡庫、邊個數據庫，官方畀嘅往往就係最優解。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
嚟動手：睇吓你部手機嘅「蘋果戶口」

{class="mt-1"}
打開 iPhone 嘅 [設定] → [一般] → [關於本機]，記低三樣嘢：iOS 版本、機型名稱、可用容量。再去 App Store 嘅「今天」頁求其行吓，留意嗰啲精品 App 嘅截圖同文案——由今日起，你行商店嘅視角要由「用戶」轉做「開發者」喇。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 2008 年 App Store 上線，「應用經濟」誕生；2026 年當前版本係 iOS 27
- 圍牆花園條數：規矩多，但設備少、版本新、用戶肯畀錢、商店乾淨
- 硬門檻：必須有 Mac；上架要 99 美元/年開發者賬號；學習階段免費賬號夠用
- 語言直接學 Swift；Objective-C 只屬於遺產代碼
- 流水線比安卓多一環：蘋果審核；TestFlight 係內測分發神器
- 2026 標準技術棧：Swift 6 + SwiftUI + MVVM + SwiftData + URLSession + Xcode
:::
