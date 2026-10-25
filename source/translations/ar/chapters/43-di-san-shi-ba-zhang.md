---
id: di-san-shi-ba-zhang
num: 38
part: ai-biancheng-pian
nav: الفصل 38: المبادئ الخمسة للتفكير في برمجة الذكاء الاصطناعي
toc: default
kind: chapter
---

### الفصل 38: المبادئ الفكرية الخمسة لبرمجة الذكاء الاصطناعي

{class="chapter-intro mb-4"}
إذا كان هذا الكتاب سيعلّمك فصلًا واحدًا، فليكن هذا الفصل. المبادئ الفكرية الخمسة هي قلب الكتاب، وكل الفصول اللاحقة — السياق، والمتطلبات، والمحادثة، والجودة — هي تطبيقات لهذه المبادئ في سياقات مختلفة. لا تقلق، كل مبدأ ليس صعبًا، لكن كل واحد يستحق أن «يترسخ في عضلاتك» عبر عدة مشاريع.

بداية القصة مثيرة: عندما نشر Andrej Karpathy مشروعه مفتوح المصدر، أرفق ملف CLAUDE.md من 70 سطرًا فقط، لخّص أربع مبادئ أساسية للتعاون مع الذكاء الاصطناعي. حصل هذا الملف على أكثر من 70,000 نجمة على GitHub، ليصبح المرجع الأكثر اقتباسًا عالميًا لممارسي برمجة الذكاء الاصطناعي. هذه المبادئ ليست شعارات فارغة، بل عادات تفكير عملية مستخلصة من ممارسة واسعة. وأضاف هذا الكتاب المبدأ الخامس — التحقق التكراري — ليكتمل نظام المبادئ الخمسة.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
لماذا ملف 70 سطرًا بهذه القيمة؟

{class="mt-1"}
ما معنى 70,000 نجمة؟ معظم مشاريع GitHub لن تصل إلى هذا الرقم أبدًا. حصول ملف نصي من 70 سطرًا عليها يثبت شيئًا واحدًا: في عصر الذكاء الاصطناعي، النادر ليس الكود، بل القدرة على «التوضيح». هذه الـ70 سطرًا هي نسخة مركزة من «التوضيح».
:::

#### أولاً، المبدأ الأول: Think Before Coding (فكر قبل الترميز)

هذا أكثر المبادئ مخالفة للحدس. إذا كان الذكاء الاصطناعي يكتب الكود، فلماذا «نفكر أولًا»؟ الإجابة بسيطة: جودة مخرجات الذكاء الاصطناعي تتناسب مع جودة مدخلاتك. إذا لم توضح ما تريد، فستغرق في حلقة «تعديل بلا نهاية» — وهي ما يسمى «الذكاء الاصطناعي يضيع معك».

«الفكر قبل» تعني أنه قبل إعطاء الأوامر للذكاء الاصطناعي، يجب الإجابة على ثلاثة أسئلة تشكل «مثلث التفكير»:

1. ما المشكلة التي أريد حلها؟ (الهدف)
2. كيف يبدو النتيجة المتوقعة؟ (معايير القبول)
3. ما القيود التي يجب الالتزام بها؟ (الحدود)

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">بُعد التفكير</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">إدخال غامض (سيئ)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">إدخال واضح (جيد)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تعريف المشكلة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ساعدني في إنشاء موقع</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ساعدني في إنشاء موقع أدوات شخصية يعرض بطاقات دخول لثلاثة أدوات ذكاء اصطناعي</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">النتيجة المتوقعة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">اجعله جميلًا</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تصميم متجاوب، وسمة داكنة، وحركة عند التمرير، ويعمل على الهاتف</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">القيود</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">(غير مذكورة)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">بدون أطر عمل، HTML+CSS+JS فقط، ملف واحد، بدون خادم خلفي</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
مقارنة بين الإدخال الغامض والواضح لنفس المتطلب

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ملاحظة: التفكير المسبق ≠ كتابة مستند مثالي

{class="mt-1"}
«الفكر قبل» لا تعني «اكتب PRD مثاليًا ثم ابدأ». بل عملية تفكير سريعة ومنظمة — اقضِ 30 ثانية في توضيح الأسئلة الثلاثة، أفضل من 30 دقيقة في تعديلات متكررة. للمهام الصغيرة يمكن أن تكون الإجابات مختصرة؛ وللمشاريع الكبيرة يمكن توسيعها إلى مستند متطلبات كامل (راجع الفصل 40).
:::

