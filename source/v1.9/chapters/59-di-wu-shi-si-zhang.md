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
欢迎来到你的第一个“正经项目”。这个记账本虽然不联网，但五脏俱全：能记一笔账、能看流水、能按月统计、能删改。做完它，你就完整走了一遍“数据 → 逻辑 → 界面”的全流程。别急着抄代码<strong>先想清楚再动手</strong>，这是咱们一贯的原则。

::: div .quick-read
##### 本章速读（5 分钟版）
这一章带你做第一个"正经项目"。一个纯本地的记账本。它不联网，但五脏俱全：能记一笔账、能看流水、能按月统计、能删改。做完它，你就完整走了一遍"数据到逻辑到界面"的全流程。它赢过应用商店里那些记账 App 的地方很实在：不开屏广告，不收你的数据，所有账目都躺在你手机的数据库文件里，关掉网络照样用。而且"不联网"还是层保护：不用碰服务器和隐私政策这些大坑，专心把"数据怎么存、界面怎么画"想透。

最关键的有两件事。一是<strong>先想清楚再动手</strong>：用"需求五要素"把想法捋一遍，What 只留四件事，记收支、看流水、按月汇总、按分类统计；多账本、云同步、拍照识别小票这些美好愿望统统先不做。第一次做项目最大的风险不是做得不够好，而是做到一半弃坑。然后把活拆成五小步：建 Room 数据层、列表页、录入页、删除与编辑、月度汇总卡片，每完成一步，手里都是一个能跑的版本。二是 MVVM 分工：View 只管画，ViewModel 管逻辑，Model 管存储；数据用 Flow、stateIn 串起来，数据一变界面自动刷新。

今天就能做的最小动作：只做第一步，建 Room 数据层，让 App 能存下一笔账。Record 实体定义字段，Dao 写增删查（月度统计交给 SQL 算），Database 全局只建一次。晚上存进一笔，列表里就多一行。顺手拿张便利贴把五步抄下来贴屏幕边上，完成一步划掉一步，"看得见的进度"，就是坚持下来的人和只收藏教程的人之间的区别。

最大的坑是眼高手低：需求还没捋清就抄代码，写到一半发现数据模型对不上；或者把界面文案和计算逻辑搅在一锅、随手写一堆魔法数字，小项目最容易养坏习惯，坏习惯练一百遍就成了本能。另一个坑是只测顺利路径：金额填 0 或负数怎么办、分类没选怎么办、数据多了卡不卡，这些边界章里的"录入弹窗打磨"和"常见 Bug 门诊"都替你排了雷。验收按三层来——功能、边界、架构，全过了才算跑通。遇到存不进去、显示不对这类问题，先翻章里的"常见 Bug 门诊"，症状、病因、处方三栏都写好了，对号入座比瞎猜快得多。
##### 速查表
- 动手前先答什么：需求五要素，What 只留四件事，其余全进愿望单
- 活怎么拆：数据层、列表页、录入页、删改、月度汇总，每步收工都是能用的 App
- 数据层三件：Record 实体、Dao 操作、Database 只建一次，统计交给 SQL
- 界面怎么自动刷新：Flow 加 stateIn 加 collectAsState，数据一变界面跟着变
- 录入怎么防呆：AlertDialog 录入，金额、分类、日期在校验那关堵严实
- 验收查什么：功能、边界、架构三层，别只走顺利路径
- 跑通之后加固：Repository 分层、一条可跑的测试、空状态设计
- 最大的敌人：想一次做全、战线拉太长，做到一半弃坑
:::

#### 一、需求思考：先问五个问题

先讲个场景。月末，你盯着银行 App 的账单发呆：这个月外卖到底点了多少单？怎么又月光了？你打开应用商店搜“记账”，下载一个评分挺高的，结果第一屏是开屏广告，第二屏让你注册手机号，第三屏弹出“开通会员解锁报表”的小窗。你只是想记个数，却像被迫签了一摞协议。那一刻你冒出的念头——“要不我自己写一个？”，就是这个项目的起点。

自己写的记账本可以丑，但在两件事上它赢过绝大多数现成产品：不开屏广告，不收你的数据。“本地版”三个字是承诺，所有账目都躺在你手机里的一个数据库文件中，关掉网络照样用；哪天卸载，文件跟着 App 一起消失，没有任何副本飘在别人的服务器上。对第一个项目来说，“不联网”还是一层保护：你不用碰服务器、账号、隐私政策这些大坑，可以专心把“数据怎么存、界面怎么画”这一件事想透。

动手之前，用“需求五要素”把想法捋清楚：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要素</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">答案</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who（给谁用）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自己用，家人朋友也行</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What（做什么）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">记收支、看流水、按月汇总、按分类统计</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why（为什么）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">练手 + 搞清楚钱花哪儿了</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How（怎么做）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin + Compose + Room + MVVM，纯本地无后端</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint（约束）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一周内完成；最低支持 Android 8；不上架也先按上架标准写</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
记账本需求五要素

这张表值得停下来多看两眼。先看 What 那一行：记收支、看流水、按月汇总、按分类统计，就这四件事，别的全算“愿望单”。多账本、云同步、拍照识别小票、预算超支提醒，先都不做。不是它们不好，是每一件都会把战线拉长。第一次做项目，最大的风险从来不是“做得不够好”。最大的风险从来是“做到一半弃坑”。

再看 Constraint 那一行：“不上架也先按上架标准写”。哪怕这 App 只有你自己用，也别随手写死一堆魔法数字，别把界面文案和计算逻辑搅在一锅里。原因很实际：小项目最容易养坏习惯，而坏习惯练一百遍就成了本能。你现在怎么写代码，将来接手大项目，多半还是怎么写。

然后拆解成“每一步都能用”的小步骤：① 建 Room 数据层（能存一笔账）；② 列表页（能看流水）；③ 录入页（能加账）；④ 删除与编辑；⑤ 月度汇总卡片。每完成一步，App 都是一个“能用的东西”。

这种拆法有个讲究：每一步收工，你手里都有一个跑得起来的版本，哪怕丑得没法看。好处藏在两处。一是心态：每晚睡前都能运行一次自己的 App，今天存进一笔，列表里就多一行，这种正反馈比“憋一整周最后联调”稳得多。二是排错范围小：第③步做完突然存不进去，问题大概率出在刚写的录入页，而不是全项目大海捞针。

顺手建议：拿一张便利贴把这五步抄下来贴在屏幕边上。完成一步划掉一步。听起来很傻，但“看得见的进度”就是坚持下来的人和只收藏教程的人之间的区别。凌晨十二点划掉第②步的那一刻，你会真切感到自己在推进一个项目，而不是在“学编程”。

最后交代一个心态问题：这个项目做完，你可能觉得“不过是个记账的，有啥了不起”。别这么想。需求分析、数据建模、状态管理、输入校验、异常兜底、验收检查，一个正经项目该走的环节，你一个都没少走。它像你跑完的第一个五公里：距离不长，但呼吸和配速的门道全摸过了。后面跑十公里，用的还是这套呼吸。

#### 动手前的准备：环境与项目骨架

如果你跟着开发篇前面几章把环境装好了，这一节五分钟就够；还没装的，先回去把 Android Studio 装上再回来。别在环境没通的情况下往下写，后面每一步的报错都会和环境问题搅在一起，你分不清哪个是代码的锅。

建项目的步骤，每一步都写上屏幕上会看到什么：

1. 打开 Android Studio，点 <strong>New Project</strong>。
2. 模板列表里选 <strong>Empty Activity</strong>——认准描述里带 Compose 字样的那个，图标和措辞随版本略有差异。
3. Name 填“我的记账本”（想练英文就叫 MyLedger），语言选 Kotlin，其余保持默认。
4. 点 Finish，等进度条走完。首次构建要下载一堆依赖，泡杯水再回来。
5. 点运行按钮，模拟器或连着的真机上出现一个空白页面：环境就算通了。

接下来补依赖。新版项目里，第三方库集中在一个 libs.versions.toml 加模块的 build.gradle.kts 里，把 Room 的运行库、注解处理（KSP 那一条）和 Compose 的 ViewModel 支持按官方文档的当前写法加进去。这里不列具体坐标和版本号，照抄半年前的版本号反而会踩坑，以官方“Room 入门”页面为准。改完点右上角 <strong>Sync Now</strong>，等它安静下来，不报红就算过了。

