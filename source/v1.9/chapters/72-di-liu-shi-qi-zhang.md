---
id: di-liu-shi-qi-zhang
num: 67
part: ios-kai-fa-pian
nav: 第六十七章：打磨与发布——上架App Store
toc: default
kind: chapter
---

### 第六十七章：打磨与发布——测试、调试与上架 App Store

{class="chapter-intro mb-4"}
App 做出来了，然后呢？这一章回答"从能跑"到"能交付"的三件事：怎么高效地调试找 bug、怎么写测试防回归、怎么把 App 送上 App Store 让全世界下载。上架不只是仪式感——它是把一个作品变成产品的分水岭。本章操作以 Xcode 26 / Swift 6.2 为准，工具年年更新，界面细节以你手上的版本为准。

#### 一、调试三板斧：print、断点、预览

抓 bug 是写码人的日常：模拟器里好好的，真机一跑就崩；明明只改了一行，坏的是另一行；凌晨一点想睡，bug 偏在这时候冒头。这一节把 Xcode 里最顺手的调试手段按"上手顺序"排一遍，从 print 一路讲到视图调试——读完之后，至少把"满屏 print 靠猜"这个习惯换掉。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">工具</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">干什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">怎么用</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">print + 控制台</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">看运行日志</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">代码里 print("值=\(x)")，Xcode 底部控制台看输出</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">断点调试</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">让程序停在某行，看变量值</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">行号旁点一下出蓝标，运行到那里暂停，逐步走</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI 预览 + 调试器</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">实时看界面与视图层级</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">#Preview 画布 + 运行时的 View Hierarchy 检查器</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
调试三板斧

##### print：最顺手的，也是最浅的

print 是所有人学会的第一个调试工具，也最容易被滥用。它的问题不在"能不能用"，在效率：每加一条 print 都要重新跑一遍程序，让执行流自己撞上去；日志一多，控制台就是一场雪崩，真正想看的那行淹没在里面。它的适用面其实很窄——快速确认"这行代码执行到了没有""这个值大概是不是我想要的"。

三个小习惯能让 print 好用不少。一是把上下文带进日志里：<code class="inline">print("提交金额=\(amount)，分类=\(category)")</code> 比光秃秃一个数字，半个月后还能看懂；二是加统一前缀，控制台右下角的过滤框输入前缀，只显示你自己的输出，系统日志全被滤掉；三是调试完顺手删，或者用 <code class="inline">#if DEBUG</code> 包起来——上架的正式包里 print 照样会执行，字符串照样在拼接，循环里成千上万次地拼，纯属白烧性能。

print 放的位置也有讲究：打在"决策点"附近（条件判断前后、函数入口出口），别打在"噪音区"（循环体内每一圈都打一遍的除外——那叫刷屏）。一条好日志回答"此刻系统做了什么决定"，而不是"此刻代码执行到了第几行"——后者是断点的工作，别让 print 抢活。

顺带一提，SwiftUI 里往 body 里塞 print 是个特殊的坑：视图会被系统反复重算，一行 print 能刷出满屏重复日志。反过来这也是个野路子诊断法——某段代码的 print 疯狂重复，说明这个视图在被反复重算，多半是状态设计有问题。更正规的查法在本章第六节的剖析器里。

再往上一步，系统还准备了更正式的日志方案：os 框架里的 Logger，可以给日志分级别（调试、信息、错误）、分门别类，用系统自带的日志工具集中过滤查看。新手阶段 print 完全够用，但知道有它——等 App 需要在用户设备上留下"可回收的日志"时（比如帮用户排查问题），就该换装备了。日志分级的思想值得提前学：别把所有输出都当"普通打印"，哪些是调试细节、哪些是业务关键动作，从第一天就分清楚，后面接日志框架才不会乱成一锅粥。

Mac 上还有个"控制台"App（在"实用工具"里），连着真机可以翻看设备的系统日志。print 的输出要在 App 连着 Xcode 运行时才能看到；用 Logger 写的日志则能在这里按 App 名过滤翻到。给爸妈远程排查问题时，让他们装一个带 Logger 的调试版本、你在自己电脑上看日志——这条远程排障的路，很多家庭用过。

##### 断点：让时间停下来给你看

断点是 print 的完全体：程序跑到那一行整体暂停，此刻所有变量的值都摊开给你，还能一步一步往前走，看着状态怎么变。用法一句话：点行号左边的空白处，出现蓝色小箭头就是断点；⌘R 运行，程序停在那里，Xcode 自动切到调试区。

停住之后先看两块地方。左边是<strong>调用栈</strong>：程序是怎么一步一步走到这里的，从下往上是"谁调用了谁"；下面是<strong>变量面板</strong>：当前作用域里每个变量的值实时展示，数组和字典可以直接展开看。工具栏上四个小按钮控制节奏：继续（一路跑到下一个断点）、单步跳过（执行完当前行，停到下一行）、单步进入（钻进这行调用的函数内部）、单步跳出（把当前函数执行完退出来）。建议新手先单步跳过走几行，盯着变量面板的变化找手感；确认问题藏在某个函数内部时，再单步进入。

单步走读还有个附加价值：它是最快的"读代码"方式。接手一段看不懂的逻辑，别干瞪眼，打个断点单步走一遍，变量的来龙去脉全在眼前——很多人读完开源项目靠的就是这招，慢即是快。

还有个特别顺手的动作：程序停在断点上时，把鼠标悬停在代码里的变量名上，会弹出小窗显示当前值。很多问题不用去面板里翻，悬停两秒就破案了。

断点还有个"探针"用法：编辑断点的界面里除了条件，还能加调试命令（Debugger Command），比如命中时自动 po 出关键变量——相当于"到点自动报数"，不用每次停下都手敲。先用好最基础的，进阶的按需解锁。

那什么时候用 print、什么时候上断点？经验法则：要"看一段历史"（过去发生了什么），print 留痕更合适；要"看一个现场"（此刻的状态），断点一次看全。两个都试过之后你会形成自己的手感——大多数人最后是"断点为主、print 补漏"。

断点也讲究"管理"：暂时不想触发，点一下让它变灰（禁用），不用删——下次还要用；断点一多，去断点导航器（⌘8）里统一看，全部清掉也是在那里一键完成。带着一堆忘删的断点打正式包，App 会莫名地卡顿甚至闪退，后面自查清单里还会提醒你。

##### 条件断点与异常断点：专治偶现

循环跑一千次，bug 只在金额超过一千元的那几次出现——难道点一千次"继续"？不用。在断点上右键 → 编辑断点（Edit Breakpoint），在 Condition 里写一个表达式，比如 <code class="inline">amount > 1000</code>，程序只在条件成立时才停。偶现 bug 的第一杀手就是它。

写条件有两个注意点：一是变量名必须用运行时真实存在的名字，写错了条件永远不成立，断点就成了摆设；二是条件别写太"贵"——循环里每次都要算的表达式，越简单越好，不然调试器自己就成了性能负担。

另一个救命开关在断点导航器（⌘8）左下角的加号里：添加一个 <strong>Swift Error Breakpoint</strong>。它的作用是只要 Swift 抛出错误，程序立即停在抛出的那一行——而不是等你发现界面不对劲，再回头大海捞针。很多"没崩溃但行为不对"的问题，加了这个断点之后当场现形。老式异常也有对应的 Exception Breakpoint，遇到接老代码的场合记得它。

同类里还有一位：符号断点（Symbolic Breakpoint）——不给它行号，给它一个方法名，任何地方调用这个方法都会停下。适合"我知道某个函数很可疑，但不知道它会被谁在哪儿调用"的场合。加号菜单里选 Symbolic Breakpoint，名字填函数名即可。

这几个开关都是"常备药"：不是天天用，但建议现在就去加上 Swift Error Breakpoint 并留着。等哪天深夜排障，你会回来谢这一段的。

##### 断点实战：十分钟抓一个崩溃

给你还原一次完整的排障过程，感受上面这些工具怎么配合。场景：记账本点"保存"就闪退，控制台打印 "Fatal error: Unexpectedly found nil while unwrapping an Optional value"，Xcode 停在高亮的那一行——代码里是一处强制解包 <code class="inline">category!.name</code>。

第一步，别急着改。在崩溃行的上一行打个断点，重新跑，复现：程序停下来了，看变量面板，category 是 nil——原来"分类"没选也能保存，强制解包直接炸了。第二步，验证猜想：在 LLDB 敲 po category 确认是 nil；再想想业务上"没选分类就保存"合不合理——合理，那就不该崩，该提示。第三步，改代码：把强制解包换成安全写法，没选分类时弹提示并 return。第四步，补一个 UI 测试把这个 bug 钉死（不选分类保存，界面应出现提示），防止以后重犯。

整个流程十分钟，没有一步是"碰运气"。断点冻结现场、LLDB 验证猜想、测试防止复发——三件套的配合就是这么顺。下次遇到崩溃，照这个节奏走，别在控制台前干瞪眼。

崩溃现场还值得"留档"：截图控制台的报错、记录复现步骤（点了什么、当时在哪个页面、设备型号），存进你的项目笔记。下一版再遇到类似问题时，这份档案就是破案卷宗——排障最怕的不是难，是同样的坑掉进去两次还没记性。

##### LLDB：停下来的那一刻，你有个"万能终端"

程序停在断点时，底部控制台的左半边其实是一个完整的调试器命令行，名叫 LLDB。图形按钮能干的它都能干，还能干更多。五个命令先记住，用时对着敲：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">命令</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">干什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">什么时候用</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">po 变量名</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">打印对象内容</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">看数组、字典、对象的实际内容</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">p 表达式</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">求值并显示结果</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">快速算一下某个表达式的值</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">expression 变量 = 新值</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">运行中改值</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">试一条分支走不走得通</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">bt</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">打印调用栈</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">崩溃分析、看"怎么走到这里"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">continue</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">放行，继续运行</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">验证完让程序继续跑</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
LLDB 五个入门命令

