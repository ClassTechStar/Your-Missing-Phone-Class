---
id: di-si-shi-jiu-zhang
num: 49
part: an-zhuo-kai-fa-pian
nav: Chapter 49: Setting Up Your Dev Environment — Android Studio and Your First Project
toc: default
kind: chapter
---

### Chapter 49: Setting Up Your Development Environment — Android Studio and Your First Project

{class="chapter-intro mb-4"}
To do a good job, first sharpen your tools. In this chapter we set up the "kitchen": install Android Studio, get the emulator running, create the first Android project of your life, then take the project structure apart until it makes sense. Once the environment is set up, you'll see your own code turn into a tappable button for the first time — a moment many people remember for the rest of their lives.

#### I. Installing Android Studio

Android Studio is Google's official integrated development environment (IDE). It's free and a full all-in-one package: writing code, previewing UI, debugging, and packaging all happen inside it. Four steps to install:

1. Open the official site developer.android.com/studio and download the latest stable version (as of August 2026, the release after Narwhal; Windows/Mac/Linux builds are all available);
2. Run the installer and click "Next" all the way through — the setup wizard automatically includes the Android SDK and emulator components;
3. On first launch, download the SDK components as prompted (the default selections are fine; it may take a few minutes and a few GB of space);
4. When it's done you'll see the welcome screen — congratulations, the "kitchen" is set up.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Note: Know the Hardware Requirements

{class="mt-1"}
Android Studio is a memory hog: 16GB of RAM is recommended (8GB will run, but the emulator can lag), reserve at least 20GB of disk, and your CPU needs virtualization support (enable VT-x/AMD-V in the BIOS). If your computer really is old, use "real device debugging" instead of the emulator (covered in Section 4 of this chapter) — the experience is actually smoother.
:::

#### II. Creating Your First Project

On the welcome screen click New Project and pick the Empty Activity template (the cleanest beginner template), then fill in three things:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Setting</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">What to Enter</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Notes</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">My First App</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The app's name, shown on the phone's home screen</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Package name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example.myfirstapp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A globally unique identifier; the convention is a reversed domain name — keep the default for now</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minimum SDK</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API 26(Android 8.0)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minimum supported version; covers 95%+ of devices</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
The three things to fill in when creating a project

After you click Finish, Android Studio uses Gradle to automatically download dependencies and build the project (the first time takes a few minutes; every run after that is much faster). When the build finishes, you have a runnable app — even if it can only display one line: "Hello Android!".

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tip: The Ins and Outs of Package Names

{class="mt-1"}
The package name is like the app's "ID number" — it must be globally unique and can't be changed after publishing. For personal practice, com.example.xxx is fine; for a real product, switch to your own domain in reverse (like com.yourname.appname). Never publish with com.example — the store will reject it.
:::

#### III. Running It: Emulator and Real Device

The code is written — now you need a "phone" to run it on. You have two choices:

##### 1. The Emulator

An emulator is a virtual Android phone inside your computer. In Android Studio, open Device Manager > Create Device, pick a device (the Pixel series is recommended) > choose a system image (one with Google APIs) > download > launch. Then click the green triangle Run in the toolbar, and a few seconds later your app appears on the "phone" screen.

##### 2. Real Device Debugging (More Recommended)

A real phone is always the truest test environment — swipe feel, real network, real sensors; the emulator can't match any of it. Debugging on a real Android phone is simple:

1. On the phone, open [Settings] > [About phone] and tap "Build number" 7 times in a row to unlock "Developer options";
2. In [Developer options], turn on USB debugging;
3. Connect the phone to the computer with a data cable and choose "Allow USB debugging" in the popup;
4. Back in Android Studio, your phone appears in the device dropdown in the toolbar — click Run.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Watch Out: Don't Leave USB Debugging On

{class="mt-1"}
USB debugging is like opening a "back door" to your phone for computers. When charging in public or connecting to a computer you don't trust, be sure to turn USB debugging off so no one can read your data through it. Turn it off after each development session — make it a habit.
:::

#### IV. Project Structure Explained: What Each File Does

