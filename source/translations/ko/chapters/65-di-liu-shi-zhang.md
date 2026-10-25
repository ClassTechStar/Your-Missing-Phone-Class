---
id: di-liu-shi-zhang
num: 60
part: ios-kai-fa-pian
nav: 제60장: 개발 환경 구축 — Xcode와 첫 번째 프로젝트
toc: default
kind: chapter
---

### 제60장: 개발 환경 구축 — Xcode와 첫 번째 프로젝트

{class="chapter-intro mb-4"}
일을 잘하려면 먼저 도구를 갈춰야 해요. 이 장에서는 '주방'을 차릴 거예요. Xcode를 설치하고, 시뮬레이터를 돌려 보고, 인생 첫 iOS 프로젝트를 만든 뒤, 프로젝트 구조를 하나씩 뜯어서 확실히 이해해요. 환경을 갖추고 나면 여러분이 쓴 코드가 누를 수 있는 버튼으로 변하는 순간을 처음 보게 될 거예요. 이 순간을 평생 기억하는 사람이 많아요.

#### 1. Mac 한 대 준비하기

먼저 장벽부터 말할게요. iOS 개발은 반드시 macOS에서 진행해야 해요. Mac이 없다면 선택지는 세 가지예요. 하나 사기(중고 Mac mini나 MacBook Air로도 충분해요), 단기간 클라우드 Mac을 빌리기, 또는 먼저 제8편 '안드로이드 개발 실전편'(Windows로도 할 수 있어요)을 읽기.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">항목</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">최소 요구 사항</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">쾌적한 선(추천)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">칩</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Silicon(M1 이상)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">M2 이상 최신형</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">메모리</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8GB</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">16GB</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">저장 공간</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">40GB 이상 확보(Xcode 본체가 꽤 커요)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256GB부터</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">시스템</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">최신 macOS</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">자동 업데이트 유지</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Mac 개발용 사양 참고(2026년 8월)

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
팁: Mac이 없어도 언어는 먼저 배울 수 있어요

{class="mt-1"}
iPad의 무료 Swift Playgrounds로 Swift 언어 기초를 배울 수 있어요(Mac이 필요 없어요). iPhone에 설치할 수도 있고요. 먼저 제61장의 언어 내용을 Playgrounds에서 익혀 두면 Mac을 받는 순간 바로 이륙할 수 있어요. '도를 가느라 장작 베기가 늦어지는 일은 없다'는 말이 딱 이런 거예요.
:::

#### 2. Xcode 설치하기

Xcode는 애플 공식 통합 개발 환경이에요. 무료고요. 세 단계로 설치해요.

1. Mac에서 App Store를 열고 "Xcode"를 검색한 뒤 설치를 누르세요. 용량이 몇 GB에 달하니 인터넷이 빠른 시간대를 골라 진행하세요.
2. 설치 후 처음 실행하면 이용약관에 동의하고 구성 요소 설치를 마치세요(자동으로 진행돼요).
3. 메뉴에서 Xcode → Settings → Locations로 가서 Command Line Tools가 선택되어 있는지 확인하세요. 명령줄 도구는 많은 스크립트와 서드파티 도구의 전제 조건이에요.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
주의: 버전과 시스템의 '맞추기 게임'

{class="mt-1"}
새 Xcode는 대개 최신 macOS를 요구하고, 오래된 Mac은 구버전에 갇히기 쉬워요. App Store에 등록할 때 애플은 비교적 새 Xcode로 빌드한 앱을 요구해요(보통 유예 기간은 줘요). 그러니 시스템 업데이트를 너무 오래 미루지 마세요. iOS 개발자는 '새 버전 좇기'에 가장 부지런한 무리거든요.
:::

#### 3. 여러분의 첫 프로젝트 만들기

Xcode를 열고 Create New Project → iOS 선택 → App 템플릿을 고른 뒤 다음을 채우세요.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">항목</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">채울 내용</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">설명</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Product Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstApp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">앱 이름</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">여러분의 Apple ID(무료)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">서명용, 개인 계정이면 충분해요</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Organization Identifier</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Product Name과 합쳐져 번들 식별자가 돼요</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interface</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">이 책의 메인 프레임워크</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Language</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">설명 생략</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
프로젝트 생성 때 채울 다섯 가지

