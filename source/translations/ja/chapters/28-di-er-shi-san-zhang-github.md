---
id: di-er-shi-san-zhang-github
part: chao-yue-pian
nav:  附：GitHub入門ガイド
toc: sub
kind: chapter
---

### 第二十三章付録：GitHub入門ガイド——コードホスティングからコラボレーションプラットフォームまで

{class="chapter-intro mb-4"}
前章で「プログラミング的思考」を説明しましたが、プログラミング的思考を実践し、他の人と一緒にプロジェクトを行うには、GitHubという名前を避けて通れません。コンピュータ専攻の学生がコンテストに参加する、自分のコード作品を保存したい、あるいは単に世界中の開発者が何に取り組んでいるか見たい場合でも、GitHubは必ず知っておくべきプラットフォームです。この節では最も基礎的な概念から説明し、明確な認識を構築します。

#### 一、GitHubとは何か？

例えで理解すると：<strong>Gitはあなたのパソコン上の日記帳、GitHubは公開のブログプラットフォーム</strong>——自分の作品を公開し、他の人のプロジェクトをフォローし、議論やコラボレーションに参加できます。それは「プログラマーのバックヤード倉庫」にとどまらず、世界中の開発者が共同で構築する「テクノロジーシティ」のようなものです——プロジェクトはここで生まれ、反復され、議論され、再利用されます。

一般の人にとってもGitHubは決して縁遠いものではありません。多くの非プログラマーがノート、電子書籍、個人ブログのホスティングに利用し、設定ファイルのバックアップにも使っています。「自分のものを整理して共有したい」というニーズが少しでもあれば、GitHubを知る価値があります。<strong>二、GitとGitHubの違い（重要概念！）</strong>初めて触れる人はこの2つの言葉を混同しがちです。ここで整理しましょう：

比較項目

#### 二、GitとGitHubの違い（重要概念！）

GitHub

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">本質</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">バージョン管理ツール（ソフトウェア）</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">コードホスティングプラットフォーム（ウェブサイト）</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">実行場所</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ローカルパソコン上</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">クラウド（ブラウザでアクセス）</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">核心の役割</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ファイルの各変更を記録（何を変更したか、誰が変更したか、いつ変更したか）</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gitリポジトリをクラウドに置き、保存・表示・コラボレーションを容易に</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ネットワーク要否</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不要、オフラインで使用可能</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ネットワーク接続が必要</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">帰属</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">オープンソースソフトウェア、Linus Torvalds（Linuxの父）が作成</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Microsoft傘下製品</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">同等の競合製品</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SVN、Mercurial</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitLab、Gitee（碼雲）、Bitbucket</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">簡単に言うと：</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gitは「変更をどう記録するか」を管理し、GitHubは「変更をどこに置き、どうコラボレーションするか」を管理します</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">。Gitはツールでローカル実行、GitHubはプラットフォームでGitリポジトリをクラウドに置き、コラボレーションと表示を容易にします。Gitだけを使ってGitHubを使わないこともできます（例えば自分でコードを書いてバージョン管理するだけ）が、GitHubを使うには必ずGitが必要です（GitHubはGitに基づいているため）。</td>
                            </tr>
                        </tbody>
                    </table>
