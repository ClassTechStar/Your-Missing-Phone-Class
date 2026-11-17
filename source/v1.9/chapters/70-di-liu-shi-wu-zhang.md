---
id: di-liu-shi-wu-zhang
num: 65
part: ios-kai-fa-pian
nav: 第六十五章：项目一——我的记账本（本地版）
toc: default
kind: chapter
---

### 第六十五章：项目一——我的记账本（本地版）

{class="chapter-intro mb-4"}
欢迎来到你的第一个"正经项目"。这个记账本虽然不联网，但五脏俱全：能记一笔账、能看流水、能按月统计、能删改。做完它，你就完整走了一遍"数据 → 逻辑 → 界面"的全流程。别急着抄代码——<strong>先想清楚再动手</strong>，这是咱们一贯的原则。

#### 一、需求思考：先问五个问题

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要素</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">答案</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who（给谁用）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自己用，家人朋友也行</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What（做什么）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">记收支、看流水、按月汇总、按分类统计</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why（为什么）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">练手 + 搞清楚钱花哪儿了</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How（怎么做）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift + SwiftUI + SwiftData + MVVM，纯本地无后端</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint（约束）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一周内完成；最低支持 iOS 17（SwiftData 门槛）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
记账本需求五要素

这五个问题不是走形式，是拿来砍功能的刀。下面咱们一问一问过一遍，你会发现每答完一个，要写的东西就少一点——这是好事，新手项目的死法十有八九是"想做太多"。

##### Who：给谁用，决定你敢砍多少功能

答案是"自己用，家人朋友也行"。这三个字值钱得很：既然是自己用，多币种不用做、多账本不用做、注册登录更不用做——你的 iPhone 本身就是完整的用户体系。但如果答案换成"给我妈用"，清单立刻变样：字号要大、分类要少、误删要能撤销（第 27 章讲适老化时那套原则，全都用得上）。先定用户，再定功能，顺序不能反。

##### What：把"记账"翻译成四块屏幕

"记收支、看流水、按月汇总、按分类统计"听起来是四件事，落到界面上其实是四块：流水列表（主界面）、记一笔弹窗、顶部汇总卡片，外加以后才做的统计页。新手最常见的翻译错误，是把"按月汇总"理解成"要做一整套报表系统"——别。第一版只要三个数字：本月收入、本月支出、结余。汇总能算对，统计页随时可以长出来。

##### Why：这个理由得撑得住第七天

"练手 + 搞清楚钱花哪儿了"不是套话。第五天晚上，你为了一个布局细节重写第三遍的时候，靠的就是这行字撑着。建议给自己加一个更具体的钩子，比如"月底我要知道外卖到底花了多少"——有了这个具体的、带点痛感的问题，你记的每一笔账都有了观众，App 也从作业变成了工具。

##### How：为什么是 SwiftData + MVVM 这一套

Swift + SwiftUI + SwiftData + MVVM，这套组合不是唯一解，但对跟着本书走到这里的你是最顺的一条路：Swift 在第 61 章过了，SwiftUI 在第 62 章练了，SwiftData 是第 64 章刚讲完的存储方案——项目章就是把学过的零件组装起来。至于为什么不用 UIKit（上手曲线陡）和 Core Data（老一代方案，概念负担重），一句话：SwiftData 是苹果现在主推的姿势，报错也更友好，新手阶段少受罪。

##### Constraint：给自己上一道枷锁

"一周内完成"是整张表里最重要的一格。期限不是压迫，是防完美主义的疫苗——没有它，你会在第三天开始纠结 App 图标配色，第五天给设置页加主题切换开关。另外"最低支持 iOS 17"不是我们挑剔，是 SwiftData 的门槛就在那儿：你的 iPhone 要是还停在 iOS 16，就先安心跑模拟器，或者把数据层降级成 UserDefaults 版（功能打折，但能走通全流程）。

再给你三条"需求膨胀"的报警信号，任何一条响了，回这张表看看：

- <strong>功能在服务想象中的用户</strong>：给"可能有人需要"的 CSV 导入写了两天，自己的一笔账还没记上；
- <strong>界面先于数据</strong>：花一晚上调卡片圆角和渐变色，数据层还是空壳——先让账存得下来，再让它好看；
- <strong>上一步没跑通就抢下一步</strong>：模型没建成就写列表页，列表页没跑通就写统计——每一步都得"能用"才准往前走。

然后拆解成"每一步都能用"的小步骤：① 建 SwiftData 数据层（能存一笔账）；② 列表页（能看流水）；③ 录入弹窗（能加账）；④ 删除与编辑；⑤ 月度汇总卡片。每完成一步，App 都是一个"能用的东西"。

"每完成一步，App 都是一个能用的东西"——这句话展开就是每一步的验收标准：① 数据层建完，往里塞一条测试数据，重启 App 还在；② 列表页写完，能看到那条数据；③ 弹窗写完，点加号能弹出、能保存、保存后列表多一行；④ 删除编辑写完，左滑能删、点行能改；⑤ 汇总卡片写完，数字跟着记录变。五步全过，你就有了一个真的能用的记账本，哪怕它长得还很朴素。

给你一个反面教材。书友小林第一晚规划了七个功能，从"语音记账"干到"账单截图识别"，三天写了两个半页面，没有一条数据真正存下来过；第四天推倒重来，照五要素砍成五个小步骤，一周后交出了一个能天天用的版本。规划阶段的克制，就是在给后期的你发工资。

如果你赶时间，五个问题还有个"地铁速答版"：给谁用——自己；做什么——记一笔、看流水、月汇总；为什么——月底想看清外卖；怎么做——课上那一套现成零件；约束——一周。四站地铁的时间，需求就定了，别让它占掉写代码的晚上。

#### 开工之前：把项目骨架搭起来

五个问题答完，先别急着写模型——花十分钟把工程建对，后面能少踩很多坑。第 60 章带你建过第一个项目，这里只说记账本特有的几个选择：

1. Xcode 里 File → New → Project → iOS → App。Product Name 建议用英文，比如 <code class="inline">LedgerBook</code>——别用中文和空格，后面写代码引用模块名时会很别扭；
2. Interface 选 SwiftUI，Language 选 Swift。如果模板里出现存储方案之类的选项，选 SwiftData 或 None 都行——没有也不要紧，下一节咱们手动挂容器；
3. Organization Identifier 随手填一个反向域名格式，比如 <code class="inline">com.yourname.demo</code>，它只影响标识，不影响你练手；
4. 建完先按 Command + R 跑一次：模拟器里蹦出空白界面，说明环境是好的——以后出了错，你至少知道不是环境背锅。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：模拟器够用，但别完全不碰真机

{class="mt-1"}
记账本几乎不用传感器，模拟器能覆盖绝大多数开发场景。但两个习惯建议养成：每周在真机上跑一次看看手感（真机调试怎么连线，第 60 章讲过）；给自己定个规矩——说"做完了"之前必须在真机过一遍。键盘弹出、深色模式、动态字体这些细节，模拟器和真机的表现并不总一样。
:::

还有一个建议：Xcode 新建项目时默认就带了本地 Git 仓库。每完成一个小步骤就提交一次，提交信息写步骤名（比如"数据层跑通"）。写砸了随时能退回去——练手项目里，这个习惯救的人比任何教程都多。远程仓库和团队协作是第 23 章附的事，本地提交到这里就够用。

##### 工程建好后，先认三个文件

工程结构第 60 章拆过，这里只说记账本会用到的三处。App 入口文件（名字和你项目同名，比如 LedgerBookApp.swift）：下一节要在这里挂数据库容器，全 App 的"总闸"。ContentView.swift：模板自带的示例界面，本章不用它——咱们新建 RecordListView 和 AddRecordView 两个文件来放界面，示例的 ContentView 可以留着也可以删。Assets.xcassets：放图片和颜色的地方，练手版记账本用系统图标就够了，这个目录先不动。建新文件用 Command + N，选 Swift File 或直接选 SwiftUI View 模板，文件名和结构体名保持一致，找起来不费劲。

#### 二、数据层：让"账"有个家

先定义一笔账长什么样——字段要够用但别贪多：

::: div .code-block
:::inline div .code-head
<span>SWIFT · Record.swift（模型）</span><span class="dots">···</span>
:::

