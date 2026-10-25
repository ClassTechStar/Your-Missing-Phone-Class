---
id: di-wu-shi-yi-zhang
num: 51
part: an-zhuo-kai-fa-pian
nav: 第五十一章：UI開発——Jetpack Compose入門
toc: default
kind: chapter
---

### 第五十一章：UI開発——Jetpack Compose入門

{class="chapter-intro mb-4"}
UIとは、ユーザーの目に見えるすべてのものです。Composeが登場する前、AndroidのUIはXMLで書かれていました——穴埋め問題のように面倒な作業です。2021年、GoogleはJetpack Composeを発表しました。Kotlinコードで直接UIを「描く」方式で、書いたものがそのまま形になり、コードを1行変えればプレビューがすぐ更新されます。2026年の今、Composeは新規プロジェクトの揺るぎない主流です。この章では、「お絵描き」を学びます。

#### 1. Composeの発想：UI＝関数

Composeの核心はひと言で言えます。UI＝関数。画面に表示できるもの（文字、ボタン、画像）は、みな「コンポーザブル関数」（Composable）で、@Composableの印を付けます。それらを積み木のように組み重ねたものが、UIなのです。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 初めてのCompose画面</span><span class="dots">···</span>
:::

```
@Composable
fun Greeting(name: String) {
    Text(text = "こんにちは、$name！")     // ひとつの「文字ブロック」
}

// 入れ子の組み合わせ：大きいブロックに小さいブロック
@Composable
fun HomeScreen() {
    Column {                          // 縦に並べる
        Greeting(name = "たろう")
        Greeting(name = "はなこ")
        Button(onClick = { /* 押したら何をするか */ }) {
            Text("押して")
        }
    }
}
```
:::

@Composableという「帽子」に注目してください。コンパイラに「これはUIの積み木ですよ」と伝えるためのものです。積み木は無限に組み合わせられます。それがComposeのすべての秘密です。

#### 2. 基本コンポーネント：文字、ボタン、入力欄、画像

Composeのコンポーネントは「積み木のブロック」です。いちばんよく使う4つを見てみましょう。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">コンポーネント</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">役割</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">必須パラメータ</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">文字を表示</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">text（表示する文字）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ボタン</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onClick（クリック時のコールバック）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">入力欄</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">value、onValueChange（入力変更のコールバック）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">画像を表示</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">painter（画像リソース）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Composeの4大基本コンポーネント

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 基本コンポーネントの例</span><span class="dots">···</span>
:::

```
@Composable
fun BasicWidgets() {
    Column {
        Text(text = "これはテキストです")
        Button(onClick = { println("押された") }) {
            Text("ボタン")
        }
        var input by remember { mutableStateOf("") }
        TextField(
            value = input,
            onValueChange = { input = it },
            label = { Text("何か入力") }
        )
    }
}
```
:::

入力欄の2行に出てきたremember { mutableStateOf("") }——これがComposeの「状態」の魔法です。この章の第5節でじっくり解説します。今は、顔見知りになってもらえれば十分です。

#### 3. レイアウトの3点セット：Column、Row、Box

部品は揃いました。どう並べましょう？「箱」を3つ覚えてください。

- Column：縦に並べる（食堂の行列のように）。
- Row：横に並べる（となり同士で並んで座るように）。
- Box：重ねて置く（トランプを積むように。バッジや重ね表示に便利）。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · レイアウト三種の神器</span><span class="dots">···</span>
:::

```
Column {
    Text("1行目")
    Row {
        Text("左")
        Text("右")
    }
    Box {
        Text("下の層")
        Text("上に重なる小さなバッジ")
    }
}
```
:::

レイアウトをもっと見栄えよくしたい？コンポーネントにModifier（修飾子）を付けましょう——積み木に「メイク」をするようなものです。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Modifierの定番テクニック</span><span class="dots">···</span>
:::

