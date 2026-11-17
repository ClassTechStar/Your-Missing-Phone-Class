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

::: div .quick-read
##### 本章速读（5 分钟版）
这一章正式学 Swift，苹果开发的第一语言。和当年学 Kotlin 一样，定心丸先发：你不需要背语法书，先掌握 20% 的语法，就能看懂和写出 80% 的日常代码，剩下的边做项目边查。学习原则还是那句——<strong>看懂大于记住，会用大于精通</strong>。这一章的示例也都很小：算一笔 AA 别、给爸妈的记账本设计个备注栏，但真实项目的每块业务逻辑都是这些小零件拼出来的。

最关键的有三件事。第一，<strong>let 优先，var 慎用</strong>——可变面越小，程序越好推理，这条在 Kotlin、Swift、鸿蒙三边通用。第二，可选值（Optional）是 Swift 的灵魂，也是它的"防崩护身符"：可能为空的类型必须标问号，用的时候必须处理——if let 解包、双问号给默认值是护身符，感叹号强制解包是高危操作，能不写就不写。第三，装数据优先用 struct，能力建模用协议（Protocol）：SwiftUI 的组件几乎全是 struct，class 只在共享状态和继承时出场，谁主流谁配角，别按老语言的直觉排座次。还有两个高频写法混个脸熟：guard let 是"拿不到值就提前退场"的解包，比层层嵌套的 if let 清爽；扩展（extension）能给别人的类型"发装备"，把金额格式化这类常用操作挂上去，调用处立刻干净。

今天就能做的最小动作：打开 Swift Playgrounds（iPad 上就有，Mac 上用 Xcode 的 Playground），把"变量与可选值"那几段代码亲手敲一遍，改改数字看输出。章里有现成的"第一周菜单"：每天 15 分钟，一周下来集合、闭包、可选值、struct 这四样就混熟了——这四样在手，你已经能读懂真实项目的大部分代码。

最大的坑。有人觉得"全都用 var 更灵活"——灵活和失控是同一枚硬币的两面；有人把可选值当"要到处防的麻烦"——它其实是"把麻烦标出来"的机制，真正麻烦的是类型上看不出空、跑起来才崩的语言；有人动不动用感叹号或 try! 把"可能失败"写成"一定崩"，或者干脆把错误晾在一边不处理——省下的三秒钟，日后要用数倍的排查时间来还。还有一条放平心态：语言只是第一张拼图，界面、数据、调试发布都是独立技能块，别在 Playground 里原地踏步半年。
##### 速查表
- 变量怎么声明：默认用 let，确要修改才用 var
- 可能为空怎么写：类型后标问号，用 if let 解包、双问号给默认值，感叹号尽量别写
- 函数怎么调：Swift 调用要带参数名，读起来像一句对话
- 没名字的逻辑：闭包，SwiftUI 里无处不在，完整、简写、尾随三张脸都认得
- 装数据用什么：优先 struct，能力靠协议，class 只管共享状态和继承
- 多种情况怎么判：枚举加 switch，编译器逼你把情况想全
- 出错怎么办：throws 声明、try 调用，try! 是把"可能失败"变成"一定崩"
- 学过安卓怎么省力：翻章末的 Kotlin 对照速查，学过安卓省一半
:::

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

类型能自动推断就不必啰嗦，但有条反方向的建议：给公开的函数、接口写明类型——人读着清楚，Xcode 26 的预测式补全和编程智能也能给出更准的建议。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：let 优先原则

{class="mt-1"}
Swift 社区的铁律：<strong>默认用 let，确有必要再用 var</strong>。能用 let 的地方用 var，Xcode 会黄字警告你。这个习惯能帮你少掉一大类"变量被意外修改"的 bug——代码越少变化，越容易推理。
:::

##### let 与 var：铁律背后的道理

"默认用 let"听着像教条，其实是一条帮你省下半个夜晚的工程经验。给你一个真实到扎心的场景：凌晨十二点半，你改一个记账功能，界面上金额显示不对，翻了四十分钟代码，最后发现是另一个函数顺手把 <code class="inline">total</code> 改掉了。如果它当初声明的是 let，编译器早就把这段故事掐死在摇篮里——变量可改的范围越小，你能出错的面积就越小。

错误示范长这样：把所有东西都声明成 var。代码能跑，但读代码的人（包括三个月后的你自己）没法判断"这个值会不会中途被改"。正确做法反过来：先写 let，等编译器提醒"这个值改不了"的时候，再把需要改的那一个升级成 var。<strong>升级比降级安全</strong>，这个顺序别搞反。

<strong>与 Kotlin 对照</strong>：这条规则几乎可以逐字平移——第 50 章讲过 Kotlin 的 val 对应 Swift 的 let，var 对应 var，连"IDE 会黄字警告你"的体验都一样。你在哪边养成的习惯，到另一边都不用改，这是学第二门语言最省力的地方。

##### 类型推断：让编译器干粗活

绝大多数时候，你不必写类型——编译器看到引号知道是文字，看到小数点知道是小数。但有三个场合建议你显式标注，照做能少踩坑：

- <strong>公开的函数</strong>：参数和返回值写明类型，调用的人才一眼看懂"喂什么、吐什么"；
- <strong>空的可选值</strong>：<code class="inline">var nickname: String? = nil</code>——不写类型，编译器猜不出来这盒子以后装什么；
- <strong>数字有歧义</strong>：想让一个小数按 Double 处理还是按 Float 处理，写出来最稳。

数字这条路上还立着一堵新手必撞的墙，现在就撞一次，省得以后半夜撞：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 类型转换</span><span class="dots">···</span>
:::

```
let count = 5          // 推断为 Int
let price = 3.14       // 推断为 Double

// let total = count + price   // 报错：Int 和 Double 不能直接相加
let total = Double(count) + price   // 显式转换：8.14
```
:::

Swift 的数字<strong>不自动混算</strong>：整数和小数相加，必须先把一方转换过来。看着麻烦，实际是在帮你——很多语言里"整数溢出、精度丢失"的暗坑，都是混算混出来的，Swift 把这类事故的入口直接焊死了。遇到报错别烦，<code class="inline">Double( )</code> 或 <code class="inline">Int( )</code> 套一下就好。

<strong>与 Kotlin 对照</strong>：这一点两边不一样——Kotlin 做算术时会自动把 Int 提升成 Double，<code class="inline">5 + 3.14</code> 能直接算；Swift 则要求你亲手转换，更较真一步。记住"Swift 更严"这个基调，后面还会遇到好几次。

##### 字符串：插值、拼接与多行

Swift 处理文字的招牌动作是插值：反斜杠加括号，把任何值或表达式塞进字符串里。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 字符串</span><span class="dots">···</span>
:::

```
let first = "张"
let last = "三"
let full = first + last              // 拼接：张三
let greeting = "你好，\(full)！"      // 插值：你好，张三！
let line = "共 \(2 + 3) 项"          // 括号里可以放表达式

let bio = """
记账本说明：
一、每天睡前记一笔
二、月初看汇总
"""                                  // 多行字符串
print(bio)
```
:::

多行字符串用三个引号包起来，换行就是真的换行，不用满屏拼 <code class="inline">\n</code>。以后做帮助页、给爸妈写的使用说明，一段三引号就能排得整整齐齐。想知道一个字符串有几个字，用 <code class="inline">full.count</code>。

<strong>与 Kotlin 对照</strong>：Kotlin 的 <code class="inline">$name</code> 和 Swift 的 <code class="inline">\(name)</code> 是同一件事的两种写法。差别有二：Swift 必须带括号，Kotlin 单个变量可以裸写；取长度 Swift 是 <code class="inline">count</code>，Kotlin 是 <code class="inline">length</code>。切语言的时候，这两个符号最容易手滑。

##### 数字与运算：几个和别处不一样的规矩

四则运算的写法和数学课一致，<code class="inline">+</code>、<code class="inline">-</code>、<code class="inline">*</code>、<code class="inline">/</code>、取余数 <code class="inline">%</code> 都在；优先级也照旧——先乘除后加减，拿不准就加括号，加括号永远不算错。复合赋值 <code class="inline">+=</code>、<code class="inline">-=</code>、<code class="inline">*=</code> 也照常用：<code class="inline">count += 1</code> 比 <code class="inline">count = count + 1</code> 顺手。

一个冷知识提前说：Swift <strong>没有 <code class="inline">++</code> 和 <code class="inline">--</code></strong>——自增请写 <code class="inline">+= 1</code>。从 C、Java 过来的同学手指会叛变几天，忍忍就过去了。另外字符串也能用加号拼接（前面见过），但正式场合优先用插值，快且不容易漏空格。

<strong>与 Kotlin 对照</strong>：Kotlin 还保留着 <code class="inline">++</code>，Swift 是真的删掉了这一对运算符；其余运算符两边几乎一一对应。这种"小差异"值得在切换语言的前几天记在备忘录里，比出 bug 后再翻旧账强。

##### Bool 与判断：条件必须是"真布尔"

判断的逻辑哪门语言都差不多，Swift 的特别之处是死板得让人安心：if 后面只能放 Bool，别的什么都不行。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 判断</span><span class="dots">···</span>
:::

```
let hasPaid = true
if hasPaid {
    print("已解锁全部章节")
} else {
    print("先看免费章节")
}

let score = 85
let passed = score >= 60    // 比较的结果就是 Bool：true
print(passed)

// if score { }              // 报错：条件必须是 Bool，整数不行

let label = score >= 60 ? "及格" : "再补课"   // 三目运算符：一行二选一
```
:::

