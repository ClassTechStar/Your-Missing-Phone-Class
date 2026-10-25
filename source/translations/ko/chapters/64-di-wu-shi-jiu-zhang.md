---
id: di-wu-shi-jiu-zhang
num: 59
part: ios-kai-fa-pian
nav: 제59장: iOS 이해하기 — 애플 생태계와 개발 생태계
toc: default
kind: chapter
---

### 제59장: iOS 알아보기 — 애플 생태계와 개발 생태계

{class="chapter-intro mb-4"}
이 결정을 내린 것을 축하해요. '아이폰을 쓰는 사람'에서 '아이폰용 앱을 만드는 사람'이 되는 거니까요. 손을 쓰기 전에 지도를 먼저 펼쳐 볼게요. iOS는 어디에서 왔을까요? 애플의 '울타리 쳐진 정원'은 개발자에게 어떤 의미일까요? 한 개의 앱이 여러분 손가락이 키보드를 두드리는 순간부터 사용자의 휴대폰에 닿기까지, 그 사이에서는 무슨 일이 벌어질까요?

#### 1. iOS의 내력: 한 대의 휴대폰이 한 산업을 바꾸다

2007년 1월, 잡스는 발표 행사에서 첫 세대 아이폰을 꺼내 보였어요. 당시에는 서드파티 앱도 지원하지 않았어요. 2008년에 이르러서야 애플이 App Store와 iPhone SDK를 내놓으며 전 세계 개발자가 아이폰용 소프트웨어를 만들도록 허용했죠. 그 순간 '앱 경제'가 탄생했어요. 오늘날 App Store에는 수백만 개의 앱이 있고, 개발자에게 누적으로 지급된 수익 배분은 수천억 달러를 넘었어요.

시스템 자체도 진화하고 있어요. 처음에는 iPhone OS라고 불렀다가 2010년에 iOS로 이름을 바꿨고, 버전 번호는 iOS 17(2023)까지 이어졌어요. 그러다 2025년에 애플은 이름을 연도를 따라 붙이는 방식으로 바꿨어요. iOS 26이 2025년에 발표됐고, 2026년 8월 현재 버전은 iOS 27이에요. 이름은 바뀌어도 한 가지는 변한 적이 없어요. iOS 사용자의 유료 결제 습관과 소프트웨어 품질 평판은 모바일 생태계에서 공인된 최고예요. 같은 앱이라도 iOS 쪽 수익이 안드로이드 쪽보다 눈에 띄게 높은 경우가 많죠.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">시점</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">연도</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">개발자에게 중요한 일</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">App Store 출시</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2008</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">서드파티 개발 생태계 문 열림</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift 발표</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2014</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">현대 iOS 개발 언어 등장</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI 발표</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2019</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">선언형 UI 프레임워크, 이 책의 메인 줄기</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">iOS 26(이름 바꾼 첫해)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2025</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">이름을 연도에 맞춰 붙임; Apple Intelligence 전면 통합</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">iOS 27</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2026</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">현재 최신 버전(이 책의 기준)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
iOS 개발 주요 연혁(2026년 8월 기준)

#### 2. 울타리 쳐진 정원: 애플 생태계의 '규칙'과 '이익'

애플 생태계는 흔히 '울타리 쳐진 정원(Walled Garden)'이라 불려요. 규칙이 많고 관리가 엄격하거든요. 앱은 심사를 통과해야 등록할 수 있고, 개발에는 반드시 Mac과 Xcode를 써야 하며, 배포는 주로 App Store로 이뤄져요. 답답하게 들리나요? 하지만 개발자 입장에서는 이 규칙들이 두둑한 이익으로 돌아와요.

- 기기 파편화가 극히 적어요: 아이폰 모델은 몇 종류 안 되고 화면 크기와 시스템 버전이 고도로 통일되어 있어요. 5가지 기기만 대응하면 사용자의 95%를 커버해요(안드로이드는 수십 종을 대응해야 할 수도 있어요).
- 시스템 버전 업데이트율이 극히 높아요: 새 시스템이 나오면 몇 주 안에 70~80%의 사용자가 업그레이드해요. 새 API를 마음껏 쓸 수 있고 '5년 전 옛 시스템'을 배려할 필요가 없어요.
- 사용자의 유료 결제 습관이 좋아요: App Store 사용자는 앱과 인앱 결제에 더 기꺼이 돈을 써요.
- 심사는 엄격해도 스토어는 깨끗해요: 짝퉁이나 악성 앱이 적어 좋은 제품이 더 잘 눈에 띄어요.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
주의: 먼저 비용부터 분명히

{class="mt-1"}
iOS 개발에는 높은 진입 장벽이 있어요. Mac이 반드시 필요하고(Xcode는 macOS 전용이에요), 스토어 등록에는 연 99달러짜리 개발자 계정이 필요해요(개인 개발자 무료 계정으로도 로컬 실기기 디버깅은 되지만 등록은 안 돼요). 이 비용을 잘 따져 본 뒤 출발하세요. 다만 좋은 소식은, 학습 단계에서는 무료 계정으로 충분하다는 거예요. 제60장에서 다룰게요.
:::

#### 3. 어떤 언어로 쓸까: Objective-C 아니면 Swift?

iOS 개발 역사에도 두 명의 '주인공'이 있었어요. Objective-C는 개국공신으로 2008년부터 2014년까지 쓰였고, Swift는 애플이 2014년에 발표한 새 언어로 이후 Swift 6(2024년 발표, 엄격한 동시성 검사 도입)까지 진화했어요. 2026년 현재 새 프로젝트는 거의 전부 Swift를 써요.

