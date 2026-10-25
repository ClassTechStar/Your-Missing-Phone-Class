---
id: di-si-shi-zhang
num: 40
part: ai-biancheng-pian
nav: 제40장: 요구사항 엔지니어링 — 아이디어를 AI 지시로 바꾸기
toc: default
kind: chapter
---

### 제40장: 요구사항 엔지니어링 — 아이디어를 AI가 실행 가능한 지시로 바꾸기

{class="chapter-intro mb-4"}
컨텍스트 엔지니어링이 'AI가 배경을 이해하게 만들기'라면, 요구사항 엔지니어링은 'AI가 이번에 구체적으로 뭘 해야 하는지 알게 만들기'예요. 이건 AI 프로그래밍에서 사람 간 차이가 가장 뚜렷하게 드러나는 단계예요. 같은 도구, 같은 모델을 써도 어떤 사람은 눈부신 프로젝트를 만들고 어떤 사람은 평범한 장난감만 만들죠. 차이는 대개 기술 실력이 아니라 요구사항을 표현하는 능력에 있어요.

#### 1. 모호한 아이디어에서 구조화된 요구사항으로

모든 프로젝트는 모호한 아이디어에서 시작해요. '가계부 앱을 만들고 싶어', '개인 웹사이트를 만들고 싶어', '할 일 목록 도구를 만들고 싶어'. 아이디어 자체는 문제없어요. 하지만 그대로 AI에게 던지면 결과물의 품질은 온전히 운에 달렸어요. 요구사항 엔지니어링의 목표는 이 모호한 아이디어를 AI가 정확히 실행할 수 있는 구조화된 요구사항으로 바꾸는 거예요.

좋은 소식은, 구조화된 요구사항에 수십 페이지짜리 PRD가 필요 없다는 거예요. 다섯 가지 질문에만 답하면 돼요. 우리는 이걸 '요구사항 5요소'라고 불러요.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">요소</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">질문</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">예시: 가계부 앱</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">누가 쓰나요?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">개인이 사용하며 매일의 수입과 지출을 기록</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">무엇을 하나요?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">수입·지출 내역을 기록하고 월별로 집계하며 시각화까지 되는 앱</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">왜 만드나요?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">내 소비 구조를 파악하고 불필요한 지출을 찾고 싶어서</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">대략 어떻게 만드나요?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">프론트엔드는 React, 데이터는 브라우저 로컬에 저장, 백엔드와 로그인은 일단 제외</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">어떤 제한이 있나요?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1인 개발, 2주 안에 완성, 서비스 배포는 불필요</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
요구사항 5요소와 예시

이 다섯 요소를 정식 문서로 쓸 필요는 없어요. 머릿속으로 빠르게 훑어보기만 해도 충분해요. 중요한 건 '명확히 생각한 뒤에 입을 여는' 습관이에요. 다섯 가지 질문에 선명하게 답할 수 있게 되면, 요구사항 설명이 자연스럽게 구조를 갖추게 된다는 걸 알게 될 거예요.

#### 2. 요구사항 분해의 계층화 기술

규모가 좀 되는 프로젝트라면 요구사항 설명 하나로는 부족해요. 큰 요구를 작고 독립적으로 검증 가능한 하위 요구로 나눠야 해요. 이 과정을 '요구사항 분해'라고 해요. 핵심 원칙은 각 하위 요구가 독립적으로 완성되고, 독립적으로 검증되고, 독립적으로 인도될 수 있어야 한다는 거예요.

'개인 가계부 앱 만들기'를 예로 들면, 합리적인 분해 방식은 이래요.

1. 기본 수입·지출 기록 기능 구현(기록 추가, 조회, 삭제 가능)
2. 분류 기능 추가(각 기록에 식비, 교통 등 태그 붙이기)
3. 월별 집계 기능 구현(월 단위로 수입·지출 통계)
4. 데이터 시각화 추가(차트로 소비 구조 표시)

