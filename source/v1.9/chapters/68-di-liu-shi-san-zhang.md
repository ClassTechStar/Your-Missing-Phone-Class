---
id: di-liu-shi-san-zhang
num: 63
part: ios-kai-fa-pian
nav: 第六十三章：视图、状态与导航
toc: default
kind: chapter
---

### 第六十三章：视图、状态与导航

{class="chapter-intro mb-4"}
单页面的玩具已经会做了。这一章解决两个"长大"问题：怎么在多个页面之间跳来跳去（导航），以及数据在页面之间怎么流动（状态管理）。学完本章，你就能搭出"列表 → 详情 → 编辑"这种经典的多页面 App 骨架。

::: div .quick-read
##### 本章速读（5 分钟版）
单页面的玩具你已经会做了，这一章解决两个"长大"的问题：页面之间怎么跳来跳去（导航），数据在页面之间怎么流动（状态管理）。学完你就能搭出"列表、详情、编辑"这种经典的多页面 App 骨架，手机上大多数正经 App，骨架都是这一条。这一章的内容也是你以后验收 AI 界面代码的清单，值得慢一点嚼透。

最关键的有两件事。第一，把状态四件套的分工记清：<strong>@State 管页面私有的临时状态，@Binding 借别人的状态来改，@Observable 模型管跨页面的业务逻辑，.environment 管全局共享</strong>（登录态、主题这类）。新项目用 @Observable 宏写视图模型，老教程的 @ObservableObject 能读懂就行。三条纪律收好：状态私藏、来源唯一、能现算的别存。第二，导航口诀是"主流程推页面、临时操作弹 sheet、并列大块用 TabView"：推页面交给 NavigationStack 这个"栈"，传参走值、保存完要自动退出就用 dismiss，别用一堆布尔开关冒充导航，十几个 isPresented 满天飞，谁也说不清用户在第几层。表单那节还有两条实用规矩：输入时抓格式、保存时抓规则，别在用户敲第一个字时就报"手机号不合法"；键盘弹出别挡住正在填的输入框，填完即走是舒服的底线。

今天就能做的最小动作：跟着章里"动手十分钟"，把上一章那个静态页面改成"活的"，状态接上、按钮有反应；再花十分钟搭一条"列表到详情到编辑"的三层导航链。做完拿一张常用 App 的截图试着拆它的骨架：哪里是栈、哪里是弹窗、哪里是标签页，这个"拆骨架"的思维训练，比多写一百行代码值钱。

最大的坑全是"当下能跑，两周后疼"。把几百条记录塞进 @State 数组，状态只活在内存里，App 一重启全归零，要跨启动得用下一章的数据库；把主题、账目、网络全塞进一个大模型。任何一处改动惊动半个界面，按业务拆小，别造"上帝对象"；在 body 里发请求、做排序：界面每刷新一次就重干一遍，重活放 .task 或模型方法里，body 只管画图。指挥 AI 写这类代码也一样：先答清"状态住哪、谁有权改、要不要跨启动"，验收时盯住 body 里的重活、存两份的数据、和布尔值导航这三处。
##### 速查表
- 状态怎么分工：@State 页面私有、@Binding 借用、@Observable 管逻辑、.environment 管全局
- 状态三纪律：私藏、独源、现算，能现算的别单独存
- 页面怎么跳：NavigationStack 推页面，保存完用 dismiss 自动退出
- 什么用栈什么弹窗：主流程推页面、临时操作弹 sheet、并列大块用 TabView
- 列表怎么写：List 加 ForEach，id 要稳、行要轻，滑动删除开箱即用
- 切后台回来状态没了：@State 只活内存，要跨启动的数据交给数据库
- body 的红线：别在 body 里发请求、排序干重活，重活放 .task 里
- 怎么指挥 AI 写界面：先答"状态住哪、谁有权改、要不要跨启动"再下指令
:::

<div class="version-anchor">本章界面路径按 iOS 18.x / HarmonyOS 5.x / Android 15 核对（2026 年 11 月）。你的机型或系统版本不同，菜单名字和位置可能对不上——以你手机上显示的为准。</div>


#### 一、状态管理的"数据流全景"

SwiftUI 的状态工具不止 @State 一个。先看这张全景图，搞懂"什么时候用哪个"：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">工具</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">管什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">谁来用</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">典型场景</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">页面私有的临时状态</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">当前视图</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">计数器、输入框文字</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Binding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">借用别人的状态</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">子视图改父视图</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自定义组件</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@StateObject / @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跨页面共享的逻辑</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">视图模型（ViewModel）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数据加载、业务逻辑</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@EnvironmentObject / .environment</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全局共享的状态</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">整个 App</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用户登录态、主题设置</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
SwiftUI 状态工具全景（2026 年，@Observable 已是主流）

::: div .code-block
:::inline div .code-head
<span>SWIFT · 2026 主流：@Observable 视图模型</span><span class="dots">···</span>
:::

```
// iOS 17+ 的现代写法：@Observable 宏（推荐新项目使用）
import Observation

@Observable
class CounterModel {                 // 视图模型
    var count = 0
    func increment() { count += 1 }
}

struct CounterView: View {
    @State private var model = CounterModel()   // 持有模型

    var body: some View {
        VStack {
            Text("你点了 \(model.count) 次")
            Button("点我") { model.increment() }
        }
    }
}
```
:::

给新手的粗暴建议：<strong>页面私有的用 @State，跨页面/有逻辑的用 @Observable 类</strong>。老教程里的 @StateObject/@ObservableObject 是上一代写法，能读懂即可，新代码按上面来。

还有一条能少掉一堆 bug 的纪律：<strong>能由现有状态算出来的值，就现算，别再存一份</strong>。存两份，就得处理两份同步：这是最常见的 bug 来源。需要长期保存的结构化数据，则交给 SwiftData（下一章细讲），别硬塞进状态里。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">

<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">需求</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">优先选择</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要避免</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一个开关、一段输入</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">为了一个布尔值建全局模型</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多个页面共享一份数据</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Observable 模型</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">层层手动传参</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需要持久化的记录</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自己拼文件读写</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">页面跳转与返回</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">NavigationStack + 路径</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">到处塞 isPresented 布尔值</td></tr>
</tbody>
</table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Swift 6.2 时代的需求对照表：按需求找工具，顺带看清要躲的坑

##### 把全景图读出声：四行格子的人话版

表格是速查用的，这里把每一行翻成人话，读完你对号入座就不慌了。

- <strong>@State</strong>：这个页面的私房钱。只有这页看得见、只有这页改得动，页面销毁它就跟着没了。开关、输入框里的字、选中的标签，都归它。
- <strong>@Binding</strong>：借条。别人持有真状态，你拿一份可读可写的引用去用——你一改，真状态跟着变，持有者那边的界面也跟着刷。
- <strong>@Observable 类</strong>：工作台。跟界面无关的业务逻辑、跨页面的共享数据住在这里。视图只管"把模型里的东西摆出来 + 调模型的方法"。
- <strong>.environment</strong>：公共广播。全 App 都关心的东西（登录态、主题）放进去，任何页面随时收听，不用一层层传话。

四样东西不是"四个选项"。四样东西是"四层架构"：一个正经 App 通常四样都用——开关用 @State，自定义组件用 @Binding，业务逻辑进 @Observable，全局配置进 environment。选错的代价不是立刻报错，而是几周后项目变成一团乱麻。

##### 从"改界面"到"改状态"：一次真实的小重构

给你一个从命令式思维切换到声明式思维的真实例子。新手写"退出登录"，第一反应是："找到用户头像那个视图，把它换成'未登录'的样子。"于是到处找"怎么把某个视图删掉/替换掉"的 API——方向从一开始就歪了。声明式的正确姿势是：定义一个 isLoggedIn 状态，body 里写清楚"登录时显示头像，未登录显示登录按钮"，然后退出登录的动作只有一行：isLoggedIn = false。

界面怎么变，是 body 早就写好的剧本；你只负责改变量。这个思维转换是本章最大的坎，很多人卡两三天，想通了以后一路畅通。判断自己转没转过来有个土办法：当你想找"怎么让某个视图消失"的 API 时，停下来问一句"这个视图的存在依赖什么状态"，把状态改掉，视图自然就没了。

##### 状态不刷新？先从一个翻车现场说起

这张表看着头大？没关系，先用一个几乎人人踩过的坑把最底层的机制讲透。你照着第 62 章的样子搭了个计数器，但把 @State 忘了，写成了普通属性：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 反面教材：缺 @State 的计数器</span><span class="dots">···</span>
:::

```
struct BadCounterView: View {
    var count = 0                    // 少了 @State，埋雷

    var body: some View {
        VStack {
            Text("你点了 \(count) 次")
            Button("点我") {
                count += 1           // 改了，但界面纹丝不动
            }
        }
    }
}
```
:::

运行起来：按钮怎么点，数字都不动，编译器还不报错——这是最气人的一类 bug，不红不黄，就是不听话。原因藏在 SwiftUI 的心脏里：<strong>视图是"值"，不是"对象"</strong>。界面每次刷新，body 都会重新执行一遍，相当于重画一张快照；普通属性记不住上一次的值，框架也不知道你改过它。@State 的作用就是把这个值交给框架代管：值一变，框架把用到它的那块界面重新画出来。

