---
id: di-liu-shi-yi-zhang
num: 61
part: ios-kai-fa-pian
nav: الفصل 61: إتقان Swift بسرعة — اللغة الأولى لتطوير Apple
toc: default
kind: chapter
---

### الفصل 61: انطلاقة سريعة مع Swift — اللغة الأولى لتطوير Apple

{class="chapter-intro mb-4"}
في هذا الفصل نتعلم اللغة رسمياً. لا تتوتر — Swift مشهورة بأنها «ودّية للمبتدئين»، ولا تحتاج إلى حفظ كتاب القواعد: بإتقان 20% من الصياغة ستقرأ وتكتب 80% من الكود اليومي. والباقي تبحث عنه وأنت تعمل على المشروع. تذكّر مبدأ تعلمنا: الفهم أهم من الحفظ، والقدرة على الاستخدام أهم من الإتقان المحض.

#### أولاً: المتغيرات والأنواع — تسمية البيانات

البرنامج هو «بيانات + منطق». والمتغير ببساطة اسم تُخزّن به البيانات. وتُعلن Swift المتغيرات باستخدام let وvar:

::: div .code-block
:::inline div .code-head
<span>SWIFT · المتغيرات</span><span class="dots">···</span>
:::

```
let name = "أحمد"        // let: ثابت (يُفضَّل افتراضيًا)
var age = 18             // var: متغير (يمكن تعديله لاحقًا)

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var يمكن تغييره
// name = "سارة"         // <i class="fas fa-times-circle mr-1"></i> let لا يمكن تغييره، خطأ في الترجمة

let score: Int = 100     // يمكن أيضًا تحديد النوع صراحة
let pi = 3.14            // إن لم تكتبه سيُستنتج تلقائيًا

print("مرحبًا \(name)")   // استيفاء النصوص: شرطة مائلة معكوسة + أقواس
```
:::

الأنواع الشائعة تحفظها من جدول واحد:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">النوع</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ماذا يخزن</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">مثال</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">عدد صحيح</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">عدد عشري</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">نص</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"مرحباً"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bool</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">صواب/خطأ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[Int] (مصفوفة)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مجموعة من البيانات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[1, 2, 3]</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
الأنواع الأساسية الشائعة في Swift

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
نصيحة: مبدأ تقديم let

{class="mt-1"}
قاعدة حديدية في مجتمع Swift: استخدم let افتراضياً، ولا تلجأ إلى var عند الضرورة الحقيقية فقط. إذا استخدمت var حيث يكفي let فسيحذرك Xcode بنص أصفر. هذه العادة تقلل صنفاً كبيراً من أخطاء «تعديل المتغير بالخطأ» — فكلما قلّت التغييرات في الكود سهل الاستدلال عليه.
:::

#### ثانياً: القيم الاختيارية (Optional) — «التميمة ضد الانهيار» في Swift

هذا أهم مفهوم في Swift بلا منازع. بجملة واحدة: عندما تكون القيمة قد «لا توجد»، يجبرك Swift على التعامل مع ذلك — فأباد من مستوى اللغة كابوس الصناعة «انهيار المؤشر الفارغ».

::: div .code-block
:::inline div .code-head
<span>SWIFT · القيم الاختيارية</span><span class="dots">···</span>
:::

```
var name: String = "أحمد"   // نوع عادي: لا يجوز أن يكون nil أبدًا
// name = nil                // <i class="fas fa-times-circle mr-1"></i> خطأ ترجمة: يوقفك فورًا

var nickname: String? = nil  // أضف علامة استفهام: يسمح بـ nil (قيمة اختيارية)
nickname = "تومي"

// مع القيم الاختيارية يجب "فك التغليف":
if let n = nickname {        // if let: فك تغليف آمن
    print("مرحبًا \(n)")
} else {
    print("لا يوجد لقب بعد")
}

let len = nickname?.count ?? 0   // ?? قيمة افتراضية (معامل الدمج الفارغ)
print(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
تنبيه: علامة ! «عملية عالية الخطورة»

{class="mt-1"}
كتابة nickname! (فك إجباري) في الكود تعني الصراخ في وجه المترجم: «أضمن أنه ليس nil» — وإذا أخطأت التخمين انهار التطبيق في الحال. مبدأ مرحلة المبتدئ: استخدم if let / ?? كلما أمكن ولا تستخدم !. وأحياناً يضيف Xcode العلامة ! تلقائياً عند إكمال الكود، فتذكّر إزالتها.
:::

#### ثالثاً: الدوال والإغلاقات — تغليف المنطق في «أزرار»

الدالة منطق ذو اسم، كزر على جهاز التحكم عن بعد. والإغلاق (Closure) هو «دالة بلا اسم» يمكن تسليمها لغيرك في أي لحظة:

::: div .code-block
:::inline div .code-head
<span>SWIFT · الدوال والـ closures</span><span class="dots">···</span>
:::

```
// دالة: الاسم في المقدمة؛ الوسائط ونوع الإرجاع في الخلف
func greet(name: String) -> String {
    return "مرحبًا، \(name)!"
}
print(greet(name: "أحمد"))     // عند الاستدعاء مع اسم الوسيط

