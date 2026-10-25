---
id: di-wu-shi-si-zhang
num: 54
part: an-zhuo-kai-fa-pian
nav: פרק 54: פרויקט 1 – אפליקציית רישום ההוצאות שלי (גרסה מקומית)
toc: default
kind: chapter
---

### פרק 54: פרויקט 1 – ספר החשבונות שלי (גרסה מקומית)

{class="chapter-intro mb-4"}
ברוכים הבאים ל"פרויקט הרציני" הראשון שלכם. ספר החשבונות הזה לא מתחבר לרשת, אבל יש בו את כל האיברים: רישום עסקה, צפייה בפירוט, סיכום חודשי, מחיקה ועריכה. אחרי שתסיימו אותו תעברו מסע שלם של "נתונים → לוגיקה → מסך". אל תמהרו להעתיק קוד – קודם חושבים ואז פועלים; זהו העיקרון הקבוע שלנו.

#### א' חשיבה על דרישות: קודם כול חמש שאלות

לפני שמתחילים, סדרו את הרעיון עם "חמשת מרכיבי הדרישה":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">מרכיב</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">תשובה</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who (למי מיועד)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">לשימוש עצמי, וגם בני משפחה וחברים</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What (מה עושים)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">רישום הכנסות והוצאות, צפייה בפירוט, סיכום חודשי, סטטיסטיקה לפי קטגוריה</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why (למה)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">תרגול + להבין לאן הכסף הולך</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How (איך)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">‏Kotlin + Compose + Room + MVVM, מקומי לחלוטין בלי שרת עורפי</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint (אילוצים)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">להשלים תוך שבוע; תמיכה מינימלית ב-Android 8; גם אם לא יועלה לחנות – לכתוב לפי סטנדרט של אפליקציה בחנות</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
חמשת מרכיבי הדרישה של ספר החשבונות

ואז פרקו לצעדים קטנים שכל אחד מהם שימושי: ① בניית שכבת נתונים ב-Room (שיהיה אפשר לשמור רשומה); ② מסך רשימה (שיהיה אפשר לצפות בפירוט); ③ מסך הזנה (שיהיה אפשר להוסיף רשומה); ④ מחיקה ועריכה; ⑤ כרטיס סיכום חודשי. אחרי כל צעד, האפליקציה היא "דבר שאפשר ממש להשתמש בו".

#### ב' שכבת הנתונים: לתת ל"רשומות" בית

קודם כול מגדירים איך נראית רשומה אחת – השדות צריכים להספיק, אבל בלי חמדנות:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Record.kt (ישות)</span><span class="dots">···</span>
:::

```
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val type: String,        // "income" הכנסה | "expense" הוצאה
    val amount: Double,      // סכום (יואן)
    val category: String,    // קטגוריה: אוכל, תחבורה, משכורת…
    val note: String = "",   // הערה (רשות)
    val date: String         // "2026-08-15"
)
```
:::

הוסיפו ב-Dao שתי שאילתות "לצורכי סטטיסטיקה" – זו הנשמה של ספר החשבונות:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordDao.kt (שאילתות סטטיסטיקה)</span><span class="dots">···</span>
:::

