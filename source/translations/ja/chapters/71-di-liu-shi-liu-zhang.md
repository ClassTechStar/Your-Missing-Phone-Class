---
id: di-liu-shi-liu-zhang
num: 66
part: ios-kai-fa-pian
nav: 第六十六章：プロジェクト2——天気チェックアプリ（ネットワーク版）
toc: default
kind: chapter
---

### 第六十六章：プロジェクト2——天気チェックアプリ（ネットワーク版）

{class="chapter-intro mb-4"}
家計簿が「内功の鍛錬」なら、天気アプリは「世間を知る」——インターネットと付き合うプロジェクトです。このプロジェクトで学ぶのは：無料APIの申し込み、JSONの解析、「読み込み中／成功／失敗」の3つの画面状態の扱い、そしてAPIキーの隠し方。完成すれば、どんな「ネット接続アプリ」でも作れる力が身につきます——ニュースも為替も翻訳も、やり方はまったく同じです。

#### 1. 無料の天気APIを申し込む

個人の練習なら、OpenWeatherMapか中国国内のQWeatherがおすすめ——どちらも無料枠があって、登録すればすぐ使えます。OpenWeatherMapを例にすると：

1. アカウント登録 → API keysページでキー（apikey）を1つ生成します。
2. 無料版で呼び出せるのはCurrent Weather API：api.openweathermap.org/data/2.5/weather? q=beijing&appid=あなたのキー&units=metric。
3. まずブラウザで1回試して、返ってくるJSONがどんな形か見てみましょう——どんなAPIをつなぐ前にもやるべき「予習」です。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
落とし穴注意：キーは絶対にコードに直書きしない

{class="mt-1"}
APIキーは、あなたの「おサイフの暗証番号」です。コードに書いてGitHubに上げた瞬間、数時間でクローラーに収集されて悪用されます。iOSでの正しいやり方：Config.xcconfig（設定ファイル。gitignoreで除外済み）に置き、Info.plist経由でコードに読み込みます。「iOS xcconfig キー管理」で検索して、手順どおりに直せばOKです。
:::

#### 2. ネットワーク層：URLSession＋Codable

まずAPIが返すJSONに合わせてモデルを定義してから、サービスを書きます：

::: div .code-block
:::inline div .code-head
<span>SWIFT · データモデル + サービス</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"晴れ"}],"main":{"temp":26.5,"humidity":40},"name":"北京"}
struct WeatherResponse: Codable {
    let weather: [Weather]
    let main: Main
    let name: String
}
struct Weather: Codable { let description: String }
struct Main: Codable { let temp: Double; let humidity: Int }

struct WeatherService {
    let key: String   // xcconfigから読み込む

    func fetchWeather(city: String) async throws -> WeatherResponse {
        var comps = URLComponents(string: "https://api.openweathermap.org/data/2.5/weather")!
        comps.queryItems = [
            URLQueryItem(name: "q", value: city),
            URLQueryItem(name: "appid", value: key),
            URLQueryItem(name: "units", value: "metric"),
            URLQueryItem(name: "lang", value: "zh_cn")
        ]
        let (data, _) = try await URLSession.shared.data(from: comps.url!)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}
```
:::

#### 3. 3つの画面状態：読み込み中／成功／失敗

ネット接続アプリの魂は「状態管理」です。ネットが遅い、つながらない、都市名を打ち間違えた……どの場合も、画面はユーザーにきちんと説明する必要があります。enum＋switchでスマートに表現しましょう：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 画面の状態</span><span class="dots">···</span>
:::

```
enum LoadState {
    case loading                  // くるくる回る
    case success(WeatherResponse) // 成功
    case error(String)            // 失敗
}

@Observable
class WeatherViewModel {
    var state: LoadState = .loading
    private let service = WeatherService(key: Config.apiKey)

    func search(city: String) async {
        state = .loading
        do {
            let data = try await service.fetchWeather(city: city)
            state = .success(data)
        } catch {
            state = .error("その都市が見つかりません。別の名前で試してみて？")
        }
    }
}

// 画面側：
switch vm.state {
case .loading: ProgressView("読み込み中…")
case .success(let d): WeatherContent(data: d)
case .error(let msg): Text(msg).foregroundColor(.secondary)
}
```
:::

このloading/success/errorの3段構えは、ネット接続画面の「万能テンプレート」です。まず丸暗記してしまえば、この先どんなネット接続アプリも同じ型で作れます。

#### 4. 実戦の画面コード：天気を描き出す

::: div .code-block
:::inline div .code-head
<span>SWIFT · 天気画面（核心部分）</span><span class="dots">···</span>
:::

```
struct WeatherContent: View {
    let data: WeatherResponse

