---
id: di-er-shi-zhang-termux
part: jin-jie-pian
nav: 附：Termux便携式Linux终端
toc: sub
kind: supplement
---

### 第二十章附：Termux——Android设备上的便携式Linux终端环境

{class="chapter-intro mb-4"}
如果你觉得开发者模式还不够"硬核"，想要在手机上体验完整的Linux命令行，那么Termux正是为你准备的。它无需root权限，就能把一台普通的安卓手机变成一台便携的Linux工作站，是进阶用户探索移动端开发与运维的利器。

#### 一、什么是Termux

Termux是一款专为Android设备设计的开源终端模拟器和Linux环境应用程序，它无需root权限即可在手机上提供完整的Linux shell体验。作为一个轻量级应用（安装包仅30MB左右），Termux通过APT包管理系统支持丰富的软件生态，允许用户在移动设备上运行Python、Node.js、Git、SSH等工具，甚至搭建服务器或进行渗透测试。

Termux的核心优势在于轻量化和高度可扩展性，适合开发、学习及系统管理等多种场景。它将标准的软件包与精确的终端仿真结合在一个开源解决方案中。

##### 它到底是个啥：装在安卓里的一个终端窗口

先打个比方。你用电脑时偶尔打开过 CMD 或 PowerShell 吗？一个黑底白字、靠敲命令干活的窗口。Termux 做的事差不多：给安卓装上这么一个"命令行窗口"，窗口里跑的是一套为安卓移植好的 Linux 工具箱——shell、编辑器、编译器、包管理器都齐了。底层内核还是安卓自己的（安卓本来就基于 Linux 内核），所以它不跟你抢系统的控制权，只在属于自己的地盘里干活。

地盘在哪？Termux 的所有文件都装在 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">/data/data/com.termux</code> 这个目录里——这是安卓分配给它的私有沙盒。装好后在提示符后面敲 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">echo $HOME</code>，你会看到一个以 /data/data/com.termux/files/home 结尾的路径，那是它的"家"；再敲 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">echo $PREFIX</code> 能看到它整套软件的"根"。理解这一点很重要：Termux 里装的一切都在这个沙盒内，哪天你把 App 卸载了，沙盒连同里面所有东西一起消失——反过来说，想"重置"它，卸载重装就是彻底重置。

##### 为什么它不需要 root

root 是把安卓系统的最高权限拿到手，代价你多半听说过：失去保修、部分支付和银行 App 直接拒绝运行、刷坏了变砖。Termux 的聪明之处在于完全不碰这套东西——它以一个普通应用的身份安家，跟微信、地图一样受安卓的权限管理和沙盒约束。好处是零风险：装、卸都像普通应用一样干净利落。

代价是有些底层操作做不了：挂载新分区、修改系统文件、管理别的应用，都不行。但学习命令行、写代码、连服务器这些事，一样都不少。说句实在的，绝大多数人一辈子都用不上 root——包括现在正拿着手机看这本书的你。

##### 它和"真正的 Linux"差在哪

用电脑 Linux 的经验直接套过来，会有几个"咦，怎么不一样"的瞬间。它没有 systemd 这样的服务管理器，服务（比如后面要讲的 sshd）就是普通进程，开机自启要靠插件实现；它没有图形界面，纯命令行（折腾党可以配 VNC 看桌面，但默认玩法就是敲字）；它对后台进程没有豁免权，系统说冻结就冻结——这是和桌面 Linux 差距最大的一点，后面专门有一节讲怎么跟省电策略斗智斗勇。

想体验完整发行版怎么办？Termux 里有 proot-distro 这类工具，能装 Debian、Ubuntu 等系统进去玩（后面也会讲）。但要心里有数：那是无 root 权限下的模拟方案，性能和兼容性都打折扣，学习够用，生产别指望。

##### 它是怎么走到今天的

Termux 由 Fredrik Fornwall 创建，后来交由社区维护。早年谷歌商店里能直接装，后来安卓系统对应用执行自带二进制的限制一代比一代紧，商店版基本停更，官方把发布渠道转到了 F-Droid 和 GitHub Releases。所以今天再有人跟你说"去应用商店搜 Termux"，你可以直接把这一节甩给他：最新稳定版是 v0.118.3，适用于 Android ≥ 7，一切以 GitHub Releases 页面为准。这段历史也能解释一个现象——为什么网上搜到的老教程很多对不上号，环境变了，教程也得看日期。

##### 手机上跑 Linux 的几条路子

想在手机上用 Linux，其实不止 Termux 一条路，把几条路放一起比一比，你就知道自己要的是什么了：

- <strong>Termux 本体</strong>：沙盒里的 Linux 工具箱，无需 root，安装即用，起步成本最低——本书推荐的主路。
- <strong>远程方案</strong>：手机只当屏幕和键盘，真正的 Linux 跑在云服务器或家里那台电脑上，SSH 连过去用。最稳、性能最好，但要联网、要有一台现成的机器（云服务器通常要花钱租）。
- <strong>模拟与发行版方案</strong>：Termux 里装 proot-distro 进 Debian、Ubuntu 这类完整发行版，或者用其他无需 root 的桌面 Linux 模拟应用——能玩得更"全"，但性能和兼容性都有折损。
- <strong>网页版练习场</strong>：一些网站提供浏览器里的 Linux 终端，适合尝鲜，不适合存东西。

判断标准很简单：想学命令行、写脚本，从 Termux 开始；想跑重活，远程到真机器；只是好奇看看，网页版就行。别一上来就追求"最完整的方案"，工具是拿来干活的，不是拿来供着的。

#### 安装之前：认清官方渠道，别在第一步就翻车

错误示范先来一遍：随手打开某个第三方应用商店，搜"Termux"，点第一个结果装完，发现是几年前的旧版本，软件源怎么都配不上；更倒霉的会遇到被二次打包过的安装包，装完多出来几个来路不明的东西。装 Termux 这一步，翻车的人比用的时候翻车的还多。

靠谱的渠道只有两个，都来自官方：

- <strong>F-Droid</strong>：一个专注于开源应用的独立应用商店，Termux 官方推荐的安装渠道之一，主应用和全套插件都能在里面找到。
- <strong>GitHub Releases</strong>：项目仓库 termux/termux-app 的发布页，直接下载 APK，版本最新最全，不依赖任何商店。

两个渠道装出来的应用签名不一样，只能选一个用到底，不能混着升级——这事在"插件生态系统"一节还有重要提示，先记住一句话：主应用和插件，必须同源。

下载的文件怎么挑？GitHub Releases 页面里的 APK 通常按 CPU 架构分了几个，看不懂就选文件名带 universal 字样的（兼容所有架构）；F-Droid 则会自动匹配你的手机，不用操心。另外核对包名：com.termux，凡是多了后缀、号称"高级版""汉化版"的，一律不要。场景还原一下：帮学弟装机那次，他从某下载站下了个"Termux Pro 中文版"，装上连软件源都是空的——世上没有这个东西，卸掉走官方渠道，五分钟就绪。

再给一个长期有用的习惯：Termux 的官方 wiki 和 GitHub 仓库是最权威的信息来源，遇到对不上的教程，先看它的日期和它假设的环境——安卓版本、Termux 版本，全都在变。教程本身也会过时，官方文档不会。

#### 二、核心功能与特性

##### 完整的Linux环境

Termux<strong>仅内置Bash</strong>这一种Shell。如果想使用Zsh或fish等其他Shell，需要通过包管理器手动安装，例如：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install zsh</code>或<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install fish</code>。同时Termux支持Vim、Nano、Emacs等编辑器，提供接近原生的命令行体验。用户可以通过"pkg install"安装2000+软件包，包括GCC、OpenSSH、SQLMap等开发和安全工具。

内置只有 bash，好处是干净——你学到的是原汁原味的 shell，不会被花哨配置带偏。等用顺了再考虑换：装完 zsh 后用 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chsh -s zsh</code> 把默认 shell 换掉，重开 Termux 生效。编辑器三选一的话：nano 最容易上手（底部常驻快捷键提示），vim 学习曲线陡但功能强，micro 手感接近现代编辑器。拿不准就先 nano，够用很久。

两千多个软件包是什么概念？从编译器到数据库（SQLite），从下载工具到网络扫描（Nmap），常见的命令行工具基本都能搜到。装之前搜一下：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg search 关键词</code>，两秒钟就知道有没有。

##### 强大的包管理

使用APT包管理器（类似Debian和Ubuntu），可安装数千种Linux软件包，涵盖开发工具、网络工具等。支持Python、Ruby、Node.js、Go、Rust、Swift等多种编程语言环境。

装完先<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code>更新软件源与基础包，再往里装工具。之后遇到「command not found」别慌——多半不是系统不支持，是没装对应的包，<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install</code>一下就好。

pkg 和 apt 的关系顺便说清：pkg 其实是 apt 的"友好外壳"，底层还是 apt 在干活，pkg 只是把常用命令封装得更短、提示更贴心。所以网上教程里写 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">apt install xxx</code> 的，你换成 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install xxx</code> 通常一样能跑。语言运行时那串名单值得再看一遍：Python、Ruby、Node.js、Go、Rust、Swift 都能装——意思是这台手机上你可以直接开始学任何一门主流语言，不用等配电脑。

和电脑 Linux 一个常见的习惯差异：Termux 没有 sudo。这不是缺陷——沙盒里你就是最高权限，装东西不需要管理员，也没有管理员可当。教程里出现 sudo 的，把 sudo 删掉直接跑后面的命令就行。

##### 安全与网络功能

- <strong>SSH远程连接</strong>：支持SSH客户端和服务器功能，可远程连接其他设备或让手机成为SSH主机。装上openssh后用<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">sshd</code>启动，默认监听8022端口，从别的设备连时要带上<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-p 8022</code>。
- <strong>加密工具</strong>：提供OpenSSL等加密工具，支持数据加密和安全通信。
- <strong>服务器搭建</strong>：可配置Nginx或Apache搭建静态网页服务器。

