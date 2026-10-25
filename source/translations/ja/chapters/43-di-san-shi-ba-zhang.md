---
id: di-san-shi-ba-zhang
num: 38
part: ai-biancheng-pian
nav: 第三十八章：AIプログラミングの5つの思考原則
toc: default
kind: chapter
---

### 第三十八章：AIプログラミング五大思考原則

{class="chapter-intro mb-4"}
もしこの本で一章だけ覚えられるとしたら、それは必ずこの章でなければなりません。五大思考原則は本書全体の心臓部であり、このあとのすべての章——コンテキスト、要件、対話、品質——は、この五つの原則をさまざまな場面に展開したものです。ご安心ください。どれ一つ難しくありませんが、どれ一つも、いくつものプロジェクトを通して「筋肉に染み込ませる」値打ちがあります。

物語の出発点がおもしろいのです。Andrej Karpathyは自分のプロジェクトをオープンソースとして公開したとき、わずか70行のCLAUDE.mdファイルを添付しました。そこにはAIと協働するための四つの中核原則がまとめられていました。このファイルはGitHubで70,000以上のStarを獲得し、世界中のAIプログラミング実践者に最も広く引用される指針となりました。この四原則は空虚なスローガンではなく、膨大な実践から磨き出された、実行できる思考の習慣です。本書はその土台の上に五つ目の原則——反復検証——を加え、完全な五大原則の体系にしました。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
70行のファイルはなぜそれほど価値があるのか？

{class="mt-1"}
70,000 Starはどれほどすごいことか？GitHubのほとんどのプロジェクトは、一生かけてもこの数字に届きません。70行のテキストファイルがそれを獲得できたということは、ただ一つの事実を証明しています。AI時代にいちばん希少なのはコードではなく、「考え抜く」能力だということです。この70行こそ、「考え抜く」の凝縮版なのです。
:::

#### 一、原則一：Think Before Coding（先に考え、それからコードを書く）

これは五つの原則の中で最も直感に反するものです。AIがコードを書いてくれるのに、どうして「先に考える」必要があるのでしょう？答えはシンプルです：AIの出力の質は、あなたの入力の質に比例します。自分でも何をしたいのかはっきり考えていなければ、AIの答えは「直してはまた直す」の果てしないループにあなたを落とし入れるだけ——いわゆる「AIと一緒に道に迷う」状態です。

「先に考える」とは、AIへの指示を出す前に、次の三つの質問に答えておくことです。この三つで、一つも欠かせない「思考のトライアングル」ができます：

1. 何の問題を解決するのか？（目標）
2. 期待する結果はどんな形か？（受け入れ基準）
3. 守るべき制約条件は何か？（境界）

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">思考の切り口</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">あいまいな入力（悪い例）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">明確な入力（良い例）</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">問題の定義</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ウェブサイトを作って</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AIミニツール3つの入口カードを並べた、個人用ツールサイトを作って</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">期待する結果</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ちょっとオシャレに</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">レスポンシブ対応、ダークテーマ、カードにはホバーのアニメーション、スマホでも使えること</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">制約条件</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">（未指定）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">フレームワークは使わない。素のHTML+CSS+JS、1ファイルでデプロイ、バックエンドは不要</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
同じ要件の、あいまいな入力と明確な入力の比較

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：先に考える ≠ 完璧な文書を先に書くこと

{class="mt-1"}
「先に考える」は「完璧なPRDを書いてから始める」という意味ではありません。短い時間で、しかし筋道立てて考えるプロセスです——上の三問を30秒で整理するほうが、30分かけて会話の中で何度もやり直すよりずっと効率的です。小さなタスクなら三問は短くてよく、大きなプロジェクトなら本格的な要件文書に発展させればよいのです（詳しくは第四十章）。
:::

#### 二、原則二：Simplicity First（シンプル・ファースト）

AIプログラミング最大の落とし穴は「作れないこと」ではなく「作りすぎること」です。AIに「ユーザー管理システムを作って」と頼むと、認証、権限、ロール、監査ログ、データエクスポートといった機能一式を生成してくるかもしれません——でも今のあなたに必要なのは、シンプルなログインページだけかもしれないのです。この「作りすぎ」こそ、AIコードがふくれ上がる主な原因です。

「シンプル・ファースト」では、指示を出すたびに「最小限で実現する」原則に従うことが求められます：いちばん少ないコードで中核機能を作り、いちばんシンプルな方法で問題を解き、いちばん少ない機能でアイデアを確かめる。Karpathyはこれをこう言い表しています：「割引価格を計算したいだけなら、ECエンジンは必要ない」。

実践では、「シンプル・ファースト」は次のような具体的な操作の習慣を意味します：

