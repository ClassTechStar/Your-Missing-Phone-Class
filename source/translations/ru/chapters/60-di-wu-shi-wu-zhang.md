---
id: di-wu-shi-wu-zhang
num: 55
part: an-zhuo-kai-fa-pian
nav: Глава 55: Проект 2 — приложение погоды (сетевая версия)
toc: default
kind: chapter
---

### Глава 55. Проект 2 — приложение для погоды (сетевая версия)

{class="chapter-intro mb-4"}
Учётная книга «ставит внутреннюю силу», а приложение погоды «выводит в большой мир» — ему предстоит возиться с интернетом. В этом проекте вы научитесь получать бесплатный API, разбирать JSON, обращаться с тремя состояниями экрана «загрузка / успех / ошибка» и прятать API-ключ так, чтобы его никто не нашёл. Сделаете его — и сможете собрать любое «сетевое приложение»: новости, курсы валют, переводчик — схема везде одна.

#### 1. Получаем бесплатный API погоды

Для личной тренировки рекомендую OpenWeatherMap или китайский QWeather — у обоих есть бесплатные квоты: зарегистрировался и пользуешься. Пример на OpenWeatherMap:

1. зарегистрируйте аккаунт → на странице API keys сгенерируйте ключ (apikey);
2. в бесплатной версии доступен метод Current Weather (текущая погода): api.openweathermap.org/data/2.5/weather? q=beijing&appid=ВАШ_КЛЮЧ&units=metric;
3. сначала попробуйте запрос в браузере и посмотрите, как выглядит ответный JSON, — обязательная «подготовка» перед подключением любого API.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Осторожно: ключ нельзя зашивать в код

{class="mt-1"}
API-ключ — это «пароль от кошелька»: закоммитите его на GitHub, и за пару часов боты его вытащат и растратят. Правильно так: положите ключ в local.properties (этот файл уже исключён через gitignore) и читайте в код через buildConfig в Gradle. Найдите по запросу «лучшие практики сокрытия API-ключа в Android» и действуйте по инструкции.
:::

#### 2. Сетевой слой: Retrofit + разбор JSON

Сначала опишите «модель данных» по JSON, который отдаёт API, — поля, которым нет соответствия, просто игнорируйте:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Модель данных + интерфейс</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"Ясно"}],"main":{"temp":26.5,"humidity":40},"name":"Пекин"}
data class WeatherResponse(
    val weather: List&lt;Weather&gt;,
    val main: Main,
    val name: String
)
data class Weather(val description: String)
data class Main(val temp: Double, val humidity: Int)

interface WeatherApi {
    @GET("data/2.5/weather")
    suspend fun getWeather(
        @Query("q") city: String,
        @Query("appid") key: String,
        @Query("units") metric: String = "metric",
        @Query("lang") lang: String = "ru"
    ): WeatherResponse
}
```
:::

Gson сам разложит JSON по этим data class — имена полей совпали, и магия происходит без вашего участия.

#### 3. Три состояния экрана: загрузка / успех / ошибка

Душа сетевого приложения — «управление состояниями». Медленная сеть, нет интернета, опечатка в названии города… В каждом случае интерфейс обязан объясниться с пользователем. Изящно опишите это через sealed class (запечатанный класс):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Состояние интерфейса</span><span class="dots">···</span>
:::

```
sealed class UiState {
    object Loading : UiState()                    // крутится спиннер
    data class Success(val data: WeatherResponse) : UiState()  // успех
    data class Error(val message: String) : UiState()          // ошибка
}

// Внутри ViewModel:
fun search(city: String) {
    viewModelScope.launch {
        _state.value = UiState.Loading
        _state.value = try {
            UiState.Success(api.getWeather(city))
        } catch (e: Exception) {
            UiState.Error("Не удалось найти этот город — попробуйте другое название?")
        }
    }
}

// В интерфейсе:
when (val s = state) {
    is UiState.Loading -&gt; CircularProgressIndicator()   // спиннер
    is UiState.Success -&gt; WeatherContent(s.data)        // показываем
    is UiState.Error -&gt; Text(s.message)                 // ошибка
}
```
:::

Трёхчастная схема Loading/Success/Error — «универсальная мазь» сетевых экранов: вызубрите её, а дальше во всех сетевых приложениях делайте по этому лекалу.

#### 4. Боевой код интерфейса: рисуем погоду

Состояния готовы; интерфейс выглядит так (ключевые фрагменты):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Экран погоды (ключевой фрагмент)</span><span class="dots">···</span>
:::

```
@Composable
fun WeatherContent(data: WeatherResponse) {
    Column(
        Modifier.fillMaxSize().padding(24.dp),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text(data.name, fontSize = 28.sp, fontWeight = FontWeight.Bold)
        Text(
            "${data.main.temp}°C",
            fontSize = 72.sp,
            fontWeight = FontWeight.Light
        )
        Text(
            data.weather.firstOrNull()?.description ?: "Неизвестно",
            fontSize = 20.sp,
            color = Color.Gray
        )
        Spacer(Modifier.height(16.dp))
        Row {
            Text("💧 Влажность ${data.main.humidity}%")
            Spacer(Modifier.width(24.dp))
            Text("🌡️ Ощущается как ${data.main.temp}°C")
        }
    }
}
```
:::

Несколько мелочей, у которых стоит поучиться: firstOrNull() безопасно берёт первый элемент (список может быть пуст), ?: "неизвестно" подставляет запасной текст — принцип null-безопасности действует и в интерфейсе. Температура набрана крупно, 72.sp, а «лёгкое» начертание (Light) делает цифры изящными — классический рецепт погодных приложений.

#### 5. Детали интерфейса и взаимодействия

- Поле поиска: TextField сверху; вводите город и жмёте «Найти» (задайте на клавиатуре действие «Поиск» — Enter сразу запускает);
- Карточка погоды: крупная температура (26.5°), описание погоды (ясно), влажность, название города;
- Избранные города: часто просматриваемые города храните в DataStore — при следующем открытии запрос уходит сам; заодно повторите главу 6;
- Обновление потягиванием: в Compose есть PullToRefreshBox (из Material 3) — и ощущение сразу «как в профессиональном приложении».

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Совет: картинки оживляют интерфейс

{class="mt-1"}
Подберите каждому типу погоды emoji или значок (☀️🌧️❄️) и свяжите через when(description) — три строки кода, а «тепло» интерфейса удваивается. Можно подключить и стороннюю библиотеку значков погоды, но для тренировки emoji хватает.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Практика: чек-лист приёмки приложения погоды

{class="mt-1"}
① Погода нормально ищется; ② при выключенной сети приложение изящно сообщает об ошибке и не падает (проверьте в режиме полёта!); ③ несуществующий город — дружелюбная подсказка; ④ два города в избранном остаются после перезапуска; ⑤ поворот экрана не теряет состояние. Пять из пяти — проект считается оконченным.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Коротко о главном

- Сначала опробуйте API в браузере и разберите JSON, потом пишите код — «подготовка» ещё никого не подводила
- API-ключ прячьте в local.properties и ни за что не кладите в репозиторий
- Интерфейс Retrofit + data class: имена полей совпали — JSON разобрался сам
- Трёхчастное состояние Loading/Success/Error — универсальная мазь сетевых экранов
- Нет сети, пустой ввод, город не существует — обработка ошибок это проходной балл сетевого приложения
:::
