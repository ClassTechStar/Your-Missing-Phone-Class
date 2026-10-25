---
id: di-liu-shi-jiu-zhang
num: 69
part: ios-kai-fa-pian
nav: 第六十九章：速查手冊與資源
toc: default
kind: chapter
---

### 第六十九章：速查手冊與資源

{class="chapter-intro mb-4"}
本章是一份可以獨立使用的速查手冊。當你記不清某個寫法或需要快速決策時，直接翻到這裡。建議把它當成"口袋卡片"：常用程式碼速查、常見問題、學習資源，一頁不落。

#### 一、常用程式碼速查卡

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要做什麼</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">關鍵程式碼</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">頁面私有狀態</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State private var x = 初值</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跨頁面邏輯</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Observable class VM { var x = 0 }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">豎排/橫排佈局</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack { }</code> / <code class="inline">HStack { }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">彈性空間</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Spacer()</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">列表</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List { ForEach(陣列) { ... } }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">頁面跳轉</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">NavigationStack + NavigationLink</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">底部跳出視窗</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">.sheet(isPresented: $show) { 內容 }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">關當前頁</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Environment(\.dismiss) var dismiss</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">聯網取資料</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">try await URLSession.shared.data(from: url)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">JSON 解析</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X: Codable</code> + <code class="inline">JSONDecoder().decode</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">存小配置</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults.standard.set(值, forKey: "鍵")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">存結構化資料</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Model</code> + <code class="inline">modelContainer</code> + <code class="inline">@Query</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">深色模式適配</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用系統顏色（.primary / Color(.systemGray6)），不寫死</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跑測試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><kbd>⌘U</kbd></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
iOS 開發速查卡（2026 年 8 月版）

#### 二、常見問題 FAQ

Q1：我沒有 Mac，能學 iOS 開發嗎？

能學語言，不能做完整開發。iPad/iPhone 上的 Swift Playgrounds 可以學完第 61 章的全部內容；但 Xcode 是 macOS 獨佔，最終必須有一臺 Mac。預算有限可以先租雲 Mac 或買二手 Mac mini 過渡，學完語言再決定投入。

Q2：學 iOS 開發要花多少錢？

學習階段：0 元（Xcode 免費 + 免費 Apple ID 真機除錯）。發佈階段：開發者帳號 99 美元/年（約 700 元）。加上一台 Mac 的硬體投入，這就是全部成本。相比回報——App Store 上哪怕一個小工具也有付費使用者——這筆帳算下來非常值得。

Q3：SwiftUI 和 UIKit 先學哪個？

SwiftUI。2026 年的新專案、新教學、新崗位都以 SwiftUI 為主，本書全程用它。UIKit 是上一代框架，仍在大量老專案中使用——等你 SwiftUI 熟練後，按需補 UIKit（官方有互操作教學），上手會很快。順序別反了。

Q4：iOS 開發好找工作嗎？

2026 年的行情：純"會畫介面"的初級崗位競爭激烈，但"懂 Swift + SwiftUI + 有上架作品"的開發者依然搶手。iOS 崗位的薪資中位數在各技術棧裡常年靠前。學習期的你，最好的簡歷就是商店裡那個自己做的 App。

Q5：App 被稽核拒絕了怎麼辦？

別慌，很正常——首次提交被拒的機率不低。蘋果的拒絕理由通常寫得非常具體（哪個頁面、哪條準則），逐條修改後在 App Store Connect 裡回覆說明，重新提交即可。常見的三大拒絕原因：權限用途說不清、介面有 bug、後設資料（截圖/描述）與實物不符。提前自查這三項，能省一輪等待。

#### 三、Xcode 高頻快速鍵速查

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">操作</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">快速鍵</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">執行 / 測試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R / ⌘U</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">開啟畫布預覽</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">快速開啟檔案</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全域性搜尋</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘F</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">格式化縮排</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">註釋 / 取消註釋</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">清理構建快取</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘K</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跳轉到定義</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘ 點按</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">重新命名（全域性安全改名）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">右鍵 → Refactor → Rename</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Xcode 高頻快速鍵速查

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：編譯玄學先清快取

{class="mt-1"}
"昨天還能跑今天就不行"的靈異事件，十有六七是構建快取錯亂。⇧⌘K 清理後重新構建，能治癒一大半玄學問題。還不行就重啟 Xcode（連 Mac 一起），再不行就"刪掉 DerivedData 資料夾"——這是 iOS 開發者口口相傳的終極三連。
:::

#### 四、推薦學習資源

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">型別</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">資源</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">推薦理由</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">developer.apple.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">蘋果官方文件，SwiftUI/Swift 教學都在裡面，第一權威</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple 的 SwiftUI Tutorials</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方手把手課程，新手友好度滿分</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift 官網 (swift.org)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">語言官方文件與線上演練場</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">社群</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hacking with Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Paul Hudson 的免費教學庫，品質公認第一梯隊</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">社群</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stack Overflow (swiftui 標籤)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">報錯求救第一站</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">影片</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Developer 官方頻道（WWDC 影片）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每年新技術的權威講解</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">設計</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple 人機介面指南（HIG）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">做出"蘋果味"介面的官方聖經</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">配套</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第七篇《AI程式設計實戰篇》（第37-47章）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用 AI 輔助 iOS 開發的完整心法</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
iOS 開發學習資源清單（2026 年 8 月）

#### 五、結語：從第一個 App 到第 N 個 App

回頭看，你從"不知道 SwiftUI 是什麼"，到裝好 Xcode、學會 Swift、用 SwiftUI 畫出介面、給 App 接上資料庫和網路，再到測試、打包、上架——這條路上你已經走完了從零到一最難的一段。

技術的世界變化很快：框架會升級，工具會換代，AI 會接手越來越多"敲鍵盤"的活。但有一樣東西不會過時：你把一個模糊的想法，拆解成清晰的步驟，再一步步實現它的能力。工具是放大器，思路是地基。放大器可以替換，地基不能動搖。

:::inline div .quote-line
你不再只是"會玩手機的人"。你能把腦海裡的想法，變成數億臺 iPhone 上真實執行的 App。從今天開始，用鍵盤去創造——這就是 iOS 開發者的浪漫。
:::

#### 參考文獻

{class="list-decimal pl-6 mb-3 space-y-1 text-xs text-gray-500"}
1. Apple Inc. (2026). SwiftUI Framework Documentation. developer.apple.com.
2. Apple Inc. (2026). Swift Programming Language Guide. swift.org.
3. Apple Inc. (2026). SwiftData Framework Documentation. developer.apple.com.
4. Apple Inc. (2026). App Store Review Guidelines. developer.apple.com/app-store/review.
5. Apple Inc. (2026). Human Interface Guidelines (HIG). developer.apple.com/design.
6. Apple Inc. (2026). Xcode 27 Release Notes and App Distribution Guide.
