---
id: di-liu-shi-er-zhang
num: 62
part: ios-kai-fa-pian
nav: 第六十二章：界面开发——SwiftUI入门
toc: default
kind: chapter
---

### 第六十二章：界面开发——SwiftUI 入门

{class="chapter-intro mb-4"}
界面是用户看到的一切。SwiftUI 是苹果 2019 年推出的<strong>声明式</strong>界面框架——你只需要"声明"界面长什么样，系统自动负责渲染、适配深色模式、适配各种屏幕。到 2026 年，SwiftUI 已是新项目的绝对主流。这一章，咱们学会"画画"。

#### 一、SwiftUI 的思想：声明式，不是命令式

老式界面开发是"命令式"：先告诉系统"创建按钮 → 放在(20,30) → 设置颜色"，一步一步指挥。SwiftUI 是"声明式"：<strong>你直接描述"界面上有一个红色按钮写着'点我'"</strong>，怎么画、什么时候重画，系统自己操心。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 第一个 SwiftUI 视图</span><span class="dots">···</span>
:::

```
import SwiftUI

struct ContentView: View {
    var body: some View {      // body：描述"界面长什么样"
        VStack {               // 竖着排列
            Text("你好，世界！")
                .font(.largeTitle)      // 修饰符：大标题
            Button("点我") {
                print("被点击了")
            }
            .buttonStyle(.borderedProminent)  // 蓝色实心按钮
        }
        .padding()
    }
}
```
:::

关键点：<strong>视图 = 遵守 View 协议的结构体</strong>，<code class="inline">body</code> 属性描述界面，<code class="inline">.修饰符()</code> 链式"上妆"。这就是 SwiftUI 的全部基本盘。

#### 二、基础视图：文字、按钮、输入框、图片

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">视图</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">干什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">示例</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">显示文字</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Text("你好")</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">按钮</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Button("点我") { 动作 }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">输入框</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">TextField("提示", text: $文本)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">显示图片</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Image(systemName: "star.fill")</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
SwiftUI 四大基础视图

注意 <code class="inline">Image(systemName:)</code>——苹果内置了 <strong>SF Symbols</strong> 图标库（几千个免费图标），"star.fill" 这种名字就能直接显示一个实心星星。这是 iOS 开发的隐藏福利：<strong>做界面几乎不用找图标素材</strong>。

#### 三、布局三件套：VStack、HStack、ZStack

- <strong>VStack</strong>：竖着排（像排队打饭）；
- <strong>HStack</strong>：横着排（像并排坐）；
- <strong>ZStack</strong>：叠着放（像扑克牌摞一起，适合做角标、遮罩）。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 布局三件套 + 常用修饰符</span><span class="dots">···</span>
:::

```
VStack(alignment: .leading, spacing: 12) {
    HStack {
        Text("账单")
        Spacer()                 // 弹性空间：把右边推到尽头
        Text("-25.5 元").foregroundColor(.red)
    }
    Divider()                    // 分割线
    Text("备注：午饭")
}
.padding(16)                     // 四周留白
.background(Color(.systemGray6)) // 浅灰底
.cornerRadius(12)                // 圆角

// 修饰符顺序有意义：先 padding 再 background，背景不含边距
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>注意：修饰符顺序有讲究

{class="mt-1"}
<code class="inline">padding(16).background(灰)</code> 和 <code class="inline">background(灰).padding(16)</code> 效果不同——前者"先留白再涂色"（背景不含边距），后者"先涂色再留白"（背景包含边距）。新手最常见的"奇怪白边"都源于此。不确定时调换顺序，预览立刻告诉你答案。
:::

#### 四、状态与绑定：让界面"活"起来

静态界面没意思。SwiftUI 的规则：<strong>界面永远忠实反映状态，状态变了，界面自动重画</strong>。

::: div .code-block
:::inline div .code-head
<span>SWIFT · @State 计数器</span><span class="dots">···</span>
:::

```
struct CounterView: View {
    @State private var count = 0   // @State：这个值变了要重画

