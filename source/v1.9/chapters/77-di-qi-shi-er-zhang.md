---
id: di-qi-shi-er-zhang
num: 72
nav: 第七十二章：ArkTS 语言速成
toc: default
kind: chapter
after_part: hongmeng-kai-fa-pian
---

### 第七十二章：ArkTS 语言速成——从 TypeScript 到鸿蒙

{class="chapter-intro mb-4"}
ArkTS = TypeScript + 鸿蒙应用框架约束。所以这一章的学法很明确：会 TS/JS 的你，重点看"鸿蒙收紧了什么、加了什么"；不会的也没关系，跟着 Kotlin/Swift 的类比走。上一章那个 @State 你已经见过了，这一章把语言层补齐。

开始之前给一个学习策略上的建议：ArkTS 的语言部分（本章）和 UI 部分（第 73 章）是两块独立的拼图，学的时候不要混。本章你只管把语言规则练熟，类型怎么标、装饰器是什么、哪些 JS 习惯要戒掉；UI 怎么写是下一章的事。分开学的好处是：报错时你能立刻判断"这是语言问题还是 UI 问题"，排查方向完全不同。

::: div .quick-read
##### 本章速读（5 分钟版）
这一章把语言层补齐：ArkTS = TypeScript + 鸿蒙应用框架约束。会 TS/JS 的你，重点看"收紧了什么、加了什么"；完全没写过的人，跟着 Kotlin/Swift 的类比走也行。语言（本章）和界面（下一章）分开学，报错时你才能一眼分清"这是语言问题还是 UI 问题"。
最关键的有三件事。第一，<strong>直接上手的部分</strong>：interface、class、泛型、箭头函数、模板字符串。解构，全是 TS 原味保留，你的旧经验大部分都在，Kotlin、Swift 老手也能逐行对上。第二，<strong>六条收紧是本章的骨头</strong>：禁 any/unknown（连 @ts-ignore 一起禁）；对象的形状不能在运行时加减属性；不用结构化类型（两个接口字段相同也不算同一类型）；UI 渲染只认可观察类型（普通 object 改了界面不动）；类型写全别依赖推断（没有返回值也要写 : void）；对象字面量和数组先定义 interface/class 再实例化。这些限制不是 bug 是特性：换来更小的包体、更快的启动、更稳的渲染。第三，<strong>鸿蒙加的料是装饰器</strong>：@Entry 标页面入口、@Component 标自定义组件、@State 标组件内部状态（一变界面自动刷新）、@Prop 父传子、@Link 父子双向，下一章的界面全靠它们驱动；状态管理先学 V1，新项目再考虑 V2。
今天就能做的最小动作：把上一章那个 TodoStore 搬进 DevEco，故意删掉一个返回类型、故意写一次 any，看看 arkts-no-xxx 报错码长什么样，再照提示改回来：主动犯一次错，比被动撞十次记得牢。
最大的坑是拿 JS 老习惯硬闯。obj.newField 随手加属性、obj['name'] 字符串下标取值、给 catch 参数标类型、把 function 表达式赋给变量——全都会撞上 arkts-no-xxx 报错码。还有拿对象字面量当类型（要改 interface 或 class）。以及以为 async/await 就不会卡界面（纯计算的重活照样卡，得走 Worker/TaskPool）。撞上报错码别硬绕：复制它去官方《从 TypeScript 到 ArkTS 适配规则》页面搜，每条规则都配着"为什么禁止"和"怎么改"的成对示例。心态一句话：把 ArkTS 当"更严格的 TypeScript"来学，报错是编译器在替未来的你省排查时间。本章还备了数组、Map、Set 的速查、异步 async/await、模块化与错误处理几节，写代码卡住时当字典翻；最后的十二道自测题，帮你看清到底学没学会。实在解决不了的报错，把报错码、最小复现代码、期望和实际行为这"三件套"贴全再问人。
##### 速查表
- 一句话定位：ArkTS 是"更严格的 TypeScript"，报错多不是你菜，是编译器提前说
- 六条收紧：禁 any、形状固定、无结构化类型、渲染类型受限、类型写全、字面量先有类型
- 报错三步：Problems 面板复制报错码 → 官方适配规则页搜 → 照错误/正确示例改
- 装饰器骨架：@Entry 入口、@Component 组件、@State 状态、@Prop 父传子、@Link 双向
- 状态管理：先学 V1（@State/@Prop/@Link），新项目再迁 V2（@Local/@Param/@Event）
- 对象当字典：字段固定用 interface，键动态用 Record 或 Map，别硬用字符串下标
- 数组两纪律：空数组先标类型再 push；sort 永远写比较函数
- async 不等于不卡界面：解析大 JSON 这类纯计算重活要走 Worker/TaskPool
:::

#### 一、你会 TS/JS：直接上手的部分

ArkTS 保留了 TypeScript 的核心语法：类型标注、接口。类、泛型、箭头函数、模板字符串、解构。来一段热身：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 基础语法</span><span class="dots">···</span>
:::

```
interface Todo {
  id: number
  title: string
  done: boolean
}

class TodoStore {
  private items: Todo[] = []

  add(title: string): Todo {
    let todo: Todo = { id: Date.now(), title: title, done: false }
    this.items.push(todo)
    return todo
  }

  get count(): number {
    return this.items.length
  }
}

let store = new TodoStore()
store.add('学 ArkTS')
```
:::

interface、class、private、泛型箭头函数——全是 TS 味道。Kotlin 和 Swift 的老手也能逐行对上：data class ≈ interface + 不可变对象，属性访问器 ≈ get count()。

这段代码里有三个"可以直接带走"的细节。第一，Todo 接口定义了数据的形状，后面的 UI（第 73 章）会直接以这种 interface 为渲染单元的类型基础，先把形状定清楚，UI 层就稳。第二，TodoStore 用 class 封装了"数据 + 操作"，这是 ArkTS 里推荐的"模型层"写法——状态和逻辑放类里，UI 只负责展示，和第 57 章讲的 MVVM 是同一个分层思路。第三，add 方法显式标注了参数和返回类型——ArkTS 里这不是可选项，下一节会讲为什么。

如果你完全没写过 TS/JS，这段代码的类比路线：Kotlin 老手看 interface 和 class 就是平时写的样子，类型标在冒号后面而不是前面；Swift 老手注意属性声明不用 var/let 区分可变性（ArkTS 用 readonly 表达不可变）；前端老手最需要注意的反而最少，你熟悉的一切语法都在，只是"更严格了"。三条路线殊途同归：本章结束时你能用 ArkTS 写出结构清晰的数据模型。

#### 二、ArkTS 收紧了什么：从"动态"到"静态"

JS 的灵活性是把双刃剑，ArkUI 渲染引擎为了性能把它收紧了。六条最常见的约束：

- <strong>禁用 any/unknown</strong>：每个变量都要有明确类型，@ts-ignore 也被禁用。
- <strong>对象的形状不能运行时改变</strong>：不能给对象动态加减属性：这直接影响 UI 刷新（框架靠固定结构做高效比对）。
- <strong>不用结构化类型</strong>：两个接口字段相同也不算同一类型，用 class 显式声明。
- <strong>UI 渲染数据类型受限</strong>：ArkUI 只支持 boolean/string/number 及其数组、class 实例等可观察类型，普通 object 不会触发刷新。
- <strong>类型要写全，别依赖推断</strong>：函数返回类型（没有返回值也要写 <code class="inline">: void</code>）、回调参数类型都要显式标注：报错里常见 <code class="inline">arkts-no-implicit-return-types</code> 这类提示；把类型写全，编辑器补全也更准。
- <strong>对象字面量与数组要有类型</strong>：别写"裸对象"和"无类型数组"，先定义 interface / class 再实例化。

这六条里，新手最常撞墙的是第二条和第四条。第二条的场景：你习惯了 JS 里 obj.newField = value 的随手加属性，在 ArkTS 里会直接报错：解法是把字段预先声明在 interface/class 里，哪怕初始值是空的。第四条的场景：你把一个普通 object 塞进 @State，改了它的属性界面却不动：因为 ArkUI 的观察机制只覆盖"可观察类型"。两者的共同解法都是"先定义类型，再创建对象"，这正是 ArkTS 的核心纪律。

每个约束都配有对应的报错码（arkts-no-xxx 格式），看到这类报错时，直接把报错码粘到官方文档的"从 TypeScript 到 ArkTS 适配规则"页面搜，每条规则都有"为什么禁止"和"怎么改"的成对说明。别硬绕：这些限制不是 bug，是特性。

这些约束换来的是：更小的包体、更快的启动、更稳定的渲染性能，和 Swift 逐年收紧动态特性的思路如出一辙。心态上也换个姿势：把 ArkTS 当「更严格的 TypeScript」来学，比当「换个语法的 JavaScript」顺畅得多；报错多不是你写错了，是编译器把以前藏着的问题提前说了。

#### 三、鸿蒙加的料：装饰器驱动 UI

