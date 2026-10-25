---
id: di-san-zhang
num: 03
part: ji-chu-pian
nav: 第三章：スマホに「ライフライン」をつなぐ
toc: default
kind: chapter
---

### 第三章：スマホに「ライフライン」をつなぐ——ネットワーク

{class="chapter-intro mb-4"}
ネットワークがないと、スマートフォンは「智障」になってしまう。ネットワークは現代スマートフォンの生命線で、それを理解し、使いこなし、保護することはすべてのスマートフォンユーザーの必修科目だ。

#### 〇、接続で迷わない——Wi-Fiとモバイルデータの「道」と「車」を区別

多くの人がスマートフォンの画面上部でWi-Fiと信号アイコンが同時に点灯しているのに、両者の本質的な違いを全く理解していない。最も典型的な誤解は：<strong>Wi-Fiに接続しているのにページが読み込めない</strong>——ルーターがネットワークから切断されているのに、スマートフォンが自動的にモバイルデータに切り替わらないからだ。この問題を完全に理解するために、「道と車」の認知モデルを構築する必要がある。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-road mr-2"></i>コア比喩：道と車

{class="mt-1"}
インターネットを都市と想像してほしい。<strong>「道」</strong>はスマートフォンからインターネットまでの通道で、<strong>「車」</strong>は道を走るデータだ。Wi-Fiとモバイルデータは2つの異なる道だが、データ（車）自体は同じだ。
:::

{class="font-semibold mt-4 mb-1"}
##### 1. 本質的違い：ローカル通道 vs リモート高速道路

Wi-Fiは本質的に<strong>ローカルエリアネットワーク技術</strong>で、自宅の階下に無線で敷かれた道のようなもので、ルーターからスマートフォンまでデータを伝送する。しかしブロードバンドの未払いや光ケーブルの切断があれば、道はあっても外の「高速道路」が切れており、どこにも行けない。一方モバイルデータ（モバイルデータ通信）はキャリアの4G/5G基地局を通じて伝送され、あなたが直接キャリアの高速専用線に乗るようなもので、信号さえあれば直接インターネットに接続できる。

{class="font-semibold mt-4 mb-1"}
##### 2. 費用とシーン：定額月額 vs 従量課金

Wi-Fiは通常一回限りの投資（ブロードバンド月額）で、電気代が続く限り家族全員が無制限で使用でき、映画のダウンロードやゲームなど大容量トラフィックシーンに非常に適する。一方モバイルデータは使用量に応じて課金され、パッケージを超えると速度制限や追加課金される可能性があり、地下鉄や出張などモバイルシーンでの軽量タスク処理に適する。

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands-helping mr-2"></i>試してみよう：データパッケージを確認

{class="mt-1"}
スマートフォンの [設定] &gt; [モバイルネットワーク] &gt; [データ管理] を開き、今月の残りデータ容量と、最もデータを消費するアプリを確認。把握してから出かければ慌てない。
:::

{class="font-semibold mt-4 mb-1"}
##### 3. セキュリティ考慮：公共Wi-Fiは隠された「フィッシング場」

セキュリティの面では、モバイルデータは通常公共Wi-Fiより安全だ。モバイルデータはキャリアが暗号化するが、公共Wi-Fiはハッカーが「偽ホットスポット」を構築して暗号化されていないトラフィックを傍受しやすい。ただしここで区別が必要：HTTPSが全面普及した今日、攻撃者が傍受できるのは<strong>あなたがどのウェブサイトにアクセスしたか</strong>（ドメイン）と、<strong>暗号化されていないHTTPコンテンツ</strong>のみ。WeChatのメッセージ、銀行アプリのログインパスワードなどHTTPSで暗号化されたデータは、攻撃者は<strong>直接読み取れない</strong>——より複雑なSSLストリッピング攻撃を実施し、ユーザーが証明書警告を無視しない限り。とはいえ、外出時の決済操作では、直接スマートフォンのモバイルデータを使用するのが最も確実な選択だ。

::: div .danger-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>セキュリティリマインダー

{class="mt-1"}
空港、ショッピングモール、カフェなどの公共場所では、名前の不審な無料Wi-Fi（例：「Free_WiFi_2024」）には接続しないでください。たとえ接続しても、銀行アプリへのログインやパスワード入力は絶対に行わないでください。
:::

{class="font-semibold mt-4 mb-1"}
##### 4. スマートフォン側での判断：ステータスバーの「暗号」を読む