The file tree on the left can make your head spin the first time you open a project. Don't panic — in daily development, 90% of your time is spent with just these few:

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="300" viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="300" fill="#fafafa" rx="8"/>
      <text x="20" y="30" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ project root</text>
      <rect x="30" y="45" width="540" height="230" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <text x="45" y="70" font-size="11" fill="#4f46e5" font-weight="bold">app/ ← where you write code</text>
      <rect x="60" y="82" width="240" height="178" fill="#eef2ff" rx="5"/>
      <text x="70" y="102" font-size="10" fill="#1e1b4b" font-weight="bold">src/main/</text>
      <text x="80" y="120" font-size="10" fill="#374151">├ java/…/MainActivity.kt  ← logic code</text>
      <text x="80" y="138" font-size="10" fill="#374151">├ res/  ← resources (images, text, colors)</text>
      <text x="80" y="156" font-size="10" fill="#374151">└ AndroidManifest.xml  ← the app's "birth certificate"</text>
      <text x="70" y="180" font-size="10" fill="#1e1b4b" font-weight="bold">build.gradle.kts</text>
      <text x="80" y="198" font-size="10" fill="#6b7280">Declares dependent libraries (SDK version, Compose, etc.)</text>
      <text x="70" y="222" font-size="10" fill="#1e1b4b" font-weight="bold">src/androidTest/ and test/</text>
      <text x="80" y="240" font-size="10" fill="#6b7280">Automated test code (used in Chapter 56)</text>
      <rect x="320" y="82" width="230" height="178" fill="#f0fdf4" rx="5"/>
      <text x="330" y="102" font-size="10" fill="#065f46" font-weight="bold">Other files in the root</text>
      <text x="340" y="122" font-size="10" fill="#374151">gradle/ + gradlew.bat  ← build scripts</text>
      <text x="340" y="142" font-size="10" fill="#374151">settings.gradle.kts  ← project settings</text>
      <text x="340" y="162" font-size="10" fill="#6b7280">(Beginner's rule of thumb: touch only the app/ folder,</text>
      <text x="340" y="180" font-size="10" fill="#6b7280">treat the rest as a "black box" for now — don't touch)</text>
      <text x="340" y="208" font-size="10" fill="#9ca3af">.gitignore  ← version-control ignore list</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figure 2: Project structure every beginner must know (the mantra: only touch the app/ folder)
:::

- MainActivity.kt: the app's "front door." When a user taps the icon, this is the first thing to wake up. In the current template it's responsible for displaying "Hello Android!".
- AndroidManifest.xml: the app's "household registry" — it declares what this app is called, which icon it uses, which screens it has, and which permissions it needs (camera, location, etc.).
- The res/ folder: the resource warehouse, storing images, icons, strings, and colors. Keeping text in resource files instead of hard-coding it into code is a good habit in Android development (it makes switching languages or themes easy).
- build.gradle.kts: the build recipe — it declares the minimum supported version and which libraries to depend on (like Compose).

#### V. A First Try: Change "Hello" to Your Name

Open MainActivity.kt and you'll see the code the Compose template generated. Find the line Text("Hello Android!") and replace the text inside the quotes with your name, e.g. Text("Hi, Zhang San! This is my first app"), then press Ctrl+R (Cmd+R on Mac) to run again. A few seconds later, your name appears on the emulator.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · MainActivity.kt (change this one line)</span><span class="dots">···</span>
:::

```
setContent {
    MyFirstAppTheme {
        Surface(modifier = Modifier.fillMaxSize()) {
            // ▼ change this to your own text
            Text("Hello, Alex! This is my first app")
        }
    }
}
```
:::

Congratulations — you've just completed a full "edit code → compile → install → run" cycle. This cycle is your daily development routine from now on. Strike while the iron is hot and change something else: make the font bigger, try another color — the next chapter shows where these "magic powers" come from.

#### VI. First Aid for Common Errors: The Beginner's "ER" for Your First Two Weeks

During environment setup and your first build, you'll most likely hit the three errors below. Don't panic — all of them have antidotes:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Error</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Common Cause</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Fix</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle sync failed / slow dependency downloads</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Poor network access to the repositories</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Configure a mirror repository for Gradle (Alibaba Cloud / Tencent Cloud Maven mirrors); search online for "gradle China mirror" and follow the instructions</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Missing SDK components</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The SDK download was skipped during installation</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Settings > SDK Manager: install the missing platforms and tools</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Emulator fails to start / black screen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Virtualization not enabled, or a corrupted image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Enable VT-x/AMD-V in the BIOS; delete and recreate the emulator; or just debug on a real device</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
First-Aid Table for Beginner Environment Errors

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tip: How to Search Error Messages

{class="mt-1"}
The first line of an error message is the most valuable — copy it verbatim into a search engine and add the keyword "android studio". Don't search vague questions like "why can't I set up my environment"; search specific errors like "Gradle sync failed: Could not resolve com.android.tools.build". Precise questions get precise answers.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Hands-On: Complete Your "Developer Ritual" Checklist

{class="mt-1"}
① Install Android Studio and get the emulator running; ② run your app on a real phone once and take a screenshot to keep; ③ change the Hello text to your name; ④ zip up the project as a backup. Once these four steps are done, you can announce to your friends: I'm an Android developer now (screenshot as proof).
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Chapter Summary

- Android Studio = the official free IDE; recommended 16GB RAM + 20GB disk + virtualization enabled
- Three essentials for a new project: name, package name (globally unique, never publish com.example), minimum SDK (API 26 or higher)
- Two ways to run: the emulator (a virtual phone on your computer) and a real device (enable USB debugging, remember to turn it off after)
- Project mantra: only touch the app/ folder — MainActivity.kt is the front door, the Manifest is the household registry, res/ is the resource warehouse
- The developer's daily loop = edit code → Run → check the result, over and over
:::
