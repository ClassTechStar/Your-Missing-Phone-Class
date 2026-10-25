---
id: di-liu-shi-wu-zhang
num: 65
part: ios-kai-fa-pian
nav: 第六十五章：項目一——我嘅記賬本（本地版）
toc: default
kind: chapter
---

### 第六十五章：項目一——我嘅記賬本（本地版）

{class="chapter-intro mb-4"}
歡迎嚟到你第一個"正經項目"。呢個記賬本雖然唔上網，但五臟俱全：記到一筆賬、睇到流水、統計到每月、又刪改到。做完佢，你就完整行咗一次"數據 → 邏輯 → 界面"嘅全流程。咪心急抄代碼——先諗清楚先動手，呢個係我哋一貫嘅原則。

#### 一、需求思考：先問五個問題

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要素</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">答案</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who（畀邊個用）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自己用，屋企人朋友都得</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What（做乜嘢）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">記收支、睇流水、按月匯總、按分類統計</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why（點解）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">練手 + 搞清楚啲錢花咗去邊</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How（點樣做）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift + SwiftUI + SwiftData + MVVM，純本地冇後端</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint（約束）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一星期內完成；最低支援 iOS 17（SwiftData 門檻）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
記賬本需求五要素

然後拆解成"每一步都用得"嘅小步驟：① 建 SwiftData 數據層（存到一筆賬）；② 列表頁（睇到流水）；③ 錄入彈窗（加到賬）；④ 刪除同編輯；⑤ 月度匯總卡片。每完成一步，App 都係一件"用得嘅嘢"。

#### 二、數據層：畀"賬"有個屋企

先定義一筆賬生乜嘢樣——字段要夠用但咪貪多：

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
    var category: String  // 分類：餐飲、交通、人工……
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
小貼士：金額點解用 Double？

{class="mt-1"}
嚴謹嘅金融 App 會用 Decimal（精確十進制）嚟避免浮點誤差（0.1+0.2≠0.3 呢個老問題）。練手項目用 Double 就夠；如果第日做真金融產品，記得換成 Decimal 或者"以分為單位嘅 Int"——呢個係無數前輩踩出嚟嘅坑。
:::

#### 三、MVVM：界面同邏輯"分家"

直接畀界面操作數據庫？行得，但界面代碼會又臭又長。MVVM 架構令大家各司其職：View（界面）淨係管畫，ViewModel（邏輯中樞）管數據，Model（SwiftData）管存儲。

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View（SwiftUI 界面）</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel（@Observable 邏輯中樞）</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model（SwiftData 數據層）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 4：MVVM 三層結構——數據單向流動，各層互不越界
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
        // SwiftData 嘅 #Predicate 篩選 + 排序
        let descriptor = FetchDescriptor<Record>(
            sortBy: [SortDescriptor(\.date, order: .reverse)]
        )
        records = (try? context.fetch(descriptor)) ?? []
    }

    func add(type: String, amount: Double, category: String, note: String) {
        let r = Record(type: type, amount: amount, category: category, note: note)
        context.insert(r)
        try? context.save()
        load()                       // 重新載入，界面刷新
    }

    func delete(_ record: Record) {
        context.delete(record)
        try? context.save()
        load()
    }
}
```
:::

界面入面 @State private var vm = RecordViewModel(...)，然後直接用 vm.records 渲染列表——數據一變，界面自動刷新。

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
                Section("本月結餘") {          // 彙總卡片
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
            .navigationTitle("我嘅記賬本")
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

錄入彈窗要點：金額輸入框鍵盤用 .keyboardType(.decimalPad)（數字鍵盤），收入／支出用分段控件（Picker），分類用菜單揀，㩒"保存"就調用 vm.add(...) 同 dismiss() 關窗。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：輸入校驗咪偷懶

{class="mt-1"}
金額輸入框一定要校驗：空值、負數、"abc" 呢類非法輸入都要攔住（用 Double(text) 判斷，失敗返回 nil）。App 崩潰最常見嘅原因之一就係"將用戶嘅輸入當成乖仔"。記住：用戶輸入嘅所有嘢，都要當敵人咁審查。
:::

#### 五、編輯、刪除同匯總

- 刪除：List 嘅 .onDelete 左滑刪除 + 確認彈窗（刪錯嘢係記賬類 App 用戶最憎嘅事）；
- 編輯：㩒行入編輯彈窗，預填原本嘅值（改一個字好過重新輸入）；
- 匯總：用 filter + reduce 計"本月收入 / 支出 / 結餘"，頂部卡片展示：

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

#### 六、驗收：三層檢查 + 兩個進階挑戰

項目做完，按"功能 → 邊界 → 架構"三層驗收：記唔記到、刪唔刪到、重啟 App 數據仲喺唔喺度（功能）；金額輸 0 或者負數會唔會崩（邊界）；界面同數據有冇溝埋一齊、字段有冇硬編碼（架構）。

基礎版驗收通過之後，畀自己加兩味"進階菜"：

1. 分類統計：加一個"統計"標籤頁，用 Swift Charts 將分類支出畫成餅圖／柱狀圖——蘋果官方圖表庫，幾行代碼出圖；
2. iCloud 同步：SwiftData 開 iCloud 同步只需要配幾項設定——賬本喺 iPhone/iPad 之間自動同步，即刻"高級"咗。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
嚟動手：今個禮拜完成佢

{class="mt-1"}
按"數據層 → ViewModel → 列表頁 → 錄入彈窗 → 匯總卡片"嘅次序動手，每日一步。卡住咗就將報錯原原本本掟畀搜尋引擎或者 AI（仲記唔記得第七篇《AI編程實戰篇》呀？描述問題嗰陣講清楚"期望行為、實際行為、復現步驟"）。完成之後用它記一星期賬——自己整嘅 App 攞嚟用，成就感會推住你繼續向前行。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 需求五要素 → 拆成"每步都用得"嘅小步驟，再動手
- 數據層：@Model 模型 + modelContainer 容器 + FetchDescriptor 查詢
- MVVM 分工：View 淨係管畫，@Observable 嘅 ViewModel 管邏輯，SwiftData 管存儲
- 界面：List + Section + toolbar + sheet 錄入彈窗
- 三層驗收（功能／邊界／架構）+ 進階挑戰（Swift Charts、iCloud 同步）
:::