举个真实场景：程序停在 parseAmount 里，你在 LLDB 敲 <code class="inline">expression input = "12.5"</code>，然后 continue 放行，看看后面的分支是不是按新值走——相当于"边开车边换轮胎"，很多逻辑问题几十秒就能验证，比改代码重新编译快一个量级。bt 则在分析崩溃时高频出场：从最上面一帧往下读，第一帧是崩在哪，第二帧是谁调的，现场的来龙去脉一目了然。

LLDB 对新手很友好：敲错命令它会提示正确姿势，表达式有补全，大胆试错即可。调试快捷键也顺手记下——单步跳过、进入、跳出默认绑在 F6、F7、F8 上（以 Xcode 菜单显示为准），手不离键盘地走代码，节奏快很多。

##### 崩溃报告入门：认识几个"惯犯"

崩溃信息里反复出现的几类名称，先混个脸熟——它们是崩溃界的惯犯，各有各的作案动机：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">崩溃类型</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">什么意思</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">常见原因</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">EXC_BAD_ACCESS</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">访问了不该访问的内存</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">已释放的对象还在被用、野指针</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">EXC_BREAKPOINT</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift 运行时强制失败</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">强制解包 nil、数组越界、强制转换失败</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">EXC_RESOURCE</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">CPU 或内存超额被系统终止</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">无节制的大图、无限增长的缓存</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">启动超时被杀</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">主线程卡太久触发看门狗</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">启动路径上塞了网络或重计算</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
常见崩溃类型速查

三条通用读法：看第一行原因，看出错的行号，看调用栈最上面几帧。真机上的历史崩溃去 Organizer 的 Crashes 页看——那里还能看到崩溃发生的机型与系统版本分布，"只在某款老机型上崩"的线索往往就藏在这里。第三方崩溃 SDK 的报告结构大同小异，学会苹果这套，别的触类旁通。

读崩溃报告还要防一个误区：别只看崩溃点的最后一帧就下结论。真正的原因常常在几帧之前——比如崩溃在数组取值，根源却是上游把空数组传了进来。往上翻几帧，把"谁传进来的"找到，才算真正结案。

##### 视图调试：界面出了问题，问界面自己

逻辑层的 bug 问变量，界面层的 bug 得问界面。写 SwiftUI 时，第 62 章用过的预览画布不只是看效果：画布左下角的调试按钮能让预览真的跑起来点一点，改一行立刻刷新。遇到"预览好好的、真机不对"，就在运行时抓一张界面快照：菜单 Debug → View Debugging → Capture View Hierarchy，Xcode 会把当前界面完整层级抓下来，变成一张可以旋转、可以逐层点开的立体图——哪个按钮实际被挡住了、哪个元素跑到了屏幕外、透明层叠了多少张，一眼看穿。"为什么点不动""为什么多了一条缝"这类问题，这招几乎是必杀。

SwiftUI 的报错也值得读：控制台里那些红字往往直接把问题写明白了——缺修饰符、状态用错地方，红字第一句就是答案。别跳过报错，读懂报错的人学得最快。

视图调试还有个更轻量的入口：预览画布。预览右下角的诊断选项可以直接展开 SwiftUI 的视图层级，不用跑完整 App。调试"为什么这个 padding 怪怪的""两个元素为什么重叠"这类小问题，预览里就能解决大半——画布是 SwiftUI 时代的第一现场，别总是绕道模拟器。

同一个"Open Developer Tool"菜单里还有一位亲戚值得认识：无障碍检查器（Accessibility Inspector）。它能逐个检查界面上元素的标签是否可读、顺序是否合理——第 65 章做无障碍时用过的"旁白"，在这里能提前做自动化体检。界面 bug 和无障碍问题，很多时候是同一个问题的两种症状。

##### 模拟器与真机：环境本身就是变量

调试时别忘了"环境"这个最大的变量。模拟器的优势是快：假定位可以随便设（模拟器菜单里直接给"当前位置"填一个别的城市，调试定位功能不用真的出门）、动画放慢了看（调试菜单里的慢速动画）。但性能、传感器、推送、蜂窝网络切换、真实电量，这些只有真机才诚实——模拟器上流畅的列表，老款真机上可能一滑就掉帧。

实用搭配是"七三开"：七成时间在模拟器上快速迭代界面和逻辑，三成时间在真机上验证手感、性能和权限。到上架前，本章第六节的自查清单会要求你用真机把核心流程再过一遍。

再补一个真机调试的冷知识：真机的"开发者"设置里藏着几个调试利器——比如人为把网络调成慢速或断流，专门用来测弱网体验。发布前用最差网络跑一遍核心流程，你会看到另一个 App：加载要兜底、失败要提示、重试要顺手，这些只有弱网才暴露。

环境不对劲时还有一套"急救三步"：先 Product → Clean Build Folder 清一遍构建产物；再把模拟器里的 App 删掉重装；还不行就重启 Xcode。这三步组合拳解决的是"玄学问题"——代码没改却突然编译不过、界面和代码对不上，多半是构建缓存闹脾气。先清缓存再怀疑人生，是老手的次序。

##### 新手调试三宗罪

<strong>罪一：满屏 print 靠猜。</strong>两百条日志里用眼神定位变量，找到眼花还没找到。纠正：先上断点把"案发现场"冻住，变量面板一次看全；print 只留给确实需要跨多次运行对比的场景。

<strong>罪二：只看报错最后一行。</strong>看到 Build Failed 就开始瞎改。纠正：从第一条报错读起，后面的错误常常是第一条的连锁反应；改一处，重新构建一次，别一口气改五处再编译——坏了都不知道是哪一改。

<strong>罪三：不存档就大改。</strong>修到一半想回到上午那个好使的版本，发现 git 里根本没提交过。纠正：每完成一个小功能就提交一次，改坏了随时退回。调试的底气，一半来自版本控制。

<strong>罪四：复现步骤说不清楚。</strong>"有时候会崩，你试试就知道了"——这样的 bug 报告连自己都没法接手。纠正：每次发现异常，当场写下复现步骤（操作路径、数据状态、设备与系统版本），复现不了的 bug 才值得贴"偶现"标签。能把 bug 稳定复现，问题就解决了一半。

##### 调试工作流：从"看到异常"到"修复落地"的地图

把这一节串成一张地图：用户报告或你自己发现异常 → 先读报错与日志（定位到"哪一层"出事：数据、逻辑还是界面）→ 用断点或视图调试冻结现场（确认"此刻的状态"）→ 用 LLDB 验证猜想（改个值试试分支）→ 改代码 → 补测试防复发 → 手动回归一遍。每一步都有现成工具，别跳步——最贵的弯路就是"还没定位就开改"。

心态也说一句：bug 是信息，不是失败。每一个 bug 都在告诉你系统某个假设错了，修好它，你的模型就又准了一点。凌晨两点抓到 bug 的沮丧是真实的，但第二天早上回想，那通常是你当天学得最多的两个小时。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：崩溃了怎么读？

{class="mt-1"}
Swift 崩溃时控制台会打印 "Fatal error" 加原因，Xcode 会停在出错那一行并高亮。真机上的历史崩溃可以在 Xcode → Window → Organizer → Crashes 里看（需付费账号）。关键词优先搜 <strong>"错误原因第一句 + swiftui"</strong>——精确的问题，才有精确的答案。
:::

#### 二、测试：给代码上保险

手测靠不住——改了这个功能，另一个悄悄坏了。测试就是"后悔药"兼"防弹衣"。iOS 用 <strong>XCTest</strong> 框架，分两种：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">层级</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">测什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Target</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">速度</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">单元测试</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">纯逻辑（计算、校验）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppTests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">秒级</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UI 测试</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真实界面行为</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppUITests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分钟级</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">手动测试</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真人感受、体验</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">永远需要</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
iOS 测试层级（模板项目已预置两个 Test Target）

::: div .code-block
:::inline div .code-head
<span>SWIFT · 单元测试示例</span><span class="dots">···</span>
:::

```
import XCTest

// 把"金额字符串转数字"这种逻辑抽成纯函数
func parseAmount(_ input: String) -> Double? {
    guard let v = Double(input.trimmingCharacters(in: .whitespaces)),
          v > 0 else { return nil }
    return v
}

final class AmountTests: XCTestCase {
    func testEmptyInputReturnsNil() {
        XCTAssertNil(parseAmount(""))
    }
    func testNegativeReturnsNil() {
        XCTAssertNil(parseAmount("-5"))
    }
    func testNormalValueParses() {
        XCTAssertEqual(parseAmount("12.5"), 12.5)
    }
}
```
:::

跑测试：<kbd>⌘U</kbd>。全绿之后再改代码，心里有底。记账本里的金额校验、汇总计算，都该有单元测试罩着。

##### 一个测试长什么样：三段式

上面那个例子值得亲手抄一遍，再补一个"写作套路"：一个测试分三段——<strong>准备</strong>（把要用的数据和对象造出来）、<strong>行动</strong>（调用要测的那个函数）、<strong>断言</strong>（检查结果对不对）。parseAmount 的三个测试全是这个结构，你以后自己写测试也照这三段搭骨架，思路不会乱。

命名也有讲究：testNormalValueParses 这种"测什么 + 期望什么"的写法，失败时扫一眼就知道哪条规则挂了。断言函数常用的就几个：XCTAssertEqual（相等）、XCTAssertTrue / False（真假）、XCTAssertNil（为空）、XCTAssertGreaterThan（大于）。够用了，别贪多——测试是写给三个月后的自己看的，那时你已经忘光了上下文。