然后给项目分个家。在包名目录下建三个包：<code class="inline">data</code> 住实体、Dao、数据库；<code class="inline">ui</code> 住界面组件；<code class="inline">viewmodel</code> 住 ViewModel。现在只是几个空文件夹，但“每个文件该住哪”从一开始定好，后面就不纠结。分完顺手再跑一次，确认还能启动，这一步没有功能产出，纯粹给未来省心。

##### 用模拟器还是真机？

两个都行，体验各有侧重。模拟器的好处是随便造：转屏、杀进程、切系统深色模式，一条快捷键的事，练这个项目的边界情况特别顺手。真机的好处是真实：键盘手感、深色模式的实际观感、滚动卡不卡，都是模拟器给不了的。建议起步用模拟器写，收尾拿真机过一遍。真机调试要在手机的开发者选项里打开 USB 调试（入口位置视品牌而定，一般是连点系统版本号几下就会出来），数据线一连，Android Studio 的设备列表里就会出现它。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：Sync 失败别慌

{class="mt-1"}
满屏报红先别关。把报错滚到最后，找 Caused by 开头的那几行：那才是病根，上面一大片多是“被吓到的下游”。十有八九是网络：依赖下载超时，配镜像或代理后重试。剩下的情况，把那几行原文丢给搜索引擎或 AI，命中率高得惊人。
:::

#### 二、数据层：让“账”有个家

先花两分钟认识 Room，安卓官方推荐的本地数据库框架（以官方文档口径为准）。它底下是老牌的 SQLite，上面把“建表、写 SQL、把查询结果变成对象”这些脏活打了个包。打个比方：数据库文件是仓库，表是货架，Room 就是那个听得懂人话的仓库管理员——你用注解告诉他“这种叫 Record 的货放这个货架”“这个动作叫 getAll”，他就替你建货架、管进出、做盘点，你全程不用碰一句建表语句。

##### 实体：一笔账的字段设计

先定义一笔账长什么样，字段要够用但别贪多：

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

逐个字段说说为什么这么设计。<strong>id</strong> 开了 autoGenerate：存进去时不用管，数据库自动发号，它是每笔账的“身份证”，后面删除、编辑、列表定位全靠它。<strong>type</strong> 存 "income"/"expense" 两个字符串而不是布尔值 isIncome——将来想加“转账”“报销”这类第三种类型，多一个字符串值就行，布尔值就得改表结构。<strong>amount</strong> 用 Double，为什么不用更严谨的类型，下面的小贴士单独说。<strong>note</strong> 给了默认值空字符串，录入页允许偷懒不填。<strong>date</strong> 存 "2026-08-15" 这样的字符串，你可能嘀咕“日期不该用正经日期类型吗”，但字符串有个意外的便宜：按字典序比较就是按时间比较，"2026-08-15" 天然排在 "2026-09-01" 前面；SQL 里 LIKE '2026-08%' 也正好圈出整个八月。练手项目，简单就是美，等真需要按日历挑日期的那天，再换类型也不迟。

##### Dao：让 SQL 替你干活

Dao 里加两条“统计用”的查询——这是记账本的灵魂：

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

这个接口里藏着两个值得咀嚼的点。第一，getAll() 返回的是 <strong>Flow</strong> 而不是 List。Flow 是一根“持续供水的水管”：数据库每次有增删改，水管里就流出一份最新的完整数据，界面接住水管，就永远显示最新状态，不用手写“改完了记得刷新”。标了 suspend 的 insert、delete 则是“一次性动作”，干完即止。一句话：持续观察用 Flow，单次动作用 suspend。

第二，看那两条统计 SQL。COALESCE(SUM(amount), 0) 在说：“一笔账都没有时，SUM 会返回 NULL，帮我把 NULL 换成 0。”不写这个，第一次打开 App，汇总卡片上可能赫然写着“null 元”，非常尴尬。WHERE date LIKE :month || '%' 里的 || 是 SQL 的字符串拼接，"2026-08" 拼上 "%" 就等于“所有八月的日期”。很多人以为统计要写一堆循环，结果两条 SQL 完事，过滤和汇总交给数据库做，比把数据全捞进界面再循环，又快又省。

命名顺便提一句：表名 records、字段 date 这些名字是要写进 SQL 的，改起来牵一发动全身，起步就想好。小写复数表名、小写字段名是常见惯例，跟着惯例走，将来查资料时别人写的例子你都能直接对上。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：金额为什么用 Double？

{class="mt-1"}
严谨的金融 App 会用 BigDecimal 或“以分为单位的 Int”来避免浮点误差（0.1+0.2≠0.3 的老问题）。练手项目用 Double 足够；如果哪天做真金融产品，记得换成“分”为单位，这是无数前辈踩出来的坑。无论用哪种，展示层都统一格式化（比如保留两位小数），界面才像个正经记账工具。
:::

数据层写完，别急着往上盖楼，先验证通路。临时在入口界面里加一段代码：插一笔测试账，再把查询结果打到日志里，运行，看到那笔账乖乖躺在日志里，数据层就算通了。五分钟的验证，换来的是后面写界面时“我只管画，数据肯定在”的底气，很多新手界面写了一半才发现数据库根本没通，回头查半天，亏大了。

#### 数据层补完：Database 与“只建一次”

三件套还差最后一件：把实体和 Dao 攒起来的 Database 类。它自己不干活，职责就两条：向上登记“我管哪些表、版本几”，向外递 Dao。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · AppDatabase.kt（单例）</span><span class="dots">···</span>
:::

```
@Database(entities = [Record::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun recordDao(): RecordDao

    companion object {
        @Volatile
        private var INSTANCE: AppDatabase? = null

        fun get(context: Context): AppDatabase =
            INSTANCE ?: synchronized(this) {
                INSTANCE ?: Room.databaseBuilder(
                    context.applicationContext,   // 一定要用 applicationContext
                    AppDatabase::class.java,
                    "records.db"
                ).build().also { INSTANCE = it }
            }
    }
}
```
:::

几个点拆开说。<strong>version = 1</strong> 是你自己这套表结构的版本号，跟 App 版本无关。以后给 Record 加字段，必须把这个数字往上加，并告诉 Room 怎么从旧表迁到新表（迁移写法以官方文档为准）；学习期懒得写迁移，最粗暴的招是卸载重装：数据清空、表重建，所以别在练手库里存要紧账。<strong>applicationContext</strong>：数据库得活得跟整个 App 一样长，不能挂在某个界面上。界面会转屏、会重建，把 Context 传成界面自己，数据库就跟着陪葬，内存泄漏往往就是这么来的。<strong>单例</strong>：建一次数据库连接不便宜，开十个实例除了拖慢没有任何好处。那段 synchronized 加双重判断，看不懂没关系，记住注释那句话“保证全 App 只建一个实例”就行，这是多少年沉淀下来的标准单例写法，抄就完了。

到这里，数据层三件套凑齐：Record 定义“存什么”，RecordDao 定义“怎么存怎么取”，AppDatabase 把它们焊在一起。下一节要解决一个接头问题：界面怎么安全地拿到这个 dao？把 Context 一路传进界面、现场建数据库？能跑，但每一层都被污染了。这就轮到架构出场。

#### 三、MVVM：界面与逻辑“分家”

先看个反面教材。有人把第一版记账本写成了一个文件：点“记一笔”的回调里直接开数据库、拼语句、刷新列表，两百行全挤在一个 Composable 里。头两天好好的，第三天屏幕一转，列表没了；第五天想加“撤销删除”，发现逻辑跟界面缠成一团，无从下手。这不是他菜，所有不分家的项目，最后都长成这样。

直接让界面操作数据库？能跑，但界面代码会又臭又长。MVVM 架构让各司其职：<strong>View（界面）只管画，ViewModel（逻辑中枢）管数据，Model（Room）管存储</strong>。

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View（Compose 界面）</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel（状态与逻辑）</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model（Room 数据层）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
图 5：MVVM 三层结构——数据单向流动，各层互不越界
:::

分家的本质是“谁活得长，谁就管数据”。界面像餐厅服务员，客人一走（转屏、退出）就换人；ViewModel 像后厨，不管前台换了几轮，锅里的菜还在。数据放后厨，前台只负责端——这就是转屏不丢数据的全部秘密，不需要你写任何“保存现场”的代码。

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

