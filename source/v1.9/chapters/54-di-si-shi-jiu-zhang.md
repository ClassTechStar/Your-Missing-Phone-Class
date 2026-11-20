---
id: di-si-shi-jiu-zhang
num: 49
part: an-zhuo-kai-fa-pian
nav: 第四十九章：搭建开发环境——Android Studio与第一个项目
toc: default
kind: chapter
---

### 第四十九章：搭建开发环境——Android Studio 与第一个项目

{class="chapter-intro mb-4"}
工欲善其事，必先利其器。这一章咱们把「厨房」搭好：装好 Android Studio、跑通模拟器、创建人生第一个安卓项目，再把工程结构拆开看个明白。装好环境之后，你会第一次看到自己写的代码变成一个能点的按钮，这个瞬间，很多人会记一辈子。

::: div .quick-read
##### 本章速读（5 分钟版）
工欲善其事，必先利其器。这一章咱们把「厨房」搭好：装好 Android Studio、跑通模拟器或真机、创建人生第一个安卓项目，再把工程结构拆开看个明白。先把丑话说在前面：装开发环境是整条入门路上「翻车率」最高的一站——第一次装花一整晚、报三次错都正常，不是你笨，是这东西天生组件多（IDE、SDK、模拟器、构建工具，每环都可能出幺蛾子）。把它当入门仪式，心态就顺了。
最关键的有三件事，第一，动手前先过一遍<strong>电脑检查清单</strong>：内存 16GB 起步最舒服（8GB 不是不能跑，是 IDE、模拟器、浏览器三者一开风扇先崩溃），磁盘给工具链预留 20GB 以上，模拟器要跑在 CPU 虚拟化（VT-x/AMD-V）之上。老电脑可能要进 BIOS 手动开。电脑实在老旧也有退路：跳过模拟器，用真机调试，一台 8GB 笔记本加一根数据线加一台旧安卓手机，照样把第一个 App 跑起来，还比卡顿的模拟器流畅。第二，安装走四步。到官网下载最新<strong>稳定版</strong>（认准 Stable 标签，别从旧教程里抄下载链接）、运行安装包一路下一步（自定义路径别带中文和空格，不然后面构建表演玄学）、首次启动下载 SDK 组件（默认勾选，几个 GB，喝杯水的工夫）、看到欢迎页就算完工。第三，创建第一个项目模板选 Empty Activity，跑起来优先真机；然后花点时间认识工程结构，res/ 目录归置「字和图」、AndroidManifest.xml 是项目的户口本、Gradle 是总管家。这三样看得懂，以后改哪儿都不慌。
今天就能做的最小动作：照检查清单过一遍自己的电脑，然后把示例里的「Hello」换成你自己的名字跑一次。看到自己写的字出现在手机屏幕上的那个瞬间，很多人会记一辈子：这是你从「用户」变「开发者」的第一步。
最大的坑集中在安装和构建环节：安装路径带中文或空格；构建一失败就重装，先翻本章的「报错急救」十个病例，最高频的三样是依赖下载失败（Could not resolve）、SDK 路径不对、AGP 与 Gradle 版本互相看不上；版本对齐比记住动物代号重要得多。还有「改完没生效」先做三个排查动作，别急着怀疑人生；备份、导出、把 APK 发给朋友装这几手也顺手学了，第一个作品值得分享出去。
##### 速查表
- 电脑门槛：内存 16GB 起步、磁盘留 20GB+、模拟器要开 CPU 虚拟化（VT-x/AMD-V）
- 装不动的退路：跳过模拟器，旧手机真机调试更流畅
- 安装四步：官网下稳定版→一路下一步→下载 SDK 组件→见到欢迎页
- 安装避坑：路径别带中文和空格，认准 Stable 标签别抄旧教程链接
- 跑通优先：模板选 Empty Activity，能用真机就别死磕模拟器
- 工程三样：res/ 归置字和图、AndroidManifest.xml 是户口本、Gradle 是总管家
- 第一次改造：把「Hello」换成你的名字，改完没生效先做三个排查动作
- 报错急救：十病例里最高频的是依赖下载失败、SDK 路径、AGP 与 Gradle 版本不对齐
:::

<div class="version-anchor">本章界面路径按 iOS 18.x / HarmonyOS 5.x / Android 15 核对（2026 年 11 月）。你的机型或系统版本不同，菜单名字和位置可能对不上——以你手机上显示的为准。</div>


#### 开始之前：检查电脑，也检查预期

先把丑话说在前面：装开发环境这件事，是整个安卓入门路上「翻车率」最高的一站。有人在周五晚上开始装，凌晨两点还在对着一个红色报错发呆，第二天中午才发现是内存不够。所以动手之前，花五分钟做两件事：检查电脑，也检查预期。

电脑这边，逐项过一遍：

- <strong>内存</strong>：16GB 起步最舒服。8GB 不是不能跑，但 IDE、模拟器、浏览器教程页三者一开，风扇会先崩溃。
- <strong>磁盘</strong>：给开发工具链预留 20GB 以上。IDE 本体、SDK、模拟器镜像、Gradle 缓存，四样加起来比你想的大得多。
- <strong>CPU 虚拟化</strong>：模拟器要在 CPU 虚拟化（VT-x/AMD-V）之上跑，大多数新电脑默认开着，老电脑可能要进 BIOS 手动开。
- <strong>操作系统</strong>：Windows、macOS、Linux 都行。新书读者大多用 Windows，本章描述以 Windows 为准，Mac 差异会顺带标注。

预期这边就一句话：<strong>第一次装环境，花一整晚是正常的，报三次错也是正常的。</strong>这不是你笨，而是环境这东西天生组件多，IDE、SDK、模拟器、构建工具，每一环都可能因为网络、磁盘、系统设置出幺蛾子。每个你现在叫得上名字的程序员，都经历过这个阶段。把它当成入门仪式，心态就顺了。

电脑实在老旧怎么办？也有一条路：跳过模拟器，用真机调试（本章第三节讲）。一台内存 8GB 的笔记本 + 一根数据线 + 一台旧安卓手机，照样能把第一个 App 跑起来，而且体验比卡顿的模拟器流畅得多。

#### 一、安装 Android Studio

Android Studio 是谷歌官方的集成开发环境（IDE），免费，功能全家桶：写代码、看界面预览、调试、打包全在里面。安装四步：

1. 打开官网 developer.android.com/studio，下载最新稳定版（IDE 代号按动物名字母序轮换，别照着旧教程里的代号找安装包，以官网当前稳定版为准；Windows/Mac/Linux 都有）。
2. 运行安装包，一路「下一步」——安装向导会自动带上 <strong>Android SDK</strong> 和模拟器组件。
3. 首次启动时按提示下载 SDK 组件（默认勾选就好，可能需要几分钟和几个 GB 的空间）。
4. 完成后你会看到欢迎页，恭喜，「厨房」搭好了。

这四步看着简单，每一步背后都有几个值得说透的细节。咱们一步步来。

##### 下载页怎么认

官网下载页最显眼的大按钮会直接给你当前平台的稳定版。往下滚一点，能看到其他平台的安装包。Windows 用户通常选 <kbd>.exe</kbd> 安装向导（双击就能装）；Mac 用户注意选对芯片版本：Apple Silicon 和 Intel 的包不一样，选错了装完打不开。版本页面上写的版本号、代号年年变，<strong>认准「稳定版/Stable」标签就行，别从旧教程里抄下载链接</strong>。旧链接有时候还能用，但装出来的老版本会和网上的新教程对不上，徒增困惑。

顺带说一句代号的事。Android Studio 的版本代号按动物名字母序轮换，写这本书的时候，稳定版停在 Rabbit 这个动物系（2026.2.x 系）。你看到这本书的时候大概率已经换了好几任动物，没关系，这不影响任何操作，界面和流程是稳定的。动物代号唯一有用的地方，是你在网上搜报错时，有些老帖子会带代号，看一眼就知道那篇教程大概多老。

##### Windows 安装向导逐屏走

1. 双击安装包，欢迎屏点 Next。
2. 组件勾选屏：默认全勾（Android Virtual Device 必须勾上，这就是模拟器）。
3. 安装路径屏：默认路径没问题；想改自定义路径的，注意别带中文和空格，不然后面构建会给你表演玄学。
4. 开始菜单屏和安装屏：Next → Install，等进度条。
5. 完成屏勾选「Start Android Studio」，点 Finish。

首次启动会弹一个设置向导：问你是导入旧配置还是全新开始（新机器选全新开始）、类型选 <strong>Standard</strong>（标准，默认）、然后向导开始下载 SDK 组件。这个环节要联网，而且要下载好几个 GB，喝杯水的工夫正好。协议列表里要挨个 Accept 才能继续，别嫌弃，这些协议就是「你要用谷歌的东西」这句话的法律版。

Mac 用户流程更短：把下载的 <kbd>.dmg</kbd> 里的图标拖进 Applications 文件夹就算装完。第一次打开如果弹「无法验证开发者」之类的系统提示，在 Finder 里对图标右键选「打开」即可放行（macOS 对新下载的 App 都有这道门禁，不是 Studio 被黑了）。

下载这步最容易失败，原因几乎都是网络问题，稍后「安装三连坑」一节专门拆。现在先假定你顺利走到了欢迎页：一个深灰色的窗口，左边列出你的项目（此刻是空的），右上角有 New Project、Open、Get from VCS 几个按钮。记住这个画面，以后每天你都会从这里出发。

给你一个真实的时间线当参考。某位读者周五晚上九点开工：下载安装包十分钟，安装十来分钟，SDK 下载因为网络反复失败，折腾到夜里十一点半；换手机热点后一次成功；十二点创建项目，第一次 Gradle 构建又等了六七分钟；凌晨快一点，模拟器开机，「Hello Android!」出现在屏幕上。前后三个多小时，其中两个小时花在网络上。第二天他给朋友复现整个流程，四十分钟跑完。这就是常态：<strong>第一晚像打仗，第二遍像散步。</strong>如果你的时间线更长，也完全正常，重点不是快，是走完。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：硬件要求心里有数

{class="mt-1"}
Android Studio 是个「吃内存」的家伙：建议 <strong>16GB 内存</strong>起步（8GB 也能跑，但模拟器一开会比较卡）、磁盘预留 <strong>20GB 以上</strong>、CPU 支持虚拟化（BIOS 里开启 VT-x/AMD-V）。如果电脑确实老旧，可以用「真机调试」代替模拟器（本章第四节会讲），体验反而更流畅。
:::

