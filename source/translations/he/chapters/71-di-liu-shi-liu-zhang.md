---
id: di-liu-shi-liu-zhang
num: 66
part: ios-kai-fa-pian
nav: פרק 66: פרויקט 2 – אפליקציית מזג האוויר (גרסת רשת)
toc: default
kind: chapter
---

### פרק 66: פרויקט 2 — אפליקציית חיפוש מזג אוויר (גרסת רשת)

{class="chapter-intro mb-4"}
ספר החשבונות היה "אימון פנימי", ואפליקציית מזג האוויר היא "יציאה אל העולם" — היא צריכה להתמודד עם האינטרנט. בפרויקט הזה תלמדו: לבקש API חינמי, לנתח JSON, לטפל בשלושה מצבי ממשק — "טוען / הצלחה / כישלון" — וגם איך להחביא היטב את מפתח ה-API. כשתסיימו אותו, תהיה לכם היכולת לבנות כל "אפליקציה מחוברת" — חדשות, שערי מטבעות, תרגום; המתכון זהה בדיוק.

#### 1. מבקשים API חינמי למזג אוויר

לתרגול אישי מומלצים OpenWeatherMap או השירות הסיני QWeather (HeFeng) — לשניהם מכסה חינמית, ואפשר להתחיל מיד אחרי הרשמה. נדגים עם OpenWeatherMap:

1. נרשמים לחשבון → יוצרים מפתח (apikey) בעמוד API keys;
2. בגרסה החינמית אפשר לקרוא ל-Current Weather: api.openweathermap.org/data/2.5/weather? q=beijing&appid=המפתח-שלך&units=metric;
3. קודם נסו פעם אחת בדפדפן וראו איך נראה ה-JSON שחוזר — זו "ההכנה המוקדמת" שחובה לעשות לפני חיבור לכל API.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
אזהרה: אסור לקבע את המפתח בקוד

{class="mt-1"}
מפתח API הוא בעצם "הסיסמה לארנק" שלכם: ברגע שהוא נכתב בקוד ומועלה ל-GitHub, תוך שעות בוטים יסרקו אותו, יגנבו אותו וינצלו אותו לרעה. הדרך הנכונה ב-iOS: לשים אותו ב-Config.xcconfig (קובץ תצורה ש-gitignore כבר מתעלם ממנו) ולקרוא אותו לקוד דרך Info.plist. חפשו "ניהול מפתחות iOS xcconfig" ובצעו לפי ההדרכה.
:::

#### 2. שכבת הרשת: URLSession + Codable

קודם מגדירים את המודל לפי ה-JSON שה-API מחזיר, ואז כותבים את השירות:

::: div .code-block
:::inline div .code-head
<span>SWIFT · מודל נתונים + שירות</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"בהיר"}],"main":{"temp":26.5,"humidity":40},"name":"תל אביב"}
struct WeatherResponse: Codable {
    let weather: [Weather]
    let main: Main
    let name: String
}
struct Weather: Codable { let description: String }
struct Main: Codable { let temp: Double; let humidity: Int }

struct WeatherService {
    let key: String   // נקרא מ-xcconfig

    func fetchWeather(city: String) async throws -> WeatherResponse {
        var comps = URLComponents(string: "https://api.openweathermap.org/data/2.5/weather")!
        comps.queryItems = [
            URLQueryItem(name: "q", value: city),
            URLQueryItem(name: "appid", value: key),
            URLQueryItem(name: "units", value: "metric"),
            URLQueryItem(name: "lang", value: "zh_cn")
        ]
        let (data, _) = try await URLSession.shared.data(from: comps.url!)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}
```
:::

#### 3. שלושה מצבי ממשק: טוען / הצלחה / כישלון

הנשמה של אפליקציה מחוברת היא "ניהול מצבים". רשת איטית, ניתוק, שגיאת הקלדה בשם עיר... בכל מצב כזה הממשק חייב לתת למשתמש תשובה. מייצגים זאת באלגנטיות עם enum + switch:

::: div .code-block
:::inline div .code-head
<span>SWIFT · מצב הממשק</span><span class="dots">···</span>
:::

```
enum LoadState {
    case loading                  // טוען
    case success(WeatherResponse) // הצלחה
    case error(String)            // כישלון
}

@Observable
class WeatherViewModel {
    var state: LoadState = .loading
    private let service = WeatherService(key: Config.apiKey)

    func search(city: String) async {
        state = .loading
        do {
            let data = try await service.fetchWeather(city: city)
            state = .success(data)
        } catch {
            state = .error("לא הצלחתי למצוא את העיר הזאת, לנסות שם אחר?")
        }
    }
}

// בממשק:
switch vm.state {
case .loading: ProgressView("טוען…")
case .success(let d): WeatherContent(data: d)
case .error(let msg): Text(msg).foregroundColor(.secondary)
}
```
:::

המבנה התלת-חלקי הזה loading/success/error הוא "תבנית הכל-בו" של ממשקים מחוברים: שננו אותו קודם, ואחר כך העתיקו את התבנית בכל אפליקציה מחוברת.

#### 4. קוד ממשק מעשי: מציירים את מזג האוויר

::: div .code-block
:::inline div .code-head
<span>SWIFT · מסך מזג האוויר (קטע מרכזי)</span><span class="dots">···</span>
:::

```
struct WeatherContent: View {
    let data: WeatherResponse