逐行拆一下这段骨架。records 这行，把 Dao 的 Flow“焊”成界面能直接观察的 StateFlow：viewModelScope 是 ViewModel 自带的协程作用域，ViewModel 没了它就跟着取消，不会留下孤儿协程；SharingStarted.WhileSubscribed 的意思是“有界面在看才供水，没人看就关闸”，省电省心；emptyList() 是初始值，数据还没到时，界面先拿到一个空列表，而不是一个会崩的 null。addRecord 和 deleteRecord 把 suspend 函数包进 viewModelScope.launch，再以普通方法的样子递给界面，界面从此不用知道协程的存在。

界面（Compose）里这样用：<code class="inline">val vm: RecordViewModel = viewModel()</code>，然后 <code class="inline">val list by vm.records.collectAsState()</code>——数据一变，列表自动刷新，你什么都不用做。这就是 MVVM + Flow + Compose 三剑合璧的威力。

顺带回应一个高频疑问：collectAsState 和 collectAsStateWithLifecycle 的区别？后者是官方更推荐的写法：屏幕退到后台时暂停收集，回来再续上，省掉无谓的刷新。起步阶段用哪个都能跑。知道有这回事就行（以官方文档的当前建议为准）。另外提一句：上面骨架里 dao 是构造参数，用默认的 viewModel() 取这种带参 ViewModel 需要配一个 Factory，写法见官方文档，稍微绕；起步更省事的姿势是让 ViewModel 继承 AndroidViewModel，下一节给代码。

还有一条纪律：ViewModel 里不写界面的事。别在 ViewModel 里存“某个按钮是什么颜色”，也别让它弹提示条，它只管数据和状态，长什么样、怎么提示，都是界面自己的事。反过来，界面里也别出现一句 SQL、一个日期计算。这条线画直了，你会发现每个文件都短得能一眼读完，改哪里一目了然。

#### ViewModel 与 UI 状态：把数据流讲透

分工说完了，这一节把“数据到底怎么流动”画成一张行车路线图。整个 App 里，数据永远沿着一个方向转圈：<strong>界面发事件（你点了“记一笔”）、ViewModel 接单（校验、组对象）、Dao 落库（Room 写进 SQLite）、Flow 吐出新数据、界面自动重画</strong>。界面从不亲自碰数据库，ViewModel 也从不伸手抓某个按钮改文字：它们只靠“状态”单向沟通。

为什么这么执着于单向？因为双向纠缠的项目，出了 bug 就像在两栋楼之间找一根接错的电线。单向流动里，任何一次界面错乱都能顺着箭头倒着查：界面画错？看状态。状态错了？看 ViewModel。库里错了？看 Dao。三段式排查，每段都不长。

落到代码上，起步版 ViewModel 长这样：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordViewModel.kt（AndroidViewModel 起步版）</span><span class="dots">···</span>
:::

```
class RecordViewModel(app: Application) : AndroidViewModel(app) {

    private val dao = AppDatabase.get(app).recordDao()

    // 界面持续观察的状态
    val records = dao.getAll()
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(), emptyList())

    fun addRecord(type: String, amount: Double, category: String, note: String, date: String) {
        viewModelScope.launch { dao.insert(Record(type, amount, category, note, date)) }
    }
}
```
:::

AndroidViewModel 是“需要一个 Application 上下文的 ViewModel”的现成答案：系统自动把 Application 塞进构造函数，不用你写 Factory。app 这个参数就是它给的，拿去建数据库正合适，它本质上是全局的上下文，生命周期跟 App 进程一样长，最安全。

界面再长一点后，还有一招叫“状态聚合”：把一个页面要用的所有状态装进一个 data class，ViewModel 只暴露这一个对象。状态多了以后（流水列表、当前月份、弹窗开关……），这样管理比东一个西一个清爽得多，也方便一口气做校验：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordUiState.kt</span><span class="dots">···</span>
:::

```
data class RecordUiState(
    val monthRecords: List&lt;Record&gt; = emptyList(),
    val month: String = LocalDate.now().toString().take(7),  // "2026-08"
    val showAddDialog: Boolean = false
)
```
:::

分界线记牢一条：<strong>remember 只存“画的辅助状态”</strong>（比如某个菜单开没开），<strong>业务数据一律进 ViewModel</strong>。判断标准就一句：这个东西没了，用户会心疼吗？菜单开关丢了无所谓，记了一半的账丢了要骂人——所以后者必须放 ViewModel。转屏演练一下立刻见分晓：随便输点什么，转个屏，在 ViewModel 里的都在，在 remember 里的全没了。

#### 四、界面：列表页 + 录入页

数据层和逻辑层都通了，现在把脸面装上。先解释一个词：懒加载。普通 Column 会一口气把列表里每一行都画出来，三千笔账就老老实实组合三千个组件，滚动时能卡成幻灯片。LazyColumn 只画屏幕里的十几行，滚到哪画到哪，滑出屏幕的行回收复用。做列表请默认用它，这是“安全牌”。

列表页用 <strong>LazyColumn</strong>（懒加载列表），数据再多也不卡：

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

        // 悬浮“记一笔”按钮 → 弹录入对话框
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

这段代码里有一处新手最容易抄丢：<code class="inline">items(records, key = { it.id })</code> 里那个 <strong>key</strong>。它告诉 Compose“每行用 id 认人，不按位置认人”。不写 key，列表头部插入新账时，Compose 可能把“原来的第 3 行”误认成“现在的第 3 行”，画面就串了；各种“列表灵异刷新”问题，一多半是这个原因。记住：有唯一 id 就一定给 key。这里先埋个伏笔，本章后面的“Bug 门诊”还会回来找它。

RecordRow 的排版也有讲究：Row 里放 <code class="inline">Spacer(Modifier.weight(1f))</code>，是安卓布局里“两端对齐”最常用的三件套——左边分类正常排，Spacer 占掉所有剩余宽度，金额自然被推到最右边。收入绿色带加号，支出红色带减号，颜色语义不用记，眼睛一扫流水就能对上号：好的视觉设计就是不用思考。

录入用 <strong>AlertDialog</strong>（对话框）最省事：几个输入框 + 收入/支出切换 + 分类下拉，点确定就调 <code class="inline">vm.addRecord(...)</code>。

控件选型说一下。输入框用 OutlinedTextField（组件名随 Material 版本可能略有出入，以官方组件库为准），带描边的样式比细线框醒目，错误提示也自带位置。收入/支出切换，最省事的是两个“分段选择”式的芯片肩并肩；分类先用一列写死的字符串（餐饮、交通、购物、娱乐、其他）做下拉——第一版够用，可配置分类在扩展练习里等着你。日期第一版不让用户改，默认记今天，代码里 <code class="inline">LocalDate.now().toString()</code> 拿到的正好是我们要的 "2026-08-15" 格式。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · AddRecordDialog.kt（骨架）</span><span class="dots">···</span>
:::

```
@Composable
fun AddRecordDialog(vm: RecordViewModel, onDismiss: () -&gt; Unit) {
    var type by remember { mutableStateOf("expense") }
    var amountText by remember { mutableStateOf("") }
    var category by remember { mutableStateOf("餐饮") }
    var note by remember { mutableStateOf("") }

    AlertDialog(
        onDismissRequest = onDismiss,
        title = { Text("记一笔") },
        text = {
            Column {
                Row { /* 两个“收入 / 支出”切换芯片，点谁 type 变成谁的值 */ }
                OutlinedTextField(value = amountText, onValueChange = { amountText = it },
                                  label = { Text("金额") })
                Row { /* 分类下拉：餐饮、交通、购物、娱乐、其他 */ }
                OutlinedTextField(value = note, onValueChange = { note = it },
                                  label = { Text("备注（可不填）") })
            }
        },
        confirmButton = {
            TextButton(onClick = {
                val amount = amountText.trim().toDoubleOrNull() ?: return@TextButton
                vm.addRecord(type, amount, category, note.trim(), LocalDate.now().toString())
                onDismiss()
            }) { Text("确定") }
        },
        dismissButton = { TextButton(onClick = onDismiss) { Text("取消") } }
    )
}
```
:::

注意确定按钮里那个 <code class="inline">?: return@TextButton</code>：输入不是合法数字时，函数直接退出，什么都不发生，这是第一道闸，粗暴但有效。更友好的做法是让它把输入框点亮成红色并给一句提示。怎么做得体面，本章后面的“录入弹窗打磨”专门讲。弹窗里所有输入状态都放在 remember 里，别慌：弹窗是“活的几秒钟”的界面，输到一半被系统杀掉的概率极低；要升级成转屏也不丢的版本，把这些状态搬进 ViewModel 就行，骨架不变。

