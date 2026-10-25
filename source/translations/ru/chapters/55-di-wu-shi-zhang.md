---
id: di-wu-shi-zhang
num: 50
part: an-zhuo-kai-fa-pian
nav: Глава 50: Быстрый старт с Kotlin — первый язык Android-разработки
toc: default
kind: chapter
---

### Глава 50: Быстрый старт с Kotlin — первый язык Android-разработки

{class="chapter-intro mb-4"}
В этой главе мы наконец учим язык. Не волнуйтесь — Kotlin славится дружелюбием к новичкам, и учить грамматику наизусть не нужно: освоив 20% синтаксиса, вы будете понимать и писать 80% повседневного кода. Остальное подсмотрите по ходу проектов. Помните наш принцип обучения: понимать важнее, чем запоминать; уметь пользоваться важнее, чем владеть в совершенстве.

#### 1. Переменные и типы: даём данным имена

Программа — это «данные + логика». Переменная — это имя, под которым данные хранятся. В Kotlin два способа объявления:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Переменные</span><span class="dots">···</span>
:::

```
val name = Иван        // val: переменная только для чтения (по умолчанию берём её)
var age = 18             // var: изменяемая переменная (можно менять позже)

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var можно изменить
// name = "Мария"         // <i class="fas fa-times-circle mr-1"></i> val изменить нельзя — ошибка компиляции

val score: Int = 100     // тип можно указать и явно
val pi = 3.14            // можно не писать — выведется сам
```
:::

Часто используемых типов всего несколько — запомните их одной таблицей:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Тип</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Что хранит</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Пример</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Целое число</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Дробное число</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Текст</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Привет"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Boolean</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Истина / Ложь</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List&lt; T&gt;</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Набор данных</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">listOf(1, 2, 3)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Базовые типы Kotlin, используемые чаще всего

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Совет: принцип «val прежде всего»

{class="mt-1"}
Железное правило сообщества Kotlin: по умолчанию val, и только при действительной необходимости var. Если там, где хватит val, вы используете var, IDE подсветит жёлтым. Эта привычка избавит вас от целого класса багов «переменную изменили случайно» — чем меньше в коде изменчивости, тем легче о нём рассуждать.
:::

#### 2. Функции: упаковываем логику в «кнопки»

Функция — это именованный фрагмент логики, как кнопка на пульте: нажали (вызвали) — выполнилась цепочка действий. В Kotlin функция объявляется словом fun:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Функции</span><span class="dots">···</span>
:::

```
fun greet(name: String): String {
    return "Привет, $name!"     // знак $ вставляет переменную в строку
}

println(greet(Иван))        // вывод: Привет, Иван!

// однострочную функцию можно записать выражением
fun add(a: Int, b: Int) = a + b

println(add(3, 5))            // вывод: 8
```
:::

Несколько моментов: параметры пишутся в скобках (сначала имя, затем тип, через двоеточие); тип возвращаемого значения — после скобок; строковые шаблоны $имя_переменной — фирменное удобство Kotlin: больше не нужно, как в Java, склеивать «строка + переменная».

#### 3. Условия и циклы: учим программу «думать»

Ум программы складывается из двух вещей: умения делать выбор (if/when) и умения повторять (for/while).

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Условия и циклы</span><span class="dots">···</span>
:::

```
// Ветвление: if / else
val age = 17
if (age >= 18) {
    println("взрослый")
} else {
    println("несовершеннолетний")
}

// Множественный выбор: when (в сто раз удобнее switch)
val score = 85
val level = when {
    score >= 90 -> "отлично"
    score >= 60 -> "зачёт"
    else -> "Так держать!"
}

// Повторение: цикл for
val fruits = listOf("яблоко", "банан", "апельсин")
for (fruit in fruits) {
    println("Я люблю $fruit")
}
```
:::

when — самый ходовой в Kotlin способ записать множественный выбор; в Android-разработке вы будете пользоваться им каждый день (например, чтобы показывать разные экраны в зависимости от состояния).

#### 4. Null-безопасность: «спасательный круг» Kotlin

Самый знаменитый баг эпохи Java — NullPointerException (исключение нулевого указателя): программа обращается к тому, в чём «ничего нет», и мгновенно падает. По статистике он годами держит первое место в рейтингах сбоев Android. Kotlin решил проблему на уровне языка: null по умолчанию запрещён.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Null-безопасность</span><span class="dots">···</span>
:::

