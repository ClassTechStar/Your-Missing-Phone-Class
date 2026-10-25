---
id: di-liu-shi-qi-zhang
num: 67
part: ios-kai-fa-pian
nav: Глава 67: Шлифовка и публикация — выпуск в App Store
toc: default
kind: chapter
---

### Глава 67. Доводка и выпуск — тесты, отладка и публикация в App Store

{class="chapter-intro mb-4"}
Приложение готово — и что дальше? В этой главе три вещи на пути «от запускается» к «можно передавать людям»: как быстро и эффективно отлаживать и ловить баги, как писать тесты против регрессий и как отправить приложение в App Store на скачивание всему миру. Публикация — не просто красивый ритуал: это водораздел между «работой» и «продуктом».

#### 1. Три кита отладки: print, точки останова, предпросмотр

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Инструмент</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Для чего</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Как пользоваться</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">print + консоль</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Смотреть журнал работы</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">В коде print("значение=\(x)"), вывод смотрите в консоли внизу Xcode</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Точки останова</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Остановить программу на нужной строке и посмотреть значения переменных</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Щёлкните рядом с номером строки — появится синяя метка; дойдя до неё, программа замрёт — идите по шагам</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Предпросмотр SwiftUI + отладчик</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Смотреть интерфейс и иерархию представлений вживую</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Холст #Preview + инспектор View Hierarchy во время работы приложения</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Три кита отладки

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Совет: как читать сообщение о падении?

{class="mt-1"}
При падении Swift консоль печатает «Fatal error» с причиной, а Xcode останавливается на сбойной строке и подсвечивает её. Историю падений на реальном устройстве смотрите в Xcode → Window → Organizer → Crashes (нужен платный аккаунт). Ключевые слова для поиска берите в формате «первая фраза причины ошибки + swiftui» — точный вопрос рождает точный ответ.
:::

#### 2. Тесты: страховка для кода

Ручная проверка ненадёжна: починили одну функцию — тихо сломалась соседняя. Тесты — это и «таблетка от сожалений», и «бронежилет». В iOS фреймворк XCTest, двух разновидностей:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Уровень</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Что проверяет</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Target</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Скорость</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Модульные тесты</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Чистая логика (вычисления, проверки)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppTests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Секунды</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UI-тесты</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Поведение настоящего интерфейса</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppUITests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Минуты</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ручное тестирование</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Впечатления живого человека</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Нужно всегда</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Уровни тестирования iOS (в шаблонном проекте уже предустановлены два Test Target)

::: div .code-block
:::inline div .code-head
<span>SWIFT · Пример модульного теста</span><span class="dots">···</span>
:::

```
import XCTest

// Выносим логику вроде «строка суммы -> число» в чистую функцию
func parseAmount(_ input: String) -> Double? {
    guard let v = Double(input.trimmingCharacters(in: .whitespaces)),
          v > 0 else { return nil }
    return v
}

final class AmountTests: XCTestCase {
    func testEmptyInputReturnsNil() {
        XCTAssertNil(parseAmount(""))
    }
    func testNegativeReturnsNil() {
        XCTAssertNil(parseAmount("-5"))
    }
    func testNormalValueParses() {
        XCTAssertEqual(parseAmount("12.5"), 12.5)
    }
}
```
:::

Запуск тестов: ⌘U. Когда всё зелёное, менять код можно смело. Проверка сумм и расчёты сводок в книге учёта должны быть под прикрытием модульных тестов.

#### 3. Подпись и упаковка: ставим на приложение «печать»

Каждое приложение iOS перед установкой обязано быть подписано — доказательство, что «пакет от вас и не подменён по дороге». Иерархия такова:

- Этап учёбы: бесплатный Apple ID + автоподпись Xcode (Personal Team), работает на реальном устройстве, продлевать каждые 7 дней;
- Этап распространения: платный аккаунт разработчика (99 долларов в год) выпускает сертификаты и профили — без них ни в магазин, ни на долгую установку.

Упаковка: меню Xcode Product → Archive (архивирование), после сборки в Organizer — Distribute App → выбрать App Store Connect → загрузить. Архивировать надо с целью Generic iOS Device (не симулятор) — новички сплошь и рядом забывают этот шаг.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Осторожно: потерян сертификат — обновления встали

