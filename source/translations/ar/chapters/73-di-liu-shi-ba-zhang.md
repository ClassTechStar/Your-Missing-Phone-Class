---
id: di-liu-shi-ba-zhang
num: 68
part: ios-kai-fa-pian
nav: الفصل 68: طريق الترقي — الأذونات والإشعارات والبنية الحديثة
toc: default
kind: chapter
---

### الفصل 68: طريق التقدم — الأذونات والإشعارات والمعماريات الحديثة

{class="chapter-intro mb-4"}
صناعة التطبيق بداية فقط. نتحدث في هذا الفصل عن الحواجز بين «أن تعرف كيف تصنع» و«أن تصنع جيدًا»: كيف تطلب الأذونات بلطف، وكيف ترسل إشعارات لا تثير السخط، وكيف ترفع المعمارية درجة أخرى، وكيف — في عام 2026 — تشرك الذكاء الاصطناعي في كتابة كود iOS. وكل بند منها ستصادفه قريبًا في مشاريع حقيقية.

#### أولًا: الأذونات — اطرق الباب أولًا ثم ادخل

الكاميرا والموقع وجهات الاتصال والإشعارات… هذه «المناطق الحساسة» يطلب iOS فيها من التطبيق أن يستأذن المستخدم بنافذة منبثقة عند الحاجة إليها. والقاعدة ثلاث خطوات: «التصريح + الطلب + التدهور الرشيق»:

::: div .code-block
:::inline div .code-head
<span>SWIFT · طلب الأذونات (مثال: الموقع)</span><span class="dots">···</span>
:::

```
// 1. صرّح في Info.plist بنص الغرض (بدون تصريح سينهار التطبيق فورًا!)
// Privacy - Location When In Use Usage Description: "يُستخدم للاستعلام عن طقس مدينتك"

// 2. طلبه عند الاستخدام
import CoreLocation

@Observable
class LocationModel {
    private let manager = CLLocationManager()

    func request() {
        switch manager.authorizationStatus {
        case .notDetermined: manager.requestWhenInUseAuthorization()
        case .denied, .restricted: /* التوجيه إلى الإعدادات لتفعيله */
        default: /* الإذن ممنوح، انطلق */
        }
    }
}

// 3. تدهور رشيق بعد الرفض: عرض تنبيه والانتقال إلى الإعدادات
// UIApplication.shared.open(URL(string: UIApplication.openSettingsURLString)!)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
تنبيه: أذونات iOS «تطلب مرة واحدة»

{class="mt-1"}
نافذة إذن iOS تظهر مرة واحدة فقط — فبعد رفض المستخدم لن تظهر أبدًا. لذلك: اختر لحظة الطلب عند «اللحظة التي يحتاج فيها المستخدم الميزة فعلًا» (لا عند الإقلاع مباشرة بمجموعة نوافذ)، وليكن النص يوضح الغرض. وتوجيه الواجهة بعد الرفض («افتح الموقع من الإعدادات») أمر أساسي، فلا تحبس المستخدم في طريق مسدود.
:::

#### ثانيًا: الإشعارات — قل كلامًا نافعًا في الوقت الصحيح

الإشعارات قناة وصول التطبيق إلى المستخدم، وهي أيضًا أكثر الوظائف عرضة لأن يضعها المستخدم في «القائمة السوداء». يستخدم iOS إطار UserNotifications، ولإرسال الإشعارات ثلاث قواعد: أرسل المفيد فقط، واسمح للمستخدم بإيقافها، ولا تزعج أحدًا في منتصف الليل. والاستخدام الأساسي:

::: div .code-block
:::inline div .code-head
<span>SWIFT · إشعارات محلية</span><span class="dots">···</span>
:::

```
import UserNotifications

// 1. طلب إذن الإشعارات (نافذة منبثقة مرة واحدة)
UNUserNotificationCenter.current()
    .requestAuthorization(options: [.alert, .sound, .badge]) { granted, _ in
        print(granted ? "ممنوح" : "مرفوض")
    }

