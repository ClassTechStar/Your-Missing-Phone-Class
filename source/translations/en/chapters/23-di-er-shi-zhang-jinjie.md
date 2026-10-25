---
id: di-er-shi-zhang-jinjie
num: 20
part: jin-jie-pian
nav: Chapter 20: Developer Mode and Advanced Permissions
toc: default
kind: supplement
---

### Chapter 20: Developer Mode and Advanced Permissions

{class="chapter-intro mb-4"}
This chapter is for users who want to deeply explore the "hidden features" of their phone. Developer Mode, Root permissions, BL lock... these geeky-sounding concepts are actually not far from ordinary users.

#### 1. Developer Mode: Unlock Hidden Settings

Developer Mode is a hidden menu built into the phone system, containing many features that ordinary users don't need but developers do.

##### How to enable:

- <strong>Android</strong>: Go to Settings &gt; About Phone &gt; tap "Build Number" 7 times continuously, until it prompts "You are now in developer mode".
- <strong>HarmonyOS</strong>: Settings &gt; About Phone &gt; tap "HarmonyOS Version" 7 times continuously.
- <strong>iOS</strong>: Ordinary users cannot enable full Developer Mode—it requires a paid Apple Developer account.

##### Commonly Used Features Overview:

- <strong>USB Debugging</strong>: A must-enable switch for connecting to a computer for advanced operations (such as flashing, data recovery, ADB commands). See the "ADB Practical Commands" section in this chapter.
- <strong>Show Taps</strong>: Shows touch points on screen (a small dot following your finger), suitable for recording tutorials or demos.

##### Performance &amp; Smoothness Related:

