---
id: di-si-shi-ba-zhang
num: 48
part: an-zhuo-kai-fa-pian
nav: Глава 48: Знакомство с Android — от операционной системы к экосистеме разработки
toc: default
kind: chapter
---

### Глава 48: Знакомство с Android — от операционной системы до экосистемы разработки

{class="chapter-intro mb-4"}
Поздравляем с этим решением — из «человека, который пользуется телефоном» стать «человеком, который делает приложения». Прежде чем браться за дело, расстелим карту: откуда взялся Android? Почему разработчики всего мира пишут для него приложения? Что происходит между моментом, когда вы стучите по клавиатуре, и появлением приложения на телефоне пользователя?

#### 1. Происхождение Android: от «маленького робота» до «крупнейшей системы мира»

История Android началась в 2003 году: инженер Энди Рубин основал компанию Android Inc. с простой целью — создать умную операционную систему, «лучше понимающую камеры». В 2005 году её купил Google, в 2007-м вместе с несколькими десятками производителей был создан альянс Open Handset Alliance (OHA), а в сентябре 2008 года официально поступил в продажу первый Android-смартфон — HTC Dream (G1).

Дальнейшее вы знаете: к 2026 году Android — мобильная операционная система с самой большой долей рынка в мире, а активных устройств — миллиарды. Ваш телефон, ТВ-приставка, экран в машине, умные часы — почти наверняка работают на Android. Что это значит? Что каждая написанная вами строка кода может дойти до самого широкого круга людей на планете.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Совет: открытые корни Android

{class="mt-1"}
Ядро Android (AOSP, Android Open Source Project) открыто: любой производитель может взять его и переделать под себя. Поэтому у Xiaomi есть MIUI (теперь HyperOS), у Huawei — слой совместимости HarmonyOS, у Samsung — One UI. Для разработчика это благо: вы изучаете «разработку под Android», а не «разработку под конкретный бренд» — одно умение работает на всех.
:::

Забавна и эволюция номеров версий: начиная с 1.5 Cupcake («капкейк») каждая крупная версия носила имя десерта — пончик, эклер, замороженный йогурт, пряничный человечек… И только Android 10 в 2019 году перешла на сухие цифры. На август 2026 года последняя официальная версия — Android 17, а «минимально поддерживаемая версия», которая действительно важна при разработке, у массовых приложений обычно между Android 8 (API 26) и Android 10 (API 29): поддерживая устройства последних нескольких лет, вы охватываете достаточно большую аудиторию.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Версия</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Кодовое имя / год</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Важное для разработчика</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 8 (API 26)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Oreo · 2017</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Каналы уведомлений, ограничения фоновой работы — нижняя планка для многих старых устройств</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 10 (API 29)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2019</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Появилось изолированное хранилище (scoped storage), правила доступа к файлам сильно изменились</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 12 (API 31)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2021</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Динамические цвета Material You — большой шаг вперёд в облике интерфейса</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 13 (API 33)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2022</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Разрешение на уведомления в рантайме: система спрашивает, «разрешать ли присылать уведомления»</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 14-15 (API 34-35)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2023-2024</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Прогнозируемое возвращение, страницы по 16 КБ, дальнейшее ужесточение приватности</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 16-17 (API 36-37)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2025-2026</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Более частые минорные релизы, интеграция ИИ-возможностей (например, расширения Gemini)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Краткая история версий Android (на август 2026 года; главные вехи для разработки)

#### 2. На каком языке писать: Java или Kotlin?

За историю разработки под Android сменились два основных языка. Java — «ветеран-основатель»: она была с Android с самого рождения. Kotlin — объявленный Google в 2017 году «гражданином первого сорта», а с 2019 года официальная линия — «Kotlin-first». К 2026 году новые проекты почти все пишут на Kotlin, а старые постепенно мигрируют.

Скажем честно: если вы совсем новичок, учите сразу Kotlin и не оглядывайтесь на Java. Причины три. Первая: кода на Kotlin на 30–40% меньше, чем на Java (та же функциональность — короче и яснее). Вторая: Kotlin от природы защищает от «нулевых указателей» — кошмара новичков. Третья: все современные уроки, официальная документация и ИИ-инструменты для программирования (помните нашу книгу о программировании с ИИ?) ориентированы на Kotlin. Java встретится лишь при сопровождении старых проектов и чтении старого кода.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Стиль Java (многословный)

{class="font-mono text-xs leading-relaxed"}
public class MainActivity extends Activity {<br>&nbsp;&nbsp;@Override<br>&nbsp;&nbsp;protected void onCreate(Bundle b) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b);<br>&nbsp;&nbsp;&nbsp;&nbsp; setContentView(R.layout.activity);<br>&nbsp;&nbsp;}<br>}
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Стиль Kotlin (лаконичный)

{class="font-mono text-xs leading-relaxed"}
class MainActivity : ComponentActivity() {<br>&nbsp;&nbsp;override fun onCreate(b: Bundle?) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b)<br>&nbsp;&nbsp;&nbsp;&nbsp;setContent { App() }<br>&nbsp;&nbsp;}<br>}
:::
:::

Одно и то же действие, а в Kotlin минус куча фигурных скобок и шаблонных строк. В главе 50 мы займёмся им всерьёз, а пока запомните: «общий язык» разработки под Android называется Kotlin.

