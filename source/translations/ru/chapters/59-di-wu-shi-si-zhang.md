---
id: di-wu-shi-si-zhang
num: 54
part: an-zhuo-kai-fa-pian
nav: Глава 54: Проект 1 — мой учёт расходов (локальная версия)
toc: default
kind: chapter
---

### Глава 54. Проект 1 — моя учётная книга расходов (локальная версия)

{class="chapter-intro mb-4"}
Добро пожаловать в ваш первый «серьёзный проект». Эта учётная книга, хоть и не выходит в сеть, полнокровна: записывает траты, показывает список, сводит статистику по месяцам, умеет удалять и править. Закончив её, вы целиком пройдёте маршрут «данные → логика → интерфейс». Не спешите срисовывать код — сперва подумайте, потом делайте: это наш вечный принцип.

#### 1. Думаем о требованиях: сначала задайте пять вопросов

Прежде чем браться за дело, распутайте замысел с помощью «пяти элементов требований»:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Элемент</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ответ</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who (для кого)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Для себя; можно и для родных и друзей</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What (что делаем)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Запись доходов и расходов, список операций, сводка за месяц, статистика по категориям</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why (зачем)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Тренировка + наконец понять, куда уходят деньги</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How (как делаем)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin + Compose + Room + MVVM, всё локально, без сервера</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint (ограничения)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Уложиться в неделю; минимум — Android 8; даже без публикации писать по стандартам для релиза</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Пять элементов требований учётной книги

Дальше разбейте проект на крошечные шаги, каждый из которых «уже полезен»: ① слой данных Room (можно сохранить запись); ② экран списка (можно смотреть операции); ③ экран ввода (можно добавить запись); ④ удаление и редактирование; ⑤ карточка месячной сводки. После каждого шага приложение остаётся «вещью, которой можно пользоваться».

#### 2. Слой данных: даём записям «дом»

Сначала определите, как выглядит одна запись, — поля нужны в меру, без жадности:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Record.kt (сущность)</span><span class="dots">···</span>
:::

```
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val type: String,        // "income" доход | "expense" расход
    val amount: Double,      // сумма (в юанях)
    val category: String,    // категория: еда, транспорт, зарплата…
    val note: String = "",   // заметка (необязательно)
    val date: String         // "2026-08-15"
)
```
:::

Добавьте в Dao два «статистических» запроса — это душа учётной книги:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordDao.kt (агрегирующие запросы)</span><span class="dots">···</span>
:::

```
@Dao
interface RecordDao {
    @Query("SELECT * FROM records ORDER BY date DESC, id DESC")
    fun getAll(): Flow&lt;List&lt;Record&gt;&gt;

    @Insert
    suspend fun insert(record: Record)

    @Delete
    suspend fun delete(record: Record)

    @Query("SELECT COALESCE(SUM(amount),0) FROM records WHERE type='income' AND date LIKE :month || '%'")
    suspend fun monthIncome(month: String): Double   // month в виде "2026-08"

    @Query("SELECT COALESCE(SUM(amount),0) FROM records WHERE type='expense' AND date LIKE :month || '%'")
    suspend fun monthExpense(month: String): Double
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Совет: почему сумма — Double?

{class="mt-1"}
Строгие финансовые приложения берут BigDecimal или «Int в копейках», чтобы избежать ошибок плавающей точки (старая песня про 0.1+0.2≠0.3). Для тренировочного проекта Double хватает с избытком; если однажды сделаете настоящий финансовый продукт, вспомните про целые «копейки» — об эти грабли споткнулось неисчислимое число предшественников.
:::

#### 3. MVVM: интерфейс и логика живут раздельно

Позволить интерфейсу напрямую трогать базу? Заработает, но код интерфейса разрастётся в зловонную простыню. Архитектура MVVM разводит всех по ролям: View (интерфейс) только рисует, ViewModel (логический штаб) ведёт данными, Model (Room) отвечает за хранение.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View (интерфейс на Compose)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel (состояние и логика)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model (слой данных Room)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Рисунок 5. Трёхслойная структура MVVM — данные текут в одну сторону, слои друг к другу не лезут
:::

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordViewModel.kt (каркас)</span><span class="dots">···</span>
:::

```
class RecordViewModel(private val dao: RecordDao) : ViewModel() {

