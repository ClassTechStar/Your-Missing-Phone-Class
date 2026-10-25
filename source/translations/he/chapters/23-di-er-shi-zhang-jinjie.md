---
id: di-er-shi-zhang-jinjie
num: 20
part: jin-jie-pian
nav: פרק 20: מצב מפתחים והרשאות מתקדמות
toc: default
kind: supplement
---

### פרק 20: מצב מפתח והרשאות מתקדמות

{class="chapter-intro mb-4"}
פרק זה מיועד למשתמשים שרוצים לחקור לעומק את "הפונקציות הנסתרות" של הטלפון. מצב מפתח, הרשאות Root, נעילת BL... מושגים שנשמעים גיקיים, אבל למעשה לא רחוקים מהמשתמש הרגיל.

#### אחת, מצב מפתח: פתיחת הגדרות נסתרות

אנדרואיד

##### : כנס להגדרות &gt; אודות הטלפון &gt; לחץ 7 פעמים על "מספר גרסה", עד שמופיע "אתה עכשיו במצב מפתח".

- <strong>HarmonyOS</strong>: הגדרות &gt; אודות הטלפון &gt; לחץ 7 פעמים על "גרסת HarmonyOS".
- <strong>iOS</strong>: משתמשים רגילים לא יכולים להפעיל מצב מפתח מלא, דורש חשבון Apple Developer בתשלום.
- <strong>פונקציות נפוצות:</strong>איתור באגים USB

##### סקירת פונקציות נפוצות:

- <strong>USB Debugging</strong>:חיבור למחשב לפעולות מתקדמות (ADB). ראה "ADB".
- <strong>הגבלת תהליכי רקע</strong>:הצגת מגע (נקודה), למדריכים.

##### קשור לביצועים וחלקות:

- <strong>מהירות אנימציה (חלון/מעבר/תוכנית)</strong>:שלוש אפשרויות אלו שולטות במשך אנימציית פתיחת App ומעבר בין דפים. ברירת המחדל היא 1x, הגדרה ל-0.5x תגרום לטלפון ל"היראות" מהיר יותר (בפועל מהירות התוכנית לא השתנתה, רק האנימציה מהירה יותר), וכיבוי משמעו קפיצה ללא אנימציה. רוב הגיקים מגדירים 0.5x - שומר על תחושת מעבר ונראה מהיר; כיבוי מלא יגרום לתחושה קשיחה, ועלול להסתיר קיתקון אמיתי, כך שתחשוב בטעות שהכל "זורם".
- <strong>Force GPU Rendering</strong>:2D דרך GPU. בישנים/לא מאופטמם = זרימה, אך עומס וסוללה. מודרני = השפעה מוגבלת, היסטורי. השאר ברירת מחדל.
- <strong>Profile GPU Rendering</strong>:מציג גרף עמודות בזמן אמת על המסך לכל פריים, קו ירוק מייצג 16.6ms (סף זמן פריים של 60fps). עמודה מעל הקו הירוק = פריים מושמט. זהו כלי למפתחים לאבחון קיתקון, אך גם משתמש רגיל יכול להשתמש בו כדי להשוות איזה App מותאם גרוע - למשל App שבגלילה העמודות מטפסות מעל הקו האדום, זה בעצם האשם.

##### קשור לרקע וחיי סוללה:

- <strong>אילוץ רינדור GPU</strong>:ניתן להגדיר "הגבלה סטנדרטית" "מקסימום תהליך 1" "מקסימום 2 תהליכים" וכו'. נראה שהגבלת תהליכי רקע חוסכת סוללה, אך בפועל ניהול הרקע המובנה של Android כבר טוב, והגבלה כפויה תגרום לטעינה תכופה מחדש של App (הפעלה קרה דווקא צורכת יותר ופוגעת בחוויה). אפשרות זו מתאימה יותר לדיבוג, לא מומלץ למשתמש רגיל להפעיל לטווח ארוך, השאר "הגבלה סטנדרטית".
- <strong>אל תשמור פעילויות</strong>:הורס בכל יציאה. לא מומלץ, מסך לבן, לבדיקות בלבד.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>הערות חשובות