각 단계는 독립적으로 실행하고 검증할 수 있는 기능 단위예요.

:::inline div .quote-line
요구사항 나누기의 황금 법칙: 매 단계가 끝나면 프로젝트는 언제나 "돌아가는 물건"이어야 해요. 기능이 허술해도 괜찮아요. "절반씩만 되어 있지만 아무것도 쓸 수 없는" 상태로 프로젝트를 방치하지 마세요.
:::

이런 분해 방식에는 두 가지 장점이 있어요. 첫째, 진행 상황이 항상 눈에 보여요. 한 단계를 끝낼 때마다 앱에 기능이 하나씩 늘어나죠. 이런 긍정적 피드백은 긴 프로젝트에서 특히 중요해요(사람은 누구나 성취감이 필요하니까요). 둘째, AI의 과제가 매번 충분히 작아져 'AI가 잘못 이해할' 위험이 줄어들어요. 과제가 작을수록 AI의 이해가 정확해지고 결과물 품질도 올라가요.

#### 3. PRD 작성 템플릿과 실전

규모가 큰 프로젝트(예: 프런트와 백엔드, 여러 기능 모듈을 갖춘 풀스택 앱)라면 요구사항 5요소만으로는 부족할 수 있어요. 이럴 때 좀 더 정식인 프로젝트 요구사항 문서(PRD)를 써야 해요. 오해하기 쉬운 점 하나: PRD는 AI에게 보여 주려고 쓰는 게 아니라 여러분 자신을 위해 쓰는 거예요. 생각을 정리해야 AI에게 더 정밀한 지시를 내릴 수 있으니까요.

좋은 PRD는 길 필요는 없지만 여섯 부분을 담아야 해요. 프로젝트 개요(무엇을 만드는지 한 문단으로), 기능 목록(각 기능 포인트가 무엇인지), 기술 방안(어떤 기술 스택, 대략적인 아키텍처), 데이터 모델(핵심 데이터 구조), 화면 설명(주요 페이지의 모습), 개발 계획(몇 단계로 완성할지).

::: div .code-block
:::inline div .code-head
<span>PRD.md</span><span class="dots">···</span>
:::

```
# 개인 가계부 앱 PRD
## 프로젝트 개요
수입·지출 기록, 분류, 월간 집계, 데이터 시각화를 지원하는 가벼운 개인 가계부 앱이에요.
## 기능 목록
1. 수입·지출 기록: 금액, 유형(수입/지출), 분류, 메모, 날짜
2. 분류 관리: 식사, 교통, 쇼핑, 여가, 기타 프리셋
3. 월간 집계: 월별 총수입, 총지출, 잔액 통계
4. 소비 시각화: 원형 차트로 분류별 비중 표시
5. 데이터 내보내기: CSV로 내보내기
## 기술 방안
- 프런트엔드: React + TypeScript + Tailwind CSS
- 데이터 저장: localStorage(백엔드 불필요)
- 차트: Chart.js 사용
- 빌드: Vite
## 데이터 모델
Record {
  id: string
  amount: number
  type: 'income' | 'expense'
  category: string
  note: string
  date: string  // YYYY-MM-DD
}
## 개발 계획
Step 1: 기본 기록 기능 (CRUD)
Step 2: 분류 관리
Step 3: 월간 집계
Step 4: 데이터 시각화
Step 5: 데이터 내보내기
```
:::

이 PRD의 작성 스타일에 주목하세요. 장황한 이야기 대신 간결한 목록과 구조화된 형식을 써요. 각 기능 포인트에는 명확한 정의를 달고, 데이터 모델은 단순한 타입으로 서술하죠. 이런 스타일의 PRD는 본인이 읽기에도 명확할 뿐 아니라, AI에게 넘겨도 AI가 각 요구 포인트를 정확히 이해해요.

#### 4. 실전: 아이디어에서 방안까지 전 과정 훑어보기