ArkTS 对语言的最大扩展是<strong>装饰器体系</strong>，它们是 ArkUI 状态管理的骨架：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">装饰器</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">作用</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">一句话类比</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Entry</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">标记页面入口</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">安卓的 Activity / iOS 的 Scene</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Component</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">标记自定义组件</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Compose 的 @Composable</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">组件内部状态，变了刷新 UI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI 的 @State</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Prop / @Link</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">父传子 / 父子双向</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Prop vs @Binding</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Watch</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">状态变化回调</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">属性观察器</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Observed/@ObjectLink</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">嵌套对象观察</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">嵌套 class 的深度监听</td></tr>
</tbody>
</table>
```
:::

装饰器的本质是"给类和属性贴标签"，框架在编译期读取这些标签，生成对应的观察与刷新逻辑。你不需要理解装饰器的实现原理（那是框架的事），只需要记住每个标签的"契约"：@State 说"我变了你就刷新"，@Prop 说"父组件给我值但我不回写"，@Link 说"我们双向同步"。第 73 章的 ArkUI 会把这些契约放进真实界面里反复练习。

本节的表格还有个 V1/V2 的背景要说清楚：上表是 V1 状态管理（成熟稳定），鸿蒙后来推出了 V2（@Local、@Param、@Event 等新装饰器），两者可以在一个应用里共存但推荐新项目用 V2。学习顺序建议：先学 V1（资料多、概念全），再按第 79 章的进阶内容迁移 V2，就像先学 Swift 再追新特性一样。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：把 TodoStore 搬进 DevEco

{class="mt-1"}
1\. 在上一章的项目里新建 ets 文件夹下的 model/TodoStore.ets，把热身代码粘进去；2. 故意把一个返回类型删掉，看编译器报什么错；3. 故意用 any，看 arkts 报错码长什么样；4. 恢复代码，确认编译通过。报错不是失败——这是你和编译器建立信任的过程。
:::

#### 四、常用语法速查：数组、Map、Set 在 ArkTS 里怎么用

集合是写任何应用都绕不开的东西。ArkTS 里常用的集合就三种：数组、Map、Set，用法和 JS 大同小异，区别在"类型必须写清楚"这一条上。这一节当成速查手册用，写代码时卡住了就翻回来。

##### 数组：最常用，也最容易踩类型坑

数组要带上元素类型，<code class="inline">string[]</code> 和 <code class="inline">Array&lt;string&gt;</code> 两种写法等价，团队里挑一种用到底就行。常用的增删改查方法都在：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 数组常用操作</span><span class="dots">···</span>
:::

```
let names: string[] = ['阿黄', '小美', '老王']
names.push('大鹏')                    // 尾部加一个
names = names.filter(n => n !== '老王')   // 过滤，返回新数组
let found = names.find(n => n.startsWith('小'))  // 找第一个匹配的
let hasMei: boolean = names.includes('小美')      // 是否存在

let lengths: number[] = names.map(n => n.length)  // 一对一变换

let scores: number[] = [88, 92, 75]
scores.sort((a: number, b: number) => a - b)      // 从小到大
```
:::

几个值得说的点。filter、map、find 这些高阶方法的回调参数不用手写类型，因为数组元素类型已经确定了，编译器推得出来。sort 永远给比较函数，JS 里不传比较函数的 sort 会把数字当字符串排（[9, 10] 会排成 [10, 9]），这个默认行为到了 ArkTS 也别赌，比较函数永远写上，一行代码省半天排查。

新手最常见的数组错误是"不带类型的空数组"和"往里混着塞"。看一组错误示范和纠正：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 数组的错误示范与纠正</span><span class="dots">···</span>
:::

```
// 错误示范一：空数组不标类型
let list = []              // 编译器不知道这是什么的数组
list.push('购物')          // 报错

// 错误示范二：一个数组混装几种东西
let mixed: string[] = []
mixed.push('购物')
mixed.push(123)            // 报错：number 塞不进 string[]

// 纠正：先定形状，再往里放
interface TodoItem {
  title: string
  done: boolean
}
let list: TodoItem[] = []
list.push({ title: '购物', done: false })   // 字面量有类型可归，合法
```
:::

注意最后那行：对象字面量不是不能写。对象字面量是必须"有类型可归"。声明了 <code class="inline">TodoItem[]</code>，push 一个长得符合 TodoItem 的字面量就合法；什么都不声明就写字面量，编译器没法替你担保，就报错。这套逻辑贯穿 ArkTS 全部语法，记住它，一半的报错你都能自己看懂。

##### Map：键值对，查得快

键值对用 Map，两个类型都要标全。存电话簿、按 id 找对象、做缓存，都是它的主场：

::: div .code-block
:::inline div .code-head
<span>ARKTS · Map 常用操作</span><span class="dots">···</span>
:::

```
let ages: Map&lt;string, number&gt; = new Map()
ages.set('阿黄', 3)                 // 存
ages.set('小美', 5)

let a = ages.get('阿黄')            // 取，取不到时是 undefined
if (a !== undefined) {
  console.info('阿黄 ' + a + ' 岁')
}

console.info('' + ages.has('老王'))   // 有没有这个键
ages.delete('小美')                 // 删
console.info('' + ages.size)        // 几条

ages.forEach((age: number, name: string) => {
  console.info(name + ': ' + age)   // 遍历
})
```
:::

两个习惯要养好。第一，get 之前想清楚"取不到怎么办"：取不到时拿到的是 undefined，直接拿去算数就会出运行时错误，用 if 判断一下再往下走。第二，键的类型要稳定，别一会儿存字符串一会儿存数字，Map 没那么聪明，乱塞早晚会还债。

##### Set：自动去重的名单

Set 只回答一个问题："这个东西在不在？"加过多少遍都算一遍，天然去重：

::: div .code-block
:::inline div .code-head
<span>ARKTS · Set 常用操作</span><span class="dots">···</span>
:::

```
let seen: Set&lt;string&gt; = new Set()
seen.add('点赞')
seen.add('点赞')            // 重复加，没用，还是一条
console.info('' + seen.has('点赞'))   // true
seen.delete('点赞')
console.info('' + seen.size)          // 0
```
:::

三种集合怎么选，有个顺口溜：要顺序、要排序、要列表渲染，用数组；要按键快速找，用 Map；只关心"有没有"和去重，用 Set。还有一句要交代：列表数据基本都用数组承载，因为它是 ArkUI 的可观察类型之一；Map 和 Set 更多用在逻辑层做缓存、索引、去重。它们要不要进状态管理、怎么进，以第 73 章和官方文档为准。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2" aria-hidden="true"></i>小贴士

{class="mt-1"}
弱引用容器这类高级玩法入门阶段先别碰，具体支持范围各版本可能不同，需要时查官方文档。前面这三种集合，够你写完前十个练手项目。
:::

#### 五、函数与闭包的进阶写法

函数是代码里最小的"活儿单位"，也是新手和老手拉开差距的地方。这一节先给一条铁律，再讲参数、函数类型和闭包，全部围绕"在 ArkTS 里怎么写才不出错"。

##### 铁律：箭头函数优先

把函数当值赋给变量时，ArkTS 不让用 function 关键字的表达式，要用箭头函数。看对比：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 函数写法对比</span><span class="dots">···</span>
:::

```
// 错误示范：函数表达式
const greet = function (name: string): string {
  return '你好，' + name
}

// 纠正：箭头函数
const greet = (name: string): string => {
  return '你好，' + name
}

// 单个表达式还能更短，大括号和 return 一起省
const greet = (name: string): string => '你好，' + name
```
:::

面板上对应的报错码形如 arkts-no-function-expressions。为什么禁？箭头函数的 this 行为是确定的，继承外层，不会因为"谁调用它"而变，少一大类玄学 bug。注意这条禁令只针对"函数表达式"：class 里的方法还是老老实实写方法（<code class="inline">greet(name: string): string { ... }</code>），那是允许且推荐的。

##### 参数：可选、默认值、剩余

三种特殊参数都支持，写法如下：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 参数的三种花样</span><span class="dots">···</span>
:::

```
// 可选参数：标问号，函数体内就得处理"没传"的情况
function hello(name?: string): void {
  let who: string = name !== undefined ? name : '朋友'
  console.info('你好，' + who)
}

// 默认值：不传就用默认的
function greet(name: string, prefix: string = '同学'): void {
  console.info(prefix + ' ' + name + '，你好')
}

// 剩余参数：不知道会传几个
function sum(...nums: number[]): number {
  let total: number = 0
  for (let n of nums) {
    total += n
  }
  return total
}
```
:::

可选参数和默认值选一个用就好，别又标问号又给默认值：语义重复，读代码的人会困惑。剩余参数收进来的是一个数组，遍历它就行。

##### 函数也是值：类型要标，回调要稳

函数可以存进变量、当参数传、当返回值返回，但每个函数值的类型都要能说清楚。参数是几个、什么类型，返回什么类型，一样都不能含糊：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 函数类型与回调</span><span class="dots">···</span>
:::

```
// 用 type 给"某种形状的函数"起个名
type Comparator = (a: number, b: number) => number

let byAsc: Comparator = (a: number, b: number) => a - b
let byDesc: Comparator = (a: number, b: number) => b - a

// 回调作为参数传入时，参数类型写清楚
function processIds(ids: number[], each: (id: number) => void): void {
  for (let id of ids) {
    each(id)
  }
}

