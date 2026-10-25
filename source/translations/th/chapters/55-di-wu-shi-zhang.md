---
id: di-wu-shi-zhang
num: 50
part: an-zhuo-kai-fa-pian
nav: บทที่ 50: เริ่มต้น Kotlin อย่างรวดเร็ว — ภาษาหลักของการพัฒนา Android
toc: default
kind: chapter
---

### บทที่ 50: เริ่มต้น Kotlin อย่างรวดเร็ว — ภาษาหลักของการพัฒนา Android

{class="chapter-intro mb-4"}
บทนี้เราจะเริ่มเรียนภาษากันจริงจัง ไม่ต้องเครียด — Kotlin ขึ้นชื่อว่า "เป็นมิตรกับมือใหม่" แถมคุณไม่ต้องท่องหนังสือไวยากรณ์: แค่เข้าใจไวยากรณ์ 20% แรก ก็อ่านรู้เรื่องและเขียนโค้ดประจำวันได้ถึง 80% ส่วนที่เหลือค่อยค้นระหว่างทำโปรเจกต์ไป จำหลักการเรียนของเราไว้: เข้าใจ > ท่องจำ ใช้เป็น > ชำนาญ

#### 1. ตัวแปรกับชนิดข้อมูล: ตั้งชื่อให้ข้อมูล

โปรแกรมก็คือ "ข้อมูล + ตรรกะ" ตัวแปร ก็คือการตั้งชื่อให้ข้อมูลแล้วเก็บไว้ Kotlin มีสองวิธีประกาศ:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · ตัวแปร</span><span class="dots">···</span>
:::

```
val name = "ซานผวน"        // val: ตัวแปรอ่านอย่างเดียว (แนะนำให้ใช้เป็นค่าเริ่มต้น)
var age = 18             // var: ตัวแปรแก้ได้ (ภายหลังเปลี่ยนได้)

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var แก้ได้
// name = "ลี่ซือ"         // <i class="fas fa-times-circle mr-1"></i> val แก้ไม่ได้ คอมไพล์แล้ว error ทันที

val score: Int = 100     // จะเขียนไทป์ชัด ๆ ก็ได้
val pi = 3.14            // ไม่เขียนก็เดาเองได้
```
:::

ชนิดที่ใช้บ่อยมีแค่ไม่กี่ตัว จำจากตารางเดียวจบ:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ชนิด</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">เก็บอะไร</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ตัวอย่าง</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">จำนวนเต็ม</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ทศนิยม</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ข้อความ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"สวัสดี"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Boolean</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">จริง/เท็จ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List&lt; T&gt;</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ชุดข้อมูล</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">listOf(1, 2, 3)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
ชนิดข้อมูลพื้นฐานที่ใช้บ่อยใน Kotlin

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
เคล็ดลับ: หลัก val มาก่อน

{class="mt-1"}
กฎเหล็กของชุมชน Kotlin: ใช้ val เป็นค่าเริ่มต้น จะใช้ var เมื่อจำเป็นจริง ๆ ถ้าที่ที่ใช้ val ได้แล้วไปใช้ var IDE จะเตือนด้วยตัวเหลือง นิสัยนี้ช่วยตัดบั๊กกลุ่มใหญ่ "ตัวแปรถูกแก้โดยไม่ตั้งใจ" ทิ้งได้ — โค้ดยิ่งมีจุดเปลี่ยนน้อย ยิ่งไล่เหตุผลง่าย
:::

#### 2. ฟังก์ชัน: รวมตรรกะเป็น "ปุ่ม" พร้อมกด

ฟังก์ชันคือตรรกะชิ้นหนึ่งที่มีชื่อ เหมือนปุ่มบนรีโมต — กดหนึ่งที (เรียกใช้) ก็ทำชุดการกระทำต่อให้ทั้งหมด ใน Kotlin ประกาศด้วย fun:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · ฟังก์ชัน</span><span class="dots">···</span>
:::

```
fun greet(name: String): String {
    return "สวัสดี $name!"     // เครื่องหมาย $ สอดตัวแปรลงในข้อความ
}

println(greet("ซานผวน"))        // ผลลัพธ์: สวัสดี ซานผวน!

// ฟังก์ชันบรรทัดเดียวเขียนเป็น expression ได้
fun add(a: Int, b: Int) = a + b

println(add(3, 5))            // ผลลัพธ์: 8
```
:::

จุดที่ต้องรู้มีดังนี้: พารามิเตอร์เขียนในวงเล็บ (ชื่อมาก่อน ชนิดมาหลัง คั่นด้วยทวิภาค); ชนิดค่าที่ส่งกลับเขียนหลังวงเล็บ; สตริงเทมเพลต $ชื่อตัวแปร คือของเด่นสะดวกสบายของ Kotlin — ไม่ต้องเอา "สตริง + ตัวแปร" มาต่อกันแบบ Java อีกแล้ว

#### 3. เงื่อนไขกับลูป: ทำให้โปรแกรม "คิด" เป็น

