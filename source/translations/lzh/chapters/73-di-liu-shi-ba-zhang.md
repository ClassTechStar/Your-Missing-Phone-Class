---
id: di-liu-shi-ba-zhang
num: 68
part: ios-kai-fa-pian
nav: 第六十八章：進階之路——權限、通知與現代架構
toc: default
kind: chapter
---

### 第六十八章：進階之途——權限、通知與現代構架

{class="chapter-intro mb-4"}
能作 App，特其始耳。此章談自「能作」至「作善」之數關：何以雅而請權限、何以發通知而不厭於人、何以舉構架再上一層，及——2026 年，何以與 AI 相偶而書 iOS 之碼。凡此皆汝於真項中即將遇者。

#### 一、權限：先叩門，後入門

相機、定位、通訊錄、通知……此等「敏感之域」，iOS 責 App 於用時向用戶彈窗而請。其規為「聲明 + 請求 + 雅而降級」三步：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 權限申請（以定位爲例）</span><span class="dots">···</span>
:::

```
// 1. Info.plist 中聲明用途之文（不聲明則立崩！）
// Privacy - Location When In Use Usage Description: "以查汝所於之城天氣"

// 2. 用時申請
import CoreLocation

@Observable
class LocationModel {
    private let manager = CLLocationManager()

    func request() {
        switch manager.authorizationStatus {
        case .notDetermined: manager.requestWhenInUseAuthorization()
        case .denied, .restricted: /* 引導至設定中開之 */
        default: /* 已授權，可行矣 */
        }
    }
}

// 3. 被拒則優雅降級：予提示 + 跳設定
// UIApplication.shared.open(URL(string: UIApplication.openSettingsURLString)!)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
按：iOS 權限之「一次性」

{class="mt-1"}
iOS 權限之窗惟彈一過——用戶拒之則不復彈。故請之時，當擇「用戶方欲用之頃」（非一啟而彈一堆），文當明其用。見拒後界面之引（「往設置中啟定位」）乃標配，勿使用戶困於窮巷。
:::

#### 二、通知：於當時而言有用之言

通知者，App 達用戶之途也，亦最易為用戶所「拒」之能。iOS 用 UserNotifications 之框，發通知有三戒：惟發有用者、使戶能關、勿半夜擾之。其基法：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 本地通知</span><span class="dots">···</span>
:::

```
import UserNotifications

// 1. 申請通知之權（彈窗一次）
UNUserNotificationCenter.current()
    .requestAuthorization(options: [.alert, .sound, .badge]) { granted, _ in
        print(granted ? "已授權" : "被拒絕")
    }

// 2. 安排一條"每日 20:00 記賬之提醒"
func scheduleDailyReminder() {
    let content = UNMutableNotificationContent()
    content.title = "記賬提醒"
    content.body = "今日尚未記賬也"
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

按：iOS 通知之權同「惟彈一過」，且用戶隨時可於系統設置中關之——故通知內容之價值甚要，濫發一過，或永失其戶。

#### 三、構架進階：MVVM 之深與可測之性

第 65 章已用 MVVM，此補三進階之要：

- 協議之抽象：使 ViewModel 倚協議（protocol）而非具體之類——測時可注「假數據之源」，此可測性之基石也；
- 一職之守：一 ViewModel 惟司一事（記賬者不問天氣）；能多則拆之；
- 勿過度設計：一人小項，「@Observable 類 + 協議抽象」足矣。VIPER、Clean Architecture 之重構，待團隊與繁難自來而後議——器者所以務其的，非以炫也。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：SwiftUI 之「生態紅利」

{class="mt-1"}
iOS 生態尚有二「獨此一家」之進階玩法：小組件（WidgetKit）使用戶不啟 App 而能觀信息（記賬本「本月支出」置於桌面），快捷之令（App Intents）使用戶以 Siri 或自動化調汝之能。二者皆有官方之框，入門之費不昂，而於用戶體驗之增益至巨——進階之途宜先解之。
:::

#### 四、2026 年之新法：AI 輔 iOS 之開發

2026 年，AI 已深嵌蘋果開發之程。汝欲提速，此組合之拳甚熟：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">環節</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">AI 何以助</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">汝之職</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">書碼</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode 內置碼之補全 + 第三方 AI 插件以生之</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">明述所需，察其所產</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">查料</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">以官方之檔與報錯之訊擲 AI 而解之</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">關鍵之結回官方之檔核之</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">書測試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">使 AI 按「常/邊/異」三類生 XCTest 之用例</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">核用例合於業之義</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">改 bug</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">貼崩潰之日誌 + 相關之碼，AI 定其位而修之</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">讀懂其改，行測試以驗</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
AI 輔 iOS 開發之四境

其具體之法——何以予 AI 指令、何以驗收、何以避坑——全十一章之文，在本書第七篇《AI編程實戰篇》（第37-47章），力勸參而讀之：Swift 之語法付本篇，AI 協作之心法付第七篇。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：為記賬本增「三件」

#### 五、Swift 並發之要：@MainActor 與 Task

Swift 6 並發之制有二規，新手必曉：

- 界面惟可於主線程更之：SwiftUI 視圖默為 @MainActor，網絡回呼返主線程而後改態（await MainActor.run { ... } 或標 ViewModel 為 @MainActor）；
- 異步之務以 Task 管之：.task { } 修飾符隨視圖現而自始、沒而自罷——此 SwiftUI 啟異動之正姿也，勿於 body 中妄書 Task 而裸行。

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
        .task {                       // 現即始，隱即止
            await vm.search(city: "北京")
        }
    }
}
```
:::

此二規之後，乃 Swift 6「數據競爭安全」之設——編譯器於汝書誤時即報，非待 App 崩而後覺。編譯器之報，非摘瑕也，乃代汝擋彈也。

{class="mt-1"}
① 為記賬本增「每日 20:00 記賬之提醒」（通知之權 + 本地通知）；② 易 ViewModel 數據之源為協議之抽象，且書一注假數據之單元測試；③ 增「本月支出」桌面小組件。三件既成，汝之項乃有「正軍」之觀矣。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小結

- 權限三步：Info.plist 聲明（漏則必崩）、用時而請、見拒則引往設置
- iOS 權限之窗惟彈一過：時擇「方欲用之頃」，文明其用
- 通知三戒：惟發有用者、能關、不擾；UserNotifications 之框
- MVVM 進階：協議之抽象（可測）、一職之守、勿過度設計
- 生態紅利：WidgetKit 小組件 + App Intents 快捷之令
- AI 輔四境：書碼、查料、書測試、改 bug；法見第七篇（第37-47章）
:::
