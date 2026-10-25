---
id: di-wu-shi-er-zhang
num: 52
part: an-zhuo-kai-fa-pian
nav: บทที่ 52: องค์ประกอบหลัก 4 ตัวและวงจรชีวิตของ Activity
toc: default
kind: chapter
---

### บทที่ 52: คอมโพเนนต์ทั้งสี่กับวงจรชีวิตของ Activity

{class="chapter-intro mb-4"}
ถ้า Compose คือ "ใบหน้า" ของแอป บทนี้ก็คือเรื่อง "โครงกระดูก" ของแอป ระบบ Android มีคอมโพเนนต์พื้นฐานสี่ตัว แอปทุกตัวประกอบขึ้นจากมัน และในบรรดานั้น Activity สำคัญที่สุด มี "แผนภาพวงจรชีวิต" ที่นักพัฒนา Android ทุกคนต้องสลักไว้ในหัว จบบทนี้ คุณจะเข้าใจปริศนาอมตะอย่าง "ทำไมสลับไปแอปอื่นแล้วกลับมา สถานะในแอปฉันหายหมด"

#### 1. คอมโพเนนต์ทั้งสี่: "เสาหลัก" ของ Android

ทางการ Android กำหนดคอมโพเนนต์พื้นฐานไว้สี่แบบ แบ่งกันรับผิดชอบงานคนละประเภท:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">คอมโพเนนต์</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">หน้าที่</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">เปรียบเทียบง่าย ๆ</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activity</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">หน้าจอที่มองเห็นได้</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">หน้าร้าน — ผู้ใช้มองเห็นและโต้ตอบได้</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Service</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"คนล่องหน" ทำงานเบื้องหลัง</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">คนงานคลัง — เปิดเพลง ดาวน์โหลดไฟล์ ไม่ต้องมีหน้าจอ</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BroadcastReceiver</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">รับการแจ้งจากระบบ (broadcast)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ห้องรับสาร — ลำโพงประกาศ "แบตหมด" "เน็ตหลุด"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ContentProvider</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">แชร์ข้อมูลข้ามแอป</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ตู้เอกสารส่วนกลาง — เช่น แชร์รายชื่อผู้ติดต่อให้แอปอื่น</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
ภาพรวมคอมโพเนนต์ทั้งสี่ของ Android

ช่วงมือใหม่ คุณใช้เวลา 95% กับ Activity ส่วน Service กับ BroadcastReceiver ใช้ตอนทำเล่นเพลง ส่งการแจ้งเตือน และ ContentProvider ใช้น้อยที่สุด (ระบบห่อข้อมูลที่ใช้บ่อยไว้ให้แล้ว) อีกเรื่องต้องระวัง: คอมโพเนนต์ทั้งสี่ต้อง "ขึ้นทะเบียน" ใน AndroidManifest.xml ด้วย ไม่ขึ้นทะเบียนระบบก็หาไม่เจอ

#### 2. วงจรชีวิตของ Activity: "แผนที่ขุมทรัพย์" แผนแรกของนักพัฒนา Android

