---
id: di-wu-shi-liu-zhang
num: 56
part: an-zhuo-kai-fa-pian
nav: บทที่ 56: ขัดเกลาและเผยแพร่ — ขึ้น Google Play
toc: default
kind: chapter
---

### บทที่ 56: ขัดเกลาและเผยแพร่ — ทดสอบ ดีบัก และขึ้น Google Play

{class="chapter-intro mb-4"}
ทำแอปเสร็จแล้ว ต่อไปล่ะ? บทนี้ตอบสามเรื่องของการจาก "รันได้" สู่ "ส่งมอบได้": ดีบักหาบั๊กอย่างมีประสิทธิภาพยังไง เขียนเทสกันบั๊กย้อนกลับยังไง และเอาแอปขึ้น Google Play ให้คนทั้งโลกดาวน์โหลดยังไง การขึ้นสโตร์ไม่ใช่แค่พิธีกรรม — มันคือเส้นแบ่งระหว่างผลงานชิ้นหนึ่งกับสินค้าหนึ่งชิ้น

#### 1. สามอาวุธดีบัก: Logcat, Breakpoint, ตัวตรวจ UI

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">เครื่องมือ</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ทำอะไร</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ใช้ยังไง</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logcat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ดู log ของระบบ/ของเราที่พิมพ์เอง</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ในโค้ดพิมพ์ Log.d("TAG", "ค่า=$x") แล้วค้นหา TAG ในแผงเพื่อกรอง</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ดีบักด้วยเบรกพอยต์</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ให้โปรแกรมหยุดที่บรรทัดที่ต้องการ แล้วดูค่าตัวแปร</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">คลิกข้างเลขบรรทัดให้ขึ้นจุดแดง แล้วรันในโหมด Debug ไล่ทีละขั้น</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Layout Inspector</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ดูโครงสร้างหน้าจอขณะแอปทำงานอยู่</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เมนู Tools → Layout Inspector ดูแผนผังคอมโพเนนต์แบบสด ๆ</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
สามท่าเด็ดของการดีบัก

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
เคล็ดลับ: วิธีอ่านข้อความ error?

{class="mt-1"}
เมื่อแอปพัง ใน Logcat จะมี stack trace สีแดง (Stacktrace) ให้ไล่จากล่างขึ้นบน หาบรรทัดแรกที่ขึ้นต้นด้วยชื่อแพ็กเกจของเราเอง (เช่น com.example.yourapp) บรรทัดนั้นมักเป็น “ที่เกิดเหตุ” พอดี ดู “ชนิดของ Exception” ก่อน (null pointer? แปลงชนิดข้อมูลผิด?) แล้วค่อยดู “at ... ไฟล์ของเรา:บรรทัด” เทคนิคนี้แก้ crash ได้ถึง 80%
:::

#### 2. การทดสอบ: ทำประกันให้โค้ด

การทดสอบด้วยมือไม่น่าเชื่อถือ — แก้ฟีเจอร์นี้ไป อีกฟีเจอร์ก็พังเงียบ ๆ ไปด้วย การทดสอบคือทั้ง “ยาถอนพิษ” และ “เสื้อเกราะกันกระสุน” การทดสอบใน Android แบ่งเป็น 3 ชั้น มือใหม่เริ่มจากทำความเข้าใจชั้นแรกให้แน่นก่อน:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ชั้น</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ทดสอบอะไร</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">วางไว้ที่ไหน</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ความเร็ว</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ยูนิตเทสต์</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ลอจิกล้วน ๆ (การคำนวณ การตรวจสอบ)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/test/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ระดับวินาที</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">อินสตรูเมนต์เทสต์</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">พฤติกรรมหน้าจอบนอุปกรณ์จริง</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/androidTest/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ระดับนาที</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เทสต์ด้วยมือ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ให้คนจริงสัมผัสและใช้งานจริง</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ต้องมีตลอดไป</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
การทดสอบสามชั้น

