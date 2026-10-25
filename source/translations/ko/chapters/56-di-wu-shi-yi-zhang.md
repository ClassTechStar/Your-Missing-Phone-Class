---
id: di-wu-shi-yi-zhang
num: 51
part: an-zhuo-kai-fa-pian
nav: 제51장: UI 개발 — Jetpack Compose 입문
toc: default
kind: chapter
---

### 제51장: 화면 개발——Jetpack Compose 입문

{class="chapter-intro mb-4"}
화면은 사용자가 보는 모든 것이에요. Compose가 나오기 전에는 안드로이드 화면을 XML로 썼어요——빈칸 채우기 문제처럼 번거로웠죠. 2021년 구글이 Jetpack Compose를 내놓았어요: Kotlin 코드로 화면을 바로 '그리는' 방식으로, 보이는 대로 얻어지고 코드 한 줄을 바꾸면 미리보기가 즉시 새로 고쳐져요. 2026년 현재 Compose는 새 프로젝트의 절대 주류예요. 이번 장에서는 '그림 그리기'를 배워 봐요.

#### 1. Compose의 발상: 화면이 곧 함수

Compose의 핵심 발상을 한 문장으로 말하면: 화면 = 함수예요. 화면에 표시될 수 있는 모든 것(글자, 버튼, 이미지)은 각각 '컴포저블 함수'(Composable)이고, @Composable로 표시해요. 이것들을 블록처럼 중첩하면 그게 화면이에요.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 첫 Compose 화면</span><span class="dots">···</span>
:::

```
@Composable
fun Greeting(name: String) {
    Text(text = "안녕, $name!")     // "글자 블록" 하나
}

// 중첩 조합: 큰 블록 안에 작은 블록
@Composable
fun HomeScreen() {
    Column {                          // 세로 배치
        Greeting(name = 김철수)
        Greeting(name = 이영희)
        Button(onClick = { /* 클릭 시 동작 */ }) {
            Text("눌러 보세요")
        }
    }
}
```
:::

@Composable이라는 '모자'에 주목하세요——컴파일러에게 '이것은 화면 블록입니다'라고 알려 주는 표시예요. 블록은 무한히 중첩할 수 있고, 이게 Compose의 비밀 전부예요.

#### 2. 기본 컴포넌트: 글자, 버튼, 입력란, 이미지

Compose의 컴포넌트는 '블록 조각'이에요. 가장 흔한 네 가지는:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">컴포넌트</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">하는 일</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">필수 매개변수</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">글자 표시</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">text(표시할 글자)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">버튼</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onClick(클릭 콜백)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">입력란</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">value, onValueChange(입력 변화 콜백)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">이미지 표시</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">painter(이미지 리소스)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Compose의 네 가지 기본 컴포넌트

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 기본 컴포넌트 예시</span><span class="dots">···</span>
:::

```
@Composable
fun BasicWidgets() {
    Column {
        Text(text = "이것은 문자예요")
        Button(onClick = { println("클릭됨") }) {
            Text("버튼")
        }
        var input by remember { mutableStateOf("") }
        TextField(
            value = input,
            onValueChange = { input = it },
            label = { Text("무언가를 입력해 보세요") }
        )
    }
}
```
:::

입력란 예문 두 줄에 remember { mutableStateOf("") }가 등장했어요——이게 바로 Compose의 '상태' 마법이에요. 이 장 5절에서 자세히 다룰게요. 지금은 얼굴만 익혀 두세요.

#### 3. 레이아웃 3형제: Column, Row, Box

컴포넌트는 생겼는데 어떻게 배치할까요? 세 가지 '상자'를 기억하세요:

- Column: 세로로 늘어 놓아요(받으러 줄 서듯);
- Row: 가로로 늘어 놓아요(나란히 앉듯);
- Box: 겹쳐 놓아요(카드를 포개 놓듯. 모서리 배지, 오버레이에 적합해요).

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 레이아웃 3형제</span><span class="dots">···</span>
:::

```
Column {
    Text("첫 줄")
    Row {
        Text("왼쪽")
        Text("오른쪽")
    }
    Box {
        Text("아래층")
        Text("그 위에 겹치는 배지")
    }
}
```
:::

레이아웃을 더 예쁘게 만들고 싶나요? 컴포넌트에 Modifier(수식어)를 붙이세요——블록에 '화장을 시키는' 것과 같아요:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Modifier 자주 쓰는 기술</span><span class="dots">···</span>
:::

