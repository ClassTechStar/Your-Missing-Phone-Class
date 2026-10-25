---
id: di-san-shi-ba-zhang
num: 38
part: ai-biancheng-pian
nav: פרק 38: חמשת עקרונות החשיבה של תכנות בעזרת AI
toc: default
kind: chapter
---

### פרק 38: חמשת עקרונות החשיבה של תכנות בעזרת AI

{class="chapter-intro mb-4"}
אם הספר הזה יכול להשאיר אתכם עם פרק אחד בלבד, זה בהכרח הפרק הזה. חמשת עקרונות החשיבה הם לב הספר, וכל הפרקים שאחריהם — הקשר, דרישות, דיאלוג ואיכות — הם פשוט פיתוח של חמשת העקרונות האלה בסביבות שונות. בנחת: אף אחד מהם אינו קשה להבנה, אבל כל אחד מהם ראוי ש"ייכנס לשרירים" באמצעות כמה פרויקטים.

נקודת הפתיחה של הסיפור מעניינת: כש-Andrej Karpathy פתח את הפרויקט שלו לקהל הרחב, הוא צירף קובץ CLAUDE.md בן 70 שורות בלבד, שריכז ארבעה עקרונות ליבה לשיתוף פעולה עם AI. הקובץ צבר מעל 70,000 כוכבים ב-GitHub והפך לקוד ההתנהגות המצוטט ביותר בקרב מתרגלי התכנות בעזרת AI בעולם. ארבעת העקרונות אינם סיסמאות ריקות אלא הרגלי חשיבה מעשיים שהופקו מהיקף עצום של ניסיון. הספר הזה מוסיף עליהם עקרון חמישי — אימות איטרטיבי — ויוצר מערכת שלמה של חמישה עקרונות.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
מדוע קובץ בן 70 שורות שווה כל כך הרבה?

{class="mt-1"}
מה זה בכלל 70,000 כוכבים? רוב הפרויקטים ב-GitHub לא מגיעים למספר הזה אפילו במשך כל חייהם. העובדה שקובץ טקסט בן 70 שורות השיג זאת מוכיחה דבר אחד: הדבר הנדיר ביותר בעידן ה-AI אינו קוד, אלא היכולת "לחשוב בבהירות". שבעים השורות האלה הן הגרסה המרוכזת של "לחשוב בבהירות".
:::

#### א. עקרון ראשון: Think Before Coding (חשיבה קודם, קידוד אחר כך)

זהו העקרון האנטי-אינטואיטיבי ביותר מבין החמישה. אם AI יכול לכתוב לנו קוד, למה צריך "לחשוב קודם"? התשובה פשוטה: איכות התוצר של ה-AI פרופורציונלית לאיכות הקלט שלכם. אם גם אתם לא ברורים לעצמכם מה רוצים לעשות, התשובות שה-AI ייתן רק יסחבו אתכם למעגל אינסופי של "מתקנים שוב ושוב" — המכונה בפי העם "AI שהולך אתכם לאיבוד יחד".

"לחשוב קודם" פירושו שלפני שאתם מוסרים הוראה ל-AI עליכם לענות על שלוש שאלות, המרכיבות יחד "משולש חשיבה" שאי אפשר בלי אף פינה שלו:

1. איזו בעיה אני רוצה לפתור? (מטרה)
2. איך נראית התוצאה שאני מצפה לה? (קריטריוני קבלה)
3. אילו אילוצים צריך לכבד? (גבולות)

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ממד החשיבה</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">קלט מעורפל (רע)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">קלט ברור (טוב)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">הגדרת הבעיה</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">תעשה לי אתר</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">בנה לי אתר כלים אישי שמציג שלושה כרטיסי כניסה לכלי AI קטנים</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">התוצאה הצפויה</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">שיהיה קצת יפה</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">פריסה רספונסיבית, ערכת נושא כהה, אנימציית ריחוף בכרטיסים, ושיהיה שמיש גם בנייד</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">אילוצים</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">(לא צוין)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">בלי פריימוורק, HTML+CSS+JS בלבד, פריסה בקובץ יחיד, בלי בק-אנד</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
השוואה בין קלט מעורפל לקלט ברור לאותה דרישה

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
שימו לב: לחשוב קודם ≠ לכתוב קודם מסמך מושלם

{class="mt-1"}
"לחשוב קודם" אינו שווה ל"כתוב תחילה PRD מושלם". זהו תהליך חשיבה מהיר אך מסודר — שלושים שניות של הבהרת שלוש השאלות שלעיל יעילות הרבה יותר משלושים דקות של תיקונים חוזרים בשיחה. במשימות קטנות שלוש השאלות יכולות להיות קצרות; בפרויקטים גדולים אפשר לפתח אותן למסמך דרישות מלא (ראו פרק 40).
:::

