---
id: di-liu-shi-qi-zhang
num: 67
part: ios-kai-fa-pian
nav: פרק 67: ליטוש ופרסום – עלייה ל-App Store
toc: default
kind: chapter
---

### פרק 67: ליטוש והוצאה לאור — בדיקות, ניפוי באגים ועלייה ל-App Store

{class="chapter-intro mb-4"}
האפליקציה נבנתה — ומה עכשיו? הפרק הזה עונה על שלושה עניינים בדרך מ"זה רץ" אל "זה מוכן למסירה": איך לנפות באגים ביעילות, איך לכתוב בדיקות שמונעות נסיגות, ואיך להעלות את האפליקציה ל-App Store כדי שכל העולם יוכל להוריד. העלייה לחנות היא לא רק טקס — זהו קו הפרדה בין יצירה למוצר.

#### 1. שלושת כלי הניפוי: print, נקודות עצירה ותצוגות מקדימות

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">כלי</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">מה הוא עושה</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">איך משתמשים</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">print + הקונסולה</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">צפייה בלוגי הריצה</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">בקוד כותבים print("ערך=\(x)") ורואים את הפלט בקונסולה שבתחתית Xcode</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ניפוי עם נקודות עצירה</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">עוצרים את התוכנית בשורה מסוימת ורואים ערכי משתנים</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">לוחצים פעם אחת ליד מספר השורה ומופיע סימן כחול; הריצה נעצרת שם ואפשר להתקדם צעד-צעד</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">תצוגה מקדימה של SwiftUI + מנפה השגיאות</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">צפייה בזמן אמת בממשק ובהיררכיית התצוגות</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">בד ה-#Preview + בודק ה-View Hierarchy בזמן ריצה</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
שלושת כלי הניפוי

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
טיפ: איך קוראים קריסה?

{class="mt-1"}
כש-Swift קורס, הקונסולה מדפיסה "Fatal error" ואת הסיבה, ו-Xcode עוצר בשורה הבעייתית ומדגיש אותה. היסטוריית קריסות ממכשיר אמיתי אפשר לראות ב-Xcode → Window → Organizer → Crashes (נדרש חשבון בתשלום). בחיפוש, תעדפו את מילות המפתח "המשפט הראשון של סיבת השגיאה + swiftui" — רק שאלה מדויקת מניבה תשובה מדויקת.
:::

#### 2. בדיקות: ביטוח לקוד

בדיקה ידנית לא אמינה — מתקנים פיצ׳ר אחד ואחר שובר בשקט. בדיקות הן גם "תרופת החרטה" וגם "שריון חץ". ב-iOS משתמשים בפריימוורק XCTest, עם שני סוגים:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">רמה</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">מה נבדק</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Target</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">מהירות</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">בדיקות יחידה</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">לוגיקה טהורה (חישובים, בדיקות תקינות)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppTests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">שניות</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">בדיקות UI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">התנהגות ממשק אמיתית</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppUITests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">דקות</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">בדיקה ידנית</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">תחושות וחוויה של אדם אמיתי</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">תמיד נדרשת</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
רמות הבדיקה ב-iOS (בפרויקט התבנית כבר מוגדרים שני Test Target)

::: div .code-block
:::inline div .code-head
<span>SWIFT · דוגמת בדיקת יחידה</span><span class="dots">···</span>
:::

```
import XCTest

// לחלץ את הלוגיקה של "המרת טקסט הסכום למספר" לפונקציה טהורה
func parseAmount(_ input: String) -> Double? {
    guard let v = Double(input.trimmingCharacters(in: .whitespaces)),
          v > 0 else { return nil }
    return v
}

final class AmountTests: XCTestCase {
    func testEmptyInputReturnsNil() {
        XCTAssertNil(parseAmount(""))
    }
    func testNegativeReturnsNil() {
        XCTAssertNil(parseAmount("-5"))
    }
    func testNormalValueParses() {
        XCTAssertEqual(parseAmount("12.5"), 12.5)
    }
}
```
:::

הרצת בדיקות: ⌘U. רק אחרי שהכל ירוק שווה לשנות קוד — אז יש לכם רגליים על הקרקע. את בדיקות התקינות של הסכומים ואת חישובי הסיכום בספר החשבונות כדאי להצמיד לבדיקות יחידה.

#### 3. חתימה ואריזה: נותנים לאפליקציה "חותמת"

כל אפליקציית iOS חייבת להיות חתומה כדי להתקין — זה מוכיח ש"החבילה הזאת יצאה ממך ולא זויפה". היררכיית ההסתמכות:

- שלב הלמידה: Apple ID חינמי + חתימה אוטומטית של Xcode (Personal Team) — עובד על מכשיר אמיתי, עם חידוש אחת ל-7 ימים;
- שלב ההפצה: חשבון מפתח בתשלום (99 דולר לשנה) מנפיק תעודות וקובצי פרופיל — רק כך אפשר לעלות לחנות ולהתקין לטווח ארוך.

אריזה: בתפריט Xcode בוחרים Product → Archive (ארכיון); אחרי הבנייה פותחים את Organizer, בוחרים Distribute App → App Store Connect → העלאה. חשוב: לארכיון חייבים לבחור Generic iOS Device כיעד (לא סימולטור) — זה השלב שמתחילים שוכחים הכי הרבה.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
אזהרה: תעודה שאבדה = הפסקת עדכונים

{class="mt-1"}
אם תעודת החתימה והמפתח הפרטי אבדו, לא תוכלו לשלוח עוד עדכונים לאפליקציה הישנה — המשתמשים יוכלו רק להתקין אפליקציה "חדשה לגמרי". גבו את התעודה כראוי (ייצוא .p12 מחולץ המפתחות) ושמרו היטב על הסיסמה. למזלכם, אפל מספקת "חתימה אוטומטית" וניהול תעודות בענן (סמנו Automatically manage signing ב-Xcode) — זה חוסך את רוב המלכודות של העבודה הידנית.
:::