每条展开一句。SSH 是最实用的一个，后面专门有一整节讲，手机和电脑互相使唤全靠它。OpenSSL 除了给网站做加密通信，日常也有妙用：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">openssl rand -base64 16</code> 能生成一串随机字符，拿来当临时密码顺手得很。Nginx 搭静态页在 Termux 里也现实——装好后通常默认监听 8080 端口（以官方包内配置为准），手机浏览器访问 http://127.0.0.1:8080 能看到欢迎页，本地调试网页很方便。

##### 系统集成与扩展

- 访问手机存储权限，实现本地文件管理。
- 通过Termux:API插件调用传感器、摄像头等Android硬件功能。
- 支持蓝牙键盘和外部显示器连接，具有完整的鼠标支持。

Termux:API 单独点名：装上插件应用后，再在终端里执行 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install termux-api</code>，就多出一批 termux- 开头的命令，比如 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-battery-status</code> 看电池状态、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-clipboard-set</code> 往剪贴板写内容、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-notification</code> 发系统通知、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-tts-speak</code> 让手机把文字念出来。命令行和手机硬件打通之后，可玩性一下子就上来了——完整的插件清单看下一节。

##### 性能的现实：手机芯片其实不弱

"手机跑 Linux，能行吗？"这是被问得最多的问题。事实是：这几年主流手机的芯片算力不输老款笔记本电脑，跑 Python 脚本、编译中小型 C 项目、跑数据库，都不在话下。真正拖后腿的是另外两件事：散热（长时间满负荷会降频）和存储速度（编译大项目时明显感觉慢）。所以合理的预期是：单次十几分钟的活，手机干得又快又好；一小时的编译大活，交给电脑。

另一个反直觉的点：Termux 装着不用的时候，它只是个安安静静躺在沙盒里的应用，不偷跑流量、不占后台——拖慢手机的从来不是 Termux 本身，而是你在里面跑的任务。任务跑完了，它就闲下来了。

#### 三、插件生态系统

Termux的核心应用程序可以通过几个可选的插件应用进行扩展，提供额外的功能和集成：

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
  <thead>
    <tr class="bg-light dark:bg-gray-700">
      <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">插件名称</th>
      <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">功能描述</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:API</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">向命令行程序公开Android API功能</td>
    </tr>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Boot</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">允许在设备启动时运行脚本</td>
    </tr>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Float</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">提供浮动终端窗口</td>
    </tr>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Styling</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">为终端启用颜色方案和字体自定义</td>
    </tr>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Tasker</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">将Termux脚本与Tasker自动化应用集成</td>
    </tr>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Widget</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">允许从主屏幕小部件运行脚本</td>
    </tr>
  </tbody>
</table>
```

表格之外，把几个插件的用法翻译成场景。Termux:Boot：把脚本放进家目录的 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">.termux/boot/</code> 文件夹，手机重启后自动执行——比如开机就把 sshd 拉起来，电脑随时能连。Termux:Widget：把常用脚本放进家目录的 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">.shortcuts/</code> 文件夹，然后在桌面长按添加 Termux 小部件，脚本就变成一个桌面按钮，点一下直接跑，不用打开终端敲命令——这是把 Termux 用出"工具箱"感觉的关键一步。Termux:Float 让终端变成悬浮窗，边查资料边敲命令；Termux:Styling 换字体和配色；Termux:Tasker 把脚本接进 Tasker 的自动化流程，比如连上家里 Wi-Fi 就自动备份照片。

插件不用一次装齐。我的建议是按需来：先把主应用用熟，哪天发现自己在重复某个动作（比如每次开机都要手敲几条命令），再去装对应的插件。装的时候记住同源原则，主应用从哪下的，插件就从哪下。

安装插件和安装主应用一个规矩：从同一个渠道装。F-Droid 装的主应用就配 F-Droid 的插件，GitHub 装的就配 GitHub 的。下面这条官方提示值得抄进备忘录：

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>重要提示

{class="mt-1"}
Termux及其插件必须从同一来源安装，因为它们共享相同的sharedUserId。混合来自不同来源（如F-Droid和GitHub）的安装将导致安装错误。
:::

万一混装了会怎样？现象通常是安装时提示"应用未安装"或签名冲突。解法也不复杂：把 Termux 全家（主应用加所有插件）卸干净，从同一个来源重新安装。注意卸载会清空家目录，重要脚本和配置先备份——复制到 ~/storage/downloads，或者推到自己的 Git 仓库，后者更稳。

#### 四、安装与配置指南

##### 安装步骤

1. <strong>下载应用</strong>：从项目官方渠道（F-Droid或GitHub Releases）下载安装Termux，无需root权限。应用商店里能搜到的Termux多半是好几年前的旧包，别装那个；不同Android版本的兼容包也可能不一样。
2. <strong>初始化系统</strong>：首次启动后等待"Installing bootstrap packages"完成。
3. <strong>获取存储权限</strong>：执行<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-setup-storage</code>获取手机文件系统权限。
4. <strong>更新软件源</strong>：执行<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code>更新软件包列表。

存储权限也可以不给：不执行<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-setup-storage</code>，Termux照样能在自己的家目录里干活，只是读不到相册和下载文件夹。能访问整个共享存储的终端，等于把你手机里的文件交给了你敲的每一条命令——按需授权，用不到就别开。

##### 基础优化

- <strong>换镜像源</strong>：使用<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-change-repo</code>命令通过图形界面更换镜像源（推荐清华大学镜像源）。
- <strong>快捷键设置</strong>：音量减键模拟Ctrl，音量加键模拟Esc，提升输入效率。
- <strong>界面美化</strong>：安装Zsh + Oh My Zsh，配置主题和插件。

上面四步是主干，几个细节展开讲。换镜像源值得单独走一遍：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-change-repo</code> 会弹出一个图形化选择界面，方向键移动、空格选中、回车确认——先选仓库组（保持默认即可），再在镜像列表里选清华大学那一家，确认后它自动改写源配置，回头再跑一遍 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update</code>，下载速度立刻不一样。国内可用的镜像不止一家，中科大等也有 Termux 镜像，以各镜像站官方页面为准。

音量键是手机键盘上"消失的 Ctrl"，常用的几组组合列个表（以官方 wiki 的快捷键说明为准，不同版本可能微调）：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
  <thead>
    <tr class="bg-light dark:bg-gray-700">
      <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">组合</th>
      <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">效果</th>
      <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">什么时候用</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">音量减 + C</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ctrl + C</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">中断卡住的命令</td>
    </tr>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">音量减 + L</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ctrl + L</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">清屏</td>
    </tr>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">音量加 + E</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Esc</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">退出 vim 等需要 Esc 的场景</td>
    </tr>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">音量加 + T</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tab</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">路径与文件名补全</td>
    </tr>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">音量加 + Q</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">显示或隐藏扩展按键行</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">想要常驻的方向键和按键时</td>
    </tr>
  </tbody>
</table>
```
:::

界面美化这条，给个实在建议：先用原版 bash 干两天活，确认自己真的需要那些主题和插件再折腾 Zsh + Oh My Zsh。它的配置脚本要从 GitHub 拉取，国内网络可能要多试几次，主题装多了还会拖慢启动速度。命令行的手感主要来自熟练，不来自花哨的提示符。进阶玩家还可以在家目录的 .termux 文件夹里放一个 termux.properties 配置文件做个性化定制（比如扩展按键行的内容），具体支持哪些选项以官方 wiki 为准。

#### 从 F-Droid 安装的完整步骤

前面是主干步骤，这里给一份更细的"照着点就行"版本，每一步都写清楚屏幕上会出现什么。全程大概十来分钟，一半时间在等下载。

1. 手机浏览器打开 F-Droid 官网 f-droid.org，点页面上的 DOWNLOAD F-DROID 按钮，开始下载 APK 安装包。
2. 下载完成后从通知栏点开文件，系统弹出"出于安全考虑，禁止安装未知来源应用"之类的提示——这不是拒绝你，是让你去开个开关：进设置找到"安装未知应用"（各家叫法略有差异），给刚才用的浏览器或文件管理器打上"允许"，返回重新点安装。
3. F-Droid 装好后首次打开，会自动刷新软件仓库索引，底部进度条走完才能搜索。网络不好就多等等。
4. 顶部搜索框输入 termux。结果里认准两点：开发者是 Termux 官方（页面上标注 termux.dev），包名是 com.termux。点进详情页。
5. 点"安装"开始下载。F-Droid 的服务器在国外，速度看运气；转圈太久就改走 GitHub Releases 渠道，不必硬耗。
6. 安装完成点"打开"，一个黑底白字的窗口出现，光标在 ~ $ 后面闪，窗口里滚动着 Installing bootstrap packages——它在初始化基础系统，等它跑完，别手滑退出去。

帮爸妈或孩子装的额外一句：装之前说清楚"这是个学习工具，里面能执行命令，别把它当玩具乱点插件"，装完把存储权限这步留给你自己操作——授权这件事，最好由理解权限的人来做。

GitHub Releases 的走法：浏览器打开 github.com/termux/termux-app，进 Releases（发布）页面，展开最新版本（写这章时是 v0.118.3，以页面为准）的资产列表，下载 APK 装上，后面的步骤完全一样。两个渠道选哪个都行，选定了就别再换。装完先别急着折腾桌面小部件和美化，把基础跑通再说——顺序错了，翻车了都不知道从哪查起。

验证装好没有：在提示符后面输入 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">echo $HOME</code>，回车看到一个以 /data/data/com.termux/files/home 结尾的路径，说明基础系统就位。这一步通过，就可以继续了。

#### 界面与输入：把手机键盘用顺手

第一次在手机上敲命令的人，几乎都会卡在同一件事上：不是不会命令，是打不出来——竖线找不到、引号打成中文的、光标不知道怎么挪。这一节专门解决"打字"问题，五分钟练熟，后面少摔无数跤。

