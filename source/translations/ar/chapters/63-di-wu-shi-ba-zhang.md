---
id: di-wu-shi-ba-zhang
num: 58
part: an-zhuo-kai-fa-pian
nav: الفصل 58: الدليل المرجعي السريع والمصادر
toc: default
kind: chapter
---

### الفصل 58: دليل المراجعة السريعة والمصادر

{class="chapter-intro mb-4"}
هذا الفصل دليل مراجعة سريعة صالح للاستخدام المستقل. عندما تخلط عليك طريقة كتابة ما أو تحتاج إلى قرار سريع، افتحه مباشرة. ننصحك بجعله «بطاقة جيب»: مراجعة الكود الشائع، والأسئلة المتكررة، ومصادر التعلم، دون تفويت صفحة.

#### أولاً: بطاقة المراجعة السريعة للكود الشائع

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ماذا تريد أن تفعل</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الكود الأساسي</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">حفظ حالة قابلة للتغيير</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">var x by remember { mutableStateOf(القيمة الابتدائية) }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">عدم فقدان الحالة عند تدوير الشاشة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">rememberSaveable { mutableStateOf(القيمة الابتدائية) }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تخطيط عمودي/أفقي</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Column { }</code> / <code class="inline">Row { }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">قائمة بالتحميل الكسول</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">LazyColumn { items(القائمة) { ... } }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">التنقل بين الشاشات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">navController.navigate("المسار")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تنفيذ أعمال الانتظار داخل coroutine</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">viewModelScope.launch { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مراقبة تدفق البيانات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">val list by flow.collectAsState()</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تخزين إعدادات صغيرة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">context.dataStore.edit { it[KEY] = القيمة }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تخزين بيانات مهيكلة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ثلاثية Room: @Entity / @Dao / @Database</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">جلب البيانات عبر الإنترنت</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">واجهة Retrofit + دالة suspend</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">إرسال إشعار</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">NotificationChannel + NotificationCompat.Builder</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">كتابة السجلات (Log)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Log.d("TAG", "message")</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
بطاقة مراجعة تطوير Android (إصدار أغسطس 2026)

#### ثانياً: الأسئلة الشائعة

س1: لا أعرف البرمجة إطلاقاً، فكم أحتاج من الوقت لتعلم تطوير Android؟

اتبع مسار هذا الكتاب: في الأسبوعين 1-2 جهّز البيئة وتعلم أساسيات Kotlin؛ في الأسبوعين 3-4 تعلم Compose وابنِ واجهة؛ في الأسبوعين 5-6 أكمل مشروع دفتر المصاريف؛ في الأسبوعين 7-8 أتم مشروع الطقس. شهران تنتقل فيهما من الصفر إلى القدرة على صنع تطبيق صغير باستقلال. الشرط أن تخصص 1-2 ساعة يومياً وأن تكتب الكود بيدك لا أن تكتفي بالقراءة.

س2: هل ما زلت بحاجة إلى تعلم Java؟

لا داعي. المشاريع الجديدة والدروس الجديدة والوظائف الجديدة تعتمد Kotlin أساساً. ولن تصطدم بكثير من Java إلا عند «صيانة مشروع عمره عشر سنوات». وبعد إتقان Kotlin ستعوّض Java سريعاً إن اقتضت العمل — فكلاهما يقوم على بيئة الجهاز الافتراضي نفسها.

س3: المحاكي أم الجهاز الحقيقي؟

المحاكي مريح للتطوير والتصحيح (لقطات الحالة وتعدد الطرازات)، لكن القبول النهائي لا بد أن يكون على جهاز حقيقي — فاللمس والأداء والشبكة الفعلية والمستشعرات لا يعوّضها المحاكي. وإن سمحت الظروف فاقتناء جهاز حقيقي متوسط الفئة للاختبار هو أجدى استثمار.

س4: هل سوق العمل جيد لتطوير Android؟

أوضاع 2026: المنافسة شديدة على الوظائف المبتدئة التي تقتصر على «كتابة الواجهات»، لكن المطوّر الذي «يتقن Kotlin + يفهم البنية + لديه عمل منشور» ما زال مطلوباً بشدة. وأنت في فترة التعلم، أفضل سيرة ذاتية لك هو ذلك التطبيق الذي صنعته بنفسك في المتجر.

س5: ماذا أفعل إذا علقت أمام رسالة خطأ؟

الخطوات الذهبية الثلاث: ① ابحث عن السطر الأول من الخطأ حرفياً في StackOverflow أو محرك بحث؛ ② راجع الصفحة المقابلة في الوثائق الرسمية؛ ③ إن لم ينجح ذلك، اجمع «السلوك المتوقع + الظاهر الفعلي + نص الخطأ كاملاً + الكود ذي الصلة» وأرسلها سؤالاً إلى الذكاء الاصطناعي أو المجتمع. الغالبية العظمى من المشاكل تُحل في الخطوة الأولى.

