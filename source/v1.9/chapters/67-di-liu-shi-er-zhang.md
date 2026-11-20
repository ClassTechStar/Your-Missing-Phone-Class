---
id: di-liu-shi-er-zhang
num: 62
part: ios-kai-fa-pian
nav: 第六十二章：界面开发——SwiftUI入门
toc: default
kind: chapter
---

### 第六十二章：界面开发——SwiftUI 入门

{class="chapter-intro mb-4"}
界面是用户看到的一切。SwiftUI 是苹果 2019 年推出的<strong>声明式</strong>界面框架，你只需要"声明"界面长什么样，系统自动负责渲染、适配深色模式、适配各种屏幕。到 2026 年，SwiftUI 已是新项目的绝对主流。这一章，咱们学会"画画"。

::: div .quick-read
##### 本章速读（5 分钟版）
这一章教你给 iPhone"画画"。SwiftUI 是苹果 2019 年推出的声明式界面框架：你只管描述"界面上有一个红色按钮写着点我"，怎么画、什么时候重画、深色模式怎么适配，系统自己操心。到 2026 年它已是新项目的绝对主流。如果你学过第 51 章的 Compose，这一章会眼熟得过分，声明式是同一套思想的另一个方言，很多概念能一一对上。

最关键的有三件事。第一，记住<strong>界面是状态的函数</strong>：body 会被反复执行，状态一变界面自动跟上，你从"修表匠"变成了"画图纸的人"。第二，状态三纪律：<strong>私藏、独源、现算</strong>——本页面的小状态用 @State 自己收着，要借给别人改就用 @Binding 把修改权借出去，能现算出来的别单独存；状态一多、要跨页面共享，下一章的 @Observable 再上。第三，布局就是三个盒子：VStack 竖排、HStack 横排、ZStack 叠放，Spacer 和 frame 负责把东西推到位；长列表交给 Lazy 家族，几百条也不卡。顺手记两条修饰符的经验：修饰符是链式包装，顺序有意义，先留白还是先上背景，出来的图差一圈；触控目标别太抠门，按钮做小了爸妈的手指按不准，"人人能用"那节有明确提醒。

今天就能做的最小动作：跟着章里的完整示例，把"饮水打卡"卡片敲出来跑一遍：它一次练到 @State、@Binding 和 ForEach。做完给它配三个预览：浅色、深色、大字体各来一份。一个界面三副面孔并排看。这不到半小时，能让你亲身体会"系统色、语义字号"为什么值钱。章里还有一页"一屏做完的十项自检"界面检查清单，收尾时照着过一遍。

最大的坑。别以为画布里的效果就是最终效果：画布是近似，真机的手感、字体渲染、性能只有设备知道，收尾要"画布定稿、模拟器过一遍、真机过一遍"三层验收。别以为深色模式要做两套界面，那是命令式思维，用系统色和语义字号，同一套代码两种外观；觉得深色是大工程的人，多半是把颜色写死了。还有两个：body 重算没你想的浪费，新手期的提前优化几乎都在帮倒忙，等测量工具说哪里慢再动手；也别把所有状态都塞进一个 @State，工具和规模不匹配，是"玄学刷新"的另一半来源。
##### 速查表
- 界面怎么写：只描述"长什么样"，怎么画系统管，body 会反复执行
- 三个盒子：VStack 竖排、HStack 横排、ZStack 叠放，Spacer 把东西推到位
- 状态怎么管：@State 私藏小状态，@Binding 借出修改权，能现算的别存
- 输入框防呆：值加回调成对出现，密码框用 SecureField
- 长列表怎么写：Lazy 家族加 ForEach，每行配稳定的 id
- 深色模式怎么适配：用系统色和语义字号，别写死颜色，一套代码两种外观
- 交付前怎么验收：画布定稿、模拟器过、真机过，三层都过才交付
- 安卓老同学怎么对表：@State 对应 remember 加 mutableStateOf，VStack 对 Column，List 对 LazyColumn
:::

#### 一、SwiftUI 的思想：声明式，不是命令式

老式界面开发是"命令式"：先告诉系统"创建按钮 → 放在(20,30) → 设置颜色"，一步一步指挥。SwiftUI 是"声明式"：<strong>你直接描述"界面上有一个红色按钮写着'点我'"</strong>，怎么画、什么时候重画，系统自己操心。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 第一个 SwiftUI 视图</span><span class="dots">···</span>
:::

```
import SwiftUI

struct ContentView: View {
 var body: some View { // body：描述"界面长什么样"
 VStack { // 竖着排列
 Text("你好，世界！")
 .font(.largeTitle) // 修饰符：大标题
 Button("点我") {
 print("被点击了")
 }
 .buttonStyle(.borderedProminent) // 蓝色实心按钮
 }
 .padding()
 }
}
```
:::

关键点：<strong>视图 = 遵守 View 协议的结构体</strong>，<code class="inline">body</code> 属性描述界面，<code class="inline">.修饰符()</code> 链式"上妆"。这就是 SwiftUI 的全部基本盘。

##### some View 是什么意思

模板里那句 <code class="inline">var body: some View</code> 会让你停顿一下，some 是什么鬼？它的官方名叫"不透明类型"，但新手期只需要一个读法：<strong>"某种视图，具体是谁，body 自己说了算"</strong>。编译器能看穿 body 到底返回哪个类型，你写起来却不用把冗长的类型名抄一遍。

使用规则也简单：每个视图结构体里有且只有一个 body，它必须是计算属性（<code class="inline">var</code>，不是 let）；body 返回的东西必须是一个 View，所以 Text、Button、VStack 都能当返回值，随便你套多少层。第一次见到 some 别深究，等你在第 63 章见过更多写法。回头再看它会有"原来如此"的感觉。

##### 两种心智：装修队与设计师

用装修打个比方。命令式像雇装修队：你得一步步指挥："砸墙、走线、刷漆、装灯"，任何一步说漏了，现场就不是你要的样子。更累的是后期：家具挪了位置。你得记得把插座、灯位、窗帘全跟着改，漏一处就是"对不上"的尴尬。老式界面代码就是这么长的：一个状态变了，你得手动把相关的每一处界面都改一遍，改漏一处就是 bug。

声明式像请设计师：你只说"我要一面北欧风的白墙、一把原木椅"，怎么施工、怎么返工是设计师的事。每当你改主意（状态变了），把新需求说一遍，现场自动变成新样子。SwiftUI 里那句"界面永远忠实反映状态"，说的就是这件事：你永远只负责"描述现在该是什么样"，不用操心"从上一个样子怎么变过来"。

这个转变对新手的意义，怎么强调都不过分：它删掉了最大的一类 bug——"状态和界面不一致"。第 61 章学的 struct、协议、闭包，在这里全部派上用场：视图是 struct，View 是协议，点击动作是闭包。

##### 声明式省掉的代码，都去哪了

感受一下两种写法的体量差。假设要做一个"开关切换，文字和颜色跟着变"的小界面，命令式的老写法（伪代码，体会意思就行）大概是这样：创建开关、创建文字标签、给开关挂一个事件处理函数。函数里判断新状态，然后手动改标签的文字、再手动改标签的颜色，三个控件三个改处，漏一处就不同步。以后每加一个"受这个开关影响"的界面元素，都得回到这个函数里追加一行。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 同一件事的声明式写法</span><span class="dots">···</span>
:::

```
struct SwitchDemo: View {
 @State private var isOn = false

 var body: some View {
 VStack {
 Toggle("电源", isOn: $isOn)
 Text(isOn ? "设备运行中" : "设备已关闭")
 .foregroundColor(isOn ? .green : .secondary)
 }
 .padding()
 }
}
```
:::

声明式版本没有"事件处理函数"，没有"手动改文字"，没有"手动改颜色"——每一个界面元素都在直接表达"我由 isOn 决定"。想加第三个受影响的元素？再加一行描述即可，别的什么都不用动。省掉的代码没有消失，它们变成了系统的基础设施：重算、比差异、刷新，全由 SwiftUI 在幕后干了。

##### 这不是苹果独创：三兄弟同一个思想

声明式界面这几年成了全行业的共同答案：安卓那边是 Jetpack Compose（第 51 章），鸿蒙那边是 ArkUI（第 73 章），苹果这边是 SwiftUI。三家思路同构：描述界面、状态驱动、自动重画——连概念的名字都长得像一家人：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">概念</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">SwiftUI</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Compose</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ArkUI</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">界面单元</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">View（struct）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Composable 函数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Component 组件</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">界面状态</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">remember + mutableStateOf</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">竖排 / 横排</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">VStack / HStack</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Column / Row</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Column / Row</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">父子传值</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Binding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">状态上提 + 回调</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Prop / @Link</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
三大声明式框架概念对照

看懂这张表的含义了吗<strong>这套思想学一次，三处通用</strong>。你已经会 SwiftUI 之后去看第 51 章，会发现 Compose 的代码像换了件外套的老朋友；反过来也一样。所以别被"我要学三套框架"吓住，它们是一套思想的三种方言。

##### body 会反复执行：UI 是状态的函数

有个新手必知的心智模型：把界面看成一个数学式子<strong>界面 = f(状态)</strong>。状态是输入，界面是输出，body 就是那个 f。状态一变，body 重新算一遍，界面跟着变。

"反复执行"这四个字带来两条纪律。第一，body 里只放"描述"，别放干活的事：网络请求、文件读写、复杂计算，都别塞进 body：它一重算你就多发一次请求，界面会疯。第二，body 里别数"执行了几次"：SwiftUI 重算的时机由系统决定，你在 body 里 print 一行，可能会看到它多跑几次，这不是 bug，是它的工作方式。真正要保证的是：同样的状态。算出来的界面永远一样（这个性质叫"无副作用"，听起来玄，其实就是"别偷改东西"）。

