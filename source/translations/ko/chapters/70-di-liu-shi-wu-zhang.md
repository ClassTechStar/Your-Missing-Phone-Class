---
id: di-liu-shi-wu-zhang
num: 65
part: ios-kai-fa-pian
nav: 제65장: 프로젝트 1 — 나의 가계부(로컬 버전)
toc: default
kind: chapter
---

### 제65장: 프로젝트 1 — 나의 가계부(로컬 버전)

{class="chapter-intro mb-4"}
여러분의 첫 '제대로 된 프로젝트'에 오신 것을 환영해요. 이 가계부는 네트워크에 연결되지 않지만 작아도 알차요. 내역을 기록하고, 흐름을 보고, 월별로 집계하고, 삭제와 수정도 할 수 있죠. 이것을 끝내면 '데이터 → 로직 → 화면' 전 과정을 한 바퀴 완주하는 거예요. 코드 베끼기부터 서두르지 마세요. 먼저 생각을 정리하고 손을 쓰는 것이 우리의 늘 그래온 원칙이에요.

#### 1. 요구 사항 생각: 먼저 다섯 가지 질문

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">요소</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">답</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who(누가 쓰나)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">자기 자신, 가족이나 친구도 좋아요</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What(무엇을 하나)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">수입·지출 기록, 내역 보기, 월별 요약, 카테고리별 통계</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why(왜 하나)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">연습 + 돈이 어디에 쓰였는지 파악</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How(어떻게 하나)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift + SwiftUI + SwiftData + MVVM, 순수 로컬, 백엔드 없음</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint(제약)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1주일 안에 완성; 최소 iOS 17 지원(SwiftData 요구 사항)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
가계부 요구 사항 5요소

그다음 '한 단계마다 쓸 수 있는' 작은 단계로 쪼개요. ① SwiftData 데이터 계층 만들기(한 건 저장 가능); ② 리스트 페이지(내역 보기 가능); ③ 입력 팝업(추가 가능); ④ 삭제와 편집; ⑤ 월별 요약 카드. 한 단계를 끝낼 때마다 앱은 '쓸 수 있는 물건'이에요.

#### 2. 데이터 계층: '장부'에 집 주기

먼저 한 건의 내역이 어떻게 생겼는지 정의하세요. 필드는 충분하되 욕심내지 마세요.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Record.swift(모델)</span><span class="dots">···</span>
:::

```
import SwiftData

@Model
class Record {
    var type: String      // "income" 수입 | "expense" 지출
    var amount: Double    // 금액(위안)
    var category: String  // 분류: 식사, 교통, 월급……
    var note: String      // 메모(선택)
    var date: Date        // 기록 날짜

    init(type: String, amount: Double, category: String, note: String = "", date: Date = Date()) {
        self.type = type
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
팁: 금액은 왜 Double을 쓸까?

{class="mt-1"}
엄격한 금융 앱은 부동소수점 오차(0.1+0.2≠0.3이라는 오래된 문제)를 피하려고 Decimal(정확한 10진수)을 써요. 연습 프로젝트는 Double로 충분해요. 언젠가 진짜 금융 제품을 만들게 되면 Decimal이나 '센트 단위의 Int'로 바꾸는 것을 잊지 마세요. 무수한 선배들이 밟아 온 함정이에요.
:::

#### 3. MVVM: 화면과 로직 '분가'

화면에서 데이터베이스를 바로 다루게 할까요? 돌아는 가지만 화면 코드가 지저분하게 길어져요. MVVM 아키텍처는 각자 제 역할을 하게 해요. View(화면)는 그리기만 하고, ViewModel(로직 중추)은 데이터를, Model(SwiftData)은 저장을 담당해요.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View(SwiftUI 화면)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel(@Observable 로직 허브)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model(SwiftData 데이터 계층)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
그림 4: MVVM 3계층 구조 — 데이터는 한 방향으로 흐르고, 각 계층은 서로의 영역을 침범하지 않아요
:::

::: div .code-block
:::inline div .code-head
<span>SWIFT · RecordViewModel.swift(뼈대)</span><span class="dots">···</span>
:::

```
import Observation

@Observable
class RecordViewModel {
    var records: [Record] = []
    private let context: ModelContext

    init(context: ModelContext) { self.context = context }

    func load() {
        // SwiftData의 #Predicate 필터 + 정렬
        let descriptor = FetchDescriptor<Record>(
            sortBy: [SortDescriptor(\.date, order: .reverse)]
        )
        records = (try? context.fetch(descriptor)) ?? []
    }

    func add(type: String, amount: Double, category: String, note: String) {
        let r = Record(type: type, amount: amount, category: category, note: note)
        context.insert(r)
        try? context.save()
        load()                       // 다시 불러오기, 화면 새로 고침
    }

