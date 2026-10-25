---
id: di-liu-shi-liu-zhang
num: 66
part: ios-kai-fa-pian
nav: Глава 66: Проект 2 — приложение погоды (сетевая версия)
toc: default
kind: chapter
---

### Глава 66. Проект 2 — приложение для погоды (сетевая версия)

{class="chapter-intro mb-4"}
Книга учёта была «тренировкой внутреннего искусства», а погодное приложение — «выходом в большой мир»: ему приходится иметь дело с интернетом. В этом проекте вы научитесь получать бесплатный API, разбирать JSON, работать с тремя состояниями интерфейса «загрузка / успех / ошибка» и прятать API-ключ. Освоите его — и сможете делать любое «сетевое приложение»: новости, курсы валют, перевод — схема одна и та же.

#### 1. Получаем бесплатный погодный API

Для личной практики советую OpenWeatherMap или китайский сервис QWeather — у обоих есть бесплатные квоты, зарегистрировался и пользуйся. Разберём на примере OpenWeatherMap:

1. Зарегистрируйте аккаунт → на странице API keys сгенерируйте ключ (apikey);
2. Бесплатная версия умеет вызывать интерфейс Current Weather: api.openweathermap.org/data/2.5/weather? q=beijing&appid=ваш_ключ&units=metric;
3. Сперва попробуйте его в браузере и посмотрите, как выглядит возвращаемый JSON, — такая «подготовка» обязательна перед подключением любого API.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Осторожно: ключ нельзя вшивать в код намертво

{class="mt-1"}
API-ключ — это пароль от вашего кошелька: попадёт в код и уедет на GitHub — за считаные часы его сметут краулеры и спустят на какие-нибудь списания. Правильный путь в iOS: положить в Config.xcconfig (конфигурационный файл, игнорируемый gitignore) и читать в код через Info.plist. Найдите «iOS xcconfig управление ключами» и повторите по шагам.
:::

#### 2. Сетевой слой: URLSession + Codable

Сперва опишите модель по JSON, который возвращает API, затем напишите сервис:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Модель данных + сервис</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"Ясно"}],"main":{"temp":26.5,"humidity":40},"name":"Пекин"}
struct WeatherResponse: Codable {
    let weather: [Weather]
    let main: Main
    let name: String
}
struct Weather: Codable { let description: String }
struct Main: Codable { let temp: Double; let humidity: Int }

struct WeatherService {
    let key: String   // читается из xcconfig

    func fetchWeather(city: String) async throws -> WeatherResponse {
        var comps = URLComponents(string: "https://api.openweathermap.org/data/2.5/weather")!
        comps.queryItems = [
            URLQueryItem(name: "q", value: city),
            URLQueryItem(name: "appid", value: key),
            URLQueryItem(name: "units", value: "metric"),
            URLQueryItem(name: "lang", value: "ru")
        ]
        let (data, _) = try await URLSession.shared.data(from: comps.url!)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}
```
:::

#### 3. Три состояния интерфейса: загрузка / успех / ошибка

Душа сетевого приложения — управление состояниями. Медленная сеть, обрыв связи, опечатка в названии города… на каждый случай интерфейс должен отчитаться перед пользователем. Выразим это изящно — перечисление + switch:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Состояние интерфейса</span><span class="dots">···</span>
:::

```
enum LoadState {
    case loading                  // крутится спиннер
    case success(WeatherResponse) // успех
    case error(String)            // ошибка
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
            state = .error("Не удалось найти этот город — попробуйте другое название?")
        }
    }
}

