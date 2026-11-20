---
id: di-wu-shi-qi-zhang
num: 57
part: an-zhuo-kai-fa-pian
nav: 第五十七章：进阶之路——权限、通知与现代架构
toc: default
kind: chapter
---

### 第五十七章：进阶之路——权限、通知与现代架构

{class="chapter-intro mb-4"}
能做出 App 只是开始。这一章聊聊从"会做"到"做好"的几道坎：怎么优雅地申请权限、怎么发通知不讨人厌、怎么把架构再往上抬一层，以及：在 2026 年，怎么和 AI 搭档写安卓代码。每一条都是你在真实项目里马上会遇到的。

::: div .quick-read
##### 本章速读（5 分钟版）
这一章是从"会做"到"做好"的几道坎：怎么优雅地申请权限、怎么发通知不讨人厌、怎么把架构再往上抬一层，还有 2026 年怎么和 AI 搭档写安卓代码。每一条都是真实项目里马上会遇到的，权限弹窗怎么开口、通知怎么不被用户划走、代码乱了怎么分家，这一章都有现成答案。最后还有一场实战串联：给你的记账本加上"每晚八点提醒"，一次练到三样本事。

最关键的有三件事。第一，权限的规矩是<strong>先敲门，再进门</strong>：Manifest 声明、运行时申请，用到哪项功能的那一下再弹窗、说清用途，用户拒绝就优雅降级，一进 App 就要相机、定位、通讯录的"权限轰炸"，换来的直接是卸载。第二，通知三纪律：只发有用的、能关、不骚扰。渠道和权限缺一不可，一个类别一个渠道；定时提醒用 WorkManager，别自己拿别的轮子造。第三，最小可用架构是四层：UI、ViewModel、Repository、数据源，事件往下走、状态往上流；依赖注入先手动写，Hilt 等痛了再上，模块化等编译慢了再拆<strong>层数是结果不是目标</strong>，能"改一处不牵连三处"的结构就是好结构。另外记住权限的连带账单：要了敏感权限，数据安全表和隐私政策就得如实跟上；能用系统组件绕开的权限就别申请，"零权限"把事办成，是最好的隐私设计。

今天就能做的最小动作：跟着章里的实战，给记账本加"每晚八点提醒"：它一口气练到通知渠道、权限和 WorkManager 三样。做完对着验收清单过一遍：提醒发得出、关得掉、不吵人。要是暂时不想写功能，就干一件更小的：把 AI 当代码评审员，让它挑一遍你权限申请代码里的毛病，自己再逐条验收。

最大的坑全是"过犹不及"。权限要得越多用户越跑，通知发得越勤打开率越低，架构叠得越厚维护越贵。性能优化别靠"感觉卡"，Profiler、重组计数这些测量工具都是现成的，感觉说这里慢、数据说那里慢，听数据的。也别让 AI 替你决定权限和隐私策略：AI 能列出技术上有几种做法，但选哪种是产品决策，只有了解你用户的你能答。
##### 速查表
- 权限怎么要：用到那一下再弹窗，说清用途，拒绝后优雅降级
- 用户拒绝了怎么办：给引导和替代路径，别死循环弹窗
- 通知怎么发：只发有用的、能关、不骚扰，一个类别一个渠道
- 定时提醒怎么定：用 WorkManager，别自己造轮子
- 架构最小骨架：UI、ViewModel、Repository、数据源，事件往下、状态往上
- 依赖注入怎么上：先手动组装，痛了再上 Hilt，别第一天就上框架
- 性能怎么查：别信感觉，Profiler 和重组计数说了算
- AI 怎么用：写码、查资料、写测试、改 bug 四个场景，产出必须自己验收
:::

<div class="version-anchor">本章界面路径按 iOS 18.x / HarmonyOS 5.x / Android 15 核对（2026 年 11 月）。你的机型或系统版本不同，菜单名字和位置可能对不上——以你手机上显示的为准。</div>


#### 一、运行时权限：先敲门，再进门

相机、定位、通讯录、通知……这些"敏感地带"，安卓要求 App <strong>运行时向用户申请</strong>（Android 6 起）。规矩是：先声明（Manifest），再申请（代码），用到哪项功能的那一下再弹窗、并说清用途，用户拒绝要优雅降级。Compose 里用官方自带的 <code class="inline">rememberLauncherForActivityResult</code>（无需第三方库）最省心：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 运行时权限（Compose 版）</span><span class="dots">···</span>
:::