แอปบนมือถือถูกขัดจังหวะได้ทุกเมื่อ: สายเรียกเข้า ผู้ใช้สลับไปตอบแชท หน่วยความจำระบบไม่พอเลยโดนฆ่าทิ้ง... ชีวิตหนึ่งของ Activity ก็คือการเดินทางวนไปมาบนแผนภาพนี้:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onCreate (เกิด: เริ่มต้น)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onStart (มองเห็นแล้ว)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onResume (อยู่พื้นหน้า กำลังโต้ตอบ)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onPause (ถูกบังบางส่วน)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onStop (มองไม่เห็นเลย)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center">onDestroy (ทำลาย)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">🔁 onRestart / onStart / onResume: กลับพื้นหน้าด้วยเส้นทางเดิม</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
ภาพที่ 4: วงจรชีวิตของ Activity (ไปข้างหน้า: แถวบนเกิด → แถวล่างออกจากฉาก ตอนกลับก็ย้อนเส้นทางเดิม)
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Callback</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">เกิดขึ้นเมื่อไร</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">การใช้งานทั่วไป</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onCreate</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ตอน Activity ถูกสร้าง (ครั้งเดียว)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">โหลดหน้าจอ กำหนดค่าเริ่มต้นข้อมูล</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStart</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">หน้าจอกลายเป็นมองเห็นได้</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เริ่มตรรกะเบา ๆ บางอย่าง</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onResume</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ได้โฟกัส พร้อมโต้ตอบ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เริ่มอนิเมชัน เล่นต่อ</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onPause</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ถูกบังบางส่วน/เพิ่งถูกสลับออก</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">หยุดอนิเมชันชั่วคราว บันทึกฉบับร่าง</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStop</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">มองไม่เห็นเลยสักนิด</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">คืนทรัพยากรหนัก พักการดาวน์โหลด</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onDestroy</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ก่อนถูกทำลาย</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">การเก็บกวาดครั้งสุดท้าย</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
การใช้งานทั่วไปของ callback วงจรชีวิตทั้งหก

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ข้อควรระวัง: หมุนหน้าจอจะ "ฆ่า" Activity

{class="mt-1"}
ฉากพลาดคลาสสิกที่สุดของมือใหม่: หมุนหน้าจอทีเดียว ข้อความในช่องกรอกหายหมด เหตุผล: หมุนหน้าจอโดยค่าเริ่มต้นจะทำลายและสร้าง Activity ใหม่ (เดินผ่าน onDestroy → onCreate หนึ่งรอบ) ทางแก้: ใช้ rememberSaveable เก็บสถานะ (ตัวแทนของ remember ใน Compose) มันจะกู้ค่ากลับมาให้เองตอนสร้างใหม่ จะได้ใช้ซ้ำอยู่บ่อย ๆ ในบทที่ 6 กับ 7
:::

#### 3. Intent: "ตั๋วโดยสาร" เดินทางเข้าออกแอป

Intent (เจตนา) คือ "ตั๋ว" ที่ใช้สื่อสารระหว่างคอมโพเนนต์ อยากกระโดดจากหน้าหนึ่งไปอีกหน้า หรือเปิดเบราว์เซอร์ เรียกกล้อง ก็ต้อง "ซื้อตั๋วขึ้นรถ" ทั้งนั้น:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · เปลี่ยนหน้าด้วย Intent</span><span class="dots">···</span>
:::

```
// แบบที่หนึ่ง: Intent แบบชัด—ระบุปลายทางเองเลย
val intent = Intent(this, DetailActivity::class.java)
intent.putExtra("name", "ซานผวน")     // เหมือนฝาก "สัมภาระ" ขึ้นรถ (ข้อมูล)
startActivity(intent)

// แบบที่สอง: Intent แบบนัย—บอกแค่จะทำอะไร ระบบหาตัวทำเอง
val web = Intent(Intent.ACTION_VIEW, Uri.parse("https://developer.android.com"))
startActivity(web)   // ระบบจะเปิดเบราว์เซอร์/หรือให้คุณเลือก
```
:::

สองแบบมีหน้าที่คนละแบบ: แบบชัดเจน (explicit) ใช้กระโดดหน้าภายในแอปตัวเอง ส่วนแบบโดยนัย (implicit) ใช้เรียกความสามารถของระบบหรือแอปอื่น (เปิดเว็บ โทรออก แชร์) ในโปรเจกต์ Compose อยู่ใน Composable ใช้ LocalContext.current ดึง Context มาแล้วเรียก startActivity ได้เลย

#### 4. หลายหน้ากับการนำทาง

แอปจริง ๆ มีหลายหน้า วิธีนำทางที่ทางการแนะนำสำหรับ Compose คือ Navigation Compose (ไลบรารี androidx.navigation):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · โครง Navigation Compose</span><span class="dots">···</span>
:::

