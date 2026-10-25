---
id: di-wu-shi-yi-zhang
num: 51
part: an-zhuo-kai-fa-pian
nav: الفصل 51: تطوير الواجهات — مدخل إلى Jetpack Compose
toc: default
kind: chapter
---

### الفصل 51: تطوير الواجهات — مدخل إلى Jetpack Compose

{class="chapter-intro mb-4"}
الواجهة هي كل ما يراه المستخدم. قبل ظهور Compose كانت واجهات Android تُكتب بـ XML — كأنها ملء الفراغات، أمر شاق؛ وفي 2021 أطلقت جوجل Jetpack Compose: "رسم" الواجهة مباشرة بكود Kotlin، بحيث ترى النتيجة فورًا وتتحدث المعاينة لحظة تعديل سطر واحد. بحلول 2026 أصبح Compose هو الخيار السائد بلا منازع للمشاريع الجديدة. في هذا الفصل سنتعلم "الرسم".

#### أولًا: فكرة Compose: الواجهة دالة

فكرة Compose الجوهرية في جملة واحدة: الواجهة = دالة. كل ما يمكن عرضه على الشاشة (نص، زر، صورة) هو "دالة قابلة للتركيب" (Composable) مميزة بـ @Composable. وعند تداخلها كقطع مكعبات تتكون الواجهة.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · أول واجهة Compose</span><span class="dots">···</span>
:::

```
@Composable
fun Greeting(name: String) {
    Text(text = "مرحبًا، $name!")     // "قطعة نص"
}

// تركيب متداخل: قطع كبيرة تحتوي قطعًا صغيرة
@Composable
fun HomeScreen() {
    Column {                          // مرتبة رأسيًا
        Greeting(name = "أحمد")
        Greeting(name = "سارة")
        Button(onClick = { /* ماذا يحدث عند الضغط */ }) {
            Text("اضغط هنا")
        }
    }
}
```
:::

انتبه إلى "القبعة" @Composable — إنها تخبر المترجم "هذه قطعة من مكعبات الواجهة". يمكن تداخل القطع إلى ما لا نهاية، وهذا كل سر Compose.

#### ثانيًا: المكونات الأساسية: نص، زر، حقل إدخال، صورة

مكونات Compose هي "قطع المكعبات"، وأكثرها شيوعًا أربعة:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">المكون</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ماذا يفعل</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">المعاملات الأساسية</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">عرض نص</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">text (النص المراد عرضه)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">زر</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onClick (دالة الاستجابة للنقر)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">حقل إدخال</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">value و onValueChange (دالة الاستجابة لتغير الإدخال)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">عرض صورة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">painter (مورد الصورة)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
المكونات الأساسية الأربعة في Compose

::: div .code-block
:::inline div .code-head
<span>KOTLIN · مثال على المكونات الأساسية</span><span class="dots">···</span>
:::

```
@Composable
fun BasicWidgets() {
    Column {
        Text(text = "هذا نص")
        Button(onClick = { println("تم الضغط!") }) {
            Text("زر")
        }
        var input by remember { mutableStateOf("") }
        TextField(
            value = input,
            onValueChange = { input = it },
            label = { Text("اكتب شيئًا") }
        )
    }
}
```
:::

في سطري حقل الإدخال ظهرت العبارة remember { mutableStateOf("") } — وهذه هي "سحر الحالة" في Compose وسنفصله في القسم الخامس من هذا الفصل. اكتفِ الآن بالتعرف على شكلها.

#### ثالثًا: ثلاثية التخطيط: Column و Row و Box

الآن لدينا المكونات؛ كيف نرتبها؟ احفظ ثلاثة "صناديق":

- Column: ترتيب رأسي (مثل الوقوف في طابور)؛
- Row: ترتيب أفقي (مثل الجلوس جنبًا إلى جنب)؛
- Box: التراكب (مثل كومة أوراق اللعب، مناسب للشارات والطبقات).