```
// Manifest 里先声明：
// &lt;uses-permission android:name="android.permission.CAMERA" /&gt;

@Composable
fun CameraButton() {
    val context = LocalContext.current
    var granted by remember {
        mutableStateOf(ContextCompat.checkSelfPermission(
            context, android.Manifest.permission.CAMERA) ==
            PackageManager.PERMISSION_GRANTED)
    }
    val launcher = rememberLauncherForActivityResult(
        ActivityResultContracts.RequestPermission()
    ) { ok -&gt; granted = ok }
    Button(onClick = {
        when {
            granted -&gt; openCamera()
            ActivityCompat.shouldShowRequestPermissionRationale(
                context as Activity, android.Manifest.permission.CAMERA)
                -&gt; showExplainDialog()
            else -&gt; launcher.launch(android.Manifest.permission.CAMERA)
        }
    }) { Text("拍照") }
}
// imports：androidx.activity.compose.rememberLauncherForActivityResult、
// androidx.activity.result.contract.ActivityResultContracts、
// androidx.core.app.ActivityCompat / ContextCompat
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>注意：被永久拒绝怎么办？

{class="mt-1"}
用户勾了"不再询问"后，再次调用 <code class="inline">launcher.launch(...)</code> 不会再弹窗。此时应引导用户去系统设置里手动开启（用 <code class="inline">Intent</code> 跳到应用设置页），并在界面里说明"这个权限用来做什么"。态度好一点，用户开权限的意愿会高很多<strong>申请权限的文案，值得认真写</strong>。
:::

##### 权限分两派：装了就给的，和开口才给的

先把全局地图画清楚。安卓的权限分两类：普通权限（比如联网 INTERNET）安装时就自动授予，你只需在 Manifest 里声明，用户全程无感，这就是为什么联网的 App 从来不弹"我要上网"的窗；危险权限（相机、录音、定位、通讯录、通知这些涉及隐私的）则必须运行时向用户开口，就是上面代码里演示的那套流程。写 App 之前先给功能清单过一遍筛子：哪些是普通权限（不用管），哪些是危险权限（要设计申请流程）。危险权限的具体清单会随系统版本调整，以官方文档为准。

这个分类直接决定产品设计：能归入"普通"的功能尽量别往"危险"凑。比如选图片这件事，用系统照片选择器的话甚至可以不需要存储权限，权限用得越少，申请流程越简单，审核也越顺。少即是多，在权限上尤其如此。

##### Manifest 声明：别漏的第一道登记

运行时申请之外，Manifest 里的声明一步都不能少：没声明就申请，系统会直接抛异常，新手第一次接权限几乎都栽在这里。顺带一个反向提醒：声明要和功能对齐，别照抄别人的 Manifest 模板把用不到的权限一起声明进来。商店审核会核对"权限清单与应用实际功能"，一个用不到的通讯录权限，就可能换来一条"权限与用途对不上"的退回意见（上一章说过这是高频退回原因）。声明按需、申请按需、解释按需，三个按需连成一条线。

##### 常见权限对照表：什么时候申请、怎么开口

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">权限</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">典型用途</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">申请时机</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">向用户解释的话术示例</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">相机</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">拍消费凭证</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">进入拍照页的那一刻</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"用于拍摄凭证照片，只存在手机里"</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">麦克风</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">语音转备注</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">点下录音按钮那一刻</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"按住说话时录音，转成文字备注"</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">精确定位</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">账单加地点标签</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用户打开"地点标签"开关时</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"用于给账单标记地点，可随时关"</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">媒体图片</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">从相册选凭证图</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">点"从相册选"时；优先考虑系统照片选择器，可省掉这权限</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"只读取你挑选的那张图"</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">通知</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每日记账提醒</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">引导页讲清价值之后</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"晚上八点提醒你记账，不想收可关"</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">附近设备</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">连蓝牙打印机打小票</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">进入"连接打印机"页面时</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"用于发现并连接附近的打印机"</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">通讯录</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——记账本根本用不到</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">（反例）别申请</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">权限越少，用户越放心</td></tr>
</tbody>
</table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
常见权限的申请时机与解释示例（清单以官方文档为准）

这张表最值得看的是"申请时机"一列。全部是"用到的那一刻"，没有一个是启动时。时机选得对，弹窗出现在用户正需要这个功能的上下文里，授权是顺水推舟；时机选得错，弹窗出现在用户还没明白这个 App 是干嘛的时候，授权就是水中捞月。

##### "仅本次允许"：容易被忽略的例外

从较新的系统开始，权限弹窗多了一个选项："仅这一次允许"（相机、麦克风、定位这类常见）。用户选它之后，授权只在这次使用期间有效，应用退出后就收回。下次再用会重新询问。这对代码的影响是实实在在的：<strong>别把"已授权"当成永久状态缓存起来</strong>。进功能页时重新检查一次权限，检查逻辑放在每次进入时而不是只放首次启动，你的代码本来就该这样写（示例代码里每次点击都查一遍），现在你知道为什么了。

对用户视角多想一层：愿意给"仅这一次"的用户，其实是"想试试"的用户，不是拒绝的用户。所以"仅本次"状态下的体验不能打折：功能要完整可用，下次再进时不要带着"你怎么又没授权"的怨气弹窗。一次性授权处理得好，用户下次很可能给永久授权。

##### 久不用的应用，权限可能被系统自动收回

还有一条系统级行为要知道：长期没被使用的应用，敏感权限可能被系统自动重置。这对用户是保护，对开发者是个"回来的老用户权限没了"的场景——某天用户重新打开你的记账本，发现拍照凭证用不了了。对策很简单：检测到权限丢失时，给一次温和的说明（"为了使用拍照凭证，需要相机权限"）加一个去设置的入口，而不是报错或沉默。系统收回了权限，你的 App 要负责体面地把流程接回来。

##### shouldShowRequestPermissionRationale 的三种状态

上面示例代码里的 <code class="inline">shouldShowRequestPermissionRationale</code> 是权限体系里最"绕"的一个方法。值得单独讲清。它只在一种情况下返回 true：用户拒绝过至少一次、但还没选"不再询问"。而从未问过、已授权、永久拒绝这三种情况下，它都返回 false。同样的 false，含义完全不同。所以判断"是否永久拒绝"不能只靠它，要配合自己记录的状态：如果它返回 false、权限没给、而且你确认之前问过，那就基本可以断定用户勾了"不再询问"，走引导去设置的那条路。

把这套逻辑画成一个状态机，就是四条路：已授权，直接用；拒绝过一次，先弹解释框再申请；从未问过，直接申请；永久拒绝，引导去系统设置。用伪代码写下来：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 权限请求的推荐流程（伪代码）</span><span class="dots">···</span>
:::

```
when {
    hasPermission -&gt; useIt()                 // 已授权：直接干活
    shouldShowRationale -&gt; explainThenAsk()  // 拒绝过一次：先讲理由再问
    askedBefore -&gt; guideToSettings()         // 问过仍被拒：引导去设置页
    else -&gt; launcher.launch(permission)      // 从没问过：直接申请
}
```
:::

记住这个四分支结构，任何权限的申请代码都是它的变体。这也是面试里常问的题，更重要的是，写对它，用户才不会觉得你的 App 在"纠缠"。

##### 有些权限可以"绕开"：系统组件的妙用

在学申请技巧之前，先学一手"不申请"的功夫。很多看似要权限的事，官方都给了系统组件替你干活：拍照可以用系统的拍照契约，调起系统相机完成拍摄、照片回传给你，多数情况下连相机权限都省了（个别情况有例外，以官方文档为准）；选图可以用系统照片选择器，用户挑哪张你才读哪张；分享内容可以调系统分享面板。这些方案共同的好处是：权限申报更少、审核更顺，用户也少弹几次窗。

把它当一条设计守则：遇到"需要权限"的需求，先查一遍官方文档有没有对应的能力组件（ActivityResultContracts 一族里翻一翻），绕得开就绕。能用系统组件解决的事申请权限，属于没做功课。

##### 申请时机的黄金三条

- <strong>用到才问</strong>：弹窗跟着功能走，不跟着启动流程走。启动页连环弹三四个权限的 App，用户的本能反应就是"它想干什么"，然后卸载。
- <strong>一次一个</strong>：需要相机和通知就分两次、在两个场景各问各的。一起问会让用户只记住"这个 App 要一大堆东西"。
- <strong>先给价值再要授权</strong>：通知权限这种"现在没用以后有用"的，先让用户体验核心功能，觉得靠谱了再在恰当的时机开口，授权意愿完全不一样。

三条背后的原理是同一条：弹窗本身没有说服力，说服力来自"此刻这个功能对我有用"。把申请流程当成产品设计来做，而不是当成技术步骤来抄。

##### 拒绝之后的产品设计：优雅降级清单

用户拒绝权限之后，你的 App 应该降级而不是罢工。给记账本列一份"降级清单"，几乎每条都是通用思路：相机被拒，支持从相册选图（照片选择器不用权限）或手动输入文字凭证；定位被拒：让用户手填"在哪儿花的"；通知被拒，App 内的提醒页面照常存在，只是不能弹系统通知，引导语放在设置页而不是反复弹窗。核心是同一句话：<strong>权限是增强，不是前提</strong>。

反过来检验一下自己的设计：把某个权限全砍掉，你的 App 还剩多少能用？剩下的部分越完整，说明降级设计越好。这个"权限残缺测试"值得在开发期就做一遍，别等用户拒绝时才发现主功能全瘫。

##### 权限的连带账单：数据安全表与隐私政策

权限还有一个容易漏算的"下游成本"：你在 Manifest 和运行时申请的每一个危险权限，都要在商店的数据安全表和隐私政策里有对应说法（上一章刚讲过那两张表）。权限申请多了，表要跟着细、政策要跟着写、审核要跟着盯，每多一个权限，发布的合规成本都在涨。这又回到了同一个结论：权限能少则少，能绕则绕。申请前先把"合规账单"算一遍，很多权限在算账这一步就会被砍掉。

##### 特殊权限：几乎都别碰的清单

除了运行时权限，还有一类"特殊权限"要单独点名：悬浮窗、无障碍服务、通知读取、电池优化忽略、修改系统设置这些，它们的授权方式不是弹窗。它们的授权方式是跳到系统设置页让用户手动打开，并且商店审核对它们格外严格。除非它们就是你应用的核心功能（比如真正的无障碍工具），否则别申请，滥用无障碍权限读取用户其他界面内容，是商店政策明确打击的行为，也是安全新闻里的常客。记账本这类工具，一份运行时权限都嫌多，特殊权限更是一个都不该有。

#### 二、通知：在正确的时间说有用的话

通知是 App 触达用户的通道，也是最容易被用户"拉黑"的功能。发通知三条纪律：<strong>只发有用的、让用户能关、别半夜骚扰</strong>。基础用法：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 发一条通知</span><span class="dots">···</span>
:::

```
// Android 13+ 必须先申请 POST_NOTIFICATIONS 权限（见上一节）

// 1. 创建通知渠道（Android 8+ 必须）
val channel = NotificationChannel(
    "reminder", "提醒", NotificationManager.IMPORTANCE_DEFAULT
)
val manager = getSystemService(NotificationManager::class.java)
manager.createNotificationChannel(channel)

// 2. 发通知
val notification = NotificationCompat.Builder(this, "reminder")
    .setSmallIcon(R.drawable.ic_notification)
    .setContentTitle("记账提醒")
    .setContentText("今天还没记账哦")
    .setPriority(NotificationCompat.PRIORITY_DEFAULT)
    .build()
if (ActivityCompat.checkSelfPermission(this,
        Manifest.permission.POST_NOTIFICATIONS) == PackageManager.PERMISSION_GRANTED
) {
    manager.notify(1, notification)
}
```
:::

代码里的 "reminder" 就是一个通知渠道，Android 8.0 起必须先建渠道才能发通知。渠道别只建一个兜底，按类别拆开（记账提醒、周报、系统公告），用户就能只关掉吵的那一类，而不是一刀切换掉你的全部通知。

定时任务（比如"每天 20:00 提醒记账"）用 <strong>WorkManager</strong>——它是官方推荐的"后台调度管家"，能保证任务在合适时机执行，不用自己操心电池优化；可延迟的活儿都交给它，别自己起一个常驻 Service 硬扛。日常提醒类用它没问题；必须准点的闹钟类需求，官方建议用 AlarmManager。

##### 渠道的最佳实践：一个类别一个渠道

渠道设计的核心问题只有一个："用户想单独关掉哪类消息？"答案就是你的渠道划分。记账提醒、周报摘要、系统公告，三类三个渠道，各起一个用户能看懂的名字，渠道名会直接显示在系统的通知设置里，"提醒""通知1"这种名字等于没起。创建渠道的操作是幂等的：同一个 id 重复创建无害，所以可以在应用启动时放心地确保渠道存在，不用记着"已经建过了"。

另外两条渠道纪律。一，用户对某个渠道做的开关、声音选择存在系统里，就算你删掉渠道再重建，用户之前的选择依然留着：所以别打"删了重建重置用户设置"的主意，行不通，还招人烦。二，发通知时用对渠道，别把所有消息都塞进默认渠道，那样用户只能一刀切，一刀切的结果通常是切掉你。

##### importance：从无声到横幅的差别

创建渠道时要选重要级别（importance），它决定通知的打扰强度：HIGH 会弹出横幅并响铃，适合"用户明确期待的即时消息"；DEFAULT 正常提示，大多数场景用它；LOW 静静躺在通知栏，不响不动，适合周报这种"回来看就行"的内容；更低的级别基本无感。级别是建渠道时定的，之后你改不了用户看到的实际表现：用户还能在系统设置里再降一级。选择的原则很简单：默认从低不从高，打扰是负债，攒多了用户就把整个 App 静音了。具体各级别在不同系统上的表现细节以官方文档为准。

##### 一条通知的完整解剖

示例代码发的是最简单的一条。真实的通知通常还要三样东西：点击后的去向、自动消失、必要时的展开样式。点击跳转靠 PendingIntent，把"点通知打开记账页面"这个动作打包给系统，系统在用户点击时替你执行；较新的系统要求显式声明 PendingIntent 的可变性，<code class="inline">FLAG_IMMUTABLE</code> 是最常用的安全选择。<code class="inline">setAutoCancel(true)</code> 让用户点完通知自动消失，不然通知会赖在栏里，看着很不专业。长内容用 <code class="inline">BigTextStyle</code> 展开显示。看一个完整版：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 可点击、会消失的通知</span><span class="dots">···</span>
:::

```
val intent = Intent(this, MainActivity::class.java)
val pending = PendingIntent.getActivity(
    this, 0, intent,
    PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT
)
val notification = NotificationCompat.Builder(this, "reminder")
    .setSmallIcon(R.drawable.ic_notification)
    .setContentTitle("记账提醒")
    .setContentText("今天还没记账哦")
    .setContentIntent(pending)
    .setAutoCancel(true)
    .build()
