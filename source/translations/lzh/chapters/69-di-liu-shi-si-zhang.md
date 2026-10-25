---
id: di-liu-shi-si-zhang
num: 64
part: ios-kai-fa-pian
nav: 第六十四章：數據存儲與網絡請求
toc: default
kind: chapter
---

### 第六十四章：數據存貯與網絡之請

{class="chapter-intro mb-4"}
惟「觀」而不能他為之 App，死物也；能存數據、能連網絡者，方為活物。此章識 iOS 數據層之「三件」：UserDefaults（貯小配置）、SwiftData（貯結構化數據）、URLSession（與伺服器言），外加解 JSON 之 Codable 與現代之 async/await。學畢此章，則能作能記用戶之習、能實時更其內容之真 App 矣。

#### 一、存貯之方何以擇：先觀此表

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">方案</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">宜貯何物</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">特點</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">本書何處用之</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">零散配置（開關、偏好）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">鍵值之對，簡而直</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 65 章設置、第 66 章所藏之城</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">結構化數據（賬目、記錄）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方數據庫之封裝，@Model 一行而聲明</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 65 章賬目之記錄</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">（不貯，連網而取）伺服器數據</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系統自帶網絡之框，無第三方之倚</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 66 章天氣數據</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
數據三件之分工

記一口訣：「小配置入 UserDefaults，成批數據入 SwiftData，外來數據行 URLSession」。舊籍之 Core Data 猶可用（SwiftData 即其今之馬甲），手書 SQLite 則大抵不須觸——徑學其新，勿履舊轍。

#### 二、UserDefaults：貯些小配置

::: div .code-block
:::inline div .code-head
<span>SWIFT · UserDefaults 示例</span><span class="dots">···</span>
:::

```
// 寫：存一個值
UserDefaults.standard.set(true, forKey: "isDarkMode")
UserDefaults.standard.set("北京", forKey: "favoriteCity")

// 讀：取之（無則返默認值）
let isDark = UserDefaults.standard.bool(forKey: "isDarkMode")
let city = UserDefaults.standard.string(forKey: "favoriteCity") ?? "北京"

// 刪：移除一個鍵
UserDefaults.standard.removeObject(forKey: "isDarkMode")
```
:::

惟其僅宜零散之小配置——數十上百之記錄請付 SwiftData，勿以 UserDefaults 為數據庫而用（將緩啟動、且不便查詢）。

#### 三、SwiftData：為數據安「真家」

SwiftData 者，iOS 17 以降官方數據庫之方也，使「建表、增刪改查」簡至其極——一 @Model 之註，數據類遂為數據庫之表：

::: div .code-block
:::inline div .code-head
<span>SWIFT · SwiftData 示例</span><span class="dots">···</span>
:::

```
import SwiftData

// 1. @Model：此類自化為"表"
@Model
class Record {
    var amount: Double
    var category: String
    var note: String
    var date: Date

    init(amount: Double, category: String, note: String, date: Date) {
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date
    }
}

// 2. App 入口掛容器
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: Record.self)   // 數據庫就緒
    }
}

// 3. 視圖中用 @Query 讀、@Environment 寫
struct RecordListView: View {
    @Query(sort: \Record.date, order: .reverse) var records: [Record]
    @Environment(\.modelContext) private var context

    var body: some View {
        List(records) { r in
            Text("\(r.category) \(r.amount) 元")
        }
    }

    func add(amount: Double, category: String) {
        let r = Record(amount: amount, category: category, note: "", date: Date())
        context.insert(r)     // 存
        try? context.save()   // 落盤
    }
}
```
:::

此「@Model + modelContainer + @Query」之模板，可原式移入汝任何之項——易其字段之名即可。數據一變，@Query 自刷界面，妙不可言。

#### 四、Codable：為 JSON「譯」

伺服器之數多為 JSON 之文。Swift 之 Codable 協議，使「JSON ⇄ 結構體」之轉換自發——字段名相合，魔法即效：

