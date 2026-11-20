---
id: di-wu-shi-yi-zhang
num: 51
part: an-zhuo-kai-fa-pian
nav: 第五十一章：界面开发——Jetpack Compose入门
toc: default
kind: chapter
---

### 第五十一章：界面开发——Jetpack Compose 入门

{class="chapter-intro mb-4"}
界面是用户看到的一切。在 Compose 出现之前，安卓界面用 XML 写，像填空题一样繁琐；2021 年谷歌推出了 <strong>Jetpack Compose</strong>：直接用 Kotlin 代码「画」界面，所见即所得，改一行代码预览立刻刷新。到 2026 年，Compose 已是新项目的绝对主流。这一章，咱们学会「画画」。

::: div .quick-read
##### 本章速读（5 分钟版）
这一章教你「画界面」。安卓界面以前用 XML 写，像填空题一样繁琐；现在用 Jetpack Compose，直接用 Kotlin 代码画，改一行代码，预览窗立刻刷新。核心思想一句话：<strong>界面就是函数</strong>——每个能显示在屏幕上的东西，文字、按钮、图片，都是一个「可组合函数」，像积木一样嵌套起来就是界面。到 2026 年，Compose 已是新项目的绝对主流，这一章学的是通用手艺：iPhone 的 SwiftUI、鸿蒙的 ArkUI 走的是同一套路子。

最关键的有两件事。一是思路整个倒过来了：以前是「找到控件、手动改属性」，现在只写「每种状态长什么样」，星星按钮写成「收藏了就红色，没收藏就灰色」，状态一变界面自己跟上。记住这句话：<strong>界面是状态的函数，状态对界面就对，界面错先查状态</strong>。二是所有组件的参数都是同一个形状：「当前是什么 + 变了怎么办」。TextField 是 value 加 onValueChange，Checkbox 是 checked 加 onCheckedChange。认出这个形状，以后碰到任何陌生组件都不用怕，接上状态就能用。还有一条整理经验顺手带走：组件参数超过五六个就该收拢，一个可组合函数在编辑器里超过一屏就该拆，按顶部栏、列表区、底部操作条这样的视觉块拆，拆完每块还能单独预览。给图片写的 contentDescription 是念给读屏软件听的，给爸妈做的 App 尤其省不得。

今天就能做的最小动作：打开 Android Studio 的模板项目，给你的第一个组件加上 @Preview，再叠两份带参数的预览：一份深色模式、一份大字体，一个函数三副面孔并排看全。这不到十分钟，能让你亲身体会「从主题取色、跟着系统字体走」为什么值钱。章里那个「心情按钮」（点一下在开心、难过、生气之间循环切换）也是半小时内能做完的练手，做完发给朋友，收获第一波夸奖。

最大的坑提前立牌。第一，输入框死活打不进字，九成是 onValueChange 没接上状态，TextField 显示什么完全由 value 决定，回调断了它就装死。第二，按钮点了没反应，多半是忘了 remember 加 mutableStateOf，普通变量没人观察，界面就是不理你。第三，列表一滑就卡，先查 LazyColumn 配没配 key、条目里有没有干重活。另外 Modifier 的顺序有意义：先留白再涂色和先涂色再留白，差一圈白边，拿不准就调换顺序，预览立刻告诉你答案。
##### 速查表
- 界面怎么搭：Column 竖排、Row 横排、Box 叠放，三种盒子拼出所有页面
- 输入框打不进字：value 和 onValueChange 都要接状态，链条断一环就装死
- 旋转后表单丢光：用户亲手输入的内容一律用 rememberSaveable
- 出现奇怪白边：Modifier 顺序有意义，调换顺序看预览是万能排查法
- 长列表怎么写：LazyColumn 加 key，key 用稳定的 id，别用数组下标
- 深色模式怎么适配：颜色一律从 colorScheme 取，别写死色值
- 图片别忘无障碍：contentDescription 写清楚是什么，纯装饰图明确传 null
- 界面不刷新：先查状态链是不是断了，链没断再查重组路径上的重活
:::

<div class="version-anchor">本章界面路径按 iOS 18.x / HarmonyOS 5.x / Android 15 核对（2026 年 11 月）。你的机型或系统版本不同，菜单名字和位置可能对不上——以你手机上显示的为准。</div>


#### 一、Compose 的思想：界面就是函数

Compose 的核心思想一句话：<strong>界面 = 函数</strong>。每个能显示在屏幕上的东西（文字、按钮、图片）都是一个「可组合函数」（Composable），用 <code class="inline">@Composable</code> 标记。把它们像积木一样嵌套起来，就是界面。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 第一个 Compose 界面</span><span class="dots">···</span>
:::

```
@Composable
fun Greeting(name: String) {
 Text(text = "你好，$name！") // 一个"文字积木"
}

// 嵌套组合：大积木套小积木
@Composable
fun HomeScreen() {
 Column { // 竖着排列
 Greeting(name = "张三")
 Greeting(name = "李四")
 Button(onClick = { /* 点击做什么 */ }) {
 Text("点我")
 }
 }
}
```
:::

注意 <code class="inline">@Composable</code> 这个「帽子」，它告诉编译器「这是一个界面积木」。积木可以无限嵌套，这就是 Compose 的全部秘密。

##### 入口在哪：那几行「套娃」代码

新建模板项目时，MainActivity 里有一小段让人困惑的代码：<code class="inline">setContent { MyFirstAppTheme { ... } }</code>。翻译一下：setContent 是 Activity 和 Compose 之间的桥，「从这个窗口开始。界面归 Compose 管」；里面套的主题和页面函数，就是你画的界面。除了这一处，整章的代码都活在「函数画函数」的世界里，不用再碰 Activity 的细节。以后看任何 Compose 项目，都从这行 setContent 顺着往里读。还有个福利：@Preview 的预览不经过 Activity，所以改界面时连 App 都不用启动。

##### 从「改界面」到「重画界面」：两种做事思路

拿一个最常见的场景开刀：收藏按钮。用户一点，星星图标从灰色变红色。XML 时代的做法分三步，在代码里找到那颗星星、判断当前状态、手动把颜色改掉。每多一个会变的东西，就多一摊「找控件、改控件」的代码；漏改一步，界面和数据就对不上。这类 bug，老安卓工程师修了快十年。

