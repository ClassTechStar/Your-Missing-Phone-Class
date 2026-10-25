---
id: di-wu-shi-san-zhang
num: 53
part: an-zhuo-kai-fa-pian
nav: פרק 53: אחסון נתונים ובקשות רשת
toc: default
kind: chapter
---

### פרק 53: אחסון נתונים ובקשות רשת

{class="chapter-intro mb-4"}
אפליקציה שאפשר רק "להסתכל" בה היא אפליקציה מתה; אפליקציה שיודעת לשמור נתונים ולהתחבר לרשת היא אפליקציה חיה. בפרק הזה נכיר את "שלושת אביזרי" שכבת הנתונים של אנדרואיד: DataStore (שמירת הגדרות קטנות), Room (שמירת נתונים מובנים) ו-Retrofit (דיבור עם השרת), ובנוסף את "המרכז המתאם" שלהם – הקורוטינות. אחרי הפרק הזה תוכלו לכתוב אפליקציה אמיתית שזוכרת את הרגלי המשתמש ומעדכנת תוכן בזמן אמת.

#### א' איך בוחרים שיטת אחסון: קודם כול תסתכלו על הטבלה

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">שיטה</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">מה מתאים לשמור</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">מאפיינים</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">היכן נשתמש בספר</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DataStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">הגדרות בודדות (ערכת עיצוב, מתגי הפעלה)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">צמדי מפתח-ערך; פשוט ובטוח</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">הגדרות ספר החשבונות בפרק 54</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">נתונים מובנים (רשומות כספים, משתמשים)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">עטיפה של מסד נתונים SQLite אמיתי, עם תמיכה בשאילתות</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">רשומות החשבונות בפרק 54</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">נתוני שרת (לא שומרים – מביאים מהרשת)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">הסטנדרט המעשי לספריות בקשות HTTP</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">נתוני מזג האוויר בפרק 55</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
חלוקת התפקידים של שלושת אביזרי הנתונים

זכרו קריאת כיוון אחת: "הגדרות קטנות נכנסות ל-DataStore, נתונים בכמויות נכנסים ל-Room, נתונים מבחוץ עוברים ב-Retrofit". ה-SharedPreferences המוכר ממדריכים ישנים הוחלף ב-DataStore, וכתיבת SQL ידנית ל-SQLite הוחלפה ב-Room – למדו ישירות את החדש, אל תלכו בדרך הישנה.

#### ב' DataStore: שמירת הגדרות קטנות

כדי לזכור ערכים בודדים כמו "המטבע שהמשתמש בחר בפעם הקודמת" או "האם מצב כהה מופעל", השתמשו ב-DataStore (הגרסה ל-Preferences):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · דוגמת DataStore</span><span class="dots">···</span>
:::

```
val Context.dataStore by preferencesDataStore(name = "settings")

// כתיבה: לשמור ערך
suspend fun saveTheme(isDark: Boolean) {
    context.dataStore.edit { prefs ->
        prefs[THEME_KEY] = isDark
    }
}

// קריאה: להוציא את הערך (‏Flow מודיע על שינויים אוטומטית)
val themeFlow: Flow<Boolean> = context.dataStore.data
    .map { it[THEME_KEY] ?: false }
```
:::

שימו לב שהתשובה היא Flow – זרימת נתונים "זורמת". ברגע שהערך משתנה, כל המקומות שצופים בו מקבלים את הערך החדש אוטומטית. המושג הזה (תכנות ריאקטיבי) הוא אבן היסוד של האנדרואיד המודרני; נתרגל אותו בפרק 54.

#### ג' Room: לתת לנתונים "בית אמיתי"

ספר חשבונות מכיל מאות ואף אלפי רשומות, וצריך גם לשאול ולסכם לפי קטגוריה ולפי חודש – וזה דורש מסד נתונים. Room היא העטיפה הרשמית של SQLite, שהופכת "יצירת טבלאות ושאילתת נתונים" לטבעית כמו כתיבת Kotlin. שלושה דברים:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · שלישיית Room: Entity / Dao / Database</span><span class="dots">···</span>
:::

```
// 1. ‏Entity: מבנה הטבלה (טבלה אחת = data class אחד)
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val amount: Double,
    val category: String,
    val note: String,
    val date: String
)

// 2. ‏Dao: ממשק הפעולות (הוספה, מחיקה, עדכון, שליפה)
@Dao
interface RecordDao {
    @Query("SELECT * FROM records ORDER BY date DESC")
    fun getAll(): Flow<List<Record>>

    @Insert
    suspend fun insert(record: Record)

    @Delete
    suspend fun delete(record: Record)

    @Query("SELECT SUM(amount) FROM records WHERE category = :c")
    suspend fun sumByCategory(c: String): Double
}

// 3. ‏Database: ההרכבה הסופית
@Database(entities = [Record::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun recordDao(): RecordDao
}
```
:::

את תבנית "שלושת האביזרים" הזאת אפשר להעביר כמו שהיא לכל פרויקט שלכם – פשוט משנים את שמות השדות. השאילתות מחזירות Flow, והמסך מתרענן אוטומטית יחד עם הנתונים – קסם אמיתי.

#### ד' Retrofit: לדבר עם השרת

מזג אוויר, חדשות, שערי מטבעות... הנתונים האלה לא נמצאים בטלפון אלא על שרתים של אחרים. Retrofit הופך את "לבקש נתונים מהשרת" לפשוט כמו קריאה לפונקציה. שלושה שלבים:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Retrofit בשלושה שלבים</span><span class="dots">···</span>
:::

