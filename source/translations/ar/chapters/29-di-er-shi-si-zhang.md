---
id: di-er-shi-si-zhang
num: 24
part: chao-yue-pian
nav: الفصل 24: شرح معمق لصلاحيات Root وقفل BL
toc: default
kind: chapter
---

### الفصل 24: تحليل عميق لصلاحيات Root وقفل BL

{class="chapter-intro mb-4"}
ثانيًا: العملية التفصيلية لفك قفل BL (باستخدام شاومي كمثال)

#### أولًا: فهم متعمق لـ Bootloader

: تقدم بطلب فك القفل على موقع أداة فك القفل من شاومي.

##### ربط الحساب

- <strong>: اربط حساب شاومي في إعدادات الهاتف.</strong>فترة الانتظار
- <strong>: حسب مستوى الحساب، تحتاج للانتظار من 7 إلى 30 يومًا.</strong>عملية فك القفل
- <strong>: استخدم أداة فك القفل من شاومي للاتصال بالحاسوب وفك القفل.</strong>ثالثًا: حلول Root المتعددة

##### 🔐 التخزين والتحقق على مستوى العتاد

حالة قفل BL (Locked/Unlocked) والمفاتيح العامة للشركة، تُخزن عادة في منطقة عتاد محمية (مثل قسم devinfo في Qualcomm أو eFuse أو قسم RPMB)، لمنع العبث البرمجي. في كل إقلاع، يقرأ Bootloader الحالة من هذه المنطقة الآمنة، ويقرر بناءً عليها ما إذا كان سينفذ التحقق الصارم للتوقيع.

##### 🔏 التحقق من التوقيع الرقمي

عند إطلاق الشركة لتحديث النظام أو صورة، توقّعها بمفتاحها الخاص. عند إقلاع الجهاز، يستخدم Bootloader المفتاح العام المدمج للتحقق من صورة النظام (مثل boot.img وrecovery.img). طريقة عمله:

1. إعادة حساب قيمة التجزئة (hash) لصورة النظام.
2. فك تشفير التوقيع المدمج في الصورة بالمفتاح العام، للحصول على قيمة تجزئة.
3. مقارنة قيمتي التجزئة، إذا تطابقت اجتاز التحقق. هذا يضمن عدم العبث بصورة النظام من طرف ثالث.

##### 🔗 سلسلة الإقلاع الآمن

قفل BL هو الحلقة الأولى في سلسلة الإقلاع الآمن بأكملها. بعد اجتياز التحقق، يحمل وينفذ برنامج التمهيد للمرحلة التالية (مثل النواة)، مما يضمن طبقة تلو الأخرى موثوقية بيئة إقلاع النظام.

##### 📊 القفل مقابل الفتح: التأثير المزدوج لقفل BL