从 JavaScript 或 Python 过来的同学最容易在这里绊一脚：那些语言里 0、空字符串都能"当假"用，Swift 里这种写法直接编译不过。这不是语言死板，是把"条件必须是明确的真假"焊进语法——很多"以为有值其实没有"的崩溃，就是靠真值转换混进程序的。

<strong>与 Kotlin 对照</strong>：Kotlin 同样要求 if 条件是 Boolean，这点两边一样严。有个小差异：Kotlin 没有三目运算符，二选一用 if 表达式；Swift 有 <code class="inline">? :</code>。另外提醒一句，Swift 的 if、for 的括号可以省略，但大括号不能省——和 C 不同，别学着老代码把大括号也省了。

##### 注释与 print：写给三个月后的自己

注释两种：单行 <code class="inline">//</code>，多行 <code class="inline">/* ... */</code>。一个冷知识：Swift 的块注释可以嵌套，<code class="inline">/* 外层 /* 里层 */ 还在外层 */</code> 是合法的——批量注释一大段代码时偶尔能救急。给函数、类型写 <code class="inline">///</code> 开头的文档注释，之后按住 Option 点这个名字，Xcode 会把你写的说明弹出来，比翻文档快得多。

print 你在第 60 章已经用过了，它会在底部控制台打一行字。语言课阶段它是你唯一的"眼睛"：程序算出了什么、走到了哪一步，print 一下就现形。这章后面的代码示例都带 print，跑 Playground 时盯着输出看，比盯着代码干读记得牢。

##### 命名规范：让代码自己会说话

Swift 圈的命名规矩是"小驼峰"：变量和函数第一个词小写、后面的词首字母大写，比如 <code class="inline">userName</code>、<code class="inline">monthlyCost()</code>；类型名每个词首字母都大写，比如 <code class="inline">Record</code>、<code class="inline">VipMember</code>。Xcode 的补全默认就这么起名，你只要别手痒改就行。

比驼峰更要紧的是"读出来像话"。反面教材一抓一大把：<code class="inline">let a = 3</code>、<code class="inline">let data1</code>、<code class="inline">func doIt()</code>——写的时候省三个字母，读的时候多猜十分钟。正面示范：<code class="inline">let monthlyTotal</code>、<code class="inline">func loadBills()</code>，眼睛扫过去就知道是什么。一个自测窍门：把调用处这句话读出声，像不像一句中文？"月度合计 monthlyTotal"——像，就对了。

<strong>与 Kotlin 对照</strong>：两门语言的命名规范完全一致，连"类型大驼峰、成员小驼峰"的细节都同步。学过第 50 章的人在这件事上是零成本的；从别处来的同学，这条也和主流编程世界通用，学会了走到哪都不亏。

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

##### 为什么会有 Optional：从一个行业噩梦说起

在 Swift 出现之前，"什么都没有"这件事没有统一的表达：有的语言用 null，有的用 0，有的干脆假装它不存在，直到程序跑到那一刻才崩给你看。Java 的 NullPointerException 常年挂在崩溃排行榜前几名——第 50 章讲 Kotlin 空安全时提过它的"光辉历史"，这里是同一场噩梦的另一端。

Swift 的解法釜底抽薪：<strong>把"可能没有"写进类型本身</strong>。<code class="inline">String</code> 和 <code class="inline">String?</code> 是两个不同的类型——前者保证一定有字，后者承诺"可能空"。编译器盯着你：用到可能空的值，就必须先处理。这一道关，把一整类"上线后才崩"的事故，提前到了"编译时就报错"。

Optional 的本质一句话就能说清：它是一个<strong>盒子</strong>，里面要么装着一个值，要么空着。用的时候必须先开盒子看看——开盒子的手法有四式，下面挨个过。

##### 解包四式：if let、guard let、?? 与 !

::: div .code-block
:::inline div .code-head
<span>SWIFT · 解包四式</span><span class="dots">···</span>
:::

```
var nickname: String? = "三儿"

// 第一式：if let——顺手处理，有就用
if let n = nickname {
    print("昵称是 \(n)")     // 这个括号里，n 保证不是 nil
}

// 第二式：guard let——不满足就早退，主路保持平整
func showNickname() {
    guard let n = nickname else {
        print("没有昵称")
        return
    }
    print("昵称是 \(n)")     // 从这里往后，n 一直是普通 String
}
showNickname()

// 第三式：??——给个兜底值
let display = nickname ?? "匿名用户"
print(display)

// 第四式：!——强制开盒，猜错就崩（新手期别用）
// print(nickname!)
```
:::

四式的分工记一下：if let 适合"有就顺手处理一下"；guard let 适合"先确认装备齐全再出发"，把不正常的情况挡在门口，正常逻辑不用套一层缩进；?? 适合"没有就用默认值"的兜底；至于 !，新手期的答案是"不用"。等哪天你能说出"这里逻辑上绝对不可能为 nil"的完整理由，再考虑它也不迟。

另外，新一点的 Swift 支持 <code class="inline">if let n</code> 的简写——变量名和可选值同名时，连 <code class="inline">= nickname</code> 都能省。看到别人代码这么写别懵，就是第一式的省事版。

##### 可选链：一路问下去，断了也不崩

真实项目里，可选值经常一层套一层：用户资料里有个邮箱，邮箱可能没有；资料本身也可能没有。问这样的问题时，<code class="inline">?.</code> 就是一串多米诺：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 可选链</span><span class="dots">···</span>
:::

```
struct Profile {
    var email: String?
}

let profile: Profile? = Profile(email: nil)

// profile 可能没有，email 也可能没有——两道门都轻轻推一下：
let letters = profile?.email?.count ?? 0
print(letters)          // 0：任何一环断了，整条链安静地变成 nil
```
:::

任何一环是 nil，整条表达式就安静地变成 nil，不崩、不报错、不打扰。最后接一个 <code class="inline">??</code> 给兜底值，是最常见的收尾姿势。读别人代码时看到一串问号，就按"一路问下去，断了就走默认"来翻译。

##### nil 到底是什么

nil 不是 0，不是空字符串 <code class="inline">""</code>，也不是某些语言里的空指针——它就是"盒子空着"这个状态本身。把 nil 当成一个值得认真设计的正常值，而不是当成要到处躲的错误，是理解 Swift 的分水岭。反过来，普通类型（没有问号的）永远不会装着 nil：<code class="inline">[Int]</code> 数组里不可能混进一个"没有"，<code class="inline">Int</code> 变量不可能"消失"。确定性，就是这套机制卖给你的东西。

<strong>与 Kotlin 对照</strong>：Kotlin 的空安全与 Swift 的 Optional 几乎同构，符号对号入座——可空类型 <code class="inline">String?</code> 两边一样，安全调用 <code class="inline">?.</code> 两边一样，唯一的坑是默认值符号：Swift 用两个问号 <code class="inline">??</code>，Kotlin 用 Elvis <code class="inline">?:</code>。切语言时这里必手滑一次，先打个预防针。

##### 什么时候最容易撞上 nil

光讲机制容易飘，把这些年新手撞 nil 的高发地点列给你。对号入座，等你自己撞到时就不会慌：

- <strong>输入框的草稿</strong>：用户还没打字，内容就是 nil——第 62 章的 TextField 会天天见面；
- <strong>没填的备注</strong>：记一笔账，备注栏空着很正常——你未来的记账本里 <code class="inline">note: String?</code>；
- <strong>字典里查不到的键</strong>：拿"张三"去查价目表，表里没这个人——第六节讲字典时会展开；
- <strong>还没回来的网络结果</strong>：请求刚发出去，数据还在路上——第 64、66 章的老朋友。

看出规律了吗？nil 的本质是"结果还没定"或"东西天生可选"。反过来说，如果你发现代码里到处都是可选值，多半是设计出了问题——该有的字段没想清楚，才会一路 <code class="inline">??</code> 兜底。Optional 是工具，不是装饰，用得节制的设计才舒服。

##### 场景案例：给爸妈的记账本，备注栏怎么设计

把这个概念落到一个具体决定上。第 65 章会带你做记账本，现在先想其中一个字段：每笔账的"备注"。爸妈手写账本的习惯是有的记一笔、没的空着——所以备注天然就是"可能没有"。落到类型上就是一行：<code class="inline">var note: String?</code>。

写界面的那天你会庆幸这个决定：显示一笔账时，<code class="inline">record.note ?? "没写备注"</code>，一句兜底，空备注显示"没写备注"而不是空白一片；导出报表时，<code class="inline">if let n = record.note</code>，有备注的才进"备注列"。要是当初把 note 声明成普通 String，你就得用空字符串假装"没有"，然后满代码判断 <code class="inline">== ""</code>——能跑，但处处是暗号。类型选对了，代码自己就干净了。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：把 ?? 读成"不然就"

{class="mt-1"}
读代码时把 <code class="inline">nickname ?? "匿名用户"</code> 翻译成"昵称，不然就叫匿名用户"，整行代码立刻从符号变成人话。同理，<code class="inline">if let</code> 读成"如果有就……"，<code class="inline">guard let</code> 读成"必须得有，不然走人"。符号背不住的时候，回到人话翻译，这条捷径全程有效。
:::

##### Optional 的边界：什么时候别用可选值

学会了 Optional，新手容易走另一个极端——把所有属性都声明成可选，"以防万一"。这是个要主动纠正的习惯。可选值是有代价的：每个问号都在向读代码的人宣布"这里可能没有"，而你到处都要解包。正确的判断方式是从业务出发，问一句：<strong>这个字段真的可能没有吗？</strong>

