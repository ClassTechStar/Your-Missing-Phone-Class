---
id: di-wu-shi-si-zhang
num: 54
part: an-zhuo-kai-fa-pian
nav: الفصل 54: المشروع الأول — دفتر حساباتي (نسخة محلية)
toc: default
kind: chapter
---

### الفصل 54: المشروع الأول — دفتر حساباتي (النسخة المحلية)

{class="chapter-intro mb-4"}
مرحبًا بك في أول "مشروع جاد" لك. هذا الدفتر لا يتصل بالإنترنت لكنه متكامل الأركان: يسجّل عملية مالية، ويعرض سجل العمليات، ويحصي شهريًا، ويتيح الحذف والتعديل. بعد إنجازه ستكون قد مررت بدورة كاملة "بيانات ← منطق ← واجهة". لا تستعجل نسخ الكود — فكّر أولًا ثم نفّذ، وهذا مبدؤنا الدائم.

#### أولًا: التفكير في المتطلبات: اسأل خمسة أسئلة أولًا

قبل التنفيذ رتّب فكرتك بعناصر المتطلبات الخمسة:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">العنصر</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الجواب</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who (لمن؟)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">لأجلك، وللأهل والأصدقاء أيضًا</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What (ماذا؟)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تسجيل الدخل والمصروف، وعرض السجل، والملخص الشهري، والإحصاء حسب الفئة</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why (لماذا؟)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تمرين عملي + معرفة أين تذهب الأموال</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How (كيف؟)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin + Compose + Room + MVVM، محلي بالكامل دون خادم خلفي</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint (القيود)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الإنجاز خلال أسبوع؛ الحد الأدنى Android 8؛ وحتى لو لم يُنشر يُكتب بمعايير النشر</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
عناصر المتطلبات الخمسة لدفتر الحسابات

ثم قسّمه إلى خطوات صغيرة "قابلة للاستخدام" كل واحدة بمفردها: ① بناء طبقة بيانات Room (تخزين عملية واحدة)؛ ② صفحة القائمة (عرض السجل)؛ ③ صفحة الإدخال (إضافة عملية)؛ ④ الحذف والتعديل؛ ⑤ بطاقة الملخص الشهري. بعد كل خطوة سيكون التطبيق "شيئًا قابلًا للاستخدام".

#### ثانيًا: طبقة البيانات: بيت لـ"العملية المالية"

عرّف أولًا شكل العملية المالية — الحقول كافية دون جشع:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Record.kt (كيان)</span><span class="dots">···</span>
:::

```
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val type: String,        // "income" إيراد | "expense" مصروف
    val amount: Double,      // المبلغ (يوان)
    val category: String,    // التصنيف: طعام، مواصلات، راتب…
    val note: String = "",   // ملاحظة (اختياري)
    val date: String         // "2026-08-15"
)
```
:::

أضف إلى الـ Dao استعلامين "للإحصاء" — وهما روح دفتر الحسابات:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordDao.kt (استعلامات إحصاء)</span><span class="dots">···</span>
:::

```
@Dao
interface RecordDao {
    @Query("SELECT * FROM records ORDER BY date DESC, id DESC")
    fun getAll(): Flow&lt;List&lt;Record&gt;&gt;

    @Insert
    suspend fun insert(record: Record)

    @Delete
    suspend fun delete(record: Record)

    @Query("SELECT COALESCE(SUM(amount),0) FROM records WHERE type='income' AND date LIKE :month || '%'")
    suspend fun monthIncome(month: String): Double   // month بصيغة "2026-08"

    @Query("SELECT COALESCE(SUM(amount),0) FROM records WHERE type='expense' AND date LIKE :month || '%'")
    suspend fun monthExpense(month: String): Double
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
نصيحة: لماذا نستخدم Double للمبلغ؟

{class="mt-1"}
التطبيقات المالية الدقيقة تستخدم BigDecimal أو "Int بوحدة العملة الصغرى" لتجنب أخطاء الفاصلة العائمة (المشكلة القديمة 0.1+0.2≠0.3). لمشروع تمرين يكفي Double؛ وإذا صنعت يومًا منتجًا ماليًا حقيقيًا فتذكّر التحويل إلى "الوحدة الصغرى" — فخ قديم تعثّر فيه كثيرون من أسلافنا.
:::

#### ثالثًا: MVVM: "فصل" الواجهة عن المنطق

تجعل الواجهة تتعامل مع قاعدة البيانات مباشرة؟ يعمل، لكن كود الواجهة سيصبح طويلًا مقهرًا. بنية MVVM توزع الأدوار: View (الواجهة) ترسم فقط، وViewModel (مركز المنطق) يدير البيانات، وModel (Room) يدير التخزين.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> العرض (واجهة Compose)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel (الحالة والمنطق)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model (طبقة بيانات Room)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
الشكل 5: بنية MVVM ثلاثية الطبقات — البيانات تجري باتجاه واحد، وكل طبقة لا تتجاوز حدودها
:::

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordViewModel.kt (هيكل)</span><span class="dots">···</span>
:::

```
class RecordViewModel(private val dao: RecordDao) : ViewModel() {

