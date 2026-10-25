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
記賬本係"練內功"，天氣 App 係"見世面"——佢要同互聯網打交道。呢個項目你會學到：申請免費 API、解析 JSON、處理"加載中／成功／失敗"三種界面狀態，仲有點樣將 API 密鑰收埋好。做完佢，你就具備咗做任何"上網 App"嘅能力——新聞、匯率、翻譯，套路一模一樣。

#### 一、申請免費天氣 API

個人練手，推薦 OpenWeatherMap 或者國內嘅和風天氣（QWeather）——都有免費額度，註冊就即刻用得。以 OpenWeatherMap 為例：

1. 註冊賬號 → 喺 API keys 頁面生成一個 Key（apikey）；
2. 免費版可以調用 Current Weather 接口：api.openweathermap.org/data/2.5/weather? q=beijing&appid=你的Key&units=metric；
3. 喺瀏覽器先試一次，睇吓返回嘅 JSON 生乜嘢樣——呢個係接任何 API 之前必做嘅"預習"。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
避坑提醒：密鑰絕對唔可以寫死喺代碼入面

{class="mt-1"}
API Key 等於你嘅"銀包密碼"，寫入代碼一提交上 GitHub，幾個鐘之內就會畀爬蟲掃走盜刷。iOS 嘅正確做法：放入 Config.xcconfig（配置檔案，已經畀 gitignore 忽略），通過 Info.plist 讀入代碼。搜尋"iOS xcconfig 管理密鑰"照住改就得。
:::

#### 二、網絡層：URLSession + Codable

先照 API 返回嘅 JSON 定義模型，再寫服務：

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

#### 三、三種界面狀態：加載中 / 成功 / 失敗

上網 App 嘅靈魂在於"狀態管理"。網絡慢、斷網、城市名打錯……每種情況界面都要向用戶交代。用枚舉 + switch 優雅咁表示：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 界面狀態</span><span class="dots">···</span>
:::

```
enum LoadState {
    case loading                  // 兜緊圈
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
            state = .error("搵唔到呢個城市，轉個名再試吓？")
        }
    }
}

// 界面入面：
switch vm.state {
case .loading: ProgressView("載入中…")
case .success(let d): WeatherContent(data: d)
case .error(let msg): Text(msg).foregroundColor(.secondary)
}
```
:::

呢個 loading/success/error 三段式係上網界面嘅"萬金油模板"，先背咗佢，以後所有上網 App 都照辦煮碗。

#### 四、實戰界面代碼：將天氣畫出嚟

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

幾個小細節值得學：first? 安全攞第一個元素（列表可能係空），?? "未知" 做兜底文案；76 號幼字重嘅溫度數字係天氣類 App 嘅經典配方；Label 係"圖標+文字"嘅官方組件，好過人手砌 HStack 咁規範。

#### 五、交互細節同收藏城市

- 搜尋框：頂部 .searchable 修飾符，系統自帶搜尋交互，提交嗰陣調用 vm.search；
- 收藏城市：將成日睇嘅城市存入 UserDefaults，下次打開自動查；
- 下拉刷新：.refreshable { await vm.search(...) } 一行搞掂；
- 天氣圖標：用 Image(systemName:) 按描述映射（sun.max / cloud.rain / snowflake），界面即刻活起嚟。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：中文城市嘅"梗"

{class="mt-1"}
OpenWeatherMap 對中文城市名支援一般，搜"北京"可能冇結果而 "beijing" 就正常。產品化做法係內置一份"城市名 → 英文／坐標"映射表，或者接國內天氣服務。練手階段先支援拼音／英文城市名就得，咪同佢硬撼。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
嚟動手：天氣 App 驗收清單

#### 六、網絡請求點樣調試：打印、抓包同模擬慢網

上網 App 出問題，十居其九都係"請求發得唔啱"或者"響應解析得唔啱"。三個調試手段：

1. 打印原始數據：將 String(data: data, encoding: .utf8) 打印出嚟睇原始 JSON——字段名、類型一目了然，好過估快十倍；
2. 抓包工具：Mac 上免費嘅 Proxyman／開源嘅 Charles 可以截獲 App 嘅全部請求同響應，好似 X 光咁睇清網絡層；
3. 模擬弱網：模擬器菜單 Features → Network Link Conditioner（需要由開發者網站下載工具），可以模擬 3G、高延遲——測出"轉圈轉半日"嘅體驗問題。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：請求過唔到 ATS？

{class="mt-1"}
如果請求一發出就報 "App Transport Security" 錯誤，好大可能係用咗 http:// 明文地址。正式接口必須 HTTPS；本地調試臨時開例外（Info.plist 加 NSAllowsLocalNetworking），上架之前記得清乾淨。
:::

{class="mt-1"}
① 正常搜尋出天氣；② 斷開網絡，App 優雅報錯唔崩潰（喺模擬器入面閂咗 Mac 嘅網絡嚟測！）；③ 輸入一個唔存在嘅城市，提示要友好；④ 收藏兩個城市，重啟 App 仲喺度；⑤ 深色模式下界面唔刺眼。五條全部過關，呢個項目先算畢業。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 先喺瀏覽器試 API、睇得明 JSON，再寫代碼——"預習"永遠唔蝕
- API Key 收入 xcconfig，絕不進代碼庫
- Codable 模型 + URLSession async/await：字段對上，JSON 自動解析
- loading/success/error 三段式狀態係上網界面嘅萬金油
- 斷網、空輸入、城市唔存在——錯誤處理係上網 App 嘅及格線
:::
