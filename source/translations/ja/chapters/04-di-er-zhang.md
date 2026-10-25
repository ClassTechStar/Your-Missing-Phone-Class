---
id: di-er-zhang
num: 02
part: ji-chu-pian
nav: 第二章：デジタルの部屋を片づける
toc: default
kind: chapter
---

### 第二章：デジタルルームを整理する——ファイル管理

{class="chapter-intro mb-4"}
スマートフォンを長く使うと乱雑になる。良い習慣はファイル管理から始まる。部屋を定期的に整理する必要があるのと同じように、デジタル空間も手入れが必要だ。整然としたスマートフォンは、物を探しやすいだけでなく、動作もより滑らかになる。

#### 一、3層ストレージ体系：あなたのデジタル倉庫

{class="list-decimal pl-6 mb-3 space-y-2"}
1. <strong>本体ストレージ</strong>：コア領域で、速度が速く、システムとアプリがここにある。スマートフォンで最も貴重な空間で、慎重に管理すべき。
2. <strong>SDカード（サポートの場合）</strong>：拡張クローゼットで、速度は遅いが、映画、写真などの大容量ファイルに適する。注意：現在多くのフラッグシップ機はSDカードをサポートしない。
3. <strong>クラウドストレージ</strong>：金庫＋同期ドライブ。紛失防止と複数デバイス間同期が可能。iCloud、Baidu Netdisk、OneDriveなどがよく使われる。

#### 二、「ファイルマネージャー」を知る

Androidには通常 [ファイル] または [ファイル管理] アプリがあり、iOSは標準の [ファイル] アプリだ。これらはスマートフォンのすべてのファイルを表示する「エクスプローラー」だ。

##### 一般的なフォルダの意味：

- <strong>DCIM</strong>：カメラで撮影した写真と動画。
- <strong>Pictures</strong>：その他の画像、スクリーンショット、保存した画像など。
- <strong>Download</strong>：ブラウザでダウンロードしたファイル。
- <strong>Music</strong>：音楽ファイル。
- <strong>Movies</strong>：動画ファイル。
- <strong>Documents</strong>：ドキュメントファイル。
- <strong>Android</strong>：Androidシステムフォルダで、中に各アプリのデータがある。通常は手動削除しないこと。

#### 三、ファイルシステム構造：より深く理解する

AndroidはLinuxベースで、ファイルシステムには一定の階層構造がある。一般ユーザーが深く理解する必要はないが、基本的な概念を知っておくと役立つ。

##### ストレージパーティション：

- <strong>/system</strong>：システムパーティションで、オペレーティングシステムファイルを格納。一般ユーザーはアクセス権限がなく、root権限が必要。
- <strong>/data</strong>：データパーティションで、ユーザーデータとアプリデータを格納。日常使用する空間。
- <strong>/sdcard または /storage/emulated/0</strong>：ユーザーがアクセス可能なストレージ空間で、写真やダウンロードファイルはここにある。

##### アプリデータストレージ：

- <strong>内部ストレージ</strong>：アプリのプライベート空間で、他のアプリはアクセス不可。アプリアンインストール時に削除される。
- <strong>外部ストレージ</strong>：アプリがユーザーアクセス可能領域に保存するファイル、例えば写真、ダウンロードコンテンツ。アプリアンインストール時に必ずしも削除されない。

#### 四、データバックアップと復元：データに保険をかける

データはプライスレス、バックアップは必須の習慣だ。

##### バックアップ戦略：

1. <strong>クラウドバックアップ</strong>：自動で便利だが、ネットワークとクラウド容量が必要。iCloud、Huawei Cloud、Xiaomi Cloudなどがサポート。
2. <strong>ローカルバックアップ</strong>：データケーブルでパソコンに接続し、公式ツールでバックアップ。速く容量が大きいが、手動操作が必要。
3. <strong>二重バックアップ</strong>：クラウドバックアップ＋ローカルバックアップで最も安全。

##### 何をバックアップする？

