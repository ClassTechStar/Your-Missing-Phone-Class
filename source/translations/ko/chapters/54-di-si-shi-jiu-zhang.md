---
id: di-si-shi-jiu-zhang
num: 49
part: an-zhuo-kai-fa-pian
nav: 제49장: 개발 환경 구축 — Android Studio와 첫 번째 프로젝트
toc: default
kind: chapter
---

### 제49장: 개발 환경 구축——Android Studio와 첫 프로젝트

{class="chapter-intro mb-4"}
일을 잘하려면 먼저 도구를 갈춰야 하죠. 이번 장에서는 '부엌'을 꾸며요: Android Studio를 설치하고, 에뮬레이터를 돌려 보고, 인생 첫 안드로이드 프로젝트를 만들고, 프로젝트 구조까지 풀어서 훑어 보는 거예요. 환경을 갖추고 나면 여러분이 쓴 코드가 누를 수 있는 버튼으로 변하는 순간을 처음 보게 될 거예요——이 순간을 평생 기억하는 사람이 많아요.

#### 1. Android Studio 설치

Android Studio는 구글 공식 통합 개발 환경(IDE)으로, 무료에 기능도 올인원이에요: 코드 작성, 화면 미리보기, 디버깅, 패키징까지 전부 여기에 들어 있어요. 설치는 네 단계예요:

1. 공식 사이트 developer.android.com/studio를 열어 최신 안정 버전을 내려받으세요(2026년 8월 기준 Narwhal 이후 버전, Windows/Mac/Linux 모두 있어요);
2. 설치 파일을 실행하고 '다음'만 계속 누르세요——설치 마법사가 Android SDK와 에뮬레이터 구성 요소를 자동으로 포함해 줘요;
3. 처음 실행할 때 안내에 따라 SDK 구성 요소를 내려받으세요(기본 선택 그대로 두면 돼요. 몇 분과 몇 GB의 공간이 필요할 수 있어요);
4. 끝나면 환영 화면이 보일 거예요——축하해요, '부엌'이 완성됐어요.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
주의: 하드웨어 요구 사항은 미리 알아 두기

{class="mt-1"}
Android Studio는 '메모리를 잡아먹는' 녀석이에요: 메모리 16GB부터 권해요(8GB도 돌아가지만 에뮬레이터를 띄우면 다소 버벅여요), 디스크는 20GB 이상 비워 두고, CPU가 가상화를 지원해야 해요(BIOS에서 VT-x/AMD-V 켜기). 컴퓨터가 정말 오래됐다면 에뮬레이터 대신 '실기기 디버깅'을 쓰면 돼요(이 장 4절에서 다룰게요). 오히려 더 매끄럽게 돌아가요.
:::

#### 2. 첫 프로젝트 만들기

환영 화면에서 New Project를 누르고 Empty Activity 템플릿(가장 깔끔한 초보용 템플릿)을 고른 뒤, 세 가지를 채우면 돼요:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">설정 항목</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">무엇을 채울까</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">설명</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">My First App</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">앱 이름. 휴대전화 홈 화면에 표시돼요</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Package name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example.myfirstapp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">전 세계에서 유일한 식별자. 관례는 '도메인 거꾸로 쓰기', 우선은 기본값 그대로</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minimum SDK</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API 26(Android 8.0)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">최소 지원 버전. 기기의 95% 이상을 커버</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
프로젝트 생성 때 채우는 세 가지

Finish를 누르면 Android Studio가 Gradle로 의존성을 자동 내려받고 프로젝트를 빌드해요(처음에는 몇 분 기다려야 하고, 그다음부터는 훨씬 빨라요). 빌드가 끝나면 실행 가능한 앱이 하나 생긴 거예요——아직 "Hello Android!" 한 줄만 보여줄 뿐이지만요.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
작은 팁: 패키지 이름의 내막

{class="mt-1"}
패키지 이름(package name)은 앱의 '주민등록번호' 같은 거예요. 전 세계에서 겹칠 수 없고, 출시한 뒤에는 바꿀 수 없어요. 개인 연습용으로는 com.example.xxx면 충분해요. 정식 제품은 자기 도메인을 거꾸로 쓴 이름(예: com.이름.앱이름)으로 바꿔야 해요. com.example 그대로 출시하지 마세요——스토어가 거부해요.
:::

#### 3. 실행하기: 에뮬레이터와 실기기

코드를 다 썼으면 돌려 볼 '휴대전화'가 필요해요. 선택지는 두 가지예요:

##### 1. 에뮬레이터(Emulator)

에뮬레이터는 컴퓨터 안에 안드로이드 휴대전화 한 대를 가상으로 만들어 내는 거예요. Android Studio에서 Device Manager → Create Device를 열고, 기기를 하나 고르고(Pixel 시리즈 추천) → 시스템 이미지를 고르고(Google APIs 포함) → 내려받고 → 실행하세요. 그다음 도구 모음의 초록색 삼각형 Run을 누르면, 몇 초 뒤 '휴대전화' 화면에 여러분의 앱이 나타나요.

