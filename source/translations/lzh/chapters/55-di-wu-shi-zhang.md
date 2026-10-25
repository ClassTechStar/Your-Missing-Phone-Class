---
id: di-wu-shi-zhang
num: 50
part: an-zhuo-kai-fa-pian
nav: 第五十章：Kotlin快速上手——安卓開發之第一語言
toc: default
kind: chapter
---

### 第五十章：Kotlin 速成——安卓開發之首語

{class="chapter-intro mb-4"}
此章吾儕始正學其語。勿怯——Kotlin 素以待新手甚善稱，且汝毋須背語法之書：先通其百分之二十之語法，則能曉且書日常代碼之百分之八十。其餘者，且作項目且查之可也。記吾儕為學之則：曉之 > 記之，能用 > 精熟。

#### 一、變量與類型：為數據命名

程序者，「數據 + 邏輯」也。變量者，與數據命一名而儲之也。Kotlin 有二聲明之法：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 變量</span><span class="dots">···</span>
:::

```
val name = "張三"        // val：唯讀變量（宜以為默認）
var age = 18             // var：可變變量（後尚可改）

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var 可改
// name = "李四"         // <i class="fas fa-times-circle mr-1"></i> val 不能改，編譯會報錯

val score: Int = 100     // 亦可明書其型
val pi = 3.14            // 不書亦自推之
```
:::

常用之類不過數種，一表可記：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">類型</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">所儲何物</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">示例</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">整數</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">小數</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">文字</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">「汝好」</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Boolean</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真/偽</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List&lt; T&gt;</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一組數據</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">listOf(1, 2, 3)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kotlin 常用基礎類型

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小識：val 為先之則

{class="mt-1"}
Kotlin 社區之鐵律：常則用 val，誠有必要方用 var。可用 val 處而用 var，IDE 將以黃字警汝。此習能免汝一大類「變量遭意外改易」之 bug——代碼愈少變，愈易推演。
:::

#### 二、函數：束邏輯為「按鈕」

函數者，有名之邏輯一段也，猶遙控器上之鈕——按之（調用），則行一串之動。Kotlin 以 fun 聲明：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 函數</span><span class="dots">···</span>
:::

```
fun greet(name: String): String {
    return "汝好，$name！"     // $ 符插變量於字串
}

println(greet("張三"))        // 輸出：汝好，張三！

// 單行函數可簡寫成表達式
fun add(a: Int, b: Int) = a + b

println(add(3, 5))            // 輸出：8
```
:::

數要點：參數書於括中（名於前、類於後，以冒號隔之）；返回之類書於括後；字符串模板 $變量名 者，Kotlin 招牌之便也——不必如 Java 之「字符串 + 變量」輾轉相拼矣。

#### 三、條件與循環：使程序能「思」

程序之智出於二事：能判斷（if/when）與能重複（for/while）。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 條件與循環</span><span class="dots">···</span>
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

// 重複：for 循環
val fruits = listOf("蘋果", "香蕉", "橙子")
for (fruit in fruits) {
    println("吾好食$fruit")
}
```
:::

when 者，Kotlin 最常用之多分支寫法也，安卓開發之中汝將日日用之（譬如依狀態而顯不同之界面）。

#### 四、空安全：Kotlin 之「保命符」

Java 之世，至著名之 bug 曰 NullPointerException（空指針之異）——程序觸一「空無所有」之物，遂崩。稽諸統計，其恆居安卓崩潰之榜首。Kotlin 自語言之層決之：常則不許空值。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 空安全</span><span class="dots">···</span>
:::

```
var name: String = "張三"   // 普通之型：決不容為 null
// name = null                // <i class="fas fa-times-circle mr-1"></i> 編譯之誤，徑阻汝

var nickname: String? = null // 加問號：許為 null
nickname = "三兒"

