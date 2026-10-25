---
id: di-wu-shi-yi-zhang
num: 51
part: an-zhuo-kai-fa-pian
nav: פרק 51: פיתוח ממשק – מבוא ל-Jetpack Compose
toc: default
kind: chapter
---

### פרק 51: פיתוח ממשק — מבוא ל-Jetpack Compose

{class="chapter-intro mb-4"}
הממשק הוא כל מה שהמשתמש רואה. לפני ש-Compose הופיע, ממשקי אנדרואיד נכתבו ב-XML — מייגע כמו מבחן השלמת חסרים; ב-2021 Google השיקה את Jetpack Compose: מציירים את הממשק ישירות בקוד Kotlin, מה שרואים זה מה שמקבלים, ושינוי שורת קוד אחת מרענן את התצוגה המקדימה מיד. נכון ל-2026, Compose הוא הסטנדרט המוחלט לפרויקטים חדשים. בפרק זה נלמד "לצייר".

#### א. הרעיון של Compose: הממשק הוא פונקציה

הרעיון המרכזי של Compose במשפט אחד: ממשק = פונקציה. כל דבר שמוצג על המסך (טקסט, כפתור, תמונה) הוא "פונקציה קומפוזבילית" (Composable) המסומנת ב-@Composable. מקננים אותן כמו קוביות בנייה — וזה הממשק.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · הממשק הראשון ב-Compose</span><span class="dots">···</span>
:::

```
@Composable
fun Greeting(name: String) {
    Text(text = "שלום, $name!")     // "בלוק טקסט"
}

// הרכבה מקוננת: בלוקים גדולים שמכילים קטנים
@Composable
fun HomeScreen() {
    Column {                          // מסודרים אנכית
        Greeting(name = "דני")
        Greeting(name = "נועה")
        Button(onClick = { /* מה קורה בלחיצה */ }) {
            Text("לחץ כאן")
        }
    }
}
```
:::

שימו לב ל"כובע" @Composable — הוא אומר למהדר "זו קוביית ממשק". אפשר לקנן קוביות ללא הגבלה — זהו כל הסוד של Compose.

#### ב. רכיבי יסוד: טקסט, כפתור, שדה קלט ותמונה

הרכיבים של Compose הם "קוביות בנייה"; אלה ארבעת הנפוצים ביותר:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">רכיב</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">מה הוא עושה</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">פרמטרים חובה</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">הצגת טקסט</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">text (הטקסט להצגה)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">כפתור</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onClick (פונקציית לחיצה)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">שדה קלט</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">value, onValueChange (פונקציית שינוי קלט)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">הצגת תמונה</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">painter (משאב התמונה)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
ארבעת רכיבי היסוד של Compose

::: div .code-block
:::inline div .code-head
<span>KOTLIN · דוגמה לרכיבים בסיסיים</span><span class="dots">···</span>
:::

```
@Composable
fun BasicWidgets() {
    Column {
        Text(text = "זהו טקסט")
        Button(onClick = { println("נלחץ!") }) {
            Text("כפתור")
        }
        var input by remember { mutableStateOf("") }
        TextField(
            value = input,
            onValueChange = { input = it },
            label = { Text("הקלד משהו") }
        )
    }
}
```
:::

בשתי שורות של שדה הקלט הופיע remember { mutableStateOf("") } — זהו "קסם המצב" של Compose; נפרט אותו בסעיף 5 של הפרק. לעת עתה — רק להכיר את הפנים.

#### ג. שלישיית הפריסה: Column, Row, Box

יש רכיבים — איך מסדרים אותם? זכרו שלושה "קופסאות":

- Column: סידור אנכי (כמו תור בקפטריה);
- Row: סידור אופקי (כמו ישיבה זה לצד זה);
- Box: ערימה זה על זה (כמו קלפים שנערמים; מתאים לתגיות בפינה ולשכבות כיסוי).

