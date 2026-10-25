---
id: di-liu-shi-ba-zhang
num: 68
part: ios-kai-fa-pian
nav: 第六十八章：上達への道——権限、通知、モダンアーキテクチャ
toc: default
kind: chapter
---

### 第六十八章：ステップアップへの道——権限、通知、モダンなアーキテクチャ

{class="chapter-intro mb-4"}
App が作れるようになるのは、まだ始まりにすぎません。この章では「作れる」から「うまく作る」までのいくつかのハードル——権限をスマートに要求する方法、嫌われない通知の出し方、アーキテクチャをもう一段引き上げる方法、そして2026年において AI と組んで iOS コードを書く方法——を取り上げます。どれも、実際のプロジェクトですぐに出会う話ばかりです。

#### 1. 権限：まずノック、それから入る

カメラ、位置情報、連絡先、通知……こうした「センシティブな領域」では、iOS は App が使う場面でユーザーにダイアログを出して許可を求めることを求めています。お作法は「宣言 + 要求 + 代替動作の用意」の3ステップです。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 権限の申請（位置情報の例）</span><span class="dots">···</span>
:::

```
// 1. Info.plistに用途の文を宣言（宣言しないと即クラッシュ！）
// Privacy - Location When In Use Usage Description: "現在地の都市の天気を調べるために使用します"

// 2. 使うときに申請
import CoreLocation

@Observable
class LocationModel {
    private let manager = CLLocationManager()

    func request() {
        switch manager.authorizationStatus {
        case .notDetermined: manager.requestWhenInUseAuthorization()
        case .denied, .restricted: /* 設定画面へ誘導 */
        default: /* 許可済み、始めよう */
        }
    }
}

// 3. 拒否されたときの優雅な代替：案内を表示 + 設定へ誘導
// UIApplication.shared.open(URL(string: UIApplication.openSettingsURLString)!)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：iOS の権限は「一度きり」

{class="mt-1"}
iOS の権限ダイアログは1度しか表示されません——ユーザーが拒否したら二度と出ません。だからこそ、要求のタイミングは「ユーザーがまさに使おうとしている瞬間」を選び（起動直後にいきなり何個も出さない）、文言では用途を説明しましょう。拒否されたあとの画面での案内（「設定で位置情報をオンにしよう」）は必須の配慮です。ユーザーを行き止まりに追い込まないこと。
:::

#### 2. 通知：正しいタイミングで役立つ言葉を届ける

通知は App がユーザーに届く大切な通路であると同時に、もっとも「ブロック」されやすい機能でもあります。iOS では UserNotifications フレームワークを使います。通知の3カ条は、役に立つものだけ送る、ユーザーがオフにできるようにする、深夜に騒がない。基本の使い方は次のとおりです。

::: div .code-block
:::inline div .code-head
<span>SWIFT · ローカル通知</span><span class="dots">···</span>
:::

```
import UserNotifications

// 1. 通知の権限を申請（ポップアップは1回）
UNUserNotificationCenter.current()
    .requestAuthorization(options: [.alert, .sound, .badge]) { granted, _ in
        print(granted ? "許可された" : "拒否された")
    }

