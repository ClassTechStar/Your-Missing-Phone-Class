---
id: di-wu-shi-liu-zhang
num: 56
part: an-zhuo-kai-fa-pian
nav: פרק 56: ליטוש ופרסום – עלייה ל-Google Play
toc: default
kind: chapter
---

### פרק 56: ליטוש והוצאה לאור – בדיקות, ניפוי באגים ועלייה ל-Google Play

{class="chapter-intro mb-4"}
האפליקציה נבנתה – ומה עכשיו? הפרק הזה עונה על שלושה עניינים בדרך מ"זה רץ" אל "זה מוכן למסירה": איך לנפות באגים ביעילות, איך לכתוב בדיקות שמונעות נסיגות, ואיך להעלות את האפליקציה ל-Google Play כדי שכל העולם יוכל להוריד אותה. עלייה לחנות היא לא רק טקס – זהו קו הפרדה בין יצירה למוצר.

#### א' שלושת כלי הניפוי: Logcat, נקודות עצירה ובודק ה-UI

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">כלי</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">למה הוא משמש</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">איך משתמשים</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logcat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">צפייה בלוגים של המערכת או שלכם</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">בקוד: Log.d("TAG","ערך=$x"), ובפאנל מחפשים את ה-TAG לסינון</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ניפוי עם נקודות עצירה</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">לעצור את התוכנית בשורה מסוימת ולבחון ערכי משתנים</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">לוחצים ליד מספר השורה – מופיעה נקודה אדומה; מריצים במצב Debug ומתקדמים שורה אחר שורה</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Layout Inspector</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">צפייה במבנה המסך בזמן ריצה</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">בתפריט Tools → Layout Inspector, צפייה בזמן אמת בעץ הרכיבים</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
שלושת כלי הניפוי

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
טיפ: איך קוראים הודעת שגיאה?

{class="mt-1"}
אחרי קריסה תופיע ב-Logcat מחסנית אדומה (Stacktrace); חפשו מלמטה למעלה את השורה הראשונה שמתחילה בשם החבילה שלכם (למשל com.example.yourapp) – שורה זו היא בדרך כלל זירת הפשע. קודם בדקו את "סוג ה-Exception" (מצביע ריק? המרת טיפוס?), ואז את "at ... הקובץ שלכם:מספר השורה". הטריק הזה פותר 80% מהקריסות.
:::

#### ב' בדיקות: ביטוח לקוד

בדיקה ידנית אינה אמינה – מתקנים תכונה אחת ואחרת נשברת בשקט. בדיקות הן "כדור התחרפות" וגם "שריון יורה". בדיקות האנדרואיד מתחלקות לשלוש שכבות, ומתחילים צריכים קודם כול לשלוט בשכבה הראשונה:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">שכבה</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">מה בודקים</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">היכן ממוקם</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">מהירות</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">בדיקות יחידה</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">לוגיקה טהורה (חישובים, ולידציה)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/test/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">שניות</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">בדיקות מכשיר (Instrumented)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">התנהגות המסך על מכשיר אמיתי</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/androidTest/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">דקות</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">בדיקה ידנית</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">תחושה וחוויה של אדם אמיתי</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">תמיד נחוצה</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
שלוש שכבות הבדיקות

::: div .code-block
:::inline div .code-head
<span>KOTLIN · דוגמת בדיקת יחידה</span><span class="dots">···</span>
:::

```
// לחלץ את הלוגיקה של "המרת טקסט הסכום למספר" לפונקציה טהורה
fun parseAmount(input: String): Double? {
    val v = input.trim().toDoubleOrNull()
    return if (v != null && v > 0) v else null
}

// בדקו אותה (JUnit4)
@Test
fun emptyInputReturnsNull() {
    assertEquals(null, parseAmount(""))
}
@Test
fun negativeReturnsNull() {
    assertEquals(null, parseAmount("-5"))
}
@Test
fun normalValueParses() {
    assertEquals(12.5, parseAmount("12.5"))
}
```
:::

