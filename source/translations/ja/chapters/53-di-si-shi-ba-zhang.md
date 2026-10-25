---
id: di-si-shi-ba-zhang
num: 48
part: an-zhuo-kai-fa-pian
nav: 第四十八章：Androidを知る——OSから開発エコシステムまで
toc: default
kind: chapter
---

### 第四十八章：Androidを知る——OSから開発エコシステムまで

{class="chapter-intro mb-4"}
この決断、おめでとうございます——「スマホで遊ぶ人」から「スマホアプリを作る人」への一歩です。手を動かす前に、まず地図を広げておきましょう。Androidはどこから来たのか？なぜ世界中の開発者がAndroid向けにアプリを作るのか？あなたがキーボードを叩いてから、アプリがユーザーのスマホに届くまで、間で何が起きているのか？

#### 1. Androidの生い立ち：「小さなロボット」から「世界最大のOS」へ

Androidの物語は2003年に始まります。Andy RubinというエンジニアがAndroid社を興し、その目標は実に素朴なものでした。「カメラをもっと得意にする」スマートOSを作る、というものです。その後、2005年にGoogleが同社を買収し、2007年には何十社ものメーカーとともにOpen Handset Alliance（OHA）を設立。そして2008年9月、最初のAndroidスマホHTC Dream（G1）が正式に発売されました。

その後の話はご存じのとおりです。2026年には、Androidは世界でいちばんシェアの大きいモバイルOSとなり、稼働するデバイスは数十億台に上ります。あなたのスマホ、テレビのセットトップボックス、カーナビの大画面、スマートウォッチも、おそらくAndroidが動いています。これはどういうことでしょう？あなたが書く1行1行のコードに、世界で最も多くの人に使われるチャンスがある、ということです。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ワンポイント：Androidのオープンソースの血

{class="mt-1"}
Androidの中核コード（AOSP、Android Open Source Project）はオープンソースです。どのメーカーも持っていって改造・カスタマイズできます。だからXiaomiにはMIUI（今のHyperOS）、HuaweiにはHarmonyOSの互換レイヤー、SamsungにはOne UIがあるのです。これは開発者にとって良いことです。あなたが学ぶのは「Android開発」であって「あるブランドの開発」ではない。1つの技術を磨けば、どの端末でも通用します。
:::

バージョン番号の歩みもおもしろいものがあります。1.5のCupcake（カップケーキ）から始まり、長らくメジャーバージョンにはデザートの名前が付いてきました——ドーナツ、エクレア、フローズンヨーグルト、ジンジャーブレッド……2019年のAndroid 10になって、ようやく数字だけの名前に変わりました。2026年8月時点での最新正式版はAndroid 17です。開発で本当に気にすべき「最低サポートバージョン」は、主流アプリならAndroid 8（API 26）〜Android 10（API 29）の間に設定するのが一般的です。数年前の端末までカバーしてこそ、ユーザーの数が大きくなるのです。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">バージョン</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">コードネーム／年</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">開発者にとって大事なこと</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 8 (API 26)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Oreo · 2017</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">通知チャネル、バックグラウンド制限——多くの旧型端末の下限ライン</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 10 (API 29)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2019</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">スコープストレージの登場。ファイルアクセスのルールが大きく変わる</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 12 (API 31)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2021</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Material Youのダイナミックカラー。UIの見た目が大きく進化</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 13 (API 33)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2022</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">実行時の通知権限。「通知を許可しますか？」のポップアップが登場</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 14-15 (API 34-35)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2023-2024</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">予測型「戻る」、16KBページ、プライバシーがさらに厳格化</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 16-17 (API 36-37)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2025-2026</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">より速いマイナーアップデートのペース、AI機能の統合（Gemini拡張など）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Androidバージョン略史（2026年8月時点、開発での注目ポイント）

#### 2. どの言語で書く？：Javaか、Kotlinか

Android開発の歴史には、2つの主流言語があります。Javaは「建国の功労者」です。Android誕生のときから使われてきました。Kotlinは2017年にGoogleが「第一級の言語」に指名した存在で、2019年からは公式に「Kotlin-first」を明言。2026年の今では、新規プロジェクトはほぼ全部Kotlinで書かれ、既存プロジェクトもどんどん移行が進んでいます。

率直に言いましょう。完全な初心者なら、まっすぐKotlinを学び、Javaには立ち戻らないことです。理由は3つ。1つは、Kotlinのコード量はJavaより30〜40%少ないこと（同じ機能なら、Kotlinのほうが短くて明確）。2つは、Null Pointer Exceptionという初心者の悪夢を、言語の仕組みレベルで防いでくれること。3つは、最近のチュートリアル、公式ドキュメント、AIプログラミングツール（本書の前半を思い出してください）のすべてがKotlin基準になっていることです。Javaと出会うのは、古いプロジェクトの保守や古いコードを読むときくらいです。

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Java風（くどい版）

{class="font-mono text-xs leading-relaxed"}
public class MainActivity extends Activity {<br>&nbsp;&nbsp;@Override<br>&nbsp;&nbsp;protected void onCreate(Bundle b) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b);<br>&nbsp;&nbsp;&nbsp;&nbsp; setContentView(R.layout.activity);<br>&nbsp;&nbsp;}<br>}
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Kotlin風（すっきり版）

{class="font-mono text-xs leading-relaxed"}
class MainActivity : ComponentActivity() {<br>&nbsp;&nbsp;override fun onCreate(b: Bundle?) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b)<br>&nbsp;&nbsp;&nbsp;&nbsp;setContent { App() }<br>&nbsp;&nbsp;}<br>}
:::
:::

