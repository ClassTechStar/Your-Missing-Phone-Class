---
id: di-si-shi-jiu-zhang
num: 49
part: an-zhuo-kai-fa-pian
nav: 第四十九章：開発環境の構築——Android Studioと最初のプロジェクト
toc: default
kind: chapter
---

### 第四十九章：開発環境を整える——Android Studioと最初のプロジェクト

{class="chapter-intro mb-4"}
仕事を仕上げるには、まず道具をととのえること。この章では「キッチン」を組み立てます。Android Studioを入れて、エミュレータを動かし、人生初のAndroidプロジェクトを作り、プロジェクト構造をほどいて覗いてみます。環境が整えば、自分の書いたコードが「押せるボタン」に変わる瞬間に、初めて出会えます——この瞬間を一生覚えているという人は少なくありません。

#### 1. Android Studioをインストールする

Android StudioはGoogle公式の統合開発環境（IDE）です。無料で、機能はフルセット。コードを書く、UIプレビューを見る、デバッグする、パッケージ化する——そのすべてがここに揃っています。インストールは4ステップです。

1. 公式サイトdeveloper.android.com/studioを開き、最新の安定版をダウンロードします（2026年8月時点ではNarwhal以降のバージョン。Windows/Mac/Linux版があります）。
2. インストーラを起動して、ひたすら「次へ」——セットアップウィザードがAndroid SDKとエミュレータのコンポーネントを自動で入れてくれます。
3. 初回起動時に、案内に従ってSDKコンポーネントをダウンロードします（デフォルトのままでOK。数分と数GBの空き容量がいるかもしれません）。
4. 終わるとウェルカム画面が現れます——おめでとうございます、「キッチン」の完成です。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：ハードウェア要件を頭に入れておく

{class="mt-1"}
Android Studioは「メモリを食べる」タイプです。メモリは16GBからがおすすめ（8GBでも動きますが、エミュレータを起動すると重くなりがち）。ディスクは20GB以上確保し、CPUが仮想化対応（BIOSでVT-x/AMD-Vを有効化）か確認しましょう。パソコンがどうしても古い場合は、エミュレータの代わりに「実機デバッグ」を使えば（この章の第4節で解説します）、むしろサクサク動きます。
:::

#### 2. 最初のプロジェクトを作る

ウェルカム画面でNew Projectをクリックし、Empty Activityテンプレート（いちばんすっきりした初心者向けテンプレート）を選んで、3つの項目を入力します。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">設定項目</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">入力する内容</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">説明</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">My First App</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">アプリ名。スマホのホーム画面に表示される</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Package name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example.myfirstapp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">世界で一意の識別子。慣習は「ドメインの逆書き」。まずはデフォルトのままで</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minimum SDK</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API 26（Android 8.0）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最低サポートバージョン。95%以上のデバイスをカバー</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
プロジェクト作成で入力する3つの項目

Finishを押すと、Android StudioがGradleで依存関係を自動ダウンロードし、プロジェクトをビルドします（初回は数分待ちますが、2回目からはぐっと速くなります）。ビルドが終われば、動くアプリの完成です——まだ「Hello Android!」と1行表示するだけですが。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ワンポイント：パッケージ名のツボ

{class="mt-1"}
パッケージ名（package name）はアプリの「身分証番号」のようなもので、世界中で重複が許されず、一度公開したら変更できません。個人の練習ならcom.example.xxxで十分。正式な製品では、自分のドメインの逆書き（com.あなたの名前.アプリ名 など）に変えます。com.exampleのままで公開すると——ストアに拒まれます。
:::

#### 3. 動かしてみる：エミュレータと実機

コードが書けたら、それを動かす「スマホ」が要ります。選択肢は2つ。

##### 1. エミュレータ（Emulator）

エミュレータは、パソコンの中にAndroidスマホを1台仮想で作る仕組みです。Android StudioでDevice Manager → Create Deviceと開き、端末を1台選び（Pixelシリーズがおすすめ）→ システムイメージを1つ選ぶ（Google APIs付きのもの）→ ダウンロード → 起動します。そしてツールバーの緑の三角Runを押せば、数秒後に「スマホ」の画面にあなたのアプリが現れます。

