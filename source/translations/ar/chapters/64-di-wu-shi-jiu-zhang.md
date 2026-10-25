---
id: di-wu-shi-jiu-zhang
num: 59
part: ios-kai-fa-pian
nav: الفصل 59: تعرف على iOS — منظومة Apple ومنظومة التطوير
toc: default
kind: chapter
---

### الفصل 59: التعرف على iOS — بيئة Apple وبيئة التطوير

{class="chapter-intro mb-4"}
مبارك لك هذا القرار — أن تتحول من «مستخدم لـ iPhone» إلى «كاتب تطبيقات لـ iPhone». وقبل الشروع في العمل، لنفرش الخريطة: من أين جاء iOS؟ ماذا تعني «الحديقة المسوّرة» لـ Apple بالنسبة إلى المطورين؟ وماذا يجري بين أن تكتب الكود بأصابعك وأن يصل التطبيق إلى هاتف المستخدم؟

#### أولاً: نشأة iOS — هاتف واحد يغيّر صناعة كاملة

في يناير 2007 أخرج جوبز أول iPhone في مؤتمر الإعلان. ولم يكن يدعم عندئذ حتى تطبيقات الأطراف الثالثة — حتى أطلقت Apple في 2008 متجر App Store وحزمة iPhone SDK وسمحت لمطوري العالم بكتابة البرامج لـ iPhone. في تلك اللحظة وُلد «اقتصاد التطبيقات»: حتى اليوم يضم App Store ملايين التطبيقات، وتجاوزت الحصص المدفوعة للمطورين تراكمياً مئات المليارات من الدولارات.

النظام نفسه يتطور أيضاً: سُمي في البداية iPhone OS ثم تغيّر اسمه إلى iOS في 2010؛ وتقدّمت الأرقام حتى iOS 17 (2023)، ثم غيّرت Apple في 2025 التسمية لتتبع السنة — أُطلق iOS 26 في 2025، والإصدار الحالي في أغسطس 2026 هو iOS 27. تتغير التسميات، لكن أمراً واحداً لم يتغير: عادة المستخدمين في الدفع وسمعة جودة البرمجيات في iOS هما الأفضل إجماعاً في بيئة الهواتف المتنقلة — التطبيق نفسه يدرّ على iOS دخلاً أعلى في الغالب بوضوح من نظيره على Android.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">المحطة</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">السنة</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ما يهم المطورين</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">إطلاق App Store</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2008</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">انطلاق بيئة تطوير الأطراف الثالثة</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">إطلاق Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2014</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ظهور لغة تطوير iOS الحديثة</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">إطلاق SwiftUI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2019</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">إطار واجهات تصريحي، وهو خط هذا الكتاب الرئيسي</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">iOS 26 (العام الأول للتسمية الجديدة)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2025</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">التسمية تتبع السنة؛ ودمج شامل لـ Apple Intelligence</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">iOS 27</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2026</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">أحدث إصدار حالي (مرجع هذا الكتاب)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
محطات بارزة في تطوير iOS (حتى أغسطس 2026)

#### ثانياً: الحديقة المسوّرة — «قواعد» بيئة Apple و«أرباحها»

توصف بيئة Apple كثيراً بأنها «حديقة مسوّرة» (Walled Garden) — قواعد كثيرة ورقابة صارمة: لا يُنشر التطبيق إلا بعد المراجعة، ولا يجوز التطوير إلا بـ Mac وXcode، والتوزيع يجري أساساً عبر App Store. يبدو ذلك خانقاً؟ لكن هذه القواعد جلبت للمطورين أرباحاً حقيقية ملموسة:

- تفتت الأجهزة ضئيل جداً: طرازات iPhone معدودة، ومقاسات الشاشة وإصدارات النظام متجانسة للغاية — تكيّف مع 5 طرازات فتغطي 95% من المستخدمين (بينما قد يتطلب Android التكيف مع عشرات الطرازات)؛
- نسبة تحديث إصدارات النظام عالية جداً: خلال أسابيع من إطلاق نظام جديد يرقّي إليه سبعون إلى ثمانون في المئة من المستخدمين، فيمكنك استخدام واجهات API الجديدة بجرأة دون مراعاة «نظام قديم عمره خمس سنوات»؛
- عادة الدفع جيدة: مستخدمو App Store أعدّ للإنفاق على التطبيقات والمشتريات الداخلية؛
- المراجعة صارمة لكن المتجر نظيف: القلّادات والبرامج الشريرة قليلة، فالمنتجات الجيدة أسهل في أن تُرى.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
تنبيه: لنوضح التكلفة أولاً

{class="mt-1"}
لتطوير iOS عقبة صلبة: تحتاج جهاز Mac (فـ Xcode حصري لـ macOS)، والنشر يتطلب حساب مطوّر بـ 99 دولاراً في السنة (حساب المطور الفردي المجاني يكفي للتصحيح على جهاز حقيقي محلياً لكنه لا يصلح للنشر). فكّر جيداً في هذا الاستثمار قبل الانطلاق — لكن الخبر السار أن الحساب المجاني يكفي تماماً في مرحلة التعلم، وسيفصّل ذلك الفصل 60.
:::

#### ثالثاً: بأي لغة نكتب — Objective-C أم Swift؟

في تاريخ تطوير iOS بطلا «رئيسيان» أيضاً. Objective-C هو الشيخ المؤسس — استُخدم من 2008 إلى 2014؛ وSwift هي اللغة الجديدة التي أطلقتها Apple في 2014، وتطورت بعدها حتى Swift 6 (أُطلقت في 2024 وأدخلت فحص تزامن صارماً)، وفي 2026 تستخدم Swift المشاريع الجديدة على وجه التقريب كلها.

