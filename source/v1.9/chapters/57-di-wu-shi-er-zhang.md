---
id: di-wu-shi-er-zhang
num: 52
part: an-zhuo-kai-fa-pian
nav: 第五十二章：四大组件与Activity生命周期
toc: default
kind: chapter
---

### 第五十二章：四大组件与 Activity 生命周期

{class="chapter-intro mb-4"}
如果说 Compose 是 App 的"脸"，那这一章讲的就是 App 的"骨架"。安卓系统有四大基本组件，所有 App 都是由它们拼成的；而其中最重要的 Activity，有一张每个安卓开发者都必须刻在脑子里的"生命周期图"。本章学完，你就能理解"为什么切个后台回来，我的 App 状态就没了"这类千古之谜。

先给你一个学习上的定心丸：这一章的概念密度是全书最高的之一，但好消息是——它是"一次学会、终身受用"的章节。生命周期、Intent、状态保存这些概念在 iOS（第 63 章）、鸿蒙（第 74 章）里都有几乎一样的对应物，学一遍等于学了三遍。所以值得慢下来，把每一个概念都嚼透。

#### 一、四大组件：安卓的"四梁八柱"

安卓官方定义了四种基本组件，分别负责一类工作：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">组件</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">职责</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">打个比方</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activity</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一个可见的界面</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">店铺的门面——用户能看见、能交互</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Service</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">后台干活的"隐形人"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">仓库工人——放音乐、下载文件，不需要界面</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BroadcastReceiver</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">接收系统广播</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">传达室——"电池没电了""网络断了"的喇叭</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ContentProvider</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跨 App 共享数据</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">公共资料柜——比如把联系人共享给别的 App</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
安卓四大组件速览

##### Activity：门面的门道

Activity 的工作方式你可能已经在第 51 章感受到一角：Compose 项目里虽然界面都是 Composable 函数，但它们仍然"住"在一个 Activity 里——MainActivity 就是整个应用的入口容器。你可以把 Activity 理解为"系统分配给你的画布窗口"：系统决定什么时候创建它、显示它、遮住它、销毁它，而你在每个时机里做该做的事。一个 App 可以有多个 Activity（比如登录页一个、主页一个、详情页一个），它们之间通过 Intent 跳转——这是第三节的内容。

新手阶段你 95% 的时间都在跟 <strong>Activity</strong> 打交道；Service 和 BroadcastReceiver 做音乐播放、消息推送时会用到；ContentProvider 用得最少（系统已把常用数据封好了）。另外注意：四大组件都要在 <strong>AndroidManifest.xml</strong> 里"登记户口"，不登记系统就找不到它们。

Manifest 的"登记"具体长什么样？每个组件是一条 XML 声明：Activity 要标名字和主题，Service 要标是否前台，Receiver 要标监听什么广播。还有一个容易被忽略的登记项是<strong>权限</strong>——应用要用的敏感权限也声明在这个文件里，运行时再向用户申请（第六章讲过权限最小化的原则，开发侧的落实就在这个文件）。第 74 章讲鸿蒙的 module.json5 时你会发现，"声明式登记"这个设计是跨平台通用的。

##### Service：后台的"隐形人"怎么管

Service 最典型的例子是音乐播放器：用户按了播放键、锁屏走人，音乐不能停——这就是 Service 在后台工作的价值。但 Service 有个新手大坑：<strong>它运行在主线程上</strong>。如果你在 Service 里直接做下载大文件这类耗时操作，界面照样会卡——后台的"隐形"不等于"不卡主线程"。耗时操作要在 Service 里开子线程或协程。

Service 还分两种运行模式：普通 Service（随时可能被系统回收）和前台 Service（必须挂一条常驻通知，告诉用户"我在后台干活"）。音乐播放器用的就是前台服务——通知栏那条"正在播放"就是它。系统对前台服务的管理比较宽松，因为它"可见"；对隐形 Service 越来越严格，现代开发中，可延迟的后台任务大多改用 WorkManager（本章第六节细说）。

##### BroadcastReceiver 与 ContentProvider：认识即可

BroadcastReceiver 的现代用法已经收窄：以前 App 们到处监听系统广播（网络变化、电量变化），现在系统对这些广播的发放越来越克制（省电考虑）。你实际会用的场景多是"应用内通信"——用本地广播在自己的组件之间传消息。ContentProvider 则是跨应用共享数据的正规通道：联系人和短信这些系统数据，系统已经内置了 Provider，你的 App 通过统一的 API 去读（要权限）。自己写 Provider 的场景很少见——通常只在"你想把数据开放给别的 App"时才需要。

#### 二、Activity 生命周期：安卓开发的第一张"藏宝图"

手机上的 App 随时可能被打断：来电话了、用户切去回微信、系统内存不够把你杀了……Activity 的一生，就是在这张图上循环旅行：

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onCreate（出生：初始化）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onStart（可见了）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onResume（前台交互中）</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onPause（部分被遮住）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onStop（完全看不见）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center">onDestroy（销毁）</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">🔁 onRestart / onStart / onResume：回到前台时原路返回</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
图 4：Activity 生命周期（前进方向：上排出生 → 下排离场，回来时原路折返）
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">回调</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">什么时候触发</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">典型用途</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onCreate</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activity 创建时（一次）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">加载界面、初始化数据</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStart</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">界面变为可见</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">开始一些轻量逻辑</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onResume</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">拿到焦点、可交互</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">开始动画、恢复播放</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onPause</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">被部分遮挡/切走瞬间</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">暂停动画、保存草稿</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStop</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">完全不可见</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">释放重资源、暂停下载</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onDestroy</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">被销毁前</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最后的清理</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
六个生命周期回调的典型用途

把这张表"翻译"成一天的生活就特别好懂：onCreate 是"起床穿衣"（一天一次的初始化），onResume 是"出门上班"（开始正事），onPause 是"有人跟你说话"（手上的事暂停但不放下），onStop 是"进了会议室"（手上事完全放下），onDestroy 是"下班回家"。回到办公室的流程（onRestart → onStart → onResume）就是"开完会回工位"。

实战中最重要的两条规则藏在表里。第一条：<strong>onPause 里别做重活</strong>——它是"切走瞬间"触发的，用户感觉到的卡顿就发生在这几毫秒里；重活放到 onStop。第二条：<strong>onStop 里做持久化</strong>——完全不可见时，你的应用随时可能被系统回收，这就是"切个后台回来状态没了"的根源：不是状态丢了，是你没在 onStop 之前把它存下来。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>避坑提醒：屏幕旋转会"杀死"Activity

{class="mt-1"}
新手最经典的翻车现场：App 转一下屏幕，输入框里的字全没了。原因：旋转屏幕默认会销毁并重建 Activity（走一遍 onDestroy → onCreate）。解法：用 <code class="inline">rememberSaveable</code> 保存状态（Compose 里替代 remember），它会在重建时自动把值找回来。第 53、54 章会反复用到。
:::

##### 生命周期日志：亲手"看见"它

学生命周期最好的方法不是背表，是"亲眼看"。在 MainActivity 的六个回调里各加一行 Log.d("LIFECYCLE", "onCreate 被调用了")（以此类推），然后做一组动作：打开应用 → 按主页键 → 重新打开 → 按返回键退出。打开 Logcat 过滤 "LIFECYCLE"，你会看到一条完整的时间线。再做几个进阶动作：旋转屏幕（观察销毁重建）、切到另一个 App 再回来（观察 onStop/onRestart）、收到一条通知点开（观察 onPause/onResume）。做完这一套，生命周期就从"背"变成了"懂"。

这套"日志观察法"在三个平台通用：iOS 的 viewDidLoad/viewDidAppear（第 63 章）、鸿蒙的 aboutToAppear/aboutToDisappear（第 74 章）都可以用同样的手法打日志观察。三平台的生命周期概念映射，本章第六节有对照表。

#### 三、Intent：App 里外通行的"车票"

Intent（意图）是组件之间通信的"车票"。你想从一个页面跳到另一个页面，或者打开浏览器、调起相机，都要"买票上车"：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 用 Intent 跳转</span><span class="dots">···</span>
:::

```
// 方式一：显式 Intent——明确指定去哪个页面
val intent = Intent(this, DetailActivity::class.java)
intent.putExtra("name", "张三")     // 车上捎带"行李"（数据）
startActivity(intent)

// 方式二：隐式 Intent——只说要干什么，系统找谁干
val web = Intent(Intent.ACTION_VIEW, Uri.parse("https://developer.android.com"))
startActivity(web)   // 系统会打开浏览器/或让你选
```
:::

