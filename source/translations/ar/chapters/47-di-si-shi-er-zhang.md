---
id: di-si-shi-er-zhang
num: 42
part: ai-biancheng-pian
nav: الفصل 42: نظرة شاملة على النماذج الكبيرة والتطبيق العملي لواجهات API
toc: default
kind: chapter
---

### الفصل 42: مشهد النماذج اللغوية الكبيرة والتطبيق العملي لواجهات API

{class="chapter-intro mb-4"}
تناوبت الفصول السابقة «كيف تتعاون مع الذكاء الاصطناعي»، أما هذا الفصل فيعالج سؤالًا أكثر أساسية: «أي ذكاء اصطناعي تستخدم؟ وكيف تستخدمه؟». صار مشهد النماذج اللغوية الكبيرة في أغسطس 2026 بالغ الثراء — فعلى الساحة الدولية تتنافس ثلاث قوى كبرى هي GPT وClaude وGemini، وفي الصين تزدهر نماذج DeepSeek وتونغ يي تشيون وِن وGLM وKimi ودو باو. ولكل نموذج شخصيته وميزته الخاصة: الاختيار الصحيح يقلل الجهد ويضاعف النتيجة، والاختيار الخاطئ يضاعف الجهد ويقلل النتيجة. لن يعرّفك هذا الفصل بهذه النماذج فحسب، بل سيعلمك أيضًا كيف تربطها بتطبيقك عبر API، وكيف تختار خطة التوكنات (Token Plan) المناسبة حسب احتياجك.

#### أولًا: النماذج اللغوية الكبيرة الدولية الرائدة: مشهد القوى الثلاث

شكّل سوق النماذج اللغوية الكبيرة الدولي في أغسطس 2026 مشهدًا تقوده ثلاث قوى: OpenAI (سلسلة GPT) وAnthropic (سلسلة Claude) وGoogle (سلسلة Gemini). ولكل شركة سماتها الواضحة — فلنتعرف عليها واحدة تلو الأخرى.

##### 1. سلسلة GPT-5.6 من OpenAI: المحارب الشامل المتوازن

OpenAI هي الشركة التي أطلقت موجة النماذج اللغوية الكبيرة، ولا تزال سلسلة GPT حتى اليوم النماذج الأوسع استخدامًا عالميًا. واعتمدت سلسلة GPT-5.6 الصادرة في يوليو 2026 استراتيجية ثلاثة مستويات: النموذج الرائد GPT-5.6 Sol لاحتياجات الاستدلال المتقدمة، والنموذج المتوازن GPT-5.6 Terra للتطوير اليومي، والنموذج الخفيف GPT-5.6 Luna للسيناريوهات عالية التزامن ومنخفضة التكلفة. وتتشارك النماذج الثلاثة نافذة سياق تبلغ 1.05 مليون توكن، وجميعها تدعم إدخال الصور واستدعاء الدوال والمخرجات المهيكلة.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الطراز</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الفئة</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الإدخال (لكل مليون توكن)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الإخراج (لكل مليون توكن)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">نافذة السياق</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Sol</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">رائد للاستدلال</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">5.00 دولار أمريكي (نحو 36 يوانًا)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">30.00 دولار أمريكي (نحو 217 يوانًا)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1.05 مليون توكن</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Terra</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">متوازن للاستخدام اليومي</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.50 دولار أمريكي (نحو 18 يوانًا)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">15.00 دولار أمريكي (نحو 109 يوانات)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1.05 مليون توكن</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Luna</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">خفيف ومنخفض التكلفة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1.00 دولار أمريكي (نحو 7 يوانات)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6.00 دولار أمريكي (نحو 44 يوانًا)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1.05 مليون توكن</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
أسعار سلسلة GPT-5.6 من OpenAI (أغسطس 2026)

تكمن الميزة الجوهرية لسلسلة GPT في «التوازن» — استدلال وبرمجة وكتابة وتعدد وسائط دون نقاط ضعف واضحة. وتضاف إلى ذلك منظومة الإضافات الضخمة لدى OpenAI ومجتمع المطورين، وهي الأكثر اكتمالًا في الوثائق المتوافقة وسلاسل الأدوات. وفي السيناريوهات التي «لا تعرف فيها ماذا تختار»، فإن GPT هي الإجابة الافتراضية التي «لا تخيب وإن اخترتها وأنت مغمض العينين». لكن نقاط ضعفها: الوصول إليها من داخل الصين يتطلب شبكة خاصة، وأداؤها في التعبير بالصينية يحمل أحيانًا «طبعًا مترجمًا»، وأسعار API فيها متوسطة إلى مرتفعة.

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
خبر سار

{class="mt-1"}
أعلنت OpenAI في أغسطس 2026 ترقية النموذج الافتراضي للمستخدمين المجانيين إلى GPT-5.6 Luna، وفتح الدردشة النصية بلا حدود. هذا يعني أنه يمكنك تجربة القدرات الأساسية لـ GPT دون أي تكلفة، ولن تحتاج إلى الدفع إلا عند الحاجة إلى استدلال أقوى أو استدعاء عبر API.
:::

##### 2. سلسلة Claude من Anthropic: قمة البرمجة والدقة

إذا كانت GPT لاعبة شاملة، فإن Claude هو «القمة» في مجال البرمجة. فسلسلة Claude من Anthropic تتقدم بفارق ساحق ومستمر في اختبار SWE-bench (المعيار المرجعي لهندسة البرمجيات)، وتحتل المرتبة الأولى صناعيًا في جودة توليد الشيفرة والقدرة على تنفيذ المشاريع بمستوى هندسي. والأثمن من ذلك أن معدل الهلوسة في Claude (احتمال توليد معلومات زائفة) هو الأدنى على الإطلاق بنحو 1% فقط — وهذا يجعله مناسبًا بشكل خاص للسيناريوهات عالية الدقة مثل الأوساط الأكاديمية والشؤون القانونية.

