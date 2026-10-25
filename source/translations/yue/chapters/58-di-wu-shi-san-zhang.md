---
id: di-wu-shi-san-zhang
num: 53
part: an-zhuo-kai-fa-pian
nav: 第五十三章：數據儲存與網絡請求
toc: default
kind: chapter
---

### 第五十三章：資料儲存同網絡請求

{class="chapter-intro mb-4"}
一個淨係得個「睇」字嘅 App 係死嘅；識儲資料、識連網絡嘅 App 先至係生嘅。呢一章認識安卓資料層嘅「三件套」：DataStore（存小配置）、Room（存結構化資料）、Retrofit（同伺服器傾偈），仲有佢哋嘅「總調度」——協程。學完呢章，你就可以寫到識記住用戶習慣、識實時更新內容嘅真 App 喇。

#### 一、儲存方案點樣揀：先睇呢張表

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">方案</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">適合存乜嘢</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">特點</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">本書邊度用</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DataStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">零散配置（主題、開關）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">鍵值對，簡單安全</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 54 章記賬本設定</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">結構化資料（賬目、用戶）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真正嘅 SQLite 資料庫封裝，可以查詢</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 54 章賬目記錄</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">（唔儲，上網攞）伺服器資料</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">HTTP 請求庫嘅事實標準</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 55 章天氣資料</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
資料三件套嘅分工

記一個口訣：「小配置入 DataStore，成批資料入 Room，外面嘅資料行 Retrofit」。舊教程入面常見嘅 SharedPreferences 已經被 DataStore 取代，SQLite 手寫 SQL 亦都已被 Room 取代——直接學新嘅，唔好行舊路。

#### 二、DataStore：存啲小配置

想記住「用戶上次揀嘅幣種」「有冇開深色模式」呢類零散值，用 DataStore（Preferences 版）：

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

// 讀：攞出嚟（Flow 會自動通知變化）
val themeFlow: Flow<Boolean> = context.dataStore.data
    .map { it[THEME_KEY] ?: false }
```
:::

留意返回嘅係 Flow——一個會「流動」嘅資料流。個值一改，所有觀察佢嘅地方自動收到新值。呢個概念（響應式）係現代安卓嘅基石，第 54 章會實戰。

#### 三、Room：畀資料安個「真正嘅屋企」

記賬本有成百上千筆賬，仲要按分類、按月份查詢統計——呢樣嘢需要資料庫。Room 係 SQLite 嘅官方封裝，將「建表、查資料」變到好似寫 Kotlin 噉自然。三樣嘢：

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

呢套「三件套」模板可以原封不動搬入你任何項目——換吓欄位名就得。查詢返回 Flow，介面跟住資料自動刷新，妙不可言。

#### 四、Retrofit：同伺服器講嘢

天氣、新聞、匯率……呢啲資料唔喺手機入面，喺其他人嘅伺服器度。Retrofit 令「向伺服器攞資料」變到好似調函數噉簡單。三步行：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Retrofit 三步走</span><span class="dots">···</span>
:::

```
// 1. 定義接口：將 HTTP 請求寫成函數
interface WeatherApi {
    @GET("v1/weather")
    suspend fun getWeather(@Query("city") city: String): WeatherResponse
}

// 2. 建立實例
val api = Retrofit.Builder()
    .baseUrl("https://api.example.com/")
    .addConverterFactory(GsonConverterFactory.create())
    .build()
    .create(WeatherApi::class.java)

// 3. 像調函數一樣調用（喺協程入面）
val result = api.getWeather("北京")
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
避坑提醒：兩條網絡鐵律

{class="mt-1"}
① 網絡請求絕對唔可以喺主線程做——會卡死介面甚至崩潰（NetworkOnMainThreadException）。所有網絡調用必須擺喺協程（viewModelScope.launch）入面。② 明文 HTTP 預設被禁止：安卓 9 開始要求 HTTPS。測試嗰陣如果要 http:// 嘅本地地址，需要喺 Manifest 入面顯式聲明 usesCleartextTraffic——但係正式產品必須全部行 HTTPS。
:::

#### 五、JSON 解析：畀網絡資料「翻譯」

伺服器返回嘅資料大多係 JSON——一串好似「嵌套字典」嘅文字。Retrofit 需要一個「翻譯官」將佢變成 Kotlin 對象。2026 年嘅兩大主流方案：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">方案</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">特點</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">推薦場景</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gson / Moshi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">老牌反射方案，配置零成本</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">快速起步、欄位唔多嘅小項目</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">kotlinx.serialization</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方編譯期方案，更快更安全</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新項目首選（2026 年主流）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
JSON 解析兩大方案

::: div .code-block
:::inline div .code-head
<span>KOTLIN · kotlinx.serialization 示例</span><span class="dots">···</span>
:::

```
// 畀數據類加 @Serializable 註解
@Serializable
data class WeatherResponse(
    val weather: List<Weather>,
    val main: Main,
    val name: String
)

// Retrofit 掛上對應 Converter（以 Retrofit 2.11+ 官方支援爲例）：
// .addConverterFactory(json.asConverterFactory("application/json".toMediaType()))
```
:::

無論邊種方案，鐵律都係：先睇真實返回嘅 JSON，再定義欄位。好多「解析失敗」嘅 bug，都係因為欄位名寫錯、嵌套層級估錯——將原始 JSON print 咗出嚟對照，十秒定位。

#### 六、協程：安卓並發嘅「普通話」

上面反覆出現嘅 suspend 同 launch 嚟自 Kotlin 協程（Coroutine）——安卓官方嘅並發方案。你可以粗略咁理解為：令「要等一陣」嘅操作（網絡、資料庫）唔會阻塞介面。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 協程初體驗</span><span class="dots">···</span>
:::

```
// 喺 ViewModel 入面啓動協程
viewModelScope.launch {
    val records = dao.getAll().first()  // suspend：會自動掛起等
    // 更新界面狀態……
}

// 關鍵詞速記：
// suspend   —— "我要等待，別攔着別人"
// launch    —— "開工！"
// viewModelScope —— 跟着頁面走嘅"工作間"，頁面銷燬自動收工
```
:::

零基礎先記住用法就好，背後嘅「掛起同恢復」原理可以第日再深究。日常開發你寫嘅 90% 都係呢個模板。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
嚟動手：整一個「每日一句」小應用

{class="mt-1"}
搵一個免費嘅名言 API（例如 hitokoto 呢類），用 Retrofit 拉取「每日一句」，顯示喺螢幕中央，加個「換一句」按鈕（喺協程入面重新請求）。再將鍾意嘅句子用 Room 儲入「收藏夾」。呢個練習將 DataStore/Room/Retrofit/協程全部用咗一次——做完佢，第 7、8 章就係小菜一碟。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 口訣：小配置入 DataStore，成批資料入 Room，外面嘅資料行 Retrofit
- DataStore 返回 Flow：個值一變，觀察者自動收到
- Room 三件套：@Entity（表）+ @Dao（操作）+ @Database（總裝），模板可以直接重用
- Retrofit 三步：定義接口 → 建立實例 → 協程入面調用
- 兩條鐵律：網絡唔入主線程；正式產品必須 HTTPS
- 協程 = 唔阻塞介面嘅等待；viewModelScope 係頁面專屬工作間
:::