processIds([1, 2, 3], (id: number) => {
  console.info('处理 ' + id)
})
```
:::

回调类型标清楚，编辑器补全才准，写错参数个数也会立刻被指出。这条在 UI 章会天天用到，ArkUI 的事件回调全是这个模式，现在练熟，到那边就是复制粘贴的事。

##### 闭包：函数把环境"记住"了

闭包听起来吓人，行为很朴素：内层函数引用了外层的变量，外层返回之后，那块变量还活着。最经典的例子是计数器：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 闭包计数器</span><span class="dots">···</span>
:::

```
function makeCounter(): () => number {
  let count: number = 0
  return (): number => {
    count++
    return count
  }
}

let c = makeCounter()
console.info('' + c())   // 1
console.info('' + c())   // 2
console.info('' + c())   // 3
```
:::

count 是 makeCounter 里的局部变量，按理说函数返回就该销毁，但返回的那个箭头函数还引用着它，于是它被"记住"了。防抖、节流、简单缓存，都是这一个原理的变体。JS 有个老坑：循环里用 var 声明计数变量，闭包里读到的全是循环结束后的值。这个坑在 ArkTS 里自动消失，var 根本不让用，let 每轮循环都是新变量，各闭包记各的。

最后说一下 this。两条经验：class 里的方法用方法写法，this 指向实例；把方法"摘下来"当回调传出去时，this 会丢，要么用箭头函数包一层再传，要么把这段逻辑写成不依赖 this 的纯函数，参数进、结果出。在类外面单独使用 this 是被禁止的，编译器会拦，别跟它较劲。

#### 六、类与继承在 ArkTS 里的规则

类是 ArkTS 应用的骨架：数据模型是类，页面组件本质上也是带装饰器的类。这一节把 class 的规则过一遍，重点是访问控制、继承、抽象类，以及"没有结构化类型"带来的实际影响。

##### 基本款：字段、构造、访问修饰

::: div .code-block
:::inline div .code-head
<span>ARKTS · Article 类</span><span class="dots">···</span>
:::

```
class Article {
  readonly id: number          // 只读：初始化之后不许改
  title: string                // 不写修饰符，默认公开
  private views: number = 0    // 私有：只有类自己能动

  constructor(id: number, title: string) {
    this.id = id
    this.title = title
  }

  read(): void {
    this.views++               // 类内部可以碰 private
  }

  get hotness(): number {
    return this.views
  }
}

let art: Article = new Article(1, 'ArkTS 十日谈')
art.read()
console.info('' + art.hotness)
```
:::

访问修饰符三个：public（默认，不写就是它）、private（只有本类能动）、protected（本类和子类）。别小看 private，它把"这个字段别人不许动"从口头约定变成编译器检查，谁越界谁报错，比注释管用一百倍。readonly 则管住"初始化之后不许改"，适合 id、创建时间这类一旦定下就不该变的字段。所有属性要么声明时给初值，要么在构造函数里赋值；真有可能暂时没值，就把类型标成可空（比如 <code class="inline">string | undefined</code>），用之前判断，编译器会盯着你。

##### 继承：extends 与 super

::: div .code-block
:::inline div .code-head
<span>ARKTS · 继承</span><span class="dots">···</span>
:::

```
class Animal {
  name: string
  constructor(name: string) {
    this.name = name
  }
  sound(): string {
    return '...'
  }
}

class Dog extends Animal {
  constructor(name: string) {
    super(name)                // 先把父类构造完，再做自己的事
  }
  sound(): string {            // 重写父类方法
    return '汪！我是' + this.name
  }
}

let d: Animal = new Dog('阿黄')
console.info(d.sound())        // 汪！我是阿黄
```
:::

子类构造函数里必须先调 <code class="inline">super(...)</code> 再碰自己的 this，顺序错了直接报错。子类可以重写父类方法，签名要兼容。ArkTS 只有单继承，一个类只能 extends 一个父类，想要"多种能力"，用接口组合：类可以实现（implements）多个接口，每个接口只约定一小块能力，拼装着用。

##### 抽象类与接口：分工不同

::: div .code-block
:::inline div .code-head
<span>ARKTS · abstract 与 implements</span><span class="dots">···</span>
:::

```
abstract class Shape {
  abstract area(): number                  // 只声明，不实现
  describe(): string {                     // 抽象类可以带现成的方法
    return '面积是 ' + this.area()
  }
}

class Circle extends Shape {
  r: number
  constructor(r: number) {
    super()
    this.r = r
  }
  area(): number {
    return Math.PI * this.r * this.r
  }
}

interface Speaker {
  speak(): string
}

class Robot implements Speaker {
  speak(): string {
    return '哔——'
  }
}
```
:::

一句话分清两者：接口只管"你会不会这些动作"（有什么方法），抽象类还管"一部分动作我替你做了"。抽象类不能直接 new，必须由子类继承并补齐抽象方法。拿捏不准就先用接口，它更轻，类的包袱更小。

##### 没有结构化类型，意味着什么

第二节说过 ArkTS 不认"长得一样就算同类"，这里给一个具体翻车现场：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 结构化类型的翻车现场</span><span class="dots">···</span>
:::

```
interface PointA { x: number, y: number }
interface PointB { x: number, y: number }

function draw(p: PointA): void {
  console.info('画点 ' + p.x + ',' + p.y)
}

let b: PointB = { x: 1, y: 2 }
draw(b)      // 在 TS 里畅通无阻，在 ArkTS 里报错
```
:::

修法有两个。治本：两处数据形状一样，就抽成一个 interface 共用，别复制粘贴定义。治标：实在动不了旧定义，写一个显式的转换函数，逐字段构造新对象。顺带说，instanceof 在 ArkTS 里可以正常用，收窄类型、判断"这到底是不是某个类"都靠它，第九节的错误处理里它会高频出场。

#### 七、异步编程：async/await 与 Promise

设想一个真实场景：你在写"每日一言"页面，点一下按钮，从服务端拿一句话显示出来。网络一来一回要几百毫秒，等的时候界面不能卡死，点了别的也要有反应，这就是异步要解决的问题。好消息：Promise 和 async/await 在 ArkTS 里都是一等公民，写法和你熟悉的一致；系统提供的网络、文件这些能力，返回的也基本都是 Promise。

##### 先认识 Promise：一张"欠条"

Promise&lt;T&gt; 表示"将来会给你一个 T"。它有等待、成功、失败三种状态，成功时调 resolve 交货，失败时调 reject 报错：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 手写一个 Promise</span><span class="dots">···</span>
:::

```
function fetchQuote(): Promise&lt;string&gt; {
  return new Promise&lt;string&gt;(
    (resolve: (v: string) => void, reject: (e: Error) => void) => {
      setTimeout(() => {
        // 假装这里是网络请求
        resolve('今天也要好好吃饭')
      }, 1000)
    }
  )
}

fetchQuote().then((quote: string) => {
  console.info(quote)
}).catch((err: Object) => {
  console.error('失败了')
})
```
:::

实际开发里你大多是"接欠条"的一方，系统 API 给你 Promise，你负责接住，自己手写 new Promise 的机会不多。接的方式有两种：then/catch 链，或者下一节的 async/await。

##### async/await：把异步写成同步的样子

::: div .code-block
:::inline div .code-head
<span>ARKTS · async/await</span><span class="dots">···</span>
:::

```
async function showQuote(): Promise&lt;void&gt; {
  try {
    let quote: string = await fetchQuote()
    console.info('拿到：' + quote)
    let another: string = await fetchQuote()
    console.info('再拿一条：' + another)
  } catch (e) {
    console.error('出错了，界面提示重试')
  }
}
```
:::

三个规则记牢：await 必须待在 async 函数里；async 函数的返回类型一定是 Promise，没返回东西就写 <code class="inline">Promise&lt;void&gt;</code>；await 的东西可能失败，外面要套 try/catch（catch 里的类型问题在错误处理一节细讲）。顺序请求直接上下两行 await 写，比 then 套 then 清爽得多。几种风格别混着来：一个函数里要么全 await，要么全 then 链，混着写排查问题时会晕。

##### 并行：几件事互不依赖，就一起等

::: div .code-block
:::inline div .code-head
<span>ARKTS · Promise.all</span><span class="dots">···</span>
:::

```
async function loadPage(): Promise&lt;void&gt; {
  // 三个请求一起发，全部完成才往下走
  let quotes: string[] = await Promise.all([
    fetchQuote(), fetchQuote(), fetchQuote()
  ])
  console.info('共拿到 ' + quotes.length + ' 条')
}
```
:::

Promise.all 适合"互相不依赖"的请求：首屏要同时拿头像、昵称、列表，就别一个 await 完再 await 下一个，三个一起发，总耗时约等于最慢的那个。注意前提是"互不依赖"：后一个请求要拿前一个的结果，老老实实顺序 await。

##### 事件回调里的 async：别让错误没人管

::: div .code-block
:::inline div .code-head
<span>ARKTS · 事件回调与异步</span><span class="dots">···</span>
:::

```
// 错误示范：回调里调 async 方法，返回的 Promise 没人管
Button('换一句')
  .onClick(() => {
    this.loadQuote()      // loadQuote 内部若出错，这里无人接住
  })

