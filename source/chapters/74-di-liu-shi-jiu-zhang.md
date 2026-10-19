---
id: di-liu-shi-jiu-zhang
num: 69
part: ios-kai-fa-pian
nav: 第六十九章：速查手册与资源
toc: default
kind: chapter
---

### 第六十九章：速查手册与资源

{class="chapter-intro mb-4"}
本章是一份可以独立使用的速查手册。当你记不清某个写法或需要快速决策时，直接翻到这里。建议把它当成"口袋卡片"：常用代码速查、常见问题、学习资源，一页不落。

#### 一、常用代码速查卡

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要做什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">关键代码</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">页面私有状态</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@State private var x = 初值</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跨页面逻辑</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Observable class VM { var x = 0 }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">竖排/横排布局</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack { }</code> / <code class="inline">HStack { }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">弹性空间</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Spacer()</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">列表</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">List { ForEach(数组) { ... } }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">页面跳转</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">NavigationStack + NavigationLink</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">底部弹窗</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.sheet(isPresented: $show) { 内容 }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">关当前页</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Environment(\.dismiss) var dismiss</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">联网取数据</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">try await URLSession.shared.data(from: url)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">JSON 解析</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X: Codable</code> + <code class="inline">JSONDecoder().decode</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">存小配置</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">UserDefaults.standard.set(值, forKey: "键")</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">存结构化数据</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Model</code> + <code class="inline">modelContainer</code> + <code class="inline">@Query</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">深色模式适配</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用系统颜色（.primary / Color(.systemGray6)），不写死</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跑测试</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><kbd>⌘U</kbd></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
iOS 开发速查卡（2026 年 8 月版）

#### 二、常见问题 FAQ

<strong>Q1：我没有 Mac，能学 iOS 开发吗？</strong>

能学语言，不能做完整开发。iPad/iPhone 上的 Swift Playgrounds 可以学完第 61 章的全部内容；但 Xcode 是 macOS 独占，最终必须有一台 Mac。预算有限可以先租云 Mac 或买二手 Mac mini 过渡，学完语言再决定投入。

<strong>Q2：学 iOS 开发要花多少钱？</strong>

学习阶段：0 元（Xcode 免费 + 免费 Apple ID 真机调试）。发布阶段：开发者账号 99 美元/年（约 700 元）。加上一台 Mac 的硬件投入，这是全部成本。相比回报——App Store 上哪怕一个小工具也有付费用户——这笔账划算。

<strong>Q3：SwiftUI 和 UIKit 先学哪个？</strong>

<strong>SwiftUI</strong>。2026 年的新项目、新教程、新岗位都以 SwiftUI 为主，本书全程用它。UIKit 是上一代框架，仍在大量老项目中使用——等你 SwiftUI 熟练后，按需补 UIKit（官方有互操作教程），上手会很快。顺序别反了。

<strong>Q4：iOS 开发好找工作吗？</strong>

2026 年的行情：纯"会画界面"的初级岗位竞争激烈，但"懂 Swift + SwiftUI + 有上架作品"的开发者依然抢手。iOS 岗位的薪资中位数在各技术栈里常年靠前。学习期的你，<strong>最好的简历就是商店里那个自己做的 App</strong>。

<strong>Q5：App 被审核拒绝了怎么办？</strong>

别慌，很正常——首次提交被拒的概率不低。苹果的拒绝理由通常写得非常具体（哪个页面、哪条准则），逐条修改后在 App Store Connect 里回复说明，重新提交即可。常见的三大拒绝原因：权限用途说不清、界面有 bug、元数据（截图/描述）与实物不符。提前自查这三项，能省一轮等待。

#### 三、Xcode 高频快捷键速查

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">操作</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">快捷键</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">运行 / 测试</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R / ⌘U</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">打开画布预览</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">快速打开文件</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全局搜索</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘F</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">格式化缩进</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">注释 / 取消注释</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">清理构建缓存</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘K</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跳转到定义</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘ 点按</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">重命名（全局安全改名）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">右键 → Refactor → Rename</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Xcode 高频快捷键速查

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：编译玄学先清缓存

{class="mt-1"}
"昨天还能跑今天就不行"的灵异事件，十有六七是构建缓存错乱。<kbd>⇧⌘K</kbd> 清理后重新构建，能治愈一大半玄学问题。还不行就重启 Xcode（连 Mac 一起），再不行就"删掉 DerivedData 文件夹"——这是 iOS 开发者口口相传的终极三连。
:::

#### 四、推荐学习资源

#### 三、推荐学习资源

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">类型</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">资源</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">推荐理由</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">developer.apple.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">苹果官方文档，SwiftUI/Swift 教程都在里面，第一权威</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple 的 SwiftUI Tutorials</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方手把手课程，新手友好度满分</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift 官网 (swift.org)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">语言官方文档与在线演练场</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">社区</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hacking with Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Paul Hudson 的免费教程库，质量公认第一梯队</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">社区</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stack Overflow (swiftui 标签)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">报错求救第一站</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">视频</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Developer 官方频道（WWDC 视频）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每年新技术的权威讲解</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">设计</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple 人机界面指南（HIG）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">做出"苹果味"界面的官方圣经</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">配套</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第七篇《AI编程实战篇》（第37-47章）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用 AI 辅助 iOS 开发的完整心法</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
iOS 开发学习资源清单（2026 年 8 月）

#### 五、结语：从第一个 App 到第 N 个 App

回头看，你从"不知道 SwiftUI 是什么"，到装好 Xcode、学会 Swift、用 SwiftUI 画出界面、给 App 接上数据库和网络，再到测试、打包、上架——<strong>这条路上你已经走完了从零到一最难的一段</strong>。

技术的世界变化很快：框架会升级，工具会换代，AI 会接手越来越多"敲键盘"的活。但有一样东西不会过时：<strong>你把一个模糊的想法，拆解成清晰的步骤，再一步步实现它的能力</strong>。工具是放大器，思路是地基。放大器可以替换，地基不能动摇。

:::inline div .quote-line
你不再只是"会玩手机的人"。你能把脑海里的想法，变成数亿台 iPhone 上真实运行的 App。从今天开始，用键盘去创造——这就是 iOS 开发者的浪漫。
:::

#### 参考文献

{class="list-decimal pl-6 mb-3 space-y-1 text-xs text-gray-500"}
1. Apple Inc. (2026). SwiftUI Framework Documentation. developer.apple.com.
2. Apple Inc. (2026). Swift Programming Language Guide. swift.org.
3. Apple Inc. (2026). SwiftData Framework Documentation. developer.apple.com.
4. Apple Inc. (2026). App Store Review Guidelines. developer.apple.com/app-store/review.
5. Apple Inc. (2026). Human Interface Guidelines (HIG). developer.apple.com/design.
6. Apple Inc. (2026). Xcode 27 Release Notes and App Distribution Guide.