拿爸妈的记账本举例：一笔账的金额会有"没有"吗？不会，金额是必须填的——那就老老实实声明成 <code class="inline">Double</code>，录入界面逼着填完才能保存。备注会空吗？会——那就 <code class="inline">String?</code>。类目呢？可以有默认值"餐饮"——那就非可选加默认值。把"必须有"的字段锁死成非可选，剩下极少数真正的可选项用问号标记，代码立刻清爽一半。记住这条顺序：<strong>先考虑非可选，再考虑默认值，最后才轮到可选值</strong>。

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

提前打声招呼，免得以后被吓到：Swift 语法主干很稳，但这几年苹果在并发安全上持续收紧——Swift 6 系列把"跨 actor 边界传递可变状态"从警告升级成了错误。以后从旧教程抄异步代码报出这类错，别慌：先想清楚这份数据归谁所有，再决定加 Sendable 约束还是改成不可变值。真卡在 actor / Task 上，Xcode 26 的 Swift 并发调试能跟踪任务跨线程的执行，能少猜很多。第 64 章用到 async/await 时咱们再细聊。

##### 参数标签：Swift 的"对话式"调用

注意上面调用时写的 <code class="inline">greet(name: "张三")</code>——调用函数要带参数名。这不是啰嗦，是 Swift 的招牌设计：调用处读起来像一个句子。再看你以后真会写到的例子：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 参数标签</span><span class="dots">···</span>
:::

```
func move(from start: Int, to end: Int) {
    print("把东西从 \(start) 号位搬到 \(end) 号位")
}
move(from: 1, to: 5)        // 读起来像英语句子：从 1 移到 5

// 不想带标签，用下划线省掉：
func add(_ a: Int, _ b: Int) -> Int {
    return a + b
}
print(add(3, 5))

// 参数可以带默认值，不传就用默认的：
func greet(_ name: String, punctuation: String = "！") -> String {
    return "你好，\(name)\(punctuation)"
}
print(greet("张三"))                      // 你好，张三！
print(greet("张三", punctuation: "？"))   // 你好，张三？
```
:::

from、to 这种标签在定义里是"外部名 + 内部名"合体：调用时用 from，函数体里用 start。想让某个参数不显示标签，就用下划线 <code class="inline">_</code> 占位。默认参数值则是省字神器——大部分调用都用默认值，个别场合再单独指定。

<strong>与 Kotlin 对照</strong>：Kotlin 调用时也支持带参数名（<code class="inline">greet(name = "张三")</code>），但那是可选项；Swift 默认强制，所有调用点整齐划一。另外 Kotlin 的默认参数和 Swift 的默认参数功能一样，写法上 Kotlin 用等号、Swift 直接赋值，一眼能对上。

##### 一次带回多个结果：元组

想让一个函数同时带回"最小值和最大值"，不必为它专门造一个类型——元组（Tuple）就是为此准备的临时口袋：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 元组</span><span class="dots">···</span>
:::

```
func minMax(of numbers: [Int]) -> (min: Int, max: Int)? {
    guard let first = numbers.first else { return nil }
    var lo = first
    var hi = first
    for n in numbers {
        lo = min(lo, n)
        hi = max(hi, n)
    }
    return (lo, hi)
}

if let result = minMax(of: [3, 1, 9, 7]) {
    print("最小 \(result.min)，最大 \(result.max)")
}
```
:::

返回类型写成 <code class="inline">(min: Int, max: Int)?</code>——注意那个问号：数组可能为空，这时候没有"最小最大"可言，返回 nil 才是诚实的做法。这也顺便复习了上一节：一个函数"可能给不出结果"，就用可选值来表达。元组适合临时组合几个值；要长期维护、多处使用的数据，还是老老实实写 struct。

##### 闭包的三张脸：完整、简写、尾随

读别人代码时，同一个闭包会以三种长相出现。看一遍它们的互变过程，以后就不会被任何一种写法吓住：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 闭包三张脸</span><span class="dots">···</span>
:::

```
let names = ["张三", "李四", "王五"]

// 第一张脸：完整写法，什么都写明
let r1 = names.map { (n: String) -> String in
    return "你好，\(n)"
}

// 第二张脸：类型能推断，return 也能省
let r2 = names.map { n in "你好，\(n)" }

// 第三张脸：参数都省了，用 $0 代表第一个参数
let r3 = names.map { "你好，\($0)" }

print(r3)   // ["你好，张三", "你好，李四", "你好，王五"]
```
:::

三张脸是同一段代码。日常写代码用第三张，读老代码认得第一张就够。Xcode 的补全和重构经常在三张脸之间帮你切换，别手动较劲。$0、$1、$2 依次代表第一、二、三个参数——超过三个参数的闭包，建议老老实实给参数起名字，不然三个月后连你自己都读不懂。

<strong>与 Kotlin 对照</strong>：Kotlin lambda 的 <code class="inline">it</code> 就是 Swift 的 <code class="inline">$0</code>；Kotlin 的尾随 lambda（最后一个参数拖到括号外面）和 Swift 的尾随闭包同构——<code class="inline">Button("点我") { ... }</code> 这种"括号后面跟大括号"的形状，两边读法一模一样。第 62 章的 SwiftUI 会让你天天写尾随闭包，现在练熟正合适。

##### 集合连招实战：把一沓账单算清楚

单看语法不过瘾，来一段真实感更强的：月底了，你有一组外卖账单，想筛出大额的、排个序、算个总账、再生成一句汇报——四个动作，四个连招：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 账单四连</span><span class="dots">···</span>
:::

```
let bills = [12.5, 88.0, 5.0, 200.0, 45.0]

let big = bills.filter { $0 > 50 }          // 筛：超过 50 的
// [88.0, 200.0]
let sorted = bills.sorted(by: >)            // 排：从大到小
// [200.0, 88.0, 45.0, 12.5, 5.0]
let total = bills.reduce(0, +)              // 合：全部加起来
// 350.5
let report = bills.map { "一笔 \($0) 元" }  // 变：变成一行行文字
// ["一笔 12.5 元", "一笔 88.0 元", ...]
```
:::

filter 筛选、sorted 排序、reduce 合并、map 变换——这四个名字值得刻进肌肉记忆。它们可以自由串联：<code class="inline">bills.filter { $0 > 50 }.reduce(0, +)</code> 一行算出"大额消费总额"。第 65 章的记账本项目里，每月汇总、分类统计全靠这几招组合，现在多练两遍，到时就是抄自己。

<strong>与 Kotlin 对照</strong>：这四个连招在 Kotlin 里名字几乎一致（filter / sortedBy / map），求和小有差异——Kotlin 有现成的 <code class="inline">sum()</code>，Swift 用 <code class="inline">reduce(0, +)</code> 达到同样效果。思想完全同源：把"对集合的批量操作"变成几个可拼接的标准件。

##### 函数命名与拆分：一个函数干一件事

函数名用动词开头：<code class="inline">loadBills()</code>、<code class="inline">saveRecord()</code>、<code class="inline">calculateTotal()</code>——读起来就是一个动作。比命名更要紧的是"一个函数只干一件事"：你写一个函数，如果描述它得用"然后"（"读取账单，然后排序，然后存起来"），那它其实该拆成三个函数。

拆分的时机有个朴素信号：同一段逻辑你复制粘贴到第二个地方时，就该把它提成函数了。复制一次是巧合，复制两次就是bug 的预订席位——改的时候忘改一处，数据就开始对不上账。函数短还有个隐性福利：报错信息说"第 X 行附近"，短函数一眼就定位，长函数得先考古。

<strong>与 Kotlin 对照</strong>：这套拆分哲学不分语言，Kotlin 侧的写法几乎一样（第 50 章的 <code class="inline">fun add(a: Int, b: Int) = a + b</code> 和 Swift 的单表达式函数也是一回事）。语言会换，"小函数、动词命名、复制即重构"这套手艺跟着你走。

##### 场景案例：把"帮妈妈算水电费"写成三个函数

把本节的知识装进一个生活场景。周日晚上，妈妈发来消息："帮我算算这个月水电，水费按吨算，电费分档。"别急着写一个大函数——先按"一件事"拆：算水费、算电费、汇总。三个函数，各管一段：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 水电费三件套</span><span class="dots">···</span>
:::

```
func waterFee(_ tons: Double) -> Double {
    return tons * 3.0            // 假设水价一吨 3 元
}

func electricFee(_ kwh: Double) -> Double {
    if kwh <= 200 {
        return kwh * 0.5         // 第一档
    } else {
        return 200 * 0.5 + (kwh - 200) * 0.8   // 第二档
    }
}

func report(waterTons: Double, kwh: Double) -> String {
    let water = waterFee(waterTons)
    let electric = electricFee(kwh)
    return "水费 \(water) 元，电费 \(electric) 元，合计 \(water + electric) 元"
}

print(report(waterTons: 12, kwh: 260))
// 水费 36.0 元，电费 148.0 元，合计 184.0 元
```
:::

这段不到二十行的小程序里，本节的零件全部到齐：电费分档那个 if 就是条件判断；三个函数各干一件事，参数标签让调用处读起来像人话；report 调用另外两个函数，是"函数调用函数"的第一次亮相。价值在后头：以后妈妈要改水价，你只动 waterFee 一行；要加燃气费，再写一个函数往 report 里加一项——拆分的好处，第一次上手就摸到了。

默认情况下，函数拿到的是参数的副本——你 在函数里改天换地，外面的原值纹丝不动（值类型尤其如此）。想让函数真的改外面的变量，用 <code class="inline">inout</code> 声明参数，调用时加 <code class="inline">&</code> 符号：