```
import SwiftData

@Model
class Record {
    var type: String      // "income" 收入 | "expense" 支出
    var amount: Double    // 金额（元）；生产建议以「分」存 Int，见下方小贴士
    var category: String  // 分类：餐饮、交通、工资……
    var note: String      // 备注（可选）
    var date: Date        // 记账日期

    init(type: String, amount: Double, category: String, note: String = "", date: Date = Date()) {
        self.type = type
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：金额到底用什么类型存？

{class="mt-1"}
浮点数算钱有经典翻车现场：0.1 + 0.2 不等于 0.3，账目一多就会冒出 0.30000000000000004 这种诡异数字。正经做法有两条：以「分」为单位存整数（Int），展示时再格式化成元；或者用 <code class="inline">Decimal</code>（精确十进制）参与运算。上面的模型为了直观用了 Double，纯练手无妨——哪天真拿它记账，先把金额这一列换掉。这是无数前辈踩出来的坑，记在账上比记在心上牢。
:::

##### 逐行拆解：@Model 到底做了什么

先看最上面的 <code class="inline">@Model</code>。它是个宏，给这个类自动加上一整套持久化能力：SwiftData 从此认识它、能存它、能查它，还会配一个框架托管的唯一标识。这就解释了一个有趣的对比——安卓篇第 54 章的 Room 版 Record 里，你得手写 <code class="inline">@PrimaryKey(autoGenerate = true)</code> 的 id 字段；SwiftData 版没有 id，不是漏了，是框架替你管了。

五个字段各有各的讲究：

- <strong>type 用 String 存 "income" / "expense"</strong>：为什么不用 Bool？因为收支是业务概念，将来想加"转账""报销"，字符串多一个值就行。练手期图省事没问题，但记得把这两个常量集中定义在 ViewModel 里，别让 "income" 这个字面量散落在五个文件里——拼错一个字母，统计就悄悄少一块钱；
- <strong>amount 用 Double</strong>：小贴士里刚说完它的坑，练手可以，真用要换；
- <strong>category 用 String</strong>：同理，分类列表集中放一份，录入弹窗和统计页都从这一份取；
- <strong>note 默认空字符串</strong>：<code class="inline">note: String = ""</code> 是 Swift 的默认参数——不传就用空串，"备注可选"四个字就这么实现了；
- <strong>date 默认当下</strong>：<code class="inline">date: Date = Date()</code> 让"现在记"什么都不用传，补记账再让用户改日期。

init 把默认值全接住了，所以 ViewModel 里新建一条记录时只写必要字段，代码很干净。这种"字段够用但别贪多"是刻意设计：每多一个字段，录入弹窗就多一行，用户记一笔就慢一秒——记账 App 的生命线是"三秒记完"，字段越少越好。

顺带回答一个常被问到的问题：要不要给账目建关联表（比如"一笔账对应一个账户，一个账户有多笔账"）？练手阶段不要。SwiftData 支持模型之间的关联，但那套东西留给账本长出"多账户"需求再说——现在的五字段单表，够你把这个项目从零跑到上架级别的完成度。功能没到，表结构先行，是新手最贵的弯路之一。

##### 同一笔账，安卓篇怎么存

眼熟吧？安卓篇第 54 章有一张几乎一样的表：type、amount、category、note、date 五个字段一字不差。差别藏在两处——Room 版多一个自增主键 id（框架不管，你自己管），日期存的是字符串"2026-08-15"（Room 版的统计 SQL 靠字符串比较月份）；本章的 SwiftData 版不要 id（框架托管），日期是真正的 Date 类型。哪个更好？没有更好，只有更合适：字符串日期靠约定，Date 类型靠类型系统。两章对照着看，你会对"数据模型"这件事的理解深一层——模型是业务概念的翻译，翻译得好不好，后面每一步都在还债或者享福。

##### 把容器挂到 App 上：一处最容易漏的接线

模型只是图纸，还得告诉整个 App"库在哪儿"。SwiftData 的做法是在入口挂一个容器，打开项目自带的 App 入口文件，改成这样：

::: div .code-block
:::inline div .code-head
<span>SWIFT · LedgerBookApp.swift（入口挂容器）</span><span class="dots">···</span>
:::

```
import SwiftData

@main
struct LedgerBookApp: App {
    var body: some Scene {
        WindowGroup {
            RecordListView()
        }
        .modelContainer(for: Record.self)   // 全 App 的数据库容器
    }
}
```
:::

全文件就加了 <code class="inline">.modelContainer(for: Record.self)</code> 一行，但它的分量顶半章：App 启动时建好数据库文件、准备存取环境，后面所有 SwiftData 操作都从这里走。数据库文件本身由系统管理，放在应用的沙盒目录里，你既不用操心它的位置，也（刻意）找不到方便的入口去手动改它——这是好事，用户的数据就该待在系统看管的地方。忘了挂容器会怎样？App 能编译、能启动，一取数据当场崩，报错信息里通常带着 modelContainer 的字样。这条接线值得记进"新手三大谜之崩溃"排行榜。

##### 先跑通一步：塞条数据，重启验证

数据层这一步的验收标准只有一条：<strong>存进去的，重启还在</strong>。给你一个最土但最有效的验证办法——临时在列表页塞个测试按钮（验证完就删）：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 临时验证按钮</span><span class="dots">···</span>
:::

```
// 放在列表页的 toolbar 或 body 里，验证完就删
@Environment(\.modelContext) private var context

Button("塞三条测试数据") {
    for i in 1...3 {
        context.insert(Record(type: "expense",
                              amount: Double(i) * 10,
                              category: "测试分类\(i)"))
    }
    try? context.save()
}
```
:::

点一下按钮，从多任务界面把 App 完全划掉再重新打开——数据还在，这一步就毕业了。这个土办法的正式版是单元测试，第 67 章会带你写。

为什么在这一步这么较真？因为数据层是地基。有位书友第一晚写完数据层没验证持久化，接着写了三天界面，录了几十条测试账目全在内存里飘着——第四天偶然重启，数据清零，三天录入白干。地基上的活，干完立刻验，别攒。

##### 想改字段了怎么办：先 commit，再动手

写到一半想加个字段（比如"支付方式"）是常事。SwiftData 对简单的新增字段通常能自动处理迁移——重新运行就行，老数据还在，新字段用默认值填上。但"通常"不是"一定"：改字段类型、删字段这类大动作可能需要写迁移方案，具体以官方文档为准。动手前先 git commit 一次，改砸了整个数据层退回上一版，五分钟恢复现场。练手期还有一个保险：真不行就删掉 App 重装，反正测试数据不值钱——但正式期千万别这么想，用户的数据删了就真没了。

#### 三、MVVM：界面与逻辑"分家"

直接让界面操作数据库？能跑，但界面代码会又臭又长。MVVM 架构让各司其职：<strong>View（界面）只管画，ViewModel（逻辑中枢）管数据，Model（SwiftData）管存储</strong>。

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View（SwiftUI 界面）</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel（@Observable 逻辑中枢）</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model（SwiftData 数据层）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
图 4：MVVM 三层结构——数据单向流动，各层互不越界
:::

::: div .code-block
:::inline div .code-head
<span>SWIFT · RecordViewModel.swift（骨架）</span><span class="dots">···</span>
:::

```
import Observation

@Observable
class RecordViewModel {
    var records: [Record] = []
    private let context: ModelContext

    init(context: ModelContext) { self.context = context }

    func load() {
        // SwiftData 的 #Predicate 筛选 + 排序
        let descriptor = FetchDescriptor<Record>(
            sortBy: [SortDescriptor(\.date, order: .reverse)]
        )
        records = (try? context.fetch(descriptor)) ?? []
    }

    func add(type: String, amount: Double, category: String, note: String) {
        let r = Record(type: type, amount: amount, category: category, note: note)
        context.insert(r)
        try? context.save()
        load()                       // 重新加载，界面刷新
    }