- <strong>写真と動画</strong>：最も容量を占有し、最も貴重。
- <strong>連絡先</strong>：クラウドアカウントに保存するのが最も便利。
- <strong>WeChatチャット履歴</strong>：WeChat内蔵のバックアップ機能を使用。
- <strong>重要ドキュメント</strong>：クラウドドライブやパソコンに保存。

#### 五、ファイルセキュリティ：プライバシーを守る

- <strong>センシティブファイルの暗号化</strong>：多くのスマートフォンには「セキュアフォルダ」や「プライベート空間」機能があり、センシティブファイルを入れ、パスワードや指紋でアクセスできる。
- <strong>削除≠抹消</strong>：通常の削除は空間が上書き可能というマークをつけるだけで、データは残っている。完全に削除するには、専用の安全消去ツールを使用するか、複数回上書き書き込みが必要。
- <strong>クラウドセキュリティ</strong>：信頼できるクラウドサービスプロバイダーを選び、二要素認証を有効化し、定期的にログインデバイスを確認。

#### 六、容量が足りない？大掃除をしよう

- <strong>キャッシュクリーン</strong>：アプリの一時記憶で、クリーンすると空き容量が増える。設定 &gt; ストレージでクリーン可能。
- <strong>大容量ファイルの検索</strong>：ファイルマネージャーでサイズ順にソートし、容量を占有する「犯人」を見つける。
- <strong>残存物の削除</strong>：アプリアンインストール後、ゴミファイルが残ることがあるので手動で削除。
- <strong>アルバムのクリーン</strong>：重複写真、ブレた写真、不要なスクリーンショットを削除。
- <strong>WeChatのクリーン</strong>：WeChatは容量の大口で、定期的なチャット履歴とキャッシュのクリーンが必須。

#### 七、一般的なファイル形式の全解析

スマートフォン内の各種ファイル拡張子は複雑だが、理解すればファイル管理がより上手になる：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                            <thead>
                                <tr class="bg-light dark:bg-gray-700">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">形式</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">タイプ</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">特性</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">推奨される開き方</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">JPG/JPEG</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">画像</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">非可逆圧縮、サイズ小、互換性最高。スマートフォン撮影のデフォルト形式。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">アルバム/任意の画像ビューアー</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">PNG</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">画像</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可逆圧縮、透明背景サポート。スクリーンショット、アイコンに常用。JPGよりサイズ大。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">アルバム/任意の画像ビューアー</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MP3</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">オーディオ</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">非可逆圧縮、サイズ小、互換性極めて高い。最も汎用的なオーディオ形式。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">任意の音楽プレーヤー</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">FLAC</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">オーディオ</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可逆圧縮、音質はCDと同等、サイズはMP3の3-5倍。オーディオマニアの第一選択。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">音楽プレーヤー/プロフェッショナル再生アプリ</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">WAV</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">オーディオ</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">無圧縮の生オーディオ、音質最高だがサイズ巨大。プロ録音に常用。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">音楽プレーヤー</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">M4A</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">オーディオ</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AACエンコード、MP3の同ビットレートより音質が良い。Appleエコシステムで常用。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Music/音楽プレーヤー</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MP4</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">動画</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最も汎用的な動画コンテナ形式、互換性極めて高い。スマートフォン録画のデフォルト形式。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">アルバム/任意の動画プレーヤー</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MKV</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">動画</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">オープンソースコンテナ形式、マルチオーディオトラック、マルチ字幕サポート。映画リソースに常用。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">VLC/nPlayer</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DOC/DOCX</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ドキュメント</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wordドキュメント。DOCXは圧縮形式でサイズがより小さい。DOCは旧形式。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">WPS/Office</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">PPT/PPTX</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">プレゼン</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">PowerPointプレゼン資料。PPTXは圧縮形式。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">WPS/Office</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">XLS/XLSX</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">スプレッドシート</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Excelスプレッドシート。XLSXは圧縮形式。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">WPS/Office</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">PDF</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ドキュメント</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">クロスプラットフォーム形式、レイアウト固定で編集不可。契約書、論文、電子書籍に常用。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Adobe Reader/WPS</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ZIP</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">圧縮</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最も汎用的な圧縮形式、クロスプラットフォーム互換性良好。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">システム標準/解凍アプリ</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">RAR</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">圧縮</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">圧縮率はZIPより高いが、専用ソフトでの解凍が必要。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">解凍アプリ</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ISO</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">イメージ</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">光ディスクイメージファイル、光ディスクの内容を完全にコピー。システムインストーラに常用。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">解凍アプリ/仮想光ドライブ</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">HTML</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ウェブページ</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ウェブページファイル、ブラウザで開く。保存したウェブページに常用。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ブラウザ</td>
                                </tr>
                            </tbody>
                        </table>
