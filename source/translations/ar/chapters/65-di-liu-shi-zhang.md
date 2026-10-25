---
id: di-liu-shi-zhang
num: 60
part: ios-kai-fa-pian
nav: الفصل 60: تهيئة بيئة التطوير — Xcode وأول مشروع
toc: default
kind: chapter
---

### الفصل 60: تجهيز بيئة التطوير — Xcode وأول مشروع

{class="chapter-intro mb-4"}
من أراد أن يُتقن عمله أتقن أدواته أولاً. في هذا الفصل سنجهز «المطبخ»: نثبّت Xcode ونشغّل المحاكي وننشئ أول مشروع iOS في حياتك، ثم نفكك بنية المشروع نفهمها فهماً تاماً. وبعد تجهيز البيئة سترى لأول مرة كودك يتحول إلى زر يمكن النقر عليه — لحظة يتذكرها كثير من الناس طول العمر.

#### أولاً: تجهيز جهاز Mac

لنبدأ بالعقبة: تطوير iOS لا يكون إلا على macOS. إن لم تكن تملك Mac فخياراتك ثلاثة: شراء جهاز (يكفي Mac mini أو MacBook Air حتى مستعملاً)، أو استئجار Mac سحابي لفترة قصيرة، أو قراءة القسم الثامن أولاً «التطبيق العملي لتطوير Android» (يمكن العمل عليه من Windows).

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">بند الإعداد</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الحد الأدنى</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">المستوى المريح (موصى به)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الشريحة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Silicon (من M1 فصاعداً)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">M2 وأحدث</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الذاكرة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8GB</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">16GB</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">القرص</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">احجز 40 غيغابايت فأكثر (فـ Xcode نفسه ضخم)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256 غيغابايت على الأقل</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">النظام</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">أحدث macOS</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">فعّل التحديث التلقائي</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
مرجع مواصفات جهاز تطوير Mac (أغسطس 2026)

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
نصيحة: يمكن تعلم اللغة أولاً دون Mac

{class="mt-1"}
تطبيق Swift Playgrounds المجاني على iPad يتيح تعلم أساسيات لغة Swift (دون حاجة إلى Mac)؛ بل يمكن تثبيته حتى على iPhone. أتقن أولاً المعرفة اللغوية للفصل 61 داخل Playgrounds، وعندما تحصل على Mac ستقلع مباشرة. من شحذ فأسه لم يضيّع وقت الحطب — وهذا هو المقصود بالضبط.
:::

#### ثانياً: تثبيت Xcode

Xcode هي بيئة التطوير المتكاملة الرسمية من Apple وهي مجانية. ثلاث خطوات للتثبيت:

1. افتح App Store على Mac وابحث عن "Xcode" وانقر التثبيت — انتبه فهو بحجم عدة غيغابايتات، فاختر وقتاً تكون فيه الشبكة سريعة؛
2. عند أول تشغيل بعد التثبيت وافق على الاتفاقية واترك المكونات تكتمل (يتم تلقائياً)؛
3. من القائمة Xcode ← Settings ← Locations تأكد من اختيار Command Line Tools — فأدوات سطر الأوامر شرط مسبق للعديد من السكربتات والأدوات الخارجية.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
تنبيه: «لعبة التوافق» بين الإصدار والنظام

{class="mt-1"}
Xcode الجديد يطالب غالباً بأحدث macOS، بينما Mac القديم يعلق في الإصدارات القديمة. وعند النشر على App Store تطلب Apple بناء التطبيق بـ Xcode أحدث (مع مهلة سماح عادة). فلا تماطل طويلاً في تحديث النظام — مطورو iOS من أكثر الناس تتبعاً للإصدارات الجديدة.
:::

#### ثالثاً: إنشاء أول مشروع لك

افتح Xcode ← Create New Project ← اختر iOS ← قالب App ثم املأ:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">بند الإعداد</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ماذا تكتب</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">التوضيح</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Product Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstApp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">اسم التطبيق</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">معرّف Apple ID الخاص بك (مجاني)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">يستخدم للتوقيع، والحساب الفردي يكفي</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Organization Identifier</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">يتحد مع Product Name ليكوّن معرّف الحزمة</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interface</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">إطار خط هذا الكتاب الرئيسي</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Language</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">لا يحتاج إلى شرح</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
خمسة بنود تملؤها عند إنشاء المشروع