```
var name: String = "Иван"   // обычный тип: null не допускается
// name = null                // <i class="fas fa-times-circle mr-1"></i> ошибка компиляции — вас сразу остановят

var nickname: String? = null // добавляем вопросик: null разрешён
nickname = "Ваня"

// С nullable-типами нужно обращаться безопасно:
println(nickname?.length)    // безопасный вызов: вернёт null, не падая
val len = nickname?.length ?: 0   // оператор Элвиса: значение по умолчанию при null
println(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Внимание: не путайте ? и ?:

{class="mt-1"}
String? означает «может быть пустым», а a ?: b — «если a пусто, возьми b» (запись похожа на причёску Элвиса, поэтому оператор прозвали Elvis). Когда в начале пути компилятор ругается на «ошибки, связанные с null», в восьми случаях из десяти вы забыли обработать nullable-тип — язык просто защищает вас.
:::

#### 5. Классы и объекты: формы для изготовления «деталей»

Класс — это «форма» для объектов, объект — «готовая деталь», отлитая по форме. Всё в Android — экраны, кнопки, данные — объекты. В Kotlin есть волшебный инструмент data class (класс данных), созданный специально, чтобы «носить данные»: одна строка заменяет десятки строк Java:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Классы и data-классы</span><span class="dots">···</span>
:::

```
// Обычный класс: форма
class Dog(val name: String) {
    fun bark() = println("$name: Гав!")
}

val dog = Dog("Шарик")      // создаём объект
dog.bark()                 // Шарик: Гав!

// data class: коробка для данных (с готовыми equals/copy и т.д.)
data class User(val id: Int, val name: String, val email: String)

val me = User(1, Иван, "zhangsan@example.com")
val twin = me.copy(name = "Иванушка")   // копируем и меняем одно поле
```
:::

Когда позже вы будете делать учёт расходов, каждая запись станет data class: data class Record(val amount: Double, val category: String, val date: String). Смотрите — вы уже способны писать структуру кода настоящего проекта.

#### 6. Лямбды и функции высшего порядка: «синтаксический сахар» Kotlin

В Android-коде вы ежедневно будете встречать «функции без имени» вида { ... } — они называются лямбдами (анонимными функциями). Button с onClick = { count++ } — это лямбда: мы упаковываем «что делать после нажатия» в один блок и вручаем его кнопке.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Первое знакомство с lambda</span><span class="dots">···</span>
:::

```
// Обычный способ: определяем именованную функцию и передаём
fun double(x: Int) = x * 2
val result = listOf(1, 2, 3).map(::double)

// Через lambda: определяем на месте, коротко и прямо
val result2 = listOf(1, 2, 3).map { it * 2 }   // it = текущий элемент

// Комбо «фильтр + преобразование» (крайне часто в реальных проектах)
val bills = listOf(12.5, 88.0, 5.0, 200.0)
val bigBills = bills.filter { it > 50 }.sorted()
// [88.0, 200.0] — «счета больше 50, отсортированы»
```
:::

Запомните несколько частых «комбо» для коллекций: filter (отбор), map (преобразование), sorted (сортировка), sum (сумма). 90% будущей работы со списками — комбинации этих четырёх приёмов. Философия Kotlin: если логику можно высказать одной фразой, не пишите пять.

#### 7. Шпаргалка по синтаксису для тех, кто с нуля

Не пытайтесь выучить весь синтаксис за один день. Сохраните эту карточку и заглядывайте в неё, пока пишете код, — недели через две всё станет привычным само собой:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Что нужно сделать</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Как записать</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Объявить переменную только для чтения</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">val x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Объявить изменяемую переменную</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Объявить функцию</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">fun имя(параметры): тип Результата { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Условие</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if (условие) {...} else {...}</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Множественный выбор</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">when { условие -> результат }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Перебор</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for (x in список) { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Склейка строк</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Привет, $name"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Обработка nullable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">x?.length ?: 0</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Объявить класс данных</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">data class X(val a: Int, val b: String)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Шпаргалка по синтаксису Kotlin (версия для новичков)

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Практика: поиграйте 10 минут в Kotlin, ничего не устанавливая

{class="mt-1"}
Откройте в браузере play.kotlinlang.org (официальную онлайн-песочницу Kotlin), вставьте туда каждый пример кода из этой главы, запустите, поменяйте числа и текст и посмотрите, как меняется вывод. Эти 10 минут «сначала поиграть, потом учить» вдвое облегчат вам старт в главе 51.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Коротко о главном

- Предпочитайте val, к var прибегайте с осторожностью; тип можно вывести автоматически, но можно объявить и явно после двоеточия
- Функция = упакованная логика; строковый шаблон $ — фирменное удобство
- if/when — выбор, for — цикл; when в Android-разработке «мастер на все руки»
- Null-безопасность — спасательный круг Kotlin: обычные типы null отвергают, nullable-типы требуют обработки через ? и ?:
- data class — коробка для данных: одно поле на строку, в настоящих проектах используется ежедневно
- 20% синтаксиса делают 80% работы: сначала научитесь пользоваться, а мастерство придёт потом
:::
