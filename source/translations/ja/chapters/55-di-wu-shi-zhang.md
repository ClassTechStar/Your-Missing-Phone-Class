---
id: di-wu-shi-zhang
num: 50
part: an-zhuo-kai-fa-pian
nav: 第五十章：Kotlinにすばやく入門——Android開発の第一言語
toc: default
kind: chapter
---

### 第五十章：Kotlinはじめの一歩——Android開発の第一言語

{class="chapter-intro mb-4"}
この章で、いよいよ言語そのものを学びます。緊張はいりません。Kotlinは昔から「初心者にやさしい」ことで有名ですし、文法書を丸暗記する必要もありません。文法の2割を押さえるだけで、日常のコードの8割は読めて書けます。残りはプロジェクトを進めながら調べればよいのです。学習の原則を思い出してください。理解する＞暗記する、使える＞完璧、です。

#### 1. 変数と型：データに名前を付ける

プログラムとは「データ＋ロジック」です。変数は、データに名前を付けて保存しておく仕組みのこと。Kotlinには2つの宣言方法があります。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 変数</span><span class="dots">···</span>
:::

```
val name = "たろう"        // val：読み取り専用の変数（デフォルトはこれがおすすめ）
var age = 18             // var：変更できる変数（あとから変えられる）

age = 19                 // <i class="fas fa-check-circle mr-1"></i> varは変えられる
// name = "はなこ"         // <i class="fas fa-times-circle mr-1"></i> valは変えられない。コンパイルエラー

val score: Int = 100     // 型を明示的に書いてもいい
val pi = 3.14            // 書かなくても自動で推論される
```
:::

よく使う型は数えるほど。1枚の表で覚えてしまいましょう。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">型</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">何を入れる？</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">例</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">整数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">小数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">文字列</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"こんにちは"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Boolean</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真/偽</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List&lt; T&gt;</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">データの集まり</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">listOf(1, 2, 3)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kotlinのよく使う基本型

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ワンポイント：val優先の原則

{class="mt-1"}
Kotlinコミュニティの鉄則です。ふだんはvalを使い、本当に必要なときだけvarにする。valで足りる場所にvarを使うと、IDEが黄色い文字で警告してくれます。この習慣だけで「変数が意図せず書き換わる」系のバグのかなりの割合を防げます。コードの動きが少ないほど、頭の中で追いやすいのです。
:::

#### 2. 関数：ロジックを「ボタン」にまとめる

関数とは、名前のついたロジックのひとかたまりです。リモコンのボタンのようなもの——押す（呼び出す）と、一連の動作が実行されます。Kotlinではfunで宣言します。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 関数</span><span class="dots">···</span>
:::

```
fun greet(name: String): String {
    return "こんにちは、$name！"     // $記号で変数を文字列に差し込む
}

println(greet("たろう"))        // 出力：こんにちは、たろう！

// 1行の関数は式として簡潔に書ける
fun add(a: Int, b: Int) = a + b

println(add(3, 5))            // 出力：8
```
:::

ポイントはいくつか。引数はかっこの中に書く（名前が先、型が後、コロンで区切る）。戻り値の型はかっこの後ろに書く。文字列テンプレートの$変数名は、Kotlin名物の便利機能——Javaのように「文字列＋変数」とつなぎ合わせる必要はありません。

#### 3. 条件とループ：プログラムに「考える」力をつける

プログラムの賢さは2つの力から生まれます。判断できること（if/when）と、繰り返せること（for/while）です。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 条件分岐とループ</span><span class="dots">···</span>
:::

```
// 判断：if / else
val age = 17
if (age >= 18) {
    println("大人")
} else {
    println("未成年者")
}

// 多分岐：when（switchの百倍使いやすい）
val score = 85
val level = when {
    score >= 90 -> "優秀"
    score >= 60 -> "合格"
    else -> "その調子！"
}

// 繰り返し：forループ
val fruits = listOf("りんご", "バナナ", "オレンジ")
for (fruit in fruits) {
    println("$fruitが大好き")
}
```
:::

whenはKotlinでいちばんよく使う多分岐の書き方です。Android開発では毎日お世話になります（たとえば状態に応じて別々の画面を出す、など）。

#### 4. Null安全性：Kotlinの「命綱」

Javaの時代でいちばん有名なバグが、NullPointerException（ヌルポインタ例外）です。何も入っていない「空」のものにプログラムがアクセスして、その場でクラッシュします。統計上も、Androidのクラッシュランキングの常連1位です。Kotlinはこれを言語の仕組みレベルで解決しました。デフォルトではnullを許さないのです。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Null Safety</span><span class="dots">···</span>
:::

