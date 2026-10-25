---
id: di-san-shi-jiu-zhang
num: 39
part: ai-biancheng-pian
nav: 第三十九章：コンテキストエンジニアリング——AIにあなたの意図を理解させる
toc: default
kind: chapter
---

### 第三十九章：コンテキストエンジニアリング——AIにあなたの意図をわからせる

{class="chapter-intro mb-4"}
こんな経験はありませんか：新しい会話ウィンドウに切り替えると、AIは記憶喪失になったように、プロジェクトの基本情報をすっかり忘れてしまう。これはAIがわざと困らせているのではなく、生まれつき「忘れっぽい」のです。この章では、AIに「長期記憶システム」を取り付ける方法を教えます。あわせて、2026年で最も注目されている開発パラダイムの一つ——仕様駆動開発——も紹介します。

#### 一、プロジェクト記憶ファイル：AIの「長期記憶」

AIモデルには根本的な制限があります：記憶が「短期的」なのです。会話が始まるたびに、AIはあなたのプロジェクトについてゼロからスタートします。だから会話の中で「使っているのはReact」「バックエンドはNode.js」「データベースはPostgreSQL」「コードのスタイルはダブルクォート」と、何度も伝え続けなければなりません。これは非効率なうえ、抜けも出やすくなります——毎日、入ってきたばかりの同僚に入社研修をするようなものです。

解決策が「プロジェクト記憶ファイル」です——プロジェクトのルートディレクトリに置くプレーンテキストのファイルで、AIツールは会話の開始時に自動で読み込みます。ツールごとに、名前の付け方の慣習が違います：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ツール</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ファイル名</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cursorrules</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">CLAUDE.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitHub Copilot</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">copilot-instructions.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">汎用</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">AGENTS.md</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
各ツールのプロジェクト記憶ファイルの命名慣習

名前は違っても原理は同じです：AIに「いつも覚えていてほしい」情報をこのファイルに書き込むのです。良いプロジェクト記憶ファイルには次を含めるべきです：プロジェクト概要（これは何のプロジェクトか）、技術スタック（どんな技術を使っているか）、コード規約（命名、インデント、コメントのスタイル）、ディレクトリ構造（コードがどう整理されているか）、開発ルール（ブランチ戦略、コミット規約、テスト要件）。KarpathyのCLAUDE.mdはわずか70行ですが、大事な情報をすべてカバーしています——簡潔でありながら完璧なのです。

::: div .code-block
:::inline div .code-head
<span>CLAUDE.md</span><span class="dots">···</span>
:::

