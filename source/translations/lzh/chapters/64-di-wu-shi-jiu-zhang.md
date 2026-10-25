---
id: di-wu-shi-jiu-zhang
num: 59
part: ios-kai-fa-pian
nav: 第五十九章：認識iOS——蘋果生態與開發生態
toc: default
kind: chapter
---

### 第五十九章：識 iOS——蘋果生態與開發生態

{class="chapter-intro mb-4"}
賀爾成此決——自「用 iPhone 之人」而為「為 iPhone 作應用之人」。動手之前，吾儕且先攤開輿圖：iOS 何自而來？蘋果「圍牆之園」於開發者何謂？一 App 自爾指敲鍵盤至用戶之機，其中何事之有？

#### 一、iOS 之身世：一機改一行

2007 年正月，喬布斯於發布會出首代之 iPhone。其時尚不容第三方之應用——至 2008 年，蘋果出 App Store 與 iPhone SDK，許天下開發者為 iPhone 作軟件。當是時，「應用經濟」生焉：至今 App Store 之上有應用數百萬，為開發者累分成逾數千億美元。

系統亦自進化：初名 iPhone OS，2010 年改曰 iOS；版本號行至 iOS 17（2023），至 2025 年，蘋果改命名以隨年份——iOS 26 於 2025 年發布，2026 年 8 月今之版乃 iOS 27。命名雖變，然一事未嘗變：iOS 用戶付費之習與軟件質量之譽，移動生態之中公認至善——同一之 App，iOS 端之入往往顯高於安卓端。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">節點</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">年份</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">於開發者至要之事</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">App Store 上線</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2008</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第三方開發之生態啟</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift 發布</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2014</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">現代 iOS 開發之語登場</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI 發布</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2019</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">聲明式界面之框架，本書主線</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">iOS 26（改名之元年）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2025</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">命名隨年份；Apple Intelligence 全面整合</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">iOS 27</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2026</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">今之最新版（本書基準）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
iOS 開發大事記（截至 2026 年 8 月）

#### 二、圍牆之園：蘋果生態之「規」與「利」

蘋果生態常被謂為「圍牆之園」（Walled Garden）——規多而管嚴：App 必經審核方得上架、開發必用 Mac 與 Xcode、分發多走 App Store。聞之豈不憋悶？然於開發者，此套規矩換得真金白銀之利：

- 設備碎片之化至微：iPhone 之型不過數款，屏之尺寸、系統之版高度劃一——爾適 5 型之機，即覆 95% 之用戶（安卓或須適數十款）；
- 系統版本更新之率至高：新系統發布數週之內，七八成用戶已升，新 API 可大膽用之，不必顧「五年前之舊系統」；
- 用戶付費之習善：App Store 之用戶更樂為應用與內購出資；
- 審核雖嚴，然商店潔：山寨流氓之軟件少，佳品易為人所見。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：先明其成本

{class="mt-1"}
iOS 開發有硬檻：必有 Mac 一台（Xcode 為 macOS 所獨佔），上架須 99 美元一年之開發者帳號（個人開發者免費之帳可於本地真機調試，然不能上架）。思此投入而後啟程——然可喜者，學習之期用免費之帳綽綽有餘，第 60 章將言之。
:::

#### 三、以何語言書寫：Objective-C 抑或 Swift？

iOS 開發之史亦有二「主角」。Objective-C 者開國之元老也——自 2008 年用至 2014 年；Swift 者蘋果 2014 年所發之新語也，其後進化至 Swift 6（2024 年發布，引入嚴格並發之檢查），至 2026 年，新項目幾盡用 Swift。

贈零基之爾一句實話：徑學 Swift，Objective-C 並觀亦不必——除非爾就職之後須守十年前之遺產代碼。Swift 之利：語法清爽（無 C 語之世分號與頭文件之累）、可選值（Optional）之制自語言之層滅「空指針崩潰」之業中惡夢、與 SwiftUI 無縫相合、且 iPad 之上 Swift Playgrounds 可且玩且學。

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Objective-C 之風（上古之遺跡）

{class="font-mono text-xs leading-relaxed"}
NSString *name = @"張三"; [name stringByAppendingString:@"你好"]; // 方括號 + 指針 + 分號三件套
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Swift 之風（今世之清爽）

{class="font-mono text-xs leading-relaxed"}
var name = "張三" name += "你好" // 直白如自然之言
:::
:::

#### 四、一個 App 何以誕生？

與諸平臺同，iOS App 之生亦有一條流水之線。然蘋果之版多兩道「安檢」：

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-lightbulb mr-1"></i> 想法</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center">📐 設計（界面+功能）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-keyboard mr-1"></i> 寫代碼（Swift + SwiftUI）</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hammer mr-1"></i> 編譯簽名</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> 測試（模擬器+真機）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-stamp mr-1"></i> 蘋果審覈</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> 上架 App Store</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖一：一 iOS App 自念頭至上架之全流程（注意多出之「審核」環節）
:::

流程中之關鍵概念：

- 簽名（Signing）：每 iOS App 皆必「簽名」方能安裝——以證「此包出於爾，未被篡改」。學習之期 Xcode 以爾之 Apple ID 自動簽之；上架則用開發者之證書。第 67 章詳之。
- 模擬器（Simulator）：Mac 上虛擬而出之 iPhone，開發調試之主戰場也。其所行者 Mac 之 CPU，故特流暢，較安卓之模擬器體驗勝一大截。
- TestFlight：蘋果官方「內測分發」之器——上架之前以測試之版致至多 10000 名測試之用戶，彼等以 TestFlight 之應用安裝而試之。此 iOS 生態獨有之雅也。

#### 五、iOS 技術棧全景：爾之「武器清單」

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">層次</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">主流之擇（2026）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">何所用</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">語言</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift 6</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">作邏輯之語言</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">界面</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI 加蘋果設計之規範（HIG）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">以代碼繪界面（本書主線）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">架構</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MVVM + @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分界面與邏輯</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">數據儲存</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData（數據庫）加 UserDefaults（配置）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">存數據於手機之中</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">網絡</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession + async/await + Codable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">與服務器對話</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">構建之器</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode Build System / xcodebuild</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">化代碼為安裝之包</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">開發環境</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode（macOS 獨佔）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">蘋果官方之 IDE</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
2026 年 iOS 主流技術棧速覽

覺之否：此單較安卓者短一截——以蘋果多事皆「包辦」矣。封閉生態之價，自由度也；其償，省心也：不必糾結擇何網絡之庫、何數據庫，官方所予往往即至優之解。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：看看爾手機之「蘋果戶口」

{class="mt-1"}
開 iPhone 之［設定］→［一般］→［關於本機］，記三事：iOS 之版本、機型之名、可用之容量。再往 App Store「今日」之頁隨意遊之，留意精品 App 之截圖與文案——自今日始，爾遊商店之目，當自「用戶」而易為「開發者」矣。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 2008 年 App Store 上線，「應用經濟」生焉；2026 年今之版乃 iOS 27
- 圍牆之園之帳：規矩多，然設備少、版本新、用戶肯出資、商店潔
- 硬檻：必有 Mac；上架須 99 美元一年之開發者帳號；學習之期免費之帳足矣
- 語言徑學 Swift；Objective-C 惟屬遺產之代碼
- 流水線較安卓多一環：蘋果審核；TestFlight 乃內測分發之利器
- 2026 標準技術棧：Swift 6 加 SwiftUI 加 MVVM 加 SwiftData 加 URLSession 加 Xcode
:::
