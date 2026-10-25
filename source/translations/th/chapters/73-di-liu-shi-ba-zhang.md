---
id: di-liu-shi-ba-zhang
num: 68
part: ios-kai-fa-pian
nav: บทที่ 68: เส้นทางระดับสูง — สิทธิ์การเข้าถึง การแจ้งเตือน และสถาปัตยกรรมสมัยใหม่
toc: default
kind: chapter
---

### บทที่ 68: เส้นทางขั้นสูง — สิทธิ์การเข้าถึง การแจ้งเตือน และสถาปัตยกรรมยุคใหม่

{class="chapter-intro mb-4"}
ทำแอปออกมาได้เป็นแค่จุดเริ่มต้น บทนี้คุยเรื่องก้าวสำคัญจาก'ทำเป็น'ไปสู่'ทำดี': ขอสิทธิ์การเข้าถึงอย่างสวยงามอย่างไร ส่งการแจ้งเตือนให้ไม่น่ารำคาญอย่างไร ยกสถาปัตยกรรมขึ้นอีกขั้นอย่างไร และ — ในปี 2026 จับคู่กับ AI เขียนโค้ด iOS อย่างไร ทุกข้อล้วนเป็นเรื่องที่คุณจะเจอทันทีในโปรเจกต์จริง

#### 1. สิทธิ์การเข้าถึง: เคาะประตูก่อน แล้วค่อยเข้าบ้าน

กล้อง, ตำแหน่งที่ตั้ง, สมุดรายชื่อ, การแจ้งเตือน... 'เขตอ่อนไหว'พวกนี้ iOS บังคับให้แอปเด้งหน้าต่างขออนุญาตจากผู้ใช้ตอนใช้จริง กติกาคือสามขั้น'ประกาศ + ขออนุญาต + ลดรูปอย่างสวยงาม':

::: div .code-block
:::inline div .code-head
<span>SWIFT · ขอสิทธิ์ (ยกตัวอย่างตำแหน่งที่ตั้ง)</span><span class="dots">···</span>
:::

```
// 1. ประกาศข้อความอธิบายใน Info.plist (ไม่ประกาศแอปจะเด้งทันที!)
// Privacy - Location When In Use Usage Description: "ใช้สำหรับดูสภาพอากาศในเมืองของคุณ"

// 2. ขอสิทธิ์ตอนใช้งาน
import CoreLocation

@Observable
class LocationModel {
    private let manager = CLLocationManager()

    func request() {
        switch manager.authorizationStatus {
        case .notDetermined: manager.requestWhenInUseAuthorization()
        case .denied, .restricted: /* พาไปเปิดในการตั้งค่า */
        default: /* ได้สิทธิ์แล้ว ลุยเลย */
        }
    }
}

// 3. ถ้าถูกปฏิเสธให้จัดการอย่างนุ่มนวล: แจ้งเตือน + พาไปหน้าตั้งค่า
// UIApplication.shared.open(URL(string: UIApplication.openSettingsURLString)!)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ข้อควรระวัง: สิทธิ์บน iOS เป็นแบบ'ถามครั้งเดียว'

{class="mt-1"}
หน้าต่างขอสิทธิ์บน iOS เด้งแค่ครั้งเดียว — ผู้ใช้ปฏิเสธไปแล้วจะไม่เด้งอีกเลย ดังนั้น: จังหวะการขอต้องเลือก'วินาทีที่ผู้ใช้กำลังจะใช้' (ไม่ใช่เปิดแอปปุ๊บเด้งมาเป็นกอง) และข้อความต้องบอกวัตถุประสงค์ ส่วนการชี้ทางในอินเทอร์เฟซหลังถูกปฏิเสธ ('ไปเปิดการระบุตำแหน่งในการตั้งค่า') เป็นอุปกรณ์มาตรฐาน อย่าปล่อยให้ผู้ใช้ติดกับดักตัน ๆ
:::

#### 2. การแจ้งเตือน: พูดสิ่งที่มีประโยชน์ในเวลาที่ถูกต้อง

การแจ้งเตือนคือช่องทางให้แอปเข้าถึงผู้ใช้ และเป็นฟีเจอร์ที่ผู้ใช้'บล็อก'ง่ายที่สุดด้วย iOS ใช้เฟรมเวิร์ก UserNotifications วินัยสามข้อของการส่งแจ้งเตือน: ส่งแต่สิ่งที่มีประโยชน์ ให้ผู้ใช้ปิดได้ และอย่าไปรบกวนกลางดึก การใช้พื้นฐาน:

::: div .code-block
:::inline div .code-head
<span>SWIFT · การแจ้งเตือนในเครื่อง</span><span class="dots">···</span>
:::

```
import UserNotifications

// 1. ขอสิทธิ์แจ้งเตือน (เด้งถามครั้งเดียว)
UNUserNotificationCenter.current()
    .requestAuthorization(options: [.alert, .sound, .badge]) { granted, _ in
        print(granted ? "ได้สิทธิ์แล้ว" : "ถูกปฏิเสธ")
    }