- <strong>会话抽屉</strong>：从屏幕左边缘向右滑，会弹出一个抽屉，里面有 NEW SESSION（新会话）和 KEYBOARD（调输入法）按钮。开两个会话，一个跑长任务，一个继续敲命令，互不干扰。
- <strong>复制粘贴</strong>：长按屏幕呼出菜单，选中文本、复制、粘贴都在里面。粘贴长路径前，扫一眼开头和结尾——剪贴板里常有你意想不到的东西。
- <strong>扩展按键行</strong>：音量加+Q 呼出（前面表格提过），方向键、Tab、竖线这些常用符号一键直达，比在输入法符号面板里翻层快得多。
- <strong>中文引号陷阱</strong>：代码里的引号必须是英文单引号或双引号。中文输入法的""和''长得像但完全不同，命令会直接报错。敲命令时切到英文模式，这一条能消灭一大半新手报错。

还有个心态问题顺便说：命令行是一门"逐字符"的语言，多一个空格、错一个字母都会失败，而且系统只报错不猜你想干什么。这不是它难，是它诚实。报错时先检查标点是不是中文标点、命令拼没拼对，九成的"玄学问题"都死在这两处。

#### 首次启动后的十分钟：推荐配置清单

装完别乱逛，按这个清单走一遍，十分钟之内你的 Termux 就从"能用"变成"顺手"：

1. 跑 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code>，让所有包到最新（中途问是否继续，回车即可）。
2. 下载慢过的话，跑 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-change-repo</code> 换国内镜像源。
3. 装常用工具：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install nano git openssh python nodejs</code>。
4. 需要读手机文件的话，执行 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-setup-storage</code>（细节看下一节"初始化与存储权限"）。
5. 下拉通知栏，找到 Termux 的那条常驻通知，点开看看里面的按钮——Acquire wakelock（防冻结）和 Exit（退出），认识一下，别误触 Exit。
6. 从屏幕左边缘滑出会话抽屉，开一个新会话再切回来，感受多会话。
7. 把本书这章加个书签，明天接着练。

这份清单刻意没有包含"装 Zsh、换主题、装一堆插件"——那些是锦上添花，锦还没织好呢。先把基础配置跑稳，用上一两周，你自然会知道自己想要什么。

#### 跟着敲：第一个半小时

清单看过，该动手了。下面这组命令按顺序敲，每一步都写明屏幕上会出现什么。半小时敲完，你对"命令行在干活"这件事就有了体感——比读十篇教程都管用。找个安静的晚上，泡杯水，开始。

1. 敲 pwd 回车，看到 /data/data/com.termux/files/home。这是你的当前位置，也是家目录。它回答的是"我在哪"。
2. 敲 ls 回车，可能什么都没有。加个参数：ls -a，多出一堆点开头的名字——Linux 里以点开头的是隐藏文件，多是配置文件。
3. 敲 mkdir practice 建一个练习文件夹，再 cd practice 进去，pwd 确认一下：路径末尾多了 /practice。
4. 敲 echo "hello termux" > note.txt，把一句话写进文件；再 cat note.txt，屏幕上原样打印出来。那个 > 叫"重定向"，把本该显示在屏幕上的内容改写到文件里。
5. 敲 cp note.txt note-bak.txt 复制一份，ls 看看，两个文件都在了。
6. 敲 mv note-bak.txt old.txt，再 ls——mv 不光是搬家，还能改名。
7. 敲 rm note.txt 删除，然后 cat note.txt，系统回你一句 No such file or directory。好好体会一下：没有回收站，删了就是没了。
8. 敲 cd .. 回上一层，再敲 cd 不带参数，直接送回家目录。迷路时这两个用法救命。
9. 敲 clear（或音量减+L）清屏，世界清净，收工。

敲完这一轮，留意两件小事。一是提示符左侧的路径跟着 cd 在变——看得懂它，你就永远不会迷路。二是报错要原样读一遍：Linux 的报错出奇地诚实，错的到底是文件名还是路径还是权限，它都说得清清楚楚，可惜多数人扫一眼就慌着去搜"怎么办"。

还有个心态问题顺便解决掉：沙盒里随便折腾，最坏的结果就是卸载重装——这恰恰是 Termux 最适合新手的地方。在电脑上你怕弄坏系统不敢敲，在这里你完全不用怕。练手的胆子，就是这么一点点攒起来的。

#### 三个概念：家目录、$PREFIX 与软件源

用 Termux 绕不开三个概念。懂了它们，网上的教程你基本都能对号入座，不用再一条条来问。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
  <thead>
    <tr class="bg-light dark:bg-gray-700">
      <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">概念</th>
      <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">是什么</th>
      <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">打个比方</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">家目录（~）</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">你自己的地盘，脚本、文档、下载的东西都在这</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">你的卧室</td>
    </tr>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">$PREFIX</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">整套软件系统的根，装进来的程序全在它下面</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">整栋楼的公共设施层</td>
    </tr>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">软件源</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">pkg 下载软件的仓库地址清单</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">小区门口的进货渠道</td>
    </tr>
  </tbody>
