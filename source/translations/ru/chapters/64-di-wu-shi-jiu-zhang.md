---
id: di-wu-shi-jiu-zhang
num: 59
part: ios-kai-fa-pian
nav: Глава 59: Знакомство с iOS — экосистема Apple и экосистема разработки
toc: default
kind: chapter
---

### Глава 59. Знакомство с iOS — экосистема Apple и экосистема разработки

{class="chapter-intro mb-4"}
Поздравляем с этим решением — перейти от «человека, который пользуется iPhone» к «человеку, который пишет приложения для iPhone». Прежде чем браться за дело, разложим карту: откуда взялся iOS? Что значит для разработчика «сад с высокими стенами» Apple? Что происходит между моментом, когда ваши пальцы стучат по клавиатуре, и появлением приложения на телефоне пользователя?

#### 1. Происхождение iOS: один телефон, изменивший целую отрасль

В январе 2007 года Стив Джобс на презентации достал из кармана первый iPhone. Тогда он даже не поддерживал сторонние приложения — и только в 2008 году Apple выпустила App Store и iPhone SDK, разрешив разработчикам со всего мира писать программы для iPhone. В тот момент родилась «экономика приложений»: сегодня в App Store миллионы приложений, а суммарные выплаты разработчикам превысили сотни миллиардов долларов.

Сама система тоже эволюционировала: сначала она называлась iPhone OS, в 2010 году сменила имя на iOS; номера версий дошли до iOS 17 (2023), а в 2025 году Apple перевела именование на «годовой» принцип — iOS 26 вышла в 2025 году, а текущая версия в августе 2026-го — iOS 27. Названия меняются, но одно не менялось никогда: привычка пользователей iOS платить и репутация качества приложений по праву считаются лучшими в мобильной экосистеме — одно и то же приложение на iOS часто приносит заметно больший доход, чем на Android.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Событие</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Год</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Что важно для разработчиков</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Запуск App Store</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2008</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Открытие экосистемы сторонней разработки</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Выпуск Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2014</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Появление современного языка разработки для iOS</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Выпуск SwiftUI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2019</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Декларативный фреймворк интерфейсов, основная линия этой книги</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">iOS 26 (первый год нового именования)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2025</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Названия привязаны к году; повсеместная интеграция Apple Intelligence</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">iOS 27</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2026</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Текущая новейшая версия (ориентир этой книги)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Ключевые вехи разработки iOS (по август 2026 года)

#### 2. Сад с высокими стенами: «правила» и «дивиденды» экосистемы Apple

Экосистему Apple часто описывают как «сад с высокими стенами» (Walled Garden) — правил много, контроль строгий: приложение должно пройти проверку, чтобы попасть в магазин; разработка возможна только на Mac и в Xcode; распространение идёт в основном через App Store. Звучит тесновато? Но для разработчика эти правила приносят вполне осязаемые дивиденды:

- Крайне малая фрагментация устройств: моделей iPhone всего несколько, размеры экранов и версии системы очень однородны — адаптировав 5 моделей, вы охватите 95% пользователей (на Android может понадобиться несколько десятков);
- Очень высокая скорость обновления системы: в течение нескольких недель после выхода новой версии её устанавливают 70–80% пользователей, так что новыми API можно смело пользоваться, не оглядываясь на «систему пятилетней давности»;
- Хорошая привычка платить: пользователи App Store охотнее тратят деньги на приложения и встроенные покупки;
- Проверка строгая, зато магазин чистый: подделок и вредоносных программ мало, и хорошим продуктам легче быть замеченными.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Внимание: сначала о затратах

{class="mt-1"}
У разработки под iOS есть жёсткий барьер: нужен Mac (Xcode существует только для macOS), а для публикации — аккаунт разработчика за 99 долларов в год (бесплатный аккаунт физлица позволяет отлаживать на реальном устройстве локально, но не публиковать приложение). Трезво оцените эти вложения перед стартом — впрочем, хорошая новость: на этапе обучения бесплатного аккаунта вполне достаточно, об этом расскажем в главе 60.
:::

#### 3. На каком языке писать: Objective-C или Swift?

В истории разработки под iOS тоже было два «главных героя». Objective-C — ветеран-основатель: использовался с 2008 по 2014 год; Swift — новый язык Apple, представленный в 2014-м и с тех пор доросший до Swift 6 (релиз 2024 года со строгой проверкой конкурентности). К 2026 году почти все новые проекты пишутся на Swift.

