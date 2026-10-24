---
id: di-wu-shi-san-zhang
num: 53
part: an-zhuo-kai-fa-pian
nav: 第五十三章：数据存储与网络请求
toc: default
kind: chapter
---

### 第五十三章：数据存储与网络请求

{class="chapter-intro mb-4"}
一个只能"看"的 App 是死的；能存数据、能连网络的 App 才是活的。这一章认识安卓数据层的"三件套"：DataStore（存小配置）、Room（存结构化数据）、Retrofit（和服务器对话），外加它们的"总调度"——协程。学完这章，你就能写会记住用户习惯、会实时更新内容的真 App 了。

#### 一、存储方案怎么选：先看这张表

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">方案</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">适合存什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">特点</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">本书哪里用</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DataStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">零散配置（主题、开关）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">键值对，简单安全</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 54 章记账本设置</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">结构化数据（账目、用户）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真正的 SQLite 数据库封装，可查询</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 54 章账目记录</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">（不存，联网取）服务器数据</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">HTTP 请求库的事实标准</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 55 章天气数据</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
数据三件套的分工

记一个口诀：<strong>"小配置进 DataStore，成批数据进 Room，外面的数据走 Retrofit"</strong>。旧教程里常见的 SharedPreferences 已被 DataStore 取代，SQLite 手写 SQL 也已被 Room 取代——直接学新的，别走老路。

#### 二、DataStore：存点小配置

想记住"用户上次选的币种""是否开启深色模式"这类零散值，用 DataStore（Preferences 版）：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · DataStore 示例</span><span class="dots">···</span>
:::

```
val Context.dataStore by preferencesDataStore(name = "settings")

// 写：存一个值
suspend fun saveTheme(isDark: Boolean) {
    context.dataStore.edit { prefs ->
        prefs[THEME_KEY] = isDark
    }
}

// 读：取出来（Flow 会自动通知变化）
val themeFlow: Flow<Boolean> = context.dataStore.data
    .map { it[THEME_KEY] ?: false }
```
:::

注意返回的是 <strong>Flow</strong>——一个会"流动"的数据流。值一旦改变，所有观察它的地方自动收到新值。这个概念（响应式）是安卓现代的基石，第 54 章会实战。

#### 三、Room：给数据安个"真正的家"

记账本有成百上千笔账，还要按分类、按月份查询统计——这需要数据库。Room 是 SQLite 的官方封装，把"建表、查数据"变得像写 Kotlin 一样自然。三样东西：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Room 三件套：Entity / Dao / Database</span><span class="dots">···</span>
:::

```
// 1. Entity：表结构（一张表 = 一个 data class）
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val amount: Double,
    val category: String,
    val note: String,
    val date: String
)

// 2. Dao：操作接口（增删改查）
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

// 3. Database：总装
@Database(entities = [Record::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun recordDao(): RecordDao
}
```
:::

这套"三件套"模板可以原样搬进你的任何项目——换换字段名就行。查询返回 Flow，界面跟着数据自动刷新，妙不可言。

#### 四、Retrofit：和服务器说话

天气、新闻、汇率……这些数据不在手机里，在别人的服务器上。Retrofit 让"向服务器要数据"变得像调函数一样简单。三步走：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Retrofit 三步走</span><span class="dots">···</span>
:::

```
// 1. 定义接口：把 HTTP 请求描述成函数
interface WeatherApi {
    @GET("v1/weather")
    suspend fun getWeather(@Query("city") city: String): WeatherResponse
}

// 2. 创建实例
val api = Retrofit.Builder()
    .baseUrl("https://api.example.com/")
    .addConverterFactory(GsonConverterFactory.create())
    .build()
    .create(WeatherApi::class.java)

// 3. 像调函数一样调用（在协程里）
val result = api.getWeather("北京")
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>避坑提醒：两条网络铁律

{class="mt-1"}
① <strong>网络请求绝不能在主线程做</strong>——会卡死界面甚至崩溃（NetworkOnMainThreadException）。所有网络调用必须放在协程（viewModelScope.launch）里。② 明文 HTTP 默认被禁止：安卓 9 起要求 HTTPS。测试时若要用 http:// 的本地地址，需要在 Manifest 里显式声明 <code class="inline">usesCleartextTraffic</code>——但正式产品必须全走 HTTPS。
:::

#### 五、JSON 解析：给网络数据"翻译"

服务器返回的数据大多是 JSON——一串像"嵌套字典"的文本。Retrofit 需要一个"翻译官"把它变成 Kotlin 对象。2026 年的两大主流方案：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">方案</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">特点</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">推荐场景</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gson / Moshi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">老牌反射方案，配置零成本</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">快速起步、字段不多的小项目</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">kotlinx.serialization</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方编译期方案，更快更安全</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新项目首选（2026 年主流）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
JSON 解析两大方案

::: div .code-block
:::inline div .code-head
<span>KOTLIN · kotlinx.serialization 示例</span><span class="dots">···</span>
:::

```
// 给数据类加 @Serializable 注解
@Serializable
data class WeatherResponse(
    val weather: List<Weather>,
    val main: Main,
    val name: String
)

// Retrofit 挂上对应 Converter（以 Retrofit 2.11+ 官方支持为例）：
// .addConverterFactory(json.asConverterFactory("application/json".toMediaType()))
```
:::

无论哪种方案，铁律都是：<strong>先看真实返回的 JSON，再定义字段</strong>。很多"解析失败"的 bug，都是因为字段名写错、嵌套层级猜错——把原始 JSON 打印出来对照，十秒定位。

#### 六、协程：安卓并发的"普通话"

上面反复出现的 <code class="inline">suspend</code> 和 <code class="inline">launch</code> 来自 Kotlin 协程（Coroutine）——安卓官方的并发方案。你可以粗暴地理解为：<strong>让"要等一会儿"的操作（网络、数据库）不阻塞界面</strong>。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 协程初体验</span><span class="dots">···</span>
:::

```
// 在 ViewModel 里启动协程
viewModelScope.launch {
    val records = dao.getAll().first()  // suspend：会自动挂起等待
    // 更新界面状态……
}

// 关键词速记：
// suspend   —— "我要等待，别拦着别人"
// launch    —— "开工！"
// viewModelScope —— 跟着页面走的"工作间"，页面销毁自动收工
```
:::

零基础先记住用法就好，背后的"挂起与恢复"原理可以以后再深究。日常开发你写的 90% 都是这个模板。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：做一个"每日一句"小应用

{class="mt-1"}
找一个免费的名言 API（比如 hitokoto 之类），用 Retrofit 拉取"每日一句"，显示在屏幕中央，加个"换一句"按钮（协程里重新请求）。再把喜欢的句子用 Room 存进"收藏夹"。这个练习把 DataStore/Room/Retrofit/协程全用了一遍——做完它，第 7、8 章就是小菜一碟。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 口诀：小配置进 DataStore，成批数据进 Room，外面的数据走 Retrofit
- DataStore 返回 Flow：值变了，观察者自动收到
- Room 三件套：@Entity（表）+ @Dao（操作）+ @Database（总装），模板可直接复用
- Retrofit 三步：定义接口 → 创建实例 → 协程里调用
- 两条铁律：网络不进主线程；正式产品必须 HTTPS
- 协程 = 不阻塞界面的等待；viewModelScope 是页面专属工作间
:::
