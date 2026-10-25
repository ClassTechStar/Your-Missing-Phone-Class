---
id: di-liu-shi-san-zhang
num: 63
part: ios-kai-fa-pian
nav: 제63장: 뷰, 상태와 내비게이션
toc: default
kind: chapter
---

### 제63장: 뷰, 상태와 내비게이션

{class="chapter-intro mb-4"}
한 페이지짜리 장난감은 이제 만들 줄 알아요. 이 장에서는 '성장' 문제 두 가지를 해결해요. 여러 페이지 사이를 오가는 방법(내비게이션)과 데이터가 페이지 사이를 어떻게 흐르는지(상태 관리)예요. 이 장을 마치면 '목록 → 상세 → 편집' 같은 고전적인 멀티페이지 앱 뼈대를 세울 수 있어요.

#### 1. 상태 관리의 '데이터 흐름 전체 그림'

SwiftUI의 상태 도구는 @State 하나만이 아니에요. 먼저 이 전체 그림을 보고 '언제 무엇을 쓰는지'를 파악하세요.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">도구</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">담당하는 것</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">누가 쓰나</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">전형적인 사례</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">페이지 전용 임시 상태</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">현재 뷰</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">카운터, 입력창 텍스트</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Binding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">다른 곳의 상태 빌려 쓰기</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">자식 뷰가 부모 뷰를 수정</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">커스텀 컴포넌트</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@StateObject / @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">페이지를 넘어 공유되는 로직</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">뷰 모델(ViewModel)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">데이터 로딩, 비즈니스 로직</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@EnvironmentObject / .environment</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">전역 공유 상태</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">앱 전체</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">사용자 로그인 상태, 테마 설정</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
SwiftUI 상태 도구 전체 그림(2026년, @Observable이 주류)

::: div .code-block
:::inline div .code-head
<span>SWIFT · 2026년 주류: @Observable 뷰 모델</span><span class="dots">···</span>
:::

```
// iOS 17+의 현대적 작성법: @Observable 매크로(신규 프로젝트 추천)
import Observation

@Observable
class CounterModel {                 // 뷰 모델
    var count = 0
    func increment() { count += 1 }
}

struct CounterView: View {
    @State private var model = CounterModel()   // 모델 보유

    var body: some View {
        VStack {
            Text("\(model.count)번 눌렀어요")
            Button("눌러 보세요") { model.increment() }
        }
    }
}
```
:::

초보자를 위한 무뚝뚝한 조언: 페이지 전용은 @State, 페이지를 넘거나 로직이 있으면 @Observable 클래스를 쓰세요. 오래된 튜토리얼의 @StateObject/@ObservableObject는 이전 세대 문법이니 읽을 수만 있으면 되고, 새 코드는 위를 따르세요.

#### 2. NavigationStack: 페이지 이동의 '스택'

iOS 16부터 멀티페이지 내비게이션은 NavigationStack을 써요. 접시 한 무더기처럼 하나씩 쌓아 올리고, 뒤로 갈 때 하나씩 꺼내죠.

::: div .code-block
:::inline div .code-head
<span>SWIFT · NavigationStack 내비게이션</span><span class="dots">···</span>
:::

```
struct HomeView: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("김철수의 가계부") {
                    DetailView(name: "김철수의 가계부")   // 목적지 화면
                }
                NavigationLink("이영희의 가계부") {
                    DetailView(name: "이영희의 가계부")
                }
            }
            .navigationTitle("가계부 목록")   // 상단 큰 제목
        }
    }
}

struct DetailView: View {
    let name: String
    var body: some View {
        Text("\(name) 상세 화면")
            .navigationTitle(name)
            .navigationBarTitleDisplayMode(.inline)
    }
}
```
:::

NavigationLink는 '누를 수 있는 이동 링크'예요. navigationTitle은 내비게이션 바 제목과 뒤로 가기 버튼을 자동으로 만들어 줘요. 코드로 이동을 제어해야 할 때(예: '저장'을 누른 뒤 자동으로 돌아가기)는 @Environment(\.dismiss)로 현재 페이지를 닫아요. 이 두 가지를 함께 쓰면 내비게이션 수요의 90%가 해결돼요.

#### 3. 팝업과 하단 탭: sheet와 TabView

'페이지를 밀어 올리는' 것 외에 두 가지 고전적인 상호작용이 있어요.

::: div .code-block
:::inline div .code-head
<span>SWIFT · sheet 팝업 + TabView 탭</span><span class="dots">···</span>
:::

