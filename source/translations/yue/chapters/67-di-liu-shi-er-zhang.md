---
id: di-liu-shi-er-zhang
num: 62
part: ios-kai-fa-pian
nav: 第六十二章：介面開發——SwiftUI入門
toc: default
kind: chapter
---

### 第六十二章：界面開發——SwiftUI 入門

{class="chapter-intro mb-4"}
界面係用戶睇到嘅一切。SwiftUI 係蘋果 2019 年推出嘅聲明式界面框架——你只需要"聲明"界面生乜嘢樣，系統自動負責渲染、適配深色模式、適配各種螢幕。到 2026 年，SwiftUI 已經係新項目嘅絕對主流。呢一章，我哋學識"畫畫"。

#### 一、SwiftUI 嘅思想：聲明式，唔係命令式

舊式界面開發係"命令式"：先話畀系統聽"建立按鈕 → 放喺(20,30) → 設定顏色"，一步一步指揮。SwiftUI 係"聲明式"：你直接描述"界面上面有一個紅色按鈕寫住'點我'"，點樣畫、幾時重畫，系統自己搞掂。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 第一個 SwiftUI 視圖</span><span class="dots">···</span>
:::

```
import SwiftUI

struct ContentView: View {
    var body: some View {      // body：描述"界面係乜嘢樣"
        VStack {               // 直向排列
            Text("你好，世界！")
                .font(.largeTitle)      // 修飾符：大標題
            Button("㩒我") {
                print("被㩒咗")
            }
            .buttonStyle(.borderedProminent)  // 藍色實心按鈕
        }
        .padding()
    }
}
```
:::

關鍵點：視圖 = 遵守 View 協議嘅結構體，body 屬性描述界面，.修飾符() 鏈式"上妝"。呢個就係 SwiftUI 嘅全部基本盤。

#### 二、基礎視圖：文字、按鈕、輸入框、圖片

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">視圖</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">做乜嘢</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">示例</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">顯示文字</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text("你好")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">按鈕</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button("點我") { 動作 }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">輸入框</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField("提示", text: $文本)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">顯示圖片</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Image(systemName: "star.fill")</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
SwiftUI 四大基礎視圖

注意 Image(systemName:)——蘋果內置咗 SF Symbols 圖標庫（幾千個免費圖標），"star.fill" 呢類名就可以直接顯示一個實心星星。呢個係 iOS 開發嘅隱藏福利：做界面幾乎唔使搵圖標素材。

#### 三、佈局三件套：VStack、HStack、ZStack

- VStack：打直咁排（好似排隊打飯）；
- HStack：打橫咁排（好似並排坐）；
- ZStack：疊住放（好似撲克牌疊埋一齊，適合做角標、遮罩）。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 佈局三件套 + 常用修飾符</span><span class="dots">···</span>
:::

```
VStack(alignment: .leading, spacing: 12) {
    HStack {
        Text("賬單")
        Spacer()                 // 彈性空間：將右邊推到盡頭
        Text("-25.5 元").foregroundColor(.red)
    }
    Divider()                    // 分隔線
    Text("備註：午餐")
}
.padding(16)                     // 四圍留白
.background(Color(.systemGray6)) // 淺灰底
.cornerRadius(12)                // 圓角

// 修飾符次序有意義：先 padding 再 background，背景唔包邊距
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：修飾符次序有講究

{class="mt-1"}
padding(16).background(灰) 同 background(灰).padding(16) 效果唔同——前者"先留白再塗色"（背景唔包含邊距），後者"先塗色再留白"（背景包含邊距）。新手最常見嘅"奇怪白邊"都係由呢度嚟。唔肯定嗰陣調轉次序，預覽即刻話你知答案。
:::

#### 四、狀態同綁定：令界面"活"起嚟

靜態界面冇乜意思。SwiftUI 嘅規則：界面永遠忠實反映狀態，狀態一變，界面自動重畫。

::: div .code-block
:::inline div .code-head
<span>SWIFT · @State 計數器</span><span class="dots">···</span>
:::

```
struct CounterView: View {
    @State private var count = 0   // @State：呢個值變咗要重畫

