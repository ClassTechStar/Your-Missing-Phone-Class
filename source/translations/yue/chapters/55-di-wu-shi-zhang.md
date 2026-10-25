---
id: di-wu-shi-zhang
num: 50
part: an-zhuo-kai-fa-pian
nav: 第五十章：Kotlin快速上手——安卓開發嘅第一語言
toc: default
kind: chapter
---

### 第五十章：Kotlin 快速上手——安卓開發嘅第一語言

{class="chapter-intro mb-4"}
呢一章我哋正式學語言。唔使緊張——Kotlin 係出名「對新手友好」，而且你唔需要死背文法書：先掌握 20% 嘅文法，就可以睇得明同寫得出 80% 嘅日常程式碼。剩低嘅就邊做項目邊查。記住我哋嘅學習原則：睇得明 > 記得住，用得到 > 精通。

#### 一、變數同類型：畀資料改個名

程式就係「資料 + 邏輯」。變數，就係畀資料改個名儲起。Kotlin 有兩種聲明方式：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 變數</span><span class="dots">···</span>
:::

```
val name = "張三"        // val：只讀變數（推薦預設用呢個）
var age = 18             // var：可變變數（之後仲可以改）

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var 可以改
// name = "李四"         // <i class="fas fa-times-circle mr-1"></i> val 不能改，編譯會報錯

val score: Int = 100     // 都可以明確寫明類型
val pi = 3.14            // 唔寫都會自動推斷
```
:::

常用類型就得幾種，一張表記住：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">類型</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">存乜嘢</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">示例</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">整數</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">小數</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">文字</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">「你好」</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Boolean</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真／假</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List&lt; T&gt;</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一組資料</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">listOf(1, 2, 3)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kotlin 常用基礎類型

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：val 優先原則

{class="mt-1"}
Kotlin 社區嘅鐵律：預設用 val，真係有需要先用 var。用得 val 嘅地方用咗 var，IDE 會用黃字警告你。呢個習慣可以幫你避開一大類「變數被意外改咗」嘅 bug——程式碼變化越少，越容易推理。
:::

#### 二、函數：將邏輯打包成「掣」

函數係一段有名嘅邏輯，好似遙控器上面嘅掣——撳一下（調用），就執行一串動作。Kotlin 入面用 fun 聲明：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 函數</span><span class="dots">···</span>
:::

```
fun greet(name: String): String {
    return "你好，$name！"     // $ 符號把變數插進字串
}

println(greet("張三"))        // 輸出：你好，張三！

// 單行函數可以簡寫成表達式
fun add(a: Int, b: Int) = a + b

println(add(3, 5))            // 輸出：8
```
:::

幾個要點：參數寫喺括號入面（名喺前、類型喺後，用冒號隔開）；返回類型寫喺括號後面；字串模板 $變數名 係 Kotlin 嘅招牌便利——唔使再好似 Java 咁將「字串 + 變數」拼嚟拼去。

#### 三、條件同循環：畀程式識「思考」

程式嘅智能嚟自兩樣嘢：識判斷（if/when）同識重複（for/while）。

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
    println("我愛喫$fruit")
}
```
:::

when 係 Kotlin 入面最常用嘅多分支寫法，安卓開發入面你會日日都用佢（例如根據狀態顯示唔同介面）。

#### 四、空安全：Kotlin 嘅「保命符」

Java 年代最出名嘅 bug 叫 NullPointerException（空指標異常）——程式訪問咗一個「乜嘢都冇」嘅嘢，即場崩潰。統計指出佢係安卓崩潰排行榜嘅常年第一名。Kotlin 喺語言層面解決咗佢：預設唔允許空值。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 空安全</span><span class="dots">···</span>
:::

```
var name: String = "張三"   // 普通類型：絕對唔會係 null
// name = null                // <i class="fas fa-times-circle mr-1"></i> 編譯錯誤，直接將你擋住

var nickname: String? = null // 加個問號：允許爲 null
nickname = "三兒"