{class="mt-1"}
Bootloader הוא התוכנית שטוענת את מערכת ההפעלה באתחול הטלפון. נעילת BL היא מנעול שהיצרנים מוסיפים מטעמי אבטחה, למנוע מהמשתמש לצרוב מערכות לא רשמיות.
:::

#### ב', OEM Unlock: "מתג צריבה"

ב-Developer Options יש "OEM Unlock". לא משחרר BL, אלא "רישיון": בלעדיו, fastboot/כלי יצרן נדחים.

- <strong>תפקיד המתג</strong>:"אני מוותר על אחריות". סגור = כל פקודה נדחית.
- <strong>קשר לנעילת BL</strong>:OEM = "בקשה", BL = "ביצוע". הראשון בהגדרות, השני אתר + fastboot ( <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing unlock</code>), שניהם חיוניים.
- <strong>האם שחזור להגדרות יצרן יאפס</strong>:כן. OEM חוזר לסגור אחרי איפוס, BL נשאר פתוח - דורש <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing lock</code> כדי לנעול מחדש.
- <strong>מתי כדאי להפעיל</strong>:אלא אם צריבה/Root, השאר סגור. עצמאי מ-"USB Debugging".

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>ידיעון: למה יצרנים מגדירים את המתג הזה

{class="mt-1"}
בישנים לא היה, תוכנה זדונית יכלה לצרוב. Google דרש "OEM Unlock" כ"הסכמה". לכן גם BL פתוח, אם OEM סגור, צריבה נכשלת.
:::

#### ג', BL Lock: הדלת הראשונה

הגנת אבטחה

##### : מונע צריבת תוכנות זדוניות למערכת.

- <strong>הגנה מפני גניבה</strong>: גם אם הטלפון נצרב, בלי סיסמת החשבון המקורי לא ניתן להשתמש.
- <strong>הגבלת אחריות</strong>: פתיחת BL בדרך כלל אומרת אובדן אחריות רשמית.
- <strong>מדיניות נעילת BL לפי מותג:</strong>Xiaomi

##### : ניתן לפתוח, דורש חשבון ותקופת המתנה (7-30 יום).

- <strong>Huawei</strong>: אחרי 2018 הפסיקו לספק קוד פתיחה, כמעט בלתי אפשרי לפתוח רשמית.
- <strong>OnePlus</strong>: ניתן לפתוח, יחסית מקל.
- <strong>OPPO/vivo</strong>: חלק מהדגמים ניתנים לפתיחה, דורש בקשה.
- <strong>Samsung</strong>: ניתן לפתוח, אבל יפעיל Knox fuse, אובדן Samsung Pay וכו'.
- <strong>Apple</strong>: למכשירי iOS אין מושג BL lock מסורתי, אבל יש מנגנוני אבטחה דומים.
- <strong>אנדרואיד</strong>הרשאות Root שקולות ל-Administrator ב-Windows, ההרשאה הגבוהה ביותר במערכת אנדרואיד. אחרי השגת Root, ניתן לשנות קבצי מערכת, להסיר אפליקציות מובנות, להשתמש באפליקציות מתקדמות הדורשות Root.

#### ד. פקודות ADB שימושיות: שליטה בטלפון דרך המחשב

ADB = Android Debug Bridge, כלי שורת פקודה רשמי של Google המאפשר למחשב לתקשר עם טלפון Android דרך USB או Wi-Fi. אינו דורש Root, מספיק ש"USB Debugging" מופעל בטלפון. אפשר לחשוב עליו כ"שלט" שמאפשר למחשב לשלוח פקודות לטלפון - צריבת ROM, התקנת App, העברת קבצים, בדיקת לוגים - הכל דרכו.