// 纠正：async 方法内部自己兜底，把错误消化在方法里
async function loadQuote(): Promise&lt;void&gt; {
  try {
    let quote: string = await fetchQuote()
    this.current = quote
  } catch (e) {
    this.current = '网络开小差了，再点一次试试'
  }
}
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>避坑提醒

{class="mt-1"}
async 不等于多线程。await 等待期间主线程确实会去干别的（比如响应你的点击），但 CPU 密集的计算，解析大 JSON、图片处理、复杂排序：照样占着主线程，界面照样卡。重活儿要走 Worker/TaskPool 那套多线程手段，后面的章节会讲，以官方文档为准。
:::

#### 八、模块化：import/export 与工程组织

代码过了两三百行，你就想拆文件了。ArkTS 的模块化和 ES 模块几乎一样，几个小差异要注意；比语法更要紧的是"文件怎么组织"，这一节两件事都讲。

##### export 与 import：拆出去，引回来

::: div .code-block
:::inline div .code-head
<span>ARKTS · 导出（model/Todo.ets）</span><span class="dots">···</span>
:::

```
export class Todo {
  id: number = 0
  title: string = ''
  done: boolean = false
}

export function formatTitle(raw: string): string {
  return raw.trim()
}
```
:::

::: div .code-block
:::inline div .code-head
<span>ARKTS · 导入（pages/Index.ets）</span><span class="dots">···</span>
:::

```
import { Todo, formatTitle } from '../model/Todo'
import { Todo as Task } from '../model/Todo'   // 重命名，避免撞名

let t: Todo = new Todo()
t.title = formatTitle('  收拾桌面  ')
```
:::

跟着官方示例走，用命名导出（<code class="inline">export class</code>、<code class="inline">export function</code>）最稳，导入时花括号里写名字。名字撞了就用 as 改名。至于 default 导出，官方示例里很少见，具体支持情况以文档为准，新手直接养成命名导出的习惯就好。

##### 系统模块：@ 开头的来客

系统能力用 @ 开头的路径导入，这是应用和操作系统打交道的大门。新模板里常见 Kit 风格，比如要操作窗口，就从 <code class="inline">@kit.ArkUI</code> 里拿 window；老一些的资料里你会看到 <code class="inline">@ohos.xxx</code> 风格。两种写法对应同一批能力，具体用哪种，以你工程模板里的既有写法和官方文档为准：拿不准时，打开模板里现成的 import 照抄最保险。

##### 桶文件：一个文件夹一个出口

::: div .code-block
:::inline div .code-head
<span>ARKTS · 桶文件（model/index.ets）</span><span class="dots">···</span>
:::

```
export { Todo } from './Todo'
export { TodoStore } from './TodoStore'
```
:::

::: div .code-block
:::inline div .code-head
<span>ARKTS · 使用方只看文件夹</span><span class="dots">···</span>
:::

```
import { Todo, TodoStore } from '../model'
```
:::

model 文件夹下文件一多，使用方一行行 import 会很烦。加一个 index.ets 当"总出口"，把里面的东西统一转手导出，外面只需要 import 文件夹一层。代价是转手这一层要维护，文件夹小的时候可以不做，东西多了再收拢。

##### 副作用导入被禁了

::: div .code-block
:::inline div .code-head
<span>ARKTS · 副作用导入的错误与纠正</span><span class="dots">···</span>
:::

```
// 错误示范：导入只为"跑一遍"里面的代码
import './setup'

// 纠正：setup.ets 里导出显式的初始化函数，入口处调用
import { initApp } from './setup'
initApp()
```
:::

"只 import 不取东西"的写法在 ArkTS 里不让用（对应 arkts-no-side-effect-imports 一类的报错）。道理也简单：隐式执行的代码没人看得见，出错都不知道从哪查起。一切初始化都走显式函数调用，谁调用的、什么时候调用的，一眼可查。

##### 工程组织：文件放哪，心里有数

::: div .code-block
:::inline div .code-head
<span>ARKTS · 目录树参考</span><span class="dots">···</span>
:::

```
entry/src/main/ets/
├── entryability/      入口 Ability（工程模板自带）
│   └── EntryAbility.ets
├── pages/             页面，一个页面一个文件
│   └── Index.ets
├── model/             数据模型：interface 与 class
│   ├── Todo.ets
│   └── TodoStore.ets
├── service/           网络请求、本地存储这类"做事"的代码
├── view/              可复用的自定义组件
└── utils/             到处都可能用的小工具
```
:::

分层的心法一句话：页面管"长什么样"，model 管"数据长什么样"，service 管"数据从哪来"，utils 放"谁都可能用"的小函数。判断一段代码该放哪，问自己一个问题："将来换个界面，这段代码还要不要存在？"要，就别写在页面文件里。工程再大之后，公共代码可以抽成共享包（官方叫 HAR、HSP 两种），DevEco 里新建时选对应模板即可，入门阶段用不到，等做第二个应用想复用代码时再回来看官方的共享包文档。

#### 九、错误处理：try/catch 与自定义错误

错误分两种来源：语言层的异常，你的代码在运行时炸了，比如解析一个不是数字的字符串；能力层的失败，网络超时、文件不存在、权限没给。两种都要接住，但接法有差别，这一节把 try/catch 的语法、catch 里的类型问题、系统 API 的错误约定、自定义错误类一次讲齐。

##### try/catch/finally 基本款

::: div .code-block
:::inline div .code-head
<span>ARKTS · 解析一个可能出错的字符串</span><span class="dots">···</span>
:::

```
function parseCount(text: string): number {
  try {
    let n: number = Number(text)
    if (Number.isNaN(n)) {
      throw new Error('不是数字：' + text)
    }
    return n
  } catch (e) {
    console.error('解析失败，按 0 处理')
    return 0
  } finally {
    console.info('解析结束')     // 无论成败都会执行
  }
}
```
:::

注意 catch 的括号里没写类型——这不是偷懒，是规矩。ArkTS 禁止给 catch 参数标类型（报错码形如 arkts-no-types-in-catch）：能进 catch 的东西类型不可靠，标了也担保不了。那怎么知道抓到的到底是什么？往下看。

##### catch 里的收窄：instanceof 与 BusinessError

::: div .code-block
:::inline div .code-head
<span>ARKTS · 收窄错误类型</span><span class="dots">···</span>
:::

```
catch (e) {
  if (e instanceof Error) {
    console.error('消息：' + e.message)
  } else {
    console.error('不知道是什么错误，原样打出来看看')
  }
}
```
:::

调用系统能力（网络、文件、传感器）时，官方对错误对象有统一约定：它长 BusinessError 的样子，带 code（数字错误码）和 message。惯用写法是转换之后取字段：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 系统 API 的错误约定</span><span class="dots">···</span>
:::

```
import { BusinessError } from '@kit.BasicServicesKit'

try {
  // 某个系统 API 调用，比如请求网络
} catch (err) {
  let e: BusinessError = err as BusinessError
  console.error('错误码 ' + e.code + '：' + e.message)
}
```
:::

code 是排障的关键线索，把它的含义到官方文档里搜一下，比笼统的"失败了"有用得多。给爸妈远程帮忙时你大概没法看日志，但自己开发时，养成"先看 code 再改代码"的习惯，能少走很多弯路。

##### 自定义错误：给业务失败起名字

::: div .code-block
:::inline div .code-head
<span>ARKTS · 自定义错误类</span><span class="dots">···</span>
:::

```
class ApiError extends Error {
  code: number
  constructor(code: number, message: string) {
    super(message)
    this.code = code
  }
}

// 业务上发现不对，就抛一个带语义的错误
function handleResponse(code: number, body: string): string {
  if (code !== 0) {
    throw new ApiError(code, '服务器说不行')
  }
  return body
}

try {
  handleResponse(401, '')
} catch (e) {
  if (e instanceof ApiError) {
    console.error('业务错误码 ' + e.code)
  } else if (e instanceof Error) {
    console.error('普通异常：' + e.message)
  }
}
```
:::

抛错误时 throw new Error(...)，别 throw 一个字符串——字符串没有 message、没有堆栈，接的人什么都查不到。自定义错误类继承 Error，加上业务字段（比如 code），接的人用 instanceof 一分，就知道该走哪条处理路径。

##### 异步错误的坑：try 要包住 await

::: div .code-block
:::inline div .code-head
<span>ARKTS · try 包不住没 await 的调用</span><span class="dots">···</span>
:::

```
// 错误示范：忘写 await
async function load(): Promise&lt;void&gt; {
  try {
    fetchSlow()          // fetchSlow 内部抛的错，这里接不到
  } catch (e) {
    // 永远走不到这里
  }
}

// 纠正：await 一写，错误才会落到这个 try 里
async function load(): Promise&lt;void&gt; {
  try {
    await fetchSlow()
  } catch (e) {
    console.error('这回真的接住了')
  }
}
```
:::

最后一条纪律：catch 里不要什么都不写。"吞掉错误"是新手最常见的反模式：界面不崩了，但数据是错的，你连哪错了都不知道。至少 console.error 记一笔；能恢复就恢复（给默认值、提示重试），不能恢复就继续往上层抛，让有 UI 的那一层给用户看提示。

