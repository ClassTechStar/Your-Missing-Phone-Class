---
id: di-liu-shi-zhang
num: 60
part: ios-kai-fa-pian
nav: פרק 60: הקמת סביבת הפיתוח – Xcode והפרויקט הראשון
toc: default
kind: chapter
---

### פרק 60: הקמת סביבת הפיתוח — Xcode והפרויקט הראשון

{class="chapter-intro mb-4"}
לפני שעושים את המלאכה, מחדדים את הכלים. בפרק הזה נקים את "המטבח": נתקין את Xcode, נריץ בהצלחה את המדמה, ניצור את פרויקט ה-iOS הראשון שלכם בחיים, ואז נפרק את מבנה הפרויקט ונבין אותו לעומק. אחרי שהסביבה מוכנה, תראו בפעם הראשונה את הקוד שכתבתם הופך לכפתור שאפשר ללחוץ עליו — רגע שהרבה אנשים זוכרים כל החיים.

#### 1. מכינים מק

קודם כל המחסום: פיתוח ל-iOS חייב להתבצע על macOS. אין לכם מק? יש שלוש אפשרויות: לקנות אחד (גם Mac mini או MacBook Air מיד שנייה מספיקים לגמרי), לשכור מק בענן לטווח קצר, או להתחיל קודם בחלק השמיני "פיתוח מעשי ל-Android" (אפשר גם מ-Windows).

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">הגדרה</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">דרישה מינימלית</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">קו נוח (מומלץ)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מעבד</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Silicon (מ-M1 ומעלה)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">M2 וחדשים יותר</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">זיכרון (RAM)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8GB</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">16GB</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">דיסק</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">להשאיר 40GB ומעלה (Xcode עצמו אחד שמן במיוחד)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256GB ומעלה</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מערכת</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">macOS העדכני ביותר</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">להשאיר עדכונים אוטומטיים</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
הגדרות ייחוס למחשב פיתוח מק (אוגוסט 2026)

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
טיפ: אפשר ללמוד את השפה גם בלי מק

{class="mt-1"}
Swift Playgrounds החינמי ב-iPad מאפשר ללמוד את יסודות שפת Swift (בלי מק); אפשר להתקין אותו גם ב-iPhone. שחקו קודם עם חומר השפה של פרק 61 ב-Playgrounds עד שיהיה לכם בקצה האצבעות, וכשתקבלו מק — תמריאו ישר. "חידוד הגרזן לא גוזל מזמן הכריתה" — זה בדיוק העניין.
:::

#### 2. מתקינים את Xcode

Xcode היא סביבת הפיתוח המשולבת הרשמית של אפל, והיא חינמית. התקנה בשלושה צעדים:

1. במק פתחו את ה-App Store, חפשו "Xcode" ולחצו על התקנה — שימו לב שמדובר בכמה GB, בחרו שעה עם רשת מהירה;
2. בהפעלה הראשונה אחרי ההתקנה אשרו את הרישיון והשלימו התקנת רכיבים (מתבצע אוטומטית);
3. בתפריט Xcode → Settings → Locations ודאו ש-Command Line Tools נבחר — כלי שורת הפקודה הם תנאי מוקדם להרבה סקריפטים וכלים של צד שלישי.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
שימו לב: "משחק ההתאמה" בין גרסאות למערכת

{class="mt-1"}
Xcode חדש דורש לרוב את macOS העדכני ביותר, ומק ישן עלול להיתקע בגרסה ישנה. בעלייה ל-App Store אפל מחייבת בנייה ב-Xcode חדש יחסית (בדרך כלל ניתנת תקופת חסד). לכן אל תדחו עדכוני מערכת יותר מדי — מפתחי iOS הם מהקבוצות שדוהרות אחרי גרסאות חדשות בלהט הרב ביותר.
:::

#### 3. יוצרים את הפרויקט הראשון שלכם

פתחו Xcode → Create New Project → בחרו iOS → תבנית App, ואז מלאו:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">הגדרה</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">מה ממלאים</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">הסבר</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Product Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstApp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">שם האפליקציה</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ה-Apple ID שלכם (חינם)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">לצורך החתימה; חשבון אישי מספיק</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Organization Identifier</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מצורף ל-Product Name ליצירת מזהה החבילה</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interface</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">הפריימוורק הראשי של הספר</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Language</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">פשוט מאליו</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
חמשת הפרטים למילוי ביצירת פרויקט