ความฉลาดของโปรแกรมมาจากสองเรื่อง: ตัดสินใจเป็น (if/when) กับทำซ้ำเป็น (for/while)

::: div .code-block
:::inline div .code-head
<span>KOTLIN · เงื่อนไขและลูป</span><span class="dots">···</span>
:::

```
// การเช็คเงื่อนไข: if / else
val age = 17
if (age >= 18) {
    println("ผู้ใหญ่")
} else {
    println("ผู้เยาว์")
}

// หลายทางเลือก: when (ใช้ดีกว่า switch ร้อยเท่า)
val score = 85
val level = when {
    score >= 90 -> "ดีเยี่ยม"
    score >= 60 -> "ผ่าน"
    else -> "สู้ ๆ เข้าละ!"
}

// ทำซ้ำ: ลูป for
val fruits = listOf("แอปเปิล", "กล้วย", "ส้ม")
for (fruit in fruits) {
    println("ฉันชอบกิน$fruit")
}
```
:::

when คือรูปแบบหลายทางเลือกที่ใช้บ่อยที่สุดใน Kotlin งานพัฒนา Android คุณจะได้ใช้มันทุกวัน (เช่น แสดงหน้าจอต่างกันตามสถานะ)

#### 4. Null Safety: "เครื่องรางกันตาย" ของ Kotlin

บั๊กที่ดังที่สุดยุค Java ชื่อ NullPointerException — โปรแกรมเผลอไปเข้าถึงสิ่งที่ "ไม่มีอะไรเลย" แล้วดับทันที ตามสถิติมันครองอันดับหนึ่งบนกระดานแอป Android พังมาหลายปีติดต่อกัน Kotlin แก้ปัญหานี้ตั้งแต่ระดับภาษา: โดยปริยายห้ามค่า null

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Null Safety</span><span class="dots">···</span>
:::

```
var name: String = "ซานผวน"   // ไทป์ปกติ: ห้ามเป็น null เด็ดขาด
// name = null                // <i class="fas fa-times-circle mr-1"></i> แก้ก่อน ไม่งั้นคอมไพเลอร์ตีกลับทันที

var nickname: String? = null // ใส่เครื่องหมายคำถาม: อนุญาตให้เป็น null
nickname = "ซานเอ๋อร์"

// ใช้ nullable type ต้องจัดการอย่างปลอดภัย:
println(nickname?.length)    // safe call: เป็น null ก็คืน null ไม่เด้ง
val len = nickname?.length ?: 0   // Elvis operator: เป็น null ก็ให้ค่าเริ่มต้น
println(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ข้อควรรู้: อย่าสับสนระหว่าง ? กับ ?:

{class="mt-1"}
String? คือ "อนุญาตให้เป็น null ได้" ส่วน a ?: b คือ "ถ้า a เป็น null ให้ใช้ b" (หน้าตาเหมือนทรงผมเอลวิส เลยเรียกกันว่า Elvis operator) ช่วงแรกที่เขียนโค้ด พอเห็นคอมไพเลอร์ฟ้อง "error เรื่อง null" แปดทับสิบคือคุณลืมจัดการชนิดที่เป็น null ได้ — นั่นแหละคือภาษากำลังคุ้มครองคุณอยู่
:::

#### 5. คลาสกับอ็อบเจกต์: แม่พิมพ์สำหรับ "หล่อชิ้นส่วน"

คลาสคือ "แม่พิมพ์" ของอ็อบเจกต์ อ็อบเจกต์คือ "ชิ้นงานจริง" ที่หล่อจากคลาส ทุกอย่างใน Android — หน้าจอ ปุ่ม ข้อมูล — ล้วนเป็นอ็อบเจกต์ ใน Kotlin มีของวิเศษชื่อ data class (คลาสข้อมูล) ทำหน้าที่ "ใส่ข้อมูล" โดยเฉพาะ หนึ่งบรรทัดแทน Java ได้หลายสิบบรรทัด:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · คลาสและ data class</span><span class="dots">···</span>
:::

```
// คลาสปกติ: แม่พิมพ์
class Dog(val name: String) {
    fun bark() = println("$name ฮ่อง ฮ่อง!")
}

val dog = Dog("โอ้เจ้า")      // สร้างออบเจกต์
dog.bark()                 // โอ้เจ้า ฮ่อง ฮ่อง!

// data class: กล่องใส่ข้อมูล (มี equals/copy ให้พร้อม)
data class User(val id: Int, val name: String, val email: String)