::: div .code-block
:::inline div .code-head
<span>SWIFT · inout</span><span class="dots">···</span>
:::

```
func doubleIt(_ x: inout Int) {
    x *= 2
}

var money = 50
doubleIt(&money)      // & 表示"我要让你改真的"
print(money)          // 100
```
:::

这个功能要节制使用：能返回新值就别 inout——<code class="inline">money = double(money)</code> 的写法更清楚，一眼看出数据往哪流。inout 的正经出场机会不多，遇到"必须原地改"的场合再请它。<strong>与 Kotlin 对照</strong>：Kotlin 没有 inout，靠返回新值表达同样意图；两边的共识是"数据流清晰优先于省一行代码"。

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
protocol Identifiable {   // 标准库协议：id 为泛型 Hashable
    var id: UUID { get }   // 这里以 UUID 为例的简化示意
}
struct Record: Identifiable { ... }   // 遵守协议 = 承诺实现其要求
```
:::

SwiftUI 里几乎一切都是 struct（View 就是协议）。这句现在不懂没关系，第 62 章会天天见面——<strong>在 Swift 的世界里，先拥抱 struct</strong>。

顺手更新一下知识地图：状态观察和持久化这两件事，新项目分别交给 <code class="inline">@Observable</code> 和 SwiftData（第 63、64 章展开）；老教程里的 ObservableObject / @Published 还会到处见到——会读就行，新代码不必跟着写。

##### 值类型与引用类型：复制还是共享

struct 和 class 最根本的差别，用一段十行代码就能看明白：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 值类型实验</span><span class="dots">···</span>
:::

```
struct Wallet {
    var cash: Double
}

var a = Wallet(cash: 100)
var b = a              // 赋值这一刻，复制了一份全新的
b.cash = 50            // 改的是 b 那一份
print(a.cash)          // 100——a 毫发无损
```
:::

struct 是值类型，赋值时复制一份，像发传单：一人一张，你涂坏你的，不影响别人。class 是引用类型，赋值时传的是"同一个东西的门牌号"，像共享在线文档：谁改一处，所有人可见。两种语义没有绝对好坏，但值类型天然少一类"我以为只改了自己这份"的 bug——这就是官方让 struct 当默认选项的原因。

<strong>与 Kotlin 对照</strong>：这是两门语言差异最大的地方。Kotlin 的 data class 本质仍是 class，引用语义；Swift 的 struct 是值类型。对照记忆：第 50 章的 <code class="inline">data class User</code> ↔ 本章的 <code class="inline">struct Record</code>，装数据的用法一致，但 Swift 这边多送一层"复制保险"。

##### 什么时候才轮到 class

别把"优先 struct"读成"class 没用"。三种情况还是要请出 class：一是需要继承，子类要沿用父类的代码；二是需要引用语义——比如一个"当前登录用户"，全 App 看的必须是同一份；三是要和系统里的老 API 打交道，UIKit 时代全家都是 class，历史惯性还在。新项目里，你亲手写的 class 大概只剩一种：<code class="inline">@Observable</code> 标注的视图模型——第 63 章正式登场，现在记住"它是个 class"就够了。

还有个容易忽略的小差别：struct 用 let 声明后，属性一个都改不了；class 用 let 声明，属性照样能改——因为 let 锁的是"门牌号别换"，房子里的家具还是可以搬动。这也是"let 优先"在 class 面前保护力打折的原因，改 class 的属性前多想一秒。

##### mutating：结构体改自己要打个招呼

::: div .code-block
:::inline div .code-head
<span>SWIFT · mutating</span><span class="dots">···</span>
:::

```
struct Counter {
    var count = 0

    mutating func plusOne() {   // 要改自己的属性，先声明 mutating
        count += 1
    }
}
var c = Counter()
c.plusOne()
print(c.count)      // 1
```
:::

值类型的方法想修改自己的属性，必须在 func 前加 <code class="inline">mutating</code>，不然编译器直接拦下。这个"打招呼"的仪式感很有价值：扫一眼代码，哪些方法会改状态一目了然。另外注意上面声明用的是 <code class="inline">var c</code>——let 声明的结构体连 mutating 方法都不让调，let 的封锁是全方位的。

<strong>与 Kotlin 对照</strong>：Kotlin 没有这层区分，data class 的属性只要声明成 var 就随处可改。Swift 把"谁能改、在哪改"写在更显眼的位置，代价是多个关键字，收益是状态变化一眼可见。

##### 协议：一纸能力清单

协议（protocol）回答的问题是"这个类型会什么"。它自己不干活，只列清单：有哪些属性、哪些方法。类型遵守协议，等于签合同——清单上的每一项都必须实现：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 协议与默认实现</span><span class="dots">···</span>
:::

```
protocol Payable {
    func monthlyCost() -> Double
}

extension Payable {
    // 协议扩展：给所有签合同的类型"批量发装备"
    func description() -> String {
        "月费用 \(monthlyCost()) 元"
    }
}

struct VipMember: Payable {
    func monthlyCost() -> Double { 25 }
}

let member = VipMember()
print(member.description())   // 月费用 25.0 元
```
:::

extension 里那段是协议扩展：给所有遵守者送一个现成的 <code class="inline">description()</code>，谁有特殊需求再自己重写。这个模式在 Swift 标准库里遍地都是——你之所以能对数组喊 <code class="inline">map</code>、对字符串喊 <code class="inline">count</code>，背后都是"标准库通过协议和扩展发的装备"。下一节咱们就把 extension 这个工具单独拆开看。

<strong>与 Kotlin 对照</strong>：protocol ↔ interface，两边思想一致，Kotlin 的接口同样能带默认实现。Swift 更激进一步：协议扩展能给任何遵守者批量加方法，"面向协议编程"在 Swift 圈是正经流派。第 62 章你会看到 SwiftUI 的 View 就是一个协议——界面框架用"签合同"的方式定义组件，这设计新手第一次见都会愣一下，但很快会习惯。

##### 计算属性：现算的，不用存

struct 里除了"存数据的属性"，还有一类"现算的属性"——长得像属性，每次访问都算一遍：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 计算属性</span><span class="dots">···</span>
:::

```
struct Order {
    var price: Double
    var count: Int

    var total: Double {        // 计算属性：不存值，现场算
        price * Double(count)
    }
}

let order = Order(price: 12.0, count: 3)
print(order.total)             // 36.0
// 改了 price，total 自动就是新值——因为它每次都现算
```
:::

判断该存还是该算，一条经验：<strong>能从别的属性推出来的，就别存</strong>。存一份"总价"，等于给数据开了两个户口，price 一改就闹分家。这和第 62 章 SwiftUI 里"派生值现算"的原则是同一条哲学，现在养成习惯，后面直接受益。

<strong>与 Kotlin 对照</strong>：Kotlin 的 <code class="inline">val total get() = price * count</code> 和 Swift 的计算属性一模一样，连"无存储、现访问现算"的语义都同步。

##### 成员逐一构造器：struct 送的开箱礼

注意上面创建 Order 时写的 <code class="inline">Order(price: 12.0, count: 3)</code>——你没写过任何构造器，它凭什么能这么建？这就是 struct 送的开箱礼："成员逐一构造器"，按属性的顺序和名字逐个填值。而 class 没有这份礼：每个属性得有默认值，或者你亲笔写一个 init。

<strong>与 Kotlin 对照</strong>：data class 的主构造器也得自己写（<code class="inline">data class User(val id: Int)</code>），写完才有逐字段构造。Swift 的 struct 更省事——属性列好，构造器自动到账。装数据的活儿，两边都顺手，但 Swift 这边连声明都省了。

##### 两个高频协议：Identifiable 与 Hashable

标准库的协议成百上千，新手期只需要提前认识两个，因为它们很快就会在你的项目里刷存在感。

一个是 <code class="inline">Identifiable</code>——"我有身份证"。遵守它只需要一个稳定唯一的 <code class="inline">id</code> 属性，常常用 <code class="inline">UUID()</code> 生成（就是本章开头代码里那个）。它的重要性在下一章：界面列表要靠 id 分清哪一行是哪一行，id 稳定，界面刷新才不串行。第四节的代码里 Record 已经在用它了。

另一个是 <code class="inline">Hashable</code>——"我能被算出一个指纹"。能放进 Set、能当字典的键，都要求这个能力。好消息是不用手写：struct 的属性都是可哈希的类型时，声明遵守一下，编译器自动帮你合成。<strong>与 Kotlin 对照</strong>：data class 自动获得 equals/hashCode，Swift 的自动合成是同一件事的另一种说法——"装数据的类型，比较相等这件事编译器代劳"。

#### 五、写给零基础的语法速查卡

下面这张卡是本章的"口袋地图"。它的正确用法是"写的时候查，不是看的时候背"——前四节的每一段代码，都能在卡里找到对应的那一行。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要做什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">写法</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定义常量/变量</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">let x = 1</code> / <code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">字符串插值</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">"你好，\(name)"</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定义函数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">func 名字(参数: 类型) -> 返回类型 { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">判断</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">if 条件 { ... } else { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">遍历</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">for x in 数组 { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">安全解包</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">if let x = 可选值 { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">默认值</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">x ?? 默认值</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定义结构体</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X { var a: Int; var b: String }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">闭包</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">{ $0 * 2 }</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Swift 语法速查卡（新手版）

这页卡不用硬背——Swift 每年小版本都会调整语法糖。遇到不认识的写法，先分辨它属于"语言特性"还是"框架 API"，再去对应的文档查。另外，Xcode 26 的预测式代码补全跑在本地、能用上更多代码上下文，是个好用的加速工具；但它不是判断工具——生成的内容要自己读懂再放进项目。

用卡也有个小技巧：先把卡上的九行抄一遍到 Playground 里，每行跑出结果后，故意改坏一处再看报错——"正确长什么样"和"错了长什么样"都见过，这行语法才算真的归你。改坏不用怕，Playground 里的错误没有成本。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：在 Playgrounds 里玩 15 分钟 Swift

{class="mt-1"}
有 Mac 就打开 Xcode → Playground；没 Mac 就用 iPad 上的 Swift Playgrounds 或网页版演练场。把本章每一段代码都跑一遍，改改数字和文字，故意制造几个错误看看 Xcode 怎么提示。这个"先玩后学"的 15 分钟，会让你第 62 章上手时轻松一倍。
:::

#### 六、集合三家：数组、字典与集合

单个变量装不下真实生活——一笔账是一个数，一个月的账是几百个数。Swift 的三大件正好对上三种收纳需求：数组像购物小票（有顺序、可重复），字典像价目表（拿名字查价钱），集合像去重后的名单（只问"在不在"）。

##### 数组：一队有编号的格子

::: div .code-block
:::inline div .code-head
<span>SWIFT · 数组</span><span class="dots">···</span>
:::

```
var scores = [90, 59, 82]
scores.append(100)        // 尾部加一个
scores.insert(75, at: 0)  // 插到最前面
scores[1] = 91            // 改第 1 格（从 0 数起）
scores.remove(at: 2)      // 删掉第 2 格
print(scores.count)       // 4 个
print(scores.isEmpty)     // false

