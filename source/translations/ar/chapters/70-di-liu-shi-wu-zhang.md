---
id: di-liu-shi-wu-zhang
num: 65
part: ios-kai-fa-pian
nav: الفصل 65: المشروع الأول — دفتر حساباتي (نسخة محلية)
toc: default
kind: chapter
---

### الفصل 65: المشروع الأول — دفتر حساباتي (نسخة محلية)

{class="chapter-intro mb-4"}
مرحبًا بك في «مشروعك الجاد» الأول. هذا الدفتر لا يتصل بالشبكة، لكنه مكتمل الأركان: يسجل عملية مالية، ويعرض كشف الحساب، ويجمع الإحصاءات شهريًا، ويتيح الحذف والتعديل. وبإتمامه تكون قد قطعت كامل الدورة «بيانات → منطق → واجهة». ولا تتسرع في نسخ الكود — فكر بوضوح أولًا ثم انطلق، فهذا مبدؤنا الدائم.

#### أولًا: التفكير في المتطلبات — اسأل خمسة أسئلة أولًا

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">العنصر</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الجواب</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who (لمن يُستخدم)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">لنفسك، ويصلح للعائلة والأصدقاء أيضًا</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What (ماذا يفعل)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تسجيل الدخل والمصروف، وعرض كشف الحركة، وجمع شهري، وإحصاء حسب الفئات</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why (لماذا)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تدريب عملي + معرفة أين ذهبت الأموال</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How (كيف يُبنى)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift + SwiftUI + SwiftData + MVVM، محلي بالكامل دون خادم خلفي</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint (القيود)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الإنجاز خلال أسبوع؛ الحد الأدنى للدعم iOS 17 (شرط SwiftData)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
عناصر المتطلبات الخمسة لدفتر الحسابات

ثم فككه إلى خطوات صغيرة «كل خطوة منها قابلة للاستخدام»: ① بناء طبقة بيانات SwiftData (تستطيع تخزين عملية)؛ ② صفحة القائمة (تستطيع عرض الكشف)؛ ③ نافذة الإدخال (تستطيع إضافة عملية)؛ ④ الحذف والتحرير؛ ⑤ بطاقة الملخص الشهري. وبعد كل خطوة يبقى التطبيق «شيئًا قابلًا للاستخدام».

#### ثانيًا: طبقة البيانات — بيت لـ«الحساب»

عرّف أولًا شكل العملية المالية الواحدة — فالحقول ينبغي أن تكفي دون طمع:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Record.swift (نموذج)</span><span class="dots">···</span>
:::

```
import SwiftData

@Model
class Record {
    var type: String      // "income" إيراد | "expense" مصروف
    var amount: Double    // المبلغ (يوان)
    var category: String  // التصنيف: طعام، مواصلات، راتب…
    var note: String      // ملاحظة (اختياري)
    var date: Date        // تاريخ التسجيل

    init(type: String, amount: Double, category: String, note: String = "", date: Date = Date()) {
        self.type = type
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
نصيحة: لماذا نستخدم Double للمبلغ؟

{class="mt-1"}
تستخدم تطبيقات المال الدقيقة النوع Decimal (عشري دقيق) لتجنب أخطاء الفاصلة العائمة (المشكلة القديمة 0.1+0.2≠0.3). وفي مشروع تدريبي يكفي Double؛ وإذا جاء يوم تصنع فيه منتجًا ماليًا حقيقيًا فتذكر حينها التحول إلى Decimal أو «عدد صحيح Int بوحدة السنتات» — فخ حذرت منه أجيال من المبرمجين قبلك.
:::

#### ثالثًا: MVVM — «فصل الواجهة عن المنطق»

أن تجعل الواجهة تتعامل مع قاعدة البيانات مباشرة؟ يعمل، لكن كود الواجهة سيصير طويلًا فاحشًا. تجعل معمارية MVVM كلًا يؤدي دوره: الواجهة View ترسم فقط، ونموذج العرض ViewModel (مركز المنطق) يدير البيانات، والنموذج Model (SwiftData) يتولى التخزين.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> العرض (واجهة SwiftUI)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel (مركز المنطق @Observable)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model (طبقة بيانات SwiftData)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
شكل 4: البنية ثلاثية الطبقات في MVVM — تتدفق البيانات في اتجاه واحد، ولا تجاوز أي طبقة حدودها
:::

::: div .code-block
:::inline div .code-head
<span>SWIFT · RecordViewModel.swift (هيكل)</span><span class="dots">···</span>
:::

```
import Observation

@Observable
class RecordViewModel {
    var records: [Record] = []
    private let context: ModelContext

    init(context: ModelContext) { self.context = context }

    func load() {
        // تصفية بـ #Predicate من SwiftData + ترتيب
        let descriptor = FetchDescriptor<Record>(
            sortBy: [SortDescriptor(\.date, order: .reverse)]
        )
        records = (try? context.fetch(descriptor)) ?? []
    }

    func add(type: String, amount: Double, category: String, note: String) {
        let r = Record(type: type, amount: amount, category: category, note: note)
        context.insert(r)
        try? context.save()
        load()                       // إعادة تحميل، وتتحدث الواجهة
    }