</table>
```
:::

家目录看一眼就知道：echo $HOME 输出的全路径就是它。养成习惯，自己的东西都在家目录里分文件夹归档，别到处散落——后面做备份时你会感谢这个习惯。$PREFIX 用 echo $PREFIX 查看，教程里出现 $PREFIX/etc/... 这种路径时，你就能自己找到对应文件。软件源的地址写在 $PREFIX 下的 sources.list 这类配置文件里，termux-change-repo 做的事就是把清单指向的仓库换成更快的镜像；哪天 pkg 报 404，先想想是不是"货架清单"该刷新了。

三个概念串起来，分寸感就有了：家目录是你的地盘，随便折腾；$PREFIX 是系统的地盘，交给包管理器打理，别手痒去改里面的东西；软件源出了问题就换镜像，别手抄网上来路不明的"源地址"。三句话，能避开新手期九成的坑。

#### proot-distro：想玩完整发行版的话

Termux 自带的工具箱用熟之后，你会撞到一类教程：命令只认 Debian 或 Ubuntu。别急着找电脑，proot-distro 能在 Termux 里装一个完整的发行版出来玩：

1. pkg install proot-distro，装上这个管理工具。
2. proot-distro list，看看有哪些可装的发行版，Debian、Ubuntu 等都在列（以命令输出为准）。
3. proot-distro install debian，开始下载安装，包体不小，等进度条跑完。
4. proot-distro login debian，提示符一变，你就站在一套相对完整的 Debian 环境里了，apt update、apt install 随便折腾。
5. 玩完敲 exit 退出，回到 Termux 本体。不想要了也可以按 help 里的说明删除重来。

它和 Termux 本体的关系要摆正：发行版环境是"寄居"在 Termux 里的，文件互通的程度以官方文档为准，进去前先看一眼说明。性能有折损，图形界面得另配 VNC 才能看到——这两条预期先放好，免得进去后觉得"也就这样"。

什么时候值得装？教程命令只在完整发行版里能跑、或者你想体验原汁原味的发行版环境时。什么时候不值得？日常学命令行——Termux 本体完全够用，多一层封装就多一层要折腾的东西。工具是拿来干活的，别为了"显得专业"给自己加戏。

#### 下一步学什么：一张路线图

这一章的技能往后延，有四样东西值得排进计划。每样都给一句"学了能干嘛"，你自己决定顺序：

- <strong>管道与重定向</strong>：把一串小命令串成流水线，比如"列出文件、筛选、排序、分页看"。这是命令行效率的分水岭，学完你会开始享受干活。
- <strong>正则表达式</strong>：文本搜索的"通配符升级版"，配 grep 用威力翻倍，处理日志、批量改名都是它的高光场。
- <strong>vim 基础</strong>：命令行编辑器的天花板。先用 nano 顶着，有空再啃——啃下来之后远程改配置不用再求人。
- <strong>SSH 深入</strong>：端口转发、密钥管理这些进阶用法，是运维日常的一半工作。

顺序建议：先管道重定向，再正则，再 vim，最后 SSH 深入。前两样立刻提高日常效率，后两样属于厚积薄发。学习材料认准 Termux 官方 wiki 和各工具自己的文档，别买"三天速成"的秘籍。卡住了就睡一觉再来——很多时候卡住不是因为难，是因为困了。

#### 网络诊断入门：先弄清问题出在哪一环

手机上某个网站打不开，原因可能藏在任何一环：手机配置、Wi-Fi、运营商、目标服务器。干着急或者反复刷新都没有用，命令行给你的是一套"逐环检查"的工具，几分钟就能把模糊的"打不开"变成具体的"哪一环出了问题"。

- <strong>ping：测连通</strong>。ping -c 4 baidu.com 发四个探测包，看有没有回应（参数以 Termux 里的 help 输出为准）。四个都通，说明路是好的；一个都不通，先查自己是不是断网了。
- <strong>curl -I 网址</strong>：只取响应头、不取内容，看状态码。2xx 正常，3xx 是跳转，4xx 多半是你这边请求的问题，5xx 是对方服务器的问题。
- <strong>termux-info</strong>：官方自带的体检命令，输出 Termux 版本和环境信息。到社区求助时把它贴上，比口述环境准确得多。

排查口诀记一句：先自己后别人，先本地后远程，先网络后软件。把问题定位到"某一环"，求助时才能一句话说清楚——"我 ping 什么地址都不通"和"就一个网站打不开"，是两种完全不同的求助，得到的答案也完全不同。

场景走一遍：宿舍楼里 Wi-Fi 一切正常，某个网站就是打不开。ping 那个网站通，curl -I 返回 5xx——服务器自己出了状况，你这边无解。学会诊断最大的好处，不是修好一切，而是立刻知道"这事不归我管"，然后把时间还给该干的事。

再往深一层说，这几条命令本身就是学习素材：ping 让你理解"数据包"，curl 让你看到"响应头"和"网页内容"的分离——都是计算机网络课的第一章。工具用着用着，知识就顺着长出来了。

#### ls 与 grep 的"再看一眼"：两个最值得深挖的命令

所有命令里，这两个出场率最高，值得多花十分钟把常用参数过一遍。不用背，先混个脸熟，用的时候自然会想起来。

- ls -lh：文件大小用人类友好的单位显示，K 和 M 一目了然，找大文件必备。
- ls -t：按修改时间排序，最新的排最前——找"我刚下载的那个文件"的神器。
- ls -r：反向排序，和 -t 组合就是"最旧的在前"。
- grep -i：忽略大小写搜索，error、Error、ERROR 一网打尽。
- grep -n：输出带行号，日志定位到"第几行"全靠它。
- grep -r：递归搜整个文件夹，"这段文字在哪个文件里"一秒出答案。
- grep -v：反向筛选，把不要的行排除掉，配管道用特别清爽。

举个组合的例子：ls -lh | grep 下载，能在满屏文件里筛出名字带"下载"的条目。管道把两个命令接起来，前一个的输出是后一个的输入——这条思路一旦通了，你就正式入门了。

练法建议：今天的任务是什么，就学今天用得上的那一两个参数，别贪多。一周之后回头看，常用的参数已经长在手指上了，比背参数表快得多，也牢得多。

卡住了就敲 命令 --help 看自带说明，或者 pkg show 包名 看介绍。帮助系统是命令行世界的说明书，养成先查 help 的习惯，以后遇到任何新命令都不会怵。

#### 案例实录：每周自动备份相册精选

把这一章学的东西串起来做一个真东西：每周把相册里的照片文件夹备份到下载目录。别小看它——路径、脚本、权限、通知，全在里面了。脚本语法后面"脚本入门"一节会细讲，这里先照抄。

1. cd ~/storage/dcim，用 ls 看清楚相册的目录结构，想明白要备份哪一层。
2. nano photobackup.sh 写脚本：开头 echo 报告开始；中间用 cp -r 把选定的文件夹复制到 ~/storage/downloads/ 下一个带日期后缀的新文件夹（日期用 date 命令生成）；结尾 termux-notification 弹一条"备份完成"。
3. termux-fix-shebang photobackup.sh 修一下解释器声明，再 chmod +x photobackup.sh 给它执行权限。
4. 手动 ./photobackup.sh 跑一遍，然后去下载目录打开备份文件夹，抽查几张照片能不能正常打开——没核对过的备份，等于没有备份。
5. 跑通之后，把脚本复制进 .shortcuts/ 文件夹，配 Termux:Widget 做成桌面按钮。
6. 每周日点一下按钮，看到"备份完成"的通知，收工。

全程没有一条"高深"命令，但它解决的是一个真实问题。所谓"会用 Termux"，指的就是这种状态：需求冒出来的时候，你脑子里能浮现出"用哪几个命令、怎么串起来"，而不是手足无措。

它还有一串扩展方向：想自动跑，研究循环加 sleep 的写法；想备份到电脑，加上 scp 传出去；想省空间，研究 tar 打包压缩。每加一层需求就多学一点东西，需求驱动的学习，永远比按手册目录啃快得多。

丑话说在前面：备份脚本第一次跑，最容易暴露的就是"目标文件夹写错"这类低级问题。所以先在练习目录里试，确认无误再指向 ~/storage。谨慎不是胆小，是流程的一部分。

#### 再答几个常见问题

<strong>问：装了 Termux 之后电池掉得快，是不是它在偷偷跑什么？</strong>答：先看通知栏有没有活着的会话和 wakelock，跑完任务记得 termux-wake-unlock。没有任务还掉电快，去系统的电池页面看耗电排行，用数据说话，别凭感觉冤枉它。

<strong>问：想给不同项目用不同的环境，有办法吗？</strong>答：Python 项目用 venv，Node 项目靠各自目录里的 package.json，脚本按项目分文件夹放。Termux 没有重量级的"多环境管理"工具，目录纪律就够用了。

<strong>问：能不能在电脑的大键盘上操作手机里的 Termux？</strong>答：能，电脑 ssh 进手机就是最直接的方式，本章 SSH 一节讲过完整步骤。输入体验立刻从"戳屏幕"升级成"打键盘"，写长脚本尤其舒服。

<strong>问：学了一半忘了怎么办？</strong>答：正常。命令行知识是肌肉记忆型的，忘了再敲一遍就回来。把练习清单留在手机里，每周摸一次，比一次性学完更牢。忘了不可怕，不摸才可怕。

<strong>问：想给终端换个"皮肤"，从哪儿下手？</strong>答：Termux:Styling 插件可以换字体和配色（记得同源原则，主应用从哪下的插件就从哪下）。我的建议还是那句：花哨不如顺手，先用原版攒手感，真需要再换。

<strong>问：卸载 Termux 会不会把我备份到下载目录的文件也删掉？</strong>答：不会。~/storage/downloads 在手机的共享存储里，卸载只清空 Termux 自己的沙盒。这正是备份要放到共享存储或云端的原因——沙盒里的东西，只在沙盒活着的时候存在。

#### find 速成：文件多了之后的必备技能

文件少的时候 ls 够用，文件多了就需要按条件找。find 就是干这个的：告诉它从哪儿找、找什么，它把所有匹配的路径列给你。语法拆开看很好懂：find 路径 条件。

- find . -name "*.jpg"：在当前目录（含子目录）找所有 jpg 图片，引号别丢。
- find ~/storage/downloads -size +10M：找下载目录里大于 10M 的文件，清理空间时首选。
- find . -mtime -7：找最近七天改过的文件，"我这周到底改了啥"一问便知。
- find . -type d：只列文件夹，想理清目录结构时用。
- find 和管道结合：find . -name "*.log" | wc -l 统计日志文件个数，管道的又一种用法。

重点讲一个安全习惯：find 可以直接执行删除（具体参数以 --help 输出为准），但新手的规矩是先只"找"不"删"——用默认的列出模式确认结果无误，再动手下一步。删除永远走两步：先看见，再下手。跳过第一步的人，都会在某一天为此补学费。

练习任务给你安排好：在练习文件夹里建几个不同类型、不同大小的文件，然后用上面五条命令各跑一遍，看看输出和你的预期差在哪。跑完这一轮，find 就从"听说过的命令"变成"会用的工具"了。

#### 管道、重定向与流：串起命令的胶水

前面几次实战里你见过 | 和 > 了，现在把它们讲透。命令行世界有个核心设计：每个命令只做一件小事，然后把"做出来的结果"交给下一个命令。连接它们的就是管道 | 和重定向 >、>>。

- 命令 > 文件：把输出写进文件（覆盖原有内容），比如 ls > list.txt。
- 命令 >> 文件：把输出追加到文件末尾，日记类工具全靠它。
- 命令A | 命令B：A 的输出直接喂给 B 当输入，比如 ls -lh | less 分页查看。
- 命令A | 命令B | 命令C：管道可以一直串下去，每一节做一道工序，像流水线。

一个日常例子：想统计下载目录里 PDF 有多少个，一条命令搞定——find . -name "*.pdf" | wc -l。find 负责"列出来"，wc -l 负责"数行数"，两个小命令联手，完成一个看起来需要写程序的任务。

重定向还有个经典用法是"留证据"：跑一个输出很长的命令，先 命令 > result.txt 存下来，再用 less 慢慢看。屏幕是流水，文件是存款——重要的输出都值得落成文件。

练习安排：在练习目录里造十几个不同名字的文件，然后用管道完成三个任务——按名字筛选、按大小排序（配合前面学过的 ls 参数）、统计总数。三个任务跑通，你就掌握了命令行一半的威力，另一半在脚本里。

#### 跑长任务前后的两张检查单

手机上跑任务，怕的不是失败，是"跑到一半没人管"。给自己立两张检查单，各五条，每次跑长任务过一遍：

<strong>开始前</strong>：确认在正确的目录（pwd 看一眼）；确认磁盘空间够（df -h）；确认任务会动到的路径没有拼错；执行 termux-wake-lock 防冻结；手机插上电。五条过完，再回车。

<strong>结束后</strong>：核对输出文件确实生成、大小正常；抽查内容对不对（别只看文件名）；跑 termux-wake-unlock 释放；清掉任务产生的临时文件；顺手 git commit 把脚本改动记下来。五条过完，才算收工。

这两张单子看着繁琐，实际各花一分钟。它们的价值在于把"忘了"变成"流程"——长任务出事故，九成不是命令错了，而是"忘了它在跑""忘了核对""忘了释放"。流程化是命令行世界里最便宜的保险。

#### 初始化与存储权限

bootstrap 跑完，Termux 只是"能用"，还没"通"到手机——默认情况下它读不到你的相册和下载文件夹。这一节把初始化的几件事一次说清。

##### bootstrap 是什么

一套最小化的 Linux 基础系统：bash、常用小工具和 apt 包管理器。它只在首次启动时安装一次，之后每次打开 Termux 都是现成的。如果初始化失败——提示符一直不出来，或者反复报错——先检查两件事：手机剩余存储空间够不够、网络通不通。还不行就长按 Termux 图标进应用信息，强制停止后重开。个别情况确实要重装才能解决，那也记得按同一来源原则来。

##### termux-setup-storage：把存储交出来

在提示符后输入 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-setup-storage</code> 回车，系统会弹出存储权限授权窗口（安卓 11 及以上通常是"允许访问所有文件"的开关页，视机型与系统版本而定）。允许之后，Termux 会在家目录生成一个 storage 文件夹，里面是一串软链接：shared 指向手机共享存储的根目录，downloads、dcim、pictures 等分别对应下载、相册、图片这些常见位置。

验证一下：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls ~/storage/downloads</code>，能看到你平时下载的文件，就通了。以后脚本要处理手机里的文件，都从 ~/storage 下面找路径。

想撤销也简单：删掉 ~/storage 目录再重新执行一次命令即可。顺带把丑话说在前面——rm 这类命令没有回收站，敲回车前多看一眼路径。

##### 要不要给，想清楚再点

存储权限等于把整个共享存储交给你敲的每一条命令：一条写错的 rm 能删掉相册里的东西，一个来路不明的脚本能把你的文件传去别处。原章节那句"按需授权，用不到就别开"就是针对这事：暂时只练命令，就先不给；哪天要处理手机文件了，执行这条命令只要一分钟。

#### 包管理与常用命令：上手第一课

凌晨一点的宿舍，你想解压一个压缩包，Termux 回你一句 command not found——别慌，多半不是不支持，是没装对应的包，<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install unzip</code> 一下就好。这一节把最常用的命令列成速查表，用得上就翻回来。

##### pkg 家族速查

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
  <thead>
    <tr class="bg-light dark:bg-gray-700">
      <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">命令</th>
      <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">干什么</th>
      <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">什么时候用</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">pkg update</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">刷新软件源列表</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">装东西之前先跑</td>
    </tr>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">pkg upgrade</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">升级已安装的包</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每隔一阵跑一次</td>
    </tr>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">pkg search 关键词</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">搜索软件包</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不确定包名时</td>
    </tr>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">pkg show 包名</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">看包的详细信息</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">装之前确认</td>
    </tr>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">pkg install 包名</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">安装</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">主力命令</td>
    </tr>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">pkg uninstall 包名</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">卸载</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不用了就清掉</td>
    </tr>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">pkg list-installed</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">列出已安装的包</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">清点家底</td>
    </tr>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">pkg reinstall 包名</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">重装</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">配置改坏了救场</td>
    </tr>
  </tbody>
</table>
```
:::