```
Text(
    text = "예쁜 문자",
    modifier = Modifier
        .padding(16.dp)          // 사방 여백
        .fillMaxWidth()          // 가로를 가득 채우기
        .background(Color.Blue)  // 배경색
        .clickable { /* 클릭 */ }// 클릭 가능
)
// 체이닝 호출: 하나씩 이어서, 순서에 의미가 있어요(padding 먼저, 배경 나중 — 배경은 여백을 포함하지 않아요)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
주의: Modifier의 순서가 중요해요

{class="mt-1"}
padding(16.dp).background(Blue)와 background(Blue).padding(16.dp)는 결과가 달라요——앞쪽은 '먼저 여백을 두고 다음에 색칠'(배경에 여백이 포함되지 않음)이고, 뒤쪽은 '먼저 색칠하고 다음에 여백'(배경에 여백이 포함됨)이에요. 초보자가 가장 쉽게 '묘한 흰 테두리'를 그리게 되는 부분이에요. 확실하지 않으면 순서를 바꿔 보세요. 미리보기가 곧바로 답을 알려 줄 거예요.
:::

#### 4. 상태: 화면에 '생명' 불어넣기

정적인 화면은 재미없어요. 버튼을 누르면 숫자가 +1 되고, 입력란에 글자를 쓸 수 있게 하려면 상태(State)가 필요해요. Compose의 규칙: 화면은 언제나 상태를 충실하게 반영하고, 상태가 바뀌면 화면이 자동으로 다시 그려져요.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 상태: 클릭 카운터</span><span class="dots">···</span>
:::

```
@Composable
fun Counter() {
    // remember + mutableStateOf: 변하는 값을 기억
    var count by remember { mutableStateOf(0) }

    Column {
        Text(text = "$count번 눌렀어요")
        Button(onClick = { count++ }) {   // 상태 변경
            Text("눌러 보세요 +1")                // 화면이 자동으로 새로 고침돼요
        }
    }
}
```
:::

세 줄의 코드로 살아 움직이는 카운터가 완성돼요. 이게 Compose가 옛 방식보다 시원한 점이에요: 화면을 손으로 '새로 고칠' 필요 없이, 데이터만 바꾸면 돼요. 핵심 함수 두 개를 기억하세요: remember(화면이 재구성될 때 값이 지워지지 않게 함)와 mutableStateOf(Compose에게 '이 값이 바뀌면 다시 그려야 한다'고 알려 줌).

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> 사용자 클릭</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> 상태 변경(count++)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> Compose가 변화를 감지</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> 화면 자동 다시 그리기(리컴포지션)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
그림 3: Compose의 '상태 → 화면' 단방향 데이터 흐름
:::

#### 5. 테마와 다크 모드: 한 번 설정, 전체 적용

템플릿 프로젝트의 MyFirstAppTheme { ... }가 바로 테마예요. Material 3 디자인 규격을 바탕으로 색, 글꼴, 모양을 한꺼번에 관리해 줘요. 다크 모드를 지원하는 건 세 단계면 충분해요:

1. 테마에 밝은/어두운 두 벌의 색 배합을 정의해 두기(템플릿이 ColorScheme을 자동으로 만들어 줘요);
2. 시스템이 다크 모드로 바뀌면 isSystemInDarkTheme()가 자동으로 판단하고;
3. 색 값을 코드에 박아 넣지 말고 테마가 제공하는 색(예: MaterialTheme.colorScheme.primary)을 쓰기.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
팁: Material 3 동적 색상 추출

{class="mt-1"}
안드로이드 12부터 도입된 "Material You"는 앱이 사용자의 배경화면에서 색상을 추출하게 해 줘요. Compose 템플릿은 기본으로 이를 지원하죠(dynamicColor). 여러분의 앱은 사용자마다 다른 휴대폰에서 "자동으로 옷을 갈아입는" 셈이에요. 이것이 바로 현대 안드로이드의 낭만이에요.
:::

#### 6. 미리보기, 애니메이션, 실시간 편집: Compose의 "치트키"

개발 경험을 바꿔 주는 Compose의 "치트키" 세 가지, 한번 쓰면 원래대로 못 돌아가요:

- @Preview 미리보기: Composable에 @Preview 어노테이션을 붙이면 Android Studio 오른쪽에 화면이 즉시 렌더링돼요. 코드를 고치면 그대로 보이니 매번 휴대폰에 설치할 필요가 없죠;
- 실시간 편집(Live Edit): 2026년 Android Studio는 에뮬레이터/실제 기기에서 일부 변경 사항을 "핫 업데이트"할 수 있어요. 글자 색 바꾸기 같은 작은 수정은 기기에서 순식간에 반영되죠;
- 애니메이션 API: animateFloatAsState, AnimatedVisibility는 몇 줄의 코드로 요소를 부드럽게 전환하게 해 줘요. "고급스러운 느낌"은 대개 이 몇십 줄의 차이에서 나와요.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 10분이면 배우는 애니메이션</span><span class="dots">···</span>
:::

```
@Composable
fun AnimatedBox() {
    var big by remember { mutableStateOf(false) }
    // 값이 바뀌면 목표값으로 자동으로 부드럽게 전환
    val size by animateDpAsState(if (big) 120.dp else 60.dp)

    Box(Modifier
        .size(size)
        .background(MaterialTheme.colorScheme.primary)
        .clickable { big = !big }
    )
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
팁: 기능 먼저, 애니메이션은 나중에

{class="mt-1"}
초보자가 자주 저지르는 실수가 "화면을 제대로 만들기도 전에 애니메이션부터 붙잡는 것"이에요. 먼저 기능이 돌아가게 만들고, 마지막에 애니메이션을 한꺼번에 추가하세요. 이것이 "단순함이 최고" 원칙이기도 해요. 애니메이션은 화룡점정이고, 기능은 가뭄의 단비예요.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
직접 해 보기: "기분 버튼" 만들기

{class="mt-1"}
템플릿 프로젝트를 기분 전환기로 바꿔 봐요. 버튼 하나를 누를 때마다 😀기쁨 → 😢슬픔 → 😡화남 사이를 순환하며 바뀌고, 글자와 배경색도 따라 변하게 하는 거예요. 힌트: when으로 상태에 따라 문구와 색을 고르세요. 다 만들면 친구에게 보내서 "어라? 너 앱을 만들 줄 알아?"라는 첫 반응을 얻어 보세요.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
이번 장 정리

- Compose 사고방식: 화면 = @Composable 함수, 블록 쌓듯 중첩
- 네 가지 기본 요소: Text / Button / TextField / Image
- 레이아웃 3종 세트: Column은 세로, Row는 가로, Box는 겹쳐 쌓기
- Modifier 체이닝 "메이크업": padding, fillMaxWidth, background, clickable — 순서에 의미가 있어요
- 상태가 영혼: remember + mutableStateOf, 데이터를 바꾸면 화면이 자동으로 다시 그려져요
- 테마는 Material 3 + 동적 색상 추출, 다크 모드는 한 번 설정하면 전체에 적용돼요
:::
