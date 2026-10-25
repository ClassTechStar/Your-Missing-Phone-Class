---
id: di-liu-shi-yi-zhang
num: 61
part: ios-kai-fa-pian
nav: บทที่ 61: เริ่มต้น Swift อย่างรวดเร็ว — ภาษาหลักของการพัฒนาบน Apple
toc: default
kind: chapter
---

### บทที่ 61: เริ่มต้น Swift อย่างรวดเร็ว — ภาษาหลักของการพัฒนาบนแพลตฟอร์ม Apple

{class="chapter-intro mb-4"}
บทนี้เราจะเรียนภาษากันจริง ๆ แล้ว ไม่ต้องเครียด — Swift มีชื่อเสียงเรื่อง “เป็นมิตรกับมือใหม่” แถมคุณไม่ต้องท่องหนังสือไวยากรณ์: ยึดไวยากรณ์แค่ 20% ก็อ่านเข้าใจและเขียนโค้ดประจำวันได้ถึง 80% ที่เหลือค่อยค้นไปทำโปรเจกต์ไป จำหลักการเรียนของเราไว้: เข้าใจ > จำได้ ใช้เป็น > ชำนาญ

#### 1. ตัวแปรกับชนิดข้อมูล: ตั้งชื่อให้ข้อมูล

โปรแกรมก็คือ “ข้อมูล + ลอจิก” ตัวแปร ก็คือการตั้งชื่อให้ข้อมูลแล้วเก็บไว้ Swift ประกาศด้วย let กับ var:

::: div .code-block
:::inline div .code-head
<span>SWIFT · ตัวแปร</span><span class="dots">···</span>
:::

```
let name = "ซานผวน"        // let: ค่าคงที่ (แนะนำให้ใช้เป็นค่าเริ่มต้น)
var age = 18             // var: ตัวแปร (แก้ภายหลังได้)

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var แก้ได้
// name = "ลี่ซือ"         // <i class="fas fa-times-circle mr-1"></i> let แก้ไม่ได้ คอมไพล์แล้ว error ทันที

let score: Int = 100     // จะเขียนไทป์ชัด ๆ ก็ได้
let pi = 3.14            // ไม่เขียนก็เดาเองได้

print("สวัสดี \(name)")   // สอดข้อความ: เครื่องหมายแบ็กสแลช + วงเล็บ
```
:::

จำชนิดข้อมูลที่ใช้บ่อยด้วยตารางเดียว:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ชนิดข้อมูล</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">เก็บอะไร</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ตัวอย่าง</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">จำนวนเต็ม</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">จำนวนทศนิยม</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ข้อความ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"สวัสดี"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bool</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">จริง/เท็จ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[Int] (อาร์เรย์)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ข้อมูลเป็นชุด</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[1, 2, 3]</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
ชนิดข้อมูลพื้นฐานที่ใช้บ่อยใน Swift

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
เคล็ดลับ: หลัก let มาก่อน

{class="mt-1"}
กฎเหล็กของชุมชน Swift: ค่าเริ่มต้นใช้ let เมื่อจำเป็นจริง ๆ ค่อยใช้ var ถ้าจุดที่ใช้ let ได้แต่ใช้ var ไป Xcode จะเตือนด้วยตัวหนังสือสีเหลือง นิสัยนี้ช่วยตัดบั๊กประเภท “ตัวแปรถูกแก้ไปโดยไม่ตั้งใจ” ได้ทั้งตระกูล — โค้ดยิ่งเปลี่ยนน้อย ยิ่งใช้เหตุผลวิเคราะห์ง่าย
:::

#### 2. Optional: “เครื่องรางกันแอปพัง” ของ Swift

นี่คือแนวคิดที่สำคัญที่สุดของ Swift ไม่มีข้อยกเว้น พูดในประโยคเดียว: เมื่อค่าหนึ่ง “อาจไม่มีอยู่” Swift จะบังคับให้คุณจัดการกับมัน — กำจัด “crash จาก null pointer” อาถรรพ์ของวงการนี้ตั้งแต่ระดับภาษา

::: div .code-block
:::inline div .code-head
<span>SWIFT · Optionals</span><span class="dots">···</span>
:::

```
var name: String = "ซานผวน"   // ไทป์ปกติ: ห้ามเป็น nil เด็ดขาด
// name = nil                // <i class="fas fa-times-circle mr-1"></i> แก้ก่อน ไม่งั้นคอมไพเลอร์ตีกลับทันที

var nickname: String? = nil  // ใส่เครื่องหมายคำถาม: อนุญาตให้เป็น nil (optional)
nickname = "ซานเอ๋อร์"

// ใช้ optional ต้อง "แกะกล่อง" ก่อน:
if let n = nickname {        // if let: แกะแบบปลอดภัย
    print("สวัสดี \(n)")
} else {
    print("ยังไม่มีชื่อเล่น")
}

let len = nickname?.count ?? 0   // ?? ให้ค่าเริ่มต้น (nil coalescing)
print(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ข้อควรรู้: ! คือ “ปฏิบัติการเสี่ยงอันตราย”

{class="mt-1"}
เขียน nickname! ในโค้ด (force unwrap) เท่ากับตะโกนบอกคอมไพเลอร์ว่า “ฉันรับประกันว่ามันไม่ใช่ nil” — พอเดาผิด แอปพังต่อหน้าต่อตา หลักช่วงมือใหม่: พยายามใช้ if let / ?? อย่าใช้ ! บางที Xcode เติมโค้ดให้แล้วแถม ! มาด้วย อย่าลืมเอาออก
:::

#### 3. ฟังก์ชันกับ closure: ห่อลอจิกเป็น “ปุ่มกด”

ฟังก์ชันคือลอจิกที่มีชื่อ อย่างปุ่มบนรีโมต ส่วน closure คือ “ฟังก์ชันไร้ชื่อ” ที่หยิบยื่นให้คนอื่นได้ทันที:

::: div .code-block
:::inline div .code-head
<span>SWIFT · ฟังก์ชันและคลูเซอร์</span><span class="dots">···</span>
:::

```
// ฟังก์ชัน: ชื่อมาก่อน พารามิเตอร์และไทป์คืนค่ามาหลัง
func greet(name: String) -> String {
    return "สวัสดี \(name)!"
}
print(greet(name: "ซานผวน"))     // ตอนเรียกต้องระบุชื่อพารามิเตอร์