```

三、GitHubの核心概念と機能<strong>📁 基礎概念</strong>作業を始める前に、いくつかの高頻度ワードを知っておきましょう。そうしないとGitHubのインターフェースを見ても混乱するだけです：

#### 三、GitHubの核心概念と機能

##### 📁 基礎概念

コミット（Commit）

- <strong>：コードの一回の変更記録。各コミットには説明情報が付属し、「今回何を変更したか、なぜ変更したか」を記録します。これがGit/GitHubで「タイムトラベル」ができる基礎です。</strong>ブランチ（Branch）
- <strong>：メインラインから分岐した独立した開発ライン。新機能を追加したい場合、ブランチを切って単独で開発し、完了後にメインラインにマージすれば、他の人に影響を与えません。</strong>クローン（Clone）
- <strong>：クラウドのリポジトリをローカルパソコンに完全にコピーし、以降はローカルでコードを修正できます。</strong>プッシュ（Push）／プル（Pull）
- <strong>：PushはローカルコードをGitHubクラウドにアップロードすること、PullはGitHubから最新コードをローカルにダウンロードすること。チームコラボレーションでコードを同期する2つのコアアクションです。</strong>プルリクエスト（Pull Request、略称PR）
- <strong>：あるブランチでコードを修正し終え、メインブランチにマージしたい時、PRを発行し、チームメンバーにコードをレビューしてからマージしてもらいます。GitHubコラボレーションの核心メカニズムです。</strong>イシュー（Issue）
- <strong>：バグ、機能要件、議論トピックを記録するために使用。各Issueは一つの掲示板スレッドのようなもので、担当者を割り当てたり、ラベルを付けたりできます。</strong>Fork
- <strong>：他人のリポジトリを自分のアカウントにコピーし、自分のコピー上で自由に修正でき、元のリポジトリに影響を与えません。修正完了後、元の作者にPRを送り、改善のマージを依頼できます。</strong>🛠️ 核心機能
- <strong>GitHubが提供するのはコード保存だけではありません：</strong>バージョン管理

##### 🛠️ 核心機能

チームコラボレーション

- <strong>：複数ユーザーによる同一プロジェクトの並行開発をサポートし、複数人が同時に開発しても上書きや競合が発生しません。</strong>問題追跡
- <strong>：Issueでバグや機能要望を記録し、チームでのフォローアップが容易に。</strong>プロジェクト管理
- <strong>：ToDoリスト、プロジェクトかんばん（Projects）などの管理ツールを統合し、軽量なTrelloを内蔵しています。</strong>オートメーション
- <strong>：</strong>GitHub Actions
- <strong>でコードコミット後の自動コンパイル、テスト、パッケージング、デプロイを実現し、現代の「CI/CD（継続的インテグレーション／継続的デプロイ）」の中核ツールです。</strong>ドキュメント管理<strong>：READMEでプロジェクトを紹介し、Wikiで詳細なアーキテクチャや開発規範を保存し、Pagesでは静的ウェブサイトを直接ホスティングできます。</strong>コードホスティングと表示
- <strong>：各リポジトリには美しいウェブページ表示があり、シンタックスハイライトをサポートし、あなたの技術作品の「看板」になります。</strong>オープンソースコミュニティ
- <strong>：好きなプロジェクトをStar（お気に入り）し、プロジェクトの動向をWatch（フォロー）し、開発者をFollow（フォロー）して、グローバルなオープンソースコラボレーションに参加できます。</strong>四、登録と使い始め：5分で最初のリポジトリを作成
- <strong>📝 アカウント登録</strong>github.com

#### 四、登録と使い始め：5分で最初のリポジトリを作成

##### 📝 アカウント登録

1. github.com/yourname<a href="https://github.com" class="text-primary hover:underline" target="_blank" rel="noopener">）。</a>メール認証とロボット認証を完了。
2. 無料プラン（Free）を選択すれば十分です。個人ユーザーには完全に対応しています。<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">📁 最初のリポジトリを作成</code>ログイン後、右上の「+」をクリックし、「New repository」を選択。
3. リポジトリ名（Repository name）を入力、例：
4. my-first-project

##### 📁 最初のリポジトリを作成

1. 簡単な説明（Description）を書き、他の人がこのリポジトリの目的をわかるようにします。
2. Public（公開）またはPrivate（非公開）を選択。公開リポジトリは誰でも閲覧可能、非公開は自分と共同作業者のみ閲覧可能。無料アカウントでも無制限の非公開リポジトリをサポートしています。<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">「Add a README file」にチェックを入れる——READMEはプロジェクトの「取扱説明書」で、各リポジトリに用意することを推奨します。</code>。
3. 豆知識：READMEとは
4. README.mdはMarkdown形式のファイルで、他の人があなたのリポジトリを開いた時に最初に目にする内容です。良いREADMEには通常、プロジェクトの概要、インストール方法、使用例、ライセンス、連絡先が含まれます。READMEを書くことはプログラマーの基本素養であり、プロジェクトが他の人に使用されるかどうかの最初の関門でもあります。
5. 五、基本ワークフロー：ローカルからクラウドへ
6. GitHubのワークフローを理解するには、このサイクルを覚えるのが核心です：

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>ローカルで修正 → ステージ → コミット → プッシュ → クラウド更新

{class="mt-1"}
。各ステップを分かりやすく説明します：
:::

#### 五、基本ワークフロー：ローカルからクラウドへ

：ローカルパソコンでエディタを使ってコードを書いたりドキュメントを修正したりします。<strong>git add</strong>：修正したファイルを「ステージングエリア」に追加し、Gitに「これらの変更を記録する準備ができた」と伝えます。

1. <strong>git commit</strong>：ステージングエリアの変更を正式に一つの「コミット」として記録し、説明を付けます。例：「ログインバグを修正」。このステップはローカルでのみ完了します。
2. <strong>git push</strong>：ローカルのコミットをGitHubクラウドにアップロードし、他の人が見られるようにします。
3. <strong>git pull</strong>：作業を始める前に、まずクラウドから最新コードをプルし、ローカルがチームの他のメンバーと同期していることを確認します。
4. <strong>初心者はこの呪文を覚えてください：</strong>「まずpullしてから修正、修正したらadd、commitには説明を付け、最後にpush」
5. <strong>。この習慣を身につければ、チームコラボレーションが乱れることはありません。</strong>六、チームコラボレーションフロー：プルリクエストはどう機能するか

GitHubの最も強力な点はコラボレーションメカニズムです。典型的なチームコラボレーションフローは次の通りです：<strong>ブランチを切る</strong>：メインブランチ（通常mainまたはmaster）から新しいブランチを切り、例：

#### 六、チームコラボレーションフロー：プルリクエストはどう機能するか

、このブランチで新機能を開発します。

1. <strong>開発してコミット</strong>：新しいブランチでコードを書き、複数回commitして進捗を記録します。<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">GitHubにプッシュ</code>：ブランチをクラウドリポジトリにpushします。
2. <strong>プルリクエストを発行</strong>：GitHubウェブページでPRを発行し、あなたのブランチをメインブランチにマージするよう依頼します。このPRで何を変更したか、なぜ変更したかを明確に書きます。
3. <strong>コードレビュー（Code Review）</strong>：チームメンバーがあなたのコードを確認し、意見や修正提案を提示します。フィードバックに基づいてコミットを続けると、PRは自動的に更新されます。
4. <strong>マージ</strong>：レビュー通過後、「Merge」をクリックしてコードをメインブランチにマージします。あなたの貢献が正式にプロジェクトに取り込まれました！
5. <strong>このフローにより、</strong>コードがメインブランチに入る前に必ずレビューが行われる
6. <strong>ことが保証され、エラー発生確率が大幅に下がります。オープンソースプロジェクトもこのメカニズムで世界中の見知らぬ人からの貢献を受け入れています——有名なオープンソースプロジェクトでPRを提出し、採用されれば、あなたはそのプロジェクトの貢献者になれます。</strong>七、GitHubの典型的な応用シナリオ

🎓 学生のコンテスト参加と課題プロジェクト<strong>コンピュータ専攻の学生がACM、ハッカソン、卒業制作に参加する際、GitHubはほぼ欠かせません。チームコラボレーションプラットフォームとしても、作品展示ウィンドウとしても機能します——コンテストの審査員はあなたのリポジトリを直接見て、コード品質とコラボレーション過程を理解できます。多くの企業の採用時にもGitHubページの添付を求め、技術力の証明にします。</strong>📚 個人ナレッジベースとノートホスティング

#### 七、GitHubの典型的な応用シナリオ

##### 🎓 学生のコンテスト参加と課題プロジェクト

GitHubはグローバルなオープンソース運動の核心拠点です。好きなプロジェクトをForkし、修正後にPRでコミュニティに還元できます。また、単にStarでお気に入りのプロジェクトをブックマークし、更新を追跡することもできます。オープンソースへの参加は技術向上と評価蓄積の絶好の道です。

##### 📚 個人ナレッジベースとノートホスティング

GitHub Actionsを活用し、「コードをpushしたら、自動テスト＋サーバーへの自動デプロイ」というフルオートフローを実現できます。多くの個人ブログやドキュメントサイトがこの方法で構築され、記事を書いてpushするだけでサイトが自動更新されます。

##### 🌐 オープンソースプロジェクトへの参加

コードリポジトリをクラウドストレージとして使い、パソコンを替えたりマルチデバイスで作業したりする際、git pull一回で最新コードを取得でき、USBメモリでコピーし回る必要がなくなります。

##### 🤖 オートメーションデプロイとCI/CD

コミットメッセージを明確に書く

##### 💾 コードバックアップとマルチデバイス同期

こまめにコミット、小刻みに進める

#### 八、初心者へのアドバイス

- <strong>ブランチで開発し、メインブランチを直接修正しない</strong>：個人プロジェクトでもブランチを切る習慣を身につければ、将来チームコラボレーション時に慌てません。
- <strong>.gitignoreを活用</strong>：このファイルでGitにどのファイルをバージョン管理から除外するかを指定します（例：パスワード設定、コンパイルの産物、依存フォルダ）。ゴミファイルのアップロードを防ぎます。
- <strong>優秀なオープンソースプロジェクトを多く見る</strong>：GitHub Trendingを巡回し、高スターのプロジェクトのコード構造、READMEの書き方、コラボレーションフローを見るのは、最も速い無料の向上方法です。
- <strong>GitHub学生パックを申請</strong>：学生認証後、多数の有料ツールやサービスの無料枠（Copilot、ドメイン、クラウドサービスなど）を獲得でき、価値は数千ドルに上ります。
- <strong>セキュリティリマインダー</strong>パスワード、APIキー、データベース接続文字などの機密情報をGitHubにコミットしないでください。特に公開リポジトリでは——一度漏洩するとクローラーに即座に取得され、深刻な結果をもたらします。
- <strong>誤って機密情報をコミットした場合、ファイルを削除するだけでは不十分です（履歴に残っています）。</strong>git filter-branch

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>セキュリティに関する注意

{class="list-disc pl-6 mt-1 space-y-1"}
- 非公開リポジトリも絶対に安全ではありません。機密情報は環境変数で管理し、コードリポジトリに入れないのが最善です。
- 中国国内からのGitHubアクセスの注意点<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">GitHubは中国国内からのアクセスが時に不安定で、開けない、クローンが遅い場合があります。次の対策を試してください：① 国内ミラーサイト（GitClone、ghproxyなど）でクローンを加速；② Hostsの設定やプロキシの使用；③ 主に国内コラボレーションが目的なら、国産代替の</code> Gitee（碼雲）
- も検討でき、機能は類似しアクセス速度も速いです。多くのチームがGitHubとGiteeの両方でホスティングし、グローバル化と国内速度を両立しています。
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>応用編：GitHub Pagesで無料個人ブログを構築

{class="mt-1"}
GitHub Pagesを使えば無料で静的ウェブサイトをホスティングでき、Jekyll、Hexo、Hugoなどの静的サイトジェネレーターと組み合わせれば、個人ブログを簡単に構築できます。Markdown記事を書いてリポジトリにpushするだけでブログが自動更新され、HTTPSとカスタムドメインも標準装備です。無数の技術ブロガーのブログがこの方法で構築され、コストゼロ、広告なし、バージョン管理可能です。<strong>九、まとめ：なぜ誰もがGitHubを知るべきか</strong>GitHubはもはや「プログラマーのツール」ではなく、
:::

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>デジタル時代の仕事方式

{class="mt-1"}
です：バージョン管理がすべてを追跡可能にし、コラボレーションメカニズムがチームを効率的に運営し、オープンソース精神が知識を自由に流通させます。コードを書かなくても、「コミット、ブランチ、マージ」という概念を理解すれば、「反復修正＋多人数コラボレーション」が必要なあらゆるコンテンツの管理に役立ちます——論文からドキュメント、ノートから企画書まで。
:::

#### 九、まとめ：なぜ誰もがGitHubを知るべきか

実践：GitHub初体験を完了<strong>GitHubアカウントを登録し、プロフィールを整える（アバター、自己紹介、興味のある技術分野）。</strong>hello-github

という公開リポジトリを作成し、「Add a README file」にチェックを入れる。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>リポジトリに入り、README.mdの編集ボタン（鉛筆アイコン）をクリックし、Markdownで自己紹介を書いて変更をコミット。

{class="list-decimal pl-6 mt-1 space-y-1"}
1. GitHubの検索バーで興味のあるキーワード（例：
2. python-tutorial<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">）を検索し、好きなプロジェクトを2つStarする。</code>（応用）パソコンにGitをインストールし、リポジトリをローカルにCloneし、READMEを修正後にクラウドにpushし、完全な「ローカル→クラウド」ワークフローを完了。
3. 第二十四章：Root権限とBLロックの深掘り解説
4. この章は第二十章の内容を深く掘り下げるもので、スマートフォンの基盤メカニズムを真に理解したい、あるいはフラッシュを試みたいユーザー向けです。これらの操作にはリスクがあるため、慎重に行ってください。<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">一、Bootloaderの深い理解</code> Bootloaderはスマートフォン起動時に最初に実行されるプログラムで、ハードウェアの初期化、OSカーネルの読み込みを担当します。Bootloaderはスマートフォンの「門番」と理解できます。
5. BLロックの動作原理：
:::