把 var count 换成 @State private var count，再点，数字开始跳了。记住这个心智模型：<strong>你不是在"操作界面"，你是在"改状态，让框架替你重画界面"</strong>。想通这一层，后面所有工具都只是同一件事的不同用法。

##### @State 的三条纪律

工具上手之前，先立规矩。这三条纪律能帮你避开日后九成的状态 bug：

- <strong>写 private</strong>：@State private var 几乎是固定搭配。状态是页面的私事，开放给外部乱改，数据流很快搅成一锅粥。
- <strong>存"最小真状态"</strong>：只存真正会变、且没法现算的东西。全名能从账号信息里拼出来，就别再存一份"当前显示的全名"。
- <strong>初始值给默认</strong>：@State 的初始值在页面创建时就定死了，别指望"从外面传个新值进去它就跟着变"：那是 @Binding 的活。

顺带回答一个高频疑问：@State 里存 struct 还是存 class？存 struct（值类型）更安心——SwiftUI 对值类型的变更检测最灵敏，改一个字段，用到它的界面就跟着刷；存 class 时框架默认"看不见"内部变化，除非这个 class 标了 @Observable。拿不准就存 struct，需要共享行为时再升级成 @Observable 类。

##### @Binding：把"改的权力"借出去

场景来了：设置页里有一行"记账提醒"开关，你想把它做成可复用的自定义行组件。开关的"真状态"应该住在设置页（父视图），子组件只负责"显示 + 改"，这就轮到 @Binding 出场：

::: div .code-block
:::inline div .code-head
<span>SWIFT · ToggleRow 自定义开关行</span><span class="dots">···</span>
:::

```
struct ToggleRow: View {
    let title: String
    @Binding var isOn: Bool          // 借来的状态

    var body: some View {
        Toggle(title, isOn: $isOn)
            .padding()
    }
}

// 父视图里这样用：
struct SettingsView: View {
    @State private var notify = true

    var body: some View {
        ToggleRow(title: "记账提醒", isOn: $notify)   // $ 把引用递过去
    }
}
```
:::

盯住两个细节。子视图里 @Binding var isOn 用起来和普通变量一模一样，改它就是改父视图里那一份；父视图传值时要在变量名前加 <code class="inline">$</code>——$notify 的意思是"把 notify 打包成一份可读可写的引用递过去"。$ 这个符号你其实早就见过。第 62 章的 <code class="inline">TextField(text: $name)</code>，就是把 name 的可写引用借给输入框。你一打字，name 跟着变。

一句话记牢分工：<strong>@State 是"我拥有这个状态"，@Binding 是"我借用别人的状态"</strong>。拥有者永远只有一个，借用者可以有很多：一台电视可以配三个遥控器，但电视只有一台。

##### 视图模型：逻辑该住的地方

再回头看本章开头那个 CounterModel。把 count 和 increment() 搬出视图，好处不只是代码好看：视图变薄了，body 里只剩"摆界面"；逻辑集中了，想改计分规则只动一个文件；可测了，逻辑类不依赖界面，写两行断言就能验证对错。页面少的时候感觉不出来，三五个页面之后，所有逻辑挤在视图里的项目，改一行要通读整个文件，你就知道"薄视图"有多值钱。

那什么该搬进模型，什么该留下？给你一把粗糙但好用的尺子：<strong>跟"数据怎么变"有关的，搬进模型；跟"数据长什么样"有关的，留在视图</strong>。金额格式化、列表排序、要不要发提醒，归模型；颜色、字号、间距、动画，归视图。实在判断不了就问自己一句：这段代码换成命令行界面还成立吗？成立，就归模型。

模型里存什么也要挑。内存里的临时数据、请求状态（加载中/成功/失败）适合放；要关掉 App 还在的记录，别放，那是下一章 SwiftData 的地盘。模型不是仓库，是"工作台"。

##### 三平台对照：同一个思想，三套方言

你可能刚从第八篇的安卓实战篇过来，或者接下来打算去学鸿蒙。好消息是：SwiftUI、Jetpack Compose、ArkUI 三家都是"声明式界面 + 状态驱动刷新"，思想完全同源，只是方言不同。这张对照表帮你把三套词汇挂到同一棵概念树上：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">概念</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">SwiftUI（本章）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Jetpack Compose（第 51 章）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ArkUI（第 73 章）</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">页面私有状态</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">remember + mutableStateOf</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">父到子单向传值</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">普通 let 属性</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">普通参数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Prop</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">子改父（双向）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Binding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">状态提升 + 回调</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Link</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跨页面共享逻辑</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Observable 类</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ViewModel + StateFlow</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Observed + @ObjectLink</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">页面路由</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">NavigationStack</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">NavController + NavHost</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Navigation + 路由（第 74 章）</td></tr>
</tbody>
</table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
三平台状态管理对照（细节以各家官方文档为准）

提醒两句。这是思想地图，不是逐行翻译：名字对上了，行为细节仍有差异，比如 Compose 里忘了写 remember，症状和忘了 @State 一模一样：改了不动。也别用背单词的心态同时学三套：任何框架都逃不开三个问题<strong>状态住在哪里、谁有权改它、变化怎么通知界面</strong>。三问答清楚，换哪门方言都只是换措辞。

##### @Environment：框架替你保管的"公共设施"

还有一类状态你从来没声明过，却随时能用：深色模式开没开、当前语言是什么、App 在前台还是后台。这些由系统统一保管、随取随用的值叫环境值，取用姿势是 @Environment：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 读取深色模式</span><span class="dots">···</span>
:::

```
struct ThemeCard: View {
    @Environment(\.colorScheme) private var scheme

    var body: some View {
        Text(scheme == .dark ? "当前深色模式" : "当前浅色模式")
    }
}
```
:::

环境值不只是读系统设置，你还能把自己的对象放进去：在 App 入口用 <code class="inline">.environment()</code> 注入，任何子页面用 <code class="inline">@Environment</code> 取出来。这正是前面需求对照表里"全局共享"的官方通道，深层页面要用一份共享数据时，不用从根视图一层层当快递往下传，放进环境，谁要谁来取：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 自定义对象进环境</span><span class="dots">···</span>
:::

```
// 注入（App 入口或任意父视图）
WindowGroup {
    ContentView()
}
.environment(AppSettings())

// 任意子页面取出
@Environment(AppSettings.self) private var settings
```
:::

用的时候留个心眼：环境是"公共设施"，不是"储物间"。登录态、主题这类全局都关心的东西放进去；某个页面自己的临时数据别放：否则环境很快变成谁都不敢动的公共储物柜，放东西的人找不到，拿东西的人也找不到。

##### 动手十分钟：把第 62 章的页面改成"活的"

概念读完，手别闲着。打开第 62 章建的那个练手项目，按顺序做五个小动作，每个动作两分钟，做完你对"状态驱动界面"的理解会从"懂了"变成"信了"：

1. 给页面加一个 @State private var name = ""，再放一个 TextField("你的名字", text: $name)，输入框里打字，观察没有任何"刷新代码"，字就是进去了。
2. 加一个 @State private var isOn = false 和 Toggle("提醒我", isOn: $isOn)，点开关，看它自己会动。
3. 加一行 Text(isOn ? "已开启提醒" : "提醒已关闭")，开关一动，这行字自动跟着变，这就是"界面是状态的函数"。
4. 把 Toggle 换成你自己写的 ToggleRow（前面那段代码），体会 $ 引用跨组件传递。
5. 把 name 改成 @State private var name = "" 外加一个 @Observable 的 UserModel，把显示逻辑搬进去，同一个界面，两种架构，直观感受"薄视图"。

做完这五步，把模拟器和代码并排放着，改一个值看一次界面。这个"改状态 → 看界面"的循环，就是声明式 UI 的全部日常。

##### 三个小问答：数组、嵌套与"放哪一层"

<strong>问：数组用 @State 存，我改了数组里某个元素的属性，界面怎么没反应？</strong>答：这是经典坑。对 struct 数组，SwiftUI 靠"整个数组换了"来发现变化，你原地改一个元素的内部属性，它可能浑然不觉。稳妥做法是整个替换——先取出元素改好，再写回数组对应位置；或者让元素本身也用 @Observable 类。

<strong>问：@State 能存字典、存嵌套结构吗？</strong>答：能，SwiftUI 对常用的值类型都接得住。但嵌套越深，"哪一层变了、该刷哪一块"越难判断。经验是：状态扁平化——能用两个平级变量说清楚的，别包成一个大 struct。

<strong>问：状态到底放在哪一层？</strong>答：放在"所有需要读写它的页面的最近公共祖先"那里。只有一个页面用：放这页自己（@State）；父子都要用：放父页面，子页面 @Binding 借；隔了三四层：别传了，进 @Observable 模型或环境。放错层的症状很固定——某天你发现自己在一层一层往深里传参数，那就是该把状态上提的信号。

##### 状态代码的"坏味道"自查清单

代码不会说话，但有味道。闻到下面任何一种，就该停下来重构了，越早越便宜：

- <strong>同一名词多处存</strong>：用户名既在 @State 里，又在模型里，还在 UserDefaults 里——一份事实三处登记，改一处忘两处。找到唯一"真相源"，其余的都改成现算。
- <strong>参数越传越多</strong>：某个子视图要传七八个参数才能用，说明它想要的其实是一份共享模型，别硬传了。
- <strong>body 越写越长</strong>：一个 body 两百行，滚动条都嫌长。按块拆成子视图，顺便把"块与块之间的数据关系"看清楚。
- <strong>布尔值越堆越多</strong>：isLoading、isEmpty、isError、isRefreshing……组合起来几十种情况。考虑用一个枚举状态（加载中/成功/失败）一锤定音。

