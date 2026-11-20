---
id: di-liu-shi-si-zhang
num: 64
part: ios-kai-fa-pian
nav: 第六十四章：数据存储与网络请求
toc: default
kind: chapter
---

### 第六十四章：数据存储与网络请求

{class="chapter-intro mb-4"}
一个只能"看"的 App 是死的；能存数据、能连网络的 App 才是活的。这一章认识 iOS 数据层的"三件套"：UserDefaults（存小配置）、SwiftData（存结构化数据）、URLSession（和服务器对话），外加解析 JSON 的 Codable 和现代化的 async/await。学完这章，你就能写会记住用户习惯、会实时更新内容的真 App 了。

::: div .quick-read
##### 本章速读（5 分钟版）
这是第 53 章同一个命题的 iOS 版：一个只能"看"的 App 是死的，能存数据、能连网络的 App 才是活的。这一章认识 iOS 数据层的"三件套"，UserDefaults 存零散小配置，SwiftData 存成批的结构化数据，URLSession 跟服务器对话，外加两位好帮手：Codable 把 JSON 自动"翻译"成结构体，async/await 让联网写起来像等快递。学完你就能写会记住用户习惯、断网也能用的真 App。

最关键的有三件事。第一，记口诀：<strong>小配置进 UserDefaults，成批数据进 SwiftData，外面的数据走 URLSession</strong>——UserDefaults 是便签墙不是仓库，塞记录类数据进去，启动变慢、查询抓瞎。第二，SwiftData 三板斧：@Model 声明一张表、modelContainer 挂容器、@Query 读加 context 写，从假数组升级到真数据库只换一层。第三，联网的两条铁律和安卓那边一字不差：不阻塞主线程，正式产品必须 HTTPS。另外记住"没抛错不等于成功"，状态码要检查，失败要分诊成网络、解析、业务三层，给用户说人话加一个重试按钮，别把英文报错原话直接甩出去。缓存那节的做法值得照抄：给缓存数据标上"更新于 X 分钟前"，用户一眼知道看到的是旧是新；不该缓存的东西（验证码、一次性结果）章里列了清单，动手前扫一眼。

今天就能做的最小动作：开十分钟飞行模式，把你的 App 从头点到尾，看它接不接得住断网，飞行模式是性价比最高的测试工具，免费、离线、随时可开。想写代码的话，跟着章里"动手十分钟"给页面装上"记忆"：一个开关用 @AppStorage 存起来，杀掉重开它还在。

最大的坑。有人把请求写在界面刷新路径里：界面刷一次就请求一次，服务器还没病自己先被打死。请求只该住在 .task、按钮动作或模型方法里；有人字段"先随便建，以后再加"：加字段要迁移、改字段要搬家，第一版花十分钟把字段想全，是本章性价比最高的十分钟；有人只在有网状态下测试——断网、弱网、飞行模式、服务器出错四个场景不测，App 就只在演示视频里能用。收尾一句：存储和网络两层没有炫技空间，拼的全是"把简单的事按纪律做"，口诀念熟、边界守住、失败路径想全，你的数据层就超过大多数入门项目了。
##### 速查表
- 存什么用什么：小配置进 UserDefaults，成批数据进 SwiftData，外面的数据走 URLSession
- SwiftData 三板斧：@Model 声明表、modelContainer 挂容器、@Query 读、context 写
- JSON 怎么翻译：Codable 字段对上自动生效，对不上用 CodingKeys 改名
- 联网怎么写：URLSession 加 async/await，请求放 .task 里，别放界面刷新路径
- 没报错就是成功吗：不是，状态码要检查，失败分网络、解析、业务三层
- 错误怎么说：给用户人话加重试按钮，别甩英文报错原话
- 断网怎么测：飞行模式走一遍全流程，这是性价比最高的测试
- 字段怎么设计：第一版就想全，迁移和搬家很贵，密钥不进代码仓库
:::

#### 一、存储方案怎么选：先看这张表

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">方案</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">适合存什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">特点</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">本书哪里用</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">零散配置（开关、偏好）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">键值对，简单直接</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 65 章设置、第 66 章收藏城市</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">结构化数据（账目、记录）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方数据库封装，@Model 一行声明</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 65 章账目记录</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">（不存，联网取）服务器数据</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系统自带网络框架，无第三方依赖</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 66 章天气数据</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
数据三件套的分工

记一个口诀：<strong>"小配置进 UserDefaults，成批数据进 SwiftData，外面的数据走 URLSession"</strong>。旧教程里的 Core Data 依然能用（SwiftData 就是它的现代马甲），手写 SQLite 则基本不用碰，直接学新的，别走老路。

##### 把口诀读细一点：三个"如果"帮你验算

口诀是导航，验算靠问题。拿到一份新数据，先过这三个"如果"：

- <strong>如果它只有几个字段、一辈子就那几条</strong>（主题开关、上次选的城市、是否首次启动），UserDefaults。存进去、取出来，一行代码的事。
- <strong>如果它会随使用不断增长、要排序筛选统计</strong>（账目、待办、笔记）：SwiftData。这是真数据库的地盘。
- <strong>如果它的源头在服务器上</strong>（天气、汇率、新闻），URLSession 取回来展示；要不要存一份本地缓存，是第五节之后要专门讨论的问题。

三者不是互斥的，正经 App 三样都用。记账本项目就是现成的例子：账目记录进 SwiftData，"记账提醒"开关进 UserDefaults，城市列表的天气数据从 URLSession 来，三件套各守一段，谁也不越界。

##### 选型之前：先问数据要"活"到什么程度

三个"如果"之外还有一问，问的是数据的寿命：这份东西只活在本机，还是要跟着用户走？只活在本机，三件套随便选；要跟着用户走，用户换了手机还想让账目原样跟过去：那就要考虑云同步这条路。SwiftData 能与系统的云服务挂钩做多设备同步，机制细节以官方文档为准，新手项目可以先不管，但架构上留个心眼：把数据访问集中写在模型层，将来把"本地库"换成"本地库加同步"，界面代码不用大动。

反过来也成立：有的数据天生不想同步。比如"上次查看的城市"同步到另一台设备毫无意义，甚至添乱。想清楚每份数据该不该跨设备，选型才算完整。

##### 场景案例：给一个天气 App 列存储清单

空谈方案不如列清单。假设你要做第 66 章那样的天气 App，动工前先花十分钟把"有什么数据、各归哪条路"列出来：

- 用户收藏的城市列表（几条、要增删排序），两条路都通：嫌麻烦存 UserDefaults 里的一个数组也行，讲究一点建一个 City 模型进 SwiftData。第 66 章取的是前者，理由见下一节"适用边界"。
- 上次查看的城市，UserDefaults，一个字符串键。
- 温度单位（摄氏/华氏）、提醒开关，UserDefaults，两个布尔或字符串键。
- 天气本身（温度、晴雨、风力）——URLSession 实时拉取，本地可以存一份最近结果当缓存（后面专门讲缓存策略）。
- 用户头像、图表历史：这个阶段没有，先不设计，遇到了再回来对表。

你会发现清单列完，方案自然浮出来——选型难，通常不是方案难。通常是"到底有哪些数据"没想清楚。动手建表之前，先动手列清单。

##### 反例巡礼：三个选型翻车现场

正着讲不如反着记。三个真实感十足的反例，每一个都对应口诀里的一句。

- <strong>把几百条账目塞进 UserDefaults</strong>：App 越用越慢，启动像开老电脑，一个键挂着一个越来越大的数组，每次启动整包读进内存。正解：SwiftData。
- <strong>为了一个"是否深色模式"建了张数据库表</strong>：杀鸡用了牛刀，还要为读写它写一堆代码，同事看了直挠头。正解：一个键的事，UserDefaults（或 @AppStorage）。
- <strong>把"温度单位"这种配置每次启动都从服务器拉一遍</strong>：断网时设置页打不开，配置明明是自己的数据，却把命交给网络。正解：本地存，别联网取自己的偏好。

三个反例的共同病灶：把数据按"技术上的方便"归类，而不是按"它是什么"归类。每次存新数据前默念口诀，翻车率直线下降。

##### 三平台对照：各家管数据的行话

和上一章一样，这里给跨平台学习的读者一张方言对照表。安卓篇（第 53 章）和鸿蒙篇（第 75 章）讲过的行话，都能在 iOS 这边找到对应位置：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">用途</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">iOS（本章）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">安卓（第 53 章）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">鸿蒙（第 75 章）</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">零散小配置</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DataStore / SharedPreferences</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Preferences（首选项）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">结构化数据</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">RelationalStore（关系型数据库）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">联网请求</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">HTTP 模块</td></tr>
</tbody>
</table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
三平台数据方案对照（细节以各家官方文档为准）

规律一眼可见：每家都是"键值小仓房 + 真数据库 + 网络层"的三件套，只是名字和手感不同。你已经学过其中两家的话，这一章就是背几个新单词的事；一家没学过也不碍事，本章自足。至于还没轮到的第三家，等你学到对应篇章时，不妨翻回来对照这张表，同一套思想过三遍，比一套思想读三遍，记得牢得多。

#### 二、UserDefaults：存点小配置

::: div .code-block
:::inline div .code-head
<span>SWIFT · UserDefaults 示例</span><span class="dots">···</span>
:::

