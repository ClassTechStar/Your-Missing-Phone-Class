---
id: di-shi-si-zhang
num: 14
part: ruan-jian-pian
nav: פרק 14: מנהלי סיסמאות בעומק
toc: default
kind: chapter
---

### פרק 14: נושא מנהל סיסמאות

{class="chapter-intro mb-4"}
לאדם המודרני יש בממוצע עשרות ואפילו מאות חשבונות אינטרנט. אם כל חשבון משתמש באותה סיסמה, ברגע שאתר אחד נפרץ, כל החשבונות בסכנה. אם כל חשבון משתמש בסיסמה מורכבת שונה, פשוט אי אפשר לזכור.

#### 1.למה אתה צריך מנהל סיסמאות？

2.איך מנהל סיסמאות עובד

אחסון מוצפן

#### 2.איך מנהל סיסמאות עובד

1. <strong>סיסמת מאסטר</strong>:אתה מגדיר סיסמת מאסטר אחת לפתיחת כספת הסיסמאות. סיסמת המאסטר עצמה לא מאוחסנת בשרת.
2. <strong>מילוי אוטומטי</strong>:במסך התחברות לאתר או אפליקציה, מנהל הסיסמאות ממלא אוטומטית את שם המשתמש והסיסמה.
3. <strong>יצירת סיסמאות</strong>:יכול ליצור סיסמאות אקראיות ומורכבות, להגברת האבטחה.
4. <strong>3.המלצות למנהלי סיסמאות מובילים</strong>מובנה במערכת:

#### ג. מבוא לעקרונות הצפנה

הבנת הצפנת מנהל סיסמאות עוזרת לשפוט אמון בספק. הסבר פשוט למושגים מרכזיים.

##### 1. הצפנת AES-256

AES (Advanced Encryption Standard) הוא אלגוריתם הצפנה סימטרי שאושר על ידי NIST, ונמצא בשימוש נרחב על ידי בנקים, צבא וממשלות. "256" מתייחס לאורך המפתח - 256 סיביות, שפיצוחו התיאורטי דורש זמן ארוך מגיל היקום. מנהלי סיסמאות מובילים (1Password, Bitwarden, KeePass) משתמשים ב-AES-256 להצפנת כספת הסיסמאות שלך.

##### 2. ארכיטקטורת Zero-Knowledge

"ידע אפס" לא אומר שספק השירות לא שומר כלום, אלא ש<strong>הצפנה ופענוח במכשיר המקומי, השרת שומר רק טקסט מוצפן</strong>. התהליך המדויק:

1. אתה מזין את הסיסמה הראשית בצד הלקוח.
2. הלקוח גוזר מפתח מהסיסמה הראשית (במכשיר שלך).
3. רק הטקסט המוצפן מועלה לשרת.
4. בהתחברות הבאה, השרת שולח טקסט מוצפן, הלקוח פוענח עם הסיסמה.

נקודות מפתח:<strong>הסיסמה הראשית עצמה לעולם לא עוזבת את המכשיר שלך</strong>, גם בשרת. גם אם הספק נפרץ, ההאקר מקבל טקסט מוצפן - אלא אם ינחש את הסיסמה.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>למה "Zero-Knowledge" אומר שהספק לא רואה את הסיסמה?

{class="mt-1"}
מפתח הפענוח נגזר מהסיסמה הראשית שלך, שנמצאת רק בראשך ובמכשיר המקומי. השרת של הספק אינו מכיל גם את הסיסמה הראשית וגם לא את מפתח הפענוח - רק טקסט מוצפן. לכן ספקים כמו Bitwarden ו-1Password מצהירים במפורש "גם אנחנו לא יכולים לראות את הסיסמאות שלך" - לא מפני שהם לא רוצים, אלא כי טכנית זה בלתי אפשרי.
:::

##### 3. פונקציית גזירת מפתח: PBKDF2 ו-Argon2

הסיסמה הראשית לא יכולה לשמש ישירות כמפתח - היא עוברת "פונקציית גזירה". תפקיד:<strong>מכוון להאטת החישוב</strong>, כדי שעלות פריצה בכוח תהיה גבוהה מדי להאקרים.

- <strong>PBKDF2</strong>:תקן ותיק, בשימוש iCloud, Bitwarden, LastPass. האטת פיצוח על ידי איטרציות (100,000+).
- <strong>Argon2</strong>:זוכה 2015, מודרני יותר מ-PBKDF2. צריכת זיכרון + חישוב - קשה ל-GPU/ASIC. Bitwarden, KeePassXC תומכים.