##### 2. 実機デバッグ（こちらがおすすめ）

実機は、常にいちばんリアルなテスト環境です。スワイプの感触も、本物のネットワークも、本物のセンサーも、エミュレータでは真似できません。Androidの実機デバッグは簡単です。

1. スマホで［設定］→［端末情報］を開き、「ビルド番号」を7回連続タップして「開発者向けオプション」を有効にします。
2. ［開発者向けオプション］でUSBデバッグをオンにします。
3. USBケーブルでパソコンにつなぎ、スマホのポップアップで「USBデバッグを許可」を選びます。
4. Android Studioに戻ると、ツールバーのデバイスのドロップダウンにあなたのスマホが現れるので、Runを押します。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
落とし穴注意：USBデバッグはつけっぱなしにしない

{class="mt-1"}
USBデバッグは、パソコンに「裏口」を開けておくようなものです。外で充電するときや、信用できないパソコンにつなぐときは、必ずUSBデバッグをオフにして、他人にデータを読まれないようにしましょう。普段の開発でも、使い終わったらオフにする。それを習慣にしてしまいましょう。
:::

#### 4. プロジェクト構造の解体：各ファイルの役割

プロジェクトを初めて開くと、左のファイルツリーに目が回るかもしれません。慌てないでください。日常の開発では、時間の90%を次のいくつかのファイルだけで過ごすことになります。

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="300" viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="300" fill="#fafafa" rx="8"/>
      <text x="20" y="30" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ プロジェクトのルート</text>
      <rect x="30" y="45" width="540" height="230" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <text x="45" y="70" font-size="11" fill="#4f46e5" font-weight="bold">app/ ← コードを書く場所</text>
      <rect x="60" y="82" width="240" height="178" fill="#eef2ff" rx="5"/>
      <text x="70" y="102" font-size="10" fill="#1e1b4b" font-weight="bold">src/main/</text>
      <text x="80" y="120" font-size="10" fill="#374151">├ java/…/MainActivity.kt  ← ロジックコード</text>
      <text x="80" y="138" font-size="10" fill="#374151">├ res/  ← リソース（画像・文字・色）</text>
      <text x="80" y="156" font-size="10" fill="#374151">└ AndroidManifest.xml  ← アプリの「戸籍簿」</text>
      <text x="70" y="180" font-size="10" fill="#1e1b4b" font-weight="bold">build.gradle.kts</text>
      <text x="80" y="198" font-size="10" fill="#6b7280">依存ライブラリを宣言（SDKバージョン、Composeなど）</text>
      <text x="70" y="222" font-size="10" fill="#1e1b4b" font-weight="bold">src/androidTest/ と test/</text>
      <text x="80" y="240" font-size="10" fill="#6b7280">自動テストコード（第五十六章で使用）</text>
      <rect x="320" y="82" width="230" height="178" fill="#f0fdf4" rx="5"/>
      <text x="330" y="102" font-size="10" fill="#065f46" font-weight="bold">ルートのその他のファイル</text>
      <text x="340" y="122" font-size="10" fill="#374151">gradle/ + gradlew.bat  ← ビルドスクリプト</text>
      <text x="340" y="142" font-size="10" fill="#374151">settings.gradle.kts  ← プロジェクト設定</text>
      <text x="340" y="162" font-size="10" fill="#6b7280">（初心者の合言葉：触っていいのは app/ ディレクトリだけ</text>
      <text x="340" y="180" font-size="10" fill="#6b7280">残りはまず「ブラックボックス」として、むやみに触らない）</text>
      <text x="340" y="208" font-size="10" fill="#9ca3af">.gitignore  ← バージョン管理の除外リスト</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
図2：初心者が必ず知るプロジェクト構造（合言葉：触るのはapp/フォルダだけ）
:::

