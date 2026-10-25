---
id: di-liu-shi-ba-zhang
num: 68
part: ios-kai-fa-pian
nav: 제68장: 고급 성장 경로 — 권한, 알림과 최신 아키텍처
toc: default
kind: chapter
---

### 제68장: 심화 여정 — 권한, 알림, 현대 아키텍처

{class="chapter-intro mb-4"}
앱을 만들 수 있다는 건 시작일 뿐이에요. 이번 장은 '할 줄 안다'에서 '잘한다'로 넘어가야 할 몇 개의 고개를 다뤄요. 권한을 우아하게 요청하는 법, 알림을 미움받지 않고 보내는 법, 아키텍처를 한 단계 더 끌어올리는 법, 그리고 2026년에 AI와 짝이 되어 iOS 코드를 쓰는 법이에요. 하나하나 모두 실제 프로젝트에서 곧 마주치는 내용이에요.

#### 1. 권한: 먼저 노크하고 들어가기

카메라, 위치, 연락처, 알림…… 이런 '민감한 영역'은 iOS가 앱이 사용하는 시점에 사용자에게 팝업으로 허용을 요청하도록 정하고 있어요. 규칙은 '선언 + 요청 + 우아한 저하' 세 단계예요:

::: div .code-block
:::inline div .code-head
<span>SWIFT · 권한 요청(위치 예시)</span><span class="dots">···</span>
:::

```
// 1. Info.plist에 용도 문구 선언(선언 없으면 바로 크래시!)
// Privacy - Location When In Use Usage Description: "사용자 도시의 날씨를 조회하는 데 사용"

// 2. 쓸 때 요청
import CoreLocation

@Observable
class LocationModel {
    private let manager = CLLocationManager()

    func request() {
        switch manager.authorizationStatus {
        case .notDetermined: manager.requestWhenInUseAuthorization()
        case .denied, .restricted: /* 설정에서 켜도록 안내 */
        default: /* 이미 승인됨, 진행 */
        }
    }
}

// 3. 거부되면 우아하게 저하: 안내 표시 + 설정으로 이동
// UIApplication.shared.open(URL(string: UIApplication.openSettingsURLString)!)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
주의: iOS 권한의 '한 번뿐' 특성

{class="mt-1"}
iOS 권한 팝업은 한 번만 떠요. 사용자가 거부하면 다시는 뜨지 않아요. 그래서 요청 시점은 '사용자가 막 쓰려는 순간'으로 골라야 하고(앱이 시작하자마자 여러 개 띄우는 게 아니라), 문구에는 용도를 설명해야 해요. 거부당한 뒤의 화면 안내('설정에서 위치를 켜세요')는 기본이에요. 사용자를 막다른 길에 가두지 마세요.
:::

#### 2. 알림: 알맞은 시간에 유용한 말 하기

알림은 앱이 사용자에게 닿는 통로이자 가장 쉽게 '차단'당하는 기능이기도 해요. iOS는 UserNotifications 프레임워크를 쓰고, 알림 발송의 세 가지 원칙: 유용한 것만 보내기, 사용자가 끌 수 있게 하기, 한밤에 괴롭히지 않기. 기본 사용법:

::: div .code-block
:::inline div .code-head
<span>SWIFT · 로컬 알림</span><span class="dots">···</span>
:::

```
import UserNotifications

// 1. 알림 권한 요청(한 번 팝업)
UNUserNotificationCenter.current()
    .requestAuthorization(options: [.alert, .sound, .badge]) { granted, _ in
        print(granted ? "승인됨" : "거부됨")
    }