    func delete(_ record: Record) {
        context.delete(record)
        try? context.save()
        load()
    }
}
```
:::

界面里 <code class="inline">@State private var vm = RecordViewModel(...)</code>，然后直接 <code class="inline">vm.records</code> 渲染列表——数据一变，界面自动刷新。

##### 错误示范：让界面直接摸数据库

先看一个能跑、但会坑你的写法：在视图里用 <code class="inline">@Environment(\.modelContext)</code> 拿到数据库环境，按钮一点直接 insert。第一个版本你感觉良好——十几行嘛。等你要加"保存前校验金额""保存后刷新统计""同一笔防双击"，这些逻辑就得复制粘贴到每一个按钮里；哪天规则变了，你得全项目找一遍改一遍。界面和逻辑不分家的账单，都是延期寄到的。

纠正后的分工：所有动数据的代码只住在 ViewModel 里，界面只做两件事——把 vm.records 画出来，把用户的动作转交给 vm。判断分家分没分对，有个简单标准：假设明天要给这个账本做一个完全不同的界面，ViewModel 一行不用改，就说明分对了。

##### @Observable 到底"观察"了什么

@Observable 是 Swift 新一代 Observation 框架的主角，它的本事是细粒度追踪：界面读了 vm.records，框架就默默记下"这个视图关心 records"；records 一变，只有关心它的地方刷新。对比老一代 ObservableObject 的"任何属性变了整个视图重算"，新方案省掉不少无用功，代码也少写一堆包装。

接线上有个细节要咬死：界面持有 ViewModel 必须用 <code class="inline">@State private var vm: RecordViewModel</code>。为什么是 @State？因为 SwiftUI 的视图是值类型，body 每次重算都会重建，@State 让框架把这个实例"钉"在原地不跟着重建。你要是顺手写成 let 或者普通 var，界面就不刷新了——数据明明变了，列表纹丝不动，这是新手三大谜之 bug 的常客。原理在第 62 章"状态与绑定"讲过，忘了就回去翻。

##### 一条数据的完整旅程：从点击保存到界面刷新

把三层串起来走一遍，比看十遍图都管用。你在弹窗里点"保存"：AddRecordView 调 <code class="inline">vm.add(...)</code>——界面没碰数据库，只交了个话。add 里新建 Record、<code class="inline">context.insert</code>、<code class="inline">save</code> 落盘，然后调 <code class="inline">load()</code> 重新查询，把结果塞进 <code class="inline">records</code>。records 一变，@Observable 立刻通知所有读过它的视图：主界面的 List 重算 body，多出来的那一行自己冒出来，动画都是白送的。整条链路里，界面只知道"调方法"，ViewModel 只知道"改数据"，谁也不越界——这就是图 4 那三个方块的全部含义。以后调试"界面没刷新"，就沿着这条链路找：数据到底存了没有？records 到底换了没有？界面到底读的是这个 vm 吗？三问下去，病灶基本现形。

##### 接线答疑：新手问得最多的两个"为什么"

问：为什么要把 vm 传进弹窗（<code class="inline">AddRecordView(vm: vm)</code>），而不是让弹窗自己新建一个？答：数据中枢全局只能有一份。弹窗里自己 new 的那个 vm 和列表页的 vm 互不相识——你在弹窗里存了账，列表页的 records 纹丝不动，你盯着代码看半天也找不出毛病，因为"毛病"是架构层面的。传引用，等于把同一条电话线接进两个房间。

问：为什么 ViewModel 类标 @Observable、界面里又要用 @State 持有？两个东西不是重复吗？答：不重复，是分工。@Observable 让"类的属性变化"变得可追踪；@State 让"视图对这个实例的持有"跨重绘稳定。一个管变化，一个管存活，缺一个链条就断——断了的表现就是那个经典症状：数据在变，界面装死。

##### try? 的两面性：省事，但会吞错

骨架代码里有两处 <code class="inline">try?</code>。它的含义是"出错就当没事发生"——fetch 失败就给个空数组，save 失败就当存好了。练手期图清净可以这么写，但你要清楚代价：数据库真出问题时，load() 会悄悄递给你一个空列表，界面不报错、控制台没动静，你以为是账丢了，其实是读取失败被吞了。

折中的做法是给吞掉的错误留个出口：

::: div .code-block
:::inline div .code-head
<span>SWIFT · load() 的兜底写法</span><span class="dots">···</span>
:::

```
do {
    records = try context.fetch(descriptor)
} catch {
    print("读取账目失败：\(error)")
    records = []
}
```
:::

一行 print，十秒钟的事，调试时能救命。正式项目里把 print 换成正经日志（第 67 章的调试三板斧会细讲），但"别让错误无声消失"这个原则，从第一个项目就得立起来。

##### ViewModel 的方法边界：进来的数据先过安检

再看 add：现在它只做"插入、保存、重载"三件事。建议给它加一道安检——金额不合法就拒绝入库，并告诉界面一声：

::: div .code-block
:::inline div .code-head
<span>SWIFT · add() 带校验返回值</span><span class="dots">···</span>
:::

```
func add(type: String, amount: Double, category: String, note: String) -> Bool {
    guard amount > 0 else { return false }   // 非法金额直接拒绝
    let r = Record(type: type, amount: amount, category: category, note: note)
    context.insert(r)
    try? context.save()
    load()
    return true
}
```
:::

返回值从空变成 Bool，界面就能据此决定"关窗"还是"提示重输"。校验规则住进 ViewModel 还有个长远好处：规则变了（比如以后允许 0 元记账），你只改这一处，界面一行不用动。这种"规则集中"的小习惯，攒到第 68 章讲架构可测试性的时候，你会发现全是伏笔。

##### load() 的两个进阶参数：先知道有，先不用上

FetchDescriptor 还能带筛选和限量条件，现在用不上，但值得知道：<code class="inline">#Predicate</code> 能按条件筛（比如只要本月的账），<code class="inline">fetchLimit</code> 能只取前若干条（比如只看最近 50 笔）。以后统计页要"只查本月"，就不必全量取回来再筛——让数据库干它擅长的活。现在全量取没问题，个人账本撑得住；这个伏笔埋在这儿，后面的扩展练习里会用上。

#### 四、界面：列表页 + 录入弹窗

::: div .code-block
:::inline div .code-head
<span>SWIFT · 记账列表页（核心片段）</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var vm: RecordViewModel
    @State private var showAdd = false

    var body: some View {
        NavigationStack {
            List {
                Section("本月结余") {          // 汇总卡片
                    SummaryRow(records: vm.records)
                }
                Section("流水") {
                    ForEach(vm.records) { r in
                        RecordRow(record: r)
                    }
                    .onDelete { idx in
                        val targets = idx.map { vm.records[$0] }
                    targets.forEach { vm.delete(it) }
                    }
                }
            }
            .navigationTitle("我的记账本")
            .toolbar {
                Button { showAdd = true } label: {
                    Image(systemName: "plus")
                }
            }
            .sheet(isPresented: $showAdd) {
                AddRecordView(vm: vm)          // 录入弹窗
            }
        }
    }
}
```
:::

##### 逐行拆解：这一页的五个零件

- <strong>NavigationStack</strong>：导航容器，顶部"我的记账本"标题栏从它这儿来，页面跳转的栈结构第 63 章讲过；
- <strong>List + Section</strong>：iOS 的"国民列表"，自带分组圆角、分隔线、滑动手势。别用 VStack 手搓滚动列表——性能和手感都差一截；
- <strong>ForEach(vm.records)</strong>：把数组展开成一行行。注意它和"遍历区间"的 ForEach 不是一回事：数组版要求元素可被识别，@Model 的类自动满足，不用你操心；
- <strong>.onDelete</strong>：左滑删除，iOS 用户十年的肌肉记忆，不做这个手势，你的列表就不"iOS"；
- <strong>toolbar + sheet</strong>：右上角加号弹出录入窗，sheet 的用法第 63 章弹窗一节刚讲过。

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>注意：多选删除的下标陷阱

{class="mt-1"}
上面 onDelete 的写法藏着本章最阴险的一个 bug：vm.delete 内部每次都会调 load()，records 数组整个换了一遍，而 idx 里装的是"删除前那一屏"的下标——删完第一条，第二个下标对应的已经不是你以为的那条，轻则删错账，重则下标越界当场崩掉。多选删除的正确姿势是<strong>先收集快照，再逐个删除</strong>：<code class="inline">let targets = idx.map { vm.records[$0] }</code>，然后 <code class="inline">targets.forEach { vm.delete(it) }</code>——先把要删的 Record 对象本身抓在手里（对象引用不会因为数组刷新而抓错），再挨个送走。单条左滑删除没这个问题，它一次只动一个下标。
:::

录入弹窗要点：金额输入框键盘用 <code class="inline">.keyboardType(.decimalPad)</code>（数字键盘），收入/支出用分段控件（Picker），分类用菜单选择，点"保存"调 <code class="inline">vm.add(...)</code> 并 <code class="inline">dismiss()</code> 关窗。

##### 流水行 RecordRow：一行账的排版

列表代码里引用了 <code class="inline">RecordRow(record: r)</code>，它还没定义。一行账要交代四件事：分类、备注（可没有）、金额、日期。排版照着系统自带 App 的习惯来——左边分类配图标，右边金额靠右对齐，日期和备注塞在下面当小字：

::: div .code-block
:::inline div .code-head
<span>SWIFT · RecordRow.swift（一行账）</span><span class="dots">···</span>
:::

```
struct RecordRow: View {
    let record: Record

    var body: some View {
        HStack(spacing: 12) {
            Image(systemName: record.type == "income" ? "plus.circle" : "minus.circle")
                .foregroundColor(record.type == "income" ? .green : .secondary)

            VStack(alignment: .leading, spacing: 2) {
                Text(record.category)
                    .font(.body)
                if !record.note.isEmpty {
                    Text(record.note)
                        .font(.footnote)
                        .foregroundColor(.secondary)
                        .lineLimit(1)          // 长备注截成一行
                }
            }

            Spacer()

            VStack(alignment: .trailing, spacing: 2) {
                Text(record.type == "income"
                     ? "+\(String(format: "%.2f", record.amount))"
                     : "-\(String(format: "%.2f", record.amount))")
                    .font(.body.weight(.semibold))
                    .foregroundColor(record.type == "income" ? .green : .primary)
                Text(record.date, format: .dateTime.month().day())
                    .font(.caption2)
                    .foregroundColor(.secondary)
            }
        }
        .padding(.vertical, 2)
    }
}
```
:::

