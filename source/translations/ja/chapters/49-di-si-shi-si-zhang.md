---
id: di-si-shi-si-zhang
num: 44
part: ai-biancheng-pian
nav: 第四十四章：0から1への実践——プロジェクトの全工程
toc: default
kind: chapter
---

### 第四十四章：0から1への実践——プロジェクト完成までの全プロセス

{class="chapter-intro mb-4"}
理論は学び終えました。いよいよ手を動かす番です。この章は単なる「写経」チュートリアルではなく、「どう考えるか、どう聞くか、どう確かめるか」という実践の方法論です。難易度の異なる3つのプロジェクトを使って、要件から完成品までの思考プロセスのすべてをお見せします。どのツールを使っていても、この流れはそのまま使えます。

#### 一、プロジェクト1：ミニマル個人ツールサイト（入門レベル）

##### 1. 要件を考える

目標：実用的な小さなツールへの入り口を3〜4個並べて表示する、個人ツールサイトのWebページを作ること。フロントエンドだけのプロジェクトで、バックエンドもデータベースも不要です。ポイントはツールそのものの複雑さではなく、「要件から完成品まで」の流れを一通り体験することです。

要件の5要素に沿って整理します。Who——個人で使う。What——ツールへの入り口を並べて見せるWebページ。Why——よく使うツールを1ページにまとめてアクセスしやすくする。How——単一ファイルのHTML+CSS+JSで、フレームワークは使わない。Constraint——30分以内に完成、デプロイは不要。

##### 2. 指示を出す

Think Before Codingの原則に基づき、指示にはAIが目標を理解するのに十分な情報を含めます。ただし、実装の細部まで指定する必要はありません。

::: div .code-block
:::inline div .code-head
<span>AIへの指示</span><span class="dots">···</span>
:::

```
個人ツールサイトのWebページを作成してください。要件：
1. 単一HTMLファイル（CSSとJSをインライン）、フレームワーク不使用
2. ダークテーマ、モダンなミニマルスタイル
3. 4つのツールカードを表示：
   - テキスト要約ツール
   - 文字数カウントツール
   - カラーピッカー
   - QRコード生成ツール
4. 各カードにアイコン、タイトル、短い説明
5. カードはホバーアニメーション付き
6. レスポンシブ、スマホで使える
7. 上部にタイトルバー
完全なHTMLファイルを直接示してください。
```
:::

##### 3. 検収と反復

AIからコードが出てきたら、反復検証の3層チェックで受け入れます。第1層・機能の検証：ファイルはブラウザで開けるか？4枚のカードはすべて表示されるか？ホバーのアニメーションは正しく動くか？第2層・境界の検証：スマホ画面のサイズでもレイアウトは崩れないか？ウィンドウが細いときカードは折り返されるか？第3層・アーキテクチャの検証：コードは読みやすいか？CSSは1つのstyleタグの中に収まっているか？目につく重複や無駄はないか？

カードの入り口だけでなく、ツールの機能そのものも実装したい場合は、少しずつ足していきましょう。1回に1つのツールの機能を追加し、確認してから次へ。これが「小刻み前進」戦略の実戦での使い方です。

#### 二、プロジェクト2：フルスタック家計簿システム（中級レベル）

##### 1. 要件の検討とPRD

目標：フロントエンド、バックエンド、データベースを備えたフルスタックの家計簿アプリ。このプロジェクトは最初のものよりずっと複雑で、第四十章の要件エンジニアリングの手法が必要になります。

まずPRDを書きます。第四十章第3節のテンプレートに沿って、プロジェクト概要、機能リスト、技術案、データモデル、開発計画をまとめましょう。技術案の選択ではSimplicity Firstの原則を考慮します。フロントエンドはReactを使うがReduxなどの複雑な状態管理は入れない。バックエンドはNode.jsを使うがマイクロサービスにはしない。データベースは開発段階ではPostgreSQLではなくSQLiteを使う、という具合です。

開発計画は5ステップに分解します。Step 1：バックエンドAPIの骨組み（Expressサーバー＋SQLite＋CRUDのエンドポイント）。Step 2：フロントエンドの基本ページ（記録リスト＋追加フォーム）。Step 3：フロントとバックのつなぎ込み（API呼び出し＋データ表示）。Step 4：カテゴリと絞り込み機能。Step 5：月次の集計と簡単なグラフ。各ステップが終わるごとに「使えるもの」になっているのが理想です。

##### 2. プロジェクト記憶ファイルを設定する

コーディングを始める前に、まずプロジェクト記憶ファイルを作成します。これがコンテキストエンジニアリングの中核となる実践です。対話が始まるたびにAIがプロジェクトの背景を把握できるようにします。

::: div .code-block
:::inline div .code-head
<span>CLAUDE.md</span><span class="dots">···</span>
:::

```
# プロジェクト：フルスタック家計簿アプリ
## 概要
収支記録・カテゴリー・月次集計に対応した個人家計簿アプリ。
## 技術スタック
- フロントエンド：React + TypeScript + Vite
- バックエンド：Node.js + Express + TypeScript
- データベース：SQLite（better-sqlite3経由）
- 前後で共有する型定義
## APIの約束事
- 基本パス：/api
- 応答形式：{ success: boolean, data: any, error: string }
- RESTfulスタイル
## データモデル
Record { id, amount, type, category, note, date }
## コーディング規約
- TypeScriptのstrictモード
- インデントはスペース2つ
- 関数にはJSDocコメント
- コメントとコミットメッセージは中国語で
```
:::

##### 3. 少しずつ実装する

開発計画に沿って、各ステップを独立した対話で完成させます。最初のステップの指示例は次のとおりです。

::: div .code-block
:::inline div .code-head
<span>AIへの指示（Step 1）</span><span class="dots">···</span>
:::

