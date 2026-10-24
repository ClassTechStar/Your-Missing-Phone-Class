---
id: di-wu-shi-liu-zhang
num: 56
part: an-zhuo-kai-fa-pian
nav: 第五十六章：打磨与发布——上架Google Play
toc: default
kind: chapter
---

### 第五十六章：打磨与发布——测试、调试与上架 Google Play

{class="chapter-intro mb-4"}
App 做出来了，然后呢？这一章回答"从能跑"到"能交付"的三件事：怎么高效地调试找 bug、怎么写测试防回归、怎么把 App 送上 Google Play 让全世界下载。上架不只是仪式感——它是把一个作品变成产品的分水岭。

#### 一、调试三板斧：Logcat、断点、UI 检查器

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">工具</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">干什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">怎么用</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logcat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">看系统/自己打的日志</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">代码里 Log.d("TAG","值=$x")，面板里搜 TAG 过滤</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">断点调试</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">让程序停在某行，看变量值</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">行号旁点一下出红点，Debug 模式运行，逐步走</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Layout Inspector</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">看运行中的界面结构</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">菜单 Tools → Layout Inspector，实时看组件树</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
调试三板斧

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：报错怎么读？

{class="mt-1"}
崩溃后 Logcat 里会有红色堆栈（Stacktrace），从下往上找 <strong>第一个自己包名开头的行</strong>（比如 com.example.yourapp），那行基本就是案发现场。先看"Exception 类型"（空指针？类型转换？），再看"at ... 你的文件:行号"。这招能解决 80% 的崩溃。
:::

#### 二、测试：给代码上保险

手测靠不住——改了这个功能，另一个悄悄坏了。测试就是"后悔药"兼"防弹衣"。安卓测试分三层，新手先吃透第一层：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">层级</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">测什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">放哪里</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">速度</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">单元测试</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">纯逻辑（计算、校验）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/test/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">秒级</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">仪器测试</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真实设备上的界面行为</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/androidTest/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分钟级</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">手动测试</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真人感受、体验</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">永远需要</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
测试三层

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 单元测试示例</span><span class="dots">···</span>
:::

```
// 把"金额字符串转数字"这种逻辑抽成纯函数
fun parseAmount(input: String): Double? {
    val v = input.trim().toDoubleOrNull()
    return if (v != null && v > 0) v else null
}

// 测试它（JUnit4）
@Test
fun emptyInputReturnsNull() {
    assertEquals(null, parseAmount(""))
}
@Test
fun negativeReturnsNull() {
    assertEquals(null, parseAmount("-5"))
}
@Test
fun normalValueParses() {
    assertEquals(12.5, parseAmount("12.5"))
}
```
:::

记账本里的金额校验、统计计算，都该有单元测试罩着。跑测试：右键 test 目录 → Run。绿色全过，放心改代码。

#### 三、签名打包：给 App 盖上"印章"

安卓要求所有安装包必须<strong>签名</strong>——就像盖公章，证明"这个包是我出的，没被篡改"。调试时 Android Studio 自动用 debug 签名；发布要用自己的 release 签名。流程：

1. 菜单 Build → Generate Signed Bundle / APK；
2. 创建 keystore 文件（密钥库）——<strong>设置密码并妥善保管</strong>；
3. 选择 release + AAB 格式，构建完成。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>避坑提醒：keystore 丢了 = App 丢了

{class="mt-1"}
上架后更新 App 必须用<strong>同一个</strong>签名，否则商店会拒绝更新。keystore 文件和密码一旦丢失，你只能换个新应用重新上架——老用户全都接不上。务必把 keystore 和密码备份到安全的地方（云盘加密 + 记事本），这是安卓开发者最昂贵的教训之一。
:::

#### 四、上架 Google Play 全流程

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> 注册开发者账号</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> 准备商店素材</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> 上传 AAB</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> 填数据安全表</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> 审核（数小时~数天）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> 上架</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
图 6：Google Play 上架六步走
:::

- <strong>注册</strong>：一次性 25 美元注册费，需能用的 Google 账号；
- <strong>素材</strong>：应用图标（512×512）、截图（至少 2 张）、功能描述、隐私政策链接（收集数据必填）；
- <strong>数据安全表</strong>：如实申报收集了哪些数据——不联网的记账本可以"零收集"；
- <strong>审核</strong>：新账号首次上架常被人工审核，数小时到数天不等，被打回就按意见改。

国内用户注意：Google Play 需要特殊网络环境，且中国大陆地区分发通常走国内商店（华为、小米、应用宝等）。<strong>上架国内商店的流程类似，但各商店有自己的审核口味</strong>——同一个 AAB/APK 可以多店分发。作为练手，先走通一家就赢了。

#### 五、商店素材怎么做：第一印象就是下载量

商店页是用户"逛店"时看到的橱窗。三个素材决定第一印象：

- <strong>图标</strong>：512×512，别用截图凑合。没设计能力就用 AI 工具生成一个简洁几何图形，<strong>在手机桌面上缩小后还能一眼认出</strong>才算合格；
- <strong>截图</strong>：至少 2 张，最好 4-6 张，展示最核心的功能场景；每张配一句人话文案（"一秒记一笔"比"高效的记账解决方案"好十倍）；
- <strong>描述</strong>：第一句说清"这是什么 + 给谁用"，别堆砌"最专业、最强"——商店搜索权重主要看关键词和下载转化，真诚比夸张有效。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：A/B 看看同行

{class="mt-1"}
上架前逛一圈商店里同类 App 的前十名，截图对比：他们图标什么风格？截图讲什么卖点？标题怎么写？<strong>模仿不是抄袭</strong>——学套路、换自己的内容，这是所有产品冷启动最快的一课。
:::

#### 六、性能优化与崩溃上报小清单

App 上架前，这两件事值得各花半小时：

##### 1. 性能自查四条

1. <strong>列表用 LazyColumn</strong>：长列表千万别用 Column 硬排——懒加载是安卓性能的第一课；
2. <strong>图片别硬塞原图</strong>：用 Coil 图片库自动缩放缓存，一张 5MB 原图足以卡爆低端机；
3. <strong>避免在主线程干重活</strong>：数据库、网络、大文件都在协程里做；
4. <strong>用 Profiler 量一量</strong>：Android Studio 自带的性能分析器能看内存、CPU、耗电——先测量，再优化，别凭感觉。

##### 2. 崩溃上报

你测试时没崩，不代表用户手机不崩。上架前接入 <strong>Firebase Crashlytics</strong>（谷歌官方，免费）：几行配置，用户崩溃时自动上报堆栈，你在后台就能看到"哪个机型、哪个版本、崩在哪一行"。<strong>没有崩溃监控的上架，等于闭着眼睛开车</strong>。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：把记账本"交付"一次

{class="mt-1"}
① 给 parseAmount 等逻辑补 3 个单元测试；② 用 Logcat 亲手抓一个自己制造的崩溃并修好；③ 生成一个 release 签名的 APK，发给朋友安装（这才是"作品"的仪式感）；④ 有余力就注册开发者账号，把记账本真正提交上架。前三条今晚就能做完。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 调试三板斧：Logcat 看日志、断点看变量、Layout Inspector 看界面
- 读崩溃：从堆栈下往上找自己包名的第一行
- 测试三层：单元（秒级，先学这个）/仪器/手动
- 发布必须签名：keystore 和密码备份好，丢了 App 就"换人"了
- 上架六步：注册 → 素材 → 上传 AAB → 数据安全表 → 审核 → 上架
:::
