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

#### 二、核心功能与特性

##### 🖥️ 完整的Linux环境

Termux<strong>仅内置Bash</strong>这一种Shell。如果想使用Zsh或fish等其他Shell，需要通过包管理器手动安装，例如：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install zsh</code>或<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install fish</code>。同时Termux支持Vim、Nano、Emacs等编辑器，提供接近原生的命令行体验。用户可以通过"pkg install"安装2000+软件包，包括GCC、OpenSSH、SQLMap等开发和安全工具。

##### 📦 强大的包管理

使用APT包管理器（类似Debian和Ubuntu），可安装数千种Linux软件包，涵盖开发工具、网络工具等。支持Python、Ruby、Node.js、Go、Rust、Swift等多种编程语言环境。

##### 🔒 安全与网络功能

- <strong>SSH远程连接</strong>：支持SSH客户端和服务器功能，可远程连接其他设备或让手机成为SSH主机。
- <strong>加密工具</strong>：提供OpenSSL等加密工具，支持数据加密和安全通信。
- <strong>服务器搭建</strong>：可配置Nginx或Apache搭建静态网页服务器。

##### 🔧 系统集成与扩展

- 访问手机存储权限，实现本地文件管理。
- 通过Termux:API插件调用传感器、摄像头等Android硬件功能。
- 支持蓝牙键盘和外部显示器连接，具有完整的鼠标支持。

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

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>重要提示

{class="mt-1"}
Termux及其插件必须从同一来源安装，因为它们共享相同的sharedUserId。混合来自不同来源（如F-Droid和GitHub）的安装将导致安装错误。
:::

#### 四、安装与配置指南

##### 📥 安装步骤

1. <strong>下载应用</strong>：从官方渠道（F-Droid或GitHub）下载安装Termux，无需root权限。
2. <strong>初始化系统</strong>：首次启动后等待"Installing bootstrap packages"完成。
3. <strong>获取存储权限</strong>：执行<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-setup-storage</code>获取手机文件系统权限。
4. <strong>更新软件源</strong>：执行<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code>更新软件包列表。

##### ⚙️ 基础优化

- <strong>换镜像源</strong>：使用<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-change-repo</code>命令通过图形界面更换镜像源（推荐清华大学镜像源）。
- <strong>快捷键设置</strong>：音量减键模拟Ctrl，音量加键模拟Esc，提升输入效率。
- <strong>界面美化</strong>：安装Zsh + Oh My Zsh，配置主题和插件。

#### 五、典型应用场景

##### 💻 移动开发测试

在手机上搭建完整的开发环境，编写并运行Python脚本，使用GCC编译C程序，通过Git管理代码仓库，结合SSH与远程服务器同步。

##### 🖥️ 服务器运维

通过SSH远程管理服务器，执行系统维护、日志分析等任务，随时随地处理服务器问题。

##### 📚 学习Linux操作

提供真实的Linux环境，是学习命令行和系统管理的理想平台，可练习Shell脚本编写、Linux文件权限管理（如 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chmod 755</code> 设置 rwxr-xr-x 权限位、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chown user:group</code> 修改文件归属、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls -l</code> 查看 owner/group/other 三组九位权限）等基础命令。注意这是Unix/Linux经典的"三组九位"权限模型（owner / group / other × 读 / 写 / 执行），与Windows NTFS的ACL访问控制列表是完全不同的两套体系。

##### 🔐 网络安全测试

安装Nmap、SQLMap、Hydra、Metasploit等安全工具，进行网络扫描和渗透测试。

#### 六、版本与兼容性

Termux的最新稳定版本是v0.118.2，适用于Android ≥ 7的设备。需要注意的是，Termux在Android 12及更高版本上可能存在不稳定性，建议关注官方更新日志以获取最新兼容性信息。

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
