---
id: di-wu-shi-si-zhang
num: 54
part: an-zhuo-kai-fa-pian
nav: 제54장: 프로젝트 1 — 나의 가계부(로컬 버전)
toc: default
kind: chapter
---

### 제54장: 프로젝트 1 — 나만의 가계부(로컬 버전)

{class="chapter-intro mb-4"}
여러분의 첫 "제대로 된 프로젝트"에 오신 것을 환영해요. 이 가계부는 네트워크에 연결되지 않지만 필요한 기능은 모두 갖췄어요. 거래 한 건을 기록하고, 내역을 보고, 월별로 통계 내고, 삭제와 수정도 돼요. 다 만들면 "데이터 → 로직 → 화면" 전체 흐름을 한 바퀴 완주한 거예요. 서두르지 말고 코드부터 베끼지 마세요. 먼저 생각하고 손을 쓰는 것이 우리의 변함없는 원칙이에요.

#### 1. 요구사항 고민: 먼저 다섯 가지 질문하기

손대기 전에 "요구사항 5요소"로 아이디어를 정리해 보세요:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">요소</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">답</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who(누가 쓰나)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">나 자신, 가족·친구도 좋아요</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What(무엇을 하나)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">수입·지출 기록, 내역 보기, 월별 요약, 카테고리별 통계</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why(왜 만드나)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">연습 + 돈이 어디에 쓰였는지 파악</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How(어떻게 만들나)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin + Compose + Room + MVVM, 순수 로컬, 백엔드 없음</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint(제약)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">일주일 안에 완성, 최소 Android 8 지원, 출시하지 않더라도 출시 기준으로 작성</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
가계부 요구사항 5요소

그다음 "매 단계마다 쓸 수 있는" 작은 단계로 쪼개세요. ① Room 데이터 계층 만들기(거래 한 건 저장), ② 목록 화면(내역 보기), ③ 입력 화면(거래 추가), ④ 삭제와 편집, ⑤ 월별 요약 카드. 한 단계를 마칠 때마다 앱은 "쓸 수 있는 물건"이 돼요.

#### 2. 데이터 계층: "장부"에 집 주기

먼저 거래 한 건이 어떻게 생겼는지 정의하세요. 필드는 충분하되 탐내지 마세요:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Record.kt(엔티티)</span><span class="dots">···</span>
:::

```
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val type: String,        // "income" 수입 | "expense" 지출
    val amount: Double,      // 금액(위안)
    val category: String,    // 분류: 식사, 교통, 월급……
    val note: String = "",   // 메모(선택)
    val date: String         // "2026-08-15"
)
```
:::

Dao에 "통계용" 쿼리 두 개를 추가하세요. 이것이 가계부의 영혼이에요:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordDao.kt(집계 쿼리)</span><span class="dots">···</span>
:::

```
@Dao
interface RecordDao {
    @Query("SELECT * FROM records ORDER BY date DESC, id DESC")
    fun getAll(): Flow&lt;List&lt;Record&gt;&gt;

    @Insert
    suspend fun insert(record: Record)

    @Delete
    suspend fun delete(record: Record)

    @Query("SELECT COALESCE(SUM(amount),0) FROM records WHERE type='income' AND date LIKE :month || '%'")
    suspend fun monthIncome(month: String): Double   // month는 "2026-08" 형태

    @Query("SELECT COALESCE(SUM(amount),0) FROM records WHERE type='expense' AND date LIKE :month || '%'")
    suspend fun monthExpense(month: String): Double
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
팁: 금액은 왜 Double을 쓸까요?

{class="mt-1"}
엄격한 금융 앱은 부동소수점 오차(0.1+0.2≠0.3이라는 오래된 문제)를 피하려고 BigDecimal이나 "가장 작은 단위(센트)를 Int로" 써요. 연습 프로젝트는 Double이면 충분해요. 언젠가 진짜 금융 제품을 만들게 되면 최소 단위를 기준으로 바꾸는 것을 잊지 마세요. 수많은 선배들이 밟아 온 함정이에요.
:::

#### 3. MVVM: 화면과 로직 "분가시키기"

화면이 데이터베이스를 직접 다루게 할까요? 돌아는 가지만 화면 코드가 걷잡을 수 없이 길어져요. MVVM 아키텍처는 각자 역할을 나눠요. View(화면)는 그리기만 하고, ViewModel(로직 중추)은 데이터를 맡고, Model(Room)은 저장을 맡죠.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View(Compose 화면)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel(상태와 로직)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model(Room 데이터 계층)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
그림 5: MVVM 3계층 구조 — 데이터는 한 방향으로 흐르고, 계층끼리 서로 침범하지 않아요
:::

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordViewModel.kt(뼈대)</span><span class="dots">···</span>
:::

```
class RecordViewModel(private val dao: RecordDao) : ViewModel() {

