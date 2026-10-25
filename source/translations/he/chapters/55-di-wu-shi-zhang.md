---
id: di-wu-shi-zhang
num: 50
part: an-zhuo-kai-fa-pian
nav: פרק 50: Kotlin במהירות – שפת הפיתוח הראשונה של Android
toc: default
kind: chapter
---

### פרק 50: Kotlin במהירות — השפה הראשונה של פיתוח אנדרואיד

{class="chapter-intro mb-4"}
בפרק זה נלמד את השפה כהלכה. אל תילחצו — Kotlin ידועה כ"ידידותית למתחילים", ואין צורך לשנן ספר תחביר: שליטה ב-20% מהתחביר מספיקה כדי להבין ולכתוב 80% מהקוד היומיומי. את השאר תחפשו תוך כדי עבודה על הפרויקט. זכרו את עקרון הלמידה שלנו: להבין > לשנן, להשתמש > לשלוט.

#### א. משתנים וטיפוסים: לתת שם לנתונים

תוכנית היא בעצם "נתונים + לוגיקה". משתנה הוא שם שנותנים לנתונים כדי לשמור אותם. ב-Kotlin יש שתי דרכי הצהרה:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · משתנים</span><span class="dots">···</span>
:::

```
val name = "דני"        // val: משתנה לקריאה בלבד (מומלץ כברירת מחדל)
var age = 18             // var: משתנה שאפשר לשנות (אפשר לשנותו אחר כך)

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var אפשר לשנות
// name = "נועה"         // <i class="fas fa-times-circle mr-1"></i> val לא ניתן לשינוי, הקומפילציה תדווח שגיאה

val score: Int = 100     // אפשר גם לציין את הטיפוס במפורש
val pi = 3.14            // גם בלי לכתוב אותו הוא יוסק אוטומטית
```
:::

הטיפוסים הנפוצים הם בודדים — טבלה אחת וזוכרים:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">טיפוס</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">מה שומרים</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">דוגמה</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מספר שלם</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מספר עשרוני</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">טקסט</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"שלום"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Boolean</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">אמת/שקר</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List&lt; T&gt;</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">קבוצת נתונים</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">listOf(1, 2, 3)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
הטיפוסים הבסיסיים הנפוצים ב-Kotlin

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
טיפ: עקרון val קודם כל

{class="mt-1"}
חוק ברזל בקהילת Kotlin: כברירת מחדל משתמשים ב-val, ו-var רק כשבאמת צריך. אם תשתמשו ב-var במקום שבו אפשר val, ה-IDE יזהיר אתכם בצהוב. ההרגל הזה חוסך מכם קטגוריה שלמה של bug-ים של "משתנה שהשתנה בטעות" — ככל שהקוד משתנה פחות, כך קל יותר להתחקות אחריו.
:::

#### ב. פונקציות: לארוז לוגיקה כ"כפתור"

פונקציה היא מקטע לוגיקה בעל שם, כמו כפתור על שלט רחוק — לוחצים עליו (קוראים לו) והוא מריץ רצף פעולות. ב-Kotlin מצהירים עליה במילה fun:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · פונקציות</span><span class="dots">···</span>
:::

```
fun greet(name: String): String {
    return "שלום, $name!"     // הסימן $ מכניס את המשתנה למחרוזת
}

println(greet("דני"))        // פלט: שלום דני!

// פונקציות של שורה אחת אפשר לכתוב כביטוי
fun add(a: Int, b: Int) = a + b

println(add(3, 5))            // פלט: 8
```
:::

כמה נקודות חשובות: הפרמטרים נכתבים בתוך הסוגריים (שם קודם, טיפוס אחרי, מופרדים בנקודתיים); טיפוס ההחזרה נכתב אחרי הסוגריים; ושילוב משתנים במחרוזות באמצעות $שם המשתנה הוא היתרון המובהק של Kotlin — אין צורך לשרשר "מחרוזת + משתנה" כמו ב-Java.

#### ג. תנאים ולולאות: לתת לתוכנית "לחשוב"