// 空数组必须写明类型，不然编译器不知道以后装什么：
var todos: [String] = []
todos.append("买牛奶")
```
:::

两个纪律记一下。第一，下标从 0 开始——<code class="inline">scores[1]</code> 是第二个，新手期"差一位"的 bug 大半出在这。第二，下标越界会崩：数组只有 4 个元素，你取 <code class="inline">scores[10]</code>，程序当场停。安全起见，不确定长度时先用 <code class="inline">count</code> 问一声，或者用 <code class="inline">if let first = scores.first</code> 这种安全取法。

##### 字典：拿名字查价钱

::: div .code-block
:::inline div .code-head
<span>SWIFT · 字典</span><span class="dots">···</span>
:::

```
var prices = ["咖啡": 15.0, "面包": 8.0]
prices["蛋糕"] = 25.0      // 没有就新增
prices["咖啡"] = 12.0      // 有就覆盖

print(prices["蛋糕"])       // Optional(25.0)——注意！
print(prices["蛋糕"] ?? 0)  // 25.0
print(prices["披萨"] ?? 0)  // 0：查不到也不崩

for (name, price) in prices {
    print("\(name) 卖 \(price) 元")
}
```
:::

重点看中间那三行：用下标查字典，返回的是<strong>可选值</strong>——因为键可能根本不在表里。这正好呼应第二节：Optional 不是高级玩具，它就藏在字典这种日常操作里。不接住它，编译器会一直红给你看；接住它（<code class="inline">?? 0</code>），程序就稳了。另外提醒：字典的遍历顺序不保证和插入顺序一致，要顺序请自己 sort。

<strong>与 Kotlin 对照</strong>：这一点两边神同步——Kotlin 的 <code class="inline">map[key]</code> 同样返回可空的 <code class="inline">T?</code>。三家集合的对应关系也整齐：数组 <code class="inline">[Int]</code> ↔ <code class="inline">List&lt;Int&gt;</code>，字典 <code class="inline">[String: Int]</code> ↔ <code class="inline">Map&lt;String, Int&gt;</code>，集合 <code class="inline">Set</code> ↔ <code class="inline">Set</code>，连名字都懒得换。

##### 集合：只问"有没有"

::: div .code-block
:::inline div .code-head
<span>SWIFT · 集合</span><span class="dots">···</span>
:::

```
var visited: Set&lt;String&gt; = ["北京", "上海"]
visited.insert("广州")
visited.insert("广州")            // 重复的自动忽略
print(visited.count)              // 3
print(visited.contains("上海"))   // true
```
:::

什么时候用集合？判断"存在与否"多的场合——收藏夹去重、标签管理、已读名单。集合查"有没有"比数组快得多，数据一多差距明显。和数组一样，声明空集合时要写明类型。

##### 改集合的两条纪律

<strong>纪律一：遍历的时候别动它。</strong>一边 for-in 一边删元素，是在给程序埋雷——删着删着下标对不上，轻则漏处理，重则当场崩溃。正确姿势是"先想清楚要什么，再动手"：想删一批，用 filter 生成一个不含它们的新数组；想改一批，用 map 生成改好的新数组。"造新的"永远比"原地折腾"稳。

<strong>纪律二：let 的集合是全冻结的。</strong>let 声明的数组连 append 都不让调——这是值类型的规矩，let 锁住整个盒子。打算增删改的集合声明成 var，打算只读的集合声明成 let，这一步顺便又帮你执行了一遍"let 优先"：凡是能用 let 的集合，说明它的内容在设计上就不该变。

##### 实战：把一个月的账按类目汇总

数组、字典合体的真实用法——第 65 章记账本的"分类汇总"，核心就这几行：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 分类汇总</span><span class="dots">···</span>
:::

```
let records = [("餐饮", 25.5), ("交通", 6.0), ("餐饮", 12.0), ("娱乐", 45.0)]

var byCategory: [String: Double] = [:]
for (category, amount) in records {
    byCategory[category, default: 0] += amount
}
print(byCategory)
// ["餐饮": 37.5, "交通": 6.0, "娱乐": 45.0]
```
:::

那个 <code class="inline">default: 0</code> 是关键——第一次遇到某个类目时，先从 0 起步再加。看懂这几行，你就理解了"数据汇总"这类功能的一半灵魂，剩下的交给第 65 章的项目实战。

<strong>与 Kotlin 对照</strong>：Kotlin 里同样的活用 <code class="inline">groupBy</code> 一行搞定，Swift 没有现成的一行版，用上面的手写循环——这也是两门语言的普遍气质：Kotlin 标准库糖更多，Swift 更"白纸"。糖少不是坏事，手写过一遍的人，换到有糖的那边一看就懂。

##### 字符串也是集合

一个彩蛋：在 Swift 里，字符串本身就是个集合——装着一串"字符"的集合。所以集合的那些玩法，字符串全都通用：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 字符串即集合</span><span class="dots">···</span>
:::

```
let word = "记账"
print(word.count)                    // 2 个字符
for ch in word {
    print(ch)                        // 逐个字符打印
}
let upper = "hello".map { $0 }       // 集合操作照样能用
print(upper)
```
:::

这个设计的实用价值在中文场景特别明显：一个汉字按"字符"算就是一个，count 不会像某些语言那样被编码问题坑到。<strong>与 Kotlin 对照</strong>：Kotlin 的字符串同样可以按字符遍历（word.forEach { }），两边体验一致。

#### 七、枚举与 switch：把"所有情况"想全

先看一个反面教材：外卖订单的状态，新手爱用字符串存——<code class="inline">"配送中"</code>、<code class="inline">delivering</code>、手一抖写成 <code class="inline">deliverin</code>，编译器一声不吭，运行时逻辑就歪了。正确姿势是枚举（enum）：把合法的情况<strong>全部列出来</strong>，此外的写法编译器直接拒收。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 枚举与 switch</span><span class="dots">···</span>
:::

```
enum OrderStatus {
    case placed        // 已下单
    case cooking       // 商家制作中
    case delivering    // 配送中
    case done          // 已完成
}

let status: OrderStatus = .delivering

switch status {
case .placed:
    print("等待商家接单")
case .cooking:
    print("商家正在做")
case .delivering:
    print("骑手在路上")
case .done:
    print("订单完成")
}
// 少写任何一个 case，编译报错——穷尽检查
```
:::

注意两个细节：赋值时可以简写成 <code class="inline">.delivering</code>，编译器知道左边是什么类型；switch 必须穷尽所有情况，少一个 case 都编译不过——这条"强迫症"规则在你以后给枚举加新状态时是救命稻草：加了新 case，所有没接住它的 switch 会一起报错，一个都跑不掉。

##### 关联值：case 自带行李

Swift 枚举的杀手锏是关联值：每个 case 可以随身携带数据。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 关联值</span><span class="dots">···</span>
:::

```
enum Weather {
    case sunny              // 晴：没什么可带
    case rainy(Int)         // 雨：带上降水量
    case cloudy             // 阴
}

let today = Weather.rainy(15)

switch today {
case .sunny:
    print("记得防晒")
case .rainy(let mm):
    print("降水 \(mm) 毫米，出门带伞")
case .cloudy:
    print("多云，体感舒适")
}
```
:::

眼熟吗？第 66 章的天气 App 里，"加载中 / 成功 / 失败"三种界面状态就是同一个思路：成功这个 case 里装着天气数据，失败这个 case 里装着错误原因。枚举 + 关联值，就是为"有限的几种情况、各自带不同的东西"这种问题而生的。

##### 原始值：case 的"底牌"

和关联值是"装新东西"不同，原始值是给 case 预先配一个固定的对应值：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 原始值</span><span class="dots">···</span>
:::

```
enum Weekday: Int {
    case mon = 1, tue, wed, thu, fri, sat, sun
}
print(Weekday.fri.rawValue)    // 5，后面的自动递增

