---
id: di-liu-shi-er-zhang
num: 62
part: ios-kai-fa-pian
nav: الفصل 62: تطوير الواجهات — مدخل إلى SwiftUI
toc: default
kind: chapter
---

### الفصل 62: تطوير الواجهات — مدخل إلى SwiftUI

{class="chapter-intro mb-4"}
الواجهة هي كل ما يراه المستخدم. SwiftUI إطار واجهات «تقريري» أطلقته Apple عام 2019 — فأنت تحتاج فقط إلى «وصف» شكل الواجهة، ويتولى النظام تلقائيًا الرسم والتكيف مع الوضع الداكن والشاشات المختلفة. بحلول عام 2026 أصبح SwiftUI السائد بلا منازع في المشاريع الجديدة. في هذا الفصل سنتعلم «الرسم».

#### أولًا: فكرة SwiftUI — تقريري لا أمري

تطوير الواجهات القديم «أمري»: تخبر النظام خطوة خطوة «أنشئ زرًا → ضعه عند (20,30) → اضبط اللون». أما SwiftUI «تقريري»: تصف مباشرة «في الواجهة زر أحمر مكتوب عليه ‘اضغطني’»، أما كيف يُرسم ومتى يُعاد رسمه فالنظام يتكفل بذلك بنفسه.

::: div .code-block
:::inline div .code-head
<span>SWIFT · أول واجهة SwiftUI</span><span class="dots">···</span>
:::

```
import SwiftUI

struct ContentView: View {
    var body: some View {      // body: يصف "كيف تبدو الواجهة"
        VStack {               // مرتبة رأسيًا
            Text("مرحبًا يا عالم!")
                .font(.largeTitle)      // معدِّل: عنوان كبير
            Button("اضغط هنا") {
                print("تم الضغط!")
            }
            .buttonStyle(.borderedProminent)  // زر أزرق ممتلئ
        }
        .padding()
    }
}
```
:::

النقاط الأساسية: العرض (View) بنية تلتزم ببروتوكول View، والخاصية body تصف الواجهة، والمُعدِّلات على الصيغة .modifier() تتسلسل «كالمكياج» طبقة فوق طبقة. هذا هو كامل أساس SwiftUI.

#### ثانيًا: العروض الأساسية — نص وزر وحقل إدخال وصورة

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">العرض</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">وظيفته</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">مثال</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">عرض نص</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text("مرحبًا")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الزر</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button("اضغطني") { الإجراء }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">حقل الإدخال</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField("تلميح", text: $النص)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">عرض صورة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Image(systemName: "star.fill")</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
العروض الأساسية الأربعة في SwiftUI

لاحظ Image(systemName:) — فقد زودت Apple مكتبة أيقونات مدمجة اسمها SF Symbols (آلاف الأيقونات المجانية)، واسم مثل "star.fill" يعرض مباشرة نجمة مصمتة. هذه ميزة خفية في تطوير iOS: تكاد لا تحتاج إلى البحث عن ملفات أيقونات عند بناء الواجهات.

#### ثالثًا: ثالوث التخطيط — VStack وHStack وZStack

- VStack: ترتيب عمودي (كالاصطفاف في طابور الطعام)؛
- HStack: ترتيب أفقي (كالجلوس جنبًا إلى جنب)؛
- ZStack: تراكب (كأوراق اللعب المكدسة، مناسب للشارات والطبقات العلوية).

::: div .code-block
:::inline div .code-head
<span>SWIFT · ثلاثية التخطيط + المعدلات الشائعة</span><span class="dots">···</span>
:::

```
VStack(alignment: .leading, spacing: 12) {
    HStack {
        Text("الحساب")
        Spacer()                 // مساحة مرنة: تدفع ما على اليمين إلى النهاية
        Text("-25.5 يوان").foregroundColor(.red)
    }
    Divider()                    // خط فاصل
    Text("ملاحظة: الغداء")
}
.padding(16)                     // هامش من كل الجهات
.background(Color(.systemGray6)) // خلفية رمادية فاتحة
.cornerRadius(12)                // زوايا مستديرة

// ترتيب المعدلات مهم: padding أولًا ثم background؛ الخلفية لا تشمل الهامش
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
تنبيه: ترتيب المُعدِّلات له شأن

{class="mt-1"}
أثر padding(16).background(رمادي) يختلف عن background(رمادي).padding(16) — الأولى «تترك فراغًا ثم تلوّن» (الخلفية لا تشمل الهوامش)، والثانية «تلوّن ثم تترك فراغًا» (الخلفية تشمل الهوامش). ومن هنا يأتي «الحاشية البيضاء الغريبة» التي تربك المبتدئين أكثر من أي شيء آخر. وإذا شككت فبدّل الترتيب، وستجيبك المعاينة فورًا.
:::

#### رابعًا: الحالة والربط — كيف تنبض الواجهة بالحياة

الواجهة الثابتة بلا طعم. قاعدة SwiftUI: الواجهة تعكس الحالة بأمانة دائمًا، وإذا تغيرت الحالة أعادت الواجهة رسم نفسها تلقائيًا.

::: div .code-block
:::inline div .code-head
<span>SWIFT · عداد مع @State</span><span class="dots">···</span>
:::

```
struct CounterView: View {
    @State private var count = 0   // @State: إذا تغيرت هذه القيمة يجب إعادة الرسم

