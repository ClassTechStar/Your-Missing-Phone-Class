---
id: di-liu-shi-yi-zhang
num: 61
part: ios-kai-fa-pian
nav: פרק 61: Swift במהירות – שפת הפיתוח הראשונה של Apple
toc: default
kind: chapter
---

### פרק 61: Swift למתחילים — השפה הראשונה לפיתוח באפל

{class="chapter-intro mb-4"}
בפרק הזה נתחיל סוף סוף ללמוד את השפה. אל תילחצו — Swift ידועה בידידותיות שלה למתחילים, ובנוסף אין צורך לשנן ספר תחביר: שליטה ב-20% מהתחביר מספיקה כדי להבין ולכתוב 80% מהקוד היומיומי. את השאר תחפשו תוך כדי עבודה על הפרויקט. זכרו את עקרון הלמידה שלנו: להבין עדיף על לשנן, לדעת להשתמש עדיף על לשלוט לעומק.

#### 1. משתנים וטיפוסים: קוראים לנתונים בשם

תוכנה היא "נתונים + לוגיקה". משתנה הוא בעצם לתת לנתונים שם ולאחסן אותם. ב-Swift מצהירים עם let ו-var:

::: div .code-block
:::inline div .code-head
<span>SWIFT · משתנים</span><span class="dots">···</span>
:::

```
let name = "דני"        // let: קבוע (מומלץ כברירת מחדל)
var age = 18             // var: משתנה (אפשר לשנותו אחר כך)

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var אפשר לשנות
// name = "נועה"         // <i class="fas fa-times-circle mr-1"></i> let לא ניתן לשינוי, שגיאת קומפילציה

let score: Int = 100     // אפשר גם לציין את הטיפוס במפורש
let pi = 3.14            // גם בלי לכתוב אותו הוא יוסק אוטומטית

print("שלום \(name)")   // שילוב מחרוזות: לוכסן אחורי + סוגריים
```
:::

את הטיפוסים הנפוצים אפשר לזכור בטבלה אחת:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">טיפוס</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">מה מאוחסן</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">דוגמה</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מספר שלם</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מספר עשרוני</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">טקסט</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"שלום"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bool</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">אמת/שקר</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[Int] (מערך)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">קבוצת נתונים</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[1, 2, 3]</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
הטיפוסים הבסיסיים הנפוצים ב-Swift

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
טיפ: כלל העדיפות של let

{class="mt-1"}
חוק הברזל של קהילת Swift: ברירת המחדל היא let, ו-var רק כשזה באמת נחוץ. אם תשתמשו ב-var במקום שאפשר let, Xcode יזהיר אתכם בטקסט צהוב. ההרגל הזה חוסך לכם שלמה שלמה של באגים מהסוג "משתנה ששונה בטעות" — כמה שפחות דברים משתנים בקוד, כך קל יותר להבין אותו.
:::

#### 2. ערכים אופציונליים (Optional): "הקמיע נגד התרסקות" של Swift

זה המושג החשוב ביותר ב-Swift, בלי תחרות. במשפט אחד: כשערך עלול "לא להתקיים", Swift מחייבת אתכם לטפל בו — השפה מחסלת מהיסוד את סיוט התעשייה של "התרסקות בגלל מצביע ריק".

::: div .code-block
:::inline div .code-head
<span>SWIFT · ערכי Optional</span><span class="dots">···</span>
:::

```
var name: String = "דני"   // טיפוס רגיל: לעולם לא יכול להיות nil
// name = nil                // <i class="fas fa-times-circle mr-1"></i> שגיאת קומפילציה: עוצרת אותך מיד

var nickname: String? = nil  // מוסיף סימן שאלה: מאפשר nil (ערך optional)
nickname = "טומי"

// עם ערכי optional חובה "לפתוח" אותם:
if let n = nickname {        // if let: פתיחה בטוחה
    print("שלום \(n)")
} else {
    print("עוד אין כינוי")
}

let len = nickname?.count ?? 0   // ?? ערך ברירת מחדל (אופרטור coalescing)
print(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
שימו לב: ! היא "פעולה מסוכנת"

{class="mt-1"}
לכתוב בקוד nickname! (פתיחה כפויה) זה כמו לצעוק למהדר "אני מבטיח שזה לא nil" — וברגע שטועים, האפליקציה מתרסקת על המקום. כלל למתחילים: השתמשו כמה שאפשר ב-if let / ?? ואל תשתמשו ב-!. לפעמים Xcode מוסיף ! מעצמו בעת השלמת קוד — זכרו לתקן את זה.
:::

#### 3. פונקציות וסגרים: אורזים לוגיקה ב"כפתורים"

פונקציה היא קטע לוגיקה עם שם, כמו כפתור בשלט רחוק. סגר (Closure) הוא "פונקציה בלי שם", שאפשר להעביר לאחרים כמו שהוא:

::: div .code-block
:::inline div .code-head
<span>SWIFT · פונקציות ו-closures</span><span class="dots">···</span>
:::

```
// פונקציה: השם בקדמת; פרמטרים וטיפוס ההחזרה מאחור
func greet(name: String) -> String {
    return "שלום, \(name)!"
}
print(greet(name: "דני"))     // בקריאה, עם שם הפרמטר

