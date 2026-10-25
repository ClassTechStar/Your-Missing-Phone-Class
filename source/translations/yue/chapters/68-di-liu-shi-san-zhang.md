---
id: di-liu-shi-san-zhang
num: 63
part: ios-kai-fa-pian
nav: 第六十三章：視圖、狀態與導航
toc: default
kind: chapter
---

### 第六十三章：視圖、狀態同導航

{class="chapter-intro mb-4"}
單頁面嘅玩具你已經識做喇。呢一章解決兩個"長大"問題：點樣喺多個頁面之間跳嚟跳去（導航），以及數據喺頁面之間點樣流動（狀態管理）。學完本章，你就可以搭出"列表 → 詳情 → 編輯"呢種經典嘅多頁面 App 骨架。

#### 一、狀態管理嘅"數據流全景"

SwiftUI 嘅狀態工具唔止 @State 一個。先睇呢張全景圖，搞清楚"幾時用邊個"：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">工具</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">管乜嘢</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">邊個用</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">典型場景</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">頁面私有嘅臨時狀態</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">當前視圖</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">計數器、輸入框文字</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Binding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">借人哋嘅狀態</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">子視圖改父視圖</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自訂組件</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@StateObject / @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跨頁面共享嘅邏輯</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">視圖模型（ViewModel）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">數據加載、業務邏輯</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@EnvironmentObject / .environment</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全局共享嘅狀態</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">成個 App</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用戶登入狀態、主題設定</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
SwiftUI 狀態工具全景（2026 年，@Observable 已經係主流）

::: div .code-block
:::inline div .code-head
<span>SWIFT · 2026 主流：@Observable 視圖模型</span><span class="dots">···</span>
:::

```
// iOS 17+ 嘅現代寫法：@Observable 宏（新建項目建議用）
import Observation

@Observable
class CounterModel {                 // 視圖模型
    var count = 0
    func increment() { count += 1 }
}

struct CounterView: View {
    @State private var model = CounterModel()   // 持有模型

    var body: some View {
        VStack {
            Text("你㩒咗 \(model.count) 次")
            Button("㩒我") { model.increment() }
        }
    }
}
```
:::

畀新手嘅粗暴建議：頁面私有嘅用 @State，跨頁面／有邏輯嘅用 @Observable 類。舊教程入面嘅 @StateObject/@ObservableObject 係上一代寫法，睇得明就得，新代碼照上面咁做。

#### 二、NavigationStack：頁面跳轉嘅"棧"

iOS 16 開始，多頁面導航用 NavigationStack——好似一疊碟咁，推一個入一個，返回嗰陣逐個彈出嚟：

::: div .code-block
:::inline div .code-head
<span>SWIFT · NavigationStack 導航</span><span class="dots">···</span>
:::

```
struct HomeView: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("張三嘅賬本") {
                    DetailView(name: "張三嘅賬本")   // 目標頁面
                }
                NavigationLink("李四嘅賬本") {
                    DetailView(name: "李四嘅賬本")
                }
            }
            .navigationTitle("賬本列表")   // 頂部大標題
        }
    }
}

struct DetailView: View {
    let name: String
    var body: some View {
        Text("\(name) 嘅詳情頁")
            .navigationTitle(name)
            .navigationBarTitleDisplayMode(.inline)
    }
}
```
:::

NavigationLink 就係"㩒得嘅跳轉連結"；navigationTitle 自動生成導航欄標題同返回按鈕。要編程式跳轉（譬如㩒完"保存"自動返回）嗰陣，用 @Environment(\.dismiss) 關閉當前頁面——呢兩招一齊用，90% 嘅導航需求就齊喇。

#### 三、彈窗同底部標籤：sheet 同 TabView

除咗"推頁面"，仲有兩種經典交互：

::: div .code-block
:::inline div .code-head
<span>SWIFT · sheet 彈窗 + TabView 標籤頁</span><span class="dots">···</span>
:::

```
// 1. 底部彈出半屏/全屏（錄入表單最愛）
struct HomeView: View {
    @State private var showAdd = false
    var body: some View {
        Button("記一筆") { showAdd = true }
            .sheet(isPresented: $showAdd) {
                AddRecordView()     // 彈出嘅錄入頁
            }
    }
}

// 2. 底部標籤欄（App 嘅"骨架"）
struct MainTabView: View {
    var body: some View {
        TabView {
            RecordListView()
                .tabItem { Label("賬本", systemImage: "book") }
            StatsView()
                .tabItem { Label("統計", systemImage: "chart.pie") }
            SettingsView()
                .tabItem { Label("設定", systemImage: "gear") }
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：幾時用邊種？

{class="mt-1"}
經驗法則：主流程用 NavigationStack 推頁面（列表→詳情），臨時操作用 sheet 彈窗（新增、編輯、確認），並列嘅幾大塊用 TabView（底部標籤）。三者組合，就係絕大多數 App 嘅骨架。
:::

#### 四、List：iOS 嘅"國民列表"

iOS 上面最常用、最有"蘋果味"嘅組件就係 List——天生帶分割線、滑動刪除、㩒咗會高亮：

::: div .code-block
:::inline div .code-head
<span>SWIFT · List 列表 + 滑動刪除</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var records = ["午餐 25.5", "地鐵 6.0", "人工 +8000"]

    var body: some View {
        List {
            ForEach(records, id: \.self) { r in
                Text(r)
            }
            .onDelete { indexSet in          // 左掃刪除
                records.remove(atOffsets: indexSet)
            }
        }
    }
}
```
:::

列表 + NavigationLink + sheet + TabView——將呢四樣組合埋一齊，你已經可以搭出"賬本列表 → 㩒開詳情 → 㩒+彈錄入"嘅完整 App 骨架喇。下一章嘅記賬本項目，就係咁搭嘅。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
嚟動手：搭一個"三頁骨架"

#### 五、程式生命週期：前台同後台

同安卓嘅 Activity 生命週期差唔多，iOS App 都有"出生、前台、後台、死亡"嘅狀態變化。SwiftUI 入面用 scenePhase 環境值嚟觀察：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 觀察前臺/後臺切換</span><span class="dots">···</span>
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
            case .active:    print("回到前臺，恢復刷新")
            case .inactive:  print("過渡中（來電/切後臺瞬間）")
            case .background: print("進後臺，保存草稿")
            @unknown default: break
            }
        }
    }
}
```
:::

典型用途：返到前台嗰陣刷新數據，入咗後台嗰陣保存草稿。iOS 對後台運行管得好嚴——普通 App 入咗後台好快就會被掛起（凍結），唔好指望喺後台偷偷哋做重活；真係要定時任務，用第 68 章嘅本地通知，而唔係"後台常駐"。

{class="mt-1"}
做一個假數據版本嘅記賬本骨架：TabView 三個標籤（賬本／統計／設定）→ 賬本頁用 List 顯示假數據、㩒行跳詳情（NavigationStack）→ 右上角"+"按鈕彈錄入 sheet。唔存數據、唔上網，純練骨架——呢個骨架做好咗，第 65 章再入去填真數據就水到渠成。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 狀態四工具：@State（頁面私有）、@Binding（借用）、@Observable（邏輯）、.environment（全局）
- 新項目用 @Observable 巨集寫視圖模型；舊教程嘅 @ObservableObject 睇得明就得
- NavigationStack 推頁面；@Environment(\.dismiss) 編程式返回
- 主流程推頁面、臨時操作彈 sheet、並列大塊用 TabView
- List 係"國民列表"：分割線、滑動刪除開箱即用
:::
