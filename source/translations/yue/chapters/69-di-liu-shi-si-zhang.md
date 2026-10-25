---
id: di-liu-shi-si-zhang
num: 64
part: ios-kai-fa-pian
nav: 第六十四章：數據儲存與網絡請求
toc: default
kind: chapter
---

### 第六十四章：數據存儲同網絡請求

{class="chapter-intro mb-4"}
一個淨係得"睇"嘅 App 係死嘅；識存數據、識連網絡嘅 App 先至係生嘅。呢一章認識 iOS 數據層嘅"三件套"：UserDefaults（存小配置）、SwiftData（存結構化數據）、URLSession（同伺服器對話），仲有解析 JSON 嘅 Codable 同現代化嘅 async/await。學完呢章，你就可以寫到識記住用戶習慣、識實時更新內容嘅真 App 喇。

#### 一、存儲方案點樣揀：先睇呢張表

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">方案</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">適合存乜嘢</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">特點</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">本書邊度用</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">零散配置（開關、偏好）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">鍵值對，簡單直接</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 65 章設定、第 66 章收藏城市</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">結構化數據（賬目、記錄）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方數據庫封裝，@Model 一行聲明</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 65 章賬目記錄</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">（唔存，上網攞）伺服器數據</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系統自帶網絡框架，冇第三方依賴</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 66 章天氣數據</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
數據三件套嘅分工

記一個口訣："小配置入 UserDefaults，成批數據入 SwiftData，出面嘅數據行 URLSession"。舊教程入面嘅 Core Data 依然用得（SwiftData 就係佢嘅現代馬甲），手寫 SQLite 就基本唔使掂——直接學新嘅，咪行舊路。

#### 二、UserDefaults：存啲小配置

::: div .code-block
:::inline div .code-head
<span>SWIFT · UserDefaults 示例</span><span class="dots">···</span>
:::

```
// 寫：存一個值
UserDefaults.standard.set(true, forKey: "isDarkMode")
UserDefaults.standard.set("北京", forKey: "favoriteCity")

// 讀：取出來（冇就返回預設值）
let isDark = UserDefaults.standard.bool(forKey: "isDarkMode")
let city = UserDefaults.standard.string(forKey: "favoriteCity") ?? "北京"

// 刪：移除一個鍵
UserDefaults.standard.removeObject(forKey: "isDarkMode")
```
:::

注意佢只係適合零散嘅小配置——幾十上百條記錄請交畀 SwiftData，唔好將 UserDefaults 當數據庫咁用（會拖慢啟動、亦都唔方便查詢）。

#### 三、SwiftData：畀數據安個"真正嘅屋企"

SwiftData 係 iOS 17 開始嘅官方數據庫方案，將"建表、增刪改查"簡化到極致——一個 @Model 註解，數據類就變成數據庫表：

::: div .code-block
:::inline div .code-head
<span>SWIFT · SwiftData 示例</span><span class="dots">···</span>
:::

```
import SwiftData

// 1. @Model：呢個類自動變成"表"
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
        .modelContainer(for: Record.self)   // 數據庫就緒
    }
}

// 3. 視圖入面用 @Query 讀、@Environment 寫
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

呢套"@Model + modelContainer + @Query"模板可以原封不動搬入你任何項目——換下字段名就得。數據一變，@Query 自動刷新界面，妙不可言。

#### 四、Codable：畀 JSON"翻譯"

伺服器嘅數據大多係 JSON 文本。Swift 嘅 Codable 協議令"JSON ⇄ 結構體"嘅轉換自動發生——字段名對得上，魔法就生效：

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

鐵律：先睇真實返回嘅 JSON，再定義字段。好多"解析失敗"嘅 bug 都係字段名寫錯、類型估錯（伺服器發 "26.5" 字串，你聲明成 Double）——將原始 JSON 打印出嚟對照，十秒定位。

#### 五、URLSession + async/await：同伺服器講嘢

iOS 上網用系統自帶嘅 URLSession，配合 Swift 嘅 async/await（異步函數），"等網絡"就好似"等快遞"咁自然：

::: div .code-block
:::inline div .code-head
<span>SWIFT · URLSession + async/await</span><span class="dots">···</span>
:::

```
struct WeatherService {
    // 異步函數：async 標記"我要等一陣"，throws 標記"可能失敗"
    func fetchWeather(city: String) async throws -> WeatherResponse {
        let url = URL(string:
            "https://api.example.com/weather?city=\(city)")!
        let (data, _) = try await URLSession.shared.data(from: url)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}

// 調用處（喺 .task 入面）：
.task {
    do {
        let weather = try await service.fetchWeather(city: "北京")
        // 更新界面……
    } catch {
        print("出咗錯：\(error)")
    }
}
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
避坑提醒：兩條網絡鐵律

{class="mt-1"}
① 上網必須 async/await，絕不阻塞主線程——卡住界面係崩潰級體驗。Swift 嘅結構化並發令呢樣嘢變得好自然，但唔好唔記得 try await 同 do/catch。② ATS 預設禁止明文 HTTP：iOS 要求 HTTPS。測試本地 http:// 服務嗰陣需要喺 Info.plist 入面臨時開例外（NSAppTransportSecurity），但正式產品必須全部行 HTTPS——審核都會盯住呢樣。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
嚟動手：做一個"每日一句"小應用

#### 六、網絡錯誤都要"分級"：唔好將所有報錯都掟畀用戶

斷網、超時、404、伺服器 500……唔同嘅錯，用戶應該睇到嘅訊息都唔同：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 錯誤分級處理</span><span class="dots">···</span>
:::

```
func friendlyMessage(_ error: Error) -> String {
    if let urlError = error as? URLError {
        switch urlError.code {
        case .notConnectedToInternet: return "網絡斷咗，檢查吓連接？"
        case .timedOut:               return "請求超時，遲啲再試？"
        case .cannotFindHost:         return "伺服器搵不到咗"
        default:                      return "網絡出咗問題：\(urlError.code)"
        }
    }
    if let d = error as? DecodingError {
        return "數據格式唔啱（可能係接口變咗）"
    }
    return "出咗錯：\(error.localizedDescription)"
}
```
:::

畀用戶睇"人話"，畀日誌睇"原話"（print 完整 error）。唔好將 error.localizedDescription 嘅英文天書直接掟畀用戶——產品感就藏喺呢啲細節入面。

{class="mt-1"}
搵一個免費嘅名言 API（譬如 hitokoto 呢類），用 URLSession + async/await 拉取"每日一句"，顯示喺螢幕中央，加個"換一句"按鈕。再將鍾意嘅句子用 SwiftData 存入"收藏夾"。呢個練習將 UserDefaults/SwiftData/Codable/URLSession 全部用咗一次——做完佢，第 7、8 章就係小菜一碟。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 口訣：小配置入 UserDefaults，成批數據入 SwiftData，出面嘅數據行 URLSession
- SwiftData 三板斧：@Model 聲明表、modelContainer 掛容器、@Query 讀 + context.insert 寫
- Codable 自動"翻譯" JSON：字段對得上，魔法就生效
- URLSession + async/await：上網好似等快遞；do/catch 處理失敗
- 兩條鐵律：唔阻塞主線程；正式產品必須 HTTPS（ATS）
:::