// closure: מוגדרת במקום, קלילה וישירה
let numbers = [1, 2, 3, 4]
let doubled = numbers.map { $0 * 2 }   // $0 = האיבר הנוכחי
// [2, 4, 6, 8]

let big = numbers.filter { $0 > 2 }    // סינון
// [3, 4]
```
:::

ב-SwiftUI סגרים בכל מקום: הסוגריים המסולסלים אחרי Button("לחצו עליי") { ... } של כפתור הם סגר. שננו את ה"קומבו" של האוספים — map, filter, sorted — כי 90% מעיבודי הרשימות בעתיד יהיו שילובים שלהם.

#### 4. מבנים ופרוטוקולים: שיטת "הלגו" של Swift

ההעדפה הרשמית של Swift ברורה: מעדיפים מבנה (struct), ומחלקה (class) רק כשנדרשת ירושה. מבנה הוא "טיפוס ערך" — כשמעתיקים אותו כל עותק חי את חייו שלו, מה שמפחית מטבעו סוג שלם של באגים:

::: div .code-block
:::inline div .code-head
<span>SWIFT · מבנים ופרוטוקולים</span><span class="dots">···</span>
:::

```
// ה-struct: קופסת הנתונים
struct Record {
    var id = UUID()
    var amount: Double
    var category: String
    var date: Date

    // ל-struct יש "memberwise initializer" מובנה: אפשר ליצור ישירות
}
let r = Record(amount: 25.5, category: "אוכל", date: Date())

// פרוטוקול: הסכם על "אילו יכולות חייבות להיות"
protocol Identifiable {
    var id: UUID { get }
}
struct Record: Identifiable { ... }   // לאמץ את הפרוטוקול = להתחייב למלא את דרישותיו
```
:::

ב-SwiftUI כמעט הכל הוא struct (View הוא פרוטוקול). אם המשפט הזה לא ברור כרגע — לא נורא, נפגש איתו יום-יום בפרק 62; בעולם של Swift מתחבקים קודם כל עם struct.

#### 5. כרטיס תחביר מהיר בשביל מי שמתחיל מאפס

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">מה רוצים לעשות</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">כיצד כותבים</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">הגדרת קבוע/משתנה</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">let x = 1</code> / <code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">שיבוץ ערכים במחרוזת</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"שלום, \(name)"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">הגדרת פונקציה</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">func שם(פרמטר: טיפוס) -> טיפוס החזרה { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">תנאי</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if תנאי { ... } else { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מעבר על איברים</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for x in מערך { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">פתיחה בטוחה</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if let x = ערך אופציונלי { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ערך ברירת מחדל</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">x ?? ערך ברירת מחדל</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">הגדרת מבנה</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X { var a: Int; var b: String }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">סגר</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">{ $0 * 2 }</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
כרטיס תחביר מהיר ל-Swift (מהדורת מתחילים)

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
הידיים על ההגה: 15 דקות של משחק עם Swift ב-Playgrounds

{class="mt-1"}
יש מק? פתחו Xcode → Playground. אין מק? השתמשו ב-Swift Playgrounds ב-iPad או במגרש המשחקים בדפדפן. הריצו כל קטע קוד בפרק, שחקו עם המספרים והטקסטים, וגרמו בכוונה לכמה שגיאות כדי לראות איך Xcode מתריע. 15 הדקות האלה של "לשחק לפני שלומדים" יקלו עליכם פי שניים כשתתחילו את פרק 62.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
סיכום הפרק

- מעדיפים let ונזהרים עם var; הטיפוסים מוסקים אוטומטית, ואפשר גם להצהיר במפורש אחרי הנקודתיים
- ערכים אופציונליים הם הנשמה של Swift: מה שעלול להיות ריק חייב טיפול, if let / ?? הם הקמיע ו-! היא פעולה מסוכנת
- בקריאה לפונקציה מציינים שמות פרמטרים; סגר = פונקציה בלי שם, והוא בכל מקום ב-SwiftUI
- מעדיפים struct ומקפידים על פרוטוקולים (Protocol); ב-SwiftUI כמעט הכל הוא struct
- 20% מהתחביר עושים 80% מהעבודה: קודם לדעת להשתמש, ואחר כך להעמיק
:::
