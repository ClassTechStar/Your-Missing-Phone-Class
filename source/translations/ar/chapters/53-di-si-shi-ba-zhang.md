---
id: di-si-shi-ba-zhang
num: 48
part: an-zhuo-kai-fa-pian
nav: الفصل 48: تعرف على Android — من نظام التشغيل إلى منظومة التطوير
toc: default
kind: chapter
---

### الفصل 48: التعرف على أندرويد — من نظام التشغيل إلى منظومة التطوير

{class="chapter-intro mb-4"}
مبروك عليك هذا القرار — أن تتحول من "شخص يلعب بالهاتف" إلى "شخص يصنع تطبيقات الهاتف". وقبل أن نشمر عن الأكمام، لننشر الخريطة أولا: من أين جاء أندرويد؟ لماذا يكتب له المطورون في العالم كله التطبيقات؟ وماذا يحدث بالضبط بين لحظة ضربك المفاتيح ووصول التطبيق إلى هواتف المستخدمين؟

#### أولاً: قصة أندرويد — من "الروبوت الصغير" إلى "أكبر أنظمة العالم"

تبدأ قصة أندرويد (Android) عام 2003 — حين أسس مهندس اسمه Andy Rubin شركة Android بهدف بسيط: بناء نظام تشغيل ذكي "يفهم الكاميرا أكثر". ثم استحوذت عليه جوجل عام 2005، وفي 2007 شكلت مع عشرات المصنعين تحالف الهواتف المفتوحة (OHA)، وفي سبتمبر 2008 طرح أول هاتف أندرويد رسميا وهو HTC Dream (G1).

قصة ما بعدها يعرفها الجميع: بحلول 2026 أصبح أندرويد نظام التشغيل المحمول الأوسع حصة سوقية في العالم، وعدد الأجهزة النشطة بمليارات. هاتفك وعلبة التلفاز وشاشة السيارة وساعتك الذكية — كلها على الأرجح تعمل بأندرويد. ماذا يعني هذا؟ يعني أن كل سطر تكتبه من الكود له فرصة أن يستخدمه أكبر عدد من الناس في العالم.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
نصيحة: الجينات مفتوحة المصدر في أندرويد

{class="mt-1"}
الكود الأساسي لأندرويد (AOSP، مشروع أندرويد مفتوح المصدر) مفتوح المصدر — وأي مصنع يستطيع أن يأخذه ويعدله ويخصصه. لذلك لدى Xiaomi واجهة MIUI (وتسمى الآن HyperOS)، ولدى Huawei طبقة توافق HarmonyOS، ولدى Samsung واجهة One UI. وهذا خير للمطورين: أنت تتعلم "تطوير أندرويد" لا "تطوير علامة بعينها" — مهارة واحدة تغطي كل الأجهزة.
:::

وتطور أرقام الإصدارات ممتع أيضا: بدءا من 1.5 باسم Cupcake (الكب كيك)، سمي كل إصدار كبير باسم حلوى — Donut وÉclair وFroyo وGingerbread... إلى أن جاء التحول إلى الأرقام الخالصة مع أندرويد 10 عام 2019. وحتى أغسطس 2026، الإصدار الرسمي الأحدث هو Android 17، أما "الحد الأدنى للدعم" الذي يهمك فعلا عند التطوير فتضعه التطبيقات السائدة عادة بين Android 8 (API 26) وAndroid 10 (API 29) — كلما دعمت أجهزة السنوات الماضية اتسعت قاعدة مستخدميك.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الإصدار</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الاسم الرمزي/السنة</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ما يهم المطور</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 8 (API 26)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Oreo · 2017</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">قنوات الإشعارات وقيود العمل في الخلفية — الحد الأدنى للعديد من الأجهزة القديمة</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 10 (API 29)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2019</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ظهور التخزين المقسم وتغيير جذري في قواعد الوصول إلى الملفات</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 12 (API 31)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2021</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ألوان ديناميكية بأسلوب Material You وترقية كبيرة لمظهر الواجهة</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 13 (API 33)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2022</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">إذن الإشعارات وقت التشغيل، ونافذة تسألك "هل تسمح بإرسال الإشعارات"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 14-15 (API 34-35)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2023-2024</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الرجوع التنبؤي، وصفحات 16KB، وتشديد إضافي للخصوصية</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 16-17 (API 36-37)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2025-2026</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">إيقاع أسرع للإصدارات الصغيرة، ودمج قدرات الذكاء الاصطناعي (مثل توسعات Gemini)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
تاريخ موجز لإصدارات أندرويد (حتى أغسطس 2026، النقاط التي يركز عليها المطورون)

#### ثانياً: بأي لغة نكتب — Java أم Kotlin؟