- MainActivity.kt：アプリの「玄関」です。ユーザーがアイコンをタップすると、最初に目覚めるのがこれ。今のテンプレートでは「Hello Android!」を表示する役割を担っています。
- AndroidManifest.xml：アプリの「住民票」です。このアプリの名前、アイコン、持っている画面、使う権限（カメラ、位置情報など）をここで宣言します。
- res/フォルダ：リソース倉庫。画像、アイコン、文字列、色を置きます。文字をコードに直書きせずリソースファイルに置くのは、Android開発の良い習慣です（言語やテーマの切り替えが楽になります）。
- build.gradle.kts：ビルドのレシピです。最低サポートバージョンや、依存するライブラリ（Composeなど）を宣言します。

#### 5. さっそく試す：「Hello」を自分の名前に変える

MainActivity.ktを開くと、Composeテンプレートが生成したコードが見えます。Text("Hello Android!")という行を探し、引用符の中を自分の名前に変えてみましょう。たとえばText("こんにちは、たろう！これは私の初めてのアプリです")として、Ctrl+R（MacならCmd+R）で再実行します。数秒後、エミュレータにあなたの名前が表示されます。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · MainActivity.kt（この行を変更）</span><span class="dots">···</span>
:::

```
setContent {
    MyFirstAppTheme {
        Surface(modifier = Modifier.fillMaxSize()) {
            // ▼ ここを自分の好きな言葉に変えてみて
            Text("こんにちは、たろう！これは私の初めてのアプリです")
        }
    }
}
```
:::

おめでとうございます。あなたは「コードを変える → コンパイル → インストール → 実行」という1周のサイクルを完了しました。このサイクルこそ、これから毎日の開発の日常です。勢いに乗って、もう少し改造してみましょう。文字を大きくする、色を変える——次の章では、こうした「魔法」の正体を学びます。

#### 6. よくあるエラーの応急処置：初心者の最初2週間の「救急室」

環境構築と初回ビルドの段階では、次の3種類のエラーにぶつかる可能性が高いでしょう。慌てないでください。どれにも効く薬があります。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">エラーの症状</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">よくある原因</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">効く薬</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle sync failed／依存関係のダウンロードが遅い</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">リポジトリへのネットワーク接続が不安定</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradleに国内のミラーリポジトリ（Alibaba Cloud/Tencent Cloudのmavenミラー）を設定する。「Gradle ミラーリポジトリ 設定」などで検索し、手順どおりに直す</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SDKコンポーネントが足りない</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">インストール時にSDKのダウンロードをスキップした</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Settings → SDK Managerで、足りないプラットフォームとツールを追加インストール</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">エミュレータが起動しない／真っ黒な画面</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">仮想化が無効、イメージの破損</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BIOSでVT-x/AMD-Vを有効化。エミュレータを削除して作り直す。または実機デバッグに切り替える</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
初心者向け環境エラー応急処置表

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ワンポイント：エラー検索の方法論

{class="mt-1"}
エラーメッセージの1行目が、いちばん価値のある手がかりです。それをそのまま検索エンジンにコピーし、「android studio」のキーワードを添えましょう。「環境が入らないのですが」といった漠然とした言葉ではなく、「Gradle sync failed: Could not resolve com.android.tools.build」のような具体的なエラー文を検索します。正確な問いにだけ、正確な答えが返ってくるのです。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
やってみよう：「開発の儀式」リストを完成させる

{class="mt-1"}
①Android Studioを入れてエミュレータを動かす。②自分のアプリを実機で1回動かし、スクリーンショットを残す。③Helloの文字を自分の名前に変える。④プロジェクトを圧縮して保存する。この4つが終わったら、友達にこう言えます。「私もAndroid開発者になったよ（証拠写真つきで）」。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
この章のまとめ

- Android Studio＝公式の無料IDE。メモリ16GB＋ディスク20GB＋仮想化の有効化がおすすめ
- 新規プロジェクトの3要素：名前、パッケージ名（世界で一意。com.exampleのまま公開しない）、最低SDK（API 26から）
- 実行方法は2つ：エミュレータ（パソコン内の仮想スマホ）と実機（USBデバッグをオン。使い終わったらオフに）
- プロジェクトの合言葉：触るのはapp/フォルダだけ——MainActivity.ktは玄関、Manifestは住民票、res/はリソース倉庫
- 開発の日常＝コードを変える → Run → 結果を見る、のくり返し
:::
