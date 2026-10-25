---
id: di-liu-shi-qi-zhang
num: 67
part: ios-kai-fa-pian
nav: 第六十七章：仕上げとリリース——App Storeへの公開
toc: default
kind: chapter
---

### 第六十七章：仕上げとリリース——テスト、デバッグ、App Store 公開

{class="chapter-intro mb-4"}
App が作れた、そのあとは？この章は「動くもの」から「届けられるもの」へ進むための3つのテーマに答えます。バグを効率よく見つけるデバッグのやり方、デグレを防ぐテストの書き方、そして App を App Store に並べて世界中にダウンロードしてもらう方法。公開は単なるセレモニーではありません——作品を製品に変える分水嶺です。

#### 1. デバッグの基本三ツール：print、ブレークポイント、プレビュー

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ツール</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">できること</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">使い方</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">print + コンソール</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">実行ログを見る</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">コードに print("値=\(x)") と書き、Xcode 下部のコンソールで出力を確認</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ブレークポイントデバッグ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">プログラムを特定の行で止めて変数の値を調べる</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">行番号の横をクリックして青いマークを付けると、そこで実行が止まり、1行ずつ進められます</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI プレビュー + デバッガ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">画面とビュー階層をリアルタイムで確認</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">#Preview のキャンバス + 実行時の View Hierarchy インスペクタ</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
デバッグの基本三ツール

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ワンポイント：クラッシュしたら何を読む？

{class="mt-1"}
Swift がクラッシュすると、コンソールに「Fatal error」と原因が印字され、Xcode はエラーの行で止まってハイライトします。実機での過去のクラッシュは Xcode → Window → Organizer → Crashes で確認できます（有料アカウントが必要）。検索キーワードは「エラー原因の最初の一文 + swiftui」を優先しましょう——正確な問いだけが、正確な答えを引き出します。
:::

#### 2. テスト：コードに保険をかける

手動テストだけでは安心できません——この機能を直したら、別の機能がこっそり壊れていた、というのはよくある話。テストは「後悔しないための薬」であり「防弾チョッキ」です。iOS では XCTest フレームワークを使い、次の2種類に分かれます。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">種類</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">テスト対象</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Target</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">速度</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ユニットテスト</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">純粋なロジック（計算・検証）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppTests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">秒単位</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UI テスト</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">実際の画面のふるまい</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppUITests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分単位</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">手動テスト</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">人間の感覚・体験の確認</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">常に必要</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
iOS のテストの種類（テンプレートプロジェクトには Test Target が2つ用意済み）

::: div .code-block
:::inline div .code-head
<span>SWIFT · ユニットテストの例</span><span class="dots">···</span>
:::

```
import XCTest

// 「金額文字列を数値へ変換」するロジックを純粋関数として切り出す
func parseAmount(_ input: String) -> Double? {
    guard let v = Double(input.trimmingCharacters(in: .whitespaces)),
          v > 0 else { return nil }
    return v
}

final class AmountTests: XCTestCase {
    func testEmptyInputReturnsNil() {
        XCTAssertNil(parseAmount(""))
    }
    func testNegativeReturnsNil() {
        XCTAssertNil(parseAmount("-5"))
    }
    func testNormalValueParses() {
        XCTAssertEqual(parseAmount("12.5"), 12.5)
    }
}
```
:::

テストの実行は ⌘U。全部緑になってからコードをいじれば、自信をもって改修できます。家計簿アプリの金額チェックや合計計算にも、ユニットテストの保護を付けましょう。

#### 3. 署名とパッケージング：App に「認め印」を押す

iOS の App はすべて署名しなければインストールできません——「このパッケージはあなたのもので、改ざんされていない」ことの証明です。階層関係は次のとおり。

- 学習段階：無料の Apple ID + Xcode の自動署名（Personal Team）なら実機でも動かせます。ただし7日ごとの更新が必要。
- 配布段階：有料の開発者アカウント（年間99ドル）が発行する証明書とプロビジョニングプロファイルがあって初めて、公開と長期インストールが可能になります。

パッケージング：Xcode のメニュー Product → Archive でアーカイブを作り、完了したら Organizer で Distribute App → App Store Connect を選んでアップロードします。アーカイブのターゲットは必ず Generic iOS Device に（シミュレータは不可）——ここは初心者がよく忘れる一手です。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
落とし穴注意：証明書を失くす = 更新が途絶える

