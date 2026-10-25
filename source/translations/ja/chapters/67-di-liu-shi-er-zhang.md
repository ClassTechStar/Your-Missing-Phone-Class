---
id: di-liu-shi-er-zhang
num: 62
part: ios-kai-fa-pian
nav: 第六十二章：UI開発——SwiftUI入門
toc: default
kind: chapter
---

### 第六十二章：画面づくり——SwiftUI入門

{class="chapter-intro mb-4"}
画面とは、ユーザーの目に触れるすべてです。SwiftUIはAppleが2019年に発表した宣言型UIフレームワーク——画面を「宣言」するだけで、描画、ダークモード対応、さまざまな画面への対応はシステムが自動で引き受けます。2026年のいま、SwiftUIは新規プロジェクトの圧倒的な主流です。この章では「お絵かき」を学びましょう。

#### 1. SwiftUIの考え方：宣言型であって命令型ではない

昔ながらの画面づくりは「命令型」です：システムに「ボタンを作る → (20,30)に置く → 色を設定する」と、一歩ずつ指示します。SwiftUIは「宣言型」：「画面には『押して』と書かれた赤いボタンが1つある」と直接記述すれば、どう描くか、いつ描き直すかはシステムが面倒を見てくれます。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 初めてのSwiftUIビュー</span><span class="dots">···</span>
:::

```
import SwiftUI

struct ContentView: View {
    var body: some View {      // body：「画面の見た目」を記述する
        VStack {               // 縦に並べる
            Text("こんにちは、世界！")
                .font(.largeTitle)      // 修飾子：大きな見出し
            Button("押して") {
                print("押された")
            }
            .buttonStyle(.borderedProminent)  // 青い塗りつぶしボタン
        }
        .padding()
    }
}
```
:::

要点：ビュー＝Viewプロトコルに従う構造体。bodyプロパティが画面を記述し、.モディファイア()でつぎつぎ「メイク」していく。これがSwiftUIの基本のすべてです。

#### 2. 基本のビュー：テキスト、ボタン、入力欄、画像

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ビュー</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">役割</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">例</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">文字を表示</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text("こんにちは")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ボタン</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button("押して") { 動作 }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">入力欄</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField("ヒント", text: $テキスト)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">画像を表示</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Image(systemName: "star.fill")</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
SwiftUIの4大基本ビュー

Image(systemName:)に注目——AppleはSF Symbolsというアイコンライブラリを内蔵していて（数千個の無料アイコン）、"star.fill"のような名前を書くだけで、塗りつぶしの星がそのまま表示できます。これぞiOS開発の隠れた特典：画面づくりでは、ほぼアイコン素材探しが不要です。

#### 3. レイアウトの3点セット：VStack、HStack、ZStack

- VStack：縦に並べる（食堂の行列のように）。
- HStack：横に並べる（並んで座るように）。
- ZStack：重ねて置く（トランプを積むように。バッジやオーバーレイにぴったり）。

::: div .code-block
:::inline div .code-head
<span>SWIFT · レイアウト三種の神器 + 定番修飾子</span><span class="dots">···</span>
:::

```
VStack(alignment: .leading, spacing: 12) {
    HStack {
        Text("請求書")
        Spacer()                 // 伸びる空間：右端まで押しやる
        Text("-25.5 元").foregroundColor(.red)
    }
    Divider()                    // 区切り線
    Text("メモ：昼ごはん")
}
.padding(16)                     // 四方に余白
.background(Color(.systemGray6)) // 薄いグレーの地
.cornerRadius(12)                // 角丸

// 修飾子の順番に意味がある：先にpadding、後にbackground。背景は余白を含まない
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：モディファイアの順番には意味がある

{class="mt-1"}
padding(16).background(グレー)とbackground(グレー).padding(16)は結果が違います——前者は「余白を取ってから色を塗る」（背景に余白は含まれない）、後者は「色を塗ってから余白を取る」（背景に余白が含まれる）ためです。初心者にいちばんよくある「変な白いすき間」は、みんなここから来ています。迷ったら順番を入れ替えてみましょう。プレビューがすぐ答えを教えてくれます。
:::

#### 4. 状態とバインディング：画面を「生き」させよう

静的な画面では面白くありません。SwiftUIのルール：画面はつねに状態を忠実に映し出し、状態が変われば画面は自動で描き直されます。

::: div .code-block
:::inline div .code-head
<span>SWIFT · @Stateカウンター</span><span class="dots">···</span>
:::

```
struct CounterView: View {
    @State private var count = 0   // @State：この値が変わったら再描画

