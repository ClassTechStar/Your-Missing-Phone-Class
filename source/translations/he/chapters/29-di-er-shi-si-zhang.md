---
id: di-er-shi-si-zhang
num: 24
part: chao-yue-pian
nav: פרק 24: הרשאות Root ונעילת ה-Bootloader לעומק
toc: default
kind: chapter
---

### פרק 24: ניתוח מעמיק של הרשאות Root ונעילת BL

{class="chapter-intro mb-4"}
פרק זה הוא הרחבה מעמיקה של תוכן פרק 20, מתאים למשתמשים שרוצים באמת להבין את מנגנוני השכבה הנמוכה של הטלפון, ואפילו לנסות להתקין ROM. שים לב, פעולות אלה כרוכות בסיכון מסוים, אנא נהג בזהירות.

#### 1. הבנה מעמיקה של Bootloader

אימות חתימה

##### : נעילת BL מאמתת את החתימה הדיגיטלית של תמונת האתחול, רק מערכת חתומה על ידי היצרן יכולה לעלות.

- <strong>מניעת ירידת גרסה</strong>: מונעת מהמשתמש להתקין גרסת מערכת ישנה כדי לנצל פרצות ידועות.
- <strong>הגנה על נתונים</strong>: גם אם מותקנת מערכת חדשה, ללא סיסמת החשבון המקורית לא ניתן לגשת לנתוני המשתמש.
- <strong>2. תהליך מפורט לפתיחת נעילת BL (דוגמת Xiaomi)</strong>בקשת הרשאת פתיחה

##### 🔐 אחסון ואימות ברמת חומרה

BL (Locked/Unlocked) ומפתח יצרן, בחומרה מוגנת (devinfo/eFuse/RPMB). בכל הפעלה, Bootloader קורא ומחליט אם לבצע אימות חתימה.

##### 🔏 אימות חתימה דיגיטלית

יצרן חותם במפתח פרטי. בהפעלה, Bootloader מאמת עם מפתח ציבורי (boot.img, recovery.img). אופן:

1. חישוב מחדש של ערך hash לתמונת מערכת.
2. פענוח חתימה עם מפתח ציבורי = hash.
3. השוואת hash, זהה = עובר. מבטיח שלמות.

##### 🔗 שרשרת אתחול מאובטח

BL = החוליה הראשונה. אימות → טעינת kernel → שרשרת אמון.

##### 📊 נעילה מול פתיחה: ההשפעה הדו-כיוונית של נעילת BL

להבנת BL, טבלת השוואה ב-5 ממדים:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 dark:border-gray-600 text-sm">
                            <thead>
                                <tr class="bg-gray-100 dark:bg-gray-800">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">תפקיד מרכזי</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">מצב נעול (ברירת מחדל)</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">מצב לאחר פתיחה</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">אבטחת מערכת</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מניעת צריבת ROM לא רשמי, הגנת שלמות<br><span class="text-emerald-600 dark:text-emerald-400">✅ בטוח: רק רשמי, נגד חבלה</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ פחות בטוח: ROM צד ג', אימות מבוטל, Root = חבלה</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">יציבות מערכת</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מערכת רשמי, יציב<br><span class="text-emerald-600 dark:text-emerald-400">✅ יציב: רשמי, OTA</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ סיכון: ROM צד ג', קריסה/brick, חומרה, OTA נכשל</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">זכויות אחריות</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BL נעול = אחריות<br><span class="text-emerald-600 dark:text-emerald-400">✅ אחריות: רשמי</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ אחריות בוטלה: BL = ויתור, גם נעילה מחדש ניתן לזהות</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">אבטחת נתונים</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">פתיחה = מחיקת נתונים<br><span class="text-emerald-600 dark:text-emerald-400">✅ בטוח: BL מגביל חבלה</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ סיכון: מחיקה, הצפנה, איבוד = חילוץ</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">מגבלות פונקציה</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">תשלום/בנק עובד<br><span class="text-emerald-600 dark:text-emerald-400">✅ פונקציונליות מלאה: כל הפונקציות הרשמיות פעילות</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ מוגבל: Google Pay/בנק דוחים, DRM יורד</span></td>
                                </tr>
                            </tbody>
                        </table>
