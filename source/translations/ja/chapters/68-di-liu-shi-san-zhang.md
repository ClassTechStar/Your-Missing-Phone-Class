---
id: di-liu-shi-san-zhang
num: 63
part: ios-kai-fa-pian
nav: 第六十三章：ビュー、ステート、ナビゲーション
toc: default
kind: chapter
---

### 第六十三章：ビュー、状態、ナビゲーション

{class="chapter-intro mb-4"}
1ページだけのおもちゃなら、もう作れます。この章で解決するのは「成長」にまつわる2つの問題：複数のページの間をどう行き来するか（ナビゲーション）と、データがページの間をどう流れるか（状態管理）です。この章を終えれば、「リスト → 詳細 → 編集」という定番のマルチページアプリの骨組みが組めるようになります。

#### 1. 状態管理の「データフロー全体図」

SwiftUIの状態管理ツールは@Stateだけではありません。まずこの全体図を見て、「いつどれを使うか」をつかみましょう：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ツール</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">担当するもの</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">使う側</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">典型的な場面</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">そのページだけの一時的な状態</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">いまのビュー</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">カウンター、入力欄の文字</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Binding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ほかの状態を借りる</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">子ビューから親ビューを書き換える</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自作コンポーネント</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@StateObject / @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ページをまたいで共有するロジック</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ビューモデル（ViewModel）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">データ読み込み、ビジネスロジック</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@EnvironmentObject / .environment</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">アプリ全体で共有する状態</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">アプリ全体</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ログイン状態、テーマ設定</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
SwiftUIの状態管理ツール全体図（2026年、@Observableが主流）

::: div .code-block
:::inline div .code-head
<span>SWIFT · 2026年の主流：@Observableビューモデル</span><span class="dots">···</span>
:::

```
// iOS 17+のモダンな書き方：@Observableマクロ（新規プロジェクトにおすすめ）
import Observation

@Observable
class CounterModel {                 // ビューモデル
    var count = 0
    func increment() { count += 1 }
}

struct CounterView: View {
    @State private var model = CounterModel()   // モデルを保持

    var body: some View {
        VStack {
            Text("\(model.count)回押しました")
            Button("押して") { model.increment() }
        }
    }
}
```
:::

初心者へのぶっきらぼうなアドバイス：ページの中だけで使うものは@State、ページをまたぐもの／ロジックを含むものは@Observableのクラスへ。古いチュートリアルの@StateObject/@ObservableObjectは前世代の書き方なので、読めればOK。新しいコードは上のルールに従いましょう。

#### 2. NavigationStack：ページ移動の「スタック」

iOS 16以降、複数ページのナビゲーションにはNavigationStackを使います——お皿を積むようなもので、進むときに1枚ずつ積んでいき、戻るときは1枚ずつ取り出します：

::: div .code-block
:::inline div .code-head
<span>SWIFT · NavigationStackナビゲーション</span><span class="dots">···</span>
:::

```
struct HomeView: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("たろうの家計簿") {
                    DetailView(name: "たろうの家計簿")   // 行き先のページ
                }
                NavigationLink("はなこの家計簿") {
                    DetailView(name: "はなこの家計簿")
                }
            }
            .navigationTitle("家計簿リスト")   // 上の大きな見出し
        }
    }
}

struct DetailView: View {
    let name: String
    var body: some View {
        Text("\(name) の詳細ページ")
            .navigationTitle(name)
            .navigationBarTitleDisplayMode(.inline)
    }
}
```
:::

NavigationLinkは「タップできる移動リンク」です。navigationTitleはナビゲーションバーのタイトルと戻るボタンを自動で生成します。プログラムで移動させたいとき（たとえば「保存」を押したら自動で戻る）は、@Environment(\.dismiss)で現在のページを閉じます——この2つの合わせ技で、ナビゲーションのニーズの90％はカバーできてしまいます。

#### 3. ポップアップと下部タブ：sheetとTabView

ページを「押し込む」以外にも、定番の操作が2つあります：

::: div .code-block
:::inline div .code-head
<span>SWIFT · sheetダイアログ + TabViewタブ</span><span class="dots">···</span>
:::