#### ב. עקרון שני: Simplicity First (פשטות לפני הכול)

המלכודת הגדולה ביותר בתכנות בעזרת AI אינה "לא מצליחים לעשות", אלא "עושים יותר מדי". כשאתם אומרים ל-AI "בנה מערכת לניהול משתמשים", ייתכן שהוא יחולל חבילה שלמה של יכולות — אימות, הרשאות, תפקידים, יומני ביקורת וייצוא נתונים — בזמן שאתם צריכים כרגע רק עמוד התחברות פשוט. יתר-ייצור הוא הגורם העיקרי לנפיחות של קוד AI.

"פשטות לפני הכול" מחייבת אתכם לדבוק בעיקרון ה"מינימום הבר-קיימא" בכל הוראה: לממש את הפונקציונליות המרכזית בקוד המעט ביותר, לפתור בעיות בפתרון הפשוט ביותר ולבחון רעיונות במינימום הפיצ'רים. ל-Karpathy יש מטאפורה חדה לכך: "אם אתה צריך לחשב מחיר מוזל, אינך צריך מנוע מסחר אלקטרוני."

בפועל, "פשטות לפני הכול" מתורגמת לכמה הרגלי עבודה קונקרטיים:

- בכל פעם תבקשו מה-AI לממש נקודת פונקציונליות אחת, בלי לתאר את כל המערכת בנשימה אחת;
- העדיפו ספריות סטנדרטיות ופתרונות פשוטים על פני תלות מורכבת;
- אם בעיה נפתרת ב-50 שורות קוד, אל תתנו ל-AI לכתוב 500;
- כשהתוצר של ה-AI חורג מהיקף הציפיות, אמרו לו בביטחה "קצץ את העודפים".

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">תרחיש</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">פתרון יתר (הימנעו)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">פתרון פשוט (מומלץ)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">צריך לאחסן נתונים</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">הקמת מסד נתונים MySQL + ORM</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">להתחיל בקובץ JSON או SQLite</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">צריך התחברות משתמשים</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OAuth2.0 + JWT + הרשאות תפקידים</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">להתחיל באימות סיסמה פשוט</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">צריך פריימוורק פרונט-אנד</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">React + Redux + Router</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">לנסות קודם HTML טהור + vanilla JS</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">צריך פריסה לאוויר</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Docker + CI/CD + K8s</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">קודם להריץ מקומית, ואז נדבר</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
השוואה בין פתרון יתר לפתרון פשוט בתרחישים נפוצים

#### ג. עקרון שלישי: Surgical Changes (תיקון מדויק)

כשאתם משפרים פרויקט קיים, כל שינוי צריך להיות מדויק כניתוח כירורגי — לגעת רק במה שצריך לשנות ולא לגעת באסור לגעת. זה קריטי במיוחד בתכנות בעזרת AI, כי ל-AI יש נטייה ל"כבר תוך כדי אתקן גם את זה": תבקשו ממנו לתקן באג אחד, והוא עלול לבנות מחדש חצי קובץ.

דרישת הליבה של "תיקון מדויק" היא שבכל הוראה ל-AI תציינו במפורש את היקף השינוי ואת גבולותיו. אמרו לו "שנה רק את הפונקציה calculate_discount", "אל תיגע בשאר החלקים", "שמור על סגנון הקוד הקיים". כשהשינויים של ה-AI חורגים מהיקף שביקשתם, דרשו ממנו מיד להחזיר את העודפים.

Karpathy המחיש זאת באמצעות דוגמת diff (השוואת גרסאות). נניח שביקשתם מה-AI להוסיף לוגיקת "מחיר חבר" לפונקציית חישוב ההנחה בעגלת הקניות: תוצר טוב נוגע רק בפונקציה הזאת ומוסיף כמה שורות קוד; תוצר רע בונה מחדש את הקובץ כולו — גם אם הקוד החדש נראה "אלגנטי" יותר, אינכם יכולים לדעת אם הוא הכניס באגים חדשים. בתכנות בעזרת AI, "נראה יותר טוב" אינו עולה ולא מתקרב להצדקה לסטות מההוראות.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
הוראה גרועה (היקף מעורפל)

{class="font-mono text-xs leading-relaxed"}
עזור לי לשפר את הלוגיקה של חישוב ההנחות בפרויקט הזה
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
הוראה טובה (היקף מוגדר במדויק)

