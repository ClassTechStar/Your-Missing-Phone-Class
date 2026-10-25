---
id: di-wu-shi-qi-zhang
num: 57
part: an-zhuo-kai-fa-pian
nav: 第五十七章：上達への道——権限、通知、モダンアーキテクチャ
toc: default
kind: chapter
---

### 第五十七章：ステップアップへの道——権限、通知、モダンなアーキテクチャ

{class="chapter-intro mb-4"}
アプリが作れるようになるのは、スタートにすぎません。この章では「作れる」から「うまく作れる」へ進むための関門をいくつか扱います。権限を上品に申請する方法。嫌われない通知の出し方。アーキテクチャをもう一段引き上げる方法。そして、2026年のいま、AIと組んでAndroidコードを書く方法です。どれも、実際のプロジェクトですぐに出会うものばかりです。

#### 1. 実行時権限：まずノックして、それから入る

カメラ、位置情報、連絡先、通知……こうした「センシティブな領域」については、Androidはアプリの実行時にユーザーへ申請することを求めます（Android 6から）。ルールはこうです。まず宣言（Manifest）、次に申請（コード）、そして拒否されたら上品に縮小して動くこと。Composeでは公式ライブラリAccompanistの rememberPermissionState を使うのが一番楽です。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · ランタイム権限（Compose版）</span><span class="dots">···</span>
:::

```
// まずManifestに宣言：
// &lt;uses-permission android:name="android.permission.CAMERA" /&gt;

@Composable
fun CameraButton() {
    val permission = rememberPermissionState(
        permission = android.Manifest.permission.CAMERA
    )
    Button(onClick = {
        when {
            permission.status.isGranted -&gt; openCamera()
            permission.status.shouldShowRationale -&gt; showExplainDialog()
            else -&gt; permission.launchPermissionRequest()
        }
    }) { Text("撮影") }
}
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：完全に拒否されたら？

{class="mt-1"}
ユーザーが「今後表示しない」を選ぶと、launchPermissionRequest はもうダイアログを出しません。その場合は、Intentでアプリ設定のページへ飛ばして、システム設定から手動で有効にするよう誘導し、画面で「この権限を何に使うのか」を説明します。態度を丁寧にすれば、ユーザーが権限を許可してくれる気持ちもぐっと高まります。権限申請の文面は、真剣に書く価値があります。
:::

#### 2. 通知：正しいタイミングで、役に立つことを伝える

通知はアプリからユーザーへ届く経路であると同時に、ユーザーに「ブロック」されやすい機能でもあります。通知を出す3つの規律。役に立つことだけ送る。ユーザーが切れるようにする。真夜中に攻めない。基本の使い方はこうです。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 通知を送る</span><span class="dots">···</span>
:::

```
// Android 13+では先にPOST_NOTIFICATIONS権限を申請する必要がある（前の節を参照）

// 1. 通知チャンネルを作成（Android 8+で必須）
val channel = NotificationChannel(
    "reminder", "リマインダー", NotificationManager.IMPORTANCE_DEFAULT
)
val manager = getSystemService(NotificationManager::class.java)
manager.createNotificationChannel(channel)

// 2. 通知を送る
val notification = NotificationCompat.Builder(this, "reminder")
    .setSmallIcon(R.drawable.ic_notification)
    .setContentTitle("記帳リマインダー")
    .setContentText("今日はまだ記帳していないよ")
    .setPriority(NotificationCompat.PRIORITY_DEFAULT)
    .build()