#### SDK 组件详解：装的那几个 GB 都是什么

安装向导替你下载的那一堆东西，新手阶段只需要知道名字和用途，不需要知道实现原理。打开 <kbd>Tools</kbd> → <kbd>SDK Manager</kbd>（欢迎页也能进：右下角齿轮里找 SDK Manager），你会看到 SDK 组件的完整清单。按用途分，主要是这么几样：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">组件</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">是干嘛的</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要不要动</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SDK Platform</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">某个安卓版本的"开发包"：编译目标 API 对应的那套系统库和框架接口</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">装 compileSdk 对应的那个就行，别贪多</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SDK Platform-Tools</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">adb、fastboot 等命令行工具——电脑和手机"说话"的翻译官</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">默认装好，跟随 IDE 更新</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SDK Build-Tools</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">打包资源、签名、生成 APK 用的工具集</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">默认装好，一般不用管</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Emulator</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">模拟器本体程序</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用模拟器就必须有</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Command-line Tools</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不带界面的 SDK 管理命令</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可选；偶尔某些工具链需要它</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">NDK</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用 C/C++ 写底层代码的套件</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新手阶段完全不用装，装了白占几个 GB</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
SDK 组件速览（以 SDK Manager 里实际列出的为准）

这些文件默认装在哪？Windows 是 <code class="inline">C:\Users\你的用户名\AppData\Local\Android\Sdk</code>，Mac 是 <code class="inline">~/Library/Android/sdk</code>。知道这个路径有两个用处：一是磁盘紧张时知道该清哪里；二是某些教程让你配置 <code class="inline">ANDROID_HOME</code> 环境变量时，知道该填什么。

SDK Manager 里你以后最常用的操作是<strong>补装平台</strong>。项目构建时会告诉你「缺哪个 API 的平台」，回来这里勾上、点 Apply、等下载，完事。每个平台通常要占一两 GB 甚至更多（视版本而定），所以不建议把列表里的安卓版本全勾上，那是老视频里「秀肌肉」的操作，对你没有任何好处。新手阶段保持「一两个平台 + 默认工具」就是最健康的配置。

SDK Manager 有两个标签页：<strong>SDK Platforms</strong> 管系统平台，<strong>SDK Tools</strong> 管工具集（模拟器、Platform-Tools 这些）。右下角有个 「Show Package Details」 勾选项，勾上后能看到每个平台的细分条目——初学阶段用不上，知道它存在就行。界面上偶发的灰色条目表示「该版本与当前 IDE 不兼容」，不用纠结，挑亮着的来。

还有个容易混淆的点顺带讲清：<strong>你电脑上不需要装「每个安卓版本」。</strong>SDK Platform 是「编译目标」用的，模拟器跑的安卓版本由单独下载的「系统镜像」提供（本章后面讲 AVD 时细说）。两套东西名字里都带安卓版本号，但用途完全不同，一个是编译时用，一个是运行时用。

给你一个磁盘心智账本，心里有数就不会中途恐慌：IDE 本体几个 GB；一个 SDK 平台一两 GB；一套默认工具几个 GB；一个系统镜像一两 GB；一台装好的 AVD 再吃几 GB；Gradle 的全局缓存会随项目数慢慢长到十 GB 上下。全部加起来，20GB 起步的预留只是「及格线」，硬盘宽裕的话按 40GB 规划更从容。这个数字会随版本变化，具体占用以你机器上的实际情况为准。

#### 安装三连坑：下载失败、磁盘告急、装完打不开

安装阶段的三种典型翻车，提前打疫苗：

- <strong>坑一：SDK 下载到一半失败。</strong>错误信息通常是 「Download interrupted」 或者进度条卡死。这不是你操作错了，是网络访问国外服务器不稳定，解法按顺序试：换个时间段重试（深夜或清早成功率高得多）；用手机热点试一次（有时候运营商线路反而通）；都不行就搜「Android Studio SDK 国内镜像」，给 SDK Manager 配上国内镜像源再下。镜像这个话题在后面报错门诊里还会出现，记住它，它会陪你整个开发生涯。
- <strong>坑二：C 盘飘红。</strong>SDK、模拟器镜像、Gradle 缓存三样东西都会往系统盘里塞。解法是在 SDK Manager 里改 <code class="inline">Android SDK Location</code> 到大盘路径（改完之前已下载的组件会重新下载，所以最好在装的时候就决定好）；Gradle 缓存的搬家方法搜「gradle 用户目录 修改」，跟着改环境变量就行。装完 IDE 本身才几个 GB，真正的大头是这些配套组件，规划磁盘时按 20GB 起步算才稳。
- <strong>坑三：装完启动白屏、卡在启动画面。</strong>先杀掉进程重开一次，多数情况下就好了。还不好就试菜单栏 <kbd>File</kbd> → <kbd>Invalidate Caches</kbd>（清除缓存并重启），这是 Android Studio 时代的「重启大法」。再不行，把安装目录下残留的旧版本配置清掉重装，放心，你的项目文件都在项目目录里，重装 IDE 不会动它们。

还有一个不算坑但要提醒的事：装好后系统里会同时出现「Android Studio」和一个叫 <strong>Gradle</strong> 的东西（这是构建工具，下一节项目里天天见），别看到陌生名字就手痒去卸载，卸了它，你的项目一个都编不出来。

顺带把「虚拟化被占用」这个第四坑也放在这里：开了 VT-x/AMD-V，模拟器还是启动失败，错误信息里提到 HAXM 或 hypervisor。常见原因是电脑上装了依赖虚拟化的安全软件或沙箱类工具，把虚拟化层抢先占了。处理思路是到对应软件的设置里关闭它对虚拟化的占用，或者按报错信息里的指引操作：这类冲突的具体选项随软件不同而变，以你电脑上那款软件的官方说明为准。

#### 二、创建你的第一个项目

在欢迎页点 <kbd>New Project</kbd>，选 <strong>Empty Activity</strong> 模板（最干净的新手模板），然后填三样东西：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">配置项</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">填什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">说明</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">My First App</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">应用名字，显示在手机桌面上</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Package name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example.myfirstapp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全球唯一标识，习惯是"域名反写"，先按默认</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minimum SDK</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API 26（Android 8.0）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最低支持版本，覆盖 95%+ 设备</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
创建项目要填的三件事

这三样除了名字都可以先按默认走。Name 随便起，改起来零成本——它只是显示在桌面上的应用名，改应用名改一行资源文件就行。真正「定了就难改」的是包名，下面的小贴士专门说它。

Minimum SDK 这个下拉框值得多说两句。你选的数字越小，能装你 App 的设备越多，但你能用的系统新功能越少；选得越大则相反。向导会在选项旁边直接告诉你当前选择能覆盖多少比例的设备，跟着这个提示走就不会错大格。示例项目按 API 26（Android 8.0）起，这是兼顾覆盖面和新特性的一档，本书后面的项目也沿用这个基准。版本策略的完整逻辑，第 48 章讲安卓生态时已经铺垫过，这里不重复。

配置屏还有两项你可能好奇：Save location 是项目文件夹的位置，建议别放在带中文和空格的路径下，原因同安装路径；Build configuration language 保持默认的 Kotlin DSL 就好，现在的新项目都用 Kotlin 代码写构建脚本，这正好和你要学的 Kotlin 是同一门语言，一份工夫两处用。

点 Finish 后，Android Studio 会用 Gradle 自动下载依赖、构建项目（第一次要等几分钟，之后每次会快很多）。构建完成后，你就有了一个能跑的 App：虽然它还只会显示一行「Hello Android!」。

第一次构建时窗口底部会滚动大量输出，看不懂没关系，你只需要盯住两件事：进度条还在不在动、最后有没有红色报错。绿了就是成了。很多新手被刷屏的英文吓到，其实九成九的输出都是「正在下载某个库」的流水账，跟你的代码没关系。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小贴士：包名的门道

{class="mt-1"}
包名（package name）就像 App 的「身份证号」，全球不能重复，上架后就不能改了。个人练习用 <code class="inline">com.example.xxx</code> 就行；正式产品要换成你自己的域名反写（比如 <code class="inline">com.你的名字.应用名</code>）。别用 <code class="inline">com.example</code> 上架：商店会拒收。
:::

#### 模板怎么选：Empty Activity 和它的邻居们

New Project 的第一屏是一堆模板缩略图，新手容易在这里犯选择困难。拆开讲：

- <strong>Empty Activity</strong>：最干净的一张白纸，用的是 Jetpack Compose 界面体系（第 51 章的主角）。本书所有项目都从它出发。
- <strong>Empty Views Activity</strong>：注意多了「Views」两个字：它是旧界面体系的模板，页面用 XML 文件描述。网上大量老教程的代码都基于它，看懂老代码时你才会需要它。
- <strong>Basic Views Activity</strong>：自带一个页面跳转示例的 Views 模板，适合研究「两个页面怎么连」这种老写法。
- <strong>Bottom Navigation / Navigation Drawer 等</strong>：带现成导航框架的模板，结构复杂，新手阶段点进去只会更晕。

怎么选？答案是：<strong>跟着本书学，一律选 Empty Activity</strong>；哪天你需要在老项目里干活、或者看不懂某篇老教程了，再开一个 Views 项目当「对照标本」。两套体系并存是安卓社区的历史包袱，不是你理解力的问题，第 51 章开头会把这个包袱的来龙去脉讲清楚。

列表底部通常还有一个「Samples」之类的入口，能拉官方示例项目下来。好东西，但别现在进去：示例代码里全是本书后半程才学的概念，现在进去只会收获满屏问号。把它记在待办里，等你学完第五十五章再回来看，会像读了半年英语再去看原版电影一样顺畅。

还有个常见误解顺便拆掉：模板不是「户型」，只是「精装程度」。选 Empty Activity 不代表你做不出带导航的应用，只是导航要你自己加（第 52 章会教）。反过来，选了花哨模板也不会让应用自动变厉害，模板里的每一行代码你都还要自己看懂。

选错了模板怎么办？最省事的答案是：删掉重建。学习阶段的项目没有任何沉没成本：删项目文件夹、重开向导，两分钟的事。别在错误模板上「将就着改」，那比重建费劲十倍。真正的项目里文件夹名、包名都会被多处引用，重建永远是新手阶段的合法操作。

