---
id: di-liu-shi-san-zhang
num: 63
part: ios-kai-fa-pian
nav: פרק 63: תצוגות, מצבים וניווט
toc: default
kind: chapter
---

### פרק 63: תצוגות, מצב וניווט

{class="chapter-intro mb-4"}
כבר יודעים לבנות צעצוע של עמוד אחד. הפרק הזה פותר שתי בעיות של "גדילה": איך מדלגים בין מספר מסכים (ניווט), ואיך נתונים זורמים בין המסכים (ניהול מצב). אחרי הפרק הזה תוכלו להקים שלד קלאסי של אפליקציה מרובת מסכים: "רשימה → פרטים → עריכה".

#### 1. "התמונה המלאה" של זרימת הנתונים בניהול מצב

ב-SwiftUI כלי ניהול המצב לא מסתכמים ב-@State. קודם תסתכלו על התמונה המלאה ותבינו "מתי משתמשים במה":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">כלי</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">על מה מפקח</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">מי משתמש בו</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">תרחיש טיפוסי</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מצב זמני פרטי למסך</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">התצוגה הנוכחית</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מונה, טקסט בשדה קלט</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Binding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">השאלת מצב מאחר</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">תצוגת בת משנה את תצוגת האב</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">רכיב מותאם אישית</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@StateObject / @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">לוגיקה משותפת בין מסכים</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מודל תצוגה (ViewModel)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">טעינת נתונים, לוגיקה עסקית</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@EnvironmentObject / .environment</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מצב משותף גלובלי</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">כל האפליקציה</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מצב התחברות המשתמש, הגדרות עיצוב</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
תמונת מצב מלאה של כלי המצב ב-SwiftUI (2026; @Observable כבר הבחירה המובילה)

::: div .code-block
:::inline div .code-head
<span>SWIFT · הסטנדרט ב-2026: view models עם @Observable</span><span class="dots">···</span>
:::

```
// הדרך המודרנית של iOS 17+: המאקרו @Observable (מומלץ לפרויקטים חדשים)
import Observation

@Observable
class CounterModel {                 // מודל התצוגה
    var count = 0
    func increment() { count += 1 }
}

struct CounterView: View {
    @State private var model = CounterModel()   // מחזיק את המודל

    var body: some View {
        VStack {
            Text("לחצת \(model.count) פעמים")
            Button("לחץ כאן") { model.increment() }
        }
    }
}
```
:::

עצה בוטה למתחילים: למצב פרטי למסך — @State; למה שחוצה מסכים או כולל לוגיקה — מחלקת @Observable. במדריכים ישנים תמצאו @StateObject/@ObservableObject — זוהי הגישה של הדור הקודם; מספיק להבין אותה, ובקוד חדש ללכת לפי מה שלמעלה.

#### 2. NavigationStack: ה"מחסנית" של מעברי מסך

מ-iOS 16 ואילך מנווטים בין מסכים עם NavigationStack — כמו ערימת צלחות: דוחפים אחת פנימה, ובחזרה שולפים אחת-אחת:

::: div .code-block
:::inline div .code-head
<span>SWIFT · ניווט עם NavigationStack</span><span class="dots">···</span>
:::

```
struct HomeView: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("הפנקס של דני") {
                    DetailView(name: "הפנקס של דני")   // מסך היעד
                }
                NavigationLink("הפנקס של נועה") {
                    DetailView(name: "הפנקס של נועה")
                }
            }
            .navigationTitle("רשימת הפנקסים")   // כותרת גדולה למעלה
        }
    }
}

struct DetailView: View {
    let name: String
    var body: some View {
        Text("פרטי \(name)")
            .navigationTitle(name)
            .navigationBarTitleDisplayMode(.inline)
    }
}
```
:::

NavigationLink הוא "קישור שאפשר ללחוץ עליו ולעבור מסך"; navigationTitle יוצר אוטומטית כותרת לסרגל הניווט וכפתור חזרה. למעבר מתוכנת (למשל חזרה אוטומטית אחרי לחיצה על "שמור") משתמשים ב-@Environment(\.dismiss) לסגירת המסך הנוכחי — בשילוב שני הטריקים האלה מכוסים 90% מצרכי הניווט.

#### 3. חלוניות קופצות ותגיות תחתונות: sheet ו-TabView

מלבד "דחיפת מסך" יש שני אינטראקציות קלאסיות נוספות:

::: div .code-block
:::inline div .code-head
<span>SWIFT · חלוניות sheet + טאבים עם TabView</span><span class="dots">···</span>
:::