这四条不用背，写代码时心里有根弦就行。代码坏味道就像屋子里的杂物，每周顺手收一次，比年底大扫除轻松得多。

#### 二、NavigationStack：页面跳转的"栈"

iOS 16 起，多页面导航用 <strong>NavigationStack</strong>——像一摞盘子，推一个进一个，返回时逐个弹出：

::: div .code-block
:::inline div .code-head
<span>SWIFT · NavigationStack 导航</span><span class="dots">···</span>
:::

```
struct HomeView: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("张三的账本") {
                    DetailView(name: "张三的账本")   // 目标页面
                }
                NavigationLink("李四的账本") {
                    DetailView(name: "李四的账本")
                }
            }
            .navigationTitle("账本列表")   // 顶部大标题
        }
    }
}

struct DetailView: View {
    let name: String
    var body: some View {
        Text("\(name) 的详情页")
            .navigationTitle(name)
            .navigationBarTitleDisplayMode(.inline)
    }
}
```
:::

NavigationLink 就是"能点的跳转链接"；<code class="inline">navigationTitle</code> 自动生成导航栏标题和返回按钮。要<strong>编程式跳转</strong>（比如点完"保存"自动返回）时，用 <code class="inline">@Environment(\.dismiss)</code> 关闭当前页面，这两招配合，90% 的导航需求就齐了。

再往上一层是<strong>基于值的导航</strong>：给 NavigationStack 绑一个"路径"，把"当前在哪一页"变成可保存、可恢复的数据：程序重启后能回到原来的页面，深层链接也好接。入门阶段先用 NavigationLink，知道有这条路就行。

##### 栈：把"一摞盘子"讲透

把比喻展开：NavigationStack 管理一摞页面，手机屏幕永远只显示最顶上那张。从列表点进详情，是"推"：新盘子压上顶；点左上角返回，或者从屏幕左缘往右一滑，是"弹"，顶上的盘子端走，露出下面那张。你每天都在用的"返回"，本质就是弹盘子。

几层摞在一起也没关系，返回永远只退一层：列表 → 详情 → 编辑页，连退三次才回列表。左上角的返回按钮自带上一页的标题，右滑返回手势也是系统自带，这些"苹果味"细节不用你写一行代码，全是 NavigationStack 的标配。

顺手立一条审美纪律：盘子摞到三四层，就该想想是不是该换弹窗或标签页了。导航深到需要用户记住"我是怎么进来的"，通常说明信息架构出了问题，而不是用户记性差。

##### 传参的两种姿势

列表页要把"点了哪一项"告诉详情页，常见两种姿势。姿势一就是前面代码的写法：NavigationLink 的目标闭包里直接把参数递过去（DetailView(name: "张三的账本")），简单直观，适合固定入口和演示。

姿势二是<strong>基于值的导航</strong>：把"目的地"定义成一个值，跳转时把值塞进路径，由 NavigationStack 统一翻译成页面。入口一多、参数一复杂，这个写法的好处立刻显出来：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 基于值的导航</span><span class="dots">···</span>
:::

```
enum Page: Hashable {                 // 所有目的地列成清单
    case detail(name: String)
    case settings
}

struct BookListView: View {
    @State private var path: [Page] = []   // 路径就是个数组

    var body: some View {
        NavigationStack(path: $path) {
            List {
                NavigationLink(value: Page.detail(name: "张三的账本")) {
                    Text("张三的账本")
                }
                Button("去设置") { path.append(.settings) }   // 编程式推入
            }
            .navigationDestination(for: Page.self) { page in
                switch page {
                case .detail(let name): DetailView(name: name)
                case .settings:         SettingsView()
                }
            }
        }
    }
}
```
:::

看懂三处就懂了整套机制：Page 枚举把所有可去的目的地列成一张清单；NavigationLink(value:) 和 path.append 都是在"往路径里塞值"；navigationDestination 负责"见到这个值就造这个页面"。路径 path 本身是个普通数组，往里 append 是跳过去，删掉末尾是退回来，一次清空是回到根页面。"当前在哪一页"从看不见摸不着的界面状态，变成了可打印、可保存、可恢复的数组：这就是"把导航变成数据"。

##### 编程式返回：保存完自动退出

更多时候，返回不是用户点出来的。返回是你安排的：录入完一笔点"保存"，页面自动关掉；详情页点"删除"，自动退回列表。这叫编程式返回，主角是 dismiss：

::: div .code-block
:::inline div .code-head
<span>SWIFT · dismiss 编程式返回</span><span class="dots">···</span>
:::

```
struct EditSheet: View {
    @Environment(\.dismiss) private var dismiss
    @State private var title = ""

    var body: some View {
        Form {
            TextField("标题", text: $title)
            Button("保存") {
                // 先落袋，再关门
                dismiss()
            }
            .disabled(title.isEmpty)
        }
    }
}
```
:::

两个容易翻车的细节。一是顺序<strong>先把数据存好，再调 dismiss()</strong>。反过来的话页面先没了，用户以为存上了，其实数据还没落袋，这种"看起来成功了"的假保存，比崩溃还难查。二是 dismiss 只退一层，想把整摞盘子端走、直接回根页面，用前面讲的路径数组一次清空，别一层层 dismiss 连退五下。

##### 导航栏的花样：标题、工具栏与返回按钮

导航栏那一条横幅，能做的事比看上去多。标题你已经会了：navigationTitle 挂在哪一层，标题就显示在哪一层；列表页用系统大标题，详情页切内联小标题：原代码里的 <code class="inline">navigationBarTitleDisplayMode(.inline)</code> 干的就是这件事。

往导航栏上放按钮，用 toolbar 修饰符。记账本右上角那个"+"，就是这样来的：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 导航栏右上角放按钮</span><span class="dots">···</span>
:::

```
RecordListView()
    .toolbar {
        ToolbarItem(placement: .navigationBarTrailing) {
            Button {
                showAdd = true        // 触发弹录入 sheet
            } label: {
                Image(systemName: "plus")
            }
        }
    }
```
:::

返回按钮默认自带，一般别去动它。有些 App 会把返回按钮藏掉、换成自己的"关闭"，甚至拦住右滑手势防止误触——技术上都做得到，但每多一层自定义，用户的肌肉记忆就被打断一次。真要藏，先问自己：用户被关在这个页面里，出去的路在哪里？答不上来就别藏。

##### 三个高频导航翻车现场

导航的问题往往不报错，页面就是不跳、按钮就是没反应。三个最常见的现场，现象、原因、解法一次给齐：

- <strong>NavigationLink 点了没反应</strong>：九成是链接没"住"在栈里。NavigationStack 是车站，NavigationLink 是车票，没有车站，票作废。检查你的 NavigationLink 外面是不是包着 NavigationStack。
- <strong>标签页之间导航"串台"</strong>：TabView 的每个标签应该各配各的 NavigationStack。全 App 共用一个栈，切标签时页面互相干扰，会出现"我在统计页，怎么一退退回了账本页"的灵异事件。
- <strong>sheet 里想继续推页面推不动</strong>：弹出的 sheet 是一张白纸，里面默认没有栈。想在弹层里继续往下推（比如设置弹层里再进子页面），要在 sheet 的内容里再包一个 NavigationStack，栈可以套栈，各自管各自那一摞。

这三个现场覆盖了新手导航问题的绝大多数。下次卡住，先对着这三条查，别急着怀疑人生，更别急着重装 Xcode。

##### 推页面还是弹窗：一条实用的判断口诀

NavigationStack 和 sheet 都能展示一个新页面。新手常在两者之间纠结。给你一条口诀：<strong>走"流程"用推页面，办"一件事"用弹窗</strong>。看一条账目的来龙去脉是浏览流程，推页面；快速记一笔是办一件事，弹窗；一层层往深钻是流程，推页面；确认一下要不要删，是办一件事，弹窗。

还有个感官标准：需要返回键的页面，推出来；需要完成/取消按钮的页面，弹出来。推页面的心理预期是"我在往里走"，弹窗的心理预期是"我临时插了个队"。顺着用户的预期走，导航就顺；逆着预期走，用户就会在错误的时刻去够返回键。拿不准的时候，看看系统自带的邮件、备忘录、设置是怎么安排同类场景的，系统 App 就是最权威的交互规范。

##### 分步实操：十分钟搭一条"三层导航链"

光看不练等于没学。跟着下面六步，在练手项目里搭一条"列表 → 详情 → 设置"的导航链，每一步都写明你会看到什么：

1. 新建一个 SwiftUI View，命名 NavDemo，把整个 body 包进 NavigationStack，画布上暂时还是一张白纸。
2. 放一个 List，里面塞三个 NavigationLink("账户""隐私""关于")，目标先都指向同一个 PlaceholderPage()，运行，能看到三条可点的行。
3. 点任意一行，页面从右侧滑入，左上角自动出现"&lt; 返回"：你没写任何返回代码，这就是栈在工作。
4. 在 PlaceholderPage 里加 .navigationTitle("详情")，运行，标题变成内联小字。
5. 把 List 外面套上 .navigationTitle("设置中心")，运行，首页出现系统大标题。
6. 从屏幕左缘往右滑，页面跟着手指滑走，右滑返回手势天然可用，一条三层链完工。

