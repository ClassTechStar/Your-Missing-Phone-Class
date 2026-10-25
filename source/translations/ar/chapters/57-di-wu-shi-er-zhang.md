---
id: di-wu-shi-er-zhang
num: 52
part: an-zhuo-kai-fa-pian
nav: الفصل 52: المكونات الأربعة ودورة حياة Activity
toc: default
kind: chapter
---

### الفصل 52: المكونات الأربعة ودورة حياة Activity

{class="chapter-intro mb-4"}
إذا كان Compose "وجه" التطبيق، فما سيشرحه هذا الفصل هو "هيكل" التطبيق. لنظام Android أربعة مكونات أساسية، وكل التطبيقات مبنية منها؛ وأهمها Activity له "خريطة دورة حياة" يجب على كل مطور Android حفرها في ذهنه. بعد إتمام هذا الفصل ستتمكن من فهم أحاجي مثل "لماذا تختفي حالة تطبيقي عندما أضعه في الخلفية وأعود إليه".

#### أولًا: المكونات الأربعة: "الأعمدة الأساسية" في Android

عرّف Android رسميًا أربعة مكونات أساسية، كل منها مسؤول عن فئة من الأعمال:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">المكون</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">المسؤولية</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">تشبيه</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activity</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">واجهة مرئية</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">واجهة المتجر — يراها المستخدم ويتفاعل معها</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Service</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الرجل الخفي الذي يعمل في الخلفية</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">عامل المستودع — يشغّل الموسيقى وينزّل الملفات دون حاجة إلى واجهة</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BroadcastReceiver</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">استقبال بث النظام</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">غرفة البريد — مكبر الصوت الذي يعلن "انخفضت البطارية" و"انقطعت الشبكة"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ContentProvider</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مشاركة البيانات بين التطبيقات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">خزانة الملفات العامة — مثل مشاركة جهات الاتصال مع تطبيقات أخرى</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
نظرة سريعة على المكونات الأربعة في Android

في مرحلة المبتدئ ستقضي 95% من وقتك مع Activity؛ وتُستخدم Service و BroadcastReceiver في تشغيل الموسيقى ودفع الرسائل؛ أما ContentProvider فهو الأقل استخدامًا (النظام يغلّف البيانات الشائعة مسبقًا). وانتبه: يجب "تسجيل قيد" المكونات الأربعة جميعًا في AndroidManifest.xml، وإلا فلن يجدها النظام.

#### ثانيًا: دورة حياة Activity: أول "خريطة كنز" في تطوير Android

قد يُقاطع التطبيق في الهاتف في أي لحظة: مكالمة واردة، أو المستخدم ينتقل للرد على WeChat، أو النظام قتل تطبيقك لنقص الذاكرة… وحياة Activity رحلة دائرية على هذه الخريطة:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onCreate (الولادة: تهيئة)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onStart (أصبح مرئيًا)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onResume (تفاعل في المقدمة)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onPause (مغطى جزئيًا)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onStop (غير مرئي تمامًا)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center">onDestroy (تدمير)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">🔁 onRestart / onStart / onResume: عند العودة إلى المقدمة يعود بنفس الطريق معكوسًا</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
الشكل 4: دورة حياة Activity (الاتجاه الأمامي: الصف العلوي للميلاد ← الصف السفلي للمغادرة، وعند العودة نرتد على نفس الطريق)
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">دالة الاستدعاء</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">متى تُستدعى</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الاستخدام النموذجي</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onCreate</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">عند إنشاء Activity (مرة واحدة)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تحميل الواجهة وتهيئة البيانات</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStart</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تصبح الواجهة مرئية</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">بدء بعض المنطق الخفيف</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onResume</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الحصول على التركيز وإتاحة التفاعل</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">بدء الحركات واستئناف التشغيل</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onPause</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">لحظة الحجب الجزئي أو الانتقال بعيدًا</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">إيقاف الحركات وحفظ المسودة</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStop</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">اختفاء تام عن الرؤية</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تحرير الموارد الثقيلة وإيقاف التنزيلات</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onDestroy</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">قبل التدمير</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">التنظيف النهائي</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
الاستخدامات النموذجية لدوال دورة الحياة الست

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
تحذير من الفخاخ: تدوير الشاشة "يقتل" Activity

{class="mt-1"}
أشهر سيناريو فشل عند المبتدئين: تُدار شاشة التطبيق قليلًا فتمحو كل الكلمات من حقول الإدخال. السبب: تدوير الشاشة يدمر Activity ويعيد إنشاءه افتراضيًا (يمر بـ onDestroy ثم onCreate). الحل: استخدم rememberSaveable لحفظ الحالة (بديل remember في Compose)، فهو يستعيد القيم تلقائيًا عند إعادة الإنشاء. سنستخدمه مرارًا في الفصلين 6 و7.
:::

#### ثالثًا: Intent: "تذكرة السفر" داخل التطبيق وخارجه

