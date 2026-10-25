---
id: di-liu-shi-er-zhang
num: 62
part: ios-kai-fa-pian
nav: บทที่ 62: การพัฒนาหน้าจอ — เริ่มต้น SwiftUI
toc: default
kind: chapter
---

### บทที่ 62: การพัฒนาอินเทอร์เฟซ — เริ่มต้นกับ SwiftUI

{class="chapter-intro mb-4"}
อินเทอร์เฟซคือทุกสิ่งที่ผู้ใช้เห็น SwiftUI คือเฟรมเวิร์กอินเทอร์เฟซแบบประกาศ (declarative) ที่ Apple เปิดตัวในปี 2019 — คุณแค่'ประกาศ'ว่าอินเทอร์เฟซหน้าตาเป็นอย่างไร ระบบจะจัดการเรนเดอร์ ปรับให้เข้ากับโหมดมืด และรองรับหน้าจอทุกขนาดให้อัตโนมัติ ถึงปี 2026 SwiftUI กลายเป็นกระแสหลักของโปรเจกต์ใหม่ไปแล้ว ในบทนี้ เราจะมาเรียนรู้การ'วาดภาพ'กัน

#### 1. แนวคิดของ SwiftUI: แบบประกาศ ไม่ใช่แบบสั่ง

การพัฒนาอินเทอร์เฟซแบบเก่าเป็นแบบ'สั่งการ': บอกระบบทีละขั้นว่า'สร้างปุ่ม → วางที่ (20,30) → ตั้งค่าสี' SwiftUI เป็นแบบ'ประกาศ': คุณบรรยายตรง ๆ ว่า'บนอินเทอร์เฟซมีปุ่มสีแดงเขียนว่า "แตะฉัน"' ส่วนจะวาดอย่างไร เมื่อไหร่วาดใหม่ ปล่อยให้ระบบจัดการเอง

::: div .code-block
:::inline div .code-head
<span>SWIFT · วิว SwiftUI แรกของคุณ</span><span class="dots">···</span>
:::

```
import SwiftUI

struct ContentView: View {
    var body: some View {      // body: บอกว่า "หน้าจอหน้าตาเป็นยังไง"
        VStack {               // เรียงตามแนวตั้ง
            Text("สวัสดีชาวโลก!")
                .font(.largeTitle)      // มอดิฟายเออร์: หัวเรื่องใหญ่
            Button("แตะฉัน") {
                print("ถูกแตะแล้ว")
            }
            .buttonStyle(.borderedProminent)  // ปุ่มทึบสีน้ำเงิน
        }
        .padding()
    }
}
```
:::

จุดสำคัญ: วิว = struct ที่คอนฟอร์มกับโปรโตคอล View, พร็อพเพอร์ตี้ body ใช้บรรยายอินเทอร์เฟซ, และ .modifier() ตกแต่งแบบต่อทอดกันเป็นโซ่ นี่คือพื้นฐานทั้งหมดของ SwiftUI

#### 2. วิวพื้นฐาน: ข้อความ ปุ่ม ช่องกรอก รูปภาพ

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">วิว</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ทำหน้าที่อะไร</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ตัวอย่าง</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">แสดงข้อความ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text("สวัสดี")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ปุ่ม</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button("แตะฉัน") { การทำงาน }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ช่องกรอกข้อความ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField("ข้อความนำ", text: $ข้อความ)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">แสดงรูปภาพ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Image(systemName: "star.fill")</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
วิวพื้นฐานทั้ง 4 ของ SwiftUI

สังเกต Image(systemName:) — Apple มีคลังไอคอน SF Symbols ในตัว (ไอคอนฟรีหลายพันตัว) แค่พิมพ์ชื่ออย่าง "star.fill" ก็แสดงดาวทึบได้เลย นี่คือของดีที่ซ่อนอยู่ของการพัฒนา iOS: ทำอินเทอร์เฟซแทบไม่ต้องหาไฟล์ไอคอนเลย

#### 3. ชุดจัดวางสามพี่น้อง: VStack, HStack, ZStack

- VStack: เรียงตามแนวตั้ง (เหมือนต่อแถวรับอาหาร)
- HStack: เรียงตามแนวนอน (เหมือนนั่งเคียงกัน)
- ZStack: วางซ้อนกัน (เหมือนไพ่กองทับกัน เหมาะทำป้ายมุมหรือเลเยอร์บัง)

::: div .code-block
:::inline div .code-head
<span>SWIFT · ชุดสามชิ้นของเลย์เอาต์ + มอดิฟายเออร์ที่ใช้บ่อย</span><span class="dots">···</span>
:::

