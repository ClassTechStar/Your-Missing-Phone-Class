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

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：val 优先原则

{class="mt-1"}
Kotlin 社区的铁律：<strong>默认用 val，确有必要再用 var</strong>。能用 val 的地方用 var，IDE 会黄字警告你。这个习惯能帮你少掉一大类"变量被意外修改"的 bug——代码越少变化，越容易推理。
:::

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

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>注意：? 和 ?: 别搞混

{class="mt-1"}
<code class="inline">String?</code> 是"允许为空"，<code class="inline">a ?: b</code> 是"a 为空时用 b"（长得像猫王发型，所以叫 Elvis 操作符）。刚开始写代码时，看到编译器报"null 相关错误"，八成是你忘了处理可空类型——这正是语言在保护你。
:::

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

#### 七、写给零基础的语法速查卡

别试图一天背完所有语法。把这张卡存下来，写代码时对照着查，两周后自然就熟了：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要做什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">写法</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定义只读变量</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">val x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定义可变变量</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定义函数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">fun 名字(参数): 返回类型 { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">判断</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">if (条件) {...} else {...}</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多分支</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">when { 条件 -> 结果 }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">遍历</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">for (x in 列表) { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">字符串拼接</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">"你好，$name"</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">处理可空</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">x?.length ?: 0</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定义数据类</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">data class X(val a: Int, val b: String)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kotlin 语法速查卡（新手版）

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
:::
