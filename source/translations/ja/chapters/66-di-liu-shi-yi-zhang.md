---
id: di-liu-shi-yi-zhang
num: 61
part: ios-kai-fa-pian
nav: 第六十一章：Swiftにすばやく入門——Apple開発の第一言語
toc: default
kind: chapter
---

### 第六十一章：Swiftにすばやく入門——Apple開発の第一言語

{class="chapter-intro mb-4"}
この章から、いよいよ言語を学びます。緊張しないでください——Swiftは「初心者にやさしい」で有名ですし、文法書を丸暗記する必要もありません。文法の20％をまず押さえれば、日常のコードの80％は読めて書けます。残りはプロジェクトを進めながら調べればOK。私たちの学習の原則を忘れずに：理解する＞暗記する、使える＞完璧。

#### 1. 変数と型：データに名前をつける

プログラムとは「データ＋ロジック」です。変数は、データに名前をつけてしまっておくもの。Swiftではletとvarで宣言します：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 変数</span><span class="dots">···</span>
:::

```
let name = "たろう"        // let：定数（デフォルトはこれがおすすめ）
var age = 18             // var：変数（あとから変えられる）

age = 19                 // <i class="fas fa-check-circle mr-1"></i> varは変えられる
// name = "はなこ"         // <i class="fas fa-times-circle mr-1"></i> letは変えられない。コンパイルエラー

let score: Int = 100     // 型を明示的に書いてもいい
let pi = 3.14            // 書かなくても自動で推論される

print("こんにちは、\(name)")   // 文字列補間：バックスラッシュ + 括弧
```
:::

よく使う型は、この1枚の表で覚えましょう：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">型</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">何を入れるか</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">例</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">整数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">小数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">文字列</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">“こんにちは”</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bool</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真／偽</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[Int]（配列）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">データのまとまり</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[1, 2, 3]</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Swiftのよく使う基本型

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ワンポイント：let優先の原則

{class="mt-1"}
Swiftコミュニティの鉄則：デフォルトはlet、本当に必要なときだけvar。letで足りる場所にvarを使うと、Xcodeが黄色い文字で警告してくれます。この習慣があるだけで、「変数が意図せず書き換わる」系のバグの一大カテゴリを減らせます——変化の少ないコードほど、頭の中で追いやすいのです。
:::

#### 2. オプショナル（Optional）：Swiftの「クラッシュ防止のお守り」

これはSwiftでいちばん重要な概念で、ほかにはありません。ひとことで言えば、値が「存在しない」かもしれないとき、Swiftはあなたに処理させる——「ヌルポインタクラッシュ」という業界の悪夢を、言語レベルで消し去ったのです。

::: div .code-block
:::inline div .code-head
<span>SWIFT · オプショナル</span><span class="dots">···</span>
:::

```
var name: String = "たろう"   // 普通の型：nilは絶対に許されない
// name = nil                // <i class="fas fa-times-circle mr-1"></i> コンパイラが直接止めてくれる

var nickname: String? = nil  // 疑問符を付けると：nilを許す（オプショナル）
nickname = "たーくん"

// オプショナルを使うときは「ほどく」必要がある：
if let n = nickname {        // if let：安全にほどく
    print("こんにちは、\(n)")
} else {
    print("まだニックネームはない")
}

let len = nickname?.count ?? 0   // ?? でデフォルト値（nil結合演算子）
print(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：!は「危険な操作」

{class="mt-1"}
コードにnickname!（強制アンラップ）と書くのは、コンパイラに「nilじゃないって保証する！」と叫ぶのと同じ——外れたらアプリはその場でクラッシュします。初心者のうちはif let / ??を使い、!は使わないのが原則。Xcodeがコードを補完するとき、たまに!を勝手に付けてくるので、直すのを忘れずに。
:::

#### 3. 関数とクロージャ：ロジックを「ボタン」にまとめる

関数は名前のついたロジックのかたまりで、リモコンのボタンのようなもの。クロージャ（Closure）は「名前のない関数」で、その場でほかに渡せます：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 関数とクロージャ</span><span class="dots">···</span>
:::

```
// 関数：名前が先、引数と戻り値の型が後
func greet(name: String) -> String {
    return "こんにちは、\(name)！"
}
print(greet(name: "たろう"))     // 呼び出すときは引数名を付ける

// クロージャ：その場で定義。手軽でストレート
let numbers = [1, 2, 3, 4]
let doubled = numbers.map { $0 * 2 }   // $0 = 現在の要素
// [2, 4, 6, 8]

let big = numbers.filter { $0 > 2 }    // 絞り込み
// [3, 4]
```
:::

SwiftUIではクロージャが至るところに登場します。ボタンのButton("押して") { ... }の後ろの中かっこもクロージャです。map、filter、sortedという「コレクションのコンボ」はしっかり覚えておきましょう——この先のリスト処理の90％は、この組み合わせです。

#### 4. 構造体とプロトコル：Swiftの「レゴ」システム

Swiftの公式のお好みははっきりしています。基本は構造体（struct）で、継承が必要なときだけクラス（class）。構造体は「値型」——コピーすればそれぞれ独立して動くので、ある種のバグが生まれにくいのです：

::: div .code-block
:::inline div .code-head
<span>SWIFT · structとprotocol</span><span class="dots">···</span>
:::

```
// struct：データを入れる箱
struct Record {
    var id = UUID()
    var amount: Double
    var category: String
    var date: Date

    // structは「メンバー逐一イニシャライザ」付き：すぐ作れる
}
let r = Record(amount: 25.5, category: "食費", date: Date())

// protocol：「どんな能力が必須か」の約束
protocol Identifiable {
    var id: UUID { get }
}
struct Record: Identifiable { ... }   // protocolへの準拠 = 要件の実装を約束すること
```
:::

SwiftUIではほぼすべてがstructです（Viewはプロトコル）。いまはピンとこなくて大丈夫。第六十二章で毎日のように顔を合わせます——Swiftの世界では、まずstructを受け入れてしまいましょう。

#### 5. ゼロからの初心者のための文法チートシート

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">やりたいこと</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">書き方</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定数／変数の定義</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">let x = 1</code> / <code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">文字列への値の埋め込み</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">“こんにちは、\(name)”</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">関数の定義</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">func 名前(引数: 型) -> 戻り値の型 { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">条件分岐</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if 条件 { ... } else { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">繰り返し</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for x in 配列 { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">安全なアンラップ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if let x = オプショナル値 { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">デフォルト値</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">x ?? デフォルト値</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">構造体の定義</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X { var a: Int; var b: String }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">クロージャ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">{ $0 * 2 }</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Swift文法チートシート（初心者版）

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
やってみよう：PlaygroundsでSwiftを15分遊ぶ

{class="mt-1"}
MacがあればXcode → Playgroundを開きましょう。なければiPadのSwift Playgroundsや、ブラウザ版のプレイグラウンドでOK。この章の各コードをすべて実行し、数字や文字をいじって、わざとエラーをいくつか起こしてXcodeがどう教えてくれるか見てみてください。この「遊んでから学ぶ」15分のおかげで、第六十二章に入るときのハードルは半分になります。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章のまとめ

- letを優先、varは慎重に。型は自動推論、コロンのあとに明示宣言してもOK
- オプショナルはSwiftの魂：空かもしれないなら必ず処理する。if let / ??はお守り、!は危険な操作
- 関数呼び出しには引数名をつける。クロージャ＝名前のない関数で、SwiftUIでは至るところに登場
- structを優先し、プロトコル（Protocol）に従う。SwiftUIではほぼすべてがstruct
- 文法の20％で仕事の80％：まず使えるようになって、それから極める
:::
