---
id: di-liu-shi-ba-zhang
num: 68
part: ios-kai-fa-pian
nav: Chapter 68: Leveling Up — Permissions, Notifications, and Modern Architecture
toc: default
kind: chapter
---

### Chapter 68: The Road Ahead—Permissions, Notifications, and Modern Architecture

{class="chapter-intro mb-4"}
Being able to build an app is only the start. This chapter is about the hurdles between "can build" and "builds well": how to ask for permissions gracefully, how to send notifications without being annoying, how to lift your architecture another level, and—here in 2026—how to team up with AI to write iOS code. Every item is something you'll run into right away in a real project.

#### 1. Permissions: knock before you enter

Camera, location, contacts, notifications... for these "sensitive zones," iOS requires the app to show a prompt asking the user at the moment of use. The rule is three steps: "declare + ask + degrade gracefully":

::: div .code-block
:::inline div .code-head
<span>SWIFT · Requesting permissions (location example)</span><span class="dots">···</span>
:::

```
// 1. Declare the usage text in Info.plist (without it, instant crash!)
// Privacy - Location When In Use Usage Description: "Used to look up the weather in your city"

// 2. Request it when you need it
import CoreLocation

@Observable
class LocationModel {
    private let manager = CLLocationManager()

    func request() {
        switch manager.authorizationStatus {
        case .notDetermined: manager.requestWhenInUseAuthorization()
        case .denied, .restricted: /* guide the user to Settings */
        default: /* already granted, go ahead */
        }
    }
}

// 3. Degrade gracefully after denial: show a hint + open Settings
// UIApplication.shared.open(URL(string: UIApplication.openSettingsURLString)!)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Note: iOS permissions are "one-shot"

{class="mt-1"}
The iOS permission prompt appears only once—once the user declines, it never pops up again. So: time the request for "the exact moment the user is about to use the feature" (not a pile of prompts at launch), and write the copy so it explains the purpose. Post-denial guidance ("go to Settings and turn on location") is standard equipment—don't leave users stuck in a dead end.
:::

#### 2. Notifications: say something useful at the right time

Notifications are the channel apps use to reach users, and also the feature most easily "blocked" by them. iOS uses the UserNotifications framework. Three rules for notifications: only send what's useful, let users turn them off, and never pester people in the middle of the night. Basic usage:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Local notifications</span><span class="dots">···</span>
:::

```
import UserNotifications

// 1. Request notification permission (one-time dialog)
UNUserNotificationCenter.current()
    .requestAuthorization(options: [.alert, .sound, .badge]) { granted, _ in
        print(granted ? "granted" : "denied")
    }

// 2. Schedule a "daily 20:00 expense reminder"
func scheduleDailyReminder() {
    let content = UNMutableNotificationContent()
    content.title = "Expense reminder"
    content.body = "You haven't recorded today's expenses yet"
    content.sound = .default

    var comps = DateComponents()
    comps.hour = 20
    let trigger = UNCalendarNotificationTrigger(dateMatching: comps, repeats: true)

    let request = UNNotificationRequest(
        identifier: "daily-reminder",
        content: content,
        trigger: trigger
    )
    UNUserNotificationCenter.current().add(request)
}
```
:::

Note: the iOS notification permission is also "one prompt only," and users can switch it off anytime in system settings—so the sense of value in each notification matters a lot. One spam blast can lose a user forever.

#### 3. Architecture, going deeper: MVVM and testability

Chapter 65 used MVVM; here are three advanced points to add:

- Protocol abstraction: make the ViewModel depend on a protocol rather than a concrete class—then tests can inject a "fake data source." This is the cornerstone of testability;
- Single responsibility: one ViewModel handles one thing only (the expense-tracking one doesn't handle weather); when features grow, split it up;
- Don't over-engineer: for a solo small project, "an @Observable class + protocol abstraction" is plenty. Heavy architectures like VIPER or Clean Architecture can wait until team size and complexity come knocking—tools serve the goal; they're not for showing off.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tip: SwiftUI's "ecosystem dividend"

{class="mt-1"}
The iOS ecosystem has two more "only-here" advanced tricks: widgets (WidgetKit) let users see information without opening the app (put the expense tracker's "spending this month" on the home screen), and Shortcuts (App Intents) let users invoke your features through Siri or automations. Both have official frameworks and are cheap to learn, yet they massively boost the user experience—worth unlocking early on the road to mastery.
:::

#### 4. The 2026 twist: AI-assisted iOS development

By 2026, AI is deeply embedded in Apple's development workflow. If you want to speed up, this combo is mature:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Stage</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">How AI helps</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Your responsibility</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Writing code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode's built-in code completion + third-party AI plugins generate it</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Describe requirements clearly, review the output</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Looking things up</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hand official docs and error messages to AI to interpret</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Verify key conclusions against the official docs</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Writing tests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Have AI generate XCTest cases in the "normal/boundary/exception" categories</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Confirm the cases match the business meaning</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fixing bugs</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Paste the crash log + relevant code, and AI locates and fixes it</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Understand the changes, run tests to verify</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Four scenarios for AI-assisted iOS development

For the full methodology—how to give AI instructions, how to review its work, how to avoid pitfalls—the complete 11 chapters are in Part 7 of this book, "Hands-On AI Coding" (Chapters 37–47), which I strongly recommend reading alongside this one: leave the Swift syntax to this part, and the art of working with AI to Part 7.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Get hands-on: add the "power trio" to the expense tracker

#### 5. Swift concurrency essentials: @MainActor and Task

Swift 6's concurrency system has two rules every beginner must understand:

- The UI can only be updated on the main thread: SwiftUI views are @MainActor by default, so bring network callbacks back to the main thread before changing state (await MainActor.run { ... }, or mark the ViewModel @MainActor);
- Manage async work with Task: the .task { } modifier starts automatically when the view appears and cancels automatically when it disappears—that's the standard way to kick off async work in SwiftUI; don't scatter raw Tasks in body.

::: div .code-block
:::inline div .code-head
<span>SWIFT · The standard async pattern</span><span class="dots">···</span>
:::

```
struct WeatherScreen: View {
    @State private var vm = WeatherViewModel()

    var body: some View {
        Group {
            switch vm.state {
            case .loading: ProgressView()
            case .success(let d): WeatherContent(data: d)
            case .error(let m): Text(m)
            }
        }
        .task {                       // starts when it appears, cancels when it disappears
            await vm.search(city: "Beijing")
        }
    }
}
```
:::

Behind these two rules is Swift 6's "data-race safety" design—the compiler errors out the moment you get it wrong, instead of waiting for the app to crash to find out. The compiler's errors aren't nitpicking; they're taking a bullet for you.

{class="mt-1"}
① Add a "daily 8:00 PM expense reminder" to the tracker (notification permission + local notifications); ② switch the ViewModel's data source to a protocol abstraction and write a unit test that injects fake data; ③ add a "spending this month" home-screen widget. Finish the trio and your project starts to look like a regular army.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Chapter summary

- Permissions in three steps: declare in Info.plist (miss it and it crashes), ask at the moment of use, guide to Settings when denied
- iOS permission prompts appear only once: pick the timing of "the moment they're about to use it," and write the purpose clearly
- Three rules for notifications: only send useful ones, let users turn them off, don't pester; UserNotifications framework
- MVVM advanced: protocol abstraction (testable), single responsibility, no over-engineering
- Ecosystem dividends: WidgetKit widgets + App Intents Shortcuts
- Four AI-assisted scenarios: writing code, research, writing tests, fixing bugs; methodology in Part 7 (Chapters 37–47)
:::