::: div .code-block
:::inline div .code-head
<span>SWIFT · Codable 解析 JSON</span><span class="dots">···</span>
:::

```
// JSON: {"name":"北京","main":{"temp":26.5},"weather":[{"description":"晴"}]}
struct WeatherResponse: Codable {
    let name: String
    let main: Main
    let weather: [Weather]
}
struct Main: Codable { let temp: Double }
struct Weather: Codable { let description: String }

// JSON 字串 → 結構體
let decoder = JSONDecoder()
let data = jsonString.data(using: .utf8)!
let result = try decoder.decode(WeatherResponse.self, from: data)
print(result.weather[0].description)   // "晴"
```
:::

鐵律：先觀實返之 JSON，後定字段。多「解析不遂」之 bug，皆字段名書誤、類型猜誤（伺服器發 "26.5" 之字串，汝聲為 Double）——印原 JSON 相對照，十秒可定。

#### 五、URLSession + async/await：與伺服器言

iOS 連網用系統自帶之 URLSession，合 Swift 之 async/await（異步之函），「候網」如「候速遞」之自然：

::: div .code-block
:::inline div .code-head
<span>SWIFT · URLSession + async/await</span><span class="dots">···</span>
:::

```
struct WeatherService {
    // 異步函數：async 標記"我要等一會兒"，throws 標記"可能失敗"
    func fetchWeather(city: String) async throws -> WeatherResponse {
        let url = URL(string:
            "https://api.example.com/weather?city=\(city)")!
        let (data, _) = try await URLSession.shared.data(from: url)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}

// 調用之處（於 .task 中）：
.task {
    do {
        let weather = try await service.fetchWeather(city: "北京")
        // 更新界面……
    } catch {
        print("有誤：\(error)")
    }
}
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
避坑之警：網絡二鐵律

{class="mt-1"}
① 連網必 async/await，絕不阻主線程——界面滯塞，崩潰級之驗也。Swift 結構化之並發使之自然，然勿忘 try await 與 do/catch。② ATS 默禁明文 HTTP：iOS 責以 HTTPS。試本地 http:// 之服時，須於 Info.plist 暫開例外（NSAppTransportSecurity），然正式之品必全行 HTTPS——審核亦監此。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：作一「每日一句」小應用

#### 六、網絡之誤亦宜「分級」：勿以凡咎盡擲於用戶

斷網、逾時、404、伺服器 500……咎各不同，用戶所當見之言亦異：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 錯誤分級處理</span><span class="dots">···</span>
:::

```
func friendlyMessage(_ error: Error) -> String {
    if let urlError = error as? URLError {
        switch urlError.code {
        case .notConnectedToInternet: return "網絡斷矣，試查連接？"
        case .timedOut:               return "請求逾時，稍後再試？"
        case .cannotFindHost:         return "尋不見服務器"
        default:                      return "網絡有疾：\(urlError.code)"
        }
    }
    if let d = error as? DecodingError {
        return "數據之式有誤（或接口已變）"
    }
    return "有誤：\(error.localizedDescription)"
}
```
:::

予用戶以「人言」，予日誌以「原言」（print 完整 error）。勿以 error.localizedDescription 之英文天書直擲於用戶——產品之感，正藏於此等細節。

{class="mt-1"}
覓一免費名言之 API（如 hitokoto 之屬），以 URLSession + async/await 取「每日一句」，陳於屏心，加「換一句」之鈕。復以 SwiftData 貯所愛之句於「收藏之夾」。此習遍用 UserDefaults/SwiftData/Codable/URLSession——成之，則第 7、8 章直小菜一碟耳。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小結

- 口訣：小配置入 UserDefaults，成批數據入 SwiftData，外來數據行 URLSession
- SwiftData 三斧：@Model 聲其表、modelContainer 掛其器、@Query 讀而 context.insert 寫
- Codable 自「譯」JSON：字段相合，魔法即效
- URLSession + async/await：連網如候速遞；do/catch 處其不遂
- 二鐵律：不阻主線程；正式之品必 HTTPS（ATS）
:::