```
// 写：存一个值
UserDefaults.standard.set(true, forKey: "isDarkMode")
UserDefaults.standard.set("北京", forKey: "favoriteCity")

// 读：取出来（没有就返回默认值）
let isDark = UserDefaults.standard.bool(forKey: "isDarkMode")
let city = UserDefaults.standard.string(forKey: "favoriteCity") ?? "北京"

// 删：移除一个键
UserDefaults.standard.removeObject(forKey: "isDarkMode")
```
:::

注意它只适合<strong>零散的小配置</strong>——几十上百条记录请交给 SwiftData，别把 UserDefaults 当数据库用（会拖慢启动、也不便查询）。

这条边界的道理，下面用三类"擅长"、三条"边界"给你讲透，先看它适合干什么，再看它干不了什么。

##### 它擅长的三类典型用途

UserDefaults 可以理解成 App 的"便签墙"：每个键是一张便签，写上就一直在，撕掉就没了。它最擅长三类活：

- <strong>用户偏好</strong>：深色模式、温度单位、提醒开关，用户划一下开关你就记一笔，下次启动原样恢复。
- <strong>上次的选择</strong>：上次查看的城市、上次选中的分类标签，记下来，下次直接摆好，App 就有了"记得你"的温度。
- <strong>一次性的旗标</strong>：是否已经看过引导页、是否弹过某条提示，存个 true，从此不再打扰。

这三类活的共同点：数据量小、结构简单、改了立刻生效。注意那句"下次启动原样恢复"，UserDefaults 写入磁盘是系统替你安排的，你只管调用 set，不用操心什么时候落盘。这既是它的省心之处，也意味着别用它记"一秒都不能丢"的数据，那种活是 SwiftData 的。

##### 它不擅长的：三条边界要心里有数

边界比功能更重要，三条一次记牢：

- <strong>量大不行</strong>：它整个文件一起读进内存，塞几千条账目进去，每次启动都背着这个包袱，记录类数据一律 SwiftData。
- <strong>查询不行</strong>：它只会"按键取值"，不会"查出所有金额大于 100 的记录"。需要筛选排序的数据，进数据库。
- <strong>结构不行</strong>：存个字符串数组勉强可以，存"账目对象列表"就得自己序列化再反序列化，出错率高。对象有成片的字段，就该有数据库的待遇。

还有个常被问到的点：读的时候给的默认值（如 ?? "北京"）只是"取不到时的兜底"，不是写进去了。想让某个键在用户第一次打开时就有值，系统还提供"注册默认值"的机制（register(defaults:)），在 App 启动时统一登记一套默认配置，细节用法以官方文档为准，新手阶段用 ?? 兜底已经够用。

##### 键名管理的小纪律

UserDefaults 的键是裸字符串，敲错一个字母，读回来就是 nil，而且不报错，只是悄悄失效。这种"安静的 bug"最耗时间，所以键名要集中管理，别散落在几十个文件里随手写：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 把键名收进一个地方</span><span class="dots">···</span>
:::

```
enum Keys {
    static let isDarkMode = "isDarkMode"
    static let favoriteCity = "favoriteCity"
}

// 用的时候
UserDefaults.standard.set(true, forKey: Keys.isDarkMode)
let dark = UserDefaults.standard.bool(forKey: Keys.isDarkMode)
```
:::

键名定了就当"合同"看：改名等于换锁，旧数据就取不到了。真要改，先写"读旧键、写新键"的迁移代码，再动原键：这段话你可以先记着，等做到第 65 章的设置页自然用得上。

##### 更顺手的写法：@AppStorage 直通界面

把 UserDefaults 和上一章的 @State 摆在一起，你会发现一个尴尬：开关存在 UserDefaults 里，界面上的开关又得用一个 @State 同步着，两份状态，又回到"别存两份"的老问题。SwiftUI 给了官方解药：<strong>@AppStorage</strong>，一个把 UserDefaults 键直接包装成界面状态的属性包装器：

::: div .code-block
:::inline div .code-head
<span>SWIFT · @AppStorage 直通开关</span><span class="dots">···</span>
:::

```
struct SettingsView: View {
    @AppStorage("notify") private var notify = true

    var body: some View {
        Toggle("记账提醒", isOn: $notify)   // 拨一下，自动存盘
    }
}
```
:::

拨开关的瞬间，值写进 UserDefaults；下次启动，初始值自动从那里读回——存取和界面驱动一步到位，没有第二份状态。它背后就是 UserDefaults，所以"只放小配置"的边界原样适用。设置页这种"开关密布"的场景，@AppStorage 是最省心的姿势；需要跨多页面共享、或要做更复杂读写的，再退回手动那一套。

##### 动手十分钟：给页面装上"记忆"

五步小练习，把第 62 章的练手页面改成"有记性"的：

1. 放一个 @State private var notify = true 的开关（上一章的 ToggleRow 正好能用）。
2. 在开关的 onChange 里写 UserDefaults.standard.set(notify, forKey: "notify")。
3. 把 @State 的初始值改成从 UserDefaults 读回来：@State private var notify = UserDefaults.standard.bool(forKey: "notify")。
4. 杀掉 App 重新打开，开关停在上次的位置，页面"记住了你"。
5. 再加一个 TextField 存"我的城市"，同样的三步走一遍，体会"偏好类数据全都这个套路"。

第 4 步的瞬间就是 UserDefaults 的全部意义：用户第二天再打开，App 认得他。这份体验的成本，十行代码。

##### 顺带说清沙盒：你的数据住在谁家里

这一节顺带补一块背景板：iOS 上每个 App 住在一个"沙盒"里，系统划给你的一块私人地盘，你的数据都存这里，别的 App 默认进不来，你也默认出不去。三件套存的东西（UserDefaults 的键值、SwiftData 的库文件）都在自家沙盒里，这也是"App 能记住你、而别的 App 偷不走"的机制基础，第 21 章讲的隐私隔离落到开发层就是它。

沙盒带来两条朴素推论。一是用户卸载 App，沙盒连锅端，所有本地数据清零，没有任何确认弹窗；所以"重要数据要不要给用户一个导出/备份的出口"值得在设计期想一下。二是别把关键数据只存一份在本地，能进 SwiftData 就别手写文件，能跟着系统备份走就别走偏门——备份和换机迁移（第 18 章讲的那些场景）在系统层面认的是规矩内的数据。

#### 三、SwiftData：给数据安个"真正的家"

SwiftData 是 iOS 17 起的官方数据库方案，把"建表、增删改查"简化到了极致<strong>一个 @Model 注解，数据类就变成数据库表</strong>：

::: div .code-block
:::inline div .code-head
<span>SWIFT · SwiftData 示例</span><span class="dots">···</span>
:::

```
import SwiftData

// 1. @Model：这个类自动变成"表"
@Model
class Record {
    var amount: Double
    var category: String
    var note: String
    var date: Date

    init(amount: Double, category: String, note: String, date: Date) {
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date
    }
}

// 2. App 入口挂上容器
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: Record.self)   // 数据库就绪
    }
}

// 3. 视图里用 @Query 读、@Environment 写
struct RecordListView: View {
    @Query(sort: \Record.date, order: .reverse) var records: [Record]
    @Environment(\.modelContext) private var context

    var body: some View {
        List(records) { r in
            Text("\(r.category) \(r.amount) 元")
        }
    }

    func add(amount: Double, category: String) {
        let r = Record(amount: amount, category: category, note: "", date: Date())
        context.insert(r)     // 存
        try? context.save()   // 落盘
    }
}
```
:::

这套"@Model + modelContainer + @Query"模板可以原样搬进你的任何项目——换换字段名就行。数据一变，@Query 自动刷新界面，妙不可言。

##### @Model 逐行拆解：一个类怎么变成一张表

原代码里的 Record 值得逐行看。@Model 标在类上，框架就接管这个类：四个 var 属性变成表的四列，类型各归各位——Double 存数字，String 存文本，Date 存时间（日期是现成类型，不用自己转字符串，排序按真时间走，这是初学者最容易体会到的甜头）。init 里给所有字段赋初值，这是 @Model 类的固定写法：建一条记录就是 new 一个对象，字段值从 init 进。

三个细节值得留意。字段要写成 var 不能是 let，数据库要支持"以后改这条记录"，常量改不了；@Model 类里加计算属性（比如"格式化后的金额"）没问题，但它不会进表，进表的只有存储属性；类型挑常用的基本款（数字、字符串、日期、布尔、Data），别把复杂对象一股脑塞进来，拿不准的字段类型先查官方文档，别靠猜。

##### 增删改：context 的三个动作

原代码演示了"增"（insert + save）。补全另外两个动作，模型上下文（modelContext）就齐了：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 删除与修改</span><span class="dots">···</span>
:::

```
// 删：从列表左滑删除那行来
func delete(_ record: Record) {
    context.delete(record)
    try? context.save()
}

// 改：直接改对象的属性，再保存
func markPaid(_ record: Record) {
    record.note = "已结清"
    try? context.save()
}
```
:::