```
バックエンドAPIの骨格を作成する必要があります。
要件：
1. Expressサーバー、ポート3001
2. SQLiteデータベース、テーブル名records
3. recordsテーブルのフィールド：
   id (TEXT PRIMARY KEY)
   amount (REAL)
   type (TEXT: 'income'|'expense')
   category (TEXT)
   note (TEXT)
   date (TEXT: YYYY-MM-DD)
4. CRUD API：
   GET /api/records - 全記録の取得
   POST /api/records - 記録の追加
   PUT /api/records/:id - 記録の更新
   DELETE /api/records/:id - 記録の削除
5. エラー処理ミドルウェア
完全なバックエンドコード構成を示してください。
```
:::

この指示の特徴に注目してください。今やるべきこの1ステップ（バックエンドの骨組み）だけを記述し、フロントエンドの要件を混ぜていない。フィールドとインターフェースを明示して（AIに十分な制約を与えつつ）、具体的な実装はAIに任せている。そしてGoal-Driven Executionの原則に従い、「どう作るか」ではなく「何を作るか」を語っている、という点です。

AIからコードが出たら、すぐに検証します。サーバーを起動し、curlかPostmanで各エンドポイントが正しく動くかをテストしましょう。問題がないことを確認したら、新しい対話を開いてStep 2（フロントエンドの基本ページ）に進みます。各ステップで「指示→検証→新しい対話」のサイクルを守ります。

#### 三、プロジェクト3：AI拡張アプリ（上級レベル）

##### 1. プロジェクトの構想

目標：大規模モデルAPIを組み込んだアプリ。たとえば「AI学習アシスタント」です。ユーザーが学習内容を入力すると、AIが要約を生成し、関連する知識ポイントを結び付け、学習リソースのおすすめを出します。このプロジェクトの特別なところは、あなたのアプリ自体がAIを呼び出すという点です。API呼び出し、プロンプトエンジニアリング、エラー処理といった新しい問題に取り組む必要があります。

このプロジェクトが教えてくれる最も大切なことは、「AIに、AIを呼び出すコードを書かせる」ときは、プロンプトエンジニアリングに格段に気を配る必要がある、ということです。あなたのアプリが大規模モデルAPIを呼び出すときに使うプロンプトにも、本ガイドで論じてきた原則——明快、簡潔、目標駆動——がそのまま当てはまります。

##### 2. 重要な技術ポイント

このプロジェクトには、最初の2つのプロジェクトでは出てこなかった技術ポイントがいくつか登場します。

- APIキーの管理：キーをコードにハードコードしては絶対だめ。環境変数で管理します
- ストリーミング応答の処理：大規模モデルの返答は通常ストリーミングで返るため、一文字ずつ表示する仕組みが必要です
- トークン使用量の制御：大規模モデルはトークン単位で課金されるため、アプリ側で使用量を抑える必要があります
- プロンプトテンプレートの管理：機能ごとに異なるプロンプトテンプレートを使うので、構造化して管理します

これらの技術ポイントは、すべてAIに実装を手伝わせられます。ただし、それぞれの「なぜ」を理解しておく必要があります。なぜキーをハードコードしてはいけないのか？ なぜストリーミング応答が必要なのか？ なぜトークン使用量を抑える必要があるのか？ 「なぜ」が分かってはじめて、AIの提案した方式が妥当かどうかを判断できます。

#### 四、汎用の実践フローチェックリスト

プロジェクトの大小にかかわらず、次が汎用のAIプログラミング実践フローチェックリストです。新しいプロジェクトを始めるときは、このリストを一通りなぞって、重要なステップの漏れがないか確認しましょう。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">段階</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">やること</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">対応する原則</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1. 要件を考える</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">要件の5要素を一通り見て、何を作るかを明確にする</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Think Before Coding</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2. 要件の分解</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">大きな要件を、独立して検証できる小さなステップに分解する</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Simplicity First</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3. PRDを書く</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">構造化されたドキュメントにまとめ、参考資料にする</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Goal-Driven</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">4. 記憶ファイルを設定する</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">CLAUDE.mdなどのファイルを作成する</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Harness Engineering</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">5. 少しずつ実装する</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1ステップ1対話。「指示→検証→次へ」</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Surgical Changes</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6. テストと検証</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">各ステップ完了後すぐに機能の正しさをテストする</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">7. コードレビュー</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">アーキテクチャの妥当性、セキュリティ、保守性をチェックする</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8. 反復と改善</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">テストとレビューの結果をもとに改善を重ねる</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
AIプログラミング汎用実践フローチェックリスト

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
やってみよう：今週「プロジェクト1」を完成させよう

{class="mt-1"}
第四十四章第1節の「個人ツールサイト」を、あなたの最初のAIプログラミングの宿題にしましょう。5分かけて5要素を確認し、AIに指示を送り（どのツールでも構いません）、3層の検証で受け入れます。30分で完成させましょう——あなたの最初のAIプログラミング作品の誕生です。終わったらきちんと保存しておいてください。「読者」から「実践者」へ変わった記念品になります。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章のまとめ

- プロジェクト1（入門）：フロントエンドだけのツールサイト——全プロセスを体験。30分で完成できる
- プロジェクト2（中級）：フルスタック家計簿システム——PRD＋記憶ファイル＋5ステップの段階的実装。各ステップで「使えるもの」に
- プロジェクト3（上級）：AI学習アシスタント——AIを呼び出すコードをAIに書かせる。プロンプトエンジニアリングに注意
- 汎用フロー8ステップ：要件検討→分解→PRD→記憶ファイル→段階的実装→テスト→レビュー→反復
- 各ステップは「指示→検証→新しい対話」のサイクルに従う
:::
