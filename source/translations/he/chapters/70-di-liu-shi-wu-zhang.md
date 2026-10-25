---
id: di-liu-shi-wu-zhang
num: 65
part: ios-kai-fa-pian
nav: פרק 65: פרויקט 1 – אפליקציית רישום ההוצאות שלי (גרסה מקומית)
toc: default
kind: chapter
---

### פרק 65: פרויקט 1 — ספר החשבונות שלי (גרסה מקומית)

{class="chapter-intro mb-4"}
ברוכים הבאים ל"פרויקט הרציני" הראשון שלכם. ספר החשבונות הזה לא מתחבר לרשת, אבל יש בו הכול: אפשר לרשום תנועה, לצפות בפירוט, לסכם לפי חודש ולמחוק ולערוך. אחרי שתסיימו אותו, תעברו מסע מלא של "נתונים → לוגיקה → ממשק". אל תמהרו להעתיק קוד — קודם חושבים לעומק ואז עושים; זה העיקרון הקבוע שלנו.

#### 1. חשיבה על דרישות: קודם שואלים חמש שאלות

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">מרכיב</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">תשובה</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who (למי זה מיועד)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">לשימוש עצמי; גם משפחה וחברים</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What (מה עושים)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">רישום הכנסות והוצאות, צפייה בפירוט התנועות, סיכום חודשי, סטטיסטיקה לפי קטגוריה</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why (למה)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">תרגול ידיים + הבנה לאן הכסף הולך</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How (איך)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift + SwiftUI + SwiftData + MVVM, מקומי לחלוטין בלי שרת</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint (אילוצים)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">להשלים תוך שבוע; תמיכה מ-iOS 17 ומעלה (מחסום SwiftData)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
חמשת מרכיבי הדרישות של ספר החשבונות

ואז מפרקים אותו לשלבים קטנים ש"כל אחד מהם שמיש": ① בניית שכבת נתונים ב-SwiftData (שתדע לשמור רשומה אחת); ② מסך רשימה (שיציג את התנועות); ③ חלון הזנה (שיאפשר להוסיף רשומה); ④ מחיקה ועריכה; ⑤ כרטיס סיכום חודשי. בסיום כל שלב, האפליקציה היא "משהו שאפשר להשתמש בו".

#### 2. שכבת הנתונים: נותנים ל"רישומים" בית

קודם מגדירים איך נראית רשומה אחת — השדות צריכים להספיק לצרכים, אבל אל תהיו חמדנים:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Record.swift (מודל)</span><span class="dots">···</span>
:::

```
import SwiftData

@Model
class Record {
    var type: String      // "income" הכנסה | "expense" הוצאה
    var amount: Double    // סכום (יואן)
    var category: String  // קטגוריה: אוכל, תחבורה, משכורת…
    var note: String      // הערה (רשות)
    var date: Date        // תאריך הרישום

    init(type: String, amount: Double, category: String, note: String = "", date: Date = Date()) {
        self.type = type
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
טיפ: למה הסכום מסוג Double?

{class="mt-1"}
אפליקציות פיננסיות רציניות משתמשות ב-Decimal (עשרון מדויק) כדי להימנע משגיאות נקודה צפה (הבעיה הישנה והמפורסמת שבה 0.1+0.2 ≠ 0.3). לפרויקט אימון Double מספיק בהחלט; אם יום אחד תפתחו מוצר פיננסי אמיתי, זכרו לעבור ל-Decimal או ל-"מספר Int שמחושב באגורות" — מלכודת שמפתחים רבים לפניכם נפלו בה.
:::

#### 3. MVVM: מפרידים בין הממשק ללוגיקה

לתת לממשק לגשת ישירות למסד הנתונים? זה יעבוד, אבל קוד הממשק יהפוך ארוך ומבולגן. ארכיטקטורת MVVM מחלקת תפקידים: View (הממשק) רק מצייר, ViewModel (מרכז הלוגיקה) מנהל נתונים, ו-Model (SwiftData) מנהל אחסון.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> תצוגה (ממשק SwiftUI)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel (מוקד הלוגיקה @Observable)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model (שכבת נתונים SwiftData)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
איור 4: מבנה שלוש השכבות של MVVM — הנתונים זורמים בכיוון אחד, וכל שכבה נשארת בגבולותיה
:::

::: div .code-block
:::inline div .code-head
<span>SWIFT · RecordViewModel.swift (שלד)</span><span class="dots">···</span>
:::

```
import Observation

@Observable
class RecordViewModel {
    var records: [Record] = []
    private let context: ModelContext

    init(context: ModelContext) { self.context = context }

    func load() {
        // סינון עם #Predicate של SwiftData + מיון
        let descriptor = FetchDescriptor<Record>(
            sortBy: [SortDescriptor(\.date, order: .reverse)]
        )
        records = (try? context.fetch(descriptor)) ?? []
    }

    func add(type: String, amount: Double, category: String, note: String) {
        let r = Record(type: type, amount: amount, category: category, note: note)
        context.insert(r)
        try? context.save()
        load()                       // טעינה מחדש, הממשק מתרענן
    }