注意"改"有多顺手：@Query 查出来的对象就是活对象，直接改属性，save 一下就落盘。而 save 之前数据只改动在内存里——App 这时被杀，改动就丢了。所以养成"一组操作完了就 save"的习惯，别攒一大批改动过夜。try? 会把保存失败悄悄吞掉，学习期够用；正经项目里建议改成 do/catch 记一笔日志，失败要有痕迹（错误处理的完整套路本章后面专门讲）。

删改之后界面为什么不刷新？因为 @Query 一直盯着数据库，数据一变它自动重查、列表自动重画，上一章学的"改状态看界面"，在数据库这里依然成立，只是"状态"升级成了"数据库"。

##### 查询进阶：排序与过滤

@Query 不只是"全量捞回来"。排序你已经见过（sort: \Record.date, order: .reverse，按时间倒序——最新一笔排最上）。过滤也不难，用官方的谓词写法把条件写进去：

::: div .code-block
:::inline div .code-head
<span>SWIFT · @Query 带过滤条件</span><span class="dots">···</span>
:::

```
// 只看"餐饮"分类的账目
@Query(filter: #Predicate<Record> { $0.category == "餐饮" },
       sort: \Record.date, order: .reverse)
var foodRecords: [Record]
```
:::

筛选逻辑进了数据库，而不是把全部记录捞进内存再自己过滤，记录上万条时，这两条路的差距就是"秒开"和"转圈"的差距。统计页想按分类汇总？第 65 章会把"查询 + 统计"的组合完整走一遍，这里先记住：能交给数据库的活，别自己扛。数据库几十年的看家本领就是"又快又准地挑出你要的那几条"，你把条件说清楚就好，别抢它的活。

##### 字段之外：关系与唯一性

真实业务迟早长出两种需求。一种是"记录要挂个分类对象"，账目和分类是一对多，SwiftData 提供 @Relationship 标注来声明这类关联，让数据库替你维护"谁属于谁"。另一种是"这个字段不许重复"，城市名单里"北京"只能有一条。用 @Attribute(.unique) 标注唯一性。这两个标注的存在先记在心里，具体语法细节以官方文档为准；新手项目的第一张表通常单表就够，别一上来就把关系设计得七弯八绕。

真正要紧的是后面第七节那句"数据迁移要早想"：字段一动，老用户手机里的数据结构就变了。所以第一版建模时多花十分钟想清楚"哪些字段将来可能有"，比事后搬家便宜得多，这十分钟花在哪，第七节细说。

##### 从假数组到真数据库：升级只换一层

上一章第十节你搭的三页骨架里，账目是 @State 假数组，杀进程就清零。把它升级成 SwiftData，变的只有"数据住哪"这一层：@State private var records: [Record] = [] 换成 @Query var records: [Record]，"往数组 append"换成 context.insert 加 save，其余界面代码一行不动，列表还是那个列表，详情还是那个详情。这正是上一章"状态住对地方"的红利：数据的消费者（界面）只认接口，供应商从内存换成数据库，无人察觉。

升级顺序建议这样走：先把 @Model 类和容器挂好（原代码第 1、2 步）；再把列表页的 @State 换成 @Query；最后把录入 sheet 里"append 一条"的位置换成 insert + save。三处改动，半小时内的事，做完你的 App 第一次拥有了"关掉再开、数据还在"的能力，多数人写到这里会忍不住多记几笔账，就为了看它还在不在。

##### 场景案例：给账本设计第一张表

空讲不如上真表。给第 65 章的记账本设计第一张表，走一遍思考过程，你可以照着改字段。第一问：一条账目由什么构成？金额、分类、时间，跑不了：amount、category、date 三个字段先定下来。第二问：还有哪些"将来八成要"？备注（用户总有话要说）、收或支的方向（一笔负数还是两个类型？新手常在这里纠结，直接用金额正负表达收支最省事）。第三问：什么不该进表？月份汇总，它能从记录现算出来，存了就多一份要同步的东西，上一章的"现算纪律"在数据库时代同样成立。

定稿就是本章原代码那张表：amount、category、note、date 四个字段，朴素但够用。你在这个基础上做两个小练习：给表加一个 paymentMethod 字段（现金/移动支付），再试着用 @Query 查"本周支出"，两个练习做完，第一张表就真正长在你手里了。

##### @Query 的三种典型组合

@Query 用熟练后，一个项目里通常固定出现三种组合，对着自己的页面挑着用就行。第一种，列表页全量加排序。@Query(sort: \Record.date, order: .reverse)，最新的在最上面，记账本主页用它。第二种，统计页带过滤——前面那个 #Predicate 的例子，只捞某个分类或某个时间段的记录。汇总由筛选后的结果现算。第三种，详情页按条件找单条，列表点进来时带个 id，详情页里用上下文的查找接口按 id 取出这一条；具体写法以官方文档为准，思路先记住："详情页不是重新发一轮全量查询，是按身份牌找那一个。"

三种组合的共同点：查询条件写在视图声明处，数据一变各页面自动各刷各的。你会发现每个页面"自己管自己的查询"，互不干扰：这比把全库数据塞进一个大数组再到处传递，干净得多。

#### 四、Codable：给 JSON"翻译"

服务器的数据大多是 JSON 文本。Swift 的 <strong>Codable</strong> 协议让"JSON ⇄ 结构体"的转换自动发生，字段名对得上，魔法就生效：

::: div .code-block
:::inline div .code-head
<span>SWIFT · Codable 解析 JSON</span><span class="dots">···</span>
:::

```
// JSON: {"name":"北京","main":{"temp":26.5},"weather":[{"description":"晴"}]}
struct WeatherResponse: Codable {
    let name: String
    let main: Main
    let weather: [Weather]
}
struct Main: Codable { let temp: Double }
struct Weather: Codable { let description: String }

// JSON 字符串 → 结构体
let decoder = JSONDecoder()
let data = jsonString.data(using: .utf8)!
let result = try decoder.decode(WeatherResponse.self, from: data)
print(result.weather[0].description)   // "晴"
```
:::

铁律：<strong>先看真实返回的 JSON，再定义字段</strong>。很多"解析失败"的 bug 都是字段名写错、类型猜错（服务器发 "26.5" 字符串，你声明成 Double），把原始 JSON 打印出来对照，十秒定位。

##### 读懂这段魔法：结构体是 JSON 的"照相机"

对照着那段 JSON 看结构体：JSON 有 name，结构体就有 let name: String；JSON 的 main 是个嵌套对象，就再定义一个 Main 结构体；weather 是个数组，就写成 [Weather]。解码器拿着你的结构体当"底片"，对着 JSON 一层一层比着填，名字对上、类型对上，值就各就各位。你写的不是解析代码，是解析的"规格书"，这是 Codable 最反直觉也最省事的地方。

理解了"照相机"这个比喻，报错也就好懂了：底片上有的字段 JSON 里没给（或类型不符），解码器就抛 DecodingError，它不猜、不凑合，缺一个字段就整个失败。所以宁可把结构体字段声明成"可选"（let temp: Double?），也别对着不确定的接口硬写必填，真机上网络千奇百怪，服务器少给一个字段不算新闻。

##### 字段名对不上怎么办：CodingKeys

理想很丰满，现实里服务器的字段名常常不讲武德：全小写、带下划线、甚至拿 Swift 保留字当名字。这时候用 CodingKeys 把"JSON 里的名"和"Swift 里的名"对上号：

::: div .code-block
:::inline div .code-head
<span>SWIFT · CodingKeys 字段映射</span><span class="dots">···</span>
:::

```
// JSON: {"city_name":"北京","temp_c":"26.5"}
struct Weather: Codable {
    let cityName: String     // Swift 习惯驼峰
    let tempC: Double

    enum CodingKeys: String, CodingKey {
        case cityName = "city_name"   // 对上 JSON 的下划线名
        case tempC = "temp_c"
    }
}
```
:::

等于给每个字段发一张"译名卡"：JSON 里叫 city_name，进到 Swift 世界就叫 cityName，两边各说各的，解码器负责对账。如果整份 JSON 都是蛇形命名（下划线风格），还有个一劳永逸的开关：给 JSONDecoder 设置转换策略（convertFromSnakeCase），整批字段名自动翻译，连 CodingKeys 都省了，用哪种看你接口的统一程度，以实际返回为准。

##### 动手十分钟：本地造一份假 JSON 练解码

解码这门手艺不需要真服务器就能练。跟着四步走，把"翻译"练出肌肉记忆：

1. 把这段 JSON 存成字符串常量：let json = #"{"city_name":"北京","temp_c":"26.5"}"#，注意 temp_c 带引号，是字符串，故意埋的雷。
2. 按"底片"规则定义结构体：cityName 映射 city_name，tempC 先声明成 String（对，先委屈它）。
3. 用 JSONDecoder 解码，print 出 cityName 和 tempC：成功，体会"名字对上就通"。
4. 现在把 tempC 改成 Double 再解一次，当场抛错，读一读报错信息；再改回 String、用 Double(tempC) 手动转，又通了。

第 4 步那条报错值得细读：它会说清"哪个字段、期望什么类型、实际收到什么"。以后面对真实接口的解析失败，你要做的事一模一样：打印原文、对照类型、改底片。假数据练熟了，真接口只剩"拿到原文"这一步区别。

##### 类型陷阱：数字、字符串与日期