##### 场景案例：深色模式，一行都没写

把思想落到一个具体时刻。周五下午，你把写了一周的界面拿给同事看，他随手把模拟器切成了深色模式，你心一凉：完了，白底黑字会不会变成白字白底？结果界面自己换好了衣服：背景深了、文字浅了、按钮的蓝还是那个蓝。你为深色模式写的代码量：零行。

这就是声明式 + 系统颜色组合的红利：你描述的是"这行字用主文字色"（而不是"这行字是黑色"），至于主文字色在浅色模式下长什么样、深色模式下长什么样，系统自己知道。第八节会把"哪些颜色该用系统的"展开讲；现在先记住这个体验<strong>当某件事系统能替你适配时，别自己抢着干</strong>。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
一句话记牢

{class="mt-1"}
命令式管过程，声明式管结果。你描述"现在该是什么样"，过去怎么变来的、未来怎么变过去，都不归你管。
:::

#### 二、基础视图：文字、按钮、输入框、图片

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">视图</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">干什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">示例</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">显示文字</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Text("你好")</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">按钮</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Button("点我") { 动作 }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">输入框</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">TextField("提示", text: $文本)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">显示图片</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Image(systemName: "star.fill")</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
SwiftUI 四大基础视图

注意 <code class="inline">Image(systemName:)</code>——苹果内置了 <strong>SF Symbols</strong> 图标库（几千个免费图标），"star.fill" 这种名字就能直接显示一个实心星星。这是 iOS 开发的隐藏福利：<strong>做界面几乎不用找图标素材</strong>。

##### Text：文字的一身本事

别看 Text 只有一行，它能接的"妆"相当多。常用的先过一遍：

::: div .code-block
:::inline div .code-head
<span>SWIFT · Text 常用修饰</span><span class="dots">···</span>
:::

```
Text("本月支出")
 .font(.headline) // 语义字号：标题级
 .foregroundColor(.secondary) // 次要文字色

Text("这是很长的一句话，会自动换行，行距也调过了。")
 .lineSpacing(6) // 行间距
 .lineLimit(2) // 最多两行，超了省略号

Text("账单共 \(12 + 3) 笔") // 插值直接用第 61 章的语法
```
:::

着重说 <code class="inline">.font(.headline)</code> 这种写法：headline、title、caption 这类是<strong>语义字号</strong>——不写死多少像素，而是告诉系统"这是标题级别的字"，用户把系统字体调大它就跟着大。给爸妈做 App，这条是刚需。真正需要精确定字的场合（比如图标旁的小角标）才用 <code class="inline">.font(.system(size: 20))</code> 写死，两类的适用场景第八节还会细说。

另外，Text 对<strong>插值</strong>照单全收<code class="inline">Text("你点了 \(count) 次")</code> 直接用第 61 章的字符串插值，界面和状态就这样接上了。数字显示格式化（保留几位小数、带不带千分位）有专门的写法，第 65 章记账本项目用到时再教。

##### Button：两种写法，一个心眼

::: div .code-block
:::inline div .code-head
<span>SWIFT · Button 两种写法</span><span class="dots">···</span>
:::

```
// 写法一：纯文字标题
Button("保存") {
 print("保存了")
}
.buttonStyle(.borderedProminent)

// 写法二：自定义外观（图标 + 文字）
Button {
 print("分享了")
} label: {
 HStack {
 Image(systemName: "square.and.arrow.up")
 Text("分享")
 }
}
.buttonStyle(.bordered)

// 置灰：条件不满足时禁用
Button("提交") { }
 .disabled(false)
```
:::

两种写法的分工：标题是纯文字就用第一种，一行搞定；外观要自定义（图标、颜色、复杂排列）就用第二种，把外观写在 label 闭包里。那个 <code class="inline">.disabled</code> 值得多看一眼：表单没填完就置灰提交按钮，比点下去再弹"请填写完整"的提示友好得多，好界面的许多功夫，都花在"让错误根本不发生"上。

buttonStyle 常用三档：borderedProminent（实心、最显眼，一屏留一个给主操作）、bordered（描边，次级操作）、borderless（几乎透明，列表里的行操作常用）。别满屏都用实心，都醒目等于都不醒目。

##### TextField 与 SecureField：输入框一族

::: div .code-block
:::inline div .code-head
<span>SWIFT · 输入框</span><span class="dots">···</span>
:::

```
struct InputDemo: View {
 @State private var nickname = ""
 @State private var password = ""

 var body: some View {
 VStack(spacing: 12) {
 TextField("给自己起个昵称", text: $nickname)
 .textFieldStyle(.roundedBorder)
 SecureField("密码", text: $password) // 自动打圆点
 .textFieldStyle(.roundedBorder)
 Text("昵称长度：\(nickname.count)")
 }
 .padding()
 }
}
```
:::

三个看点：placeholder（"给自己起个昵称"）是框里那行灰色提示语，用户一开始打字它就消失；<code class="inline">$nickname</code> 是双向绑定——输入框和变量从此连体，谁变另一个跟着变，第四节的第二段代码就是它；SecureField 是 TextField 的密码版，自动把内容打码。需要数字键盘时加一行 <code class="inline">.keyboardType(.numberPad)</code>，速查表里已经收录。

##### Image：系统图标与本地图片

::: div .code-block
:::inline div .code-head
<span>SWIFT · Image 三种来源</span><span class="dots">···</span>
:::

```
Image(systemName: "heart") // SF Symbols 系统图标
 .imageScale(.large)
 .foregroundColor(.red)

Image(systemName: "heart.fill") // .fill = 实心变体

Image("trip-photo") // Assets 里的本地图片
 .resizable() // 允许改尺寸
 .scaledToFit() // 按比例缩放，不变形
```
:::

SF Symbols 的名字有规律：基础名 + 变体后缀：heart 和 heart.fill、bell 和 bell.fill、wifi 和 wifi.slash。记住这个规律，想用图标时先猜名字，八成猜中；猜不中就在 Xcode 里问编程智能，或者去苹果开发者网站的 SF Symbols 页面查。本地图片的流程第 60 章讲过：拖进 Assets.xcassets，代码里按名字取用，名字写错不会崩，但会显示不出来，"图片没显示"先查名字拼写。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小贴士：先问系统要，再找素材

{class="mt-1"}
做界面想用任何图标之前，先想想 SF Symbols 里有没有：铃铛、Wi-Fi、电池、文件夹、各种箭头，日常 App 的图标需求它基本全包了，还自动适配深色模式和粗细调整。第三方图标库是"系统图标不合适"时才轮到的选项，顺序别颠倒。
:::

##### 控件家族点将：Toggle、Slider、Picker、Stepper

四大基础视图之外，常用控件还有一整排，每个都长得很像：<code class="inline">@State</code> 存值 + <code class="inline">$</code> 绑定 + 一个提示文案。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 控件全家福（上）</span><span class="dots">···</span>
:::

```
struct ControlsDemo: View {
 @State private var on = true
 @State private var volume = 0.5
 @State private var choice = "浅色"

 var body: some View {
 VStack(spacing: 16) {
 Toggle("提醒我", isOn: $on) // 开关
 Slider(value: $volume, in: 0...1) // 滑块
 Picker("主题", selection: $choice) { // 选择器
 Text("浅色").tag("浅色")
 Text("深色").tag("深色")
 }
 .pickerStyle(.segmented) // 分段样式
 }
 .padding()
 }
}
```
:::

认个脸就够，第四节的完整示例里它们会真实上岗。这里只提醒一件事：Picker 的选项用 <code class="inline">.tag( )</code> 标记，tag 的类型要和 selection 绑定的变量类型一致：都是 String 或者都是 Int，不一致编译器会给你颜色看。还有 Stepper（加减步进器）和 DatePicker（日期选择），用法同一个模子，第七节做设置页时一起练。

##### 控件全家福（下）：Stepper 与 DatePicker

剩下两个常用控件一起认了。Stepper 是"加减号步进器"，适合数字微调；DatePicker 是日期选择，一行顶别人一个日历控件：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 控件全家福（下）</span><span class="dots">···</span>
:::

```
struct MoreControlsDemo: View {
 @State private var cups = 3
 @State private var startDate = Date()

 var body: some View {
 VStack(spacing: 16) {
 Stepper("每天目标 \(cups) 杯", value: $cups, in: 1...20)
 DatePicker("开始日期", selection: $startDate,
 displayedComponents: .date)
 }
 .padding()
 }
}
```
:::

Stepper 的 <code class="inline">in: 1...20</code> 顺手复习了第 61 章的区间写法，范围一限定，用户想点破天也超不出去。DatePicker 传 <code class="inline">.date</code> 表示只选日期不选时间，去掉这个参数它就日期时间一起选。到这里的规律你已经能自己总结了吧：<strong>每个控件 = 状态绑定 + 外观参数</strong>，学会了四个，剩下的一看就会。

#### 三、布局三件套：VStack、HStack、ZStack

- <strong>VStack</strong>：竖着排（像排队打饭）。
- <strong>HStack</strong>：横着排（像并排坐）。
- <strong>ZStack</strong>：叠着放（像扑克牌摞一起，适合做角标、遮罩）。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 布局三件套 + 常用修饰符</span><span class="dots">···</span>
:::

