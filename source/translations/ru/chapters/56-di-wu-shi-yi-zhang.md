---
id: di-wu-shi-yi-zhang
num: 51
part: an-zhuo-kai-fa-pian
nav: Глава 51: Разработка интерфейсов — введение в Jetpack Compose
toc: default
kind: chapter
---

### Глава 51. Разработка интерфейса — знакомство с Jetpack Compose

{class="chapter-intro mb-4"}
Интерфейс — всё, что видит пользователь. До появления Compose интерфейсы Android писали на XML — муторно, как заполнять пропуски в упражнениях. В 2021 году Google выпустила Jetpack Compose: интерфейс «рисуют» прямо кодом на Kotlin, и результат виден сразу — поменялась строка кода, предпросмотр мгновенно обновился. К 2026 году Compose стал безоговорочным мейнстримом для новых проектов. В этой главе мы научимся «рисовать».

#### 1. Идея Compose: интерфейс — это функция

Ядро идеи Compose — одна фраза: интерфейс = функция. Всё, что может появиться на экране (текст, кнопка, картинка), — «композируемая функция» (Composable), помеченная @Composable. Вложите их друг в друга, словно кубики, — вот вам и интерфейс.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Первый экран в Compose</span><span class="dots">···</span>
:::

```
@Composable
fun Greeting(name: String) {
    Text(text = "Привет, $name!")     // «кирпичик текста»
}

// Вложенная компоновка: большие блоки содержат маленькие
@Composable
fun HomeScreen() {
    Column {                          // вертикально
        Greeting(name = Иван)
        Greeting(name = Мария)
        Button(onClick = { /* что делать по нажатию */ }) {
            Text("Нажми")
        }
    }
}
```
:::

Обратите внимание на «шляпу» @Composable — она говорит компилятору: «это кубик интерфейса». Кубики можно вкладывать без ограничений — в этом весь секрет Compose.

#### 2. Базовые компоненты: текст, кнопка, поле ввода, изображение

Компоненты Compose — те же «кубики». Вот четыре самых ходовых:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Компонент</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Что делает</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Обязательные параметры</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Показывает текст</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">text (текст для показа)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Кнопка</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onClick (колбэк нажатия)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Поле ввода</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">value, onValueChange (колбэк изменения ввода)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Показывает изображение</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">painter (графический ресурс)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Четыре базовых компонента Compose

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Пример базовых виджетов</span><span class="dots">···</span>
:::

```
@Composable
fun BasicWidgets() {
    Column {
        Text(text = "Это какой-то текст")
        Button(onClick = { println("Нажато") }) {
            Text("Кнопка")
        }
        var input by remember { mutableStateOf("") }
        TextField(
            value = input,
            onValueChange = { input = it },
            label = { Text("Введите что-нибудь") }
        )
    }
}
```
:::

В двух строках про поле ввода мелькнуло remember { mutableStateOf("") } — это «магия состояния» Compose; подробно разберём в пятом разделе главы. Пока просто запомните её в лицо.

#### 3. Трио раскладок: Column, Row, Box

Компоненты есть — как их расставить? Запомните три «коробки»:

- Column: ставит элементы столбиком (как очередь за обедом);
- Row: выстраивает элементы в ряд (как сидящие рядом);
- Box: кладёт элементы стопкой (как колода карт; удобно для бейджей и наложений).

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Три базовых раскладки</span><span class="dots">···</span>
:::

```
Column {
    Text("Первая строка")
    Row {
        Text("Слева")
        Text("Справа")
    }
    Box {
        Text("Нижний слой")
        Text("Бейдж поверх")
    }
}
```
:::

Хотите, чтобы раскладка выглядела лучше? Добавьте компонентам Modifier (модификатор) — он словно «накладывает грим» на кубики:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Полезные приёмы Modifier</span><span class="dots">···</span>
:::

