---
id: di-wu-shi-si-zhang
num: 54
part: an-zhuo-kai-fa-pian
nav: 第五十四章：项目一——我的记账本（本地版）
toc: default
kind: chapter
---

### 第五十四章：项目一——我的记账本（本地版）

{class="chapter-intro mb-4"}
欢迎来到你的第一个"正经项目"。这个记账本虽然不联网，但五脏俱全：能记一笔账、能看流水、能按月统计、能删改。做完它，你就完整走了一遍"数据 → 逻辑 → 界面"的全流程。别急着抄代码——<strong>先想清楚再动手</strong>，这是咱们一贯的原则。

#### 一、需求思考：先问五个问题

动手之前，用"需求五要素"把想法捋清楚：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要素</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">答案</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who（给谁用）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自己用，家人朋友也行</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What（做什么）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">记收支、看流水、按月汇总、按分类统计</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why（为什么）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">练手 + 搞清楚钱花哪儿了</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How（怎么做）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin + Compose + Room + MVVM，纯本地无后端</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint（约束）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一周内完成；最低支持 Android 8；不上架也先按上架标准写</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
记账本需求五要素

然后拆解成"每一步都能用"的小步骤：① 建 Room 数据层（能存一笔账）；② 列表页（能看流水）；③ 录入页（能加账）；④ 删除与编辑；⑤ 月度汇总卡片。每完成一步，App 都是一个"能用的东西"。

#### 二、数据层：让"账"有个家

先定义一笔账长什么样——字段要够用但别贪多：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Record.kt（实体）</span><span class="dots">···</span>
:::

```
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val type: String,        // "income" 收入 | "expense" 支出
    val amount: Double,      // 金额（元）
    val category: String,    // 分类：餐饮、交通、工资……
    val note: String = "",   // 备注（可选）
    val date: String         // "2026-08-15"
)
```
:::

Dao 里加两条"统计用"的查询——这是记账本的灵魂：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordDao.kt（统计查询）</span><span class="dots">···</span>
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
    suspend fun monthIncome(month: String): Double   // month 形如 "2026-08"

    @Query("SELECT COALESCE(SUM(amount),0) FROM records WHERE type='expense' AND date LIKE :month || '%'")
    suspend fun monthExpense(month: String): Double
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：金额为什么用 Double？

{class="mt-1"}
严谨的金融 App 会用 BigDecimal 或"以分为单位的 Int"来避免浮点误差（0.1+0.2≠0.3 的老问题）。练手项目用 Double 足够；如果哪天做真金融产品，记得换成"分"为单位——这是无数前辈踩出来的坑。
:::

#### 三、MVVM：界面与逻辑"分家"

直接让界面操作数据库？能跑，但界面代码会又臭又长。MVVM 架构让各司其职：<strong>View（界面）只管画，ViewModel（逻辑中枢）管数据，Model（Room）管存储</strong>。

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View（Compose 界面）</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel（状态与逻辑）</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model（Room 数据层）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
图 5：MVVM 三层结构——数据单向流动，各层互不越界
:::

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordViewModel.kt（骨架）</span><span class="dots">···</span>
:::

```
class RecordViewModel(private val dao: RecordDao) : ViewModel() {

    // 把 Flow 转成界面能观察的状态
    val records = dao.getAll()
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(), emptyList())

    // 用户操作：调用 suspend 函数
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

界面（Compose）里这样用：<code class="inline">val vm: RecordViewModel = viewModel()</code>，然后 <code class="inline">val list by vm.records.collectAsState()</code>——数据一变，列表自动刷新，你什么都不用做。这就是 MVVM + Flow + Compose 三剑合璧的威力。

#### 四、界面：列表页 + 录入页

列表页用 <strong>LazyColumn</strong>（懒加载列表）——数据再多也不卡：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 记账列表页（核心片段）</span><span class="dots">···</span>
:::

```
@Composable
fun RecordListScreen(vm: RecordViewModel) {
    val records by vm.records.collectAsState()

    Column {
        // 顶部汇总卡片（收入-支出=结余）
        SummaryCard(records)

        // 流水列表
        LazyColumn {
            items(records, key = { it.id }) { record -&gt;
                RecordRow(record) { vm.deleteRecord(record) }
            }
        }

        // 悬浮"记一笔"按钮 → 弹录入对话框
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

录入用 <strong>AlertDialog</strong>（对话框）最省事：几个输入框 + 收入/支出切换 + 分类下拉，点确定就调 <code class="inline">vm.addRecord(...)</code>。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>注意：输入校验别偷懒

{class="mt-1"}
金额输入框一定要校验：空值、负数、"abc"这类非法输入都要拦住（用 <code class="inline">toDoubleOrNull()</code> 判断）。App 崩掉最常见的原因之一就是"把用户的输入当成了乖孩子"。记住：<strong>用户输入的一切，都要当敌人审查</strong>。
:::

#### 五、编辑与删除：让数据"能进能出"

只会加不会删的记账本，用三天就废了。补两个操作：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 删除与编辑</span><span class="dots">···</span>
:::

```
// Dao 里补两条：
@Query("UPDATE records SET amount=:amount, category=:category, note=:note WHERE id=:id")
suspend fun update(id: Long, amount: Double, category: String, note: String)

@Query("DELETE FROM records WHERE id=:id")
suspend fun deleteById(id: Long)

// 界面上：长按列表项弹"编辑/删除"菜单（Compose 用 DropdownMenu 或 AlertDialog）
// 删除前最好弹确认框——"误删"是记账类 App 用户最痛恨的事
```
:::

交互细节两条经验：<strong>删除必须二次确认</strong>（防止手滑），编辑尽量<strong>预填原值</strong>（改一个字比重新输入省事）。别小看这两个细节——产品感就是这些细节堆出来的。

#### 六、验收：三层检查 + 两个进阶挑战

项目做完，按"功能 → 边界 → 架构"三层验收：能不能记、能不能删、重开 App 数据还在不在（功能）；金额输 0 或负数会不会崩、转屏会不会丢数据（边界）；界面和数据有没有混在一起、字段有没有硬编码（架构）。

基础版验收通过后，给自己加两道"进阶菜"：

1. <strong>月度筛选</strong>：顶部加月份切换（比如 2026-08 ▾），列表只显示当月流水；
2. <strong>分类饼图</strong>：用 Compose 的 Canvas 或引入轻量图表库，把"钱花哪儿了"画成饼图——做完这个，记账本就有点"产品样"了。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：本周完成它

{class="mt-1"}
按"数据层 → ViewModel → 列表页 → 录入页 → 汇总卡片"的顺序动手，每天一步。卡住了就把报错原样丢给搜索引擎或 AI（还记得第七篇《AI编程实战篇》吗？描述问题时说清"期望行为、实际行为、复现步骤"）。完成后用它记一周账——自己做的 App 用起来，成就感会推着你继续往前走。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 需求五要素 → 拆成"每步能用"的小步骤，再动手
- 数据层：Record 实体 + Dao（含月份统计 SQL）+ Database
- MVVM 分工：View 只管画，ViewModel 管逻辑，Model 管存储
- Flow + stateIn + collectAsState：数据一变界面自动刷新
- LazyColumn 懒加载列表；AlertDialog 做录入
- 三层验收（功能/边界/架构）+ 进阶挑战（月度筛选、分类饼图）
:::