```
VStack(alignment: .leading, spacing: 12) {
    HStack {
        Text("บิล")
        Spacer()                 // ช่องยืดหยุ่น: ดันฝั่งขวาไปสุด
        Text("-25.5 หยวน").foregroundColor(.red)
    }
    Divider()                    // เส้นแบ่ง
    Text("โน้ต: มื้อกลางวัน")
}
.padding(16)                     // เว้นรอบด้าน
.background(Color(.systemGray6)) // พื้นเทาอ่อน
.cornerRadius(12)                // มุมโค้ง

// ลำดับมอดิฟายเออร์มีผล: padding ก่อน แล้ว background พื้นหลังไม่รวมช่องว่าง
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ข้อควรระวัง: ลำดับของ modifier มีผล

{class="mt-1"}
padding(16).background(สีเทา) กับ background(สีเทา).padding(16) ให้ผลไม่เหมือนกัน — แบบแรกคือ'เว้นระยะก่อนแล้วระบายสี' (พื้นหลังไม่รวมระยะขอบ) ส่วนแบบหลังคือ'ระบายสีก่อนแล้วเว้นระยะ' (พื้นหลังรวมระยะขอบด้วย) ปัญหา'ขอบขาวปริศนา'ที่มือใหม่เจอบ่อยที่สุดก็มาจากจุดนี้ ไม่แน่ใจเมื่อไหร่ให้สลับลำดับดู พรีวิวจะบอกคำตอบทันที
:::

#### 4. สเตตและการไบนด์: ทำให้อินเทอร์เฟซ'มีชีวิต'

อินเทอร์เฟซนิ่ง ๆ ไม่สนุกหรอก กฎของ SwiftUI คือ: อินเทอร์เฟซสะท้อนสเตตอย่างซื่อสัตย์เสมอ พอสเตตเปลี่ยน อินเทอร์เฟซจะวาดใหม่เองอัตโนมัติ

::: div .code-block
:::inline div .code-head
<span>SWIFT · ตัวนับ @State</span><span class="dots">···</span>
:::

```
struct CounterView: View {
    @State private var count = 0   // @State: ค่านี้เปลี่ยนเมื่อไร วาดใหม่เมื่อนั้น

    var body: some View {
        VStack {
            Text("คุณแตะไป \(count) ครั้ง")
            Button("แตะฉัน +1") {
                count += 1          // แก้สเตต หน้าจอเด้งเอง
            }
        }
    }
}
```
:::

ช่องกรอกข้อความต้องใช้'การไบนด์สองทาง' — สัญลักษณ์ $ ส่งทั้ง'ค่าและสิทธิ์แก้ไข'เข้าไปพร้อมกัน:

::: div .code-block
:::inline div .code-head
<span>SWIFT · @Binding ไบนดิ้งสองทาง</span><span class="dots">···</span>
:::

```
struct InputView: View {
    @State private var text = ""

    var body: some View {
        TextField("พิมพ์อะไรก็ได้", text: $text)  // $ ไบนดิ้งสองทาง
            .textFieldStyle(.roundedBorder)
        Text("คุณพิมพ์ว่า: \(text)")   // อัปเดตสด ๆ ระหว่างพิมพ์
    }
}
```
:::

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> ผู้ใช้ดำเนินการ</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> สเตตเปลี่ยน (count += 1)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> SwiftUI ตรวจจับการเปลี่ยนแปลง</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> วาด UI ใหม่อัตโนมัติ (body คำนวณใหม่)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
ภาพที่ 3: การไหลของข้อมูลทางเดียว'สเตต → อินเทอร์เฟซ'ของ SwiftUI
:::

#### 5. พรีวิว ธีม และแอนิเมชัน: 'ไอเทมเสริมพลัง'ของ SwiftUI

- มาโคร #Preview: เพิ่ม #Preview { ContentView() } ไว้ท้ายไฟล์ แคนวาสด้านขวาจะเรนเดอร์แบบเรียลไทม์ — แก้โค้ดปุ๊บเห็นผลปั๊บ ตาเห็นอะไรก็ได้อย่างนั้น
- โหมดมืดได้ฟรี: ใช้สีของระบบ (Color(.systemGray6), .primary) แทนการกำหนดสีตายตัว โหมดมืดจะปรับให้เองอัตโนมัติ ไม่ต้องเขียนเพิ่มแม้แต่บรรทัดเดียว
- แอนิเมชันจบในบรรทัดเดียว: ใช้ withAnimation { count += 1 } หรือใส่ .animation(.default, value: count) ให้วิว — ทรานซิชันลื่นไหลสุด ๆ

::: div .code-block
:::inline div .code-head
<span>SWIFT · แอนิเมชันเรียน 10 นาทีเป็น</span><span class="dots">···</span>
:::

```
struct AnimatedHeartView: View {
    @State private var liked = false