```
:::

还有一条容易忘的：<code class="inline">setSmallIcon</code> 是必填项，没它通知发不出来。小图标用单色的线条图形，别用彩色大图：它在状态栏只有一小格的空间。这些"发出去才算数"的细节，第一次发通知时会挨个碰一遍，碰完就都记住了。

##### 通知权限：两道闸门与申请话术

发一条通知要过两道闸门：通知权限（Android 13 起）和渠道开关。权限不在，通知根本发不出；权限在但渠道被关了，还是发不出。排查"通知发不出来"时按这两层依次检查，一分钟的活。申请权限的时机前面讲过原则，这里补话术：不要在启动时直接弹系统授权框，先给自己的 App 一个"预告页"："想每天提醒你记账，需要通知权限，现在开启吗？"用户点头再调 launcher。预告页加系统弹窗的两段式，比裸弹窗的授权率高得多，因为用户是在知情的情况下做的决定。

被拒绝之后的姿势也别忘了：设置页里保留一个"开启记账提醒"的入口，点击走引导去系统设置的流程。通知权限和相机权限不一样，它没有"用到那一刻"的天然场景，所以更要靠"价值先行"来申请。

##### 远程推送入门：FCM 与它的边界

前面代码里的通知都是"本地通知"：你的 App 自己发起。另一大类是"远程推送"：服务器有新消息，经过 Firebase Cloud Messaging（FCM）送达设备并展示。比如"你的账单报告已生成"。整套链路是：你的后端调用 FCM → FCM 把消息路由到对应设备 → 系统展示（或转交应用处理）。推送需要 Firebase 项目和后端配合，属于"接入成本"明显更高的一档，纯本地应用完全用不着。

两个入门要点。一，推送消息分"通知消息"和"数据消息"两类：前者系统直接展示，后者交给你的代码自己决定怎么处理，怎么选以官方文档为准，别想当然。二，边界要心里有数：FCM 依赖设备上的 Google 服务，中国大陆的常规设备环境用不了它，国内推送通常要接各厂商自家的推送通道（每家一套，规则各异）。本章只建立"推送是怎么回事"的概念，真要接入时按官方文档走，这是那一整天的事，不是这一小节的事。

##### WorkManager 与 AlarmManager：到底怎么选

第二节正文说过结论，这里把判断标准展开。WorkManager 的定位是"可延迟的后台任务"：同步数据、上传备份、定期清理，这些活儿晚几分钟无所谓，系统会挑省电又合适的时机执行：注意"合适时机"不等于准点，它不保证秒级准时。而"每天早上 7:00 必须响"的闹钟类需求，用 AlarmManager 的精确闹钟能力；较新的系统上精确闹钟还需要专门的声明（官方对闹钟、日历这类"时间就是功能本身"的应用有相应的授权通道），细节以官方文档为准。

一句话决策：晚几分钟无所谓的，WorkManager；晚一分钟都算错的，AlarmManager。记账本那个"每天八点提醒"落在哪边？说实话它是灰色的，用户对提醒的准点有期待，但晚几分钟通常也能接受。参考做法：先用 WorkManager 实现一版看体验，用户真的抱怨不准点再升级到 AlarmManager。别一上来就用最重的方案，也别为了省事用错方案。另外 WorkManager 还支持给任务加条件（比如"只在 Wi-Fi 下执行""只在充电时执行"），这让它管"可延迟任务"的能力更完整，具体约束项以官方文档为准。

##### 通知的礼仪清单

- <strong>渠道分好类</strong>：用户能单独关掉吵的那类，而不是一刀切。
- <strong>营销类默认关</strong>：促销、拉新类消息默认不发，要发也让用户主动订阅。
- <strong>深夜别响</strong>：提醒类消息按用户时区发，别让"晚上八点"变成地球另一端的凌晨三点。
- <strong>一条通知只说一件事</strong>：标题说清来源，正文说清要干什么，点开就有对应页面。
- <strong>可聚合就聚合</strong>：同类消息合并成一条摘要，别一晚上刷十条。

把通知想象成"你敲用户家的门"：有事才敲，敲门时说清楚是谁、什么事，敲完就走。天天来敲、敲门不说话、半夜来敲的，用不了几次就会被拉进黑名单，通知渠道就是这个黑名单的按钮。

#### 三、架构进阶：依赖注入与模块化

项目变大后，两个"甜蜜的烦恼"会找上门：

- <strong>对象创建乱</strong>：每个页面都在自己 new 数据库、new API，用 <strong>Hilt</strong>（依赖注入框架）统一管理，"谁要什么，开口就有人递"。
- <strong>代码堆成山</strong>：单模块项目越改越慢，拆成 <strong>多模块</strong>（app / core / feature-xxx），各功能独立开发、独立测试。

比"上工具"更要紧的，是先把数据流向捋直。2026 年安卓项目的一个"最小可用架构"长这样：<strong>UI → ViewModel → Repository → 数据源</strong>，事件往下走、状态往上流，界面不直接碰数据库或网络。用 StateFlow 或 Compose State 对外暴露一个不可变的 UI 状态，界面只负责渲染和发事件，一条单向数据流，够用，还特别不容易写乱。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：别过度设计

{class="mt-1"}
Hilt 和模块化都是好工具，但<strong>单人项目先别急着上</strong>。记账本单模块 + 手动创建依赖完全够用。等代码量超过几万行、编译开始变慢、多人协作时，再按需引入，到时候 Koin 这类更轻的替代品也值得看一眼，把对象的构造交给容器，测试时还能换成假实现。架构不是层数越多越好，能让你"改一处不牵连三处"就够了。工具是服务目标的，不是用来炫耀的——这也是咱们 AI 编程书里的"简单至上"原则。
:::

##### 先看病：什么都写进界面代码的下场

架构这事儿，先看"病"才知道"药"治什么。新手最常见的写法是全部塞进界面层：点击"保存"的回调里，读输入框、算金额、开数据库、写记录、刷新列表，一口气二百行。写的时候一气呵成，痛在三周后，想给"保存"加个金额上限校验，得在五个页面各改一遍；想在测试里验证记账逻辑，得先把整个界面跑起来；改一处列表刷新，统计页跟着出怪毛病。界面、业务、数据搅成一团泥，这就是"要架构"的全部理由。

药方也不是什么高深的咒语，就是"分家"：界面只管显示和转发，业务集中在 ViewModel，数据的进出只走 Repository。分完之后你会发现，前面几章反复出现的那些词，单向数据流、StateFlow、依赖注入，全都是"分家"这件事的具体手法。先有目的，后有手段，学架构就不会晕。

##### MVVM 是什么：一张表说清分工

这套"分家"方案在安卓的官方语境里叫 MVVM（Model-View-ViewModel）。名字唬人，分工很朴素：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">角色</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">职责</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">记账本里对应什么</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">View（界面）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">渲染状态、转发用户事件，不含业务</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Compose 写的记账列表页</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ViewModel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">持有界面状态、编排业务逻辑</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">LedgerViewModel：列表、总额、加载状态</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Model（Repository）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数据的唯一出入口，封装数据源</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">LedgerRepository：包着 Room 和文件存取</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数据源</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真正存取的地方</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room 数据库、以后的远程 API</td></tr>
</tbody>
</table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
MVVM 四个角色的分工

检验自己有没有分对家的办法很简单：看你写界面的时候，有没有出现数据库或网络的名字。出现了，就是有人串门了，把那段逻辑请回 ViewModel 或 Repository 去。

##### ViewModel 为什么"活得久"：屏幕转了它不死

ViewModel 有一个让新手惊喜的特性：旋转屏幕这类"配置变化"会重建界面，但 ViewModel 会存活下来。这意味着列表数据、滚动状态、加载标记这类东西放在 ViewModel 里，转个屏不会丢，这是"状态放 ViewModel"最实在的理由，也是它名字里"生命周期感知"的由来。反过来有一条红线要记住：ViewModel 里不要持有界面（Activity、Context）的引用，界面死了它还在抓着，内存泄漏就来敲门（上一章的 LeakCanary 逮的就是这类）。要用 Context，用应用级的，而且大多数时候你根本不需要。

##### 最小 ViewModel 示例：记账本的样子

看一个最小可用的 ViewModel，对着读一遍胜过十段理论：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 一个最小可用的 ViewModel</span><span class="dots">···</span>
:::

```
data class LedgerUiState(
    val records: List&lt;Record&gt; = emptyList(),
    val totalAmount: Double = 0.0,
    val loading: Boolean = false
)

class LedgerViewModel(private val repo: LedgerRepository) : ViewModel() {

    private val _uiState = MutableStateFlow(LedgerUiState())
    val uiState: StateFlow&lt;LedgerUiState&gt; = _uiState.asStateFlow()

    init { loadRecords() }

    fun loadRecords() {
        viewModelScope.launch {
            _uiState.update { it.copy(loading = true) }
            val list = repo.getAllRecords()
            _uiState.update {
                it.copy(records = list, totalAmount = list.sumOf { r -&gt; r.amount },
                        loading = false)
            }
        }
    }

