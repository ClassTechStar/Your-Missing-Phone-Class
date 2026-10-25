---
id: di-wu-shi-qi-zhang
num: 57
part: an-zhuo-kai-fa-pian
nav: Chapter 57: Leveling Up — Permissions, Notifications, and Modern Architecture
toc: default
kind: chapter
---

### Chapter 57: The Road Ahead — Permissions, Notifications, and Modern Architecture

{class="chapter-intro mb-4"}
Being able to build an app is only the start. This chapter covers the hurdles between "can build" and "builds well": how to ask for permissions gracefully, how to send notifications without annoying people, how to lift your architecture another level, and — in 2026 — how to pair with AI to write Android code. Every one of these will show up in your real projects right away.

#### 1. Runtime Permissions: Knock First, Then Come In

Camera, location, contacts, notifications... for these "sensitive zones," Android requires the app to ask the user at runtime (Android 6 and up). The rules: declare first (the Manifest), then request (in code), and degrade gracefully if the user refuses. In Compose, the easiest path is rememberPermissionState from the official Accompanist library:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Runtime permissions (Compose edition)</span><span class="dots">···</span>
:::

```
// First declare it in the Manifest:
// &lt;uses-permission android:name="android.permission.CAMERA" /&gt;

@Composable
fun CameraButton() {
    val permission = rememberPermissionState(
        permission = android.Manifest.permission.CAMERA
    )
    Button(onClick = {
        when {
            permission.status.isGranted -&gt; openCamera()
            permission.status.shouldShowRationale -&gt; showExplainDialog()
            else -&gt; permission.launchPermissionRequest()
        }
    }) { Text("Take photo") }
}
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Note: what if you're permanently denied?

{class="mt-1"}
Once the user checks "don't ask again," launchPermissionRequest won't pop up anymore. At that point, guide them to turn it on manually in system settings (jump to the app's settings page with an Intent), and explain in the UI "what this permission is for." A kinder tone makes users far more willing to grant it — the words you use in a permission request are worth writing carefully.
:::

#### 2. Notifications: Saying Useful Things at the Right Time

Notifications are the channel apps use to reach users — and the feature users block first. Three disciplines for notifications: only send useful things, let users turn them off, and never pester at midnight. The basic usage:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Sending a notification</span><span class="dots">···</span>
:::

```
// On Android 13+ you must request POST_NOTIFICATIONS first (see the previous section)

// 1. Create the notification channel (required on Android 8+)
val channel = NotificationChannel(
    "reminder", "Reminder", NotificationManager.IMPORTANCE_DEFAULT
)
val manager = getSystemService(NotificationManager::class.java)
manager.createNotificationChannel(channel)

// 2. Send the notification
val notification = NotificationCompat.Builder(this, "reminder")
    .setSmallIcon(R.drawable.ic_notification)
    .setContentTitle("Expense reminder")
    .setContentText("You haven't recorded today's expenses yet")
    .setPriority(NotificationCompat.PRIORITY_DEFAULT)
    .build()
if (ActivityCompat.checkSelfPermission(this,
        Manifest.permission.POST_NOTIFICATIONS) == PackageManager.PERMISSION_GRANTED
) {
    manager.notify(1, notification)
}
```
:::

For scheduled tasks (like "remind me to log expenses at 20:00 every day"), use WorkManager — the officially recommended "background scheduling butler" that guarantees tasks run at the right moment, with no need to fuss over battery optimization yourself. For alarm-type needs, it's always the right choice.

#### 3. Architecture, Next Level: Dependency Injection and Modularity

As the project grows, two "sweet troubles" come knocking:

- Messy object creation: every screen builds its own database, its own API — use Hilt (a dependency injection framework) to manage them centrally, so "whoever needs something just asks and it's handed over";
- Code piling into a mountain: single-module projects get slower and slower to change — split into multiple modules (app / core / feature-xxx) so each feature is developed and tested independently.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tip: don't over-engineer

{class="mt-1"}
Hilt and modularity are both good tools, but don't rush them into a solo project. For the tracker, a single module plus manual dependency creation is entirely enough. Bring them in when the code passes tens of thousands of lines, compilation starts to slow down, or several people begin collaborating — and only as needed. Tools serve goals; they're not for showing off — that's also the "simplicity first" principle from our AI coding book.
:::

#### 4. The 2026 Way: AI-Assisted Android Development

In 2026, AI is deeply embedded in the Android development workflow. If you want to speed up, this combination is well proven:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Stage</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">How AI helps</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Your responsibility</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Writing code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gemini built into Android Studio / third-party AI plugins for completion and generation</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Describe requirements clearly; review the output</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Looking things up</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Feed official docs and error messages to AI for interpretation</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Verify key conclusions against the official docs</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Writing tests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Have AI generate cases in the three categories "normal/edge/exception"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Confirm the cases match the intended behavior</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fixing bugs</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Paste the stack trace + relevant code; AI locates and fixes</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Understand the change; run tests to verify</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Four scenarios for AI-assisted Android development

The full methodology — how to give AI instructions, how to review its work, how to avoid pitfalls — spans 11 complete chapters in Part 7 of this book, "AI Coding in Practice" (Chapters 37-47), which I strongly recommend reading alongside: leave the Android syntax to this part, and the AI collaboration know-how to Part 7.

#### 5. Compose Performance Tuning and Debugging Tools

Writing Compose is a joy, but "too much recomposition" can also lag. Three practical techniques:

- Stabilize parameters: add @Immutable to data classes or use derivedStateOf to keep unrelated state changes from triggering large recompositions;
- Remember to use keys: items(list, key = { it.id }) makes list additions and deletions touch only the items that should change — without a key, deleting one item may redraw the whole list;
- Layout Inspector's Compose mode: watch each Composable's recomposition count in real time — you can see at a glance who recomposes too often, and optimize those hotspots.

Also turn on the Compose compiler reports (metrics) to generate a report of "which components are unstable" — on the road to mastery, data is always more reliable than gut feeling.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Hands-on: add the "trio" to the tracker

{class="mt-1"}
(1) Add a "remind me to log expenses at 20:00 every day" feature to the tracker (WorkManager + a notification channel + the Android 13 notification permission); (2) switch the database and API creation to Hilt injection; (3) try using an AI tool to speed-build the "monthly filter" feature, then check its output with the three-layer acceptance method. Finish all three and your project starts to look like a proper, professional operation.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Chapter Summary

- Sensitive permissions: declare in the Manifest + request at runtime + guide gracefully after a refusal
- Three notification disciplines: only useful things, can be turned off, no pestering; channel + permission, both required
- Use WorkManager for scheduled tasks; don't reinvent the wheel
- Hilt manages objects, modularity manages code — hold off on both for small solo projects
- Four AI-assisted scenarios: writing code, research, writing tests, fixing bugs; the methodology is in Part 7 (Chapters 37-47)
:::
