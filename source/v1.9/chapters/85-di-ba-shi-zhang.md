---
id: di-ba-shi-zhang
num: 80
nav: 第八十章：速查手册与资源
toc: default
kind: chapter
after_part: hongmeng-kai-fa-pian
---

### 第八十章：速查手册与资源

{class="chapter-intro mb-4"}
最后一章是全篇的"口袋工具"：常用命令、关键概念、官方资源一页速查。建议把这一页加入书签——写到后面前面的细节总会忘，这一页能帮你 30 秒找回记忆。

速查章的用法说明：它不是用来通读的，是"按问题查"的——遇到什么问题，翻到对应的那一表。每个表格后面都标注了"详见第几章"，忘了上下文就去那一章补。查完就关掉，继续写代码——速查章的价值就在"快进快出"。

::: div .quick-read
##### 本章速读（5 分钟版）
这一章是全篇的"口袋工具箱"：常用命令、关键概念、官方资源，一页速查。它不是拿来通读的，是"按问题查"的——写代码遇到什么问题，翻到对应的那张表，查完就关掉，继续写代码。每个表格后面都标了"详见第几章"，忘了上下文就去那一章补。建议现在就把这一页加入书签：写到后面，前面的细节总会忘，这一页能帮你 30 秒找回记忆。书里的硬信息都标了核对时间，拿不准的以官方文档为准，二手教程只当导读。
最关键的有三件事。第一，把 hdc 用顺手：它是鸿蒙版的 adb，hdc list targets 看设备、hdc install -r 覆盖安装、file send/recv 互传文件（设备上的中转目录用 /data/local/tmp）、hilog 按 Tag 过滤日志。设备列表为空先查三样：数据线是不是只能充电、USB 调试开没开、授权弹窗点没点；设备不止一台时，命令前永远带 -t，不然包装到哪台设备上全凭运气。第二，排查有固定顺序：先环境后代码，先日志（HiLog）看现象、再断点看现场、最后才是 Profiler；性能问题的口诀是<strong>先测量、再归因、后优化</strong>，改之前改之后各录一段对比，别凭"感觉快了"下结论。第三，发布三样记牢：签名三件套 .p12（密钥库）、.cer（证书）、.p7b（Profile，有有效期），打包用 hvigorw 或 IDE 的 Build 菜单，上架前确认 versionCode 比线上版本大、Profile 在有效期内——<strong>拿调试签名去上架会被拒</strong>，这是新手第一次投稿失败最常见的原因。
今天就能做的最小动作：把 DevEco 安装目录 sdk 下的 toolchains 加进 PATH，敲一句 hdc -h，能弹出帮助信息就算通了；再给自己打的日志定一个统一 Tag 前缀（比如 MyApp_Net 这样"项目缩写_模块"），以后几万行系统日志里一筛就是你的。顺手把本章"常见报错速对"那张表也截图存进相册，出问题先对号再动手，比从头翻文档快得多。
最大的坑是把速查章当小说从头读，或者收藏之后永不打开——它得"快进快出"才活得下来。几个具体翻车点也顺手记住：凭"感觉卡"就动手优化，其实很多是动效预期错位，先用 Frame 面板确认真掉帧再归因；"我明明改了怎么没生效"一半是改错了文件——版本号在 AppScope/app.json5，权限在 module.json5，签名在根目录 build-profile.json5；还有 .p12 和密码千万别提交进公共仓库，发布密钥丢了，已有应用的更新会非常麻烦，备份完还要确认备份能恢复。
##### 速查表
- 忘了命令：敲 hdc -h 查帮助，参数以它为准，别硬背旧教程
- 设备列表为空：换支持数据传输的线、开发者选项开 USB 调试、授权弹窗点允许
- 多台设备：命令前带 -t 设备key，防止包装到模拟器或别的手机上
- 日志过滤：Tag 统一前缀（项目缩写_模块），hilog -T 一筛就是你的
- 列表掉帧：LazyForEach 加稳定 key，图片按显示尺寸加载，别原图直出
- 改了没生效：版本号去 app.json5、权限去 module.json5、签名去 build-profile.json5
- 上架三查：发布签名构建、versionCode 递增、Profile 在有效期内
- 升级后满屏报错：跑 API Change Assistant，对着版本说明逐条改
:::

#### 一、命令与工具速查

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">命令/工具</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">作用</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc list targets</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">列出连接的设备（类似 adb devices）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc install xxx.hap</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">安装应用包</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc shell aa start -b 包名 -a Ability名</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">命令行拉起应用</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc file send / recv</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">与设备互传文件</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc shell aa force-stop 包名</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">强制停止应用</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc shell hilog</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">命令行查看设备日志</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DevEco Log 窗口</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">HiLog 日志过滤（tag + 级别）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DevEco Profiler</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">性能分析：CPU/内存/帧率</td></tr>
</tbody>
</table>
```
:::

hdc 的两个高频排查场景顺手记一下：设备列表为空时，先查 USB 调试是否开启、数据线是否支持数据传输（很多线只能充电）、驱动是否安装；命令报"command not found"时，是 hdc 不在 PATH 里——DevEco 安装目录的 sdk 下有 hdc.exe，把它加进环境变量一劳永逸。

HiLog 的过滤技巧也值得记：日志按 Domain 和 Tag 区分，自己打的日志用统一的 tag（比如" MyApp"前缀），过滤时一筛就是你的——别在几万行系统日志里大海捞针。

#### 二、装饰器与 Kit 速查

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">名称</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">一句话</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State / @Prop / @Link</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自有状态 / 父传子 / 父子双向（V1）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Watch</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">状态变化回调（V1）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Observed/@ObjectLink</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">嵌套对象状态观察（V1）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@ComponentV2 + @Local / @Param</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">V2 状态：组件自有 / 父传子输入</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@ObservedV2 + @Trace</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">V2 嵌套对象状态观察</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Monitor</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">V2 状态变化回调</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ArkData-Preferences</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">键值小设置</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ArkData-RelationalStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SQLite 关系库</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">NetworkKit-http</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">HTTP 请求</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Form Kit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">服务卡片</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ability Kit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UIAbility 生命周期与跳转</td></tr>
</tbody>
</table>
```
:::

状态装饰器分两代：V1 一套、V2 一套（上表已并排列出）。同一个组件里<strong>不要混用两代装饰器</strong>；新项目建议从 V2 起步，老组件要迁就整块一起迁。Kit 则是"能力包"——用哪个能力引哪个 Kit，不用的别引，包体会感谢你。

装饰器速查的"记忆钩子"送你一个：V1 三兄弟（@State 自有、@Prop 单向、@Link 双向）记成"自、进、双"；V2 三兄弟（@Local 自有、@Param 输入、@Event 回调）记成"本、入、回"。记钩子不丢方向，比背定义快。

#### 三、官方资源与学习路径

- <strong>官方文档</strong>：developer.huawei.com/consumer/cn/doc/——HarmonyOS 指南、API 参考、Best Practice 三大块，质量在国产文档里属第一梯队
- <strong>示例代码</strong>：Docs 里的 Samples 中心，官方示例按 Kit 分类可直接导入 DevEco
- <strong>认证体系</strong>：HarmonyOS 应用开发者认证（基础版免费，进阶版付费）——简历上的国产化加分项
- <strong>社区</strong>：华为开发者论坛、51CTO 鸿蒙专区；遇到 NEXT 迁移问题优先搜官方迁移指南

学习资源的"使用顺序"建议：官方文档的第一遍读法是"按 Kit 读"（每个 Kit 的指南 + API 参考），Samples 的正确打开方式是"先跑起来再改"——导入后先运行看效果，再拆解代码，最后改成自己的需求。认证考试作为学习的"收口动作"：备考过程会把散落的知识点串成体系，比裸学效率高。

遇到问题时的求助优先级：官方文档 → 官方论坛（华为工程师会回复）→ 社区帖子 → AI 助手（第 41 章的工具，贴报错让它解释）。这个顺序是按"答案可靠性"排的——越往上越权威，越往下越快但可能不准。

#### 四、版本与升级清单（2026 年 11 月核对）

命令和装饰器之外，版本坐标这类硬信息最容易记混，单独列一节。以下值写书时核对过一遍，查不到的以官方文档为准：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">项目</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">2026-11 可核对的值 / 做法</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">出处</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系统版本 ↔ API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">HarmonyOS 7.0 对应 API 26.0.0</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方升级适配指南</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SDK 预置</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自 DevEco Studio 6.0.0(20) 起预置配套 SDK</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方升级适配指南</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">版本字段</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">targetSdkVersion / compileSdkVersion / compatibleSdkVersion</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">build-profile.json5</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API 变更检查</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tools &gt; API Change Assistant</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方升级适配指南</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">行为变更示例</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">5.1.0(18) 含 ArkTS、ArkUI、XComponent 等条目</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方版本说明（2026-10-08 更新）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">构建 / 调试 / 包</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hvigor / hdc / HAP</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">开发工具文档</td></tr>
</tbody>
</table>
```
:::

- <strong>升级五步</strong>：升 DevEco Studio → 同步升命令行工具 → 跑 API Change Assistant → 新旧设备兼容性测试 → 发布到 AppGallery。
- <strong>ArkTS 严格类型四条</strong>：函数写返回类型、回调参数标类型、对象与数组有明确类型、别用 any 与动态增删属性。
- <strong>三大平台对照</strong>：安卓 Activity / iOS scenePhase / 鸿蒙 UIAbility，名字不同，回答的都是「何时创建、何时后台、何时销毁」。版本坐标也顺手对齐：安卓侧 Android 17（API level 37）2026 年 6 月正式发布，Play 商店要求 target API 37 自 2027 年 8 月起；iOS 侧 2026 年的开发基线是 Xcode 26 / Swift 6.2。
- <strong>排错顺序</strong>：先看编译报错（多半是严格类型），再查版本说明里的行为变更，最后用 DevEco Log 过滤 HiLog 定位运行时问题。

版本表的"保鲜"提醒：这张表的核对时间是 2026 年 11 月，鸿蒙的版本节奏是一年一大版——你读到它时，右上角的 API 版本大概率已经更新。核对方法不变：官方升级适配指南是唯一权威来源，二手教程（包括本书）只当导读。

::: div .tip-box .rounded-lg .p-4 .mb-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>一句话记牢

{class="mt-1"}
到这里三平台都走完了：安卓、iOS、鸿蒙。把各自的「环境 → 语言 → 界面 → 数据 → 发布」五段串起来，你会发现迁移成本主要在名字，不在思路。
:::

#### 五、hdc 命令完整手册

第一节只给了最常用的八条，这一节把 hdc 掰开揉碎讲全。你可以把本节当成 hdc 的随身说明书：用到哪条查哪条，每条都带参数说明和一个能直接抄的例子。没写到的选项，敲 <code class="inline">hdc -h</code> 就有——帮助信息永远是最权威的字典。

hdc 是鸿蒙版的 adb：电脑这头的你，靠它跟设备那头的系统对话。所有命令共享同一个骨架：<code class="inline">hdc [目标] [命令] [参数]</code>。目标不写，默认作用于当前唯一连接的设备；设备多于一台时必须用 -t 指明，不然命令会"随机"落到某一台上。

##### 先把 hdc 变顺手

- <strong>找到它</strong>：DevEco Studio 安装目录下的 sdk 文件夹里有 hdc，把它所在的 toolchains 目录加进 PATH 环境变量，以后在任何终端敲 hdc 都生效。
- <strong>验证连通</strong>：终端敲 <code class="inline">hdc -h</code>，能打印出帮助信息就通了。参数记不清时也回这里查。
- <strong>版本意识</strong>：hdc 的子命令会随工具链版本增减，遇到"参数不认"，别硬背旧教程，敲一遍 -h 核对。

##### 设备管理

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">命令</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">说明</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc list targets</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">列出已连接设备；加 -v 可看更详细的信息</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc -t 设备key 命令</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多设备时指定目标；设备key就是 list targets 打印出的那串</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc tconn IP:端口</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">连接网络里的设备（先在手机开发者选项打开无线调试，拿到它显示的 IP 和端口）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc tmode port</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把 USB 连接的设备切到网络监听，之后走 tconn 无线连接（端口等参数以 hdc -h 为准）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc kill / hdc start</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">重启本机 hdc 服务；端口被占、状态诡异时的"重启大法"</td></tr>
</tbody>
</table>
```
:::