```
@Dao
interface RecordDao {
    @Query("SELECT * FROM records ORDER BY date DESC, id DESC")
    fun getAll(): Flow&lt;List&lt;Record&gt;&gt;

    @Insert
    suspend fun insert(record: Record)

    @Delete
    suspend fun delete(record: Record)

    @Query("SELECT COALESCE(SUM(amount),0) FROM records WHERE type='income' AND date LIKE :month || '%'")
    suspend fun monthIncome(month: String): Double   // month בפורמט "2026-08"

    @Query("SELECT COALESCE(SUM(amount),0) FROM records WHERE type='expense' AND date LIKE :month || '%'")
    suspend fun monthExpense(month: String): Double
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
טיפ: למה הסכום הוא Double?

{class="mt-1"}
אפליקציות פיננסיות קפדניות משתמשות ב-BigDecimal או ב-Int "שסופר באגורות" כדי להימנע משגיאות נקודה צפה (הבעיה הישנה של 0.1+0.2≠0.3). לפרויקט תרגול Double מספיק; אם יום אחד תבנו מוצר פיננסי אמיתי, זכרו לעבור לספירה באגורות – זהו מוקש שדרכו בו אינספור מפתחים לפניכם.
:::

#### ג' MVVM: "פירוד" בין המסך ללוגיקה

לתת למסך לגשת ישירות למסד הנתונים? זה ירוץ, אבל קוד המסך יהפוך לבלגן ארוך ומבאס. ארכיטקטורת MVVM נותנת לכל אחד תפקיד: ‏View (המסך) רק מצייר, ‏ViewModel (מרכז הלוגיקה) מנהל נתונים, ‏Model (Room) מנהל אחסון.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> תצוגה (ממשק Compose)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel (מצב ולוגיקה)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model (שכבת נתונים Room)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
איור 5: מבנה MVVM בשלוש שכבות – הנתונים זורמים בכיוון אחד, וכל שכבה נשארת בגבולותיה
:::

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordViewModel.kt (שלד)</span><span class="dots">···</span>
:::

```
class RecordViewModel(private val dao: RecordDao) : ViewModel() {

    // הופך את ה-Flow למצב שהממשק יכול לצפות בו
    val records = dao.getAll()
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(), emptyList())

    // פעולות משתמש: קריאה לפונקציות suspend
    fun addRecord(type: String, amount: Double, category: String, note: String, date: String) {
        viewModelScope.launch {
            dao.insert(Record(type = type, amount = amount,
                category = category, note = note, date = date))
        }
    }

    fun deleteRecord(record: Record) {
        viewModelScope.launch { dao.delete(record) }
    }
}
```
:::

במסך (Compose) משתמשים כך: val vm: RecordViewModel = viewModel(), ואז val list by vm.records.collectAsState() – ברגע שהנתונים משתנים הרשימה מתרעננת אוטומטית, בלי שתעשו דבר. זו העוצמה של השילוב בין MVVM + Flow + Compose.

#### ד' המסכים: מסך רשימה + מסך הזנה

במסך הרשימה משתמשים ב-LazyColumn (רשימה בטעינה עצלה) – גם עם הרבה מאוד נתונים, בלי קפאונים:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · מסך רשימת ההוצאות (קטע מרכזי)</span><span class="dots">···</span>
:::

```
@Composable
fun RecordListScreen(vm: RecordViewModel) {
    val records by vm.records.collectAsState()

    Column {
        // כרטיס הסיכום העליון (הכנסות - הוצאות = יתרה)
        SummaryCard(records)

        // רשימת הרשומות
        LazyColumn {
            items(records, key = { it.id }) { record -&gt;
                RecordRow(record) { vm.deleteRecord(record) }
            }
        }

        // כפתור צף "רישום הוצאה" → פותח דיאלוג הזנה
        FloatingActionButton(onClick = { showAddDialog = true }) {
            Text("+")
        }
    }
}

@Composable
fun RecordRow(record: Record, onDelete: () -&gt; Unit) {
    Row(Modifier.fillMaxWidth().padding(12.dp)) {
        Text(record.category, fontWeight = FontWeight.Bold)
        Spacer(Modifier.weight(1f))
        Text(if (record.type == "income") "+${record.amount}" else "-${record.amount}",
             color = if (record.type == "income") Color(0xFF27AE60) else Color(0xFFC0392B))
    }
}
```
:::

להזנה הדרך הפשוטה ביותר היא AlertDialog (תיבת דו-שיח): כמה שדות קלט + מתג הכנסה/הוצאה + תפריט קטגוריות נפתח, ובלחיצה על אישור קוראים ל-vm.addRecord(...).

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
שימו לב: אל תתעצלו על בדיקת הקלט

{class="mt-1"}
חובה לבדוק את שדה הסכום: ערך ריק, מספר שלילי וקלט לא חוקי כמו "abc" חייבים להיתפס (בדקו עם toDoubleOrNull()). אחת הסיבות הנפוצות ביותר לקריסת אפליקציות היא "להתייחס לקלט של המשתמש כאל ילד טוב". זכרו: כל קלט של משתמש בודקים כאילו היה אויב.
:::

#### ה' עריכה ומחיקה: לאפשר לנתונים "להיכנס וגם לצאת"

ספר חשבונות שיודע רק להוסיף ולא למחוק מתיישן אחרי שלושה ימים. הוסיפו שתי פעולות:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · מחיקה ועריכה</span><span class="dots">···</span>
:::

```
// מוסיפים שתי פונקציות ל-Dao:
@Query("UPDATE records SET amount=:amount, category=:category, note=:note WHERE id=:id")
suspend fun update(id: Long, amount: Double, category: String, note: String)

