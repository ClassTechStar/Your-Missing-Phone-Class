---
id: di-wu-shi-wu-zhang
num: 55
part: an-zhuo-kai-fa-pian
nav: 第五十五章：项目二——天气查询App（网络版）
toc: default
kind: chapter
---

### 第五十五章：项目二——天气查询 App（网络版）

{class="chapter-intro mb-4"}
记账本是"练内功"，天气 App 是"见世面"——它要和互联网打交道。这个项目你会学到：申请免费 API、解析 JSON、处理"加载中/成功/失败"三种界面状态，以及怎么把 API 密钥藏好。做完它，你就具备了做任何"联网 App"的能力——新闻、汇率、翻译，套路一模一样。

#### 一、申请免费天气 API

个人练手，推荐 <strong>OpenWeatherMap</strong> 或国内的 <strong>和风天气（QWeather）</strong>——都有免费额度，注册即用。以 OpenWeatherMap 为例：

1. 注册账号 → 在 API keys 页面生成一个 Key（<code class="inline">apikey</code>）；
2. 免费版可调用 Current Weather（当前天气）接口：<code class="inline">api.openweathermap.org/data/2.5/weather? q=beijing&appid=你的Key&units=metric</code>；
3. 浏览器里先试一次，看看返回的 JSON 长什么样——这是接任何 API 前必做的"预习"。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>避坑提醒：密钥绝不能写死在代码里

{class="mt-1"}
API Key 相当于你的"钱包密码"，写进代码一提交到 GitHub，几小时内就会被爬虫扫走盗刷。正确做法：放进 <code class="inline">local.properties</code>（这个文件已被 gitignore 忽略），再通过 Gradle 的 buildConfig 读进代码。搜索"Android 隐藏 API Key 的最佳实践"照着改即可。
:::

#### 二、网络层：Retrofit + JSON 解析

先照 API 返回的 JSON 定义"数据模型"，字段对不上的一律忽略：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 数据模型 + 接口</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"晴"}],"main":{"temp":26.5,"humidity":40},"name":"北京"}
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
        @Query("lang") lang: String = "zh_cn"
    ): WeatherResponse
}
```
:::

Gson 会自动把 JSON 塞进这些 data class——<strong>字段名一致，魔法自动发生</strong>。

#### 三、三种界面状态：加载中 / 成功 / 失败

联网 App 的灵魂在于"状态管理"。网络慢、断网、城市名打错……每种情况界面都要给用户交代。用一个 sealed class（密封类）优雅地表示：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 界面状态</span><span class="dots">···</span>
:::

```
sealed class UiState {
    object Loading : UiState()                    // 转圈中
    data class Success(val data: WeatherResponse) : UiState()  // 成功
    data class Error(val message: String) : UiState()          // 失败
}

// ViewModel 里：
fun search(city: String) {
    viewModelScope.launch {
        _state.value = UiState.Loading
        _state.value = try {
            UiState.Success(api.getWeather(city))
        } catch (e: Exception) {
            UiState.Error("查不到这个城市，换个名字试试？")
        }
    }
}

// 界面里：
when (val s = state) {
    is UiState.Loading -&gt; CircularProgressIndicator()   // 转圈
    is UiState.Success -&gt; WeatherContent(s.data)        // 展示
    is UiState.Error -&gt; Text(s.message)                 // 报错
}
```
:::

这个 <code class="inline">Loading/Success/Error</code> 三段式是联网界面的"万金油模板"，先背下来，以后所有联网 App 照葫芦画瓢。

#### 四、实战界面代码：把天气画出来

状态有了，界面长这样（关键片段）：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 天气界面（核心片段）</span><span class="dots">···</span>
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
            data.weather.firstOrNull()?.description ?: "未知",
            fontSize = 20.sp,
            color = Color.Gray
        )
        Spacer(Modifier.height(16.dp))
        Row {
            Text("💧 湿度 ${data.main.humidity}%")
            Spacer(Modifier.width(24.dp))
            Text("🌡️ 体感 ${data.main.temp}°C")
        }
    }
}
```
:::

几个小细节值得学：<code class="inline">firstOrNull()</code> 安全取第一个元素（列表可能为空），<code class="inline">?: "未知"</code> 给兜底文案——空安全原则在界面里同样适用。温度用 <code class="inline">72.sp</code> 的大字号撑场面，"轻"字重（Light）让数字显得优雅，这是天气类 App 的经典配方。

#### 五、界面与交互细节

- <strong>搜索框</strong>：顶部 TextField，输城市名点搜索（键盘上设"搜索"动作，回车即搜）；
- <strong>天气卡片</strong>：大字号温度（26.5°）、天气描述（晴）、湿度、城市名；
- <strong>收藏城市</strong>：把常看的城市存进 DataStore，下次打开自动查——顺手复习第 6 章；
- <strong>下拉刷新</strong>：Compose 里用 <code class="inline">PullToRefreshBox</code>（Material 3 提供），手感立刻"专业"起来。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：图片让界面活起来

{class="mt-1"}
给每种天气配一个 emoji 或图标（☀️🌧️❄️），用 <code class="inline">when(description)</code> 映射——三行代码，界面温度感翻倍。也可以加载第三方的天气图标库，但练手阶段 emoji 足够。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：天气 App 验收清单

{class="mt-1"}
① 正常搜索出天气；② 断开网络，App 优雅报错不崩溃（开飞行模式测！）；③ 输一个不存在的城市，提示友好；④ 收藏两个城市，重启 App 还在；⑤ 转屏不丢状态。五条全过，这个项目才算毕业。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 先浏览器试 API、看懂 JSON，再写代码——"预习"永远不亏
- API Key 藏进 local.properties，绝不进代码库
- Retrofit 接口 + data class：字段对上，JSON 自动解析
- Loading/Success/Error 三段式状态是联网界面万金油
- 断网、空输入、城市不存在——错误处理是联网 App 的及格线
:::
