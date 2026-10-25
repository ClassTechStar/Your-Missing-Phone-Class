---
id: di-liu-shi-si-zhang
num: 64
part: ios-kai-fa-pian
nav: 第六十四章：資料儲存與網路請求
toc: default
kind: chapter
---

### 第六十四章：資料儲存與網路請求

{class="chapter-intro mb-4"}
一個只能"看"的 App 是死的；能存資料、能連網路的 App 才是活的。這一章認識 iOS 資料層的"三件套"：UserDefaults（存小配置）、SwiftData（存結構化資料）、URLSession（和伺服器對話），外加解析 JSON 的 Codable 和現代化的 async/await。學完這章，你就能寫會記住使用者習慣、會實時更新內容的真 App 了。

#### 一、儲存方案怎麼選：先看這張表

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">方案</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">適合存什麼</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">特點</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">本書哪裡用</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">零散配置（開關、偏好）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">鍵值對，簡單直接</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 65 章設定、第 66 章收藏城市</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">結構化資料（賬目、記錄）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方資料庫封裝，@Model 一行宣告</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 65 章賬目記錄</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">（不存，聯網取）伺服器資料</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系統自帶網路框架，無第三方依賴</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 66 章天氣資料</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
資料三件套的分工

記一個口訣："小配置進 UserDefaults，成批資料進 SwiftData，外面的資料走 URLSession"。舊教學裡的 Core Data 依然能用（SwiftData 就是它的現代馬甲），手寫 SQLite 則基本不用碰——直接學新的，別走老路。

#### 二、UserDefaults：存點小配置

::: div .code-block
:::inline div .code-head
<span>SWIFT · UserDefaults 示例</span><span class="dots">···</span>
:::

```
// 寫：存一個值
UserDefaults.standard.set(true, forKey: "isDarkMode")
UserDefaults.standard.set("北京", forKey: "favoriteCity")

// 讀：取出來（沒有就返回預設值）
let isDark = UserDefaults.standard.bool(forKey: "isDarkMode")
let city = UserDefaults.standard.string(forKey: "favoriteCity") ?? "北京"

// 刪：移除一個鍵
UserDefaults.standard.removeObject(forKey: "isDarkMode")
```
:::

注意它只適合零散的小配置——幾十上百條記錄請交給 SwiftData，別把 UserDefaults 當資料庫用（會拖慢啟動、也不便查詢）。

#### 三、SwiftData：給資料安個"真正的家"

SwiftData 是 iOS 17 起的官方資料庫方案，把"建表、增刪改查"簡化到了極致——一個 @Model 註解，資料類就變成資料庫表：

::: div .code-block
:::inline div .code-head
<span>SWIFT · SwiftData 示例</span><span class="dots">···</span>
:::

```
import SwiftData

// 1. @Model：這個類自動變成"表"
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

// 2. App 入口掛上容器
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: Record.self)   // 資料庫就緒
    }
}

// 3. 檢視裡用 @Query 讀、@Environment 寫
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

這套"@Model + modelContainer + @Query"模板可以原樣搬進你的任何專案——換換欄位名就行。資料一變，@Query 自動重新整理介面，妙不可言。

#### 四、Codable：給 JSON"翻譯"

伺服器的資料大多是 JSON 文字。Swift 的 Codable 協議讓"JSON ⇄ 結構體"的轉換自動發生——欄位名對得上，魔法就生效：

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

鐵律：先看真實返回的 JSON，再定義欄位。很多"解析失敗"的 bug 都是欄位名寫錯、型別猜錯（伺服器發 "26.5" 字串，你宣告成 Double）——把原始 JSON 列印出來對照，十秒定位。

#### 五、URLSession + async/await：和伺服器說話

iOS 聯網用系統自帶的 URLSession，配合 Swift 的 async/await（非同步函式），"等網路"就像"等快遞"一樣自然：

::: div .code-block
:::inline div .code-head
<span>SWIFT · URLSession + async/await</span><span class="dots">···</span>
:::

```
struct WeatherService {
    // 非同步函式：async 標記"我要等一會兒"，throws 標記"可能失敗"
    func fetchWeather(city: String) async throws -> WeatherResponse {
        let url = URL(string:
            "https://api.example.com/weather?city=\(city)")!
        let (data, _) = try await URLSession.shared.data(from: url)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}

// 呼叫處（在 .task 裡）：
.task {
    do {
        let weather = try await service.fetchWeather(city: "北京")
        // 更新介面……
    } catch {
        print("出錯了：\(error)")
    }
}
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
避坑提醒：兩條網路鐵律

{class="mt-1"}
① 聯網必須 async/await，絕不阻塞主執行緒——卡住介面是崩潰級體驗。Swift 的結構化併發讓這變得很自然，但別忘了 try await 和 do/catch。② ATS 預設禁止明文 HTTP：iOS 要求 HTTPS。測試本地 http:// 服務時需要在 Info.plist 裡臨時開例外（NSAppTransportSecurity），但正式產品必須全走 HTTPS——稽核也會盯這個。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：做一個"每日一句"小應用

#### 六、網路錯誤也要"分級"：別把一切報錯都丟給使用者

斷網、超時、404、伺服器 500……不同的錯，使用者該看到的話不一樣：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 錯誤分級處理</span><span class="dots">···</span>
:::

```
func friendlyMessage(_ error: Error) -> String {
    if let urlError = error as? URLError {
        switch urlError.code {
        case .notConnectedToInternet: return "網路斷了，檢查一下連線？"
        case .timedOut:               return "請求超時，稍後再試？"
        case .cannotFindHost:         return "伺服器找不到了"
        default:                      return "網路出問題了：\(urlError.code)"
        }
    }
    if let d = error as? DecodingError {
        return "資料格式不對（可能是介面變了）"
    }
    return "出錯了：\(error.localizedDescription)"
}
```
:::

給使用者看"人話"，給日誌看"原話"（print 完整 error）。別把 error.localizedDescription 的英文天書直接甩給使用者——產品感就藏在這些細節裡。

{class="mt-1"}
找一個免費的名言 API（比如 hitokoto 之類），用 URLSession + async/await 拉取"每日一句"，顯示在螢幕中央，加個"換一句"按鈕。再把喜歡的句子用 SwiftData 存進"收藏夾"。這個練習把 UserDefaults/SwiftData/Codable/URLSession 全用了一遍——做完它，第 7、8 章就是小菜一碟。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 口訣：小配置進 UserDefaults，成批資料進 SwiftData，外面的資料走 URLSession
- SwiftData 三板斧：@Model 宣告表、modelContainer 掛容器、@Query 讀 + context.insert 寫
- Codable 自動"翻譯" JSON：欄位對得上，魔法就生效
- URLSession + async/await：聯網像等快遞；do/catch 處理失敗
- 兩條鐵律：不阻塞主執行緒；正式產品必須 HTTPS（ATS）
:::
