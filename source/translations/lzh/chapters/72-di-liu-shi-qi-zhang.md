---
id: di-liu-shi-qi-zhang
num: 67
part: ios-kai-fa-pian
nav: 第六十七章：打磨與發布——上架App Store
toc: default
kind: chapter
---

### 第六十七章：琢磨與發布——測試、調試與上架 App Store

{class="chapter-intro mb-4"}
App 既成，繼之何為？此章答「自能行」至「能交付」之三事：何以高效調試而覓 bug、何以書測試以防回歸、何以獻 App 於 App Store 而使天下載之。上架非徒儀式——乃使作品化為產品之分水嶺也。

#### 一、調試三斧：print、斷點、預覽

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">工具</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">司何事</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">何以用之</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">print + 控制臺</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">觀運行之日誌</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">碼中 print("值=\(x)")，Xcode 底部控制臺觀其出</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">斷點調試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">使程序止於某行，觀變量之值</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">行號旁一點而出藍標，行至彼而暫止，逐步歷之</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI 預覽 + 調試器</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">實時觀界面與視圖之層級</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">#Preview 畫布 + 運行時之 View Hierarchy 檢查器</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
調試三斧

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：崩而何以讀之？

{class="mt-1"}
Swift 崩時，控制臺印 "Fatal error" 及其因，Xcode 止於出誤之行而高亮。真機之舊崩，可於 Xcode → Window → Organizer → Crashes 觀之（須付費之賬）。關鍵之詞，先搜「誤因首句 + swiftui」——問精則答精。
:::

#### 二、測試：為碼投保

手測不足恃——改此一能，彼一能潛壞。測試者，悔之藥也，兼防彈之衣。iOS 用 XCTest 之框，分二種：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">層級</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">測何物</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Target</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">速度</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">單元測試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">純邏輯（計算、校驗）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppTests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">秒級</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UI 測試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真界面之行</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppUITests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分鐘級</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">手動測試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真人之感、體驗</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">恆所需也</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
iOS 測試層級（模板之項已預置二 Test Target）

::: div .code-block
:::inline div .code-head
<span>SWIFT · 單元測試示例</span><span class="dots">···</span>
:::

```
import XCTest

// 將"金額字符串轉數字"此種邏輯抽成純函數
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

行測試：⌘U。既全綠而後改碼，心中乃有據。記賬本中金額之驗、彙總之算，皆當有單元測試護之。

#### 三、署名與打包：為 App 鈐「印」

凡 iOS App 必署名而後可安——以證「此包出於汝，未遭竄改」。層級之係：

- 學習之期：免費 Apple ID + Xcode 自動署名（Personal Team），真機可行，七日一續；
- 分發之期：付費開發者之賬（99 美元/年）簽發證書與描述之檔，而後可上架與久安。

打包：Xcode 菜單 Product → Archive（歸檔），構建既成，於 Organizer 中 Distribute App → 擇 App Store Connect → 上傳。歸檔必以 Generic iOS Device 為的（非擬器），此新手所常忘之一程也。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
避坑之警：證書亡則更新絕

{class="mt-1"}
署名之證與私鑰一亡，則舊 App 不得復更新——用戶惟可安「全新」之應用。善備證書（鑰匙串導出 .p12）而謹記其密碼。幸蘋果有「自動署名」與雲證書之管（Xcode 中勾 Automatically manage signing），能省手工諸坑之大半。
:::

#### 四、上架 App Store 之全程

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> 註冊開發者賬號</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> 準備商店素材</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> 上傳構建包</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> 填隱私與審覈信息</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> 蘋果審覈（1-7 天）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> 上架</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 5：App Store 上架六步
:::

- 註冊：developer.apple.com，個人賬號 99 美元/年；
- 素材：圖標（1024×1024，勿帶圓角——蘋果自裁之）、截圖（iPhone 各尺寸）、描述、隱私政策之連結；
- 隱私之問卷：如實申報所收何數據——不連網之記賬本可「不收任何數據」；
- 審核：首提常候一至七日，見拒則依「審核之註」逐條改之——蘋果拒之由，常書之甚詳，循而行之即可；
- TestFlight：上架之先，以測試版予友內測（至多 10000 人），集一輪之復而後正提，專業之範十足。

#### 五、商店素材何以為之：第一印象即下載之量

商店之頁，用戶「逛店」所見之櫥窗也。三素材定第一印象：

- 圖標：1024×1024，勿以截圖苟且。無設計之能，則以 AI 之具生一簡潔之形，於桌面縮之而猶能一望而識，方為合格；
- 截圖：至少二套（iPhone 主流之尺寸），陳其最核之功能之景；每張配一句白話之文（「一秒記一筆」較「高效記賬之方」善十倍）；
- 描述：首句當明「此何物 + 為誰而作」，勿堆「最專、最強」——誠較誇為效。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：以記賬本「交付」一過

#### 六、崩潰之上報與性能優化小單

App 上架之先，此二事宜各費三十分鐘：

##### 1. 崩潰監控

汝測時不崩，非謂用戶之機不崩。蘋果於 Xcode Organizer 中予免費之崩報（付費之賬可觀真機崩潰之日誌）；更省心者，接第三方 SDK（如 Firebase Crashlytics）。無崩監而上架，猶閉目而御車也。

##### 2. 性能自察四條

1. 列表用 LazyVStack / List：長列表勿以常 VStack 硬排——懶載者，性能第一課也；
2. 圖勿硬塞原圖：用 AsyncImage（遠圖）與系統之緩存，5MB 原圖足以滯壞舊機；
3. 勿於主線程任重務：網絡、大檔皆行 async/await；
4. 以 Instruments 量之：Xcode 自帶性能剖析之器（Time Profiler、記憶體洩漏之檢）——先量而後優，勿憑感覺。

{class="mt-1"}
① 為 parseAmount 等邏輯補三單元測試（⌘U 行之而綠）；② 以斷點親捕自造之崩而修之；③ Product → Archive 打一包，由 TestFlight 邀友內測；④ 有餘力則註冊開發者之賬，以記賬本真提而上架。前三程今夕可成。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小結

- 調試三斧：print 之誌、斷點、SwiftUI 預覽與視圖檢查器
- XCTest：單元測試（⌘U）+ UI 測試 + 手動測試，模板已預置
- 署名：免費賬號自動署名（七日一續）；付費賬號方能分發
- 打包：Generic iOS Device + Archive + Distribute；證書務必備份
- 上架六步：註冊 → 素材 → 上傳 → 隱私問卷 → 審核 → 上架；TestFlight 先內測
:::
