---
id: di-san-shi-zhang
num: 30
part: shi-zhan-pian
nav: 第三十章：画面ミラーリング、プレゼン、車載連携
toc: default
kind: chapter
---

### 第三十章：スクリーンミラーリング、プレゼンとカーナビ連携

{class="chapter-intro mb-4"}
スマホ画面は大きくても7インチだが、テレビは55インチ、プロジェクターは100インチだ。スマホ画面を大画面に"投げる"と、体験は全く次元が異なる。この章ではスクリーンキャスト、プレゼン、カースル連携の三つの高頻度シーンを明確にし、スマホの能力をより大きな画面に拡張する方法を説明する。

#### 一、ワイヤレスキャストの三大陣営——混同しないように

ワイヤレスキャストはどれも"スマホ画面をテレビに"のように見えるが、基盤の技術は三種類あり、互いに互換性がない：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                            <thead>
                                <tr class="bg-light dark:bg-gray-700">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">技術</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">使用者</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">特徴</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">AirPlay</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">iPhone/iPad/Mac</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Appleエコシステム、体験最も滑らか。Apple TVまたはAirPlay対応テレビが必要</td></tr>
                                <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Miracast</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Androidスマホ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi Direct直接接続、ルーター不要。Androidスマホの"ワイヤレスキャスト"はデフォルトでこれを使用</td></tr>
                                <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">DLNA</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全プラットフォーム</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">メディアファイル（動画/音楽/画像）のみプッシュ、画面ミラーリングなし。テレビに動画を送って再生するのに適している</td></tr>
                            </tbody>
                        </table>