Compose 把思路整个倒过来：不写「怎么改」，只写「每种状态长什么样」。星星写成「收藏了就红色，没收藏就灰色」，收藏状态一变，界面自己跟上。你从「修表匠」变成了「画图纸的人」，图纸上写清楚所有情况，钟表具体怎么走，不归你管。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">对比点</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">XML 时代（命令式）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Compose（声明式）</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">你要做的事</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">找到控件，手动改属性</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">描述"状态对应的样子"</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">谁负责刷新</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">你自己，容易漏</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">框架自动，状态变了就重画</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数据和界面不一致</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最常见的 bug 来源</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">界面永远跟着状态走</td></tr>
</tbody>
</table>
```
:::

这套思路有个公式化的说法：<strong>界面是状态的函数</strong>。同样的状态，永远画出同样的界面。你要操心的只剩一件事，把状态管对。

还有件事值得偷着乐：这不是安卓一家的发明。iPhone 的 SwiftUI、鸿蒙的 ArkUI 走的是同一套声明式路子。概念几乎能一一对上。你在这一章花的时间，买的是一张「通用方言」的门票。

##### 可组合函数的四条规矩

- <strong>函数名首字母大写</strong>：Greeting、HomeScreen、Avatar。这是社区的硬约定，可组合函数名像名词，代表「屏幕上的一块东西」；普通函数小写开头。混着写，内行一眼看穿。
- <strong>只描述，不返回东西</strong>：可组合函数没有返回值，它的全部工作是把「要显示什么」告诉 Compose。
- <strong>可能被执行很多次</strong>：这是新手最容易心理失衡的一条。你以为函数只跑一次，Compose 实际会反复调用它。所以函数体里别做耗时操作、别发网络请求、别弹对话框，这些和「画界面」无关的事，第八节讲重组时再敲一次黑板。
- <strong>随便嵌套、随便组合</strong>：小函数拼成大函数，大函数拼成整个屏幕。你上一步写的 Greeting，下一步就能塞进 HomeScreen。

顺带拆一个常见懵点：<code class="inline">Button(onClick = { ... }) { Text("点我") }</code> 里，大括号包着的 <code class="inline">Text(「点我」)</code> 是什么？它是 Button 的「内容槽」。Kotlin 的尾 lambda 语法，意思是「按钮里显示的东西」。你会在 Compose 里到处见到这个形状：末尾一个 lambda，装着子积木。

##### 从外往里读：快速看懂一段 Compose 代码

新框架最劝退的时刻，是打开示例项目一屏代码看不懂。给你一个读法：像剥洋葱，从最外层函数开始，只看两件事，它用了哪些布局盒子（Column、Row、Box），它引用了哪些子函数。子函数里面写了什么，第一遍跳过。

这样读的好处：任何复杂界面，剥两三层就见底，最里面无非是 Text、Button、Image 这些基础积木。XML 时代你要在几十层嵌套的标签树里找根，Compose 代码天生就是一棵函数调用树，从树根往下读，层次和屏幕上的视觉层次一一对应。读代码的顺序，就是眼睛扫过界面的顺序。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
一句话记牢

{class="mt-1"}
界面是状态的函数：状态对，界面就对；界面错，先查状态。
:::

#### 二、基础组件：文字、按钮、输入框、图片

Compose 的组件就是「积木块」，最常见的四种：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">组件</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">干什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">必备参数</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">显示文字</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">text（要显示的字）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">按钮</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onClick（点击回调）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">输入框</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">value、onValueChange（输入变化回调）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">显示图片</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">painter（图片资源）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Compose 四大基础组件

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 基础组件示例</span><span class="dots">···</span>
:::

```
@Composable
fun BasicWidgets() {
 Column {
 Text(text = "这是一段文字")
 Button(onClick = { println("被点击了") }) {
 Text("按钮")
 }
 var input by remember { mutableStateOf("") }
 TextField(
 value = input,
 onValueChange = { input = it },
 label = { Text("输入点什么") }
 )
 }
}
```
:::

输入框那两行里出现了 <code class="inline">remember { mutableStateOf("") }</code>——这就是 Compose 的「状态」魔法，本章第五节细讲。现在先混个脸熟。

##### Text：最常用，也最容易被低估

Text 看着最简单，实际承担了界面里一半的信息量。真正常用的招数就三样，看一段新闻列表里的真实写法：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Text 的三板斧</span><span class="dots">···</span>
:::

```
Text(
 text = news.title,
 maxLines = 2, // 最多两行
 overflow = TextOverflow.Ellipsis, // 放不下就省略号
 style = MaterialTheme.typography.titleMedium // 字号字体听主题的
)
```
:::

场景很具体：新闻标题长短不一，不截断会把整行撑乱，maxLines 加 overflow 是新闻、聊天、商品列表的标配组合。style 那一行是重点：字号别写死，用主题的排版档位，深色模式和大字体适配会顺带解决：第五节展开。

##### Button：一大家子，不止一种

实心的 Button 只是老大，它还有几个兄弟姐妹：长相不同，用法完全一致，都吃一个 onClick。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 按钮家族</span><span class="dots">···</span>
:::

```
Button(onClick = { /* 主操作 */ }) { Text("立即下单") }
OutlinedButton(onClick = { /* 次要操作 */ }) { Text("看看就好") }
TextButton(onClick = { /* 轻量操作 */ }) { Text("跳过") }
IconButton(onClick = { /* 图标点击 */ }) {
 Icon(Icons.Default.Favorite, contentDescription = "收藏")
}
```
:::

挑选逻辑不复杂：一屏里最重要的操作用实心 Button，别超过一两个；次要操作用描边的 OutlinedButton；「跳过」「取消」这类轻量操作用 TextButton；工具栏上的小图标用 IconButton。还有个 enabled 参数：传 false 按钮自动变灰、不可点。「协议没勾选就不能注册」这类联动，全靠它——下面 Checkbox 会现场演示。

##### TextField：value 加 onValueChange 是铁律

先看一个新手必踩的坑，输入框怎么都打不进字。有人在这上面卡过半小时，一度怀疑自己键盘坏了：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 错误示范</span><span class="dots">···</span>
:::

```
// 错误示范：只给了值，没接"值变了怎么办"
TextField(value = "固定的", onValueChange = {})
```
:::

TextField 在 Compose 里是「受控组件」：它显示什么，完全由你传进去的 value 决定。用户敲键盘时系统回调 onValueChange，你在里面把新值存进状态，界面才会跟着变。链条断在任何一环，输入框就「装死」。正确姿势是让状态住进去：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 正确姿势</span><span class="dots">···</span>
:::

```
var address by remember { mutableStateOf("") }
TextField(
 value = address,
 onValueChange = { address = it }, // it 是用户敲进去的新内容
 label = { Text("收货地址") },
 singleLine = true
)
```
:::

常用参数再报两个名字：keyboardOptions 决定弹出什么键盘（数字、邮箱、网址），visualTransformation 配 PasswordVisualTransformation() 就是密码打点。这些不用背，用到时查官方文档，两分钟的事。

##### 实战连线：搜索框加清空按钮

组合两个组件解决一个真需求：输入内容时右侧出现小叉，一点就清空。别小看这个细节，几乎所有带搜索的 App 都有它，而它恰好是「value + 回调」的绝佳练习：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 搜索框</span><span class="dots">···</span>
:::

```
var query by rememberSaveable { mutableStateOf("") }
TextField(
 value = query,
 onValueChange = { query = it },
 label = { Text("搜歌曲、歌手") },
 singleLine = true,
 trailingIcon = {
 if (query.isNotEmpty()) {
 IconButton(onClick = { query = "" }) {
 Icon(Icons.Default.Close, contentDescription = "清空")
 }
 }
 }
)
```
:::

trailingIcon 是输入框预留的「尾巴槽」，里面放任意组件。注意那个 if 写在槽里：query 为空时，清空按钮干脆不进入组合，而不是画出来再藏起来，这也是声明式的习惯：不显示，就不组合。这个小组合可以原样搬进你自己的项目。

##### Icon：无处不在的小零件

图标在界面里的出场率比图片还高：返回箭头、放大镜、三个点的更多菜单。Compose 里用 Icon 组件，Material 自带的图标库有几百个现成的，一行就能放进去：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 放一个图标</span><span class="dots">···</span>
:::

```
Icon(
 Icons.Default.Search,
 contentDescription = "搜索",
 tint = MaterialTheme.colorScheme.primary // 颜色也听主题的
)
```
:::

三件事值得注意：图标名在 IDE 里敲出 Icons.Default. 会自动弹候选列表，翻一遍比联网搜快；contentDescription 的规矩和图片一样，有含义的写清楚，纯装饰的明确传 null；颜色用 tint 从主题取，别写死。深色模式自动成立。图标配文字的组合，通常包进 Row，或者直接用带 label 参数的按钮。

##### Image：contentDescription 别空着

显示本地图片用 <code class="inline">Image(painterResource(R.drawable.avatar), ...)</code>。第一个参数好理解，第二个参数 contentDescription 才是想敲黑板的地方：它是写给屏幕朗读（TalkBack）听的。视障用户靠读屏软件「听」界面，图片对他们是一片空白——除非你写了描述。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 有含义的图和装饰图</span><span class="dots">···</span>
:::

```
Image(
 painter = painterResource(R.drawable.avatar),
 contentDescription = "用户头像", // 有含义的图：写清楚是什么
 modifier = Modifier.size(48.dp)
)
// 纯装饰性的图（背景花纹之类），明确传 null，读屏会跳过它
Image(painter = painterResource(R.drawable.pattern), contentDescription = null)
```
:::

这不是选修课。给爸妈做的 App、要上架商店的 App，读屏描述都是基本盘。养成习惯：每放一张图，先问自己一句「这张图被读出来，用户听到的是什么」。

##### Checkbox、Switch、RadioButton：三个状态小件

这三个长相不同，参数结构一模一样：checked（当前状态）加 onCheckedChange（状态变了怎么办）。又是「value + 回调」的铁律。直接上真实场景，注册页的协议勾选：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 勾了才能点</span><span class="dots">···</span>
:::

```
var agreed by remember { mutableStateOf(false) }

Row(verticalAlignment = Alignment.CenterVertically) {
 Checkbox(checked = agreed, onCheckedChange = { agreed = it })
 Text("我已阅读并同意用户协议")
}
Spacer(Modifier.height(12.dp))
Button(
 onClick = { /* 注册 */ },
 enabled = agreed // 勾了才亮
) { Text("注册") }
```
:::

这十几行是真实 App 里出现频率最高的联动之一：勾协议才能注册、开关打开才生效、单选决定配送方式。写完这一段，你对「状态驱动界面」的理解就超过大部分初学者了。选型上跟着语义走：Switch 适合「开/关」设置项，RadioButton 适合三四选一，Checkbox 适合独立的是/否，别因为哪个好看就乱用。

##### 发现没有：组件参数的「通用形状」

把这一节的组件排成一排看参数：Button 是「内容 + onClick」，TextField 是「value + onValueChange」，Checkbox 是「checked + onCheckedChange」，Image 是「内容 + contentDescription」。全部同一个形状：<strong>当前是什么 + 变了怎么办</strong>。

认出这个形状，新组件就不用一个一个学了。以后碰到任何陌生组件（滑块、评分条、日历），先找两个东西：它要的「值」，和它给的「回调」。接上状态，就能用。API 文档几千页，骨架其实就这么一条。

#### 三、布局三件套：Column、Row、Box

组件有了，怎么摆放？记住三个「盒子」：

- <strong>Column</strong>：竖着排（像排队打饭）。
- <strong>Row</strong>：横着排（像并排坐）。
- <strong>Box</strong>：叠着放（像扑克牌摞一起，适合做角标、遮罩）。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 布局三件套</span><span class="dots">···</span>
:::

```
Column {
 Text("第一行")
 Row {
 Text("左边")
 Text("右边")
 }
 Box {
 Text("底层")
 Text("叠在上面的角标")
 }
}
```
:::

想让布局更好看？给组件加 <strong>Modifier</strong>（修饰符），它就像给积木「上妆」：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Modifier 常用招式</span><span class="dots">···</span>
:::

```
Text(
 text = "好看的文字",
 modifier = Modifier
 .padding(16.dp) // 四周留白
 .fillMaxWidth() // 撑满宽度
 .background(Color.Blue) // 背景色
 .clickable { /* 点击 */ }// 可点击
)
// 链式调用：一个接一个，顺序有意义（先 padding 再背景，背景不含边距）
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：Modifier 的顺序有讲究

