---
id: di-liu-shi-wu-zhang
num: 65
part: ios-kai-fa-pian
nav: บทที่ 65: โปรเจกต์ 1 — สมุดบัญชีรายรับรายจ่ายของฉัน (เวอร์ชันในเครื่อง)
toc: default
kind: chapter
---

### บทที่ 65: โปรเจกต์ที่ 1 — สมุดบัญชีของฉัน (เวอร์ชันออฟไลน์)

{class="chapter-intro mb-4"}
ยินดีต้อนรับสู่'โปรเจกต์จริงจัง'แรกของคุณ สมุดบัญชีเล่มนี้แม้ไม่ต่อเน็ต แต่ครบเครื่องภายใน: บันทึกรายการได้ ดูประวัติได้ สรุปรายเดือนได้ ลบและแก้ไขได้ ทำเสร็จ คุณจะได้เดินครบทั้งสายพาน'ข้อมูล → โลจิก → อินเทอร์เฟซ' อย่ารีบก๊อปโค้ด — คิดให้ขึ้นก่อนแล้วค่อยลงมือ นี่คือหลักการของเรามาแต่ต้น

#### 1. คิดความต้องการ: ถามห้าคำถามก่อน

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">องค์ประกอบ</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">คำตอบ</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who (ทำให้ใครใช้)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ใช้เอง ให้ครอบครัวเพื่อนฝูงใช้ก็ได้</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What (ทำอะไร)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">บันทึกรายรับรายจ่าย ดูประวัติ สรุปรายเดือน สถิติตามหมวดหมู่</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why (ทำไม)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ฝึกมือ + ทำให้รู้ว่าเงินหายไปไหน</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How (ทำอย่างไร)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift + SwiftUI + SwiftData + MVVM ทำงานในเครื่องล้วน ๆ ไม่มีแบ็กเอนด์</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint (ข้อจำกัด)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ทำให้เสร็จในหนึ่งสัปดาห์; รองรับขั้นต่ำ iOS 17 (เงื่อนไขของ SwiftData)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
องค์ประกอบความต้องการห้าข้อของสมุดบัญชี

แล้วแตกเป็นขั้นย่อยที่'ทำถึงขั้นไหนก็ใช้ได้': ① สร้างชั้นข้อมูล SwiftData (เก็บรายการหนึ่งได้) ② หน้ารายการ (ดูประวัติได้) ③ ป๊อปอัปบันทึกรายการ (เพิ่มบัญชีได้) ④ ลบและแก้ไข ⑤ การ์ดสรุปรายเดือน ทุกครั้งที่จบหนึ่งขั้น แอปก็ยังเป็น'ของที่ใช้งานได้'เสมอ

#### 2. ชั้นข้อมูล: ให้'บัญชี'มีบ้าน

กำหนดก่อนว่ารายการหนึ่งหน้าตาเป็นอย่างไร — ฟิลด์ต้องพอใช้แต่อย่าโลภเกินจำเป็น:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Record.swift (โมเดล)</span><span class="dots">···</span>
:::

```
import SwiftData

@Model
class Record {
    var type: String      // "income" รายรับ | "expense" รายจ่าย
    var amount: Double    // จำนวนเงิน (หยวน)
    var category: String  // หมวดหมู่: อาหาร เดินทาง เงินเดือน……
    var note: String      // โน้ต (ใส่หรือไม่ก็ได้)
    var date: Date        // วันที่จดบัญชี

    init(type: String, amount: Double, category: String, note: String = "", date: Date = Date()) {
        self.type = type
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
เคล็ดลับ: ทำไมจำนวนเงินใช้ Double?

{class="mt-1"}
แอปการเงินที่เข้มงวดจะใช้ Decimal (ทศนิยมเที่ยงตรง) เพื่อเลี่ยงความคลาดเคลื่อนของทศนิยม (ปัญหาเก่า 0.1+0.2≠0.3) โปรเจกต์ฝึกมือใช้ Double ก็พอ ถ้าวันหนึ่งทำผลิตภัณฑ์การเงินจริง อย่าลืมเปลี่ยนเป็น Decimal หรือ'Int ที่หน่วยเป็นสตางค์' — นี่คือหลุมที่รุ่นพี่นับไม่ถ้วนเคยตกมาแล้ว
:::

#### 3. MVVM: แยกบ้านระหว่างอินเทอร์เฟซกับโลจิก

ให้อินเทอร์เฟซไปจิ้มฐานข้อมูลตรง ๆ? รันได้ แต่โค้ดอินเทอร์เฟซจะยืดยาวและรกมั่ว สถาปัตยกรรม MVVM แบ่งหน้าที่ชัดเจน: View (อินเทอร์เฟซ) สนใจแค่การวาด, ViewModel (ศูนย์กลางโลจิก) ดูแลข้อมูล, Model (SwiftData) ดูแลการจัดเก็บ

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View (UI ฝั่ง SwiftUI)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel (ศูนย์กลางตรรกะ @Observable)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model (ชั้นข้อมูล SwiftData)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
ภาพที่ 4: โครงสร้างสามชั้นของ MVVM — ข้อมูลไหลทางเดียว แต่ละชั้นไม่ล้ำเขตกัน
:::

::: div .code-block
:::inline div .code-head
<span>SWIFT · RecordViewModel.swift (โครง)</span><span class="dots">···</span>
:::

```
import Observation