布局骨架也提前定好：整个页面一个 Column，从上到下是“月份与汇总卡片 → 流水列表 → 底部留白”，右下角悬浮一个 FloatingActionButton 顶着“记一笔”。列表的 LazyColumn 记得给 <code class="inline">Modifier.weight(1f)</code>，让它占满中间所有剩余空间，漏了这一条，列表矮矮一截、下面空一大块，是新手页面最常见的“歪”。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>注意：输入校验别偷懒

{class="mt-1"}
金额输入框一定要校验：空值、负数、"abc"这类非法输入都要拦住（用 <code class="inline">toDoubleOrNull()</code> 判断）。App 崩掉最常见的原因之一就是“把用户的输入当成了乖孩子”。记住：<strong>用户输入的一切，都要当敌人审查</strong>。
:::

#### 录入弹窗的打磨：把校验和边界堵严实

上一节末尾的避坑提醒说了“用户输入的一切，都要当敌人审查”。这一节就把审查落到实处。把校验单独写成一个函数，别散在按钮回调里，它能被复用，还能被单独测试：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · InputValidate.kt（校验函数）</span><span class="dots">···</span>
:::

```
// 返回 null 表示合法，否则返回错误提示文案
fun validateAmount(input: String): String? {
    val text = input.trim()
    if (text.isEmpty()) return "金额不能为空"
    val value = text.toDoubleOrNull() ?: return "金额得是数字，比如 12.5"
    if (value &lt;= 0) return "金额要大于 0"
    if (value &gt; 99_999_999) return "金额太大了，检查一下是不是多按了个零"
    return null
}
```
:::

四道关卡各管一件事。<strong>空输入</strong>：用户点了确定却什么都没输，或者只敲了一串空格——trim() 先把首尾空白剥掉再判断。<strong>非数字</strong>："abc"、“一二三”、混进全角字符的"１２３"，toDoubleOrNull() 一律给出 null，正好拦下。<strong>非正数</strong>：记账没有“负的支出”这一说，想记一笔退款，请记成收入；0 元也没有意义。<strong>超大金额</strong>：Double 装得下天文数字，但把工资输成小数点错位的天文数字毫无意义，还会把汇总卡片挤变形。给个上限，超了就提示“是不是多按了个零”，比默默存进去友好得多。上限具体取多少看你的使用场景，思路是“比你会出现的最大数字再大一点”。

小数也要有个说法：用户输 12.345 怎么办？保存前统一四舍五入到两位，显示时统一格式化，全 App 只认一个标准。别有的地方显示 12.5、有的地方显示 12.50——这种不一致说不清哪里错，但用户就是会觉得“这 App 不靠谱”。

错误提示放哪？放输入框正下方，OutlinedTextField 的错误状态自带位置，把 validateAmount 的返回值塞进去就行。错误发生在哪，提示就出现在哪，视线不用跳。别用弹窗套弹窗：校验失败又弹一个“输入不合法”，用户会把手机扔了。

校验的时机也有讲究。实时校验（每敲一个字符就查）太吵，输到一半满屏红；只在点确定时查又太迟。常见折中是“失焦时查 + 提交时再查一遍”：输入框失去焦点就给提示，点确定时最后把关。两种都行，选一种做到底，别混着来。

重复提交是第二个坑。手快的用户会连点两下“确定”，账就记重了。两个动作就能堵住：点下确定先置个“正在保存”标记，按钮立刻禁用，保存成功马上关弹窗，让“再点一次”从物理上不可能。保存动作在协程里跑得很快，但“快”不等于“瞬间”，防的就是这个瞬间。顺手也检查一下 FAB：弹窗用 showAddDialog 这一个状态控制，天然不会叠出两个弹窗。

还有个不起眼的细节：键盘。弹窗在屏幕下半截，键盘一弹起来正好挡住输入框。给根布局加 imePadding()（组件名以官方文档为准，作用是“给键盘让出高度”），输入框就能始终露在键盘上方。这种细节用户说不出哪里好，但少了就是觉得“硌得慌”。

日期先不开放修改，第一版一律记今天，什么时候记什么时候按。想改日期的需求写进愿望单，等基础版稳定了再说。这条克制在多人协作里有个学名，叫“控制需求范围”，一个人的项目里它叫“别跟自己过不去”。

#### 五、编辑与删除：让数据“能进能出”

先说一个真实瞬间：你手一滑，把昨天记的 200 块饭钱删了，找遍 App 没有撤销按钮，本地数据库又不会进回收站。从这一刻起你就懂了，为什么“能删”和“敢删”是两回事，交互设计要替手滑负责。

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

// 界面上：长按列表项弹“编辑/删除”菜单（Compose 用 DropdownMenu 或 AlertDialog）
// 删除前最好弹确认框——“误删”是记账类 App 用户最痛恨的事
```
:::

界面上的具体做法：长按列表项弹菜单，点条目直接进编辑。给一个能抄的最小骨架：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordRow.kt（长按菜单与删除确认）</span><span class="dots">···</span>
:::

```
// 列表项：长按弹菜单（combinedClickable 是实验性 API，按编译器提示加 @OptIn）
@Composable
fun RecordRow(record: Record, onEdit: (Record) -&gt; Unit, onDelete: (Record) -&gt; Unit) {
    var menuOpen by remember { mutableStateOf(false) }
    Box(Modifier.combinedClickable(onLongClick = { menuOpen = true },
                                   onClick = { onEdit(record) })) {
        Row(Modifier.fillMaxWidth().padding(12.dp)) { /* 原有那行布局照旧 */ }
        DropdownMenu(expanded = menuOpen, onDismissRequest = { menuOpen = false }) {
            DropdownMenuItem(text = { Text("编辑") }, onClick = { onEdit(record); menuOpen = false })
            DropdownMenuItem(text = { Text("删除") }, onClick = { onDelete(record); menuOpen = false })
        }
    }
}

// 删除前确认：pendingDelete 不为 null 时弹框
if (pendingDelete != null) {
    AlertDialog(
        onDismissRequest = { pendingDelete = null },
        title = { Text("删除这笔账？") },
        text = { Text("删了就找不回来了。") },
        confirmButton = {
            TextButton(onClick = { pendingDelete?.let(vm::deleteRecord); pendingDelete = null }) {
                Text("删除", color = MaterialTheme.colorScheme.error)
            }
        },
        dismissButton = { TextButton(onClick = { pendingDelete = null }) { Text("手滑了") } }
    )
}
```
:::

编辑预填的实现在弹窗那一侧：点开编辑时，把这条记录的原值塞进输入框初始状态。这里有个极易翻车的细节，输入框状态要跟记录 id 绑定（初始化用 <code class="inline">remember(record.id)</code> 这类写法），否则你从 A 行切到 B 行，弹窗里还留着 A 的数字，一保存就把 B 改成了 A 的样子，数据被无声地改错。改完点确定，调 Dao 的 update，Flow 一抖，列表自动变——注意看，这几行代码里没有一句“刷新列表”，MVVM 的省力之处全在这了。

交互细节两条经验：<strong>删除必须二次确认</strong>（防止手滑），编辑尽量<strong>预填原值</strong>（改一个字比重新输入省事）。别小看这两个细节，产品感就是这些细节堆出来的。

想再进一步，可以学成熟记账 App 做“删除后撤销”：点删除先不真删，提示条里挂一个“撤销”按钮，几秒内可反悔，超时再真删。或者走“软删除”路线：记录加个 isDeleted 字段，删除只是把它标记成真，列表查询把它过滤掉——想找回随时能找回。本地版没有回收站，这两种宽容设计就是用户的后悔药，实现都在二十行上下。

#### 月度统计的实现：把“钱花哪儿了”算清楚

流水是一笔一笔的散账，统计负责把它们捏成结论。先想清楚要展示什么：本月收入合计、本月支出合计、结余（收入减支出），以及一张能切换月份的流水。目标定了，实现有两条路，都不丢人。

##### 路线一：内存过滤（起步推荐）

全量流水本来就在 ViewModel 里，按月过滤只是一个 filter：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · MonthFilter.kt（ViewModel 里的月筛选）</span><span class="dots">···</span>
:::

```
// 当前选中的月份，形如 "2026-08"
private val _month = MutableStateFlow(LocalDate.now().toString().take(7))
val month: StateFlow&lt;String&gt; = _month.asStateFlow()

