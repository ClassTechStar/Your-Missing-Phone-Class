---
id: di-liu-shi-qi-zhang
num: 67
part: ios-kai-fa-pian
nav: الفصل 67: الصقل والنشر — الإطلاق على App Store
toc: default
kind: chapter
---

### الفصل 67: الصقل والنشر — الاختبار والتنقيح والنشر على App Store

{class="chapter-intro mb-4"}
أنجزت التطبيق، وماذا بعد؟ يجيب هذا الفصل عن ثلاث مسائل في الطريق «من كود يعمل» إلى «منتج قابل للتسليم»: كيف تنقح بفاعلية لتجد الأخطاء، وكيف تكتب اختبارات تمنع الانتكاس، وكيف ترفع التطبيق إلى App Store ليحمّله العالم. والنشر ليس مجرد طقس — بل هو الفاصل الذي يحول عملاً إلى منتج.

#### أولًا: أدوات التنقيح الثلاث — print ونقاط التوقف والمعاينة

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الأداة</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">وظيفتها</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">كيف تستخدمها</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">print + وحدة التحكم</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">عرض سجلات التشغيل</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">في الكود اكتب print("القيمة=\(x)")، وانظر الناتج في وحدة التحكم أسفل Xcode</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">التنقيح بنقاط التوقف</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">إيقاف البرنامج عند سطر معين ومعرفة قيم المتغيرات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">انقر بجوار رقم السطر فيظهر علام زرقاء، فيتوقف التشغيل عنده، وتتقدم خطوة خطوة</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">معاينة SwiftUI + المنقح</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مشاهدة الواجهة وتسلسل العروض لحظيًا</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">لوحة #Preview + فاحص View Hierarchy أثناء التشغيل</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
أدوات التنقيح الثلاث

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
نصيحة: كيف تقرأ تقرير الانهيار؟

{class="mt-1"}
عند انهيار Swift تطبع وحدة التحكم "Fatal error" مع السبب، ويتوقف Xcode عند السطر المخطئ مبرزًا إياه. أما الانهيارات التاريخية على الجهاز الحقيقي فيمكن رؤيتها في Xcode → Window → Organizer → Crashes (يتطلب حسابًا مدفوعًا). واجعل أولوية الكلمات المفتاحية في البحث "الجملة الأولى من سبب الخطأ + swiftui" — فبالسؤال الدقيق تأتي الإجابة الدقيقة.
:::

#### ثانيًا: الاختبار — تأمين على الكود

الاختبار اليدوي لا يُعتمد — فتصلح ميزة فتتعطل أخرى بصمت. الاختبار «دواء الندم» و«السترة المضادة للرصاص» معًا. يستخدم iOS إطار XCTest وينقسم إلى نوعين:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">المستوى</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ماذا يختبر</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Target</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">السرعة</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">اختبارات الوحدات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">المنطق الصافي (الحساب والتحقق)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppTests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">بالثواني</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">اختبارات الواجهة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">سلوك الواجهة الحقيقي</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppUITests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">بالدقائق</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الاختبار اليدوي</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">إحساس وتجربة إنسان حقيقي</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">لا غنى عنه أبدًا</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
مستويات الاختبار في iOS (المشروع النموذجي يتضمن مسبقًا هدفَي اختبار Test Target)

::: div .code-block
:::inline div .code-head
<span>SWIFT · مثال اختبار وحدة</span><span class="dots">···</span>
:::

