---
id: di-liu-shi-san-zhang
num: 63
part: ios-kai-fa-pian
nav: الفصل 63: العروض والحالة والتنقل
toc: default
kind: chapter
---

### الفصل 63: العروض والحالة والتنقل

{class="chapter-intro mb-4"}
أصبحت تعرف صناعة التطبيقات الصغيرة ذات الصفحة الواحدة. يعالج هذا الفصل مسألتَي «النمو»: كيف تتنقل بين عدة صفحات (التنقل)، وكيف تتدفق البيانات بين الصفحات (إدارة الحالة). وبإتمام هذا الفصل ستستطيع بناء الهيكل الكلاسيكي لتطبيق متعدد الصفحات: «قائمة → تفاصيل → تحرير».

#### أولًا: «المشهد الكامل» لتدفق البيانات في إدارة الحالة

أدوات الحالة في SwiftUI لا تقتصر على @State. انظر أولًا إلى هذه الصورة الشاملة لتفهم «متى تستخدم أيّها»:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الأداة</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ماذا تدير</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">من يستخدمها</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">السيناريو النموذجي</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">حالة مؤقتة خاصة بالصفحة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">العرض الحالي</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">العدادات ونص حقول الإدخال</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Binding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">استعارة حالة من جهة أخرى</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">عرض فرعي يعدل عرضًا أبًا</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">المكونات المخصصة</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@StateObject / @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">منطق مشترك بين الصفحات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">نموذج العرض (ViewModel)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تحميل البيانات ومنطق الأعمال</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@EnvironmentObject / .environment</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">حالة مشتركة عالميًا</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">التطبيق بأكمله</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">حالة تسجيل دخول المستخدم وإعدادات السمة</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
منظور شامل لأدوات الحالة في SwiftUI (في عام 2026 صار @Observable هو السائد)

::: div .code-block
:::inline div .code-head
<span>SWIFT · المعيار في 2026: نماذج عرض مع @Observable</span><span class="dots">···</span>
:::

```
// الأسلوب الحديث في iOS 17+: ماكرو @Observable (موصى به للمشاريع الجديدة)
import Observation

@Observable
class CounterModel {                 // نموذج العرض
    var count = 0
    func increment() { count += 1 }
}

struct CounterView: View {
    @State private var model = CounterModel()   // يحتفظ بالنموذج

    var body: some View {
        VStack {
            Text("ضغطت \(model.count) مرات")
            Button("اضغط هنا") { model.increment() }
        }
    }
}
```
:::

نصيحة صريحة بلا مجاملة للمبتدئين: ما هو خاص بالصفحة فاستخدم له @State، وما هو عابر للصفحات أو ذا منطق فاستخدم له صنف @Observable. أما @StateObject/@ObservableObject في الدروس القديمة فهو أسلوب الجيل السابق؛ يكفي أن تقرأه وتفهمه، وفي الكود الجديد اتبع ما مرّ أعلاه.

#### ثانيًا: NavigationStack — «المكدس» الذي ينقل بين الصفحات

منذ iOS 16 يُستخدم NavigationStack للتنقل بين عدة صفحات — فهو كرصة أطباق: تدفع طبقًا فدخله، وعند العودة تُسحب الأطباق واحدًا تلو الآخر:

::: div .code-block
:::inline div .code-head
<span>SWIFT · التنقل مع NavigationStack</span><span class="dots">···</span>
:::

```
struct HomeView: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("دفتر أحمد") {
                    DetailView(name: "دفتر أحمد")   // الشاشة الهدف
                }
                NavigationLink("دفتر سارة") {
                    DetailView(name: "دفتر سارة")
                }
            }
            .navigationTitle("قائمة الدفاتر")   // عنوان كبير في الأعلى
        }
    }
}

struct DetailView: View {
    let name: String
    var body: some View {
        Text("تفاصيل \(name)")
            .navigationTitle(name)
            .navigationBarTitleDisplayMode(.inline)
    }
}
```
:::

NavigationLink هو «رابط تنقل قابل للنقر»؛ وnavigationTitle يولد تلقائيًا عنوان شريط التنقل وزر الرجوع. وعندما تحتاج إلى تنقل برمجي (كالعودة تلقائيًا بعد الضغط على «حفظ»)، استخدم @Environment(\.dismiss) لإغلاق الصفحة الحالية — بهاتين الحركتين تكتمل 90% من احتياجات التنقل.

#### ثالثًا: النوافذ المنبثقة وعلامات التبويب السفلية — sheet وTabView

إلى جانب «دفع الصفحات» هناك نمطان كلاسيكيان للتفاعل:

::: div .code-block
:::inline div .code-head
<span>SWIFT · نوافذ sheet + تبويبات مع TabView</span><span class="dots">···</span>
:::