{class="mt-1"}
署名証明書と秘密鍵を一度失うと、旧 App への更新を配布できなくなります——ユーザーは「真っ新な」アプリを入れ直すしかありません。証明書はキーチェーンから .p12 を書き出すなどしてしっかりバックアップし、パスワードも記録しておきましょう。幸い Apple は「自動署名」とクラウド証明書管理（Xcode の Automatically manage signing にチェック）を用意しており、手作業の落とし穴の大半を回避できます。
:::

#### 4. App Store 公開の全ステップ

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> 開発者アカウントを登録</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> ストア用素材を準備</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> ビルドパッケージをアップロード</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> プライバシーと審査情報を記入</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Appleの審査（1〜7日）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> ストアにリリース</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
図5：App Store 公開の6ステップ
:::

- 登録：developer.apple.com から。個人アカウントは年間99ドル。
- 素材：アイコン（1024×1024。角丸は付けない——Apple が自分で切り取ってくれます）、スクリーンショット（iPhone の各サイズ）、説明文、プライバシーポリシーのリンク。
- プライバシーの設問：収集するデータを正直に申告します——ネットに接続しない家計簿アプリなら「データを一切収集しない」でOK。
- 審査：初回の提出は1〜7日の待ちもよくあります。却下されたら「審査コメント」に沿って1件ずつ修正を——Apple の却下理由は通常とても具体的に書かれているので、指示どおりに対応すれば大丈夫です。
- TestFlight：公開の前にテスト版を友だちに配って内部テストし（最大10,000人）、フィードバックを一巡集めてから正式提出——とてもプロらしい進め方です。

#### 5. ストア素材の作り方：第一印象がダウンロード数を左右する

ストアページは、ユーザーが「店をのぞく」ときに見るショーウィンドーです。第一印象を決めるのは3つの素材。

- アイコン：1024×1024。スクリーンショットで間に合わせないこと。デザインが苦手なら AI ツールでシンプルな図形を生成し、ホーム画面で縮小されてもひと目で判別できるものが合格ライン。
- スクリーンショット：最低2セット（iPhone の主流サイズ）。最も核となる機能の場面を見せ、1枚ごとにひと言のキャプションを添えます（「1秒で記録」は「効率的な家計管理ソリューション」より10倍伝わります）。
- 説明文：最初の一文で「これは何で、誰に使ってほしいのか」をはっきり。「最もプロフェッショナル」「最強」と並べ立てない——誠実さのほうが誇張より効きます。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
やってみよう：家計簿アプリを1回「リリース」してみる

#### 6. クラッシュ報告とパフォーマンス改善のミニチェックリスト

App の公開前に、この2つにはそれぞれ30分を確保する価値があります。

##### 1. クラッシュ監視

自分のテストでクラッシュしなくても、ユーザーの端末では起こるかもしれません。Apple は Xcode の Organizer で無料のクラッシュレポートを提供しています（実機のクラッシュログを見るには有料アカウントが必要）。もっと手軽にやるならサードパーティ SDK（Firebase Crashlytics など）を組み込む方法も。クラッシュ監視なしの公開は、目をつぶったまま車を運転するのと同じです。

##### 2. パフォーマンス自己点検の4項目

1. リストには LazyVStack／List を使う：長いリストを普通の VStack で無理に組まない——遅延読み込みはパフォーマンスの第一課。
2. 画像に原寸を詰め込まない：AsyncImage（リモート画像）とシステムのキャッシュを使う。5MB の元画像ひとつで旧機種は軽く悲鳴を上げます。
3. メインスレッドで重い処理をしない：通信も大きなファイルも async/await に任せる。
4. Instruments で測る：Xcode 内蔵のプロファイラ（Time Profiler、メモリリーク検査）——測ってから最適化。勘で語らないこと。

{class="mt-1"}
① parseAmount などのロジックにユニットテストを3つ追加する（⌘U で緑に）。② ブレークポイントを使い、自分で仕込んだクラッシュを捕まえて直す。③ Product → Archive でパッケージを作り、TestFlight で友だちを内部テストに招待する。④ 余力があれば開発者アカウントを登録して、家計簿アプリを本当に提出・公開する。最初の3つは今夜中に終えられます。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
この章のまとめ

- デバッグの基本三ツール：print ログ、ブレークポイント、SwiftUI プレビューとビューインスペクタ
- XCTest：ユニットテスト（⌘U）+ UI テスト + 手動テスト。テンプレートに最初から用意済み
- 署名：無料アカウントは自動署名（7日ごとに更新）。配布には有料アカウントが必要
- パッケージング：Generic iOS Device + Archive + Distribute。証明書は必ずバックアップ
- 公開の6ステップ：登録 → 素材 → アップロード → プライバシー設問 → 審査 → 公開。まずは TestFlight で内部テスト
:::
