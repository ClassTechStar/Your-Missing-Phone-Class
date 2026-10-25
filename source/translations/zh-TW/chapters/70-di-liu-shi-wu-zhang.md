---
id: di-liu-shi-wu-zhang
num: 65
part: ios-kai-fa-pian
nav: 第六十五章：專案一——我的記帳本（本地版）
toc: default
kind: chapter
---

### 第六十五章：專案一——我的記帳本（本地版）

{class="chapter-intro mb-4"}
歡迎來到你的第一個"正經專案"。這個記帳本雖然不聯網，但五臟俱全：能記一筆賬、能看流水、能按月統計、能刪改。做完它，你就完整走了一遍"資料 → 邏輯 → 介面"的全流程。別急著抄程式碼——先想清楚再動手，這是咱們一貫的原則。

#### 一、需求思考：先問五個問題

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要素</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">答案</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who（給誰用）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自己用，家人朋友也行</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What（做什麼）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">記收支、看流水、按月彙總、按分類統計</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why（為什麼）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">練手 + 搞清楚錢花哪兒了</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How（怎麼做）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift + SwiftUI + SwiftData + MVVM，純本地無後端</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint（約束）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一週內完成；最低支援 iOS 17（SwiftData 門檻）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
記帳本需求五要素

然後拆解成"每一步都能用"的小步驟：① 建 SwiftData 資料層（能存一筆賬）；② 列表頁（能看流水）；③ 錄入跳出視窗（能加賬）；④ 刪除與編輯；⑤ 月度彙總卡片。每完成一步，App 都是一個"能用的東西"。

#### 二、資料層：讓"賬"有個家

先定義一筆賬長什麼樣——欄位要夠用但別貪多：

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
    var category: String  // 分類：餐飲、交通、工資……
    var note: String      // 備註（可選）
    var date: Date        // 記帳日期

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
小貼士：金額為什麼用 Double？

{class="mt-1"}
嚴謹的金融 App 會用 Decimal（精確十進位制）來避免浮點誤差（0.1+0.2≠0.3 的老問題）。練手專案用 Double 足夠；如果哪天做真金融產品，記得換成 Decimal 或"以分為單位的 Int"——這是無數前輩踩出來的坑。
:::

#### 三、MVVM：介面與邏輯"分家"

直接讓介面運算元據庫？能跑，但介面程式碼會又臭又長。MVVM 架構讓各司其職：View（介面）只管畫，ViewModel（邏輯中樞）管資料，Model（SwiftData）管儲存。

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View（SwiftUI 介面）</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel（@Observable 邏輯中樞）</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model（SwiftData 資料層）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 4：MVVM 三層結構——資料單向流動，各層互不越界
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
        // SwiftData 的 #Predicate 篩選 + 排序
        let descriptor = FetchDescriptor<Record>(
            sortBy: [SortDescriptor(\.date, order: .reverse)]
        )
        records = (try? context.fetch(descriptor)) ?? []
    }

    func add(type: String, amount: Double, category: String, note: String) {
        let r = Record(type: type, amount: amount, category: category, note: note)
        context.insert(r)
        try? context.save()
        load()                       // 重新載入，介面重新整理
    }

    func delete(_ record: Record) {
        context.delete(record)
        try? context.save()
        load()
    }
}
```
:::

介面裡 @State private var vm = RecordViewModel(...)，然後直接 vm.records 渲染列表——資料一變，介面自動重新整理。

#### 四、介面：列表頁 + 錄入跳出視窗

::: div .code-block
:::inline div .code-head
<span>SWIFT · 記帳列表頁（核心片段）</span><span class="dots">···</span>
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
            .navigationTitle("我的記帳本")
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

錄入跳出視窗要點：金額輸入框鍵盤用 .keyboardType(.decimalPad)（數字鍵盤），收入/支出用分段控制元件（Picker），分類用選單選擇，點"儲存"調 vm.add(...) 並 dismiss() 關窗。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：輸入校驗別偷懶

{class="mt-1"}
金額輸入框一定要校驗：空值、負數、"abc"這類非法輸入都要攔住（用 Double(text) 判斷，失敗返回 nil）。App 崩掉最常見的原因之一就是"把使用者的輸入當成了乖孩子"。記住：使用者輸入的一切，都要當敵人審查。
:::

#### 五、編輯、刪除與彙總

- 刪除：List 的 .onDelete 左滑刪除 + 確認跳出視窗（誤刪是記帳類 App 使用者最痛恨的事）；
- 編輯：點行進編輯跳出視窗，預填原值（改一個字比重新輸入省事）；
- 彙總：用 filter + reduce 算"本月收入 / 支出 / 結餘"，頂部卡片展示：

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

專案做完，按"功能 → 邊界 → 架構"三層驗收：能不能記、能不能刪、重啟 App 資料還在不在（功能）；金額輸 0 或負數會不會崩（邊界）；介面和資料有沒有混在一起、欄位有沒有硬編碼（架構）。

基礎版驗收透過後，給自己加兩道"進階菜"：

1. 分類統計：加一個"統計"標籤頁，用 Swift Charts 把分類支出畫成餅圖/柱狀圖——蘋果官方圖表庫，幾行程式碼出圖；
2. iCloud 同步：SwiftData 開 iCloud 同步只需配幾項設定——帳本在 iPhone/iPad 之間自動同步，瞬間"進階"起來。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：本週完成它

{class="mt-1"}
按"資料層 → ViewModel → 列表頁 → 錄入跳出視窗 → 彙總卡片"的順序動手，每天一步。卡住了就把報錯原樣丟給搜尋引擎或 AI（還記得第七篇《AI程式設計實戰篇》嗎？描述問題時說清"期望行為、實際行為、復現步驟"）。完成後用它記一週賬——自己做的 App 用起來，成就感會推著你繼續往前走。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 需求五要素 → 拆成"每步能用"的小步驟，再動手
- 資料層：@Model 模型 + modelContainer 容器 + FetchDescriptor 查詢
- MVVM 分工：View 只管畫，@Observable 的 ViewModel 管邏輯，SwiftData 管儲存
- 介面：List + Section + toolbar + sheet 錄入跳出視窗
- 三層驗收（功能/邊界/架構）+ 進階挑戰（Swift Charts、iCloud 同步）
:::