#### ثانيًا، المبدأ الثاني: Simplicity First (البساطة أولًا)

أكبر فخ في برمجة الذكاء الاصطناعي ليس «عدم القدرة على الإنجاز»، بل «الإنجاز الزائد». عندما تقول «أنشئ نظام إدارة مستخدمين»، قد يولد نظامًا كاملًا للمصادقة والصلاحيات والأدوار وسجلات التدقيق وتصدير البيانات — بينما قد تحتاج فقط إلى صفحة تسجيل دخول بسيطة. الإفراط في التوليد هو السبب الرئيسي لانتفاخ الكود.

«البساطة أولًا» تطلب منك اتباع مبدأ «الحد الأدنى القابل للتطبيق» في كل أمر: أنجز الوظيفة الأساسية بأقل كود، وحل المشكلة بأبسط حل، واختبر الفكرة بأقل ميزات. قال Karpathy تشبيهًا بليغًا: «إذا أردت حساب سعر الخصم، فلا تحتاج إلى محرمة تجارة إلكترونية.»

في الممارسة، تعني «البساطة أولًا» عادات عمل محددة:

- اجعل الذكاء الاصطناعي ينفذ وظيفة واحدة في كل مرة، لا النظام كله دفعة واحدة؛
- فضّل المكتبات القياسية والحلول البسيطة على الاعتماديات المعقدة؛
- ما يمكن حله بـ50 سطرًا، لا تدعِ الذكاء الاصطناعي يكتب 500 سطر؛
- عندما تتجاوز المخرجات النطاق المتوقع، أخبره بشجاعة «احذف الزائد».

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الموقف</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الحل المفرط (تجنّبه)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الحل البسيط (موصى به)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الحاجة إلى تخزين البيانات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">بناء قاعدة بيانات MySQL + ORM</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">استخدم ملف JSON أو SQLite أولًا</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الحاجة إلى تسجيل دخول المستخدم</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OAuth2.0 + JWT + صلاحيات الأدوار</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ابدأ بالتحقق البسيط من كلمة المرور</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الحاجة إلى إطار عمل واجهة أمامية</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">React + Redux + Router</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">جرّب HTML + JS الأصلي أولًا</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الحاجة إلى النشر</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Docker + CI/CD + K8s</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">شغّله محليًا أولًا ثم فكر في النشر</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
مقارنة الحلول المفرطة والبسيطة في المواقف الشائعة

#### ثالثًا، المبدأ الثالث: Surgical Changes (التعديل الجراحي)

عند تطوير مشروع قائم، يجب أن يكون كل تعديل دقيقًا كالجراحة — لا تلمس إلا ما يجب لمسه. وهذا مهم بشكل خاص في برمجة الذكاء الاصطناعي، لأن الذكاء الاصطناعي يميل إلى «التعديل العرضي»: تطلب إصلاح خطأ، فيعيد هيكلة نصف الملف.

جوهر «التعديل الجراحي»: حدد في كل أمر نطاق وحدود التعديل. قل له «عدّل فقط الدالة calculate_discount» و«لا تلمس الباقي» و«حافظ على نمط الكود الحالي». وإذا تجاوز التعديل النطاق المطلوب، اطلب فورًا التراجع عن الزائد.

وضح Karpathy ذلك بمثال diff (مقارنة الفروقات). افترض أنك طلبت إضافة منطق «سعر العضوية» لدالة حساب الخصم في سلة التسوق: النتيجة الجيدة هي تعديل هذه الدالة فقط مع إضافة بضعة أسطر؛ والنتيجة السيئة هي إعادة هيكلة الملف بالكامل — حتى لو بدا الكود الجديد «أكثر أناقة»، لا يمكنك التأكد من عدم إدخال أخطاء جديدة. في برمجة الذكاء الاصطناعي، «أن يبدو أفضل» لا يبرر أبدًا الانحراف عن الأمر.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
أمر سيئ (نطاق غامض)

{class="font-mono text-xs leading-relaxed"}
ساعدني في تحسين منطق حساب الخصم في هذا المشروع
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
أمر جيد (نطاق محدد بدقة)

