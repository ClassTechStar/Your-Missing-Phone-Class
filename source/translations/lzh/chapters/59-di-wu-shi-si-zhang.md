---
id: di-wu-shi-si-zhang
num: 54
part: an-zhuo-kai-fa-pian
nav: 第五十四章：項目一——吾之記賬本（本地版）
toc: default
kind: chapter
---

### 第五十四章：項目一——吾之記賬冊（本地版）

{class="chapter-intro mb-4"}
喜迎汝首個「正經之項目」。此記賬冊雖不連網，然五臟俱全：能記一筆之賬、能觀流水、能依月而計、能刪能改。既成之，汝遂全歷「數據 → 邏輯 → 界面」之全程。勿遽抄代碼——先思之明而後動，此吾儕恆守之則也。

#### 一、需求之思：先問五問

動手之前，以「需求五要素」理其念使明：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要素</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">所答</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who（誰用之）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">己用之，家人朋友亦可</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What（為何事）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">記收支、觀流水、依月而彙、依類而計</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why（何以為之）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">練手 + 明錢費於何所</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How（以何術為之）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin + Compose + Room + MVVM，純本地無後端</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint（所限）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一週而成；最低支持 Android 8；雖不上架，亦先依上架之準而書</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
記賬冊需求五要素

繼而拆為「步步可用」之小節：① 建 Room 數據之層（能儲一賬）；② 列表之頁（能觀流水）；③ 錄入之頁（能加賬）；④ 刪與編；⑤ 月彙之卡。每竟一步，App 皆一「能用之物」也。

#### 二、數據之層：使「賬」有家

先定一賬之形——字段須足用而毋貪多：

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
    val category: String,    // 分類：餐飲、交通、薪俸……
    val note: String = "",   // 備註（可選）
    val date: String         // "2026-08-15"
)
```
:::

Dao 中加二「統計用」之查詢——此記賬冊之魂也：

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
小識：金額何以用 Double？

{class="mt-1"}
謹嚴之金融 App 當用 BigDecimal 或「以分為單位之 Int」以免浮點之差（0.1+0.2≠0.3 之舊題）。練手之項目用 Double 足矣；他日若作真金融之品，記易「分」為單位——此無數先輩踐而後知之坑也。
:::

#### 三、MVVM：界面與邏輯「分家」

逕使界面操作數據庫乎？能行，然界面之碼將冗長可憎。MVVM 之構使各司其職：View（界面）惟司畫，ViewModel（邏輯之樞）司數據，Model（Room）司儲。

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View（Compose 界面）</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel（狀態與邏輯）</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model（Room 數據層）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 5：MVVM 三層之構——數據單向而流，層層不相踰
:::

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordViewModel.kt（骨架）</span><span class="dots">···</span>
:::

```
class RecordViewModel(private val dao: RecordDao) : ViewModel() {

    // 將 Flow 化為界面可觀之狀態
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

界面（Compose）中如是用之：val vm: RecordViewModel = viewModel()，繼 val list by vm.records.collectAsState()——數據一變，列表自新，汝無所事。此 MVVM + Flow + Compose 三劍合璧之威也。

#### 四、界面：列表之頁 + 錄入之頁

列表之頁用 LazyColumn（懶載之列）——數據雖多不卡：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 記賬列表頁（核心片段）</span><span class="dots">···</span>
:::

```
@Composable
fun RecordListScreen(vm: RecordViewModel) {
    val records by vm.records.collectAsState()

    Column {
        // 頂部匯總卡片（收入-支出=結餘）
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

錄入用 AlertDialog（對話之框）至省事：數輸入框 + 收入/支出之切換 + 分類之下拉，點「確定」則調 vm.addRecord(...)。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
慎之：輸入之校驗勿惰

{class="mt-1"}
金額之輸入框必驗之：空值、負數、「abc」此類非法之入皆須攔之（以 toDoubleOrNull() 判之）。App 之崩，至常之因一即「以用戶之入為乖孺」。記之：凡用戶所入，皆當敵而審之。
:::

#### 五、編輯與刪除：使數據「能進能出」

惟加而莫刪之記賬冊，用之三日即廢。補二操作：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 刪除與編輯</span><span class="dots">···</span>
:::

```
// Dao 中補二條：
@Query("UPDATE records SET amount=:amount, category=:category, note=:note WHERE id=:id")
suspend fun update(id: Long, amount: Double, category: String, note: String)

@Query("DELETE FROM records WHERE id=:id")
suspend fun deleteById(id: Long)

// 界面上：長按列表項彈"編輯/刪除"之單（Compose 用 DropdownMenu 或 AlertDialog）
// 刪前宜彈確認之框——"誤刪"者記賬類 App 用戶之所最深恨也
```
:::

交互之細，經驗二條：刪必再確認之（防手之滑），編宜預填原值（易一字較重輸省事）。毋輕此二細——產品之感，即此諸細所堆成也。

#### 六、驗收：三層之檢 + 二進階之挑戰

項目既成，依「功能 → 邊界 → 架構」三層而驗：能記否、能刪否、重啟 App 數據尚在不（功能）；金額入 0 或負數崩否、轉屏失數否（邊界）；界面與數據有無相混、字段有無硬編（架構）。

基礎之版既過驗收，為己加二道「進階之菜」：

1. 月度之篩選：頂加月份之切換（譬如 2026-08 ▾），列表惟顯當月之流水；
2. 分類之餅圖：以 Compose 之 Canvas 或引入輕量圖表之庫，繪「錢費何處」為餅圖——既成此，記賬冊遂頗有「產品之樣」矣。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：本週竟之

{class="mt-1"}
依「數據層 → ViewModel → 列表頁 → 錄入頁 → 彙總卡片」之序而動手，日竟一步。困則以報錯原樣擲於搜索引擎或 AI（猶憶第七篇《AI編程實戰篇》乎？述問題時明言「期望之行、實際之行、復現之步」）。既成以之記賬一週——自作之 App 自用之，成就之感將推汝前行不輟。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 需求五要素 → 拆為「步步能用」之小節，而後動手
- 數據層：Record 實體 + Dao（含月度統計之 SQL）+ Database
- MVVM 之分：View 惟司畫，ViewModel 司邏輯，Model 司儲
- Flow + stateIn + collectAsState：數據一變界面自新
- LazyColumn 懶載之列；AlertDialog 以錄入
- 三層之驗（功能/邊界/架構）+ 進階之挑戰（月度之篩選、分類之餅圖）
:::
