---
id: di-wu-shi-liu-zhang
num: 56
part: an-zhuo-kai-fa-pian
nav: 제56장: 다듬고 출시하기 — Google Play 등록
toc: default
kind: chapter
---

### 제56장: 갈고닦기와 출시 — 테스트, 디버깅, Google Play 출시

{class="chapter-intro mb-4"}
앱을 만들었는데, 그다음은요? 이번 장은 "돌아가는 수준"에서 "인도할 수 있는 수준"으로 가는 세 가지를 다뤄요. 어떻게 효율적으로 디버깅해 버그를 찾는지, 어떻게 테스트를 작성해 회귀를 막는지, 어떻게 앱을 Google Play에 올려 전 세계가 다운로드하게 만드는지죠. 출시는 단순한 의식이 아니에요. 작품을 제품으로 바꾸는 기점이에요.

#### 1. 디버깅 3대 필살기: Logcat, 중단점, UI 인스펙터

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">도구</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">무엇을 하나</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">어떻게 쓰나</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logcat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">시스템/직접 남긴 로그 보기</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">코드에서 Log.d("TAG","값=$x"), 패널에서 TAG 검색으로 필터</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">중단점 디버깅</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">프로그램을 특정 줄에서 멈추게 하고 변수 값을 확인</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">줄 번호 옆을 클릭해 빨간 점을 만들고, Debug 모드로 실행해 한 단계씩 진행</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Layout Inspector</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">실행 중인 화면 구조 보기</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">메뉴 Tools → Layout Inspector, 컴포넌트 트리를 실시간으로 확인</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
디버깅 3대 필살기

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
팁: 오류 메시지는 어떻게 읽나요?

{class="mt-1"}
크래시가 나면 Logcat에 빨간색 스택 트레이스(Stacktrace)가 떠요. 아래에서 위로 올라가며 내 패키지 이름으로 시작하는 첫 줄(예: com.example.yourapp)을 찾으세요. 그 줄이 대체로 사건 현장이에요. 먼저 "Exception 종류"(null 포인터? 타입 변환?)를 보고, 이어서 "at ... 내 파일:줄 번호"를 보세요. 이 한 방으로 크래시의 80%를 해결할 수 있어요.
:::

#### 2. 테스트: 코드에 보험 들기

손으로 하는 테스트는 믿음직스럽지 않아요. 이 기능을 고쳤더니 다른 기능이 몰래 고장 나 있죠. 테스트는 "후회약"이자 "방탄 조끼"예요. 안드로이드 테스트는 세 계층으로 나뉘는데, 초보자는 먼저 첫 계층을 완전히 익히세요:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">계층</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">무엇을 테스트하나</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">어디에 두나</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">속도</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">단위 테스트</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">순수 로직(계산, 검증)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/test/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">초 단위</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">계측 테스트</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">실제 기기에서의 화면 동작</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/androidTest/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">분 단위</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">수동 테스트</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">사람이 직접 느끼고 경험</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">언제나 필요</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
테스트 3계층

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 단위 테스트 예시</span><span class="dots">···</span>
:::

```
// "금액 문자열을 숫자로" 같은 로직은 순수 함수로 분리
fun parseAmount(input: String): Double? {
    val v = input.trim().toDoubleOrNull()
    return if (v != null && v > 0) v else null
}

// 테스트(JUnit4)
@Test
fun emptyInputReturnsNull() {
    assertEquals(null, parseAmount(""))
}
@Test
fun negativeReturnsNull() {
    assertEquals(null, parseAmount("-5"))
}
@Test
fun normalValueParses() {
    assertEquals(12.5, parseAmount("12.5"))
}
```
:::

가계부의 금액 검증, 통계 계산에는 모두 단위 테스트가 뒤를 받쳐 줘야 해요. 테스트 실행: test 디렉터리 우클릭 → Run. 초록불로 전부 통과하면 마음 놓고 코드를 고치세요.

#### 3. 서명과 패키징: 앱에 "도장" 찍기

안드로이드는 모든 설치 패키지에 서명을 요구해요. 공식 도장을 찍듯 "이 패키지는 내가 냈고 변조되지 않았다"를 증명하는 거죠. 디버깅 때는 Android Studio가 자동으로 debug 서명을 쓰고, 출시에는 자신만의 release 서명이 필요해요. 절차예요:

1. 메뉴 Build → Generate Signed Bundle / APK;
2. keystore 파일(키 저장소) 생성 — 비밀번호를 설정하고 안전하게 보관;
3. release + AAB 형식을 선택하고 빌드 완료.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
주의: keystore를 잃어버리면 = 앱을 잃어버려요

{class="mt-1"}
출시 후 앱을 업데이트할 때는 반드시 같은 서명을 써야 해요. 그렇지 않으면 스토어가 업데이트를 거절하거든요. keystore 파일과 비밀번호를 잃어버리면 새 앱을 만들어 다시 출시할 수밖에 없어요. 기존 사용자는 모두 끊기죠. keystore와 비밀번호를 반드시 안전한 곳(암호화한 클라우드 드라이브 + 메모)에 백업하세요. 안드로이드 개발자가 치르는 가장 비싼 교훈 중 하나예요.
:::

#### 4. Google Play 출시 전 과정

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> 개발자 계정 등록</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> 스토어 자료 준비</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> AAB 업로드</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> 데이터 보안 양식 작성</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> 심사(수 시간~수 일)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> 출시</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
그림 6: Google Play 출시 6단계
:::

