---
id: di-liu-shi-zhang
num: 60
part: ios-kai-fa-pian
nav: 第六十章：開発環境の構築——Xcodeと最初のプロジェクト
toc: default
kind: chapter
---

### 第六十章：開発環境を整える——Xcodeと最初のプロジェクト

{class="chapter-intro mb-4"}
仕事をうまくやるには、まず道具をととのえること。この章では「キッチン」を整えます：Xcodeを入れて、シミュレータを動かして、人生初のiOSプロジェクトを作り、さらにプロジェクトの構造をばらして丸ごと理解します。環境が整えば、自分が書いたコードが「押せるボタン」になる瞬間に初めて出会えます——この瞬間を一生覚えている人は多いものです。

#### 1. Macを1台用意する

まずハードルの話：iOS開発はmacOS上で行う必要があります。Macを持っていない場合、選択肢は3つ。1台買う（中古のMac miniやMacBook Airでも十分）、短期だけクラウドMacを借りる、あるいは先に第8編『Android開発実践編』（WindowsでOK）を読む——この3つです。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">項目</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">最低要件</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">快適ライン（おすすめ）</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">チップ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Silicon（M1以降）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">M2以降</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">メモリ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8GB</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">16GB</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ストレージ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">40GB以上を確保（Xcode本体はかなり大きい）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256GB以上</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OS</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最新のmacOS</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自動更新をオンのまま</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Mac開発マシンの構成目安（2026年8月）

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ワンポイント：Macがなくても、言語から先に学べる

{class="mt-1"}
iPadの無料アプリSwift Playgroundsなら、MacなしでSwiftの基礎が学べます（iPhoneにも入れます）。まず第六十一章の言語の知識をPlaygroundsで遊びながら慣らしておき、Macを手に入れたらそのまま飛び立てます。「薪を割る前に斧を研ぐ時間は無駄にならない」というわけです。
:::

#### 2. Xcodeをインストールする

XcodeはApple公式の統合開発環境で、無料です。3ステップで入れましょう：

1. MacでApp Storeを開き、「Xcode」と検索してインストールをクリック——数GBあるので、ネットが快適な時間帯を選びましょう。
2. インストール後の初回起動で規約に同意し、必要なコンポーネントを入れます（自動で完了します）。
3. メニューのXcode → Settings → Locationsで、Command Line Toolsが選択されているか確認します——コマンドラインツールは、多くのスクリプトやサードパーティツールの前提になるものです。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：バージョンとOSの「組み合わせゲーム」

{class="mt-1"}
新しいXcodeはたいてい最新のmacOSを求め、古いMacは古いバージョンで止まってしまいます。App Storeに公開するとき、Appleは比較的新しいXcodeでのビルドを求めます（たいてい猶予期間はあります）。だからOSの更新はサボらないでください——iOS開発者は「最新版を追いかける」のがいちばん勤勉な集団なのです。
:::

#### 3. 最初のプロジェクトを作る

Xcodeを開いてCreate New Project → iOSを選択 → Appテンプレートを選び、次のように入力します：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">項目</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">入力するもの</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">説明</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Product Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstApp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">アプリ名</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">あなたのApple ID（無料）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">署名用。個人アカウントでOK</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Organization Identifier</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Product Nameと組み合わせてパッケージIDになる</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interface</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">本書のメインで使うフレームワーク</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Language</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">説明は不要でしょう</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
プロジェクト作成で入力する5つの項目

Createを押すと、Xcodeはそのまま実行できるプロジェクトを生成します。左上でシミュレータを1台選び（たとえばiPhone 17）、▶を押して実行——数秒後、シミュレータの画面に「Hello, world!」と書かれたウィンドウが現れます。あなたの初めてのiOSアプリが誕生した瞬間です。

#### 4. プロジェクト構造の分解：ファイルごとの役割

左側はプロジェクトナビゲータです。初心者がまず知っておけばいいのはこのくらい：

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="290" viewBox="0 0 600 290" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="290" fill="#fafafa" rx="8"/>
      <text x="20" y="28" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ プロジェクトのルート</text>
      <rect x="30" y="42" width="540" height="225" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <rect x="45" y="56" width="250" height="196" fill="#eef2ff" rx="5"/>
      <text x="56" y="78" font-size="11" fill="#1e1b4b" font-weight="bold">MyFirstApp/（コードのディレクトリ）</text>
      <text x="66" y="100" font-size="10" fill="#374151">├ MyFirstAppApp.swift  ← プログラムの入口</text>
      <text x="66" y="120" font-size="10" fill="#374151">├ ContentView.swift  ← メイン画面</text>
      <text x="66" y="140" font-size="10" fill="#374151">└ Assets.xcassets  ← アイコン・画像・色</text>
      <text x="56" y="166" font-size="10" fill="#6b7280">（新しいファイルはすべてこのディレクトリへ）</text>
      <text x="56" y="196" font-size="10" fill="#1e1b4b" font-weight="bold">Infoタブ / Info.plist</text>
      <text x="66" y="216" font-size="10" fill="#6b7280">アプリの宣言：名前、権限、設定</text>
      <rect x="310" y="56" width="245" height="196" fill="#f0fdf4" rx="5"/>
      <text x="321" y="78" font-size="11" fill="#065f46" font-weight="bold">その他の重要な場所</text>
      <text x="331" y="100" font-size="10" fill="#374151">📁 Preview Content/  ← プレビュー素材</text>
      <text x="331" y="122" font-size="10" fill="#374151"><i class="fas fa-bullseye mr-1"></i> Targetの設定（青いプロジェクトアイコン）</text>
      <text x="331" y="142" font-size="10" fill="#6b7280">── バージョン番号、最低システム、署名はすべてここに</text>
      <text x="331" y="168" font-size="10" fill="#374151"><i class="fas fa-flask mr-1"></i> MyFirstAppTests/  ← ユニットテスト</text>
      <text x="331" y="188" font-size="10" fill="#374151">📱 MyFirstAppUITests/ ← 画面テスト</text>
      <text x="331" y="216" font-size="10" fill="#9ca3af">（テストのテンプレートは生成済み。第六十七章で使用）</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
