---
id: di-wu-shi-er-zhang
num: 52
part: an-zhuo-kai-fa-pian
nav: 제52장: 4대 컴포넌트와 Activity 생명주기
toc: default
kind: chapter
---

### 제52장: 안드로이드 4대 컴포넌트와 Activity 생명주기

{class="chapter-intro mb-4"}
Compose가 앱의 "얼굴"이라면, 이번 장은 앱의 "뼈대" 이야기예요. 안드로이드 시스템에는 4대 기본 컴포넌트가 있고 모든 앱은 이것들로 조립돼요. 그중 가장 중요한 Activity에는 모든 안드로이드 개발자가 반드시 머리에 새겨 넣어야 할 "생명주기 그림"이 있죠. 이 장을 끝내면 "뒤로 나갔다 돌아왔을 뿐인데 왜 내 앱 상태가 사라졌을까?" 같은 오랜 난제를 이해하게 될 거예요.

#### 1. 4대 컴포넌트: 안드로이드의 "기둥과 보"

안드로이드는 각각 한 가지 일을 맡는 네 가지 기본 컴포넌트를 공식적으로 정의하고 있어요:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">컴포넌트</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">역할</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">비유하면</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activity</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">보이는 화면 하나</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">가게의 매장 앞 — 사용자가 볼 수 있고 만질 수 있어요</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Service</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">뒤에서 일하는 "보이지 않는 사람"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">창고 노동자 — 음악 재생, 파일 다운로드처럼 화면이 필요 없는 일을 해요</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BroadcastReceiver</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">시스템 브로드캐스트 수신</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">수위실 — "배터리가 다 떨어졌어요" "네트워크가 끊겼어요"를 알려 주는 확성기</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ContentProvider</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">앱 간 데이터 공유</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">공용 자료장 — 예를 들어 연락처를 다른 앱과 공유해요</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
안드로이드 4대 컴포넌트 한눈에 보기

초보 단계에서는 시간의 95%를 Activity와 씨름하며 보내요. Service와 BroadcastReceiver는 음악 재생이나 메시지 푸시를 만들 때 쓰고, ContentProvider는 가장 적게 써요(자주 쓰는 데이터는 시스템이 이미 감싸 뒀으니까요). 한 가지 더 주의하세요. 4대 컴포넌트는 모두 AndroidManifest.xml에 "주민등록"을 해야 해요. 등록하지 않으면 시스템이 찾지 못해요.

#### 2. Activity 생명주기: 안드로이드 개발의 첫 번째 "보물지도"

휴대폰의 앱은 언제든 끼어들 수 있어요. 전화가 오거나, 사용자가 위챗 답장하러 잠시 떠나거나, 시스템 메모리가 부족해 앱을 강제로 끝내 버리기도 하죠…… Activity의 일생은 바로 이 그림 위를 반복해 여행하는 거예요:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onCreate(탄생: 초기화)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onStart(보이기 시작)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onResume(포그라운드에서 상호작용 중)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onPause(일부 가려짐)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onStop(완전히 안 보임)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center">onDestroy(소멸)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">🔁 onRestart / onStart / onResume: 포그라운드 복귀 시 되돌아가는 경로</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
그림 4: Activity 생명주기(진행 방향: 윗줄은 탄생 → 아랫줄은 퇴장, 돌아올 때는 왔던 길로 되돌아감)
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">콜백</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">언제 호출되나</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">대표적인 용도</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onCreate</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activity가 생성될 때(한 번)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">화면 로드, 데이터 초기화</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStart</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">화면이 보이기 시작할 때</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">가벼운 로직 시작</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onResume</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">포커스를 얻고 상호작용 가능할 때</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">애니메이션 시작, 재생 재개</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onPause</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">일부 가려지거나 화면이 전환되는 순간</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">애니메이션 일시정지, 임시 저장</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStop</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">완전히 보이지 않을 때</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">무거운 자원 해제, 다운로드 일시정지</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onDestroy</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">소멸되기 전</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">마지막 정리</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
여섯 가지 생명주기 콜백의 대표적인 용도

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
주의: 화면 회전은 Activity를 "죽여요"

{class="mt-1"}
초보자의 가장 고전적인 사고 현장: 앱 화면을 한 번 돌렸을 뿐인데 입력창의 글자가 모두 사라져요. 원인: 화면을 회전하면 기본적으로 Activity가 소멸 후 재생성되거든요(onDestroy → onCreate를 한 바퀴 돌아요). 해법: rememberSaveable로 상태를 저장하세요(Compose에서 remember를 대체해요). 재생성될 때 값이 자동으로 복원돼요. 6장과 7장에서 계속 쓰게 될 거예요.
:::

#### 3. Intent: 앱 안팎을 오가는 "차표"