    var body: some View {
        VStack {
            Text("你㩒咗 \(count) 次")
            Button("㩒我 +1") {
                count += 1          // 改狀態，界面自動刷新
            }
        }
    }
}
```
:::

輸入框要用"雙向綁定"——$ 符號將"值同修改權"一齊傳入去：

::: div .code-block
:::inline div .code-head
<span>SWIFT · @Binding 雙向綁定</span><span class="dots">···</span>
:::

```
struct InputView: View {
    @State private var text = ""

    var body: some View {
        TextField("輸入啲乜嘢", text: $text)  // $ 雙向綁定
            .textFieldStyle(.roundedBorder)
        Text("你輸入咗：\(text)")   // 輸入嗰陣即時更新
    }
}
```
:::

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> 用戶操作</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> 狀態改變（count += 1）</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> SwiftUI 感知到變化</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> 自動重畫界面（body 重新計算）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 3：SwiftUI 嘅"狀態 → 界面"單向數據流
:::

#### 五、預覽、主題同動畫：SwiftUI 嘅"外掛"

- #Preview 巨集：喺檔案底部加 #Preview { ContentView() }，右邊畫布即時渲染——改代碼所見即所得；
- 深色模式免費：用系統顏色（Color(.systemGray6)、.primary）而唔係寫死顏色，深色模式自動適配，一行都唔使多寫；
- 動畫一行搞掂：withAnimation { count += 1 } 或者畀視圖加 .animation(.default, value: count)——過渡絲滑。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 十分鐘上手的動畫</span><span class="dots">···</span>
:::

```
struct AnimatedHeartView: View {
    @State private var liked = false

    var body: some View {
        Button {
            withAnimation(.spring(duration: 0.4)) {
                liked.toggle()
            }
        } label: {
            Image(systemName: liked ? "heart.fill" : "heart")
                .font(.system(size: 48))
                .foregroundColor(liked ? .red : .gray)
                .scaleEffect(liked ? 1.3 : 1.0)
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：先功能後動畫

{class="mt-1"}
新手常犯嘅毛病係"界面仲未做啱，就開始糾結動畫"。先令功能行得通，最後先統一加動效——動畫係錦上添花，功能係雪中送炭。呢個都係我哋一貫嘅"簡單至上"原則。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
嚟動手：做一個"心情按鈕"

#### 六、常用修飾符速查：一頁在手，界面唔使愁

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">想做乜嘢</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">修飾符</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">留白</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.padding(16)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">圓角</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cornerRadius(12)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">背景色</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.background(Color(.systemGray6))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">字體同字號</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.font(.title.bold())</code> / <code class="inline">.font(.system(size: 20))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">前景色（文字／圖標）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.foregroundColor(.red)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">撐滿闊度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(maxWidth: .infinity)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">固定尺寸</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(width:100, height: 44)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">對齊方式</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack(alignment: .leading)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">透明度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.opacity(0.6)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">陰影</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.shadow(radius: 5)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">點擊手勢</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.onTapGesture { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">鍵盤類型</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.keyboardType(.decimalPad)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
SwiftUI 常用修飾符速查

記唔住唔緊要——呢一頁就係用嚟查嘅。用得最多嘅其實就係頭四個：padding、圓角、背景、字體。

{class="mt-1"}
將模板項目改成一個心情切換器：一個按鈕，㩒咗之後喺 😀開心 → 😢難過 → 😡嬲 之間循環切換，文字同背景色跟住變。提示：用陣列存三組（文字+顏色），@State 存下標，㩒嗰陣 (index + 1) % 3。做完傳畀朋友玩，收穫第一波"哇你識做 App 喇"。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- SwiftUI 係聲明式：描述"生乜嘢樣"，系統負責畫同重畫
- 視圖 = 遵守 View 協議嘅結構體；body 描述界面；修飾符鏈式"上妝"
- 四大基礎視圖：Text / Button / TextField / Image；SF Symbols 圖標庫免費任用
- 佈局三件套：VStack 直排、HStack 橫排、ZStack 疊放；Spacer 係彈性空間
- @State 令界面活起嚟；$ 雙向綁定餵畀輸入框
- #Preview 所見即所得；系統顏色自動適配深色模式；withAnimation 一行動效
:::
