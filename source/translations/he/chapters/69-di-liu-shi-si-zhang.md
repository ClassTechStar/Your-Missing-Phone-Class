---
id: di-liu-shi-si-zhang
num: 64
part: ios-kai-fa-pian
nav: פרק 64: אחסון נתונים ובקשות רשת
toc: default
kind: chapter
---

### פרק 64: אחסון נתונים ובקשות רשת

{class="chapter-intro mb-4"}
אפליקציה שאפשר רק "להסתכל" בה היא אפליקציה מתה; אפליקציה שיודעת לשמור נתונים ולהתחבר לרשת היא אפליקציה חיה. בפרק הזה נכיר את "שלישיית שכבת הנתונים" של iOS: UserDefaults (להגדרות קטנות), SwiftData (לנתונים מובנים) ו-URLSession (לתקשורת עם השרת), ולצידן את Codable לפענוח JSON ואת הגישה המודרנית async/await. אחרי הפרק הזה תוכלו לכתוב אפליקציות אמיתיות שזוכרות את הרגלי המשתמש ומעדכנות תוכן בזמן אמת.

#### 1. איך בוחרים פתרון אחסון: קודם כל הטבלה

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">פתרון</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">מה מתאים לאחסן</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">מאפיינים</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">איפה בספר</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">הגדרות מפוזרות (מתגים, העדפות)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">צמדי מפתח-ערך, פשוט וישיר</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ההגדרות בפרק 65; הערים המועדפות בפרק 66</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">נתונים מובנים (חשבונות, רשומות)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">עטיפת מסד הנתונים הרשמית; הצהרה בשורת @Model</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">רשומות החשבונות בפרק 65</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">נתוני שרת (לא שומרים — מביאים מהרשת)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">פריימוורק הרשת המובנה של המערכת, בלי תלות בצד שלישי</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">נתוני מזג האוויר בפרק 66</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
חלוקת התפקידים בשלישיית הנתונים

שיננו את הפזמון: "הגדרות קטנות נכנסות ל-UserDefaults, נתונים בכמויות נכנסים ל-SwiftData, ונתונים מבחוץ עוברים דרך URLSession". Core Data מהמדריכים הישנים עדיין עובד (SwiftData הוא המעטפת המודרנית שלו), אבל SQLite ידני אין כמעט סיבה לגעת — למדו ישר את החדש ואל תלכו בדרך הישנה.

#### 2. UserDefaults: שומרים כמה הגדרות קטנות

::: div .code-block
:::inline div .code-head
<span>SWIFT · דוגמת UserDefaults</span><span class="dots">···</span>
:::

```
// כתיבה: לשמור ערך
UserDefaults.standard.set(true, forKey: "isDarkMode")
UserDefaults.standard.set("תל אביב", forKey: "favoriteCity")

// קריאה: להוציא אותו (אם אין, מחזיר את ברירת המחדל)
let isDark = UserDefaults.standard.bool(forKey: "isDarkMode")
let city = UserDefaults.standard.string(forKey: "favoriteCity") ?? "תל אביב"

// מחיקה: הסרת מפתח
UserDefaults.standard.removeObject(forKey: "isDarkMode")
```
:::

זכרו שהוא מתאים רק להגדרות מפוזרות וקטנות — עשרות ומאות רשומות מפקידים אצל SwiftData; אל תתייחסו ל-UserDefaults כאל מסד נתונים (זה מאט את הפעלת האפליקציה ולא נוח לשאילתות).

#### 3. SwiftData: נותנים לנתונים "בית אמיתי"

SwiftData הוא פתרון מסד הנתונים הרשמי החל מ-iOS 17, שמפשט את "יצירת הטבלאות והוספה, מחיקה, עדכון ושליפה" לקצה: אנוטציית @Model אחת, ומחלקת הנתונים הופכת לטבלה במסד:

::: div .code-block
:::inline div .code-head
<span>SWIFT · דוגמת SwiftData</span><span class="dots">···</span>
:::

```
import SwiftData

// 1. ‏@Model: המחלקה הזאת הופכת אוטומטית ל"טבלה"
@Model
class Record {
    var amount: Double
    var category: String
    var note: String
    var date: Date

    init(amount: Double, category: String, note: String, date: Date) {
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date
    }
}

// 2. לחבר את הקונטיינר בנקודת הכניסה של האפליקציה
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: Record.self)   // מסד הנתונים מוכן
    }
}

// 3. ב-View קוראים עם @Query וכותבים עם @Environment
struct RecordListView: View {
    @Query(sort: \Record.date, order: .reverse) var records: [Record]
    @Environment(\.modelContext) private var context

    var body: some View {
        List(records) { r in
            Text("\(r.category) \(r.amount) יואן")
        }
    }

    func add(amount: Double, category: String) {
        let r = Record(amount: amount, category: category, note: "", date: Date())
        context.insert(r)     // לשמור
        try? context.save()   // שמירה לדיסק
    }
}
```
:::

את התבנית "@Model + modelContainer + @Query" אפשר להעביר כמו שהיא לכל פרויקט שלכם — רק להחליף שמות שדות. ברגע שהנתונים משתנים, @Query מרענן את הממשק אוטומטית — קסם ממש.

#### 4. Codable: "מתרגם" את ה-JSON

רוב הנתונים מהשרת מגיעים כטקסט JSON. פרוטוקול Codable של Swift גורם להמרה בין "JSON ⇄ מבנים" להתרחש אוטומטית — שמות השדות תואמים, והקסם קורה:

