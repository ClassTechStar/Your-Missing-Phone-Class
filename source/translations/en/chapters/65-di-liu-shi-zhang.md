---
id: di-liu-shi-zhang
num: 60
part: ios-kai-fa-pian
nav: Chapter 60: Setting Up Your Dev Environment — Xcode and Your First Project
toc: default
kind: chapter
---

### Chapter 60: Setting Up Your Development Environment—Xcode and Your First Project

{class="chapter-intro mb-4"}
A craftsman is only as good as their tools. In this chapter we'll set up the "kitchen": install Xcode, get the simulator running, create the first iOS project of your life, and then take the project structure apart so you understand every piece. Once the environment is ready, you'll see your own code turn into a button you can tap for the very first time—a moment many people remember for the rest of their lives.

#### 1. Getting a Mac Ready

First, the entry requirement: iOS development must happen on macOS. If you don't have a Mac, you have three options: buy one (even a used Mac mini or MacBook Air is enough), rent a cloud Mac for the short term, or read Part 8, "Hands-On Android Development," first (you can do that on Windows).

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Spec</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Minimum</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Comfort zone (recommended)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Chip</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Silicon (M1 or later)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">M2 or newer</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memory</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8GB</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">16GB</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Disk</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Reserve 40GB+ (Xcode itself is chunky)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256GB to start</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">System</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The latest macOS</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Keep auto-updates on</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Reference specs for a Mac development machine (August 2026)

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tip: You Can Start Learning the Language Without a Mac

{class="mt-1"}
The free Swift Playgrounds app on the iPad teaches the basics of the Swift language (no Mac needed); you can even install it on the iPhone. Get comfortable with the Chapter 61 language material in Playgrounds first, and you'll take off the moment you get a Mac. This is the classic "sharpen the axe before you chop" principle.
:::

#### 2. Installing Xcode

Xcode is Apple's official integrated development environment, and it's free. Three steps to install:

1. On your Mac, open the App Store, search for "Xcode," and click Install—heads up, it's several GB, so pick a time when your connection is fast;
2. On first launch after installing, accept the agreement and let the components install (it happens automatically);
3. In the menu bar, go to Xcode > Settings > Locations and make sure Command Line Tools is selected—the command line tools are a prerequisite for many scripts and third-party tools.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Note: The Version and System "Matching Game"

{class="mt-1"}
A new Xcode usually demands the latest macOS, while older Macs get stuck on older versions. When you publish to the App Store, Apple requires building with a relatively recent Xcode (usually with a grace period). So don't put off system updates too long—iOS developers are among the busiest "new version chasers" out there.
:::

#### 3. Creating Your First Project

Open Xcode > Create New Project > choose iOS > the App template, then fill in:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Setting</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">What to enter</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Description</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Product Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstApp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">App name</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Your Apple ID (free)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Used for signing; a personal account is fine</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Organization Identifier</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Combined with the Product Name to form the bundle identifier</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interface</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The main framework used in this book</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Language</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">No explanation needed</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
The five things to fill in when creating a project

After you click Create, Xcode generates a project that runs right away. Pick a simulator in the top-left corner (say, iPhone 17) and click ▶ to run—a few seconds later, a window saying "Hello, world!" appears on the simulator's screen. Your first iOS app has been born.

#### 4. Project Structure, Dissected: What Each File Does

On the left is the project navigator—as a beginner, you only need to know these:

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="290" viewBox="0 0 600 290" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="290" fill="#fafafa" rx="8"/>
      <text x="20" y="28" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ project root</text>
      <rect x="30" y="42" width="540" height="225" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <rect x="45" y="56" width="250" height="196" fill="#eef2ff" rx="5"/>
      <text x="56" y="78" font-size="11" fill="#1e1b4b" font-weight="bold">MyFirstApp/ (code folder)</text>
      <text x="66" y="100" font-size="10" fill="#374151">├ MyFirstAppApp.swift  ← app entry point</text>
      <text x="66" y="120" font-size="10" fill="#374151">├ ContentView.swift  ← main screen</text>
      <text x="66" y="140" font-size="10" fill="#374151">└ Assets.xcassets  ← icons, images, colors</text>
      <text x="56" y="166" font-size="10" fill="#6b7280">(new files all go in this folder)</text>
      <text x="56" y="196" font-size="10" fill="#1e1b4b" font-weight="bold">Info tab / Info.plist</text>
      <text x="66" y="216" font-size="10" fill="#6b7280">App declarations: name, permissions, settings</text>
      <rect x="310" y="56" width="245" height="196" fill="#f0fdf4" rx="5"/>
      <text x="321" y="78" font-size="11" fill="#065f46" font-weight="bold">Other key places</text>
      <text x="331" y="100" font-size="10" fill="#374151">📁 Preview Content/  ← preview assets</text>
      <text x="331" y="122" font-size="10" fill="#374151"><i class="fas fa-bullseye mr-1"></i> Target settings (the blue project icon)</text>
      <text x="331" y="142" font-size="10" fill="#6b7280">— version number, minimum OS, signing are all here</text>
      <text x="331" y="168" font-size="10" fill="#374151"><i class="fas fa-flask mr-1"></i> MyFirstAppTests/  ← unit tests</text>
      <text x="331" y="188" font-size="10" fill="#374151">📱 MyFirstAppUITests/ ← UI tests</text>
      <text x="331" y="216" font-size="10" fill="#9ca3af">(test templates are already generated; used in Chapter 67)</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figure 2: The Xcode project structure every beginner must know