- AIには一度にひとつの機能だけを実装させる。システム全体を一気に説明しない。
- 複雑な依存関係を追加するより、標準ライブラリとシンプルな方法を優先する。
- 50行で済む問題を、AIに500行書かせない。
- AIの出力が期待の範囲を超えたら、思いきって「余計な部分は削って」と伝える。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">場面</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">作りすぎの案（避けるべき）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">シンプルな案（おすすめ）</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">データを保存したい</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MySQLデータベース＋ORMを構築する</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">まずはJSONファイルかSQLiteを使う</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ユーザーのログインが必要</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OAuth2.0＋JWT＋ロール権限</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">まずはシンプルなパスワード認証から</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">フロントエンドのフレームワークが必要</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">React + Redux + Router</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">まずは素のHTML＋ネイティブJSを試す</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">デプロイして公開したい</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Docker + CI/CD + K8s</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">まずはローカルで動くことを確認してから</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
よくある場面での「作りすぎの案」と「シンプルな案」の比較

#### 三、原則三：Surgical Changes（ピンポイント修正）

すでにあるプロジェクトを手入れしていくときは、毎回の修正を外科手術のように精密に——直すべきところだけを直し、触れてはいけないところには触れない。これはAIプログラミングではとりわけ大事です。AIには「ついでに直しておこう」という癖があるからです：バグをひとつ直してと頼んだのに、ファイルの半分をリファクタリングして返してくることがあります。

「ピンポイント修正」でいちばん大事なのは、AIに出す指示ごとに、直す範囲と境界をはっきり指定することです。「calculate_discount関数だけを直すこと」「ほかの部分には触れないこと」「今のコードのスタイルを保つこと」と伝えます。AIの修正が頼んだ範囲を超えたら、すぐに余計な部分を元に戻すよう求めましょう。

Karpathyはdiff（差分）の例でこれを説明しています。買い物カゴの割引計算関数に「会員価格」のロジックを追加させるとしましょう。良い出力は、この関数ひとつだけを直して数行を足すもの。悪い出力は、ファイル全体を作り直してしまうもの——新しいコードのほうが「エレガント」に見えても、新しいバグを持ち込んでいないかは保証できません。AIプログラミングでは、「見た目が良くなった」ことは、指示から外れてよい理由には決してなりません。

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
悪い指示（範囲があいまい）

{class="font-mono text-xs leading-relaxed"}
このプロジェクトの 割引計算ロジックを改善して
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
良い指示（範囲をピンポイント指定）

{class="font-mono text-xs leading-relaxed"}
cart.pyのcalculate_discount関数だけを修正： 1. 既存の割引に会員価格のロジックを追加する 2. 会員ユーザーはさらに10%の割引 3. 関数シグネチャと他の関数は修正しない 4. 既存の変数命名のスタイルを守る
:::
:::

#### 四、原則四：Goal-Driven Execution（目標駆動実行）

この原則は、大事な問いに答えてくれます：AIには「どうやるか」の指示を出すべきか、それとも「何をするか」の指示を出すべきか？Karpathyの答えは後者です。「まずクラスを作って、次にメソッドを足して、テストを書いて」と伝えるより、「CSVファイルを読み込んで、各列のユニークな値の数を数えるツールが欲しい」と伝えるほうがうまくいきます。実装の道筋はAIに任せ、あなたは成果を受け入れる側に回ります。

「目標駆動」のメリットは二つあります。AIにとっては、より広い裁量の余地が生まれ、あなたの途中の手順に縛られず最適な実装ルートを選べます。あなたにとっては、意識を「どうやるか」から「できあがりが正しいか」へ移せる——これこそ指揮官のやるべきことです。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：目標駆動 ≠ すべて丸投げすること

{class="mt-1"}
AIが実行を終えたあとは、厳しく受け入れ確認をすることが前提です：結果は要件を満たしているか？境界のケースは処理されているか？明白な作りすぎはないか？期待と違っていたら、具体的なフィードバックを返します——「書き直して」ではなく、「ここは空のリストを入力するとIndexErrorが出ます。空チェックを足してください」と伝えるのです。
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">指示のスタイル</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">例</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">結果の特徴</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">命令型（どうやるか）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">「まずDataParserという名のPythonクラスを作り、parseメソッドをひとつ追加して、filename引数を受け取り、csvモジュールで読み込んで…」</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AIはただのタイピストになる。あなたの途中の手順が最適ルートとは限らない</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">目標型（何をするか）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">「CSVファイルを読み込み、各列のユニークな値の数を数え、JSON形式で出力するツールが欲しい。完全な実装を示してください。」</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AIが自ら最適なルートを選び、あなたは成果を受け入れる</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
命令型の指示と目標型の指示の比較

#### 五、原則五：Iterate and Verify（反復検証）