多设备的典型翻车现场：插着真机又开着模拟器，一条 install 敲下去，包装到了模拟器上，你还纳闷"怎么没效果"。养成习惯——设备不止一台时，命令前永远带 -t，这一条习惯能省掉一半扯皮。

##### 应用安装、拉起与卸载

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">命令</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">说明</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc install xxx.hap</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">安装 HAP 包</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc install -r xxx.hap</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">覆盖安装；调试期改一版装一版，全靠这个 -r</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc shell bm uninstall -n 包名</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">卸载应用（bm 是设备端的包管理工具）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc shell bm dump -n 包名</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">查看已装应用的详细信息：版本、Ability 列表、申请的权限</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc shell aa start -b 包名 -a Ability名</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">命令行拉起应用，Ability 名写全（如 EntryAbility）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc shell aa force-stop 包名</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">强制停止应用</td></tr>
</tbody>
</table>
```
:::

::: div .code-block
:::inline div .code-head
<span>SHELL · 日常调试循环</span><span class="dots">···</span>
:::

```
hdc install -r entry-release.hap
hdc shell aa start -b com.example.myapp -a EntryAbility
hdc shell aa force-stop com.example.myapp
hdc shell bm dump -n com.example.myapp
```
:::

装包报错先看三点：包名跟已装应用冲突没有、签名跟旧包是否一致、HAP 文件本身是否完整。调试期最常见的状况是"旧版本卸不干净"，覆盖安装不行就先 uninstall 再 install，两秒钟的事。

##### 文件传输

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">命令</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">说明</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc file send 本地路径 设备路径</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把电脑上的文件推到设备</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc file recv 设备路径 本地路径</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把设备上的文件拉回电脑</td></tr>
</tbody>
</table>
```
:::

设备上约定俗成的中转目录是 <code class="inline">/data/local/tmp</code>——你有读写权限，先发到这里再挪动。日志文件、抓的截屏、测试数据，全走这条路。别往系统目录里塞东西，那是给自己挖坑。

##### 日志、截屏与界面信息

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">命令</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">说明</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc shell hilog</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">实时刷日志（Ctrl+C 停止）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc shell hilog -T 你的Tag</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">只看指定 Tag 的日志</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc shell hilog -D 0x0001</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">只看指定 Domain 的日志</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc shell hilog -L INFO</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">按级别过滤（DEBUG/INFO/WARN/ERROR/FATAL）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc shell hilog -x</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">打印当前缓冲区里的日志后退出，适合"存一段带走"</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc shell snapshot_display -f 路径</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">抓屏到设备上的文件，再用 file recv 拉回来</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc shell uitest dumpLayout</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">导出当前界面的控件树；排查"点不到"、写自动化时用</td></tr>
</tbody>
</table>
```
:::

截屏加控件树这对组合是报 bug 的标配：一张图让同事看懂现象，一棵控件树让他知道你点的是哪个节点——不用复现也能接手。导出的文件都在设备上，记得 recv 回来。

##### 系统信息查看

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">命令</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">说明</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc shell ps -ef</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">进程列表</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc shell top</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">进程资源占用，找"谁在吃 CPU"</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc shell df -h</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">各分区磁盘占用</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc shell param get 参数名</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">读系统参数；参数名以官方文档为准</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc shell hidumper -ls</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">列出系统服务（类似安卓的 dumpsys）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc shell hidumper -s 服务名</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">看某个服务的运行状态</td></tr>
</tbody>
</table>
```
:::

hidumper 的输出很专业也很长，第一次用别慌：先 -ls 找到服务名，再 -s 单查。电量、窗口、内存这些服务都能这么翻，做性能排查时经常要来一圈。

##### 进阶：端口转发与脚本化

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">命令</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">说明</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc fport tcp:本机端口 tcp:设备端口</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">端口转发：访问本机端口等于访问设备端口</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc fport ls</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">查看已有转发规则</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc fport rm 规则</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">删除指定转发规则</td></tr>
</tbody>
</table>
```
:::

端口转发的典型用途：设备上起了本地服务，你在电脑浏览器里开本机端口就能直接调。调试本地 HTTP 接口、WebSocket 时，省去一大堆网络配置。

这些命令本身就是脚本积木：装包、拉起、截屏、拉回，四步串成一个脚本，每次改完代码一键回归。以后在 CI 上做自动化冒烟，用的也是同一套命令——现在把 -t、file、hilog 用熟，到那时就是现成的手艺。

##### 无线调试六步

1. 手机开发者选项里打开"无线调试"，屏幕上会显示 IP 和端口。
2. 确认手机和电脑连的是同一个局域网（同一路由器，不是访客网络）。
3. 电脑终端敲 <code class="inline">hdc tconn IP:端口</code>。
4. 敲 <code class="inline">hdc list targets</code>，列表里多出一台网络设备即成功。
5. DevEco 的设备下拉框里也会出现它，正常点 Debug 调试。
6. 用完断开：tconn 的连接随无线调试开关关闭而断，不用专门找"断开"按钮。

##### 常见报错速对

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">报错现象</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">多半是</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">'hdc' 不是内部或外部命令</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">PATH 没配好，或终端没重开</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">list targets 结果为空</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">线不支持数据、USB 调试没开、授权弹窗没点</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">install 失败提示包名相关</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">包名冲突，卸载旧包或换包名</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">install 失败提示签名相关</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新包签名与已装版本不一致，先卸载再装</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">file send 失败</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">目标路径不存在或无权限，先用 /data/local/tmp</td></tr>
</tbody>
</table>
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>避坑提醒

{class="mt-1"}
/data/local/tmp 是你在设备上的演练场，出了这个目录的"顺手删除"都算危险操作——真机没有回收站，删掉的东西不会回来。
:::

#### 六、HiLog 日志系统详解

断点调试要你在场，日志可以事后看——线上问题、凌晨复现的 bug、用户手机上的崩溃，全靠日志说话。这节讲三件事：日志怎么打、怎么过滤、怎么打得不被人骂。

##### 三要素：Domain、Tag、级别

每条日志由三样东西定位：Domain（领域，0x0 到 0xFFFF 的十六进制数，一般一个业务域给一个号）、Tag（标签，通常一个模块一个）、级别（DEBUG 到 FATAL 五档）。过滤时最好用的是 Tag，所以打日志之前，先把团队（或你自己）的 Tag 规范定下来。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">级别</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">什么时候用</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DEBUG</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">开发期看变量、看流程，细节多、寿命短</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">INFO</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">关键节点：启动完成、请求返回、状态切换</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">WARN</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">出了问题但兜住了：降级、重试、数据异常但没崩</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ERROR</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">失败了，必须带上下文：哪个接口、哪个参数、什么码</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">FATAL</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">崩溃前最后一口气，通常框架会替你打</td></tr>
</tbody>
</table>
```
:::

##### 在代码里打日志

ArkTS 里用 hilog（从 PerformanceAnalysisKit 引入），别拿 console.log 应付一切——console 的输出不好按模块过滤，也不参与统一的级别管理，量一多就是灾难。

::: div .code-block
:::inline div .code-head
<span>ARKTS · pages/Index.ets</span><span class="dots">···</span>
:::

```
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN: number = 0x0001;
const TAG: string = 'MyApp_Net';

hilog.info(DOMAIN, TAG, '请求完成 status=%{public}d 耗时=%{public}d ms', status, cost);
hilog.error(DOMAIN, TAG, '拉取失败 code=%{public}d msg=%{private}s', code, msg);
```
:::

##### 格式化与隐私标注

hilog 的格式串里可以给每个参数标 %{public} 或 %{private}：public 明文输出，private 打成占位。默认按 private 处理——这是框架替用户挡隐私的第一道闸，也是很多人"日志里怎么全是占位符"的答案。

你的原则应该是：跟隐私无关的参数标 public 方便排查；手机号、token、位置这类干脆别打。靠 private 的默认遮挡来"偷偷打敏感信息"不是合规思路，出事没有第二道闸。

##### 窗口过滤与命令行过滤

DevEco 底部的 Log 窗口日常够用：选设备与进程，过滤框敲 Tag 或关键字，级别有颜色区分。两种场景得用命令行：应用在后台被杀、屏幕外的事，以及想把日志存档给同事——这时候：

::: div .code-block
:::inline div .code-head
<span>SHELL · 命令行捞日志</span><span class="dots">···</span>
:::

```
hdc shell hilog -T MyApp_Net -L ERROR
hdc shell hilog | grep MyApp    （Windows 传统命令行把 grep 换成 findstr）
```
:::

第二条是组合技：设备端的日志流接到本机的文本工具里再筛一道。grep 在 Git Bash 里可用，Windows 自带命令行用 findstr，效果一样。

##### 日志规范清单（可直接抄进团队 README）

- <strong>Tag 统一前缀</strong>：项目缩写_模块，比如 MyApp_Net、MyApp_DB，过滤一筛就是你的。
- <strong>级别别乱用</strong>：出问题时要能靠一行 -L ERROR 把相关记录全捞出来。
- <strong>高频路径少打 INFO</strong>：循环里、滚动回调里的 INFO 会形成日志洪峰，把关键行冲走。
- <strong>ERROR 必须带上下文</strong>：哪里、做了什么操作、错误码是多少——只打"失败了"等于没打。
- <strong>上线前过一遍</strong>：临时的 DEBUG 降级或删除，敏感字段一律不 public。

