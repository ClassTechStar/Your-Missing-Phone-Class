---
id: di-liu-shi-jiu-zhang
num: 69
part: ios-kai-fa-pian
nav: Chapter 69: Quick Reference and Resources
toc: default
kind: chapter
---

### Chapter 69: Quick Reference and Resources

{class="chapter-intro mb-4"}
This chapter is a quick-reference handbook that works on its own. When you can't remember a bit of syntax or need to make a fast decision, flip straight here. Treat it as a set of "pocket cards": common code, common questions, and learning resources—nothing left out.

#### 1. Common code cheat sheet

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">What you want to do</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Key code</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Page-private state</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State private var x = initialValue</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logic shared across pages</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Observable class VM { var x = 0 }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Vertical/horizontal layout</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack { }</code> / <code class="inline">HStack { }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Flexible space</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Spacer()</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lists</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List { ForEach(array) { ... } }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Navigating between pages</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">NavigationStack + NavigationLink</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bottom sheet</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">.sheet(isPresented: $show) { content }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dismiss the current page</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Environment(\.dismiss) var dismiss</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fetch data over the network</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">try await URLSession.shared.data(from: url)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">JSON parsing</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X: Codable</code> + <code class="inline">JSONDecoder().decode</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Store small settings</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults.standard.set(value, forKey: "key")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Store structured data</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Model</code> + <code class="inline">modelContainer</code> + <code class="inline">@Query</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dark mode support</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Use system colors (.primary / Color(.systemGray6)); never hard-code</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Run tests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><kbd>⌘U</kbd></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
iOS development cheat sheet (August 2026 edition)

#### 2. Frequently asked questions (FAQ)

Q1: Can I learn iOS development without a Mac?

You can learn the language, but not do the full development. Swift Playgrounds on iPad/iPhone can cover everything in Chapter 61; but Xcode is macOS-only, so in the end you'll need a Mac. On a tight budget, you can rent a cloud Mac or buy a used Mac mini as a stopgap, then decide how much to invest after learning the language.

Q2: How much does learning iOS development cost?

Learning stage: 0 dollars (Xcode is free + a free Apple ID for on-device debugging). Release stage: a developer account at 99 USD/year (about 700 RMB). Add a Mac, and that's the entire cost. Compared with the payoff—even a small utility on the App Store has paying users—the math works out.

Q3: SwiftUI or UIKit—which one first?

SwiftUI. In 2026, new projects, new tutorials, and new job listings all center on SwiftUI, and this book uses it throughout. UIKit is the previous-generation framework, still used in many older projects—once you're comfortable with SwiftUI, pick up UIKit as needed (Apple has interop tutorials), and it will come quickly. Just don't reverse the order.

Q4: Is iOS development easy to find work in?

The 2026 job market: entry-level roles that amount to "can draw interfaces" are fiercely competitive, but developers who "know Swift + SwiftUI and have a shipped app" are still in demand. Median pay for iOS roles has ranked near the top among tech stacks for years. While you're learning, the best line on your resume is that app you made, sitting in the store.

Q5: What if my app gets rejected in review?

Don't panic—it's normal; first submissions get rejected at a decent rate. Apple's rejection reasons are usually written very specifically (which page, which guideline). Fix things one by one, reply with an explanation in App Store Connect, and resubmit. The three most common rejection reasons: permission purposes not clearly explained, buggy interfaces, and metadata (screenshots/description) that doesn't match the real thing. Self-check those three ahead of time and you'll save yourself a round of waiting.

#### 3. High-frequency Xcode shortcuts

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Action</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Shortcut</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Run / test</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R / ⌘U</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Open the canvas preview</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Quickly open a file</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Search everywhere</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘F</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fix indentation</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Comment / uncomment</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Clean the build cache</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘K</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jump to definition</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘-click</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rename (safe renaming across the project)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Right-click → Refactor → Rename</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
High-frequency Xcode shortcuts

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tip: when builds act haunted, clean the cache first

{class="mt-1"}
That spooky "it ran yesterday but not today" phenomenon is, six or seven times out of ten, a scrambled build cache. Clean with ⇧⌘K and rebuild, and it cures the majority of these hauntings. Still broken? Restart Xcode (and the Mac along with it), and if that fails, "delete the DerivedData folder"—the legendary ultimate trio, passed down among iOS developers.
:::

#### 4. Recommended learning resources

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Type</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Resource</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Why it's recommended</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Official</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">developer.apple.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple's official documentation, with the SwiftUI/Swift tutorials inside—the first authority</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Official</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple's SwiftUI Tutorials</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple's official hands-on course—maximum beginner-friendliness</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Official</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The Swift website (swift.org)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Official language docs and an online playground</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Community</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hacking with Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Paul Hudson's free tutorial library, widely recognized as top-tier in quality</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Community</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stack Overflow (the swiftui tag)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The first stop when an error has you stumped</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Video</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The official Apple Developer channel (WWDC videos)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Authoritative coverage of each year's new technologies</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Design</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple's Human Interface Guidelines (HIG)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The official bible for building interfaces with that "Apple feel"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Companion</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Part 7, "Hands-On AI Coding" (Chapters 37–47)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The complete playbook for AI-assisted iOS development</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
iOS development learning resources (August 2026)

#### 5. Closing: from your first app to your Nth app

Looking back, you went from "having no idea what SwiftUI was" to installing Xcode, learning Swift, drawing interfaces with SwiftUI, hooking your app up to a database and the network, and on to testing, packaging, and shipping—on this road, you've already walked the hardest stretch of the journey from zero to one.

The world of technology changes fast: frameworks upgrade, tools get replaced, and AI takes over more and more of the "typing" work. But one thing never goes out of date: your ability to take a fuzzy idea, break it into clear steps, and then build it one step at a time. Tools are the amplifier; the way you think is the foundation. The amplifier can be swapped out; the foundation must not shake.

:::inline div .quote-line
You're no longer just "someone who knows how to use a phone." You can turn the ideas in your head into real apps running on hundreds of millions of iPhones. From today, create with your keyboard — that's the romance of being an iOS developer.
:::

#### References

{class="list-decimal pl-6 mb-3 space-y-1 text-xs text-gray-500"}
1. Apple Inc. (2026). SwiftUI Framework Documentation. developer.apple.com.
2. Apple Inc. (2026). Swift Programming Language Guide. swift.org.
3. Apple Inc. (2026). SwiftData Framework Documentation. developer.apple.com.
4. Apple Inc. (2026). App Store Review Guidelines. developer.apple.com/app-store/review.
5. Apple Inc. (2026). Human Interface Guidelines (HIG). developer.apple.com/design.
6. Apple Inc. (2026). Xcode 27 Release Notes and App Distribution Guide.