// 当前月份的流水：记录或月份任一变化，就重新算一遍
val monthRecords = combine(records, month) { list, m -&gt;
    list.filter { it.date.startsWith(m) }
}.stateIn(viewModelScope, SharingStarted.WhileSubscribed(), emptyList())

fun switchMonth(m: String) { _month.value = m }
```
:::

combine 的意思是“两条水管任何一条来水，就重新算一遍”：记录变了重算，月份变了也重算。算完照样 stateIn 成一根新水管递给界面。记几百条账以内，这点计算量手机闭着眼都跑得动：先把功能做出来，别为了想象的“性能”提前绕路。

##### 路线二：让数据库算

数据量大了（比如记了好几年），或者要做按分类汇总这种复杂统计，就把活儿交给 SQL，Dao 里早有现成的 monthIncome/monthExpense（suspend，一次取一个数），也可以补一条按月取流水的查询。两条路线的分工记一句话：<strong>界面持续看的数据走 Flow，按一下算一次的数字走 suspend</strong>。这个项目建议两条都写一遍，体会差别，这正是 Dao 里那两条统计 SQL 存在的意义。

##### 汇总卡片与月份切换

界面侧，把过滤结果交给 remember 缓存着算：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · MonthSummary.kt（卡片与月份切换）</span><span class="dots">···</span>
:::

```
val monthList by vm.monthRecords.collectAsState()
val month by vm.month.collectAsState()

val income  = remember(monthList) { monthList.filter { it.type == "income"  }.sumOf { it.amount } }
val expense = remember(monthList) { monthList.filter { it.type == "expense" }.sumOf { it.amount } }
val balance = income - expense

// 卡片：本月收入 / 本月支出 / 结余 三列；结余为负时换个警示色
// 卡片下面一排月份 Chip：
Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
    recentMonths().forEach { m -&gt;
        FilterChip(selected = m == month,
                   onClick = { vm.switchMonth(m) },
                   label = { Text(m) })
    }
}
```
:::

remember(monthList) 的意思是“列表没变就不重算”，界面重组再频繁也不心疼。卡片本体用一个 Card 装三列数字；月份切换用一排 FilterChip，点一下换月。“最近几个月”这个列表用 LocalDate 的日期运算往前推着生成，别手写“2026-01、2026-02”，写死的东西迟早变成 bug。

边界情况过一遍：某个月一笔账都没有，卡片显示 0.00，列表给一句“本月还没有记录”，别留白；半夜十二点前后记的账落哪天，跟随设备本地时间（LocalDate.now() 的口径），不用你操心；切到过去的月份再切回来。状态从 combine 里自动回来，也不用你操心。统计这块想不健壮都难，因为重活都让 Flow 和数据库干了。

#### 深色模式与细节打磨

现在的手机一到晚上自动切深色，你的 App 要是还顶着一块大白底，用户在被窝里点开就是一次闪光弹。好消息是，Compose 主题里深色模式几乎是白送的——前提是你别把颜色写死。

看一眼之前的代码：<code class="inline">Color(0xFF27AE60)</code> 这种写死的具体色值，白天是清爽的绿，深夜大黑底上就刺眼。正确姿势是用<strong>语义色</strong>：MaterialTheme.colorScheme 里的 primary、onSurface、error 这些名字描述的是“用途”而不是“颜色值”，主题会根据当前深浅模式自动给它们换装。业务色（收入绿、支出红）语义色里没有，那就自己成对定义：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · ThemeColor.kt（业务色）</span><span class="dots">···</span>
:::

```
@Composable
fun rememberBizColors(): Pair&lt;Color, Color&gt; {
    val dark = isSystemInDarkTheme()
    return if (dark) Color(0xFF7BD3A2) to Color(0xFFE58A8A)   // 深色：更亮、更柔
           else Color(0xFF1E8E5A) to Color(0xFFC0392B)        // 浅色
}
```
:::

选色原则一句话：深色模式里把颜色调亮一档、饱和度降一点。深底上的纯绿纯红都太“跳”，柔和的亮色才睡得着觉。具体色值你自己挑，挑完在深浅两种模式里各看一眼，很多颜色单看不错，放进另一个模式就脏了。

除了颜色，还有一串小细节值得花半小时过一遍：

- <strong>金额格式统一</strong>：全 App 只留一个格式化函数，保留两位小数，别有的地方 12.5、有的地方 12.50。
- <strong>间距成体系</strong>：内边距统一用 4dp 的倍数（12dp、16dp……），界面立刻显“齐”。
- <strong>触控目标别抠门</strong>：删除按钮做得再小，也要留出官方建议的最小触控尺寸（以官方规范为准），地铁上单手操作的人会感谢你。
- <strong>空状态设计</strong>：第一次打开一条账都没有，给一句“记下第一笔，看看钱都去哪儿了”加大按钮，别给一片空白。
- <strong>当前月份抬头</strong>：列表顶部常驻显示正在看哪个月，切月份时用户不会迷路。

字号也别一路加粗放大：页面标题、卡片数字、列表正文、辅助说明，拉开两三档就够，字号层级少而分明，比处处强调更显专业。打磨没有尽头，做到“自己愿意天天用”这一档，就可以停了。

打磨还要克制。清单上的事别一口气全做：挑最碍眼的三件先修，修完看一眼整体，再决定下一件。判断该不该停的标准很简单。连续五分钟里，你说不出一个用户能感知到的差别，就收手。界面微调是新手最容易掉进去的“温柔陷阱”，它永远有得调，但你的时间该花在下一章的新鲜事上。

顺手的小升级：在流水列表里按天分组，每天开头插一行“8 月 15 日 · 支出 86.50”的日期头。实现不复杂：把当月流水按 date 的前十位分组，每组前面放一个标题行。列表立刻从“一堆数字”变成“一本日记”，这是投入产出比最高的一个界面改动，十分钟就能加上。

#### 数据多了以后：性能的第一次照面

几百条账的时候，这个 App 怎么跑怎么快，性能这个词还用不上。但记账本的特点是只增不减：一年下来几千条，两年上万条，当初随手写的代码就会开始露出吃力相。提前把三个点踩对，你几乎永远不用回头返工。

第一个点是索引。date 是查询和排序都要摸的高频字段，给它建个索引，相当于给一本书加了目录：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Record.kt（加索引）</span><span class="dots">···</span>
:::

```
@Entity(tableName = "records", indices = [Index("date")])
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val type: String,
    val amount: Double,
    val category: String,
    val note: String = "",
    val date: String
)
```
:::

字段一个没变，只多了一个注解，查询计划却从“翻全书”变成“查目录”。这里也藏着一个前面埋好的伏笔：月份筛选用的是 LIKE '2026-08%' 这种前缀匹配，前缀匹配能用上索引，而两边都带百分号的模糊匹配用不上。当初“date 存成日期字符串”的设计，在这里连本带利地还了回来。

第二个点是让数据库干数据库的活。数据一多，“把全表捞进内存再过滤”的路子就开始浪费电、浪费内存，这时路线二（SQL 统计）就成了正解。两条路线不是二选一。两条路线是随数据量升级：小的时候怎么写都快，大的时候把统计下沉到 SQL，界面代码一行不用改，因为 ViewModel 暴露的还是同一根水管。

第三个点是别在主线程碰数据库，Room 默认禁止主线程访问——这不是刁难，是保护：主线程一卡，用户看到的就是“应用无响应”。挂起函数和 Flow 默认把活儿挪到合适的线程，前面所有代码已经天然做对了。你只要记住一条纪律：看到“cannot access database on the main thread”的报错，别去找绕过它的歪招，去找哪一步漏了协程。

至于分页（数据多到列表都装不下时只取一屏），官方有现成方案，以官方文档为准；本地记账本通常一辈子用不上，知道有这回事就行。性能优化的顺序永远是：先量出来慢，再动手改——凭感觉优化，十次有九次是在给不慢的代码做手术。

#### 常见 Bug 门诊：症状、病因与处方

下面这几位“病人”，几乎每个做过这个项目的人都见过。按“症状 → 病因 → 处方”排列，对号入座：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">症状</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">多半的病因</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">处方</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">加了一笔，列表纹丝不动</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">界面拿的不是 collectAsState 出来的状态（比如自己另存了一个 List）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数据从 Dao 的 Flow 出发，界面用 collectAsState 接</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">删除删错行、行内容串位</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">items 没给 key，或拿列表下标当 key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">key = { it.id }，永远用业务 id</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">转屏后输入到一半的内容没了</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">输入状态放在 remember 里，跟着界面一起重建</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">业务输入进 ViewModel；纯界面状态用 rememberSaveable</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">改了 Record 字段，一启动就闪退</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">表结构变了，version 没升或没写迁移</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">学习期卸载重装；正经做法是升 version 加迁移（以官方文档为准）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">满屏 Unresolved reference: Entity</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room 依赖或 KSP 注解处理没配好</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">回官方“Room 入门”页面对照依赖清单，Sync 后 Clean 再构建</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">调 insert 报“只能在协程里调用 suspend”</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">在协程外直接调了 suspend 函数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">包进 viewModelScope.launch</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">金额显示 0.30000000000000004</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double 直接 toString 上屏</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全 App 统一走格式化函数，保留两位小数</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">键盘弹起来正好挡住输入框</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">没给键盘让位</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">根布局加 imePadding()（组件名以官方文档为准）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">汇总卡片显示“null 元”</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">统计 SQL 没兜住空结果</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">COALESCE(SUM(amount), 0)，空月返回 0</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">模拟器正常，真机崩溃（或反过来）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系统版本差异触发的兼容问题</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">看清崩溃行，相关 API 的兼容写法以官方文档为准；日常两个环境都跑</td></tr></tbody></table>
```
:::