两种方式各有用途：<strong>显式</strong>用于自己 App 内部的页面跳转；<strong>隐式</strong>用于调用系统或其他 App 的能力（开网页、打电话、分享）。Compose 项目里，在 Composable 中用 <code class="inline">LocalContext.current</code> 拿到 Context 就能 <code class="inline">startActivity</code>。

隐式 Intent 有个重要的"契约"细节：你只声明"我要看网页"，系统会找所有能干这件事的 App 让用户选——如果装了多个浏览器就会弹选择框。反过来，你的 App 也可以"被别人调起"：在 Manifest 里声明"我能处理分享图片"这类能力，别的 App 分享时你的应用就会出现在列表里。这个"发布能力"的机制在鸿蒙（第 74 章的 skills 声明）和 iOS（URL Scheme）里都有对应物——"组件通信"的跨平台思路也是相通的。

putExtra 捎带的"行李"也有边界要记住：它适合传小数据（字符串、数字），不适合传大对象（Bitmap 图片这种动辄几 MB 的东西）——大对象应该先存到存储或内存缓存，Intent 里只传一个"取货凭证"（比如文件路径或 ID）。滥用 Intent 传大对象，是新手常见的性能事故来源。

#### 四、多页面与导航

真实 App 都有多个页面。Compose 官方推荐的导航方案是 <strong>Navigation Compose</strong>（依赖库 androidx.navigation）：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Navigation Compose 骨架</span><span class="dots">···</span>
:::

```
val navController = rememberNavController()

NavHost(navController, startDestination = "home") {
    composable("home") { HomeScreen(navController) }
    composable("detail/{name}") { entry ->
        val name = entry.arguments?.getString("name")
        DetailScreen(name ?: "未知")
    }
}

// 在页面里跳转：
navController.navigate("detail/张三")     // 带参数
navController.popBackStack()              // 返回上一页
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：页面多了怎么办？

{class="mt-1"}
项目长大后，把所有页面路由集中写在一个文件里（比如 <code class="inline">AppNavGraph.kt</code>），统一管理，别让"跳转到哪"的逻辑散落在各个页面。这是从"能跑"走向"可维护"的第一步。
:::

Navigation Compose 与传统 Intent 跳转的关系也要理清：Intent 是"系统层"的组件调度（一个 Activity 拉起另一个 Activity），Navigation Compose 是"应用层"的页面切换（同一个 Activity 里的页面栈）。现代应用的常见架构是：整个应用只有一个 MainActivity，内部所有页面用 Navigation 管理——简单、流畅、转场自然。Intent 只在"调起系统能力"或"跨应用"时使用。这个"单 Activity 架构"是 2026 年的主流实践，也是第 51 章推荐的项目起点。

#### 五、顺带认识：Fragment 是什么（以及为什么本书没教）

查老教程时你一定会撞见 <strong>Fragment</strong>——它是 Activity 里的"可复用界面片段"，在老式多页面架构里是绝对主角。但 Compose 时代，页面直接用 Composable 函数 + Navigation 路由就够了，官方也已弱化 Fragment 的地位。本书因此没把它放进主线。

给你的建议：<strong>新项目不主动用 Fragment</strong>；但读老代码、面试被问到时，知道它是"Activity 里嵌的界面片段"即可。学习资源永远优先选 2023 年以后的——安卓技术栈的"老黄历"更新得比想象中快。

Fragment 的"过时轨迹"还有个学习上的启示：技术栈的更新换代在安卓生态里特别快，Fragment 从"绝对主角"到"被弱化"只用了几年。应对之道不是追每个新技术，而是抓"不变的东西"——生命周期、状态管理、组件通信这些系统层的概念永远有效（本章讲的就是它们），界面层的新框架来了换一套 API 就行。第 37 章讲 AI 编程时说"学不变的东西"，就是这个道理的应用。

#### 六、Compose 时代还要不要学四大组件

聊完 Fragment，把这个问题问得更彻底些：Compose 时代，四大组件还要不要学？要——但着眼点变了：界面用 Compose 写，四大组件与生命周期仍然决定"你的代码什么时候活着"。

- <strong>Activity 仍是大门</strong>：旋转屏幕、切后台、被系统回收，走的是 Activity 生命周期；Compose 只是挂在它上面的界面。
- <strong>用生命周期感知的状态</strong>：ViewModel 承载业务状态，界面重组不会丢数据；<code class="inline">collectAsStateWithLifecycle</code> 一类 API 让订阅跟着生命周期走，避免后台泄漏。
- <strong>配置变更</strong>：本章第二节的避坑提醒说了 rememberSaveable；更进一步的常规解法是 ViewModel——旋转重建时 remember 会丢、ViewModel 不会。要跨重建保留的东西，放 ViewModel 或 savedStateHandle。
- <strong>权限请求</strong>：危险权限仍在运行时申请，只是入口从 Activity 回调换成了 <code class="inline">rememberLauncherForActivityResult</code>。
- <strong>Service / BroadcastReceiver / ContentProvider</strong>：后台任务、系统广播、跨应用数据共享仍靠它们；新代码里，可延迟的后台工作多交给 WorkManager 处理。

ViewModel 值得单独强调，因为它是 Compose 时代的"状态保险箱"：旋转屏幕会重建 Activity 和界面，但 ViewModel 活在更长的生命周期里不受影响——所以"输入到一半的数据、网络请求的结果"这类重要状态都该放 ViewModel。rememberSaveable 适合保存轻量的临时状态（比如一个开关），重要数据交给 ViewModel。两者的分工在下一章讲数据层时还会展开。

::: div .tip-box .rounded-lg .p-4 .mb-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>一句话记牢

{class="mt-1"}
框架换了界面层，系统层没换。生命周期不过时，只是入口从回调变成了可组合函数里的副作用 API。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：给计数器装上"记忆"

{class="mt-1"}
把第 51 章的计数器改造一下：① 把 remember 换成 rememberSaveable，旋转屏幕验证数字还在；② 加一个"关于"按钮，用 Navigation 跳到第二个页面显示版本号；③ 在两个页面的 onCreate/onPause 里打印日志（Log.d），用 Logcat 观察生命周期调用顺序。做完这三步，生命周期就不再是纸上谈兵。
:::

#### 七、状态保存的完整方案：三层各管一段

生命周期一懂，"状态去哪儿了"就成了核心问题。安卓的状态保存其实是一套三层体系，每层管不同的"存续时间"——搞混层次是状态丢失问题的总根源。

- <strong>临时层：remember / rememberSaveable</strong>——活在一个界面里。remember 管最轻的临时状态（一个开关、一段输入），旋转屏幕会丢；rememberSaveable 能扛过旋转重建，但应用被系统杀死还是会丢。
- <strong>中期层：ViewModel</strong>——活在"这个界面的一辈子"里。旋转重建、切后台回来，ViewModel 都还在；只有界面彻底退出（用户按返回键离开）它才销毁。输入到一半的表单、网络请求的结果、滚动位置——这些"界面级的重要状态"都该住在这里。
- <strong>永久层：数据库与文件</strong>——活过应用的生命周期。用户精心录入的记账数据、聊天记录，用 Room 或文件系统持久化（第 53 章展开）。重启手机都还在。

三层的分工可以用一个记账 App 的例子串起来：你正在输入的一笔金额，放 rememberSaveable（临时）；已经记账成功的本月流水，放 ViewModel（界面级）；一个月的历史账单，放 Room 数据库（永久）。数据按"丢了多心疼"分层，而不是按"实现起来哪个方便"。

savedStateHandle 是一个容易被忽略的中间角色：它挂在 ViewModel 上，专门保存"进程被系统杀死后恢复"用的关键状态。系统内存不足时，会把后台应用的进程整个杀掉——ViewModel 也随之消失。但 savedStateHandle 里的数据会被系统存档，用户切回来时系统重建进程并还给它。适合放的东西很少而关键：正在浏览的条目 ID、搜索关键词。判断标准一句话：<strong>用户切走半小时回来，看到界面能否无缝继续？</strong>能答"是"，就说明三层各放对了。

##### 配置变更的"全家福"：不止旋转屏幕

旋转屏幕只是配置变更的明星案例，全家族还包括：深色模式切换、字体大小调整、多窗口模式、语言切换、键盘可用性变化——每一次都会触发 Activity 重建。所以"状态保存"不是旋转专用的补丁，而是所有配置变更的通用对策。检验方法也很简单：打开开发者选项里的"不可调整大小的活动模拟尺寸变化"，随手切几个配置，看界面的状态是否都在。能扛过这一套的，才算状态管理及格。

#### 八、后台任务：WorkManager 与它的伙伴们

"后台干活"听起来简单，实际上安卓给了一整套工具箱，各有明确的分工。选错工具是新手第二常见的问题（第一是状态丢失）。

- <strong>WorkManager</strong>：可延迟的后台任务主力。它的特点是"保证执行"——即使应用退出、设备重启，任务也会在条件满足时跑起来。适合：同步数据、上传日志、定期清理缓存。它支持约束条件（仅在 Wi-Fi 下执行、仅在充电时执行）和周期性任务，是"可靠后台"的代名词。但记住它的边界：不保证精确时间——你定"1 小时后"，它可能在 1 小时到几小时之间的任何时刻执行（系统会攒着省电）。
- <strong>AlarmManager</strong>：精确的定时触发。闹钟类需求（每天早上 7 点整提醒）必须用它，WorkManager 干不了这活。它还能区分"精确唤醒"（strict）与"非精确"（省电模式友好）——默认非精确，闹钟类选精确。
- <strong>前台 Service</strong>：用户主动启动的持续任务（播放音乐、导航中）。必须挂常驻通知。系统对它的限制最松，因为它"用户看得见"。
- <strong>协程</strong>：应用在前台时的"当前任务"。点击按钮加载列表、提交表单——这类随用随走的异步操作用协程最自然，不需要动用上面任何重型工具。

选型的口诀：<strong>当前界面做→协程；必须可靠执行→WorkManager；必须准时→AlarmManager；用户看得见的持续任务→前台 Service</strong>。四句话覆盖 90% 的场景，剩下 10% 是混合需求（比如"每小时精确同步一次"= AlarmManager 触发 + WorkManager 执行）。

WorkManager 还有一个新手盲区：它处理的是"应用的排队任务"，不是"接收外部事件"。比如"监听用户删除了一条短信"这类系统事件监听，要用 BroadcastReceiver（现代写法里很多系统广播需要动态注册）。工具箱里每件工具解决一类问题——先定义问题，再选工具。

##### WorkManager 实战：三步写出可靠的后台任务

::: div .code-block
:::inline div .code-head
<span>KOTLIN · WorkManager 三步走</span><span class="dots">···</span>
:::

```
// 1. 定义任务（继承 CoroutineWorker，用协程写异步逻辑）
class SyncWorker(context: Context, params: WorkerParameters) :
    CoroutineWorker(context, params) {
    override suspend fun doWork(): Result {
        return try {
            syncData()               // 你的同步逻辑
            Result.success()
        } catch (e: Exception) {
            Result.retry()           // 失败自动重试
        }
    }
}

