---
id: di-wu-shi-zhang
num: 50
part: an-zhuo-kai-fa-pian
nav: 第五十章：Kotlin快速上手——安卓开发的第一语言
toc: default
kind: chapter
---

### 第五十章：Kotlin 快速上手——安卓开发的第一语言

{class="chapter-intro mb-4"}
这一章咱们正式学语言。别紧张——Kotlin 是出了名的"对新手友好"，而且你不需要背语法书：先掌握 20% 的语法，就能看懂和写出 80% 的日常代码。剩下的边做项目边查。记住咱们的学习原则：<strong>看懂 > 记住，会用 > 精通</strong>。

#### 怎么用这一章：三个建议

开讲之前，先说清楚这一章的打开方式，不然再好的教材也会被读成催眠材料。

- <strong>边读边敲，不要只看</strong>。代码是"肌肉记忆型"知识，看十遍不如敲一遍。每一节的代码块都建议你在 Kotlin Playground（play.kotlinlang.org，浏览器直接打开的官方在线练习场）里亲手跑一遍——不用装任何软件，上一章的电脑条件再差也不影响。
- <strong>改坏不要慌</strong>。在线演练场没有"项目"概念，改坏了刷新页面就归零，零成本。新手阶段最宝贵的就是这种"随便折腾"的自由。
- <strong>别追求一次记住</strong>。这一章的知识点后面章节会反复出现，今天记不住的东西，第 54 章做记账本时会再遇到一次，那时自然就熟了。语言学习是螺旋形的，不是直线形的。

另外一个心理建设：这一章的示例为了能独立运行，都比较"小"——打印一句话、算一笔账。别嫌弃它们小，真实 App 里的每一块业务逻辑，都是由这些小零件拼出来的。你今天学会的 <code class="inline">filter</code>，就是未来记账本 App 里"筛选本月大额支出"的全部秘密。

#### 一、变量与类型：给数据起名字

程序就是"数据 + 逻辑"。变量，就是给数据起个名字存起来。Kotlin 有两种声明方式：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 变量</span><span class="dots">···</span>
:::

```
val name = "张三"        // val：只读变量（推荐默认用这个）
var age = 18             // var：可变变量（以后还能改）

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var 可以改
// name = "李四"         // <i class="fas fa-times-circle mr-1"></i> val 不能改，编译会报错

val score: Int = 100     // 也可以显式写明类型
val pi = 3.14            // 不写也能自动推断
```
:::

常用类型就几种，一张表记住：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">类型</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">存什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">示例</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">整数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">小数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">文字</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"你好"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Boolean</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真/假</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List&lt; T&gt;</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一组数据</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">listOf(1, 2, 3)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kotlin 常用基础类型

"类型推断"值得单独说一句，因为它是 Kotlin 读起来清爽的第一功臣。<code class="inline">val pi = 3.14</code> 里你没写类型，编译器看一眼右边就知道 pi 是小数（Double）；<code class="inline">val name = "张三"</code> 同理推断出 String。类型还在那里，只是不用你亲手写。什么时候必须写？两种情况：变量声明时不赋值（<code class="inline">val result: Int</code>，回头再算）；以及"我想让它不是默认类型"（比如你想要单精度浮点就写 <code class="inline">val f: Float = 3.14f</code>）。

数字类型之间不能隐式混用，这点和很多语言不同。Int 想当 Double 用，要显式转换：<code class="inline">val d: Double = age.toDouble()</code>。乍看很啰嗦，实际上是保护——记账 App 里"元"和"分"混算出的 bug，十条有八条栽在自动类型转换上。Kotlin 让你在转换的那一刻亲自动手，正是让你"知道自己正在换算"。

运算符就五个主力：<code class="inline">+ - * / %</code>。前三个不解释，除号和百分号各有一个坑要提前拆。<strong>除号坑：整数除整数还是整数</strong>——<code class="inline">5 / 2</code> 得到 2 不是 2.5！因为两边都是 Int，Kotlin 做的是"整除"，小数部分直接扔掉。想要 2.5，至少一边是 Double：<code class="inline">5.0 / 2</code> 或 <code class="inline">5.toDouble() / 2</code>。记账、算平均分这类场景，这个坑能让你调试一小时还找不到原因，现在记住它，等于省了一小时。<strong>百分号（取余）</strong>：拿除完剩下的零头，<code class="inline">7 % 3</code> 得 1。最经典的用法是"奇偶判断"——<code class="inline">if (number % 2 == 0)</code> 就是偶数。另外简写运算符 <code class="inline">+=、-=、*=</code> 都通用：<code class="inline">count += 1</code> 等于 <code class="inline">count = count + 1</code>，计数器专用。

val 和 var 的取舍，光看定义容易轻敌。给你一个真实场景：记账本里有一笔金额 <code class="inline">var amount = 12.5</code>。三个月后你翻回这段代码，要花十分钟想"这金额中途被谁改过"——每一处赋值都得查。如果当时用的是 val，金额从创建起就是 12.5，一眼定案。数据能不变就不变，逻辑才好推理，这是"val 优先"背后的全部思想。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：val 优先原则

{class="mt-1"}
Kotlin 社区的铁律：<strong>默认用 val，确有必要再用 var</strong>。能用 val 的地方用 var，IDE 会黄字警告你。这个习惯能帮你少掉一大类"变量被意外修改"的 bug——代码越少变化，越容易推理。
:::

#### 字符串模板再进一步：不只是 $变量

字符串是日常代码里出现频率最高的类型，Kotlin 给它的三个便利值得单独一节。

<strong>第一，模板里可以放表达式</strong>。写 <code class="inline">$变量名</code> 只能插入变量本身；要插入计算结果，用花括号包起来：<code class="inline">"总价：${price * count} 元"</code>。新手常犯的错是写 <code class="inline">"总价：$price * count"</code>——结果只插了 price，后面乘法原样当文字输出。记住口诀：<strong>纯变量用 $，表达式用 ${ }</strong>。

<strong>第二，字符串自带一堆现成方法</strong>。常用的有：<code class="inline">length</code>（长度）、<code class="inline">uppercase()</code>/<code class="inline">lowercase()</code>（大小写）、<code class="inline">trim()</code>（去首尾空格）、<code class="inline">contains("关键词")</code>（是否包含）、<code class="inline">split(",")</code>（按分隔符拆成列表）、<code class="inline">isEmpty()</code>（是否为空）。它们不用背，Playground 里敲一遍 <code class="inline">"hello".u</code>，补全列表自己会跳出来。

<strong>第三，三引号原样字符串</strong>。写多行文字（比如一段说明、一段 JSON 示例）时，用三个引号包住，换行、缩进、引号都不用转义：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 原样字符串</span><span class="dots">···</span>
:::

```
val receipt = """
    记账小票
    ----------
    午餐：12.5 元
    交通：5.0 元
""".trimIndent()

println(receipt)
```
:::

末尾的 <code class="inline">trimIndent()</code> 把缩进的空白去掉，输出才是干净的小票。这个写法在后面做项目时还会反复出现——第 55 章"预习"网络返回的 JSON 时你会再见到它。

顺带一个"显示格式"的小技巧：金额想显示成 54.10 而不是 54.1（小数点后补零），用格式化模板：<code class="inline">"%.2f".format(share)</code> 得到 "54.10"。%.2f 的意思是"按小数点后两位格式化一个浮点数"。显示层的格式化和数据层的计算要分开——数据存 Double，显示时才格式化，这个分层习惯现在建立，第 54 章记账本里直接受益。

#### 集合初见：List 是装一串数据的盒子

基础类型表里那个 <code class="inline">List&lt;T&gt;</code> 单拎出来讲，因为它是"从单数到复数"的跨越——学会了它，一个变量就能装下整个通讯录。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · List 入门</span><span class="dots">···</span>
:::

```
val fruits = listOf("苹果", "香蕉", "橙子")   // 创建一个列表

println(fruits.size)        // 3（元素个数）
println(fruits[0])          // 苹果（下标从 0 开始！）
println(fruits.last())      // 橙子
println(fruits.contains("香蕉"))   // true

val scores = listOf(85, 92, 78)
println(scores.sum())       // 255（求和，第 54 章的记账本要用）
```
:::

三个新手必须刻进脑子的事实。<strong>第一，下标从 0 开始</strong>：第一个元素是 <code class="inline">fruits[0]</code> 不是 <code class="inline">fruits[1]</code>——全世界程序员都被这个惯例绊过一脚，绊一次就记住了。<strong>第二，listOf 创建的是只读列表</strong>：往 fruits 里"添加"元素会编译报错。想要能增删的列表，用 <code class="inline">mutableListOf(...)</code>，配合 <code class="inline">add()</code>、<code class="inline">remove()</code> 使用。看出规律没有？可读写的版本在名字里就写了 "mutable"——Kotlin 把"会不会变"又写进了名字里，跟 val/var 一脉相承。<strong>第三，列表里的元素类型必须一致</strong>：<code class="inline">listOf(1, 2, 3)</code> 是 Int 列表，往里塞字符串会被编译器拦下。泛型 T 的意思就是"这个盒子里装的都是 T 这种类型"。

