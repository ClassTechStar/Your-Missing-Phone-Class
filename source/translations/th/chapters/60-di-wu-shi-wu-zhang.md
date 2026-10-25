---
id: di-wu-shi-wu-zhang
num: 55
part: an-zhuo-kai-fa-pian
nav: บทที่ 55: โปรเจกต์ 2 — แอปดูอากาศ (เวอร์ชันออนไลน์)
toc: default
kind: chapter
---

### บทที่ 55: โปรเจกต์ที่ 2 — แอปค้นหาสภาพอากาศ (เวอร์ชันออนไลน์)

{class="chapter-intro mb-4"}
แอปบันทึกบัญชีคือการ "ฝึกพื้นฐานภายใน" แอปสภาพอากาศคือการ "ออกไปเห็นโลกกว้าง" — มันต้องคุยกับอินเทอร์เน็ต ในโปรเจกต์นี้คุณจะได้เรียน: สมัคร API ฟรี แปลง JSON จัดการสถานะหน้าจอสามแบบ "กำลังโหลด/สำเร็จ/ล้มเหลว" และวิธีซ่อนคีย์ API ให้มิดชิด ทำเสร็จ คุณก็มีความสามารถทำ "แอปที่ต่อเน็ต" ได้ทุกแบบ — ข่าว อัตราแลกเปลี่ยน คำแปล สูตรเดียวกันหมด

#### 1. สมัคร API สภาพอากาศฟรี

ฝึกมือส่วนตัว แนะนำ OpenWeatherMap หรือค่าย QWeather — ทั้งคู่มีโควตาใช้ฟรี สมัครเสร็จใช้ได้ทันที ยกตัวอย่าง OpenWeatherMap:

1. สมัครบัญชี → ไปที่หน้า API keys สร้าง Key หนึ่งตัว (apikey);
2. เวอร์ชันฟรีเรียกใช้เอนด์พอยต์ Current Weather (สภาพอากาศปัจจุบัน) ได้: api.openweathermap.org/data/2.5/weather? q=beijing&appid=คีย์ของคุณ&units=metric;
3. ลองยิงในเบราว์เซอร์สักครั้งก่อน ดูว่า JSON ที่คืนมาหน้าตาเป็นยังไง — นี่คือการ "เตรียมบทเรียน" ที่ต้องทำก่อนเชื่อม API ใด ๆ

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ข้อควรระวัง: ห้ามเขียนคีย์ฝังไว้ในโค้ดเด็ดขาด

{class="mt-1"}
API Key เทียบเท่า "รหัสกระเป๋าเงิน" ของคุณ พอเขียนลงโค้ดแล้วคอมมิตขึ้น GitHub ไม่กี่ชั่วโมงก็จะถูกบอตกวาดไปใช้ฟรี วิธีที่ถูกต้อง: ใส่ไว้ใน local.properties (ไฟล์นี้ถูก gitignore ไม่สนใจอยู่แล้ว) แล้วอ่านเข้าโค้ดผ่าน buildConfig ของ Gradle ค้นหา "best practice ซ่อน API Key บน Android" แล้วทำตามก็พอ
:::

#### 2. ชั้นเครือข่าย: Retrofit + การแปลง JSON

นิยาม "โมเดลข้อมูล" ตาม JSON ที่ API คืนมาก่อน ฟิลด์ไหนไม่ตรงก็ตัดทิ้งทั้งหมด:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · โมเดลข้อมูล + อินเทอร์เฟซ</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"แจ่มใส"}],"main":{"temp":26.5,"humidity":40},"name":"ปักกิ่ง"}
data class WeatherResponse(
    val weather: List&lt;Weather&gt;,
    val main: Main,
    val name: String
)
data class Weather(val description: String)
data class Main(val temp: Double, val humidity: Int)

interface WeatherApi {
    @GET("data/2.5/weather")
    suspend fun getWeather(
        @Query("q") city: String,
        @Query("appid") key: String,
        @Query("units") metric: String = "metric",
        @Query("lang") lang: String = "zh_cn"
    ): WeatherResponse
}
```
:::

Gson จะยัด JSON ลง data class เหล่านี้ให้เองอัตโนมัติ — ชื่อฟิลด์ตรงกัน เวทมนตร์ก็เกิดเอง

#### 3. สถานะหน้าจอสามแบบ: กำลังโหลด / สำเร็จ / ล้มเหลว

ดวงวิญญาณของแอปออนไลน์อยู่ที่ "การจัดการสถานะ" เน็ตช้า เน็ตหลุด พิมพ์ชื่อเมืองผิด... ทุกกรณีหน้าจอต้องอธิบายให้ผู้ใช้เข้าใจ ใช้ sealed class (คลาสปิด) แสดงอย่างสวยงาม:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · สเตตของ UI</span><span class="dots">···</span>
:::

```
sealed class UiState {
    object Loading : UiState()                    // กำลังหมุน
    data class Success(val data: WeatherResponse) : UiState()  // สำเร็จ
    data class Error(val message: String) : UiState()          // ล้มเหลว
}

// ใน ViewModel:
fun search(city: String) {
    viewModelScope.launch {
        _state.value = UiState.Loading
        _state.value = try {
            UiState.Success(api.getWeather(city))
        } catch (e: Exception) {
            UiState.Error("หาเมืองนี้ไม่เจอ ลองชื่ออื่นไหม?")
        }
    }
}

