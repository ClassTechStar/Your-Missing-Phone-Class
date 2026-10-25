---
id: di-liu-shi-er-zhang
num: 62
part: ios-kai-fa-pian
nav: 第六十二章：界面開發——SwiftUI入門
toc: default
kind: chapter
---

### 第六十二章：界面之開發——SwiftUI 入門

{class="chapter-intro mb-4"}
界面者，用戶所見之一切也。SwiftUI 者，蘋果 2019 年所推出聲明式界面之框架也——爾惟「聲明」界面之狀貌，系統自任渲染、適配深色之模式、適配諸般之屏。至 2026 年，SwiftUI 已為新項目絕對之主流。此章，吾儕學「繪畫」。

#### 一、SwiftUI 之思想：聲明式，非命令式

舊式界面之開發乃「命令式」：先告系統「創按鈕 → 置於(20,30) → 設其色」，一步一步指揮之。SwiftUI 乃「聲明式」：爾徑述「界面之上有一赤色按鈕書『點我』」，如何繪、何時重繪，系統自任之。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 第一個 SwiftUI 視圖</span><span class="dots">···</span>
:::

```
import SwiftUI

struct ContentView: View {
    var body: some View {      // body：狀"界面之形"
        VStack {               // 豎而列之
            Text("汝好，世界！")
                .font(.largeTitle)      // 修飾符：大標題
            Button("點我") {
                print("被點擊了")
            }
            .buttonStyle(.borderedProminent)  // 藍色實心按鈕
        }
        .padding()
    }
}
```
:::

關鍵之點：視圖者，守 View 協議之結構體也，body 之屬性述界面，.修飾符() 鏈式「上妝」。此即 SwiftUI 全部之基本盤也。

#### 二、基礎視圖：文字、按鈕、輸入框、圖

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">視圖</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">何為</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">示例</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">顯示文字</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text(「你好」)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">按鈕</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button(「點我」) { 動作 }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">輸入框</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField(「提示」, text: $文本)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">顯示圖片</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Image(systemName: "star.fill")</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
SwiftUI 四大基礎視圖

注意 Image(systemName:)——蘋果內置 SF Symbols 圖標之庫（免費圖標數千），「star.fill」此等之名即可徑示一實心之星。此 iOS 開發隱藏之福利：作界面幾乎不必覓圖標之素材。

#### 三、佈局三件套：VStack、HStack、ZStack

- VStack：縱而列之（若列隊取餐）；
- HStack：橫而列之（若並肩而坐）；
- ZStack：疊而置之（若撲克之牌相壘，宜作角標、遮罩）。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 佈局三件套 + 常用修飾符</span><span class="dots">···</span>
:::

```
VStack(alignment: .leading, spacing: 12) {
    HStack {
        Text("賬單")
        Spacer()                 // 彈性之空：推右至盡
        Text("-25.5 元").foregroundColor(.red)
    }
    Divider()                    // 分割線
    Text("備註：午餐")
}
.padding(16)                     // 四周留白
.background(Color(.systemGray6)) // 淺灰底
.cornerRadius(12)                // 圓角

// 修飾符之序有義：先 padding 後 background，背景不含邊距
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
按：修飾符次序有講究

{class="mt-1"}
padding(16).background(灰) 與 background(灰).padding(16)，其效迥異——前者先留白而後塗色（背景不含邊距），後者先塗色而後留白（背景兼含邊距）。新手所見怪異之白邊，多源於此。倘有疑，互易其序，預覽立示其答。
:::

#### 四、狀態與綁定：使界面「活」起來

靜態界面殊無意味。SwiftUI 之規則：界面恆忠實反映狀態，狀態一變，界面自重繪焉。

::: div .code-block
:::inline div .code-head
<span>SWIFT · @State 計數器</span><span class="dots">···</span>
:::

```
struct CounterView: View {
    @State private var count = 0   // @State：此值變則重畫

    var body: some View {
        VStack {
            Text("汝點了 \(count) 次")
            Button("點我 +1") {
                count += 1          // 改狀態，界面自動刷新
            }
        }
    }
}
```
:::

輸入框須用「雙向綁定」——$ 符號將「值與修改之權」一併傳入：

::: div .code-block
:::inline div .code-head
<span>SWIFT · @Binding 雙向綁定</span><span class="dots">···</span>
:::

```
struct InputView: View {
    @State private var text = ""

    var body: some View {
        TextField("輸入若干", text: $text)  // $ 雙向綁定
            .textFieldStyle(.roundedBorder)
        Text("汝輸入了：\(text)")   // 輸入則實時更新
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
圖 3：SwiftUI「狀態 → 界面」單向數據流
:::

#### 五、預覽、主題與動畫：SwiftUI 之「外掛」

- #Preview 宏：於檔案之末加 #Preview { ContentView() }，右側畫布即時渲染——改碼所見即所得；
- 深色模式免費：用系統顏色（Color(.systemGray6)、.primary）而非寫死之色，深色模式自能相配，不多書一行；
- 動畫一行可成：withAnimation { count += 1 }，或予視圖加 .animation(.default, value: count)——過渡絲滑。

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
新手常病：界面未正，而先糾結於動畫。宜先令功能通達，終乃一體加諸動效——動畫者錦上添花也，功能者雪中送炭也。此亦吾儕一貫「簡單至上」之旨。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：做一「心情按鈕」

#### 六、常用修飾符速查：一頁在手，界面無憂

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">欲作何事</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">修飾符</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">留白</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.padding(16)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">圓角</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cornerRadius(12)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">背景色</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.background(Color(.systemGray6))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">字體與字號</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.font(.title.bold())</code> / <code class="inline">.font(.system(size: 20))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">前景色（文字/圖標）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.foregroundColor(.red)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">撐滿寬度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(maxWidth: .infinity)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">固定尺寸</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(width:100, height: 44)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">對齊之法</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack(alignment: .leading)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">透明度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.opacity(0.6)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">陰影</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.shadow(radius: 5)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">點擊手勢</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.onTapGesture { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">鍵盤類型</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.keyboardType(.decimalPad)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
SwiftUI 常用修飾符速查

記之不住亦無妨——此頁正為查檢而設。用之最多者，實惟前四：padding、圓角、背景、字體。

{class="mt-1"}
改模板之項為心情輪換器：一按鈕，點之則於 😀開心 → 😢難過 → 😡生氣 之間循環遞換，文字與背景之色隨之而變。提示：以陣列貯三組（文字+顏色），@State 貯其下標，點時用 (index + 1) % 3。成則示諸友朋，可得第一聲「哇，汝能作 App 矣」之歎。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小結

- SwiftUI 為聲明式：述其「所長之形」，系統任描繪重繪之責
- 視圖 = 遵 View 協議之結構體；body 述界面；修飾符連綴如「上妝」
- 四大基礎視圖：Text / Button / TextField / Image；SF Symbols 圖標庫免費而用之不竭
- 佈局三件：VStack 豎列、HStack 橫列、ZStack 疊置；Spacer 者彈性之空也
- @State 使界面活起來；$ 雙向綁定以饋輸入框
- #Preview 所見即所得；系統顏色自配深色模式；withAnimation 一行成動效
:::
