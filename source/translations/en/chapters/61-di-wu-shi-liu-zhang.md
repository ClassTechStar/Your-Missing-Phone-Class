---
id: di-wu-shi-liu-zhang
num: 56
part: an-zhuo-kai-fa-pian
nav: Chapter 56: Polish and Publish — Launching on Google Play
toc: default
kind: chapter
---

### Chapter 56: Polish and Release — Testing, Debugging, and Publishing on Google Play

{class="chapter-intro mb-4"}
The app is built — now what? This chapter covers the three things that take you from "it runs" to "it ships": how to debug efficiently to find bugs, how to write tests to prevent regressions, and how to put the app on Google Play for the whole world to download. Publishing isn't just ceremony — it's the dividing line between a finished work and a product.

#### 1. The Three Debugging Tools: Logcat, Breakpoints, and the UI Inspector

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tool</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">What it does</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">How to use it</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logcat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">View system and your own logs</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">In code: Log.d("TAG","value=$x"); filter by searching TAG in the panel</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Breakpoint debugging</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pause the program at a line and inspect variable values</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Click next to the line number to drop a red dot, run in Debug mode, and step through</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Layout Inspector</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Inspect the live UI structure</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menu Tools → Layout Inspector; watch the component tree in real time</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
The three debugging tools

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tip: how do you read an error?

{class="mt-1"}
After a crash, Logcat shows a red stack trace. Scan from the bottom up for the first line that starts with your own package name (e.g., com.example.yourapp) — that line is basically the crime scene. First check the "Exception type" (a null pointer? a bad cast?), then the "at ... yourfile:line". This one trick solves 80% of crashes.
:::

#### 2. Testing: Insuring Your Code

Manual testing can't be trusted — fix one feature and another quietly breaks. Tests are both "regret medicine" and a "bulletproof vest." Android testing comes in three layers; as a beginner, master the first one first:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Layer</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">What it tests</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Where it lives</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Speed</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Unit tests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pure logic (calculations, validation)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/test/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Seconds</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Instrumented tests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UI behavior on a real device</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/androidTest/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minutes</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Manual testing</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A real human feeling out the experience</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Always needed</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
The three testing layers

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Unit test example</span><span class="dots">···</span>
:::

```
// Extract logic like "amount string to number" into a pure function
fun parseAmount(input: String): Double? {
    val v = input.trim().toDoubleOrNull()
    return if (v != null && v > 0) v else null
}

// Testing it (JUnit4)
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

The amount validation and summary calculations in the tracker should all be covered by unit tests. To run them: right-click the test directory → Run. Green across the board means you can change code with confidence.

#### 3. Signing and Packaging: Stamping Your App

Android requires every installable package to be signed — like an official seal proving "this package came from me and hasn't been tampered with." While debugging, Android Studio signs automatically with the debug key; for release you use your own release signature. The process:

1. Menu Build → Generate Signed Bundle / APK;
2. Create the keystore file — set a password and keep it safe;
3. Choose release + the AAB format, and the build is done.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Watch out: losing the keystore = losing the app

{class="mt-1"}
Updates after publishing must use the same signature, or the store will reject the update. If the keystore file and password are lost, your only option is to publish as a brand-new app — none of your existing users can come along. Back up the keystore and password somewhere secure (encrypted cloud storage + a notebook). It's one of the most expensive lessons an Android developer can learn.
:::

#### 4. The Full Google Play Publishing Process

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Register a developer account</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> Prepare store assets</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> Upload the AAB</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> Fill in the data-safety form</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Review (hours to days)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> Published</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figure 6: The six steps to publishing on Google Play
:::

- Register: a one-time $25 registration fee; you need a working Google account;
- Assets: an app icon (512×512), screenshots (at least 2), a feature description, and a privacy policy link (required if you collect data);
- Data safety form: honestly declare what data you collect — an offline expense tracker can declare "zero collection";
- Review: a new account's first submission is often reviewed by a human, taking anywhere from hours to days; if it's rejected, fix things per the feedback.

A note for users in mainland China: Google Play requires special network access, and distribution in mainland China usually goes through domestic stores (Huawei, Xiaomi, Tencent MyApp, etc.). Publishing to domestic stores is a similar process, but each store has its own review quirks — the same AAB/APK can be distributed to several stores. As practice, getting through just one store is already a win.

#### 5. Making Store Assets: First Impressions Are Downloads

The store page is the shop window users see while browsing. Three assets decide the first impression:

- Icon: 512×512; don't just make do with a screenshot. If design isn't your thing, use an AI tool to generate a clean geometric shape — it only counts if it's still recognizable at home-screen size;
- Screenshots: at least 2, ideally 4-6, showing your most core feature scenes; pair each with one line of plain speech ("Log an expense in a second" is ten times better than "An efficient expense-tracking solution");
- Description: the first sentence should make clear "what this is + who it's for"; don't pile up "most professional, most powerful" — store search ranking depends mainly on keywords and download conversion, and honesty works better than exaggeration.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tip: A/B against your peers

{class="mt-1"}
Before publishing, browse the top ten apps in your category and screenshot them for comparison: what style are their icons? What selling points do their screenshots push? How are their titles written? Imitating isn't copying — learn the playbook and swap in your own content. It's the fastest cold-start lesson in every product's life.
:::

#### 6. A quick checklist for performance and crash reporting

Before publishing, these two things are each worth half an hour:

##### 1. Four performance self-checks

1. Use LazyColumn for lists: never lay out long lists with a plain Column — lazy loading is Android performance lesson one;
2. Don't shove full-size images in: use the Coil image library to auto-scale and cache; a single 5MB original is enough to choke a low-end phone;
3. Keep heavy work off the main thread: database, network, and large files all belong in coroutines;
4. Measure with the Profiler: Android Studio's built-in profiler shows memory, CPU, and battery use — measure first, then optimize; don't go by feel.

##### 2. Crash reporting

Not crashing during your tests doesn't mean it won't crash on users' phones. Before publishing, add Firebase Crashlytics (Google's official, free tool): a few lines of config, and when a user hits a crash it automatically reports the stack trace, so from the console you can see "which device model, which version, and which line it crashed on." Publishing without crash monitoring is driving with your eyes closed.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Hands-on: "deliver" the tracker once

{class="mt-1"}
(1) Add 3 unit tests for logic like parseAmount; (2) use Logcat to catch a crash you created on purpose and fix it; (3) generate a release-signed APK and send it to a friend to install (that's the real "finished work" ceremony); (4) if you have energy to spare, register a developer account and actually submit the tracker for publication. The first three can be done tonight.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Chapter Summary

- The three debugging tools: Logcat for logs, breakpoints for variables, Layout Inspector for the UI
- Reading crashes: scan the stack from the bottom up for the first line with your package name
- Three testing layers: unit (seconds — learn this first) / instrumented / manual
- Publishing requires signing: back up the keystore and password; lose them and the app "changes identity"
- Six publishing steps: register → assets → upload the AAB → data safety form → review → live
:::