ورقة Claude الرابحة الأخرى هي السياق فائق الطول: فهو يدعم نافذة سياق تبلغ مليون توكن، ويستطيع «قراءة» عقد من مئات الصفحات أو مكتبة شيفرة كاملة دفعة واحدة دون تفويت التفاصيل. وهذا أمر بالغ الصعوبة في السيناريوهات مثل إعادة هيكلة الشيفرة وتحليل المستندات الطويلة. وClaude Code بوصفه أداة برمجة بالذكاء الاصطناعي في الطرفية بلغت إيراداته السنوية 2.5 مليار دولار بحلول منتصف 2026 — وهو أقوى دليل على الاعتراف الواسع بقدرات Claude البرمجية.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الطراز</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الفئة</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الإدخال (لكل مليون توكن)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الإخراج (لكل مليون توكن)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">نافذة السياق</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Fable 5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الطراز الرائد</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">10.00 دولار أمريكي (نحو 72 يوانًا)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">50.00 دولار أمريكي (نحو 362 يوانًا)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مليون توكن</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Opus 4.8</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الطراز الاحترافي</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">5.00 دولار أمريكي (نحو 36 يوانًا)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">25.00 دولار أمريكي (نحو 181 يوانًا)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مليون توكن</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Sonnet 5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">طراز القيمة مقابل السعر</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.00 دولار أمريكي (نحو 14 يوانًا)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">10.00 دولار أمريكي (نحو 72 يوانًا)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مليون توكن</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
أسعار سلسلة Claude من Anthropic (أغسطس 2026، وسعر Sonnet 5 مخفَّض)

نقطة ضعف Claude هي السعر — فسعر الإخراج لدى Fable 5 هو الأعلى بين جميع النماذج، إذ يبلغ 50 دولارًا لكل مليون توكن. كما أن قدراته في تعدد الوسائط (فهم الصور والفيديو) ضعيفة نسبيًا. أما للمطورين الأفراد محدودي الميزانية، فإن Sonnet 5 خلال فترة الخصم يقدم قيمة استثنائية مقابل السعر.

##### 3. سلسلة Gemini من Google: ملك تعدد الوسائط

وصلت سلسلة Gemini من Google بحلول 2026 إلى الإصدار 3.1 Pro. وأقوى ورقة لدى Gemini هي تعدد الوسائط الأصيل — تحليل دقيق للصور والنصوص، وتعرف بلا أخطاء على الجداول عبر OCR، واستخراج فعال لإطارات الفيديو، مع دعم التحليل المتعمق للصوت والفيديو. وهو مرتبط بعمق بمنظومة Google (البحث والبريد والخدمات السحابية)، ويتميز في استرجاع المعلومات في الوقت الفعلي والفهم عبر الوسائط. كما يدعم Gemini إدخال سياق فائق الطول يبلغ مليوني توكن، وهو النموذج صاحب أكبر نافذة سياق حتى الآن.

تموضع Gemini هو «الخيار الأول لسيناريوهات الاستدلال العلمي وتعدد الوسائط». إذا كان مشروعك يتضمن تحليلًا مكثفًا للصور أو فهم فيديو أو حسابات علمية، فلن يجد Gemini شبه منافس. لكنه يقل قليلًا عن Claude في توليد الشيفرة النصية الصرفة، كما أن تعبيره باللغة الصينية ليس بسلاسة النماذج الصينية.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">بند المقارنة</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GPT-5.6</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Claude Fable 5</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Gemini 3.1 Pro</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الدرجة الإجمالية</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">94.8</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">95.0</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">92.1</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">القدرة البرمجية (SWE-bench)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">74.9%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">64.3% (Pro)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">متوسط</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">نافذة السياق</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1.05 مليون توكن</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مليون توكن</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مليونا توكن</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">قدرات تعدد الوسائط</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">متوازنة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">أضعف نسبيًا</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الأقوى</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">معدل الهلوسة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">منخفض نسبيًا</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الأدنى (نحو 1%)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">منخفض نسبيًا</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الإتاحة داخل الصين</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تتطلب شبكة خاصة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تتطلب شبكة خاصة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تتطلب شبكة خاصة</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">منظومة API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الأكثر اكتمالًا</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">في طور النمو</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مرتبط بمنظومة Google</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
مقارنة أفقية بين النماذج الدولية الثلاثة الكبرى (أغسطس 2026)

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
تنبيه: العوائق الواقعية للاستخدام داخل الصين

{class="mt-1"}
بالنسبة للمطورين داخل الصين، يتمثل العائق الأساسي أمام GPT وClaude وGemini في الوصول عبر الشبكة. ورغم إمكانية استخدامها بشكل غير مباشر عبر وسطاء Azure أو منصات تجميع API وغيرها، فإن الاستقرار والامتثال أمران ينبغي تقييمهما بنفسك. وإذا كان مشروعك يفرض متطلبات صارمة لأمن البيانات، فننصح بالنظر أولًا في النماذج الصينية.
:::

#### ثانيًا: النماذج اللغوية الكبيرة الصينية الرائدة: ازدهار متعدد الألوان

تحولت النماذج اللغوية الكبيرة الصينية في 2026 من «طاردة» إلى «منافسة في الصف الأول»، بل حققت «الصدارة» في بعض المجالات. وعلى خلاف جدل «الغلاف الخارجي» في 2023، أصبحت النماذج الصينية الرائدة في 2026 منافسة للنماذج الدولية من الطراز الأول في الاستدلال المنطقي وتوليد الشيفرة وفهم اللغة الصينية، وقد تقلصت الفجوة إلى ما دون 5%. والأهم أن النماذج الصينية تتمتع بمزايا يصعب تعويضها في السيناريوهات الصينية والتكلفة والنشر المطابق للأنظمة.

##### 1. DeepSeek V4: ملك القيمة مقابل السعر

DeepSeek (شن دو تشيو سو) ظاهرة بارزة بين النماذج اللغوية الكبيرة الصينية. ففي مطلع 2025 صدمت DeepSeek-V3 السوق بتموضع «أرخص من GPT بعُشر السعر وبالقدرة نفسها»، وسمتها الأوساط الصناعية «خط الإسقاط للنماذج اللغوية العامة» — فما هو أرخص منها ليس بجودتها، وما هو أغلى منها لا يضاهي وفرة إمكانياتها. وبحلول أغسطس 2026 صدرت النسخة الرسمية DeepSeek V4-Pro: بنية MoE بـ 1.6 تريليون معامل مع تنشيط نحو 49 مليار منها، ودعم سياق بلا فقدان يبلغ مليون توكن، وتُعد قيمتها مقابل السعر في البرمجة على نطاق واسع القمة عالميًا.