기초가 없는 여러분에게 드리는 솔직한 한마디: 바로 Swift를 배우세요. Objective-C는 볼 필요도 없어요. 입사 후 10년 전 레거시 코드를 관리하게 되는 경우가 아니라면요. Swift의 장점은 이래요. 문법이 깔끔하고(C 언어 시절의 세미콜론과 헤더 파일 부담이 없어요), 옵셔널(Optional) 메커니즘이 언어 차원에서 '널 포인터 크래시'를 없애 주고, SwiftUI와 매끄럽게 맞물리며, iPad의 Swift Playgrounds로 놀면서 배울 수도 있어요.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Objective-C 스타일(고대 유적)

{class="font-mono text-xs leading-relaxed"}
NSString *name = @"장산"; [name stringByAppendingString:@"안녕하세요"]; // 대괄호 + 포인터 + 세미콜론 3종 세트
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Swift 스타일(현대적이고 깔끔)

{class="font-mono text-xs leading-relaxed"}
var name = "장산" name += "안녕하세요" // 자연어처럼 직관적이에요
:::
:::

#### 4. 앱은 어떻게 태어날까?

모든 플랫폼과 마찬가지로 iOS 앱의 탄생에도 생산 라인이 있어요. 다만 애플 버전에는 '보안 검색대'가 두 개 더 있죠.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-lightbulb mr-1"></i> 아이디어</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center">📐 설계(화면+기능)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-keyboard mr-1"></i> 코드 작성(Swift + SwiftUI)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hammer mr-1"></i> 컴파일·서명</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> 테스트(에뮬레이터+실기기)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-stamp mr-1"></i> 애플 심사</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> App Store 출시</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
그림 1: iOS 앱이 아이디어에서 스토어 등록까지 가는 전 과정(추가된 '심사' 단계에 주목)
:::

과정의 핵심 개념:

- 서명(Signing): 모든 iOS 앱은 설치되려면 반드시 '서명'이 있어야 해요. '이 패키지는 여러분이 만들었고 변조되지 않았다'는 증명이죠. 학습 단계에서는 Xcode가 여러분의 Apple ID로 자동 서명하고, 등록할 때는 개발자 인증서를 써요. 제67장에서 자세히 다뤄요.
- 시뮬레이터(Simulator): Mac 위에 가상으로 만들어진 아이폰으로, 개발과 디버깅의 주 전장이에요. Mac의 CPU로 돌아가서 특히 부드럽고, 안드로이드 에뮬레이터보다 체험이 한참 좋아요.
- TestFlight: 애플 공식 '내부 테스트 배포' 도구예요. 등록 전에 테스트 버전을 최대 10,000명의 테스트 사용자에게 보내고, 그들이 TestFlight 앱으로 설치해 써 봐요. iOS 생태계만의 우아함이에요.

#### 5. iOS 기술 스택 전체 그림: 여러분의 '무기 목록'

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">계층</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">주류 선택(2026)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">어디에 쓰나</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">언어</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift 6</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">로직을 쓰는 언어</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">화면</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI + 애플 디자인 가이드라인(HIG)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">코드로 화면 그리기(이 책의 메인 줄기)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">아키텍처</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MVVM + @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">화면과 로직 분리</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">데이터 저장</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData(데이터베이스) + UserDefaults(설정)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">데이터를 휴대폰에 저장</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">네트워크</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession + async/await + Codable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">서버와 대화</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">빌드 도구</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode Build System / xcodebuild</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">코드를 설치 패키지로</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">개발 환경</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode(macOS 전용)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">애플 공식 IDE</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
2026년 iOS 주류 기술 스택 한눈에 보기

눈치챘나요? 이 목록은 안드로이드 것보다 한참 짧아요. 애플이 많은 일을 '전부 도맡아' 하기 때문이에요. 닫힌 생태계의 대가는 자유도이고, 보상은 편안함이에요. 어떤 네트워크 라이브러리를, 어떤 데이터베이스를 고를지 고민할 필요가 없어요. 공식이 주는 것이 대개 최선의 답이거든요.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
직접 해 보기: 휴대폰의 '애플 등록 정보' 살펴보기

{class="mt-1"}
아이폰의 [설정] → [일반] → [정보]를 열고 세 가지를 적어 두세요. iOS 버전, 기기 이름, 사용 가능한 용량이요. 그다음 App Store의 '투데이' 페이지를 이리저리 둘러보며 좋은 앱들의 스크린샷과 카피에 주목하세요. 오늘부터 여러분이 스토어를 보는 시선은 '사용자'에서 '개발자'로 바뀌는 거예요.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
이 장 정리

- 2008년 App Store 출시로 '앱 경제' 탄생; 2026년 현재 버전은 iOS 27
- 울타리 정원의 계산서: 규칙은 많지만 기기는 적고, 버전은 새것이며, 사용자는 돈을 쓰고, 스토어는 깨끗해요
- 높은 장벽: Mac 필수; 등록에는 연 99달러 개발자 계정; 학습 단계에서는 무료 계정으로 충분
- 언어는 바로 Swift를 배우세요; Objective-C는 레거시 코드의 전유물
- 파이프라인은 안드로이드보다 한 단계 더: 애플 심사; TestFlight는 내부 테스트 배포의 필살기
- 2026 표준 기술 스택: Swift 6 + SwiftUI + MVVM + SwiftData + URLSession + Xcode
:::
