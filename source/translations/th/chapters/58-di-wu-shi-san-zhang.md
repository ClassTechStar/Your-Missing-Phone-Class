---
id: di-wu-shi-san-zhang
num: 53
part: an-zhuo-kai-fa-pian
nav: บทที่ 53: การจัดเก็บข้อมูลและการร้องขอผ่านเครือข่าย
toc: default
kind: chapter
---

### บทที่ 53: การเก็บข้อมูลกับการเรียกเครือข่าย

{class="chapter-intro mb-4"}
แอปที่ "ดู" ได้อย่างเดียวคือแอปตาย แอปที่เก็บข้อมูลได้ เชื่อมเน็ตได้ ต่างหากที่มีชีวิต บทนี้จะพาทำความรู้จัก "สามชิ้น" ของชั้นข้อมูล Android: DataStore (เก็บค่าตั้งเล็ก ๆ), Room (เก็บข้อมูลเชิงโครงสร้าง), Retrofit (คุยกับเซิร์ฟเวอร์) แถม "ผู้กำกับใหญ่" ของพวกมัน — โครูทีน (coroutine) จบบทนี้ คุณก็เขียนแอปจริงที่จำนิสัยผู้ใช้ได้ อัปเดตเนื้อหาแบบเรียลไทม์ได้แล้ว

#### 1. เลือกวิธีจัดเก็บยังไง: ดูตารางนี้ก่อน

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ทางเลือก</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">เหมาะกับเก็บอะไร</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">จุดเด่น</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ใช้ตรงไหนในหนังสือ</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DataStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ค่าตั้งเล็ก ๆ ที่กระจัดกระจาย (ธีม, สวิตช์เปิดปิด)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">คู่คีย์-ค่า ง่ายและปลอดภัย</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">การตั้งค่าแอปบันทึกบัญชีในบทที่ 54</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ข้อมูลเชิงโครงสร้าง (รายการบัญชี, ผู้ใช้)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">การห่อฐานข้อมูล SQLite ตัวจริง ค้นหาได้</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">รายการบัญชีในบทที่ 54</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ข้อมูลจากเซิร์ฟเวอร์ (ไม่เก็บ ดึงผ่านเน็ต)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">มาตรฐานที่ใช้กันจริงของไลบรารีคำขอ HTTP</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ข้อมูลสภาพอากาศในบทที่ 55</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
การแบ่งหน้าที่ของสามชิ้นเรื่องข้อมูล

จำคาถาสั้น ๆ ไว้: "ค่าตั้งเล็กเข้า DataStore ข้อมูลเป็นก้อนเข้า Room ข้อมูลจากข้างนอกใช้ Retrofit" SharedPreferences ที่เห็นบ่อยในบทเรียนเก่าถูก DataStore แทนที่ไปแล้ว และการเขียน SQL เองบน SQLite ก็ถูก Room แทนที่ไปแล้ว — เรียนของใหม่ไปเลย อย่าเดินทางเก่า

#### 2. DataStore: เก็บค่าตั้งเล็ก ๆ

อยากจำค่ากระจัดกระจายอย่าง "เหรียญที่ผู้ใช้เลือกไว้ล่าสุด" "เปิดโหมดมืดหรือยัง" ให้ใช้ DataStore (แบบ Preferences):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · ตัวอย่าง DataStore</span><span class="dots">···</span>
:::

```
val Context.dataStore by preferencesDataStore(name = "settings")

// เขียน: เก็บค่า
suspend fun saveTheme(isDark: Boolean) {
    context.dataStore.edit { prefs ->
        prefs[THEME_KEY] = isDark
    }
}

// อ่าน: ดึงค่าออกมา (Flow แจ้งการเปลี่ยนแปลงเอง)
val themeFlow: Flow<Boolean> = context.dataStore.data
    .map { it[THEME_KEY] ?: false }
```
:::

สังเกตว่าสิ่งที่คืนกลับมาคือ Flow — กระแสข้อมูลที่ "ไหล" ได้ ค่าเปลี่ยนเมื่อไร ทุกจุดที่สังเกตมันอยู่จะได้รับค่าใหม่ทันทีเอง แนวคิดนี้ (reactive) คือศิลาแลงของ Android ยุคใหม่ บทที่ 54 จะได้ลงมือจริง

#### 3. Room: ให้ข้อมูลมี "บ้านแท้ ๆ" ของตัวเอง

