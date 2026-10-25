---
id: di-si-shi-jiu-zhang
num: 49
part: an-zhuo-kai-fa-pian
nav: الفصل 49: تهيئة بيئة التطوير — Android Studio وأول مشروع
toc: default
kind: chapter
---

### الفصل 49: تجهيز بيئة التطوير — Android Studio وأول مشروع

{class="chapter-intro mb-4"}
من أراد أن يُتقن العمل أتقن أدواته أولًا. في هذا الفصل سنجعل «المطبخ» جاهزًا: نثبّت Android Studio، ونشغّل المحاكي بنجاح، وننشئ أول مشروع Android في حياتك، ثم نفكك بنية المشروع لنفهمها فهمًا واضحًا. وبعد تجهيز البيئة ستشاهد لأول مرة كودك يتحول إلى زر يمكنك النقر عليه — لحظة يتذكرها كثيرون طوال العمر.

#### أولًا: تثبيت Android Studio

Android Studio هي بيئة التطوير المتكاملة (IDE) الرسمية من جوجل، مجانية وشاملة الوظائف: كتابة الكود، ومعاينة الواجهة، وتصحيح الأخطاء، وحزم التطبيق، كل ذلك في مكان واحد. التثبيت في أربع خطوات:

1. افتح الموقع الرسمي developer.android.com/studio ونزّل أحدث إصدار مستقر (في أغسطس 2026 كان الإصدار الذي يلي Narwhal، وهو متاح لأنظمة Windows/Mac/Linux)؛
2. شغّل ملف التثبيت واختر «التالي» طوال الطريق — سيثبّت المعالج تلقائيًا مكونات Android SDK والمحاكي؛
3. عند أول تشغيل نزّل مكونات SDK حسب التعليمات (اترك الخيارات الافتراضية كما هي؛ قد يستغرق الأمر بضع دقائق وبضعة جيجابايت من المساحة)؛
4. بعد الانتهاء ستظهر لك صفحة الترحيب — تهانينا، أصبح «المطبخ» جاهزًا.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
تنبيه: خذ متطلبات العتاد بعين الاعتبار

{class="mt-1"}
Android Studio «آكلة للذاكرة»: يُنصح بذاكرة 16 جيجابايت في الحد الأدنى (يعمل بـ 8 جيجابايت لكن المحاكي سيتقطع كثيرًا)، مع حجز أكثر من 20 جيجابايت على القرص، ومعالج يدعم المحاكاة الافتراضية (فعّل VT-x/AMD-V من BIOS). إذا كان حاسوبك قديمًا فعلًا، يمكنك استخدام «التصحيح على جهاز حقيقي» بدلًا من المحاكي (سأشرحه في القسم الرابع من هذا الفصل)، وقد تكون التجربة عندها أكثر سلاسة.
:::

#### ثانيًا: إنشاء أول مشروع لك

من صفحة الترحيب انقر New Project واختر قالب Empty Activity (أنظف قالب للمبتدئين)، ثم املأ ثلاثة أشياء:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">بند الإعداد</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ماذا تملأ</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الشرح</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">My First App</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">اسم التطبيق، ويظهر على الشاشة الرئيسية للهاتف</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Package name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example.myfirstapp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">معرّف فريد عالميًا، والعادة هي «عكس ترتيب اسم النطاق»، اتركه الافتراضي في البداية</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minimum SDK</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API 26(Android 8.0)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الحد الأدنى للإصدارات المدعومة، ويغطي أكثر من 95% من الأجهزة</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
الأشياء الثلاثة المطلوب ملؤها عند إنشاء المشروع

بعد النقر على Finish سيستخدم Android Studio أداة Gradle لتنزيل الاعتماديات وبناء المشروع تلقائيًا (المرة الأولى تستغرق بضع دقائق، وبعدها تصبح أسرع بكثير). وبعد اكتمال البناء سيكون لديك تطبيق قابل للتشغيل — وإن كان لا يعرض سوى سطر "Hello Android!".

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
نصيحة: أسرار اسم الحزمة

{class="mt-1"}
اسم الحزمة (package name) يشبه «رقم الهوية» للتطبيق؛ لا يجوز تكراره عالميًا، وبعد النشر لا يمكن تغييره. للتمارين الشخصية يكفي com.example.xxx؛ أما المنتجات الرسمية فيجب أن تحمل عكس ترتيب نطاقك الخاص (مثل com.اسمك.اسمالتطبيق). لا تنشر تطبيقًا باسم com.example — فالمتجر سيرفضه.
:::

#### ثالثًا: لنشغّله: المحاكي والجهاز الحقيقي

بعد كتابة الكود، نحتاج «هاتفًا» نشغّل عليه. أمامك خياران:

##### 1. المحاكي (Emulator)

المحاكي ينشئ هاتف Android افتراضيًا داخل حاسوبك. في Android Studio افتح Device Manager ثم Create Device، واختر جهازًا (يُنصح بسلسلة Pixel) ثم صورة نظام (من النوع الذي يتضمن Google APIs) ثم نزّلها وشغّلها. بعدها انقر المثلث الأخضر Run في شريط الأدوات، وخلال ثوانٍ ستظهر على شاشة «الهاتف» واجهة تطبيقك.

