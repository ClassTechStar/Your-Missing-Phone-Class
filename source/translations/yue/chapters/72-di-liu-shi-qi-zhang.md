---
id: di-liu-shi-qi-zhang
num: 67
part: ios-kai-fa-pian
nav: 第六十七章：打磨與發佈——上架App Store
toc: default
kind: chapter
---

### 第六十七章：打磨同發佈——測試、調試同上架 App Store

{class="chapter-intro mb-4"}
App 整好咗，跟住點呢？呢一章回答"由行得到"到"交到貨"嘅三件事：點樣高效咁調試搵 bug、點樣寫測試防回歸、點樣將 App 送上 App Store 畀全世界下載。上架唔止係儀式感——佢係將一件作品變成產品嘅分水嶺。

#### 一、調試三板斧：print、斷點、預覽

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">工具</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">做乜嘢</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">點樣用</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">print + 控制檯</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">睇運行日誌</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">代碼入面 print("值=\(x)")，喺 Xcode 底部控制台睇輸出</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">斷點調試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">令程式停喺某一行，睇變量值</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">喺行號旁邊㩒一下出藍標，運行到嗰度就停，逐步行</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI 預覽 + 調試器</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">即時睇界面同視圖層級</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">#Preview 畫布 + 運行時嘅 View Hierarchy 檢查器</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
調試三板斧

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：崩潰咗點樣讀？

{class="mt-1"}
Swift 崩潰嗰陣控制台會打印 "Fatal error" 加原因，Xcode 會停喺出錯嗰一行並高亮。真機上面嘅歷史崩潰可以喺 Xcode → Window → Organizer → Crashes 入面睇（需要付費賬號）。關鍵詞優先搜"錯誤原因第一句 + swiftui"——精確嘅問題，先至有精確嘅答案。
:::

#### 二、測試：畀代碼上保險

手測靠唔住——改咗呢個功能，另一個靜靜哋壞咗。測試就係"後悔藥"兼"防彈衣"。iOS 用 XCTest 框架，分兩種：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">層級</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">測乜嘢</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Target</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">速度</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">單元測試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">純邏輯（計算、校驗）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppTests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">秒級</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UI 測試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真實界面行為</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppUITests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分鐘級</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">手動測試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真人感受、體驗</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">永遠需要</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
iOS 測試層級（模板項目已預置兩個 Test Target）

::: div .code-block
:::inline div .code-head
<span>SWIFT · 單元測試示例</span><span class="dots">···</span>
:::

```
import XCTest

// 把"金額字串轉數字"呢種邏輯抽成純函數
func parseAmount(_ input: String) -> Double? {
    guard let v = Double(input.trimmingCharacters(in: .whitespaces)),
          v > 0 else { return nil }
    return v
}

final class AmountTests: XCTestCase {
    func testEmptyInputReturnsNil() {
        XCTAssertNil(parseAmount(""))
    }
    func testNegativeReturnsNil() {
        XCTAssertNil(parseAmount("-5"))
    }
    func testNormalValueParses() {
        XCTAssertEqual(parseAmount("12.5"), 12.5)
    }
}
```
:::

行測試：⌘U。全綠之後再改代碼，心裏有底。記賬本入面嘅金額校驗、匯總計算，都應該有單元測試罩住。

#### 三、簽名同打包：畀 App 蓋上"印章"

每個 iOS App 都必須簽名先安裝到——證明"呢個包出自你手，冇畀人改過"。層級關係：

- 學習階段：免費 Apple ID + Xcode 自動簽名（Personal Team），真機行得到，7 日續期一次；
- 分發階段：付費開發者賬號（99 美元／年）簽發證書同描述檔，先可以上架同長期安裝。

打包：Xcode 菜單 Product → Archive（歸檔），構建完成之後喺 Organizer 入面 Distribute App → 揀 App Store Connect → 上傳。歸檔必須用 Generic iOS Device 做目標（唔係模擬器），呢一步係新手成日唔記得嘅。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
避坑提醒：證書丟咗 = 更新斷纜