#### 3. Как рождается приложение?

Многие думают, что «разработка приложения» — это сесть за компьютер и лихорадочно писать код. На самом деле от идеи до телефона пользователя приложение проходит примерно такой конвейер:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-lightbulb mr-1"></i> Идея</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center">📐 Проектирование (интерфейс + функции)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-keyboard mr-1"></i> Пишем код</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hammer mr-1"></i> Сборка (APK/AAB)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Тесты (эмулятор + реальное устройство)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-rocket mr-1"></i> Публикация (магазин/установщик)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Рисунок 1: полный путь Android-приложения — от идеи до полки магазина
:::

В этом процессе есть два понятия, которые нужно усвоить прямо сейчас:

- APK: формат установочного пакета Android-приложения (.apk) — как .exe в Windows: его можно поставить на телефон. Годится для собственных тестов и «перебросить другу поиграть».
- AAB: Android App Bundle (.aab) — «продвинутый формат упаковки» для публикации в Google Play. Магазин динамически подрезает пакет под модель телефона пользователя, чтобы каждый скачивал меньше. Самому установить его нельзя — только через магазин.

И ещё один термин, который будет звучать постоянно: SDK (Software Development Kit — комплект средств разработки). Это весь набор «экипировки» от Android: API-библиотеки разных версий, отладочные инструменты, образы эмулятора и т. д. Классы вроде Activity и Button, которые вы вызываете в коде, приходят именно из SDK.

#### 4. Панорама технологий Android: ваш «список вооружений»

Перед началом обучения познакомьтесь со стандартным набором типичного Android-проекта 2026 года. Если сейчас список непонятен — не страшно: перечитаете его после всей книги, и всё встанет на свои места:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Слой</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Основной выбор (2026)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Для чего нужен</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Язык</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin 2.x</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Язык написания логики</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Интерфейс</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jetpack Compose + Material 3</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Интерфейс рисуется кодом (главная линия книги)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Архитектура</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MVVM + ViewModel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Разделяет интерфейс и логику — код не превращается в кашу</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Хранение данных</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room (база данных) + DataStore (настройки)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Сохраняет данные на телефоне</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Сеть</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit + OkHttp + корутины Kotlin</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Общение с сервером</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Инструмент сборки</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle + Kotlin DSL</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Превращает код в установочный пакет</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Среда разработки</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Официальная IDE-«всё в одном» от Google</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Основной стек Android-разработки 2026 года одним взглядом

Не пугайтесь этого набора английских слов. Он как кастрюли и половники на кухне: сейчас достаточно знать, что «готовить надо на кухне», а как пользоваться каждым инструментом — разберём по главам, один за другим. И хорошая новость: при создании нового проекта Android Studio сама настроит весь этот набор — вам останется только «жарить».

#### 5. Android против iOS: первый «урок выбора стороны» для разработчика

Возможно, у вас в руках и Android, и устройство Apple. Как разработчику стоит заранее знать разницу в опыте с двух сторон — это не «какая платформа лучше», а трезвый расчёт, «с какой стороны вам удобнее начать»:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Критерий</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Разработка под Android</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Разработка под iOS</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Компьютер для разработки</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Подходит Windows / Mac / Linux</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Только Mac (Xcode эксклюзивен)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Инструмент разработки</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio (бесплатно)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode (бесплатно) + 99 долларов в год за публикацию</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Проверка при публикации</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Мягкая: от нескольких часов до пары дней</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Строгая: 1–7 дней — обычное дело</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Установка на устройство и тесты</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">APK распространяется и ставится свободно</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Распространение ограничено: для тестов нужны подпись / TestFlight</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Условия заработка</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">В основном реклама / локальные магазины</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">В App Store привычка платить за внутренние покупки лучше</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Стоимость обучения</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Понятий больше (четыре главных компонента и т. д.)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Экосистема закрытая, но целостная, документация отличная</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Сравнение путей разработки под Android и iOS (август 2026 года)

Скажем честно: если ваш компьютер не Mac, выбирать не из чего — Android единственный вариант. Если Mac есть, восьмую и девятую части этой книги можно читать параллельно: логика программирования общая, и после освоения одной стороны вторая пойдёт куда быстрее.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Попробуйте сами: посмотрите на «Android» в своём телефоне

{class="mt-1"}
Откройте в телефоне [Настройки] → [О телефоне] (или «Об этом устройстве») и найдите строку «Версия Android» — нажмите на неё несколько раз подряд, и сработает пасхалка: мини-игра от системы. Запишите номер своей версии и сверьтесь с таблицей выше: к какому поколению относится ваш телефон. Ваш телефон и станет первым «тестовым устройством» для разработки.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Краткие итоги главы

- Android родился в 2008 году; к 2026-му — мобильная система с самой большой долей рынка в мире, миллиарды активных устройств
- Последняя официальная версия — Android 17; массовые приложения поддерживают минимум Android 8–10 — так больше пользователей
- Новые проекты — всегда на Kotlin: кода на 30%+ меньше, защита от нулевых указателей, официальный выбор
- APK — для установки самому, AAB — для магазина; SDK — официальный набор для разработки
- Стандартный стек 2026: Kotlin + Compose + MVVM + Room + Retrofit + Gradle + Android Studio
:::
