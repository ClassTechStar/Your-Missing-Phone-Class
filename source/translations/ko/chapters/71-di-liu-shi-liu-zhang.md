---
id: di-liu-shi-liu-zhang
num: 66
part: ios-kai-fa-pian
nav: 제66장: 프로젝트 2 — 날씨 조회 앱(네트워크 버전)
toc: default
kind: chapter
---

### 제66장: 프로젝트 2 — 날씨 조회 앱(네트워크 버전)

{class="chapter-intro mb-4"}
가계부가 '기본기 닦기'라면 날씨 앱은 '세상 구경'이에요. 인터넷과 직접 소통해야 하거든요. 이 프로젝트에서 무료 API 신청, JSON 파싱, '로딩 중/성공/실패' 세 가지 화면 상태 처리, 그리고 API 키를 안전하게 숨기는 방법을 배워요. 이걸 완성하면 어떤 '네트워크 앱'이든 만들 능력이 생겨요. 뉴스, 환율, 번역 앱도 똑같은 방식이에요.

#### 1. 무료 날씨 API 신청하기

개인 연습용이라면 OpenWeatherMap이나 중국의 허펑톈치(QWeather)를 추천해요. 둘 다 무료 할당량이 있고 가입하면 바로 쓸 수 있어요. OpenWeatherMap을 예로 들면:

1. 계정 가입 → API keys 페이지에서 Key(apikey) 하나 생성;
2. 무료 버전에서는 Current Weather API를 호출할 수 있어요: api.openweathermap.org/data/2.5/weather? q=beijing&appid=당신의Key&units=metric;
3. 브라우저에서 먼저 한 번 시도해 반환되는 JSON이 어떤 모습인지 확인하세요. 어떤 API든 연결하기 전에 반드시 하는 '예습'이에요.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
실수 방지 경고: 키는 절대 코드에 하드코딩하지 마세요

{class="mt-1"}
API Key는 당신의 '지갑 비밀번호'와 같아요. 코드에 넣어 GitHub에 올리는 순간 몇 시간 안에 크롤러가 훔쳐가 마음대로 써 버려요. iOS의 올바른 방법: Config.xcconfig(설정 파일, gitignore에 이미 무시됨)에 넣고 Info.plist를 통해 코드로 읽어들이세요. 'iOS xcconfig 키 관리'로 검색해서 따라 하면 돼요.
:::

#### 2. 네트워크 계층: URLSession + Codable

먼저 API가 반환하는 JSON에 맞춰 모델을 정의하고, 그다음 서비스를 작성해요:

::: div .code-block
:::inline div .code-head
<span>SWIFT · 데이터 모델 + 서비스</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"맑음"}],"main":{"temp":26.5,"humidity":40},"name":"베이징"}
struct WeatherResponse: Codable {
    let weather: [Weather]
    let main: Main
    let name: String
}
struct Weather: Codable { let description: String }
struct Main: Codable { let temp: Double; let humidity: Int }

struct WeatherService {
    let key: String   // xcconfig에서 읽어 들임

    func fetchWeather(city: String) async throws -> WeatherResponse {
        var comps = URLComponents(string: "https://api.openweathermap.org/data/2.5/weather")!
        comps.queryItems = [
            URLQueryItem(name: "q", value: city),
            URLQueryItem(name: "appid", value: key),
            URLQueryItem(name: "units", value: "metric"),
            URLQueryItem(name: "lang", value: "ko")
        ]
        let (data, _) = try await URLSession.shared.data(from: comps.url!)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}
```
:::

#### 3. 세 가지 화면 상태: 로딩 중 / 성공 / 실패

네트워크 앱의 핵심은 '상태 관리'에 있어요. 네트워크가 느리거나, 연결이 끊기거나, 도시 이름을 잘못 입력하는 등 모든 상황에서 화면이 사용자에게 상황을 알려 줘야 해요. 열거형 + switch로 깔끔하게 표현해 보세요:

::: div .code-block
:::inline div .code-head
<span>SWIFT · 화면 상태</span><span class="dots">···</span>
:::

```
enum LoadState {
    case loading                  // 로딩 표시
    case success(WeatherResponse) // 성공
    case error(String)            // 실패
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
            state = .error("그 도시를 찾을 수 없어요. 다른 이름으로 시도해 볼까요?")
        }
    }
}

// 화면 안에서:
switch vm.state {
case .loading: ProgressView("불러오는 중…")
case .success(let d): WeatherContent(data: d)
case .error(let msg): Text(msg).foregroundColor(.secondary)
}
```
:::

이 loading/success/error 3단 방식은 네트워크 화면의 '만능 템플릿'이에요. 먼저 외워 두고, 앞으로 만드는 모든 네트워크 앱에 그대로 응용하세요.

#### 4. 실전 화면 코드: 날씨를 화면에 그리기

::: div .code-block
:::inline div .code-head
<span>SWIFT · 날씨 화면(핵심 발췌)</span><span class="dots">···</span>
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
            Text(data.weather.first?.description ?? "알 수 없음")
                .font(.title3)
                .foregroundColor(.secondary)
            HStack(spacing: 24) {
                Label("습도 \(data.main.humidity)%", systemImage: "humidity")
                Label("체감 \(Int(data.main.temp))°C", systemImage: "thermometer")
            }
        }
        .padding()
    }
}
```
:::

