---
id: di-wu-shi-er-zhang
num: 52
part: an-zhuo-kai-fa-pian
nav: 第五十二章：4大コンポーネントとActivityのライフサイクル
toc: default
kind: chapter
---

### 第五十二章：4大コンポーネントとActivityのライフサイクル

{class="chapter-intro mb-4"}
Composeをアプリの「顔」とするなら、この章で扱うのはアプリの「骨格」です。Androidシステムには4つの基本コンポーネントがあり、すべてのアプリはそれらの組み合わせでできています。中でもいちばん大事なActivityには、すべてのAndroid開発者が脳に刻むべき「ライフサイクル図」があります。この章を終えれば、「バックグラウンドに行って戻ったら、なぜアプリの状態が消えているのか」といった永遠の謎が解けるようになります。

#### 1. 4大コンポーネント：Androidの「大黒柱」

Androidは公式に4種類の基本コンポーネントを定めていて、それぞれが1種類の仕事を担います。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">コンポーネント</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">役割</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">たとえるなら</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activity</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">目に見える画面</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">お店の店構え——ユーザーが見て、操作できる部分</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Service</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">バックグラウンドで働く「見えない人」</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">倉庫の作業員——音楽を流す、ファイルをダウンロードする。画面は不要</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BroadcastReceiver</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">システムのブロードキャストを受け取る</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">受付——「電池が残り少ない」「ネットが切れた」を告げるスピーカー</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ContentProvider</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">アプリをまたいでデータを共有</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">共用の資料棚——たとえば連絡先を別のアプリに共有する</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Android 4大コンポーネント早見

初心者のうちは、時間の95%をActivityとの付き合いに使います。ServiceとBroadcastReceiverは音楽再生やプッシュ通知で出番があり、ContentProviderはいちばん登場が少ないです（よく使うデータはシステムがすでにまとめてくれています）。もう1つ大事なこと。4大コンポーネントは、すべてAndroidManifest.xmlに「住民登録」が要ります。登録しないと、システムはそれを見つけられません。

#### 2. Activityのライフサイクル：Android開発で最初の「宝の地図」

スマホのアプリは、いつでも中断され得ます。電話がかかってくる、ユーザーがWeChatの返信に切り替える、メモリが足りなくてシステムに止められる……Activityの一生は、この図の上をぐるぐる巡る旅なのです。

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onCreate（誕生：初期化）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onStart（見えるようになった）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onResume（前面で操作中）</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onPause（一部が隠れた）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onStop（まったく見えない）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center">onDestroy（破棄）</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">🔁 onRestart / onStart / onResume：前面に戻るときは同じ道をたどる</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
図4：Activityのライフサイクル（進む向き：上段が誕生 → 下段が退場。戻るときは同じ道を逆にたどる）
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">コールバック</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">いつ呼ばれる？</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">典型的な用途</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onCreate</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activityが生成されるとき（1回だけ）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UIの読み込み、データの初期化</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStart</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">画面が見える状態になる</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">軽めの処理を始める</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onResume</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">フォーカスを得て、操作できるようになる</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">アニメーションの開始、再生の再開</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onPause</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一部が隠れる／切り替わる瞬間</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">アニメーションの一時停止、下書きの保存</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStop</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">完全に見えなくなる</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">重いリソースの解放、ダウンロードの一時停止</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onDestroy</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">破棄される前</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最後のクリーンアップ</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
6つのライフサイクルコールバックの典型的な用途

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
落とし穴注意：画面回転はActivityを「殺して」しまう

{class="mt-1"}
初心者にいちばん多い失敗例：アプリの画面を回したら、入力欄の文字が全部消えた。原因：画面を回転すると、デフォルトではActivityが破棄されて再び作り直されるためです（onDestroy → onCreate が一巡します）。解決策：rememberSaveable で状態を保存する（Composeでのrememberの代わり）。再生成のときに自動で値を取り戻してくれます。第6・7章で何度も使うことになります。
:::

#### 3. Intent：アプリの内と外をつなぐ「切符」

