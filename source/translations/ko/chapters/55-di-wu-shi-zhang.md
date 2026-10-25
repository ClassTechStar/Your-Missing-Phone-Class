---
id: di-wu-shi-zhang
num: 50
part: an-zhuo-kai-fa-pian
nav: 제50장: Kotlin 빠르게 익히기 — 안드로이드 개발의 첫 번째 언어
toc: default
kind: chapter
---

### 제50장: Kotlin 빠르게 시작하기——안드로이드 개발의 첫 언어

{class="chapter-intro mb-4"}
이번 장에서는 본격적으로 언어를 배워요. 긴장하지 마세요——Kotlin은 '초보자에게 친절한' 언어로 유명하고, 문법책을 통 외울 필요도 없어요: 문법의 20%만 먼저 잡으면 일상적인 코드의 80%는 읽고 쓸 수 있어요. 나머지는 프로젝트를 하면서 찾아 보면 돼요. 우리의 학습 원칙을 기억하세요: 이해 > 암기, 활용 > 정통.

#### 1. 변수와 타입: 데이터에 이름 붙이기

프로그램이란 '데이터 + 로직'이에요. 변수는 데이터에 이름을 붙여 저장해 두는 거예요. Kotlin에는 두 가지 선언 방식이 있어요:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 변수</span><span class="dots">···</span>
:::

```
val name = 김철수        // val: 읽기 전용 변수(기본으로 추천)
var age = 18             // var: 변경 가능한 변수(나중에 또 바꿀 수 있어요)

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var는 바꿀 수 있어요
// name = 이영희         // <i class="fas fa-times-circle mr-1"></i> val은 바꿀 수 없어요, 컴파일 오류

val score: Int = 100     // 타입을 직접 쓸 수도 있어요
val pi = 3.14            // 생략해도 자동으로 추론해요
```
:::

자주 쓰는 타입은 몇 가지 안 돼요. 표 하나로 기억하세요:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">타입</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">담는 것</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">예시</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">정수</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">소수</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">문자</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"안녕하세요"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Boolean</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">참/거짓</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List&lt; T&gt;</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">데이터 묶음</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">listOf(1, 2, 3)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kotlin 자주 쓰는 기본 타입

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
작은 팁: val 우선 원칙

{class="mt-1"}
Kotlin 커뮤니티의 철칙: 기본은 val, 정말 필요할 때만 var. val을 쓸 수 있는 곳에 var를 쓰면 IDE가 노란 글자로 경고해 줘요. 이 습관 하나로 '변수가 뜻밖에 변경되는' 부류의 버그를 크게 줄일 수 있어요——코드에서 변하는 것이 적을수록 추론이 쉬워지거든요.
:::

#### 2. 함수: 로직을 '버튼'으로 포장하기

함수는 이름이 붙은 로직 한 덩어리예요. 리모컨의 버튼처럼——누르면(호출하면) 일련의 동작이 실행돼요. Kotlin에서는 fun으로 선언해요:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 함수</span><span class="dots">···</span>
:::

```
fun greet(name: String): String {
    return "안녕, $name!"     // $ 기호가 변수를 문자열에 끼워 넣어요
}

println(greet(김철수))        // 출력: 안녕, 김철수!

// 한 줄 함수는 식으로 간단히 쓸 수 있어요
fun add(a: Int, b: Int) = a + b

println(add(3, 5))            // 출력: 8
```
:::

포인트 몇 가지: 매개변수는 괄호 안에 써요(이름이 앞, 타입이 뒤, 콜론으로 구분). 반환 타입은 괄호 뒤에 써요. 문자열 템플릿 $변수명은 Kotlin의 간판급 편의 기능이에요——Java처럼 "문자열 + 변수"를 이리저리 이어 붙일 필요가 없거든요.

#### 3. 조건과 반복: 프로그램에게 '생각' 가르치기

프로그램의 지능은 두 가지에서 나와요: 판단할 줄 아는 것(if/when)과 반복할 줄 아는 것(for/while)이에요.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 조건과 반복</span><span class="dots">···</span>
:::

```
// 판단: if / else
val age = 17
if (age >= 18) {
    println("어른")
} else {
    println("미성년자")
}

// 다분기: when(switch보다 백배 편해요)
val score = 85
val level = when {
    score >= 90 -> "우수"
    score >= 60 -> "보통"
    else -> "분발하세요!"
}

// 반복: for 루프
val fruits = listOf("사과", "바나나", "오렌지")
for (fruit in fruits) {
    println("$fruit 좋아해요")
}
```
:::

when은 Kotlin에서 가장 많이 쓰는 다중 분기 표현이에요. 안드로이드 개발에서는 매일 쓰게 될 거예요(예: 상태에 따라 다른 화면을 보여주기).

#### 4. 널 안전성: Kotlin의 '생명 부적

Java 시대의 가장 유명한 버그는 NullPointerException(널 포인터 예외)예요——프로그램이 '아무것도 없는' 것에 접근하다가 그대로 터지죠. 통계상 안드로이드 크래시 순위의 단골 1위거든요. Kotlin은 언어 차원에서 이 문제를 해결했어요: 기본적으로 널 값을 허용하지 않아요.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 널 안전성</span><span class="dots">···</span>
:::