enum Direction: String {
    case up = "上", down = "下"
}
print(Direction.up.rawValue)   // 上
```
:::

什么时候用原始值？和外部世界"对暗号"的场合——存进数据库、和服务器通信、显示成文字。关联值和原始值不冲突，但一个 case 二选一，具体用法到项目里自然分清。

##### switch 的进阶：区间、多值与一句话匹配

::: div .code-block
:::inline div .code-head
<span>SWIFT · switch 进阶</span><span class="dots">···</span>
:::

```
let score = 85
switch score {
case 90...100:
    print("优秀")
case 60..<90:
    print("及格")
case 0..<60:
    print("补考预备")
default:
    print("分数不对劲")
}

// 多个值共用一个 case，用逗号隔开：
let letter = "a"
switch letter {
case "a", "e", "i", "o", "u":
    print("元音")
default:
    print("辅音")
}
```
:::

区间匹配（<code class="inline">90...100</code>）让"成绩分档"这种逻辑一行一档，比一串 if 干净得多。注意给整数打分时仍要写 default——编译器算不出"所有整数都被覆盖"，宁可多写一行兜底。另外，switch 的 case 里还能加条件做更细的匹配，那是后面的事，现在这两招已经够用。

<strong>与 Kotlin 对照</strong>：Kotlin 用 sealed class + when 组合实现同样的能力，连"穷尽检查"的思想都一致——只是 Swift 把它做进了语法：普通 switch 也强制穷尽，Kotlin 的 when 只在当表达式用时强制。区间匹配 when 一样能写（in 90..100）。另外 Swift 枚举更轻，大多数时候不用先写个 sealed class 再套一层。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-quote-left mr-2"></i>一句话记牢

{class="mt-1"}
字符串会拼错，枚举不会。让"可能的取值"列在代码里、由编译器看守，用户就少看到一半的诡异 bug。
:::

#### 八、错误处理：throws 与 try，错了怎么办

Optional 管"有没有"，错误处理管"过程中的失败"。经典场景：登录。密码太短、账号被锁、网络断了——每一种都是"这次注定失败"。Swift 的规矩：可能失败的函数，在类型上就声明出来（<code class="inline">throws</code>），调用方必须显式善后。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 错误处理</span><span class="dots">···</span>
:::

```
enum LoginError: Error {
    case wrongPassword     // 密码不合法
    case accountLocked     // 账号被锁
}

func login(name: String, password: String) throws -> String {
    guard password.count >= 6 else {
        throw LoginError.wrongPassword    // 抛出一个"事故"
    }
    return "欢迎回来，\(name)"
}

do {
    let message = try login(name: "张三", password: "123")
    print(message)
} catch LoginError.accountLocked {
    print("账号被锁了，请联系客服")
} catch {
    print("登录失败：\(error)")          // 兜底 catch
}
```
:::

三个关键词分工明确：<code class="inline">throws</code> 写在函数签名上，等于挂牌"我可能失败"；<code class="inline">throw</code> 是真出事时抛出具体原因；<code class="inline">try</code> 写在调用处，给读代码的人亮灯"这行可能炸"。do 块里放正常逻辑，catch 依次接住——最后那个不带类型的 catch 是兜底，必须写，少它编译不过。

错误类型用枚举来定义——现在你知道为什么了：错误的情况是有限的、可列全的，正好是枚举的主场。switch 能穷尽检查，catch 的匹配也一样思路。

##### try? 与 try!：两种偷懒，一种危险

::: div .code-block
:::inline div .code-head
<span>SWIFT · try 家族</span><span class="dots">···</span>
:::

```
// try?：失败就得到 nil，把错误降级成可选值
let message = try? login(name: "张三", password: "123456")
print(message ?? "登录没成")

// try!：失败就当场崩溃——新手期禁用
// let message2 = try! login(name: "张三", password: "123")
```
:::

try? 的哲学是"失败也正常，没有就没有"——比如读缓存文件，没有就当空的处理。try! 和 Optional 的 ! 一样是高危操作：它把错误硬生生变成崩溃。规则可以复用第二节那句：新手期不用 !，用 if let / ?? / try? 的世界太平得多。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>避坑提醒：别用空 catch 装没事

{class="mt-1"}
catch 块里什么都不写，等于把事故报告撕掉假装无事发生——之后界面空白、数据没存上，你对着一片正常运行的假象查半小时。哪怕暂时不知道怎么处理，也先 <code class="inline">print(error)</code> 留个证据，比吞掉强一百倍。
:::

<strong>与 Kotlin 对照</strong>：这里是两门语言哲学差异最大的地方。Kotlin 没有受检异常，try 是个表达式，异常可以不处理，靠运行时兜底；Swift 则在编译期就逼你表态——要么 catch，要么 try? 降级成可选值，要么明确写 try! 说不怕崩。学完两边你会各有体会：Swift 啰嗦，但"忘了处理"这类事故在编译期就被清零。

##### 一个错误的三种去向

写真实项目时，错误从产生到解决，通常只有三种合法去向。把它们想清楚，错误处理的架构感就有了：

- <strong>就地处理</strong>：当场 do-catch，重试一下、给个默认值，用户根本没感觉到出过事；
- <strong>降级吸收</strong>：用 try? 变成可选值——适合"失败也无所谓"的场合，比如读缓存；
- <strong>往上抛</strong>：函数自己也标 throws，把决定权交给调用方——一层层传上去，最后由界面接住。

第三种是新手最容易忽略的：不是每个函数都要亲自处理错误，"往上抛"也是正经处理。但抛到最后总得有人接——第 66 章的天气 App 里，那个"失败状态"界面就是错误的最终归宿：把技术性的报错，翻译成"网络不太顺，稍后再试"这样的人话。<strong>错误处理的终点，永远是用户能看懂的一句话。</strong>

#### 九、扩展与泛型：给现有类型"发装备"

扩展（extension）解决一个日常尴尬：系统自带的类型很好用，就差一个小功能。比如你想让金额直接显示成"￥25.5"，总不能到处手写格式化代码——给 Double 发件装备：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 扩展</span><span class="dots">···</span>
:::

```
extension Double {
    var yuan: String {
        "￥\(self)"
    }
}

extension Int {
    var squared: Int { self * self }
}

print(25.5.yuan)     // ￥25.5
print(7.squared)     // 49
```
:::

extension 里可以加计算属性（上面是）、加方法，还能让类型补签某个协议（前面 Payable 的默认实现就是这么送的）。两条规矩要守：<strong>不能加存储属性</strong>（不能给 Double 塞一个新变量进去），<strong>不要重写系统已有的方法</strong>（同名会制造谁也说不清的歧义）。扩展是"添置"，不是"改造"。

<strong>与 Kotlin 对照</strong>：Kotlin 的扩展函数 <code class="inline">fun Double.yuan(): String</code> 和 Swift 的 extension 几乎同构，都是"不动别人的源码，给它加方法"。这也是两门语言最让老程序员羡慕彼此的设计之一——你从哪边来，这个概念都能直接平移。

##### 泛型：先混个脸熟

你天天在用的 <code class="inline">map</code>、<code class="inline">filter</code> 其实都是泛型函数：数组里装 Int 也好、String 也好，它们都照常工作。泛型就是"类型也当参数传"——写一份逻辑，适配所有类型。现在不用写自己的泛型函数，能认出尖括号就行：<code class="inline">Array&lt;Int&gt;</code> 和 <code class="inline">[Int]</code> 是同一个东西的两种写法。等你在第 63、64 章看到大量尖括号，回想起这一小节，就知道那不过是"这个函数什么类型都能接"的意思。

#### 十、函数也是值：把逻辑传来传去

前面说"闭包是没名字的函数"，还有更彻底的一层：在 Swift 里，<strong>函数本身就是一种值</strong>——可以存进变量、当参数传、当返回值带回来。数字有 Int，文字有 String，逻辑就有自己的类型，写法像这样：<code class="inline">(Int, Int) -> Int</code>。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 函数当值用</span><span class="dots">···</span>
:::

```
// 把一段逻辑存进变量：类型是 (Int, Int) -> Int
let operation: (Int, Int) -> Int = { $0 + $1 }
print(operation(3, 5))          // 8

// 函数当参数传：把"怎么处理"交给调用的人
func apply(_ x: Int, _ f: (Int) -> Int) -> Int {
    f(x)
}
print(apply(10) { $0 * 2 })     // 20
print(apply(10) { $0 + 1 })     // 11——同一个 apply，不同的逻辑

