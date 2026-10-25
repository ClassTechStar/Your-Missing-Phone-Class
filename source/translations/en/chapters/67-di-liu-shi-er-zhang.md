---
id: di-liu-shi-er-zhang
num: 62
part: ios-kai-fa-pian
nav: Chapter 62: Building UIs — Getting Started with SwiftUI
toc: default
kind: chapter
---

### Chapter 62: Building Interfaces—Getting Started with SwiftUI

{class="chapter-intro mb-4"}
The interface is everything the user sees. SwiftUI is the declarative interface framework Apple launched in 2019—you only need to "declare" what the interface looks like, and the system automatically takes care of rendering, dark mode, and every kind of screen. By 2026, SwiftUI is the clear mainstream for new projects. In this chapter, we learn to "paint."

#### 1. The SwiftUI Idea: Declarative, Not Imperative

Old-style interface development is "imperative": you give the system orders one step at a time—"create a button → place it at (20,30) → set the color." SwiftUI is "declarative": you simply describe "there's a red button on the screen that says 'Tap me'," and the system takes care of how to draw it and when to redraw it.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Your first SwiftUI view</span><span class="dots">···</span>
:::

```
import SwiftUI

struct ContentView: View {
    var body: some View {      // body: describes "what the screen looks like"
        VStack {               // vertical stack
            Text("Hello, world!")
                .font(.largeTitle)      // modifier: large title
            Button("Tap me") {
                print("clicked")
            }
            .buttonStyle(.borderedProminent)  // solid blue button
        }
        .padding()
    }
}
```
:::

Key point: a view = a struct that conforms to the View protocol, the body property describes the interface, and .modifier() chains "apply the makeup." That's the entire foundation of SwiftUI.

#### 2. The Basic Views: Text, Buttons, Text Fields, Images

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">View</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">What it does</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Example</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Displays text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text("Hello")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button("Tap me") { action }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text field</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField("Placeholder", text: $text)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Displays an image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Image(systemName: "star.fill")</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
SwiftUI's four basic views

Notice Image(systemName:)—Apple ships a built-in icon library called SF Symbols (thousands of free icons); a name like "star.fill" instantly shows a solid star. This is a hidden perk of iOS development: you almost never have to hunt for icon assets.

#### 3. The Layout Trio: VStack, HStack, ZStack

- VStack: lines things up vertically (like queuing for lunch);
- HStack: lines things up horizontally (like sitting side by side);
- ZStack: stacks things on top of each other (like a pile of playing cards—perfect for badges and overlays).

::: div .code-block
:::inline div .code-head
<span>SWIFT · The three layout stacks + common modifiers</span><span class="dots">···</span>
:::

```
VStack(alignment: .leading, spacing: 12) {
    HStack {
        Text("Bill")
        Spacer()                 // flexible space: pushes the right side to the edge
        Text("-25.5 yuan").foregroundColor(.red)
    }
    Divider()                    // divider
    Text("Note: lunch")
}
.padding(16)                     // padding on all sides
.background(Color(.systemGray6)) // light gray background
.cornerRadius(12)                // rounded corners

// Modifier order matters: padding first, then background — the background excludes the padding
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Note: Modifier Order Matters

{class="mt-1"}
padding(16).background(gray) and background(gray).padding(16) produce different results—the former "spaces first, then paints" (the background excludes the padding), the latter "paints first, then spaces" (the background includes the padding). This is the source of beginners' most common "mystery white edge." When in doubt, swap the order and the preview will tell you the answer instantly.
:::

#### 4. State and Binding: Bringing the Interface to Life

A static interface is dull. SwiftUI's rule: the interface always faithfully reflects the state—when the state changes, the interface redraws automatically.

::: div .code-block
:::inline div .code-head
<span>SWIFT · A @State counter</span><span class="dots">···</span>
:::

```
struct CounterView: View {
    @State private var count = 0   // @State: when this value changes, redraw