بعد النقر على Create سيولّد Xcode مشروعاً يعمل مباشرة. اختر محاكياً من الزاوية العلوية اليسرى (مثل iPhone 17) وانقر ▶ للتشغيل — بعد ثوانٍ تظهر في شاشة المحاكي نافذة مكتوب فيها "Hello, world!". لقد وُلد أول تطبيق iOS لك.

#### رابعاً: تشريح بنية المشروع — ما وظيفة كل ملف

على اليسار متصفح المشروع، ويكفي المبتدئ معرفة هذه فقط:

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="290" viewBox="0 0 600 290" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="290" fill="#fafafa" rx="8"/>
      <text x="20" y="28" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ جذر المشروع</text>
      <rect x="30" y="42" width="540" height="225" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <rect x="45" y="56" width="250" height="196" fill="#eef2ff" rx="5"/>
      <text x="56" y="78" font-size="11" fill="#1e1b4b" font-weight="bold">MyFirstApp/ (مجلد الكود)</text>
      <text x="66" y="100" font-size="10" fill="#374151">├ MyFirstAppApp.swift  ← نقطة الدخول</text>
      <text x="66" y="120" font-size="10" fill="#374151">├ ContentView.swift  ← الواجهة الرئيسية</text>
      <text x="66" y="140" font-size="10" fill="#374151">└ Assets.xcassets  ← أيقونات وصور وألوان</text>
      <text x="56" y="166" font-size="10" fill="#6b7280">(الملفات الجديدة توضع في هذا المجلد)</text>
      <text x="56" y="196" font-size="10" fill="#1e1b4b" font-weight="bold">تبويب Info / Info.plist</text>
      <text x="66" y="216" font-size="10" fill="#6b7280">إعلان التطبيق: الاسم، الأذونات، الإعدادات</text>
      <rect x="310" y="56" width="245" height="196" fill="#f0fdf4" rx="5"/>
      <text x="321" y="78" font-size="11" fill="#065f46" font-weight="bold">أماكن مهمة أخرى</text>
      <text x="331" y="100" font-size="10" fill="#374151">📁 Preview Content/  ← مواد المعاينة</text>
      <text x="331" y="122" font-size="10" fill="#374151"><i class="fas fa-bullseye mr-1"></i> إعدادات الهدف (أيقونة المشروع الزرقاء)</text>
      <text x="331" y="142" font-size="10" fill="#6b7280">——الإصدار والنظام الأدنى والتوقيع كلها هنا</text>
      <text x="331" y="168" font-size="10" fill="#374151"><i class="fas fa-flask mr-1"></i> MyFirstAppTests/  ← اختبارات الوحدات</text>
      <text x="331" y="188" font-size="10" fill="#374151">📱 MyFirstAppUITests/ ← اختبارات الواجهة</text>
      <text x="331" y="216" font-size="10" fill="#9ca3af">(قالب الاختبارات جاهز، يُستخدم في الفصل 67)</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
الشكل 2: بنية مشروع Xcode التي يجب على المبتدئ فهمها
:::

- MyFirstAppApp.swift: نقطة دخول البرنامج، وفي SwiftUI لا يتجاوز بضعة أسطر — «ابدأ ثم اعرض الواجهة الرئيسية»؛
- ContentView.swift: عرض الواجهة الرئيسية، وكل ما تراه الآن موجود هنا؛
- Assets.xcassets: مخزن الموارد — الأيقونات والصور والألوان توضع هنا؛
- إعدادات Target: انقر أيقونة المشروع الزرقاء على اليسار للدخول، فداخلها رقم الإصدار وأدنى إصدار iOS والتوقيع. ومن هنا أيضاً تُضبط الاسم الظاهر للتطبيق والأيقونة.

#### خامساً: حيل إتقان Xcode — خمس «إضافات اختصارات» للمبتدئ

أتقن هذه جيداً وستبدو «محترفاً جداً»:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الإجراء</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الاختصار</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الوظيفة</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">التشغيل</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تصريف التطبيق وتشغيله</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">فتح/تبديل معاينة اللوحة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مفتاح «ما تراه هو ما تحصل عليه»</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تنسيق المسافات البادئة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ترتيب مسافات الكود المحدد تلقائياً</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">فتح الملفات بسرعة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">اكتب اسم الملف فيُفتح فوراً (الأكثر استخداماً!)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تعليق/إلغاء تعليق</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تعطيل وتمكين الأسطر بسرعة أثناء التصحيح</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
اختصارات Xcode الأكثر استخداماً (خمسة للمبتدئ)