スマートフォンが現在何でネットワーク接続しているかを知るには？Huaweiスマートフォンを例にすると、ステータスバーのキャリア信号またはWLAN信号の横に<strong>双方向矢印アイコン</strong>が表示されれば、対応する方式でインターネットに接続中を表す。両方が同時に点灯していれば、ネットワーク加速が有効で、スマートフォンが2つの通道を同時に利用していることを示す。

iPhoneユーザーはより直感的：Wi-Fiアイコンが点灯していればWi-Fiを使用中、消灯時は右上の信号バーを見ればモバイルデータを使用中。一部のAndroidスマートフォンはステータスバーに「5G」や「4G」と表示し、現在のモバイルネットワークタイプを直接伝える。

{class="text-lg font-semibold mt-6 mb-2"}
#### 一、モバイルネットワーク（4G/5G）とデータ通信

モバイルネットワークはいつでもどこでも接続する基盤だ。2Gから5Gまで、速度は千倍以上向上したが、原理は実は似ている。

##### ネットワーク方式：

- <strong>4G LTE</strong>：現在カバレッジが最も広く、速度も十分（理論上最高100Mbps+）、消費電力が比較的低い。
- <strong>5G</strong>：速度が速く（理論上最高10Gbps）、カバレッジはまだ整備中で、消費電力が高い。大容量ファイルのダウンロードや高画質動画の視聴に適しています。
- <strong>5G SA vs NSA</strong>：SAは独立ネットワーク、NSAは4G基地局に依存。SAの方が体験が良いが、キャリアとスマートフォンの両方がサポートする必要がある。

##### データ管理：

- <strong>データ通信量とは</strong>：スマートフォンがインターネットに接続して発生するデータ量。動画視聴、画像閲覧が最もデータを消費し、テキストと音声は比較的少ない。
- <strong>節約のヒント</strong>：設定で「データ節約モード」を有効化し、Wi-Fi環境下でアプリの更新や高画質動画を視聴する。
- <strong>信号バー≠速度</strong>：信号が強いのは接続が良いことを示すだけ。速度は基地局の混雑度、基地局からの距離にも依存する。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>重要警告：海外渡航前に【データローミング】をオフに！

{class="mt-1"}
海外でモバイルデータを使用すると天文学的な請求が発生する可能性がある！海外渡航前に必ず設定でデータローミングをオフにするか、現地のSIMカードや国際ローミングパッケージを事前に購入すること。
:::

#### 二、Wi-Fi：接続、共有、セキュリティ

Wi-Fiは家庭やオフィスのインターネット接続の主力で、速度が速くデータ消費がない。しかしWi-Fiも絶えず進化しており、規格により差が大きい。

##### Wi-Fi接続：

[設定] &gt; [WLAN] でネットワークを選択しパスワードを入力。現在多くのスマートフォンはQRコード接続をサポートし、より便利。

##### パスワード共有：

AndroidとiOSはどちらも接続済みのスマートフォンから友人にパスワードを素早く共有できる。AndroidはQRコードを生成し、iOSは近接で自動共有できる。

##### Wi-Fi規格の進化：

Wi-Fi規格はIEEEが制定し、各世代で顕著な向上がある：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                            <thead>
                                <tr class="bg-light dark:bg-gray-700">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">規格</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">プロトコル</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">周波数帯</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">最高速度</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">特徴</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 4</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11n</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.4/5GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">600Mbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">旧規格、カバレッジはそこそこ</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 5</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11ac</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">5GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.5Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">現在最も普及、速度も十分</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 6</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11ax</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.4/5GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">9.6Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多数のデバイスで高性能、遅延が少ない</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 6E</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11ax</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.4/5/6GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">9.6Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6GHz帯追加、混雑なし</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 7</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11be</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.4/5/6GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">46Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">超高速転送、マルチリンク集約</td>
                                </tr>
                            </tbody>
                        </table>