```
// 1. 下から半画面/全画面で表示（入力フォームの定番）
struct HomeView: View {
    @State private var showAdd = false
    var body: some View {
        Button("記帳する") { showAdd = true }
            .sheet(isPresented: $showAdd) {
                AddRecordView()     // 表示される入力ページ
            }
    }
}

// 2. 下部タブバー（アプリの「骨格」）
struct MainTabView: View {
    var body: some View {
        TabView {
            RecordListView()
                .tabItem { Label("家計簿", systemImage: "book") }
            StatsView()
                .tabItem { Label("統計", systemImage: "chart.pie") }
            SettingsView()
                .tabItem { Label("設定", systemImage: "gear") }
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ワンポイント：どの場面でどれを使う？

{class="mt-1"}
経験則：メインの流れはNavigationStackでページをpush（リスト→詳細）、一時的な操作はsheetのポップアップ（追加・編集・確認）、並び立つ大ブロックはTabView（下部タブ）。この3つの組み合わせこそ、ほとんどのアプリの骨組みです。
:::

#### 4. List：iOSの「国民的リスト」

iOSでいちばんよく使い、いちばん「Appleらしい」コンポーネントがListです——区切り線、スワイプ削除、タップ時のハイライトが、はじめから付いてきます：

::: div .code-block
:::inline div .code-head
<span>SWIFT · Listリスト + スワイプ削除</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var records = ["昼ごはん 25.5", "地下鉄 6.0", "給料 +8000"]

    var body: some View {
        List {
            ForEach(records, id: \.self) { r in
                Text(r)
            }
            .onDelete { indexSet in          // 左スワイプで削除
                records.remove(atOffsets: indexSet)
            }
        }
    }
}
```
:::

リスト＋NavigationLink＋sheet＋TabView——この4つを組み合わせれば、「帳簿リスト → タップで詳細 → ＋で入力ポップアップ」という完全なアプリの骨組みがもう組めます。次章の家計簿プロジェクトは、まさにこの組み方で作ります。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
やってみよう：「3ページの骨組み」を組む

#### 5. アプリのライフサイクル：フォアグラウンドとバックグラウンド

AndroidのActivityのライフサイクルと同じように、iOSアプリにも「誕生、フォアグラウンド、バックグラウンド、終了」という状態の変化があります。SwiftUIではscenePhaseという環境値で観察します：

::: div .code-block
:::inline div .code-head
<span>SWIFT · フォアグラウンド/バックグラウンド切替の観察</span><span class="dots">···</span>
:::

```
@main
struct MyApp: App {
    @Environment(\.scenePhase) private var phase

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .onChange(of: phase) { _, newPhase in
            switch newPhase {
            case .active:    print("前面に戻る。更新を再開")
            case .inactive:  print("移行中（着信/バックグラウンド切替の瞬間）")
            case .background: print("バックグラウンドへ。下書きを保存")
            @unknown default: break
            }
        }
    }
}
```
:::

典型的な使い方：フォアグラウンドに戻ったらデータを更新、バックグラウンドに入ったら下書きを保存。iOSはバックグラウンド動作にとても厳しく——普通のアプリはバックグラウンドに入るとすぐ停止（凍結）されるので、裏でこっそり重い処理をさせるのは期待しないでください。どうしても定期実行したいなら、「バックグラウンド常駐」ではなく第六十八章のローカル通知を使います。

{class="mt-1"}
ダミーデータ版の家計簿の骨組みを作りましょう：TabViewの3つのタブ（帳簿／統計／設定）→ 帳簿ページはListでダミーデータを表示し、行をタップしたら詳細へ（NavigationStack）→ 右上の「＋」ボタンで入力用のsheetを出す。データ保存も通信もなし、純粋に骨組みの練習——この骨組みができていれば、第六十五章で本物のデータを流し込むのは水到渠成です。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章のまとめ

- 状態管理の4ツール：@State（ページ内）、@Binding（借用）、@Observable（ロジック）、.environment（全体）
- 新規プロジェクトのビューモデルは@Observableマクロで書く。古いチュートリアルの@ObservableObjectは読めればOK
- ページ移動はNavigationStack。@Environment(\.dismiss)でプログラムから戻る
- メインの流れはページをpush、一時的な操作はsheet、並び立つ大ブロックはTabView
- Listは「国民的リスト」：区切り線もスワイプ削除も、はじめから使える
:::
