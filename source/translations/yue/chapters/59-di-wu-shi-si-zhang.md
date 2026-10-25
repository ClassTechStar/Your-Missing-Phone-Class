---
id: di-wu-shi-si-zhang
num: 54
part: an-zhuo-kai-fa-pian
nav: 第五十四章：項目一——我嘅記賬本（本地版）
toc: default
kind: chapter
---

### 第五十四章：項目一——我嘅記賬本（本地版）

{class="chapter-intro mb-4"}
歡迎嚟到你第一個「正式項目」。呢個記賬本雖然唔上網，但五臟俱全：記到一筆賬、睇到流水、按月統計到、又刪改到。做完佢，你就完整行咗一次「資料 → 邏輯 → 介面」嘅全流程。唔好心急抄程式碼——先諗清楚先至郁手，呢個係我哋一貫嘅原則。

#### 一、需求思考：先問五條問題

郁手之前，用「需求五要素」將個諗法捋清楚：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要素</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">答案</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who（畀邊個用）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自己用，屋企人朋友都得</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What（做乜嘢）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">記收支、睇流水、按月匯總、按分類統計</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why（點解）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">練手 + 搞清楚啲錢使咗去邊</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How（點樣做）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin + Compose + Room + MVVM，純本地冇後端</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint（約束）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一個禮拜之內完成；最低支援 Android 8；唔上架都先按上架標準寫</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
記賬本需求五要素

跟住拆解成「每一步都用得」嘅小步驟：① 建 Room 資料層（儲到一筆賬）；② 列表頁（睇到流水）；③ 錄入頁（加到賬）；④ 刪除同編輯；⑤ 月度匯總卡。每完成一步，App 都係一樣「用得嘅嘢」。

#### 二、資料層：畀「賬」有個屋企

先定義一筆賬係咩樣——欄位要夠用但唔好貪多：

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
    val category: String,    // 分類：餐飲、交通、人工……
    val note: String = "",   // 備註（可選）
    val date: String         // "2026-08-15"
)
```
:::

Dao 入面加兩條「統計用」嘅查詢——呢個係記賬本嘅靈魂：

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
小貼士：金額點解用 Double？

{class="mt-1"}
嚴謹嘅金融 App 會用 BigDecimal 或者「以『分』為單位嘅 Int」嚟避免浮點誤差（0.1+0.2≠0.3 呢個老問題）。練手項目用 Double 就夠；如果第日做真金融產品，記得轉做用「分」做單位——呢個係無數前輩踩出嚟嘅坑。
:::

#### 三、MVVM：介面同邏輯「分家」

直接畀介面去操作資料庫？行到，但介面程式碼會又長又臭。MVVM 架構令大家各司其職：View（介面）淨係負責畫，ViewModel（邏輯中樞）管資料，Model（Room）管儲存。

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View（Compose 界面）</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel（狀態與邏輯）</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model（Room 數據層）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 5：MVVM 三層結構——資料單向流動，各層互唔過界
:::

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordViewModel.kt（骨架）</span><span class="dots">···</span>
:::

```
class RecordViewModel(private val dao: RecordDao) : ViewModel() {

    // 將 Flow 轉成界面觀察到嘅狀態
    val records = dao.getAll()
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(), emptyList())

    // 用戶操作：調用 suspend 函數
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

介面（Compose）入面咁樣用：val vm: RecordViewModel = viewModel()，跟住 val list by vm.records.collectAsState()——資料一變，列表自動刷新，你乜都唔使做。呢個就係 MVVM + Flow + Compose 三劍合璧嘅威力。

#### 四、介面：列表頁 + 錄入頁

列表頁用 LazyColumn（懶載入列表）——資料幾多都唔卡：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 記賬列表頁（核心片段）</span><span class="dots">···</span>
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

        // 懸浮"記一筆"按鈕 → 彈錄入對話框
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

錄入用 AlertDialog（對話框）最慳事：幾個輸入框 + 收入／支出切換 + 分類下拉，撳確定就調 vm.addRecord(...)。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：輸入校驗唔好偷懶

{class="mt-1"}
金額輸入框一定要校驗：空值、負數、「abc」呢類非法輸入全部要欄住（用 toDoubleOrNull() 判斷）。App 冧咗最常見嘅原因之一就係「將用戶嘅輸入當咗係乖仔」。記住：用戶輸入嘅所有嘢，都要當敵人咁審查。
:::

#### 五、編輯同刪除：畀資料「入得到又出得到」

淨係識加唔識刪嘅記賬本，用三日就報廢。補返兩個操作：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 刪除與編輯</span><span class="dots">···</span>
:::

```
// Dao 入面補兩條：
@Query("UPDATE records SET amount=:amount, category=:category, note=:note WHERE id=:id")
suspend fun update(id: Long, amount: Double, category: String, note: String)

@Query("DELETE FROM records WHERE id=:id")
suspend fun deleteById(id: Long)

// 界面上：長㩒列表項彈"編輯／刪除"菜單（Compose 用 DropdownMenu 或 AlertDialog）
// 刪除之前最好彈確認框——"刪錯嘢"係記賬類 App 用戶最憎嘅事
```
:::

互動細節兩條經驗：刪除必須二次確認（防止手快快），編輯盡量預填返原本個值（改一個字比起重新輸入慳事）。唔好睇小呢兩個細節——產品感就係呢啲細節堆出嚟嘅。

#### 六、驗收：三層檢查 + 兩個進階挑戰

項目做完，按「功能 → 邊界 → 架構」三層驗收：記唔記到、刪唔刪到、重開 App 資料仲喺唔喺度（功能）；金額輸 0 或者負數會唔會冧、轉屏會唔會冇咗資料（邊界）；介面同資料有冇撈埋一齊、欄位有冇寫死（架構）。

基礎版驗收過關之後，畀自己加兩味「進階菜」：

1. 月度篩選：頂部加月份切換（例如 2026-08 ▾），列表淨係顯示當月流水；
2. 分類圓餅圖：用 Compose 嘅 Canvas 或者引入輕量圖表庫，將「錢使咗去邊」畫成圓餅圖——做完呢樣嘢，記賬本就有啲「產品樣」喇。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
嚟動手：今個禮拜搞掂佢

{class="mt-1"}
按「資料層 → ViewModel → 列表頁 → 錄入頁 → 匯總卡」嘅次序郁手，每日一步。卡咗就將報錯原封不動丟畀搜尋引擎或者 AI（仲記唔記得第七篇《AI編程實戰篇》？描述問題嗰陣講清楚「期望行為、實際行為、重現步驟」）。完成之後用它記一個禮拜賬——自己整嘅 App 用起上嚟，成就感會推住你繼續向前行。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 需求五要素 → 拆成「每步用得」嘅小步驟，先至郁手
- 資料層：Record 實體 + Dao（包埋月份統計 SQL）+ Database
- MVVM 分工：View 淨係負責畫，ViewModel 管邏輯，Model 管儲存
- Flow + stateIn + collectAsState：資料一變介面自動刷新
- LazyColumn 懶載入列表；AlertDialog 做錄入
- 三層驗收（功能／邊界／架構）+ 進階挑戰（月度篩選、分類圓餅圖）
:::
