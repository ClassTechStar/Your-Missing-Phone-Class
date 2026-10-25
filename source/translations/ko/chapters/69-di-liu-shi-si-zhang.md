---
id: di-liu-shi-si-zhang
num: 64
part: ios-kai-fa-pian
nav: 제64장: 데이터 저장과 네트워크 요청
toc: default
kind: chapter
---

### 제64장: 데이터 저장과 네트워크 요청

{class="chapter-intro mb-4"}
'보기만' 할 수 있는 앱은 죽은 앱이에요. 데이터를 저장하고 네트워크에 연결할 수 있는 앱이 살아 있는 앱이죠. 이 장에서는 iOS 데이터 계층의 '3종 세트'를 만나요. UserDefaults(작은 설정 저장), SwiftData(구조화된 데이터 저장), URLSession(서버와 대화)이요. 여기에 JSON을 해석하는 Codable과 현대적인 async/await까지 더해요. 이 장을 마치면 사용자의 습관을 기억하고 내용을 실시간으로 업데이트하는 진짜 앱을 쓸 수 있어요.

#### 1. 저장 방식 고르기: 먼저 이 표를 보세요

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">방식</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">무엇을 저장하기에 적합한가</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">특징</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">이 책에서 쓰이는 곳</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">흩어진 설정(스위치, 취향)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">키-값 쌍, 단순하고 직관적</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">제65장 설정, 제66장 즐겨찾는 도시</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">구조화된 데이터(가계부 항목, 기록)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">공식 데이터베이스 래퍼, @Model 한 줄 선언</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">제65장 가계부 기록</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">(저장하지 않고 네트워크로 가져옴) 서버 데이터</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">시스템 내장 네트워크 프레임워크, 서드파티 의존성 없음</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">제66장 날씨 데이터</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
데이터 3종 세트의 역할 분담

암기 문구 하나: '작은 설정은 UserDefaults로, 한꺼번에 몰리는 데이터는 SwiftData로, 밖의 데이터는 URLSession으로'. 오래된 튜토리얼의 Core Data는 여전히 쓸 수 있고(SwiftData가 그 현대 버전이에요), 손으로 쓰는 SQLite는 거의 만질 일이 없어요. 바로 새것을 배우세요. 옛길로 가지 마세요.

#### 2. UserDefaults: 작은 설정 저장하기

::: div .code-block
:::inline div .code-head
<span>SWIFT · UserDefaults 예시</span><span class="dots">···</span>
:::

```
// 쓰기: 값 저장
UserDefaults.standard.set(true, forKey: "isDarkMode")
UserDefaults.standard.set("베이징", forKey: "favoriteCity")

// 읽기: 꺼내 오기(없으면 기본값 반환)
let isDark = UserDefaults.standard.bool(forKey: "isDarkMode")
let city = UserDefaults.standard.string(forKey: "favoriteCity") ?? "베이징"

// 삭제: 키 제거
UserDefaults.standard.removeObject(forKey: "isDarkMode")
```
:::

UserDefaults는 흩어진 작은 설정에만 적합하다는 점에 유의하세요. 수십에서 수백 건의 기록은 SwiftData에 맡기세요. UserDefaults를 데이터베이스처럼 쓰면 시작이 느려지고 조회도 불편해요.

#### 3. SwiftData: 데이터에 '진짜 집' 마련해 주기

SwiftData는 iOS 17부터의 공식 데이터베이스 방식으로, '테이블 만들기, 추가·삭제·수정·조회'를 극한까지 단순화했어요. @Model 주석 하나면 데이터 클래스가 데이터베이스 테이블이 돼요.

::: div .code-block
:::inline div .code-head
<span>SWIFT · SwiftData 예시</span><span class="dots">···</span>
:::

```
import SwiftData

// 1. @Model: 이 클래스는 자동으로 "테이블"이 돼요
@Model
class Record {
    var amount: Double
    var category: String
    var note: String
    var date: Date

    init(amount: Double, category: String, note: String, date: Date) {
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date
    }
}

// 2. 앱 진입점에 컨테이너 연결
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: Record.self)   // 데이터베이스 준비 완료
    }
}

// 3. 뷰에서는 @Query로 읽고 @Environment로 기록
struct RecordListView: View {
    @Query(sort: \Record.date, order: .reverse) var records: [Record]
    @Environment(\.modelContext) private var context

    var body: some View {
        List(records) { r in
            Text("\(r.category) \(r.amount)위안")
        }
    }

    func add(amount: Double, category: String) {
        let r = Record(amount: amount, category: category, note: "", date: Date())
        context.insert(r)     // 저장
        try? context.save()   // 디스크에 기록
    }
}
```
:::

이 '@Model + modelContainer + @Query' 템플릿은 그대로 여러분의 어떤 프로젝트에도 옮겨 쓸 수 있어요. 필드 이름만 바꾸면 돼요. 데이터가 바뀌면 @Query가 화면을 자동으로 새로 고쳐요. 이 얼마나 묘한 일인가요.

#### 4. Codable: JSON '통역'하기

서버의 데이터는 대부분 JSON 텍스트예요. Swift의 Codable 프로토콜은 'JSON ⇄ 구조체' 변환을 자동으로 일으켜요. 필드 이름만 맞으면 마법이 발동하죠.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Codable로 JSON 해석</span><span class="dots">···</span>
:::

