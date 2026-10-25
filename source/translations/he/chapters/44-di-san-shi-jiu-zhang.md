---
id: di-san-shi-jiu-zhang
num: 39
part: ai-biancheng-pian
nav: פרק 39: הנדסת הקשר – לגרום ל-AI להבין את הכוונה שלך
toc: default
kind: chapter
---

### פרק 39: הנדסת הקשר — לגרום ל-AI להבין את כוונתכם

{class="chapter-intro mb-4"}
האם קרה לכם: פתחתם חלון שיחה חדש, ופתאום ה-AI נראה כמי שסבל מאמנזיה ושכח לגמרי את כל מה שקשור לפרויקט שלכם? זה לא בגלל שה-AI מנסה להרגיז אתכם — זו פשוט "שכחה" מולדת שלו. בפרק זה תלמדו להתקין ל-AI "מערכת זיכרון ארוכת טווח", ובדרך תכירו אחת מפרדיגמות הפיתוח החמות של 2026 — פיתוח מונחה מפרט (Spec-Driven Development).

#### א. קובץ זיכרון הפרויקט: "הזיכרון ארוך הטווח" של ה-AI

למודלי AI יש מגבלה יסודית: הזיכרון שלהם "קצר". בכל תחילת שיחה הידע של ה-AI על הפרויקט שלכם שווה אפס. עליכם להסביר לו שוב ושוב בתוך השיחה "אנחנו עובדים עם React", "הבק-אנד הוא Node.js", "מסד הנתונים הוא PostgreSQL", "סגנון הקוד — מירכאות כפולות". זה לא רק בזבזני, אלא גם מזמן השמטות — כמו לערוך מדי יום קבלת עובדים מחדש לעמית חדש.

הפתרון הוא "קובץ זיכרון הפרויקט" — קובץ טקסט פשוט בתיקיית השורש של הפרויקט, שכלי ה-AI קוראים אוטומטית בכל תחילת שיחה. לכל כלי יש מוסכמת שמות משלו:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">כלי</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">שם הקובץ</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cursorrules</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">CLAUDE.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitHub Copilot</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">copilot-instructions.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">פתרון כללי</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">AGENTS.md</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
מוסכמות השמות של קובצי זיכרון הפרויקט בכלי השונים

אמנם השמות שונים, אבל העיקרון אחד: את המידע שאתם רוצים שה-AI "יזכור תמיד" כותבים בקובץ הזה. קובץ זיכרון פרויקט טוב אמור לכלול: סקירת הפרויקט (מהו הפרויקט), מחסנית טכנולוגיות (במה משתמשים), כללי קוד (שמות, הזחה, סגנון הערות), מבנה תיקיות (איך הקוד מאורגן) ומוסכמות פיתוח (אסטרטגיית ענפים, כללי קומיט, דרישות בדיקות). ה-CLAUDE.md של Karpathy מכיל 70 שורות בלבד, ומכסה את כל המידע הקריטי — תמציתי אך ממצה.

::: div .code-block
:::inline div .code-head
<span>CLAUDE.md</span><span class="dots">···</span>
:::

