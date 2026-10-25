---
id: di-wu-shi-er-zhang
num: 52
part: an-zhuo-kai-fa-pian
nav: Chapter 52: The Four Core Components and the Activity Lifecycle
toc: default
kind: chapter
---

### Chapter 52: The Four Components and the Activity Lifecycle

{class="chapter-intro mb-4"}
If Compose is an app's "face," then this chapter is about the app's "skeleton." Android has four basic components, and every app is assembled from them. The most important one, the Activity, has a "lifecycle diagram" that every Android developer must burn into memory. Once you finish this chapter, you'll finally understand age-old mysteries like "why did my app lose all its state after I switched away and came back?"

#### 1. The Four Components: Android's Pillars

Android officially defines four basic components, each responsible for one kind of job:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Component</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Job</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Think of it as</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activity</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A visible screen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The storefront — what users see and interact with</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Service</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The invisible workhorse doing jobs in the background</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A warehouse worker — playing music, downloading files; no screen needed</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BroadcastReceiver</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Receives system broadcasts</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The gatehouse — the loudspeaker for "battery low" and "network lost"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ContentProvider</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Shares data across apps</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A public filing cabinet — for example, sharing contacts with other apps</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Android's four components at a glance

As a beginner you'll spend 95% of your time working with the Activity. The Service and BroadcastReceiver come into play for things like music playback and push notifications, and the ContentProvider is used the least (the system has already wrapped the common data for you). One more thing: all four components must "register their household" in AndroidManifest.xml — if they're not registered, the system can't find them.

#### 2. The Activity Lifecycle: Your First Android "Treasure Map"

Apps on a phone can be interrupted at any moment: a call comes in, the user hops over to WeChat, the system runs short on memory and kills you... An Activity's whole life is a loop around this diagram:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onCreate (birth: initialization)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onStart (visible)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onResume (in the foreground, interacting)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onPause (partially covered)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onStop (fully hidden)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center">onDestroy (destroyed)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">🔁 onRestart / onStart / onResume: the same route in reverse when returning to the foreground</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figure 4: The Activity lifecycle (going forward: the top row is birth → the bottom row is exit; coming back retraces the same path)
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Callback</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">When it fires</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Typical use</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onCreate</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">When the Activity is created (once)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Load the UI, initialize data</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStart</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The screen becomes visible</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Start some lightweight logic</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onResume</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Has focus and can be interacted with</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Start animations, resume playback</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onPause</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Partly covered, or the moment the user switches away</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pause animations, save drafts</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStop</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fully invisible</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Release heavy resources, pause downloads</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onDestroy</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Before being destroyed</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Final cleanup</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Typical uses of the six lifecycle callbacks

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Watch out: rotating the screen "kills" the Activity

{class="mt-1"}
The most classic beginner fail: you rotate the screen and everything typed into the input fields is gone. Why? By default, rotating the screen destroys and recreates the Activity (running through onDestroy → onCreate). The fix: save state with rememberSaveable (the Compose replacement for remember); it automatically recovers the values when the Activity is rebuilt. You'll use it again and again in Chapters 6 and 7.
:::

#### 3. Intents: The "Tickets" for Traveling Inside and Outside the App

An Intent is the "ticket" components use to talk to each other. Whether you want to jump from one screen to another, open the browser, or launch the camera, you have to "buy a ticket and hop on":

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Navigating with Intent</span><span class="dots">···</span>
:::

```
// Method 1: explicit Intent — you name the exact destination screen
val intent = Intent(this, DetailActivity::class.java)
intent.putExtra("name", Alex)     // carrying "luggage" (data) along for the ride
startActivity(intent)

// Method 2: implicit Intent — you say what to do, the system finds who does it
val web = Intent(Intent.ACTION_VIEW, Uri.parse("https://developer.android.com"))
startActivity(web)   // the system opens a browser / or lets you choose
```
:::

Each kind has its own job: explicit intents are for jumping between screens inside your own app; implicit intents are for using the system's or other apps' abilities (opening a web page, making a call, sharing). In a Compose project, get the Context with LocalContext.current inside a Composable and you can call startActivity.

#### 4. Multiple Screens and Navigation

Real apps have more than one screen. The navigation solution officially recommended for Compose is Navigation Compose (the androidx.navigation library):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Navigation Compose skeleton</span><span class="dots">···</span>
:::

```
val navController = rememberNavController()

NavHost(navController, startDestination = "home") {
    composable("home") { HomeScreen(navController) }
    composable("detail/{name}") { entry ->
        val name = entry.arguments?.getString("name")
        DetailScreen(name ?: "Unknown")
    }
}

// Navigating from a screen:
navController.navigate("detail/Alex")     // with arguments
navController.popBackStack()              // go back
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tip: What if you have lots of screens?

{class="mt-1"}
As the project grows, keep all the screen routes together in one file (say, AppNavGraph.kt) and manage them in one place — don't let the "where do I go next" logic scatter across every screen. It's the first step from "it runs" to "it's maintainable."
:::

#### 5. A Quick Look: What Is a Fragment (and Why This Book Doesn't Teach It)

Digging through older tutorials, you'll definitely bump into Fragments — reusable pieces of UI embedded in an Activity, the absolute star of the old multi-screen architecture. But in the Compose era, Composable functions plus Navigation routes are all you need, and the official docs have downplayed Fragments. That's why this book leaves them off the main path.

My advice: don't reach for Fragments in new projects; just know they're "UI pieces embedded in an Activity" for when you read old code or get asked in an interview. For learning materials, always prefer anything from 2023 onward — Android's stack of "old almanacs" goes stale faster than you'd think.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Hands-on: Give the Counter a "Memory"

{class="mt-1"}
Upgrade the counter from Chapter 51: (1) swap remember for rememberSaveable and rotate the screen to confirm the number survives; (2) add an "About" button that uses Navigation to jump to a second screen showing the version number; (3) print logs (Log.d) in onCreate/onPause on both screens and watch the lifecycle call order in Logcat. Finish these three steps and the lifecycle stops being just theory.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Chapter Summary

- The four components: Activity (the storefront), Service (the background), BroadcastReceiver (the loudspeaker), ContentProvider (the filing cabinet)
- The six lifecycle callbacks: onCreate → onStart → onResume → onPause → onStop → onDestroy
- Rotating the screen destroys and recreates the Activity: use rememberSaveable to keep your state
- An Intent is a "ticket": explicit for your own screens, implicit for system abilities
- Multiple screens use Navigation Compose: NavHost + composable routes
:::