את בדיקות הסכום והחישובים הסטטיסטיים בספר החשבונות צריך לכסות בבדיקות יחידה. הרצת בדיקות: קליק ימני על תיקיית test → Run. ירוק – הכול עבר; עכשיו אפשר לשנות קוד בראש שקט.

#### ג' חתימה ואריזה: לתת לאפליקציה "חותמת"

אנדרואיד דורשת שכל חבילת התקנה תהיה חתומה – כמו חותמת רשמית שמאשרת "החבילה הזאת יצאה ממני ולא שונתה". בזמן פיתוח Android Studio חותמת אוטומטית בחתימת debug; להפצה דרושה חתימת release משלכם. התהליך:

1. בתפריט Build → Generate Signed Bundle / APK;
2. יוצרים קובץ keystore (מחסן מפתחות) – מגדירים סיסמה ושומרים עליה היטב;
3. בוחרים release בפורמט AAB – והבנייה הושלמה.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
אזהרה: keystore שאבד = אפליקציה שאבדה

{class="mt-1"}
עדכון האפליקציה אחרי העלייה לחנות חייב להתבצע עם אותה חתימה, אחרת החנות תדחה את העדכון. אם קובץ ה-keystore והסיסמה אבדו, תיאלצו להעלות אפליקציה חדשה מאפס – וכל המשתמשים הוותיקים יישארו מחוץ למשחק. הקפידו לגבות את ה-keystore והסיסמה במקום בטוח (ענן מוצפן + מחברת רשומה) – זהו אחד השיעורים היקרים ביותר של מפתחי אנדרואיד.
:::

#### ד' התהליך המלא של עלייה ל-Google Play

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> רישום חשבון מפתח</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> הכנת חומרים לחנות</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> העלאת ה-AAB</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> מילוי טופס אבטחת המידע</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> בדיקה (שעות עד ימים)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> פרסום</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
איור 6: שישה שלבים לעלייה ל-Google Play
:::

- רישום: דמי רישום חד-פעמיים של 25 דולר; נדרש חשבון Google תקין;
- חומרים: אייקון אפליקציה (512×512), צילומי מסך (לפחות 2), תיאור התכונות וקישור למדיניות פרטיות (חובה כשאוספים נתונים);
- טופס אבטחת נתונים: מצהירים ביושר על הנתונים שנאספים – ספר חשבונות ללא חיבור לרשת יכול להצהיר "אפס איסוף";
- ביקורת: חשבונות חדשים בהעלאה הראשונה עוברים לרוב בדיקה אנושית, מכמה שעות ועד כמה ימים; אם דוחים – מתקנים לפי ההערות.

לתשומת לב משתמשים בסין: Google Play דורש סביבת רשת מיוחדת, ובסין היבשתית ההפצה נעשית בדרך כלל דרך החנויות המקומיות (Huawei, Xiaomi, MyApp וכדומה). תהליך העלאה לחנות מקומית דומה, אך לכל חנות טעם ביקורת משלה – אותו AAB/APK אפשר להפיץ בכמה חנויות. לצורך תרגול – לעבור בהצלחה חנות אחת כבר ניצחון.

#### ה' איך מכינים את חומרי החנות: הרושם הראשון שווה הורדות

עמוד החנות הוא הוויטרינה שהמשתמש רואה ב"טיול בחנות". שלושה חומרים קובעים את הרושם הראשוני:

- אייקון: ‏512×512, אל תסתפקו בצילום מסך. אין כישורי עיצוב? צרו עם כלי AI צורה גיאומטרית פשוטה; האייקון עובר רק אם מזהים אותו במבט אחד גם כשהוא מוקטן על מסך הבית של הטלפון;
- צילומי מסך: לפחות 2, עדיף 4-6, שמציגים את תרחישי השימוש המרכזיים; לכל אחד שורת טקסט בשפה פשוטה ("רושמים עסקה בשנייה" טובה פי עשרה מ"פתרון יעיל לניהול חשבונות");
- תיאור: המשפט הראשון מסביר "מה זה + למי זה מיועד"; אל תערמו "הכי מקצועי, הכי חזק" – משקל החיפוש בחנות נקבע בעיקר לפי מילות מפתח ושיעור המרה להורדות, וכנות יעילה יותר מהגזמה.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
טיפ: עשו A/B והסתכלו על המתחרים