// 2. 「毎日20:00に記帳リマインダー」を予約
func scheduleDailyReminder() {
    let content = UNMutableNotificationContent()
    content.title = "記帳リマインダー"
    content.body = "今日はまだ記帳していないよ"
    content.sound = .default

    var comps = DateComponents()
    comps.hour = 20
    let trigger = UNCalendarNotificationTrigger(dateMatching: comps, repeats: true)

    let request = UNNotificationRequest(
        identifier: "daily-reminder",
        content: content,
        trigger: trigger
    )
    UNUserNotificationCenter.current().add(request)
}
```
:::

注意：iOS の通知権限も同じく「一度きり」で、ユーザーはシステム設定でいつでもオフにできます——だからこそ、通知の中身の「価値」がとても重要です。一度でも乱発すれば、ユーザーを永遠に失いかねません。

#### 3. アーキテクチャのステップアップ：MVVM の深掘りとテスト容易性

第六十五章で MVVM を使いました。ここで、レベルアップのためのポイントを3つ補足します。

- プロトコル抽象化：ViewModel を具体的なクラスではなくプロトコルに依存させます——テストのときに「偽のデータソース」を注入でき、テスト容易性の土台になります。
- 単一責任：1つの ViewModel は1つのことだけを担当する（家計簿担当は天気を扱わない）。機能が増えたら分割する。
- 設計しすぎない：一人の小さなプロジェクトなら「@Observable クラス + プロトコル抽象化」で十分です。VIPER や Clean Architecture のような重いアーキテクチャは、チームや複雑さが訪れてから考えましょう——ツールは目的に仕えるものであって、見せびらかすためのものではありません。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ワンポイント：SwiftUI の「エコシステムの恩恵」

{class="mt-1"}
iOS エコシステムには、ここでしか使えないレベルアップの技がもう2つあります。ウィジェット（WidgetKit）は App を開かなくても情報を確認できるようにします（家計簿アプリの「今月の支出」をホーム画面に置くイメージ）。ショートカット（App Intents）は、ユーザーが Siri やオートメーションからあなたの機能を呼び出せるようにします。どちらも公式フレームワークが用意され、導入コストは高くないのに、ユーザー体験への追い風は絶大です——ステップアップの道では優先的に解禁したい能力です。
:::

#### 4. 2026年の新常識：AI 支援の iOS 開発

2026年、AI はすでに Apple の開発フローに深く組み込まれています。作業を速めたいなら、次の組み合わせがすっかり定着しています。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">場面</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">AI の助け方</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">あなたの役割</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">コードを書く</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode 内蔵のコード補完 + サードパーティ AI プラグインによる生成</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">要件を明確に伝え、生成物をレビューする</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">調べもの</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">公式ドキュメントやエラーメッセージを AI に渡して解説してもらう</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">重要な結論は公式ドキュメントで裏取りする</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">テストを書く</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">「正常／境界／異常」の3分類で XCTest ケースを AI に生成させる</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ケースが業務の意味に合っているか確認する</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">バグを直す</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">クラッシュログと関係するコードを貼り、AI に原因特定と修正をしてもらう</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">変更を理解し、テストを回して検証する</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
AI 支援 iOS 開発の4つの場面

具体的な方法論——AI への指示の出し方、成果物の受け取り方、落とし穴の避け方——は、本書の第7部『AIプログラミング実践編』（第37〜47章）に全11章ぶん収録しています。あわせて読むことを強くおすすめします。Swift の文法はこの部で、AI との協働のコツは第7部で、という分担です。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
やってみよう：家計簿アプリに「3点セット」を追加する

#### 5. Swift の並行処理の要点：@MainActor と Task

Swift 6 の並行処理の仕組みには、初心者が必ず知っておくべきルールが2つあります。

- UI はメインスレッドでしか更新できない：SwiftUI のビューはデフォルトで @MainActor なので、ネットワークのコールバックはメインスレッドに戻ってから状態を更新します（await MainActor.run { ... } を使うか、ViewModel を @MainActor としてマーク）。
- 非同期タスクは Task で管理する：.task { } モディファイアはビューが現れると自動で始まり、消えると自動でキャンセルされます——SwiftUI で非同期処理を始める標準の作法です。body の中に Task をむき出しで書き散らかすのは避けましょう。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 標準の非同期スタイル</span><span class="dots">···</span>
:::

```
struct WeatherScreen: View {
    @State private var vm = WeatherViewModel()

    var body: some View {
        Group {
            switch vm.state {
            case .loading: ProgressView()
            case .success(let d): WeatherContent(data: d)
            case .error(let m): Text(m)
            }
        }
        .task {                       // 現れたら開始、消えたら取消
            await vm.search(city: "北京")
        }
    }
}
```
:::

この2つのルールの背景には、Swift 6 の「データ競合安全」設計があります——間違えたとき、App がクラッシュするのを待たずにコンパイラがその場でエラーを出してくれます。コンパイラのエラーは嫌がらせではなく、あなたに代わって弾丸を受けてくれているのです。

{class="mt-1"}
① 家計簿アプリに「毎日20:00の記帳リマインダー」を追加する（通知権限 + ローカル通知）。② ViewModel のデータソースをプロトコル抽象化に替え、偽データを注入するユニットテストを1つ書く。③「今月の支出」のホーム画面ウィジェットを追加する。3点セットが完成すれば、あなたのプロジェクトは「正規軍」の風格を帯びてきます。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
この章のまとめ

- 権限の3ステップ：Info.plist での宣言（抜けると必ずクラッシュ）、使うときに要求、拒否されたら設定への案内
- iOS の権限ダイアログは一度きり：タイミングは「まさに使おうとする瞬間」を選び、文言で用途をはっきり書く
- 通知の3カ条：役に立つものだけ、オフにできる、迷惑をかけない。フレームワークは UserNotifications
- MVVM のステップアップ：プロトコル抽象化（テスト可能に）、単一責任、設計しすぎない
- エコシステムの恩恵：WidgetKit ウィジェット + App Intents ショートカット
- AI 支援の4つの場面：コーディング、調べもの、テスト作成、バグ修正。方法論は第7部（第37〜47章）参照
:::