// 2. ตั้งเวลา "ทุกวัน 20:00 เตือนจดบัญชี"
func scheduleDailyReminder() {
    let content = UNMutableNotificationContent()
    content.title = "เตือนจดบัญชี"
    content.body = "วันนี้ยังไม่ได้จดบัญชีนะ"
    content.sound = .default

    var comps = DateComponents()
    comps.hour = 20
    let trigger = UNCalendarNotificationTrigger(dateMatching: comps, repeats: true)

    let request = UNNotificationRequest(
        identifier: "daily-reminder",
        content: content,
        trigger: trigger
    )
    UNUserNotificationCenter.current().add(request)
}
```
:::

ข้อควรระวัง: สิทธิ์การแจ้งเตือนบน iOS ก็'เด้งแค่ครั้งเดียว'เช่นกัน และผู้ใช้ปิดได้ทุกเมื่อในการตั้งค่าระบบ — คุณค่าของเนื้อหาการแจ้งเตือนจึงสำคัญมาก ส่งสะเทือนสักครั้งอาจเสียผู้ใช้ไปตลอดกาล

#### 3. สถาปัตยกรรมขั้นสูง: MVVM แบบลึกและความสามารถในการทดสอบ

บทที่ 65 เราใช้ MVVM มาแล้ว ที่นี่เสริมประเด็นขั้นสูงอีกสามข้อ:

- การแยกส่วนด้วยโปรโตคอล: ให้ ViewModel พึ่งพาโปรโตคอล (protocol) แทนคลาสใดคลาสหนึ่ง — ตอนทดสอบจะฉีด'แหล่งข้อมูลปลอม'เข้าไปได้ นี่คือรากฐานของความสามารถในการทดสอบ
- หนึ่งหน้าที่ต่อหนึ่งตัว: ViewModel หนึ่งตัวดูแลเรื่องเดียว (ที่ทำบัญชีไม่ยุ่งเรื่องอากาศ); ฟีเจอร์เยอะขึ้นเมื่อไหร่แยกออกเมื่อนั้น
- อย่าออกแบบเกินจำเป็น: โปรเจกต์เล็กคนเดียว '@Observable คลาส + การแยกส่วนด้วยโปรโตคอล'ก็พอแล้ว สถาปัตยกรรมหนักอย่าง VIPER หรือ Clean Architecture รอวันที่ทีมและความซับซ้อนมาเคาะประตูค่อยว่ากัน — เครื่องมือเกิดมาเพื่อรับใช้เป้าหมาย ไม่ใช่เพื่ออวด

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
เคล็ดลับ: 'เงินปันผลจากระบบนิเวศ'ของ SwiftUI

{class="mt-1"}
ระบบนิเวศ iOS ยังมีวิธีเล่นขั้นสูงแบบ'มีที่เดียว'อีกสองอย่าง: วิดเจ็ต (WidgetKit) ให้ผู้ใช้ดูข้อมูลได้โดยไม่ต้องเปิดแอป (เอา'ค่าใช้จ่ายเดือนนี้'ของสมุดบัญชีวางบนหน้าจอโฮม) และคำสั่งลัด (App Intents) ให้ผู้ใช้เรียกใช้ฟีเจอร์ของคุณผ่าน Siri หรือระบบอัตโนมัติ ทั้งคู่มีเฟรมเวิร์กทางการรองรับ ต้นทุนการเริ่มต้นไม่สูง แต่เสริมประสบการณ์ผู้ใช้ได้มหาศาล — ระหว่างทางสู่ขั้นสูง ควรปลดล็อกสองตัวนี้ก่อน
:::

#### 4. วิธีเล่นใหม่ปี 2026: พัฒนา iOS โดยมี AI ช่วย

ปี 2026 AI ฝังลึกในขั้นตอนการพัฒนาของ Apple ไปแล้ว ถ้าอยากเร่งความเร็ว ชุดคอมโบนี้สุกงอมเต็มที่แล้ว:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ขั้นตอน</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">AI ช่วยอย่างไร</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">หน้าที่ของคุณ</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เขียนโค้ด</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">โค้ดคอมพลีทในตัวของ Xcode + ปลั๊กอิน AI ภายนอกสร้างให้</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">บรรยายความต้องการให้ชัด แล้วตรวจผลงาน</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ค้นข้อมูล</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">โยนเอกสารทางการและข้อความ error ให้ AI ตีความ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ข้อสรุปสำคัญกลับไปเช็กกับเอกสารทางการ</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เขียนเทสต์</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ให้ AI สร้างเคส XCTest ตามสามประเภท'ปกติ/ขอบเขต/ผิดปกติ'</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ยืนยันว่าเคสสอดคล้องกับความหมายทางธุรกิจ</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">แก้บั๊ก</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">วางล็อกการพัง + โค้ดที่เกี่ยวข้อง ให้ AI หาจุดผิดและแก้ให้</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เข้าใจการแก้ แล้วรันเทสต์ยืนยัน</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
สี่สถานการณ์ของการพัฒนา iOS โดยมี AI ช่วย

วิธีการเชิงละเอียด — สั่ง AI อย่างไร ตรวจรับอย่างไร เลี่ยงหลุมอย่างไร — อยู่ครบ 11 บทในภาคที่ 7 ของหนังสือเล่มนี้'ภาคปฏิบัติเขียนโปรแกรมด้วย AI' (บทที่ 37-47) แนะนำอย่างยิ่งให้อ่านคู่กัน: ไวยากรณ์ Swift ฝากไว้กับภาคนี้ ส่วนเคล็ดวิชาการร่วมงานกับ AI ฝากไว้กับภาคที่ 7

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ลงมือทำ: เติม'สามพี่น้อง'ให้สมุดบัญชี

#### 5. ประเด็นสำคัญของคอนเคอเรนซีใน Swift: @MainActor กับ Task

ระบบคอนเคอเรนซีของ Swift 6 มีกฎสองข้อที่มือใหม่ต้องเข้าใจ:

- อินเทอร์เฟซอัปเดตได้บนเธรดหลักเท่านั้น: วิวของ SwiftUI เป็น @MainActor ตามค่าเริ่มต้น ให้ callback จากเน็ตกลับมาที่เธรดหลักก่อนแล้วค่อยแก้สเตต (await MainActor.run { ... } หรือทำเครื่องหมาย ViewModel เป็น @MainActor)
- งานอะซิงโครนัสจัดการด้วย Task: modifier .task { } เริ่มเองอัตโนมัติเมื่อวิวปรากฏ และยกเลิกเองเมื่อวิวหายไป — นี่คือท่ามาตรฐานการเริ่มงานอะซิงโครนัสใน SwiftUI อย่าเขียน Task มั่ว ๆ เปลือย ๆ ใน body

::: div .code-block
:::inline div .code-head
<span>SWIFT · รูปแบบ async มาตรฐาน</span><span class="dots">···</span>
:::

```
struct WeatherScreen: View {
    @State private var vm = WeatherViewModel()