ה"אינטליגנציה" של תוכנית נובעת משני דברים: יכולת לשפוט (if/when) ויכולת לחזור (for/while).

::: div .code-block
:::inline div .code-head
<span>KOTLIN · תנאים ולולאות</span><span class="dots">···</span>
:::

```
// תנאי: if / else
val age = 17
if (age >= 18) {
    println("מבוגר")
} else {
    println("קטין")
}

// מספר ענפים: when (פי מאה יותר טוב מ-switch)
val score = 85
val level = when {
    score >= 90 -> "מצוין"
    score >= 60 -> "עובר"
    else -> "המשך כך!"
}

// חזרה: לולאת for
val fruits = listOf("תפוח", "בננה", "תפוז")
for (fruit in fruits) {
    println("אני אוהב לאכול $fruit")
}
```
:::

when היא הדרך הנפוצה ביותר ב-Kotlin לענפים מרובים; בפיתוח אנדרואיד תשתמשו בה מדי יום (למשל להציג ממשק שונה לפי מצב).

#### ד. בטיחות ריק: "קמיע ההישרדות" של Kotlin

ה-bug המפורסם ביותר מתקופת Java נקרא NullPointerException (חריגת מצביע ריק) — התוכנית ניגשת ל"משהו שאין בו כלום" וקורסת מיד. לפי הסטטיסטיקה, הוא ראש טבלת הקריסות באנדרואיד שנה אחר שנה. Kotlin פתרה את זה ברמת השפה: כברירת מחדל ערכי ריק אסורים.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · בטיחות null</span><span class="dots">···</span>
:::

```
var name: String = "דני"   // טיפוס רגיל: לעולם לא יכול להיות null
// name = null                // <i class="fas fa-times-circle mr-1"></i> שגיאת קומפילציה: עוצרת אותך מיד

var nickname: String? = null // מוסיף סימן שאלה: מאפשר null
nickname = "טומי"

// עם טיפוסים שיכולים להיות null חובה לטפל בבטחה:
println(nickname?.length)    // קריאה בטוחה: אם null מחזיר null, בלי קריסה
val len = nickname?.length ?: 0   // אופרטור Elvis: ערך ברירת מחדל כש-null
println(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
שימו לב: אל תתבלבלו בין ? ו-?:

{class="mt-1"}
String? פירושו "מותר להיות ריק", ו-a ?: b פירושו "אם a ריק, השתמשו ב-b" (נראה כמו תסרוקת של אלביס, ולכן קרוי אופרטור Elvis). כשמתחילים לכתוב קוד והמהדר מדווח על "שגיאת null", הסיכוי הגדול ששכחתם לטפל בטיפוס ריק-אפשרי — דווקא השפה מגינה עליכם.
:::

#### ה. מחלקות ואובייקטים: התבניות לייצור "חלקים"

מחלקה היא ה"תבנית" של האובייקט, ואובייקט הוא "המוצר המוגמר" של המחלקה. כל דבר באנדרואיד — מסכים, כפתורים, נתונים — הוא אובייקט. ל-Kotlin יש כלי נפלא בשם data class (מחלקת נתונים), המיועד במיוחד "לאחסן נתונים" — שורה אחת במקום עשרות שורות ב-Java:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · מחלקות ו-data class</span><span class="dots">···</span>
:::

```
// מחלקה רגילה: התבנית
class Dog(val name: String) {
    fun bark() = println("$name: האו האו!")
}

val dog = Dog("Rex")      // יוצר אובייקט
dog.bark()                 // Rex: האו האו!

// data class: קופסת הנתונים (כולל equals/copy וכו' אוטומטית)
data class User(val id: Int, val name: String, val email: String)

