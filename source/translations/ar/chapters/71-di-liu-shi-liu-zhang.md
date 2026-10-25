---
id: di-liu-shi-liu-zhang
num: 66
part: ios-kai-fa-pian
nav: الفصل 66: المشروع الثاني — تطبيق الاستعلام عن الطقس (نسخة شبكية)
toc: default
kind: chapter
---

### الفصل 66: المشروع الثاني — تطبيق الاستعلام عن الطقس (نسخة شبكية)

{class="chapter-intro mb-4"}
دفتر الحسابات كان «تدريبًا على القوة الداخلية»، وتطبيق الطقس «تعرفًا على العالم» — فهو يتعامل مع الإنترنت. في هذا المشروع ستتعلم: طلب API مجاني، وتحليل JSON، والتعامل مع حالات الواجهة الثلاث «جار التحميل / النجاح / الفشل»، وكيف تخفي مفتاح API جيدًا. وبإتمامه ستملك القدرة على صنع أي «تطبيق شبكي» — الأخبار وأسعار الصرف والترجمة، فالطريقة واحدة عينها.

#### أولًا: طلب واجهة طقس مجانية (API)

للتدريب الشخصي ننصح بـ OpenWeatherMap أو الخدمة الصينية QWeather (طقس هفنغ) — فكلاهما يمنح حصة مجانية تعمل فور التسجيل. ولنأخذ OpenWeatherMap مثالًا:

1. سجل حسابًا → في صفحة API keys أنشئ مفتاحًا (apikey)؛
2. النسخة المجانية تستدعي واجهة Current Weather: api.openweathermap.org/data/2.5/weather? q=beijing&appid=مفتاحك&units=metric؛
3. جربها أولًا في المتصفح وانظر كيف يبدو JSON العائد — فهذا «الواجب التمهيدي» الذي لا بد منه قبل ربط أي API.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
تنبيه لتجنب الفخاخ: المفتاح لا يجوز أن يكتب ثابتًا في الكود أبدًا

{class="mt-1"}
مفتاح API أشبه بـ«كلمة سر محفظتك»؛ فما إن يكتب في الكود ويرفع إلى GitHub حتى تجرفه الزواحف خلال ساعات قليلة ويستخدم بغير حق. والطريقة الصحيحة في iOS: ضعه في Config.xcconfig (ملف إعدادات يتجاهله gitignore)، ثم اقرأه في الكود عبر Info.plist. ابحث عن «إدارة مفاتيح iOS باستخدام xcconfig» وعدّل وفق ما تجد.
:::

#### ثانيًا: طبقة الشبكة — URLSession مع Codable

عرّف النموذج أولًا وفق JSON الذي يعيده الـ API، ثم اكتب الخدمة:

::: div .code-block
:::inline div .code-head
<span>SWIFT · نموذج البيانات + الخدمة</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"صافٍ"}],"main":{"temp":26.5,"humidity":40},"name":"الرياض"}
struct WeatherResponse: Codable {
    let weather: [Weather]
    let main: Main
    let name: String
}
struct Weather: Codable { let description: String }
struct Main: Codable { let temp: Double; let humidity: Int }

struct WeatherService {
    let key: String   // يُقرأ من xcconfig

    func fetchWeather(city: String) async throws -> WeatherResponse {
        var comps = URLComponents(string: "https://api.openweathermap.org/data/2.5/weather")!
        comps.queryItems = [
            URLQueryItem(name: "q", value: city),
            URLQueryItem(name: "appid", value: key),
            URLQueryItem(name: "units", value: "metric"),
            URLQueryItem(name: "lang", value: "zh_cn")
        ]
        let (data, _) = try await URLSession.shared.data(from: comps.url!)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}
```
:::

#### ثالثًا: حالات الواجهة الثلاث — جار التحميل / النجاح / الفشل

روح التطبيق الشبكي في «إدارة الحالة». بطء الشبكة، وانقطاعها، وخطأ في اسم المدينة… لكل حالة يجب أن توضح الواجهة للمستخدم ما يجري. عبّر عنها بأناقة بـ enum مع switch:

::: div .code-block
:::inline div .code-head
<span>SWIFT · حالة الواجهة</span><span class="dots">···</span>
:::

```
enum LoadState {
    case loading                  // جارٍ التحميل
    case success(WeatherResponse) // نجاح
    case error(String)            // فشل
}

@Observable
class WeatherViewModel {
    var state: LoadState = .loading
    private let service = WeatherService(key: Config.apiKey)

    func search(city: String) async {
        state = .loading
        do {
            let data = try await service.fetchWeather(city: city)
            state = .success(data)
        } catch {
            state = .error("تعذر العثور على هذه المدينة، جرّب اسمًا آخر؟")
        }
    }
}

// في الواجهة:
switch vm.state {
case .loading: ProgressView("جارٍ التحميل…")
case .success(let d): WeatherContent(data: d)
case .error(let msg): Text(msg).foregroundColor(.secondary)
}
```
:::

هذا النمط الثلاثي loading/success/error هو «القالب المضمون متعدد الأغراض» للواجهات الشبكية؛ احفظه الآن، وسترسم على منواله كل تطبيقاتك الشبكية لاحقًا.

#### رابعًا: كود الواجهة عمليًا — نرسم الطقس

::: div .code-block
:::inline div .code-head
<span>SWIFT · شاشة الطقس (مقطع رئيسي)</span><span class="dots">···</span>
:::

```
struct WeatherContent: View {
    let data: WeatherResponse