除了 List，还有两个近亲混个脸熟：<strong>Set</strong>（<code class="inline">setOf(...)</code>）不允许重复元素，适合装"去重后的标签"；<strong>Map</strong>（<code class="inline">mapOf("姓名" to "张三", "城市" to "杭州")</code>）是键值对，适合装"一个东西的多个属性"。本节先把 List 玩熟，Set 和 Map 遇到时再补——它们在本书项目里出场的机会比 List 少。

List 的几个查询动作顺手记齐：<code class="inline">fruits.indexOf("香蕉")</code> 找位置（找不到返回 -1），<code class="inline">"香蕉" in fruits</code> 判断在不在（返回 Boolean，比 contains 更顺口的写法），<code class="inline">fruits.first()</code> 和 <code class="inline">fruits.last()</code> 拿头尾，<code class="inline">fruits.isEmpty()</code> 问是否为空。这些方法在 List 上几乎都有对应版本，记住"东西都在列表的方法里"这个感觉，具体名字用时查补全列表就行——代码补全会教你一切。

#### 与 Swift 对照：变量与类型

如果你学过一点 Swift（或者打算之后翻第 59 章往 iOS 走），这两门语言在变量这件事上像得让人安心，差异点也值得现在就记住：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">这件事</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kotlin</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Swift</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">只读变量</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">val name = "张三"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">let name = "张三"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可变变量</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">var age = 18</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">var age = 18</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">显式类型</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">val s: String = "hi"（冒号在前）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">let s: String = "hi"（一样）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">字符串插值</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"你好，\(name 的 Kotlin 写法是 $name)"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"你好，\(name)"（统一用反斜杠括号）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kotlin 与 Swift 的变量声明对照

一图流总结：val ≈ let，var ≈ var，类型推断两边都是标配，插值语法的"手感"几乎一致（Swift 全用 <code class="inline">\(表达式)</code>，Kotlin 简写 <code class="inline">$变量</code>、全写 <code class="inline">${表达式}</code>）。两门语言都是 2010 年代才诞生的"现代语法"，互相借鉴了很多。学会了 Kotlin，以后看 Swift 代码不会是天书——反过来也一样。这个对照表的路数，本章每一节都会走一遍，帮你把"学一门语言"的价值放大成"看懂两门语言"。

#### 二、函数：把逻辑打包成"按钮"

函数是一段有名字的逻辑，像遥控器上的按钮——按一下（调用），就执行一串动作。Kotlin 里用 <code class="inline">fun</code> 声明：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 函数</span><span class="dots">···</span>
:::

```
fun greet(name: String): String {
    return "你好，$name！"     // $ 符号把变量插进字符串
}

println(greet("张三"))        // 输出：你好，张三！

// 单行函数可以简写成表达式
fun add(a: Int, b: Int) = a + b

println(add(3, 5))            // 输出：8
```
:::

几个要点：参数写在括号里（名字在前、类型在后，用冒号隔开）；返回类型写在括号后；<strong>字符串模板</strong> <code class="inline">$变量名</code> 是 Kotlin 的招牌便利——不用再像 Java 那样"字符串 + 变量"地拼来拼去。

"返回类型写在哪"这个记忆点容易忘，给你一个顺口的读法：<strong>从左往右读一遍，就是函数的说明书</strong>——"fun greet，输入 name（String），输出 String"。把签名当句子读，看陌生代码时特别管用：先读函数签名，猜它干什么，再看函数体验证，这个顺序和"先看封面再看正文"一样自然。

表达式函数体（单行简写）值得多说两句：函数体只有一行时，花括号和 return 都能省，等号右边就是返回值。省掉的还有返回类型声明——编译器能从 <code class="inline">a + b</code> 推断出返回 Int，跟 val 的类型推断一个道理。什么时候不省？逻辑超过一行、或者你想让"返回什么"写明在纸面上（第八节会讲这是好习惯），就老老实实用花括号。

来写一个"真事"函数，感受一下函数怎么把现实问题装进去。场景：周五聚餐，四个人 AA，总消费 216.4 元，各付多少？写成人话是"总价除以人数"，写成函数：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 第一个真事函数</span><span class="dots">···</span>
:::

```
fun splitBill(total: Double, people: Int): Double {
    return total / people
}

val share = splitBill(216.4, 4)
println("每人应付：$share 元")   // 每人应付：54.1 元
```
:::

这个函数小到不值一提，但注意它做对了三件事：参数有名字（看调用就知道传什么）、返回类型明确（Double，钱要用小数）、逻辑只有一行（没有多余动作）。真实项目里的函数就是这样的放大版——名字说清楚自己干嘛，参数说明白需要什么，函数体只做一件事。以后你写一百行的函数时，随时问自己一句："它还能不能拆成几个 splitBill 这样的零件？"拆到不能再拆，你的代码就比九成新手干净了。

还有一个特殊的返回类型会遇到：<strong>Unit</strong>。函数不返回任何东西时，返回类型是 Unit（可以不写，编译器自动补）。它就像 Swift 里的 Void——"我干完活就走，不带回东西"。打印日志、更新界面这类函数十有八九返回 Unit。

#### 参数的进阶玩法：默认值、具名参数与变长参数

函数的参数系统比入门示例丰富，三个进阶特性真实项目天天用：

- <strong>默认参数</strong>：给参数一个默认值，调用时不传就用默认。<code class="inline">fun greet(name: String, greeting: String = "你好")</code>——调用 <code class="inline">greet("张三")</code> 得到"你好，张三！"，调用 <code class="inline">greet("张三", "早上好")</code> 得到"早上好，张三！"。同一种问候逻辑不用写两个函数。
- <strong>具名参数</strong>：调用时指名道姓，可读性暴涨。<code class="inline">greet("张三", greeting = "晚安")</code> 一眼看清"晚安"是传给谁的。参数多的时候（比如画一个按钮要十来个参数），具名调用几乎是你唯一看得懂的写法。Compose 里你会天天见它。
- <strong>变长参数</strong>：参数个数不定时用 <code class="inline">vararg</code>。<code class="inline">fun sumAll(vararg nums: Int): Int</code>——<code class="inline">sumAll(1)</code>、<code class="inline">sumAll(1, 2, 3)</code> 都合法。用得少，见到别慌。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 默认参数与具名参数</span><span class="dots">···</span>
:::

```
fun orderTea(type: String, sugar: Int = 0, ice: Boolean = false): String {
    val desc = if (ice) "加冰" else "去冰"
    return "一杯$type，糖 $snow 份，$desc"
}
```
:::

上面这段代码里藏了一个故意写错的地方——你找到了吗？<code class="inline">$snow</code> 应该是 <code class="inline">$sugar</code>。编译器会立刻报错：找不到叫 snow 的变量。这个错误的好处是<strong>报在编译期</strong>：程序根本没跑起来就拦住了你，而不是跑到一半蹦出奇怪的结果。Kotlin 大量的设计都是这个思路：能编译期发现的问题，绝不留到运行期。把运行代码前被拦住当成常态，你会越来越喜欢这种"严厉"。

#### 与 Swift 对照：函数

函数语法的对照比变量多一点差异，逐条看：

- <strong>声明词</strong>：Kotlin 用 <code class="inline">fun</code>，Swift 用 <code class="inline">func</code>——一字母之差，别混就行。
- <strong>返回箭头方向</strong>：Kotlin 是 <code class="inline">fun f(): String</code>（冒号），Swift 是 <code class="inline">func f() -> String</code>（箭头）。这是两边最显眼的语法分歧，初学时最容易写串。
- <strong>默认参数</strong>：两边都支持，写法几乎一样，都是"参数名: 类型 = 默认值"。但 Swift 的调用习惯强制写参数名（外部标签），Kotlin 只在你想写时才写具名——Kotlin 更宽松，Swift 更"自述"。
- <strong>无返回值</strong>：Kotlin 的 Unit ≈ Swift 的 Void，概念完全对得上。

一句话总结：函数这节两边"神似形不似"，差异集中在符号（冒号 vs 箭头）。如果你两边都在学，建议现在就做一张自己的对照表——亲手抄一遍的语法，比看十遍都记得牢。

#### 三、条件与循环：让程序会"思考"

程序的智能来自两件事：<strong>会判断</strong>（if/when）和<strong>会重复</strong>（for/while）。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 条件与循环</span><span class="dots">···</span>
:::

```
// 判断：if / else
val age = 17
if (age >= 18) {
    println("成年人")
} else {
    println("未成年")
}

// 多分支：when（比 switch 好用一百倍）
val score = 85
val level = when {
    score >= 90 -> "优秀"
    score >= 60 -> "及格"
    else -> "再接再厉"
}

// 重复：for 循环
val fruits = listOf("苹果", "香蕉", "橙子")
for (fruit in fruits) {
    println("我爱吃$fruit")
}
```
:::

<code class="inline">when</code> 是 Kotlin 里最常用的多分支写法，安卓开发里你会天天用到它（比如根据状态显示不同界面）。

示例里的 when 有个容易被一眼扫过的好细节：<strong>它被当作表达式用了</strong>——多分支的结果直接赋给了 level 变量。if 也有同样的能力：<code class="inline">val desc = if (score >= 60) "及格" else "不及格"</code>。Kotlin 的 if 和 when 都"有返回值"，这让判断逻辑可以像数据一样流动，省掉先声明变量再赋值的繁琐。用惯了之后，你会发现自己的代码里"中间变量"越来越少。