    var body: some View {
        VStack(spacing: 12) {
            Text(data.name)
                .font(.title.bold())
            Text("\(Int(data.main.temp))°C")
                .font(.system(size: 76, weight: .thin))
            Text(data.weather.first?.description ?? "不明")
                .font(.title3)
                .foregroundColor(.secondary)
            HStack(spacing: 24) {
                Label("湿度 \(data.main.humidity)%", systemImage: "humidity")
                Label("体感 \(Int(data.main.temp))°C", systemImage: "thermometer")
            }
        }
        .padding()
    }
}
```
:::

学ぶ価値のある小さなディテールがいくつか：first?は最初の要素を安全に取り出し（リストが空かもしれないので）、?? "不明"がフォールバックの文言。細いウェイトの76ポイントの温度数字は、天気系アプリの定番レシピ。Labelは「アイコン＋文字」の公式コンポーネントで、HStackを手で組み合わせるより規範的です。

#### 5. 操作のディテールとお気に入り都市

- 検索欄：上部に.searchableモディファイアを付けると、システム標準の検索操作になって、確定時にvm.searchを呼び出せます。
- お気に入り都市：よく見る都市をUserDefaultsに保存すれば、次に開いたとき自動で検索します。
- 下スワイプ更新：.refreshable { await vm.search(...) }の1行で完成。
- 天気アイコン：Image(systemName:)で説明に合わせて対応付け（sun.max / cloud.rain / snowflake）。画面が一気に生き生きします。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ワンポイント：中国語の都市名の「クセ」

{class="mt-1"}
OpenWeatherMapは中国語の都市名への対応がいまひとつで、「北京」と検索すると結果が出ないのに、"beijing"なら正常です。製品化するなら「都市名 → 英語／座標」の対応表を内蔵するか、中国国内の天気サービスにつなぐのが定石。練習段階では、ピンイン／英語の都市名に対応しておけば十分。ガチンコ勝負をしないことです。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
やってみよう：天気アプリの検収チェックリスト

#### 6. ネットワーク通信のデバッグ：出力、パケットキャプチャ、低速ネットの再現

ネット接続アプリで問題が起きたら、十中八九「リクエストが正しく送れていない」か「レスポンスが正しく解析できていない」です。デバッグの手段は3つ：

1. 生データを出力する：String(data: data, encoding: .utf8) を印字して生の JSON を確認——フィールド名も型もひと目でわかり、当てずっぽうより10倍速いです。
2. パケットキャプチャツール：Mac の無料の Proxyman やオープンソースの Charles なら、App のすべてのリクエストとレスポンスを傍受して、X 線のようにネットワーク層をはっきり見せてくれます。
3. 低速回線の再現：シミュレータのメニュー Features → Network Link Conditioner（開発者サイトからツールをダウンロードする必要あり）を使うと、3G や高遅延をエミュレートでき、「ぐるぐる回りっぱなし」といった体験の問題を洗い出せます。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ワンポイント：リクエストが ATS に阻まれたら？

{class="mt-1"}
リクエストを出したとたん「App Transport Security」エラーが出るなら、十中八九は http:// の平文アドレスが原因です。正式な API は必ず HTTPS に。ローカルデバッグ中だけ例外的に許可し（Info.plist に NSAllowsLocalNetworking を追加）、リリース前には忘れず解除しましょう。
:::

{class="mt-1"}
① 普通に天気を検索できる。② ネットを切っても App はクラッシュせず、やさしくエラーを出す（シミュレータで Mac のネットワークを切って試す！）。③ 存在しない都市を入れると親切な表示が出る。④ 都市を2つお気に入りに入れても、App を再起動しても残っている。⑤ ダークモードでも画面がまぶしくない。この5つがすべて合格してはじめて、このプロジェクトは卒業です。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
この章のまとめ

- コードを書く前にブラウザで API を試し、JSON を理解する——「予習」で損をすることはありません
- API キーは xcconfig にしまい、決してリポジトリに入れない
- Codable モデル + URLSession の async/await：フィールドが合っていれば JSON は自動でパース
- loading／success／error の3段階ステートは、ネットワーク系画面の万能薬
- 通信断・空入力・存在しない都市——エラー処理こそネットワーク App の合格ライン
:::
