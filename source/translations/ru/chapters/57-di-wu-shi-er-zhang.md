---
id: di-wu-shi-er-zhang
num: 52
part: an-zhuo-kai-fa-pian
nav: Глава 52: Четыре основных компонента и жизненный цикл Activity
toc: default
kind: chapter
---

### Глава 52. Четыре компонента и жизненный цикл Activity

{class="chapter-intro mb-4"}
Если Compose — «лицо» приложения, то эта глава о его «скелете». В Android есть четыре базовых компонента, из которых собрано любое приложение; а у важнейшего из них, Activity, есть «карта жизненного цикла», которую каждый Android-разработчик обязан вырезать на памяти. Осилив главу, вы наконец поймёте вечные загадки вроде «почему после сворачивания моё приложение забыло всё своё состояние».

#### 1. Четыре компонента: несущие опоры Android

Официально в Android определены четыре базовых компонента; каждый отвечает за свой класс задач:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Компонент</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Обязанность</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Для наглядности</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activity</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Видимый экран</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Витрина магазина — её видно, с ней взаимодействуют</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Service</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">«Невидимка», работающая в фоне</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Складской рабочий — играет музыку, качает файлы, экран ему не нужен</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BroadcastReceiver</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Принимает системные оповещения</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Проходная — «рупор» вестей вроде «батарея садится» или «сеть пропала»</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ContentProvider</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Делится данными между приложениями</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Общий архив — например, открывает контакты другим приложениям</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Четыре компонента Android: краткий обзор

В роли новичка 95% времени вы будете возиться с Activity; Service и BroadcastReceiver понадобятся для музыки и push-уведомлений; ContentProvider нужен реже всего (типовые данные система уже упаковала). И учтите: все четыре компонента обязаны «прописаться» в AndroidManifest.xml — непрописанных система не найдёт.

#### 2. Жизненный цикл Activity: первая «карта сокровищ» Android-разработчика

Приложение на телефоне могут прервать в любой момент: звонок, пользователь ушёл ответить в WeChat, системе не хватило памяти, и она вас убила… Жизнь Activity — вечное странствие по этой карте:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onCreate (рождение: инициализация)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onStart (виден)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onResume (на переднем плане, взаимодействие)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onPause (частично перекрыт)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onStop (полностью скрыт)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center">onDestroy (уничтожен)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">🔁 onRestart / onStart / onResume: при возврате на передний план — обратный путь</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Рисунок 4. Жизненный цикл Activity (по ходу: верхний ряд — рождение → нижний ряд — уход; обратно — тем же путём)
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Колбэк</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Когда срабатывает</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Типичное применение</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onCreate</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">При создании Activity (один раз)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Загрузка интерфейса, инициализация данных</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStart</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Интерфейс стал видимым</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Запуск нетяжёлой логики</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onResume</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Получен фокус, можно взаимодействовать</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Запуск анимаций, продолжение воспроизведения</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onPause</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Экран частично перекрыт / момент ухода с него</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Пауза анимаций, сохранение черновика</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStop</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Полностью невидим</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Освобождение тяжёлых ресурсов, пауза загрузок</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onDestroy</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Перед уничтожением</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Финальная уборка</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Типичное применение шести колбэков жизненного цикла

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Осторожно: поворот экрана «убивает» Activity

{class="mt-1"}
Классическое фиаско новичка: повернулся экран — и весь текст в полях ввода исчез. Причина: по умолчанию поворот экрана уничтожает и заново создаёт Activity (проходит цикл onDestroy → onCreate). Решение: сохраняйте состояние через rememberSaveable (замена remember в Compose) — при пересоздании он сам вернёт значения. Пригодится и в главах 6, и в главе 7.
:::

#### 3. Intent: «билет» на поездку из приложения и внутрь него

Intent («намерение») — «билет» для общения компонентов. Хотите перейти с экрана на экран, открыть браузер или вызвать камеру — сначала «купите билет и сядьте в вагон»:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Переход с помощью Intent</span><span class="dots">···</span>
:::

```
// Способ 1: явный Intent — прямо указываем, на какой экран идти
val intent = Intent(this, DetailActivity::class.java)
intent.putExtra("name", Иван)     // везём с собой «багаж» (данные)
startActivity(intent)

// Способ 2: неявный Intent — говорим, что сделать, система ищет исполнителя
val web = Intent(Intent.ACTION_VIEW, Uri.parse("https://developer.android.com"))
startActivity(web)   // система откроет браузер / или предложит выбрать
```
:::

У двух способов разные роли: явный (explicit) — для переходов между экранами своего приложения; неявный (implicit) — чтобы обратиться к возможностям системы или чужих приложений (открыть сайт, позвонить, поделиться). В Compose-проекте возьмите Context через LocalContext.current прямо в Composable — и вызывайте startActivity.

#### 4. Несколько экранов и навигация

В настоящих приложениях экранов много. Официально рекомендованное для Compose навигационное решение — Navigation Compose (библиотека androidx.navigation):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Каркас Navigation Compose</span><span class="dots">···</span>
:::

```
val navController = rememberNavController()

NavHost(navController, startDestination = "home") {
    composable("home") { HomeScreen(navController) }
    composable("detail/{name}") { entry ->
        val name = entry.arguments?.getString("name")
        DetailScreen(name ?: "Неизвестно")
    }
}

// Переход внутри экрана:
navController.navigate("detail/Иван")     // с аргументами
navController.popBackStack()              // назад
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Совет: экранов становится много — что делать?

{class="mt-1"}
Когда проект вырастет, соберите все маршруты экранов в одном файле (например, AppNavGraph.kt) и управляйте ими централизованно — не раскидывайте логику «куда перейти» по разным экранам. Это первый шаг от «работает» к «легко поддерживать».
:::

#### 5. Заодно знакомимся: что такое Fragment (и почему книга его не преподаёт)

В старых учебниках вы непременно наткнётесь на Fragment — «переиспользуемый кусочек интерфейса» внутри Activity, абсолютную звезду старой многоэкранной архитектуры. Но в эпоху Compose для экранов хватает Composable-функций и маршрутов Navigation, и официально роль Fragment ослабла. Поэтому основная линия книги его обходит.

Мой совет: в новых проектах сами Fragment не тащите; но при чтении старого кода или вопросе на собеседовании достаточно знать, что это «кусочек интерфейса, встроенный в Activity». Учебные материалы всегда берите не старше 2023 года — «старый календарь» Android-стека обновляется быстрее, чем кажется.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Практика: научите счётчик «помнить»

{class="mt-1"}
Доработайте счётчик из главы 51: ① замените remember на rememberSaveable и, повернув экран, проверьте, что число на месте; ② добавьте кнопку «О программе», которая через Navigation ведёт на второй экран с номером версии; ③ добавьте в onCreate/onPause обоих экранов вывод в журнал (Log.d) и понаблюдайте в Logcat за порядком вызовов жизненного цикла. Сделаете эти три шага — и жизненный цикл перестанет быть абстракцией.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Коротко о главном

- Четыре компонента: Activity (витрина), Service (фон), BroadcastReceiver (рупор), ContentProvider (архив)
- Шесть колбэков жизненного цикла: onCreate → onStart → onResume → onPause → onStop → onDestroy
- Поворот экрана уничтожает и пересоздаёт Activity: спасайте состояние через rememberSaveable
- Intent — «билет»: явный ведёт на свои экраны, неявный зовёт возможности системы
- Несколько экранов — через Navigation Compose: NavHost + маршруты composable
:::
