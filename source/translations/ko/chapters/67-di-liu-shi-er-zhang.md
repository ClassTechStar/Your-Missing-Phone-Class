---
id: di-liu-shi-er-zhang
num: 62
part: ios-kai-fa-pian
nav: 제62장: UI 개발 — SwiftUI 입문
toc: default
kind: chapter
---

### 제62장: 화면 개발 — SwiftUI 입문

{class="chapter-intro mb-4"}
화면은 사용자가 보는 모든 것이에요. SwiftUI는 애플이 2019년에 내놓은 선언형 UI 프레임워크예요. 화면이 어떻게 생겼는지 '선언'만 하면 시스템이 렌더링, 다크 모드 대응, 각종 화면 크기 대응을 알아서 해 줘요. 2026년 현재 SwiftUI는 새 프로젝트의 절대 주류예요. 이 장에서는 '그림 그리기'를 배워요.

#### 1. SwiftUI의 사상: 선언형이지 명령형이 아니다

옛 방식 화면 개발은 '명령형'이에요. 시스템에게 '버튼 만들기 → (20,30)에 놓기 → 색상 설정'이라고 한 단계씩 지시하죠. SwiftUI는 '선언형'이에요. 여러분은 '화면에 "눌러 보세요"라고 적힌 빨간 버튼이 있다'고 직접 서술만 하고, 어떻게 그릴지 언제 다시 그릴지는 시스템이 알아서 신경 써요.

::: div .code-block
:::inline div .code-head
<span>SWIFT · 첫 SwiftUI 뷰</span><span class="dots">···</span>
:::

```
import SwiftUI

struct ContentView: View {
    var body: some View {      // body: "화면이 어떻게 생겼는지"를 기술
        VStack {               // 세로 배치
            Text("안녕, 세상!")
                .font(.largeTitle)      // 수식어: 큰 제목
            Button("눌러 보세요") {
                print("클릭됨")
            }
            .buttonStyle(.borderedProminent)  // 파란색 솔리드 버튼
        }
        .padding()
    }
}
```
:::

핵심: 뷰 = View 프로토콜을 채택하는 구조체, body 프로퍼티가 화면을 서술, .수정자() 체인으로 '화장'하기. 이것이 SwiftUI의 전체 기본판이에요.

#### 2. 기본 뷰: 텍스트, 버튼, 입력창, 이미지

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">뷰</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">하는 일</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">예시</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">텍스트 표시</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text("안녕하세요")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">버튼</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button("눌러 보세요") { 동작 }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">입력창</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField("힌트", text: $텍스트)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">이미지 표시</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Image(systemName: "star.fill")</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
SwiftUI의 네 가지 기본 뷰

Image(systemName:)에 주목하세요. 애플이 SF Symbols 아이콘 라이브러리(수천 개의 무료 아이콘)를 내장하고 있어서 "star.fill" 같은 이름만으로 꽉 찬 별 하나를 바로 표시할 수 있어요. iOS 개발의 숨은 혜택이에요. 화면을 만들 때 아이콘 소재를 거의 찾을 필요가 없거든요.

#### 3. 레이아웃 3종 세트: VStack, HStack, ZStack

- VStack: 세로로 나열(식당 줄 서듯)
- HStack: 가로로 나열(나란히 앉듯)
- ZStack: 겹쳐 놓기(카드를 포개 놓듯, 배지나 오버레이에 적합)

::: div .code-block
:::inline div .code-head
<span>SWIFT · 레이아웃 3형제 + 자주 쓰는 수식어</span><span class="dots">···</span>
:::

```
VStack(alignment: .leading, spacing: 12) {
    HStack {
        Text("청구서")
        Spacer()                 // 탄성 공간: 오른쪽을 끝까지 밀어냄
        Text("-25.5위안").foregroundColor(.red)
    }
    Divider()                    // 구분선
    Text("메모: 점심")
}
.padding(16)                     // 사방 여백
.background(Color(.systemGray6)) // 옅은 회색 배경
.cornerRadius(12)                // 둥근 모서리

// 수식어 순서에 의미가 있어요: padding 먼저, background 나중 — 배경은 여백을 포함하지 않아요
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
주의: 수정자 순서가 중요해요

{class="mt-1"}
padding(16).background(회색)과 background(회색).padding(16)은 결과가 달라요. 전자는 '먼저 여백 두고 나중에 색칠'(배경에 여백 미포함), 후자는 '먼저 색칠하고 나중에 여백'(배경에 여백 포함)이에요. 초보자가 가장 흔히 겪는 '묘한 하얀 여백'이 모두 여기서 나와요. 확실하지 않으면 순서를 바꿔 보세요. 미리보기가 바로 답을 알려 줘요.
:::

#### 4. 상태와 바인딩: 화면을 '살아 있게' 만들기

정적인 화면은 재미없죠. SwiftUI의 규칙: 화면은 언제나 상태를 충실히 반영하고, 상태가 바뀌면 화면이 자동으로 다시 그려져요.

::: div .code-block
:::inline div .code-head
<span>SWIFT · @State 카운터</span><span class="dots">···</span>
:::

```
struct CounterView: View {
    @State private var count = 0   // @State: 이 값이 바뀌면 다시 그려요

