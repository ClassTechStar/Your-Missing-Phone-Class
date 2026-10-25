---
id: di-liu-shi-jiu-zhang
num: 69
part: ios-kai-fa-pian
nav: 제69장: 빠른 참조 매뉴얼과 리소스
toc: default
kind: chapter
---

### 제69장: 빠른 참조 매뉴얼과 리소스

{class="chapter-intro mb-4"}
이번 장은 단독으로 쓸 수 있는 빠른 참조 매뉴얼이에요. 어떤 작성법이 가물가물하거나 빠르게 결정이 필요할 때 바로 여기로 넘어오세요. '포켓 카드'로 여기길 권해요. 자주 쓰는 코드 참조, 자주 묻는 질문, 학습 리소스까지 한 페이지도 빠짐없이 담겨 있어요.

#### 1. 자주 쓰는 코드 빠른 참조 카드

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">하려는 작업</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">핵심 코드</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">화면 내부 상태</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State private var x = 초기값</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">화면 간 공유 로직</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Observable class VM { var x = 0 }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">세로/가로 레이아웃</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack { }</code> / <code class="inline">HStack { }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">유연한 공간</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Spacer()</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">리스트</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List { ForEach(배열) { ... } }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">화면 이동</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">NavigationStack + NavigationLink</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">바텀 시트</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">.sheet(isPresented: $show) { 내용 }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">현재 화면 닫기</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Environment(\.dismiss) var dismiss</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">네트워크로 데이터 가져오기</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">try await URLSession.shared.data(from: url)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">JSON 파싱</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X: Codable</code> + <code class="inline">JSONDecoder().decode</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">작은 설정 저장</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults.standard.set(값, forKey: "키")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">구조화된 데이터 저장</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Model</code> + <code class="inline">modelContainer</code> + <code class="inline">@Query</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">다크 모드 대응</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">시스템 색상 사용(.primary / Color(.systemGray6)), 하드코딩 금지</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">테스트 실행</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><kbd>⌘U</kbd></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
iOS 개발 빠른 참조 카드(2026년 8월판)

#### 2. 자주 묻는 질문 FAQ

Q1: Mac이 없는데 iOS 개발을 배울 수 있나요?

언어는 배울 수 있지만 완전한 개발은 어려워요. iPad/iPhone의 Swift Playgrounds로 61장의 내용 전부를 배울 수 있어요. 하지만 Xcode는 macOS 전용이라 결국 Mac 한 대는 필요해요. 예산이 부족하면 클라우드 Mac을 임대하거나 중고 Mac mini를 사서 버틴 다음, 언어를 다 배고 나서 투자를 결정해도 돼요.

Q2: iOS 개발을 배우는 데 비용이 얼마나 들까요?

학습 단계: 0원(Xcode 무료 + 무료 Apple ID로 실기기 디버깅). 출시 단계: 개발자 계정 연 99달러(약 700위안). 여기에 Mac 한 대 하드웨어 투자가 더해지는데, 이게 전부예요. 보상에 비하면 — 앱스토어에서 작은 도구 앱도 유료 사용자가 생겨요 — 충분히 계산이 맞는 투자예요.

Q3: SwiftUI와 UIKit 중 뭘 먼저 배워야 하나요?

SwiftUI예요. 2026년의 새 프로젝트, 새 튜토리얼, 새 채용 공고는 모두 SwiftUI 중심이고 이 책도 처음부터 끝까지 SwiftUI를 써요. UIKit은 이전 세대 프레임워크로 아직도 수많은 기존 프로젝트에서 쓰여요. SwiftUI에 익숙해진 뒤 필요할 때 UIKit을 보충하면(공식 상호 운용 튜토리얼이 있어요) 금방 익힐 수 있어요. 순서를 거꾸로 하지 마세요.

Q4: iOS 개발은 취업이 잘 되나요?

2026년 시세: 단순히 '화면을 그릴 줄 아는' 초급 포지션은 경쟁이 치열하지만, 'Swift + SwiftUI를 알고 출시한 작품이 있는' 개발자는 여전히 인기가 많아요. iOS 포지션의 급여 중위값은 여러 기술 스택 중에서 늘 상위권이에요. 배우는 시기의 당신에게 가장 좋은 이력서는 스토어에 올라 있는 자신이 만든 앱이에요.

Q5: 앱이 심사에서 반려됐다면 어떻게 하나요?

당황하지 마세요. 아주 흔한 일이에요. 첫 제출이 반려될 확률은 결코 낮지 않아요. 애플의 반려 사유는 보통 매우 구체적으로 적혀 있어요(어느 페이지, 어떤 가이드라인). 하나씩 고친 뒤 App Store Connect에서 답변으로 설명하고 다시 제출하면 돼요. 흔한 세 가지 반려 원인: 권한 용도 설명 부족, 화면의 버그, 메타데이터(스크린샷/설명)와 실물의 불일치. 이 세 가지를 미리 점검하면 한 바퀴의 대기를 줄일 수 있어요.