    // Flow를 화면에서 관찰 가능한 상태로 변환
    val records = dao.getAll()
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(), emptyList())

    // 사용자 조작: suspend 함수 호출
    fun addRecord(type: String, amount: Double, category: String, note: String, date: String) {
        viewModelScope.launch {
            dao.insert(Record(type = type, amount = amount,
                category = category, note = note, date = date))
        }
    }

    fun deleteRecord(record: Record) {
        viewModelScope.launch { dao.delete(record) }
    }
}
```
:::

화면(Compose)에서는 이렇게 써요. val vm: RecordViewModel = viewModel()로 뷰모델을 얻고, val list by vm.records.collectAsState()로 수집하세요. 데이터가 바뀌는 순간 목록이 자동으로 새로 고침돼요. 여러분은 아무것도 할 필요가 없죠. 이것이 MVVM + Flow + Compose 세 가지가 힘을 합친 위력이에요.

#### 4. 화면: 목록 화면 + 입력 화면

목록 화면은 LazyColumn(지연 로딩 리스트)을 쓰세요. 데이터가 아무리 많아도 끊기지 않아요:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 가계부 목록 화면(핵심 발췌)</span><span class="dots">···</span>
:::

```
@Composable
fun RecordListScreen(vm: RecordViewModel) {
    val records by vm.records.collectAsState()

    Column {
        // 상단 요약 카드(수입-지출=잔액)
        SummaryCard(records)

        // 내역 목록
        LazyColumn {
            items(records, key = { it.id }) { record -&gt;
                RecordRow(record) { vm.deleteRecord(record) }
            }
        }

        // 떠 있는 "한 줄 기록" 버튼 → 입력 대화상자 표시
        FloatingActionButton(onClick = { showAddDialog = true }) {
            Text("+")
        }
    }
}

@Composable
fun RecordRow(record: Record, onDelete: () -&gt; Unit) {
    Row(Modifier.fillMaxWidth().padding(12.dp)) {
        Text(record.category, fontWeight = FontWeight.Bold)
        Spacer(Modifier.weight(1f))
        Text(if (record.type == "income") "+${record.amount}" else "-${record.amount}",
             color = if (record.type == "income") Color(0xFF27AE60) else Color(0xFFC0392B))
    }
}
```
:::

입력은 AlertDialog(대화상자)가 가장 편해요. 입력창 몇 개 + 수입/지출 전환 + 카테고리 드롭다운을 두고, 확인을 누르면 vm.addRecord(...)를 호출하면 돼요.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
주의: 입력 검증은 게으름 피우지 않기

{class="mt-1"}
금액 입력창은 반드시 검증하세요. 빈 값, 음수, "abc" 같은 잘못된 입력은 모두 막아야 해요(toDoubleOrNull()으로 판단). 앱이 크래시되는 가장 흔한 원인 중 하나가 "사용자의 입력을 착한 아이로 착각하는 것"이에요. 기억하세요. 사용자가 입력하는 모든 것은 적처럼 검열해야 해요.
:::

#### 5. 편집과 삭제: 데이터 "들어오고 나가기"

추가만 하고 삭제를 못하는 가계부는 사흘이면 망가져요. 두 가지 동작을 보태세요:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 삭제와 편집</span><span class="dots">···</span>
:::

```
// Dao에 두 개 더 추가:
@Query("UPDATE records SET amount=:amount, category=:category, note=:note WHERE id=:id")
suspend fun update(id: Long, amount: Double, category: String, note: String)

