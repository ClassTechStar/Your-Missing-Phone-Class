---
id: di-liu-shi-wu-zhang
num: 65
part: ios-kai-fa-pian
nav: Chapter 65: Project 1 — My Expense Tracker (Local Version)
toc: default
kind: chapter
---

### Chapter 65: Project One—My Expense Tracker (Local Version)

{class="chapter-intro mb-4"}
Welcome to your first "serious project." This expense tracker never touches the internet, but it's complete in every part: you can record a transaction, view the running history, see monthly totals, and edit or delete entries. Finishing it means you've walked the whole "data → logic → interface" path end to end. Don't rush to copy code—think it through first, then build. That's our standing principle.

#### 1. Thinking About Requirements: Ask Five Questions First

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Element</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Answer</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who (who's it for)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">For yourself; family and friends too</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What (what it does)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Record income and spending, view the history, monthly summaries, statistics by category</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why (the reason)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Practice + finding out where the money goes</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How (the approach)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift + SwiftUI + SwiftData + MVVM, purely local, no backend</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint (the limits)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Done within one week; supports iOS 17 at minimum (the SwiftData requirement)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
The five requirement elements of the expense tracker

Then break it into small steps where "every step is usable": 1) build the SwiftData data layer (can save a transaction); 2) the list screen (can view the history); 3) the entry sheet (can add a transaction); 4) deleting and editing; 5) the monthly summary card. After every step, the app is a "usable thing."

#### 2. The Data Layer: Giving Transactions a Home

First, define what a transaction looks like—enough fields to do the job, but don't get greedy:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Record.swift (the model)</span><span class="dots">···</span>
:::

```
import SwiftData

@Model
class Record {
    var type: String      // "income" = money in | "expense" = money out
    var amount: Double    // amount (in yuan)
    var category: String  // category: food, transport, salary...
    var note: String      // note (optional)
    var date: Date        // expense date

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
Tip: Why Use Double for Amounts?

{class="mt-1"}
Rigorous financial apps use Decimal (exact decimal arithmetic) to avoid floating-point errors (the old 0.1 + 0.2 ≠ 0.3 problem). Double is plenty for a practice project; if you ever build a real financial product, remember to switch to Decimal or "an Int counted in cents"—a pitfall countless developers before you have stumbled into.
:::

#### 3. MVVM: When Interface and Logic "Move Apart"

Let the interface talk to the database directly? It runs, but the interface code becomes bloated and ugly. The MVVM architecture gives each part its own job: the View (interface) only draws, the ViewModel (logic hub) manages the data, and the Model (SwiftData) handles storage.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View (the SwiftUI interface)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel (the @Observable logic hub)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model (the SwiftData data layer)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figure 4: MVVM's three layers—data flows in one direction, and no layer oversteps its bounds
:::

::: div .code-block
:::inline div .code-head
<span>SWIFT · RecordViewModel.swift (skeleton)</span><span class="dots">···</span>
:::

```
import Observation

@Observable
class RecordViewModel {
    var records: [Record] = []
    private let context: ModelContext

    init(context: ModelContext) { self.context = context }

    func load() {
        // filtering + sorting with SwiftData's #Predicate
        let descriptor = FetchDescriptor<Record>(
            sortBy: [SortDescriptor(\.date, order: .reverse)]
        )
        records = (try? context.fetch(descriptor)) ?? []
    }

    func add(type: String, amount: Double, category: String, note: String) {
        let r = Record(type: type, amount: amount, category: category, note: note)
        context.insert(r)
        try? context.save()
        load()                       // reload; the UI refreshes
    }

    func delete(_ record: Record) {
        context.delete(record)
        try? context.save()
        load()
    }
}
```
:::

In the interface, write @State private var vm = RecordViewModel(...), then render the list straight from vm.records—the moment the data changes, the interface refreshes automatically.

#### 4. The Interface: List Screen + Entry Sheet

::: div .code-block
:::inline div .code-head
<span>SWIFT · Expense list screen (core excerpt)</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var vm: RecordViewModel
    @State private var showAdd = false

    var body: some View {
        NavigationStack {
            List {
                Section("This month's balance") {          // summary card
                    SummaryRow(records: vm.records)
                }
                Section("Transactions") {
                    ForEach(vm.records) { r in
                        RecordRow(record: r)
                    }
                    .onDelete { idx in
                        idx.forEach { vm.delete(vm.records[$0]) }
                    }
                }
            }
            .navigationTitle("My expense tracker")
            .toolbar {
                Button { showAdd = true } label: {
                    Image(systemName: "plus")
                }
            }
            .sheet(isPresented: $showAdd) {
                AddRecordView(vm: vm)          // the entry dialog
            }
        }
    }
}
```
:::

Entry sheet essentials: use .keyboardType(.decimalPad) for the amount field (a number pad), a segmented control (Picker) for income/expense, a menu picker for the category, and on "Save," call vm.add(...) and dismiss() to close the sheet.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Note: Don't Get Lazy with Input Validation

{class="mt-1"}
Always validate the amount field: block empty values, negative numbers, and invalid input like "abc" (check with Double(text), which returns nil on failure). One of the most common reasons apps crash is "treating the user's input like a well-behaved child." Remember: treat everything the user types as hostile until proven otherwise.
:::

#### 5. Editing, Deleting, and Summaries

- Delete: List's .onDelete swipe-to-delete plus a confirmation dialog (accidental deletion is what users of expense apps hate most);
- Edit: tapping a row opens an edit sheet pre-filled with the original values (fixing one word beats retyping everything);
- Summaries: use filter + reduce to compute "this month's income / spending / balance," shown in a card at the top:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Monthly totals calculation</span><span class="dots">···</span>
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

#### 6. Acceptance: A Three-Layer Check + Two Advanced Challenges

When the project is done, run acceptance across three layers—"function → edge cases → architecture": can you record and delete, and does the data survive restarting the app (function); does entering 0 or a negative amount crash it (edge cases); are interface and data mixed together, and are any fields hard-coded (architecture)?

Once the basic version passes acceptance, serve yourself two "advanced dishes":

1. Category statistics: add a "Stats" tab and use Swift Charts to draw category spending as a pie chart or bar chart—Apple's official charting library, charts in just a few lines of code;
2. iCloud sync: With SwiftData, turning on iCloud sync only takes a few settings—the ledger syncs automatically between iPhone and iPad, and instantly feels "pro."

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Get hands-on: finish it this week

{class="mt-1"}
Work in the order "data layer → ViewModel → list page → entry sheet → summary card," one step a day. If you get stuck, paste the error message straight into a search engine or an AI (remember Part 7, "Hands-On AI Coding"? When describing a problem, clearly state the "expected behavior, actual behavior, and steps to reproduce"). Once it's done, use it to track a week of expenses—using an app you built yourself gives you a sense of accomplishment that will push you forward.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Chapter summary

- Five elements of a requirement → break it into small, "usable at every step" steps, then start building
- Data layer: @Model models + the modelContainer container + FetchDescriptor queries
- MVVM division of labor: the View only draws, the @Observable ViewModel handles logic, SwiftData handles storage
- UI: List + Section + toolbar + a sheet for the entry dialog
- Three-layer acceptance (features/edge cases/architecture) + advanced challenges (Swift Charts, iCloud sync)
:::