update 和 upgrade 的区别最容易混：update 只刷新"货架目录"，告诉系统仓库里现在有什么；upgrade 才真正把已装的包升到新版本。所以标准姿势是 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code> 两连，先看清单再升级。

##### 基础文件命令速查

装完工具，日常和文件打交道的高频命令：pwd 看当前路径，ls 列目录（加 -l 能看权限，后面练习会用到），cd 换目录，mkdir 建文件夹，touch 建空文件，cp 复制，mv 移动或改名，rm 删除，cat 看小文件，less 翻大文件，grep 在文本里搜关键词，df -h 看磁盘空间。这些在"学习Linux操作"一节都有练习安排，先混个脸熟。

三条最常用的连招，可以直接抄：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code>（新装完先来一遍）；<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install nano git openssh python nodejs</code>（常用工具一次装齐）；搜索不到想要的命令时，用搜索引擎搜"Termux 加命令名"，以官方 wiki 为准。

##### rm 的两条保命习惯

Linux 的 rm 没有回收站，删了就是删了。两条习惯能救你很多次：删除前先 ls 一眼，确认路径和文件名都在；批量删除用 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">rm -r</code> 而不是 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">rm -rf</code> 起手——f 会压掉所有提示，等你发现删错往往已经晚了。另外路径勤用 Tab 补全，别手打：手打的 /storge 和 /storage 差一个字母，结果天差地别。

##### 报错对照：见招拆招

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
  <thead>
    <tr class="bg-light dark:bg-gray-700">
      <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">看到的报错</th>
      <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">多半的原因</th>
      <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">怎么办</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">command not found</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">包没装，或命令拼错</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">pkg search 后安装；检查拼写</td>
    </tr>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Permission denied</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">权限不够</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">想想是不是在动沙盒外的东西；Termux 没有 sudo</td>
    </tr>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Failed to fetch / 404</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">源数据过期或网络问题</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">先 pkg update；不行就 termux-change-repo 换镜像</td>
    </tr>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">No space left on device</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">空间满了</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">卸载不用的包，检查手机剩余空间</td>
    </tr>
  </tbody>
