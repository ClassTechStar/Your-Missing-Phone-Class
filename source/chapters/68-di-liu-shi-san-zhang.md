---
id: di-liu-shi-san-zhang
num: 63
part: ios-kai-fa-pian
nav: 第六十三章：视图、状态与导航
toc: default
kind: chapter
---

### 第六十三章：视图、状态与导航

{class="chapter-intro mb-4"}
单页面的玩具已经会做了。这一章解决两个"长大"问题：怎么在多个页面之间跳来跳去（导航），以及数据在页面之间怎么流动（状态管理）。学完本章，你就能搭出"列表 → 详情 → 编辑"这种经典的多页面 App 骨架。

#### 一、状态管理的"数据流全景"

SwiftUI 的状态工具不止 @State 一个。先看这张全景图，搞懂"什么时候用哪个"：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">工具</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">管什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">谁来用</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">典型场景</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">页面私有的临时状态</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">当前视图</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">计数器、输入框文字</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Binding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">借用别人的状态</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">子视图改父视图</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自定义组件</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@StateObject / @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跨页面共享的逻辑</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">视图模型（ViewModel）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数据加载、业务逻辑</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@EnvironmentObject / .environment</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全局共享的状态</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">整个 App</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用户登录态、主题设置</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
SwiftUI 状态工具全景（2026 年，@Observable 已是主流）

::: div .code-block
:::inline div .code-head
<span>SWIFT · 2026 主流：@Observable 视图模型</span><span class="dots">···</span>
:::

```
// iOS 17+ 的现代写法：@Observable 宏（推荐新项目使用）
import Observation

@Observable
class CounterModel {                 // 视图模型
    var count = 0
    func increment() { count += 1 }
}

struct CounterView: View {
    @State private var model = CounterModel()   // 持有模型

    var body: some View {
        VStack {
            Text("你点了 \(model.count) 次")
            Button("点我") { model.increment() }
        }
    }
}
```
:::

给新手的粗暴建议：<strong>页面私有的用 @State，跨页面/有逻辑的用 @Observable 类</strong>。老教程里的 @StateObject/@ObservableObject 是上一代写法，能读懂即可，新代码按上面来。

#### 二、NavigationStack：页面跳转的"栈"

iOS 16 起，多页面导航用 <strong>NavigationStack</strong>——像一摞盘子，推一个进一个，返回时逐个弹出：

::: div .code-block
:::inline div .code-head
<span>SWIFT · NavigationStack 导航</span><span class="dots">···</span>
:::

```
struct HomeView: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("张三的账本") {
                    DetailView(name: "张三的账本")   // 目标页面
                }
                NavigationLink("李四的账本") {
                    DetailView(name: "李四的账本")
                }
            }
            .navigationTitle("账本列表")   // 顶部大标题
        }
    }
}

struct DetailView: View {
    let name: String
    var body: some View {
        Text("\(name) 的详情页")
            .navigationTitle(name)
            .navigationBarTitleDisplayMode(.inline)
    }
}
```
:::

NavigationLink 就是"能点的跳转链接"；<code class="inline">navigationTitle</code> 自动生成导航栏标题和返回按钮。要<strong>编程式跳转</strong>（比如点完"保存"自动返回）时，用 <code class="inline">@Environment(\.dismiss)</code> 关闭当前页面——这两招配合，90% 的导航需求就齐了。

#### 三、弹窗与底部标签：sheet 与 TabView

除了"推页面"，还有两种经典交互：

::: div .code-block
:::inline div .code-head
<span>SWIFT · sheet 弹窗 + TabView 标签页</span><span class="dots">···</span>
:::

```
// 1. 底部弹出半屏/全屏（录入表单最爱）
struct HomeView: View {
    @State private var showAdd = false
    var body: some View {
        Button("记一笔") { showAdd = true }
            .sheet(isPresented: $showAdd) {
                AddRecordView()     // 弹出的录入页
            }
    }
}

// 2. 底部标签栏（App 的"骨架"）
struct MainTabView: View {
    var body: some View {
        TabView {
            RecordListView()
                .tabItem { Label("账本", systemImage: "book") }
            StatsView()
                .tabItem { Label("统计", systemImage: "chart.pie") }
            SettingsView()
                .tabItem { Label("设置", systemImage: "gear") }
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：什么时候用哪种？

{class="mt-1"}
经验法则：<strong>主流程用 NavigationStack 推页面（列表→详情），临时操作用 sheet 弹窗（新增、编辑、确认），并列的几大块用 TabView（底部标签）</strong>。三者组合，就是绝大多数 App 的骨架。
:::

#### 四、List：iOS 的"国民列表"

iOS 上最常用、最有"苹果味"的组件就是 <strong>List</strong>——天然带分割线、滑动删除、点击高亮：

::: div .code-block
:::inline div .code-head
<span>SWIFT · List 列表 + 滑动删除</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var records = ["午饭 25.5", "地铁 6.0", "工资 +8000"]

    var body: some View {
        List {
            ForEach(records, id: \.self) { r in
                Text(r)
            }
            .onDelete { indexSet in          // 左滑删除
                records.remove(atOffsets: indexSet)
            }
        }
    }
}
```
:::

列表 + NavigationLink + sheet + TabView——把这四样组合起来，你已经能搭出"账本列表 → 点开详情 → 点+弹录入"的完整 App 骨架了。下一章的记账本项目，就是这么搭的。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：搭一个"三页骨架"

#### 五、程序生命周期：前台与后台

和安卓的 Activity 生命周期类似，iOS App 也有"出生、前台、后台、死亡"的状态变化。SwiftUI 里用 <code class="inline">scenePhase</code> 环境值观察：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 观察前台/后台切换</span><span class="dots">···</span>
:::

```
@main
struct MyApp: App {
    @Environment(\.scenePhase) private var phase

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .onChange(of: phase) { _, newPhase in
            switch newPhase {
            case .active:    print("回到前台，恢复刷新")
            case .inactive:  print("过渡中（来电/切后台瞬间）")
            case .background: print("进后台，保存草稿")
            @unknown default: break
            }
        }
    }
}
```
:::

典型用途：<strong>回前台时刷新数据，进后台时保存草稿</strong>。iOS 对后台运行管得很严——普通 App 进后台后很快被挂起（冻结），别指望在后台偷偷干重活；真要定时任务，用第 68 章的本地通知，而不是"后台常驻"。

{class="mt-1"}
做一个假数据版本的记账本骨架：TabView 三个标签（账本/统计/设置）→ 账本页用 List 显示假数据、点行跳详情（NavigationStack）→ 右上角"+"按钮弹录入 sheet。不存数据、不联网，纯练骨架——这个骨架做好，第 65 章往里填真数据就是水到渠成。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 状态四工具：@State（页面私有）、@Binding（借用）、@Observable（逻辑）、.environment（全局）
- 新项目用 @Observable 宏写视图模型；老教程的 @ObservableObject 能读即可
- NavigationStack 推页面；@Environment(\.dismiss) 编程式返回
- 主流程推页面、临时操作弹 sheet、并列大块用 TabView
- List 是"国民列表"：分割线、滑动删除开箱即用
:::