// 函数当返回值带出：造一台"逻辑生成器"
func makeGreeter() -> (String) -> String {
    return { "你好，\($0)！" }
}
let greet = makeGreeter()
print(greet("张三"))            // 你好，张三！
```
:::

看懂这三段，你就理解了本章很多"魔法"的底层：map 接一个闭包，本质是"函数当参数传"；集合连招能自由组合，本质是"逻辑可以像积木一样搬来搬去"。以后你在 SwiftUI 里看到的按钮回调、列表的每一行长什么样，全是这个模式的变体。

什么时候自己写"函数当参数"？有个朴素信号：两个函数的主体逻辑一样、只有中间一小段不同——把不同的那小段抽成参数。上面 apply 就是这么来的：取值逻辑相同，加工方式交给你现场指定。这个重构手法在第 65 章的项目里会真实用到。

<strong>与 Kotlin 对照</strong>：函数类型写法几乎一字不差——Kotlin 的 <code class="inline">(Int, Int) -> Int</code> 和 Swift 同形；Kotlin 的函数同样是一等公民，能存能传能返回。两边连"尾随闭包"的调用形态都互相照着对方设计，切换成本接近零。

#### 十一、struct 还是 class：一张决策表

第四节的道理散在好几段里，这里收拢成一张决策表。以后拿不准用哪个，扫一眼这张表就能定：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">你要写的东西</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">选谁</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">一句话理由</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">装数据的模型（账单、用户资料）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">struct</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">复制语义，天然少一类共享 bug</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI 的界面组件</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">struct</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">框架规定，View 是协议，组件全是 struct</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跨页面共享的可变状态（登录态等）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">class + @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需要"所有人看同一份"，第 63 章展开</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需要继承复用代码的层级</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">class</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">struct 不能继承</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">和 UIKit 等老框架配合的对象</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">class</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">老框架的历史约定，跟着走</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
struct 与 class 决策表

读表有个好消息：前两行覆盖了新手期九成以上的场景，而答案都是 struct。也就是说，你短期内几乎不会主动写 class——直到第 63 章的 @Observable 登场。别把"写不出 class"当落后，这是现代 Swift 刻意引导的方向：数据不可变、组件可复制，状态集中到少数几个明确的对象里管。

顺带安一颗定心丸：有人担心"到处复制，性能会不会差"。标准库的数组、字典、字符串这类集合有写时复制之类的优化，日常使用感知不到；真到了性能敏感的场景，第 67 章的工具会告诉你瓶颈在哪。现在先按"默认 struct"写，思路对了再谈优化。

##### 纠结时的三个快问快答

<strong>问：我拿不准要不要共享，先选 struct 会后悔吗？</strong>答：基本不会。从 struct 换成 class 是局部改动；从 class 换回 struct，得排查所有共享它的地方，工程量大得多。方向错了也改得动，但别逆着便宜的方向走。

<strong>问：struct 能有方法吗？</strong>答：能，而且很正常——本章的 Counter、Order 里写的都是方法。struct 不是"只装数据"，它是"自带行为的数据"，方法、计算属性、协议，一样不缺。

<strong>问：SwiftUI 里为什么从没写过 class？</strong>答：因为框架替你规划好了：组件是 struct，状态归 @State 管，跨页面共享的状态归 @Observable 的 class 管（第 63 章）。你只要按分工摆位，不用自己造轮子。

#### 十二、Swift 与 Kotlin 对照速查：学过安卓省一半

这本书两头都教：第 50 章是 Kotlin，本章是 Swift。两门语言的思想同源——强类型、类型推断、空安全、函数式集合操作、声明式界面（第 51 章的 Compose ↔ 第 62 章的 SwiftUI）。把最常用的对照收进一张表，两边来回切的时候用得上：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要做的事</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Swift</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kotlin</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">只读 / 可变变量</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">let x = 1</code> / <code class="inline">var x = 1</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">val x = 1</code> / <code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">字符串插值</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">"你好，\(name)"</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">"你好，$name"</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定义函数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">func greet(name: String) -> String</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">fun greet(name: String): String</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多分支</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">switch（强制穷尽）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">when</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">装数据的类型</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">struct（值类型）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">data class（引用类型）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">能力约定</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">protocol</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">interface</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可空类型</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">String?</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">String?</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">空时给默认值</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">a ?? b</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">a ?: b</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">匿名函数参数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">{ $0 * 2 }</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">{ it * 2 }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">异步操作</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">async / await（第 64 章）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">suspend 协程（第 53 章）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">扩展系统类型</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">extension Double { }</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">fun Double.xxx( ) { }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">集合三家</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数组 / 字典 / Set</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List / Map / Set</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Swift ↔ Kotlin 对照速查

用这张表学第二门语言的方法：别从头再学一遍，拿着表按行平移。你已经会"filter 一组数据"这件事，切语言时只需查两格——这行的 Swift 怎么写、Kotlin 怎么写，十秒完成迁移。真正需要重新学的只有"两边不一样"的那几格（struct 的复制语义、throws 的强制善后），把注意力省下来砸在差异上，两周就能双修。

如果你是先读过第八篇的安卓同学，这张表等于半章白送：语法换壳，思想通用。反过来先学了 Swift 再去碰 Kotlin，也是同一批表格反着查。两边最大的三处"不同"再单独点名：数字不自动混算（Swift 更严）、struct 是值类型（Kotlin 的 data class 不是）、错误处理强制善后（Kotlin 不强制）。这三处恰恰是 Swift 被"吐槽较真"的地方，也恰恰是它少出事故的地方。

异步这条多说一句：Kotlin 的协程和 Swift 的 async/await 解决同一个问题——"等待的时候别把界面卡死"。第 64 章正式用到时你会发现，两边的心法都是"把回调地狱拉直成顺序代码"。另外本章第三节预告过，Swift 6 系列对并发数据安全的要求更严，第 68 章会讲 @MainActor 与 Task 的实践，到时一起收网。

版本口径也在这里交代：Kotlin 那边的基线是 2.x 与 K2 编译器（第 50 章说过）；Swift 这边，2026 年的基线是 Swift 6.2。语言主干多年稳定，你屏幕上显示的版本号大概率更新——照本章的写法学不会错，最新情况以官方发布为准。

#### 十三、Swift Playgrounds 练习路径：从 15 分钟到第一周

第五节的动手盒子只管"今晚 15 分钟"，这里给想走远一点的人排一张周计划。练习环境三条路，按手头设备挑：

- <strong>iPad 上的 Swift Playgrounds</strong>：免费，不用 Mac，触屏就能写——学生党和没有 Mac 的人首选；
- <strong>Mac 上的 Xcode Playground</strong>：第 60 章装好的 Xcode 里就有，文件 → 新建 Playground，和将来写 App 的环境无缝衔接；
- <strong>网页版演练场</strong>：搜"Swift 在线演练场"能找到若干网页版，随手就能跑，适合在公司电脑上偷偷练——具体选哪个以你搜到的口碑为准。

##### 第一周菜单：每天 15 分钟

1. 第 1 天：let/var、类型推断、字符串插值、print——把第一节代码全部跑一遍并改坏三处；
2. 第 2 天：Optional 四式（if let、guard let、??、可选链），故意对 nil 解包看报错长什么样；
3. 第 3 天：函数、参数标签、默认参数、元组——写一个"算饭钱 AA"的函数；
4. 第 4 天：闭包三张脸 + map/filter/sorted/reduce 四连招；
5. 第 5 天：数组、字典、集合 + 分类汇总那段代码抄熟；
6. 第 6 天：枚举 + switch + throws/try/catch——把登录例子改成"取钱"场景；
7. 第 7 天：综合——命令行版迷你记账器：一组账单算总额、按类目汇总、输出一段汇报文字。

##### 自检清单：这六件事能不能不看书写出来

- 声明一个只读数组，筛选出偶数并打印；
- 对一个可选值用 if let 解包，nil 时打印默认提示；
- 用 filter + reduce 算出一组账单里大额消费的总和；
- 定义一个带关联值的枚举，switch 处理每种情况；
- 定义一个装"学生成绩"的 struct，创建两三个实例；
- 写一个 throws 函数，调用处用 do-catch 接住。

六条全过，本章就算毕业；卡在哪条，就回到对应小节再玩十分钟。别小看这份清单——它就是第 65 章项目里最常用的六个动作，现在练的是两个月后的自己。

##### 练习期的三个小坑，提前绕开

<strong>坑一：只看不敲。</strong>Playground 里的代码看着都懂，自己从空文件敲就处处卡壳——这太正常了，"看懂"和"写出"隔着一条肌肉记忆的河。对策很土：所有示例代码亲手敲一遍，包括你觉得最简单的那段。

<strong>坑二：一上来就抄大项目。</strong>GitHub 上有些开源 App 几万行，新手抄它等于用《新华字典》学认字——不是字典不好，是页码不对。按上面的周计划走，第七天那个三十行的迷你记账助手就是你的"合理难度"。

<strong>坑三：报错就问 AI 不读报错。</strong>编程智能能给出答案，但直接给答案会跳过"读报错"这项核心技能的练习。顺序应该是：自己读三十秒，有思路就试；没思路再问，问完把报错和原因的对应关系记下来——这笔账记多了，你就成了别人问的对象。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：让编程智能当陪练，别让它代笔

{class="mt-1"}
Xcode 26 的编程智能能陪你练：把本章代码贴给它，让它"故意改坏一处，我来找茬"，或者让它出题你答题。没装 Xcode 的同学，用通用 AI 聊天工具当陪练也行。但有一条纪律：练习阶段的代码必须自己敲——让 AI 代笔，等于花钱请人替你跑步。
:::

#### 十四、综合演练：Playground 里的迷你记账助手

知识点看十遍，不如连起来写一遍。现在把本章的大件全部装进一个约三十行的小程序——以后第 65 章的记账本，界面部分就是给这段逻辑套上壳。分四步搭，每步都能在 Playground 里立刻看到输出。

第一步，定义"一笔账"长什么样（struct + 枚举 + 原始值）：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 迷你记账助手 · 第一步</span><span class="dots">···</span>
:::

```
enum Category: String {
    case food = "餐饮"
    case transport = "交通"
    case play = "娱乐"
}

struct Expense {
    let name: String
    let amount: Double
    let category: Category
}

let expenses = [
    Expense(name: "午饭", amount: 25.5, category: .food),
    Expense(name: "地铁", amount: 6.0, category: .transport),
    Expense(name: "电影", amount: 45.0, category: .play),
    Expense(name: "咖啡", amount: 18.0, category: .food),
]
```
:::

第二步，写统计函数（默认参数 + filter + reduce）：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 迷你记账助手 · 第二步</span><span class="dots">···</span>
:::

```
func total(of list: [Expense], in category: Category? = nil) -> Double {
    list
        .filter { category == nil || $0.category == category }
        .reduce(0) { $0 + $1.amount }
}

