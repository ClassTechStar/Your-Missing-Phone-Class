---
id: di-wu-shi-si-zhang
num: 54
part: an-zhuo-kai-fa-pian
nav: 第五十四章：プロジェクト1——家計簿アプリ（ローカル版）
toc: default
kind: chapter
---

### 第五十四章：プロジェクト1——わたしの家計簿（ローカル版）

{class="chapter-intro mb-4"}
いよいよ最初の「きちんとしたプロジェクト」です。この家計簿はネットにはつながりませんが、中身はそろっています。記録を付けられて、履歴が見られて、月ごとの集計ができて、削除も編集もできる。作り終える頃には、「データ → ロジック → 画面」の全工程を一通り歩いたことになります。コードを急いで写そうとしないこと。まず考えてから手を動かす。これが本書のいつもの方針です。

#### 1. 要件を考える：まず5つの質問

手を動かす前に、「要件の5要素」でアイデアを整理しましょう。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要素</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">答え</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who（誰に使うか）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自分用。家族や友人でもOK</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What（何をするか）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">収支を記録、履歴を見る、月ごとにまとめる、カテゴリ別に集計</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why（なぜ作るか）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">練習＋お金を何に使ったかをはっきりさせる</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How（どう作るか）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin＋Compose＋Room＋MVVM。完全ローカルでサーバーなし</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint（制約）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1週間で完成。Android 8以上に対応。ストアに出さないとしても、出品基準で作っておく</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
家計簿の要件5要素

次に、「どの段階でも使える」小さなステップに分解します。①Roomのデータ層を作る（1件保存できる）。②一覧画面（履歴が見られる）。③入力画面（記録を追加できる）。④削除と編集。⑤月次のまとめカード。1ステップ終えるたびに、アプリは「使えるもの」になっています。

#### 2. データ層：記録に「住まい」を与える

まず1件の記録がどんな形かを定義します。フィールドは足りる分だけで、欲張らないこと。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Record.kt（エンティティ）</span><span class="dots">···</span>
:::

```
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val type: String,        // "income" 収入 | "expense" 支出
    val amount: Double,      // 金額（元）
    val category: String,    // カテゴリー：食費、交通、給料……
    val note: String = "",   // メモ（任意）
    val date: String         // "2026-08-15"
)
```
:::

Daoに「集計用」のクエリを2つ追加します。ここが家計簿の魂です。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordDao.kt（集計クエリ）</span><span class="dots">···</span>
:::

```
@Dao
interface RecordDao {
    @Query("SELECT * FROM records ORDER BY date DESC, id DESC")
    fun getAll(): Flow&lt;List&lt;Record&gt;&gt;

    @Insert
    suspend fun insert(record: Record)

    @Delete
    suspend fun delete(record: Record)

    @Query("SELECT COALESCE(SUM(amount),0) FROM records WHERE type='income' AND date LIKE :month || '%'")
    suspend fun monthIncome(month: String): Double   // monthは「2026-08」の形

    @Query("SELECT COALESCE(SUM(amount),0) FROM records WHERE type='expense' AND date LIKE :month || '%'")
    suspend fun monthExpense(month: String): Double
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ワンポイント：金額はなぜDouble？

{class="mt-1"}
真面目な金融アプリは、BigDecimalや「分（セント）単位のInt」で浮動小数点の誤差（0.1+0.2≠0.3という古典的な問題）を避けます。練習のプロジェクトならDoubleで十分です。いつか本物の金融の製品を作るときは「分」単位に替えるのを忘れずに。先人たちが無数に踏んできた落とし穴です。
:::

#### 3. MVVM：画面とロジックを「別々の家」にする

画面から直接データベースを操作させたら？　動きはしますが、画面のコードは長くて読みにくくなります。MVVMアーキテクチャなら、それぞれの役割がはっきりします。View（画面）は描くことだけ、ViewModel（ロジックの中枢）はデータを担当、Model（Room）は保存を担当です。

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View（Composeの画面）</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel（状態とロジック）</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model（Roomのデータ層）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
図5：MVVMの3層構造——データは一方向に流れ、各層は互いに境界を越えない
:::

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordViewModel.kt（骨格）</span><span class="dots">···</span>
:::

```
class RecordViewModel(private val dao: RecordDao) : ViewModel() {

    // Flowを画面から観察できる状態に変換
    val records = dao.getAll()
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(), emptyList())

    // ユーザー操作：suspend関数を呼ぶ
    fun addRecord(type: String, amount: Double, category: String, note: String, date: String) {
        viewModelScope.launch {
            dao.insert(Record(type = type, amount = amount,
                category = category, note = note, date = date))
        }
    }

    fun deleteRecord(record: Record) {
        viewModelScope.launch { dao.delete(record) }
    }
}
```
:::

画面（Compose）ではこう書きます。val vm: RecordViewModel = viewModel() として、続いて val list by vm.records.collectAsState()。データが変わればリストが自動で更新され、こちらは何もする必要がありません。これがMVVM＋Flow＋Composeの三本柱がそろった力です。

#### 4. 画面：一覧画面＋入力画面

一覧画面にはLazyColumn（遅延読み込みリスト）を使います。データがどれだけ増えても動きが重くなりません。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 家計簿リスト画面（核心部分）</span><span class="dots">···</span>
:::

```
@Composable
fun RecordListScreen(vm: RecordViewModel) {
    val records by vm.records.collectAsState()

    Column {
        // 上部の集計カード（収入-支出=残高）
        SummaryCard(records)

        // 明細リスト
        LazyColumn {
            items(records, key = { it.id }) { record -&gt;
                RecordRow(record) { vm.deleteRecord(record) }
            }
        }

        // 浮遊する「記帳」ボタン → 入力ダイアログを出す
        FloatingActionButton(onClick = { showAddDialog = true }) {
            Text("+")
        }
    }
}

