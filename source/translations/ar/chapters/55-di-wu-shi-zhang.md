---
id: di-wu-shi-zhang
num: 50
part: an-zhuo-kai-fa-pian
nav: الفصل 50: إتقان Kotlin بسرعة — اللغة الأولى لتطوير Android
toc: default
kind: chapter
---

### الفصل 50: انطلاقة سريعة مع Kotlin — اللغة الأولى لتطوير Android

{class="chapter-intro mb-4"}
في هذا الفصل نبدأ رسميًا تعلم اللغة. لا تتوتر — Kotlin معروفة بأنها "ودودة مع المبتدئين"، ولا تحتاج إلى حفظ كتاب قواعد: بإتقان 20% من القواعد تستطيع فهم وكتابة 80% من الكود اليومي، والباقي تتعلمه أثناء العمل على المشاريع. تذكّر مبدأنا في التعلم: الفهم أهم من الحفظ، والاستخدام أهم من الإتقان.

#### أولًا: المتغيرات والأنواع: إعطاء البيانات أسماء

البرنامج هو "بيانات + منطق". والمتغير اسم نطلقه على البيانات لنخزنها. في Kotlin طريقتان للتصريح:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · المتغيرات</span><span class="dots">···</span>
:::

```
val name = "أحمد"        // val: متغير للقراءة فقط (يُفضَّل افتراضيًا)
var age = 18             // var: متغير قابل للتغيير (يمكن تعديله لاحقًا)

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var يمكن تغييره
// name = "سارة"         // <i class="fas fa-times-circle mr-1"></i> val لا يمكن تغييره، الترجمة ستُظهر خطأ

val score: Int = 100     // يمكن أيضًا تحديد النوع صراحة
val pi = 3.14            // إن لم تكتبه سيُستنتج تلقائيًا
```
:::

الأنواع الشائعة قليلة، وجدول واحد يكفي لحفظها:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">النوع</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ماذا يخزن</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">مثال</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">عدد صحيح</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">عدد عشري</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">نص</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"مرحبًا"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Boolean</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">صح/خطأ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List&lt; T&gt;</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مجموعة بيانات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">listOf(1, 2, 3)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
الأنواع الأساسية الشائعة في Kotlin

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
نصيحة: قاعدة أولوية val

{class="mt-1"}
قاعدة حديدية في مجتمع Kotlin: استخدم val افتراضيًا، ولا تلجأ إلى var إلا عند الضرورة القصوى. إذا استخدمت var حيث يكفي val سيحذرك المحرر بخط أصفر. هذه العادة توفر عليك فئة كبيرة من الأخطاء الناتجة عن "تعديل المتغيرات دون قصد" — فكلما قلّ التغيير في الكود سهُل فهمه.
:::

#### ثانيًا: الدوال: تجميع المنطق في "أزرار"

الدالة منطق له اسم، تشبه زرًا على جهاز التحكم — تضغطه (تستدعيه) فتنفَّذ سلسلة من الأوامر. في Kotlin نصرّح عنها بالكلمة fun:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · الدوال</span><span class="dots">···</span>
:::

```
fun greet(name: String): String {
    return "مرحبًا، $name!"     // رمز $ يُدرج المتغير داخل النص
}

println(greet("أحمد"))        // الناتج: مرحبًا أحمد!

// الدوال ذات السطر الواحد يمكن كتابتها كتعبير
fun add(a: Int, b: Int) = a + b

println(add(3, 5))            // الناتج: 8
```
:::

نقاط مهمة: تُكتب المعاملات داخل الأقواس (الاسم أولًا ثم النوع، يفصلهما نقطتان رأسيتان)، ويُكتب نوع الإرجاع بعد الأقواس؛ وقالب النص $اسم_المتغير هو ميزة Kotlin المميزة — لم تعد تحتاج إلى "لصق" السلاسل مع المتغيرات كما في Java.