قفزت قدرات الوكيل (Agent) في DeepSeek V4 قفزة كبيرة — إذ ارتفع معيار DeepSWE من 12.8 إلى 62.7 (+390%)، وNL2Repo من 38.5 إلى 61.5. وأضاف الـ API دعم البروتوكولين معًا: Responses API وAnthropic API، وهو متوافق الآن مع أدوات البرمجة الرئيسية مثل Codex وClaude Code. هذا يعني أنه يمكنك استخدام API الخاص بـ DeepSeek بدلًا من API الخاص بـ Claude داخل Claude Code — بانخفاض التكلفة أضعافًا وبخبرة شبه مطابقة.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الطراز</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الفئة</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الإدخال (لكل مليون توكن)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الإخراج (لكل مليون توكن)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">نافذة السياق</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek V4 Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">رائد للاستدلال</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3 يوانات (نحو 0.43 دولار أمريكي)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6 يوانات (نحو 0.87 دولار أمريكي)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مليون توكن</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek V4 Flash</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">خفيف وسريع</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">يوان واحد (نحو 0.14 دولار أمريكي)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">يوانان (نحو 0.28 دولار أمريكي)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مليون توكن</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
أسعار سلسلة DeepSeek V4 (أغسطس 2026، أسعار ترويجية)

مقارنة الأسعار: مقابل مليون توكن إدخال + مليون توكن إخراج، تنفق DeepSeek V4 Flash نحو 0.42 دولار، وGPT-5.6 Sol نحو 35 دولارًا، وClaude Fable 5 نحو 60 دولارًا. فارق يصل إلى 80-140 ضعفًا.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
تحذير من الفخ: أسعار DeepSeek على وشك الارتفاع

{class="mt-1"}
أعلنت DeepSeek رسميًا في 6 أغسطس 2026 عن «خطط لرفع أسعار API بشكل كبير قريبًا»، وقد لا تدوم الأسعار الترويجية طويلًا. وتشير شائعات في بعض وسائل الإعلام إلى أن الارتفاع قد يبلغ 30 ضعفًا، وحتى 14 أغسطس لم تعلن الشركة بعد عن خطة التسعير النهائية. فضلًا عن أن النسخة الرسمية من DeepSeek V4 أدخلت آلية تسعير حسب الذروة — إذ يتضاعف سعر الاستدعاء مباشرة في أوقات الذروة. ننصح بمتابعة الإعلانات الرسمية للحصول على أحدث الأسعار.
:::

##### 2. Qwen3.7 Max من تونغ يي تشيون وِن: الخيار المؤسسي من Alibaba Cloud

تعتمد سلسلة تونغ يي تشيون وِن (Qwen) من Alibaba Cloud على منظومة Alibaba Cloud، فتتمتع بميزة فطرية في النشر على مستوى المؤسسات. ونموذج Qwen3.7 Max الصادر في يوليو 2026 هو الرائد الحالي: نموذج كثيف بـ 235 مليار معامل، وسياق أصلي يبلغ 256K قابل للتوسيع حتى مليون. وتكمن المزايا الجوهرية لـ Qwen في: نضج منظومته مفتوحة المصدر (سلسلة كاملة مفتوحة المصدر من 7B إلى 235B)، ودقته في فهم السيناريوهات الصينية، وتكامله العميق مع بنية Alibaba Cloud التحتية.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الطراز</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">سعر الإخراج (لكل مليون توكن)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">السيناريوهات المناسبة</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen-turbo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">0.6 يوان</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">أسئلة وأجوبة مبسطة، وتصنيف نصوص، وتزامن عالٍ</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen-long</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.0 يوان</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">معالجة سياق فائق الطول يبلغ 10 ملايين توكن</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen3.7-flash</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">7.2 يوان</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">المحادثات العامة وتوليد المحتوى</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen3.7-plus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">12.0 يوانًا</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تعدد الوسائط (صور + فيديو)، والإبداع باللغة الصينية</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen3.7-max</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">36.0 يوانًا</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">القدرات الصينية الرائدة، والمهام المعقدة</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
التسعير المتدرج لسلسلة Qwen من تونغ يي تشيون وِن (أغسطس 2026)

يعتمد تسعير Qwen استراتيجية متدرجة — من qwen-turbo منخفض التكلفة جدًا (إخراج 0.6 يوان لكل مليون توكن) إلى الرائد qwen3.7-max (إخراج 36 يوانًا لكل مليون توكن)، ليغطي احتياجات جميع السيناريوهات من الأسئلة الخفيفة إلى الاستدلال المعقد. وبالنسبة للشركات التي تستخدم Alibaba Cloud بالفعل، يُعد Qwen خيار التكامل الأسهل.

##### 3. GLM-5.1 من Zhipu: الأول بين النماذج الصينية في SWE-bench

تألقت سلسلة GLM من Zhipu AI في 2026. إذ حقق GLM-5.1 المركز الأول بين النماذج الصينية في SWE-bench: بنية هجينة MoE بـ 744 مليار معامل، ودعم سياق يبلغ مليون توكن. ويتميز بفهمه الدقيق للدلالات الصينية، ودعمه للنشر الخاص المطابق للأنظمة داخل الصين — وهو أمر بالغ الأهمية لسيناريوهات التمويل والحكومة ذات المتطلبات الصارمة لأمن البيانات. أما تسعير GLM-5.1 فهو 6 يوانات للإدخال و24 يوانًا للإخراج لكل مليون توكن، وهو في المستوى المتوسط بين النماذج الصينية.

##### 4. Kimi K3: ملك النصوص فائقة الطول

تشتهر سلسلة Kimi من شركة Moonshot AI بقدرتها على معالجة النصوص فائقة الطول. ونموذج Kimi K3 الصادر في يوليو 2026 يبلغ حجمه 2.8 تريليون معامل، ودخل الصف الأول عالميًا في تقييمات مهام معقدة متعددة. والسيناريو الجوهري لـ Kimi هو تحليل مكتبات الشيفرة الطويلة والاسترجاع المعزز للمستندات الطويلة — فهو يستطيع معالجة نص كتاب كامل أو شيفرة مشروع بأكمله، ويقدم أداءً متميزًا في مهام الاسترجاع من نوع «إبرة في كومة قش». وتسعيرة Kimi مرتفعة نسبيًا (نحو 12-20 يوانًا للإخراج لكل مليون توكن)، لكن لا أحد يضاهي قيمته مقابل السعر في سيناريوهات النصوص الطويلة.

##### 5. دو باو Doubao: اللاعب الشامل من ByteDance

