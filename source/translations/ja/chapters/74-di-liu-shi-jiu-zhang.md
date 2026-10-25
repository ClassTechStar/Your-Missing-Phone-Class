---
id: di-liu-shi-jiu-zhang
num: 69
part: ios-kai-fa-pian
nav: 第六十九章：クイックリファレンスとリソース
toc: default
kind: chapter
---

### 第六十九章：クイックリファレンスと学習リソース

{class="chapter-intro mb-4"}
この章は、それ単体で使えるクイックリファレンスです。書き方を思い出せないときや、すばやく判断したいときは、直接ここを開きましょう。「ポケットカード」として活用するのがおすすめです。よく使うコードの一覧、よくある質問、学習リソース——この3つをまるごと収めています。

#### 1. よく使うコードのクイックカード

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">やりたいこと</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">キーコード</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">画面内のプライベートな状態</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State private var x = 初期値</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">画面をまたぐロジック</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Observable class VM { var x = 0 }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">縦並び／横並びのレイアウト</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack { }</code> / <code class="inline">HStack { }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">伸縮する余白</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Spacer()</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">リスト</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List { ForEach(配列) { ... } }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">画面遷移</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">NavigationStack + NavigationLink</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ボトムシート</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">.sheet(isPresented: $show) { 中身 }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">現在の画面を閉じる</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Environment(\.dismiss) var dismiss</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ネットワークからデータを取得</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">try await URLSession.shared.data(from: url)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">JSON のパース</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X: Codable</code> + <code class="inline">JSONDecoder().decode</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">小さな設定を保存</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults.standard.set(値, forKey: "キー")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">構造化データを保存</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Model</code> + <code class="inline">modelContainer</code> + <code class="inline">@Query</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ダークモード対応</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">システムカラー（.primary / Color(.systemGray6)）を使い、色を決め打ちしない</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">テストを実行</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><kbd>⌘U</kbd></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
iOS 開発クイックカード（2026年8月版）

#### 2. よくある質問 FAQ

Q1：Mac を持っていません。iOS 開発は学べますか？

言語の学習はできますが、本格的な開発はできません。iPad／iPhone の Swift Playgrounds なら第六十一章の内容までは学べます。ただし Xcode は macOS 専用なので、最終的には Mac が1台必要です。予算が限られているなら、クラウド Mac をレンタルしたり中古の Mac mini を買ってしのいだりして、言語を学び終えてから本格投資を決めるのもよいでしょう。

Q2：iOS 開発の学習には、いくらお金がかかりますか？

学習段階：0円（Xcode は無料 + 無料の Apple ID で実機デバッグ可能）。リリース段階：開発者アカウントが年間99ドル。これに Mac 1台のハードウェアへの投資を加えたものが総コストです。見返りと比べれば——App Store では小さなツールでも有料ユーザーがつくもの——十分に割に合う勘定です。

Q3：SwiftUI と UIKit、どちらを先に学ぶべき？

SwiftUI です。2026年の新規プロジェクト・新しいチュートリアル・新しい求人はいずれも SwiftUI が中心で、本書も通して SwiftUI を使います。UIKit は前世代のフレームワークで、多くの古いプロジェクトでは今も使われています——SwiftUI に慣れてから必要に応じて UIKit を補えば（公式に相互運用のチュートリアルがあります）、習得は速いはずです。順序だけは逆にしないこと。

Q4：iOS 開発は仕事探しに強いですか？

2026年の市況：単に「画面が描けるだけ」の初級ポジションは競争が激しいものの、「Swift + SwiftUI を理解し、リリース実績がある」開発者は今も引く手あまたです。iOS 関連職の給与中央値は、各技術スタックの中で長年上位にあります。学習中のあなたにとって最高の履歴書は、ストアに並んだ自分の App です。

Q5：App が審査で却下されたら、どうすればいい？

慌てなくて大丈夫、ごく普通のことです——初回提出が却下される確率は決して低くありません。Apple の却下理由は通常とても具体的に書かれている（どの画面か、どのガイドラインか）ので、1件ずつ修正し、App Store Connect で回答を添えて再提出すればOK。よくある却下理由のビッグ3は、権限の用途説明が不明瞭、画面にバグがある、メタデータ（スクリーンショット／説明文）と実際の中身が合っていない、の3つ。事前にこの3点をセルフチェックすれば、1回ぶんの待ち時間を節約できます。