##### 三个现成的日志模板

启动埋点：应用冷启动打一条 INFO 记录总耗时，每次发版对比一眼，启动变慢第一时间发现。网络请求：发起前打一条（哪个接口），返回时打一条（状态码加耗时），ERROR 留给真正失败的。异常兜底：catch 里至少打一条 ERROR，把异常信息完整带上——静默吞掉的异常是最难查的一类 bug，因为它连"出错了"都不告诉你。

日志跟性能 Trace 的分工：日志回答"执行到没、值是多少"，Trace 回答"花了多久"。查功能性 bug 用日志，查性能问题用 Trace（下一节讲），别拿日志计时——时间戳肉眼对不齐，还容易被打印本身的开销骗。

##### "打了但看不见"三步排查

1. 过滤框里是不是残留了上一次的关键字——清掉再搜。
2. 进程下拉框选没选对——你的应用可能根本不是当前选中的进程。
3. 级别门限是不是把 DEBUG 挡了——真机上 debug 级别默认可能不输出，门限的开启方式以官方日志文档为准。

三样都排除了还看不见，多半是你打的时机根本没执行到——在那行之前加一条 INFO 验证执行路径，往往五分钟就定位了。

#### 七、调试技巧速查

断点调试的按钮就那几个，但会用条件断点和"断而不停"的人不多。这节按从最常用到进阶排列，每条独立成段，卡住时翻到对应行照做。

##### 四个单步按钮（记名字，别记键位）

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">动作</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">干什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">什么时候用</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Step Over</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">执行当前行，不进入函数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">九成的日常场景</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Step Into</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">进入函数内部</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">疑点在函数体里</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Step Out</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把当前函数跑完，停在调用处</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">进错了想快速出来</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Resume</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">放行，跑到下一个断点</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">该看的都看完了</td></tr>
</tbody>
</table>
```
:::

快捷键跟 IDE 的 Keymap 设置走，不同系统、不同习惯配置不一样。网上教程背的键位经常跟你的环境对不上——名字才是跨环境通用的。

##### 条件断点：只停你想要的那一次

右键断点，填一个布尔表达式，比如 <code class="inline">item.id === 100</code>。循环一千次只在第一百次停下来——没有这个功能，你只能握着 Resume 按一百次。条件里可以直接引用断点位置可见的变量，写错类型时断点图标会有提示，改了就好。

##### 日志断点：断而不停

断点设置里可以把"挂起"关掉、改成打印一个表达式：程序不停，断点位置像替你打了一行日志。高频路径（比如列表每行的渲染）想看值又不想把界面卡死，用它——比在代码里临时塞 console 打印干净，不用改源码，删的时候点掉断点就行。

##### 暂停现场的求值与观察

停在某一行时，用 Evaluate Expression 对任意变量求值，甚至现场试一行代码。修 bug 的正确姿势：先在暂停现场验证你的猜想，确认了再回去改代码——省掉一轮又一轮"改、跑、看"。Watch 窗口则把你关心的表达式钉在面板上，每次单步自动刷新，盯状态变化特别方便。

##### 真机、模拟器与无线调试

USB 真机：开发者选项开 USB 调试，插线后设备出现在 DevEco 的设备列表，点 Debug 直接跑。模拟器：不用插线，适合纯 UI 验证；涉及传感器、真机权限的行为，以真机为准。无线真机：手机开无线调试拿到 IP 和端口，电脑上 <code class="inline">hdc tconn</code> 连上后设备列表多一台——边充电边调试、线不够长时的解法，具体步骤见第五节。

##### 附加到进程

应用已经在跑（比如你从桌面图标点进去，复现了一个崩溃），别急着重启——用 IDE 的附加调试选中那个进程接着调，现场不丢。前提是这个应用是调试包；发布包附加不了，也别指望。

##### 断点排坑三条

断点图标变空心或打叉：源码跟跑的包不一致，先 Sync 再 Debug。断在一行但变量全是空：多半是异步还没返回，看调用栈理时序，别急着怪调试器。断点命中后界面像卡死：那是正常暂停，不是应用出问题，Resume 就走。

##### 调试 FAQ 四条

<strong>问：断点打上了但永远不停，是不是坏了？</strong>答：八成代码没编译进包——改完没构建、构建了没装到设备，都会这样。重新 Sync、重新 Debug，再看断点图标实不实。

<strong>问：模拟器能断点，真机不行？</strong>答：真机上装的可能是发布包（或旧的调试包），用调试构建重新安装再试。

<strong>问：一进 Debug 就停在一堆不是我想看的异常上？</strong>答：给真正的目标行设断点，其他异常先放行；或者干脆把断点改成条件断点，把"无关的停"过滤掉。

<strong>问：变量面板里全是占位或看不懂的东西？</strong>答：对象还没初始化或类型被裁剪了，用求值表达式单独看某个字段，比翻整个对象树快。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hand-pointer mr-2"></i>来动手

{class="mt-1"}
给列表渲染埋一个条件断点（条件写 index === 5），再给同一行配一个日志断点，各跑一次——体会"停"与"不停"两种玩法的区别，以后按需选。
:::

#### 八、性能优化速查

性能问题的正确处理顺序：先测量、再归因、后优化——Profiler 就是测量环节的工具。这节先认面板，再给一张"症状-根因-修法"对照表，末尾是两个完整的小案例。

##### Profiler 面板地图

入口在 DevEco 底部工具栏或菜单里的 Profiler（不同版本入口位置略有差异）。连上设备跑起来，录制一段操作，各面板分工如下：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">面板</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">看什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">对应的典型问题</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">CPU</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">占用曲线与调用栈</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">谁在吃 CPU、卡在哪个函数</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memory</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">内存趋势、快照对比</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">有没有只涨不跌的泄漏</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Frame</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">帧率曲线与丢帧位置</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">滑动掉帧、动画卡顿</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Startup</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">启动耗时分解</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">首页为什么这么慢</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Trace 打点</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">函数级耗时</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">疑点函数到底花多久</td></tr>
</tbody>
</table>
```
:::

用法要点只有一条：录两段对比——改之前一段、改之后一段，操作路径完全相同。数据说话，别凭"感觉快了"。

##### 症状-根因-修法对照表

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">症状</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">多半是</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">修法</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">滑动列表掉帧</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每次滚动全量重建组件</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">LazyForEach + 稳定 key，能复用的组件复用</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">首页转圈久</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">aboutToAppear 里干重活（同步 IO、大循环）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">重活挪到 TaskPool / Worker，界面先出骨架</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">越用越卡、内存只涨</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">监听器、定时器没注销；闭包持有大对象</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">页面 aboutToDisappear 里统一清理</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">图片一多就卡</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">原图直出，解码内存爆炸</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">按显示尺寸加载，列表外的原图不进内存</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">点按响应慢</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">主线程同步 IO</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数据库与文件操作异步化</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">改一个值整页重绘</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">状态粒度太粗</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">拆小组件、缩小状态范围（V2 用 @Trace 精确追踪）</td></tr>
</tbody>
</table>
```
:::

##### 案例一：首页启动慢

1. Startup 面板录一次冷启动，看耗时都花在哪些段。
2. 发现大头在页面初始化——aboutToAppear 里同步读了一遍数据库，还做了两张大表的遍历。
3. 把读库改成异步，首屏只渲染骨架加前几条，剩下的数据回来再补。
4. 同一操作再录一次，对比两段的启动耗时，确认改善幅度。
5. 把改动前的数据记下来——下次有人说"首页变慢了"，你有基线可查。

##### 案例二：列表滑动掉帧

Frame 面板录制滑动，看到丢帧集中出现在列表项进入屏幕的时刻——典型的全量重建。检查代码发现用的是 ForEach 且没给稳定的 key，每个列表项里还有一张原图直出。修法：换 LazyForEach、给每项稳定 key、图片按显示尺寸加载。改完再录一段，丢帧点基本消失。整个过程没改任何业务逻辑——性能优化经常就是这样，找对地方比大力出奇迹重要。

##### 两条心法

优化前先量化：没测过基线，你不知道改没改对。一次只改一处：同时改三处，好了不知道谢谁，坏了不知道怨谁。

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>避坑提醒

{class="mt-1"}
别上来就"优化"。先用 Frame 确认真掉帧，再用 CPU 面板归因——很多"我觉得卡"其实是动效预期错位，改代码反而帮倒忙。
:::

#### 九、签名与发布命令速查

发布环节要记的就三样：签名三件套、构建命令、上架清单。这节按"调试能跑 → 发布能上"的顺序排，每一步只讲你动手要敲的东西。

##### 签名三件套

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">文件</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">是什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">从哪来</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">.p12</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">密钥库，存私钥</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">本地生成，IDE 可以代劳</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">.cer</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数字证书，证明"你是你"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AGC（AppGallery Connect）申请</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">.p7b</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Profile 描述文件，限定应用与权限，有有效期</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AGC 创建</td></tr>
</tbody>
</table>
```
:::

调试签名不用管：DevEco 登录账号后自动生成调试用的三件套。发布签名必须手动来：去 AGC 生成发布证书与发布 Profile，再在项目里配置——拿调试签名去上架会被拒，这是新手最常见的第一次投稿失败原因。

##### 调试签名与发布签名的差异

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">维度</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">调试签名</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">发布签名</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">来源</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">IDE 自动生成</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AGC 手动申请与配置</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用途</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">开发自装自测</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">上架 AppGallery</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">有效期</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">较短，过期重新生成</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Profile 有有效期，到期在 AGC 续</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">与密钥的关系</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">丢了就重新生成</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">与应用绑定，务必备份</td></tr>
</tbody>
</table>
```
:::

##### 配置长什么样

签名信息在 build-profile.json5 的 signingConfigs 里，示意如下（路径与密码以你自己生成的为准）：

::: div .code-block
:::inline div .code-head
<span>JSON5 · build-profile.json5（示意）</span><span class="dots">···</span>
:::

```
"signingConfigs": [
  {
    "name": "release",
    "material": {
      "storeFile": "xxx.p12",
      "storePassword": "****",
      "keyAlias": "xxx",
      "keyPassword": "****",
      "certpath": "xxx.cer",
      "profile": "xxx.p7b",
      "signAlg": "SHA256withECDSA"
    }
  }
]
```
:::

字段名以你生成签名材料时的实际文件为准；这份配置里含密码相关内容，别提交进公共仓库——密钥与密码泄露，等于应用的身份被人拿走。

##### 构建命令

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">命令 / 入口</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">说明</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hvigorw clean</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">清理构建产物；"莫名其妙的编译错误"先跑它</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hvigorw assembleHap</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">命令行打 HAP 包的主力命令，更多参数看官方构建文档</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">IDE 菜单 Build &gt; Build App(s)/Hap(s)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">图形界面打包；上架选 Build App(s) 生成 .app</td></tr>
</tbody>
</table>
```
:::

