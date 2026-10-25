---
id: di-er-shi-zhang-jinjie
num: 20
part: jin-jie-pian
nav: 第二十章：開発者モードと高度な権限
toc: default
kind: supplement
---

### 第二十章：開発者モードと高度な権限

{class="chapter-intro mb-4"}
一、開発者モード：隠し設定のアンロック

#### 一、開発者モード：隠し設定のアンロック

有効化方法：

##### 有効にする方法：

- <strong>Android</strong>：設定 → 端末情報 → 「ビルド番号」を7回連続タップし、「開発者モードになりました」と表示されるまで操作。
- <strong>HarmonyOS</strong>iOS
- <strong>iOS</strong>よく使う機能：

##### よく使う機能一覧：

- <strong>：パソコンに接続して高度な操作、フラッシュやデータ復元など。</strong>: PCに接続して高度な操作（フラッシュ、データ復元、ADB コマンドなど）を行うために必ず有効化するスイッチ。本章の「ADB 実用コマンド」小節を参照。
- <strong>：画面にタッチポイントを表示、チュートリアル録画に適する。</strong>: 画面にタッチポイントを表示（小さな丸が指に追従）。操作チュートリアルやデモの録画に適しています。

##### パフォーマンスと快適さ関連：

- <strong>アニメーション速度調整（ウィンドウアニメーションスケール / トランジションアニメーションスケール / アニメーション時間スケール）</strong>: これら3つのオプションは App を開く時やページ切り替え時のアニメーション時間を制御します。デフォルトは1x。0.5xにするとスマホが「見た目上」速くなります（実際の処理速度は変わらず、アニメーションが速くなるだけ）。完全にオフにするとアニメーションなしで直接ジャンプします。多くのギークは0.5xに設定し、遷移感を残しつつ速さを演出。完全オフは操作がぎこちなくなり、本来のカクつきを隠して「とても滑らか」と誤認させる原因にもなります。
- <strong>GPU レンダリングの強制（Force GPU Rendering）</strong>: すべての2D描画を CPU ではなく GPU に強制的に処理させます。旧機種や最適化の不十分な App でスクロールの滑らかさが向上することがありますが、GPU 負荷と消費電力も増加します。現代のスマホはデフォルトで GPU レンダリングを多用しているため、このスイッチは中高級機種への影響は限定的で、歴史的な名残のオプションです。一般ユーザーはデフォルトのままで問題ありません。
- <strong>GPU レンダリングプロファイリングの表示（Profile GPU Rendering）</strong>: 画面上に棒グラフで毎フレームのレンダリング所要時間をリアルタイム表示。緑色の横線は16.6ms（60fps のフレーム時間閾値）を表します。棒が緑線を超えるとフレームドロップが発生しています。これは開発者が App のカクつきを調査する強力なツールで、一般ユーザーもどの App の最適化が不十分かを比較できます——例えば、ある App のスクロール時に棒が頻繁に赤線を超えるなら、ほぼその App が原因です。

##### バックグラウンドとバッテリー持ち関連：

- <strong>：バックグラウンドで動作するアプリ数を制限し、省電力。</strong>: 「標準制限」「最大1プロセス」「最大2プロセス」などが設定できます。一見バックグラウンドプロセスを制限すると省電力になりそうですが、実際には Android のバックグラウンド管理は既に十分機能しており、強制制限は App の頻繁な再読み込みを引き起こし（コールドスタートはかえって消費電力が多く、体験も低下します）。このオプションはデバッグ向けで、一般ユーザーが長期有効にすることは推奨されません。「標準制限」のままで問題ありません。
- <strong>アクティビティを保持しない</strong>: 画面から離れるたびに即座に破棄します。非常に非推奨。App が頻繁にホワイトスクリーンになり、再読み込みが発生します。App の復元ロジックのテスト用のみ。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>注意事項

{class="mt-1"}
二、BLロック（Bootloaderロック）：フラッシュの第一の門
:::

#### 二、OEM ロック解除：開発者オプション内の「フラッシュスイッチ」

開発者オプションの中に目立たないが重要なスイッチがあります——「OEM ロック解除」（一部ブランドでは「OEM アンロック許可」や「デバイスアンロック」と呼ばれます）。このスイッチ自体は BL ロックを解除しませんが、「事前許可」です：これをオンにして初めて、メーカーが fastboot コマンドやブランドツールで BL の解除を許可します。

