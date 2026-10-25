---
id: di-wu-shi-wu-zhang
num: 55
part: an-zhuo-kai-fa-pian
nav: الفصل 55: المشروع الثاني — تطبيق الاستعلام عن الطقس (نسخة شبكية)
toc: default
kind: chapter
---

### الفصل 55: المشروع الثاني — تطبيق الطقس (النسخة الشبكية)

{class="chapter-intro mb-4"}
دفتر الحسابات "تمرين داخلي"، أما تطبيق الطقس فـ"انطلاق إلى العالم" — فهو يتعامل مع الإنترنت. في هذا المشروع ستتعلم: طلب API مجاني، وتحليل JSON، ومعالجة حالات الواجهة الثلاث "جارٍ التحميل/نجاح/فشل"، وكيفية إخفاء مفتاح API جيدًا. بعد إنجازه ستكتسب القدرة على بناء أي "تطبيق متصل بالشبكة" — أخبار، أسعار صرف، ترجمة؛ والطريقة واحدة تمامًا.

#### أولًا: طلب API طقس مجاني

لتمرين شخصي أنصح بـ OpenWeatherMap أو "هيفنغ للطقس" (QWeather) — كلاهما يوفر حصة مجانية، وسجّل فاستخدم. لنأخذ OpenWeatherMap مثالًا:

1. سجّل حسابًا ← أنشئ مفتاحًا (apikey) من صفحة API keys؛
2. النسخة المجانية تستدعي واجهة Current Weather (الطقس الحالي): api.openweathermap.org/data/2.5/weather? q=beijing&appid=مفتاحك&units=metric؛
3. جرّبها أولًا في المتصفح وانظر كيف يبدو JSON المعاد — هذا "واجب التحضير" اللازم قبل استدعاء أي API.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
تحذير من الفخاخ: لا تثبّت المفتاح في الكود إطلاقًا

{class="mt-1"}
مفتاح API يشبه "كلمة سر محفظتك"؛ إذا كتبته في الكود ودفعت إلى GitHub ستسرقه الزواحف خلال ساعات ويُستهلك دون إذنك. الطريقة الصحيحة: ضعه في local.properties (وهذا الملف مستثنى عبر gitignore)، ثم اقرأه في الكود عبر buildConfig من Gradle. ابحث عن "أفضل الممارسات لإخفاء مفتاح API في Android" واتبع الشرح.
:::

#### ثانيًا: طبقة الشبكة: Retrofit + تحليل JSON

عرّف "نموذج البيانات" وفق JSON المعاد من الـ API، وتجاهل الحقول غير المتطابقة:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · نموذج البيانات + الواجهة</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"صافٍ"}],"main":{"temp":26.5,"humidity":40},"name":"الرياض"}
data class WeatherResponse(
    val weather: List&lt;Weather&gt;,
    val main: Main,
    val name: String
)
data class Weather(val description: String)
data class Main(val temp: Double, val humidity: Int)

interface WeatherApi {
    @GET("data/2.5/weather")
    suspend fun getWeather(
        @Query("q") city: String,
        @Query("appid") key: String,
        @Query("units") metric: String = "metric",
        @Query("lang") lang: String = "zh_cn"
    ): WeatherResponse
}
```
:::

سيضع Gson بيانات JSON تلقائيًا في صنوف data class هذه — متى تطابقت أسماء الحقول حدث السحر تلقائيًا.

#### ثالثًا: حالات الواجهة الثلاث: جارٍ التحميل / نجاح / فشل

روح التطبيق المتصل بالشبكة في "إدارة الحالات". الشبكة بطيئة، أو منقطعة، أو اسم المدينة مكتوب خطأ… كل حالة تستحق ردًا واضحًا للمستخدم. عبّر عنها بأناقة عبر sealed class (صنف مغلق):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · حالة الواجهة</span><span class="dots">···</span>
:::

```
sealed class UiState {
    object Loading : UiState()                    // جارٍ التحميل
    data class Success(val data: WeatherResponse) : UiState()  // نجاح
    data class Error(val message: String) : UiState()          // فشل
}

// في الـ ViewModel:
fun search(city: String) {
    viewModelScope.launch {
        _state.value = UiState.Loading
        _state.value = try {
            UiState.Success(api.getWeather(city))
        } catch (e: Exception) {
            UiState.Error("تعذر العثور على هذه المدينة، جرّب اسمًا آخر؟")
        }
    }
}

