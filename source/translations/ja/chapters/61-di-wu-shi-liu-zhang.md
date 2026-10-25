---
id: di-wu-shi-liu-zhang
num: 56
part: an-zhuo-kai-fa-pian
nav: 第五十六章：仕上げとリリース——Google Playへの公開
toc: default
kind: chapter
---

### 第五十六章：仕上げとリリース——テスト、デバッグ、Google Playへの出品

{class="chapter-intro mb-4"}
アプリができました。それで次は？　この章では「動くもの」から「届けられるもの」へ進むための3つのことを扱います。効率よくデバッグしてバグを見つける方法。テストを書いてデグレを防ぐ方法。そしてアプリをGoogle Playに並べて、世界中にダウンロードしてもらう方法です。出品は儀式ではありません。作品を製品に変える分水嶺です。

#### 1. デバッグの三種の神器：Logcat、ブレークポイント、UIインスペクター

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ツール</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">何をするか</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">使い方</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logcat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">システムや自分が出したログを見る</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">コードで Log.d("TAG","値=$x") と書き、パネルでTAGを検索して絞り込む</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ブレークポイントデバッグ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">プログラムをある行で止めて、変数の値を見る</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">行番号の横をクリックして赤点を出し、Debugモードで実行して1行ずつ進める</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Layout Inspector</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">動いている画面の構造を見る</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">メニューのTools → Layout Inspectorで、コンポーネントツリーをリアルタイムに見る</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
デバッグの三種の神器

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ワンポイント：エラーの読み方

{class="mt-1"}
クラッシュするとLogcatに赤いスタックトレース（Stacktrace）が出ます。下から上へ向かって、自分のパッケージ名で始まる最初の行（たとえば com.example.yourapp）を探します。その行がほぼ現場です。まず「Exceptionの種類」（ヌルポインタ？　型変換？）を見て、次に「at ... 自分のファイル:行番号」を見ます。この技で、クラッシュの8割は解決できます。
:::

#### 2. テスト：コードに保険をかける

手動テストは頼りになりません。ある機能を直したら、別の機能がこっそり壊れていた——そんなことはよくあります。テストは「後悔しないための薬」であり、「防弾チョッキ」です。Androidのテストは3層に分かれています。初心者はまず第1層をしっかり押さえましょう。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">層</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">何をテストするか</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">どこに置くか</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">速さ</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ユニットテスト</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">純粋なロジック（計算、検証）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/test/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">秒単位</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">インストゥルメンテーションテスト</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">実機上での画面の動き</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/androidTest/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分単位</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">手動テスト</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">本物の人間の感覚・体験</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">常に必要</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
テストの3層

::: div .code-block
:::inline div .code-head
<span>KOTLIN · ユニットテストの例</span><span class="dots">···</span>
:::

```
// 「金額文字列を数値へ変換」するロジックを純粋関数として切り出す
fun parseAmount(input: String): Double? {
    val v = input.trim().toDoubleOrNull()
    return if (v != null && v > 0) v else null
}

// テストする（JUnit4）
@Test
fun emptyInputReturnsNull() {
    assertEquals(null, parseAmount(""))
}
@Test
fun negativeReturnsNull() {
    assertEquals(null, parseAmount("-5"))
}
@Test
fun normalValueParses() {
    assertEquals(12.5, parseAmount("12.5"))
}
```
:::

家計簿の金額チェックや集計の計算には、ユニットテストをかぶせておくべきです。テストの実行は、testディレクトリを右クリック → Run。緑で全部通れば、安心してコードを直せます。

#### 3. 署名とパッケージング：アプリに「ハンコ」を押す

Androidでは、すべてのインストールパッケージに署名が必須です。公印を押すのと同じで、「このパッケージは自分が出したもので、改ざんされていない」ことを証明します。デバッグ中はAndroid Studioが自動でdebug署名を使い、リリースでは自分のrelease署名を使います。手順はこうです。

1. メニューのBuild → Generate Signed Bundle / APK を選ぶ。
2. keystoreファイル（キーストア）を作る——パスワードを設定して、大切に保管する。
3. release＋AAB形式を選んで、ビルド完了。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
落とし穴注意：keystoreを失う＝アプリを失う

{class="mt-1"}
出品後のアップデートには、必ず同じ署名を使います。そうしないとストアは更新を拒否します。keystoreファイルとパスワードを一度失うと、新しいアプリとして出し直すしかなく、既存のユーザーはみんなつながらなくなります。keystoreとパスワードは必ず安全な場所（クラウドの暗号化保存＋メモ）にバックアップしてください。Android開発者にとって、いちばん高くつく教訓のひとつです。
:::

#### 4. Google Play出品の全ステップ

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> 開発者アカウントを登録</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> ストア用素材を準備</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> AABをアップロード</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> データセキュリティ表を記入</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> 審査（数時間〜数日）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> ストアにリリース</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
図6：Google Play出品の6ステップ
:::