for 循环还有个"带下标"的兄弟。需要序号时（"第 1 名：苹果"），用 <code class="inline">for ((index, fruit) in fruits.withIndex())</code>，一次拿到序号和元素。这个写法初次看很怪——括号里塞了两个变量——它其实是"解构"语法，第六节数据类部分会再遇到它，到时候你会恍然大悟。

#### when 的完整形态：带主语、带类型判断

入门示例里的 when 是"无主语"形态（每个分支自己写完整条件）。它还有两种常用形态，配齐之后你就能处理绝大多数分支场景：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · when 的两种常用形态</span><span class="dots">···</span>
:::

```
// 形态一：带主语（对同一个值反复判断）
val weather = "雨"
when (weather) {
    "晴" -> println("适合出门")
    "雨" -> println("记得带伞")
    "雪" -> println("注意保暖")
    else -> println("查查天气 App")
}

// 形态二：区间匹配（不用一个个列举）
val temp = 26
when (temp) {
    in 35..100 -> println("高温预警")
    in 24..34  -> println("舒适")
    in 10..23  -> println("微凉")
    else -> println("要穿外套了")
}
```
:::

带主语的 when 读起来像中文的"看天气说话"：是晴就怎样，是雨就怎样。区间匹配用 <code class="inline">in 起点..终点</code>，特别适合"温度、分数、金额"这类连续数值。两种形态都能当表达式赋值给变量，跟入门示例一样。

when 还有一个大杀器——<strong>类型判断</strong>：<code class="inline">when (obj) { is String -> ...; is Int -> ... }</code>，用 <code class="inline">is</code> 检查"它是不是某种类型"，而且匹配成功的分支里，编译器自动把它当成那个类型来用（智能转换）。这个能力现在看着平淡，等第五节学了密封类，它会成为你处理"界面状态"的主力武器——先埋个伏笔。

再给你一个"真事"分支场景练手感：会员折扣。同一个函数对不同等级的会员收不同折扣——<code class="inline">when (vipLevel) { 3 -> total * 0.8; 2 -> total * 0.9; else -> total }</code>。注意这里 when 用了主语形态加表达式返回，两招合流。以后你在 App 里看到的"不同身份不同显示"，底层几乎都是这类分支在转。判断逻辑不难，难的是把现实规则完整地翻译成分支——漏一种情况就是 bug。写 when 时的自检口诀：把 else 想成"兜底网"，问问自己"网住的都是什么？有没有漏网的？"

#### 区间与循环控制：..、until、downTo、step

"循环 10 次"、"倒着数"、"隔一个取一个"这些常见需求，Kotlin 全部用区间语法解决：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 区间四件套</span><span class="dots">···</span>
:::

```
for (i in 1..5)        println(i)   // 1 2 3 4 5（含 5）
for (i in 1 until 5)   println(i)   // 1 2 3 4（不含 5）
for (i in 5 downTo 1)  println(i)   // 5 4 3 2 1（倒数）
for (i in 1..10 step 2) println(i)  // 1 3 5 7 9（隔一个）
```
:::

四个写法的区别就在"端点"和"步子"上：<code class="inline">..</code> 两端都含；<code class="inline">until</code> 含头不含尾——配合"列表长度"用最顺手（列表下标从 0 到 长度-1，<code class="inline">0 until list.size</code> 正好不越界）；<code class="inline">downTo</code> 倒数；<code class="inline">step</code> 调步幅。这四个组合词不是函数调用，是 Kotlin 语法的一部分，写的次数多了肌肉记忆就来了。

循环控制词只有两个，借用很多语言的传统：<strong>break</strong>（跳出整个循环）和 <strong>continue</strong>（跳过本轮、进下一轮）。找东西找到就停用 break，过滤掉不合适的用 continue。while 循环（"满足条件就一直做"）在安卓业务代码里出现频率不高，认识即可：<code class="inline">while (条件) { ... }</code>。

最后提醒一个现代 Kotlin 的事实：<strong>很多"循环"其实可以不用循环写</strong>。想给每个水果打印一行？<code class="inline">fruits.forEach { println(it) }</code>。想挑出所有带"果"字的？<code class="inline">fruits.filter { it.contains("果") }</code>。这些"集合连招"是第六节的主角，for 循环帮你建立直觉，连招帮你写出更简洁的正式代码——两者都要会，先会 for，再拥抱连招。

#### 四、空安全：Kotlin 的"保命符"

Java 时代最著名的 bug 叫 <strong>NullPointerException（空指针异常）</strong>——程序访问了一个"什么都没有"的东西，直接崩溃。据统计它是安卓崩溃排行榜的常年第一。Kotlin 从语言层面解决了它：<strong>默认不允许空值</strong>。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 空安全</span><span class="dots">···</span>
:::

```
var name: String = "张三"   // 普通类型：绝不允许是 null
// name = null                // <i class="fas fa-times-circle mr-1"></i> 编译错误，直接把你拦住

var nickname: String? = null // 加个问号：允许为 null
nickname = "三儿"

// 使用可空类型时，必须安全地处理：
println(nickname?.length)    // 安全调用：null 就返回 null，不崩
val len = nickname?.length ?: 0   // Elvis 操作符：null 时给默认值
println(len)
```
:::

把空安全的思路翻译成人话：<strong>Kotlin 把"这里可能什么都没有"写进了类型本身。</strong>类型后面不带问号，编译器向你担保"这个变量永远有值"；带了问号，编译器的态度变成"它可能没值，所以你必须逐次处理"。崩溃从"运行时的惊喜"变成了"编译时的选择题"——你被迫在写代码时就回答"没值怎么办"，答案无非三种：给默认值（?:）、跳过不处理（?.）、或者斩钉截铁地说"绝不可能为空"（!!，后面讲它的危险）。

为什么这个设计在安卓里格外值钱？因为安卓代码里"空"无处不在：刚打开的页面，用户还没输入昵称——空；网络没回来，数据还没到手——空；通讯录里查一个不存在的联系人——空。老代码里这三种情况各写各的"防崩补丁"，写漏一处就是线上崩溃。Kotlin 的问号把这些"可能为空"标在了明面上，编译器成了你雇的、不睡觉的检查员。

可空类型的"必须处理"有多严格？严格到 <code class="inline">nickname.length</code> 这种直接调用都会编译报错——哪怕你上一行刚赋了值。编译器的逻辑是：可空类型的值，每个使用点都要检查。接下来的一节讲"检查"的完整工具箱。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>注意：? 和 ?: 别搞混

{class="mt-1"}
<code class="inline">String?</code> 是"允许为空"，<code class="inline">a ?: b</code> 是"a 为空时用 b"（长得像猫王发型，所以叫 Elvis 操作符）。刚开始写代码时，看到编译器报"null 相关错误"，八成是你忘了处理可空类型——这正是语言在保护你。
:::

#### 空安全工具箱补全：let、!! 与智能检查

? 和 ?: 之外，工具箱里还有三件，配齐它们你就能从容应对一切可空场景：

- <strong>?.let { }</strong>："如果不为空，就做点什么"。值不为空时，花括号里通过 <code class="inline">it</code> 拿到这个值；为空则整段跳过。<code class="inline">nickname?.let { println("昵称是 $it") }</code>——比 if 判空少写一层嵌套，还能顺便拿到非空的值用。它是 ?: 的"做动作版"：Elvis 给默认值，let 执行动作。
- <strong>!!（双感叹号）</strong>："我担保它不为空，为空就崩给我看"。这是编译器的"闭嘴按钮"。真实代码里 !! 应该像烟头一样罕见——看到它就要问自己：为什么这里"不可能为空"？有没有更安全的写法？新手阶段甚至可以立个规矩：一个月内不许用 !!。
- <strong>if 检查后的智能转换</strong>：<code class="inline">if (nickname != null) { println(nickname.length) }</code>——在确认过非空的代码块里，编译器自动把 nickname 当非空类型用，不用再写问号。这个"智能转换"让 if 判空也不显得笨重。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · let 与智能转换</span><span class="dots">···</span>
:::

```
var nickname: String? = "三儿"

// let：不为空才打印
nickname?.let { println("昵称是 $it，长度 ${it.length}") }

// 智能转换：检查过就放行
if (nickname != null) {
    println(nickname.length)   // 这里不用写 ?.，编译器知道它非空
}
```
:::

这一节的四个工具（?、?:、?.let、!!）覆盖了日常空处理的 95% 场景。选哪个的直觉可以这么建：<strong>要有值就用 ?:，要做动作就用 ?.let，要自证清白就用 if 检查，!! 永远是最后手段。</strong>第 55 章处理"网络数据可能拿不到"时，这套工具会成建制地登场。

拿一个生活场景把它们串起来。你在写一个"查快递"的小功能：快递单号可能还没填（用户没输入）、可能查不到（单号错了）。用 Kotlin 表达这个现实：<code class="inline">var trackingNumber: String? = null</code>——类型后面那个问号，诚实记录了"单号可能不存在"这个事实。展示到界面时：<code class="inline">val display = trackingNumber ?: "暂无单号"</code>；要发起查询时：<code class="inline">trackingNumber?.let { queryExpress(it) }</code>——没单号就安静地什么都不做，绝不崩溃。你看，空安全不是炫技语法，它是"把现实里的'不一定'翻译成代码"的方式。现实里充满不一定，所以这门语言把"不一定"做到了一等公民。

