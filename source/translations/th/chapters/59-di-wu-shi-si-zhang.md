---
id: di-wu-shi-si-zhang
num: 54
part: an-zhuo-kai-fa-pian
nav: บทที่ 54: โปรเจกต์ 1 — สมุดบัญชีรายรับรายจ่ายของฉัน (เวอร์ชันในเครื่อง)
toc: default
kind: chapter
---

### บทที่ 54: โปรเจกต์ที่ 1 — แอปบันทึกรายรับรายจ่ายของฉัน (เวอร์ชันออฟไลน์)

{class="chapter-intro mb-4"}
ยินดีต้อนรับสู่ "โปรเจกต์จริงจัง" แรกของคุณ แอปบันทึกบัญชีนี้แม้ไม่ต่อเน็ต แต่อวัยวะครบทุกชิ้น: บันทึกรายการได้ ดูประวัติได้ สรุปสถิติรายเดือนได้ ลบแก้ได้ ทำเสร็จ คุณก็เดินครบวงจร "ข้อมูล → ตรรกะ → หน้าจอ" อย่างสมบูรณ์ อย่ารีบก๊อปโค้ด — คิดให้ขาดก่อนแล้วค่อยลงมือ นี่คือหลักการประจำตัวของเรา

#### 1. คิดความต้องการ: ถามห้าคำถามก่อน

ก่อนลงมือ ใช้ "ห้าองค์ประกอบของความต้องการ" ร้อยเรียงความคิดให้ชัด:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">องค์ประกอบ</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">คำตอบ</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who (ให้ใครใช้)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ใช้เอง ครอบครัวเพื่อนฝูงก็ได้</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What (ทำอะไร)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">บันทึกรายรับรายจ่าย ดูประวัติ สรุปรายเดือน สถิติตามหมวด</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why (ทำไม)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ฝึกมือ + รู้ว่าเงินหายไปไหน</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How (ทำยังไง)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin + Compose + Room + MVVM ล้วนทำงานในเครื่อง ไม่มีแบ็กเอนด์</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint (ข้อจำกัด)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ทำให้เสร็จในหนึ่งสัปดาห์; รองรับขั้นต่ำ Android 8; แม้ยังไม่ขึ้นสโตร์ก็เขียนตามมาตรฐานขึ้นสโตร์ไว้ก่อน</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
ห้าองค์ประกอบความต้องการของแอปบันทึกบัญชี

แล้วแตกเป็นขั้นย่อยแบบ "ทีละขั้นก็ใช้ได้": 1) สร้างชั้นข้อมูล Room (เก็บรายการหนึ่งได้); 2) หน้ารายการ (ดูประวัติได้); 3) หน้าเพิ่มรายการ (เพิ่มรายการได้); 4) ลบกับแก้ไข; 5) การ์ดสรุปรายเดือน ทุกครั้งที่จบหนึ่งขั้น แอปก็เป็น "สิ่งที่ใช้ได้จริง"

#### 2. ชั้นข้อมูล: ให้ "รายการ" มีบ้าน

นิยามก่อนว่ารายการหนึ่งหน้าตาเป็นยังไง — ฟิลด์พอใช้ก็พอ อย่าโลภเยอะ:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Record.kt (Entity)</span><span class="dots">···</span>
:::

```
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val type: String,        // "income" รายรับ | "expense" รายจ่าย
    val amount: Double,      // จำนวนเงิน (หยวน)
    val category: String,    // หมวดหมู่: อาหาร เดินทาง เงินเดือน……
    val note: String = "",   // โน้ต (ใส่หรือไม่ก็ได้)
    val date: String         // "2026-08-15"
)
```
:::

เพิ่มคิวรีสอย่างไว้ "ใช้ทำสถิติ" ใน Dao — นี่คือดวงวิญญาณของแอปบันทึกบัญชี:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordDao.kt (คิวรีสถิติ)</span><span class="dots">···</span>
:::