    func delete(_ record: Record) {
        context.delete(record)
        try? context.save()
        load()
    }
}
```
:::

في الواجهة تكتب @State private var vm = RecordViewModel(...) ثم تعرض القائمة مباشرة من vm.records — فبمجرد تغير البيانات تنعكس الواجهة تلقائيًا.

#### رابعًا: الواجهة — صفحة القائمة ونافذة الإدخال

::: div .code-block
:::inline div .code-head
<span>SWIFT · شاشة قائمة المصروفات (مقطع رئيسي)</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var vm: RecordViewModel
    @State private var showAdd = false

    var body: some View {
        NavigationStack {
            List {
                Section("رصيد الشهر") {          // بطاقة الملخص
                    SummaryRow(records: vm.records)
                }
                Section("الحركات") {
                    ForEach(vm.records) { r in
                        RecordRow(record: r)
                    }
                    .onDelete { idx in
                        idx.forEach { vm.delete(vm.records[$0]) }
                    }
                }
            }
            .navigationTitle("دفتر مصروفاتي")
            .toolbar {
                Button { showAdd = true } label: {
                    Image(systemName: "plus")
                }
            }
            .sheet(isPresented: $showAdd) {
                AddRecordView(vm: vm)          // نافذة الإدخال
            }
        }
    }
}
```
:::

نقاط نافذة الإدخال: لوحة مفاتيح حقل المبلغ من نوع .keyboardType(.decimalPad) (لوحة أرقام)، والدخل/المصروف عبر أداة مقسمة (Picker)، والفئة عبر قائمة اختيار، وعند الضغط على «حفظ» تستدعي vm.add(...) ثم dismiss() لإغلاق النافذة.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
تنبيه: لا تكاسل في التحقق من المدخلات

{class="mt-1"}
حقل المبلغ يجب التحقق منه حتمًا: اعترض القيم الفارغة والسالبة والمدخلات غير الصالحة مثل "abc" (بالحكم عبر Double(text) الذي يعيد nil عند الفشل). فمن أكثر أسباب انهيار التطبيقات شيوعًا «معاملة مدخلات المستخدم كطفل مطيع». وتذكر: كل ما يدخله المستخدم عاملُه كعدو يخضع للتفتيش.
:::

#### خامسًا: التحرير والحذف والملخص

- الحذف: .onDelete في List للحذف بسحب لليسار + نافذة تأكيد (فالحذف الخاطئ أكثر ما يكره مستخدمو تطبيقات الحسابات)؛
- التحرير: النقر على صف يفتح نافذة تحرير معبأة مسبقًا بالقيم الأصلية (تصحيح حرف واحد أسهل من إعادة الإدخال)؛
- الملخص: حساب «دخل الشهر / مصروفه / الرصيد» عبر filter مع reduce وعرضها في بطاقة أعلى الصفحة:

::: div .code-block
:::inline div .code-head
<span>SWIFT · حساب الملخص الشهري</span><span class="dots">···</span>
:::

```
func monthSummary(_ records: [Record]) -> (income: Double, expense: Double) {
    let cal = Calendar.current
    let monthRecords = records.filter {
        cal.isDate($0.date, equalTo: Date(), toGranularity: .month)
    }
    let income = monthRecords
        .filter { $0.type == "income" }
        .reduce(0) { $0 + $1.amount }
    let expense = monthRecords
        .filter { $0.type == "expense" }
        .reduce(0) { $0 + $1.amount }
    return (income, expense)
}
```
:::

#### سادسًا: القبول — فحص بثلاث طبقات وتحديان متقدمان

بعد إنهاء المشروع اقبله على ثلاث طبقات وفق «الوظائف → الحدود → المعمارية»: هل يسجل وهل يحذف وهل تبقى البيانات بعد إعادة تشغيل التطبيق (الوظائف)؛ هل ينهار عند إدخال 0 أو رقم سالب في المبلغ (الحدود)؛ هل اختلطت الواجهة بالبيانات وهل الحقول مكتوبة بشكل ثابت داخل الكود (المعمارية).

بعد نجاح النسخة الأساسية في القبول، أضف لنفسك «طبقين متقدمين»:

1. إحصاء الفئات: أضف علامة تبويب «إحصاءات»، وارسم مصروفات الفئات دائريًا أو أعمدة باستخدام Swift Charts — مكتبة الرسوم الرسمية من Apple، بضعة أسطر كود تنتج الرسم؛
2. مزامنة iCloud: تفعيل مزامنة iCloud في SwiftData لا يتطلب سوى ضبط بضع إعدادات — فيتزامن الدفتر تلقائيًا بين iPhone وiPad، ويرتقي المشروع فورًا إلى مستوى «راقٍ».

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
هيا نجرّب: أكمله خلال هذا الأسبوع

{class="mt-1"}
انطلق بالترتيب «طبقة البيانات → ViewModel → صفحة القائمة → نافذة الإدخال → بطاقة الملخص»، خطوة كل يوم. وإذا علقت فاطرح رسالة الخطأ كما هي على محرك البحث أو على الذكاء الاصطناعي (أتذكر الجزء السابع «البرمجة العملية بالذكاء الاصطناعي»؟ عند وصف المشكلة وضح «السلوك المتوقع، والسلوك الفعلي، وخطوات إعادة الإنتاج»). وبعد الانتهاء سجل به حسابات أسبوع كامل — فاستخدام تطبيق صنعته بنفسك يولد شعور الإنجاز الذي يدفعك إلى مواصلة الطريق.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
خلاصة الفصل

- عناصر المتطلبات الخمسة → تفكيكها إلى خطوات صغيرة «كل خطوة قابلة للاستخدام» ثم الشروع في العمل
- طبقة البيانات: نموذج @Model + حاوية modelContainer + استعلام FetchDescriptor
- توزيع أدوار MVVM: الواجهة View ترسم فقط، وViewModel المبني على @Observable يدير المنطق، وSwiftData يتولى التخزين
- الواجهة: List مع Section مع toolbar ونافذة الإدخال sheet
- قبول بثلاث طبقات (الوظائف / الحدود / المعمارية) + تحديان متقدمان (Swift Charts ومزامنة iCloud)
:::