##### 2. التصحيح على جهاز حقيقي (الأكثر توصية)

الجهاز الحقيقي يبقى بيئة الاختبار الأكثر واقعية — انسياب اللمس والشبكة الحقيقية والمستشعرات الحقيقية لا يشبهها المحاكي فيها شيء. والتصحيح على هاتف Android حقيقي بسيط جدًا:

1. في الهاتف افتح [الإعدادات] > [حول الهاتف]، وانقر «رقم الإصدار» 7 مرات متتالية لتفعيل «خيارات المطوّر»؛
2. في [خيارات المطوّر] فعّل تصحيح USB؛
3. وصّل الهاتف بالحاسوب بكابل بيانات، واختر «السماح بتصحيح USB» من النافذة المنبثقة؛
4. عُد إلى Android Studio وسيظهر هاتفك في قائمة الأجهزة المنسدلة في شريط الأدوات، ثم انقر Run.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
تحذير من الفخاخ: لا تُبقِ تصحيح USB مفعّلًا دائمًا

{class="mt-1"}
تصحيح USB يشبه فتح «باب خلفي» لحاسوبك. عند الشحن في الأماكن العامة أو الاتصال بحواسيب لا تثق بها، احرص على إيقاف تصحيح USB لمنع الآخرين من قراءة بياناتك عبره. أغلقه بعد كل استخدام أثناء التطوير، حتى يصبح عادة راسخة.
:::

#### رابعًا: تفكيك بنية المشروع: ما وظيفة كل ملف

عند فتح المشروع لأول مرة قد تُذهلك شجرة الملفات على اليسار. لا تقلق؛ في التطوير اليومي ستقضي 90% من وقتك مع الملفات التالية فقط:

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="300" viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="300" fill="#fafafa" rx="8"/>
      <text x="20" y="30" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ جذر المشروع</text>
      <rect x="30" y="45" width="540" height="230" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <text x="45" y="70" font-size="11" fill="#4f46e5" font-weight="bold">app/ ← حيث تكتب الكود</text>
      <rect x="60" y="82" width="240" height="178" fill="#eef2ff" rx="5"/>
      <text x="70" y="102" font-size="10" fill="#1e1b4b" font-weight="bold">src/main/</text>
      <text x="80" y="120" font-size="10" fill="#374151">├ java/…/MainActivity.kt  ← الكود المنطقي</text>
      <text x="80" y="138" font-size="10" fill="#374151">├ res/  ← الموارد (صور ونصوص وألوان)</text>
      <text x="80" y="156" font-size="10" fill="#374151">└ AndroidManifest.xml  ← "بطاقة هوية" التطبيق</text>
      <text x="70" y="180" font-size="10" fill="#1e1b4b" font-weight="bold">build.gradle.kts</text>
      <text x="80" y="198" font-size="10" fill="#6b7280">يعلن عن المكتبات المعتمدة (إصدار SDK و Compose وغيرها)</text>
      <text x="70" y="222" font-size="10" fill="#1e1b4b" font-weight="bold">src/androidTest/ و test/</text>
      <text x="80" y="240" font-size="10" fill="#6b7280">كود اختبارات مؤتمتة (يُستخدم في الفصل 56)</text>
      <rect x="320" y="82" width="230" height="178" fill="#f0fdf4" rx="5"/>
      <text x="330" y="102" font-size="10" fill="#065f46" font-weight="bold">ملفات أخرى في الجذر</text>
      <text x="340" y="122" font-size="10" fill="#374151">gradle/ + gradlew.bat  ← سكربتات البناء</text>
      <text x="340" y="142" font-size="10" fill="#374151">settings.gradle.kts  ← إعدادات المشروع</text>
      <text x="340" y="162" font-size="10" fill="#6b7280">(قاعدة المبتدئين: العب فقط بمجلد app/،</text>
      <text x="340" y="180" font-size="10" fill="#6b7280">اعتبر الباقي "صندوق أسود" ولا تلمسه)</text>
      <text x="340" y="208" font-size="10" fill="#9ca3af">.gitignore  ← قائمة التجاهل الخاصة بتحكم الإصدارات</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
الشكل 2: بنية المشروع التي يجب على المبتدئ فهمها (القاعدة الذهبية: لا تلمس سوى مجلد app/)
:::

- MainActivity.kt: «البوابة الرئيسية» للتطبيق. عندما ينقر المستخدم على الأيقونة فهو أول ما يُيقظ. في القوالب الحالية مسؤوليته عرض "Hello Android!".
- AndroidManifest.xml: «سجل القيد» للتطبيق — يصرّح باسم التطبيق وأيقونته وصفحاته والأذونات التي يحتاجها (الكاميرا، تحديد الموقع وغيرها).
- مجلد res/: مستودع الموارد، يخزن الصور والأيقونات والنصوص والألوان. وضع النصوص في ملفات الموارد بدلًا من تثبيتها في الكود عادة جيدة في تطوير Android (يسهل بها تغيير اللغة والمظهر).
- build.gradle.kts: وصفة البناء — تصريح الحد الأدنى للإصدارات والاعتماديات المطلوبة (مثل Compose).