断言还能带一句自定义消息：XCTAssertEqual(实际值, 期望值, "金额汇总应只含支出")。失败时控制台会先报数值差异、再显示你的那句话——将来排查时，这句"人话"比一串数字更快让人进入状态。写测试时多敲这半行代码，未来感谢你的还是你自己。

测试代码也要讲究"隔离"：一个测试只验一件事，测试之间互不依赖、先后顺序无所谓。如果跑测试必须先跑另一个测试垫数据，那不是测试，是连环坑——XCTest 默认会打乱执行顺序来帮你暴露这种依赖。

测试文件从哪来？不用从零建：模板项目已经预置了两个测试 target（表格里那两个），对应文件夹里各有一个带示例的模板文件，照着改就行。以后加新测试，就在同一个文件夹里新建文件、类名对齐"被测对象 + Tests"，找起来不乱。

##### 该测什么，不该测什么

新手容易走两个极端：一个是不写测试（"我手动点点就行了"），一个是啥都想测（连按钮颜色都断言一遍）。合理的分界线是：<strong>纯逻辑必须测，核心交互选着测，视觉细节别测</strong>。

优先给这几类写测试：金额计算与汇总（算错就是真金白银的事）、字符串校验与格式转换、日期边界（月末、闰年、跨年）、存取层的增删改查。这些地方出 bug 代价高，测试又好写，投入产出比最高。对照第 65 章的记账本：汇总卡片那个"本月支出"的计算，就是头号该测对象。

还有一个容易漏掉的测试对象：数据迁移。第 64 章的 SwiftData 模型以后加了字段，老用户升级后旧数据还在不在、格式对不对——这类问题手测很难覆盖全，自动化测试能一次性把"旧数据进、新版本出"的链路验干净。上架前自查清单里那遍"真机冷启动"，一半价值就在这里。

反过来，"没法测"本身也是个信号：如果一个函数写不了测试，多半因为它把网络请求、数据库读写、界面更新搅在了一起。这正是下一章要讲的协议抽象与依赖注入要解决的问题——可测试性是设计出来的，不是硬测出来的。

##### 写不出测试的代码怎么办：先分离，再测

"这个函数没法测"的解法通常是把它拆开。看一个反面教材：求"本月支出"的函数长这样——先读数据库，再算总数，最后顺手更新了界面上的标签。三件事挤在一个函数里，想测它就得先搭好数据库再搭好界面，谁都会嫌麻烦，测试永远排不上日程。

拆法固定两刀：把"读数据"留在数据层，把"算总数"抽成纯函数——输入一组记录，输出一个数字；界面更新交给调用它的人。拆完之后，纯函数一句断言就测完了，数据层另测，界面用 UI 测试抽查。这个"把计算从读写里剥出来"的手法，是新手从"没测试"走向"有测试"的关键一步，也是下一章协议抽象的前置功。

##### UI 测试：让机器人替你点一遍

单元测试管逻辑，UI 测试管"人机交互的真实链条"：点这个按钮、输入这些字、界面上该出现什么。它跑得慢（分钟级），数量要克制，但两类场景值得写：核心流程（记一笔 → 列表里出现这条），和曾经修过的 bug——写个测试把它钉死，防止下次改代码旧病复发。这种"防复发测试"有个形象的名字叫回归测试，是 UI 测试里最值钱的一类。

写 UI 测试前，先给要找的控件挂个"门牌号"——accessibilityIdentifier，机器人才能稳定找到它（顺便说一句，这个标识同时也是给"旁白"读屏用的，一举两得）：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 给控件挂门牌号</span><span class="dots">···</span>
:::

```
TextField("金额", text: $amount)
    .accessibilityIdentifier("amountField")
```
:::

然后在 UITests target 里写机器人脚本：

::: div .code-block
:::inline div .code-head
<span>SWIFT · UI 测试示例</span><span class="dots">···</span>
:::

```
import XCTest

final class MyFirstAppUITests: XCTestCase {
    func testAddRecordShowsInList() {
        let app = XCUIApplication()
        app.launch()                              // 启动被测 App
        app.buttons["记一笔"].tap()                // 点"记一笔"进录入页
        let field = app.textFields["amountField"]
        field.tap()
        field.typeText("12.5")                    // 机器人替你打字
        app.buttons["保存"].tap()                  // 保存
        XCTAssertTrue(app.staticTexts["12.5"].waitForExistence(timeout: 3))
    }
}
```
:::

⌘U 一按，你会看到模拟器自己动起来：光标自己点、自己打字，第一回看挺魔幻，习惯就好。示例里那句 waitForExistence 是个好人：给它几秒耐心等界面刷新，比一秒都不等就断言稳定得多。UI 测试失败的排查顺序是：先确认控件有没有挂门牌号，再确认模拟步骤跟真人操作一致（先 tap 聚焦再 typeText），最后才怀疑代码逻辑。

UI 测试还要防一个捣乱分子：系统弹窗。测试跑到一半弹出"是否允许通知"，后面的步骤全找不着北——这类场景系统提供了"中断监控"机制（测试代码里注册一个监控器，弹窗出现时自动处理）。新手阶段遇到得少，先知道有这回事：UI 测试不是失败在业务逻辑上，十有八九是环境出了岔子。

条数上给个参考：核心流程一条、高频操作一条、曾经的 bug 一条，就这个量级起步。UI 测试的价值在"稳"不在"多"——三十条动辄超时误报的 UI 测试，比五条全绿的更伤团队信心。

表格里第三行"手动测试：永远需要"也别忘了——测试再全，"这个界面顺不顺手""这段动画舒不舒服"只有真人知道。自动化管"对不对"，人管"好不好"，两条腿走路才是完整的质量观。定期把真机掏出来从头玩五分钟，是手动测试的最低配。

##### 异步代码怎么测

涉及网络和等待的代码，测试起来多一层：结果不是立刻回来的。现代写法已经简单了很多——测试函数本身声明成 async，直接 await 那个调用，断言照写。Swift Testing 对此是天然支持：

::: div .code-block
:::inline div .code-head
<span>SWIFT · async 测试</span><span class="dots">···</span>
:::

```
import Testing

struct CityLookupTests {
    @Test func knownCityReturnsResult() async throws {
        let result = await WeatherService.lookup(city: "北京")
        #expect(result != nil)
    }
}
```
:::

但注意一个坑：上面这种测试真的去连了网——不稳定，也慢。正式项目里应该测"逻辑"而不是测"网络"：把网络层也抽象成协议，测试时注入一个"永远返回假天气"的假实现，测试就稳定成毫秒级。做法和下一章的依赖注入一模一样——到时候你会发现，"可测试"和"好架构"是同一件事的两面。

异步测试还有个经典的坑要提防：忘了 await。少写一个 await，断言比对的可能是"还没完成的任务"，结果时对时错——这种"薛定谔的绿"最磨人。规则记一条：测试里出现的每个异步调用，前面都要有 await，一眼扫过去全有，才许提交。

##### 跑测试的姿势：只跑一个，也只看一个

全套测试不必每次都跑。测试导航器（⌘6）里，每个测试方法旁边有个小菱形按钮，点它只跑这一个——改了金额校验就只跑金额那组，几秒钟出结果。测试失败时，问题导航器（⌘5）里会列出哪条断言挂了、期望值和实际值各是多少，点进去直接定位到行。

跑完的报告也值得点开看一眼：哪些测试跑得慢、哪些经常红，都是信号。慢的测试通常在偷偷做重活（读真数据库、连真网络），常红的测试通常是依赖太多——它们都在暗示你的架构还有改进空间。

测试多了之后，用"组"管理：同一个功能相关的测试放同一个类里，类名前缀一致（比如 AmountTests、SummaryTests），测试导航器里就自然分组。找测试像找文件一样有规律，维护成本就低。

一个来自实战的节奏：写完一个功能，先手动点一遍确认大方向，然后立刻补两三条测试钉住边界，再 ⌘U 全跑一遍。测试跟代码一起长大，比"功能全写完再补测试"省力得多——后者面对几百行代码，补测试的热情通常撑不过一个晚上。

##### 测试不是越多越好：三条纪律

纪律一：测行为，不测实现。断言"输入 -5 返回 nil"，而不是断言"内部调了两次字符串处理"。前者重构后依然成立，后者一重构就碎——碎掉的测试只会教坏你。

纪律二：每个 bug 修完，留一个测试。bug 被修掉的同一个提交里带上复现它的测试，这个 bug 从此就被测试拦在门外了。这是防复发最便宜的保险。

纪律三：红了必须当天处理。测试失败放着不管，三天后你自己都会对满屏红字视而不见——测试的生命力在于"绿是常态"。做到这三条，测试是资产；做不到，测试是债务。

##### 测试当草稿纸：另一种打开方式

测试还有一个被低估的用途：当"实验田"。想试试某个字符串 API 的行为、某个日期格式化到底输出什么？别在 App 里改来改去，写个临时测试函数，把 API 调一遍、断言打上去，跑一下就出答案。比在真机上反复点 App 快，也比靠记忆猜靠谱。实验完了删掉，或者留着当文档——一个写得好的测试，读起来就是这份 API 的使用说明书。

##### Swift Testing：Xcode 16 起的新方言

XCTest 用了十几年，苹果又拿出了新框架 <strong>Swift Testing</strong>（Xcode 16 起可用，Swift 官方开源项目）。它不取代 XCTest——同一个项目里两者可以共存，旧的照跑，新的用新写法。它好在三件事。

一是写起来轻：@Test 一标就是一个测试，断言用 #expect 宏，不用再记 XCTAssert 家族那一串名字；失败时它会把表达式里每个变量的值都打印出来，一眼看出哪不对。

二是参数化测试：一个校验函数配十组非法输入，XCTest 得写十个方法，Swift Testing 一行搞定——把输入列在 arguments 里，框架自动每组跑一遍：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 参数化测试</span><span class="dots">···</span>
:::

