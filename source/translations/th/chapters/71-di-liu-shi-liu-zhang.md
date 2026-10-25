---
id: di-liu-shi-liu-zhang
num: 66
part: ios-kai-fa-pian
nav: บทที่ 66: โปรเจกต์ 2 — แอปดูอากาศ (เวอร์ชันออนไลน์)
toc: default
kind: chapter
---

### บทที่ 66: โปรเจกต์ที่ 2 — แอปเช็คอากาศ (เวอร์ชันออนไลน์)

{class="chapter-intro mb-4"}
สมุดบัญชีคือการ'ฝึกพื้นฐานภายใน' ส่วนแอปอากาศคือการ'ออกไปพบโลกภายนอก' — ต้องเจรจากับอินเทอร์เน็ต ในโปรเจกต์นี้คุณจะได้เรียน: สมัคร API ฟรี แปลงค่า JSON จัดการสถานะอินเทอร์เฟซสามแบบ'กำลังโหลด/สำเร็จ/ล้มเหลว' และวิธีซ่อนคีย์ API ให้ปลอดภัย ทำเสร็จ คุณจะมีฝีมือทำ'แอปต่อเน็ต'ได้ทุกประเภท — ข่าว, อัตราแลกเปลี่ยน, แปลภาษา สูตรเดียวกันหมด

#### 1. สมัคร API อากาศฟรี

สำหรับฝึกมือส่วนตัว แนะนำ OpenWeatherMap หรือ QWeather ที่ใช้กันในจีน — ทั้งคู่มีโควตาฟรี สมัครแล้วใช้ได้เลย ขอยก OpenWeatherMap เป็นตัวอย่าง:

1. สมัครบัญชี → ไปที่หน้า API keys แล้วสร้าง Key หนึ่งตัว (apikey)
2. เวอร์ชันฟรีเรียกใช้ปลายทาง Current Weather ได้: api.openweathermap.org/data/2.5/weather? q=beijing&appid=คีย์ของคุณ&units=metric
3. ลองรันในเบราว์เซอร์สักครั้งก่อน ดูว่า JSON ที่ส่งกลับมาหน้าตาเป็นอย่างไร — นี่คือ'การเตรียมตัว'ที่ต้องทำก่อนต่อกับ API ทุกตัว

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
กันพลาด: ห้ามเขียนคีย์ลงในโค้ดเด็ดขาด

{class="mt-1"}
API Key เทียบเท่า'รหัสกระเป๋าเงิน'ของคุณ พอเขียนลงโค้ดแล้วคอมมิตขึ้น GitHub ไม่กี่ชั่วโมงบอทจะกวาดไปใช้ฟรีทันที วิธีที่ถูกต้องบน iOS: ใส่ไว้ใน Config.xcconfig (ไฟล์คอนฟิกที่ gitignore ข้ามไปแล้ว) แล้วอ่านเข้าโค้ดผ่าน Info.plist ค้นหา 'iOS xcconfig จัดการคีย์' แล้วทำตามก็พอ
:::

#### 2. ชั้นเครือข่าย: URLSession + Codable

นิยามโมเดลตาม JSON ที่ API ส่งกลับมาก่อน แล้วค่อยเขียนส่วนบริการ:

::: div .code-block
:::inline div .code-head
<span>SWIFT · โมเดลข้อมูล + เซอร์วิส</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"แจ่มใส"}],"main":{"temp":26.5,"humidity":40},"name":"ปักกิ่ง"}
struct WeatherResponse: Codable {
    let weather: [Weather]
    let main: Main
    let name: String
}
struct Weather: Codable { let description: String }
struct Main: Codable { let temp: Double; let humidity: Int }

struct WeatherService {
    let key: String   // อ่านจาก xcconfig

