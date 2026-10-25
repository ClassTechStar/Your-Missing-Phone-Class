---
id: di-wu-shi-yi-zhang
num: 51
part: an-zhuo-kai-fa-pian
nav: Chapter 51: Building UIs — Getting Started with Jetpack Compose
toc: default
kind: chapter
---

### Chapter 51: Building the UI — Getting Started with Jetpack Compose

{class="chapter-intro mb-4"}
The UI is everything the user sees. Before Compose came along, Android UIs were written in XML — as tedious as fill-in-the-blank exercises. In 2021 Google introduced Jetpack Compose: you "draw" the UI directly in Kotlin code, what you see is what you get, and the preview refreshes the moment you change a line of code. By 2026, Compose is the clear mainstream for new projects. This chapter is where we learn to "draw."

#### I. Compose's Big Idea: The UI Is a Function

Compose's core idea in one sentence: UI = function. Everything that can appear on screen (text, buttons, images) is a "composable function," marked with @Composable. Nest them like building blocks, and that's your UI.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Your first Compose screen</span><span class="dots">···</span>
:::

```
@Composable
fun Greeting(name: String) {
    Text(text = "Hello, $name!")     // a "text building block"
}

// Nested composition: big blocks around small ones
@Composable
fun HomeScreen() {
    Column {                          // vertical stack
        Greeting(name = "Alex")
        Greeting(name = "Sam")
        Button(onClick = { /* what happens on tap */ }) {
            Text("Tap me")
        }
    }
}
```
:::

Note the @Composable "hat" — it tells the compiler "this is a UI building block." Blocks can nest infinitely; that's the whole secret of Compose.

#### II. Basic Components: Text, Button, Input Field, Image

Compose's components are "building blocks." The four most common:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Component</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">What It Does</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Required Parameter</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Displays text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">text (the text to show)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onClick (the click callback)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">value and onValueChange (the callback for input changes)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Displays images</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">painter (the image resource)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Compose's Four Basic Components

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Basic widgets example</span><span class="dots">···</span>
:::

```
@Composable
fun BasicWidgets() {
    Column {
        Text(text = "This is some text")
        Button(onClick = { println("clicked") }) {
            Text("Button")
        }
        var input by remember { mutableStateOf("") }
        TextField(
            value = input,
            onValueChange = { input = it },
            label = { Text("Type something") }
        )
    }
}
```
:::

In those two lines for the input field you'll spot remember { mutableStateOf("") } — that's Compose's "state" magic, covered in detail in Section 5 of this chapter. For now, just get acquainted with it.

#### III. The Layout Trio: Column, Row, Box

You have the components — how do you arrange them? Remember three "boxes":

- Column: stacks things vertically (like a line at the cafeteria counter);
- Row: lines things up horizontally (like sitting side by side);
- Box: stacks things on top of each other (like a pile of playing cards — great for badges and overlays).

::: div .code-block
:::inline div .code-head
<span>KOTLIN · The three layout building blocks</span><span class="dots">···</span>
:::

```
Column {
    Text("First row")
    Row {
        Text("Left")
        Text("Right")
    }
    Box {
        Text("Bottom layer")
        Text("Corner badge stacked on top")
    }
}
```
:::

Want the layout to look better? Add a Modifier to components — it's like putting makeup on your building blocks:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Handy Modifier moves</span><span class="dots">···</span>
:::

