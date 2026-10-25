---
id: di-liu-shi-wu-zhang
num: 65
part: ios-kai-fa-pian
nav: 第六十五章：プロジェクト1——家計簿アプリ（ローカル版）
toc: default
kind: chapter
---

### 第六十五章：プロジェクト1——わたしの家計簿（ローカル版）

{class="chapter-intro mb-4"}
あなたの初めての「まともなプロジェクト」へようこそ。この家計簿はネットにはつながりませんが、中身は一通り揃っています：1件の記録ができ、履歴が見られて、月ごとに集計できて、削除・編集もできます。完成すれば、「データ → ロジック → 画面」の全工程をひととおり歩いたことになります。コードをいきなり写すのは急がないで——まずよく考えてから手を動かす。それが私たちのいつもの原則です。

#### 1. 要件を考える：まず5つの質問

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要素</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">答え</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who（誰が使うか）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自分用。家族や友だちでもOK</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What（何を作るか）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">収支を記録、履歴を見る、月ごとにまとめる、カテゴリ別に集計</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why（なぜ作るか）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">練習＋お金を何に使ったかをはっきりさせる</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How（どう作るか）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift＋SwiftUI＋SwiftData＋MVVM。完全ローカル、サーバーなし</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint（制約）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1週間で完成。iOS 17以上をサポート（SwiftDataの要件）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
家計簿の要件5要素

そして「どの段階でも使える」小さなステップに分解します：①SwiftDataのデータ層を作る（1件保存できる）。②リストページ（履歴が見られる）。③入力ポップアップ（記録を追加できる）。④削除と編集。⑤月次集計カード。1ステップ終えるごとに、アプリは「使えるもの」になります。

#### 2. データ層：記録に「家」を用意する

まず1件の記録がどんな形かを定義します——フィールドは十分に、でも欲張らない：

::: div .code-block
:::inline div .code-head
<span>SWIFT · Record.swift（モデル）</span><span class="dots">···</span>
:::

```
import SwiftData

@Model
class Record {
    var type: String      // "income" 収入 | "expense" 支出
    var amount: Double    // 金額（元）
    var category: String  // カテゴリー：食費、交通、給料……
    var note: String      // メモ（任意）
    var date: Date        // 記帳日

    init(type: String, amount: Double, category: String, note: String = "", date: Date = Date()) {
        self.type = type
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ワンポイント：金額はなぜDouble？

{class="mt-1"}
本格的な金融アプリは、浮動小数点の誤差（0.1＋0.2≠0.3という昔からの問題）を避けるためにDecimal（正確な十進数）を使います。練習用プロジェクトならDoubleで十分です。いつか本物の金融商品を作るときは、Decimalか「分単位のInt」に切り替えるのを忘れずに——これは先人たちが何度も踏んできた落とし穴です。
:::

#### 3. MVVM：画面とロジックの「世帯分け」

画面にデータベースを直接操作させる？　動きはしますが、画面のコードが長ったらしくなります。MVVMアーキテクチャなら、それぞれが持ち場を守ります：View（画面）は描くことだけ、ViewModel（ロジックの中枢）はデータを担当、Model（SwiftData）は保存を担当。

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View（SwiftUIの画面）</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel（@Observableのロジック中枢）</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model（SwiftDataのデータ層）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
図4：MVVMの3層構造——データは一方向に流れ、各層は互いに踏み込まない
:::

::: div .code-block
:::inline div .code-head
<span>SWIFT · RecordViewModel.swift（骨格）</span><span class="dots">···</span>
:::

```
import Observation

@Observable
class RecordViewModel {
    var records: [Record] = []
    private let context: ModelContext

    init(context: ModelContext) { self.context = context }

    func load() {
        // SwiftDataの#Predicateで絞り込み + 並べ替え
        let descriptor = FetchDescriptor<Record>(
            sortBy: [SortDescriptor(\.date, order: .reverse)]
        )
        records = (try? context.fetch(descriptor)) ?? []
    }

    func add(type: String, amount: Double, category: String, note: String) {
        let r = Record(type: type, amount: amount, category: category, note: note)
        context.insert(r)
        try? context.save()
        load()                       // 読み込み直す。画面が更新される
    }

