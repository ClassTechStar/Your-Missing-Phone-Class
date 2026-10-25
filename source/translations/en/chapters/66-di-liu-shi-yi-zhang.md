---
id: di-liu-shi-yi-zhang
num: 61
part: ios-kai-fa-pian
nav: Chapter 61: A Quick Start with Swift — Apple's First Language
toc: default
kind: chapter
---

### Chapter 61: Swift Quick Start—Apple's Top Development Language

{class="chapter-intro mb-4"}
In this chapter we officially start learning the language. Don't worry—Swift is famous for being "beginner-friendly," and you don't need to memorize a grammar book: once you've mastered 20% of the syntax, you can read and write 80% of everyday code. Look up the rest as you go, while working on projects. Remember our learning principle: understanding beats memorizing, and being able to use it beats being an expert.

#### 1. Variables and Types: Giving Data a Name

A program is just "data + logic." A variable is simply a name you give to a piece of data so you can store it. Swift declares them with let and var:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Variables</span><span class="dots">···</span>
:::

```
let name = "Alex"        // let: constant (the recommended default)
var age = 18             // var: variable (can change later)

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var can change
// name = "Sam"         // <i class="fas fa-times-circle mr-1"></i> let can't be changed — compile error

let score: Int = 100     // you can also declare the type explicitly
let pi = 3.14            // omitted, it's still inferred automatically

print("Hello, \(name)")   // string interpolation: backslash + parentheses
```
:::

Memorize the common types with one table:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Type</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">What it holds</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Example</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Whole numbers</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Decimals</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Hello"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bool</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">True/false</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[Int] (an array)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A group of values</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[1, 2, 3]</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Common basic types in Swift

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tip: The let-First Principle

{class="mt-1"}
An iron rule of the Swift community: use let by default, and only use var when it's truly necessary. If you use var where let would do, Xcode will warn you with yellow text. This habit saves you from a whole family of "variable got changed by accident" bugs—the less your code changes, the easier it is to reason about.
:::

#### 2. Optionals: Swift's "Anti-Crash Charm"

This is the most important concept in Swift, bar none. In one sentence: when a value might "not exist," Swift forces you to deal with it—wiping out the industry's nightmare of "null pointer crashes" at the language level.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Optionals</span><span class="dots">···</span>
:::

```
var name: String = Alex   // a regular type: never allowed to be nil
// name = nil                // <i class="fas fa-times-circle mr-1"></i> compile error — it stops you outright

var nickname: String? = nil  // add a question mark: nil is allowed (an optional)
nickname = "Al"

// To use an optional, you must "unwrap" it:
if let n = nickname {        // if let: safe unwrapping
    print("Hello, \(n)")
} else {
    print("No nickname yet")
}

let len = nickname?.count ?? 0   // ?? provides a default (the nil-coalescing operator)
print(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Note: ! Is a "High-Risk Operation"

{class="mt-1"}
Writing nickname! in code (force unwrapping) is like shouting at the compiler, "I guarantee it's not nil"—guess wrong once, and the app crashes on the spot. Beginner rule: use if let / ?? wherever possible, and never use !. When Xcode autocompletes your code it occasionally slips in a !—remember to swap it out.
:::

#### 3. Functions and Closures: Packing Logic into "Buttons"

A function is a named piece of logic, like a button on a remote control. A closure is a "function with no name," one you can hand to someone else on the spot:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Functions and closures</span><span class="dots">···</span>
:::

```
// Functions: name first, then parameters and return type
func greet(name: String) -> String {
    return "Hello, \(name)!"
}
print(greet(name: "Alex"))     // the argument label is required at the call site

// Closures: defined inline, quick and direct
let numbers = [1, 2, 3, 4]
let doubled = numbers.map { $0 * 2 }   // $0 = the current element
// [2, 4, 6, 8]

let big = numbers.filter { $0 > 2 }    // filter
// [3, 4]
```
:::

Closures are everywhere in SwiftUI: the braces after Button("Tap me") { ... } are a closure. Please commit these "collection combo moves" to memory—map, filter, and sorted—because 90% of the list handling you'll ever do is just combinations of them.

#### 4. Structs and Protocols: Swift's "LEGO" System

Swift's official preference is clear: prefer structs, and use classes only when you need inheritance. A struct is a "value type"—each copy lives its own separate life, which naturally cuts out a whole family of bugs:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Structs and protocols</span><span class="dots">···</span>
:::

```
// A struct: a box for data
struct Record {
    var id = UUID()
    var amount: Double
    var category: String
    var date: Date

    // Structs come with a built-in "memberwise initializer": you can create one directly
}
let r = Record(amount: 25.5, category: "Food", date: Date())

// A protocol: a contract for "which abilities are required"
protocol Identifiable {
    var id: UUID { get }
}
struct Record: Identifiable { ... }   // conforming to a protocol = promising to fulfill its requirements
```
:::

Almost everything in SwiftUI is a struct (View is a protocol). It's fine if that sentence doesn't click yet—you'll run into it every day in Chapter 62. In the world of Swift, embrace the struct first.

#### 5. A Syntax Cheat Sheet for Absolute Beginners

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">What you want to do</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">How to write it</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Define a constant/variable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">let x = 1</code> / <code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String interpolation</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Hello, \(name)"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Define a function</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">func name(parameter: Type) -> ReturnType { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Making a decision</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if condition { ... } else { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Looping through items</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for x in array { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Safe unwrapping</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if let x = optionalValue { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Default value</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">x ?? defaultValue</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Define a struct</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X { var a: Int; var b: String }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Closures</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">{ $0 * 2 }</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Swift syntax cheat sheet (beginner edition)

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Hands-on: Play with Swift in Playgrounds for 15 Minutes

{class="mt-1"}
If you have a Mac, open Xcode > Playground; if not, use Swift Playgrounds on the iPad or a web-based playground. Run every piece of code in this chapter, fiddle with the numbers and text, and deliberately create a few errors to see how Xcode reacts. These 15 minutes of "play first, learn after" will make starting Chapter 62 twice as easy.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Chapter summary

- let first, var with care; types are inferred automatically, but you can also declare them explicitly after a colon
- Optionals are the soul of Swift: if a value might be missing, you must handle it—if let / ?? are your protective charm, and ! is a high-risk move
- Function calls carry argument names; a closure = a function without a name, and they're everywhere in SwiftUI
- Prefer structs and conform to protocols; almost everything in SwiftUI is a struct
- 20% of the syntax does 80% of the work: learn to use it first, master it later
:::
