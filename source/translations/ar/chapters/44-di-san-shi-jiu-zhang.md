---
id: di-san-shi-jiu-zhang
num: 39
part: ai-biancheng-pian
nav: الفصل 39: هندسة السياق — اجعل الذكاء الاصطناعي يفهم قصدك
toc: default
kind: chapter
---

### الفصل 39: هندسة السياق — اجعل الذكاء الاصطناعي يفهم نيتك

{class="chapter-intro mb-4"}
هل جربت هذا الموقف: تفتح نافذة محادثة جديدة، وكأن الذكاء الاصطناعي أصيب بفقدان الذاكرة ونسي كل شيء عن مشروعك؟ ليس لأنه يتعمد إزعاجك، بل لأنه «سريع النسيان» بطبيعته. يعلمك هذا الفصل كيف تركّب له «نظام ذاكرة طويلة المدى»، وتتعرف على أحد أشهر نماذج التطوير في 2026 — التطوير المدفوع بالمواصفات.

#### أولاً: ملف ذاكرة المشروع: «الذاكرة طويلة المدى» للذكاء الاصطناعي

للنماذج الذكية قيد جوهري: ذاكرتها «قصيرة المدى». في بداية كل محادثة، لا يعرف الذكاء الاصطناعي شيئًا عن مشروعك. عليك إخباره باستمرار: «نستخدم React» و«الخادم الخلفي Node.js» و«قاعدة البيانات PostgreSQL» و«نمط الكود يستخدم علامتي اقتباس مزدوجتين». هذا غير فعال ويسهل فيه النسيان — كما لو كنت تعيد تدريب زميل جديد كل يوم.

الحل هو «ملف ذاكرة المشروع» — ملف نصي في جذر المشروع، تقرأه أدوات الذكاء الاصطناعي تلقائيًا عند بداية كل محادثة. لكل أداة تسميتها الخاصة:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الأداة</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">اسم الملف</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cursorrules</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">CLAUDE.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitHub Copilot</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">copilot-instructions.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الحل العام</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">AGENTS.md</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
تسميات ملفات ذاكرة المشروع لكل أداة

رغم اختلاف التسميات، المبدأ واحد: اكتب في هذا الملف المعلومات التي تريد أن «يتذكرها» الذكاء الاصطناعي دائمًا. ملف الذاكرة الجيد يشمل: نظرة عامة على المشروع (ما هو)، والمكدس التقني (ما التقنيات المستخدمة)، ومعايير الكود (التسمية والمسافة البادئة ونمط التعليقات)، وبنية المجلدات (كيف يُنظم الكود)، واتفاقيات التطوير (استراتيجية الفروع، وقواعد الإيداع، ومتطلبات الاختبار). ملف CLAUDE.md لـ Karpathy 70 سطرًا فقط، لكنه يغطي كل المعلومة المهمة — مختصر ومكتمل.

::: div .code-block
:::inline div .code-head
<span>CLAUDE.md</span><span class="dots">···</span>
:::