لفهم فوائد وعيوب قفل BL بشكل أكثر مباشرة، نستخدم جدول مقارنة لعرض الاختلافات في 5 أبعاد أساسية:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 dark:border-gray-600 text-sm">
                            <thead>
                                <tr class="bg-gray-100 dark:bg-gray-800">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">الدور الأساسي</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">حالة القفل (الافتراضية)</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">حالة ما بعد الفتح</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">أمان النظام</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">منع وميض أنظمة غير رسمية غير موقعة، حماية سلامة النظام والأمان الأساسي<br><span class="text-emerald-600 dark:text-emerald-400">✅ أمان عالٍ: تحميل الصور الموقعة رسمياً فقط، مقاومة فعالة للعبث بالبرامج الثابتة الخبيثة</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ أمان منخفض: السماح بميض ROM خارجي، آلية فحص سلامة النظام تتعطل، البرمجيات الخبيثة إذا حصلت على Root يمكنها العبث العميق بالنظام</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">استقرار النظام</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ضمان تشغيل الهاتف للنظام الرسمي المختبر والمُحسّن من الشركة، ضمان الاستقرار والسلاسة<br><span class="text-emerald-600 dark:text-emerald-400">✅ مستقر: استخدام البرامج الثابتة الرسمية، وظائف كاملة، تحديثات OTA موثوقة</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ زيادة المخاطر: ROM الخارجي قد يكون به مشاكل توافق، قد يؤدي لانهيار النظام وتحول الجهاز لقرميد، وأعطال وظائف العتاد (مثل الكاميرا والشحن السريع)، وقد تفشل تحديثات OTA</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">حقوق الضمان</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">الشركة توفر نظاماً رسمياً مستقراً عبر قفل BL لتقديم خدمة الضمان<br><span class="text-emerald-600 dark:text-emerald-400">✅ الضمان ساري: التمتع بخدمة الضمان المجانية الرسمية (للأضرار غير المتعمدة)</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ الضمان يبطل: أغلب الشركات تعتبر فتح BL تنازلاً طوعياً عن الضمان، حتى بعد إعادة القفل قد يُكشف سجل الفتح ويرفض الضمان</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">أمان البيانات</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">عملية الفتح تمسح البيانات إجبارياً عادة، لمنع استخدام البيانات القديمة في بيئة النظام الجديد بشكل خبيث<br><span class="text-emerald-600 dark:text-emerald-400">✅ أمان البيانات: في الاستخدام اليومي، قفل BL يحد من قدرة البرامج الخبيثة على تعديل قسم النظام</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ مخاطر البيانات: الفتح يمسح جميع بيانات المستخدم إجبارياً؛ إذا لم يُشفّر بشكل صحيح بعد الفتح، قد يكون تخزين البيانات غير آمن؛ بعد الفقدان يسهل استخراج البيانات عبر الوميض</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">قيود الوظائف</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ضمان عمل الوظائف المعتمدة على البيئة الآمنة (مثل المدفوعات وتطبيقات البنوك) بشكل طبيعي<br><span class="text-emerald-600 dark:text-emerald-400">✅ وظائف كاملة: جميع الوظائف الرسمية يمكن استخدامها بشكل طبيعي</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ وظائف محدودة: بعض التطبيقات الحساسة أمنياً (مثل Google Pay وتطبيقات البنوك) قد ترفض العمل due للكشف عن حالة فتح BL؛ قد تتدهور خدمات DRM، مما يؤثر على تشغيل الفيديو بدقة عالية</span></td>
                                </tr>
                            </tbody>
                        </table>
