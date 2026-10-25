---
id: di-wu-shi-qi-zhang
num: 57
part: an-zhuo-kai-fa-pian
nav: الفصل 57: طريق الترقي — الأذونات والإشعارات والبنية الحديثة
toc: default
kind: chapter
---

### الفصل 57: طريق التقدم — الأذونات والإشعارات والبنية الحديثة

{class="chapter-intro mb-4"}
صناعة التطبيق مجرد بداية. يتناول هذا الفصل العقبات في الانتقال من «أعرف أن أعمله» إلى «أعمله بإتقان»: كيف تطلب الأذونات بأناقة، وكيف ترسل إشعارات لا تزعج أحداً، وكيف ترفع بنية المشروع درجة أخرى، وكيف — في عام 2026 — تنظم مع الذكاء الاصطناعي في كتابة كود Android. وكل نقطة منها ستقابلها قريباً في مشروع حقيقي.

#### أولاً: الأذونات أثناء التشغيل — اطرق الباب قبل الدخول

الكاميرا والموقع وجهات الاتصال والإشعارات... هذه «المناطق الحساسة» يطلب Android من التطبيق استئذان المستخدم فيها أثناء التشغيل (منذ Android 6). القاعدة: أعلن أولاً (في Manifest)، ثم اطلب (في الكود)، وتراجع برفق عند رفض المستخدم. وفي Compose أسهل خيار هو rememberPermissionState من المكتبة الرسمية Accompanist:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · أذونات وقت التشغيل (نسخة Compose)</span><span class="dots">···</span>
:::

```
// صرّح أولًا في الـ Manifest:
// &lt;uses-permission android:name="android.permission.CAMERA" /&gt;

@Composable
fun CameraButton() {
    val permission = rememberPermissionState(
        permission = android.Manifest.permission.CAMERA
    )
    Button(onClick = {
        when {
            permission.status.isGranted -&gt; openCamera()
            permission.status.shouldShowRationale -&gt; showExplainDialog()
            else -&gt; permission.launchPermissionRequest()
        }
    }) { Text("التقاط صورة") }
}
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
تنبيه: ماذا لو رُفض الإذن نهائياً؟

{class="mt-1"}
إذا علّم المستخدم «لا تسأل مرة أخرى» فلن تظهر launchPermissionRequest أي نافذة بعدها. عندها وجب توجيه المستخدم إلى تفعيلها يدوياً من إعدادات النظام (باستخدام Intent يفتح صفحة إعدادات التطبيق)، مع شرح في الواجهة «ما الغاية من هذا الإذن». لبقة بسيطة ترفع كثيراً رغبة المستخدم في منح الإذن — فصياغة طلب الإذن تستحق عناية حقيقية.
:::

#### ثانياً: الإشعارات — قل الكلمة المفيدة في الوقت المناسب

الإشعار قناة وصول التطبيق إلى المستخدم، وهو أيضاً أكثر الميزات عرضة لـ «الحجب» من طرفه. ثلاث قواعد عند الإرسال: أرسل المفيد فقط، واتركه قادراً على إيقافها، ولا تزعجه في جوف الليل. الاستخدام الأساسي:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · إرسال إشعار</span><span class="dots">···</span>
:::

```
// في Android 13+ يجب طلب إذن POST_NOTIFICATIONS أولًا (انظر القسم السابق)

// 1. إنشاء قناة الإشعارات (إلزامي في Android 8+)
val channel = NotificationChannel(
    "reminder", "تذكيرات", NotificationManager.IMPORTANCE_DEFAULT
)
val manager = getSystemService(NotificationManager::class.java)
manager.createNotificationChannel(channel)

// 2. إرسال الإشعار
val notification = NotificationCompat.Builder(this, "reminder")
    .setSmallIcon(R.drawable.ic_notification)
    .setContentTitle("تذكير بتسجيل المصروفات")
    .setContentText("لم تسجل أي مصروفات اليوم بعد")
    .setPriority(NotificationCompat.PRIORITY_DEFAULT)
    .build()