@Observable
class RecordViewModel {
    var records: [Record] = []
    private let context: ModelContext

    init(context: ModelContext) { self.context = context }

    func load() {
        // กรองและเรียงด้วย #Predicate ของ SwiftData
        let descriptor = FetchDescriptor<Record>(
            sortBy: [SortDescriptor(\.date, order: .reverse)]
        )
        records = (try? context.fetch(descriptor)) ?? []
    }

    func add(type: String, amount: Double, category: String, note: String) {
        let r = Record(type: type, amount: amount, category: category, note: note)
        context.insert(r)
        try? context.save()
        load()                       // โหลดใหม่ หน้าจอจะเด้งตาม
    }

    func delete(_ record: Record) {
        context.delete(record)
        try? context.save()
        load()
    }
}
```
:::

ในอินเทอร์เฟซเขียน @State private var vm = RecordViewModel(...) แล้วดึง vm.records มาเรนเดอร์รายการตรง ๆ — ข้อมูลเปลี่ยนเมื่อไหร่ อินเทอร์เฟซรีเฟรชให้เอง

#### 4. อินเทอร์เฟซ: หน้ารายการ + ป๊อปอัปบันทึก

::: div .code-block
:::inline div .code-head
<span>SWIFT · หน้ารายการบันทึกบัญชี (ส่วนสำคัญ)</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var vm: RecordViewModel
    @State private var showAdd = false

    var body: some View {
        NavigationStack {
            List {
                Section("ยอดคงเหลือเดือนนี้") {          // การ์ดสรุป
                    SummaryRow(records: vm.records)
                }
                Section("เดินบัญชี") {
                    ForEach(vm.records) { r in
                        RecordRow(record: r)
                    }
                    .onDelete { idx in
                        idx.forEach { vm.delete(vm.records[$0]) }
                    }
                }
            }
            .navigationTitle("สมุดบัญชีของฉัน")
            .toolbar {
                Button { showAdd = true } label: {
                    Image(systemName: "plus")
                }
            }
            .sheet(isPresented: $showAdd) {
                AddRecordView(vm: vm)          // กล่องบันทึก
            }
        }
    }
}
```
:::

ประเด็นสำคัญของป๊อปอัปบันทึก: คีย์บอร์ดช่องจำนวนเงินใช้ .keyboardType(.decimalPad) (คีย์บอร์ดตัวเลข), รายรับ/รายจ่ายใช้ตัวเลือกแบบแบ่งส่วน (Picker), หมวดหมู่เลือกผ่านเมนู, กด'บันทึก'แล้วเรียก vm.add(...) พร้อม dismiss() ปิดหน้าต่าง

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ข้อควรระวัง: อย่าขี้เกียจตรวจค่าที่กรอก

{class="mt-1"}
ช่องจำนวนเงินต้องตรวจสอบเสมอ: ค่าว่าง ค่าติดลบ และอินพุตผิดประเภทอย่าง "abc" ต้องดักให้หมด (ใช้ Double(text) ตรวจ ถ้าแปลงไม่ได้จะได้ nil) สาเหตุที่แอปพังบ่อยที่สุดอย่างหนึ่งคือ'ถือว่าอินพุตของผู้ใช้เป็นเด็กดี' จดไว้: ทุกอย่างที่ผู้ใช้กรอก ให้ตรวจอย่างผู้ตรวจเข้มงวดที่สุด
:::

#### 5. แก้ไข ลบ และสรุปยอด