    var body: some View {
        VStack {
            Text("You tapped \(count) times")
            Button("Tap me +1") {
                count += 1          // change the state; the UI refreshes automatically
            }
        }
    }
}
```
:::

A text field needs "two-way binding"—the $ symbol hands over both the value and the right to change it:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Two-way binding with @Binding</span><span class="dots">···</span>
:::

```
struct InputView: View {
    @State private var text = ""

    var body: some View {
        TextField("Type something", text: $text)  // $ = two-way binding
            .textFieldStyle(.roundedBorder)
        Text("You typed: \(text)")   // updates live as you type
    }
}
```
:::

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> User action</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> State changes (count += 1)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> SwiftUI notices the change</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> UI redraws automatically (body recomputed)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figure 3: SwiftUI's one-way "state → interface" data flow
:::

#### 5. Previews, Theming, and Animation: SwiftUI's "Power-Ups"

- The #Preview macro: add #Preview { ContentView() } at the bottom of a file, and the canvas on the right renders in real time—change the code and see the result immediately;
- Dark mode for free: use system colors (Color(.systemGray6), .primary) instead of hard-coded ones, and dark mode adapts automatically without a single extra line;
- Animation in one line: withAnimation { count += 1 } or add .animation(.default, value: count) to a view—buttery-smooth transitions.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Animations in ten minutes</span><span class="dots">···</span>
:::

```
struct AnimatedHeartView: View {
    @State private var liked = false

    var body: some View {
        Button {
            withAnimation(.spring(duration: 0.4)) {
                liked.toggle()
            }
        } label: {
            Image(systemName: liked ? "heart.fill" : "heart")
                .font(.system(size: 48))
                .foregroundColor(liked ? .red : .gray)
                .scaleEffect(liked ? 1.3 : 1.0)
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tip: Function First, Animation Later

{class="mt-1"}
A classic beginner mistake is "polishing animations before the interface even works." Get the functionality running first, then add motion at the end—animation is the icing, function is the cake. That's also our standing "simplicity first" principle.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Hands-on: Build a "Mood Button"

#### 6. Common Modifiers Cheat Sheet: One Page in Hand, No Interface Worries

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">What you want to do</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Modifier</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Spacing</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.padding(16)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rounded corners</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cornerRadius(12)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Background color</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.background(Color(.systemGray6))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Font and size</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.font(.title.bold())</code> / <code class="inline">.font(.system(size: 20))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Foreground color (text/icons)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.foregroundColor(.red)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fill the width</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(maxWidth: .infinity)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fixed size</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(width:100, height: 44)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Alignment</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack(alignment: .leading)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Opacity</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.opacity(0.6)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Shadow</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.shadow(radius: 5)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tap gesture</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.onTapGesture { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Keyboard type</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.keyboardType(.decimalPad)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Common SwiftUI modifiers cheat sheet

No need to memorize any of this—this page is for looking things up. The ones you'll use most are actually just the first four: padding, rounded corners, background, and font.

{class="mt-1"}
Turn the template project into a mood switcher: one button that cycles through 😀 happy → 😢 sad → 😡 angry with each tap, while the text and background color change along with it. Hint: store the three pairs (text + color) in an array, keep the index in @State, and on each tap use (index + 1) % 3. Send it to a friend when you're done and collect your first round of "wow, you can make apps now."
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Chapter summary

- SwiftUI is declarative: you describe "what it looks like," and the system handles drawing and redrawing
- A view = a struct conforming to the View protocol; body describes the interface; modifiers chain on like "makeup"
- The four basic views: Text / Button / TextField / Image; the SF Symbols icon library is free and all-you-can-eat
- The layout trio: VStack stacks vertically, HStack horizontally, ZStack in layers; Spacer is flexible space
- @State brings the interface to life; $ feeds two-way bindings into text fields
- #Preview is WYSIWYG; system colors adapt to dark mode automatically; withAnimation adds motion in one line
:::