##### 2. 실기기 디버깅(더 추천)

실기기는 언제나 가장 진짜에 가까운 테스트 환경이에요——스와이프 감촉, 실제 네트워크, 실제 센서는 에뮬레이터가 따라올 수 없죠. 안드로이드 실기기 디버깅은 아주 간단해요:

1. 휴대전화에서 [설정] → [휴대전화 정보]를 열고 '빌드 번호'를 7번 연속 눌러 '개발자 옵션'을 켜세요;
2. [개발자 옵션]에서 USB 디버깅을 켜세요;
3. 데이터 케이블로 컴퓨터에 연결하고, 휴대전화 팝업에서 'USB 디버깅 허용'을 선택하세요;
4. Android Studio로 돌아가면 도구 모음의 기기 드롭다운 목록에 휴대전화가 나타나요. Run을 누르세요.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
함정 주의보: USB 디버깅은 상시 켜 두지 않기

{class="mt-1"}
USB 디버깅은 컴퓨터에 '뒷문'을 열어 주는 것과 같아요. 공공장소에서 충전하거나 믿지 못할 컴퓨터에 연결할 때는 반드시 USB 디버깅을 꺼서 남이 이 경로로 여러분의 데이터를 읽지 못하게 하세요. 평소 개발할 때도 다 쓰면 바로 끄는 습관을 들이세요.
:::

#### 4. 프로젝트 구조 뜯어보기: 각 파일은 무슨 일을 할까

프로젝트를 처음 열면 왼쪽의 파일 트리가 어질어질 수 있어요. 놀라지 마세요. 일상 개발에서는 시간의 90%를 아래의 이것들만 다루는 데 쓰게 돼요:

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="300" viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="300" fill="#fafafa" rx="8"/>
      <text x="20" y="30" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ 프로젝트 루트</text>
      <rect x="30" y="45" width="540" height="230" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <text x="45" y="70" font-size="11" fill="#4f46e5" font-weight="bold">app/ ← 코드를 작성하는 곳</text>
      <rect x="60" y="82" width="240" height="178" fill="#eef2ff" rx="5"/>
      <text x="70" y="102" font-size="10" fill="#1e1b4b" font-weight="bold">src/main/</text>
      <text x="80" y="120" font-size="10" fill="#374151">├ java/…/MainActivity.kt  ← 로직 코드</text>
      <text x="80" y="138" font-size="10" fill="#374151">├ res/  ← 리소스(이미지, 문자, 색상)</text>
      <text x="80" y="156" font-size="10" fill="#374151">└ AndroidManifest.xml  ← 앱의 "주민등록부"</text>
      <text x="70" y="180" font-size="10" fill="#1e1b4b" font-weight="bold">build.gradle.kts</text>
      <text x="80" y="198" font-size="10" fill="#6b7280">의존 라이브러리 선언(SDK 버전, Compose 등)</text>
      <text x="70" y="222" font-size="10" fill="#1e1b4b" font-weight="bold">src/androidTest/와 test/</text>
      <text x="80" y="240" font-size="10" fill="#6b7280">자동화 테스트 코드(56장에서 사용)</text>
      <rect x="320" y="82" width="230" height="178" fill="#f0fdf4" rx="5"/>
      <text x="330" y="102" font-size="10" fill="#065f46" font-weight="bold">루트의 다른 파일들</text>
      <text x="340" y="122" font-size="10" fill="#374151">gradle/ + gradlew.bat  ← 빌드 스크립트</text>
      <text x="340" y="142" font-size="10" fill="#374151">settings.gradle.kts  ← 프로젝트 설정</text>
      <text x="340" y="162" font-size="10" fill="#6b7280">(초보의 구호: app/ 디렉터리만 만지고,</text>
      <text x="340" y="180" font-size="10" fill="#6b7280">나머지는 일단 "블랙박스"로 두고 함부로 만지지 않기)</text>
      <text x="340" y="208" font-size="10" fill="#9ca3af">.gitignore  ← 버전 관리 제외 목록</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
그림 2: 초보자가 꼭 알아야 할 프로젝트 구조(주문: app/ 폴더만 다루기)
:::