这六步跑完，你顺带验证了本章最重要的判断：导航的基础设施系统已经全包了，你要做的只是"声明有哪些页面、从哪里能过去"。

##### 场景案例：账本详情页的一条完整动线

把栈、传参、编程式返回串成一条真实动线，看看它们在用户手里是怎么配合的。周五晚上十一点，你打开自己的记账本想看看这个月花了多少。

你点列表里"十一月"这一行——NavigationStack 把 DetailView 推上顶，参数 month: "十一月"一起递过去；详情页标题显示"十一月"，正文是这个月的分类汇总。你发现餐饮超支了，点右上角"调整预算"，又一个页面压上来，栈里现在是三层。改完预算点"保存"，页面调 dismiss() 自动退出，回到详情页，数字已经变了，因为预算存在共享模型里，两层页面读的是同一份。

你连退两次回到列表，列表页的分类汇总也跟着变了，同一个模型的另一面。全程没有一处"手动刷新界面"的代码：数据一变，看到它的页面各自重画。这一条动线，把本章前半章的每个工具都用了一遍。值得你在自己的练手项目里原样复刻。

##### 进阶：可保存、可恢复的导航路径

基于值的导航还有一层进阶玩法，先知道方向，等你做到需要它的项目再回来翻。前面说过，路径 path 是一个普通数组，数组是数据，数据就能持久化。让你的 Page 枚举遵守 Codable 协议，这个数组就能像普通数据一样存进 UserDefaults 或文件：用户上次停在哪个详情页，冷启动后恢复到哪个详情页。

另一路应用是深层链接：推送通知点进来，直接落到"十一月"的详情页，而不是冷冰冰的首页，写法就是往路径里 append 一个 Page.detail(name: "十一月")。把"界面在哪"变成"数据是什么"，这一转换是导航系统从"能用"到"好用"的分水岭。细节写法随项目而定，动手前先翻一遍官方文档里关于 NavigationStack 路径的部分。

入门阶段用不上这些很正常，先用闭包直传把页面跳通，等你的 App 有了"从通知直达"这类需求，再回头升级，成本也不高。

#### 三、弹窗与底部标签：sheet 与 TabView

除了"推页面"，还有两种经典交互：

::: div .code-block
:::inline div .code-head
<span>SWIFT · sheet 弹窗 + TabView 标签页</span><span class="dots">···</span>
:::

```
// 1. 底部弹出半屏/全屏（录入表单最爱）
struct HomeView: View {
    @State private var showAdd = false
    var body: some View {
        Button("记一笔") { showAdd = true }
            .sheet(isPresented: $showAdd) {
                AddRecordView()     // 弹出的录入页
            }
    }
}

// 2. 底部标签栏（App 的"骨架"）
struct MainTabView: View {
    var body: some View {
        TabView {
            RecordListView()
                .tabItem { Label("账本", systemImage: "book") }
            StatsView()
                .tabItem { Label("统计", systemImage: "chart.pie") }
            SettingsView()
                .tabItem { Label("设置", systemImage: "gear") }
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：什么时候用哪种？

{class="mt-1"}
经验法则：<strong>主流程用 NavigationStack 推页面（列表→详情），临时操作用 sheet 弹窗（新增、编辑、确认），并列的几大块用 TabView（底部标签）</strong>。三者组合，就是绝大多数 App 的骨架。
:::

##### sheet 的驱动方式：布尔开关与"选择项"

原代码里 sheet 用布尔值 isPresented 驱动，true 就弹，false 就收，这是最常用的写法。它有个兄弟写法是"绑定一个可选项"：点哪条记录就把它赋给 selectedRecord，sheet 直接展示这个记录，记录为 nil 时弹层自动收起。两种写法选一个顺手的用到底，别在同一段代码里混着来：两套开关并存，正是"页面关了状态没关"这类诡异 bug 的温床。

还有个新手必踩的小坑：sheet 挂在哪个视图上，就从哪个视图"头顶"滑出来。把 sheet 挂在 List 的某一行上，行滚出屏幕，弹层行为就变得怪异。规矩很简单：<strong>sheet 和 alert 一律挂在最外层容器上</strong>，别挂在行、按钮这类会消失的元素上。

##### 弹层里的数据流：进来一份拷贝，走时交回结果

录入 sheet 和父页面的关系值得专门说清。推荐的模式是：sheet 打开时拿到一份工作副本，用户在弹层里随便改，改的都是副本；点"保存"，把副本写回父页面（或模型）再 dismiss；点"取消"，副本直接扔掉，父页面毫发无损。这样"取消"才真的等于什么都没发生：用户反悔没有任何代价，也没有"改了一半的脏数据"留在界面上。

反过来，如果弹层直接 @Binding 改真数据，用户改到一半点了取消，真数据已经脏了——你再想恢复，就得自己写"撤销"逻辑，得不偿失。记住口诀：<strong>弹层里用副本，保存时才交卷</strong>。这个模式在表单类 App 里几乎处处适用，第 65 章的录入页就是这么写的。

##### TabView 的骨架设计：三个标签怎么分家

回到底部标签栏。标签数量三到五个最舒服：三个是"账本/统计/设置"这种经典三件套，四个可以加一个"我的"，五个到顶，再多就得左右滑动才能看全，不如砍掉一个。每个标签的标题用名词（"账本"），别用动词（"去记账"），标签是地点，不是动作。图标从系统图标库（SF Symbols）里挑，搜 book、gear 这类关键词，风格自动和系统对齐。

前面翻车现场提过，这里正式立规矩：<strong>每个标签内部各配各的 NavigationStack</strong>。记账本的骨架就是"TabView 三个标签，每个标签一个 NavigationStack，栈里推列表和详情，录入走 sheet"，三层结构定下来，整个 App 的骨架就不会跑偏。标签之间不共享导航栈，也就互不干扰：你在账本标签推到第三层，切到统计再切回来，账本标签还停在第三层，这是符合直觉的行为。

##### alert 与 confirmationDialog：确认类弹窗的正牌军

删除账目、清空数据这类不可逆操作，别拿 sheet 应付，系统正牌的确认弹窗是 alert（一两句话加按钮）和 confirmationDialog（从底部滑出的选项单）：

::: div .code-block
:::inline div .code-head
<span>SWIFT · alert 与 confirmationDialog</span><span class="dots">···</span>
:::

```
struct RecordRow: View {
    @State private var showDelete = false

    var body: some View {
        Button("删除这条账目") { showDelete = true }
            .alert("删除账目", isPresented: $showDelete) {
                Button("删除", role: .destructive) {
                    // 真正执行删除
                }
                Button("取消", role: .cancel) { }
            } message: {
                Text("删除后这条记录无法找回")
            }
    }
}
```
:::

两者的分工看选项数量：alert 适合"确定/取消"的二选一；confirmationDialog 适合三个以上选项的场合，比如"仅删这一条 / 删整个系列 / 取消"。文案别写"警告：您的操作将不可撤销！"这种威胁句式，把后果说清楚就行："删除后这条记录无法找回"一句话足够。role: .destructive 会自动把按钮染成红色，这是用户熟悉的"危险动作"信号，删数据的按钮记得带上。

##### fullScreenCover：需要整屏时才请出来

sheet 还有一位亲兄弟 fullScreenCover：一样从底部滑出，但盖满整屏，下滑手势默认关不掉。适合"必须走完"的流程，首次打开的引导页、全屏的相机取景、沉浸式的阅读页。请它出场前想清楚一件事：出口在哪里？没有明确出口的整屏弹层，和把用户锁进房间没什么区别；哪怕流程强制，右上角也要留一个"跳过"或"关闭"。

选择顺序记这条：默认想 sheet，半屏装不下或者必须全屏才升级 fullScreenCover。很多 App 的通病是把所有弹层都做成整屏，用户的"临时插队"被抬举成"换了间屋子"，进出的心理成本全变了。

##### 场景案例：给记账本定骨架

把本章三样工具合到一张图上。你闭上眼过一遍用户的动线：打开 App，落在"账本"标签（TabView），看到本月账目列表（List + NavigationStack），点一条进详情（推页面）。右上角"+"弹录入表单（sheet），保存后自动关掉（dismiss），切到"统计"标签看图表，再切到"设置"改提醒开关（TabView 切换，各自的栈互不打扰）。

这条动线覆盖了九成的日常使用。动手写代码前，先在纸上画出这条线，标出每一站用哪个工具——花五分钟画图，能省掉半小时"怎么又跳错了"的调试。骨架先通、血肉后填，这正是第 65 章项目的施工顺序：先搭一个假数据的骨架，再往里填真数据。

#### 四、List：iOS 的"国民列表"

iOS 上最常用、最有"苹果味"的组件就是 <strong>List</strong>——天然带分割线、滑动删除、点击高亮：

::: div .code-block
:::inline div .code-head
<span>SWIFT · List 列表 + 滑动删除</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var records = ["午饭 25.5", "地铁 6.0", "工资 +8000"]

    var body: some View {
        List {
            ForEach(records, id: \.self) { r in
                Text(r)
            }
            .onDelete { indexSet in          // 左滑删除
                records.remove(atOffsets: indexSet)
            }
        }
    }
}
```
:::

