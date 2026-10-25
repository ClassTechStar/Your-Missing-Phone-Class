---
id: di-wu-shi-wu-zhang
num: 55
part: an-zhuo-kai-fa-pian
nav: Chapter 55: Project 2 — Weather App (Networked Version)
toc: default
kind: chapter
---

### Chapter 55: Project 2 — Weather App (Networked Version)

{class="chapter-intro mb-4"}
The expense tracker was "internal training"; the weather app is "seeing the world" — it has to deal with the internet. In this project you'll learn to: apply for a free API, parse JSON, handle the three UI states of "loading/success/failure," and keep your API key well hidden. Finish it, and you can build any "connected app" — news, exchange rates, translation; the recipe is exactly the same.

#### 1. Apply for a Free Weather API

For personal practice, OpenWeatherMap or China's QWeather are good picks — both have free tiers that work right after you sign up. Taking OpenWeatherMap as an example:

1. Sign up for an account → generate a key (apikey) on the API keys page;
2. The free tier can call the Current Weather endpoint: api.openweathermap.org/data/2.5/weather? q=beijing&appid=YOUR_KEY&units=metric;
3. Try it in your browser first to see what the returned JSON looks like — this "preview" is a must before wiring up any API.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Watch out: never hard-code your key into the code

{class="mt-1"}
An API key is like your "wallet password" — the moment it's committed to GitHub, bots will scrape and abuse it within hours. The right way: put it in local.properties (a file already ignored by gitignore), then read it into your code through Gradle's buildConfig. Search for "best practices for hiding API keys on Android" and follow along.
:::

#### 2. The Network Layer: Retrofit + JSON Parsing

First define your "data model" based on the JSON the API returns; ignore any fields that don't match:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Data model + interface</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"Sunny"}],"main":{"temp":26.5,"humidity":40},"name":"Beijing"}
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
        @Query("lang") lang: String = "en"
    ): WeatherResponse
}
```
:::

Gson automatically stuffs the JSON into these data classes — the field names line up, and the magic happens on its own.

#### 3. Three UI States: Loading / Success / Failure

The soul of a connected app is "state management." Slow network, no connection, a mistyped city name... the UI needs an answer for the user in every case. Express it elegantly with a sealed class:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · UI state</span><span class="dots">···</span>
:::

```
sealed class UiState {
    object Loading : UiState()                    // spinner showing
    data class Success(val data: WeatherResponse) : UiState()  // success
    data class Error(val message: String) : UiState()          // failure
}

// In the ViewModel:
fun search(city: String) {
    viewModelScope.launch {
        _state.value = UiState.Loading
        _state.value = try {
            UiState.Success(api.getWeather(city))
        } catch (e: Exception) {
            UiState.Error("Can't find that city — try another name?")
        }
    }
}

// In the UI:
when (val s = state) {
    is UiState.Loading -&gt; CircularProgressIndicator()   // spinner
    is UiState.Success -&gt; WeatherContent(s.data)        // show
    is UiState.Error -&gt; Text(s.message)                 // error
}
```
:::

This Loading/Success/Error three-part pattern is the "all-purpose template" for connected screens. Memorize it now, and every connected app you build later just follows the mold.

#### 4. Real UI Code: Drawing the Weather

With the states in place, the UI looks like this (key excerpts):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Weather screen (core excerpt)</span><span class="dots">···</span>
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
            data.weather.firstOrNull()?.description ?: "Unknown",
            fontSize = 20.sp,
            color = Color.Gray
        )
        Spacer(Modifier.height(16.dp))
        Row {
            Text("💧 Humidity ${data.main.humidity}%")
            Spacer(Modifier.width(24.dp))
            Text("🌡️ Feels like ${data.main.temp}°C")
        }
    }
}
```
:::

A few small details worth learning: firstOrNull() safely grabs the first element (the list may be empty), and ?: "Unknown" provides fallback text — the null-safety principle applies in UI code too. The temperature uses a big 72.sp font to anchor the screen, and the Light weight makes the number look elegant — a classic recipe for weather apps.

#### 5. UI and Interaction Details

- Search box: a TextField at the top; type a city name and tap search (set the keyboard's "Search" action so Enter searches);
- Weather card: a large-font temperature (26.5°), the weather description (Sunny), the humidity, and the city name;
- Favorite cities: save the cities you check often into DataStore and query them automatically on next launch — a handy review of Chapter 6;
- Pull to refresh: use PullToRefreshBox in Compose (provided by Material 3) and the feel instantly turns "professional."

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tip: images bring the UI to life

{class="mt-1"}
Give each kind of weather an emoji or icon (☀️🌧️❄️), mapped with when(description) — three lines of code, and the UI feels twice as warm. You could also load a third-party weather icon library, but for practice, emoji is plenty.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Hands-on: weather app acceptance checklist

{class="mt-1"}
(1) A normal search returns the weather; (2) with the network cut off, the app reports the error gracefully instead of crashing (test with airplane mode!); (3) entering a nonexistent city shows a friendly message; (4) two favorite cities survive an app restart; (5) rotating doesn't lose state. Only when all five pass does this project graduate.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Chapter Summary

- Test the API in the browser and understand the JSON before writing code — "previewing" never hurts
- Hide the API key in local.properties; never let it into the codebase
- Retrofit interface + data classes: fields line up, and the JSON parses itself
- The Loading/Success/Error three-part state pattern is the all-purpose tool for connected screens
- No connection, empty input, unknown city — error handling is the passing grade for connected apps
:::