#### خامسًا: تجربة أولى: استبدل "Hello" باسمك

افتح MainActivity.kt وسترى الكود الذي ولّده قالب Compose. ابحث عن السطر Text("Hello Android!") واستبدل ما بين علامتي التنصيص باسمك، مثل Text("مرحبًا، أنا أحمد! هذا أول تطبيق لي")، ثم اضغط Ctrl+R (أو Cmd+R على Mac) لإعادة التشغيل. وبعد ثوانٍ سيظهر اسمك على المحاكي.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · MainActivity.kt (غيّر هذا السطر)</span><span class="dots">···</span>
:::

```
setContent {
    MyFirstAppTheme {
        Surface(modifier = Modifier.fillMaxSize()) {
            // ▼ غيّر هنا إلى النص الذي تريده
            Text("مرحبًا أحمد! هذا أول تطبيق لي")
        }
    }
}
```
:::

تهانينا؛ لقد أكملت دورة كاملة "تعديل الكود ← تجميع ← تثبيت ← تشغيل". هذه الدورة هي روتين التطوير اليومي مستقبلًا. اجعل الحديد ساخنًا وجرّب تعديل أشياء أخرى: كبّر حجم الخط أو غيّر اللون — في الفصل القادم سنتعلم من أين تأتي هذه "التعاويذ".

#### سادسًا: إسعافات أولية للأخطاء الشائعة: "قسم الطوارئ" لأول أسبوعين للمبتدئ

في مرحلة تجهيز البيئة وأول بناء ستقابل على الأرجح الأخطاء الثلاثة التالية. لا تذعر؛ لكل منها علاج:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">شكل الخطأ</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">السبب الشائع</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">العلاج</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">فشل مزامنة Gradle / بطء تنزيل الاعتماديات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ضعف الوصول الشبكي إلى المستودعات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">اضبط Gradle لاستخدام مستودعات مرايا محلية (مرايا maven من Aliyun/Tencent Cloud)، وابحث في الإنترنت عن «مرايا Gradle الصينية» واتبع الشرح</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مكونات SDK ناقصة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تجاوز تنزيل SDK أثناء التثبيت</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">افتح Settings ثم SDK Manager وثبّت المنصات والأدوات الناقصة</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">فشل تشغيل المحاكي / شاشة سوداء</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">المحاكاة الافتراضية غير مفعّلة أو الصورة تالفة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">فعّل VT-x/AMD-V من BIOS؛ واحذف المحاكي وأنشئه من جديد؛ أو استخدم التصحيح على جهاز حقيقي مباشرة</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
جدول الإسعافات الأولية لأخطاء بيئة المبتدئين

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
نصيحة: منهجية البحث عن الأخطاء

{class="mt-1"}
السطر الأول من رسالة الخطأ هو الأثمن — انسخه كما هو في محرك البحث وأضف الكلمة المفتاحية "android studio". لا تبحث عن أسئلة عامة مثل "لا أستطيع تجهيز البيئة ماذا أفعل"، بل عن أخطاء محددة مثل "Gradle sync failed: Could not resolve com.android.tools.build". السؤال الدقيق وحده يعطي الجواب الدقيق.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
لنتجرب: أكمل قائمة "طقوس التطوير" الخاصة بك

{class="mt-1"}
① ثبّت Android Studio وشغّل المحاكي بنجاح؛ ② شغّل تطبيقك على جهاز حقيقي مرة واحدة واحتفظ بلقطة شاشة؛ ③ غيّر نص Hello إلى اسمك؛ ④ اضغط المشروع في ملف مضغوط واحفظ نسخة احتياطية. بعد هذه الخطوات الأربع يمكنك إعلان أصدقائك: صرت مطوّر Android أيضًا (ولقطة الشاشة هي الدليل).
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
خلاصة الفصل

- Android Studio = بيئة التطوير الرسمية المجانية؛ يُنصح بذاكرة 16 جيجابايت + 20 جيجابايت قرص + تفعيل المحاكاة الافتراضية
- عناصر المشروع الجديد الثلاثة: الاسم، واسم الحزمة (فريد عالميًا ولا تنشر بـ com.example)، والحد الأدنى للـ SDK (ابتداءً من API 26)
- طريقتان للتشغيل: المحاكي (هاتف افتراضي داخل الحاسوب) والجهاز الحقيقي (فعّل تصحيح USB وتذكّر إيقافه بعد الانتهاء)
- قاعدة المشروع: لا تلمس سوى مجلد app/ — MainActivity.kt هو البوابة، وManifest سجل القيد، وres/ مستودع الموارد
- روتين التطوير = تعديل الكود ← Run ← مشاهدة النتيجة، بالتكرار المستمر
:::
