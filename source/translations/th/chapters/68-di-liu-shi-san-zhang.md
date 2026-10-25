---
id: di-liu-shi-san-zhang
num: 63
part: ios-kai-fa-pian
nav: บทที่ 63: วิว สถานะ และการนำทาง
toc: default
kind: chapter
---

### บทที่ 63: วิว สเตต และการนำทาง

{class="chapter-intro mb-4"}
ของเล่นแอปหน้าเดียวเราทำเป็นแล้ว บทนี้จะแก้สองปัญหาของการ'โตขึ้น': วิธีกระโดดไปมาระหว่างหลายหน้า (การนำทาง) และข้อมูลไหลระหว่างหน้าอย่างไร (การจัดการสเตต) เรียนจบบทนี้ คุณจะสร้างโครงแอปหลายหน้าสุดคลาสสิกอย่าง'รายการ → รายละเอียด → แก้ไข'ได้

#### 1. 'ภาพรวมการไหลของข้อมูล'ในการจัดการสเตต

เครื่องมือจัดการสเตตของ SwiftUI ไม่ได้มีแค่ @State ตัวเดียว ลองดูภาพรวมนี้ก่อน เพื่อเข้าใจว่า'เมื่อไหร่ใช้ตัวไหน':

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">เครื่องมือ</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ดูแลอะไร</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ใครใช้</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">สถานการณ์ทั่วไป</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">สเตตชั่วคราวส่วนตัวของแต่ละหน้า</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">วิวปัจจุบัน</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ตัวนับ, ข้อความในช่องกรอก</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Binding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ยืมสเตตของคนอื่นมาใช้</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ให้วิวลูกแก้ค่าของวิวแม่</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">คอมโพเนนต์ที่สร้างเอง</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@StateObject / @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">โลจิกที่ใช้ร่วมกันข้ามหน้า</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">วิวโมเดล (ViewModel)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">การโหลดข้อมูล, โลจิกของแอป</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@EnvironmentObject / .environment</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">สเตตที่แชร์ทั้งแอป</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ทั้งแอป</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">สถานะล็อกอินของผู้ใช้, การตั้งค่าธีม</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
ภาพรวมเครื่องมือจัดการสเตตของ SwiftUI (ปี 2026 @Observable ขึ้นเป็นกระแสหลักแล้ว)

::: div .code-block
:::inline div .code-head
<span>SWIFT · กระแสหลักปี 2026: วิวโมเดล @Observable</span><span class="dots">···</span>
:::

```
// สไตล์ทันสมัยบน iOS 17+: แมโคร @Observable (แนะนำสำหรับโปรเจกต์ใหม่)
import Observation

@Observable
class CounterModel {                 // วิวโมเดล
    var count = 0
    func increment() { count += 1 }
}

struct CounterView: View {
    @State private var model = CounterModel()   // ถือโมเดลไว้

    var body: some View {
        VStack {
            Text("คุณแตะไป \(model.count) ครั้ง")
            Button("แตะฉัน") { model.increment() }
        }
    }
}
```
:::

คำแนะนำแบบตรง ๆ สำหรับมือใหม่: อันที่เป็นส่วนตัวของหน้าใช้ @State ส่วนที่ข้ามหน้าหรือมีโลจิกให้ใช้คลาสแบบ @Observable @StateObject/@ObservableObject ในบทเรียนเก่าเป็นสไตล์รุ่นก่อน อ่านออกก็พอ โค้ดใหม่ให้ทำตามข้างบน

#### 2. NavigationStack: 'กองจาน'ของการเปลี่ยนหน้า

ตั้งแต่ iOS 16 เป็นต้นไป การนำทางหลายหน้าใช้ NavigationStack — เหมือนกองจาน ดันใส่ทีละใบ ย้อนกลับก็เด้งออกทีละใบ:

::: div .code-block
:::inline div .code-head
<span>SWIFT · นำทางด้วย NavigationStack</span><span class="dots">···</span>
:::