    // يحوّل الـ Flow إلى حالة تستطيع الواجهة مراقبتها
    val records = dao.getAll()
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(), emptyList())

    // عمليات المستخدم: استدعاء دوال suspend
    fun addRecord(type: String, amount: Double, category: String, note: String, date: String) {
        viewModelScope.launch {
            dao.insert(Record(type = type, amount = amount,
                category = category, note = note, date = date))
        }
    }

    fun deleteRecord(record: Record) {
        viewModelScope.launch { dao.delete(record) }
    }
}
```
:::

في الواجهة (Compose) تستخدمها هكذا: val vm: RecordViewModel = viewModel() ثم val list by vm.records.collectAsState() — متى تغيرت البيانات تحدث القائمة تلقائيًا دون أن تفعل شيئًا. هذه قوة اجتماع MVVM وFlow وCompose الثلاثة معًا.

#### رابعًا: الواجهة: صفحة القائمة + صفحة الإدخال

استخدم في صفحة القائمة LazyColumn (قائمة التحميل الكسول) — لن تتجمد مهما كثرت البيانات:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · شاشة قائمة المصروفات (مقطع رئيسي)</span><span class="dots">···</span>
:::

```
@Composable
fun RecordListScreen(vm: RecordViewModel) {
    val records by vm.records.collectAsState()

    Column {
        // بطاقة الملخص العلوية (الإيرادات - المصروفات = الرصيد)
        SummaryCard(records)

        // قائمة الحركات
        LazyColumn {
            items(records, key = { it.id }) { record -&gt;
                RecordRow(record) { vm.deleteRecord(record) }
            }
        }

        // زر عائم "تسجيل مصروف" → يفتح نافذة الإدخال
        FloatingActionButton(onClick = { showAddDialog = true }) {
            Text("+")
        }
    }
}

@Composable
fun RecordRow(record: Record, onDelete: () -&gt; Unit) {
    Row(Modifier.fillMaxWidth().padding(12.dp)) {
        Text(record.category, fontWeight = FontWeight.Bold)
        Spacer(Modifier.weight(1f))
        Text(if (record.type == "income") "+${record.amount}" else "-${record.amount}",
             color = if (record.type == "income") Color(0xFF27AE60) else Color(0xFFC0392B))
    }
}
```
:::

أما الإدخال فأسهل حل هو AlertDialog (نافذة حوار): بضعة حقول إدخال + مبدّل دخل/مصروف + قائمة فئات منسدلة، وعند النقر على تأكيد يُستدعى vm.addRecord(...).

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
تنبيه: لا تتهاون في التحقق من المدخلات

{class="mt-1"}
لا بد من التحقق من حقل المبلغ: أوقف القيم الفارغة والسالبة والمدخلات غير الصالحة مثل "abc" (استخدم toDoubleOrNull() للفحص). من أكثر أسباب انهيار التطبيقات شيوعًا "اعتبار مدخلات المستخدم ولدًا مطيعًا". تذكّر: كل ما يدخله المستخدم عاملَه كعدو وافحصه.
:::

#### خامسًا: التعديل والحذف: بيانات "تدخل وتخرج"

دفتر حسابات يضيف ولا يحذف يصبح عديم الفائدة بعد ثلاثة أيام. أضف عمليتين:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · الحذف والتعديل</span><span class="dots">···</span>
:::

```
// أضف دالتين إلى الـ Dao:
@Query("UPDATE records SET amount=:amount, category=:category, note=:note WHERE id=:id")
suspend fun update(id: Long, amount: Double, category: String, note: String)

