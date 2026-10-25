---
id: di-liu-shi-wu-zhang
num: 65
part: ios-kai-fa-pian
nav: 第六十五章：項目一——吾之記賬本（本地版）
toc: default
kind: chapter
---

### 第六十五章：項目一——吾之記賬本（本地版）

{class="chapter-intro mb-4"}
迎汝入首個「正經之項」。此記賬本雖不連網，然五臟悉備：能記一筆之賬、能觀流水、能按月統計、能刪改。成之，則「數據 → 邏輯 → 界面」之全流程已遍歷矣。勿遽抄代碼——先思之審而後動手，此吾儕一貫之則也。

#### 一、思其所需：先問五事

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要素</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">答案</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who（為誰而作）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自用，家人朋友亦可</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What（作何事）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">記收支、觀流水、按月彙總、按類統計</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why（何為）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">練手 + 明錢之所往</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How（何以為之）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift + SwiftUI + SwiftData + MVVM，純本地而無後端</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint（約束）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一週內成之；最低須支 iOS 17（SwiftData 之檻）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
記賬本所需五要素

繼而析為「步步可用」之小程：① 建 SwiftData 數據層（能貯一賬）；② 列表頁（能觀流水）；③ 錄入彈窗（能增賬）；④ 刪與編；⑤ 月度彙總之卡。每成一程，App 皆「可用之物」也。

#### 二、數據層：使「賬」有其所

先定一賬之形——字段足用即可，勿貪多：

::: div .code-block
:::inline div .code-head
<span>SWIFT · Record.swift（模型）</span><span class="dots">···</span>
:::

```
import SwiftData

@Model
class Record {
    var type: String      // "income" 收入 | "expense" 支出
    var amount: Double    // 金額（元）
    var category: String  // 分類：餐飲、交通、薪俸……
    var note: String      // 備註（可選）
    var date: Date        // 記賬日期

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
小貼士：金額何以用 Double？

{class="mt-1"}
嚴謹之金融 App 用 Decimal（精確十進制）以避浮點之差（0.1+0.2≠0.3 之舊惑）。練手之項用 Double 足矣；他日若作真金融之品，宜易為 Decimal 或「以分為單位之 Int」——此無數先輩所踐之坑也。
:::

#### 三、MVVM：界面與邏輯「分家」

徑使界面操數據庫乎？可行，然界面之碼將冗長可憎。MVVM 之構使各司其職：View（界面）惟司繪，ViewModel（邏輯之樞）司數據，Model（SwiftData）司存貯。

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View（SwiftUI 界面）</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel（@Observable 邏輯中樞）</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model（SwiftData 數據層）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 4：MVVM 三層之構——數據單向而流，各層互不越界
:::

::: div .code-block
:::inline div .code-head
<span>SWIFT · RecordViewModel.swift（骨架）</span><span class="dots">···</span>
:::

```
import Observation

@Observable
class RecordViewModel {
    var records: [Record] = []
    private let context: ModelContext

    init(context: ModelContext) { self.context = context }

    func load() {
        // SwiftData 之 #Predicate 篩選 + 排序
        let descriptor = FetchDescriptor<Record>(
            sortBy: [SortDescriptor(\.date, order: .reverse)]
        )
        records = (try? context.fetch(descriptor)) ?? []
    }

    func add(type: String, amount: Double, category: String, note: String) {
        let r = Record(type: type, amount: amount, category: category, note: note)
        context.insert(r)
        try? context.save()
        load()                       // 重載，界面自新
    }

    func delete(_ record: Record) {
        context.delete(record)
        try? context.save()
        load()
    }
}
```
:::

界面中 @State private var vm = RecordViewModel(...)，遂徑以 vm.records 渲列表——數據一變，界面自刷。

#### 四、界面：列表頁 + 錄入彈窗

::: div .code-block
:::inline div .code-head
<span>SWIFT · 記賬列表頁（核心片段）</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var vm: RecordViewModel
    @State private var showAdd = false

    var body: some View {
        NavigationStack {
            List {
                Section("本月結餘") {          // 匯總卡片
                    SummaryRow(records: vm.records)
                }
                Section("流水") {
                    ForEach(vm.records) { r in
                        RecordRow(record: r)
                    }
                    .onDelete { idx in
                        idx.forEach { vm.delete(vm.records[$0]) }
                    }
                }
            }
            .navigationTitle("吾之記賬本")
            .toolbar {
                Button { showAdd = true } label: {
                    Image(systemName: "plus")
                }
            }
            .sheet(isPresented: $showAdd) {
                AddRecordView(vm: vm)          // 錄入彈窗
            }
        }
    }
}
```
:::

錄入彈窗之要：金額輸入框之鍵盤用 .keyboardType(.decimalPad)（數字鍵盤），收入/支出用分段之控件（Picker），分類以菜單擇之，點「保存」則調 vm.add(...) 並 dismiss() 以闔窗。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
按：輸入之驗勿懈

{class="mt-1"}
金額輸入框必驗之：空值、負數、"abc" 之類非法輸入皆當攔（以 Double(text) 審之，不遂則返 nil）。App 之崩，其常因之一，即「視用戶之輸為馴良」。謹記：凡用戶所輸，皆當如敵而察之。
:::

#### 五、編、刪與彙總

- 刪：List 之 .onDelete 左滑而刪 + 確認彈窗（誤刪者，記賬類 App 用戶之所深憾也）；
- 編：點行入編輯彈窗，預填舊值（易一字較重輸為省）；
- 彙總：以 filter + reduce 算「本月收入 / 支出 / 結餘」，頂部之卡陳之：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 月度彙總計算</span><span class="dots">···</span>
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

#### 六、驗收：三層之檢 + 二進階之挑戰

項既成，按「功能 → 邊界 → 構架」三層驗之：能記否、能刪否、重啟 App 而數據存否（功能）；金額輸 0 或負數，崩否（邊界）；界面與數據有無相混、字段有無硬編（構架）。

基礎版驗過，則自加二道「進階之饌」：

1. 分類統計：增「統計」標籤頁，以 Swift Charts 繪分類支出為餅圖/柱狀圖——蘋果官方圖表之庫，數行碼而圖成；
2. iCloud 同步：SwiftData 開 iCloud 同步，惟須配數項設置——賬本於 iPhone/iPad 之間自同步，頓覺「高級」矣。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：本週成之

{class="mt-1"}
按「數據層 → ViewModel → 列表頁 → 錄入彈窗 → 彙總卡片」之序而動手，日進一程。困則以報錯原文擲於搜索引擎或 AI（尚憶第七篇《AI編程實戰篇》乎？述問題時，明言「期望之行、實際之行、復現之步」）。成則以之記賬一週——自作之 App 自用之，成就之感將推汝前行。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小結

- 所需五要素 → 析為「步步能用」之小程，而後動手
- 數據層：@Model 之模 + modelContainer 之器 + FetchDescriptor 之詢
- MVVM 分職：View 惟司繪，@Observable 之 ViewModel 司邏輯，SwiftData 司存貯
- 界面：List + Section + toolbar + sheet 錄入彈窗
- 三層驗收（功能/邊界/構架）+ 進階挑戰（Swift Charts、iCloud 同步）
:::
