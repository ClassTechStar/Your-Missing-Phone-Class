---
id: di-liu-shi-jiu-zhang
num: 69
part: ios-kai-fa-pian
nav: الفصل 69: الدليل المرجعي السريع والمصادر
toc: default
kind: chapter
---

### الفصل 69: دليل المراجعة السريعة والمصادر

{class="chapter-intro mb-4"}
هذا الفصل دليل مراجعة سريعة يمكن استخدامه مستقلًا. وعندما تختلط عليك صيغة ما أو تحتاج قرارًا سريعًا فافتحه مباشرة. وأنصحك بمعاملته كـ«بطاقة جيب»: مرجع سريع للكود الشائع، والمسائل المتكررة، ومصادر التعلم، دون أن تفوتك صفحة.

#### أولًا: بطاقة المراجعة السريعة للكود الشائع

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ماذا تريد أن تفعل</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الكود الأساسي</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">حالة خاصة بالصفحة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State private var x = القيمة الأولية</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">منطق عابر للصفحات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Observable class VM { var x = 0 }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تخطيط عمودي/أفقي</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack { }</code> / <code class="inline">HStack { }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مساحة مرنة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Spacer()</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">القائمة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List { ForEach(المصفوفة) { ... } }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">التنقل بين الصفحات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">NavigationStack + NavigationLink</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">نافذة منبثقة سفلية</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">.sheet(isPresented: $show) { المحتوى }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">إغلاق الصفحة الحالية</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Environment(\.dismiss) var dismiss</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">جلب البيانات عبر الشبكة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">try await URLSession.shared.data(from: url)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تحليل JSON</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X: Codable</code> + <code class="inline">JSONDecoder().decode</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تخزين إعدادات صغيرة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults.standard.set(القيمة, forKey: "المفتاح")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تخزين بيانات مهيكلة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Model</code> + <code class="inline">modelContainer</code> + <code class="inline">@Query</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">التكيف مع الوضع الداكن</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">استخدم ألوان النظام (.primary / Color(.systemGray6)) ولا تثبت الألوان يدويًا</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تشغيل الاختبارات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><kbd>⌘U</kbd></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
بطاقة مرجعية سريعة لتطوير iOS (نسخة أغسطس 2026)

#### ثانيًا: الأسئلة الشائعة FAQ

س1: لا أملك جهاز Mac، فهل أستطيع تعلّم تطوير iOS؟

يمكنك تعلّم اللغة، لكن لا يمكنك القيام بالتطوير الكامل. تطبيق Swift Playgrounds على iPad/iPhone يكفي لإتقان كامل محتوى الفصل 61؛ لكن Xcode حصري لنظام macOS، وستحتاج حتمًا إلى جهاز Mac. إن كانت ميزانيتك محدودة، يمكنك مبدئيًا استئجار Mac سحابي أو شراء Mac mini مستعمل كحل انتقالي، ثم تقرر حجم الاستثمار بعد إتقان اللغة.

س2: كم يكلّف تعلّم تطوير iOS؟

مرحلة التعلم: 0 دولار (Xcode مجاني + حساب Apple ID مجاني للتصحيح على جهاز حقيقي). مرحلة النشر: حساب مطوّر بـ 99 دولارًا سنويًا (نحو 700 يوان). أضِف إليها تكلفة جهاز Mac، وتلك هي التكلفة كاملة. وبالمقابل — حتى أداة صغيرة على App Store تجد مستخدمين يدفعون ثمنها — فالحسبة مجزية.

س3: أيّهما أتعلم أولًا: SwiftUI أم UIKit؟

SwiftUI. ففي عام 2026 تعتمد المشاريع الجديدة والدروس الجديدة والوظائف الجديدة على SwiftUI أساسًا، وهذا الكتاب يستخدمه من أوله إلى آخره. أما UIKit فهو إطار الجيل السابق وما يزال مستخدمًا في عدد كبير من المشاريع القديمة — بعد إتقانك لـ SwiftUI، أكمل تعلم UIKit حسب الحاجة (توجد دروس توافق رسمية)، وستتقنه بسرعة. لا تعكس الترتيب.

س4: هل من السهل إيجاد عمل في تطوير iOS؟

سوق 2026: الوظائف المبتدئة التي تقتصر على «رسم الواجهات» تنافسية للغاية، لكن المطوّر «الملمّ بـ Swift وSwiftUI ولديه أعمال منشورة في المتجر» ما يزال مطلوبًا بشدة. ويظل الراتب الوسيط لوظائف iOS في الصدارة بين مختلف حزم التقنيات. وأفضل سيرة ذاتية لك في مرحلة التعلم هو ذلك التطبيق الذي صنعته بنفسك والموجود في المتجر.

س5: ماذا أفعل إذا رُفض تطبيقي في المراجعة؟

لا تقلق، فهذا أمر طبيعي — احتمال رفض أول إرسال ليس قليلًا. تكون أسباب الرفض من Apple محددة جدًا عادة (أي صفحة، وأي بند من الإرشادات)، عدّل بناءً عليها بندًا بندًا ثم ردّ بالتوضيح في App Store Connect وأعد الإرسال. أكثر ثلاثة أسباب شيوعًا للرفض: غموض الغرض من الأذونات، ووجود خلل في الواجهة، وعدم تطابق البيانات الوصفية (لقطات الشاشة/الوصف) مع التطبيق الفعلي. افحص هذه البنود الثلاثة مسبقًا لتوفر على نفسك جولة انتظار.