if (ActivityCompat.checkSelfPermission(this,
        Manifest.permission.POST_NOTIFICATIONS) == PackageManager.PERMISSION_GRANTED
) {
    manager.notify(1, notification)
}
```
:::

定期タスク（たとえば「毎日20:00に記録を促す」）にはWorkManagerを使います。公式おすすめの「バックグラウンド調整の執事」で、タスクが適切なタイミングで実行されることを保証してくれ、バッテリー最適化を自分で気にする必要がありません。目覚まし系の要望には、これで間違いありません。

#### 3. アーキテクチャのステップアップ：依存性注入とモジュール化

プロジェクトが大きくなると、2つの「うれしい悩み」がやってきます。

- オブジェクトの生成が乱れる：各画面が自分でデータベースをnewし、APIをnewする——Hilt（依存性注入フレームワーク）で一元管理して、「誰が何を欲しければ、口を開けば渡してくれる」ようにする。
- コードが山になる：単一モジュールのプロジェクトは、直すたびに遅くなる——マルチモジュール（app / core / feature-xxx）に分割して、機能ごとに独立して開発・テストする。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ワンポイント：設計しすぎない

{class="mt-1"}
Hiltもモジュール化も良い道具ですが、個人プロジェクトなら急いで導入しないこと。家計簿は単一モジュール＋依存の手動生成で十分です。コードが数万行を超えて、ビルドが遅くなり、複数人で作業するようになったら、必要に応じて入れましょう。道具は目的のためにあるのであって、見せびらかすためではありません。これが本書で言う「シンプル至上主義」の原則です。
:::

#### 4. 2026年の新しいやり方：AI支援のAndroid開発

2026年、AIはすでにAndroid開発の流れの中に深く入り込んでいます。作業を速くしたいなら、この連携プレーがとても固まっています。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">段階</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">AIの助け方</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">あなたの役割</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">コードを書く</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio内蔵のGeminiやサードパーティAIプラグインで補完・生成</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">要件をはっきり説明し、成果物をチェックする</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">調べ物</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">公式ドキュメントやエラー情報をAIに渡して解説してもらう</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">大事な結論は公式ドキュメントで確認する</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">テストを書く</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AIに「正常／境界／異常」の3種類でテストケースを生成させる</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">テストケースが業務の意味に合っているか確認する</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">バグを直す</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">スタックトレース＋関係するコードを貼って、AIが原因の特定と修正を行う</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">変更内容を理解し、テストを実行して確認する</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
AI支援Android開発の4つの場面

具体的な方法論——AIへの指示の出し方、検収のやり方、落とし穴の避け方——は、本書第7部『AIプログラミング実戦編』（第37〜47章）に全11章でまとまっています。あわせて読むことを強くおすすめします。Androidの文法は本編で、AIとの協働のコツは第7部で、と分担してください。

#### 5. Composeの性能最適化とデバッグツール

Composeは書いていて気持ちいいものの、「再構成のしすぎ」で重くなることもあります。実用的な技を3つ。

- パラメータを安定させる：データクラスに @Immutable を付けるか、derivedStateOf を使って、関係のない状態変化で広範囲の再構成が起きるのを防ぐ。
- keyを忘れない：items(list, key = { it.id }) とすれば、リストの追加・削除のときに動かすべき項目だけが動きます。keyがないと、1項目の削除で表全体が描き直されることもあります。
- Layout InspectorのComposeモード：各Composableの再構成回数をリアルタイムに見られます。どれが頻繁に再構成されているか一目瞭然なので、その重点箇所を狙って最適化します。

さらにComposeコンパイラのレポート（Metrics）を有効にすると、「どのコンポーネントが不安定か」のレポートが生成できます。ステップアップの道では、データのほうが感覚よりいつでも信頼できます。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
やってみよう：家計簿に「三種の神器」を追加する

{class="mt-1"}
① 家計簿に「毎日20:00の記録リマインダー」を追加する（WorkManager＋通知チャネル＋Android 13の通知権限）。② データベースとAPIの生成を、Hiltによる注入に替える。③ AIツールを使って「月別フィルター」機能の実装を速めてみて、3層検収の方法で成果物をチェックする。3つそろえば、あなたのプロジェクトも「正規軍」らしくなります。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章のまとめ

- センシティブな権限：Manifestで宣言＋実行時に申請＋拒否されたら上品に誘導
- 通知の3規律：役に立つものだけ、切れる、攻めない。チャネル＋権限のどちらも必須
- 定期タスクはWorkManager。車輪の再発明をしない
- オブジェクトはHilt、コードはモジュール化——個人プロジェクトでは急いで導入しない
- AI支援の4場面：コード作成、調べ物、テスト作成、バグ修正。方法論は第7部（第37〜47章）を参照
:::