    var body: some View {
        VStack {
            Text("\(count)번 눌렀어요")
            Button("눌러 보세요 +1") {
                count += 1          // 상태 변경, 화면 자동 새로 고침
            }
        }
    }
}
```
:::

입력창에는 '양방향 바인딩'이 필요해요. $ 기호가 '값과 수정 권한'을 함께 넘겨 줘요.

::: div .code-block
:::inline div .code-head
<span>SWIFT · @Binding 양방향 바인딩</span><span class="dots">···</span>
:::

```
struct InputView: View {
    @State private var text = ""

    var body: some View {
        TextField("무언가를 입력해 보세요", text: $text)  // $ 양방향 바인딩
            .textFieldStyle(.roundedBorder)
        Text("입력한 내용: \(text)")   // 입력하는 즉시 갱신
    }
}
```
:::

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> 사용자 조작</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> 상태 변경(count += 1)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> SwiftUI가 변화를 감지</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> 화면 자동 다시 그리기(body 재계산)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
그림 3: SwiftUI의 '상태 → 화면' 단방향 데이터 흐름
:::

#### 5. 미리보기, 테마와 애니메이션: SwiftUI의 '치트키'

- #Preview 매크로: 파일 맨 아래에 #Preview { ContentView() }를 추가하면 오른쪽 캔버스에 실시간으로 렌더링돼요. 코드를 고치면 보는 대로 반영되죠.
- 다크 모드는 공짜예요: 색을 하드코딩하지 말고 시스템 색상(Color(.systemGray6), .primary)을 쓰면 다크 모드가 자동으로 맞춰져요. 한 줄 더 쓸 필요가 없죠.
- 애니메이션은 한 줄이면 끝: withAnimation { count += 1 } 또는 뷰에 .animation(.default, value: count)를 추가하면 전환이 매끄러워요.

::: div .code-block
:::inline div .code-head
<span>SWIFT · 10분이면 배우는 애니메이션</span><span class="dots">···</span>
:::

```
struct AnimatedHeartView: View {
    @State private var liked = false

    var body: some View {
        Button {
            withAnimation(.spring(duration: 0.4)) {
                liked.toggle()
            }
        } label: {
            Image(systemName: liked ? "heart.fill" : "heart")
                .font(.system(size: 48))
                .foregroundColor(liked ? .red : .gray)
                .scaleEffect(liked ? 1.3 : 1.0)
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
팁: 기능 먼저, 애니메이션은 나중에

{class="mt-1"}
초보자가 흔히 저지르는 실수는 '화면이 아직 제대로 안 됐는데 애니메이션부터 붙잡고 늘어지는' 거예요. 먼저 기능이 돌아가게 하고, 마지막에 효과를 한꺼번에 추가하세요. 애니메이션은 화룡점정이고, 기능이 곧 본체예요. 이것이 우리의 늘 그래온 '단순함 최우선' 원칙이에요.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
직접 해 보기: '기분 버튼' 만들기

#### 6. 자주 쓰는 수정자 빠른 참조: 한 페이지 있으면 화면 걱정 없어요

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">하고 싶은 것</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">수정자</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">여백</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.padding(16)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">둥근 모서리</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cornerRadius(12)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">배경색</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.background(Color(.systemGray6))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">글꼴과 글자 크기</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.font(.title.bold())</code> / <code class="inline">.font(.system(size: 20))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">전경색(텍스트/아이콘)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.foregroundColor(.red)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">너비 꽉 채우기</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(maxWidth: .infinity)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">고정 크기</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(width:100, height: 44)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">정렬 방식</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack(alignment: .leading)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">투명도</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.opacity(0.6)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">그림자</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.shadow(radius: 5)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">탭 제스처</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.onTapGesture { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">키보드 유형</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.keyboardType(.decimalPad)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
SwiftUI 자주 쓰는 수정자 빠른 참조

외우지 못해도 괜찮아요. 이 페이지는 찾아 보라고 있는 거니까요. 실제로 가장 많이 쓰는 것은 앞의 네 가지, padding, 둥근 모서리, 배경, 글꼴이에요.

{class="mt-1"}
템플릿 프로젝트를 기분 전환기로 바꿔 보세요. 버튼 하나를 누를 때마다 😀기쁨 → 😢슬픔 → 😡화남 사이를 순환하며 글자와 배경색이 함께 바뀌어요. 힌트: 배열에 세 세트(텍스트+색상)를 담고, @State에 인덱스를 저장하고, 누를 때 (index + 1) % 3으로요. 완성하면 친구에게 보내 보세요. '우와, 너 앱을 만들 줄 알아?'라는 첫 반응을 거둘 수 있어요.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
이 장 정리

- SwiftUI는 선언형: '어떻게 생겼는지' 서술하면 시스템이 그리고 다시 그려요
- 뷰 = View 프로토콜을 채택한 구조체; body가 화면을 서술; 수정자 체인으로 '화장'
- 네 가지 기본 뷰: Text / Button / TextField / Image; SF Symbols 아이콘 라이브러리는 무료로 넉넉해요
- 레이아웃 3종 세트: VStack은 세로, HStack은 가로, ZStack은 겹침; Spacer는 탄력 있는 공간
- @State로 화면을 살아 있게; $ 양방향 바인딩으로 입력창에 먹이기
- #Preview는 보는 대로; 시스템 색상은 다크 모드 자동 대응; withAnimation은 한 줄 효과
:::