三处小心思：收入用加号配绿色、支出减号配默认色，扫一眼就知道方向；<code class="inline">lineLimit(1)</code> 防止长备注把行撑爆；日期用 <code class="inline">.dateTime.month().day()</code> 格式化，系统自动按用户地区显示。颜色别用纯红纯绿的大色块——很多色弱用户分不清红绿，形状（加号/减号）才是真正的信息载体，颜色只是辅助。

##### 录入弹窗完整版：从骨架到能保存

骨架里的 AddRecordView 还是空的。给你一版能直接抄进项目的完整实现，先看代码再听讲解：

::: div .code-block
:::inline div .code-head
<span>SWIFT · AddRecordView.swift（完整版）</span><span class="dots">···</span>
:::

```
struct AddRecordView: View {
    let vm: RecordViewModel
    @Environment(\.dismiss) private var dismiss

    @State private var type = "expense"      // 默认记支出（多数账是支出）
    @State private var amountText = ""
    @State private var category = "餐饮"
    @State private var note = ""

    let categories = ["餐饮", "交通", "购物", "居住", "娱乐", "医疗", "其他"]

    var amount: Double? {
        Double(amountText)                   // 转不出来就是 nil，不崩
    }

    var canSave: Bool {
        (amount ?? 0) > 0
    }

    var body: some View {
        NavigationStack {
            Form {
                Picker("类型", selection: $type) {
                    Text("支出").tag("expense")
                    Text("收入").tag("income")
                }
                .pickerStyle(.segmented)

                HStack {
                    Text("金额")
                    TextField("0.00", text: $amountText)
                        .keyboardType(.decimalPad)
                        .multilineTextAlignment(.trailing)
                }

                Picker("分类", selection: $category) {
                    ForEach(categories, id: \.self) { Text($0) }
                }

                TextField("备注（可选）", text: $note)
            }
            .navigationTitle("记一笔")
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("取消") { dismiss() }
                }
                ToolbarItem(placement: .confirmationAction) {
                    Button("保存") {
                        if let a = amount,
                           vm.add(type: type, amount: a,
                                  category: category, note: note) {
                            dismiss()
                        }
                    }
                    .disabled(!canSave)
                }
            }
        }
    }
}
```
:::

三个设计点值得展开。其一，金额用字符串存、转换放计算属性：TextField 的 text 绑定天生是 String，硬塞 Double 会处处别扭；转换放在 <code class="inline">amount</code> 里，转不出来就是 nil，非法输入在"进 ViewModel 之前"就被拦下。其二，用 disabled 灰掉保存按钮：<code class="inline">canSave</code> 不满足时按钮自动变灰，灰按钮本身就是提示，比弹警告窗温柔。其三，保存成功才 dismiss：add 返回 true 才关窗，失败时窗口留着，用户已经输的东西一条不丢。

##### 分类列表放哪儿：一处定义，处处引用

弹窗里那个 <code class="inline">categories</code> 数组随手写在视图里了，工程上一旦统计页也要用同一份分类，你就得复制粘贴。建议给它一个正式的家——新建一个专门的常量文件，或者放进 ViewModel：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 集中定义常量</span><span class="dots">···</span>
:::

```
enum Ledger {
    static let categories = ["餐饮", "交通", "购物",
                             "居住", "娱乐", "医疗", "其他"]
    static let income = "income"
    static let expense = "expense"
}

// 用的时候：Ledger.categories、Ledger.income
```
:::

以后弹窗、流水行、统计页全都写 <code class="inline">Ledger.income</code>，哪个地方想加一个"宠物"分类，只改一行。这种小整理在项目长到第二个界面之前做，成本最低。

##### 键盘与聚焦：两处小接线

第一处：数字键盘没有"完成"键，收键盘要靠手势或滚动。给 Form 挂上 <code class="inline">.scrollDismissesKeyboard(.interactively)</code>，用户往下滑动键盘就跟着收，一行搞定。

第二处：进弹窗自动聚焦金额框，省一次点击。用一个 <code class="inline">@FocusState</code> 变量绑定金额输入框，界面出现时把焦点递过去：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 自动聚焦金额框</span><span class="dots">···</span>
:::

```
@FocusState private var amountFocused: Bool

TextField("0.00", text: $amountText)
    .keyboardType(.decimalPad)
    .focused($amountFocused)
    .onAppear { amountFocused = true }
```
:::

这种"少一次点击"的细节单看不显眼，攒上五六个，App 的手感就和"学生作业"拉开档次了。

##### 深色模式：不写死颜色，就自动及格

SwiftUI 的默认组件天生支持深色模式——前提是你别跟系统较劲。背景用默认的，别铺一层写死的白色；文字用 <code class="inline">.primary</code>、<code class="inline">.secondary</code> 这些语义色，别写死 Color.black；绿色标记收入在深色模式下也看得清，因为系统给的 .green 本来就带两套颜色。验收办法很土：模拟器里把外观切成深色，每一页扫一遍，看有没有哪块"白底白字"或者刺眼——真机验收清单里也有这一条。

还有一个新手最容易漏的画面：<strong>空状态</strong>。刚装上 App 一条记录都没有，别让用户对着白屏发呆——给一句明确的提示，再放一个「记第一笔」的入口。iOS 17 起有现成的 <code class="inline">ContentUnavailableView</code>（图标 + 标题 + 描述），几行就能搭出「还没有账目，点右上角 + 记第一笔」。

配合 <code class="inline">ContentUnavailableView</code>，空状态长这样：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 空状态视图</span><span class="dots">···</span>
:::

```
if vm.records.isEmpty {
    ContentUnavailableView {
        Label("还没有账目", systemImage: "tray")
    } description: {
        Text("点右上角 +，记下第一笔")
    }
} else {
    // 正常的流水列表
}
```
:::

把它包一层条件判断——records 为空时显示它，有数据时显示流水列表，第一屏就永远不会再是白板。

##### 金额校验的三道关

"用户输入的一切都要当敌人审查"，落到金额上，审查分三道关。类型关：<code class="inline">Double(text)</code> 转不出来就是非法，nil 直接拒绝。范围关：0 和负数拦下，另外留意"手滑多打一个 0"——一笔记成十倍，比崩溃更可怕的是账默默错着，可以给个大额提醒（比如金额超过你半个月生活费就弹个确认，具体数字你自己定）。格式关：粘贴进来的内容什么都有可能，别只信键盘。三道关都放进 ViewModel 的 add 里过，界面不用重复写。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>注意：输入校验别偷懒

{class="mt-1"}
金额输入框一定要校验：空值、负数、"abc"这类非法输入都要拦住（用 <code class="inline">Double(text)</code> 判断，失败返回 nil）。App 崩掉最常见的原因之一就是"把用户的输入当成了乖孩子"。记住：<strong>用户输入的一切，都要当敌人审查</strong>。
:::

#### 五、编辑、删除与汇总

- <strong>删除</strong>：List 的 .onDelete 左滑删除 + 确认弹窗（误删是记账类 App 用户最痛恨的事）；
- <strong>编辑</strong>：点行进编辑弹窗，预填原值（改一个字比重新输入省事）；
- <strong>汇总</strong>：用 <code class="inline">filter</code> + <code class="inline">reduce</code> 算"本月收入 / 支出 / 结余"，顶部卡片展示：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 月度汇总计算</span><span class="dots">···</span>
:::

```
func monthSummary(_ records: [Record]) -> (income: Double, expense: Double) {
    let cal = Calendar.current
    let monthRecords = records.filter {
        cal.isDate($0.date, equalTo: Date(), toGranularity: .month)
    }
    let income = monthRecords
        .filter { $0.type == "income" }
        .reduce(0) { $0 + $1.amount }
    let expense = monthRecords
        .filter { $0.type == "expense" }
        .reduce(0) { $0 + $1.amount }
    return (income, expense)
}
```
:::

##### 汇总代码逐行读

这十来行里有三个值得咀嚼的点。第一，"同一个月"的判断交给 <code class="inline">cal.isDate(_:equalTo:toGranularity:)</code>——大小月、跨年这些边角系统都替你处理了，别手写"日期字符串前七位相等"这种土办法。安卓篇第 54 章的 Room 版就是拿字符串比较月份的，也能用，但前提是存储时格式永远规整；本章存的是真正的 Date 类型，从根上免了这份约定。第二，<code class="inline">reduce(0) { $0 + $1.amount }</code> 是把数组折叠成一个数的标准姿势，看着眼生就回去翻第 61 章闭包那节。第三，这段代码把数组过了两遍（先筛收入再筛支出），账目多了可以换成一遍 for 循环同时累加两个数——不过个人记账一年也就几百上千条，先把功能做对，再谈快。

##### 汇总卡片：SummaryRow 长这样

数字算出来了，还得体面地摆上去。给顶部那个 Section 用的行视图可以这样写：