```
// JSON: {"name":"베이징","main":{"temp":26.5},"weather":[{"description":"맑음"}]}
struct WeatherResponse: Codable {
    let name: String
    let main: Main
    let weather: [Weather]
}
struct Main: Codable { let temp: Double }
struct Weather: Codable { let description: String }

// JSON 문자열 → 구조체
let decoder = JSONDecoder()
let data = jsonString.data(using: .utf8)!
let result = try decoder.decode(WeatherResponse.self, from: data)
print(result.weather[0].description)   // "맑음"
```
:::

철칙: 실제로 돌아오는 JSON을 먼저 보고 필드를 정의하세요. '파싱 실패' 버그의 상당수는 필드 이름 오타나 타입 착각(서버는 "26.5" 문자열을 보냈는데 여러분이 Double로 선언)에서 나와요. 원본 JSON을 프린트해 대조하면 10초 만에 원인을 찾아요.

#### 5. URLSession + async/await: 서버와 말하기

iOS 네트워킹은 시스템 내장 URLSession을 쓰고, Swift의 async/await(비동기 함수)와 함께하면 '네트워크 기다리기'가 '택배 기다리기'처럼 자연스러워요.

::: div .code-block
:::inline div .code-head
<span>SWIFT · URLSession + async/await</span><span class="dots">···</span>
:::

```
struct WeatherService {
    // 비동기 함수: async는 "잠깐 기다릴게요", throws는 "실패할 수도 있어요" 표시
    func fetchWeather(city: String) async throws -> WeatherResponse {
        let url = URL(string:
            "https://api.example.com/weather?city=\(city)")!
        let (data, _) = try await URLSession.shared.data(from: url)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}

// 호출부(.task 안에서):
.task {
    do {
        let weather = try await service.fetchWeather(city: "베이징")
        // 화면 업데이트……
    } catch {
        print("오류가 발생했어요: \(error)")
    }
}
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
함정 주의: 네트워크 철칙 두 가지

{class="mt-1"}
① 네트워킹은 반드시 async/await로 하고 절대 메인 스레드를 막지 마세요. 화면이 멈추는 건 크래시급 경험이에요. Swift의 구조화된 동시성이 이를 자연스럽게 해 주지만 try await와 do/catch를 잊지 마세요. ② ATS는 기본적으로 평문 HTTP를 금지해요. iOS는 HTTPS를 요구하죠. 로컬 http:// 서비스를 테스트할 때는 Info.plist에 임시 예외(NSAppTransportSecurity)를 열어야 하지만, 정식 제품은 반드시 전부 HTTPS로 가야 해요. 심사에서도 이 부분을 봐요.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
직접 해 보기: '오늘의 한 문장' 미니 앱 만들기

#### 6. 네트워크 오류도 '등급을 나눠요': 모든 오류를 사용자에게 던지지 마세요

끊긴 네트워크, 시간 초과, 404, 서버 500… 오류에 따라 사용자가 봐야 할 말이 달라요.

::: div .code-block
:::inline div .code-head
<span>SWIFT · 오류 등급별 처리</span><span class="dots">···</span>
:::

```
func friendlyMessage(_ error: Error) -> String {
    if let urlError = error as? URLError {
        switch urlError.code {
        case .notConnectedToInternet: return "네트워크가 끊겼어요. 연결을 확인해 볼까요?"
        case .timedOut:               return "요청 시간 초과. 잠시 후 다시 시도할까요?"
        case .cannotFindHost:         return "서버를 찾을 수 없어요"
        default:                      return "네트워크 문제: \(urlError.code)"
        }
    }
    if let d = error as? DecodingError {
        return "데이터 형식이 달라요(인터페이스가 바뀌었을 수 있어요)"
    }
    return "오류가 발생했어요: \(error.localizedDescription)"
}
```
:::

사용자에게는 '사람 말'을, 로그에는 '원문'을 남기세요(error 전체를 print). error.localizedDescription의 영어 점서를 사용자에게 그대로 던지지 마세요. 제품의 완성도는 바로 이런 디테일에 숨어 있어요.

{class="mt-1"}
무료 명언 API(hitokoto 같은 것)를 하나 찾아 URLSession + async/await로 '오늘의 한 문장'을 가져와 화면 중앙에 표시하고, '다른 문장' 버튼을 하나 추가하세요. 마음에 드는 문장은 SwiftData로 '즐겨찾기'에 저장하고요. 이 연습은 UserDefaults/SwiftData/Codable/URLSession을 모두 한 번씩 쓰게 해 줘요. 이것을 끝내면 제7, 8편은 식은 죽 먹기예요.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
이 장 정리

- 암기 문구: 작은 설정은 UserDefaults로, 대량 데이터는 SwiftData로, 밖의 데이터는 URLSession으로
- SwiftData 3수: @Model로 테이블 선언, modelContainer로 컨테이너 연결, @Query로 읽기 + context.insert로 쓰기
- Codable이 JSON을 자동 '통역': 필드 이름만 맞으면 마법이 발동
- URLSession + async/await: 네트워킹은 택배 기다리듯; do/catch로 실패 처리
- 두 가지 철칙: 메인 스레드를 막지 않기; 정식 제품은 반드시 HTTPS(ATS)
:::
