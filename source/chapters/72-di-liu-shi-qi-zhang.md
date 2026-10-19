---
id: di-liu-shi-qi-zhang
num: 67
part: ios-kai-fa-pian
nav: 第六十七章：打磨与发布——上架App Store
toc: default
kind: chapter
---

### 第六十七章：打磨与发布——测试、调试与上架 App Store

{class="chapter-intro mb-4"}
App 做出来了，然后呢？这一章回答"从能跑"到"能交付"的三件事：怎么高效地调试找 bug、怎么写测试防回归、怎么把 App 送上 App Store 让全世界下载。上架不只是仪式感——它是把一个作品变成产品的分水岭。

#### 一、调试三板斧：print、断点、预览

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">工具</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">干什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">怎么用</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">print + 控制台</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">看运行日志</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">代码里 print("值=\(x)")，Xcode 底部控制台看输出</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">断点调试</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">让程序停在某行，看变量值</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">行号旁点一下出蓝标，运行到那里暂停，逐步走</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI 预览 + 调试器</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">实时看界面与视图层级</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">#Preview 画布 + 运行时的 View Hierarchy 检查器</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
调试三板斧

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：崩溃了怎么读？

{class="mt-1"}
Swift 崩溃时控制台会打印 "Fatal error" 加原因，Xcode 会停在出错那一行并高亮。真机上的历史崩溃可以在 Xcode → Window → Organizer → Crashes 里看（需付费账号）。关键词优先搜 <strong>"错误原因第一句 + swiftui"</strong>——精确的问题，才有精确的答案。
:::

#### 二、测试：给代码上保险

手测靠不住——改了这个功能，另一个悄悄坏了。测试就是"后悔药"兼"防弹衣"。iOS 用 <strong>XCTest</strong> 框架，分两种：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">层级</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">测什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Target</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">速度</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">单元测试</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">纯逻辑（计算、校验）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppTests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">秒级</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UI 测试</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真实界面行为</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppUITests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分钟级</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">手动测试</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真人感受、体验</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">永远需要</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
iOS 测试层级（模板项目已预置两个 Test Target）

::: div .code-block
:::inline div .code-head
<span>SWIFT · 单元测试示例</span><span class="dots">···</span>
:::

```
import XCTest

// 把"金额字符串转数字"这种逻辑抽成纯函数
func parseAmount(_ input: String) -> Double? {
    guard let v = Double(input.trimmingCharacters(in: .whitespaces)),
          v > 0 else { return nil }
    return v
}

final class AmountTests: XCTestCase {
    func testEmptyInputReturnsNil() {
        XCTAssertNil(parseAmount(""))
    }
    func testNegativeReturnsNil() {
        XCTAssertNil(parseAmount("-5"))
    }
    func testNormalValueParses() {
        XCTAssertEqual(parseAmount("12.5"), 12.5)
    }
}
```
:::

跑测试：<kbd>⌘U</kbd>。全绿之后再改代码，心里有底。记账本里的金额校验、汇总计算，都该有单元测试罩着。

#### 三、签名与打包：给 App 盖上"印章"

每个 iOS App 都必须<strong>签名</strong>才能安装——证明"这个包出自你，没被篡改"。层级关系：

- <strong>学习阶段</strong>：免费 Apple ID + Xcode 自动签名（Personal Team），真机可跑，7 天续期一次；
- <strong>分发阶段</strong>：付费开发者账号（99 美元/年）签发证书与描述文件，才能上架和长期安装。

打包：Xcode 菜单 Product → Archive（归档），构建完成后在 Organizer 里 <kbd>Distribute App</kbd> → 选 App Store Connect → 上传。<strong>归档必须用 Generic iOS Device 作为目标</strong>（不是模拟器），这是新手常忘的一步。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>避坑提醒：证书丢了 = 更新断档

{class="mt-1"}
签名证书和私钥一旦丢失，你无法再给旧 App 发更新——用户只能装"全新"应用。妥善备份证书（钥匙串导出 .p12）并记好密码。好在苹果提供了"自动签名"和云证书管理（Xcode 里勾选 Automatically manage signing），能省掉大部分手工操作的坑。
:::

#### 四、上架 App Store 全流程

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> 注册开发者账号</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> 准备商店素材</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> 上传构建包</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> 填隐私与审核信息</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> 苹果审核（1-7 天）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> 上架</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
图 5：App Store 上架六步走
:::

- <strong>注册</strong>：developer.apple.com，个人账号 99 美元/年；
- <strong>素材</strong>：图标（1024×1024，别带圆角——苹果自己切）、截图（iPhone 各尺寸）、描述、隐私政策链接；
- <strong>隐私问卷</strong>：如实申报收集了哪些数据——不联网的记账本可以"不收集任何数据"；
- <strong>审核</strong>：首次提交常有 1-7 天等待，被拒就按"审核备注"逐条改——苹果的拒绝理由通常写得非常具体，照做即可；
- <strong>TestFlight</strong>：上架前先把测试版发给朋友内测（最多 10000 人），收集一轮反馈再正式提交，专业范儿十足。

#### 五、商店素材怎么做：第一印象就是下载量

商店页是用户"逛店"时看到的橱窗。三个素材决定第一印象：

- <strong>图标</strong>：1024×1024，别用截图凑合。没设计能力就用 AI 工具生成一个简洁图形，<strong>在桌面上缩小后还能一眼认出</strong>才算合格；
- <strong>截图</strong>：至少 2 套（iPhone 主流尺寸），展示最核心的功能场景；每张配一句人话文案（"一秒记一笔"比"高效的记账解决方案"好十倍）；
- <strong>描述</strong>：第一句说清"这是什么 + 给谁用"，别堆砌"最专业、最强"——真诚比夸张有效。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：把记账本"交付"一次

#### 六、崩溃上报与性能优化小清单

App 上架前，这两件事值得各花半小时：

##### 1. 崩溃监控

你测试时没崩，不代表用户手机不崩。苹果在 Xcode Organizer 里提供免费的崩溃报告（付费账号可看真机崩溃日志）；更省心的方案是接入第三方 SDK（如 Firebase Crashlytics）。<strong>没有崩溃监控的上架，等于闭着眼睛开车</strong>。

##### 2. 性能自查四条

1. <strong>列表用 LazyVStack / List</strong>：长列表别用普通 VStack 硬排——懒加载是性能第一课；
2. <strong>图片别硬塞原图</strong>：用 AsyncImage（远程图）和系统缓存，5MB 原图足以卡爆老机型；
3. <strong>别在主线程干重活</strong>：网络、大文件都走 async/await；
4. <strong>用 Instruments 量一量</strong>：Xcode 自带的性能分析器（Time Profiler、内存泄漏检查）——先测量，再优化，别凭感觉。

{class="mt-1"}
① 给 parseAmount 等逻辑补 3 个单元测试（⌘U 跑绿）；② 用断点亲手抓一个自己制造的崩溃并修好；③ Product → Archive 打一个包，走 TestFlight 邀请朋友内测；④ 有余力就注册开发者账号，把记账本真正提交上架。前三步今晚就能做完。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 调试三板斧：print 日志、断点、SwiftUI 预览与视图检查器
- XCTest：单元测试（⌘U）+ UI 测试 + 手动测试，模板已预置
- 签名：免费账号自动签名（7 天续期）；付费账号才能分发
- 打包：Generic iOS Device + Archive + Distribute；证书务必备份
- 上架六步：注册 → 素材 → 上传 → 隐私问卷 → 审核 → 上架；TestFlight 先内测
:::