    var body: some View {
        VStack(spacing: 12) {
            Text(data.name)
                .font(.title.bold())
            Text("\(Int(data.main.temp))°C")
                .font(.system(size: 76, weight: .thin))
            Text(data.weather.first?.description ?? "לא ידוע")
                .font(.title3)
                .foregroundColor(.secondary)
            HStack(spacing: 24) {
                Label("לחות \(data.main.humidity)%", systemImage: "humidity")
                Label("תחושה \(Int(data.main.temp))°C", systemImage: "thermometer")
            }
        }
        .padding()
    }
}
```
:::

כמה פרטים קטנים ששווה ללמוד: first? שולף את האיבר הראשון בבטחה (הרשימה עלולה להיות ריקה), ו-?? "לא ידוע" נותן טקסט גיבוי; מספר הטמפרטורה במשקל גופן דק 76 הוא המתכון הקלאסי של אפליקציות מזג אוויר; ו-Label הוא הרכיב הרשמי ל"אייקון+טקסט", מסודר יותר מ-HStack שהרכבתם ידנית.

#### 5. פרטי אינטראקציה וערים מועדפות

- שדה חיפוש: המודיפייר .searchable בראש המסך נותן את אינטראקציית החיפוש המובנית של המערכת, ובשליחה קוראים ל-vm.search;
- ערים מועדפות: שומרים את הערים שבודקים לעתים קרובות ב-UserDefaults, ובפתיחה הבאה מבצעים חיפוש אוטומטי;
- רענון במשיכה למטה: .refreshable { await vm.search(...) } — שורה אחת וזה נגמר;
- אייקוני מזג אוויר: ממפים לפי התיאור עם Image(systemName:) (sun.max / cloud.rain / snowflake), והממשק מיד מתעורר לחיים.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
טיפ: ה"בעיה" עם שמות ערים בסינית

{class="mt-1"}
התמיכה של OpenWeatherMap בשמות ערים בסינית מתונה: חיפוש "בייג׳ין" בסינית עלול להחזיר ריק בעוד "beijing" עובד כשורה. הפתרון המקצועי הוא להטמיע טבלת מיפוי "שם עיר → אנגלית/קואורדינטות" או להתחבר לשירות מזג אוויר סיני. בשלב התרגול מספיק לתמוך בשמות ערים בפין-יין/אנגלית — אל תילחמו עם זה.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
הידיים על ההגה: רשימת קבלה לאפליקציית מזג האוויר

#### 6. איך מנפים באגים בבקשות רשת: הדפסה, לכידת תעבורה וסימולציית רשת איטית

כשאפליקציה מחוברת מתקלקלת, בתשע מתוך עשרה מקרים הבעיה היא "הבקשה נשלחה לא נכון" או "התגובה לא נותחה נכון". שלושה כלי ניפוי:

1. הדפסת הנתונים הגולמיים: מדפיסים את String(data: data, encoding: .utf8) ורואים את ה-JSON המקורי — שמות השדות והסוגים לנגד העיניים, פי עשרה מהיר מלנחש;
2. כלי לכידת תעבורה: Proxyman החינמי במק או Charles יכולים ליירט את כל הבקשות והתגובות של האפליקציה — כמו צילום רנטגן שחושף את שכבת הרשת;
3. סימולציית רשת חלשה: בתפריט הסימולטור Features → Network Link Conditioner (צריך להוריד את הכלי מאתר המפתחים) אפשר לדמות 3G והשהיות גבוהות — ולחשוף בעיות חוויה מהסוג "הספינר מסתובב חצי נצח".

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
טיפ: הבקשה נתקעת ב-ATS?

{class="mt-1"}
אם הבקשה נכשלת מיד עם השליחה בשגיאת "App Transport Security", סביר מאוד שהשתמשתם בכתובת http:// לא מוצפנת. ממשקים רשמיים חייבים HTTPS; לדיבוג מקומי אפשר לפתוח חריגה זמנית (מוסיפים NSAllowsLocalNetworking ל-Info.plist), אבל זכרו לנקות את זה לפני העלייה לחנות.
:::

{class="mt-1"}
① חיפוש רגיל מציג מזג אוויר; ② ניתוק הרשת — האפליקציה מציגה שגיאה בעדינות בלי לקרוס (בדקו עם כיבוי הרשת של המק כשהסימולטור פועל!); ③ הזנת עיר שלא קיימת מציגה הודעה ידידותית; ④ שתי ערים מועדפות שורדות הפעלה מחדש של האפליקציה; ⑤ הממשק נעים לעין גם במצב הכהה. רק כשכל חמשת הסעיפים עוברים — הפרויקט הזה "מסיים בגרות".
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
סיכום הפרק

- קודם בודקים את ה-API בדפדפן ומבינים את ה-JSON, ורק אז כותבים קוד — "הכנה מוקדמת" אף פעם לא מפסידה
- מפתח ה-API מוחבא אל תוך xcconfig, ולעולם לא נכנס למאגר הקוד
- מודל Codable + URLSession עם async/await: כשהשדות תואמים, ה-JSON מנותח אוטומטית
- מצבים בשלושה שלבים loading/success/error הם תבנית הכל-בו של ממשקים מחוברים
- ניתוק רשת, קלט ריק, עיר שלא קיימת — טיפול בשגיאות הוא ציון העובר של אפליקציה מחוברת
:::
