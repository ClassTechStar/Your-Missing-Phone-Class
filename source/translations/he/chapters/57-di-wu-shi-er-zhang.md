---
id: di-wu-shi-er-zhang
num: 52
part: an-zhuo-kai-fa-pian
nav: פרק 52: ארבעת רכיבי היסוד ומחזור החיים של Activity
toc: default
kind: chapter
---

### פרק 52: ארבעת הרכיבים ומחזור החיים של Activity

{class="chapter-intro mb-4"}
אם Compose הוא "הפנים" של האפליקציה, הפרק הזה עוסק ב"שלד" שלה. למערכת אנדרואיד יש ארבעה רכיבים בסיסיים, וכל אפליקציה בנויה מהם; והחשוב מביניהם, Activity, מלווה ב"מפת מחזור חיים" שכל מפתח אנדרואיד חייב לחרוט בזיכרון. אחרי הפרק הזה תבינו חידות נצחיות כמו "למה כשחוזרים מהרקע, המצב של האפליקציה שלי נעלם".

#### א' ארבעת הרכיבים: עמודי התווך של אנדרואיד

אנדרואיד מגדירה רשמית ארבעה רכיבים בסיסיים, שכל אחד מהם אחראי על סוג עבודה אחר:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">רכיב</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">תפקיד</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">אנלוגיה</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activity</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מסך גלוי לעין</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">חזית החנות – המשתמש רואה אותה ומקיים איתה אינטראקציה</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Service</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"הבלתי נראה" שעובד ברקע</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">פועל המחסן – מנגן מוזיקה, מוריד קבצים; לא צריך מסך</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BroadcastReceiver</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">קבלת שידורי מערכת</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">חדר השער – הרמקול שמכריז "הסוללה נגמרה" ו"הרשת התנתקה"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ContentProvider</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">שיתוף נתונים בין אפליקציות</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ארון מסמכים ציבורי – למשל לשתף אנשי קשר עם אפליקציות אחרות</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
סקירה מהירה של ארבעת רכיבי אנדרואיד

בשלב המתחיל תבלו כ-95% מהזמן עם Activity; ‏Service ו-BroadcastReceiver נדרשים לנגינת מוזיקה ולדחיפת התראות; את ContentProvider תשתמשו הכי פחות (המערכת כבר עוטפת את הנתונים הנפוצים). שימו לב: כל אחד מארבעת הרכיבים חייב "להירשם" ב-AndroidManifest.xml – בלי רישום, המערכת פשוט לא תמצא אותם.

#### ב' מחזור החיים של Activity: "מפת האוצר" הראשונה בפיתוח אנדרואיד

אפליקציה בטלפון עלולה להיקטע בכל רגע: שיחה נכנסת, המשתמש עובר לענות ב-WeChat, למערכת אין מספיק זיכרון והיא מסיימת את התהליך שלך... חיי Activity הם מסע מעגלי על המפה הזאת:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onCreate (לידה: אתחול)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onStart (גלוי)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onResume (בחזית, אינטראקציה)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onPause (מוסתר חלקית)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onStop (בלתי נראה לגמרי)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center">onDestroy (הריסה)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">🔁 onRestart / onStart / onResume: בחזרה לחזית, אותו מסלול בכיוון הפוך</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
איור 4: מחזור החיים של Activity (כיוון ההתקדמות: השורה העליונה – לידה → השורה התחתונה – יציאה; בדרך חזרה – אותו נתיב בכיוון ההפוך)
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">פונקציית Callback</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">מתי מופעלת</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">שימוש טיפוסי</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onCreate</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">בעת יצירת ה-Activity (פעם אחת)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">טעינת המסך ואתחול הנתונים</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStart</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">המסך הופך לגלוי</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">התחלת לוגיקה קלה</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onResume</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מקבל מיקוד ומוכן לאינטראקציה</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">התחלת אנימציות, המשך נגינה</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onPause</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ברגע הכיסוי החלקי או המעבר למסך אחר</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">השהיית אנימציות, שמירת טיוטה</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStop</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">בלתי נראה לגמרי</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">שחרור משאבים כבדים, השהיית הורדות</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onDestroy</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">לפני ההריסה</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ניקוי אחרון</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
השימושים הטיפוסיים של שש פונקציות ה-Callback של מחזור החיים

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
אזהרה: סיבוב המסך "הורג" את ה-Activity

{class="mt-1"}
המקרה הקלאסי של מתחילים: מסובבים את המסך וכל הטקסט בשדות הקלט נעלם. הסיבה: סיבוב מסך כברירת מחדל הורס ובונה מחדש את ה-Activity (עובר על onDestroy → onCreate). הפתרון: שמירת מצב עם rememberSaveable (התחליף ל-remember ב-Compose), שמשחזר את הערכים אוטומטית בעת הבנייה מחדש. נשתמש בזה שוב ושוב בפרקים 6 ו-7.
:::

#### ג' Intent: "כרטיס הנסיעה" לתנועה בתוך האפליקציה ומחוצה לה