אחרי לחיצה על Create, Xcode ייצור פרויקט שרץ מיד. בפינה השמאלית העליונה בחרו מדמה (למשל iPhone 17) ולחצו על ▶ להרצה — כעבור מספר שניות יופיע על מסך המדמה חלון עם הכיתוב "Hello, world!". האפליקציית ה-iOS הראשונה שלכם כבר נולדה.

#### 4. פירוק מבנה הפרויקט: מה תפקידו של כל קובץ

בצד שמאל נמצא סייר הפרויקט; למתחילים מספיק להכיר את אלה:

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="290" viewBox="0 0 600 290" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="290" fill="#fafafa" rx="8"/>
      <text x="20" y="28" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ תיקיית השורש של הפרויקט</text>
      <rect x="30" y="42" width="540" height="225" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <rect x="45" y="56" width="250" height="196" fill="#eef2ff" rx="5"/>
      <text x="56" y="78" font-size="11" fill="#1e1b4b" font-weight="bold">MyFirstApp/ (תיקיית הקוד)</text>
      <text x="66" y="100" font-size="10" fill="#374151">├ MyFirstAppApp.swift  ← נקודת הכניסה</text>
      <text x="66" y="120" font-size="10" fill="#374151">├ ContentView.swift  ← המסך הראשי</text>
      <text x="66" y="140" font-size="10" fill="#374151">└ Assets.xcassets  ← אייקונים, תמונות, צבעים</text>
      <text x="56" y="166" font-size="10" fill="#6b7280">(קבצים חדשים נשמרים בתיקייה הזאת)</text>
      <text x="56" y="196" font-size="10" fill="#1e1b4b" font-weight="bold">לשונית Info / Info.plist</text>
      <text x="66" y="216" font-size="10" fill="#6b7280">הצהרת האפליקציה: שם, הרשאות, הגדרות</text>
      <rect x="310" y="56" width="245" height="196" fill="#f0fdf4" rx="5"/>
      <text x="321" y="78" font-size="11" fill="#065f46" font-weight="bold">מקומות חשובים נוספים</text>
      <text x="331" y="100" font-size="10" fill="#374151">📁 Preview Content/  ← משאבי תצוגה מקדימה</text>
      <text x="331" y="122" font-size="10" fill="#374151"><i class="fas fa-bullseye mr-1"></i> הגדרות ה-Target (אייקון הפרויקט הכחול)</text>
      <text x="331" y="142" font-size="10" fill="#6b7280">——כאן נמצאים מספר הגרסה, המערכת המינימלית והחתימה</text>
      <text x="331" y="168" font-size="10" fill="#374151"><i class="fas fa-flask mr-1"></i> MyFirstAppTests/  ← בדיקות יחידה</text>
      <text x="331" y="188" font-size="10" fill="#374151">📱 MyFirstAppUITests/ ← בדיקות ממשק</text>
      <text x="331" y="216" font-size="10" fill="#9ca3af">(תבנית הבדיקות כבר נוצרה, בשימוש בפרק 67)</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
איור 2: מבנה הפרויקט ב-Xcode שחובה על מתחילים להכיר
:::

- MyFirstAppApp.swift: נקודת הכניסה של התוכנה; ב-SwiftUI היא מכילה רק כמה שורות — "התחל, ואז הצג את המסך הראשי";
- ContentView.swift: תצוגת המסך הראשי; כל מה שאתם רואים עכשיו נמצא כאן;
- Assets.xcassets: מחסן המשאבים — כאן נשמרים האייקונים, התמונות והצבעים;
- הגדרות ה-Target: לוחצים על אייקון הפרויקט הכחול בצד שמאל כדי להיכנס; מספר הגרסה, גרסת ה-iOS המינימלית והחתימה — הכול שם. גם את שם התצוגה של האפליקציה ואת האייקון מגדירים כאן.

#### 5. טריקי יעילות ב-Xcode: חמשת "הצ׳יטים" של קיצורי המקשים למתחילים

ברגע שתשלטו באלה, תיראו "ממש מקצוענים":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">פעולה</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">קיצור מקשים</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">מה זה עושה</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">הרצה</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מהדר ומריץ</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">פתיחה/החלפה של התצוגה המקדימה בקנבס</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">המתג של "מה שרואים זה מה שמקבלים"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">עיצוב הזחות</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">סידור אוטומטי של ההזחה בקוד המסומן</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">פתיחת קובץ מהירה</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מקלידים שם קובץ והוא נפתח מיד (הכי שימושי!)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">הערה/ביטול הערה</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">הפעלה וכיבוי מהירים של קוד בזמן ניפוי שגיאות</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
קיצורי המקשים השכיחים ב-Xcode (חמישיית המתחילים)