// closure: تُعرَّف في المكان، خفيفة ومباشرة
let numbers = [1, 2, 3, 4]
let doubled = numbers.map { $0 * 2 }   // $0 = العنصر الحالي
// [2, 4, 6, 8]

let big = numbers.filter { $0 > 2 }    // تصفية
// [3, 4]
```
:::

الإغلاقات في كل مكان في SwiftUI: الأقواس المعقوفة بعد Button("اضغطني") { ... } هي إغلاق من الطراز الأول. واحفظ جيداً «ضربات المجموعات»: map وfilter وsorted — فـ 90% من معالجة القوائم مستقبلاً توليفة منها.

#### رابعاً: البنى والبروتوكولات — نظام «الليغو» في Swift

تفضيل Swift الرسمي واضح: فضّل البنية (struct) أولًا، ولا تلجأ إلى الصنف (class) إلا عند الحاجة إلى الوراثة. البنية من «نوع القيمة» — فعند النسخ تعيش كل نسخة حياتها المستقلة، وهذا يغنيك بطبيعته عن فئة كاملة من الأخطاء:

::: div .code-block
:::inline div .code-head
<span>SWIFT · الهياكل والبروتوكولات</span><span class="dots">···</span>
:::

```
// الهيكل: صندوق البيانات
struct Record {
    var id = UUID()
    var amount: Double
    var category: String
    var date: Date

    // الهيكل يأتي مع "مُهيئ الأعضاء بالترتيب": يمكن إنشاؤه مباشرة
}
let r = Record(amount: 25.5, category: "طعام", date: Date())

// بروتوكول: اتفاق على "ما القدرات التي يجب توفرها"
protocol Identifiable {
    var id: UUID { get }
}
struct Record: Identifiable { ... }   // اعتماد البروتوكول = الالتزام بتنفيذ متطلباته
```
:::

في SwiftUI كل شيء تقريبًا بنية (struct) — فبروتوكول View نفسه يُنفَّذ كبنية. لا بأس إن لم تفهم هذه الجملة الآن، فستقابلها يوميًا في الفصل 62 — في عالم Swift، احضن struct أولًا.

#### خامسًا: بطاقة مراجعة سريعة لقواعد اللغة للمبتدئين تمامًا

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ماذا تريد أن تفعل</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الصيغة</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تعريف ثابت/متغير</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">let x = 1</code> / <code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">استيفاء السلاسل النصية</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"مرحبًا، \(name)"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تعريف دالة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">func الاسم(المعامل: النوع) -> نوع_الإرجاع { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">التحقق الشرطي</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if الشرط { ... } else { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">المرور على العناصر</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for x in المصفوفة { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">فك الاختيارية بأمان</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if let x = قيمة اختيارية { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">القيمة الافتراضية</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">x ?? القيمة الافتراضية</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تعريف بنية</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X { var a: Int; var b: String }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الإغلاق (Closure)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">{ $0 * 2 }</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
بطاقة مراجعة سريعة لقواعد Swift (نسخة المبتدئين)

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
هيا نجرّب: 15 دقيقة من اللعب بـ Swift في Playgrounds

{class="mt-1"}
إن كان لديك Mac فافتح Xcode → Playground؛ وإن لم يكن فاستخدم Swift Playgrounds على iPad أو ساحة التدريب في المتصفح. شغّل كل مقطع برمجي في هذا الفصل، وغيّر الأرقام والنصوص، وأحدث عمدًا بعض الأخطاء لترى كيف ينبهك Xcode. هذه الدقائق الخمس عشرة من «اللعب قبل التعلم» ستجعل انطلاقتك في الفصل 62 أسهل بمقدار الضعف.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
خلاصة الفصل

- فضّل let على var، واستخدم var بحذر؛ الأنواع تُستنتج تلقائيًا، ويمكن أيضًا التصريح بها صراحةً بعد النقطتين
- القيم الاختيارية هي روح Swift: كل ما قد يكون فارغًا يجب معالجته؛ if let / ?? تمسكك من الأذى، و! عملية عالية الخطورة
- استدعاء الدوال يتضمن أسماء المعاملات؛ والإغلاق دالة بلا اسم، وهو منتشر في كل مكان في SwiftUI
- فضّل struct والتزم بالبروتوكولات (Protocol)؛ في SwiftUI كل شيء تقريبًا بنية
- 20% من القواعد تنجز 80% من العمل: تعلّم الاستخدام أولًا ثم أتقِن
:::