```
import Testing

struct AmountValidationTests {
    @Test(arguments: ["", "  ", "-5", "abc"])
    func invalidInputsReturnNil(input: String) {
        #expect(parseAmount(input) == nil)
    }
}
```
:::

三是天生并行：默认同时跑多个测试，套件越大越快出结果；也天然支持 async 测试函数，和 Swift 并发配合没有历史包袱。

迁移成本也低：现有 XCTest 项目不用推倒重来，新写的测试用新框架、旧的继续跑，等哪天顺手了再逐个改写。很多大项目正是这样"新旧并存"过渡的——工具的进化从来不是急转弯。

给你的建议和签名那节一个逻辑：新手直接学新写法，老教程、老项目里的 XCTest 也要看得懂——它们是同一种思想的两种方言，三段式、断言、隔离这些原则完全通用，只是语法肌肉记忆不同。本书后面的示例两种都会出现，见到不慌。

##### 收官清单：记账本该有的八条测试

把这一节落成一张可执行的清单，对照着给记账本配齐（用 XCTest 或 Swift Testing 都行）：

- 金额校验：空串、负数、正常值（上面示例已经覆盖）；
- 金额校验：前后空格、"12.5.3"这类非法格式；
- 汇总计算：只有收入的月份，支出为零；
- 汇总计算：跨月边界——上月最后一笔不算进本月；
- 分类统计：未知分类不进统计、不崩溃；
- 存取层：存进去一条，能按日期查出来；
- UI：记一笔 → 列表出现这条（核心流程回归）；
- UI：金额为空点保存，出现提示而不是闪退。

八条全绿，你的记账本就有了"防弹衣"。以后每次改代码，⌘U 一按，三十秒知道有没有改坏东西——这就是测试给你的自由。

清单之外补两件进阶装备，知道即可：XCTest 还支持性能度量测试——把一段代码放进 measure 块里反复跑取平均耗时，给"这段代码是不是变慢了"一个客观基线；测试也可以挂在持续集成服务上，每次推送代码自动跑一遍。单人小项目先不折腾这些，等测试数量过五十条、你开始记不清谁罩着谁的时候，再来解锁。

测试也不是终身制。功能删了，对应测试一起删；两个测试重复覆盖同一条路径，合并；断言早已过时的，更新或删除。测试套件和花园一样，定期修剪才健康——满园枯枝的测试套件，跑得慢、误报多，最后没人再看它。

#### 三、签名与打包：给 App 盖上"印章"

每个 iOS App 都必须<strong>签名</strong>才能安装——证明"这个包出自你，没被篡改"。层级关系：

- <strong>学习阶段</strong>：免费 Apple ID + Xcode 自动签名（Personal Team），真机可跑，7 天续期一次；
- <strong>分发阶段</strong>：付费开发者账号（99 美元/年）签发证书与描述文件，才能上架和长期安装。

先把链路跑通，再谈精细控制：个人项目一路用自动签名完全够用，进了团队、需要管理多套证书时，再切手动——顺序别反。

真机调试的第一步也要过签名这道门：数据线连上 iPhone，手机上点"信任此电脑"，然后在 Xcode 顶部设备栏选中它——第一次会提示在开发者设置里开启开发者模式（按屏幕提示来），之后 Xcode 会自动为这台设备注册并生成描述文件。装好后手机桌面出现你的 App 图标；如果点开提示"不受信任的开发者"，去 设置 → 通用 → VPN 与设备管理 里信任一次即可。这套动作每台新设备都来一遍，走熟了两分钟搞定。

数据线也不是永久绑定的：第一次连过之后，同一网络下可以改用无线调试（设备窗口里有对应选项），以后改代码直接跑真机，不用满桌子找线。无线传输比有线慢一点，跑界面调试完全够用——"线自由"之后，真机调试的频率会明显上升。

打包：Xcode 菜单 Product → Archive（归档），构建完成后在 Organizer 里 <kbd>Distribute App</kbd> → 选 App Store Connect → 上传。<strong>归档必须选 "Any iOS Device (arm64)" 目标</strong>（旧版叫 Generic iOS Device，不是模拟器），这是新手常忘的一步。另外，每次上传的<strong>构建号（Build 号）要比上一次递增</strong>——崩溃日志就是靠它对回具体版本的，别随手乱填。

##### 签名三件套：证书、描述文件、App ID

把签名拆开看，其实是三件套：<strong>证书</strong>是你的身份证，证明这个包出自谁；<strong>描述文件</strong>（Provisioning Profile）是一张授权清单，规定这个身份的包可以装到哪些设备上、走哪条分发渠道；<strong>App ID</strong> 是应用的户口，Bundle ID 唯一标识它。三件对上了，iPhone 才肯装。听着复杂，但 Xcode 的自动签名把三件套的办理全包了：在 target 的 Signing &amp; Capabilities 里勾上 Automatically manage signing、选好自己的团队，剩下的它来办。

描述文件有"有效期"概念：免费账号的 7 天一续（上面说过的原因），付费账号的通常一年一换，基本无感。签名出问题时先别慌，看 Xcode 报错第一句——十有八九是证书过期或设备没注册，点一下报错旁边的 Fix，让 Xcode 自动处理。

查看这套东西的地方在 Xcode → Settings → Accounts：你的 Apple ID、所属团队、已生成的证书全在里面。签名出诡异问题时先来这儿"看看户口本"——团队选错了、证书过期了，当场就能看出来，比对着报错瞎猜快得多。

什么时候才需要手动签名？团队大了，证书和描述文件要统一管理（谁有发布权限、哪台机器能打包）；上架了多个 App 要分门别类；或者公司有专门的发布流水线。到那时再学手动签名也不迟——它只是把三件套的办理从"自动档"换成"手动档"，概念完全一样。新手阶段硬学手动签名，除了多踩几个坑，收获有限。

签名的行话先混个脸熟，以后读文档不卡壳：证书（Certificate）是身份文件；描述文件（Provisioning Profile）是把证书、App ID、设备/渠道绑在一起的授权清单；Team ID 是开发者账号的编号；Bundle ID 是单个 App 的唯一标识。这四个词在报错信息里出镜率极高，认得它们，报错就不再是天书。

##### 版本号与构建号：一对容易混的兄弟

Version（版本号）是给用户看的：1.0、1.1、2.0，对应"这一版有什么新东西"；Build（构建号）是给你自己和苹果看的：同一版功能下每打一个新包，构建号就往前走一格。上传 App Store Connect 时，同一个版本号配同一个构建号只能传一次——改了东西要重传，构建号必须变。崩溃日志和审核记录都靠构建号对回具体那个包，所以别跳号、别复用。

记不清上次传到几了？App Store Connect 里对应 App 的构建列表能看到全部历史。单人项目手动加一就够，别在这上面发明花活。

版本号怎么定，有个简单的民间惯例：主版本.次版本.修订号——大改版动第一位，加功能动第二位，修 bug 动第三位。用户在商店看到的是版本号，"新增功能"栏也按版本号写更新说明。构建号则老实递增就好，别把它当版本号的花样使。

##### 上传之后：构建处理的"三态"

上传完不是立刻能用：构建要经过苹果的处理，状态从"正在处理"变成"处理完成"（会收到邮件），才可以在版本或 TestFlight 里选用；处理出了问题（比如缺图标）也会邮件告知原因。新手常犯的错是传完包在后台反复刷新，发现"构建不见了"就以为传丢了——其实还在处理中。等邮件，别慌；真超过大半天没动静，再回 Xcode 检查上传日志。

处理时间受什么影响？没有公开的公式，经验上是高峰期（新版 iOS 刚发布的几周）会慢一些，平时通常在"泡杯咖啡到一顿饭"的量级。所以发版节奏要给构建处理预留时间——想周五上线，最晚周三就该传包。

##### 命令行打包：给"重复劳动"留条后路

点鼠标的 Archive 每次都是同一套动作，做多了自然会想："能不能一条命令搞定？"能。Xcode 的命令行工具 xcodebuild 支持归档与导出，不少团队用它把"打包—上传—通知测试员"整条流水线自动化。单人项目用不着，但值得知道这条路存在——等你开始每周发版，再回来研究，那时重复劳动的痛才是真实的痛。

##### Archive 前的三个检查

正式打包前花两分钟，过三个检查：设备目标选对——左上角选 "Any iOS Device (arm64)"，选成某台模拟器的话 Archive 菜单直接是灰的；Scheme 的配置是 Release——默认就是，改过的人记得切回来；断点清空——带着断点打出的包性能失真。三个检查过了再 Product → Archive，一次到位。

##### 打包产物去哪了：认识 Organizer

Archive 完成后，Xcode 会自动弹出 Organizer（也可以从 Window 菜单随时打开）——它是所有归档的"仓库"：左边是 App 与日期列表，右边是这一包的详情与分发按钮。历史归档都在，想重新上传某个旧包、或者导出一份 .ipa 文件留档，都在这里操作。崩溃报告页（Crashes）也住在 Organizer 里——前面调试一节提过的那个。花五分钟把这个窗口逛熟，上架流程里你还会回来好几次。

##### 签名报错实录：三段真实翻车

<strong>翻车一：真机突然装不上了。</strong>报错大意是找不到有效的描述文件。多半是免费账号的 7 天到期——数据线连上 Xcode 重新跑一遍就好，签名会自动续期。这不是事故，是免费账号的日常，别慌。

<strong>翻车二：Bundle ID 冲突。</strong>报错说标识符不可用。Bundle ID 在苹果体系里全球唯一，跟别的 App 撞了就换一个：反过来写的域名风格（com.你的名字.应用名）基本不会撞。

<strong>翻车三：换了 Mac 签不了名。</strong>手动管理的证书和私钥留在旧电脑钥匙串里了。这也是后面避坑盒子里"备份证书"的现实原因——不过只要你用自动签名，新 Mac 登录同一账号就能重新生成，问题自愈。

