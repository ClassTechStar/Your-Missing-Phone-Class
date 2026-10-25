---
id: di-liu-shi-qi-zhang
num: 67
part: ios-kai-fa-pian
nav: บทที่ 67: ขัดเกลาและเผยแพร่ — ขึ้น App Store
toc: default
kind: chapter
---

### บทที่ 67: ขัดเกลาและเผยแพร่ — ทดสอบ ดีบัก และขึ้น App Store

{class="chapter-intro mb-4"}
ทำแอปเสร็จแล้ว แล้วต่อไปล่ะ? บทนี้ตอบสามเรื่องของการไปจาก'รันได้'สู่'ส่งมอบได้': ดีบักหาบั๊กอย่างมีประสิทธิภาพอย่างไร เขียนเทสต์กันบั๊กย้อนกลับอย่างไร และส่งแอปขึ้น App Store ให้ทั่วโลกดาวน์โหลดอย่างไร การขึ้นร้านไม่ใช่แค่พิธีกรรม — มันคือเส้นแบ่งที่เปลี่ยนผลงานชิ้นหนึ่งให้เป็นผลิตภัณฑ์

#### 1. สามท่าเด็ดการดีบัก: print, จุดพัก, พรีวิว

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">เครื่องมือ</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ทำหน้าที่อะไร</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ใช้อย่างไร</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">print + คอนโซล</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ดูล็อกการทำงาน</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ในโค้ดพิมพ์ print("ค่า=\(x)") แล้วดูผลลัพธ์ที่คอนโซลด้านล่างของ Xcode</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">การดีบักด้วยจุดพัก</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ให้โปรแกรมหยุดที่บรรทัดใดบรรทัดหนึ่งเพื่อดูค่าตัวแปร</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">คลิกข้างเลขบรรทัดจะมีตัวหมายสีน้ำเงิน รันถึงจุดนั้นจะหยุด แล้วไล่ทีละขั้น</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">พรีวิว SwiftUI + ดีบักเกอร์</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ดูอินเทอร์เฟซและลำดับชั้นวิวแบบเรียลไทม์</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">แคนวาส #Preview + ตัวตรวจ View Hierarchy ตอนรันจริง</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
สามท่าเด็ดการดีบัก

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
เคล็ดลับ: แอปพังแล้วอ่านอย่างไร?

{class="mt-1"}
ตอน Swift พัง คอนโซลจะพรินต์ "Fatal error" พร้อมสาเหตุ และ Xcode จะหยุดที่บรรทัดที่มีปัญหาพร้อมไฮไลต์ไว้ ประวัติการพังบนเครื่องจริงดูได้ที่ Xcode → Window → Organizer → Crashes (ต้องใช้บัญชีแบบเสียเงิน) ตอนค้นหาให้เอา'ประโยคแรกของสาเหตุ error + swiftui'ไปค้นก่อน — คำถามแม่น คำตอบถึงจะแม่น
:::

#### 2. การทดสอบ: ทำประกันให้โค้ด

การเทสต์ด้วยมือไม่น่าเชื่อถือ — แก้ฟีเจอร์นี้ไป อีกตัวเงียบ ๆ พังไป เทสต์จึงเป็นทั้ง'ยาแก้สำนึก'และ'เสื้อกันกระสุน' iOS ใช้เฟรมเวิร์ก XCTest แบ่งเป็นสองประเภท:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ระดับ</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ทดสอบอะไร</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Target</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ความเร็ว</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Unit Test</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">โลจิกล้วน ๆ (การคำนวณ, การตรวจสอบ)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppTests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ระดับวินาที</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UI Test</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">พฤติกรรมอินเทอร์เฟซจริง</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppUITests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ระดับนาที</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เทสต์ด้วยมือ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ความรู้สึกและประสบการณ์ของคนจริง</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ต้องมีตลอดไป</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
ระดับการทดสอบบน iOS (โปรเจกต์เทมเพลตมี Test Target ให้สองตัวแล้ว)

::: div .code-block
:::inline div .code-head
<span>SWIFT · ตัวอย่าง unit test</span><span class="dots">···</span>
:::

```
import XCTest

// แยกตรรกะ "แปลงข้อความจำนวนเงินเป็นตัวเลข" ออกเป็นฟังก์ชันล้วน
func parseAmount(_ input: String) -> Double? {
    guard let v = Double(input.trimmingCharacters(in: .whitespaces)),
          v > 0 else { return nil }
    return v
}

final class AmountTests: XCTestCase {
    func testEmptyInputReturnsNil() {
        XCTAssertNil(parseAmount(""))
    }
    func testNegativeReturnsNil() {
        XCTAssertNil(parseAmount("-5"))
    }
    func testNormalValueParses() {
        XCTAssertEqual(parseAmount("12.5"), 12.5)
    }
}
```
:::