    func fetchWeather(city: String) async throws -> WeatherResponse {
        var comps = URLComponents(string: "https://api.openweathermap.org/data/2.5/weather")!
        comps.queryItems = [
            URLQueryItem(name: "q", value: city),
            URLQueryItem(name: "appid", value: key),
            URLQueryItem(name: "units", value: "metric"),
            URLQueryItem(name: "lang", value: "zh_cn")
        ]
        let (data, _) = try await URLSession.shared.data(from: comps.url!)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}
```
:::

#### 3. สถานะอินเทอร์เฟซสามแบบ: กำลังโหลด / สำเร็จ / ล้มเหลว

จิตวิญญาณของแอปต่อเน็ตอยู่ที่'การจัดการสถานะ' เน็ตช้า เน็ตหลุด พิมพ์ชื่อเมืองผิด... ทุกกรณีอินเทอร์เฟซต้องรายงานให้ผู้ใช้ทราบ ใช้ enum + switch แสดงได้อย่างสวยงาม:

::: div .code-block
:::inline div .code-head
<span>SWIFT · สเตตของ UI</span><span class="dots">···</span>
:::

```
enum LoadState {
    case loading                  // กำลังหมุน
    case success(WeatherResponse) // สำเร็จ
    case error(String)            // ล้มเหลว
}

@Observable
class WeatherViewModel {
    var state: LoadState = .loading
    private let service = WeatherService(key: Config.apiKey)

    func search(city: String) async {
        state = .loading
        do {
            let data = try await service.fetchWeather(city: city)
            state = .success(data)
        } catch {
            state = .error("หาเมืองนี้ไม่เจอ ลองชื่ออื่นไหม?")
        }
    }
}

// ในหน้าจอ:
switch vm.state {
case .loading: ProgressView("กำลังโหลด…")
case .success(let d): WeatherContent(data: d)
case .error(let msg): Text(msg).foregroundColor(.secondary)
}
```
:::

แบบสามช่วง loading/success/error นี้คือ'เทมเพลตสารพัดประโยชน์'ของอินเทอร์เฟซต่อเน็ต ท่องไว้ก่อน ต่อไปทำแอปต่อเน็ตตัวไหนก็ลอกแบบได้เลย

#### 4. โค้ดอินเทอร์เฟซเชิงปฏิบัติ: วาดอากาศออกมา

::: div .code-block
:::inline div .code-head
<span>SWIFT · หน้าจอ weather (ส่วนสำคัญ)</span><span class="dots">···</span>
:::

```
struct WeatherContent: View {
    let data: WeatherResponse

