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
一个只能"看"的 App 是死的；能存数据、能连网络的 App 才是活的。这一章认识安卓数据层的"三件套"：DataStore（存小配置）、Room（存结构化数据）、Retrofit（和服务器对话），外加它们的"总调度"，协程。学完这章，你就能写会记住用户习惯、会实时更新内容的真 App 了。

这一章与第 52 章是"黄金搭档"：上一章的 ViewModel 解决了"状态放哪"，本章解决"数据从哪来、到哪去"。ViewModel 是状态的容器，容器里的数据要有来源（Room/Retrofit 供给）、有去处（写回 Room/Preferences），两层结合，应用的"数据血脉"就通了。

::: div .quick-read
##### 本章速读（5 分钟版）
一个只能"看"的 App 是死的，能存数据、能连网络的 App 才是活的。这一章教你的就是数据层的"三件套"：DataStore 存零散小配置，Room 存成批的结构化数据，Retrofit 跟服务器对话，再加一个总调度，协程。和上一章是黄金搭档：ViewModel 解决"状态放哪"，这一章解决"数据从哪来、到哪去"。学完你就能写出会记住用户习惯、断网也能看的真 App 了。

最关键的有三件事。第一，记住选型口诀：<strong>小配置进 DataStore，成批数据进 Room，外面的数据走 Retrofit</strong>。别再用老教程里的 SharedPreferences 存列表，也别拿 Room 存一个开关——工具放错了层，代码处处跟你别扭。第二，记住一条主线：<strong>界面只读 Room，网络只写 Room</strong>。服务器数据先落本地库，界面永远从本地读，断网时用户照样能看旧数据，这就是"离线优先"。第三，网络请求的两条铁律：网络不进主线程，正式产品必须 HTTPS；查询想让界面跟着数据走，就返回 Flow，返回 List 的查询拍完照就过时了。协程那节的分工也记一句：主线程管界面，文件和数据库读写交给 Dispatchers.IO，活儿派对车道才不堵；viewModelScope 是页面专属工作间，页面关了它带的活儿自动收摊，这就是它省心的原因。

今天就能做的最小动作：挑一个你项目里的小配置（比如深色模式开关），用 DataStore 存起来，App 杀掉重开它还在——十分钟的事。然后给现有的网络请求过一遍"网络四问"：没网怎么办、超时怎么办、返回非 2xx 怎么办、解析失败怎么办。四个都答得上，才轮得到谈上线。

最大的坑也说清楚。一是主线程 runBlocking 等结果：代码是短了。代价是整条主线程被按住，界面冻结甚至直接崩，协程那几行不是仪式是护栏。二是 JSON 字段全写成非空：服务器少发一个字段解析就失败，网络模型的字段该可空就可空、给默认值，把崩溃降级成降级显示。三是 fallbackToDestructiveMigration 这个"省事神器"，真实含义是"版本对不上就清空用户数据"，开发期用可以，正式包里出现就是给用户埋雷。还有：本地数据库扛不住卸载和换机，重要的数据要留云同步这条路。
##### 速查表
- 存什么用什么：小配置进 DataStore，成批数据进 Room，外面的数据走 Retrofit
- Room 怎么搭：@Entity 建表、@Dao 操作、@Database 总装，模板可直接复用
- 联网三步：定义接口、创建实例、协程里调用，网络永远不进主线程
- 界面怎么跟着数据走：查询返回 Flow，值一变观察者自动收到
- 断网也要能用：界面只读 Room，网络只写 Room，本地当缓存
- 上线前必答网络四问：没网、超时、非 2xx、解析失败各怎么办
- 安全底线：正式产品必须 HTTPS，token 加密再落盘，日志别打敏感信息
- 数据库迁移别乱来：fallbackToDestructiveMigration 等于清空用户数据，正式包禁用
:::

<div class="version-anchor">本章界面路径按 iOS 18.x / HarmonyOS 5.x / Android 15 核对（2026 年 11 月）。你的机型或系统版本不同，菜单名字和位置可能对不上——以你手机上显示的为准。</div>


#### 一、存储方案怎么选：先看这张表

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">方案</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">适合存什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">特点</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">本书哪里用</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DataStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">零散配置（主题、开关）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">键值对，简单安全</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 54 章记账本设置</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">结构化数据（账目、用户）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真正的 SQLite 数据库封装，可查询</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 54 章账目记录</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">（不存，联网取）服务器数据</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">HTTP 请求库的事实标准</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 55 章天气数据</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
数据三件套的分工

记一个口诀：<strong>"小配置进 DataStore，成批数据进 Room，外面的数据走 Retrofit"</strong>。旧教程里常见的 SharedPreferences，官方已推荐用 DataStore 替代，SQLite 手写 SQL 也已被 Room 取代——直接学新的，别走老路。反过来说也成立：别用 SharedPreferences 存列表，也别拿 Room 存一个开关——工具放错了层，代码处处跟你别扭。

这张表的"反例"栏值得展开讲讲，因为"工具放错层"是真实项目里的高频事故。拿 SharedPreferences 存列表：数据一多，每次读取都是全量 JSON 反序列化，列表长到几百条就肉眼可见地卡；拿 Room 存单个开关：建一张表存一个布尔值。查询、迁移的成本远超一个键值对。选型的本质是"数据形态与工具能力的匹配"，掌握了匹配逻辑，遇到新数据类型时自然知道选什么。

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
val themeFlow: Flow&lt;Boolean&gt; = context.dataStore.data
    .map { it[THEME_KEY] ?: false }
```
:::

注意返回的是 <strong>Flow</strong>——一个会"流动"的数据流。值一旦改变，所有观察它的地方自动收到新值。这个概念（响应式）是安卓现代的基石，第 54 章会实战。

Flow 的"响应式"要展开解释一下，因为它是现代安卓最重要的概念之一，传统做法：读一个值 → 显示 → 用户改了设置 → 手动刷新显示。响应式做法：把"值的来源"声明为 Flow → 界面"订阅"这个 Flow → 值变。界面自动收到新值。你不需要写任何"刷新"代码，数据驱动界面，这是 Compose + Flow 组合的核心优势。DataStore 的 data 属性天然是 Flow，Room 的查询也是 Flow，三件套里两个都内置了响应式，这就是为什么"学新方案"不只是换个 API，而是换一种架构思维。

DataStore 还有一个进阶版本：Proto DataStore（用 Protocol Buffers 定义类型安全的数据结构）。它的优势是类型安全（编译期检查）与性能，但需要额外学习 proto 语法。新手建议从 Preferences 版起步，需求复杂（字段多、类型多）再迁移 Proto 版，两者切换的成本不高，因为 DataStore 的"数据层接口"可以保持不变。

#### 三、Room：给数据安个"真正的家"

记账本有成百上千笔账，还要按分类、按月份查询统计，这需要数据库。Room 是 SQLite 的官方封装，把"建表、查数据"变得像写 Kotlin 一样自然。三样东西：

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

这套"三件套"模板可以原样搬进你的任何项目，换换字段名就行。查询返回 Flow，界面跟着数据自动刷新，妙不可言。

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

趁热把边界意识补全。示例代码几乎都只演"成功路径"，真实项目的网络请求有四个必答题：没网怎么办？超时怎么办？返回码不是 2xx 怎么办？解析失败怎么办？四个问题各有各的兜底，全答上了才算能上线的 App。答完还有一步加分动作：把上次的数据缓存一层，地铁里没网也能看到内容——"能用"和"好用"的分界线常在这里，第 55 章的天气项目会真的实践它。

安全习惯也从第一天养成：token 这类敏感数据用加密存储，别塞进普通 DataStore，更别打进日志；接口地址放进配置里，别硬编码在代码中：将来换环境，你会感谢自己。

#### 五、JSON 解析：给网络数据"翻译"

服务器返回的数据大多是 JSON，一串像"嵌套字典"的文本。Retrofit 需要一个"翻译官"把它变成 Kotlin 对象。2026 年的两大主流方案：

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

上面反复出现的 <code class="inline">suspend</code> 和 <code class="inline">launch</code> 来自 Kotlin 协程（Coroutine），安卓官方的并发方案。你可以粗暴地理解为：<strong>让"要等一会儿"的操作（网络、数据库）不阻塞界面</strong>。

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

再多给一句进阶提示：协程跑在哪个调度器（Dispatcher）有讲究——数据库、文件、网络这类 I/O 交给 <code class="inline">Dispatchers.IO</code>，界面状态的更新回到主线程。区别可以以后再抠，但"别在主线程做 I/O"这条，从今天写第一行网络代码起就要记住。

::: div .tip-box .rounded-lg .p-4 .mb-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>一句话记牢

{class="mt-1"}
升级依赖时先升 BOM 与 Kotlin 插件，再看编译报错；单独升某一个库，最容易踩版本不匹配。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：做一个"每日一句"小应用

{class="mt-1"}
找一个免费的名言 API（比如 hitokoto 之类），用 Retrofit 拉取"每日一句"，显示在屏幕中央，加个"换一句"按钮（协程里重新请求）。再把喜欢的句子用 Room 存进"收藏夹"。这个练习把 DataStore/Room/Retrofit/协程全用了一遍，做完它，第 54、55 章就是小菜一碟。
:::

#### 七、把 Room 用完整：增删改、单例与数据库迁移

三件套的最小示例能跑，但一进真实项目，三个问题马上排队上门：改一条记录怎么写？数据库实例从哪拿、要不要每次新建？App 升级后表结构变了，老用户的数据怎么办？这一节把三个坑一次填平，填完你就能放心把 Room 放进正式项目里。

##### Dao 补全：改和按条件删

增删查你在三件套里见过了，补上"改"。@Update 按主键找行、整行替换；想按 id 精确删一条，直接写 SQL 更省事。顺手把两个高频小需求也加上：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordDao 补全</span><span class="dots">···</span>
:::

```
@Dao
interface RecordDao {
    // 单条查询也返回 Flow：这条记录一变，观察它的界面自动刷新
    @Query("SELECT * FROM records WHERE id = :id")
    fun getById(id: Long): Flow&lt;Record?&gt;