</table>
```
:::

三个提升手感的细节：Tab 补全（打一半按 Tab 自动补完）、方向键上（翻出上一条命令改改接着用）、Ctrl+C（音量减+C 中断卡死的命令）。就这三招，能让你少输一半的字。

#### SSH 远程连接：让电脑和手机互相使唤

装上 openssh 之后，手机有两个身份可选：当客户端去连别的机器，或当服务端让别人连进来。两个方向都讲，都很实用。

##### 手机当客户端：远程管理服务器

装包：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install openssh</code>。连接：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ssh 用户名@服务器地址</code>，第一次连会问你是否信任对方指纹，核对后输 yes；以后每次连接都用这把"指纹"校验，哪天突然提示指纹变了，先警惕是不是连错了机器或被劫持，别急着 yes。

每次输密码很烦，配免密：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ssh-keygen -t ed25519</code> 一路回车生成密钥对，然后 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ssh-copy-id 用户名@服务器地址</code> 把公钥送过去，之后连接不再要密码。服务器多的话，在家目录的 .ssh/config 文件里给每台机器起别名（Host、HostName、Port、User 四行一组），以后 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ssh 别名</code> 直达。

错误示范给一个：图省事把私钥文件发到微信群"自己备份用"——私钥就像你家钥匙的模具，发给谁谁就能进你家门。私钥永远只待在生成它的设备里，备份进密码管理器或加密存储，绝不进聊天软件和网盘。

##### 端口转发：顺手就能用的进阶招

SSH 还有个不张扬的本事叫端口转发：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ssh -L 8000:localhost:80 用户名@服务器地址</code> 连上去之后，你在手机浏览器开 http://127.0.0.1:8000，看到的其实是服务器上那个 80 端口的网页——流量全程走加密隧道。用处很实在：公司内网的管理后台、服务器上没对外开的服务，都能这样"拉"到手机上看。玩熟了这一招，你会觉得很多付费的"远程访问工具"没什么魔法。

##### 手机当服务端：从电脑连进手机

这招在"手机和电脑配合"时特别好用。五步走：

1. Termux 里执行 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">passwd</code> 给自己设个密码（输入时屏幕不显示，正常，输完回车）。
2. 执行 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">whoami</code> 查用户名，是 u0_a 开头的一串。
3. 查手机的局域网 IP：ifconfig 或 ip addr（不同版本预装的命令略有差异，缺什么装什么），找 wlan0 里的地址，形如 192.168.x.x。
4. 执行 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">sshd</code> 启动服务，它默认监听 8022 端口——注意不是 22。
5. 电脑上执行 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ssh -p 8022 u0_axxxx@192.168.1.8</code>（用户名和 IP 换成你查到的），输刚才设的密码，就连进手机了。

传文件用 SFTP：电脑上用 WinSCP、FileZilla 这类工具，协议选 SFTP、端口 8022，就能像网盘一样在电脑上拖拽手机家目录里的文件。命令行党用 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">sftp -P 8022</code> 同样可以。免密登录给手机也成立：把电脑的公钥追加进手机的 authorized_keys 文件，或直接在电脑上执行 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ssh-copy-id -p 8022 用户名@手机IP</code>。

##### 常见坑

- 连不上先三连问：手机和电脑在同一 Wi-Fi 吗？IP 对吗（路由器可能重新分配了地址）？sshd 起了吗？
- 连接突然超时：八成是系统把后台的 sshd 冻结了，重新打开 Termux，或按后面"后台保活与电池的现实"一节处理。
- 公网直连别玩：想让外网直接连进家里的手机，需要路由器端口映射等一堆配置，风险也大，新手不建议。

#### Python、Node.js、Git：先把三大件装上

一条命令装齐：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install python nodejs git</code>。三样各管一摊：Python 管脚本和数据处理，Node.js 管网页和小工具，Git 管代码版本。装完各自验证：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python --version</code>、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">node --version</code>、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git --version</code>，都能报出版号就齐了。

##### Python：从一句 print 到一个小脚本

先跑交互环境：直接输 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python</code>，看到 &gt;&gt;&gt; 提示符就进去了，敲一句 print("hello") 回车看结果，<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">exit()</code> 退出。写正经脚本：nano hello.py 写几行，保存退出，<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python hello.py</code> 运行。

装第三方库用 pip，但有个讲究：优先给每个项目建独立的虚拟环境——<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python -m venv venv</code> 创建，<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">source venv/bin/activate</code> 激活（提示符前面会多出 venv 标记），之后再 pip install。全都往系统环境里装，迟早把依赖搅成一锅粥，这在哪台 Linux 上都一样。

pip 装包偶尔也会失败，多半是两种情况：一是带编译步骤的库在手机上缺编译工具，报错信息里通常写得明白，照着装缺的东西（比如编译器）就行；二是网络问题，多试一次或换个时段。实在装不上的库，先查查有没有纯 Python 的替代品——这条路在手机上往往比电脑上更管用。

场景：地铁通勤的四十分钟，够你写完一个处理 CSV 的小脚本再加半轮调试——手机上写、手机上跑，到公司把代码 push 上去接着用电脑改。

##### Node.js：跑个小工具

装完自带 npm。新建目录进去执行 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">npm init -y</code> 生成 package.json，写个 app.js，<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">node app.js</code> 跑起来。npm 装包慢可以换国内镜像源（用 npm config 命令设置 registry，具体地址以 npmmirror 等镜像站官方说明为准），别从论坛里抄来路不明的源地址。

##### Git：把每一天的练习都记下来

先报户口：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git config --global user.name "你的名字"</code> 和 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git config --global user.email "邮箱"</code>。然后 clone 一个练习仓库，每天改完 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git add .</code>、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git commit -m "day 1"</code>，一个月回头看你写了多少东西，成就感实打实。HTTPS 方式克隆对新手最省事；想用 SSH 连 GitHub，就把前面 SSH 一节生成的公钥添加到 GitHub 账户里。GitHub 在国内访问时快时慢，多试几次或换个网络时段，别轻信网上来路不明的"加速"工具。

#### 和桌面开发的配合

场景：在公司电脑写了一半的脚本，下班地铁上想接着改。四条路，按推荐程度排：

- <strong>Git 中转</strong>：电脑 push 到远端仓库，手机 pull 下来改，改完再 push 回去。最规范，顺便把 Git 练熟了。
- <strong>SSH 直连</strong>：电脑 ssh 进手机（手机当服务端那套），直接在电脑的大键盘上操作手机里的环境；反过来手机 ssh 进电脑也行，等于把电脑当服务器用。
- <strong>SFTP 拷文件</strong>：就改一个文件？sftp 或 WinSCP 拖过来，改完拖回去。
- <strong>文件同步</strong>：Syncthing 这类同步工具有 Termux 移植版，能把电脑目录和手机家目录保持双向同步。配置有一点门槛，动手前先备份。

走 Git 中转这条路，要立一条纪律：开工前先 pull，收工立刻 commit 加 push。两台设备先后改同一个文件而不及时同步，合并冲突比想象中容易发生——冲突本身不可怕，可怕的是手忙脚乱之下把两边的改动都弄丢。纪律比技巧重要。

编辑器方面：在电脑上通过 SSH/SFTP 直接编辑手机里的文件是可行的；各编辑器对 Termux 这类环境的远程支持程度不一，能不能配、怎么配，以你所用编辑器的官方文档为准，别硬套针对服务器的教程。

输入这关也得过：正经写代码别硬戳软键盘，几十块的蓝牙键盘能让手机秒变"小笔记本"，再接个鼠标（有线 OTG 或蓝牙都行），体验再上一层。原章节提到的外接显示器同理，条件够就试。

分寸感：手机端当轻量执行环境——改脚本、跑小任务、看日志；编译大项目、跑容器这类重活交给电脑。不是手机不行，是不值当：发烫、掉电、随时可能被系统冻结。

#### 定时与自动化：让脚本自己跑

用了一阵子，你会想偷懒："能不能让脚本自己跑，别让我手动敲？"能，但有前提——安卓不给 Termux 常驻后台的待遇，所以自动化方案都是"借力"型的：

- <strong>开机即跑</strong>：装 Termux:Boot，把脚本放进 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">.termux/boot/</code> 文件夹，重启后自动执行。适合每次开机都要做的事，比如拉起 sshd。
- <strong>一键执行</strong>：装 Termux:Widget，脚本放进 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">.shortcuts/</code>，桌面长按加小部件，点一下就跑。备份照片、查快递这类高频动作特别合适。
- <strong>循环轮询</strong>：最朴素的定时——脚本里写个循环，干完活 sleep 一段时间再来一轮。适合对时间不敏感的任务，缺点是必须有个活着的会话。
- <strong>完成提醒</strong>：脚本结尾加一句 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-notification</code>，跑完手机顶栏弹通知。挂后台跑东西时，这一句能救你于"到底跑完没"。
- <strong>Tasker 联动</strong>：装 Termux:Tasker，把脚本接进 Tasker 的触发条件——连上家里 Wi-Fi 就同步照片、晚上十点自动备份，随你编排。

预期要现实：这些自动化都受系统冻结影响，"每五分钟准时执行"这种要求别提，"每天早上大概八点同步一次"这种可以谈。想要工业级的定时调度，还是要回到常供电的电脑上。

#### 备份与迁移：给家目录上份保险

Termux 的家目录不在普通文件区，换机工具、清理软件都碰不到它——好处是安全，坏处是你不备份它，它就真的没了。三层保险，由轻到重：

1. <strong>脚本进 Git</strong>：所有自己写的脚本放一个仓库，推到远端。这是最稳的一层，恢复就是一次 clone。
2. <strong>配置文件单独存</strong>：.bashrc、.ssh/config 这些小文件，复制到 ~/storage/downloads，随手机文件一起被你的常规备份覆盖。
3. <strong>整体打包</strong>：需要整体搬家时，把整个家目录打成一个压缩包放到共享存储再传走，恢复和解包照着官方 wiki 的备份方案来，别自己发明格式。

换新手机的标准流程：新手机从同一来源装 Termux，初始化完成后，把备份的家目录数据放回去。老手机先别急着卸——等新手机跑通一遍再删，是换机的基本礼貌。

#### 五、典型应用场景

##### 移动开发测试

在手机上搭建完整的开发环境，编写并运行Python脚本，使用GCC编译C程序，通过Git管理代码仓库，结合SSH与远程服务器同步。

展开说：Python 脚本处理数据、编译第一个 C 语言 hello world（编译器以官方仓库提供的为准）、git 记录每天的练习——这一套全在手机上走得通。它还是个理想的"试错场"：环境搞坏了，卸载重装十分钟满血复活，比在电脑上乱折腾系统便宜多了。

##### 服务器运维

通过SSH远程管理服务器，执行系统维护、日志分析等任务，随时随地处理服务器问题。

但预期要摆正：安卓对后台应用的管控一代比一代紧，任务跑一半被系统冻结是常事。SSH上去敲几条命令、看看日志没问题；真要挂机跑几个小时的任务，交给电脑或一台常供电的小设备更稳。

常用的小连招：ssh 上去看磁盘 df -h、看内存 free -h、grep 关键字翻日志、必要时重启服务，一两分钟解决战斗。再强调一次：生产密钥别放手机，用完即走的跳板最安全。

##### 学习Linux操作

提供真实的Linux环境，是学习命令行和系统管理的理想平台，可练习Shell脚本编写、Linux文件权限管理（如 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chmod 755</code> 设置 rwxr-xr-x 权限位、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chown user:group</code> 修改文件归属、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls -l</code> 查看 owner/group/other 三组九位权限）等基础命令。注意这是Unix/Linux经典的"三组九位"权限模型（owner / group / other × 读 / 写 / 执行），与Windows NTFS的ACL访问控制列表是完全不同的两套体系。

给一份七天练习清单，一天十几分钟：第一天 ls -l 看权限位；第二天 chmod 改权限看变化；第三天 ps 看进程、kill 结束进程；第四天 df -h 与 du 看磁盘占用；第五天 grep 在日志里找关键词；第六天写个 for 循环批量改文件名；第七天把这六天的操作串成一个 shell 脚本。做完这一轮，命令行就不再是"背命令"，而是"使唤电脑"。

##### 🔐 网络安全测试

安装Nmap、SQLMap、Hydra、Metasploit等安全工具，进行网络扫描和渗透测试。

先把红线说清楚：这些工具只允许用在自己的设备，或拿到明确书面授权的网络。扫描别人的系统不叫学习，叫违法，责任由使用者自己担，法规以你所在地区的现行法律为准。学习姿势示例：nmap 扫自己家的路由器看开了哪些端口、SQLMap 在本地搭的测试环境里练，一步都别越界。

#### 给三类人的使用建议

同一把工具，不同人玩出的花样完全不同。对号入座一下：

- <strong>学生党</strong>：把它当"随身机房"。通勤刷题、睡前写脚本、用 Git 给自己攒作品集——毕业面试时，"我从大三开始每天提交"比任何话都有说服力。
- <strong>运维和后端党</strong>：把它当"应急跳板"。半夜告警不用爬起来开电脑，ssh 上去看日志、重启服务；日常给服务器做巡检的几条命令，做成桌面小部件一键执行。
- <strong>文字工作者</strong>：把它当"文本处理机"。批量给文章重命名、统计字数、把 Markdown 转成需要的格式，脚本一跑全省。写作本身用顺手的 App，处理交给命令行。

至于爸妈：不建议主动推荐。命令行对长辈的学习成本太高，他们的手机需求用常规 App 就能满足。真有长辈感兴趣想学，那另说——好奇心是最好的入学资格。

#### 后台保活与电池的现实

安卓的省电策略是 Termux 长任务的头号敌人。想让任务多活一会儿，三板斧：

1. 会话里执行 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-wake-lock</code>（或点通知栏里的 Acquire wakelock 按钮），告诉系统"别冻我"；干完活用 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-wake-unlock</code> 释放。
2. 去系统设置里给 Termux 关掉电池优化：各家入口不同，华为在"启动管理"、小米在"省电策略"，OPPO、vivo 也有类似开关，名称视机型与系统版本而定，统一设成允许后台运行、不被一键清理。
3. 长任务挂上充电器再跑，顺手把屏幕亮度调到最低。

通知栏里那条常驻的 Termux 通知也留意一下：它带着 Exit 这类按钮，是会话的"总开关"，点 Exit 就是退出，别当成普通通知划着玩。跑任务期间，它一直挂在通知栏是正常现象，不是 bug。

还有个安卓 12 及以上版本的特殊情况：系统会清理所谓的"幽灵进程"，后台命令行子进程更容易被杀，这正是 Termux 在新系统上不够稳定的原因之一。缓解办法官方 wiki 有专门说明，以官方文档为准，别照抄来路不明的 adb 命令。

把预期放平：几分钟到几十分钟的短任务加 wake-lock 基本稳；几小时的任务就要看脸——机型、系统版本、省电策略都在掺和。真有长期挂机的需求，电脑或一台常供电的小设备仍然是对的答案。

#### 六、边界与安全：哪些事别放进Termux做

Termux能干的事很多，但它本质上是一个能跑任意命令的终端环境，有几条边界要自己守住：

- <strong>敏感信息别进去</strong>：生产密钥、支付凭证、真实账号的口令，都不要放进手机终端——屏幕录制、剪贴板、通知预览，任何一个环节都可能把内容带出去。
- <strong>别当服务器用</strong>：手机不是常供电设备，省电策略随时可能冻结你的进程。「口袋里的Linux」适合学命令、写临时脚本、看懂日志，不适合承载长期在线的服务。

两条之外，再补几条具体的。权限边界要心里有数：Termux 的权限就是你的权限，你给了它存储权限，家目录里的任何脚本就都能读你的共享存储。装第三方脚本前问一句——我信得过写它的人吗？curl 一把梭是老坑：网上教程常见"复制这条命令直接跑"的安装方式，等于把你的终端交给对方，脚本里写了什么你根本没看；装东西优先走 pkg，真要用安装脚本，先 cat 出来看一遍再跑。社区里还有额外的第三方软件源，这些包没有官方审核，装之前想清楚出问题自己兜底。

法律这条单独立一块：渗透测试工具只对自有设备或获授权的网络使用，未授权扫描和攻击是违法行为，跟工具本身无关，用的人自己担责。工具无罪不等于使用无罪。

::: div .tip-box .rounded-lg .p-4 .mb-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>一句话记牢

{class="mt-1"}
Termux适合学命令、做临时脚本、看懂日志，不适合当服务器或存secrets。
:::

#### 脚本入门：把重复的事写成文件

用了一两周，你一定发现了几件"每天都重复做"的事：备份某个文件夹、清理下载目录、连上 Wi-Fi 后跑一遍检查。这种事就该写成脚本，让文件替你记，命令替你跑。

一个最小的例子，跟着做一遍：

1. nano myfirst.sh 新建脚本文件，在里面写两行：echo "开始干活" 和 date。
2. 第一行加上声明：#!/data/data/com.termux/files/usr/bin/bash——告诉系统用哪个解释器跑这个文件（也可以写完脚本后用 termux-fix-shebang 命令帮你补上，这是官方提供的工具）。
3. Ctrl+O 保存、Ctrl+X 退出（nano 底部有快捷键提示）。
4. chmod +x myfirst.sh 给它"可执行"的权限——还记得 ls -l 里的 rwx 吗？+x 就是加执行位。
5. ./myfirst.sh 运行。屏幕先打印"开始干活"，再打印当前时间。

恭喜，你已经会写脚本了——剩下的只是往这两行之间加内容：变量存中间结果，for 循环批量处理文件，if 判断条件分支。语法不用背，用到了查，查多了自然会。改完就跑、跑错就改，脚本的好处就是迭代极快。

两个实用的衔接：脚本放进 .shortcuts/ 文件夹配 Termux:Widget，就成了桌面按钮；放进 .termux/boot/ 配 Termux:Boot，就成了开机自启。前面插件一节讲过的东西，到这儿才算真正派上用场。提醒一条：脚本里别放密码和密钥，脚本会被人看到，也会被备份出去——要用的东西用环境变量传，敏感凭证干脆别放手机。

#### 四周学习路线：从会敲到会写

给你一张四周的路线图，每天十五分钟，载体就用你自己的真实需求——练起来才有意思：

- <strong>第一周：文件与目录</strong>。ls、cd、mv、cp、rm、grep、less，练习任务是整理一遍 ~/storage/downloads，按类型分文件夹归档。
- <strong>第二周：权限与进程</strong>。chmod、ls -l 读权限位、ps 看进程、kill 结束进程、df 和 du 看空间。练习任务是给脚本加执行权限、把占空间的目录找出来清理。
- <strong>第三周：网络与远程</strong>。ssh 客户端与服务端、sftp 传文件、ping 测连通。练习任务是从电脑 ssh 进手机传一张图，再反向来一次。
- <strong>第四周：脚本与自动化</strong>。变量、循环、.shortcuts 桌面按钮、开机任务。练习任务是写一个"每周把相册备份到指定文件夹"的脚本，做成桌面按钮。

四周走完回头看：你不是"学会了 Linux"，你是真的用它干了几件活。这个区别很重要——命令行的安全感来自"我改的东西我知道在哪、坏了怎么退"，而这只能靠动手攒。中途哪一周断了，断就断了，从断的那周接着来，别从头开始。

#### 出问题时排查的五步法

用得越多，遇到的问题就越五花八门。与其记报错，不如记一套排查流程，什么问题都能套：

1. <strong>把报错原文读一遍</strong>：不是扫一眼，是读。报错里通常有文件名、行号和原因，九成的问题写在字面上。
2. <strong>查拼写和标点</strong>：命令打错一个字母、用了中文引号或中文空格，都会失败。把命令重新敲一遍而不是凭记忆改。
3. <strong>查环境三件套</strong>：网络通不通（ping 一个网址）、磁盘满没满（df -h）、权限够不够（ls -l 看文件）。很多"玄学问题"其实就死在这。
4. <strong>把命令拆小复现</strong>：一长串命令失败时，拆成单步跑，看死在哪一步——复合命令出错时，罪魁往往只是其中一段。
5. <strong>查官方 wiki 和仓库的 issue 区</strong>：带着报错原文去搜，比在群里干等快得多。搜到答案也留个心眼：看日期、看环境，对不上的老答案别硬套。

最后送一句话：报错不是失败，是信息。命令行世界里，沉默才可怕——它什么都不说的时候，才是真的出了大事。养成跟报错对话的习惯，你会比身边大多数人更早脱离"新手"这个词。

#### 进阶技巧：别名、函数与 .bashrc

敲命令多了，总有几个又长又难记的组合天天用。bash 给你两个偷懒工具：别名和函数，都写在家目录的 .bashrc 文件里，每次打开 Termux 自动生效。这个文件，就是你的"自定义启动清单"。

别名最简单：alias up='pkg update && pkg upgrade'，以后敲两个字母 up 就是完整升级流程；alias ll='ls -l' 是从电脑时代传下来的肌肉记忆；alias gs='git status' 给 Git 用户省掉一半打字。敲 alias 不带参数，能看到当前所有别名。规则很简单：等号两边不能有空格，右边整段用引号包住。

函数更进一步，能带参数。比如定义一个"进目录顺便列内容"的 mycd(){ cd "$1" && ls; }，以后 mycd practice 一步到位，进去的同时看到里面有什么。$1 表示第一个参数，$2 表示第二个——看不懂没关系，先抄能用的，用着用着就懂了。

两条纪律要立好：改 .bashrc 之前，先 cp .bashrc .bashrc.bak 做个备份，改坏了恢复就是一条命令的事；改完执行 source .bashrc 让改动立即生效，或者干脆重开 Termux。如果哪天打开 Termux 就报错，多半是语法改坏了，恢复备份文件即可。

最后一个分寸问题：别抄网上炫技的一大坨配置。每个别名都应该是你真的每周在用的——配置是给自己省事的，不是给自己找事的。抄三条自己真用的，胜过抄三十条别人的。

#### 与电脑 Linux 的差异速查表

网上的 Linux 教程默认你在电脑上，遇到对不上的地方，先查这张表，多数困惑当场解决：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
  <thead>
    <tr class="bg-light dark:bg-gray-700">
      <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">教程里出现的</th>
      <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Termux 的现实</th>
      <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">怎么办</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">sudo 命令</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">没有，也不需要</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">删掉 sudo，直接跑后面的部分</td>
    </tr>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">apt 命令</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">与 pkg 等价</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">当成 pkg 用</td>
    </tr>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">systemctl 管理服务</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">没有 systemd 这一层</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">服务就是普通进程；开机自启用 Termux:Boot</td>
    </tr>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">图形界面操作</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">默认纯命令行</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真需要就另配 VNC，以官方文档为准</td>
    </tr>
    <tr>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">/etc、/usr 等系统路径</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">都对应到沙盒的 $PREFIX 下</td>
      <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把教程路径里的系统目录换到 $PREFIX 下对号入座</td>
    </tr>
  </tbody>
</table>
```
:::