#### 与 Swift 对照：可选项的同与不同

空安全是 Kotlin 和 Swift 最深的一处共鸣——两门语言几乎同时代诞生，都被 Java 和 Objective-C 时代的空指针崩溃折磨过，于是都选择了"把可空性写进类型"。对照着看：

- <strong>概念完全对应</strong>：Kotlin 的 <code class="inline">String?</code> ≈ Swift 的 <code class="inline">Optional&lt;String&gt;</code>（写作 <code class="inline">String?</code>）。"类型后加问号表示可为空"是同一套设计。
- <strong>Elvis vs 空合并</strong>：<code class="inline">a ?: b</code> 在 Swift 里写作 <code class="inline">a ?? b</code>，功能一字不差——为空给默认。名字不同（Elvis 操作符 vs nil 合并操作符），手感相同。
- <strong>?.let vs if let / guard let</strong>：Swift 判空做动作的经典写法是 <code class="inline">if let n = nickname { ... }</code> 或提前退出的 <code class="inline">guard let</code>；Kotlin 用 <code class="inline">nickname?.let { ... }</code>。形式不同，思想一致：先确认有值，再用这个值。
- <strong>强制解包</strong>：Kotlin 的 <code class="inline">!!</code> ≈ Swift 的 <code class="inline">!</code>。两边都主张少用，两边的新手都爱用——这门"共性"你最好别学。
- <strong>一点差异</strong>：Swift 的可选项是"包装盒"概念（值被 Optional 包着，解包后才能用），教学时常用比喻；Kotlin 的可空类型是编译器的静态检查，没有"盒子"的运行时开销。初学阶段这个差异可以忽略，先会用问号。

把空安全这三节学完，你其实已经同时学会了 Swift 的可选项——这不是夸张，是两门语言设计者有意的殊途同归。后面 data class 和协程的对照还会让你再惊两次：这两门语言的"现代武器库"，重合度高得惊人。

#### 误区清单：语法学习阶段的五个想当然

这一节把新手在语言学习期的五个典型想当然摆出来逐个纠正，看看你有没有中招：

- <strong>误区一：以为学语言就是背语法。</strong>其实语法是"查表"知识，逻辑是"肌肉"知识。你不需要记住 String 有哪些方法——你需要在脑子里装下"字符串有处理方法可查、数字类型转换要显式、空值必须处理"这些骨架，肌肉部分靠 Playground 练出来。
- <strong>误区二：以为要把所有类型学全才能开工。</strong>Int、Double、String、Boolean 加 List，五样够写完本书所有项目。Float、Long、Char、Set、Map 这些是"遇到再学"的库存，提前囤只会占内存（你的，不是电脑的）。
- <strong>误区三：以为 == 在比较"内容"这个事可以不问。</strong>好消息：Kotlin 的 <code class="inline">==</code> 就是比较内容（相当于 Java 的 equals），字符串 <code class="inline">"abc" == 输入</code> 直接比内容，新手不用再学一套"引用相等"。要比较"是不是同一个对象"时才用 <code class="inline">===</code>——日常几乎用不到，知道存在即可。
- <strong>误区四：以为代码越长越厉害。</strong>同一件事，五行代码解决比五十行解决高级得多。Kotlin 的设计哲学就是"把常见模式变成一句话"（第六节的集合连招是巅峰体现），写得短是这门语言给你的奖励，不是偷懒。
- <strong>误区五：以为报错是惩罚。</strong>编译器拦下的错误是"免费的失败"——它发生在你自己的电脑上、程序还没发布、改一行就好。真正的惩罚是错误跑到用户手机上才爆。把每次红色报错当成编译器给你的免费陪练。

#### FAQ：语言学习阶段的七个真问题

收集了学语法阶段问得最多的七个问题，答案从短：

- <strong>问：我英语很烂，能学编程吗？</strong>答：能。日常要认识的英文单词就几十个（fun、val、return、if……），翻来覆去就这些。报错信息是英文，但本书教过方法论——抓第一行、搜关键词，或者扔给 AI 翻译。语言障碍在 2026 年是 AI 时代前的问题。
- <strong>问：要先学 Java 吗？网上说"安卓祖师爷是 Java"。</strong>答：不需要。Kotlin 是官方钦定的第一语言，本书全部项目用它。老代码里的 Java 成分，你按对照读就行——真需要补的时候，第 48 章的语言史铺垫已经让你知道该查什么。
- <strong>问：Playground 和 Android Studio，先练哪个？</strong>答：先 Playground。它零安装、零配置、秒出结果，适合纯语法练习；等你的代码开始"要用到界面和手机功能"，自然迁回 Android Studio（第 51 章）。两个场景分工明确，不冲突。
- <strong>问：多久能"学会"？</strong>答：看"学会"的定义。看懂别人的代码，两周；能改、能拼装，一个月；能独立设计，几个月到一年不等，取决于你写了多少。唯一确定的是：进度和敲代码的次数成正比，和看视频的集数无关。
- <strong>问：AI 都能写代码了，我为什么还要学语法？</strong>答：因为<strong>指挥的人必须看得懂结果</strong>。第七篇讲过：AI 是天才实习生，你是验收人。验收不懂语法的代码，就像不懂菜谱的美食评委——AI 报"这个函数会崩"你听不懂为什么，它写错时你发现不了。语法是你的"验收资格证"，这一章教的就是它。
- <strong>问：记不住怎么办？学完就忘。</strong>答：正常，所有人的语法记忆都是"用了才长住"。本书的应对是结构化复习：语法速查卡（第七节）收藏起来随用随查，各章项目里同一批语法反复出现——第 54 章你至少会再写五次 data class，到那时"忘记"反而难。
- <strong>问：要不要买语法书或买课？</strong>答：先把本书项目做完再说。教程的边际价值递减得很快，动手项目的价值不会。真要补，官方文档（Kotlin 官网的中文文档）和 Kotlin Playground 自带的教程（Interactive tutorial）都是免费且权威的。
- <strong>问：Kotlin 只能写安卓吗？学了会不会白学？</strong>答：不会白学。服务端、跨平台应用（Kotlin Multiplatform）、桌面程序都是它的主场，语法学到手去哪儿都能用。而 val、函数、空安全这些概念，更是通用于所有现代语言——这门"课"的学费，在任何一门语言上都认账。

#### 练习五连：今天就能做完的小题

把前四节的知识点焊成肌肉记忆，五道小题足够。全部在 Playground 里完成，每题都先自己写、写不出来再看提示：

1. <strong>自我介绍函数</strong>：写一个函数 <code class="inline">fun intro(name: String, age: Int): String</code>，用字符串模板返回"我叫 XX，今年 XX 岁"。调用三次，改三个不同的人。提示：模板里 Int 可以直接插值。
2. <strong>AA 分摊改良版</strong>：给 splitBill 加一个默认参数 <code class="inline">tipRate: Double = 0.0</code>（小费比例），算出含小费的每人金额。用具名参数调用一次、不具名调用一次，观察读感差别。
3. <strong>成绩报告机</strong>：用 when 当表达式，输入一个分数（0-100），返回"优秀/良好/及格/不及格"四档。故意传一个 105，想想边界该怎么处理（提示：when 的 else 也能兜住超范围的值，或者先用 if 校验）。
4. <strong>倒计时打印</strong>：用 <code class="inline">downTo</code> 从 10 打印到 1，最后一行打印"发射！"——发射那一行在循环外面。
5. <strong>空值模拟器</strong>：声明一个可空的 <code class="inline">var phone: String? = null</code>，分别用三种方式处理它：?: 给默认值"未填写"、?.let 打印值、!! 亲眼看一次崩溃（就这一次，体验一下什么叫"运行时惊喜"）。
6. <strong>整除陷阱亲历记</strong>：打印 <code class="inline">5 / 2</code> 和 <code class="inline">5.0 / 2</code> 的结果，然后写一个函数 <code class="inline">fun average(scores: List&lt;Int&gt;): Double</code> 正确算出平均值——提示：先把 sum() 转成 Double 再除 size。这道题专治"整数除法想当然"。

五题全部跑通的成就感，比看完全章课文要实在得多。哪题卡住了，回到对应小节看一遍示例再写——卡住说明那块知识点没焊牢，正是要补的地方。写完别删，下一节你会用第四题的代码做对照实验。

#### 先当读者，再当作者：读代码的方法

这一章教的是"写"，但占你未来时间更多的其实是"读"——读别人的代码、读自己三个月前的代码。读代码有一套独立的方法，现在就练：

- <strong>第一遍只看骨架</strong>：变量名、函数名、缩进结构。跳过所有细节，回答一个问题："这段代码大概在干嘛？"对上面的 splitBill，第一遍你应该能说出"算 AA 制"。
- <strong>第二遍顺数据流</strong>：挑一个变量从头跟到尾。比如跟 splitBill 里的 total：它从参数进来，被除法用掉，变成返回值，变成 share，最后被打印。数据从哪来、变成什么、去了哪，这条线清楚了，代码就"通"了。
- <strong>第三遍才抠语法</strong>：哪个符号不认识查哪个。新手常犯的错是第一遍就抠语法，被一个没见过的写法卡死，忘记了整段代码在干嘛。语法问题永远是局部问题，别让它绑架全局理解。

