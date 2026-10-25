---
id: di-liu-shi-yi-zhang
num: 61
part: ios-kai-fa-pian
nav: 第六十一章：Swift快速上手——蘋果開發嘅第一語言
toc: default
kind: chapter
---

### 第六十一章：Swift 快速上手——蘋果開發嘅第一語言

{class="chapter-intro mb-4"}
呢一章我哋正式學語言。唔使緊張——Swift 係出名「對新手友好」，而且你唔需要背語法書：先掌握 20% 嘅語法，就已經睇得明同寫得出 80% 嘅日常代碼。淨低嘅一邊做項目一邊查。記住我哋嘅學習原則：睇得明 > 記得住，識用 > 精通。

#### 一、變數同類型：畀數據改個名

程式就係「數據 + 邏輯」。變數，就係畀數據改個名儲起佢。Swift 用 let 同 var 嚟聲明：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 變數</span><span class="dots">···</span>
:::

```
let name = "張三"        // let：常量（推薦預設用呢個）
var age = 18             // var：變數（之後仲可以改）

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var 可以改
// name = "李四"         // <i class="fas fa-times-circle mr-1"></i> let 唔可以改，編譯報錯

let score: Int = 100     // 都可以明確寫明類型
let pi = 3.14            // 唔寫都會自動推斷

print("你好，\(name)")   // 字串插值：反斜槓 + 括號
```
:::

常用類型一張表記住：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">類型</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">存乜嘢</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">示例</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">整數</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">小數</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">文字</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"你好"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bool</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真/假</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[Int]（陣列）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一組數據</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[1, 2, 3]</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Swift 常用基礎類型

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：let 優先原則

{class="mt-1"}
Swift 社區嘅鐵律：預設用 let，真係有需要先用 var。可以用 let 嘅地方用 var，Xcode 會出黃字警告你。呢個習慣幫你避開一大類「變數畀人意外改咗」嘅 bug——代碼變化越少，就越容易推理。
:::

#### 二、可選值（Optional）：Swift 嘅"防崩護身符"

呢個係 Swift 最重要嘅概念，冇之一。一句講晒：當一個值可能"唔存在"嗰陣，Swift 會迫你處理佢——喺語言層面消滅咗"空指針崩潰"呢個行業噩夢。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 可選值</span><span class="dots">···</span>
:::

```
var name: String = "張三"   // 普通類型：絕對唔會係 nil
// name = nil                // <i class="fas fa-times-circle mr-1"></i> 編譯錯誤，直接擋住

var nickname: String? = nil  // 加個問號：允許爲 nil（可選值）
nickname = "三兒"

// 用可選值，必須"解包"：
if let n = nickname {        // if let：安全解包
    print("你好，\(n)")
} else {
    print("仲未有暱稱")
}

let len = nickname?.count ?? 0   // ?? 畀預設值（空合運算符）
print(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：! 係"高危操作"

{class="mt-1"}
代碼入面寫 nickname!（強制解包）等於對編譯器嗌"我保證佢唔係 nil"——一估錯，App 就會即場崩潰。新手期原則：盡量用 if let / ??，唔好用 !。Xcode 補全代碼嗰陣有時會順手加個 !，記得改返佢。
:::

#### 三、函數同閉包：將邏輯打包成"按鈕"

函數係一段有名嘅邏輯，好似搖控器上面嘅按鈕。閉包（Closure）就係"冇名嘅函數"，可以隨手遞畀人：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 函數與閉包</span><span class="dots">···</span>
:::

```
// 函數：名字喺前，參數同返回類型喺後
func greet(name: String) -> String {
    return "你好，\(name)！"
}
print(greet(name: "張三"))     // 調用時要帶參數名

// 閉包：就地定義，輕快直接
let numbers = [1, 2, 3, 4]
let doubled = numbers.map { $0 * 2 }   // $0 = 當前元素
// [2, 4, 6, 8]

let big = numbers.filter { $0 > 2 }    // 篩選
// [3, 4]
```
:::

SwiftUI 入面閉包無處不在：按鈕嘅 Button("點我") { ... } 後面嗰對大括號就係一個閉包。map、filter、sorted 呢幾招"集合連招"請記實——將來 90% 嘅列表處理都係佢哋嘅組合。

#### 四、結構體同協議：Swift 嘅"樂高"體系

Swift 官方嘅偏好好明確：優先用結構體（struct），要到需要繼承嗰陣先用類（class）。結構體係"值類型"——複製嗰陣各自各嘅，天然少一類 bug：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 結構體與協議</span><span class="dots">···</span>
:::

```
// 結構體：裝數據嘅盒
struct Record {
    var id = UUID()
    var amount: Double
    var category: String
    var date: Date

    // 結構體自帶"逐一成員構造器"：直接就建到
}
let r = Record(amount: 25.5, category: "餐飲", date: Date())

// 協議：約定"必須具備邊啲能力"
protocol Identifiable {
    var id: UUID { get }
}
struct Record: Identifiable { ... }   // 遵守協議 = 承諾實現其要求
```
:::

SwiftUI 入面幾乎所有嘢都係 struct（View 就係協議）。呢句而家唔明唔緊要，第 62 章會日日見面——喺 Swift 嘅世界入面，先擁抱 struct。

#### 五、寫畀零基礎嘅語法速查卡

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">想做乜嘢</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">寫法</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定義常量／變數</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">let x = 1</code> / <code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">字串插值</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"你好，\(name)"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定義函數</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">func 名字(參數: 類型) -> 返回類型 { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">判斷</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if 條件 { ... } else { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">遍歷</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for x in 陣列 { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">安全解包</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if let x = 可選值 { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">預設值</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">x ?? 預設值</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定義結構體</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X { var a: Int; var b: String }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">閉包</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">{ $0 * 2 }</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Swift 語法速查卡（新手版）

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
嚟動手：喺 Playgrounds 玩 15 分鐘 Swift

{class="mt-1"}
有 Mac 就開 Xcode → Playground；冇 Mac 就用 iPad 上嘅 Swift Playgrounds 或者網頁版演練場。將本章每一段代碼都行一次，改改數字同文字，故意整幾個錯誤睇吓 Xcode 點提示。呢個"先玩後學"嘅 15 分鐘，會令你第 62 章上手嗰陣輕鬆一倍。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- let 優先，var 慎用；類型自動推斷，冒號後面顯式聲明都得
- 可選值係 Swift 嘅靈魂：可能係空就必須處理，if let / ?? 係護身符，! 係高危操作
- 函數調用要帶參數名；閉包 = 冇名嘅函數，SwiftUI 入面無處不在
- 優先 struct，遵守協議（Protocol）；SwiftUI 入面幾乎所有嘢都係 struct
- 20% 語法做 80% 嘅嘢：先用得，再精通
:::