@Composable
fun RecordRow(record: Record, onDelete: () -&gt; Unit) {
    Row(Modifier.fillMaxWidth().padding(12.dp)) {
        Text(record.category, fontWeight = FontWeight.Bold)
        Spacer(Modifier.weight(1f))
        Text(if (record.type == "income") "+${record.amount}" else "-${record.amount}",
             color = if (record.type == "income") Color(0xFF27AE60) else Color(0xFFC0392B))
    }
}
```
:::

入力にはAlertDialog（ダイアログ）が一番手軽です。入力欄をいくつか並べて、収入／支出の切り替え、カテゴリのプルダウンを付け、「確定」を押したら vm.addRecord(...) を呼ぶだけです。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：入力チェックは手を抜かない

{class="mt-1"}
金額の入力欄は必ずチェックします。空の値、マイナス、「abc」のような不正な入力は全部はじきます（toDoubleOrNull() で判定）。アプリがクラッシュするいちばんよくある原因のひとつが、「ユーザーの入力をいい子だと思い込む」ことです。ユーザーの入力はすべて、敵として吟味する、と覚えてください。
:::

#### 5. 編集と削除：データを「入れて出せる」ように

追加だけできて削除できない家計簿は、3日で使わなくなります。操作を2つ足しましょう。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 削除と編集</span><span class="dots">···</span>
:::

```
// Daoに2つ追加：
@Query("UPDATE records SET amount=:amount, category=:category, note=:note WHERE id=:id")
suspend fun update(id: Long, amount: Double, category: String, note: String)

@Query("DELETE FROM records WHERE id=:id")
suspend fun deleteById(id: Long)

// 画面では：リスト項目を長押しして「編集/削除」メニューを出す（ComposeはDropdownMenuかAlertDialogを使う）
// 削除前には確認ダイアログを出すのが一番——「うっかり削除」は家計簿アプリのユーザーが最も嫌うこと
```
:::

操作まわりの細かいコツが2つ。削除は必ず二重確認にする（うっかり操作の防止）。編集はできるだけ元の値を先に入れておく（1文字だけ直すほうが、打ち直すより楽）。この2つの細かい点を舐めてはいけません。製品らしい使い心地は、こうした積み重ねでできているのです。

#### 6. 検収：3層のチェック＋2つの上級チャレンジ

プロジェクトができたら、「機能 → 境界 → アーキテクチャ」の3層で検収します。記録できるか、削除できるか、アプリを開き直してもデータが残っているか（機能）。金額に0やマイナスを入れてもクラッシュしないか、画面回転でデータが消えないか（境界）。画面とデータが混ざっていないか、値がハードコーディングされていないか（アーキテクチャ）。

基本版の検収を通ったら、自分に「上級の一品」を2つ追加しましょう。

1. 月別フィルター：上部に月の切り替え（たとえば 2026-08 ▾）を付け、リストには当月の履歴だけを表示する。
2. カテゴリ別の円グラフ：ComposeのCanvasを使うか、軽量なグラフライブラリを入れて、「お金を何に使ったか」を円グラフにします。ここまでできれば、家計簿はだいぶ「製品っぽく」なります。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
やってみよう：今週中に完成させる

{class="mt-1"}
「データ層 → ViewModel → 一覧画面 → 入力画面 → まとめカード」の順に手を動かし、1日1ステップで進めます。つまづいたら、エラーをそのまま検索エンジンやAIに投げましょう（第7部『AIプログラミング実戦編』を覚えていますか？　問題を説明するときは「期待する動作・実際の動作・再現手順」をはっきり伝えます）。完成したら、1週間これで家計をつけてみてください。自分で作ったアプリを使うと、達成感が先へ進む力になります。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章のまとめ

- 要件の5要素 → 「どの段階でも使える」小ステップに分解してから手を動かす
- データ層：Recordエンティティ＋Dao（月次集計のSQLを含む）＋Database
- MVVMの分担：Viewは描くだけ、ViewModelはロジック、Modelは保存
- Flow＋stateIn＋collectAsState：データが変われば画面が自動で更新される
- LazyColumnは遅延読み込みリスト。入力にはAlertDialog
- 3層の検収（機能／境界／アーキテクチャ）＋上級チャレンジ（月別フィルター、カテゴリ別円グラフ）
:::