    func delete(_ record: Record) {
        context.delete(record)
        try? context.save()
        load()
    }
}
```
:::

화면에서 @State private var vm = RecordViewModel(...)로 만들고 vm.records로 리스트를 바로 렌더링하면, 데이터가 바뀌는 순간 화면도 자동으로 새로 고쳐져요.

#### 4. 화면: 리스트 페이지 + 입력 팝업

::: div .code-block
:::inline div .code-head
<span>SWIFT · 가계부 목록 화면(핵심 발췌)</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var vm: RecordViewModel
    @State private var showAdd = false

    var body: some View {
        NavigationStack {
            List {
                Section("이번 달 잔액") {          // 요약 카드
                    SummaryRow(records: vm.records)
                }
                Section("내역") {
                    ForEach(vm.records) { r in
                        RecordRow(record: r)
                    }
                    .onDelete { idx in
                        idx.forEach { vm.delete(vm.records[$0]) }
                    }
                }
            }
            .navigationTitle("내 가계부")
            .toolbar {
                Button { showAdd = true } label: {
                    Image(systemName: "plus")
                }
            }
            .sheet(isPresented: $showAdd) {
                AddRecordView(vm: vm)          // 입력 팝업
            }
        }
    }
}
```
:::

입력 팝업 핵심: 금액 입력창 키보드는 .keyboardType(.decimalPad)(숫자 키패드), 수입/지출은 세그먼트 컨트롤(Picker), 카테고리는 메뉴에서 선택하고, '저장'을 누르면 vm.add(...)를 호출한 뒤 dismiss()로 창을 닫아요.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
주의: 입력 검증은 게을리하지 마세요

{class="mt-1"}
금액 입력창은 반드시 검증하세요. 빈 값, 음수, 'abc' 같은 잘못된 입력은 모두 막아야 해요(Double(text)로 판단하고, 실패하면 nil을 반환). 앱이 크래시되는 가장 흔한 원인 중 하나가 바로 '사용자 입력을 착한 아이로만 여기는 것'이에요. 기억하세요: 사용자가 입력하는 모든 것은 적처럼 의심하고 검사해야 해요.
:::

#### 5. 편집, 삭제와 합계

- 삭제: List의 .onDelete로 왼쪽으로 밀어 삭제 + 확인 팝업(실수로 지우는 일은 가계부 앱 사용자가 가장 싫어하는 일이에요);
- 편집: 행을 눌러 편집 팝업으로 들어가고 기존 값을 미리 채워 줘요(한 글자 고치는 게 처음부터 다시 입력하는 것보다 편해요);
- 합계: filter + reduce로 '이번 달 수입 / 지출 / 잔액'을 계산해 상단 카드에 표시해요:

::: div .code-block
:::inline div .code-head
<span>SWIFT · 월간 집계 계산</span><span class="dots">···</span>
:::

```
func monthSummary(_ records: [Record]) -> (income: Double, expense: Double) {
    let cal = Calendar.current
    let monthRecords = records.filter {
        cal.isDate($0.date, equalTo: Date(), toGranularity: .month)
    }
    let income = monthRecords
        .filter { $0.type == "income" }
        .reduce(0) { $0 + $1.amount }
    let expense = monthRecords
        .filter { $0.type == "expense" }
        .reduce(0) { $0 + $1.amount }
    return (income, expense)
}
```
:::

#### 6. 검수: 3단계 점검 + 심화 도전 2가지

프로젝트를 다 만들었으면 '기능 → 경계 → 아키텍처' 3단계로 검수해요. 기록할 수 있고, 삭제할 수 있고, 앱을 다시 실행해도 데이터가 남아 있는지(기능), 금액에 0이나 음수를 입력하면 크래시가 나는지(경계), 화면과 데이터가 뒤섞이지 않았는지, 필드가 하드코딩되지 않았는지(아키텍처).

기본 버전 검수를 통과했다면 스스로에게 '심화 메뉴' 두 가지를 더해 보세요:

1. 카테고리 통계: '통계' 탭을 추가하고 Swift Charts로 카테고리별 지출을 원형/막대 그래프로 그려요. 애플 공식 차트 라이브러리라 몇 줄의 코드로 그래프가 완성돼요;
2. iCloud 동기화: SwiftData는 iCloud 동기화를 몇 가지 설정만 고르면 켤 수 있어요. 가계부가 iPhone/iPad 사이에서 자동으로 동기화되며 순식간에 '고급' 앱처럼 보여요.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
직접 해 보기: 이번 주 안에 완성하기

{class="mt-1"}
'데이터 계층 → ViewModel → 리스트 페이지 → 입력 팝업 → 합계 카드' 순서로 하루에 한 단계씩 진행해요. 막히면 오류 메시지를 그대로 검색 엔진이나 AI에 던져 주세요(제7편 〈AI 코딩 실전편〉 기억하나요? 문제를 설명할 때는 '기대한 동작, 실제 동작, 재현 절차'를 분명히 말해요). 완성하면 일주일 동안 직접 가계부를 써 보세요. 자신이 만든 앱을 쓰다 보면 성취감이 앞으로 나아갈 힘이 돼 줄 거예요.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
이번 장 정리

- 요구사항 5요소 → '매 단계마다 동작하는' 작은 단계로 쪼갠 뒤 시작
- 데이터 계층: @Model 모델 + modelContainer 컨테이너 + FetchDescriptor 쿼리
- MVVM 역할 분담: View는 그리기만, @Observable ViewModel은 로직, SwiftData는 저장 담당
- 화면: List + Section + toolbar + sheet 입력 팝업
- 3단계 검수(기능/경계/아키텍처) + 심화 도전(Swift Charts, iCloud 동기화)
:::
