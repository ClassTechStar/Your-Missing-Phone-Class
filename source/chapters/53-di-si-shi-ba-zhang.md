---
id: di-si-shi-ba-zhang
num: 48
part: an-zhuo-kai-fa-pian
nav: 第四十八章：认识安卓——从操作系统到开发生态
toc: default
kind: chapter
---

### 第四十八章：认识安卓——从操作系统到开发生态

{class="chapter-intro mb-4"}
恭喜你做出这个决定——从"玩手机的人"变成"做手机应用的人"。在动手之前，咱们先把地图摊开：安卓从哪里来？为什么全世界的开发者都在给它写应用？一个 App 从你的手指敲键盘到用户手机上，中间都发生了什么？

#### 一、安卓的身世：从"小机器人"到"全球最大系统"

安卓（Android）的故事始于 2003 年——一个叫 Andy Rubin 的工程师创办了 Android 公司，目标很朴素：做一套"更懂相机"的智能操作系统。后来谷歌在 2005 年收购了它，2007 年联合几十家厂商成立开放手机联盟（OHA），2008 年 9 月，第一款安卓手机 HTC Dream（G1）正式发售。

后面的故事大家都知道了：到 2026 年，<strong>安卓是全球市场份额最大的移动操作系统，活跃设备数以十亿计</strong>。你的手机、电视盒子、车载大屏、智能手表，很可能都在跑安卓。这意味着什么？意味着你写的每一行代码，都有机会被世界上最多的人用到。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：安卓的开源基因

{class="mt-1"}
安卓的核心代码（AOSP，Android Open Source Project）是开源的——任何厂商都能拿去修改定制。所以小米有 MIUI（现在叫澎湃 OS）、华为有鸿蒙兼容层、三星有 One UI。这对开发者是好事：<strong>你学的是"安卓开发"，不是"某个品牌的开发"</strong>，一套功夫，全网通吃。
:::

版本号的进化也很有意思：从 1.5 的纸杯蛋糕（Cupcake）开始，每个大版本都以甜点命名——甜甜圈、闪电泡芙、冻酸奶、姜饼……一直到 2019 年的安卓 10 才改成了纯数字。到 2026 年 8 月，最新正式版是 <strong>Android 17</strong>，而开发时你真正需要关心的"最低支持版本"，主流 App 一般定在 Android 8（API 26）到 Android 10（API 29）之间——<strong>支持到几年前的设备，你的用户盘子才够大</strong>。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">版本</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">代号/年份</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">对开发者重要的事</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 8 (API 26)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Oreo · 2017</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">通知渠道、后台限制——很多老机型的最低线</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 10 (API 29)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2019</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分区存储登场，文件访问规矩大改</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 12 (API 31)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2021</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Material You 动态取色，界面观感大升级</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 13 (API 33)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2022</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">运行时通知权限，弹窗问你"准不准发通知"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 14-15 (API 34-35)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2023-2024</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">预测性返回、16KB 页、隐私进一步收紧</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 16-17 (API 36-37)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2025-2026</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">更快的小版本节奏、AI 能力整合（如 Gemini 扩展）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
安卓版本简史（截至 2026 年 8 月，开发重点关注项）

#### 二、用什么语言写：Java 还是 Kotlin？

安卓开发历史上出现过两种主流语言。Java 是"开国元老"——安卓诞生之初就用它；<strong>Kotlin 是 2017 年谷歌钦点的"一等公民"</strong>，2019 年起官方明确"Kotlin 优先"（Kotlin-first），到 2026 年，新项目几乎全部用 Kotlin，旧项目也大多在陆续迁移。

说句实在话：如果你是完全零基础，<strong>直接学 Kotlin，别回头碰 Java</strong>。原因有三：一是 Kotlin 代码量比 Java 少 30%-40%（同样的功能，Kotlin 更短更清晰）；二是它天生防"空指针"这种新手噩梦；三是所有现代教程、官方文档、AI 编程工具（还记得咱们的 AI 编程书吗？）都在以 Kotlin 为准。Java 只在维护老项目、读老代码时会遇到。

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
<i class="fas fa-times-circle mr-1"></i> Java 风格（啰嗦版）

{class="font-mono text-xs leading-relaxed"}
public class MainActivity extends Activity {<br>&nbsp;&nbsp;@Override<br>&nbsp;&nbsp;protected void onCreate(Bundle b) {<br>&nbsp;&nbsp;&nbsp;&nbsp;super.onCreate(b);<br>&nbsp;&nbsp;&nbsp;&nbsp;setContentView(R.layout.activity);<br>&nbsp;&nbsp;}<br>}
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
<i class="fas fa-check-circle mr-1"></i> Kotlin 风格（清爽版）

{class="font-mono text-xs leading-relaxed"}
class MainActivity : ComponentActivity() {<br>&nbsp;&nbsp;override fun onCreate(b: Bundle?) {<br>&nbsp;&nbsp;&nbsp;&nbsp;super.onCreate(b)<br>&nbsp;&nbsp;&nbsp;&nbsp;setContent { App() }<br>&nbsp;&nbsp;}<br>}
:::
:::