::: div .code-block
:::inline div .code-head
<span>SWIFT · SummaryRow.swift（汇总卡片）</span><span class="dots">···</span>
:::

```
struct SummaryRow: View {
    let records: [Record]

    private var s: (income: Double, expense: Double) {
        monthSummary(records)
    }

    var body: some View {
        HStack {
            VStack(alignment: .leading, spacing: 4) {
                Text("本月结余")
                    .font(.footnote)
                    .foregroundColor(.secondary)
                Text("\(String(format: "%.2f", s.income - s.expense)) 元")
                    .font(.title2.bold())
            }
            Spacer()
            VStack(alignment: .trailing, spacing: 4) {
                Text("收入 \(String(format: "%.2f", s.income))")
                    .font(.footnote)
                Text("支出 \(String(format: "%.2f", s.expense))")
                    .font(.footnote)
            }
        }
        .padding(.vertical, 4)
    }
}
```
:::

排版逻辑：结余放左边当主角——用户打开汇总卡想看的就是"这个月净剩多少"；收入支出缩成右侧两行小字当配角。数字用 <code class="inline">String(format: "%.2f", ...)</code> 统一两位小数，别让浮点尾巴直接上屏——小贴士里那个 0.30000000000000004，展示层是最后一道防线。

##### 编辑：复用录入弹窗，别写第二个

编辑和录入的字段一模一样，界面也该一模一样——给 AddRecordView 加一个可选参数就行：

::: div .code-block
:::inline div .code-head
<span>SWIFT · sheet(item:) 打开编辑</span><span class="dots">···</span>
:::

```
@State private var editingRecord: Record?

// 行的点击手势里：editingRecord = r
.sheet(item: $editingRecord) { r in
    AddRecordView(vm: vm, editing: r)
}
```
:::

<code class="inline">sheet(item:)</code> 要求对象可识别，@Model 的类天生满足，直接用。弹窗内部发现 editing 不为 nil 时，onAppear 把原值预填进各个输入框；点保存时不新建，直接改这个对象身上的属性，再 <code class="inline">try? context.save()</code>——SwiftData 对已入库对象的属性修改，保存后自动落库。用户视角的效果：点任何一行，看到的是那笔账的原样，改一个字就能存。顺手给行加点击手势时记得留出左滑删除的区域，两个手势不冲突，但都得能被摸到。

##### 补记账：日期选择器别省

真实生活里大量账是事后补的——昨天打车忘了记，前天的外卖今天想起来了。录入弹窗里放一个 <code class="inline">DatePicker("日期", selection: $date)</code>，默认今天，想补哪天改哪天。汇总代码按 date 字段统计，补记的账自然落进正确的月份——这就是数据层存真日期的好处，前面省的力气这里全还给你。反例是某些新手为了省事不存日期、只存"第几条"，等想做月度汇总那天，只能对着满屏记录一条条人工回忆，欲哭无泪。

##### 删除的两种姿势，加一颗后悔药

单条删除用左滑（onDelete），批量清理在 toolbar 放个 <code class="inline">EditButton</code> 进编辑模式勾选——多选时的下标陷阱，照第四节"先收集快照再逐个删除"的修法处理。真正拉开体验差距的是后悔药：误删是记账用户最恨的事，光靠确认弹窗不够——弹窗点多了就成了肌肉记忆，照样删。更顺手的做法是删除后在底部冒出一条"已删除 · 撤销"：实现思路很朴素，删之前把那条记录的字段抄下来，用户点撤销就用这些字段重建一条新的，再 load() 刷一遍。十几行代码，换来的安全感巨大。

#### 六、验收：三层检查 + 两个进阶挑战

项目做完，按"功能 → 边界 → 架构"三层验收：能不能记、能不能删、重启 App 数据还在不在（功能）；金额输 0 或负数会不会崩（边界）；界面和数据有没有混在一起、字段有没有硬编码（架构）。

把这三层展开成一张能打勾的清单，验收时逐条过：

- <strong>功能层</strong>：能记一笔、能删一笔、能改一笔；完全退出重开，数据都在；汇总卡三个数字和流水对得上；
- <strong>边界层</strong>：金额输 0、负数、"abc"，App 不崩且不给保存；备注贴一段两百字长文，界面不破；日期选到去年，账落进正确的月份；保存按钮连点两下，只记一笔（保存成功立即 dismiss，天然防了双击）；
- <strong>架构层</strong>：界面代码里有没有直接出现 context（有就是分家没分干净）；"income" 这类字符串字面量是不是只住在 ViewModel；ViewModel 里有没有超过一屏的方法（有就该拆了）。

从「演示」到「经得起每天打开」，还差两件小事，顺手做掉：

- <strong>两条单元测试</strong>：覆盖「新增一笔 → 合计变化」和「删除后 → 归零」就够了；SwiftData 的持久化在测试里可以用测试配置隔离，不碰真数据（XCTest 怎么写，第 67 章马上讲）；
- <strong>无障碍</strong>：给金额输入框、保存按钮这些关键控件加 <code class="inline">accessibilityLabel</code>，文字交给系统动态字体——花不了十分钟，却决定长辈能不能用你的 App。

##### 两条单元测试的真身

"用测试配置隔离"落到代码里长这样：

::: div .code-block
:::inline div .code-head
<span>SWIFT · LedgerTests.swift（内存容器测试）</span><span class="dots">···</span>
:::

```
import XCTest
import SwiftData

final class LedgerTests: XCTestCase {

    func testAddChangesCount() throws {
        let config = ModelConfiguration(isStoredInMemoryOnly: true)
        let container = try ModelContainer(for: Record.self,
                                           configurations: config)
        let vm = RecordViewModel(context: ModelContext(container))

        vm.add(type: "expense", amount: 12,
               category: "测试", note: "")

        XCTAssertEqual(vm.records.count, 1)
    }

    func testDeleteEmpties() throws {
        // 同样的内存容器：先加一笔，删掉，断言归零
        let config = ModelConfiguration(isStoredInMemoryOnly: true)
        let container = try ModelContainer(for: Record.self,
                                           configurations: config)
        let vm = RecordViewModel(context: ModelContext(container))

        vm.add(type: "expense", amount: 12, category: "测试", note: "")
        vm.delete(vm.records[0])

        XCTAssertTrue(vm.records.isEmpty)
    }
}
```
:::

关键在 <code class="inline">ModelConfiguration(isStoredInMemoryOnly: true)</code>：测试跑在一个内存数据库里，不碰你手机上真实的账本——这就是正文说的"测试配置隔离"。这也回过头解释了为什么 ViewModel 要接收 context 参数：能注入，就能替换。第二条"删除后归零"照葫芦画瓢。测试怎么组织、怎么跑，第 67 章有整节，这里先混个脸熟。

##### 无障碍：这十分钟花给谁

给关键控件补上 <code class="inline">.accessibilityLabel("金额")</code> 这类标注，旁白（VoiceOver）用户就能听懂每个框是干嘛的、按钮按下会发生什么。另一条隐形红线：别把字号写死——<code class="inline">.font(.system(size: 14))</code> 这种写法在用户调大系统字体时纹丝不动，等于告诉长辈"你的视力与我无关"。用 <code class="inline">.body</code>、<code class="inline">.title</code> 这些语义字体，字号自动跟着设置走。这十分钟不是慈善，是给未来的你自己——谁没有老去的一天。

基础版验收通过后，给自己加两道"进阶菜"：

1. <strong>分类统计</strong>：加一个"统计"标签页，用 <strong>Swift Charts</strong> 把分类支出画成饼图/柱状图——苹果官方图表库，几行代码出图；
2. <strong>iCloud 同步</strong>：SwiftData 开 iCloud 同步只需配几项设置——账本在 iPhone/iPad 之间自动同步，瞬间"高级"起来。分层的好处这时候显出来了：界面、状态、持久化各管各的，把本地存储换成云同步，界面基本不用动。

##### 进阶一：Swift Charts 出图的最短路径

先把支出按分类归堆求和，再交给 Charts 画柱状图：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 分类支出柱状图</span><span class="dots">···</span>
:::

```
import Charts

// items: [(category: String, total: Double)]
Chart(items, id: \.category) { item in
    BarMark(
        x: .value("分类", item.category),
        y: .value("金额", item.total)
    )
}
.frame(height: 220)
```
:::

归堆用 <code class="inline">Dictionary(grouping: by:)</code> 按分类分组、再对每组求和，剩下的坐标轴、配色 Charts 全包了。入口建议做成 TabView 的第三个标签（TabView 用法第 63 章讲过）。做完它，账本就从"流水账"升级成"看得见结构的账"——凌晨想知道这个月奶茶花了多少，一眼就有答案。

##### 进阶二：iCloud 同步，动配置不动架构