```
// 1. لوحة تنبثق من الأسفل، نصف شاشة أو كاملة (المفضلة لنماذج الإدخال)
struct HomeView: View {
    @State private var showAdd = false
    var body: some View {
        Button("تسجيل مصروف") { showAdd = true }
            .sheet(isPresented: $showAdd) {
                AddRecordView()     // شاشة الإدخال المنبثقة
            }
    }
}

// 2. شريط التبويبات السفلي ("الهيكل العظمي" للتطبيق)
struct MainTabView: View {
    var body: some View {
        TabView {
            RecordListView()
                .tabItem { Label("الدفتر", systemImage: "book") }
            StatsView()
                .tabItem { Label("إحصاءات", systemImage: "chart.pie") }
            SettingsView()
                .tabItem { Label("الإعدادات", systemImage: "gear") }
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
نصيحة: متى تستخدم أيّها؟

{class="mt-1"}
قاعدة الخبرة: استخدم NavigationStack لدفع الصفحات في المسار الرئيسي (قائمة → تفاصيل)، وsheet للنوافذ المنبثقة في العمليات المؤقتة (إضافة وتحرير وتأكيد)، وTabView للأقسام الكبيرة المتوازية (علامات التبويب السفلية). وتوليفة الثلاثة معًا هي هيكل أغلب التطبيقات.
:::

#### رابعًا: List — «قائمة الجميع» في iOS

المكون الأكثر استخدامًا والأكثر «نكهة أبل» في iOS هو List — فهو يأتي بطبيعته بفواصل بين الصفوف وحذف بالسحب وإبراز عند النقر:

::: div .code-block
:::inline div .code-head
<span>SWIFT · قوائم مع List + حذف بالسحب</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var records = ["غداء 25.5", "مترو 6.0", "راتب +8000"]

    var body: some View {
        List {
            ForEach(records, id: \.self) { r in
                Text(r)
            }
            .onDelete { indexSet in          // اسحب لليسار للحذف
                records.remove(atOffsets: indexSet)
            }
        }
    }
}
```
:::

قائمة + NavigationLink + sheet + TabView — بجمع هذه الأربعة تصبح قادرًا على بناء هيكل تطبيق كامل: «قائمة دفتر الحسابات → فتح التفاصيل → الضغط على + لإظهار نافذة الإدخال». وهكذا تمامًا بُني مشروع دفتر الحسابات في الفصل التالي.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
هيا نجرّب: ابنِ «هيكلًا من ثلاث صفحات»

#### خامسًا: دورة حياة التطبيق — المقدمة والخلفية

كما لدورة حياة Activity في Android، يمر تطبيق iOS أيضًا بحالات «الولادة والمقدمة والخلفية والموت». في SwiftUI تراقب ذلك عبر قيمة البيئة scenePhase:

::: div .code-block
:::inline div .code-head
<span>SWIFT · مراقبة الانتقال بين المقدمة والخلفية</span><span class="dots">···</span>
:::

```
@main
struct MyApp: App {
    @Environment(\.scenePhase) private var phase

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .onChange(of: phase) { _, newPhase in
            switch newPhase {
            case .active:    print("عودة إلى المقدمة: استئناف التحديث")
            case .inactive:  print("في الانتقال (مكالمة أو لحظة الانتقال إلى الخلفية)")
            case .background: print("إلى الخلفية: حفظ المسودة")
            @unknown default: break
            }
        }
    }
}
```
:::

الاستخدام النموذجي: حدّث البيانات عند العودة إلى المقدمة، واحفظ المسودة عند الانتقال إلى الخلفية. iOS صارم جدًا في تشغيل الخلفية — فالتطبيق العادي يعلق (يُجمّد) سريعًا بعد دخول الخلفية، فلا تتمنى إنجاز أعمال ثقيلة سرًا في الخلفية؛ وإن احتجت مهامًا مجدولة فاستخدم الإشعارات المحلية كما في الفصل 68، لا «الإقامة الدائمة في الخلفية».

{class="mt-1"}
اصنع نسخة ببيانات وهمية من هيكل دفتر الحسابات: TabView بثلاث علامات (الدفتر / الإحصاءات / الإعدادات) → صفحة الدفتر تعرض بيانات وهمية بـ List، والنقر على صف ينقل إلى التفاصيل (NavigationStack) → زر «+» في الزاوية العلوية يفتح نافذة إدخال sheet. بلا تخزين وبلا اتصال بالشبكة، تدريب صرف على الهيكل — وإذا أتقنت هذا الهيكل فملء البيانات الحقيقية فيه في الفصل 65 سيأتي تلقائيًا.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
خلاصة الفصل

- أدوات الحالة الأربع: @State (خاصة بالصفحة) و@Binding (استعارة) و@Observable (منطق) و.environment (عالمي)
- في المشاريع الجديدة اكتب نماذج العرض بماكرو @Observable؛ أما @ObservableObject في الدروس القديمة فيكفي أن تقرأه
- NavigationStack لدفع الصفحات؛ و@Environment(\.dismiss) للعودة برمجيًا
- المسار الرئيسي بدفع الصفحات، والعمليات المؤقتة بنافذة sheet، والأقسام الكبيرة المتوازية بـ TabView
- List هي «قائمة الجميع»: فواصل وحذف بالسحب جاهزة فور فتح العلبة
:::
