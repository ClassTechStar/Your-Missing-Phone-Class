---
id: di-er-shi-zhang-termux
part: jin-jie-pian
nav: Chapter 20 Appendix
toc: sub
kind: supplement
---

### Chapter 20 Appendix: Termux—A Portable Linux Terminal Environment on Android Devices

{class="chapter-intro mb-4"}
If you feel Developer Mode isn't "hardcore" enough and want to experience a complete Linux command line on your phone, then Termux is for you. It requires no root permission, yet can turn an ordinary Android phone into a portable Linux workstation—a powerful tool for advanced users to explore mobile development and operations.

#### 1. What Is Termux

Termux is an open-source terminal emulator and Linux environment application designed specifically for Android devices. It provides a complete Linux shell experience on your phone without requiring root permission. As a lightweight application (installation package only about 30MB), Termux supports a rich software ecosystem through the APT package management system, allowing users to run tools like Python, Node.js, Git, SSH on mobile devices, and even set up servers or perform penetration testing.

Termux's core advantages lie in its lightweight nature and high extensibility, suitable for development, learning, and system administration scenarios. It combines standard software packages with precise terminal emulation in an open-source solution.

#### 2. Core Features and Characteristics

##### 🖥️ Complete Linux Environment

Termux <strong>Only Bash is Built-in</strong> is the only built-in shell. If you want to use Zsh, fish, or other shells, you need to install them manually via the package manager, for example:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install zsh</code> or<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install fish</code>. Termux also supports editors like Vim, Nano, and Emacs, providing a near-native command-line experience. Users can install 2000+ packages via "pkg install," including GCC, OpenSSH, SQLMap, and other development and security tools.

##### 📦 Powerful Package Management

Uses the APT package manager (similar to Debian and Ubuntu), can install thousands of Linux software packages, covering development tools, network tools, and more. Supports multiple programming language environments including Python, Ruby, Node.js, Go, Rust, and Swift.

##### 🔒 Security and Network Features

- <strong>SSH remote connection</strong>: Supports SSH client and server features—connect to other devices remotely or turn your phone into an SSH host.
- <strong>Encryption tools</strong>: Provides encryption tools like OpenSSL, supports data encryption and secure communication.
- <strong>Server setup</strong>: Can configure Nginx or Apache to set up a static web server.

##### 🔧 System Integration and Extension

- Access phone storage permissions for local file management.
- Call Android hardware features like sensors and cameras through the Termux:API plugin.
- Supports Bluetooth keyboard and external display connection, with full mouse support.

#### 3. Plugin Ecosystem

Termux's core application can be extended through several optional plugin apps, providing additional functionality and integration:

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Plugin Name</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Feature Description</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:API</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Exposes Android API functionality to command-line programs</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Boot</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Allows running scripts when the device boots</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Float</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Provides a floating terminal window</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Styling</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Enables color schemes and font customization for the terminal</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Tasker</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Integrates Termux scripts with the Tasker automation app</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Widget</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Allows running scripts from home screen widgets</td>
                            </tr>
                        </tbody>
                    </table>
```

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Important Note

{class="mt-1"}
Termux and its plugins must be installed from the same source, because they share the same sharedUserId. Mixing installations from different sources (such as F-Droid and GitHub) will result in installation errors.
:::

#### 4. Installation and Configuration Guide

##### 📥 Installation Steps

1. <strong>Download the app</strong>: Download and install Termux from official channels (F-Droid or GitHub), no root permission required.
2. <strong>Initialize the system</strong>: Wait for "Installing bootstrap packages" to complete after first launch.
3. <strong>Get storage permission</strong>: Execute<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-setup-storage</code> to get phone file system permission.
4. <strong>Update package sources</strong>: Execute<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">: Use the</code> to update the package list.

##### ⚙️ Basic Optimization

- <strong>Change mirror source</strong>: Use the<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Enter</code> command to change the mirror source through a graphical interface (Tsinghua University mirror recommended).
- <strong>Shortcut settings</strong>: Volume down key simulates Ctrl, volume up key simulates Esc, improving input efficiency.
- <strong>Interface beautification</strong>: Install Zsh + Oh My Zsh, configure themes and plugins.

#### 5. Typical Use Cases

##### 💻 Mobile Development Testing

Set up a complete development environment on your phone, write and run Python scripts, compile C programs with GCC, manage code repositories with Git, and sync with remote servers via SSH.

##### 🖥️ Server Operations

Remotely manage servers via SSH, perform system maintenance, log analysis, and other tasks, handling server issues anytime, anywhere.

##### 📚 Learning Linux Operations

Provides a real Linux environment, an ideal platform for learning the command line and system administration—you can practice Shell scripting and Linux file permission management (such as  <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">🔐 Network Security Testing</code> Install security tools like Nmap, SQLMap, Hydra, and Metasploit for network scanning and penetration testing.<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">6. Version and Compatibility</code> The latest stable version of Termux is v0.118.2, suitable for devices with Android ≥ 7. Note that Termux may have instability on Android 12 and higher versions; recommend following the official update log for the latest compatibility information.<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Provides a real Linux environment, making it an ideal platform for learning command line and system administration. You can practice Shell scripting, Linux file permission management (such as</code> chmod 755

##### 🔐 Network Security Testing

Install Nmap, SQLMap, Hydra, Metasploit, and other security tools for network scanning and penetration testing.

#### 6. Versions and Compatibility

The latest stable version of Termux is v0.118.2, for devices running Android 7.0 and above. Note that Termux may be unstable on Android 12 and higher; follow the official changelog for the latest compatibility information.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Summary

{class="mt-1"}
Termux brings the powerful Linux terminal experience to Android devices, making the phone a portable development and learning tool. Whether developers, system administrators, or tech enthusiasts, all can use Termux to enjoy a complete command-line experience on mobile devices, realizing the concept of "Linux in your pocket".
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Hands-on: Run Your First Linux Command on Your Phone

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Download and install Termux from F-Droid, wait for initialization to complete on first launch.
2. Execute<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code> to update packages.
3. Install Python:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install python</code>.
4. Enter<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python3 -c "print('Hello from Termux!')"</code>, and experience the joy of running code on your phone.
:::