// ในหน้าจอ:
when (val s = state) {
    is UiState.Loading -&gt; CircularProgressIndicator()   // หมุนรอ
    is UiState.Success -&gt; WeatherContent(s.data)        // แสดงผล
    is UiState.Error -&gt; Text(s.message)                 // แสดงข้อผิดพลาด
}
```
:::

สามช่วง Loading/Success/Error นี้คือ "เทมเพลตสารพัดประโยชน์" ของหน้าจอออนไลน์ ท่องไว้ก่อน ต่อไปทำแอปออนไลน์อะไรก็ลอกแบบได้เลย

#### 4. โค้ดหน้าจอลงมือจริง: วาดสภาพอากาศออกมา

มีสถานะแล้ว หน้าจอหน้าตาเป็นแบบนี้ (ช่วงสำคัญ):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · หน้าจอ weather (ส่วนสำคัญ)</span><span class="dots">···</span>
:::

```
@Composable
fun WeatherContent(data: WeatherResponse) {
    Column(
        Modifier.fillMaxSize().padding(24.dp),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text(data.name, fontSize = 28.sp, fontWeight = FontWeight.Bold)
        Text(
            "${data.main.temp}°C",
            fontSize = 72.sp,
            fontWeight = FontWeight.Light
        )
        Text(
            data.weather.firstOrNull()?.description ?: "ไม่ทราบ",
            fontSize = 20.sp,
            color = Color.Gray
        )
        Spacer(Modifier.height(16.dp))
        Row {
            Text("💧 ความชื้น ${data.main.humidity}%")
            Spacer(Modifier.width(24.dp))
            Text("🌡️ รู้สึกเหมือน ${data.main.temp}°C")
        }
    }
}
```
:::

รายละเอียดเล็ก ๆ ที่ควรเรียนมี: firstOrNull() หยิบตัวแรกอย่างปลอดภัย (ลิสต์อาจว่าง) และ ?: "ไม่ทราบ" ให้ข้อความสำรอง — หลัก null safety ใช้กับหน้าจอได้เหมือนกัน อุณหภูมิใช้ฟอนต์ใหญ่ 72.sp อวดโฉม น้ำหนัก "บาง" (Light) ทำให้ตัวเลขดูสง่างาม นี่คือสูตรคลาสสิกของแอปสภาพอากาศ

#### 5. รายละเอียดหน้าจอกับการโต้ตอบ

- ช่องค้นหา: TextField ด้านบน พิมพ์ชื่อเมืองแล้วกดค้นหา (ตั้ง action "ค้นหา" บนคีย์บอร์ด กด Enter ก็ค้นทันที);
- การ์ดสภาพอากาศ: อุณหภูมิฟอนต์ใหญ่ (26.5°) คำอธิบายสภาพอากาศ (แดดออก) ความชื้น ชื่อเมือง;
- เมืองโปรด: เก็บเมืองที่ดูบ่อยลง DataStore เปิดครั้งหน้าค้นให้เอง — ได้ทบทวนบทที่ 6 ไปในตัว;
- ดึงลงเพื่อรีเฟรช: ใน Compose ใช้ PullToRefreshBox (มาจาก Material 3) ความรู้สึกใช้งาน "มืออาชีพ" ขึ้นทันที

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
เคล็ดลับ: รูปภาพทำให้หน้าจอมีชีวิต

{class="mt-1"}
จับคู่ emoji หรือไอคอนกับสภาพอากาศแต่ละแบบ (☀️🌧️❄️) แล้ว map ด้วย when(description) — สามบรรทัด ความอบอุ่นของหน้าจอเพิ่มเท่าตัว จะโหลดไลบรารีไอคอนสภาพอากาศของบุคคลที่สามก็ได้ แต่ช่วงฝึกมือ emoji ก็พอแล้ว
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ลงมือทำด้วยกัน: เช็กลิสต์ตรวจรับแอปสภาพอากาศ

{class="mt-1"}
1) ค้นหาสภาพอากาศได้ตามปกติ; 2) ปิดเน็ตแล้วแอปแสดง error อย่างสวยงามไม่พัง (ลองเปิดโหมดเครื่องบิน!); 3) พิมพ์เมืองที่ไม่มีจริง ให้ข้อความแนะนำที่เป็นมิตร; 4) เก็บเมืองโปรดสองเมือง ปิดเปิดแอปใหม่ยังอยู่; 5) หมุนหน้าจอสถานะไม่หาย ผ่านครบห้าข้อ โปรเจกต์นี้ถึงจะเรียนจบ
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
สรุปบทนี้

- ลองยิง API ในเบราว์เซอร์ อ่าน JSON ให้เข้าใจก่อน แล้วค่อยเขียนโค้ด — "เตรียมตัวก่อน" ไม่มีวันเสียเปล่า
- ซ่อน API Key ไว้ใน local.properties ห้ามเข้า repository โค้ดเด็ดขาด
- อินเทอร์เฟซ Retrofit + data class: ฟิลด์ตรงกัน JSON แปลงเองอัตโนมัติ
- สถานะสามช่วง Loading/Success/Error คือเทมเพลตสารพัดประโยชน์ของหน้าจอออนไลน์
- เน็ตหลุด ป้อนค่าว่าง เมืองไม่มีจริง — การจัดการ error คือเส้นผ่านของแอปออนไลน์
:::