{class="mt-1"}
Если сертификат подписи и закрытый ключ пропали, обновления для старого приложения выпускать больше нельзя — пользователю останется лишь «совершенно новое» приложение. Храните сертификат в надёжной резервной копии (экспорт .p12 из Связки ключей) и не теряйте пароль. К счастью, Apple предлагает автоподпись и облачное управление сертификатами (галочка Automatically manage signing в Xcode) — это снимает большую часть ручных граблей.
:::

#### 4. Полный путь публикации в App Store

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Зарегистрировать аккаунт разработчика</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> Подготовить материалы для магазина</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> Загрузить сборку</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> Заполнить сведения о приватности и для проверки</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Проверка Apple (1-7 дней)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> Публикация</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Рисунок 5: шесть шагов публикации в App Store
:::

- Регистрация: developer.apple.com, личный аккаунт — 99 долларов в год;
- Материалы: иконка (1024×1024, без скруглений — Apple сама отрежет), скриншоты (размеры iPhone), описание, ссылка на политику конфиденциальности;
- Анкета конфиденциальности: честно перечислите, какие данные собираете, — книга учёта без сети может ответить «не собираем никаких данных»;
- Проверка: первое представление нередко ждёт 1–7 дней; отклонили — правьте по каждому пункту «замечаний». Причины отказа Apple обычно формулирует очень конкретно — просто делайте, как сказано;
- TestFlight: до публикации раздайте тестовую версию друзьям на закрытое тестирование (до 10 000 человек), соберите круг отзывов и лишь потом подавайте официально — сразу видно профессионала.

#### 5. Материалы для магазина: первое впечатление и есть количество загрузок

Страница в магазине — витрина, на которую пользователь смотрит, «заходя в лавку». Первое впечатление делают три материала:

- Иконка: 1024×1024, не отделывайтесь скриншотом. Не умеете в дизайн — сгенерируйте лаконичный знак ИИ-инструментом; годится лишь та, что узнаётся с одного взгляда даже уменьшенной на рабочем столе;
- Скриншоты: минимум 2 набора (ходовые размеры iPhone), показывайте самые главные сценарии; к каждому — одна фраза человеческим языком («Запись за секунду» в десять раз лучше «Эффективного решения для учёта финансов»);
- Описание: первая фраза объясняет «что это + для кого»; не громоздите «самый профессиональный, самый мощный» — искренность действует сильнее преувеличений.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Практика: один раз «выпустите» книгу учёта

#### 6. Отчёты о падениях и мини-чеклист производительности

Перед публикацией на эти два дела стоит потратить по полчаса:

##### 1. Мониторинг падений

То, что у вас в тестах ничего не падало, не значит, что не будет падать у пользователей. Apple бесплатно даёт отчёты о падениях в Xcode Organizer (платный аккаунт видит журналы падений с реальных устройств); способ попроще — подключить сторонний SDK (например, Firebase Crashlytics). Публиковаться без мониторинга падений — всё равно что водить машину с закрытыми глазами.

##### 2. Четыре пункта самопроверки производительности

1. Списки через LazyVStack / List: длинные списки не выстраивайте обычным VStack в лоб — ленивая загрузка это первый урок производительности;
2. Не пихайте в интерфейс картинки-оригиналы: берите AsyncImage (удалённые изображения) и системный кеш — оригинал на 5 МБ способен повесить старый телефон;
3. Не делайте тяжёлую работу в главном потоке: сеть и большие файлы — через async/await;
4. Замерьте Instruments: встроенный в Xcode анализатор производительности (Time Profiler, проверка утечек памяти) — сперва меряем, потом ускоряем, никаких «на глазок».

{class="mt-1"}
① Добавьте 3 модульных теста к логике вроде parseAmount (⌘U — всё зелёное); ② через точку останова своими руками поймайте специально устроенное падение и почините его; ③ соберите пакет через Product → Archive и пригласите друзей на закрытое тестирование через TestFlight; ④ если остались силы, заведите аккаунт разработчика и по-настоящему отправьте книгу учёта в магазин. Первые три шага реально успеть сегодня вечером.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Краткие итоги главы

- Три кита отладки: журнал print, точки останова, предпросмотр SwiftUI и инспектор представлений
- XCTest: модульные тесты (⌘U) + UI-тесты + ручное тестирование, шаблоны предустановлены
- Подпись: бесплатный аккаунт — автоподпись (продление раз в 7 дней); распространять может лишь платный
- Упаковка: Generic iOS Device + Archive + Distribute; сертификат обязательно в резервную копию
- Шесть шагов публикации: регистрация → материалы → загрузка → анкета конфиденциальности → проверка → выход в магазин; сперва закрытое тестирование в TestFlight
:::