::: div .code-block
:::inline div .code-head
<span>KOTLIN · ثلاثية التخطيط</span><span class="dots">···</span>
:::

```
Column {
    Text("السطر الأول")
    Row {
        Text("يسار")
        Text("يمين")
    }
    Box {
        Text("الطبقة السفلية")
        Text("شارة علوية متراكبة")
    }
}
```
:::

تريد تخطيطًا أجمل؟ أضف إلى المكونات Modifier (المُزخرف) — فهو بمثابة "مكياج" للمكعبات:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Modifier: حيل شائعة</span><span class="dots">···</span>
:::

```
Text(
    text = "نص جميل",
    modifier = Modifier
        .padding(16.dp)          // هامش من كل الجهات
        .fillMaxWidth()          // يملأ العرض كاملًا
        .background(Color.Blue)  // لون الخلفية
        .clickable { /* عند الضغط */ }// قابل للنقر
)
// استدعاءات متسلسلة: واحدًا بعد الآخر، والترتيب مهم (padding أولًا ثم الخلفية؛ الخلفية لا تشمل الهامش)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
تنبيه: ترتيب Modifier له شأن

{class="mt-1"}
padding(16.dp).background(Blue) و background(Blue).padding(16.dp) تعطيان نتيجتين مختلفتين — الأولى "فراغ ثم تلوين" (الخلفية لا تشمل الهامش)، والثانية "تلوين ثم فراغ" (الخلفية تشمل الهامش). هذا أكثر موضع يخطئ فيه المبتدئ فيرسم "حواف بيضاء غريبة". عند الشك بدّل الترتيب وستخبرك المعاينة بالجواب فورًا.
:::

#### رابعًا: الحالة: نجعل الواجهة "حية"

الواجهة الثابتة مملة. لجعل الرقم يزيد +1 عند نقر الزر أو حقل الإدخال يقبل الكتابة، نحتاج إلى الحالة (State). قاعدة Compose: الواجهة تعكس الحالة بأمانة دائمًا، ومتى تغيرت الحالة أُعيد رسم الواجهة تلقائيًا.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · الحالة: عداد نقرات</span><span class="dots">···</span>
:::

```
@Composable
fun Counter() {
    // ‏remember + mutableStateOf: يتذكر هذه القيمة المتغيرة
    var count by remember { mutableStateOf(0) }

    Column {
        Text(text = "ضغطت $count مرات")
        Button(onClick = { count++ }) {   // يغيّر الحالة
            Text("اضغط +1")                // تتحدث الواجهة تلقائيًا
        }
    }
}
```
:::

ثلاثة أسطر تكفي لعمل عدّاد حي. وهذه هي متعة Compose مقارنة بالأسلوب القديم: لا حاجة إلى "تحديث الواجهة" يدويًا؛ يكفي تغيير البيانات. احفظ دالتين رئيسيتين: remember (تحفظ القيمة من المسح عند إعادة تركيب الواجهة) و mutableStateOf (تخبر Compose "إذا تغيرت هذه القيمة أعيد الرسم").

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> المستخدم يضغط</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> الحالة تتغير (count++)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> Compose يلاحظ التغير</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> يعيد رسم الواجهة (إعادة تركيب)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
الشكل 3: تدفق البيانات أحادي الاتجاه "الحالة ← الواجهة" في Compose
:::

#### خامسًا: المظهر والوضع الداكن: إعداد واحد يسري على الكل

ما تراه في قالب المشروع MyFirstAppTheme { ... } هو المظهر (Theme). وهو مبني على مواصفات التصميم Material 3، ويساعدك على إدارة الألوان والخطوط والأشكال بشكل موحد. دعم الوضع الداكن يحتاج ثلاث خطوات فقط:

1. عرّف في المظهر مجموعتي ألوان: فاتحة وداكنة (القالب يولّد ColorScheme تلقائيًا)؛
2. عندما ينتقل النظام إلى الوضع الداكن تكتشف الدالة isSystemInDarkTheme() ذلك تلقائيًا؛
3. استخدم ألوان المظهر المعرّفة (مثل MaterialTheme.colorScheme.primary) بدلًا من تثبيت قيم الألوان يدويًا.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
نصيحة: الألوان الديناميكية في Material 3

{class="mt-1"}
ميزة "Material You" ابتداءً من Android 12 تتيح للتطبيق استخراج الألوان من خلفية جهازك. قوالب Compose تدعمها افتراضيًا (dynamicColor). سيتغير "لباس" تطبيقك تلقائيًا على هواتف المستخدمين المختلفة — هذه هي رومانسية Android الحديثة.
:::

#### سادسًا: المعاينة والحركة والتحرير الحي: "القوى الخارقة" في Compose

ثلاث "قوى خارقة" في تجربة تطوير Compose؛ متى تستخدمها لن تعود إلى الوراء:

- معاينة @Preview: أضف التعليق @Preview إلى الدالة القابلة للتركيب فتعرض Android Studio الواجهة فورًا على الجانب — تعديل مباشر يريك النتيجة دون تثبيت على الهاتف في كل مرة؛
- التحرير الحي (Live Edit): يدعم Android Studio في 2026 "التحديث الساخن" لبعض التعديلات على المحاكي/الجهاز الحقيقي؛ تعديلات صغيرة مثل تغيير لون النص تظهر على الجهاز في ثوانٍ؛
- واجهات الحركة (Animation API): بضعة أسطر مثل animateFloatAsState و AnimatedVisibility تكفي لحركة سلسة للعناصر — "الإحساس الاحترافي" غالبًا يكمن في هذه العشرات من الأسطر.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · رسوم متحركة في عشر دقائق</span><span class="dots">···</span>
:::

```
@Composable
fun AnimatedBox() {
    var big by remember { mutableStateOf(false) }
    // عند تغير القيمة ينتقل بسلاسة إلى القيمة الهدف
    val size by animateDpAsState(if (big) 120.dp else 60.dp)

    Box(Modifier
        .size(size)
        .background(MaterialTheme.colorScheme.primary)
        .clickable { big = !big }
    )
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
نصيحة: الوظيفة أولًا ثم الحركة

{class="mt-1"}
خطأ المبتدئين الشائع: "الواجهة لم تُصح بعد ومع ذلك يبدؤون بالانشغال بالحركات". اجعل الوظيفة تعمل أولًا ثم أضف الحركات دفعة واحدة في النهاية — وهذا أيضًا مبدأ "البساطة أولًا": الحركة زينة تُضاف، والوظيفة حاجة أساسية لا غنى عنها.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
لنتجرب: اصنع "زر المزاج"

{class="mt-1"}
حوّل مشروع القالب إلى مبدّل مزاج: زر واحد، عند نقره يتنقل بين 😀 سعيد ← 😢 حزين ← 😡 غاضب، مع تغير النص ولون الخلفية تبعًا لذلك. تلميح: استخدم when لاختيار النص واللون حسب الحالة. عند الانتهاء أرسله لأصدقائك لتجربوه وستحصد أول موجة "واو، صرت تصنع تطبيقات!".
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
خلاصة الفصل

- فكرة Compose: الواجهة = دوال @Composable متداخلة كقطع مكعبات
- المكونات الأربعة: Text / Button / TextField / Image
- ثلاثية التخطيط: Column رأسي، Row أفقي، Box متراكب
- سلسلة Modifier لل"تزيين": padding و fillMaxWidth و background و clickable — والترتيب له معنى
- الحالة هي الروح: remember + mutableStateOf؛ غيّر البيانات فتُعاد رسم الواجهة تلقائيًا
- المظهر عبر Material 3 مع الألوان الديناميكية؛ إعداد واحد للوضع الداكن يسري على الكل
:::
