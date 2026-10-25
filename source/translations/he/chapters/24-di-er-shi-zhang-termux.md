---
id: di-er-shi-zhang-termux
part: jin-jie-pian
nav:  פרק 20 נספח
toc: sub
kind: supplement
---

### נספח לפרק 20:Termux — סביבת טרמינל לינוקס ניידת על מכשירי Android

{class="chapter-intro mb-4"}
אם נראה לך שמצב מפתח עדיין לא מספיק "הארדקור", ואתה רוצה לחוות שורת פקודה מלאה של לינוקס על הטלפון שלך, אז Termux מיועד בדיוק עבורך. הוא אינו דורש הרשאות root, ויכול להפוך טלפון Android רגיל לתחנת עבודת לינוקס ניידת, והוא כלי רב עוצמה למשתמשים מתקדמים החוקרים פיתוח ותפעול במובייל.

#### אחד, מה זה Termux

שניים, פונקציות ותכונות מרכזיות

🖥️ סביבת לינוקס מלאה

#### שניים, פונקציות ותכונות מרכזיות

##### 🖥️ סביבת לינוקס מלאה

Termux<strong>Bash מובנה בלבד</strong>Shell. ל-Zsh/fish, התקן ידנית:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install zsh</code>.<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install fish</code>. Termux: Vim/Nano/Emacs. "pkg install" 2000+ חבילות, GCC, OpenSSH, SQLMap.

##### 📦 ניהול חבילות חזק

חיבור SSH מרוחק

##### 🔒 פונקציות אבטחה ורשת

- <strong>כלי הצפנה</strong>: מספק כלי הצפנה כמו OpenSSL, תומך בהצפנת נתונים ותקשורת מאובטחת.
- <strong>בניית שרת</strong>: ניתן להגדיר Nginx או Apache לבניית שרת אתרים סטטיים.
- <strong>🔧 שילוב מערכת והרחבה</strong>גישה להרשאות אחסון הטלפון לניהול קבצים מקומי.

##### 🔧 שילוב מערכת והרחבה

- תומך בחיבור מקלדת בלוטות' וצגים חיצוניים, עם תמיכה מלאה בעכבר.
- שלוש, מערכת אקולוגית של תוספים
- היישום המרכזי של Termux ניתן להרחבה דרך מספר יישומי תוספים אופציונליים, המספקים פונקציות ושילובים נוספים:

#### שלוש, מערכת אקולוגית של תוספים

תיאור פונקציה

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Termux:API</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">חושף פונקציות Android API לתוכניות שורת פקודה</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Boot</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מאפשר הרצת סקריפטים בעת אתחול המכשיר</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Float</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מספק חלון טרמינל צף</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Styling</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מאפשר סכמות צבעים והתאמת גופנים לטרמינל</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Tasker</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">משלב סקריפטים של Termux עם אפליקציית האוטומציה Tasker</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Widget</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מאפשר הרצת סקריפטים מווידג'ט במסך הבית</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">הערה חשובה</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">את Termux והתוספים שלו חובה להתקין מאותו מקור, מכיוון שהם חולקים את אותו sharedUserId. ערבוב התקנות ממקורות שונים (כמו F-Droid ו-GitHub) יגרום לשגיאות התקנה.</td>
                            </tr>
                        </tbody>
                    </table>