- <strong>スイッチの役割</strong>: メーカーに「私は保証を放棄し、自己責任で BL の解除を許可してほしい」と宣言するようなものです。このスイッチがオフの場合、BL 解除コマンドはすべて直接拒否されます。
- <strong>BL ロックとの関係</strong>: OEM ロック解除は「資格申請」、BL 解除が「実際の操作」です。前者はスマホの設定でタップするだけ、後者はメーカーの公式サイトで解除コードを申請し、PC で fastboot コマンド（例： <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing unlock</code>）を実行する必要があり、両方が不可欠です。
- <strong>初期化するとリセットされるか</strong>: はい。「OEM ロック解除」スイッチは初期化後にオフに戻りますが、BL ロックは一度解除すると物理レベルの状態となり、初期化では再ロックされません——手動で <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing lock</code> を実行して再ロックする必要があります。
- <strong>いつオンにすべきか</strong>: フラッシュや Root を確実に行う場合を除き、オフのままにしてください。「USB デバッグ」とは独立したスイッチで、フラッシュ時は通常両方をオンにします。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>豆知識：なぜメーカーはこのスイッチを設けるのか

{class="mt-1"}
初期の Android にはこのスイッチがなく、マルウェアは権限を取得すれば密かにシステムをフラッシュできました。Google は後にすべての Android メーカーに対し、開発者オプションに「OEM ロック解除」スイッチを追加し、「ユーザーの知情同意」の確認とすることを要求しました。これが、BL ロックを解除していても OEM ロック解除スイッチがオフなら再フラッシュが失敗する理由です。
:::

#### 三、BL ロック（Bootloader ロック）：フラッシュの第一の門

BLロックの役割：

##### セキュリティ保護

- <strong>：マルウェアのシステムフラッシュを防止。</strong>盗難防止
- <strong>：スマホがフラッシュされても、元のアカウントパスワードがなければ使用不可。</strong>保証制限
- <strong>：BLアンロックは通常、公式保証の喪失を意味します。</strong>各ブランドBLロックポリシー：

##### 各ブランドのBLロック方針：

- <strong>Xiaomi</strong>：ロック解除可能。アカウント連携と待機期間（7〜30日）が必要。
- <strong>Huawei</strong>OnePlus
- <strong>：アンロック可能、比較的緩和。</strong>OPPO/vivo
- <strong>：一部機種はアンロック可能、申請が必要。</strong>Samsung
- <strong>Samsung</strong>Apple
- <strong>Apple</strong>三、Root権限：Androidの「スーパーアドミン」

#### 四、ADB 実用コマンド：PC からスマホを操作

ADB の正式名称は Android Debug Bridge で、Google が公式提供するコマンドラインツールです。PC から USB または Wi-Fi 経由で Android スマホと通信できます。Root 不要で、スマホの「USB デバッグ」がオンなら使えます。「PC からスマホに指示を出すリモコン」と理解してください——フラッシュ、App インストール、ファイル転送、ログ確認にすべて必要です。

##### USB で接続する方法：

1. スマホ側：開発者オプション → 「USB デバッグ」をオン。
2. PC 側：Google 公式から Platform Tools（ <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb</code> 3. タスク（Task）：AIに何をするか明確に伝える <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot</code> の2つの実行ファイルを含む）をダウンロードし、任意のディレクトリに解凍。
3. データケーブルでスマホと PC を接続。スマホに「USB デバッグを許可しますか？」のポップアップが表示されるので、「常に許可」にチェックを入れて確定。
4. PC のコマンドライン（Windows の PowerShell や cmd）で <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code>を実行し、 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">List of devices attached / xxxxxxxx device</code>のような出力があれば接続成功です。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>ドライバーと認証ポップアップを見逃さないで

{class="mt-1"}
Windows ユーザーで <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code> が「unauthorized」と表示されるかデバイスがリストされない場合、多くはドライバーが未インストールかスマホで「許可」を押し忘れたのが原因です。Samsung/Xiaomi などのブランドは各社の「USB ドライバー」や「スマホアシスタント」をインストールしてドライバーを補完できます。Mac と Linux は通常ドライバー不要です。スマホのポップアップを誤って消してしまった場合は、ケーブルを挿し直すと再表示されます。
:::