::: div .code-block
:::inline div .code-head
<span>SWIFT · פענוח JSON עם Codable</span><span class="dots">···</span>
:::

```
// JSON: {"name":"תל אביב","main":{"temp":26.5},"weather":[{"description":"בהיר"}]}
struct WeatherResponse: Codable {
    let name: String
    let main: Main
    let weather: [Weather]
}
struct Main: Codable { let temp: Double }
struct Weather: Codable { let description: String }

// ממחרוזת JSON למבנה
let decoder = JSONDecoder()
let data = jsonString.data(using: .utf8)!
let result = try decoder.decode(WeatherResponse.self, from: data)
print(result.weather[0].description)   // "בהיר"
```
:::

חוק ברזל: קודם מסתכלים על ה-JSON האמיתי שמגיע, ורק אז מגדירים שדות. הרבה באגים של "פענוח נכשל" נובעים משם שדה שגוי או מטיפוס שניחש שגוי (השרת שולח את המחרוזת "26.5" ואתם הצהרתם Double) — הדפיסו את ה-JSON הגולמי והשוו, ותאתרו את הבעיה בעשר שניות.

#### 5. URLSession + async/await: מדברים עם השרת

ב-iOS מתחברים לרשת עם ה-URLSession המובנה של המערכת, יחד עם async/await של Swift (פונקציות אסינכרוניות) — "לחכות לרשת" הופך טבעי כמו "לחכות לשליח":

::: div .code-block
:::inline div .code-head
<span>SWIFT · URLSession + async/await</span><span class="dots">···</span>
:::

```
struct WeatherService {
    // פונקציה אסינכרונית: async מסמן "אני צריך לחכות רגע", throws מסמן "עלול להיכשל"
    func fetchWeather(city: String) async throws -> WeatherResponse {
        let url = URL(string:
            "https://api.example.com/weather?city=\(city)")!
        let (data, _) = try await URLSession.shared.data(from: url)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}

// נקודת הקריאה (בתוך .task):
.task {
    do {
        let weather = try await service.fetchWeather(city: "תל אביב")
        // לעדכן את הממשק…
    } catch {
        print("שגיאה: \(error)")
    }
}
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
אזהרת מוקשים: שני חוקי ברזל של רשת

{class="mt-1"}
① חיבור לרשת חייב async/await, ובשום פנים לא חוסמים את הת׳רד הראשי — ממשק קפוא הוא חוויה ברמת התרסקות. התכנות המקבילי המובנה של Swift הופך את זה לטבעי, אבל אל תשכחו try await ו-do/catch. ② ATS אוסר כברירת מחדל על HTTP גלוי: iOS דורש HTTPS. בבדיקות מול שירות http:// מקומי צריך לפתוח חריגה זמנית ב-Info.plist (NSAppTransportSecurity), אבל מוצר רשמי חייב לעבוד כולו על HTTPS — גם צוות האישור של החנות משגיח על זה.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
הידיים על ההגה: בונים אפליקציה קטנה של "משפט ליום"

#### 6. גם לשגיאות רשת יש "דרגות": אל תשליכו את כל השגיאות על המשתמש

אין רשת, פסק זמן, 404, שרת 500... לכל שגיאה יש משפט אחר שהמשתמש צריך לראות:

::: div .code-block
:::inline div .code-head
<span>SWIFT · טיפול בשגיאות לפי דרגות</span><span class="dots">···</span>
:::

```
func friendlyMessage(_ error: Error) -> String {
    if let urlError = error as? URLError {
        switch urlError.code {
        case .notConnectedToInternet: return "אין רשת, לבדוק את החיבור?"
        case .timedOut:               return "פסק הזמן חלף, לנסות שוב מאוחר יותר?"
        case .cannotFindHost:         return "השרת לא נמצא"
        default:                      return "בעיית רשת: \(urlError.code)"
        }
    }
    if let d = error as? DecodingError {
        return "פורמט הנתונים שגוי (ייתכן שה-API השתנתה)"
    }
    return "שגיאה: \(error.localizedDescription)"
}
```
:::

תנו למשתמש "שפה אנושית" וליומן "שפת מקור" (print של ה-error המלא). אל תשלחו את הג׳יבריש האנגלי של error.localizedDescription ישר אל המשתמש — תחושת המוצר מסתתרת בפרטים האלה.

{class="mt-1"}
מצאו API חינמי לציטוטים (למשל hitokoto או דומיו), משכו עם URLSession + async/await את "המשפט ליום", הציגו אותו במרכז המסך והוסיפו כפתור "החלף משפט". אחר כך שמרו משפטים אהובים ב"מועדפים" עם SwiftData. התרגיל הזה מפעיל את UserDefaults/SwiftData/Codable/URLSession כולם יחד — אחרי שתסיימו אותו, פרקים 7 ו-8 יהיו קלים למדי.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
סיכום הפרק

- הפזמון: הגדרות קטנות ל-UserDefaults, נתונים בכמויות ל-SwiftData, נתונים מבחוץ דרך URLSession
- שלושת כלי הקסם של SwiftData: @Model מצהיר על הטבלה, modelContainer מצמיד את הקונטיינר, @Query לקריאה ו-context.insert לכתיבה
- Codable מתרגם את ה-JSON אוטומטית: השדות תואמים, והקסם קורה
- URLSession + async/await: חיבור לרשת הוא כמו לחכות לשליח; do/catch מטפל בכישלונות
- שני חוקי ברזל: לא חוסמים את הת׳רד הראשי; מוצר רשמי חייב HTTPS (ATS)
:::
