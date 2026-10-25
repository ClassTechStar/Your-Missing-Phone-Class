---
id: di-liu-shi-er-zhang
num: 62
part: ios-kai-fa-pian
nav: פרק 62: פיתוח ממשק – מבוא ל-SwiftUI
toc: default
kind: chapter
---

### פרק 62: פיתוח ממשק — מבוא ל-SwiftUI

{class="chapter-intro mb-4"}
הממשק הוא כל מה שהמשתמש רואה. SwiftUI הוא פריימוורק ממשק הצהרתי שאפל השיקה ב-2019 — אתם רק "מצהירים" איך הממשק אמור להיראות, והמערכת דואגת בעצמה לרינדור, להתאמה למצב הכהה ולהתאמה לכל גדלי המסך. נכון ל-2026, SwiftUI הוא כבר הבחירה המובילה באופן חד-משמעי לפרויקטים חדשים. בפרק הזה נלמד "לצייר".

#### 1. תפיסת העולם של SwiftUI: הצהרתי, לא פקודתי

פיתוח ממשק ישן הוא "פקודתי": מורים למערכת "צור כפתור → שים ב-(20,30) → קבע צבע", שלב אחר שלב. SwiftUI הוא "הצהרתי": אתם פשוט מתארים "בממשק יש כפתור אדום עם הכיתוב לחצו עליי", ואיך לצייר ומתי לצייר מחדש — זה כבר כאב הראש של המערכת.

::: div .code-block
:::inline div .code-head
<span>SWIFT · ה-View הראשון ב-SwiftUI</span><span class="dots">···</span>
:::

```
import SwiftUI

struct ContentView: View {
    var body: some View {      // body: מתאר "איך הממשק נראה"
        VStack {               // מסודרים אנכית
            Text("שלום, עולם!")
                .font(.largeTitle)      // מודיפאייר: כותרת גדולה
            Button("לחץ כאן") {
                print("נלחץ!")
            }
            .buttonStyle(.borderedProminent)  // כפתור כחול מלא
        }
        .padding()
    }
}
```
:::

הנקודה המרכזית: תצוגה = מבנה שמקיים את פרוטוקול View; המאפיין body מתאר את הממשק; והמשנים מתשרשרים כמו שכבות "איפור". זהו כל הבסיס של SwiftUI.

#### 2. תצוגות בסיס: טקסט, כפתור, שדה קלט ותמונה

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">תצוגה</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">למה זה משמש</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">דוגמה</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">הצגת טקסט</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text("שלום")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">כפתור</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button("לחצו עליי") { פעולה }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">שדה קלט</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField("רמז", text: $טקסט)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">הצגת תמונה</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Image(systemName: "star.fill")</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
ארבע תצוגות הבסיס של SwiftUI

שימו לב ל-Image(systemName:) — אפל משלבת מובנה את ספריית האייקונים SF Symbols (אלפי אייקונים חינמיים), ושם כמו "star.fill" מציג ישר כוכב מלא. זו הטבה נסתרת של פיתוח iOS: כמעט ואין צורך לחפש חומרי אייקונים לממשק.

#### 3. שלישיית הפריסה: VStack, HStack, ZStack

- VStack: מסדרים אנכית (כמו תור למזנון);
- HStack: מסדרים אופקית (כמו ישיבה זה לצד זה);
- ZStack: עורמים זה על זה (כמו חפיסת קלפים; מתאים לתגיות פינה ולכיסויים).

::: div .code-block
:::inline div .code-head
<span>SWIFT · שלישיית הפריסה + מודיפאיירים נפוצים</span><span class="dots">···</span>
:::

```
VStack(alignment: .leading, spacing: 12) {
    HStack {
        Text("חשבון")
        Spacer()                 // מרווח אלסטי: דוחף את הצד הימני עד הסוף
        Text("-25.5 יואן").foregroundColor(.red)
    }
    Divider()                    // קו הפרדה
    Text("הערה: ארוחת צהריים")
}
.padding(16)                     // ריווח מכל הצדדים
.background(Color(.systemGray6)) // רקע אפור בהיר
.cornerRadius(12)                // פינות מעוגלות

// סדר המודיפאיירים משנה: קודם padding ואז background; הרקע לא כולל את השוליים
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
שימו לב: סדר המשנים משנה

{class="mt-1"}
ל-padding(16).background(אפור) ול-background(אפור).padding(16) השפעות שונות — הראשון "קודם ריווח ואז צבע" (הרקע לא כולל את השוליים), והשני "קודם צבע ואז ריווח" (הרקע כולל את השוליים). מכאן נובעים "השוליים הלבנים המוזרים" הכי שכיחים אצל מתחילים. כשלא בטוחים — החליפו סדר, והתצוגה המקדימה תענה מיד.
:::

#### 4. מצב וקישור: נותנים לממשק "חיים"

ממשק סטטי זה משעמם. הכלל של SwiftUI: הממשק תמיד משקף נאמנה את המצב; המצב השתנה — הממשק מצויר מחדש אוטומטית.

::: div .code-block
:::inline div .code-head
<span>SWIFT · מונה עם @State</span><span class="dots">···</span>
:::

```
struct CounterView: View {
    @State private var count = 0   // @State: אם הערך הזה משתנה צריך לצייר מחדש

