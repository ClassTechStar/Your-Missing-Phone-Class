---
id: di-wu-shi-wu-zhang
num: 55
part: an-zhuo-kai-fa-pian
nav: 第五十五章：プロジェクト2——天気チェックアプリ（ネットワーク版）
toc: default
kind: chapter
---

### 第五十五章：プロジェクト2——天気チェックアプリ（ネットワーク版）

{class="chapter-intro mb-4"}
家計簿が「内功の鍛錬」なら、天気アプリは「外の世界へ出る」プロジェクトです——インターネットと付き合うことになります。ここで学ぶのは、無料APIの申し込み、JSONの解析、「読み込み中／成功／失敗」の3つの画面状態の処理、そしてAPIキーをきちんと隠す方法です。これをやり遂げれば、どんな「ネット接続アプリ」でも作れる力が手に入ります。ニュースも、為替も、翻訳も、やることはまったく同じです。

#### 1. 無料の天気APIを申し込む

個人で練習するなら、OpenWeatherMapか、中国国内の「和風天気（QWeather）」がおすすめです。どちらも無料枠があって、登録すればすぐ使えます。OpenWeatherMapを例に見てみましょう。

1. アカウントを登録 → API keysページでキー（apikey）を1つ発行する。
2. 無料版で呼べるのはCurrent Weather（現在の天気）のAPIです。api.openweathermap.org/data/2.5/weather? q=beijing&appid=あなたのキー&units=metric。
3. まずブラウザで一度試して、返ってくるJSONがどんな形か見ておきましょう。どんなAPIにつなぐ前にも必ずやる「予習」です。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
落とし穴注意：キーをコードに直書きしない

{class="mt-1"}
APIキーはあなたの「財布のパスワード」みたいなものです。コードに書いてGitHubにプッシュすれば、数時間のうちにクローラーに収集されて勝手に使われます。正しいやり方は、local.properties（このファイルはgitignoreで無視されています）に置いておき、GradleのbuildConfig経由でコードに読み込むことです。「Android API Key 隠す ベストプラクティス」で検索して、その通りに直せば大丈夫です。
:::

#### 2. ネットワーク層：Retrofit＋JSON解析

まずAPIが返すJSONに合わせて「データモデル」を定義します。対応関係にないフィールドは、すべて無視してかまいません。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · データモデル + インターフェース</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"晴れ"}],"main":{"temp":26.5,"humidity":40},"name":"北京"}
data class WeatherResponse(
    val weather: List&lt;Weather&gt;,
    val main: Main,
    val name: String
)
data class Weather(val description: String)
data class Main(val temp: Double, val humidity: Int)

interface WeatherApi {
    @GET("data/2.5/weather")
    suspend fun getWeather(
        @Query("q") city: String,
        @Query("appid") key: String,
        @Query("units") metric: String = "metric",
        @Query("lang") lang: String = "zh_cn"
    ): WeatherResponse
}
```
:::

GsonはJSONをこれらのdata classへ自動で詰め込みます。フィールド名が一致していれば、魔法は自動的に起こります。

#### 3. 3つの画面状態：読み込み中／成功／失敗

ネット接続アプリの魂は「状態管理」にあります。ネットが遅い、つながらない、都市名を打ち間違えた……どの場合にも、画面はユーザーにきちんと伝える必要があります。sealed class（シールドクラス）で、美しく表現しましょう。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 画面の状態</span><span class="dots">···</span>
:::

```
sealed class UiState {
    object Loading : UiState()                    // くるくる回る
    data class Success(val data: WeatherResponse) : UiState()  // 成功
    data class Error(val message: String) : UiState()          // 失敗
}

// ViewModel側：
fun search(city: String) {
    viewModelScope.launch {
        _state.value = UiState.Loading
        _state.value = try {
            UiState.Success(api.getWeather(city))
        } catch (e: Exception) {
            UiState.Error("その都市が見つかりません。別の名前で試してみて？")
        }
    }
}

// 画面側：
when (val s = state) {
    is UiState.Loading -&gt; CircularProgressIndicator()   // 回る
    is UiState.Success -&gt; WeatherContent(s.data)        // 表示
    is UiState.Error -&gt; Text(s.message)                 // エラー表示
}
```
:::

このLoading/Success/Errorの三段構えは、ネット接続画面の「万能テンプレート」です。まず暗記してしまえば、この先のどんなネット接続アプリでも同じ形で書けます。

#### 4. 実戦の画面コード：天気を描き出す

状態が決まったら、画面はこうなります（要点の抜粋）。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 天気画面（核心部分）</span><span class="dots">···</span>
:::

```
@Composable
fun WeatherContent(data: WeatherResponse) {
    Column(
        Modifier.fillMaxSize().padding(24.dp),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text(data.name, fontSize = 28.sp, fontWeight = FontWeight.Bold)
        Text(
            "${data.main.temp}°C",
            fontSize = 72.sp,
            fontWeight = FontWeight.Light
        )
        Text(
            data.weather.firstOrNull()?.description ?: "不明",
            fontSize = 20.sp,
            color = Color.Gray
        )
        Spacer(Modifier.height(16.dp))
        Row {
            Text("💧 湿度 ${data.main.humidity}%")
            Spacer(Modifier.width(24.dp))
            Text("🌡️ 体感 ${data.main.temp}°C")
        }
    }
}
```
:::

学ぶ価値のある小さな工夫がいくつかあります。firstOrNull() は最初の要素を安全に取り出します（リストが空かもしれないので）。?: "不明" はいざというときの表示を用意しておく——安全に空を扱うという原則は、画面でも同じです。温度は 72.sp の大きい文字で存在感を出し、「細め」のウェイト（Light）で数字を上品に見せる。天気系アプリの定番レシピです。

#### 5. 画面と操作の細かい工夫

- 検索ボックス：上部にTextFieldを置き、都市名を入れて検索（キーボードのアクションを「検索」に設定して、Enterで検索できるように）。
- 天気カード：大きい文字の温度（26.5°）、天気の説明（晴れ）、湿度、都市名。
- お気に入りの都市：よく見る都市をDataStoreに保存して、次に開いたときに自動で検索——第六章の復習もかねて。
- 引っ張って更新：ComposeではPullToRefreshBox（Material 3が提供）を使います。操作の感触が一気に「プロっぽく」なります。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ワンポイント：画像で画面を生き生きと

{class="mt-1"}
天気の種類ごとに絵文字かアイコン（☀️🌧️❄️）を割り当て、when(description) で対応づけます。3行のコードで、画面のぬくもりが倍になります。サードパーティの天気アイコンライブラリを読み込んでもいいですが、練習の段階なら絵文字で十分です。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
やってみよう：天気アプリの検収チェックリスト

{class="mt-1"}
① 普通に検索して天気が出る。② ネットを切っても、アプリはエラーを上品に表示してクラッシュしない（機内モードで試す！）。③ 存在しない都市を入れても、やさしい表示が出る。④ 都市を2つお気に入りに入れて、アプリを再起動しても残っている。⑤ 画面を回しても状態が消えない。この5つを全部クリアして、このプロジェクトは卒業です。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章のまとめ

- まずブラウザでAPIを試し、JSONを読んでからコードを書く——「予習」で損をすることはない
- APIキーはlocal.propertiesに隠す。リポジトリには絶対入れない
- Retrofitインターフェース＋data class：フィールドが合えば、JSONは自動で解析される
- Loading/Success/Errorの三段構えは、ネット接続画面の万能テンプレート
- 切断、空の入力、存在しない都市——エラー処理はネット接続アプリの合格ライン
:::
