---
id: di-wu-shi-wu-zhang
num: 55
part: an-zhuo-kai-fa-pian
nav: פרק 55: פרויקט 2 – אפליקציית מזג האוויר (גרסת רשת)
toc: default
kind: chapter
---

### פרק 55: פרויקט 2 – אפליקציית חיפוש מזג אוויר (גרסת רשת)

{class="chapter-intro mb-4"}
ספר החשבונות היה "תרגול פנימי"; אפליקציית מזג האוויר היא "יציאה לעולם" – היא מתמודדת עם האינטרנט. בפרויקט הזה תלמדו: להגיש בקשה ל-API חינמי, לפענח JSON, לטפל בשלושת מצבי המסך "טוען/הצלחה/כישלון" וכיצד להחביא היטב את מפתח ה-API. אחריו תהיו מצוידים לבנות כל "אפליקציית רשת" – חדשות, שערי מטבעות, תרגום; המתכון זהה.

#### א' הגשת בקשה ל-API חינמי למזג אוויר

לתרגול אישי מומלץ OpenWeatherMap או QWeather הסינית – לשניהם מכסה חינמית, נרשמים ומתחילים להשתמש מיד. ניקח לדוגמה את OpenWeatherMap:

1. נרשמים לחשבון → יוצרים Key (apikey) בעמוד API keys;
2. בגרסה החינמית אפשר לקרוא לממשק Current Weather (מזג האוויר הנוכחי): api.openweathermap.org/data/2.5/weather? q=beijing&appid=YOUR_KEY&units=metric;
3. קודם כול נסו פעם אחת בדפדפן ותראו איך נראה ה-JSON שמוחזר – זהו "תרגול מקדים" שחובה לעשות לפני חיבור לכל API.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
אזהרה: אסור לקבע את המפתח בקוד

{class="mt-1"}
‏API Key הוא בעצם "סיסמת הארנק" שלכם; ברגע שהוא נכנס לקוד ונשלח ל-GitHub, תוך כמה שעות סורקים אותו זחלנים ומנצלים לרעה. הדרך הנכונה: לשים אותו ב-local.properties (קובץ שכבר מנוטרל על ידי gitignore) ולקרוא אותו לקוד דרך buildConfig של Gradle. חפשו "שיטות מומלצות להסתרת API Key ב-Android" ופעלו לפי זה.
:::

#### ב' שכבת הרשת: Retrofit + פענוח JSON

קודם מגדירים "מודל נתונים" לפי ה-JSON שה-API מחזיר; שדות שאינם נכללים במודל פשוט מזניחים:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · מודל נתונים + ממשק</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"בהיר"}],"main":{"temp":26.5,"humidity":40},"name":"תל אביב"}
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

‏Gson מכניס את ה-JSON אוטומטית למחלקות ה-data class האלה – כששמות השדות תואמים, הקסם קורה מעצמו.

#### ג' שלושה מצבי מסך: טוען / הצלחה / כישלון

הנשמה של אפליקציית רשת היא "ניהול מצבים". רשת איטית, ניתוק, שם עיר שגוי... בכל מקרה המסך חייב לתת למשתמש תשובה. מייצגים זאת באלגנטיות עם sealed class (מחלקה אטומה):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · מצב הממשק</span><span class="dots">···</span>
:::

```
sealed class UiState {
    object Loading : UiState()                    // טוען
    data class Success(val data: WeatherResponse) : UiState()  // הצלחה
    data class Error(val message: String) : UiState()          // כישלון
}

// ב-ViewModel:
fun search(city: String) {
    viewModelScope.launch {
        _state.value = UiState.Loading
        _state.value = try {
            UiState.Success(api.getWeather(city))
        } catch (e: Exception) {
            UiState.Error("לא הצלחתי למצוא את העיר הזאת, לנסות שם אחר?")
        }
    }
}

// בממשק:
when (val s = state) {
    is UiState.Loading -&gt; CircularProgressIndicator()   // מחוון טעינה
    is UiState.Success -&gt; WeatherContent(s.data)        // מציג
    is UiState.Error -&gt; Text(s.message)                 // מציג את השגיאה
}
```
:::