    func delete(_ record: Record) {
        context.delete(record)
        try? context.save()
        load()
    }
}
```
:::

画面の中で@State private var vm = RecordViewModel(...)としておき、vm.recordsをそのままリストに描画——データが変わると、画面も自動で更新されます。

#### 4. 画面：リストページ＋入力ポップアップ

::: div .code-block
:::inline div .code-head
<span>SWIFT · 家計簿リスト画面（核心部分）</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var vm: RecordViewModel
    @State private var showAdd = false

    var body: some View {
        NavigationStack {
            List {
                Section("今月の残高") {          // 集計カード
                    SummaryRow(records: vm.records)
                }
                Section("明細") {
                    ForEach(vm.records) { r in
                        RecordRow(record: r)
                    }
                    .onDelete { idx in
                        idx.forEach { vm.delete(vm.records[$0]) }
                    }
                }
            }
            .navigationTitle("私の家計簿")
            .toolbar {
                Button { showAdd = true } label: {
                    Image(systemName: "plus")
                }
            }
            .sheet(isPresented: $showAdd) {
                AddRecordView(vm: vm)          // 入力ダイアログ
            }
        }
    }
}
```
:::

入力ポップアップのポイント：金額入力欄のキーボードは.keyboardType(.decimalPad)（数字キーボード）。収入／支出はセグメントコントロール（Picker）で、カテゴリはメニューで選択。「保存」を押したらvm.add(...)を呼び、dismiss()で閉じます。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：入力チェックの手抜きは禁物

{class="mt-1"}
金額入力欄は必ずチェックしましょう：空の値、負の数、"abc"のような不正な入力はすべてはじく（Double(text)で判定し、失敗するとnilが返ります）。アプリがクラッシュするいちばんよくある原因のひとつが、「ユーザーの入力をお行儀のいい子だと思い込む」ことです。忘れずに：ユーザーが入力したものは、すべて敵として審査する。
:::

#### 5. 編集、削除、集計

- 削除：Listの.onDeleteで左スワイプ削除＋確認ポップアップ（うっかり削除は、家計簿系アプリのユーザーがいちばん恨むものです）。
- 編集：行をタップして編集ポップアップへ。元の値を先に入れておく（1文字直すほうが、打ち直すよりずっとラク）。
- 集計：filter＋reduceで「今月の収入／支出／残高」を計算して、上部のカードに表示します：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 月次集計の計算</span><span class="dots">···</span>
:::

```
func monthSummary(_ records: [Record]) -> (income: Double, expense: Double) {
    let cal = Calendar.current
    let monthRecords = records.filter {
        cal.isDate($0.date, equalTo: Date(), toGranularity: .month)
    }
    let income = monthRecords
        .filter { $0.type == "income" }
        .reduce(0) { $0 + $1.amount }
    let expense = monthRecords
        .filter { $0.type == "expense" }
        .reduce(0) { $0 + $1.amount }
    return (income, expense)
}
```
:::

#### 6. 検収：3層チェック＋2つの上級チャレンジ

プロジェクトが完成したら、「機能 → 境界 → アーキテクチャ」の3層で検収します：記録できるか、削除できるか、アプリを再起動してもデータが残っているか（機能）。金額に0や負の数を入れてもクラッシュしないか（境界）。画面とデータが混ざっていないか、フィールドがハードコードされていないか（アーキテクチャ）。

基本版の検収をパスしたら、自分に2品の「上級メニュー」を出しましょう：

1. カテゴリ別集計：「統計」タブを追加して、Swift Chartsでカテゴリ別支出を円グラフ／棒グラフに——Apple公式のグラフライブラリで、数行のコードでグラフが描けます。
2. iCloud同期：SwiftDataのiCloud同期は、設定をいくつか入れるだけ——帳簿がiPhone／iPadの間で自動同期されて、一気に「高級感」が出ます。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
やってみよう：今週中に完成させる

{class="mt-1"}
「データ層 → ViewModel → リストページ → 入力ポップアップ → 集計カード」の順に手を動かし、1日1ステップ。つまづいたら、エラーをそのまま検索エンジンやAIに投げましょう（第7編『AIプログラミング実践編』を覚えていますか？　問題を説明するときは「期待した動き、実際の動き、再現手順」をはっきりと）。完成したら、1週間これで家計簿をつけてみてください——自分で作ったアプリを使うと、達成感が次へ進む力になります。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章のまとめ

- 要件5要素 → 「どの段階でも使える」小ステップに分解してから、着手する
- データ層：@Modelモデル＋modelContainerコンテナ＋FetchDescriptorクエリ
- MVVMの分担：Viewは描くだけ、@ObservableなViewModelがロジック、SwiftDataが保存を担当
- 画面：List＋Section＋toolbar＋sheetの入力ポップアップ
- 3層検収（機能／境界／アーキテクチャ）＋上級チャレンジ（Swift Charts、iCloud同期）
:::