    fun addRecord(amount: Double, note: String) {
        viewModelScope.launch {
            repo.insert(Record(amount = amount, note = note))
            loadRecords()
        }
    }
}
```
:::

读的时候注意三个设计决定。一，对外只暴露只读的 <code class="inline">StateFlow</code>，界面能看不能改，改状态的入口全部收在 ViewModel 的方法里；二，状态打包成一个 UiState 数据类，界面只拿这一个对象。渲染逻辑简单到"照着画"就行；三，界面事件对应 ViewModel 的公开方法（addRecord），方法内部该干嘛干嘛，界面完全不用知道。这三条就是"单向数据流"的全部实操。

##### 单向数据流：为什么它"不容易写乱"

把上面这套的运转画成圈：

1. 用户点"保存"
2. 界面调 viewModel.addRecord()
3. ViewModel 让 Repository 写库、更新 UiState
4. StateFlow 发出新状态
5. 界面重组渲染

事件永远往下走，状态永远往上传，没有第二条路。它"不容易写乱"的原理是：状态只有一个写入口（ViewModel），出问题时你只需要问"谁改了状态"，而不是"这几个地方谁先谁后改了状态"。调试和测试的成本都跟着降：这跟上一章讲的"单一职责"是同一个思想，落在了数据流上。

##### 依赖注入入门：先手动，再谈框架

依赖注入（DI）这个词听着高级，手动版其实就一句话：把"对象自己创建依赖"改成"依赖从外面递进来"。LedgerViewModel 的构造参数里写着 <code class="inline">repo: LedgerRepository</code>——它自己没有 new 任何数据库，谁来创建它，谁就得把 repo 递进来。这就是依赖注入，你已经会用了一半。

手动版的完整做法是用一个容器统一保管依赖：应用启动时创建一次数据库和仓库，全 App 共用，谁需要就递给谁。官方文档里管这个模式叫手动依赖注入，记账本这个体量用它刚刚好：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 手动依赖注入的容器</span><span class="dots">···</span>
:::

```
class AppContainer(database: AppDatabase) {
    val ledgerRepository = LedgerRepository(database.ledgerDao())
}