<strong>翻车四：真机上 App 打不开。</strong>装是装上了，点开就弹"不受信任的开发者"。这不是签名失败，是设备还没信任你的免费证书：设置 → 通用 → VPN 与设备管理 → 找到你的开发者 App → 点信任。免费账号每七天还会提醒你重签一次，别误以为是中了病毒。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>避坑提醒：证书丢了 = 更新断档

{class="mt-1"}
签名证书和私钥一旦丢失，你无法再给旧 App 发更新——用户只能装"全新"应用。妥善备份证书（钥匙串导出 .p12）并记好密码。好在苹果提供了"自动签名"和云证书管理（Xcode 里勾选 Automatically manage signing），能省掉大部分手工操作的坑。
:::

#### 四、上架 App Store 全流程

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> 注册开发者账号</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> 准备商店素材</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> 上传构建包</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> 填隐私与审核信息</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> 苹果审核（1-7 天）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> 上架</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
图 5：App Store 上架六步走
:::

- <strong>注册</strong>：developer.apple.com，个人账号 99 美元/年；
- <strong>先建记录</strong>：上传前先在 App Store Connect 把应用记录建好——应用名称、Bundle ID、类别、描述、截图、隐私政策各就各位，构建包才传得上去；
- <strong>素材</strong>：图标（1024×1024，别带圆角——苹果自己切）、截图（iPhone 各尺寸）、描述、隐私政策链接；
- <strong>隐私问卷</strong>：如实申报收集了哪些数据——不联网的记账本可以"不收集任何数据"；
- <strong>审核</strong>：首次提交常有 1-7 天等待，被拒就按"审核备注"逐条改——苹果的拒绝理由通常写得非常具体，照做即可。常见退回原因就那几样：崩溃、功能不完整、描述与实际不符、权限用途没写清、隐私政策链接打不开，提交前自查一遍；
- <strong>TestFlight</strong>：上传构建后先小范围发给测试员验证——内部测试最多 100 人、外部测试最多 10000 人，收集崩溃与反馈再正式提交，专业范儿十足。测试期的具体规则以 Apple 官网为准。

##### 先分清两套审核对象：二进制与元数据

提交审核的东西其实有两套：<strong>二进制</strong>（构建包，代码编译出来的那个）和<strong>元数据</strong>（商店页上你能看到的文字与图片）。二进制变了要重新 Archive 上传新构建号；元数据改了不用动包，但同样要过审核。理解这个区分，你就明白为什么"只改一句描述"也要等审核——因为在苹果眼里，商店页上的每一句话都是对用户的承诺。

隐私问卷的产出值得专门看一眼：填完后，你的商店页会多出一个"隐私标签"区块，用简洁的图形告诉用户"这个 App 收集哪些数据"。你这时是站在商店页消费者的对面——回头看一眼第 5 章教大家怎么读隐私标签，如今轮到你自己填那张表了。视角换过来，填的时候自然诚实。

##### 开工前：账号与两条硬杠杠

注册开发者账号没有捷径：developer.apple.com → Account → Enroll，选个人账号，年费 99 美元，实名信息填真实身份——后面收款、税务都挂在这上面，审核通过通常要等上一两天。想注册公司账号的，需要的组织材料以注册页面提示为准，个人练手直接选个人。

两条硬杠杠先划出来。一是<strong>工具版本</strong>：2026 年 4 月 28 日起，新 App 和版本更新必须用 Xcode 26 及以上、基于 iOS 26 SDK 构建才能上传，旧版 Xcode 的包会被直接拒收——写到这里是最新口径，每年的具体要求以苹果官方"App Store 提交要求"页面为准，升级 Xcode 这一步别拖到提审前夜。二是<strong>账号类型</strong>：上架必须付费开发者账号，免费 Apple ID 只能真机自装（7 天续期），连 TestFlight 都参与不了。

心态上再送一句：把第一次提审当成"产品体检"，而不是"大考"。审核员的备注、隐私问卷的逐项确认、截图与描述的对齐——每一项都在逼你把自己的 App 再想一遍。很多人上架后的感想是：比过审本身更值钱的，是提审前自查的过程。

##### 六步逐步走：每一步屏幕上会发生什么

对着上面的六步图，把每一步的"屏幕画面"给你提前剧透一遍：

1. <strong>注册开发者账号</strong>：付款通过后，打开 appstoreconnect.apple.com 能登录了，首页"我的 App"列表空空如也——那是你的货架，还没摆货；
2. <strong>建应用记录</strong>：我的 App → 左上角加号 → 新建 App。填名称、主要语言，Bundle ID 从下拉里选你在 Xcode 里配置的那个，SKU 随手填个内部代号。保存后你会得到一个"准备提交"状态的 App 页面；
3. <strong>填元数据</strong>：左侧导航从上往下过一遍——App 信息（类别、年龄分级问卷）、定价与销售范围、版本信息（描述、关键词、宣传文本、截图、技术支持网址）。带星号的必填，填不满的可以先留到最后一版再补；
4. <strong>隐私问卷</strong>：逐项勾选收集了哪些数据、是否用于追踪。不联网的记账本可以选"不收集任何数据"。这份问卷会变成商店页上的"隐私标签"，乱勾的后果在速查表里讲；
5. <strong>类别与分级</strong>：类别选"最像"的那个就行（记账本选财务类），它影响商店的分类列表位置；年龄分级问卷如实答，暴力、赌博、成人内容没有就选无——虚高或虚低都会被纠；
6. <strong>上传构建包</strong>：回到 Xcode，按本章第三节的路子 Archive → Distribute App。上传成功后到 ASC 的 TestFlight 页签刷新，等"处理完成"邮件；
7. <strong>提交审核</strong>：回到 App Store 页签，把构建包挂到版本上，右上角"添加以供审核"→ 提交。状态会依次变成"等待审核""正在审核"，然后是"可供销售"或"被拒绝"。

上传素材环节有两个高频小坑提前说：截图尺寸不对会被后台直接拒绝（按它给出的规格来，差一个像素都不收）；宣传图里别出现老款机型的边框——用系统提供的最新机型模板，苹果对"过时机型出镜"也会挑刺。

##### 提交之后：等待期做什么

等待审核的这几天不是干等，三件事值得做：把"技术支持网址"和反馈邮箱检查一遍——审核员有时会真的点开看；需要登录的 App，备好演示账号并写进审核备注；准备一段"新版本说明"（What's New），上架后用户第一时间看到的就是它。

同时盯紧注册邮箱：审核状态变化、构建处理结果、协议提醒，苹果的邮件往往比后台通知还快。等待期间不要再上传新构建——会重置排队，纯纯帮倒忙。想改元数据？忍到这次审核出结果。

给你一份第一次提审的参考日程：提审日，上午提交，下午开始等；第二天，大概率收到结果——通过就直接进入发布准备，被拒就当天回复 Resolution Center；第三天，改完重提或手动发布上线。第一次通常要一周上下，第二次熟练了三四天。别把发布日期定死在"提审次日"——审核排队不受你控制，留足缓冲是规矩。

##### 审核要等多久，被拒了怎么办

时间上给你一个靠谱的预期：官方口径是大约九成的提交在 48 小时内有结果，多数人体验到的是 1-3 天；赶上节假日高峰、首次上架或账号信息待补全，等更久也不稀奇——上面流程图里那个"1-7 天"就是留了余量的说法。审核通过后还可以选"自动发布"或"手动发布"，想卡某个日子上线就选手动。

被拒不是世界末日，流程是这样的：状态变成"被拒绝"，Resolution Center（解决中心）里会有一封写明条款编号和具体原因的信；你逐条回复说明，或改完代码重新上传构建再提交——重新排队，时间重新算。回复信件用真诚的短句把改动点列清楚；如果你认为苹果判错了，申诉也走这里。被个一两次很正常，苹果的拒绝理由写得具体，照着改就是最好的学习。

真有紧急情况——线上崩溃、严重 bug 必须马上修复——可以申请<strong>加急审核</strong>：App Store Connect 的"联系我们"表单里有专门入口，说明哪个版本、什么崩溃、影响多大即可。它是救火通道，不是营销工具，用多了就不好使了。

给你看看被拒信的标准长相，收到时不慌：标题带条款编号，正文一两段，写清"审核员做了什么操作、看到了什么问题"，可能附截图或视频。回复时用同样的结构：确认问题 → 说明改动 → 感谢指正。情绪化的长篇申辩没有帮助，具体、简短、有行动，才是过审最快的路径。

一个可以直接套用的回复模板："感谢指出。问题确认属实，原因是（一句话）。已做如下修改：（列 1、2、3 点）。新构建（构建号）已上传，请再次审核。"——三句话，五分钟写完，比千字小作文管用。被拒不可怕，可怕的是回复里只有解释没有行动。

##### 常见被拒理由速查表

把新手最常吃到的退回原因整理成一张表，提交前对着自查一遍：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">被拒理由</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">典型症状</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">提交前怎么自查</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">崩溃 / 严重 Bug</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">审核员一打开就闪退</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真机+模拟器过核心流程；Organizer 看历史崩溃</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">功能不完整</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">占位页、"敬请期待"、半成品界面</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">砍掉没做完的功能，别让毛坯房上货架</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">元数据与实际不符</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">截图是效果图、描述吹了没做的功能</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">截图全部来自真实运行画面</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">权限用途没写清</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用途文案是空话，或没声明就申请</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每个权限文案写清"用于做什么"，具体到场景</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">隐私问题</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">隐私政策链接打不开、隐私标签与实际不符</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">链接自测一遍；问卷如实填；隐私清单一并核对（第 68 章）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">强制注册无演示账号</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不登录啥都看不到，审核员进不去</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需要登录的 App 在审核备注里给演示账号</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">支付绕过内购</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数字内容用第三方支付收款</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">虚拟商品走内购；实物商品用普通支付没问题</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
常见被拒理由与自查方法

