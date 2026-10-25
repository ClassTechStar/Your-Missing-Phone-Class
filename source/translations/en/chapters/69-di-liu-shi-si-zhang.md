---
id: di-liu-shi-si-zhang
num: 64
part: ios-kai-fa-pian
nav: Chapter 64: Data Storage and Network Requests
toc: default
kind: chapter
---

### Chapter 64: Data Storage and Network Requests

{class="chapter-intro mb-4"}
An app you can only "look at" is dead; an app that can store data and reach the network is alive. This chapter introduces the "three essentials" of the iOS data layer: UserDefaults (for small settings), SwiftData (for structured data), and URLSession (for talking to servers), plus Codable for parsing JSON and the modern async/await. After this chapter, you'll be able to write real apps that remember user preferences and update their content live.

#### 1. Choosing a Storage Option: Look at This Table First

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Option</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">What it's good for</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Key traits</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Where this book uses it</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Loose settings (toggles, preferences)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Key-value pairs, simple and direct</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Chapter 65 settings, Chapter 66 favorite cities</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Structured data (transactions, records)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The official database wrapper, declared in one line with @Model</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Chapter 65 transaction records</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Server data (not stored, fetched online)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The built-in networking framework, no third-party dependencies</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Chapter 66 weather data</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
The division of labor among the data trio

Memorize this mantra: "small settings go into UserDefaults, batches of data go into SwiftData, and data from the outside travels over URLSession." Core Data from old tutorials still works (SwiftData is its modern incarnation), while hand-written SQLite is essentially a thing of the past—learn the new way directly and don't take the old road.

#### 2. UserDefaults: Storing a Few Small Settings

::: div .code-block
:::inline div .code-head
<span>SWIFT · UserDefaults example</span><span class="dots">···</span>
:::

```
// Write: store a value
UserDefaults.standard.set(true, forKey: "isDarkMode")
UserDefaults.standard.set("Beijing", forKey: "favoriteCity")

// Read: fetch it (falls back to the default)
let isDark = UserDefaults.standard.bool(forKey: "isDarkMode")
let city = UserDefaults.standard.string(forKey: "favoriteCity") ?? "Beijing"

// Delete: remove a key
UserDefaults.standard.removeObject(forKey: "isDarkMode")
```
:::

Keep in mind that it's only right for loose little settings—hand dozens or hundreds of records over to SwiftData, and don't use UserDefaults as a database (it slows down launch time and makes searching a pain).

#### 3. SwiftData: Giving Data a "Real Home"

SwiftData is the official database solution starting with iOS 17, and it boils "creating tables, adding, deleting, updating, querying" down to the bare minimum—one @Model annotation turns a data class into a database table:

::: div .code-block
:::inline div .code-head
<span>SWIFT · SwiftData example</span><span class="dots">···</span>
:::

```
import SwiftData

// 1. @Model: this class automatically becomes a "table"
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

// 2. Attach the container at the app's entry point
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: Record.self)   // database ready
    }
}

// 3. In views, read with @Query and write via @Environment
struct RecordListView: View {
    @Query(sort: \Record.date, order: .reverse) var records: [Record]
    @Environment(\.modelContext) private var context

    var body: some View {
        List(records) { r in
            Text("\(r.category) \(r.amount) yuan")
        }
    }

    func add(amount: Double, category: String) {
        let r = Record(amount: amount, category: category, note: "", date: Date())
        context.insert(r)     // store
        try? context.save()   // persist to disk
    }
}
```
:::

This "@Model + modelContainer + @Query" template can be dropped into any of your projects as-is—just swap in your own field names. The moment the data changes, @Query refreshes the interface automatically. Simply delightful.

#### 4. Codable: A "Translator" for JSON

Most of what servers send is JSON text. Swift's Codable protocol makes the "JSON ⇄ struct" conversion happen automatically—line up the field names, and the magic works:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Parsing JSON with Codable</span><span class="dots">···</span>
:::