قدمت سلسلة دو باو (Doubao) من ByteDance أداءً مستقرًا في 2026. ونموذج Doubao Seed 2.1 Pro هو النموذج الرائد من Volcano Engine بسياق 256K، ويقدم أداءً إجماليًا مستقرًا في الاختبارات الفعلية مع تجربة بارزة في السيناريوهات الصينية. وتكمن مزايا دو باو في: توكنات مجانية كبيرة تُمنح فور التسجيل، وتكامل مكتمل مع منظومة Volcano Engine، وتسعير في أحد أدنى المستويات داخل الصين. وللمبتدئين الراغبين في تجربة البرمجة بالذكاء الاصطناعي سريعًا، يُعد دو باو خيارًا للبدء دون أي عتبة.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">بند المقارنة</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">DeepSeek V4</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Qwen3.7 Max</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GLM-5.1</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kimi K3</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">دو باو 2.1 Pro</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الدرجة الإجمالية</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">87.5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">89.7</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">90.5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">88+</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">85+</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">القدرة البرمجية</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">قوية للغاية</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">قوي</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الأول بين النماذج الصينية في SWE</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">قوي</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">فوق المتوسط</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">فهم اللغة الصينية</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ممتاز</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ممتاز</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">دقيق</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ممتاز</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ممتاز</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">نافذة السياق</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مليون</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256K-1M</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مليون</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">فائق الطول</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256K</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">سعر الإخراج (يوان/مليون)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">36</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">24</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">12-20</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">30</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مفتوح المصدر</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">رخصة MIT</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">السلسلة كلها مفتوحة المصدر</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مفتوح المصدر جزئيًا</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مغلق المصدر</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مغلق المصدر</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">النشر الخاص</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مدعوم</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مدعوم</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مدعوم</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">غير مدعوم</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">غير مدعوم</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
مقارنة أفقية بين النماذج الصينية الخمسة الكبرى (أغسطس 2026)

أحد الاتجاهات المهمة هو أن «الإحساس بفجوة الأجيال» بين النماذج الصينية وGPT/Claude قد زال. ففي الاستدلال المنطقي ومسابقات الرياضيات، يبقى الفارق بين النماذج الصينية الرائدة وGPT-5 في خانة الأرقام المفردة غالبًا. وفي التفكير المعماري المنهجي والاستدلال الهندسي المعقد، لا يزال Claude متقدمًا — إذ يقدم حلولًا معمارية أكثر «روحًا وإبداعًا»، بينما تبدو النماذج الصينية أحيانًا «جمادة تتبع القوالب». لكن في السيناريوهات الصينية وضبط التكلفة والنشر المطابق للأنظمة، تتمتع النماذج الصينية بأفضلية ساحقة.

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="620" height="290" viewBox="0 0 620 290" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="620" height="290" fill="#ffffff" rx="8"/>
      <line x1="70" y1="230" x2="590" y2="230" stroke="#9ca3af" stroke-width="1.5"/>
      <line x1="70" y1="230" x2="70" y2="20" stroke="#9ca3af" stroke-width="1.5"/>
      <line x1="70" y1="60" x2="590" y2="60" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="70" y1="116" x2="590" y2="116" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="70" y1="173" x2="590" y2="173" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="4,4"/>
      <text x="62" y="234" font-size="10" fill="#6b7280" text-anchor="end">0</text>
      <text x="62" y="120" font-size="10" fill="#6b7280" text-anchor="end">50</text>
      <text x="62" y="64" font-size="10" fill="#6b7280" text-anchor="end">100</text>
      <text x="340" y="262" font-size="10.5" fill="#374151" text-anchor="middle">سعر المخرجات (يوان/مليون رمز)</text>
      <!-- bars: price -->
      <rect x="95" y="218" width="60" height="12" fill="#4f46e5"/><text x="125" y="212" font-size="9" fill="#374151" text-anchor="middle">6</text><text x="125" y="248" font-size="9.5" fill="#374151" text-anchor="middle">DeepSeek</text>
      <rect x="195" y="146" width="60" height="84" fill="#4f46e5"/><text x="225" y="140" font-size="9" fill="#374151" text-anchor="middle">36</text><text x="225" y="248" font-size="9.5" fill="#374151" text-anchor="middle">Qwen</text>
      <rect x="295" y="182" width="60" height="48" fill="#4f46e5"/><text x="325" y="176" font-size="9" fill="#374151" text-anchor="middle">24</text><text x="325" y="248" font-size="9.5" fill="#374151" text-anchor="middle">GLM</text>
      <rect x="395" y="200" width="60" height="30" fill="#4f46e5"/><text x="425" y="194" font-size="9" fill="#374151" text-anchor="middle">16</text><text x="425" y="248" font-size="9.5" fill="#374151" text-anchor="middle">Kimi</text>
      <rect x="495" y="170" width="60" height="60" fill="#4f46e5"/><text x="525" y="164" font-size="9" fill="#374151" text-anchor="middle">30</text><text x="525" y="248" font-size="9.5" fill="#374151" text-anchor="middle">Doubao</text>
      <!-- scores -->
      <circle cx="125" cy="118" r="5" fill="#d4a017"/><text x="140" y="114" font-size="9" fill="#78350f">87.5</text>
      <circle cx="225" cy="110" r="5" fill="#d4a017"/><text x="240" y="106" font-size="9" fill="#78350f">89.7</text>
      <circle cx="325" cy="105" r="5" fill="#d4a017"/><text x="340" y="101" font-size="9" fill="#78350f">90.5</text>
      <circle cx="425" cy="112" r="5" fill="#d4a017"/><text x="440" y="108" font-size="9" fill="#78350f">88+</text>
      <circle cx="525" cy="116" r="5" fill="#d4a017"/><text x="540" y="112" font-size="9" fill="#78350f">85+</text>
      <rect x="90" y="30" width="12" height="12" fill="#4f46e5"/><text x="108" y="41" font-size="9.5" fill="#374151">سعر المخرجات (كلما انخفض كان أفضل)</text>
      <circle cx="170" cy="36" r="5" fill="#d4a017"/><text x="182" y="40" font-size="9.5" fill="#374151">النتيجة الإجمالية (كلما ارتفع كان أفضل)</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
الشكل 4: مقارنة الأسعار والأداء بين النماذج الخمسة (كلما انخفض السعر كان أفضل، وكلما ارتفعت الدرجة كان أفضل)
:::

#### ثالثًا: إطار اتخاذ قرار اختيار النموذج