#### 十、常见报错门诊：arkts-no-xxx 逐个看

这一节像门诊：先给通用就诊流程，再给一张速查表，最后挑三个高发病症详细会诊。通用流程三步：在 DevEco 的 Problems 面板复制报错码；到官方文档《从 TypeScript 到 ArkTS 适配规则》页面搜这个码；照着成对的"错误示例/正确示例"改。报错码偶尔随版本调整，以你面板上实际显示的为准，搜不到就搜关键词。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">报错码（形如）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">病因</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">修法</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">arkts-no-any-unknown</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用了 any / unknown</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">换具体类型；一时说不清就定义 interface</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">arkts-no-var</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用了 var</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">换 let 或 const</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">arkts-no-function-expressions</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把 function 表达式赋给变量</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">改箭头函数</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">arkts-no-obj-literals-as-types</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把对象字面量当类型（type X = {...}）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">改 interface 或 class</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">arkts-no-structural-typing</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">指望"字段相同就算同类型"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">共用同一个 interface，或写显式转换</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">arkts-no-props-by-name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用字符串下标取属性 obj['name']</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">直接 obj.name；键真动态用 Record 或 Map</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">arkts-no-types-in-catch</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">给 catch 参数标了类型</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">去掉标注，用 instanceof 收窄</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">arkts-no-side-effect-imports</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">只为副作用而导入</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">导出显式函数并在入口调用</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">arkts-no-standalone-this</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">在类外面单独用 this</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用实例引用代替</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">arkts-no-spread</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">扩展运算符用在了受限场合</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数组用 concat，对象逐字段赋值</td></tr>
</tbody>
</table>
```
:::

##### 会诊一：any 依赖症

::: div .code-block
:::inline div .code-head
<span>ARKTS · any 依赖症</span><span class="dots">···</span>
:::

```
// 症状
function process(data: any): void {
  console.info(data.name)
}
// 诊断：any 的意思是"我不想想类型"。ArkTS 直接禁。
// 处方：想清楚它到底是什么。是用户？就定义 User。

interface User {
  name: string
  age: number
}