```
var name: String = "たろう"   // 普通の型：nullは絶対に許されない
// name = null                // <i class="fas fa-times-circle mr-1"></i> コンパイラが直接止めてくれる

var nickname: String? = null // 疑問符を付けると：nullを許す
nickname = "たーくん"

// null許容型を使うときは、安全に扱う必要がある：
println(nickname?.length)    // safe call：nullならnullを返すだけで、落ちない
val len = nickname?.length ?: 0   // Elvis演算子：nullのときはデフォルト値
println(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：?と?:を取り違えない

{class="mt-1"}
String?は「nullを許す」、a ?: bは「aがnullならbを使う」という意味です（形がエルヴィスの髪型に似ているので、Elvis演算子と呼ばれます）。書き始めの頃にコンパイラから「null関連のエラー」が出たら、たいていはnull許容型の扱いを忘れているせいです。それは、言語があなたを守ってくれている合図なのです。
:::

#### 5. クラスとオブジェクト：「部品」を作る鋳型

クラスはオブジェクトの「鋳型」で、オブジェクトはクラスから作った「製品」です。Androidの世界にあるもの——画面、ボタン、データ——は、すべてオブジェクトです。Kotlinにはdata class（データクラス）という便利な道具があり、データを「入れる」ことに特化していて、Javaなら数十行になるのを1行で済ませます。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · クラスとdata class</span><span class="dots">···</span>
:::

```
// 普通のクラス：鋳型
class Dog(val name: String) {
    fun bark() = println("$name ワンワン！")
}

val dog = Dog("ポチ")      // オブジェクトを作る
dog.bark()                 // ポチ ワンワン！

// data class：データを入れる箱（equals/copyなど付き）
data class User(val id: Int, val name: String, val email: String)

val me = User(1, "たろう", "zhangsan@example.com")
val twin = me.copy(name = "たろう丸")   // コピーして1つのフィールドだけ変える
```
:::

この先、おこづかい帳を作るときは、1件の記録がそのままdata classになります。data class Record(val amount: Double, val category: String, val date: String)。ほら、もう本物のプロジェクトのコード構造が書けるのです。

#### 6. ラムダと高階関数：Kotlinの「シンタックスシュガー」

Androidのコードでは、{ ... }という「名前のない関数」を毎日見かけます。これがラムダ（匿名関数）です。ButtonのonClick = { count++ }も1つのラムダで、「クリックされたら何をするか」をひと塊にして、ボタンに手渡しています。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · lambda入門</span><span class="dots">···</span>
:::

```
// 普通の書き方：名前付き関数を定義してから渡す
fun double(x: Int) = x * 2
val result = listOf(1, 2, 3).map(::double)

// lambdaの書き方：その場で定義。手軽でストレート
val result2 = listOf(1, 2, 3).map { it * 2 }   // it = 現在の要素

// 絞り込み + 変換の連携（実際のプロジェクトで非常によくある形）
val bills = listOf(12.5, 88.0, 5.0, 200.0)
val bigBills = bills.filter { it > 50 }.sorted()
// [88.0, 200.0]——「50を超える請求を並べ替え」
```
:::

使用頻度の高い「コレクションの連係技」を覚えましょう。filter（しぼり込み）、map（変換）、sorted（並べ替え）、sum（合計）。この先のリスト処理の90%は、この4つの組み合わせです。Kotlinの哲学はこうです。1言で言い切れるロジックを、5言で書く必要はない。

#### 7. 超初心者向けの文法早見カード

1日で全部の文法を覚えようとしないこと。このカードを保存しておき、コードを書くときに照らし合わせれば、2週間もすれば自然と身につきます。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">やりたいこと</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">書き方</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">読み取り専用の変数を定義</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">val x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">変更できる変数を定義</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">関数を定義</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">fun 名前(引数): 戻り値の型 { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">条件分岐</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if (条件) {...} else {...}</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多分岐</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">when { 条件 -> 結果 }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">繰り返し</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for (x in リスト) { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">文字列の組み立て</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"こんにちは、$name"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">nullの扱い</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">x?.length ?: 0</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">データクラスを定義</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">data class X(val a: Int, val b: String)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kotlin文法早見カード（初心者版）

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
やってみよう：ソフトを1つも入れずに、まずKotlinを10分遊ぶ

{class="mt-1"}
ブラウザでplay.kotlinlang.org（Kotlin公式のオンライン練習場）を開き、この章のコードを順番に貼り付けて実行してみましょう。数字や文字を書き換えて、出力がどう変わるか観察します。この「遊んでから学ぶ」10分のおかげで、第五十一章に入ったときの負担が半分になります。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
この章のまとめ

- valを優先、varは慎重に。型は自動で推論されるが、コロンの後で明示してもよい
- 関数＝まとめたロジック。文字列テンプレートの$はKotlin名物の便利機能
- 判断はif/when、繰り返しはfor。whenはAndroid開発の「何でも屋」
- Null安全性はKotlinの命綱。ふつうの型はnullを拒み、null許容型は?／?:での扱いが必須
- data classはデータを入れる箱。1フィールド1行で、本物のプロジェクトで毎日使う
- 文法の2割で仕事の8割をこなす。まず使えるようになり、それから極める
:::