    var body: some View {
        VStack {
            Text("你点了 \(count) 次")
            Button("点我 +1") {
                count += 1          // 改状态，界面自动刷新
            }
        }
    }
}
```
:::

输入框要用"双向绑定"——<code class="inline">$</code> 符号把"值和修改权"一起传进去：

::: div .code-block
:::inline div .code-head
<span>SWIFT · @Binding 双向绑定</span><span class="dots">···</span>
:::

```
struct InputView: View {
    @State private var text = ""

    var body: some View {
        TextField("输入点什么", text: $text)  // $ 双向绑定
            .textFieldStyle(.roundedBorder)
        Text("你输入了：\(text)")   // 输入时实时更新
    }
}
```
:::

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> 用户操作</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> 状态改变（count += 1）</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> SwiftUI 感知到变化</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> 自动重画界面（body 重新计算）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
图 3：SwiftUI 的"状态 → 界面"单向数据流
:::

#### 五、预览、主题与动画：SwiftUI 的"外挂"

- <strong>#Preview 宏</strong>：文件底部加 <code class="inline">#Preview { ContentView() }</code>，右侧画布实时渲染——改代码所见即所得；
- <strong>深色模式免费</strong>：用系统颜色（<code class="inline">Color(.systemGray6)</code>、<code class="inline">.primary</code>）而不是写死颜色，深色模式自动适配，一行不用多写；
- <strong>动画一行搞定</strong>：<code class="inline">withAnimation { count += 1 }</code> 或给视图加 <code class="inline">.animation(.default, value: count)</code>——过渡丝滑。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 十分钟上手的动画</span><span class="dots">···</span>
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
<i class="fas fa-lightbulb mr-2"></i>小贴士：先功能后动画

{class="mt-1"}
新手常犯的毛病是"界面还没做对，就开始纠结动画"。先让功能跑通，最后再统一加动效——动画是锦上添花，功能是雪中送炭。这也是咱们一贯的"简单至上"原则。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：做一个"心情按钮"

#### 六、常用修饰符速查：一页在手，界面不愁

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">想做什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">修饰符</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">留白</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.padding(16)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">圆角</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cornerRadius(12)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">背景色</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.background(Color(.systemGray6))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">字体与字号</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.font(.title.bold())</code> / <code class="inline">.font(.system(size: 20))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">前景色（文字/图标）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.foregroundColor(.red)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">撑满宽度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(maxWidth: .infinity)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">固定尺寸</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(width:100, height: 44)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">对齐方式</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack(alignment: .leading)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">透明度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.opacity(0.6)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">阴影</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.shadow(radius: 5)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">点击手势</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.onTapGesture { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">键盘类型</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.keyboardType(.decimalPad)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
SwiftUI 常用修饰符速查

记不住没关系——这页就是用来查的。用得最多的其实就前四个：padding、圆角、背景、字体。

{class="mt-1"}
把模板项目改成一个心情切换器：一个按钮，点击后在 😀开心 → 😢难过 → 😡生气 之间循环切换，文字和背景色跟着变。提示：用数组存三组（文字+颜色），<code class="inline">@State</code> 存下标，点击时 <code class="inline">(index + 1) % 3</code>。做完发给朋友玩，收获第一波"哇你会做 App 了"。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- SwiftUI 是声明式：描述"长什么样"，系统负责画和重画
- 视图 = 遵守 View 协议的结构体；body 描述界面；修饰符链式"上妆"
- 四大基础视图：Text / Button / TextField / Image；SF Symbols 图标库免费管饱
- 布局三件套：VStack 竖排、HStack 横排、ZStack 叠放；Spacer 是弹性空间
- @State 让界面活起来；$ 双向绑定喂给输入框
- #Preview 所见即所得；系统颜色自动适配深色模式；withAnimation 一行动效
:::