```
var name: String = 김철수   // 일반 타입: 절대 null이면 안 돼요
// name = null                // <i class="fas fa-times-circle mr-1"></i> 컴파일 오류가 바로 잡아 줘요

var nickname: String? = null // 물음표 하나: null 허용
nickname = "순이"

// 널 가능 타입을 쓸 때는 반드시 안전하게 다뤄야 해요:
println(nickname?.length)    // 안전 호출: null이면 null을 돌려주고 크래시 없음
val len = nickname?.length ?: 0   // Elvis 연산자: null일 때 기본값
println(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
주의: ?와 ?:는 헷갈리지 않기

{class="mt-1"}
String?는 '널 허용'이고, a ?: b는 'a가 널이면 b를 쓴다'는 뜻이에요(생김새가 엘비스 프레슬리 헤어스타일 같아서 Elvis 연산자라고 불러요). 코드를 막 쓰기 시작했을 때 컴파일러가 'null 관련 오류'를 내면, 십중팔구는 널이 될 수 있는 타입 처리를 잊은 거예요——이건 언어가 여러분을 보호하고 있는 거랍니다.
:::

#### 5. 클래스와 객체: '부품'을 찍어 내는 틀

클래스는 객체의 '틀'이고, 객체는 클래스의 '완성품'이에요. 안드로이드의 모든 것——화면, 버튼, 데이터——가 전부 객체죠. Kotlin에는 data class(데이터 클래스)라는 신기한 도구가 있는데, '데이터를 담는' 전용으로, 한 줄이면 Java의 수십 줄을 대신해요:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 클래스와 데이터 클래스</span><span class="dots">···</span>
:::

```
// 일반 클래스: 틀
class Dog(val name: String) {
    fun bark() = println("$name 멍멍!")
}

val dog = Dog("바둑이")      // 객체 생성
dog.bark()                 // 바둑이: 멍멍!

// data class: 데이터를 담는 상자(equals/copy 등 자동 제공)
data class User(val id: Int, val name: String, val email: String)

val me = User(1, 김철수, "zhangsan@example.com")
val twin = me.copy(name = "김철수2")   // 복사하고 한 필드만 변경
```
:::

나중에 가계부를 만들면 한 건의 기록이 곧 data class가 돼요: data class Record(val amount: Double, val category: String, val date: String). 보세요, 이제 실제 프로젝트의 코드 구조를 쓸 수 있게 됐어요.

#### 6. lambda와 고차 함수: Kotlin의 '문법 설탕

안드로이드 코드에서 { ... } 같은 '이름 없는 함수'를 매일 보게 되는데, 이걸 lambda(익명 함수)라고 불러요. Button의 onClick = { count++ }가 바로 lambda예요——'클릭하면 무엇을 할지' 한 덩어리로 포장해서 버튼에게 넘겨 주는 거죠.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · lambda 첫 경험</span><span class="dots">···</span>
:::

```
// 일반 방식: 이름 있는 함수를 정의해 전달
fun double(x: Int) = x * 2
val result = listOf(1, 2, 3).map(::double)

// lambda 방식: 그 자리에서 정의, 가볍고 직접적
val result2 = listOf(1, 2, 3).map { it * 2 }   // it = 현재 원소

// 필터 + 변환 연계(실제 프로젝트에서 아주 흔함)
val bills = listOf(12.5, 88.0, 5.0, 200.0)
val bigBills = bills.filter { it > 50 }.sorted()
// [88.0, 200.0] — "50을 넘는 청구서, 정렬 완료"
```
:::

자주 쓰는 '컬렉션 연계기' 몇 가지를 기억하세요: filter(거르기), map(바꾸기), sorted(정렬), sum(더하기). 앞으로 리스트 처리의 90%는 이 네 가지의 조합이에요. Kotlin의 철학은 이거예요: 한 문장으로 설명할 수 있는 로직을 다섯 문장으로 쓰지 않는다.

#### 7. 왕초보를 위한 문법 빠른 참조 카드

모든 문법을 하루 만에 외우려고 하지 마세요. 이 카드를 저장해 두고 코드를 쓸 때 찾아 보면, 두 주 뒤에는 저절로 익숙해져요:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">하려는 일</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">쓰는 법</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">읽기 전용 변수 정의</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">val x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">변경 가능한 변수 정의</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">함수 정의</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">fun 이름(매개변수): 반환 타입 { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">판단</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if (조건) {...} else {...}</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">다중 분기</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">when { 조건 -> 결과 }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">순회</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for (x in 리스트) { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">문자열 연결</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"안녕, $name"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">널 처리</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">x?.length ?: 0</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">데이터 클래스 정의</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">data class X(val a: Int, val b: String)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kotlin 문법 빠른 참조 카드(초보용)

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
따라 해 봐요: 아무것도 설치하지 않고 Kotlin 10분 맛보기

{class="mt-1"}
브라우저에서 play.kotlinlang.org(Kotlin 공식 온라인 연습장)를 열고, 이번 장의 코드를 하나씩 붙여 넣어 실행해 보세요. 숫자와 글자를 바꿔 가며 출력이 어떻게 달라지는지 보는 거예요. 이 '놀고 나서 배우는' 10분이 51장에 들어설 때 여러분을 두 배 편하게 해 줄 거예요.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
이번 장 정리

- val 우선, var는 신중하게. 타입은 자동 추론도 되고, 콜론 뒤에 직접 선언해도 돼요
- 함수 = 포장한 로직. 문자열 템플릿 $는 간판급 편의 기능
- if/when으로 판단, for로 반복. when은 안드로이드 개발의 '만능 선수'예요
- 널 안전성은 Kotlin의 생명 부적: 일반 타입은 null을 거부하고, 널 가능 타입은 ? / ?:로 반드시 처리
- data class는 데이터를 담는 상자. 필드 하나에 한 줄, 실제 프로젝트에서 매일 써요
- 20%의 문법으로 80%의 일을: 먼저 쓸 줄 알게 되고, 그다음에 정통하기
:::