배울 만한 작은 디테일들: first?는 첫 번째 요소를 안전하게 꺼내요(리스트가 비어 있을 수 있어요), '알 수 없음' ?? 연산은 기본 문구를 줘요. 온도 숫자에 76번 얇은 글꼴 두께를 쓰는 건 날씨 앱의 클래식한 조합이에요. Label은 '아이콘+텍스트' 공식 컴포넌트로 HStack을 손으로 조립하는 것보다 더 규범적이에요.

#### 5. 인터랙션 디테일과 즐겨찾는 도시

- 검색창: 상단에 .searchable 한정자를 쓰면 시스템 기본 검색 인터랙션이 제공되고, 제출 시 vm.search를 호출해요;
- 즐겨찾는 도시: 자주 보는 도시를 UserDefaults에 저장하면 다음에 열 때 자동으로 조회해요;
- 당겨서 새로 고침: .refreshable { await vm.search(...) } 한 줄로 끝;
- 날씨 아이콘: Image(systemName:)로 설명에 맞춰 매핑하면(sun.max / cloud.rain / snowflake) 화면이 바로 살아나요.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
팁: 중국어 도시 이름의 '함정'

{class="mt-1"}
OpenWeatherMap은 중국어 도시 이름 지원이 좋지 않아 '베이징'으로 검색하면 결과가 없는데 'beijing'은 정상이에요. 제품화하려면 '도시 이름 → 영어/좌표' 매핑 테이블을 내장하거나 중국 날씨 서비스를 연결하는 방법이 있어요. 연습 단계에서는 병음/영어 도시 이름만 지원해도 충분하니 억지로 붙잡고 늘어지지 마세요.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
직접 해 보기: 날씨 앱 검수 체크리스트

#### 6. 네트워크 요청 디버깅: 출력, 패킷 캡처, 느린 네트워크 시뮬레이션

네트워크 앱에 문제가 생기면 십중팔구 '요청을 잘못 보냈거나' '응답을 잘못 파싱한' 경우예요. 세 가지 디버깅 수단:

1. 원본 데이터 출력: String(data: data, encoding: .utf8)을 출력해 원본 JSON을 확인하세요. 필드 이름과 타입이 한눈에 보여 추측보다 열 배 빨라요;
2. 패킷 캡처 도구: Mac의 무료 Proxyman이나 오픈소스 Charles는 앱의 모든 요청과 응답을 가로채 X선처럼 네트워크 계층을 들여다볼 수 있게 해 줘요;
3. 약한 네트워크 시뮬레이션: 시뮬레이터 메뉴 Features → Network Link Conditioner(개발자 사이트에서 도구를 내려받아야 해요)로 3G, 높은 지연 시간 등을 흉내 낼 수 있어요. '빙글빙글 도는 시간이 한없이 긴' 경험 문제를 찾아낼 수 있어요.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
팁: 요청이 ATS를 통과하지 못했나요?

{class="mt-1"}
요청을 보내자마자 'App Transport Security' 오류가 뜬다면 십중팔구 http:// 평문 주소를 썼기 때문이에요. 정식 API는 반드시 HTTPS여야 하고, 로컬 디버깅 중이라면 임시로 예외를 열 수 있어요(Info.plist에 NSAllowsLocalNetworking 추가). 출시 전에는 깔끔히 지우는 것을 잊지 마세요.
:::

{class="mt-1"}
① 정상적으로 검색해 날씨가 나오는가; ② 네트워크를 끊었을 때 앱이 우아하게 오류를 알리고 크래시하지 않는가(시뮬레이터에서 Mac의 네트워크를 꺼서 테스트!); ③ 존재하지 않는 도시를 입력했을 때 친절한 안내가 나오는가; ④ 도시 두 개를 즐겨찾기하고 앱을 다시 실행해도 남아 있는가; ⑤ 다크 모드에서 화면이 눈부시지 않은가. 다섯 항목을 모두 통과해야 이 프로젝트는 졸업이에요.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
이번 장 정리

- 먼저 브라우저로 API를 시험하고 JSON을 이해한 뒤 코드를 작성 — '예습'은 손해 볼 일이 없어요
- API Key는 xcconfig에 숨기고 절대 코드 저장소에 넣지 않기
- Codable 모델 + URLSession async/await: 필드만 맞추면 JSON이 자동으로 파싱돼요
- loading/success/error 3단 상태 관리는 네트워크 화면의 만능 해법
- 끊긴 네트워크, 빈 입력, 존재하지 않는 도시 — 오류 처리가 네트워크 앱의 합격선
:::