#### ثالثًا: الشروط والحلقات: نجعل البرنامج "يفكر"

ذكاء البرنامج يأتي من أمرين: القدرة على الحكم (if/when) والقدرة على التكرار (for/while).

::: div .code-block
:::inline div .code-head
<span>KOTLIN · الشروط والحلقات</span><span class="dots">···</span>
:::

```
// شرط: if / else
val age = 17
if (age >= 18) {
    println("بالغ")
} else {
    println("قاصر")
}

// فروع متعددة: when (أفضل من switch بمئة مرة)
val score = 85
val level = when {
    score >= 90 -> "ممتاز"
    score >= 60 -> "ناجح"
    else -> "واصل المحاولة!"
}

// تكرار: حلقة for
val fruits = listOf("تفاح", "موز", "برتقال")
for (fruit in fruits) {
    println("أحب أكل $fruit")
}
```
:::

التعبير when هو أسلوب التفرع المتعدد الأكثر استخدامًا في Kotlin، وستستخدمه يوميًا في تطوير Android (مثل عرض واجهات مختلفة حسب الحالة).

#### رابعًا: أمان الفراغ: "تميمة الحماية" في Kotlin

أشهر خطأ في عصر Java اسمه NullPointerException (استثناء المؤشر الفارغ) — ينهار البرنامج عندما يصل إلى شيء "لا يحتوي شيئًا". وتقول الإحصائيات إنه يتصدر قائمة أعطال Android باستمرار. حلت Kotlin هذه المشكلة من مستوى اللغة نفسه: القيم الفارغة ممنوعة افتراضيًا.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · الأمان من القيم الفارغة</span><span class="dots">···</span>
:::

```
var name: String = "أحمد"   // نوع عادي: لا يجوز أن يكون null أبدًا
// name = null                // <i class="fas fa-times-circle mr-1"></i> خطأ ترجمة: يوقفك فورًا

var nickname: String? = null // أضف علامة استفهام: يسمح بـ null
nickname = "تومي"

// مع الأنواع القابلة لـ null يجب التعامل بأمان:
println(nickname?.length)    // استدعاء آمن: إذا كانت null يرجع null دون انهيار
val len = nickname?.length ?: 0   // معامل Elvis: قيمة افتراضية عند null
println(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
تنبيه: لا تخلط بين ? و ?:

{class="mt-1"}
النوع String? يعني "مسموح أن يكون فارغًا"، أما a ?: b فتعني "إذا كان a فارغًا استخدم b" (تشبه تسريحة شعر إلفيس بريسلي لذلك تسمى معامل Elvis). في بداياتك، إذا ظهر لك خطأ متعلق بـ null فالأرجح أنك نسيت معالجة نوع قابل للفراغ — وهذا هو اللغة تحميك.
:::

#### خامسًا: الأصناف والكائنات: قوالب صناعة "القطع"

الصنف (class) هو "قالب" الكائن، والكائن "المنتج النهائي" من الصنف. كل شيء في Android — الصفحات والأزرار والبيانات — كائن. وفي Kotlin أداة رائعة اسمها data class (صنف البيانات) مخصصة "لحمل البيانات"؛ سطر واحد يعادل عشرات الأسطر في Java:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · الأصناف وأصناف البيانات</span><span class="dots">···</span>
:::

```
// صنف عادي: القالب
class Dog(val name: String) {
    fun bark() = println("$name: هو هو!")
}

val dog = Dog("Rex")      // ينشئ الكائن
dog.bark()                 // Rex: هو هو!

// data class: صندوق البيانات (يشمل equals/copy وغيرها تلقائيًا)
data class User(val id: Int, val name: String, val email: String)

