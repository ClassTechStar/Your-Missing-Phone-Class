---
id: di-wu-shi-zhang
num: 50
part: an-zhuo-kai-fa-pian
nav: Chapter 50: A Quick Start with Kotlin — Android's First Language
toc: default
kind: chapter
---

### Chapter 50: Kotlin Quick Start — Android's First Language

{class="chapter-intro mb-4"}
This chapter is where we officially learn the language. Don't be nervous — Kotlin is famous for being beginner-friendly, and you don't need to memorize a syntax book: master 20% of the syntax and you can read and write 80% of everyday code. Look up the rest as you work on projects. Remember our learning principle: understanding beats memorizing, using beats mastering.

#### I. Variables and Types: Giving Data a Name

A program is "data + logic." A variable is just a name you give data so you can store it. Kotlin has two ways to declare one:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Variables</span><span class="dots">···</span>
:::

```
val name = "Alex"        // val: read-only variable (the recommended default)
var age = 18             // var: mutable variable (can change later)

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var can change
// name = "Sam"         // <i class="fas fa-times-circle mr-1"></i> val can't be changed — compile error

val score: Int = 100     // you can also declare the type explicitly
val pi = 3.14            // omitted, it's still inferred automatically
```
:::

There are only a few common types — remember them with one table:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Type</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">What It Stores</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Example</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Whole numbers</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Decimal numbers</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Hi"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Boolean</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">True/False</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List&lt; T&gt;</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A group of data</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">listOf(1, 2, 3)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kotlin's Common Basic Types

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tip: The val-First Rule

{class="mt-1"}
An iron rule of the Kotlin community: use val by default and only use var when truly necessary. If you use var where val would work, the IDE will warn you with yellow text. This habit saves you a whole class of "variable got changed unexpectedly" bugs — the less your code changes, the easier it is to reason about.
:::

#### II. Functions: Packaging Logic into "Buttons"

A function is a named piece of logic, like a button on a remote control — press it (call it) and a sequence of actions runs. In Kotlin you declare one with fun:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Functions</span><span class="dots">···</span>
:::

```
fun greet(name: String): String {
    return "Hello, $name!"     // the $ sign inserts the variable into the string
}

println(greet(Alex))        // prints: Hello, Alex!

// single-line functions can be written as expressions
fun add(a: Int, b: Int) = a + b

println(add(3, 5))            // prints: 8
```
:::

A few key points: parameters go in the parentheses (name first, type after, separated by a colon); the return type goes after the parentheses; and string templates like $variableName are Kotlin's signature convenience — no more gluing "string + variable" together the way Java does.

#### III. Conditions and Loops: Teaching the Program to "Think"

A program's intelligence comes from two things: knowing how to judge (if/when) and knowing how to repeat (for/while).

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Conditionals and loops</span><span class="dots">···</span>
:::

```
// Decisions: if / else
val age = 17
if (age >= 18) {
    println("adult")
} else {
    println("minor")
}

// Multi-branch: when (a hundred times handier than switch)
val score = 85
val level = when {
    score >= 90 -> "excellent"
    score >= 60 -> "pass"
    else -> "Keep it up!"
}

// Repetition: a for loop
val fruits = listOf("apple", "banana", "orange")
for (fruit in fruits) {
    println("I love $fruit")
}
```
:::

when is Kotlin's most common way to write multi-branch logic, and you'll use it every day in Android development (like showing different screens based on state).

#### IV. Null Safety: Kotlin's "Life Saver"

The most famous bug of the Java era is the NullPointerException — the program touches something that "isn't there" and crashes on the spot. Statistics say it's the perennial number one on Android's crash leaderboard. Kotlin solved it at the language level: null values are not allowed by default.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Null safety</span><span class="dots">···</span>
:::

