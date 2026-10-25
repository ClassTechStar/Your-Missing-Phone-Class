---
id: di-er-shi-zhang-termux
part: jin-jie-pian
nav:  ملحق الفصل 20
toc: sub
kind: supplement
---

### ملحق الفصل 20:Termux — بيئة طرف Linux محمولة على أجهزة Android

{class="chapter-intro mb-4"}
إذا كنت ترى أن وضع المطور ليس "قوياً" بما يكفي، وتريد تجربة سطر أوامر Linux كامل على هاتفك، فإن Termux هو ما تبحث عنه. لا يتطلب صلاحية root، ويحوّل هاتف أندرويد عادي إلى محطة عمل Linux محمولة، وهو أداة قوية للمستخدمين المتقدمين لاستكشاف تطوير وإدارة الأنظمة على الأجهزة المحمولة.

#### أولاً: ما هو Termux

Termux هو تطبيق مفتوح المصدر لمحاكاة الطرف وبيئة Linux مصمم خصيصاً لأجهزة Android، يوفّر تجربة shell كاملة لـ Linux على الهاتف دون الحاجة إلى صلاحية root. كتطبيق خفيف (حجم التثبيت حوالي 30 ميغابايت فقط)، يدعم Termux نظام إدارة الحزم APT بمنظومة برمجيات غنية، ويتيح للمستخدمين تشغيل Python وNode.js وGit وSSH وغيرها على الأجهزة المحمولة، بل وبناء خوادم أو إجراء اختبارات اختراق.

قوة Termux الأساسية في خفّته وقابليته العالية للتوسعة، مما يجعله مناسباً لمختلف السيناريوهات مثل التطوير والتعلم وإدارة الأنظمة. يجمع بين الحزم البرمجية القياسية ومحاكاة الطرف الدقيقة في حل مفتوح المصدر واحد.

#### ثانياً: الوظائف والخصائص الأساسية

##### 🖥️ بيئة Linux كاملة

Termux<strong>Bash مدمج فقط</strong>هذا النوع من Shell. إذا أردت استخدام Zsh أو fish أو غيرها، تحتاج تثبيتها يدوياً عبر مدير الحزم، مثلاً:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install zsh</code>أو<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install fish</code>. يدعم Termux أيضاً محررات مثل Vim وNano وEmacs، ويوفر تجربة سطر أوامر قريبة من الأصلية. يمكن للمستخدم تثبيت أكثر من 2000 حزمة برمجية عبر "pkg install"، بما فيها GCC وOpenSSH وSQLMap وغيرها من أدوات التطوير والأمان.

##### 📦 إدارة حزم قوية

يستخدم مدير الحزم APT (مشابه لـ Debian وUbuntu)، يمكن تثبيت آلاف حزم Linux، تغطي أدوات التطوير وأدوات الشبكة وغيرها. يدعم بيئات لغات برمجة متعددة مثل Python وRuby وNode.js وGo وRust وSwift.

##### 🔒 وظائف الأمان والشبكة

- <strong>اتصال SSH عن بُعد</strong>: يدعم وظائف عميل وخادم SSH، يمكن الاتصال بأجهزة أخرى عن بُعد أو جعل الهاتف مضيف SSH.
- <strong>أدوات التشفير</strong>: يوفّر أدوات تشفير مثل OpenSSL، يدعم تشفير البيانات والاتصال الآمن.
- <strong>بناء الخوادم</strong>: يمكن تهيئة Nginx أو Apache لبناء خادم صفحات ثابتة.

##### 🔧 تكامل النظام والتوسعة

- الوصول إلى صلاحية تخزين الهاتف، لتحقيق إدارة الملفات المحلية.
- استدعاء وظائف أجهزة Android مثل المستشعرات والكاميرا عبر إضافة Termux:API.
- دعم لوحة مفاتيح Bluetooth والشاشات الخارجية، مع دعم كامل للماوس.

#### ثالثاً: منظومة إضافات النظام البيئية

يمكن توسعة تطبيق Termux الأساسي بعدة تطبيقات إضافات اختيارية، توفّر وظائف وتكاملات إضافية:

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">اسم الإضافة</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">وصف الوظيفة</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:API</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">يعرّض وظائف Android API لبرامج سطر الأوامر</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Boot</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">يسمح بتشغيل السكربتات عند إقلاع الجهاز</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Float</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">يوفّر نافذة طرف عائمة</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Styling</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">يفعّل أنظمة ألوان وتخصيص الخطوط للطرف</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Tasker</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">يدمج سكربتات Termux مع تطبيق الأتمتة Tasker</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Widget</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">يسمح بتشغيل السكربتات من عنصر واجهة على الشاشة الرئيسية</td>
                            </tr>
                        </tbody>
                    </table>