وميزتان خفيتان إضافيتان: تشغيل أكثر من محاكي (لتشغيل iPhone وiPad معاً ومقارنة التخطيط) ومكتبة مقتطفات الكود (اسحب الأسطر الشائعة إلى لوحة Snippets على اليمين لتدرجها لاحقاً بنقرة واحدة) — استخدم أدوات الإتقان من الآن وستتحسن براعتك تلقائياً.

#### سادساً: التصحيح على الجهاز الحقيقي — تثبيت التطبيق في iPhone الخاص بك

المحاكي جيد لكن الجهاز الحقيقي هو المحطة النهائية. ويمكن التصحيح على جهاز حقيقي بمعرّف Apple ID مجاني:

1. وصّل iPhone بكابل البيانات (أو صحّح لاسلكياً عبر شبكة Wi-Fi نفسها)؛
2. اختر هاتفك من قائمة الأجهزة أعلى Xcode، وفي المرة الأولى سيُطالبك بتسجيل الدخول إلى Apple ID ويضبط التوقيع تلقائياً؛
3. في iPhone: [الإعدادات] ← [عام] ← [VPN وإدارة الأجهزة] ← ثق بشهادة المطوّر الخاصة بك؛
4. انقر ▶ فيُثبَّت التطبيق على الجهاز الحقيقي.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
تنبيه: «قيد الأيام السبعة» للحساب المجاني

{class="mt-1"}
التطبيق الموقّع بمعرّف Apple ID مجاني يبطل بعد 7 أيام (يُجدد بمجرد إعادة التشغيل مرة واحدة). هذه آلية Apple لمنع إساءة الاستخدام وتكفي تماماً في مرحلة التعلم؛ أما حساب المطور المدفوع (99 دولاراً في السنة) فلا يخضع لهذا القيد، والتفصيل في الفصل 67.
:::

#### سابعاً: أول تجربة + إسعاف الأخطاء الشائعة

افتح ContentView.swift واستبدل الكلمة في Text("Hello, world!") باسمك واضغط ⌘R لإعادة التشغيل — بعد ثوانٍ سيظهر اسمك على المحاكي. مبروك، لقد أتممت أول دورة كاملة «تعديل الكود ← التصريف ← التثبيت ← التشغيل».

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ظاهرة الخطأ</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">السبب الشائع</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">العلاج</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">خطأ Signing</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">عدم اختيار Team أو انتهاء صلاحية الشهادة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">فعّل حسابك في Target ← Signing؛ وأعد التشغيل مرة واحدة للحساب المجاني</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">شاشة المحاكي سوداء أو لا يفتح</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">صورة النظام تالفة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">من القائمة Device ← Erase All Content؛ أو احذف المحاكي وأضفه من جديد</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تحميل Xcode بطيء أو يفشل التثبيت</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تذبذب الشبكة في App Store</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">جرّب وقتاً آخر؛ أو نزّل حزمة .xip دون اتصال من موقع مطوري Apple</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
جدول إسعاف أخطاء البيئة للمبتدئين

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
لنطبّق: أتمم قائمة «طقوس التطوير» الخاصة بك

{class="mt-1"}
① ثبّت Xcode وشغّل المحاكي بنجاح؛ ② شغّل تطبيقك على جهاز حقيقي مرة والتقط صورة تذكارية؛ ③ استبدل كلمة Hello باسمك؛ ④ من إعدادات Target غيّر الاسم الظاهر للتطبيق إلى «تطبيقي الأول». بإتمام هذه الخطوات الأربع تصبح صاحب عمل منجز.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
خلاصة الفصل

- العقبة الصلبة: Mac + Xcode؛ وإن لم يتوفر Mac فتعلم اللغة أولاً عبر Swift Playgrounds على iPad
- ثبّت Xcode من App Store؛ الإصدار الجديد يطالب بنظام جديد، فلا تماطل في التحديث
- عناصر المشروع الجديد الخمسة: الاسم وTeam ومعرّف المؤسسة وSwiftUI وSwift
- قاعدة المشروع: الكود كله في مجلد MyFirstApp/؛ وإعدادات Target تتكفل بالإصدار والتوقيع
- التصحيح على جهاز حقيقي بمعرّف Apple ID مجاني خاضع لقيد توقيع 7 أيام؛ والحساب المدفوع بلا هذا القيد
- روتين التطوير = عدّل الكود ← ⌘R ← شاهد النتيجة، في دورة متجددة
:::
