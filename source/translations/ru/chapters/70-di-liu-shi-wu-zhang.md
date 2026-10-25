---
id: di-liu-shi-wu-zhang
num: 65
part: ios-kai-fa-pian
nav: Глава 65: Проект 1 — мой учёт расходов (локальная версия)
toc: default
kind: chapter
---

### Глава 65. Проект 1 — моя книга учёта (локальная версия)

{class="chapter-intro mb-4"}
Добро пожаловать в ваш первый «серьёзный проект». Эта книга учёта не выходит в сеть, но устроена по полной программе: записывает транзакции, показывает историю, сводит статистику по месяцам, умеет удалять и править. Сделав её, вы целиком пройдёте весь цикл «данные → логика → интерфейс». Не спешите срисовывать код — сперва подумайте, потом делайте: так мы договаривались с самого начала.

#### 1. Мыслим требованиями: сперва задайте пять вопросов

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Элемент</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ответ</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who (для кого)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Для себя, можно и для родных и друзей</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What (что делаем)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Записывать доходы и расходы, смотреть историю, сводить по месяцам, считать статистику по категориям</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why (зачем)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Тренировка + понять, куда утекают деньги</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How (как делаем)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift + SwiftUI + SwiftData + MVVM, полностью локально, без бэкенда</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint (ограничения)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Уложиться в неделю; минимум iOS 17 (порог SwiftData)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Пять элементов требований книги учёта

Затем разбейте работу на мелкие шаги, где «после каждого шага уже можно пользоваться»: ① слой данных на SwiftData (можно сохранить запись); ② страница-список (можно смотреть историю); ③ окно ввода (можно добавить запись); ④ удаление и правка; ⑤ карточка месячной сводки. После каждого шага приложение остаётся «работающей вещью».

#### 2. Слой данных: даём записям дом

Сначала опишите, как выглядит одна запись, — поля нужны достаточные, но без жадности:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Record.swift (модель)</span><span class="dots">···</span>
:::

```
import SwiftData

@Model
class Record {
    var type: String      // "income" доход | "expense" расход
    var amount: Double    // сумма (в юанях)
    var category: String  // категория: еда, транспорт, зарплата…
    var note: String      // заметка (необязательно)
    var date: Date        // дата записи

    init(type: String, amount: Double, category: String, note: String = "", date: Date = Date()) {
        self.type = type
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Совет: почему сумма — это Double?

{class="mt-1"}
Строгие финансовые приложения берут Decimal (точная десятичная арифметика), чтобы избежать ошибок плавающей точки (вечная проблема 0.1+0.2≠0.3). Для учебного проекта хватает Double; если однажды будете делать настоящий финансовый продукт, не забудьте перейти на Decimal или «Int в копейках» — на эти грабли наступили бессчётные предшественники.
:::

#### 3. MVVM: интерфейс и логика живут раздельно

Дать интерфейсу право напрямую трогать базу? Работать будет, но код интерфейса разрастётся в длинную неопрятную простыню. Архитектура MVVM разводит всех по обязанностям: View (интерфейс) только рисует, ViewModel (логический центр) распоряжается данными, Model (SwiftData) ведает хранением.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View (интерфейс SwiftUI)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel (логический центр на @Observable)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model (слой данных SwiftData)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Рисунок 4: трёхслойная структура MVVM — данные текут в одну сторону, слои не заходят на чужую территорию
:::

::: div .code-block
:::inline div .code-head
<span>SWIFT · RecordViewModel.swift (каркас)</span><span class="dots">···</span>
:::

```
import Observation

@Observable
class RecordViewModel {
    var records: [Record] = []
    private let context: ModelContext

    init(context: ModelContext) { self.context = context }

    func load() {
        // фильтрация + сортировка через #Predicate в SwiftData
        let descriptor = FetchDescriptor<Record>(
            sortBy: [SortDescriptor(\.date, order: .reverse)]
        )
        records = (try? context.fetch(descriptor)) ?? []
    }

    func add(type: String, amount: Double, category: String, note: String) {
        let r = Record(type: type, amount: amount, category: category, note: note)
        context.insert(r)
        try? context.save()
        load()                       // перезагружаем — интерфейс обновится
    }