말로만 하면 재미없죠. 완성된 예시 하나로 요구사항 엔지니어링의 전 과정을 한 번 걸어 봐요. 아이디어가 이렇다고 해 볼게요. '매일 뭘 배웠는지 기록해 주는 학습 트래커를 만들고 싶어요.'

첫 번째 단계, 요구사항 5요소를 한번 훑어 봐요.

- Who: 개인 사용.
- What: 매일의 학습 내용을 기록하고 학습 시간을 추적하며 학습 진행을 돌아볼 수 있는 도구.
- Why: 꾸준히 배우는 습관을 들이고 쌓여 가는 걸 눈으로 보고 싶어서.
- How: 일단 웹 버전으로 만들고, 데이터는 브라우저 로컬에 저장.
- Constraint: 개발 기초가 없는 상태에서 1주 안에 핵심 기능 완성.

두 번째 단계, 요구사항을 나눠요.

1. Step 1: '학습 항목 기록' 기능 구현(날짜, 내용, 시간)
2. Step 2: '학습 시간 통계' 추가(오늘, 이번 주 누계)
3. Step 3: '학습 달력' 뷰 구현(GitHub 기여 그래프처럼 표시)
4. Step 4: '학습 복습' 기능 추가(과거 특정 날의 기록을 무작위로 보여 주어 복습 도움)

세 번째 단계, 짧은 PRD를 써요. 길 필요 없어요. 위의 분해 자체가 PRD의 몸통을 이루거든요. 이를 .md 파일 하나로 정리해 프로젝트 루트 디렉터리에 두고, 여러분과 AI의 공동 참고 자료로 쓰세요.

네 번째 단계, 첫 단계 개발을 시작해요. AI에게 줄 지시는 이런 식이 될 수 있어요.

::: div .code-block
:::inline div .code-head
<span>AI에게 주는 지시</span><span class="dots">···</span>
:::

```
학습 추적기의 첫 번째 기능 — 학습 항목 기록이 필요해요.
사용자는 날짜, 학습 내용, 학습 시간(분)을 포함한 학습 기록을 추가할 수 있어요.
데이터는 localStorage에 저장해요.
프런트엔드는 React + TypeScript를 써요.
전체 구현을 제시해 주세요.
```
:::

이 지시의 특징에 주목하세요. 현재 단계의 목표(기록 기능)만 설명하고 다른 기능은 섞지 않아요. 기술 제약(React, TypeScript, localStorage)을 명확히 밝혀요. AI가 '무엇을'하고 '어떻게' 할지 알 만한 정보는 충분히 주되, 구체적 구현은 AI가 결정하게 하죠. 요구사항 엔지니어링을 거친 고 품질 AI 프로그래밍 지시문의 모습이에요.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
직접 해 보기: 내 '아이템'에 5요소 카드 한 장 쓰기

{class="mt-1"}
오래 숙성시켜 온 작은 프로젝트 하나를 골라 5분만 들여 카드를 채워 보세요. Who / What / Why / How / Constraint, 각각 한 문장씩요. 그다음 '한 단계 끝날 때마다 쓸 수 있는' 3~5개의 단계로 나눠 보세요. 알게 될 거예요. 아이디어를 종이에 적는 순간, 그것이 '공상'에서 '할 일 목록'으로 바뀐다는 걸요.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
이번 장 정리

- 요구사항 5요소: Who / What / Why / How / Constraint — 명확히 생각한 뒤에 입을 열어요
- 요구사항 분해 황금 법칙: 한 단계를 마칠 때마다 프로젝트는 '쓸 수 있는 물건'이에요
- PRD는 자신을 위해 쓰는 거예요: 개요, 기능 목록, 기술 방안, 데이터 모델, 화면, 계획
- 좋은 지시 = 현재 단계만 설명 + 제약을 명확히 + '어떻게'가 아니라 '무엇을'이라고 말하기
- 전 과정 템플릿: 5요소 → 분해 → PRD → 지시 내리기, 4단계로 가요
:::
