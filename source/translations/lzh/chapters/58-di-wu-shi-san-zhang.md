---
id: di-wu-shi-san-zhang
num: 53
part: an-zhuo-kai-fa-pian
nav: 第五十三章：數據存儲與網絡請求
toc: default
kind: chapter
---

### 第五十三章：數據之儲與網絡之請

{class="chapter-intro mb-4"}
App 之僅可「觀」者，死物也；能儲數據、能連網絡者，方為活物。此章識安卓數據層之「三件」：DataStore（儲小配置）、Room（儲結構之數據）、Retrofit（與服務器言），外益其「總調度」——協程。此章既學，汝遂能書真 App 矣，能記用戶之習、能實時更新其內容者也。

#### 一、儲存之方何擇：先觀此表

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">方案</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">宜儲何物</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">特點</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">本書何處用之</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DataStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">零散配置（主題、開關）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">鍵值之對，簡而安</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第五十四章記賬冊之設置</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">結構之數據（賬目、用戶）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真 SQLite 數據庫之封裝，可查詢</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第五十四章賬目之記錄</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">（不儲，聯網而取）服務器之數據</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">HTTP 請求庫之事實標準</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第五十五章天氣之數據</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
數據三件之分工

記一口訣：「小配置入 DataStore，成批之數據入 Room，外之數據行 Retrofit」。舊教程所常見之 SharedPreferences，已為 DataStore 所代；SQLite 手書之 SQL，亦已為 Room 所代——逕學其新，毋蹈舊轍。

#### 二、DataStore：儲少許小配置

欲記「用戶前所擇之幣種」「深色模式啟否」此類零散之值，用 DataStore（Preferences 之版）：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · DataStore 示例</span><span class="dots">···</span>
:::

```
val Context.dataStore by preferencesDataStore(name = "settings")

// 寫：存一個值
suspend fun saveTheme(isDark: Boolean) {
    context.dataStore.edit { prefs ->
        prefs[THEME_KEY] = isDark
    }
}

// 讀：取之（Flow 自告其變）
val themeFlow: Flow<Boolean> = context.dataStore.data
    .map { it[THEME_KEY] ?: false }
```
:::

慎之，所返者 Flow 也——能流之數據流也。值一變，凡觀之之處自受新值。此概念（響應式）乃現代安卓之基石，第五十四章將實戰焉。

#### 三、Room：為數據安「真家」

記賬之冊有賬成百上千，且欲依類、依月查而計之——此須數據庫也。Room 者，SQLite 官家之封裝，使「建表、查數據」如書 Kotlin 之自然。有三物焉：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Room 三件套：Entity / Dao / Database</span><span class="dots">···</span>
:::

```
// 1. Entity：表結構（一張表 = 一個 data class）
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val amount: Double,
    val category: String,
    val note: String,
    val date: String
)

// 2. Dao：操作接口（增刪改查）
@Dao
interface RecordDao {
    @Query("SELECT * FROM records ORDER BY date DESC")
    fun getAll(): Flow<List<Record>>

    @Insert
    suspend fun insert(record: Record)

    @Delete
    suspend fun delete(record: Record)

    @Query("SELECT SUM(amount) FROM records WHERE category = :c")
    suspend fun sumByCategory(c: String): Double
}

// 3. Database：總裝
@Database(entities = [Record::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun recordDao(): RecordDao
}
```
:::

此「三件」之模板可原樣搬入汝之任何項目——易其字段之名足矣。查詢所返者 Flow，界面隨數據自新，妙不可言也。

#### 四、Retrofit：與服務器言

天氣、新聞、匯率……此諸數據不在機中，在他人之服務器上。Retrofit 使「向服務器索數據」易如調函數。三步而行：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Retrofit 三步走</span><span class="dots">···</span>
:::

```
// 1. 定接口：狀 HTTP 之請如函數
interface WeatherApi {
    @GET("v1/weather")
    suspend fun getWeather(@Query("city") city: String): WeatherResponse
}

// 2. 建實例
val api = Retrofit.Builder()
    .baseUrl("https://api.example.com/")
    .addConverterFactory(GsonConverterFactory.create())
    .build()
    .create(WeatherApi::class.java)

// 3. 如調函數然（於協程中）
val result = api.getWeather("北京")
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
避坑之警：網絡鐵律二條

{class="mt-1"}
① 網絡之請決不可行於主線程——將卡死界面乃至崩潰（NetworkOnMainThreadException）。凡網絡之調必置於協程（viewModelScope.launch）之中。② 明文之 HTTP，默則被禁：自安卓 9 始須 HTTPS。測試之時若欲用 http:// 本地之址，須於 Manifest 顯聲 usesCleartextTraffic——然正式之品必全行 HTTPS。
:::

#### 五、JSON 之析：為網絡數據作「譯」

服務器所返之數據多為 JSON——一串如「嵌套字典」之文。Retrofit 須一「譯官」化之為 Kotlin 對象。2026 年兩大主流之方：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">方案</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">特點</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">所薦之境</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gson / Moshi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">老牌反射之方，配置無費</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">速於起步、字段無多之小項目</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">kotlinx.serialization</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官家編譯期之方，愈速愈安</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新項目之首選（2026 年主流）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
JSON 析之兩大方

::: div .code-block
:::inline div .code-head
<span>KOTLIN · kotlinx.serialization 示例</span><span class="dots">···</span>
:::

```
// 予數據類加 @Serializable 註解
@Serializable
data class WeatherResponse(
    val weather: List<Weather>,
    val main: Main,
    val name: String
)

// Retrofit 掛對應之 Converter（以 Retrofit 2.11+ 官方支持為例）：
// .addConverterFactory(json.asConverterFactory("application/json".toMediaType()))
```
:::

無論何方，鐵律皆曰：先觀真返之 JSON，後定字段。多「析之敗」之 bug，皆因字段名書誤、嵌套之層猜誤——印原 JSON 而對之，十秒可定。

#### 六、協程：安卓並發之「通語」

上文屢現之 suspend 與 launch，出於 Kotlin 協程（Coroutine）——安卓官家並發之方也。汝可粗而解之曰：使「須待片時」之操作（網絡、數據庫）不塞界面。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 協程初體驗</span><span class="dots">···</span>
:::

```
// 於 ViewModel 中啟協程
viewModelScope.launch {
    val records = dao.getAll().first()  // suspend：自掛起而待
    // 更新界面狀態……
}

// 關鍵詞速記：
// suspend   —— "吾欲待，毋阻他人"
// launch    —— "開工！"
// viewModelScope —— 隨頁面之"工坊"，頁毀則自收工
```
:::

零基者但記其用法可也，其後「掛起與復還」之理可後而深究之。日常開發，汝所書者百分之九十皆此模板也。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：作「每日一句」之小應用

{class="mt-1"}
覓一免費名言之 API（譬如 hitokoto 之屬），以 Retrofit 拉「每日一句」，顯於屏之中央，加「易一句」之鈕（協程中復請之）。復以 Room 存所喜之句於「收藏之夾」。此一習，DataStore/Room/Retrofit/協程盡嘗用之——既成之，則第七、八章如小菜一碟矣。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 口訣：小配置入 DataStore，成批數據入 Room，外之數據行 Retrofit
- DataStore 返 Flow：值一變，觀者自受
- Room 三件：@Entity（表）+ @Dao（操作）+ @Database（總裝），模板可逕復用
- Retrofit 三步：定接口 → 創實例 → 協程中調之
- 鐵律二條：網絡不入主線程；正式之品必 HTTPS
- 協程 = 不塞界面之待；viewModelScope 者，頁面專屬之作坊也
:::