```
# المشروع: تطبيق لتتبع المصروفات الشخصية
## نظرة عامة
تطبيق متكامل (full-stack) لتتبع المصروفات الشخصية يساعد المستخدم على تسجيل الإيرادات والمصروفات اليومية.
## الحزمة التقنية
- الواجهة الأمامية: React + TypeScript + Tailwind CSS
- الواجهة الخلفية: Node.js + Express + TypeScript
- قاعدة البيانات: SQLite (تطوير) / PostgreSQL (إنتاج)
- الاختبارات: Vitest
## قواعد الكود
- استخدم علامات الاقتباس المزدوجة
- مسافة بادئة بمسافتين
- أسماء الدوال بصيغة camelCase
- تعريفات الأنواع بصيغة PascalCase
- كل دالة يجب أن تملك تعليق JSDoc
## هيكل المجلدات
/src
  /frontend  - كود الواجهة الأمامية
  /backend   - كود الواجهة الخلفية
  /shared    - الأنواع المشتركة بين الواجهتين
  /tests     - ملفات الاختبار
## اتفاقيات التطوير
- رسائل الـ commit بالعربية
- كل ميزة جديدة تبدأ باختبار أولًا
- ردود الـ API بصيغة موحدة { success, data, error }
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ملاحظة: لا تحوّله إلى «مستند متطلبات ثانٍ»

{class="mt-1"}
انتبه لطول الملف — لا تكتبه كعشرات الصفحات من مستند المتطلبات. الهدف هو «تمكين الذكاء الاصطناعي من بناء فهم سريع للخلفية»، وليس «وصف كل وظيفة بالتفصيل». أبقِه مختصرًا ومنظّمًا، واكتب فقط «ما يحتاجه الذكاء الاصطناعي معرفته».
:::

#### ثانيًا: التطوير المدفوع بالمواصفات (SDD)

التطوير المدفوع بالمواصفات (Spec-Driven Development، SDD) هو نموذج تطوير نضج تدريجيًا في 2026، وفكرته في جملة: اكتب المواصفات أولًا، ثم الكود. بخلاف TDD التقليدي (التطوير المدفوع بالاختبارات)، لا تقتصر «المواصفات» في SDD على حالات الاختبار، بل تشمل وصف المتطلبات وتعريفات الواجهات ونماذج البيانات. يولد الذكاء الاصطناعي الكود بناءً على هذه المواصفات، ودور الإنسان هو كتابتها وصيانتها.

سير عمل SDD في خمس خطوات:

1. صِف المتطلبات باللغة الطبيعية (في ملف .md)؛
2. حدد الواجهات وهياكل البيانات (في ملف المواصفات)؛
3. دع الذكاء الاصطناعي يولّد الكود وفقًا للمواصفات؛
4. شغّل الاختبارات للتحقق من مطابقة المخرجات للمواصفات؛
5. إذا لم تتطابق، عدّل المواصفات أو اطلب من الذكاء الاصطناعي تصحيح الكود.

في هذه العملية، ملف المواصفات هو «مصدر الحقيقة الوحيد» — يمكن إعادة توليد الكود، لكن المواصفات يجب أن تكون صحيحة أولًا.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> كتابة ملف المواصفات</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> هل المواصفات مكتملة؟</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> مكتملة</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> الذكاء الاصطناعي يولّد الكود وفق المواصفات</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> تشغيل الاختبارات للتحقق من الناتج</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> غير مكتملة / اختبارات لا تنجح</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-tools mr-1"></i> مشكلة في الكود → صحح الكود؛ مشكلة في المواصفات → صحح المواصفات</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> العودة إلى التحقق</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> كل الاختبارات ناجحة → تسليم</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
الشكل 3: سير عمل التطوير المدفوع بالمواصفات (SDD)
:::

تكمن ميزة SDD في أن ملف المواصفات أكثر استقرارًا من الشيفرة. فعندما تتغير النماذج الأساسية أو الأدوات، يبقى ملف المواصفات لديك صالحًا، ويكفي أن تطلب من أداة الذكاء الاصطناعي الجديدة إعادة توليد الشيفرة. ولهذا يؤكد هذا الكتاب على أن «المنهجية أهم من الأدوات» — فملف المواصفات هو التجسيد الملموس لمنهجيتك.

#### ثالثًا: إدارة نافذة السياق

حتى مع ملف ذاكرة المشروع، ستواجه مشكلة «نقص السياق» في المحادثات. نافذة سياق النموذج (كمية المعلومات التي يعالجها في وقت واحد) محدودة. عندما تطول المحادثة وتكثر الملفات المذكورة، «ينسى» الذكاء الاصطناعي المعلومات المبكرة، فتنخفض جودة المخرجات — كما لو دردشت مع صديق ست ساعات، فنسي أول ما قلته.

الاستراتيجية الأساسية لإدارة نافذة السياق هي «الاستشهاد المُصعَّد»:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">طبقة السياق</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">المحتوى</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">طريقة الإدارة</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الطبقة الأولى: ذاكرة المشروع</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">المكدس التقني، والمواصفات، وبنية المجلدات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">تُكتب في ملفات مثل CLAUDE.md، وتُحمَّل تلقائيًا دون تكرار</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الطبقة الثانية: استشهاد الملفات</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ملفات الكود المتعلقة بالمهمة الحالية</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">استشهد بدقة برمز @، ولا تلصق الملف كاملًا في المحادثة</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الطبقة الثالثة: سياق المحادثة</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">سجل محادثة المهمة الحالية</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">بعد إتمام مهمة، افتح محادثة جديدة لتجنب تضخم السياق</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الطبقة الرابعة: الأمر الفوري</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">متطلبات الخطوة الحالية</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">واضح ومختصر ومحدد، وتجنب الوصف المطول</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
استراتيجية الإدارة المُصعَّدة لنافذة السياق

#### رابعًا: نقاط عملية في هندسة السياق

هندسة السياق ليست إعدادًا يُجرى مرة واحدة، بل عملية تحسين مستمرة. وإليك بعض النقاط التي ثبتت فعاليتها مرارًا وتكرارًا في الممارسة:

1. حدِّث ملف الذاكرة بالتزامن مع تطور المشروع. فعند إدخال تقنية جديدة أو تغيير البنية، حدِّث ملف الذاكرة فورًا بدلًا من الشرح المؤقت داخل المحادثة.
2. أحسن استخدام الإحالة بـ @ بدلًا من لصق النص كاملًا. تدعم معظم أدوات البرمجة بالذكاء الاصطناعي صيغة @file أو @folder التي تُدخل محتوى الملف إلى سياق الذكاء الاصطناعي في الخلفية، وهي أكثر كفاءة من اللصق اليدوي ولا تُلوِّث المحادثة.
3. اجعل المحادثات «قصيرة ومركزة». كل محادثة تعالج مهمة واحدة أو نقطة وظيفية واحدة، وبعد الانتهاء افتح محادثة جديدة للمهمة التالية. فالمحادثات الطويلة لا تستهلك نافذة السياق فحسب، بل تُشتت تركيز الذكاء الاصطناعي أيضًا.
4. دَع الذكاء الاصطناعي «يرى» النتائج بدلًا من «وصفها» له. فعند مواجهة خطأ (bug)، أشر إلى سجل الأخطاء مباشرة بـ @ بدلًا من وصفه بكلماتك مثل «يبدو أن هناك خطأً ما». فرؤية الذكاء الاصطناعي للمعلومة الأصلية أنجع من رؤيته لروايتك عنها.
5. نظِّف والأرشف دوريًا. فالمحادثات المنتهية والملفات المؤقتة تشغل مساحة العمل. نظِّف المحتوى غير ذي الصلة بانتظام وحافظ على نظافة مجلد المشروع، فهذا يساعد الذكاء الاصطناعي أيضًا على فهم بنية المشروع بكفاءة أكبر.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
هيّا نطبق: اكتب لمشروعك ملف ذاكرة من 70 سطرًا

{class="mt-1"}
اختر مشروعًا تعمل عليه الآن (أو تنوي العمل عليه)، واكتب ملف CLAUDE.md يتضمن: نظرة عامة على المشروع (من جملتين إلى ثلاث)، والحزمة التقنية (اذكرها)، ومعايير الشيفرة (من 3 إلى 5 بنود)، وهيكل المجلدات (ارسمه شجرة)، واتفاقيات التطوير (من بندين إلى ثلاثة). ويُفضل ألا يتجاوز 70 سطرًا — وستجد بعد الانتهاء أن فهمك للمشروع صار أوضح بكثير.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
خلاصة الفصل

- ذاكرة الذكاء الاصطناعي «قصيرة المدى»: في كل محادثة جديدة تبدأ معرفته بالمشروع من الصفر
- ملف ذاكرة المشروع (مثل CLAUDE.md) هو «الذاكرة طويلة المدى» للذكاء الاصطناعي، ويُحمَّل تلقائيًا عند كل محادثة
- ملف الذاكرة الجيد = نظرة عامة + حزمة تقنية + معايير + هيكل المجلدات + اتفاقيات، و70 سطرًا تكفي
- التطوير الموجَّه بالمواصفات (SDD): اكتب المواصفات قبل الشيفرة، فالمواصفات هي «المصدر الوحيد للحقيقة» وهي أكثر استقرارًا من الشيفرة
- يُدار السياق في أربع طبقات: ذاكرة المشروع ← إحالة الملفات بـ @ ← سجل المحادثة ← التعليمات الفورية
- خمس نقاط عملية: التحديث المتزامن، والإحالة بـ @، والمحادثات القصيرة، وإعطاء المعلومة الأصلية، والتنظيف الدوري
:::
