---
id: di-si-shi-san-zhang
num: 43
part: ai-biancheng-pian
nav: 第四十三章：対話エンジニアリング——効率的な対話テクニック
toc: default
kind: chapter
---

### 第四十三章：対話エンジニアリング——AIと効率的に協働するための対話技術

{class="chapter-intro mb-4"}
対話はAIプログラミングの中核となるやり取りの方法です。ただし「対話」は「おしゃべり」と同じではありません。効率的なAIプログラミングの対話とは、構造化されたコミュニケーション技術のことで、本書ではこれを「対話エンジニアリング」と呼びます。その研究対象は、いかに少ない対話ターンで最高品質のコードを引き出すか。はっきり言えば、この章はAIと「物事をはっきり伝える」方法を教える章なのです。

#### 一、プロンプトの階層戦略

AIとの対話は3つの階層に分けられ、それぞれ担う役割が違います。この3層を理解すれば、積み木を組み合わせるように効率的なプロンプトを作れるようになります。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">階層</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">機能</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">例</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">頻度</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">システム層</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AIの役割と全体的な制約を設定する</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">「あなたはReactの専門家です。コードは必ずTypeScriptで書くこと」</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">プロジェクト開始時に1度だけ設定</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">タスク層</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">今から取り組む具体的なタスクを記述する</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">「ユーザー名とパスワードの入力欄を含むフォームコンポーネントを実装してください」</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">タスクごとの開始時に与える</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">フィードバック層</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AIの出力を評価して修正させる</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">「パスワード欄に表示/非表示の切り替えがないので追加してください」</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">出力の質に応じて与える</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
対話プロンプトの3つの階層

システム層のプロンプトは通常、プロジェクト記憶ファイル（CLAUDE.mdなど）に書いておきます。対話のたびに繰り返す必要はありません。タスク層は対話の中で最もよく使う層で、「何を」「どの技術で」「どんな制約のもとで」という3要素を含めるべきです。いちばん腕の見せどころはフィードバック層です。良いフィードバックはAIに的確に修正させられますが、悪いフィードバックはAIに再び当てずっぽうをさせるだけです。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ワンポイント：フィードバックの3つのコツ

{class="mt-1"}
実用的なフィードバックのテンプレートが「問題を指摘＋期待を説明＋文脈を提供」です。たとえば「25行目のエラー処理がconsole.logだけになっています（問題を指摘）。本番環境では共通のエラーハンドラを使い、ユーザーに分かりやすいメッセージを返すべきです（期待を説明）。プロジェクトにはhandleError関数があるので使えます（文脈を提供）」。このようなフィードバックは「エラー処理を直して」と頼むより10倍効きます。
:::

#### 二、デバッグ対話：エラーの説明でAIの問題特定を速くするには

デバッグはAIプログラミングで最も頻繁に登場する場面のひとつです。バグに遭遇したとき、問題をAIにどう伝えるかが、そのまま素早く特定して直せるかどうかを左右します。デバッグ対話の4つのポイントは次のとおりです。

1. あなたの言い換えではなく、生の情報をAIに「見せる」。エラーログや例外のスタックトレース、関連コードは「なんかエラーが出たみたい」と説明するのではなく、@で直接引用してAIに渡しましょう。AIはあなたの解釈を見るより、生の情報を見るほうが正確に把握できます。
2. 「期待する動作」と「実際の動作」の差を説明する。「ボタンをクリックしたらホームに遷移するつもりでした（期待）が、実際にはクリックしてもページが反応しません（実際）」——こうした説明は「ボタンが壊れています」よりずっと役に立ちます。
3. 再現手順を示す。「先にユーザー名を入力し、次にログインボタンをクリックすると、このエラーが出ます」——再現手順があればAIはあなたの操作の流れをなぞれるので、問題を特定しやすくなります。
4. すでに試したことをはっきり伝える。「ネットワークリクエストは確認済みで、200が返ってきてデータも正常です」——これはAIが検証済みの方向を除外し、同じ調査を繰り返して時間を無駄にするのを防いでくれます。

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
悪いデバッグの説明

{class="font-mono text-xs leading-relaxed"}
ボタンをクリックしても反応がありません。見てください
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
良いデバッグの説明

{class="font-mono text-xs leading-relaxed"}
ログインボタンをクリックしてもページが反応しません。 期待する動作：クリックすると /home ページに遷移する 実際の動作：クリックしても何も反応せず、コンソールにエラーなし 再現手順： 1. ログインページでユーザー名adminとパスワード123456を入力 2. 「ログイン」ボタンをクリック 3. ページが反応しない 確認済みの項目： - ネットワークリクエストは正常、200を返す - onClickイベントはバインド済み - LoginButtonコンポーネントのコードを確認済み 関連ファイル：@src/components/LoginButton.tsx @src/pages/Login.tsx
:::
:::