بعد التعرف على خصائص كل نموذج، كيف تختار النموذج المناسب لمشروعك؟ نقدم لك هنا «طريقة الأسئلة الأربعة لاتخاذ القرار» — أجب عن أربعة أسئلة فتحدد النموذج الأنسب لك.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-globe mr-1"></i> هل مشروعك يُنشر داخل الصين أم دوليًا؟</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">داخل الصين → اختر نماذج محلية</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">دوليًا → يمكن اختيار نماذج أجنبية</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-laptop-code mr-1"></i> هل المهمة الأساسية برمجة أم شيء آخر؟</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">برمجة → Claude أو DeepSeek</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">شيء آخر → تابع التقييم</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-book mr-1"></i> تحتاج سياقًا طويلًا جدًا (&gt;500 ألف رمز)؟</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">نعم → Gemini أو Kimi</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">لا حاجة → تابع التقييم</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-coins mr-1"></i> هل الميزانية ضيقة؟</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">ضيقة → DeepSeek أو Qwen-turbo</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">ليست ضيقة → GPT-5.6 أو Claude</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
الشكل 5: طريقة الأسئلة الأربعة لاختيار النموذج اللغوي الكبير
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
نصيحة: استراتيجية الدمج

{class="mt-1"}
هذه الطريقة ليست قاعدة جامدة — فكثير من السيناريوهات تتطلب استخدام عدة نماذج مجتمعة. ومن استراتيجيات الدمج الشائعة: استخدام DeepSeek أو Qwen للتطوير اليومي (تكلفة منخفضة وكفاءة في الصينية)، وClaude لتصميم البنية الحاسمة (استدلال قوي وهلوسة منخفضة)، وGemini لتحليل الوسائط المتعددة (معالجة الصور والفيديو). بدِّل النموذج حسب الحاجة بدلًا من «الاستمرار بنموذج واحد إلى الأبد».
:::

#### رابعًا: مدخل إلى استدعاء API: ربط النماذج اللغوية الكبيرة من الصفر

كثير من دروس البرمجة بالذكاء الاصطناعي تكتفي بتعليمك استخدام واجهة المحادثة، لكن «البرمجة بالذكاء الاصطناعي» الحقيقية — أي جعل تطبيقك يستدعي النموذج اللغوي الكبير — تتم عبر API. فالـ API (Application Programming Interface، واجهة برمجة التطبيقات) هي بروتوكول اتصال بين البرامج. وعبر API يمكن لشيفرة أن تستدعي قدرات النموذج اللغوي الكبير كما تستدعي دالة.

##### 1. ما هو التوكن (Token)

قبل التعرف على API، لا بد أولًا من فهم مفهوم «التوكن» (Token). التوكن هي وحدة الحساب الأساسية في النماذج اللغوية الكبيرة، ويمكن اعتبارها «وحدة القراءة والكتابة لدى الذكاء الاصطناعي». التوكن الواحد يقابل تقريبًا: 0.75 كلمة إنجليزية (4 محارف)، أو 0.5-1 حرف صيني. ونص صيني من 1000 حرف يستهلك نحو 1500-2000 توكن.

التوكن ليس عدد الكلمات ولا عدد المحارف. تستخدم النماذج اللغوية الكبيرة مُقسِّمًا للكلمات (Tokenizer) متخصصًا لتقطيع النص إلى توكنات. وقد يختلف عدد توكنات الكلمة الواحدة بين نموذج وآخر — فمثلًا قد تكون كلمة «الذكاء الاصطناعي» بالصينية 3 توكنات في GPT وتوكنين في DeepSeek. وتعيد API معظم النماذج عدد التوكنات المستهلكة فعليًا، ويمكنك الاطلاع عليه في استجابة الـ API.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
تقدير سريع لتكلفة التوكنات

{class="mt-1"}
مليون حرف صيني يقابل نحو 1.5 مليون توكن. بمعالجة مليون حرف إدخال + مليون حرف إخراج باستخدام DeepSeek V4 Flash تبلغ التكلفة نحو 0.42 دولار (نحو 3 يوانات)، وباستخدام Claude Fable 5 للكمية نفسها تبلغ نحو 60 دولارًا (نحو 434 يوانًا). لهذا فإن اختيار النموذج يؤثر مباشرة في تكلفة مشروعك.
:::

##### 2. الحصول على مفتاح API

الخطوة الأولى لاستخدام API النماذج اللغوية الكبيرة هي الحصول على مفتاح API — سلسلة رموز تُستخدم للتحقق من الهوية. ولكل مزود نموذج منصته الخاصة لـ API، وتحتاج إلى تسجيل حساب وإنشاء المفتاح. وإليك بوابات منصات API للنماذج الرئيسية وخطوات الحصول عليها:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">النموذج</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">منصة API</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">خطوات الحصول</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الحصة المجانية</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">platform.deepseek.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">التسجيل ← التحقق من الهوية ← إنشاء مفتاح API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">حصة تُمنح للمستخدمين الجدد</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تونغ يي تشيون وِن (Qwen)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">bailian.aliyun.com (منصة Bailian)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تسجيل الدخول بحساب Alibaba Cloud ← تفعيل الخدمة ← إنشاء المفتاح</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تجربة مجانية للمستخدمين الجدد</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Zhipu GLM</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">open.bigmodel.cn</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">التسجيل ← التحقق من الهوية ← إنشاء مفتاح API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">حصة تُمنح للمستخدمين الجدد</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kimi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">platform.moonshot.cn</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">التسجيل ← التحقق من الهوية ← إنشاء مفتاح API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">حصة مجانية محدودة</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">دو باو (Doubao)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">volcengine.com (Volcano Engine)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">التسجيل ← تفعيل خدمة Ark ← إنشاء مفتاح API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">توكنات مجانية كثيرة عند التسجيل</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenAI GPT</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">platform.openai.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">التسجيل ← ربط بطاقة ائتمانية ← إنشاء مفتاح API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">لا حصة مجانية (يتطلب الدفع)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Anthropic Claude</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">console.anthropic.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">التسجيل ← ربط البطاقة ← إنشاء مفتاح API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">حصة صغيرة للمستخدمين الجدد</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
منصات API للنماذج الرئيسية وطرق الحصول على المفتاح (أغسطس 2026)

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
تنبيه أمني: مفتاح API = كلمة مرور محفظتك

{class="mt-1"}
مفتاح API يعادل كلمة مرور محفظتك — فأي شخص يحصل على المفتاح يستطيع استدعاء النموذج على حساب حصتك. لذلك: لا تكتب مفتاح API أبدًا داخل الشيفرة (أدره عبر متغيرات البيئة)؛ ولا ترفع شيفرة تحتوي المفتاح إلى مستودع Git عام أبدًا؛ ولا تشارك لقطات شاشة تظهر المفتاح على وسائل التواصل الاجتماعي أبدًا. وإذا تسرب المفتاح فاحذفه فورًا على المنصة وأنشئ مفتاحًا جديدًا.
:::

##### 3. أول استدعاء لـ API

