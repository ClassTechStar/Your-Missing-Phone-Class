---
id: di-liu-shi-si-zhang
num: 64
part: ios-kai-fa-pian
nav: บทที่ 64: การจัดเก็บข้อมูลและการร้องขอผ่านเครือข่าย
toc: default
kind: chapter
---

### บทที่ 64: การจัดเก็บข้อมูลและการเรียกใช้เครือข่าย

{class="chapter-intro mb-4"}
แอปที่ทำได้แค่ให้'ดู'เป็นแอปไร้ชีวิต แอปที่เก็บข้อมูลได้และต่อเน็ตได้ต่างหากที่มีชีวิตจริง บทนี้พาไปรู้จัก'สามพี่น้อง'ของชั้นข้อมูลใน iOS: UserDefaults (เก็บการตั้งค่าเล็ก ๆ), SwiftData (เก็บข้อมูลมีโครงสร้าง), URLSession (คุยกับเซิร์ฟเวอร์) พร้อมด้วย Codable สำหรับแปลง JSON และ async/await สไตล์ยุคใหม่ เรียนจบบทนี้ คุณจะเขียนแอปจริงที่จดจำนิสัยผู้ใช้และอัปเดตเนื้อหาแบบเรียลไทม์ได้แล้ว

#### 1. เลือกวิธีจัดเก็บอย่างไร: ดูตารางนี้ก่อน

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ทางเลือก</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">เหมาะกับเก็บอะไร</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">จุดเด่น</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ใช้ตรงไหนในหนังสือเล่มนี้</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">การตั้งค่าเรื่อยเปื่อย (สวิตช์, สิ่งที่ชอบ)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">คู่คีย์-ค่า ง่ายและตรงไปตรงมา</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">การตั้งค่าบทที่ 65, เมืองโปรดบทที่ 66</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ข้อมูลมีโครงสร้าง (รายการบัญชี, บันทึกต่าง ๆ)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ตัวห่อฐานข้อมูลทางการ ประกาศด้วย @Model บรรทัดเดียว</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">บันทึกรายการบัญชีบทที่ 65</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">(ไม่เก็บ ดึงผ่านเน็ต) ข้อมูลจากเซิร์ฟเวอร์</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เฟรมเวิร์กเครือข่ายมากับระบบ ไม่ต้องพึ่งไลบรารีภายนอก</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ข้อมูลอากาศบทที่ 66</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
หน้าที่ของสามพี่น้องฝ่ายข้อมูล

จดคำกลับไว้ว่า'การตั้งค่าเล็ก ๆ เข้า UserDefaults ข้อมูลเป็นชุดใหญ่เข้า SwiftData ข้อมูลจากภายนอกใช้ URLSession' Core Data ในบทเรียนเก่ายังใช้ได้อยู่ (SwiftData ก็คือตัวตนยุคใหม่ของมัน) ส่วนการเขียน SQLite เองแทบไม่ต้องแตะ — เรียนของใหม่ตรง ๆ ดีกว่า อย่าเดินซ้ำทางเก่า

#### 2. UserDefaults: เก็บการตั้งค่าเล็ก ๆ น้อย ๆ

::: div .code-block
:::inline div .code-head
<span>SWIFT · ตัวอย่าง UserDefaults</span><span class="dots">···</span>
:::

```
// เขียน: เก็บค่า
UserDefaults.standard.set(true, forKey: "isDarkMode")
UserDefaults.standard.set("ปักกิ่ง", forKey: "favoriteCity")

// อ่าน: ดึงค่าออกมา (ไม่มีก็คืนค่าเริ่มต้น)
let isDark = UserDefaults.standard.bool(forKey: "isDarkMode")
let city = UserDefaults.standard.string(forKey: "favoriteCity") ?? "ปักกิ่ง"

// ลบ: เอาคีย์นี้ออก
UserDefaults.standard.removeObject(forKey: "isDarkMode")
```
:::

ระวังว่ามันเหมาะกับการตั้งค่าเล็ก ๆ เท่านั้น — ถ้ามีรายการเป็นสิบเป็นร้อย ให้ส่งต่อให้ SwiftData จัดการ อย่าเอา UserDefaults มาใช้แทนฐานข้อมูล (จะทำให้แอปเปิดช้าลงและค้นหาไม่สะดวก)

#### 3. SwiftData: สร้าง'บ้านจริง ๆ'ให้ข้อมูล