配套练习现在就能做：回到本节开头，重读那个 splitBill 和会员折扣的示例——这次用"顺数据流"的方法读一遍，你会有和初读完全不同的感受。这个方法在第 54 章读项目代码时是主力武器，先用小代码练熟它。

读和写的比例，老手们的共识大约是"读远多于写"——就像作家都是读书人。本书后面每章的示例代码，都值得用这套三遍法过一遍：第一遍骨架、第二遍数据、第三遍语法。习惯了之后，你会发现"看不懂"的焦虑少了一大半：不是代码变简单了，是你有了可靠的阅读路径。

#### 综合小例：从一句话需求到十几行代码

最后做个收束实验：把一个"一句话需求"翻译成代码，看看前四节的知识怎么合体。需求是——"我记了一周的花销，想知道总共花了多少、最大的一笔是多少、哪几天花了钱"。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 一周花销统计</span><span class="dots">···</span>
:::

```
val expenses = listOf(12.5, 88.0, 5.0, 23.3, 0.0, 66.0, 45.2)

val total = expenses.sum()                      // 总共：240.0
val biggest = expenses.max()                    // 最大的一笔：88.0
val days = expenses.count { it > 0 }            // 有花销的天数：6

println("本周合计：$total 元")
println("最大单笔：$biggest 元")
println("花钱的日子有 $days 天")
```
:::

十几行，把"数据结构（listOf 装一周花销）+ 计算（sum、max）+ 条件统计（count { it > 0 }）+ 输出（字符串模板）"四件事全干了。其中 <code class="inline">count { it > 0 }</code> 是"满足条件的个数"——花括号里的 <code class="inline">it</code> 是第六节 lambda 的主角，这里先混个脸熟：它代表"每一个正在被检查的数"。这个例子值得存档，第 54 章做记账本时，你统计月度支出的代码和它几乎是同一个骨架，只是数据从七个数变成了数据库里的一千条。

从这个例子里你还该带走一个习惯：<strong>需求先翻译成三五个短句，每个短句对应一行代码。</strong>"总共花了多少"→ sum；"最大一笔"→ max；"哪几天花了钱"→ count 条件。代码写作的真正难度不在语法，在"翻译"——把含糊的人话拆成精确的短句。这个能力本书第七篇（第 39 章上下文工程、第 40 章需求工程）从 AI 协作的角度系统讲过，原理相通：表达得清楚，才做得出来。

#### 五、类与对象：造"零件"的模具

类是对象的"模具"，对象是类的"成品"。安卓里的一切——页面、按钮、数据——都是对象。Kotlin 里有个神器叫 <strong>data class</strong>（数据类），专门用来"装数据"，一行顶 Java 几十行：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 类与数据类</span><span class="dots">···</span>
:::

```
// 普通类：模具
class Dog(val name: String) {
    fun bark() = println("$name 汪汪！")
}

val dog = Dog("旺财")      // 造对象
dog.bark()                 // 旺财 汪汪！

// data class：装数据的盒子（自动带 equals/copy 等）
data class User(val id: Int, val name: String, val email: String)

val me = User(1, "张三", "zhangsan@example.com")
val twin = me.copy(name = "张三丰")   // 复制并改一个字段
```
:::

以后你做记账本，一笔账就是一个 data class：<code class="inline">data class Record(val amount: Double, val category: String, val date: String)</code>。看，你已经能写出真实项目的代码结构了。

普通类和 data class 的分工现在就能说清：<strong>普通类装"会做事的东西"（Dog 会叫），data class 装"被记录的事实"（一笔账、一个用户）。</strong>这个分界在界面开发里极其好用：按钮、页面用普通类（严格说是 Compose 函数，第 51 章见），用户的一笔账、一条消息、一次天气查询结果，全是 data class。你写 App 的大部分时间都在跟"事实"打交道，所以 data class 的出场率远高于普通类——这也是为什么它值得单独一节深讲。

类声明里 <code class="inline">val name: String</code> 直接写在括号里的写法叫"主构造函数"——声明属性的同时声明了"造出来需要什么"。对象造出来后，<code class="inline">dog.name</code> 就能读到名字。Kotlin 还默认给你防了一手：所有属性都必须"出生时就有值"，不存在"造出来是空的回头再补"的对象——又是空安全思想在类层面的延伸。

#### data class 深度：它到底帮你生成了什么

"一行顶几十行"不是广告词。写一个 data class，编译器悄悄替你生成了四样东西，每样都有用：

- <strong>equals()：按内容比较</strong>。两个 User 只要三个字段都相同，== 就是 true。前面误区清单说过 Kotlin 的 == 比较内容——对 data class 来说，"内容"就是这些字段。这在"判断列表里有没有这条记录"时天天用到。
- <strong>hashCode()：让对象能放进 Set、当 Map 的键</strong>。它是 equals 的"搭档"，两者配套工作。现在只需要知道：想用 <code class="inline">setOf(这笔账, 那笔账)</code> 去重，data class 的账对象才行为正确。
- <strong>toString()：打印时自己报家门</strong>。<code class="inline">println(me)</code> 输出 User(id=1, name=张三, email=...) 而不是一串看不懂的哈希码。调试时的救命特性——打印一个列表，每条数据清清楚楚。
- <strong>copy()：批量改字段的复制</strong>。<code class="inline">me.copy(name = "张三丰")</code> 造出一个"只有名字不同"的新对象。这招在界面开发里是主力：第 51 章讲"状态不可变、要改就造新的"，造新对象靠的就是 copy。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · data class 的四件套体验</span><span class="dots">···</span>
:::

```
data class Record(val amount: Double, val category: String, val date: String)

val a = Record(12.5, "餐饮", "10-01")
val b = Record(12.5, "餐饮", "10-01")

println(a == b)            // true——按内容比较，不是"同一条"才算相等
println(a)                 // Record(amount=12.5, category=餐饮, date=10-01)
val edited = a.copy(amount = 20.0)   // 只改金额，其他字段原样带走
println(edited)            // Record(amount=20.0, category=餐饮, date=10-01)
```
:::

还有一个隐藏福利：解构。<code class="inline">val (amount, category, date) = a</code> 一行把三个字段拆给三个变量——顺序就是字段声明顺序。第三节埋的 withIndex 伏笔在这里接上了：同一个语法，既能拆列表的"下标+元素"，也能拆数据类的各个字段。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>注意：data class 的字段也要守 val 优先

{class="mt-1"}
data class 的字段默认都写成 <code class="inline">val</code>（只读）——改数据用 copy 造新对象，而不是直接改旧对象的字段。"数据不可变 + 改动即复制"是现代界面开发的通行哲学，Compose 把它当基本前提。刚开始会觉得绕，用两次就顺了。
:::

#### 密封类：把"状态"圈起来

data class 之后，Kotlin 还有一件配套武器叫 <strong>sealed class（密封类）</strong>。它解决的问题是：怎么把"一个东西只可能是这几种情况"编码给编译器看。看例子就懂：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 密封类建模界面状态</span><span class="dots">···</span>
:::

```
sealed class UiState {
    object Loading : UiState()                          // 加载中（没有数据，用 object）
    data class Success(val list: List&lt;String&gt;) : UiState()   // 成功（带着数据）
    data class Error(val message: String) : UiState()   // 失败（带着原因）
}

fun render(state: UiState): String = when (state) {
    is UiState.Loading -> "加载中…"
    is UiState.Success -> "加载到 ${state.list.size} 条数据"
    is UiState.Error -> "出错了：${state.message}"
}
```
:::

三句话解读。第一句：UiState 是密封类，它圈定了"界面状态只可能是 Loading、Success、Error 三种"，子类必须在花括号里出生——这就是"密封"的含义，圈外不许有第三个可能。第二句：三种可能里有的是"光秃秃的状态"（Loading 用 object），有的是"状态+数据"（Success 带着 list，Error 带着 message）——data class 和 object 各司其职。第三句：when 处理密封类时，编译器知道可能情况全部枚举了，<strong>漏写一个分支直接编译报错</strong>。以后产品加第四种状态"空数据"，你把 when 一编译，所有没处理它的地方全部标红——编译器替你做全局检查。

"加载中 / 成功 / 失败"这个三态模型是联网界面的万能骨架，第 55 章的天气 App 就是它 + sealed class + when 的组合。现在先把密封类当"带编译器检查的状态清单"用，第 51 章界面状态、第 53 章网络请求都会反复用到它——这是 Kotlin 对安卓 UI 开发最重要的语言级贡献之一。

#### 与 Swift 对照：struct、enum 与 Kotlin 的答案

这一节的对照最有意思，因为 Swift 给出的方案和 Kotlin 不同但目标一致——"把数据建模做简单、把状态穷尽做安全"：