// 2. 定义约束（仅在 Wi-Fi + 充电时执行）
val constraints = Constraints.Builder()
    .setRequiredNetworkType(NetworkType.UNMETERED)
    .setRequiresCharging(true)
    .build()

// 3. 入队（周期性：每 6 小时一次）
val request = PeriodicWorkRequestBuilder&lt;SyncWorker&gt;(6, TimeUnit.HOURS)
    .setConstraints(constraints)
    .build()
WorkManager.getInstance(context).enqueueUniquePeriodicWork(
    "daily_sync", ExistingPeriodicWorkPolicy.KEEP, request)
```
:::

三个细节值得标注。第一，Result.retry() 会触发指数退避——系统自动把重试间隔拉长，避免无脑猛试。第二，enqueueUniquePeriodicWork 的"唯一名字"保证同一个任务不会重复入队——多次调用只是更新配置。第三，约束条件是"动态的"：用户没插充电器时任务就等着，插上才跑——这正是 WorkManager 比手写定时器聪明的地方，它把"什么时候能干活的判断"交给了系统。

#### 九、通知与前台服务：让用户"看得见"你的后台

前台 Service 必须挂通知——这不是负担，是与用户的契约：你在后台干什么，用户有权知道，也有权叫停。通知的构建在现代安卓里用 NotificationCompat + 通知渠道（NotificationChannel）：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 创建通知渠道并发出通知</span><span class="dots">···</span>
:::

```
// 创建渠道（应用首次启动时做一次即可）
val channel = NotificationChannel(
    "music", "音乐播放",
    NotificationManager.IMPORTANCE_LOW)   // 播放类通知用低优先级，不响不震
notificationManager.createNotificationChannel(channel)

// 发通知（前台 Service 里）
val notification = NotificationCompat.Builder(context, "music")
    .setContentTitle("正在播放")
    .setContentText("歌曲名 - 歌手")
    .setSmallIcon(R.drawable.ic_music)
    .setOngoing(true)                      // 常驻，不可滑掉
    .build()
```
:::

通知渠道是安卓 8.0 起的强制度设计：每个渠道一个独立的优先级与提醒方式，用户可以在系统设置里逐渠道关闭——所以"渠道规划"是产品级决策：音乐播放、下载进度、消息提醒各建一个渠道，别把所有通知塞进一个渠道让用户"要么全开要么全关"。这个设计思路在鸿蒙（第 74 章）和 iOS（第 68 章）里同样存在，只是 API 不同。

通知还有一条"礼貌守则"：只在"用户关心且需要打断"时才发。营销推送、每日签到提醒这类内容，用一次就删一次用户——安卓 13 起通知权限本身就是运行时申请的，用户不给你的通知权限，什么通知都发不出去。权限的珍贵程度，决定了通知的克制程度。

#### 十、权限请求：运行时权限的完整流程

四大组件里的权限话题在本章的落点是"怎么申请"。危险权限（位置、相机、麦克风、存储）必须运行时向用户申请，流程四步：

1. <strong>Manifest 声明</strong>：这是"申请资格"，漏了声明连弹窗都弹不出来；
2. <strong>检查是否已授权</strong>：每次使用前检查，用户可能改过主意；
3. <strong>申请并处理结果</strong>：用 rememberLauncherForActivityResult（Compose 里）发起，回调里处理"允许/拒绝"；
4. <strong>拒绝后的降级体验</strong>：用户拒绝不等于功能报废——设计降级路径（位置被拒就手动输入城市），并在合适的时机解释"为什么需要"（系统允许在拒绝两次后展示"不再询问"前的解释页）。

第六章的"权限最小化"原则在开发侧的落实就是：申请列表与功能强绑定（市场审核会查）、申请时机贴合使用场景、拒绝体验有降级方案。这三条做齐了，权限相关的差评和审核驳回就基本与你无缘。

#### 十一、三平台生命周期对照：一次学习，三处复用

你已经在本篇走完了安卓的生命周期，第 74 章还会走鸿蒙的，第 63 章已经走过 SwiftUI 的 scenePhase。三个平台的生命周期概念高度同构，把它们放进一张对照表，你会发现"学的是思路，记的是名字"：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">阶段</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">安卓（Activity）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">iOS（SwiftUI）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">鸿蒙（UIAbility）</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">创建与初始化</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onCreate</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">init / onAppear</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onCreate</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">窗口就绪</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStart</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onAppear</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onWindowStageCreate</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">前台交互</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onResume</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">scenePhase .active</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onForeground</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">退到后台</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onPause / onStop</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">scenePhase .background</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onBackground</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">销毁清理</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onDestroy</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onDisappear</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onDestroy</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">状态保存</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">rememberSaveable / savedStateHandle</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@SceneStorage / @AppStorage</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onSaveAbilityState</td></tr>
</tbody>
</table>
```
:::

这张表的正确用法不是背，而是"迁移时查"。比如你日后想给 iOS 版的记账本加"切后台自动保存"，看 iOS 列的"退到后台"对应 scenePhase .background——在 .onChange(of: scenePhase) 里触发保存即可。安卓篇学到的方法，在这张表的指引下迁移成本极低。这也是本书坚持三平台并排教学的核心理由：移动开发的通用素养，比单一平台的 API 记忆值钱得多。

对照表还有一个"防坑"价值：三平台对"后台停留时间"的策略不同——安卓的后台进程回收最激进，iOS 次之（有几分钟的宽限），鸿蒙介于两者之间。跨平台开发时，"切后台保存数据"这件事在安卓上最紧迫；而在 iOS 上，scenePhase 的变化通知可能在你写保存逻辑之前就已经发出——时序细节的差异，只有把三张生命周期图并排看过才能预判。

#### 十二、FAQ：八个最常问的问题

