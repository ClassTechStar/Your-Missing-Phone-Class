---
id: di-liu-shi-jiu-zhang
num: 69
part: ios-kai-fa-pian
nav: Глава 69: Справочник и ресурсы
toc: default
kind: chapter
---

### Глава 69. Справочник и ресурсы

{class="chapter-intro mb-4"}
Эта глава — справочник, которым можно пользоваться и отдельно. Забыли, как что-то пишется, или надо быстро принять решение — листайте прямо сюда. Держите его как «карманные карточки»: шпаргалка по ходовому коду, частые вопросы, ресурсы для учёбы — без единой пропущенной страницы.

#### 1. Карточки быстрой справки по ходовому коду

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Что делаем</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ключевой код</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Приватное состояние страницы</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State private var x = начальное значение</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Логика между страницами</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Observable class VM { var x = 0 }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Вертикальная / горизонтальная раскладка</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack { }</code> / <code class="inline">HStack { }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Гибкое пространство</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Spacer()</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Список</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List { ForEach(массив) { ... } }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Переход на другую страницу</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">NavigationStack + NavigationLink</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Всплывающее окно снизу</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">.sheet(isPresented: $show) { содержимое }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Закрыть текущую страницу</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Environment(\.dismiss) var dismiss</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Загрузить данные из сети</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">try await URLSession.shared.data(from: url)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Разобрать JSON</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X: Codable</code> + <code class="inline">JSONDecoder().decode</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Сохранить мелкую настройку</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults.standard.set(значение, forKey: "ключ")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Сохранить структурированные данные</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Model</code> + <code class="inline">modelContainer</code> + <code class="inline">@Query</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Поддержка тёмного режима</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Берите системные цвета (.primary / Color(.systemGray6)), не вшивайте свои</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Запустить тесты</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><kbd>⌘U</kbd></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Карточки быстрой справки по разработке iOS (август 2026)

#### 2. Частые вопросы (FAQ)

В 1: У меня нет Mac — могу ли я изучать разработку под iOS?

Язык изучить можно, полноценная разработка — нет. Swift Playgrounds на iPad/iPhone покрывает весь материал главы 61; но Xcode живёт только на macOS, так что в итоге Mac необходим. При ограниченном бюджете можно на переходный период арендовать облачный Mac или взять б/у Mac mini, а о вложениях решить, когда освоите язык.

В 2: Сколько стоит научиться разработке под iOS?

Этап учёбы: 0 (Xcode бесплатен + бесплатный Apple ID для отладки на устройстве). Этап публикации: аккаунт разработчика 99 долларов в год (около 700 юаней). Плюс вложения в сам Mac — вот и все расходы. А по сравнению с отдачей — даже маленькая утилита в App Store находит платящих пользователей — это выгодная сделка.

В 3: Что учить первым — SwiftUI или UIKit?

SwiftUI. Новые проекты, новые уроки и новые вакансии 2026 года строятся вокруг SwiftUI, и вся книга пользуется именно им. UIKit — фреймворк прошлого поколения, он по-прежнему живёт во множестве старых проектов: когда освоите SwiftUI, доучите UIKit по необходимости (у Apple есть учебники по взаимодействию), вберётся быстро. Только не перепутайте порядок.

В 4: Легко ли найти работу разработчика iOS?

Рынок 2026 года: начальные позиции «умею рисовать интерфейсы» перегреты конкуренцией, но разработчики, которые «знают Swift + SwiftUI и имеют опубликованное приложение», по-прежнему нарасхват. Медианные зарплаты iOS-разработчиков стабильно в верхних строчках среди стеков. Лучшая часть вашего резюме в период учёбы — то приложение в магазине, которое вы сделали сами.

В 5: Приложение отклонили на проверке — что делать?

Не паникуйте, это нормально — вероятность отказа при первой подаче немаленькая. Причины отказа Apple обычно пишет очень конкретно (какая страница, какой пункт правил); исправьте по каждому пункту, ответьте с пояснением в App Store Connect и подайте заново. Три частые причины отказа: непонятно назначение разрешений, в интерфейсе есть баги, метаданные (скриншоты/описание) не соответствуют действительности. Проверьте эти три пункта заранее — сэкономите круг ожидания.