#### ثالثًا: مرجع سريع لاختصارات Xcode الأكثر استخدامًا

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">العملية</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الاختصار</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تشغيل / اختبار</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R / ⌘U</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">فتح معاينة اللوحة (Canvas)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">فتح ملف بسرعة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">بحث شامل</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘F</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تنسيق المسافات البادئة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تعليق / إزالة التعليق</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تنظيف ذاكرة البناء المؤقتة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘K</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الانتقال إلى التعريف</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">نقر مع ⌘</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">إعادة تسمية (تغيير آمن للاسم في كل مكان)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">انقر بزر الفأرة الأيمن ثم Refactor ثم Rename</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
مرجع سريع لاختصارات Xcode الأكثر استخدامًا

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
نصيحة: إن بدت عملية التجميع «غامضة» فنظّف الذاكرة المؤقتة أولًا

{class="mt-1"}
«أمس كان يعمل واليوم لا يعمل» — في ست أو سبع حالات من كل عشر يكون السبب خللًا في ذاكرة البناء المؤقتة. نظّفها بـ ⇧⌘K ثم أعد البناء، فهذا يعالج أغلب هذه الألغاز. وإن لم ينجح الأمر فأعد تشغيل Xcode (مع جهاز Mac أيضًا)، وإن استمرت المشكلة ف«احذف مجلد DerivedData» — هذه هي الثلاثية الختامية التي يتناقلها مطوّرو iOS.
:::

#### رابعًا: مصادر التعلم الموصى بها

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">النوع</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">المصدر</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">سبب التوصية</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">رسمي</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">developer.apple.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">وثائق Apple الرسمية، وفيها دروس SwiftUI/Swift، وهي المرجع الأول الأكثر موثوقية</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">رسمي</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">دروس SwiftUI Tutorials من Apple</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">دورة رسمية خطوة بخطوة، وودّية للمبتدئين إلى أقصى حد</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">رسمي</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الموقع الرسمي للغة Swift (swift.org)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الوثائق الرسمية للغة وساحة تجربة عبر الإنترنت</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مجتمع</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hacking with Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مكتبة الدروس المجانية من Paul Hudson، وجودتها معترف بها في الصف الأول</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مجتمع</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stack Overflow (وسم swiftui)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">المحطة الأولى لطلب النجدة عند الأخطاء</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">فيديو</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">قناة Apple Developer الرسمية (فيديوهات WWDC)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">شرح موثوق للتقنيات الجديدة كل عام</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تصميم</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">دليل Apple لواجهات الإنسان والحاسوب (HIG)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">المرجع الرسمي الأقدس لصنع واجهات بروح Apple</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مكمّل لهذا الكتاب</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">القسم السابع «برمجة الذكاء الاصطناعي بالتطبيق العملي» (الفصول 37-47)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">المنهجية الكاملة للاستعانة بالذكاء الاصطناعي في تطوير iOS</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
قائمة مصادر تعلم تطوير iOS (أغسطس 2026)

#### خامسًا: الخاتمة — من أول تطبيق إلى التطبيق رقم N

بتأمل رحلتك، انتقلت من «لا أعرف ما هو SwiftUI» إلى تثبيت Xcode، وتعلم Swift، ورسم الواجهات بـ SwiftUI، وربط التطبيق بقاعدة بيانات وشبكة الإنترنت، ثم الاختبار والتغليف والنشر في المتجر — في هذا الطريق قطعتَ بالفعل أصعب مرحلة: الانتقال من الصفر إلى الواحد.

عالم التقنية يتغير بسرعة: تترقى الأطر البرمجية، وتتبدل الأدوات، ويتولى الذكاء الاصطناعي عددًا متزايدًا من مهام «الكتابة على لوحة المفاتيح». لكن ثمة شيء لا يقعض أبدًا: قدرتك على تفكيك فكرة غامضة إلى خطوات واضحة ثم تنفيذها خطوة بخطوة. الأدوات مكبِّرات، والفكر هو الأساس؛ المكبِّرات يمكن استبدالها، أما الأساس فلا يهتز.

:::inline div .quote-line
لم تعد مجرد "شخص يعرف استخدام الهاتف". يمكنك أن تحوّل أفكارك في رأسك إلى تطبيقات تعمل فعلًا على مئات الملايين من أجهزة iPhone. من اليوم، ابتكر بلوحة المفاتيح — هذه هي رومانسية مطوّري iOS.
:::

#### المراجع

{class="list-decimal pl-6 mb-3 space-y-1 text-xs text-gray-500"}
1. Apple Inc. (2026). SwiftUI Framework Documentation. developer.apple.com.
2. Apple Inc. (2026). Swift Programming Language Guide. swift.org.
3. Apple Inc. (2026). SwiftData Framework Documentation. developer.apple.com.
4. Apple Inc. (2026). App Store Review Guidelines. developer.apple.com/app-store/review.
5. Apple Inc. (2026). Human Interface Guidelines (HIG). developer.apple.com/design.
6. Apple Inc. (2026). Xcode 27 Release Notes and App Distribution Guide.