// В интерфейсе:
switch vm.state {
case .loading: ProgressView("Загрузка…")
case .success(let d): WeatherContent(data: d)
case .error(let msg): Text(msg).foregroundColor(.secondary)
}
```
:::

Эта трёхчастная схема loading/success/error — «универсальная мазь» сетевых интерфейсов. Выучите её наизусть, а дальше во всех сетевых приложениях повторяйте по образцу.

#### 4. Боевой код интерфейса: рисуем погоду

::: div .code-block
:::inline div .code-head
<span>SWIFT · Экран погоды (ключевой фрагмент)</span><span class="dots">···</span>
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
            Text(data.weather.first?.description ?? "Неизвестно")
                .font(.title3)
                .foregroundColor(.secondary)
            HStack(spacing: 24) {
                Label("Влажность \(data.main.humidity)%", systemImage: "humidity")
                Label("Ощущается как \(Int(data.main.temp))°C", systemImage: "thermometer")
            }
        }
        .padding()
    }
}
```
:::

Несколько мелочей, которые стоит перенять: first? безопасно берёт первый элемент (список может быть пуст), ?? «Неизвестно» подставляет запасной текст; тонкий шрифт (вес 76) у цифр температуры — классический рецепт погодных приложений; Label — официальный компонент «иконка + текст», аккуратнее ручной сборки из HStack.

#### 5. Детали взаимодействия и избранные города

- Поле поиска: модификатор .searchable вверху страницы — поисковое поведение даёт система, при отправке вызываем vm.search;
- Избранные города: часто смотримые города кладём в UserDefaults, при следующем открытии они запрашиваются автоматически;
- Обновление потягиванием: .refreshable { await vm.search(...) } — одна строка, и готово;
- Погодные значки: через Image(systemName:) сопоставьте описание с иконкой (sun.max / cloud.rain / snowflake) — и интерфейс сразу оживает.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Совет: фокусы с китайскими названиями городов

{class="mt-1"}
OpenWeatherMap поддерживает китайские названия городов не блестяще: поиск китайским названием может ничего не найти, а латиницей «beijing» работает нормально. Для продукта правильнее встроить таблицу соответствий «название города → английский/координаты» или подключить китайский погодный сервис. На этапе практики достаточно принять пиньинь и английские названия — не воюйте с этим.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Практика: чек-лист приёмки погодного приложения

#### 6. Как отлаживать сетевые запросы: печать, перехват трафика и имитация медленной сети

Сетевое приложение барахлит — в девяти случаях из десяти это «запрос ушёл не тот» или «ответ разобран не так». Три средства отладки:

1. Печать исходных данных: выведите String(data: data, encoding: .utf8) и глядите на сырой JSON — имена полей и типы как на ладони, в десять раз быстрее догадок;
2. Перехват трафика: бесплатный на Mac Proxyman и открытый Charles перехватывают все запросы и ответы приложения и позволяют разглядеть сетевой слой, как на рентгене;
3. Имитация слабой сети: в меню симулятора Features → Network Link Conditioner (инструмент скачивается с сайта разработчика) можно сымитировать 3G и большую задержку — и выловить проблемы вроде «крутится и крутится».

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Совет: запрос не проходит ATS?

{class="mt-1"}
Если ошибка «App Transport Security» выскакивает сразу при отправке запроса, почти наверняка используется открытый адрес http://. Настоящие интерфейсы обязаны ходить по HTTPS; для локальной отладки можно временно сделать исключение (добавить NSAllowsLocalNetworking в Info.plist), а перед публикацией не забудьте всё подчистить.
:::

{class="mt-1"}
① Погода ищется как надо; ② отрубаем сеть — приложение сообщает об ошибке изящно и не падает (проверьте, отключив сеть Mac при работающем симуляторе!); ③ вводим несуществующий город — получаем дружелюбную подсказку; ④ добавляем два города в избранное — после перезапуска они на месте; ⑤ в тёмном режиме интерфейс не слепит. Все пять пунктов сданы — вот теперь проект можно выпускать.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Краткие итоги главы

- Сперва опробуйте API в браузере и разберитесь в JSON, потом пишите код — «подготовка» ещё никого не подводила
- API-ключ прячем в xcconfig, в репозитории кода ему не место
- Модель Codable + URLSession с async/await: поля совпали — JSON разбирается сам
- Трёхчастное состояние loading/success/error — универсальная мазь сетевых интерфейсов
- Нет сети, пустой ввод, несуществующий город — обработка ошибок это проходной балл сетевого приложения
:::
