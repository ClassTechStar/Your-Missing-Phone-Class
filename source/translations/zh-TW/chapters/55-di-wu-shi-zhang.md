---
id: di-wu-shi-zhang
num: 50
part: an-zhuo-kai-fa-pian
nav: 第五十章：Kotlin快速上手——安卓開發的第一語言
toc: default
kind: chapter
---

### 第五十章：Kotlin 快速上手——安卓開發的第一語言

{class="chapter-intro mb-4"}
這一章咱們正式學語言。別緊張——Kotlin 是出了名的"對新手友好"，而且你不需要背語法書：先掌握 20% 的語法，就能看懂和寫出 80% 的日常程式碼。剩下的邊做專案邊查。記住咱們的學習原則：看懂 > 記住，會用 > 精通。

#### 一、變數與型別：給資料起名字

程式就是"資料 + 邏輯"。變數，就是給資料起個名字存起來。Kotlin 有兩種宣告方式：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 變數</span><span class="dots">···</span>
:::

```
val name = "張三"        // val：只讀變數（推薦預設用這個）
var age = 18             // var：可變變數（以後還能改）

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var 可以改
// name = "李四"         // <i class="fas fa-times-circle mr-1"></i> val 不能改，編譯會報錯

val score: Int = 100     // 也可以顯式寫明型別
val pi = 3.14            // 不寫也能自動推斷
```
:::

常用型別就幾種，一張表記住：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">型別</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">存什麼</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">示例</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">整數</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">小數</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">文字</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"你好"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Boolean</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真/假</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List&lt; T&gt;</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一組資料</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">listOf(1, 2, 3)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kotlin 常用基礎型別

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：val 優先原則

{class="mt-1"}
Kotlin 社群的鐵律：預設用 val，確有必要再用 var。能用 val 的地方用 var，IDE 會黃字警告你。這個習慣能幫你少掉一大類"變數被意外修改"的 bug——程式碼越少變化，越容易推理。
:::

#### 二、函式：把邏輯打包成"按鈕"

函式是一段有名字的邏輯，像遙控器上的按鈕——按一下（呼叫），就執行一串動作。Kotlin 裡用 fun 宣告：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 函式</span><span class="dots">···</span>
:::

```
fun greet(name: String): String {
    return "你好，$name！"     // $ 符號把變數插進字串
}

println(greet("張三"))        // 輸出：你好，張三！

// 單行函式可以簡寫成表示式
fun add(a: Int, b: Int) = a + b

println(add(3, 5))            // 輸出：8
```
:::

幾個要點：引數寫在括號裡（名字在前、型別在後，用冒號隔開）；返回型別寫在括號後；字串模板 $變數名 是 Kotlin 的招牌便利——不用再像 Java 那樣"字串 + 變數"地拼來拼去。

#### 三、條件與迴圈：讓程式會"思考"

程式的智慧來自兩件事：會判斷（if/when）和會重複（for/while）。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 條件與迴圈</span><span class="dots">···</span>
:::

```
// 判斷：if / else
val age = 17
if (age >= 18) {
    println("成年人")
} else {
    println("未成年")
}

// 多分支：when（比 switch 好用一百倍）
val score = 85
val level = when {
    score >= 90 -> "優秀"
    score >= 60 -> "及格"
    else -> "再接再厲"
}

// 重複：for 迴圈
val fruits = listOf("蘋果", "香蕉", "橙子")
for (fruit in fruits) {
    println("我愛吃$fruit")
}
```
:::

when 是 Kotlin 裡最常用的多分支寫法，安卓開發裡你會天天用到它（比如根據狀態顯示不同介面）。

#### 四、空安全：Kotlin 的"保命符"

Java 時代最著名的 bug 叫 NullPointerException（空指標異常）——程式訪問了一個"什麼都沒有"的東西，直接崩潰。據統計它是安卓崩潰排行榜的常年第一。Kotlin 從語言層面解決了它：預設不允許空值。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 空安全</span><span class="dots">···</span>
:::