بعد الحصول على مفتاح API، يمكنك استدعاء API النماذج اللغوية الكبيرة بأي لغة برمجة. وفيما يلي مثال بأبسط استدعاء ممكن باستخدام Python — إرسال رسالة إلى DeepSeek والحصول على الرد.

::: div .code-block
:::inline div .code-head
<span>PYTHON · أول استدعاء API</span><span class="dots">···</span>
:::

```
# تثبيت الـ SDK: pip install openai
# DeepSeek متوافق مع صيغة OpenAI SDK، يمكن استخدامه مباشرة
from openai import OpenAI
import os

# 1. إنشاء العميل (يُقرأ مفتاح API من متغير البيئة)
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 2. إرسال الطلب
response = client.chat.completions.create(
    model="deepseek-chat",  # تحديد النموذج
    messages=[
        {"role": "system", "content": "أنت مساعد برمجة بلغة بايثون."},
        {"role": "user", "content": "اكتب دالة ترتيب سريع."}
    ]
)

# 3. الحصول على الرد
print(response.choices[0].message.content)

# 4. عرض استهلاك الرموز
print(f"رموز الإدخال: {response.usage.prompt_tokens}")
print(f"رموز المخرجات: {response.usage.completion_tokens}")
print(f"إجمالي الرموز: {response.usage.total_tokens}")
```
:::

المنطق الجوهري لهذه الشيفرة هو: إنشاء العميل (مع مفتاح API وعنوان النموذج) ← بناء قائمة الرسائل (system يحدد الدور، وuser هو مدخل المستخدم) ← إرسال الطلب ← الحصول على الرد. هذا النمط يصلح تقريبًا لكل النماذج المتوافقة مع صيغة OpenAI — يكفي تغيير api_key وbase_url لتبديل النموذج. ولهذا تختار كثير من النماذج الصينية التوافق مع صيغة OpenAI SDK: يستطيع المطور تبديل النموذج بتغيير سطرين فقط، فتكون تكلفة الانتقال بالغة الانخفاض.

فيما يلي فروق الشيفرة عند التبديل إلى نماذج أخرى — لاحظ أن التغيير لا يتجاوز سطرين:

::: div .code-block
:::inline div .code-head
<span>PYTHON · تبديل النموذج يتطلب سطرين فقط</span><span class="dots">···</span>
:::

```
# DeepSeek
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
# model="deepseek-chat"

# Qwen (منصة Bailian)
client = OpenAI(
    api_key=os.environ.get("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
# model="qwen-plus"

# GLM من Zhipu
client = OpenAI(
    api_key=os.environ.get("GLM_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4"
)
# model="glm-4"

# OpenAI GPT
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    # يكفي base_url الافتراضي
)
# model="gpt-5.6-terra"
```
:::

##### 4. معالجة الاستجابة المتدفقة

في التطبيقات الفعلية، لن ترغب عادةً في الانتظار حتى يكتب الذكاء الاصطناعي كل المحتوى قبل عرضه دفعة واحدة — فهذا يجعل المستخدم ينتظر طويلًا. وتتيح لك الاستجابة المتدفقة (Streaming) عرض النص حرفًا بحرف أثناء توليده من الذكاء الاصطناعي، مما يحسّن تجربة المستخدم بشكل كبير. فمثل الآلة الكاتبة، تظهر الحروف واحدة تلو الأخرى، وشعور المستخدم يختلف تمامًا.

::: div .code-block
:::inline div .code-head
<span>PYTHON · استجابة متدفقة</span><span class="dots">···</span>
:::

```
# استجابة متدفقة: إخراج كلمة بكلمة
stream = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "اكتب درسًا عن خوارزمية الترتيب الفقاعي في بايثون"}
    ],
    stream=True  # تفعيل البث المتدفق
)

# استلام وطباعة على شكل كتل
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)
# سيظهر الناتج حرفًا حرفًا مثل آلة كاتبة
```
:::

#### خامسًا: دليل شراء باقات التوكنات (Token Plan)

تقدم معظم مزودي النماذج طريقتين للحساب: الدفع حسب الاستعمال (Pay-as-you-go) والاشتراك بالباقات (Token Plan / Subscription). وفهم الفرق بين الطريقتين يمكن أن يساعدك على خفض تكلفة الاستخدام بشكل كبير.

##### 1. الدفع حسب الاستعمال مقابل الاشتراك بالباقات

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">البعد</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الدفع حسب الاستعمال (Pay-as-you-go)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الاشتراك بالباقات (Subscription)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">طريقة الحساب</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تدفع مقابل التوكنات التي تستخدمها</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تدفع مبلغًا ثابتًا مسبقًا مقابل حصة</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">السيناريوهات المناسبة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">استخدام غير مستقر أو استدعاءات متقطعة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">استخدام مستقر واستدعاءات كثيفة</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الميزة السعرية</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">السعر القياسي</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">أقل من الدفع حسب الاستعمال بنسبة 20%-50%</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">المرونة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">متاح في أي وقت دون أي التزام</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تتطلب دفعًا مسبقًا، وقد تنتهي صلاحية الحصة غير المستخدمة</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">معالجة تجاوز الحصة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تحويل تلقائي إلى الدفع حسب الاستعمال</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">بعد تجاوز الحصة يتحول إلى الدفع حسب الاستعمال</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">المنصات الممثلة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">منصات API الرسمية لكل نموذج</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenAI Plus/Pro, Claude Pro, Cursor Pro</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
مقارنة بين طريقتي الحساب

للمبتدئين، ننصح بالبدء بالدفع حسب الاستعمال — فلا حاجة إلى دفع مسبق، وتدفع ما تستخدمه فقط. وحين يستقر استهلاكك الشهري عند مستوى معين (مثلًا تجاوز 50 يوانًا شهريًا)، فكّر حينها في الانتقال إلى الاشتراك بالباقات للحصول على سعر وحدة أقل.

