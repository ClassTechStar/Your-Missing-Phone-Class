---
id: di-liu-shi-san-zhang
num: 63
part: ios-kai-fa-pian
nav: 第六十三章：視圖、狀態與導航
toc: default
kind: chapter
---

### 第六十三章：視圖、狀態與導航

{class="chapter-intro mb-4"}
單頁之玩物既已能為。此章解二「成長」之惑：如何於眾頁之間往來跳轉（導航），及數據如何在頁間流動（狀態管理）。學畢此章，則能搭「列表 → 詳情 → 編輯」經典多頁 App 之骨架矣。

#### 一、狀態管理之「數據流全景」

SwiftUI 狀態之具，非惟 @State 一端。先觀此全景之圖，明「何時用何者」：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">工具</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">司何事</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">孰用之</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">典型場景</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">頁面私有之暫態</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">當前視圖</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">計數器、輸入框文字</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Binding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">借他人之狀態</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">子視圖改父視圖</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自定義組件</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@StateObject / @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跨頁共用之邏輯</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">視圖模型（ViewModel）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">數據載入、業務邏輯</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@EnvironmentObject / .environment</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全局共用之狀態</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">整個 App</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用戶登入之態、主題設置</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
SwiftUI 狀態之具全景（2026 年，@Observable 已為主流）

::: div .code-block
:::inline div .code-head
<span>SWIFT · 2026 主流：@Observable 視圖模型</span><span class="dots">···</span>
:::

```
// iOS 17+ 之新法：@Observable 宏（新項目宜用）
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
            Text("汝點了 \(model.count) 次")
            Button("點我") { model.increment() }
        }
    }
}
```
:::

予新手直截之勸：頁面私有者用 @State，跨頁或有邏輯者用 @Observable 類。舊籍之 @StateObject/@ObservableObject 乃前代寫法，能讀懂即可，新碼悉遵上式。

#### 二、NavigationStack：頁面跳轉之「棧」

iOS 16 以降，多頁導航用 NavigationStack——若一疊盤，推一入一，返則逐一彈出：

::: div .code-block
:::inline div .code-head
<span>SWIFT · NavigationStack 導航</span><span class="dots">···</span>
:::

```
struct HomeView: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("張三之賬本") {
                    DetailView(name: "張三之賬本")   // 目標頁面
                }
                NavigationLink("李四之賬本") {
                    DetailView(name: "李四之賬本")
                }
            }
            .navigationTitle("賬本列表")   // 頂部大標題
        }
    }
}

struct DetailView: View {
    let name: String
    var body: some View {
        Text("\(name) 之詳情頁")
            .navigationTitle(name)
            .navigationBarTitleDisplayMode(.inline)
    }
}
```
:::

NavigationLink 即「可點之跳轉連結」；navigationTitle 自生導航欄之題與返鈕。欲程式化跳轉（如點「保存」而自返）者，用 @Environment(\.dismiss) 以闔當前之頁——二法相濟，九成導航之需備矣。

#### 三、彈窗與底部標籤：sheet 與 TabView

除「推頁」外，尚有二種經典之交互：

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
                AddRecordView()     // 彈出之錄入頁
            }
    }
}

// 2. 底部標籤欄（App 之"骨架"）
struct MainTabView: View {
    var body: some View {
        TabView {
            RecordListView()
                .tabItem { Label("賬本", systemImage: "book") }
            StatsView()
                .tabItem { Label("統計", systemImage: "chart.pie") }
            SettingsView()
                .tabItem { Label("設置", systemImage: "gear") }
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：何時用何種？

{class="mt-1"}
經驗之法：主流程以 NavigationStack 推頁（列表→詳情），暫時之操作以 sheet 彈窗（新增、編輯、確認），並列數大塊以 TabView（底部標籤）。三者相合，即絕大多數 App 之骨架。
:::

#### 四、List：iOS 之「國民列表」

iOS 最常用而最具「蘋果味」之組件即 List——天生帶分割線、滑動而刪、點而高亮：

::: div .code-block
:::inline div .code-head
<span>SWIFT · List 列表 + 滑動刪除</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var records = ["午餐 25.5", "地鐵 6.0", "薪俸 +8000"]

    var body: some View {
        List {
            ForEach(records, id: \.self) { r in
                Text(r)
            }
            .onDelete { indexSet in          // 左滑而刪
                records.remove(atOffsets: indexSet)
            }
        }
    }
}
```
:::

列表 + NavigationLink + sheet + TabView——合此四者，汝已能搭「賬本列表 → 點開詳情 → 點+彈錄入」完整 App 之骨架矣。次章記賬本之項，即如是搭成。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：搭一「三頁骨架」

#### 五、程序生命之期：前台與後台

與安卓 Activity 生命週期相類，iOS App 亦有「生、前台、後台、亡」狀態之變。SwiftUI 中以 scenePhase 環境值察之：

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
            case .active:    print("返前臺，復刷新")
            case .inactive:  print("過渡中（來電/切後臺瞬間）")
            case .background: print("入後臺，存草稿")
            @unknown default: break
            }
        }
    }
}
```
:::

典型之用：返前台則刷數據，入後台則存草稿。iOS 於後台之運行管束甚嚴——常 App 入後台不久即被懸置（凍結），勿冀於後台潛作重務；誠欲定時之務，用第 68 章本地通知，而非「後台常駐」。

{class="mt-1"}
作一假數據版記賬本之骨架：TabView 三標籤（賬本/統計/設置）→ 賬本頁以 List 陳假數據、點行跳詳情（NavigationStack）→ 右上「+」鈕彈錄入 sheet。不貯數據、不連網，純練骨架——骨架既成，第 65 章填以真數，如水到而渠成。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小結

- 狀態四具：@State（頁私有）、@Binding（借用）、@Observable（邏輯）、.environment（全局）
- 新項以 @Observable 宏作視圖模型；舊籍之 @ObservableObject 能讀即可
- NavigationStack 推頁；@Environment(\.dismiss) 程式化而返
- 主流程推頁、暫事彈 sheet、並列大塊用 TabView
- List 者「國民列表」也：分割線、滑動而刪，啟箱即用
:::