図2：初心者が必ず知りたいXcodeのプロジェクト構造
:::

- MyFirstAppApp.swift：プログラムの入口。SwiftUIではわずか数行——「起動して、メイン画面を表示する」だけです。
- ContentView.swift：メイン画面のビュー。いまあなたが見ているものは、ぜんぶここにあります。
- Assets.xcassets：リソースの倉庫——アイコン・画像・色はここに置きます。
- Targetの設定：左側の青いプロジェクトアイコンをクリックして入ります。バージョン番号、対応最低iOSバージョン、署名はぜんぶここにあります。アプリの表示名やアイコンもここで設定します。

#### 5. Xcodeの時短テクニック：初心者に効く「ショートカット裏ワザ」5選

これを使いこなせば、あなたはグッと「プロっぽく」見えます：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">操作</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ショートカット</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">効果</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">実行</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ビルドして動かす</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">キャンバスプレビューの表示／切り替え</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">見たままがそのまま出るスイッチ</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">インデントを整形</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">選択したコードのインデントを自動で整える</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ファイルをすばやく開く</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ファイル名を入れて即オープン（いちばん使う！）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">コメント化／コメント解除</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">デバッグ中にコードを手軽にオン・オフする</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Xcodeのよく使うショートカット（初心者の基本5選）

さらに2つの隠れた特典：シミュレータの複数起動（iPhoneとiPadを同時に動かしてレイアウトを比較）と、コードスニペット庫（よく使う数行を右側のSnippetsパネルにドラッグしておけば、次からワンクリックで挿入）——効率化ツールはまず使ってみると、手感は自然についてきます。

#### 6. 実機デバッグ：アプリをあなたのiPhoneに入れる

シミュレータも便利ですが、ゴールは実機です。無料のApple IDでも実機デバッグはできます：

1. ケーブルでiPhoneをつなぐ（または同じWi-Fiでワイヤレスデバッグ）。
2. Xcode上部のデバイスリストで自分のiPhoneを選びます。初回はApple IDでのサインインと、署名の自動設定を案内されます。
3. iPhoneの［設定］→［一般］→［VPNとデバイス管理］で、開発者証明書を信頼します。
4. ▶を押すと、アプリが実機に入ります。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：無料アカウントの「7日間制限」

{class="mt-1"}
無料Apple IDで署名したアプリは7日後に使えなくなります（もう一度実行すれば更新されます）。これはAppleの不正利用防止の仕組みで、学習段階なら十分です。有料開発者アカウント（年99ドル）ならこの制限はありません。詳しくは第六十七章で。
:::

#### 7. さっそく試す＋よくあるエラーの応急処置

ContentView.swiftを開いて、Text("Hello, world!")の中の文字を自分の名前に変え、⌘Rでもう一度実行——数秒後、シミュレータに自分の名前が表示されます。おめでとうございます。「コードを直す → ビルド → インストール → 実行」という、最初の完全なサイクルを終えました。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">エラーの症状</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">よくある原因</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">対処法</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Signingエラー</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Teamが未選択、証明書の期限切れ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Target → Signingで自分のアカウントにチェック。無料アカウントならもう一度実行</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">シミュレータが真っ暗／開かない</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">イメージが壊れている</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">メニューのDevice → Erase All Content。またはシミュレータを削除して作り直す</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcodeのダウンロードが遅い／インストールできない</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">App Storeのネットワーク不安定</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">時間帯を変える。またはApple開発者サイトから.xipオフラインパッケージをダウンロード</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
初心者の環境エラー応急処置表

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
やってみよう：「開発の儀式」リストを完成させる

{class="mt-1"}
①Xcodeを入れてシミュレータを動かす。②実機で自分のアプリを1回実行し、スクリーンショットを記念に残す。③Helloの文字を自分の名前に変える。④Target設定でアプリの表示名を「わたしの初めてのアプリ」に変える。この4ステップを終えれば、あなたはもう「作品を持つ人」です。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章のまとめ

- ハードル：Mac＋Xcode。Macがなければ、まずiPadのSwift Playgroundsで言語を学ぶ
- XcodeはApp Storeから。新バージョンは新しいOSを求めるので、更新はサボらない
- 新規プロジェクトの5要素：名前、Team、Organization Identifier、SwiftUI、Swift
- プロジェクトの合言葉：コードはみんなMyFirstApp/フォルダの中。Target設定がバージョンと署名を担当
- 無料Apple IDの実機デバッグには7日間の署名制限。有料アカウントなら制限なし
- 開発の毎日＝コードを直す → ⌘R → 結果を見る、の繰り返し
:::