- <strong>data class ≈ struct</strong>：Swift 的结构体（struct）自动获得按值的相等比较和"成员逐一构造"，日常装数据用它。Kotlin 用 data class 达成同样的体验。区别在内存语义（Swift struct 是值类型、复制即拷贝；Kotlin data class 是引用类型、copy 才产生新对象），初学阶段感受不到，先不深究。
- <strong>密封类 ≈ 带关联值的 enum</strong>：Swift 的 enum 可以为每种情况"携带数据"（associated values）：<code class="inline">enum UiState { case loading; case success([String]); case error(String) }</code>。Kotlin 的 sealed class + data class 子类是同一件事的另一种写法。两边都靠 switch/when 做穷尽检查——漏分支编译报错的行为两边一致。
- <strong>协程预告 ≈ async/await</strong>：下一节讲协程时你会再对一次表——Swift 的 async/await 和 Kotlin 的 suspend 概念同源，都是"让等待不阻塞"。先记住这条线索。

总结成一个记忆框架：<strong>Kotlin 用"类"的世界解决这两件事（data class 装数据、sealed class 圈状态），Swift 用"值与枚举"的世界解决（struct 装数据、enum 圈状态）。</strong>路线不同，终点相同。所以"学了两门语言会不会乱"的担心可以放下了——它们在你脑子里会自动形成一张对照网，越学越牢。

#### 六、lambda 与高阶函数：Kotlin 的"语法糖"

安卓代码里你会天天看到 <code class="inline">{ ... }</code> 这种"没名字的函数"，它叫 <strong>lambda（匿名函数）</strong>。Button 的 <code class="inline">onClick = { count++ }</code> 就是一个 lambda——把"点击后做什么"打包成一坨，递给按钮。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · lambda 初体验</span><span class="dots">···</span>
:::

```
// 普通写法：定义一个有名函数再传入
fun double(x: Int) = x * 2
val result = listOf(1, 2, 3).map(::double)

// lambda 写法：就地定义，轻快直接
val result2 = listOf(1, 2, 3).map { it * 2 }   // it = 当前元素

// 筛选 + 变换连招（真实项目里极常见）
val bills = listOf(12.5, 88.0, 5.0, 200.0)
val bigBills = bills.filter { it > 50 }.sorted()
// [88.0, 200.0]——"超过 50 的账单，排好序"
```
:::

几个高频"集合连招"记一下：<code class="inline">filter</code>（筛选）、<code class="inline">map</code>（变换）、<code class="inline">sorted</code>（排序）、<code class="inline">sum</code>（求和）。你未来 90% 的列表处理，都是这四招的组合。Kotlin 的哲学就是：<strong>能用一句话说清楚的逻辑，绝不写五句</strong>。

it 这个魔法值得拆开讲一次。lambda 的完整写法是 <code class="inline">map { x -> x * 2 }</code>——箭头左边声明参数名，右边写逻辑。当 lambda 只有一个参数时，Kotlin 让你省掉声明，用默认名 it 代替：<code class="inline">map { it * 2 }</code>。什么时候不用 it？嵌套 lambda 时（两个 it 会打架，内层要手动起名，比如 <code class="inline">map { outer -> outer.map { inner -> inner * 2 } }</code>），或者参数含义需要自述时（起名 readability 更好）。理解了 it 是"默认的单参数名"，看到别人代码里的 it 就再也不会心慌。

四招连招的"手工等价版"写一次，你就明白它们替你省了什么：filter 手写就是一个 for 循环加 if，把满足的塞进新列表；map 手写就是一个 for 循环加新列表.add。这些循环你迟早都会写，但会写了不代表要天天写——连招让"意图"直接出现在代码里：filter 一看就知道"在筛选"，三行 for 循环得读完才知道。代码是写给人看的，顺带让机器执行——连招是这句话的最佳注脚。

#### 高阶函数：自己写一个试试

"高阶函数"听着唬人，定义简单：<strong>参数里有函数、或返回值是函数的函数</strong>。上面的 map 就是——它的参数是"一个变换逻辑"（lambda）。自己写一个，立刻祛魅：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 第一个高阶函数</span><span class="dots">···</span>
:::

```
fun calc(a: Int, b: Int, op: (Int, Int) -> Int): Int {
    return op(a, b)
}

println(calc(3, 5) { x, y -> x + y })   // 8
println(calc(3, 5) { x, y -> x * y })   // 15
println(calc(10, 3) { x, y -> x - y })  // 7
```
:::

读一下签名：<code class="inline">op: (Int, Int) -> Int</code> 的意思是"op 是一个函数，吃两个 Int，吐一个 Int"。调用时把具体的逻辑用 lambda 塞进去：加法、乘法、减法，同一个 calc 全能干。这就是"把行为当参数传"的威力——<strong>变化的逻辑写成参数，不变的框架写成函数</strong>。空调的"模式"键就是这个思想的实体：制冷、制热、除湿是传进去的行为，吹风框架是函数本体。

调用时那个 <code class="inline">calc(3, 5) { ... }</code> 的写法叫"尾 lambda"（trailing lambda）：函数的最后一个参数是 lambda 时，花括号可以挪到括号外面。这是 Kotlin 的招牌排版，Compose 里满屏都是它——以后你写 <code class="inline">Button(onClick = { ... }) { Text("点我") }</code>，用的就是这个语法。现在知道"花括号为什么能在外面"就够了。

为什么要学自己写高阶函数？因为你会在真实代码里遇到它们——安卓框架里大量 API 吃函数参数（各种回调、配置块）。能看懂签名、能写出调用，你就拿到了安卓 API 世界的通行证。自己造高阶函数的机会反而不多，读和调是主战场。

#### 集合连招进阶：groupBy、associate、fold

四招基础连招之外，还有三招中阶连招，记账本和统计类功能里出场率极高：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 中阶连招</span><span class="dots">···</span>
:::

```
data class Record(val amount: Double, val category: String)

val records = listOf(
    Record(12.5, "餐饮"), Record(30.0, "交通"),
    Record(20.0, "餐饮"), Record(88.0, "购物")
)

// groupBy：按某个条件分组，得到"组名 -> 组员列表"的 Map
val byCategory = records.groupBy { it.category }
println(byCategory["餐饮"]?.size)   // 2（餐饮组有两条）

// associateBy：按某个字段建立索引，得到"键 -> 对象"的 Map
val byName = records.associateBy { it.category }

// fold：带着"累积值"遍历——比 sum 更自由的归并
val total = records.fold(0.0) { acc, r -> acc + r.amount }
println(total)                      // 150.5

// 组合技：分组后算各组总额
val sums = records.groupBy { it.category }
    .mapValues { (_, group) -> group.sumOf { it.amount } }
println(sums)                       // {餐饮=32.5, 交通=30.0, 购物=88.0}
```
:::

组合技那几行值得多看两眼——"按分类分组，再把每组的金额加总"，这就是记账 App"分类饼图"背后的全部数据加工。<code class="inline">sumOf { it.amount }</code> 是 sum 的带字段版，专门对付对象列表。<code class="inline">mapValues</code> 是 map 的"只变值不变键"版。连招库比想象的大，但记住本节开头的话：你不需要全记住，需要时查，用三五次就长在脑子里了。

读连招代码的诀窍送你一个：<strong>从左往右读成流水句</strong>。"records.groupBy { 它的分类 }.mapValues { 组合计 }"读出来就是"先分组、再求每组合计"。连招代码的可读性建立在"每个函数名都是动词"上——filter 筛、map 变、group 分组、fold 折叠、sum 加总。像读句子一样读代码，这是 Kotlin 社区引以为傲的阅读体验。

#### 扩展函数：给别人的类"加挂件"

接下来这招最能体现 Kotlin 的巧劲。<code class="inline">String</code> 是标准库的类，你改不了它的源码，但 Kotlin 允许你"从外面给它装新方法"——这叫<strong>扩展函数</strong>：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 扩展函数</span><span class="dots">···</span>
:::

```
// 给 String 加一个"喊话"方法
fun String.shout(): String = this.uppercase() + "！！"

println("你好".shout())          // 你好！！
println("kotlin".shout())        // KOTLIN！！

// 给 Int 加一个"打折"方法
fun Int.discount(rate: Double): Double = this * rate

println(100.discount(0.8))       // 80.0

// 更实用的例子：金额格式化
fun Double.toPrice(): String = "%.2f".format(this)
println(54.1.toPrice())          // 54.10
```
:::

语法的读法：<code class="inline">fun String.shout()</code>——"给 String 扩展一个叫 shout 的函数"。函数体里的 <code class="inline">this</code> 指"被作用的那个字符串本身"。写好之后，任何字符串后面直接 <code class="inline">.shout()</code>，就像它原生自带这个方法一样。IDE 的补全列表里它和官方方法并肩出现，完全无缝。

它解决的真实痛点是：第三方类的功能不够用时，你不用继承、不用工具类（<code class="inline">PriceUtils.format(54.1)</code> 那种），直接"挂件式"补方法。安卓开发里有一批框架级好物本身就是扩展函数构成的——比如 Compose 里给界面元素"上妆"的 Modifier（第 51 章主角），链式调用的一环环全是扩展。可以这样理解扩展函数：<strong>它是"把常用操作变成 .方法"的包装术</strong>，学会了它，你写代码的语感会明显接近官方库的语感。

与 Swift 对照收个尾：Swift 的 extension 和 Kotlin 的扩展函数几乎是同一招，<code class="inline">extension String { func shout() -> String { ... } }</code> 等价于上面的写法。两边连"不能添加存储属性、只能加方法"这条限制都一致。这已经是本章第三组"殊途同归"了——空安全、数据建模、扩展，三门语言（加上 Java 当对照组）的演进方向惊人一致。