:::

- MyFirstAppApp.swift: the program's entry point. In SwiftUI it's only a few lines—"launch, then show the main screen";
- ContentView.swift: the main screen view—everything you're looking at right now lives here;
- Assets.xcassets: the resource warehouse—icons, images, and colors all go here;
- Target settings: click the blue project icon on the left to get in. The version number, the minimum iOS version, and signing are all in there. The app's display name and icon are configured here too.

#### 5. Xcode Efficiency Tricks: Five "Shortcut Power-Ups" for Beginners

Get fluent with these and you'll look "very professional":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Action</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Shortcut</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">What it does</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Run</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Build and run</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Open/toggle the canvas preview</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The what-you-see-is-what-you-get switch</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Re-indent</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Automatically tidy up the indentation of the selected code</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Quick Open</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Type a file name and it opens instantly (the most used!)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Comment/uncomment</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Switch code on and off while debugging</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
High-frequency Xcode shortcuts (the beginner's five)

Two more hidden perks: multiple simulators at once (run an iPhone and an iPad side by side to compare layouts) and the snippet library (drag a few lines of frequently used code into the Snippets panel on the right, then insert them with one click next time)—use these efficiency tools early, and the fluency will follow naturally.

#### 6. Testing on a Real Device: Install the App on Your iPhone

The simulator is nice, but a real device is the destination. You can test on a real device even with a free Apple ID:

1. Connect your iPhone with a cable (or debug wirelessly over the same Wi-Fi);
2. Pick your phone from the device list at the top of Xcode; the first time, you'll be asked to sign in with your Apple ID and signing gets configured automatically;
3. On the iPhone, go to [Settings] > [General] > [VPN & Device Management] and trust your developer certificate;
4. Click ▶, and the app lands on your real device.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Note: The Free Account's "Seven-Day Limit"

{class="mt-1"}
An app signed with a free Apple ID stops working after 7 days (just run it again to renew). This is Apple's anti-abuse mechanism, and it's completely fine for the learning stage; a paid developer account ($99/year) has no such limit—Chapter 67 has the details.
:::

#### 7. Try It Yourself + First Aid for Common Errors

Open ContentView.swift, change the text inside Text("Hello, world!") to your name, and press ⌘R to run again—a few seconds later, your name shows up on the simulator. Congratulations: you've completed your first full "edit code → build → install → run" loop.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Symptom</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Common cause</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">The fix</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Signing error</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">No Team selected, or an expired certificate</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">In Target > Signing, check your account; with a free account, just run again</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Simulator shows a black screen / won't open</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Corrupted simulator image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menu: Device > Erase All Content; or delete the simulator and add it again</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode downloads slowly / won't install</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">App Store network hiccup</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Try a different time of day; or download the .xip offline installer from the Apple developer website</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
First-aid table for beginner environment errors

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Hands-on: Finish Your "Developer Initiation" Checklist

{class="mt-1"}
1) Install Xcode and get the simulator running; 2) run your app on a real device once and take a screenshot to mark the occasion; 3) change the Hello text to your name; 4) go to the Target settings and change the app's display name to "My First App." Once these four steps are done, you're officially someone with a creation of your own.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Chapter summary

- Hard requirements: a Mac + Xcode; no Mac yet? Learn the language first with Swift Playgrounds on the iPad
- Install Xcode from the App Store; new versions demand new systems, so don't put off updates
- The five essentials of a new project: name, Team, organization identifier, SwiftUI, Swift
- The project mantra: all your code lives in the MyFirstApp/ folder; Target settings manage the version and signing
- Real-device testing with a free Apple ID has a 7-day signing limit; a paid account has no such limit
- The developer's daily routine = edit code → ⌘R → see the result, over and over
:::