{class="font-mono text-xs leading-relaxed"}
שנה רק את הפונקציה calculate_discount בקובץ cart.py: 1. הוסף לוגיקת מחיר חבר על בסיס ההנחה הקיימת 2. משתמשי חבר מקבלים 10% הנחה נוספים 3. אל תשנה את חתימת הפונקציה ואת שאר הפונקציות 4. שמור על סגנון השמות הקיים של המשתנים
:::
:::

#### ד. עקרון רביעי: Goal-Driven Execution (ביצוע מונחה מטרה)

העקרון הזה עונה על שאלה מרכזית: האם להורות ל-AI "איך לעשות" או "מה לעשות"? התשובה של Karpathy: את השני. במקום לומר ל-AI "קודם צור מחלקה, אחר כך הוסף מתודות, ואז כתוב בדיקות", עדיף לומר לו "אני צריך כלי שמנתח קובץ CSV ומונה את מספר הערכים הייחודיים בכל עמודה". תנו ל-AI לבחור בעצמו את נתיב המימוש, ואתם תאשרו את התוצאות.

היתרון של "מונחה מטרה" הוא כפול. ל-AI זה נותן מרחב פעולה גדול יותר לבחור בנתיב המימוש האופטימלי, במקום להיות כבול לצעדי הביניים שלכם; ולכם זה מאפשר להעביר את תשומת הלב מ"איך עושים" אל "האם התוצאה נכונה" — וזה בדיוק תפקידו של המנצח.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
שימו לב: מונחה מטרה ≠ לתת לזה ללכת

{class="mt-1"}
הוא מחייב אתכם לבצע קבלה קפדנית אחרי שה-AI מסיים: האם התוצאה עונה על הדרישות? האם מקרי הקצה טופלו? האם יש תכנון-יתר בולט? אם התוצאה אינה כצפוי, ספקו משוב קונקרטי — לא "כתוב מחדש", אלא "הבעיה כאן היא שקלט של רשימה ריקה זורק IndexError; הוסף בדיקת ערך ריק".
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">סגנון ההוראה</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">דוגמה</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">מאפייני התוצאה</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">פקודתי (איך לעשות)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"קודם צור מחלקת Python בשם DataParser, הוסף מתודה parse שמקבלת פרמטר filename וקוראת באמצעות מודול csv…"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ה-AI הופך לקלדן, וצעדי הביניים שלכם אולי אינם הנתיב האופטימלי</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מונחה מטרה (מה לעשות)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"אני צריך כלי: לקרוא קובץ CSV, לספור את מספר הערכים הייחודיים בכל עמודה ולפלוט פלט בפורמט JSON. תן מימוש מלא."</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ה-AI בוחר בעצמו את הנתיב האופטימלי, ואתם אחראים לאשר את התוצאות</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
השוואה בין הוראה פקודתית להוראה מונחית מטרה

#### ה. עקרון חמישי: Iterate and Verify (אימות איטרטיבי)

זהו העקרון החמישי שהספר הזה מוסיף על ארבעת עקרונות Karpathy. האמונה שבליבו: התוצר הראשון של ה-AI כמעט אף פעם אינו הגרסה הסופית. תכנות יעיל בעזרת AI הוא לולאת איטרציה של "יצירה-אימות-תיקון", ולא "הוראה-תוצר" חד-פעמית.

"אימות איטרטיבי" אינו "לא טוב? מנסים שוב" בהמתנה סבילנטית, אלא תהליך אימות מובנה. אחרי כל תוצר שה-AI מספק, מאמתים בשלוש רמות:

- רמה ראשונה — אימות תפקוד: האם זה בכלל רץ? האם הקלט והפלט נכונים?
- רמה שנייה — אימות גבולות: מה קורה עם קלט ריק, קלט ארוך מאוד או קלט חריג?
- רמה שלישית — אימות ארכיטקטורה: האם מבנה הקוד הגיוני? האם יש קידוד מאולץ (hardcoded)? האם קל להרחיב בהמשך?

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-bullseye mr-1"></i> הגדרת היעד</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> ה-AI מייצר קוד</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> בדיקה תפקודית</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> עבר</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> בדיקת גבולות</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> עבר</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-landmark mr-1"></i> סקירת ארכיטקטורה</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> עבר, ממשיכים לשלב הבא</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> לא עבר</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> לתת משוב ממוקד</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> לייצר מחדש</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
איור 2: לולאת האימות האיטרטיבי של תכנות בעזרת AI
:::