```

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>تنبيه مهم

{class="mt-1"}
يجب تثبيت Termux وإضافاته من المصدر نفسه، لأنها تتشارك نفس sharedUserId. خلط التثبيتات من مصادر مختلفة (مثل F-Droid وGitHub) سيؤدي إلى أخطاء في التثبيت.
:::

#### رابعاً: دليل التثبيت والتهيئة

##### 📥 خطوات التثبيت

1. <strong>تنزيل التطبيق</strong>: نزّل Termux من القناة الرسمية (F-Droid أو GitHub)، لا يتطلب صلاحية root.
2. <strong>تهيئة النظام</strong>: بعد أول تشغيل انتظر حتى يكتمل "Installing bootstrap packages".
3. <strong>الحصول على صلاحية التخزين</strong>: نفّذ<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-setup-storage</code>للحصول على صلاحية نظام ملفات الهاتف.
4. <strong>تحديث مصادر البرمجيات</strong>: نفّذ<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code>لتحديث قائمة الحزم.

##### ⚙️ التحسين الأساسي

- <strong>تغيير مصدر المرآة</strong>: استخدم الأمر<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-change-repo</code>لتغيير مصدر المرآة عبر واجهة رسومية (يُوصى بمصدر مرآة جامعة Tsinghua).
- <strong>إعداد الاختصارات</strong>: مفتاح خفض الصوت يحاكي Ctrl، مفتاح رفع الصوت يحاكي Esc، لتحسين كفاءة الإدخال.
- <strong>تجميل الواجهة</strong>: ثبّت Zsh + Oh My Zsh، وتهيئة السمات والإضافات.

#### خامساً: سيناريوهات التطبيق النموذجية

##### 💻 اختبار التطوير المحمول

بناء بيئة تطوير كاملة على الهاتف، كتابة وتشغيل سكربتات Python، استخدام GCC لتجميع برامج C، إدارة مستودعات الأكواد عبر Git، والمزامنة مع الخوادم البعيدة عبر SSH.

##### 🖥️ تشغيل وصيانة الخوادم

إدارة الخوادم عن بُعد عبر SSH، تنفيذ مهام صيانة النظام وتحليل السجلات، ومعالجة مشاكل الخوادم في أي وقت وأي مكان.

##### 📚 تعلم عمليات Linux

يوفر بيئة Linux حقيقية، وهو منصة مثالية لتعلم سطر الأوامر وإدارة النظام، يمكن التدرب على كتابة سكربتات Shell وإدارة صلاحيات ملفات Linux (مثل <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chmod 755</code> ضبط صلاحيات rwxr-xr-x،<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chown user:group</code> تعديل مالك الملف،<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls -l</code> عرض owner/group/other ثلاث مجموعات تسع بتات) وغيرها من الأوامر الأساسية. تجدر الإشارة إلى أن هذا نموذج الصلاحيات "ثلاث مجموعات تسع بتات" الكلاسيكي في Unix/Linux (owner / group / other × قراءة / كتابة / تنفيذ)، وهو نظام مختلف تماماً عن نظام ACL لقائمة التحكم بالوصول في Windows NTFS.

##### 🔐 اختبار أمن الشبكات

تثبيت أدوات أمنية مثل Nmap وSQLMap وHydra وMetasploit، لإجراء مسح الشبكات واختبارات الاختراق.

#### سادساً: الإصدارات والتوافق

أحدث إصدار مستقر من Termux هو v0.118.2، مناسب لأجهزة Android ≥ 7. تجدر الإشارة إلى أن Termux قد يكون غير مستقر على Android 12 والإصدارات الأحدث، يُنصح بمتابعة سجل التحديثات الرسمي للحصول على أحدث معلومات التوافق.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>خلاصة

{class="mt-1"}
يجلب Termux تجربة طرف Linux القوية إلى أجهزة Android، ويجعل الهاتف أداة تطوير وتعلم محمولة. سواء كنت مطوراً أو مدير أنظمة أو هاوياً للتقنية، يمكنك الاستفادة من Termux على الأجهزة المحمولة للاستمتاع بتجربة سطر أوامر كاملة، وتحقيق مفهوم "Linux في جيبك".
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>جرّب: شغّل أول أمر Linux على هاتفك

{class="list-decimal pl-6 mt-1 space-y-1"}
1. نزّل Termux من F-Droid وثبّته، وعند أول تشغيل انتظر اكتمال التهيئة.
2. نفّذ<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code>لتحديث الحزم.
3. ثبّت Python:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install python</code>.
4. أدخل<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python3 -c "print('Hello from Termux!')"</code>، واستمتع بمتعة تشغيل الكود على الهاتف.
:::