Intent(인텐트)는 컴포넌트끼리 소통하는 "차표"예요. 한 화면에서 다른 화면으로 넘어가거나, 브라우저를 열거나, 카메라를 띄우려면 모두 "표를 끊고 탑승"해야 해요:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Intent로 화면 이동</span><span class="dots">···</span>
:::

```
// 방법 1: 명시적 Intent — 어떤 화면으로 갈지 직접 지정
val intent = Intent(this, DetailActivity::class.java)
intent.putExtra("name", 김철수)     // 차에 "짐"(데이터)을 싣는 셈
startActivity(intent)

// 방법 2: 암시적 Intent — 무엇을 할지만 말하면 시스템이 처리할 주체를 찾아요
val web = Intent(Intent.ACTION_VIEW, Uri.parse("https://developer.android.com"))
startActivity(web)   // 시스템이 브라우저를 열거나 선택하게 해요
```
:::

두 방식은 쓰임이 달라요. 명시적(explicit)은 내 앱 안의 화면 전환에, 암시적(implicit)은 시스템이나 다른 앱의 기능을 호출할 때 써요(웹페이지 열기, 전화 걸기, 공유하기). Compose 프로젝트에서는 Composable 안에서 LocalContext.current로 Context를 얻으면 startActivity를 쓸 수 있어요.

#### 4. 여러 화면과 내비게이션

실제 앱에는 화면이 여러 개 있어요. Compose에서 공식 추천하는 내비게이션 방식은 Navigation Compose예요(의존성 라이브러리 androidx.navigation):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Navigation Compose 뼈대</span><span class="dots">···</span>
:::

```
val navController = rememberNavController()

NavHost(navController, startDestination = "home") {
    composable("home") { HomeScreen(navController) }
    composable("detail/{name}") { entry ->
        val name = entry.arguments?.getString("name")
        DetailScreen(name ?: "알 수 없음")
    }
}

// 화면 안에서 이동:
navController.navigate("detail/김철수")     // 인자 전달
navController.popBackStack()              // 이전 화면으로 돌아가기
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
팁: 화면이 많아지면 어떻게 할까요?

{class="mt-1"}
프로젝트가 커지면 모든 화면 라우트를 한 파일(예: AppNavGraph.kt)에 모아 통일해서 관리하세요. "어디로 이동할까"라는 로직이 여러 화면에 흩어지게 두지 말라는 뜻이에요. "돌아가기만 하는 코드"에서 "유지보수할 수 있는 코드"로 가는 첫걸음이에요.
:::

#### 5. 곁가지로 알아두기: Fragment란 무엇일까(그리고 이 책에서 다루지 않은 이유)

오래된 튜토리얼을 보다 보면 반드시 Fragment를 만나게 돼요. Activity 안에 들어가는 "재사용 가능한 화면 조각"으로, 구식 다중 화면 아키텍처의 절대 주인공이었죠. 하지만 Compose 시대에는 화면을 Composable 함수 + Navigation 라우트로 바로 만들면 충분하고, 공식적으로도 Fragment의 비중이 줄었어요. 그래서 이 책은 본줄기에 넣지 않았어요.

여러분을 위한 조언: 새 프로젝트에서는 Fragment를 굳이 쓰지 마세요. 다만 오래된 코드를 읽거나 면접에서 물어볼 때 "Activity에 들어가는 화면 조각"이라는 것만 알면 돼요. 학습 자료는 언제나 2023년 이후 것을 먼저 고르세요. 안드로이드 기술 스택은 생각보다 훨씬 빨리 낡아가니까요.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
직접 해 보기: 카운터에 "기억력" 달기

{class="mt-1"}
51장의 카운터를 개조해 봐요. ① remember를 rememberSaveable로 바꾸고 화면을 회전해도 숫자가 남아 있는지 확인하세요. ② "정보" 버튼을 추가해 Navigation으로 두 번째 화면으로 이동해 버전 번호를 보여 주세요. ③ 두 화면의 onCreate/onPause에 로그를 남기고(Log.d) Logcat으로 생명주기 호출 순서를 관찰하세요. 이 세 단계를 마치면 생명주기가 더 이상 종이 위의 이론이 아니에요.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
이번 장 정리

- 4대 컴포넌트: Activity(매장 얼굴), Service(뒷일 담당), BroadcastReceiver(확성기), ContentProvider(자료장)
- 생명주기 6대 콜백: onCreate → onStart → onResume → onPause → onStop → onDestroy
- 화면 회전은 Activity를 소멸 후 재생성해요: rememberSaveable로 상태를 지키세요
- Intent는 "차표": 명시적은 내 앱 화면 이동, 암시적은 시스템 기능 호출
- 여러 화면은 Navigation Compose로: NavHost + composable 라우트
:::
