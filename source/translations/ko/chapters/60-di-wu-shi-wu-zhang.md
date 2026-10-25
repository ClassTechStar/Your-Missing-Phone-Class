---
id: di-wu-shi-wu-zhang
num: 55
part: an-zhuo-kai-fa-pian
nav: 제55장: 프로젝트 2 — 날씨 조회 앱(네트워크 버전)
toc: default
kind: chapter
---

### 제55장: 프로젝트 2 — 날씨 조회 앱(네트워크 버전)

{class="chapter-intro mb-4"}
가계부가 "내공 연습"이라면 날씨 앱은 "세상 구경"이에요. 인터넷과 손을 잡아야 하거든요. 이 프로젝트에서 여러분은 무료 API 신청하기, JSON 파싱하기, "로딩 중/성공/실패" 세 가지 화면 상태 다루기, 그리고 API 키를 잘 숨기는 법을 배워요. 다 만들면 어떤 "네트워크 앱"이든 만들 능력이 생겨요. 뉴스, 환율, 번역, 요령은 똑같으니까요.

#### 1. 무료 날씨 API 신청하기

개인 연습용으로는 OpenWeatherMap이나 중국의 QWeather(허펑 날씨)를 추천해요. 둘 다 무료 한도가 있고 가입하면 바로 쓸 수 있죠. OpenWeatherMap을 예로 들게요:

1. 계정 가입 → API keys 페이지에서 키(apikey)를 하나 생성;
2. 무료 버전에서는 Current Weather(현재 날씨) 엔드포인트를 호출할 수 있어요: api.openweathermap.org/data/2.5/weather? q=beijing&appid=발급받은키&units=metric;
3. 브라우저에서 먼저 한 번 시험해 보고 돌아오는 JSON이 어떻게 생겼는지 확인하세요. 어떤 API든 붙이기 전에 꼭 하는 "예습"이에요.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
주의: 키는 절대 코드에 박아 두지 않기

{class="mt-1"}
API 키는 "지갑 비밀번호"와 같아서, 코드에 넣어 GitHub에 올리면 몇 시간 안에 크롤러가 긁어가 도용해요. 올바른 방법: local.properties에 넣고(이 파일은 gitignore가 이미 무시해요) Gradle의 buildConfig로 코드에 읽어 들이세요. "Android API 키 숨기기 모범 사례"를 검색해서 그대로 따라 하면 돼요.
:::

#### 2. 네트워크 계층: Retrofit + JSON 파싱

먼저 API가 돌려주는 JSON을 보고 "데이터 모델"을 정의하세요. 맞지 않는 필드는 모두 무시하면 돼요:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 데이터 모델 + 인터페이스</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"맑음"}],"main":{"temp":26.5,"humidity":40},"name":"베이징"}
data class WeatherResponse(
    val weather: List&lt;Weather&gt;,
    val main: Main,
    val name: String
)
data class Weather(val description: String)
data class Main(val temp: Double, val humidity: Int)

interface WeatherApi {
    @GET("data/2.5/weather")
    suspend fun getWeather(
        @Query("q") city: String,
        @Query("appid") key: String,
        @Query("units") metric: String = "metric",
        @Query("lang") lang: String = "ko"
    ): WeatherResponse
}
```
:::

Gson이 JSON을 이 data class들에 자동으로 채워 넣어요. 필드 이름만 일치하면 마법이 저절로 일어나죠.

#### 3. 세 가지 화면 상태: 로딩 중 / 성공 / 실패

네트워크 앱의 영혼은 "상태 관리"에 있어요. 네트워크가 느리거나, 끊기거나, 도시 이름을 잘못 입력하거나…… 모든 상황에서 화면은 사용자에게 보고해야 해요. sealed class(봉인 클래스) 하나로 우아하게 표현해 봐요:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 화면 상태</span><span class="dots">···</span>
:::

```
sealed class UiState {
    object Loading : UiState()                    // 로딩 표시
    data class Success(val data: WeatherResponse) : UiState()  // 성공
    data class Error(val message: String) : UiState()          // 실패
}

// ViewModel 안에서:
fun search(city: String) {
    viewModelScope.launch {
        _state.value = UiState.Loading
        _state.value = try {
            UiState.Success(api.getWeather(city))
        } catch (e: Exception) {
            UiState.Error("그 도시를 찾을 수 없어요. 다른 이름으로 시도해 볼까요?")
        }
    }
}