- <strong>问：onPause 和 onStop 我该用哪个保存数据？</strong>答：轻量的、必须尽快完成的（保存正在编辑的文字）放 onPause；重的、可以稍慢的（批量写入数据库）放 onStop。原则是 onPause 的时间会被用户感知，别让他等。
- <strong>问：应用被系统杀掉之前，会给我"临终遗言"的机会吗？</strong>答：不会——进程被杀是"无声"的。这就是为什么关键状态要在前台时就持久化（savedStateHandle / 数据库），而不是指望"被杀前的回调"。
- <strong>问：Compose 的 remember 和 rememberSaveable 到底差在哪？</strong>答：remember 活在"界面这一帧的组合"里，重组不丢、旋转丢；rememberSaveable 把值写进系统提供的存档，旋转重建后自动恢复。简单记：扛旋转用 Saveable，扛进程被杀用 ViewModel + savedStateHandle。
- <strong>问：为什么我按返回键退出后，进程还在？</strong>答：按返回销毁的是 Activity，进程可能还在后台缓存着（加快下次启动）。这不影响数据——Activity 销毁时的状态已经保存，下次启动走 onCreate 恢复。
- <strong>问：隐式 Intent 调用的 App 不存在会怎样？</strong>答：应用直接崩溃。所以调用前必须用 resolveActivity 检查是否有 App 能响应——这是隐式 Intent 的必配安全带。
- <strong>问：Service 和协程都是"后台"，选哪个？</strong>答：问自己"这个任务需要活多久、需要什么条件"。界面里的一次请求用协程；需要"保证执行"的后台同步用 WorkManager；需要持续运行的播放器用前台 Service。协程的生命周期跟着调用方，App 死它就死——不能承担"可靠性"职责。
- <strong>问：Compose 里怎么拿到生命周期？</strong>答：用 LifecycleEventObserver 监听 LocalLifecycleOwner 的状态变化，或用 collectAsStateWithLifecycle 让数据流跟随生命周期。UI 写在 Composable 里，生命周期感知的副作用用 LaunchedEffect + 生命周期状态组合实现。
- <strong>问：四大组件都要写在 Manifest 里，漏了会怎样？</strong>答：系统"找不到"该组件——启动它的 Intent 会直接抛异常。Manifest 是组件的户口本，开发新组件时第一件事就是去登记。

#### 十三、误区清单：六条"想当然"

- <strong>误区一：后台 Service 能一直活着</strong>——现代安卓对后台的限制越来越严，Service 也可能被系统回收。可靠的"后台"来自 WorkManager 的调度保证，不是 Service 的常驻。
- <strong>误区二：onDestroy 一定会被调用</strong>——进程被直接杀死时，onDestroy 不会执行。所以"清理动作"不能只依赖 onDestroy，重要资源的管理要用生命周期感知组件（自动跟随状态）。
- <strong>误区三：旋转屏幕可以在 Manifest 里"锁死"解决</strong>——锁方向确实避开了重建，但用户会举起手来横着用你的 App。正确解法是支持重建（状态保存），而不是对抗系统。
- <strong>误区四：前台 Service 想开就开</strong>——现代安卓要求前台 Service 有正当理由（播放、导航、健康数据记录），滥用会被系统限制甚至触发用户投诉。该用 WorkManager 的活别用前台 Service。
- <strong>误区五：putExtra 能传任何东西</strong>——它只支持基础类型和可序列化对象，而且有大小上限的实践约束（大对象会导致 TransactionTooLargeException 崩溃）。大文件传路径，不传内容。
- <strong>误区六：双击返回键退出是"标配"</strong>——这是老式交互的遗产。现代导航组件处理返回栈已经很自然，除非你的应用有明确的防误触需求，别硬加双击退出逻辑。

#### 十四、实战场景：用生命周期知识排一次真实的"案"

理论落地需要实战检验。来看一个真实感的排障案例，你跟着"侦探"走一遍，看看生命周期知识怎么用：

<strong>案情</strong>：用户反馈"在你们 App 里填了一半的表单，接了个电话回来，填的内容全没了"。电话是接了五分钟——时间不算短。<strong>排查第一步</strong>：复现。在表单页填几个字，模拟来电（另一台手机打过来），接听挂断后回来——复现了，内容确实丢了。<strong>第二步</strong>：看日志。开发版打上生命周期日志，重复上述操作：来电瞬间触发 onPause → onStop（全屏来电），挂断后 onRestart → onStart → onResume——中间没有 onDestroy，Activity 没销毁，只是切到后台。<strong>第三步</strong>：定位原因。表单内容存在 remember 里，切后台后界面没有被重建，为什么内容还是丢了？再查——原来是电话触发的是全屏来电界面，App 被切到后台超过 30 秒后系统回收了 Activity（内存压力下），重建时 remember 的值找不回来了。<strong>结案</strong>：把表单草稿迁移到 ViewModel，并在 onStop 里额外持久化到 Preferences 作为双保险。修复后，同样的操作流程，内容完好无损。

这个案例里用到的知识：生命周期回调顺序（判断是重建还是仅切后台）、remember 与 rememberSaveable/ViewModel 的存续差异（定位状态丢失）、onStop 持久化（最终修复方案）。一个真实 bug，动用了本章三节的知识——这就是"藏宝图"的价值。

#### 十五、给不同读者的学习路径建议

本章的深度对不同读者的需求不同，给你三条路径自行取用。<strong>纯新手</strong>：把一、二两节读懂，动手项做完即可，其余小节等遇到问题时回来查——第一次做项目不需要理解"进程被杀"的细节。<strong>有其他平台经验的人</strong>：直接看第十一节的对照表，把安卓的"名字"对到你熟悉的那套上，然后重点看第八节（WorkManager）——它是安卓独有的调度体系。<strong>准备面试的人</strong>：二、六、七、十二这四节是高频考点，特别是"状态保存三层"和"WorkManager 选型"，能把这两节的例子讲清楚，生命周期就算过关了。

不管选哪条路径，本章的动手项（给计数器装记忆、日志观察法）都强烈建议亲手做一遍——生命周期是"看不懂但一做就懂"的典型知识点，动手十分钟胜过阅读半小时。

#### 十六、launchMode 与任务栈：返回键背后的机制

按返回键为什么有时回到上一个页面，有时直接退出了应用？答案藏在"任务栈（Task）"与 launchMode 里。每个 Activity 启动时都会进入一个"任务栈"（后进先出），返回键就是"弹出栈顶"。而 launchMode 决定了"同一个 Activity 再次启动时，是新建一个实例还是复用已有的"。

- <strong>standard（默认）</strong>：每次启动都新建实例。连点五次按钮就创建五个——如果这是详情页，用户按五次返回才能退出，所以详情页用默认没问题，入口页千万别用默认。
- <strong>singleTop</strong>：如果目标 Activity 已在栈顶，就复用（触发 onNewIntent），不再新建。适合"搜索页"这类可能被连续触发的页面——用户连续搜索不会堆出十个搜索页。
- <strong>singleTask</strong>：整个任务栈里只有一个实例，再次启动时把上面的 Activity 全部弹掉。适合应用的主入口（首页）——从通知栏点回首页，不该在首页上面叠一个新首页。
- <strong>singleInstance</strong>：独占一个任务栈，全系统仅此一个实例。极少用，除非是"独立入口"型的特殊功能。

判断"该用哪种"的方法很简单：想象用户按返回键的预期。按了返回应该回到"上一个逻辑页面"——只要 launchMode 的行为符合这个预期就对了。别把 launchMode 当配置题背，把它当"返回键行为的控制器"来理解，选择就变得直觉化。

#### 十七、Intent Flag：比 launchMode 更细的控制粒度

launchMode 是"静态配置"，Intent Flag 是"启动时的动态微调"。三个最常用的 Flag：

- <strong>FLAG_ACTIVITY_CLEAR_TOP</strong>：启动已存在的目标 Activity 时，把它上面的全部弹掉。典型场景：通知栏点回来，直接回到首页而不是叠在当前页面之上；
- <strong>FLAG_ACTIVITY_SINGLE_TOP</strong>：配合 CLEAR_TOP 使用，如果目标已在栈顶则复用（触发 onNewIntent）而不是销毁重建；
- <strong>FLAG_ACTIVITY_NEW_TASK</strong>：在新任务栈中启动——从通知、桌面图标发起的启动通常带这个标志。

Compose + Navigation 的世界里，这些 Flag 大多数被 Navigation 组件封装了（导航栈的管理内置）。但理解它们的原理仍然必要：一是读老代码、读系统源码时需要；二是从通知栏点击进入应用的场景（PendingIntent）仍然要手动处理 Flag——处理不当会出现"点通知进来的页面，按返回退不出应用"的怪现象。

#### 十八、Activity 间数据共享：四种方案对比

"两个 Activity 之间怎么共享数据"是架构设计的经典问题，四种方案各有适用边界：

- <strong>Intent 传递</strong>：一次性、小数据（跳转时带上）。简单直接，但只是"单向、一次性的"；
- <strong>共享 ViewModel</strong>：同一 Activity 范围内（Compose 的页面间）共享状态——现代单 Activity 架构的主力方案；
- <strong>单例仓库（Repository/数据层）</strong>：跨页面、跨生命周期的数据源——记账本的所有账单数据都在仓库层，任何页面读写都是同一份；
- <strong>持久化（数据库/文件）</strong>：要活过应用重启的数据——终极方案，成本也最高。

