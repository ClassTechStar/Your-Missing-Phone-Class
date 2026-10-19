---
id: di-er-shi-zhang-jinjie
num: 20
part: jin-jie-pian
nav: 第二十章：开发者模式与高级权限
toc: default
kind: supplement
---

### 第二十章：开发者模式与高级权限

{class="chapter-intro mb-4"}
这一章是给那些想要深入探索手机"隐藏功能"的用户准备的。开发者模式、Root权限、BL锁……这些听起来很极客的概念，其实离普通用户并不遥远。

#### 一、开发者模式：解锁隐藏设置

开发者模式是手机系统内置的一个隐藏菜单，里面有很多普通用户用不到但开发者需要的功能。

##### 如何开启：

- <strong>安卓</strong>：进入设置 > 关于手机 > 连续点击"版本号"7次，直到提示"您已处于开发者模式"。
- <strong>鸿蒙</strong>：设置 > 关于手机 > 连续点击"HarmonyOS版本"7次。
- <strong>iOS</strong>：普通用户无法开启完整的开发者模式，需要付费的Apple Developer账号。

##### 常用功能一览：

- <strong>USB调试</strong>：连接电脑进行高级操作（如刷机、数据恢复、ADB命令）的必开开关，详见本章"ADB实用命令"小节。
- <strong>显示触摸操作</strong>：屏幕上显示触摸点（一个小圆点跟随手指），适合录制操作教程或演示。

##### 性能与流畅度相关：

- <strong>动画速度调节（窗口动画缩放 / 过渡动画缩放 / 动画程序时长缩放）</strong>：这三个选项控制打开App、切换页面时的动画时长。默认是1x，调到0.5x会让手机"看起来"更快（实际上程序运行速度没变，只是动画变快了），调到关闭则直接无动画跳转。多数极客会设为0.5x，既保留过渡感又显快；完全关闭会让操作显得生硬，并且可能掩盖程序真实的卡顿，反而让你误以为"很流畅"。
- <strong>强制GPU渲染（Force GPU Rendering）</strong>：强制所有2D绘图通过GPU而非CPU处理。在老旧机型或某些App优化不佳时能提升滚动流畅度，但也会增加GPU负载和耗电。现代手机默认已大量使用GPU渲染，这个开关对中高端机型影响有限，更多是历史遗留选项，普通用户保持默认即可。
- <strong>显示GPU呈现模式分析（Profile GPU Rendering）</strong>：在屏幕上以柱状图实时显示每帧的渲染耗时，绿色横线代表16.6ms（60fps的帧时间阈值）。柱子超过绿线就说明掉帧了。这是开发者排查App卡顿的利器，普通用户也可以用它来对比哪个App优化得差——比如某个App滚动时柱子经常飙到红线以上，那基本就是它的锅。

##### 后台与续航相关：

- <strong>后台进程限制</strong>：可以设置"标准限制""最多1个进程""最多2个进程"等。表面上看限制后台进程能省电，但实际上Android自带的后台管理已经做得不错，强行限制反而会导致App频繁重新加载（冷启动反而更耗电、体验也变差）。这个选项更适合调试用，不建议普通用户长期开启，保持"标准限制"即可。
- <strong>不保留活动</strong>：每离开一个界面就立即销毁它。极不推荐，会导致App频繁白屏、重新加载，仅用于测试App的恢复逻辑。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>注意事项

{class="mt-1"}
开发者模式里的设置可能会影响系统稳定性，不懂的选项不要乱改。开启USB调试后，连接电脑时要小心，不要连接不信任的电脑。
:::

#### 二、OEM解锁：开发者选项里的"刷机开关"

在开发者选项里有一个不太起眼但很重要的开关——"OEM解锁"（部分品牌叫"OEM解锁允许"或"设备解锁"）。这个开关本身不会解锁BL锁，但它是一个"前置许可"：只有打开它，厂商才允许你通过fastboot命令或品牌工具去解锁BL。

- <strong>开关的作用</strong>：相当于向厂商声明"我同意放弃保修、自负风险，请允许我解锁BL"。如果这个开关是关闭的，任何解锁BL的命令都会被直接拒绝。
- <strong>与BL锁的关系</strong>：OEM解锁是"申请资格"，BL解锁才是"实际操作"。前者在手机设置里点一下就行，后者需要去厂商官网申请解锁码、用电脑跑fastboot命令（如 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing unlock</code>），二者缺一不可。
- <strong>恢复出厂设置会重置吗</strong>：会。"OEM解锁"开关在恢复出厂后会回到关闭状态，但BL锁一旦解锁就是物理级别的状态，不会因为恢复出厂而重新上锁——需要手动执行 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing lock</code> 才能重新上锁。
- <strong>什么时候应该打开</strong>：除非你确定要刷机或Root，否则保持关闭。它和"USB调试"是两个独立开关，刷机时通常需要同时打开。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>小知识：为什么厂商要设置这个开关