function process(data: User): void {
  console.info(data.name)   // 编辑器还能帮你补全 name
```
:::

遇到"类型说不清"的时候，别用 any 打发，把说不清本身当成信号：说明这块数据的形状你还没想明白。想明白了写下来，就是 interface；写完之后编辑器的补全和检查全是白送的。

##### 会诊二：拿对象当字典用

::: div .code-block
:::inline div .code-head
<span>ARKTS · 字符串下标的两种修法</span><span class="dots">···</span>
:::

```
// 症状：JS 老习惯，对象当字典
let obj = { a: 1, b: 2 }
let va = obj['a']            // 字符串下标——报错

// 修法一：字段固定，直接点出来
interface Config {
  a: number
  b: number
}
let c: Config = { a: 1, b: 2 }
let va: number = c.a

// 修法二：键真的是动态的，用 Record
let scores: Record&lt;string, number&gt; = {}
scores['math'] = 90
let ms = scores['math']      // Record 允许下标访问
```
:::

判断标准：编译期能列出全部键，用 interface；键要到运行时才知道（比如以用户 id 为键的缓存），用 Record 或 Map。Record 是官方给"字符串键字典"留的正门，比绕路强。

##### 会诊三：长得一样不算数

::: div .code-block
:::inline div .code-head
<span>ARKTS · 结构化类型报错的修法</span><span class="dots">···</span>
:::

```
// 症状
interface A { x: number, y: number }
interface B { x: number, y: number }
function show(p: A): void { console.info('' + p.x) }
let b: B = { x: 1, y: 2 }
show(b)          // 报错：B 不能当 A 用

// 修法：共用一个定义
interface Point { x: number, y: number }
function show(p: Point): void { console.info('' + p.x) }
let b: Point = { x: 1, y: 2 }
show(b)          // 通过
```
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hand-pointer mr-2"></i>来动手：主动制造三个报错

{class="mt-1"}
1\. 写一行 let x: any = 1，记下面板上的报错码；2. 写一个 function 表达式赋值给变量，再记一个；3. 在 catch 括号里标个类型。每一条都先试编辑器的快速修复，修不动就对照上面的门诊表手改。主动犯一次错，比被动撞十次记得牢。
:::

#### 十一、TS/JS 老手的迁移对照表

这张表给写过 TS/JS 的你：左边是肌肉记忆，右边是到了 ArkTS 该怎么做。表后把最容易反复犯的三条展开说。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">TS/JS 的习惯</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ArkTS 的写法</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">let x: any 兜底</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定义具体 interface 或 class</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">var 声明变量</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">let（会变）或 const（不变）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">运行时给对象加属性 obj.newField = v</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">字段预先声明在 interface/class 里</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">type T = { a: number }</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">interface T { a: number } 或 class</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">const f = function () {}</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">箭头函数</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">obj['key'] 字符串下标</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">obj.key；键动态用 Record 或 Map</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">结构相同即兼容</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">显式同名 interface/class</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">catch (e: Error) 标类型</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">catch (e) 后 instanceof 收窄</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">对象解构 const { a, b } = obj</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">逐个赋值（解构受限，以官方为准）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">== 宽松相等</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一律 ===</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">import './mod' 副作用导入</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">导出 init() 显式调用</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">依赖编译器推断一切</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">关键位置显式标注，尤其函数返回值</td></tr>
</tbody>
</table>
```
:::

##### 重点一：解构受限，老老实实点出来

对象解构在 ArkTS 里属于受限特性，不同场景的可用程度以官方规则页为准。稳妥做法是想用哪个属性就单独取：<code class="inline">let title: string = article.title</code>。一行一个，看着笨，但每个变量的类型清清楚楚，出问题排查也快。别赌编辑器会不会放行——它这次放行了，换个写法可能就不放了。

##### 重点二：等号多打一个

JS 里 == 的隐式转换坑（'1' == 1 是 true 这类）在 ArkTS 里没有存在的必要，全部写 ===。多打一个等号，少查半天 bug，这笔账怎么算都划算。顺手把"判断前先想清楚两边是什么类型"也练上：严格相等逼你直面类型，这正是迁移的价值。

##### 重点三：扩展运算符省不了几行

...spread 在 ArkTS 里受限（报错码形如 arkts-no-spread），别硬绕。数组合并用 concat，对象合并就逐字段赋值或者写一个小的合并函数：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 不用 spread 的合并</span><span class="dots">···</span>
:::

```
// 旧习惯：let all = [...arr1, ...arr2]
let all: string[] = arr1.concat(arr2)

// 旧习惯：let both = { ...base, ...patch }
function merge(base: Config, patch: Config): Config {
  let out: Config = { a: base.a, b: base.b }
  if (patch.a !== undefined) { out.a = patch.a }
  if (patch.b !== undefined) { out.b = patch.b }
  return out
}
```
:::

迁移的整体心态：这不是"重新学一门语言"。这是"把以前靠运气的地方改成靠类型"。你过去写 any 省下的每一秒，都在未来的某次线上问题里等着你还；ArkTS 只是提前把账单递到了你手上。

#### 十二、纯新手的入门路径：从零学语言的最小路线

如果你连 JavaScript 都没写过，别慌，也别去走"先学完 JS，再学 TS，再学 ArkTS"的老路，那是给多年前端准备的顺序，不适合你。直接在 ArkTS 的语境里学，报错就是你的第一任老师。下面是按依赖关系排好的最小路径，一步练熟再走下一步，跳步会在后面加倍还回来。

1. <strong>变量与类型</strong>：let/const、number/string/boolean、类型标注怎么写。
2. <strong>分支与循环</strong>：if/else、for、while，数组遍历。
3. <strong>函数</strong>：参数、返回值、箭头函数。
4. <strong>数组与对象</strong>：数组方法、interface、class。
5. <strong>异步初步</strong>：Promise 与 async/await 是什么、怎么用。
6. <strong>装饰器感知</strong>：认得 @State 这些标签，细节留给 UI 章。

第一步，变量与类型。核心就三行代码的事：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 变量与类型</span><span class="dots">···</span>
:::

```
let name: string = '阿黄'      // 会变的，用 let
const maxTries: number = 3     // 不变的，用 const
let done: boolean = false
```
:::

一个新手常见困惑：const 是"绑定不可变"，不是"内容不可变"<code class="inline">const arr: number[] = []</code> 之后依然可以 push，只是不能把 arr 重新赋值成别的东西。想连内容都不许动，那是 readonly 的活儿。这个区别现在记不住没关系，写两周自然懂。

第二步，分支与循环。if/else 和其他语言一样，遍历数组优先用 for...of，比下标循环少出 off-by-one 的错：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 分支与循环</span><span class="dots">···</span>
:::

```
let scores: number[] = [88, 92, 75]
let pass: number = 0
for (let s of scores) {
  if (s >= 80) {
    pass++
  }
}
console.info('80 分以上 ' + pass + ' 人')
```
:::

坑提醒一条：想"边遍历边删"，先停手——下标会乱跳，通常 filter 出一个新数组更安全。第三步，函数。这一步除了语法，更重要的是养成给东西好好取名的习惯：函数名用动词（loadUser、formatTitle），变量名用名词（userName、itemList），布尔值用 is/has 开头（isReady、hasCache）。<code class="inline">const isAdult = (age: number): boolean => age >= 18</code> 这样的函数，三个月后回看不用猜。

第四步，数组与对象，是前面第四、六两节的主场，回去把 TodoStore 的例子亲手敲一遍。第五步，异步初步，只需要理解三个词：Promise 是"欠条"，async 是"这里要等"，await 是"等到了再往下走"。细节看第七节，不着急一次吃透。第六步，装饰器，你只要会"认"和"抄"：工程模板里出现 @Entry、@Component、@State 时，知道它们是框架贴的标签，照着模板用，别自己发明。

练习场的选择也有讲究：网上那些在线 TS 演练场用的是宽松版规则，很多 ArkTS 禁止的写法在那边畅通无阻。建议全部练习都在 DevEco 的 Previewer 里做，改一行，看一次界面，报错就地消化。在线演练场可以当草稿纸，但每个写法回到 DevEco 都要重新"过安检"。

最后是几个新手高频问题，一次答完。问：要不要先把 JavaScript 学完？答：不用，走上面的最小路径，缺什么补什么；JS 里大量浏览器相关的知识（DOM、事件冒泡）在鸿蒙开发里用不上，先学了也是白背。问：纯新手学 ArkTS 会不会太难？答：难在"教程比老语言少"，但语言本身因为禁掉了各种花活，反而更规矩：你犯不了太多错，编译器全给你拦着。问：数学不好能学吗？答：语言层用到的是加减乘除和取余，初中数学绰绰有余。问：看视频还是看文档？答：视频入门快，成体系的知识在文档里；以文档为主、视频为辅，视频里的界面和步骤以你装的版本为准。问：每天学多久？答：三十分钟能稳定推进，比周末突击八小时有效，编程是手感活，靠连续，不靠爆发。

#### 十三、代码风格与工程规范

语言关过了，决定你代码"能不能和人协作"的就是风格。这一节没有绝对对错，只有"跟谁保持一致"，跟团队保持一致，跟官方示例保持一致，然后整个项目从头到尾一致。三个一致做到，你的代码就已经好于大多数练手项目。

##### 命名：名字要说人话

- <strong>类与接口</strong>：大驼峰，TodoStore、ArticleItem、HttpService。
- <strong>变量、函数、方法</strong>：小驼峰，loadUser、fetchQuote、currentPage。
- <strong>固定常量</strong>：用 static readonly 收进类里，全大写加下划线（如 MAX_RETRY）也行，关键是团队统一。
- <strong>文件名</strong>：跟着工程模板走，同一个项目里统一，别一个文件一个风格。

质量比格式更要紧：名字要说"是什么、做什么"，别怕长。getUserById 比 getData 好，isReady 比 flag 好，secondsUntilRetry 比 s 好。取名的本质是替三个月后的自己写注释，那个已经忘光上下文的你，会感谢现在多打了五个字母的你。

##### 注释：写为什么，不写是什么

::: div .code-block
:::inline div .code-head
<span>ARKTS · 注释的两个档次</span><span class="dots">···</span>
:::

```
// 不好：把代码翻译一遍
// 把 count 加一
count++

// 好：解释代码说不出来的背景
// 服务端对连续请求限速，这里隔一拍再发
count++
```
:::

"代码自己会说的"（做什么）一行注释都别写；"代码说不出来的"（为什么这么做、踩过什么坑、和哪个约定绑定）必须写。接口和公开类用 /** */ 写一句用途说明，编辑器悬停时能看到，这是花三十秒换长期收益的买卖。

##### 文件组织与拆分时机

一个文件干一件事：一个页面、一个组件、一个模型类。文件超过两三百行就留心拆分（这是心理阈值，不是硬规定）。拆分按"职责"按"行数"都行。但优先问：这段逻辑换界面后还要不要？要，就挪出页面文件，网络细节进 service，数据变换进 model，通用小工具进 utils。第八节的目录树就是按这个逻辑长出来的。

##### 让工具替你把关

DevEco 自带 Code Linter，提交代码前跑一遍，能把本章讲的大部分规矩自动查出来。缩进、空格、行宽这类格式问题彻底交给工具——菜单里的格式化功能就是干这个的，具体快捷键以你的键位设置为准。人和工具要分工：人管"这段逻辑对不对"，工具管"这个分号写没写"。把格式问题留给工具，把脑力留给设计。

如果要跟人协作，交出去之前按这份清单过一遍：有没有 any 的亲戚（unknown、as any）偷偷溜进来；异步调用有没有人接错误；新增字段是不是先改了 interface；命名能不能不看实现就懂；有没有复制粘贴超过两次的代码块（该抽函数了）。五个都过了，再喊人 review，这是对彼此时间的尊重。

#### 十四、实战串讲：把"能跑"的小工具改成"好改"的小工具

前面十个小节是零件，这一节装配。场景是这样的：周日晚上你想给楼下小卖部写个"赊账本"，记谁欠了多少钱、能记账、能销账、能看总欠款。第一版图快，全塞在页面文件里。严格说，这一版在 ArkTS 里连编译都过不了，一会儿你就知道为什么。现在分五步，把它改成下个月自己还愿意打开的样子。

##### 第一步：数据先定型

::: div .code-block
:::inline div .code-head
<span>ARKTS · 第一版的雏形</span><span class="dots">···</span>
:::

```
// 第一版的样子：类型全是谜
let rows = []
function addRow(who, howMuch) {
  rows.push({ name: who, amount: howMuch, time: Date.now() })
}
```
:::

这段在 JS 里能跑，在 ArkTS 里第一行就报错：数组没类型，函数参数没类型。别嫌编译器烦，一个月后你回头看这段代码，rows 里到底装了什么，只有当时赶工的你一个人知道。改成下面这样：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 给数据定形状</span><span class="dots">···</span>
:::

```
interface DebtRow {
  name: string
  amount: number
  time: number
}

let rows: DebtRow[] = []

function addRow(who: string, howMuch: number): void {
  rows.push({ name: who, amount: howMuch, time: Date.now() })
}
```
:::

对象字面量能直接 push 进去，因为它有 DebtRow 可归。数据形状定了，后面每一步都有地方落脚。

##### 第二步：数据与逻辑进 class

现在记账销账的逻辑散在页面文件里，将来第二个页面要用，就得复制一份。把"欠账"这件事封装成类：

::: div .code-block
:::inline div .code-head
<span>ARKTS · Ledger 类</span><span class="dots">···</span>
:::

```
class Ledger {
  private rows: DebtRow[] = []

  add(name: string, amount: number): DebtRow {
    let row: DebtRow = { name: name, amount: amount, time: Date.now() }
    this.rows.push(row)
    return row
  }

  settle(name: string, amount: number): boolean {
    let row = this.rows.find(r => r.name === name)
    if (row === undefined) {
      return false            // 人都不在账上，销个啥
    }
    row.amount = row.amount - amount
    if (row.amount &lt;= 0) {
      this.rows = this.rows.filter(r => r.name !== name)
    }
    return true
  }

  total(): number {
    let sum: number = 0
    for (let r of this.rows) {
      sum += r.amount
    }
    return sum
  }

  get all(): DebtRow[] {
    return this.rows
  }
}
```
:::

注意 rows 是 private——外面想动账本，只能走 add 和 settle，想绕过校验直接改数组？编译器不答应。settle 里那个人可能根本不在账上，所以返回 boolean 告诉调用方"销没销成"，比默默什么都不做强太多。等下一章把界面做完，UI 只需要拿着 Ledger 调方法，一行账务逻辑都不用碰。

##### 第三步：统计写成纯函数

"一共欠多少""谁欠得最多"这类统计，天生和界面无关，也和账本怎么存无关：它们是"给一批数据、还你一个结果"的纯函数，放进 utils：

::: div .code-block
:::inline div .code-head
<span>ARKTS · utils/stats.ets</span><span class="dots">···</span>
:::

```
import { DebtRow } from '../model/DebtRow'

export function sumDebts(rows: DebtRow[]): number {
  let sum: number = 0
  for (let r of rows) {
    sum += r.amount
  }
  return sum
}

export function topDebtor(rows: DebtRow[]): string | undefined {
  let top: DebtRow | undefined = undefined
  for (let r of rows) {
    if (top === undefined || r.amount > top.amount) {
      top = r
    }
  }
  return top === undefined ? undefined : top.name
}
```
:::

纯函数的好处是"随便测"：不用起界面、不用连数据，构造几行假数据传进去就知道对不对。参数进、结果出，不碰任何全局变量，写的时候守这条，测试的时候省半天。

##### 第四步：把可能失败的操作包起来

账本总得存到手机上，下次打开还在。存储和网络的调用要到后面的章节才细讲，这里先把"必须接错误"的骨架搭好：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 带兜底的保存</span><span class="dots">···</span>
:::

```
import { BusinessError } from '@kit.BasicServicesKit'

async function saveLedger(rows: DebtRow[]): Promise&lt;void&gt; {
  try {
    await saveToDisk(rows)      // 假想的存储调用
  } catch (err) {
    let e: BusinessError = err as BusinessError
    console.error('保存失败，错误码 ' + e.code)
    // 界面上提示"这笔记账没存上"，别让用户白记
  }
}
```
:::

骨架的意义在于：错误处理的形状先长好，等真正接上系统能力，你只需要换掉中间那一行调用。

##### 第五步：各回各家，各找各妈

::: div .code-block
:::inline div .code-head
<span>ARKTS · 拆完之后的目录</span><span class="dots">···</span>
:::

```
ets/
├── pages/
│   └── Index.ets            页面：只管显示和响应点击
├── model/
│   ├── DebtRow.ets          interface DebtRow
│   └── Ledger.ets           class Ledger
├── service/
│   └── LedgerStore.ets      保存、读取
└── utils/
    └── stats.ets            sumDebts、topDebtor
```
:::

::: div .code-block
:::inline div .code-head
<span>ARKTS · 页面里的导入</span><span class="dots">···</span>
:::

```
import { DebtRow } from '../model/DebtRow'
import { Ledger } from '../model/Ledger'
import { sumDebts, topDebtor } from '../utils/stats'
```
:::

盘点一下前后差别：数据从"没类型的数组"变成 DebtRow[]；散落的函数收进 Ledger，private 挡住野路子；统计变成可独立测试的纯函数；可能失败的操作有了兜底；一个文件变成五个，每个只干一件事。五步里没有用到任何新知识，全是前面小节讲过的东西。所谓"代码好改"，就是把每一件小事都用规矩的方式做一遍。下次功能跑通之后，先别急着加新功能，照这五步过一遍，你写出来的就不只是"能跑的代码"，而是"敢继续往上摞的代码"。

#### 十五、问与答：语言层的高频疑问

收尾之前，把初学者问得最多的十个问题集中答一遍。这些问题都带着真实情绪，因为它们多半是提问者真踩过的坑。

<strong>问：ArkTS 和 TypeScript 到底什么关系？我会 TS，是不是等于已经会了九成？</strong><br>答：语言层面可以这么说——TS 的核心语法全在，你主要学"哪些被收紧、哪些被扩展"。但别把"语言会了"当成"开发会了"：状态管理、UI 写法、工程组织都是新的。语言是入场券，不是全程。

<strong>问：为什么连 any 都不给用？这也太死板了吧？</strong><br>答：死板就是它卖给你的东西之一。ArkTS 的高性能渲染建立在"类型在编译期就确定"之上，any 恰恰意味着"编译期什么都不知道"。你交出去的是随手乱写的自由，换回来的是精准的补全、编译期排错和更稳的运行时。

<strong>问：JS 的 class 和 ArkTS 的 class 有区别吗？</strong><br>答：语法几乎一样，家规更严：不能运行时加属性，不能用"长得像"冒充同类型，函数表达式要换成箭头函数。把第六节那几条记住，你写的 class 就不会翻车。

<strong>问：装饰器先学 V1 还是直接上 V2？</strong><br>答：先 V1。V1 资料多、概念全，学透之后迁 V2 是个顺手的活儿（进阶内容在第 79 章）。反过来先学 V2，你查报错时会反复撞上 V1 时代的资料，两边对不上号，反而晕。

<strong>问：const 和 readonly 到底差在哪？</strong><br>答：const 管"绑定"——这个变量名不能再指向别的东西；readonly 管"属性"——这个字段初始化之后不能再改值。所以 <code class="inline">const arr: number[] = []</code> 之后照样能 push；要连内容都不许动，得 readonly 上场。两个都用上，才是真正的"不许动"。

<strong>问：什么时候用 interface，什么时候用 class？</strong><br>答：只描述"数据长什么样"，用 interface；数据要带行为、要 new 出来、要进状态管理，用 class。拿不准就先 interface，需要行为时再升级成 class——从 interface 升到 class 容易，反过来拆难。

<strong>问：为什么我的 try 接不住异步函数里的错误？</strong><br>答：九成的可能是漏了 await。没 await 的 async 调用只返回一张"欠条"，欠条里的错误谁也没接。把 await 补上，错误才会真正落进你的 try。

<strong>问：泛型要学到什么程度？</strong><br>答：会读、会写最基础的就行。读：看懂 <code class="inline">Array&lt;string&gt;</code>、<code class="inline">Map&lt;string, number&gt;</code> 尖括号里是"里面装什么"。写：最常见的场景是通用的小工具函数：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 最小泛型</span><span class="dots">···</span>
:::

```
function pick&lt;T&gt;(items: T[], index: number): T {
  return items[index]
}

let n: number = pick([10, 20, 30], 1)      // 20
let s: string = pick(['a', 'b'], 0)        // 'a'
```
:::

复杂的泛型约束用到再查，别提前折磨自己——你在这个阶段写的十个函数里，九个用不上。

<strong>问：报错多得看不下去，正常吗？</strong><br>答：正常，而且是好事。报错多说明问题被拦在了运行之前，而不是等你手机上白屏了才炸。头两周把每个报错码都查一次文档，第三周你会发现报错肉眼可见地变少——不是编译器心软了，是你已经开始"用类型的脑子"写代码了。

<strong>问：这一章学完，下一步干什么？</strong><br>答：把本章出现过的每个代码块亲手敲一遍——是敲，不是复制粘贴，手指的记忆比眼睛可靠。然后把十四节的重构不看书独立走一遍。做完这两件事，再翻第 73 章：UI 章的每一段示例，用的都是这一章的语言件。

#### 十六、再深一层：日常高频的进阶写法

基础零件到这一步已经够用了，但真实项目里还有一些天天出现的小场景。这一节当工具袋用，按场景取用，不必一次读完。

##### 判定与查找：some、every、indexOf

::: div .code-block
:::inline div .code-head
<span>ARKTS · 三种常用判定</span><span class="dots">···</span>
:::

```
let ages: number[] = [12, 17, 30, 44]

let hasTeen: boolean = ages.some((a: number) => a >= 13 && a &lt;= 19)
// some：只要有一个满足就 true
let allAdult: boolean = ages.every((a: number) => a >= 18)
// every：全部满足才 true
let idx: number = ages.indexOf(30)
// indexOf：找值的位置，找不到是 -1
```
:::

这三个方法的名字就是语义：some 问"有没有"，every 问"是不是都"，indexOf 问"在第几位"。.includes 判断单个值在不在，some 判断"有没有满足条件的"：注意分清这两个的分工，别用 includes 去找"符合条件的元素"，它只认完全相等的值。

##### 链式调用：好看，但别套娃

::: div .code-block
:::inline div .code-head
<span>ARKTS · filter 接 map</span><span class="dots">···</span>
:::

```
interface Order {
  user: string
  amount: number
}

let orders: Order[] = [
  { user: '阿黄', amount: 88 },
  { user: '小美', amount: 199 },
  { user: '老王', amount: 120 }
]

let bigUsers: string[] = orders
  .filter((o: Order) => o.amount > 100)
  .map((o: Order) => o.user)
// 结果：['小美', '老王']
```
:::

两三段的链式调用清晰好读，超过三段就建议拆成 for..of 加中间变量，链子一长，后来的人（包括三个月后的你）要从尾往头倒着读，容易断。另外链式每一段都会产生一个中间数组，数据量特别大、又抠性能的时候，写成一个循环更省。

##### 对象数组排序与多条件

::: div .code-block
:::inline div .code-head
<span>ARKTS · 先按金额，再按名字</span><span class="dots">···</span>
:::

```
let sorted: Order[] = orders.slice().sort((a: Order, b: Order) => {
  if (a.amount !== b.amount) {
    return b.amount - a.amount        // 金额大的在前
  }
  if (a.user !== b.user) {
    return a.user > b.user ? 1 : -1   // 同额按名字排
  }
  return 0
})
```
:::

两个细节。开头先 slice() 复制一份再排，sort 会原地修改数组，不复制就把原顺序毁了，界面上一闪一闪的诡异排序多半是这个原因。多条件排序的套路是"从主要到次要"逐级比较：第一条件分不出胜负，才比第二条件，最后返回 0 表示平局。

##### 字符串与数字之间：防御性转换

::: div .code-block
:::inline div .code-head
<span>ARKTS · 转换要先验伤</span><span class="dots">···</span>
:::

```
function toCount(text: string): number {
  let n: number = Number(text)
  if (Number.isNaN(n) || n &lt; 0) {
    return 0                // 不是数、是负数，都按 0 算
  }
  return Math.floor(n)
}

let tags: string[] = '学习,运动,睡觉'.split(',')
let line: string = tags.join(' · ')   // '学习 · 运动 · 睡觉'
```
:::

来自输入框、网络、存储的字符串一律先验证再转换：Number('') 是 0，Number('12abc') 是 NaN，这两个边界记牢。split 按分隔符拆成数组，join 反向拼回字符串。一对搭档处理逗号分隔的数据非常好用。模板字符串（反引号加 ${}）也在，拼长字符串比加号清爽，该用就用。

##### 引用还是副本：新手第一大坑

::: div .code-block
:::inline div .code-head
<span>ARKTS · 赋值赋的是地址</span><span class="dots">···</span>
:::

```
let a: number[] = [1, 2, 3]
let b: number[] = a          // b 和 a 是同一个数组
b.push(4)
console.info('' + a.length)  // 4！a 也"变"了

let c: number[] = a.slice()  // 复制一份新的
c.push(5)
console.info('' + a.length)  // 还是 4，a 安然无恙
```
:::

对象和数组赋值时传的是"地址"，不是内容——b 和 a 拿到的是同一个柜子的钥匙，b 往里塞东西，a 打开柜子当然也看得见。想复制：数组用 slice() 或 concat()；对象逐字段新建一个；对象里还嵌着对象时，浅拷一层不够，嵌套字段指向的还是旧地址，要写个 clone 函数逐层新建。这个坑在"我明明改了数据，界面怎么没动"一类问题里是常客，第 73 章讲状态管理时，你还会和它打照面，先混个脸熟。

#### 十七、自测：十二道题检查你学没学会

合上书答一遍。答不上来的，回对应小节再看一遍再答，这一步比继续往下读有用得多。每题后面的"考点"是自查用的，别先偷看。

<strong>第 1 题</strong>：<code class="inline">const arr: number[] = []</code> 之后还能 <code class="inline">arr.push(1)</code> 吗？<br>考点：const 与 readonly 的分工。能。const 只锁"变量名不能指向别的东西"，不锁内容；要连内容都锁，用 readonly。

<strong>第 2 题</strong>：把 <code class="inline">{ name: '阿黄' }</code> 直接赋给一个没标类型的变量，行不行？<br>考点：字面量的类型归属。不行。先声明 interface，让字面量"有类型可归"，再赋值。

<strong>第 3 题</strong>：两个 interface 字段完全一样，变量能互相赋值吗？<br>考点：结构化类型。不能。字段相同不等于同一个类型，共用一个定义，或写显式转换函数。

<strong>第 4 题</strong>：<code class="inline">catch (e: Error)</code> 为什么报错？<br>考点：catch 的类型规矩。catch 参数禁止标注类型。写成 catch (e)，进去之后用 instanceof 收窄，系统 API 的错误按 BusinessError 约定转换。

<strong>第 5 题</strong>：async 函数的返回类型怎么标？<br>考点：异步函数签名。一定是 Promise。没有返回值就写 <code class="inline">Promise&lt;void&gt;</code>，有返回值写 <code class="inline">Promise&lt;T&gt;</code>。

<strong>第 6 题</strong>：想运行时给对象临时加个新字段，怎么办？<br>考点：对象形状不可变。字段预先声明在 interface 或 class 里，哪怕初始值是空的；键要到运行时才知道的，用 Record 或 Map。

<strong>第 7 题</strong>：find 取不到时拿到什么？用之前该做什么？<br>考点：可空值的处理。拿到 undefined。先判断再用，或者用 instanceof/收窄逻辑兜底，别直接拿去算数。

<strong>第 8 题</strong>：sort 不传比较函数会怎样？<br>考点：排序的默认行为。元素会被当字符串排，数字数组会乱序。比较函数永远写上，一行省半天。

<strong>第 9 题</strong>：把方法从类里"摘下来"当回调传出去，会丢什么？<br>考点：this 的绑定。this 会丢。要么用箭头函数包一层再传，要么把这段逻辑写成不依赖 this 的纯函数。

<strong>第 10 题</strong>：<code class="inline">let b = a</code> 之后改 b，a 跟着变，为什么？<br>考点：引用与副本。赋值传的是地址不是内容。数组用 slice()/concat() 复制，对象逐字段新建，嵌套结构要逐层拷。

<strong>第 11 题</strong>：<code class="inline">import './init'</code> 为什么不让用？<br>考点：模块化的显式原则。副作用导入被禁。改成 init 模块导出初始化函数，在入口显式调用，执行路径一眼可查。

<strong>第 12 题</strong>：把一个普通 object 塞进 @State，改了属性界面不刷新，为什么？<br>考点：可观察类型。ArkUI 只观察 boolean、string、number 及其数组、class 实例这些可观察类型。把数据改成 class 实例再看——细节在第二节和第 73 章。

对了几个不重要，错了哪几道才重要：每道错题背后是一节要重看的内容。全部答对也别急着骄傲，语言是练出来的，不是读出来的。给你三个本周练习，难度递增：

- <strong>练习一</strong>：给十四节的 Ledger 加一个 findByName 方法，返回 <code class="inline">DebtRow | undefined</code>，自己写三个用例测它：人在账上、不在账上、同名多笔。
- <strong>练习二</strong>：给 stats.ets 加一个 topThree 函数，返回欠款最多的三个人名（排序加 slice 就够），注意别把原数组排乱。
- <strong>练习三</strong>：打开 DevEco 的工程模板，把页面文件里每个 @ 开头的标签认一遍，口头说出它是"标记入口""标记组件"还是"标记状态"，认不全没关系，第 73 章会逐个讲透，现在脸熟就行。

做完这三个练习，你对这一章的掌握就不止于"看懂"了。语言层的学习到这儿可以画句号，剩下的精进都在真实项目里发生。

#### 十八、常见误区：四个"我以为"

最后把初学者最顽固的四个误会集中拆一遍。它们的特点是"听着还挺有道理"，所以单独拎出来说。

<strong>误区一：我以为报错越少，说明我代码写得越好。</strong><br>其实恰恰相反。在 ArkTS 里，主动制造报错是最快的学习方式——第十三节那个"来动手"让你故意写 any、故意标错 catch 类型，就是为了让你在没人催的时候熟悉报错的脾气。报错面前不用慌，它说的是"这里要改"，不是"你不行"。

<strong>误区二：我以为 private 只是写给同事看的注释。</strong><br>其实它是编译器执行的硬规矩。字段标了 private，任何外部代码碰它都直接编译失败——注释靠自觉，private 靠机器。同理 readonly、接口签名，这些"看起来形式化"的东西，全是把口头约定升级成机器执法。

<strong>误区三：我以为用了 async/await 就不会卡界面。</strong><br>其实 async/await 只是换了一种"等"的方式：网络、磁盘这类等待确实不占主线程，但纯计算的活儿——解析几 MB 的 JSON、图片压缩——await 一样把主线程按住，界面照样卡。重活儿的出路是 Worker/TaskPool 那套多线程方案，后面的章节会讲。

<strong>误区四：我以为类型标注是重复劳动，编译器明明推得出来。</strong><br>其实在 ArkTS 的规则下，显式类型不是劳动，是燃料：编辑器补全靠它才精准，报错靠它才能提前到编译期，重构时"改一处、全线报警"也靠它。你在 JS 里靠推断省下的几分钟，都会变成将来排查"运行时怎么是 undefined"的几小时。

练习节奏上再给一个可以照做的安排：每天固定 30 分钟，前 20 分钟敲代码，后 10 分钟只做两件事，读报错、查文档。敲的部分别贪多：把当天学会的一个写法用上三次，比把三个写法各用一次记得牢。如果某天实在没状态，就把十四节的 Ledger 打开随便加个小方法。保持手感比推进进度重要。那 10 分钟是复利所在：今天多认识一个报错码，将来某个赶工的深夜就少熬一小时。

还有一个小习惯，建议从今天就开始：每解决一个报错，就在那行代码旁边留一句注释，写清楚"当时为什么错、怎么改的"。不用工整，一句话就行。两周之后回头翻，这本散落在代码里的"错题本"，会比任何教程都贴合你的实际，里面每一个字，都是你亲手踩出来的坑。等代码量上来，你会感谢它：不是你犯过的错，是你已经跨过的坑。

遇到实在解决不了的报错，提问也有姿势：把报错码、十行以内的最小复现代码、你期望的行为和实际行为这"三件套"贴全，别只丢一句"它报错了"。三件套给全，别人三十秒就能帮你看出问题；只丢一句话，大概率等来的是沉默。官方社区和论坛也吃这一套，完整的提问往往能直接换回改好的代码，而不是来回追问三轮。这个习惯在团队协作里同样是硬通货：会描述问题的开发者，走到哪里都不缺帮手。

至于"什么时候算学会"，有个朴素的标准：当你写新功能时，第一反应是"先定义 interface"；报错弹出来时，第一反应是"读码、查文档"，而不是随手 as 一下绕过去。不用别人告诉你，你自己会感觉到那个瞬间。到了那时，这一章的任务就真正完成了。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-quote-left mr-2"></i>一句话记牢

{class="mt-1"}
ArkTS 的所有规矩，都是在替未来的你省排查时间。
:::

到这里，语言这一章的全部内容就齐了。你已经能读懂模型层的代码、看懂报错、把逻辑拆进合适的文件。下一章把这些零件装进界面，装饰器们会在那里正式开工。

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- ArkTS 保留 TS 核心：类型、接口、类、泛型、箭头函数
- 六条收紧：禁 any、形状固定、无结构化类型、渲染类型受限、类型写全、字面量要有类型
- 报错码 arkts-no-xxx 可直接查官方适配规则页
- 装饰器是状态管理骨架：@Entry/@Component/@State/@Prop/@Link/@Watch
- V1 先学扎实，V2（@Local/@Param/@Event）是进阶方向
- 把 ArkTS 当"更严格的 TypeScript"，报错是编译器在帮你
:::