选型原则：数据的"重要性"决定"持久层级"，数据的"共享范围"决定"共享方式"。临时草稿用 Intent 或 ViewModel，业务数据用仓库层，用户资产用持久化。第 53 章的数据层设计会把这个体系落到代码。

#### 十九、面试高频题精讲：生命周期五连问

生命周期是安卓面试的"保留节目"，五道高频题与答题要点——用本章的知识就能从容应对：

- <strong>Q1：从 A 页面跳到 B 页面，两边的生命周期顺序是什么？</strong>答：A.onPause → B.onCreate → B.onStart → B.onResume → A.onStop。记忆点：新页面完全显示后，旧页面才 onStop——中间的"交接棒"在 onPause 与 onResume 之间。
- <strong>Q2：旋转屏幕发生了什么？怎么处理？</strong>答：销毁重建（走完整生命周期循环），状态用 rememberSaveable/ViewModel/savedStateHandle 保住。答出"三层保存"是加分项。
- <strong>Q3：onSaveInstanceState 什么时候调用？</strong>答：Activity "可能被系统回收"之前（按主页键、进入其他应用）——旋转重建时也会调用。它与 onStop 的区别：onSaveInstanceState 的 Bundle 有大小限制（约 1MB 级别），只放关键恢复数据。
- <strong>Q4：什么情况下 App 会被系统杀掉？杀掉前有回调吗？</strong>答：内存不足时按"优先级"从低到高杀（后台的先死）。被杀是"无声"的，没有回调——所以关键数据的持久化不能指望"临终回调"，要在前台时就做好。
- <strong>Q5：singleTask 的 Activity 收到新 Intent 会怎样？</strong>答：不新建实例，而是把该实例带到前台、清除其上面的 Activity，并通过 onNewIntent 传递新 Intent——注意此时不会走 onCreate，处理新数据要在 onNewIntent 里。

面试答题的通用技巧也送你一个：每个答案都用"一句话结论 + 具体场景 + 修复方案"三段式回答——比背概念描述显得懂行得多。这些答题能力其实就是排障能力的变装：能把原理讲清楚的开发者，排查问题也快。

#### 二十、本章自测十题

- 1. 四大组件各自的职责是什么？用一句话说清，并说出各自的"现代替代品"（若有的话）。
- 2. 从 A 跳 B 再返回，完整的生命周期顺序？（提示：A 的 onStop 在 B 的 onResume 之后）
- 3. remember、rememberSaveable、ViewModel 三者分别扛得住什么？各举一个适用场景。
- 4. 显式 Intent 与隐式 Intent 的区别是什么？隐式调用前必须做什么检查？
- 5. 旋转屏幕后 "输入框内容丢失"，三种修复方案分别是什么？优先选哪种？
- 6. WorkManager 和 AlarmManager 的分工边界是什么？举一个各自必须使用的场景。
- 7. 前台 Service 为什么必须挂通知？通知渠道的作用是什么？
- 8. singleTop 和 singleTask 分别适合什么类型的页面？判断依据是什么？
- 9. 从通知栏点击启动 Activity 时，为什么要小心 FLAG_ACTIVITY_NEW_TASK 的栈行为？
- 10. "切后台回来数据丢了"的排查思路是什么？（参照本章第十四节的案例，说出三步）

十题全部能答上来，这一章就可以翻篇了。答不上来的，回对应小节再读——每一题的答案都在本章正文里，而且都用过"场景+修复"的方式讲过一遍。

#### 二十一、WorkManager 进阶：约束、重试与链式任务

第 8 节给了 WorkManager 的三步入门，进阶用法围绕三个维度展开：<strong>约束、重试、链式</strong>。掌握这三件事，WorkManager 就能承担绝大多数"可靠后台"的职责。

约束（Constraints）是任务执行的"前提条件"，系统会在条件满足时才调度任务：网络类型（ANY/METERED/UNMETERED——"仅 Wi-Fi"是最常用的约束）、充电状态、存储余量、设备空闲。多个约束是"且"的关系——全部满足才执行。约束的正确用法是把"业务对环境的要求"翻译给系统：同步任务要求 Wi-Fi（用户不想为同步烧流量），大文件处理要求充电中（耗电大户别在用户走路时啃电池）。

重试策略由 Result 决定：success 完成、failure 不再重试、retry 进入指数退避（默认 30 秒起、每次翻倍、上限由 BackoffPolicy 配置）。失败任务的合理姿势是：临时性错误（网络断开）返回 retry，永久性错误（参数非法）返回 failure——乱用 retry 会让一个注定失败的任务永远重试下去。

链式任务（WorkContinuation）让多个任务按顺序执行："下载 → 解析 → 入库"三条任务串成一条链，前一个成功才执行后一个。这在"多步骤数据处理"场景非常好用——每一步都是独立的 Worker（可单独测试），链式组织保证了执行顺序与失败中断。最后提醒一个工程细节：周期性任务的最小间隔是 15 分钟——这是系统的硬下限，更短间隔的需求要考虑 AlarmManager 或前台服务。

#### 二十二、进程优先级与"保活"的真相

"应用被杀"的机制值得说透，因为它解释了 Android 生态里"保活"产业的兴衰。系统按进程的"重要性"分级管理内存：前台进程（用户正在交互）最不容易被杀；可见进程（部分可见）、服务进程次之；后台进程（缓存）最容易被杀——系统按"最近使用时间"从旧到新清理。

很多应用想"常驻后台"（即时通讯、步数统计），早期生态里催生了各种"保活"黑科技（双进程守护、账户同步触发）。但现代安卓的态度非常明确：滥用保活伤害用户体验与续航，系统持续封堵这些手段，甚至会将"行为异常的应用"限制后台活动。正确的姿势是顺应系统的调度：用 WorkManager 的"保证执行"替代"常驻活着"，用高优先级消息推送（FCM）替代"进程常驻等消息"。

给学习者的建议直白一点：不要研究保活。把精力放在"应用被杀后能快速恢复状态"上——这个能力（状态保存三层）才是用户感知得到的、也经得起系统演进考验的。保活研究得越深，离安卓官方设计的意图越远。

#### 二十三、Intent 传大对象的正确姿势：路径凭证模式

前面提过 Intent 传大对象的坑，这里给出完整的"路径凭证模式"——处理图片、文件这类大资源的标准流程：

1. <strong>第一步：把大对象写入应用私有存储</strong>——拍到的照片先存到应用的 files 目录（或 MediaStore），得到一个 Uri；
2. <strong>第二步：Intent 只传 Uri 或文件路径</strong>——目标 Activity 通过这个"取货凭证"自己读取内容；
3. <strong>第三步：跨应用共享时用临时授权</strong>——通过 FLAG_GRANT_READ_URI_PERMISSION 把读取权临时授予对方（不暴露文件的真实路径），用完自动失效。

这个模式的名字叫"凭证"是因为：Intent 传递的是"取货凭证"而非"货物本身"——货物放在安全的仓库里，凭证指定取哪一件。它的好处：避免 Binder 传输的大小限制；避免大对象在多处持有内存；跨应用时不暴露真实路径。第 55 章的天气项目会用到"传城市名"（小数据直传），第 76 章的鸿蒙待办清单同样遵循这个模式——存储细节被数据层封装，Intent 只传 ID。

#### 二十四、本章知识地图：从"零件"到"系统"的完整框架

这一章的知识量在安卓篇数一数二，最后用一张"知识地图"帮你建立全景：

- <strong>组件层</strong>：四大组件是应用的"功能单元"——Activity 管界面、Service 管后台、Receiver 管广播、Provider 管共享；都在 Manifest 登记，都靠 Intent 协作；
- <strong>生命周期层</strong>：六个回调是"系统与应用的契约"—— onCreate 初始化、onStop 持久化、onDestroy 清理；旋转与配置变更是"高频考题"，rememberSaveable + ViewModel 是标准答案；
- <strong>导航层</strong>：Intent 管"跨应用/系统能力"，Navigation Compose 管"应用内页面栈"；单 Activity + Navigation 是现代架构主线；
- <strong>后台层</strong>：协程管当前任务、WorkManager 管可靠后台、AlarmManager 管精确时间、前台 Service 管用户可见的持续任务；选型口诀见第 8 节；
- <strong>状态层</strong>：remember → rememberSaveable → ViewModel → 数据库，四层按"丢了多心疼"逐级升级；savedStateHandle 专管"进程被杀恢复"。