::: div .code-block
:::inline div .code-head
<span>KOTLIN · ตัวอย่าง unit test</span><span class="dots">···</span>
:::

```
// แยกตรรกะ "แปลงข้อความจำนวนเงินเป็นตัวเลข" ออกเป็นฟังก์ชันล้วน
fun parseAmount(input: String): Double? {
    val v = input.trim().toDoubleOrNull()
    return if (v != null && v > 0) v else null
}

// ทดสอบมัน (JUnit4)
@Test
fun emptyInputReturnsNull() {
    assertEquals(null, parseAmount(""))
}
@Test
fun negativeReturnsNull() {
    assertEquals(null, parseAmount("-5"))
}
@Test
fun normalValueParses() {
    assertEquals(12.5, parseAmount("12.5"))
}
```
:::

การตรวจสอบจำนวนเงินและการคำนวณสถิติในแอปบันทึกรายรับ-รายจ่าย ควรมียูนิตเทสต์คอยปกป้องไว้ วิธีรันเทสต์: คลิกขวาที่โฟลเดอร์ test → Run ถ้าขึ้นเขียวผ่านหมด ก็แก้โค้ดได้อย่างมั่นใจ

#### 3. การเซ็นและแพ็กเกจ: ประทับตราให้แอป

Android กำหนดว่าไฟล์ติดตั้งทุกไฟล์ต้องถูกเซ็นก่อน — เหมือนประทับตราทางการ ยืนยันว่า “แพ็กเกจนี้มาจากเราและไม่ถูกแก้ไข” ตอนดีบัก Android Studio จะเซ็นด้วย debug key ให้อัตโนมัติ ส่วนการเผยแพร่ต้องใช้ release key ของเราเอง ขั้นตอนมีดังนี้:

1. เมนู Build → Generate Signed Bundle / APK;
2. สร้างไฟล์ keystore (คลังกุญแจ) — ตั้งรหัสผ่านและเก็บรักษาให้ดี;
3. เลือก release + รูปแบบ AAB แล้วบิลด์เป็นอันเสร็จ.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ระวังพลาด: keystore หาย = แอปหาย

{class="mt-1"}
หลังขึ้นสโตร์ การอัปเดตแอปต้องใช้ลายเซ็นชุดเดิมเสมอ ไม่เช่นนั้นสโตร์จะปฏิเสธการอัปเดต ถ้าไฟล์ keystore และรหัสผ่านหายไป คุณจะเหลือทางเดียวคือสร้างแอปใหม่ขึ้นมาขึ้นสโตร์ใหม่ตั้งแต่ต้น — ผู้ใช้เดิมทั้งหมดเชื่อมต่อไม่ได้เลย อย่าลืมสำรอง keystore และรหัสผ่านไว้ในที่ปลอดภัย (เข้ารหัสในคลาวด์ + สมุดจด) นี่คือบทเรียนที่แพงที่สุดบทหนึ่งของนักพัฒนา Android
:::

#### 4. กระบวนการครบวงจรของการขึ้น Google Play

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> สมัครบัญชีนักพัฒนา</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> เตรียมสื่อสำหรับสโตร์</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> อัปโหลด AAB</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> กรอกตารางความปลอดภัยข้อมูล</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> รีวิว (หลายชั่วโมง~หลายวัน)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> เผยแพร่บนสโตร์</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
ภาพที่ 6: หกขั้นตอนสู่ Google Play
:::