// 2. جدولة "تذكير يومي الساعة 20:00 لتسجيل المصروفات"
func scheduleDailyReminder() {
    let content = UNMutableNotificationContent()
    content.title = "تذكير بتسجيل المصروفات"
    content.body = "لم تسجل أي مصروفات اليوم بعد"
    content.sound = .default

    var comps = DateComponents()
    comps.hour = 20
    let trigger = UNCalendarNotificationTrigger(dateMatching: comps, repeats: true)

    let request = UNNotificationRequest(
        identifier: "daily-reminder",
        content: content,
        trigger: trigger
    )
    UNUserNotificationCenter.current().add(request)
}
```
:::

انتبه: إذن الإشعارات في iOS كذلك «يطلب مرة واحدة»، ويمكن للمستخدم إيقافه في أي وقت من إعدادات النظام — لذا فالإحساس بقيمة محتوى الإشعار مهم جدًا؛ فإرسال عشوائي واحد قد يفقدك المستخدم إلى الأبد.

#### ثالثًا: ترقية المعمارية — تعميق MVVM وقابلية الاختبار

استخدمنا MVVM في الفصل 65، ونضيف هنا ثلاث نقاط متقدمة:

- التجريد بالبروتوكول: اجعل ViewModel يعتمد على بروتوكول (protocol) لا على صنف محدد — فتستطيع في الاختبار حقن «مصدر بيانات وهمي»، وهذا حجر الأساس في قابلية الاختبار؛
- المسؤولية الواحدة: ViewModel واحد يتكفل بمهمة واحدة (المسؤول عن الحسابات لا يتولى الطقس)؛ وإذا كثرت الوظائف ففككه؛
- لا تبالغ في التصميم: في مشروع صغير لشخص واحد يكفي «صنف @Observable مع تجريد بالبروتوكول». أما المعماريات الثقيلة مثل VIPER وClean Architecture فانتظر حتى يطرق بابك فريق عمل وتعقيد حقيقي — فالأدوات تخدم الأهداف، ولا تلبس للتفاخر.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
نصيحة: «مكافآت البيئة» في SwiftUI

{class="mt-1"}
في بيئة iOS أيضًا أسلوبان متقدمان «لا بديل عنهما»: الأدوات المصغرة (WidgetKit) تتيح للمستخدم رؤية المعلومات دون فتح التطبيق (كوضع «مصروفات هذا الشهر» من الدفتر على سطح المكتب)، والأوامر السريعة (App Intents) تتيح للمستخدم استدعاء وظائفك عبر Siri أو الأتمتة. وكلاهما له إطار رسمي وتكلفة تعلم ليست عالية، لكنهما يرفعان تجربة المستخدم ارتفاعًا هائلًا — فالأولوية على طريق التقدم أن تفتحهما أولًا.
:::

#### رابعًا: أسلوب 2026 الجديد — تطوير iOS بمساعدة الذكاء الاصطناعي

في عام 2026 صار الذكاء الاصطناعي مدمجًا بعمق في دورة تطوير Apple. وإن أردت التسريع فهذه التوليفة ناضجة جدًا:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">المرحلة</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">كيف يساعد الذكاء الاصطناعي</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">مسؤوليتك</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">كتابة الكود</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">إكمال الكود المدمج في Xcode + توليد عبر إضافات ذكاء اصطناعي من طرف ثالث</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">وصف المتطلبات بوضوح ومراجعة الناتج</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">البحث عن المعلومات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">إعطاء الوثائق الرسمية ورسائل الخطأ إلى الذكاء الاصطناعي ليشرحها</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">التحقق من النتائج المهمة بالعودة إلى الوثائق الرسمية</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">كتابة الاختبارات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">اطلب من الذكاء الاصطناعي توليد حالات XCTest بثلاث فئات: «عادي / حدّي / استثنائي»</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">التأكد من أن الحالات تنسجم مع دلالات مجال العمل</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">إصلاح الأخطاء</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">لصق سجل الانهيار مع الكود ذي الصلة، والذكاء الاصطناعي يحدد الموضع ويصلح</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">فهم التعديلات وتشغيل الاختبارات للتحقق</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
المشاهد الأربعة لتطوير iOS بمساعدة الذكاء الاصطناعي

أما المنهجية التفصيلية — كيف توجه الذكاء الاصطناعي بالتعليمات، وكيف تقبل العمل، وكيف تتجنب الفخاخ — فهناك 11 فصلًا كاملة عنها في الجزء السابع من هذا الكتاب «البرمجة العملية بالذكاء الاصطناعي» (الفصول 37-47)، وننصح بشدة بقراءتها معًا: اترك قواعد Swift لهذا الجزء، وأسرار التعاون مع الذكاء الاصطناعي للجزء السابع.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
هيا نجرّب: أضف «الثالوث» إلى دفتر الحسابات

#### خامسًا: أساسيات التزامن في Swift — @MainActor وTask

في منظومة التزامن في Swift 6 قاعدتان يجب على كل مبتدئ فهمهما:

- الواجهة لا تُحدَّث إلا على الخيط الرئيسي: عروض SwiftUI من نوع @MainActor افتراضيًا، فعند عودة نتيجة الشبكة ارجع إلى الخيط الرئيسي ثم غيّر الحالة (عبر await MainActor.run { ... } أو بوسم ViewModel بـ @MainActor)؛
- المهام غير المتزامنة تديرها Task: المُعدِّل .task { } يبدأ تلقائيًا مع ظهور العرض ويُلغى تلقائيًا عند اختفائه — وهذه هي الطريقة المعيارية لبدء عمل غير متزامن في SwiftUI، فلا تكتب Task عشوائيًا داخل body مباشرة.

::: div .code-block
:::inline div .code-head
<span>SWIFT · الأسلوب القياسي للعمل غير المتزامن</span><span class="dots">···</span>
:::

```
struct WeatherScreen: View {
    @State private var vm = WeatherViewModel()