#### 错误示范：创建项目的三个典型翻车

这一节用「错误示范 → 会发生什么 → 正确姿势」的格式，提前拆掉三个高频翻车现场：

- <strong>翻车一：项目建在带中文或空格的路径下。</strong>比如放在桌面「我的 文档/新文件夹」里。会发生什么：多数情况能建起来，但构建时可能出现各种莫名其妙的路径解析错误，且错误信息不直接指向真实原因。正确姿势：项目放在类似 <code class="inline">D:\AndroidProjects\MyFirstApp</code> 这种全英文、无空格的路径里。这个习惯从第一个项目养起，以后所有项目照办。
- <strong>翻车二：Minimum SDK 挑了最高的「显新」。</strong>有新手觉得「学最新的嘛」，把最低支持拉到最高的稳定版本。会发生什么：你的 App 只能装在极少数旗舰机和你自己的模拟器上，而且很多教程代码用了兼容写法你会看不懂。正确姿势：跟着向导默认或 API 26 一档走，理解了「覆盖面 vs 新特性」的权衡（第 48 章讲过）再自行调整。
- <strong>翻车三：包名随手起了个大写或特殊字符。</strong>比如手动改成 「MyApp」 或带下划线大写字母。会发生什么：向导会当场用红字拦你，这是好事：总比构建到一半报错强。正确姿势：包名全小写、字母数字加下划线、至少两段（反写域名习惯），拿不准就用默认。

三个翻车一个共同点：出问题时报错都不「诚实」——它抱怨的文件和真正的原因隔了好几层。环境类问题的基本素养就是：把规则前置，让问题根本没有发生的机会。

#### 第一次构建时，电脑在忙什么

点完 Finish 到你能开始写代码，中间有一段看似发呆的等待。把它拆开看，你就不焦虑了，还能提前认识几个以后天天打交道的名字。

- <strong>下载 Gradle 本身</strong>：Gradle 是构建工具，项目里带了它的「版本说明书」（wrapper 配置），IDE 照着说明去下载对应版本的 Gradle。这是第一次构建慢的大头之一，之后再快。
- <strong>下载依赖库</strong>：模板声明了要用哪些库（Compose、安卓核心库等），Gradle 把它们从仓库拉到你本地缓存。第一次要下几十上百个包，之后的构建直接用缓存。
- <strong>执行构建任务</strong>：编译代码、合并资源、生成调试签名，最后产出一个能装的包。这一步的输出在底部 Build 标签里滚动。

顺带认识两个目录：项目文件夹里会出现 <code class="inline">.gradle</code> 和 <code class="inline">build</code> 两个自动生成的文件夹，前者是 Gradle 的项目级缓存，后者是构建产物。它们都属于「能删能重建」的东西，哪天项目状态诡异，把这两个文件夹删掉重新 sync，往往就解决了。另外，全局缓存在你的用户目录下的 <code class="inline">.gradle</code> 文件夹里。它会随着项目越做越多而悄悄长大，磁盘紧张时记得来看它一眼。

第二次构建为什么快？因为上面三样，Gradle 本体、依赖缓存、构建守护进程（一个在后台待命的构建服务），都已经就位。所以「第一次特别慢」不是你电脑不行，是它真的在下载半个互联网的工具链。等待的这几分钟不用干瞪眼。正好把下一个要学的概念（工程结构）在脑子里过一遍。

#### 认识主窗口：五个区域记牢

项目打开后，满屏的按钮和面板可能让你有点眩晕。别急着研究每个按钮，先把五个区域认出来，日常 95% 的操作都发生在它们身上：

- <strong>工具栏（顶部）</strong>：绿色三角 <kbd>Run</kbd>、设备下拉框、项目名，你每天点得最多的三个东西都在这一条上。
- <strong>项目面板（左侧）</strong>：文件树。点左上角的下拉箭头可以在「Android 视图」和「Project 视图」之间切换，前者把结构整理得清爽（只显示你关心的部分），后者显示真实的磁盘目录。新手默认用 Android 视图，等读了第四节再切 Project 视图对照。
- <strong>编辑器（中央）</strong>：写代码的地方，带行号、代码补全和语法高亮。右边可能出现一条彩色竖条，提示这一行有警告或建议，先不理会。
- <strong>底部窗口条</strong>：Build、Logcat、Gradle 几个标签页。构建的进度和报错都在 Build 里滚动；Logcat 是看运行日志的地方，第 56 章调试时会把它当主角细讲。
- <strong>状态栏（最底部一行）</strong>：同步进度、任务状态。Gradle 转圈时看一眼状态栏，就知道它是在下载还是在编译。

有两个新手误区提前拆掉。其一，界面上大量按钮这辈子都用不到，它们是给各类复杂场景准备的，忽略它们不丢人。其二，窗口布局被你拖乱了不要慌，菜单 <kbd>Window</kbd> 里有恢复默认布局的选项，一键还原。

#### 三、跑起来：模拟器与真机

代码写好了，得找个「手机」来跑。你有两个选择：

##### 1. 模拟器（Emulator）

模拟器是在电脑里虚拟出一台安卓手机。在 Android Studio 里打开 <kbd>Device Manager</kbd> → <kbd>Create Device</kbd>，挑一台设备（推荐 Pixel 系列）→ 选一个系统镜像（带 Google APIs 的）→ 下载 → 启动。镜像列表里你会看到「Canary」字样，谷歌已经用这个持续更新的通道取代了以往的开发者预览版，那是给尝鲜玩家准备的；新手认准稳定版（Stable）就好。然后点工具栏的绿色三角 <kbd>Run</kbd>，几秒钟后，「手机」屏幕上就会出现你的 App。

模拟器的好处在后面「AVD 逐步指南」里展开，这里先说它最实用的三个场景：想看 App 在不同尺寸屏幕上的样子、想快速切换深色模式验证配色、想模拟横竖屏旋转——这三件事模拟器点两下就完成，换真机折腾半天。学习阶段你大概率会「模拟器为主」，没问题，这就是它的主场。

##### 2. 真机调试（更推荐）

真机永远是最真实的测试环境，滑动手感、真网络、真传感器，模拟器都比不了。安卓真机调试很简单：

1. 手机上打开 [设置] → [关于手机]，连点「版本号」 7 次，开启「开发者选项」。
2. 在 [开发者选项] 里打开 <strong>USB 调试</strong>。
3. 用数据线连电脑，手机弹窗选「允许 USB 调试」。
4. 回到 Android Studio，工具栏的设备下拉列表里就会出现你的手机，点 Run。

四个步骤里有几个容易绊脚的小地方。「连点版本号 7 次」这步，有些厂商的入口藏在 [设置] → [我的设备] → [全部参数] 之类的页面下，找不到就在设置里搜「版本号」。数据线必须是能传数据的线，很多随手抓来的线只能充电，插上电脑毫无反应时，第一反应就换线。国产厂商多数还有第二道开关，名字带「USB 安装」或「USB 调试（安全设置）」，普通调试用不到它，但哪天「手机连上了却装不上 App」，回来把这道开关也打开。开启开发者选项后，手机顶栏会常驻一条「开发者选项已开启」的提示，不用管它，这是正常现象，不是手机坏了。

补充一个很多人不知道的点：<strong>模拟器和真机可以同时在线。</strong>工具栏的设备下拉框里会同时列出模拟器和连着的真机，点谁就部署到谁。想对比「同一份代码在两边跑起来有什么差别」，这个下拉框来回切就行，不用拔来插去。

弹窗「允许 USB 调试」里的复选框写着「一律允许使用这台计算机进行调试」，家用电脑就勾上，以后不再重复弹窗；公司的公共电脑别勾，原因看下面的避坑提醒。

开发者选项里还有个对开发者格外友好的开关叫<strong>「充电时不锁定屏幕」（Stay awake）</strong>：打开后只要插着 USB 线，屏幕就不休眠。调试时反复点亮屏幕很烦人，打开它一次解决。用完开发记得关，免得晚上充电时屏幕亮一宿，开关是双刃剑，位置就在 USB 调试附近，顺手的事。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
避坑提醒：USB 调试别常开

{class="mt-1"}
USB 调试相当于给电脑开了「后门」。在公共场合充电、连接不信任的电脑时，务必关闭 USB 调试，防止别人通过它读取你的数据。平时开发用完就关，养成习惯。
:::

#### 创建第一台模拟器：AVD 逐步指南

AVD（Android Virtual Device）就是模拟器那台「虚拟手机」的正式名字，一台 AVD = 一份硬件配置 + 一个系统镜像。你在 Device Manager 里创建它的完整流程，一步一步是：

1. 点右侧边栏的手机形图标（或者菜单 <kbd>Tools</kbd> → <kbd>Device Manager</kbd>），打开设备管理面板。
2. 点 <kbd>Create Device</kbd>（加号），弹出硬件选择窗口。
3. 在 Phone 分类里挑一台设备。推荐 Pixel 系列：尺寸标准、资料多。新手选新一点的机型。
4. 点 Next，进入系统镜像选择页。列表里每行是一个安卓版本，带「下载」箭头的表示这个镜像还没下载到本地。
5. 点一个合适版本旁边的下载箭头，弹出协议，Accept，开始下载（又是网络环节，失败就重试或换时段）。
6. 下载完点 Finish，回到镜像列表，选中刚下载的那个，Next。
7. 最后一屏显示 AVD 配置摘要，直接 Finish。
8. 设备列表里出现你的新 AVD，点右侧的启动三角，窗口里「开机」——第一次开机要一两分钟，属正常。
9. 以后再启动就快了：模拟器默认保存快照（Quick Boot），关窗再开像手机息屏亮屏一样秒回。
10. 想验证它真的能当手机用，点开模拟器里的浏览器随便开个网页试试。

模拟器窗口侧边有一排工具按钮：旋转、音量、截屏、缩放，都在那儿。最常用的是旋转（验证横屏布局）和深色模式切换：这两个动作在真机上要进系统设置，在模拟器上是一秒的事。

Device Manager 里每台 AVD 的条目右边还有个下拉菜单，藏着几个有用的动作：<strong>Duplicate</strong>（复制一台，改个镜像测对比）、<strong>Wipe Data</strong>（抹掉 AVD 里的所有数据恢复出厂：App 状态诡异时的「重置大法」）、<strong>Stop</strong>（关机）。其中 Wipe Data 值得单独记住：哪天你的 App 在模拟器上行为不对劲，先怀疑模拟器自己的状态，Wipe 一下再跑，能省掉不少冤枉路的排查。