Create를 누르면 Xcode가 바로 실행할 수 있는 프로젝트를 만들어 줘요. 왼쪽 위에서 시뮬레이터(예: iPhone 17)를 고르고 ▶를 눌러 실행하세요. 몇 초 뒤 시뮬레이터 화면에 "Hello, world!"가 적힌 창이 나타나요. 여러분의 첫 iOS 앱이 태어난 거예요.

#### 4. 프로젝트 구조 해부: 파일마다 하는 일

왼쪽은 프로젝트 내비게이터예요. 초보자는 이것들만 알면 돼요.

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="290" viewBox="0 0 600 290" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="290" fill="#fafafa" rx="8"/>
      <text x="20" y="28" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ 프로젝트 루트</text>
      <rect x="30" y="42" width="540" height="225" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <rect x="45" y="56" width="250" height="196" fill="#eef2ff" rx="5"/>
      <text x="56" y="78" font-size="11" fill="#1e1b4b" font-weight="bold">MyFirstApp/(코드 디렉터리)</text>
      <text x="66" y="100" font-size="10" fill="#374151">├ MyFirstAppApp.swift  ← 앱 진입점</text>
      <text x="66" y="120" font-size="10" fill="#374151">├ ContentView.swift  ← 메인 화면</text>
      <text x="66" y="140" font-size="10" fill="#374151">└ Assets.xcassets  ← 아이콘, 이미지, 색상</text>
      <text x="56" y="166" font-size="10" fill="#6b7280">(새 파일은 모두 이 디렉터리에 넣어요)</text>
      <text x="56" y="196" font-size="10" fill="#1e1b4b" font-weight="bold">Info 탭 / Info.plist</text>
      <text x="66" y="216" font-size="10" fill="#6b7280">앱 선언: 이름, 권한, 설정</text>
      <rect x="310" y="56" width="245" height="196" fill="#f0fdf4" rx="5"/>
      <text x="321" y="78" font-size="11" fill="#065f46" font-weight="bold">다른 중요한 위치</text>
      <text x="331" y="100" font-size="10" fill="#374151">📁 Preview Content/  ← 미리보기 소재</text>
      <text x="331" y="122" font-size="10" fill="#374151"><i class="fas fa-bullseye mr-1"></i> Target 설정(파란색 프로젝트 아이콘)</text>
      <text x="331" y="142" font-size="10" fill="#6b7280">— 버전 번호, 최소 지원 시스템, 서명이 모두 여기</text>
      <text x="331" y="168" font-size="10" fill="#374151"><i class="fas fa-flask mr-1"></i> MyFirstAppTests/  ← 단위 테스트</text>
      <text x="331" y="188" font-size="10" fill="#374151">📱 MyFirstAppUITests/ ← UI 테스트</text>
      <text x="331" y="216" font-size="10" fill="#9ca3af">(테스트 템플릿이 이미 생성됨, 67장에서 사용)</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
그림 2: 초보자가 꼭 알아야 할 Xcode 프로젝트 구조
:::

- MyFirstAppApp.swift: 프로그램 진입점이에요. SwiftUI에서는 몇 줄 안 돼요. '시작한 뒤 메인 화면을 표시'하는 역할이죠.
- ContentView.swift: 메인 화면 뷰예요. 지금 보고 있는 모든 것이 여기 있어요.
- Assets.xcassets: 리소스 창고예요. 아이콘, 이미지, 색상이 모두 여기에 들어가요.
- Target 설정: 왼쪽 파란색 프로젝트 아이콘을 눌러 들어가면 버전 번호, 최소 iOS 버전, 서명이 모두 안에 있어요. 앱 표시 이름과 아이콘도 여기서 설정해요.

#### 5. Xcode 생산성 팁: 초보자의 다섯 가지 '단축키 치트키'

이것들을 익혀 두면 '아주 프로답게' 보일 거예요.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">동작</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">단축키</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">역할</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">실행</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">빌드해서 실행해요</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">캔버스 미리보기 열기/전환</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">위지위그(WYSIWYG) 스위치</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">들여쓰기 정리</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">선택한 코드의 들여쓰기를 자동으로 정리해요</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">빠른 파일 열기</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">파일 이름 입력으로 즉시 열기(가장 많이 써요!)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">주석 달기/해제</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">디버깅하며 코드를 손쉽게 켜고 끄기</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Xcode 자주 쓰는 단축키(초보자 5종 세트)