```
@Dao
interface RecordDao {
    @Query("SELECT * FROM records ORDER BY date DESC, id DESC")
    fun getAll(): Flow&lt;List&lt;Record&gt;&gt;

    @Insert
    suspend fun insert(record: Record)

    @Delete
    suspend fun delete(record: Record)

    @Query("SELECT COALESCE(SUM(amount),0) FROM records WHERE type='income' AND date LIKE :month || '%'")
    suspend fun monthIncome(month: String): Double   // month หน้าตาแบบนี้ "2026-08"

    @Query("SELECT COALESCE(SUM(amount),0) FROM records WHERE type='expense' AND date LIKE :month || '%'")
    suspend fun monthExpense(month: String): Double
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
เคล็ดลับ: ทำไมยอดเงินใช้ Double?

{class="mt-1"}
แอปการเงินที่เข้มงวดจะใช้ BigDecimal หรือ "Int โดยนับหน่วยย่อยสุด" เพื่อเลี่ยงความคลาดเคลื่อนของทศนิยม (ปัญหาคลาสสิก 0.1+0.2≠0.3) โปรเจกต์ฝึกมือใช้ Double ก็พอ ส่วนวันหนึ่งถ้าทำของจริงด้านการเงิน อย่าลืมเปลี่ยนเป็นนับหน่วยย่อยสุด — โพรงนี้รุ่นพี่หลายคนเคยหล่นลงไปแล้ว
:::

#### 3. MVVM: แยกบ้านระหว่างหน้าจอกับตรรกะ

ให้หน้าจอไปยุ่งฐานข้อมูลโดยตรงเลย? รันได้ แต่โค้ดหน้าจอจะยาวเหยียดและอ่านทรมาน สถาปัตยกรรม MVVM แบ่งหน้าที่กันชัด: View (หน้าจอ) สนใจแค่วาด, ViewModel (ศูนย์กลางตรรกะ) ดูแลข้อมูล, Model (Room) ดูแลการจัดเก็บ

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View (UI ฝั่ง Compose)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel (สเตตและตรรกะ)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model (ชั้นข้อมูล Room)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
ภาพที่ 5: โครงสร้างสามชั้นของ MVVM — ข้อมูลไหลทางเดียว แต่ละชั้นไม่ล้ำเขตกัน
:::

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordViewModel.kt (โครง)</span><span class="dots">···</span>
:::

```
class RecordViewModel(private val dao: RecordDao) : ViewModel() {

    // แปลง Flow เป็นสเตตที่ UI เฝ้าดูได้
    val records = dao.getAll()
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(), emptyList())

    // การกระทำของผู้ใช้: เรียกฟังก์ชัน suspend
    fun addRecord(type: String, amount: Double, category: String, note: String, date: String) {
        viewModelScope.launch {
            dao.insert(Record(type = type, amount = amount,
                category = category, note = note, date = date))
        }
    }

    fun deleteRecord(record: Record) {
        viewModelScope.launch { dao.delete(record) }
    }
}
```
:::

ในหน้าจอ (Compose) ใช้แบบนี้: val vm: RecordViewModel = viewModel() แล้ว val list by vm.records.collectAsState() — ข้อมูลเปลี่ยนเมื่อไร ลิสต์รีเฟรชเอง คุณไม่ต้องทำอะไรเลย นี่คือพลังเมื่อ MVVM + Flow + Compose สามเครื่องมือรวมพลังกัน

#### 4. หน้าจอ: หน้ารายการ + หน้าเพิ่มรายการ

หน้ารายการใช้ LazyColumn (ลิสต์โหลดเท่าที่จำเป็น) — ข้อมูลเยอะแค่ไหนก็ไม่กระตุก:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · หน้ารายการบันทึกบัญชี (ส่วนสำคัญ)</span><span class="dots">···</span>
:::

```
@Composable
fun RecordListScreen(vm: RecordViewModel) {
    val records by vm.records.collectAsState()

    Column {
        // การ์ดสรุปด้านบน (รายรับ-รายจ่าย=คงเหลือ)
        SummaryCard(records)

        // รายการเดินบัญชี
        LazyColumn {
            items(records, key = { it.id }) { record -&gt;
                RecordRow(record) { vm.deleteRecord(record) }
            }
        }

        // ปุ่มลอย "จดรายการ" → เด้งกล่องบันทึก
        FloatingActionButton(onClick = { showAddDialog = true }) {
            Text("+")
        }
    }
}

@Composable
fun RecordRow(record: Record, onDelete: () -&gt; Unit) {
    Row(Modifier.fillMaxWidth().padding(12.dp)) {
        Text(record.category, fontWeight = FontWeight.Bold)
        Spacer(Modifier.weight(1f))
        Text(if (record.type == "income") "+${record.amount}" else "-${record.amount}",
             color = if (record.type == "income") Color(0xFF27AE60) else Color(0xFFC0392B))
    }
}
```
:::

ส่วนเพิ่มรายการใช้ AlertDialog (กล่องโต้ตอบ) ง่ายที่สุด: ช่องกรอกไม่กี่ช่อง + สลับรายรับ/รายจ่าย + ดรอปดาวน์เลือกหมวด กดยืนยันก็เรียก vm.addRecord(...)

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ข้อควรรู้: ตรวจข้อมูลป้อน อย่าขี้เกียจ

{class="mt-1"}
ช่องกรอกยอดเงินต้องตรวจให้เป็น: ค่าว่าง เลขติดลบ ข้อความแปลก ๆ อย่าง "abc" ต้องดักให้หมด (ใช้ toDoubleOrNull() เช็ก) สาเหตุที่แอปพังบ่อยที่สุดข้อหนึ่งคือ "เอาสิ่งที่ผู้ใช้ป้อนมาเป็นเด็กดี" จำไว้: ทุกอย่างที่ผู้ใช้ป้อน ให้ถือว่าเป็นศัตรูแล้วตรวจตราเสมอ
:::

#### 5. แก้ไขกับลบ: ให้ข้อมูล "เข้าได้ออกได้"

แอปบันทึกบัญชีที่เพิ่มได้อย่างเดียวลบไม่ได้ ใช้ได้สามวันก็เละ เพิ่มสองการกระทำนี้:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · ลบและแก้ไข</span><span class="dots">···</span>
:::

```
// เพิ่มใน Dao อีกสองฟังก์ชัน:
@Query("UPDATE records SET amount=:amount, category=:category, note=:note WHERE id=:id")
suspend fun update(id: Long, amount: Double, category: String, note: String)