    func delete(_ record: Record) {
        context.delete(record)
        try? context.save()
        load()
    }
}
```
:::

בממשק כותבים @State private var vm = RecordViewModel(...) ואז מציגים את הרשימה ישירות מ-vm.records — ברגע שהנתונים משתנים, הממשק מתרענן אוטומטית.

#### 4. הממשק: מסך רשימה + חלון הזנה

::: div .code-block
:::inline div .code-head
<span>SWIFT · מסך רשימת ההוצאות (קטע מרכזי)</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var vm: RecordViewModel
    @State private var showAdd = false

    var body: some View {
        NavigationStack {
            List {
                Section("יתרת החודש") {          // כרטיס סיכום
                    SummaryRow(records: vm.records)
                }
                Section("רשומות") {
                    ForEach(vm.records) { r in
                        RecordRow(record: r)
                    }
                    .onDelete { idx in
                        idx.forEach { vm.delete(vm.records[$0]) }
                    }
                }
            }
            .navigationTitle("פנקס ההוצאות שלי")
            .toolbar {
                Button { showAdd = true } label: {
                    Image(systemName: "plus")
                }
            }
            .sheet(isPresented: $showAdd) {
                AddRecordView(vm: vm)          // דיאלוג הזנה
            }
        }
    }
}
```
:::

עיקרי חלון ההזנה: לשדה הסכום מגדירים מקלדת .keyboardType(.decimalPad) (מקלדת מספרים), להכנסה/הוצאה — פקד מקטעים (Picker), לקטגוריה — בחירה מתפריט, ובלחיצה על "שמור" קוראים ל-vm.add(...) וסוגרים עם dismiss().

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
שימו לב: אל תתעצלו על בדיקות קלט

{class="mt-1"}
חובה לבדוק את שדה הסכום: ערך ריק, מספר שלילי וקלט בלתי חוקי כמו "abc" — את כולם צריך לחסום (בודקים עם Double(text); אם ההמרה נכשלת מתקבל nil). אחת הסיבות הנפוצות ביותר לקריסת אפליקציות היא "להניח שהקלט של המשתמש תמיד מתנהג יפה". זכרו: כל מה שמגיע מהמשתמש בודקים כאילו זה אויב.
:::

#### 5. עריכה, מחיקה וסיכום

- מחיקה: .onDelete של List נותן מחיקה בהחלקה שמאלה + חלון אישור (מחיקה בטעות היא הדבר שמשתמשי אפליקציות ניהול חשבונות שונאים יותר מכל);
- עריכה: לחיצה על שורה פותחת חלון עריכה עם הערכים המקוריים ממולאים מראש (לתקן מילה אחת קל יותר מלהקליד הכל מחדש);
- סיכום: מחשבים "הכנסות / הוצאות / יתרה של החודש" באמצעות filter + reduce ומציגים בכרטיס שבראש המסך:

::: div .code-block
:::inline div .code-head
<span>SWIFT · חישוב הסיכום החודשי</span><span class="dots">···</span>
:::

```
func monthSummary(_ records: [Record]) -> (income: Double, expense: Double) {
    let cal = Calendar.current
    let monthRecords = records.filter {
        cal.isDate($0.date, equalTo: Date(), toGranularity: .month)
    }
    let income = monthRecords
        .filter { $0.type == "income" }
        .reduce(0) { $0 + $1.amount }
    let expense = monthRecords
        .filter { $0.type == "expense" }
        .reduce(0) { $0 + $1.amount }
    return (income, expense)
}
```
:::

#### 6. קבלה: שלוש שכבות בדיקה + שני אתגרים למתקדמים

אחרי שסיימתם את הפרויקט, ערכו קבלה בשלוש שכבות לפי הסדר "תפקוד → קצוות → ארכיטקטורה": האם אפשר לרשום, האם אפשר למחוק, והאם הנתונים שורדים הפעלה מחדש של האפליקציה (תפקוד); האם הזנת 0 או מספר שלילי גורמת לקריסה (קצוות); האם הממשק והנתונים מעורבבים זה בזה, והאם יש ערכים מקודדים קשיח בשדות (ארכיטקטורה).

אחרי שהגרסה הבסיסית עברה קבלה, תנו לעצמכם שתי "מנות מתקדמות":

1. סטטיסטיקה לפי קטגוריות: מוסיפים כרטיסיית "סטטיסטיקה" ומציירים את ההוצאות לפי קטגוריה כתרשים עוגה/עמודות עם Swift Charts — ספריית התרשימים הרשמית של אפל; כמה שורות קוד ויש גרף;
2. סנכרון iCloud: הפעלת סנכרון iCloud ב-SwiftData דורשת רק כמה הגדרות — ספר החשבונות מסתנכרן אוטומטית בין iPhone ל-iPad, ופתאום הכל נראה "מתקדם" באמת.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
הידיים על ההגה: מסיימים את זה השבוע

{class="mt-1"}
עבדו לפי הסדר "שכבת נתונים → ViewModel → מסך רשימה → חלון הזנה → כרטיס סיכום", שלב אחד בכל יום. נתקעתם? שלחו את הודעת השגיאה כמו שהיא למנוע חיפוש או ל-AI (זוכרים את החלק השביעי "פרקטיקת תכנות בעזרת AI"? בתיאור הבעיה הקפידו לציין "התנהגות צפויה, התנהגות בפועל ושלבי שחזור"). אחרי שתסיימו, נהלו איתו את החשבונות שבוע — כשמשתמשים באפליקציה שבניתם בעצמכם, תחושת ההישג דוחפת אתכם להמשיך קדימה.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
סיכום הפרק

- חמישה מרכיבי דרישות → פירוק לשלבים קטנים ש"כל אחד שמיש", ורק אז מתחילים לעבוד
- שכבת נתונים: מודל @Model + מיכל modelContainer + שאילתות FetchDescriptor
- חלוקת תפקידים ב-MVVM: View רק מצייר, ViewModel עם @Observable מנהל את הלוגיקה, ו-SwiftData מנהל את האחסון
- ממשק: List + Section + toolbar + חלון הזנה עם sheet
- קבלה בשלוש שכבות (תפקוד/קצוות/ארכיטקטורה) + אתגרים למתקדמים (Swift Charts, סנכרון iCloud)
:::