איטרציות גבוהות = בטוח יותר אך איטי. ספקים רציניים מפרסמים אלגוריתם ואיטרציות לביקורת.

##### 4. אזהרה: דליפת LastPass 2022

אוגוסט 2022, LastPass הודיעה על חדירה; נובמבר, ההאקר לקח גיבוי מוצפן. לקחים:

- <strong>ארכיטקטורת ידע-אפס שומרת על הקו האדום</strong>:הספרייה מוצפנת, ההאקר לא יכול לפענח - בתנאי שהסיסמה חזקה.
- <strong>משתמשים עם סיסמה ראשית חלשה בסכנה הגדולה ביותר</strong>:האקר יכול לפרוץ סיסמה חלשה ללא רשת, משתמשים עם סיסמה חלשה/חוזרת בסיכון.
- <strong>גם מטה-נתונים דולפים</strong>:תוכן מוצפן, אך URL והערות אולי לא, חושף אילו שירותים בשימוש.

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>לקחים מתקרית LastPass

{class="mt-1"}
1) סיסמה ארוכה וייחודית (16+, גדול/קטן/מספר/סמל); 2) העדף Argon2id, איטרציות גבוהות; 3) 2FA עצמאי לחשבונות רגישים (בנק, דוא"ל), אל תסתמך רק על מנהל סיסמאות.
:::

#### ד. המלצות על מנהלי סיסמאות מובילים

##### :בחירה מועדפת למשתמשי אקוסיסטם אפל. אינטגרציה חלקה עם Safari ואפליקציות, חינמי, מאובטח. החיסרון הוא שימוש לא נוח בפלטפורמות אחרות.

- <strong>Google Password Manager</strong>:נוח למשתמשי אנדרואיד. אינטגרציה עם Chrome ומערכת אנדרואיד, חינמי.
- <strong>Huawei Password Vault</strong>:מובנה במערכת HarmonyOS, מתאים למשתמשי Huawei.
- <strong>כלים מקצועיים צד שלישי:</strong>Bitwarden

##### :קוד פתוח וחינמי, פונקציונלי מאוד, תומך בכל הפלטפורמות. מומלץ בחום למשתמשים שמעריכים פרטיות.

- <strong>1Password</strong>:ממשק יפה, פונקציות עשירות, מתאים למשפחות וצוותים. בתשלום.
- <strong>LastPass</strong>:מנהל סיסמאות ותיק, הגרסה החינמית מוגבלת.
- <strong>KeePass</strong>:אחסון מקומי לחלוטין, קוד פתוח וחינמי. מתאים למשתמשי גיקים.
- <strong>4.שיטות עבודה מומלצות למנהל סיסמאות</strong>הגדר סיסמת מאסטר חזקה

#### ה. הערכת חוזק סיסמה בפועל

מנהלי סיסמאות מציגים "חוזק" (אדום/צהוב/ירוק), אך בודק רק אורך וסוג. לבדיקה אמיתית דרוש "אנטרופיה" ו"האם הודלף".

##### 1. אנטרופיה: מדידה מדעית של חוזק סיסמה

"אנטרופיה" מודדת אי-ודאות, ביחידת סיביות. גבוהה יותר = יותר ניסיונות לפריצה.

- <strong>"123456"</strong>: אנטרופיה נמוכה מאוד, פריצה מיידית.
- <strong>"P@ssw0rd"</strong>:נראה מורכב, אך בכל רשימת מילון, אנטרופיה נמוכה.
- <strong>"correct horse battery staple"</strong>:4 מילים אקראיות, ~44 סיביות, קשה יותר מ-"P@ssw0rd".
- <strong>16 תווים אקראיים (אותיות גדולות+קטנות+מספרים+סמלים)</strong>:~100 סיביות, כוח נוכחי לא יכול לפרוץ.

מסקנה:<strong>"אורך + אקראיות" חשוב יותר מ"סמלים מורכבים"</strong>. לכן סיסמאות ארוכות אקראיות של מנהל הסיסמאות בטוחות באמת.

##### 2. HaveIBeenPwned: בדוק אם הסיסמה הודלפה

מתוחזק על ידי חוקר האבטחה Troy Hunt <a href="https://haveibeenpwned.com" class="text-primary hover:underline" target="_blank" rel="noopener">haveibeenpwned.com</a> מכיל חשבונות וסיסמאות מדליפות גדולות. אפשר:

1. הזן דוא"ל, בדוק אם החשבון נחשף.
2. Pwned Passwords - בדוק אם סיסמה במאגר (מובנה במנהלים ודפדפנים).

אם סיסמה מופיעה במאגר דליפות,<strong>לא משנה כמה מורכבת היא נראית, יש להחליף אותה מיד</strong>– כי התקפת מילון מנסה סיסמאות ידועות אלה קודם.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-shield-alt mr-2"></i>עיקרון שאילתת k-Anonymity

{class="mt-1"}
דואג שהזנת הסיסמה ב-HaveIBeenPwned תגרום לדליפה נוספת? אל תדאג. שאילתות מודרניות משתמשות בפרוטוקול "k-אנונימיות": הדפדפן שולח רק את 5 התווים הראשונים של ה-hash לשרת, השרת מחזיר רשימת hashes שמתחילים ב-5 תווים אלה, וההשוואה נעשית מקומית. כלומר, השרת לעולם לא רואה את ה-hash המלא של הסיסמה. "בדיקת סיסמאות שדלפו" של 1Password ו-Bitwarden פועלות בדיוק כך.
:::

##### 3. פונקציית ניטור מובנית במנהל סיסמאות

- <strong>1Password Watchtower</strong>:ניטור סיסמאות חלשות/חוזרות/מודלפות/ישנות/ללא 2FA, אדום/כתום/צהוב.
- <strong>Bitwarden Vault Health</strong>:חינם: חלשות/חוזרות; בתשלום: מודלפות (HaveIBeenPwned).
- <strong>"המלצות אבטחה" ב-iCloud Keychain</strong>:iOS &gt; סיסמאות &gt; המלצות, מצביע על מודלפות/חוזרות.
- <strong>"בדיקת סיסמאות" ב-Google Password Manager</strong>:Chrome מובנה, בדיקת מודלפות/חלשות/חוזרות.

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>בדוק עכשיו: האם הסיסמה שלך בטוחה

{class="list-decimal pl-6 mt-1 space-y-1"}
1. פתח haveibeenpwned.com, הזן דוא"ל, בדוק דליפות.
2. iPhone: הגדרות &gt; סיסמאות &gt; המלצות, טפל באדומים.
3. Chrome: הגדרות &gt; סיסמאות &gt; בדוק, תקן.
4. 1Password/Bitwarden: Watchtower/Health, "מודלף" ו"חוזר" קודם.
:::

#### ו. Passkey: העתיד של התחברות ללא סיסמה

2024-2026, מהפכת סיסמאות -<strong>Passkey (מפתח גישה)</strong>צפוי להחליף סיסמאות. Apple, Google, Microsoft, FIDO, W3C, השינוי הגדול ביותר בעשרות שנים.

##### 1. מהו Passkey?

Passkey מבוסס FIDO2/WebAuthn, משתמש<strong>זוג מפתחות על המכשיר</strong>תחליף לסיסמה. העיקרון מפושט:

- הטלפון שלך מייצר זוג מפתחות:<strong>מפתח ציבורי</strong>(נרשם אצל האתר) + <strong>מפתח פרטי</strong>(נשמר תמיד בשבב האבטחה של המכשיר שלך).
- בהתחברות, האתר שולח "אתגר", הטלפון חותם במפתח פרטי, האתר מאמת במפתח ציבורי.
- לפני חתימה, אימות ביומטרי (Face ID/טביעת אצבע) או PIN.
- בכל התהליך, <strong>שום סיסמה לא מועברת ברשת</strong>.

##### 2. Passkey מול סיסמה מסורתית

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ממד</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">סיסמה מסורתית</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Passkey</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">עמידות לדיוג</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">חלש, אתר דיוג יכול לגנוב סיסמה</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">עמיד טבעית לדיוג, מפתח פרטי חותם רק על דומיין אמיתי</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">השפעת דליפת שרת</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">גיבוב סיסמה עלול להיפרץ</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">השרת שומר רק מפתח ציבורי, דליפה ללא השפעה</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">נוחות</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">דורש זיכרון/הקלדה/ניהול</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">התחברות בשנייה עם Face ID/טביעת אצבע</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">התקפת השמעה חוזרת</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">עלולה להיחטף ולהיות מושמעת חזרה על ידי אדם באמצע</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">כל חתימה חד-פעמית, לא ניתנת להשמעה חוזרת</td>
                            </tr>
                        </tbody>
                    </table>
```

##### 3. תמיכת פלטפורמות

- <strong>Apple iCloud Passkey</strong>:iOS 16+/macOS Ventura+, סנכרון בין מכשירי Apple, ללא יצירה מחדש.
- <strong>Passkey ב-Google Password Manager</strong>:Android+Chrome, Passkey ב-Google, סנכרון; 2023 Google תומך.
- <strong>Microsoft</strong>:Windows 11/Edge תומכים; Microsoft, Outlook, Office, ב-Authenticator.
- <strong>1Password / Bitwarden</strong>:יצירה, אחסון, סנכרון חוצה פלטפורמות, לא תלוי באקוסיסטם.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>סנכרון חוצה-מכשירים הוא פריצת דרך מרכזית

{class="mt-1"}
הבעיה הגדולה ביותר של Passkey בגרסאותיו המוקדמות הייתה "קשירה למכשיר יחיד" - החלפת טלפון דרשה יצירה מחדש. החל מ-2023, Apple, Google ו-Microsoft יישמו סנכרון ענן של Passkey: iCloud Keychain מסנכרן בין מכשירי Apple, Google Password Manager מסנכרן בין מכשירי Android. 1Password וספקים אחרים חיברו סנכרון חוצה-אקוסיסטמים. משמעות הדבר: ל-Passkey יש עתיד כתחליף מעשי לסיסמאות.
:::

##### 4. יצירה ושימוש ב-Passkey

<strong>נתיב iOS (iPhone):</strong>

1. באתר תומך (Google, Microsoft, Amazon, eBay, PayPal) &gt; "Add passkey".
2. Face ID/Touch ID, Passkey נוצר ונשמר ב-iCloud.
3. בכניסה הבאה, "התחבר עם iPhone", Face ID.
4. ניהול: הגדרות &gt; סיסמאות &gt; אתר.

<strong>נתיב Android:</strong>

1. באתר &gt; "Add passkey".
2. Google Password Manager &gt; חשבון &gt; נעילת מסך (טביעת אצבע/תבנית/PIN).
3. Passkey נשמר ב-Google, סנכרון בין מכשירי Android.
4. בכניסה, "Passkey", נעילת מסך.
5. ניהול: הגדרות &gt; סיסמאות &gt; Password Manager &gt; google.com.

##### 5. התחברות Passkey חוצה-מכשירים

ב-Windows ללא Passkey, סרוק קוד QR מ-iPhone:

1. בעמוד ההתחברות של האתר בחר "השתמש ב-Passkey".
2. בחר "השתמש במכשיר אחר".
3. המחשב מציג קוד QR, סרוק עם ה-iPhone.
4. iPhone Face ID, האתר נפתח במחשב.

Bluetooth+אינטרנט מוצפן, המפתח לא עוזב את ה-iPhone.

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>נסה עכשיו: חווית התחברות ללא סיסמה

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Google &gt; אבטחה &gt; Passkey &gt; הוסף, Face ID/טביעת אצבע.
2. Microsoft &gt; אבטחה &gt; אפשרויות &gt; Passkey.
3. Taobao, JD, eBay, PayPal.
4. שמור סיסמה כגיבוי, העבר חשבונות רגישים ל-Passkey.
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>המלצה לתקופת מעבר

{class="mt-1"}
Passkey לא מחליף לגמרי - אתרים ב"Passkey+סיסמה". המלצה: חשבונות רגישים קודם, אך<strong>אל תמחק מיד סיסמאות מסורתיות</strong>, כגיבוי; המשך להשתמש במנהל סיסמאות. Passkey = "תוספת חזקה" לא "החלפה".
:::

#### ז. מפתחות אבטחה חומרתיים

אם דרישות האבטחה שלך גבוהות - קריפטו, מנהל/עיתונאי/פעיל, חשבונות ארגון - מפתח חומרה אמין יותר מ-SMS.

##### 1. מהו מפתח אבטחה חומרתי?

מפתח חומרה (דמוי USB), שבב מאובטח, דורש מגע/NFC. מוצרים:

- <strong>YubiKey</strong>(Yubico): פופולרי, FIDO2/WebAuthn/U2F/OTP/PIV/OpenPGP, USB-C/USB-A/NFC. 5 Series 50-70 USD.
- <strong>Google Titan</strong>:Google, USB-C+NFC/Bluetooth, 30-40 USD.
- <strong>OnlyKey</strong>: חלופת קוד פתוח, תומך בפרוטוקולים מרובים.
- <strong>תחליף מקומי</strong>:Feitian ePasskey, זול יותר.

##### 2. למה מפתח חומרתי בטוח יותר מקוד SMS?

- <strong>עמידות לדיוג</strong>:כמו Passkey, רק לדומיין אמיתי, פישינג לא עובד.
- <strong>עמיד לחטיפת SIM</strong>:SMS פגיע ל-SIM-swap, מפתח לא צריך מספר.
- <strong>עמיד לאיש-באמצע</strong>:FIDO2 כולל challenge, לא ניתן לשחזר.
- <strong>בידוד פיזי</strong>:מפתח בשבב, תוכנה זדונית לא קורא.

##### 3. תרחישים מתאימים

- חשבונות בורסת מטבעות קריפטו, שחזור ארנק.
- SSO ארגוני, VPN, SSH.
- דוא"ל, GitHub, "חשבונות ראשיים" - פריצה = איפוס הכל.
- עיתונאים, עורכי דין, מנהלים בכירים – אנשים בסיכון גבוה.

##### 4. איך מגדירים מפתח חומרתי כאימות דו-שלבי

Google + YubiKey:

1. קנה YubiKey (שניים: יומיומי + גיבוי, מיקומים שונים).
2. myaccount.google.com &gt; אבטחה &gt; 2FA.
3. "הוסף מפתח" &gt; USB-C או NFC.
4. גע במגע המתכת.
5. מומלץ לרשום מפתח גיבוי שני.
6. הגדר מפתח כעדיפות, SMS כגיבוי.

אתרים: Google, GitHub, Microsoft, Apple, Facebook, Twitter, Dropbox, GitLab, AWS, Coinbase, Binance.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>אסטרטגיית מפתח כפול

{class="mt-1"}
הסיכון: "איבוד". 1) שני מפתחות; 2) אחד עליך (קליפ), אחד בכספת; 3) קודי גיבוי מודפסים. איבוד = לא נעילה.
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>יש להיזהר בערוץ הרכישה

{class="mt-1"}
קנה רשמי, לא יד שנייה - עלול להיות backdoor. קושחה לא מתעדכנת, אך Yubico מפרסמת אזהרות.
:::

#### ח. שיתוף סיסמאות למשפחה/צוות

משפחה: Netflix, Wi-Fi, מנעול. צוות: שרתים, מסד נתונים, רשתות חברתיות.<strong>שליחת סיסמה ב-WeChat או כתיבה במסמך משותף הם פעולות בסיכון גבוה</strong>—ברגע שצ'אט או מסמך נודע, הסיסמה נחשפת.

##### 1. "Vault" משותף ב-1Password

1Password הוא תקן לשיתוף. מנגנון הליבה שלו הוא <strong>מספר כספות</strong>:

- <strong>כספת אישית</strong>: רק אתה רואה, כגון בנק, דוא"ל וחשבונות פרטיים.
- <strong>כספת משותפת</strong>:כולם רואים: Netflix, Wi-Fi, כרטיס.
- <strong>רמות הרשאה</strong>:צוות: "קריאה בלבד" או "קריאה ללא עריכה".

כל אחד מתחבר בחשבונו, רואה Vault משותף. שינוי = סנכרון מיידי.

##### 2. פונקציית "ארגון" ב-Bitwarden

Bitwarden חינם: Send (שיתוף זמני); בתשלום: ארגון, הרשאות. גם self-hosted, לארגונים עם דרישות ריבונות נתונים.

##### 3. משפחה: Netflix, Wi-Fi

- <strong>Netflix / אתרי וידאו</strong>:1Password Family Vault, כל אחד מתחבר, בלי צ'אט.
- <strong>סיסמת Wi-Fi ביתית</strong>:AirDrop Wi-Fi (iOS); Android 12+ "Nearby Share".
- <strong>מנעול חכם, מכשירי חשמל חכמים</strong>:"משפחה" ב-App, חשבון לכל אחד, לא מנהל משותף.
- <strong>ממשק ניהול נתב ביתי</strong>:מנהל ב-1Password, Wi-Fi אורח SSID נפרד.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>יחס עלות-תועלת של 1Password משפחתי

{class="mt-1"}
1Password Families עולה כ-4.99 USD לחודש, תומך בעד 5 בני משפחה, לכל אחד כספת פרטית עצמאית + 4 כספות משותפות. בחישוב זה פחות מ-1 USD לאדם לחודש - זהו פתרון שיתוף המשפחתי עם החוויה הטובה ביותר כיום. Bitwarden Family עולה 10 USD לשנה ותומך ב-6 אנשים, עם יחס איכות-מחיר גבוה יותר, אך חוויית הממשק מעט נחותה.
:::

##### 4. תרחיש צוות: שיתוף סיסמאות שרת/מסד נתונים

- <strong>1Password Teams / Business</strong>:Vault לפי מחלקה/פרויקט, הרשאות, ביקורת.
- <strong>Bitwarden Teams / Enterprise</strong>:קוד פתוח, self-hosted, SSO.
- <strong>עיקרון הפרדת תפקידים</strong>:מנהל לא רק אחד - 2-3 "אנשי חירום", רצף עסקי.
- <strong>תהליך עזיבה</strong>:עזיבה = בטל גישה, שנה סיסמאות רגישות.

##### 5. Emergency Access: אם משהו קורה

תרחיש: אתה מנהל את כל החשבונות, ונפגעת/נפטרת - המשפחה לא יכולה להיכנס.<strong>פונקציית "גישת חירום"</strong>מתוכנן לזה - איש קשר מהימן, כשאתה לא יכול.

<strong>הגדרת גישת חירום ב-Bitwarden:</strong>

1. Bitwarden Web Vault &gt; הגדרות &gt; Emergency Access.
2. הוסף את הדוא"ל של איש קשר מהימן והזמן אותו לקבל.
3. "תקופת המתנה" (7-14 ימים): מבקש עד שאתה מאשר.
4. אם לא מגיב, אחרי התקופה הוא מקבל גישה.
5. אתה יכול לדחות או לבטל.

<strong>גישת חירום ב-1Password:</strong>

1. 1Password: "משפחה/צוות" - שים פריטים ב-Vault משותף.
2. לגרסה אישית: מסור סיסמה לאדם מהימן, או במעטפה בכספת.
3. 1Password: "קוד שחזור", הדפס.

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>הגדר עכשיו: השאר "מפתח גיבוי" למשפחה

{class="list-decimal pl-6 mt-1 space-y-1"}
1. בחר בן משפחה מהימן כ"איש קשר לחירום".
2. הגדר Emergency Access (Bitwarden) או Family Vault (1Password).
3. סיסמה + קוד על נייר, במעטפה, בכספת.
4. כחצי שנה, ודא איש קשר.
:::

#### ט. שיטות עבודה מומלצות למנהל סיסמאות

- <strong>הפעל אימות דו-שלבי</strong>:הפעל אימות דו-שלבי לחשבון מנהל הסיסמאות, להוספת שכבת הגנה.
- <strong>בדוק סיסמאות חלשות באופן קבוע</strong>:לרוב מנהלי הסיסמאות יש פונקציית "ביקורת אבטחה", שעוזרת לך למצוא סיסמאות חלשות וכפולות.
- <strong>אל תשכח את סיסמת המאסטר</strong>:סיסמת המאסטר לא ניתנת לשחזור, לשכוח פירושו לאבד את כל הסיסמאות. מומלץ לרשום על נייר ולשמור במקום בטוח.
- <strong>גישת חירום</strong>:הגדר איש קשר לשעת חירום, למקרה שלא תוכל לגשת, אדם מהימן יוכל לקבל את הסיסמאות שלך.
- <strong>תזכורת חשובה</strong>מנהל סיסמאות אמנם נוח, אבל יש גם סיכון:אם סיסמת המאסטר דולפת, כל הסיסמאות חשופות. לכן סיסמת המאסטר ממש לא יכולה להיות זהה לסיסמאות אחרות, וגם לא להיכתב במקום שקל למצוא. בנוסף, מומלץ לבחור ספק שירות עם רקורד אבטחה טוב.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>נסה עכשיו:התחל להשתמש במנהל סיסמאות

{class="mt-1"}
בחר מנהל סיסמאות (מומלץ Bitwarden או המובנה במערכת).
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>הירשם לחשבון, הגדר סיסמת מאסטר חזקה.

{class="list-decimal pl-6 mt-1 space-y-1"}
1. ייבא סיסמאות קיימות (אם יש) או התחל להוסיף סיסמאות חדשות.
2. התקן תוסף דפדפן או אפליקציית טלפון, חווה את פונקציית המילוי האוטומטי.
3. בדוק את דוח ביקורת האבטחה, מצא סיסמאות שדורשות שיפור.
4. ג. חלק מתקדם(פרקים 15-20)
5. אחרי ששלטת ביסודות וביישומי תוכנה, בוא נצלול עמוק יותר לפונקציות המתקדמות של הטלפון. תוכן זה יעזור לך להפוך למומחה טלפונים אמיתי, ואפילו לפתוח כמה "כישורים נסתרים".
:::