门诊看多了你会发现规律：十次里有七八次，不是什么“高科技难题”，是数据流的某个环节没接对：状态没走 Flow、key 没给、协程没开。所以排错别上来就怀疑人生，先顺着“事件、ViewModel、Dao、Flow、界面”这条线摸一遍，断点多半就躺在箭头中间。

再给一套通用排查三步：<strong>读全报错</strong>——别只看第一行，滚到最后找 Caused by，那才是根因；<strong>最小复现</strong>——把出问题的场景缩到三步以内。“我一点编辑就崩”比“有时候会崩”好查十倍；<strong>二分定位</strong>——拿不准哪段出的问题，注释掉一半再看，两三轮就能锁定。这套功夫在第七篇还会反复练。

门诊的最后，送一个把报错变成营养的小习惯：每修好一个 bug，花一分钟把“症状、原因、修法”记进项目里的一个文本文件。别小看这本流水账，一个月后它是你私人的“坑典”，面试前翻一遍，比任何背下来的答案都好使。写教程的人，也是这么攒素材的。

#### 新人误区清单：这五个想法，趁早放下

这个项目不大，但踩的坑和做大项目是同一种坑。五个流传最广的想法，趁早放下：

- <strong>很多人以为“功能越多越像真产品”，其实真产品的标准是核心流程顺滑。</strong>记账 App 从打开到记完一笔，三步以内是及格线，多一步都嫌多。堆功能谁都会，做减法才是本事。
- <strong>很多人以为“架构是大项目才需要的东西”，其实架构的成本随规模涨得比规模本身快。</strong>两百行时不分家，涨到五倍大时还债的利息翻好几倍。你现在多写的那几层接口，是将来最便宜的投资。
- <strong>很多人以为“代码能跑就行，回头再重构”，其实“回头”在个人项目里永远不会来。</strong>能跑和能维护是两码事，而负责维护的那个人，三个月后是你自己。
- <strong>很多人以为“抄教程代码不算真本事”，其实会抄、会改、会排错，就是初级工程师的日常。</strong>新手和熟手的区别只有一条：熟手抄完能讲清楚每一行为什么在那。
- <strong>很多人以为“AI 都能写了，学这个没用”，其实 AI 写得越快，判断对错的能力越值钱。</strong>字段怎么设计、校验放哪、状态归谁管：这个项目练的每一步都是判断力，这是 AI 替不了的。

#### 六、验收：三层检查 + 两个进阶挑战

项目做完，按“功能 → 边界 → 架构”三层验收：能不能记、能不能删、重开 App 数据还在不在（功能）；金额输 0 或负数会不会崩、转屏会不会丢数据（边界）；界面和数据有没有混在一起、字段有没有硬编码（架构）。

基础版验收通过后，给自己加两道“进阶菜”：

1. <strong>月度筛选</strong>：顶部加月份切换（比如 2026-08 ▾），列表只显示当月流水。
2. <strong>分类饼图</strong>：用 Compose 的 Canvas 或引入轻量图表库，把“钱花哪儿了”画成饼图：做完这个，记账本就有点“产品样”了。

三条检查展开成动作。功能层，就按一个真实用户的方式点：记三笔、删一笔、改一笔、把 App 从后台划掉再打开，数据还在，就过了最要紧的一关。边界层专门“欺负”App：金额输 0、输负数、输一长串 9、输"abc"，弹窗开着转个屏，确定键连点十下。架构层不用看代码，做个思想实验：假如把界面全删了重写一版，ViewModel 和数据层要不要动？一个字都不用改，就过关了。月度筛选这道进阶菜，前文“月度统计”已经给了完整思路；饼图在扩展练习里等着。

#### 扩展练习：分类统计、导出 CSV 与图表入门

基础版跑稳了，从愿望单里挑三件“性价比最高”的，一步一步做。每件都给思路和关键代码，细节留给你折腾：折腾才是练手的本体。

##### 练习零：把写死的分类变成可配置

动手加新功能之前，先拆一处“违章建筑”：分类现在是一列写死在界面里的字符串。把它变成数据，最省事的存法是加一张 categories 表，录入页的下拉改成从数据库读；嫌重的存成一个本地文件也行，思路对就好。这个练习规模最小，却最能练出“界面里不留死数据”的手感，做完它，后面三个练习都会顺很多。

##### 练习一：分类统计

“这个月餐饮花了多少？”一句 GROUP BY 的事。Dao 里加：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · CategoryStats.kt（分类统计）</span><span class="dots">···</span>
:::

```
data class CategoryTotal(val category: String, val total: Double)

@Query("SELECT category, SUM(amount) AS total FROM records " +
       "WHERE type='expense' AND date LIKE :month || '%' " +
       "GROUP BY category ORDER BY total DESC")
suspend fun categoryTotals(month: String): List&lt;CategoryTotal&gt;
```
:::

GROUP BY category 把同分类的账归堆，SUM 求和，ORDER BY 排出“花钱大户”。注意这里返回一次性结果（suspend），因为分类页是“点开看一眼”的场景，不需要持续盯着。展示成横向条形图最简单：每行左边分类名，中间按占比变宽的色块，右边金额：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 分类条形（核心片段）</span><span class="dots">···</span>
:::

```
val maxTotal = totals.maxOfOrNull { it.total } ?: return
totals.forEach { t -&gt;
    Row(verticalAlignment = Alignment.CenterVertically) {
        Text(t.category, Modifier.width(56.dp))
        Box(
            Modifier
                .fillMaxWidth(t.total / maxTotal)   // 占比决定宽度
                .height(16.dp)
                .background(incomeColor, RoundedCornerShape(4.dp))
        )
        Spacer(Modifier.width(8.dp))
        Text(formatMoney(t.total))
    }
}
```
:::

fillMaxWidth(fraction) 接受 0 到 1 的小数，正好拿来画占比。不需要任何图表库，二十行以内的代码，效果已经很像模像样。

##### 练习二：导出 CSV

把流水导成 CSV，用表格软件打开做进一步分析。核心是把每笔账拼成一行逗号分隔的文本：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · CsvExport.kt（导出 CSV）</span><span class="dots">···</span>
:::

```
fun exportCsv(records: List&lt;Record&gt;): String = buildString {
    appendLine("type,amount,category,note,date")
    records.forEach { r -&gt;
        appendLine(
            listOf(
                r.type,
                formatMoney(r.amount),
                escapeCsv(r.category),
                escapeCsv(r.note),
                r.date
            ).joinToString(",")
        )
    }
}

// CSV 约定：字符串字段用引号包住，内部引号翻倍转义
fun escapeCsv(s: String): String = "\"${s.replace("\"", "\"\"")}\""
```
:::