##### よく使う ADB コマンド：

- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb install app.apk</code>: PC 上の APK をスマホにインストール（<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-r</code> は上書きインストールでデータ保持；<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code> は SD カードにインストール）。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb uninstall com.xxx.xxx</code>: パッケージ名で App をアンインストール。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb push PCパス /sdcard/目標パス</code>: PC のファイルをスマホにプッシュ。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb pull /sdcard/ファイル PCパス</code>: スマホのファイルを PC に取り込む（WeChat で自分に送ってダウンロードするよりはるかに速い）。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell</code>: スマホの Linux Shell に入り、直接 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls</code>、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm</code>、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">am</code> などのコマンドを実行できます。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot bootloader</code>: スマホを Fastboot モードで再起動（フラッシュの入口）。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot recovery</code>: Recovery モードで再起動。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages</code>: スマホにインストールされたすべての App のパッケージ名をリスト（パッケージ名検索に必須）。 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code> を付けるとシステム App のみ、 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-3</code> を付けるとサードパーティ App のみ。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 パッケージ名</code>: 現在のユーザーのプリインストール App をアンインストール。Root 不要。下記の実戦を参照。

##### Root 不要でプリインストール App をアンインストールする実戦：

これは ADB の最も実用的な機能の一つです： <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code> コマンドで「現在のユーザー」のプリインストール App をアンインストールでき、Root 不要でシステムパーティションにも影響しません。アンインストールされた App はシステムから「消滅」しますが、実際にはシステムパーティションに残っており、初期化すれば戻ります。

1. まず <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages -s</code> で全システム App をリストし、アンインストールしたいパッケージ名を見つけます。例えば Xiaomi ブラウザは <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.browser</code>、Huawei アプリストアは <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.vmall.client</code>。
2. パッケージ名がどの App か不明な場合は、PC で <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages | findstr キーワード</code> で検索するか、サードパーティ App「Package Viewer」をインストールしてスマホ上で各 App のパッケージ名を直接確認できます。
3. アンインストールを実行：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 パッケージ名</code>、例えば <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 com.android.browser</code>。戻り値が <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Success</code> なら成功です。
4. 復元したい場合は？2つの方法：① 初期化（最も徹底だが面倒）；② 再インストール：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell cmd package install-existing パッケージ名</code>。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>システムコアパッケージをむやみに削除しないでください

{class="mt-1"}
「pm uninstall --user 0」は Root 不要の安全な方法ですが、重要システム App（ <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.systemui</code> ステータスバー、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.phone</code> 電話、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.settings</code> 設定など）をむやみに削除すると、システムクラッシュ、ブラックスクリーン、起動不能などの深刻な問題を引き起こします。削除前に「このパッケージ名は削除できるか」を検索し、少なくとも間違えないようにしてください。一度に1-2個だけ削除し、問題ないことを確認してから続行することを推奨します。
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>豆知識：--user 0 とは何か

{class="mt-1"}
Android 4.2 以降はマルチユーザーをサポートし、各ユーザーに独立した ID があります（機主は0、追加ユーザーは10から開始）。<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">--user 0</code> は「現在の機主のみアンインストール」を意味し、システムパーティション内の APK ファイルは依然存在し、機主に表示されなくなるだけです。これが Root 不要の理由——システムファイルは変更せず、「ユーザー設定」を変えただけです。Root 後のアンインストールとの最大の違いもここにあります：Root アンインストールはシステムから本当に削除し、全ユーザーから消えますが、ADB アンインストールは「現在のユーザーに非表示」にするだけです。
:::

#### 五、Root 権限：Android の「スーパー管理者」

Root 権限は Linux のスーパーユーザーに相当し（/ ディレクトリに対して完全な制御権を持ち、任意のファイルの読み書きが可能）、Android システムの最高権限です。Windows の Administrator とは本質的な違いがあります：Windows はセキュリティ上の理由から管理者に多くの制限を設けており（真の最高権限は TrustedInstaller）、Administrator であっても Linux root のように直接 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">sudo rm -rf /*</code>を実行できません。Root 権限を取得すると、システムファイルの変更、プリインストール App のアンインストール、Root 必要な高度な App の使用が可能になります。