```
Text(
    text = "Красивый текст",
    modifier = Modifier
        .padding(16.dp)          // отступы со всех сторон
        .fillMaxWidth()          // занять всю ширину
        .background(Color.Blue)  // цвет фона
        .clickable { /* нажатие */ }// кликабельно
)
// Цепочки вызовов: одна за другой, порядок важен (сначала padding, потом фон — фон не включает отступы)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Внимание: порядок в Modifier имеет значение

{class="mt-1"}
padding(16.dp).background(Blue) и background(Blue).padding(16.dp) дают разный результат: первый — «сначала отступ, потом заливка» (фон не захватывает отступы), второй — «сначала заливка, потом отступ» (фон включает отступы). Новички чаще всего рисуют здесь «загадочные белые поля». Сомневаетесь — поменяйте порядок, и предпросмотр тут же даст ответ.
:::

#### 4. Состояние: оживляем интерфейс

Статичный интерфейс — скучное зрелище. Чтобы после нажатия кнопки число росло на 1, а в поле ввода можно было печатать, нужно состояние (State). Правило Compose: интерфейс всегда верно отражает состояние; состояние изменилось — интерфейс сам перерисовался.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Состояние: счётчик нажатий</span><span class="dots">···</span>
:::

```
@Composable
fun Counter() {
    // remember + mutableStateOf: запоминаем меняющееся значение
    var count by remember { mutableStateOf(0) }

    Column {
        Text(text = "Вы нажали $count раз")
        Button(onClick = { count++ }) {   // меняем состояние
            Text("Нажми +1")                // интерфейс обновится сам
        }
    }
}
```
:::

Три строки кода — и живой счётчик. Вот чем Compose приятнее старых подходов: не нужно вручную «обновлять интерфейс» — достаточно поменять данные. Запомните две ключевые функции: remember (не даёт значению обнулиться при рекомпозиции интерфейса) и mutableStateOf (сообщает Compose: «это значение изменилось, надо перерисовать»).

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> Пользователь нажимает</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> Состояние меняется (count++)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> Compose замечает изменение</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> Интерфейс перерисовывается сам (рекомпозиция)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Рисунок 3. Однонаправленный поток данных «состояние → интерфейс» в Compose
:::

#### 5. Тема и тёмный режим: настроил один раз — работает везде

MyFirstAppTheme { ... } из шаблонного проекта — это и есть тема. Она построена на дизайн-системе Material 3 и помогает единообразно управлять цветами, шрифтами и формами. Поддержка тёмного режима — всего три шага:

1. определите в теме две палитры — светлую и тёмную (шаблон уже генерирует ColorScheme автоматически);
2. когда система переходит в тёмный режим, isSystemInDarkTheme() определяет это автоматически;
3. берите цвета из темы (например, MaterialTheme.colorScheme.primary), а не вписывайте значения напрямую.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Совет: динамические цвета Material 3

{class="mt-1"}
Начиная с Android 12 «Material You» позволяет приложению брать цвета из ваших обоев. Шаблон Compose поддерживает это из коробки (dynamicColor). Ваше приложение будет «переодеваться» на телефонах разных пользователей — вот она, романтика современного Android.
:::

#### 6. Предпросмотр, анимации и живое редактирование: «читы» Compose

Три «чита» Compose для удобства разработки: попробуешь — назад дороги нет:

- Предпросмотр @Preview: добавьте Composable аннотацию @Preview — и Android Studio мгновенно отрисует интерфейс справа: правите код и сразу видите результат, без установки на телефон каждый раз;
- Живое редактирование (Live Edit): Android Studio 2026 года умеет «горячо» применять часть правок на эмуляторе или реальном устройстве — мелкие изменения вроде цвета текста появляются на устройстве за секунды;
- API анимаций: animateFloatAsState и AnimatedVisibility позволяют парой строк добиться плавных переходов элементов — до ощущения «дорогого» продукта часто не хватает именно этих нескольких десятков строк.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Анимация за десять минут</span><span class="dots">···</span>
:::

```
@Composable
fun AnimatedBox() {
    var big by remember { mutableStateOf(false) }
    // при изменении значения плавно переходит к целевому
    val size by animateDpAsState(if (big) 120.dp else 60.dp)

    Box(Modifier
        .size(size)
        .background(MaterialTheme.colorScheme.primary)
        .clickable { big = !big }
    )
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Совет: сперва функциональность, потом анимация

{class="mt-1"}
Типичная болезнь новичков — «интерфейс ещё не сделан, а человек уже мучается с анимациями». Сначала добейтесь, чтобы всё работало, а затем разом добавьте анимацию — это и есть принцип «простота превыше всего»: анимация — украшение, а функциональность — спасение.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Практика: сделайте «кнопку настроения»

{class="mt-1"}
Превратите шаблонный проект в переключатель настроения: одна кнопка; каждое нажатие двигает настроение по кругу 😀 радость → 😢 грусть → 😡 злость, а текст и цвет фона меняются вслед за ним. Подсказка: выбирайте текст и цвет через when по состоянию. Готовым приложением поделитесь с друзьями — и соберёте первый урожай «Вау, ты уже умеешь делать приложения!».
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Коротко о главном

- Идея Compose: интерфейс = функции @Composable, вложенные как кубики
- Четыре главных компонента: Text / Button / TextField / Image
- Трио раскладок: Column — столбиком, Row — в ряд, Box — стопкой
- Modifier «накладывает грим» цепочкой: padding, fillMaxWidth, background, clickable — порядок важен
- Состояние — душа интерфейса: remember + mutableStateOf; поменял данные — интерфейс перерисовался сам
- Тема: Material 3 + динамические цвета; тёмный режим настраивается один раз и работает везде
:::