#### 协程入门：会"等待"的代码

本章最后一个语言点，解决一个必须面对的问题：<strong>等待</strong>。App 查网络要等两秒、读大文件要等一秒——等待期间界面不能冻结（冻住的 App 叫"无响应"，用户会直接划掉它）。Kotlin 的答案是<strong>协程（coroutine）</strong>：让"慢操作"在后台等，等完再回来更新界面，而代码写起来还是一行行往下读的样子。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 协程初体验（Playground 可跑）</span><span class="dots">···</span>
:::

```
import kotlinx.coroutines.*

fun main() = runBlocking {
    launch {
        delay(1000L)                    // 模拟"等 1 秒"（网络、读文件）
        println("慢操作完成了")
    }
    println("这行先打印")               // 不会等上面那秒，立刻执行
    delay(1500L)                        // 撑住 main，让协程有时间跑完
}
```
:::

三个新面孔，各给一句话解释。<strong>suspend</strong>：能"暂停再恢复"的函数标记，本例里 delay 就是标准库的 suspend 函数——它暂停的是当前协程，不是整个程序。<strong>launch</strong>："开一个后台任务"，花括号里的东西去别处跑，本行立刻往下走。<strong>runBlocking</strong>："开一个能等协程的容器"，Playground 和 main 函数里用它兜底；真实安卓项目里你几乎不用它，界面有专门的容器（viewModelScope，第 53 章的主角）。现在只需要建立直觉：<strong>慢活儿丢进 launch，界面该干嘛干嘛，活儿干完自动回来</strong>。

协程的完整故事（作用域、异常、Flow）是第 53 章的主菜，这里只上一盘开胃菜，够你在 Playground 里玩"同时跑三个 delay、看谁先打印"的小实验即可。与 Swift 对照：协程 ≈ Swift 的 async/await——suspend 函数 ≈ async 函数，launch ≈ Task。两边都是"用同步的写法干异步的活"，这是现代语言的又一次殊途同归，也是本章最后一次对照——你会发现每次对照，"现代语言进化论"都在加强。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：协程最容易记错的一件事

{class="mt-1"}
协程不等于多线程，它是"可暂停的任务"。大多数时候你不需要关心它跑在哪个线程上——框架已经替你安排好了（界面相关的活儿在主线程，网络文件在后台线程，第 53 章细说）。新手阶段对协程的过度关心，九成九是提前焦虑。
:::

为什么"别挡界面"这件事如此重要，值得单独用语言特性来解决？给你一个画面：界面绘制由主线程负责，主线程每秒要画几十帧——就像翻页动画，翻得够快才流畅。如果主线程被一个"等 2 秒的网络请求"占住，动画就翻不动了：手指滑动没反应、按钮按下去没动静、系统弹"应用未响应"。用户体验里最致命的几种差评，全都指向这一个原因。所以现代语言纷纷把"让等待不挡路"做成语言级能力——Kotlin 的协程、Swift 的 async/await、Dart 的 async/await，出发点一模一样。

协程在本书的出场安排也值得交代清楚，帮你规划学习节奏：本章建立三个直觉（launch、delay、suspend 能等）；第 51、52 章写界面和页面跳转时几乎不碰它；第 53 章做网络请求和数据库时它会大举登场——viewModelScope、withContext 这些进阶名字都在那一章解锁。学协程的最好方式就是"用真实需求倒逼"，比现在硬啃文档有效得多。

#### 七、写给零基础的语法速查卡