#### ثالثاً: مصادر تعلم موصى بها

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">النوع</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">المصدر</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">سبب التوصية</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">رسمي</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">developer.android.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الوثائق الرسمية لـ Android، وفيها دروس Compose وKotlin — المرجع الأول والأوثق</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">رسمي</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">موقع Kotlin الرسمي (kotlinlang.org)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">وثائق اللغة الرسمية + ساحة تجريب على الإنترنت</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">رسمي</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Google Codelabs</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">دروس عملية خطوة بخطوة يد بيد، وأشد ودّية للمبتدئين</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مجتمع</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stack Overflow (وسم android)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">المحطة الأولى لطلب المساعدة عند الأخطاء</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مجتمع</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">قسما Android في Juejin وCSDN</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مقالات عملية بالصينية كثيرة؛ انتبه للتمييز بين الجديد والقديم (اقرأ التاريخ أولاً)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">فيديو</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">قناة Google Developers الرسمية</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">شرح التقنيات الجديدة في مؤتمر المطورين كل عام</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مرافق للكتاب</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">القسم السابع «التطبيق العملي لبرمجة الذكاء الاصطناعي» (الفصول 37-47)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">المنهجية الكاملة لتطوير Android بمساعدة الذكاء الاصطناعي</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
قائمة مصادر تعلم تطوير Android (أغسطس 2026)

#### رابعاً: مراجعة سريعة لأوامر Gradle الشائعة

النقر على الأزرار يكفي عادة، لكن سطر الأوامر أجدى أحياناً (خصوصاً مع أدوات الذكاء الاصطناعي أو خطوط CI):

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الأمر</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الوظيفة</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew assembleDebug</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">بناء APK نسخة التصحيح (على Windows احذف ./)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew assembleRelease</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">بناء نسخة النشر (يتطلب ضبط التوقيع)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew test</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تشغيل جميع اختبارات الوحدة</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew lint</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">فحص ساكن: كشف الأخطاء الكامنة والكتابات غير القياسية</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew clean</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تنظيف مخلفات البناء (النظير التصريفي لأسلوب «إعادة التشغيل»)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew :app:dependencies</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">عرض شجرة التبعيات (سلاح ممتاز لتشخيص تعارض الإصدارات)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
مراجعة سريعة لأوامر Gradle الشائعة

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
نصيحة: عند مشكلة في البناء ابدأ بـ clean

{class="mt-1"}
ظاهرة «كان يعمل أمس وتوقف اليوم» سببها في ست أو سبع حالات من كل عشر خلل في ذاكرة البناء المؤقتة. بعد ./gradlew clean أعد البناء، فذلك يشفي أغلب المشاكل الغامضة. وإن لم ينجح فأعد تشغيل Android Studio — وخذ هذه الحيلة مع File ← Invalidate Caches معاً.
:::

#### خامساً: خاتمة — من أول تطبيق إلى التطبيق رقم N

بالنظر إلى الوراء، انتقلت من «لا أعرف ما هو Activity» إلى تجهيز البيئة وإتقان Kotlin ورسم الواجهات بـ Compose وربط التطبيق بقاعدة بيانات وشبكة، ثم الاختبار والتجزئة والنشر — في هذا الطريق قطعتَ أصعب جزء من الرحلة من الصفر إلى الواحد.

عالم التقنية يتغير بسرعة: الأطر تترقى، والأدوات تتبدل، والذكاء الاصطناعي يتولى المزيد من أعمال «ضرب المفاتيح». لكن شيئاً واحداً لا يبطل: قدرتك على تفكيك فكرة غامضة إلى خطوات واضحة ثم تنفيذها خطوة خطوة. الأدوات مضخّمات، والفكر أساس. المضخّم يُستبدل، والأساس لا يهتز.

:::inline div .quote-line
لم تعد مجرد "شخص يعرف استخدام الهاتف". يمكنك أن تحوّل أفكارك في رأسك إلى تطبيقات تعمل فعلًا على ثلاثمئة مليون جهاز أندرويد. من اليوم، ابتكر بلوحة المفاتيح — هذه هي رومانسية مطوّري أندرويد.
:::

#### المراجع

{class="list-decimal pl-6 mb-3 space-y-1 text-xs text-gray-500"}
1. Android Developers. (2026). Android Developer Guides and Jetpack Compose Documentation. developer.android.com.
2. Kotlin Foundation. (2026). Kotlin Language Documentation. kotlinlang.org.
3. Android Open Source Project. (2026). Android Platform Version History and API Levels.
4. Google Play. (2026). Play Console Help: Publishing and App Signing.
5. AndroidX Release Notes. (2026). Room / DataStore / Navigation / WorkManager releases.
6. Square. (2026). Retrofit Documentation. github.com/square/retrofit.
