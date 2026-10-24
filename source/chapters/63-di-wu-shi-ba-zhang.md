---
id: di-wu-shi-ba-zhang
num: 58
part: an-zhuo-kai-fa-pian
nav: 第五十八章：速查手册与资源
toc: default
kind: chapter
---

### 第五十八章：速查手册与资源

{class="chapter-intro mb-4"}
本章是一份可以独立使用的速查手册。当你记不清某个写法或需要快速决策时，直接翻到这里。建议把它当成"口袋卡片"：常用代码速查、常见问题、学习资源，一页不落。

#### 一、常用代码速查卡

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要做什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">关键代码</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">记住一个可变状态</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">var x by remember { mutableStateOf(初值) }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">转屏不丢状态</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">rememberSaveable { mutableStateOf(初值) }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">竖排/横排布局</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Column { }</code> / <code class="inline">Row { }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">懒加载列表</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">LazyColumn { items(列表) { ... } }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">页面跳转</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">navController.navigate("路由")</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">协程里干等活儿</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">viewModelScope.launch { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">观察数据流</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">val list by flow.collectAsState()</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">存小配置</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">context.dataStore.edit { it[KEY] = 值 }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">存结构化数据</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room 三件套：@Entity / @Dao / @Database</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">联网取数据</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit 接口 + suspend 函数</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">发通知</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">NotificationChannel + NotificationCompat.Builder</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">打日志</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Log.d("TAG", "message")</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
安卓开发速查卡（2026 年 8 月版）

#### 二、常见问题 FAQ

<strong>Q1：我完全不会编程，学安卓开发要多久？</strong>

按本书路径走：第 1-2 周装环境、学 Kotlin 基础；第 3-4 周学 Compose 做出界面；第 5-6 周完成记账本项目；第 7-8 周做完天气项目。<strong>两个月，从零到能独立做小 App</strong>。前提是每天投入 1-2 小时，且动手敲代码而不是只看书。

<strong>Q2：Java 还要学吗？</strong>

不用。新项目、新教程、新岗位基本都以 Kotlin 为准。只在"维护十年老项目"时才会遇到大量 Java。学完 Kotlin 后如果工作需要，再补 Java 会很快——两者底层是同一个虚拟机生态。

<strong>Q3：模拟器还是真机？</strong>

开发调试用模拟器方便（快照、多机型），但<strong>验收必须过真机</strong>——触感、性能、真网络、传感器，模拟器替代不了。条件允许，买一台中端真机当测试机，是最划算的投资。

<strong>Q4：安卓开发好找工作吗？</strong>

2026 年的行情：纯"会写界面"的初级岗位竞争激烈，但"懂 Kotlin + 会架构 + 有上线作品"的开发者依然抢手。学习期的你，<strong>最好的简历就是商店里那个自己做的 App</strong>。

<strong>Q5：遇到报错卡住了怎么办？</strong>

黄金三步：① 把报错第一行原样搜 StackOverflow/搜索引擎；② 查官方文档对应页面；③ 还不行，就把"期望行为 + 实际现象 + 报错全文 + 相关代码"打包发给 AI 或社区提问。绝大多数问题，第一步就解决了。

#### 三、推荐学习资源

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">类型</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">资源</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">推荐理由</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">developer.android.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">安卓官方文档，Compose/Kotlin 教程都在里面，第一权威</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin 官网 (kotlinlang.org)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">语言官方文档 + 在线演练场</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Google Codelabs</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">手把手的分步实验课，新手友好度满分</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">社区</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stack Overflow (android 标签)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">报错求救第一站</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">社区</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">掘金 / CSDN 安卓专区</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">中文实战文章多，注意甄别新旧（先看日期）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">视频</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Google Developers 官方频道</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每年的开发者大会新技术讲解</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">配套</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第七篇《AI编程实战篇》（第37-47章）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用 AI 辅助安卓开发的完整心法</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
安卓开发学习资源清单（2026 年 8 月）

#### 四、Gradle 常用命令速查

平时点按钮就够，但命令行有时更高效（尤其是配合 AI 工具或 CI 流水线时）：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">命令</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">作用</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew assembleDebug</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">打一个调试版 APK（Windows 把 ./ 去掉）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew assembleRelease</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">打发布版（需配好签名）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew test</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跑全部单元测试</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew lint</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">静态检查：找出潜在 bug 和不规范写法</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew clean</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">清空构建产物（"重启大法"的编译版）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew :app: dependencies</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">查看依赖树（排查版本冲突神器）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Gradle 常用命令速查

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：构建出问题先 clean

{class="mt-1"}
"昨天还能跑今天就不行"的灵异事件，十有六七是构建缓存错乱。<code class="inline">./gradlew clean</code> 之后重新构建，能治愈一大半玄学问题。还不行再重启 Android Studio——这招请配合 File → Invalidate Caches 一起服用。
:::

#### 五、结语：从第一个 App 到第 N 个 App

回头看，你从"不知道 Activity 是什么"，到装好环境、学会 Kotlin、用 Compose 画出界面、给 App 接上数据库和网络，再到测试、打包、上架——<strong>这条路上你已经走完了从零到一最难的一段</strong>。

技术的世界变化很快：框架会升级，工具会换代，AI 会接手越来越多"敲键盘"的活。但有一样东西不会过时：<strong>你把一个模糊的想法，拆解成清晰的步骤，再一步步实现它的能力</strong>。工具是放大器，思路是地基。放大器可以替换，地基不能动摇。

:::inline div .quote-line
你不再只是"会玩手机的人"。你能把脑海里的想法，变成三亿安卓设备上真实运行的 App。从今天开始，用键盘去创造——这就是安卓开发者的浪漫。
:::

#### 参考文献

{class="list-decimal pl-6 mb-3 space-y-1 text-xs text-gray-500"}
1. Android Developers. (2026). Android Developer Guides and Jetpack Compose Documentation. developer.android.com.
2. Kotlin Foundation. (2026). Kotlin Language Documentation. kotlinlang.org.
3. Android Open Source Project. (2026). Android Platform Version History and API Levels.
4. Google Play. (2026). Play Console Help: Publishing and App Signing.
5. AndroidX Release Notes. (2026). Room / DataStore / Navigation / WorkManager releases.
6. Square. (2026). Retrofit Documentation. github.com/square/retrofit.