숨은 혜택 두 가지 더: 시뮬레이터 여러 개 띄우기(iPhone과 iPad를 동시에 돌려 레이아웃 비교)와 코드 조각 라이브러리(자주 쓰는 코드 몇 줄을 오른쪽 Snippets 패널로 드래그해 두면 다음에 한 번에 삽입). 효율 도구를 먼저 쓰다 보면 손감각은 저절로 좋아져요.

#### 6. 실기기 디버깅: 앱을 여러분의 아이폰에 설치하기

시뮬레이터도 좋지만 진짜 기기가 최종 목적지예요. 무료 Apple ID로도 실기기 디버깅이 가능해요.

1. 케이블로 iPhone을 연결하세요(또는 같은 Wi-Fi에서 무선 디버깅).
2. Xcode 상단 기기 목록에서 여러분의 휴대폰을 선택하세요. 처음에는 Apple ID 로그인을 안내하며 서명을 자동으로 구성해 줘요.
3. iPhone의 [설정] → [일반] → [VPN 및 기기 관리]에서 여러분의 개발자 인증서를 신뢰하세요.
4. ▶를 누르면 앱이 실기기에 설치돼요.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
주의: 무료 계정의 '7일 제한'

{class="mt-1"}
무료 Apple ID로 서명한 앱은 7일 뒤에 만료돼요(다시 한 번 실행하면 갱신돼요). 애플의 남용 방지 메커니즘으로, 학습 단계에서는 전혀 지장이 없어요. 유료 개발자 계정(연 99달러)에는 이 제한이 없어요. 제67장에서 자세히 다뤄요.
:::

#### 7. 맛보기 실습 + 자주 나오는 오류 응급 처치

ContentView.swift를 열어 Text("Hello, world!")의 글자를 여러분의 이름으로 바꾸고 ⌘R로 다시 실행하세요. 몇 초 뒤 시뮬레이터에 여러분의 이름이 표시돼요. 축하해요. '코드 수정 → 빌드 → 설치 → 실행'의 완전한 첫 사이클을 끝낸 거예요.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">오류 증상</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">흔한 원인</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">해결책</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Signing 오류</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team 미선택, 인증서 만료</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Target → Signing에서 여러분의 계정을 체크하세요. 무료 계정은 다시 한 번 실행</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">시뮬레이터 검은 화면/실행 안 됨</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">시뮬레이터 이미지 손상</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">메뉴 Device → Erase All Content; 또는 시뮬레이터를 삭제 후 다시 추가</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode 다운로드 느림/설치 안 됨</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">App Store 네트워크 불안정</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">시간대를 바꿔 보세요; 또는 애플 개발자 사이트에서 .xip 오프라인 패키지를 내려받으세요</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
초보자 환경 오류 응급 처치표

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
직접 해 보기: '개발 입문 의식' 체크리스트 완성하기

{class="mt-1"}
① Xcode를 설치하고 시뮬레이터를 돌려 보기; ② 실기기에서 내 앱을 한 번 실행하고 스크린샷으로 남기기; ③ Hello 글자를 내 이름으로 바꾸기; ④ Target 설정에서 앱 표시 이름을 '내 첫 번째 앱'으로 바꾸기. 이 네 가지를 끝내면 여러분도 작품을 가진 사람이 돼요.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
이 장 정리

- 높은 장벽: Mac + Xcode; Mac이 없으면 iPad의 Swift Playgrounds로 먼저 언어 배우기
- Xcode는 App Store에서 설치; 새 버전은 새 시스템을 요구하니 업데이트를 미루지 마세요
- 새 프로젝트 5요소: 이름, Team, 조직 식별자, SwiftUI, Swift
- 프로젝트 암기 문구: 코드는 모두 MyFirstApp/ 폴더에; Target 설정이 버전과 서명을 담당
- 무료 Apple ID 실기기 디버깅은 7일 서명 제한; 유료 계정에는 이 제한이 없음
- 개발 일상 = 코드 수정 → ⌘R → 결과 확인, 계속 반복
:::