几个提前打的预防针：<strong>开机黑屏</strong>，九成是 CPU 虚拟化没开或镜像下坏了，回 BIOS 开虚拟化或删掉 AVD 重建；<strong>卡得像 PPT</strong>，先冷启动一次（Device Manager 里下拉菜单选 Cold Boot），还不行就换低分辨率机型；<strong>磁盘又红了</strong>，一个 AVD 加镜像通常占好几 GB，测试完的旧 AVD 从列表里删除即可，删了随时能重建，不心疼。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小贴士：一台就够，别囤 AVD

{class="mt-1"}
新手常犯的错误是照着教程囤五六台 AVD：「万一要测别的版本呢？」实际上学习阶段一台主力 + 换镜像测试就够了。每个 AVD 都吃磁盘、吃内存，囤多了 IDE 反而变卡。真要跨版本测试，建一个、测完、删掉，几分钟的事。
:::

#### 看懂系统镜像那一长串名字

选镜像那一步，列表里的名字长得像一串暗号：API 等级、系统版本名、ABI、目标系统混在一起。拆开看就三段：

- <strong>API 等级 + 版本名</strong>：比如 「API 26 / Android 8.0」。数字越大系统越新。学习阶段选一个和你项目 compileSdk 接近的稳定版本即可；想看老设备什么样，就补个老镜像。
- <strong>ABI</strong>：处理器架构。Intel 和 AMD 的电脑选 x86_64；Apple Silicon 的 Mac 和 ARM 架构的 Windows 电脑选 arm64-v8a。选错架构的镜像轻则慢、重则根本跑不起来，这也是「模拟器莫名卡顿」的常见病因之一。
- <strong>目标系统</strong>：带 <strong>Google Play</strong> 标的镜像里内置了应用商店，能登录谷歌账号、能装 App，最像真机；带 <strong>Google APIs</strong> 的有谷歌服务框架但没有商店，日常开发它最省心；还有不带谷歌服务的 AOSP 裸镜像，给特殊测试用，新手绕开。

新手建议的组合：新一点的稳定版 API + 对的 ABI + Google APIs 镜像。这一套跑起来快、坑少，跟本书后面的章节完全兼容。镜像列表里那些标着 Canary 的条目，是谷歌滚动发布的预览通道，尝鲜玩家玩的东西，看到它们绕开就行，等它们毕业成稳定版你再碰，一句话总结：<strong>你的第一个目标是「让 App 跑起来」，不是「追新」。</strong>

镜像和 AVD 的关系再澄清一次，这是新手最容易搞混的地方：镜像相当于「系统安装盘」，AVD 相当于「装了系统的那台手机」。一个镜像可以装进多台不同配置的 AVD；删掉某台 AVD，镜像还在，下次建新 AVD 直接复用，不用重新下载。

#### 模拟器 vs 真机：到底听谁的

前面两套流程你都跑通了，接下来每天写代码用哪个？给你一张对照表，按需选：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">维度</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">模拟器</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">真机</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">上手成本</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">下个镜像就能用，可随时换机型</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">开开发者选项、找数据线，一次性配置</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">流畅度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">吃电脑性能，低配机明显卡</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真机自己的性能，通常很流畅</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">传感器</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">加速度计、GPS 等靠虚拟注入，够用但假</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全是真的，涉及传感器功能必用</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">摄像头/通话/短信</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">虚拟摄像头、虚拟通话，只能走个过场</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真实可用，涉及这些功能必须真机</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">网络环境</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">借电脑的网络，断网/弱网要手动模拟</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真实 Wi-Fi、真实蜂窝网络</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多机型测试</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">建多台 AVD 即可覆盖，便宜</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每台都是真金白银，或用云真机服务</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系统定制</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">原生安卓系统，干净</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">各家定制系统，能暴露兼容性问题</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
模拟器与真机对照：不是二选一，是分工

表看完，结论其实一句话：<strong>学习阶段两个都要有，日常以你顺手的那个为主。</strong>写界面、练语法、看布局，模拟器舒服；调手势、测定位、验证推送和真实网络，必须真机。到了上架前的验收阶段（第 56 章），拿真机过一遍更是不可省略的动作。

拿一个真实场景练练手。假设周六下午你在做一个记账 App（第 54 章的项目），今天的安排是验证「旋转屏幕后数据还在不在」。模拟器五分钟搞完：建好项目跑起来、加一笔账、点旋转按钮、看数据。下周的任务是「真实的月份切换提醒」，要靠系统日历触发：这就得真机了，插上线跑一整天。两个环境各司其职，谁也不淘汰谁。

手头没有安卓真机、又想认真学的读者也别慌：学习阶段的前几章（学语言、学 Compose）用模拟器完全够用，等真需要真机验证了再捡起来也不迟——开发者选项那套流程十分钟就能配好。另外，谷歌官方也提供云真机类的测试服务，把 App 扔到远处的真机上跑，细节以官方文档为准，这里先记个名字。

反过来也给你一个错误示范：有人学习期间<strong>全押模拟器</strong>，三个月后第一个项目想给同学装，结果在对方的国产定制系统上字号错乱、返回键行为诡异、应用图标显示模糊，所有问题在模拟器上从未出现过。模拟器跑的是「原生安卓的某种理想状态」，而真实世界是各厂商深度定制的。所以从第一天起就保持「每周至少一次真机运行」的习惯，让两个世界的差异尽早暴露，别攒到最后。

#### 真机调试疑难杂症：连不上的五种情况

真机流程只有四步，但每个环节都可能出岔子。按「插上电脑之后」的时间顺序，五种最常见的情况和解法：

- <strong>情况一：插上毫无反应，设备列表是空的。</strong>先换一根确定能传数据的线（电脑认 U 盘的那种线），再检查手机上 USB 连接模式是否选成了「仅充电」，改成「传输文件」往往就通了。这种情况占了「连不上」的一半以上，而且每次都让人怀疑人生。
- <strong>情况二：设备名出现了，旁边标着 unauthorized（未授权）。</strong>手机屏幕上应该有个「允许 USB 调试」的弹窗等着你点允许。有时候弹窗被你按了「取消」，把数据线拔插一次，弹窗就回来了。
- <strong>情况三：设备显示 offline（离线）。</strong>ADB 的连接抽风了，手机和电脑都别动，在电脑终端执行 <code class="inline">adb kill-server</code> 再 <code class="inline">adb start-server</code>，然后重新插拔。这两条命令是安卓开发者的「重启路由器」，记住它们。
- <strong>情况四：连上了，Run 时提示安装失败。</strong>回到手机的开发者选项，把「USB 安装」「USB 调试（安全设置）」这类带安装字样的开关打开：国产定制系统尤其爱藏这道门。开了还不行，看第六节的报错门诊。
- <strong>情况五：想摆脱数据线。</strong>Android 11 起的开发者选项里有「无线调试」，手机和电脑连同一个 Wi-Fi，用配对码配对后就能无线部署，具体入口以你手机系统为准。散步式开发体验极佳，但首次配对要耐心。

排查的基本顺序永远是：<strong>线 → 授权弹窗 → 开发者选项开关 → adb 重启。</strong>从便宜到贵，从常见到罕见，按这个顺序走，大部分问题五分钟内解决。全都试过还不行。重启手机和电脑，别笑，这招的命中率比你想的高。

#### 模拟器窗口边的实用按钮

模拟器窗口的侧边有一列小图标，每个都值得认识一下，因为它们对应着真机上的各种「物理动作」：

- <strong>返回、Home、多任务</strong>：就是手机底部三键的模拟，调试页面跳转时天天用。
- <strong>旋转</strong>：一键横竖屏切换，验证布局响应，比真机进设置快十倍。
- <strong>电源键</strong>：锁屏、开机，测试 App 从后台恢复的表现时会用到。
- <strong>音量键</strong>：不解释了。
- <strong>截屏</strong>：把模拟器画面存成图片，写学习笔记、发朋友圈展示成果都靠它。
- <strong>Extended Controls（三个点）</strong>：大宝藏。点开是个面板，能改模拟器的 GPS 位置、网络信号强弱、电池电量、指纹等等。测定位相关功能时，把「手机」挪到东京试试，就靠这里。

这些按钮背后的逻辑是：模拟器把真机的「物理世界」都虚拟化了，而你手里握着这个世界的参数面板。真机上你得真的走到另一个城市才能测定位，模拟器上点两下就行，这就是它不可替代的地方。

#### 安装阶段 FAQ：七个真问题

收集了新手在这一阶段问得最多的七个问题，答案都尽量短：

- <strong>问：C 盘只剩十几个 GB 了，还能装吗？</strong>答：能。IDE 安装时选个大盘路径；SDK 位置在 SDK Manager 里改到大盘；Gradle 缓存目录用环境变量搬家。三步做完，C 盘只承担少量配置文件。
- <strong>问：装在移动硬盘里，宿舍电脑和图书馆电脑共用一套行不行？</strong>答：不推荐。SDK 和缓存路径绑死在系统目录里，换机器路径全变，问题比你想象的多。真要两台电脑用，让两边各自装环境，项目文件用网盘或 Git 同步。
- <strong>问：要先学 Java 再学安卓吗？</strong>答：不需要。Kotlin 是官方钦定的第一语言（第 48 章说过原因），直接学它。Java 知识等看老代码时再按需补。
- <strong>问：不「科学上网」就装不了吗？</strong>答：不是。慢是真的，但镜像和重试能解决大部分问题。下载类报错翻回「安装三连坑」照方抓药。
- <strong>问：8GB 内存的笔记本能学吗？</strong>答：能，但把模拟器用量降到最低：主力真机调试，模拟器只在需要时开一台低分辨率 AVD。关掉用不到的插件和后台软件，体验还能再挤一挤。
- <strong>问：IDE 天天弹更新提示，要不要升？</strong>答：学习阶段的原则是「项目能跑就不急」。大版本更新常伴随构建工具链变动，升完第一次 sync 可能又是一轮折腾；想升级时先备份当前能跑的环境，挑时间从容来。
- <strong>问：视频里那些花花绿绿的代码主题怎么弄？</strong>答：<kbd>Settings</kbd> → <kbd>Editor</kbd> → <kbd>Color Scheme</kbd>，或直接装主题插件。这个不着急，等你写满两周代码再打扮也不迟，工具的颜值永远排在功能后面。
- <strong>问：装的时候要断网吗？家里网慢得离谱。</strong>答：不能断网，安装和首次启动都要下载。网慢就换时段、换热点、上镜像，三招总有灵的。
- <strong>问：装完杀毒软件报警了，是不是中了什么？</strong>答：开发工具被误报是常事（它要调试进程、读写系统目录），把安装目录加入白名单即可。当然，前提是你从官网下的安装包，第三方下载站的包才真的值得警惕。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
一句话记牢

