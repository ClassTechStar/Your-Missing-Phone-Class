---
id: di-liu-shi-qi-zhang
num: 67
part: ios-kai-fa-pian
nav: Chapter 67: Polish and Publish — Launching on the App Store
toc: default
kind: chapter
---

### Chapter 67: Polish and Ship—Testing, Debugging, and the App Store

{class="chapter-intro mb-4"}
The app works—now what? This chapter covers the three things on the road from "it runs" to "it's deliverable": how to debug efficiently to find bugs, how to write tests to prevent regressions, and how to get your app onto the App Store for the whole world to download. Shipping isn't just ceremony—it's the dividing line between a project and a product.

#### 1. The three debugging essentials: print, breakpoints, and previews

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tool</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">What it does</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">How to use it</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">print + console</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">View run logs</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">In code: print("value = \(x)"), and watch the output in the Xcode console at the bottom</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Breakpoint debugging</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pause the program at a given line and inspect variable values</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Click next to a line number to place a blue marker; execution pauses there and you can step through</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI previews + debugger</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">See the UI and view hierarchy in real time</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">#Preview canvas + the runtime View Hierarchy inspector</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
The three debugging essentials

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tip: how do you read a crash?

{class="mt-1"}
When Swift crashes, the console prints "Fatal error" plus the reason, and Xcode stops on the offending line and highlights it. Historical crashes on real devices can be viewed in Xcode → Window → Organizer → Crashes (paid account required). When searching, prioritize "the first sentence of the error message + swiftui"—precise questions get precise answers.
:::

#### 2. Testing: insurance for your code

Manual testing can't be trusted—fix one feature and another quietly breaks. Tests are both the "undo button" and the "bulletproof vest." iOS uses the XCTest framework, in two flavors:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Level</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">What it tests</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Target</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Speed</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Unit tests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pure logic (calculations, validation)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppTests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Seconds</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UI tests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Real interface behavior</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppUITests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minutes</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Manual testing</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Human feel and experience</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Always needed</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
iOS testing levels (the template project already includes two Test Targets)

::: div .code-block
:::inline div .code-head
<span>SWIFT · Unit test example</span><span class="dots">···</span>
:::

```
import XCTest

// Extract logic like "amount string to number" into a pure function
func parseAmount(_ input: String) -> Double? {
    guard let v = Double(input.trimmingCharacters(in: .whitespaces)),
          v > 0 else { return nil }
    return v
}

final class AmountTests: XCTestCase {
    func testEmptyInputReturnsNil() {
        XCTAssertNil(parseAmount(""))
    }
    func testNegativeReturnsNil() {
        XCTAssertNil(parseAmount("-5"))
    }
    func testNormalValueParses() {
        XCTAssertEqual(parseAmount("12.5"), 12.5)
    }
}
```
:::

Run tests with ⌘U. Change code only once everything is green, and you'll feel confident. The amount validation and summary calculations in the expense tracker should all be covered by unit tests.

#### 3. Signing and packaging: stamping your app

Every iOS app must be signed before it can be installed—proof that "this package came from you and hasn't been tampered with." The hierarchy:

- Learning stage: a free Apple ID + Xcode automatic signing (Personal Team) runs on a real device, renewed every 7 days;
- Distribution stage: a paid developer account (99 USD/year) issues the certificates and provisioning profiles needed to ship and install long-term.

Packaging: in Xcode, Product → Archive; once the build finishes, in Organizer choose Distribute App → App Store Connect → upload. Archiving must target the Generic iOS Device (not the Simulator)—a step beginners often forget.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Pitfall warning: lose the certificate = updates cut off

{class="mt-1"}
Once a signing certificate and its private key are lost, you can no longer push updates to your old app—users can only install it as a "brand-new" app. Back up your certificates carefully (export a .p12 from Keychain) and keep the password safe. Fortunately, Apple offers "automatic signing" and cloud certificate management (check Automatically manage signing in Xcode), which spares you most of the manual pitfalls.
:::

#### 4. The full App Store submission process

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Register a developer account</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> Prepare store assets</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> Upload the build</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> Fill in privacy and review info</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Apple review (1-7 days)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> Published</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figure 5: Six steps to the App Store
:::

- Register: developer.apple.com, personal accounts 99 USD/year;
- Assets: icon (1024×1024, no rounded corners—Apple does the rounding itself), screenshots (each iPhone size), description, privacy policy link;
- Privacy questionnaire: honestly declare what data you collect—an offline expense tracker can declare "no data collected";
- Review: the first submission often waits 1–7 days; if rejected, fix things one by one per the "review notes"—Apple's rejection reasons are usually written very specifically, so just follow them;
- TestFlight: before release, send a beta build to friends for internal testing (up to 10,000 people), gather a round of feedback, then submit officially—very professional.

#### 5. Store assets: first impressions drive downloads

The store page is the shop window users see while "browsing." Three assets decide the first impression:

- Icon: 1024×1024, don't just make do with a screenshot. If you have no design skills, use an AI tool to generate a simple graphic; it only passes if it's still recognizable when shrunk down on a home screen;
- Screenshots: at least 2 sets (mainstream iPhone sizes), showing your most core feature scenarios; give each one a plain-language caption ("Log an expense in one second" beats "An efficient expense-tracking solution" ten times over);
- Description: the first sentence should make clear "what this is + who it's for." Don't pile on "the most professional, the most powerful"—sincerity works better than hype.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Get hands-on: "ship" the expense tracker once

#### 6. A mini checklist for crash reporting and performance

Before release, these two things are each worth half an hour:

##### 1. Crash monitoring

Just because it didn't crash in your testing doesn't mean it won't on users' phones. Apple provides free crash reports in the Xcode Organizer (paid accounts can see real-device crash logs); an even more hassle-free option is a third-party SDK (such as Firebase Crashlytics). Shipping without crash monitoring is like driving with your eyes closed.

##### 2. Four performance self-checks

1. Use LazyVStack / List for lists: don't lay out long lists with a plain VStack—lazy loading is lesson one of performance;
2. Don't force in full-size images: use AsyncImage (for remote images) and the system cache; a 5MB original can bog down older phones badly;
3. Don't do heavy work on the main thread: route network calls and large files through async/await;
4. Measure with Instruments: Xcode's built-in profiler (Time Profiler, memory leak checks)—measure first, then optimize; don't go by feel.

{class="mt-1"}
① Add 3 unit tests for logic like parseAmount (green with ⌘U); ② use a breakpoint to catch a crash you created yourself and fix it; ③ build a package with Product → Archive and invite friends to test via TestFlight; ④ if you have the bandwidth, register a developer account and actually submit the expense tracker to the store. The first three steps can be done tonight.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Chapter summary

- The three debugging essentials: print logs, breakpoints, and SwiftUI previews with the view inspector
- XCTest: unit tests (⌘U) + UI tests + manual testing, prebuilt in the template
- Signing: free accounts get automatic signing (renewed every 7 days); distribution requires a paid account
- Packaging: Generic iOS Device + Archive + Distribute; always back up your certificates
- Six steps to release: register → assets → upload → privacy questionnaire → review → go live; beta test with TestFlight first
:::