{class="mt-1"}
<code class="inline">padding(16.dp).background(Blue)</code> 和 <code class="inline">background(Blue).padding(16.dp)</code> 效果不同——前者是「先留白再涂色」（背景不含边距），后者是「先涂色再留白」（背景包含边距）。新手最容易在这上面画错「奇怪的白边」。不确定时，调换顺序试试，预览立刻告诉你答案。
:::

##### 排列与对齐：让内容「站对位置」

三个盒子只是开始，决定「好看不好看」的是两个参数：Column 带 verticalArrangement（子项之间怎么分配空隙）和 horizontalAlignment（子项在水平方向怎么对齐），Row 反过来对应一套。最常见的实战是「列表行左边标题、右边时间」：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 一行两端的经典排法</span><span class="dots">···</span>
:::

```
Row(
 verticalAlignment = Alignment.CenterVertically,
 modifier = Modifier.fillMaxWidth()
) {
 Text("订单详情", modifier = Modifier.weight(1f)) // 占据剩余宽度
 Text("14:23")
}
```
:::

weight(1f) 单独说一句：它把一行或一列的剩余空间分给某个子项。上面例子里「订单详情」吃掉了除时间以外的全部宽度，列表行左标题右时间的布局，全靠这一招。空隙分配还有 Arrangement.SpaceBetween（两端对齐）、SpaceEvenly（均匀分），各试一遍就有体感。间距不够时插一个 <code class="inline">Spacer(Modifier.height(8.dp))</code>，比硬凑 padding 清晰得多。dp 这个单位顺带解释：它是「密度无关像素」，在低分屏和高分屏上物理大小接近，写界面一律用 dp，别用裸像素。

##### Modifier 常用招式速查

正文里出现过四个，实战里高频的其实是一小撮，收进一张表：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Modifier</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">干什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">一句话备注</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">padding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">留白</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最高频，没有之一</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">size(48.dp)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">固定大小</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">头像、图标常用</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">fillMaxWidth()</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">撑满宽度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">配 weight 用更灵活</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">background(Color)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">背景色</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">顺序影响范围（见前面避坑提醒）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">clip(圆角形状)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">按形状裁剪</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">圆角卡片感就靠它</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">clickable { }</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">整块可点</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">让任意组件有按钮行为</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">alpha(0.6f)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">透明度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">禁用态、遮罩常用</td></tr>
</tbody>
</table>
```
:::

这张表不用背，写两周自然长在手上。唯一的「心法」就是避坑提醒里那句：顺序有意义，拿不准就调换试试。另外注意，Compose 里没有「margin」这个概念，外间距也是 padding，加在哪个位置效果不同，习惯了反而比网页那套简单。

##### Box 的实战：角标、遮罩、悬浮按钮

三件套里 Box 最少被讲透，却是「高级感」的秘密来源。凡是「叠在另一个东西上面」的视觉，消息红点、图片上的价格标签、右下角的悬浮按钮——全是 Box。看一个消息红点：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 图标 + 红点角标</span><span class="dots">···</span>
:::

```
Box {
 Icon(
 Icons.Default.Notifications,
 contentDescription = "通知",
 modifier = Modifier.size(32.dp)
 )
 Box(
 modifier = Modifier
 .size(10.dp)
 .align(Alignment.TopEnd) // 钉在右上角
 .clip(CircleShape)
 .background(Color.Red)
 )
}
```
:::

Box 里的子项默认全部叠在同一个位置；想挪动某个子项，用 align 指定它贴在哪。外层 Box 多大？默认「裹」住最大的子项——图标 32dp，红点就钉在它的右上角。把红点换成半透明黑色块，是图片上的遮罩；换成小按钮，是悬浮操作按钮。一个思路，三种效果。

##### 拼一张真实的卡片：聊天列表的一行

来把三件套和 Modifier 串成一个真场景。微信、QQ、短信，列表每一行都长一个样：左边头像，中间两行字（名字加最后一条消息），右边时间。用 Compose 写出来是十几行：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · ChatRow.kt</span><span class="dots">···</span>
:::

```
@Composable
fun ChatRow(name: String, lastMessage: String, time: String) {
 Card(modifier = Modifier.fillMaxWidth()) {
 Row(
 modifier = Modifier.padding(12.dp),
 verticalAlignment = Alignment.CenterVertically
 ) {
 Image(
 painter = painterResource(R.drawable.avatar),
 contentDescription = null, // 行整体有文字，头像算装饰
 modifier = Modifier
 .size(48.dp)
 .clip(CircleShape)
 )
 Spacer(Modifier.width(12.dp))
 Column(modifier = Modifier.weight(1f)) {
 Text(name, style = MaterialTheme.typography.titleMedium)
 Text(
 lastMessage,
 maxLines = 1,
 overflow = TextOverflow.Ellipsis,
 style = MaterialTheme.typography.bodySmall
 )
 }
 Text(time, style = MaterialTheme.typography.bodySmall)
 }
 }
}
```
:::

逐层拆一下：外层 Card 给出圆角和阴影；Row 负责横向布局；头像固定 48dp；中间 Column 用 weight 吃掉剩余宽度，所以消息再长只截断消息、不挤压时间；时间永远靠右。这个骨架可以直接搬去改造成订单行、通讯录行、播放列表行：手机上七成的列表行，都是这个结构换了张皮。

##### 从 XML 翻译过来：一张过户对照表

如果你以前写过 XML 布局，旧知识其实大半能「过户」。收进一张表，翻译时对号入座：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">XML 里的老朋友</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Compose 里的对应物</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">LinearLayout（竖）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Column</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">LinearLayout（横）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Row</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">FrameLayout / 叠放</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Box</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">layout_weight</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">weight(1f)</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">gravity / layout_gravity</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Arrangement（管子项之间）+ Alignment（管单个子项）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">margin</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">没有 margin，用 padding 的位置变化实现</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">RecyclerView + Adapter + ViewHolder</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">LazyColumn + items</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">include 标签</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">抽成一个小 Composable</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">dp / sp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不变：尺寸用 dp，字体用 sp（跟系统大字体走）</td></tr>
</tbody>
</table>
```
:::

ConstraintLayout 一行没列，因为多数界面用 Row、Column、Box 组合就够了；真遇到复杂的相对定位需求，再去看官方的对齐方案。对照着写两三个页面，肌肉记忆就切换完了。真正需要重建的只有一样：过去「改一行布局、重新编译、等半天」的循环，现在预览窗秒回，你会发现调布局这件事突然变得「愿意调了」。

##### 新手三连：为什么我的界面一片空白

写完第一个页面，运行起来全黑或全白，一般就三种原因：一是忘了在 setContent 里把你的页面函数放进去，界面压根没被组合；二是所有东西都没给尺寸、又没有内容撑开：空盒子里塞空盒子；三是颜色写死成和背景一样，自己把自己隐形了。排查口诀三步走：先确认「放进组合没有」，再看「有没有内容撑开」，最后看「是不是被颜色藏住了」。三步下来，空白基本都有主。这三步也顺手教了你一个重要直觉：界面出了问题，先想「它有没有被画出来」，再想「画得对不对」，顺序别反。

#### 四、状态：让界面「活」起来

静态界面没意思。想让按钮点击后数字 +1、输入框能打字，就需要<strong>状态（State）</strong>。Compose 的规则：<strong>界面永远忠实反映状态，状态变了，界面自动重画</strong>。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 状态：点击计数器</span><span class="dots">···</span>
:::

```
@Composable
fun Counter() {
 // remember + mutableStateOf：记住这个会变化的值
 var count by remember { mutableStateOf(0) }

 Column {
 Text(text = "你点了 $count 次")
 Button(onClick = { count++ }) { // 改状态
 Text("点我 +1") // 界面自动刷新
 }
 }
}
```
:::

三行代码，一个活的计数器。这就是 Compose 比老式写法爽的地方：<strong>不用手动「刷新界面」，改数据就行</strong>。记住两个关键函数：<code class="inline">remember</code>（让值在界面重组时不被清空）和 <code class="inline">mutableStateOf</code>（告诉 Compose「这个值变了要重画」）。

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"> 用户点击</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"> 状态改变（count++）</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"> Compose 感知到变化</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"> 自动重画界面（重组）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
图 3：Compose 的「状态 → 界面」单向数据流
:::

##### remember 和 mutableStateOf：两个词各管一半

<code class="inline">var count by remember { mutableStateOf(0) }</code> 这行代码信息量不小，拆成三块看：

- <strong>mutableStateOf(0)</strong>：造一个「能被观察的盒子」，里面装着 0。它自带 Compose 的观察机制，哪个界面读了它，哪个界面就被登记成「订户」。
- <strong>remember</strong>：别忘了这个盒子。Compose 会反复执行你的函数（第八节细讲），没有 remember，每次执行都会造一个新盒子、旧值清零，计数器会永远停在「你点了 1 次」。
- <strong>by</strong>：Kotlin 的委托语法糖，让你直接写 count，不用写 count.value。少敲几个字符，多出无数清爽。

不信可以做个对照实验：把那行换成 <code class="inline">var count = 0</code> 普通变量，点按钮，屏幕纹丝不动。代码在跑、值在变，界面就是不理你，因为普通变量没人观察。「点击没反应」这个新手第一大坑。八成是漏了 remember 和 mutableStateOf 其中一个。

##### rememberSaveable：旋转屏幕也不丢