    func delete(_ record: Record) {
        context.delete(record)
        try? context.save()
        load()
    }
}
```
:::

В интерфейсе создаём @State private var vm = RecordViewModel(...) и рисуем список прямо из vm.records — данные изменились, интерфейс обновился сам.

#### 4. Интерфейс: страница-список + окно ввода

::: div .code-block
:::inline div .code-head
<span>SWIFT · Экран списка расходов (ключевой фрагмент)</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var vm: RecordViewModel
    @State private var showAdd = false

    var body: some View {
        NavigationStack {
            List {
                Section("Баланс за месяц") {          // сводная карточка
                    SummaryRow(records: vm.records)
                }
                Section("Операции") {
                    ForEach(vm.records) { r in
                        RecordRow(record: r)
                    }
                    .onDelete { idx in
                        idx.forEach { vm.delete(vm.records[$0]) }
                    }
                }
            }
            .navigationTitle("Мои записи расходов")
            .toolbar {
                Button { showAdd = true } label: {
                    Image(systemName: "plus")
                }
            }
            .sheet(isPresented: $showAdd) {
                AddRecordView(vm: vm)          // диалог ввода
            }
        }
    }
}
```
:::

Главное в окне ввода: у поля суммы клавиатура .keyboardType(.decimalPad) (цифровая), доход/расход — сегментный переключатель (Picker), категория — выбор в меню, по кнопке «Сохранить» вызываем vm.add(...) и закрываем окно через dismiss().

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Внимание: проверку ввода не упрощаем

{class="mt-1"}
Поле суммы обязательно проверять: пустое значение, отрицательные числа, недопустимый ввод вроде «abc» — всё перехватываем (проверяем через Double(text), при неудаче он вернёт nil). Одна из самых частых причин падений приложений — «посчитать пользовательский ввод послушным ребёнком». Запомните: любой ввод пользователя досматривайте как потенциального врага.
:::

#### 5. Правка, удаление и сводка

- Удаление: .onDelete у List — смахнули влево и удалили + окно подтверждения (случайное удаление — то, что пользователи учётных приложений ненавидят сильнее всего);
- Правка: нажатие на строку открывает окно редактирования с уже подставленными старыми значениями (поправить одно слово проще, чем вводить всё заново);
- Сводка: через filter + reduce считаем «доход / расход / остаток за месяц» и показываем карточкой вверху:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Расчёт итогов за месяц</span><span class="dots">···</span>
:::

```
func monthSummary(_ records: [Record]) -> (income: Double, expense: Double) {
    let cal = Calendar.current
    let monthRecords = records.filter {
        cal.isDate($0.date, equalTo: Date(), toGranularity: .month)
    }
    let income = monthRecords
        .filter { $0.type == "income" }
        .reduce(0) { $0 + $1.amount }
    let expense = monthRecords
        .filter { $0.type == "expense" }
        .reduce(0) { $0 + $1.amount }
    return (income, expense)
}
```
:::

#### 6. Приёмка: три уровня проверки + два задания со звёздочкой

Проект готов — принимайте по трём уровням «функции → границы → архитектура»: записывается ли, удаляется ли, остаются ли данные после перезапуска приложения (функции); не упадёт ли при вводе суммы 0 или отрицательного числа (границы); не перемешаны ли интерфейс с данными, нет ли жёстко вбитых значений (архитектура).

Когда базовая версия прошла приёмку, добавьте себе два «блюда повыше классом»:

1. Статистика по категориям: добавьте вкладку «Статистика» и рисуйте траты по категориям в виде круговой или столбчатой диаграммы через Swift Charts — официальная библиотека графиков Apple: пара строк кода, и диаграмма готова;
2. Синхронизация iCloud: чтобы включить iCloud у SwiftData, нужно лишь несколько настроек — книга учёта сама синхронизируется между iPhone и iPad, и проект мгновенно становится «по-взрослому».

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Практика: закончите его за эту неделю

{class="mt-1"}
Действуйте в порядке «слой данных → ViewModel → страница-список → окно ввода → карточка сводки», по шагу в день. Застряли — отдайте ошибку в первозданном виде поисковику или ИИ (помните часть 7 «Практика программирования с ИИ»? Описывая проблему, ясно формулируйте «ожидаемое поведение, фактическое поведение, шаги воспроизведения»). Когда закончите, ведите в нём учёт неделю — пользоваться приложением, сделанным своими руками, приятно, и это чувство успеха подтолкнёт вас идти дальше.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Краткие итоги главы

- Пять элементов требований → разбить на мелкие шаги, где «после каждого шага всё работает», и лишь потом браться за код
- Слой данных: модель @Model + контейнер modelContainer + запрос FetchDescriptor
- Разделение в MVVM: View только рисует, @Observable-ViewModel ведает логикой, SwiftData — хранением
- Интерфейс: List + Section + toolbar + окно ввода через sheet
- Трёхуровневая приёмка (функции / границы / архитектура) + задания со звёздочкой (Swift Charts, синхронизация iCloud)
:::
