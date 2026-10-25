---
id: di-wu-shi-san-zhang
num: 53
part: an-zhuo-kai-fa-pian
nav: الفصل 53: تخزين البيانات وطلبات الشبكة
toc: default
kind: chapter
---

### الفصل 53: تخزين البيانات وطلبات الشبكة

{class="chapter-intro mb-4"}
التطبيق الذي "يرى" فقط هو تطبيق ميت؛ أما الذي يخزن البيانات ويتصل بالشبكة فهو حي. في هذا الفصل سنتعرف على "الثلاثية" لطبقة بيانات Android: DataStore (لتخزين الإعدادات الصغيرة)، وRoom (لتخزين البيانات المهيكلة)، وRetrofit (للحديث مع الخوادم)، إضافة إلى "المنسق العام" لها — الكوروتينات. بعد هذا الفصل ستكتب تطبيقًا حقيقيًا يتذكر عادات المستخدم ويحدّث محتواه لحظيًا.

#### أولًا: كيف تختار حل التخزين: انظر هذا الجدول أولًا

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الحل</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ماذا يخزن</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الخصائص</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">أين استخدمناه في الكتاب</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DataStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">إعدادات متفرقة (المظهر، المفاتيح)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">أزواج مفتاح-قيمة، بسيطة وآمنة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">إعدادات دفتر الحسابات في الفصل 54</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">بيانات مهيكلة (العمليات المالية، المستخدمون)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تغليف حقيقي لقاعدة بيانات SQLite، قابل للاستعلام</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">سجلات العمليات في الفصل 54</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">بيانات الخادم (لا تُخزن بل تُجلب عبر الشبكة)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">المعيار الفعلي لمكتبات طلبات HTTP</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">بيانات الطقس في الفصل 55</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
تقسيم عمل ثلاثية البيانات

احفظ القاعدة: "الإعدادات الصغيرة في DataStore، والبيانات المجمعة في Room، وبيانات الخارج عبر Retrofit". أما SharedPreferences الشائعة في الدروس القديمة فقد حلّ محلها DataStore، وكتابة SQL يدويًا في SQLite حلّ محلها Room — تعلّم الجديد مباشرة ولا تسلك الطريق القديم.

#### ثانيًا: DataStore: لتخزين الإعدادات الصغيرة

لتذكر قيم متفرقة مثل "العملة التي اختارها المستخدم آخر مرة" و"هل الوضع الداكن مفعّل" استخدم DataStore (نسخة Preferences):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · مثال DataStore</span><span class="dots">···</span>
:::

```
val Context.dataStore by preferencesDataStore(name = "settings")

// كتابة: تخزين قيمة
suspend fun saveTheme(isDark: Boolean) {
    context.dataStore.edit { prefs ->
        prefs[THEME_KEY] = isDark
    }
}

// القراءة: استخراج القيمة (Flow يبلّغ عن التغييرات تلقائيًا)
val themeFlow: Flow<Boolean> = context.dataStore.data
    .map { it[THEME_KEY] ?: false }
```
:::

انتبه إلى أن الدالة تعيد Flow — وهو تدفق بيانات "يجري". متى تغيرت القيمة استلمت كل المواضع التي تراقبها القيمة الجديدة تلقائيًا. هذا المفهوم (الاستجابية) حجر الأساس في Android الحديثة، وسنطبقه عمليًا في الفصل 54.

#### ثالثًا: Room: بيت "حقيقي" للبيانات

دفتر الحسابات فيه مئات وآلاف العمليات، مع استعلام وإحصاء حسب الفئة والشهر — وهذا يتطلب قاعدة بيانات. Room هي التغليف الرسمي لـ SQLite، تجعل "إنشاء الجداول والاستعلام" طبيعيًا ككتابة Kotlin. ثلاثة أشياء:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · ثلاثية Room: Entity / Dao / Database</span><span class="dots">···</span>
:::

```
// 1. ‏Entity: بنية الجدول (جدول واحد = data class واحد)
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val amount: Double,
    val category: String,
    val note: String,
    val date: String
)

// 2. ‏Dao: واجهة العمليات (إضافة وحذف وتعديل واستعلام)
@Dao
interface RecordDao {
    @Query("SELECT * FROM records ORDER BY date DESC")
    fun getAll(): Flow<List<Record>>

    @Insert
    suspend fun insert(record: Record)

    @Delete
    suspend fun delete(record: Record)

    @Query("SELECT SUM(amount) FROM records WHERE category = :c")
    suspend fun sumByCategory(c: String): Double
}

// 3. ‏Database: التجميع النهائي
@Database(entities = [Record::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun recordDao(): RecordDao
}
```
:::

قالب "الثلاثية" هذا يمكن نقله كما هو إلى أي مشروع من مشاريعك — يكفي تغيير أسماء الحقول. الاستعلام يعيد Flow فتتحدث الواجهة تلقائيًا مع البيانات — رائع بلا حدود.

#### رابعًا: Retrofit: الحديث مع الخادم

الطقس والأخبار وأسعار الصرف… هذه البيانات ليست في الهاتف بل على خوادم الآخرين. Retrofit تجعل "طلب البيانات من الخادم" بسيطًا كاستدعاء دالة. ثلاث خطوات:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Retrofit في ثلاث خطوات</span><span class="dots">···</span>
:::