これは本書がKarpathyの四原則に加えた五つ目の原則です。中核にある信念はこうです：AIの最初の出力は、ほとんどの場合、最終版ではない。効果的なAIプログラミングとは「生成—検証—修正」の反復ループであって、一回きりの「指示—出力」ではない、と。

「反復検証」は受動的な「ダメならもう一回」ではなく、構造化された検証のプロセスです。AIが出力を返してくるたびに、三つの層で確かめます：

- 第一層・機能検証：動くか？入出力は正しいか？
- 第二層・境界検証：空の入力、長すぎる入力、変な入力ではどうなるか？
- 第三層・アーキテクチャ検証：コードの構造は妥当か？ハードコーディングはないか？あとでの拡張はしやすいか？

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-bullseye mr-1"></i> 目標を定める</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> AIがコードを生成</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> 機能の検証</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> 合格</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> 境界値検証</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> 合格</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-landmark mr-1"></i> アーキテクチャレビュー</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> 合格、次のステップへ</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> 不合格</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> 具体的なフィードバックを与える</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> 再生成</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
図2：AIプログラミングの反復検証ループ
:::

このループでカギになるのが「具体的なフィードバックを返す」という一手です。検証が通らなかったときは、「違う、やり直して」ではなく、「この関数は空のリストを入力するとIndexErrorが出ます。15行目に空チェックを足してください」と伝えます。具体的なフィードバックならAIはピンポイントで直せます。あいまいなフィードバックは、あなたの意図を推測し直させるだけです。

#### 六、Harness Engineering：Agent = Model + Harness

2026年の半ばごろから、Harness Engineeringという概念がAIプログラミングのコミュニティで広まり始めました。その中核となる公式はとてもシンプルです：

:::inline div .quote-line .text-center .text-base .font-bold
<strong>Agentの能力 = モデル能力 × Harnessの質</strong>
:::

モデルの能力は、AIという脳の知能の上限です。Harnessはモデルを取り巻くように作られた「作業環境」——コンテキスト管理、ツール統合、処理の流れの設計、記憶システムなどを指します。

この概念は、よくある疑問を説明してくれます：同じGPT-4やClaudeを使っていても、なぜ驚くようなプロジェクトを作れる人と、平凡なコードしか得られない人がいるのか？違いはモデルではなくHarnessにあります。良いHarnessには、明確なプロジェクト仕様のファイル、妥当なツール統合、整理された対話コンテキスト、行き届いた検証の流れが含まれます。モデルは知能の上限を決め、Harnessはその上限をどこまで発揮できるかを決めるのです。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
天才インターン生のたとえ

{class="mt-1"}
モデルを天才インターン生だと思ってください——知能はとても高いけれど、プロジェクトの背景資料を渡さず、どのツールを使うかも教えず、期限と受け入れ基準も設定しなければ、良いものは作れません。Harness Engineeringとは、「天才インターン生のために作業環境をちゃんと整えてあげる」ためのエンジニアリングなのです。
:::

本書のこのあとの章は、本質的にはすべて、良いHarnessの作り方を教えています：第三十九章はコンテキスト管理（プロジェクト記憶システム）、第四十章は要件定義（PRD）、第四十三章は対話技術（プロンプトの階層化）、第四十五章は品質保証（検証の流れ）。これらを組み合わせたものが、あなたのHarnessです。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
やってみよう：「思考のトライアングル」で次のアイデアを分解しよう

{class="mt-1"}
ずっと作りたかったのに手を出せずにいる小さなもの（例：カウントダウンのWebページ、水分補給リマインダーのスクリプト）をひとつ選びます。3分かけて答えましょう：① どんな問題を解決するもの？② できあがりはどんな形？③ どんな制約（時間、技術、環境）がある？そして答えをひとつの段落にまとめます。おめでとうございます。あなたは人生で初めて「Think Before Coding」を完了しました——この段落こそ、合格点の高品質な指示です。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章のまとめ

- 五大原則はKarpathyの70行のCLAUDE.md（Star 70,000超）に由来し、本書が五つ目の「反復検証」を補足
- Think Before Coding：口を開く前に三問に答える——何をする？結果はどんな形？どんな制約がある？
- Simplicity First：AI最大の落とし穴は「作りすぎ」——割引の計算にECエンジンは不要
- Surgical Changes：外科手術のようにピンポイントで直し、AIの「ついでに直す」を拒否する
- Goal-Driven Execution：「何をするか」を伝え、「どうやるか」は伝えず、AIに自ら道筋を選ばせる
- Iterate and Verify：三層の検証（機能／境界／アーキテクチャ）＋具体的なフィードバックで反復する
- Harness Engineering：能力 ＝ モデル × Harness。AIを「天才インターン生」とみなし、環境を整えて管理する
:::
