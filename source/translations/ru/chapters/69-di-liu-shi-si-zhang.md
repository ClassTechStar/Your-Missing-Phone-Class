---
id: di-liu-shi-si-zhang
num: 64
part: ios-kai-fa-pian
nav: Глава 64: Хранение данных и сетевые запросы
toc: default
kind: chapter
---

### Глава 64. Хранение данных и сетевые запросы

{class="chapter-intro mb-4"}
Приложение, которое умеет только «показывать», мертво; жить ему дают умение хранить данные и выходить в сеть. В этой главе — знакомство с «тройкой» слоя данных iOS: UserDefaults (мелкие настройки), SwiftData (структурированные данные), URLSession (разговор с сервером), плюс Codable для разбора JSON и современный async/await. Пройдёте главу — и сможете писать настоящие приложения, которые помнят привычки пользователя и обновляют содержимое в реальном времени.

#### 1. Как выбрать способ хранения: сначала взгляните на эту таблицу

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Способ</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Что хранить</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Особенности</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Где используется в книге</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Разрозненные настройки (переключатели, предпочтения)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Пары «ключ — значение», просто и напрямую</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Настройки в главе 65, избранные города в главе 66</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Структурированные данные (записи, учёт)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Официальная обёртка базы данных, объявление одной строкой через @Model</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Записи о доходах и расходах в главе 65</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Данные сервера (не храним, берём из сети)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Сетевой фреймворк из состава системы, без сторонних зависимостей</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Данные о погоде в главе 66</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Кто за что отвечает в тройке данных

Запомните правило: «мелкие настройки — в UserDefaults, массивы данных — в SwiftData, внешние данные — через URLSession». Core Data из старых уроков по-прежнему работает (SwiftData — её современное воплощение), а ручной SQLite почти не нужен — учитесь сразу новому, не ходите старыми дорожками.

#### 2. UserDefaults: храним мелкие настройки

::: div .code-block
:::inline div .code-head
<span>SWIFT · Пример UserDefaults</span><span class="dots">···</span>
:::

```
// Запись: сохраняем значение
UserDefaults.standard.set(true, forKey: "isDarkMode")
UserDefaults.standard.set("Пекин", forKey: "favoriteCity")

// Чтение: достаём (нет — вернётся значение по умолчанию)
let isDark = UserDefaults.standard.bool(forKey: "isDarkMode")
let city = UserDefaults.standard.string(forKey: "favoriteCity") ?? "Пекин"

// Удаление: убираем ключ
UserDefaults.standard.removeObject(forKey: "isDarkMode")
```
:::

Учтите: он годится только для разрозненных мелких настроек — десятки и сотни записей отдавайте SwiftData, не превращайте UserDefaults в базу данных (запуск замедлится, а поиски усложнятся).

#### 3. SwiftData: настоящий дом для данных

SwiftData — официальное решение для баз данных начиная с iOS 17, доведённое до предела простоты «создать таблицу, добавить, удалить, изменить, прочитать» — одна аннотация @Model, и класс данных превращается в таблицу базы:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Пример SwiftData</span><span class="dots">···</span>
:::

```
import SwiftData

// 1. @Model: этот класс автоматически становится «таблицей»
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

// 2. Подключаем контейнер в точке входа приложения
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: Record.self)   // база готова
    }
}

// 3. В представлениях читаем через @Query, пишем через @Environment
struct RecordListView: View {
    @Query(sort: \Record.date, order: .reverse) var records: [Record]
    @Environment(\.modelContext) private var context

    var body: some View {
        List(records) { r in
            Text("\(r.category) \(r.amount) юаня")
        }
    }

    func add(amount: Double, category: String) {
        let r = Record(amount: amount, category: category, note: "", date: Date())
        context.insert(r)     // сохраняем
        try? context.save()   // записываем на диск
    }
}
```
:::

Шаблон «@Model + modelContainer + @Query» можно переносить в любой ваш проект как есть — достаточно заменить имена полей. Данные меняются — @Query сама обновляет интерфейс. Волшебство, и ничего больше.

#### 4. Codable: «переводчик» для JSON

Данные с сервера — в основном текст в формате JSON. Протокол Codable в Swift делает превращение «JSON ⇄ структура» автоматическим — совпали имена полей, и магия сработала:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Разбор JSON через Codable</span><span class="dots">···</span>
:::

