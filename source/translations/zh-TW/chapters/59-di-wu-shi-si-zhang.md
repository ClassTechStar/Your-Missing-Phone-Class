---
id: di-wu-shi-si-zhang
num: 54
part: an-zhuo-kai-fa-pian
nav: 第五十四章：專案一——我的記帳本（本地版）
toc: default
kind: chapter
---

### 第五十四章：專案一——我的記帳本（本地版）

{class="chapter-intro mb-4"}
歡迎來到你的第一個"正經專案"。這個記帳本雖然不聯網，但五臟俱全：能記一筆賬、能看流水、能按月統計、能刪改。做完它，你就完整走了一遍"資料 → 邏輯 → 介面"的全流程。別急著抄程式碼——先想清楚再動手，這是咱們一貫的原則。

#### 一、需求思考：先問五個問題

動手之前，用"需求五要素"把想法捋清楚：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要素</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">答案</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who（給誰用）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自己用，家人朋友也行</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What（做什麼）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">記收支、看流水、按月彙總、按分類統計</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why（為什麼）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">練手 + 搞清楚錢花哪兒了</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How（怎麼做）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin + Compose + Room + MVVM，純本地無後端</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint（約束）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一週內完成；最低支援 Android 8；不上架也先按上架標準寫</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
記帳本需求五要素

然後拆解成"每一步都能用"的小步驟：① 建 Room 資料層（能存一筆賬）；② 列表頁（能看流水）；③ 錄入頁（能加賬）；④ 刪除與編輯；⑤ 月度彙總卡片。每完成一步，App 都是一個"能用的東西"。

#### 二、資料層：讓"賬"有個家

先定義一筆賬長什麼樣——欄位要夠用但別貪多：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Record.kt（實體）</span><span class="dots">···</span>
:::

```
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val type: String,        // "income" 收入 | "expense" 支出
    val amount: Double,      // 金額（元）
    val category: String,    // 分類：餐飲、交通、工資……
    val note: String = "",   // 備註（可選）
    val date: String         // "2026-08-15"
)
```
:::

Dao 里加兩條"統計用"的查詢——這是記帳本的靈魂：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordDao.kt（統計查詢）</span><span class="dots">···</span>
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
小貼士：金額為什麼用 Double？

{class="mt-1"}
嚴謹的金融 App 會用 BigDecimal 或"以分為單位的 Int"來避免浮點誤差（0.1+0.2≠0.3 的老問題）。練手專案用 Double 足夠；如果哪天做真金融產品，記得換成"分"為單位——這是無數前輩踩出來的坑。
:::

#### 三、MVVM：介面與邏輯"分家"

直接讓介面運算元據庫？能跑，但介面程式碼會又臭又長。MVVM 架構讓各司其職：View（介面）只管畫，ViewModel（邏輯中樞）管資料，Model（Room）管儲存。

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View（Compose 介面）</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel（狀態與邏輯）</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model（Room 資料層）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 5：MVVM 三層結構——資料單向流動，各層互不越界
:::

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordViewModel.kt（骨架）</span><span class="dots">···</span>
:::

```
class RecordViewModel(private val dao: RecordDao) : ViewModel() {

    // 把 Flow 轉成介面能觀察的狀態
    val records = dao.getAll()
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(), emptyList())

    // 使用者操作：呼叫 suspend 函式
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

介面（Compose）裡這樣用：val vm: RecordViewModel = viewModel()，然後 val list by vm.records.collectAsState()——資料一變，列表自動重新整理，你什麼都不用做。這就是 MVVM + Flow + Compose 三劍合璧的威力。

#### 四、介面：列表頁 + 錄入頁

列表頁用 LazyColumn（懶載入列表）——資料再多也不卡：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 記帳列表頁（核心片段）</span><span class="dots">···</span>
:::

```
@Composable
fun RecordListScreen(vm: RecordViewModel) {
    val records by vm.records.collectAsState()

    Column {
        // 頂部彙總卡片（收入-支出=結餘）
        SummaryCard(records)

        // 流水列表
        LazyColumn {
            items(records, key = { it.id }) { record -&gt;
                RecordRow(record) { vm.deleteRecord(record) }
            }
        }

        // 懸浮"記一筆"按鈕 → 彈錄入對話方塊
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

錄入用 AlertDialog（對話方塊）最省事：幾個輸入框 + 收入/支出切換 + 分類下拉，點確定就調 vm.addRecord(...)。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：輸入校驗別偷懶

{class="mt-1"}
金額輸入框一定要校驗：空值、負數、"abc"這類非法輸入都要攔住（用 toDoubleOrNull() 判斷）。App 崩掉最常見的原因之一就是"把使用者的輸入當成了乖孩子"。記住：使用者輸入的一切，都要當敵人審查。
:::

#### 五、編輯與刪除：讓資料"能進能出"

只會加不會刪的記帳本，用三天就廢了。補兩個操作：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 刪除與編輯</span><span class="dots">···</span>
:::

```
// Dao 裡補兩條：
@Query("UPDATE records SET amount=:amount, category=:category, note=:note WHERE id=:id")
suspend fun update(id: Long, amount: Double, category: String, note: String)

@Query("DELETE FROM records WHERE id=:id")
suspend fun deleteById(id: Long)

// 介面上：長按列表項彈"編輯/刪除"選單（Compose 用 DropdownMenu 或 AlertDialog）
// 刪除前最好彈確認框——"誤刪"是記帳類 App 使用者最痛恨的事
```
:::

互動細節兩條經驗：刪除必須二次確認（防止手滑），編輯儘量預填原值（改一個字比重新輸入省事）。別小看這兩個細節——產品感就是這些細節堆出來的。

#### 六、驗收：三層檢查 + 兩個進階挑戰

專案做完，按"功能 → 邊界 → 架構"三層驗收：能不能記、能不能刪、重開 App 資料還在不在（功能）；金額輸 0 或負數會不會崩、轉屏會不會丟資料（邊界）；介面和資料有沒有混在一起、欄位有沒有硬編碼（架構）。

基礎版驗收透過後，給自己加兩道"進階菜"：

1. 月度篩選：頂部加月份切換（比如 2026-08 ▾），列表只顯示當月流水；
2. 分類餅圖：用 Compose 的 Canvas 或引入輕量圖表庫，把"錢花哪兒了"畫成餅圖——做完這個，記帳本就有點"產品樣"了。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：本週完成它

{class="mt-1"}
按"資料層 → ViewModel → 列表頁 → 錄入頁 → 彙總卡片"的順序動手，每天一步。卡住了就把報錯原樣丟給搜尋引擎或 AI（還記得第七篇《AI程式設計實戰篇》嗎？描述問題時說清"期望行為、實際行為、復現步驟"）。完成後用它記一週賬——自己做的 App 用起來，成就感會推著你繼續往前走。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 需求五要素 → 拆成"每步能用"的小步驟，再動手
- 資料層：Record 實體 + Dao（含月份統計 SQL）+ Database
- MVVM 分工：View 只管畫，ViewModel 管邏輯，Model 管儲存
- Flow + stateIn + collectAsState：資料一變介面自動重新整理
- LazyColumn 懶載入列表；AlertDialog 做錄入
- 三層驗收（功能/邊界/架構）+ 進階挑戰（月度篩選、分類餅圖）
:::
