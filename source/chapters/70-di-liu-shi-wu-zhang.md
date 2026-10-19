---
id: di-liu-shi-wu-zhang
num: 65
part: ios-kai-fa-pian
nav: 第六十五章：项目一——我的记账本（本地版）
toc: default
kind: chapter
---

### 第六十五章：项目一——我的记账本（本地版）

{class="chapter-intro mb-4"}
欢迎来到你的第一个"正经项目"。这个记账本虽然不联网，但五脏俱全：能记一笔账、能看流水、能按月统计、能删改。做完它，你就完整走了一遍"数据 → 逻辑 → 界面"的全流程。别急着抄代码——<strong>先想清楚再动手</strong>，这是咱们一贯的原则。

#### 一、需求思考：先问五个问题

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要素</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">答案</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who（给谁用）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自己用，家人朋友也行</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What（做什么）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">记收支、看流水、按月汇总、按分类统计</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why（为什么）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">练手 + 搞清楚钱花哪儿了</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How（怎么做）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift + SwiftUI + SwiftData + MVVM，纯本地无后端</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint（约束）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一周内完成；最低支持 iOS 17（SwiftData 门槛）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
记账本需求五要素

然后拆解成"每一步都能用"的小步骤：① 建 SwiftData 数据层（能存一笔账）；② 列表页（能看流水）；③ 录入弹窗（能加账）；④ 删除与编辑；⑤ 月度汇总卡片。每完成一步，App 都是一个"能用的东西"。

#### 二、数据层：让"账"有个家

先定义一笔账长什么样——字段要够用但别贪多：

::: div .code-block
:::inline div .code-head
<span>SWIFT · Record.swift（模型）</span><span class="dots">···</span>
:::

```
import SwiftData

@Model
class Record {
    var type: String      // "income" 收入 | "expense" 支出
    var amount: Double    // 金额（元）
    var category: String  // 分类：餐饮、交通、工资……
    var note: String      // 备注（可选）
    var date: Date        // 记账日期

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
<i class="fas fa-lightbulb mr-2"></i>小贴士：金额为什么用 Double？

{class="mt-1"}
严谨的金融 App 会用 Decimal（精确十进制）来避免浮点误差（0.1+0.2≠0.3 的老问题）。练手项目用 Double 足够；如果哪天做真金融产品，记得换成 <code class="inline">Decimal</code> 或"以分为单位的 Int"——这是无数前辈踩出来的坑。
:::

#### 三、MVVM：界面与逻辑"分家"

直接让界面操作数据库？能跑，但界面代码会又臭又长。MVVM 架构让各司其职：<strong>View（界面）只管画，ViewModel（逻辑中枢）管数据，Model（SwiftData）管存储</strong>。

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View（SwiftUI 界面）</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel（@Observable 逻辑中枢）</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model（SwiftData 数据层）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
图 4：MVVM 三层结构——数据单向流动，各层互不越界
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
        // SwiftData 的 #Predicate 筛选 + 排序
        let descriptor = FetchDescriptor<Record>(
            sortBy: [SortDescriptor(\.date, order: .reverse)]
        )
        records = (try? context.fetch(descriptor)) ?? []
    }

    func add(type: String, amount: Double, category: String, note: String) {
        let r = Record(type: type, amount: amount, category: category, note: note)
        context.insert(r)
        try? context.save()
        load()                       // 重新加载，界面刷新
    }

    func delete(_ record: Record) {
        context.delete(record)
        try? context.save()
        load()
    }
}
```
:::

界面里 <code class="inline">@State private var vm = RecordViewModel(...)</code>，然后直接 <code class="inline">vm.records</code> 渲染列表——数据一变，界面自动刷新。

#### 四、界面：列表页 + 录入弹窗

::: div .code-block
:::inline div .code-head
<span>SWIFT · 记账列表页（核心片段）</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var vm: RecordViewModel
    @State private var showAdd = false

    var body: some View {
        NavigationStack {
            List {
                Section("本月结余") {          // 汇总卡片
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
            .navigationTitle("我的记账本")
            .toolbar {
                Button { showAdd = true } label: {
                    Image(systemName: "plus")
                }
            }
            .sheet(isPresented: $showAdd) {
                AddRecordView(vm: vm)          // 录入弹窗
            }
        }
    }
}
```
:::

录入弹窗要点：金额输入框键盘用 <code class="inline">.keyboardType(.decimalPad)</code>（数字键盘），收入/支出用分段控件（Picker），分类用菜单选择，点"保存"调 <code class="inline">vm.add(...)</code> 并 <code class="inline">dismiss()</code> 关窗。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>注意：输入校验别偷懒

{class="mt-1"}
金额输入框一定要校验：空值、负数、"abc"这类非法输入都要拦住（用 <code class="inline">Double(text)</code> 判断，失败返回 nil）。App 崩掉最常见的原因之一就是"把用户的输入当成了乖孩子"。记住：<strong>用户输入的一切，都要当敌人审查</strong>。
:::

#### 五、编辑、删除与汇总

- <strong>删除</strong>：List 的 .onDelete 左滑删除 + 确认弹窗（误删是记账类 App 用户最痛恨的事）；
- <strong>编辑</strong>：点行进编辑弹窗，预填原值（改一个字比重新输入省事）；
- <strong>汇总</strong>：用 <code class="inline">filter</code> + <code class="inline">reduce</code> 算"本月收入 / 支出 / 结余"，顶部卡片展示：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 月度汇总计算</span><span class="dots">···</span>
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

#### 六、验收：三层检查 + 两个进阶挑战

项目做完，按"功能 → 边界 → 架构"三层验收：能不能记、能不能删、重启 App 数据还在不在（功能）；金额输 0 或负数会不会崩（边界）；界面和数据有没有混在一起、字段有没有硬编码（架构）。

基础版验收通过后，给自己加两道"进阶菜"：

1. <strong>分类统计</strong>：加一个"统计"标签页，用 <strong>Swift Charts</strong> 把分类支出画成饼图/柱状图——苹果官方图表库，几行代码出图；
2. <strong>iCloud 同步</strong>：SwiftData 开 iCloud 同步只需配几项设置——账本在 iPhone/iPad 之间自动同步，瞬间"高级"起来。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：本周完成它

{class="mt-1"}
按"数据层 → ViewModel → 列表页 → 录入弹窗 → 汇总卡片"的顺序动手，每天一步。卡住了就把报错原样丢给搜索引擎或 AI（还记得第七篇《AI编程实战篇》吗？描述问题时说清"期望行为、实际行为、复现步骤"）。完成后用它记一周账——自己做的 App 用起来，成就感会推着你继续往前走。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 需求五要素 → 拆成"每步能用"的小步骤，再动手
- 数据层：@Model 模型 + modelContainer 容器 + FetchDescriptor 查询
- MVVM 分工：View 只管画，@Observable 的 ViewModel 管逻辑，SwiftData 管存储
- 界面：List + Section + toolbar + sheet 录入弹窗
- 三层验收（功能/边界/架构）+ 进阶挑战（Swift Charts、iCloud 同步）
:::