{class="mt-1"}
环境搭建的成功标准只有一个：绿色三角点下去，你的 App 出现在某块屏幕上。其他一切：内存条、动物代号、报错黑话：都只是路上的风景。
:::

#### 给三类人的安装路线

同样的安装流程，不同处境的人有不同的省力走法。对号入座：

- <strong>学生（宿舍党）</strong>：校园网高峰期下载经常龟速，大文件下载改用深夜或手机热点；笔记本硬盘小的话，提前把 SDK 位置规划到大盘；项目每周压缩备份到网盘一次，图书馆电脑坏了也不怕。宿舍熄电前记得保存：IDE 会自动恢复未保存内容，但别赌它每次都灵。
- <strong>上班族（通勤学习党）</strong>：白天碎片时间啃不了安装报错，把「折腾环境」整块安排在周末上午；工作电脑没有管理员权限的话，便携版思路走不通，就在家里电脑装好、公司里用云真机或在线预览过渡；下班路上可以打开第 50 章提到的 Kotlin Playground，用浏览器先把语言学起来，回家再上真家伙。
- <strong>低配电脑党</strong>：路线就是「真机为主」。安装时可以只勾最小组件；模拟器镜像选尺寸小的机型；编译慢时趁等待时间读下一节内容，把等待变成学习时间。这套打法练出来，你对「构建」的理解往往比高配机用户还深。

装到这里，硬件、软件、模拟器、真机四样齐活。下一节开始，我们终于要碰到真正的东西了，项目的文件，以及藏在文件背后的构建逻辑。

#### 让 AI 当你的「陪装助手」

2026 年学开发的人有个前几代没有的福利：卡住的时候，AI 随叫随到。但「随叫随到」和「用得好」是两回事，给你一套在装环境这个场景里的正确用法。

第一步，喂对信息。报错时别只截图，把<strong>报错文字原样复制</strong>给 AI，再附上三样背景：你的操作系统、你正在做哪一步（装 SDK？建项目？开模拟器？）、报错前你点过什么。上下文越全，AI 的诊断越准——这正是本书第七篇讲过的需求工程，套在这里完全成立。

第二步，让它给「步骤清单」而不是「一键脚本」。AI 很爱给你贴一段大而全的命令让你整段粘贴，装环境这种事恰恰最忌讳黑箱，出问题你不知道是哪步坏的。你可以直接说：「一步一步来，每步告诉我点什么、会看到什么，我确认完再进行下一步。」把 AI 从「代驾」调教成「副驾」。

第三步，验证它的每句话涉及「在哪里」。AI 最常见的翻车点是菜单路径，版本迭代理由，它说的入口可能在你的版本里换了位置。凡是指路的答案，自己到界面上确认一遍，找不到就回问「在我这个版本里这个入口在哪」。涉及版本号的回答，去官网核对再采用，这条规矩贯穿全书。

什么时候不该用 AI？<strong>你还没有报错、只是「感觉慢」的时候。</strong>先观察：等它跑完，看看状态栏和 Build 输出。很多「卡住」其实是正常的下载进度，AI 会一本正经地教你重装一遍，白折腾半小时。工具再聪明，也替代不了你对自己环境的观察。

#### 四、工程结构拆解：每个文件是干嘛的

第一次打开项目，左侧的文件树可能让你头晕。别慌，日常开发你 90% 的时间只跟下面这几个打交道：

::: div .figure
```html
<svg aria-hidden="true" style="max-width:100%;height:auto" width="600" height="300" viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg">
 <rect x="0" y="0" width="600" height="300" rx="8" style="fill:var(--surface-6)" />
 <text x="20" y="30" font-size="13" font-weight="bold" style="fill:var(--ink-3)">MyFirstApp/ 项目根目录</text>
 <rect x="30" y="45" width="540" height="230" rx="6" style="fill:var(--ink-inverse);stroke:var(--line-2)" />
 <text x="45" y="70" font-size="11" font-weight="bold" style="fill:var(--accent-book)">app/ ← 你写代码的地方</text>
 <rect x="60" y="82" width="240" height="178" rx="5" style="fill:var(--accent-wash)" />
 <text x="70" y="102" font-size="10" font-weight="bold" style="fill:var(--accent-deep)">src/main/</text>
 <text x="80" y="120" font-size="10" style="fill:#374151">├ java/…/MainActivity.kt ← 逻辑代码</text>
 <text x="80" y="138" font-size="10" style="fill:#374151">├ res/ ← 资源（图片、文字、颜色）</text>
 <text x="80" y="156" font-size="10" style="fill:#374151">└ AndroidManifest.xml ← 应用"户口本"</text>
 <text x="70" y="180" font-size="10" font-weight="bold" style="fill:var(--accent-deep)">build.gradle.kts</text>
 <text x="80" y="198" font-size="10" style="fill:var(--muted-2)">声明依赖的库（SDK 版本、Compose 等）</text>
 <text x="70" y="222" font-size="10" font-weight="bold" style="fill:var(--accent-deep)">src/androidTest/ 与 test/</text>
 <text x="80" y="240" font-size="10" style="fill:var(--muted-2)">自动化测试代码（第 56 章用）</text>
 <rect x="320" y="82" width="230" height="178" rx="5" style="fill:#f0fdf4" />
 <text x="330" y="102" font-size="10" font-weight="bold" style="fill:#065f46">根目录的其他文件</text>
 <text x="340" y="122" font-size="10" style="fill:#374151">gradle/ + gradlew.bat ← 构建脚本</text>
 <text x="340" y="142" font-size="10" style="fill:#374151">settings.gradle.kts ← 项目设置</text>
 <text x="340" y="162" font-size="10" style="fill:var(--muted-2)">（新手的口诀：只碰 app/ 目录，</text>
 <text x="340" y="180" font-size="10" style="fill:var(--muted-2)">其余的先当"黑盒"，别乱动）</text>
 <text x="340" y="208" font-size="10" style="fill:var(--muted)">.gitignore ← 版本控制忽略清单</text>
 </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
图 2：新手必懂的工程结构（口诀：只碰 app/ 目录）
:::

- <strong>MainActivity.kt</strong>：App 的「大门」。用户点开图标，第一个被唤醒的就是它。现在的模板里它负责显示「Hello Android!」。
- <strong>AndroidManifest.xml</strong>：App 的「户口本」，声明这个 App 叫什么、图标是哪个、有哪些页面、要用哪些权限（相机、定位等）。
- <strong>res/ 目录</strong>：资源仓库，存图片、图标、字符串、颜色。把文字放资源文件而不是写死在代码里，是安卓开发的好习惯（换语言、换主题都方便）。
- <strong>build.gradle.kts</strong>：构建配方：声明最低支持版本、依赖哪些库（比如 Compose）。

图里「只碰 app/ 目录」这句口诀再强调一遍：根目录那堆文件是构建系统的「厨房后台」，新手阶段一个都不要动。等你读完全书、能看懂构建配置了，自然会去碰它们；现在动了只有坏处：改坏一个标点，整个项目可能就编不出来了。

顺带解释「Android 视图 vs Project 视图」的困惑。左侧面板默认的 Android 视图是「整理过」的样子，它把真实磁盘结构按「对开发者友好」的方式重新排了序，比如把 java/ 和 res/ 合并显示成一个 app/ 的内部结构。切到 Project 视图（面板左上角下拉切换），你看到的是磁盘上的真实样子：多出一堆以点开头的配置文件夹、build 产物目录等等。两个视图展示的是同一个项目，不是两份文件。看教程时如果截图里的文件树跟你的对不上，先检查视图再怀疑人生。

还有一类「看不见的文件」也要认识：<code class="inline">.gradle</code> 和 <code class="inline">build</code> 这两个自动生成的目录（前面讲构建时提过）。它们是机器的临时工作区，删了能重建。你拷贝项目给别人、或者用 Git 提交项目时，都不带它们<code class="inline">.gitignore</code> 文件已经替你把这些写进忽略清单了。

#### res/ 目录漫游：把「字」和「图」都归置好

res/ 是你最早要熟悉的一块地盘。打开它，会看到几个子文件夹，每个有固定含义：

- <strong>values/</strong>：字符串、颜色、样式的「字典」。其中 <code class="inline">strings.xml</code> 最常用——应用名、按钮文字都定义在这里。
- <strong>drawable/</strong>：图片和矢量图形。你画的各种小图标放这里。
- <strong>mipmap/</strong>：应用图标专属目录（launcher icon），系统会按屏幕密度挑合适的尺寸。
- <strong>themes/</strong>：主题定义，颜色方案和深色模式都从这里出发。

为什么安卓这么执着地让你把文字放进 XML 而不是写在代码里？看一眼 <code class="inline">strings.xml</code> 的样子：

::: div .code-block
:::inline div .code-head
<span>XML · res/values/strings.xml</span><span class="dots">···</span>
:::

```
&lt;resources&gt;
 &lt;string name="app_name"&gt;My First App&lt;/string&gt;
 &lt;string name="welcome_text"&gt;你好，张三！这是我的第一个App&lt;/string&gt;