- MainActivity.kt: 앱의 '대문'이에요. 사용자가 아이콘을 누르면 가장 먼저 깨어나는 게 이 파일이죠. 지금 템플릿에서는 "Hello Android!"를 표시하는 일을 맡고 있어요.
- AndroidManifest.xml: 앱의 '주민등록부'예요——이 앱의 이름이 무엇인지, 아이콘은 무엇인지, 어떤 화면이 있는지, 어떤 권한(카메라, 위치 등)을 쓰는지 선언해요.
- res/ 폴더: 리소스 창고로, 이미지, 아이콘, 문자열, 색을 보관해요. 글자를 코드에 박아 넣지 않고 리소스 파일에 두는 건 안드로이드 개발의 좋은 습관이에요(언어 교체, 테마 교체가 모두 편해요).
- build.gradle.kts: 빌드 레시피예요——최소 지원 버전과 어떤 라이브러리(예: Compose)에 의존하는지 선언해요.

#### 5. 맛보기 실습: "Hello"를 여러분의 이름으로 바꾸기

MainActivity.kt를 열면 Compose 템플릿이 만들어 준 코드가 보여요. Text("Hello Android!") 줄을 찾아 따옴표 안의 글자를 여러분의 이름으로 바꾸세요. 예컨대 Text("안녕, 철수! 이건 내 첫 앱이야")처럼요. 그다음 Ctrl+R(Mac은 Cmd+R)을 눌러 다시 실행하세요. 몇 초 뒤 에뮬레이터에 여러분의 이름이 나타나요.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · MainActivity.kt(이 한 줄만 수정)</span><span class="dots">···</span>
:::

```
setContent {
    MyFirstAppTheme {
        Surface(modifier = Modifier.fillMaxSize()) {
            // ▼ 이곳을 자신의 문자로 바꾸기
            Text("안녕, 김철수! 이게 내 첫 앱이에요")
        }
    }
}
```
:::

축하해요, "코드 수정 → 컴파일 → 설치 → 실행"의 온전한 한 바퀴를 완주했어요. 이 반복이야말로 앞으로 매일의 개발 일상이에요. 잘 풀렸으니 이왕 하는 김에 다른 것도 바꿔 보세요: 글자 크기를 키우거나 색을 바꿔 보는 거예요——다음 장에서 이런 '마법'이 어디서 오는지 배우게 돼요.

#### 6. 자주 나오는 오류 응급처치: 초보자 첫 2주의 '응급실

환경 구축과 첫 빌드 단계에서는 아래 세 가지 오류를 만날 가능성이 커요. 놀라지 마세요. 모두 해독제가 있어요:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">오류 증상</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">흔한 원인</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">해독제</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle sync failed / 의존성 내려받기가 느림</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">저장소(리포지터리)에 네트워크 접근이 원활하지 않음</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle에 중국 내 미러 저장소를 설정하세요(알리바바 클라우드/텐센트 클라우드의 maven 미러). 'gradle 중국 미러'로 검색해서 그대로 따라 고치세요</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SDK 구성 요소 누락</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">설치할 때 SDK 내려받기를 건너뜀</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Settings → SDK Manager에서 빠진 플랫폼과 도구를 추가 설치</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">에뮬레이터 시작 실패 / 검은 화면</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">가상화 미사용, 이미지 손상</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BIOS에서 VT-x/AMD-V 켜기; 에뮬레이터를 지우고 다시 만들기; 또는 그냥 실기기 디버깅 사용</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
초보자 환경 오류 응급처치표

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
작은 팁: 오류 검색의 방법론

{class="mt-1"}
오류 메시지의 첫 줄이 가장 가치 있어요——그대로 복사해서 검색 엔진에 넣고 "android studio"라는 키워드를 붙이세요. '환경 설치가 안 돼요 어떡하죠' 같은 두루뭉술한 질문이 아니라 "Gradle sync failed: Could not resolve com.android.tools.build" 같은 구체적인 오류를 검색하는 거예요. 정확한 문제여야 정확한 답이 나와요.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
따라 해 봐요: '개발 의식감' 체크리스트 완성하기

{class="mt-1"}
① Android Studio를 설치하고 에뮬레이터를 돌려 보기; ② 실기기로 내 앱을 한 번 실행해 보고 스크린샷으로 남기기; ③ Hello 글자를 내 이름으로 바꾸기; ④ 프로젝트를 압축해서 백업해 두기. 이 네 가지를 마치면 SNS에서 이렇게 선언할 수 있어요: 나도 이제 안드로이드 개발자다(스크린샷이 증거).
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
이번 장 정리

- Android Studio = 공식 무료 IDE. 메모리 16GB + 디스크 20GB + 가상화 켜기를 권해요
- 새 프로젝트 3요소: 이름, 패키지 이름(전 세계 유일, com.example로 출시 금지), 최소 SDK(API 26부터)
- 두 가지 실행 방법: 에뮬레이터(컴퓨터 속 가상 휴대전화)와 실기기(USB 디버깅 켜기, 다 쓰면 끄기)
- 프로젝트 주문: app/ 폴더만 다루기——MainActivity.kt는 대문, Manifest는 주민등록부, res/는 리소스 창고
- 개발 일상 = 코드 수정 → Run → 결과 확인의 반복
:::