    var body: some View {
        Group {
            switch vm.state {
            case .loading: ProgressView()
            case .success(let d): WeatherContent(data: d)
            case .error(let m): Text(m)
            }
        }
        .task {                       // يبدأ عند الظهور ويُلغى عند الاختفاء
            await vm.search(city: "الرياض")
        }
    }
}
```
:::

خلف هاتين القاعدتين تصميم «أمان سباقات البيانات» في Swift 6 — فالمترجم يخبرك بالخطأ عند كتابته مباشرة، بدلاً من اكتشافه بعد انهيار التطبيق. وخطأ المترجم ليس تنمرًا، بل هو يتقاضى عنك الرصاصات.

{class="mt-1"}
① أضف إلى الدفتر «تذكيرًا يوميًا الساعة 20:00 لتسجيل الحساب» (إذن الإشعارات + إشعار محلي)؛ ② حوّل مصدر بيانات ViewModel إلى تجريد بالبروتوكول، واكتب اختبار وحدات يحقن بيانات وهمية؛ ③ أضف أداة مصغرة على سطح المكتب لـ«مصروفات هذا الشهر». وبإتمام الثلاثة يكتسب مشروعك هيئة «الجيش النظامي».
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
خلاصة الفصل

- الأذونات في ثلاث خطوات: التصريح في Info.plist (فإذا أُهمل انهار التطبيق)، والطلب عند الاستخدام، وتوجيه المستخدم إلى الإعدادات عند الرفض
- نافذة إذن iOS تظهر مرة واحدة: اختر لحظة «الاستخدام الفعلي»، وليكن النص واضح الغرض
- قواعد الإشعارات الثلاث: المفيد فقط، ويمكن إيقافها، ولا إزعاج؛ عبر إطار UserNotifications
- ترقية MVVM: تجريد بالبروتوكول (قابل للاختبار)، ومسؤولية واحدة، وبلا مبالغة في التصميم
- مكافآت البيئة: أدوات مصغرة بـ WidgetKit + أوامر سريعة بـ App Intents
- أربعة مشاهد لمساعدة الذكاء الاصطناعي: كتابة الكود، والبحث عن المعلومات، وكتابة الاختبارات، وإصلاح الأخطاء؛ والمنهجية في الجزء السابع (الفصول 37-47)
:::