    var body: some View {
        VStack {
            Text("ضغطت \(count) مرات")
            Button("اضغط +1") {
                count += 1          // غيّر الحالة وستتحدث الواجهة تلقائيًا
            }
        }
    }
}
```
:::

حقل الإدخال يحتاج «ربطًا ثنائي الاتجاه» — فالرمز $ يمرر «القيمة وحق تعديلها» معًا:

::: div .code-block
:::inline div .code-head
<span>SWIFT · ربط ثنائي الاتجاه مع @Binding</span><span class="dots">···</span>
:::

```
struct InputView: View {
    @State private var text = ""

    var body: some View {
        TextField("اكتب شيئًا", text: $text)  // ربط ثنائي الاتجاه بـ $
            .textFieldStyle(.roundedBorder)
        Text("كتبت: \(text)")   // يتحدث فوريًا أثناء الكتابة
    }
}
```
:::

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> عملية المستخدم</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> الحالة تتغير (count += 1)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> SwiftUI يلاحظ التغير</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> يعيد رسم الواجهة (إعادة حساب body)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
شكل 3: تدفق البيانات أحادي الاتجاه في SwiftUI من «الحالة → الواجهة»
:::

#### خامسًا: المعاينة والسمات والحركة — «قوى SwiftUI الخارقة»

- ماكرو #Preview: أضف #Preview { ContentView() } في أسفل الملف، فتعرض لوحة الجانب النتيجة لحظيًا — عدّل الكود وترى النتيجة فورًا؛
- الوضع الداكن مجانًا: استخدم ألوان النظام (Color(.systemGray6) و.primary) بدلًا من تثبيت الألوان يدويًا، فيتكيف الوضع الداكن تلقائيًا دون سطر إضافي واحد؛
- الحركة بسطر واحد: withAnimation { count += 1 } أو أضف إلى العرض .animation(.default, value: count) — فتصبح الانتقالات انسيابية.

::: div .code-block
:::inline div .code-head
<span>SWIFT · رسوم متحركة في عشر دقائق</span><span class="dots">···</span>
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
نصيحة: الوظيفة أولًا ثم الحركة

{class="mt-1"}
من أكثر علات المبتدئين «الانشغال بالحركة قبل أن تصح الواجهة». اجعل الوظائف تعمل أولًا، ثم أضف المؤثرات الحركية دفعة واحدة في النهاية — فالحركة زينة تُضاف لما أُحسن، والوظيفة إغاثة تُقدَّم في وقت الحاجة. وهذا هو مبدؤنا الدائم: البساطة فوق كل شيء.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
هيا نجرّب: اصنع «زر المزاج»

#### سادسًا: مرجع سريع للمُعدِّلات الشائعة — صفحة بيدك فلا واجهة تقلقك

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ماذا تريد أن تفعل</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">المُعدِّل</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">التباعد الداخلي</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.padding(16)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الزوايا الدائرية</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cornerRadius(12)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">لون الخلفية</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.background(Color(.systemGray6))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الخط وحجمه</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.font(.title.bold())</code> / <code class="inline">.font(.system(size: 20))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">لون المقدمة (النص/الأيقونة)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.foregroundColor(.red)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ملء العرض</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(maxWidth: .infinity)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">حجم ثابت</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(width:100, height: 44)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">المحاذاة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack(alignment: .leading)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الشفافية</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.opacity(0.6)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الظل</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.shadow(radius: 5)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">إيماءة النقر</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.onTapGesture { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">نوع لوحة المفاتيح</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.keyboardType(.decimalPad)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
مرجع سريع للمُعدِّلات الشائعة في SwiftUI

لا بأس إن لم تحفظها — فهذه الصفحة موجودة للرجوع إليها. الأكثر استخدامًا في الحقيقة هي الأربعة الأولى: padding والزوايا الدائرية والخلفية والخط.

{class="mt-1"}
حوّل المشروع النموذجي إلى مبدّل مزاج: زر واحد، وعند كل نقرة يتنقل بالتناوب بين 😀 سعيد → 😢 حزين → 😡 غاضب، ويتغير معه النص ولون الخلفية. تلميح: خزّن المجموعات الثلاث (نص + لون) في مصفوفة، وخزّن الفهرس في @State، وعند النقر استخدم (index + 1) % 3. بعد الانتهاء أرسله لأصدقائك يلعبون به، واجمع موجة «واو» الأولى: «واو، أنت تصنع تطبيقات!».
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
خلاصة الفصل

- SwiftUI تقريري: تصف «الشكل المطلوب»، والنظام يتولى الرسم وإعادة الرسم
- العرض بنية تلتزم ببروتوكول View؛ وbody يصف الواجهة؛ والمُعدِّلات تتسلسل «كالمكياج»
- العروض الأساسية الأربعة: Text / Button / TextField / Image؛ ومكتبة أيقونات SF Symbols مجانية بلا حدود
- ثالوث التخطيط: VStack عمودي وHStack أفقي وZStack متراكب؛ وSpacer مساحة مرنة
- @State تجعل الواجهة حية؛ والرمز $ ربط ثنائي الاتجاه يوصل القيمة إلى حقل الإدخال
- #Preview ما تراه هو ما تحصل عليه؛ وألوان النظام تتكيف تلقائيًا مع الوضع الداكن؛ وwithAnimation حركة بسطر واحد
:::