รันเทสต์: ⌘U ให้เขียวหมดก่อนแล้วค่อยแก้โค้ด ใจก็นิ่ง การตรวจจำนวนเงินและการคำนวณสรุปยอดในสมุดบัญชี ควรมี Unit Test คุ้มกันไว้

#### 3. การเซ็นและแพ็กเกจ: ประทับ'ตรา'ให้แอป

แอป iOS ทุกตัวต้องเซ็นก่อนถึงจะติดตั้งได้ — เพื่อพิสูจน์ว่า'แพ็กเกจนี้มาจากคุณและไม่ถูกแก้ไข' ความสัมพันธ์แบบลำดับชั้น:

- ช่วงเรียน: Apple ID ฟรี + Xcode เซ็นให้อัตโนมัติ (Personal Team) รันบนเครื่องจริงได้ ต้องต่ออายุทุก 7 วัน
- ช่วงเผยแพร่: ต้องใช้บัญชีนักพัฒนาแบบเสียเงิน (99 ดอลลาร์/ปี) ออกใบรับรองและโปรไฟล์จัดเตรียม จึงจะขึ้นร้านและติดตั้งระยะยาวได้

แพ็กเกจ: เมนู Xcode Product → Archive (เก็บถาวร) พอบิลด์เสร็จไปที่ Organizer เลือก Distribute App → เลือก App Store Connect → อัปโหลด การเก็บถาวรต้องตั้งเป้าหมายเป็น Generic iOS Device (ไม่ใช่โปรแกรมจำลอง) นี่คือขั้นตอนที่มือใหม่ลืมบ่อยที่สุด

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
กันพลาด: ใบรับรองหาย = การอัปเดตสะดุด

{class="mt-1"}
ใบรับรองเซ็นและคีย์ส่วนตัวพอหายไป คุณจะส่งอัปเดตให้แอปเก่าไม่ได้อีก — ผู้ใช้จะติดตั้งได้แต่แอป'ใหม่เอี่ยม' สำรองใบรับรองให้ดี (ส่งออก .p12 จากคีย์เชน) และจดรหัสผ่านไว้ให้แน่น โชคดีที่ Apple มี'การเซ็นอัตโนมัติ'และการจัดการใบรับรองผ่านคลาวด์ (ติ๊กเลือก Automatically manage signing ใน Xcode) ช่วยตัดปัญหางานมือไปได้ส่วนใหญ่
:::

#### 4. ขั้นตอนครบวงจรการขึ้น App Store

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> สมัครบัญชีนักพัฒนา</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> เตรียมสื่อสำหรับสโตร์</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> อัปโหลดแพ็กเกจบิลด์</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> กรอกข้อมูลความเป็นส่วนตัวและการรีวิว</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> รีวิวโดย Apple (1-7 วัน)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> เผยแพร่บนสโตร์</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
ภาพที่ 5: ขึ้น App Store หกขั้นตอน
:::

- ลงทะเบียน: developer.apple.com บัญชีบุคคล 99 ดอลลาร์/ปี
- สื่อประกอบ: ไอคอน (1024×1024 อย่าทำมุมโค้ง — Apple ตัดเอง), ภาพหน้าจอ (iPhone ทุกขนาด), คำอธิบาย, ลิงก์นโยบายความเป็นส่วนตัว
- แบบสอบถามความเป็นส่วนตัว: แจ้งตรง ๆ ว่าเก็บข้อมูลอะไรบ้าง — สมุดบัญชีที่ไม่ต่อเน็ตเลือก'ไม่เก็บข้อมูลใด ๆ'ได้
- การรีวิว: ส่งครั้งแรกมักต้องรอ 1-7 วัน ถูกปฏิเสธก็แก้ตาม'หมายเหตุจากทีมรีวิว'ทีละข้อ — เหตุผลการปฏิเสธของ Apple มักเขียนละเอียดมาก ทำตามก็จบ
- TestFlight: ก่อนขึ้นร้านส่งเวอร์ชันทดสอบให้เพื่อนทดลองใช้ก่อน (ได้สูงสุด 10000 คน) เก็บฟีดแบ็กหนึ่งรอบแล้วค่อยส่งจริง ดูมืออาชีพสุด ๆ

#### 5. ทำสื่อหน้าร้านอย่างไร: ความประทับใจแรกคือจำนวนดาวน์โหลด

หน้าร้านคือช่องโชว์ที่ผู้ใช้เห็นตอน'เดินเลือกซื้อ' สื่อสามชิ้นกำหนดความประทับใจแรก:

