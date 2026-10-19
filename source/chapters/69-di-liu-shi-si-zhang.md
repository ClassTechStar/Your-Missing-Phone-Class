---
id: di-liu-shi-si-zhang
num: 64
part: ios-kai-fa-pian
nav: 第六十四章：数据存储与网络请求
toc: default
kind: chapter
---

### 第六十四章：数据存储与网络请求

{class="chapter-intro mb-4"}
一个只能"看"的 App 是死的；能存数据、能连网络的 App 才是活的。这一章认识 iOS 数据层的"三件套"：UserDefaults（存小配置）、SwiftData（存结构化数据）、URLSession（和服务器对话），外加解析 JSON 的 Codable 和现代化的 async/await。学完这章，你就能写会记住用户习惯、会实时更新内容的真 App 了。

#### 一、存储方案怎么选：先看这张表

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">方案</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">适合存什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">特点</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">本书哪里用</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">零散配置（开关、偏好）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">键值对，简单直接</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 65 章设置、第 66 章收藏城市</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">结构化数据（账目、记录）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方数据库封装，@Model 一行声明</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 65 章账目记录</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">（不存，联网取）服务器数据</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系统自带网络框架，无第三方依赖</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 66 章天气数据</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
数据三件套的分工

记一个口诀：<strong>"小配置进 UserDefaults，成批数据进 SwiftData，外面的数据走 URLSession"</strong>。旧教程里的 Core Data 依然能用（SwiftData 就是它的现代马甲），手写 SQLite 则基本不用碰——直接学新的，别走老路。

#### 二、UserDefaults：存点小配置

::: div .code-block
:::inline div .code-head
<span>SWIFT · UserDefaults 示例</span><span class="dots">···</span>
:::

```
// 写：存一个值
UserDefaults.standard.set(true, forKey: "isDarkMode")
UserDefaults.standard.set("北京", forKey: "favoriteCity")

// 读：取出来（没有就返回默认值）
let isDark = UserDefaults.standard.bool(forKey: "isDarkMode")
let city = UserDefaults.standard.string(forKey: "favoriteCity") ?? "北京"

// 删：移除一个键
UserDefaults.standard.removeObject(forKey: "isDarkMode")
```
:::

注意它只适合<strong>零散的小配置</strong>——几十上百条记录请交给 SwiftData，别把 UserDefaults 当数据库用（会拖慢启动、也不便查询）。

#### 三、SwiftData：给数据安个"真正的家"

SwiftData 是 iOS 17 起的官方数据库方案，把"建表、增删改查"简化到了极致——<strong>一个 @Model 注解，数据类就变成数据库表</strong>：

::: div .code-block
:::inline div .code-head
<span>SWIFT · SwiftData 示例</span><span class="dots">···</span>
:::

```
import SwiftData

// 1. @Model：这个类自动变成"表"
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

// 2. App 入口挂上容器
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: Record.self)   // 数据库就绪
    }
}

// 3. 视图里用 @Query 读、@Environment 写
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
        try? context.save()   // 落盘
    }
}
```
:::

这套"@Model + modelContainer + @Query"模板可以原样搬进你的任何项目——换换字段名就行。数据一变，@Query 自动刷新界面，妙不可言。

#### 四、Codable：给 JSON"翻译"

服务器的数据大多是 JSON 文本。Swift 的 <strong>Codable</strong> 协议让"JSON ⇄ 结构体"的转换自动发生——字段名对得上，魔法就生效：

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

// JSON 字符串 → 结构体
let decoder = JSONDecoder()
let data = jsonString.data(using: .utf8)!
let result = try decoder.decode(WeatherResponse.self, from: data)
print(result.weather[0].description)   // "晴"
```
:::

铁律：<strong>先看真实返回的 JSON，再定义字段</strong>。很多"解析失败"的 bug 都是字段名写错、类型猜错（服务器发 "26.5" 字符串，你声明成 Double）——把原始 JSON 打印出来对照，十秒定位。

#### 五、URLSession + async/await：和服务器说话

iOS 联网用系统自带的 <strong>URLSession</strong>，配合 Swift 的 <strong>async/await</strong>（异步函数），"等网络"就像"等快递"一样自然：

::: div .code-block
:::inline div .code-head
<span>SWIFT · URLSession + async/await</span><span class="dots">···</span>
:::

```
struct WeatherService {
    // 异步函数：async 标记"我要等一会儿"，throws 标记"可能失败"
    func fetchWeather(city: String) async throws -> WeatherResponse {
        let url = URL(string:
            "https://api.example.com/weather?city=\(city)")!
        let (data, _) = try await URLSession.shared.data(from: url)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}

// 调用处（在 .task 里）：
.task {
    do {
        let weather = try await service.fetchWeather(city: "北京")
        // 更新界面……
    } catch {
        print("出错了：\(error)")
    }
}
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>避坑提醒：两条网络铁律

{class="mt-1"}
① <strong>联网必须 async/await，绝不阻塞主线程</strong>——卡住界面是崩溃级体验。Swift 的结构化并发让这变得很自然，但别忘了 <code class="inline">try await</code> 和 <code class="inline">do/catch</code>。② <strong>ATS 默认禁止明文 HTTP</strong>：iOS 要求 HTTPS。测试本地 http:// 服务时需要在 Info.plist 里临时开例外（NSAppTransportSecurity），但正式产品必须全走 HTTPS——审核也会盯这个。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：做一个"每日一句"小应用

#### 六、网络错误也要"分级"：别把一切报错都丢给用户

断网、超时、404、服务器 500……不同的错，用户该看到的话不一样：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 错误分级处理</span><span class="dots">···</span>
:::

```
func friendlyMessage(_ error: Error) -> String {
    if let urlError = error as? URLError {
        switch urlError.code {
        case .notConnectedToInternet: return "网络断了，检查一下连接？"
        case .timedOut:               return "请求超时，稍后再试？"
        case .cannotFindHost:         return "服务器找不到了"
        default:                      return "网络出问题了：\(urlError.code)"
        }
    }
    if let d = error as? DecodingError {
        return "数据格式不对（可能是接口变了）"
    }
    return "出错了：\(error.localizedDescription)"
}
```
:::

给用户看"人话"，给日志看"原话"（print 完整 error）。别把 <code class="inline">error.localizedDescription</code> 的英文天书直接甩给用户——产品感就藏在这些细节里。

{class="mt-1"}
找一个免费的名言 API（比如 hitokoto 之类），用 URLSession + async/await 拉取"每日一句"，显示在屏幕中央，加个"换一句"按钮。再把喜欢的句子用 SwiftData 存进"收藏夹"。这个练习把 UserDefaults/SwiftData/Codable/URLSession 全用了一遍——做完它，第 7、8 章就是小菜一碟。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 口诀：小配置进 UserDefaults，成批数据进 SwiftData，外面的数据走 URLSession
- SwiftData 三板斧：@Model 声明表、modelContainer 挂容器、@Query 读 + context.insert 写
- Codable 自动"翻译" JSON：字段对得上，魔法就生效
- URLSession + async/await：联网像等快递；do/catch 处理失败
- 两条铁律：不阻塞主线程；正式产品必须 HTTPS（ATS）
:::
