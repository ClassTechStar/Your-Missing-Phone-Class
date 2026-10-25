---
id: di-wu-shi-san-zhang
num: 53
part: an-zhuo-kai-fa-pian
nav: 第五十三章：データ保存とネットワーク通信
toc: default
kind: chapter
---

### 第五十三章：データ保存とネットワーク通信

{class="chapter-intro mb-4"}
「見る」ことしかできないアプリは生きていません。データを保存できて、ネットにつながるアプリこそが本物です。この章ではAndroidデータ層の「三種の神器」を学びます。DataStore（小さな設定の保存）、Room（構造化データの保存）、Retrofit（サーバーとのやりとり）の3つと、それらを取り仕切る「総指揮者」であるコルーチンです。この章を終える頃には、ユーザーの使い方を覚えて、中身をリアルタイムに更新できる本物のアプリが書けるようになっています。

#### 1. 保存方式の選び方：まずこの表を見る

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">方式</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">何の保存に向くか</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">特徴</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">本書での使用箇所</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DataStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">こまごました設定（テーマ、スイッチなど）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">キーと値のペア。シンプルで安全</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第五十四章の家計簿の設定</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">構造化データ（明細、ユーザーなど）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">本物のSQLiteデータベースのラッパー。検索できる</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第五十四章の収支の記録</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">（保存せず、ネットで取得）サーバーのデータ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">HTTP通信ライブラリの事実上の標準</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第五十五章の天気データ</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
データ三種の神器の分担

覚え言葉をひとつ。「小さな設定はDataStoreへ、まとまったデータはRoomへ、外のデータはRetrofitで」。古いチュートリアルでよく出てくるSharedPreferencesはDataStoreに、手書きSQLのSQLiteはRoomに取って代わられました。最初から新しいやり方を学び、古い道へは戻らないことです。

#### 2. DataStore：小さな設定を保存する

「ユーザーが前回選んだ通貨」「ダークモードを有効にしているか」のようなこまごました値を覚えておきたいときは、DataStore（Preferences版）を使います。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · DataStoreの例</span><span class="dots">···</span>
:::

```
val Context.dataStore by preferencesDataStore(name = "settings")

// 書く：値を保存
suspend fun saveTheme(isDark: Boolean) {
    context.dataStore.edit { prefs ->
        prefs[THEME_KEY] = isDark
    }
}

// 読む：取り出す（Flowが変化を自動通知）
val themeFlow: Flow<Boolean> = context.dataStore.data
    .map { it[THEME_KEY] ?: false }
```
:::

返ってくるのがFlow、つまり「流れる」データの流れである点に注目しましょう。値がひとたび変われば、それを監視しているすべての場所に新しい値が自動で届きます。この概念（リアクティブ）が現代Android開発の土台で、第五十四章で実戦します。

#### 3. Room：データに「本物の家」を用意する

家計簿には何百、何千件もの記録がたまり、しかもカテゴリ別・月別に集計もしたい。そこで必要になるのがデータベースです。RoomはSQLiteの公式ラッパーで、「テーブルを作る・データを引く」をKotlinを書くのと同じように自然にしてくれます。登場するのは3つ。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Roomの三種の神器：Entity / Dao / Database</span><span class="dots">···</span>
:::

```
// 1. Entity：テーブル構造（1テーブル = 1 data class）
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val amount: Double,
    val category: String,
    val note: String,
    val date: String
)

// 2. Dao：操作用インターフェース（追加・削除・変更・検索）
@Dao
interface RecordDao {
    @Query("SELECT * FROM records ORDER BY date DESC")
    fun getAll(): Flow<List<Record>>

    @Insert
    suspend fun insert(record: Record)

    @Delete
    suspend fun delete(record: Record)

    @Query("SELECT SUM(amount) FROM records WHERE category = :c")
    suspend fun sumByCategory(c: String): Double
}

// 3. Database：組み立て
@Database(entities = [Record::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun recordDao(): RecordDao
}
```
:::

この「三種の神器」のテンプレートは、そのままどんなプロジェクトにも持ち込めます。フィールド名を変えるだけでOKです。クエリはFlowを返し、データが変われば画面が自動で更新される。なかなか気持ちのいい仕組みです。

#### 4. Retrofit：サーバーと会話する

天気、ニュース、為替レート……こうしたデータはスマホの中にはなく、他人のサーバー上にあります。Retrofitは「サーバーにデータをねだる」ことを、関数を呼ぶのと同じくらい簡単にしてくれます。3ステップで進みます。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Retrofitの3ステップ</span><span class="dots">···</span>
:::