ظهرت في تاريخ تطوير أندرويد لغتان رئيسيتان. Java هي "العمود الفقري المؤسس" — فقد استخدمت منذ ولادة أندرويد؛ وKotlin هي "المواطنة من الدرجة الأولى" التي اختارتها جوجل عام 2017، ومنذ 2019 أعلنت رسميا مبدأ "Kotlin أولا" (Kotlin-first)، وبحلول 2026 صارت المشاريع الجديدة كلها تقريبا بـ Kotlin، وترحل المشاريع القديمة معظمها إليها تباعا.

وبصراحة: إذا كنت مبتدئا تاما فتعلّم Kotlin مباشرة ولا ترجع إلى Java. ثلاثة أسباب: أولا كود Kotlin أقل من Java بنسبة 30%-40% (نفس الوظيفة لكنه أقصر وأوضح)؛ ثانيا يقيك بطبيعته من "المؤشر الفارغ" (Null Pointer) كابوس المبتدئين؛ ثالثا كل الدروس الحديثة والوثائق الرسمية وأدوات البرمجة بالذكاء الاصطناعي (أتذكر كتابنا في البرمجة بالذكاء الاصطناعي؟) تعتمد Kotlin مرجعا. أما Java فلن تصادفها إلا في صيانة المشاريع القديمة وقراءة الكود القديم.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
أسلوب Java (النسخة المطولة)

{class="font-mono text-xs leading-relaxed"}
public class MainActivity extends Activity {<br>&nbsp;&nbsp;@Override<br>&nbsp;&nbsp;protected void onCreate(Bundle b) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b);<br>&nbsp;&nbsp;&nbsp;&nbsp; setContentView(R.layout.activity);<br>&nbsp;&nbsp;}<br>}
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
أسلوب Kotlin (النسخة المقتضبة)

{class="font-mono text-xs leading-relaxed"}
class MainActivity : ComponentActivity() {<br>&nbsp;&nbsp;override fun onCreate(b: Bundle?) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b)<br>&nbsp;&nbsp;&nbsp;&nbsp;setContent { App() }<br>&nbsp;&nbsp;}<br>}
:::
:::

نفس العملية تماما، لكن Kotlin يستغني عن الكثير من الأقواس المعقوفة والكود النمطي. سنتعلمه رسميا في الفصل 50، والآن يكفيك أن تحفظ: "اللغة العامة" لتطوير أندرويد اسمها Kotlin.

#### ثالثاً: كيف يولد التطبيق (App)؟

يظن كثيرون أن "تطوير التطبيقات" مجرد فتح الحاسوب والكتابة بلا توقف. في الواقع يحتاج التطبيق من الفكرة إلى هواتف المستخدمين إلى خط إنتاج تقريبي كالتالي:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-lightbulb mr-1"></i> فكرة</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center">📐 التصميم (الواجهة + الوظائف)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-keyboard mr-1"></i> كتابة الكود</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hammer mr-1"></i> الترجمة والتغليف (APK/AAB)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> الاختبار (محاكي + جهاز حقيقي)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-rocket mr-1"></i> النشر (المتجر/حزمة التثبيت)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
الشكل 1: الدورة الكاملة لتطبيق أندرويد من الفكرة إلى النشر في المتجر
:::

في هذا المسار مفهومان عليك التعرف عليهما من الآن:

- APK: صيغة حزمة تثبيت تطبيقات أندرويد (.apk)، تنقر عليها فيثبت في الهاتف، تماما مثل ملف .exe في Windows. استخدمها لاختباراتك الشخصية ولمشاركة التطبيق مع أصدقائك للتجربة.
- AAB: صيغة Android App Bundle (.aab)، وهي "صيغة التغليف المتقدمة" المستخدمة للنشر على Google Play. يقوم المتجر بقص الحزمة ديناميكيا حسب طراز هاتف كل مستخدم، فيكون ما ينزله كل شخص أصغر حجما. لا يمكنك تثبيتها بنفسك، وهي تسلم إلى المتجر فقط.

وسوف تسمع باستمرار مصطلحا آخر: SDK (مجموعة تطوير البرمجيات). وهي "عدة التطوير" الكاملة التي توفرها أندرويد رسميا — تشمل مكتبات API لكل الإصدارات وأدوات التصحيح وصور المحاكيات وغيرها. الكلاسات مثل Activity وButton التي تستدعيها في كودك تأتي كلها من الـ SDK.

#### رابعاً: المشهد الكامل لحزمة تقنيات أندرويد — "قائمة أسلحتك"