列表 + NavigationLink + sheet + TabView：把这四样组合起来，你已经能搭出"账本列表 → 点开详情 → 点+弹录入"的完整 App 骨架了。下一章的记账本项目，就是这么搭的。

##### List 与 ForEach：容器和模具的分工

List 是容器，ForEach 是"把数组摊平成一排排内容"的模具，两者配合但分工清楚。原代码里 <code class="inline">ForEach(records, id: \.self)</code> 的 id: \.self，意思是"拿每个元素自己当身份牌"，框架靠它分清哪行是哪行、增删时该动哪里。更正规的做法是让数据类型实现 Identifiable 协议，自带一个 id 字段：

::: div .code-block
:::inline div .code-head
<span>SWIFT · Identifiable 数据类型</span><span class="dots">···</span>
:::

```
struct Record: Identifiable {
    let id = UUID()          // 身份牌，全局唯一
    let title: String        // "午饭"
    let amount: Double       // 25.5
}

struct RecordListView: View {
    @State private var records: [Record] = [
        Record(title: "午饭", amount: 25.5),
        Record(title: "地铁", amount: 6.0)
    ]

    var body: some View {
        List(records) { r in                 // 有 id，不用再写 id: \.self
            Text("\(r.title) \(r.amount)")
        }
    }
}
```
:::

有了稳定身份，滑动删除才删得准：你删的是"第三条"还是"那条午饭账"，在数据一变界面就重算的世界里，全靠身份牌对号入座。用 UUID 或数据库主键当 id 都行，唯独别用数组下标，数组一增删，下标全体错位，界面就会出现"删了 A 结果 B 消失了"的灵异事件。

##### 滑动操作全家桶：删除、排序与侧滑按钮

左滑删除是默认技能，还有两样常用的：长按拖动排序（onMove）和自定义侧滑按钮（swipeActions）。账本里的"置顶""收藏"，就适合做成侧滑按钮：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 侧滑按钮与拖动排序</span><span class="dots">···</span>
:::

```
List {
    ForEach(records) { r in
        RecordRow(record: r)
    }
    .onMove { source, destination in        // 长按拖动排序
        records.move(fromOffsets: source, toOffset: destination)
    }
    .swipeActions {
        Button("置顶") { /* 置顶逻辑 */ }
            .tint(.gray)
        Button("删除", role: .destructive) { /* 删除逻辑 */ }
    }
}
```
:::

侧滑按钮的摆放有个约定俗成：破坏性操作（删除）默认在右边配红色，常用操作（置顶、收藏）放左边配灰色或主题色。用户在系统邮件 App 里养成的手感，到你 App 里最好原样保留。别让用户在你的列表里重新学一遍侧滑。另外 onMove 排序的顺序只改了内存里的数组，要"下次打开还是这个顺序"，得把新顺序存起来——存哪儿，下一章揭晓。

##### 分组、节头与搜索

账目一多，一锅炖就该改分组了。Section 给列表加节头，配上 insetGrouped 列表样式，立刻就是你熟悉的"设置 App"那种圆角分组卡片；再叠一个 searchable，导航栏下方自动长出系统样式的搜索框：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 分组与搜索</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var searchText = ""
    @State private var records: [Record] = []

    var body: some View {
        List {
            Section("今天") {
                ForEach(todayRecords) { RecordRow(record: $0) }
            }
            Section("昨天") {
                ForEach(yesterdayRecords) { RecordRow(record: $0) }
            }
        }
        .listStyle(.insetGrouped)
        .searchable(text: $searchText, prompt: "搜账目或备注")
    }
}
```
:::

searchText 一变，你按它过滤数据源，列表自动跟着变，又是"改状态、看界面"。列表、分组、搜索三件套搭起来，账本页就有了"正规军"的成色；实现成本加起来不到二十行代码。这都是 List 这个"国民组件"的福利。

##### 一行账目长什么样：行内布局练手

列表行就是普通 SwiftUI 视图，想怎么摆就怎么摆。一行账目的经典布局：左边图标和标题，右边金额靠右对齐，支出红色、收入绿色：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 一行账目的布局</span><span class="dots">···</span>
:::

```
struct RecordRow: View {
    let record: Record

    var body: some View {
        HStack {
            Image(systemName: record.icon)
                .foregroundStyle(.secondary)
            VStack(alignment: .leading) {
                Text(record.title)
                Text(record.note)
                    .font(.caption)
                    .foregroundStyle(.secondary)
            }
            Spacer()
            Text(record.amount, format: .currency(code: "CNY"))
                .foregroundStyle(record.amount >= 0 ? .green : .primary)
        }
    }
}
```
:::

第 62 章学的布局三件套（VStack/HStack/ZStack）在这里全部派上用场。给每行做"主标题 + 小字备注"的两层结构，比一行塞太多信息更耐看，列表是扫视用的，不是阅读用的。

##### 空状态与下拉刷新

列表还有两种状态值得专门伺候：空和旧。空状态，用户第一次打开，账本里一条记录都没有，别留一片白，告诉用户"还没有账目，点右上角 + 记第一笔"；iOS 17 起系统提供了现成的空状态视图（ContentUnavailableView），一行代码画出占位图加说明文字。旧状态，数据在云端时，加一个 refreshable 修饰符，用户下拉列表触发你写的数据更新，比自动轮询体贴得多：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 下拉刷新</span><span class="dots">···</span>
:::

```
List { /* 行内容 */ }
    .refreshable {
        await loadRecords()      // 下拉时执行，转圈自动消失
    }
```
:::

这两个状态的共同精神：别让用户对着一片空白发呆。界面每多一种"状态"，就多一句该说的话。写完列表页，把空、加载、错误、正常四种状态各跑一遍，是每个列表页交付前的例行检查。

##### 性能小节：id 要稳，行要轻

列表一旦上了几百条，两个性能习惯就开始值钱。第一个：id 要稳定：每行的身份牌从头到尾不变，别用会变的值（下标、随机数）当 id，否则框架分不清谁是谁，该复用的行不复用，滚动就开始卡。第二个：行要轻：每行的 body 里别做排序、过滤、日期格式化这类计算，进列表前把数据收拾好，行里只管摆出来。一条账目行两次 Text 加一个图标就够了，别在行里塞嵌套 List 或动辄十几层嵌套的布局。

真遇到大列表卡顿，优化方向按顺序来：先查 id，再查行内计算，最后才考虑换工具。多数"列表卡"的元凶是新手在行 body 里调了一个又调一个的格式化函数——把它挪到数据层，一次算好存起来，卡顿就消失了大半。

##### 场景案例：一次"删除错行"的排查过程

给你一段真实的排查复盘，体会 id 有多重要。某天你的列表出现灵异现象：想删"地铁 6.0"，左滑删除后消失的却是"工资 +8000"。钱和记录对不上，这种 bug 用户会立刻发现。

排查过程：第一步检查删除代码，onDelete 里 remove(atOffsets:) 没写错；第二步检查数据源，发现 records 用的是 id: \.self，而元素是 String，字符串当身份牌，两条内容相同的记录就撞牌了。第三步确认现场：列表里恰好有两条都是"午饭 25.5"的记录，框架靠字符串分不清它们，增删时对错了行。修复：换成带 UUID 的 Record 结构体（本节前面的写法），问题消失。

复盘的教训就一句：<strong>身份牌必须独一无二</strong>。这一类"界面和数据对不上"的问题，八成查到最后都是 id 的锅。下次遇到，先看 id，再看别的。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：搭一个"三页骨架"

#### 五、程序生命周期：前台与后台

和安卓的 Activity 生命周期类似，iOS App 也有"出生、前台、后台、死亡"的状态变化。SwiftUI 里用 <code class="inline">scenePhase</code> 环境值观察：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 观察前台/后台切换</span><span class="dots">···</span>
:::

```
@main
struct MyApp: App {
    @Environment(\.scenePhase) private var phase

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .onChange(of: phase) { _, newPhase in
            switch newPhase {
            case .active:    print("回到前台，恢复刷新")
            case .inactive:  print("过渡中（来电/切后台瞬间）")
            case .background: print("进后台，保存草稿")
            @unknown default: break
            }
        }
    }
}
```
:::

典型用途：<strong>回前台时刷新数据，进后台时保存草稿</strong>。iOS 对后台运行管得很严：普通 App 进后台后很快被挂起（冻结），别指望在后台偷偷干重活；真要定时任务，用第 68 章的本地通知，而不是"后台常驻"。也正因为系统随时可能回收 App，界面重新出现时要能正确重建状态，别依赖"它一直没被销毁"。

##### 三态各自的活：别把过渡态当后台

原代码里三个状态摆在一起了，这里把每态该干的活掰开说。.active 是正常使用中，该干嘛干嘛；.inactive 是"过渡态"：来电话、下拉通知栏、进入多任务界面的那一瞬间，App 还看得见但不接收触摸了；.background 才是真后台。把过渡态当后台处理是常见误判：用户只是下拉看了一眼通知就回来，你却在这零点几秒里存盘、停动画、掐定时器，回来时界面一脸懵。<strong>过渡态只做轻动作，重活留给 background</strong>。

还有个方向别搞反：scenePhase 在 App 级监听（挂在 WindowGroup 上），管的是全局；单个页面的进出场另有对应的事件。分不清时就问自己：这件事是"整个 App 该知道的"还是"这一页该知道的"？前者上 App 级，后者留页面级。

##### 场景案例：记账本的"后台存草稿"

具体到记账本：用户录到一半，金额输完、分类选好：一个电话进来把 App 压到后台。没做处理的 App，等用户接完电话回来，表单可能被系统回收重建成一张白纸：半小时的心情和那笔 38.5 元的午饭就这么没了。正确姿势是监听 scenePhase：一进 .inactive 或 .background，立刻把表单里未提交的内容存成草稿；回到 .active 时读回来，原样填上。用户全程无感，但数据一条没丢。

这种"用户没注意到才算成功"的细节，正是 App 和玩具的分界线。草稿怎么存能撑过 App 被杀？答案要等下一章的持久化：但你可以在搭骨架时就先把"该存草稿了"的钩子留好，第 65 章往里填存取逻辑就行。

##### 常见疑问：切后台再回来，@State 为什么全没了？

有人会碰到更彻底的情况：App 压后台几分钟，回来时界面整个重置，@State 存的东西全丢了。这不是 scenePhase 的锅。这是系统把 App 挂起后、内存紧张时<strong>直接终止了进程</strong>——再打开就是一次全新启动，内存里的一切自然清零。这正好呼应了前面那句"别依赖它一直没被销毁"。

应对思路分两步：能重建的状态，别手存，用 @State 加默认值，让框架重建；不能丢的状态（用户填了一半的表单、当前停在哪个页面），在进后台的时机主动落到磁盘。这条分界线，正好是本章（内存状态）和下一章（持久化）的分工图，两边各管一半，拼起来才完整。

{class="mt-1"}
做一个假数据版本的记账本骨架：TabView 三个标签（账本/统计/设置）→ 账本页用 List 显示假数据、点行跳详情（NavigationStack）→ 右上角"+"按钮弹录入 sheet。不存数据、不联网，纯练骨架，这个骨架做好，第 65 章往里填真数据就是水到渠成。
:::

#### 六、表单输入与验证：让用户填得舒服

导航搭好、列表能滑，还差一样高频场景：让用户填东西。记账本要录金额和分类，天气 App 要输城市，设置页要改昵称——SwiftUI 给表单准备了现成容器 <strong>Form</strong>：长得像设置 App 的分组列表，自带节奏和间距：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 录入一笔账目的表单</span><span class="dots">···</span>
:::

```
struct AddRecordView: View {
    @State private var amountText = ""
    @State private var category = "餐饮"
    @State private var note = ""