##### 上架后想改名字换头像？也走审核

名称、图标、描述、截图这些"元数据"的任何修改，都要重新提交审核（不用重传包，流程和首次一样）。所以商店页不是"上架那天定终身"，可以慢慢打磨——但每次改动都有排队成本，攒一批一起改是更聪明的做法。

顺带认识一个特殊字段：宣传文本（Promotional Text），出现在描述上方，它的内容更新不需要重新审核（以官方说明为准）——适合放限时活动、临时公告这类时效性内容。描述、截图、关键词这些主字段则是"改一次审一次"，两边的节奏要分清。

#### 五、商店素材怎么做：第一印象就是下载量

商店页是用户"逛店"时看到的橱窗。三个素材决定第一印象：

- <strong>图标</strong>：1024×1024，别用截图凑合。没设计能力就用 AI 工具生成一个简洁图形，<strong>在桌面上缩小后还能一眼认出</strong>才算合格；
- <strong>截图</strong>：至少 2 套（iPhone 主流尺寸），展示最核心的功能场景；每张配一句人话文案（"一秒记一笔"比"高效的记账解决方案"好十倍）；
- <strong>描述</strong>：第一句说清"这是什么 + 给谁用"，别堆砌"最专业、最强"——真诚比夸张有效。

##### 图标：过三关才算合格

第一关"缩小关"：桌面图标只有指甲盖大，你那张 1024×1024 的图缩小到桌面图标尺寸还能一眼认出来，才算过关——识别度差的图标在商店里约等于隐形。第二关"技术关"：别带圆角（苹果自己切）、别带透明背景，直角方形原图交上去就行。第三关"气质关"：一个主体图形加一个主色，比塞五个元素好得多。没设计基础就用 AI 工具生成几张候选，缩小摆在一起挑，再放到真实桌面上看一眼。

一个省事的自检法：把候选图标放进备忘录，和微信、地图、相册的图标排成一列——十秒之内能不能被找到？答案会诚实得多。

反面清单同样重要：别用照片当图标（缩小后是一团色块）、别堆文字（"记账大师专业版"塞进图标里谁也看不清）、别抄热门 App 的图形语言（用户认错、审核找茬，两头吃亏）。图标的本质是"一个能被记住的形状"，克制一点反而走得更远。

##### 截图：写给只看三秒的人

商店页的截图不是"功能证明"，是"橱窗海报"。三件事最值钱：第一张放最核心的场景——用户先看它，再决定要不要往下滑；每张配一句人话文案，前面那句"一秒记一笔"就是标准；画面干净——用真机截屏，别对着模拟器拍（模拟器画面的细节，火眼金睛的用户看得出来）。

制作流程很土但有效：真机截屏 → 加上大字文案排版 → 导出对应尺寸。排版工具随意，Keynote、PPT 都能干，别为这步买新软件。iPhone 主流尺寸各出一套是基本要求，上传时按商店后台的尺寸提示来，界面会告诉你缺哪套。

##### 描述、副标题与关键词

描述的第一句是黄金位，公式是"这是什么 + 给谁用 + 一句最大的卖点"。正文别写小作文——用户在商店里停留的耐心以秒计，条目式短句比大段落讨喜；功能列表（"记一笔：三秒完成，支持撤销"）比形容词堆砌（"极致体验、匠心之作"）可信十倍。

描述里还有一类高价值内容常被漏掉：承诺边界。"本 App 不联网、不收集任何数据"这种否定句，对隐私敏感的用户是强卖点；"免费，无广告"如果能兑现，就大方写上——商店里敢把"不做什么"写清楚的 App 反而显得自信。

关键词栏（keywords）是另一块战场：填那些塞不进描述的词，逗号分隔，有字数上限（编辑框会提示，以 App Store Connect 里的说明为准）。两条红线：别塞竞品品牌名——这是违规项，被抓就是白干；别重复 App 名称里已有的词——浪费位置。

"新增功能"（What's New）栏也别空着，更别只写"修复若干 bug"——用户会在更新提示里看到它。写法依旧是人话："新增：按月统计页；修复：个别情况下金额显示错误"。它同时也是你自己的发布备忘录，一年后翻回去看，每一版的足迹都在。

##### 隐私政策与技术支持链接

这两条链接是必填项，而且必须真实可打开。没有网站的解决方案很简单：把隐私政策写成网页，放到 GitHub Pages 上（免费，前面讲 GitHub 时用过）。内容写三件事——收集什么数据、怎么使用、怎么删除。个人 App 一页纸就够，但别照抄模板把没做的事写进去：政策与实际不符，比没有政策更糟。

##### 评分与评论：商店页的信任引擎

商店页上还有一样你控制不了、但影响巨大的东西：评分。它的运行规则朴素——满意的人很少主动评，不满意的人很主动。所以高质量的评分要靠"时机合适的邀请"：在用户刚完成一次顺利操作后（比如记完第 10 笔账）请求评分，系统提供了专门的评分请求接口，SwiftUI 里几行代码就能调起；频率克制，别在同一次使用里反复弹。

与之配套的是回复（前面发布后那一节会讲）。评分加回复，构成商店页的"信任闭环"：后来的用户看到的不只是分数，还有"这家开发者认真对待反馈"的证据。刷分、诱导评分这类捷径，违反规则还砸自己招牌，别碰。

##### 商店页自查：把自己当陌生用户

全部素材就位后，做一个终检：把你的商店页给一个没用过这个 App 的朋友看三十秒，然后问三个问题——这是什么？给谁用的？和同类 App 差在哪？三个都能答上来，素材合格；答不上来的那条，就是你要重写的地方。创作者视角里"显而易见"的信息，陌生用户常常一头雾水——这一步专治这种盲区。

##### 素材制作的最小流程

把第五节的全部建议压成一条流水线，照着做就行：

1. 定一句"身份句"——这是什么、给谁用，所有素材围绕它展开；
2. 做图标：AI 生成或图形工具画，过"缩小关"；
3. 列 5-6 个核心场景，每个配一句人话文案；
4. 真机截屏对应画面，加文案排版出全套尺寸；
5. 写描述：身份句开头，条目式列功能与特点；
6. 填关键词（避开名称已有词），写隐私政策网页；
7. 找一位没用过的朋友做三十秒测试，按反馈微调。

一个下午能把这套走完。别追求"工作室级"的精致——真实、清楚、说人话，就赢过商店里一半的页面。

#### 六、崩溃上报与性能优化小清单

App 上架前，这两件事值得各花半小时：

##### 1. 崩溃监控

你测试时没崩，不代表用户手机不崩。苹果在 Xcode Organizer 里提供免费的崩溃报告（付费账号可看真机崩溃日志）；更省心的方案是接入第三方 SDK（如 Firebase Crashlytics）。<strong>没有崩溃监控的上架，等于闭着眼睛开车</strong>。

两条的取舍：苹果自带方案零依赖、隐私负担最小，适合起步；第三方 SDK 报告更聚合、统计维度更全，代价是多一个依赖和多一份隐私申报（接了谁就要在隐私问卷里算谁的账，第 68 章讲隐私清单时会再提）。个人第一个 App，先用苹果自带的，等崩溃量大了再考虑升级装备。

想让崩溃"可复现"，还有一个便宜的办法：在关键动作处留下简短日志（本章第一节教的分级思想用上），崩溃报告附带的信息加上日志，就能还原用户最后几步做了什么。注意日志里别写敏感数据——记的是动作，不是内容。

##### 2. 性能自查四条

1. <strong>列表用 LazyVStack / List</strong>：长列表别用普通 VStack 硬排——懒加载是性能第一课；
2. <strong>图片别硬塞原图</strong>：用 AsyncImage（远程图）和系统缓存，5MB 原图足以卡爆老机型；
3. <strong>别在主线程干重活</strong>：网络、大文件都走 async/await；
4. <strong>用 Instruments 量一量</strong>：Xcode 自带的性能分析器（Time Profiler、内存泄漏检查）——先测量，再优化，别凭感觉。Xcode 16 起的 SwiftUI 专用剖析视图，加上 26 新增的 Processor Trace 与 Power Profiler，提交前过一遍，能抓掉明显的性能与耗电问题。

##### 3. Instruments 各面板：把"卡"拆开看

上面第 4 条提到的 Instruments，值得单独展开。打开方式两条路：Xcode 菜单 Product → Profile（⌘I），或 Xcode → Open Developer Tool → Instruments。常用面板先认识五个：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">面板</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">看什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">什么时候用</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Time Profiler</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">CPU 时间花在哪个函数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">卡顿、掉帧</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Allocations</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">内存分配曲线</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">内存警告、越用越慢</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Leaks</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">泄漏的内存</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">长时间运行越来越卡</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Energy Log</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">耗电去向</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">后台活动异常、发热</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Network</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">请求次数与耗时</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">流量异常、加载慢</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Instruments 五个常用面板

使用套路固定三步：连真机（模拟器的数据不作数）；录一段典型操作（滑列表、刷新、切页面，一两分钟）；停下来看结果，从占比最大的那项开始查。多数"我觉得慢"最后查出来是主线程上塞了网络请求或图片解码——Time Profiler 的火焰图会直接指认凶手。

走一个真实例子：记账本的流水列表滑动发卡。打开 Time Profiler，连真机录一段"上下滑列表"，火焰图里最高的柱子是图片解码函数——原来列表里塞了几张原图，滑动时每张都在主线程解码。对策：让列表显示缩略图，原图只在点开详情时加载。改完再录一段，柱子矮下去，卡顿消失。全程十来分钟，没有一行代码是凭感觉改的——这就是"先测量再优化"的样子。