- ลงทะเบียน: ค่าสมัครครั้งเดียว 25 ดอลลาร์ ต้องมีบัญชี Google ที่ใช้งานได้;
- สื่อ: ไอคอนแอป (512×512), ภาพหน้าจอ (อย่างน้อย 2 ภาพ), คำอธิบายฟีเจอร์, ลิงก์นโยบายความเป็นส่วนตัว (ถ้ามีการเก็บข้อมูลต้องใส่);
- แบบฟอร์มความปลอดภัยของข้อมูล: แจ้งตรง ๆ ว่าเก็บข้อมูลอะไรบ้าง — แอปบันทึกรายรับ-รายจ่ายที่ไม่ต่อเน็ตเลือก “ไม่เก็บเลย” ก็ได้;
- ตรวจสอบ: บัญชีใหม่ที่ขึ้นสโตร์ครั้งแรกมักถูกตรวจโดยคน ใช้เวลาตั้งแต่ไม่กี่ชั่วโมงถึงหลายวัน ถ้าถูกส่งกลับให้แก้ตามข้อเสนอแนะ.

สำหรับผู้ใช้ในจีน: Google Play ต้องใช้สภาพแวดล้อมเครือข่ายพิเศษ และการเผยแพร่ในจีนแผ่นดินใหญ่มักทำผ่านสโตร์ในประเทศ (Huawei, Xiaomi, Yingyongbao ฯลฯ) ขั้นตอนขึ้นสโตร์ในประเทศคล้ายกัน แต่แต่ละสโตร์มีเกณฑ์ตรวจสอบแบบของตัวเอง — AAB/APK ชุดเดียวกันเผยแพร่หลายสโตร์ได้ สำหรับการฝึกมือ ขึ้นได้สักสโตร์หนึ่งก็ถือว่าชนะแล้ว

#### 5. ทำสื่อในสโตร์อย่างไร: ความประทับใจแรกก็คือยอดดาวน์โหลด

หน้าสโตร์คือหน้าต่างโชว์ที่ผู้ใช้เห็นตอน “เดินเลือกซื้อ” สื่อ 3 อย่างตัดสินความประทับใจแรก:

- ไอคอน: 512×512 อย่าใช้ภาพหน้าจอมาแก้ขัด ถ้าไม่มีทักษะออกแบบ ให้ใช้เครื่องมือ AI สร้างรูปทรงเรขาคณิตเรียบ ๆ ขึ้นมา เกณฑ์ผ่านคือหดเล็กลงบนหน้าจอหลักแล้วยังมองปุ๊บรู้เรื่องทันที;
- ภาพหน้าจอ: อย่างน้อย 2 ภาพ ดีที่สุด 4-6 ภาพ โชว์สถานการณ์ใช้งานที่สำคัญที่สุด แต่ละภาพแปะประโยคสั้น ๆ เป็นภาษาคน (“จดรายการเสร็จในวินาทีเดียว” ดีกว่า “โซลูชันบันทึกบัญชีที่มีประสิทธิภาพ” สิบเท่า);
- คำอธิบาย: ประโยคแรกต้องบอกให้ชัดว่า “นี่คืออะไร + ทำไว้ให้ใครใช้” อย่าเรียงร้อยคำว่า “เป็นมืออาชีพที่สุด เก่งที่สุด” — ผลการค้นหาในสโตร์ขึ้นกับคีย์เวิร์ดและอัตราการดาวน์โหลดเป็นหลัก ความจริงใจได้ผลกว่าการอวด.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
เคล็ดลับ: เปิดเทียบแอปเพื่อนร่วมอาชีพ

{class="mt-1"}
ก่อนขึ้นสโตร์ หมั่นเข้าไปดูแอปประเภทเดียวกันใน 10 อันดับแรก จับภาพมาเปรียบเทียบ: ไอคอนเขาสไตล์ไหน? ภาพหน้าจอขายจุดไหน? เขียนชื่ออย่างไร? เลียนแบบไม่ใช่ลอก — เรียนรู้สูตร แล้วใส่เนื้อหาของตัวเอง นี่คือบทเรียนที่ทำให้ผลิตภัณฑ์ใหม่เริ่มต้นได้เร็วที่สุด
:::

#### 6. เช็กลิสต์เล็ก ๆ เรื่องประสิทธิภาพกับการรายงาน crash