שלשת המצבים Loading/Success/Error היא "תבנית הכול-בו" של מסכי רשת; שננו אותה קודם, ובכל אפליקציית רשת עתידית פשוט העתיקו את התבנית.

#### ד' קוד מסך בפועל: לצייר את מזג האוויר

יש מצבים – וכך נראה המסך (קטעים מרכזיים):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · מסך מזג האוויר (קטע מרכזי)</span><span class="dots">···</span>
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
            data.weather.firstOrNull()?.description ?: "לא ידוע",
            fontSize = 20.sp,
            color = Color.Gray
        )
        Spacer(Modifier.height(16.dp))
        Row {
            Text("💧 לחות ${data.main.humidity}%")
            Spacer(Modifier.width(24.dp))
            Text("🌡️ תחושה ${data.main.temp}°C")
        }
    }
}
```
:::

כמה פרטים קטנים שראוי ללמוד: ‏firstOrNull() לוקח בבטחה את האיבר הראשון (הרשימה עלולה להיות ריקה), ו-?: "לא ידוע" נותן טקסט גיבוי – עקרון הבטיחות מפני null תקף גם במסך. הטמפרטורה מוצגת בגודל גדול 72.sp כדי להרשים, ומשקל גופן "קל" (Light) מעניק למספרים אלגנטיות – זהו המתכון הקלאסי של אפליקציות מזג אוויר.

#### ה' פרטי מסך ואינטראקציה

- שדה חיפוש: ‏TextField בראש המסך; מקלידים שם עיר ולוחצים חיפוש (מגדירים במקלדת פעולת "חיפוש", ו-Enter מחפש מיד);
- כרטיס מזג אוויר: טמפרטורה בגודל גדול (26.5°), תיאור מזג האוויר (בהיר), לחות, שם העיר;
- ערים מועדפות: שומרים את הערים שבודקים לעתים קרובות ב-DataStore, ובפתיחה הבאה מבצעים חיפוש אוטומטי – בדרך גם חוזרים על פרק 6;
- רענון בגרירה למטה: ב-Compose משתמשים ב-PullToRefreshBox (מסופק על ידי Material 3), והתחושה מיד משתדרגת ל"מקצועית".

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
טיפ: תמונות מחיות את המסך

{class="mt-1"}
תנו לכל סוג מזג אוויר emoji או אייקון מתאים (☀️🌧️❄️) ומפו עם when(description) – שלוש שורות קוד, ותחושת החיים של המסך מוכפלת. אפשר גם להוסיף ספריית אייקוני מזג אוויר של צד שלישי, אבל בשלב התרגול emoji מספיק.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
הגיע הזמן להתנסות: רשימת קבלה לאפליקציית מזג האוויר

{class="mt-1"}
① חיפוש מזג אוויר רגיל עובד; ② מנתקים את הרשת – האפליקציה מציגה שגיאה באלגנטיות בלי לקרוס (בדקו עם מצב טיסה!); ③ מקלידים עיר שלא קיימת – מתקבלת הודעה ידידותית; ④ מוסיפים שתי ערים למועדפים – הן נשארות גם אחרי הפעלה מחדש; ⑤ סיבוב מסך לא מאבד מצב. רק אם כל חמשת הסעיפים עוברים – הפרויקט הזה מסיים בהצלחה.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
סיכום הפרק

- קודם בודקים את ה-API בדפדפן ומבינים את ה-JSON, ורק אז כותבים קוד – "תרגול מקדים" אף פעם לא מפסיד
- ‏API Key מוחבא לתוך local.properties, ואף פעם לא נכנס למאגר הקוד
- ממשק Retrofit + data class: השדות תואמים – ה-JSON מפוענח אוטומטית
- שלשת המצבים Loading/Success/Error היא התבנית האוניברסלית של מסכי רשת
- ניתוק, קלט ריק, עיר לא קיימת – טיפול בשגיאות הוא הציון העובר של אפליקציית רשת
:::