Xcode 16 起，剖析器里有了 SwiftUI 专用视图：能看清每个视图被重建了多少次、耗时占比多少，"列表一滑就卡"十有八九在这里现形，答案多半是没用懒加载。Xcode 26 又添了 Processor Trace 和 Power Profiler：前者把 CPU 指令级的执行轨迹摆出来查深水区问题，后者直接看功耗花在了哪。工具越来越聪明，但套路没变：先测量，再动手，别凭感觉优化。

耗电与发热值得单说，因为用户对它的敏感度超过卡顿。App 常见的耗电三凶：后台频繁定位、高频率的网络轮询、无节制的动画。自查方法朴素有效——玩你的 App 十分钟，摸一下手机温不温；再用 Power Profiler 看耗电构成。记账本这类工具 App 的及格线很简单：不用时几乎零耗电，用时轻松流畅。

内存也顺带说两句：老机型内存小，同一份代码在小内存设备上更容易被系统"劝退"。自查方法是长时间使用你的 App——连着刷几百条记录、开开合合几十次页面——观察会不会越来越卡（内存没释放的信号）。Allocations 面板的曲线应该"锯齿状"波动（分配又释放），如果只涨不跌，说明有东西一直攥在手里不撒手，那就是优化对象。

##### 4. 发布前最后一遍自查清单

提交前的半小时，把这张清单过一遍，每一条都是本章讲过的动作的"最后一遍"：

- 断点全清掉（带着断点打的包会莫名卡顿）；
- 调试 print 删掉，或用 #if DEBUG 包住；
- 全部测试 ⌘U 跑绿；
- 构建号比上次 +1，版本号按计划改好；
- 每个权限的用途文案读一遍，说人话；
- 隐私问卷和隐私清单与实际采集行为对得上（隐私清单第 68 章细讲）；
- 深色模式、大字号、飞行模式各过一遍——离线时界面不能白屏；
- 用真机装一次 TestFlight 的包，冷启动把核心流程走完。
- 弱网（飞行模式 + 慢速网络）下核心流程不白屏、不卡死；
- 深色模式下每页看过一眼，金额与提示文字都清晰可读。

#### 七、TestFlight：内测分发的完整流程

TestFlight 是苹果官方的内测平台，也是上架前最值得走的一步：它让你把包发给成百上千台真实设备、收集真实崩溃，而不用把人聚起来连数据线。

##### 1. 它解决什么问题

没有 TestFlight 的年代，发测试包靠逐台连数据线，或者各种第三方签名渠道——又累又有安全风险。TestFlight 把这件事搬进了官方体系：你把构建上传到 App Store Connect，发出邀请；测试员在 iPhone 上装一个 TestFlight App，你的构建出现在里面，点一下就装上。测试员的崩溃报告和截图反馈会自动回流给你。它和正式上架用的是同一个构建上传通道，所以走完 TestFlight，上架的流程你也基本走熟了。

##### 2. 内部测试与外部测试

两类测试组，规则不同。<strong>内部测试组</strong>：成员必须是你 App Store Connect 团队里的人（在"用户和访问"里加），上限 100 人，构建处理完就能装，不需要额外审核——适合自己人先过一遍。<strong>外部测试组</strong>：面向团队之外的任何人，上限 10000 人，邀请方式两种——逐个邮箱邀请，或生成公开链接（拿到链接的人都能加入）。外部测试的第一个构建要通过一次"Beta App 审核"，比正式审核轻量得多；同一版本的后续构建一般不用再审。规则细节以 Apple 官网为准。

给个人开发者的实用组合：朋友同事拉内部组，先抓真问题；想扩大反馈面（在社群里发个招募帖）就用公开链接走外部组。两头加起来，一个几百人规模的"野生测试团队"就有了。

##### 从上传到邀请：完整时间线

串一遍时间线给你：Xcode 里 Archive → Distribute → 上传（几分钟）；ASC 里等构建处理完成（通常几十分钟到几小时，收到邮件）；填这版构建的"What to Test"；把构建加入测试组——内部组即刻可装，外部组的首个构建先过 Beta 审核；测试员收到更新提醒，安装、使用、反馈。链路走熟之后，"发一个新版本给测试员"是半小时级别的日常操作——对比当年连数据线一台台装，幸福感是跨越式的。

##### 3. 测试员那边长什么样

测试员收到邀请邮件或点开公开链接后，流程是三步：跳转下载 TestFlight App → 在 TestFlight 里看到你的 App → 点安装。之后你每传一个新构建，他会收到更新提醒，点一下就升级。反馈同样方便：App 里截个屏可以直接加注释发给你；摇一摇设备也能唤出反馈面板；崩溃更是自动上报，连重现路径都替他写好了一半。

招测试员有个小门道：与其招一百个"装完就没打开过"的人，不如招十个愿意写反馈的。公开链接发出去之后，记得在社群里配一句"遇到问题请用 TestFlight 的截图反馈"，反馈率立刻不一样。

遇到"装完没声了"的测试员也别急——正常现象。低成本促活两招：在更新说明里点名感谢反馈者（人都在意被看见）；每隔一两周在群里发一条"这版重点想让大家试试 XX"，把注意力给到具体功能。测试员是伙伴不是资源，维持温度比拉长名单重要。

给个具体场景感受它的价值：你把记账本发给五位朋友内测，第二天 Organizer 里躺了两条崩溃——都来自某款老机型，堆栈指向同一个数组越界；另一位朋友的截图反馈写着"深色模式下金额看不清"。这三个问题在你自己的设备上永远碰不到，而它们已经在提审之前修掉了。TestFlight 的本质，就是花 99 美元买到了"别人家的设备"。

招募文案也有模板可抄："我在做一个记账 App，找 10 位真实用户内测（TestFlight 一键安装，不用越狱不用折腾）。要求：每周用三次，愿意在遇到别扭的地方随手截图反馈。回报：你的建议会被写进下一版更新说明。"——要求具体（每周三次）、门槛真实（一键安装）、有回报（写进更新说明），满足这三条的招募帖，反馈质量远高于"有人想试试吗"。

##### 4. 三件管理小事

构建有有效期（上传后 90 天，以官方文档为准），到期自动失效，重新传一个新构建就行——这也是"保持上传节奏"的一个动力。每传一版记得填"What to Test"（测试要点），一两句话告诉测试员这版重点看哪里，反馈质量立刻上一个台阶。上传后到 ASC 的 TestFlight 页签看处理状态，处理完成后把构建加进对应测试组，测试员才会收到它。

也认清它的边界：TestFlight 里不能收款、不能长期留存用户（构建会过期）、外部测试要过 Beta 审核——它是分发和验证工具，不是运营阵地。测试做得再热闹，最终都要落到"提交正式审核"这一步，两边用的是同一套上传通道，衔接是顺的。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">对比项</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">TestFlight</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">App Store 上架</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">谁能装</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">受邀测试员（内部 100 人 / 外部 10000 人）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">所有人</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">审核</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">内部免审；外部首构建过 Beta 审核</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每次提交都过完整审核</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">有效期</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">构建到期自动失效（具体天数以官方为准）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">长期在线</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">收款</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不能</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可以</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定位</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">提审前的练兵场</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">正式货架</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
TestFlight 与正式上架的分工

#### 八、App Store Connect 后台导览

App Store Connect 不只是传包的地方，上架后的日常运营都在这里。五个板块值得挨个逛一遍：

- <strong>我的 App</strong>：主战场。每个 App 的"App Store"页签管上架信息与版本，"TestFlight"页签管内测。名称、截图、描述、价格都在这里改——改完都要重新走审核（前面说过）；
- <strong>用户和访问</strong>：加团队成员、分配角色，TestFlight 内部测试员也从这里来。个人开发者初期只有你自己；有了协作者后再研究最小授权——能只给营销权限就别给管理权限；
- <strong>协议、税务与银行业务</strong>：想收钱（付费下载或内购）必来此地——签付费协议、填税务表单、绑收款账户。流程繁琐但一劳永逸，很多人卡在税表上半个小时，耐心点，表单有中文界面；
- <strong>App 分析</strong>：上架后的数据驾驶舱——下载量、活跃、崩溃率、各渠道转化。别天天盯，每周看一次足够；崩溃率是重点，看趋势比看绝对值有用；
- <strong>财务与销售报告</strong>：每月结算的明细与打款记录都在这里查，报表可以下载。

导览时留意一个状态灯："协议、税务与银行业务"里各协议的状态要处于有效——付费 App 和内购都挂在协议之下，协议没生效，相关功能在后台是"锁着"的。很多新手第一次加内购发现添加不了，根源就是协议没签完。

两个导览提醒：后台界面偶尔改版，别背菜单，认准板块名；所有"提交审核""协议"相关的邮件都会发到注册邮箱——有些问题（比如协议没签导致无法上传）是邮件比后台先知道的。

再提一句未来的你可能用到的事：如果记账本以后加了内购（比如订阅高级统计），ASC 里还要配置内购项和沙盒测试账号——沙盒是苹果提供的"假支付环境"，不用真扣钱就能把购买流程测通。现在先知道有这块地方，到时候顺着界面提示走就行。

##### 导览路线：第一次进后台的三十分钟

给你排一条第一次进后台的参观路线，照着走三十分钟对全貌有数：先进"我的 App"，把建好的 App 页面从左到右点一遍（App 信息、版本、定价）；再到"用户和访问"，看看角色列表长什么样；然后去"协议、税务与银行业务"，确认付费协议的状态——没签就先放着，上架免费 App 不拦你；最后点开"App 分析"，现在是空的，上架两周后回来——那时它会开始讲故事。后台的每个角落都去过了，后面遇到问题才知道该去哪儿找。

#### 九、发布后的第一周：盯三件事

上架不是终点，是观察期的开始。第一周盯三件事，密度比平时大一点，之后回归常规节奏。