كلمة صادقة لك وأنت في الصفر: تعلّم Swift مباشرة، ولا تنظر إلى Objective-C حتى — إلا إذا احتجت بعد التوظيف إلى صيانة كود تراثي من عشر سنوات. مزايا Swift: صياغة نقية (بلا أقواس منقوطة ولا أعباء ملفات الترويسة من عصر C)، وآلية القيم الاختيارية (Optional) التي أبادت «انهيار المؤشر الفارغ» من مستوى اللغة نفسها، وتكامل سلس مع SwiftUI، فضلاً عن Swift Playgrounds على iPad للتعلم واللعب معاً.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
نمط Objective-C (أطلال قديمة)

{class="font-mono text-xs leading-relaxed"}
NSString *name = @"أحمد"; [name stringByAppendingString:@"مرحبا"]; // الأقواس المعقوفة والمؤشرات والفواصل المنقوطة — ثلاثية كاملة
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
نمط Swift (عصري ونقي)

{class="font-mono text-xs leading-relaxed"}
var name = "أحمد" name += "مرحبا" // واضح ومباشر كاللغة الطبيعية
:::
:::

#### رابعاً: كيف يولد التطبيق؟

ككل المنصات، لولادة تطبيق iOS خط إنتاج أيضاً. لكن نسخة Apple فيها «فحصان» إضافيان:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-lightbulb mr-1"></i> فكرة</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center">📐 التصميم (الواجهة + الوظائف)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-keyboard mr-1"></i> كتابة الكود (Swift + SwiftUI)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hammer mr-1"></i> البناء والتوقيع</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> الاختبار (محاكي + جهاز حقيقي)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-stamp mr-1"></i> مراجعة Apple</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> النشر في App Store</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
الشكل 1: المسار الكامل لتطبيق iOS من الفكرة إلى النشر (لاحظ مرحلة «المراجعة» الإضافية)
:::

مفاهيم أساسية في المسار:

- التوقيع (Signing): كل تطبيق iOS يجب أن يُوقَّع ليُثبَّت — إثباتاً بأن «هذه الحزمة منك ولم يُعبث بها». في مرحلة التعلم يوقّع Xcode تلقائياً بمعرّف Apple ID الخاص بك، وعند النشر تُستخدم شهادة المطور. التفصيل في الفصل 67.
- المحاكي (Simulator): جهاز iPhone افتراضي على Mac وساحة العمل الرئيسية للتطوير والتصحيح. يعمل بمعالج Mac نفسه، لذا فهو سلس للغاية وتجربته أفضل بكثير من محاكي Android.
- TestFlight: أداة Apple الرسمية «لتوزيع الاختبار الداخلي» — تُرسل قبل النشر نسخة تجريبية إلى ما يصل إلى 10000 مستخدم اختبار يثبّتونها ويجربونها عبر تطبيق TestFlight. وهذه أناقة يفرد بها iOS وحده.

#### خامساً: منظومة تقنيات iOS الكاملة — «قائمة أسلحتك»

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الطبقة</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الخيار السائد (2026)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ما استخدامه</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">اللغة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift 6</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">لغة كتابة المنطق</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الواجهة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI + دليل تصميم Apple (HIG)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">رسم الواجهة بالكود (خط هذا الكتاب الرئيسي)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">البنية</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MVVM + @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">فصل الواجهة عن المنطق</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تخزين البيانات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData (قاعدة البيانات) + UserDefaults (الإعدادات)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">حفظ البيانات في الهاتف</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الشبكة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession + async/await + Codable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">التواصل مع الخادم</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">أداة البناء</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode Build System / xcodebuild</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تحويل الكود إلى حزمة تثبيت</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">بيئة التطوير</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode (حصري لـ macOS)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">بيئة التطوير المتكاملة الرسمية من Apple</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
نظرة سريعة على منظومة تقنيات iOS السائدة في 2026

هل لاحظت؟ هذه القائمة أقصر من قائمة Android — لأن Apple «تكفل» بأمور كثيرة. ثمن البيئة المغلقة هو حرية أقل، ومكافأتها راحة البال: لا تتحير في اختيار مكتبة الشبكة أو قاعدة البيانات، فما تقدمه الجهة الرسمية هو غالباً الحل الأمثل.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
لنطبّق: ألقِ نظرة على «هوية Apple» في هاتفك

{class="mt-1"}
افتح في iPhone [الإعدادات] ← [عام] ← [حول]، وسجّل ثلاثة أمور: إصدار iOS واسم الطراز والمساحة المتاحة. ثم تجول على صفحة «اليوم» في App Store وراقب لقطات شاشة التطبيقات المميزة ونصوصها — فمن اليوم يتغير منظرك في المتجر من «مستخدم» إلى «مطور».
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
خلاصة الفصل

- في 2008 أُطلق App Store ووُلد «اقتصاد التطبيقات»؛ والإصدار الحالي في 2026 هو iOS 27
- حساب الحديقة المسوّرة: قواعد كثيرة، لكن أجهزة قليلة وإصدارات جديدة ومستخدمون يبذلون المال ومتجر نظيف
- العقبة الصلبة: Mac ضروري؛ والنشر يتطلب حساب مطوّر بـ 99 دولاراً سنوياً؛ والحساب المجاني يكفي في مرحلة التعلم
- تعلّم Swift مباشرة؛ فـ Objective-C لا يخص إلا الكود التراثي
- خط الإنتاج أطول بخطوة من Android: مراجعة Apple؛ وTestFlight أداة توزيع الاختبار الداخلي المذهلة
- منظومة 2026 القياسية: Swift 6 + SwiftUI + MVVM + SwiftData + URLSession + Xcode
:::