{class="mt-1"}
לפני העלייה, סיירו בעשירייה הפותחת של אפליקציות דומות בחנות והשוו צילומי מסך: איזה סגנון אייקון יש להן? מה נקודת המכירה בצילומים? איך נוסח הכותרת? חיקוי אינו העתקה – לומדים את המתכונת ומחליפים לתוכן משלכם; זהו השיעור המהיר ביותר להשקה קרה של כל מוצר.
:::

#### ו' רשימה קצרה לאופטימיזציית ביצועים ודיווח קריסות

לפני שהאפליקציה עולה לחנות, שווה להקדיש לכל אחד משני הדברים האלה חצי שעה:

##### 1. ארבעה סעיפים לבדיקת ביצועים עצמית

1. רשימות ב-LazyColumn: לעולם אל תסדרו רשימה ארוכה ב-Column רגיל – טעינה עצלה היא השיעור הראשון בביצועי אנדרואיד;
2. אל תדחפו תמונות מקור בגודל מלא: השתמשו בספריית התמונות Coil לשינוי קנה מידה ומטמון אוטומטיים; תמונת מקור אחת של 5MB מספיקה כדי לחנוק מכשיר חלש;
3. הימנעו מעבודה כבדה בת'רד הראשי: מסד נתונים, רשת וקבצים גדולים – הכול בתוך קורוטינות;
4. מדדו עם Profiler: כלי ניתוח הביצועים המובנה ב-Android Studio מציג זיכרון, CPU וצריכת סוללה – קודם מודדים, אחר כך מייעלים; אל תסתמכו על ההרגשה.

##### 2. דיווח קריסות

זה שלא קרס אצלכם בבדיקות לא אומר שלא יקרוס בטלפון של משתמשים. לפני העלייה חברו את Firebase Crashlytics (הרשמי של גוגל, חינמי): כמה שורות הגדרה, ובכל קריסת משתמש נשלחת אוטומטית המחסנית – בממשק הניהול תראו "איזה דגם, איזו גרסה, ובאיזו שורה קרס". עלייה לחנות בלי ניטור קריסות שווה נהיגה בעיניים עצומות.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
הגיע הזמן להתנסות: "למסור" את ספר החשבונות פעם אחת

{class="mt-1"}
① הוסיפו 3 בדיקות יחידה ללוגיקה כמו parseAmount; ② תפסו במו ידיכם ב-Logcat קריסה שיצרתם בעצמכם ותקנו אותה; ③ צרו APK עם חתימת release ושלחו לחבר להתקנה (זהו בדיוק טקס "היצירה"); ④ אם נשאר כוח – רשמו חשבון מפתחים והגישו באמת את ספר החשבונות לחנות. את שלושת הראשונים אפשר להשלים עוד הערב.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
סיכום הפרק

- שלושת כלי הניפוי: Logcat ללוגים, נקודות עצירה למשתנים, Layout Inspector למסך
- קריאת קריסה: מלמטה למעלה במחסנית, מוצאים את השורה הראשונה עם שם החבילה שלכם
- שלוש שכבות בדיקות: יחידה (שניות – מתחילים בזה)/מכשיר/ידנית
- הפצה מחייבת חתימה: גבו את ה-keystore ואת הסיסמה; אם אבדו – לאפליקציה "מחליפים זהות"
- ששת שלבי העלייה לחנות: רישום → חומרים → העלאת AAB → טופס אבטחת נתונים → ביקורת → פרסום
:::