    var body: some View {
        VStack {
            Text("לחצת \(count) פעמים")
            Button("לחץ +1") {
                count += 1          // משנים את המצב והממשק מתרענן אוטומטית
            }
        }
    }
}
```
:::

שדה קלט דורש "קישור דו-כיווני" — הסימן $ מעביר פנימה גם את הערך וגם את "זכות השינוי":

::: div .code-block
:::inline div .code-head
<span>SWIFT · קישור דו-כיווני עם @Binding</span><span class="dots">···</span>
:::

```
struct InputView: View {
    @State private var text = ""

    var body: some View {
        TextField("הקלד משהו", text: $text)  // קישור דו-כיווני עם $
            .textFieldStyle(.roundedBorder)
        Text("הקלדת: \(text)")   // מתעדכן בזמן אמת בזמן ההקלדה
    }
}
```
:::

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> פעולת המשתמש</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> המצב משתנה (count += 1)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ‏SwiftUI מזהה את השינוי</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> מצייר מחדש (body מחושב מחדש)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
איור 3: זרימת הנתונים החד-כיוונית "מצב → ממשק" של SwiftUI
:::

#### 5. תצוגה מקדימה, ערכות עיצוב ואנימציה: "הצ׳יטים" של SwiftUI

- מאקרו #Preview: מוסיפים בתחתית הקובץ #Preview { ContentView() }, והקנבס בצד ימין מציג בזמן אמת — משנים קוד ורואים מיד;
- מצב כהה בחינם: משתמשים בצבעי המערכת (Color(.systemGray6), .primary) במקום לקבע צבעים, וההתאמה למצב הכהה מתבצעת אוטומטית בלי שורת קוד נוספת;
- אנימציה בשורה אחת: withAnimation { count += 1 } או הוספת .animation(.default, value: count) לתצוגה — מעברים חלקים כמשי.

::: div .code-block
:::inline div .code-head
<span>SWIFT · אנימציות בעשר דקות</span><span class="dots">···</span>
:::

```
struct AnimatedHeartView: View {
    @State private var liked = false

    var body: some View {
        Button {
            withAnimation(.spring(duration: 0.4)) {
                liked.toggle()
            }
        } label: {
            Image(systemName: liked ? "heart.fill" : "heart")
                .font(.system(size: 48))
                .foregroundColor(liked ? .red : .gray)
                .scaleEffect(liked ? 1.3 : 1.0)
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
טיפ: קודם פונקציונליות, אחר כך אנימציה

{class="mt-1"}
הטעות הנפוצה של מתחילים היא "הממשק עוד לא בנוי נכון, וכבר מתלבטים על אנימציות". קודם דאגו שהפונקציונליות עובדת, ורק בסוף הוסיפו את האפקטים — אנימציה היא קישוט על העוגה, פונקציונליות היא העוגה עצמה. זהו גם העיקרון הקבוע שלנו: "פשטות לפני הכל".
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
הידיים על ההגה: בונים "כפתור מצב רוח"

#### 6. מדריך מהיר למשנים נפוצים: עמוד אחד ביד — והממשק נפתר

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">מה רוצים לעשות</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">משנה</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ריווח</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.padding(16)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">פינות מעוגלות</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cornerRadius(12)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">צבע רקע</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.background(Color(.systemGray6))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">גופן וגודל גופן</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.font(.title.bold())</code> / <code class="inline">.font(.system(size: 20))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">צבע חזית (טקסט/אייקון)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.foregroundColor(.red)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מילוי כל הרוחב</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(maxWidth: .infinity)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">גודל קבוע</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(width:100, height: 44)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">יישור</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack(alignment: .leading)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">שקיפות</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.opacity(0.6)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">צל</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.shadow(radius: 5)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">מחוות הקשה</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.onTapGesture { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">סוג מקלדת</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.keyboardType(.decimalPad)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
מדריך מהיר למשנים הנפוצים ב-SwiftUI

לא זוכרים? לא נורא — העמוד הזה בדיוק בשביל לגלול אליו. בפועל משתמשים הכי הרבה בארבעת הראשונים: padding, פינות מעוגלות, רקע וגופן.

{class="mt-1"}
הפכו את פרויקט התבנית למחליף מצבי רוח: כפתור אחד שבכל לחיצה עובר במעגל בין 😀 שמח → 😢 עצוב → 😡 כועס, והטקסט וצבע הרקע מתחלפים יחד איתו. רמז: אחסנו במערך שלוש קבוצות (טקסט + צבע), אחסנו את האינדקס ב-@State, ובלחיצה חשבו (index + 1) % 3. כשתסיימו, שלחו לחברים לנסות — ותקבלו את הגל הראשון של "וואו, אתה כבר בונה אפליקציות".
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
סיכום הפרק

- SwiftUI הוא הצהרתי: מתארים "איך זה אמור להיראות", והמערכת דואגת לצייר ולצייר מחדש
- תצוגה = מבנה שמקיים את פרוטוקול View; body מתאר את הממשק; משנים מתשרשרים כמו שכבות "איפור"
- ארבע תצוגות הבסיס: Text / Button / TextField / Image; ספריית האייקונים SF Symbols חינמית ובשפע
- שלישיית הפריסה: VStack אנכי, HStack אופקי, ZStack עורם; Spacer הוא מרווח גמיש
- @State מעיר את הממשק לחיים; $ מספק קישור דו-כיווני לשדה הקלט
- #Preview נותן "מה שרואים זה מה שמקבלים"; צבעי המערכת מתאימים עצמם למצב הכהה; withAnimation אפקט בשורה אחת
:::