ก่อนขึ้นสโตร์ สองเรื่องนี้คุ้มค่าที่จะลงเวลาอย่างละครึ่งชั่วโมง:

##### 1. เช็กประสิทธิภาพด้วยตัวเอง 4 ข้อ

1. ลิสต์ใช้ LazyColumn: รายการยาว ๆ ห้ามใช้ Column เรียงตรง ๆ เด็ดขาด — lazy loading คือบทเรียนแรกเรื่องประสิทธิภาพบน Android;
2. อย่ายัดภาพต้นฉบับลงไปตรง ๆ: ใช้ไลบรารีภาพ Coil ย่อขนาดและแคชให้อัตโนมัติ ภาพต้นฉบับ 5MB ไฟล์เดียวก็พอทำให้เครื่องราคาถูกกระตุกจนตาย;
3. หลีกเลี่ยงการทำงานหนักบน main thread: ฐานข้อมูล เครือข่าย ไฟล์ใหญ่ ทำใน coroutine ทั้งหมด;
4. ใช้ Profiler วัดดู: เครื่องมือวิเคราะห์ประสิทธิภาพในตัวของ Android Studio บอกได้ทั้งหน่วยความจำ CPU และการกินแบต — วัดก่อน แล้วค่อยปรับปรุง อย่าเดาด้วยความรู้สึก.

##### 2. รายงาน crash

แอปไม่พังตอนเราทดสอบ ไม่ได้แปลว่าจะไม่พังบนเครื่องผู้ใช้ ก่อนขึ้นสโตร์ ต่อ Firebase Crashlytics (ของ Google เอง ฟรี): แค่ไม่กี่บรรทัดของการตั้งค่า เมื่อแอปของผู้ใช้พัง มันจะส่ง stack trace ขึ้นมาให้อัตโนมัติ คุณเห็นในหลังบ้านเลยว่า “รุ่นไหน เวอร์ชันไหน พังบรรทัดไหน” การขึ้นสโตร์โดยไม่มีระบบเฝ้าดู crash เท่ากับขับรถล้อตา

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ลงมือทำ: “ส่งมอบ” แอปบันทึกรายรับ-รายจ่ายสักครั้ง

{class="mt-1"}
① เติมยูนิตเทสต์ 3 ตัวให้ลอจิกอย่าง parseAmount และอื่น ๆ; ② ใช้ Logcat จับ crash ที่เราสร้างขึ้นเองด้วยมือตัวเองแล้วแก้ให้หาย; ③ สร้าง APK ที่เซ็นแบบ release ส่งให้เพื่อนติดตั้ง (นี่คือ “พิธีกรรม” ของผลงาน); ④ ถ้ามีแรงเหลือ ลงทะเบียนบัญชีนักพัฒนาแล้วยื่นแอปบันทึกรายรับ-รายจ่ายขึ้นสโตร์จริง ๆ สามข้อแรกทำเสร็จได้ในคืนนี้
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
สรุปบทนี้

- สามท่าเด็ดของการดีบัก: Logcat ดู log, เบรกพอยต์ดูตัวแปร, Layout Inspector ดูหน้าจอ
- อ่าน crash: ไล่ stack จากล่างขึ้นบน หาบรรทัดแรกที่เป็นชื่อแพ็กเกจของเรา
- ทดสอบ 3 ชั้น: ยูนิต (ระดับวินาที เริ่มจากอันนี้) / อินสตรูเมนต์ / แมนนวล
- เผยแพร่ต้องเซ็น: สำรอง keystore กับรหัสผ่านให้ดี ถ้าหาย แอปก็ต้อง “เปลี่ยนตัว” ไป
- หกขั้นตอนขึ้นสโตร์: ลงทะเบียน → เตรียมสื่อ → อัปโหลด AAB → กรอกแบบฟอร์มความปลอดภัยของข้อมูล → ตรวจสอบ → เผยแพร่
:::