包的分工一句话：HAP 用于调试与分发，.app 是上架 AppGallery 的完整包。版本号在 AppScope 的 app.json5 里改，上架前确认 versionCode 比线上版本大——不然商店不收。

##### 上架前清单

- <strong>版本号</strong>：versionCode 递增，versionName 规整。
- <strong>签名</strong>：用发布签名构建，不是调试签名。
- <strong>Profile</strong>：在有效期内；申请的权限与代码实际用的一致，多申请会被问。
- <strong>物料</strong>：图标、名称、隐私声明齐全，截图按商店要求准备。
- <strong>回归</strong>：真机全流程走一遍——安装、登录、核心功能，涉及支付的多走两遍。

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>避坑提醒

{class="mt-1"}
.p12 和密码别进代码仓库；发布密钥丢了，已有应用的更新会非常麻烦。备份到安全的地方（加密盘、密码管理器），并且确认备份能恢复——备份打不开等于没备份。
:::

#### 十、ArkTS 语言规则速查

从 TS 转过来的第一天，编译器会连着给你几记闷棍——那不是 bug，是 ArkTS 故意收紧的规则。这节把最常见的六条与修法列成表，报错时对着查。

为什么收紧？一句话：ArkTS 要做静态编译优化，界面才跑得快。动态特性省下的编写时间，会加倍还到运行性能上。习惯了"随便写随便跑"的人会觉得别扭，两周后你会发现——类型写清楚，bug 反而少了。

##### 六条规则与修法

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">规则</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">原写法（不行）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ArkTS 写法</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">禁 any / unknown 兜底</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">let v: any = getData()</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">给具体类型或联合类型</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">对象字面量必须带类型</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">let u = { name: 'x' }</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">先声明 interface User { name: string }，再 let u: User = ...</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">属性运行期冻结</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">delete obj.key、随手加新属性</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可选属性置 undefined；动态键改用 Map</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">类不做结构化互认</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">字段一样的两个类直接互赋</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">抽共同接口，按接口类型传值</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">运算符语义收紧</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一元 + 拼数字、用 in 探测属性</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">显式数值转换、明确的类型判断</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">只抛 Error</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">throw 'something wrong'</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">throw new Error('something wrong')</td></tr>
</tbody>
</table>
```
:::

##### 顺手记的对照清单

- <strong>var 不用</strong>：let / const 顶上。
- <strong>返回类型补全</strong>：函数写明返回类型，回调参数标类型——IDE 的黄色波浪线消掉，编译器也不再猜。
- <strong>动态键访问</strong>：拿字符串变量当属性名查对象，换成 Map，或用声明了键值类型的 Record。
- <strong>匿名函数里少用 this</strong>：语义不稳，能用箭头函数就用箭头函数。

##### 报错信息反查

ArkTS 的规则报错常带 arkts-no-xxx 这样的编号。最高效的排查法：直接拿编号搜官方的《TypeScript 到 ArkTS 迁移指南》，对应条目里有正反例代码。别拿报错全文去搜博客——博客的修法可能基于旧版本，官方指南才是当前有效的。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">报错关键词</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">一步修法</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">arkts-no-any</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">给变量、参数、返回值标具体类型</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">arkts-no-untyped-obj-literals</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">声明 interface 或 class，再写字面量</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">arkts-no-delete</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可选属性赋 undefined，或改用 Map</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">arkts-no-structural-identity</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">提取接口，按接口约束两个类</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">arkts-no-throw-literals</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">改成 throw new Error(...)</td></tr>
</tbody>
</table>
```
:::

##### 迁移老代码的自查清单

- 全项目搜一遍 any 和 unknown，逐个换成具体类型。
- 搜"对象字面量赋值给无类型变量"——都是等着报错的地方。
- 搜 delete 与运行时加属性的写法，改可选属性或 Map。
- 搜 throw 后面不是 new Error 的，全改。
- 改完跑一次构建，把报错里的 arkts 编号抄成清单，按编号批量收尾。

::: div .tip-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2" aria-hidden="true"></i>小贴士

{class="mt-1"}
迁移老 TS 代码时，先跑一遍编译器把所有 arkts 编号抄下来，按编号批量修——比逐行猜快得多，也比"感觉上改完了"可靠得多。
:::

#### 十一、三平台 API 对照大表

迁移期最花时间的不是思路，是名词翻译。五张表按主题对照：生命周期、权限、存储、网络、UI，最后附一张异步与并发的加餐表。用法是"我要做某事 → 查行 → 找到三方名字"，不是背表。

两个提醒：框架演进快，表里的 API 名称以各家当前文档为准——概念映射是稳定的，具体名字可能微调；同一概念在不同平台有语义细节差异（比如"后台"的定义各家不一），写代码前到对应文档确认行为。

##### 生命周期（应用级）

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">概念</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Android（Activity）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">iOS（SwiftUI 为主）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">HarmonyOS（UIAbility）</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">首次创建</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onCreate</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">scenePhase 首次变为 active</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onCreate</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">进入可交互</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onResume</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">scenePhase 变为 active</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onWindowStageCreate / onForeground</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">退到后台</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStop</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">scenePhase 变为 background</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onBackground</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">回前台</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onRestart / onResume</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">回到 active</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onForeground</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">销毁</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onDestroy</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">（UIKit）applicationWillTerminate</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onWindowStageDestroy / onDestroy</td></tr>
</tbody>
</table>
```
:::

鸿蒙比两家多一层"页面级"生命周期：aboutToAppear、onPageShow、onPageHide、aboutToDisappear——感觉上接近安卓里 Fragment 的那套钩子。页面级管 UI 状态，Ability 级管应用状态，别混着用。

##### 权限

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">概念</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Android</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">iOS</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">HarmonyOS</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">静态声明</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AndroidManifest.xml</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Info.plist（写用途说明）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">module.json5 的 requestPermissions</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">运行时申请</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">requestPermissions()</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">直接调对应系统能力，系统弹窗</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">requestPermissionsFromUser()</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">查询授权状态</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">checkSelfPermission</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">各框架各自提供的状态查询</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">权限管理器（abilityAccessCtrl）查询</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">特殊权限</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">部分需特殊声明与审核</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">部分用途需说明理由</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">少数受限权限走额外申请（ACL）</td></tr>
</tbody>
</table>
```
:::

##### 存储

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">概念</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Android</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">iOS</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">HarmonyOS</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">键值小配置</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SharedPreferences</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Preferences</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">关系型数据库</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room（SQLite）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Core Data</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">RelationalStore（SQLite）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">文件读写</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">File API + SAF</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">FileManager</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">fs 模块（应用沙箱目录）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跨应用拿文件</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">FileProvider / 系统选择器</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">沙箱 + 系统 Picker</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系统 Picker（照片、文件）</td></tr>
</tbody>
</table>
```
:::

##### 网络

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">概念</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Android</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">iOS</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">HarmonyOS</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">HTTP 请求</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OkHttp / Retrofit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">NetworkKit 的 http</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">WebSocket</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OkHttp 的 WebSocket</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSessionWebSocketTask</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">NetworkKit 的 webSocket</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">明文 HTTP</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">默认受限，配置例外</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ATS 限制，配置例外</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">相关权限与配置，以文档为准</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">网络权限</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Manifest 声明 INTERNET</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">无需声明（内容受 ATS 管）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">module.json5 声明 ohos.permission.INTERNET</td></tr>
</tbody>
</table>
```
:::

##### UI 与状态

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">概念</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Android</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">iOS</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">HarmonyOS</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">声明式框架</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jetpack Compose</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ArkUI（ArkTS）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">组件自有状态</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">mutableStateOf</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State（V1）/ @Local（V2）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">父传子</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">参数 + 状态提升</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Binding / init 参数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Prop（V1）/ @Param（V2）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">列表</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">LazyColumn</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List / LazyVStack</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List + LazyForEach</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">导航</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Navigation Compose</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">NavigationStack</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Navigation 组件（router 为旧方案）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">弹窗</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dialog</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Alert / Sheet</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AlertDialog / CustomDialog</td></tr>
</tbody>
</table>
```
:::

##### 加餐：异步与并发

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">概念</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Android</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">iOS</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">HarmonyOS</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">异步写法</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin 协程（suspend）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">async / await</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">async / await</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">后台并发</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">协程 + 线程池</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GCD</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TaskPool / Worker</td></tr>
</tbody>
</table>
```
:::

用表的正确姿势：迁移某个功能时按行查，查完去对应平台文档确认签名与行为——表是"翻译词典"，不是使用说明书。翻译完名词，思路你早就有了。

#### 十二、学习资源与社区导航

第三节给的是资源名单，这一节给"每个资源怎么用"。同一份资源，用法的差距能到几倍——文档当小说读是浪费，Samples 只收藏不运行也是浪费。

##### 文档的四层读法

- <strong>指南</strong>：按 Kit 通读一遍，建立地图——第一遍别跳读，跳过的地方以后都会变成坑。
- <strong>API 参考</strong>：当字典查，别当书读；查的时候连参数说明一起看，别只看函数名。
- <strong>Best Practice</strong>：场景手册，遇到对应场景再读，结构可以整段抄。
- <strong>版本说明</strong>：升级前必读，行为变更都藏在这里——很多人升级后"代码没改却坏了"，答案就在这份文档里。

##### Samples 的三步用法

只看不跑等于白看。正确顺序：导入跑起来（先看到效果，确认环境没问题）→ 拆代码（找到最小实现，删掉示例里的干扰项）→ 改成你的需求（搬运完成）。一个 Sample 按这三步走完，对应的 Kit 你就算上手了——比看三个视频快。

##### 视频的正确时机

入门期看视频效率高：有人带着走，少踩环境坑。进阶后别再依赖视频——信息密度太低，同一个问题文字文档十分钟讲完，视频要半小时。官方开发者网站有视频中心，社区平台（视频站、博客站）也有大量课程。看的时候认准发布日期：鸿蒙一年一大版，半年前的视频随时可能过时，重点看操作路径是否还一致。

##### 论坛发帖的礼仪与技巧

- <strong>标题带关键报错行</strong>：别写"求助！大佬进"，直接写报错核心词，懂的人一眼判断能不能答。
- <strong>正文带环境</strong>：IDE 版本、API 版本、真机还是模拟器——很多问题是版本错配，没这些信息猜都没法猜。
- <strong>贴最小复现代码</strong>：删到只剩报错那二十行。贴整个项目没人看。
- <strong>说明你试过什么</strong>：避免收到"你先搜一下"式的回复，也帮回答者少绕路。

渠道优先级照旧：官方论坛（华为工程师会回）→ 社区专区（51CTO 鸿蒙板块等）→ 博客搜索。文档页还有反馈入口，文档写错了也能报——报了真有人处理，你自己也会被通知。