@Query("DELETE FROM records WHERE id=:id")
suspend fun deleteById(id: Long)

// ในหน้าจอ: กดค้างที่รายการเพื่อเด้งเมนู "แก้ไข/ลบ" (Compose ใช้ DropdownMenu หรือ AlertDialog)
// ก่อนลบควรเด้งกล่องยืนยันก่อน—"ลบพลาด" คือสิ่งที่ผู้ใช้แอปบัญชีเกลียดที่สุด
```
:::

รายละเอียดการโต้ตอบมีบทเรียนสองข้อ: ลบต้องยืนยันสองรอบ (กันมือลั่น) แก้ไขควรเติมค่าเดิมไว้ให้ก่อนเท่าที่ทำได้ (แก้ตัวเดียวง่ายกว่าพิมพ์ใหม่หมด) อย่ามองข้ามสองรายละเอียดนี้ — ความรู้สึก "ของจริงระดับสินค้า" คือของพวกนี้กองรวมกัน

#### 6. ตรวจรับงาน: ตรวจสามชั้น + โจทย์ท้าทายสองข้อ

พอโปรเจกต์เสร็จ ตรวจรับสามชั้นตาม "ฟังก์ชัน → ขอบเขต → สถาปัตยกรรม": บันทึกได้ไหม ลบได้ไหม ปิดเปิดแอปใหม่ข้อมูลยังอยู่ไหม (ฟังก์ชัน); กรอกยอด 0 หรือติดลบแล้วพังไหม หมุนหน้าจอข้อมูลหายไหม (ขอบเขต); หน้าจอกับข้อมูลปนกันหรือเปล่า ฟิลด์เขียนฝังตายหรือเปล่า (สถาปัตยกรรม)

ตรวจรับเวอร์ชันพื้นฐานผ่านแล้ว เพิ่ม "เมนูพิเศษขั้นสูง" ให้ตัวเองอีกสองอย่าง:

1. ตัวกรองรายเดือน: เพิ่มปุ่มสลับเดือนด้านบน (เช่น 2026-08 ▾) ลิสต์แสดงเฉพาะประวัติเดือนนั้น;
2. แผนภูมิวงกลมตามหมวด: ใช้ Canvas ของ Compose หรือเพิ่มไลบรารีกราฟเบา ๆ วาด "เงินหายไปไหน" เป็นแผนภูมิวงกลม — ทำจบข้อนี้ แอปบันทึกบัญชีก็เริ่มมี "กลิ่นอายสินค้าจริง" แล้ว

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ลงมือทำด้วยกัน: จบให้ได้ภายในสัปดาห์นี้

{class="mt-1"}
ลงมือตามลำดับ "ชั้นข้อมูล → ViewModel → หน้ารายการ → หน้าเพิ่มรายการ → การ์ดสรุป" วันละหนึ่งขั้น ติดเมื่อไรก็โยน error ตามตัวให้เสิร์ชเอนจินหรือ AI (ยังจำภาคที่ 7 "ลงมือเขียนโปรแกรมด้วย AI" ได้ไหม? ตอนอธิบายปัญหาให้บอกให้ชัด "พฤติกรรมที่คาดหวัง พฤติกรรมที่เกิดจริง ขั้นตอนทำซ้ำ") พอเสร็จแล้วเอาไปบันทึกบัญชีสักหนึ่งสัปดาห์ — ได้ใช้แอปที่ตัวเองทำ ความภูมิใจจะดันให้คุณเดินต่อไปเอง
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
สรุปบทนี้

- ห้าองค์ประกอบความต้องการ → แตกเป็นขั้นย่อย "ทีละขั้นใช้ได้" แล้วค่อยลงมือ
- ชั้นข้อมูล: เอนทิตี Record + Dao (มี SQL สถิติรายเดือน) + Database
- แบ่งหน้าที่ MVVM: View สนใจแค่วาด, ViewModel ดูแลตรรกะ, Model ดูแลจัดเก็บ
- Flow + stateIn + collectAsState: ข้อมูลเปลี่ยนเมื่อไรหน้าจอรีเฟรชเอง
- LazyColumn ลิสต์โหลดเท่าที่จำเป็น; AlertDialog ไว้เพิ่มรายการ
- ตรวจรับสามชั้น (ฟังก์ชัน/ขอบเขต/สถาปัตยกรรม) + โจทย์ท้าทายขั้นสูง (ตัวกรองรายเดือน, แผนภูมิวงกลมตามหมวด)
:::