解码失败的重灾区在类型。三个高频陷阱提前打疫苗：一是"数字穿字符串的衣裳"：服务器发 "26.5"（带引号），你声明 Double 就崩，要么改成 String 再转，要么自定义解码逻辑；二是日期，JSON 里的时间可能是时间戳、可能是 ISO 字符串、可能是自定义格式，JSONDecoder 有对应的日期解码策略（dateDecodingStrategy），先看服务器给的什么样式，再选对策略，默认策略对不上的话失败是必然；三是可空字段，服务器"有时不给"的字段一律声明成可选，别赌它每次都给。

排查这类问题有个十秒定位法，就是原代码里那句"把原始 JSON 打印出来"：请求回来先 print 一份原文，对着原文逐字段核对名字和类型，十次里九次当场破案。剩下的第十次，多半是嵌套层级看错了，把 JSON 粘到任何在线格式化工具里缩进一下，层级一目了然。

##### 双向通行：编码回去也要会

Codable 这个词是 Decodable（解码）和 Encodable（编码）的组合：能从 JSON 翻译进来，也能翻译回去。什么时候要把结构体变回 JSON？给服务器发数据的时候，提交表单、上传配置，把你的结构体用 JSONEncoder 编成 JSON 塞进请求体发出去。第五节讲请求时你会看到完整用法。现在先记住分工：解码用 JSONDecoder，进你的世界；编码用 JSONEncoder，出去到服务器。两个方向同一套结构体，一份规格书两头用。

#### 五、URLSession + async/await：和服务器说话

iOS 联网用系统自带的 <strong>URLSession</strong>，配合 Swift 的 <strong>async/await</strong>（异步函数），"等网络"就像"等快递"一样自然：

::: div .code-block
:::inline div .code-head
<span>SWIFT · URLSession + async/await</span><span class="dots">···</span>
:::

```
struct WeatherService {
    // 异步函数：async 标记"我要等一会儿"，throws 标记"可能失败"
    func fetchWeather(city: String) async throws -> WeatherResponse {
        let url = URL(string:
            "https://api.example.com/weather?city=\(city)")!
        let (data, _) = try await URLSession.shared.data(from: url)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}

// 调用处（在 .task 里）：
.task {
    do {
        let weather = try await service.fetchWeather(city: "北京")
        // 更新界面……
    } catch {
        print("出错了：\(error)")
    }
}
```
:::

##### async、await、throws：三个词各管一件事

把函数签名那句注释展开讲透。async 写在返回值箭头前面，声明"这是个会等待的函数"：等待期间不霸占主线程，界面该转还转；await 写在调用处，意思是"我在这一行等结果，等的时候让出线程"；throws 声明"可能失败"，失败时抛出错误，调用方必须用 do/catch 接住。三个词拼起来就是一条契约：<strong>我会等、等时不卡界面、可能失败且失败不瞒你</strong>。前面几章说"联网绝不阻塞主线程"，async/await 就是官方把这条纪律做成了语法，你想写错都难。

对照着看原代码那两行主体：data(from:) 一行把"发请求、等响应、收数据"全包了，返回数据和解码之外的响应信息（下划线扔掉的部分，状态码就藏在那里，本节后面会用上它）；decode 一行把字节翻译成结构体。网络层的"骨架代码"就这么多，剩下百分之八十的功夫都花在失败时怎么办，那是第六节的主题，先把骨架背熟，再去学招式。

##### 什么时候发请求：.task 是 SwiftUI 的"自动门铃"

调用处的 .task 是关键配角：它把异步任务和视图的生死绑在一起：页面出现时任务自动开始，页面消失时任务自动取消。这解决了两个老问题：不用手写"页面加载完就请求"的时机判断，也不会"页面都关了请求还在跑"。天气页把 .task 挂在根视图上，一进页面就拉数据，就是这个用法。

进阶一点：.task 还能带一个 id 参数，id 变了，旧任务自动取消、新任务自动开始。搜索框实时联想就是典型场景：用户每敲一个字发一次请求，id 绑定搜索词，敲快了也不怕旧请求排着队回来捣乱。新手阶段用无参 .task 起步，知道有这个能力就行。

##### 没抛错不等于成功：状态码检查

原代码把响应信息用下划线扔掉了，学习期可以，真做产品要捡回来。HTTP 有个约定：服务器用状态码告诉你事情办得怎么样，200 到 299 是成功，401 是没登录或凭证过期，404 是地址不对，500 一类是服务器自己病了。麻烦在于：URLSession 对很多"坏消息"并不抛错，服务器返回 404，请求照样"成功"完成，你拿到的却是一页错误说明而不是天气数据，解码当场炸出 DecodingError，症状和"接口变了"一模一样，查起来云里雾里。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 检查状态码</span><span class="dots">···</span>
:::

```
let (data, response) = try await URLSession.shared.data(from: url)
guard let http = response as? HTTPURLResponse,
      (200...299).contains(http.statusCode) else {
    throw URLError(.badServerResponse)   // 不是 2xx，当失败处理
}
return try JSONDecoder().decode(WeatherResponse.self, from: data)
```
:::

养成习惯：解码之前先看状态码，2xx 才往下走；401 单独处理（引导重新登录），别混进通用错误里。就多四行代码，能省掉一类最难查的"玄学解析失败"。

##### 串成一页：请求、检查、解码、呈现

把本节积木拼成一整页，看它们如何咬合。页面状态用上一章说的枚举（加载中/成功/失败）管理，.task 一出现就开拉，状态码把过关，Codable 负责翻译：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 一页完整流程</span><span class="dots">···</span>
:::

```
enum LoadState {
    case loading
    case loaded(WeatherResponse)
    case failed(String)
}

struct WeatherView: View {
    @State private var state: LoadState = .loading

    var body: some View {
        Group {
            switch state {
            case .loading:              Text("加载中……")
            case .loaded(let weather):  Text("\(weather.name) \(weather.main.temp)°")
            case .failed(let message):  Text(message)
            }
        }
        .task {
            state = .loading
            do {
                let (data, response) = try await URLSession.shared.data(from: url)
                guard let http = response as? HTTPURLResponse,
                      (200...299).contains(http.statusCode) else {
                    state = .failed("服务器没答对，稍后再试"); return
                }
                state = .loaded(try JSONDecoder().decode(WeatherResponse.self, from: data))
            } catch {
                state = .failed("网络出了点问题，检查一下连接？")
            }
        }
    }
}
```
:::

从第 63 章的枚举状态，到本章的 await、状态码、Codable，一页代码里全员到齐，这就是 iOS 数据层的标准开工姿势。第 66 章的天气项目会把这页代码展开到生产级，包括更细的错误分级和缓存；这里先把骨架吃透。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>避坑提醒：两条网络铁律

{class="mt-1"}
① <strong>联网必须 async/await，绝不阻塞主线程</strong>——卡住界面是崩溃级体验。Swift 的结构化并发让这变得很自然，但别忘了 <code class="inline">try await</code> 和 <code class="inline">do/catch</code>。② <strong>ATS 默认禁止明文 HTTP</strong>：iOS 要求 HTTPS。测试本地 http:// 服务时需要在 Info.plist 里临时开例外（NSAppTransportSecurity），但正式产品必须全走 HTTPS，审核也会盯这个。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：做一个"每日一句"小应用

#### 六、网络错误也要"分级"：别把一切报错都丢给用户

断网、超时、404、服务器 500……不同的错，用户该看到的话不一样。接口要登录的，鉴权失效（401）还得单独处理，引导用户重新登录，而不是甩一句"出错了"：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 错误分级处理</span><span class="dots">···</span>
:::

```
func friendlyMessage(_ error: Error) -> String {
    if let urlError = error as? URLError {
        switch urlError.code {
        case .notConnectedToInternet: return "网络断了，检查一下连接？"
        case .timedOut:               return "请求超时，稍后再试？"
        case .cannotFindHost:         return "服务器找不到了"
        default:                      return "网络出问题了：\(urlError.code)"
        }
    }
    if let d = error as? DecodingError {
        return "数据格式不对（可能是接口变了）"
    }
    return "出错了：\(error.localizedDescription)"
}
```
:::

给用户看"人话"，给日志看"原话"（print 完整 error）。别把 <code class="inline">error.localizedDescription</code> 的英文天书直接甩给用户：产品感就藏在这些细节里。

比报错更进一步的，是根本不让用户干等：把上次成功的数据先摆出来，标注一句"更新于 X 分钟前"，再在后台默默刷新。全屏转圈等网络，体验上等于把风险转嫁给用户。网络层最值钱的从来不是请求代码，是"失败时用户看到什么"的设计。

##### 错误的三层分诊：网络、解析、业务

原代码那张分诊台可以再扩展一层，把所有错误分成三诊，每诊一套话术。第一诊网络错误（URLError）：断网、超时、找不到主机：责任多半在链路，话术指向用户的网络，顺手给个"重试"按钮。第二诊解析错误（DecodingError）：数据收到了但读不懂，责任多半在"规格书和实际数据对不上"，用户什么都不用做，你回去改代码，话术别让用户背锅。第三诊业务错误（状态码带出来的）：401 请重新登录、404 内容没了、500 服务器病了，各自有各自的处理路径。三诊划清了"该怪谁、该说什么、该做什么"，任何错误进来先归诊，再出方。