```
var name: String = Alex   // a regular type: never allowed to be null
// name = null                // <i class="fas fa-times-circle mr-1"></i> compile error — it stops you right there

var nickname: String? = null // add a question mark: null is allowed
nickname = "Al"

// When using nullable types, you must handle them safely:
println(nickname?.length)    // safe call: returns null instead of crashing
val len = nickname?.length ?: 0   // Elvis operator: default value when null
println(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Note: Don't Confuse ? and ?:

{class="mt-1"}
String? means "null is allowed," while a ?: b means "if a is null, use b" (it looks like Elvis's hairstyle, hence the name Elvis operator). When you're starting out and the compiler complains about a "null-related error," odds are you forgot to handle a nullable type — that's the language protecting you.
:::

#### V. Classes and Objects: Molds for Making "Parts"

A class is the "mold" for objects; objects are the "finished products" of a class. Everything in Android — screens, buttons, data — is an object. Kotlin has a magic tool called the data class, built specifically for "holding data," where one line does what takes dozens in Java:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Classes and data classes</span><span class="dots">···</span>
:::

```
// Regular class: a mold
class Dog(val name: String) {
    fun bark() = println("$name says woof!")
}

val dog = Dog("Rex")      // create an instance
dog.bark()                 // Rex says woof!

// data class: a box for data (with equals/copy built in)
data class User(val id: Int, val name: String, val email: String)

val me = User(1, Alex, "zhangsan@example.com")
val twin = me.copy(name = "Alexandra")   // copy and change one field
```
:::

Later, when you build an expense tracker, each entry is a data class: data class Record(val amount: Double, val category: String, val date: String). See — you can already write the code structure of a real project.

#### VI. Lambdas and Higher-Order Functions: Kotlin's "Syntax Candy"

In Android code you'll see { ... } every day — a "function without a name" called a lambda (anonymous function). Button's onClick = { count++ } is a lambda — it bundles "what to do when clicked" into one package and hands it to the button.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · First taste of lambdas</span><span class="dots">···</span>
:::

```
// The regular way: define a named function and pass it in
fun double(x: Int) = x * 2
val result = listOf(1, 2, 3).map(::double)

// The lambda way: define it inline, quick and direct
val result2 = listOf(1, 2, 3).map { it * 2 }   // it = the current element

// Filter + transform combo (extremely common in real projects)
val bills = listOf(12.5, 88.0, 5.0, 200.0)
val bigBills = bills.filter { it > 50 }.sorted()
// [88.0, 200.0] — "bills over 50, sorted"
```
:::

Memorize a few high-frequency "collection combos": filter, map, sorted, and sum. 90% of the list handling in your future is a combination of these four moves. Kotlin's philosophy: if logic can be said in one sentence, never write five.

#### VII. A Syntax Cheat Sheet for Absolute Beginners

Don't try to memorize every bit of syntax in one day. Save this card, refer to it while you code, and within two weeks it will feel natural:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">What You Want to Do</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">How to Write It</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Define a read-only variable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">val x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Define a mutable variable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Define a function</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">fun name(params): ReturnType { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Decision</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if (condition) {...} else {...}</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Multi-way branch</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">when { condition -> result }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Loop</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for (x in list) { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String interpolation</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Hi, $name"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Handle null</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">x?.length ?: 0</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Define a data class</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">data class X(val a: Int, val b: String)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kotlin Syntax Cheat Sheet (Beginner Edition)

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Hands-On: Play with Kotlin for 10 Minutes, No Install Needed

{class="mt-1"}
Open play.kotlinlang.org in your browser (Kotlin's official online playground), paste in every code snippet from this chapter and run it, tweak the numbers and text, and watch how the output changes. These 10 minutes of "play before learn" will make Chapter 51 twice as easy.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Chapter Summary

- Prefer val, use var sparingly; types can be inferred automatically, or declared explicitly after a colon
- A function = packaged logic; the $ string template is the signature convenience
- if/when to decide, for to repeat; when is Android's all-rounder
- Null safety is Kotlin's life saver: normal types reject null, nullable types must be handled with ? / ?:
- A data class is a box for data, one field per line, used daily in real projects
- 20% of the syntax does 80% of the work: learn to use it first, master it later
:::