```
// 1. להגדיר את הממשק: לתאר בקשות HTTP כפונקציות
interface WeatherApi {
    @GET("v1/weather")
    suspend fun getWeather(@Query("city") city: String): WeatherResponse
}

// 2. יצירת המופע
val api = Retrofit.Builder()
    .baseUrl("https://api.example.com/")
    .addConverterFactory(GsonConverterFactory.create())
    .build()
    .create(WeatherApi::class.java)

// 3. לקרוא כמו לפונקציה רגילה (בתוך קורוטינה)
val result = api.getWeather("תל אביב")
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
אזהרה: שני כללי ברזל של הרשת

{class="mt-1"}
① אסור לבצע בקשות רשת בת'רד הראשי – זה יקפיא את המסך ואף יגרום לקריסה (NetworkOnMainThreadException). את כל קריאות הרשת יש לבצע בתוך קורוטינות (viewModelScope.launch). ② HTTP בלתי מוצפן אסור כברירת מחדל: החל מאנדרואיד 9 נדרש HTTPS. אם בזמן בדיקות תרצו להשתמש בכתובת מקומית http://, יש להצהיר על כך במפורש ב-Manifest עם usesCleartextTraffic – אבל במוצר רשמי הכול חייב לעבור ב-HTTPS.
:::

#### ה' פענוח JSON: "תרגום" נתוני הרשת

רוב הנתונים שהשרת מחזיר הם JSON – טקסט שנראה כמו "מילון מקונן". Retrofit זקוק ל"מתרגם" שהופך אותו לאובייקטים של Kotlin. שתי השיטות המובילות ב-2026:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">שיטה</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">מאפיינים</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">תרחיש מומלץ</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gson / Moshi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">השיטה הוותיקה מבוססת ה-Reflection, בלי שום הגדרות</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">התחלה מהירה, פרויקטים קטנים עם מעט שדות</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">kotlinx.serialization</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">הפתרון הרשמי בזמן הידור; מהיר ובטוח יותר</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">הבחירה הראשונה לפרויקטים חדשים (הזרם המרכזי ב-2026)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
שתי שיטות פענוח ה-JSON המובילות

::: div .code-block
:::inline div .code-head
<span>KOTLIN · דוגמת kotlinx.serialization</span><span class="dots">···</span>
:::

```
// הוסף את האנוטציה @Serializable ל-data class
@Serializable
data class WeatherResponse(
    val weather: List<Weather>,
    val main: Main,
    val name: String
)

// מחברים ל-Retrofit את ה-Converter המתאים (דוגמה עם התמיכה הרשמית של Retrofit 2.11+):
// .addConverterFactory(json.asConverterFactory("application/json".toMediaType()))
```
:::

בכל שיטה שתבחרו, כלל הברזל הוא: קודם תסתכלו על ה-JSON האמיתי שמוחזר, ורק אז הגדירו את השדות. הרבה באגים של "פענוח נכשל" נובעים משם שדה שגוי או מהערכה לא נכונה של רמות הקינון – הדפיסו את ה-JSON הגולמי והשוו, ותאתרו את הבעיה בעשר שניות.

#### ו' קורוטינות: "השפה המשותפת" של המקביליות באנדרואיד

ה-suspend וה-launch שמופיעים שוב ושוב למעלה מגיעים מהקורוטינות של Kotlin (Coroutine) – פתרון המקביליות הרשמי של אנדרואיד. בגסות אפשר להבין זאת כך: פעולות "שצריך לחכות להן קצת" (רשת, מסד נתונים) לא חוסמות את המסך.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · היכרות ראשונה עם קורוטינות</span><span class="dots">···</span>
:::

```
// הפעלת קורוטינה בתוך ה-ViewModel
viewModelScope.launch {
    val records = dao.getAll().first()  // suspend: מושהה וממתין אוטומטית
    // לעדכן את מצב הממשק…
}

// פתק זיכרון למילות המפתח:
// suspend   —— "אני צריך לחכות, אל תחסום לאחרים"
// launch    —— "קדימה, לעבודה!"
// viewModelScope —— "סדנת העבודה" שהולכת אחרי המסך; נסגרת מעצמה כשהמסך נהרס
```
:::

בלי רקע – פשוט זכרו את השימוש; את עיקרון "ההשהיה וההמשך" שמאחור אפשר לחקור מאוחר יותר. בפיתוח היומיומי כ-90% מהקוד שתכתבו יהיה בדיוק התבנית הזאת.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
הגיע הזמן להתנסות: בנו אפליקציה קטנה של "משפט היום"

{class="mt-1"}
מצאו API חינמי לציטוטים (למשל hitokoto וכדומה), משכו עם Retrofit את "משפט היום", הציגו אותו במרכז המסך והוסיפו כפתור "עוד אחד" (ששולח בקשה חדשה בתוך קורוטינה). ואז שמרו משפטים אהובים ב"מועדפים" באמצעות Room. התרגיל הזה משתמש ב-DataStore/Room/Retrofit/קורוטינות כולם – אחריו, פרקים 7 ו-8 יהיו קלים כמו עוגה.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
סיכום הפרק

- קריאת הכיוון: הגדרות קטנות נכנסות ל-DataStore, נתונים בכמויות נכנסים ל-Room, נתונים מבחוץ עוברים ב-Retrofit
- ‏DataStore מחזיר Flow: הערך השתנה? הצופים מקבלים זאת אוטומטית
- שלושת אביזרי Room: ‏@Entity (טבלה) + ‏@Dao (פעולות) + ‏@Database (הרכבה סופית) – תבנית לשימוש חוזר ישיר
- שלושה שלבים ב-Retrofit: הגדרת ממשק → יצירת מופע → קריאה בתוך קורוטינה
- שני כללי ברזל: לא רשת בת'רד הראשי; מוצר רשמי – חובה HTTPS
- קורוטינה = המתנה שלא חוסמת את המסך; ‏viewModelScope הוא חדר העבודה הייעודי של המסך
:::
