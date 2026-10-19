---
id: di-liu-shi-zhang
num: 60
part: ios-kai-fa-pian
nav: 第六十章：搭建开发环境——Xcode与第一个项目
toc: default
kind: chapter
---

### 第六十章：搭建开发环境——Xcode 与第一个项目

{class="chapter-intro mb-4"}
工欲善其事，必先利其器。这一章咱们把"厨房"搭好：装好 Xcode、跑通模拟器、创建人生第一个 iOS 项目，再把工程结构拆开看个明白。装好环境之后，你会第一次看到自己写的代码变成一个能点的按钮——这个瞬间，很多人会记一辈子。

#### 一、准备一台 Mac

先说门槛：iOS 开发必须在 macOS 上进行。如果你没有 Mac，选项有三：买一台（哪怕是二手 Mac mini 或 MacBook Air 都够用）、短期租云 Mac、或者先读第八篇《安卓开发实战篇》（Windows 就能干）。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">配置项</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">最低要求</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">舒适线（推荐）</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">芯片</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Silicon（M1 起）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">M2 及更新</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">内存</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8GB</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">16GB</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">磁盘</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">预留 40GB+（Xcode 本体很胖）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256GB 起步</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系统</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最新 macOS</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">保持自动更新</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Mac 开发机配置参考（2026 年 8 月）

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：没有 Mac 也能先学语言

{class="mt-1"}
iPad 上免费的 <strong>Swift Playgrounds</strong> 能学 Swift 语言基础（不用 Mac）；甚至 iPhone 上也能装。先把第 61 章的语言知识在 Playgrounds 里玩熟，等拿到 Mac 后直接起飞。磨刀不误砍柴工，说的就是这个。
:::

#### 二、安装 Xcode

Xcode 是苹果官方的集成开发环境，免费。三步装好：

1. Mac 上打开 <strong>App Store</strong>，搜索 "Xcode"，点安装——注意它有好几个 GB，找个网速好的时段；
2. 装完首次启动，同意协议、装完组件（自动完成）；
3. 菜单 Xcode → Settings → Locations，确认 <strong>Command Line Tools</strong> 已选中——命令行工具是很多脚本和第三方工具的前提。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>注意：版本和系统的"匹配游戏"

{class="mt-1"}
新 Xcode 往往要求最新 macOS，旧 Mac 则会卡在老版本。上架 App Store 时，苹果会要求用<strong>较新的 Xcode</strong> 构建（通常给一个宽限期）。所以系统更新别拖太久——iOS 开发者是"追新版"最勤快的一群人。
:::

#### 三、创建你的第一个项目

打开 Xcode → <kbd>Create New Project</kbd> → 选 <strong>iOS → App</strong> 模板，然后填：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">配置项</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">填什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">说明</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Product Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstApp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">应用名字</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">你的 Apple ID（免费）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">签名用，个人账号即可</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Organization Identifier</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">和 Product Name 拼成包标识</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interface</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">本书主线框架</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Language</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不解释</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
创建项目要填的五件事

点 Create 后，Xcode 会生成一个能直接跑的项目。左上角选一台模拟器（比如 iPhone 17），点 ▶ 运行——几秒后，模拟器屏幕上出现一个写着 "Hello, world!" 的窗口。<strong>你的第一个 iOS App 已经诞生了</strong>。

#### 四、工程结构拆解：每个文件是干嘛的

左侧是工程导航器，新手只需认识这几个：

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="290" viewBox="0 0 600 290" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="290" fill="#fafafa" rx="8"/>
      <text x="20" y="28" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ 项目根目录</text>
      <rect x="30" y="42" width="540" height="225" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <rect x="45" y="56" width="250" height="196" fill="#eef2ff" rx="5"/>
      <text x="56" y="78" font-size="11" fill="#1e1b4b" font-weight="bold">MyFirstApp/（代码目录）</text>
      <text x="66" y="100" font-size="10" fill="#374151">├ MyFirstAppApp.swift  ← 程序入口</text>
      <text x="66" y="120" font-size="10" fill="#374151">├ ContentView.swift  ← 主界面</text>
      <text x="66" y="140" font-size="10" fill="#374151">└ Assets.xcassets  ← 图标、图片、颜色</text>
      <text x="56" y="166" font-size="10" fill="#6b7280">（新增文件都放这个目录下）</text>
      <text x="56" y="196" font-size="10" fill="#1e1b4b" font-weight="bold">Info 标签页 / Info.plist</text>
      <text x="66" y="216" font-size="10" fill="#6b7280">应用声明：名字、权限、设置</text>
      <rect x="310" y="56" width="245" height="196" fill="#f0fdf4" rx="5"/>
      <text x="321" y="78" font-size="11" fill="#065f46" font-weight="bold">其他重要位置</text>
      <text x="331" y="100" font-size="10" fill="#374151">📁 Preview Content/  ← 预览素材</text>
      <text x="331" y="122" font-size="10" fill="#374151"><i class="fas fa-bullseye mr-1"></i> Target 设置（蓝色工程图标）</text>
      <text x="331" y="142" font-size="10" fill="#6b7280">——版本号、最低系统、签名都在这</text>
      <text x="331" y="168" font-size="10" fill="#374151"><i class="fas fa-flask mr-1"></i> MyFirstAppTests/  ← 单元测试</text>
      <text x="331" y="188" font-size="10" fill="#374151">📱 MyFirstAppUITests/ ← 界面测试</text>
      <text x="331" y="216" font-size="10" fill="#9ca3af">（测试模板已生成，第 67 章用）</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