    // Превращаем Flow в наблюдаемое состояние интерфейса
    val records = dao.getAll()
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(), emptyList())

    // Действия пользователя: вызываем suspend-функции
    fun addRecord(type: String, amount: Double, category: String, note: String, date: String) {
        viewModelScope.launch {
            dao.insert(Record(type = type, amount = amount,
                category = category, note = note, date = date))
        }
    }

    fun deleteRecord(record: Record) {
        viewModelScope.launch { dao.delete(record) }
    }
}
```
:::

В интерфейсе (Compose) это работает так: val vm: RecordViewModel = viewModel(), затем val list by vm.records.collectAsState() — данные изменились, список сам обновился, а вам не нужно ничего делать. Вот сила союза MVVM + Flow + Compose.

#### 4. Интерфейс: экран списка + экран ввода

Для списка берите LazyColumn («ленивый» список) — он не тормозит даже на огромных данных:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Экран списка расходов (ключевой фрагмент)</span><span class="dots">···</span>
:::

```
@Composable
fun RecordListScreen(vm: RecordViewModel) {
    val records by vm.records.collectAsState()

    Column {
        // сводная карточка сверху (доходы - расходы = баланс)
        SummaryCard(records)

        // список операций
        LazyColumn {
            items(records, key = { it.id }) { record -&gt;
                RecordRow(record) { vm.deleteRecord(record) }
            }
        }

        // плавающая кнопка «новая запись» → открывает диалог ввода
        FloatingActionButton(onClick = { showAddDialog = true }) {
            Text("+")
        }
    }
}

@Composable
fun RecordRow(record: Record, onDelete: () -&gt; Unit) {
    Row(Modifier.fillMaxWidth().padding(12.dp)) {
        Text(record.category, fontWeight = FontWeight.Bold)
        Spacer(Modifier.weight(1f))
        Text(if (record.type == "income") "+${record.amount}" else "-${record.amount}",
             color = if (record.type == "income") Color(0xFF27AE60) else Color(0xFFC0392B))
    }
}
```
:::

Для ввода проще всего AlertDialog (диалог): несколько полей ввода + переключатель доход/расход + выпадающий список категорий; по «ОК» вызывается vm.addRecord(...).

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Внимание: проверяйте ввод, не ленитесь

{class="mt-1"}
Поле суммы проверять обязательно: пустое значение, отрицательное число, «abc» — всё это надо отсекать (удобно через toDoubleOrNull()). Одна из самых частых причин падений приложения — «считать пользовательский ввод примерным отличником». Запомните: всё, что вводит пользователь, проверяйте как врага на границе.
:::

#### 5. Редактирование и удаление: данным нужен и «вход», и «выход»

Учётная книга, которая умеет только добавлять, но не удалять, надоедает за три дня. Добавьте две операции:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Удаление и правка</span><span class="dots">···</span>
:::

```
// Добавим в Dao ещё два метода:
@Query("UPDATE records SET amount=:amount, category=:category, note=:note WHERE id=:id")
suspend fun update(id: Long, amount: Double, category: String, note: String)

@Query("DELETE FROM records WHERE id=:id")
suspend fun deleteById(id: Long)

// В интерфейсе: долгое нажатие на пункт списка открывает меню «правка/удалить» (в Compose — DropdownMenu или AlertDialog)
// Перед удалением лучше показать подтверждение — случайное удаление больше всего ненавидят пользователи финансовых приложений
```
:::

Два правила взаимодействия: удаление — только с повторным подтверждением (защита от случайного нажатия), при редактировании по возможности подставляйте прежние значения (исправить один знак проще, чем вводить заново). Не недооценивайте эти мелочи — из таких мелочей и складывается ощущение настоящего продукта.

#### 6. Приёмка: три уровня проверки + два задания со звёздочкой

Закончив проект, проведите приёмку по трём уровням «функциональность → крайние случаи → архитектура»: записывается ли, удаляется ли, остаются ли данные после перезапуска (функциональность); не падает ли при вводе суммы 0 или отрицательного числа, не теряются ли данные при повороте экрана (крайние случаи); не смешались ли интерфейс с данными, нет ли вписанных напрямую значений (архитектура).

Как только базовая версия пройдёт приёмку, добавьте себе два «блюда со звёздочкой»:

1. Фильтр по месяцам: сверху переключатель месяца (например, 2026-08 ▾), и в списке остаются операции только выбранного месяца;
2. Круговая диаграмма по категориям: через Canvas в Compose или лёгкую библиотеку диаграмм нарисуйте «куда ушли деньги» пирогом — с ней учётная книга уже похожа на продукт.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Практика: доделайте за эту неделю

{class="mt-1"}
Двигайтесь по порядку «слой данных → ViewModel → экран списка → экран ввода → карточка сводки», шаг в день. Застряли — швыряйте текст ошибки как есть в поисковик или ИИ (помните седьмой раздел «Практика программирования с ИИ»? Описывая проблему, чётко назовите «ожидаемое поведение, фактическое поведение, шаги воспроизведения»). Когда доделаете, ведите в нём учёт неделю — пользоваться приложением собственного изготовления так приятно, что оно само понесёт вас дальше.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Коротко о главном

- Пять элементов требований → разбить на маленькие шаги, каждый из которых полезен, — и лишь потом браться за дело
- Слой данных: сущность Record + Dao (включая SQL для месячной статистики) + Database
- Разделение в MVVM: View только рисует, ViewModel ведёт логику, Model хранит
- Flow + stateIn + collectAsState: данные изменились — интерфейс обновился сам
- LazyColumn — «ленивый» список; AlertDialog — для ввода
- Трёхуровневая приёмка (функциональность / крайние случаи / архитектура) + задания со звёздочкой (фильтр по месяцам, круговая диаграмма)
:::