```
# פרויקט: אפליקציה לניהול הוצאות אישיות
## סקירה
אפליקציית full-stack לניהול הוצאות אישיות שעוזרת למשתמש לתעד הכנסות והוצאות יומיות.
## סטאק טכנולוגי
- Frontend: React + TypeScript + Tailwind CSS
- Backend: Node.js + Express + TypeScript
- מסד נתונים: SQLite (פיתוח) / PostgreSQL (ייצור)
- בדיקות: Vitest
## כללי קוד
- להשתמש במרכאות כפולות
- הזחה של 2 רווחים
- שמות פונקציות ב-camelCase
- הגדרות טיפוסים ב-PascalCase
- לכל פונקציה חייב להיות תיעוד JSDoc
## מבנה תיקיות
/src
  /frontend  - קוד הפרונט
  /backend   - קוד הבק
  /shared    - טיפוסים משותפים לפרונט ולבק
  /tests     - קבצי בדיקה
## הסכמי פיתוח
- הודעות commit בעברית
- כל יכולת חדשה מתחילה בבדיקה
- תשובות ה-API תמיד בפורמט { success, data, error }
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
שימו לב: אל תהפכו אותו ל"מסמך דרישות שני"

{class="mt-1"}
שימו לב לאורך הקובץ — אל תכתבו מסמך דרישות בן עשרות עמודים. מטרת קובץ זיכרון הפרויקט היא "לאפשר ל-AI לבנות במהירות תמונת רקע", לא "לתאר כל פיצ'ר לעומק". שמרו על תמציתיות, על מבנה ברור, וכתבו רק את "מה שה-AI צריך לדעת".
:::

#### ב. פיתוח מונחה מפרט (SDD)

Spec-Driven Development (SDD, פיתוח מונחה מפרט) היא פרדיגמת פיתוח שהבשילה בהדרגה ב-2026, ורעיון הליבה שלה במשפט אחד: קודם כותבים מפרט, ואז כותבים קוד. בשונה מ-TDD המסורתי (פיתוח מונחה בדיקות), ה"מפרט" ב-SDD אינו רק מקרי בדיקה, אלא כולל גם תיאור דרישות, הגדרות ממשק, מודלי נתונים ועוד. ה-AI מחולל קוד על סמך המפרטים האלה, ותפקיד בני האדם הוא לכתוב ולתחזק את המפרט.

תהליך העבודה של SDD בחמישה צעדים:

1. מתארים את מפרט הדרישות בשפה טבעית (בתוך קובץ .md);
2. מגדירים ממשקים ומבני נתונים (בתוך קובץ המפרט);
3. מבקשים מה-AI לחולל את מימוש הקוד על סמך המפרט;
4. מריצים בדיקות לאמת שהתוצר תואם למפרט;
5. אם אין התאמה — מתקנים את המפרט או מבקשים מה-AI לתקן את הקוד.

בתהליך הזה קובץ המפרט הוא "מקור האמת היחיד" — את הקוד אפשר לחולל מחדש, אבל המפרט חייב להיות נכון תחילה.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> כתיבת מסמך המפרט</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> האם המפרט מלא?</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> מלא</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> ה-AI מייצר קוד על פי המפרט</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> להריץ בדיקות כדי לוודא את התוצר</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> לא מלא / הבדיקות נכשלות</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-tools mr-1"></i> בעיה בקוד → תקן את הקוד; בעיה במפרט → תקן את המפרט</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> חזרה לבדיקה</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> הכול עבר → מסירה</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
איור 3: תהליך העבודה של פיתוח מונחה מפרט (SDD)
:::

יתרונו של SDD: קובץ המפרט יציב יותר מהקוד. כשהמודל או הכלי משתנים, קובץ המפרט שלכם נותר בתוקף, וכל שנדרש הוא לבקש מכלי AI חדש לחולל את הקוד מחדש. וזו בדיוק הסיבה שהספר הזה מדגיש "המתודולוגיה חשובה יותר מהכלים" — קובץ המפרט הוא הנשא המוחשי של המתודולוגיה שלכם.

#### ג. ניהול חלון ההקשר

גם עם קובץ זיכרון פרויקט, עדיין תיתקלו בשיחות בבעיית "אין מספיק הקשר". חלון ההקשר של מודל AI (כמות המידע שהוא מסוגל לעבד בו-זמנית) הוא מוגבל. כשהשיחה ארוכה מדי ומוזכרים בה יותר מדי קבצים, ה-AI "שוכח" מידע מוקדם ואיכות התוצר יורדת — כמו חבר שאיתו שוחחתם שעות ושכבר שכח את הדבר הראשון שסיפרתם לו בתחילת היום.

האסטרטגיה המרכזית לניהול חלון ההקשר היא "התייחסות בשכבות":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">שכבת ההקשר</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">תוכן</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">אופן הניהול</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">שכבה ראשונה: זיכרון הפרויקט</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מחסנית טכנולוגיות, מפרטים, מבנה תיקיות</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">נכתב בקבצים כמו CLAUDE.md, נטען אוטומטית ואין צורך לחזור עליו</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">שכבה שנייה: התייחסות לקבצים</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">קובצי הקוד הנוגעים למשימה הנוכחית</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מפנים במדויק באמצעות סימן @, בלי להדביק את הקובץ המלא לשיחה</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">שכבה שלישית: הקשר השיחה</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">היסטוריית השיחה של המשימה הנוכחית</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">אחרי השלמת משימה פותחים שיחה חדשה, כדי למנוע נפיחות הקשר</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">שכבה רביעית: הוראות מיידיות</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">הדרישות הספציפיות של הצעד הנוכחי</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">בהירות, תמציתיות ומיקוד, בלי תיאורים ארוכים</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
אסטרטגיית הניהול השכבתי של חלון ההקשר

#### ד. נקודות מפתח בתרגול של הנדסת הקשר

הנדסת הקשר אינה הגדרה חד-פעמית אלא תהליך של שיפור מתמיד. הנה כמה נקודות שאומתו שוב ושוב בשטח:

1. מעדכנים את קובץ הזיכרון בהתאמה עם התפתחות הפרויקט. כשמאמצים טכנולוגיה חדשה או משנים ארכיטקטורה — מעדכנים מיד את קובץ הזיכרון, במקום להסביר זאת באופן חד-פעמי בתוך השיחה.
2. מנצלים התייחסות ב-@ במקום הדבקת טקסט מלא. רוב כלי התכנות בעזרת AI תומכים בתחביר @file או @folder, שמזריקים את תוכן הקובץ להקשר של ה-AI ברקע — יעיל יותר מהדבקה ידנית ולא מזהם את השיחה.
3. שומרים על שיחות "קצרות וממוקדות". שיחה אחת מטפלת במשימה אחת או בנקודת פונקציונליות אחת. בסיומה פותחים שיחה חדשה למשימה הבאה. שיחה ארוכה לא רק שוחקת את חלון ההקשר, אלא גם מסיחה את דעת ה-AI.
4. נותנים ל-AI "לראות" את התוצאה ולא "לשמוע תיאור" שלה. כשנתקלים בבאג, מפנים את יומן השגיאות ישירות ב-@ ל-AI, במקום לתאר במילים שלכם "נראה לי שיש איזו שגיאה". ל-AI קל יותר לעבד את המידע הגולמי מאשר את תמציתכם.
5. מנקים ומארכיבים באופן קבוע. שיחות שהסתיימו וקבצים זמניים תופסים מקום עבודה. ניקוי קבוע של תוכן לא רלוונטי ושמירה על תיקיית פרויקט מסודרת עוזרים גם ל-AI להבין את מבנה הפרויקט ביעילות רבה יותר.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
תרגול מעשי: כתבו לפרויקט שלכם קובץ זיכרון בן 70 שורות

{class="mt-1"}
בחרו פרויקט שאתם עובדים עליו (או מתכננים להתחיל), וכתבו קובץ CLAUDE.md: סקירת הפרויקט (2-3 משפטים), מחסנית הטכנולוגיות (רשימה), כללי קוד (3-5 סעיפים), מבנה תיקיות (אילן קטן) ומוסכמות פיתוח (2-3 סעיפים). הקפידו לא לחרוג מ-70 שורות — בסיום תגלו שגם ההבנה שלכם את הפרויקט התבהרה משמעותית.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
סיכום הפרק

- הזיכרון של ה-AI הוא "קצר": בכל שיחה חדשה הידע שלו על הפרויקט שווה אפס
- קובץ זיכרון הפרויקט (CLAUDE.md ודומיו) הוא "הזיכרון ארוך הטווח" של ה-AI, ונטען אוטומטית בכל שיחה
- קובץ זיכרון טוב = סקירה + מחסנית טכנולוגיות + מפרטים + תיקיות + מוסכמות — 70 שורות מספיקות
- SDD — פיתוח מונחה מפרט: קודם מפרט ואז קוד; המפרט הוא "מקור האמת היחיד" ויציב יותר מהקוד
- ההקשר מנוהל בארבע שכבות: זיכרון הפרויקט → התייחסות לקבצים ב-@ → היסטוריית שיחה → הוראות מיידיות
- חמש נקודות תרגול: עדכון מסונכרן, התייחסות ב-@, שיחות קצרות, מתן מידע גולמי, ניקוי תקופתי
:::