class LedgerApp : Application() {
    lateinit var container: AppContainer
    override fun onCreate() {
        super.onCreate()
        container = AppContainer(AppDatabase.getDatabase(this))
    }
}
```
:::

手动版的好处是"看得见"：每个对象从哪来、谁依赖谁，打开容器一目了然。代价是递东西靠手工：页面多了、依赖链深了，手工就会累。累到那个份上，就该请出 Hilt 了。

##### Hilt 概览：注解怎么变成"自动递送"

Hilt 是官方的依赖注入框架（基于 Dagger），它替你干的就是"递东西"这件事，规则用注解写。常用的几个：<code class="inline">@HiltAndroidApp</code> 标在 Application 上，打开整套机制；<code class="inline">@Inject constructor</code> 标在构造函数上，意思是"这类可以要、也可以给"；ViewModel 用 <code class="inline">@HiltViewModel</code> 加构造上的 <code class="inline">@Inject</code>，界面里就能直接拿到现成的；遇到你改不了构造函数的第三方库，用 <code class="inline">@Module</code> 加 <code class="inline">@InstallIn</code> 写一个"怎么造它"的说明书。标注了单例作用域的对象全 App 一份（比如那个数据库）。

它和手动版的本质区别在于：这些接线在<strong>编译期</strong>就生成好，不靠反射运行时找对象，接错了线编译直接报错，问题在写代码时暴露而不是在用户手机上。学习成本主要在概念（作用域、组件层级），第一次上手建议照官方文档的示例抄一遍，比读十篇讲解都快。该不该现在就引入？回到上面那块小贴士：记账本还没累，先手动；手动版开始"递到手酸"，再上 Hilt。工具的引入时机跟着痛感走，不跟着潮流走。

##### 多模块拆分：等编译慢了再动

模块化是把一个巨大的 app 模块拆成若干小模块（core:database、core:design、feature:ledger……），好处有三：编译可以按模块增量进行、代码边界被物理强制（想跨模块乱引用都引用不了）、多人可以各改各的模块互不阻塞。代价是配置成本和心智负担，每个模块一套构建脚本、一套依赖声明。单人小项目通常用不上。判断信号很明确：编译等得心慌、或者要跟别人协作了，再拆。拆的时候从"最稳定的底层"开始（数据库、通用 UI 组件），别一上来就按页面拆。

##### 架构的最终产出：可测试性

把这一节收个口。MVVM、依赖注入、模块化，三件事指向同一个终点：代码可以被单独测试。ViewModel 不依赖界面，单元测试直接new 一个假 Repository 就能测（上一章讲的测试替身，在这里接上了头）；Repository 依赖接口，数据库可以换成内存假实现；模块边界清晰，每个模块自带测试。架构好不好，不看图多漂亮，看"改一处会不会牵连三处"和"想测的时候测不测得了"，这两条达标，架构就及格了，层数多一层都是浪费。

##### 把权限流程测一遍：模拟四种用户

权限的四分支逻辑写完了，怎么验证它都对？在设置页里手动扮演四种用户：路径是系统的应用信息 → 权限，把相机权限在"允许、询问、拒绝"几个状态之间切换，每个状态进一次拍照页，看走的分支对不对。四个分支各过一遍，比写十遍代码都踏实：权限这东西 UI 测试覆盖起来麻烦，手动走查反而是最经济的验法。

顺手把"仅本次允许"和"系统自动收回"这两个特殊状态也测了：选一次"仅这次允许"退出再进，看会不会重新问；把应用晾几天（或者手动关掉权限模拟）再打开，看提示是否体面。这几种边缘状态，恰恰是线上用户最容易撞见的。

##### 声音和震动：让渠道替你管，别自己管

新手常问"怎么让通知响铃、怎么震动"：答案是不用管：渠道创建时的 importance 决定了默认的声音和震动行为，用户还能在系统设置里对每个渠道自定义。你在代码里手动播放声音、手动震动的做法，在通知场景里基本属于画蛇添足：渠道已经是这套体验的"设置中心"。你唯一要做的是给渠道选对级别，剩下的交给系统和用户的偏好。除非有非常特殊的场景需求，别绕过渠道自己造声音。

##### 通知的五种结局：发了不等于送达

站在用户那边看，一条通知有五种结局：正常弹出被看到、被点开、被划掉、根本没弹（权限或渠道被关）、看到了但无感。对开发者有意义的洞察是：前两种说明通知在干活，第三、五种说明它在消耗信任，第四种说明管道断了。别只统计"发了多少条"——那是在奖励自己；要看"点开率和划掉率"：那才反映用户的态度。划掉率悄悄上涨，通常意味着通知内容和时机出了问题，先于评分崩掉自查。

##### Repository 到底是什么：一个具体的样子

架构表里 Repository 出现频率最高，但它对新手来说最抽象。把它具体化：Repository 就是一个普通类，里面装着"怎么取数据、怎么存数据"的全部细节，对上只暴露干净的方法。记账本的样子大概是：<code class="inline">getAllRecords()</code> 返回记录列表、<code class="inline">insert(record)</code> 存一条、<code class="inline">getMonthlyStats(month)</code> 算月度统计，ViewModel 只认识这三个方法，至于背后是 Room 数据库、是文件、还是将来的远程接口，ViewModel 一个字都不用知道。

这层封装的价值在"换数据源"那天兑现：哪天你想给记账本加云同步，改的是 Repository 内部，ViewModel 和界面一行不动，这就是"改一处不牵连三处"最典型的兑现场景。写 Repository 时给自己立一条规矩：它对外的方法参数和返回值里，不要出现 Room 的类型、网络库的类型，只出现你自己的数据类。守住这条，封装就守住了。

##### 一段"泥球"代码的重构：动手感受分家

光说不练感受不深，来重构一段典型的泥球。设想保存按钮的回调里现在躺着四十行：读输入框、转数字、开数据库、写记录、重新查询。更新列表、弹提示。按三步分家。第一步，数据操作搬进 Repository：开库、写库、查询这三段变成 repository.insert(...) 和 repository.getAllRecords()；第二步，编排搬进 ViewModel：保存按钮的回调里只剩一行 viewModel.addRecord(amount, note)，四十行里剩下的逻辑进了 ViewModel 的方法，方法内部更新 StateFlow。第三步，界面只渲染：列表从 uiState 里读，提示根据状态显示。三步走完，原来那四十行泥球变成了三段各司其职的代码，每一处都能被单独测试。

自己做一遍这个练习（拿你记账本的任何一个页面），比读五篇架构文章都有用。做完你会得到一个副产品：知道"搬到哪里去"的手感：这份手感，就是后面看懂 Hilt、模块化这些"进阶名词"的地基。

##### 状态如何到达界面：最后一公里

还剩最后一公里没讲：ViewModel 里的 StateFlow 怎么变成界面上的画面？Compose 里有现成的桥：<code class="inline">collectAsState()</code>（或官方生命周期库提供的生命周期感知变体），它把 StateFlow 变成一个 Compose 可观察的状态：流里发新值，界面自动重组。于是在界面里你只写一行：
<code class="inline">val state by viewModel.uiState.collectAsState()</code>
然后整页照着 state 渲染。数据从"存的地方"一路流到"画的地方"，中间每一站都清清楚楚。

把整条链路背下来：

1. 数据库变化
2. Repository 发出
3. ViewModel 合成 UiState
4. StateFlow
5. collectAsState
6. Compose 重组

将来调试任何"界面没刷新"的问题，就顺着这条链一站一站查，数据在哪一站断了，问题就在哪一站。架构图不是装饰，它是排查问题的路线图。

#### 四、2026 年的新玩法：AI 辅助安卓开发

2026 年，AI 已经深度嵌入安卓开发流程。如果你想提速，这套组合拳很成熟：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">环节</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">AI 怎么帮</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">你的职责</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">写代码</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio 内置 Gemini/第三方 AI 插件补全与生成</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">描述清楚需求，审查产出</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">查资料</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把官方文档和报错信息丢给 AI 解读</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">关键结论回官方文档核实</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">写测试</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">让 AI 按"正常/边界/异常"三类生成用例</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">确认用例符合业务语义</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">改 bug</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">贴堆栈 + 相关代码，AI 定位修复</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">看懂改动，跑测试验证</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
AI 辅助安卓开发的四个场景

具体方法论，怎么给 AI 下指令、怎么验收、怎么避坑，完整的 11 章内容在本书第七篇《AI编程实战篇》（第37-47章）里，强烈建议配合阅读：<strong>安卓语法交给本篇，AI 协作的心法交给第七篇</strong>。

##### 给 AI 下指令的安卓专用模板

安卓语境下的提问有一套趁手的模板。要界面，把约束说全："用 Compose 实现一个记账列表页，状态来自 ViewModel 的 StateFlow，列表加 key，先给代码再给说明"，技术栈、数据来源、注意事项全在指令里，产出质量立刻不一样。要测试，把边界情况列出来："给 parseAmount 写单元测试，覆盖空串、全角数字、超大数、负数"。要改 bug，把"完整堆栈 + 相关代码 + 复现步骤"三样一起给，别只贴一行报错。

模板的共同点是<strong>把上下文喂足</strong>。AI 不知道你的项目用什么架构、哪个版本、什么约定，你不说它就按"大众默认"来，大众默认常常和你对不上。指令多写两行，返工少花两小时，这笔账很好算。

##### AI 产出最常见的三种坑与验收

- <strong>过时的 API</strong>：训练数据里存着旧写法，比如用老的方式处理权限和通知，验收动作是核对当前官方文档。
- <strong>编造的 API</strong>：一本正经地写出不存在的方法名，验收动作是让代码真的编译一遍，编译器是第一道关卡。
- <strong>永远通过的测试</strong>：断言写得不对，测试挂不出真问题，验收动作是把被测代码故意改错，看测试会不会红。

三个验收动作有一个共同的底层逻辑：不信任"看起来对"，只相信"验证过的对"。AI 把写代码的成本降了十倍，但验证的责任一分没少，它转移到了你身上。

##### 什么时候别用 AI

也有几类场景，劝你先自己来。学基础语法时，手写一遍大脑才记得住，AI 代写等于把练习题外包了；权限和隐私这类"边界敏感"的决策，AI 给的是通用答案，你的 App 该要哪个权限取决于你的产品，这题只有你能答；还有调试的思路本身，上一章教的二分定位，是肌肉记忆，外包出去就长不出来了。AI 是加速器，不是替身：加速你已经会做的事，别替你做还不会的事。

##### 把 AI 变成代码评审员

AI 还有一个被低估的用法：让它当你的评审。提交前把权限申请那段代码贴给它，问三个问题："这个四分支逻辑有没有漏洞？用户永久拒绝后的路径走得通吗？有没有把授权状态缓存成永久状态？"它会像找茬一样列出一堆"可能的问题"，大部分无关紧要，但十个里有一两个真的命中，就值回票价。

用它的产出时留个心眼：AI 评审给的是"清单"，不是"结论"。它指出的每一条你都要自己过一遍脑子，确认是真问题就修，是误报就忽略。评审的价值在于多一双眼睛，不在于免你自己思考。反过来，把你的代码让它解释一遍（"逐行讲讲这段在干嘛"）也是个好习惯：AI 讲不通顺的地方，往往就是你逻辑含糊的地方。

#### 五、Compose 性能优化与调试工具

Compose 写起来爽，但"重组过多"也会卡。三个实用技巧：

- <strong>稳定参数</strong>：给数据类加 <code class="inline">@Immutable</code> 或使用 <code class="inline">derivedStateOf</code>，避免无关状态变化触发大面积重组。
- <strong>记得用 key</strong>：<code class="inline">items(list, key = { it.id })</code> 让列表增删时只动该动的项，不加 key，删除一项可能整表重画。
- <strong>Layout Inspector 的 Compose 模式</strong>：实时看每个 Composable 的重组次数，谁频繁重组一目了然，照着热点优化。

另外把 <code class="inline">Compose 编译器报告</code>（Metrics）打开，能生成一份"哪些组件不稳定"的报告，进阶路上，数据永远比感觉可靠。

##### 先懂重组，再谈优化

上面三个技巧都建立在同一个概念上：重组（recomposition）。Compose 的界面是"状态到界面"的函数，状态一变，相关组件重新执行一遍、画出新界面，这个重新执行就叫重组。它本身不慢，慢的是"该只重组一个小组件时，整页都跟着重跑"。什么时候会整页重跑？通常是你传进去的数据类型"不稳定"，Compose 无法确认两个对象是否相等，干脆全量重画。所以优化的第一性原理是：让传给组件的参数类型稳定、明确。

新手不建议背稳定性规则，规则很长还随版本变。实操路径是：先用 Layout Inspector 看重组次数，谁在无意义地狂重组，就针对谁查参数类型：工具指哪，你打哪，比背规则省力得多。

##### 列表性能的两个动作

列表是最容易出性能问题的地方，两个动作值得养成习惯。动作一，永远给 items 加 key（上面正文说过），key 的本质是告诉框架"这条数据的身份是什么"，增删时只动该动的行；不加 key，删掉中间一项，后面所有行都可能重画。动作二，别在列表项里做重计算：每一项渲染时都要现算的格式化、排序、过滤，应该提到 ViewModel 算好一次，界面只拿结果。这两条做完，大多数列表卡顿就消失了；剩下的，交给 Profiler 说话。

##### 从"感觉卡"到"哪里卡"：Profiler 实操

上一章把 Profiler 的面板讲过了，这里讲在 Compose 项目里的用法。打开 Profiler 连上设备，重点看两样：CPU 曲线和"掉帧"提示。滚动列表时 CPU 频繁打满。多半是重组过热或列表项太重；点击响应偶尔僵一下，八成有主线程重活。选中一段可疑的时间轴，能看到那段时间里在执行什么方法，"感觉卡"到"哪一行卡"，就是这么一步步逼出来的。定位到热点之后，优化、再录一段对比，前后两条曲线就是你的验收单。

##### 把重组计数用成"仪表盘"

Layout Inspector 的 Compose 重组计数值得单独说一个用法：把它当仪表盘，而不是当事故后的事察工具。做法是开发期就开着它，随手做几个日常操作，切换页面、加一条记录、筛选月份，边做边看哪个组件的计数在"无辜地涨"。健康的状态是：操作哪个功能，就只有相关的组件涨；如果只是打开设置页，列表组件的计数也在飙升，那就是状态串门了，顺着 UiState 的更新链查。把"看重组计数"变成肌肉记忆，性能问题在你手里活不过一天。

##### 内存问题的三个典型症状

内存问题在 Compose 项目里的长相和传统项目一样，认症状就好：一是"越用越卡、重进恢复"，典型的泄漏，界面被谁抓着不放，LeakCanary 上（上一章装过了）看引用链；二是"内存曲线只涨不跌"，集合被塞进去就没人清理，查缓存策略；三是"某个页面一进就涨一大截不回落"：十有八九是在往内存里塞大图或大数据，改成分页加载或用 Coil 这类库做缩放缓存。三种症状对应三种病，别混着治。抓不准就抓一次堆转储，看哪个类的实例数量最离谱，顺着它查。

##### 启动优化入门：别让用户等白屏

启动是性能的第一印象。先把概念分清：冷启动（进程不在了，从头来）最慢，也是用户吐槽的对象；热启动（刚切走又回来）很快，不是优化重点。冷启动慢的常见病因就几个：Application 的 onCreate 里初始化了一堆东西，能懒加载的全懒加载，用到再初始化；首屏就要读数据库或网络，首屏先出框架、数据到了再补，别让白屏替你挡子弹；图标主题配置老式，用官方的 SplashScreen 方案统一启动画面。官方还有基线配置档（Baseline Profiles）这类进阶手段可以再提速，属于"想再抠一点"时的选项，以官方文档为准。改完用 Profiler 的启动记录量一下前后对比，又是那句老话：先测量，再优化。

##### 性能之外的"体验性能"：深色、大字体与低端机

狭义的性能指标之外，还有三样东西决定了用户嘴里"卡不卡、顺不顺"的感受：深色模式下的对比度（不是看不清就是白叫卡）、大字体下的布局（挤爆的界面让人心慌）、低端机上的响应速度（旗舰机永远感觉良好，你的用户不全是旗舰机）。这三样上一章的手动清单已经覆盖，这里补一个视角：它们是"免费的性能优化"，不涉及任何算法，只涉及你有没有在真实条件下看过自己的应用。发布前找一台最旧的备用机开最大字体走一遍，往往比一次 Profiler 会话暴露的问题更多。

##### 把优化变成习惯：发版前的性能走查

性能优化最怕"运动式"，某天被卡顿刺痛了猛搞三天，然后一个月不闻不问。可持续的节奏是把它并进发版流程：每次发布前，用上一章的手动清单加本节的三个动作。花十分钟走查一遍。走查内容固定三样：滚动主列表顺不顺、进出主要页面有没有掉帧、内存曲线涨了会不会落。数据没异常就发版，有异常就地排查，十分钟防住的是上线后几百次"怎么又卡了"的差评。

顺带定一条优化优先级，别在错的地方较劲：崩溃和 ANR 永远第一（功能性伤害），启动第二（第一印象），主列表滚动第三（高频操作），内存第四（慢性病），其余视觉级细节最后。前三项做完，你的 App 已经好过大多数同类了。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：给记账本加"三件套"

{class="mt-1"}
① 给记账本加"每天 20:00 记账提醒"（WorkManager + 通知渠道 + Android 13 通知权限）；② 把数据库和 API 的创建改成 Hilt 注入；③ 试着用 AI 工具让"月度筛选"功能提速实现，然后按三层验收法检查产出。三件套做完，你的项目就有"正规军"的样子了。
:::

#### 六、实战串联：给记账本加上"每晚八点提醒"

这一章的前半教了权限，中间教了通知和 WorkManager，现在把三样串成一个真实功能：它就是"来动手"三件套里的第一件，带你走完一遍。目标：每天晚上八点提醒用户记账。先把边界想清楚：这不是闹钟，晚几分钟用户能接受，所以 WorkManager 合格（必须准点的场景才升级 AlarmManager，判断标准在第二节）。

1. 建渠道：启动时确保"记账提醒"渠道存在，importance 给 DEFAULT：提醒不响铃也能看到。
2. 申请通知权限：设置页放一个"开启记账提醒"入口，点开后先讲价值再调 launcher（第一节的话术和四分支逻辑）。
3. 写 Worker：一个继承 Worker 的类，doWork 里检查通知权限、构造通知（第二节的完整版带 PendingIntent 和 AutoCancel）、用 NotificationManager 发出。
4. 注册周期任务：用 enqueueUniquePeriodicWork 注册每天一次的唯一任务，策略用 KEEP：已存在就不重建，防止重复提醒。
5. 测试：把周期间隔临时改成最短档在模拟器上验证流转，确认通知弹出、点击能进记账页。
6. 还原并收尾：改回一天一次，写进发布文档的"本次变更"段。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 注册每日提醒（示意）</span><span class="dots">···</span>
:::

```
class ReminderWorker(context: Context, params: WorkerParameters) :
    Worker(context, params) {
    override fun doWork(): Result {
        // 复用第二节的通知代码：查权限 → 构造通知 → 发出
        return Result.success()
    }
}