    var body: some View {
        VStack {
            Text("\(count)回押しました")
            Button("押して +1") {
                count += 1          // 状態を変えると画面が自動更新
            }
        }
    }
}
```
:::

入力欄には「双方向バインディング」を使います——$マークが「値と書き換え権」をセットで渡してくれます：

::: div .code-block
:::inline div .code-head
<span>SWIFT · @Binding双方向バインディング</span><span class="dots">···</span>
:::

```
struct InputView: View {
    @State private var text = ""

    var body: some View {
        TextField("何か入力", text: $text)  // $による双方向バインディング
            .textFieldStyle(.roundedBorder)
        Text("入力した内容：\(text)")   // 入力中にリアルタイム更新
    }
}
```
:::

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> ユーザー操作</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> 状態が変わる（count += 1）</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> SwiftUIが変化を検知</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> 画面を自動で再描画（bodyの再計算）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
図3：SwiftUIの「状態 → 画面」一方向データフロー
:::

#### 5. プレビュー、テーマ、アニメーション：SwiftUIの「裏ワザ」

- ファイルのいちばん下に#Preview { ContentView() }を足すと、右側のキャンバスがリアルタイムで描画——コードを直すと、見たままがそのまま反映されます。
- ダークモードはタダ：色を直書きせず、システムカラー（Color(.systemGray6)、.primary）を使えばダークモードに自動で対応し、1行も追加で書く必要がありません。
- アニメーションは1行でOK：withAnimation { count += 1 }とするか、ビューに.animation(.default, value: count)を付ける——切り替えがぬるぬる滑らかに。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 10分で身につくアニメーション</span><span class="dots">···</span>
:::

```
struct AnimatedHeartView: View {
    @State private var liked = false

    var body: some View {
        Button {
            withAnimation(.spring(duration: 0.4)) {
                liked.toggle()
            }
        } label: {
            Image(systemName: liked ? "heart.fill" : "heart")
                .font(.system(size: 48))
                .foregroundColor(liked ? .red : .gray)
                .scaleEffect(liked ? 1.3 : 1.0)
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ワンポイント：まず機能、アニメーションはそのあと

{class="mt-1"}
初心者にありがちな失敗は「画面がまだ正しくできていないのに、アニメーションで悩み始める」こと。まず機能を通るようにして、動きは最後にまとめて足しましょう——アニメーションは華やかさの上乗せ、機能は困ったときの命綱です。これも私たちの一貫した「シンプル第一」の原則です。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
やってみよう：「気分ボタン」を作る

#### 6. よく使うモディファイア早見表：この1ページがあれば、画面づくりはもう安心

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">やりたいこと</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">モディファイア</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">余白</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.padding(16)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">角丸</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cornerRadius(12)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">背景色</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.background(Color(.systemGray6))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">フォントと文字サイズ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.font(.title.bold())</code> / <code class="inline">.font(.system(size: 20))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">前景色（文字／アイコン）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.foregroundColor(.red)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">幅いっぱいに広げる</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(maxWidth: .infinity)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">サイズを固定</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(width:100, height: 44)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">そろえ方</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack(alignment: .leading)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不透明度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.opacity(0.6)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">影</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.shadow(radius: 5)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">タップ操作</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.onTapGesture { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">キーボードの種類</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.keyboardType(.decimalPad)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
SwiftUIのよく使うモディファイア早見表

覚えられなくても大丈夫——このページは調べるためのもの。実際にいちばん使うのは、上の4つ：padding、角丸、背景、フォントです。

{class="mt-1"}
テンプレートプロジェクトを「気分チェンジャー」に改造しましょう：ボタンを1つ用意して、タップするたびに😀うれしい → 😢かなしい → 😡おこりの間をぐるぐる切り替え、文字と背景色も連動して変わるようにします。ヒント：3組（文字＋色）を配列に入れ、@Stateにインデックスを保存して、タップのたびに(index + 1) % 3。できたら友だちに送って遊んでもらい、「え、アプリ作れるの？」という最初のリアクションをもらいましょう。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章のまとめ

- SwiftUIは宣言型：どんな見た目かを記述し、描くのも描き直すのもシステムまかせ
- ビュー＝Viewプロトコルに従う構造体。bodyが画面を記述。モディファイアでつぎつぎ「メイク」
- 4大基本ビュー：Text / Button / TextField / Image。SF Symbolsのアイコンライブラリは無料でたっぷり
- レイアウト3点セット：VStackは縦並び、HStackは横並び、ZStackは重ね置き。Spacerは伸び縮みするすき間
- @Stateで画面が生き返る。$の双方向バインディングで入力欄に値を渡す
- #Previewで見たままを確認。システムカラーならダークモードに自動対応。withAnimationで1行アニメーション
:::