```
:::

#### 2. תהליך מפורט לפתיחת נעילת BL (דוגמת Xiaomi)

1. <strong>קישור חשבון</strong>: בהגדרות הטלפון קשר חשבון Xiaomi.
2. <strong>תקופת המתנה</strong>: בהתאם לרמת החשבון, יש להמתין 7-30 ימים.
3. <strong>פעולת פתיחה</strong>: השתמש בכלי פתיחת הנעילה של Xiaomi בחיבור למחשב לפתיחת הנעילה.
4. <strong>שלוש. אפשרויות Root שונות</strong>Magisk

#### שלוש. אפשרויות Root שונות

- <strong>Magisk</strong>: פתרון Root מבוסס-ליבה, עמוק יותר, הסתרה טובה יותר.
- <strong>SuperSU</strong>: פתרון Root ותיק, הפסיק להתעדכן.
- <strong>ארבע. מבוא להתקנת ROM</strong>הבהוב (התקנת ROM) פירושו התקנת מערכת הפעלה חדשה בטלפון. סוגי הבהוב נפוצים:

#### ארבע. מבוא להתקנת ROM

: התקנת מערכת רשמית, להצלת מכשיר או הורדת גרסה.

- <strong>הבהוב Recovery צד-שלישי</strong>: כמו TWRP, לגיבוי ושחזור, הבהוב ROM צד-שלישי.
- <strong>הבהוב ROM צד-שלישי</strong>: כמו LineageOS, Pixel Experience, לחוות מערכות שונות.
- <strong>אזהרה חשובה</strong>הבהוב כרוך בסיכון, יש לפעול בזהירות. עלול לגרום ל:

#### ה. Samsung Knox: המחיר הבלתי-הפיך של פתיחת BL

Samsung: "נתיק" ייחודי:<strong>Samsung: Knox נשרף, Samsung Pay אובד, נתונים נמחקים, אחריות.</strong>. בפרט:

- <strong>הנתיך חד-פעמי</strong>:בתוך הטלפון יש נתיך eFuse, ברגע שמזוהה ש-BL שוחרר הנתיך נשרף לצמיתות, לא ניתן לשחזר.
- <strong>פונקציות מושפעות</strong>:Samsung Pay (כרטיס אוטובוס/בנק), תיקיית Knox מאובטחת, ניהול MDM ארגוני, אפליקציות ביטוח בריאות - כולם יפסיקו לעבוד.
- <strong>מחיקת נתונים בכפייה</strong>:לאחר הפעלת הנתיק הטלפון יבצע איפוס יצרן, כל הנתונים המקומיים יימחקו (נתוני ענן לא מושפעים).
- <strong>השפעה על אחריות</strong>:Huawei מצהירה רשמית שלאחר נתיק Knox אין אחריות.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>חשבו פעמיים לפני שתפעלו

{class="mt-1"}
הנתיך של Samsung Knox הוא<strong>בלתי הפיך</strong>לאחר ההפעלה לא ניתן לחזור למצב יצרן. אם רק רצית פונקציות הדורשות Root, מומלץ לבדוק חלופות ללא Root.
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>הטלפון הופך ל"לבנה" (לא נדלק)

{class="mt-1"}
אובדן אחריות

{class="list-disc pl-6 mt-1 space-y-1"}
- אובדן נתונים
- תקלה בפונקציות תשלום
- לפני הבהוב יש לבצע גיבוי מלא, לקרוא בעיון את המדריך, ולוודא התאמה לדגם ולגרסה.
- משאבים מומלצים

{class="mt-1"}
XDA Developers
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>: קהילת מפתחי האנדרואיד הגדולה בעולם, עם שפע מדריכי הבהוב ומשאבי ROM.

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>Coolapk (CoolAPK)</strong>: קהילה דיגיטלית ידועה, עם מדריכים ודיונים רבים.
- <strong>פורומים לפי דגם</strong>: כמו קהילת Xiaomi, קהילת OnePlus, עם מדריכים רשמיים וקהילתיים.
- <strong>פרק 25: טיפול בטלפון יד שנייה ומורשת דיגיטלית</strong>היי, חברים, אחרי יותר מעשרים פרקים של "אימון", אני מאמין שכבר הפכתם מ"טירון דיגיטלי" למשתמש טלפון די בטוח בעצמו. אבל לחיי הטכנולוגיה יש תמיד מחזוריות – החדש הופך בסוף לישן. כשאתם מתכוננים "להפריש" את החבר הוותיק, האם אתם יודעים איך להיפרד בכבוד ובבטחה?
:::

#### ו. שאלות נפוצות (Q&amp; A)

::: div .qa-item .mt-3
{class="font-semibold mb-1"}
<i class="fas fa-question-circle text-primary mr-1"></i>Q1: האם ניתן לשחזר לאחר פתיחת נעילת BL?

{class="mb-2 pl-6"}
<strong>A:</strong>ניתן לנעול מחדש. בדרך כלל נדרש לצרוב חבילת יצרן מלאה ולהשתמש בסקריפט צריבה (כמו של Xiaomi) <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">flash_all_lock.bat</code>) כדי לנעול. אך שים לב, נעילה מחדש לא מבטלת נתיכי אבטחה (כמו Knox של Samsung).
:::

::: div .qa-item .mt-3
{class="font-semibold mb-1"}
<i class="fas fa-question-circle text-primary mr-1"></i>Q2: איך מבצעים Root לאחר פתיחה?

{class="mb-2 pl-6"}
<strong>A:</strong>פתיחת BL היא רק הצעד הראשון. Root בדרך כלל דורש:

{class="list-decimal pl-12 mb-2 space-y-1"}
1. צרוב Recovery מותאם (כמו TWRP).
2. דרך Recovery צרוב Magisk לתיקון תמונת boot והשגת Root.
:::