{class="font-mono text-xs leading-relaxed"}
عدّل فقط الدالة calculate_discount في cart.py: 1. أضف منطق سعر العضوية على الخصم الحالي 2. يحصل الأعضاء على خصم إضافي 10% 3. لا تغير توقيع الدالة أو الدوال الأخرى 4. حافظ على نمط تسمية المتغيرات الحالي
:::
:::

#### رابعًا، المبدأ الرابع: Goal-Driven Execution (التنفيذ المدفوع بالأهداف)

يجيب هذا المبدأ عن سؤال جوهري: هل تعطي الذكاء الاصطناعي أمرًا «كيف تفعل» أم «ماذا تفعل»؟ إجابة Karpathy هي الثانية. بدلًا من قوله «أنشئ فئة أولًا، ثم أضف طرقًا، ثم اكتب اختبارات»، قل له «أحتاج إلى أداة تحلل ملف CSV وتعد القيم الفريدة في كل عمود». دع الذكاء الاصطناعي يحدد مسار التنفيذ، وأنت تتحقق من النتيجة.

فوائد «التنفيذ المدفوع بالأهداف» مزدوجة. للذكاء الاصطناعي مساحة أكبر لاختيار المسار الأمثل، بدلاً من التقييد بخطواتك الوسيطة؛ لك أنت، تنتقل التركيز من «كيف» إلى «هل النتيجة صحيحة؟» — وهذا هو دور القائد.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ملاحظة: التنفيذ المدفوع بالأهداف ≠ التخلي عن الرقابة

{class="mt-1"}
يجب عليك التحقق الصارم بعد التنفيذ: هل تحقق النتيجة من المتطلبات؟ هل عولجت الحالات الحدية؟ هل يوجد تصميم مفرط؟ وإذا لم تتطابق النتيجة مع التوقعات، قدم ملاحظات محددة — وليس «أعد الكتابة»، بل «المشكلة هنا أن الإدخال الفارغ يسبب IndexError، يرجى إضافة فحص للقيم الفارغة».
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">أسلوب الأمر</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">مثال</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">سمات النتيجة</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الأمر (كيف تفعل)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">«أنشئ فئة Python اسمها DataParser، وأضف طريقة parse تستقبل filename، وتستخدم وحدة csv للقراءة…»</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">يصبح الذكاء الاصطناعي كاتبًا آليًا، وقد لا تكون خطواتك الوسيطة المسار الأمثل</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الهدف (ماذا تفعل)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">«أحتاج إلى أداة: تقرأ ملف CSV، وتعد القيم الفريدة في كل عمود، وتخرجها بصيغة JSON. قدّم تنفيذًا كاملًا.»</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">يختار الذكاء الاصطناعي المسار الأمثل، وأنت تتحقق من النتيجة</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
مقارنة بين أوامر «كيف» وأوامر «ماذا»

#### خامسًا، المبدأ الخامس: Iterate and Verify (التكرار والتحقق)

هذا هو المبدأ الخامس الذي يضيفه هذا الكتاب على مبادئ Karpathy الأربع. قناعته الجوهرية: مخرجات الذكاء الاصطناعي الأولى ليست أبدًا النسخة النهائية. البرمجة الفعالة هي حلقة «توليد-تحقق-تصحيح»، وليست «أمر-مخرج» لمرة واحدة.

«التكرار والتحقق» ليس «أعد المحاولة إذا فشل» بشكل سلبي، بل عملية تحقق منظمة. بعد كل مخرج، تحقق على ثلاثة مستويات:

- المستوى الأول · التحقق الوظيفي: هل يعمل؟ هل الإدخال والإخراج صحيحان؟
- المستوى الثاني · التحقق الحدي: ماذا يحدث عند الإدخال الفارغ أو الطويل جدًا أو غير القياسي؟
- المستوى الثالث · التحقق المعماري: هل بنية الكود معقولة؟ هل يوجد ترميز ثابت؟ هل يسهل التوسع لاحقًا؟

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-bullseye mr-1"></i> تحديد الهدف</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> الذكاء الاصطناعي يولّد الكود</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> تحقق وظيفي</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> ناجح</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> تحقق من الحالات الحدية</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> ناجح</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-landmark mr-1"></i> مراجعة المعمارية</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> ناجح، ننتقل للخطوة التالية</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> فاشل</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> تقديم تغذية راجعة محددة</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> إعادة التوليد</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
الشكل 2: حلقة التكرار والتحقق في برمجة الذكاء الاصطناعي
:::

