---
id: di-liu-shi-ba-zhang
num: 68
part: ios-kai-fa-pian
nav: 第六十八章：进阶之路——权限、通知与现代架构
toc: default
kind: chapter
---

### 第六十八章：进阶之路——权限、通知与现代架构

{class="chapter-intro mb-4"}
能做出 App 只是开始。这一章聊聊从"会做"到"做好"的几道坎：怎么优雅地申请权限、怎么发通知不讨人厌、怎么把架构再往上抬一层，以及——在 2026 年，怎么和 AI 搭档写 iOS 代码。每一条都是你在真实项目里马上会遇到的。

#### 一、权限：先敲门，再进门

相机、定位、通讯录、通知……这些"敏感地带"，iOS 要求 App <strong>在用到时向用户弹窗申请</strong>。规矩是"声明 + 申请 + 优雅降级"三步：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 权限申请（以定位为例）</span><span class="dots">···</span>
:::

```
// 1. Info.plist 里声明用途文案（不声明直接崩溃！）
// Privacy - Location When In Use Usage Description: "用于查询你所在城市的天气"

// 2. 用的时候申请
import CoreLocation

@Observable
class LocationModel {
    private let manager = CLLocationManager()

    func request() {
        switch manager.authorizationStatus {
        case .notDetermined: manager.requestWhenInUseAuthorization()
        case .denied, .restricted: /* 引导去设置里开 */
        default: /* 已授权，开干 */
        }
    }
}

// 3. 被拒后优雅降级：给提示 + 跳设置
// UIApplication.shared.open(URL(string: UIApplication.openSettingsURLString)!)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>注意：iOS 权限的"一次性"

{class="mt-1"}
iOS 的权限弹窗<strong>只弹一次</strong>——用户拒绝后再也不会弹。所以：申请的时机要选在"用户正要用的那一刻"（而不是一启动就弹一堆），文案要说明用途。被拒后的界面引导（"去设置里开启定位"）是标配，别让用户困在死胡同里。
:::

#### 二、通知：在正确的时间说有用的话

通知是 App 触达用户的通道，也是最容易被用户"拉黑"的功能。iOS 用 <strong>UserNotifications</strong> 框架，发通知三条纪律：<strong>只发有用的、让用户能关、别半夜骚扰</strong>。基础用法：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 本地通知</span><span class="dots">···</span>
:::

```
import UserNotifications

// 1. 申请通知权限（弹窗一次）
UNUserNotificationCenter.current()
    .requestAuthorization(options: [.alert, .sound, .badge]) { granted, _ in
        print(granted ? "已授权" : "被拒绝")
    }

// 2. 安排一条"每天 20:00 记账提醒"
func scheduleDailyReminder() {
    let content = UNMutableNotificationContent()
    content.title = "记账提醒"
    content.body = "今天还没记账哦"
    content.sound = .default

    var comps = DateComponents()
    comps.hour = 20
    let trigger = UNCalendarNotificationTrigger(dateMatching: comps, repeats: true)

    let request = UNNotificationRequest(
        identifier: "daily-reminder",
        content: content,
        trigger: trigger
    )
    UNUserNotificationCenter.current().add(request)
}
```
:::

注意：iOS 的通知权限同样"只弹一次"，且用户随时可以在系统设置里关掉——所以通知内容的价值感很重要，滥发一次可能就永远失去用户。

#### 三、架构进阶：MVVM 深入与可测试性

第 65 章用过 MVVM，这里补三个进阶要点：

- <strong>协议抽象</strong>：让 ViewModel 依赖协议（protocol）而不是具体类——测试时可以注入"假数据源"，这是可测试性的基石；
- <strong>单一职责</strong>：一个 ViewModel 只管一件事（记账的不管天气）；功能多了就拆；
- <strong>别过度设计</strong>：单人小项目，"@Observable 类 + 协议抽象"就够了。VIPER、Clean Architecture 这类重架构，等团队和复杂度找上门再说——工具是服务目标的，不是用来炫耀的。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：SwiftUI 的"生态红利"

{class="mt-1"}
iOS 生态还有两个"只此一家"的进阶玩法：<strong>小组件（WidgetKit）</strong>让用户不打开 App 就能看信息（记账本的"本月支出"放桌面），<strong>快捷指令（App Intents）</strong>让用户用 Siri 或自动化调用你的功能。两者都有官方框架，入门成本不高，但对用户体验的加成巨大——进阶路上值得优先解锁。
:::

#### 四、2026 年的新玩法：AI 辅助 iOS 开发

2026 年，AI 已经深度嵌入苹果开发流程。如果你想提速，这套组合拳很成熟：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">环节</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">AI 怎么帮</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">你的职责</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">写代码</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode 内置代码补全 + 第三方 AI 插件生成</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">描述清楚需求，审查产出</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">查资料</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把官方文档和报错信息丢给 AI 解读</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">关键结论回官方文档核实</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">写测试</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">让 AI 按"正常/边界/异常"三类生成 XCTest 用例</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">确认用例符合业务语义</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">改 bug</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">贴崩溃日志 + 相关代码，AI 定位修复</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">看懂改动，跑测试验证</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
AI 辅助 iOS 开发的四个场景

具体方法论——怎么给 AI 下指令、怎么验收、怎么避坑——完整的 11 章内容在本书第七篇《AI编程实战篇》（第37-47章）里，强烈建议配合阅读：<strong>Swift 语法交给本篇，AI 协作的心法交给第七篇</strong>。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：给记账本加"三件套"

#### 五、Swift 并发要点：@MainActor 与 Task

Swift 6 的并发体系有两条新手必懂的规则：

- <strong>界面只能在主线程更新</strong>：SwiftUI 视图默认是 <code class="inline">@MainActor</code>，网络回调回到主线程再改状态（<code class="inline">await MainActor.run { ... }</code> 或把 ViewModel 标成 @MainActor）；
- <strong>异步任务用 Task 管理</strong>：<code class="inline">.task { }</code> 修饰符随视图出现自动开始、消失自动取消——这是 SwiftUI 里启动异步工作的标准姿势，别在 body 里乱写 Task 裸奔。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 标准异步姿势</span><span class="dots">···</span>
:::

```
struct WeatherScreen: View {
    @State private var vm = WeatherViewModel()

    var body: some View {
        Group {
            switch vm.state {
            case .loading: ProgressView()
            case .success(let d): WeatherContent(data: d)
            case .error(let m): Text(m)
            }
        }
        .task {                       // 出现即开始，消失即取消
            await vm.search(city: "北京")
        }
    }
}
```
:::

这两条规则背后是 Swift 6 的"数据竞争安全"设计——编译器会在你写错时直接报错，而不是等 App 崩了才发现。<strong>编译器的报错不是找茬，是替你挡子弹</strong>。

{class="mt-1"}
① 给记账本加"每天 20:00 记账提醒"（通知权限 + 本地通知）；② 把 ViewModel 的数据源改成协议抽象，并写一个注入假数据的单元测试；③ 加一个"本月支出"桌面小组件。三件套做完，你的项目就有"正规军"的样子了。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 权限三步：Info.plist 声明（漏了必崩）、用时申请、被拒引导去设置
- iOS 权限弹窗只弹一次：时机选在"正要用的那一刻"，文案写清用途
- 通知三纪律：只发有用的、能关、不骚扰；UserNotifications 框架
- MVVM 进阶：协议抽象（可测试）、单一职责、不过度设计
- 生态红利：WidgetKit 小组件 + App Intents 快捷指令
- AI 辅助四场景：写码、查资料、写测试、改 bug；方法论见第七篇（第37-47章）
:::