    var body: some View {
        VStack(spacing: 12) {
            Text(data.name)
                .font(.title.bold())
            Text("\(Int(data.main.temp))°C")
                .font(.system(size: 76, weight: .thin))
            Text(data.weather.first?.description ?? "ไม่ทราบ")
                .font(.title3)
                .foregroundColor(.secondary)
            HStack(spacing: 24) {
                Label("ความชื้น \(data.main.humidity)%", systemImage: "humidity")
                Label("รู้สึกเหมือน \(Int(data.main.temp))°C", systemImage: "thermometer")
            }
        }
        .padding()
    }
}
```
:::

รายละเอียดเล็ก ๆ ที่ควรเรียนรู้: first? ดึงสมาชิกตัวแรกอย่างปลอดภัย (รายการอาจว่าง), ?? "ไม่ทราบ" ใช้เป็นข้อความสำรอง; ตัวเลขอุณหภูมิฟอนต์บาง weight 76 เป็นสูตรคลาสสิกของแอปอากาศ; Label คือคอมโพเนนต์ทางการสำหรับ'ไอคอน+ข้อความ' เรียบร้อยกว่าประกอบ HStack เอง

#### 5. รายละเอียดการโต้ตอบและเมืองโปรด

- ช่องค้นหา: modifier .searchable ด้านบน ระบบมีการโต้ตอบการค้นหามาให้พร้อม ตอนกดยืนยันเรียก vm.search
- เมืองโปรด: เก็บเมืองที่ดูบ่อยลง UserDefaults เปิดครั้งหน้าจะค้นให้อัตโนมัติ
- ดึงลงเพื่อรีเฟรช: .refreshable { await vm.search(...) } จบในบรรทัดเดียว
- ไอคอนอากาศ: ใช้ Image(systemName:) จับคู่ตามลักษณะอากาศ (sun.max / cloud.rain / snowflake) อินเทอร์เฟซก็มีชีวิตขึ้นทันที

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
เคล็ดลับ: กับดักของชื่อเมืองภาษาจีน

{class="mt-1"}
OpenWeatherMap รองรับชื่อเมืองภาษาจีนได้ทั่วไปไม่ค่อยดี ค้นชื่อจีนว่า "เป่ยจิง" อาจไม่เจออะไรเลย แต่ "beijing" ปกติ วิธีแบบผลิตภัณฑ์จริงจังคือฝังตารางจับคู่'ชื่อเมือง → ภาษาอังกฤษ/พิกัด'ไว้ หรือต่อกับบริการอากาศในประเทศ ช่วงฝึกมือรองรับชื่อเมืองแบบพินอิน/อังกฤษพอก่อน อย่าเอามาเถียงกับมันเลย
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ลงมือทำ: เช็กลิสต์ตรวจรับแอปอากาศ

#### 6. ดีบักการเรียกเครือข่ายอย่างไร: พรินต์, ดักจับแพ็กเก็ต และจำลองเน็ตช้า

แอปต่อเน็ตเป็นปัญหา สิบครั้งเก้าครั้งมาจาก'ส่งคำขอไม่ถูก'หรือ'แปลงคำตอบไม่ถูก' เครื่องมือดีบักมีสามอย่าง:

1. พรินต์ข้อมูลดิบ: พรินต์ String(data: data, encoding: .utf8) ออกมาดู JSON ดิบ — ชื่อฟิลด์ ชนิดข้อมูล เห็นชัดจบในตัว เร็วกว่าการเดาสิบเท่า
2. เครื่องมือดักจับแพ็กเก็ต: Proxyman ฟรีบน Mac หรือ Charles แบบโอเพนซอร์ส ดักดูคำขอและคำตอบทั้งหมดของแอปได้ เห็นชั้นเครือข่ายชัดเจนเหมือนถ่ายเอกซเรย์
3. จำลองเน็ตอ่อน: เมนู Features → Network Link Conditioner ของโปรแกรมจำลอง (ต้องดาวน์โหลดเครื่องมือจากเว็บนักพัฒนา) จำลอง 3G, ความหน่วงสูงได้ — ช่วยเจอปัญหาประสบการณ์แบบ'หมุนวนเป็นวี่เป็นวัน'

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
เคล็ดลับ: คำขอไม่ผ่าน ATS เหรอ?

{class="mt-1"}
ถ้าพอส่งคำขอก็เจอ error "App Transport Security" ทันที แปดสิบเปอร์เซ็นต์คือใช้ที่อยู่ http:// แบบไม่เข้ารหัส ปลายทางจริงต้องเป็น HTTPS ช่วงดีบักในเครื่องเปิดข้อยกเว้นชั่วคราว (เพิ่ม NSAllowsLocalNetworking ใน Info.plist) และก่อนขึ้นร้านอย่าลืมล้างให้สะอาด
:::

{class="mt-1"}
① ค้นหาอากาศได้ปกติ; ② ตัดเน็ตแล้วแอปรายงาน error อย่างมีระเบียบไม่พัง (ลองปิดเน็ตของ Mac ตอนรันในโปรแกรมจำลองดูสิ!); ③ กรอกชื่อเมืองที่ไม่มีอยู่จริง ข้อความแจ้งต้องเป็นมิตร; ④ เก็บเมืองโปรดสองเมือง ปิดเปิดแอปใหม่ยังอยู่; ⑤ ในโหมดมืดหน้าจอไม่แสบตา ผ่านครบห้าข้อ โปรเจกต์นี้ถึงจะเรียกว่าจบหลักสูตร
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
สรุปบทนี้

- ลอง API ในเบราว์เซอร์ก่อน อ่าน JSON ให้ออก แล้วค่อยเขียนโค้ด — 'การเตรียมตัว'ไม่เคยเสียเปล่า
- ซ่อน API Key ไว้ใน xcconfig ห้ามเข้าโค้ดรีโพซิทอรีเด็ดขาด
- โมเดล Codable + URLSession async/await: ฟิลด์ตรงกัน JSON แปลงให้เองอัตโนมัติ
- สถานะสามช่วง loading/success/error คือสารพัดประโยชน์ของอินเทอร์เฟซต่อเน็ต
- เน็ตหลุด, กรอกว่าง, ไม่มีเมืองนั้น — การจัดการข้อผิดพลาดคือเส้นผ่านของแอปต่อเน็ต
:::