```
# プロジェクト：個人家計簿アプリ
## 概要
日常の収支を記録するのを助ける、フルスタックの個人家計簿アプリです。
## 技術スタック
- フロントエンド：React + TypeScript + Tailwind CSS
- バックエンド：Node.js + Express + TypeScript
- データベース：SQLite（開発）/ PostgreSQL（本番）
- テスト：Vitest
## コーディング規約
- ダブルクォートを使う
- インデントはスペース2つ
- 関数名はcamelCase
- 型定義はPascalCase
- すべての関数にJSDocコメントを付ける
## ディレクトリ構成
/src
  /frontend  - フロントエンドのコード
  /backend   - バックエンドのコード
  /shared    - 前後で共有する型
  /tests     - テストファイル
## 開発の約束事
- コミットメッセージは中国語で
- 新機能は必ずテストを先に書く
- APIの応答は { success, data, error } 形式で統一
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：「二枚目の要件文書」にしないこと

{class="mt-1"}
このファイルの長さに注意してください——何十ページもの要件文書にはしないこと。プロジェクト記憶ファイルの目的は「AIにすばやく背景の認識を持たせる」ことであって、「各機能をくわしく記述する」ことではありません。簡潔に、構造化して、「AIが知っておくべきこと」だけを書きましょう。
:::

#### 二、仕様駆動開発（SDD）

Spec-Driven Development（SDD、仕様駆動開発）は2026年に成熟してきた開発パラダイムです。核心理念はひと言：先に仕様を書き、それからコードを書く。従来のTDD（テスト駆動開発）と違うのは、SDDの「仕様」にはテストケースだけでなく、要件の記述、インターフェースの定義、データモデルなども含まれることです。AIはこれらの仕様に基づいてコードを生成し、人間の役割は仕様を書き、維持することです。

SDDのワークフローは五つのステップです：

1. 自然言語で要件の仕様を書く（.mdファイルに記述する）。
2. インターフェースとデータ構造を決める（仕様ファイルに書く）。
3. AIに、仕様に沿ったコードを実装させる。
4. テストを動かして、成果物が仕様どおりか確かめる。
5. ずれていたら、仕様を直すか、AIにコードを直させる。

この流れの中で、仕様ファイルは「唯一の真実の源」です——コードは作り直せますが、仕様が先に正しくなければなりません。

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> 仕様ファイルを書く</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> 仕様は完全ですか？</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> 完全</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> AIが仕様からコードを生成</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> テストを実行して成果を検証</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> 仕様不完全 / テスト不合格</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-tools mr-1"></i> コードの問題 → コードを修正。仕様の問題 → 仕様を修正</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> 検証に戻る</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> 全部合格 → 納品</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
図3：仕様駆動開発（SDD）のワークフロー
:::

SDDの強みは、仕様ファイルがコードより安定していることです。土台のモデルやツールが変わっても、仕様ファイルは依然として有効で、新しいAIツールにコードを作り直させるだけで済みます。だからこそ本書は「方法論はツールより大事」と強調するのです——仕様ファイルは、あなたの方法論の具体的な担い手なのです。

#### 三、コンテキストウィンドウ管理

プロジェクト記憶ファイルがあっても、会話の中で「コンテキストが足りない」という問題には出会います。AIモデルのコンテキストウィンドウ（同時に処理できる情報の量）には限りがあります。会話が長くなりすぎたり、参照するファイルが多すぎたりすると、AIは序盤の情報を「忘れ」て、成果物の質が落ちます——友人と6時間もおしゃべりしていたら、冒頭で話した最初の話題なんて忘れているのと同じです。

コンテキストウィンドウ管理の中核戦略は「層わけした参照」です：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">コンテキストの層</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">内容</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">管理方法</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第一層：プロジェクト記憶</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">技術スタック、規約、ディレクトリ構造</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">CLAUDE.mdなどのファイルに書き、自動で読み込まれる。繰り返し不要</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第二層：ファイル参照</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">いまのタスクに関わるコードファイル</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@記号で正確に参照する。全文を会話に貼らない</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第三層：対話コンテキスト</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">いまのタスクの会話履歴</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ひとつのタスクが終わったら新しい会話を開く。コンテキストのふくらみを防ぐ</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第四層：その場の指示</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">いまこの手順での具体的な要求</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">明確・簡潔・的確に。くどい説明はしない</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
コンテキストウィンドウの層別管理戦略

#### 四、コンテキストエンジニアリングの実践ポイント

コンテキストエンジニアリングは一回きりの設定ではなく、続けて最適化していくプロセスです。実践で繰り返し効いてきたポイントを紹介します：

1. 記憶ファイルはプロジェクトの進化に合わせて随時更新する。新しい技術を取り入れたりアーキテクチャを変えたりしたら、真っ先に記憶ファイルを更新します。会話の中でその場で説明するのは避けましょう。
2. @参照を活用し、全文の貼り付けはしない。ほとんどのAIプログラミングツールは@fileや@folderという書き方に対応していて、裏側でファイルの中身をAIのコンテキストに注入してくれます。手で貼り付けるより効率的で、会話を汚しません。
3. 会話は「短く、濃く」を心がける。ひとつの会話では、ひとつのタスクかひとつの機能だけを扱います。終わったら新しい会話で次へ進みます。長い会話はコンテキストウィンドウを消耗するだけでなく、AIを「ぼんやり」させます。
4. 結果を「説明」するのではなく、AIに結果を「見せる」。バグに出会ったら、「なんかエラーが出たみたい」と自分の言葉で説明するのではなく、エラーログをそのまま@参照でAIに渡しましょう。AIはあなたの伝え聞きより、生の情報を見るほうがずっと効率的です。
5. 定期的に掃除とアーカイブをする。終わった会話や一時ファイルは作業スペースを占領します。無関係なものを定期的に片付けてプロジェクトのディレクトリをきれいに保つと、AIがプロジェクトの構造をより効率的に理解するのにも役立ちます。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
やってみよう：あなたのプロジェクトに70行の記憶ファイルを書こう

{class="mt-1"}
いま作っている（または作ろうと思っている）プロジェクトをひとつ選び、CLAUDE.mdを書いてみましょう：プロジェクト概要（2〜3文）、技術スタック（書き出す）、コード規約（3〜5項目）、ディレクトリ構造（ツリーで描く）、開発ルール（2〜3項目）。70行以内に収めます——書き終えるころには、プロジェクトに対する自分の理解までずいぶんはっきりしていることに気づくはずです。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章のまとめ

- AIの記憶は「短期的」：新しい会話のたびに、プロジェクトの理解はゼロから
- プロジェクト記憶ファイル（CLAUDE.mdなど）はAIの「長期記憶」。会話のたびに自動で読み込まれる
- 良い記憶ファイル ＝ 概要＋技術スタック＋規約＋ディレクトリ＋開発ルール。70行で十分
- SDD（仕様駆動開発）：先に仕様を書き、それからコードを書く。仕様は「唯一の真実の源」で、コードより安定している
- コンテキストは四つの層で管理：プロジェクト記憶 → @ファイル参照 → 会話履歴 → その場の指示
- 五つの実践ポイント：随時更新、@参照、短い会話、生の情報を渡す、定期的な整理
:::