    let categories = ["餐饮", "交通", "购物", "娱乐"]

    var body: some View {
        Form {
            Section("金额") {
                TextField("0.00", text: $amountText)
                    .keyboardType(.decimalPad)       // 数字键盘
            }
            Section("分类") {
                Picker("分类", selection: $category) {
                    ForEach(categories, id: \.self) { Text($0) }
                }
            }
            Section("备注") {
                TextField("选填", text: $note)
            }
        }
    }
}
```
:::

Form 里的行会自动排成系统样式的分组卡片，Section 就是节头。字段顺序有讲究：必填的放最上面（金额），选填的放最下面（备注）——用户填不完也可以先保存。敏感信息用 SecureField（密码），单选用 Picker，开关用 Toggle，数量用 Stepper，都是现成控件，别自己画。

##### 键盘、焦点与"填完即走"

表单的手感藏在细节里：金额栏给数字键盘（keyboardType(.decimalPad)），别让用户在九键全键盘里找数字；备注栏的回车键设成"完成"（submitLabel），点一下顺便收起键盘；想让"填完金额自动跳到分类"，用 @FocusState 管理焦点流转，哪个字段该聚焦，写成状态，字段一填完就切焦点。这些东西加起来不超过十行代码，但"这个 App 用着真顺"的评价，一半是它们挣来的。

还有一条容易忽略：键盘弹出来会盖住下半屏表单。SwiftUI 的 Form 默认会自动把正在编辑的行顶到键盘上方，一般不用你操心；但如果表单底部有"保存"按钮，记得验证一下键盘弹起时按钮还能不能点到，真机上手测一次，胜过猜十次。

##### 验证的时机：输入时抓格式，保存时抓规则

验证分两道岗。第一道在输入时：金额栏只放行数字，粘贴进来带了字母就当场拦下，别让错误数据流进下一关。第二道在点保存时：逐项检查业务规则。金额不能为空、不能是负数、分类必须选了。两道岗各司其职，<strong>输入时抓"格式"，保存时抓"规则"</strong>，别把所有检查都堆到最后一刻。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 校验不过就灰掉保存按钮</span><span class="dots">···</span>
:::

```
// 金额合法：能转成数字且大于 0
var amountIsValid: Bool {
    (Double(amountText) ?? 0) > 0
}