还得知道 remember 的边界：它的记忆只活在「这个界面被显示」期间。用户退出这个页面再回来，值重置；旋转屏幕这类导致界面重建的操作，同样清零。想象用户填了一半的收货地址，转个屏全没了——差评就是这么来的。想扛住旋转，用它的兄弟 rememberSaveable：用法一模一样，框架自动把简单值（字符串、数字、布尔）存起来，界面重建后原样恢复。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 换一个词，扛住旋转</span><span class="dots">···</span>
:::

```
var address by rememberSaveable { mutableStateOf("") }
```
:::

复杂对象的自定义恢复规则（Saver）先不展开，多数时候你存的是几个字符串和数字，默认机制够用。原则记住一条：<strong>用户亲手输入的内容，一律 rememberSaveable</strong>。

##### 状态提升：谁拥有状态，谁说了算

计数器把状态写在自己肚子里，没问题。真实项目很快遇到两种情况：两个组件要共用同一个状态——顶部的搜索框和中间的列表都要用搜索词；或者你写了一个漂亮组件想复用，可它肚子里藏着一个写死的状态，放到哪儿都水土不服。

解法叫「状态提升」：把状态从组件肚子里拿出来，交给调用方；组件只收「值 + 回调」两个参数。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 把状态上交</span><span class="dots">···</span>
:::

```
// 无状态版本：值从外面来，变化也交回外面
@Composable
fun Counter(count: Int, onIncrement: () -> Unit) {
 Column {
 Text("你点了 $count 次")
 Button(onClick = onIncrement) { Text("点我 +1") }
 }
}

// 有状态的调用方：状态住在这里
@Composable
fun CounterScreen() {
 var count by remember { mutableStateOf(0) }
 Counter(count = count, onIncrement = { count++ })
}
```
:::

术语对一下：带状态的叫「有状态组件」（stateful），只收参数的叫「无状态组件」（stateless）。社区的主流做法是：能无状态就无状态，状态尽量往上提，提到「需要它的那几个组件的共同祖先」那里。好处实打实：状态只有一个源头，不会两处显示对不上；无状态组件拿假数据就能预览、能测试；将来状态要搬家，界面代码一行不用改。

##### 状态放哪：一张决策表

