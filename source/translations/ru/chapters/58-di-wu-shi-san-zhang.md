---
id: di-wu-shi-san-zhang
num: 53
part: an-zhuo-kai-fa-pian
nav: Глава 53: Хранение данных и сетевые запросы
toc: default
kind: chapter
---

### Глава 53. Хранение данных и сетевые запросы

{class="chapter-intro mb-4"}
Приложение, которое умеет лишь «показывать», — мёртвое; живым его делают умение сохранять данные и выходить в сеть. В этой главе знакомимся с «тройкой» слоя данных Android: DataStore (хранит мелкие настройки), Room (хранит структурированные данные), Retrofit (говорит с сервером) — плюс их «главный диспетчер», корутины. Осилив главу, вы сможете писать настоящие приложения, которые помнят привычки пользователя и обновляют содержимое на лету.

#### 1. Как выбрать хранилище: сначала взгляните на таблицу

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Решение</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Что удобно хранить</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Особенности</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Где применяется в книге</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DataStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Разрозненные настройки (тема, переключатели)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Пары «ключ — значение», просто и надёжно</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Настройки учётной книги, глава 54</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Структурированные данные (записи, пользователи)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Настоящая обёртка над базой SQLite, умеет делать запросы</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Записи расходов, глава 54</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">(не хранит, берёт из сети) данные с сервера</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Фактический стандарт среди библиотек HTTP-запросов</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Данные о погоде, глава 55</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Как делят работу три инструмента хранения

Заучите присказку: «мелкие настройки — в DataStore, данные пачками — в Room, внешние данные — через Retrofit». Привычный по старым учебникам SharedPreferences вытеснен DataStore, а рукописный SQL для SQLite — Room: учитесь сразу новому, не топчитесь по старой колее.

#### 2. DataStore: храним мелкие настройки

Хотите запоминать разрозненные значения вроде «валюта, выбранная в прошлый раз» или «включён ли тёмный режим»? Берите DataStore (вариант Preferences):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Пример DataStore</span><span class="dots">···</span>
:::

```
val Context.dataStore by preferencesDataStore(name = "settings")

// Запись: сохраняем значение
suspend fun saveTheme(isDark: Boolean) {
    context.dataStore.edit { prefs ->
        prefs[THEME_KEY] = isDark
    }
}

// Чтение: достаём (Flow сам сообщит об изменениях)
val themeFlow: Flow<Boolean> = context.dataStore.data
    .map { it[THEME_KEY] ?: false }
```
:::

Обратите внимание: возвращается Flow — «текущий» поток данных. Значение изменилось — и все, кто за ним наблюдает, автоматически получают новое. Эта идея (реактивность) — краеугольный камень современного Android; практика будет в главе 54.

#### 3. Room: строим для данных «настоящий дом»

В учётной книге сотни и тысячи записей, да ещё нужны запросы и статистика по категориям и месяцам — без базы данных не обойтись. Room — официальная обёртка над SQLite: она делает «создание таблиц и выборки» таким же естественным, как написание Kotlin. Нужны три вещи:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Триада Room: Entity / Dao / Database</span><span class="dots">···</span>
:::

```
// 1. Entity: структура таблицы (одна таблица = один data class)
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val amount: Double,
    val category: String,
    val note: String,
    val date: String
)

// 2. Dao: интерфейс операций (CRUD)
@Dao
interface RecordDao {
    @Query("SELECT * FROM records ORDER BY date DESC")
    fun getAll(): Flow<List<Record>>

    @Insert
    suspend fun insert(record: Record)

    @Delete
    suspend fun delete(record: Record)

    @Query("SELECT SUM(amount) FROM records WHERE category = :c")
    suspend fun sumByCategory(c: String): Double
}

// 3. Database: общая сборка
@Database(entities = [Record::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun recordDao(): RecordDao
}
```
:::

Этот шаблон «тройки» можно целиком переносить в любой ваш проект — поменяйте имена полей и готово. Запросы возвращают Flow, и интерфейс сам обновляется вслед за данными. Прелесть!

#### 4. Retrofit: разговор с сервером

Погода, новости, курсы валют… Этих данных в телефоне нет — они на чужих серверах. Retrofit превращает «попросить данные у сервера» в нечто столь же простое, как вызов функции. Три шага:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Retrofit за три шага</span><span class="dots">···</span>
:::

