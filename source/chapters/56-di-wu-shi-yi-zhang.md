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
界面是用户看到的一切。在 Compose 出现之前，安卓界面用 XML 写——像填空题一样繁琐；2021 年谷歌推出了 <strong>Jetpack Compose</strong>：直接用 Kotlin 代码"画"界面，所见即所得，改一行代码预览立刻刷新。到 2026 年，Compose 已是新项目的绝对主流。这一章，咱们学会"画画"。

#### 一、Compose 的思想：界面就是函数

Compose 的核心思想一句话：<strong>界面 = 函数</strong>。每个能显示在屏幕上的东西（文字、按钮、图片）都是一个"可组合函数"（Composable），用 <code class="inline">@Composable</code> 标记。把它们像积木一样嵌套起来，就是界面。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 第一个 Compose 界面</span><span class="dots">···</span>
:::

```
@Composable
fun Greeting(name: String) {
    Text(text = "你好，$name！")     // 一个"文字积木"
}

// 嵌套组合：大积木套小积木
@Composable
fun HomeScreen() {
    Column {                          // 竖着排列
        Greeting(name = "张三")
        Greeting(name = "李四")
        Button(onClick = { /* 点击做什么 */ }) {
            Text("点我")
        }
    }
}
```
:::

注意 <code class="inline">@Composable</code> 这个"帽子"——它告诉编译器"这是一个界面积木"。积木可以无限嵌套，这就是 Compose 的全部秘密。

#### 二、基础组件：文字、按钮、输入框、图片

Compose 的组件就是"积木块"，最常见的四种：

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

输入框那两行里出现了 <code class="inline">remember { mutableStateOf("") }</code>——这就是 Compose 的"状态"魔法，本章第五节细讲。现在先混个脸熟。

#### 三、布局三件套：Column、Row、Box

组件有了，怎么摆放？记住三个"盒子"：

- <strong>Column</strong>：竖着排（像排队打饭）；
- <strong>Row</strong>：横着排（像并排坐）；
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

想让布局更好看？给组件加 <strong>Modifier</strong>（修饰符）——它就像给积木"上妆"：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Modifier 常用招式</span><span class="dots">···</span>
:::

```
Text(
    text = "好看的文字",
    modifier = Modifier
        .padding(16.dp)          // 四周留白
        .fillMaxWidth()          // 撑满宽度
        .background(Color.Blue)  // 背景色
        .clickable { /* 点击 */ }// 可点击
)
// 链式调用：一个接一个，顺序有意义（先 padding 再背景，背景不含边距）
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>注意：Modifier 的顺序有讲究

{class="mt-1"}
<code class="inline">padding(16.dp).background(Blue)</code> 和 <code class="inline">background(Blue).padding(16.dp)</code> 效果不同——前者是"先留白再涂色"（背景不含边距），后者是"先涂色再留白"（背景包含边距）。新手最容易在这上面画错"奇怪的白边"。不确定时，调换顺序试试，预览立刻告诉你答案。
:::

#### 四、状态：让界面"活"起来

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
        Button(onClick = { count++ }) {   // 改状态
            Text("点我 +1")                // 界面自动刷新
        }
    }
}
```
:::

三行代码，一个活的计数器。这就是 Compose 比老式写法爽的地方：<strong>不用手动"刷新界面"，改数据就行</strong>。记住两个关键函数：<code class="inline">remember</code>（让值在界面重组时不被清空）和 <code class="inline">mutableStateOf</code>（告诉 Compose"这个值变了要重画"）。

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> 用户点击</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> 状态改变（count++）</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> Compose 感知到变化</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> 自动重画界面（重组）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
图 3：Compose 的"状态 → 界面"单向数据流
:::

#### 五、主题与深色模式：一次配置，全局生效

模板项目里的 <code class="inline">MyFirstAppTheme { ... }</code> 就是主题。它基于 <strong>Material 3</strong> 设计规范，帮你把颜色、字体、形状统一管理。支持深色模式只需三步：

1. 在主题里定义好浅色/深色两套配色（模板已自动生成 <code class="inline">ColorScheme</code>）；
2. 系统切到深色模式时，<code class="inline">isSystemInDarkTheme()</code> 自动判断；
3. 用主题提供的颜色（如 <code class="inline">MaterialTheme.colorScheme.primary</code>）而不是写死颜色值。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：Material 3 动态取色

{class="mt-1"}
Android 12 起的"Material You"能让 App 从你的壁纸里提取颜色。Compose 模板默认支持（<code class="inline">dynamicColor</code>）。你的 App 在不同用户手机上会"自动换装"，这就是现代安卓的浪漫。
:::

#### 六、预览、动画与实时编辑：Compose 的"外挂"

Compose 三个开发体验上的"外挂"，用上就回不去：

- <strong>@Preview 预览</strong>：给 Composable 加 <code class="inline">@Preview</code> 注解，Android Studio 右侧立刻渲染出界面——改代码所见即所得，不用每次装到手机上；
- <strong>实时编辑（Live Edit）</strong>：2026 年的 Android Studio 支持在模拟器/真机上"热更新"部分改动，改文字颜色之类的小调整，设备上秒变；
- <strong>动画 API</strong>：<code class="inline">animateFloatAsState</code>、<code class="inline">AnimatedVisibility</code> 几行代码就能让元素平滑过渡——"高级感"往往就差这几十行。

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
<i class="fas fa-lightbulb mr-2"></i>小贴士：先功能后动画

{class="mt-1"}
新手常犯的毛病是"界面还没做对，就开始纠结动画"。先让功能跑通，最后再统一加动效——这也是"简单至上"原则：<strong>动画是锦上添花，功能是雪中送炭</strong>。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：做一个"心情按钮"

{class="mt-1"}
把模板项目改成一个心情切换器：一个按钮，点击后在 😀开心 → 😢难过 → 😡生气 之间循环切换，文字和背景色跟着变。提示：用 <code class="inline">when</code> 根据状态选文案和颜色。做完发给朋友玩，收获第一波"哇你会做 App 了"。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- Compose 思想：界面 = @Composable 函数，积木式嵌套
- 四大组件：Text / Button / TextField / Image
- 布局三件套：Column 竖排、Row 横排、Box 叠放
- Modifier 链式"上妆"：padding、fillMaxWidth、background、clickable——顺序有意义
- 状态是灵魂：remember + mutableStateOf，改数据界面自动重画
- 主题用 Material 3 + 动态取色，深色模式一次配置全局生效
:::
