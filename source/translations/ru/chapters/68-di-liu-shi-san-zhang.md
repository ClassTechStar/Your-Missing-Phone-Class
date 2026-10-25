---
id: di-liu-shi-san-zhang
num: 63
part: ios-kai-fa-pian
nav: Глава 63: Виды, состояние и навигация
toc: default
kind: chapter
---

### Глава 63. Представления, состояние и навигация

{class="chapter-intro mb-4"}
Делать игрушки из одного экрана вы уже умеете. Эта глава решает две проблемы «повзросления»: как перемещаться между несколькими экранами (навигация) и как данные текут между экранами (управление состоянием). Пройдя её, вы сможете собрать классический скелет многоэкранного приложения «список → детали → редактирование».

#### 1. «Панорама потоков данных» в управлении состоянием

У SwiftUI не один инструмент состояния — не только @State. Сначала взгляните на панораму и разберитесь, «когда что использовать»:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Инструмент</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">За что отвечает</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Кто использует</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Типичный сценарий</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">временное состояние, приватное для экрана</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">текущее представление</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">счётчик, текст в поле ввода</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Binding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">заимствование чужого состояния</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">дочернее представление меняет родительское</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">свои компоненты</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@StateObject / @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">логика, общая для нескольких экранов</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">модель представления (ViewModel)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">загрузка данных, бизнес-логика</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@EnvironmentObject / .environment</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">глобальное общее состояние</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">всё приложение</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">статус входа пользователя, настройки темы</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Панорама инструментов состояния SwiftUI (2026 год, @Observable уже мейнстрим)

::: div .code-block
:::inline div .code-head
<span>SWIFT · Мейнстрим 2026: модели представлений с @Observable</span><span class="dots">···</span>
:::

```
// Современный способ на iOS 17+: макрос @Observable (рекомендуется для новых проектов)
import Observation

@Observable
class CounterModel {                 // модель представления
    var count = 0
    func increment() { count += 1 }
}

struct CounterView: View {
    @State private var model = CounterModel()   // хранит модель

    var body: some View {
        VStack {
            Text("Вы нажали \(model.count) раз")
            Button("Нажми") { model.increment() }
        }
    }
}
```
:::

Грубый совет новичку: для приватного состояния экрана — @State, для межэкранного/с логикой — классы @Observable. @StateObject/@ObservableObject из старых учебников — вчерашний стиль: достаточно уметь читать, а новый код пишите, как сказано выше.

#### 2. NavigationStack: «стек» переходов между экранами

Начиная с iOS 16, навигация по нескольким экранам строится на NavigationStack — как стопка тарелок: кладёшь одну сверху, при возврате снимаешь по одной:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Навигация через NavigationStack</span><span class="dots">···</span>
:::

```
struct HomeView: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("Записная книжка Ивана") {
                    DetailView(name: "Записная книжка Ивана")   // целевой экран
                }
                NavigationLink("Записная книжка Марии") {
                    DetailView(name: "Записная книжка Марии")
                }
            }
            .navigationTitle("Список записных книжек")   // крупный заголовок сверху
        }
    }
}

struct DetailView: View {
    let name: String
    var body: some View {
        Text("Подробности: \(name)")
            .navigationTitle(name)
            .navigationBarTitleDisplayMode(.inline)
    }
}
```
:::

NavigationLink — «кликабельная ссылка-переход»; navigationTitle автоматически создаёт заголовок панели навигации и кнопку «назад». Когда нужен программный переход (например, автоматический возврат после нажатия «Сохранить»), закрывайте текущий экран через @Environment(\.dismiss) — этих двух приёмов хватает на 90% навигационных задач.

#### 3. Всплывающие окна и нижние вкладки: sheet и TabView

Кроме «проталкивания экранов», есть ещё два классических приёма взаимодействия:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Диалоги sheet + вкладки TabView</span><span class="dots">···</span>
:::