记住一句话：差异多在环境，不在知识。命令的语法、参数、管道这些知识，在哪台 Linux 上都一样；Termux 特有的只是"它怎么被安进手机"。所以你在这台手机上学的每一样东西，到了电脑上直接就能用。

反过来说，遇到"教程能跑、Termux 跑不通"的情况，别急着怀疑自己学错了——先查这张表，再查官方 wiki，九成能对上号。剩下的一成，去 proot-distro 里装个发行版试试，那已经接近完整环境了。

#### 案例实录：二十分钟整理一团糟的下载目录

场景：下载目录里堆了三个月的东西——发票照片、课件 PDF、聊天记录导出的压缩包，混作一团，每次找文件靠肉眼滚屏。用命令行整理，全程二十分钟。

1. cd ~/storage/downloads 进目录，ls -l 看全貌，后面接一个 | less 分页慢慢翻——你的第一个管道，用上了。
2. mkdir -p 发票/课件/压缩包，一次建好三个分类文件夹，-p 参数允许一次建多层。
3. 按关键词归堆：mv *发票* 发票/ 这类操作，通配符 * 表示"匹配任意内容"，一学就会。文件名里带关键词的，几条命令归完。
4. 名字完全看不出类型的，别猜。ls -t 按时间排列之后逐个确认——拿不准的留在原地，宁可慢一点也不放错。
5. 把上面几条 mv 命令存进一个 sort.sh，下次下载堆积了直接跑；顺手放进 .shortcuts/ 做成桌面按钮。
6. 整理完再 ls 一遍核对，确认没有文件失踪，收工。

这次实战用到的新知识只有两个：通配符和管道。但解决的是一个真问题。命令行整理文件还有个隐藏好处：mv 本质是改名操作，不存在"复制到一半断网"的中间态，比图形界面拖拽稳得多。

收尾提醒必须放在前面说：这次整理的是共享存储，是你手机里真实的文件，不是练习沙盒。在共享存储动 rm 之前，把"rm 的两条保命习惯"再读一遍——先 ls 确认，再用不带 f 的删除。胆大心细，缺一不可。

#### 把 Termux 用进日常的十个瞬间

学工具最大的动力是"用得上"。给你十个真实的小场景，每个都只需要这一章教过的东西：