- 가입: 일회성 등록비 25달러, 쓸 수 있는 Google 계정 필요;
- 소재: 앱 아이콘(512×512), 스크린샷(2장 이상), 기능 설명, 개인정보 처리방침 링크(데이터 수집 시 필수);
- 데이터 보안 양식: 어떤 데이터를 수집하는지 사실대로 신고 — 네트워크 없는 가계부라면 "수집 없음"도 가능;
- 심사: 새 계정의 첫 출시는 흔히 사람이 심사하고, 몇 시간에서 며칠까지 걸려요. 반려되면 지적 사항대로 고치세요.

중국 본토 사용자 주의: Google Play는 특별한 네트워크 환경이 필요하고, 중국 본토 배포는 보통 현지 스토어(화웨이, 샤오미, 잉융바오 등)로 이루어져요. 현지 스토어 출시 절차도 비슷하지만 스토어마다 심사 기준이 달라요. 같은 AAB/APK로 여러 스토어에 배포할 수 있어요. 연습 삼아 일단 한 곳이라도 통과하면 이긴 거예요.

#### 5. 스토어 소재 만들기: 첫인상이 곧 다운로드예요

스토어 페이지는 사용자가 "가게를 구경"할 때 보는 쇼윈도예요. 세 가지 소재가 첫인상을 결정해요:

- 아이콘: 512×512, 스크린샷으로 대충 때우지 마세요. 디자인 감각이 없다면 AI 도구로 간결한 기하학 도형을 하나 만들고, 휴대폰 홈 화면에서 줄어든 크기로도 한눈에 알아볼 수 있어야 합격이에요;
- 스크린샷: 최소 2장, 가능하면 4-6장으로 핵심 기능 장면을 보여 주세요. 매 장마다 사람 말투 문구 한 줄을 붙이고요("1초 만에 한 건 기록"이 "효율적인 가계부 솔루션"보다 열 배 좋아요);
- 설명: 첫 문장에서 "이것이 무엇인지 + 누구에게 쓰는 것인지"를 분명히 하세요. "가장 전문적, 최강" 같은 말을 쌓아 두지 말고요. 스토어 검색 가중치는 주로 키워드와 다운로드 전환을 보니까 솔직함이 과장보다 효과적이에요.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
팁: 경쟁 앱을 비교해 보기

{class="mt-1"}
출시 전에 스토어에서 같은 종류 앱 상위 10개를 둘러보고 스크린샷을 찍어 비교하세요. 아이콘은 어떤 스타일인지, 스크린샷은 어떤 셀링 포인트를 말하는지, 제목은 어떻게 썼는지요. 모방은 표절이 아니에요. 요령을 배우고 내용만 자신의 것으로 바꾸는 것, 이것이 모든 제품의 콜드 스타트에서 가장 빨리 배우는 한 과목이에요.
:::

#### 6. 성능 최적화와 크래시 리포트 체크리스트

앱을 출시하기 전에, 이 두 가지에 각각 30분씩 쓸 가치가 있어요:

##### 1. 성능 셀프 점검 네 가지

1. 리스트는 LazyColumn: 긴 목록을 절대 Column으로 억지로 나열하지 마세요. 지연 로딩이 안드로이드 성능의 첫 번째 교훈이에요;
2. 이미지는 원본을 그대로 밀어 넣지 마세요: Coil 이미지 라이브러리로 자동 축소와 캐싱을 하세요. 5MB짜리 원본 한 장이면 저사양 기기를 아예 멈추게 할 수 있어요;
3. 메인 스레드에서 무거운 일 피하기: 데이터베이스, 네트워크, 큰 파일은 모두 코루틴에서 처리;
4. Profiler로 측정하기: Android Studio에 내장된 성능 분석기로 메모리, CPU, 배터리 사용량을 볼 수 있어요. 먼저 측정하고 나서 최적화하세요. 감각에 의존하지 말고요.

##### 2. 크래시 리포트

여러분이 테스트할 때 크래시가 안 났다고 사용자 휴대폰에서도 안 나는 건 아니에요. 출시 전에 Firebase Crashlytics(구글 공식, 무료)를 붙이세요. 설정 몇 줄로 사용자가 크래시를 겪으면 스택 트레이스가 자동으로 보고되고, 콘솔에서 "어떤 기종, 어떤 버전, 몇 번째 줄에서 크래시됐는지"를 볼 수 있어요. 크래시 모니터링 없는 출시는 눈 감고 운전하는 것과 같아요.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
직접 해 보기: 가계부를 한 번 "인도"하기

{class="mt-1"}
① parseAmount 같은 로직에 단위 테스트 3개를 보태세요. ② Logcat으로 직접 만든 크래시를 직접 잡아 고치세요. ③ release 서명이 된 APK를 만들어 친구에게 보내 설치하게 하세요(이래야 "작품"의 의식이 있죠). ④ 여유가 되면 개발자 계정을 만들고 가계부를 실제로 제출해 출시하세요. 앞의 세 가지는 오늘 밤 안에 끝낼 수 있어요.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
이번 장 정리

- 디버깅 3대 필살기: Logcat으로 로그, 중단점으로 변수, Layout Inspector로 화면 보기
- 크래시 읽기: 스택의 아래에서 위로 내 패키지 이름이 처음 나오는 줄 찾기
- 테스트 3계층: 단위(초 단위, 이것부터 배우기)/계측/수동
- 출시에는 반드시 서명: keystore와 비밀번호를 백업해 두세요. 잃어버리면 앱 신원이 바뀌어 버려요
- 출시 6단계: 가입 → 소재 → AAB 업로드 → 데이터 보안 양식 → 심사 → 출시
:::
