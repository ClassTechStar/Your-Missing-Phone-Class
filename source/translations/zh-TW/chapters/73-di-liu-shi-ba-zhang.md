---
id: di-liu-shi-ba-zhang
num: 68
part: ios-kai-fa-pian
nav: 第六十八章：進階之路——權限、通知與現代架構
toc: default
kind: chapter
---

### 第六十八章：進階之路——權限、通知與現代架構

{class="chapter-intro mb-4"}
能做出 App 只是開始。這一章聊聊從"會做"到"做好"的幾道坎：怎麼優雅地申請權限、怎麼發通知不討人厭、怎麼把架構再往上抬一層，以及——在 2026 年，怎麼和 AI 搭檔寫 iOS 程式碼。每一條都是你在真實專案裡馬上會遇到的。

#### 一、權限：先敲門，再進門

相機、定位、通訊錄、通知……這些"敏感地帶"，iOS 要求 App 在用到時向使用者跳出視窗申請。規矩是"宣告 + 申請 + 優雅降級"三步：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 許可權申請（以定位為例）</span><span class="dots">···</span>
:::

```
// 1. Info.plist 裡宣告用途文案（不宣告直接崩潰！）
// Privacy - Location When In Use Usage Description: "用於查詢你所在城市的天氣"

// 2. 用的時候申請
import CoreLocation

@Observable
class LocationModel {
    private let manager = CLLocationManager()

    func request() {
        switch manager.authorizationStatus {
        case .notDetermined: manager.requestWhenInUseAuthorization()
        case .denied, .restricted: /* 引導去設定裡開 */
        default: /* 已授權，開幹 */
        }
    }
}

// 3. 被拒後優雅降級：給提示 + 跳設定
// UIApplication.shared.open(URL(string: UIApplication.openSettingsURLString)!)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：iOS 權限的"一次性"

{class="mt-1"}
iOS 的權限跳出視窗只彈一次——使用者拒絕後再也不會彈。所以：申請的時機要選在"使用者正要用的那一刻"（而不是一啟動就彈一堆），文案要說明用途。被拒後的介面引導（"去設定裡開啟定位"）是標配，別讓使用者困在死衚衕裡。
:::

#### 二、通知：在正確的時間說有用的話

通知是 App 觸達使用者的通道，也是最容易被使用者"拉黑"的功能。iOS 用 UserNotifications 框架，發通知三條紀律：只發有用的、讓使用者能關、別半夜騷擾。基礎用法：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 本地通知</span><span class="dots">···</span>
:::

```
import UserNotifications

// 1. 申請通知許可權（彈窗一次）
UNUserNotificationCenter.current()
    .requestAuthorization(options: [.alert, .sound, .badge]) { granted, _ in
        print(granted ? "已授權" : "被拒絕")
    }