##### איך מתחברים דרך USB:

1. טלפון: Developer Options &gt; "USB Debugging".
2. מחשב: Platform Tools ( <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb</code> . אותה שאלה, מוסברת אחרת לתלמיד ולהורה; המלצות שונות לתושב עיר ולתושב עיירה. בלי רקע, AI יכול לתת רק תשובות "המכנה המשותף הגדול ביותר", לרוב לא משמעותיות. <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot</code> שני קבצי הפעלה), חלץ לכל תיקייה.
3. חבר כבל, "אפשר USB Debugging?" &gt; "תמיד" &gt; אישור.
4. ב-cmd/PowerShell: <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code>, אם הפלט דומה ל- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">List of devices attached / xxxxxxxx device</code>, זה אומר שהחיבור הצליח.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>אל תתעלם מדרייבר וחלון הרשאה

{class="mt-1"}
משתמשי Windows אם <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code> "unauthorized" או שהמכשיר לא מופיע כלל, כנראה הדרייבר לא מותקן או שכחת ללחוץ "אפשר" בטלפון. Samsung/Xiaomi ומותגים אחרים מספקים "USB Driver" או "Phone Assistant"; Mac ו-Linux בדרך כלל לא דורשים דרייבר. אם חלון האישור נעלם, נתק וחבר מחדש את הכבל.
:::

##### פקודות ADB נפוצות:

- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb install app.apk</code>: התקן APK מהמחשב לטלפון (<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-r</code> מציין התקנה על-גבי תוך שמירת נתונים;<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code> התקן ל-SD card).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb uninstall com.xxx.xxx</code>: הסר App לפי שם חבילה.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb push PC /sdcard/target</code>: דחוף קובץ מהמחשב לטלפון.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb pull /sdcard/file PC</code>:מהטלפון למחשב (מהיר מ-WeChat).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell</code>:Linux Shell, בצע <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls</code>ו<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm</code>ו<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">am</code> ופקודות נוספות.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot bootloader</code>:הפעלה ל-Fastboot (צריבה).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot recovery</code>: הפעל מחדש למצב Recovery.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages</code>:רשימת חבילות App. הוסף <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code> לצפייה ב-App מערכת בלבד, הוסף <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-3</code> לצפייה ב-App צד שלישי בלבד.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 package</code>:הסרת App מובנה, בלי Root.

##### הסרת App מובנית ללא Root בפועל:

זוהי אחת מהפונקציות השימושיות ביותר של ADB: באמצעות <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code> מסיר App מובנה ל"משתמש נוכחי", בלי Root, ללא שינוי מחיצה. ה-App "נעלם" אך נשאר, חוזר אחרי איפוס.

1. תחילה השתמש ב- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages -s</code> רשימת App מערכת, מצא חבילה. דפדפן Xiaomi: <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.browser</code>, Huawei AppGallery הוא <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.vmall.client</code>.
2. לא בטוח? במחשב, <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages | findstr keyword</code> או "Package Viewer" בטלפון.
3. בצע הסרה:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 package</code>, למשל <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 com.android.browser</code>. מחזיר <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Success</code> מציין הצלחה.
4. שחזור? 1) איפוס; 2) התקן:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell cmd package install-existing package</code>.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>אל תמחק חבילות ליבה של המערכת!

{class="mt-1"}
"pm uninstall" בלי Root, אך מחיקת App קריטי ( <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.systemui</code> סרגל מצב,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.phone</code> טלפון,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.settings</code> ) = קריסה, מסך שחור. Google לפני מחיקה. מעט בכל פעם.
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>ידיעון: מה המשמעות של --user 0