SwiftData คือแนวทางฐานข้อมูลทางการตั้งแต่ iOS 17 เป็นต้นมา ย่อ'สร้างตาราง เพิ่ม ลบ แก้ ค้น'ให้ง่ายสุดขีด — แค่ใส่แอนโนเทชัน @Model คลาสข้อมูลก็กลายเป็นตารางในฐานข้อมูล:

::: div .code-block
:::inline div .code-head
<span>SWIFT · ตัวอย่าง SwiftData</span><span class="dots">···</span>
:::

```
import SwiftData

// 1. @Model: คลาสนี้กลายเป็น "ตาราง" อัตโนมัติ
@Model
class Record {
    var amount: Double
    var category: String
    var note: String
    var date: Date

    init(amount: Double, category: String, note: String, date: Date) {
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date
    }
}

// 2. ผูกคอนเทนเนอร์ที่จุดเริ่มแอป
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: Record.self)   // ฐานข้อมูลพร้อม
    }
}

// 3. ในวิวใช้ @Query อ่าน, @Environment เขียน
struct RecordListView: View {
    @Query(sort: \Record.date, order: .reverse) var records: [Record]
    @Environment(\.modelContext) private var context

    var body: some View {
        List(records) { r in
            Text("\(r.category) \(r.amount) หยวน")
        }
    }

    func add(amount: Double, category: String) {
        let r = Record(amount: amount, category: category, note: "", date: Date())
        context.insert(r)     // บันทึก
        try? context.save()   // ลงดิสก์
    }
}
```
:::

เทมเพลต '@Model + modelContainer + @Query' ชุดนี้เอาไปวางในโปรเจกต์ไหนของคุณก็ได้ตรง ๆ — เปลี่ยนชื่อฟิลด์เท่านั้น พอข้อมูลเปลี่ยน @Query จะรีเฟรชอินเทอร์เฟซให้เอง ช่างมหัศจรรย์นัก

#### 4. Codable: คอย'แปลภาษา'ให้ JSON

ข้อมูลจากเซิร์ฟเวอร์ส่วนใหญ่เป็นข้อความ JSON โปรโตคอล Codable ของ Swift ทำให้การแปลง'JSON ⇄ struct'เกิดขึ้นเองอัตโนมัติ — ชื่อฟิลด์ตรงกัน มนต์ก็ทำงาน:

::: div .code-block
:::inline div .code-head
<span>SWIFT · ถอดรหัส JSON ด้วย Codable</span><span class="dots">···</span>
:::

```
// JSON: {"name":"ปักกิ่ง","main":{"temp":26.5},"weather":[{"description":"แจ่มใส"}]}
struct WeatherResponse: Codable {
    let name: String
    let main: Main
    let weather: [Weather]
}
struct Main: Codable { let temp: Double }
struct Weather: Codable { let description: String }

// จากข้อความ JSON → struct
let decoder = JSONDecoder()
let data = jsonString.data(using: .utf8)!
let result = try decoder.decode(WeatherResponse.self, from: data)
print(result.weather[0].description)   // "แจ่มใส"
```
:::

กฎเหล็ก: ดู JSON ที่ส่งกลับมาจริงก่อน แล้วค่อยนิยามฟิลด์ บั๊ก'แปลงค่าไม่สำเร็จ'ส่วนใหญ่มาจากชื่อฟิลด์พิมพ์ผิดหรือเดาชนิดข้อมูลผิด (เซิร์ฟเวอร์ส่ง "26.5" เป็นสตริง แต่คุณประกาศเป็น Double) — พรินต์ JSON ดิบออกมาเทียบดู หาจุดผิดเจอในสิบวินาที

#### 5. URLSession + async/await: คุยกับเซิร์ฟเวอร์

การต่อเน็ตบน iOS ใช้ URLSession ที่มากับระบบ คู่กับ async/await (ฟังก์ชันอะซิงโครนัส) ของ Swift ทำให้'การรอเน็ต'เป็นธรรมชาติเหมือน'รอพัสดุ':

::: div .code-block
:::inline div .code-head
<span>SWIFT · URLSession + async/await</span><span class="dots">···</span>
:::

