---
id: di-liu-shi-er-zhang
num: 62
part: ios-kai-fa-pian
nav: Глава 62: Разработка интерфейсов — введение в SwiftUI
toc: default
kind: chapter
---

### Глава 62. Разработка интерфейсов — введение в SwiftUI

{class="chapter-intro mb-4"}
Интерфейс — это всё, что видит пользователь. SwiftUI — декларативный фреймворк интерфейсов, представленный Apple в 2019 году: вам нужно лишь «объявить», как выглядит интерфейс, а система сама займётся отрисовкой, тёмной темой и разными экранами. К 2026 году SwiftUI — безоговорочный мейнстрим для новых проектов. В этой главе мы научимся «рисовать».

#### 1. Идея SwiftUI: декларативность, а не императивность

Старая разработка интерфейсов — «императивная»: вы инструктируете систему шаг за шагом — «создай кнопку → помести в (20,30) → задай цвет». SwiftUI — «декларативный»: вы просто описываете «на экране есть красная кнопка с надписью "Нажми меня"», а как рисовать и когда перерисовывать — система решает сама.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Первый view в SwiftUI</span><span class="dots">···</span>
:::

```
import SwiftUI

struct ContentView: View {
    var body: some View {      // body: описывает «как выглядит экран»
        VStack {               // вертикально
            Text("Привет, мир!")
                .font(.largeTitle)      // модификатор: крупный заголовок
            Button("Нажми") {
                print("Нажато")
            }
            .buttonStyle(.borderedProminent)  // сплошная синяя кнопка
        }
        .padding()
    }
}
```
:::

Ключевой момент: представление = структура, соблюдающая протокол View; свойство body описывает интерфейс, а модификаторы через точку «наносят макияж» цепочкой. Это и есть весь фундамент SwiftUI.

#### 2. Базовые представления: текст, кнопка, поле ввода, картинка

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Представление</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Для чего</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Пример</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">показывать текст</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text("Привет")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">кнопка</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button("Нажми меня") { действие }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">поле ввода</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField("подсказка", text: $текст)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">показывать картинку</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Image(systemName: "star.fill")</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Четыре базовых представления SwiftUI

Обратите внимание на Image(systemName:) — у Apple есть встроенная библиотека иконок SF Symbols (несколько тысяч бесплатных иконок): имя вроде "star.fill" сразу покажет залитую звёздочку. Это скрытый бонус разработки под iOS: для интерфейсов почти не нужно искать иконки.

#### 3. Трио компоновки: VStack, HStack, ZStack

- VStack: выстраивает по вертикали (как очередь в столовой);
- HStack: выстраивает по горизонтали (как сидящие рядом);
- ZStack: накладывает друг на друга (как стопка игральных карт, подходит для бейджей и масок).

::: div .code-block
:::inline div .code-head
<span>SWIFT · Три стека раскладки + частые модификаторы</span><span class="dots">···</span>
:::

```
VStack(alignment: .leading, spacing: 12) {
    HStack {
        Text("Счёт")
        Spacer()                 // гибкое пространство: отталкивает правую часть к краю
        Text("-25.5 юаня").foregroundColor(.red)
    }
    Divider()                    // разделитель
    Text("Заметка: обед")
}
.padding(16)                     // отступы со всех сторон
.background(Color(.systemGray6)) // светло-серый фон
.cornerRadius(12)                // скругление углов

// Порядок модификаторов важен: сначала padding, потом background — фон не включает отступы
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Внимание: порядок модификаторов имеет значение

{class="mt-1"}
padding(16).background(серый) и background(серый).padding(16) дают разный эффект: первый — «сначала отступ, потом краска» (фон без отступов), второй — «сначала краска, потом отступ» (фон включает отступы). Отсюда и самые частые у новичков «странные белые полосы». Сомневаетесь — поменяйте порядок, и предпросмотр тут же покажет ответ.
:::

#### 4. Состояние и привязка: оживляем интерфейс

Статичный интерфейс скучен. Правило SwiftUI: интерфейс всегда верно отражает состояние; изменилось состояние — интерфейс перерисовывается сам.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Счётчик на @State</span><span class="dots">···</span>
:::

```
struct CounterView: View {
    @State private var count = 0   // @State: при изменении значения перерисовать