#### 4. תהליך העלאה מלא ל-App Store

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> רישום חשבון מפתח</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> הכנת חומרים לחנות</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> העלאת חבילת הבנייה</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> מילוי פרטי פרטיות ובדיקה</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> בדיקת Apple (1-7 ימים)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> פרסום</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
איור 5: ששת שלבי העלייה ל-App Store
:::

- הרשמה: developer.apple.com, חשבון אישי ב-99 דולר לשנה;
- חומרים: אייקון (1024×1024, בלי פינות מעוגלות — אפל קובעת את העיגול בעצמה), צילומי מסך (בגדלים השונים של iPhone), תיאור וקישור למדיניות פרטיות;
- שאלון פרטיות: מדווחים ביושר אילו נתונים נאספים — ספר חשבונות שלא מתחבר לרשת יכול לסמן "לא אוספים דבר";
- ביקורת: הגשה ראשונה כרוכה בהמתנה של 1–7 ימים בדרך כלל; אם נדחיתם, תקנו סעיף-סעיף לפי "הערות הביקורת" — סיבות הדחייה של אפל בדרך כלל כתובות במפורש מאוד, פשוט בצעו לפיהן;
- TestFlight: לפני העלייה לחנות שלחו קודם גרסת בטא לחברים (עד 10,000 איש), אספו סבב משוב ורק אז הגישו רשמית — זה נראה מקצועי בטירוף.

#### 5. חומרי חנות: הרושם הראשוני הוא ההורדות

עמוד החנות הוא חלון הראווה שהמשתמש רואה כשהוא "מסתובב בשוק". שלושה חומרים קובעים את הרושם הראשוני:

- אייקון: 1024×1024, אל תסתפקו בצילום מסך. אין לכם כישורי עיצוב? צרו גרפיקה פשוטה עם כלי AI; האייקון עובר את המבחן רק אם הוא ניכר מבט אחד גם אחרי כיווץ על שולחן העבודה;
- צילומי מסך: לפחות 2 סטים (בגדלים הנפוצים של iPhone), שמציגים את תרחישי הפונקציונליות המרכזיים; לכל צילום מוסיפים משפט אחד בשפת בני אדם ("רושמים חשבון בשנייה" טוב פי עשרה מ"פתרון יעיל לניהול חשבונות");
- תיאור: המשפט הראשון מסביר בבירור "מה זה + למי זה מיועד"; אל תערמו "הכי מקצועי, הכי חזק" — כנות משפיעה יותר מהגזמה.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
הידיים על ההגה: "מוסרים" את ספר החשבונות פעם אחת

#### 6. רשימה קצרה: דיווח קריסות ואופטימיזציית ביצועים

לפני שהאפליקציה עולה לחנות, שווה להשקיע חצי שעה בכל אחד משני הדברים האלה:

##### 1. ניטור קריסות

זה שלא קרס אצלכם בבדיקות לא אומר שלא יקרוס בטלפון של המשתמשים. אפל מספקת דוחות קריסה חינמיים ב-Xcode Organizer (בחשבון בתשלום אפשר לראות לוגים ממכשירים אמיתיים); פתרון נוח עוד יותר הוא שילוב SDK חיצוני (כמו Firebase Crashlytics). העלייה לחנות בלי ניטור קריסות זה כמו לנהוג בעיניים עצומות.

##### 2. ארבעה סעיפים לבדיקת ביצועים עצמית

1. רשימות עם LazyVStack / List: אל תסדרו רשימה ארוכה ב-VStack רגיל — טעינה עצלה היא השיעור הראשון בביצועים;
2. אל תציפו בתמונות מקור בגודל מלא: השתמשו ב-AsyncImage (תמונה מרוחקת) ובמטמון המערכת — תמונת מקור של 5MB מספיקה כדי לחנוק מכשיר ישן;
3. אל תעשו עבודה כבדה בת׳רד הראשי: רשת, קבצים גדולים — הכל דרך async/await;
4. מדדו עם Instruments: מנתח הביצועים המובנה ב-Xcode (Time Profiler, בדיקת דליפות זיכרון) — קודם מודדים, רק אז מייעלים; אל תסמכו על תחושת בטן.

{class="mt-1"}
① הוסיפו 3 בדיקות יחידה ללוגיקה כמו parseAmount (מריצים עם ⌘U עד לירוק); ② תפסו בעצמכם עם נקודת עצירה קריסה שיצרתם במו ידיכם ותקנו אותה; ③ ארזו חבילה עם Product → Archive והזמינו חברים לבטא דרך TestFlight; ④ אם נשאר לכם כוח — רשמו חשבון מפתח והגישו בפועל את ספר החשבונות לחנות. את שלושת הצעדים הראשונים אפשר לסיים עוד הלילה.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
סיכום הפרק

- שלושת כלי הניפוי: לוג print, נקודות עצירה, תצוגה מקדימה של SwiftUI ובודק התצוגות
- XCTest: בדיקות יחידה (⌘U) + בדיקות UI + בדיקה ידנית — התבנית כבר מוגדרת מראש
- חתימה: חשבון חינמי עם חתימה אוטומטית (חידוש כל 7 ימים); רק חשבון בתשלום מאפשר הפצה
- אריזה: Generic iOS Device + Archive + Distribute; חובה לגבות את התעודה
- שישה שלבי עלייה לחנות: הרשמה → חומרים → העלאה → שאלון פרטיות → ביקורת → פרסום; בטא קודם עם TestFlight
:::