```

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>ארבע, מדריך התקנה והגדרה

{class="mt-1"}
📥 שלבי התקנה
:::

#### ארבע, מדריך התקנה והגדרה

##### 📥 שלבי התקנה

1. <strong>אתחול המערכת</strong>: לאחר ההפעלה הראשונה המתן עד להשלמת "Installing bootstrap packages".
2. <strong>קבלת הרשאות אחסון</strong>: הרץ את
3. <strong>termux-setup-storage</strong>לעדכון רשימת החבילות.<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">עדכון מקורות תוכנה</code>: הרץ את
4. <strong>pkg update &amp;&amp; pkg upgrade</strong>לעדכון רשימת החבילות.<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">התקן את Python:</code>החלפת מקור מראה

##### ⚙️ אופטימיזציה בסיסית

- <strong>termux-change-repo</strong>כדי להחליף מקור מראה דרך ממשק גרפי (מומלץ מקור המראה של אוניברסיטת Tsinghua).<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">הגדרת מקשי קיצור</code>: מקש הורדת עוצמת הקול מדמה Ctrl, מקש העלאת עוצמת הקול מדמה Esc, לשיפור יעילות הקלט.
- <strong>עיצוב ממשק</strong>: התקן Zsh + Oh My Zsh, הגדר ערכות נושא ותוספים.
- <strong>חמישה, תרחישי שימוש אופייניים</strong>💻 בדיקות פיתוח במובייל

#### חמישה, תרחישי שימוש אופייניים

##### 💻 בדיקות פיתוח במובייל

נהל שרתים מרחוק דרך SSH, בצע משימות תחזוקת מערכת, ניתוח יומנים ועוד, טפל בבעיות שרת בכל זמן ובכל מקום.

##### 🖥️ תפעול ותחזוקת שרתים

מספק סביבת לינוקס אמיתית, פלטפורמה אידיאלית ללימוד שורת פקודה וניהול מערכת, ניתן לתרגל כתיבת סקריפטים ב-Shell, ניהול הרשאות קבצים ופקודות בסיסיות.

##### 📚 למידת פעולות לינוקס

Linux אמיתי, ללימוד Shell והרשאות ( <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chmod 755</code> הגדרת סיביות הרשאה rwxr-xr-x,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chown user:group</code> שינוי בעלות קובץ,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls -l</code> הצגת owner/group/other 3 קבוצות 9 סיביות) ופקודות בסיסיות. זהו מודל ההרשאות הקלאסי של Unix/Linux (owner / group / other × קריאה / כתיבה / ביצוע), שונה לחלוטין מ-ACL של NTFS ב-Windows.

##### 🔐 בדיקות אבטחת רשת

הגרסה היציבה האחרונה של Termux היא v0.118.2, המיועדת למכשירי Android ≥ 7. חשוב לציין ש-Termux עלול להיות לא יציב ב-Android 12 ומעלה, מומלץ לעקוב אחר יומן העדכונים הרשמי למידע תאימות עדכני.

#### שישה, גרסאות ותאימות

Termux מביא את חוויית טרמינל הלינוקס העוצמתית למכשירי Android, והופך את הטלפון לכלי פיתוח ולמידה נייד. בין אם אתה מפתח, מנהל מערכת או חובב טכנולוגיה, תוכל לנצל את Termux כדי ליהנות מחוויית שורת פקודה מלאה על מכשיר נייד, ולממש את הרעיון של "לינוקס בכיס".

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>בוא ננסה: הרץ את פקודת הלינוקס הראשונה שלך על הטלפון

{class="mt-1"}
הורד והתקן את Termux מ-F-Droid, בהפעלה הראשונה המתן לסיום האתחול.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>הרץ את

{class="list-decimal pl-6 mt-1 space-y-1"}
1. pkg update &amp;&amp; pkg upgrade
2. הריצו <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code> לעדכון חבילות התוכנה.
3. התקינו את Python: <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install python</code>.
4. הקלידו <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python3 -c "print('Hello from Termux!')"</code> וחושו בהנאה שבהרצת קוד על הטלפון.
5. , ותרגיש את ההנאה של הרצת קוד על הטלפון.<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ארבע, מעבר (פרקים 21-26)</code>חלק זה ייקח אותך אל העולם הדיגיטלי העמוק יותר. מאבטחת מידע ועד עקרונות AI, מחשיבה תכנותית ועד מורשת דיגיטלית, תכנים אלו יעזרו לך להפוך לאזרח דיגיטלי אמיתי.
:::