```
:::

- <strong>Wi-Fi 6の主要技術</strong>：OFDMA（直交周波数分割多元接続）が複数デバイスの同時転送を可能にし、MU-MIMO（マルチユーザーマルチプルインプットマルチプルアウトプット）がマルチデバイス同時効率を向上、TWT（ターゲットウェイクタイム）がデバイスの省電力化を実現。
- <strong>Wi-Fi 6E</strong>：Wi-Fi 6をベースに6GHz帯を追加し、より多くのチャネルを提供して干渉を低減します。スマートフォンとルーターの両方が対応している必要があります。
- <strong>Wi-Fi 7</strong>：MLO（マルチリンク操作）を導入し、複数の周波数帯を同時に使用してデータ転送が可能になり、レイテンシが大幅に削減されます。320MHzの超広帯域チャネルにより速度が飛躍的に向上します。Snapdragon 8 Elite Gen5、Dimensity 9400などのフラッグシップチッププラットフォームがWi-Fi 7に対応しており、Xiaomi 17、Huawei Mate 80、Samsung S26などの機種でWi-Fi 7ネットワークを利用できます（Wi-Fi 7ルーターとの組み合わせが必要）。
- <strong>2.4GHz vs 5GHz</strong>：2.4GHzは壁貫通が良いが速度が遅く干渉が多い。5GHzは速度が速いが壁貫通が弱い。Wi-Fi 6E/7の6GHz周波数帯は速度が最も速いが壁貫通が最も弱く、同一部屋内での使用に適する。

##### 公共Wi-Fiのリスク：

公共Wi-Fiではハッカーがデータを傍受したりフィッシングホットスポットを設置する可能性がある。ルール：

- 銀行アカウントへのログイン、パスワード入力を避ける。
- 可能ならVPNで暗号化接続を使用。
- 知らないWi-Fiに自動接続しない。
- HTTPSウェブサイト（アドレスバーに鍵アイコン）を使用。

#### 三、Bluetooth：短距離無線通信の万能選手

Bluetoothはスマートフォンで最も使用頻度の高い無線技術の一つかもしれない——ワイヤレスイヤホン、スマートウォッチ、カーシステム、キーボードマウス、すべてそれで接続する。

##### 技術原理：

Bluetoothは2.4GHz ISM帯で動作し、周波数ホッピング拡散（FHSS）技術でデータを79チャネルに分散して高速に切り替えながら伝送するため、干渉を効果的に回避できます。Bluetoothの通信距離は3つのクラスに分かれます：Class 1は約100メートル、Class 2は約10メートル（スマートフォンでよく使われる）、Class 3は約1メートルです。

##### バージョン進化：

- <strong>Bluetooth 4.0</strong>：低消費電力Bluetooth（BLE）を導入し、バンド、心拍センサーなどの小電池デバイスも無線接続可能になり、バッテリー持続が日単位から月単位に。
- <strong>Bluetooth 4.2</strong>：転送速度とプライバシー保護を向上、IPv6直接接続をサポート。
- <strong>Bluetooth 5.0</strong>：転送速度2倍（2Mbps）、転送距離4倍（理論300メートル）、ブロードキャスト能力8倍。デュアルオーディオ（同時に2つのイヤホン接続）をサポート。
- <strong>Bluetooth 5.1</strong>：方向測位機能（AoA/AoD）を導入し、測位精度はセンチメートル級に到達。
- <strong>Bluetooth 5.2</strong>：LE Audio新規格、LC3コーデックサポート（音質向上、消費電力低下）、マルチストリームオーディオ、ブロードキャストオーディオ。
- <strong>Bluetooth 5.3/5.4</strong>：消費電力と接続安定性をさらに最適化、周期的ブロードキャストを強化。

<strong>LE Audio普及状況</strong>：2025-2026年、LE Audioは急速な普及段階に入っています。主要ブランドの新型完全ワイヤレスイヤホン（Huawei FreeBuds Pro 5、Xiaomi Buds 6 Pro、Samsung Galaxy Buds3 Proなど）はLE AudioとLC3コーデックに対応しており、より低いレイテンシとより良い音質を提供します。新しいイヤホンを購入する際は、LE Audio対応製品を優先することをお勧めします。

##### 活用シーン：

- <strong>オーディオ伝送</strong>：ワイヤレスイヤホン、カーオーディオ。Bluetooth 5.2のLE Audioで音質と遅延が質的に飛躍。
- <strong>データ転送</strong>：近距離でのファイル、写真転送。速度はWi-Fi Directに劣るが、シンプルさで勝る。
- <strong>デバイスペアリング</strong>：スマートウォッチ、バンド、キーボードとマウス、ゲームコントローラ。
- <strong>位置サービス</strong>：Bluetoothビーコン（Beacon）は屋内ナビゲーション、物品追跡（Apple AirTagなど）に使用。
- <strong>スマートホーム</strong>：Bluetooth Meshネットワークで電球やスマートロックなどを制御します。

#### 四、赤外線リモコン：スマートフォンが万能リモコンに変身

赤外線リモコンは最も古い無線制御技術の一つだが、スマートフォンでも依然として実用的だ。一部のAndroidスマートフォン（Xiaomi、Huaweiの一部機種など）には赤外線送信機が内蔵され、テレビ、エアコン、セットトップボックスなどの家電をリモコン操作できる。

##### 動作原理：

赤外線リモコンは、赤外線発光ダイオードから特定の周波数（通常38kHz）の赤外光パルス信号を放ち、家電の赤外線受信器がこのパルスを復号して対応する操作を実行します。ブランドごとに異なるエンコードプロトコルが使われており、一般的なのはNEC、RC5、RC6、SONYなどです。スマートフォンの赤外線アプリには各ブランドのコードライブラリが内蔵されており、ブランドと型番を選ぶだけでマッチします。

##### 制限事項：

- <strong>方向性</strong>：赤外線は直線伝播で、デバイスに向けて発信する必要があり、壁越しは不可。
- <strong>距離が短い</strong>：有効距離は一般に5-8メートル。
- <strong>Apple非サポート</strong>：iPhoneには赤外線送信機がなく、この機能は使用不可。

#### 五、NFC：タッチする魔法

NFC（Near Field Communication、近距離無線通信）は極短距離（10センチ以内）の高周波無線通信技術で、動作周波数13.56MHz、転送速度最高424Kbps。

##### 通信原理とモード：

NFCはRFID技術から派生し、3つの動作モードをサポート：

- <strong>読み取り/書き込みモード</strong>：スマートフォンがNFCタグの情報を読み取る。NFCステッカーの読み取りでアクションをトリガーするなど。
- <strong>ピアツーピアモード</strong>：2台のNFCデバイスが相互にデータ転送。Android Beam（廃止済み）など。
- <strong>カードエミュレーションモード</strong>：スマートフォンがスマートカードをエミュレート。これが最もよく使われるモード——交通カード、ドアカード、銀行カードはすべてこのモード。

##### セキュリティメカニズム：

- <strong>超短距離</strong>：10センチ以内の通信距離自体が物理的セキュリティ保障で、遠隔からの盗聴はほぼ不可能。
- <strong>セキュリティチップ</strong>：スマートフォンに独立したセキュリティチップ（SE）を内蔵するかHCE（ホストカードエミュレーション）を使用し、決済鍵はセキュアエリアに保存され、スマートフォンがroot化されても抽出不可。
- <strong>指紋/顔認証</strong>：決済時に生体認証確認が必要で、スマートフォン紛失時も不正使用不可。
- <strong>トークン化</strong>：Apple Pay、Huawei Payなどは実際のカード番号を転送せず、一次性トークンを使用し、傍受されても再利用不可。

##### 典型的な応用：

- <strong>交通カード/ドアカード</strong>：実体カードの情報をスマートフォンに書き込み、スマートフォンをかざすだけ。
- <strong>モバイル決済</strong>：Apple Pay、Huawei Payなどで、銀行カードをスマートフォンにバインドし、タッチで決済。
- <strong>デバイスペアリング</strong>：NFCタッチでBluetoothイヤホン、スピーカーと迅速ペアリング。
- <strong>本人認証</strong>：NFC身分証読み取り、電子運転免許認証。

#### 六、テザリング：スマートフォンをWi-Fiルーターに

自分のデータ通信量が余っている時、テザリングでタブレットやパソコンに提供できる。

- <strong>有効化方法</strong>：設定 &gt; テザリング/ネットワーク共有で有効化。
- <strong>注意事項</strong>：電池とデータ通信量を大きく消費するので、複雑なパスワードを設定し、接続デバイス数を制限することを忘れないでください。
- <strong>USB共有</strong>：データケーブルでパソコンと接続。ワイヤレステザリングより安定で速い。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>やってみよう：テザリングの設定と管理

{class="list-decimal pl-6 mt-1 space-y-1"}
1. [設定]を開き、「テザリング」または「ネットワーク共有」を見つけて有効化し、名称とパスワードを設定。
2. 別のデバイス（パソコンなど）でこのWi-Fiを検索して接続。
3. スマートフォン側で、接続済みデバイスを管理したり、知らないデバイスをキックできるか確認。
4. 第四章：アプリのインストールと管理——スマートフォンの「スキルパック」
:::