这张地图在下一章（数据存储）和第 57 章（进阶之路）都会被反复引用——它们是安卓篇的"承重墙"。第 74 章的鸿蒙骨架、第 63 章的 iOS 生命周期，都会与这张地图一一对应。

#### 二十五、动手挑战：三天的小项目

本章的知识密度大，用一个小项目把它们"焊"进手感。三天节奏，每天 40 分钟：

<strong>第一天</strong>：建一个"灵感速记"应用——一个输入框 + 一个列表，用 rememberSaveable 保存输入内容，旋转屏幕验证不丢。<strong>第二天</strong>：接入 Navigation——添加"灵感详情"页，从列表点进去看全文；把生命周期日志加上，观察进出页面的回调序列。<strong>第三天</strong>：接入 WorkManager——写一个"每天晚上 9 点统计灵感数量"的后台任务，用约束条件限定"仅充电时执行"，跑起来后在 Logcat 里观察任务的执行时间（你会发现它未必精确在 9 点——这就是 WorkManager 的"可延迟"本性，符合预期）。

做完这个小项目，你会发现一个有趣的现象：这些知识在动手之前是"一坨概念"，动手之后变成"一套工具"——每一件都知道什么时候用、怎么用。这就是"项目驱动学习"的威力，也是第 76 章要带你做完整项目的原因。下一章，我们给这些灵感与数据一个正式的"家"：数据存储。

#### 二十六、深链接（Deep Links）：从网页直达你的应用内页面

深链接是 Intent 家族的"高阶玩法"：用户点一条短信里的链接，直接跳进你应用内的某个具体页面——不是打开应用首页，而是精确到"那个商品详情"或"那条订单"。它是电商、资讯类应用的核心竞争力：转化路径每少一步，成交率都会显著上升。

实现分两层。<strong>基础层：自定义 Scheme</strong>——在 Manifest 的 intent-filter 里声明 myapp:// 这类自定义协议，链接形如 myapp://product/42。简单，但浏览器可能拦截非 http 协议的链接。<strong>进阶层：App Links</strong>——用 https://yourdomain.com/product/42 的标准网址，并在网站根目录放置一个"资产声明文件"（assetlinks.json）证明域名归属。验证通过后，系统直接打开你的应用而跳过选择框——体验最顺滑，也是大厂的标准做法。

接住深链接的技术要点：深链接会拉起你的 Activity 并通过 Intent 传入完整链接——你需要在 onCreate 和 onNewIntent（应用已在后台时再次触发走这里）两处解析链接并导航到对应页面。两处都要处理，因为"冷启动"与"热启动"的入口不同。解析后的导航用 Navigation 跳转到目标页面——把链接的路径参数映射成导航参数，就完成了"网页 URL → 应用内页面"的翻译。

调试深链接有个快捷命令：<code class="inline">adb shell am start -a android.intent.action.VIEW -d "myapp://product/42"</code>——不用真发短信或网页，命令行直接模拟一次点击。把这条命令存进你的速查表，深链接开发会顺畅很多。

#### 二十七、ViewModel 实战：把第 51 章的计数器"升级"成生产级

第 51 章的计数器用了 remember——这一章讲过它的局限。现在用 ViewModel 把它升级成"生产级"，完整代码与逐行解释：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · CounterViewModel.kt</span><span class="dots">···</span>
:::

```
class CounterViewModel : ViewModel() {
    private val _count = MutableStateFlow(0)
    val count: StateFlow&lt;Int&gt; = _count.asStateFlow()   // 对外只读

    fun increment() {
        _count.value += 1
    }

    fun reset() {
        _count.value = 0
    }
}
```
:::

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 在 Composable 中使用</span><span class="dots">···</span>
:::

```
@Composable
fun CounterScreen(viewModel: CounterViewModel = viewModel()) {
    val count by viewModel.count.collectAsStateWithLifecycle()

    Column(horizontalAlignment = Alignment.CenterHorizontally) {
        Text("点击了 ${count} 次", style = MaterialTheme.typography.headlineMedium)
        Button(onClick = { viewModel.increment() }) {
            Text("点我")
        }
        TextButton(onClick = { viewModel.reset() }) {
            Text("归零")
        }
    }
}
```
:::

这段"生产级"代码与第 51 章的"教学级"代码有三个本质区别。第一，<strong>状态与 UI 分离</strong>：计数逻辑住在 ViewModel 里，界面只负责"渲染状态 + 调用方法"——单元测试可以直接测 ViewModel 而不需要界面。第二，<strong>只读暴露</strong>：对外暴露的是 StateFlow（只读），修改只能通过方法——外部无法"绕过逻辑"乱改状态。第三，<strong>生命周期安全</strong>：collectAsStateWithLifecycle 让订阅只在界面可见时激活，切到后台自动停止——避免后台刷新浪费资源或引发崩溃。

把这套模式记住：它是本书安卓篇所有后续项目（记账本、天气助手）的标准结构。第 53 章的数据层会以同样的分层思路接进来——ViewModel 调用仓库，仓库调用数据源，各层职责分明。

#### 二十八、常见 bug 集锦：五个真实翻车与修复

本章知识点的"事故现场"集中复盘——每个 bug 都是真实项目里高频出现的，修复方案就用本章讲过的知识。

- <strong>Bug 1：切后台回来，网络请求结果"丢了"</strong>——请求写在 Composable 的 remember 协程里，旋转后协程取消、结果丢失。修复：请求移到 ViewModel（viewModelScope 里），界面只观察结果。
- <strong>Bug 2：通知点了没反应，或者点开是"旧页面"</strong>——PendingIntent 的 Intent 没设置 Flag 或没处理 onNewIntent。修复：通知的 PendingIntent 加 FLAG_UPDATE_CURRENT + 正确的 Flag 组合，并在 onNewIntent 里处理导航。
- <strong>Bug 3：应用从最近任务恢复后，列表回到顶部</strong>——列表滚动位置存在 remember 里，进程被杀恢复后丢失。修复：滚动位置或关键状态放 savedStateHandle / 持久化。
- <strong>Bug 4：后台同步任务"永远不执行"</strong>——WorkManager 设置了"仅 Wi-Fi"约束，但用户环境没有 Wi-Fi。修复：约束是有意设计（省流量），检查设备状态或在设置里给用户"立即同步（消耗流量）"的选项。
- <strong>Bug 5：旋转屏幕后弹窗消失了</strong>——弹窗用 remember 状态控制显示，旋转后状态丢失。修复：弹窗状态用 rememberSaveable，或用 Dialog 组件的"状态由 ViewModel 驱动"模式。

五个 bug 的共同点：都可以用本章的"三层状态保存"与"生命周期知识"预防。排查它们的通用方法也送你一句：<strong>先看日志里的生命周期序列，再查状态放在哪一层</strong>——十次有八次，问题出在"状态放错了层"。

#### 二十九、术语速查表：本章全部概念一行定义

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">术语</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">一行定义</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activity</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">有界面的应用组件，生命周期与状态保存的核心载体</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Service</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">无界面的后台组件，前台 Service 需挂常驻通知</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BroadcastReceiver</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">接收系统或应用广播的组件</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ContentProvider</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跨应用共享数据的组件</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">生命周期回调</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onCreate/onStart/onResume/onPause/onStop/onDestroy 六段</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Intent</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">组件通信的"意图"载体，显式与隐式两种</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">任务栈（Task）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activity 的后进先出栈，返回键弹栈顶</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">launchMode</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">standard/singleTop/singleTask/singleInstance 四种启动模式</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">配置变更</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">旋转/深色模式/字体等触发 Activity 重建的事件</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">rememberSaveable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">扛过配置变更的临时状态保存</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ViewModel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跨配置变更存活的界面级状态容器</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">savedStateHandle</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">进程被杀恢复用的关键状态存档</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">WorkManager</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可延迟后台任务的可靠调度器</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AlarmManager</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">精确定时触发器</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">通知渠道</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">通知的分组与优先级容器（用户可逐渠道关闭）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">深链接</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">从外部直达应用内特定页面的链接</td></tr>
</tbody>
</table>
```
:::

速查表的用法：遇到概念想不起来时按表查一行，深入细节回正文对应小节。它也是"复习提纲"——面试或考试前，把这张表从头到尾过一遍，本章的骨架就都在脑子里了。

#### 三十、给下一章的"接口"：数据层在等你

本章的待办清单和计数器还有一个"不完美"：数据放在内存里，应用彻底退出就没了。这不是遗漏——数据持久化是下一章的主角：Preferences、RelationalStore（SQLite）、文件系统三套方案各管一类数据，第 76 章的鸿蒙待办清单会把同样的分层思想用在 ArkTS 里。

你已经准备好了：本章建立的 ViewModel 结构正是"挂载数据层"的标准位置——ViewModel 调用仓库，仓库操作数据库或发起网络请求，界面只管渲染。下一章见。

#### 三十一、Lifecycle 库：生命周期感知组件的基石

手动在六个回调里"注册/注销"资源（ onStart 开始监听、onStop 停止监听）写多了很繁琐还容易漏。Jetpack 的 Lifecycle 库提供了优雅的解法：<strong>生命周期感知组件</strong>——把"跟随生命周期"的逻辑封装成对象，框架自动在正确的时机调用它。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 生命周期感知组件</span><span class="dots">···</span>
:::

```
class MyLocationListener(
    private val context: Context,
    private val lifecycle: Lifecycle,
    private val callback: (Location) -&gt; Unit
) : DefaultLifecycleObserver {

    override fun onStart(owner: LifecycleOwner) {
        // 生命周期开始时自动启动监听
        startListening()
    }

    override fun onStop(owner: LifecycleOwner) {
        // 生命周期结束时自动停止——不需要手动在 Activity 里调
        stopListening()
    }

    private fun startListening() { /* ... */ }
    private fun stopListening() { /* ... */ }
}