```
:::

##### 各プラットフォームの操作方法：

- <strong>iPhone</strong>：コントロールセンター &gt; 画面ミラーリング &gt; テレビ/Apple TVを選択。テレビがAirPlayに対応していない場合、Apple TVボックスまたはAirPlay対応のテレビスティックを購入できる。
- <strong>Android</strong>：通知パネルをプルダウン &gt; "ワイヤレスキャスト"/"スマートキャスト"/"マルチスクリーンインタラクション"ボタンを見つける &gt; テレビを選択。スマホとテレビが同じWi-Fiに接続している必要がある。
- <strong>汎用ソリューション</strong>：テレビが古すぎてワイヤレスキャストに対応しない場合、ChromecastやXiaomiボックス/Huaweiボックスを買ってテレビのHDMI端子に挿せばキャスト受信ができる。

#### 二、有線キャスト——より安定、ゼロ遅延

ワイヤレスキャストは便利だが遅延があり、ゲームやプレゼンでは体験が良くない。有線キャストはこの問題を解決できる：

- <strong>iPhone</strong>：Lightning/USB-C to HDMI変換ケーブルが必要（約100-200元）。接続するとスマホ画面がテレビ/プロジェクターのHDMI端子に直接出力される。
- <strong>Android</strong>：一部のスマホはUSB-C to HDMI直接接続に対応（スマホがDP Alt Modeをサポートする必要あり、大部分のフラッグシップが対応）。USB-C to HDMIケーブルを一本買えばよい。
- <strong>会議室シーン</strong>：頻繁にスマホでプレゼンする場合は、バッグにHDMI変換ケーブルを常備することを推奨。会議室のテレビ/プロジェクターはほぼHDMI端子があり、挿せば使える。ワイヤレスキャストをあれこれするよりはるかに頼りになる。

#### 三、スマホがパソコンに——デスクトップモード

一部のAndroidスマホは"デスクトップモード"に対応——モニターに接続すると、パソコンのデスクトップに似たUIを出力し、マウスとキーボードで操作できる：

- <strong>Samsung DeX</strong>：Samsungフラッグシップの看板機能。モニター接続後にデスクトップUIが起動し、マルチウィンドウ操作が可能。本当のパソコンに最も近い体験。Bluetoothキーボード/マウスと組み合わせれば、出張時にノートPCを持たずに済む。
- <strong>Huaweiデスクトップモード</strong>：Huawei Mateシリーズ/Puraシリーズがモニター接続後に類似機能あり。マルチウィンドウ、ファイル管理、オフィスAppに対応。
- <strong>Motorola Ready For</strong>：Motoフラッグシップも対応、機能はDeXに類似。
- <strong>：ハイエンドプロフェッショナル制作。iPhone 15 ProシリーズはApple ProRes動画撮影に対応（最大4K 60fps）しますが、ProRes RAW形式は現状外部録画デバイスとの組み合わせが必要で、スマホ単体での直接撮影は未対応。</strong>：ライトなオフィス作業（メール返信、文書編集）、PPTプレゼン、大画面で動画視聴。ヘビーなExcel操作や専門的なデザインには不適。

#### 四、カースル連携——運転中のスマホの正しい使い方

運転中のスマホ操作は違法だが、ナビ、音楽、電話は必須だ。カースル連携システムで車載画面上でスマホのコア機能を使い、スマホは置いて触らないでおける：

- <strong>Apple CarPlay</strong>：iPhoneユーザーの第一選択。USBまたはワイヤレスでカースルに接続、車載画面にiPhoneのシンプルUIが表示される——ナビ（Amap/Baidu Map）、音楽、電話、メッセージ、ポッドキャスト。Siri音声操作で完全ハンズフリー。
- <strong>Android Auto</strong>：Androidユーザー向けの対応策。機能はCarPlayに類似、Google Maps、Spotifyなどに対応。国内はGoogleサービス制限により一部機能使用不可。
- <strong>Huawei HiCar</strong>：Huawei自社開発方案、国内車種のサポート率が高い。ナビ・音楽のほか、Huaweiビデオ通話、駐車映像統合などの独自機能も使える。
- <strong>Baidu CarLife</strong>：クロスプラットフォーム方案、iOSとAndroidの両方で使用可能。機能は少ないが互換性が広く、多くの旧型車種はCarLifeのみ対応。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>セキュリティに関する注意

{class="mt-1"}
どのカースル連携方案でも、運転中はできるだけ音声操作を使うべきだ。ナビは事前に目的地を設定し、音楽は事前にプレイリストを選んでおき、走行中に車載画面を操作しない。
:::

#### 五、会議室キャスト実戦——もうバタバタしない

会議はキャストの最も高頻度なシーンであり、最も問題が起きやすいシーンでもある。以下は実戦の経験則：

- <strong>事前到着してテスト</strong>：会議開始直前にキャスト接続を試すのは絶対に避ける。10分前に到着し、接続方法をテストする。Wi-Fiキャストの失敗確率は想像より高い。
- <strong>有線方案をPlan Bとして準備</strong>：バッグにHDMI変換ケーブルを入れておく。ワイヤレスキャストが繋がらない時に有線が命綱になる。
- <strong>通知プレビューをオフにする</strong>：キャスト中、WeChatメッセージが会議室の大画面に表示される。キャスト前に設定で"ロック画面通知のプレビュー"をオフにするか、"プレゼンモード"をオンにする（一部スマホ対応、キャスト時に通知を自動非表示）。
- <strong>"プレゼン文書"を使う而非"スマホ操作"</strong>：PPTを展示する場合、PPTをスマホに保存してWPSで全画面再生する方が、スマホ画面全体をキャストするよりよい。よりプロフェッショナルでスムーズ。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>実践：スマホからテレビへのキャストを一度完了する

{class="list-decimal pl-6 mt-1 space-y-1"}
1. テレビで「画面ミラーリング」または「AirPlay」機能を見つけてオン。
2. スマホで写真または動画を一枚開く。
3. ワイヤレスキャストを試す（iPhoneは画面ミラーリング、Androidはワイヤレスキャストボタン）。
4. 失敗した場合、テレビが対応プロトコルをサポートしているか確認、またはDLNAプッシュを試す（アルバム/動画Appで"キャスト"ボタンをタップ）。
5. キャスト成功後、スマホで他の操作をして、大画面が同期表示されるか確認する。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1" aria-hidden="true"></i>本章のまとめ

{class="list-disc pl-5 text-sm space-y-0.5"}
- ワイヤレスキャストの三大陣営：AirPlay（Apple）、Miracast（Android）、DLNA（クロスプラットフォーム・メディアプッシュ）
- 有線キャストはより安定・ゼロ遅延、会議室シーンにHDMI変換ケーブルが必須
- Samsung DeX/HuaweiデスクトップモードでスマホがライトオフィスPCに変身
- カースル連携：CarPlay/Android Auto/HiCar/CarLifeの四大方案
- 会議室キャストの鉄則：事前テスト、Plan B準備、通知プレビューオフ
:::