```
// 1. Выезжает снизу на пол/весь экран (любимый приём для форм ввода)
struct HomeView: View {
    @State private var showAdd = false
    var body: some View {
        Button("Новая запись") { showAdd = true }
            .sheet(isPresented: $showAdd) {
                AddRecordView()     // появляющаяся форма ввода
            }
    }
}

// 2. Нижняя панель вкладок ("скелет" приложения)
struct MainTabView: View {
    var body: some View {
        TabView {
            RecordListView()
                .tabItem { Label("Записи", systemImage: "book") }
            StatsView()
                .tabItem { Label("Статистика", systemImage: "chart.pie") }
            SettingsView()
                .tabItem { Label("Настройки", systemImage: "gear") }
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Совет: когда что использовать?

{class="mt-1"}
Эмпирическое правило: основной поток строим на NavigationStack (список → детали), временные действия — во всплывающем окне sheet (добавление, правка, подтверждение), несколько равноправных крупных разделов — в TabView (вкладки внизу). Вместе эти три элемента — скелет подавляющего большинства приложений.
:::

#### 4. List: «народный список» iOS

Самый ходовой и самый «яблочный» компонент в iOS — List: разделители, удаление свайпом и подсветка нажатия идут у него из коробки:

::: div .code-block
:::inline div .code-head
<span>SWIFT · List + удаление свайпом</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var records = ["Обед 25.5", "Метро 6.0", "Зарплата +8000"]

    var body: some View {
        List {
            ForEach(records, id: \.self) { r in
                Text(r)
            }
            .onDelete { indexSet in          // свайп влево — удалить
                records.remove(atOffsets: indexSet)
            }
        }
    }
}
```
:::

Список + NavigationLink + sheet + TabView — соединив эти четыре элемента, вы уже способны собрать полный скелет приложения «список записей → открыть детали → нажать + и добавить запись». Именно так построен проект книги учёта в следующей главе.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Практика: соберите «каркас из трёх страниц»

#### 5. Жизненный цикл приложения: передний план и фон

Подобно жизненному циклу Activity в Android, приложение iOS проходит состояния «рождение, передний план, фон, смерть». В SwiftUI за ними наблюдают через значение окружения scenePhase:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Отслеживаем переходы передний/задний план</span><span class="dots">···</span>
:::

```
@main
struct MyApp: App {
    @Environment(\.scenePhase) private var phase

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .onChange(of: phase) { _, newPhase in
            switch newPhase {
            case .active:    print("Снова на переднем плане, возобновляем обновление")
            case .inactive:  print("Переход (звонок / мгновение в фоне)")
            case .background: print("Ушёл в фон, сохраняем черновик")
            @unknown default: break
            }
        }
    }
}
```
:::

Типичное применение: обновить данные при возвращении на передний план, сохранить черновик при уходе в фон. iOS очень строго следит за фоновой работой — обычное приложение вскоре после ухода в фон приостанавливается («замораживается»), так что не рассчитывайте тайком делать в фоне тяжёлую работу; если нужны задачи по расписанию, используйте локальные уведомления из главы 68, а не «вечное проживание в фоне».

{class="mt-1"}
Соберите скелет книги учёта на фиктивных данных: TabView с тремя вкладками (Книга / Статистика / Настройки) → страница книги через List показывает фиктивные данные, нажатие на строку ведёт к деталям (NavigationStack) → кнопка «+» в правом верхнем углу открывает sheet для ввода. Данные не сохраняются, сеть не используется — чистая тренировка каркаса; когда скелет готов, наполнить его настоящими данными в главе 65 будет уже делом техники.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Краткие итоги главы

- Четыре инструмента состояния: @State (приватно для страницы), @Binding (заимствование), @Observable (логика), .environment (глобально)
- В новых проектах пишите модель представления макросом @Observable; @ObservableObject из старых уроков достаточно уметь читать
- NavigationStack открывает страницы; @Environment(\.dismiss) — программный возврат назад
- Основной поток — страницы, временные действия — sheet, равноправные крупные разделы — TabView
- List — «народный список»: разделители и удаление свайпом доступны из коробки
:::
