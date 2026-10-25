---
id: di-wu-shi-liu-zhang
num: 56
part: an-zhuo-kai-fa-pian
nav: الفصل 56: الصقل والنشر — الإطلاق على Google Play
toc: default
kind: chapter
---

### الفصل 56: الصقل والنشر — الاختبار وتصحيح الأخطاء والنشر على Google Play

{class="chapter-intro mb-4"}
صنعت التطبيق، وماذا بعد؟ يجيب هذا الفصل على ثلاث مسائل للانتقال من «يعمل» إلى «جاهز للتسليم»: كيف تصحح الأخطاء بكفاءة، وكيف تكتب اختبارات تمنع عودة المشاكل، وكيف ترفع تطبيقك إلى Google Play لينزّله العالم. والنشر ليس مجرد طقس — إنه الفاصل الذي يحوّل عملاً منجزاً إلى منتج حقيقي.

#### أولاً: أدوات التصحيح الثلاث — Logcat ونقاط التوقف وفاحص واجهة المستخدم

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الأداة</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ماذا تفعل</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">كيف تستخدمها</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logcat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">عرض سجلات النظام أو سجلاتك الخاصة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">اكتب Log.d("TAG", "القيمة=$x") في الكود ثم ابحث عن TAG في اللوحة للتصفية</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">التصحيح بنقاط التوقف</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">إيقاف البرنامج عند سطر معيّن ومشاهدة قيم المتغيرات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">انقر بجانب رقم السطر فتظهر نقطة حمراء، ثم شغّل بوضع Debug وتقدّم خطوة بخطوة</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Layout Inspector</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">فحص بنية الواجهة أثناء التشغيل</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">من القائمة Tools ← Layout Inspector لرؤية شجرة المكونات مباشرة</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
أدوات التصحيح الثلاث

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
نصيحة: كيف تقرأ رسائل الخطأ؟

{class="mt-1"}
بعد الانهيار يظهر في Logcat تتبع أحمر (Stacktrace)؛ ابحث من الأسفل إلى الأعلى عن أول سطر يبدأ باسم حزمتك (مثل com.example.yourapp)، فهذا السطر هو مكان الحادث غالباً. اقرأ أولاً «نوع الاستثناء» (مؤشر فارغ؟ تحويل نوع؟) ثم «at ... ملفك: رقم السطر». بهذه الحيلة تحل 80% من الانهيارات.
:::

#### ثانياً: الاختبارات — تأمين على الكود

الاختبار اليدوي لا يُعتمد — تعدّل ميزة فتنكسر أخرى بصمت. الاختبارات هي «دواء الندم» و«السترة الواقية» معاً. تنقسم اختبارات Android إلى ثلاث طبقات، وعلى المبتدئ إتقان الطبقة الأولى أولاً:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الطبقة</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ماذا تختبر</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">أين توضع</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">السرعة</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">اختبارات الوحدة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">منطق خالص (حساب وتحقق)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/test/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">من رتبة الثواني</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">اختبارات الأجهزة (Instrumented)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">سلوك الواجهة على جهاز حقيقي</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/androidTest/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">من رتبة الدقائق</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الاختبار اليدوي</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">إحساس وتجربة إنسان حقيقي</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">لا غنى عنه أبداً</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
طبقات الاختبار الثلاث

::: div .code-block
:::inline div .code-head
<span>KOTLIN · مثال اختبار وحدة</span><span class="dots">···</span>
:::

```
// استخرج منطق "تحويل نص المبلغ إلى رقم" كدالة نقية
fun parseAmount(input: String): Double? {
    val v = input.trim().toDoubleOrNull()
    return if (v != null && v > 0) v else null
}

// اختبرها (JUnit4)
@Test
fun emptyInputReturnsNull() {
    assertEquals(null, parseAmount(""))
}
@Test
fun negativeReturnsNull() {
    assertEquals(null, parseAmount("-5"))
}
@Test
fun normalValueParses() {
    assertEquals(12.5, parseAmount("12.5"))
}
```
:::