同じ内容なのに、Kotlinでは波かっこや定型的な行がひと山減ります。第五十章で正式に学ぶので、今はこれだけ覚えてください。Android開発の「標準語」の名前はKotlinです。

#### 3. アプリはどうやって生まれるのか？

「アプリ開発」というと、パソコンに向かってひたすらコードを打ち込むイメージを持つ人が多いようです。実際には、アプリはアイデアからユーザーのスマホに届くまで、おおむね次のようなラインをたどります。

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-lightbulb mr-1"></i> アイデア</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center">📐 設計（画面+機能）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-keyboard mr-1"></i> コードを書く</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hammer mr-1"></i> コンパイルとパッケージ化（APK/AAB）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> テスト（エミュレータ+実機）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-rocket mr-1"></i> リリース（ストア/インストールパッケージ）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
図1：Androidアプリがアイデアからストア公開までたどる全工程
:::

この流れの中で、今すぐ知っておきたい概念が2つあります。

- APK：Androidアプリのインストールパッケージ形式（.apk）。タップするだけでスマホにインストールでき、Windowsの.exeのようなものです。普段の自分用テストや、友人に配って遊んでもらうときはこれを使います。
- AAB：Android App Bundle（.aab）。Google Playに公開するための「高機能パッケージ形式」です。ストアがユーザーの機種に応じて動的に切りつぶしてくれるので、誰もがより小さいサイズでダウンロードできます。自分ではインストールできず、ストアに預けるしかありません。

それから、何度も耳にすることばがもう1つあります。SDK（Software Development Kit、ソフトウェア開発キット）です。Android公式が用意する開発装備の一式——各バージョンのAPIライブラリ、デバッグツール、エミュレータのイメージなど——を指します。コードの中で使うActivityやButtonといったクラスは、みなSDKから来ています。

#### 4. Android技術スタックの全体図：あなたの「武器リスト」

学びに入る前に、2026年の主流Androidプロジェクトの標準装備をざっと見ておきましょう。今は分からなくて当然です。本書を読み終えて戻ってくれば、すっきり見えてくるはずです。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">層</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">主流の選択（2026年）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">何のためのもの？</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">言語</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin 2.x</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ロジックを書く言語</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jetpack Compose + Material 3</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">コードでUIを描く（本書のメインライン）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">アーキテクチャ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MVVM + ViewModel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UIとロジックを分けて、コードの混乱を防ぐ</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">データ保存</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room（データベース）＋DataStore（設定）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">データをスマホに保存する</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ネットワーク</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit＋OkHttp＋Kotlinコルーチン</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">サーバーと会話する</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ビルドツール</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle + Kotlin DSL</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">コードをインストールパッケージにする</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">開発環境</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Google公式の「フルセット」IDE</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
2026年のAndroid主流技術スタック早見

この英語の並びに気おくれしないでください。これらはキッチンの鍋やボウルのようなものです。今は「料理するにはキッチンへ」と分かれば十分で、各道具の使い方はこの先の章で1つずつ解き明かします。しかも朗報です。Android Studioで新規プロジェクトを作れば、この一式を自動でセットアップしてくれます。あとは料理に集中するだけです。

#### 5. Android vs iOS：開発者向け最初の「陣取り」の授業

手元にAndroid端末とApple端末が両方あるかもしれません。開発者としては、両者の体験の違いを前もって知っておく価値があります。「どちらが上か」の派閥争いではなく、「どちらが自分のスタートに向いているか」という現実的な話です。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">観点</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Android開発</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">iOS開発</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">開発マシン</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Windows／Mac／Linuxいずれも可</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mac必須（XcodeはMac専用）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">開発ツール</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio（無料）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode（無料）＋ストア公開に年間99ドル</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ストア審査</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">緩い。数時間〜数日</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">厳しい。1〜7日があたりまえ</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">端末に入れて試す</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">APKは自由に配れる、自由に入れられる</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">配布は制限あり。テストには署名/TestFlightが必要</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">収益環境</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">広告／中国国内チャネルが中心</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">App Storeはアプリ内課金の文化がより定着</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">学習コスト</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">概念が多い（4大コンポーネントなど）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">エコシステムは閉じているが体系は統一され、ドキュメントも充実</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
AndroidとiOSの開発パス比較（2026年8月時点）

率直に言えば、お使いのパソコンがMacでなければ、この問題はそもそも選ぶ必要がありません。Androidが唯一の選択肢です。Macをお持ちなら、本書の第8篇と第9篇は並行して読めます。プログラミングの考え方は共通なので、片方を学んでからもう片方に入ると、ぐっと速くなります。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
やってみよう：あなたのスマホの中の「Android」をのぞいてみる

{class="mt-1"}
スマホの［設定］→［端末情報］（「デバイス情報」など）を開き、「Androidバージョン」の欄を探します——そこを何度か連続タップすると、システムの隠しミニゲームが現れます。バージョン番号を書き留めて、上のバージョン表と見比べ、どの世代か確かめてみましょう。あなたのスマホこそ、最初の「開発テスト機」です。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
この章のまとめ

- Androidは2008年誕生。2026年には世界最大シェアのモバイルOSとなり、稼働デバイスは数十億台
- 最新正式版はAndroid 17。主流アプリの最低サポートはAndroid 8〜10。数年前の端末までカバーしてユーザー数を確保
- 新規プロジェクトはとにかくKotlin：コード量30%減、ヌルポ防止、公式のお墨付き
- APKは自分で入れる用、AABはストア公開用。SDKは公式の開発装備一式
- 2026年の標準技術スタック：Kotlin＋Compose＋MVVM＋Room＋Retrofit＋Gradle＋Android Studio
:::
