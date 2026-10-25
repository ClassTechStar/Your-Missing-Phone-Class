---
id: di-yi-zhang-harmony
part: ji-chu-pian
nav:  Chapter 1 Appendix: HarmonyOS Operating System Special Topic
toc: default
kind: supplement
---

### Chapter 1 Appendix: HarmonyOS Operating System Special Topic

{class="chapter-intro mb-4"}
HarmonyOS is Huawei's self-developed operating system. Since its release in 2019, it has gone through several major versions. It's not just "another Android replacement"—it's a new species with a unique design philosophy. Let's dive deep into this rising operating system.

#### 1. What Is HarmonyOS? Why Is It Different?

HarmonyOS's core philosophy is "interconnection of all things." Unlike traditional operating systems that primarily serve a single device, HarmonyOS was designed from the start with multi-device collaboration in mind.

<strong>Distributed architecture</strong> is the soul of HarmonyOS. Simply put, it can virtualize multiple devices into a "super terminal." Your phone, tablet, computer, watch, and TV are no longer isolated individuals but integrated "organs" that can call upon each other's capabilities.

For example: You're watching a video on your phone and want to see it on a bigger screen. The traditional way is screen casting; on HarmonyOS, you can directly "stream" the video to the TV to continue watching, with the phone becoming a remote control. This isn't simple screen casting—the app itself is running across devices.

#### 2. HarmonyOS 4.3: A Mature Version Based on AOSP

HarmonyOS 4.3 is the currently widely deployed version on Huawei phones. It should be noted that HarmonyOS 4.3 is compatible with the code framework of the Android Open Source Project (AOSP), so it can fully support Android apps—most apps you download from the Huawei AppGallery are essentially still Android apps, running through HarmonyOS's compatibility layer. But HarmonyOS 4.3 is not simply a reskinned Android; it adds a large number of Huawei's self-developed distributed capabilities, Ark engine, and other technologies on top of AOSP.

##### Core Features:

- <strong>Android app compatibility</strong>: Since it's developed based on AOSP, HarmonyOS 4.3 can run almost all Android apps normally; users hardly notice any difference.
- <strong>Ark engine</strong>: Huawei's self-developed compiler and runtime, making apps run more smoothly and power-efficiently. Compared to early versions, fluidity has improved significantly.
- <strong>Super Device</strong>: In the Control Center, you can intuitively see other HarmonyOS devices around you—just drag to connect. It's convenient for the phone to use the computer's keyboard and mouse, or the tablet to use the phone's camera.
- <strong>Service cards</strong>: Similar to iOS widgets, but more flexible. You can swipe up on an app icon to expand a card showing key information without opening the app.
- <strong>or</strong>: Only allows installing apps from the official app store, reducing malware risks.
- <strong>Privacy Center</strong>: Centrally manage app permissions and view app behavior records.

##### User Interface Features:

- <strong>Magazine lock screen</strong>: The lock screen displays beautiful images and articles; swipe to enter the home screen.
- <strong>Universal cards</strong>: Home screen icons can be expanded into cards to display more information.
- <strong>Super Hub</strong>: A temporary storage area where you can stash text, images, and files, then drag them into any app. Cross-app sharing becomes incredibly smooth.
- <strong>Smart Search</strong>: Global search that can find apps, files, settings, and web pages.

#### 3. HarmonyOS NEXT (HarmonyOS 6): The True Starting Point of Huawei's Autonomous Operating System

HarmonyOS NEXT (HarmonyOS NEXT 5.0) is fundamentally different from HarmonyOS 4.3—it uses Huawei's self-developed HarmonyOS microkernel, no longer relying on the Linux kernel and AOSP code, and <strong>no longer directly supports Android apps</strong>. This is the key step for HarmonyOS to officially transition from "an Android-compatible transitional form" to "a fully independent operating system."

##### Major Changes:

