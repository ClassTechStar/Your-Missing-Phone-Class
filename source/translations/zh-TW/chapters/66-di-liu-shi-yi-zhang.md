---
id: di-liu-shi-yi-zhang
num: 61
part: ios-kai-fa-pian
nav: 第六十一章：Swift快速上手——蘋果開發的第一語言
toc: default
kind: chapter
---

### 第六十一章：Swift 快速上手——蘋果開發的第一語言

{class="chapter-intro mb-4"}
這一章咱們正式學語言。別緊張——Swift 是出了名的"對新手友好"，而且你不需要背語法書：先掌握 20% 的語法，就能看懂和寫出 80% 的日常程式碼。剩下的邊做專案邊查。記住咱們的學習原則：看懂 > 記住，會用 > 精通。

#### 一、變數與型別：給資料起名字

程式就是"資料 + 邏輯"。變數，就是給資料起個名字存起來。Swift 用 let 和 var 宣告：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 變數</span><span class="dots">···</span>
:::

```
let name = "張三"        // let：常量（推薦預設用這個）
var age = 18             // var：變數（以後還能改）

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var 可以改
// name = "李四"         // <i class="fas fa-times-circle mr-1"></i> let 不能改，編譯報錯

let score: Int = 100     // 也可以顯式寫明型別
let pi = 3.14            // 不寫也能自動推斷

print("你好，\(name)")   // 字串插值：反斜槓 + 括號
```
:::

常用型別一張表記住：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">型別</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">存什麼</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">示例</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">整數</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">小數</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">文字</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"你好"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bool</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真/假</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[Int]（陣列）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一組資料</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[1, 2, 3]</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Swift 常用基礎型別

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：let 優先原則

{class="mt-1"}
Swift 社群的鐵律：預設用 let，確有必要再用 var。能用 let 的地方用 var，Xcode 會黃字警告你。這個習慣能幫你少掉一大類"變數被意外修改"的 bug——程式碼越少變化，越容易推理。
:::

#### 二、可選值（Optional）：Swift 的"防崩護身符"

這是 Swift 最重要的概念，沒有之一。一句話：一個值可能"不存在"時，Swift 強迫你處理它——從語言層面消滅了"空指標崩潰"這個行業噩夢。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 可選值</span><span class="dots">···</span>
:::

```
var name: String = "張三"   // 普通型別：絕不允許是 nil
// name = nil                // <i class="fas fa-times-circle mr-1"></i> 編譯錯誤，直接攔住

var nickname: String? = nil  // 加個問號：允許為 nil（可選值）
nickname = "三兒"

// 使用可選值，必須"解包"：
if let n = nickname {        // if let：安全解包
    print("你好，\(n)")
} else {
    print("還沒有暱稱")
}

let len = nickname?.count ?? 0   // ?? 給預設值（空合運算子）
print(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：! 是"高危操作"

{class="mt-1"}
程式碼裡寫 nickname!（強制解包）等於對編譯器喊"我保證它不是 nil"——一旦猜錯，App 當場崩潰。新手期原則：儘量用 if let / ?? ，不用 !。Xcode 補全程式碼時偶爾會順手加 !，記得改掉它。
:::

#### 三、函式與閉包：把邏輯打包成"按鈕"

函式是一段有名字的邏輯，像遙控器上的按鈕。閉包（Closure）則是"沒名字的函式"，可以隨手遞給別人：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 函式與閉包</span><span class="dots">···</span>
:::

```
// 函式：名字在前，引數和返回型別在後
func greet(name: String) -> String {
    return "你好，\(name)！"
}
print(greet(name: "張三"))     // 呼叫時要帶引數名

// 閉包：就地定義，輕快直接
let numbers = [1, 2, 3, 4]
let doubled = numbers.map { $0 * 2 }   // $0 = 當前元素
// [2, 4, 6, 8]

let big = numbers.filter { $0 > 2 }    // 篩選
// [3, 4]
```
:::

SwiftUI 裡閉包無處不在：按鈕的 Button("點我") { ... } 後面的大括號就是一個閉包。map、filter、sorted 這幾個"集合連招"請記牢——未來 90% 的列表處理都是它們的組合。

#### 四、結構體與協議：Swift 的"樂高"體系

Swift 的官方偏好很明確：優先用結構體（struct），需要繼承時才用類（class）。結構體是"值型別"——複製時各過各的，天然少一類 bug：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 結構體與協議</span><span class="dots">···</span>
:::

```
// 結構體：裝資料的盒子
struct Record {
    var id = UUID()
    var amount: Double
    var category: String
    var date: Date

    // 結構體自帶"成員逐一構造器"：直接就能建立
}
let r = Record(amount: 25.5, category: "餐飲", date: Date())

// 協議：約定"必須具備哪些能力"
protocol Identifiable {
    var id: UUID { get }
}
struct Record: Identifiable { ... }   // 遵守協議 = 承諾實現其要求
```
:::

SwiftUI 裡幾乎一切都是 struct（View 就是協議）。這句現在不懂沒關係，第 62 章會天天見面——在 Swift 的世界裡，先擁抱 struct。

#### 五、寫給零基礎的語法速查卡

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要做什麼</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">寫法</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定義常量/變數</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">let x = 1</code> / <code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">字串插值</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"你好，\(name)"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定義函式</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">func 名字(引數: 型別) -> 返回型別 { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">判斷</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if 條件 { ... } else { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">遍歷</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for x in 陣列 { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">安全解包</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if let x = 可選值 { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">預設值</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">x ?? 預設值</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定義結構體</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X { var a: Int; var b: String }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">閉包</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">{ $0 * 2 }</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Swift 語法速查卡（新手版）

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：在 Playgrounds 裡玩 15 分鐘 Swift

{class="mt-1"}
有 Mac 就開啟 Xcode → Playground；沒 Mac 就用 iPad 上的 Swift Playgrounds 或網頁版演練場。把本章每一段程式碼都跑一遍，改改數字和文字，故意製造幾個錯誤看看 Xcode 怎麼提示。這個"先玩後學"的 15 分鐘，會讓你第 62 章上手時輕鬆一倍。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- let 優先，var 慎用；型別自動推斷，冒號後顯式宣告也行
- 可選值是 Swift 的靈魂：可能為空必須處理，if let / ?? 是護身符，! 是高危操作
- 函式呼叫要帶引數名；閉包 = 沒名字的函式，SwiftUI 裡無處不在
- 優先 struct，遵守協議（Protocol）；SwiftUI 幾乎一切都是 struct
- 20% 語法幹 80% 的活：先會用，再精通
:::