```
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>練習：「ダウンロード」フォルダを整理

{class="mt-1"}
ファイルマネージャーを開き &gt; 「ダウンロード」フォルダに入る。中に何があるか？不要なものを削除し、有用なものを分類（例えば「仕事資料」「スタンプ」フォルダを作成して入れる）。ついでにストレージ容量を確認し、どのタイプのファイルが最も多く占有しているか把握する。
:::

{class="text-lg font-semibold mt-6 mb-2"}
#### 八、画像とファイルシステム管理：資産を整然と

前節で「フォルダを知る」ことを学んだが、知るだけでは不十分。本節では<strong>長期的に実行可能な管理規範を主体的に構築する方法</strong>を説明し、ファイルがいつでも見つかり、失われず、覗き見されないようにする。

{class="font-semibold mt-4 mb-1"}
##### 1. ファイル分類と命名規範

混乱の根源はルールがないこと。ルールの構築は実は簡単で、重要なのは<strong>継続</strong>。

```html
<ul class="list-disc pl-6 mb-3 space-y-2">
                        <li><strong>「時間＋イベント」命名法</strong>：フォルダ名にタイムスタンプとイベント記述を含め、後日の回想と検索に便利。例えば <code>202606_旅行チケット</code>、<code>2025年年末まとめ</code>、<code>2024子供の誕生日</code>。これでタイムラインが見え、内容も一目で分かる。</li>
                        <li><strong>3階層分類体系</strong>：
                            <ul class="list-disc pl-6 mt-1 space-y-0.5">
                                <li><strong>第1層</strong>：ファイルタイプ別（ドキュメント / 画像 / 動画 / オーディオ）</li>
                                <li><strong>第2層</strong>：使用シーン別（仕事 / 生活 / 学習）</li>
                                <li><strong>第3層</strong>：具体的なイベントやプロジェクト別（例：「2026Q2_プロジェクトA」）</li>
                            </ul>
                        </li>
                        <li><strong>月次クリーン計画</strong>：毎月固定日付（給料日や月初1日を推奨）に、「ダウンロード」ディレクトリを一括整理：<strong>有用なものをアーカイブ、不要なものを削除、貴重なものを転送保存</strong>。年12回の小整理は、1年分の大掃除よりはるかに楽。</li>
                    </ul>