{class="mt-1"}
Android 4.2+ רב-משתמש, ID (בעלים 0, נוסף 10+).<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">--user 0</code> "הסרה רק לבעלים הנוכחי" - קובץ ה-APK במחיצת המערכת עדיין קיים, פשוט לא מוצג לבעלים. לכן אינו דורש Root - לא נגע בקבצי מערכת, רק שינה "הגדרות משתמש". זה ההבדל מ-Root: Root מוחק באמת מהמערכת, כל המשתמשים לא רואים; ADB רק "מסתיר למשתמש הנוכחי".
:::

#### ה. הרשאת Root: "מנהל-העל" של Android

Root מקביל לסופר-יוזר ב-Linux (שליטה מלאה ב-/ , קריאה/כתיבה של כל קובץ), ההרשאה הגבוהה ב-Android. שונה מ-Administrator ב-Windows: Windows מגביל את המנהל (ההרשאה הגבוהה באמת היא TrustedInstaller), גם Administrator לא יכול לבצע ישירות כמו root ב-Linux <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">sudo rm -rf /*</code>. עם Root: שינוי מערכת, הסרת App, App מתקדמים.

##### שימוש באפליקציות פונקציה מתקדמות (כמו Titanium Backup, Greenify).

- שינוי ממשק ופונקציות מערכת.
- התקנת Recovery צד שלישי ו-ROM מותאם אישית.
- סיכוני Root:
- אובדן אחריות

##### : רוב היצרנים לא מכסים טלפונים שעברו Root.

- <strong>תקלה בפונקציות תשלום</strong>: אפליקציות זדוניות עשויות להשיג הרשאות Root, תוצאות חמורות.
- <strong>אי יציבות מערכת</strong>: פעולה שגויה עשויה לגרום לקריסת מערכת.
- <strong>אפליקציות בנק לא עובדות</strong>: הרבה אפליקציות בנק ותשלום מזהות Root ומסרבות לרוץ.
- <strong>כשל בעדכון OTA</strong>: עשוי לא לקבל עדכוני מערכת רשמיים.
- <strong>אזהרה חמורה</strong>פעולת Root כרוכה בסיכון, עשויה לגרום ל-bricking של הטלפון (לא נדלק). אם אתה מתחיל, מומלץ קודם ללמוד היטב, ולוודא שיש גיבוי מלא. לפני פעולה קרא את המדריך בעיון, אשר את דגם המכשיר וגרסת המערכת.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>ארבע, המלצות למשתמשים רגילים

{class="mt-1"}
מצב מפתח
:::

#### ו', SafetyNet/Play Integrity: למה Root = בנק לא עובד

Root משתמשים רבים חוו את הרגע: מתקינים מודולים בהתלהבות, פותחים App בנק - "המכשיר שלך לא בטוח, לא ניתן להשתמש", Google Pay לא עובד, אפילו Netflix מסרב ל-HD. מאחורי זה שני מנגנוני אימות שלמות: SafetyNet הישן ו-Play Integrity API החדש.

##### SafetyNet / Play Integrity:

- <strong>SafetyNet Attestation (ישן, 2017)</strong>:API ישן של Google לבדיקת שלמות מכשיר, App שואל את שרת Google "האם המכשיר עבר CTS ובמצב רשמי ללא שינוי". התוצאה מתחלקת ל-Basic (בסיסי) ו-Strong (חזק, דורש מפתח חומרה). Google הודיע ש-SafetyNet יושבת בהדרגה אחרי 2024.
- <strong>Play Integrity API (חדש, 2022)</strong>:תחליף, קפדני יותר. מכשיר + App + חשבון. App חדשים יעברו.
- <strong>מי משתמש</strong>:בנק, תשלום (Google Pay, Alipay, WeChat), Netflix HD, משחקים, MDM.

##### Play Integrity 3 רמות:

- <strong>MEETS_DEVICE_INTEGRITY</strong>:Android רשמי, BL נעול, ללא Root, CTS. בנק/תשלום עובד.
- <strong>MEETS_BASIC_INTEGRITY</strong>:בסיסי, אולי חריג. Netflix מוגבל, בנק עלול לדחות.
- <strong>MEETS_STRONG_INTEGRITY</strong>:גבוה, מפתח חומרה (Titan M), רוב המכשירים לא מגיעים.
- <strong>ללא תגית (NO_INTEGRITY)</strong>:Root/BL פתוח/ROM/אמולטור, בנק דוחה.

##### למה Root = App נכשל:

App שולח בקשה לשרת Google דרך Play Integrity API, Google בודק מספר מדדים - מצב BL, האם מחיצת מערכת שונתה, האם קיים su, האם SELinux במצב permissive. כל חריגה תגרום לירידת רמת האימות או החזרת ערך ריק, App בנק רואה "מכשיר לא בטוח" ומסרב.

##### הסתרה: Magisk Hide / Shamiko / Zygisk:

כדי להשתמש ב-Root ובבנק, פיתחו "הסתרת Root". עיקרון: להראות "נורמלי".

- <strong>Magisk</strong>:Systemless Root - לא משנה מחיצה, מעלה. OTA נקי, בסיס להסתרה. דורש BL פתוח.
- <strong>Magisk Hide (הופסק)</strong>:מודול ישן, מסתיר Root. 2021 הוסר, Google משדרג, "משחק חתול ועכבר".
- <strong>Zygisk</strong>:Magisk 24.0+, כמו Riru, Zygote, חבוי יותר. תנאי להסתרה.
- <strong>Shamiko</strong>:מודול מרכזי, עם Zygisk, "רשימה לבנה", מסתיר Root/Magisk/BL. דרך LSPosed/GitHub.
- <strong>Play Integrity Fix(osm0sis)</strong>:מודול ל-Play Integrity, משנה fingerprint, Google "רואה" רשמי.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>משחק החתול והעכבר לעולם לא יסתיים

{class="mt-1"}
Google מעדכן כללים מעת לעת, ויצרני App עוקבים ומשדרגים Play Integrity. מה שעובד היום עשוי להיחשף מחר. אם אתה תלוי לחלוטין ב-App בנק/תשלום, הבחירה הבטוחה: אל תעשה Root, אל תפתח BL. שיטות הסתרה מתאימות יותר ל"מכשיר ראשי בלי Root + מכשיר גיבוי עם Root".
:::

#### ז. עצות למשתמשים רגילים

- <strong>נעילת BL</strong>:אפשר לפתוח, אנימציה/GPU, אל תשנה מה שלא מבין.
- <strong>פתיחת OEM ונעילת BL</strong>:אם לא צריבה/Root, שניהם סגורים.
- <strong>ADB</strong>:כלי חזק בלי Root - כמו <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code> הסר App. בדוק חבילה לפני מחיקה.
- <strong>Root</strong>:לא מומלץ Root, סיכון &gt; תועלת. חלופות: ADB, Shizuku.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>לחץ 7 פעמים על "מספר גרסה", עד שמופיע שמצב מפתח הופעל.

{class="list-decimal pl-6 mt-1 space-y-1"}
1. חזור להגדרות, מצא "אפשרויות מפתח" (בדרך כלל בתחתית ההגדרות או ב"מערכת").
2. מצא "Window animation scale", "Transition animation scale", "Animator duration scale", קבע את כולם ל-0.5x או כבה.
3. הרגש אם הטלפון מהיר יותר.
4. נספח לפרק 20:Termux — סביבת טרמינל לינוקס ניידת על מכשירי Android
5. אם נראה לך שמצב מפתח עדיין לא מספיק "הארדקור", ואתה רוצה לחוות שורת פקודה מלאה של לינוקס על הטלפון שלך, אז Termux מיועד בדיוק עבורך. הוא אינו דורש הרשאות root, ויכול להפוך טלפון Android רגיל לתחנת עבודת לינוקס ניידת, והוא כלי רב עוצמה למשתמשים מתקדמים החוקרים פיתוח ותפעול במובייל.
:::