แอปบันทึกบัญชีมีรายการร้อยเป็นพัน แถมต้องค้นสถิติตามหมวดตามเดือน — นี่ต้องใช้ฐานข้อมูล Room คือการห่อ SQLite อย่างเป็นทางการ ทำให้ "สร้างตาราง ค้นข้อมูล" ธรรมชาติเหมือนเขียน Kotlin เลย มีสามอย่าง:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · ชุดสามชิ้นของ Room: Entity / Dao / Database</span><span class="dots">···</span>
:::

```
// 1. Entity: โครงตาราง (หนึ่งตาราง = หนึ่ง data class)
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val amount: Double,
    val category: String,
    val note: String,
    val date: String
)

// 2. Dao: อินเทอร์เฟซจัดการข้อมูล (เพิ่ม ลบ แก้ ค้น)
@Dao
interface RecordDao {
    @Query("SELECT * FROM records ORDER BY date DESC")
    fun getAll(): Flow<List<Record>>

    @Insert
    suspend fun insert(record: Record)

    @Delete
    suspend fun delete(record: Record)

    @Query("SELECT SUM(amount) FROM records WHERE category = :c")
    suspend fun sumByCategory(c: String): Double
}

// 3. Database: ประกอบร่าง
@Database(entities = [Record::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun recordDao(): RecordDao
}
```
:::

เทมเพลต "สามชิ้น" ชุดนี้เอาไปใช้ในโปรเจกต์ไหนของคุณก็ได้ตามเดิม — เปลี่ยนชื่อฟิลด์ก็จบ คิวรีคืน Flow หน้าจอรีเฟรชตามข้อมูลเองอัตโนมัติ วิเศษจริง ๆ

#### 4. Retrofit: คุยกับเซิร์ฟเวอร์

สภาพอากาศ ข่าว อัตราแลกเปลี่ยน... ข้อมูลพวกนี้ไม่ได้อยู่ในมือถือ แต่อยู่บนเซิร์ฟเวอร์ของคนอื่น Retrofit ทำให้ "ขอข้อมูลจากเซิร์ฟเวอร์" ง่ายเหมือนเรียกฟังก์ชัน เดินสามขั้นตอน:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Retrofit ใน 3 ขั้นตอน</span><span class="dots">···</span>
:::

```
// 1. ประกาศอินเทอร์เฟซ: เขียนคำขอ HTTP ให้เหมือนเรียกฟังก์ชัน
interface WeatherApi {
    @GET("v1/weather")
    suspend fun getWeather(@Query("city") city: String): WeatherResponse
}

// 2. สร้างอินสแตนซ์
val api = Retrofit.Builder()
    .baseUrl("https://api.example.com/")
    .addConverterFactory(GsonConverterFactory.create())
    .build()
    .create(WeatherApi::class.java)

// 3. เรียกเหมือนเรียกฟังก์ชันเลย (ใน coroutine)
val result = api.getWeather("ปักกิ่ง")
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ข้อควรระวัง: กฎเหล็กเรื่องเครือข่ายสองข้อ

{class="mt-1"}
1) ห้ามยิงคำขอเครือข่ายบนเธรดหลักเด็ดขาด — จะทำให้หน้าจอค้างจนแอปพัง (NetworkOnMainThreadException) คำขอเครือข่ายทุกตัวต้องอยู่ในโครูทีน (viewModelScope.launch) 2) HTTP ข้อความล้วนถูกห้ามไว้ตามค่าเริ่มต้น: ตั้งแต่ Android 9 ต้องใช้ HTTPS ถ้าช่วงทดสอบต้องใช้ที่อยู่ http:// ในเครื่อง ต้องประกาศ usesCleartextTraffic อย่างชัดเจนใน Manifest — แต่ของจริงต้องใช้ HTTPS ทั้งหมด
:::

#### 5. แปลง JSON: เป็น "ล่าม" ให้ข้อมูลจากเครือข่าย

ข้อมูลที่เซิร์ฟเวอร์ส่งกลับมาส่วนใหญ่เป็น JSON — ข้อความชุดหนึ่งหน้าตาเหมือน "พจนานุกรมซ้อนกัน" Retrofit ต้องมี "ล่าม" แปลงมันเป็นอ็อบเจกต์ Kotlin สองทางเลือกหลักยอดนิยมของปี 2026:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ทางเลือก</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">จุดเด่น</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">สถานการณ์ที่แนะนำ</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gson / Moshi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">แบบใช้ reflection รุ่นเก๋า ตั้งค่าแทบไม่เสียแรง</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">โปรเจกต์เล็กที่เริ่มเร็ว ฟิลด์ไม่กี่ตัว</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">kotlinx.serialization</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">แบบคอมไพล์ตอนบิลด์ของทางการ เร็วกว่า ปลอดภัยกว่า</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">อันดับหนึ่งของโปรเจกต์ใหม่ (กระแสหลักปี 2026)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
สองทางเลือกแปลง JSON

::: div .code-block
:::inline div .code-head
<span>KOTLIN · ตัวอย่าง kotlinx.serialization</span><span class="dots">···</span>
:::

```
// ใส่แอนโนเทชัน @Serializable ให้ data class
@Serializable
data class WeatherResponse(
    val weather: List<Weather>,
    val main: Main,
    val name: String
)