SwiftData 开同步的大头在工程配置：选中 target，Signing &amp; Capabilities 里添加 iCloud 能力、勾选容器，模型侧按官方文档声明支持，具体开关项以官方文档为准。代码层几乎不用大改——这正是分层的好处：ViewModel 和界面根本不知道数据住在本地还是云端。做完这一步，iPhone 上记的账在 iPad 上也在，家人拿你的旧设备也能一起记，App 一下子从"练手项目"变成"家里真能用的东西"。动手前记得 git commit，云配置改砸了能整体退回。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：本周完成它

{class="mt-1"}
按"数据层 → ViewModel → 列表页 → 录入弹窗 → 汇总卡片"的顺序动手，每天一步。卡住了就把报错原样丢给搜索引擎或 AI（还记得第七篇《AI编程实战篇》吗？描述问题时带上环境版本——比如 Xcode 26 / Swift 6.2——再说清"期望行为、实际行为、复现步骤"，版本说清了能少绕不少路）。完成后用它记一周账——自己做的 App 用起来，成就感会推着你继续往前走。
:::

#### 七、常见 bug 门诊：六个高频翻车现场与修复动作

下面六个病例来自真实的新手提问，症状、病因、处方一次给全。对号入座，比搜索引擎快。

<strong>病例一：加了记录，列表纹丝不动</strong>。数据明明 insert 了，界面没反应。九成是界面持有 ViewModel 的姿势不对：写成 let 或者普通 var，或是在 body 里现 new 一个，框架根本没在观察它。处方：<code class="inline">@State private var vm</code> 只初始化一次，类上确认有 @Observable。剩下的一成是增删改之后忘了调 load()——数据变了，但没通知数组换血。沿着第三节那条"数据旅程"三问，基本都能定位。

<strong>病例二：重启 App，账全没了</strong>。两种病因。入口忘挂 .modelContainer——取数据当场崩，好发现；挂了但 save 一直失败，而 try? 把失败吞了——阴险得多，界面一切正常，重启清零。处方：临时把 <code class="inline">try? context.save()</code> 换成 do-catch 打印错误，重启验证一次，确认落盘再换回去。第三节说过，吞错是安静的地雷，这一例就是它炸的样子。

<strong>病例三：点了保存没反应</strong>。金额框里明明有数字，保存按钮却一直灰着。多半是校验在拦：全角数字、夹了空格的输入，Double 解析失败返回 nil，canSave 恒为 false——不是 bug，是安检在工作，只是用户不知道。处方：金额框用 decimalPad 挡掉字母输入；遇到"看着是数字还是灰"，检查文本里是不是混了全角字符或空格。顺便表扬一下 disabled 灰按钮的设计——用户至少知道"条件没满足"，而不是点了没动静。

<strong>病例四：键盘把保存按钮顶出屏幕</strong>。把保存按钮从页面底部挪进导航栏 toolbar（取消、保存放左右两角），键盘弹起时系统自动处理导航栏避让；再配一个 scrollDismissesKeyboard，滚动收键盘。底部放大按钮的方案留给字段少的表单，弹窗里别用。

<strong>病例五：预览没数据或直接崩</strong>。#Preview 里忘了挂容器，预览一渲染取数据的代码就炸。处方：给预览也挂 <code class="inline">.modelContainer(for: Record.self)</code>；想让预览里有几条好看的假数据，用内存配置（isStoredInMemoryOnly）建个容器再塞两条——和单元测试同一招，搜索"SwiftData preview sample data"有现成写法。

<strong>病例六：多选删除，删错或崩溃</strong>。就是第四节讲过的下标陷阱：每次 delete 内部 load()，数组换血，旧下标失效。处方：快照先行——<code class="inline">let targets = idx.map { vm.records[$0] }</code>，再 <code class="inline">targets.forEach { vm.delete(it) }</code>。哪天想根治，可以把"每次操作都 load"改成"批量操作完统一 load 一次"，不过那是第 68 章架构优化的活儿，现在先记住快照这招就够。

#### 八、边界情况清单：这些场景，想清楚再写代码

bug 门诊治的是"已经翻车的"，这一节防的是"还没翻车的"。八个边界场景，动手前过一遍脑子，动手后就不用半夜爬起来修。

<strong>边界一：跨月的那一分钟</strong>。23:59 记的账和 00:01 记的账分属两个月。isDate 按 toGranularity 判断，用的是设备当前日历和时区的"自然月"——对个人记账这就是正确语义，你的本地时间就是你的月。真要较真（出差跨时区记账），将来记下"记账那一刻的时区"再说，现在不用管。

<strong>边界二：同一笔记了两遍</strong>。手一抖连点两次保存，汇总就虚高一笔。低成本防线是"保存成功立即 dismiss"，双击的第二下已经没有按钮可点；想再稳一点，add 前查一下"同金额、同分类、同一天"的记录是否刚记过，是就弹个温和的确认。

<strong>边界三：大额与小额</strong>。0.01 能存（大于 0 就放行），真正的风险是手滑多打个 0——一百变一千。给个软提醒：金额超过你日常单笔的量级就弹确认，具体数字自己定，别在代码里写死一个"全天下通用"的阈值。

<strong>边界四：超长备注</strong>。列表行的 lineLimit(1) 已经防了撑爆；编辑体验上，备注框可以用多行形态（TextField 自带竖向增长的参数），长备注输入时有地方展开，保存时也不怕截断。

<strong>边界五：正在编辑的记录被删了</strong>。两个界面同时指向同一条记录是本地单机 App 的少见但真实的场景。稳妥写法：保存编辑前守卫一下——这条对象还在 records 里才动手，不在就提示"这条已被删除"并关窗。一行 guard 的事，写上它，你半夜少接一个自己吓自己的调试电话。

<strong>边界六：中途杀 App</strong>。用户点完保存立刻上划杀掉 App，账还在不在？在——因为 add 里是 insert、save、load 三连发，保存即落盘，不存在"攒着一起写"的空窗。要记住这个顺序，别哪天"优化"成批量攒写，把刚保存的账攒丢了。

<strong>边界七：系统设置变了</strong>。用户改了时区、改了日历设置，汇总会不会乱？Calendar.current 每次现取，行为跟着系统走，一般无感。真正要记的是：别在哪个角落把日历或时区缓存成常量——动态取，跟系统保持一致，麻烦最少。

<strong>边界八：测试数据忘删</strong>。上架或给家人装之前，把"塞三条测试数据"按钮和那些"测试分类"记录清干净。检查办法：搜索代码里所有 "测试" 字样，再在真机上把流水翻一遍。演示数据混进真账，是记账类 App 上线前最尴尬的事故。

#### 九、性能与数据量：账记了一年会怎样

先给结论：个人记账的数据量，撑得起这一章的写法，你不用现在就优化。List 本身是懒加载的——屏幕上只画看得见的那十几行，滚到哪儿画到哪儿，几千行也不卡。真正值得留意的是每次 load() 全量查询：一年记账也就几千条，取回来到渲染完通常都在一瞬间，感知不到。

什么时候该管性能？两个信号：界面出现你能感知的卡顿；统计页打开明显变慢。出现了再动手，三板斧按顺序试：第一斧，列表只取最近若干条（fetchLimit），统计页单独查询，两边互不拖累；第二斧，按月分段查询——FetchDescriptor 配上按月筛选的谓词，一次只取一个月的账；第三斧，汇总别在每次界面重算时都算一遍，records 变了才算一次、存住结果。第三斧涉及缓存计算结果，第 68 章讲架构时是现成例题。

把"先测量、再优化"记成习惯。感觉慢不等于真慢，Instruments 一测，多半会发现卡的不是数据库，是你顺手写在 body 里的某个重复计算——这类"性能问题"占了大半，而它们本来就不该出现。比如每次 body 重算都重新归堆分类、每次重绘都重新算汇总，这些顺手放进计算属性的活儿，列表一滚就跑成千上万遍。第 67 章的性能小清单会给你一套现成的测量动作，先把"感觉"变成"数字"，再决定动不动手。

#### 十、界面细节打磨：从"能用"到"顺手"的最后一层

功能齐了之后，App 的档次差在细节里。这一节攒了六条打磨清单，都不难，难的是知道要打磨。

<strong>第一条：间距交给系统</strong>。SwiftUI 的 VStack、HStack、padding 默认值本身就是一套设计体系，苹果调过。别到处写死魔法数字——十个视图里五个 spacing: 8、三个 spacing: 10、两个 spacing: 12，界面立刻显得"没商量过"。默认值能不动就不动，真要调，全项目统一一个值。

<strong>第二条：别把可点的东西做太小</strong>。系统组件（List 行、Button、toolbar）默认满足可点面积标准；自己画的小图标按钮要记得留 padding——图标只有点阵那么大，手指点不中，用户只会觉得"这按钮坏了"，不会觉得"是我没点准"。