    @Update
    suspend fun update(record: Record)

    // 按 id 精确删，不用先查出整个对象
    @Query("DELETE FROM records WHERE id = :id")
    suspend fun deleteById(id: Long)
}
```
:::

两个细节值得记：@Insert 可以返回 Long，值是新行的主键，以后做"账单 + 明细"这类主从表时会用到；查单条也建议返回 Flow 而不是一次性对象，这样"详情页"同样获得自动刷新能力。另外，较新版本的 Room 还提供了 @Upsert，有则更新、无则插入一步到位，做数据同步特别顺手，具体写法以官方文档为准。

把调用链完整串一遍：界面点"保存"，ViewModel 的方法里 viewModelScope.launch，调 Dao 的 suspend insert，Room 写库，getAll() 这条 Flow 自动发射新列表，界面自动更新。全程没有一处"手动刷新"代码，你在第 52 章学的状态容器，在这里正式接上了数据源。

##### Database 实例：全局一份就够

Room.databaseBuilder 每次调用都有开销，而且两个实例同时写同一个库文件还容易出乱子。惯例是写一个单例：第一次用到时构建，之后全 App 共用。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · AppDatabase 单例</span><span class="dots">···</span>
:::

```
@Database(entities = [Record::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun recordDao(): RecordDao

    companion object {
        @Volatile
        private var INSTANCE: AppDatabase? = null

        fun getInstance(context: Context): AppDatabase =
            INSTANCE ?: synchronized(this) {
                INSTANCE ?: Room.databaseBuilder(
                    context.applicationContext,
                    AppDatabase::class.java,
                    "ledger.db"   // 数据库文件名，落在应用私有目录
                ).build().also { INSTANCE = it }
            }
    }
}
```
:::

构建参数里的第三个字符串是数据库文件名，它会在应用私有目录的 databases 子目录里落成一个真实文件。记住这个位置的另一层含义：应用私有目录随卸载一起清空，本地数据库扛不住卸载，云同步才是终极保险，这也是第 54 章综合案例要补上的最后一块。

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>避坑提醒：allowMainThreadQueries()

{class="mt-1"}
老教程里常见的这个开关，意思是"允许在主线程查数据库"，等于把卡顿合法化。演示两行代码时勉强能用，项目里别碰，列表一长，界面直接冻住。正确姿势就是 suspend 函数加 Flow，Room 会自己安排后台线程。
:::

##### 迁移：表结构变了，老数据怎么办

场景来了：App 上线几个月，你想给 records 表加一列"同步状态"。改了 Entity，version 从 1 升到 2，这时 Room 打开老用户的数据库，发现版本对不上，需要一个 Migration 告诉它"从旧结构怎么一步步改到新结构"。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Migration 示例</span><span class="dots">···</span>
:::

```
// 从版本 1 升到 2：给 records 表加一列
val MIGRATION_1_2 = object : Migration(1, 2) {
    override fun migrate(db: SupportSQLiteDatabase) {
        db.execSQL(
            "ALTER TABLE records ADD COLUMN syncStatus INTEGER NOT NULL DEFAULT 0"
        )
    }
}

// 构建数据库时挂上（可以挂多条）：
Room.databaseBuilder(context, AppDatabase::class.java, "ledger.db")
    .addMigrations(MIGRATION_1_2)
    .build()
```
:::

没写迁移直接升版本号，老用户一打开 App 就崩——这是后面"报错门诊"里的头号 Room 病号。你可能在网上见过 fallbackToDestructiveMigration：版本对不上就清库重建，本地数据全丢。开发期图快可以临时用，正式包里绝对不能留，用户升个级，几年的记账没了，这不是 bug，是事故。

写迁移有条纪律：Migration 里的 SQL 只负责"把结构改成 Room 期望的样子"，列名、类型要和改后的 Entity 完全对上，错一个字编译期不报、运行时直接崩。改完先在自己手机上装旧版、造几条数据、再覆盖安装新版走一遍，五分钟的事，能省一晚上的排查。

#### 八、Retrofit 进阶：超时、拦截器与统一错误处理

场景先摆这儿：电梯门一关，信号从满格掉到一格。你的页面还在转圈，用户在心里数秒：数到十还没动静，他就退出了。前面"网络四问"（没网、超时、非 2xx、解析失败）这一节正式作答，顺便给 Retrofit 装上两个高配件：超时和拦截器。

##### 超时与拦截器：都装在 OkHttpClient 上

Retrofit 底层的网络活儿其实是 OkHttpClient 干的。通过 .client() 把配好的 client 递给 Retrofit，超时、拦截器、日志全都从这里进。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 带超时和拦截器的 OkHttpClient</span><span class="dots">···</span>
:::

```
val client = OkHttpClient.Builder()
    .connectTimeout(10, TimeUnit.SECONDS)   // 连不上就放弃的时间
    .readTimeout(30, TimeUnit.SECONDS)      // 连上了但迟迟不给数据的时间
    .addInterceptor { chain ->
        val request = chain.request().newBuilder()
            .addHeader("Authorization", "Bearer $token")
            .build()
        chain.proceed(request)              // 放行，请求继续往下走
    }
    .build()

val api = Retrofit.Builder()
    .baseUrl("https://api.example.com/")
    .client(client)
    // .addConverterFactory(……) 挂上你选的转换器，前文两种任选其一
    .build()
    .create(WeatherApi::class.java)
```
:::

拦截器（Interceptor）可以理解成"每个请求出门前的安检口"：统一塞 token、统一打日志、统一改请求头，都在这里做。上面这段让每个请求自动带上 Authorization 头，十几二十个接口不用一个个手写，将来登录态过期换 token，也只改一处。

超时数值没有标准答案：连接超时通常短一些，读超时按数据量放宽，具体以你的接口表现为准。原则是"宁可快速失败，不要无限等待"：快速失败还能触发重试或给出提示，无限等待只会耗电耗耐心。

##### 统一错误处理：把"成功/失败"变成类型

散落各处的 try-catch 容易漏。更整齐的做法是定义一个状态类型，让编译器逼着你把每种情况都处理到：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · UiState 错误处理模板</span><span class="dots">···</span>
:::

```
// 三种状态，少了哪种编译器都会提醒你
sealed interface UiState&lt;out T&gt; {
    data object Loading : UiState&lt;Nothing&gt;
    data class Success&lt;T&gt;(val data: T) : UiState&lt;T&gt;
    data class Error(val message: String) : UiState&lt;Nothing&gt;
}

private val _weather = MutableStateFlow&lt;UiState&lt;WeatherResponse&gt;&gt;(UiState.Loading)
val weather = _weather.asStateFlow()

fun load(city: String) {
    viewModelScope.launch {
        _weather.value = UiState.Loading
        try {
            _weather.value = UiState.Success(api.getWeather(city))
        } catch (e: Exception) {
            _weather.value = UiState.Error("加载失败，点我重试")
        }
    }
}
```
:::

界面层拿到这个 StateFlow 后 when 一把：Loading 显示转圈，Success 显示数据，Error 显示文案加一个"重试"按钮。这套模板不算新鲜，但很多线上事故的根因就是没装它，"接口挂了，页面白屏，用户以为 App 坏了"。

另一条路线也认识一下：把接口方法的返回值写成 Response&lt;WeatherResponse&gt;，Retrofit 就不自动抛异常，而是把状态码交给你判断（isSuccessful、code()）。两种风格都常见，一个项目里选一种用到底，别混着来。

重试要不要做？只读请求（天气、新闻）失败后让用户手动点重试就够了。写操作的自动重试要小心：网络慢导致的失败，服务端可能其实已经处理成功，盲目重试等于"重复下单"。这类问题的正解在后端的幂等设计上，前端只做防连点：具体方案和你的后端同学对齐，别自己拍脑袋。

#### 九、Flow 与响应式数据：让数据自己流到界面

DataStore 的 data、Room 的 getAll() 都返回 Flow，但 Flow 本身是什么，值得单独一节说透。一句话定义：Flow 是"按时间依次到达的一串数据"，它不是装数据的盒子。它是数据流动的管道。盒子看一眼就完了；管道得"接上"才能持续收货，接的动作叫收集（collect）。

##### 冷流：你不接，它不动

Flow 默认是"冷"的：构建它的代码写在那里并不执行，每次 collect 才真正跑一遍。同一个查询 Flow 收集两次，就查两遍库。听起来像缺点，其实是特性：查询这类动作天然适合"要用才执行"。

管道中途可以加工，操作符的写法和集合的 map/filter 一脉相承，只是"加工完还是一条流"：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Flow 操作符链</span><span class="dots">···</span>
:::

```
dao.getAll()
    .map { list -&gt; list.filter { it.amount &gt; 0 } }  // 只看收入
    .onEach { println("拿到 ${it.size} 条") }       // 途中做点副作用
    .distinctUntilChanged()                        // 数据没变就别惊动界面
    .flowOn(Dispatchers.Default)                   // 上面的加工放后台算
    .collect { list -&gt; render(list) }              // 收集：数据在这被真正消费
```
:::

两个高频操作符单独点名：debounce 是"停止输入一小段时间后再执行"，搜索框必备，不然每敲一个字查一次库、发一次请求；flatMapLatest 是"新输入来了，上一个还没完成的查询直接作废"，防止旧结果晚到覆盖新结果。搜索场景这俩基本是固定搭配。

##### combine：两条流拧成一条

场景：账目列表 + 筛选关键词，任何一个变了界面都要重算。分开监听再互相通知，很容易写出"你更新我、我更新你"的环。combine 把两条流拧成一条。任何一条上游变化，下游自动拿到"最新组合"：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · combine 合并两条流</span><span class="dots">···</span>
:::

```
val visible: Flow&lt;List&lt;Record&gt;&gt; =
    combine(dao.getAll(), keyword) { list, kw -&gt;
        if (kw.isBlank()) list
        else list.filter {
            it.note.contains(kw) || it.category.contains(kw)
        }
    }
```
:::

##### StateFlow：专给界面用的状态流

界面直接订阅普通 Flow 有个别扭处：界面随时可能重建（转个屏幕、切个后台再回来），重建后需要"立刻拿到当前值"，而不是干等下一次变化。StateFlow 就是为界面准备的：必须有初值、任何时刻都能取到最新值、新值和旧值相同时不重复通知。第 52 章写过的 MutableStateFlow/StateFlow 就是它。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · stateIn：把查询流转成界面状态</span><span class="dots">···</span>
:::

```
val records: StateFlow&lt;List&lt;Record&gt;&gt; = dao.getAll()
    .stateIn(
        scope = viewModelScope,
        started = SharingStarted.WhileSubscribed(), // 有人看才开工，短暂离开不重启
        initialValue = emptyList()                  // 开工前的占位值
    )
```
:::

stateIn 是"普通 Flow 转 StateFlow"的桥，三个参数各管一件事：scope 说这条流跟着 ViewModel 活；started 说"有人订阅才开工，没人看就歇一会儿"，短暂离开（比如转个屏）不至于把查询重启一遍；initialValue 是开工前的占位值。亲手配过一遍就懂了。

Compose 界面绑定只要一行 collectAsState()，第 52 章讲状态时你已经见过用法。数据 → StateFlow → 界面，这条链是本书后半部所有项目的骨架。还有个兄弟叫 SharedFlow，适合"事件"类通知（弹一次提示、跳转一次页面这种不该"重播"的），先用不到，遇到了查官方文档。

#### 十、缓存与离线策略：没网也要能看

场景：地铁过隧道，朋友的天气 App 还显示着半小时前的数据，你的直接白屏。差别不在网络库，在缓存策略。思路朴素得很：网络数据落到 Room，界面永远读 Room；有网就刷新，没网就看旧的。

##### Room 当缓存层：单一事实来源

两种做法摆在一起看：

- <strong>直接派</strong>：网络结果 → 界面。写起来快，代价是每次进页面都转圈，断网就空屏，历史上看过什么全忘。
- <strong>缓存派</strong>：网络结果 → 写进 Room → 界面读 Room。第一次联网后，Room 里永远有一份；界面读本地库，打开即显示；刷新只是"往库里写新数据"，界面靠 Flow 自动更新。

缓存派有个正式名字：单一事实来源（Single Source of Truth）。界面不关心数据是网络来的还是本地的，只认 Room 一处。它消灭的是一整类 bug——"界面显示的和数据库里的不一致"。Retrofit 和 Room 的分工也由此清晰：Retrofit 负责"最新的"，Room 负责"手头有的"，网络只管往 Room 写，界面只管订阅 Room。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 天气缓存仓库</span><span class="dots">···</span>
:::

```
class WeatherRepository(
    private val api: WeatherApi,
    private val dao: WeatherDao
) {
    // 界面只订阅这个：永远读库
    val cached: Flow&lt;List&lt;Weather&gt;&gt; = dao.getAll()

    // 有网才调这个：拉最新 → 写库。界面不直接碰它
    suspend fun refresh(city: String) {
        try {
            val resp = api.getWeather(city)
            dao.insertAll(listOf(resp.toEntity(fetchedAt = System.currentTimeMillis())))
        } catch (e: Exception) {
            // 刷新失败不吭声：旧数据还在，下次再试
        }
    }
}
```
:::

##### 过期标记：旧到什么程度该刷新

缓存不能永远信。惯例是给数据记"拉取时间"（实体里的 fetchedAt 字段），进页面时判断：距上次拉取太久就后台刷一次。多久算太久视业务定，天气可能十几分钟就该换，账单缓存放一天也不奇怪。刷新期间旧数据继续显示。新数据到了自动替换，用户全程感知不到等待。这个套路可以概括成"先给旧的，后台换新的"，第 55 章的天气项目就按它写。

两个常见追问提前答了。其一：缓存要不要手动清理？App 缓存不用你操心，空间紧张时系统自己回收，你只管往里写。其二：过期标记存哪？和数据放一起（同一张表加个字段）最省事，别单独开一张"时间戳表"给自己找事。

离线写入怎么和在线数据和平共处？记账 App 的经典解法是给记录加"同步状态"字段：本地新增先标"待同步"，联网后补传，传完改"已同步"。这个字段在迁移那一节的例子里出现过，现在你知道它为什么存在了。

#### 十一、安全要点：HTTPS、token 与日志脱敏

数据层的安全坑不算多，但每一个都够写进事故报告。三件事从第一个项目就做对：全程 HTTPS、token 妥善存、日志不泄密。

##### HTTPS 是底线，不是加分项

安卓 9 起系统默认拒绝明文 HTTP（前面的避坑提醒提过），这不是刁难你，是替你兜底。配套习惯两条：接口地址集中放在配置里（比如 BuildConfig 字段），别散落在代码各处，将来换环境只改一处；证书校验永远别关，网上流传的"信任所有证书"的代码，等于把自家门锁焊死在开门状态，测试环境都不建议用。

##### token 存哪：加密后再落盘

登录后服务器发的 token 相当于一张长期有效的通行证。存普通文件、普通键值存储，都是明文躺在手机里。正规姿势是借助系统密钥体系（安卓上是 Keystore，密钥可以由设备的隔离硬件保管，能力视机型而定）先加密再存盘。官方的加密存储方案这几年一直在演进，具体写法以官方文档为准；你自己要守的原则只有一条：token 不明文落盘、不打日志。

再补一个新手盲区：token 会过期。请求返回"未授权"时要有出路，刷新 token，或者引导重新登录，而不是让用户盯着一个永远失败的页面。

##### 日志脱敏：别把家底打给全世界

开发期把响应体整包打进日志确实方便，风险也实在：Authorization 头、手机号、地址全在里面。真机连过电脑调试、接了第三方日志或崩溃收集，这些内容就可能离开你的手机。底线两条：正式包关掉 body 级日志；确实要打的敏感头先脱敏：OkHttp 的日志拦截器给了专门的开关：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 日志拦截器脱敏</span><span class="dots">···</span>
:::

```
val logging = HttpLoggingInterceptor().apply {
    level = HttpLoggingInterceptor.Level.BODY
    redactHeader("Authorization")   // 日志里这根头永远显示为 ***
}
```
:::

顺手把权限这课补了：联网要在 Manifest 里声明 INTERNET 权限。它属于"正常权限"，声明即授予，不用用户点同意；但漏了声明的报错很迷惑：UnknownHostException（"找不到主机"），新手常以为网断了，其实是权限没给。这个问题在下一节门诊里还会挂号。

#### 十二、三件套综合案例：离线优先的记账本

前面都在发零件，这一节装整机。目标是一个"离线优先"的记账本：断网照样记账查账，联网自动同步。第 54 章会真的把它写出来，这里先把图纸看懂。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-quote-left mr-2"></i>一句话记牢

{class="mt-1"}
界面只读 Room，网络只写 Room。
:::

拆开说：Room 是唯一事实来源；Retrofit 是进货渠道，只负责把远端数据搬进 Room；DataStore 管主题、币种这些设置。用户从头到尾感知不到"网络"这个概念，他看到的只是列表永远是全的。

##### 一次记账的完整旅程

1. 用户点"记一笔"，填金额、选分类，界面只做收集，不做存储。
2. ViewModel 收到事件，在 viewModelScope 里调 Repository 的 addRecord()。
3. Repository 组装一条 Record，同步状态标"待同步"，调 Dao 的 suspend insert。
4. Room 写库，getAll() 这条 Flow 自动发射新列表。
5. 界面订阅着这条 Flow，列表自动多出一行：没有一行"刷新"代码。
6. 联网后同步任务把"待同步"的记录传给服务器，成功后改标"已同步"——Flow 又发射一次，界面上的"未同步"角标自己消失。

注意第 6 步之后没有"通知界面"的代码——因为根本不需要。数据变了流就动，流动了界面就跟，这套机制在第九节已经拆解过了。

##### Repository：三件套的组装车间

::: div .code-block
:::inline div .code-head
<span>KOTLIN · LedgerRepository</span><span class="dots">···</span>
:::

```
class LedgerRepository(
    private val dao: RecordDao,
    private val api: LedgerApi
) {
    // 界面唯一的数据入口：永远读 Room
    val records: Flow&lt;List&lt;Record&gt;&gt; = dao.getAll()

    // 记一笔：只写本地，标"待同步"，全程没有网络代码
    suspend fun addRecord(amount: Double, category: String, note: String) {
        dao.insert(
            Record(
                amount = amount,
                category = category,
                note = note,
                date = todayString(),
                syncStatus = SYNC_PENDING
            )
        )
    }

    // 联网时：把远端账单搬进 Room（upsert：有则更新、无则插入）
    suspend fun syncFromRemote() {
        try {
            api.getRecords().forEach { dao.upsert(it.toEntity()) }
        } catch (e: Exception) {
            // 断网不算错误：本地照常能用，下次再同步
        }
    }
}
```
:::

逐段看：records 只是把 Dao 的 Flow 原样递出去，Repository 不加工不缓存，界面拿到的永远是库的最新状态。addRecord 里没有一行网络代码，所以断网记账畅通无阻。syncFromRemote 把远端账单 upsert 进库，界面一行不用改，列表自己就变了，"数据驱动界面"的复利从这里开始兑现。

冲突问题（同一笔账本地和远端都改过）属于分布式话题，记账场景用"以后修改时间为准"通常够用；要做得精细，靠服务器给每条记录发版本号。水很深，第一个项目别去挑战它。

ViewModel 那层就是第 52 章的模板接上 Repository：状态用 StateFlow 暴露，按钮事件调 Repository 的 suspend 函数。四层各司其职：界面管展示、ViewModel 管状态、Repository 管数据编排、Dao 与 Api 管执行。哪天你想把记账数据整体挪去云数据库，改的只有 Repository 一层，这就是分层的全部意义。

#### 十三、协程进阶：调度器、异常与生命周期

前面把协程当"会等待的 launch"用，写小项目够了。这一节补三件进阶的事：活儿在哪个线程干、出错怎么兜、页面销毁谁收拾现场。

##### Dispatchers：三条车道

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">调度器</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">干的活</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">例子</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dispatchers.Main</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">主线程，碰界面的都在这</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">更新界面状态</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dispatchers.IO</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">等待型操作</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">网络、文件、数据库</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dispatchers.Default</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">计算型操作</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">解析大 JSON、排序、压缩图片</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
三条车道的分工

切换用 withContext：进 IO 干活，干完带着结果回主线程。有个省心事：Room 的 suspend 函数和 DataStore 的 edit 都会自己安排后台线程，调它们不用手动切；只有自己写的耗时逻辑才需要 withContext(Dispatchers.IO)。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · withContext 换车道</span><span class="dots">···</span>
:::

```
viewModelScope.launch {
    val lines = withContext(Dispatchers.IO) {
        file.readLines()                        // 等待型操作，走 IO 车道
    }
    val stats = withContext(Dispatchers.Default) {
        lines.map { it.toDouble() }.sorted()    // 计算型操作，走 Default 车道
    }
    _uiState.value = UiState.Success(stats)     // 回到主线程更新界面
}
```
:::

##### 异常：转圈永远要能停

协程里的异常不会自动变成界面提示，接不住就是崩溃或静默卡死。最小方案第八节给过：launch 里 try-catch，catch 里更新 Error 状态。项目大了以后，可以给作用域配一个 CoroutineExceptionHandler 统一兜底，但它是保险网不是替身：业务上该处理的失败（重试、提示）还是要在现场 try。

async 有一处容易踩：async 块里抛的异常不会立刻冒出来，要等到 await() 那一行才炸。所以 try 要包在 await 外面，而不是 async 里面。并发拉两个接口的完整模板：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 并发请求与异常</span><span class="dots">···</span>
:::

```
viewModelScope.launch {
    try {
        val weatherDeferred = async { api.getWeather("北京") }
        val newsDeferred = async { api.getNews() }
        // 两个请求同时出发；await 时才可能抛异常，所以 try 包在外层
        val weather = weatherDeferred.await()
        val news = newsDeferred.await()
        _uiState.value = UiState.Success(HomeData(weather, news))
    } catch (e: Exception) {
        _uiState.value = UiState.Error("加载失败，点我重试")
    }
}
```
:::

##### 生命周期：viewModelScope 为什么省心

自己 new 的 CoroutineScope 要自己 cancel，忘了就是泄漏。viewModelScope 由框架接管：页面销毁自动取消全部协程，跑了一半的网络请求也会中断：这正是你要的，用户都退出了，没必要替他继续下载。反面教材是 GlobalScope：协程活得比页面久，回调里再摸一下界面就是崩溃，新手阶段直接当它不存在。

取消是"协作式"的：协程只在挂起点（suspend 调用处）响应取消信号。一个不带挂起的 while 循环取消不掉，写长任务时记得周期性调一下 delay 之类的挂起函数，给取消留检查点。

#### 十四、常见报错门诊

数据层的报错信息一个比一个吓人，病根就那几个。按"报错关键词 → 病因 → 药方"挂号，八个高频病号，就诊前先对照：

<strong>病号 1：Expected BEGIN_OBJECT but was BEGIN_ARRAY</strong>

症状：一联网就崩，堆栈停在 JSON 解析。病因：服务器顶层返回的是数组 [...]，你的数据类却按对象 {...} 定义了。药方：先把原始 JSON 完整打出来对照（开发期开 body 日志），顶层是数组就套一层 List 再解析。序列化类报错十有八九是"想象的 JSON"和"真实的 JSON"长得不一样。

<strong>病号 2：NetworkOnMainThreadException</strong>

症状：点按钮秒崩。病因：网络调用写在了点击回调里，没包协程。药方：整个调用挪进 viewModelScope.launch，用第八节的 UiState 模板接结果。

<strong>病号 3：Cannot access database on the main thread</strong>

症状：第一次查库就崩。病因：直接调了普通（非 suspend）的 Dao 方法。药方：把 Dao 方法改成 suspend 或返回 Flow；急着调试也别用 allowMainThreadQueries 糊弄，那是第七节点过名的反面教材。

<strong>病号 4：A migration from 1 to 2 was required but not found</strong>

症状：覆盖安装新版后一打开就崩。病因：Entity 改了、version 升了，但没写对应的 Migration。药方：按第七节补一个 Migration；本地开发懒得保数据可以临时用清库回退，正式包不行。

<strong>病号 5：CLEARTEXT communication not permitted</strong>

症状：请求直接失败，提示明文通信被禁。病因：接口地址是 http://。药方：换成 https://；本机调试的临时豁免（usesCleartextTraffic）用完记得撤。

<strong>病号 6：UnknownHostException</strong>

症状：找不到主机。病因按概率排：没声明 INTERNET 权限 > 域名拼错 > 真的断网。药方：先查 Manifest，再查 baseUrl 拼写，最后才怀疑网络。

<strong>病号 7：界面不动，Flow"不发射"</strong>

症状：不报错，但改了数据列表不变。病因常见三种：界面没收集（忘了 collectAsState 或 collect）；查询写成了返回 List 而不是 Flow；数据库被建了两个实例，写 A 读 B。药方：沿着"写库 → Flow → 收集 → 界面"这条链逐段排查，断在哪修哪。

<strong>病号 8：There are multiple DataStores active for the same file</strong>

症状：第一次读写没事，第二次崩。病因：DataStore 按文件名全局只能有一个实例，代码里每次都新建了。药方：改成顶层属性或单例持有，第二章开头那段写法就是对的。

<strong>病号 9：Room 报"表结构不匹配"（迁移后字段对不上）</strong>

症状：覆盖安装新版后崩，报错里列出两份表结构，"期望的"和"实际的"。病因：Migration 写的 SQL 和改后的 Entity 对不上。列名拼错、类型不一致、漏了 NOT NULL 字段的默认值。药方：把报错里的两份表结构逐列对照，Room 其实已经把答案打印给你了，照着改 Migration 就行。

<strong>病号 10：MissingFieldException（解析时字段缺失）</strong>

症状：昨天还好的接口，今天突然解析失败。病因：服务器少发了某个字段，而你的数据类把它声明成必填。药方：网络模型的字段一律给默认值：数字给 0、字符串给空串、复杂对象用可空类型，把"少字段"从崩溃降级成"该处显示占位内容"。误区清单里"字段全非空"那条，病根就在这。

<strong>病号 11：Unresolved reference: suspend / Flow</strong>

症状：照抄教程，编译不过。病因：依赖没加齐或版本太旧，协程、生命周期、Room 各自要带，缺一个就不认识 suspend 和 Flow。药方：以官方文档的依赖清单为准，先对齐 BOM 再补库，别凭记忆手敲版本号。

<strong>病号 12：查询结果"对，但顺序乱"</strong>

症状：列表显示正常，顺序和预期不一致。病因：SELECT 没写 ORDER BY，或者拿字符串排日期——"2026-1-5" 和 "2026-12-30" 按字符串排会乱。药方：日期存标准格式或时间戳再排；查询里显式写 ORDER BY，别指望数据库"默认"给你什么顺序。

门诊看不完的病，统一急救动作：把报错原文完整复制去搜，比"我的 App 崩了"有效一百倍，报错信息本身就是最好的检索词。搜之前顺手确认两件事：报错发生在哪个操作之后（点按钮、切页面还是开机），以及真机还是模拟器，这两个信息能让你的检索结果准一大截。

#### 十五、三平台数据层对照

本章讲的是安卓三件套，但"数据层"这个分层的思想在三个平台几乎逐字通用。认功能，不认名字：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">能力</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">安卓</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">iOS</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">鸿蒙</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">结构化存储</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData（较新方案）与 CoreData</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ArkData 里的关系型数据库</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">键值小存储</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DataStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用户首选项（Preferences）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">网络请求</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit（底层 OkHttp）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession 与第三方 Alamofire</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Network Kit 的 http 模块</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">响应式</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Flow 与 StateFlow</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Combine 与 async/await</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ArkUI 的状态装饰器</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
三平台数据层能力对照

对照着读：Room 与 SwiftData/CoreData 都是"对象映射进数据库 + 查询结果可观察"；Retrofit、Alamofire、Network Kit 都是"把 HTTP 请求包装成函数调用"；Flow、Combine、ArkUI 状态装饰器解决的都是同一个问题，"数据变了，界面自动变"。iOS 那列多一句：SwiftData 是较新的方案，存量项目里 CoreData 还大量存在，两者会长期共存，看懂老代码两样都得认识；鸿蒙的 ArkData 是官方数据管理框架的统称，具体模块名与用法以官方文档为准。

顺序建议：概念先于 API。你在本章建立的"存储分层 + 响应式数据 + 仓储层"心智模型到哪个平台都值钱；换平台时只查"这东西在这儿叫什么"，不必把架构重学一遍。这也是本书把安卓讲透的理由之一，公开资料最全。学会一次，迁移成本最低。

#### 十六、FAQ：数据层十问

这些问题来自真实的学习过程，每个都带着一点"我知道问出来很傻，但它真的困扰过我"的气质。傻问题才是好问题。

<strong>问：项目里已经一堆 SharedPreferences 了，要全部重写成 DataStore 吗？</strong>

不用急。新代码一律 DataStore；存量数据官方提供了一次性迁移的方案（把旧键值搬进 DataStore），以官方文档为准。重写的真正动机是"要存的数据变复杂了"，单纯为了新而新，不值当。

<strong>问：Room 的表里能存图片吗？</strong>

技术上能（存字节），实际上别。图片本体放应用文件目录，表里只存路径或文件名。大字段会让整表查询变慢：数据库存"指针"，文件系统存"本体"，这是通用经验。

<strong>问：Flow 和 LiveData 什么关系？老项目里全是 LiveData，我要学吗？</strong>

LiveData 是上一代的生命周期感知方案，新项目官方主推 Flow 配合生命周期感知的收集方式。看懂老代码需要认识 LiveData，写新代码优先 Flow。两者心智模型相通，切换成本不高。

<strong>问：两张表怎么关联？比如账单和它的明细。</strong>

Room 支持外键和关系查询（@Relation 一类），官方文档有完整例子。建议新手先把单表玩熟，再上关联，关联查询的坑（嵌套对象、一对多）值得单独留一个晚上。

<strong>问：服务器接口改版了，老版本 App 会崩吗？</strong>

可能解析失败。防线有三：App 端字段允许缺失（给默认值，别全写成非空）；后端尽量向后兼容（只加字段不删字段）；解析失败走 Error 态而不是崩。三条都在，接口改版就是"功能降级"，而不是"事故"。

<strong>问：卸载重装，数据还在吗？</strong>

应用私有目录（数据库、DataStore、文件）随卸载清空；能否通过系统备份恢复，视机型与设置而定，别指望它。重要的用户数据要有云端副本，"离线优先 + 云同步"才是完整答案，第 54 章综合案例会补上这半边。

<strong>问：列表多长需要分页？</strong>

没有统一数字。信号是体感：滚动掉帧、一次查询肉眼可见地慢，就该考虑官方的分页方案（Paging 一类）。几百条的记账数据通常用不上，别提前优化。

<strong>问：我能让主线程"等一下"网络结果吗？就等一秒。</strong>

不能。这一秒是界面冻结的一秒，系统对主线程网络请求还会直接抛异常（门诊病号 2）。正确姿势永远是协程加状态：发起 → Loading → 结果到了更新界面。代码看着多两行，体验差一个次元。

<strong>问：为什么要 Repository 这一层？ViewModel 直接调 Dao 不行吗？</strong>

小项目直接调，没人拦你。加一层的原因：数据来源多了以后（本地 + 远端 + 缓存），编排逻辑得有个家；测试时可以把 Repository 换成假实现。等你第 54 章把记账本写完，会自然知道这层该不该加。

<strong>问：Room 能不能存对象列表？比如一个 List&lt;String&gt; 字段。</strong>

直接存不行：Room 只认基本类型和 String。官方给了 TypeConverter 机制：你写好"对象 ↔ 基本类型"的转换函数，Room 在存取时自动转换。能用，但往一列里塞复杂结构会让这条数据没法单独查询，优先考虑拆一张子表，转换器留给轻量场景。

<strong>问：DataStore 的值，我只想读一次怎么办？</strong>

用 first()，从流里取第一个值就收工，适合"进页面读一次设置"这类一次性需求；持续监听变化才用 collect。反过来，别在 collect 里塞"只执行一次"的标志位，那是把管道当盒子用，迟早出乱子。

<strong>问：编译报"no such table"，表明明建了啊？</strong>

表名和 Entity 的 tableName 对不上，或者查询里写了 Entity 没有的列。Room 的 SQL 是编译期校验的，这正是它的优点之一：报错提前到编译，改到编译通过为止，别自己绕过去。

<strong>问：服务器返回的 id 是带引号的 "123"，我定义成 Long 就崩，怎么办？</strong>

以服务器实际类型为准定义字段，或者在转换器里收编这个"看起来像数字的字符串"。解析层的铁律是照实描述、不擅自升格——它看起来像数字，不等于它承诺永远是数字。

<strong>问：需要"每次启动都清一遍缓存"吗？</strong>

一般不需要。缓存空间系统自己管，该不该刷新由过期标记判断；真要清数据的场景是"退出登录"这类隐私需求，那叫清数据，不叫清缓存，两者别混。

<strong>问：电脑上 localhost 调试的接口，真机能访问吗？</strong>

真机上的 localhost 是手机自己，不是你的电脑。用电脑的局域网地址，并保证手机和电脑在同一网络；模拟器访问宿主机有专门的地址别名，视模拟器而定。查官方文档。另外记得前文的铁律：本地 http 调试要临时声明明文许可，联调完撤掉。

#### 十七、三个真实项目：三件套怎么落地

选型表背得再熟，不如看三个真实项目怎么落子。每个项目的组合都不一样，这正是三件套的妙处：它们是积木，不是套餐。

##### 项目 A：离线新闻阅读器

场景：凌晨的机场，赶早班机，想趁登机前把今天的新闻刷完，信号时有时无。数据层这么搭：新闻列表走"缓存派"（第十节），Retrofit 拉最新的 feed 写进 Room，界面只读 Room；DataStore 存两个偏好：字号大小、是否只看某几个栏目。正文里嵌的图片不进数据库——表里只存图片地址，加载交给专门的图片库（Glide、Coil 这类成熟方案都行）。

这个项目的坑在解析：很多新闻接口的正文是带 HTML 标签的富文本，清洗是计算型操作，放 Default 车道；feed 一次拉几十条，别一条条 insert，批量写（下一节的"事务"就是为它准备的）。另一个坑是"已读标记"：已读状态存 Room 的一张小表，还是 DataStore 的键值？条目多、要按时间清理，就进 Room；量小，DataStore 也行——这正是第一节"选型看形态"的实战版。

##### 项目 B：小商家的记账与欠款本

场景：小区门口的水果店，老板娘记账靠脑子，月底对账靠翻本子。给她做一个 App：Room 是绝对主角，每一笔销售、每一笔赊账都是结构化数据；"按客户汇总欠款"就是一条 GROUP BY 查询；月底导出对账单，把查询结果拼成 CSV 写进文件（IO 车道），再通过系统分享面板发出去。

给这类项目一个特别提醒：删除要"软"。老板娘手滑删错一笔账，硬删除就是数据蒸发，找不回来。加一个"是否已删除"的字段，删除只是打标记，界面上过滤掉，真删错了，翻回来就行。这个习惯在"数据是别人的生计"时尤其重要。

##### 项目 C：学生课程表

场景：开学第一周，课程表 App 是刚需。它的数据层分工堪称教科书：课程条目（哪天、第几节、教室、老师）进 Room，查"今天的课"就是一条按星期几过滤的 SQL；"当前是第几教学周""主题色""要不要显示周末"这类零散配置进 DataStore。想加"上课前提醒"，用的是系统能力（视机型与系统版本而定），数据层只要能按时把下节课吐给系统就行。

三个项目摆完，回看第一节的口诀会有新的体会：口诀没变，变的是你对"什么算小配置、什么算成批数据"的判断力。这种判断力没有捷径，就是每个项目亲手搭一遍。

#### 十八、数据层的测试与调试

写完不等于写对。数据层的 bug 有个特点：界面好好的，数据悄悄错了，等你发现，往往已经记了半个月的错账。这一节给你几件趁手的调试与验证工具。

##### 调试第一现场：Logcat 与网络日志

报错先看 Logcat（日志面板）：按进程过滤你的 App，按关键字搜报错原文。网络问题配合第八节的日志拦截器，开发期开到 BODY 级别，请求发了什么、服务器回了什么，一行行都摆在明面上。记得联调完把级别调回去，第十一节的脱敏原则还管着这里。

##### Room 的"透视镜"

数据库不再是黑盒：Android Studio 的 App Inspection 面板（视 IDE 版本与运行方式而定，找不到就搜官方文档）可以在调试时直接看表里的数据，甚至跑一句 SQL 验证查询写得对不对。排查"明明插了数据界面却不显示"这类问题时，先开这个面板看表里到底有没有——十秒钟把"写入问题"和"显示问题"切成两半。

##### 测试怎么起步

不用一上来就追求覆盖率。两个性价比最高的起点：其一，Repository 的逻辑测试：接口用"假实现"（一个返回固定数据的 FakeApi），Dao 用官方支持的内存数据库方案（测试跑完即焚，不碰真实文件），具体写法以官方文档为准；其二，把"网络四问"的每个分支手动触发一遍：飞行模式、错域名、把超时调小、返回坏 JSON——确认每种情况界面都有得看，而不是崩。

调试心法一句：二分定位。注释掉一半代码，问题还在不在？在，bug 在剩下的一半里；不在，在被注释的那一半里。听起来笨，但对"数据莫名不对"这类悬案，比盯着代码干瞪眼快得多。

#### 十九、数据层长大之后：索引、事务与体量

几百条数据时怎么写都对；数据到几万条，写法就开始分出高下。三个"长大之后"的知识点，先知道，用到了再深究。

##### 索引：给常查的字段建目录

在 @Entity 上可以声明 @Index，给某个字段建索引，相当于给书加目录：按 date、category 这类常查询的字段建，按条件查的速度能差出数量级；代价是写入略慢、文件略大。别无脑给全字段加索引，目录比正文还厚的书，翻起来也累。

##### 事务：一万条插入和一次插入的差距

批量写数据时，一条条 insert 和包在一个事务里一次写完，速度差出几个数量级是常事，每条 insert 默认各自落盘一次，事务把多次落盘合并成一次。Room 里用 @Transaction 注解或 withTransaction 函数（以官方文档为准）；配合 @Insert 直接收 List 的写法，批量导入一次搞定。

##### 响应太大：先想后端，再想前端

接口一返回就是几兆 JSON。前端再怎么优化都是被动挨打。第一顺位是和后端商量"字段裁剪、分页返回"；前端能做的是解析放 Default 车道、只把需要的字段映射进实体。主线程卡住几秒，系统会弹"应用无响应"（ANR），而数据层的大 JSON 正是最常见的元凶之一。

##### 分页：列表再长也不怕

几万条记录全量塞进一个列表，再快的库也会慢，再好的手机也会烫。分页的思路是"界面看到哪，才加载哪"：官方的 Paging 库把"按页查询、自动续页、数据变化自动刷新"打包好了，Room 的查询接上它，几万条数据和几十条的手感可以做到差不多。接法以官方文档为准。

比 Paging 更轻的过渡方案也常用：列表先只查最近一段（比如"最近三个月"），页面底部放一个"查看更早的记录"按钮，点了再往后查一段。两行查询的事，撑过 App 的前半生绰绰有余，等真需要 Paging 的那天，你已经清楚痛点具体长什么样了。

这一节的几件事（索引、事务、分页）指向同一个判断：性能问题不是"上线前统一优化"出来的，是"设计表和查询时顺手想"出来的。字段怎么定、查询怎么写、列表怎么喂——这些选择在你写下第一行代码时就已经做了。

#### 二十、账号与多设备同步入门

手机上记的账，换了平板也想看，这就是同步要解决的事。完整方案水很深，但"最小可用模型"值得现在就懂，因为第十二节的 syncStatus 字段就是它的地基。

##### 最小同步模型

三句话：服务器存一份权威数据；每条记录带"最后修改时间"（updatedAt）；客户端联网时把远端拉下来、按时间新覆盖旧，再把本地"待同步"的推上去。推完拉完，两端趋同。这个模型覆盖了大多数个人工具类 App 的需求，剩下的问题都叫"冲突"。

##### 冲突：两个人同时改一条

手机上把"午饭 30 元"改成 35，平板同一时刻改成 33，服务器听谁的？"以后改的为准"是大多数场景的默认答案；认真做就给每条记录加版本号，由服务端裁决。前者现在就能写，后者留给需求真出现的那天，过早设计冲突策略，是数据层最典型的过度工程。

##### 退出登录：数据怎么办

两个问题提前想：其一，本地数据清不清？私人数据（记账、日记）建议清，或至少加密留档，别让下一个借手机的人翻到；清不清没有标准答案，看产品定位。其二，后台任务停没停？退出登录要顺手把同步协程、轮询任务全取消：第十三节说的"viewModelScope 自动取消"管不到你自己建的 scope，记得手动 cancel。

顺序建议：先把离线体验做完美，再上同步。同步是 bug 高发区，而"离线也能用"是它的安全网，同步出问题最多数据旧一点，不至于没法用。

#### 二十一、把三件套装进新项目：最小骨架

学完零件，最后给一张"新项目开工图"。照着搭，十分钟把数据层的架子立起来。

##### 目录结构：一眼能找到东西

不必教条，但要有约定。常见做法：data 目录装数据层：entity（表结构）、dao、db（Database 与迁移）、api（Retrofit 接口与配置）、repo（Repository）；界面层按功能分目录。只准调用 Repository，不准直接摸 Dao 和 Api。目录名随你，规矩只有一条：数据来源只在 data 层出现。

##### Application 类：单例的挂载点

数据库和网络客户端都要全局单例，挂载点就是 Application 子类：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · MyApp.kt</span><span class="dots">···</span>
:::

```
class MyApp : Application() {
    // lazy：第一次用到才初始化，不拖慢启动
    val database by lazy { AppDatabase.getInstance(this) }
    val ledgerApi by lazy { buildLedgerApi() }   // 用第八节的 OkHttp + Retrofit 配置
}
```
:::

别忘了在 Manifest 里注册这个 Application 类（android:name 属性），漏注册是新手高频翻车点，症状是运行时各种"拿不到依赖"的报错。

ViewModel 怎么拿到这些依赖？第 52 章的工厂写法可以起步；项目大了会想上依赖注入框架（Hilt 是目前的常见选择），以官方文档为准——新手期不必强上，先把"谁创建、谁使用"想清楚，比框架本身重要。

依赖版本怎么填？以官方文档为准，并沿用本章开头那条经验：先对齐 BOM 与 Kotlin 插件版本，再补各个库，版本错配的报错，能把一个正确的骨架折腾一下午。

#### 二十二、动手清单：一周把三件套练进手指

看懂和写出之间隔着一周动手。下面这份清单每天不超过两小时，做完刚好接上第 54 章。

1. <strong>第 1 天</strong>：DataStore 存"深色模式"开关，杀掉 App 重开，设置还在。
2. <strong>第 2 天</strong>：照第七节搭 Room 三件套，手工插十条数据，用 IDE 的数据库面板亲眼看看表。
3. <strong>第 3 天</strong>：把列表查询接到 StateFlow 再绑到界面，然后改一条数据，什么都不做，界面自己变。
4. <strong>第 4 天</strong>：Retrofit 接一个公开接口，打印原始 JSON 对照着定义字段，跑通成功路径。
5. <strong>第 5 天</strong>：把第 4 天的数据写进 Room，界面改成只读库；开飞行模式重进，还有内容。
6. <strong>第 6 天</strong>：加上 UiState 三态和"重试"按钮，把第 6 节门诊里的网络故障手动触发一遍。
7. <strong>第 7 天</strong>：合体，离线记账加同步标记，有条件就接个免费后端，把 syncFromRemote 真正跑通。

卡住超过半小时就翻回对应小节；还不通，就把报错原文拿去搜。别硬耗，这一章的每一节，本来就是为"翻回来查"而写的。

#### 二十四、场景深拆：天气 App 的数据层五幕剧

第 55 章会把天气 App 完整写出来，这一节先把它的数据层拆成五幕剧。你可以拿它当剧本：每一幕都是前面小节的排列组合，看懂幕与幕之间怎么衔接，到第 55 章就是照着施工。

##### 第一幕：添加城市

用户在搜索框输入"昆明"，界面把字符变化收集成一条 Flow，debounce 之后拿关键词去调城市搜索接口：注意这一步还没碰天气数据，先拿到的是城市编码。搜索过的城市顺手写进 Room 的一张小表：下次输入"昆"，提示列表里就有"昆明"，不用再等网络。这个细节让搜索从"每次都等"变成"常用秒选"，成本只是多一张表加一条 insert。

##### 第二幕：首次拉取

拿到城市编码，Repository 调天气接口，把返回写进 Room，fetchedAt 记下当前时间。界面此刻显示的是 UiState.Loading 的转圈；写库完成的瞬间 Flow 发射、数据上屏、状态切到 Success。第八节写的错误处理模板在这里原样复用：超时、断网、解析失败各有各的提示，不会白屏。

##### 第三幕：二次进入

用户关掉 App 又打开。界面第一时间订阅 Room，上一份天气立刻上屏——不是等网络，是本地库直接给。后台同时比对 fetchedAt，发现数据过了"新鲜期"，静默调接口刷新，新数据写库，Flow 再发射一次，界面无感更新。用户感受到的是"秒开"。实际发生的是"先给旧的、后台换新的"：第十节缓存派的打法。带新鲜度判断的刷新函数大概长这样：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 带过期标记的刷新</span><span class="dots">···</span>
:::

```
override suspend fun refresh(city: String) {
    val latest = dao.getLatest(city)
    val isFresh = latest != null &amp;&amp;
        System.currentTimeMillis() - latest.fetchedAt &lt; FRESH_MS  // 多久算新鲜，视业务定
    if (isFresh) return               // 还新鲜，不打扰服务器
    try {
        dao.insertAll(api.getWeather(city).toEntities())
    } catch (e: Exception) {
        // 断网：旧数据继续服役，界面不受影响
    }
}
```
:::

##### 第四幕：断网

地铁过隧道，用户下拉刷新。refresh() 的 try 接住异常，状态机不动，旧数据继续显示；顶栏给一条"当前可能不是最新数据"的轻提示。这一幕的关键词是"降级"而不是"报错"，断网不是用户的错，界面不该用大红叉惩罚他。顺手检查一下重试按钮：断网时点了要停在原地给出提示，而不是崩出一屏堆栈。

##### 第五幕：后台定时

就算用户不开 App，天气也想隔几小时自己更新一次。这超出了 viewModelScope 的管辖：它随页面生、随页面死，页面不开它就不存在。这种需求要靠系统级的后台任务调度，官方的 WorkManager 是常见选择：注册一个"最少间隔多久跑一次"的任务，系统自己挑省电的时机执行。具体配置第 55 章拆，这里先认个脸。

五幕演完你会发现没有一幕是新技术：Flow、Room、Retrofit、UiState、过期标记、后台任务，全是前面出现过的零件。数据层设计的常态就是这样：难点从来不在记住 API，而在面对新需求时，能自己排出这五幕。

#### 二十五、给不同人群的数据层建议

同一套三件套，服务不同人群时重心完全不同。这一节按人给方案，你自己写 App，或者给家里人做小工具，都能对号入座。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">人群</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">数据层重心</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">最容易踩的坑</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">爸妈</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">离线优先 + 偏好极简</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">让老人手动同步</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">学生党</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room 分层练手</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一张表塞所有数据</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">出差党</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">按天过期的缓存</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">缓存永不更新</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">小商家</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">软删除 + 导出</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">硬删除丢账</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
人群 × 数据层重心

<strong>给爸妈的 App：设置越少越好。</strong>DataStore 里真正值得存的只有"字号大小"和"上次看到哪"，深色模式跟随系统就好，别给老人出选择题。列表数据一律离线优先——他们在地铁上、在没信号的老家，App 打开必须有内容；同步必须全自动，绝不能让老人理解什么叫"手动同步"。界面上永远不出现"数据层"三个字，就是数据层最大的功劳。

<strong>给学生党：课程表加零花账。</strong>两份数据形态不同，正好练分层：课程条目（哪天、第几节、教室）进 Room，查"今天的课"是一条按星期几过滤的 SQL；消费记录也进 Room，月底一条 SUM 出总花费；"本周是第几教学周"这种一个数字的配置进 DataStore。第一晚搭出"今天的课"，第二晚加"本月花了多少"，成就感来得快，最适合当三件套的第一个完整练手项目。

<strong>给出差党：汇率与行程。</strong>汇率数据"隔一阵才变"，缓存按天判断新鲜度，当天拉一次就够，没必要每次打开都请求；行程信息（航班号、酒店地址、确认码）量小但极重要，建议 Room 加云同步双保险——手机没电了，借同事的设备登录网页版也能过安检。这类数据丢一条的代价，是误一趟飞机。

<strong>给小商家：能导出、能找回。</strong>第十七节水果店案例再补两条：账目要能导出成 CSV，通过系统分享面板发出去；数据要用软删除，手滑删错能翻回来。再补一条容易被忽略的——换手机。安卓的备份与换机迁移能力视机型与系统而定，别把"用户自己会备份"当借口，重要数据要么云同步，要么定期提醒导出。

对号入座完再回头看第一节的选型表，会有新的体会："给谁做"比"做什么"更影响数据层设计。同一门生意，对象是老人还是店主，离线策略、同步策略、删除策略全都不一样，需求里的人，比需求里的功能，更值得你多想一层。

#### 二十六、数据层的来路：老方案长什么样

你在网上搜教程，一半结果还在讲"老三样"：SharedPreferences、SQLiteOpenHelper、AsyncTask。认得它们不是为了用，是为了看懂老代码，以及明白新方案到底新在哪。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">需求</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">老方案</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">新方案</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">新在哪</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">键值配置</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SharedPreferences</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DataStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">协程 + Flow，不卡主线程</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">结构化存储</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SQLiteOpenHelper</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">注解生成代码，查询可观察</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">后台任务</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AsyncTask、手开线程</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">协程</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">生命周期感知，取消内置</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
老三样与新三样

<strong>SharedPreferences → DataStore。</strong>老的键值存储是同步 API：主线程读、主线程写，文件一大就卡界面，而且没法"值变了通知我"；写入失败的返回值，老代码常常没人看。DataStore 把这些全修了：读写全是挂起函数，读取天然是 Flow，失败藏不住。新代码没有理由再用它；存量数据官方有迁移通道，以官方文档为准。

<strong>SQLiteOpenHelper → Room。</strong>再往前，操作数据库要手写 SQL、手动把 Cursor 一行行读成对象、自己管版本升级，样板代码几百行起，还容易在字符串拼接里埋错。Room 底下其实还是 SQLite，变的是你写的部分：注解描述表结构，SQL 写在注解里且编译期校验，剩下的代码由编译器生成。老项目里手写 SQLite 的还不少，看懂即可，新项目没理由从它起步。

<strong>AsyncTask → 协程。</strong>老方案做后台任务，要继承一个类、重写两个方法，自己处理"页面已经销毁但任务还在跑"的尴尬，写错就是内存泄漏。协程把这套流程压缩成 launch 加 suspend，取消、换线程、生命周期全内置。看到教程里还在写 AsyncTask 的，基本可以直接判断年代。

给一个判断教程新旧的小技巧：看它怎么开线程。写 new Thread、AsyncTask、runOnUiThread 的多半是旧教程；写 viewModelScope.launch、suspend、Flow 的才是本章的同路人。API 会老，思路不老——存储分层、响应式、别堵主线程，这三条十年前成立，十年后大概率还成立。老代码看得多了你还会发现：每一代"新方案"都在解决上一代的同一类痛，卡顿、泄漏、样板代码。知道来路，才不容易被下一个"新方案"晃点。

#### 二十七、进阶三招：学有余力再看

三招都不难，但都踩在前面几节的地基上，所以压轴。

##### 第一招：把回调变成 Flow

很多系统能力（定位、传感器、连接状态变化）的 API 是"注册一个监听器"的回调风格，和 Flow 的管道风格接不上。官方提供了 callbackFlow 一类的桥接构建器，把回调装进管道，界面就能像订阅 Room 一样订阅这些事件。代码不长，思路值钱：让整个 App 只有 Flow 一种数据形态，所有来源统一收编，界面层不需要知道数据是从数据库、网络还是传感器流过来的。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · callbackFlow 示意</span><span class="dots">···</span>
:::

```
val locationFlow: Flow&lt;Location&gt; = callbackFlow {
    registerListener { loc -&gt; trySend(loc) }     // 回调塞进管道
    awaitClose { unregisterListener() }          // 管道关闭时反注册，防泄漏
}
```
:::

练手建议：挑一个最小的系统回调（比如网络连接状态变化），跑通"回调进、Flow 出"，这一招就归你了。awaitClose 为什么必须有、漏了会怎样，官方文档解释得很清楚，值得去读。

##### 第二招：数据库文件加密

第十一节管住了 token，但记账、日记这类数据本体还躺在明文文件里。数据库文件级别的加密方案存在（官方与第三方都有），接入成本视方案而定，以官方文档为准。多数工具类 App 用不上，但做日记本、私人记账这类贴身产品时，值得多问一句，加密不是万能的，明文却是确定的不及格。

##### 第三招：定时后台同步

第二十四节第五幕留下的钩子：页面死了谁来干活？WorkManager 允许你注册"最少间隔多久跑一次"的后台任务，系统挑省电的时机执行，设备重启后任务还在；约束条件（比如"有网才跑"）也是声明式的：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · WorkManager 示意</span><span class="dots">···</span>
:::

```
val syncRequest = PeriodicWorkRequestBuilder&lt;SyncWorker&gt;(6, TimeUnit.HOURS)  // 间隔按业务定
    .setConstraints(
        Constraints.Builder()
            .setRequiredNetworkType(NetworkType.CONNECTED)
            .build()
    )
    .build()
WorkManager.getInstance(context).enqueue(syncRequest)
```
:::

三招学完不必急着全用上：它们是"遇到了再回来查"的工具，不是"每个项目必装"的仪式。数据层的功力体现在用对的工具做对的事：配置进 DataStore、账目进 Room、天气走 Retrofit、定时交给 WorkManager，每样东西待在它该待的层。

#### 二十八、误区清单

收尾前把最容易信错的几句话集中处理。判断标准不是"能不能跑"。判断标准是"数据量大了、断网了、App 升级了之后还能不能跑"：

1. <strong>"查询一次，永远新鲜。"</strong>其实是：只有返回 Flow 的查询才是活的，返回 List 的查询拍完照就过时了。界面要跟着数据走，查的方法本身就得是流。
2. <strong>"JSON 字段全写成非空最安全。"</strong>恰恰相反：服务器少发一个字段，解析就失败。网络模型的字段默认可空并给默认值，把"缺字段"从崩溃降级成降级显示。
3. <strong>"fallbackToDestructiveMigration 是省事神器。"</strong>它的真实含义是"版本对不上就清空用户数据"。开发期用可以，正式包里出现它等于给用户埋雷。
4. <strong>"主线程 runBlocking 等结果，代码还短点。"</strong>短的代价是整条主线程被你按住，界面冻结、系统还可能直接崩。协程那几行不是仪式，是护栏。
5. <strong>"数据存进本地数据库就万无一失了。"</strong>本地库扛不住卸载、换机、摔进水里。重要的数据要云同步，本地只是"手头有的那份"。
6. <strong>"能跑通就等于能上线。"</strong>演示环境和真实环境的差别就是网络四问：没网、超时、非 2xx、解析失败。四个都答上了，才轮得到谈上线。

这章的终点和第 54 章的起点是同一句话：界面只读 Room，网络只写 Room。带着它进下一章，那个完整的记账本会把你这几节学的每一块，串成一个真正能装的 App。

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 口诀：小配置进 DataStore，成批数据进 Room，外面的数据走 Retrofit
- DataStore 返回 Flow：值变了，观察者自动收到
- Room 三件套：@Entity（表）+ @Dao（操作）+ @Database（总装），模板可直接复用
- Retrofit 三步：定义接口 → 创建实例 → 协程里调用
- 两条铁律：网络不进主线程；正式产品必须 HTTPS
- 协程 = 不阻塞界面的等待；viewModelScope 是页面专属工作间，I/O 交给 Dispatchers.IO
- 网络四问（没网/超时/非2xx/解析失败）+ 敏感数据加密存 + 先跑通离线可用
:::