המפתח בלולאה הזאת הוא שלב "מתן משוב קונקרטי". כשהאימות נכשל, אל תאמרו "לא נכון, תעשה מחדש", אלא "הפונקציה זורקת IndexError כשמזינים רשימה ריקה; הוסף בדיקת ערך ריק בשורה 15". משוב קונקרטי מאפשר ל-AI לתקן במדויק; משוב מעורפל רק יגרום לו לנחש מחדש את כוונתכם.

#### ו. Harness Engineering: Agent = Model + Harness

באמצע 2026 החל מושג בשם Harness Engineering לצבור תאוצה בקהילת התכנות בעזרת AI. הנוסחה שבליבו פשוטה:

:::inline div .quote-line .text-center .text-base .font-bold
<strong>יכולת ה-Agent = יכולת המודל × איכות ה-Harness</strong>
:::

יכולת המודל היא תקרת האינטליגנציה של "המוח" של ה-AI; ה-Harness הוא "סביבת העבודה" הנבנית סביב המודל — ניהול הקשר, שילוב כלים, תזמור תהליכים, מערכות זיכרון ועוד.

המושג הזה מסביר תהייה נפוצה: מדוע, כשכולם משתמשים באותו GPT-4 או Claude, יש מי שמצליח להוציא פרויקטים מרהיבים ויש מי שמקבל רק קוד בינוני? ההבדל אינו במודל אלא ב-Harness. Harness טוב כולל: קובץ מוסכמות פרויקט ברור, שילוב כלים הגיוני, הקשר שיחה מסודר ותהליך אימות מלא. המודל קובע את תקרת האינטליגנציה, וה-Harness קובע עד כמה תוכלו לממש את התקרה הזאת.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
מטאפורת המתמחה המחונן

{class="mt-1"}
דמיינו את המודל כמתמחה מחונן — אינטליגנציה גבוהה, אבל אם לא תיתנו לו תיעוד רקע על הפרויקט, לא תגידו לו באילו כלים להשתמש ולא תקבעו לו לוחות זמנים וקריטריוני קבלה, הוא לא יוציא דבר טוב. Harness Engineering הוא ההנדסה של "איך להקים למתמחה המחונן סביבת עבודה נכונה".
:::

הפרקים הבאים בספר הזה, במהותם, מלמדים אתכם לבנות Harness טוב: פרק 39 מלמד לנהל הקשר (מערכת זיכרון הפרויקט), פרק 40 מלמד להגדיר דרישות (PRD), פרק 43 מלמד טכניקות דיאלוג (ריבוד Prompt), ופרק 45 מלמד הבטחת איכות (תהליך אימות). השילוב של כולם הוא ה-Harness שלכם.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
תרגול מעשי: פרקו את הרעיון הבא שלכם באמצעות "משולש החשיבה"

{class="mt-1"}
בחרו דבר קטן שרציתם תמיד לעשות ולא הרמתם יד (למשל עמוד ספירה לאחור לתאריך, או סקריפט לתזכורת לשתות מים). הקדישו 3 דקות לענות: (1) איזו בעיה הוא פותר? (2) איך הוא ייראה כשייבנה? (3) מהם האילוצים (זמן, טכנולוגיה, סביבה)? ואז כתבו את התשובות כפסקה אחת. מזל טוב — זה עתה ביצעתם את ה-"Think Before Coding" הראשון בחייכם, והפסקה הזאת היא הוראה איכותית ולגיטימית לכל דבר.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
סיכום הפרק

- חמשת העקרונות מקורם ב-CLAUDE.md בן 70 השורות של Karpathy (מעל 70 אלף כוכבים); הספר מוסיף עקרון חמישי — "אימות איטרטיבי"
- Think Before Coding: לפני שפותחים את הפה עונים על שלוש שאלות — מה עושים? איך נראית התוצאה? מהם האילוצים?
- Simplicity First: המלכודת הגדולה של AI היא "לעשות יותר מדי" — לחישוב הנחה אין צורך במנוע מסחר אלקטרוני
- Surgical Changes: לתקן בדיוק כירורגי, ולסרב ל"כבר תוך כדי אתקן גם את זה" של ה-AI
- Goal-Driven Execution: לומר "מה לעשות" ולא "איך לעשות", ולתת ל-AI לבחור בעצמו את הנתיב
- Iterate and Verify: אימות בשלוש רמות (תפקוד/גבולות/ארכיטקטורה) + משוב קונקרטי, בלולאות איטרציה
- Harness Engineering: יכולת = מודל × Harness — להתייחס ל-AI כאל "מתמחה מחונן" ולנהל את סביבתו
:::