##### 2. نظرة على باقات الاشتراك الرئيسية

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الباقة</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الرسوم الشهرية</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">المحتوى المشمول</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الفئة المناسبة</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ChatGPT Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مجانًا</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">دردشة نصية غير محدودة بنموذج GPT-5.6 Luna</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تجربة للمبتدئين تمامًا</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ChatGPT Plus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">20 دولارًا أمريكيًا/شهريًا</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Sol، وتوليد الصور، وتحليل البيانات، والوصول إلى الإضافات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">المستخدمون متوسطو الاستخدام</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ChatGPT Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">200 دولار أمريكي/شهريًا</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">استخدام غير محدود لجميع النماذج، وأولوية الوصول إلى الميزات الجديدة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">المستخدمون المحترفون كثيفو الاستخدام</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مجانًا</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">عدد محدود من محادثات Claude</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تجربة للمبتدئين تمامًا</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">20 دولارًا أمريكيًا/شهريًا</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">استخدام غير محدود لـ Claude، وأولوية الوصول إلى النماذج الجديدة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مطورو البرمجة</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مجانًا</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">عدد محدود من إكمالات الذكاء الاصطناعي والمحادثات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تجربة للمبتدئين</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">20 دولارًا أمريكيًا/شهريًا</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">إكمال ذكاء اصطناعي غير محدود، و500 طلب متقدم شهريًا</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">المطورون في الاستخدام اليومي</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor Business</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">40 دولارًا أمريكيًا/شهريًا/للفرد</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تعاون الفريق، ولوحة الإدارة، ووضع الخصوصية</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الفرق والاستخدام الجماعي</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
باقات الاشتراك لأدوات الذكاء الاصطناعي الرئيسية (أغسطس 2026)

تختلف خطط الاشتراك للنماذج الصينية قليلًا. فـ DeepSeek تعتمد أساسًا على الدفع حسب الاستعمال ولا تقدم باقات اشتراك شهرية — تُحمل رصيدًا ثم يُخصم وفق الاستهلاك الفعلي. وتقدم تونغ يي تشيون وِن حزم موارد مدفوعة مسبقًا على منصة Bailian (شراء كمية محددة من التوكنات بسعر مخفض). ولدى دو باو أيضًا خطط مدفوعة مسبقًا مشابهة على Volcano Engine. وبالنسبة للمطورين داخل الصين، فإن التوليفة الأكثر اقتصادية عادة هي: الدفع حسب الاستعمال لدى DeepSeek (للتطوير اليومي) + الحصة المجانية من دو باو (للتجربة والاختبار).

##### 3. منصات تجميع API

إذا احتجت إلى استخدام عدة نماذج في آن واحد، فمنصات تجميع API خيار مريح. تقدم منصة التجميع مفتاح API واحدًا موحدًا تستطيع به استدعاء عشرات النماذج حول العالم دون الحاجة إلى التسجيل في كل منصة على حدة.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">المنصة</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الخصائص</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الميزة السعرية</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">السيناريوهات المناسبة</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenRouter (openrouter.ai)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">منصة تجميع خارجية، بمفتاح واحد تستدعي نماذج العالم</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">أسعار شفافة مع مقارنة فورية للأسعار</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">لمن يحتاج إلى التبديل المرن بين عدة نماذج أجنبية</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SiliconFlow (siliconflow.cn)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">منصة تجميع صينية توفر واجهات API لنماذج صينية متعددة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">أقل من الأسعار الرسمية بنسبة 20%-30%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مطورون داخل الصين، ومقارنة أسعار بين عدة نماذج</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Azure OpenAI (وكيل Microsoft)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">واجهة OpenAI API عبر وكيل Microsoft Azure</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">خصم 50% مع Batch API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">استدعاءات OpenAI على مستوى المؤسسات، للمهام الدفعية غير المتزامنة الكبيرة</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Baidu Qianfan (qianfan.baidubce.com)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">منصة بايدو السحابية للذكاء الاصطناعي، توفر نماذج مثل ERNIE</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">رصيد مجاني هدية للمستخدمين الجدد</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">مستخدمو منظومة بايدو</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
أبرز منصات تجميع واجهات API (أغسطس 2026)

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
تنبيه من الفخ: لا تشترِ "مفاتيح مشتركة"

{class="mt-1"}
لا تشترِ ما يُعرف بـ"مفاتيح API المشتركة" من منصات مثل Taobao أو Xianyu — فهذه المفاتيح مجهولة المصدر غالباً، وقد يُحظر حسابها في أي لحظة، إضافة إلى مخاطر تسرب البيانات. احصل على مفاتيح API دائماً من المنصات الرسمية أو منصات التجميع النظامية.
:::

##### 4. استراتيجيات تحسين التكلفة

اختيار النموذج المناسب هو الخطوة الأولى فقط، و"كيف تستخدمه بتكلفة أقل" لا تقل أهمية. إليك عدة استراتيجيات لتحسين التكلفة أثبتت جدواها عملياً:

1. استفد جيداً من إصابة التخزين المؤقت. توفر نماذج كثيرة ميزة "التخزين المؤقت" (Cache) — حين يتضمن طلبك محتوى سبقت معالجته (مثل موجه النظام)، يُحتسب هذا الجزء بسعر منخفض جداً. سعر إصابة التخزين المؤقت لدى DeepSeek لا يزيد عن 1/60 من السعر العادي. ضع موجه النظام الثابت في بداية قائمة الرسائل لتعظيم نسبة إصابة التخزين المؤقت.
2. التوجيه المتدرج — استخدم النموذج الرخيص للمهام البسيطة والنموذج الغالي للمهام المعقدة. مثلاً استخدم DeepSeek V4 Flash لتصنيف النصوص (المخرجات بسعر 2 يوان لكل مليون Token)، واستخدم Claude لتصميم البنية (المخرجات بسعر 181 يواناً لكل مليون Token). نحو 80% من استدعاءات المشروع الواحد يمكن إنجازها بالنماذج الرخيصة.
3. حدد طول المخرجات. تُحتسب واجهات API حسب Token المخرجات، وكلما طالت المخرجات ارتفعت التكلفة. في الحالات التي لا تحتاج فيها إلى إسهاب، اضبط معامل max_tokens لتحديد طول المخرجات وتجنب "إسهاب الذكاء الاصطناعي".
4. استخدم Batch API للمهام غير الفورية. إذا كانت لديك مهام كثيرة لا تتطلب استجابة فورية (مثل وسم البيانات الدفعي أو تلخيص المستندات)، فإن استخدام Batch API يمنحك خصماً بنسبة 50%. توفر OpenAI وAzure هذه الميزة معاً.
5. راقب استهلاك Token. توفر معظم منصات API لوحة إحصاءات للاستخدام. راجع توزيع الاستهلاك دورياً وحدد الاستدعاءات الأكثر استهلاكاً للـToken لتحسينها بشكل موجه. تعديل صغير في الموجه (مثل تغيير "اشرح بالتفصيل" إلى "اشرح في 3 جمل") قد يوفر 50% من الـToken.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">استراتيجية التحسين</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">نسبة التوفير</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">صعوبة التنفيذ</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الوصف</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">إصابة التخزين المؤقت</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تصل إلى 98%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">منخفض</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ضع المحتوى الثابت في بداية الرسائل</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">التوجيه المتدرج</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">50%-80%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">متوسط</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">استخدم النموذج الرخيص للمهام البسيطة</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تحديد طول المخرجات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">30%-60%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">منخفض</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">اضبط معامل max_tokens</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Batch API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">50%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">منخفض</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">استخدم المعالجة الدفعية للمهام غير الفورية</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تحسين الموجهات (Prompt)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">20%-50%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">متوسط</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">اختصر الموجه وقلل الحشو</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
استراتيجيات تحسين التكلفة ونتائجها (أغسطس 2026)

