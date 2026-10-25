---
id: di-liu-shi-jiu-zhang
num: 69
part: ios-kai-fa-pian
nav: 第六十九章：速查手冊與資源
toc: default
kind: chapter
---

### 第六十九章：速查之冊與資源

{class="chapter-intro mb-4"}
此章者，可獨用之速查冊也。汝記不清某寫法、或須速決之際，徑翻至此。宜視之為「囊中之卡」：常用碼之速查、常見之問、學習之資，一頁不遺。

#### 一、常用碼速查之卡

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">欲作何事</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">關鍵之碼</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">頁面私有之態</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State private var x = 初值</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跨頁之邏輯</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Observable class VM { var x = 0 }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">豎列/橫列之佈</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack { }</code> / <code class="inline">HStack { }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">彈性之空</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Spacer()</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">列表</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List { ForEach(陣列) { ... } }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">頁面之跳轉</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">NavigationStack + NavigationLink</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">底部彈窗</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">.sheet(isPresented: $show) { 內容 }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">闔當前頁</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Environment(\.dismiss) var dismiss</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">連網取數據</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">try await URLSession.shared.data(from: url)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">JSON 之解析</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X: Codable</code> + <code class="inline">JSONDecoder().decode</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">貯小配置</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults.standard.set(值, forKey: "鍵")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">貯結構化數據</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Model</code> + <code class="inline">modelContainer</code> + <code class="inline">@Query</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">深色模式之配</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用系統顏色（.primary / Color(.systemGray6)），勿寫死</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">行測試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><kbd>⌘U</kbd></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
iOS 開發速查之卡（2026 年 8 月版）

#### 二、常見之問 FAQ

Q1：吾無 Mac，可學 iOS 開發乎？

可學其語，難為全之開發。iPad/iPhone 之 Swift Playgrounds，足學第 61 章之全文；然 Xcode 為 macOS 所獨，終須有一 Mac。預算有限者，可先租雲 Mac 或購二手 Mac mini 以過渡，學成其語再定所投。

Q2：學 iOS 開發，費幾何？

學習之期：0 元（Xcode 免費 + 免費 Apple ID 真機調試）。發布之期：開發者賬號 99 美元/年（約 700 元）。加一 Mac 硬件之投，此其全費也。較其所償——App Store 之上，雖一小具亦有付費之戶——此賬合算。

Q3：SwiftUI 與 UIKit，孰先學？

SwiftUI。2026 年新之項、新之教、新之職，皆以 SwiftUI 為主，本書終始用之。UIKit 為前代之框，猶多用於舊項——待汝 SwiftUI 嫻熟，按需補 UIKit（官方有互通之教），上手甚速。序勿倒置。

Q4：iOS 開發，覓職易乎？

2026 年之市情：徒「能繪界面」之初職，競爭烈；然「曉 Swift + SwiftUI + 有上架之作」之開發者，猶為所爭。iOS 職之俸中數，於諸技之列常居前。學習期之汝，至善之履歷，即商店中自作之 App。

Q5：App 為審核所拒，奈何？

勿惶，此常事也——首提見拒之率不低。蘋果拒之由，常書之甚具（何頁、何條之則），逐條改之，於 App Store Connect 復而說明，再提即可。常見拒之三大由：權限之用不明、界面有 bug、元數據（截圖/描述）與實物不符。先自察此三，可省一輪之候。

#### 三、Xcode 高頻快捷鍵速查

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">操作</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">快捷鍵</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">運行 / 測試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R / ⌘U</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">啟畫布預覽</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">速啟檔案</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全局搜索</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘F</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">格式化縮進</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">註釋 / 去註釋</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">滌構建之緩存</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘K</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跳至其定義</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘ 點按</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">易名（全局安改）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">右鍵 → Refactor → Rename</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Xcode 高頻快捷鍵速查

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：編譯玄而莫測，先滌緩存

{class="mt-1"}
「昨日可行今日不可」之靈異，什六七為構建緩存之亂。⇧⌘K 滌之而重構，可愈玄惑之大半。不驗則重啟 Xcode（並 Mac 同之），再不驗則「刪 DerivedData 之夾」——此 iOS 開發者口耳相傳之終極三連也。
:::

#### 四、薦學習之資

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">類型</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">資源</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">薦之之由</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">developer.apple.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">蘋果官方之檔，SwiftUI/Swift 之教悉在其中，權威居首</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple 之 SwiftUI Tutorials</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方親授之程，於新手至為友善</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift 官網 (swift.org)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">語言官方之檔與在線演練之場</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">社群</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hacking with Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Paul Hudson 免費教程之庫，其質公認居首列</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">社群</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stack Overflow (swiftui 標籤)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">報錯求救之首驛</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">視頻</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Developer 官方之頻道（WWDC 視頻）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">歲歲新技之權威講解</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">設計</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple 人機界面指南（HIG）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">造「蘋果味」界面之官方聖經</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">配套</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第七篇《AI編程實戰篇》（第37-47章）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">以 AI 輔助 iOS 開發之完整心法</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
iOS 開發學習資源清單（2026 年 8 月）

#### 五、結語：從第一個 App 到第 N 個 App

回顧既往，爾自「不知 SwiftUI 為何物」，至裝好 Xcode、學會 Swift、以 SwiftUI 繪出界面、為 App 接上數據庫與網絡，再到測試、打包、上架——此路之上，爾已走完從零到一最難之一段。

技藝之世界變化極快：框架會升級，工具會換代，AI 會接手越來越多「敲鍵盤」之活。然有一物不會過時：爾把模糊之想法，拆解成清晰之步驟，再一步步實現之能力。工具者，放大器也；思路者，地基也。放大器可替換，地基不可動搖。

:::inline div .quote-line
汝不復徒為"玩手機之人"。汝能以胸中之念，化為數億 iPhone 上實運行之 App。自今日始，以鍵盤創物——此 iOS 開發者之浪漫也。
:::

#### 參考文獻

{class="list-decimal pl-6 mb-3 space-y-1 text-xs text-gray-500"}
1. Apple Inc. (2026). SwiftUI Framework Documentation. developer.apple.com.
2. Apple Inc. (2026). Swift Programming Language Guide. swift.org.
3. Apple Inc. (2026). SwiftData Framework Documentation. developer.apple.com.
4. Apple Inc. (2026). App Store Review Guidelines. developer.apple.com/app-store/review.
5. Apple Inc. (2026). Human Interface Guidelines (HIG). developer.apple.com/design.
6. Apple Inc. (2026). Xcode 27 Release Notes and App Distribution Guide.