{class="mt-1"}
早期安卓没有这个开关，恶意软件只要拿到权限就能偷偷刷入系统。Google后来要求所有安卓厂商在开发者选项中加入"OEM解锁"开关，作为一道"用户知情同意"的确认。这也就是为什么即便你解了BL锁，如果OEM解锁开关被关闭，重新刷机仍然会失败。
:::

#### 三、BL锁（Bootloader锁）：刷机的第一道门

Bootloader是手机启动时加载操作系统的程序。BL锁就是厂商为了安全而加的锁，防止用户刷入非官方系统。

##### BL锁的作用：

- <strong>安全保护</strong>：防止恶意软件刷入系统。
- <strong>防盗</strong>：即使手机被刷机，没有原账号密码也无法使用。
- <strong>保修限制</strong>：解锁BL通常意味着失去官方保修。

##### 各品牌BL锁政策：

- <strong>小米</strong>：可以解锁，需要绑定账号等待期（7-30天）。
- <strong>华为</strong>：2018年后停止提供解锁码，基本无法官方解锁。
- <strong>一加</strong>：可以解锁，相对宽松。
- <strong>OPPO/vivo</strong>：部分机型可以解锁，需要申请。
- <strong>三星</strong>：可以解锁，但会触发Knox熔断，失去Samsung Pay等功能。
- <strong>苹果</strong>：iOS设备没有传统意义上的BL锁概念，但有类似的安全机制。

#### 四、ADB实用命令：通过电脑控制手机

ADB 全称 Android Debug Bridge（安卓调试桥），是 Google 官方提供的命令行工具，让电脑通过 USB 或 Wi-Fi 与安卓手机通信。它本身不需要 Root，只要手机开了"USB调试"就能用。可以把它理解为"用电脑给手机下指令的遥控器"——刷机、装App、传文件、查日志，都得靠它。

##### 如何通过 USB 连接：

1. 手机端：进入开发者选项 → 打开"USB调试"。
2. 电脑端：从 Google 官方下载 Platform Tools（含 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb</code> 和 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot</code> 两个可执行文件），解压到任意目录。
3. 用数据线连接手机和电脑，手机上会弹窗"是否允许USB调试"，勾选"始终允许"并确定。
4. 在电脑命令行（Windows 的 PowerShell 或 cmd）里执行 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code>，如果输出类似 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">List of devices attached / xxxxxxxx device</code>，就说明连上了。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>驱动和授权弹窗别忽略

{class="mt-1"}
Windows 用户如果 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code> 显示 "unauthorized" 或根本不列出设备，多半是驱动没装好或者忘了在手机上点"允许"。三星/小米等品牌可以装各自的"USB驱动"或"手机助手"来补齐驱动；Mac 和 Linux 一般免驱。如果手机弹窗被你手滑点掉了，拔插一下数据线就会重新弹出来。
:::

##### 常用 ADB 命令：

- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb install app.apk</code>：把电脑上的 APK 装到手机（<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-r</code> 表示覆盖安装并保留数据；<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code> 装到 SD 卡）。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb uninstall com.xxx.xxx</code>：按包名卸载 App。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb push 电脑路径 /sdcard/目标路径</code>：把电脑文件推送到手机。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb pull /sdcard/文件 电脑路径</code>：把手机文件拉到电脑（比发给自己微信再下载快得多）。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell</code>：进入手机的 Linux Shell，可以直接执行 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls</code>、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm</code>、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">am</code> 等命令。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot bootloader</code>：重启手机进入 Fastboot 模式（刷机的入口）。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot recovery</code>：重启进入 Recovery 模式。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages</code>：列出手机上所有已安装应用的包名（找包名必用）。加 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code> 只看系统应用，加 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-3</code> 只看第三方应用。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 包名</code>：为当前用户卸载预装 App，免 Root，详见下方实战。

##### 免 Root 卸载预装 App 实战：

这是 ADB 最实用的功能之一：用 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code> 命令可以为"当前用户"卸载预装 App，而不需要 Root，也不影响系统分区。被卸载的 App 在系统里"消失"，但实际还在系统分区里，恢复出厂设置后会回来。