```
Text(
    text = "Pretty text",
    modifier = Modifier
        .padding(16.dp)          // padding on all sides
        .fillMaxWidth()          // fill the width
        .background(Color.Blue)  // background color
        .clickable { /* tap */ }// clickable
)
// Chained calls: one after another, order matters (padding first, then background — the background excludes the padding)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Note: Modifier Order Matters

{class="mt-1"}
padding(16.dp).background(Blue) and background(Blue).padding(16.dp) give different results — the first is "spacing first, then paint" (the background excludes the padding), the second is "paint first, then spacing" (the background includes the padding). This is where beginners most often paint themselves a "mysterious white border." When unsure, swap the order — the preview instantly tells you the answer.
:::

#### IV. State: Bringing the UI to Life

A static UI is boring. To make a number go up by 1 when a button is clicked, or let an input field accept typing, you need state. Compose's rule: the UI always faithfully reflects the state — when the state changes, the UI redraws automatically.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · State: a tap counter</span><span class="dots">···</span>
:::

```
@Composable
fun Counter() {
    // remember + mutableStateOf: remember this changing value
    var count by remember { mutableStateOf(0) }

    Column {
        Text(text = "You tapped $count times")
        Button(onClick = { count++ }) {   // change the state
            Text("Tap me +1")                // the UI refreshes automatically
        }
    }
}
```
:::

Three lines of code, one live counter. This is where Compose feels better than the old way: no manually "refreshing the UI" — just change the data. Remember the two key functions: remember (keeps a value from being wiped when the UI recomposes) and mutableStateOf (tells Compose "redraw when this value changes").

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> User taps</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> State changes (count++)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> Compose notices the change</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> UI redraws automatically (recomposition)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figure 3: Compose's one-way data flow from state to UI
:::

#### V. Theming and Dark Mode: Configure Once, Apply Everywhere

The MyFirstAppTheme { ... } in the template project is the theme. Based on the Material 3 design spec, it manages colors, fonts, and shapes in one place. Supporting dark mode takes only three steps:

1. Define both a light and a dark color scheme in the theme (the template already generates the ColorScheme);
2. When the system switches to dark mode, isSystemInDarkTheme() detects it automatically;
3. Use the colors the theme provides (like MaterialTheme.colorScheme.primary) instead of hard-coded color values.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tip: Material 3 Dynamic Color

{class="mt-1"}
Starting with Android 12, "Material You" lets an app pull colors from your wallpaper. Compose templates support it by default (dynamicColor). Your app will "change outfits" on different users' phones — that's the romance of modern Android.
:::

#### VI. Preview, Animation, and Live Edit: Compose's "Cheat Codes"

Three "cheat codes" for Compose's developer experience — once you use them, there's no going back:

- @Preview: add the @Preview annotation to a Composable and Android Studio instantly renders the UI on the right side — what you see is what you get as you edit, no need to install on a phone every time;
- Live Edit: the 2026 Android Studio supports "hot updating" certain changes on the emulator or a real device — small tweaks like changing text color appear on the device in seconds;
- Animation APIs: animateFloatAsState and AnimatedVisibility let elements transition smoothly in a few lines of code — that "premium feel" is often just these few dozen lines away.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Animations in ten minutes</span><span class="dots">···</span>
:::

```
@Composable
fun AnimatedBox() {
    var big by remember { mutableStateOf(false) }
    // when the value changes, it smoothly animates to the target
    val size by animateDpAsState(if (big) 120.dp else 60.dp)

    Box(Modifier
        .size(size)
        .background(MaterialTheme.colorScheme.primary)
        .clickable { big = !big }
    )
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tip: Function First, Animation Later

{class="mt-1"}
A common beginner mistake is fussing over animations before the UI even works. Get the feature running first, then add motion at the end — that's the Simplicity First principle too: animations are the icing on the cake, features are the cake itself.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Hands-On: Build a "Mood Button"

{class="mt-1"}
Turn the template project into a mood switcher: one button that, when tapped, cycles through 😀 happy → 😢 sad → 😡 angry, with the text and background color changing along. Hint: use when to pick the wording and color based on the state. Send it to friends when it's done and collect your first round of "whoa, you can make apps now".
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Chapter Summary

- Compose's idea: the UI = @Composable functions, nested like building blocks
- Four basic components: Text / Button / TextField / Image
- The layout trio: Column stacks vertically, Row lines up horizontally, Box stacks on top
- Modifier chains apply "makeup" in sequence: padding, fillMaxWidth, background, clickable — order matters
- State is the soul: remember + mutableStateOf — change the data and the UI redraws itself
- Theming with Material 3 + dynamic color: configure dark mode once and it applies everywhere
:::