val me = User(1, "أحمد", "zhangsan@example.com")
val twin = me.copy(name = "خالد")   // ينسخ ويغيّر حقلًا واحدًا
```
:::

عندما تصنع لاحقًا دفتر حسابات، ستكون كل عملية مالية data class مثل: data class Record(val amount: Double, val category: String, val date: String). أرأيت؟ صرت قادرًا على كتابة بنية كود مشروع حقيقي.

#### سادسًا: اللامدا والدوال العليا: "سكر Kotlin النحوي"

ستشاهد يوميًا في كود Android تعابير مثل { ... } وهي "دوال بلا اسم" تسمى lambda (دالة مجهولة). السطر onClick = { count++ } في الزر هو lambda — يجمع "ماذا نفعل بعد النقر" في كتلة واحدة ويسلّمها للزر.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · أول تجربة مع lambda</span><span class="dots">···</span>
:::

```
// الطريقة العادية: تعرّف دالة مسماة ثم تمررها
fun double(x: Int) = x * 2
val result = listOf(1, 2, 3).map(::double)

// طريقة lambda: تُعرَّف في المكان، خفيفة ومباشرة
val result2 = listOf(1, 2, 3).map { it * 2 }   // it = العنصر الحالي

// تصفية + تحويل متسلسل (شائع جدًا في المشاريع الحقيقية)
val bills = listOf(12.5, 88.0, 5.0, 200.0)
val bigBills = bills.filter { it > 50 }.sorted()
// [88.0, 200.0]——"الفواتير فوق 50 بعد الترتيب"
```
:::

احفظ "المجموعات" عالية التكرار: filter (التصفية) و map (التحويل) و sorted (الترتيب) و sum (الجمع). في المستقبل ستعالج 90% من قوائمك بتركيبات هذه الحيل الأربع. فلسفة Kotlin: ما يمكن قوله بجملة واحدة لا يُكتب بخمس.

#### سابعًا: بطاقة مراجعة نحوية للمبتدئين من الصفر

لا تحاول حفظ كل القواعد في يوم واحد. احفظ هذه البطاقة وراجعها أثناء كتابة الكود، وبعد أسبوعين ستألفها تلقائيًا:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ماذا تريد أن تفعل</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الطريقة</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تعريف متغير للقراءة فقط</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">val x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تعريف متغير قابل للتغيير</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تعريف دالة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">fun الاسم(المعاملات): نوع الإرجاع { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">اتخاذ قرار</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if (الشرط) {...} else {...}</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تفرع متعدد</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">when { الشرط -> النتيجة }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">المرور على العناصر</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for (x in القائمة) { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">دمج النصوص</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"مرحبًا، $name"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">معالجة الفراغ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">x?.length ?: 0</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تعريف صنف بيانات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">data class X(val a: Int, val b: String)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
بطاقة مراجعة نحو Kotlin (نسخة المبتدئين)

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
لنتجرب: جرّب Kotlin 10 دقائق دون تثبيت أي برنامج

{class="mt-1"}
افتح play.kotlinlang.org (ساحة التجارب الرسمية لـ Kotlin) في المتصفح، والصق كل مقطع كود في هذا الفصل وشغّله، وعدّل الأرقام والنصوص وراقب كيف يتغير الناتج. هذه الـ 10 دقائق من "اللعب قبل التعلم" ستسهّل عليك البدء في الفصل 51 إلى ضعفين.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
خلاصة الفصل

- أولوية val واحذر مع var؛ يمكن استنتاج الأنواع تلقائيًا، أو التصريح بها صراحة بعد النقطتين
- الدالة = منطق مجمّع؛ وقالب النص $ هو الميزة المميزة
- if/when للحكم و for للتكرار؛ و when هو "متعدد المواهب" في تطوير Android
- أمان الفراغ هو تميمة الحماية في Kotlin: الأنواع العادية ترفض null، والأنواع القابلة للفراغ تتطلب معالجة بـ ? أو ?:
- data class صندوق لحمل البيانات، حقل لكل سطر، وتستخدم يوميًا في المشاريع الحقيقية
- 20% من القواعد تُنجز 80% من العمل: استخدم أولًا ثم أتقن
:::