עוד שתי הטבות נסתרות: הרצה במקביל של כמה מדמים (להריץ iPhone ו-iPad יחד ולהשוות פריסות) וספריית קטעי קוד (גררו כמה שורות קוד שכיחות אל חלונית ה-Snippets בצד ימין, ופעם הבאה הכניסו אותן בקליק אחד) — תתחילו להשתמש בכלי היעילות, והקלות תגיע מאליה.

#### 6. ניפוי שגיאות על מכשיר אמיתי: מתקינים את האפליקציה ב-iPhone שלכם

המדמה נהדר, אבל היעד האמיתי הוא מכשיר אמיתי. גם עם Apple ID חינמי אפשר לנפות שגיאות על מכשיר אמיתי:

1. חברו את ה-iPhone בכבל נתונים (או נפו שגיאות אלחוטית באותו Wi-Fi);
2. ברשימת המכשירים למעלה ב-Xcode בחרו את המכשיר שלכם; בפעם הראשונה יתבקשו להתחבר עם Apple ID והחתימה תוגדר אוטומטית;
3. ב-iPhone: [הגדרות] → [כללי] → [ניהול VPN ומכשירים] → סמכו על תעודת המפתח שלכם;
4. לחצו על ▶, והאפליקציה תותקן במכשיר האמיתי.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
שימו לב: "מגבלת שבעת הימים" של החשבון החינמי

{class="mt-1"}
אפליקציה שנחתמה עם Apple ID חינמי פגה אחרי 7 ימים (הרצה חוזרת אחת מחדשת את התוקף). זהו מנגנון נגד שימוש לרעה של אפל, ולשלב הלמידה הוא מספיק לגמרי; לחשבון מפתח בתשלום (99 דולר לשנה) אין את המגבלה הזאת — נפרט בפרק 67.
:::

#### 7. ניסיון ראשון + עזרה ראשונה לשגיאות נפוצות

פתחו את ContentView.swift, החליפו את הטקסט ב-Text("Hello, world!") בשם שלכם ולחצו על ⌘R להרצה מחדש — כעבור מספר שניות השם שלכם יופיע במדמה. מזל טוב: השלמתם את מחזור "עריכת קוד → הידור → התקנה → הרצה" המלא הראשון שלכם.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">תסמין השגיאה</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">סיבה נפוצה</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">התרופה</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">שגיאת Signing</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">לא נבחר Team או תעודה שפג תוקפה</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ב-Target → Signing סמנו את החשבון שלכם; בחשבון חינמי פשוט מריצים שוב</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מסך שחור במדמה / הוא לא נפתח</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">תמונת המערכת פגומה</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">בתפריט Device → Erase All Content; או מוחקים את המדמה ומוסיפים אותו מחדש</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">הורדת Xcode איטית / ההתקנה נכשלת</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">תנודות ברשת של ה-App Store</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מנסים בשעה אחרת; או מורידים חבילת .xip להתקנה אופליין מאתר המפתחים של אפל</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
טבלת עזרה ראשונה לשגיאות סביבה למתחילים

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
הידיים על ההגה: השלימו את רשימת "טקס הפיתוח" שלכם

{class="mt-1"}
① התקינו את Xcode והריצו בהצלחה את המדמה; ② הריצו את האפליקציה שלכם פעם אחת על מכשיר אמיתי ושמרו צילום מסך למזכרת; ③ החליפו את טקסט ה-Hello בשם שלכם; ④ בהגדרות ה-Target שנו את שם התצוגה של האפליקציה ל"האפליקציה הראשונה שלי". אחרי ארבעת הצעדים האלה אתם כבר אנשים עם יצירה משלכם.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
סיכום הפרק

- מחסום קשיח: מק + Xcode; אין מק? למדו את השפה קודם ב-Swift Playgrounds ב-iPad
- מתקינים את Xcode מה-App Store; גרסה חדשה דורשת מערכת חדשה — אל תדחו עדכונים
- חמשת המרכיבים ביצירת פרויקט חדש: שם, Team, מזהה ארגון, SwiftUI, Swift
- כלל אצבע לפרויקט: כל הקוד בתיקיית MyFirstApp/; הגדרות ה-Target מנהלות גרסה וחתימה
- ניפוי שגיאות על מכשיר אמיתי עם Apple ID חינמי כולל מגבלת חתימה של 7 ימים; לחשבון בתשלום אין מגבלה כזאת
- השגרה היומיומית של המפתח = עריכת קוד → ⌘R → בדיקת התוצאה, שוב ושוב
:::
