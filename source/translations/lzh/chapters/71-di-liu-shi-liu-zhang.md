---
id: di-liu-shi-liu-zhang
num: 66
part: ios-kai-fa-pian
nav: 第六十六章：項目二——天氣查詢App（網絡版）
toc: default
kind: chapter
---

### 第六十六章：項目二——天氣查詢 App（網絡版）

{class="chapter-intro mb-4"}
記賬本者「練內功」也，天氣 App 者「廣見聞」也——將與互聯網相周旋。此項汝將學：請免費之 API、解 JSON、處「載入中/成/敗」三種界面之態，及藏 API 密鑰之法。成之，則作任何「連網 App」之能具矣——新聞、匯率、翻譯，其術如一。

#### 一、請免費天氣之 API

個人練手，薦 OpenWeatherMap 或國內之和風天氣（QWeather）——皆有免費之額，註冊即用。以 OpenWeatherMap 為例：

1. 註冊賬號 → 於 API keys 頁生一 Key（apikey）；
2. 免費版可調 Current Weather 之接口：api.openweathermap.org/data/2.5/weather? q=beijing&appid=汝之Key&units=metric；
3. 先於瀏覽器一試，觀其返 JSON 之狀——此接任何 API 前必為之「預習」。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
避坑之警：密鑰絕不可寫死於碼中

{class="mt-1"}
API Key 猶汝「錢囊之密碼」，一入碼而提交於 GitHub，數時之內即為爬蟲所掃而盜刷。iOS 之正法：納於 Config.xcconfig（配置之檔，已為 gitignore 所忽），由 Info.plist 讀入碼中。搜「iOS xcconfig 管理密鑰」依而改之即可。
:::

#### 二、網絡層：URLSession + Codable

先依 API 所返之 JSON 定其模，後書其服：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 數據模型 + 服務</span><span class="dots">···</span>
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

#### 三、界面三態：載入中 / 成 / 敗

連網 App 之魂在「狀態管理」。網緩、斷網、城名誤書……凡此諸況，界面皆當予用戶以交代。以枚舉 + switch 雅而表之：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 界面狀態</span><span class="dots">···</span>
:::

```
enum LoadState {
    case loading                  // 旋轉中
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
            state = .error("查無此城，易其名再試之？")
        }
    }
}

// 界面中：
switch vm.state {
case .loading: ProgressView("載入中…")
case .success(let d): WeatherContent(data: d)
case .error(let msg): Text(msg).foregroundColor(.secondary)
}
```
:::

此 loading/success/error 三段式者，連網界面之「萬金油模板」也，先誦之，後凡連網 App 皆可依樣畫瓢。

#### 四、實戰界面之碼：繪天氣而出

::: div .code-block
:::inline div .code-head
<span>SWIFT · 天氣界面（核心片段）</span><span class="dots">···</span>
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

數細節可學：first? 安全取首元（列表或空），?? "未知" 以為備底之文；76 號細字重之溫度數字，天氣類 App 之經典配方也；Label 者「圖標+文字」官方之組件，較手拼 HStack 更為規範。

#### 五、交互之細與所藏之城

- 搜索之框：頂部 .searchable 修飾符，系統自帶搜索之交互，提交時調 vm.search；
- 藏城：以常觀之城貯於 UserDefaults，下次啟則自動查之；
- 下拉而刷：.refreshable { await vm.search(...) } 一行而成；
- 天氣之圖標：以 Image(systemName:) 依所述而映（sun.max / cloud.rain / snowflake），界面立活。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：中文城名之「梗」

{class="mt-1"}
OpenWeatherMap 於中文城名之助平平，搜「北京」或無所得而 "beijing" 自若。產品化之法，乃內置「城名 → 英文/坐標」映射之表，或接國內天氣之服。練手之期，先支拼音/英文城名即可，勿與之較。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：天氣 App 驗收之單

#### 六、網絡之請何以調試：印之、抓包與擬緩網

連網 App 有疾，十居八九在「請未發正」或「應未解正」。調試之術三：

1. 印原始數據：以 String(data: data, encoding: .utf8) 印而觀原 JSON——字段名、類型一目了然，較猜速十倍；
2. 抓包之具：Mac 上免費之 Proxyman / 開源之 Charles 能截 App 諸請與應，如 X 光之透視網絡層；
3. 擬弱網：擬器菜單 Features → Network Link Conditioner（須自開發者之站載具），能擬 3G、高遲滯——以驗「旋轉半晌」之疾。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：請未過 ATS 乎？

{class="mt-1"}
若請甫發即報 "App Transport Security" 之誤，什九為用 http:// 明文之址所致。正式之接口必 HTTPS；本地調試暫開例外（Info.plist 增 NSAllowsLocalNetworking），上架前務滌除之。
:::

{class="mt-1"}
① 常搜而得天氣；② 斷網，App 雅報其誤而不崩（於擬器中關 Mac 之網以試之！）；③ 輸不存之城，提示宜人；④ 藏二城，重啟 App 猶在；⑤ 深色模式下界面不刺目。五者悉過，此項方為卒業。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小結

- 先於瀏覽器試 API、讀懂 JSON，而後書碼——「預習」終無所虧
- API Key 藏於 xcconfig，絕不入碼庫
- Codable 之模 + URLSession async/await：字段相合，JSON 自解
- loading/success/error 三段之態，連網界面之萬金油也
- 斷網、空輸、城之不存——誤之處置，連網 App 及格之線也
:::