```
var name: String = "張三"   // 普通型別：絕不允許是 null
// name = null                // <i class="fas fa-times-circle mr-1"></i> 編譯錯誤，直接把你攔住

var nickname: String? = null // 加個問號：允許為 null
nickname = "三兒"

// 使用可空型別時，必須安全地處理：
println(nickname?.length)    // 安全呼叫：null 就返回 null，不崩
val len = nickname?.length ?: 0   // Elvis 運運算元：null 時給預設值
println(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：? 和 ?: 別搞混

{class="mt-1"}
String? 是"允許為空"，a ?: b 是"a 為空時用 b"（長得像貓王髮型，所以叫 Elvis 運運算元）。剛開始寫程式碼時，看到編譯器報"null 相關錯誤"，八成是你忘了處理可空型別——這正是語言在保護你。
:::

#### 五、類與物件：造"零件"的模具

類是物件的"模具"，物件是類的"成品"。安卓裡的一切——頁面、按鈕、資料——都是物件。Kotlin 裡有個神器叫 data class（資料類），專門用來"裝資料"，一行頂 Java 幾十行：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 類與資料類</span><span class="dots">···</span>
:::

```
// 普通類：模具
class Dog(val name: String) {
    fun bark() = println("$name 汪汪！")
}

val dog = Dog("旺財")      // 造物件
dog.bark()                 // 旺財 汪汪！

// data class：裝資料的盒子（自動帶 equals/copy 等）
data class User(val id: Int, val name: String, val email: String)

val me = User(1, "張三", "zhangsan@example.com")
val twin = me.copy(name = "張三豐")   // 複製並改一個欄位
```
:::

以後你做記帳本，一筆帳就是一個 data class：data class Record(val amount: Double, val category: String, val date: String)。看，你已經能寫出真實專案的程式碼結構了。

#### 六、lambda 與進階函式：Kotlin 的"語法糖"

安卓程式碼裡你會天天看到 { ... } 這種"沒名字的函式"，它叫 lambda（匿名函式）。Button 的 onClick = { count++ } 就是一個 lambda——把"點選後做什麼"打包成一坨，遞給按鈕。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · lambda 初體驗</span><span class="dots">···</span>
:::

```
// 普通寫法：定義一個有名函式再傳入
fun double(x: Int) = x * 2
val result = listOf(1, 2, 3).map(::double)

// lambda 寫法：就地定義，輕快直接
val result2 = listOf(1, 2, 3).map { it * 2 }   // it = 當前元素

// 篩選 + 變換連招（真實專案裡極常見）
val bills = listOf(12.5, 88.0, 5.0, 200.0)
val bigBills = bills.filter { it > 50 }.sorted()
// [88.0, 200.0]——"超過 50 的帳單，排好序"
```
:::

幾個高頻"集合連招"記一下：filter（篩選）、map（變換）、sorted（排序）、sum（求和）。你未來 90% 的列表處理，都是這四招的組合。Kotlin 的哲學就是：能用一句話說清楚的邏輯，絕不寫五句。

#### 七、寫給零基礎的語法速查卡

別試圖一天背完所有語法。把這張卡存下來，寫程式碼時對照著查，兩週後自然就熟了：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要做什麼</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">寫法</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定義只讀變數</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">val x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定義可變變數</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定義函式</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">fun 名字(引數): 返回型別 { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">判斷</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if (條件) {...} else {...}</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多分支</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">when { 條件 -> 結果 }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">遍歷</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for (x in 列表) { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">字串拼接</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"你好，$name"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">處理可空</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">x?.length ?: 0</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定義資料類</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">data class X(val a: Int, val b: String)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kotlin 語法速查卡（新手版）

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：不裝任何軟體，先玩 10 分鐘 Kotlin

{class="mt-1"}
瀏覽器開啟 play.kotlinlang.org（Kotlin 官方線上演練場），把本章的每一段程式碼都粘進去跑一遍，改改數字和文字，看看輸出怎麼變。這個"先玩後學"的 10 分鐘，會讓你第 51 章上手時輕鬆一倍。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- val 優先，var 慎用；型別可自動推斷，冒號後顯式宣告也行
- 函式 = 打包的邏輯；字串模板 $ 是招牌便利
- if/when 判斷，for 迴圈；when 是安卓開發裡的"多面手"
- 空安全是 Kotlin 的保命符：普通型別拒絕 null，可空型別必須 ? / ?: 處理
- data class 是裝資料的盒子，一個欄位一行，真實專案天天用
- 20% 語法幹 80% 的活：先會用，再精通
:::