// 用可空之型，必安處之：
println(nickname?.length)    // 安全調用：null 則返 null，不崩
val len = nickname?.length ?: 0   // Elvis 運算符：null 時予默認值
println(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
慎之：? 與 ?: 勿混

{class="mt-1"}
String? 者，「許其為空」也；a ?: b 者，「a 空則用 b」也（形似貓王之髮，故號 Elvis 操作符）。初書代碼時，見編譯器報「null 之誤」，十有八九乃汝忘處可空之類——此正語言之護汝也。
:::

#### 五、類與對象：造「零件」之模

類者，對象之「模」也；對象者，類之「成品」也。安卓中萬物——頁面、按鈕、數據——皆對象也。Kotlin 有神器曰 data class（數據類），專以盛數據，一行可抵 Java 數十行：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 類與數據類</span><span class="dots">···</span>
:::

```
// 普通類：模具
class Dog(val name: String) {
    fun bark() = println("$name 汪汪！")
}

val dog = Dog("旺財")      // 造物件
dog.bark()                 // 旺財 汪汪！

// data class：盛數據之盒（自動帶 equals/copy 等）
data class User(val id: Int, val name: String, val email: String)

val me = User(1, "張三", "zhangsan@example.com")
val twin = me.copy(name = "張三豐")   // 複製並改一個字段
```
:::

他日汝作記賬之冊，一筆之賬即一 data class：data class Record(val amount: Double, val category: String, val date: String)。觀之，汝已能書真實項目代碼之構矣。

#### 六、lambda 與高階函數：Kotlin 之「語法糖」

安卓代碼之中，汝將日日見 { ... } 此類「無名之函」，為曰 lambda（匿名函數）。Button 之 onClick = { count++ } 即一 lambda——束「點而後何為」為一團，以授於鈕。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · lambda 初體驗</span><span class="dots">···</span>
:::

```
// 普通寫法：定義一個有名函數再傳入
fun double(x: Int) = x * 2
val result = listOf(1, 2, 3).map(::double)

// lambda 寫法：就地定義，輕快直接
val result2 = listOf(1, 2, 3).map { it * 2 }   // it = 當前元素

// 篩選 + 變換連招（真實項目裏極常見）
val bills = listOf(12.5, 88.0, 5.0, 200.0)
val bigBills = bills.filter { it > 50 }.sorted()
// [88.0, 200.0]——"逾 50 之賬單，序之"
```
:::

高頻「集合連招」數者宜記：filter（篩選）、map（變換）、sorted（排序）、sum（求與）。汝異日列表之理，百分之九十皆此四招之合。Kotlin 之哲曰：可一語明之之邏輯，決不書五語。

#### 七、貽零基者之語法速查卡

勿欲一日盡背語法。藏此卡，書代碼時對而查之，二旬之後自熟矣：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">欲為何事</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">寫法</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定唯讀之變量</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">val x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定可變之變量</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定函數</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">fun 名(參數): 返回類型 { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">判斷</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if (條件) {...} else {...}</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多分支</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">when { 條件 -> 結果 }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">遍歷</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for (x in 列表) { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">字符串拼接</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">「汝好，$name」</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">處可空者</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">x?.length ?: 0</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定數據類</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">data class X(val a: Int, val b: String)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kotlin 語法速查卡（新手之版）

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：不裝任何軟件，先玩 Kotlin 十分鐘

{class="mt-1"}
以瀏覽器啟 play.kotlinlang.org（Kotlin 官家線上演武之場），粘本章每段代碼而運之一遭，易其數與文，觀所出如何變。此「先玩後學」之十分鐘，將使汝至第五十一章上手之時，其易倍之。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- val 為先，var 慎用；類可自動推之，冒號後顯而聲明亦可
- 函數 = 束成之邏輯；字符串模板 $ 為招牌之便
- if/when 以判，for 以循；when 者，安卓開發之「多面手」也
- 空安全者，Kotlin 之保命符也：常類拒 null，可空之類必以 ? / ?: 處之
- data class 者，盛數據之匣也，一字段一行，真實項目日日用之
- 百分之二十之語法，成百分之八十之功：先用之，後精之
:::