#### 3. Xcode 자주 쓰는 단축키 빠른 참조

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">동작</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">단축키</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">실행 / 테스트</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R / ⌘U</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">캔버스 프리뷰 열기</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">빠르게 파일 열기</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">전체 검색</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘F</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">들여쓰기 정리</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">주석 / 주석 해제</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">빌드 캐시 정리</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘K</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">정의로 이동</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘ 클릭</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">이름 바꾸기(전체에서 안전하게 이름 변경)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">우클릭 → Refactor → Rename</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Xcode 자주 쓰는 단축키 빠른 참조

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
팁: 빌드가 이상하면 먼저 캐시부터 정리

{class="mt-1"}
'어제까지만 해도 돌아가던 앱이 오늘은 안 돼' 같은 괴현상의 6~7할은 빌드 캐시 꼬임이 원인이에요. ⇧⌘K로 정리하고 다시 빌드하면 이런 미스터리의 태반은 치유돼요. 그래도 안 되면 Xcode를(Mac째로) 재시작하고, 그래도 안 되면 'DerivedData 폴더 삭제'예요. iOS 개발자들 사이에 입에서 입으로 전해지는 궁극의 3연타예요.
:::

#### 4. 추천 학습 리소스

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">유형</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">리소스</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">추천 이유</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">공식</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">developer.apple.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">애플 공식 문서. SwiftUI/Swift 튜토리얼이 모두 들어 있는 최고 권위</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">공식</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple의 SwiftUI Tutorials</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">공식 따라하기 강좌, 초보자 친화성 만점</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">공식</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift 공식 사이트(swift.org)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">언어 공식 문서와 온라인 연습장</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">커뮤니티</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hacking with Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Paul Hudson의 무료 튜토리얼 모음, 품질은 인정받는 최상위권</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">커뮤니티</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stack Overflow(swiftui 태그)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">오류로 헤맬 때 가장 먼저 찾는 곳</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">영상</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Developer 공식 채널(WWDC 영상)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">매년 새 기술의 권위 있는 해설</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">디자인</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple 휴먼 인터페이스 가이드라인(HIG)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">'애플다운' 화면을 만들기 위한 공식 성경</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">함께 읽기</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">제7편 〈AI 코딩 실전편〉(37~47장)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI로 iOS 개발을 보조하는 완전한 노하우</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
iOS 개발 학습 리소스 목록(2026년 8월)

#### 5. 맺음말: 첫 번째 앱에서 N번째 앱까지

돌아보면 당신은 'SwiftUI가 뭔지도 모르던' 상태에서 Xcode를 설치하고, Swift를 배우고, SwiftUI로 화면을 그리고, 앱에 데이터베이스와 네트워크를 연결하고, 나아가 테스트, 패키징, 출시까지 — 이 길에서 0에서 1로 가는 가장 어려운 구간을 이미 걸어 넘었어요.

기술의 세계는 변화가 빨라요. 프레임워크는 업그레이드되고, 도구는 세대를 바꾸고, AI는 '키보드를 두드리는' 일을 점점 더 많이 대신하겠죠. 하지만 하나만은 낡지 않아요. 막연한 아이디어를 명확한 단계로 쪼개고 한 걸음씩 실현하는 당신의 능력이에요. 도구는 증폭기이고, 사고는 기초예요. 증폭기는 바꿀 수 있지만 기초는 흔들리면 안 돼요.

:::inline div .quote-line
더 이상 "휴대폰 잘 쓰는 사람"이 아니에요. 머릿속 아이디어를 수억 대의 아이폰에서 실제로 돌아가는 앱으로 만들 수 있어요. 오늘부터 키보드로 만들어 보세요 — 이것이 iOS 개발자의 낭만이에요.
:::

#### 참고 문헌

{class="list-decimal pl-6 mb-3 space-y-1 text-xs text-gray-500"}
1. Apple Inc. (2026). SwiftUI Framework Documentation. developer.apple.com.
2. Apple Inc. (2026). Swift Programming Language Guide. swift.org.
3. Apple Inc. (2026). SwiftData Framework Documentation. developer.apple.com.
4. Apple Inc. (2026). App Store Review Guidelines. developer.apple.com/app-store/review.
5. Apple Inc. (2026). Human Interface Guidelines (HIG). developer.apple.com/design.
6. Apple Inc. (2026). Xcode 27 Release Notes and App Distribution Guide.
