---
id: di-wu-shi-qi-zhang
num: 57
part: an-zhuo-kai-fa-pian
nav: บทที่ 57: เส้นทางระดับสูง — สิทธิ์การเข้าถึง การแจ้งเตือน และสถาปัตยกรรมสมัยใหม่
toc: default
kind: chapter
---

### บทที่ 57: เส้นทางขั้นสูง — สิทธิ์การเข้าถึง การแจ้งเตือน และสถาปัตยกรรมสมัยใหม่

{class="chapter-intro mb-4"}
ทำแอปออกมาได้เป็นแค่จุดเริ่มต้น บทนี้จะคุยเรื่องก้าวสำคัญจาก “ทำได้” ไปสู่ “ทำได้ดี”: จะขอสิทธิ์การเข้าถึงอย่างสวยงามได้อย่างไร จะส่งการแจ้งเตือนอย่างไรไม่ให้น่ารำคาญ จะยกสถาปัตยกรรมขึ้นอีกขั้นได้อย่างไร และ — ในปี 2026 จะจับมือกับ AI เขียนโค้ด Android อย่างไร ทุกข้อคือสิ่งที่คุณจะเจอทันทีในโปรเจกต์จริง

#### 1. สิทธิ์ขณะรัน: เคาะประตูก่อนแล้วค่อยเข้า

กล้อง, ตำแหน่งที่ตั้ง, สมุดรายชื่อ, การแจ้งเตือน … “เขตอ่อนไหว” เหล่านี้ Android กำหนดให้แอปต้องขอจากผู้ใช้ขณะรันแอป (ตั้งแต่ Android 6 เป็นต้นมา) กฎคือ: ประกาศก่อน (ใน Manifest) แล้วค่อยขอ (ในโค้ด) ถ้าผู้ใช้ปฏิเสธต้องรับมืออย่างสุภาพ ใน Compose ใช้ rememberPermissionState จากไลบรารีทางการ Accompanist แล้วสบายใจที่สุด:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · สิทธิ์ runtime (เวอร์ชัน Compose)</span><span class="dots">···</span>
:::

```
// ประกาศใน Manifest ก่อน:
// &lt;uses-permission android:name="android.permission.CAMERA" /&gt;

@Composable
fun CameraButton() {
    val permission = rememberPermissionState(
        permission = android.Manifest.permission.CAMERA
    )
    Button(onClick = {
        when {
            permission.status.isGranted -&gt; openCamera()
            permission.status.shouldShowRationale -&gt; showExplainDialog()
            else -&gt; permission.launchPermissionRequest()
        }
    }) { Text("ถ่ายรูป") }
}
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ข้อควรรู้: ถูกปฏิเสธแบบถาวรแล้วทำยังไง?

{class="mt-1"}
เมื่อผู้ใช้ติ๊ก “ไม่ต้องถามอีก” แล้ว launchPermissionRequest จะไม่ขึ้นหน้าต่างถามอีก ตอนนั้นให้ชี้ทางให้ผู้ใช้ไปเปิดเองในการตั้งค่าระบบ (ใช้ Intent เด้งไปหน้าตั้งค่าของแอป) พร้อมอธิบายในหน้าจอว่า “สิทธิ์นี้เอาไว้ทำอะไร” ทำตัวนุ่มนวลขึ้นหน่อย ผู้ใช้จะยอมเปิดสิทธิ์มากขึ้นเยอะ — ข้อความตอนขอสิทธิ์ ควรค่าแก่การเขียนให้ดี
:::

#### 2. การแจ้งเตือน: บอกสิ่งที่มีประโยชน์ในเวลาที่ถูกต้อง

การแจ้งเตือนคือช่องทางที่แอปเข้าถึงผู้ใช้ และเป็นฟีเจอร์ที่ผู้ใช้ “บล็อก” ง่ายที่สุด วินัย 3 ข้อในการส่งการแจ้งเตือน: ส่งแต่สิ่งที่มีประโยชน์ ให้ผู้ใช้ปิดได้ อย่าไปรบกวนกลางดึก การใช้งานพื้นฐาน:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · ส่งการแจ้งเตือน</span><span class="dots">···</span>
:::

```
// Android 13+ ต้องขอสิทธิ์ POST_NOTIFICATIONS ก่อน (ดูบทก่อนหน้า)