if (ActivityCompat.checkSelfPermission(this,
        Manifest.permission.POST_NOTIFICATIONS) == PackageManager.PERMISSION_GRANTED
) {
    manager.notify(1, notification)
}
```
:::

المهام المجدولة (مثل «تذكير بتسجيل المصاريف كل يوم عند 20:00») تُنفَّذ عبر WorkManager — وهو «مدبّر الجدولة في الخلفية» الموصى به رسمياً، يضمن تنفيذ المهمة في وقتها المناسب دون أن تنشغل أنت بتحسين البطارية. استخدمه لكل حاجة تشبه المنبه ولن تخطئ.

#### ثالثاً: تقدّم في البنية — حقن التبعيات والتجزئة إلى وحدات

عندما يكبر المشروع، يقترب منك «إزعاجان لطيفان»:

- فوضى إنشاء الكائنات: كل شاشة تنشئ قاعدة بياناتها وواجهة API بنفسها — استخدم Hilt (إطار حقن التبعيات) للإدارة الموحدة، «من طلب شيئاً وجد من يسلمه إياه»؛
- تراكم الكود جبلاً: مشروع الوحدة الواحدة يتباطأ مع كل تعديل — قسّمه إلى وحدات متعددة (app / core / feature-xxx)، تتطوّر كل ميزة وتُختبر باستقلال.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
نصيحة: لا تبالغ في التصميم

{class="mt-1"}
Hilt والتجزئة إلى وحدات أدوات جيدة، لكن لا تتسرع في تبنّيها في مشروع فردي. دفتر المصاريف بوحدة واحدة وإنشاء يدوي للتبعيات يكفي تماماً. انتظر حتى يتجاوز الكود عشرات آلاف الأسطر أو يتباطأ التصريف أو ينضم آخرون إلى العمل، ثم أدخلها حسب الحاجة. الأدوات تخدم الهدف ولا تُستعرض بها — وهذا مبدأ «البساطة أولاً» في كتابنا عن برمجة الذكاء الاصطناعي.
:::

#### رابعاً: أساليب 2026 الجديدة — تطوير Android بمساعدة الذكاء الاصطناعي

في 2026 أصبح الذكاء الاصطناعي مدمجاً بعمق في دورة تطوير Android. إن أردت تسريع عملك فهذه السلسلة المتكاملة ناضجة جداً:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">المرحلة</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">كيف يساعد الذكاء الاصطناعي</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">مسؤوليتك</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">كتابة الكود</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الإكمال والتوليد عبر Gemini المدمج في Android Studio أو إضافات ذكاء اصطناعي من أطراف ثالثة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">وصف المتطلبات بوضوح ومراجعة المخرجات</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">البحث عن المعلومات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">أعطِ الذكاء الاصطناعي الوثائق الرسمية ورسائل الخطأ ليفسرها</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تحقّق من الاستنتاجات المهمة في الوثائق الرسمية</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">كتابة الاختبارات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">اطلب من الذكاء الاصطناعي توليد حالات اختبار في ثلاث فئات: عادي/حدّي/استثنائي</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تأكد من أن الحالات تطابق دلالة مجال العمل</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">إصلاح الأخطاء (bug)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الصق التتبع مع الكود ذي الصلة، فيحدد الذكاء الاصطناعي الموضع ويصلح</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">افهم التعديل وشغّل الاختبارات للتحقق</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
أربعة سيناريوهات لمساعدة الذكاء الاصطناعي في تطوير Android

أما المنهجية التفصيلية — كيف توجّه الذكاء الاصطناعي، وكيف تقبل المخرجات، وكيف تتجنب الفخاخ — فموضوعها 11 فصلاً كاملاً في القسم السابع من هذا الكتاب «التطبيق العملي لبرمجة الذكاء الاصطناعي» (الفصول 37-47)، وننصح بشدة بقراءته بالتوازي: اترك قواعد لغة Android لهذا القسم، وأسلوب التعاون مع الذكاء الاصطناعي للقسم السابع.

#### خامساً: تحسين أداء Compose وأدوات تصحيحه

الكتابة بـ Compose ممتعة، لكن «إعادة التركيب الزائدة» تسبب التقطيع أيضاً. ثلاث حيل عملية:

- ثبّت المعاملات: أضف @Immutable إلى فئات البيانات أو استخدم derivedStateOf لتجنب إعادة تركيب واسعة بسبب تغيرات حالة لا صلة لها؛
- لا تنسَ key: تجعل items(list, key = { it.id }) القائمة تعدّل العنصر المطلوب فقط عند الإضافة والحذف — بدون key قد تُرسم القائمة كلها من جديد عند حذف عنصر واحد؛
- وضع Compose في Layout Inspector: يعرض مباشرة عدد مرات إعادة تركيب كل Composable، فتعرف بنظرة واحدة من يُعاد تركيبه كثيراً، وحسّن هذه النقاط الساخنة.

كذلك فعّل تقرير مترجم Compose (المقاييس Metrics) ليولّد لك تقريراً عن «المكونات غير المستقرة» — في طريق التقدم، البيانات أدعى إلى الثقة دائماً من الإحساس.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
لنطبّق: أضف «الثلاثية» إلى دفتر المصاريف

{class="mt-1"}
① أضف إلى دفتر المصاريف «تذكير تسجيل المصاريف كل يوم عند 20:00» (WorkManager + قناة إشعارات + إذن الإشعارات في Android 13)؛ ② حوّل إنشاء قاعدة البيانات وواجهة API إلى حقن عبر Hilt؛ ③ جرّب أداة ذكاء اصطناعي لتسريع تنفيذ ميزة «التصفية الشهرية» ثم راجع المخرجات بطريقة القبول الثلاثية. بإتمام الثلاثية سيأخذ مشروعك هيئة «جيش نظامي».
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
خلاصة الفصل

- الأذونات الحساسة: إعلان في Manifest + طلب أثناء التشغيل + توجيه لطيف بعد الرفض
- قواعد الإشعارات الثلاث: المفيد فقط، ويمكن إيقافه، ولا إزعاج؛ القناة والإذن لا يكفي أحدهما دون الآخر
- المهام المجدولة عبر WorkManager، ولا تخترع العجلة من جديد
- Hilt للكائنات والوحدات للكود — لا تتسرع بهما في مشروعك الصغير الفردي
- أربعة سيناريوهات لمساعدة الذكاء الاصطناعي: كتابة الكود، والبحث عن المعلومات، وكتابة الاختبارات، وإصلاح الأخطاء؛ والمنهجية في القسم السابع (الفصول 37-47)
:::