val request = PeriodicWorkRequestBuilder&lt;ReminderWorker&gt;(1, TimeUnit.DAYS).build()
WorkManager.getInstance(context).enqueueUniquePeriodicWork(
    "daily_reminder",          // 唯一名字，防止重复注册
    ExistingPeriodicWorkPolicy.KEEP,
    request
)
```
:::

两个容易踩的细节提前告诉你。周期任务的最短间隔有系统限制（具体数值以官方文档为准），调试时想"每分钟弹一次"是做不到的，用临时缩短加日志的方式验证逻辑就好；任务在设备重启后依然有效，WorkManager 会把任务持久化，这正是"别自己造轮子"的理由之一。这个功能做完，权限、通知、调度三套知识就真的长在你手上了。

##### 验收清单：这个功能"做完"的标准

判断提醒功能算不算做完，用这张清单说话：权限被拒时设置页入口可用；通知渠道在系统设置里名字正确、级别正确；点击通知能进记账页并自动消失；任务重启手机后依然生效；把时间临时改短测完已经还原。五条全勾才叫做完，"功能在我手机上跑通了一次"和"功能做完了"是两回事，这张清单就是把它们区分开的尺子。

#### 七、FAQ：权限、通知与架构的十七个问题

<strong>问：为什么别的 App 不申请通知权限也能发通知，我的就要弹窗？</strong><br>答：和应用"声明的目标系统版本"有关——不同目标版本在不同系统上的默认行为不一样，用户升级系统前装的老应用也有过渡规则。别对着别人 App 的表现猜规则，以官方文档关于通知权限的说明为准，然后按"两道闸门"的思路把自己的权限和渠道逻辑写规范。

<strong>问：用户拒绝了通知权限，我的提醒功能是不是就废了？</strong><br>答：系统通知发不出，但 App 内的提醒可以照常存在——应用内的提示条、设置页的红点都不占系统通知的额度。设计上让"提醒"这个功能不依赖单一通道，用户拒了通知，体验降级但不断供，哪天他想要了，入口一直在设置页等着。

<strong>问：ViewModel 里到底能不能用 Context？</strong><br>答：能不用就不用。ViewModel 活得比界面久，抓着界面级的 Context 会造成泄漏（上一章 LeakCanary 逮的典型）。真要用，用 Application 级别的 Context，并且想清楚"这个功能是不是应该挪到 Repository 或工具类里去"。把"ViewModel 里出现 Context"当成代码异味的信号，通常没错。

<strong>问：Hilt 会不会拖慢编译或者启动？</strong><br>答：它在编译期生成注入代码，不走运行时反射，对启动速度的影响通常可以忽略；编译时间会有所增加（多了代码生成环节），换来的是"接线错误在编译期暴露"。具体量级随项目而异，别拿感觉当结论——真在意就用大项目前自己量一次。以官方文档说明为准。

<strong>问：MVVM 和 MVI 那些流派之争，我要不要站队？</strong><br>答：不用。流派的分歧在"状态怎么组织、事件怎么收"，但共同内核就是你学过的单向数据流——事件往下、状态往上、状态单一入口。先把内核用熟，之后无论项目用哪个流派，你看代码的眼光都是通的。神化流派名字的人多，把数据流写干净的人少。

<strong>问：WorkManager 的任务，手机重启之后还在吗？</strong><br>答：在。WorkManager 会把任务持久化，设备重启后自动恢复——这正是"提醒类需求放心交给它"的重要理由，也是别自己起常驻服务硬扛的理由之一。要注意的反而是别重复注册：用唯一名字加 KEEP 策略（第六节的做法），任务就只会有一个。

<strong>问：精确闹钟权限（如果我要做准点提醒）被用户拒了怎么办？</strong><br>答：降级到非精确模式继续工作，并在界面上温和说明"准点提醒未开启，提醒可能稍有延迟"。功能不瘫痪、不反复纠缠，用户哪天在意准点了，自己去设置里打开。任何权限的申请失败都适用这个套路：降级 + 说明 + 入口，三件套。

<strong>问：老项目全写在一个 Activity 里，值得重构成 MVVM 吗？</strong><br>答：别"全量重构"，那是新手最容易掉进去的大坑。策略是"新页面新写法，旧页面按需搬"：以后新加的功能一律 MVVM；旧代码在你需要改它时，顺手把要改的部分抽到 ViewModel。三个月后你会发现，最常被改的代码已经全是新写法了——重构跟着需求走，不跟着热情走。

<strong>问：通知渠道建几个合适？会不会越多越好管理？</strong><br>答：按"用户想单独关什么"来划，通常三五个足够。渠道泛滥（十几个渠道各管一条消息）反而让用户在设置页里迷路，最后选择一刀切——和你的初衷相反。宁可粗一点，也别细到切碎。

<strong>问：AI 能帮我看懂官方文档吗？</strong><br>答：能，而且是很推荐的用法——把文档段落丢给 AI，让它用大白话解释、举适合你项目的例子。但两条纪律别破：关键结论（版本行为、参数含义）回原文核对；例子要真跑一遍。AI 解读文档省的是"翻译时间"，省不掉"验证责任"。

<strong>问：通知的小图标有什么讲究？随便放个图行不行？</strong><br>答：不行。小图标在状态栏和通知栏里只有一小格空间，要求是单色线条风格的图形资源，彩色照片或大图标放进去要么显示成色块要么丑得惊人。做法：用图标编辑器做一套单色图标，或用现成的图标素材库挑一个。通知头图（大图标）另算，那是 setLargeIcon 的事，两者别混。

<strong>问：横幅提醒和普通通知栏，谁来决定表现形式？</strong><br>答：渠道的 importance 等级决定默认形态（HIGH 走横幅、LOW 静默进栏），用户还能在系统设置里对每个渠道再改一档。你只能"建渠道时定调"，之后的表现是"系统按渠道配置执行"——想改形态就是改渠道配置或让用户自己改，别想着绕过渠道硬控表现。

<strong>问：ViewModel 一多，会不会比泥球还乱？</strong><br>答：会的，如果没有边界。判断要不要拆分 ViewModel 的依据是"页面之间要不要共享状态"：一个页面独享的状态就放它自己的 ViewModel；几个页面共享的（比如全局设置），提到更高层或放进 Repository 管理的数据。原则还是那条——状态单一写入口，写入口在谁那里，谁就是它的主人。

<strong>问：权限我都如实申请了，商店还是退"权限与用途对不上"，怎么办？</strong><br>答：多半是"解释"环节没跟上——你申请了，但没让审核和用户都看到用途。检查三处：应用内申请时的解释文案有没有、商店描述里有没有提到相关功能的说明、数据安全表与权限清单是否一致。补齐后重新提交，退回意见里通常会写明它认为哪一项"对不上"，照着那一项改就行。

<strong>问：我照着老教程写的权限代码，在新手机上行为不一样，是教程错了吗？</strong><br>答：多半不是教程错，是"版本错"——老教程写于旧版本的权限语义。看它教的是哪个年代的行为（第十一节有一份演进速览），再用当前官方文档对一遍同样的主题。教程没教错当年的规则，只是规则变了；这也是为什么本章反复强调"骨架不变、细节查文档"。

<strong>问：ViewModel 的方法该设计成什么样？直接把整个记录对象传进去吗？</strong><br>答：可以，但注意"谁来校验"。界面的职责是收集输入，ViewModel 的职责是校验与编排——金额合法性这类检查放 ViewModel（它也是单元测试最容易覆盖的地方），界面别自己偷偷校验一遍导致两处规则。方法名照业务语义起（addRecord 而不是 onButtonClick2），将来读代码的人会感谢现在的你。

<strong>问：提醒类通知，用户反馈"有时晚半小时才来"，怎么向用户解释？</strong><br>答：照实说：系统为了省电会把可延迟任务安排在合适的时机执行，提醒可能略有延迟；如果某类用户必须分秒不差，引导他们了解精确闹钟选项。诚实的解释比"我也不知道"体面得多——用户能接受系统的省电逻辑，接受不了装糊涂。

#### 八、误区清单：七个流行但不成立的认知

- <strong>很多人以为"权限要得越多，功能越强"</strong>，其实权限清单是用户卸载决策的重要依据：要得越多，装机越少、审核越严，能用普通权限和系统组件解决的事就别申请危险权限。
- <strong>很多人以为"通知发得越多，用户越活跃"</strong>，其实通知的打开率会随频率迅速衰减，超过阈值后每一发都在净消耗信任，克制不是善良，是策略。
- <strong>很多人以为"架构层数越多越专业"</strong>，其实每一层都是维护成本，能"改一处不牵连三处"的最小结构就是好结构，层数是结果不是目标。
- <strong>很多人以为"Hilt 要从项目第一天就上"</strong>，其实手动依赖注入撑单人项目绰绰有余，工具跟着痛感走，痛感没到就上工具，学会的是工具不是架构。
- <strong>很多人以为"性能优化就是靠感觉和经验"</strong>，其实Profiler、重组计数、堆转储全是现成的测量工具，感觉说"这里慢"，数据说"那里慢"，听数据的。
- <strong>很多人以为"AI 能替我决定权限和隐私策略"</strong>，其实权限决策是你的产品决策，AI 能告诉你技术上有几种做法，选哪种、为什么选，只有了解你用户的你能答。
- <strong>很多人以为"通知和小组件越多越显得功能丰富"</strong>，其实每多一个打扰渠道就多一分卸载风险：功能丰富靠核心体验撑，不靠提醒的数量撑。

#### 九、给三类背景读者的进阶路线

<strong>学生</strong>：这一章的内容是简历上"项目亮点"的原料。面试里"我处理了 Android 13 的通知权限降级""我用单向数据流重构了列表页，重组次数降下来了"这类句子，比"我熟悉安卓开发"有力得多。路线建议：把记账本按这一章升级完，然后写一篇技术复盘，截图放重组曲线和崩溃数据——复盘本身就是应聘作品。

<strong>想转行的上班族</strong>：你的独特任务是"读懂别人的代码"。公司里的老项目不会是教科书式的 MVVM，你需要的是这一章给的眼力：一眼看出状态在哪、事件怎么流、依赖谁创建谁。路线建议：用记账本练手升级后，找一两个开源安卓项目（官方示例就好）读它的目录结构和数据流，把学到的"分家"模式对号入座。读别人代码的能力，决定你入职后的爬坡速度。

<strong>小商家与自由职业者</strong>：诚实的建议是——这一章你只需要前两节。权限和通知决定你的小工具"贴不贴心"，架构和性能优化对你的规模属于"以后再说"。路线建议：把记账提醒做出来给自己用，通知的礼仪清单照着执行；架构那节留着，等你的工具有第二个用户开始提需求时再回来看。

三条路线的交集还是那句老话：这一章的所有东西都值得"做完一遍"而不是"看懂一遍"。权限的四分支、通知的两道闸门、数据流的一个圈，做完了，它们才是你的。

最后送三类读者每人一句叮嘱。学生：别急着把本章名词全堆进简历，做一个、懂一个、讲得清一个，比罗列十个名词有力。转行的：老代码里的"为什么这么写"往往有历史原因，先问再改，架构洁癖要给现实让半步。小商家：你的用户是你的熟客，他们提的意见比任何"好办法"都优先：这一章的纪律帮你守住底线，底线之上听用户的。

#### 十、错误示范：一次"权限轰炸"引发的卸载

再来一个反面教材。小周给记账本 2.0 加新功能，上线前把权限申请写成了"保险起见"：启动页连续弹相机、通知、定位三个系统弹窗，理由一句话没说。他自己测着挺顺，权限都给了嘛。结果第一批用户里，不少人压根没看到主界面就在弹窗阵里卸载了，商店评论区多了一条一星："还没用上就要一堆权限。"

复盘他的三个错误，正好对应第一节的黄金三条。第一个错误，启动即申请。三个权限没有一个是"此刻有用"的；第二个错误，连环弹窗，一次一个都嫌多，一次三个等于逼用户做排列组合题；第三个错误，零解释：系统弹窗之外，他自己的 App 没说一个字"为什么要"。

改法照表执行：相机挪到"进入拍照凭证页"那一刻申请；通知挪到用户开了几天账、在设置页看到"开启提醒"入口时申请；定位干脆砍了，地点标签是伪需求。手填一个"备注地点"覆盖了九成场景。改完之后授权率明显回升，差评也没再出现。这一课的浓缩版就是：权限是用户递给你的信任，不是你伸手要来的资源。

给自己的权限设计留一道自查题，每次加新权限时问三句：这个权限对应的功能是核心还是锦上添花？能不能用系统组件绕开？被拒绝了 App 会坏成什么样？三问答完再动手，"权限轰炸"这类事故就离你很远。

#### 十一、版本演进速览：为什么老教程总教错

权限和通知大概是全网教程"过期率"最高的两个主题，你在旧教程里看到的代码，很可能在今天的系统上行为完全不同。给你一份"哪年变了什么"的速览，看完你就知道旧教程错在哪：Android 6 引入运行时权限（从此不能再"声明即拥有"）；Android 8 引入通知渠道（从此必须先建渠道）；分区存储在 Android 10、11 逐步收紧（从此不能随便读外部存储）；Android 12 把蓝牙相关权限归入"附近设备"、精确闹钟开始需要声明；Android 13 通知本身也要运行时权限了。再往后的变化，以官方文档为准。

这份清单的用途有二：读老代码时，先对一下它写于哪个版本语义；搜教程时，先看发布日期和提到的系统版本。安卓的权限模型只紧不松：凡是"更简单了"的权限教程，都要多一分警惕。不是某个版本的细节，是"声明—申请—解释—降级"这套骨架，骨架不随版本变。

最后补一句这份清单的用法：它不是让你背年份。它是让你建立"版本直觉"，看到一段教程代码，先问它写于哪个版本语义；看到一次行为差异，先怀疑版本差异而不是怀疑人生。安卓的权限模型只在紧的方向上演进，记住这个大势，遇到具体差异去官方文档对号入座，就永远不慌。

#### 十二、下一步地图：从这一章往后学什么

这一章把你从"会做"推向"做好"，往后还有两条路可走。第一条是横向扩展：数据同步（多设备）、加密存储、小组件、桌面快捷方式这些"让 App 更像产品"的能力，官方文档和 Codelabs（谷歌官方的免费实操教程）里每一样都有现成的入门路径，按需取用。第二条是纵向加深：把这一章的每个主题往深挖一层，协程的取消与异常、Flow 的操作符、Room 的迁移、Compose 的自定义布局，每样都值得独立的一周。

选哪条路，判断标准还是那个：你的记账本下一步最需要什么。缺同步就横向，某块代码让你写得难受就纵向。跟着自己项目的真实需求走，永远比跟着"进阶清单"走学得快。官方文档、官方示例、Codelabs 三件套收藏好，它们是这条路上一辈子都在更新的地图。

无论选哪条，都有一个小建议：学新东西时继续用记账本当练习场：同步就给记账本加多端、加密就加密记录、小组件就做"今日支出"桌面插件。学以致用的项目你已经有了，别再为每个新主题另起炉灶，一个应用养所有知识，知识也会反哺这个应用。

#### 十三、通知进阶实战：给记账本加上"月度周报"

第六节做了"每晚提醒"，现在做第二个通知功能：每月 1 号发一条上月统计（记了多少笔、总支出、最大的一笔）。这个练习的新考点是：低打扰渠道和大文本样式。设计决策先摆出来：它属于"回来看就行"的内容，importance 用 LOW，静默进通知栏，绝不横幅；内容超过一行，用 BigTextStyle 展开显示；单独一个"月度报告"渠道，和每日提醒分开，用户可能想关提醒留周报，也可能反过来，分开才给得了这种自由。

1. 建"月度报告"渠道，importance 选 LOW。
2. Worker 里查上月数据：日期计算放 Repository，别在 Worker 里现写日期逻辑（它是该被单测的纯逻辑，上一章讲过）。
3. 组通知：标题"你的 X 月记账报告"，正文摘要一句，BigTextStyle 放明细。
4. 点击去向：跳到统计页（PendingIntent 指向对应界面）。
5. 调度：每月 1 号的周期任务，同样用唯一名字加 KEEP 策略。
6. 验收：临时缩短间隔测试流转，确认无声弹出、内容完整、点击跳转正确，再还原。

做完这两个通知功能，回头看你会发现自己实践了通知教程的全部要点：渠道划分、importance 分级、权限两道闸门、PendingIntent、展开样式、WorkManager 调度。通知这一课，到这一步就算真正出师了。

两个通知功能放在一起看，还有一层产品视角的收获：每日提醒和月度报告服务的是两种完全不同的心理：前者是"催你做事"，后者是"帮你复盘"。一个 App 的通知体系里最好两种都有、比例以"复盘类"居多：催的多了是负担，复盘的多了是价值。给每个新通知功能归类时先问一句"这是催，还是帮"，答案往往就决定了它的渠道级别和频率。

#### 十四、调试通知的三个小技巧：不用等到晚上八点

通知的调试有个天然麻烦：定时任务要等到点才跑，一次调试等一天。三个技巧把等待去掉。第一条，调试期间把 WorkManager 的周期临时改短（在系统允许的最短间隔内），验证完整流转后改回来，别忘了改回来，这种"临时改动忘还原"是通知功能上线事故的经典来源；第二条，把 Worker 里的业务逻辑抽成一个普通函数，先用单元测试直接调它验证通知内容，不用等调度。第三条，给 Worker 的 doWork 加日志，Logcat 里看它到底跑没跑、跑到了哪一步，"没收到通知"十有八九是权限或渠道被关了，日志一翻便知。

还有一个验证思路值得养成：真机测一遍深色模式下的通知样式、再测一遍免打扰模式下的表现，不同系统环境下通知的呈现差别不小，以真机为准，模拟器只能算参考。

#### 十五、权限与通知自检清单（一页版）

把本章前半压成一页纸，发版前逐条过：

- 每个危险权限：Manifest 声明了、代码里运行时申请了、界面上解释过用途。
- 权限申请全部发生在"用到的那一刻"，没有启动即弹窗、没有连环弹窗。
- 四分支逻辑齐全：已授权、拒绝过、从未问、永久拒绝，各有一条路。
- "仅本次允许"和"系统自动收回"两种状态下，功能都能体面恢复。
- 每个权限被拒后的降级方案存在且可用（"权限残缺测试"做过）。
- 没有申请任何与应用核心功能无关的权限，没有碰特殊权限。
- 通知渠道按类别划分，名字用户能看懂，importance 从低配置。
- 通知权限申请有"价值预告"，拒绝后设置页留有入口。
- 每条通知都有点击去向、会自动消失、内容说人话。
- 定时提醒确认了 WorkManager 与 AlarmManager 的选型理由，任务不会重复注册。
- 权限与通知的文案进了 strings.xml，没有硬编码在代码里。

#### 十六、文案也要本地化：把弹窗和通知的话术搬进 strings.xml

本章给了不少"话术"，申请权限的解释、通知的标题正文。工程上它们该住在哪？答案是资源文件：字符串统一放 <code class="inline">strings.xml</code>，别硬编码在代码里。好处立竿见影：改文案不用动代码；想做多语言时，加一个翻译目录就能整套替换；商店审核问你权限用途，你还能把这套文案直接甩给审核看。文案写完做一次"读出声测试"，拗口的句子在弹窗里格外刺眼，念不顺就重写。

再进一小步：文案的语气要有"产品人格"。记账本这种天天见面的工具，话术可以亲切一点——"今天还没记账哦"就比"您有一条待处理记账任务"舒服得多。语气定下来就全 App 统一，别有的页面卖萌有的页面公事公办。这类细节用户说不出但感受得到，攒起来就是"这个 App 有人味"的整体印象。

#### 十七、一次代码评审实录：AI 和我互查权限代码

来一场真实的评审，看看"AI 当评审员"怎么落地。我把记账本的权限四分支代码贴给 AI，让它找漏洞。它列了五条，我逐条过了一遍：第一条"shouldShowRationale 为 false 且未授权时，无法区分首次和永久拒绝"，真问题，我确实没记 askedBefore 状态，采纳；第二条"建议在 onCreate 里预申请所有权限"——伪问题，正好踩了我们反对的"权限轰炸"，忽略；第三条"授权状态可以缓存到 DataStore 避免重复检查"：半真半假，缓存省的那点检查不痛，但缓存会让"仅本次允许"和"自动收回"失效，不采纳；第四条"跳设置页的 Intent 建议加包名限制"，采纳，顺手的事；第五条"通知权限也该走同一套四分支"，采纳，本来就该复用。

一场评审下来，五条意见采纳三条、忽略两条。改动十来行。注意这个过程里做判断的是谁：AI 提清单，你做裁决。评审能力是这样长出来的，见得多（它有库存）、判得准（你有上下文）。把这次评审的三个采纳项记下来。你的"发布文档"又厚了一页。

#### 十八、本章知识地图：一张表串起四个主题

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">主题</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">核心纪律</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">一句话记牢</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">权限</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">声明按需、申请按场景、解释说人话、拒绝有退路</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">权限是增强，不是前提</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">通知</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">渠道分类、级别从低、点击有去向、深夜不响</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">通知是敲门，有事才敲</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">调度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可延迟交给 WorkManager，必须准点才上 AlarmManager</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">别自己造后台轮子</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">架构</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">事件往下、状态往上、状态单一写入口</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">改一处不牵连三处就是好架构</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">性能</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">先测量再优化，优先级：崩溃 &gt; ANR &gt; 启动 &gt; 滚动 &gt; 内存</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">感觉说慢不算数，数据才算</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI 协作</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">上下文喂足、产出必验证、敏感决策自己拍板</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI 加速你会的事，不替你学不会的事</td></tr>
</tbody>
</table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
权限、通知、架构、性能、AI 协作的一页总览

这张表和上一章末尾的速查表凑成一对：那章管"用什么工具"，这章管"守什么纪律"。工具和纪律都有了，你的项目就同时具备了"跑得起来"和"活得下去"的两条腿：接下来往哪个方向深入，照第十二节的地图按需取用就好。

这张表还有个复盘用法：每做完一个版本，对照六行各问一次"这一行的纪律我守了吗"。哪一行答不上来，就回对应章节补课，知识地图的用途不是装饰目录，是当检查表。

#### 十九、给"已有老代码"的渐进式升级手册

如果你的记账本（或任何项目）已经按前面几章写了不少"不分家"的代码，怎么往本章的架构迁移？答案不是推倒重来，是渐进手术，四条规则。第一条，跟着改动走：下次要改哪个页面，就顺手把那个页面的逻辑抽进 ViewModel。改动是最好的重构时机，没改动就没必要动。第二条，先立测试再动刀：重构前给要搬的逻辑补几条单测（照上一章的做法），搬完测试还绿，才证明搬对了。第三条，每次只搬一层：这周把数据操作搬进 Repository。下周再搬业务进 ViewModel，一口气全搬等于给自己埋雷。第四条，保持能跑：每次手术做完立刻运行验证，"大手术攒到最后一起验"是新手灾难的高发区。

按这个节奏，一个月后你的项目就会"悄悄地"变成 MVVM，没有 dedicated 的重构周，没有停摆的进度，代码却一天比一天清爽。渐进式迁移的精髓就一句话：让重构跟着需求走，需求是车，重构是顺路捎的货。

迁移期还有一个心态提醒：别追求"一步到位的完美架构"。搬进 ViewModel 的代码可能一开始还带着老习惯，没关系，先让它"有家"，再慢慢"装修"。结构的改善是几十次小步迭代的结果，不是一次大爆炸式的重写，后者往往以"改到一半放弃了"收场。

#### 二十、常见报错速修：权限、通知、Hilt 三类高频问题

这一章的知识点各有几条"必踩"的报错，提前给你排雷手册。权限类：申请了权限但没在 Manifest 声明，运行到申请那行直接异常，报错信息会点名权限名，回 Manifest 补声明即可；跳设置页的 Intent 写错，页面打不开，先在真机上单独验证跳转，再接进降级流程。通知类：notify 报错说没设置小图标，补 setSmallIcon；通知发了看不见，按"权限闸门、渠道闸门"两层排查；PendingIntent 在新系统上要求显式可变性，没写 FLAG 会运行时崩溃，统一加 FLAG_IMMUTABLE。Hilt 类：编译报"缺少绑定"（missing binding 一类的提示），几乎总是某个类没标 @Inject constructor、或者你改不了的第三方类没写 @Module 说明书；Application 忘了标 @HiltAndroidApp，整套机制静默失效，ViewModel 注入失败时第一个查它。

排雷手册的正确用法是"遇到时回来看"，不是提前背。所有报错的通用解法还是上一章那套：读完整异常信息、定位到自己包名的第一帧、缩小范围修掉。三类高频问题的价值在于让你知道"这些坑踩过的人很多"，别怀疑自己。

#### 二十一、把三件套排进两周日程

"来动手"的三件套（提醒功能、Hilt 注入、AI 提速月度筛选）值得排进日程，给你一份两周排期。第一周：第 1-2 天做通知渠道与权限申请（本章第一节、第二节），第 3-4 天做 Worker 与调度（第六节），第 5 天按验收清单走一遍并修问题；第二周：第 1-2 天按手动依赖注入整理容器（第三节），第 3 天换装 Hilt（如果痛感到了），第 4-5 天用 AI 提速月度筛选并按三层验收，顺手跑一遍全量测试。

两周的量按每天一小时估的。日程表存进日历，比"有空就做"靠谱十倍——这一章的所有知识，最后都要落到"做"上才生效。做完三件套，你的记账本就不再是练手项目，而是一个有权限设计、有通知体系、有架构骨架的正规应用：下一章，我们聊的是把它变得更值得被更多人用的那些事。

排期时给自己留一个"缓冲日"：两周日程里必然有一天会被现实打乱，模拟器抽风、临时加班、报错卡住。预留的那一天就是安全垫，别把它排成"提前完成日"。日程的意义不是逼你冲刺，是让进度可见：每天一小时，两周后一个功能从无到有，这个确定性本身就是继续做下去的燃料。

#### 二十二、六周复盘：从泥球到"正规军"的一次完整演进

把本章的所有动作装回一条时间线，给你一个"别人家"的完整样本。第一周，权限体检：按对照表清点所有权限，砍掉伪需求，给保留项补齐四分支和解释文案，变化是弹窗从三个降到两个，且个个出现在该出现的地方。第二周，通知翻新：渠道拆分、级别调低、话术重写。变化是划掉率回落，设置页多了两个用户能看懂的渠道。第三周，提醒上线：WorkManager 加每日提醒加验收清单，变化是有了第一个"主动服务"的通知功能。第四周，数据分家：所有数据库操作搬进 Repository。变化是界面代码里不再出现数据库的名字。第五周，业务归位：主要页面的逻辑进 ViewModel，状态走 StateFlow，变化是改统计逻辑不再牵连界面。第六周，收尾与验证：注入方式理顺、性能走查一遍、全量测试转绿，变化是发布文档里多了一页"架构现状"。

六周里没有一个"停下来重构"的日子，每周照常出新版本。这就是本章想说的一切：权限、通知、架构、性能，全都是"跟着版本走的小步动作"，不是"攒起来大干一场"的工程。六周后的记账本，弹窗更少、通知更贴心、代码更好改：用户看不到你的架构，但用户感受得到架构的结果。

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 敏感权限：Manifest 声明 + 运行时申请 + 被拒后优雅引导
- 通知三纪律：只发有用的、能关、不骚扰；渠道 + 权限缺一不可
- 定时任务用 WorkManager，别自己造轮子
- 最小可用架构：UI → ViewModel → Repository → 数据源，事件往下走、状态往上流
- Hilt 管对象、模块化管代码，单人小项目先别急着上
- AI 辅助四场景：写码、查资料、写测试、改 bug；方法论见第七篇（第37-47章）
:::
