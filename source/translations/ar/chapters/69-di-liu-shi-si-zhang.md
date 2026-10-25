---
id: di-liu-shi-si-zhang
num: 64
part: ios-kai-fa-pian
nav: الفصل 64: تخزين البيانات وطلبات الشبكة
toc: default
kind: chapter
---

### الفصل 64: تخزين البيانات وطلبات الشبكة

{class="chapter-intro mb-4"}
التطبيق الذي «يُشاهد» فقط تطبيق ميت؛ أما التطبيق الذي يحفظ البيانات ويتصل بالشبكة فهو حي. في هذا الفصل تتعرف على «الثالوث» في طبقة بيانات iOS: UserDefaults (لتخزين الإعدادات الصغيرة) وSwiftData (لتخزين البيانات المهيكلة) وURLSession (للحوار مع الخادم)، إضافة إلى Codable لتحليل JSON وasync/await الحديثة. وبإتمام هذا الفصل ستكتب تطبيقًا حقيقيًا يتذكر عادات المستخدم ويحدث محتواه لحظيًا.

#### أولًا: كيف تختار حل التخزين — انظر إلى هذا الجدول أولًا

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الحل</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ماذا يصلح لتخزينه</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الخصائص</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">أين يُستخدم في هذا الكتاب</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">إعدادات متفرقة (مفاتيح تبديل وتفضيلات)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">أزواج مفتاح-قيمة، بسيط ومباشر</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">إعدادات الفصل 65 والمدن المفضلة في الفصل 66</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">بيانات مهيكلة (قيود مالية وسجلات)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">غلاف رسمي لقاعدة بيانات، يُصرح به بـ @Model في سطر واحد</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">سجلات المصروفات في الفصل 65</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">(لا يخزن، بل يجلب عبر الشبكة) بيانات الخادم</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">إطار الشبكة المدمج في النظام، دون اعتماد على أطراف ثالثة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">بيانات الطقس في الفصل 66</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
توزيع الأدوار في «الثالوث» المخزني

احفظ هذه القاعدة: «الإعدادات الصغيرة إلى UserDefaults، والبيانات المجمعة إلى SwiftData، وبيانات الخارج عبر URLSession». ما زال Core Data في الدروس القديمة صالحًا للاستخدام (وSwiftData ليس إلا هيئته العصرية)، أما كتابة SQLite يدويًا فلا داعي إليها عمليًا — تعلم الجديد مباشرة ولا تسلك الطريق القديم.

#### ثانيًا: UserDefaults — لتخزين الإعدادات الصغيرة

::: div .code-block
:::inline div .code-head
<span>SWIFT · مثال UserDefaults</span><span class="dots">···</span>
:::

```
// كتابة: تخزين قيمة
UserDefaults.standard.set(true, forKey: "isDarkMode")
UserDefaults.standard.set("الرياض", forKey: "favoriteCity")

// قراءة: استخراجه (إن لم يوجد يعيد القيمة الافتراضية)
let isDark = UserDefaults.standard.bool(forKey: "isDarkMode")
let city = UserDefaults.standard.string(forKey: "favoriteCity") ?? "الرياض"

// حذف: إزالة مفتاح
UserDefaults.standard.removeObject(forKey: "isDarkMode")
```
:::

انتبه: هو مناسب فقط للإعدادات الصغيرة المتفرقة — أما عشرات أو مئات السجلات فاتركها لـ SwiftData، ولا تستخدم UserDefaults قاعدةَ بيانات (فهو يبطئ بدء التشغيل ولا يناسب الاستعلام).

#### ثالثًا: SwiftData — بيت «حقيقي» للبيانات

SwiftData هو حل قواعد البيانات الرسمي منذ iOS 17، وقد بسط «إنشاء الجداول والإضافة والحذف والتعديل والاستعلام» إلى أقصى حد — فبملاحظة @Model واحدة يصير صنف البيانات جدولًا في قاعدة البيانات:

::: div .code-block
:::inline div .code-head
<span>SWIFT · مثال SwiftData</span><span class="dots">···</span>
:::

```
import SwiftData

// 1. ‏@Model: هذا الصنف يصبح تلقائيًا "جدولًا"
@Model
class Record {
    var amount: Double
    var category: String
    var note: String
    var date: Date

    init(amount: Double, category: String, note: String, date: Date) {
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date
    }
}

// 2. ربط الحاوية بنقطة دخول التطبيق
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: Record.self)   // قاعدة البيانات جاهزة
    }
}

// 3. في الواجهة تُقرأ البيانات بـ @Query وتُكتب بـ @Environment
struct RecordListView: View {
    @Query(sort: \Record.date, order: .reverse) var records: [Record]
    @Environment(\.modelContext) private var context

    var body: some View {
        List(records) { r in
            Text("\(r.category) \(r.amount) يوان")
        }
    }

    func add(amount: Double, category: String) {
        let r = Record(amount: amount, category: category, note: "", date: Date())
        context.insert(r)     // حفظ
        try? context.save()   // كتابة على القرص
    }
}
```
:::

يمكن نقل قالب «@Model + modelContainer + @Query» هذا كما هو إلى أي من مشاريعك — يكفي تغيير أسماء الحقول. وبمجرد تغير البيانات يحدّث @Query الواجهة تلقائيًا، وهو ما لا يوصف روعته.

#### رابعًا: Codable — «مترجم» JSON

أغلب بيانات الخوادم نصوص JSON. وبروتوكول Codable في Swift يجعل التحويل بين «JSON ⇄ البنية» يتم تلقائيًا — إذا تطابقت أسماء الحقول اشتغلت السحر:

::: div .code-block
:::inline div .code-head
<span>SWIFT · تحليل JSON مع Codable</span><span class="dots">···</span>
:::