```
VStack(alignment: .leading, spacing: 12) {
 HStack {
 Text("账单")
 Spacer() // 弹性空间：把右边推到尽头
 Text("-25.5 元").foregroundColor(.red)
 }
 Divider() // 分割线
 Text("备注：午饭")
}
.padding(16) // 四周留白
.background(Color(.systemGray6)) // 浅灰底
.cornerRadius(12) // 圆角

// 修饰符顺序有意义：先 padding 再 background，背景不含边距
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：修饰符顺序有讲究

{class="mt-1"}
<code class="inline">padding(16).background(灰)</code> 和 <code class="inline">background(灰).padding(16)</code> 效果不同——前者"先留白再涂色"（背景不含边距），后者"先涂色再留白"（背景包含边距）。新手最常见的"奇怪白边"都源于此。不确定时调换顺序，预览立刻告诉你答案。
:::

##### 对齐与间距：两个参数管氛围

VStack 和 HStack 都接受两个"氛围参数"：<code class="inline">alignment</code> 管对齐，<code class="inline">spacing</code> 管孩子之间的间距。上面的账单卡片用了 <code class="inline">.leading</code>（左对齐）加 12 的间距，比默认紧凑一点，阅读节奏立刻不一样。

新手对这两个参数的常见误区是"不用它们也能跑"。能跑，但界面会显得"说不出的业余"：标题和数值一个左一个右的错位感、密密麻麻没有呼吸感的堆叠。经验值是：同类信息之间间距小一点（8 到 12 左右），不同区块之间大一点（16 到 24 左右），拿不准就用默认值——苹果的默认间距是设计师调过的，多数时候比自作主张好看。

##### Spacer 与 frame：把东西推到位

布局问题的两大高频需求："把 A 推到最右边"和"这个东西固定多大"。前者用 Spacer，它会吃掉所有富余空间，把旁边的兄弟挤到边上；后者用 <code class="inline">.frame</code>：

::: div .code-block
:::inline div .code-head
<span>SWIFT · Spacer 与 frame</span><span class="dots">···</span>
:::

```
HStack {
 Text("左侧")
 Spacer() // 弹簧：把右边推到头
 Text("右侧")
}

Text("撑满整行")
 .frame(maxWidth: .infinity, alignment: .leading) // 撑满 + 左对齐

Button("标准按钮") { }
 .frame(width: 120, height: 44) // 固定尺寸
```
:::

一个组合技值得记：<code class="inline">.frame(maxWidth: .infinity, alignment: .leading)</code> 能把"天生只占一角"的东西撑满整行还保持左对齐，宽屏上左对齐的表单、贴边的提示条，全靠这一招。Spacer 和 frame(maxWidth:) 的区别是：Spacer 只管"让位"，frame 是给视图本身划地盘。

##### ZStack 实战：角标、遮罩与背景

ZStack 最常见的三个用途里，角标最有代表性——"铃铛图标右上角有个红点"，一秒写出：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 红点角标</span><span class="dots">···</span>
:::

```
ZStack(alignment: .topTrailing) {
 Image(systemName: "bell")
 .font(.title2)
 Circle()
 .fill(.red)
 .frame(width: 10, height: 10)
 .offset(x: 4, y: -4) // 微调位置
}
```
:::

ZStack(alignment:) 决定孩子们怎么叠：topTrailing 就是右上角。第三个用途是背景，把一张渐变色或图片垫在最底下，内容叠在上面，很多 App 的"高级感"卡片就是这么来的。记住叠放顺序：写在 ZStack 里越靠前的越在底下，和扑克牌一张一张往上摞是同一个方向。

##### 长列表的事：Lazy 两兄弟

内容多到要滚动时，别把几百行一次性全画出来，用 <code class="inline">LazyVStack</code> 和 <code class="inline">LazyHStack</code>：lazy 的意思是"滚到哪画到哪"，屏幕外的先不渲染，内存和流畅度都救了。用法和普通 VStack 一模一样，就是把名字换成 Lazy 开头。

<strong>与 Compose 对照</strong>：安卓那边的 LazyColumn 和这边的 LazyVStack 是同一个意思，连"Lazy"这个前缀都同款（第 51 章的同学会心一笑）。至于 iOS 的"国民列表" List——分组、滑动删除、侧滑按钮一整套——第 63 章专门讲它，这节知道有这号人物就行。

##### 场景案例：三步拼出一张账单卡片

把"纸上画格"翻译成一次真实的编码。目标：一张卡片，上面"餐饮"和金额同行，下面一行备注，底色浅灰、带圆角。按三步走。

第一步，纸上画格：整卡竖切两块（信息行、备注行），信息行横切两块（类别、金额）。第二步，选容器：整卡 VStack，信息行 HStack，两块之间要分开，中间夹 Divider 或调 spacing。第三步，翻译成代码：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 账单卡片</span><span class="dots">···</span>
:::

```
VStack(alignment: .leading, spacing: 8) {
 HStack {
 Text("交通")
 .font(.headline)
 Spacer()
 Text("-6.0 元")
 .foregroundColor(.red)
 }
 Text("备注：早高峰地铁")
 .font(.caption)
 .foregroundColor(.secondary)
}
.padding(16)
.background(Color(.systemGray6))
.cornerRadius(12)
```
:::

十几行，一个能直接放进项目的卡片组件。注意细节：备注用 caption（小字）加 secondary（次要色）做了视觉降级，重要信息醒目、次要信息安静，这比"全部一样大"高级得多。这张卡片在第 65 章会升级成真正的列表行，现在先把它存进你的代码片段库。

##### 嵌套心法：先竖后横，纸上画格

真实界面都是三件套的嵌套组合。新手最容易在这里迷路，给你一个笨但百试百灵的方法：<strong>在纸上画格子</strong>。拿一张便利贴，把界面用横线竖线切成块，整页竖着切几大块，是 VStack；其中某块里横着排，是 HStack；有东西要叠，是 ZStack。画完照着翻译成代码，一格一个容器。

举个例子，一张账单卡片：整卡竖排（VStack）→ 第一行"类别 + 金额"横排（HStack，中间塞 Spacer）→ 第二行备注独占一行（Text）→ 底部"编辑/删除"横排（HStack）。三层结构，纸上画出来一目了然，直接照抄进代码。反过来，如果写出来的界面"怎么调都不对劲"，九成是纸上没画清，回到纸面重新切格子，比在代码里瞎试快得多。

##### padding 家族与 Divider：呼吸感的细节

padding 有四种常见形态，一口气认全：

::: div .code-block
:::inline div .code-head
<span>SWIFT · padding 四形态</span><span class="dots">···</span>
:::

```
.padding() // 系统默认留白
.padding(16) // 四周都留 16
.padding(.horizontal, 16) // 只左右留
.padding(.top, 8) // 只顶上留
```
:::

单边 padding 特别实用：列表行的左右留白统一、卡片顶部多留一口气、按钮和分割线之间隔一点，都是它的活。配合 <code class="inline">Divider()</code>（一条系统样式的细分割线，自动适配深色模式），页面立刻从"糊成一团"变成"段落分明"。

这些小零件单看都不起眼，组合起来就是界面的"排版素养"。一个自检习惯：每写完一屏，眯起眼睛看整体，哪里太挤、哪里太空、哪里抢戏，眯眼测试暴露的排版问题，比逐个控件检查快得多。

##### 三种高频布局翻车，当场纠偏

新手写布局，翻车姿势高度集中。先看三种最常见的，中了就对号纠正。

<strong>翻车一：想左右分开，却忘了 Spacer。</strong>两个 Text 放进 HStack，它们亲密地挤在中间——因为 Stack 默认只管"排"，不管"推"。

<div class="case-box">
<div class="case-box-head">翻车现场</div>
<p>一个账单行的界面：左边是项目名，右边是金额。写完一看，两串文字紧紧挨在屏幕中间，金额没贴着屏幕右边。反复调 padding、调 frame，两小时过去还是不对。</p>
<p class="case-box-quote">"怎么让它靠右，padding 加了没用"</p>
<p class="case-box-src">场景来源：全书通用场景（非特定读者）</p>
<p><strong>怎么办</strong>：在两者中间塞一个 Spacer，右边立刻到位。看到"该靠边的东西没靠边"，第一反应就该是 Spacer——Stack 默认只管"排"，不管"推"，padding 补的是边距，不是位置。</p>
</div>


<strong>翻车二：拿 ZStack 当万能容器。</strong>有人发现 ZStack 也能装下所有东西，就什么都往里放——结果全部叠在左上角。记住分工：左右排是 HStack，上下排是 VStack，真要叠（角标、背景）才用 ZStack。容器选对，一半以上的布局问题当场消失。

容器别混用。

<strong>翻车三：嵌套到十层，自己都看不懂。</strong>body 里套了七八层括号，缩进拉满，改一处要数半天配对。解法是"拆子视图"：把一段结构完整的部分拎出来，变成一个独立的 View 结构体（第三节的账单卡片就该拆成 CardView）。拆完 body 只剩三五行，可读性回来了。拆分的判断信号和第 61 章讲函数时一样：看着眼晕，就该拆。

#### 四、状态与绑定：让界面"活"起来

静态界面没意思。SwiftUI 的规则：<strong>界面永远忠实反映状态，状态变了，界面自动重画</strong>。

::: div .code-block
:::inline div .code-head
<span>SWIFT · @State 计数器</span><span class="dots">···</span>
:::

```
struct CounterView: View {
 @State private var count = 0 // @State：这个值变了要重画

 var body: some View {
 VStack {
 Text("你点了 \(count) 次")
 Button("点我 +1") {
 count += 1 // 改状态，界面自动刷新
 }
 }
 }
}
```
:::

输入框要用"双向绑定"<code class="inline">$</code> 符号把"值和修改权"一起传进去：

::: div .code-block
:::inline div .code-head
<span>SWIFT · @Binding 双向绑定</span><span class="dots">···</span>
:::

```
struct InputView: View {
 @State private var text = ""