<strong>第三条：动画白送的要接住，额外的要克制</strong>。List 增删行自带过渡动画，前提是你用 withAnimation 包住数据变更那一下——行了，插入的行会自己滑进来。别再往上叠：到处都动的界面显得慌张，动画只为"交代东西去哪了"服务，不为炫技服务。

<strong>第四条：图标用 SF Symbols</strong>。加号、日历、垃圾桶，系统图标库全有——Xcode 里搜含义就能找到，自动适配粗细和深浅色。自己找 PNG 贴图标是最后手段：深色模式下白底图标会变成一块白斑。

<strong>第五条：手感清单</strong>。把这几条贴在便签上，每完成一个页面就过一遍：进页有焦点（自动聚焦第一个要填的框）、保存有关窗反馈、删除有撤销、空态有引导、错误有出口。这五条全过，界面就从"能交作业"变成"愿意天天用"。

<strong>第六条：真机过手感</strong>。模拟器摸不出"跟手"——滚动惯性、触感、键盘弹出节奏，都得真机才知道。每隔两三天把 App 在真机上从头滚到尾一遍，别攒到最后。

细节不是第一天全做完，是每天按清单过一遍。打磨这层的正确心态：你不是在"装修"，你是在替未来的用户省去每一次皱眉。

#### 十一、数据校验进阶：把规则写成测试

第四节给金额立了三道关，但规则写出来不等于守得住——三个月后你改 add 的实现，谁知道还能不能拦住负数？把校验规则固化成测试，规则就长在了代码里。

先列非法输入矩阵，每一种都是一个测试用例：

- 空字符串——add 应拒绝；
- "abc"——转不出数，应拒绝；
- "0" 与 "-5"——非正数，应拒绝；
- "1.2.3"——解析失败，应拒绝；
- 夹全角字符或空格的"１２３ "——解析失败或异常值，应拒绝；
- 正常的"12.5"——应通过且入库金额一致。

测试写起来很短，拿第一节那条内存容器的思路套：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 校验规则测试</span><span class="dots">···</span>
:::

```
func testRejectsInvalidAmount() throws {
    let config = ModelConfiguration(isStoredInMemoryOnly: true)
    let container = try ModelContainer(for: Record.self,
                                       configurations: config)
    let vm = RecordViewModel(context: ModelContext(container))

    let ok = vm.add(type: "expense", amount: -5,
                    category: "测试", note: "")

    XCTAssertFalse(ok)                       // 拒绝了
    XCTAssertTrue(vm.records.isEmpty)        // 而且没入库
}
```
:::

能这么测，靠的还是分家：校验规则全住在 ViewModel 里，测试直接调方法就能打中，不用点界面。哪天有人（包括三个月后的你）把 guard 改掉了，测试当场变红——规则被机器看着，比被脑子记着可靠。

#### 十二、FAQ：动手这一周，你真的会问出口的问题

<strong>问：每天只有两小时，这项目要拖多久？</strong>

答：每天两小时、每周五天的节奏，两周能到验收。别按"日历周"焦虑——正文说一周完成，指的是全职强度；碎片时间的正确预期是"每步都能用"，就算卡在第四步，手里也已经握着半个能用的 App。要防的不是慢，是停：哪天实在没状态，就只做五分钟——把前一天的代码跑起来、看一眼、提交一次，链条不断，你照样毕业。

<strong>问：我就不想搞 MVVM，逻辑直接写在界面里，行不行？</strong>

答：第一个版本真的行。但统计页一出现，你就得在两个页面之间复制逻辑；第三处出现时，你会自己回来重构的——这话不是吓你，是几乎每个走过的人的共同经历。分家早做是十分钟的事，晚做是半天的手术。

<strong>问：SwiftData 和 Core Data 什么关系？网上教程好多都是 Core Data 的。</strong>

答：SwiftData 是苹果新一代的持久化框架，与 Core Data 底层一脉相承。Core Data 教程里的概念——实体、关系、迁移——大多能平移过来理解，但 API 别照抄，两代写法差别不小。搜资料时记得带上 SwiftData 这个词，不然容易掉进老教程的坑。

<strong>问：为什么模型必须是 class？我 struct 用得很顺手。</strong>

答：SwiftData 需要引用语义——框架要跟踪同一个对象的增删改查；struct 一赋值就复制一份，框架没法跟踪。@Model 宏也只能贴在 class 上。这不是设计洁癖，是持久化的现实需要。

<strong>问：能不能让 AI 直接把整个项目写完？</strong>

答：能跑通，但你会错过这一章真正要教的东西：数据怎么流动、状态怎么管理、错误怎么兜底。第 38 章讲 AI 编程时说过，拆解需求的活儿不能外包。折中方案：让 AI 生成，你逐行看懂再粘贴，看不懂的地方追问到懂——学东西的是"看懂"这个动作，不是"粘贴"。

<strong>问：以后想加个"账户"字段（现金/银行卡）麻烦吗？</strong>

答：不麻烦。模型里加一个带默认值的字段，录入弹窗加一个 Picker。简单的新增字段 SwiftData 通常能自动处理迁移；复杂的模型改动才需要写迁移方案，以官方文档为准。动手前 git commit 一次，改砸了能退回来。

<strong>问：模拟器和真机，我该用哪个开发？</strong>

答：日常写代码用模拟器，快、省事、能随便重启。记账本几乎不碰传感器，模拟器覆盖面很够；但每周在真机上跑一次，交付前必须真机过一遍——键盘、深色模式、动态字体这些细节两边并不总一样。

<strong>问：我在模拟器里记的账，真机上能看到吗？</strong>

答：看不到。模拟器和真机是两个独立的沙盒，数据各存各的。想搬家就做第十六节的导出练习（发给自己邮箱再导入），或者按进阶挑战二上 iCloud——练手阶段最省心的办法其实是：把真机当唯一的"正式账本"，模拟器只跑测试数据。

<strong>问：为什么我改了模型字段，老数据全没了？</strong>

答：多半是迁移没做：改字段类型、删字段这类大动作，SwiftData 不一定认得怎么把老数据塞进新结构。轻量改动（新增带默认值的字段）通常没事，复杂改动要写迁移方案，以官方文档为准。另一种可能：你是删了 App 重装的——沙盒一清，数据自然归零。所以第二节才反复强调：先 commit 再改模型。

<strong>问：金额这个 Double 我现在用着挺开心，真要换吗？</strong>

答：练手阶段开心就好。哪天这个 App 转正了——比如全家开始真用——再动手换：以"分"为单位存 Int 或改用 Decimal，顺带写个小迁移把老数据换算一遍，半天能干完。知道自己哪天要换、为什么换，比现在就过度设计重要。

#### 十三、与安卓篇对照：同一本账，两种写法

第 54 章用 Kotlin + Compose + Room 做过一模一样的项目。把两章摆在一起读，你会发现一件神奇的事：架构思想完全通用，具体零件各有各的名字。下面这张表建议存下来，学另一端时对着找朋友。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">环节</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">本章（iOS）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">第 54 章（安卓）</th></tr></thead><tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">编程语言</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">界面框架</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI（声明式）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jetpack Compose（声明式）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数据层</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData @Model</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room @Entity + @Dao</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">查询写法</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">FetchDescriptor + 排序描述</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SQL 注解 @Query</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数据变界面</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Observable + @State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Flow + collectAsState</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">列表组件</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List + ForEach</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">LazyColumn + items</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">记一笔入口</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">导航栏加号 + sheet</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">悬浮按钮 + 弹窗</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">金额存储</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double（建议换"分"）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double（同样建议）</td></tr>
</tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
记账本项目两端对照

三处观念差异值得展开。其一，统计的位置：Room 版把"本月合计"写成 SQL，在数据库里算完才返回；本章把数据全取出来用 filter/reduce 在 Swift 里算。条数少时无所谓，数据量大了"让数据库算"更省——两种思路你都见过，选型时心里就有秤。其二，响应的来源：Room 的 Flow 是数据库级监听，表一有动静 Flow 自动吐新值；SwiftData 这边，模型属性一改，依赖它的视图自动刷新。殊途同归，都是"数据变，界面动"——这正是声明式 UI 的共同信仰。其三，主键与日期：Room 版显式声明自增主键、日期存字符串；SwiftData 版框架托管标识、日期是 Date 类型——后者做按月统计省了格式约定的心。

什么时候去学另一端？先把这一端吃透。概念一一对应之后，学第二端只需要三分之一的时间——你已经知道要学什么，只是在等一门新语法。顺便说一句，鸿蒙篇第 76 章的待办清单应用和本章同属"本地增删改查"项目，ArkTS 的声明式界面思路与 SwiftUI、Compose 一脉相通，学完本章去翻那一章，会有强烈的既视感。

#### 十四、场景实录：用自己写的 App 记一天账

写完不如用一天。给你一份"验收之外的实战记录"，主角是书友小周，App 是他刚做完的基础版。