```
struct HomeView: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("สมุดของซานผวน") {
                    DetailView(name: "สมุดของซานผวน")   // หน้าปลายทาง
                }
                NavigationLink("สมุดของลี่ซือ") {
                    DetailView(name: "สมุดของลี่ซือ")
                }
            }
            .navigationTitle("รายชื่อสมุดบัญชี")   // หัวเรื่องใหญ่ด้านบน
        }
    }
}

struct DetailView: View {
    let name: String
    var body: some View {
        Text("หน้ารายละเอียดของ \(name)")
            .navigationTitle(name)
            .navigationBarTitleDisplayMode(.inline)
    }
}
```
:::

NavigationLink ก็คือ'ลิงก์เปลี่ยนหน้าที่แตะได้' ส่วน navigationTitle สร้างชื่อบนแถบนำทางและปุ่มย้อนกลับให้อัตโนมัติ ถ้าอยากเปลี่ยนหน้าด้วยโค้ด (เช่นกด'บันทึก'แล้วกลับหน้าเดิมอัตโนมัติ) ให้ใช้ @Environment(\.dismiss) ปิดหน้าปัจจุบัน — สองเทคนิคนี้คู่กัน ก็ครอบคลุมความต้องการด้านนำทางถึง 90%

#### 3. ป๊อปอัปและแท็บด้านล่าง: sheet กับ TabView

นอกจาก'ดันหน้าใหม่เข้ามา' ยังมีรูปแบบการโต้ตอบคลาสสิกอีกสองแบบ:

::: div .code-block
:::inline div .code-head
<span>SWIFT · ป๊อปอัป sheet + แท็บ TabView</span><span class="dots">···</span>
:::

```
// 1. ป๊อปครึ่งจอ/เต็มจอจากด้านล่าง (ฟอร์มบันทึกชอบใช้)
struct HomeView: View {
    @State private var showAdd = false
    var body: some View {
        Button("จดรายการ") { showAdd = true }
            .sheet(isPresented: $showAdd) {
                AddRecordView()     // หน้าบันทึกที่ป๊อปขึ้นมา
            }
    }
}

// 2. แถบแท็บด้านล่าง ("โครง" ของแอป)
struct MainTabView: View {
    var body: some View {
        TabView {
            RecordListView()
                .tabItem { Label("สมุดบัญชี", systemImage: "book") }
            StatsView()
                .tabItem { Label("สถิติ", systemImage: "chart.pie") }
            SettingsView()
                .tabItem { Label("ตั้งค่า", systemImage: "gear") }
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
เคล็ดลับ: เมื่อไหร่ใช้แบบไหน?

{class="mt-1"}
กฎจากประสบการณ์: ขั้นตอนหลักใช้ NavigationStack ดันหน้า (รายการ → รายละเอียด), การทำงานชั่วคราวใช้ป๊อปอัป sheet (เพิ่ม, แก้ไข, ยืนยัน), ส่วนบล็อกใหญ่ที่อยู่เคียงกันใช้ TabView (แท็บด้านล่าง) ประกอบสามอย่างนี้เข้าด้วยกัน ก็คือโครงของแอปเกือบทุกตัว
:::

#### 4. List: 'ลิสต์แบบฉบับ iOS'

คอมโพเนนต์ที่ใช้บ่อยที่สุดและมี'กลิ่นอาย Apple'ที่สุดบน iOS ก็คือ List — เส้นแบ่งรายการ ปัดเพื่อลบ ไฮไลต์เมื่อแตะ มาให้ตั้งแต่แกะกล่อง:

::: div .code-block
:::inline div .code-head
<span>SWIFT · List รายการ + ปัดเพื่อลบ</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var records = ["มื้อกลางวัน 25.5", "รถไฟใต้ดิน 6.0", "เงินเดือน +8000"]

    var body: some View {
        List {
            ForEach(records, id: \.self) { r in
                Text(r)
            }
            .onDelete { indexSet in          // ปัดซ้ายเพื่อลบ
                records.remove(atOffsets: indexSet)
            }
        }
    }
}
```
:::