1. 先用 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages -s</code> 列出所有系统应用，找到你想卸载的包名。比如小米浏览器是 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.browser</code>，华为应用市场是 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.vmall.client</code>。
2. 不确定包名对应哪个 App？可以在电脑上用 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages | findstr 关键字</code> 搜索，或者装一个第三方 App "Package Viewer"在手机上直接查看每个 App 的包名。
3. 执行卸载：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 包名</code>，比如 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 com.android.browser</code>。返回 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Success</code> 就成功了。
4. 想恢复怎么办？两种方法：① 恢复出厂设置（最彻底但麻烦）；② 重新安装：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell cmd package install-existing 包名</code>。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>千万别乱删系统核心包

{class="mt-1"}
"pm uninstall --user 0"虽然是免 Root 的安全方式，但乱删关键系统应用（如 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.systemui</code> 状态栏、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.phone</code> 电话、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.settings</code> 设置）会导致系统崩溃、黑屏、无法开机等严重问题。删之前先 Google 一下"这个包名能不能删"，宁可少删不要错删。建议一次只删一两个，确认没问题再继续。
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>小知识：--user 0 是什么意思

{class="mt-1"}
安卓 4.2 之后支持多用户，每个用户有独立的 ID（机主是 0，附加用户从 10 开始）。<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">--user 0</code> 表示"只对当前机主卸载"，系统分区里的 APK 文件依然存在，只是不给机主显示了。这就是为什么它不需要 Root——没动系统文件，只是改了"用户配置"。这也是它和 Root 后卸载最大的区别：Root 卸载是真正从系统里删掉，所有用户都不再有；ADB 卸载只是"对当前用户隐藏"。
:::

#### 五、Root权限：安卓的"超级管理员"

Root权限相当于Linux中的超级用户（对/目录拥有完全控制权，可以读写任意文件），是安卓系统的最高权限。它与Windows的Administrator有本质区别：Windows出于安全考虑对管理员做了诸多限制（真正的最高权限其实是 TrustedInstaller），即便是 Administrator 也无法像 Linux root 那样直接执行 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">sudo rm -rf /*</code>。获得Root权限后，你可以修改系统文件、卸载预装应用、使用需要Root的高级App。

##### Root的好处：

- 卸载无法卸载的预装应用。
- 使用高级功能App（如钛备份、绿色守护）。
- 修改系统界面和功能。
- 安装第三方Recovery和自定义ROM。

##### Root的风险：

- <strong>失去保修</strong>：大多数厂商不保修Root过的手机。
- <strong>安全风险</strong>：恶意App可能获得Root权限，造成严重后果。
- <strong>系统不稳定</strong>：误操作可能导致系统崩溃。
- <strong>银行App不能用</strong>：很多银行和支付App检测到Root会拒绝运行。
- <strong>OTA更新失败</strong>：可能无法正常接收官方系统更新。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>严重警告

{class="mt-1"}
Root操作有一定风险，可能导致手机变砖（无法开机）。如果你是新手，建议先充分了解相关知识，并确保有完整的备份。操作前请仔细阅读教程，确认你的机型和系统版本。
:::

#### 六、SafetyNet与Play Integrity认证：为什么Root后银行App不能用

很多Root用户都遇到过这样的崩溃瞬间：Root之后兴致勃勃地装了一堆模块，结果打开银行App——"您的设备不安全，无法使用"，Google Pay也用不了，连Netflix都拒绝高清播放。这背后是Google的两套设备完整性认证机制：旧的 SafetyNet 和新的 Play Integrity API。

##### 什么是 SafetyNet / Play Integrity：

- <strong>SafetyNet Attestation（旧版，2017年起）</strong>：Google 早期推出的设备完整性检查 API，应用通过它向 Google 服务器查询"这台设备是否通过 CTS 兼容性测试、是否处于未修改的官方状态"。返回结果分为 Basic Attestation（基础校验）和 Strong Attestation（强校验，依赖硬件密钥）。Google 已宣布 SafetyNet 将在 2024 年后逐步停用。
- <strong>Play Integrity API（新版，2022年起）</strong>：Google 推出的替代方案，比 SafetyNet 更严格也更全面。除了设备完整性，还包括"应用完整性"（App 是否被篡改）和"账号/授权完整性"（用户账号是否被 Google 信任）。新 App 应迁移到 Play Integrity。
- <strong>谁来用</strong>：银行、金融、支付类 App（如 Google Pay、各银行的网银、支付宝/微信支付的部分场景）、流媒体（Netflix 高清版权保护）、部分游戏反作弊（如腾讯/网易的部分游戏）、企业办公 App（MDM 设备合规性检查）。

##### Play Integrity 的三级认证结果：