分诊的顺序也有讲究：先网络、再解析、后业务，因为解析失败的表象经常盖住网络真相（状态码那节讲过，404 的错误页拿去解码一样炸 DecodingError）。所以正规流程是"先验状态码，再解码，最后分类提示"，三道关卡按顺序把守，错误就骗不了你。

##### 话术表：六种常见错误的标准答案

把分诊结果落成一张话术表，写界面时照着抄，比现场编文案又快又稳：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">出事的场景</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">给用户看的话</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">给用户的出口</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">断网 / 无连接</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">网络断了，检查一下连接？</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">重试按钮</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">请求超时</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">请求超时了，稍后再试？</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">重试按钮</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">服务器 5xx</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">服务器开小差了，稍后再试</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">重试按钮</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">401 鉴权失效</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">登录状态过期了</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跳登录页</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">解析失败</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数据加载出了点问题</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">重试按钮（后台记日志）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">有旧数据可用</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">更新于 X 分钟前</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">下拉刷新</td></tr>
</tbody>
</table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
错误话术对照表（文案可以按你的产品调风格，出口必须有）

表格的最后一行就是那一节的灵魂：只要缓存在，多数"错误"都能降级成"旧闻"。话术的尺子很简单。说清楚发生了什么、现在看的是什么、接下来能做什么，三句齐了就是及格线。把这张表贴在显示器边上，写错误处理时先查表再动笔，比每次现场发挥又快又稳。

##### 重试与超时：自动重试的"度"

失败之后怎么办？第一反应往往是"自动重试"，但重试有度。可以自动重试的：拉取类操作（刷新天气、加载列表），读一下不会出事，重试一两次无妨，而且两次之间要隔开一点时间（隔几秒再试，别挤在同一秒连发）。绝不自动重试的：支付、提交订单这类"操作类"请求：万一服务器其实收到了，自动重试等于下了两单，这种事故没有后悔药。拿不准就手动：失败后摆一个"重试"按钮，让用户决定。手动重试还有一个隐形好处：用户的点击天然拉开了间隔，还替你确认了"此刻网络可用"，很多设计里，最聪明的重试机制就是用户本人。

超时也别放任不管：请求可以设置超时时限，超过就算失败，别让用户对着转圈发呆到天荒地老。时限给多长视接口而定，原则是"用户愿意等的最长时间"——列表类操作用户等得起的时长很短，宁可报错让他点重试，也别吊着。

##### 缓存策略：给数据摆三层货架

"更新于 X 分钟前"背后的技术就是缓存。给数据摆三层货架，越往上越快：第一层内存，刚拉到的数据顺手放在模型里，页面切走再切回来不用重新请求；第二层磁盘，把最近一次成功的 JSON 存到本地（自己写文件，或用系统自带的 URLCache 这类现成机制），App 重启了还在。第三层才是服务器——前两层都没有了才出门去取。读取顺序从上往下，写进顺序也是从上往下，这套流程叫"缓存优先"。

缓存要有"保鲜期"概念：这份数据多久会变一次？天气按分钟变，新闻按小时变，都视业务而定。保鲜期内直接用缓存，过了保鲜期先展示旧的、后台去拉新的（正是原文说的那套体验）。别忘了缓存的另一面：存的时候就要想好"存多少、留多久"，只留最近一两份数据，别把缓存盘塞成一个无人打扫的仓库。

##### 场景案例：地铁里的天气页

用一段真实场景检验缓存设计的价值。周一早高峰，你在地铁隧道里，手机没信号，只有早已下过的缓存。打开天气 App：糟糕的版本是一片白屏，转圈十秒，然后弹出"网络错误"，你明明只想看一眼今天穿什么。好的版本是：页面瞬间显示昨晚的数据，角落标着"更新于 40 分钟前"，出地面后你随手下拉，数字刷一下变成现在，全程没等一秒。

两条版本的分差不在网络代码，而在"没网时展示什么"的设计：缓存优先、旧数据标注时间、失败给手动刷新而不是自动转圈。把这个场景写进你的验收清单，每个联网页面交付前，开一次飞行模式试试，它才配叫"能用"。

##### 错误处理的"度"：什么时候该静默

分级和留痕都讲了，还有一面没讲：不是每个失败都值得惊动用户。判定尺子是"用户此刻能不能做点什么"：能做点什么的（断网可重试、过期可重登），报出来加出口；什么都做不了的（后台预取失败、统计上报失败），静默重试或记日志就好，弹窗只会制造焦虑。把这条尺子和三层分诊合起来用。先判断"该不该说"，再决定"怎么说"，错误处理才算有了完整的度。

##### 场景案例续：一次服务器 500 的完整处置

再走一遍不常见的路径。某个下午，天气服务商的机房出事，接口开始返回 500。你的 App 会经历什么？请求发出、响应回来、状态码 500，因为提前做了状态码检查，代码当场识别"这不是成功"，抛出带号码的 server 错误；分诊层翻译成"服务器开小差了，稍后再试"；界面显示这句话加一个重试按钮；与此同时缓存货架还在，页面上依然有上次的数据顶着。用户全程只会觉得"今天接口有点慢"，不至于觉得"这 App 坏了"。

同样的 500，如果当初没做状态码检查：500 返回的错误页拿去解码，炸出 DecodingError，用户看到"数据格式不对（接口变了）"——一句话把锅从服务器甩到了"你的 App 坏了"，评价星级的下限就是这么被拉低的。同样的故障，处置设计的差距就是一条评价的分差。

{class="mt-1"}
找一个免费的名言 API（比如 hitokoto 之类），用 URLSession + async/await 拉取"每日一句"，显示在屏幕中央，加个"换一句"按钮。再把喜欢的句子用 SwiftData 存进"收藏夹"。这个练习把（UserDefaults/SwiftData/Codable/URLSession）全用了一遍：做完它，第 65、66 章就是小菜一碟。
:::

#### 七、三个容易被忽略的现实问题

<strong>权限与用途说明</strong>：位置、照片、通知这些敏感权限，iOS 要求在 Info.plist 里写清用途说明，审核也会看；申请时机放在用户真正要用那个功能的那一下，别一启动就弹一堆。第 57 章讲的"先敲门再进门"，在 iOS 上同样是铁律。

<strong>密钥与配置</strong>：接口地址、API key 别硬编码进源码，更别提交到仓库——和第 55 章的密钥铁律一模一样。用配置文件或环境变量装着，并按开发 / 生产环境区分开。

<strong>数据迁移要早想</strong>：SwiftData 模型一旦改字段，老用户手机里已经存下的数据怎么办？这事要在第一个版本就留余地——动结构前先想清楚老数据往哪儿去，拿不准就查一遍官方的迁移说明再动手。

##### 顺带一条：开发与生产的两副面孔

密钥那段里"按开发 / 生产环境区分"值得单独展开。写代码时连的往往是测试服务器或调试用的 key，上线后要连正式的，如果这套切换靠"发布前手动改代码"，迟早有一天你会在发布版里留下调试配置，这类事故年年有，而且出一次就是大事。

办法是把两套配置提前分开放：接口地址、key 各备一份开发版和正式版，按构建方式自动选择，代码里不出现"要发布记得改回来"的注释。新手项目可以先用最笨的版本：一个专门的配置文件装着所有环境差异，进版本库前把敏感项填空。做法细节以后会随工具升级，思路不变<strong>环境切换靠机制，不靠记性</strong>。

##### 把三条现实问题落成三张清单

原则人人都懂，难的是落地。每条给你一张可勾选的清单，写代码前扫一眼、发版前再扫一眼，落地就靠这两眼。

- <strong>权限清单</strong>：这个功能要几个权限？每个权限的用途说明写了没有（一句话讲清"为什么要"）？申请时机是不是放在用户点到那个功能的一瞬？被拒绝之后的功能降级路径想好了没有（用户不给定位，App 至少能手动输城市）？
- <strong>密钥清单</strong>：key 在不在源码里？配置文件进没进版本库的忽略名单？换一台机器拉代码，项目还能不能跑（说明配置方式没绑死在一个人身上）？开发用的测试 key 和上线的正式 key 分开了没有？
- <strong>迁移清单</strong>：这次改字段，老数据是加默认值、改名搬运，还是废弃重建？改完的代码用"装着旧版本数据的真机"测过没有？官方迁移文档里对应的条目读过没有？

三张清单的共同精神：这些事的成本在设计期是一句话，在发布后是一次事故。花小钱免大灾，永远是好买卖。

#### 八、缓存策略实战：让"每日一句"离线也能用

缓存策略前面讲了三层货架，这里动手铺一遍。练习对象就用本章末尾"来动手"的"每日一句"：目标，断网也能看到上一次拉到的句子。思路是"缓存优先"：页面先展示上一次成功的句子，再尝试联网刷新，成了就更新并记下时间。十四行代码，五个设计决策，慢慢拆。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 缓存优先的加载流程</span><span class="dots">···</span>
:::