// Retrofit ต่อ Converter (ยกตัวอย่างแบบทางการรองรับใน Retrofit 2.11+):
// .addConverterFactory(json.asConverterFactory("application/json".toMediaType()))
```
:::

ไม่ว่าจะทางไหน กฎเหล็กคือ: ดู JSON ที่คืนมาจริงก่อน แล้วค่อยนิยามฟิลด์ บั๊ก "แปลงไม่สำเร็จ" จำนวนมากเกิดจากชื่อฟิลด์พิมพ์ผิด เดาระดับการซ้อนผิด — พิมพ์ JSON ดิบออกมาเทียบดู สิบวินาทีก็เจอจุดผิด

#### 6. โครูทีน: "ภาษากลาง" ของการทำงานขนานบน Android

suspend กับ launch ที่โผล่ซ้ำ ๆ ข้างบนมาจากโครูทีน (Coroutine) ของ Kotlin — โซลูชันทำงานขนานอย่างเป็นทางการของ Android เข้าใจแบบหยาบ ๆ ก็คือ: ทำให้งานที่ "ต้องรอสักพัก" (เครือข่าย ฐานข้อมูล) ไม่ไปทำหน้าจอค้าง

::: div .code-block
:::inline div .code-head
<span>KOTLIN · เริ่มต้นกับ coroutine</span><span class="dots">···</span>
:::

```
// เปิด coroutine ใน ViewModel
viewModelScope.launch {
    val records = dao.getAll().first()  // suspend: รอได้เองโดยไม่บล็อกใคร
    // อัปเดตสเตตหน้าจอ……
}

// จำคีย์เวิร์ดง่าย ๆ:
// suspend   —— "ฉันต้องรอ อย่ามาขวาง"
// launch    —— "เริ่มงาน!"
// viewModelScope —— "โรงงาน" ที่ตามหน้านี้ไป หน้าปิดก็ปิดงานเอง
```
:::

คนเริ่มจากศูนย์จำวิธีใช้ก่อนก็พอ หลักการ "หยุดพักกับกลับมาทำต่อ" ข้างหลังค่อยไปลุยลึกทีหลัง งานพัฒนาประจำวันของคุณ 90% ก็เขียนตามเทมเพลตนี้

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ลงมือทำด้วยกัน: สร้างแอปเล็ก "คำคมประจำวัน"

{class="mt-1"}
หา API คำคมฟรี ๆ (เช่น hitokoto หรือแบบนั้น) ใช้ Retrofit ดึง "คำคมประจำวัน" มาแสดงกลางหน้าจอ เพิ่มปุ่ม "เปลี่ยนประโยค" (ขอใหม่ในโครูทีน) แล้วเก็บประโยคที่ชอบลง "รายการโปรด" ด้วย Room แบบฝึกหัดนี้ใช้ครบทั้ง DataStore/Room/Retrofit/โครูทีน — ทำเสร็จแล้ว บทที่ 7 กับ 8 คือขนมหวานชิ้นเล็ก
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
สรุปบทนี้

- คาถาจำ: ค่าตั้งเล็กเข้า DataStore ข้อมูลเป็นก้อนเข้า Room ข้อมูลจากข้างนอกใช้ Retrofit
- DataStore คืน Flow: ค่าเปลี่ยน ผู้สังเกตได้รับเองอัตโนมัติ
- สามชิ้นของ Room: @Entity (ตาราง) + @Dao (การกระทำ) + @Database (ประกอบร่าง) เทมเพลตนำกลับมาใช้ได้เลย
- Retrofit สามขั้น: นิยามอินเทอร์เฟซ → สร้างอินสแตนซ์ → เรียกใช้ในโครูทีน
- กฎเหล็กสองข้อ: เครือข่ายห้ามยุ่งเธรดหลัก; ของจริงต้อง HTTPS
- โครูทีน = การรอแบบไม่ทำหน้าจอค้าง; viewModelScope คือห้องทำงานประจำหน้า
:::