- <strong>MEETS_DEVICE_INTEGRITY（设备完整性通过）</strong>：设备运行正版 Android 系统，Bootloader 未解锁，没有 Root，CTS 兼容性测试通过。可以正常使用银行、支付类 App。
- <strong>MEETS_BASIC_INTEGRITY（基础完整性通过）</strong>：设备基本可信，但可能存在轻微异常。某些 App 会降级使用（如 Netflix 仍可播放但限制清晰度），某些严格的银行 App 会直接拒绝。
- <strong>MEETS_STRONG_INTEGRITY（强完整性通过）</strong>：最高级别，要求硬件密钥背书（如 Google Pixel 系列的 Titan M 芯片），大多数第三方品牌机型即使未 Root 也达不到这一级。
- <strong>无任何标签（NO_INTEGRITY）</strong>：设备已 Root、解锁 BL、刷了第三方 ROM 或被识别为模拟器，绝大多数支付/银行 App 会直接拒绝运行。

##### 为什么 Root 后这些 App 会失效：

应用通过 Play Integrity API 向 Google 服务器发起认证请求，Google 会检查设备的多项指标——Bootloader 锁定状态、系统分区是否被修改、是否存在 su 二进制文件、SELinux 是否处于宽松模式等。任何一项异常都会导致返回的认证级别降低或为空，银行 App 一看"设备不安全"，自然就拒绝服务了。

##### 现代隐藏方案：Magisk Hide / Shamiko / Zygisk：

为了在享受 Root 便利的同时还能用银行 App，社区开发了一系列"隐藏 Root 状态"的方案。核心思路都是：让检测程序看到的不是一个被修改过的系统，而是一个"看起来正常"的设备。

- <strong>Magisk</strong>：当前最主流的 Systemless Root 方案——不修改系统分区，而是通过挂载的方式实现 Root。这样设计的好处是 OTA 更新失败的几率小、卸载比较干净，是后续所有隐藏方案的基础。但使用 Magisk 仍然需要解锁 BL 锁。
- <strong>Magisk Hide（已停更）</strong>：Magisk 早期内置的隐藏模块，能对指定 App 隐藏 Root。但 2021 年起已被 Magisk 官方移除，原因是 Google 持续升级检测手段，双方陷入"猫鼠游戏"。
- <strong>Zygisk</strong>：Magisk 24.0+ 引入的新机制，类似 Riru，通过注入 Zygote 进程实现模块加载，比直接修改系统更隐蔽。开启 Zygisk 是使用现代隐藏方案的前提。
- <strong>Shamiko</strong>：当前最主流的隐藏模块，配合 Zygisk 工作，可以为指定 App（"反向白名单"模式）隐藏 Root、隐藏 Magisk 自身、伪造 Bootloader 锁定状态。Shamiko 通过 LSPosed 仓库或 GitHub 分发。
- <strong>Play Integrity Fix（osm0sis）</strong>：专门针对 Google Play Integrity 检测的 Magisk 模块，会修改设备指纹（fingerprint）让 Google 认为你的设备是某个未 Root 的官方机型。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>猫鼠游戏永远不会结束

{class="mt-1"}
Google 每隔一段时间就会更新检测规则，App 厂商也会跟进升级 Play Integrity 校验。今天还能用的隐藏方案，明天可能就被识别。如果你完全依赖银行/支付 App（比如日常转账、扫码付款），最稳妥的选择仍然是：不要 Root、不要解 BL 锁。隐藏方案更适合"主力机不 Root + 备用机玩 Root"的玩家配置。
:::

#### 七、给普通用户的建议

- <strong>开发者模式</strong>：可以开启，体验一下动画加速、GPU 呈现分析等功能，但不要乱改其他不理解的选项。
- <strong>OEM 解锁与 BL 锁</strong>：如果你不打算刷机或 Root，两个开关都保持默认（关闭）状态最安全。
- <strong>ADB</strong>：免 Root 的强大工具，普通人也能用——比如用 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code> 卸载预装 App。但删之前一定要查清楚包名能不能删。
- <strong>Root</strong>：普通用户不建议 Root，风险大于收益。如果确实需要某些功能，可以先了解有没有不需要 Root 的替代方案（比如用 ADB 卸载预装、用 Shizuku 替代部分 Root 功能）。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：开启开发者模式并调整动画速度

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 进入设置 > 关于手机。
2. 连续点击"版本号"7次，直到提示已开启开发者模式。
3. 返回设置，找到"开发者选项"（通常在设置底部或"系统"里）。
4. 找到"窗口动画缩放"、"过渡动画缩放"、"动画程序时长缩放"，将它们都设为0.5x或关闭。
5. 感受一下手机是否变快了。
:::