// 用可空類型嗰陣，必須安全咁處理：
println(nickname?.length)    // 安全調用：null 就返回 null，唔會崩
val len = nickname?.length ?: 0   // Elvis 操作符：null 時畀預設值
println(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：? 同 ?: 唔好撈亂

{class="mt-1"}
String? 係「允許為空」，a ?: b 係「a 為空嗰陣就用 b」（個樣好似貓王髮型，所以叫 Elvis 操作符）。啱啱開始寫程式碼嗰陣，見到編譯器報「null 相關錯誤」，十居其九係你唔記得咗處理可空類型——呢個正正係語言喺度保護你。
:::

#### 五、類同對象：整「零件」嘅模具

類係對象嘅「模具」，對象係類嘅「成品」。安卓入面嘅所有嘢——頁面、按鈕、資料——都係對象。Kotlin 入面有個神器叫 data class（資料類），專門用嚟「裝資料」，一行頂 Java 幾十行：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 類與數據類</span><span class="dots">···</span>
:::

```
// 普通類：模具
class Dog(val name: String) {
    fun bark() = println("$name 汪汪！")
}

val dog = Dog("旺財")      // 整物件
dog.bark()                 // 旺財 汪汪！

// data class：裝數據嘅盒（自動帶 equals/copy 等）
data class User(val id: Int, val name: String, val email: String)

val me = User(1, "張三", "zhangsan@example.com")
val twin = me.copy(name = "張三豐")   // 複製並改一個字段
```
:::

第日你做記賬本，一筆賬就係一個 data class：data class Record(val amount: Double, val category: String, val date: String)。睇，你已經寫得出真實項目嘅程式碼結構喇。

#### 六、lambda 同高階函數：Kotlin 嘅「語法糖」

安卓程式碼入面你會日日都見到 { ... } 呢種「冇名嘅函數」，佢叫 lambda（匿名函數）。Button 嘅 onClick = { count++ } 就係一個 lambda——將「撳完之後做乜嘢」打包成一嚿，遞畀個按鈕。

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

// 篩選 + 變換連招（真實項目入面極常見）
val bills = listOf(12.5, 88.0, 5.0, 200.0)
val bigBills = bills.filter { it > 50 }.sorted()
// [88.0, 200.0]——"超過 50 嘅賬單，排好曬序"
```
:::

幾個高頻「集合連招」記住佢：filter（篩選）、map（變換）、sorted（排序）、sum（求同）。你將來 90% 嘅列表處理，都係呢四招嘅組合。Kotlin 嘅哲學就係：一句話講得清楚嘅邏輯，就絕對唔寫五句。

#### 七、寫畀零基礎嘅文法速查卡

唔好諗住一日背曬所有文法。將呢張卡儲低，寫程式碼嗰陣對照住查，兩個禮拜之後自然就熟：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要做乜嘢</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">寫法</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定義唯讀變數</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">val x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定義可變變數</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定義函數</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">fun 名字(參數): 返回類型 { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">判斷</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if (條件) {...} else {...}</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多分支</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">when { 條件 -> 結果 }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">遍歷</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for (x in 列表) { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">字串拼接</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">「你好，$name」</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">處理可空</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">x?.length ?: 0</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定義資料類</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">data class X(val a: Int, val b: String)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kotlin 文法速查卡（新手版）

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
嚟動手：唔使裝任何軟件，先玩 10 分鐘 Kotlin

{class="mt-1"}
瀏覽器打開 play.kotlinlang.org（Kotlin 官方線上演練場），將本章每一段程式碼都貼入去行一次，改嚇數字同文字，睇嚇輸出點樣變。呢個「先玩後學」嘅 10 分鐘，會令你第 51 章上手嗰陣輕鬆一倍。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- val 優先，var 慎用；類型可以自動推斷，冒號後面顯式聲明都得
- 函數 = 打包咗嘅邏輯；字串模板 $ 係招牌便利
- if/when 判斷，for 循環；when 係安卓開發入面嘅「多面手」
- 空安全係 Kotlin 嘅保命符：普通類型拒絕 null，可空類型必須用 ? / ?: 處理
- data class 係裝資料嘅盒，一個欄位一行，真實項目日日都用
- 20% 文法做 80% 嘅嘢：先用得，再精通
:::
