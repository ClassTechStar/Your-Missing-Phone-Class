---
id: di-wu-shi-si-zhang
num: 54
part: an-zhuo-kai-fa-pian
nav: Chapter 54: Project 1 — My Expense Tracker (Local Version)
toc: default
kind: chapter
---

### Chapter 54: Project 1 — My Expense Tracker (Local Version)

{class="chapter-intro mb-4"}
Welcome to your first "real project." This expense tracker never goes online, but it has everything it needs: record a transaction, view the ledger, see monthly summaries, delete and edit. Finishing it means you've walked the full "data → logic → UI" pipeline from start to end. Don't rush to copy code — think it through first, then build. That's our standing principle.

#### 1. Thinking Through Requirements: Ask Five Questions First

Before building, sort out the idea with the "five elements of a requirement":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Element</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Answer</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who (who's it for)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Me; family and friends are fine too</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What (what it does)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Record income and spending, view the ledger, monthly summaries, category breakdowns</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why (the reason)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Practice + figuring out where the money goes</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How (the approach)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin + Compose + Room + MVVM, fully local, no backend</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint (the limits)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Done within a week; supports Android 8 at minimum; written to store standards even if never published</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
The five requirement elements of the expense tracker

Then break it into small steps where "every step is usable": (1) build the Room data layer (can save one transaction); (2) the list screen (can view the ledger); (3) the entry screen (can add a transaction); (4) delete and edit; (5) a monthly summary card. After each step, the app is something "that works."

#### 2. The Data Layer: Giving Each Transaction a Home

First define what one transaction looks like — enough fields to be useful, but don't get greedy:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Record.kt (the entity)</span><span class="dots">···</span>
:::

```
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val type: String,        // "income" = money in | "expense" = money out
    val amount: Double,      // amount (in yuan)
    val category: String,    // category: food, transport, salary...
    val note: String = "",   // note (optional)
    val date: String         // "2026-08-15"
)
```
:::

Add two "summary" queries to the Dao — these are the soul of the tracker:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordDao.kt (aggregate queries)</span><span class="dots">···</span>
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
    suspend fun monthIncome(month: String): Double   // month looks like "2026-08"

    @Query("SELECT COALESCE(SUM(amount),0) FROM records WHERE type='expense' AND date LIKE :month || '%'")
    suspend fun monthExpense(month: String): Double
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tip: why use Double for amounts?

{class="mt-1"}
Rigorous finance apps use BigDecimal or "an Int counted in cents" to avoid floating-point errors (the old 0.1 + 0.2 ≠ 0.3 problem). For a practice project, Double is plenty; if you ever build a real financial product, remember to switch to cents as the unit — it's a pitfall countless developers before you have stumbled into.
:::

#### 3. MVVM: UI and Logic "Live Apart"

Let the UI talk to the database directly? It runs, but the UI code turns long and ugly. The MVVM architecture gives each part its own job: the View (UI) only draws, the ViewModel (the logic hub) handles data, and the Model (Room) handles storage.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View (the Compose UI)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel (state and logic)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model (the Room data layer)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figure 5: The three layers of MVVM — data flows in one direction, and no layer crosses into another
:::

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordViewModel.kt (skeleton)</span><span class="dots">···</span>
:::

```
class RecordViewModel(private val dao: RecordDao) : ViewModel() {

    // Turn the Flow into observable UI state
    val records = dao.getAll()
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(), emptyList())

    // User actions: call suspend functions
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

In the UI (Compose) you'd write: val vm: RecordViewModel = viewModel(), then val list by vm.records.collectAsState() — the moment the data changes, the list refreshes by itself, and you do nothing. That's the power of MVVM + Flow + Compose working as one.

#### 4. The UI: List Screen + Entry Screen

The list screen uses LazyColumn (a lazy-loading list) — smooth no matter how much data:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Expense list screen (core excerpt)</span><span class="dots">···</span>
:::

```
@Composable
fun RecordListScreen(vm: RecordViewModel) {
    val records by vm.records.collectAsState()

    Column {
        // summary card at the top (income - expenses = balance)
        SummaryCard(records)

        // the transactions list
        LazyColumn {
            items(records, key = { it.id }) { record -&gt;
                RecordRow(record) { vm.deleteRecord(record) }
            }
        }

        // floating "add entry" button → opens the entry dialog
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

An AlertDialog (dialog) is the easiest way to enter data: a few input fields + an income/expense toggle + a category dropdown; tap OK and it calls vm.addRecord(...).

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Note: don't skimp on input validation

{class="mt-1"}
Always validate the amount field: empty values, negative numbers, and illegal input like "abc" must all be blocked (check with toDoubleOrNull()). One of the most common reasons apps crash is "trusting the user's input like a well-behaved child." Remember: treat everything the user types as hostile until proven otherwise.
:::

#### 5. Edit and Delete: Let Data "Come and Go"

An expense tracker that can only add and never delete is useless within three days. Add two more operations:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Deleting and editing</span><span class="dots">···</span>
:::

```
// Add two more to the Dao:
@Query("UPDATE records SET amount=:amount, category=:category, note=:note WHERE id=:id")
suspend fun update(id: Long, amount: Double, category: String, note: String)

@Query("DELETE FROM records WHERE id=:id")
suspend fun deleteById(id: Long)

// In the UI: long-press a list item to open an "edit/delete" menu (use DropdownMenu or AlertDialog in Compose)
// Best to confirm before deleting — accidental deletion is what expense-app users hate most
```
:::

Two bits of interaction wisdom: deleting always needs a second confirmation (to prevent fat-finger slips), and editing should pre-fill the original values (fixing one character beats retyping everything). Don't underestimate these details — that "polished product" feel is built exactly from details like these.

#### 6. Acceptance: a three-layer check + two advanced challenges

When the project is done, accept it across three layers: "features → edge cases → architecture." Can you record and delete, is the data still there after reopening the app (features); does entering 0 or a negative amount crash it, does rotating the screen lose data (edge cases); are UI and data tangled together, are any fields hard-coded (architecture).

Once the basic version passes acceptance, serve yourself two "advanced dishes":

1. Monthly filter: add a month switcher at the top (e.g., 2026-08 ▾) so the list shows only that month's transactions;
2. Category pie chart: use Compose's Canvas or add a lightweight charting library to draw "where the money went" as a pie chart — finish this and the tracker starts to look like a real product.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Hands-on: finish it this week

{class="mt-1"}
Build in this order: "data layer → ViewModel → list screen → entry screen → summary card," one step a day. When stuck, paste the error as-is into a search engine or an AI (remember Part 7, "AI Coding in Practice"? When describing a problem, spell out the "expected behavior, actual behavior, and steps to reproduce"). Once it's done, track a week of spending with it — using an app you built yourself gives you a sense of achievement that pushes you forward.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Chapter Summary

- Five requirement elements → break into "every step usable" small steps, then start building
- Data layer: the Record entity + Dao (including monthly-summary SQL) + Database
- MVVM division of labor: the View only draws, the ViewModel runs the logic, the Model handles storage
- Flow + stateIn + collectAsState: the UI refreshes automatically when data changes
- LazyColumn for lazy-loading lists; AlertDialog for data entry
- Three-layer acceptance (features/edge cases/architecture) + advanced challenges (monthly filter, category pie chart)
:::