مفتاح هذه الحلقة هو «تقديم ملاحظات محددة». عند فشل التحقق، لا تقل «هذا خاطئ، أعد»، بل قل «الدالة تسبب IndexError عند الإدخال الفارغ، أضف فحص قيم فارغة في السطر 15». الملاحظات المحددة تجعل التصحيح دقيقًا؛ أما الغامضة فتجعله يخمّن نيتك من جديد.

#### سادسًا، Harness Engineering: الوكيل = النموذج + الهيكل

في منتصف 2026، انتشر مفهوم Harness Engineering في مجتمع برمجة الذكاء الاصطناعي. صيغته بسيطة:

:::inline div .quote-line .text-center .text-base .font-bold
<strong>قدرة الـ Agent = قدرة النموذج × جودة الـ Harness</strong>
:::

قدرة النموذج هي السقف العقلي لدماغ الذكاء الاصطناعي؛ والهيكل (Harness) هو «بيئة العمل» المحيطة بالنموذج — تشمل إدارة السياق وتكامل الأدوات وتنسيق العمليات ونظام الذاكرة.

يوضح هذا المفهوم حيرة شائعة: لماذا باستخدام GPT-4 أو Claude نفسه، ينجح بعض الناس في مشاريع مذهلة، بينما يحصل آخرون على كود عادي؟ الفرق ليس في النموذج، بل في الهيكل. الهيكل الجيد يشمل: ملف مواصفات مشروع واضح، وتكامل أدوات منطقي، وسياق محادثة منظم، وعملية تحقق متكاملة. النموذج يحدد السقف، والهيكل يحدد مدى استغلالك له.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
تشبيه المتدبق العبقرية

{class="mt-1"}
تخيّل النموذج متدبقًا عبقريًا — ذكاء عالٍ، لكن بدون مستندات خلفية المشروع أو معرفة الأدوات أو المواعيد النهائية ومعايير القبول، لن ينتج شيئًا جيدًا. Harness Engineering هي هندسة «كيف تهيئ بيئة العمل للمتدبق العبقرية».
:::

الفصول اللاحقة في هذا الكتاب تعلمك في جوهرها كيف تبني هيكلًا جيدًا: الفصل 39 يعلمك إدارة السياق (نظام ذاكرة المشروع)، والفصل 40 يعلمك تحديد المتطلبات (PRD)، والفصل 43 يعلمك تقنيات المحادثة (تجميع الأوامر)، والفصل 45 يعلمك ضمان الجودة (عملية التحقق). مجتمعة، هذه هي بنيتك.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
تطبيق عملي: حلّل فكرتك القادمة بـ«مثلث التفكير»

{class="mt-1"}
اختر شيئًا صغيرًا أردت فعله منذ فترة (مثل صفحة العد التنازلي أو سكربت تذكير بشرب الماء). اقضِ 3 دقائق في الإجابة: ① ما المشكلة التي يحلها؟ ② كيف تبدو النتيجة؟ ③ ما القيود (الوقت، التقنية، البيئة)؟ ثم اكتب الإجابة في فقرة. مبروك، لقد أتممت أول «Think Before Coding» في حياتك — وهذه الفقرة هي أمر عالي الجودة.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
ملخص الفصل

- المبادئ الخمسة من ملف CLAUDE.md البالغ 70 سطرًا لـ Karpathy (70 ألف+ نجمة)، وأضاف هذا الكتاب المبدأ الخامس «التكرار والتحقق»
- Think Before Coding: أجب عن ثلاثة أسئلة قبل البدء — ماذا؟ كيف النتيجة؟ ما القيود؟
- Simplicity First: أكبر فخ هو «الإنجاز الزائد» — حساب الخصم لا يحتاج محرمة تجارة إلكترونية
- Surgical Changes: تعديل دقيق كالجراحة، ورفض «التعديل العرضي»
- Goal-Driven Execution: قل «ماذا» لا «كيف»، ودع الذكاء الاصطناعي يختار المسار
- Iterate and Verify: تحقق من ثلاث طبقات (وظيفي/حدّي/معماري) + ملاحظات محددة، وكرر
- Harness Engineering: القدرة = النموذج × الهيكل، وأدر الذكاء الاصطناعي كـ«متدبق عبقري»
:::