##### アンインストールできないプリインストールアプリを削除。

- 高度な機能Appの使用（Titanium Backup、Greenifyなど）。
- システムインターフェースと機能の修正。
- サードパーティRecoveryとカスタムROMのインストール。
- Rootのリスク：

##### 保証喪失

- <strong>ROM焼きにはリスクがあり、操作には慎重さが必要です。次のような問題が発生する可能性があります：</strong>セキュリティリスク
- <strong>：マルウェアAppがRoot権限を取得し、深刻な結果を招く可能性。</strong>システム不安定
- <strong>：誤操作でシステムクラッシュの可能性。</strong>銀行App使用不可
- <strong>：多くの銀行・決済AppはRootを検出すると実行を拒否。</strong>OTA更新失敗
- <strong>：公式システム更新を正常に受信できない可能性。</strong>深刻な警告

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>Root操作にはリスクがあり、スマホがレンガ化（起動不可）する可能性があります。初心者の場合、まず関連知識を十分に学び、完全なバックアップがあることを確認してください。操作前にチュートリアルを注意深く読み、あなたの機種とシステムバージョンを確認してください。

{class="mt-1"}
四、一般ユーザーへのアドバイス
:::

#### 六、SafetyNet と Play Integrity 認証：なぜ Root 後に銀行 App が使えないのか

多くの Root ユーザーがこんな絶望的瞬間を経験しています：Root 後、意気揚々とモジュールをインストールしたのに、銀行 App を開くと——「お使いのデバイスは安全でないため使用できません」。Google Pay も使えず、Netflix すら高画質再生を拒否されます。その背後にあるのは Google の2つのデバイス完全性認証メカニズム：旧式の SafetyNet と新型の Play Integrity API です。

##### SafetyNet / Play Integrity とは：

- <strong>SafetyNet Attestation（旧版、2017年〜）</strong>: Google が早期に発表したデバイス完全性チェック API。App はこれを通じて Google サーバーに「このデバイスは CTS 互換性テストに合格しているか、未変更の公式状態か」を問い合わせます。戻り値は Basic Attestation（基本検証）と Strong Attestation（強力検証、ハードウェアキー依存）に分かれます。Google は SafetyNet を2024年以降順次廃止すると発表しています。
- <strong>Play Integrity API（新版、2022年〜）</strong>: Google が発表した代替方案で、SafetyNet より厳格かつ包括的です。デバイス完全性に加え、「アプリ完全性」（App が改ざんされていないか）と「アカウント/認可完全性」（ユーザーアカウントが Google に信頼されているか）も含みます。新規 App は Play Integrity に移行すべきです。
- <strong>誰が使うか</strong>: 銀行、金融、決済系 App（Google Pay、各銀行のネットバンキング、支付宝/WeChat Pay の一部シーン）、ストリーミング（Netflix の高画質著作権保護）、一部ゲームのアンチチート（Tencent/NetEase の一部ゲーム）、企業オフィス App（MDM デバイスコンプライアンスチェック）。

##### Play Integrity の3段階認証結果：

- <strong>MEETS_DEVICE_INTEGRITY（デバイス完全性合格）</strong>: デバイスは正規 Android システムを実行し、Bootloader は未解除、Root なし、CTS 互換性テスト合格。銀行・決済系 App を正常に使用できます。
- <strong>MEETS_BASIC_INTEGRITY（基本完全性合格）</strong>: デバイスは基本的に信頼できるが、軽微な異常の可能性あり。一部 App はダウングレード使用（Netflix は再生可能だが画質制限など）、厳格な銀行 App は直接拒否します。
- <strong>MEETS_STRONG_INTEGRITY（強力完全性合格）</strong>: 最高レベル。ハードウェアキーの裏付けが必要（Google Pixel シリーズの Titan M チップなど）。ほとんどのサードパーティブランドは Root なしでもこのレベルに達しません。
- <strong>ラベルなし（NO_INTEGRITY）</strong>: デバイスが Root 済み、BL 解除済み、サードパーティ ROM フラッシュ済み、またはエミュレータと認識され、ほとんどの決済/銀行 App が直接実行を拒否します。

##### なぜ Root 後にこれらの App が使えなくなるのか：