```
Text(
    text = "見栄えのするテキスト",
    modifier = Modifier
        .padding(16.dp)          // 四方に余白
        .fillMaxWidth()          // 幅いっぱいに
        .background(Color.Blue)  // 背景色
        .clickable { /* クリック */ }// クリックできる
)
// チェーン呼び出し：順番に意味がある（先にpadding、後に背景。背景は余白を含まない）
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：Modifierの順番には意味がある

{class="mt-1"}
padding(16.dp).background(Blue)とbackground(Blue).padding(16.dp)は、結果が違います。前者は「先に余白をつくってから塗る」（背景に余白を含まない）、後者は「先に塗ってから余白をつくる」（背景に余白を含む）です。初心者を悩ます「変な白いふち」は、たいていここから生まれます。迷ったら順番を入れ替えて試してみてください。プレビューがすぐ答えを教えてくれます。
:::

#### 4. 状態：UIを「生きている」ものにする

静的なUIでは物足りません。ボタンを押すたびに数字を+1したり、入力欄で文字を打てるようにするには、状態（State）が要ります。Composeのルールはこうです。UIは、常に状態をそのまま写す。状態が変われば、UIは自動で描き直される。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 状態：タップカウンター</span><span class="dots">···</span>
:::

```
@Composable
fun Counter() {
    // remember + mutableStateOf：変わる値を覚えておく
    var count by remember { mutableStateOf(0) }

    Column {
        Text(text = "$count回押しました")
        Button(onClick = { count++ }) {   // 状態を変える
            Text("押して +1")                // 画面は自動更新
        }
    }
}
```
:::

3行のコードで、生きているカウンターのできあがりです。ここが従来の書き方よりComposeが気持ちいいところです。UIを手動で「更新」する必要はなく、データを変えるだけでよい。大事な2つの関数を覚えましょう。remember（画面の再構成で値が消えないようにする）と、mutableStateOf（「この値が変わったら描き直して」とComposeに伝える）です。

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> ユーザーがタップ</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> 状態が変わる（count++）</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> Composeが変化を検知</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> 画面を自動で再描画（再構成）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
図3：Composeの「状態 → UI」一方向データフロー
:::

#### 5. テーマとダークモード：1回の設定で全体に効く

テンプレートプロジェクトにあるMyFirstAppTheme { ... }がテーマです。Material 3のデザイン規格に基づいて、色、フォント、形をまとめて管理してくれます。ダークモード対応は3ステップだけです。

1. テーマの中に、ライト用／ダーク用の2セットの配色を定義する（テンプレートがColorSchemeを自動生成済み）。
2. システムがダークモードに切り替わると、isSystemInDarkTheme()が自動で判定する。
3. 色を直接書かず、テーマが提供する色（MaterialTheme.colorScheme.primaryなど）を使う。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ワンポイント：Material 3のダイナミックカラー

{class="mt-1"}
Android 12からの「Material You」は、アプリが壁紙から色を取り込めるしくみです。Composeテンプレートはデフォルトで対応しています（dynamicColor）。あなたのアプリは、ユーザーごとのスマホで「自動で着替え」ます。これぞ現代Androidのロマンチックなところです。
:::

#### 6. プレビュー、アニメーション、ライブ編集：Composeの「チート機能」

開発体験を上げるComposeの「チート機能」3種。一度使うともう戻れません。

- @Previewプレビュー：Composableに@Previewアノテーションを付けると、Android Studioの右側にすぐUIが表示されます。コードを変えた結果がそのまま見えるので、いちいち実機に入れる必要がありません。
- ライブ編集（Live Edit）：2026年のAndroid Studioでは、エミュレータや実機の画面に一部の変更を「ホット反映」できます。文字の色を変える程度の調整なら、端末上で一瞬で変わります。
- アニメーションAPI：animateFloatAsStateやAnimatedVisibilityなら、数行のコードで要素をなめらかに動かせます。「上級者っぽさ」は、たいていこの数十行の差です。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 10分で身につくアニメーション</span><span class="dots">···</span>
:::

```
@Composable
fun AnimatedBox() {
    var big by remember { mutableStateOf(false) }
    // 値が変わると目標値へ自動でなめらかに遷移
    val size by animateDpAsState(if (big) 120.dp else 60.dp)

    Box(Modifier
        .size(size)
        .background(MaterialTheme.colorScheme.primary)
        .clickable { big = !big }
    )
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ワンポイント：まず機能、アニメーションはそのあと

{class="mt-1"}
初心者がよくやるのは、「UIがまだ正しく動いていないのに、アニメーションを気にし始める」という流れです。まず機能を通るようにして、最後にまとめて動きを足しましょう。これも「シンプル第一」の原則です。アニメーションは花を添えるもの、機能は雪の中の炭です。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
やってみよう：「気分ボタン」を作る

{class="mt-1"}
テンプレートプロジェクトを、気分チェンジャーに改造しましょう。ボタンを1つ置き、押すたびに😀うれしい → 😢かなしい → 😡おこるの間をぐるぐる切り替えて、文字と背景色がそれに合わせて変わるようにします。ヒント：whenで状態ごとに文言と色を選びましょう。できたら友達に送って、最初の「え、アプリ作れるの！？」をいただきましょう。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
この章のまとめ

- Composeの発想：UI＝@Composable関数。積み木のように組み合わせる
- 4大コンポーネント：Text／Button／TextField／Image
- レイアウト3点セット：Columnは縦並び、Rowは横並び、Boxは重ね置き
- Modifierはチェーンで「メイク」：padding、fillMaxWidth、background、clickable——順番に意味がある
- 状態こそ魂：remember＋mutableStateOf。データを変えればUIは自動で描き直される
- テーマはMaterial 3＋ダイナミックカラー。ダークモードは1回の設定で全体に効く
:::