早上八点零五，地铁闸机。扫码进站的瞬间他顺手点开 App：加号、输"4"、保存——三步，闸机响完提示音之前搞定。这里快，是因为第四节那些"少一次点击"的接线：默认支出、自动聚焦金额框、保存即关窗。中午十二点半，外卖 26.5，同样三步。下午三点想起昨晚看电影忘了记——点开昨天那笔的邻居，加号，金额 45，把日期往回拨一天，保存：补记账的 DatePicker 第一次派上用场，账落进了正确的日子。

晚上十一点半，他点开顶部汇总卡：本月支出比上个礼拜多了一截，大头是"购物"分类里两笔大额。他在其中一笔的备注里补了两个字"超支"，顺手把上周一笔重复记录的"打车 28"删掉（那天网络打卡失败他记了两遍——多选删除的快照修法也用上了）。合上手机，一分钟不到。

这一天里没有一个功能是"高级"的，但每个动作都顺手——这就是基础版该有的样子：功能不多，个个能用，天天会开。他后来在复盘笔记里只写了三行：记一笔快不快，取决于输入框自动聚焦；敢不敢删，取决于有没有撤销；看不看得清，取决于汇总卡三个数字。你自己的实战记录，大概率也长这样——用它，然后照着不顺手的地方改，这个 App 才真正开始属于你。

#### 十五、重构小课堂：把散落的逻辑收编回家

功能跑通之后，给你看一段"真实风格"的新手代码——它能用，但长了三只手：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 错误示范：删除逻辑写在界面里</span><span class="dots">···</span>
:::

```
// 列表行里：
.onDelete { idx in
    for i in idx {
        context.delete(records[i])   // 界面直接摸数据库
    }
    try? context.save()
}
```
:::

三个问题。其一，界面直接操作 context，分家没分干净——视图既画界面又管存储，跟谁都不打招呼。其二，删完没有 load()，别的视图不知道数据变了，而且它正是第八节那个"多选删除删错行"的近亲：绕开 ViewModel 的删除，下标和数组状态都不受控。其三，同样的删除规则哪天统计页也要用，就得再抄一遍。纠正版五分钟就能改完：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 纠正后：收编进 ViewModel</span><span class="dots">···</span>
:::

```
// ViewModel 里：
func delete(_ record: Record) {
    context.delete(record)
    try? context.save()
    load()
}

// 界面里只剩一句：
vm.delete(record)
```
:::

改动虽小，收益有三份：数据操作的规则只剩一份，改就改一处；界面更薄了——脱掉数据库知识，只留"转交动作"；删除逻辑进得了单元测试（直接调 vm.delete，不用点界面）。以后每写一段新逻辑就问自己一句：这段东西的家在哪儿？找不到现成的家，就给 ViewModel 盖一间。

#### 十六、扩展练习：给账本长出新肌肉

基础版验收通过就够毕业了。如果意犹未尽，下面六个练习按性价比排序，做完前两个就值回票价。

<strong>练习一：分类统计页（性价比之王）</strong>。步骤清单：① 新建统计视图，用 <code class="inline">Dictionary(grouping: by:)</code> 把本月支出按分类归堆求和；② 引入 Charts 画柱状图（第六节的代码直接抄）；③ 主界面套 TabView，统计页放第三个标签；④ 顶部加个月份切换，往上翻还能看上个月。做完它，账本就有了"复盘"能力。

<strong>练习二：导出与备份</strong>。把流水拼成 CSV 文本，用 SwiftUI 的 ShareLink 分享出去——发到自己邮箱就是异地备份，发到家庭群里就是"本月账单公示"。十几行代码：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 导出 CSV 并分享</span><span class="dots">···</span>
:::

```
let header = "日期,类型,分类,金额,备注"
let lines = vm.records.map {
    "\($0.date),\($0.type),\($0.category),\($0.amount),\($0.note)"
}
let csv = ([header] + lines).joined(separator: "\n")

ShareLink(item: csv,
          preview: SharePreview("我的账单.csv"))
```
:::

<strong>练习三：把"记一笔"压到三秒</strong>。默认选中支出（多数账是支出）、常用分类排最前、金额框自动聚焦、记住上一次用的分类（UserDefaults，第 64 章讲过）。记账 App 大多死于"记一笔太麻烦"，这三秒就是它的生命线。

<strong>练习四：搜索与筛选</strong>。列表页加 <code class="inline">.searchable</code>，按备注和分类过滤。别小看它——"那笔转账是哪天记的"是记账三个月后最高频的动作。

<strong>练习五：每周复盘仪式</strong>。技术上零代码：每周日晚上打开汇总卡，把最超预期的一笔在备注里做上标记。工具加仪式才等于习惯，这五分钟是整个项目里回报率最高的时间。

<strong>练习六：一条温柔的提醒</strong>。每晚固定时间问一句"今天的账记了吗"——本地通知就能做到，申请姿势和节制原则第 68 章细讲。提醒要克制：一天一条是上限，超过就成骚扰，用户会连 App 一起恨。

给你一张七天上手日历，照着走：第一天，工程骨架 + 数据层 + 重启验证；第二天，列表页 + RecordRow；第三天，录入弹窗 + 校验三道关；第四天，编辑、删除、汇总卡片；第五天，三层验收清单 + 两条单元测试；第六天，无障碍 + 深色模式过一遍，顺手开做练习一；第七天，真机全流程过一遍，git 提交打标，正式开始用它记账。

##### 做完之后：三段式复盘

不管做到哪个练习，停下来时给自己写三段话：做了什么（到哪一步、哪些过了验收）；卡在哪、怎么解的（把报错和当时的猜测记下来）；下次提前做什么（比如"动手前先 commit""数据层当天验"）。存进备忘录，或跟着 git 提交一起留档。这个习惯从第一个项目就开始养——第 67 章讲发布复盘时用的就是同一套格式，练过的手到那时不慌。

最后一句提醒：练习做到第二个就该见好就收，把时间还给记账本身——真用一周，比再改十版都涨经验。下一个项目（第 66 章的天气 App）会把你的手艺从"单机"带进"联网"世界：API、JSON、三态界面，全都在那儿等你。

<strong>问：我想给 App 换个名字、配个图标，现在能做吗？</strong>

答：能，但先忍住。显示名在 target 设置里改一个词就行，图标需要一张 1024 尺寸的正方形图放进 Assets（素材怎么做，第 67 章上架一节细讲）。这两件事属于"最后 10% 的活儿"——功能没稳之前折腾外观，是小林同学第一天犯过的错，别重蹈覆辙。

#### 十七、给三类读者的定制建议

同一本账，不同的人卡在不同的地方。三类常见读者，各给一份对症的用法建议，对号入座。

<strong>学生党</strong>：你的痛点是"钱不多，更得看清楚"。分类别贪多——吃饭、交通、学习、娱乐四类足够，分类越少，记一笔越快，越容易坚持。练习一做好之后，把统计页当成每月的"生活费体检"：月初看一眼上月的四根柱子，哪根冒头心里就有数了。另外一个容易被忽略的点：这个练手项目就是你最早的作品集——作业质量的代码，找实习时也是拿得出手的谈资，认真写注释、认真提交，就是在给半年后的自己铺路。

<strong>上班族</strong>：你的痛点是"根本没时间记"。把练习三做满：默认支出、自动聚焦、记住上次分类，通勤电梯里的三十秒就够记一笔。再给自己立一条成本低到不会失效的规则——超过某个金额的消费当天必记，小额零头周末统一补。别追求"笔笔不漏"，记账的敌人从来不是漏记，是嫌麻烦之后彻底放弃。

<strong>想拉爸妈一起用的</strong>：你的 App 是现成的适老化练兵场。字号交给动态字体（第六节无障碍已经埋好底）、分类精简到六七个、删除必配撤销（第五节的后悔药正好派上用场）。第一次远程教的时候，只教"记一笔"这一个动作，教会就收手——一天教五个功能的结果是一个都记不住。第 27 章的适老化原则，在自己写的 App 里练一遍，比读三遍都管用。

到这里，你已经完整走完了一遍"想清楚 → 建数据 → 分逻辑 → 画界面 → 兜错误 → 验收"的全流程——这套流程本身就是这一章最大的产出，比记账本这个 App 值钱。下一章，我们把同一套手艺放进网络世界：你的 App 第一次和远方的服务器说话，学会申请 API、解析 JSON、在"加载中/成功/失败"三种状态下都体面。带上你的账本，第 66 章见。

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 需求五要素 → 拆成"每步能用"的小步骤，再动手
- 数据层：@Model 模型 + modelContainer 容器 + FetchDescriptor 查询
- MVVM 分工：View 只管画，@Observable 的 ViewModel 管逻辑，SwiftData 管存储
- 界面：List + Section + toolbar + sheet 录入弹窗
- 三层验收（功能/边界/架构）+ 进阶挑战（Swift Charts、iCloud 同步）
- 从演示到能用：金额存整数或 Decimal、空状态引导、无障碍、两条单元测试
:::