Intent（インテント）は、コンポーネント同士がやりとりするための「切符」です。ある画面から別の画面へ移動したいときも、ブラウザを開きたいときも、カメラを起動したいときも、必ず「切符を買って乗車」します。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Intentで画面遷移</span><span class="dots">···</span>
:::

```
// 方法その1：明示的Intent——行き先のページをはっきり指定
val intent = Intent(this, DetailActivity::class.java)
intent.putExtra("name", "たろう")     // 車に「荷物」を積むイメージ（データ）
startActivity(intent)

// 方法その2：暗黙的Intent——何をしたいかだけ言う。実行役はシステムが探す
val web = Intent(Intent.ACTION_VIEW, Uri.parse("https://developer.android.com"))
startActivity(web)   // システムがブラウザを開く/または選択させる
```
:::

2つの方式にはそれぞれ役割があります。明示的Intentは自分のアプリ内の画面遷移に、暗黙的Intentはシステムや他アプリの機能を呼び出すとき（Webページを開く、電話をかける、共有するなど）に使います。Composeプロジェクトでは、Composableの中で LocalContext.current でContextを取れば startActivity が使えます。

#### 4. 複数画面とナビゲーション

実際のアプリには複数の画面があります。Composeの公式が推奨するナビゲーション手法はNavigation Compose（依存ライブラリ androidx.navigation）です。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Navigation Composeの骨格</span><span class="dots">···</span>
:::

```
val navController = rememberNavController()

NavHost(navController, startDestination = "home") {
    composable("home") { HomeScreen(navController) }
    composable("detail/{name}") { entry ->
        val name = entry.arguments?.getString("name")
        DetailScreen(name ?: "不明")
    }
}

// ページ内で遷移：
navController.navigate("detail/たろう")     // 引数付き
navController.popBackStack()              // 前のページへ戻る
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ワンポイント：画面が増えてきたら？

{class="mt-1"}
プロジェクトが大きくなったら、すべての画面のルートを1つのファイル（たとえば AppNavGraph.kt）にまとめて一元管理しましょう。「どこへ遷移するか」というロジックが各画面に散らばらないようにするのです。これが「動くもの」から「保守できるもの」へ進む第一歩です。
:::

#### 5. ついでに知っておく：Fragmentとは何か（そして本書で扱わない理由）

古いチュートリアルを読むと必ずFragmentに出会います。FragmentはActivityの中に置ける「再利用できる画面の部品」で、昔ながらの複数画面アーキテクチャでは主役でした。しかしComposeの時代には、画面はComposable関数＋Navigationのルートで足りていて、公式もFragmentの立ち位置を弱めています。そのため本書では本筋に含めていません。

アドバイス：新しいプロジェクトでFragmentを進んで使う必要はありません。ただし古いコードを読むときや、面接で聞かれたときには「Activityに組み込む画面の部品」だと分かっていれば十分です。学習リソースは常に2023年以降のものを優先しましょう。Androidの技術スタックの「古い常識」は、想像以上に速く役目を終えていきます。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
やってみよう：カウンターに「記憶」をつける

{class="mt-1"}
第五十一章のカウンターを改造してみましょう。① remember を rememberSaveable に替え、画面を回転しても数字が残ることを確認する。②「このアプリについて」ボタンを追加し、Navigationで2つ目の画面へ遷移してバージョン番号を表示する。③ 両方の画面の onCreate/onPause にログ出力（Log.d）を入れ、Logcatでライフサイクルが呼ばれる順番を観察する。この3つができれば、ライフサイクルはもう机上の知識ではありません。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章のまとめ

- 4大コンポーネント：Activity（顔）・Service（バックグラウンド）・BroadcastReceiver（スピーカー）・ContentProvider（資料棚）
- ライフサイクルの6つのコールバック：onCreate → onStart → onResume → onPause → onStop → onDestroy
- 画面回転でActivityは破棄・再生成される：rememberSaveableで状態を守る
- Intentは「切符」：明示的は自アプリの画面遷移、暗黙的はシステム機能の呼び出し
- 複数画面はNavigation Composeで：NavHost＋composableルート
:::