- ลบ: ใช้ .onDelete ของ List ปัดซ้ายเพื่อลบ + ป๊อปอัปยืนยัน (การลบพลาดคือสิ่งที่ผู้ใช้แอปบัญชีเกลียดที่สุด)
- แก้ไข: แตะแถวเข้าป๊อปอัปแก้ไข กรอกค่าเดิมไว้ให้ก่อน (แก้ตัวอักษรเดียวง่ายกว่าพิมพ์ใหม่ทั้งชุด)
- สรุปยอด: ใช้ filter + reduce คำนวณ'รายรับ / รายจ่าย / ยอดคงเหลือเดือนนี้' แสดงบนการ์ดด้านบน:

::: div .code-block
:::inline div .code-head
<span>SWIFT · คำนวณสรุปรายเดือน</span><span class="dots">···</span>
:::

```
func monthSummary(_ records: [Record]) -> (income: Double, expense: Double) {
    let cal = Calendar.current
    let monthRecords = records.filter {
        cal.isDate($0.date, equalTo: Date(), toGranularity: .month)
    }
    let income = monthRecords
        .filter { $0.type == "income" }
        .reduce(0) { $0 + $1.amount }
    let expense = monthRecords
        .filter { $0.type == "expense" }
        .reduce(0) { $0 + $1.amount }
    return (income, expense)
}
```
:::

#### 6. การตรวจรับ: ตรวจสามชั้น + โจทย์ท้าทายขั้นสูงสองข้อ

ทำโปรเจกต์เสร็จแล้ว ตรวจรับสามชั้นตามลำดับ'ฟังก์ชัน → ขอบเขต → สถาปัตยกรรม': บันทึกได้ไหม ลบได้ไหม ปิดแอปเปิดใหม่ข้อมูลยังอยู่ไหม (ฟังก์ชัน); กรอกจำนวนเงิน 0 หรือติดลบแล้วแอปพังไหม (ขอบเขต); อินเทอร์เฟซกับข้อมูลปนกันหรือเปล่า ฟิลด์ถูก hardcode หรือเปล่า (สถาปัตยกรรม)

ผ่านการตรวจรับเวอร์ชันพื้นฐานแล้ว เพิ่ม'เมนูขั้นสูง'ให้ตัวเองอีกสองอย่าง:

1. สถิติตามหมวดหมู่: เพิ่มแท็บ'สถิติ' ใช้ Swift Charts วาดค่าใช้จ่ายตามหมวดเป็นแผนภูมิวงกลม/แผนภูมิแท่ง — ไลบรารีกราฟทางการของ Apple เขียนโค้ดไม่กี่บรรทัดก็ได้กราฟ
2. ซิงก์ iCloud: เปิดซิงก์ iCloud ใน SwiftData ต้องตั้งค่าแค่ไม่กี่ข้อ — สมุดบัญชีจะซิงก์อัตโนมัติระหว่าง iPhone/iPad ดู'ระดับพรีเมียม'ขึ้นทันที

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ลงมือทำ: ทำให้เสร็จภายในสัปดาห์นี้

{class="mt-1"}
ลงมือตามลำดับ'ชั้นข้อมูล → ViewModel → หน้ารายการ → ป๊อปอัปบันทึก → การ์ดสรุปยอด' วันละหนึ่งขั้น ติดขัดเมื่อไหร่ก็เอาข้อความ error ตามตัวไปให้เสิร์ชเอนจินหรือ AI (ยังจำภาคที่ 7 'ภาคปฏิบัติเขียนโปรแกรมด้วย AI' ได้ไหม? อธิบายปัญหาให้ชัดว่า'พฤติกรรมที่คาดหวัง พฤติกรรมที่เกิดขึ้นจริง ขั้นตอนทำซ้ำ') ทำเสร็จแล้วใช้มันจดบัญชีสัปดาห์หนึ่ง — ได้ใช้แอปที่ตัวเองสร้างเอง ความภูมิใจจะดันให้คุณเดินต่อไปเอง
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
สรุปบทนี้

- องค์ประกอบความต้องการห้าข้อ → แตกเป็นขั้นย่อยที่'ทำถึงขั้นไหนก็ใช้ได้' แล้วค่อยลงมือ
- ชั้นข้อมูล: โมเดล @Model + คอนเทนเนอร์ modelContainer + คิวรี FetchDescriptor
- แบ่งงาน MVVM: View สนใจแค่วาด, ViewModel แบบ @Observable ดูแลโลจิก, SwiftData ดูแลการจัดเก็บ
- อินเทอร์เฟซ: List + Section + toolbar + sheet ป๊อปอัปบันทึกรายการ
- ตรวจรับสามชั้น (ฟังก์ชัน/ขอบเขต/สถาปัตยกรรม) + โจทย์ท้าทายขั้นสูง (Swift Charts, ซิงก์ iCloud)
:::
