---
id: di-liu-shi-yi-zhang
num: 61
part: ios-kai-fa-pian
nav: Глава 61: Быстрый старт со Swift — первый язык разработки под Apple
toc: default
kind: chapter
---

### Глава 61. Быстрый старт со Swift — первый язык разработки для Apple

{class="chapter-intro mb-4"}
В этой главе мы всерьёз берёмся за язык. Не волнуйтесь — Swift славится «дружелюбием к новичкам», и зубрить учебник по синтаксису не нужно: освоив 20% синтаксиса, вы сможете понимать и писать 80% повседневного кода. Остальное будете подсматривать по ходу проекта. Запомните наш принцип обучения: понять важнее, чем запомнить; уметь пользоваться важнее, чем владеть в совершенстве.

#### 1. Переменные и типы: даём данным имена

Программа — это «данные + логика». Переменная — это имя, под которым данные хранятся. В Swift их объявляют через let и var:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Переменные</span><span class="dots">···</span>
:::

```
let name = "Иван"        // let: константа (по умолчанию берём её)
var age = 18             // var: переменная (можно менять потом)

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var можно изменить
// name = "Мария"         // <i class="fas fa-times-circle mr-1"></i> let изменить нельзя — ошибка компиляции

let score: Int = 100     // тип можно указать и явно
let pi = 3.14            // можно не писать — выведется сам

print("Привет, \(name)")   // строковая интерполяция: обратный слэш + скобки
```
:::

Часто используемые типы — запомните одной таблицей:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Тип</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Что хранит</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Пример</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">целые числа</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">дробные числа</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">текст</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Привет"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bool</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">истина/ложь</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[Int] (массив)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">набор данных</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[1, 2, 3]</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Часто используемые базовые типы Swift

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Совет: принцип «сначала let»

{class="mt-1"}
Железное правило сообщества Swift: по умолчанию используйте let, а var — только когда это действительно нужно. Если там, где хватило бы let, вы написали var, Xcode предупредит вас жёлтым. Эта привычка избавит вас от целого класса багов «переменную случайно изменили» — чем меньше в коде меняется, тем легче о нём рассуждать.
:::

#### 2. Опциональные значения (Optional): «оберег от падений» в Swift

Это важнейшее понятие Swift, и без всякой конкуренции. Одной фразой: если значение может «отсутствовать», Swift заставляет вас это обработать — язык на корню искореняет профессиональный кошмар «падение из-за нулевого указателя».

::: div .code-block
:::inline div .code-head
<span>SWIFT · Опционалы</span><span class="dots">···</span>
:::

```
var name: String = "Иван"   // обычный тип: nil не допускается
// name = nil                // <i class="fas fa-times-circle mr-1"></i> ошибка компиляции — вас сразу остановят

var nickname: String? = nil  // добавляем вопросик: nil разрешён (опционал)
nickname = "Ваня"

// Опционал нужно «распаковать»:
if let n = nickname {        // if let: безопасная распаковка
    print("Привет, \(n)")
} else {
    print("Никнейма ещё нет")
}

let len = nickname?.count ?? 0   // ?? подставляет значение по умолчанию (оператор nil-coalescing)
print(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Внимание: «!» — опасная операция

{class="mt-1"}
Написать nickname! (принудительное разворачивание) — всё равно что крикнуть компилятору «клянусь, там не nil»: ошибётесь — приложение рухнет на месте. Правило новичка: по возможности используйте if let / ?? и не используйте «!». Когда Xcode автодополняет код, он иногда подсовывает «!» — не забудьте это убрать.
:::

#### 3. Функции и замыкания: упаковываем логику в «кнопки»

Функция — это поименованный кусок логики, как кнопка на пульте. Замыкание (Closure) — «функция без имени», которую можно передать другому одним движением руки:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Функции и замыкания</span><span class="dots">···</span>
:::

```
// Функции: имя впереди, параметры и возвращаемый тип после
func greet(name: String) -> String {
    return "Привет, \(name)!"
}
print(greet(name: "Иван"))     // при вызове нужно указывать имя параметра

// Замыкания: определяем на месте, коротко и прямо
let numbers = [1, 2, 3, 4]
let doubled = numbers.map { $0 * 2 }   // $0 = текущий элемент
// [2, 4, 6, 8]

let big = numbers.filter { $0 > 2 }    // фильтрация
// [3, 4]
```
:::

В SwiftUI замыкания повсюду: фигурные скобки после Button("Нажми меня") { ... } — это и есть замыкание. Крепко запомните «комбо» для коллекций: map, filter, sorted — 90% будущей обработки списков будет их комбинацией.

#### 4. Структуры и протоколы: «лего»-система Swift

Официальное предпочтение Swift ясно: сначала структуры (struct), а классы (class) — только когда нужно наследование. Структура — «тип значения»: при копировании каждая живёт своей жизнью, и это само по себе избавляет от целого класса багов:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Структуры и протоколы</span><span class="dots">···</span>
:::

```
// Структура: коробка для данных
struct Record {
    var id = UUID()
    var amount: Double
    var category: String
    var date: Date

    // У структуры есть встроенный «инициализатор по членам»: создавать можно сразу
}
let r = Record(amount: 25.5, category: "Еда", date: Date())

// Протокол: договорённость «какие способности обязательны»
protocol Identifiable {
    var id: UUID { get }
}
struct Record: Identifiable { ... }   // соответствие протоколу = обещание выполнить его требования
```
:::

В SwiftUI почти всё — struct (View — это протокол). Если сейчас фраза непонятна — не страшно, в главе 62 вы будете встречаться с ней каждый день. В мире Swift сперва обнимите struct.

#### 5. Шпаргалка по синтаксису для начинающих с нуля

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Что нужно сделать</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Как пишется</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Объявить константу/переменную</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">let x = 1</code> / <code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Интерполяция строк</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Привет, \(name)"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Объявить функцию</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">func имя(параметр: Тип) -> Тип Результата { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Условие</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if условие { ... } else { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Перебор</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for x in массив { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Безопасное разворачивание</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if let x = опциональное Значение { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Значение по умолчанию</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">x ?? значение По Умолчанию</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Объявить структуру</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X { var a: Int; var b: String }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Замыкание</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">{ $0 * 2 }</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Шпаргалка по синтаксису Swift (для новичков)

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Попробуйте сами: 15 минут игры со Swift в Playgrounds

{class="mt-1"}
Есть Mac — откройте Xcode → Playground; нет Mac — используйте Swift Playgrounds на iPad или онлайн-песочницу. Прогоните каждый кусочек кода из этой главы, меняйте числа и текст, нарочно наделайте ошибок и посмотрите, как на них реагирует Xcode. Эти 15 минут «сначала поиграть, потом учиться» сделают старт главы 62 вдвое легче.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Краткие итоги главы

- let — по умолчанию, var — с осторожностью; типы выводятся автоматически, но можно указать и явно после двоеточия
- Опциональные значения — душа Swift: если значение может быть пустым, это обязательно обрабатывается; if let / ?? — оберег, «!» — опасная операция
- При вызове функции указываются имена параметров; замыкание = функция без имени, в SwiftUI оно повсюду
- Приоритет — struct, соблюдайте протоколы (Protocol); в SwiftUI почти всё — struct
- 20% синтаксиса делают 80% работы: сначала научитесь пользоваться, потом совершенствуйтесь
:::