```
:::

#### ثانيًا: العملية التفصيلية لفك قفل BL (باستخدام شاومي كمثال)

1. <strong>: حل Root حديث، تصميم Systemless، يمكنه إخفاء حالة Root.</strong>Kernelsu
2. <strong>: حل Root قائم على النواة، أعمق وأفضل إخفاءً.</strong>SuperSU
3. <strong>: حل Root كلاسيكي، توقف تحديثه حاليًا.</strong>رابعًا: مدخل إلى فلاش النظام
4. <strong>فلاش النظام يعني تثبيت نظام تشغيل جديد على الهاتف. أنواع الفلاش الشائعة:</strong>فلاش ROM رسمي

#### ثالثًا: حلول Root المتعددة

- <strong>فلاش Recovery خارجي</strong>: مثل TWRP، يُستخدم للنسخ الاحتياطي والاستعادة وفلاش ROM خارجي.
- <strong>فلاش ROM خارجي</strong>: مثل LineageOS وPixel Experience، لتجربة أنظمة مختلفة.
- <strong>تحذير مهم</strong>فلاش النظام ينطوي على مخاطر، تصرف بحذر. قد يؤدي إلى:

#### رابعًا: مدخل إلى فلاش النظام

فقدان الضمان

- <strong>فقدان البيانات</strong>خلل في وظائف الدفع
- <strong>قبل الفلاش، احرص على نسخة احتياطية كاملة، واقرأ الدروس بعناية، وتأكد من تطابق طراز الجهاز والإصدار.</strong>موارد موصى بها
- <strong>XDA Developers</strong>: أكبر مجتمع لمطوري Android في العالم، يحتوي على ثروة من دروس الفلاش وموارد ROM.

#### خمسة: Samsung Knox: الثمن غير القابل للعكس لفتح BL

بخلاف شركات Android الأخرى، آلية فتح BL لهواتف Samsung لها تصميم "فاصل" فريد:<strong>بالنسبة لهواتف Samsung، الفتح يُفعّل فصل Knox، ويفقد بشكل دائم بعض الوظائف الأمنية (مثل Samsung Pay)؛ ويمسح جميع البيانات المحمية؛ ويؤثر على الضمان</strong>. تحديداً:

- <strong>الفاصل يستخدم لمرة واحدة</strong>: داخل الهاتف صمام eFuse، بمجرد الكشف عن فتح BL يُحرق بشكل دائم، لا يمكن استعادته.
- <strong>الوظائف المتأثرة</strong>: Samsung Pay (بطاقة المواصلات/البطاقة البنكية),مجلد Knox الآمن,إدارة MDM المؤسسية,بعض تطبيقات التأمين الصحي تتوقف جميعها.
- <strong>مسح إجباري للبيانات</strong>: بعد تفعيل الفاصل يُجبر الهاتف على الاستعادة للمصنع، وتُمسح جميع البيانات المحلية (البيانات السحابية غير متأثرة).
- <strong>تأثير الضمان</strong>: صرّحت رسمياً بأن فصل Knox يُفقد الجهاز خدمة الضمان.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>فكر مرتين قبل التصرف

{class="mt-1"}
فصل Knox في Samsung<strong>غير قابل للعكس</strong>بمجرد تفعيله لا يمكن العودة لحالة المصنع. إذا كنت تريد فقط وظائف تتطلب Root، يُنصح أولاً بالبحث عن بدائل لا تحتاج Root.
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>Coolapk

{class="mt-1"}
: مجتمع رقميات معروف محليًا، به الكثير من الدروس والنقاشات بالصينية.

{class="list-disc pl-6 mt-1 space-y-1"}
- منتديات كل طراز
- : مثل مجتمع شاومي ومجتمع OnePlus، بها دروس رسمية وشعبية.
- الفصل 25: معالجة الهواتف المستعملة والتراث الرقمي
- مرحبًا يا رفاق، بعد "التدريب" في أكثر من عشرين فصلًا سابقة، أعتقد أنك تطورت من "مبتدئ رقمي" إلى مستخدم هاتف واثق تمامًا. لكن الحياة التقنية لها دورة — سيتحول الحبيب الجديد قريبًا إلى حبيب قديم. عندما تستعد لإحالة "الرفيق القديم" إلى التقاعد، هل تعرف كيف تودعه بشكل لائق وآمن؟

{class="mt-1"}
أولًا: "الموت الرحيم" للهاتف القديم — دليل البيع أو الإهداء الآمن
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>المبدأ الأساسي: تنظيف البيانات ليس "حذفًا"، بل "كتابة فوق".

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>"التنظيف الشامل" الذاتي</strong>: أكمل آخر نسخة احتياطية كاملة، وسجّل الخروج من جميع الحسابات.
- <strong>تنفيذ "التهيئة" النهائية</strong>: "استعادة ضبط المصنع" في الهواتف الحديثة تتضمن عادة محوًا مشفرًا.
- <strong>"التمويه" الأخير</strong>: بعد استعادة ضبط المصنع، املأ التخزين بملفات غير مفيدة، ثم نفّذ استعادة ضبط المصنع مرة أخرى.
:::

#### ستة: أسئلة شائعة (Q&amp; A)

::: div .qa-item .mt-3
{class="font-semibold mb-1"}
<i class="fas fa-question-circle text-primary mr-1"></i>Q1: هل يمكن استعادة قفل BL بعد فتحه؟

{class="mb-2 pl-6"}
<strong>A:</strong>يمكن إعادة القفل. عادةً يتطلب وميض حزمة وميض سلكية رسمية كاملة، واستخدام سكربت وميض محدد (مثل <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">flash_all_lock.bat</code>) لإعادة القفل. لكن انتبه، بعد إعادة القفل، بعض الفواصل الأمنية المُفعّلة بالفتح (مثل Knox في Samsung) قد لا يمكن عكسها.
:::

::: div .qa-item .mt-3
{class="font-semibold mb-1"}
<i class="fas fa-question-circle text-primary mr-1"></i>Q2: كيف أحصل على Root بعد فتح القفل؟

{class="mb-2 pl-6"}
<strong>A:</strong>فتح قفل BL هو الخطوة الأولى فقط. Root عادةً يتطلب:

{class="list-decimal pl-12 mb-2 space-y-1"}
1. وميض Recovery مخصص (مثل TWRP).
2. وميض مدير Root مثل Magisk عبر Recovery لإصلاح صورة boot، للحصول على صلاحية Root.
:::