 var body: some View {
 TextField("输入点什么", text: $text) // $ 双向绑定
 .textFieldStyle(.roundedBorder)
 Text("你输入了：\(text)") // 输入时实时更新
 }
}
```
:::

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"> 用户操作</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"> 状态改变（count += 1）</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"> SwiftUI 感知到变化</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"> 自动重画界面（body 重新计算）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
图 3：SwiftUI 的"状态 → 界面"单向数据流
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：状态放哪儿，决定界面重算多大一圈

{class="mt-1"}
一个状态该放在 @State、@Observable 对象还是 SwiftData 模型里，直接决定视图重算的范围。放错了位置，就会出现"改一个字段整页闪"。SwiftUI 的多数"玄学刷新"，最后都能归结到两件事：状态放错了地方，或是把能现算的派生值又存了一份。
:::

##### @ 是什么：属性包装器，有人也叫它装饰器

变量前面那个 @ 不是装饰，是<strong>属性包装器</strong>（Property Wrapper）的标志，给普通变量套上一层"外挂"。第 72 章讲 ArkTS 时用过"装饰器"这个叫法，说的是同一个思想：变量被包装之后，SwiftUI 就能感知它的变化，变化一发生就安排重画。

你不需要关心包装器内部的实现原理，新手期只要记住分工：<code class="inline">@State</code> 管"本页面自己的、会变的小状态"；<code class="inline">@Binding</code> 管"借来的修改权"；<code class="inline">@Environment</code> 管"系统环境塞给你的值"。这三个是本章的主角，第 63 章还有 @Observable 等一众亲戚等着认门。

##### @Binding：把修改权借出去

单页面的 @State 已经够用，可界面一拆成多个组件就遇到新问题：子组件怎么改父组件的状态？答案是 @Binding，父视图把状态的"修改权"借出去，子视图改它，等于改原件：

::: div .code-block
:::inline div .code-head
<span>SWIFT · @Binding 父子接力</span><span class="dots">···</span>
:::

```
struct ParentView: View {
 @State private var isOn = false

 var body: some View {
 VStack {
 Text("开关现在是 \(isOn ? "开" : "关")")
 ChildToggle(isOn: $isOn) // $ ：把"值 + 修改权"一起借出去
 }
 }
}

struct ChildToggle: View {
 @Binding var isOn: Bool // 子视图声明"我借了一个绑定"

 var body: some View {
 Toggle("孩子这边也能控制", isOn: $isOn)
 .padding()
 }
}
```
:::

$ 符号是这段代码的灵魂，读法固定：<strong>父视图写 $isOn 是"把修改权交出去"，子视图声明 @Binding var 是"接住这份修改权"</strong>。打个比方：电视（状态）放在客厅（父视图），遥控器（绑定）借给孩子（子视图），孩子按遥控器，客厅的电视真的会换台，因为遥控器控制的是同一台电视。注意子视图声明用的是 @Binding（不带 $），带 $ 的是"借出"这个动作本身。

<strong>与 ArkUI 对照</strong>：这套父子接力在鸿蒙那边叫 @Prop / @Link（第 73 章讲过），分工几乎一致——单向传值、双向绑定各司其职。概念对上了，框架就不可怕。

##### @Environment：系统塞给你的环境值

有些值你不用自己存——系统早就备好了，放在"环境"里随取随用：<code class="inline">@Environment</code> 就是取用口。最常用的两个：当前深浅色模式（colorScheme）和"关闭当前页面"的动作（dismiss）：

::: div .code-block
:::inline div .code-head
<span>SWIFT · @Environment 两连</span><span class="dots">···</span>
:::

```
struct ThemeCard: View {
 @Environment(\.colorScheme) var colorScheme // 读环境：深浅色

 var body: some View {
 Text(colorScheme == .dark ? "现在是深色模式" : "现在是浅色模式")
 .padding()
 .background(colorScheme == .dark ? Color.black : Color.white)
 }
}

struct EditSheet: View {
 @Environment(\.dismiss) private var dismiss // 拿到"关闭"动作

 var body: some View {
 Button("保存并关闭") {
 dismiss() // 一句话关页面
 }
 }
}
```
:::

（ThemeCard 里写了死的黑白色，只为演示判断逻辑：真实项目请用系统色，第八节细说。）读法上有个格式约定：@Environment 后面括号里写要哪把"钥匙"（<code class="inline">\.colorScheme</code>），变量名随便起。环境值的特点是"只读、系统维护"：colorScheme 会跟着用户设置自动变，你的界面自动跟着重画，一行订阅代码都不用写。这种"值放在环境里、谁需要谁取"的思路，第 63 章的全局状态还会升级出场。

##### 完整示例：一个能用的"饮水打卡"卡片

把 @State、绑定、控件、布局串成一个真实的小界面。这段代码每一行都是前面讲过的，没有新面孔，这正是重点：到这一节为止，你已经能读懂一个完整组件了。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 饮水打卡卡片</span><span class="dots">···</span>
:::

```
struct WaterView: View {
 @State private var cups = 0
 @State private var nickname = ""

 var body: some View {
 VStack(spacing: 16) {
 TextField("你的昵称", text: $nickname)
 .textFieldStyle(.roundedBorder)

 Text("\(nickname.isEmpty ? "朋友" : nickname)，今天喝了 \(cups) 杯")
 .font(.title2)

 HStack(spacing: 12) {
 Button("+1 杯") { cups += 1 }
 .buttonStyle(.borderedProminent)
 Button("重来") { cups = 0 }
 .buttonStyle(.bordered)
 }

 if cups >= 8 {
 Text("今日目标达成！")
 .foregroundColor(.green)
 }
 }
 .padding()
 }
}
```
:::

逐块对号：两个 @State 是这页的全部状态；TextField 用 $nickname 双向绑定；标题文字用插值现算（昵称没填就显示"朋友"——能算出来的就别另存一份，本节开头的告警框说的就是这）；两个按钮各改一次状态；最后那个 if 是"条件界面"——状态达标才出现，不达标自动消失。声明式的味道就出来了：<strong>整个界面是状态的函数，状态一变，一切自动就位</strong>。

##### 状态三纪律：私藏、独源、现算

用 @State 有三条纪律，违反任何一条，迟早会撞上"玄学刷新"。写下来贴在显示器边上：

- <strong>私藏</strong>：@State 加 private，状态是视图的私事，别让外人直改，要改走 @Binding 的正规渠道。
- <strong>独源</strong>：一个数据只有一份原件。同一个值在两处各存一份，迟早改不同步，"单一事实来源"是状态管理的第一性原理。
- <strong>现算</strong>：能从别的状态推出来的值（总数、达标没、文案），现算，不存。存了就是第二份原件，违反上一条。

三条纪律盯着的是同一件事：状态越少、来源越唯一，"界面不对劲"的概率就越低。第 63 章的状态全景图（@Observable、环境对象）看着名头吓人，其实都是在不同规模上执行这三条纪律：页面内部用 @State，跨页面用共享对象，仅此而已。

##### 什么时候传值，什么时候传绑定

拆组件拆多了，你会反复遇到一个选择：给子组件传数据，传"值"还是传"绑定"？判断标准一句话：<strong>子组件要改它，就传绑定（$）；只是显示它，就传值</strong>。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 传值 vs 传绑定</span><span class="dots">···</span>
:::

```
struct Badge: View {
 let count: Int // 只显示：普通参数，let 收下

 var body: some View {
 Text("未读 \(count)")
 .font(.caption)
 }
}

// 调用：Badge(count: unread) —— 不加 $

struct Editor: View {
 @Binding var title: String // 要修改：接绑定

 var body: some View {
 TextField("标题", text: $title)
 }
}

// 调用：Editor(title: $title) —— 加 $
```
:::

默认选择"传值"。传值的子组件更简单、更好复用、更好预览（预览时随手编个数就行）；绑定是一种"授权"，发出去的授权越多，数据流向越难追踪。拿不准时先传值，等子视图真的需要"往回写"再升级成绑定，和第 61 章"先 let 再 var"的思路一模一样，不是巧合，状态管理的哲学是相通的。

先传值。

##### ForEach：把数组变成一排视图

还有个高频配角值得在本节出场：ForEach。数组里有几条数据，就要画几行界面——这个"重复"不用手写，交给 ForEach：

::: div .code-block
:::inline div .code-head
<span>SWIFT · ForEach 初见</span><span class="dots">···</span>
:::

```
struct TagList: View {
 let tags = ["餐饮", "交通", "娱乐"]

 var body: some View {
 HStack {
 ForEach(tags, id: \.self) { tag in
 Text(tag)
 .font(.caption)
 .padding(.horizontal, 10)
 .padding(.vertical, 4)
 .background(Color(.systemGray6))
 .cornerRadius(8)
 }
 }
 }
}
```
:::

那个 <code class="inline">id: \.self</code> 是在告诉 SwiftUI"拿数据本身当身份证"，字符串没有重复时这么用最省事。id 的重要性本章开头提过。SwiftUI 靠 id 认清"哪行是哪行"，数据增删时界面才知道该动谁。等数据变成 struct（第 65 章的账单），就换用 Identifiable 的 id（第 61 章埋的那个伏笔在那就收线了）；更完整的列表玩法（滑动删除、分组）归第 63 章的 List 讲。这里先掌握"数组变视图"这一步。

#### 五、预览、主题与动画：SwiftUI 的"外挂"

- <strong>#Preview 宏</strong>：文件底部加 <code class="inline">#Preview { ContentView() }</code>，右侧画布实时渲染——改代码所见即所得。还能给同一视图写多个预览：浅色/深色、大字体、长文本、空数据各来一个，比手动切设置快得多。
- <strong>深色模式免费</strong>：用系统颜色（<code class="inline">Color(.systemGray6)</code>、<code class="inline">.primary</code>）而不是写死颜色，深色模式自动适配，一行不用多写。
- <strong>动画一行搞定</strong>：<code class="inline">withAnimation { count += 1 }</code> 或给视图加 <code class="inline">.animation(.default, value: count)</code>——过渡丝滑。

预览调布局，真机调手感，大字体、深色模式、动态岛、横竖屏，都要在设备上过一遍才作数。等 App 跑起来觉得"哪儿有点卡"，Xcode 26 的 Instruments 里有 SwiftUI 视图剖析，能看出哪个视图因为哪个状态被反复重建；再往深还有 Processor Trace、CPU Counters 追函数级瓶颈，电池与散热看 Power Profiler。入门阶段混个脸熟即可，知道去哪儿查就行。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 十分钟上手的动画</span><span class="dots">···</span>
:::

```
struct AnimatedHeartView: View {
 @State private var liked = false