    var body: some View {
        Group {
            switch vm.state {
            case .loading: ProgressView()
            case .success(let d): WeatherContent(data: d)
            case .error(let m): Text(m)
            }
        }
        .task {                       // โผล่เมื่อไรเริ่มเมื่อนั้น หายเมื่อไรยกเลิกเมื่อนั้น
            await vm.search(city: "ปักกิ่ง")
        }
    }
}
```
:::

เบื้องหลังกฎสองข้อนี้คือการออกแบบ'ปลอดภัยจาก data race'ของ Swift 6 — คอมไพเลอร์จะฟ้องผิดทันทีที่คุณเขียนพลาด ไม่ใช่รอให้แอปพังแล้วค่อยรู้ error จากคอมไพเลอร์ไม่ใช่มาหาเรื่อง แต่มาเบียดกระสุนแทนคุณ

{class="mt-1"}
① เพิ่ม'แจ้งเตือนจดบัญชีทุกวัน 20:00'ให้สมุดบัญชี (สิทธิ์แจ้งเตือน + การแจ้งเตือนในเครื่อง); ② เปลี่ยนแหล่งข้อมูลของ ViewModel เป็นการแยกส่วนด้วยโปรโตคอล และเขียน Unit Test ที่ฉีดข้อมูลปลอมหนึ่งตัว; ③ เพิ่มวิดเจ็ตบนหน้าจอโฮม'ค่าใช้จ่ายเดือนนี้' ทำครบสามพี่น้อง โปรเจกต์ของคุณก็จะมีลุค'ทหารอาชีพ'แล้ว
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
สรุปบทนี้

- สามขั้นของสิทธิ์: ประกาศใน Info.plist (ละไว้คือพังแน่), ขอตอนใช้จริง, ถูกปฏิเสธให้ชี้ทางไปการตั้งค่า
- หน้าต่างขอสิทธิ์ iOS เด้งแค่ครั้งเดียว: เลือกจังหวะ'วินาทีที่กำลังจะใช้'และเขียนข้อความบอกวัตถุประสงค์ให้ชัด
- วินัยสามข้อของการแจ้งเตือน: ส่งแต่ของมีประโยชน์, ปิดได้, ไม่รบกวน; เฟรมเวิร์ก UserNotifications
- MVVM ขั้นสูง: การแยกส่วนด้วยโปรโตคอล (ทดสอบได้), หนึ่งหน้าที่ต่อหนึ่งตัว, ไม่ออกแบบเกินจำเป็น
- เงินปันผลจากระบบนิเวศ: วิดเจ็ต WidgetKit + คำสั่งลัด App Intents
- สี่สถานการณ์ที่ AI ช่วยได้: เขียนโค้ด, ค้นข้อมูล, เขียนเทสต์, แก้บั๊ก; ดูวิธีการในภาคที่ 7 (บทที่ 37-47)
:::