val me = User(1, "דני", "zhangsan@example.com")
val twin = me.copy(name = "איתי")   // מעתיק ומשנה שדה אחד
```
:::

כשתבנו בעתיד פנקס הוצאות, כל רשומה תהיה data class: data class Record(val amount: Double, val category: String, val date: String). מבינים? כבר עכשיו אתם מסוגלים לכתוב מבנה קוד של פרויקט אמיתי.

#### ו. lambda ופונקציות מסדר גבוה: "סוכר תחבירי" של Kotlin

בקוד אנדרואיד תראו מדי יום את ה-{ ... } הזה — "פונקציה חסרת שם", הנקראת lambda (פונקציה אנונימית). ה-onClick = { count++ } של ה-Button הוא lambda — "מה קורה אחרי הלחיצה" נארז לחבילה אחת ונמסר לכפתור.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · היכרות ראשונה עם lambda</span><span class="dots">···</span>
:::

```
// הדרך הרגילה: להגדיר פונקציה עם שם ואז להעביר אותה
fun double(x: Int) = x * 2
val result = listOf(1, 2, 3).map(::double)

// דרך lambda: מוגדרת במקום, קלילה וישירה
val result2 = listOf(1, 2, 3).map { it * 2 }   // it = האיבר הנוכחי

// סינון + המרה בשרשרת (נפוץ מאוד בפרויקטים אמיתיים)
val bills = listOf(12.5, 88.0, 5.0, 200.0)
val bigBills = bills.filter { it > 50 }.sorted()
// [88.0, 200.0]——"חשבונות מעל 50, ממוינים"
```
:::

שמרו בזיכרון כמה "קומבינציות אוספים" בתדירות גבוהה: filter (סינון), map (טרנספורמציה), sorted (מיון), sum (סכימה). 90% מעיבודי הרשימות שלכם בעתיד יהיו שילוב של ארבע הטכניקות האלה. הפילוסופיה של Kotlin: לוגיקה שאפשר לומר במשפט אחד — לא תיכתב בחמישה.

#### ז. כרטיס עיון מהיר לתחביר, למתחילים מאפס

אל תנסו לשנן את כל התחביר ביום אחד. שמרו את הכרטיס הזה, עיינו בו בזמן כתיבת קוד — בעוד שבועיים זה ייכנס לראש מעצמו:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">מה רוצים לעשות</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">איך כותבים</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">הגדרת משתנה לקריאה בלבד</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">val x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">הגדרת משתנה ניתן לשינוי</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">הגדרת פונקציה</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">fun שם(פרמטרים): טיפוס החזרה { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">תנאי</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if (תנאי) {...} else {...}</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ענפים מרובים</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">when { תנאי -> תוצאה }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מעבר על פריטים</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for (x in רשימה) { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">חיבור מחרוזות</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"שלום, $name"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">טיפול בערכים ריקים</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">x?.length ?: 0</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">הגדרת מחלקת נתונים</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">data class X(val a: Int, val b: String)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
כרטיס עיון מהיר לתחביר Kotlin (מהדורת מתחילים)

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
היד על הדופק: שחקו 10 דקות ב-Kotlin בלי להתקין דבר

{class="mt-1"}
פתחו בדפדפן את play.kotlinlang.org (מגרש המשחקים המקוון הרשמי של Kotlin), הדביקו לשם כל מקטע קוד מהפרק הזה והריצו, שנו מספרים וטקסטים וצפו איך הפלט משתנה. ה-10 דקות האלה של "לשחק קודם וללמוד אחר כך" יקלו עליכם פי שניים כשתגיעו לפרק 51.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
סיכום הפרק

- עדיף val, ב-var להשתמש בזהירות; טיפוסים יכולים להיגזר אוטומטית, ואפשר גם להצהיר עליהם במפורש אחרי הנקודתיים
- פונקציה = לוגיקה ארוזה; תבניות מחרוזת עם $ הן היתרון המובהק
- if/when לשיפוט, for ללולאות; when הוא "הרב-גוני" של פיתוח האנדרואיד
- בטיחות הריק היא קמיע ההישרדות של Kotlin: טיפוס רגיל דוחה null; טיפוס ריק-אפשרי מחייב טיפול ב-? / ?:
- data class היא קופסה לנתונים — שדה אחד בכל שורה, בשימוש יומיומי בפרויקטים אמיתיים
- 20% מהתחביר עושים 80% מהעבודה: קודם להשתמש, אחר כך לשלוט
:::