#### 3. Xcode のよく使うショートカット一覧

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">操作</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ショートカット</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">実行／テスト</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R / ⌘U</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">キャンバスプレビューを開く</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ファイルをすばやく開く</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">プロジェクト全体を検索</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘F</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">インデントを整形</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">コメント／コメント解除</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ビルドキャッシュをクリーン</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘K</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定義へジャンプ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘クリック</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">リネーム（全体を安全に改名）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">右クリック → Refactor → Rename</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Xcode のよく使うショートカット一覧

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ワンポイント：コンパイルの怪奇現象は、まずキャッシュクリア

{class="mt-1"}
「昨日は動いたのに今日は動かない」という怪奇現象は、六七割がビルドキャッシュの不調です。⇧⌘K でクリーンしてから再ビルドすれば、怪奇現象の大半は解決します。それでもだめなら Xcode を再起動（Mac ごとでも）、さらにだめなら「DerivedData フォルダを削除」——iOS 開発者の間で口伝えに受け継がれてきた究極の三連コンボです。
:::

#### 4. おすすめ学習リソース

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">種類</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">リソース</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">おすすめの理由</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">公式</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">developer.apple.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple の公式ドキュメント。SwiftUI／Swift のチュートリアルもここに。第一の権威です</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">公式</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple の SwiftUI Tutorials</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">公式のきめ細かいハンズオン。初心者へのやさしさは満点</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">公式</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift 公式サイト（swift.org）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">言語の公式ドキュメントとオンラインの実行環境</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">コミュニティ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hacking with Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Paul Hudson の無料チュートリアル集。品質は誰もが認めるトップクラス</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">コミュニティ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stack Overflow（swiftui タグ）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">エラーで困ったときの最初の駆け込み先</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">動画</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Developer 公式チャンネル（WWDC 動画）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">毎年の新技術を権威者が解説</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">デザイン</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple ヒューマンインターフェースガイドライン（HIG）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">「Apple らしい」画面を作るための公式のバイブル</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">本書の関連</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第7部『AIプログラミング実践編』（第37〜47章）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI で iOS 開発を支援するための完全な心得</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
iOS 開発の学習リソース一覧（2026年8月）

#### 5. おわりに：最初の App から N 個目の App へ

振り返ってみれば、「SwiftUI が何かも知らなかった」あなたが、Xcode をインストールし、Swift を学び、SwiftUI で画面を描き、App にデータベースとネットワークを接続し、さらにテスト・パッケージング・リリースまで進みました——この道のりで、あなたはもうゼロからイチへ至るいちばん難しい区間を歩き終えています。

技術の世界は変化が速いものです。フレームワークは更新され、ツールは世代交代し、AI は「キーボードを叩く」作業をどんどん引き受けていくでしょう。でも、色あせないものがひとつあります。ぼんやりしたアイデアを明確なステップに分解し、一歩ずつ形にしていくあなたの力です。ツールは増幅器、考え方は土台。増幅器は取り替えられますが、土台は揺るぎません。

:::inline div .quote-line
あなたはもう「スマホが使える人」だけではありません。頭の中のアイデアを、数億台のiPhoneで実際に動くアプリに変えられるのです。今日からキーボードで創造しよう——これがiOS開発者のロマンです。
:::

#### 参考文献

{class="list-decimal pl-6 mb-3 space-y-1 text-xs text-gray-500"}
1. Apple Inc. (2026). SwiftUI Framework Documentation. developer.apple.com.
2. Apple Inc. (2026). Swift Programming Language Guide. swift.org.
3. Apple Inc. (2026). SwiftData Framework Documentation. developer.apple.com.
4. Apple Inc. (2026). App Store Review Guidelines. developer.apple.com/app-store/review.
5. Apple Inc. (2026). Human Interface Guidelines (HIG). developer.apple.com/design.
6. Apple Inc. (2026). Xcode 27 Release Notes and App Distribution Guide.