@Query("DELETE FROM records WHERE id=:id")
suspend fun deleteById(id: Long)

// 화면에서: 목록 항목을 길게 누르면 "편집/삭제" 메뉴 표시(Compose에서는 DropdownMenu 또는 AlertDialog 사용)
// 삭제 전에 확인 창을 띄우는 게 좋아요 — "실수로 삭제"는 가계부 앱 사용자가 가장 싫어하는 일이에요
```
:::

인터랙션 디테일 경험칙 두 가지: 삭제는 반드시 한 번 더 확인하게 하고(손미끼 방지), 편집은 기존 값을 미리 채워 주세요(한 글자 고치는 게 다시 입력하는 것보다 편하죠). 이 두 디테일을 얕보지 마세요. "제품다움"은 이런 디테일이 쌓여 만들어지는 거예요.

#### 6. 검수: 3단계 점검 + 심화 도전 두 가지

프로젝트를 다 만들었으면 "기능 → 경계 → 아키텍처" 세 단계로 검수하세요. 기록할 수 있나요, 삭제할 수 있나요, 앱을 다시 열어도 데이터가 남아 있나요(기능)? 금액에 0이나 음수를 넣으면 크래시되나요, 화면을 돌리면 데이터가 사라지나요(경계)? 화면과 데이터가 뒤섞여 있나요, 필드가 하드코딩돼 있나요(아키텍처)?

기본 버전 검수를 통과했으면 스스로에게 "심화 코스" 두 가지를 추가해 보세요:

1. 월별 필터: 상단에 월 전환을 추가하고(예: 2026-08 ▾) 목록에는 해당 월의 내역만 표시해요;
2. 카테고리 원형 차트: Compose의 Canvas를 쓰거나 가벼운 차트 라이브러리를 도입해 "돈이 어디에 쓰였는지"를 원형 차트로 그려 보세요. 이걸 끝내면 가계부가 좀 "제품다운 모습"을 갖춰요.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
직접 해 보기: 이번 주 안에 완성하기

{class="mt-1"}
"데이터 계층 → ViewModel → 목록 화면 → 입력 화면 → 요약 카드" 순서로 하루에 한 단계씩 진행하세요. 막히면 오류 메시지를 그대로 검색 엔진이나 AI에 던지세요(제7편 〈AI 코딩 실전편〉 기억하나요? 문제를 설명할 때는 "기대한 동작, 실제 동작, 재현 단계"를 분명히 말해야 해요). 완성되면 일주일 동안 직접 써서 가계부를 기록해 보세요. 자신이 만든 앱을 쓰고 있으면 성취감이 계속 앞으로 나아가게 밀어 줄 거예요.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
이번 장 정리

- 요구사항 5요소 → "매 단계 쓸 수 있는" 작은 단계로 쪼갠 뒤 착수
- 데이터 계층: Record 엔티티 + Dao(월별 통계 SQL 포함) + Database
- MVVM 분업: View는 그리기만, ViewModel은 로직, Model은 저장
- Flow + stateIn + collectAsState: 데이터가 바뀌면 화면이 자동으로 새로 고침
- LazyColumn 지연 로딩 리스트, AlertDialog로 입력
- 3단계 검수(기능/경계/아키텍처) + 심화 도전(월별 필터, 카테고리 원형 차트)
:::