 var body: some View {
 Button {
 withAnimation(.spring(duration: 0.4)) {
 liked.toggle()
 }
 } label: {
 Image(systemName: liked ? "heart.fill" : "heart")
 .font(.system(size: 48))
 .foregroundColor(liked ? .red : .gray)
 .scaleEffect(liked ? 1.3 : 1.0)
 }
 }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小贴士：先功能后动画

{class="mt-1"}
新手常犯的毛病是"界面还没做对，就开始纠结动画"。先让功能跑通，最后再统一加动效：动画是锦上添花，功能是雪中送炭。这也是咱们一贯的"简单至上"原则。
:::

##### 预览画布的日常姿势：把第 60 章的开关用熟

画布的开关（⌥⌘↩ 呼出、Resume 唤醒、底部那排设备设置）第 60 章第十节都教过了，这里只补三个"用出价值"的场景。改完布局，先在画布上把外观切到深色过一遍，上一节的系统颜色搭配做得对不对，一试便知；给爸妈做的界面。把动态字体拉到最大档再看一眼，文字截没截断当场现形；写完一个新交互，先进交互模式点两下，确认行为对了再上模拟器。

这套动作养成习惯后，你会发现自己跑模拟器的次数变少了：多数问题在画布上就被拦截，模拟器留给了"真机手感"级别的验收。工具的分工就是这样：画布管快，真机管准。

##### 主题色：一处改，全局换装

颜色还有一个更高层的玩法：App 主色调。第 60 章在 Assets.xcassets 里见过那个 AccentColor 条目——它就是全局主题色的总开关。改掉它的值，你会发现所有按钮、开关、选中的分段控件一夜之间换装，一处修改，全局生效。

个别视图想临时另用别的强调色，用 .tint 修饰符就地覆盖。分工记住一条：全局品牌色归 AccentColor，局部强调色归 .tint，别用满屏的 foregroundColor 手动涂品牌色，那样改主题时你得满代码找补。让系统替你管理一致性，是声明式的一贯作风。

##### 动画的两条心法

上面那个红心例子值得多看两眼，里面藏着动画的两条心法。第一，<strong>动画跟着状态走</strong>：代码里没有任何"从灰色变红"的逐步描述，只有 liked 这一个布尔值的翻转，过渡的每一帧都是系统从新旧两种状态之间插值算出来的。想改动画节奏，改的是 withAnimation 的参数；想改动画的目标，改的是状态本身。

第二，<strong>让所有相关变化都动起来</strong>：颜色、图标、大小三个属性都挂在 liked 上，一次 withAnimation 全都平滑过渡。如果只有一处动了另一处瞬间跳变，多半是那处的变化没被包进动画作用域，把状态修改挪进 withAnimation 的闭包里就好。这两条心法记住，常见的动画小毛病都能自己诊断。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
来动手：做一个"心情按钮"

#### 六、常用修饰符速查：一页在手，界面不愁

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">想做什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">修饰符</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">留白</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.padding(16)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">圆角</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cornerRadius(12)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">背景色</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.background(Color(.systemGray6))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">字体与字号</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.font(.title.bold())</code> / <code class="inline">.font(.system(size: 20))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">前景色（文字/图标）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.foregroundColor(.red)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">撑满宽度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(maxWidth: .infinity)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">固定尺寸</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(width:100, height: 44)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">对齐方式</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack(alignment: .leading)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">透明度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.opacity(0.6)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">阴影</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.shadow(radius: 5)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">点击手势</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.onTapGesture { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">键盘类型</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.keyboardType(.decimalPad)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
SwiftUI 常用修饰符速查

记不住没关系——这页就是用来查的。用得最多的其实就前四个：padding、圆角、背景、字体。

{class="mt-1"}
把模板项目改成一个心情切换器：一个按钮，点击后在 😀开心 → 😢难过 → 😡生气 之间循环切换，文字和背景色跟着变。提示：用数组存三组（文字+颜色），<code class="inline">@State</code> 存下标，点击时 <code class="inline">(index + 1) % 3</code>。做完发给朋友玩，收获第一波"哇你会做 App 了"。
:::

##### 修饰符为什么能一直点下去

速查表里的修饰符能无限链下去<code class="inline">.padding().background().cornerRadius()</code> 想点几个点几个。这不是语法糖障眼法，背后有一个值得知道的事实：<strong>每个修饰符都返回一个"包了一层"的新视图</strong>，像套娃一样，套一层变一点。你在 body 里写的那串代码，最终表达的是一组层层包裹的视图。

理解了"套娃"，第三节的顺序告警就不神秘了：先 padding 再 background，是"先给内容留白、再给整体涂色"；反过来就是"先涂色、再给涂好色的块留白"，包裹顺序不同。结果自然不同。以后看到"背景不对劲""阴影出现在边距外面"，都往"谁包着谁"上想，答案往往一眼可见。

这个模型还有个实用推论：修饰符没有"撤销"<code class="inline">.padding()</code> 套上去就是一层实实在在的包装，没有"把刚才那层去掉"的操作。想调整布局，改代码重新描述，而不是"对着界面修补"。这就是声明式的纪律：界面永远由代码完整描述，不存在"半路手动干预"。

##### 修饰符太多记不住，怎么办

不用记。三件事按顺序做：速查表放在手边，写什么查什么；Xcode 的补全帮你兜底：敲个点号，当前视图能接的修饰符全列出来，选一个试试，画布立刻给反馈；实在拿不准效果。把想做的效果用中文说给编程智能听，让它给一两个候选写法，你挑一个跑。两周下来，你会发现常用的就那十几个——工具的 80/20 法则在修饰符上同样成立。

另外提醒一句：修饰符是 SwiftUI 的"皮肤系统"，和第 61 章的"语言"是两回事。语言特性（Optional、闭包）值得理解到根；修饰符用查的就行，查多了自然记住，别本末倒置。

#### 七、做一个设置页：Form、Section 与控件全家福

第四节的控件零散见过，现在把它们装进真实容器。iOS 的设置页有个标准做法：<code class="inline">Form</code>——自带分组、圆角卡片、滚动能力的表单容器，配上 <code class="inline">Section</code> 划分板块，二十几行就是一个像模像样的设置页：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 设置页</span><span class="dots">···</span>
:::

```
struct SettingsView: View {
 @State private var notifications = true
 @State private var dailyGoal = 8
 @State private var drink = "白开水"
 @State private var startDate = Date()

 var body: some View {
 Form {
 Section("提醒") {
 Toggle("打卡提醒", isOn: $notifications)
 Stepper("每天 \(dailyGoal) 杯", value: $dailyGoal, in: 1...20)
 }
 Section("偏好") {
 Picker("常喝的", selection: $drink) {
 Text("白开水").tag("白开水")
 Text("茶").tag("茶")
 Text("咖啡").tag("咖啡")
 }
 DatePicker("开始日期", selection: $startDate,
 displayedComponents: .date)
 }
 }
 }
}
```
:::

Form 的妙处是"你只管填内容，排版它包了"：每一行自动获得标准的行高、分割线和点击反馈，控件会自动对齐 iOS 设置 App 的样式——用户看到就觉得"是原生的、靠谱的"。Section 的标题参数就是分组抬头，想再加一组就再写一个 Section。

再走一个完整场景：给第 65 章的记账本做"新增一笔账"的表单。金额输入框、分类选择、备注、保存按钮——四样零件，Section 一分，表单就成了：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 新增账单表单</span><span class="dots">···</span>
:::

```
struct AddExpenseForm: View {
 @State private var amountText = ""
 @State private var category = "餐饮"
 @State private var note = ""

 var canSave: Bool {
 Double(amountText) != nil // 金额能转成数字才允许保存
 }

 var body: some View {
 Form {
 Section("金额与分类") {
 TextField("金额", text: $amountText)
 .keyboardType(.decimalPad)
 Picker("分类", selection: $category) {
 Text("餐饮").tag("餐饮")
 Text("交通").tag("交通")
 Text("娱乐").tag("娱乐")
 }
 }
 Section("备注") {
 TextField("可不填", text: $note)
 }
 Section {
 Button("保存这笔账") {
 // 存进数据层——第 64 章见
 }
 .disabled(!canSave)
 }
 }
 }
}
```
:::

注意那个 <code class="inline">canSave</code>——它是个计算属性（第 61 章的老朋友）：能从现有状态推出来的值就现算，不另存一份。金额用字符串接输入，点保存时才转数字，转不成（用户输的不是数）按钮就置灰，校验发生在类型转换的边界上，这是表单处理的标准姿势。这个表单到第 65 章会接到真正的数据层，界面部分你现在就能跑通。

两个延伸。第一，想给这页加个大标题，在最外层加一行 <code class="inline">.navigationTitle("设置")</code>——它属于导航体系的一部分，第 63 章讲 NavigationStack 时会给你完整的导航拼图，这里先尝一口。第二，Form 本质是"分组列表样式"的容器，所以它和 List 是近亲，表单选 Form，普通内容列表选 List，别用反。

<strong>与 Compose 对照</strong>：Compose 没有现成的 Form 等价物，设置页得自己拿 LazyColumn 拼——SwiftUI 在"系统风格页面"这件事上预制程度更高。反过来说，Compose 的自由度更大。两边各有所长，习惯了就好。

#### 八、深色模式与动态字体：把"人人能用"写进代码

第五节说了"深色模式免费"，这一节把"免费"的适用范围说清楚——因为边界感恰恰是新手和熟手的分水岭。免费的只有一件事：<strong>用系统提供的颜色和字号</strong>。一旦写死，免费就变收费。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 系统色与固定色</span><span class="dots">···</span>
:::

```
// 会自己换装的（推荐）：
Text("金额")
 .foregroundColor(.primary) // 主文字色：深浅色模式自动反转
 .background(Color(.systemGray6)) // 系统灰：自动适配

// 写死颜色的（深色模式下会出事）：
Text("金额")
 .foregroundColor(.black) // 深色模式下几乎看不见
 .background(Color.white)
```
:::

常用系统色记几个就够：<code class="inline">.primary</code>（主文字）、<code class="inline">.secondary</code>（次要文字）、<code class="inline">Color(.systemGray6)</code>（卡片底）、<code class="inline">.accentColor</code> / <code class="inline">.tint</code>（App 主色调，第 60 章在 Assets 里见过的 AccentColor）。品牌色当然可以自定义，但给它们建 Asset 颜色条目时，同时配浅色和深色两套值—— Assets 里每种颜色都能填深浅两版，系统自动挑。

##### 动态字体：字号不是你说了算

::: div .code-block
:::inline div .code-head
<span>SWIFT · 语义字号 vs 固定字号</span><span class="dots">···</span>
:::

```
Text("跟系统走")
 .font(.body) // 用户调大字体，这行跟着变大

Text("不跟系统走")
 .font(.system(size: 17)) // 写死了，用户调多大都是 17
```
:::

给爸妈做 App，这个区别是生死线。老年用户多半会把系统字体调到最大档，语义字号会乖乖放大，固定字号纹丝不动：然后你的界面就在他们的手机上显得"字小得欺负人"。检验方法第 60 章教过：模拟器里把字体拉到最大档跑一遍。写代码时的纪律就一条：<strong>正文一律语义字号（.body/.title/.caption），只有装饰性小元素才写死尺寸</strong>。

别写死尺寸。

顺手再加一条"人人能用"的细节：图标按钮最好补一句给读屏用户的说明<code class="inline">.accessibilityLabel("删除这条账单")</code>。纯图标按钮视觉上没问题，但 VoiceOver 读出来只会是"按钮"，加一行说明，视障用户才知道它干嘛的。这一行不写不影响你自己用，写了就是给别人留的门。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小贴士：无障碍不是加分题

{class="mt-1"}
系统色、动态字体、读屏标签这三件事，共同点是"各多写一两行而已"，覆盖的却是深色模式用户、长辈用户、视障用户三大人群。把它们当默认习惯，而不是上架前的"临终关怀"。

<div class="stance-box">
<div class="stance-box-head">作者立场</div>
<p>我的结论：深色模式和动态字体，现在就做，别留到上架前。理由三条：</p>
<ul>
<li>系统色一行顶一行——你写死颜色，深色模式下就得再写一套；</li>
<li>动态字体的代价是"正文一律用 .body/.title/.caption，只有装饰性小元素才写死尺寸"这一条纪律，写完就不再有成本；</li>
<li>长辈用户把系统字体调到最大档时，固定字号的界面会小得没法看——这种问题在真机上才暴露，模拟器里拉一次最大档就能提前看见。</li>
</ul>
<p class="stance-box-note">（无利益相关。触控目标与字号的建议以苹果官方人机界面指南的当前版本为准；作者没有在开发工具上获得任何赞助。）</p>
</div>

:::

##### 顺手一查：触控目标别太抠门

字号之外还有个"能不能点中"的问题。手指不是鼠标光标，可点元素太小时，用户要瞄准半天还可能点偏。写代码时给小图标按钮留足点击区域（padding 撑一下，或 .frame 给个舒适的高度），小屏幕上尤其如此。苹果的人机界面指南对触控目标尺寸有具体建议，需要精确数值时以官方文档为准，记住原则就行：<strong>宁可区域大一点，别让用户练狙击</strong>。

#### 九、动画进阶：transition 与"出场方式"

第五节的动画管"已经显示的东西怎么变"，这一节管"东西怎么出现和消失"。条件渲染（if）加上 <code class="inline">transition</code>，就能指定出场姿势：

::: div .code-block
:::inline div .code-head
<span>SWIFT · transition 出场动画</span><span class="dots">···</span>
:::

```
struct RevealView: View {
 @State private var show = false

 var body: some View {
 VStack {
 Button(show ? "收起" : "展开") {
 withAnimation(.easeInOut(duration: 0.3)) {
 show.toggle()
 }
 }
 if show {
 Text("这里是隐藏内容")
 .padding()
 .background(Color(.systemGray6))
 .cornerRadius(10)
 .transition(.scale.combined(with: .opacity))
 }
 }
 }
}
```
:::

两个零件各司其职：withAnimation 包住状态翻转，负责"什么时候动"；transition 描述"怎么进怎么出"，这里的写法是"缩放叠加淡入淡出"。不加 transition 时系统给个默认的淡入淡出，多数场合也够用，所以 transition 属于"锦上添花的锦上添花"，优先级排在功能、布局、深色模式之后。

写动画还有一条调试窍门：动画不对劲时，先检查状态翻转有没有被包进 withAnimation，再看 transition 参数，九成的"动画没生效"是前者，不是后者。这一节加上第五节的招数，入门阶段的动画弹药已经够用，更炫的活儿等做出第一个完整 App 再说。

动画还有个容易被忽略的受众问题：有的用户系统里开着"减弱动态效果"（晕动症用户、部分老年用户），满屏乱飞对他们不是炫，是折磨。尊重这个设置的写法是读一下对应的环境值，减弱模式就少动或不动，一两行的事，和第八节的动态字体是同一个"人人能用"的思路。新学动画的人不必现在就做，知道有这根弦即可。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
来动手：给"心情按钮"加动画

{class="mt-1"}
回到第六节的心情切换器，加两个动效：文字和背景色变化包进 withAnimation；切换瞬间给整个卡片一个 .transition(.scale.combined(with: .opacity))。改完在画布的交互模式里点几下——同一行业务代码，观感立刻上一个档次。这就是"先功能后动画"的正确打开方式：功能已经稳了，动效是最后穿上的外套。
:::

#### 十、预览画布深玩：多环境、假数据与占位

预览的进阶玩法从"多预览并存"开始。同一个视图，浅色一份、深色一份、大字体一份，#Preview 写三份，画布并排渲染，改一处代码三份齐动：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 多预览并存</span><span class="dots">···</span>
:::

```
#Preview("浅色") {
 WaterView()
}

#Preview("深色") {
 WaterView()
 .preferredColorScheme(.dark)
}

#Preview("大字体") {
 WaterView()
 .environment(\.dynamicTypeSize, .accessibility3)
}
```
:::

第二份用 <code class="inline">.preferredColorScheme(.dark)</code> 把预览环境按进深色；第三份用环境值把动态字体拉到无障碍档——environment 这个词眼熟吧？第四节它还是"读系统值"。这里反过来了：往预览环境里"注入"值。读写是同一个机制的两面，这个认识第 63 章还会加深。

##### 给预览喂假数据

界面写复杂后会撞上鸡生蛋问题：预览要数据，真数据要么还没接、要么涉及隐私。解法是假数据：专门给预览准备的一小份示例：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 预览专用假数据</span><span class="dots">···</span>
:::

```
struct Expense {
 let name: String
 let amount: Double
}

// 示例数据：只给预览和测试用
let sampleExpenses = [
 Expense(name: "午饭", amount: 25.5),
 Expense(name: "地铁", amount: 6.0),
 Expense(name: "一场电影", amount: 45.0),
]

#Preview {
 VStack {
 ForEach(sampleExpenses, id: \.name) { e in
 Text("\(e.name)：\(e.amount) 元")
 }
 }
 .padding()
}
```
:::

第 60 章说过假数据的两条原则，这里补上第三条：<strong>假数据要"长得像真的"</strong>——名字有长有短、金额有小数有整数，排版问题才暴露得出来；全是"测试1""测试2"的预览，等于没测。等正式数据接进来（第 64 章），预览代码里的假数据按需替换就行，界面代码一行不用改。

##### 预览红字了怎么办

预览整片红字，先按第 60 章的三板斧走一遍：点 Resume、关掉重开、⌘R 真跑一次看真实报错。这里补充一个经验判据，帮你分清"预览的错"和"代码的错"：<strong>真跑能过、只有预览红</strong>，多半是预览环境不支持，比如要权限弹窗、要真机的功能，预览给不了，这不是你写错了；<strong>真跑也报错</strong>，才是代码的问题，去问题导航器看第一条。分清这两者，能省下大把自我怀疑的时间。

还有一个提高预览命中率的小习惯：预览只编译当前文件相关的内容，所以它比整个 App 快得多：但反过来说，跨文件的全局改动（改了公共模型）会让预览需要重build，慢是正常的。等它，别疯狂点击；预览的进度条和你焦虑的程度成正比，和速度无关。

##### 预览的边界：三件事它干不了

夸了半天预览，把边界也说清，免得你拿它当万能：权限弹窗（相机、相册、定位）在预览里出不来——这类流程要上模拟器或真机验证；真实推送、真机传感器（相机取景、指南针）预览没有；性能数据全部不算数，预览跑在你 Mac 的算力上，动画卡不卡必须真机说话。第 60 章那张"模拟器与真机分工对照"表，在这里同样适用，把"模拟器"换成"预览"就行。

#### 十一、界面调试门诊：不刷新、红屏与"为什么没反应"

第 60 章埋了个话头："第 62 章调试专题会细讲"，现在兑现。界面调试的病种和语言调试不同，前三名常年霸榜：改了不刷新、编译一片红、点了没反应。逐个开方。

<strong>病例一：改了状态，界面不刷新。</strong>按概率排查四步：第一步，变量前面有没有 @State——没包装的普通变量，改了系统不知道，这是第一大病因；第二步，你是不是改了"副本"——值类型赋值即复制（第 61 章的 Wallet 实验），如果你把状态拷给了另一个变量再改，原件纹丝不动，界面当然不动；第三步，改的是不是 let——let 的东西根本改不了，编译器应该已经拦过你了；第四步，画布没醒就点 Resume，模拟器抽风就重启 App。四步走完，大部分"玄学"现出原形。

先查 @State。

<div class="case-box">
<div class="case-box-head">翻车现场</div>
<p>一个计数器的界面，点了按钮，数字纹丝不动。检查了四遍代码，@State 加了，let 没用，闭包里的赋值也没问题。最后发现：状态被拷进了另一个变量，闭包里改的是那份拷贝，原件一直没动。</p>
<p class="case-box-quote">"按钮点了，count 就是不变"</p>
<p class="case-box-src">场景来源：全书通用场景（非特定读者）</p>
<p><strong>怎么办</strong>：按四步走，别跳步。第一步查 @State，第二步查副本——值类型赋值即复制，把状态拷给别人再改，原件当然不动。第三步查 let，第四步重启 App。四步走完，"玄学"基本会现出原形；确实还没头绪，再把相关代码连同"这个视图为什么没刷新"一起问编程智能当第二意见。</p>
</div>


<strong>病例二：编译报"无法在合理时间内完成类型检查"。</strong>这串英文报错（unable to type-check in reasonable time）吓坏过无数新手，其实病因很朴素：<strong>body 里一口气写了太多层嵌套和修饰符，编译器算不动了</strong>。解法不是等，是拆——把大 body 拆成几个子视图，每个子视图结构简单，编译器各个击破。顺便说，拆视图本来就是好习惯，这个报错等于编译器在督促你整洁。

拆成子视图。

<strong>病例三：点击没反应。</strong>三个常见嫌疑：按钮被 .disabled 了（检查条件）；点的是手势不是按钮，手势区域和视觉区域不一致（比如图片上盖了透明层）；或者闭包里改的是"拷贝"而不是状态——又回到病例一的第二步。排查工具还是那招老实的 print：在闭包第一行 print 一下，看代码到底有没有执行到，"没执行"和"执行了没效果"是两个完全不同的诊断方向。

先打印一行。

<strong>病例四：图标或图片不显示。</strong>四个嫌疑按顺序排：SF Symbols 的名字拼错了（heart.fill 写成 hear.fill，静默失败不报错）；本地图片没拖进 Assets 或名字不一致；图片忘了 .resizable 却给了很大的 frame，被裁得只剩一角；或者网络图片压根没加载完——网络图的加载与占位，第 64 章讲完网络请求后你会有一套完整方案。"图片不显示"几乎从来不是玄学，是名字或资源没对上。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小贴士：把编程智能当第二意见

{class="mt-1"}
自己排查两轮还没头绪，把"这个视图为什么没刷新"连同相关代码一起问 Xcode 26 的编程智能——第 60 章装好它时就打过照面。它的价值在"第二意见"：先自己想，再看它说，两边对不上的地方往往就是盲区。直接伸手要答案，练不出自己的诊断力。
:::

最后把本章的调试手段收拢成一句话：状态可疑就 print，布局可疑就换预览环境，刷新可疑就查 @ 和副本，报错可疑就拆视图。这四句话覆盖界面开发前三个月的绝大多数疑难，第 67 章的调试三板斧（print、断点、预览）会把 print 这条线接到新的高度。

#### 十二、滚动、键盘与长文本：长内容的三个现实问题

##### 内容超出屏幕：ScrollView 来兜底

Form 自带滚动，但普通页面内容一多（比如说明页、详情页）就会溢出屏幕底，解决办法是套一层 ScrollView：

::: div .code-block
:::inline div .code-head
<span>SWIFT · ScrollView</span><span class="dots">···</span>
:::

```
ScrollView {
 VStack(alignment: .leading, spacing: 12) {
 Text("使用说明")
 .font(.title.bold())
 Text("第一段：这是一段很长的说明文字，页面会滚动。")
 Text("第二段：内容再多也不怕，滚到哪画到哪。")
 // ……更多内容
 }
 .padding()
}
```
:::

用法就一句：<strong>把原来那坨内容包进 ScrollView</strong>，竖向滚动自动获得。它也支持横滚，把方向参数改成 .horizontal，里面配 HStack，就能做出"横向滑动的标签墙、封面列表"，很多 App 首页的横滑区就是这么来的。记住 ScrollView 和 Lazy 家族的分工：ScrollView 管滚动这件事本身，LazyVStack 管省着渲染；内容真的很多时，两个叠着用（ScrollView { LazyVStack { ... } }）是标准姿势。

##### 键盘弹出，会不会挡住输入框

会不会？绝大多数情况不会：SwiftUI 默认就做了键盘避让：键盘弹起时，系统自动把界面往上顶，输入框会露在键盘上方。这个"默认值"是老框架时代无数新手哭出来的福利，现在白送。

要留意的反而是两件小事。一是键盘的收起：点键盘外的区域默认不收键盘，给界面加个点击手势收起键盘是常见做法，新版本系统还支持"往下滑动收起键盘"的修饰符，用法现查现用。二是回车键的行为：给输入框加 <code class="inline">.submitLabel(.done)</code> 之类，能把键盘右下角那个键从"换行"变成"完成"，表单填写顺手不少。真遇到极端布局（输入框在屏幕最底部又顶不上去）再研究，新手期罕见。

##### 长文本与超长数字：截断的艺术

::: div .code-block
:::inline div .code-head
<span>SWIFT · 截断三招</span><span class="dots">···</span>
:::

```
Text(长文本)
 .lineLimit(3) // 最多三行，超出省略
 .lineLimit(nil) // 不限行数（写 nil 是"不限"）

Text("0000000000000000000")
 .minimumScaleFactor(0.5) // 空间不够时允许缩到一半大

Text("超长的账号名显示不下")
 .truncationMode(.middle) // 中间省略：保留头尾
```
:::

三招各管一种尴尬：说明文字限行数、长数字允许缩小、长账号中间打点。特别是最后那个 middle 截断。展示订单号、设备号这类"头尾重要中间冗长"的东西，用户一看就懂。这些招数都是"提前设计"，比上线后看监控里"文字被截断投诉"便宜得多。

#### 十三、反馈三件套：让每次点击都"有回音"

界面的高级感，一半来自"反应快"，另一半来自"反应明确"。用户点了一下，界面必须有回音，没回音的按钮，用户会连点三次，然后怀疑 App 死了。SwiftUI 的反馈三件套，按场景对号入座。

<strong>第一件：即时视觉反馈。</strong>系统按钮（bordered 系列）自带按压效果，不用你操心；自定义的点击区域用 onTapGesture 的，可以自己加一点按压变化（透明度、缩放），一行修饰符的事。原则是"看得见的元素，点它就要有动静"。

<strong>第二件：结果反馈——弹窗与确认。</strong>操作有结果（成功、失败、需要确认）时，用 alert 说清楚：

::: div .code-block
:::inline div .code-head
<span>SWIFT · alert 提示</span><span class="dots">···</span>
:::

```
struct AlertDemo: View {
 @State private var showSaved = false

 var body: some View {
 Button("保存") {
 showSaved = true // 改状态触发弹窗
 }
 .alert("已保存", isPresented: $showSaved) {
 Button("好", role: .cancel) { }
 }
 }
}
```
:::

注意声明式的味道：弹窗的显隐也是状态（showSaved）驱动的，改状态，弹窗自动出现；点掉，状态自动归位。和界面别的部分一模一样，没有"showDialog()"这种命令式调用。删除之类的破坏性操作，记得给按钮标 <code class="inline">role: .destructive</code>，系统会自动把它染成警示红。需要多选项的确认场景，换成从底部弹出的操作面板 confirmationDialog：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 确认面板</span><span class="dots">···</span>
:::

```
.confirmationDialog("确定删除这笔账？", isPresented: $showConfirm,
 titleVisibility: .visible) {
 Button("删除", role: .destructive) {
 // 真正执行删除
 }
 Button("取消", role: .cancel) { }
}
```
:::

它的挂法和 alert 一样，挂在视图上、由状态驱动。破坏性操作前加一道确认，是界面设计里少数"永远不该省"的步骤：手滑的代价，远大于多点一下的麻烦。

<strong>第三件：过程反馈——加载指示。</strong>网络请求、大计算进行中，给个 ProgressView（系统转圈组件），结束时换成结果界面。三种界面状态（加载中 / 成功 / 失败）的完整打法，第 66 章的天气 App 会专门练——这里先记住原则：<strong>等待超过一眨眼的工夫，就要给"正在处理"的信号</strong>，沉默的等待最伤信任。

#### 十四、界面检查清单：一屏做完的十项自检

本章知识点很多，最后压成一张"交稿自检单"。以后每做完一屏，按顺序过一遍，全绿才算完：

1. 画布切深色模式过一遍：没有写死的黑底白字。
2. 动态字体拉到最大档过一遍——没有截断、没有溢出。
3. 空数据状态过一遍，列表为空时显示的是友好提示，不是白屏。
4. 超长文本过一遍，换成十几个字的标题和几百字的备注试试。
5. 最小屏幕过一遍：画布换最小机型，按钮还点得到、文字还完整。
6. 键盘过一遍，点输入框，键盘弹出不挡关键内容。
7. 每个图标按钮都有 accessibilityLabel——读屏用户能听懂。
8. 条件按钮的置灰逻辑检查过，表单没填完提交是灰的。
9. 每个点击都有反馈，要么有变化，要么有提示，没有"沉默的按钮"。
10. 模拟器真跑一次：画布定稿，真机验收，两条腿走路。

十项看着多，练熟后过完一屏不超过五分钟：因为它们是"顺手检查"，不是"返工工程"。这张清单和第 60 章的报错门诊、第 61 章的自检清单一脉相承：把专业习惯变成固定动作，你就已经比大多数"能跑就行"的业余选手专业了。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
一句话记牢

{class="mt-1"}
界面写完只算一半，检查通过才算做完。你替用户多想一步，用户就少骂你一句。
:::

#### 十五、新手 FAQ：界面开发的十个高频问题

<strong>问：SwiftUI 和 UIKit 到底学哪个？听说老项目都是 UIKit。</strong><br>答：学 SwiftUI，本书主线也是它。UIKit 是历史存量，维护老项目才深接触；新项目在 2026 年已经是 SwiftUI 的天下。真遇到 UIKit 代码，看懂大意即可，不用回头重学。

<strong>问：画布预览和模拟器，我该信哪个？</strong><br>答：分工不同。布局、颜色、多环境适配信画布（快、可切条件）；交互手感、真实性能、系统弹窗信模拟器和真机（准）。画布骗不了布局，但也替代不了真机。

<strong>问：修饰符的顺序我总记不住，有什么口诀吗？</strong><br>答：与其背口诀，不如记住"套娃"模型——修饰符从上到下就是从里到外包。想要"边距也在背景里"就先涂色再留白，想要"边距露在外面"就先留白再涂色。拿不准就两种都写一遍，画布秒回答案。

<strong>问：@State 为什么都建议加 private？不加也能跑。</strong><br>答：能跑，但状态变成了"全项目可改"的公共变量——谁都能伸手，出问题就查无此人。加 private 是把修改权锁在本视图内，这是第四节"状态三纪律"的第一条，白拿的保险。

<strong>问：我把状态传给子组件改了，父界面怎么没变？</strong><br>答：大概率是传成了"值"而不是"绑定"——子组件拿到的是复制品，改的是复制品。把调用处的参数改成 $ 开头、子组件的属性声明改成 @Binding，再试。第四节末尾那张传值/传绑定的对照就是为这个坑准备的。

<strong>问：动画要学到什么程度？我看别人的 App 动效超炫。</strong><br>答：本章两节（withAnimation 加 transition）够用到第一个 App 上线。炫技动效是锦上添花的锦上添花，花在上面性价比极低——用户对"顺滑"的感知远大于对"炫"的感知。

<strong>问：界面代码要不要写注释？感觉代码已经很直白了。</strong><br>答：少写"这行在干嘛"的翻译式注释（代码自己会说话），多写"为什么这么设计"的动机式注释——为什么这个按钮要置灰、为什么这里间距特别大。后者才是三个月后最需要的信息。

<strong>问：学完这章，我离做出一个真 App 还差什么？</strong><br>答：差三块拼图：页面跳转与列表（第 63 章）、数据存储与网络（第 64 章）、把零件组装成完整项目的两次实战（第 65、66 章）。界面是这三块里最先到位的，你已经有了。

<strong>问：我照着抄教程代码，为什么还是报错？</strong><br>答：三个常见原因：教程的框架版本和你的不一样（以官方文档的当前写法为准）；抄代码时漏了配套的 @State 或绑定（它们常常定义在代码块外面）；或者字段名拼错了——抄代码最怕"看起来一样"，逐字符比对再跑。

<strong>问：界面的"设计感"怎么练？我做的总是很土。</strong><br>答：先抄后创。把系统自带的设置 App、提醒事项一个个界面用 SwiftUI 复刻一遍，间距、字号、颜色全对着调——复刻三个界面，审美自然校准。本章的三件套加速查表就是复刻的全部词汇量，缺的只是练习。

#### 十六、误区清单：六个"想当然"

<strong>误区一：以为声明式就是"不用懂逻辑了"。</strong>恰恰相反，逻辑全在你身上——只是从"指挥过程"变成了"描述结果"。状态怎么设计、数据怎么流动，想得越清楚界面越稳。声明式省的是体力，费的是脑力，赚的是可靠。

<strong>误区二：以为 body 重算很浪费，要提前优化。</strong>SwiftUI 的重算和渲染经过大量优化，日常规模（几十个视图）感知不到开销。新手期的优化动作几乎都在帮倒忙——把简单代码拆得七零八落。等 Instruments 告诉你哪里慢（第五节那个工具），再动手不迟。

<strong>误区三：以为画布里的效果就是最终效果。</strong>画布是"近似"——真机的手感、字体渲染、性能表现只有设备知道。养成收尾习惯：画布定稿，模拟器过一遍，真机过一遍，三层验收。第 60 章那条"预览调布局，真机调手感"值得再念一遍。

<strong>误区四：以为深色模式要单独做一套界面。</strong>做两套是命令式思维。正确的做法本章第八节全给了：系统色、语义字号、Assets 里的深浅两版品牌色——同一套代码，两种外观，系统负责切换。觉得"深色模式是大工程"的人，多半是写死了颜色。

<strong>误区五：以为所有状态都塞一个 @State 就行。</strong>@State 适合"本页面的、简单的小状态"。状态一多、要跨页面共享、要和服务器同步，就该升级工具——第 63 章的 @Observable 就是为这些场合准备的。在错误的规模上硬扛错误的工具，是"玄学刷新"的另一半来源。

#### 十七、给三类背景读者的建议

这本书的读者来自三个方向，每个人在 SwiftUI 门口的起点和陷阱都不一样。对号入座，各取一份攻略。

##### 从安卓来：Compose 老同学（第 51 章）

你的起点最高，思想完全同构，这张表就是你的翻译词典：@Composable 函数 ↔ View 结构体（一个用函数一个用 struct，SwiftUI 的组件是有 body 的类型）；remember + mutableStateOf ↔ @State；状态上提 + 回调 ↔ @Binding（SwiftUI 把这件事做成了语法）；Column / Row ↔ VStack / HStack；LazyColumn ↔ LazyVStack / List。

要留神的差异有两处。一是预览方式：Compose 的 @Preview 和 SwiftUI 的画布思路一致，但 SwiftUI 的画布交互更深（交互模式、环境开关），值得重新适应；二是修饰符模型：Compose 是参数和 Modifier，SwiftUI 是链式包装，"顺序有意义"这条两边道理相同、写法不同，别肌肉记忆。状态管理往下走（第 63 章的 @Observable）时，你会在 ViewModel 的老朋友身上看到新面孔。

##### 从鸿蒙来：ArkUI 老同学（第 73 章）

你甚至不用换概念名：@State 和 SwiftUI 同名同义，ArkUI 官方文档本来就是对着 SwiftUI 的模型设计的。对照表更短：@State ↔ @State；@Prop / @Link ↔ @Binding（单向借值、双向绑定一一对应）；@Entry / @Component ↔ App / View 的层级；build { } ↔ body；Column / Row ↔ VStack / HStack；@Watch ↔ 下一章的观察类工具。

要留神的差异：ArkTS 是 TypeScript 的收紧版，SwiftUI 这边的语言是 Swift，语法差异比框架差异大得多，第 61 章的对照表值得回炉；装饰器在 ArkTS 是语言级扩展，SwiftUI 的 @ 是属性包装器，机制不同、用法形似，"会用但别乱类比"是稳妥姿势。

##### 从网页前端来：React 老同学

你带来的最大资产是"组件思维"：React 的函数组件 + useState + 单向数据流，和 SwiftUI 是同一套哲学的不同实现，JSX ↔ body，useState ↔ @State，props 传值 ↔ 构造参数传值，状态上提 ↔ @Binding。布局上，HStack/VStack 相当于 flex 的横排/竖排，Spacer 相当于 flex-grow，思维可以平移。

要留神的差异有三处。第一，Swift 是编译型强类型语言，没有 any 的舒适区——第 61 章的类型系统要真正学进去，这在你那边通常是最大的坎。第二，没有 CSS：样式即视图（修饰符直接写在视图上）。别找样式表，也别惦记类名复用：复用靠拆子组件。第三，"重新渲染"的心智可以保留（SwiftUI 的 body 重算和 React 的 re-render 几乎同频），但 useMemo 那套手动优化习惯先收起来，SwiftUI 会自己处理大多数场景。

三个背景都不占的纯零基础同学，你们的攻略只有一条：按书页顺序走。第 61 章的语言底子没打牢就冲进界面章，是唯一被历史反复验证的翻车路线——不是不可能成功，是成功的人后来都回头补了语言课。慢慢来，比较快。

最后给三类人一句共同的提醒：无论从哪来，都别用旧框架的直觉给 SwiftUI "纠错"。见过 Compose 同学把 @State 当 remember 手动层层传、见过 ArkUI 同学在新代码里硬写 ObservableObject、见过前端同学试图建一个"全局样式表"：都工作，但都逆着框架的 grain（纹理）。SwiftUI 的答案是现成的：状态归 @State、共享归 @Observable、样式归修饰符和 Assets。先用框架的方式做成一件事，再谈个人风格。

<strong>误区六：以为"能跑"就等于"做完了"。</strong>跑起来只是及格线，深色、大字体、空数据、反馈这四关（第十四节的清单）没过都不算完工。业余和专业的差距，从来不在"会不会写"，而在"写完之后检查什么"。

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小结

- SwiftUI 是声明式：描述"长什么样"，系统负责画和重画
- 视图 = 遵守 View 协议的结构体；body 描述界面；修饰符链式"上妆"
- 四大基础视图：Text / Button / TextField / Image；SF Symbols 图标库免费管饱
- 布局三件套：VStack 竖排、HStack 横排、ZStack 叠放；Spacer 是弹性空间
- @State 让界面活起来；$ 双向绑定喂给输入框
- #Preview 所见即所得；系统颜色自动适配深色模式；withAnimation 一行动效
:::
