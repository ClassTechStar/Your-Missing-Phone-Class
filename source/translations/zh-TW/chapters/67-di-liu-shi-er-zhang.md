---
id: di-liu-shi-er-zhang
num: 62
part: ios-kai-fa-pian
nav: 第六十二章：介面開發——SwiftUI入門
toc: default
kind: chapter
---

### 第六十二章：介面開發——SwiftUI 入門

{class="chapter-intro mb-4"}
介面是使用者看到的一切。SwiftUI 是蘋果 2019 年推出的宣告式介面框架——你只需要"宣告"介面長什麼樣，系統自動負責渲染、適配深色模式、適配各種螢幕。到 2026 年，SwiftUI 已是新專案的絕對主流。這一章，咱們學會"畫畫"。

#### 一、SwiftUI 的思想：宣告式，不是命令式

老式介面開發是"命令式"：先告訴系統"建立按鈕 → 放在(20,30) → 設定顏色"，一步一步指揮。SwiftUI 是"宣告式"：你直接描述"介面上有一個紅色按鈕寫著'點我'"，怎麼畫、什麼時候重畫，系統自己操心。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 第一個 SwiftUI 檢視</span><span class="dots">···</span>
:::

```
import SwiftUI

struct ContentView: View {
    var body: some View {      // body：描述"介面長什麼樣"
        VStack {               // 豎著排列
            Text("你好，世界！")
                .font(.largeTitle)      // 修飾符：大標題
            Button("點我") {
                print("被點選了")
            }
            .buttonStyle(.borderedProminent)  // 藍色實心按鈕
        }
        .padding()
    }
}
```
:::

關鍵點：檢視 = 遵守 View 協議的結構體，body 屬性描述介面，.修飾符() 鏈式"上妝"。這就是 SwiftUI 的全部基本盤。

#### 二、基礎檢視：文字、按鈕、輸入框、圖片

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">檢視</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">幹什麼</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">示例</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">顯示文字</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text("你好")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">按鈕</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button("點我") { 動作 }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">輸入框</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField("提示", text: $文字)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">顯示圖片</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Image(systemName: "star.fill")</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
SwiftUI 四大基礎檢視

注意 Image(systemName:)——蘋果內建了 SF Symbols 圖示庫（幾千個免費圖示），"star.fill" 這種名字就能直接顯示一個實心星星。這是 iOS 開發的隱藏福利：做介面幾乎不用找圖示素材。

#### 三、佈局三件套：VStack、HStack、ZStack

- VStack：豎著排（像排隊打飯）；
- HStack：橫著排（像並排坐）；
- ZStack：疊著放（像撲克牌摞一起，適合做角標、遮罩）。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 佈局三件套 + 常用修飾符</span><span class="dots">···</span>
:::

```
VStack(alignment: .leading, spacing: 12) {
    HStack {
        Text("帳單")
        Spacer()                 // 彈性空間：把右邊推到盡頭
        Text("-25.5 元").foregroundColor(.red)
    }
    Divider()                    // 分割線
    Text("備註：午飯")
}
.padding(16)                     // 四周留白
.background(Color(.systemGray6)) // 淺灰底
.cornerRadius(12)                // 圓角

// 修飾符順序有意義：先 padding 再 background，背景不含邊距
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：修飾符順序有講究

{class="mt-1"}
padding(16).background(灰) 和 background(灰).padding(16) 效果不同——前者"先留白再塗色"（背景不含邊距），後者"先塗色再留白"（背景包含邊距）。新手最常見的"奇怪白邊"都源於此。不確定時調換順序，預覽立刻告訴你答案。
:::

#### 四、狀態與繫結：讓介面"活"起來

靜態介面沒意思。SwiftUI 的規則：介面永遠忠實反映狀態，狀態變了，介面自動重畫。

::: div .code-block
:::inline div .code-head
<span>SWIFT · @State 計數器</span><span class="dots">···</span>
:::

```
struct CounterView: View {
    @State private var count = 0   // @State：這個值變了要重畫

    var body: some View {
        VStack {
            Text("你點了 \(count) 次")
            Button("點我 +1") {
                count += 1          // 改狀態，介面自動重新整理
            }
        }
    }
}
```
:::

輸入框要用"雙向繫結"——$ 符號把"值和修改權"一起傳進去：

::: div .code-block
:::inline div .code-head
<span>SWIFT · @Binding 雙向繫結</span><span class="dots">···</span>
:::

```
struct InputView: View {
    @State private var text = ""

    var body: some View {
        TextField("輸入點什麼", text: $text)  // $ 雙向繫結
            .textFieldStyle(.roundedBorder)
        Text("你輸入了：\(text)")   // 輸入時實時更新
    }
}
```
:::

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> 使用者操作</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> 狀態改變（count += 1）</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> SwiftUI 感知到變化</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> 自動重畫介面（body 重新計算）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 3：SwiftUI 的"狀態 → 介面"單向資料流
:::

#### 五、預覽、主題與動畫：SwiftUI 的"外掛"

- #Preview 宏：檔案底部加 #Preview { ContentView() }，右側畫布實時渲染——改程式碼所見即所得；
- 深色模式免費：用系統顏色（Color(.systemGray6)、.primary）而不是寫死顏色，深色模式自動適配，一行不用多寫；
- 動畫一行搞定：withAnimation { count += 1 } 或給檢視加 .animation(.default, value: count)——過渡絲滑。

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
新手常犯的毛病是"介面還沒做對，就開始糾結動畫"。先讓功能跑通，最後再統一加動效——動畫是錦上添花，功能是雪中送炭。這也是咱們一貫的"簡單至上"原則。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：做一個"心情按鈕"

#### 六、常用修飾符速查：一頁在手，介面不愁

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">想做什麼</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">修飾符</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">留白</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.padding(16)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">圓角</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cornerRadius(12)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">背景色</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.background(Color(.systemGray6))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">字型與字號</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.font(.title.bold())</code> / <code class="inline">.font(.system(size: 20))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">前景色（文字/圖示）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.foregroundColor(.red)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">撐滿寬度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(maxWidth: .infinity)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">固定尺寸</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(width:100, height: 44)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">對齊方式</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack(alignment: .leading)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">透明度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.opacity(0.6)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">陰影</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.shadow(radius: 5)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">點選手勢</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.onTapGesture { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">鍵盤型別</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.keyboardType(.decimalPad)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
SwiftUI 常用修飾符速查

記不住沒關係——這頁就是用來查的。用得最多的其實就前四個：padding、圓角、背景、字型。

{class="mt-1"}
把模板專案改成一個心情切換器：一個按鈕，點選後在 😀開心 → 😢難過 → 😡生氣 之間迴圈切換，文字和背景色跟著變。提示：用陣列存三組（文字+顏色），@State 存下標，點選時 (index + 1) % 3。做完發給朋友玩，收穫第一波"哇你會做 App 了"。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- SwiftUI 是宣告式：描述"長什麼樣"，系統負責畫和重畫
- 檢視 = 遵守 View 協議的結構體；body 描述介面；修飾符鏈式"上妝"
- 四大基礎檢視：Text / Button / TextField / Image；SF Symbols 圖示庫免費管飽
- 佈局三件套：VStack 豎排、HStack 橫排、ZStack 疊放；Spacer 是彈性空間
- @State 讓介面活起來；$ 雙向繫結餵給輸入框
- #Preview 所見即所得；系統顏色自動適配深色模式；withAnimation 一行動效
:::