同样一件事，Kotlin 少了一堆花括号和样板。第 50 章咱们会正式学它，现在你只需要记住：<strong>安卓开发的"普通话"叫 Kotlin</strong>。

#### 三、一个 App 是怎么诞生的？

很多人以为"开发 App"就是打开电脑狂写代码。实际上，一个 App 从想法到用户手机上，大致要经过这样一条流水线：

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-lightbulb mr-1"></i> 想法</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center">📐 设计（界面+功能）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-keyboard mr-1"></i> 写代码</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hammer mr-1"></i> 编译打包（APK/AAB）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> 测试（模拟器+真机）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-rocket mr-1"></i> 发布（商店/安装包）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
图 1：一个安卓 App 从想法到上架的全流程
:::

流程里有两个概念你现在就要认识：

- <strong>APK</strong>：安卓应用的安装包格式（.apk），双击就能装到手机上，就像 Windows 的 .exe。平时自己测试、给朋友传着玩，用它。
- <strong>AAB</strong>：Android App Bundle（.aab），上架 Google Play 用的"高级打包格式"。商店会根据用户的手机型号动态裁剪，让每个人下载的包更小。自己装不了，只能交给商店。

另外你还会不断听到一个词：<strong>SDK</strong>（Software Development Kit，软件开发工具包）。它就是安卓官方提供的一整套"开发装备"——包括各版本的 API 库、调试工具、模拟器镜像等。你写代码时调用的 <code class="inline">Activity</code>、<code class="inline">Button</code> 这些类，都来自 SDK。

#### 四、安卓技术栈全景：你的"武器清单"

正式学习前，先认识一下 2026 年主流安卓项目的标准配置——这张清单你现在看不懂没关系，全书学完回来看，会豁然开朗：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">层次</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">主流选择（2026）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">干什么用的</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">语言</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin 2.x</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">写逻辑的语言</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">界面</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jetpack Compose + Material 3</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用代码画界面（本书主线）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">架构</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MVVM + ViewModel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把界面和逻辑分开，代码不乱</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数据存储</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room（数据库）+ DataStore（配置）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把数据存进手机</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">网络</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit + OkHttp + Kotlin 协程</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">和服务器对话</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">构建工具</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle + Kotlin DSL</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把代码变成安装包</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">开发环境</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">谷歌官方的"全家桶"IDE</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
2026 年安卓主流技术栈速览

别被这一串英文吓到。<strong>它们就像厨房里的锅碗瓢盆</strong>——你现在只需要知道"做饭要进厨房"，具体每样工具怎么用，后面章节逐个拆给你看。而且好消息是：Android Studio 创建新项目时会自动帮你把这一整套配置好，你只管炒菜。

#### 五、安卓 vs iOS：开发者的第一堂"选边课"

你手里可能正同时有安卓和苹果设备。作为开发者，两边的体验差异值得提前了解——不是"哪个更好"的站队，而是"哪边更适合你起步"的现实账：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">维度</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">安卓开发</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">iOS 开发</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">开发电脑</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Windows / Mac / Linux 都行</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><strong>必须 Mac</strong>（Xcode 独占）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">开发工具</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio（免费）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode（免费）+ 上架年费 99 美元</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">上架审核</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">宽松，几小时~几天</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">严格，1-7 天是常态</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">装机试玩</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">APK 随便发、随便装</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分发受限，测试需签名/TestFlight</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">收入环境</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">广告/国内渠道为主</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">App Store 内购付费习惯更好</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">学习成本</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">概念较多（四大组件等）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">生态封闭但体系统一、文档精良</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
安卓与 iOS 开发路径对比（2026 年 8 月）

说句实在话：<strong>如果你的电脑不是 Mac，那这道题根本不用选——安卓是唯一选项</strong>。如果你有 Mac，本书第八、九两篇可以对照着读，编程思路是相通的，学完一边再学另一边会快很多。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：看看你手机里的"安卓"

{class="mt-1"}
打开手机的 [设置] → [关于手机]（或"关于本机"），找到"安卓版本"或"Android 版本"那一栏——连续点它几下，还能触发系统的彩蛋小游戏。记下你的版本号，对照上面的版本表看看它属于哪一代。你的手机，就是你的第一个"开发测试机"。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 安卓 2008 年诞生，2026 年是全球市场份额最大的移动系统，活跃设备数十亿
- 最新正式版 Android 17；主流 App 最低支持 Android 8-10，用户盘子才够大
- 新项目一律用 Kotlin：代码少 30%+、防空指针、官方钦定
- APK 自己装，AAB 上商店；SDK 是官方开发装备包
- 2026 标准技术栈：Kotlin + Compose + MVVM + Room + Retrofit + Gradle + Android Studio
:::