```
// JSON: {"name":"الرياض","main":{"temp":26.5},"weather":[{"description":"صافٍ"}]}
struct WeatherResponse: Codable {
    let name: String
    let main: Main
    let weather: [Weather]
}
struct Main: Codable { let temp: Double }
struct Weather: Codable { let description: String }

// من سلسلة JSON إلى بنية
let decoder = JSONDecoder()
let data = jsonString.data(using: .utf8)!
let result = try decoder.decode(WeatherResponse.self, from: data)
print(result.weather[0].description)   // "صافٍ"
```
:::

قاعدة حديدية: انظر أولًا إلى JSON الحقيقي العائد ثم عرف الحقول. كثير من أخطاء «فشل التحليل» سببها اسم حقل خاطئ أو نوع مخمن خطأ (الخادم يرسل النص "26.5" وأنت تصرح بأنه Double) — اطبع JSON الخام وقارنه، وستحدد المشكلة في عشر ثوانٍ.

#### خامسًا: URLSession مع async/await — الحوار مع الخادم

يتصل iOS بالشبكة عبر URLSession المدمج في النظام، وبتوافقه مع async/await في Swift (الدوال غير المتزامنة) يصير «انتظار الشبكة» طبيعيًا كـ«انتظار شحنة»:

::: div .code-block
:::inline div .code-head
<span>SWIFT · URLSession + async/await</span><span class="dots">···</span>
:::

```
struct WeatherService {
    // دالة غير متزامنة: async تعني "عليّ الانتظار قليلًا"، وthrows تعني "قد تفشل"
    func fetchWeather(city: String) async throws -> WeatherResponse {
        let url = URL(string:
            "https://api.example.com/weather?city=\(city)")!
        let (data, _) = try await URLSession.shared.data(from: url)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}

// موضع الاستدعاء (داخل .task):
.task {
    do {
        let weather = try await service.fetchWeather(city: "الرياض")
        // تحديث الواجهة…
    } catch {
        print("حدث خطأ: \(error)")
    }
}
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
تنبيه لتجنب الفخاخ: قاعدتان حديديتان للشبكة

{class="mt-1"}
① الاتصال بالشبكة يجب أن يكون بـ async/await، ولا تسد الخيط الرئيسي أبدًا — فتجميد الواجهة تجربة سيئة بمستوى الانهيار. يجعل التزامن المهيكل في Swift هذا الأمر طبيعيًا، لكن لا تنسَ try await وdo/catch. ② يمنع ATS افتراضيًا HTTP النصي الصريح: فـ iOS يطلب HTTPS. وعند اختبار خدمة محلية عبر http:// تحتاج إلى استثناء مؤقت في Info.plist (عبر NSAppTransportSecurity)، أما المنتج الرسمي فيجب أن يسلك HTTPS كله — فالمراجعة تطاردها أيضًا.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
هيا نجرّب: اصنع تطبيق «جملة اليوم» الصغير

#### سادسًا: «تصنيف» أخطاء الشبكة أيضًا — لا ترم كل رسائل الخطأ إلى المستخدم

انقطاع الشبكة، وانتهاء المهلة، و404، وخطأ الخادم 500… لكل خطأ مختلف ينبغي أن يرى المستخدم رسالة مختلفة:

::: div .code-block
:::inline div .code-head
<span>SWIFT · معالجة الأخطاء بالتصنيف</span><span class="dots">···</span>
:::

```
func friendlyMessage(_ error: Error) -> String {
    if let urlError = error as? URLError {
        switch urlError.code {
        case .notConnectedToInternet: return "انقطع الاتصال، تتحقق من الشبكة؟"
        case .timedOut:               return "انتهت المهلة، تحاول لاحقًا؟"
        case .cannotFindHost:         return "تعذر العثور على الخادم"
        default:                      return "مشكلة في الشبكة: \(urlError.code)"
        }
    }
    if let d = error as? DecodingError {
        return "تنسيق البيانات غير صحيح (ربما تغيّرت الواجهة)"
    }
    return "حدث خطأ: \(error.localizedDescription)"
}
```
:::

اعرض للمستخدم «لغة بشرية»، واحتفظ بـ«النص الأصلي» للسجلات (اطبع الخطأ error كاملًا). ولا تلقي إلى المستخدم مباشرة رمية error.localizedDescription بالإنجليزية الغامضة — فإحساس الاحترافية يختبئ في هذه التفاصيل.

{class="mt-1"}
ابحث عن واجهة برمجية (API) مجانية للاقتباسات والحكم (مثل hitokoto ونظائرها)، واستخدم URLSession مع async/await لجلب «جملة اليوم» وعرضها في وسط الشاشة، وأضف زر «جملة أخرى». ثم خزن الجمل التي تعجبك في «المفضلة» باستخدام SwiftData. هذا التمرين يستعمل UserDefaults وSwiftData وCodable وURLSession كلها معًا — وبإتمامه يصير الفصلان 7 و8 قطعة من الكعك.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
خلاصة الفصل

- القاعدة: الإعدادات الصغيرة إلى UserDefaults، والبيانات المجمعة إلى SwiftData، وبيانات الخارج عبر URLSession
- خطوات SwiftData الثلاث: @Model للتصريح بالجدول، وmodelContainer لربط الحاوية، و@Query للقراءة + context.insert للكتابة
- Codable يترجم JSON تلقائيًا: إذا تطابقت الحقول اشتغلت السحر
- URLSession مع async/await: الاتصال بالشبكة كانتظار شحنة؛ وdo/catch لمعالجة الفشل
- قاعدتان حديديتان: لا تسد الخيط الرئيسي؛ والمنتج الرسمي يجب أن يستخدم HTTPS (بموجب ATS)
:::