الـ Intent (القصد) هو "تذكرة السفر" للتواصل بين المكونات. للانتقال من صفحة إلى أخرى، أو فتح المتصفح، أو تشغيل الكاميرا، عليك "شراء التذكرة ثم الصعود":

::: div .code-block
:::inline div .code-head
<span>KOTLIN · التنقل باستخدام Intent</span><span class="dots">···</span>
:::

```
// الطريقة الأولى: Intent صريح — تحدد بوضوح إلى أي شاشة تذهب
val intent = Intent(this, DetailActivity::class.java)
intent.putExtra("name", "أحمد")     // يحمل "أمتعة" في السيارة (البيانات)
startActivity(intent)

// الطريقة الثانية: Intent ضمني — تقول فقط ما المطلوب والنظام يجد من ينفذه
val web = Intent(Intent.ACTION_VIEW, Uri.parse("https://developer.android.com"))
startActivity(web)   // سيفتح النظام المتصفح (أو سيتيح لك الاختيار)
```
:::

لكل من الطريقتين استخدامها: الصريحة للتنقل بين صفحات تطبيقك نفسه؛ والضمنية لاستدعاء قدرات النظام أو تطبيقات أخرى (فتح صفحة ويب، إجراء مكالمة، مشاركة). في مشاريع Compose، احصل على Context عبر LocalContext.current داخل الدالة القابلة للتركيب ثم استدعِ startActivity.

#### رابعًا: الصفحات المتعددة والتنقل

التطبيقات الحقيقية متعددة الصفحات. الحل الرسمي الموصى به في Compose هو Navigation Compose (مكتبة androidx.navigation):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · هيكل Navigation Compose</span><span class="dots">···</span>
:::

```
val navController = rememberNavController()

NavHost(navController, startDestination = "home") {
    composable("home") { HomeScreen(navController) }
    composable("detail/{name}") { entry ->
        val name = entry.arguments?.getString("name")
        DetailScreen(name ?: "غير معروف")
    }
}

// للتنقل من داخل الشاشة:
navController.navigate("detail/أحمد")     // مع وسيط
navController.popBackStack()              // العودة إلى الشاشة السابقة
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
نصيحة: ماذا تفعل عندما تكثر الصفحات؟

{class="mt-1"}
عندما يكبر المشروع اجمع كل مسارات الصفحات في ملف واحد (مثل AppNavGraph.kt) لإدارتها بشكل موحد، ولا تترك منطق "الانتقال إلى أين" مبعثرًا بين الصفحات. هذه أول خطوة من "يعمل" إلى "قابل للصيانة".
:::

#### خامسًا: تعارف عرضي: ما هو Fragment (ولماذا لم يشرحه الكتاب)

عند تصفح الدروس القديمة ستقابل حتمًا Fragment — إنه "مقطع واجهة قابل لإعادة الاستخدام" داخل Activity، وكان بطلًا لا منازع له في بنية الصفحات المتعددة القديمة. لكن في عصر Compose يكفي استخدام دوال Composable مع مسارات Navigation مباشرة، وقد خفّضت جوجل رسميًا مكانة Fragment. لذلك لم يضعه هذا الكتاب في المسار الرئيسي.

نصيحتي لك: لا تستخدم Fragment طوعًا في المشاريع الجديدة؛ واكتفِ عند قراءة الكود القديم أو مواجهته في مقابلة عمل بمعرفة أنه "مقطع واجهة مدمج داخل Activity". واختر دائمًا مصادر التعلم الصادرة بعد 2023 — فـ"التقاوين القديمة" لتقنيات Android تتحدث أسرع مما تتصور.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
لنتجرب: امنح العدّاد "ذاكرة"

{class="mt-1"}
عدّل عدّاد الفصل 51: ① استبدل remember بـ rememberSaveable وتحقق من بقاء الرقم بعد تدوير الشاشة؛ ② أضف زر "حول" يستخدم Navigation للانتقال إلى صفحة ثانية تعرض رقم الإصدار؛ ③ اطبع سجلات (Log.d) في onCreate/onPause لكلا الصفحتين وراقب ترتيب استدعاءات دورة الحياة عبر Logcat. بعد هذه الخطوات الثلاث لن تكون دورة الحياة حبرًا على ورق.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
خلاصة الفصل

- المكونات الأربعة: Activity (الواجهة)، Service (الخلفية)، BroadcastReceiver (مكبر الصوت)، ContentProvider (خزانة الملفات)
- دوال دورة الحياة الست: onCreate → onStart → onResume → onPause → onStop → onDestroy
- تدوير الشاشة يدمر Activity ويعيد إنشاءه: احفظ الحالة بـ rememberSaveable
- الـ Intent "تذكرة": الصريحة للتنقل داخل صفحاتك، والضمنية لاستدعاء قدرات النظام
- الصفحات المتعددة عبر Navigation Compose: مسارات NavHost + composable
:::