##### 第一件：崩溃与评分

每天看一眼 Organizer 的崩溃页和后台的崩溃率——第一批用户是最好的压力测试员，他们手机型号五花八门、网络环境千奇百怪。商店评分同步关注：一两颗星的差评往往就是崩溃或误导性描述的直接反馈，逐条看，别玻璃心。发现问题立即分诊：能热修的下周提更新，需要大改的进下一版计划。

顺带一条伦理提醒：请求评分的时机要避开"用户正在骂你"的时刻——崩溃恢复后、报错弹窗后，都不是好时机。"刚顺利记完第 10 笔账"才是黄金时刻。时机错误的好评请求，等于提醒用户去打差评。

崩溃分析的方法第一章刚讲过：按机型分组看分布，按系统版本看兼容性，读堆栈定位代码。上架初期的崩溃多半是"自己设备上没出现过"的环境问题——内存小的老机型、系统语言不同的设备、弱网。把每一个崩溃当成一封用户来信，回信的方式就是修复。

##### 第二件：回评论

App Store Connect 支持开发者回复用户评论（以官方功能说明为准），这是最容易被浪费的免费运营位。认真回复前十条评论——好评道谢、差评给修复时间表——后来者会把你的回复当成"这个开发者还活着"的证据。回复就一条原则：承认问题，给行动，不吵架。被评论气到的晚上，先写草稿，第二天再发。

##### 第三件：排下一版

把第一周收集的问题分成三堆：崩溃（立刻修，走更新）、易用性反馈（进下一版）、锦上添花（进愿望清单）。然后按本章全流程再走一遍下一版——第二次会比第一次快一半，因为每一步你都认识路了。发布的节奏感，就是这样一圈圈转出来的。

版本说明也在这里顺手写好：每版发出去之前，把"这版改了什么"写成三五条人话放进"新增功能"栏。它既是给用户的交代，也是给自己的项目日志——半年后回看，每一版的足迹清清楚楚。

##### 顺手做：定一个发布日历

把节奏写进日历，别靠临场发挥。一个可抄的模板：发布前一周，素材与描述定稿、测试全绿；前三到四天，提审（给审核排队留余量）；发布日，盯崩溃、盯评分、盯下载曲线；发布后第七天，复盘——哪些反馈最多、下一版排什么。每版重复这个循环，改的只是内容，不是流程。文档里存一份模板，下一版照着填空。

#### 十、FAQ：上架前后最常问的十一个问题

<strong>问：免费 Apple ID 到底能干到哪一步？能不能发 TestFlight？</strong>

答：能跑模拟器、能真机自装（7 天续期）、能写测试跑测试；TestFlight 和上架都需要付费开发者账号。换句话说，"给朋友装一个试试"这个需求，免费账号只能逐台设备连 Xcode 装，付费账号一个 TestFlight 链接就解决了。

<strong>问：被拒了会留"案底"，影响下次提交吗？</strong>

答：不会公开，也不影响下次。审核针对的是"这一次提交"。认真改，重新提交就行——被个两三次很正常，拒绝理由写得具体，照着改就是最好的学习过程。

<strong>问：加急审核真的有用吗？什么条件能过？</strong>

答：有用，但它是给线上严重问题准备的救火通道，不是营销工具。理由写清楚（哪个版本、什么崩溃、影响多大用户），通过率不低；频繁申请会失效。日常版本更新老老实实排队。

<strong>问：上架后改名字、换图标，要重新审核吗？</strong>

答：要。元数据的任何改动都走一遍审核（不用重传包）。商店页的优化可以慢慢做，但每次都有排队成本，攒着一起改更划算。

<strong>问：我是个人开发者，用个人账号好还是等注册公司？</strong>

答：个人账号申请简单、收款方便，商店页会展示开发者姓名；公司账号需要额外的组织材料（以注册页面要求为准），商店页显示公司名。个人练手和独立开发，个人账号完全够，以后真需要再转移 App 也来得及——苹果支持 App 在不同账号之间转移，后台有入口，细节以官方文档为准。

<strong>问：审核都通过了，商店里为什么搜不到我的 App？</strong>

答：新 App 的搜索索引有延迟，通常几小时到一天内出现（以实际为准）。先确认状态是"可供销售"，然后直接搜完整名称；还不行就检查 App 名称是否与已上架的热门 App 高度相似——相似的名称会影响搜索展示。

<strong>问：要不要找"签名服务商"或者买什么企业证书？</strong>

答：不要。个人开发者用官方通道（自动签名 + TestFlight + 上架）就够了，第三方签名渠道绕开的是官方审核，代价是安全风险和随时失效。真想省钱，先想清楚：99 美元一年，是整个生态的入场券，不是智商税。

<strong>问：一年 99 美元交了，反悔能退吗？</strong>

答：订阅的退款规则以苹果官方为准，注册前想清楚。更实际的问题是反过来问自己：这一年打算发几版？哪怕只发一版，TestFlight 加上架的完整体验也值回票价——这套流程教会你的东西，比任何一门"App 变现"网课都扎实。

<strong>问：审核员会看我的源代码吗？</strong>

答：不会，审核针对的是提交上来的 App 本身——装上、点开、按条款测。但隐私条款要求你对数据采集如实申报，出了问题责任在你。代码里有没有"暗私"（偷偷上报数据之类），得自己管好，那是信用问题，不是审核问题。

<strong>问：想让海外用户也能下载，要做什么？</strong>

答：定价与销售范围里可以选多个国家与地区（以官方文档为准）；描述、截图这些元数据支持按地区本地化，各写各的。建议先在熟悉的地区打磨好评分和崩溃率，再逐步铺开，别一口气全选——铺得越广，维护的元数据越多。

<strong>问：上架之后价格还能改吗？改成免费行不行？</strong>

答：价格在后台的价格设置里随时可调，免费与付费之间也能切换，具体生效规则以官方说明为准。要留意的是"从付费转免费"再"转回付费"可能让老用户的观感摇摆——定价策略想好再动，别把商店页当实验田。

<strong>问：我 App 里有个功能依赖登录，审核会不会直接进不去？</strong>

答：会卡。需要登录的 App 必须在提交时提供演示账号（写进审核备注的 App Review Information 区块），账号密码要真实有效。没给或失效，是"审核员进不去 App"这一被拒类型的头号原因——别栽在这种最便宜就能避免的坑上。

<strong>问：我想直接联系留下差评的用户，拿得到他的邮箱吗？</strong>

答：拿不到，也不该去拿——苹果不向开发者提供用户联系方式，套取用户信息本身也是违规动作。合法的通道是商店评论的公开回复，以及 App 内的反馈入口。想倾听用户，就在 App 里放一个显眼的"提建议"按钮，让人愿意主动来找你。

<strong>问：审核备注（App Review Information）里该写什么？</strong>

答：替审核员省时间的内容都值钱：演示账号（如果有登录）、特殊功能的触发路径（"长按首页标题三秒进入统计页"）、测试注意事项（"数据为空时显示引导页属正常"）。审核员看得越顺，你的过审越快——这份备注本质上是给"第一位用户"的使用说明。

#### 十一、上架误区清单：五个"以为"与真相

- <strong>以为"全做完再上架"</strong>。其实小步快跑更稳：核心功能打磨好就提交，审核反馈本身就是一次免费体检；拖着不上架，问题只会攒得更多，心态也越拖越虚。
- <strong>以为"过审一次，以后秒过"</strong>。每次版本更新、每次元数据修改都重新排队。给版本节奏留出审核时间的余量，别卡着某个纪念日提审。
- <strong>以为"没人下载就不需要崩溃监控"</strong>。崩溃率按启动次数算，下载少不等于没崩。第一批用户的崩溃日志，恰好是上架初期最值钱的反馈，别浪费。
- <strong>以为"描述越长越好"</strong>。商店页的阅读耐心以秒计，三行人话胜过三十行排比。真想读长文的用户只有想买的那几个，把关键信息放前三行就够。
- <strong>以为"TestFlight 是不上架的替代方案"</strong>。它有有效期、外部测试要过 Beta 审核、不能收款，是上架前的练兵场，不是绕过审核的后门。想长期分发，上架是唯一正路。
- <strong>以为"上架后就万事大吉"</strong>。上架只是把货架摆好了——崩溃要盯、评论要回、新系统要适配（每年大版本更新后把你的 App 过一遍）。维护成本从上架那天开始，没有"结束"那天。
- <strong>以为"苹果会帮我推广"</strong>。商店给的曝光主要来自关键词、转化率和评分，运营是你自己的事。第五节素材那一节花的功夫，本质上就是在做"商店里的获客"。
- <strong>以为"过审等于代码合格"</strong>。审核查的是条款合规（安全、隐私、功能完整），代码质量——性能、可维护性、测试覆盖——得你自己负责。过审只是"可以上货架"，不是"是个好产品"。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：把记账本"交付"一次

{class="mt-1"}
① 给 parseAmount 等逻辑补 3 个单元测试（⌘U 跑绿）；② 用断点亲手抓一个自己制造的崩溃并修好；③ Product → Archive 打一个包，走 TestFlight 邀请朋友内测；④ 有余力就注册开发者账号，把记账本真正提交上架。前三步今晚就能做完。

{class="mt-1"}
临走再送一句：发布不是一次性动作——把版本号规则、归档步骤、上传与测试分组写进项目文档，下一版照着走就行。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 调试三板斧：print 日志、断点、SwiftUI 预览与视图检查器
- XCTest：单元测试（⌘U）+ UI 测试 + 手动测试，模板已预置
- 签名：免费账号自动签名（7 天续期）；付费账号才能分发
- 打包：Generic iOS Device + Archive + Distribute；证书务必备份
- 上架六步：注册 → 素材 → 上传 → 隐私问卷 → 审核 → 上架；TestFlight 先内测
:::