التحقق من المبالغ والحسابات الإحصائية في دفتر المصاريف يجب أن تحميها اختبارات الوحدة. لتشغيلها: انقر بالزر الأيمن على مجلد test ثم Run. إذا اجتازت الاختبارات كلها بلون أخضر فعدّل كودك مطمئناً.

#### ثالثاً: التوقيع والتجزئة — وضع «الختم» على التطبيق

يشترط Android أن تكون كل حزمة تثبيت موقّعة — كالختم الرسمي الذي يثبت أن «هذه الحزمة مني ولم يُعبث بها». أثناء التصحيح يستخدم Android Studio توقيع debug تلقائياً، أما النشر فيتطلب توقيع release خاصاً بك. الخطوات:

1. من القائمة Build ← Generate Signed Bundle / APK؛
2. إنشاء ملف keystore (مخزن المفاتيح) — اضبط كلمة مرور واحفظه بعناية؛
3. اختر صيغة release مع AAB ويكتمل البناء.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
تحذير من فخ: ضياع keystore يعني ضياع التطبيق

{class="mt-1"}
تحديث التطبيق بعد نشره يتطلب التوقيع نفسه، وإلا رفض المتجر التحديث. وإذا ضاع ملف keystore وكلمة المرور فلا سبيل إلا إلى تطبيق جديد يُنشر من الصفر — ولن يلتحق به المستخدمون القدامى. احرص على أخذ نسخة احتياطية من keystore وكلمة المرور في مكان آمن (سحابة مشفرة + دفتر ملاحظات)، فهذا من أغلى الدروس التي يدفعها مطورو Android.
:::

#### رابعاً: خطوات النشر على Google Play كاملة

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> تسجيل حساب مطوّر</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> تجهيز مواد المتجر</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> رفع ملف AAB</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> ملء نموذج أمان البيانات</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> المراجعة (ساعات إلى أيام)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> النشر</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
الشكل 6: ست خطوات للنشر على Google Play
:::

- التسجيل: رسوم لمرة واحدة قدرها 25 دولاراً، مع حساب Google عامل؛
- المواد: أيقونة التطبيق (512×512)، ولقطات شاشة (اثنتان على الأقل)، ووصف الوظائف، ورابط سياسة الخصوصية (إلزامي عند جمع البيانات)؛
- استمارة أمان البيانات: صرّح بصدق عن البيانات التي تجمعها — دفتر المصاريف غير المتصل بالإنترنت يمكنه الإعلان عن «صفر جمع»؛
- المراجعة: النشر الأول للحسابات الجديدة يخضع غالباً لمراجعة بشرية تستغرق من ساعات إلى أيام، وإن رُفض فعدّل وفق الملاحظات.

ملاحظة للمستخدمين داخل الصين: يتطلب Google Play بيئة شبكة خاصة، ويتم توزيع التطبيقات في البر الرئيسي الصيني عادة عبر المتاجر المحلية (Huawei وXiaomi وTencent MyApp وغيرها). عملية النشر في المتاجر المحلية مشابهة، لكن لكل متجر ذوقه في المراجعة — ويمكن توزيع ملف AAB/APK نفسه على متاجر متعددة. وللتدريب، يكفيك النجاح مع متجر واحد.

#### خامساً: إعداد مواد المتجر — الانطباع الأول هو تحميلاتك

صفحة المتجر هي واجهة العرض التي يراها المستخدم أثناء تجوله. ثلاث مواد تحدد الانطباع الأول:

- الأيقونة: بمقاس 512×512، ولا تلجم بلقطة شاشة. إن لم تكن مصمماً فولّد شكلاً هندسياً بسيطاً بأداة ذكاء اصطناعي، والمعيار أن تتعرف عليه بنظرة واحدة حتى بعد صغره على الشاشة الرئيسية للهاتف؛
- لقطات الشاشة: اثنتان على الأقل، ويفضّل من 4 إلى 6 تعرض أهم سيناريوهات الوظائف؛ مع جملة وصف بسيطة لكل لقطة (عبارة «سجّل مصروفاً في ثانية» أفضل بعشرة أضعاف من «حل متكامل ومحترف لإدارة الحسابات»)؛
- الوصف: أوضح في الجملة الأولى «ما هذا + لمن هو»، ولا تكدّس عبارات مثل «الأكثر احترافاً والأقوى» — فترتيب البحث في المتجر يعتمد أساساً على الكلمات المفتاحية ونسبة التحويل إلى تحميل، والصدق أكثر فاعلية من المبالغة.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
نصيحة: قارن بنظرة إلى المنافسين