##### 认证怎么用

基础版免费，当学习验收：觉得基本掌握了再去做，重点在备考过程把散落的知识点串成体系，证书本身是副产品。进阶版付费，求职时是简历上的加分项。备考方式：对照官方考纲逐项自查，不会的回到对应 Kit 的文档和本书相关章节补——认证是学习的收口动作，别为考证而考证，也别什么都不做只收藏资源。

##### 一条学习路线建议

入门：官方指南按 Kit 通读，同时跟着 Sample 抄——动手比例保持在七成。练手：自己选一个小应用（记账、倒计时、天气都行）从头做一遍，遇到问题按求助优先级查。进阶：读 Best Practice，把 API 参考当字典精查，开始关心性能与包体。收口：做一遍认证题自查，查漏补缺。每个阶段的时间长短因人而异，判断标准很简单——下一个阶段的问题你问得出来了，就说明该进下一个阶段了。

##### 搜索的两个技巧

报错先搜 arkts-xxx 规则编号（见第十节），再搜报错文本——编号直接对应官方指南条目，命中率最高。中文教程认日期与版本号：一年一大版的节奏下，半年前的教程随时可能过时，多源交叉验证，别把单一来源当真理。

#### 十三、常见问题速查（环境 10 条）

最后一节是"急救卡"：10 条最常见环境问题，每条一句解法。你以为是代码问题的，十有八九其实在这张表里。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">现象</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">一句解法</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">'hdc' 不是内部或外部命令</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把 SDK 的 toolchains 目录加进 PATH，重开终端再试</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc list targets 是空列表</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">换一根支持数据传输的线、开发者选项里开 USB 调试、手机弹授权点允许</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">命令作用到了错的设备</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多设备时每条命令前加 -t 设备key</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc 报端口占用或状态诡异</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc kill 再 hdc start，重启本机服务</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">模拟器起不来</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BIOS 里开虚拟化，再按官方模拟器文档核对系统设置</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">预览器白屏或报不支持</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">预览器只渲染部分特性，换模拟器或真机验证</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">构建卡在下载依赖</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">查网络与代理配置，清理缓存后重新 Sync</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">升级 IDE 后满屏报错</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跑 API Change Assistant，按版本说明逐条改</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真机安装失败提示签名问题</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">确认账号已登录，重新构建生成调试签名，必要时先卸载旧包</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">项目各种玄学报错</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把项目挪到纯英文、无空格的路径，多半就好了</td></tr>
</tbody>
</table>
```
:::

排除顺序口诀：先环境后代码。代码没改过的前提下突然出错，九成是环境——先查这张表，再怀疑自己的代码。表里没覆盖的问题，回到第一节的求助优先级链：官方文档、官方论坛、社区、AI 助手，从可靠到快捷逐级试。

这张表会过时，排查思路不会：报错信息逐字读、环境版本逐项核、改动逐步回退——任何工具链的问题，最终都能被这三板斧定位。环境之外的问题也别慌，后面几节把工程文件、组件布局、数据场景各自的"急救卡"也备齐了。

#### 十四、工程结构文件速查

新项目打开就懵：一串 json5 文件谁管谁？这节按文件讲，每个文件给一句话定位，再给一张"我想改 X 该去哪个文件"的速对表。工程文件是配置不是代码——改错位置不会报错，只会"没生效"，那才是最气人的事故。

##### 文件定位总表

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">文件 / 目录</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">管什么</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AppScope/app.json5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全局应用信息：包名（bundleName）、版本号（versionCode / versionName）、应用图标与名称</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AppScope/resources</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全局资源：应用级图标与标签字符串</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">build-profile.json5（工程根目录）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">构建总配置：SDK 版本坐标、签名（signingConfigs）、产品（product）定义</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">oh-package.json5（工程根目录）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">依赖声明：三方库与模块间依赖，加完要 Sync</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">entry/src/main/module.json5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">模块配置：Ability 声明、权限（requestPermissions）、入口设置</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">entry/src/main/ets</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">代码本体：pages 页面、components 组件、model 数据结构</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">entry/src/main/resources</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">模块资源：图片、字符串、颜色，分 base 与限定词目录</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">resources/base/profile</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">路由等配置文件所在（main_pages.json 在这里，页面要注册进去才能跳）</td></tr>
</tbody>
</table>
```
:::

三个方向记牢：改版本号去 app.json5，加权限去 module.json5，升 API 或配签名去根目录的 build-profile.json5。"我明明改了怎么没生效"的事故，一半是改错了文件——另一个常见版本是改了模块级的 oh-package.json5，而依赖其实声明在工程根级。

##### 我想改 X，该去哪个文件

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">想做的事</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">去哪改</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">改应用版本号</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AppScope/app.json5 的 versionCode / versionName</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">升级 API 版本</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">根目录 build-profile.json5 的 SDK 版本字段</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新增一个权限</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">entry 的 module.json5，往 requestPermissions 里加</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">引入三方库</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">oh-package.json5 加依赖，然后 Sync</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新增页面并让它可跳转</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">pages 下建文件，再到 main_pages.json 注册</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">改应用名称</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AppScope 里的字符串资源（应用标签），多语言与深浅色目录记得一起看</td></tr>
</tbody>
</table>
```
:::

##### resources 的匹配规则

base 是默认值；语言、深浅色等限定词目录在设备命中条件时覆盖 base。真机上改的字符串没生效，先看是不是改了 base 而设备命中了别的限定词目录，或者反过来——你改的是某个限定词，测试机根本不在那个限定范围里。

##### 别手改的两类东西

build 产物目录与各类构建缓存都是生成物：手改无用，下次构建直接覆盖。编译报"文件不存在"时也去 clean 重建，别钻进产物目录里找文件——你找到的也只是上一轮的遗物。

::: div .tip-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2" aria-hidden="true"></i>小贴士

{class="mt-1"}
接手别人的项目，第一件事把 app.json5、根 build-profile.json5、module.json5 各读一遍——三个文件读完，这个项目的版本、签名、权限、入口你就全知道了。
:::

#### 十五、UI 组件与布局速查

写界面忘了组件名，谁都有过。两张表解围：组件一句话表、布局选择表。组件的完整属性永远以官方 API 参考为准，这里只管一件事——让你想起"该用哪个"。

##### 组件一句话表

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">组件</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">一句话</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Column / Row</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">纵向 / 横向排列子组件，九成布局由它俩完成</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stack</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">层叠：图上压字、角标、浮层</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Flex</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">弹性布局；大多数场景 Column / Row 已够用</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Scroll</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">内容超出屏幕时的滚动容器</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">长列表，配 LazyForEach 用（性能见第八节）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Grid</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">宫格：相册、九宫格菜单</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swiper</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">轮播图与横滑翻页</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tabs</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">页签切换（顶部或底部）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text / TextInput / TextArea</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">文本显示 / 单行输入 / 多行输入</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button / Toggle</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">按钮 / 开关</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">图片，记得约束尺寸与填充方式</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Video</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">视频播放</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Refresh</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">下拉刷新容器</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AlertDialog / CustomDialog</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">确认弹窗 / 自定义弹窗</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">半模态面板（Sheet 类）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">从底部滑出的面板，比整页跳转轻</td></tr>
</tbody>
</table>
```
:::

##### 布局选择表

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">需求</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">用什么</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">上下排列</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Column</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">左右排列</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Row</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">叠放</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stack</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">大量数据滑动</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List + LazyForEach</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">宫格</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Grid</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">页签加内容区</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tabs</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">局部滚动</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Scroll</td></tr>
</tbody>
</table>
```
:::

对齐与分布用 justifyContent（主轴）与 alignItems（交叉轴）——记不清方向没关系，写个小例子进预览器看一眼，比背文档快。布局嵌套别超过两三层，深了先想合并；嵌套过深本身就是掉帧来源之一（见第八节）。

##### 新手 UI 三问

<strong>问：组件死活不显示？</strong>答：先查尺寸——很多容器组件不给宽高就是零大小，界面上自然"消失"。给个固定尺寸确认是不是这个问题，再回头改约束。

<strong>问：怎么都对不齐？</strong>答：主轴和交叉轴搞反了。Column 的主轴是竖直方向，Row 的是水平方向；换一个属性试试，立刻见分晓。

<strong>问：图片变形了？</strong>答：填充方式没设。Image 的 objectFit 属性管"按比例裁还是拉伸"，选覆盖就用裁切类取值，别让原图硬挤进不匹配的框。

##### 深浅色与多设备

颜色写进资源而不是硬编码，深色模式才有得切；尺寸用 vp / fp 这类相对单位，别拿像素硬怼。适配的验收标准：预览器多档尺寸过一遍、真机过一遍——两处都体面才算完成。深浅色切换的验收动作就一个：系统里切一下主题，回到应用看有没有"惨白"或"死黑"的角落。

::: div .tip-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2" aria-hidden="true"></i>小贴士

{class="mt-1"}
不确定组件长什么样时，去官方 Samples 按组件搜，几乎每个常用组件都有能跑的示例——按第十二节的三步用法处理，半天就能上手一组组件。
:::

#### 十六、网络与数据场景速查

数据层就三个问题：请求怎么发、数据往哪存、出错怎么办。这节给最小可用代码和方案选择表——细节回对应 Kit 的文档查，这里只管"照抄就能跑、选型不纠结"。

##### 发一个请求（最小可用）

::: div .code-block
:::inline div .code-head
<span>ARKTS · 网络请求最小示例</span><span class="dots">···</span>
:::

```
import { http } from '@kit.NetworkKit';

let client = http.createHttp();
let resp = await client.request('https://example.com/api/list',
  { method: http.RequestMethod.GET, expectDataType: http.HttpDataType.OBJECT });
client.destroy();
```
:::

三件事别忘：destroy 释放连接（不释放，请求一多就拖垮自己）；超时给默认值，别默认无限等；返回码先看再解析——状态不对时解析出的"数据"只会把你引向歧途。expectDataType 决定返回按对象还是字符串处理，按接口实际给。

##### 请求封装四条建议

- <strong>统一超时与错误码处理</strong>：别每个页面各写一套判断，写三遍之后你就不想改了。
- <strong>统一打日志</strong>：Tag 按第六节的规范，出问题一筛到底。
- <strong>重试放封装层</strong>：页面只关心成功与失败两态，重试细节别泄漏到界面代码里。
- <strong>base 地址走配置</strong>：切测试环境改一行，而不是全局翻代码。

##### 存数据的方案选择

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">场景</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">用什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">提醒</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">设置项、开关、上次浏览位置</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Preferences</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">键值对，别往里塞大对象</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">结构化数据、要条件查询</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">RelationalStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">底下是 SQLite，建表想清楚再动手</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">文件、图片缓存</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">fs 模块</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">放应用沙箱目录，配好清理策略</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">拿别的应用里的东西</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系统 Picker</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">沙箱绕不过去，也不该绕</td></tr>
</tbody>
</table>
```
:::