```
struct WeatherService {
    // ฟังก์ชัน async: async หมายถึง "ต้องรอสักครู่" throws หมายถึง "อาจล้มเหลว"
    func fetchWeather(city: String) async throws -> WeatherResponse {
        let url = URL(string:
            "https://api.example.com/weather?city=\(city)")!
        let (data, _) = try await URLSession.shared.data(from: url)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}

// จุดเรียก (ใน .task):
.task {
    do {
        let weather = try await service.fetchWeather(city: "ปักกิ่ง")
        // อัปเดตหน้าจอ……
    } catch {
        print("เกิดข้อผิดพลาด: \(error)")
    }
}
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
กันพลาด: กฎเหล็กสองข้อของการใช้เครือข่าย

{class="mt-1"}
① การต่อเน็ตต้องใช้ async/await ห้ามปิดกั้นเธรดหลักเด็ดขาด — อินเทอร์เฟซค้างคือประสบการณ์ระดับทำให้แอปล้ม โครงสร้างคอนเคอเรนซีของ Swift ทำให้เรื่องนี้เป็นธรรมชาติมาก แต่อย่าลืม try await กับ do/catch ② ATS ห้าม HTTP แบบไม่เข้ารหัสเป็นค่าเริ่มต้น: iOS บังคับให้ใช้ HTTPS ตอนทดสอบบริการ http:// ในเครื่องต้องเปิดข้อยกเว้นชั่วคราวใน Info.plist (NSAppTransportSecurity) แต่ผลิตภัณฑ์จริงต้องใช้ HTTPS ทั้งหมด — ทีมรีวิวก็เฝ้าดูเรื่องนี้เช่นกัน
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ลงมือทำ: สร้างแอปเล็ก ๆ 'คำคมประจำวัน'

#### 6. ข้อผิดพลาดเครือข่ายก็ต้อง'จัดระดับ': อย่าโยน error ทุกชนิดให้ผู้ใช้

เน็ตหลุด, หมดเวลา, 404, เซิร์ฟเวอร์ 500... แต่ละความผิดพลาด ผู้ใช้ควรเห็นข้อความที่ไม่เหมือนกัน:

::: div .code-block
:::inline div .code-head
<span>SWIFT · จัดการข้อผิดพลาดแบบแบ่งระดับ</span><span class="dots">···</span>
:::

```
func friendlyMessage(_ error: Error) -> String {
    if let urlError = error as? URLError {
        switch urlError.code {
        case .notConnectedToInternet: return "เน็ตหลุด ลองเช็คการเชื่อมต่อไหม?"
        case .timedOut:               return "คำขอหมดเวลา ลองใหม่ภายหลังไหม?"
        case .cannotFindHost:         return "หาเซิร์ฟเวอร์ไม่เจอ"
        default:                      return "เน็ตมีปัญหา: \(urlError.code)"
        }
    }
    if let d = error as? DecodingError {
        return "รูปแบบข้อมูลไม่ตรง (อาจเพราะ API เปลี่ยน)"
    }
    return "เกิดข้อผิดพลาด: \(error.localizedDescription)"
}
```
:::

แสดง'ภาษาคน'ให้ผู้ใช้ ส่วน'ต้นฉบับ'ปล่อยไว้ในล็อก (พรินต์ error ฉบับเต็ม) อย่าเอาสำนวนอังกฤษกึกกือจาก error.localizedDescription โยนใส่ผู้ใช้ตรง ๆ — ความเป็นแอปชั้นดีซ่อนอยู่ในรายละเอียดพวกนี้

{class="mt-1"}
หา API คำคมฟรีสักตัว (อย่าง hitokoto หรือแนวเดียวกัน) ใช้ URLSession + async/await ดึง'คำคมประจำวัน'มาแสดงกลางหน้าจอ เพิ่มปุ่ม'เปลี่ยนประโยค' แล้วเก็บประโยคที่ชอบลง'รายการโปรด'ด้วย SwiftData แบบฝึกหัดนี้ใช้ครบทั้ง UserDefaults/SwiftData/Codable/URLSession — ทำเสร็จแล้ว บทที่ 7 กับ 8 ก็ง่ายเหมือนกินขนม
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
สรุปบทนี้

- คำกลับ: การตั้งค่าเล็ก ๆ เข้า UserDefaults ข้อมูลเป็นชุดใหญ่เข้า SwiftData ข้อมูลจากภายนอกใช้ URLSession
- สามท่าเด็ดของ SwiftData: @Model ประกาศตาราง, modelContainer ติดตั้งคอนเทนเนอร์, @Query สำหรับอ่าน + context.insert สำหรับเขียน
- Codable'แปลภาษา'JSON ให้เองอัตโนมัติ: ชื่อฟิลด์ตรงกัน มนต์ก็ทำงาน
- URLSession + async/await: ต่อเน็ตเหมือนรอพัสดุ; do/catch จัดการความล้มเหลว
- กฎเหล็กสองข้อ: อย่าปิดกั้นเธรดหลัก; ผลิตภัณฑ์จริงต้องใช้ HTTPS (ATS)
:::