// 1. สร้างแชแนลแจ้งเตือน (Android 8+ ต้องมี)
val channel = NotificationChannel(
    "reminder", "เตือน", NotificationManager.IMPORTANCE_DEFAULT
)
val manager = getSystemService(NotificationManager::class.java)
manager.createNotificationChannel(channel)

// 2. ส่งการแจ้งเตือน
val notification = NotificationCompat.Builder(this, "reminder")
    .setSmallIcon(R.drawable.ic_notification)
    .setContentTitle("เตือนจดบัญชี")
    .setContentText("วันนี้ยังไม่ได้จดบัญชีนะ")
    .setPriority(NotificationCompat.PRIORITY_DEFAULT)
    .build()
if (ActivityCompat.checkSelfPermission(this,
        Manifest.permission.POST_NOTIFICATIONS) == PackageManager.PERMISSION_GRANTED
) {
    manager.notify(1, notification)
}
```
:::

งานตามเวลา (เช่น “แจ้งเตือนให้จดบัญชีทุกวัน 20:00”) ให้ใช้ WorkManager — มันคือ “ผู้จัดการตารางงานเบื้องหลัง” ที่ทางการแนะนำ รับประกันว่างานจะถูกรันในจังหวะที่เหมาะสม ไม่ต้องไปกังวลเรื่องประหยัดแบตเอง งานแนวปลุกเตือนแบบนี้ใช้มันถูกทางแน่นอน

#### 3. สถาปัตยกรรมขั้นถัดไป: dependency injection และการแบ่งโมดูล

พอโปรเจกต์ใหญ่ขึ้น ปัญหาหวาน ๆ สองเรื่องจะตามมาเยือน:

- การสร้าง object รกขรุงขราง: ทุกหน้าจอต่างพากัน new ฐานข้อมูล new API ของตัวเอง — ใช้ Hilt (เฟรมเวิร์ก dependency injection) มาจัดการให้เป็นระบบ “ใครต้องการอะไร เอ่ยปากแล้วมีคนส่งให้ทันที”;
- โค้ดกองเป็นภูเขา: โปรเจกต์โมดูลเดียวยิ่งแก้ยิ่งช้า — แยกเป็นหลายโมดูล (app / core / feature-xxx) ให้แต่ละฟีเจอร์พัฒนาและทดสอบแยกจากกัน.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
เคล็ดลับ: อย่าออกแบบเกินจำเป็น

{class="mt-1"}
ทั้ง Hilt และการแบ่งโมดูลเป็นเครื่องมือดี แต่โปรเจกต์คนเดียวอย่ารีบใช้ แอปบันทึกรายรับ-รายจ่ายแบบโมดูลเดียว + สร้าง dependency ด้วยมือก็เอาอยู่สบาย รอโค้ดเกินหลายหมื่นบรรทัด คอมไพล์เริ่มช้า หรือต้องทำงานหลายคน ค่อยแนะนำเข้ามาตามความจำเป็น เครื่องมือมีไว้รับใช้เป้าหมาย ไม่ใช่ไว้โชว์ — นี่ก็คือหลัก “เรียบง่ายเหนือสิ่งอื่นใด” ในหนังสือเขียนโค้ดด้วย AI ของเรานี่เอง
:::

#### 4. วิธีเล่นใหม่ปี 2026: ใช้ AI ช่วยพัฒนา Android

ปี 2026 AI ได้แทรกซึมเข้ากระบวนการพัฒนา Android อย่างลึกซึ้งแล้ว ถ้าอยากเร่งความเร็ว ชุดท่าต่อเนื่องนี้เข้าทางมาก:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ขั้นตอน</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">AI ช่วยอย่างไร</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">หน้าที่ของคุณ</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เขียนโค้ด</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gemini ที่ฝังมาใน Android Studio / ปลั๊กอิน AI ของบุคคลที่สาม ช่วยเติมและสร้างโค้ด</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">อธิบายความต้องการให้ชัด และตรวจผลงาน</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ค้นคว้าข้อมูล</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">โยนเอกสารทางการกับข้อความ error ให้ AI ช่วยอ่านแปลความ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ข้อสรุปสำคัญต้องกลับไปเช็กกับเอกสารทางการ</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เขียนเทสต์</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ให้ AI สร้างเทสต์เคสตาม 3 ประเภท “ปกติ / ขอบเขต / ผิดปกติ”</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ยืนยันว่าเทสต์เคสสอดคล้องกับความหมายทางธุรกิจ</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">แก้บั๊ก</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">แปะ stack trace + โค้ดที่เกี่ยวข้อง ให้ AI ชี้จุดและแก้</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">อ่านการแก้ไขให้เข้าใจ แล้วรันเทสต์ยืนยัน</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
4 สถานการณ์ของการใช้ AI ช่วยพัฒนา Android

วิธีทำแบบละเอียด — จะสั่ง AI อย่างไร จะตรวจรับงานอย่างไร จะเลี่ยงหลุมพรางอย่างไร — มีครบ 11 บทในภาคที่ 7 “ลงมือเขียนโค้ดด้วย AI” (บทที่ 37-47) ของหนังสือเล่มนี้ แนะนำอย่างแรงให้อ่านคู่กัน: ไวยากรณ์ Android ฝากไว้กับภาคนี้ ส่วนศาสตร์การทำงานร่วมกับ AI ฝากไว้กับภาคที่ 7

#### 5. ปรับปรุงประสิทธิภาพ Compose กับเครื่องมือดีบัก

เขียน Compose สนุกจริง แต่ “recompose เยอะเกินไป” ก็ทำให้กระตุกได้ สามเทคนิคที่ใช้ได้จริง:

- ทำพารามิเตอร์ให้เสถียร: ใส่ @Immutable ให้ data class หรือใช้ derivedStateOf เพื่อกันไม่ให้สถานะที่ไม่เกี่ยวข้องเปลี่ยนแล้วจุด recompose ทั้งจอ;
- อย่าลืมใช้ key: items(list, key = { it.id }) ทำให้เวลาเพิ่มหรือลบรายการ มีแค่รายการที่ควรขยับเท่านั้นที่ขยับ — ไม่ใส่ key แล้วลบไปหนึ่งชิ้น ทั้งลิสต์อาจวาดใหม่หมดเลย;
- โหมด Compose ของ Layout Inspector: ดูจำนวนครั้งที่แต่ละ Composable ถูก recompose แบบสด ๆ ใคร recompose ถี่เห็นกันชัด ๆ แล้วปรับปรุงตามจุดร้อน.

อีกอย่าง เปิดรายงานของ Compose compiler (Metrics) ด้วย จะได้รายงานว่า “คอมโพเนนต์ไหนยังไม่เสถียร” — บนเส้นทางขั้นสูง ข้อมูลเชื่อถือได้เสมอกว่าความรู้สึก

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ลงมือทำ: เพิ่ม “ชุดสามชิ้น” ให้แอปบันทึกรายรับ-รายจ่าย

{class="mt-1"}
① เพิ่ม “แจ้งเตือนให้จดบัญชีทุกวัน 20:00” ให้แอป (WorkManager + notification channel + สิทธิ์แจ้งเตือนของ Android 13); ② เปลี่ยนการสร้างฐานข้อมูลและ API ให้เป็นการ inject ผ่าน Hilt; ③ ลองใช้เครื่องมือ AI เร่งทำฟีเจอร์ “กรองรายการรายเดือน” แล้วตรวจผลงานด้วยวิธีตรวจรับ 3 ชั้น ทำชุดสามชิ้นจบ โปรเจกต์ของคุณก็จะดูเป็น “ทีมงานมืออาชีพ” ขึ้นมาทันที
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
สรุปบทนี้

- สิทธิ์อ่อนไหว: ประกาศใน Manifest + ขอขณะรัน + ถูกปฏิเสธแล้วชี้ทางอย่างสุภาพ
- วินัย 3 ข้อของการแจ้งเตือน: ส่งแต่ของมีประโยชน์ ปิดได้ ไม่รบกวน; ต้องมีทั้ง channel และสิทธิ์ ขาดอย่างใดอย่างหนึ่งไม่ได้
- งานตามเวลาใช้ WorkManager อย่าปั่นล้อขึ้นมาเอง
- Hilt ดูแล object, โมดูลดูแลโค้ด — โปรเจกต์เล็กคนเดียวอย่ารีบใช้
- AI ช่วยได้ 4 สถานการณ์: เขียนโค้ด ค้นข้อมูล เขียนเทสต์ แก้บั๊ก; วิธีทำอยู่ในภาคที่ 7 (บทที่ 37-47)
:::