方案怎么选只看一个问题：数据长什么样、要不要查询。键值小配置选 Preferences，要查询选 RelationalStore，大块二进制选文件，跨应用一律走系统 Picker。拿不准就从小方案开始——小方案升级成大方案容易，反过来难受。

数据库与文件操作别忘了异步化：主线程上做同步 IO，点按响应立刻变肉（症状与修法见第八节的对照表）。

##### 错误处理清单

- <strong>区分"没网"和"服务端出错"</strong>：提示语不同，重试策略也不同——没网重试是白费，服务端 5xx 重试才有意义。
- <strong>超时要有明确反馈</strong>：别让用户对着无限转圈，给"加载失败，点此重试"。
- <strong>解析失败要兜底</strong>：服务端改了返回结构，客户端不该崩，该给空态加日志。
- <strong>空数据是正常态</strong>：空列表给空态页，别白屏（排查路径见第十九节）。

#### 十七、DevEco Studio 效率速查

工具用得顺，一天能省出半小时。这节全是小技巧，每条半分钟学会；键位一律以 IDE 的 Keymap 设置为准——名字记住了，键位随时能查。

##### 十个最值回票价的功能

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">功能</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">用法</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">什么时候用</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Find in Files</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全工程搜文本</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">搜报错词、搜资源名</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Replace in Files</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全工程替换</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">批量改统一前缀的命名</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">重构重命名</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">光标放符号上，Refactor &gt; Rename</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">引用一起改，比手搜安全十倍</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跳到定义</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">点击符号</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">看系统组件与 API 的签名</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Reformat Code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一键格式化</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">提交前统一风格</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Live Templates</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">输缩写展开代码块</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">高频片段做成自定义模板</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">剪贴板历史</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多份粘贴记录可回选</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">从多处抄代码拼装时</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">内置 Git 面板</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">diff、提交、回滚</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不用切出去敲命令</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">断点管理面板</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">批量启用 / 禁用断点</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">调完一轮关一批</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">结构面板</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">看当前文件的结构大纲</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">长文件里找段落</td></tr>
</tbody>
</table>
```
:::

##### 三处设置值得先调

- <strong>Keymap</strong>：按你顺手的风格选，IDEA 系、VSCode 系都支持——团队里键位统一，互帮时少一句"你的快捷键是什么"。
- <strong>编辑器字体字号</strong>：别为了塞下更多代码把字调太小，眼睛是长期成本。
- <strong>自动导入与保存时格式化</strong>：按习惯开；开了就别关，规则一致比规则多更重要。

##### Run、Debug、Profiler 别混用

三个启动方式干三件事：Run 只跑；Debug 支持断点；Profiler 带性能采集。测性能必须从 Profiler 启动——普通 Run 下测出来的数据不作数，因为采集开关根本没开。反过来，日常开发用 Profiler 启动又白白变慢。三个入口各干各的活，混着用只会得出错误结论。

#### 十八、模拟器与真机速查

什么时候用模拟器、什么时候必须真机？一句话：迭代快慢用模拟器，数据真假看真机。

##### 差异对照

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">维度</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">模拟器</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">真机</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">启动与切换</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">已开着时秒切</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">插线即用，安装要稍等</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">传感器、相机、指纹</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">模拟或缺失</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真实行为</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">性能表现</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">仅作参考</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">唯一可信来源</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">权限弹窗</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">模拟流程</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真实流程</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定位</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可设固定坐标，方便测"人在外地"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真实或模拟注入</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">网络环境</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跟着电脑走</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用户真实网络（弱网、切网）</td></tr>
</tbody>
</table>
```
:::

回归规则：发版前所有核心流程在真机过一遍——性能、权限、后台行为这三类，模拟器都可能骗你。日常写 UI、调流程，放心用模拟器与预览器，快就是生产力。

##### 真机调试的三个前提

- 开发者选项与 USB 调试已打开（首次开启路径视机型而定，一般在"关于"里连点版本号解锁）。
- 数据线支持数据传输——只充电的线插上没反应，换了三根才好使是经典剧情。
- 手机上的授权弹窗点了允许；拒绝过的，去开发者选项里撤销授权重来。

##### 模拟器三件小事

- 开关机与实例管理在 Device Manager 里；它占资源大，同时开一个就好。
- 端口冲突或状态卡死：关掉实例重开，还不行就删实例重建。
- 模拟器上测出来的帧率别当真——它的渲染路径跟真机不同，掉帧结论只在真机上下。

#### 十九、闪退与白屏排查路径

闪退与白屏是两大"天塌了"现象。各给一条固定排查路径，照着走，不靠灵感。

##### 闪退五步

1. DevEco Log 里按你的进程过滤，先找 FATAL 与 ERROR——崩溃栈就在这附近。
2. 看栈里的文件名与行号，直接跳到现场；一长串系统栈里，看最后一段自己代码出现的位置。
3. 判断必现还是偶发：连着复现三次，全中算必现。
4. 必现的上断点（第七节）；偶发的按第六节埋日志，等它下次再来。
5. 修完把崩溃栈与原因记进清单——同类问题第二次出现时，你五分钟就能定位。

##### 白屏五步

1. 先分清"页面开了但空白"还是"根本没跳过去"——看跳转与路由日志。
2. 页面开了但空白：多半是异步数据没回来又没兜底——加加载态与空态。
3. 看渲染相关报错：组件参数不合法有时被静默忽略，界面上就是缺一块。
4. 检查资源：深色模式、多语言限定词目录缺文件，界面就是"消失"。
5. 换真机验证一次，排除预览器与模拟器的特性差异。

顺手记一个近亲现象：应用卡住不响应但没退——那是"无响应"而不是闪退，看 Trace 找主线程被什么占住了，排查入口与闪退不同。

##### 通用原则

改动一步一验证：连改三处再跑，出了问题你不知道是谁干的。三把钥匙的顺序：先日志看现象（第六节），再断点看现场（第七节），最后才是 Profiler（第八节）——顺着来，别倒着来。代码之外的问题，接下来几节接着盘。

#### 二十、Kit 与系统能力扩展速查

第二节那张表只列了最常用的几个 Kit，这一节把"手机上那些系统能力"补齐成一张全表：用哪个能力引哪个 Kit，一行一个。引入方式统一是 <code class="inline">import ... from '@kit.对应Kit'</code>，写代码时 IDE 会自动补全。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kit</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">干什么</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Notification Kit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">发本地通知：提醒、进度、消息都在通知栏</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Background Tasks Kit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">后台任务：短任务、长时任务、延迟任务的申请</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Location Kit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定位与逆地理编码</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Map Kit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">地图显示、地点检索、路径规划</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Scan Kit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">扫码：识别码图，也能生成码图</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Push Kit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">服务端推送消息到设备</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Account Kit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">华为账号登录</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">IAP Kit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">应用内购买与支付</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Media Library Kit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">相册：选照片、保存图片</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AVSession Kit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">媒体播放接入锁屏与控制中心</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sensor Kit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">传感器：加速度计、陀螺仪等</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bluetooth Kit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">蓝牙扫描、连接、传输</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Calendar Kit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">日历事件读写</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Contact Kit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">通讯录读写</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ArkWeb（Web 组件）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">应用内嵌网页</td></tr>
</tbody>
</table>
```
:::

三条使用规则：规则一，不用的 Kit 别引——包体与启动时间都会感谢你（思路见第二节）；规则二，不少 Kit 自带权限要求，引入前先看该 Kit 文档的权限说明，再到 module.json5 声明（文件位置见第十四节）；规则三，Kit 文档里的"约束与限制"区块必读——大多数"代码没毛病但被系统拦下"的问题，答案就写在里面。

##### 后台任务速对

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">需求</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">走哪条路</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">音乐、导航等持续后台行为</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">长时任务，声明对应类型</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">大文件下载、不着急的同步</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">延迟任务，系统择机执行</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">退出页面前几秒的收尾</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">短任务</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定时提醒类需求</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">延迟任务或通知，视精度要求</td></tr>
</tbody>
</table>
```
:::

后台的心法一句话：别惦记"常驻"，系统不答应——想清楚你的功能到底需要哪种"还在干活"，按类型申请，按约束收尾。申请的类型与实际行为不符，是后台任务被系统中途掐掉的头号原因。

##### 通知三句话

通知先过授权关：用户可以在系统设置里关掉你的通知，发之前查授权，被关了就引导用户去开。普通文本通知一行代码的事；进度条、大文本、折叠样式去官方文档抄示例，别自己造。频次克制——一天弹七八条的应用，离被静音只差一次更新。

推送（Push Kit）与本地通知是两回事：本地通知是你的应用自己发的，推送是服务端经由系统通道送到设备的。接推送要配服务端，工程量另算——需求里写"发个通知"时，先问清楚到底是哪一种。

##### 三问排坑

<strong>问：通知发不出来？</strong>答：授权没开或渠道受限，先查授权状态，再看 Kit 的约束说明。

<strong>问：后台任务干着干着被杀？</strong>答：长时任务类型没声明，或声明的类型跟实际行为对不上，系统按违规处理。

<strong>问：定位拿不到？</strong>答：权限声明的精度与 API 要求不匹配，或用户只给了"仅使用期间"——两种情况都做降级处理。

<strong>问：模拟器上好好的，真机上不行？</strong>答：系统能力类功能（通知、后台、支付、扫码）一律真机验证——模拟器的模拟程度不一，这类结论只在真机上下（详见第十八节）。

::: div .tip-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2" aria-hidden="true"></i>小贴士

{class="mt-1"}
引入新 Kit 的固定动作四连——读指南、看约束、声明权限、真机验证。四步走完再写业务代码，返工最少。
:::

#### 二十一、安全与隐私速查