รายการ + NavigationLink + sheet + TabView — เอาสี่อย่างนี้มาประกอบกัน คุณก็สร้างโครงแอปที่สมบูรณ์แบบ'ลิสต์สมุดบัญชี → แตะดูรายละเอียด → กด + แล้วฟอร์มบันทึกเด้งขึ้นมา'ได้แล้ว โปรเจกต์สมุดบัญชีในบทหน้าก็สร้างด้วยวิธีนี้แหละ

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ลงมือทำ: สร้าง'โครงสามหน้า'

#### 5. วงจรชีวิตของแอป: ฟอร์กราวด์กับแบ็กกราวด์

คล้ายวงจรชีวิต Activity ของ Android แอป iOS ก็มีการเปลี่ยนสถานะแบบ'เกิด, อยู่ฟอร์กราวด์, ลงแบ็กกราวด์, ตาย'เช่นกัน ใน SwiftUI ให้เฝ้าดูผ่านค่าสภาพแวดล้อม scenePhase:

::: div .code-block
:::inline div .code-head
<span>SWIFT · เฝ้าดูการสลับพื้นหน้า/พื้นหลัง</span><span class="dots">···</span>
:::

```
@main
struct MyApp: App {
    @Environment(\.scenePhase) private var phase

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .onChange(of: phase) { _, newPhase in
            switch newPhase {
            case .active:    print("กลับมาพื้นหน้า กู้การรีเฟรชต่อ")
            case .inactive:  print("อยู่ระหว่างเปลี่ยน (สายเข้า/พึ่งสลับไปพื้นหลัง)")
            case .background: print("ลงพื้นหลัง บันทึกฉบับร่าง")
            @unknown default: break
            }
        }
    }
}
```
:::

การใช้งานทั่วไป: กลับมาที่ฟอร์กราวด์ก็รีเฟรชข้อมูล ลงแบ็กกราวด์ก็บันทึกฉบับร่าง iOS ควบคุมการรันพื้นหลังเข้มงวดมาก — แอปทั่วไปพอเข้าแบ็กกราวด์จะถูกระงับ (แช่แข็ง) ในเวลาไม่นาน อย่าหวังให้แอปแอบทำงานหนักเบื้องหลัง ถ้าจำเป็นต้องทำงานตามเวลาจริง ๆ ให้ใช้การแจ้งเตือนในเครื่องจากบทที่ 68 ไม่ใช่การ'อาศัยอยู่เบื้องหลังถาวร'

{class="mt-1"}
สร้างโครงสมุดบัญชีเวอร์ชันข้อมูลปลอม: TabView สามแท็บ (สมุดบัญชี/สถิติ/ตั้งค่า) → หน้าสมุดบัญชีใช้ List แสดงข้อมูลปลอม แตะแถวแล้วเปลี่ยนไปหน้ารายละเอียด (NavigationStack) → ปุ่ม + มุมขวาบนเด้ง sheet บันทึกรายการขึ้นมา ไม่เก็บข้อมูล ไม่ต่อเน็ต เอาไว้ฝึกสร้างโครงล้วน ๆ — ทำโครงนี้ได้ พอถึงบทที่ 65 ใส่ข้อมูลจริงลงไปก็ลื่นไหลเป็นธรรมชาติ
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
สรุปบทนี้

- เครื่องมือสเตตสี่ตัว: @State (ส่วนตัวของหน้า), @Binding (ยืมมาใช้), @Observable (โลจิก), .environment (ทั้งแอป)
- โปรเจกต์ใหม่ใช้มาโคร @Observable เขียนวิวโมเดล; @ObservableObject ในบทเรียนเก่า อ่านออกก็พอ
- NavigationStack ดันหน้าใหม่; @Environment(\.dismiss) ใช้ย้อนกลับด้วยโค้ด
- ขั้นตอนหลักดันหน้า งานชั่วคราวเด้ง sheet บล็อกใหญ่เคียงกันใช้ TabView
- List คือ'ลิสต์แบบฉบับ iOS': เส้นแบ่งและปัดเพื่อลบ ใช้ได้ทันทีแบบแกะกล่อง
:::