```
// JSON: {"name":"Пекин","main":{"temp":26.5},"weather":[{"description":"Ясно"}]}
struct WeatherResponse: Codable {
    let name: String
    let main: Main
    let weather: [Weather]
}
struct Main: Codable { let temp: Double }
struct Weather: Codable { let description: String }

// JSON-строка → структура
let decoder = JSONDecoder()
let data = jsonString.data(using: .utf8)!
let result = try decoder.decode(WeatherResponse.self, from: data)
print(result.weather[0].description)   // "Ясно"
```
:::

Железное правило: сперва посмотрите настоящий JSON из ответа, потом объявляйте поля. Многие баги «разбор не удался» — это опечатка в имени поля или неверно угаданный тип (сервер прислал строку «26.5», а вы объявили Double) — выведите исходный JSON на печать и сверьте: дело десяти секунд.

#### 5. URLSession + async/await: разговор с сервером

Для выхода в сеть iOS использует системный URLSession в паре с async/await (асинхронными функциями) Swift — «ждать сеть» так же естественно, как «ждать курьера»:

::: div .code-block
:::inline div .code-head
<span>SWIFT · URLSession + async/await</span><span class="dots">···</span>
:::

```
struct WeatherService {
    // Асинхронные функции: async — «нужно чуть подождать», throws — «может выбросить ошибку»
    func fetchWeather(city: String) async throws -> WeatherResponse {
        let url = URL(string:
            "https://api.example.com/weather?city=\(city)")!
        let (data, _) = try await URLSession.shared.data(from: url)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}

// Место вызова (внутри .task):
.task {
    do {
        let weather = try await service.fetchWeather(city: "Пекин")
        // обновляем интерфейс…
    } catch {
        print("Что-то пошло не так: \(error)")
    }
}
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Осторожно: два железных правила сети

{class="mt-1"}
① Сетевые вызовы — только async/await, главный поток не блокируем никогда: зависший интерфейс — впечатление уровня «приложение сломалось». Структурная конкурентность Swift делает это естественным, но не забывайте про try await и do/catch. ② ATS по умолчанию запрещает открытый HTTP: iOS требует HTTPS. Для теста локального сервиса http:// придётся временно открыть исключение в Info.plist (NSAppTransportSecurity), но настоящий продукт обязан целиком работать по HTTPS — и проверка при публикации следит именно за этим.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Практика: делаем мини-приложение «Цитата дня»

#### 6. Сетевые ошибки тоже надо «сортировать»: не вываливайте на пользователя всё подряд

Нет сети, тайм-аут, 404, ошибка сервера 500… разным ошибкам — разные слова для пользователя:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Поуровневая обработка ошибок</span><span class="dots">···</span>
:::

```
func friendlyMessage(_ error: Error) -> String {
    if let urlError = error as? URLError {
        switch urlError.code {
        case .notConnectedToInternet: return "Сеть пропала — проверить подключение?"
        case .timedOut:               return "Запрос не успел — попробовать позже?"
        case .cannotFindHost:         return "Сервер не найден"
        default:                      return "Проблема с сетью: \(urlError.code)"
        }
    }
    if let d = error as? DecodingError {
        return "Неожиданный формат данных (возможно, API изменился)"
    }
    return "Что-то пошло не так: \(error.localizedDescription)"
}
```
:::

Пользователю — «человеческий язык», в журнал — «оригинал» (print полного error). Не швыряйте пользователю английскую тарабарщину из error.localizedDescription — ощущение настоящего продукта прячется именно в таких мелочах.

{class="mt-1"}
Найдите бесплатный API цитат (например, hitokoto или похожий) и через URLSession + async/await тяните «цитату дня», показывайте её в центре экрана, добавьте кнопку «Ещё одну». Понравившиеся цитаты складывайте через SwiftData в «избранное». Это упражнение прогоняет через руки сразу UserDefaults, SwiftData, Codable и URLSession — после него главы 7 и 8 будут пустяком.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Краткие итоги главы

- Правило: мелкие настройки — в UserDefaults, массивы данных — в SwiftData, внешние данные — через URLSession
- Три кита SwiftData: @Model объявляет таблицу, modelContainer подключает контейнер, @Query читает + context.insert пишет
- Codable «переводит» JSON автоматически: совпали поля — магия сработала
- URLSession + async/await: ждать сеть как ждать курьера; do/catch обрабатывает неудачи
- Два железных правила: не блокируем главный поток; настоящий продукт — только HTTPS (ATS)
:::