```
import XCTest

// استخرج منطق "تحويل نص المبلغ إلى رقم" كدالة نقية
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

تشغيل الاختبارات: ⌘U. وبعد أن يصير كل شيء أخضر تعدل الكود وقلبك مطمئن. والتحقق من المبالغ وحسابات الملخص في دفتر الحسابات ينبغي أن تحميها اختبارات وحدات.

#### ثالثًا: التوقيع والتغليف — ختم على التطبيق

كل تطبيق iOS يجب أن يوقع حتى يمكن تثبيته — إثباتًا أن «هذه الحزمة منك ولم يمسها تغيير». العلاقة الهرمية:

- مرحلة التعلم: Apple ID مجاني + التوقيع التلقائي في Xcode (Personal Team)، يعمل على الجهاز الحقيقي ويجدد كل 7 أيام؛
- مرحلة التوزيع: حساب مطور مدفوع (99 دولارًا سنويًا) يصدر الشهادات وملفات الوصف، وعندها فقط يمكن النشر على المتجر والتثبيت طويل الأمد.

التغليف: من قائمة Xcode اختر Product → Archive (الأرشفة)، وبعد انتهاء البناء افتح Organizer واختر Distribute App → ثم App Store Connect → ثم ارفع. يجب أن يكون هدف الأرشفة Generic iOS Device (لا المحاكي)، وهي خطوة ينساها المبتدئون كثيرًا.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
تنبيه لتجنب الفخاخ: ضياع الشهادة = انقطاع التحديثات

{class="mt-1"}
بمجرد ضياع شهادة التوقيع والمفتاح الخاص لن تستطيع إصدار تحديثات للتطبيق القديم — وسيضطر المستخدمون إلى تثبيت تطبيق «جديد كليًا». احتفظ بنسخة احتياطية من الشهادة (بتصدير .p12 من حلقة المفاتيح) واحفظ كلمة السر جيدًا. ولحسن الحظ توفر Apple «التوقيع التلقائي» وإدارة الشهادات السحابية (فعّل Automatically manage signing في Xcode)، وهو ما يجنبك معظم فخاخ العمل اليدوي.
:::

#### رابعًا: الدورة الكاملة للنشر على App Store

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> تسجيل حساب مطوّر</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> تجهيز مواد المتجر</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> رفع حزمة البناء</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> ملء معلومات الخصوصية والمراجعة</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> مراجعة Apple (1-7 أيام)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> النشر</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
شكل 5: ست خطوات للنشر على App Store
:::

- التسجيل: على developer.apple.com، حساب فردي بـ 99 دولارًا سنويًا؛
- المواد: الأيقونة (1024×1024 دون زوايا دائرية — فApple تقصها بنفسها)، واللقطات (بمقاسات iPhone المختلفة)، والوصف، ورابط سياسة الخصوصية؛
- استبيان الخصوصية: أعلن بصدق ما جمعته من بيانات — دفتر الحسابات غير المتصل بالشبكة يمكنه اختيار «لا نجمع أي بيانات»؛
- المراجعة: أول إرسال ينتظر عادة من يوم إلى سبعة، وإذا رُفض فعدّل بندًا بندًا وفق «ملاحظات المراجعة» — فأسباب الرفض من Apple تكتب عادة بتفصيل محدد، فنفذها كما هي؛
- TestFlight: قبل النشر أرسل النسخة التجريبية إلى أصدقائك للاختبار الداخلي (حتى 10000 شخص)، واجمع جولة من الملاحظات قبل الإرسال الرسمي، فتبدو احترافية تمامًا.

#### خامسًا: كيف تصنع مواد المتجر — الانطباع الأول هو عدد التنزيلات

صفحة المتجر هي واجهة المحل التي يراها المستخدم أثناء «تجوله». ثلاث مواد تحسم الانطباع الأول:

- الأيقونة: 1024×1024، ولا تكتفي بلقطة شاشة حلاً عجلاً. إن لم تملك مهارات التصميم فولّد شكلًا بسيطًا بأدوات الذكاء الاصطناعي، والمعيار أن تميزها من نظرة واحدة حتى بعد تصغيرها على سطح المكتب؛
- اللقطات: مجموعتان على الأقل (بمقاسات iPhone السائدة) تعرضان أهم مشاهد الوظائف؛ وكل لقطة معها جملة بسيطة مفهومة («سجل عملية في ثانية» أفضل بعشرة أضعاف من «حل متقدم لإدارة الحسابات»)؛
- الوصف: الجملة الأولى توضح «ما هذا + لمن هو»، ولا تكدد صفات مثل «الأكثر احترافية والأقوى» — فالصدق أنجع من المبالغة.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
هيا نجرّب: «سلّم» دفتر الحسابات مرة واحدة

#### سادسًا: قائمة مختصرة للإبلاغ عن الانهيارات وتحسين الأداء

قبل نشر التطبيق، يستحق هذان الأمران نصف ساعة لكل منهما:

##### 1. مراقبة الانهيارات

عدم انهياره في اختباراتك لا يعني أنه لن ينهار على هواتف المستخدمين. توفر Apple تقارير انهيار مجانية في Xcode Organizer (وحساب مدفوع لرؤية سجلات انهيار الأجهزة الحقيقية)؛ والحل الأريح أكثر هو دمج SDK من طرف ثالث (مثل Firebase Crashlytics). والنشر دون مراقبة للانهيارات كالقيادة والعينان مغمضتان.

##### 2. أربعة بنود لفحص الأداء

1. القوائم بـ LazyVStack أو List: لا ترص القائمة الطويلة بـ VStack العادي — فالتحميل الكسول هو الدرس الأول في الأداء؛
2. لا تدس الصور الأصلية كما هي: استخدم AsyncImage (للصور البعيدة) والتخزين المؤقت للنظام، فصورة أصلية بحجم 5MB تكفي لتختنق بها الأجهزة القديمة؛
3. لا تنجز أعمالًا ثقيلة على الخيط الرئيسي: الشبكة والملفات الكبيرة كلها عبر async/await؛
4. قس باستخدام Instruments: محلل الأداء المدمج في Xcode (Time Profiler وفحص تسريب الذاكرة) — قس أولًا ثم حسن، ولا تعتمد على الحدس.

{class="mt-1"}
① أضف ثلاث اختبارات وحدات لمنطق parseAmount ونظائره (وشغّلها بـ ⌘U حتى تخضرّ)؛ ② اصطاد بنفسك بنقطة توقف انهيارًا صنعته عمدًا وأصلحه؛ ③ أنشئ حزمة عبر Product → Archive وادعُ أصدقاءك لاختبارها عبر TestFlight؛ ④ إن وسعت سجل حساب مطور وقدّم دفتر الحسابات للنشر فعليًا. الخطوات الثلاث الأولى يمكن إنجازها الليلة.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
خلاصة الفصل

- أدوات التنقيح الثلاث: سجلات print، ونقاط التوقف، ومعاينة SwiftUI وفاحص العروض
- XCTest: اختبارات وحدات (⌘U) + اختبارات واجهة + اختبار يدوي، والمشروع النموذجي يتضمنها مسبقًا
- التوقيع: حساب مجاني بتوقيع تلقائي (يجدد كل 7 أيام)؛ والتوزيع لا يتم إلا بحساب مدفوع
- التغليف: Generic iOS Device + Archive + Distribute؛ ولا بد من نسخة احتياطية للشهادة
- النشر في ست خطوات: التسجيل → المواد → الرفع → استبيان الخصوصية → المراجعة → النشر؛ وTestFlight للاختبار الداخلي أولًا
:::