隐私合规三问：这个数据必须收吗？用户知道吗？存得安全吗？三问过不了，功能再炫也不做。这节把日常开发里跟安全沾边的事收成一张表，配上红线、误区和上架清单。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">场景</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要点</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">权限申请</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最小够用；用途说明写人话；被拒绝后给降级体验而不是白屏</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">敏感数据落盘</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不明文写文件；用系统提供的安全存储能力，具体 API 以官方安全文档为准</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">网络传输</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全程 HTTPS；别为绕过校验去关证书验证</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">日志</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">姓名、手机号、token 不进日志；private 标注不是保险箱（见第六节）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">剪贴板</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">敏感内容用完即清，别长期滞留</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">三方库</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">引入前看它申请什么权限；能不给的不给</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">外部跳转</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">校验来源与参数，别让任意链接直通敏感页面</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数据删除</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">提供删除入口；注销账号就同步清数据</td></tr>
</tbody>
</table>
```
:::

##### 数据分级一分钟

给数据分四级管理：内部日志（出问题才看）、使用统计（不识别个人）、个人信息（能对上号）、敏感个人信息（身份证、健康、精确位置）——级别越高，收集门槛越高、存储越谨慎、展示越收敛。拿不准级别时往高的算：多管一格不亏，少管一炷香出事。

##### 三条红线

- <strong>用户没点头的数据不收</strong>——"默认勾选"不算点头，"继续使用视为同意"也不算。
- <strong>明文密码、token 不落盘、不进日志</strong>——内存里用完即弃。
- <strong>权限申请别捆绑</strong>——要定位就只申请定位，搭车申请会被问，也该被问。

##### 误区三条

以为调试包不合规没关系——调试期养成的坏习惯会原样带进发布。以为日志只在自己设备上——用户导出日志求助时，它就上路了。以为隐私声明抄模板就行——模板覆盖不了你的特殊权限，照实写才有说服力。

##### 被拒之后的降级体验

权限被拒绝不是终点。给一个"为什么需要 + 去开启"的引导，同时功能用降级方式跑着：手动选照片替代直接读相册，手动输入替代自动读取，模糊定位替代精确定位。被拒一次就摆烂罢工的应用，用户会连应用一起弃了。

##### 上架合规清单

- <strong>隐私声明与实际行为一致</strong>——审核的人会对照你的权限清单逐条看。
- <strong>每个权限写清用途</strong>——"为了改善体验"这种话等于没写。
- <strong>数据收集范围列清楚</strong>：收什么、存多久、给谁用。
- <strong>测试数据清理</strong>：别把测试账号里的真实信息带上线。
- <strong>地区差异</strong>：不同上架地区的合规要求以 AppGallery 上架规范为准，别只看一篇攻略。

##### 安全三问排坑

<strong>问：测试图方便用了真实用户数据，怎么办？</strong>答：上线前彻底清理测试数据；若已涉及真实用户信息，按你们的隐私事故流程处理——别抱着"就这一次"的心态。

<strong>问：怎么知道三方库干了什么？</strong>答：看它的权限申请与文档说明，有疑虑就在测试环境抓包看它请求了什么——来路不明的库别引。

<strong>问：应用沙箱已经隔离了，还需要管存储安全吗？</strong>答：沙箱隔离的是"别的应用"，挡不住设备丢失、备份导出这些场景——敏感数据按官方安全文档的能力来做。

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>避坑提醒

{class="mt-1"}
敏感信息进一次日志，就可能永远留在某次导出的文件里——打日志之前，回看第六节的规范清单，三秒钟的事。
:::

安全不是发布前补的作业，是写每一行代码时的默认姿势——凡是碰到用户数据的地方，把开头那三问再过一遍。

#### 二十二、术语中英对照速查

半夜读文档最烦"这词是啥"。这张对照表按主题排，行行一句话——读文档、看帖子、搜报错时遇到生词，先来这查一行，再决定要不要深入。英文词不用刻意背，见三次自然就记住了。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">术语</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">一句话</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stage 模型</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">当前应用框架的组织方式，UIAbility 是它的核心单元</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UIAbility</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">带界面的能力单元，应用的"门面"（生命周期见第十一节）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Page（页面）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可显示、可跳转的界面单位，有页面级生命周期</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ArkTS</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">应用开发语言，TypeScript 的收紧版（规则见第十节）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ArkUI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">声明式 UI 框架（组件速查见第十五节）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">HAP</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Harmony Ability Package，应用的安装单位</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">HAR</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Harmony Archive，静态共享包，编译期打进包里</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">HSP</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Harmony Shared Package，动态共享包，运行时共享</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">.app 包</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">上架 AppGallery 的完整包（见第九节）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hvigor / hvigorw</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">构建工具与其命令行入口（见第九节）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">HarmonyOS Device Connector，鸿蒙版 adb（手册见第五节）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">HiLog</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系统日志方案（详解见第六节）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Domain / Tag</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">日志的两个过滤维度：领域号与标签</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AGC</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AppGallery Connect，证书申请与发布后台</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Profile（.p7b）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">签名描述文件，限定应用与权限，有有效期</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ACL</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">受限权限的额外申请机制</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">沙箱</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">应用私有目录的隔离机制，别的应用进不来</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Picker</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系统提供的照片、文件选择器，跨应用取物的正道</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">服务卡片</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">桌面上的小卡片，Form Kit 负责</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">元服务</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">免安装的轻量服务形态，与应用并列</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一多</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一次开发、多端部署，一套代码适配多设备</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State / @Local</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">组件自有状态（V1 / V2 两代，见第二节）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Prop / @Param</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">父传子的单向输入（V1 / V2）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Link / @Event</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">V1 的父子双向绑定 / V2 的回调事件</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TaskPool / Worker</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">轻量任务池与独立线程，重活的去处（见第八节）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">LazyForEach</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">按需渲染的列表迭代，长列表标配</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DevEco Studio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方 IDE（效率技巧见第十七节）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API 版本</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系统能力版本坐标（版本表见第四节）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">版本三字段</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">compileSdkVersion 等，写在 build-profile.json5</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">冷启动</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">进程不存在时的启动，Startup 面板量它</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">丢帧 / 帧率</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UI 流畅度指标，Frame 面板量它</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">断点 / 条件断点</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">调试暂停点与带条件的暂停点（玩法见第七节）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">覆盖安装</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc install -r，调试期最常用的安装方式</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">权限弹窗</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系统统一的授权弹窗，触发时机由你的申请代码决定</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">增量 / 全量构建</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">增量只编译改动部分；报错诡异时 clean 一把再全量</td></tr>
</tbody>
</table>
```
:::

两个选型问顺手答掉。<strong>问：HAR 和 HSP 怎么选？</strong>答：多数场景优先 HAR，简单可靠；确有运行时共享、按需加载的诉求再上 HSP，差异细节以官方对比文档为准。<strong>问：元服务和应用什么关系？</strong>答：两种独立形态，元服务更轻、免安装，上架要求也不同——动手前先读官方对比，别把应用的包直接"瘦身"当元服务。

记忆方法给你一把钥匙：工具类记全称（hdc、hvigor），包类记缩写（HAP、HAR、HSP、.app），概念类记场景（沙箱、一多、冷启动）——分不清时回到那个问题："它到底解决什么问题？"答得出，词就归位了。术语会随版本演进微调，拿不准的定义永远以官方术语页为准，这张表只负责让你读文档时不卡壳。

#### 二十三、给不同背景读者的速通路径

你带着哪门手艺来的，决定了该先翻哪几节。四条速通路径，每条配一个"最容易踩的坑"。

<strong>安卓背景</strong>：名词替换靠第十一节，一两周就能对上号。先看权限与生命周期——安卓的思维模型直接可用，换名字就行；构建从 Gradle 思维切到 hvigor，命令更少反而简单。最容易踩的坑：把四大组件的拆分习惯照搬过来——Stage 模型的核心就两个概念，UIAbility 加页面，先轻装上阵。

<strong>iOS 背景</strong>：SwiftUI 的声明式经验百分百复用，状态管理与 @State/@Binding 的对应看第十一节的 UI 表；Info.plist 的配置思维平移到 module.json5。最容易踩的坑：签名——你在 iOS 证书体系里攒下的直觉会误导你，鸿蒙的三件套流程不同（第九节），照文档一步步来。

<strong>前端背景</strong>：TypeScript 语法是你的优势，但第十节的六条收紧规则先读——最常见的翻车就是拿 TS 的动态写法硬写。布局从 CSS 盒模型思维映射到 Row/Column/Stack，弹性布局的肌肉记忆大半可用。最容易踩的坑：在 ArkTS 里写"TS 风格的动态对象"，编译器不会客气，早点改习惯早舒服。

<strong>纯新手</strong>：不用对照表，直接按第十二节的学习路线走——指南按 Kit 通读，Samples 三步用法当主要学习方式。第一个月别碰性能与架构，做出能跑的小东西比"写得正确"重要。最容易踩的坑：收藏教程不等于学会——每周至少留一次"从零建项目、跑起来"的完整练习。

四条路径的共同点只有一个：第一个星期都以"能跑起来"为目标，第二周才开始管"写得对不对"。对照表是拐杖，走稳了就扔。

#### 二十四、把速查章用起来的守则

速查章最怕两种死法：一是被人从头到尾通读（它不是小说）；二是收藏之后永不打开（它不是护身符）。五条守则，让它真正"活着"。

- <strong>按问题查</strong>：遇到什么翻什么，查完就走，不通读。
- <strong>给用过的节做标记</strong>：一节被用过三次，里面的内容你基本已经内化了。
- <strong>表格当签到表</strong>：每次踩坑回来，给对应行补一句自己的备注——你踩的坑比书里写的全。
- <strong>团队共享一张增补表</strong>：格式照下面的模板，谁踩坑谁补行，季度会上过一遍。
- <strong>每半年回审一次</strong>：版本坐标（第四节）与命令参数（第五节）跟着官方文档走，书会旧，方法不会。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">现象</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">原因</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">一句修法</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">（示例行）预览器白屏</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用了预览器不支持的特性</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">换模拟器或真机验证</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">（你的行）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"></td></tr>
</tbody>
</table>
```
:::

凌晨两点报障的标准翻页顺序：十三（环境）→ 十九（闪退白屏）→ 六（日志）→ 七（断点）。翻页顺序就是排查顺序——照这个顺序走过一遍，大半的猜谜时间就省下来了。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-quote-left mr-2"></i>一句话记牢

{class="mt-1"}
速查章的价值不在写它的人，在批注它的人——书是地图，你的批注才是本地路况。
:::

用满半年你会发现，需要翻的节越来越少——不是书变薄了，是你变强了。到那时候，这一章的任务就完成了：把你从"查表的人"，变成"写表的人"。

#### 二十五、一次完整的求助剧本

拿一个真实场景把全章串起来：周五晚上十一点，测试同事发来一句"你那个页面又闪退了，我复现不了几次"。整个求助过程该怎么走？八步剧本，照演。

1. 先问清三个事实：什么设备（真机还是模拟器）、什么版本（调试包还是历史版本）、什么操作路径——这三问能省掉一半猜谜。
2. 自己按第十九节的闪退五步走一遍：Log 过滤、找 FATAL、看调用栈。
3. 栈里能定位就上断点复现（第七节）；定位不了就按第六节埋日志，请测试帮忙蹲复现。
4. 十分钟没有头绪，别硬磕——把现象与环境信息整理成帖，按第十二节的发帖礼仪发出去。
5. 等回复的同时过一遍第十三节的环境表，排除环境因素——很多"偶现"其实是特定设备状态。
6. 论坛有人回帖，照建议验证；成了，把结论写下来。
7. 没人回，升级路径：官方文档的反馈入口提问题单，附最小复现步骤与环境信息。
8. 修完把崩溃栈、原因、修法写进团队增补表（上一节的模板）——同一个坑不踩第二次。

这个剧本的核心不是技巧，是顺序：先信息后猜测，先自证后求助，先修复后归档。反过来走的人，通常在群里问了一整晚，最后发现是数据线不支持传输。

求助不是示弱。把"我试过什么、卡在哪"讲清楚的人，得到的答案总是更快、更准——描述问题的能力，本身就是开发能力的一部分。

#### 二十六、构建报错与编译问题速对

编译期的问题有九成是"同一批老面孔"。一张速对表加一个通用三步，收尾这一章。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">报错关键词</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">一步修法</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">arkts-no-xxx（规则编号）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">按编号查第十节的对照表与官方迁移指南</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">资源引用失败（$r 找不到）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">资源名拼错或放错目录，改完 clean 再构建</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">页面路由相关报错</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新页面没在 main_pages.json 注册（见第十四节）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">依赖解析失败</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">oh-package.json5 版本号或网络问题，Sync 重来</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">类型不匹配</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">按第十节补类型，别用 any 糊弄</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">权限相关运行时报错</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">module.json5 没声明或用户没授权，两处分别核对</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">签名校验失败</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">调试签名过期或与旧包不一致，重新构建或先卸载（见第九节）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">端口 / 进程占用</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hdc kill 加 hdc start 重启服务（见第五节）</td></tr>
</tbody>
</table>
```
:::