val me = User(1, "ซานผวน", "zhangsan@example.com")
val twin = me.copy(name = "ซานซานเฟิง")   // คัดลอกแล้วแก้ค่าเดียว
```
:::

ต่อไปถ้าคุณทำแอปบันทึกบัญชี หนึ่งรายการก็คือ data class หนึ่งตัว: data class Record(val amount: Double, val category: String, val date: String) เห็นไหมล่ะ คุณเขียนโครงสร้างโค้ดระดับโปรเจกต์จริงได้แล้ว

#### 6. lambda กับ high-order function: "น้ำตาลไวยากรณ์" ของ Kotlin

ในโค้ด Android คุณจะเจอ "ฟังก์ชันไร้ชื่อ" แบบ { ... } ทุกวัน มันชื่อ lambda (ฟังก์ชันนิรนาม) onClick = { count++ } ของ Button ก็คือ lambda หนึ่งตัว — ห่อ "กดแล้วทำอะไร" เป็นแพ็กเดียว แล้วส่งต่อให้ปุ่มไป

::: div .code-block
:::inline div .code-head
<span>KOTLIN · เริ่มต้นกับ lambda</span><span class="dots">···</span>
:::

```
// แบบปกติ: นิยามฟังก์ชันมีชื่อก่อนแล้วค่อยส่งเข้าไป
fun double(x: Int) = x * 2
val result = listOf(1, 2, 3).map(::double)

// สไตล์ lambda: นิยามเลยตรงนั้น กระชับไว
val result2 = listOf(1, 2, 3).map { it * 2 }   // it = ตัวปัจจุบัน

// กรอง + แปลงต่อกัน (เจอบ่อยมากในโปรเจกต์จริง)
val bills = listOf(12.5, 88.0, 5.0, 200.0)
val bigBills = bills.filter { it > 50 }.sorted()
// [88.0, 200.0]—"บิลที่เกิน 50 เรียงให้เรียบร้อย"
```
:::

จำคอมโบ "คอลเลกชัน" ที่ใช้บ่อยไว้หน่อย: filter (กรอง), map (แปลง), sorted (เรียง), sum (รวม) งานจัดการลิสต์ของคุณในอนาคต 90% คือการผสมสี่ท่านี้ ปรัชญาของ Kotlin คือ: ตรรกะที่อธิบายให้ชัดได้ในหนึ่งประโยค ห้ามเขียนกินห้าประโยค

#### 7. การ์ดสรุปไวยากรณ์ฉบับคนเริ่มจากศูนย์

อย่าหวังท่องไวยากรณ์ทั้งหมดให้จบในหนึ่งวัน เก็บการ์ดนี้ไว้ ตอนเขียนโค้ดค่อยเปิดเทียบดู อีกสองสัปดาห์ก็คุ้นมือเอง:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ต้องการทำอะไร</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">วิธีเขียน</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ประกาศตัวแปรแบบอ่านอย่างเดียว</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">val x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ประกาศตัวแปรแบบแก้ได้</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ประกาศฟังก์ชัน</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">fun ชื่อ(พารามิเตอร์): ชนิดค่าที่ส่งกลับ { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เช็กเงื่อนไข</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if (เงื่อนไข) {...} else {...}</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">หลายทางเลือก</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">when { เงื่อนไข -> ผลลัพธ์ }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">วนลูป</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for (x in ลิสต์) { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ต่อข้อความ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"สวัสดี $name"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">จัดการค่าที่อาจเป็น null</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">x?.length ?: 0</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ประกาศ data class</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">data class X(val a: Int, val b: String)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
การ์ดสรุปไวยากรณ์ Kotlin (ฉบับมือใหม่)

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ลงมือทำด้วยกัน: เล่น Kotlin 10 นาที โดยไม่ต้องติดตั้งอะไรเลย

{class="mt-1"}
เปิดเบราว์เซอร์ไปที่ play.kotlinlang.org (สนามซ้อมออนไลน์อย่างเป็นทางการของ Kotlin) แล้วเอาโค้ดแต่ละช่วงในบทนี้ไปวางรันดูทีละชุด ลองเปลี่ยนตัวเลขกับข้อความดูว่าผลลัพธ์เปลี่ยนยังไง 10 นาทีแบบ "เล่นก่อนเรียน" นี้ จะทำให้คุณเริ่มบทที่ 51 ได้ง่ายขึ้นเท่าตัว
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
สรุปบทนี้

- val มาก่อน ใช้ var อย่างระวัง; ชนิดข้อมูลอนุมานให้เองได้ หรือประกาศชัดหลังทวิภาคก็ได้
- ฟังก์ชัน = ตรรกะที่ห่อไว้พร้อมใช้; สตริงเทมเพลต $ คือของเด่นสะดวกสบาย
- if/when ไว้ตัดสินใจ for ไว้วนลูป; when คือ "ผู้รอบด้าน" ของงานพัฒนา Android
- null safety คือเครื่องรางกันตายของ Kotlin: ชนิดปกติปฏิเสธ null ส่วนชนิดที่เป็น null ได้ต้องจัดการด้วย ? / ?:
- data class คือกล่องใส่ข้อมูล หนึ่งฟิลด์ต่อหนึ่งบรรทัด โปรเจกต์จริงใช้ทุกวัน
- ไวยากรณ์ 20% ทำงานได้ 80%: ใช้เป็นก่อน แล้วค่อยไปลุ้นความชำนาญ
:::