```

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-calendar-check mr-2"></i>今月のタスクリスト

{class="mt-1"}
暇な週末を選び、以下の順序で操作：

{class="list-decimal pl-6 mt-1 space-y-0.5 text-sm"}
1. ファイルマネージャーで <code>2026Q2_プロジェクトA</code> 形式の今月の仕事フォルダを作成；
2. 「ダウンロード」ディレクトリ内の今週のファイルをすべて確認し、有用なものを残し、アーカイブし、不要なものを削除；
3. 今年の家族写真に <code>2025家族</code>、<code>2026家族</code> という年次フォルダを作成。
:::

{class="font-semibold mt-4 mb-1"}
##### 2. 冗長ファイル処理戦略

スマートフォンを長く使うと「太る」が、多くは冗長ファイルの仕業だ。

{class="list-disc pl-6 mb-3 space-y-2"}
- <strong>72時間自動クリーン</strong>：WeChat、QQなどソーシャルアプリが受信する一時ファイル（スタンプ、チャット画像、ショート動画）は、ほとんど一度見たら不要。[WeChat] &gt; [設定] &gt; [一般] &gt; [ストレージ] で「自動クリーン」を有効化し、期限切れキャッシュを72時間に設定。スマートフォンが瞬時にさっぱりし、重要な記録も失われない。
- <strong>ストレージ容量の指向性クリーン</strong>：Android [設定] &gt; [ストレージ] &gt; [クリーン加速]、iOS [設定] &gt; [一般] &gt; [iPhoneストレージ]で、システムが「キャッシュ / 一時ファイル / アンインストール可能アプリ / 大容量ファイル」別にリスト化。重点クリーン：① キャッシュファイル；② 期限切れインストーラ（アプリアップグレード後に残る旧版インストーラ）；③ 重複ファイル（同名同サイズの写真）。
- <strong>自動分類ルール</strong>：大部分のブランドのアルバムアプリはスマート分類をサポート：人物、風景、ドキュメント、スクリーンショット。有効化すると、新しく撮った集合写真は自動的に「人物 &gt; 張三」に分類され、スキャンした契約書は自動的に「ドキュメント」に分類される。<strong>月次整理と組み合わせることで、「物が見つからない」確率を大幅に低減</strong>。

{class="font-semibold mt-4 mb-1"}
##### 3. 画像安全処理規範

画像はスマートフォンで最も「センシティブ」なデータタイプだ——何気なく撮った1枚であなたの位置、デバイス、時間が漏れる。私たちは<strong>「二重保護」ワークフローの構築</strong>：

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-image mr-2"></i>証明写真/センシティブスクリーンショット送信の標準フロー

{class="list-decimal pl-6 mt-1 space-y-1 text-sm"}
1. <strong>可視情報のマスキング</strong>：システム標準またはサードパーティツール（Meitu XiuXiu、Snapseedなど）で<strong>身分証番号の中間数桁、ナンバープレート、部屋番号、氏名、金額</strong>などのキーフィールドを塗りつぶす；
2. <strong>メタデータ剥離</strong>：送信前にアルバムで「共有」または「エクスポート」をタップすると、システムが位置情報を保持するか尋ねるので<strong>「保持しない」</strong>を選択。これで撮影デバイスの型番、GPS座標、撮影時間が画像と一緒に送信されない；
3. <strong>一時透かし</strong>（オプション）：センシティブスクリーンショットに「XX手続き専用」のテキスト透かしを追加し、悪用を防止。
:::

{class="mt-3 mb-2"}
メタデータ（EXIF）削除の一般的な方法（基本操作、詳細な保護は第六章「写真のセンシティブ情報処理」を参照）：

- <strong>システム標準</strong>：iOS [設定] &gt; [プライバシーとセキュリティ] &gt; [カメラ]で「正確な位置」をオフにできる；共有時に「現在の写真のみ」を選択すると<strong>大部分のEXIFを自動剥離</strong>。
- <strong>Android</strong>：大部分のブランドのアルバムアプリは「共有」時に「位置情報を削除するか」を確認し、チェックを入れるだけ。
- <strong>プロフェッショナルツール</strong>：ExifTool（PC版）、Metapho（iOS）、Photo Metadata Remover（Android）ですべてのメタデータを完全に削除可能。

長期保存<strong>が必要なセンシティブ画像（身分証、銀行カード、戸籍謄本のスキャン、パスポート）は、</strong>暗号化アルバム<strong>に保存することを推奨：</strong>：

- Huawei/Xiaomi：[アルバム] &gt; 写真を長押し &gt; 「セキュアボックスに移動」；
- サードパーティ暗号化アプリ：
- 360セキュアアルバム<strong>、</strong>、<strong>、</strong>、<strong>など、単独パスワード保護で隠蔽性がより高い。</strong> 第三章：スマートフォンに「生命線」をつなぐ——ネットワーク
