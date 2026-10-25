---
id: di-er-shi-zhang-termux
part: jin-jie-pian
nav:  第二十章付録
toc: sub
kind: supplement
---

### 第二十章付録：Termux——Androidデバイス上のポータブルLinuxターミナル環境

{class="chapter-intro mb-4"}
開発者モードでもまだ「ハードコア」不够だと思い、スマホで完全なLinuxコマンドラインを体験したいなら、Termuxはまさにあなたのためにあります。Root不要で、普通のAndroidスマホをポータブルLinuxワークステーションに変え、応用ユーザーがモバイル開発と運用保守を探求する強力なツールです。

#### 一、Termuxとは

Termuxの核心的優位性は軽量性と高い拡張性にあり、開発、学習、システム管理など多くのシーンに適しています。標準的なソフトウェアパッケージと精密なターミナルエミュレーションをオープンソースソリューションに統合しています。

二、核心機能と特徴

#### 二、核心機能と特徴

##### 🖥️ 完全なLinux環境

Termux<strong>Bash のみ内蔵</strong>という1種類の Shell のみです。Zsh や fish などの他の Shell を使いたい場合は、パッケージマネージャーで手動インストールが必要です。例：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install zsh</code>プロテクトモード<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install fish</code>。また Termux は Vim、Nano、Emacs などのエディターをサポートし、ネイティブに近いコマンドライン体験を提供します。ユーザーは「pkg install」で2000以上のパッケージをインストールでき、GCC、OpenSSH、SQLMap などの開発・セキュリティツールも含まれます。

##### 📦 強力なパッケージ管理

🔒 セキュリティとネットワーク機能

##### 🔒 セキュリティとネットワーク機能

- <strong>：SSHクライアントとサーバー機能をサポート、他デバイスへのリモート接続やスマホをSSHホストにすることが可能。</strong>暗号化ツール
- <strong>：OpenSSLなどの暗号化ツールを提供、データ暗号化とセキュア通信をサポート。</strong>サーバー構築
- <strong>：NginxやApacheを設定して静的ウェブページサーバーを構築可能。</strong>🔧 システム統合と拡張

##### 🔧 システム統合と拡張

- Termux:APIプラグインでセンサー、カメラなどAndroidハードウェア機能を呼び出し。
- Bluetoothキーボードと外部ディスプレイの接続をサポート、完全なマウスサポートあり。
- 三、プラグインエコシステム

#### 三、プラグインエコシステム

プラグイン名

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">機能説明</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Termux:API</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">コマンドラインプログラムにAndroid API機能を公開</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Boot</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">デバイス起動時のスクリプト実行を許可</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Float</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">フローティングターミナルウィンドウを提供</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Styling</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ターミナルでカラースキームとフォントカスタマイズを有効化</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Tasker</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TermuxスクリプトをTasker自動化アプリと統合</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Widget</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ホーム画面ウィジェットからスクリプト実行を許可</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">重要なヒント</td>
                            </tr>
                        </tbody>
                    </table>
```

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Termuxとそのプラグインは同じソースからインストールする必要があります、同じsharedUserIdを共有するため。異なるソース（F-DroidとGitHubなど）からの混在インストールはインストールエラーになります。

{class="mt-1"}
四、インストールと設定ガイド
:::

#### 四、インストールと設定ガイド

##### 📥 インストール手順

1. <strong>：公式チャネル（F-DroidまたはGitHub）からTermuxをダウンロードインストール、Root不要。</strong>システム初期化
2. <strong>：初回起動後「Installing bootstrap packages」の完了を待つ。</strong>ストレージ権限の取得
3. <strong>：</strong>pkg update &amp;&amp; pkg upgrade<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">を実行してスマホファイルシステム権限を取得。</code>ソフトウェアソースの更新
4. <strong>：</strong>pkg update &amp;&amp; pkg upgrade<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Pythonをインストール：</code>⚙️ 基本最適化

##### ⚙️ 基本最適化

- <strong>：</strong>termux-change-repo<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">コマンドでグラフィカルインターフェースからミラーソースを変更（清華大学ミラーソースを推奨）。</code>ショートカットキー設定
- <strong>：音量下キーがCtrlを、音量上キーがEscをエミュレート、入力効率を向上。</strong>インターフェース美化
- <strong>：Zsh + Oh My Zshをインストール、テーマとプラグインを設定。</strong>五、典型的な応用シーン

#### 五、典型的な応用シーン

##### 💻 モバイル開発テスト

🖥️ サーバー運用保守

##### 🖥️ サーバー運用保守

📚 Linux操作の学習

##### 📚 Linux操作の学習

リアルな Linux 環境を提供し、コマンドラインやシステム管理の学習に理想的なプラットフォームです。Shell スクリプト作成、Linux ファイル権限管理（例： <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chmod 755</code> で rwxr-xr-x 権限を設定、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chown user:group</code> でファイル所有者を変更、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls -l</code> で owner/group/other の3組9桁の権限を確認）などの基本コマンドを練習できます。これは Unix/Linux の古典的な「3組9桁」権限モデル（owner / group / other × 読み / 書き / 実行）で、Windows NTFS の ACL アクセス制御リストとは完全に異なる体系であることに注意してください。

##### 🔐 ネットワークセキュリティテスト

六、バージョンと互換性

#### 六、バージョンと互換性

まとめ

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Termuxは強力なLinuxターミナル体験をAndroidデバイスにもたらし、スマホをポータブルな開発・学習ツールにします。開発者、システム管理者、技術愛好家のいずれも、Termuxを活用してモバイルデバイスで完全なコマンドライン体験を楽しみ、「ポケットの中のLinux」という理念を実現できます。

{class="mt-1"}
やってみよう：スマホで最初のLinuxコマンドを実行
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>F-DroidからTermuxをダウンロードインストール、初回起動で初期化完了を待つ。

{class="list-decimal pl-6 mt-1 space-y-1"}
1. pkg update &amp;&amp; pkg upgrade
2. を実行してパッケージを更新。<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Pythonをインストール：</code> pkg install python
3. 。<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python3 -c "print('Hello from Termux!')"</code>。
4. 四、超越編（第21-26章）<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">この編ではより深いデジタル世界にご案内します。情報セキュリティからAIの原理、プログラミング思考からデジタル遺産まで、これらのコンテンツはあなたを真のデジタル市民にします。</code>第二十一章：モバイルネットワークと情報セキュリティの深掘り
:::