::: div .code-block
:::inline div .code-head
<span>KOTLIN · שלישיית הפריסה</span><span class="dots">···</span>
:::

```
Column {
    Text("שורה ראשונה")
    Row {
        Text("שמאל")
        Text("ימין")
    }
    Box {
        Text("השכבה התחתונה")
        Text("תג מרוחף מעל")
    }
}
```
:::

רוצים פריסה יפה יותר? הוסיפו לרכיבים Modifier (מתאם) — זה כמו "לאפות" את הקוביות:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Modifier: טריקים נפוצים</span><span class="dots">···</span>
:::

```
Text(
    text = "טקסט יפה",
    modifier = Modifier
        .padding(16.dp)          // ריווח מכל הצדדים
        .fillMaxWidth()          // ממלא את כל הרוחב
        .background(Color.Blue)  // צבע רקע
        .clickable { /* בלחיצה */ }// ניתן ללחיצה
)
// קריאות שרשרת: אחת אחרי השנייה, הסדר משנה (קודם padding ואז רקע; הרקע לא כולל את השוליים)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
שימו לב: סדר ה-Modifier משנה

{class="mt-1"}
ל-padding(16.dp).background(Blue) ול-background(Blue).padding(16.dp) יש אפקט שונה — הראשון הוא "קודם רווח, אחר כך צבע" (הרקע לא כולל את השוליים), והשני "קודם צבע, אחר כך רווח" (הרקע כולל את השוליים). זו בדיוק הנקודה שבה מתחילים מציירים "שוליים לבנים מוזרים". לא בטוחים? החליפו את הסדר — התצוגה המקדימה תענה מיד.
:::

#### ד. מצב: לתת לממשק "חיים"

ממשק סטטי זה משעמם. כדי שהמספר יגדל ב-1 בלחיצה על הכפתור ושיהיה אפשר להקליד בשדה הקלט, צריך מצב (State). הכלל של Compose: הממשק תמיד משקף נאמנה את המצב; המצב השתנה — הממשק מצויר מחדש אוטומטית.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · מצב: מונה לחיצות</span><span class="dots">···</span>
:::

```
@Composable
fun Counter() {
    // ‏remember + mutableStateOf: זוכר את הערך המשתנה הזה
    var count by remember { mutableStateOf(0) }

    Column {
        Text(text = "לחצת $count פעמים")
        Button(onClick = { count++ }) {   // משנה את המצב
            Text("לחץ +1")                // הממשק מתרענן אוטומטית
        }
    }
}
```
:::

שלוש שורות קוד — ומונה חי. זו בדיוק הנקודה שבה Compose נעים יותר מהסגנון הישן: אין צורך "לרענן את הממשק" ידנית — פשוט משנים את הנתונים. זכרו שתי פונקציות מפתח: remember (מונעת מהערך להימחק כשהממשק נבנה מחדש) ו-mutableStateOf (אומרת ל-Compose "הערך הזה השתנה — צייר מחדש").

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> המשתמש לוחץ</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> המצב משתנה (count++)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ‏Compose מזהה את השינוי</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> מצייר מחדש את הממשק (recomposition)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
איור 3: זרימת הנתונים החד-כיוונית "מצב → ממשק" של Compose
:::

#### ה' ערכת עיצוב ומצב כהה: הגדרה אחת שחלה על הכול

‏MyFirstAppTheme { ... } בפרויקט התבנית הוא ערכת העיצוב. הוא מבוסס על מפרט העיצוב Material 3 ועוזר לך לנהל באופן אחיד צבעים, גופנים וצורות. תמיכה במצב כהה דורשת רק שלושה שלבים:

1. מגדירים בתוך ערכת העיצוב שתי ערכות צבעים – בהירה וכהה (התבנית כבר יוצרת אוטומטית ColorScheme);
2. כשהמערכת עוברת למצב כהה, הפונקציה isSystemInDarkTheme() מזהה זאת אוטומטית;
3. משתמשים בצבעים שערכת העיצוב מספקת (כמו MaterialTheme.colorScheme.primary) במקום לקבע ערכי צבע בקוד.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
טיפ: הצבעים הדינמיים של Material 3

{class="mt-1"}
מאז Android 12, התכונה "Material You" מאפשרת לאפליקציה לשלוף צבעים מטפטפת המסך שלך. תבנית Compose תומכת בכך כברירת מחדל (dynamicColor). האפליקציה שלך "מתחלפת בבגדים" אוטומטית בכל מכשיר של משתמש – זהו הקסם של האנדרואיד המודרני.
:::

#### ו' תצוגה מקדימה, אנימציה ועריכה חיה: ה"צ'יטים" של Compose

שלושת ה"צ'יטים" של Compose בחוויית הפיתוח – ברגע שמתחילים להשתמש בהם, אין דרך חזרה:

- תצוגה מקדימה באמצעות @Preview: מוסיפים את ההערה @Preview לפונקציית Composable, ו-Android Studio מציג מיד את המסך בצד ימין – מה שרואים הוא מה שמקבלים בכל שינוי קוד, בלי להתקין על הטלפון בכל פעם;
- עריכה חיה (Live Edit): ב-2026 תומך Android Studio ב"עדכון חם" של חלק מהשינויים ישירות באמולטור או במכשיר אמיתי; שינויים קטנים כמו צבע טקסט מופיעים על המכשיר תוך שניות;
- ממשקי API לאנימציה: animateFloatAsState ו-AnimatedVisibility – כמה שורות קוד בודדות מעניקות מעבר חלק לאלמנטים; תחושת "היוקרה" נמצאת לרוב בדיוק בעשרות השורות האלה.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · אנימציות בעשר דקות</span><span class="dots">···</span>
:::

```
@Composable
fun AnimatedBox() {
    var big by remember { mutableStateOf(false) }
    // כשהערך משתנה, מעבר חלק לערך היעד
    val size by animateDpAsState(if (big) 120.dp else 60.dp)

    Box(Modifier
        .size(size)
        .background(MaterialTheme.colorScheme.primary)
        .clickable { big = !big }
    )
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
טיפ: קודם פונקציונליות, אחר כך אנימציה

{class="mt-1"}
הטעות הנפוצה של מתחילים: "המסך עוד לא בנוי נכון, וכבר מתלבטים על אנימציות". קודם תגרמו לפונקציונליות לרוץ, ורק בסוף תוסיפו את האפקטים באופן אחיד – זהו עיקרון "הפשטות לפני הכול": אנימציה היא קישוט נוסף, פונקציונליות היא הצלה אמיתית.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
הגיע הזמן להתנסות: בנו "כפתור מצב רוח"

{class="mt-1"}
הפכו את פרויקט התבנית למחליף מצבי רוח: כפתור אחד, שבלחיצה עליו מתחלף במעגל בין 😀 שמח → 😢 עצוב → 😡 כועס, כשהטקסט וצבע הרקע משתנים יחד איתו. רמז: השתמשו ב-when כדי לבחור טקסט וצבע לפי המצב. שלחו לחברים לשחק – ותקבלו את הגל הראשון של "וואו, אתה יודע לבנות אפליקציות".
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
סיכום הפרק

- הרעיון של Compose: המסך = פונקציית @Composable, קינון כמו לבני בנייה
- ארבעת הרכיבים המרכזיים: Text / Button / TextField / Image
- שלושת כלי הפריסה: Column לסידור אנכי, Row לסידור אופקי, Box לערימה
- שרשור Modifier כמו "התאפרות": padding, fillMaxWidth, background, clickable – לסדר יש משמעות
- המצב הוא הנשמה: remember + mutableStateOf – משנים נתונים והמסך מצויר מחדש אוטומטית
- ערכת עיצוב עם Material 3 + צבעים דינמיים; מצב כהה – הגדרה אחת שחלה על הכול
:::