```
// 1. تعريف الواجهة: وصف طلبات HTTP كدوال
interface WeatherApi {
    @GET("v1/weather")
    suspend fun getWeather(@Query("city") city: String): WeatherResponse
}

// 2. إنشاء الكائن
val api = Retrofit.Builder()
    .baseUrl("https://api.example.com/")
    .addConverterFactory(GsonConverterFactory.create())
    .build()
    .create(WeatherApi::class.java)

// 3. الاستدعاء كأنه دالة (داخل كوروتين)
val result = api.getWeather("الرياض")
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
تحذير من الفخاخ: قاعدتان حديديتان للشبكة

{class="mt-1"}
① لا يجوز أبدًا إجراء طلب الشبكة في الخيط الرئيسي — فسيجمّد الواجهة وقد ينهار التطبيق (NetworkOnMainThreadException). وكل استدعاءات الشبكة يجب أن توضع داخل كوروتين (viewModelScope.launch). ② يُمنع HTTP غير المشفر افتراضيًا: من Android 9 فما فوق يُطلب HTTPS. لاستخدام عنوان محلي بصيغة http:// أثناء الاختبار عليك التصريح بذلك عبر usesCleartextTraffic في الـ Manifest — لكن المنتجات الرسمية يجب أن تعتمد HTTPS بالكامل.
:::

#### خامسًا: تحليل JSON: "ترجمة" بيانات الشبكة

أغلب البيانات التي يعيدها الخادم بصيغة JSON — نص يشبه "قاموسًا متداخلًا". يحتاج Retrofit إلى "مترجم" يحولها إلى كائنات Kotlin. الحلان السائدان في 2026:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الحل</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الخصائص</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الحالة الموصى بها</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gson / Moshi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الحل القديم المعتمد على الانعكاس، تكوينه بلا كلفة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الانطلاق السريع والمشاريع الصغيرة قليلة الحقول</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">kotlinx.serialization</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الحل الرسمي في زمن الترجمة (compile-time)، أسرع وأكثر أمانًا</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الخيار الأول للمشاريع الجديدة (السائد في 2026)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
حلا تحليل JSON الرئيسيان

::: div .code-block
:::inline div .code-head
<span>KOTLIN · مثال kotlinx.serialization</span><span class="dots">···</span>
:::

```
// أضف تعليق @Serializable إلى صنف البيانات
@Serializable
data class WeatherResponse(
    val weather: List<Weather>,
    val main: Main,
    val name: String
)

// يُركَّب على Retrofit الـ Converter المناسب (مثال بالدعم الرسمي من Retrofit 2.11+):
// .addConverterFactory(json.asConverterFactory("application/json".toMediaType()))
```
:::

مهما اخترت الحل، القاعدة الحديدية: انظر إلى JSON الفعلي المعاد أولًا ثم عرّف الحقول. كثير من أخطاء "فشل التحليل" سببها اسم حقل خاطئ أو مستوى تداخل مخمَّن — اطبع JSON الخام وقارنه وستحدد المشكلة في عشر ثوانٍ.

#### سادسًا: الكوروتينات: "اللغة المشتركة" للتوازي في Android

الكلمتان suspend و launch المتكررتان أعلاه تأتيان من كوروتينات Kotlin (Coroutine) — الحل الرسمي للتوازي في Android. يمكن فهمها ببساطة: العمليات التي "تحتاج انتظارًا قليلًا" (الشبكة، قاعدة البيانات) لا تحجب الواجهة.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · أول تجربة مع الكوروتينات</span><span class="dots">···</span>
:::

```
// إطلاق كوروتين داخل الـ ViewModel
viewModelScope.launch {
    val records = dao.getAll().first()  // suspend: يعلّق نفسه وينتظر تلقائيًا
    // تحديث حالة الواجهة…
}

// تذكير سريع بالكلمات المفتاحية:
// suspend   —— "عليّ الانتظار، لا تعطّل الآخرين"
// launch    —— "يلا نبدأ!"
// viewModelScope —— "ورشة العمل" التي تتبع الشاشة؛ تُغلق تلقائيًا عند تدمير الشاشة
```
:::

في مرحلة المبتدئ اكتفِ بحفظ طريقة الاستخدام؛ ومبدأ "التعليق والاستئناف" وراءها يمكنك دراسته لاحقًا. في التطوير اليومي ستكتب في 90% من الوقت بهذا القالب نفسه.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
لنتجرب: اصنع تطبيق "جملة اليوم"

{class="mt-1"}
ابحث عن API مجاني للاقتباسات (مثل hitokoto أو شبيهاته)، واستخدم Retrofit لجلب "جملة اليوم" وعرضها في وسط الشاشة، وأضف زر "جملة أخرى" (طلب جديد داخل كوروتين). ثم خزّن الجمل المفضلة في "المفضلة" باستخدام Room. هذا التمرين يستخدم DataStore وRoom وRetrofit والكوروتينات كلها — وبعد إنجازه سيكون الفصلان 7 و8 أمرًا يسيرًا للغاية.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
خلاصة الفصل

- القاعدة: الإعدادات الصغيرة في DataStore، والبيانات المجمعة في Room، وبيانات الخارج عبر Retrofit
- DataStore يعيد Flow: متى تغيرت القيمة وصلت إلى المراقبين تلقائيًا
- ثلاثية Room: @Entity (الجدول) + @Dao (العمليات) + @Database (التجميع النهائي)، وقالب قابل لإعادة الاستخدام مباشرة
- خطوات Retrofit الثلاث: تعريف الواجهة ← إنشاء النسخة ← الاستدعاء داخل كوروتين
- قاعدتان حديديتان: الشبكة لا تدخل الخيط الرئيسي؛ والمنتج الرسمي يجب أن يعتمد HTTPS
- الكوروتين = انتظار لا يحجب الواجهة؛ وviewModelScope هو ورشة العمل الخاصة بالصفحة
:::