```
// JSON: {"name":"Beijing","main":{"temp":26.5},"weather":[{"description":"Sunny"}]}
struct WeatherResponse: Codable {
    let name: String
    let main: Main
    let weather: [Weather]
}
struct Main: Codable { let temp: Double }
struct Weather: Codable { let description: String }

// JSON string → struct
let decoder = JSONDecoder()
let data = jsonString.data(using: .utf8)!
let result = try decoder.decode(WeatherResponse.self, from: data)
print(result.weather[0].description)   // "Sunny"
```
:::

Iron rule: look at the JSON that actually comes back before you define your fields. Many "parse failed" bugs come from a misspelled field name or a wrongly guessed type (the server sends the string "26.5" and you declared a Double)—print out the raw JSON and compare, and you'll locate the problem in ten seconds.

#### 5. URLSession + async/await: Talking to Servers

iOS networking uses the built-in URLSession, paired with Swift's async/await (asynchronous functions), so "waiting for the network" feels as natural as "waiting for a delivery":

::: div .code-block
:::inline div .code-head
<span>SWIFT · URLSession + async/await</span><span class="dots">···</span>
:::

```
struct WeatherService {
    // Async functions: async marks "I need to wait a moment," throws marks "this can fail"
    func fetchWeather(city: String) async throws -> WeatherResponse {
        let url = URL(string:
            "https://api.example.com/weather?city=\(city)")!
        let (data, _) = try await URLSession.shared.data(from: url)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}

// At the call site (inside .task):
.task {
    do {
        let weather = try await service.fetchWeather(city: "Beijing")
        // update the UI...
    } catch {
        print("Something went wrong: \(error)")
    }
}
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Pitfall Alert: Two Iron Rules of Networking

{class="mt-1"}
1) Networking must use async/await and must never block the main thread—a frozen interface is a crash-level experience. Swift's structured concurrency makes this natural, but don't forget try await and do/catch. 2) ATS blocks plain-text HTTP by default: iOS requires HTTPS. While testing a local http:// service, you can temporarily allow an exception in Info.plist (NSAppTransportSecurity), but a production app must use HTTPS throughout—App Review keeps an eye on this too.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Hands-on: Build a "Quote of the Day" Mini App

#### 6. "Grade" Your Network Errors Too: Don't Throw Every Error at the User

No connection, timeout, 404, server 500... different errors deserve different messages for the user:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Graded error handling</span><span class="dots">···</span>
:::

```
func friendlyMessage(_ error: Error) -> String {
    if let urlError = error as? URLError {
        switch urlError.code {
        case .notConnectedToInternet: return "Network is down — check your connection?"
        case .timedOut:               return "Request timed out — try again in a bit?"
        case .cannotFindHost:         return "Server not found"
        default:                      return "Network problem: \(urlError.code)"
        }
    }
    if let d = error as? DecodingError {
        return "Unexpected data format (the API may have changed)"
    }
    return "Something went wrong: \(error.localizedDescription)"
}
```
:::

Show the user "plain words," and save the "raw words" for the logs (print the full error). Don't fling the gibberish English of error.localizedDescription straight at the user—that feeling of a polished product hides in details like these.

{class="mt-1"}
Find a free quotes API (something like hitokoto), use URLSession + async/await to fetch a "quote of the day," show it in the middle of the screen, and add a "New quote" button. Then use SwiftData to save your favorite quotes into a "favorites" list. This one exercise uses UserDefaults/SwiftData/Codable/URLSession all at once—finish it, and Chapters 7 and 8 will be a piece of cake.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Chapter summary

- The mantra: small settings into UserDefaults, batches of data into SwiftData, outside data over URLSession
- SwiftData's three moves: @Model declares the table, modelContainer attaches the container, @Query reads and context.insert writes
- Codable "translates" JSON automatically: line up the fields and the magic works
- URLSession + async/await: networking feels like waiting for a delivery; do/catch handles failures
- Two iron rules: never block the main thread; production apps must use HTTPS (ATS)
:::
