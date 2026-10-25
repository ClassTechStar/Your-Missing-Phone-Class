---
id: di-si-shi-ba-zhang
num: 48
part: an-zhuo-kai-fa-pian
nav: Chapter 48: Meet Android — From Operating System to Developer Ecosystem
toc: default
kind: chapter
---

### Chapter 48: Getting to Know Android — From Operating System to Development Ecosystem

{class="chapter-intro mb-4"}
Congratulations on making this decision — going from "someone who plays with phones" to "someone who makes phone apps." Before we start, let's spread out the map: where did Android come from? Why are developers all over the world writing apps for it? And from the moment your fingers hit the keyboard to when an app lands on a user's phone, what happens in between?

#### I. Android's Origin Story: From "Little Robot" to "The World's Biggest System"

Android's story begins in 2003 — an engineer named Andy Rubin founded Android Inc., with a modest goal: build a smart operating system that "understood cameras better." Google acquired it in 2005, and in 2007 joined dozens of manufacturers to form the Open Handset Alliance (OHA). In September 2008, the first Android phone, the HTC Dream (G1), went on sale.

You know the rest of the story: by 2026, Android is the world's largest mobile operating system by market share, with active devices in the billions. Your phone, TV box, car dashboard screen, and smartwatch are very likely all running Android. What does that mean? It means every line of code you write has a chance to be used by the largest number of people on Earth.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tip: Android's Open-Source DNA

{class="mt-1"}
Android's core code (AOSP, the Android Open Source Project) is open source — any manufacturer can take it and customize it. That's why Xiaomi has MIUI (now called HyperOS), Huawei has its HarmonyOS compatibility layer, and Samsung has One UI. That's good news for developers: what you learn is "Android development," not "development for one brand" — one skill set that works on every device.
:::

The version numbers are fun too: starting with 1.5 Cupcake, every major release was named after a dessert — Donut, Eclair, Froyo, Gingerbread... until Android 10 in 2019 switched to plain numbers. As of August 2026, the latest official release is Android 17, and the "minimum supported version" you actually need to care about in development is usually set by mainstream apps somewhere between Android 8 (API 26) and Android 10 (API 29) — support devices from a few years back and your potential user base is big enough.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Version</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Codename / Year</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">What Matters for Developers</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 8 (API 26)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Oreo · 2017</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Notification channels and background limits — the minimum line for many older devices</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 10 (API 29)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2019</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Scoped storage arrives; the rules for file access get a major overhaul</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 12 (API 31)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2021</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Material You dynamic color; a big upgrade in look and feel</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 13 (API 33)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2022</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Runtime notification permission — a popup asks whether to allow notifications</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 14-15 (API 34-35)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2023-2024</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Predictive back, 16KB pages, privacy tightened further</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 16-17 (API 36-37)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2025-2026</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Faster minor-release cadence, AI capability integration (like Gemini extensions)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
A Brief History of Android Versions (as of August 2026 — key items for development)

#### II. Which Language to Write In: Java or Kotlin?

Two mainstream languages have appeared over Android's history. Java is the "founding elder" — Android used it from day one. Kotlin was named a "first-class citizen" by Google in 2017, and from 2019 the official stance has been "Kotlin-first." By 2026, nearly all new projects use Kotlin, and most older projects are gradually migrating too.

Let's be honest: if you're a complete beginner, learn Kotlin directly and don't look back at Java. Three reasons: first, Kotlin takes 30%-40% less code than Java (same features, shorter and clearer); second, it's natively protected against "null pointers," a beginner's nightmare; third, all modern tutorials, official docs, and AI coding tools (remember our AI coding book?) are Kotlin-based. You'll only run into Java when maintaining old projects or reading old code.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Java style (the wordy version)

{class="font-mono text-xs leading-relaxed"}
public class MainActivity extends Activity {<br>&nbsp;&nbsp;@Override<br>&nbsp;&nbsp;protected void onCreate(Bundle b) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b);<br>&nbsp;&nbsp;&nbsp;&nbsp; setContentView(R.layout.activity);<br>&nbsp;&nbsp;}<br>}
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Kotlin style (the clean version)

{class="font-mono text-xs leading-relaxed"}
class MainActivity : ComponentActivity() {<br>&nbsp;&nbsp;override fun onCreate(b: Bundle?) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b)<br>&nbsp;&nbsp;&nbsp;&nbsp;setContent { App() }<br>&nbsp;&nbsp;}<br>}
:::
:::