&lt;/resources&gt;
```
:::

三个好处立竿见影。其一，<strong>改文案不用动代码</strong>：产品经理说「欢迎语换个说法」，你改一行 XML，代码零改动。其二，<strong>多语言几乎白送</strong>：新建一个 <code class="inline">values-zh-rCN</code> 这样的文件夹（资源限定符），放一份中文翻译的 strings.xml，系统会自动按手机语言挑对应文件：这就是国际化的全部秘密的入口。其三，<strong>深色模式同理</strong>：<code class="inline">values-night</code> 文件夹里放一套深色配色，系统切深色模式时自动换装。资源系统 + 限定符文件夹，是安卓「一套代码适配千机」思想的根基。

代码里怎么引用这些资源？通过一个叫 R 的自动生成类：<code class="inline">R.string.app_name</code> 就是刚才那行字符串的「门牌号」。你在 Compose 里写 <code class="inline">Text(stringResource(R.string.welcome_text))</code>，就能把资源文字显示到界面上。R 类是构建时自动生成的，报错说 「Unresolved reference: R」 时，多半是资源文件写错了，回头检查 XML。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：别把资源文件改名改出大事

{class="mt-1"}
资源文件名只能小写字母、数字和下划线，大写字母或空格会让整个项目编不过，报错还指不到文件本身。给资源命名时用「用途_描述」的格式，比如 <code class="inline">icon_back</code>、<code class="inline">text_welcome</code>，一周后你自己还能看懂。
:::

#### AndroidManifest.xml：户口本逐行看懂

Manifest 文件平时不需要你频繁编辑，但每次加新页面、新权限都会路过它。打开 app/src/main/AndroidManifest.xml，结构大致是这样：

::: div .code-block
:::inline div .code-head
<span>XML · app/src/main/AndroidManifest.xml（节选）</span><span class="dots">···</span>
:::

```
&lt;manifest ...&gt;
 &lt;application
 android:icon="@mipmap/ic_launcher"
 android:label="@string/app_name"
 android:theme="@style/主题..."&gt;

 &lt;activity
 android:name=".MainActivity"
 android:exported="true"&gt;
 &lt;intent-filter&gt;
 &lt;action android:name="android.intent.action.MAIN" /&gt;
 &lt;category android:name="android.intent.category.LAUNCHER" /&gt;
 &lt;/intent-filter&gt;
 &lt;/activity&gt;
 &lt;/application&gt;
&lt;/manifest&gt;
```
:::

三处重点。<strong>application 标签</strong>的三个属性决定 App 的「脸」：icon 指向桌面图标，label 指向应用名（就是从 strings.xml 引用的，资源系统又出现了），theme 指向主题。<strong>activity 标签</strong>里那个 intent-filter 是「这是入口页面」的声明：MAIN 加 LAUNCHER 的组合告诉系统「我有一个可以从桌面点开的入口」，少了它，应用装上了却没有图标。以后你每加一个新页面（Activity），都要来这里登记一笔，户口本嘛，人口要如实申报。<strong>uses-permission</strong> 标签（模板里暂时没有）是申请权限的地方：用相机、定位、网络时按需添加，第 57 章讲权限时再细拆。

还有个小知识：老教程里 manifest 有 <code class="inline">package="..."</code> 属性，新项目里没有：它搬家了，搬进了 build.gradle.kts 的 namespace 字段。看到老代码里 manifest 里有包名、你的没有，不是谁抄错了，是时代变了。

#### Gradle：项目的「总管家」

接下来这几节咱们把构建系统说透。Gradle 到底是什么？一句话：<strong>按你的配方，把代码、资源、依赖库加工成可安装包的项目管家。</strong>你写完代码点 Run，中间发生的「编译、合并资源、打包、签名、安装到设备」，全是 Gradle 在干活。它读的「配方」就是那些 build.gradle.kts 文件。

新手只需要分清两件事：<strong>Sync（同步）和 Build（构建）。</strong>Sync 是「管家重新读一遍配方」：你改了任何构建文件，IDE 都会要求重新 sync，检查配方有没有矛盾、下载新声明的依赖。Build 是「按配方真干活」：编译打包。改代码不需要 sync，直接 Run；改构建文件必须 sync。菜单栏有个大象图标的按钮（Sync Project with Gradle Files），它出现黄色提示点它就对了。

根目录里的 <code class="inline">gradlew</code> 和 <code class="inline">gradlew.bat</code> 是「Gradle 包装器」的启动脚本（bat 是 Windows 用的）。它的存在解决了一个经典问题：不同的人、不同的电脑装的 Gradle 版本不一样，同一个项目就编出不同结果。包装器强制「这个项目永远用声明的那一版 Gradle」，你换电脑、同事拉你的项目，构建环境自动对齐。这就是为什么你几乎永远不需要手动安装 Gradle。

还有一个容易忽略的成员：<code class="inline">gradle/</code> 文件夹里的 <code class="inline">libs.versions.toml</code>，叫「版本目录」（version catalog）。新项目把所有依赖的版本号集中写在这个文件里，各 build 文件用别名引用它。好处是版本号只有一处真相源，改版本不会漏改。你在代码里看到 <code class="inline">libs.compose.ui</code> 这种引用，源头就在那个 toml 文件。

#### build.gradle.kts 逐段拆解：看得懂构建配方了

打开 app/ 目录下的 build.gradle.kts（注意有两个 build.gradle.kts：根目录一个管整个项目，app 目录一个管你的应用，日常你编辑的是 app 这个）。逐段看：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · app/build.gradle.kts（结构示意，数值以你项目的实际生成为准）</span><span class="dots">···</span>
:::

```
plugins {
 alias(libs.plugins.android.application) // 安卓应用插件
 alias(libs.plugins.kotlin.android) // Kotlin 语言插件
 alias(libs.plugins.kotlin.compose) // Compose 编译插件（跟 Kotlin 版本走）
}

android {
 namespace = "com.example.myfirstapp" // 包名（从 Manifest 搬来的那个）
 compileSdk = 36 // 编译目标 API（以向导生成为准）

 defaultConfig {
 applicationId = "com.example.myfirstapp" // 商店里的唯一身份
 minSdk = 26 // 最低支持 Android 8.0
 targetSdk = 36 // 目标 API（跟随商店政策逐年抬高）
 versionCode = 1 // 内部版本号，每次上架递增
 versionName = "1.0" // 用户看到的版本名
 }

 buildTypes {
 release { // 正式包：默认开启压缩混淆
 isMinifyEnabled = true
 }
 }
}