- 课程资料打包成十个压缩包，一条循环命令批量解压，不用点十次。
- 查一个关键词在几十个笔记文件里各出现几次，grep -c 一秒钟。
- 批量给照片文件名加上拍摄日期前缀，相册导出的乱名瞬间整齐。
- 加密一个压缩包再发给别人，密码另发一条消息——敏感文件的正确寄法。
- 想练 SQL，装个 sqlite3，手机上就是一整块练习场。
- 看懂服务器日志的前一百行，grep 带行号定位问题。
- 把常去的几个网站抓成纯文本存档，curl 一条命令的事。
- 写一个每日提醒脚本，termux-notification 到点弹通知。
- 把散落各处的表格数据合并成一个文件，处理完发回电脑接着用。
- 给朋友演示"手机也是电脑"，顺手安利这本书。

清单的目的不是让你照做，而是让你意识到：凡是"电脑命令行能干"的事，多数在这台手机上也能干。脑子里有这张清单，机会出现的那一刻，你才抓得住。

还有一个更隐蔽的收益：这份清单会改变你和手机的关系。手机不再只是消费工具，它开始能替你"干活"。这种掌控感，是命令行送给每个初学者的礼物。

#### 常用组合命令十连

单个命令是砖，组合起来才是房子。给你十组常用组合，每组附一句"什么时候用"，抄进备忘录里慢慢用熟：

- ls -lhS | head：找出当前目录最大的几个文件，清理空间第一步。
- du -sh * | sort -h：看每个文件夹占多少空间并从小到大排列，空间去哪了一目了然。
- grep -rn 关键词 .：在当前整个目录树里搜关键词并带行号，找内容的神器。
- find . -name "*.txt" | wc -l：统计某类文件的数量。
- history | tail：翻最近敲过的几条命令，"刚才那条怎么写的来着"。
- 命令 > log.txt 2>&1：把正常输出和报错一起存进文件，求助时贴它（写法以 help 为准）。
- tar -zcf 包名.tar.gz 目录名：把整个目录打包压缩，备份的基本功。
- cat 文件 | grep -v 注释 | less：看配置文件时过滤掉注释行，清爽很多。
- date +%F：生成形如年月日的日期字符串，给备份文件起名用。
- 命令1 && 命令2：前一条成功才执行后一条，pkg update && pkg upgrade 就是它。

别一次全用。哪天的真实需求撞上了哪一条，就用哪一条——组合命令的价值只有在真实需求里才会显出来。用熟十组，你的命令行就已经超过大多数"入门者"了。

#### 把 Termux 推荐给朋友时，从哪一步开始

用出心得后，你多半想安利给朋友。别一上来就甩十个命令，那只会把人吓跑。好的入门路径是三步：先让人在朋友手机上装好官方版（帮他做"认清渠道"那一步），再带他跑通"跟着敲：第一个半小时"的前五条命令，然后就停住——让他自己用一周。

一周后他回来问的问题，才是最好的教学材料。他要解压文件，你教 pkg install；他嫌打字慢，你教 Tab 补全；他想备份照片，你带他写第一个脚本。需求拉动的教学，比我按顺序灌输有效得多。

还有一句实话要一起说：Termux 不是人人需要。朋友如果只是刷视频聊天购物，装它纯属添乱。判断标准很简单——他有没有"想在手机上干活"的时刻。有，才值得装；没有，把这本书的其他章节推给他也一样是好意。

#### 常见问题 FAQ

<strong>问：装完打开是黑屏，提示符一直不出来？</strong>答：八成是 bootstrap 初始化失败。检查剩余存储空间和网络，强制停止后重开；反复失败就按同一来源原则卸载重装（先备份家目录）。

<strong>问：pkg install 报 404，包明明存在？</strong>答：先 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update</code> 刷新源；还不行就 termux-change-repo 换镜像，国内网络首选国内镜像。

<strong>问：termux-setup-storage 敲完没反应？</strong>答：弹窗可能被系统拦了，去系统设置里手动给 Termux 文件权限，再跑一次命令。

<strong>问：能装 sudo 吗？</strong>答：没有，也不需要。沙盒里你就是最高权限，教程里的 sudo 直接删掉跑。

<strong>问：竖线、波浪号这些符号打不出来？</strong>答：音量加+Q 呼出扩展按键行，或在输入法的符号面板里找。常用符号一上手就记住了。

<strong>问：怎么把 Termux 里生成的文件发给别人？</strong>答：复制到 ~/storage/downloads，然后在微信、网盘里当普通文件发。反过来，别人发你的文件也在那个文件夹里。

<strong>问：电脑 ssh 连手机总超时？</strong>答：三连问——同一 Wi-Fi 吗？IP 对吗？sshd 起了吗？都不行就重启 Termux 再 sshd 一次。

<strong>问：F-Droid 下载太慢怎么办？</strong>答：改走 GitHub Releases，或换个时间段。别用第三方"加速"下载站，宁可等。

<strong>问：装插件提示签名冲突、应用未安装？</strong>答：来源混了。全家卸干净，从同一来源重装，重要数据先备份。

<strong>问：手机重启后，之前的会话和任务没了？</strong>答：正常现象，安卓重启会终止会话。要开机自动跑任务，用 Termux:Boot 插件。

#### 误区清单

- 很多人以为 Termux 等于 root，其实它就是个普通 App：沙盒内自由，沙盒外无权。
- 很多人以为 Linux 软件都能装，其实依赖 systemd 的服务、桌面软件、需要特定内核模块的东西，装不了或跑不了。
- 很多人以为应用商店里的 Termux 是正版，恰恰相反——官方渠道是 F-Droid 和 GitHub Releases。
- 很多人以为手机能替代服务器，其实省电策略、网络切换、发热降频，都在跟"长期在线"作对。
- 很多人以为换新手机数据会自动全搬过去，其实 Termux 家目录在沙盒里，多数换机工具搬不到它——要按"备份与迁移"一节手动带。
- 很多人以为装了 Termux 手机就会卡，其实闲置的它只是个躺在沙盒里的应用，卡的是你让它跑的重活。

#### 小项目：用 Termux:API 做一个剪贴板日记

学了插件一节，来做一个只有 Termux 能做的小东西：剪贴板日记。思路是——你平时复制的任何内容（网址、灵感、待办），跑一下小命令，就追加进一个日记文件，攒着以后翻。

做法只有两步。装齐插件（Termux:API 应用加 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install termux-api</code>）；然后做一个几行的脚本：先 termux-clipboard-get 取出剪贴板内容，再判断不是空的，就带上时间戳追加写进 diary.txt（date 命令生成时间，重定向符号 >> 表示追加写入）。脚本怎么组织，套用"脚本入门"一节的模板就行。

跑通之后，放进 .shortcuts/ 配 Termux:Widget 做成桌面按钮。从此你的复制动作多了一个去向：随手复制一段话，点一下按钮，它就进了你的日记。这个项目把插件、脚本、重定向、日期命令全串了一遍——做完它，你对这一章的理解会上一个台阶。

同类思路还能变出好几个工具：用 termux-notification 做喝水提醒，用 termux-battery-status 写个"电量低于两成弹通知"的小脚本，用 termux-tts-speak 把长文读出来边走边听。这些小工具的共同点是：需求小、命令少、成就感大。

手机命令行玩到这个阶段，你就不再是"学工具的人"，而是"用工具造东西的人"了。这中间的距离，就是几个十几行的小脚本。

提醒一句隐私边界：剪贴板里偶尔会有验证码、地址这类敏感内容，diary.txt 存在沙盒里还算安全，但别把它同步到公共位置，也别把脚本原样发给别人——里面可能躺着你的复制习惯。

#### 输入与显示的疑难再答四条

<strong>问：终端里的中文显示正常，跑脚本时输出却是一堆问号？</strong>答：多半是文件编码问题。把脚本和数据文件都保存成 UTF-8 编码（nano 默认就是），问题基本消失；还乱码就检查生成文件的那个环节用什么编码写的。

<strong>问：命令太长，能不能换行输入？</strong>答：能。行尾敲一个反斜杠再回车，命令会"接着"写——这在写长命令时特别有用。但注意反斜杠后不能有空格，这是新手高频踩坑点。

<strong>问：误按了什么，屏幕显示全是奇怪字符？</strong>答：先 Ctrl+C 中断，不行就敲 reset 命令（或干脆关掉这个会话开个新的）。显示乱套不影响真实文件，别慌。

<strong>问：怎么复制终端里翻不到的内容？</strong>答：把输出重定向到文件再看，比如 命令 > out.txt，然后用 less 或编辑器看、用剪贴板插件复制。长输出别硬在屏幕里找——落地成文件才是正路。

#### 七、版本与兼容性

Termux的最新稳定版本是v0.118.3（以 GitHub Releases 页面为准），适用于Android ≥ 7的设备。需要注意的是，Termux在Android 12及更高版本上可能存在不稳定性，建议关注官方更新日志以获取最新兼容性信息。

再补几句实在的。主程序升级：F-Droid 用户在 F-Droid 里更新，GitHub 用户重新下载新 APK 覆盖安装，两条路别混；软件包升级是另一码事，在终端里跑 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg upgrade</code> 就行，两者互不影响。换手机迁移：新手机装好后，老手机的家目录数据可以打包带过去（备份方案以官方 wiki 为准），比一件件重配省事。老设备能不能跑？Android ≥ 7 都能装，但老机器存储小、省电策略狠，练命令行没问题，跑重活就算了。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>总结

{class="mt-1"}
Termux将强大的Linux终端体验带到了Android设备上，让手机成为一台便携的开发和学习工具。无论是开发者、系统管理员还是技术爱好者，都可以利用Termux在移动设备上享受完整的命令行体验，实现"口袋里的Linux"这一理念。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：在手机上跑通第一条Linux命令

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 从F-Droid下载并安装Termux，首次启动等待初始化完成。
2. 执行<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code>更新软件包。
3. 安装Python：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install python</code>。
4. 输入<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python3 -c "print('Hello from Termux!')"</code>，感受在手机上运行代码的乐趣。
:::