有个细节别省：备注里如果带逗号或引号，会破坏 CSV 的列结构，所以字符串字段要用引号包住、内部引号翻倍，这是 CSV 的通用约定。想用表格软件顺利打开中文，编码怎么选、要不要加 BOM，拿你常用的软件试一下就知道（以实际软件为准）。文件往哪存？写进 App 专属目录，再用系统的分享面板发给自己，这条路不用申请任何存储权限，是新手最省心的姿势；公共目录规矩多，以官方存储文档为准，别硬闯。

##### 练习三：饼图入门

“钱花哪儿了”的终极答案是一张饼图。Compose 里用 Canvas 画圆弧，每个分类占的角度等于份额乘 360 度：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · PieChart.kt（Canvas 饼图）</span><span class="dots">···</span>
:::

```
@Composable
fun CategoryPie(totals: List&lt;CategoryTotal&gt;, colorFor: (String) -&gt; Color) {
    val grand = totals.sumOf { it.total }.takeIf { it &gt; 0 } ?: return
    Canvas(Modifier.size(160.dp)) {
        var start = -90f                       // 从正上方开始扫
        totals.forEach { t -&gt;
            val sweep = (t.total / grand * 360.0).toFloat()
            drawArc(
                color = colorFor(t.category),
                startAngle = start,
                sweepAngle = sweep,
                useCenter = true
            )
            start += sweep
        }
    }
}
```
:::

每个分类配一个稳定不变的颜色（同一个分类永远同色，不然每次刷新换色，用户会晕），图例就纯是排版功夫了。想加动画，让扫过的角度从 0 涨到目标值，一行代码的事，效果翻倍（具体 API 名以官方文档为准）。图表库当然存在，功能也全；但第一次建议自己画：就这几十行，画完你对“图表就是数学加画笔”的理解会上一个台阶。

#### 对照 iOS 篇第 65 章：同一个项目，两条路线

如果你手头也有 iOS 篇，翻到第 65 章，那边同样在做一个记账本项目。需求一模一样，拆步骤的思路一模一样，分层的思想一模一样，差别只在“口音”。把两边的零件并排放：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">这边（安卓）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">那边（iOS，以第 65 章口径为准）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">背后同一件事</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">静态类型语言，空安全思想相通</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Compose 界面</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI 界面</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">声明式 UI：状态变，界面自动变</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room（实体 + Dao）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">iOS 侧的本地持久化方案（以该章所用为准）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">结构化数据存本地</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ViewModel + StateFlow</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">iOS 侧的可观察状态对象</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">状态住在界面外面，界面只读状态</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle 管依赖</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode 工程体系</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">依赖交给工具管，别手工搬文件</td></tr></tbody></table>
```
:::

这张表里最有价值的其实是第三列：减掉平台名词，剩下的全是可迁移的通用功夫，数据建模、状态管理、输入校验、分层思想。这些学会了，换哪门语言、哪个框架都作数；平台名词只是给功夫套的一件衣服。

两边都做一遍这个项目，收获比做两个不同项目大得多。你会亲手体会到：声明式 UI 的思路（描述“界面在某状态下长什么样”，刷新交给框架）在两大平台是同一句话；真正的平台差异集中在生命周期、权限、构建这些“边角”上。有了这套跨平台视角，你看技术选型的争论也会平和很多——多数争论，争的只是衣服的颜色。

常有人问：先学哪边？我的建议是手头有什么设备就用什么。两边的概念可以互相翻译，读完这章再看第 65 章，你会一路“哦哦哦”地读过去：哦，这就是实体；哦，这就是他们的状态流。反过来也成立。两个平台各做过一遍记账本之后，你带走的不只是两个 App，而是“项目”这个词的完整手感。

#### 给三种读者的一周计划

同样一个记账本，不同人做完该带走的东西不一样。对号入座，把有限的时间花在刀刃上：

- <strong>自用党（目标：下周就开始记真账）</strong>：按正文五步走，做完录入弹窗打磨和深色模式就停，别碰图表。扩展练习里挑“导出 CSV”做上，你的账永远有后路，用起来才安心。
- <strong>作品集党（目标：放进简历能看）</strong>：基础版之外，把月度统计和分类统计做出样式，深浅两套模式各截一张图；文档里画清架构图、写清踩过的坑。看的人评判的不是你做了多大，是你能不能讲清楚为什么这么分层。
- <strong>转行党（目标：面试能聊）</strong>：重点啃“MVVM”和“ViewModel 与 UI 状态”两节，把 stateIn、combine 这些词背后的“为什么”吃透；再做一条可跑的测试。面试聊项目，考的就是这些细节是不是你亲手踩出来的。

计划之外的忠告只有一条：每天收工前，把当天的代码存个档——用版本管理工具也好，打个压缩包也好。哪天你把能跑的版本改崩了又改不回来，就会明白这个习惯值多少钱。它救过每一个写代码的人，包括写这本书的人。

#### FAQ：动手时最容易卡住的几个问题

<strong>问：能不能不用 Room，直接把账目存成一个文本文件？</strong><br>答：前三笔账没问题，写到“按月求和”就露馅了：文件方案意味着每次把所有行读出来自己算，还得自己处理坏行、自己管编码。这些活数据库天生就会，一句 SUM 的事。Room 又是官方推荐的本地数据库方案（以官方文档为准），学它不亏。

<strong>问：一定要 MVVM 吗？我看有人一个文件写完也能跑。</strong><br>答：两百行以内，怎么写都行。超过五百行，你自己都找不到逻辑在哪。MVVM 不是仪式感，是“三个月后你还能看懂自己代码”的保险，也是想加测试时的前提——逻辑和界面长在一起的东西，没法测。

<strong>问：鸿蒙那几章里的 this.getUIContext().getHostContext()，为什么这章的代码里找不到？</strong><br>答：因为那是鸿蒙的 API，安卓里压根没有这个东西。安卓里需要“环境上下文”时用的是 Context，比如建数据库时传 applicationContext。两个平台很多概念长得像，但 API 名字几乎都不同——抄代码前先确认它出自哪个平台，能省掉一大半莫名其妙的报错。

<strong>问：金额用 Double 真的没事吗？网上都说必须 BigDecimal。</strong><br>答：练手记账本没事：误差躲在小数点后十几位，显示时格式化成两位，肉眼永远看不见。真做金融类产品，换成“以分为单位的整数”或 BigDecimal——这就是前面小贴士那句话的完整版。判断标准就一条：误差会不会被用户看见、会不会被累加放大。

<strong>问：我让 AI 生成了整个项目，粘进去一堆红线，怎么办？</strong><br>答：分两类处理。Unresolved reference 之类是依赖没配，回官方文档把依赖补齐；API 用法报错或提示过时，把报错原文连同你的开发环境情况一起丢回给 AI，让它自己修。别整项目一把粘：一次一个文件，跑通再下一个——出了问题，你才知道是哪个文件带来的。

<strong>问：为什么非要 LazyColumn？我用 Column 也很流畅。</strong><br>答：五十条以内确实看不出差别。差别出现在几个月后的某一天：列表滑到几百条，手机发烫、滚动掉帧，而你早忘了当初为什么用 Column。有些选择的代价是延后支付的，LazyColumn 属于“现在多打两个字，以后不用还债”的那种。

<strong>问：Flow 和 suspend 我还是分不清，给个一句话版本？</strong><br>答：Flow 是“订阅”，suspend 是“办事”。界面要一直盯着的数据——列表、统计——走 Flow；点一下干一件事——插入、删除——走 suspend。拿不准就问自己：这个结果需要“持续最新”吗？需要，就 Flow。

<strong>问：做完想装到爸妈手机上用，怎么办？</strong><br>答：最省事的路：数据线连上你的电脑，Android Studio 里选中那台设备直接运行（开发者选项的入口视品牌而定）。不开电脑的路线是打出安装包发过去安装，打包签名的完整流程以官方文档为准。记得告诉他们：这个 App 不联网，数据只在本机——对长辈来说，这句话比任何功能都安心。

<strong>问：先做界面还是先做数据层？我看教程大多先画界面，看着更有成就感。</strong><br>答：先做数据层，本章的五步拆解也是这么排的。界面好看的前提是“有东西可看”，数据层不通，界面画完也是一次性的摆设，回头还得返工。想要成就感，可以用日志里的那一行测试数据安慰自己：它已经是一笔真实的账了。

<strong>问：分类旁边想加个图标，会不会很麻烦？</strong><br>答：比你想的简单：建一张“分类名 对应 图标编号”的对照表，列表行里按分类查出编号、换上对应图标就行。真正的功夫在于前面说的“别把分类写死在界面里”——分类已经是数据，加图标就只是多一列的事。

#### 仓库层：给数据请个管家

加固点里的“状态与持久化分层”值得单独展开，因为它是新手最容易跳过、后劲最大的一层。现在的 ViewModel 直接握着 Dao：自己用没问题，但有一个隐患：哪天你想把账同步到云端，或者加一个“回收站”，就得把 ViewModel 里每一处调用都翻出来改。仓库层（Repository）就是插在中间的管家：ViewModel 只跟管家说话，管家决定去本地拿还是去网络拿，去哪拿、怎么拿，界面和 ViewModel 一概不知。

账本版的仓库薄得像个玩笑，但骨架是完整的：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordRepository.kt</span><span class="dots">···</span>
:::

```
class RecordRepository(private val dao: RecordDao) {