- ไอคอน: 1024×1024 อย่าใช้ภาพหน้าจอมาแกะโล่ะ ถ้าไม่มีฝีมือออกแบบ ใช้เครื่องมือ AI สร้างกราฟิกเรียบ ๆ สักชิ้น ขอให้ย่อลงบนหน้าจอโฮมแล้วยังมองปุ๊บรู้เรื่องทันทีถึงจะผ่าน
- ภาพหน้าจอ: อย่างน้อย 2 ชุด (ขนาดยอดนิยมของ iPhone) โชว์ฟีเจอร์หลักที่สำคัญที่สุด แต่ละภาพแนบคำโปรยภาษาคนหนึ่งประโยค ('จดหนึ่งรายการในหนึ่งวินาที'ดีกว่า'โซลูชันบันทึกบัญชีที่มีประสิทธิภาพ'สิบเท่า)
- คำอธิบาย: ประโยคแรกบอกให้ชัดว่า'นี่คืออะไร + ทำให้ใครใช้' อย่ากองคำว่า'มืออาชีพที่สุด เก่งที่สุด' — ความจริงใจได้ผลกว่าความเว่อร์

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ลงมือทำ: 'ส่งมอบ'สมุดบัญชีสักหนึ่งครั้ง

#### 6. รายการสั้น ๆ เรื่องการรายงานการพังและการปรับประสิทธิภาพ

ก่อนแอปขึ้นร้าน สองเรื่องนี้คุ้มที่จะใช้เวลาคนละครึ่งชั่วโมง:

##### 1. การเฝ้าระวังการพังของแอป

ตอนคุณทดสอบไม่พัง ไม่ได้แปลว่าในมือถือผู้ใช้จะไม่พัง Apple มีรายงานการพังฟรีใน Xcode Organizer (บัญชีแบบเสียเงินดูล็อกการพังบนเครื่องจริงได้) ทางที่สบายใจกว่าคือต่อ SDK ภายนอก (อย่าง Firebase Crashlytics) ขึ้นร้านโดยไม่มีการเฝ้าระวังการพัง เท่ากับขับรถลืมตาปิด

##### 2. ตรวจประสิทธิภาพเองสี่ข้อ

1. รายการใช้ LazyVStack / List: ลิสต์ยาว ๆ อย่าจัดด้วย VStack ธรรมดาเป็นอันขาด — การโหลดแบบขี้เกียจคือบทเรียนแรกของประสิทธิภาพ
2. รูปอย่ายัดไฟล์ต้นฉบับใหญ่เข้าไป: ใช้ AsyncImage (รูปจากระยะไกล) กับแคชของระบบ ไฟล์ต้นฉบับ 5MB พอจะทำเครื่องรุ่นเก่าค้างทั้งตัว
3. อย่าทำงานหนักบนเธรดหลัก: ทั้งเครือข่ายและไฟล์ใหญ่ให้ผ่าน async/await หมด
4. ใช้ Instruments วัดดู: ตัววิเคราะห์ประสิทธิภาพที่มากับ Xcode (Time Profiler, ตรวจหาหน่วยความจำรั่ว) — วัดก่อน แล้วค่อยปรับ อย่าเชื่อความรู้สึก

{class="mt-1"}
① เพิ่ม Unit Test ให้โลจิกอย่าง parseAmount สามตัว (รัน ⌘U ให้เขียว); ② ใช้จุดพักจับการพังที่ตัวเองสร้างขึ้นเองสักหนึ่งครั้งแล้วแก้ให้ดี; ③ Product → Archive แพ็กเกจหนึ่งชุด ผ่าน TestFlight เชิญเพื่อนมาทดลองใช้; ④ ถ้ามีกำลังเหลือ ลงทะเบียนบัญชีนักพัฒนาแล้วส่งสมุดบัญชีขึ้นร้านจริง ๆ สามขั้นแรกทำเสร็จได้ภายในคืนนี้
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
สรุปบทนี้

- สามท่าเด็ดการดีบัก: ล็อก print, จุดพัก, พรีวิว SwiftUI กับตัวตรวจวิว
- XCTest: Unit Test (⌘U) + UI Test + เทสต์ด้วยมือ เทมเพลตมีให้พร้อมแล้ว
- การเซ็น: บัญชีฟรีเซ็นให้อัตโนมัติ (ต่ออายุทุก 7 วัน); แจกจ่ายจริงต้องใช้บัญชีแบบเสียเงิน
- แพ็กเกจ: Generic iOS Device + Archive + Distribute; สำรองใบรับรองให้แน่นอน
- หกขั้นสู่ร้าน: ลงทะเบียน → สื่อประกอบ → อัปโหลด → แบบสอบถามความเป็นส่วนตัว → รีวิว → วางขาย; ให้ TestFlight ทดลองใช้ก่อน
:::