```
val navController = rememberNavController()

NavHost(navController, startDestination = "home") {
    composable("home") { HomeScreen(navController) }
    composable("detail/{name}") { entry ->
        val name = entry.arguments?.getString("name")
        DetailScreen(name ?: "ไม่ทราบ")
    }
}

// เปลี่ยนหน้าในหน้าจอ:
navController.navigate("detail/ซานผวน")     // พร้อมพารามิเตอร์
navController.popBackStack()              // กลับหน้าก่อนหน้า
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
เคล็ดลับ: หน้าเยอะขึ้นแล้วทำยังไงดี?

{class="mt-1"}
พอโปรเจกต์โตขึ้น ให้รวมเส้นทาง (route) ของทุกหน้าไว้ในไฟล์เดียว (เช่น AppNavGraph.kt) จัดการแบบศูนย์กลาง อย่าปล่อยให้ตรรกะ "จะกระโดดไปไหน" กระจัดกระจายอยู่ตามแต่ละหน้า นี่คือก้าวแรกจาก "รันได้" สู่ "ดูแลต่อได้"
:::

#### 5. รู้จักไว้ระหว่างทาง: Fragment คืออะไร (และทำไมหนังสือเล่มนี้ไม่สอน)

ค้นหาบทเรียนเก่าเมื่อไร คุณต้องเจอ Fragment แน่ ๆ — มันคือ "ชิ้นส่วนหน้าจอที่ใช้ซ้ำได้" อยู่ใน Activity เป็นพระเอกตัวจริงในสถาปัตยกรรมหลายหน้าแบบเก่า แต่ยุค Compose ทำหน้าด้วยฟังก์ชัน Composable + เส้นทาง Navigation ก็พอแล้ว ทางการก็ลดบทบาท Fragment ลง หนังสือเล่มนี้จึงไม่ใส่มันไว้ในเส้นทางหลัก

คำแนะนำสำหรับคุณ: โปรเจกต์ใหม่ไม่ต้องไปใช้ Fragment เอง แต่พออ่านโค้ดเก่าหรือโดนถามตอนสัมภาษณ์ แค่รู้ว่ามันคือ "ชิ้นส่วนหน้าจอที่ฝังอยู่ใน Activity" ก็พอ แหล่งเรียนรู้ให้เลือกที่เป็นหลังปี 2023 เป็นอันดับแรกเสมอ — "ปฏิทินเก่า" ของสแตกเทคโนโลยี Android อัปเดตเร็วกว่าที่คิด

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ลงมือทำด้วยกัน: ใส่ "ความจำ" ให้ตัวนับ

{class="mt-1"}
ปรับตัวนับจากบทที่ 51: 1) เปลี่ยน remember เป็น rememberSaveable แล้วหมุนหน้าจอดูว่าเลขยังอยู่ไหม; 2) เพิ่มปุ่ม "เกี่ยวกับ" ใช้ Navigation กระโดดไปหน้าที่สองแสดงหมายเลขเวอร์ชัน; 3) พิมพ์ log (Log.d) ใน onCreate/onPause ของทั้งสองหน้า แล้วใช้ Logcat ดูลำดับการเรียกวงจรชีวิต ทำครบสามข้อนี้ วงจรชีวิตก็ไม่ใช่แค่ทฤษฎีบนกระดาษอีกต่อไป
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
สรุปบทนี้

- คอมโพเนนต์ทั้งสี่: Activity (หน้าร้าน), Service (เบื้องหลัง), BroadcastReceiver (ลำโพง), ContentProvider (ตู้เอกสาร)
- callback วงจรชีวิตหกตัว: onCreate → onStart → onResume → onPause → onStop → onDestroy
- หมุนหน้าจอจะทำลายและสร้าง Activity ใหม่: ใช้ rememberSaveable ช่วยรักษาสถานะ
- Intent คือ "ตั๋ว": แบบชัดเจนกระโดดหน้าในแอปตัวเอง แบบโดยนัยเรียกใช้ความสามารถของระบบ
- หลายหน้าใช้ Navigation Compose: เส้นทาง NavHost + composable
:::