// 在 Activity 里一行挂载：
// lifecycle.addObserver(MyLocationListener(this, lifecycle, callback))
```
:::

这个模式的威力在于"自动对齐"：组件自己知道生命周期到了哪一步，该启动启动、该停止停止——Activity 的回调代码从此干净，资源泄漏的风险也大幅降低。Compose 时代更进一步：DisposableEffect + LifecycleEventObserver 把同样的能力带进了声明式世界（第 51 章提过 LaunchedEffect 的生命周期安全，底层就是这套机制）。

Lifecycle 还有两个状态查询能力：lifecycle.currentState（当前状态）与 isAtLeast(STARTED)（至少可见）——在异步回调里判断"界面还在不在"特别有用：网络请求回来时，先检查界面是否还活着，活着才更新 UI（否则更新会抛异常或白做）。collectAsStateWithLifecycle 的内部就是这套判断。

#### 三十二、实战：给表单加"切后台自动保存"

把本章的知识合成一个实战功能：表单页的"切后台自动保存"。需求：用户填表时来电话切走，回来内容还在；更进一步，就算进程被杀，重新打开时草稿也还在。实现三层：

- <strong>第一层：ViewModel 里的"活状态"</strong>——表单的所有字段放 ViewModel 的 StateFlow，旋转与短暂切后台都靠它扛；
- <strong>第二层：onStop 时的"即时保存"</strong>——在 Activity 的 onStop 里把 ViewModel 的当前表单内容写入 Preferences（几毫秒的轻量操作，不卡用户感知）；
- <strong>第三层：onCreate 时的"草稿恢复"</strong>——检测到有草稿（Preferences 里有值），弹出"恢复草稿？"的提示，用户确认后读回 ViewModel。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · onStop 保存草稿</span><span class="dots">···</span>
:::

```
override fun onStop() {
    super.onStop()
    // 从 ViewModel 取当前表单内容，写入 Preferences
    lifecycleScope.launch {
        preferences.edit()
            .putString("draft_title", viewModel.title.value)
            .putString("draft_body", viewModel.body.value)
            .apply()
    }
}
```
:::

这三层实现用了本章与第 51 章的四个概念：ViewModel（状态容器）、onStop（保存时机）、Preferences（轻量持久化）、lifecycleScope（生命周期感知的协程）。一个真实功能，四个知识点各就各位——这就是"框架式学习"的成果：每个知识点都在系统里找到了自己的位置。

#### 三十三、本章知识在真实项目里的应用清单

最后把"这些知识会在项目的哪一步被用到"列成清单——当你做第 54 章的记账本项目时，可以按图索骥：

- <strong>列表页的旋转保活</strong>：记账列表的滚动位置、筛选状态 → rememberSaveable + ViewModel（本章第七节）；
- <strong>输入页的草稿保存</strong>：金额输入到一半切电话 → onStop 持久化 + onCreate 恢复（本章第三十二节的三层实现）；
- <strong>后台同步</strong>：每日云端备份 → WorkManager + 网络约束（本章第八节）；
- <strong>统计通知</strong>：月底"本月支出汇总" → 通知渠道 + 定时触发（本章第九节）；
- <strong>权限申请</strong>：导出 CSV 需要存储权限 → rememberLauncherForActivityResult（本章第十节）；
- <strong>深链接直达</strong>：点击通知跳到"某笔账单详情" → 深链接 + onNewIntent 处理（本章第二十六节）。

这张清单的意义在于"知识到应用的映射"——学完一章，你知道它的每个知识点会在项目里的哪个位置发光。下一章的数据层，就是这张清单里"账单持久化"的地基。带着这张地图，开始第 53 章吧。

#### 三十四、Compose 与生命周期的"新契约"：副作用 API 全家福

本章讲的生命周期是 Activity 层的，Compose 层还有一套"副作用 API"——它们是 Composable 与外部世界（网络、存储、传感器）打交道的正规渠道，也各自绑定了生命周期。五个常用副作用，各自的用途与触发时机：

- <strong>LaunchedEffect(key)</strong>：进入组合时启动协程，key 变化时重启协程，离开组合时取消。异步请求的标准写法——"当 city 参数变化时重新请求天气"就是 LaunchedEffect(city)；
- <strong>rememberCoroutineScope</strong>：在事件回调里启动协程（比如按钮点击时提交表单）。LaunchedEffect 是"组合驱动"，这个是"事件驱动"——两者别混用；
- <strong>DisposableEffect</strong>：需要"清理"的副作用（注册监听器、开启 GPS）——进入组合时执行，离开时执行 onDispose 清理。它就是"Compose 版的 onStart/onStop"；
- <strong>SideEffect</strong>：每次成功重组后都要执行的非挂起操作（把状态同步给非 Compose 的对象）；
- <strong>rememberUpdatedState</strong>：让长时运行的协程总能拿到"最新的回调值"——避免协程捕获旧值导致逻辑错误。

五个副作用的选择逻辑一句话：<strong>跟状态走用 LaunchedEffect，跟用户操作走用 rememberCoroutineScope，需要清理用 DisposableEffect，其余罕见场景用 SideEffect/rememberUpdatedState</strong>。第 51 章的"声明式"思路在这里的延伸：连"副作用"都要声明其生命周期绑定关系——这是 Compose 安全性的重要组成。

副作用 API 与本章的 Activity 生命周期的关系也要理清：LaunchedEffect 的生命周期是"组合"级别（进组合启动、出组合取消），而 Activity 的生命周期是"应用窗口"级别（onStart/onStop）。一个界面的组合嵌在 Activity 的生命周期之内——Activity onStop 时组合虽然"还在"，但通常你应该用 collectAsStateWithLifecycle 暂停数据订阅。两层生命周期都要顾及，才是完整的生命周期管理。

#### 三十五、单元测试入门：给 ViewModel 写第一组测试

本章的 ViewModel（计数器、表单）逻辑清晰、无界面依赖——正是单元测试的最佳对象。给它们写测试是"学习本章知识"的最强验收方式：测试通过，说明你真的理解了状态流转。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · CounterViewModel 的单元测试</span><span class="dots">···</span>
:::

```
class CounterViewModelTest {
    private lateinit var viewModel: CounterViewModel

    @Before
    fun setup() {
        viewModel = CounterViewModel()
    }

    @Test
    fun `初始值为零`() {
        assertEquals(0, viewModel.count.value)
    }

    @Test
    fun `点击一次后为一`() {
        viewModel.increment()
        assertEquals(1, viewModel.count.value)
    }

    @Test
    fun `连续点击三次后为三`() {
        repeat(3) { viewModel.increment() }
        assertEquals(3, viewModel.count.value)
    }