#### 三、反復戦略：小刻み前進 vs 一括リファクタリング

AIプログラミングにおける反復には2つの基本的な戦略があり、向いている場面がそれぞれ違います。この2つの違いを理解しておくと、状況に応じて正しい選択ができます。

「小刻み前進」戦略は、機能開発やバグ修正に向いています。核心は、毎回AIに小さな修正を1つだけさせ、検証が通ってから次に進むこと。メリットは、一歩ごとに検証も取り消しもでき、リスクを制御できること。デメリットは、スピードが遅めで、対話のやり取りを頻繁に要ることです。向いているのは：新機能の開発、最適解が定まらないときの探索、AIの出力にあまり安心できないときの慎重な反復。

「一括リファクタリング」戦略は、目標が明確な大規模な変更に向いています。核心は、完成形の目標を一度に記述し、変更全体の計画と実行をAIに任せること。メリットは、スピードが速く、AIが全体像を見ながらより良いアーキテクチャ判断を下せること。デメリットは、リスクが高く、AIの理解がズレた場合の修正コストが大きいことです。向いているのは：明確なアーキテクチャの刷新、大規模なコード移行、十分なテストで裏付けられたリファクタリング。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">観点</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">小刻み前進</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">一括リファクタリング</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1回あたりの修正量</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">機能1つまたはバグ1つ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">モジュール1つまたはアーキテクチャ層1つ</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">検証の頻度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">修正のたびにすぐ検証</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">すべての修正が完了してからまとめて検証</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">対話のターン数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多い（機能あたり5〜10ターン）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">少ない（モジュールあたり1〜3ターン）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">リスク</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">低い。各ステップで取り消し可能</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">高い。ズレを直すコストが大きい</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">向いている場面</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新機能の開発、探索的な開発</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">目標のはっきりしたリファクタリングや移行</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">前提条件</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">特別な要件なし</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">テストカバレッジが必要</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
2つの反復戦略の比較

実践では、この2つの戦略を組み合わせて使うことがよくあります。たとえばモジュールをリファクタリングするとき、まず「一括リファクタリング」でAIに全体案を出させ、その案をレビューしてから「小刻み前進」で少しずつ実行します。こうすれば全体を見渡す視点を保ちつつ、実行のリスクも抑えられます。

#### 四、マルチターン対話のコンテキスト管理

対話のターンが重なるにつれ、対話のコンテキストを自分から管理して、「AIが最初の情報を忘れてしまう」問題を避ける必要があります。実用的なコンテキスト管理のテクニックをいくつか紹介します。

第一に、重要な情報を「固定（アンカー）」する。対話の最初に重要な制約を明確に書き、その後の対話でも適宜繰り返します。たとえば「覚えておいてください。データはlocalStorageに保存していて、データベースは使えません」——関連する修正の依頼の中でこの制約を重ねて伝え、AIの忘却を防ぎます。

第二に、「要約して引き継ぐ」テクニックを活用する。対話が長くなってきたら、AIに「ここまでの進捗と残りのタスクを要約してください」と頼み、その要約を出発点に新しい対話を始めます。こうすれば重要なコンテキストを保ちつつ、長い対話による劣化を避けられます。

第三に、「1つの対話に1つのタスク」。これは最もシンプルで、最も効果的なコンテキスト管理の戦略です。1つの対話では1つのタスクか機能だけを扱い、終わったら新しい対話で次に進みます。対話の長さが自然に制限され、コンテキストが明快に保たれます。

第四に、ツールのコンテキスト管理機能を利用する。ほとんどのAIプログラミングツールには「コンテキストをクリア」や「新規セッション」のボタンがあります。AIの回答の質が落ちてきたと感じたら、ためらわずに新しいセッションを開きましょう。会話履歴を少し失うほうが、劣化したコンテキストの中で足掻き続けるよりずっとましです。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
やってみよう：AIの「患者」を一度やってみる

{class="mt-1"}
ブラウザでわざと小さなページを作り、バグを仕込んでみましょう（たとえばボタンが反応しない、など）。そして本章の「良いデバッグの説明」の形式に従って、AIに一度きちんと説明してみます。生の情報、期待vs実際、再現手順、確認済みの項目。AIが問題を特定する速さの違いを体感すれば、「問題の説明」それ自体がひとつの技術だと分かるはずです。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章のまとめ

- プロンプトの3層：システム層（記憶ファイルに書く）、タスク層（何を＋技術＋制約）、フィードバック層（問題の指摘＋期待＋文脈）
- デバッグの4つのポイント：生の情報を渡す、期待vs実際、再現手順、確認済み項目
- 小刻み前進：低リスク・ターン数多めで新機能に最適。一括リファクタリング：高リスク・ターン数少なめでテストの裏付けが必要
- コンテキスト管理の4つの技：重要情報の固定、要約して引き継ぐ、1対話1タスク、思い切って新しいセッションを開く
:::