{class="mt-1"}
قبل النشر تجول بين العشرة الأوائل من التطبيقات المشابهة في المتجر والتقط لقطات شاشة للمقارنة: ما نمط أيقوناتها؟ ما الميزات التي تعرضها اللقطات؟ كيف تكتب العناوين؟ المحاكاة ليست سرقة — تعلّم القوالب وضع محتواك أنت، فهذا أسرع درس في الإطلاق لأي منتج جديد.
:::

#### سادسًا: قائمة مختصرة لتحسين الأداء والإبلاغ عن الانهيارات

قبل نشر التطبيق، تستحق هاتان المسألتان نصف ساعة لكل منهما:

##### 1. أربع نقاط لفحص الأداء

1. استخدم LazyColumn للقوائم: لا تعرض قائمة طويلة أبداً بـ Column العادي — فالتحميل الكسول هو الدرس الأول في أداء Android؛
2. لا تدرج الصور بمقاسها الأصلي: استخدم مكتبة الصور Coil لتصغيرها وتخزينها مؤقتاً تلقائياً — صورة واحدة بحجم 5 ميغابايت كافية لتعطيل الأجهزة الضعيفة؛
3. تجنّب الأعمال الثقيلة في الخيط الرئيسي: نفّذ قاعدة البيانات والشبكة والملفات الكبيرة داخل coroutines؛
4. قِس باستخدام Profiler: محلّل الأداء المدمج في Android Studio يعرض الذاكرة والمعالج واستهلاك البطارية — قِس أولاً ثم حسّن، ولا تعتمد على الإحساس.

##### 2. الإبلاغ عن الانهيارات

عدم انهيار التطبيق أثناء اختبارك لا يعني أنه لن ينهار على هواتف المستخدمين. قبل النشر ادمج Firebase Crashlytics (رسمي من Google ومجاني): بضعة أسطر إعداد تكفي ليُرسل تتبع الانهيار تلقائياً عند حدوثه، فترى في لوحة التحكم «أي طراز، وأي إصدار، وأي سطر انهار». والنشر دون مراقبة للانهيارات كقيادة السيارة وعينان مغمضتان.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
لنطبّق: سلّم دفتر المصاريف مرة واحدة

{class="mt-1"}
① أضف 3 اختبارات وحدة لمنطق parseAmount وما شابهه؛ ② اصطد بنفسك عبر Logcat انهياراً صنّعته ثم أصلحه؛ ③ أنشئ ملف APK موقّعاً بنسخة release وأرسله لصديق ليثبته (هذه هي متعة «العمل المنجز»)؛ ④ وإن سمحت طاقتك فسجّل حساب مطوّر وقدّم دفتر المصاريف فعلياً للنشر. الثلاث الأولى تنجزها الليلة.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
خلاصة الفصل

- أدوات التصحيح الثلاث: Logcat للسجلات، ونقاط التوقف للمتغيرات، وLayout Inspector للواجهة
- قراءة الانهيار: ابحث من أسفل التتبع إلى أعلاه عن أول سطر يحمل اسم حزمتك
- طبقات الاختبار الثلاث: الوحدة (من رتبة الثواني، تعلّمها أولاً) / الأجهزة / اليدوي
- النشر يتطلب توقيعاً: احفظ نسخة احتياطية من keystore وكلمة المرور، فضياعهما يعني «تطبيقاً بغير صاحبه»
- ست خطوات للنشر: التسجيل ← المواد ← رفع AAB ← استمارة أمان البيانات ← المراجعة ← النشر
:::