- <strong>Animation Speed Adjustment (Window Animation Scale / Transition Animation Scale / Animator Duration Scale)</strong>: These three options control the animation duration when opening apps and switching pages. The default is 1x; setting to 0.5x makes the phone "feel" faster (the actual program speed hasn't changed, just the animation is quicker); setting to off disables animations entirely. Most geeks set it to 0.5x — it preserves transition feel while seeming fast. Completely disabling animations can make operations feel abrupt and may mask real program stuttering, misleading you into thinking it's "very smooth."
- <strong>Force GPU Rendering</strong>: Forces all 2D drawing to be processed by the GPU instead of the CPU. Can improve scrolling smoothness on older models or with poorly optimized apps, but also increases GPU load and power consumption. Modern phones already use GPU rendering extensively by default, so this toggle has limited impact on mid-to-high-end models — it's more of a legacy option. Ordinary users should keep the default.
- <strong>Profile GPU Rendering</strong>: Displays a real-time bar chart on screen showing the rendering time of each frame. The green horizontal line represents 16.6ms (the frame time threshold for 60fps). Bars above the green line indicate dropped frames. This is a developer tool for troubleshooting app stuttering — ordinary users can also use it to compare which apps are poorly optimized. For example, if an app's bars frequently spike above the red line during scrolling, it's basically that app's fault.

##### Background &amp; Battery Related:

- <strong>Settings in Developer Mode may affect system stability—don't change options you don't understand. After enabling USB Debugging, be careful when connecting to computers, and don't connect to untrusted computers.</strong>: You can set "Standard limit," "At most 1 process," "At most 2 processes," etc. On the surface, limiting background processes seems like it would save battery, but Android's built-in background management is already quite good. Forcibly limiting it causes apps to reload frequently (cold starts actually consume more power and worsen the experience). This option is more suited for debugging — ordinary users shouldn't keep it enabled long-term; "Standard limit" is fine.
- <strong>Don't Keep Activities</strong>: Destroys every activity as soon as you leave it. Highly discouraged — causes frequent white screens and reloads, only for testing app recovery logic.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Notes

{class="mt-1"}
: Prevents malicious software from being flashed into the system.
:::

#### II. OEM Unlocking: The "Flashing Switch" in Developer Options

In Developer Options, there's an inconspicuous but important toggle — "OEM Unlocking" (some brands call it "Allow OEM Unlocking" or "Device Unlocking"). This toggle doesn't unlock the Bootloader itself — it's a "prerequisite permission": only when enabled will the manufacturer allow you to unlock the BL via fastboot commands or brand tools.

- <strong>Purpose of the Toggle</strong>: Equivalent to declaring to the manufacturer "I agree to waive my warranty and accept the risks — please allow me to unlock the BL." If this toggle is off, any BL unlock command will be rejected outright.
- <strong>Relationship with the BL Lock</strong>: OEM Unlocking is the "qualification application," while BL Unlock is the "actual operation." The former is just a tap in phone settings; the latter requires applying for an unlock code from the manufacturer's website and running fastboot commands on a computer (such as <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing unlock</code>), and both are indispensable.
- <strong>Does Factory Reset Reset It?</strong>: Yes. The "OEM Unlocking" toggle returns to off after a factory reset, but once the BL is unlocked, it's a physical-level state — a factory reset won't relock it. You need to manually execute <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing lock</code> to relock it.
- <strong>When Should You Enable It</strong>: Unless you're certain you want to flash or Root, keep it off. It and "USB Debugging" are independent toggles — both usually need to be enabled simultaneously when flashing.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Trivia: Why Do Manufacturers Include This Toggle

{class="mt-1"}
Early Android didn't have this toggle, so malware could silently flash the system as long as it got permissions. Google later required all Android manufacturers to include the "OEM Unlocking" toggle in Developer Options as a "user informed consent" confirmation. This is why even if you've unlocked the BL, reflashing will still fail if the OEM Unlocking toggle is turned off.
:::

#### III. Bootloader Lock: The First Gate to Flashing

: Even if the phone is flashed, it can't be used without the original account password.

##### Warranty restriction

- <strong>: Unlocking BL usually means losing official warranty.</strong> BL lock policies by brand:
- <strong>Xiaomi</strong>: Can be unlocked, requires account binding waiting period (7-30 days).
- <strong>Huawei</strong>: Stopped providing unlock codes after 2018, basically cannot be officially unlocked.

##### OnePlus

- <strong>Xiaomi</strong> OPPO/vivo
- <strong>Huawei</strong> Samsung
- <strong>: Can be unlocked, but triggers Knox fuse, losing Samsung Pay and other features.</strong> Apple
- <strong>[Install Apps from External Sources]</strong>3. Root Permission: Android's "Super Administrator"
- <strong>Samsung</strong> Benefits of Root:
- <strong>Apple</strong> Use advanced feature apps (like Titanium Backup, Greenify).

#### IV. ADB Practical Commands: Controlling Your Phone via Computer

ADB stands for Android Debug Bridge, an official Google command-line tool that lets a computer communicate with an Android phone via USB or Wi-Fi. It doesn't require Root — as long as the phone has "USB Debugging" enabled, you can use it. Think of it as a "remote control that sends commands from your computer to your phone" — flashing, installing apps, transferring files, checking logs, all rely on it.

##### How to Connect via USB:

1. On the phone: Enter Developer Options → enable "USB Debugging."
2. On the computer: Download Platform Tools from Google's official site (includes <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb</code> verb <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot</code> two executable files), extract to any directory.
3. Connect the phone and computer with a data cable. The phone will show a popup "Allow USB debugging?" — check "Always allow" and confirm.
4. In the computer's command line (Windows PowerShell or cmd), execute <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code>. If the output is similar to <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">List of devices attached / xxxxxxxx device</code>, the connection is successful.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Don't Ignore Driver and Authorization Popups

{class="mt-1"}
If Windows users see <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code> showing "unauthorized" or not listing the device at all, it's usually because the driver isn't installed properly or you forgot to tap "Allow" on the phone. Samsung/Xiaomi and other brands can install their respective "USB Drivers" or "Phone Assistant" to fix the driver; Mac and Linux generally don't need drivers. If you accidentally dismissed the phone popup, just unplug and replug the data cable and it will pop up again.
:::

##### Commonly Used ADB Commands:

- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb install app.apk</code>: Installs an APK from the computer to the phone (<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-r</code> means reinstall while keeping data;<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code> installs to SD card).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb uninstall com.xxx.xxx</code>: Uninstalls an app by package name.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb push [computer path] /sdcard/[target path]</code>: Pushes a file from the computer to the phone.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb pull /sdcard/[file] [computer path]</code>: Pulls a file from the phone to the computer (much faster than sending it to yourself on WeChat and downloading).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell</code>: Enters the phone's Linux shell, can directly execute <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls</code> and<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm</code> and<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">am</code> and other commands.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot bootloader</code>: Reboots the phone into Fastboot mode (the entry point for flashing).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot recovery</code>: Reboots into Recovery mode.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages</code>: Lists all installed app package names on the phone (essential for finding package names). Add <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code> to see only system apps, add <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-3</code> to see only third-party apps.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 [package name]</code>: Uninstalls pre-installed apps for the current user — no Root required. See the practical guide below.

##### Practical Guide: Uninstalling Pre-installed Apps Without Root:

This is one of ADB's most practical features: using the <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code> command, you can uninstall pre-installed apps for the "current user" without Root and without affecting the system partition. Uninstalled apps "disappear" from the system but are actually still in the system partition — they'll come back after a factory reset.

1. First use <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages -s</code> to list all system apps and find the package name you want to uninstall. For example, Xiaomi Browser is <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.browser</code>, and Huawei AppGallery is <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.vmall.client</code>.
2. Not sure which app a package name corresponds to? You can use <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages | findstr [keyword]</code> to search on the computer, or install a third-party app "Package Viewer" on the phone to directly view each app's package name.
3. Execute the uninstall:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 [package name]</code>. For example, <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 com.android.browser</code>. If it returns <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Success</code> , it's successful.
4. Want to restore? Two methods: ① Factory reset (most thorough but cumbersome); ② Reinstall:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell cmd package install-existing [package name]</code>.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>Never Delete Critical System Packages

{class="mt-1"}
Although "pm uninstall --user 0" is a safe method that doesn't require Root, deleting critical system apps (such as <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.systemui</code> status bar,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.phone</code> phone,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.settings</code> settings) can cause serious problems like system crashes, black screens, and inability to boot. Before deleting, Google "can this package name be deleted" — better to delete less than to delete wrong. Recommend deleting only one or two at a time and confirming everything is fine before continuing.
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Trivia: What Does --user 0 Mean?

{class="mt-1"}
Android 4.2+ supports multi-user, where each user has an independent ID (the owner is 0, additional users start from 10).<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">--user 0</code> means "uninstall for the current owner only" — the APK file in the system partition still exists, it's just not shown to the owner. That's why it doesn't need Root — it doesn't touch system files, it just changes the "user configuration." This is also the biggest difference from Root uninstalling: Root uninstalling actually deletes from the system, so no user has it anymore; ADB uninstalling just "hides it for the current user."
:::

#### V. Root Access: Android's "Super Administrator"

Root access is equivalent to the superuser in Linux (full control over the / directory, can read/write any file), the highest privilege level in Android. It fundamentally differs from Windows Administrator: Windows imposes many restrictions on administrators for security (the true highest privilege is actually TrustedInstaller), and even Administrator can't directly execute like Linux root can. <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">sudo rm -rf /*</code>. After obtaining Root access, you can modify system files, uninstall pre-installed apps, and use advanced apps that require Root.

##### Risks of Root:

- Loss of warranty
- : Most manufacturers don't warranty Rooted phones.
- Security risks
- : Malicious apps may obtain Root permission, causing serious consequences.

##### System instability

- <strong>XDA Developers</strong> Banking apps won't work
- <strong>: Many banking and payment apps refuse to run when Root is detected.</strong> OTA update failure
- <strong>: May not be able to receive official system updates normally.</strong> Severe Warning
- <strong>Root operations carry certain risks and may brick your phone (won't turn on). If you're a beginner, recommend fully understanding the relevant knowledge first and ensuring you have a complete backup. Read tutorials carefully before operating, and confirm your phone model and system version.</strong>4. Advice for Ordinary Users
- <strong>Developer Mode</strong>: Can be enabled to experience animation acceleration and other features, but don't randomly change other settings.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>BL lock

{class="mt-1"}
: If you don't plan to flash, keeping it locked is safer.
:::

#### VI. SafetyNet and Play Integrity Certification: Why Bank Apps Don't Work After Root

Many Root users have experienced this devastating moment: after Rooting and excitedly installing a bunch of modules, you open your bank app — "Your device is insecure and cannot be used," Google Pay doesn't work, and even Netflix refuses HD playback. Behind this is Google's two device integrity certification mechanisms: the older SafetyNet and the newer Play Integrity API.

##### What Are SafetyNet / Play Integrity:

- <strong>SafetyNet Attestation (Legacy, since 2017)</strong>: Google's early device integrity check API, where apps query Google servers to check "whether this device passed CTS compatibility testing and is in an unmodified official state." Results are divided into Basic Attestation and Strong Attestation (relies on hardware keys). Google has announced that SafetyNet will be gradually deprecated after 2024.
- <strong>Play Integrity API (New, since 2022)</strong>: Google's replacement, stricter and more comprehensive than SafetyNet. In addition to device integrity, it includes "app integrity" (whether the app has been tampered with) and "account/licensing integrity" (whether the user account is trusted by Google). New apps should migrate to Play Integrity.
- <strong>Who Uses It</strong>: Banking, financial, and payment apps (such as Google Pay, various banks' mobile banking, some scenarios of Alipay/WeChat Pay), streaming media (Netflix HD copyright protection), some game anti-cheat (such as some Tencent/NetEase games), enterprise office apps (MDM device compliance checks).

##### Play Integrity's Three Certification Levels:

- <strong>MEETS_DEVICE_INTEGRITY</strong>: The device runs genuine Android, Bootloader is locked, no Root, CTS compatibility test passed. Banking and payment apps work normally.
- <strong>MEETS_BASIC_INTEGRITY</strong>: The device is basically trustworthy, but may have minor anomalies. Some apps will degrade (e.g., Netflix still plays but limits resolution), some strict bank apps will refuse outright.
- <strong>MEETS_STRONG_INTEGRITY</strong>: The highest level, requires hardware key endorsement (such as the Titan M chip in Google Pixel series). Most third-party brand devices can't reach this level even without Root.
- <strong>No Label (NO_INTEGRITY)</strong>: The device is Rooted, BL is unlocked, a third-party ROM is flashed, or it's identified as an emulator. The vast majority of payment/banking apps will refuse to run.

##### Why Do These Apps Fail After Root:

Apps initiate certification requests to Google servers through the Play Integrity API. Google checks multiple device indicators — Bootloader lock status, whether the system partition has been modified, whether su binary files exist, whether SELinux is in permissive mode, etc. Any anomaly causes the returned certification level to be lowered or empty, and bank apps see "device insecure" and naturally refuse service.

##### Modern Hiding Solutions: Magisk Hide / Shamiko / Zygisk:

To enjoy Root convenience while still using banking apps, the community has developed a series of solutions to "hide the Root state." The core idea is the same: make the detection program see a "normal-looking" device instead of a modified system.

- <strong>: Old-school Root solution, currently no longer updated.</strong>: The current mainstream Systemless Root solution — doesn't modify the system partition, but achieves Root through mounting. The benefit of this design is a lower chance of OTA update failure and cleaner uninstall. It's the foundation for all subsequent hiding solutions. However, using Magisk still requires unlocking the BL.
- <strong>Magisk Hide (Discontinued)</strong>: Magisk's early built-in hiding module, could hide Root from specified apps. But since 2021 it was removed by Magisk officially, because Google continuously upgraded detection methods, and the two sides fell into a "cat-and-mouse game."
- <strong>Zygisk</strong>: A new mechanism introduced in Magisk 24.0+, similar to Riru, injects into the Zygote process to load modules, more stealthy than directly modifying the system. Enabling Zygisk is a prerequisite for using modern hiding solutions.
- <strong>Shamiko</strong>: The current mainstream hiding module, works with Zygisk, can hide Root for specified apps ("reverse whitelist" mode), hide Magisk itself, and fake the Bootloader lock status. Shamiko is distributed through the LSPosed repository or GitHub.
- <strong>Play Integrity Fix(osm0sis)</strong>: A Magisk module specifically targeting Google Play Integrity detection, modifies the device fingerprint to make Google think your device is an unrooted official model.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>The Cat-and-Mouse Game Never Ends

{class="mt-1"}
Google updates detection rules periodically, and app developers follow up with Play Integrity upgrades. A hiding solution that works today may be detected tomorrow. If you fully rely on banking/payment apps (such as daily transfers, QR code payments), the safest choice remains: don't Root, don't unlock the BL. Hiding solutions are more suitable for a "main phone without Root + backup phone for Root experimentation" enthusiast setup.
:::

#### VII. Advice for Ordinary Users

- <strong>: Not recommended for ordinary users—risks outweigh benefits. If you really need certain features, first look into whether there are alternatives that don't require Root.</strong>: You can enable it to experience animation acceleration, GPU rendering analysis, and other features, but don't randomly change other options you don't understand.
- <strong>OEM Unlocking and BL Lock</strong>: If you don't plan to flash or Root, keep both toggles in their default (off) state for maximum safety.
- <strong>ADB</strong>: A powerful no-Root tool that ordinary people can use too — for example, using <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code> to uninstall pre-installed apps. But before deleting, always check whether the package name can be safely deleted.
- <strong>Root</strong>: Root is not recommended for ordinary users — the risks outweigh the benefits. If you truly need certain features, first check whether there are no-Root alternatives (such as using ADB to uninstall pre-installed apps, or using Shizuku to replace some Root functionality).

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Hands-On: Enable Developer Mode and Adjust Animation Speed

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Go to Settings &gt; About Phone.
2. Tap "Build Number" 7 times in a row until it says Developer Mode is enabled.
3. Go back to Settings and find "Developer Options" (usually at the bottom of Settings or under "System").
4. Find "Window animation scale", "Transition animation scale", and "Animator duration scale", and set them all to 0.5x or off.
5. Feel whether the phone has become faster.
:::