Same task, but Kotlin drops a pile of curly braces and boilerplate. We'll learn it properly in Chapter 50; for now you only need to remember: the "common language" of Android development is called Kotlin.

#### III. How Is an App Born?

Many people think "developing an app" means opening the computer and furiously writing code. In reality, an app goes through roughly this pipeline from idea to a user's phone:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-lightbulb mr-1"></i> Idea</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center">📐 Design (UI + features)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-keyboard mr-1"></i> Write code</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hammer mr-1"></i> Compile and package (APK/AAB)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Test (emulator + real device)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-rocket mr-1"></i> Release (store/installer)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figure 1: The full journey of an Android app from idea to the store
:::

Two concepts from this pipeline you need to know right now:

- APK: the installation package format for Android apps (.apk). Like a Windows .exe, it installs onto a phone with a tap. Use it for your own testing or for sharing with friends to try.
- AAB: Android App Bundle (.aab), the "advanced packaging format" used to publish on Google Play. The store dynamically trims the package to match each user's phone model, so everyone downloads a smaller file. You can't install it yourself — it only goes through the store.

Another term you'll hear constantly: SDK (Software Development Kit). It's the full set of "development gear" provided officially by Android — the API libraries for each version, debugging tools, emulator images, and more. Classes like Activity and Button that you call in your code all come from the SDK.

#### IV. The Android Tech Stack at a Glance: Your "Weapon List"

Before we formally start learning, meet the standard configuration of a mainstream Android project in 2026 — it's fine if this list makes no sense yet; come back after you finish the book and it will all click:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Layer</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Mainstream Choice (2026)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">What It's For</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Language</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin 2.x</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The language for writing logic</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jetpack Compose + Material 3</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Draws the UI in code (the main thread of this book)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Architecture</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MVVM + ViewModel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Keeps UI and logic separate so the code stays tidy</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Data Storage</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room (database) + DataStore (settings)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Saves data on the phone</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Networking</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit + OkHttp + Kotlin coroutines</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Talks to the server</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Build Tool</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle + Kotlin DSL</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Turns code into an installable package</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Development Environment</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Google's official all-in-one IDE</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
The Mainstream Android Tech Stack of 2026 at a Glance

Don't be intimidated by all that English. These are just the pots and pans in the kitchen — right now you only need to know that "cooking means entering the kitchen"; how each tool works will be unpacked for you chapter by chapter. And here's the good news: when Android Studio creates a new project, it sets up this whole stack for you automatically. You just get cooking.

#### V. Android vs. iOS: A Developer's First Lesson in Choosing Sides

You may be holding an Android device and an Apple device at the same time. As a developer, the differences in experience between the two sides are worth knowing up front — this isn't about taking sides on "which is better," it's the practical math of "which side suits your start":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dimension</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Android Development</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">iOS Development</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Development Computer</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Windows / Mac / Linux all work</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Must be a Mac (Xcode is exclusive)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Development Tool</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio (free)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode (free) + $99/year to publish</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Store Review</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lenient; a few hours to a few days</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Strict; 1-7 days is the norm</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">On-Device Testing</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">APKs can be shared and installed freely</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Distribution is restricted; testing requires signing/TestFlight</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Revenue Environment</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mainly ads and domestic channels</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">App Store users have better in-app purchase habits</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Learning Cost</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">More concepts to learn (the four major components, etc.)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Closed ecosystem, but unified and superbly documented</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Android vs. iOS Development Paths (August 2026)

Let's be honest: if your computer isn't a Mac, this question answers itself — Android is the only option. If you do have a Mac, you can read Parts Eight and Nine of this book side by side; the programming mindset transfers, and learning the second side after the first is much faster.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Hands-On: Look at the "Android" in Your Phone

{class="mt-1"}
Open [Settings] > [About phone] (or "About device") on your phone and find the "Android version" row — tap it several times in a row and you'll trigger the system's hidden Easter-egg game. Note your version number and check it against the version table above to see which generation it belongs to. Your phone is your very first "development test device."
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Chapter Summary

- Android was born in 2008; by 2026 it's the world's largest mobile system by market share, with billions of active devices
- The latest official release is Android 17; mainstream apps support Android 8-10 at minimum, so the user base stays big
- New projects all use Kotlin: 30%+ less code, null-pointer protection, officially endorsed
- APK for installing yourself, AAB for the store; the SDK is the official development gear kit
- The standard 2026 stack: Kotlin + Compose + MVVM + Room + Retrofit + Gradle + Android Studio
:::