dependencies {
 // Compose 全家桶的版本交给 BOM 统一定价
 implementation(platform("androidx.compose:compose-bom:2026.08.00"))
 implementation("androidx.compose.ui:ui") // 注意：不写版本号
 implementation("androidx.compose.material3:material3")
 implementation("androidx.activity:activity-compose")
}
```
:::

<strong>plugins 块</strong>：声明「这个项目用哪些插件」。三个插件各有分工：安卓应用插件负责把东西打包成 APK/AAB，Kotlin 插件负责编译 Kotlin 代码，Compose 插件负责让 @Composable 函数能工作。注意它们都用 alias 引用版本目录——版本号在 gradle/ 目录的 toml 文件里，不在眼前，这是新项目的默认组织方式。

<strong>android 块</strong>：应用的「出厂参数」。namespace 是包名；compileSdk 是「我用哪个版本的 API 编译」——通常跟最新稳定版走；defaultConfig 里的三兄弟值得一个一个说清楚：<strong>minSdk</strong> 是「最低能装到哪个版本」（低于它的手机装不上，向下兼容的代价是很多新语法不能直接用）；<strong>targetSdk</strong> 是「我声明自己按哪个版本的规则运行」——系统看到这个数字，决定对你启用哪些新行为。谷歌商店的政策会逐年抬高 targetSdk 门槛（比如 API 37 的新要求自 2027 年 8 月起生效，具体以官方政策页为准），所以它迟早要跟着涨。<strong>versionCode</strong> 是整数版本号，上架后每次更新都要递增，用户看不见；versionName 才是用户看到的「1.0」。

<strong>dependencies 块</strong>：你项目的「购物清单」，每一行 implementation 是「我要用这个库」。最值得看懂的是 BOM 那一行：Compose 的十几个库各自都在更新，版本对不齐就打架。BOM（Bill of Materials，物料清单）说「这一批库的版本组合我打包认证过」——你声明了 BOM，下面每个 Compose 库就不用写版本号，全都由 BOM 统一分配。这是官方推荐的姿势，也是第八节报错门诊里「依赖打架」病的特效药。

改这个文件的规矩只有两条：改完必须 sync；一次只改一处。它会成为你未来最常打开的文件之一，每次想加个新库（图片加载、网络请求），都是来这里添一行清单。

#### 五、小试牛刀：把「Hello」换成你的名字

打开 MainActivity.kt，你会看到 Compose 模板生成的代码。找到 <code class="inline">Text(「Hello Android!」)</code> 这一行，把引号里的字换成你的名字，比如 <code class="inline">Text(「你好，张三！这是我的第一个App」)</code>，然后点工具栏的绿色三角 Run（Windows 默认 <kbd>Shift+F10</kbd>；Mac 默认 <kbd>Ctrl+R</kbd>）重新运行。几秒后，模拟器上就显示了你的名字。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · MainActivity.kt（改这一行）</span><span class="dots">···</span>
:::

```
setContent {
 MyFirstAppTheme {
 Surface(modifier = Modifier.fillMaxSize()) {
 // ▼ 把这里改成你自己的文字
 Text("你好，张三！这是我的第一个App")
 }
 }
}
```
:::

恭喜，你已经完成了一次完整的「改代码 → 编译 → 安装 → 运行」循环。这个循环，就是未来每一天的开发日常。趁热打铁，试着再改点别的：把字号调大、换个颜色——下一章我们就会学到这些「魔法」是怎么来的。

这里埋个作业：把那句话从代码里挪出去，放进 strings.xml，再在代码里用 <code class="inline">stringResource(R.string.welcome_text)</code> 引用它。做成这一步，你就把上一节的资源系统真正用上了，学以致用的闭环，就此打通。

#### 改完没生效？三个排查动作

偶尔你会遇到「明明改了代码，跑起来还是老样子」。按这个顺序排查，九成能解决：

1. <strong>确认真的点了 Run</strong>：改完代码不点 Run，模拟器里跑的还是旧包——这是出现频率最高、也最尴尬的一种。看一眼 Build 输出有没有新一轮构建的滚动记录。
2. <strong>确认改对了文件</strong>：同名文件可能不止一个（比如复制过项目），检查编辑器顶部的文件路径，确认是当前项目里那个 MainActivity.kt。
3. <strong>确认设备上是新包</strong>：极端情况（改了包名、版本冲突）下设备会拒绝覆盖安装旧版本仍在运行。把模拟器上的应用长按卸载，重新 Run 一次。

顺带预告一个后面才会用到的省时神器：Live Edit 之类「改了立即生效」的编辑功能，Compose 学到第 51 章再解锁。现在老老实实「改 → Run → 看」，先把循环跑顺，再谈加速。

#### 六、常见报错急救：新手前两周的「急诊室」

环境搭建和首次构建阶段，你会大概率遇到下面三种报错。别慌，都有解药：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">报错现象</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">常见原因</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">解药</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle sync failed / 依赖下载慢</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">网络访问仓库不畅</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">给 Gradle 配置国内镜像仓库（阿里云/腾讯云 maven 镜像），网上搜"gradle 国内镜像"照着改</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SDK 组件缺失</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">安装时跳过了 SDK 下载</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Settings → SDK Manager 补装缺失的平台与工具</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">模拟器启动失败 / 黑屏</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">虚拟化未开启、镜像损坏</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BIOS 开 VT-x/AMD-V；删掉模拟器重建；或直接用真机调试</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">依赖版本互相打架</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">IDE、AGP、Gradle、Kotlin 插件没对齐</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">按下一节的版本链逐项核对；Compose 依赖交给 BOM 统一管</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
新手环境报错急救表

这张急救表覆盖的是「高频大病」，但真实世界的报错千奇百怪。下面把门诊继续开下去——九个真实病例，每个按「症状 / 诊断 / 处方」三段式走，欢迎对号入座。

##### 病例一：依赖下载失败（Could not resolve）

症状：Sync 报错一大串 「Could not resolve all files」，最后总有 「Could not get ...」 或超时（timeout）字样。诊断：十有八九是网络到仓库的路不通， Gradle 去国外仓库拉包被卡住。处方：给 Gradle 配国内镜像仓库（急救表第一行的做法），或者重试几次、换个时段。判断是不是网络问题的土办法：把报错里的网址复制到浏览器里开一下，浏览器都打不开，就是路的问题，不是代码的问题。

##### 病例二：Unsupported class file major version

症状：构建报 「Unsupported class file major version」 加一个大数字。诊断：Java 版本和 Gradle 版本不匹配，大数字对应更新的 JDK。处方：新手不该自己配 JDK。到 <kbd>Settings</kbd>、<kbd>Build, Execution, Deployment</kbd>、<kbd>Build Tools</kbd>、<kbd>Gradle</kbd>，把 Gradle JDK 设成 IDE 内置（Embedded）的那个选项，重新 sync。整个安卓工具链自带配套 JDK，你唯一要做的是「别去手动换它」。

##### 病例三：SDK location not found

症状：打开一个从别处拷来的项目（或解压的项目 zip），Sync 报 「SDK location not found. Define a local.sdk...」。诊断：项目里有个 local.properties 文件记录了「SDK 装在这台电脑的哪里」，拷贝过来的项目带着别人电脑的路径，或者压根没带上这个文件。处方：关掉报错，新建一个空项目（能正常构建的那种），把它根目录的 local.properties 拷到报错项目里，重新打开。这个文件记录的是本机路径，本来就不该跟着项目走。

##### 病例四：AGP 与 Gradle 版本互相看不上

症状：Sync 报错提到 「requires Gradle X」 或 「minimum compatible Gradle version」。诊断：安卓 Gradle 插件（AGP）和 Gradle 版本没对齐，版本链断了一环。处方：别手改版本号碰运气，先看第七节的版本链方法，再到官方的「AGP 与 Gradle 兼容表」（developer.android.com 上有）核对；或者干脆用升级向导（IDE 会对可升级的项目给出建议入口）。版本链的完整逻辑第七节展开，这里先立个规矩：<strong>版本号只动向导生成的那份，改之前一定查兼容表。</strong>

##### 病例五：模拟器报硬件加速错误

症状：启动模拟器弹窗 「x86 emulation currently requires hardware acceleration」 或类似字样。诊断：CPU 虚拟化没开、被其他软件占用，或者镜像的架构（ABI）跟你的 CPU 对不上。处方：按顺序查，BIOS 里确认 VT-x/AMD-V 开着；检查前面说的虚拟化占用冲突；确认镜像 ABI 选对了（Intel/AMD 用 x86_64）。三步查完还不行，别恋战，切真机调试，改天再修模拟器。

##### 病例六：Installed Build Tools revision is corrupted

症状：构建报 「Installed Build Tools revision ... is corrupted」。诊断：Build-Tools 组件没装全或下载损坏（常见于网络抽风时的半截包）。处方：<kbd>Settings</kbd> → <kbd>SDK Manager</kbd> → SDK Tools 标签，勾上对应版本点 Apply 重装。这类「文件损坏」病通常是下载中断的遗留，重装即愈，不用怀疑人生。

##### 病例七：INSTALL_FAILED_USER_RESTRICTED

症状：代码编译成功。往真机装的时候报 INSTALL_FAILED 开头的一串。诊断：手机厂商的安装限制，定制系统默认拦「来自电脑的安装」。处方：开发者选项里找到「USB 安装」或「USB 调试（安全设置）」打开；小米机型可能还要求登录账号后才能开这个开关，各家具体规则以厂商说明为准。开了还不行，卸载设备上的旧包再试。

##### 病例八：Unresolved reference（代码满屏红）

症状：代码里一堆名字变红，提示 「Unresolved reference」。诊断：三种可能，按概率排，你刚改了 build.gradle.kts 但还没 sync；你刚在资源文件里加了新东西，R 类还没重新生成；真的打错了字或者漏了 import。处方：先 sync 一次；不行就检查资源 XML 有没有语法错误；最后看红字是不是真的拼错了（多数时候是）。报错指向的第一行不一定是病根，顺着红色往上游找。

##### 病例九：Waiting for device to come online

症状：Run 之后底部一直转圈 「Waiting for device to come online」，最后失败，诊断：设备连接假死——模拟器或真机状态和 ADB 的登记对不上了。处方：设备下拉框里确认目标设备状态图标；模拟器就冷启动一次（Device Manager → 下拉菜单 → Cold Boot），真机就拔插数据线；再不行，电脑终端跑 <code class="inline">adb kill-server</code> 然后 <code class="inline">adb start-server</code>。这一套「重启三连」专治设备假死，记住它，能省下无数个深夜。

##### 病例十：构建越来越慢，最后彻底卡住

症状：以前十几秒完成的构建，越用越慢，某天彻底卡在某个百分比。诊断：构建守护进程的状态坏了，或者磁盘满了导致缓存写不进去（后者在 C 盘常年飘红的机器上高发）。处方：先看磁盘剩多少，不够就清 Gradle 全局缓存里旧版本的目录（它们能再生）；然后菜单 <kbd>File</kbd> → <kbd>Invalidate Caches</kbd> 重启 IDE。还慢就重启电脑：构建服务是常驻进程，重启是对它最彻底的「关机再开机」。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小贴士：搜报错的方法论

{class="mt-1"}
报错信息第一行是最有价值的，把它原样复制进搜索引擎，加「android studio」关键词。别搜「我装不上环境怎么办」这种笼统问题，搜「Gradle sync failed: Could not resolve com.android.tools.build」这种具体错误。精确的问题，才有精确的答案。
:::

#### 七、版本怎么对齐（比记住代号更重要）

安装那一步说过：别按旧教程里的动物代号找安装包，以官网当前稳定版为准。这里把话说透，代号年年换，真正要对齐的是「IDE ↔ AGP ↔ Gradle ↔ SDK ↔ Kotlin/Compose 插件」这条链：

- <strong>Compose Compiler 已换插件</strong>：现在用 <code class="inline">org.jetbrains.kotlin.plugin.compose</code>，由 Kotlin 侧统一管理，不再单独配 <code class="inline">kotlinCompilerExtensionVersion</code>。
- <strong>用 BOM 管 Compose 版本</strong>：依赖里声明 <code class="inline">platform(「androidx.compose:compose-bom:2026.08.00」)</code>，其余 Compose 依赖不再写版本号，避免互相打架。
- <strong>Kotlin 与编译器要配套</strong>：Compose 1.13 系列要求 Kotlin 2.2；升级 IDE 时，顺手确认 Gradle 与 Kotlin 插件也在兼容区间。
- <strong>硬件的事第一节讲过了</strong>：磁盘留足、虚拟化打开；老机器优先用真机调试，体验反而更流畅。

这条链上的每一环都有「我不将就、你太老了」的脾气：IDE 太新而 Gradle 太旧，Sync 就罢工；Kotlin 插件太新而 Compose 插件太旧，编译就报错。新手看到这种报错最容易做的事是「挨个升级」——大忌，一次只动一环，动完 sync 看结果。链条对齐了，工具们才能合唱；错一环，全场跑调。

再给一张可以核对的小表——把它当索引，别当答案：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">组件</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">2026-11 可核对的稳定值</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">去哪确认</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Compose UI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1.12.1（1.13.0 处于 beta）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AndroidX Compose 发布说明</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Material 3</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1.4.0（1.5.0 处于 alpha）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AndroidX Compose 发布说明</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Compose BOM</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2026.08.00</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Compose BOM 版本映射页（developer.android.com）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.x（1.13 要求 2.2）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin 发布说明</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minimum SDK</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">示例项目用 API 26</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新建项目向导</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
版本对齐速查（动手前打开官网核对当前稳定版）

::: div .tip-box .rounded-lg .p-4 .mb-3
{class="font-semibold"}
一句话记牢

{class="mt-1"}
把这张表当索引，不要当答案：动手前打开官网看一眼当前稳定版，比背版本号可靠。
:::

#### 新手五个误区：以为 X，其实 Y

环境这一章攒下来的误区，值得单独拉个清单。看看你中了几条：

- <strong>误区一：以为要先把快捷键背全。</strong>其实你需要的快捷键就五个左右：Run、停止、查找文件（双击 Shift）、代码格式化、复制行。其余的用到再学，IDE 的提示会追着你教。
- <strong>误区二：以为模拟器卡说明代码写得烂。</strong>模拟器的流畅度和你的代码没关系，只和电脑配置、镜像、ABI 有关。代码性能问题要靠工具测量（第 56 章），不靠「感觉卡不卡」。
- <strong>误区三：以为报错都是自己的错。</strong>环境类报错一半以上和网络、磁盘、版本链有关，跟你的智力零关系。先查环境三件套，再怀疑自己。
- <strong>误区四：以为要背下整个工程结构。</strong>你只需要记住五个东西：MainActivity、Manifest、res/、build.gradle.kts、「只碰 app/」。其余的用到再查，图就挂在那儿。
- <strong>误区五：以为教程里的版本号必须分毫不差。</strong>教程滞后于版本是常态，思路和方法照学，版本号以官网为准，这也是本书反复强调「以官方为准」的原因。
- <strong>误区六：以为设备列表里的名字就是手机的型号。</strong>有时下拉框里显示的是一串代号或「未知设备」，跟手机品牌对不上。名字乱了不代表连接坏了，看设备图标状态（在线/离线）更可靠；真要确认，跑一下 <code class="inline">adb devices</code> 对序列号。

#### 常见问题快答（工程结构篇）

拆完结构和构建系统，问题清单又涨了一批。快问快答，不绕弯：

- <strong>问：左侧文件树里找不到 MainActivity.kt，是不是装坏了？</strong>答：先切视图。Android 视图里它在 app/java/你的包名下；Project 视图里在 app/src/main/java/ 下。还找不到就用双击 Shift 搜文件名，按两次 Shift 呼出全项目搜索，这个快捷键你会用一辈子。
- <strong>问：两个 build.gradle.kts 我该改哪个？</strong>答：app 目录下那个管你的应用（加依赖、改版本），根目录那个管整个项目的插件配置。拿不准就看你 要改的内容：加库、改 minSdk 都在 app 的。
- <strong>问：libs.versions.toml 是必需的吗？我看有些教程直接在依赖里写版本号。</strong>答：不是必需，是新版向导的默认组织方式。两种写法都合法，跟着你项目的现状走，别照教程把两套写法混着抄。
- <strong>问：res/ 里的每个文件夹都是我手动建的吗？</strong>答：不是，模板会建好常用的；需要新文件夹（比如 values-night）时右键 res/ → New → Android Resource Directory，选好限定符让 IDE 帮你建：手建文件夹不会被识别成资源目录，这是新手常见的坑。
- <strong>问：Manifest 里那个 android:exported="true" 是什么意思？</strong>答：声明「这个页面对其他应用开放调用」。入口页面必须为 true（桌面要能拉起它），内部页面一般 false。它和安全强相关，第 57 章细讲，现在保持模板原样就好。
- <strong>问：gradlew.bat 能双击运行吗？</strong>答：能，但没必要。IDE 会替你调它。它的价值是命令行构建（第 56 章打包时会用到），现在知道它是「永不换版的 Gradle」即可。
- <strong>问：我把项目文件夹改名了，现在打不开了。</strong>答：文件夹改名本身没问题，重新用 Open 打开新路径即可；如果项目已经登录过「最近项目」列表，旧入口会失效，别点它，走欢迎页 Open 选新文件夹。改包名才是大手术，别和文件夹改名混为一谈。

#### 把项目交给别人：备份、导出与二次打开

迟早有一天，你想把项目拷给朋友、换台电脑继续写，或者备份一份。记住一个原则：<strong>项目 = 文件夹，备份 = 整个文件夹原样复制。</strong>右键项目文件夹压缩成 zip，就是最可靠的备份。哪台电脑装好了环境，把这个 zip 解压、用 Open 打开文件夹，它就复活了。

几个细节让这个操作更稳。第一，压缩前最好把项目里的 <code class="inline">build</code> 和 <code class="inline">.gradle</code> 文件夹删掉，它们是可再生的临时产物，占了 zip 里的大头，还会把这台电脑的构建状态带到另一台电脑。第二，解压到全英文路径再打开，别在压缩软件里直接双击打开项目。第三，别人打开你的项目时会重新 sync 一轮，他自己电脑缺的依赖会被自动下载，属于正常现象，不是项目坏了。

反向场景也要会说：你收到别人发来的项目（比如本书配套示例），<strong>不要用「最近项目」里残留的旧入口</strong>，走欢迎页的 Open，选中项目文件夹打开，等第一轮 sync 跑完再动代码。如果 sync 报「SDK location not found」，翻回报错门诊的病例三。

更专业的备份方式是 Git（第 23 章附专门讲过 GitHub 入门），学习阶段的早期用压缩包完全够用，等你项目多了、改坏了想回退时，再迁到 Git，那个「后悔药」的用法，第 45 章已经教过方法论。

#### 顺手来一发：把 APK 发给朋友装

这一节是本章的彩蛋，也是「开发者成就感」的第一次变现：把你写的东西真的装到别人的手机上。菜单 <kbd>Build</kbd> → <kbd>Build App Bundle(s) / APK(s)</kbd> → <kbd>Build APK(s)</kbd>，构建完成后右下角会弹出通知，带「locate」链接——点开就是产出的 APK 文件，路径在 app/build/outputs/apk/debug/ 下面。

把这个 APK 文件用微信/网盘发给自己或朋友，手机上点开安装（需要允许「安装未知应用」，第 4 章讲过的那道门）。朋友手机上出现你的「你好，张三」，那种感觉和模拟器上完全不同，这是第一次，你的作品走出了你自己的设备。

三点说明提前打上。其一，这是 debug 包（调试签名），装着玩、学习交流都没问题，正式上架要换正式签名，第 56 章讲。其二，对方的手机要开「允许安装未知应用」的权限，不同品牌入口不同，以厂商说明为准。其三，Android 高版本对这种安装包有更强的安全检查，如果你的应用以后加了权限和特殊功能，这条「裸发 APK」的路会越来越受限——先玩起来，规矩后面再守。

#### 资源系统的实战检验：深色模式与多语言

前面讲 res/ 时说过「限定符文件夹」是安卓适配千机千人的根基，现在就带你亲手验证一次，这个实验十分钟做完，成就感却很足。

<strong>实验一：深色模式自动换装。</strong>右键 res/ → New → Android Resource Directory，目录类型选 values，限定符里选 Night Mode → Night，得到一个 values-night 文件夹。在里面新建一份 colors.xml，把主色定成深蓝或深灰。然后打开模拟器，下拉快捷面板点深色模式开关（或用侧边 Extended Controls），你的 App 跟着变装。你会亲眼看到「系统状态改变 → 资源系统自动换文件」的全过程——没有一行代码，全靠目录名的约定。

<strong>实验二：多语言随手可得。</strong>同样的路数，建一个 values-zh-rCN 文件夹（语言选 Chinese、地区选 China），放一份 strings.xml，把应用名翻译成中文。然后把模拟器系统语言切到中文——应用名和界面文字自动换成中文版；切回英文，又变回去。那一刻你会理解为什么书前面强调「文字别写死在代码里」：写死的文字是钉死的招牌，进资源文件的文字是随系统变形的水。

两个实验都完成后，回望 build.gradle.kts 里的 minSdk、res/ 里的限定符、模拟器的深色开关，你会发现本章学的所有东西其实是一个整体：<strong>环境、结构、资源、构建，共同服务于「一套代码适配万千设备」这个安卓的根本设计。</strong>下一章开始，我们往这套系统里装真正的东西，界面的代码。

#### 效率起步包：三个顶得上半个老师的功能

收尾前送你三个「用了就回不去」的功能，比背快捷键划算得多：

- <strong>双击 Shift 全局搜索</strong>：按两下 Shift 呼出「搜一切」面板，找文件、找设置、找代码里的符号全靠它。你记不住功能藏在哪个菜单没关系，会搜就行。IDE 上千个功能点，这一个入口全都能带你到。
- <strong>代码补全</strong>：写代码打到一半停下来，IDE 会浮出候选列表，Tab 或回车选中。它不只是帮你省字，更是一个「活的语法教材」：你记不清某个函数叫什么、参数是什么，列表里全写着。配合代码右边的灰色提示行（IDE 的「灯泡」建议），新手期一半的问题在写代码的当下就被解决了。
- <strong>快速文档</strong>：光标停在函数名上按文档快捷键（悬浮窗口会标出组合键），该函数的官方说明直接弹出。养成「不懂就看文档」的习惯，比每次都去网上搜快，而且永远和你的版本一致。

这三个功能的共同点是：<strong>它们把「记忆」外包给了工具。</strong>安卓的 API 面大得没人能全记住，真正拉开差距的不是记性，是你多快能找到「该用的那个东西」。本书后面所有章节的实操，都默认你已经会这三招。

#### 环境搭好之后的一天：你的开发日常

最后把镜头拉远，看看环境搭好后，你的普通一天长什么样。早上打开电脑，启动 Android Studio，欢迎页点开昨天那个项目：它会先自动 sync 一会儿，泡杯茶回来刚刚好。之后是一段你可能想不到的事实：<strong>写代码的时间其实只占一小半</strong>，剩下的是 Run 等待、看效果、改细节、再 Run 的循环，以及偶尔的构建报错排查。

一个上午的典型节奏：改几行代码，Shift+F10，看模拟器，不满意，再改，再 Run。每次 Run 等十几秒到几十秒（视改动大小），这段时间可以瞄一眼刚改的逻辑，或者看看底部 Logcat 有没有新日志。这个节奏听着琐碎，但它是所有安卓开发者共同的日常，第 51 章开始写界面后，你每天都会在这条流水线上转几十圈。习惯了这个循环，后面任何新知识点都只是在循环里替换某一段工序而已。

晚上收工，建议养成两个小仪式：项目文件备份（压缩包扔网盘，或学第 57 章前的简化版 Git 提交）；顺手关掉模拟器和真机的 USB 调试。第二件事跟第 3 章的安全习惯一脉相承——开发者身份和普通用户身份，在「门」这件事上要一样谨慎。仪式虽小，坚持下来的价值在于：明天打开电脑时，一切都是你熟悉的样子。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
来动手：完成你的「开发仪式感」清单

{class="mt-1"}
① 装好 Android Studio 并跑通模拟器；② 用真机跑一次自己的 App 并截图留念；③ 把 Hello 文字改成你的名字；④ 把项目压缩存个档。做完这四步，你就可以在朋友圈宣布：我也是安卓开发者了（截图为证）。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小结

- Android Studio = 官方免费 IDE；建议 16GB 内存 + 20GB 磁盘 + 开虚拟化
- 新建项目三要素：名字、包名（全球唯一，com.example 别上架）、最低 SDK（API 26 起）
- 两种运行方式：模拟器（电脑里虚拟手机）与真机（开 USB 调试，用完记得关）
- 工程口诀：只碰 app/ 目录，MainActivity.kt 是大门，Manifest 是户口本，res/ 是资源仓库
- 开发日常 = 改代码 → Run → 看效果，循环往复
- 版本对齐看链条：IDE ↔ AGP ↔ Gradle ↔ SDK ↔ Kotlin/Compose 插件；Compose 版本交给 BOM
:::