// في الواجهة:
when (val s = state) {
    is UiState.Loading -&gt; CircularProgressIndicator()   // مؤشر تحميل دائري
    is UiState.Success -&gt; WeatherContent(s.data)        // يعرض
    is UiState.Error -&gt; Text(s.message)                 // يعرض الخطأ
}
```
:::

قالب Loading/Success/Error ثلاثي المراحل هو "الوصفة الذهبية" لواجهات الشبكة؛ احفظه أولًا ثم استخدمه في كل تطبيق متصل مستقبلًا.

#### رابعًا: كود الواجهة عمليًا: لرسم الطقس

بعد الحالة هكذا تبدو الواجهة (المقاطع الأساسية):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · شاشة الطقس (مقطع رئيسي)</span><span class="dots">···</span>
:::

```
@Composable
fun WeatherContent(data: WeatherResponse) {
    Column(
        Modifier.fillMaxSize().padding(24.dp),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text(data.name, fontSize = 28.sp, fontWeight = FontWeight.Bold)
        Text(
            "${data.main.temp}°C",
            fontSize = 72.sp,
            fontWeight = FontWeight.Light
        )
        Text(
            data.weather.firstOrNull()?.description ?: "غير معروف",
            fontSize = 20.sp,
            color = Color.Gray
        )
        Spacer(Modifier.height(16.dp))
        Row {
            Text("💧 الرطوبة ${data.main.humidity}%")
            Spacer(Modifier.width(24.dp))
            Text("🌡️ الإحساس ${data.main.temp}°C")
        }
    }
}
```
:::

تفاصيل صغيرة تستحق التعلم: firstOrNull() تلتقط العنصر الأول بأمان (قد تكون القائمة فارغة)، و?: "غير معروف" يوفر نصًا احتياطيًا — فمبدأ أمان الفراغ يسري على الواجهة أيضًا. تُعرض الحرارة بخط 72.sp الكبير ليحتل الصدارة، ووزن الخط "الخفيف" (Light) يجعل الأرقام تبدو أنيقة — هذه الوصفة الكلاسيكية لتطبيقات الطقس.

#### خامسًا: تفاصيل الواجهة والتفاعل

- مربع البحث: TextField في الأعلى، اكتب اسم المدينة وانقر بحث (اضبط إجراء "بحث" على لوحة المفاتيح فيبحث Enter مباشرة)؛
- بطاقة الطقس: حرارة بخط كبير (26.5°)، ووصف الطقس (صافٍ)، والرطوبة، واسم المدينة؛
- المدن المفضلة: خزّن المدن التي تتابعها كثيرًا في DataStore لتبحث عنها تلقائيًا عند الفتح القادم — وفرصة لمراجعة الفصل 6؛
- السحب للتحديث: استخدم في Compose مكوّن PullToRefreshBox (الموفر من Material 3) فيصبح "الإحساس الاحترافي" فوريًا.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
نصيحة: الصور تنبض بالواجهة حياة

{class="mt-1"}
أعطِ كل حالة طقس رمزًا تعبيريًا أو أيقونة (☀️🌧️❄️) عبر التعيين when(description) — ثلاثة أسطر تضاعف "الدفء البصري" للواجهة. يمكن أيضًا استخدام مكتبة أيقونات طقس من طرف ثالث، لكن الرموز التعبيرية تكفي في مرحلة التمرين.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
لنتجرب: قائمة قبول تطبيق الطقس

{class="mt-1"}
① البحث عن الطقس يعمل طبيعيًا؛ ② عند قطع الشبكة يعرض التطبيق رسالة خطأ أنيقة دون انهيار (جرّب وضع الطيران!)؛ ③ عند إدخال مدينة غير موجودة تظهر رسالة لطيفة؛ ④ احفظ مدينتين في المفضلة وتبقيان بعد إعادة تشغيل التطبيق؛ ⑤ تدوير الشاشة لا يفقد الحالة. اجتياز البنود الخمسة كلها يعني تخرج هذا المشروع.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
خلاصة الفصل

- جرّب الـ API في المتصفح وافهم JSON أولًا ثم اكتب الكود — "التحضير" لا يخسر أبدًا
- خزّن مفتاح API داخل ملف local.properties ولا تدعه يدخل مستودع الكود أبداً
- واجهة Retrofit مع data class: بتطابق الحقول يُحلَّل JSON تلقائياً
- حالات التحميل/النجاح/الخطأ الثلاث هي الحل الجامع لأي واجهة متصلة بالإنترنت
- انقطاع الشبكة، وإدخال فارغ، ومدينة غير موجودة — معالجة الأخطاء هي الحد الأدنى للقبول في أي تطبيق متصل بالإنترنت
:::