#### سادساً: تطبيق عملي — دمج واجهة النموذج الكبير API في مشروعك

لنختم هذا الفصل بتطبيق عملي متكامل — إنشاء "مولد ملخصات بالذكاء الاصطناعي": يدخل المستخدم نصاً طويلاً، فيستدعي التطبيق واجهة النموذج الكبير API لتوليد الملخص. سيعرض هذا التطبيق الدورة الكاملة لاستدعاء API: إعداد البيئة، الاستدعاء، معالجة الأخطاء، والتحكم في التكلفة.

::: div .code-block
:::inline div .code-head
<span>PYTHON · ai_summarizer.py</span><span class="dots">···</span>
:::

```
# ai_summarizer.py - مولّد ملخصات بالذكاء الاصطناعي
import os
from openai import OpenAI

# 1. الإعداد (يُقرأ مفتاح API من متغير البيئة، ولا يُكتب في الكود أبدًا)
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def summarize(text: str, max_length: int = 200) -> dict:
    """يولّد ملخصًا للنص

    Args:
        text: النص الأصلي المراد تلخيصه
        max_length: الطول الأقصى للملخص (عدد الرموز)

    Returns:
        dict: يتضمن الملخص ومعلومات استهلاك الرموز
    """
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "system",
                    "content": "أنت مولّد ملخصات."
                               "لخص نص المستخدم بلغة واضحة وموجزة."
                               "الملخص لا يتجاوز 3 جمل."
                },
                {
                    "role": "user",
                    "content": f"لخص النص التالي:\n\n{text}"
                }
            ],
            max_tokens=max_length,  # يحدد طول المخرجات
            temperature=0.3  # حرارة منخفضة = أكثر استقرارًا
        )

        return {
            "success": True,
            "summary": response.choices[0].message.content,
            "input_tokens": response.usage.prompt_tokens,
            "output_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

# 2. مثال للاستخدام
if __name__ == "__main__":
    long_text = """
    (الصق نصًا طويلًا هنا...)
    """

    result = summarize(long_text)

    if result["success"]:
        print(f"الملخص: {result['summary']}")
        print(f"الرموز المستهلكة: {result['total_tokens']}")
        # تقدير التكلفة: DeepSeek V4 Flash
        cost = result['total_tokens'] * 0.000004  # ≈ 0.4 سنت لكل 1000 رمز
        print(f"التكلفة التقديرية: {cost:.4f} يوان")
    else:
        print(f"حدث خطأ: {result['error']}")
```
:::

يجسد هذا الكود عدة ممارسات مثلى لاستدعاء API: يُقرأ مفتاح API من متغيرات البيئة ولا يُكتب مطلقاً داخل الكود؛ للدالة توثيق واضح وتلميحات أنواع؛ ضُبط max_tokens لتحديد طول المخرجات؛ وعينت temperature على قيمة منخفضة (0.3) لمخرجات أكثر استقراراً؛ توجد معالجة أخطاء كاملة؛ وتُعاد معلومات استهلاك Token لتتبع التكلفة. وعندما تستعين بالذكاء الاصطناعي لكتابة هذا الكود، أبلغه بهذه المتطلبات — فهو قادر تماماً على تحقيقها لك.

:::inline div .quote-line
الخلاصة النهائية لهذا الفصل: النماذج "ذخيرة" والمنهجية "تكتيك". اختيار الذخيرة الصحيحة يجعل المعركة أسهل، لكن بدون تكتيك جيد لن تربح الحرب ولو كانت الذخيرة ممتازة. بعد أن تعرفت على خصائص كل نموذج وطريقة استخدام الـ API، أصبح لديك "مستودع ذخيرة" وافر، أما كيف تخوض المعركة فيعتمد على منهجية التفكير التي تعلمتها في الفصول السابقة.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
لنطبق عملياً: نفذ أول استدعاء API لك بنجاح

{class="mt-1"}
سجل في منصة نماذج صينية (نوصي بـ DeepSeek أو Zhipu، وكلاهما يمنح رصيداً للمستخدمين الجدد)، وأنشئ مفتاح API، واكتبه في متغيرات بيئة النظام (وليس في الكود!)، ثم شغل كود "أول استدعاء API" أعلاه. في اللحظة التي ترى فيها رد الذكاء الاصطناعي مطبوعاً أمامك، تكون قد اجتزت الخط الفاصل بين "استخدام الذكاء الاصطناعي" و"بناء تطبيقات الذكاء الاصطناعي".
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
خلاصة الفصل

- الثلاثي الدولي الكبير: GPT-5.6 (متوازن وشامل)، Claude (قمة البرمجة ونسبة هلوسة 1% فقط)، Gemini (ملك تعدد الوسائط وسياق يتسع لمليوني Token)
- الخماسي الصيني الكبير: DeepSeek V4 (ملك القيمة مقابل السعر، وانتبه لإعلانات رفع الأسعار)، Qwen3.7 (للمؤسسات)، GLM-5.1 (الأول محلياً في SWE)، Kimi K3 (النصوص فائقة الطول)، Doubao (مجاني للمبتدئين)
- طريقة القرار بالأسئلة الأربعة: أين النشر؟ برمجة أم غيرها؟ سياق فائق الطول؟ حساسية للميزانية؟
- Token وحدة الفوترة: الحرف الصيني الواحد يساوي نحو 1.5-2 Token، ومليون حرف صيني يساوي نحو 1.5 مليون Token
- مفتاح API = كلمة سر محفظتك: يُدار عبر متغيرات البيئة، ولا يُكتب في الكود مطلقاً ولا يُرفع إلى Git
- النماذج الصينية متوافقة عموماً مع OpenAI SDK: لتبديل النموذج يكفي تعديل سطرين هما api_key وbase_url
- خمس حيل للتوفير: إصابة التخزين المؤقت، التوجيه المتدرج، تحديد المخرجات، Batch API، مراقبة الاستهلاك
:::
