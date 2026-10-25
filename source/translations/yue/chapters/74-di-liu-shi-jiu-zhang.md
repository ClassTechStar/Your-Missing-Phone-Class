---
id: di-liu-shi-jiu-zhang
num: 69
part: ios-kai-fa-pian
nav: 第六十九章：速查手冊與資源
toc: default
kind: chapter
---

### 第六十九章：速查手冊同資源

{class="chapter-intro mb-4"}
本章係一份可以獨立使用嘅速查手冊。當你記唔清某個寫法或者需要快速決策嗰陣，直接揭到呢度。建議將佢當成"口袋卡"：常用代碼速查、常見問題、學習資源，一頁都唔漏。

#### 一、常用代碼速查卡

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">想做乜嘢</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">關鍵代碼</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">頁面私有狀態</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State private var x = 初值</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跨頁面邏輯</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Observable class VM { var x = 0 }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">直排／橫排佈局</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack { }</code> / <code class="inline">HStack { }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">彈性空間</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Spacer()</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">列表</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List { ForEach(陣列) { ... } }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">頁面跳轉</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">NavigationStack + NavigationLink</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">底部彈窗</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">.sheet(isPresented: $show) { 內容 }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">閂當前頁</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Environment(\.dismiss) var dismiss</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">上網攞數據</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">try await URLSession.shared.data(from: url)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">JSON 解析</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X: Codable</code> + <code class="inline">JSONDecoder().decode</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">存小配置</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults.standard.set(值, forKey: "鍵")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">儲存結構化數據</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Model</code> + <code class="inline">modelContainer</code> + <code class="inline">@Query</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">深色模式適配</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用系統顏色（.primary / Color(.systemGray6)），唔好寫死</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">行測試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><kbd>⌘U</kbd></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
iOS 開發速查卡（2026 年 8 月版）

#### 二、常見問題 FAQ

Q1：我冇 Mac，可唔可以學 iOS 開發？

可以學語言，但做唔到完整開發。iPad/iPhone 上的 Swift Playgrounds 可以學完第 61 章嘅全部內容；不過 Xcode 係 macOS 獨佔，最終一定要有一部 Mac。預算有限可以先租雲端 Mac 或者買二手 Mac mini 過渡，學完語言再決定投入幾多。

Q2：學 iOS 開發要使幾多錢？

學習階段：0 蚊（Xcode 免費 + 免費 Apple ID 真機調試）。發佈階段：開發者帳號 99 美元一年（大概 700 蚊）。加埋一部 Mac 嘅硬件投入，呢個就係全部成本。比起回報——App Store 上就算一個小工具都有人肯畀錢——呢條數好劃算。

Q3：SwiftUI 同 UIKit 應該先學邊個？

SwiftUI。2026 年嘅新項目、新教程、新職位都以 SwiftUI 為主，本書全程都用佢。UIKit 係上一代框架，仍然喺大量舊項目入面用緊——等你 SwiftUI 熟練之後，按需要補返 UIKit（官方有互操作教程），上手會好快。次序唔好掉轉。

Q4：學識 iOS 開發容唔容易搵工？

2026 年嘅行情：淨係「識畫介面」嘅初級職位競爭好激烈，但「識 Swift + SwiftUI + 有上架作品」嘅開發者依然搶手。iOS 職位嘅人工中位數喺各個技術棧入面長期排前列。學習期嘅你，最好嘅履歷就係 App Store 入面你自己整嗰個 App。

Q5：App 俾審核拒絕咗點算？

唔使慌，好正常——第一次提交被拒嘅機率唔低。蘋果嘅拒絕理由通常寫得好具體（邊個頁面、邊條準則），逐條修改之後喺 App Store Connect 入面回覆說明，再重新提交就得。三大常見拒絕原因：權限用途講唔清、介面有 bug、元數據（截圖／描述）同實物唔符。提早自查呢三項，可以慳返一輪等待。

#### 三、Xcode 高頻快捷鍵速查

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">操作</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">快捷鍵</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">運行 / 測試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R / ⌘U</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">打開畫布預覽</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">快速打開檔案</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全域搜尋</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘F</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">格式化縮排</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">註解 / 取消註解</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">清理構建快取</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘K</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跳到定義</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘ 點按</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">重新命名（全域安全改名）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">右鍵 → Refactor → Rename</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Xcode 高頻快捷鍵速查

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：編譯玄學先清快取

{class="mt-1"}
「琴日仲行到今日就行唔到」呢啲靈異事件，十居其六七都係構建快取錯亂。⇧⌘K 清理完重新構建，可以醫好一大半玄學問題。仲唔得就重啟 Xcode（連 Mac 一齊），再唔得就「剷走 DerivedData 資料夾」——呢個係 iOS 開發者口耳相傳嘅終極三連。
:::

#### 四、推薦學習資源

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">類型</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">資源</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">推薦理由</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">developer.apple.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">蘋果官方文件，SwiftUI/Swift 教程全部都喺入面，第一權威</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple 嘅 SwiftUI Tutorials</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方手把手課程，對新手友好度滿分</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift 官網 (swift.org)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">語言官方文件同埋線上演練場</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">社區</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hacking with Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Paul Hudson 嘅免費教程庫，質素公認第一梯隊</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">社區</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stack Overflow (swiftui 標籤)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">報錯求救第一站</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">影片</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Developer 官方頻道（WWDC 影片）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每年新技術嘅權威講解</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">設計</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple 人機介面指南（HIG）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">做出「蘋果味」介面嘅官方聖經</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">配套</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第七篇《AI編程實戰篇》（第37-47章）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用 AI 輔助 iOS 開發嘅完整心法</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
iOS 開發學習資源清單（2026 年 8 月）

#### 五、結語：由第一個 App 到第 N 個 App

回頭看，你由「唔知 SwiftUI 係乜嘢」，到裝好 Xcode、學識 Swift、用 SwiftUI 畫出介面、幫個 App 接上資料庫同網絡，再到測試、打包、上架——呢條路上你已經行完咗由零到一最難嗰一段。

技術嘅世界變得好快：框架會升級，工具會換代，AI 會接手越嚟越多「敲鍵盤」嘅嘢。但有一樣嘢唔會過時：你將一個模糊嘅諗法，拆解成清晰嘅步驟，再一步一步實現佢嘅能力。工具係放大器，思路係地基。放大器可以換，地基唔可以郁。

:::inline div .quote-line
你唔再只係"識玩手機嘅人"。你可以將腦入面嘅諗法，變成喺幾億部 iPhone 上面真實運行嘅 App。由今日開始，用鍵盤去創造——呢個就係 iOS 開發者嘅浪漫。
:::

#### 參考文獻

{class="list-decimal pl-6 mb-3 space-y-1 text-xs text-gray-500"}
1. Apple Inc. (2026). SwiftUI Framework Documentation. developer.apple.com.
2. Apple Inc. (2026). Swift Programming Language Guide. swift.org.
3. Apple Inc. (2026). SwiftData Framework Documentation. developer.apple.com.
4. Apple Inc. (2026). App Store Review Guidelines. developer.apple.com/app-store/review.
5. Apple Inc. (2026). Human Interface Guidelines (HIG). developer.apple.com/design.
6. Apple Inc. (2026). Xcode 27 Release Notes and App Distribution Guide.