print("本月总计：\(total(of: expenses).yuan)")
print("餐饮小计：\(total(of: expenses, in: .food).yuan)")
```
:::

第三步，找最大的一笔（可选值 + 解包）：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 迷你记账助手 · 第三步</span><span class="dots">···</span>
:::

```
let biggest = expenses.max(by: { $0.amount < $1.amount })
if let biggest = biggest {
    print("最大一笔：\(biggest.name)，\(biggest.amount.yuan)")
}
// 最大一笔：电影，￥45.0
```
:::

第四步，生成汇报文字（map + 多行字符串）：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 迷你记账助手 · 第四步</span><span class="dots">···</span>
:::

```
func report(_ list: [Expense]) -> String {
    let lines = list.map { "\($0.name)：\($0.amount.yuan)" }
    return "共 \(list.count) 笔\n" + lines.joined(separator: "\n")
}
print(report(expenses))
```
:::

对账一下，这段小程序用到了本章的哪些件：struct 定义模型、enum 划分类目、数组存列表、字典和 reduce 做汇总、Optional 表达"可能没有的筛选条件"、if let 解包、默认参数省事、闭包在 filter 和 map 里到处跑、扩展的 yuan 给金额穿上衣服。三十行不到，本章前面各节的骨架全在。把它亲手敲一遍，卡壳的地方就是你的复习清单。

还想多走一步的话，给自己留两个挑战：把汇总改成用字典按类目分组（第六节的套路）；给 total 函数加一个"只算某个日期之后"的条件（提示：给 Expense 加个日期属性，filter 里多判一条）。这两个挑战，恰好是第 65 章项目的真实需求预告。

#### 十五、读报错入门：新手前两周的五类红字

学语言阶段，报错比成功更常见——这不是安慰，是统计事实。既然躲不掉，不如学会读。下面五类红字覆盖了前两周绝大多数遭遇，认特征就行，具体措辞随版本会变。

<strong>第一类：类型不匹配。</strong>报错里出现"expected ... found ..."或者"cannot convert"字样，意思是"这里要的是 A，你给的是 B"。典型现场：把 Double 塞给了要 Int 的参数、忘了转换数字类型。修法：顺着报错把两边的类型都对一遍，缺转换就补转换。

<strong>第二类：可选值没解包。</strong>关键词是 optional、unwrapped。这是 Swift 特有的善意提醒："你还没开盒子就要拿东西"。修法：if let 解包、?. 安全调用，或者 ?? 给默认值——三个手法本章第二节全教过。

<strong>第三类：括号没配平。</strong>报错像"expected '}'"或者指向一行看起来完全无辜的代码。真相往往在更早的地方：某个大括号或小括号忘了关，编译器从那里开始全线错乱。修法：Xcode 会把配对的括号高亮，从报错行往前扫，把没关的那对找出来。缩进规整的人很少遇到这类问题——格式化快捷键（⌃I）顺手按。

<strong>第四类：名字不存在。</strong>关键词是"cannot find ... in scope"。十有八九是拼写错误——colorScheme 写成 colorscheme，编译器立刻翻脸；剩下的一成是作用域问题：你想用的东西声明在别的函数里，这里看不见。修法：先查拼写，再查声明位置。

<strong>第五类：运行时崩溃。</strong>编译能过、一跑就炸，控制台红字里常见"index out of range"（数组越界）或"unexpectedly found nil"（对 nil 强制解包）。这类编译器拦不住，是值类型规则里的"现场执法"。修法：越界的先检查 count 再取下标，nil 的回头找哪个可选值没接住——按调用顺序打 print 定位，几分钟就能锁定。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：读报错的三步固定动作

{class="mt-1"}
第一步，只读第一条报错——后面的多半是连锁反应；第二步，双击跳到出事行，看那一行和它上一行；第三步，看不懂就把报错原文复制去搜——英文原文是检索关键词，比转述强十倍。三步走完还没头绪，就去第 60 章第十一节的门诊表对号入座，那里专治环境类报错，和本节的语言类报错正好互补。
:::

#### 十六、新手 FAQ：关于 Swift 的十一个问题

<strong>问：let 和 var 全用 var 行不行？反正都能跑。</strong><br>答：能跑，但你等于主动关掉了编译器的一层保护。变的东西多了，"值什么时候被谁改了"这类问题会成倍增加。let 优先是白捡的保险，别拒收。

<strong>问：为什么我的 5 + 3.14 会报错？别的语言都行。</strong><br>答：Swift 不自动混算整数和小数，必须先转换：<code class="inline">Double(5) + 3.14</code>。这是故意的——混算是精度事故的重灾区，Swift 把入口焊死了。

<strong>问：if let 解包出来的变量，为什么出了大括号就不能用？</strong><br>答：因为大括号里是"确认过有值"的世界，外面没有这个保证。想全程都有值，用 guard let 提前拦截，或者调整设计让这个值根本不该是可选的。

<strong>问：字典取值为什么返回 Optional？太麻烦了。</strong><br>答：因为"查不到"是真实存在的结果，不是异常。返回可选值是把这份真实写进类型——习惯了你会发现，它替你挡住的是"以为查到了"这种最阴的 bug。

<strong>问：struct 和 class 怎么选，有没有口诀？</strong><br>答：有——默认 struct；要"所有人共享同一份可变状态"才用 class（配 @Observable，第 63 章）；和 UIKit 老框架打交道跟着它用 class。第十节的决策表收着完整版。

<strong>问：需要先把这章背熟才能进第 62 章吗？</strong><br>答：不需要。SwiftUI 阶段会反复用到本章的内容，用一周等于复习三十遍。带着"大概知道有这个东西"的印象往前走，回头查这张速查卡就行。

<strong>问：网上教程的写法和书上不一样，是谁错了？</strong><br>答：多半都没错——Swift 多年演进下来，同一个功能常有新旧两种写法。分辨办法：语言特性看官方文档的当前版本，框架用法认准新项目主流。遇到旧写法别慌，能看懂就行，新代码跟着本章的写法走。

<strong>问：学完这章我能做什么？</strong><br>答：能在 Playground 里写出一段完整的小逻辑（算账、分类、汇总），能看懂大多数 Swift 代码的结构。下一章 SwiftUI 一开，这些零件立刻开始拼成真正的界面。

<strong>问：Swift 是编译型语言吗？跑得快吗？</strong><br>答：是编译型——代码先由编译器翻译成机器指令再运行，性能属于第一梯队。对使用者的日常影响有两点：一是改完代码要点一下编译才能看到结果（第 60 章的画布预览缓解了这件事）；二是很多错误在编译阶段就被拦下，运行时崩的次数比脚本语言少得多。

<strong>问：不装 Xcode，光靠 iPad 或网页能学完这章吗？</strong><br>答：能，本章全部代码都不依赖 Xcode——iPad 的 Swift Playgrounds 和网页演练场都跑得动。但到第 62 章写界面，还是得回到 Mac 和 Xcode。语言阶段用 iPad 起步完全没问题，很多人就是这么入的门。

<strong>问：代码能跑就行，为什么你们总强调"写得规范"？</strong><br>答：因为代码是写给人看的，顺带让机器执行。不规范的名字和结构，编译器不在乎，但和你协作的人在乎，三个月后的你更在乎。规范不是洁癖，是给未来的自己递台阶。

#### 十七、误区清单：六个"想当然"

<strong>误区一：以为"全都用 var 更灵活"是好事。</strong>其实灵活和失控是同一个东西的两面。可变面越小，程序越容易推理——这条在 Kotlin、Swift、ArkTS 三边都成立，是声明式时代的通用审美。

<strong>误区二：以为 Optional 是"要到处防的麻烦"。</strong>恰恰相反，它是"把麻烦标出来"的机制：没标问号的地方保证有值，标了问号的地方逼你表态。真正麻烦的是那些"有时候有有时候没有，但类型上看不出来"的语言——你大概率还没在那边摔过跤。

<strong>误区三：以为 struct 是"穷人版 class"。</strong>现代 Swift 正好相反：SwiftUI 的组件全是 struct，装数据的模型首选 struct，class 只在共享状态和继承时出场。谁主流谁配角，别按 C++ 时代的直觉排座次。

<strong>误区四：以为错误处理就是 try! 或者干脆不写。</strong>try! 把"可能失败"变成"一定崩"，空 catch 把事故报告撕掉。这两个动作省下的三秒钟，日后都要用数倍的排查时间来还。

<strong>误区五：以为必须把全部语法学完才能动手。</strong>本章开头那句话值得再读一遍：20% 的语法干 80% 的活。集合、闭包、Optional、struct——这四样在手，你已经能读懂真实项目的大部分代码了。剩下的，第 62 章界面、第 64 章数据，用到哪个学哪个。

<strong>误区六：以为"会一门语言"就等于"会做 App"。</strong>语言只是第一张拼图——界面（第 62、63 章）、数据（第 64 章）、调试与发布（第 67 章）都是独立的技能块。把本章学扎实是对的，但别在 Playground 里原地踏步半年，拼图要一块块往上拼。

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- let 优先，var 慎用；类型自动推断，冒号后显式声明也行
- 可选值是 Swift 的灵魂：可能为空必须处理，if let / ?? 是护身符，! 是高危操作
- 函数调用要带参数名；闭包 = 没名字的函数，SwiftUI 里无处不在
- 优先 struct，遵守协议（Protocol）；SwiftUI 几乎一切都是 struct
- 20% 语法干 80% 的活：先会用，再精通
:::