// 2. "매일 20:00 가계부 알림" 예약
func scheduleDailyReminder() {
    let content = UNMutableNotificationContent()
    content.title = "가계부 알림"
    content.body = "오늘 가계부 기록이 아직 없어요"
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

주의: iOS의 알림 권한 역시 '한 번만 떠요'. 게다가 사용자는 언제든 시스템 설정에서 끌 수 있어요. 그래서 알림 내용의 가치가 매우 중요하고, 무분별하게 한 번만 보내도 사용자를 영원히 잃을 수 있어요.

#### 3. 아키텍처 심화: MVVM 깊이 들어가기와 테스트 가능성

65장에서 MVVM을 썼는데, 여기서 심화 포인트 세 가지를 더해요:

- 프로토콜 추상화: ViewModel이 구체 클래스가 아니라 프로토콜(protocol)에 의존하게 해요. 테스트할 때 '가짜 데이터 소스'를 주입할 수 있어서 테스트 가능성의 초석이 돼요;
- 단일 책임: 하나의 ViewModel은 한 가지만 담당해요(가계부 ViewModel은 날씨를 신경 쓰지 않아요). 기능이 많아지면 분리해요;
- 과설계 금지: 혼자 하는 작은 프로젝트라면 '@Observable 클래스 + 프로토콜 추상화'면 충분해요. VIPER, Clean Architecture 같은 무거운 아키텍처는 팀과 복잡도가 찾아왔을 때 다뤄도 늦지 않아요. 도구는 목표를 위해 존재하지 뽐내려고 있는 게 아니에요.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
팁: SwiftUI의 '생태계 혜택'

{class="mt-1"}
iOS 생태계에는 '여기서만 가능한' 심화 기능이 두 가지 더 있어요. 위젯(WidgetKit)은 앱을 열지 않고도 정보를 볼 수 있게 해 주고(가계부의 '이번 달 지출'을 홈 화면에), 단축어(App Intents)는 사용자가 Siri나 자동화로 당신의 기능을 호출하게 해 줘요. 둘 다 공식 프레임워크가 있어 진입 비용이 높지 않지만 사용자 경험에 큰 힘을 보태 줘요. 심화 여정에서 우선적으로 열어 볼 가치가 있어요.
:::

#### 4. 2026년의 새로운 방식: AI가 돕는 iOS 개발

2026년, AI는 이미 애플 개발 과정에 깊이 들어와 있어요. 속도를 내고 싶다면 이 조합이 아주 성숙해 있어요:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">작업</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">AI가 돕는 방법</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">당신의 역할</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">코드 작성</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode 내장 코드 자동 완성 + 서드파티 AI 플러그인 생성</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">요구사항을 명확히 설명하고 산출물 검토</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">자료 찾기</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">공식 문서와 오류 메시지를 AI에 던져 해석</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">핵심 결론은 공식 문서에서 다시 확인</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">테스트 작성</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI가 '정상/경계/예외' 세 유형으로 XCTest 케이스를 생성하도록 하기</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">케이스가 업무 의미에 맞는지 확인</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">버그 수정</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">크래시 로그 + 관련 코드를 붙여 넣고 AI가 위치를 찾아 수정</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">변경 내용을 이해하고 테스트로 검증</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
AI 보조 iOS 개발의 네 가지 장면

구체적인 방법론 — AI에 지시를 내리는 법, 검수하는 법, 함정 피하는 법 — 은 이 책의 제7편 〈AI 코딩 실전편〉(37~47장)에 11개 장으로 완전히 담겨 있으니 꼭 함께 읽기를 권해요. Swift 문법은 이번 편에, AI 협업 노하우는 제7편에 맡겨요.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
직접 해 보기: 가계부에 '3종 세트' 더하기

#### 5. Swift 동시성 핵심: @MainActor와 Task

Swift 6의 동시성 체계에는 초보자가 꼭 알아야 할 규칙이 두 가지 있어요:

- 화면은 메인 스레드에서만 갱신: SwiftUI 뷰는 기본적으로 @MainActor예요. 네트워크 콜백은 메인 스레드로 돌아온 뒤 상태를 바꿔야 해요(await MainActor.run { ... } 또는 ViewModel에 @MainActor 표시);
- 비동기 작업은 Task로 관리: .task { } 한정자는 뷰가 나타나면 자동으로 시작되고 사라지면 자동으로 취소돼요. SwiftUI에서 비동기 작업을 시작하는 표준 방식이에요. body 안에 Task를 아무렇게나 던져 두고 방치하지 마세요.

::: div .code-block
:::inline div .code-head
<span>SWIFT · 표준 비동기 패턴</span><span class="dots">···</span>
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
        .task {                       // 나타나면 시작, 사라지면 취소
            await vm.search(city: "베이징")
        }
    }
}
```
:::

이 두 규칙 뒤에는 Swift 6의 '데이터 경쟁 안전성' 설계가 있어요. 잘못 쓴 순간 컴파일러가 바로 오류를 내 주는 거지, 앱이 크래시된 뒤에야 알게 되는 게 아니에요. 컴파일러의 오류 메시지는 트집 잡기가 아니라 대신 총알을 막아 주는 거예요.

{class="mt-1"}
① 가계부에 '매일 20:00 가계부 알림' 추가(알림 권한 + 로컬 알림); ② ViewModel의 데이터 소스를 프로토콜 추상화로 바꾸고 가짜 데이터를 주입하는 단위 테스트 하나 작성; ③ '이번 달 지출' 홈 화면 위젯 추가. 3종 세트를 끝내면 프로젝트가 '정규군'다운 모습을 갖추게 돼요.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
이번 장 정리

- 권한 3단계: Info.plist 선언(빠지면 반드시 크래시), 사용할 때 요청, 거부당하면 설정으로 안내
- iOS 권한 팝업은 한 번만: 시점은 '막 쓰려는 순간'으로 고르고 문구에는 용도를 분명히
- 알림 3원칙: 유용한 것만, 끌 수 있게, 괴롭히지 않기; UserNotifications 프레임워크
- MVVM 심화: 프로토콜 추상화(테스트 가능), 단일 책임, 과설계 금지
- 생태계 혜택: WidgetKit 위젯 + App Intents 단축어
- AI 보조 4장면: 코드 작성, 자료 찾기, 테스트 작성, 버그 수정; 방법론은 제7편(37~47장) 참조
:::