@Query("DELETE FROM records WHERE id=:id")
suspend fun deleteById(id: Long)

// בממשק: לחיצה ארוכה על פריט פותחת תפריט "עריכה/מחיקה" (ב-Compose: DropdownMenu או AlertDialog)
// לפני מחיקה עדיף דיאלוג אישור — "מחיקה בטעות" היא הדבר שמשתמשי אפליקציות הוצאות שונאים יותר מכול
```
:::

שני כללי ניסיון לפרטי האינטראקציה: למחיקה חובה אישור כפול (למנוע החלקת אצבע), ובעריכה כדאי למלא מראש את הערך המקורי (לתקן מילה אחת קל יותר מאשר להקליד הכול מחדש). אל תזלזלו בשני הפרטים האלה – תחושת המוצר בנויה בדיוק מפרטים כאלה.

#### ו' קבלת הפרויקט: בדיקה בשלוש שכבות + שני אתגרים למתקדמים

אחרי שהפרויקט מוכן, קבלו אותו לפי שלוש שכבות "תפקוד → קצוות → ארכיטקטורה": האם אפשר לרשום, למחוק, והאם הנתונים נשארים אחרי פתיחה מחדש (תפקוד); האם הזנת 0 או מספר שלילי מפילה את האפליקציה, האם סיבוב מסך מאבד נתונים (קצוות); האם המסך והנתונים מעורבבים, האם יש ערכים מקובעים בקוד (ארכיטקטורה).

אחרי שעברתם את קבלת הגרסה הבסיסית, תנו לעצמכם שתי "מנות מתקדמות":

1. סינון חודשי: מוסיפים בראש המסך החלפת חודשים (למשל 2026-08 ▾), והרשימה מציגה רק את הפירוט של החודש הנוכחי;
2. תרשים עוגה לפי קטגוריות: משתמשים ב-Canvas של Compose או מוסיפים ספריית תרשימים קלת-משקל, ומציירים את "לאן הכסף הולך" כתרשים עוגה – אחרי זה ספר החשבונות כבר נראה קצת כמו "מוצר אמיתי".

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
הגיע הזמן להתנסות: השלימו אותו השבוע

{class="mt-1"}
פעלו בסדר "שכבת נתונים → ViewModel → מסך רשימה → מסך הזנה → כרטיס סיכום", צעד אחד בכל יום. נתקעתם? שלחו את הודעת השגיאה כמו שהיא למנוע חיפוש או ל-AI (זוכרים את החלק השביעי, "AI לקידוד בפועל"? בתיאור בעיה אמרו בבהירות "התנהגות צפויה, התנהגות בפועל, שלבי שחזור"). אחרי ההשלמה נהלו בו חשבונות במשך שבוע – כשמשתמשים באפליקציה שבניתם בעצמכם, תחושת ההישג דוחפת אתכם קדימה.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
סיכום הפרק

- חמשת מרכיבי הדרישה → פירוק לצעדים קטנים "שכל אחד שימושי", ורק אז לפעול
- שכבת נתונים: ישות Record + Dao (כולל SQL לסטטיסטיקה חודשית) + Database
- חלוקת תפקידים ב-MVVM: ‏View רק מצייר, ‏ViewModel מנהל לוגיקה, ‏Model מנהל אחסון
- ‏Flow + stateIn + collectAsState: הנתונים משתנים – המסך מתרענן אוטומטית
- ‏LazyColumn לרשימה בטעינה עצלה; ‏AlertDialog להזנה
- קבלה בשלוש שכבות (תפקוד/קצוות/ארכיטקטורה) + אתגרים למתקדמים (סינון חודשי, תרשים עוגה לפי קטגוריות)
:::