- 登録：25ドルの一回払いの登録料。使えるGoogleアカウントが必要。
- 素材：アプリのアイコン（512×512）、スクリーンショット（2枚以上）、機能の説明、プライバシーポリシーのリンク（データを集める場合は必須）。
- データセーフティフォーム：どんなデータを集めるかを正直に申告する——ネットにつながらない家計簿なら「ゼロ収集」にできます。
- 審査：新しいアカウントの初出品は、人手による審査になることがよくあります。数時間から数日。差し戻されたら指摘に従って直します。

中国国内の読者へ：Google Playには特別なネット環境が必要で、中国大陸向けの配信は普通、国内ストア（Huawei、Xiaomi、Tencent（応用宝）など）を使います。国内ストアへの出品も流れはよく似ていますが、ストアごとに審査の好みがあります。同じAAB/APKを複数のストアで配信できます。練習としては、まず1つでいいので通せば勝ちです。

#### 5. ストア素材の作り方：第一印象がそのままダウンロード数になる

ストアページは、ユーザーが「お店をのぞく」ときに目にするショーウィンドーです。3つの素材が第一印象を決めます。

- アイコン：512×512。スクリーンショットで代用しないこと。デザインが苦手なら、AIツールでシンプルな幾何学模様を生成しましょう。スマホのホーム画面で小さくしても、一目で見分けられるかが合格ラインです。
- スクリーンショット：2枚以上、できれば4〜6枚で、いちばん核となる機能の場面を見せる。1枚ごとに、自然なひと言を添える（「1秒で1件メモ」は「効率的な家計簿ソリューション」より10倍いい）。
- 説明文：最初の一文で「これが何で、誰のためのものか」をはっきりさせる。「最もプロフェッショナル」「最強」を並べないこと。ストアの検索順位は主にキーワードとダウンロードへの転換で決まります。誠実さのほうが、誇張より効きます。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ワンポイント：A/Bで同業をのぞいてみる

{class="mt-1"}
出品する前に、ストアで同ジャンルの上位10アプリを見て回り、スクリーンショットを取って比べましょう。アイコンはどんなスタイル？　スクリーンショットは何を売りにしている？　タイトルはどう書く？　真似は盗作ではありません。型を学んで、中身を自分のものに替える。これはどんな製品でも、最初の一歩を最速で踏み出すための教訓です。
:::

#### 6. パフォーマンス最適化とクラッシュ報告の小チェックリスト

アプリを出品する前に、この2つにはそれぞれ30分かける価値があります。

##### 1. パフォーマンスのセルフチェック4か条

1. リストはLazyColumn：長いリストをColumnで無理に並べないこと——遅延読み込みは、Androidの性能の最初の一歩です。
2. 画像は元のままで使わない：Coil画像ライブラリで自動的に縮小とキャッシュを行う。5MBの元画像1枚で、ローエンド機は固まってしまいます。
3. メインスレッドで重い仕事をしない：データベース、ネットワーク、大きなファイルは、すべてコルーチンの中で。
4. Profilerで測る：Android Studio内蔵のプロファイラーで、メモリ、CPU、消費電力が見られます。まず測ってから最適化する。感覚に頼らないこと。

##### 2. クラッシュ報告

自分のテストでクラッシュしなくても、ユーザーのスマホでクラッシュしないとは限りません。出品前にFirebase Crashlytics（Google公式、無料）を組み込みましょう。数行の設定で、ユーザーがクラッシュするとスタックトレースが自動で送られ、「どの機種・どのバージョン・どこで落ちたか」が管理画面で分かります。クラッシュ監視なしの出品は、目をつぶって車を運転するのと同じです。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
やってみよう：家計簿を一度「引き渡す」

{class="mt-1"}
① parseAmountなどのロジックにユニットテストを3つ追加する。② Logcatで、自分で仕込んだクラッシュを実際につかまえて直す。③ release署名のAPKを生成して、友人に送ってインストールしてもらう（これこそ「作品」の儀式です）。④ 余裕があれば開発者アカウントを登録して、家計簿を本当に出品する。最初の3つは今夜中にできます。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章のまとめ

- デバッグの三種の神器：Logcatでログ、ブレークポイントで変数、Layout Inspectorで画面
- クラッシュの読み方：スタックトレースを下から上へ、自分のパッケージ名の最初の行を探す
- テストの3層：ユニット（秒単位、まずこれを学ぶ）／インストゥルメンテーション／手動
- リリースには署名が必須：keystoreとパスワードはバックアップ必須。失うとアプリは「別のアプリ」になる
- 出品の6ステップ：登録 → 素材 → AABをアップロード → データセーフティフォーム → 審査 → 出品
:::