```
struct Quote: Codable { let text: String }

struct QuoteView: View {
    let quoteURL = URL(string: "https://api.example.com/daily")!
    @AppStorage("lastQuote") private var lastQuote = ""
    @AppStorage("lastFetch") private var lastFetch = 0.0
    @State private var offline = false

    var body: some View {
        VStack {
            Text(lastQuote.isEmpty ? "还没有句子" : lastQuote)
            if offline { Text("当前离线，显示的是上次内容") }
            Button("换一句") { Task { await load() } }
        }
        .task { await load() }
    }

    func load() async {
        do {
            let (data, _) = try await URLSession.shared.data(from: quoteURL)
            lastQuote = (try? JSONDecoder().decode(Quote.self, from: data))?.text ?? lastQuote
            lastFetch = Date().timeIntervalSince1970
            offline = false
        } catch {
            offline = true          // 没网：继续用缓存，别清空
        }
    }
}
```
:::

这段代码有四个值得圈点的决策：缓存键用 @AppStorage 存（一句话很小，符合"小配置"边界，几百字的正文放这里不算越界）；失败分支里<strong>不清空旧数据</strong>——清空缓存是最常见的自毁行为；offline 状态让用户知道自己在看"旧闻"；成功后顺手记时间戳，界面上就能标"更新于几分钟前"。四个决策单看都不起眼，合起来就是"地铁里那个好版本"的全部秘密，缓存设计的功夫从来不在存取那两行，在这些"出事时怎么办"的分支里。

数据量大一点就要升级货架：句子列表、天气详情这类成批数据，缓存该进 SwiftData 建张"快照表"，或者交给系统级的 URLCache 这类现成机制，具体选哪种视数据形状而定，原则不变：内存第一层、磁盘第二层、服务器第三层。系统级缓存的配置细节以官方文档为准，先用"自己存一份"的笨办法，够用且透明。

##### 快照表：缓存和 SwiftData 打配合

"快照表"值得单独说一句，因为它把本章两件套接在了一起：建一个和在线数据同构的 @Model（比如 CachedWeather），字段照抄接口返回，外加一个 fetchedAt 时间戳；每次网络成功就用新数据覆盖旧行。它比"往 UserDefaults 里塞 JSON"正规，比手写文件省事，还能用 @Query 直接驱动界面，离线页面和数据层严丝合缝。

配合第七节的"迁移要早想"再补一钩子：快照表是内部数据，随时可以整表清掉重建，所以它可以放心大胆地改结构，缓存数据的"可牺牲性"恰恰是它的自由。区分"真数据"和"缓存数据"两张表，还能让清缓存的功能一键只清快照、不动用户记录。

##### 反面清单：不该缓存的东西

缓存是工具不是信仰，几类东西请勿上架：验证码、口令、token 这类凭据，缓存它们等于把钥匙插在门上；用户明确"不要记住"的内容；变化太快的实时数据（缓存两秒就过期的东西缓存它干什么）。还有一条容易漏的：包含他人隐私或敏感信息的内容，缓存要跟着"退出登录即清空"走。判断口诀：存它的收益大于泄露的风险才存：数据安全这一课，第 21 章的规矩在缓存层同样生效，一条都不打折。

##### 动手：给缓存页加上"更新于 X 分钟前"

缓存页的标配是时间标注，动手加上它。第八节代码里 lastFetch 已经存了时间戳（Unix 时间，一个浮点数），算"距现在多少分钟"就是一道减法：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 计算并显示缓存时间</span><span class="dots">···</span>
:::

```
var cacheAgeText: String {
    guard lastFetch > 0 else { return "" }
    let minutes = Int(Date().timeIntervalSince1970 - lastFetch) / 60
    if minutes < 1 { return "刚刚更新" }
    return "更新于 \(minutes) 分钟前"
}

Text(cacheAgeText)
    .font(.caption)
    .foregroundStyle(.secondary)
```
:::

三行逻辑：没存过时间戳就什么都不显示；一分钟内说"刚刚"；其余报分钟数。它是计算属性，界面刷新时自动重算，时间标注永远新鲜，又落回"现算别存"的纪律。把这个小配件装进第八节的 QuoteView，你的离线页面就齐装满员了。

#### 九、async/await 的四个小坑，提前拆弹

async/await 用起来自然，但新手期有四个高频小坑，提前知道长相，遇到了不慌：

- <strong>忘了 await</strong>：调用异步函数时不写 await，编译器会直接拦下并提示你补，Swift 在这里把你看得死死的，看到紫色警告照着补就行，这坑属于"摔不死人"。
- <strong>在循环里一个个 await</strong>：十张图片串行下载，一张等完再等下一张。能并发的请求不该排队，Swift 有任务组这类并发工具，进阶用法以官方文档为准；新手期可以先接受串行，把"并发优化"记在待办里。
- <strong>把重计算夹在请求前后</strong>：await 只让"等网络"不卡界面，你自己写的排序、循环计算该卡还是会卡主线程。重活挪进模型方法或后台任务，别赖 async/await 不背锅。
- <strong>页面死了任务还在跑</strong>：手动用 Task 起的活不会随页面销毁自动取消，回来更新一个已经不存在的界面就会出怪事。新手期统一用 .task（自带生死绑定），需要手动 Task 时先想想取消路径。

四个坑的共同预防针就一针：尽量用 .task 发请求、把业务逻辑放模型里。规矩守住，async/await 是帮手不是雷区。

##### 排查案例：列表页的神秘卡顿

用一段排查复盘把本节的概念串起来。某天你发现天气列表页滚动发卡，但数据加载明明用了 async，不是说不卡界面吗？排查三步：先看卡顿时机，是"进入页面那一瞬间卡"还是"滚动全程卡"？前者嫌疑在加载路径，后者嫌疑在行渲染。再看加载路径，发现请求回来后有一段几百行的排序加格式化代码同步执行，await 只保护了"等网络"，这段计算照旧卡了主线程。最后看行渲染，每行的 body 里都在调一个日期格式化函数，滚动时每帧都在重新格式化。

处置：排序和格式化挪进模型层，加载完成后算好一次存好；行的 body 只读现成结果；日期格式化器建一个共享实例别每次新建。三处改完，滚动恢复跟手。这个案例的教训值得抄在本子上：<strong>async/await 保的是"等待"，不保"计算"</strong>——卡顿排查永远先分清这两种耗时。

#### 十、自定义错误类型：让错误说人话的正规军

第六节的分诊用 if-let 逐层试探，错误一多就容易漏。正规军做法是自己定义错误类型——用一个枚举把 App 可能发生的错误列全，请求层只负责"把原始错误翻译成自家错误"，界面层只认自家错误：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 自定义错误枚举</span><span class="dots">···</span>
:::

```
enum AppError: Error {
    case offline          // 断网
    case server(Int)      // 服务器状态码异常，带上号码
    case badData          // 数据读不懂
    case unknown

    var message: String {
        switch self {
        case .offline:        return "网络断了，检查一下连接？"
        case .server(let c):  return "服务器开小差了（\(c)），稍后再试"
        case .badData:        return "数据格式不对，我们正在修"
        case .unknown:        return "出了点小问题，再试一次？"
        }
    }
}
```
:::

请求层在 do/catch 里把 URLError、DecodingError、状态码各归各位抛出 AppError。界面层拿到错误只需要一句 error.message——话术集中在枚举里管理，想改文案改一处就行。这个模式的好处随项目规模放大：错误处理从"散落的字符串"变成"一处注册、处处使用"，测试也能对着枚举逐个验。新手项目可以先不抽象，等错误话术写到第二遍时再升级，重构的最好时机，就是你第二遍写同样代码的时候。

##### 日志：给未来的自己留线索

错误处理的最后一环是留痕。用户报"打不开"的时候，你需要的不是猜，是当时的现场记录。记什么？四样：时间、哪一步失败（请求/状态码/解码）、错误原文（完整 error，不是翻译件）、关键参数（请求了哪个接口、带了什么参数）。别记什么？用户的敏感数据，日志是给自己看的，不是新的泄露源，这条红线第 21 章讲过。

新手期用 print 打到控制台就够，Xcode 的日志面板能翻旧账；将来要收集用户端日志，再升级到系统级的日志框架，接口细节以官方文档为准。习惯现在就养成：每个 catch 里都留下一条"什么时候、在哪一步、错成什么样"的记录，三周后你回来看"为什么偶发打不开"，会感谢今天留痕的自己。日志和错误话术是同一件事的两面：话术给用户兜底，日志给你兜底，两头都稳，故障才翻不了车。

#### 十一、FAQ：存储与网络的十四个高频问题

存储和网络是新手问题密度最高的两层，下面这些问题基本月月有人问，先存档备用。读法建议：别当列表浏览，把它当"出事时的急救卡"，撞上哪个问题再回来翻哪条，印象反而深；现在通读一遍混个脸熟也值，至少出事时知道"这病有药"：

<strong>问：UserDefaults 和 SwiftData 能混用吗？</strong>答：能，而且正经 App 都在混用——各管各的数据，互不干涉。要守住的只有一条：同一份数据别两头都存一份"真身"，否则同步噩梦重演。口诀再念一遍：小配置、成批数据、外面的数据，各回各家。

<strong>问：@Query 查出来永远是空的，代码看着没错，为什么？</strong>答：按顺序查三处——App 入口挂没挂 modelContainer（忘了它，数据库根本没开工）；insert 之后 save 了没有；过滤条件是不是写得比想象中严（把条件临时删掉看能不能查出全部）。三处都不是，再看字段类型和查询类型对不对得上。