Button("保存") {
    // 校验通过才走到这里，放心保存
}
.disabled(!amountIsValid)
```
:::

报错的方式也有讲究：行内红字比弹窗好。哪个字段错了，就在那个字段下面用一行红字说人话："金额不能为空"，而不是弹一个"输入有误"把人打回原地。弹窗是最后手段，不是第一反应；用户填错本是常态，好的表单把纠错成本降到最低。

##### 表单的五个人机细节，逐条过一遍

表单好不好用，全在细节。下面五条是新手最容易漏的，写完表单照着核对一遍：

- <strong>占位文字别当标签用</strong>：一旦用户开始输入，占位文字就消失了，用户不知道这个框本来问的是什么。正式标签用 Section 节头或字段左侧的固定文字，占位只放示例（"0.00""选填"）。
- <strong>必填和选填要分开</strong>：选填字段标注"选填"，别让用户以为每一格都必须填，填不完就保存不了。
- <strong>数字输入要温柔</strong>：金额栏用数字键盘之外，再容错一下全角数字和小数点：用户会用中文输入法打出"２５"这种全角字符，转换一下再存。
- <strong>失败不丢内容</strong>：保存失败（比如断网）时，表单里填的东西一条都不能少。清空表单等于把用户的工作扔进垃圾桶。
- <strong>成功要看得见</strong>：保存成功后关掉弹层（dismiss），列表顶部出现那条新记录：这就是最直接的"成功了"信号，比弹一个"保存成功"再让用户点确定，少一步打扰。

这五条没有一条涉及高深技术，全是"替用户多想一步"。表单是用户和你的 App 说话的地方，态度就藏在细节里。

##### 两种流派：灰按钮，还是点了再报错

保存按钮的验证处理有两派。一派"没填对就灰掉"：校验不过按钮就 disabled，用户想点都点不了，省事干净，但用户不知道为什么灰着。另一派"随时可点，点了再报"：按钮永远亮着，点了以后把没填对的项逐一标红。反馈清楚，代价是多一次无效点击。实践里常用折中：关键字段灰按钮（旁边配行内提示，告诉用户"还差什么"），可选项不拦截。选哪派都行，唯独别两头都不做，按钮永远亮着、点了没反应，是表单体验的谷底。

第 65 章的录入页会把这一节的表单原样用起来：金额数字键盘、分类 Picker、备注选填、金额不合法就灰保存按钮。写到这里，你不妨先自己搭一遍，再去看第 65 章的实现，对照着找差距。

##### 从表单到模型：一次保存的完整旅程

把本章的几块积木拼成一条完整的保存链路，看看一次"记一笔"从点击到呈现要经过几站。用户在录入 sheet 里填好金额、选了分类，点"保存"：表单先过验证（金额能转成数字且大于零）；通过后，把三个字段打包成一个 Record 值，交给账目模型；模型把新记录追加进数组（将来这一步换成写进 SwiftData）；数组一变，@State 或模型触发刷新；列表页的 @Query 式读取自动看到新数据，新行出现；最后 dismiss() 关掉弹层，用户看到自己刚记的那一笔排在最上面。

六站里没有一处"手动刷新界面"的代码，每一步都是"改状态、看界面"。将来从假数据升级到真数据库，变的只有第三站，前后五站原封不动。这就是分层的好处：接口稳住，内部随便换。建议你把这个链路画在纸上贴到显示器旁边，写代码卡住时抬头看看自己在第几站。

#### 七、FAQ：状态与导航的高频八问

学完这一章，你大概率会在某个深夜的模拟器前撞上下面的场面。答案提前放这儿：

<strong>问：@State 改了，界面就是不刷新，代码看着一模一样，为什么？</strong>答：按顺序查三处——改的是不是 class 的普通属性（没标 @Observable，框架看不见）；是不是原地改了数组某个元素的属性（整个替换才稳）；是不是在 body 里直接改状态（自己触发自己，行为诡异）。三处都没问题还不刷，把状态往上提一层试试。

<strong>问：两个页面都要改同一份数据，@State 放谁那里？</strong>答：谁那里都不放。提到两个页面的共同祖先；或者干脆搬进 @Observable 模型，两个页面各拿一份引用。@State 从设计上就是"一页私有"，强行放某一页，另一页永远拿不到最新值。

<strong>问：sheet 关掉再打开，里面填的东西全没了，怎么留住？</strong>答：sheet 的 @State 跟着弹层生死走，弹层一关状态就销毁——这是特性不是 bug。要跨开关保留，把数据提到弹层外面（父页面持有，弹层 @Binding 借用）；要留到下次启动 App，那已经不是状态的活儿了，去下一章找 SwiftData。

<strong>问：持有 @Observable 模型为什么也要写 @State？它不是"页面私有"吗？</strong>答：这里的 @State 更多是告诉视图"这个模型归我管"：页面创建时把模型建出来，页面销毁时模型跟着走。想让模型活得比页面久、跨页面共享，就别用 @State 持有，改用 .environment 注入（本章第一节讲过）。

<strong>问：返回按钮的文字能改吗？能整个藏掉吗？</strong>答：技术上都能，但一般别动。返回按钮和右滑手势是用户的认路本能，你改成"上一步"或者藏掉，等于在路上撤指示牌。真有沉浸式需求（全屏图片浏览之类），用 fullScreenCover 代替推页面，别在导航栈里做半吊子自定义。

<strong>问：一个 App 能有几个 NavigationStack？</strong>答：可以有多个，每个标签页一个是最常见的结构；但一个标签内部只放一个栈。栈里再套栈（sheet 里那层除外）会把返回手势和返回按钮搅乱——sheet 里需要推页面时，在 sheet 内容里单独包一个栈，两不相扰。

<strong>问：状态、模型、数据库，一份数据我到底该放哪？</strong>答：两个问题定归属——关掉 App 还要在吗？多个页面要共享吗？都不在：@State。要共享：@Observable 模型。要跨启动：SwiftData。三个格子对号入座，放错屋的代价是后面全部返工，拿不准就先放模型里，迁移比重构便宜。

<strong>问：我在 body 里写了个 for 循环算统计数据，页面一卡一卡的，是我写错了吗？</strong>答：方向写反了。body 的职责是"画"，不是"算"——它随时可能被重算，你却让它每次都从头统计。把统计逻辑搬进模型（或 .task），算好存成结果，body 只读结果。判断标准回到本章开头那句：换成命令行还成立吗？成立就别放 body 里。

#### 八、误区清单：五个昂贵的误解

- <strong>误区一：状态就是数据库</strong>。把几百条记录全塞进 @State 数组，App 一重启全归零，状态只活在内存里，进程一死它就散场。要跨启动，下一章 SwiftData 见。
- <strong>误区二：一个全局大模型包打天下</strong>。把主题、账目、网络、用户全塞进一个 @Observable 类，任何一处改动都可能惊动半个界面。按业务拆小模型，别造"上帝对象"。
- <strong>误区三：用布尔开关当导航</strong>。showDetailA、showDetailB、showEdit……十几个 isPresented 布尔值满天飞，谁也说不清用户现在在第几层。推页面交给 NavigationStack，弹窗才是 isPresented 的地盘。
- <strong>误区四：body 里干重活</strong>。在 body 里发网络请求、做排序过滤，界面每刷新一次就重干一遍。重活放 .task 或模型方法里，body 只管画图。
- <strong>误区五：老写法就是错的</strong>。看到老项目用 @ObservableObject 别急着"纠正"，它没坏，只是上一代。读懂它，新代码用新写法，把"全部迁移"留给有闲的周末。

这五条覆盖了新手项目里最贵的返工。每一条的特征都一样：当下能跑，两周后疼。写完今天的代码，回头扫一眼这份清单，两分钟，值。

#### 九、给三类背景读者的建议

这本书的读者来路不同，这一节按三个最常见的背景分别给建议，对号入座，各取所需。

##### 从安卓篇过来的读者

你刚在第 51 章摸过 Jetpack Compose，那迁移成本很低：两家几乎是同一种哲学的两种口音：remember + mutableStateOf 对应 @State，状态提升对应 @Binding，ViewModel 对应 @Observable 模型，NavHost/NavController 对应 NavigationStack。最大的心态差异在"预设组件的多少"：SwiftUI 把列表、表单、导航栏都做成了带系统手感的成品，你少了很多自由，省了大量胶水代码。建议第一周忍住"什么都自己画"的冲动，先用成品搭骨架，确实需要定制再下场。

还有一个容易别扭的点：Compose 里状态提升靠回调函数传来传去，SwiftUI 里靠 $ 引用直通车。刚开始会觉得 $ 这个符号来路不明。记住它就是"可读可写的引用"，用两周就顺了。导航那节多看两眼：Compose 的 NavController 用字符串路由，SwiftUI 用值和数组，思路一致，词汇不同。

##### 从鸿蒙篇过来的读者

第 73 章的 ArkUI 和 SwiftUI 更像双胞胎：@State 几乎同名同义；@Prop 对应"父到子单向传值"，在 SwiftUI 里就是普通的 let 传参；@Link 对应 @Binding；@Observed/@ObjectLink 的对象联动对应 @Observable 模型。页面路由的差异稍大：ArkUI 的 Navigation 与路由栈（第 74 章细讲）走"页面入栈"，SwiftUI 的 NavigationStack 走"值进数组"，思想一致、写法各有脾气。

建议你把本章"基于值的导航"那一节多读一遍：路径数组这个模型两家是相通的，看懂一边，另一边只是换语法。另外 SwiftUI 的修饰符链（.navigationTitle 那一串点语法）第一眼会陌生，把它读成"给上面的东西再配置一条规则"，两周就习惯了。

##### 从 AI 编程篇过来、习惯"指挥 AI 写代码"的读者

你在第七篇练出了让 AI 生成代码的本事，到了 SwiftUI 这类状态驱动框架，指挥的功课要升级：AI 最容易犯的错不是语法错，而是把状态放错地方，该上提的没上提、该注入的满屏传参、该持久化的塞进 @State。所以下指令前，先自己想清楚三问：这份状态住哪里？谁有权改它？要不要跨启动？把答案写进需求里，AI 的产出质量立刻上一个台阶。

验收 AI 生成的界面代码，盯三处就够：body 里有没有重活（请求、排序）；同一份数据有没有存了两份；导航用的是栈还是一串布尔值。这三处干净，代码基本歪不到哪去，本章的内容，正好就是你的验收清单。第七篇第 45 章讲过"让 AI 写的代码可靠"，在 UI 这一层，可靠的具体含义就是这三条。

##### 写给一路零基础读过来的你

如果你不属于上面任何一类背景，从第零章一路读到这里，第一次摸代码就是 Swift，恭喜你，你其实站在最有利的位置：没有旧习惯要拆，本章的概念直接长在你的白纸上。状态、栈、弹窗，对你来说不是"新框架的规则"。对你来说是"App 本来的样子"。

给你的建议只有两条。一条是节奏：本章概念密度大，别指望一遍读完就通，读一节，去练手项目里摸一遍，再读下一节，"读一段、写一段"的循环别断。另一条是预期：第十节的施工清单第一次做，预计要一个下午，中间卡三四个坑都正常，每个坑都在给你的错题本添一条，这不是弯路，这就是路本身。

#### 十、实战走一遍：三页骨架施工全记录

这一节把前面所有工具串成一次完整施工：从空项目到"账本/统计/设置"三页骨架，全部用假数据。跟着做，做完你会拥有第 65 章的地基。每一步都标注了"你会看到什么"，卡住就对号找原因。

1. 新建 SwiftUI 项目，把 ContentView 改名 MainTabView，body 换成 TabView 三个标签（账本 book、统计 chart.pie、设置 gear），运行后底部出现三个标签，每个标签页里暂时是一行占位文字。
2. 把"账本"标签的内容换成包着 NavigationStack 的 RecordListView，注意是每个标签各一个栈，别全局共用。
3. RecordListView 里用 @State 假数据数组（四五条记账字符串）+ List + ForEach 渲染，运行能看到带分割线的列表。
4. 给每行包 NavigationLink，推到 DetailView（用闭包直传，把那行文字传过去），详情页用 navigationTitle 显示标题，点行进详情、左上角返回，都能用了。
5. 加 onDelete 左滑删除，再试试给 List 加 .searchable，搜索框出现，删行生效。
6. 在列表页 toolbar 上加"+"按钮，配 @State showAdd 和 sheet(isPresented:)，弹出一个只有 TextField 和"保存"按钮的 AddRecordView——弹层能开能关。
7. AddRecordView 里加 @Environment(\.dismiss)，"保存"按钮里先往假数组里 append 一条、再 dismiss()，保存后弹层自动关闭，列表立刻多一行。
8. 给详情页加 toolbar 的"删除"按钮，confirmationDialog 确认后 dismiss 回列表，危险操作有了正牌确认流程。
9. 统计标签和设置标签各放几个 Toggle、Slider 占位，体会表单控件：顺手把设置页的一行换成你写的 ToggleRow。
10. 最后跑一遍检查单：空状态能看、删除有确认、保存后列表更新、每个标签的导航互不干扰，四条都过，骨架完工。

施工中如果某步"看到了不一样的"，回到对应小节找原因：跳不动查 NavigationStack 包没包（第二节），删错行查 id（第四节），弹层关不上查 sheet 挂的位置（第三节）。这份清单也适合当"改完代码的回归测试"：每次大改之后跑一遍，骨架没散，才往上盖新楼。

#### 十一、下一步：从骨架到成品还差三步

骨架只是骨架。要变成能天天用的成品，还差三步，正好对应本书后面三章的安排，这里先指个路，让你知道脚下的位置。

第一步，给数据安个家：现在所有记录都是 @State 假数据，杀掉 App 就清零。下一章的 SwiftData 把它们变成真正存得下来的记录——你今天搭的 @State 数组，到时候换成 @Query 就行，界面代码几乎不用动，这就是"状态住哪"设计得好带来的红利。第二步，接上外面的世界：第 66 章的天气项目让 URLSession 和 async/await 上场，你的 App 第一次知道服务器长什么样。第三步，打磨与出门：第 67 章的测试调试、第 68 章的权限通知与架构，把"能跑的 Demo"变成"敢给爸妈用的 App"。

顺序别乱。见过不少新手跳过存储直接上网络，结果记录存在内存里、刷新就丢，网络层写得再漂亮也是空中楼阁。先地基后楼层，按 65、66、67 的顺序推进，每章的成果都踩在上一章的地基上：这本书的项目篇就是这么设计的，跟着走最省力。

最后说说节奏。本章概念密，别按"读小说"的速度赶。一个晚上啃两节、动手验证一节，是正常的速度。状态管理这东西有个特点：当时觉得懂了，动手才发现没懂，所以"读一段、写一段"的循环别断。等你把三页骨架亲手搭完，回头看这一章，会发现薄了很多，不是内容变少了，是你长高了。

#### 十二、错题本：十个高频症状的快速诊断

报错信息千千万，新手常撞的就那几类。这本"错题本"按症状组织：看到什么，先查什么，怎么修。对症下药，比通读文档快得多。

- <strong>改了值界面不动</strong>：查 @State 写没写；查改的是不是 class 普通属性；查是不是原地改了数组元素。三个都是"框架没看见你改"的变体。
- <strong>编译器说某个变量"找不到"</strong>：多半是 $variable 用在了没有对应 @State/@Binding 的变量上，或者变量声明在别的 struct 里。检查变量声明和 $ 的配对关系。
- <strong>NavigationLink 点击无反应</strong>：链接不在 NavigationStack 里。把栈补上，或者检查是不是把链接放进了 TabView 直属位置而没套栈。
- <strong>sheet 弹不出来或行为诡异</strong>：先查 sheet 挂在哪个视图上：挂在会消失的行或按钮上就会出怪事，挪到最外层容器。
- <strong>弹层里的按钮点了没效果</strong>：弹层内容是不是忘了套 NavigationStack 却想用 push；或者按钮的 action 里写的是"改本地状态"而弹层被 @State 重新初始化了。弹层状态要外提。
- <strong>列表删除后删错行</strong>：id 撞牌或用了下标当 id。换成 Identifiable + UUID，见第四节。
- <strong>列表滚动掉帧</strong>：行 body 里做了重活，或行内嵌套过深。把计算挪到数据层，行瘦身。
- <strong>页面进来就闪退或白屏</strong>：八成是把必传参数漏了（DetailView 少了参数），或者 @State 初始化里调了会崩的强解包。查 init 和强解包。
- <strong>返回手势失灵</strong>：最近是不是自定义了导航栏或拦了手势；sheet 里嵌套栈也会抢手势。先还原自定义，再逐项加回。
- <strong>切标签后页面状态全丢</strong>：状态放在了"标签内容"里且标签被销毁重建。把需要跨标签存活的状态上提到 App 级或模型。

用法建议：报错时先扫一遍这份清单对症状，两分钟没对上的再复制报错去搜。这份清单要一直养着，把自己踩的新坑也记进去，三个月后它就是你的私人诊室。

#### 十三、思维训练：拿到任何 App，先拆骨架

学框架最快的方式之一，是拿成熟 App 当教材。从今天起，打开手机上任何一个 App，都试着用本章的词汇拆一拆它的骨架，这个习惯不花钱，但能把"看得懂代码"升级成"看得懂产品"。

拿系统自带的"邮件"练手：底部有没有标签栏？没有：它是单栈 App，进进出出全靠推页面（NavigationStack）。列表页和详情页是几层？进入一篇邮件算一层，那标记、移动这些操作是推页面还是弹窗？是弹窗，办一件事，办完就走，口诀应验了。删除要不要确认？滑动删除直接删，而"清空废纸篓"有确认弹窗，破坏范围越大，确认越重。

再拆"设置"：它就是 List 分组样式的教科书：insetGrouped 卡片、Section 节头、行内箭头、开关、选择器，全是你这两章摸过的控件。你会发现苹果自家的 App 几乎不用炫技布局，全靠这些基础控件的排列组合：这就是"系统 App 是交互规范"的含义。

拆的时候给自己三问：主流程是推页面还是弹窗？并列功能怎么分标签？哪些操作有确认、哪些没有？三问答完，这个 App 的骨架就到你手里了。等你自己设计记账本时，这些拆过的 App 就是你的参考答案库——不用发明交互，先学会认出好交互。

频率建议：不用专门抽时间，通勤排队时打开一个 App 拆两分钟就够了，一天一个。两周后你会发现自己看 App 的眼光变了，知道哪些页面做得顺手、哪些别扭，顺手在哪、别扭在哪。这份"手感"没有公式可教，只能这样一点一点拆出来；而它恰恰是设计自己第一个 App 时最值钱的东西。

#### 十四、自测十题：合上书答一遍

十道小题，都是本章的核心概念。先自己答，再看括号里的参考答案，答错不扣分，答错不知道错在哪才亏。

1. @State、@Binding、@Observable、.environment，各用一句话说清管什么。（私有状态／借用的引用／共享逻辑／全局广播）
2. 改了变量界面不刷新，最常见的原因是什么？（忘了 @State，或改的是框架"看不见"的 class 普通属性）
3. 子视图想改父视图的开关，用什么工具，父视图传值时要加什么符号？（@Binding；$）
4. 视图模型里该放什么、不该放什么？（数据怎么变的逻辑；颜色字号这类长相、以及要持久化的记录）
5. NavigationStack 的"栈"用盘子怎么解释？返回对应哪个动作？（推压顶、弹出顶）
6. 点"保存"后自动关页面，用什么 API？顺序上要注意什么？（dismiss；先存数据再关门）
7. 主流程、临时操作、并列大块，分别用什么导航方式？（推页面、sheet、TabView）
8. ForEach 的 id 参数是干什么的？用数组下标当 id 会出什么事？（身份牌；删错行、界面错位）
9. 列表空了和列表旧了，各给用户看什么？（空状态引导文案；下拉刷新）
10. App 进后台第一件事该做什么？为什么？（保存草稿；进程随时可能被系统终止）

九题以上答对，本章过关；错三题以上，回到对应小节再读一遍，然后打开练手项目把第十节的施工清单重跑一遍，代码不会骗人，做过一遍的概念才是你的。

#### 十五、进阶三招：让骨架更专业

基础已经齐了，这节给想再往前走一步的读者三招，都是"新手项目"和"老手项目"肉眼可见的分界线。不急的话可以先跳过，做到第 65 章自然会想回来。

##### 第一招：用一个枚举管住页面的"命运"

前面误区清单提过：isLoading、isEmpty、isError 几个布尔值组合起来，情况越理越乱。老手的做法是定义一个枚举状态，加载中、成功（带上数据）、失败（带上错误），三选一，同一时刻页面只可能处于一种情况，switch 一写，所有分支都被编译器盯着，漏一个都编译不过。列表页、详情页凡是"要等"的地方都适用这一招。等下一章学到网络请求，这个模式会天天见面：请求发出去是加载中，返回了是成功，抛错了是失败，界面跟着状态走，一气呵成。

##### 第二招：把重复的行抽成真正的组件

列表里同一种行出现了三处以上，就值得抽成一个独立 View。抽取不只是复制粘贴的搬家，要点在"接口"：组件只接收它真正需要的数据（比如一条 Record），不接收整个数组、不接收父页面的环境，接口越窄，组件越独立，别处复用越省心。抽完之后父页面的 body 会明显变薄，这正是本章反复说的"薄视图"。组件写多了，你会攒出一套自己的"预制件库"：开关行、金额行、空状态视图，下个项目直接搬，这是比任何教程都实在的资产。

##### 第三招：让预览替你把状态测一遍

SwiftUI 的画布预览不止能看一张图：同一个视图可以配多套预览，空数据的、满列表的、标题特别长的、深色模式的。写完一个行组件。顺手配两三个预览，改一处立刻看到所有状态的表现，比来回改代码模拟情况快得多。尤其是深色模式：颜色写死（纯黑纯白）的界面，一切深色模式就穿帮。预览里切一下立刻现形。让"每种状态都有一张预览图"成为你的交付标准，界面质量会稳一个台阶。

三招的共同精神只有一个：把"到时候再说"变成"现在就定规矩"。枚举定死状态，组件定死接口，预览定死外观，规矩定在写代码之前，返工就轮不到你。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-quote-left mr-2"></i>一句话记牢

{class="mt-1"}
你不是在"操作界面"，你是在"改状态，让框架替你重画界面"，状态住对地方，导航顺着用户预期，界面就永远不会和你作对。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 状态四工具：@State（页面私有）、@Binding（借用）、@Observable（逻辑）、.environment（全局）
- 新项目用 @Observable 宏写视图模型；老教程的 @ObservableObject 能读即可
- NavigationStack 推页面；@Environment(\.dismiss) 编程式返回
- 主流程推页面、临时操作弹 sheet、并列大块用 TabView
- List 是"国民列表"：分割线、滑动删除开箱即用
:::