@Query("DELETE FROM records WHERE id=:id")
suspend fun deleteById(id: Long)

// في الواجهة: الضغط المطول على عنصر يفتح قائمة "تعديل/حذف" (في Compose استخدم DropdownMenu أو AlertDialog)
// قبل الحذف يُستحسن إظهار مربع تأكيد — "الحذف الخاطئ" أكثر ما يكره مستخدمو تطبيقات تتبع المصروفات
```
:::

خبرتان في تفاصيل التفاعل: الحذف يجب أن يُؤكد مرتين (لمنع الزلل)، والتعديل يُعبأ مسبقًا بالقيمة الأصلية قدر الإمكان (تعديل حرف أسهل من إعادة الكتابة كاملة). لا تحتقر هاتين التفصيلتين — فـ"الإحساس بالمنتج" يُبنى من تفاصيل كهذه.

#### سادسًا: القبول: فحص ثلاثي الطبقات + تحديان متقدميان

بعد إنجاز المشروع اقبله بفحص ثلاث طبقات "الوظائف ← الحدود ← البنية": هل يسجل؟ هل يحذف؟ هل تبقى البيانات بعد إعادة فتح التطبيق (الوظائف)؛ هل ينهار عند إدخال 0 أو رقم سالب للمبلغ، وهل تضيع البيانات عند تدوير الشاشة (الحدود)؛ هل اختلطت الواجهة بالبيانات، وهل الحقول مثبتة في الكود (البنية).

بعد اجتياز قبول النسخة الأساسية أضف لنفسك "طبقين متقدمين":

1. التصفية الشهرية: أضف مبدّل أشهر في الأعلى (مثل 2026-08 ▾) فتعرض القائمة عمليات الشهر المختار فقط؛
2. المخطط الدائري للفئات: استخدم Canvas في Compose أو مكتبة رسوم بيانية خفيفة لتحويل "أين تذهب الأموال" إلى مخطط دائري — بعد هذا سيبدو الدفتر "شكل منتج حقيقي".

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
لنتجرب: أنجزها هذا الأسبوع

{class="mt-1"}
نفّذ بالترتيب "طبقة البيانات ← ViewModel ← صفحة القائمة ← صفحة الإدخال ← بطاقة الملخص"، خطوة كل يوم. إذا علقت فألقِ رسالة الخطأ كما هي إلى محرك البحث أو الذكاء الاصطناعي (أتذكر الجزء السابع "ممارسة البرمجة بالذكاء الاصطناعي"؟ عند وصف المشكلة وضّح "السلوك المتوقع، السلوك الفعلي، خطوات إعادة إنتاجها"). وبعد الإنجاز استخدمه لتسجيل نفقات أسبوع كامل — فاستخدام تطبيق صنعته بنفسك يمنحك شعورًا بالإنجاز يدفعك للمضي قدمًا.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
خلاصة الفصل

- عناصر المتطلبات الخمسة ← تقسيمها إلى خطوات صغيرة "كل خطوة قابلة للاستخدام" ثم التنفيذ
- طبقة البيانات: كيان Record + Dao (بما فيه SQL للإحصاء الشهري) + Database
- تقسيم MVVM: View ترسم فقط، وViewModel يدير المنطق، وModel يدير التخزين
- Flow + stateIn + collectAsState: متى تغيرت البيانات تحدث الواجهة تلقائيًا
- LazyColumn قائمة التحميل الكسول؛ وAlertDialog للإدخال
- قبول ثلاثي الطبقات (الوظائف/الحدود/البنية) + التحديان المتقدميان (التصفية الشهرية، المخطط الدائري للفئات)
:::
