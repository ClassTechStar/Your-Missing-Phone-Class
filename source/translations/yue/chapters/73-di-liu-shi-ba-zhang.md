---
id: di-liu-shi-ba-zhang
num: 68
part: ios-kai-fa-pian
nav: 第六十八章：進階之路——權限、通知與現代架構
toc: default
kind: chapter
---

### 第六十八章：進階之路——權限、通知同現代架構

{class="chapter-intro mb-4"}
做到 App 出嚟只係開始。呢一章傾吓由"識做"到"做好"嘅幾道坎：點樣優雅咁申請權限、點樣發通知唔惹人嬲、點樣將架構再抬高一層，仲有——喺 2026 年，點樣同 AI 拍檔寫 iOS 代碼。每一條都係你喺真實項目入面好快會遇到嘅。

#### 一、權限：先敲門，再入門

相機、定位、通訊錄、通知……呢啲"敏感地帶"，iOS 要求 App 喺用到嗰陣向用戶彈窗申請。規矩係"聲明 + 申請 + 優雅降級"三步：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 權限申請（以定位爲例）</span><span class="dots">···</span>
:::

```
// 1. Info.plist 入面聲明用途文案（不聲明直接崩潰！）
// Privacy - Location When In Use Usage Description: "用嚟查你所在城市嘅天氣"

// 2. 用嘅時候申請
import CoreLocation

@Observable
class LocationModel {
    private let manager = CLLocationManager()

    func request() {
        switch manager.authorizationStatus {
        case .notDetermined: manager.requestWhenInUseAuthorization()
        case .denied, .restricted: /* 引導去設定入面開 */
        default: /* 已授權，開搞 */
        }
    }
}

// 3. 被拒之後優雅降級：畀提示 + 跳去設定
// UIApplication.shared.open(URL(string: UIApplication.openSettingsURLString)!)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：iOS 權限嘅"一次性"

{class="mt-1"}
iOS 嘅權限彈窗只彈一次——用戶拒絕咗之後就唔會再彈。所以：申請嘅時機要揀喺"用戶就嚟要用嗰一刻"（而唔係一啟動就彈一堆），文案要講明用途。被拒之後嘅界面引導（"去設定入面開啟定位"）係標配，咪令用戶困喺死胡同入面。
:::

#### 二、通知：喺啱嘅時間講有用嘅嘢

通知係 App 接觸用戶嘅通道，亦都係最容易被用戶"封殺"嘅功能。iOS 用 UserNotifications 框架，發通知三條紀律：淨係發有用嘅、畀用戶閂得、咪半夜嘈住人。基礎用法：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 本地通知</span><span class="dots">···</span>
:::

```
import UserNotifications

// 1. 申請通知權限（彈一次窗）
UNUserNotificationCenter.current()
    .requestAuthorization(options: [.alert, .sound, .badge]) { granted, _ in
        print(granted ? "已授權" : "被拒絕")
    }

// 2. 安排一條"每日 20:00 記賬提醒"
func scheduleDailyReminder() {
    let content = UNMutableNotificationContent()
    content.title = "記賬提醒"
    content.body = "今日仲未記賬喎"
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

注意：iOS 嘅通知權限同樣"只彈一次"，而且用戶隨時可以喺系統設定入面閂咗佢——所以通知內容嘅價值感好重要，濫發一次可能就永遠失去用戶。

#### 三、架構進階：MVVM 深入同可測試性

第 65 章用過 MVVM，呢度補三個進階要點：

- 協議抽象：令 ViewModel 依賴協議（protocol）而唔係具體類——測試嗰陣可以注入"假數據源"，呢個係可測試性嘅基石；
- 單一職責：一個 ViewModel 淨係管一件事（記賬嘅唔會理天氣）；功能多咗就拆；
- 咪過度設計：單人小項目，"@Observable 類 + 協議抽象"就夠。VIPER、Clean Architecture 呢類重架構，等團隊同複雜度找上門先再講——工具係服務目標嘅，唔係用嚟炫耀嘅。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：SwiftUI 嘅"生態紅利"

{class="mt-1"}
iOS 生態仲有兩個"只此一家"嘅進階玩法：小組件（WidgetKit）令用戶唔使打開 App 都睇到資訊（記賬本嘅"本月支出"放桌面），快捷指令（App Intents）令用戶用 Siri 或者自動化調用你嘅功能。兩者都有官方框架，入門成本唔高，但對用戶體驗嘅加成好大——進階路上值得優先解鎖。
:::

#### 四、2026 年嘅新玩法：AI 輔助 iOS 開發

2026 年，AI 已經深度嵌入蘋果開發流程。如果你想提速，呢套組合拳好成熟：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">環節</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">AI 點樣幫</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">你嘅職責</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">寫代碼</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode 內置代碼補全 + 第三方 AI 插件生成</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">描述清楚需求，審查產出</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">查資料</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">將官方文檔同報錯資訊掟畀 AI 解讀</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">關鍵結論返去官方文檔核實</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">寫測試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">令 AI 按"正常／邊界／異常"三類生成 XCTest 用例</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">確認用例符合業務語義</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">改 bug</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">貼崩潰日誌 + 相關代碼，AI 定位修復</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">睇得明改動，行測試驗證</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
AI 輔助 iOS 開發嘅四個場景

具體方法論——點樣畀 AI 下指令、點樣驗收、點樣避坑——完整嘅 11 章內容喺本書第七篇《AI編程實戰篇》（第37-47章）入面，強烈建議配合閱讀：Swift 語法交畀本篇，AI 協作嘅心法交畀第七篇。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
嚟動手：畀記賬本加"三件套"

#### 五、Swift 並發要點：@MainActor 同 Task

Swift 6 嘅並發體系有兩條新手必識嘅規則：

- 界面只可以喺主線程更新：SwiftUI 視圖預設係 @MainActor，網絡回調返到主線程先改狀態（await MainActor.run { ... } 或者將 ViewModel 標成 @MainActor）；
- 異步任務用 Task 管理：.task { } 修飾符跟住視圖出現自動開始、消失自動取消——呢個係 SwiftUI 入面啟動異步工作嘅標準姿勢，咪喺 body 入面亂咁寫 Task 裸奔。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 標準異步姿勢</span><span class="dots">···</span>
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
        .task {                       // 出現就開始，消失就取消
            await vm.search(city: "北京")
        }
    }
}
```
:::

呢兩條規則背後係 Swift 6 嘅"數據競爭安全"設計——編譯器會喺你寫錯嗰陣直接報錯，而唔係等到 App 崩咗先發現。編譯器嘅報錯唔係同你搵碴，係替你擋子彈。

{class="mt-1"}
① 畀記賬本加"每日 20:00 記賬提醒"（通知權限 + 本地通知）；② 將 ViewModel 嘅數據源改成協議抽象，並寫一個注入假數據嘅單元測試；③ 加一個"本月支出"桌面小組件。三件套做完，你嘅項目就有"正規軍"嘅樣喇。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 權限三步：Info.plist 聲明（漏咗必崩）、用嗰陣申請、被拒引導去設定
- iOS 權限彈窗只彈一次：時機揀喺"就嚟要用嗰一刻"，文案寫清楚用途
- 通知三紀律：淨係發有用嘅、閂得、唔嘈住人；UserNotifications 框架
- MVVM 進階：協議抽象（可測試）、單一職責、唔過度設計
- 生態紅利：WidgetKit 小組件 + App Intents 快捷指令
- AI 輔助四場景：寫碼、查資料、寫測試、改 bug；方法論見第七篇（第37-47章）
:::
