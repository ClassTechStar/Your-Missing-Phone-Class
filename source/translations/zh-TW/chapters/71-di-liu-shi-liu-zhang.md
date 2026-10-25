---
id: di-liu-shi-liu-zhang
num: 66
part: ios-kai-fa-pian
nav: 第六十六章：專案二——天氣查詢App（網路版）
toc: default
kind: chapter
---

### 第六十六章：專案二——天氣查詢 App（網路版）

{class="chapter-intro mb-4"}
記帳本是"練內功"，天氣 App 是"見世面"——它要和網際網路打交道。這個專案你會學到：申請免費 API、解析 JSON、處理"載入中/成功/失敗"三種介面狀態，以及怎麼把 API 金鑰藏好。做完它，你就具備了做任何"聯網 App"的能力——新聞、匯率、翻譯，套路一模一樣。

#### 一、申請免費天氣 API

個人練手，推薦 OpenWeatherMap 或國內的 和風天氣（QWeather）——都有免費額度，註冊即用。以 OpenWeatherMap 為例：

1. 註冊帳號 → 在 API keys 頁面生成一個 Key（apikey）；
2. 免費版可呼叫 Current Weather 介面：api.openweathermap.org/data/2.5/weather? q=beijing&appid=你的Key&units=metric；
3. 瀏覽器裡先試一次，看看返回的 JSON 長什麼樣——這是接任何 API 前必做的"預習"。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
避坑提醒：金鑰絕不能寫死在程式碼裡

{class="mt-1"}
API Key 相當於你的"錢包密碼"，寫進程式碼一提交到 GitHub，幾小時內就會被爬蟲掃走盜刷。iOS 的正確做法：放進 Config.xcconfig（配置檔案，已被 gitignore 忽略），透過 Info.plist 讀入程式碼。搜尋"iOS xcconfig 管理金鑰"照著改即可。
:::

#### 二、網路層：URLSession + Codable

先照 API 返回的 JSON 定義模型，再寫服務：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 資料模型 + 服務</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"晴"}],"main":{"temp":26.5,"humidity":40},"name":"北京"}
struct WeatherResponse: Codable {
    let weather: [Weather]
    let main: Main
    let name: String
}
struct Weather: Codable { let description: String }
struct Main: Codable { let temp: Double; let humidity: Int }

struct WeatherService {
    let key: String   // 從 xcconfig 讀入

    func fetchWeather(city: String) async throws -> WeatherResponse {
        var comps = URLComponents(string: "https://api.openweathermap.org/data/2.5/weather")!
        comps.queryItems = [
            URLQueryItem(name: "q", value: city),
            URLQueryItem(name: "appid", value: key),
            URLQueryItem(name: "units", value: "metric"),
            URLQueryItem(name: "lang", value: "zh_cn")
        ]
        let (data, _) = try await URLSession.shared.data(from: comps.url!)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}
```
:::

#### 三、三種介面狀態：載入中 / 成功 / 失敗

聯網 App 的靈魂在於"狀態管理"。網路慢、斷網、城市名打錯……每種情況介面都要給使用者交代。用列舉 + switch 優雅地表示：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 介面狀態</span><span class="dots">···</span>
:::

```
enum LoadState {
    case loading                  // 轉圈中
    case success(WeatherResponse) // 成功
    case error(String)            // 失敗
}

@Observable
class WeatherViewModel {
    var state: LoadState = .loading
    private let service = WeatherService(key: Config.apiKey)

    func search(city: String) async {
        state = .loading
        do {
            let data = try await service.fetchWeather(city: city)
            state = .success(data)
        } catch {
            state = .error("查不到這個城市，換個名字試試？")
        }
    }
}

// 介面裡：
switch vm.state {
case .loading: ProgressView("載入中…")
case .success(let d): WeatherContent(data: d)
case .error(let msg): Text(msg).foregroundColor(.secondary)
}
```
:::

這個 loading/success/error 三段式是聯網介面的"萬金油模板"，先背下來，以後所有聯網 App 照葫蘆畫瓢。

#### 四、實戰介面程式碼：把天氣畫出來

::: div .code-block
:::inline div .code-head
<span>SWIFT · 天氣介面（核心片段）</span><span class="dots">···</span>
:::

```
struct WeatherContent: View {
    let data: WeatherResponse

    var body: some View {
        VStack(spacing: 12) {
            Text(data.name)
                .font(.title.bold())
            Text("\(Int(data.main.temp))°C")
                .font(.system(size: 76, weight: .thin))
            Text(data.weather.first?.description ?? "未知")
                .font(.title3)
                .foregroundColor(.secondary)
            HStack(spacing: 24) {
                Label("溼度 \(data.main.humidity)%", systemImage: "humidity")
                Label("體感 \(Int(data.main.temp))°C", systemImage: "thermometer")
            }
        }
        .padding()
    }
}
```
:::

幾個小細節值得學：first? 安全取第一個元素（列表可能為空），?? "未知" 給兜底文案；76 號細字重的溫度數字是天氣類 App 的經典配方；Label 是"圖示+文字"的官方元件，比手拼 HStack 更規範。

#### 五、互動細節與收藏城市

- 搜尋框：頂部 .searchable 修飾符，系統自帶搜尋互動，提交時調 vm.search；
- 收藏城市：把常看的城市存進 UserDefaults，下次開啟自動查；
- 下拉重新整理：.refreshable { await vm.search(...) } 一行搞定；
- 天氣圖示：用 Image(systemName:) 按描述對映（sun.max / cloud.rain / snowflake），介面立刻活起來。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：中文城市的"梗"

{class="mt-1"}
OpenWeatherMap 對中文城市名支援一般，搜"北京"可能無結果而 "beijing" 正常。產品化做法是內建一份"城市名 → 英文/座標"對映表，或接國內天氣服務。練手階段先支援拼音/英文城市名即可，別和它較勁。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：天氣 App 驗收清單

#### 六、網路請求怎麼除錯：列印、抓包與模擬慢網

聯網 App 出問題，十有八九在"請求沒發對"或"響應沒解析對"。三個除錯手段：

1. 列印原始資料：把 String(data: data, encoding: .utf8) 列印出來看原始 JSON——欄位名、型別一目瞭然，比猜快十倍；
2. 抓包工具：Mac 上免費的 Proxyman / 開源 Charles 能截獲 App 的全部請求和響應，像 X 光一樣看清網路層；
3. 模擬弱網：模擬器選單 Features → Network Link Conditioner（需從開發者網站下載工具），能模擬 3G、高延遲——測出"轉圈半天"的體驗問題。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：請求沒過 ATS？

{class="mt-1"}
如果請求一發出就報 "App Transport Security" 錯誤，八成是用了 http:// 明文地址。正式介面必須 HTTPS；本地除錯臨時開例外（Info.plist 加 NSAllowsLocalNetworking），上架前記得清乾淨。
:::

{class="mt-1"}
① 正常搜尋出天氣；② 斷開網路，App 優雅報錯不崩潰（模擬器裡關掉 Mac 的網路測！）；③ 輸一個不存在的城市，提示友好；④ 收藏兩個城市，重啟 App 還在；⑤ 深色模式下介面不刺眼。五條全過，這個專案才算畢業。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 先瀏覽器試 API、看懂 JSON，再寫程式碼——"預習"永遠不虧
- API Key 藏進 xcconfig，絕不進程式碼庫
- Codable 模型 + URLSession async/await：欄位對上，JSON 自動解析
- loading/success/error 三段式狀態是聯網介面萬金油
- 斷網、空輸入、城市不存在——錯誤處理是聯網 App 的及格線
:::