Честное слово новичку, начинающему с нуля: учите сразу Swift, а Objective-C даже не открывайте — разве что на работе вам достанется поддерживать legacy-код десятилетней давности. Плюсы Swift: чистый синтаксис (никакого багажа эпохи C — точек с запятой и заголовочных файлов), механизм опциональных значений (Optional), искореняющий «падения из-за нулевых указателей» на уровне языка, бесшовная работа со SwiftUI, а ещё Swift Playgrounds на iPad — можно учиться, играя.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Стиль Objective-C (древние руины)

{class="font-mono text-xs leading-relaxed"}
NSString *name = @"Иван"; [name stringByAppendingString:@"Привет"]; // квадратные скобки + указатели + точка с запятой — классическая троица
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Стиль Swift (современный и лаконичный)

{class="font-mono text-xs leading-relaxed"}
var name = "Иван" name += "Привет" // просто и понятно, как естественный язык
:::
:::

#### 4. Как рождается приложение?

Как и на любой платформе, у приложения iOS есть свой конвейер. Но в версии Apple к нему добавлены две «процедуры досмотра»:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-lightbulb mr-1"></i> Идея</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center">📐 Проектирование (интерфейс + функции)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-keyboard mr-1"></i> Пишем код (Swift + SwiftUI)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hammer mr-1"></i> Сборка и подпись</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Тесты (эмулятор + реальное устройство)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-stamp mr-1"></i> Проверка Apple</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> Публикация в App Store</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Рисунок 1. Полный путь приложения iOS от идеи до полки магазина (обратите внимание на дополнительный этап «проверка»)
:::

Ключевые понятия этого процесса:

- Подпись (Signing): каждое приложение iOS должно быть «подписано», чтобы его можно было установить, — это доказательство того, что «пакет исходит от вас и не был подделан». На этапе обучения Xcode автоматически подписывает приложения вашим Apple ID; для публикации используется сертификат разработчика. Подробнее — в главе 67.
- Симулятор (Simulator): виртуальный iPhone на Mac, главная арена разработки и отладки. Он работает на процессоре Mac, поэтому особенно плавный — по ощущениям заметно лучше эмулятора Android.
- TestFlight: официальное средство Apple для «раздачи бета-версий» — до публикации тестовую версию получают до 10 000 тестеров, которые устанавливают её через приложение TestFlight. Это изящное решение, свойственное именно экосистеме iOS.

#### 5. Технологический стек iOS целиком: ваш «арсенал»

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Уровень</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Основной выбор (2026)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Для чего нужен</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Язык</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift 6</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Язык для написания логики</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Интерфейс</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI + дизайн-правила Apple (HIG)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Рисовать интерфейс кодом (основная линия книги)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Архитектура</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MVVM + @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Разделять интерфейс и логику</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Хранение данных</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData (база данных) + UserDefaults (настройки)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Сохранять данные в телефоне</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Сеть</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession + async/await + Codable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Общаться с сервером</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Инструмент сборки</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode Build System / xcodebuild</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Превращать код в установочный пакет</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Среда разработки</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode (только для macOS)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Официальная IDE Apple</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Обзор основного технологического стека iOS в 2026 году

Заметили? Этот список заметно короче андроидовского — потому что Apple многое «берёт на себя». Плата за закрытую экосистему — меньше свободы, а награда — спокойствие: не нужно мучиться выбором сетевой библиотеки или базы данных; то, что даёт Apple, чаще всего и есть оптимальное решение.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Попробуйте сами: посмотрите «яблочный паспорт» своего телефона

{class="mt-1"}
Откройте на iPhone [Настройки] → [Основные] → [Об этом устройстве] и запишите три вещи: версию iOS, название модели и доступный объём. Затем полистайте вкладку «Сегодня» в App Store и присмотритесь к скриншотам и описаниям качественных приложений — с сегодняшнего дня вы смотрите на магазин уже не глазами пользователя, а глазами разработчика.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Краткие итоги главы

- В 2008 году запустился App Store — родилась «экономика приложений»; текущая версия в 2026 году — iOS 27
- Баланс «сада с высокими стенами»: правил много, но устройств мало, версии свежие, пользователи готовы платить, магазин чистый
- Жёсткие барьеры: нужен Mac; для публикации — аккаунт разработчика за 99 долларов в год; на этапе обучения хватит бесплатного аккаунта
- Язык — сразу Swift; Objective-C остаётся достоянием legacy-кода
- У конвейера на один шаг больше, чем у Android: проверка Apple; TestFlight — волшебный инструмент раздачи бета-версий
- Стандартный стек 2026 года: Swift 6 + SwiftUI + MVVM + SwiftData + URLSession + Xcode
:::
