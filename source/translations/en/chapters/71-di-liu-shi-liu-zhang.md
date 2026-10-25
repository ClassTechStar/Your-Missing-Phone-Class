---
id: di-liu-shi-liu-zhang
num: 66
part: ios-kai-fa-pian
nav: Chapter 66: Project 2 — Weather App (Networked Version)
toc: default
kind: chapter
---

### Chapter 66: Project 2—Weather App (the Networked Version)

{class="chapter-intro mb-4"}
The expense tracker was "internal training"; the weather app is "seeing the world"—it has to deal with the internet. In this project you'll learn: how to apply for a free API, parse JSON, handle the three UI states of "loading/success/failure," and how to keep an API key safe. Once you finish it, you'll be able to build any "networked app"—news, exchange rates, translation—the pattern is exactly the same.

#### 1. Apply for a free weather API

For personal practice, we recommend OpenWeatherMap or, in China, QWeather (HeFeng Weather)—both have free tiers you can use right after registering. Taking OpenWeatherMap as an example:

1. Register an account → generate a Key (apikey) on the API keys page;
2. The free tier can call the Current Weather endpoint: api.openweathermap.org/data/2.5/weather? q=beijing&appid=YOUR_KEY&units=metric;
3. Try it in a browser first and see what the returned JSON looks like—this "preview" is a must before hooking up any API.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Pitfall warning: never hard-code the key into your code

{class="mt-1"}
An API key is like your "wallet password." Put it in code, commit it to GitHub, and crawlers will scan it up and abuse it within hours. The right way on iOS: put it in a Config.xcconfig (a config file that's already gitignored) and read it into your code via Info.plist. Search "iOS xcconfig manage keys" and follow along.
:::

#### 2. The network layer: URLSession + Codable

First define the model based on the JSON the API returns, then write the service:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Data model + service</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"Sunny"}],"main":{"temp":26.5,"humidity":40},"name":"Beijing"}
struct WeatherResponse: Codable {
    let weather: [Weather]
    let main: Main
    let name: String
}
struct Weather: Codable { let description: String }
struct Main: Codable { let temp: Double; let humidity: Int }

struct WeatherService {
    let key: String   // read in from xcconfig

    func fetchWeather(city: String) async throws -> WeatherResponse {
        var comps = URLComponents(string: "https://api.openweathermap.org/data/2.5/weather")!
        comps.queryItems = [
            URLQueryItem(name: "q", value: city),
            URLQueryItem(name: "appid", value: key),
            URLQueryItem(name: "units", value: "metric"),
            URLQueryItem(name: "lang", value: "en")
        ]
        let (data, _) = try await URLSession.shared.data(from: comps.url!)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}
```
:::

#### 3. Three UI states: loading / success / failure

The soul of a networked app is "state management." Slow network, no connection, a misspelled city name... the UI needs to give the user an answer for every case. Express it elegantly with an enum + switch:

::: div .code-block
:::inline div .code-head
<span>SWIFT · UI state</span><span class="dots">···</span>
:::

```
enum LoadState {
    case loading                  // spinner showing
    case success(WeatherResponse) // success
    case error(String)            // failure
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
            state = .error("Can't find that city — try another name?")
        }
    }
}

// In the UI:
switch vm.state {
case .loading: ProgressView("Loading…")
case .success(let d): WeatherContent(data: d)
case .error(let msg): Text(msg).foregroundColor(.secondary)
}
```
:::

This loading/success/error three-part pattern is the "all-purpose template" for networked interfaces—memorize it first, and every networked app you build later can follow the same recipe.

#### 4. Hands-on UI code: drawing the weather

::: div .code-block
:::inline div .code-head
<span>SWIFT · Weather screen (core excerpt)</span><span class="dots">···</span>
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
            Text(data.weather.first?.description ?? "Unknown")
                .font(.title3)
                .foregroundColor(.secondary)
            HStack(spacing: 24) {
                Label("Humidity \(data.main.humidity)%", systemImage: "humidity")
                Label("Feels like \(Int(data.main.temp))°C", systemImage: "thermometer")
            }
        }
        .padding()
    }
}
```
:::

A few details worth learning: first? safely grabs the first element (the list may be empty), and ?? "Unknown" provides fallback text; a large temperature number in a thin font weight is a classic recipe for weather apps; Label is the official "icon + text" component, cleaner than hand-assembling an HStack.

#### 5. Interaction details and favorite cities

- Search box: the .searchable modifier at the top gives you system-native search interaction; call vm.search on submit;
- Favorite cities: store frequently viewed cities in UserDefaults, and they're looked up automatically the next time you open the app;
- Pull to refresh: one line with .refreshable { await vm.search(...) } does it;
- Weather icons: map descriptions with Image(systemName:) (sun.max / cloud.rain / snowflake) and the UI comes alive instantly.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tip: the quirk with Chinese city names

{class="mt-1"}
OpenWeatherMap's support for Chinese city names is spotty—searching a Chinese name may return no results while "beijing" works fine. The production-grade approach is to bundle a "city name → English/coordinates" mapping table, or hook up a domestic weather service. At the practice stage, just support pinyin/English city names—don't fight it.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Get hands-on: the weather app acceptance checklist

#### 6. How to debug network requests: printing, packet capture, and simulating a slow network

When a networked app misbehaves, nine times out of ten it's "the request wasn't sent right" or "the response wasn't parsed right." Three debugging tools:

1. Print the raw data: print String(data: data, encoding: .utf8) to see the raw JSON—field names and types at a glance, ten times faster than guessing;
2. Packet capture tools: the free Proxyman on Mac, or the open-source Charles, can intercept all of the app's requests and responses, letting you see the network layer like an X-ray;
3. Simulate a weak network: the Simulator menu's Features → Network Link Conditioner (download the tool from the developer website) can simulate 3G and high latency—surfacing those "spinner spins forever" experience problems.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tip: request blocked by ATS?

{class="mt-1"}
If a request fails the moment it's sent with an "App Transport Security" error, you're probably using a plain-text http:// address. Production endpoints must use HTTPS; for local debugging you can temporarily add an exception (NSAllowsLocalNetworking in Info.plist), but remember to clean it up before release.
:::

{class="mt-1"}
① Search for weather normally; ② disconnect the network and the app fails gracefully without crashing (turn off your Mac's network and test in the Simulator!); ③ enter a nonexistent city and get a friendly message; ④ favorite two cities and they're still there after restarting the app; ⑤ the UI looks good in Dark Mode. Only when all five pass does this project graduate.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Chapter summary

- Try the API in a browser and understand the JSON before writing code—"previewing" never hurts
- Hide the API key in an xcconfig—never in the codebase
- Codable models + URLSession async/await: match the fields and the JSON parses automatically
- The loading/success/error three-state pattern is the Swiss Army knife of networked UIs
- No connection, empty input, nonexistent city—error handling is the passing grade for a networked app
:::