```
// 1. 아래에서 하프/전체 화면 팝업(입력 폼의 단골)
struct HomeView: View {
    @State private var showAdd = false
    var body: some View {
        Button("한 줄 기록") { showAdd = true }
            .sheet(isPresented: $showAdd) {
                AddRecordView()     // 팝업되는 입력 화면
            }
    }
}

// 2. 하단 탭 바(앱의 "뼈대")
struct MainTabView: View {
    var body: some View {
        TabView {
            RecordListView()
                .tabItem { Label("가계부", systemImage: "book") }
            StatsView()
                .tabItem { Label("통계", systemImage: "chart.pie") }
            SettingsView()
                .tabItem { Label("설정", systemImage: "gear") }
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
팁: 언제 무엇을 쓸까?

{class="mt-1"}
경험 법칙: 주요 흐름은 NavigationStack으로 페이지를 밀어 올리고(목록→상세), 임시 조작은 sheet 팝업으로(추가, 편집, 확인), 나란히 있는 큰 블록은 TabView(하단 탭)로요. 이 셋을 조합하면 대부분의 앱 뼈대가 완성돼요.
:::

#### 4. List: iOS의 '국민 리스트'

iOS에서 가장 많이 쓰이고 '애플맛'이 가장 나는 컴포넌트가 바로 List예요. 구분선, 스와이프 삭제, 탭 하이라이트가 기본으로 딸려 와요.

::: div .code-block
:::inline div .code-head
<span>SWIFT · List 목록 + 밀어서 삭제</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var records = ["점심 25.5", "지하철 6.0", "월급 +8000"]

    var body: some View {
        List {
            ForEach(records, id: \.self) { r in
                Text(r)
            }
            .onDelete { indexSet in          // 왼쪽으로 밀어서 삭제
                records.remove(atOffsets: indexSet)
            }
        }
    }
}
```
:::

리스트 + NavigationLink + sheet + TabView. 이 네 가지를 조합하면 '가계부 목록 → 눌러서 상세 보기 → +를 눌러 입력 띄우기'의 완전한 앱 뼈대를 세울 수 있어요. 다음 장의 가계부 프로젝트가 바로 이렇게 지은 거예요.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
직접 해 보기: '세 페이지 뼈대' 세우기

#### 5. 앱 생명주기: 포그라운드와 백그라운드

안드로이드의 Activity 생명주기와 비슷하게, iOS 앱에도 '탄생, 포그라운드, 백그라운드, 소멸'의 상태 변화가 있어요. SwiftUI에서는 scenePhase 환경값으로 관찰해요.

::: div .code-block
:::inline div .code-head
<span>SWIFT · 포그라운드/백그라운드 전환 관찰</span><span class="dots">···</span>
:::

```
@main
struct MyApp: App {
    @Environment(\.scenePhase) private var phase

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .onChange(of: phase) { _, newPhase in
            switch newPhase {
            case .active:    print("포그라운드 복귀, 새로 고침 재개")
            case .inactive:  print("전환 중(전화 수신/백그라운드 전환 순간)")
            case .background: print("백그라운드 진입, 임시 저장")
            @unknown default: break
            }
        }
    }
}
```
:::

전형적인 용도: 포그라운드로 돌아올 때 데이터를 새로 고치고, 백그라운드로 갈 때 임시 저장해요. iOS는 백그라운드 실행을 아주 엄격히 관리해요. 일반 앱은 백그라운드에 들어가면 곧 중단(동결)되니 백그라운드에서 몰래 무거운 일을 하려 하지 마세요. 정말 예약 작업이 필요하면 '백그라운드 상주'가 아니라 제68장의 로컬 알림을 쓰세요.

{class="mt-1"}
가짜 데이터 버전의 가계부 뼈대를 만들어 보세요. TabView의 세 탭(가계부/통계/설정) → 가계부 페이지는 List로 가짜 데이터를 표시하고 행을 누르면 상세로 이동(NavigationStack) → 오른쪽 위 '+' 버튼으로 입력 sheet를 띄우기. 데이터를 저장하지도 네트워크에 연결하지도 않는 순수 뼈대 연습이에요. 이 뼈대를 잘 만들어 두면 제65장에서 진짜 데이터를 채우는 건 물 흐르듯 자연스러워요.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
이 장 정리

- 상태 4대 도구: @State(페이지 전용), @Binding(빌려 쓰기), @Observable(로직), .environment(전역)
- 새 프로젝트는 @Observable 매크로로 뷰 모델을 작성; 오래된 튜토리얼의 @ObservableObject는 읽을 수만 있으면 돼요
- NavigationStack으로 페이지를 밀어 올리고; @Environment(\.dismiss)로 코드로 뒤로 가기
- 주요 흐름은 페이지 밀기, 임시 조작은 sheet, 나란한 큰 블록은 TabView
- List는 '국민 리스트': 구분선, 스와이프 삭제가 기본 제공
:::