图 2：新手必懂的 Xcode 工程结构
:::

- <strong>MyFirstAppApp.swift</strong>：程序入口，SwiftUI 里它只有几行——"启动，然后显示主界面"；
- <strong>ContentView.swift</strong>：主界面视图，你现在看到的一切都在这里；
- <strong>Assets.xcassets</strong>：资源仓库——图标、图片、颜色都放这；
- <strong>Target 设置</strong>：点左侧蓝色工程图标进去，版本号、最低 iOS 版本、签名都在里面。App 显示名、图标也在这配置。

#### 五、真机调试：把 App 装进你的 iPhone

#### 五、Xcode 效率技巧：新手的五个"快捷键外挂"

用熟这几个，你会显得"很专业"：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">操作</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">快捷键</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">作用</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">运行</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">编译并跑起来</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">打开/切换画布预览</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">所见即所得的开关</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">格式化缩进</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自动整理选中代码的缩进</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">快速打开文件</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">输入文件名秒开（最常用！）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">注释/取消注释</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">调试时随手开关代码</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Xcode 高频快捷键（新手五件套）

另外两个隐藏福利：<strong>多开模拟器</strong>（同时跑 iPhone 和 iPad 对比布局）和<strong>代码片段库</strong>（把常用的几行代码拖进右侧 Snippets 面板，下次一键插入）——效率工具先用起来，手感自然就上来了。

#### 六、真机调试：把 App 装进你的 iPhone

模拟器虽好，真机才是终点。用免费 Apple ID 也能真机调试：

1. 数据线连上 iPhone（或同 Wi-Fi 无线调试）；
2. Xcode 顶部设备列表选你的手机，首次会提示登录 Apple ID 并自动配置签名；
3. iPhone 上 [设置] → [通用] → [VPN与设备管理] → 信任你的开发者证书；
4. 点 ▶，App 装进真机。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>注意：免费账号的"七天限制"

{class="mt-1"}
免费 Apple ID 签名的 App <strong>7 天后会失效</strong>（重新运行一次即可续期）。这是苹果的防滥用机制，学习阶段完全够用；付费开发者账号（99 美元/年）则没有这个限制，第 67 章细说。
:::

#### 七、小试牛刀 + 常见报错急救

#### 六、小试牛刀 + 常见报错急救

打开 ContentView.swift，把 <code class="inline">Text("Hello, world!")</code> 里的字换成你的名字，按 <kbd>⌘R</kbd> 重新运行——几秒后模拟器上就显示你的名字。恭喜，你完成了第一次完整的"改代码 → 编译 → 安装 → 运行"循环。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">报错现象</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">常见原因</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">解药</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Signing 报错</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team 没选、证书过期</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Target → Signing 里勾上你的账号；免费账号重跑一次</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">模拟器黑屏/打不开</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">镜像损坏</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">菜单 Device → Erase All Content；或删掉重加模拟器</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode 下载慢/装不上</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">App Store 网络波动</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">换时段；或到苹果开发者网站下载 .xip 离线包</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
新手环境报错急救表

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：完成你的"开发仪式感"清单

{class="mt-1"}
① 装好 Xcode 并跑通模拟器；② 用真机跑一次自己的 App 并截图留念；③ 把 Hello 文字改成你的名字；④ 到 Target 设置里把 App 显示名改成"我的第一个App"。做完这四步，你就是有作品的人了。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 硬门槛：Mac + Xcode；没有 Mac 先用 iPad 上的 Swift Playgrounds 学语言
- Xcode 从 App Store 装；新版本要求新系统，更新别拖
- 新建项目五要素：名字、Team、组织标识、SwiftUI、Swift
- 工程口诀：代码都在 MyFirstApp/ 目录；Target 设置管版本与签名
- 免费 Apple ID 真机调试有 7 天签名限制；付费账号无此限制
- 开发日常 = 改代码 → ⌘R → 看效果，循环往复
:::