// 화면 안에서:
when (val s = state) {
    is UiState.Loading -&gt; CircularProgressIndicator()   // 로딩
    is UiState.Success -&gt; WeatherContent(s.data)        // 표시
    is UiState.Error -&gt; Text(s.message)                 // 오류
}
```
:::

이 Loading/Success/Error 3단 구성은 네트워크 화면의 "만능 템플릿"이에요. 먼저 외워 두고, 이후 모든 네트워크 앱에서 그대로 본떠 쓰세요.

#### 4. 실전 화면 코드: 날씨 그려 내기

상태가 준비됐으면 화면은 이렇게 생겼어요(핵심 부분):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 날씨 화면(핵심 발췌)</span><span class="dots">···</span>
:::

```
@Composable
fun WeatherContent(data: WeatherResponse) {
    Column(
        Modifier.fillMaxSize().padding(24.dp),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text(data.name, fontSize = 28.sp, fontWeight = FontWeight.Bold)
        Text(
            "${data.main.temp}°C",
            fontSize = 72.sp,
            fontWeight = FontWeight.Light
        )
        Text(
            data.weather.firstOrNull()?.description ?: "알 수 없음",
            fontSize = 20.sp,
            color = Color.Gray
        )
        Spacer(Modifier.height(16.dp))
        Row {
            Text("💧 습도 ${data.main.humidity}%")
            Spacer(Modifier.width(24.dp))
            Text("🌡️ 체감 ${data.main.temp}°C")
        }
    }
}
```
:::

배울 만한 디테일 몇 가지: firstOrNull()은 첫 번째 요소를 안전하게 꺼내요(리스트가 비어 있을 수 있으니까요), ?: "알 수 없음"이 기본 문구를 채워 줘요. null 안전 원칙은 화면에서도 그대로 통하죠. 온도는 72.sp의 큰 글자로 위용을 세우고, "가는" 글꼴 두께(Light)가 숫자를 우아하게 보이게 해요. 날씨 앱의 고전 레시피예요.

#### 5. 화면과 인터랙션 디테일

- 검색창: 상단에 TextField를 두고 도시 이름을 입력한 뒤 검색(키보드에 "검색" 동작을 설정하면 엔터로 바로 검색);
- 날씨 카드: 큰 글자 온도(26.5°), 날씨 설명(맑음), 습도, 도시 이름;
- 즐겨찾는 도시: 자주 보는 도시를 DataStore에 저장해 다음에 열 때 자동으로 조회 — 덤으로 6장 복습;
- 당겨서 새로 고침: Compose에서는 PullToRefreshBox(Material 3 제공)를 쓰세요. 손맛이 곧바로 "프로"급이 돼요.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
팁: 이미지가 화면에 생기를 불어넣어요

{class="mt-1"}
날씨 종류마다 이모지나 아이콘(☀️🌧️❄️)을 하나씩 매기고 when(description)으로 연결하세요. 세 줄 코드로 화면의 온기가 두 배가 돼요. 서드파티 날씨 아이콘 라이브러리를 쓸 수도 있지만, 연습 단계에서는 이모지면 충분해요.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
직접 해 보기: 날씨 앱 검수 체크리스트

{class="mt-1"}
① 정상적으로 검색해 날씨가 나오는가; ② 네트워크를 끊어도 앱이 우아하게 오류를 알리고 크래시되지 않는가(비행기 모드를 켜서 테스트!); ③ 존재하지 않는 도시를 입력했을 때 친절하게 안내하는가; ④ 도시 두 개를 즐겨찾기하고 앱을 재시작해도 남아 있는가; ⑤ 화면을 돌려도 상태가 사라지지 않는가. 다섯 항목을 모두 통과해야 이 프로젝트는 졸업이에요.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
이번 장 정리

- 먼저 브라우저로 API를 시험하고 JSON을 이해한 뒤 코드 작성 — "예습"은 언제나 이득
- API 키는 local.properties에 숨기고 절대 코드 저장소에 넣지 않기
- Retrofit 인터페이스 + data class: 필드만 맞으면 JSON이 자동으로 파싱돼요
- Loading/Success/Error 3단 상태는 네트워크 화면의 만능 해법
- 끊긴 네트워크, 빈 입력, 없는 도시 — 오류 처리는 네트워크 앱의 합격선
:::