    fun getAll(): Flow&lt;List&lt;Record&gt;&gt; = dao.getAll()

    fun observeMonth(month: String): Flow&lt;List&lt;Record&gt;&gt; =
        dao.recordsOfMonth(month)   // Dao 里补一条按月查询

    suspend fun add(record: Record) = dao.insert(record)

    suspend fun remove(record: Record) = dao.delete(record)

    suspend fun monthIncome(month: String) = dao.monthIncome(month)

    suspend fun monthExpense(month: String) = dao.monthExpense(month)
}
```
:::

看起来只是“把 Dao 的函数换个名字再包一遍”，就是这样的，而且这是刻意的。这层薄包装的价值在于接口约定：ViewModel 依赖的是“仓库能干什么”，而不是“Room 怎么干”。哪天你在 add() 里先写本地、再发网络。ViewModel 一行都不用动；写测试时也能塞一个假仓库进去，不需要真数据库。分层的红利要到改动来临那天才兑现，而改动总是会来的。

改造路径也简单：ViewModel 的构造参数从 dao 换成 repository，所有 dao.xxx 换成 repository.xxx，十几分钟的事。做完顺手检查一遍：界面包和 data 包之间，现在是不是只剩 ViewModel 一个“接头人”？是，就对了。另外别过度设计——仓库层只需要暴露 ViewModel 真正用到的那几个方法，没人调用的方法先不写，需求来了再加，这本身就是一种分层纪律。

#### 第一条测试：给账本上一道回归保险

加固点里说“补一条可跑的测试”，这里给足做法。别被“测试”两个字吓到，第一条测试就是一段会自动运行的验证代码：插一笔账，数一数是不是一笔；删掉，数一数是不是零笔。写好它，以后每次改完代码跑一下，几十秒就知道有没有把老功能改坏：比每次手动点十遍强太多。

测数据层最省事的办法，是让 Room 建一个“内存数据库”：跑在内存里，测试结束就消失，不留垃圾：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordDaoTest.kt（骨架）</span><span class="dots">···</span>
:::

```
class RecordDaoTest {

    private lateinit var db: AppDatabase
    private lateinit var dao: RecordDao

    @Before fun setUp() {
        val context = ApplicationProvider.getApplicationContext&lt;Context&gt;()
        db = Room.inMemoryDatabaseBuilder(context, AppDatabase::class.java)
            .allowMainThreadQueries()   // 测试里图省事，允许主线程访问
            .build()
        dao = db.recordDao()
    }

    @After fun tearDown() { db.close() }

    @Test fun insertThenCount() = runTest {
        dao.insert(Record(type = "expense", amount = 25.0,
                          category = "餐饮", date = "2026-08-15"))
        assertEquals(1, dao.getAll().first().size)
    }

    @Test fun deleteThenEmpty() = runTest {
        dao.insert(Record(type = "income", amount = 100.0,
                          category = "工资", date = "2026-08-01"))
        dao.delete(dao.getAll().first().first())
        assertEquals(0, dao.getAll().first().size)
    }
}
```
:::

几个名词快速过一遍：@Before 在每条测试前跑，负责搭环境；@After 收尾；runTest 是专门伺候协程的测试助手。它们来自官方测试库，依赖怎么加以官方“测试 Room 数据库”文档为准。跑法也简单：Android Studio 里点测试类旁边的绿色箭头，看到绿色对勾，你的项目就有回归防线了。

进阶一步，把统计也算上：插两笔支出、一笔收入，调 monthExpense 和 monthIncome，核对数字对不对，这一条顺带就把“空月份返回 0”也测了，COALESCE 写没写，一测便知。三条测试，把增、删、统计都罩住，几百行的项目就算有了正经的防线。

测试也有边界，两条纪律先立好。别急着测界面：界面测试的基础设施重，第一周不值得，把测试留给数据层和校验函数这些“纯逻辑”，validateAmount 那个函数就是天生的测试对象，空串、字母、负数，一行一个用例。也别追求覆盖率数字：测最有价值的三五个行为就够了，为了好看的比例给 getter 写测试，是另一种形式的摸鱼。

#### 场景复盘：周五晚上，记完这一周

写代码的时候一个功能一个功能看，容易忘了它们拼起来是什么体验。走一遍真实的一周。周一早上，地铁上，你掏出手机点了悬浮按钮，输 4 块的早餐钱，确定，收起手机——单手三秒搞定，这就是“确定后立刻关弹窗”的意义：下一笔随时能记。周三中午，外卖 28.5，你顺手在备注里写了“和同事拼单”，将来导出 CSV 对账的那天，你会感谢这行小字。

周四出了个小插曲：手滑把 28.5 记成了 285，列表里那行红字扎眼得很。没关系——点进去，金额框里预填着 285，删一位，确定，完事。要是没有编辑功能，这个瞬间你就只能删除重录，还得在心里骂写代码的人（你自己）不考虑周全。深色模式也在这周悄悄立了功：夜里躺在床上记账，深色主题下的绿色收入、暗红支出都不刺眼，你没写一行“夜间专用界面”，全靠语义色和成对的业务色自己换装。

周五晚上，你切到本月，汇总卡片报出这个月的收入、支出和结余，数字多少不重要，重要的是“它们全是我自己一笔一笔存下来的”。睡前你把这个 App 的图标拖到手机首屏。从今天起，它不再是练习，是一个你真的在用的工具；而你对“数据 → 逻辑 → 界面”这条链路的理解，也跟着账目一起，存进了自己脑子里。

#### 七、跑通之后的三个加固点

本地版跑通之后，再补三件事，它才像一个“能用的 App”，而不是一次演示：

- <strong>状态与持久化分层</strong>：界面只读 ViewModel 暴露的状态，写入再垫一层“仓库”（Repository）。将来把本地 Room 换成云端接口，界面一行不用改。
- <strong>补一条可跑的测试</strong>：至少覆盖“新增一笔 → 合计变化”与“删除后为空”两条。项目再小，有测试就有回归防线，第四十五章讲的三道防线，在几百行的项目里照样成立。
- <strong>空状态也要设计</strong>：第一次打开、一条记录都没有时，给一句引导文案，而不是一片空白。

三件事按顺序做：先垫仓库层（半天），再补测试（一晚上），最后打磨空状态（半小时）。做完这三件，这个项目就可以光明正大写进你的简历或作品集了，“独立完成，含数据层、状态管理与基础测试”，这话一点不虚。

::: div .tip-box .rounded-lg .p-4 .mb-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>一句话记牢

{class="mt-1"}
小项目的价值不在功能多，在分层清楚。分层练熟了，后面天气项目加网络只是多接一层。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：本周完成它

{class="mt-1"}
按“数据层、ViewModel、列表页、录入页、汇总卡片”的顺序动手，每天一步。卡住了就把报错原样丢给搜索引擎或 AI（还记得第七篇《AI编程实战篇》吗？描述问题时说清“期望行为、实际行为、复现步骤”）。完成后用它记一周账，自己做的 App 用起来，成就感会推着你继续往前走。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 需求五要素 → 拆成“每步能用”的小步骤，再动手
- 数据层：Record 实体 + Dao（含月份统计 SQL）+ Database
- MVVM 分工：View 只管画，ViewModel 管逻辑，Model 管存储
- Flow + stateIn + collectAsState：数据一变界面自动刷新
- LazyColumn 懒加载列表；AlertDialog 做录入
- 三层验收（功能/边界/架构）+ 进阶挑战（月度筛选、分类饼图）
- 跑通后加固三件事：状态分层（Repository）、一条可跑的测试、空状态设计
:::