    var body: some View {
        VStack {
            Text("Вы нажали \(count) раз")
            Button("Нажми +1") {
                count += 1          // меняем состояние — интерфейс обновится сам
            }
        }
    }
}
```
:::

Для поля ввода нужна «двусторонняя привязка» — знак $ передаёт одновременно «значение и право его менять»:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Двустороннее связывание через @Binding</span><span class="dots">···</span>
:::

```
struct InputView: View {
    @State private var text = ""

    var body: some View {
        TextField("Введите что-нибудь", text: $text)  // $ — двусторонняя связь
            .textFieldStyle(.roundedBorder)
        Text("Вы ввели: \(text)")   // обновляется на лету
    }
}
```
:::

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> Действие пользователя</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> Состояние меняется (count += 1)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> SwiftUI замечает изменение</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> Интерфейс перерисовывается сам (body пересчитывается)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Рисунок 3. Однонаправленный поток данных «состояние → интерфейс» в SwiftUI
:::

#### 5. Предпросмотр, темы и анимация: «читы» SwiftUI

- Макрос #Preview: добавьте в конец файла #Preview { ContentView() } — холст справа начнёт рендерить в реальном времени, и правки кода будут видны сразу;
- Тёмная тема бесплатно: используйте системные цвета (Color(.systemGray6), .primary), а не жёстко заданные — тёмная тема подстроится автоматически, без единой лишней строки;
- Анимация в одну строку: withAnimation { count += 1 } или добавьте к представлению .animation(.default, value: count) — переходы станут шелковистыми.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Анимация за десять минут</span><span class="dots">···</span>
:::

```
struct AnimatedHeartView: View {
    @State private var liked = false

    var body: some View {
        Button {
            withAnimation(.spring(duration: 0.4)) {
                liked.toggle()
            }
        } label: {
            Image(systemName: liked ? "heart.fill" : "heart")
                .font(.system(size: 48))
                .foregroundColor(liked ? .red : .gray)
                .scaleEffect(liked ? 1.3 : 1.0)
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Совет: сначала функция, потом анимация

{class="mt-1"}
Типичная ошибка новичка — «интерфейс ещё не доделан, а он уже мучается с анимациями». Сначала добейтесь, чтобы всё работало, а эффекты добавьте в конце разом: анимация — украшение, функциональность — спасение. Это и есть наш вечный принцип «простота превыше всего».
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Попробуйте сами: сделайте «кнопку настроения»

#### 6. Шпаргалка по частым модификаторам: одна страница под рукой — и интерфейсы не страшны

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Что хотите сделать</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Модификатор</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Отступы</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.padding(16)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Скругление углов</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cornerRadius(12)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Цвет фона</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.background(Color(.systemGray6))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Шрифт и размер</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.font(.title.bold())</code> / <code class="inline">.font(.system(size: 20))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Цвет переднего плана (текст/иконки)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.foregroundColor(.red)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Растянуть на всю ширину</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(maxWidth: .infinity)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Фиксированный размер</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(width:100, height: 44)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Выравнивание</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack(alignment: .leading)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Прозрачность</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.opacity(0.6)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Тень</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.shadow(radius: 5)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Жест нажатия</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.onTapGesture { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Тип клавиатуры</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.keyboardType(.decimalPad)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Шпаргалка по частым модификаторам SwiftUI

Ничего страшного, если не запомнили — эта страница и существует для справки. На деле чаще всего используются первые четыре: padding, скругление, фон, шрифт.

{class="mt-1"}
Переделайте шаблонный проект в переключатель настроений: одна кнопка, при каждом нажатии циклически меняется 😀 радость → 😢 грусть → 😡 злость, а текст и цвет фона меняются вместе с ней. Подсказка: храните три пары (текст + цвет) в массиве, индекс — в @State, при нажатии — (index + 1) % 3. Когда сделаете, отправьте друзьям поиграть и соберите первую волну «вау, ты уже умеешь делать приложения!».
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Краткие итоги главы

- SwiftUI декларативен: вы описываете, «как это выглядит», а система рисует и перерисовывает
- представление = структура, соблюдающая протокол View; body описывает интерфейс; модификаторы «наносят макияж» цепочкой
- четыре базовых представления: Text / Button / TextField / Image; библиотека иконок SF Symbols — бесплатно и вдоволь
- трио компоновки: VStack — вертикаль, HStack — горизонталь, ZStack — наложение; Spacer — упругое пространство
- @State оживляет интерфейс; $ — двусторонняя привязка для поля ввода
- #Preview — что видишь, то и получаешь; системные цвета сами подстраиваются под тёмную тему; withAnimation — анимация в одну строку
:::