قبل البدء بالتعلم الرسمي، تعرف على الإعداد القياسي لمشاريع أندرويد السائدة في 2026 — لا يهم إن لم تفهم هذه القائمة الآن، فعندما تعود إليها بعد إنهاء الكتاب كلها ستنفتح أمامك تماما:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الطبقة</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الخيار السائد (2026)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">لأي غرض يستخدم</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">اللغة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin 2.x</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">لغة كتابة المنطق</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الواجهة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jetpack Compose + Material 3</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">رسم الواجهة بالكود (الخط الرئيسي لهذا الكتاب)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">البنية المعمارية</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MVVM + ViewModel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">فصل الواجهة عن المنطق حتى لا يتشابك الكود</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تخزين البيانات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room (قاعدة بيانات) + DataStore (الإعدادات)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">حفظ البيانات في الهاتف</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الشبكات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit + OkHttp + Coroutines في Kotlin</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">التحدث مع الخادم</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">أدوات البناء</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle + Kotlin DSL</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تحويل الكود إلى حزمة تثبيت</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">بيئة التطوير</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">بيئة التطوير المتكاملة "الشاملة" الرسمية من جوجل</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
نظرة سريعة على حزمة تقنيات أندرويد السائدة في 2026

لا تدع هذه السلسلة من الكلمات الأجنبية تخيفك. إنها أشبه بأدوات المطبخ — كل ما تحتاج معرفته الآن هو أن "الطبخ يجري في المطبخ"، وكيفية استخدام كل أداة سنفككها لك واحدة تلو الأخرى في الفصول القادمة. والخبر السار: عند إنشاء مشروع جديد يهيئ Android Studio هذه المجموعة كلها تلقائيا، وأنت مكلف بالطبخ فقط.

#### خامساً: أندرويد مقابل iOS — أول درس "اختيار المعسكر" للمطور

قد تكون تحمل الآن جهاز أندرويد وجهاز آبل معا. بصفتك مطورا، من المفيد التعرف مسبقا على الفروق بين التجربتين — ليس انحيازا لسؤال "أيهما أفضل" بل حسابا واقعيا لسؤال "أي الجهتين أنسب لبدايتك":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">البعد</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">تطوير أندرويد</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">تطوير iOS</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">حاسوب التطوير</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Windows / Mac / Linux — أي منها يصلح</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">يتطلب جهاز Mac حصرًا (Xcode متاح عليه فقط)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">أدوات التطوير</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio (مجاني)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode (مجاني) + رسم سنوي للنشر قدره 99 دولارًا</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مراجعة النشر على المتجر</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">متساهلة، من بضع ساعات إلى بضعة أيام</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">صارمة، ومن 1 إلى 7 أيام هو المعتاد</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">التثبيت والتجربة على الأجهزة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ملف APK يمكن نشره وتثبيته بحرية تامة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">التوزيع محدود، والاختبار يتطلب التوقيع أو TestFlight</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">بيئة تحقيق الإيرادات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الأغلبية للإعلانات والقنوات المحلية</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">عادات الدفع داخل App Store أفضل (المستخدمون أكثر استعدادًا للشراء داخل التطبيق)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">كلفة التعلم</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مفاهيم أكثر (المكونات الأربعة وغيرها)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">نظام مغلق لكنه موحد وبتوثيق ممتاز</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
مقارنة بين مساري تطوير Android و iOS (أغسطس 2026)

لنتحدث بصراحة: إذا لم يكن حاسوبك من نوع Mac، فلا يوجد أصلًا سؤال للتفكير فيه — Android هو الخيار الوحيد. أما إذا كان لديك Mac، فيمكنك قراءة الجزأين الثامن والتاسع من هذا الكتاب بالتوازي، فالأفكار البرمجية واحدة، وبتعلم أحد المسارين سيصبح تعلم الآخر أسرع بكثير.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
لنتجرب: انظر إلى نظام Android في هاتفك

{class="mt-1"}
افتح في هاتفك [الإعدادات] > [حول الهاتف] (أو «حول هذا الجهاز»)، وابحث عن السطر الخاص بـ«إصدار Android» — وانقر عليه عدة نقرات متتابعة لتفعيل لعبة المفاجآت المخفية في النظام. دوّن رقم الإصدار لديك وقارنه بالجدول أعلاه لترى إلى أي جيل ينتمي. هاتفك هو أول «جهاز اختبار للتطوير» لديك.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
خلاصة الفصل

- وُلد Android عام 2008، وفي 2026 أصبح النظام المحمول الأكبر حصةً سوقية عالميًا بمليارات الأجهزة النشطة
- أحدث إصدار رسمي هو Android 17؛ والتطبيقات الرئيسية تدعم كحد أدنى Android 8-10 لتكون قاعدة المستخدمين واسعة بما يكفي
- استخدم Kotlin في كل مشروع جديد: كود أقل بنسبة 30%+، وحماية من المؤشرات الفارغة، وهو الاختيار الرسمي المعتمد
- ملف APK تثبته بنفسك، وصيغة AAB للمتجر؛ وSDK هي حزمة أدوات التطوير الرسمية
- حزمة التقنيات القياسية لعام 2026: Kotlin + Compose + MVVM + Room + Retrofit + Gradle + Android Studio
:::