‏Intent (כוונה) הוא "כרטיס הנסיעה" לתקשורת בין רכיבים. כדי לקפוץ ממסך אחד לאחר, לפתוח דפדפן או להפעיל מצלמה – צריך "לקנות כרטיס ולעלות לרכבת":

::: div .code-block
:::inline div .code-head
<span>KOTLIN · ניווט עם Intent</span><span class="dots">···</span>
:::

```
// דרך 1: Intent מפורש – מציינים בבירור לאיזה מסך ללכת
val intent = Intent(this, DetailActivity::class.java)
intent.putExtra("name", "דני")     // לוקח "מזוודות" לדרך (הנתונים)
startActivity(intent)

// דרך 2: Intent גלוי-מרומז – אומרים רק מה לעשות והמערכת מוצאת מי יעשה
val web = Intent(Intent.ACTION_VIEW, Uri.parse("https://developer.android.com"))
startActivity(web)   // המערכת תפתח את הדפדפן (או תבקש ממך לבחור)
```
:::

לשתי הדרכים שימושים שונים: מפורשת – למעברים בין מסכים בתוך האפליקציה שלכם; מרומזת – להפעלת יכולות של המערכת או של אפליקציות אחרות (פתיחת דף אינטרנט, שיחה, שיתוף). בפרויקט Compose, בתוך Composable משיגים את ה-Context עם LocalContext.current, ואז אפשר להריץ startActivity.

#### ד' מספר מסכים וניווט

לכל אפליקציה אמיתית יש כמה מסכים. פתרון הניווט הרשמי המומלץ ל-Compose הוא Navigation Compose (ספריית התלות androidx.navigation):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · שלד Navigation Compose</span><span class="dots">···</span>
:::

```
val navController = rememberNavController()

NavHost(navController, startDestination = "home") {
    composable("home") { HomeScreen(navController) }
    composable("detail/{name}") { entry ->
        val name = entry.arguments?.getString("name")
        DetailScreen(name ?: "לא ידוע")
    }
}

// כדי לנווט מתוך המסך:
navController.navigate("detail/דני")     // עם פרמטר
navController.popBackStack()              // חזרה למסך הקודם
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
טיפ: מה עושים כשהמסכים מתרבים?

{class="mt-1"}
כשהפרויקט גדל, רכזו את כל נתיבי המסכים בקובץ אחד (למשל AppNavGraph.kt) לניהול אחיד – אל תפזרו את הלוגיקה של "לאן עוברים" בין המסכים. זהו הצעד הראשון מ"רץ" אל "ניתן לתחזוקה".
:::

#### ה' בדרך אגב: מהו Fragment (ולמה הספר הזה לא מלמד אותו)

בחיפוש אחר מדריכים ישנים בוודאי תיתקלו ב-Fragment – הוא "קטע מסך לשימוש חוזר" בתוך Activity, והיה הכוכב הראשי בארכיטקטורות רבי-מסכים ישנות. אבל בעידן ה-Compose מספיק לבנות מסכים ישירות עם פונקציות Composable + נתיבי Navigation, וגם הרשויות הפחיתו בחשיבותו של Fragment. לכן הספר הזה לא כולל אותו בקו הראשי.

ההמלצה שלנו: בפרויקט חדש אל תשתמשו ב-Fragment מיוזמתכם; אבל בקריאת קוד ישן או בראיון עבודה, מספיק שתדעו שזהו "קטע מסך משובץ בתוך Activity". במשאבי לימוד תעדיפו תמיד מ-2023 ואילך – "לוח השנה הישן" של טכנולוגיית האנדרואיד מתעדכן מהר יותר משחושבים.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
הגיע הזמן להתנסות: תנו למונה "זיכרון"

{class="mt-1"}
שדרגו את המונה מפרק 51: ‏① החליפו את remember ב-rememberSaveable וסובבו את המסך כדי לוודא שהמספר נשאר; ② הוסיפו כפתור "אודות" שמנווט עם Navigation למסך שני שמציג את מספר הגרסה; ③ הדפיסו לוגים (Log.d) ב-onCreate/onPause של שני המסכים וצפו בסדר הקריאות של מחזור החיים דרך Logcat. אחרי שלושת הצעדים האלה, מחזור החיים כבר לא יישאר תיאוריה על הנייר.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
סיכום הפרק

- ארבעת הרכיבים: Activity (חזית), Service (רקע), BroadcastReceiver (רמקול), ContentProvider (ארון נתונים)
- שש פונקציות ה-Callback של מחזור החיים: onCreate → onStart → onResume → onPause → onStop → onDestroy
- סיבוב מסך הורס ובונה מחדש את ה-Activity: שמרו מצב עם rememberSaveable
- ‏Intent הוא "כרטיס הנסיעה": מפורש – למסכים שלכם; מרומז – ליכולות המערכת
- ריבוי מסכים עם Navigation Compose: NavHost + נתיבי composable
:::
