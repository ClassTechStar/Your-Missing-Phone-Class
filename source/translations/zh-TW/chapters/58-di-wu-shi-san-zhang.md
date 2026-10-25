---
id: di-wu-shi-san-zhang
num: 53
part: an-zhuo-kai-fa-pian
nav: 第五十三章：資料儲存與網路請求
toc: default
kind: chapter
---

### 第五十三章：資料儲存與網路請求

{class="chapter-intro mb-4"}
一個只能"看"的 App 是死的；能存資料、能連網路的 App 才是活的。這一章認識安卓資料層的"三件套"：DataStore（存小配置）、Room（存結構化資料）、Retrofit（和伺服器對話），外加它們的"總排程"——協程。學完這章，你就能寫會記住使用者習慣、會實時更新內容的真 App 了。

#### 一、儲存方案怎麼選：先看這張表

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">方案</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">適合存什麼</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">特點</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">本書哪裡用</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DataStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">零散配置（主題、開關）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">鍵值對，簡單安全</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 54 章記帳本設定</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">結構化資料（賬目、使用者）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真正的 SQLite 資料庫封裝，可查詢</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 54 章賬目記錄</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">（不存，聯網取）伺服器資料</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">HTTP 請求庫的事實標準</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 55 章天氣資料</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
資料三件套的分工

記一個口訣："小配置進 DataStore，成批資料進 Room，外面的資料走 Retrofit"。舊教學裡常見的 SharedPreferences 已被 DataStore 取代，SQLite 手寫 SQL 也已被 Room 取代——直接學新的，別走老路。

#### 二、DataStore：存點小配置

想記住"使用者上次選的幣種""是否開啟深色模式"這類零散值，用 DataStore（Preferences 版）：

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

// 讀：取出來（Flow 會自動通知變化）
val themeFlow: Flow<Boolean> = context.dataStore.data
    .map { it[THEME_KEY] ?: false }
```
:::

注意返回的是 Flow——一個會"流動"的資料流。值一旦改變，所有觀察它的地方自動收到新值。這個概念（響應式）是安卓現代的基石，第 54 章會實戰。

#### 三、Room：給資料安個"真正的家"

記帳本有成百上千筆賬，還要按分類、按月份查詢統計——這需要資料庫。Room 是 SQLite 的官方封裝，把"建表、查資料"變得像寫 Kotlin 一樣自然。三樣東西：

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

// 2. Dao：操作介面（增刪改查）
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

這套"三件套"模板可以原樣搬進你的任何專案——換換欄位名就行。查詢返回 Flow，介面跟著資料自動重新整理，妙不可言。

#### 四、Retrofit：和伺服器說話

天氣、新聞、匯率……這些資料不在手機裡，在別人的伺服器上。Retrofit 讓"向伺服器要資料"變得像調函式一樣簡單。三步走：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Retrofit 三步走</span><span class="dots">···</span>
:::

```
// 1. 定義介面：把 HTTP 請求描述成函式
interface WeatherApi {
    @GET("v1/weather")
    suspend fun getWeather(@Query("city") city: String): WeatherResponse
}

// 2. 建立例項
val api = Retrofit.Builder()
    .baseUrl("https://api.example.com/")
    .addConverterFactory(GsonConverterFactory.create())
    .build()
    .create(WeatherApi::class.java)

// 3. 像調函式一樣呼叫（在協程裡）
val result = api.getWeather("北京")
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
避坑提醒：兩條網路鐵律

{class="mt-1"}
① 網路請求絕不能在主執行緒做——會卡死介面甚至崩潰（NetworkOnMainThreadException）。所有網路呼叫必須放在協程（viewModelScope.launch）裡。② 明文 HTTP 預設被禁止：安卓 9 起要求 HTTPS。測試時若要用 http:// 的本地地址，需要在 Manifest 裡顯式宣告 usesCleartextTraffic——但正式產品必須全走 HTTPS。
:::

#### 五、JSON 解析：給網路資料"翻譯"

伺服器返回的資料大多是 JSON——一串像"巢狀字典"的文字。Retrofit 需要一個"翻譯官"把它變成 Kotlin 物件。2026 年的兩大主流方案：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">方案</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">特點</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">推薦場景</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gson / Moshi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">老牌反射方案，配置零成本</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">快速起步、欄位不多的小專案</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">kotlinx.serialization</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方編譯期方案，更快更安全</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新專案首選（2026 年主流）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
JSON 解析兩大方案

::: div .code-block
:::inline div .code-head
<span>KOTLIN · kotlinx.serialization 示例</span><span class="dots">···</span>
:::

```
// 給資料類加 @Serializable 註解
@Serializable
data class WeatherResponse(
    val weather: List<Weather>,
    val main: Main,
    val name: String
)

// Retrofit 掛上對應 Converter（以 Retrofit 2.11+ 官方支援為例）：
// .addConverterFactory(json.asConverterFactory("application/json".toMediaType()))
```
:::

無論哪種方案，鐵律都是：先看真實返回的 JSON，再定義欄位。很多"解析失敗"的 bug，都是因為欄位名寫錯、巢狀層級猜錯——把原始 JSON 列印出來對照，十秒定位。

#### 六、協程：安卓併發的"普通話"

上面反覆出現的 suspend 和 launch 來自 Kotlin 協程（Coroutine）——安卓官方的併發方案。你可以粗暴地理解為：讓"要等一會兒"的操作（網路、資料庫）不阻塞介面。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 協程初體驗</span><span class="dots">···</span>
:::

```
// 在 ViewModel 裡啟動協程
viewModelScope.launch {
    val records = dao.getAll().first()  // suspend：會自動掛起等待
    // 更新介面狀態……
}

// 關鍵字速記：
// suspend   —— "我要等待，別攔著別人"
// launch    —— "開工！"
// viewModelScope —— 跟著頁面走的"工作間"，頁面銷燬自動收工
```
:::

零基礎先記住用法就好，背後的"掛起與還原"原理可以以後再深究。日常開發你寫的 90% 都是這個模板。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：做一個"每日一句"小應用

{class="mt-1"}
找一個免費的名言 API（比如 hitokoto 之類），用 Retrofit 拉取"每日一句"，顯示在螢幕中央，加個"換一句"按鈕（協程裡重新請求）。再把喜歡的句子用 Room 存進"收藏夾"。這個練習把 DataStore/Room/Retrofit/協程全用了一遍——做完它，第 7、8 章就是小菜一碟。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 口訣：小配置進 DataStore，成批資料進 Room，外面的資料走 Retrofit
- DataStore 返回 Flow：值變了，觀察者自動收到
- Room 三件套：@Entity（表）+ @Dao（操作）+ @Database（總裝），模板可直接複用
- Retrofit 三步：定義介面 → 建立例項 → 協程裡呼叫
- 兩條鐵律：網路不進主執行緒；正式產品必須 HTTPS
- 協程 = 不阻塞介面的等待；viewModelScope 是頁面專屬工作間
:::