```
// 1. インターフェースを定義：HTTPリクエストを関数として書き表す
interface WeatherApi {
    @GET("v1/weather")
    suspend fun getWeather(@Query("city") city: String): WeatherResponse
}

// 2. インスタンスを作成
val api = Retrofit.Builder()
    .baseUrl("https://api.example.com/")
    .addConverterFactory(GsonConverterFactory.create())
    .build()
    .create(WeatherApi::class.java)

// 3. 関数のように呼び出す（コルーチンの中で）
val result = api.getWeather("北京")
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
落とし穴注意：ネットワークの2大鉄則

{class="mt-1"}
① ネットワーク通信はメインスレッドで絶対にしてはいけません。画面が固まり、最悪クラッシュします（NetworkOnMainThreadException）。ネットワーク呼び出しは必ずコルーチン（viewModelScope.launch）の中に入れます。② 平文のHTTPはデフォルトで禁止です。Android 9からHTTPSが求められます。テストで http:// のローカルアドレスを使いたい場合は、Manifestに usesCleartextTraffic を明示的に宣言する必要がありますが、正式な製品は必ずすべてHTTPSにすること。
:::

#### 5. JSON解析：ネットのデータに「翻訳」をつける

サーバーが返すデータの多くはJSONです。入れ子になった辞書のようなテキストのことです。RetrofitはこれをKotlinオブジェクトに変えてくれる「翻訳者」を必要とします。2026年の主流は2つあります。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">方式</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">特徴</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">おすすめの場面</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gson / Moshi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">昔からの定番、リフレクション方式。設定の手間ゼロ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">手早く始めたい小規模プロジェクト、フィールドの少ないもの</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">kotlinx.serialization</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">公式のコンパイル時方式。より速く、より安全</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新規プロジェクトの第一候補（2026年の主流）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
JSON解析の2大方式

::: div .code-block
:::inline div .code-head
<span>KOTLIN · kotlinx.serializationの例</span><span class="dots">···</span>
:::

```
// data classに@Serializableアノテーションを付ける
@Serializable
data class WeatherResponse(
    val weather: List<Weather>,
    val main: Main,
    val name: String
)

// Retrofitに対応するConverterを取り付ける（Retrofit 2.11+の公式サポートを例に）：
// .addConverterFactory(json.asConverterFactory("application/json".toMediaType()))
```
:::

どちらの方式でも鉄則は同じです。まず実際に返ってくるJSONを見て、それからフィールドを定義すること。「解析に失敗した」バグの多くは、フィールド名の書き間違いや、入れ子の階層の読み違いが原因です。元のJSONを印字して見比べれば、10秒で原因がつかめます。

#### 6. コルーチン：Androidの並行処理の「共通語」

さきほどから何度も出てきた suspend と launch は、Kotlinコルーチン（Coroutine）のものです。Android公式の並行処理の仕組みです。乱暴に言えば、「少し待つ必要がある」処理（ネットワークやデータベース）が画面を止めないようにするためのもの、と覚えてください。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · コルーチン入門</span><span class="dots">···</span>
:::

```
// ViewModelの中でコルーチンを起動
viewModelScope.launch {
    val records = dao.getAll().first()  // suspend：自動的に待機する
    // 画面の状態を更新……
}

// キーワードの覚え方：
// suspend   —— 「待ちたい、他を止めないで」
// launch    —— 「仕事開始！」
// viewModelScope —— 画面について回る「作業場」。画面が壊れると自動で片付く
```
:::

まずは使い方だけ覚えれば大丈夫です。その裏にある「一時停止と再開」の仕組みは、後からじっくり掘ればいい。ふだんの開発で書くコードの9割は、このテンプレートです。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
やってみよう：「今日のひとこと」アプリを作る

{class="mt-1"}
無料の名言API（hitokotoなど）を探して、Retrofitで「今日のひとこと」を取得し、画面の中央に表示しましょう。「別のひとこと」ボタン（コルーチン内で再リクエスト）も付けます。さらに気に入った文はRoomで「お気に入り」に保存します。この練習でDataStore/Room/Retrofit/コルーチンを全部使うことになります。これができれば、第7・8章は楽勝です。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章のまとめ

- 覚え言葉：小さな設定はDataStoreへ、まとまったデータはRoomへ、外のデータはRetrofitで
- DataStoreはFlowを返す：値が変われば、監視している側に自動で届く
- Roomの三種の神器：@Entity（テーブル）＋@Dao（操作）＋@Database（組み立て）。テンプレートはそのまま再利用できる
- Retrofitの3ステップ：インターフェースを定義 → インスタンスを作る → コルーチン内で呼ぶ
- 2大鉄則：ネットワークはメインスレッドに入れない。正式な製品は必ずHTTPS
- コルーチン＝画面を止めない待ち方。viewModelScopeは画面専用の作業場
:::