App は Play Integrity API で Google サーバーに認証リクエストを送信し、Google はデバイスの複数指標をチェックします——Bootloader ロック状態、システムパーティションの変更有無、su バイナリの存在、SELinux が Permissive モードかなど。いずれかの異常が認証レベルの低下または空を引き起こし、銀行 App は「デバイスが安全でない」と判断してサービスを拒否します。

##### 現代の隠蔽方案：Magisk Hide / Shamiko / Zygisk：

Root の利便性を享受しながら銀行 App も使えるよう、コミュニティは一連の「Root 状態隠蔽」方案を開発しました。核心的な考え方はすべて同じです：検出プログラムが見るのは変更されたシステムではなく、「正常に見える」デバイスにする。

- <strong>：古参のRoot方案、現在は更新停止。</strong>: 現在最も主流な Systemless Root 方案——システムパーティションを変更せず、マウント方式で Root を実現します。この設計の利点は OTA 更新失敗の確率が低く、アンインストールが比較的クリーンで、後続のすべての隠蔽方案の基盤となることです。ただし Magisk の使用には BL ロック解除が依然として必要です。
- <strong>Magisk Hide（開発終了）</strong>: Magisk に初期内蔵されていた隠蔽モジュールで、指定 App に対して Root を隠せました。しかし2021年以降 Magisk 公式から削除されました。理由は Google が検出手法を継続強化し、双方が「いたちごっこ」に陥ったためです。
- <strong>Zygisk</strong>: Magisk 24.0+ で導入された新メカニズム。Riru に似て、Zygote プロセスへの注入でモジュール読み込みを実現し、システム直接変更より隠蔽性が高いです。Zygisk の有効化は現代隠蔽方案使用の前提です。
- <strong>Shamiko</strong>: 現在最も主流な隠蔽モジュール。Zygisk と連携し、指定 App（「リバースホワイトリスト」モード）に対して Root を隠蔽、Magisk 自身を隠蔽、Bootloader ロック状態を偽装します。Shamiko は LSPosed リポジトリまたは GitHub から配布されます。
- <strong>Play Integrity Fix（osm0sis）</strong>: Google Play Integrity 検出に特化した Magisk モジュール。デバイスのフィンガープリントを変更し、Google に未 Root の公式機種と認識させます。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>いたちごっこは永遠に終わらない

{class="mt-1"}
Google は定期的に検出ルールを更新し、App メーカーも Play Integrity 検証をアップグレードします。今日使える隠蔽方案が明日認識されるかもしれません。もし銀行/決済 App に完全に依存している（日常送金、QRコード決済など）なら、最も確実な選択は依然として：Root しない、BL ロックを解除しない。隠蔽方案は「メイン機 Root なし + サブ機で Root 遊び」のプレイヤー構成により適しています。
:::

#### 七、一般ユーザーへのアドバイス

- <strong>：有効化して、アニメーション加速などの機能を体験しても良いが、他の設定は変更しない。</strong>: オンにして、アニメーション加速、GPU レンダリングプロファイリングなどの機能を体験できますが、理解できない他のオプションはむやみに変更しないでください。
- <strong>OEM ロック解除と BL ロック</strong>: フラッシュや Root の予定がなければ、両方のスイッチをデフォルト（オフ）のままが最も安全です。
- <strong>ADB</strong>: Root 不要の強力ツールで、一般でも使えます——例えば <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code> でプリインストール App をアンインストール。ただし削除前にパッケージ名が削除可能か必ず確認してください。
- <strong>ワイヤレスシステムアップデート</strong>: 一般ユーザーの Root は推奨しません。リスクが利益を上回ります。どうしても必要な機能がある場合は、Root 不要の代替方案を先に調べましょう（ADB でプリインストール削除、Shizuku で一部 Root 機能を代替など）。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>設定 &gt; デバイス情報に入る。

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 「ビルド番号」を連続7回タップ、開発者モードが有効化されたと表示されるまで。
2. 設定に戻り、「開発者オプション」を見つける（通常は設定下部または「システム」内）。
3. 「ウィンドウアニメーションスケール」、「トランジションアニメーションスケール」、「アニメーション時間スケール」を見つけ、すべて0.5xまたはオフに設定。
4. スマホが速くなったか感じてみる。
5. 第二十章付録：Termux——Androidデバイス上のポータブルLinuxターミナル環境
:::
