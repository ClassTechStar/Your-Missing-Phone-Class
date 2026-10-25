---
id: di-liu-shi-san-zhang
num: 63
part: ios-kai-fa-pian
nav: Chapter 63: Views, State, and Navigation
toc: default
kind: chapter
---

### Chapter 63: Views, State, and Navigation

{class="chapter-intro mb-4"}
You already know how to build a single-screen toy. This chapter tackles two "growing up" problems: how to hop between multiple screens (navigation) and how data flows between screens (state management). After this chapter, you'll be able to build the classic multi-screen app skeleton: "list → detail → edit."

#### 1. The Big Picture of State Management and Data Flow

@State isn't the only state tool in SwiftUI. Start with this overview so you understand "which one to use when":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tool</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">What it manages</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Who uses it</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Typical scenario</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Private, temporary state for one screen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The current view</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Counters, text field content</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Binding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Borrowing someone else's state</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A child view changing a parent view</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Custom components</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@StateObject / @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logic shared across screens</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The view model (ViewModel)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Data loading, business logic</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@EnvironmentObject / .environment</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">State shared across the whole app</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The entire app</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Login state, theme settings</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
The SwiftUI state toolbox at a glance (2026, @Observable is now mainstream)

::: div .code-block
:::inline div .code-head
<span>SWIFT · The 2026 mainstream: @Observable view models</span><span class="dots">···</span>
:::

```
// The modern way on iOS 17+: the @Observable macro (recommended for new projects)
import Observation

@Observable
class CounterModel {                 // the view model
    var count = 0
    func increment() { count += 1 }
}

struct CounterView: View {
    @State private var model = CounterModel()   // holds the model

    var body: some View {
        VStack {
            Text("You tapped \(model.count) times")
            Button("Tap me") { model.increment() }
        }
    }
}
```
:::

Blunt advice for beginners: use @State for state private to one screen, and @Observable classes for anything shared across screens or involving logic. The @StateObject/@ObservableObject in older tutorials are the previous generation—being able to read them is enough; write new code the way described above.

#### 2. NavigationStack: The "Stack" Behind Screen Jumps

Since iOS 16, multi-screen navigation uses NavigationStack—like a stack of plates: push one on, and pop them off one by one as you go back:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Navigation with NavigationStack</span><span class="dots">···</span>
:::

```
struct HomeView: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("Alex's ledger") {
                    DetailView(name: "Alex's ledger")   // destination screen
                }
                NavigationLink("Sam's ledger") {
                    DetailView(name: "Sam's ledger")
                }
            }
            .navigationTitle("Ledger list")   // large title at the top
        }
    }
}

struct DetailView: View {
    let name: String
    var body: some View {
        Text("\(name) details")
            .navigationTitle(name)
            .navigationBarTitleDisplayMode(.inline)
    }
}
```
:::

NavigationLink is a "tappable link to another screen"; navigationTitle automatically generates the navigation bar title and the back button. When you need programmatic navigation (say, returning automatically after tapping "Save"), use @Environment(\.dismiss) to close the current screen—together, these two tricks cover 90% of your navigation needs.

#### 3. Pop-Ups and Bottom Tabs: sheet and TabView

Besides "pushing screens," there are two more classic interactions:

::: div .code-block
:::inline div .code-head
<span>SWIFT · sheet dialogs + TabView tabs</span><span class="dots">···</span>
:::

```
// 1. Slides up half/full screen (the favorite for entry forms)
struct HomeView: View {
    @State private var showAdd = false
    var body: some View {
        Button("Add entry") { showAdd = true }
            .sheet(isPresented: $showAdd) {
                AddRecordView()     // the entry sheet
            }
    }
}

// 2. The bottom tab bar (the app's "skeleton")
struct MainTabView: View {
    var body: some View {
        TabView {
            RecordListView()
                .tabItem { Label("Ledger", systemImage: "book") }
            StatsView()
                .tabItem { Label("Stats", systemImage: "chart.pie") }
            SettingsView()
                .tabItem { Label("Settings", systemImage: "gear") }
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tip: When Do You Use Which?

{class="mt-1"}
Rules of thumb: use NavigationStack to push screens for the main flow (list → detail), use a sheet pop-up for temporary actions (adding, editing, confirming), and use TabView for several side-by-side sections (bottom tabs). Combine the three, and you have the skeleton of the vast majority of apps.
:::

#### 4. List: iOS's Go-To List

The most used—and most "Apple-flavored"—component on iOS is List: it comes with dividers, swipe-to-delete, and tap highlighting out of the box:

::: div .code-block
:::inline div .code-head
<span>SWIFT · List + swipe to delete</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var records = ["Lunch 25.5", "Metro 6.0", "Salary +8000"]

    var body: some View {
        List {
            ForEach(records, id: \.self) { r in
                Text(r)
            }
            .onDelete { indexSet in          // swipe left to delete
                records.remove(atOffsets: indexSet)
            }
        }
    }
}
```
:::

List + NavigationLink + sheet + TabView—put these four together, and you can already build a complete app skeleton: "ledger list → tap for details → tap + to open the entry sheet." The expense tracker project in the next chapter is built exactly this way.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Hands-on: Build a "Three-Screen Skeleton"

#### 5. The App Lifecycle: Foreground and Background

Much like Android's Activity lifecycle, iOS apps also move through "born, foreground, background, dead" state changes. In SwiftUI, watch them with the scenePhase environment value:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Observing foreground/background switches</span><span class="dots">···</span>
:::

```
@main
struct MyApp: App {
    @Environment(\.scenePhase) private var phase

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .onChange(of: phase) { _, newPhase in
            switch newPhase {
            case .active:    print("Back in the foreground, resuming refresh")
            case .inactive:  print("Transitioning (call / just backgrounded)")
            case .background: print("Went to background, saving draft")
            @unknown default: break
            }
        }
    }
}
```
:::

Typical uses: refresh data when coming back to the foreground, save drafts when heading to the background. iOS runs a tight ship on background activity—an ordinary app gets suspended (frozen) shortly after going to the background, so don't expect to secretly do heavy work back there; if you truly need scheduled tasks, use the local notifications from Chapter 68 instead of "staying alive in the background."

{class="mt-1"}
Build a fake-data skeleton of the expense tracker: a TabView with three tabs (Ledger / Stats / Settings) → the Ledger screen shows fake data in a List, and tapping a row jumps to the details (NavigationStack) → the "+" button in the top-right opens the entry sheet. No saving, no internet—pure skeleton practice. Get this skeleton right, and filling it with real data in Chapter 65 will be a smooth ride.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Chapter summary

- The four state tools: @State (screen-private), @Binding (borrowed), @Observable (logic), .environment (global)
- Use the @Observable macro for view models in new projects; being able to read the older @ObservableObject is enough
- NavigationStack pushes screens; @Environment(\.dismiss) navigates back programmatically
- Push screens for the main flow, pop up a sheet for temporary actions, and use TabView for side-by-side sections
- List is the go-to list: dividers and swipe-to-delete work out of the box
:::
