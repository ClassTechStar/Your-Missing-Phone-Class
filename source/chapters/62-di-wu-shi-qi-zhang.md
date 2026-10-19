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
能做出 App 只是开始。这一章聊聊从"会做"到"做好"的几道坎：怎么优雅地申请权限、怎么发通知不讨人厌、怎么把架构再往上抬一层，以及——在 2026 年，怎么和 AI 搭档写安卓代码。每一条都是你在真实项目里马上会遇到的。

#### 一、运行时权限：先敲门，再进门

相机、定位、通讯录、通知……这些"敏感地带"，安卓要求 App <strong>运行时向用户申请</strong>（Android 6 起）。规矩是：先声明（Manifest），再申请（代码），用户拒绝要优雅降级。Compose 里用官方库 Accompanist 的 <code class="inline">rememberPermissionState</code> 最省心：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 运行时权限（Compose 版）</span><span class="dots">···</span>
:::

```
// Manifest 里先声明：
// &lt;uses-permission android:name="android.permission.CAMERA" /&gt;

@Composable
fun CameraButton() {
    val permission = rememberPermissionState(
        permission = android.Manifest.permission.CAMERA
    )
    Button(onClick = {
        when {
            permission.status.isGranted -&gt; openCamera()
            permission.status.shouldShowRationale -&gt; showExplainDialog()
            else -&gt; permission.launchPermissionRequest()
        }
    }) { Text("拍照") }
}
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>注意：被永久拒绝怎么办？

{class="mt-1"}
用户勾了"不再询问"后，<code class="inline">launchPermissionRequest</code> 不会再弹窗。此时应引导用户去系统设置里手动开启（用 <code class="inline">Intent</code> 跳到应用设置页），并在界面里说明"这个权限用来做什么"。态度好一点，用户开权限的意愿会高很多——<strong>申请权限的文案，值得认真写</strong>。
:::

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

定时任务（比如"每天 20:00 提醒记账"）用 <strong>WorkManager</strong>——它是官方推荐的"后台调度管家"，能保证任务在合适时机执行，不用自己操心电池优化。闹钟类需求用它准没错。

#### 三、架构进阶：依赖注入与模块化

项目变大后，两个"甜蜜的烦恼"会找上门：

- <strong>对象创建乱</strong>：每个页面都在自己 new 数据库、new API——用 <strong>Hilt</strong>（依赖注入框架）统一管理，"谁要什么，开口就有人递"；
- <strong>代码堆成山</strong>：单模块项目越改越慢——拆成 <strong>多模块</strong>（app / core / feature-xxx），各功能独立开发、独立测试。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：别过度设计

{class="mt-1"}
Hilt 和模块化都是好工具，但<strong>单人项目先别急着上</strong>。记账本单模块 + 手动创建依赖完全够用。等代码量超过几万行、编译开始变慢、多人协作时，再按需引入。工具是服务目标的，不是用来炫耀的——这也是咱们 AI 编程书里的"简单至上"原则。
:::

#### 四、2026 年的新玩法：AI 辅助安卓开发

2026 年，AI 已经深度嵌入安卓开发流程。如果你想提速，这套组合拳很成熟：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">环节</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">AI 怎么帮</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">你的职责</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">写代码</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio 内置 Gemini/第三方 AI 插件补全与生成</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">描述清楚需求，审查产出</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">查资料</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把官方文档和报错信息丢给 AI 解读</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">关键结论回官方文档核实</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">写测试</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">让 AI 按"正常/边界/异常"三类生成用例</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">确认用例符合业务语义</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">改 bug</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">贴堆栈 + 相关代码，AI 定位修复</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">看懂改动，跑测试验证</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
AI 辅助安卓开发的四个场景

具体方法论——怎么给 AI 下指令、怎么验收、怎么避坑——完整的 11 章内容在本书第七篇《AI编程实战篇》（第37-47章）里，强烈建议配合阅读：<strong>安卓语法交给本篇，AI 协作的心法交给第七篇</strong>。

#### 五、Compose 性能优化与调试工具

Compose 写起来爽，但"重组过多"也会卡。三个实用技巧：

- <strong>稳定参数</strong>：给数据类加 <code class="inline">@Immutable</code> 或使用 <code class="inline">derivedStateOf</code>，避免无关状态变化触发大面积重组；
- <strong>记得用 key</strong>：<code class="inline">items(list, key = { it.id })</code> 让列表增删时只动该动的项——不加 key，删除一项可能整表重画；
- <strong>Layout Inspector 的 Compose 模式</strong>：实时看每个 Composable 的重组次数，谁频繁重组一目了然，照着热点优化。

另外把 <code class="inline">Compose 编译器报告</code>（Metrics）打开，能生成一份"哪些组件不稳定"的报告——进阶路上，数据永远比感觉可靠。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：给记账本加"三件套"

{class="mt-1"}
① 给记账本加"每天 20:00 记账提醒"（WorkManager + 通知渠道 + Android 13 通知权限）；② 把数据库和 API 的创建改成 Hilt 注入；③ 试着用 AI 工具让"月度筛选"功能提速实现，然后按三层验收法检查产出。三件套做完，你的项目就有"正规军"的样子了。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 敏感权限：Manifest 声明 + 运行时申请 + 被拒后优雅引导
- 通知三纪律：只发有用的、能关、不骚扰；渠道 + 权限缺一不可
- 定时任务用 WorkManager，别自己造轮子
- Hilt 管对象、模块化管代码——单人小项目先别急着上
- AI 辅助四场景：写码、查资料、写测试、改 bug；方法论见第七篇（第37-47章）
:::