<strong>问：模拟器上能联网吗？</strong>答：能，模拟器走 Mac 的网络。但正因为如此，模拟器一切正常不代表真机没问题——蜂窝网络、弱网、VPN 这些真机环境只有真机知道。规矩是：开发用模拟器图快，网络相关功能验收必须真机再来一遍，飞行模式也开一次。

<strong>问：接口要用 key，我先写在代码里，上线前再挪走行不行？</strong>答：不好。习惯是一天养成的，"先写死、再挪走"的下一步往往就是"忘了挪走"，而且删掉的代码在版本历史里还在。从第一行就放进配置文件并加进忽略名单，让"key 不进源码"成为肌肉记忆——第 55 章那些惨案，起点都是"就这一次"。

<strong>问：await 回来以后更新 @State，界面为什么有时候不刷新？</strong>答：先确认更新的是 @State 或 @Observable 属性（改普通变量当然没人理）；再确认是不是在别的 Task 里偷偷改了页面已经销毁的状态。用 .task 把请求和页面绑在一起，这类问题基本绝迹——它替你管住了"页面死了任务还活着"的窗口期。

<strong>问：要不要给每个请求都配"加载中"转圈？</strong>答：要，但优先级排在缓存之后。正确顺序是：有缓存先展示缓存（转圈根本没机会出现），没缓存才转圈，超时或失败展示可重试的错误态。把转圈当第一方案的页面，用户会以为你的 App 很慢——其实只是架构顺序反了。

<strong>问：SwiftData 能存图片吗？</strong>答：技术上能（Data 类型的字段），但通行做法是"图片存文件、表里只记路径"——大对象进数据库会拖慢整体读写。记账本的小票照片、天气的图标缓存，都适用这条分流规则。

<strong>问：try? 和 do/catch，什么时候用哪个？</strong>答：看失败要不要被人知道。失败无所谓、可以静默放弃的用 try?（比如读一个不存在的缓存文件）；失败必须处理或必须留痕的用 do/catch（保存数据、网络请求）。风险排序记住一句：能 try? 的都是丢了也不心疼的，心疼的一律 catch。

<strong>问：用户反馈"App 打不开数据"，我这边模拟器一切正常，怎么查？</strong>答：先收集环境三要素——机型、系统版本、网络方式（Wi-Fi 还是蜂窝），这三样决定了一半答案。然后让用户截图报错画面，对照你的分诊话术定位是哪一诊。最后申请一次环境复现：用同款网络方式试一遍。新手最容易犯的错是"我这边好好的"就关单——环境不同，bug 就不同。

<strong>问：接口的返回格式变了，我的 App 会不会当场炸掉？</strong>答：会炸，但不该炸得难看。字段删了或改名，解码抛错，走"数据格式不对"的话术；这就是声明成可选字段的价值——服务器少给的、后加的字段都不至于掀桌。真正要紧的是跟服务方约定好"只加字段、不改旧字段"这类兼容规则，一纸约定省掉半个客户端的连锁返工。

<strong>问：SwiftData 的数据能导出备份吗？用户想换手机怎么办？</strong>答：导出能力要自己做——把查询结果序列化成通用格式（JSON 之类）写个文件，让用户通过系统分享面板存走；导入就是反向的解码加入库。做不做取决于数据的重要性：记账数据值得做，缓存数据不值得。第 18 章讲过的换机迁移场景，到了开发层就是这类"导出/导入"的活。

<strong>问：开发时用假数据，什么时候切真接口？</strong>答：按层切，别一刀切。第一步用本地假 JSON 练解码（第四节动手练习那套），第二步连真实接口但只读不改，第三步才碰写操作。每切一层跑一遍体检表（下一节有），确认上一层不塌再往上走——混着切最容易出"分不清是数据问题还是接口问题"的糊涂案。

<strong>问：请求数据和 SwiftData 里已有的记录"对不上"怎么办？比如服务器也存了一份？</strong>答：这是"数据真相源"问题，规矩只有一条：每份数据指定一个唯一真相源，其他地方都是它的投影。账号信息服务器是真源；本地草稿本地是真源；云端同步的数据以"最后写入者为准"并由同步机制裁决。两边都想说了算的项目，最后谁也说不算——先定真源，再写代码。

<strong>问：模拟器里的 App 卸载重装，为什么 UserDefaults 的东西也没了？</strong>答：因为它们都住在沙盒里，卸载连锅端——这不是 bug，是上一节说的沙盒规则。真机上同样如此。所以"用户会不会误删 App"从来不是技术问题，而是你要不要提供云端同步或导出备份的产品决策。

#### 十二、误区清单：五个昂贵的误解

- <strong>误区一：UserDefaults 是个缩小版数据库</strong>。它整个文件一起读写、只会按键取值，塞记录类数据进去，启动变慢、查询抓瞎。它是便签墙，不是仓库——便签墙贴满账本，翻什么都费劲。
- <strong>误区二：请求写在界面刷新路径里</strong>。放在 body 或每次重算都会触发的位置，界面刷一次就请求一次，服务器还没病自己先被打死。请求只该住在 .task、按钮动作或模型方法里，界面刷新只消费结果。
- <strong>误区三：error.localizedDescription 就是给用户看的话</strong>。那串英文是给开发者看的原话，直接甩给用户等于把日志当文案。分诊、翻译、给出口（重试按钮），三步一个不能少，产品感就差在这一步。
- <strong>误区四：测试只在"有网"状态下做</strong>。断网、弱网、飞行模式、服务器 500，这四个场景不测，你的 App 就只在演示视频里能用。飞行模式是性价比最高的测试工具，免费、离线、随时可开。
- <strong>误区五：字段设计"先随便建，以后再加"</strong>。加字段要迁移、改字段要搬家，老用户的旧数据还可能对不上号。第一版就花十分钟把字段想全，这十分钟是本章性价比最高的十分钟，没有之一。

五条里最贵的是第四条——"只在有网时测试"翻的车，往往到用户手里才被发现，而那时候你连复现现场都凑不齐。养成开飞行模式调试的习惯，受益终身。反例清单说到这里，正面的话收个尾：存储和网络两层没有炫技的空间，拼的全是"把简单的事情按纪律做"，口诀念熟、边界守住、失败路径想全，你的数据层就已经超过大多数入门项目了。

#### 十三、给三类背景读者的建议

和上一章一样，这一节按来路分三类给建议，另外给一路零基础读过来的读者单独留了一段。

##### 从安卓篇过来的读者

你在第 53 章用过 Room、DataStore 和 Retrofit，这一章几乎是"换个口音重新考一遍"：Room 的 @Dao 查询对应 @Query 加 #Predicate，都是"把筛选条件交给数据库"；DataStore 对应 UserDefaults 和 @AppStorage，键值小仓房的边界两条平台完全一致；Retrofit 对应 URLSession，但注意手感差异：Retrofit 是"声明接口自动生成实现"，URLSession 是"亲手发请求亲手解码"，自由度高，模板代码也多，把第五节那页完整流程存成自己的模板就能补齐。协程挂起函数对应 async/await，suspend 和 async 是同一件事的两种拼法，思路接得上。

最容易别扭的一点：安卓习惯把序列化交给库自动推导，Swift 这边 Codable 是"你写规格书、框架照办"，字段名映射、类型选择都要你亲自确认。头两天会觉得啰嗦，想通"底片"比喻之后，你会反过来喜欢这种确定性：解析行为全部写在你自己声明的结构体里。

##### 三平台网络层的方言表

顺手把三家的网络层行话也对照一遍，和上一章那张状态表配成一对：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">环节</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">iOS（本章）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">安卓（第 53 章）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">鸿蒙（第 75 章）</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">发起请求</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">HTTP 模块</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">异步等待</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">async/await</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">协程挂起函数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">await / Promise</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">JSON 解码</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Codable + JSONDecoder</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">序列化库自动推导</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">手动解析或工具类</td></tr>
</tbody>
</table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
三平台网络层对照（细节以各家官方文档为准）

看得出三家的"请求—等待—解码"三段式完全一致，差异只在自动化程度：安卓和鸿蒙把更多环节交给工具生成，iOS 把每一步摊开在你面前。摊开有摊开的好处，出问题时每一环你都亲手写过，排查不用猜黑盒。三家行话入账之后，你的"跨平台数据层词典"就齐了：往后无论在哪个平台碰到存储和网络的问题，先默念三段式，再对口词典，路子都是通的。

##### 从鸿蒙篇过来的读者

第 75 章的三件套在这里几乎一一对应：Preferences 对应 UserDefaults（连"别当数据库用"的警告都是同一句），RelationalStore 对应 SwiftData（鸿蒙那边写 SQL 多一些，这边声明式多一些），HTTP 模块对应 URLSession。异步写法上，ArkTS 的 await 调用和 Swift 的 async/await 同源。唯一要适应的是 Swift 把"可能失败"也写进了类型系统，throws 和 do/catch 是显式契约，不是可选项。把这套契约当成"错误处理的路线图"来读，你会发现它逼着你想清楚每一条失败路径——这正是很多自学的项目最缺的那一块。