#### 3. Частые горячие клавиши Xcode: шпаргалка

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Действие</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Горячие клавиши</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Запуск / тесты</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R / ⌘U</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Открыть предпросмотр на холсте</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Быстро открыть файл</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Поиск по всему проекту</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘F</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Форматировать отступы</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Закомментировать / раскомментировать</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Очистить кеш сборки</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘K</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Перейти к определению</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘ + щелчок</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Переименовать (безопасно по всему проекту)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Правый клик → Refactor → Rename</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Частые горячие клавиши Xcode: шпаргалка

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Совет: при «мистике» компиляции сперва чистим кеш

{class="mt-1"}
В «полтергейсте» вида «вчера работало, сегодня нет» в шести-семи случаях из десяти виноват перепутанный кеш сборки. ⇧⌘K — очистить и пересобрать: это лечит большую половину мистики. Не помогло — перезапустите Xcode (вместе с Mac), не помогло и это — «удалите папку DerivedData»: таков заветный «тройной приём», передаваемый из уст в уста разработчиками iOS.
:::

#### 4. Рекомендуемые ресурсы для учёбы

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Тип</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ресурс</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Почему стоит</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Официальный</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">developer.apple.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Официальная документация Apple: там и уроки SwiftUI/Swift, авторитет номер один</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Официальный</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI Tutorials от Apple</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Официальный курс «за руку», максимальная дружелюбность к новичкам</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Официальный</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Официальный сайт Swift (swift.org)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Официальная документация языка и онлайн-площадка для упражнений</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Сообщество</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hacking with Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Бесплатная библиотека уроков Paul Hudson, качество общепризнанно в первой лиге</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Сообщество</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stack Overflow (тег swiftui)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Первая станция за помощью при ошибках</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Видео</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Официальный канал Apple Developer (видео WWDC)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Авторитетные разборы новых технологий каждый год</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Дизайн</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Руководство по интерфейсам Apple (HIG)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Официальная библия интерфейсов «с яблочным вкусом»</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">К книге</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Часть 7 «Практика программирования с ИИ» (главы 37–47)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Полное искусство разработки iOS с помощью ИИ</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Список ресурсов для изучения разработки iOS (август 2026)

#### 5. Заключение: от первого приложения к N-му

Оглянитесь назад: от «не знаю, что такое SwiftUI» — до установленного Xcode, освоенного Swift, интерфейса, нарисованного на SwiftUI, подключённой к приложению базы данных и сети, и дальше до тестов, упаковки и публикации — самый трудный отрезок пути «от нуля к единице» вы уже прошли.

Мир технологий меняется быстро: фреймворки обновляются, инструменты сменяются, ИИ забирает всё больше «клавиатурной» работы. Но одно не устареет никогда: ваша способность размытую идею разложить на ясные шаги и шаг за шагом воплотить её. Инструменты — усилители, мышление — фундамент. Усилители можно менять, фундамент не должен шататься.

:::inline div .quote-line
Вы больше не просто «умеющий пользоваться телефоном». Вы можете превратить идеи из головы в настоящие приложения на сотнях миллионов iPhone. С сегодняшнего дня творите с клавиатурой — в этом романтика iOS-разработчика.
:::

#### Список литературы

{class="list-decimal pl-6 mb-3 space-y-1 text-xs text-gray-500"}
1. Apple Inc. (2026). SwiftUI Framework Documentation. developer.apple.com.
2. Apple Inc. (2026). Swift Programming Language Guide. swift.org.
3. Apple Inc. (2026). SwiftData Framework Documentation. developer.apple.com.
4. Apple Inc. (2026). App Store Review Guidelines. developer.apple.com/app-store/review.
5. Apple Inc. (2026). Human Interface Guidelines (HIG). developer.apple.com/design.
6. Apple Inc. (2026). Xcode 27 Release Notes and App Distribution Guide.