「这个状态该放哪」是写 Compose 时每天都要回答的问题，起步期用这张表当路标：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">什么样的状态</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">放哪儿</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">只影响当前页面的临时值（草稿、展开收起、计数）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">remember</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">要扛住旋转屏幕、界面重建</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">rememberSaveable</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">要跨页面存活、和业务逻辑相关</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ViewModel 这类专门容器（超出本章范围，官方文档有完整指南）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">从服务器拿回来的数据</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数据层，界面只管显示</td></tr>
</tbody>
</table>
```
:::

这张表不是铁律。判断错了也没关系，状态提升意味着你随时能给状态「搬家」，这正是它的另一层好处。真正不能破的是两条底线：别把用户输入放普通变量，别用 remember 硬扛跨页面数据。

##### 练手场：一个能用的迷你表单

把本节零件装进一个真实场景：昵称和手机号两个输入框，两个都填对才允许点「下一步」。几乎所有 App 的注册流程都是这个雏形：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · MiniForm.kt</span><span class="dots">···</span>
:::

```
@Composable
fun MiniForm() {
 var nickname by rememberSaveable { mutableStateOf("") }
 var phone by rememberSaveable { mutableStateOf("") }
 val canSubmit = nickname.isNotBlank() && phone.length == 11

 Column(Modifier.padding(16.dp)) {
 TextField(
 value = nickname,
 onValueChange = { nickname = it },
 label = { Text("昵称") },
 singleLine = true,
 modifier = Modifier.fillMaxWidth()
 )
 Spacer(Modifier.height(8.dp))
 TextField(
 value = phone,
 onValueChange = { phone = it },
 label = { Text("手机号") },
 singleLine = true,
 modifier = Modifier.fillMaxWidth()
 )
 Spacer(Modifier.height(16.dp))
 Button(
 onClick = { /* 提交 */ },
 enabled = canSubmit,
 modifier = Modifier.fillMaxWidth()
 ) {
 Text(if (canSubmit) "下一步" else "先填完整再点我")
 }
 }
}
```
:::

三处细节值得圈出来：状态用 rememberSaveable，旋转不丢；canSubmit 是个「派生值」，由两个状态现算出来，不单独存，单独存就可能对不上；按钮文案跟着状态变，填完整它才说「下一步」。这个模式可以直接抄进注册页、发帖页、收货地址页，改改字段就行。

#### 五、主题与深色模式：一次配置，全局生效

模板项目里的 <code class="inline">MyFirstAppTheme { ... }</code> 就是主题。它基于 <strong>Material 3</strong> 设计规范，帮你把颜色、字体、形状统一管理。支持深色模式只需三步：

1. 在主题里定义好浅色/深色两套配色（模板已自动生成 <code class="inline">ColorScheme</code>）。
2. 系统切到深色模式时，<code class="inline">isSystemInDarkTheme()</code> 自动判断。
3. 用主题提供的颜色（如 <code class="inline">MaterialTheme.colorScheme.primary</code>）而不是写死颜色值。

##### colorScheme 的槽位：颜色也要「对号入座」

Material 3 的配色是一套「槽位」系统：primary 是主色；onPrimary 是「主色上面放内容该用的颜色」；surface 是卡片和表层的底色；background 是页面底色……on 开头的一族，说的都是「叠在某个色之上的内容用什么色」。你用 <code class="inline">MaterialTheme.colorScheme.primary</code> 取色，取到的永远是「当前浅色/深色模式下的正确颜色」。

这就是第三节清单里「不要写死颜色值」的原因：写死一个深灰色，浅色模式下正常，深色模式下文字直接糊进背景。反过来，只要全 App 都从槽位取色，深色模式是自动送的，你可能一行布局代码都不用改。字体同理：MaterialTheme.typography 里从特大标题到辅助小字有一整排档位，对应中文 App 就是「页面大标题、卡片标题、正文、辅助说明」几档。设计感的一半来自克制，另一半来自统一。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小贴士：Material 3 动态取色

{class="mt-1"}
Android 12 起的「Material You」能让 App 从你的壁纸里提取颜色。Compose 模板默认支持（<code class="inline">dynamicColor</code>）。你的 App 在不同用户手机上会「自动换装」，这就是现代安卓的浪漫。
:::

动态取色打开或关闭，是主题文件里一个参数的事。想验证效果：把模拟器的壁纸换一张，App 的按钮和强调色跟着变：第一次看到会觉得挺神奇，背后就是主题把「从壁纸提取的配色」填进了那些槽位。

##### 动主题去哪儿改：模板里的三个文件

新建项目的 ui/theme 目录里通常躺着三个文件：Color.kt 放颜色定义，Theme.kt 放主题装配（浅色、深色两套配色就在这里），Type.kt 放排版档位。想换品牌色，去 Color.kt 改那几个颜色值，全 App 一起变；想调全局字号，去 Type.kt。改完预览立刻见效——这也是「一次配置」的意思：集中在几处，改一处，全局跟。

##### 两套配色怎么配：先抄基准，再逐个微调

Color.kt 里会看到 lightColorScheme(...) 和 darkColorScheme(...) 两个方法，各自收一整套槽位。新手别一上来就给十几个槽位全填自己的颜色：先把模板生成的基准配色留着，只改 primary 和少数几个你能明显感知差异的槽位，界面立刻变成你的品牌色，还不会出现「配出一个看不清的按钮」。配色这门手艺讲究基准先行：一口气全改，等于什么都没改；逐个槽位微调、每改一次看一眼预览，才是正路。判断改得好不好只有一个标准。文字放上去，看得清吗？

#### 六、预览、动画与实时编辑：Compose 的「外挂」

Compose 三个开发体验上的「外挂」，用上就回不去：

- <strong>@Preview 预览</strong>：给 Composable 加 <code class="inline">@Preview</code> 注解，Android Studio 右侧立刻渲染出界面——改代码所见即所得，不用每次装到手机上（预览窗渲染不出来怎么排查？下一节专门讲）。
- <strong>实时编辑（Live Edit）</strong>：2026 年的 Android Studio 支持在模拟器/真机上「热更新」部分改动，改文字颜色之类的小调整，设备上秒变。
- <strong>动画 API</strong>：<code class="inline">animateFloatAsState</code>、<code class="inline">AnimatedVisibility</code> 几行代码就能让元素平滑过渡，「高级感」往往就差这几十行。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 十分钟上手的动画</span><span class="dots">···</span>
:::

```
@Composable
fun AnimatedBox() {
 var big by remember { mutableStateOf(false) }
 // 值变化时自动平滑过渡到目标值
 val size by animateDpAsState(if (big) 120.dp else 60.dp)

 Box(Modifier
 .size(size)
 .background(MaterialTheme.colorScheme.primary)
 .clickable { big = !big }
 )
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小贴士：先功能后动画

{class="mt-1"}
新手常犯的毛病是「界面还没做对，就开始纠结动画」。先让功能跑通，最后再统一加动效——这也是「简单至上」原则：<strong>动画是锦上添花，功能是雪中送炭</strong>。
:::

##### @Preview 的实用参数：预览窗也能「换装」

@Preview 不只是「能渲染」，加几个参数它就变成你的多机型检查台：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 一个组件，三副面孔</span><span class="dots">···</span>
:::

```
@Preview(showBackground = true, name = "浅色")
@Preview(showBackground = true, name = "深色",
 uiMode = Configuration.UI_MODE_NIGHT_YES)
@Preview(showBackground = true, name = "大字体", fontScale = 1.3f)
@Composable
fun ChatRowPreview() {
 MyFirstAppTheme {
 ChatRow(name = "妈妈", lastMessage = "记得吃饭", time = "12:30")
 }
}
```
:::

uiMode 让预览直接以深色模式渲染——深色适配不用真机来回切；fontScale 把字体放大，模拟系统里开了大字体的用户（给爸妈做 App 的人，这个参数值得常开）。一个函数可以叠多个 @Preview，浅色深色、大字小字在预览窗里并排一屏看全。顺带一提：预览函数里直接传假数据就行——这正是第四节「状态提升」的回报，无状态组件才预览得这么轻松。

##### 预览还能点：交互模式

预览默认是「静态照片」，但预览工具栏里有个交互模式开关，打开后预览里的按钮真的能点、开关真的能拨、状态真的会变，不用启动模拟器就能检查一段交互逻辑。旋转、深色切换这类环境变化，工具栏里也有对应按钮。具体入口随 IDE 版本会挪位置，以你手上的 Android Studio 界面为准，认准「交互」两个字就行。

##### 动画其实就三招

上面代码里的 animateDpAsState 属于第一招：animate 开头的一族函数，「值从 A 变到 B 时自动平滑过渡」，尺寸、颜色、位置都有对应版本。第二招 AnimatedVisibility 管出现和消失：加载中的转圈、错误提示条这类「有时有、有时没」的元素，套上它就自带淡入淡出和展开收起。第三招 animateContentSize 管容器尺寸自适应：聊天气泡变高、卡片展开详情，不至于「啪」一下跳变。

三招的共同点：你只声明目标值，中间每一帧框架替你算。这是声明式思路的延续，连动画都是「描述结果，不写过程」。想玩弹簧、关键帧这类更细的，Compose 也有更深的 API，但先把这三招用熟，界面的「高级感」已经能上一档。

#### 七、依赖与预览的实用细节

写界面之前，先把依赖与预览这两件小事理顺，后面能省掉大量「为什么预览不出」的排查时间：

- <strong>BOM 一次声明</strong>：<code class="inline">implementation(platform(「androidx.compose:compose-bom:2026.08.00」))</code>，之后 <code class="inline">material3</code>、<code class="inline">ui</code>、<code class="inline">ui-tooling-preview</code> 都不写版本。
- <strong>稳定版与预览版分开</strong>：稳定线是 Compose UI 1.12.1 / Material 3 1.4.0；1.13 与 1.5 还在 beta/alpha。学习项目一律用稳定版。
- <strong>预览要单独加依赖</strong>：<code class="inline">debugImplementation</code> 加 <code class="inline">ui-tooling</code>，<code class="inline">implementation</code> 加 <code class="inline">ui-tooling-preview</code>，预览窗才渲染得出来。
- <strong>状态驱动刷新</strong>：第四节的「状态变 → 重组 → 界面更新」要记牢：别在 Composable 里直接改业务对象，状态放进 remember 或 ViewModel。
- <strong>预览与真机都要看</strong>：预览快，但不等同真机；深色模式、大字体、横屏这三类问题，只在真机上暴露。

##### BOM 到底替你管了什么

Compose 不是一个库，是一组库：ui、material3、foundation、ui-tooling，每个有自己的版本号，相互之间还有兼容关系。BOM（物料清单）做的事是「打包配平」：你声明一次 BOM 版本，清单里的每个库自动用官方配平过的版本，不用逐个填数字，也不会踩「版本不配套」的坑。升级时改 BOM 一行，全体跟进。

所以社区的好办法就一句：Compose 相关依赖一律走 BOM；个别不在清单里的库（导航、部分第三方库）才单独写版本。选哪个版本？跟着 Android Studio 新建项目自动生成的走，那是当下被官方配平的组合，比自己拍脑袋靠谱。

::: div .tip-box .rounded-lg .p-4 .mb-3
{class="font-semibold"}
一句话记牢

{class="mt-1"}
Compose 的难点不是控件 API，是「状态放在哪」。把这一句想清楚，大部分界面 bug 会自己消失。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
来动手：做一个「心情按钮」

{class="mt-1"}
把模板项目改成一个心情切换器：一个按钮，点击后在 😀开心 → 😢难过 → 😡生气 之间循环切换，文字和背景色跟着变。提示：用 <code class="inline">when</code> 根据状态选文案和颜色。做完发给朋友玩，收获第一波「哇你会做 App 了」。
:::

#### 八、重组：Compose 怎么决定「重画」谁

前面几节反复出现「重组」这个词：状态变了，Compose 重新执行你的函数，界面随之刷新。听起来像「整个界面推倒重画」，其实不是：重组的粒度是单个函数，而且 Compose 会聪明地跳过「参数没变」的函数。理解这一节，你就能解释大部分「为什么它没刷新」和「为什么列表卡」的问题。

##### 重组是函数级的，不是屏幕级的

Compose 执行你的函数时，会顺手记录「谁读了哪个状态」。状态一变，它不重画全屏，只重新执行「读了那个状态的函数」。计数器的例子里，count 变了，只有 Counter 这个函数重新跑一遍，屏幕上别的东西一动不动。这就是为什么「把状态放进尽量小的函数」是性能常识：状态被读的范围越小，需要重组的范围越小。

还有第二层省力：重新执行一个函数之前，Compose 会对比它的参数。参数没变，整个函数直接跳过。所以一个页面函数重组时，底下没收到新参数的子组件全部原地待命。理解了这两层，「Compose 会不会很卡」的担忧基本可以放下——它比你想象的省力得多。

拿第十节的导航场景感受一下：从列表页跳详情页时，只有「收到新 id 的详情页」被重新组合，列表页在后台纹丝不动；你从详情页返回时，列表页接到的还是原来那些参数，一样不用重画。页面越多，你越能体会到这种「哪里变改哪里」的省心，这套机制存在的意义就一条：不浪费力气画没变的东西。

##### 三条性能守则

- <strong>别在重组路径上做重活</strong>：可组合函数会被反复执行，函数体里别排序、别算哈希、别读数据库。需要计算的，用 <code class="inline">remember(输入) { 计算 }</code> 缓存，输入不变就返回上次结果。
- <strong>别把「现场新建的对象」当参数传</strong>：每次重组都新建一个列表，Compose 会认为参数变了、跳过机制失效。列表提前算好存起来，或者用 lambda 传下去（Compose 对 lambda 有特殊豁免）。
- <strong>读状态的范围要小</strong>：让「角标数字」的变化只连累角标所在的函数，而不是整个页面。

错误示范长这样：在 Composable 里直接写 <code class="inline">val sorted = messages.sortedBy { it.time }</code>——每次重组都重排一遍，消息一多，滑动立刻卡。正确姿势是 <code class="inline">val sorted = remember(messages) { messages.sortedBy { it.time } }</code>：只有 messages 变了才重排。一行改动，天壤之别。

还有一条红线：可组合函数里别直接「做事」，弹提示、写文件、发请求。这些叫副作用，官方给的出口是 LaunchedEffect 这类专门 API（大意是「界面显示时，帮我执行一次某个动作」）。本章点到为止，你记住「函数体里只描述界面，不干别的」就够了。

##### 亲眼看到重组：两个小办法

重组看不见摸不着，但有两个办法让它现形。笨办法：在 Composable 函数体里加一行日志，运行时看它打印的频率：适合快速验证「这个函数到底被执行了几次」，别玩太久，日志本身也吵。正经办法：Android Studio 的 Layout Inspector，连上设备后能实时显示每个组件的重组次数，哪个组件重组得比想象中频繁，一眼露馅。

使用节奏建议：写界面时不看，卡顿了再看。它像体检报告，平时盯着容易焦虑，出问题时看能快速定位。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
一句话记牢

{class="mt-1"}
重组不可怕，可怕的是你亲手放在重组路径上的重活。
:::

#### 九、列表：LazyColumn 与 LazyRow

界面最重的活永远是列表：几百条聊天记录、上千个商品。Compose 的答案叫 LazyColumn：「懒」的竖排列表。懒在哪：屏幕外的条目根本不创建。给它一万条数据，它只组合屏幕上看得见的那几条，滚到哪、创建到哪。相比之下，用 Column 硬塞一万条 Text，等于让手机把一万条全部画出来，卡是应得的。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 联系人列表</span><span class="dots">···</span>
:::

```
val contacts = remember { listOf("张三", "李四", "王五", "赵六") }

LazyColumn {
 items(contacts, key = { it }) { name ->
 ChatRow(name = name, lastMessage = "最近消息", time = "12:30")
 }
}
```
:::

内容写在 LazyColumn 自己的 lambda 里：<code class="inline">item { }</code> 放单个东西（比如列表顶部的公告条），<code class="inline">items(集合) { }</code> 放批量，lambda 的 it 就是当前这条数据。第三节写的 ChatRow 到这里终于有了用武之地：一条数据一个 ChatRow，列表就成了。

<code class="inline">key = { it }</code> 值得单独讲。默认情况下，Compose 按位置识别列表条目：删除第 3 条，后面所有条目都「换了身份」，各自的内部状态会串位——A 条目被展开的状态跑到 B 条目头上，这类玄学 bug 的根源多半是没配 key。给了 key，每个条目有了身份证：删掉谁回收谁，别人原地不动。凡是会增删的列表都配上 key，值用数据里稳定的唯一标识（id、主键），别用数组下标。

横滑列表就是 LazyRow，参数一模一样：商品页的图片墙、首页的「猜你喜欢」胶囊标签，全是它。两个坑提前说：一，LazyColumn 内部别再嵌同方向的 LazyColumn，两个「懒人」抢同一个滚动方向，表现就是滑不动或闪跳，需要嵌套时改成固定高度或换布局思路；二，每个列表条目写成独立 Composable（像 ChatRow 那样），别把一坨代码塞在 items 的 lambda 里，条目组件化之后能复用、能单独预览，第六节的 Preview 参数正好在上面练手。

##### 网格和粘性头：Lazy 家族的亲戚

列表不止一列。相册、商品货架那种格子，用 LazyVerticalGrid，用法和 LazyColumn 一个路数，只是多了「几列」的参数；长列表里的分组标题想「粘」在顶部不随滚动消失，官方提供了粘性头的现成玩法（文档里搜 sticky header）。整个 Lazy 家族都是同一套心法：懒加载、可配 key、条目拆成组件。学会 LazyColumn，亲戚们只是改个参数的事。

##### 懒加载的小账本：内存为什么不会爆

把「懒」算成账就明白了：普通 Column 是「数据有多少，画多少」，内存占用跟着数据量涨；LazyColumn 是「屏幕能看见多少，画多少」，内存占用只跟屏幕大小相关，跟数据量无关。一万条和一百条。滑动同样流畅：这不是魔法，是把「看不见就不创建」执行到了底。理解这笔账，你就明白为什么滚动列表一律用 Lazy 系，而普通 Column 更适合「数量固定的少数几行」。

#### 十、页面导航：Navigation Compose 入门

真实 App 都有「页面」：列表页点进详情页，详情页进设置页。Compose 的界面是函数，没有「页面」这个天然概念，谁来管切换？官方答案是 Navigation Compose：给每个页面起一个路由名（就是字符串），框架负责「哪个路由显示哪个函数」。三个角色先认个脸：

- <strong>NavController</strong>：导航总管，记录你去过哪些页面、现在在哪。
- <strong>NavHost</strong>：一个舞台，根据当前路由决定把哪个 Composable 搬上台。
- <strong>composable(「路由名」) { 页面函数 }</strong>：把路由和页面绑起来的节目单。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 两个页面的完整导航</span><span class="dots">···</span>
:::

```
@Composable
fun App() {
 val navController = rememberNavController()
 NavHost(navController = navController, startDestination = "list") {
 composable("list") {
 ContactListScreen(
 onOpenDetail = { id -> navController.navigate("detail/$id") }
 )
 }
 composable("detail/{id}") { entry ->
 val id = entry.arguments?.getString("id")
 DetailScreen(id = id, onBack = { navController.popBackStack() })
 }
 }
}
```
:::

逐句看：startDestination 是启动时显示的页面；<code class="inline">navigate(「detail/$id」)</code> 跳详情页，路由里的 {id} 是占位符，跳转时填真实值；详情页从 entry.arguments 里把 id 取出来用；popBackStack() 就是「返回上一页」。返回栈不用手动管：navigate 压栈、popBackStack 弹栈，系统返回键自动接上。传复杂对象先不急，字符串路由能覆盖绝大多数页面传参场景，真遇到再查官方文档。

##### 传参细节：id 怎么进路由，结果怎么带回来

路由参数支持带类型：<code class="inline">detail/{id}</code> 之外还能写 <code class="inline">detail/{id}?tab=1</code> 这类查询参数，取出时用对应的方法解析。给一条经验：路由里传 id 这类「地址」，页面内容让详情页自己去取，别把整个对象序列化了塞进路由，又长又容易出错。

A 页面跳到 B 页面、B 把选择结果带回 A 的场景（比如从地址列表选一个回填订单页），官方文档里有「返回结果给前一页面」的专门写法。第一次接触容易绕晕，遇到时再查、照抄即可——本章先记住一句话：这需求有官方解，别自己造。

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
避坑提醒：别自己发明「页面切换」

{class="mt-1"}
有人图省事，用一个状态变量 if/else 换整屏内容：返回键失灵、状态丢失、切换动画要手写，老式写法的坑一个不少。页面归属导航系统管，界面归属 Composable 管，别越界。
:::

底部标签栏和 NavHost 是标准搭配：NavigationBar 加 NavigationBarItem，选中哪个标签就 navigate 到对应路由，图标亮不亮由当前路由决定。官方示例里有完整写法，照着换图标和路由名，一个多页面的 App 半小时内能跑起来。顺带分清一件事：一页之内切换几个子视图（比如「全部 / 未完成」两个标签），那是同页面的显示切换，用标签页组件配合状态就行，不必动导航，切换范围越小，用越轻的工具。

#### 十一、真实案例：从设计稿到界面的完整翻译

零件齐了，来干一次真的。设想你接了个活：给一家咖啡店做点单页。设计师发来一张图，从上到下是：一张大图、商品名和价格、一段描述、一个数量加减器、最底部一个「加入购物车」按钮。日常开发里占比最大的工作就是这种「翻译」：把视觉语言翻译成组件语言。下面走一遍完整流程。

##### 第一步：把图拆成积木

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">设计稿上的东西</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">对应的 Compose 零件</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">整页从上到下</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Column</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">顶部大图</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">商品名 + 价格（左右分布）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Row + weight</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">描述文字</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数量加减器</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Row（减按钮、数字、加按钮）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">底部大按钮</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button + Spacer 推到底</td></tr>
</tbody>
</table>
```
:::

这个拆解动作说穿了就是找「盒子」：整页是竖盒子，横着的区域是 Row，叠着的角标是 Box。翻译设计稿的难点从来不是 API，是练出这双「看什么都是盒子」的眼睛：拆上五六张图就有了。

##### 第二步：先搭骨架，再填血肉

::: div .code-block
:::inline div .code-head
<span>KOTLIN · OrderScreen.kt</span><span class="dots">···</span>
:::

```
@Composable
fun OrderScreen() {
 var quantity by remember { mutableStateOf(1) }

 Column(Modifier.fillMaxSize()) {
 Image(
 painter = painterResource(R.drawable.latte),
 contentDescription = "燕麦拿铁商品图",
 modifier = Modifier.fillMaxWidth().height(220.dp),
 contentScale = ContentScale.Crop
 )
 Column(Modifier.padding(16.dp)) {
 Row(verticalAlignment = Alignment.CenterVertically) {
 Text("燕麦拿铁", style = MaterialTheme.typography.headlineSmall)
 Spacer(Modifier.weight(1f))
 Text(
 "￥28",
 style = MaterialTheme.typography.titleLarge,
 color = MaterialTheme.colorScheme.primary
 )
 }
 Text(
 "中度烘焙，丝滑燕麦，冰热可选。",
 style = MaterialTheme.typography.bodyMedium,
 modifier = Modifier.padding(top = 8.dp)
 )
 }
 Spacer(Modifier.weight(1f)) // 弹簧：把按钮推到最底
 Button(
 onClick = { /* 加入购物车 */ },
 modifier = Modifier.fillMaxWidth().padding(16.dp)
 ) { Text("加入购物车") }
 }
}
```
:::

几个「翻译痕迹」值得圈出来：图片高度定死、宽度撑满，ContentScale.Crop 让图片裁剪填满不变形——对应设计稿的「大图占顶」；价格用 <code class="inline">Spacer(Modifier.weight(1f))</code> 推到行最右；外层 Column 倒数第二行那个 Spacer 是经典手法，一个谁也不占的弹簧，把按钮压到页面最底。

##### 第三步：数量加减器，状态上场

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 步进器</span><span class="dots">···</span>
:::

```
Row(verticalAlignment = Alignment.CenterVertically) {
 OutlinedButton(onClick = { if (quantity > 1) quantity-- }) { Text("−") }
 Text(" $quantity ", style = MaterialTheme.typography.titleMedium)
 OutlinedButton(onClick = { quantity++ }) { Text("+") }
}
```
:::

quantity 是状态，两个按钮只改状态，数字自动跟着变。注意减按钮里那个 if：数量最少一份，比点了之后在别处报错体面得多，业务规则长在交互里，这是新手和老手都看得见的差别。想让按钮文案显示份数，把 Text 改成 <code class="inline">「加入购物车（$quantity）」</code> 就行，状态驱动的好处顺手就体现了。

##### 第四步：交付前的「三连问」

界面做完别急着交，按第七节的口径自查三件事：切深色模式看看，写死的颜色有没有露馅；把系统字体调大看看——定死的图片高度和小按钮撑不撑得住；转个横屏看看：一整列的东西是不是挤成一团。三连问暴露的问题，十有八九回到主题取色和 Modifier 上改，而不是推翻重来。

回头看，这个页面全部代码不到百行，零件全是前面几节的：组件、布局、Modifier、状态、主题。所谓「会做界面」，不是背下多少 API，是看到任何一张图都能条件反射地拆盒子、认零件、接状态，这件事你刚刚完整走过一遍。

##### 翻译事故对照：为什么你的界面「和设计稿不像」

新手交出来的界面和设计稿对不上，翻来覆去就三种事故：

- <strong>间距全靠默认</strong>：设计稿留白舒服，你的界面挤成一团，多数是没加 padding 和 Spacer。留白不是「高级装饰」，是可读性的一半。
- <strong>图片变形</strong>：忘了 ContentScale.Crop，图片被拉伸得七扭八歪。裁剪填满还是完整显示，是两种不同意图，动笔前选清楚。
- <strong>元素挤压</strong>：该用 weight 的地方没用，文字一长就把时间戳、价格挤出屏幕。看到「挤」，先问一句：剩余空间归谁。

排查方法也简单：把你的界面和设计稿并排放，从外往里逐层对照，间距对不对、尺寸对不对、对齐对不对。三层对下来，九成的「不像」都能定位到具体某一行代码。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
来动手：翻译你自己的设计稿

{class="mt-1"}
打开一个你常用的 App，截一张页面，在纸上拆出盒子（哪里 Column、哪里 Row、哪里 Box），再用 Compose 把它写出来，配上 @Preview 的浅色/深色/大字体三个预览。不用做得一模一样，骨架对就行。
:::

#### 十二、常见问题：十问十答

这些问题都来自真实的初学者，原话风格保留。

- <strong>问：XML 是不是白学了？手里的老项目要重写吗？</strong>答：没白学。市面上仍有大量 App 是 XML 写的，维护它们就得会 XML；两种思路对照着学，你反而更明白声明式好在哪。新项目直接 Compose；老项目官方支持两种共存、按需逐步迁移，不需要推倒重写。
- <strong>问：Modifier 那么多，根本记不住怎么办？</strong>答：不用记。高频的就一小撮：padding、size、fillMaxWidth、background、clip、clickable，写到哪查到哪，两周就长在手上。真正要记住的只有一件事：顺序有意义。
- <strong>问：界面时不时「闪一下」，数字跳来跳去，哪里出问题了？</strong>答：多半是状态没放稳。依次查三处：是不是忘了 remember（每次重组都重置）；该不该换 rememberSaveable（界面重建丢值）；是不是每次重组都新建对象当参数（跳过机制失效）。第八节的三条守则对着过一遍。
- <strong>问：TextField 死活打不进字，键盘都快被我砸了。</strong>答：深呼吸。九成是 onValueChange 没接状态，TextField 显示什么完全由 value 决定，回调断了它就装死。回第二节照正确示范抄一遍，两分钟解决。
- <strong>问：手机一旋转，填了一半的表单全没了。</strong>答：remember 只在界面存活期间有效，旋转会让界面重建。换成 rememberSaveable 就扛得住。存复杂对象才需要自定义 Saver，大多数时候默认机制够用。
- <strong>问：列表一滑就卡，是不是 Compose 本身不行？</strong>答：不是。按概率排查：条目里嵌了同方向滚动、没配 key、条目里重计算没 remember、每次重组新建重对象当参数。第八、九节各管一半。都排除了还卡，再用性能工具深挖，大概率轮不到。
- <strong>问：Kotlin 还不太会，能直接学 Compose 吗？</strong>答：能，但要补几样高频语法：var/val、lambda（大括号当参数）、字符串模板（「$变量」）、when、数据类、by 委托。就这几样，一两天的事。Compose 反而是学 Kotlin 的好陪练，每写一个界面都在反复用这些语法。
- <strong>问：预览里好好的，装到手机上长得不一样？</strong>答：预览是近似，不是真机。深色、真实字体、大字体、横屏、刘海遮挡，只有真机能暴露。第七节的口径再说一遍：预览负责快迭代，真机负责验收，两边都看才交付。
- <strong>问：必须用 Material 3 吗？我想自己画。</strong>答：M3 是默认附赠的一整套视觉规范，不是强制。完全自定义视觉 Compose 也支持，但建议先把 M3 用顺，主题、动态取色、无障碍、控件手感它全包了，自研一套的成本远超想象。等真有了自己的设计体系再谈替换不迟。
- <strong>问：学完这章，下一步做什么练手？</strong>答：做一个「心情日记」：列表页用 LazyColumn 配 key 展示历史心情，点条目用 Navigation 进详情页，详情页能删条目（练状态提升），全程开着深色预览开发。做完它，你对本章的把握就不是「看过」，是「会用」。

#### 十三、误区清单：出发前看一眼

这一章最容易走的岔路都在下面，提前知道能省不少回头路。

- 很多人以为 Compose 是一门新语言，其实它是一套 Kotlin 库，语言还是 Kotlin，@Composable 是标记不是新语法。Kotlin 欠的债到哪都得还，躲不掉也无需躲。
- 很多人以为重组是「整屏重画、代价巨大」，其实重组按函数粒度进行、参数没变的函数直接跳过，日常完全够快；真正的性能杀手是你在重组路径上亲手放的重活。
- 很多人以为 remember 是个全局变量容器，其实它的生命周期跟着界面走：界面销毁它就没了。跨页面共享的数据交给专门容器，别用 remember 硬扛。
- 很多人以为 Modifier 顺序无所谓，其实先 padding 还是先 background，出来的图差一圈白边。记住并善用「调换顺序、预览验证」这个万能排查法。
- 很多人以为状态提升是「代码洁癖」，其实它是解耦手段：无状态组件可预览、可复用、可测试，状态搬家时界面代码一行不用动。
- 很多人以为列表随便用 Column 堆也行：数据少确实行，数据一多就是卡顿现场。会增删的列表，LazyColumn 加 key 是起点，不是「以后的优化项」。
- 很多人以为「深色模式就是把颜色反过来」，其实浅色和深色是两套各有讲究的配色（对比度、层次感都不同），交给主题的两套槽位去做，比手动反色靠谱得多。

#### 十四、给三种背景读者的建议

这一章的读者大概分三类，各有各的旧习惯要「格式化」，也各有各的红利可领。对号入座。

##### 从 XML 老手过来的你

你的最大资产是布局直觉，什么场景用什么容器，一眼就有数；最大包袱是「找控件改控件」的肌肉记忆。两件事要主动换：一是别再想「这个控件在哪」，改想「这个状态对应什么样」；二是 RecyclerView、Adapter、ViewHolder 那一整套，在 Compose 里被 LazyColumn 一个函数取代，适配器模式不是被优化了，是被声明式「吃掉」了。自定义 View 的经验则能平移：你踩过的坑，变成一个个小 Composable，反而更轻。

##### 从 SwiftUI 过来的你

你的红利最大：几乎每个概念都有对应物：State 对 remember 加 mutableStateOf，body 对可组合函数，Modifier 的用法也像（细节有差：Compose 的 Modifier 严格按书写顺序生效）。要警惕的只有一个心理落差：SwiftUI 的 body 看起来「声明一次」，Compose 的函数会被反复执行，副作用管理因此更严格。把「函数会被多次调用」刻进脑子，其他基本是无缝切换。学完 Compose 再看 SwiftUI，你会觉得只是换了方言。

##### 从前端（React/Vue）过来的你

你会觉得 Compose 眼熟得过分：组件是函数、状态驱动渲染、列表要配 key——mutableStateOf 之于 Compose，约等于 useState 之于 React。要适应的地方不多：没有虚拟 DOM，对比更新发生在编译期和运行时的组合系统里，比 JS 生态更依赖编译；样式不是 CSS，是 Modifier 链加主题对象，约束更强也更统一。前端带来的组件化直觉是纯红利，几乎不用格式化。

##### 从低代码、模板站过来的你

如果你用过拖拽式建站或 App 模板工具，来 Compose 反而少一层门槛：属性面板对应参数，拖拽嵌套对应函数嵌套，「选中一个元素改属性」对应「改一行参数」。区别是没了看得见面板，你得靠预览窗看效果——刚开始慢一点，但面板里没有的选项你也能写了，天花板一下高了很多。

三条路殊途同归，因为声明式本来就是同一套思想的三个方言。这一章学完，你手里的不只是安卓界面的入场券——这门「手机课」后面再遇到界面功夫的场景，你已经站在门槛上了。

#### 十五、场景案例：给爸妈做界面，Compose 帮你哪儿忙

全书讲「给爸妈远程帮忙」的地方不少，这一次落到界面上。假设要给妈妈做一个「今天吃什么」抽签页：一个按钮，点了随机出一个菜名。界面简单得不能再简单，但「爸妈用得顺手」这个目标会逼你注意一堆平时忽略的细节：而这些细节恰好是 Compose 的强项。

##### 老人界面的四条军规，对应的 Compose 做法

- <strong>字要大，还要跟着系统走</strong>：别拍脑袋定字号，style 用 typography 的大档位；更重要的是，用户系统里开了特大字体时，界面要跟着放大，用 sp 和主题档位，这事自动成立。预览时加 fontScale 参数提前看效果，别等妈妈来投诉。
- <strong>能点的地方要大</strong>：小细条的 TextButton 在爸妈手指下基本是灾难。用实心 Button，再用 height 或 padding 撑一撑。最小可点尺寸官方规范里有建议，做之前查一下。
- <strong>层级要浅</strong>：一屏一件事，Column 从上往下排，别套娃。爸妈在厨房里单手瞟一眼，两屏还找不到重点，就直接退了。
- <strong>颜色对比要够</strong>：从 colorScheme 取色，别用浅灰写「次要信息」——对老人来说没有「次要信息」，只有「看不见的信息」。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · MealPicker.kt</span><span class="dots">···</span>
:::

```
@Composable
fun MealPicker() {
 var meal by rememberSaveable { mutableStateOf("还没抽") }

 Column(
 modifier = Modifier.fillMaxSize().padding(24.dp),
 horizontalAlignment = Alignment.CenterHorizontally,
 verticalArrangement = Arrangement.Center
 ) {
 Text(meal, style = MaterialTheme.typography.displaySmall)
 Spacer(Modifier.height(32.dp))
 Button(
 onClick = {
 meal = listOf("番茄炒蛋", "青椒肉丝", "清蒸鲈鱼").random()
 },
 modifier = Modifier.height(64.dp)
 ) {
 Text("今天吃什么", style = MaterialTheme.typography.titleLarge)
 }
 }
}
```
:::

就二十来行。字自动跟着主题和系统设置走；深色模式自动成立；读屏软件能把「还没抽」「今天吃什么」念得清清楚楚，因为界面上全是真文本，不是图片。老式写法里这些要么靠小心、要么靠运气，Compose 把它们变成了默认。

有条件的话，把手机上的 TalkBack（屏幕朗读）打开，闭着眼睛用一遍自己的页面：一分钟的实际体验，胜过读十篇无障碍文章。你会立刻发现哪个按钮没描述、哪段提示读不出来。

##### 三件烦心事，各有解法

- <strong>系统字体特大时按钮文字被截断</strong>：别把按钮高度定得太死，让它用默认的自适应高度，或者用 padding 撑，内容变了，容器跟着变。
- <strong>深色模式下图片刺眼</strong>：准备一套偏暗的图片资源，或者在深色模式下降一点透明度；主题管不到的视觉细节，就自己判断当前模式给不同的资源。
- <strong>横屏后内容跑偏</strong>：一竖列的东西横过来确实难看。简单 App 锁定竖屏也是正经选择，算产品决策不算技术妥协，以需求为准。

交给妈妈之前，最后一步是你自己拿手机过一遍：系统字体开到最大、切深色、转横屏，各玩一分钟。这三分钟能替你挡掉半夜「字怎么变小了」的求救电话。给爸妈做界面，功夫不在代码量，在这些「多看一眼」。

#### 十六、加载、空态与出错：界面的另外三种表情

界面不只有「成功态」。数据还在路上、服务器两手一摊、用户断网了，这三种时刻的界面质量，是普通 App 和好用 App 的分水岭。Compose 处理它们的套路不变：把它们也做成状态，界面自动换脸。

##### 加载中：别让用户盯着白屏

数据没到之前，放一个转圈的 CircularProgressIndicator，居中放在原本列表的位置。比白屏强得多：用户知道「在干活」，而不是「卡死了」。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 加载和内容二选一</span><span class="dots">···</span>
:::

```
@Composable
fun FeedScreen(loading: Boolean) {
 if (loading) {
 Box(Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
 CircularProgressIndicator()
 }
 } else {
 LazyColumn {
 items(posts, key = { it.id }) { post ->
 PostRow(post)
 }
 }
 }
}
```
:::

提交按钮也是重灾区：用户手快连点三下，订单下了三单。做法是点击后把按钮置灰（enabled = !loading），按钮里换成小转圈，请求完成再恢复。一个小细节，挡掉一大类「重复扣款」级别的投诉。

##### 空态：空列表别真的空着

列表为空时只剩一个标题，用户会心慌「我是不是弄坏了什么」。给一句人话和一个出口：「还没有记账记录」加一个「记一笔」按钮，把用户引到正确的下一步。文案别写「暂无数据」这种机器腔，写用户听得懂的人话。做法就是前面练过的组合拳：一个 if 判断列表是否为空，空了就显示提前写好的 EmptyState 组件，非空就走正常列表。

##### 出错：把锅说清楚，把出路给出来

请求失败时给用户三样东西：出了什么事（「网络不给力」）、跟他有什么关系（「刚才那笔没提交」）、现在能干什么（「重试」按钮）。全部用状态表达：error 状态一变，界面自动换脸：又是开篇那句「界面是状态的函数」，连出错都是。

进阶的写法是把「加载中 / 成功（带数据）/ 失败（带原因）」收拢成一个整体来管理：三种表情互斥，用类型把它们框住，就永远不会出现「一边转圈一边显示数据」的鬼畜画面。这是后面学架构时的正式课题，这里先混个脸熟。

三种表情做齐，你的 App 就比大部分初学者作品耐用。自测方法简单粗暴：开飞行模式、清掉数据、狂点按钮，三个动作各试一遍，看界面接不接得住。接得住，就可以放心交给别人用了。

#### 十七、组件整理术：把界面代码收拾利索

界面写多了，真正的敌人不是 API，是乱。一个 Screen 函数从五十行涨到五百行，改个按钮要翻半天。这一节给几条整理规矩，都便宜，都立竿见影。

##### 拆分的信号：一个函数超过一屏

一个可组合函数在编辑器里超过一屏，就该拆了。按视觉块拆：顶部栏一个函数、列表区一个函数、底部操作条一个函数。拆完之后 Screen 函数只剩十几行「目录」，想改哪儿跳哪儿。拆出来的零件顺便就能单独预览——一举两得。

##### 文件怎么放：页面一个文件，零件一个抽屉

常见做法是每个页面一个文件（HomeScreen.kt、OrderScreen.kt）；通用零件，你写的 ChatRow、空态页、确认对话框——单独放进一个「组件库」文件，谁要用谁 import。别一个组件建一个文件（文件爆炸），也别把整个 App 塞一个文件（翻页地狱），两个极端都难受。

##### 命名带后缀：看名字就知道身份

社区习惯用后缀标身份：整页叫 XxxScreen，列表行叫 XxxRow 或 XxxItem，卡片叫 XxxCard，对话框叫 XxxDialog。三个月后回看代码，后缀就是路标。这条没有编译器强制，纯靠自觉，但将来一起写代码的人会谢谢你。

##### 参数超过一巴掌，就该收拢

组件参数超过五六个，调用处就开始「糊」，两种收法：相关的参数打包成一个数据类传进去；或者重新审视状态归属，该提升的提升，该下沉的下沉。参数列表是组件的接口，接口清爽，组件才好维护。

##### 注释怎么写：给三个月后的自己

组件头上写两行就够：这是干什么的、适合什么场合用。至于某一行代码「在干嘛」，能不注释就不注释，代码本身已经说清楚了，注释说得比代码还啰嗦反而添乱。检验标准很简单：三个月后的你打开这个文件，能不能十秒内想起它是干嘛的。能，就合格；不能，补注释。

这几条规矩不是哪本权威定的，是无数人把代码写乱之后的总结。你可以先用第一条（超一屏就拆），其余的等代码真的长起来再补：规矩是跟着项目长出来的，不是提前背下来的。

#### 十八、下一步：把 Compose 放进你的工具箱

##### 三个可以马上养成的习惯

每写一个组件就配一个 @Preview（浅色、深色、大字体各来一份）；写列表之前先想 key 用什么；写输入框就检查 onValueChange 接没接状态。三个习惯都不花时间，合起来能挡掉八成返工。

##### 学 API 的正确姿势

本章的零件够撑起大部分页面，遇到没见过的组件别慌：官方文档的组件目录按场景分类，配了能直接跑的示例；Android Studio 里对任何组件按住 Ctrl 点进去，源码里的注释常常就是最好的教程。一切以官方文档为准，教程会过时，文档不会。

##### 和下一块拼图的衔接

界面只负责「显示和收集」，数据从哪来、业务规则放哪，是另一门功课。本章刻意没展开 ViewModel 和数据层，避免一次吞太多；等你要做第二个页面、要真传数据的时候，顺着官方文档的架构指南往前走，路是通的，而且你这一章练的「状态思维」会在那里再次派上用场。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
一句话记牢

{class="mt-1"}
先把界面做对，再做好看，最后才做花，顺序反了，三样都保不住。
:::

#### 十九、排查实录：一次「界面不刷新」的完整排错

理论说了不少，来走一遍真实的排错。凌晨一点，你给设置页加了个「省流模式」开关：开关一开，下面一行说明文字应该从「当前使用流量加载图片」变成「图片仅 Wi-Fi 下加载」。你点了开关，圆点动了，文字没变。别急着怀疑人生，按这个顺序查：

1. 确认状态真的变了：在 onClick 里加一行日志，点一下开关看输出。状态没变，问题在「改状态」那半截——多半是 lambda 里改错了变量。
2. 状态变了、文字没变：检查显示文字的那个函数，读的是不是同一个状态。最常见的乌龙是两个地方各写了一份 remember，你改的是 A，屏幕上显示的是 B，这正是第四节「单一数据源」要防的事。
3. 同一个状态还不刷新：看看文字是不是被「每次重组都新建的对象」当参数包住了，跳过机制失效，第八节的三条守则对着过。
4. 还不行：先 Build & Refresh 一下预览窗，再确认模拟器上跑的是不是最新代码，走到这一步，多半是「看的是新代码、跑的是旧包」这种低级乌龙，谁都有过。

复盘一下：整条排查链没用到任何高深工具，全是本章的概念，状态、单一数据源、重组、跳过、预览刷新。所谓「会调试」，就是把概念在脑子里跑一遍。下次遇到「不刷新」，照这条链走，多数几分钟能定位。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
一句话记牢

{class="mt-1"}
不刷新，先查状态链；链没断，再查重组——顺序别反。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小结

- Compose 思想：界面 = @Composable 函数，积木式嵌套
- 四大组件：Text / Button / TextField / Image
- 布局三件套：Column 竖排、Row 横排、Box 叠放
- Modifier 链式「上妆」：padding、fillMaxWidth、background、clickable，顺序有意义
- 状态是灵魂：remember + mutableStateOf，改数据界面自动重画
- 主题用 Material 3 + 动态取色，深色模式一次配置全局生效
- 依赖交给 Compose BOM；预览要配 ui-tooling；深色、大字体、横屏只有真机能暴露
:::