通用三步：看清第一行报错（后面的几十行大多是它拖出来的）、跳到报错的文件与行号、改完 clean 再重跑。三步走完还有问题，才轮得到你去搜——而且这时你已经握着准确的关键词了。

编译缓存偶尔会记仇：代码明明改对了还报旧错，clean 一把、必要时把 IDE 的缓存清理选项用上，通常就清醒了。别跟缓存讲道理，它不讲。

#### 二十七、常用代码片段速查

第十一节给的是"翻译词典"，这一节给"现成句子"。十个最常用的片段，每个都带一句"什么时候抄它"——抄之前记得把名字与业务换成你的。

##### 轻提示（Toast）

保存成功、复制完成这类不打断操作的小反馈，用 Toast。

::: div .code-block
:::inline div .code-head
<span>ARKTS · Toast</span><span class="dots">···</span>
:::

```
import { promptAction } from '@kit.ArkUI';

promptAction.showToast({ message: '已保存' });
```
:::

##### 确认弹窗

删除前的确认这类强打断，用弹窗而不是 Toast——用户得明确表态。

::: div .code-block
:::inline div .code-head
<span>ARKTS · AlertDialog</span><span class="dots">···</span>
:::

```
AlertDialog.show({ message: '确认删除这条记录？' });
```
:::

按钮与回调参数看官方 API 参考，先把"能不能弹出来"跑通，再补交互细节。

##### 定时器与清理

页面里的定时器必须在页面销毁时清理，否则就是第八节说的那种"越用越卡"。

::: div .code-block
:::inline div .code-head
<span>ARKTS · 定时器</span><span class="dots">···</span>
:::

```
private timerId: number = -1;

aboutToAppear(): void {
  this.timerId = setInterval(() => {
    // 周期任务
  }, 1000);
}

aboutToDisappear(): void {
  clearInterval(this.timerId);
}
```
:::

##### 列表渲染

数组变界面的最小写法——第三个参数给稳定 key，长列表换 LazyForEach（第八节）。

::: div .code-block
:::inline div .code-head
<span>ARKTS · ForEach</span><span class="dots">···</span>
:::

```
ForEach(this.list, (item: Item) => {
  Text(item.name).fontSize(16)
}, (item: Item) => item.id)
```
:::

##### 点击与状态更新

状态一改、界面就变——这就是声明式的好处。

::: div .code-block
:::inline div .code-head
<span>ARKTS · 状态</span><span class="dots">···</span>
:::

```
@State count: number = 0;

Button('加一').onClick(() => {
  this.count += 1;
})
Text(`当前：${this.count}`)
```
:::

##### 本地键值存储

记住用户的开关与上次浏览位置，Preferences 三步：取、存、冲。

::: div .code-block
:::inline div .code-head
<span>ARKTS · Preferences</span><span class="dots">···</span>
:::

```
import { preferences } from '@kit.ArkData';

let prefs = await preferences.getPreferences(getContext(this), 'myStore');
await prefs.put('lastPage', 'detail');
await prefs.flush();
```
:::

##### 日志统一封装

第六节规范的最小落地——Domain 与 Tag 全项目只定义一次，别每个文件各写一套。

::: div .code-block
:::inline div .code-head
<span>ARKTS · Log 工具类</span><span class="dots">···</span>
:::

```
import { hilog } from '@kit.PerformanceAnalysisKit';

export class Log {
  private static readonly DOMAIN: number = 0x0001;
  static info(tag: string, msg: string): void {
    hilog.info(Log.DOMAIN, tag, '%{public}s', msg);
  }
}
```
:::

##### 资源引用

颜色、字符串、图片全走资源文件，深色模式才有得切（第十五节）。

::: div .code-block
:::inline div .code-head
<span>ARKTS · 资源</span><span class="dots">···</span>
:::

```
Text($r('app.string.welcome'))
  .fontColor($r('app.color.text_primary'))
  .backgroundImage($r('app.media.banner'))
```
:::

##### 获取上下文

存储、权限申请等不少 API 都要先拿应用上下文。

::: div .code-block
:::inline div .code-head
<span>ARKTS · Context</span><span class="dots">···</span>
:::

```
let context = getContext(this);
```
:::

具体类型按你调用的 API 要求转换，细节以当前版本的 API 参考为准。

##### 重活挪后台

主线程只留轻活——TaskPool 是第八节开的第一味药。

::: div .code-block
:::inline div .code-head
<span>ARKTS · TaskPool</span><span class="dots">···</span>
:::

```
import { taskpool } from '@kit.ArkTS';

@Concurrent
function heavyWork(input: number): number {
  return input * 2; // 真正的重活放这里
}

taskpool.execute(heavyWork, 100).then((result: number) => {
  // 回到主线程更新状态
});
```
:::

这些片段是"最小骨架"——能跑，但不是最佳实践的全部。抄完之后，回到对应小节把上下文补齐：错误处理看第十六节，性能看第八节，规范看第六节。

<strong>问：Toast 有时弹不出来？</strong>答：高频循环里反复刷会被限流——反馈要克制，通知同理（第二十节）。

<strong>问：片段编译报错？</strong>答：API 签名随版本微调，以你当前 SDK 的 API 参考为准——片段是骨架，不是合同。

<strong>问：片段能直接进生产吗？</strong>答：先把注释占位换成真实逻辑，错误处理按第十六节的清单补齐，再谈上线。

#### 二十八、自动化脚本与 CI 速查

把第五节的命令串成脚本，日常调试循环就从"手敲六条"变成"一键"。下面这条流水线照抄能跑（路径与包名换成你的）。

::: div .code-block
:::inline div .code-head
<span>SHELL · build_and_run.sh</span><span class="dots">···</span>
:::

```
# 日常回归流水线
hvigorw clean
hvigorw assembleHap
hdc install -r entry-release.hap
hdc shell aa start -b com.example.myapp -a EntryAbility
hdc shell hilog -x | grep MyApp > run.log
hdc shell snapshot_display -f /data/local/tmp/run.jpeg
hdc file recv /data/local/tmp/run.jpeg ./run.jpeg
```
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">步骤</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">它在干什么</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">clean</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">清产物，防缓存记仇（第二十六节）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">assembleHap</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">打包</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">install -r</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">装包</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">aa start</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">拉起应用</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hilog -x</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">存一段日志带回</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">snapshot + recv</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">截屏带回落档</td></tr>
</tbody>
</table>
```
:::

脚本三守则：多设备环境必带 -t，别让脚本"随机发货"；每一步判返回值，坏一步就停，别带着错误继续跑；产物统一收进带时间戳的目录，事后好翻。

这套脚本原样搬进 CI 也能用：提交即打包、装包、截屏，冒烟结果进产物目录。模拟器或真机在 CI 上的接入方式视平台而定，以官方 CI 相关指南为准。跑完把日志与截屏归档到增补表对应的行（第二十四节）——回归记录自己会长成团队的资产。

<strong>问：脚本里 grep 报错找不到命令？</strong>答：Windows 传统终端用 findstr，Git Bash 才有 grep。

<strong>问：截屏出来是黑的？</strong>答：部分界面（如支付页）系统限制截屏，属正常保护——别绕，也没必要绕。

#### 二十九、发版前验收清单

全章的收口是一张真机回归清单：十五条，逐条打勾，勾完才准点"构建发布包"。

- 冷启动到首屏无长时间白屏（对照第八节 Startup）
- 核心页面深浅色各过一遍
- 弱网下核心流程有明确提示，不无限转圈
- 断网提示准确，网络恢复后能自动续上
- 每个权限"拒绝后"的降级路径走得通（第二十一节）
- 通知开关关闭后功能不崩，重新打开后恢复
- 后台切回前台，页面状态与输入内容还在
- 长列表连续滑动不掉帧（Frame 面板确认）
- 反复进出核心页面十次，内存不持续上涨（Memory 面板）
- 来电、闹钟打断媒体播放的行为符合预期
- 登录态过期后的跳转与重登流程完整
- 涉及支付的功能走完整的沙箱与真机流程
- 占位图、测试文案、调试入口清零
- 卸载重装后的首次启动引导完整
- 上架物料（图标、名称、截图、隐私声明）与最终版本一致

时间紧时按三级验收砍：一级是登录、核心功能、支付，一条不能省；二级是权限降级与后台行为；三级是体验细节。砍的顺序从三级往下，别倒着来。

<strong>问：十五个条目都过一遍太费时，能抽查吗？</strong>答：日常迭代抽查一、二级即可；大版本或升级 API 之后必须全量——版本说明里的行为变更就是为这时候准备的（第四节）。

<strong>问：验收发现问题，改完要全量重跑吗？</strong>答：改了什么验什么，外加一级项兜底——回归范围跟着改动走，但一级项永远在场。

这张清单可以直接进增补表（第二十四节）：团队每发现一个漏验项就补一行，半年后它就是你们团队最值钱的一页纸。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-quote-left mr-2"></i>一句话记牢

{class="mt-1"}
发布的底气不是"应该没问题"，而是清单上十五个勾——勾是证据，感觉不是。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- hdc 是鸿蒙的 adb：list targets / install / shell aa start / file
- 装饰器速查：V1 的 @State/@Prop/@Link 优先记牢，V2 别与 V1 混用
- Kit 即"能力包"：Form/Ability/Network/ArkData 按需引入
- 升级走五步：IDE → 命令行 → API Change Assistant → 兼容测试 → 发布
- 官方文档 + Samples + 认证考试是进阶三件套
- 三大平台毕业：安卓、iOS、鸿蒙——你已经是全平台移动开发者
:::