    var body: some View {
        VStack(spacing: 12) {
            Text(data.name)
                .font(.title.bold())
            Text("\(Int(data.main.temp))°C")
                .font(.system(size: 76, weight: .thin))
            Text(data.weather.first?.description ?? "غير معروف")
                .font(.title3)
                .foregroundColor(.secondary)
            HStack(spacing: 24) {
                Label("الرطوبة \(data.main.humidity)%", systemImage: "humidity")
                Label("الإحساس \(Int(data.main.temp))°C", systemImage: "thermometer")
            }
        }
        .padding()
    }
}
```
:::

تفاصيل صغيرة تستحق التعلم: first? لالتقاط العنصر الأول بأمان (قد تكون القائمة فارغة)، و?? "غير معروف" نصًا احتياطيًا؛ وعرض درجة الحرارة بخط رقيق حجمه 76 وصفة كلاسيكية في تطبيقات الطقس؛ وLabel هو المكون الرسمي «أيقونة + نص»، وهو أنظم من تركيب HStack يدويًا.

#### خامسًا: تفاصيل التفاعل والمدن المفضلة

- حقل البحث: المُعدِّل .searchable في الأعلى يجلب تفاعل البحث من النظام، وعند الإرسال يستدعي vm.search؛
- المدن المفضلة: خزن المدن التي تتابعها كثيرًا في UserDefaults، فيستعلم عنها تلقائيًا عند الفتح التالي؛
- السحب للتحديث: .refreshable { await vm.search(...) } تكفي سطرًا واحدًا؛
- أيقونة الطقس: استخدم Image(systemName:) بالربط حسب الوصف (sun.max / cloud.rain / snowflake)، فتنبض الواجهة بالحياة فورًا.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
نصيحة: «عويصة» أسماء المدن الصينية

{class="mt-1"}
دعم OpenWeatherMap لأسماء المدن بالحروف الصينية متوسط، فالبحث عن «بكين» بالحروف الصينية قد يعود بلا نتائج بينما "beijing" يعمل عاديًا. والحل الاحترافي هو تضمين جدول تحويل «اسم المدينة → اسم إنجليزي/إحداثيات»، أو الربط بخدمة طقس محلية. في مرحلة التدريب يكفي أن تدعم أسماء المدن بالإنجليزية، فلا تشن حربًا مع هذا القصور.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
هيا نجرّب: قائمة قبول تطبيق الطقس

#### سادسًا: كيف تنقح طلبات الشبكة — الطباعة والتقاط الحزم ومحاكاة الشبكة البطيئة

إذا اختل تطبيق شبكي ففي تسع حالات من عشر يكون السبب «طلبًا لم يرسل صحيحًا» أو «استجابة لم تحلل صحيحة». ثلاث وسائل للتنقيح:

1. طباعة البيانات الخام: اطبع String(data: data, encoding: .utf8) لترى JSON الخام — فتتبين أسماء الحقول وأنواعها من نظرة واحدة، وهو أسرع من التخمين بعشرة أضعاف؛
2. أدوات التقاط الحزم: Proxyman المجاني على Mac أو Charles مفتوح المصدر يعترض طلبات التطبيق واستجاباته كلها، فترى طبقة الشبكة بوضوح أشعة X؛
3. محاكاة الشبكة الضعيفة: من قائمة المحاكي Features → Network Link Conditioner (تتطلب تنزيل أداة من موقع المطورين)، تحاكي شبكة 3G والتأخر العالي — فتكشف مشكلات تجربة «الدوامة التي لا تنتهي».

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
نصيحة: هل رفض ATS طلبك؟

{class="mt-1"}
إذا ظهر خطأ "App Transport Security" بمجرد إرسال الطلب فالأرجح أنك استخدمت عنوان http:// نصيًا صريحًا. الواجهات الرسمية يجب أن تكون HTTPS؛ وفي التنقيح المحلي افتح استثناء مؤقت (أضف NSAllowsLocalNetworking إلى Info.plist)، وتذكر تنظيفه قبل النشر.
:::

{class="mt-1"}
① البحث عن الطقس يعمل بشكل طبيعي؛ ② عند قطع الشبكة يعرض التطبيق رسالة خطأ أنيقة دون انهيار (جرب بإطفاء شبكة Mac من داخل المحاكي!)؛ ③ إدخال مدينة غير موجودة يعطي تنبيهًا ودودًا؛ ④ حفظ مدينتين مفضلتين يبقيهما بعد إعادة تشغيل التطبيق؛ ⑤ الواجهة لا تؤذي العين في الوضع الداكن. وإذا اجتازت البنود الخمسة كلها يكون هذا المشروع قد تخرج.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
خلاصة الفصل

- جرب الـ API في المتصفح وافهم JSON قبل كتابة الكود — فـ«الاستطلاع المسبق» لا يخسر أبدًا
- أخف مفتاح API في xcconfig، ولا يدخل مستودع الكود أبدًا
- نموذج Codable مع URLSession وasync/await: إذا تطابقت الحقول تحلل JSON تلقائيًا
- نمط الحالات الثلاث loading/success/error هو قالب كل الأغراض للواجهات الشبكية
- انقطاع الشبكة، والإدخال الفارغ، ومدينة غير موجودة — معالجة الأخطاء هي حد النجاح للتطبيقات الشبكية
:::
