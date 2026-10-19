---
id: di-liu-shi-yi-zhang
num: 61
part: ios-kai-fa-pian
nav: 第六十一章：Swift快速上手——苹果开发的第一语言
toc: default
kind: chapter
---

### 第六十一章：Swift 快速上手——苹果开发的第一语言

{class="chapter-intro mb-4"}
这一章咱们正式学语言。别紧张——Swift 是出了名的"对新手友好"，而且你不需要背语法书：先掌握 20% 的语法，就能看懂和写出 80% 的日常代码。剩下的边做项目边查。记住咱们的学习原则：<strong>看懂 > 记住，会用 > 精通</strong>。

#### 一、变量与类型：给数据起名字

程序就是"数据 + 逻辑"。变量，就是给数据起个名字存起来。Swift 用 <code class="inline">let</code> 和 <code class="inline">var</code> 声明：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 变量</span><span class="dots">···</span>
:::

```
let name = "张三"        // let：常量（推荐默认用这个）
var age = 18             // var：变量（以后还能改）

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var 可以改
// name = "李四"         // <i class="fas fa-times-circle mr-1"></i> let 不能改，编译报错

let score: Int = 100     // 也可以显式写明类型
let pi = 3.14            // 不写也能自动推断

print("你好，\(name)")   // 字符串插值：反斜杠 + 括号
```
:::

常用类型一张表记住：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">类型</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">存什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">示例</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">整数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">小数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">文字</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"你好"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bool</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真/假</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[Int]（数组）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一组数据</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[1, 2, 3]</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Swift 常用基础类型

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：let 优先原则

{class="mt-1"}
Swift 社区的铁律：<strong>默认用 let，确有必要再用 var</strong>。能用 let 的地方用 var，Xcode 会黄字警告你。这个习惯能帮你少掉一大类"变量被意外修改"的 bug——代码越少变化，越容易推理。
:::

#### 二、可选值（Optional）：Swift 的"防崩护身符"

这是 Swift 最重要的概念，没有之一。一句话：<strong>一个值可能"不存在"时，Swift 强迫你处理它</strong>——从语言层面消灭了"空指针崩溃"这个行业噩梦。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 可选值</span><span class="dots">···</span>
:::

```
var name: String = "张三"   // 普通类型：绝不允许是 nil
// name = nil                // <i class="fas fa-times-circle mr-1"></i> 编译错误，直接拦住

var nickname: String? = nil  // 加个问号：允许为 nil（可选值）
nickname = "三儿"

// 使用可选值，必须"解包"：
if let n = nickname {        // if let：安全解包
    print("你好，\(n)")
} else {
    print("还没有昵称")
}

let len = nickname?.count ?? 0   // ?? 给默认值（空合运算符）
print(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>注意：! 是"高危操作"

{class="mt-1"}
代码里写 <code class="inline">nickname!</code>（强制解包）等于对编译器喊"我保证它不是 nil"——一旦猜错，App 当场崩溃。新手期原则：<strong>尽量用 if let / ?? ，不用 !</strong>。Xcode 补全代码时偶尔会顺手加 !，记得改掉它。
:::

#### 三、函数与闭包：把逻辑打包成"按钮"

函数是一段有名字的逻辑，像遥控器上的按钮。闭包（Closure）则是"没名字的函数"，可以随手递给别人：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 函数与闭包</span><span class="dots">···</span>
:::

```
// 函数：名字在前，参数和返回类型在后
func greet(name: String) -> String {
    return "你好，\(name)！"
}
print(greet(name: "张三"))     // 调用时要带参数名

// 闭包：就地定义，轻快直接
let numbers = [1, 2, 3, 4]
let doubled = numbers.map { $0 * 2 }   // $0 = 当前元素
// [2, 4, 6, 8]

let big = numbers.filter { $0 > 2 }    // 筛选
// [3, 4]
```
:::

SwiftUI 里闭包无处不在：按钮的 <code class="inline">Button("点我") { ... }</code> 后面的大括号就是一个闭包。<code class="inline">map</code>、<code class="inline">filter</code>、<code class="inline">sorted</code> 这几个"集合连招"请记牢——未来 90% 的列表处理都是它们的组合。

#### 四、结构体与协议：Swift 的"乐高"体系

Swift 的官方偏好很明确：<strong>优先用结构体（struct），需要继承时才用类（class）</strong>。结构体是"值类型"——复制时各过各的，天然少一类 bug：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 结构体与协议</span><span class="dots">···</span>
:::

```
// 结构体：装数据的盒子
struct Record {
    var id = UUID()
    var amount: Double
    var category: String
    var date: Date

    // 结构体自带"成员逐一构造器"：直接就能创建
}
let r = Record(amount: 25.5, category: "餐饮", date: Date())

// 协议：约定"必须具备哪些能力"
protocol Identifiable {
    var id: UUID { get }
}
struct Record: Identifiable { ... }   // 遵守协议 = 承诺实现其要求
```
:::

SwiftUI 里几乎一切都是 struct（View 就是协议）。这句现在不懂没关系，第 62 章会天天见面——<strong>在 Swift 的世界里，先拥抱 struct</strong>。

#### 五、写给零基础的语法速查卡

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要做什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">写法</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定义常量/变量</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">let x = 1</code> / <code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">字符串插值</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">"你好，\(name)"</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定义函数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">func 名字(参数: 类型) -> 返回类型 { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">判断</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">if 条件 { ... } else { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">遍历</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">for x in 数组 { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">安全解包</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">if let x = 可选值 { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">默认值</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">x ?? 默认值</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定义结构体</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X { var a: Int; var b: String }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">闭包</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">{ $0 * 2 }</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Swift 语法速查卡（新手版）

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：在 Playgrounds 里玩 15 分钟 Swift

{class="mt-1"}
有 Mac 就打开 Xcode → Playground；没 Mac 就用 iPad 上的 Swift Playgrounds 或网页版演练场。把本章每一段代码都跑一遍，改改数字和文字，故意制造几个错误看看 Xcode 怎么提示。这个"先玩后学"的 15 分钟，会让你第 62 章上手时轻松一倍。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- let 优先，var 慎用；类型自动推断，冒号后显式声明也行
- 可选值是 Swift 的灵魂：可能为空必须处理，if let / ?? 是护身符，! 是高危操作
- 函数调用要带参数名；闭包 = 没名字的函数，SwiftUI 里无处不在
- 优先 struct，遵守协议（Protocol）；SwiftUI 几乎一切都是 struct
- 20% 语法干 80% 的活：先会用，再精通
:::