{class="mt-1"}
簽名證書同私鑰一旦丟失，你就冇得再畀舊 App 發更新——用戶只可以裝"全新"應用。妥當備份證書（鑰匙串導出 .p12）並記好密碼。好在蘋果提供咗"自動簽名"同雲端證書管理（Xcode 入面剔選 Automatically manage signing），可以慳返大部分手工操作嘅坑。
:::

#### 四、上架 App Store 全流程

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> 註冊開發者賬號</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> 準備商店素材</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> 上傳構建包</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> 填隱私與審覈資訊</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> 蘋果審覈（1-7 天）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> 上架</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 5：App Store 上架六步走
:::

- 註冊：developer.apple.com，個人賬號 99 美元／年；
- 素材：圖標（1024×1024，咪帶圓角——蘋果自己切）、截圖（iPhone 各尺寸）、描述、私隱政策連結；
- 私隱問卷：如實申報收集咗哪些數據——唔上網嘅記賬本可以"唔收集任何數據"；
- 審核：首次提交通常要等 1-7 日，被拒就按"審核備註"逐條改——蘋果嘅拒絕理由通常寫得好具體，照做就得；
- TestFlight：上架之前先將測試版傳畀朋友內測（最多 10000 人），收集一輪反饋再正式提交，專業範十足。

#### 五、商店素材點樣做：第一印象就係下載量

商店頁係用戶"行街"嗰陣睇到嘅櫥窗。三個素材決定第一印象：

- 圖標：1024×1024，咪用截圖求其頂住。冇設計能力就用 AI 工具生成一個簡潔圖形，喺桌面縮細之後仲一眼認得出先算合格；
- 截圖：至少 2 套（iPhone 主流尺寸），展示最核心嘅功能場景；每張配一句貼地文案（"一秒記一筆"好過"高效的記賬解決方案"十倍）；
- 描述：第一句講清楚"呢個係乜嘢 + 畀邊個用"，咪堆砌"最專業、最強"——真誠好過誇張。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
嚟動手：將記賬本"交付"一次

#### 六、崩潰上報同性能優化小清單

App 上架之前，呢兩件事值得各花半個鐘：

##### 1. 崩潰監控

你測試嗰陣冇崩，唔代表用戶部手機唔崩。蘋果喺 Xcode Organizer 入面提供免費嘅崩潰報告（付費賬號可以睇真機崩潰日誌）；更省心嘅方案係接入第三方 SDK（好似 Firebase Crashlytics 咁）。冇崩潰監控就上架，等於合埋眼揸車。

##### 2. 性能自查四條

1. 列表用 LazyVStack / List：長列表咪用普通 VStack 硬排——懶加載係性能第一課；
2. 圖片咪硬塞原圖：用 AsyncImage（遠程圖）同系統快取，5MB 原圖足以卡爆舊機型；
3. 咪喺主線程做重活：網絡、大文件都行 async/await；
4. 用 Instruments 度一度：Xcode 自帶嘅性能分析器（Time Profiler、記憶體泄漏檢查）——先測量，再優化，咪靠感覺。

{class="mt-1"}
① 畀 parseAmount 等邏輯補 3 個單元測試（⌘U 行到全綠）；② 用斷點親手捉一個自己整出嚟嘅崩潰並整好佢；③ Product → Archive 打一個包，行 TestFlight 邀請朋友內測；④ 有餘力就註冊開發者賬號，將記賬本真正提交上架。頭三步今晚就做得完。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 調試三板斧：print 日誌、斷點、SwiftUI 預覽同視圖檢查器
- XCTest：單元測試（⌘U）+ UI 測試 + 手動測試，模板已預置
- 簽名：免費賬號自動簽名（7 日續期）；付費賬號先可以分發
- 打包：Generic iOS Device + Archive + Distribute；證書務必備份
- 上架六步：註冊 → 素材 → 上傳 → 私隱問卷 → 審核 → 上架；TestFlight 先內測
:::