别试图一天背完所有语法。把这张卡存下来，写代码时对照着查，两周后自然就熟了：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要做什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">写法</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定义只读变量</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">val x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定义可变变量</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定义函数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">fun 名字(参数): 返回类型 { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">判断</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">if (条件) {...} else {...}</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多分支</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">when { 条件 -> 结果 }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">遍历</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">for (x in 列表) { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">字符串拼接</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">"你好，$name"</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">处理可空</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">x?.length ?: 0</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定义数据类</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">data class X(val a: Int, val b: String)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kotlin 语法速查卡（新手版）

学完本章再看这张卡，每行你都应该"见过真人"了。卡片是索引不是教材——第 54 章开工第一天，把它放在手边，写到哪里查到哪里。用两周你会发现查得越来越少：语法从"记忆"变成了"手感"，就像你打字不再需要看键盘。

想给这张卡"扩容"的话，把本章后半章的三行也补上去：定义数据类带字段 <code class="inline">data class X(val a: Int)</code>、给类加方法 <code class="inline">fun String.f(): String</code>、后台任务 <code class="inline">launch { ... }</code>。自己动手补的卡片记得最牢——手抄一遍速查卡，抵得上目读十遍，这个朴素的道理在学习语法上依然成立。

这张卡也给你一个"自查清单"的用法。每次代码编译报错，先扫一遍速查卡对不对号——<code class="inline">val cannot be reassigned</code> 对应第一行，<code class="inline">unresolved reference</code> 八成是拼错名字。把报错和速查卡的行对上，你就在建立"报错暗号 → 语法知识"的检索表，这是后面门诊一节的预热。

#### Kotlin Playground：一周练习路径

章首说过 20% 语法干 80% 的活，这一节把"干活的练习"排成一个七天的表。每天 20-30 分钟，全部在 Kotlin Playground（play.kotlinlang.org）完成，不需要装任何东西：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">第几天</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">练什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">小任务</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 1 天</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">val/var、数字、字符串模板</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">写一段"自我介绍生成器"：三个变量拼一段话；再体验一次 5/2 的整除陷阱</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 2 天</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">函数、默认参数、具名参数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">写 splitBill 的完全版：含小费、含抹零参数，两种调用方式各来一次</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 3 天</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if/when、区间、循环</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">写"温度穿衣指南"：when 区间匹配，输出五档穿衣建议</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 4 天</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List 与四招连招</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">给一组账单做统计：总和、大额筛选、排序、平均（记得先转 Double）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 5 天</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">空安全四件套</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">做一个"联系卡"：可空的邮箱和电话，用 ?: 和 ?.let 分别处理，打印三种状态</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 6 天</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">data class、sealed class、扩展函数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">建 Record 数据类 + 分组统计；给 Double 写 toPrice() 扩展并用到列表打印上</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第 7 天</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">综合 + 协程</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把前六天代码拼成"迷你记账本"：录入三条账、按类统计、格式化输出；末尾加一个 launch+delay 模拟"异步存档"</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Playground 一周练习路径（每天 20-30 分钟）

这张表的用法有三个讲究。第一，<strong>先写再看</strong>：每天的任务先自己敲，卡住了再翻本章对应小节，最后才对照本章示例。第二，<strong>允许抄自己的</strong>：第 6、7 天大量复用前面的代码——复用是真实开发的常态，不是作弊。第三，<strong>第 7 天的成品存档</strong>：Playground 支持保存和分享链接（右上角 Share），把你的迷你记账本链接存下来，这是你学习过程的第一个"作品"。

七天之后怎么走？答案在下一章——同样的语法，开始给界面用。你会发现第 51 章的 Compose 代码读起来亲切得可疑：满屏的 val、lambda、具名参数——对，全是你这两周练过的东西。语言学习到界面开发，不是换赛道，是换场景。

#### 八、Kotlin 2.x 值得留意的变化

最后交代一下版本：这一章学的语法主干多年没变，但编译器换了代——Kotlin 2.x 背后的 K2 编译器。几处体验差异值得知道，尤其是从旧教程里抄代码的时候：

- <strong>K2 编译器</strong>：编译更快、类型推断与错误信息更清楚；旧项目升级后，个别边界写法可能报新警告，按提示补上显式类型就好。
- <strong>Compose 插件由 Kotlin 管</strong>：<code class="inline">org.jetbrains.kotlin.plugin.compose</code> 与 Kotlin 版本绑定，别再手动指定编译器扩展版本——上一章装环境时也提过这条。
- <strong>显式类型是好习惯</strong>：空安全之外，给公开函数写明返回类型、给回调写明参数类型，既方便人读，也方便智能体改。
- <strong>协程仍是异步主线</strong>：suspend + CoroutineScope 的组合没变；注意在 ViewModel 作用域里启动，别用全局作用域。
- <strong>与 ArkTS 的对照</strong>：后面鸿蒙篇的 ArkTS 同样强调显式类型与严格模式；两边都学的话，这一点是共通的。

版本号的具体语境再补一句：写这本书的时候，Kotlin 的稳定版是 2.4 系（2.4.x），上一章版本表里"Compose 1.13 要求 Kotlin 2.2"说的就是这条进化线上的门槛。你不需要追最新版——<strong>语法主干在 2.x 全系通用</strong>，本章代码在 2.2、2.3、2.4 上跑起来没有差别。真正要盯版本号的场景只有一个：新项目向导生成的 Kotlin 版本和网上某篇教程不一致时，以你的向导为准，教程的思路照学，数字照抄反而容易错位。

"语言版本升级学不学新东西"的判断方法也给你一套：看<strong>语法层面的新增</strong>（新关键字、新语法糖）和<strong>行为层面的收紧</strong>（编译器开始拒绝以前容忍的写法）。前者值得学——它们通常是效率工具；后者不用怕——报错信息会教你怎么改，而且改完的代码更稳。这正好呼应本章空安全的哲学：编译器变严，是它在替你的用户挡崩溃。

::: div .tip-box .rounded-lg .p-4 .mb-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>一句话记牢

{class="mt-1"}
语言版本升级通常不动语法，动的是「编译器愿意容忍什么」。报错变多往往是变严格了，不是你写错了。
:::

#### 编译报错暗号表：新手最常见的五条

K2 时代的报错信息已经相当"说人话"，但英文报错依然会吓到新手。五条最常见的暗号，配上翻译和解法：

- <strong>Unresolved reference: xxx</strong>——"我不认识 xxx 这个名字"。翻译：拼错了、没导入、或者你引用的东西还没定义。解法：先查拼写（IDE 的红色下划线会圈出），再 Alt+Enter 看有没有"import"的快修建议，最后确认依赖里的库真的加了。
- <strong>Val cannot be reassigned</strong>——"val 不许改"。翻译：你用 val 声明了又想赋值。解法：真的会变就改 var，不会变就删掉那句赋值——九成情况是后者，顺手就守了 val 优先。
- <strong>Type mismatch: inferred type is X but Y was expected</strong>——"类型对不上，你塞的是 X，槽位要 Y"。翻译：类型转换没做。解法：按提示转换（toDouble()、toString() 之类）。新手期最常见的具体案例是 Int 没转 Double 就参与除法。
- <strong>Null can not be a value of a non-null type X</strong>——"这个类型不许 null"。翻译：你把 null 塞给了不带问号的类型。解法：要么真会为空就加问号（类型后补 ?），要么给默认值。编译器在逼你想清楚"这东西到底会不会没有"，这是好事。
- <strong>Not enough information to infer type variable T</strong>——"信息不够，猜不出类型"。翻译：你写的表达式太"空"了，编译器无从推断。解法：给变量显式写类型，或者给列表塞初始内容。<code class="inline">val list = mutableListOf()</code> 这种空列表是高发区，补成 <code class="inline">mutableListOf&lt;String&gt;()</code>。

读报错的通用姿势复述一遍上一章的方法论：<strong>从第一条报错读起，别被几十条吓住</strong>——后面的报错多半是第一条的连锁反应；报错行号指向的是"编译器发现不对的地方"，不一定是你写错的地方，顺着变量和数据流往上游找（第四节读代码的三遍法在这里同样管用）。解决了第一条，刷新一次，列表往往清空一半。

#### 误区清单：后半章概念的五个想当然

后半章的概念抽象度高，误区也跟着多起来。五个最典型的想当然，逐个纠正：

- <strong>误区一：以为 data class 的字段要写成 var 才能改。</strong>其实恰恰相反——data class 的字段默认 val，改数据靠 copy 造新对象。写成 var 虽然编译器不拦，但会破坏"数据不可变"的默契，界面开发里会踩到状态混乱的坑。
- <strong>误区二：以为 lambda 是"语法玩具"，正式项目里要少用。</strong>恰恰相反——连招（filter/map）、回调（onClick）、Compose 的界面声明，全都是 lambda。它是正式项目的主力写法，不是玩具。
- <strong>误区三：以为密封类就是"普通类的父类"，随便继承。</strong>密封类的全部价值在于"子类穷尽且圈定"——子类必须和它写在同一个包的同一层结构里，圈外继承直接编译报错。正因为圈死了，when 才敢做穷尽检查。别把它当普通继承用。
- <strong>误区四：以为扩展函数会"污染"别人的类。</strong>扩展函数的作用域由你导入的方式决定——不 import 就看不见，完全无害。它不修改原类的字节码，只是"在你自己的文件里多了一个函数"。可以放心大胆地写。
- <strong>误区五：以为 fold 比 sum 高级，处处该用 fold。</strong>fold 是 sum 的"通用版"，通用意味着啰嗦。简单求和用 sum，只有"要带着中间值做复杂累积"（比如累乘、按条件跳着加）才请出 fold。用最顺手的工具，不炫技。

#### 实战演练：迷你记账本（Playground 完整版）

本章所有知识点的大合练，一份可以直接粘进 Playground 跑的完整小程序。建议先自己照着"七天练习路径"拼一遍，拼不出来再看这份参考——参考的意义是对照，不是替代：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 迷你记账本（合练版）</span><span class="dots">···</span>
:::

```
data class Record(val amount: Double, val category: String, val note: String)

fun Double.toPrice(): String = "%.2f".format(this)   // 扩展函数：格式化金额

val records = listOf(
    Record(12.5, "餐饮", "午餐"),
    Record(30.0, "交通", "地铁"),
    Record(88.0, "购物", "卫衣"),
    Record(20.0, "餐饮", "奶茶")
)

// 总支出（sum 连招）
val total = records.sumOf { it.amount }
println("总支出：${total.toPrice()} 元")

// 分组统计（groupBy + mapValues 组合技）
val byCategory = records.groupBy { it.category }
    .mapValues { (_, group) -> group.sumOf { it.amount } }
byCategory.forEach { (category, sum) ->
    println("$category：${sum.toPrice()} 元")
}

// 大额消费（filter + sorted 连招）
val big = records.filter { it.amount > 25 }.sortedByDescending { it.amount }
big.forEach { println("大额：${it.amount.toPrice()} 元 - ${it.note}") }

// 状态建模（sealed class + when 穷尽检查）
sealed class Report {
    object Empty : Report()
    data class Summary(val count: Int, val total: Double) : Report()
}

val report = if (records.isEmpty()) Report.Empty
             else Report.Summary(records.size, total)
when (report) {
    is Report.Empty -> println("本周还没有记账")
    is Report.Summary -> println("共 ${report.count} 笔，合计 ${report.total.toPrice()} 元")
}
```
:::

三十行出头的代码里，val、字符串模板、data class、扩展函数、四招连招、组合技、sealed class、when 穷尽检查全部到场——这一章教的东西，一件不少。跑起来看看输出，然后用"三遍法"通读一遍：第一遍看骨架，第二遍跟 total 这条数据从 sum 到 report 的旅程，第三遍抠你不熟的写法。

这份合练还有第二层价值：<strong>它是第 54 章真实记账本 App 的"无界面预演"</strong>。到时候你会发现，真实项目只是把 listOf 换成了数据库、把 println 换成了界面显示，中间的数据加工逻辑和这里的三十行几乎逐行对应。语法课上出的力气，每一分都会在项目课上还给你——这就是"先学语言再看项目"路线的回报方式。

改这份合练的三个挑战，比照抄一遍收获大十倍：加一个"分类"筛选函数，输入分类名返回该类的所有记录（filter 一行的事）；给 Record 加一个 val 的时间字段，让大额列表按时间排（sortedByDescending 换个字段）；让空状态的提示更贴心——不要"本周还没有记账"，换成鼓励性的文案。改代码比写代码快，也比写代码涨功力，这三处小改动各只需一两行。

#### FAQ：数据类、lambda 与协程的四个快问快答

后半章的新概念多，收尾前把最集中的一批疑问清掉：

- <strong>问：data class 和普通类，我全用 data class 行不行？</strong>答：不建议。data class 的语义是"纯数据记录"，行为逻辑（方法）放多了会名不副实；而且主构造函数里每个字段都要有值、不能继承别的类，限制也不适合复杂对象。判断口诀：装事实用 data class，装行为用普通类。
- <strong>问：lambda 里那个 it 到底是什么类型的？</strong>答：由上下文推断。filter { it > 50 } 里 it 是 Double（列表元素的类型），map { it * 2 } 里 it 是 Int。你不用写类型——编译器知道。这也是"连招代码读起来像英文"的技术基础。
- <strong>问：扩展函数会修改原类吗？会不会有性能损失？</strong>答：不会修改，也几乎零损失。扩展函数编译后就是个普通函数，第一个参数悄悄变成了那个"被扩展"的对象——语法糖的本质是把"方法调用"翻译成"函数调用"。它的"魔法"只在书写层。
- <strong>问：协程要现在学深吗？看着有点吓人。</strong>答：不需要。本章你只需要三个直觉：慢活儿别挡界面、launch 开后台任务、suspend 函数能等。这三个直觉支撑你读完第 51、52 章；第 53 章做网络请求时会带着真实需求把协程学完整——那时它不再吓人，因为每个概念都有活儿等着它干。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：不装任何软件，先玩 10 分钟 Kotlin

{class="mt-1"}
浏览器打开 play.kotlinlang.org（Kotlin 官方在线演练场），把本章的每一段代码都粘进去跑一遍，改改数字和文字，看看输出怎么变。这个"先玩后学"的 10 分钟，会让你第 51 章上手时轻松一倍。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- val 优先，var 慎用；类型可自动推断，冒号后显式声明也行
- 函数 = 打包的逻辑；字符串模板 $ 是招牌便利
- if/when 判断，for 循环；when 是安卓开发里的"多面手"
- 空安全是 Kotlin 的保命符：普通类型拒绝 null，可空类型必须 ? / ?: 处理
- data class 是装数据的盒子，一个字段一行，真实项目天天用
- 20% 语法干 80% 的活：先会用，再精通
- Kotlin 2.x：语法没变，K2 编译器更快更严格；Compose 插件跟着 Kotlin 走
:::