// คลูเซอร์: นิยามเลยตรงนั้น กระชับไว
let numbers = [1, 2, 3, 4]
let doubled = numbers.map { $0 * 2 }   // $0 = ตัวปัจจุบัน
// [2, 4, 6, 8]

let big = numbers.filter { $0 > 2 }    // กรอง
// [3, 4]
```
:::

ใน SwiftUI closure อยู่ทุกหนแห่ง: วงเล็บปีกกาหลัง Button("กดฉัน") { ... } ก็คือ closure หนึ่ง map, filter, sorted ท่าคอมโบพวกนี้จำให้แม่น — ต่อจากนี้การประมวลผลลิสต์ 90% ล้วนเป็นการผสมกันของพวกมัน

#### 4. struct กับ protocol: ระบบ “เลโก้” ของ Swift

จุดยืนทางการของ Swift ชัดเจน: ให้ใช้ struct เป็นหลัก ค่อยใช้ class เมื่อต้องการ inheritance โดย struct เป็น “value type” — พอคัดลอกก็แยกกันไปใช้ชีวิตคนละทาง ตัดบั๊กได้ทั้งประเภทโดยธรรมชาติ:

::: div .code-block
:::inline div .code-head
<span>SWIFT · struct และ protocol</span><span class="dots">···</span>
:::

```
// struct: กล่องใส่ข้อมูล
struct Record {
    var id = UUID()
    var amount: Double
    var category: String
    var date: Date

    // struct มี "memberwise initializer" ให้พร้อม: สร้างได้เลย
}
let r = Record(amount: 25.5, category: "อาหาร", date: Date())

// protocol: สัญญาว่า "ต้องมีความสามารถอะไรบ้าง"
protocol Identifiable {
    var id: UUID { get }
}
struct Record: Identifiable { ... }   // เชื่อฟัง protocol = สัญญาว่าจะทำตามที่กำหนด
```
:::

ใน SwiftUI แทบทุกอย่างเป็น struct (View ก็คือ protocol) ประโยคนี้ตอนนี้ไม่เข้าใจก็ไม่เป็นไร บทที่ 62 จะได้เจอกันทุกวัน — ในโลกของ Swift ให้กอด struct ไว้ก่อน

#### 5. การ์ดค้นเร็วไวยากรณ์สำหรับคนเริ่มจากศูนย์

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ต้องการทำอะไร</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">วิธีเขียน</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ประกาศค่าคงที่/ตัวแปร</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">let x = 1</code> / <code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">แทรกค่าลงในสตริง</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"สวัสดี \(name)"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ประกาศฟังก์ชัน</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">func ชื่อฟังก์ชัน(พารามิเตอร์: ชนิดข้อมูล) -> ชนิดค่าที่คืน { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">การเช็คเงื่อนไข</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if เงื่อนไข { ... } else { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">การวนลูป</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for x in อาร์เรย์ { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">การคลายค่าอย่างปลอดภัย</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if let x = ค่าทางเลือก { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ค่าเริ่มต้น</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">x ?? ค่าเริ่มต้น</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">การนิยาม struct</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X { var a: Int; var b: String }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Closure</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">{ $0 * 2 }</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
บัตรค้นเร็วไวยากรณ์ Swift ฉบับมือใหม่

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ลงมือทำ: เล่น Swift ใน Playgrounds 15 นาที

{class="mt-1"}
มี Mac ก็เปิด Xcode → Playground; ไม่มี Mac ก็ใช้ Swift Playgrounds บน iPad หรือสนามซ้อมเวอร์ชันเว็บ รันโค้ดทุกช่วงในบทนี้ให้ครบ ลองแก้ตัวเลขและข้อความดู และตั้งใจทำให้เกิด error สักสองสามครั้งเพื่อดูว่า Xcode จะแจ้งเตือนอย่างไร 15 นาทีของการ'เล่นก่อนเรียน'แบบนี้ จะทำให้คุณเริ่มต้นบทที่ 62 ได้ง่ายขึ้นเท่าตัว
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
สรุปบทนี้

- ใช้ let เป็นหลัก ส่วน var ใช้อย่างระมัดระวัง; ชนิดข้อมูลอนุมานให้เอง หรือจะระบุชัดหลังเครื่องหมายทวิภาค (:) ก็ได้
- Optional คือจิตวิญญาณของ Swift: ค่าที่อาจว่างต้องจัดการให้ครบ if let / ?? คือเครื่องรางของขลัง ส่วน ! คือการเสี่ยงระดับสูง
- การเรียกฟังก์ชันต้องระบุชื่อพารามิเตอร์; Closure คือฟังก์ชันไร้ชื่อ ที่พบได้ทั่วไปใน SwiftUI
- ใช้ struct เป็นหลัก และคอนฟอร์มกับ Protocol; แทบทุกอย่างใน SwiftUI ล้วนเป็น struct
- ไวยากรณ์แค่ 20% ทำงานได้ถึง 80%: ใช้ให้เป็นก่อน แล้วค่อยเชี่ยวชาญ
:::