// 2. 安排一條"每天 20:00 記帳提醒"
func scheduleDailyReminder() {
    let content = UNMutableNotificationContent()
    content.title = "記帳提醒"
    content.body = "今天還沒記帳哦"
    content.sound = .default

    var comps = DateComponents()
    comps.hour = 20
    let trigger = UNCalendarNotificationTrigger(dateMatching: comps, repeats: true)

    let request = UNNotificationRequest(
        identifier: "daily-reminder",
        content: content,
        trigger: trigger
    )
    UNUserNotificationCenter.current().add(request)
}
```
:::

注意：iOS 的通知權限同樣"只彈一次"，且使用者隨時可以在系統設定裡關掉——所以通知內容的價值感很重要，濫發一次可能就永遠失去使用者。

#### 三、架構進階：MVVM 深入與可測試性

第 65 章用過 MVVM，這裡補三個進階要點：

- 協議抽象：讓 ViewModel 依賴協議（protocol）而不是具體類——測試時可以注入"假資料來源"，這是可測試性的基石；
- 單一職責：一個 ViewModel 只管一件事（記帳的不管天氣）；功能多了就拆；
- 別過度設計：單人小專案，"@Observable 類 + 協議抽象"就夠了。VIPER、Clean Architecture 這類重架構，等團隊和複雜度找上門再說——工具是服務目標的，不是用來炫耀的。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：SwiftUI 的"生態紅利"

{class="mt-1"}
iOS 生態還有兩個"只此一家"的進階玩法：小工具（WidgetKit）讓使用者不開啟 App 就能看資訊（記帳本的"本月支出"放桌面），快捷指令（App Intents）讓使用者用 Siri 或自動化呼叫你的功能。兩者都有官方框架，入門成本不高，但對使用者體驗的加成巨大——進階路上值得優先解鎖。
:::

#### 四、2026 年的新玩法：AI 輔助 iOS 開發

2026 年，AI 已經深度嵌入蘋果開發流程。如果你想提速，這套組合拳很成熟：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">環節</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">AI 怎麼幫</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">你的職責</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">寫程式碼</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode 內建程式碼補全 + 第三方 AI 外掛生成</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">描述清楚需求，審查產出</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">查資料</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把官方文件和報錯資訊丟給 AI 解讀</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">關鍵結論回官方文件核實</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">寫測試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">讓 AI 按"正常/邊界/異常"三類生成 XCTest 用例</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">確認用例符合業務語義</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">改 bug</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">貼崩潰日誌 + 相關程式碼，AI 定位修復</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">看懂改動，跑測試驗證</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
AI 輔助 iOS 開發的四個場景

具體方法論——怎麼給 AI 下指令、怎麼驗收、怎麼避坑——完整的 11 章內容在本書第七篇《AI程式設計實戰篇》（第37-47章）裡，強烈建議配合閱讀：Swift 語法交給本篇，AI 協作的心法交給第七篇。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：給記帳本加"三件套"

#### 五、Swift 併發要點：@MainActor 與 Task

Swift 6 的併發體系有兩條新手必懂的規則：

- 介面只能在主執行緒更新：SwiftUI 檢視預設是 @MainActor，網路回撥回到主執行緒再改狀態（await MainActor.run { ... } 或把 ViewModel 標成 @MainActor）；
- 非同步任務用 Task 管理：.task { } 修飾符隨檢視出現自動開始、消失自動取消——這是 SwiftUI 裡啟動非同步工作的標準姿勢，別在 body 裡亂寫 Task 裸奔。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 標準非同步姿勢</span><span class="dots">···</span>
:::

```
struct WeatherScreen: View {
    @State private var vm = WeatherViewModel()

    var body: some View {
        Group {
            switch vm.state {
            case .loading: ProgressView()
            case .success(let d): WeatherContent(data: d)
            case .error(let m): Text(m)
            }
        }
        .task {                       // 出現即開始，消失即取消
            await vm.search(city: "北京")
        }
    }
}
```
:::

這兩條規則背後是 Swift 6 的"資料競爭安全"設計——編譯器會在你寫錯時直接報錯，而不是等 App 崩了才發現。編譯器的報錯不是找茬，是替你擋子彈。

{class="mt-1"}
① 給記帳本加"每天 20:00 記帳提醒"（通知權限 + 本地通知）；② 把 ViewModel 的資料來源改成協議抽象，並寫一個注入假資料的單元測試；③ 加一個"本月支出"桌面小工具。三件套做完，你的專案就有"正規軍"的樣子了。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 權限三步：Info.plist 宣告（漏了必崩）、用時申請、被拒引導去設定
- iOS 權限跳出視窗只彈一次：時機選在"正要用的那一刻"，文案寫清用途
- 通知三紀律：只發有用的、能關、不騷擾；UserNotifications 框架
- MVVM 進階：協議抽象（可測試）、單一職責、不過度設計
- 生態紅利：WidgetKit 小工具 + App Intents 快捷指令
- AI 輔助四場景：寫碼、查資料、寫測試、改 bug；方法論見第七篇（第37-47章）
:::