建议你重点读 @Model 那节和"查询进阶"那节：把过滤条件写进数据库这一步，两家的收益完全一样，写法上的差异（谓词宏 versus 手写条件）看两遍就顺。另外 @AppStorage 这个直通界面的写法值得记住，它是 SwiftUI 特色，ArkUI 里你要手写持久化加状态两步，这里一步到位。

##### 从 AI 编程篇过来、习惯"指挥 AI 写代码"的读者

数据层是 AI 最容易写出"能跑但不合格"代码的地方，因为它的问题都藏在失败路径里。给 AI 下需求时，把本章的三个关键词写进指令：错误要分级（网络、解析、业务三诊）、状态码要检查（2xx 才解码）、要有缓存策略（缓存优先加时间标注）。这三条在指令里写明白，AI 的产出立刻从"Demo 级"抬到"产品级"，第 44 章做全流程实战时，这一条经验反复应验。

验收 AI 的数据层代码，盯四点：try? 有没有滥用（数据保存被静默吞错）；请求有没有写在界面刷新路径里；密钥有没有硬编码；缓存有没有上限。这四点全干净，这层代码基本可以收货：它们就是本章的"验收清单"，和上一章的三条合起来，是你指挥 AI 写 App 的全套质检工具。

##### 写给一路零基础读过来的你

存储和网络这两章概念量大，但好消息是它们"动手即懂"：清单列一遍、表建一遍、请求发一遍，概念就落了地。节奏建议照旧：读一节，练一节，别连读。本章最值得动手的是第五节末尾那页完整流程和第六节里的"每日一句"：前者是数据层的标准姿势，后者是三件套的总复习，做这两个就等于把整章过了一遍手。另外把第八节的缓存流程也跑一遍，它篇幅小、决策多，是最适合练"设计感"的一块小场地。

还有一个心态提醒：网络报错是新手期挫败感的重灾区，因为变量比界面多——你的代码没变，服务器变了、网络变了都会错。遇到"昨天还好好的"，先查环境再查代码：飞行模式开了没、接口是不是失效了、key 是不是过期了。排除环境，剩下的才是你的事，这个排查顺序能保住你不少头发。最后布置一份两章合练的作业：把上一章的三页骨架和本章的三件套清单接起来：账目进库、设置进键值、天气留好结构体。这份作业做完，你在项目篇开工前的全部准备就齐了。

##### 三类背景殊途同归的一课

三类读者背景不同，但在数据层要补的课是同一门：<strong>把"失败路径"当成一等公民来设计</strong>。界面写得再漂亮，断网时的表现才暴露真功夫；查询写得再花哨，改一次字段就散架的结构等于没设计。安卓和鸿蒙过来的读者，你们在原平台学过的 Room 迁移、Preferences 边界，到了这边是同一门课换了个教室；AI 编程篇过来的读者，你们的验收清单里从此多了一栏"失败路径"。这一课没有捷径，只有清单和复测：好消息是，本章已经把清单替你写好了。

#### 十四、实战清单：把三件套装进记账本

本章收尾，把三件套的落位清单列出来，这就是第 65 章记账本的数据层施工图，每一项都配一句验收标准，做完一项勾一项。清单按依赖顺序排：模型先行、容器随后、读写跟上、配置收尾、网络预留，谁先谁后都有讲究，颠倒了顺序，后面每一步都要回头返工。验收标准的写法也有讲究：不写"完成了没有"，写"什么现象出现了才算成"，让每一步都可自查。

1. 建模型：按第三节的场景案例定稿 Record 四字段表，验收标准：项目能编译，@Model 类没有红线。
2. 挂容器：App 入口 .modelContainer(for: Record.self)——验收标准：App 能启动，控制台没有数据库报错。
3. 接录入：录入 sheet 的"保存"改成 context.insert + save，验收标准：记一笔，杀 App，重开还在。
4. 接列表：@State 假数组换成 @Query 按时间倒序，验收标准：新增、左滑删除，列表实时跟上。
5. 接设置：提醒开关、默认城市换 @AppStorage——验收标准：拨开关，杀 App，重开还是那个位置。
6. 预留网络位：天气相关的数据结构（Codable 结构体）先定义好，请求留到第 66 章，验收标准：结构体能用本地假 JSON 解码成功。

六步做完，你的记账本就有了完整的"记忆系统"：记得每一笔账、记得每个设置、还知道去哪里取天气。第 65 章的界面代码会在这个地基上飞快铺开，你会发现项目篇的"快"，全是这两章清单的功劳。顺序也别打乱：先存储后网络。先把"记得住"做扎实，再让"会更新"锦上添花：这是第 65、66 两章的分界线，提前知道，到时候就不慌。

#### 十五、自测八题：合上书答一遍

老规矩，八道小题先自己答，再对括号里的参考答案。这章偏工程判断，答错的地方记得回小节里补课。答题时间建议控制在五分钟内，答不上来的题，说明那个概念只停在"眼熟"，还没长进手。

1. 三件套口诀是什么？各举一个例子。（小配置进 UserDefaults、成批数据进 SwiftData、外面的数据走 URLSession；开关／账目／天气）
2. @Model 类里，哪些东西会进数据库表？（存储属性；计算属性不进）
3. "增、删、改"各对应 context 的什么动作？（insert、delete、改属性；都要 save）
4. 解码失败的两大主因是什么？排查第一步做什么？（字段名对不上、类型猜错；打印原始 JSON 对照）
5. async/await 里三个关键词各管什么？（async 声明会等待、await 挂起让出线程、throws 声明可能失败）
6. 为什么"没抛错"还可能失败？该检查什么？（404 等"坏消息"不抛错；检查状态码 2xx）
7. 缓存三层货架是哪三层？读取顺序？（内存、磁盘、服务器；从上往下）
8. 哪些请求绝不自动重试？为什么？（支付、下单这类操作类请求；重复提交可能造成双份后果）

答对六题以上过关，错得多就把对应小节重读一遍，再动手把第八节的缓存流程和第十四节的清单各跑一遍，存储和网络这两层，做过才算会，会过才算稳。

#### 十六、上线前的数据层体检表

本章最后一节，把散在各节的标准收成一张体检表。功能写完、准备给真实用户用之前，逐项过一遍，每项都是一行"过/不过"，不过的项回到对应小节补课。这张表的用法有个讲究：别攒到最后一起查，每完成一个功能模块就查对应的几项，趁记忆新鲜，修改成本最低。

##### 存储体检：五项

- <strong>数据各归各家</strong>：对照三件套口诀，抽查每份存的数据——有没有记录混进 UserDefaults？不少人配置进了数据库。
- <strong>杀 App 复测</strong>：记一笔、拨一个开关、删一条，然后杀掉 App 重开：三样都还在吗？这一项专抓"看着能存、其实没落盘"的假保存。
- <strong>保存留痕</strong>：所有 save 调用不少人静默吞错（try。 满天飞）？关键保存失败时用户知道吗？静默吞错的数据丢失，是用户投诉里最难解释的一种。
- <strong>字段有余地</strong>：模型字段是按"第一版就想清楚"设计的，还是"先随便建的"？加字段的迁移路径想过吗？
- <strong>键名有契约</strong>：UserDefaults 的键集中在管理处，没有散落的魔法字符串？

存储五项对着三件套口诀查，查的是"数据放对了地方、丢了能找回"；接下来五项对着网络查，查的是"出事时用户看到什么"，两半合起来，才是完整的数据层。

##### 网络体检：五项

- <strong>状态码把过关</strong>：每个请求解码前都检查了 2xx？401 有独立处理路径？
- <strong>错误有分诊</strong>：网络、解析、业务三诊话术齐备，每条错误都有"出口"（重试按钮或跳转）？
- <strong>缓存有兜底</strong>：断网时页面不是白屏，旧数据带时间标注？缓存清单查过"不该存的东西"？飞行模式开一次，这一项当场见分晓。
- <strong>请求位置正确</strong>：请求都在 .task、按钮动作或模型方法里，body 和刷新路径里没有裸奔的请求？
- <strong>HTTPS 全覆盖</strong>：所有正式接口走 HTTPS？ATS 例外只在测试环境开了？

十项全过，你的数据层就有底气见真实用户了。这张表建议抄进你的开发备忘录，和第 63 章的施工清单配成一对：一个管"骨架搭对没有"，一个管"数据层站得住没有"。两章合起来，你手里已经有了把想法变成真 App 的全套工序，第 65 章见真章。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-quote-left mr-2"></i>一句话记牢

{class="mt-1"}
小配置进 UserDefaults，成批数据进 SwiftData，外面的数据走 URLSession，而网络层最值钱的部分，是失败时用户看到什么。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 口诀：小配置进 UserDefaults，成批数据进 SwiftData，外面的数据走 URLSession
- SwiftData 三板斧：@Model 声明表、modelContainer 挂容器、@Query 读 + context.insert 写
- Codable 自动"翻译" JSON：字段对得上，魔法就生效
- URLSession + async/await：联网像等快递；do/catch 处理失败
- 两条铁律：不阻塞主线程；正式产品必须 HTTPS（ATS）
- 错误分级 + 缓存上次结果标注时间：失败时的体验才是网络层的灵魂
- 三个现实问题：权限写清用途、密钥不进仓库、数据迁移早留余地
:::