    @Test
    fun `重置后归零`() {
        viewModel.increment()
        viewModel.increment()
        viewModel.reset()
        assertEquals(0, viewModel.count.value)
    }
}
```
:::

四个测试覆盖了"正常路径、多次操作、边界重置"三类场景。测试的名字用反引号写成中文句子——这是 Kotlin 的特性，测试名即"需求描述"，读测试就是读需求。ViewModel 的测试不需要模拟器、不需要 Android 框架——纯 JVM 上毫秒级完成，这就是"把逻辑放 ViewModel"的另一个红利：可测试性。

测试的运行方式：在 Android Studio 里点击测试类旁边的绿色三角即可。测试文件放在 src/test/java 目录（注意不是 androidTest——那是仪器测试，需要真机或模拟器）。第 45 章的质量保障方法论在这里的落地就是：核心逻辑都有单元测试，改代码前先跑一遍，测试全绿再提交。

#### 三十六、本章学习复盘：从"概念清单"到"能力清单"

全章三十多节的内容，最后收拢成一份"能力清单"——读完本章后，你应该能做到的每一件事。用"能/不能"自测一下，不能的条目回对应小节补课：

- <strong>能说出</strong>四大组件各自的职责，以及"现代安卓开发中哪些还在高频使用"；
- <strong>能画出</strong>Activity 的生命周期图，并解释每个回调的典型用途与翻车场景；
- <strong>能实现</strong>状态保存的三层方案：rememberSaveable（临时）、ViewModel（界面级）、数据库（永久）；
- <strong>能使用</strong>Intent 的显式与隐式两种方式，并理解深链接的两层实现；
- <strong>能搭建</strong>Navigation Compose 的多页面导航，并理解单 Activity 架构的趋势；
- <strong>能选对</strong>后台任务工具：协程 / WorkManager / AlarmManager / 前台 Service；
- <strong>能写出</strong>WorkManager 的三步代码（定义任务/约束/入队），并理解约束与重试；
- <strong>能解释</strong>通知渠道的设计意图，并写出合规的前台服务通知；
- <strong>能完成</strong>运行时权限的完整流程（声明→检查→申请→降级）；
- <strong>能使用</strong>Compose 的副作用 API（LaunchedEffect/DisposableEffect 等）并理解其生命周期绑定；
- <strong>能给 ViewModel 写单元测试</strong>，理解"逻辑放 ViewModel"带来的可测试性红利。

十一条能力就是本章的"毕业标准"。达标后，你对安卓应用"骨架"的理解已经超过大部分初学者——下一章的数据层、第 54-56 章的实战项目，都会建立在这套骨架之上。带着你的能力清单，进入第 53 章吧。

#### 三十七、SavedStateHandle：ViewModel 里的"小保险柜"

第七节讲了状态保存的三层分工，其中"进程死亡恢复"这一层，现代做法是把要救的临时状态放进 ViewModel 的 SavedStateHandle——它像 ViewModel 内置的一个小保险柜：进程被杀前系统把里面的数据落盘，恢复时原样还给你。

用法上一句话就能说清：ViewModel 的构造函数里接收 <code>savedStateHandle: SavedStateHandle</code>，把"丢了会很疼"的 UI 态（当前选中的标签页、正在输入的搜索词、列表滚动到的筛选条件）用 <code>handle["key"] = value</code> 存进去，恢复时直接读。它能存的数据量很小（Binder 事务限制在 1MB 上下文内，实际建议只存几百 KB 以内的键值对），所以定位明确：<strong>只存"钥匙"，不存"行李"</strong>——表单全文存 DataStore，搜索关键词存 SavedStateHandle。

三个容易犯的错：一，把大对象塞进去导致恢复时 TransactionTooLargeException 崩溃，日志里只给一行晦涩的提示，很多新手卡在这里一晚上——记住保险柜只收小件；二，把可以从数据库重算出来的数据也存进去，导致"保险柜里的"和"数据库里的"两份数据互相矛盾，恢复后界面状态撕裂——能重算的不存；三，忘了它随进程恢复而不是随 Activity 恢复，测试时以为没生效——用下面第四十节的"不保留活动"开关才能测出真实效果。

#### 三十八、Activity Result API：告别 onActivityResult 的现代方式

老教程里的 <code>onActivityResult()</code> 写法已经被官方标记为过时：请求和回调分散在两处、每个请求一个 requestCode、类型全靠人脑对应。现代方案是 Activity Result API——"请求什么"和"拿到结果干什么"写在一起，类型安全，还和 Compose 天然配合。

三个最高频场景的写法套路：请求单个权限，用 <code>registerForActivityResult(RequestPermission())</code> 拿到布尔结果，配合第十节的"该不该解释"逻辑决定弹系统框还是先弹解释框；拍一张照片，用 <code>TakePicturePreview()</code> 或 <code>TakePicture()</code> 合约，后者还要配 <code>FileProvider</code> 指定照片保存位置；从文件选择器拿文件，用 <code>OpenDocument()</code> 合约拿回 URI，再用 ContentResolver 读内容。注意注册时机：register 必须在 Activity STARTED 之前完成（Compose 里放在 composable 函数体顶层即可），放在按钮点击回调里注册会直接抛异常——这是新手最常见的崩溃来源。

它和第三十四节副作用 API 的配合也值得记一笔：在 Compose 里，把 launcher 的调用包在 onClick 里、把结果用 rememberUpdatedState 转成状态，结果一回来 UI 自动刷新，全程没有一行"手动刷新界面"的胶水代码。你在第 51 章学的"状态驱动 UI"在这里第一次体现威力。

#### 三十九、预测性返回：返回手势也要"预览"了

从 Android 14 引入、15 之后逐步成为默认，"预测性返回"（Predictive Back）改变了返回键的观感：上滑返回时，系统会先给你一个当前页面缩小、露出上一页的"预览动画"，你松手才算真的返回——就像 iOS 上早就习惯的那种"看到要回到哪"的手势体验。

对开发者的影响集中在三件事。第一，拦截返回不再用重写 <code>onBackPressed()</code>，而要用 OnBackPressedDispatcher 注册回调——老写法在新目标版本上会被忽略，表现为"我的双击退出逻辑突然失效了"。第二，只有声明了 <code>android:enableOnBackInvokedCallback="true"</code> 的应用才启用预测性行为，老应用暂时还能用旧行为，但方向已经确定：迟早强制。第三，自定义的"确认退出"对话框、抽屉关闭、搜索页清空——这些拦截逻辑都应该迁移到 Dispatcher，并保证每个回调只处理自己范围内的返回事件，避免两个模块抢同一个返回键。

给新手的教学建议：新项目从一开始就统一用 Dispatcher 写返回逻辑，别再抄老教程的 onBackPressed；老项目迁移时全局搜"onBackPressed"，逐个改造并用手势真机验证预览动画正常——这项改造不大，但它决定你的 App 在新系统上"手感"是否跟得上时代。

#### 四十、配置变更实测：用开发者选项把"翻车"提前暴露

生命周期知识学完，最后一课是怎么"主动制造事故"来验证自己的代码——等到用户在真机上帮你发现，代价就大了。开发者选项里有两个开关是 Android 开发者的"压力测试器"：

<strong>"不保留活动"（Don't keep activities）</strong>：每次离开 Activity 就立刻销毁它。开着它把 App 正常用十分钟——切后台再回来、页面间跳转再返回——凡是出现"回来后白屏、数据丢了、输入框清空"的页面，就是状态保存没做。这正是第七节三层方案和第三十七节 SavedStateHandle 的验收现场。

<strong>"更改显示大小/强制深色"</strong>：触发最常见的两类配置变更（density 和 uiMode）。强制深色切一下，看有没有页面闪崩或布局错乱——特别是那些把颜色写死在代码里而不是主题资源里的页面；改显示大小，看布局在"特大字体"下是否还能正常显示——这也是第二十七章适老化检查的日常工作之一。

建议把它变成习惯：每个新页面写完，开着"不保留活动"来回用一遍再提交代码。两分钟的测试，挡住的是线上最难复现的那一类"偶发白屏"。生命周期不是背出来的，是被这些开关"折腾"出来的肌肉记忆。

::: div .tip-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>一句话记牢

{class="mt-1"}
小状态进 SavedStateHandle，大状态进 DataStore，跨页面请求走 Activity Result，返回拦截统一 OnBackPressedDispatcher；提交前开着"不保留活动"折腾一遍——生命周期这关就算真过了。
:::

如果这一章的四十个小节让你有些"消化不良"，回到第三十六节的复盘清单重新排个序：先扎实的生命周期与状态保存（一、二、七、三十二），再 Intent 与导航（三、四、十六、二十三），后台与权限（八、九、十、二十一）紧随其后，剩下的进阶专题按需取用。四大组件不是一天建成的——但它值得你花一周慢慢建。

把这句话写在你贴工位的那张便利贴上：界面是状态的函数，生命周期是状态的家。

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 四大组件：Activity（门面）、Service（后台）、BroadcastReceiver（喇叭）、ContentProvider（资料柜）
- 生命周期六回调：onCreate → onStart → onResume → onPause → onStop → onDestroy
- 旋转屏幕会销毁重建 Activity：用 rememberSaveable 保住状态
- Intent 是"车票"：显式跳自家页面，隐式调系统能力
- 多页面用 Navigation Compose：NavHost + composable 路由
- Compose 没换掉系统层：生命周期与四大组件照旧管用，后台活儿多想想 WorkManager
:::