    var body: some View {
        Button {
            withAnimation(.spring(duration: 0.4)) {
                liked.toggle()
            }
        } label: {
            Image(systemName: liked ? "heart.fill" : "heart")
                .font(.system(size: 48))
                .foregroundColor(liked ? .red : .gray)
                .scaleEffect(liked ? 1.3 : 1.0)
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
เคล็ดลับ: ฟังก์ชันมาก่อน แอนิเมชันมาทีหลัง

{class="mt-1"}
โรคที่มือใหม่เป็นกันบ่อยคือ'อินเทอร์เฟซยังทำไม่ถูกเลย แต่ไปเป็นกังวลกับแอนิเมชันเสียก่อน' ให้ฟังก์ชันรันผ่านก่อน แล้วค่อยใส่ลูกเล่นทั้งหมดตอนท้าย — แอนิเมชันคือของตกแต่งให้งานที่ดีอยู่แล้วเด่นขึ้น แต่ฟังก์ชันคือสิ่งที่ช่วยชีวิตตอนยากจนที่สุด นี่ก็คือหลัก'เรียบง่ายเหนือสิ่งอื่นใด'ที่เรายึดมาตลอด
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ลงมือทำ: สร้าง'ปุ่มอารมณ์'

#### 6. สรุป modifier ที่ใช้บ่อย: มีหน้าเดียวในมือ จัดอินเทอร์เฟซได้ไม่ยาก

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">อยากทำอะไร</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Modifier</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เว้นระยะขอบ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.padding(16)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">มุมโค้ง</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cornerRadius(12)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">สีพื้นหลัง</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.background(Color(.systemGray6))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ฟอนต์และขนาดตัวอักษร</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.font(.title.bold())</code> / <code class="inline">.font(.system(size: 20))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">สีพื้นหน้า (ข้อความ/ไอคอน)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.foregroundColor(.red)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">กว้างเต็มจอ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(maxWidth: .infinity)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ขนาดคงที่</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(width:100, height: 44)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">การจัดตำแหน่ง</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack(alignment: .leading)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ความโปร่งใส</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.opacity(0.6)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เงา</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.shadow(radius: 5)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เจสเชอร์การแตะ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.onTapGesture { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ชนิดคีย์บอร์ด</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.keyboardType(.decimalPad)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
สรุป modifier ที่ใช้บ่อยของ SwiftUI

จำไม่ได้ก็ไม่เป็นไร — หน้านี้ไว้เปิดค้นเฉย ๆ จริง ๆ ที่ใช้บ่อยที่สุดมีแค่สี่ตัวแรก: padding, มุมโค้ง, สีพื้นหลัง, ฟอนต์

{class="mt-1"}
ลองแปลงโปรเจกต์เทมเพลตเป็นตัวสลับอารมณ์: มีปุ่มหนึ่งปุ่ม แตะแล้ววนสลับไปมาระหว่าง 😀ดีใจ → 😢เศร้า → 😡โมโห โดยข้อความและสีพื้นหลังเปลี่ยนตาม คำใบ้: ใช้อาร์เรย์เก็บสามชุด (ข้อความ+สี), ใช้ @State เก็บค่าอินเด็กซ์ และเวลาแตะใช้ (index + 1) % 3 ทำเสร็จส่งให้เพื่อนเล่นดู รับคำว้าวแรกว่า "โห ทำแอปเป็นแล้วเหรอ"
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
สรุปบทนี้

- SwiftUI เป็นแบบประกาศ: คุณบรรยายว่า'หน้าตาเป็นอย่างไร' ระบบจัดการวาดและวาดใหม่ให้
- วิว = struct ที่คอนฟอร์มกับโปรโตคอล View; body ใช้บรรยายอินเทอร์เฟซ; modifier ตกแต่งแบบต่อกันเป็นโซ่
- วิวพื้นฐานสี่ตัว: Text / Button / TextField / Image; คลังไอคอน SF Symbols ฟรีเพียบ ใช้ไม่อั้น
- ชุดจัดวางสามพี่น้อง: VStack แนวตั้ง, HStack แนวนอน, ZStack ซ้อนกัน; Spacer คือพื้นที่ยืดหยุ่น
- @State ทำให้อินเทอร์เฟซมีชีวิต; $ ไบนด์สองทางป้อนให้ช่องกรอก
- #Preview เห็นอะไรได้อย่างนั้น; สีของระบบปรับเข้ากับโหมดมืดอัตโนมัติ; withAnimation ใส่ลูกเล่นได้ในบรรทัดเดียว
:::