- <strong>Fully autonomous kernel</strong>: HarmonyOS NEXT uses Huawei's self-developed kernel, containing no AOSP code. The system is more streamlined, more secure, and more efficient.
- <strong>No longer supports Android apps</strong>: This is the biggest change. HarmonyOS NEXT can only run native HarmonyOS apps and cannot install or run APK files. Before upgrading, please confirm that your frequently used apps already have native HarmonyOS versions.
- <strong>Native app ecosystem</strong>: Huawei is fully pushing developers to migrate apps to the native HarmonyOS platform. Currently, mainstream apps such as WeChat, Alipay, and Taobao have launched native HarmonyOS versions, but some niche apps may not yet be adapted.
- <strong>Star Shield security architecture</strong>: A brand-new security system with full-chain protection from hardware to software. Supports finer-grained permission control, such as "fuzzy location"—apps can only know roughly where you are, not your precise location.
- <strong>Deep AI integration</strong>: System-level AI capabilities, not just a single app having AI. For example, AI subtitles can translate videos in real time, and AI cutout can intelligently identify subjects.
- <strong>Cross-device seamless streaming</strong>: Further distributed capabilities. App state can switch seamlessly between devices—a document you're editing on your phone automatically opens on your computer when you walk up to it.
- <strong>Meta-services</strong>: Lightweight services that can be used without installation. For example, scanning a QR code directly opens a function without first downloading an app.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Must-Read Before Upgrading to HarmonyOS NEXT

{class="mt-1"}
After upgrading to HarmonyOS NEXT, your phone will not be able to run Android apps. Please be sure to confirm before upgrading: ① Your frequently used apps already have native HarmonyOS versions; ② Your work or life doesn't have scenarios that must depend on Android apps. After upgrading, you cannot roll back to HarmonyOS 4.3.
:::

##### Operation Logic Changes:

- <strong>Gesture navigation</strong>: Swipe from left or right edge to go back, swipe up from the bottom to return to the home screen, swipe up and pause to enter multitasking.
- <strong>Smart multi-window</strong>: Supports split screen, floating windows, parallel view, and other multitasking forms.
- <strong>Celia calls</strong>: Huawei's video call service, supporting screen sharing, beauty effects, and background blur.

#### 4. HarmonyOS Ecosystem: Devices and Apps

HarmonyOS is not just a phone system—it's an ecosystem covering multiple devices.

##### Supported Device Types:

- <strong>Phones and tablets</strong>: Core devices with the most complete functionality.
- <strong>Smart watches and bands</strong>: Run independently or in coordination with the phone.
- <strong>Smart screens (TVs)</strong>: Home entertainment centers.
- <strong>Smart speakers</strong>: Voice interaction entry points.
- <strong>Automobiles</strong>: HarmonyOS cockpit, smart driving cabin experience.
- <strong>Smart home</strong>: Refrigerators, air conditioners, washing machines, etc.

##### App Ecosystem Status:

The HarmonyOS App Market already has millions of apps, and mainstream apps are essentially all available. Huawei is also actively encouraging developers to create native HarmonyOS apps. As of mid-2026, top apps including WeChat, Alipay, Taobao, Douyin, Meituan, and JD.com have all launched native HarmonyOS versions, making daily use largely barrier-free. Some niche and industry-specific apps may still be in adaptation — before upgrading, it's recommended to confirm whether your frequently used apps are already supported.

#### 5. HarmonyOS Practical Tips

- <strong>Super Device</strong>: Swipe down from the top right of the screen to open the Control Center, tap "Super Device" to see other devices around you—drag to connect.
- <strong>Super Hub</strong>: Long-press text/images/files, select "Copy to Hub," then long-press to paste in other apps, or drag it out.
- <strong>Service cards</strong>: Swipe up on an app icon to expand the card; long-press the card to resize or add to the home screen.
- <strong>Smart multi-window</strong>: Swipe inward from the left or right edge of the screen and pause to open the sidebar; tap an app to open it as a floating window.
- <strong>Privacy protection</strong>: Settings &gt; Privacy, where you can view app permission usage records, set fuzzy location, etc.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Notes

{class="mt-1"}
HarmonyOS is continuously updating and iterating; different versions may have some differences. This description is based on the main features of HarmonyOS 4.3 and 6; specific functions are subject to your phone's actual version. It's recommended to keep the system updated to get the latest features and security patches.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Try It Now: Experience HarmonyOS Features

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Open the Control Center, find "Super Device," and see if there are other HarmonyOS devices around.
2. Try "Super Hub": Copy some text to the Hub, then drag it out in Notes.
3. Swipe up on a few common app icons to see what their service cards display.
4. Go to Settings &gt; Privacy to see which apps have recently used sensitive permissions.
:::
