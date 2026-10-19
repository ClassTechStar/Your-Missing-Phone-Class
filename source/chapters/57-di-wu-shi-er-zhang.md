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

#### 一、四大组件：安卓的"四梁八柱"

安卓官方定义了四种基本组件，分别负责一类工作：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">组件</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">职责</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">打个比方</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activity</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一个可见的界面</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">店铺的门面——用户能看见、能交互</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Service</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">后台干活的"隐形人"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">仓库工人——放音乐、下载文件，不需要界面</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BroadcastReceiver</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">接收系统广播</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">传达室——"电池没电了""网络断了"的喇叭</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ContentProvider</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跨 App 共享数据</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">公共资料柜——比如把联系人共享给别的 App</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
安卓四大组件速览

新手阶段你 95% 的时间都在跟 <strong>Activity</strong> 打交道；Service 和 BroadcastReceiver 做音乐播放、消息推送时会用到；ContentProvider 用得最少（系统已把常用数据封好了）。另外注意：四大组件都要在 <strong>AndroidManifest.xml</strong> 里"登记户口"，不登记系统就找不到它们。

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

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>避坑提醒：屏幕旋转会"杀死"Activity

{class="mt-1"}
新手最经典的翻车现场：App 转一下屏幕，输入框里的字全没了。原因：旋转屏幕默认会销毁并重建 Activity（走一遍 onDestroy → onCreate）。解法：用 <code class="inline">rememberSaveable</code> 保存状态（Compose 里替代 remember），它会在重建时自动把值找回来。第 6、7 章会反复用到。
:::

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

#### 五、顺带认识：Fragment 是什么（以及为什么本书没教）

查老教程时你一定会撞见 <strong>Fragment</strong>——它是 Activity 里的"可复用界面片段"，在老式多页面架构里是绝对主角。但 Compose 时代，页面直接用 Composable 函数 + Navigation 路由就够了，官方也已弱化 Fragment 的地位。本书因此没把它放进主线。

给你的建议：<strong>新项目不主动用 Fragment</strong>；但读老代码、面试被问到时，知道它是"Activity 里嵌的界面片段"即可。学习资源永远优先选 2023 年以后的——安卓技术栈的"老黄历"更新得比想象中快。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：给计数器装上"记忆"

{class="mt-1"}
把第 51 章的计数器改造一下：① 把 remember 换成 rememberSaveable，旋转屏幕验证数字还在；② 加一个"关于"按钮，用 Navigation 跳到第二个页面显示版本号；③ 在两个页面的 onCreate/onPause 里打印日志（Log.d），用 Logcat 观察生命周期调用顺序。做完这三步，生命周期就不再是纸上谈兵。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 四大组件：Activity（门面）、Service（后台）、BroadcastReceiver（喇叭）、ContentProvider（资料柜）
- 生命周期六回调：onCreate → onStart → onResume → onPause → onStop → onDestroy
- 旋转屏幕会销毁重建 Activity：用 rememberSaveable 保住状态
- Intent 是"车票"：显式跳自家页面，隐式调系统能力
- 多页面用 Navigation Compose：NavHost + composable 路由
:::
