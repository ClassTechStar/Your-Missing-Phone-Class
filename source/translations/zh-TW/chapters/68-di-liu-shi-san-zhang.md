---
id: di-liu-shi-san-zhang
num: 63
part: ios-kai-fa-pian
nav: 第六十三章：檢視、狀態與導航
toc: default
kind: chapter
---

### 第六十三章：檢視、狀態與導航

{class="chapter-intro mb-4"}
單頁面的玩具已經會做了。這一章解決兩個"長大"問題：怎麼在多個頁面之間跳來跳去（導航），以及資料在頁面之間怎麼流動（狀態管理）。學完本章，你就能搭出"列表 → 詳情 → 編輯"這種經典的多頁面 App 骨架。

#### 一、狀態管理的"資料流全景"

SwiftUI 的狀態工具不止 @State 一個。先看這張全景圖，搞懂"什麼時候用哪個"：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">工具</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">管什麼</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">誰來用</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">典型場景</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">頁面私有的臨時狀態</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">當前檢視</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">計數器、輸入框文字</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Binding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">借用別人的狀態</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">子檢視改父檢視</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自定義元件</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@StateObject / @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跨頁面共享的邏輯</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">檢視模型（ViewModel）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">資料載入、業務邏輯</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@EnvironmentObject / .environment</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全域性共享的狀態</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">整個 App</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">使用者登入態、主題設定</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
SwiftUI 狀態工具全景（2026 年，@Observable 已是主流）

::: div .code-block
:::inline div .code-head
<span>SWIFT · 2026 主流：@Observable 檢視模型</span><span class="dots">···</span>
:::

```
// iOS 17+ 的現代寫法：@Observable 宏（推薦新專案使用）
import Observation

@Observable
class CounterModel {                 // 檢視模型
    var count = 0
    func increment() { count += 1 }
}

struct CounterView: View {
    @State private var model = CounterModel()   // 持有模型

    var body: some View {
        VStack {
            Text("你點了 \(model.count) 次")
            Button("點我") { model.increment() }
        }
    }
}
```
:::

給新手的粗暴建議：頁面私有的用 @State，跨頁面/有邏輯的用 @Observable 類。老教學裡的 @StateObject/@ObservableObject 是上一代寫法，能讀懂即可，新程式碼按上面來。

#### 二、NavigationStack：頁面跳轉的"棧"

iOS 16 起，多頁面導航用 NavigationStack——像一摞盤子，推一個進一個，返回時逐個跳出：

::: div .code-block
:::inline div .code-head
<span>SWIFT · NavigationStack 導航</span><span class="dots">···</span>
:::

```
struct HomeView: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("張三的帳本") {
                    DetailView(name: "張三的帳本")   // 目標頁面
                }
                NavigationLink("李四的帳本") {
                    DetailView(name: "李四的帳本")
                }
            }
            .navigationTitle("帳本列表")   // 頂部大標題
        }
    }
}

struct DetailView: View {
    let name: String
    var body: some View {
        Text("\(name) 的詳情頁")
            .navigationTitle(name)
            .navigationBarTitleDisplayMode(.inline)
    }
}
```
:::

NavigationLink 就是"能點的跳轉連結"；navigationTitle 自動生成導航欄標題和返回按鈕。要程式設計式跳轉（比如點完"儲存"自動返回）時，用 @Environment(\.dismiss) 關閉當前頁面——這兩招配合，90% 的導航需求就齊了。

#### 三、跳出視窗與底部標籤：sheet 與 TabView

除了"推頁面"，還有兩種經典互動：

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
                AddRecordView()     // 彈出的錄入頁
            }
    }
}

// 2. 底部標籤欄（App 的"骨架"）
struct MainTabView: View {
    var body: some View {
        TabView {
            RecordListView()
                .tabItem { Label("帳本", systemImage: "book") }
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
小貼士：什麼時候用哪種？

{class="mt-1"}
經驗法則：主流程用 NavigationStack 推頁面（列表→詳情），臨時操作用 sheet 跳出視窗（新增、編輯、確認），並列的幾大塊用 TabView（底部標籤）。三者組合，就是絕大多數 App 的骨架。
:::

#### 四、List：iOS 的"國民列表"

iOS 上最常用、最有"蘋果味"的元件就是 List——天然帶分割線、滑動刪除、點選高亮：

::: div .code-block
:::inline div .code-head
<span>SWIFT · List 列表 + 滑動刪除</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var records = ["午飯 25.5", "地鐵 6.0", "工資 +8000"]

    var body: some View {
        List {
            ForEach(records, id: \.self) { r in
                Text(r)
            }
            .onDelete { indexSet in          // 左滑刪除
                records.remove(atOffsets: indexSet)
            }
        }
    }
}
```
:::

列表 + NavigationLink + sheet + TabView——把這四樣組合起來，你已經能搭出"帳本列表 → 點開詳情 → 點+彈錄入"的完整 App 骨架了。下一章的記帳本專案，就是這麼搭的。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：搭一個"三頁骨架"

#### 五、程式生命週期：前臺與後臺

和安卓的 Activity 生命週期類似，iOS App 也有"出生、前臺、後臺、死亡"的狀態變化。SwiftUI 裡用 scenePhase 環境值觀察：

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
            case .active:    print("回到前臺，恢復重新整理")
            case .inactive:  print("過渡中（來電/切後臺瞬間）")
            case .background: print("進後臺，儲存草稿")
            @unknown default: break
            }
        }
    }
}
```
:::

典型用途：回前臺時重新整理資料，進後臺時儲存草稿。iOS 對後臺執行管得很嚴——普通 App 進後臺後很快被掛起（凍結），別指望在後臺偷偷乾重活；真要定時任務，用第 68 章的本地通知，而不是"後臺常駐"。

{class="mt-1"}
做一個假資料版本的記帳本骨架：TabView 三個標籤（帳本/統計/設定）→ 帳本頁用 List 顯示假資料、點行跳詳情（NavigationStack）→ 右上角"+"按鈕彈錄入 sheet。不存資料、不聯網，純練骨架——這個骨架做好，第 65 章往裡填真資料就是水到渠成。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 狀態四工具：@State（頁面私有）、@Binding（借用）、@Observable（邏輯）、.environment（全域性）
- 新專案用 @Observable 宏寫檢視模型；老教學的 @ObservableObject 能讀即可
- NavigationStack 推頁面；@Environment(\.dismiss) 程式設計式返回
- 主流程推頁面、臨時操作彈 sheet、並列大塊用 TabView
- List 是"國民列表"：分割線、滑動刪除開箱即用
:::