```
// 1. sheet שעולה מלמטה, חצי מסך או מסך מלא (האהובה על טפסי הזנה)
struct HomeView: View {
    @State private var showAdd = false
    var body: some View {
        Button("לרשום הוצאה") { showAdd = true }
            .sheet(isPresented: $showAdd) {
                AddRecordView()     // מסך ההזנה שנפתח
            }
    }
}

// 2. סרגל טאבים תחתון ("השלד" של האפליקציה)
struct MainTabView: View {
    var body: some View {
        TabView {
            RecordListView()
                .tabItem { Label("פנקס", systemImage: "book") }
            StatsView()
                .tabItem { Label("סטטיסטיקה", systemImage: "chart.pie") }
            SettingsView()
                .tabItem { Label("הגדרות", systemImage: "gear") }
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
טיפ: מתי משתמשים במה?

{class="mt-1"}
כלל אצבע: את הזרימה הראשית דוחפים עם NavigationStack (רשימה → פרטים), פעולות זמניות נפתחות בחלונית sheet (הוספה, עריכה, אישור), ובלוקים ראשיים שעומדים בפני עצמם — ב-TabView (תגיות תחתונות). השילוב של השלושה הוא השלד של רוב האפליקציות.
:::

#### 4. List: הרשימה "הלאומית" של iOS

הרכיב הכי שכיח והכי "אפלי" ב-iOS הוא List — עם קווי הפרדה, מחיקה בהחלקה והדגשה בהקשה, מובנים מטבעם:

::: div .code-block
:::inline div .code-head
<span>SWIFT · רשימות עם List + מחיקה בהחלקה</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var records = ["צהריים 25.5", "מטרו 6.0", "משכורת +8000"]

    var body: some View {
        List {
            ForEach(records, id: \.self) { r in
                Text(r)
            }
            .onDelete { indexSet in          // החלקה שמאלה למחיקה
                records.remove(atOffsets: indexSet)
            }
        }
    }
}
```
:::

רשימה + NavigationLink + sheet + TabView — בשילוב ארבעת אלה תוכלו להקים כבר שלד אפליקציה שלם: "רשימת חשבונות → פתיחת פרטים → לחיצה על + לפתיחת חלונית הזנה". פרויקט ספר החשבונות בפרק הבא נבנה בדיוק כך.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
הידיים על ההגה: בונים "שלד של שלושה מסכים"

#### 5. מחזור החיים של האפליקציה: חזית ורקע

בדומה למחזור החיים של ה-Activity ב-Android, גם לאפליקציית iOS יש מעברי מצב של "לידה, חזית, רקע ומוות". ב-SwiftUI עוקבים אחריהם בערך הסביבה scenePhase:

::: div .code-block
:::inline div .code-head
<span>SWIFT · מעקב אחר מעבר חזית/רקע</span><span class="dots">···</span>
:::

```
@main
struct MyApp: App {
    @Environment(\.scenePhase) private var phase

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .onChange(of: phase) { _, newPhase in
            switch newPhase {
            case .active:    print("חזרה לחזית: לחדש את הרענון")
            case .inactive:  print("במעבר (שיחה או רגע המעבר לרקע)")
            case .background: print("מעבר לרקע: לשמור טיוטה")
            @unknown default: break
            }
        }
    }
}
```
:::

שימושים טיפוסיים: רענון נתונים בחזרה לחזית, שמירת טיוטה בכניסה לרקע. iOS מפקח בקפדנות על ריצה ברקע — אפליקציה רגילה מושעית (מוקפאת) זמן קצר אחרי שיורדת לרקע, ואל תקוו לבצע עבודה כבדה בחשאי ברקע; למשימות מתוזמנות באמת השתמשו בהתראות המקומיות של פרק 68, ולא ב"ריצת רקע קבועה".

{class="mt-1"}
בנו שלד של ספר חשבונות עם נתוני דמה: TabView עם שלוש תגיות (חשבונות/סטטיסטיקה/הגדרות) → עמוד החשבונות מציג נתוני דמה ב-List, לחיצה על שורה עוברת למסך הפרטים (NavigationStack) → כפתור "+" בפינה העליונה פותח חלונית הזנה ב-sheet. בלי שמירת נתונים ובלי אינטרנט — תרגול שלד טהור; כשהשלד הזה מוכן, מילוי הנתונים האמיתיים בפרק 65 יזרום מאליו.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
סיכום הפרק

- ארבעת כלי המצב: @State (פרטי למסך), @Binding (השאלה), @Observable (לוגיקה), .environment (גלובלי)
- בפרויקטים חדשים כותבים מודלי תצוגה עם המאקרו @Observable; את @ObservableObject מהמדריכים הישנים מספיק להבין
- NavigationStack דוחף מסכים; @Environment(\.dismiss) לחזרה מתוכנת
- בזרימה הראשית דוחפים מסכים, פעולות זמניות נפתחות ב-sheet, ובלוקים ראשיים עוברים עם TabView
- List הוא "הרשימה הלאומית": קווי הפרדה ומחיקה בהחלקה מוכנים מהקופסה
:::