```
// 1. Определяем интерфейс: описываем HTTP-запросы как функции
interface WeatherApi {
    @GET("v1/weather")
    suspend fun getWeather(@Query("city") city: String): WeatherResponse
}

// 2. Создаём экземпляр
val api = Retrofit.Builder()
    .baseUrl("https://api.example.com/")
    .addConverterFactory(GsonConverterFactory.create())
    .build()
    .create(WeatherApi::class.java)

// 3. Вызываем как обычную функцию (в корутине)
val result = api.getWeather("Пекин")
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Осторожно: два железных правила сетевой работы

{class="mt-1"}
① Сетевые запросы нельзя выполнять в главном потоке — интерфейс замрёт или приложение упадёт (NetworkOnMainThreadException). Все сетевые вызовы обязаны жить в корутинах (viewModelScope.launch). ② Открытый HTTP по умолчанию запрещён: начиная с Android 9 требуется HTTPS. Если для тестов нужен локальный адрес http://, придётся явно объявить usesCleartextTraffic в Manifest — но в настоящем продукте всё должно ходить только по HTTPS.
:::

#### 5. Разбор JSON: «переводим» сетевые данные

Большинство данных с сервера приходит в JSON — текст, похожий на «вложенный словарь». Retrofit нужен «переводчик», который превратит его в объекты Kotlin. Два главных решения 2026 года:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Решение</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Особенности</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Когда выбирать</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gson / Moshi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Проверенное временем решение на рефлексии, настраивать нечего</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Быстрый старт, небольшие проекты с малым числом полей</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">kotlinx.serialization</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Официальное решение с обработкой на этапе компиляции: быстрее и безопаснее</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Первый выбор для новых проектов (мейнстрим 2026 года)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Два главных решения для разбора JSON

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Пример kotlinx.serialization</span><span class="dots">···</span>
:::

```
// Добавляем data-классу аннотацию @Serializable
@Serializable
data class WeatherResponse(
    val weather: List<Weather>,
    val main: Main,
    val name: String
)

// Подключаем к Retrofit соответствующий Converter (официальная поддержка с Retrofit 2.11+):
// .addConverterFactory(json.asConverterFactory("application/json".toMediaType()))
```
:::

При любом решении железное правило одно: сначала изучите реальный JSON-ответ, потом описывайте поля. Множество багов «не парсится» рождаются из опечаток в именах полей и неверно угаданной вложенности — распечатайте исходный JSON и сверьтесь — через десять секунд виновник найден.

#### 6. Корутины: «общий язык» многозадачности Android

Снова и снова мелькавшие выше suspend и launch родом из корутин Kotlin (Coroutine) — официального механизма многозадачности Android. Грубо говоря, это способ дать операциям «с ожиданием» (сеть, база данных) не блокировать интерфейс.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Первое знакомство с корутинами</span><span class="dots">···</span>
:::

```
// Запускаем корутину в ViewModel
viewModelScope.launch {
    val records = dao.getAll().first()  // suspend: сам приостановится и подождёт
    // обновляем состояние интерфейса…
}

// Шпаргалка по ключевым словам:
// suspend   — «мне надо подождать, не мешайте другим»
// launch    — «За работу!»
// viewModelScope — «рабочая», привязанная к экрану; закрывается сама при уничтожении экрана
```
:::

Если вы начинаете с нуля — просто запомните, как этим пользоваться; принцип «приостановил и продолжил» можно изучить позже. 90% вашего повседневного кода — именно этот шаблон.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Практика: мини-приложение «фраза дня»

{class="mt-1"}
Найдите бесплатный API цитат (например, hitokoto или похожий), через Retrofit подтягивайте «фразу дня» и показывайте её в центре экрана, добавьте кнопку «Ещё» (новый запрос в корутине). Любимые фразы складывайте в «избранное» через Room. Это упражнение прогоняет через DataStore/Room/Retrofit/корутины всё сразу — сделаете его, и главы 7 и 8 пройдёте как по маслу.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Коротко о главном

- Присказка: мелкие настройки — в DataStore, данные пачками — в Room, внешние данные — через Retrofit
- DataStore возвращает Flow: значение поменялось — наблюдатели узнали сами
- Тройка Room: @Entity (таблица) + @Dao (операции) + @Database (общая сборка) — шаблон можно брать как есть
- Три шага Retrofit: объявить интерфейс → создать экземпляр → вызвать в корутине
- Два железных правила: сеть — не в главном потоке; в настоящем продукте — только HTTPS
- Корутина = ожидание, не блокирующее интерфейс; viewModelScope — личный рабочий кабинет экрана
:::
