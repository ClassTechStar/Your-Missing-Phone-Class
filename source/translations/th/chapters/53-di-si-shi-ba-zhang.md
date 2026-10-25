---
id: di-si-shi-ba-zhang
num: 48
part: an-zhuo-kai-fa-pian
nav: บทที่ 48: รู้จัก Android — จากระบบปฏิบัติการสู่ระบบนิเวศการพัฒนา
toc: default
kind: chapter
---

### บทที่ 48: ทำความรู้จัก Android—จากระบบปฏิบัติการสู่ระบบนิเวศนักพัฒนา

{class="chapter-intro mb-4"}
ยินดีด้วยที่คุณตัดสินใจก้าวนี้—จาก "คนเล่นมือถือ" มาเป็น "คนทำแอปมือถือ" ก่อนลงมือ มาแผ่แผนที่ดูกันก่อน: Android มาจากไหน? ทำไมนักพัฒนาทั่วโลกถึงแห่กันเขียนแอปให้มัน? จากนิ้วที่พิมพ์คีย์บอร์ดของคุณจนถึงโทรศัพท์ผู้ใช้ แอปหนึ่งตัวเดินผ่านอะไรมาบ้าง?

#### 1. ชาติกำเนิดของ Android: จาก "หุ่นยนต์ตัวจิ๋ว" สู่ "ระบบที่ใหญ่ที่สุดในโลก"

เรื่องราวของ Android เริ่มปี 2003—วิศวกรชื่อ Andy Rubin ก่อตั้งบริษัท Android ขึ้น เป้าหมายเรียบง่าย: ทำระบบปฏิบัติการอัจฉริยะที่ "เข้าใจกล้องมากกว่าใคร" ต่อมา Google เข้าซื้อกิจการในปี 2005 และปี 2007 ร่วมกับผู้ผลิตหลายสิบรายก่อตั้ง Open Handset Alliance (OHA) จนเดือนกันยายน 2008 โทรศัพท์ Android รุ่นแรก HTC Dream (G1) วางขายอย่างเป็นทางการ

เรื่องต่อจากนั้นทุกคนก็รู้แล้ว: ถึงปี 2026 Android คือระบบปฏิบัติการเคลื่อนที่ที่มีส่วนแบ่งตลาดมากที่สุดในโลก อุปกรณ์ที่ใช้งานอยู่มีจำนวนหลักพันล้านเครื่อง โทรศัพท์ของคุณ กล่องทีวี จอใหญ่ในรถ นาฬิกาอัจฉริยะ ส่วนใหญ่อาจวิ่งบน Android ทั้งหมด นั่นแปลว่าอะไร? แปลว่าโค้ดทุกบรรทัดที่คุณเขียน มีโอกาสถูกใช้งานโดยคนหมู่มากที่สุดในโลก

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
เคล็ดลับ: พันธุกรรมโอเพนซอร์สของ Android

{class="mt-1"}
โค้ดแกนของ Android (AOSP, Android Open Source Project) เป็นโอเพนซอร์ส—ผู้ผลิตรายใดก็เอาไปแก้และปรับแต่งได้ เพราะงั้น Xiaomi จึงมี MIUI (ตอนนี้ชื่อ HyperOS), Huawei มีชั้นรองรับความเข้ากันได้ของ HarmonyOS, ส่วน Samsung มี One UI อันนี้ดีต่อนักพัฒนา: ที่คุณเรียนคือ "การพัฒนา Android" ไม่ใช่ "การพัฒนาของแบรนด์ใดแบรนด์หนึ่ง" ฝีมือชุดเดียว ใช้ได้กับทุกแบรนด์
:::

การวิวัฒนาการของเลขเวอร์ชันก็สนุกไม่แพ้กัน: เริ่มจาก 1.5 ชื่อ Cupcake ทุกเวอร์ชันใหญ่ใช้ชื่อขนมหวาน—Donut, Eclair, Froyo, Gingerbread... จนถึง Android 10 ปี 2019 จึงเปลี่ยนมาใช้ตัวเลขล้วน ถึงเดือนสิงหาคม 2026 เวอร์ชันทางการล่าสุดคือ Android 17 ส่วนตอนพัฒนา "เวอร์ชันขั้นต่ำที่ต้องรองรับ" ที่แอปหลักมักตั้งไว้อยู่ระหว่าง Android 8 (API 26) ถึง Android 10 (API 29)—รองรับไปถึงเครื่องเมื่อไม่กี่ปีก่อน ฐานผู้ใช้ของคุณถึงจะกว้างพอ

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">เวอร์ชัน</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ชื่อรหัส/ปี</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">สิ่งสำคัญสำหรับนักพัฒนา</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 8 (API 26)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Oreo · 2017</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ช่องทางแจ้งเตือน ข้อจำกัดการทำงานเบื้องหลัง—เส้นต่ำสุดของเครื่องรุ่นเก่าจำนวนมาก</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 10 (API 29)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2019</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เกิดระบบจัดเก็บแบบแบ่งส่วน (scoped storage) กฎการเข้าถึงไฟล์ปรับใหญ่</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 12 (API 31)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2021</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Material You ดึงสีแบบไดนามิก หน้าตาหน้าจออัปเกรดครั้งใหญ่</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 13 (API 33)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2022</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">สิทธิ์แจ้งเตือนแบบขอตอนรันไทม์ มีป็อปอัปถามว่า "จะอนุญาตให้ส่งแจ้งเตือนไหม"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 14-15 (API 34-35)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2023-2024</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">การย้อนกลับแบบคาดการณ์ หน้า 16KB ความเป็นส่วนตัวเข้มขึ้นอีกขั้น</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 16-17 (API 36-37)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2025-2026</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">จังหวะอัปเดตเวอร์ชันย่อยถี่ขึ้น บูรณาการความสามารถ AI (เช่น ส่วนขยาย Gemini)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
ประวัติย่อเวอร์ชัน Android (ณ สิงหาคม 2026 สิ่งที่นักพัฒนาต้องโฟกัส)

#### 2. เขียนด้วยภาษาอะไร: Java หรือ Kotlin?

ประวัติศาสตร์การพัฒนา Android เคยมีสองภาษาหลัก Java คือ "ผู้ก่อตั้งรุ่นแรก"—Android เกิดขึ้นก็ใช้มันเลย; Kotlin คือ "พลเมืองชั้นหนึ่ง" ที่ Google สถาปนาปี 2017 และตั้งแต่ปี 2019 ทางการประกาศชัดว่า "Kotlin ก่อน" (Kotlin-first) ถึงปี 2026 โปรเจกต์ใหม่แทบทั้งหมดใช้ Kotlin โปรเจกต์เก่าส่วนใหญ่ก็กำลังย้ายไปเรื่อย ๆ

พูดกันตรง ๆ: ถ้าคุณเริ่มจากศูนย์จริง ๆ เรียน Kotlin ไปตรง ๆ อย่าย้อนไปยุ่งกับ Java เหตุผลมีสาม: หนึ่ง โค้ด Kotlin สั้นกว่า Java 30%-40% (ฟังก์ชันเดียวกัน Kotlin กระชับและชัดกว่า); สอง มันกัน "null pointer" ฝันร้ายของมือใหม่ได้ตั้งแต่ออกแบบ; สาม บทเรียนสมัยใหม่ทั้งหมด เอกสารทางการ และเครื่องมือเขียนโปรแกรม AI (ยังจำหนังสือเขียนโปรแกรม AI ของเราได้ไหม?) ใช้ Kotlin เป็นมาตรฐาน Java จะเจอแค่ตอนดูแลโปรเจกต์เก่าหรืออ่านโค้ดเก่าเท่านั้น

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
สไตล์ Java (เวอร์ชันเยอะคำ)

{class="font-mono text-xs leading-relaxed"}
public class MainActivity extends Activity {<br>&nbsp;&nbsp;@Override<br>&nbsp;&nbsp;protected void onCreate(Bundle b) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b);<br>&nbsp;&nbsp;&nbsp;&nbsp; setContentView(R.layout.activity);<br>&nbsp;&nbsp;}<br>}
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
สไตล์ Kotlin (เวอร์ชันกระชับ)

{class="font-mono text-xs leading-relaxed"}
class MainActivity : ComponentActivity() {<br>&nbsp;&nbsp;override fun onCreate(b: Bundle?) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b)<br>&nbsp;&nbsp;&nbsp;&nbsp;setContent { App() }<br>&nbsp;&nbsp;}<br>}
:::
:::

ทำงานเดียวกัน Kotlin ตัดวงเล็บปีกกาและโค้ดบังคับไปเยอะ บทที่ 50 เราจะเรียนมันอย่างจริงจัง ตอนนี้คุณแค่ต้องจำว่า: "ภาษากลาง" ของการพัฒนา Android ชื่อว่า Kotlin

#### 3. แอปหนึ่งตัวถือกำเนิดขึ้นได้อย่างไร?

หลายคนคิดว่า "พัฒนาแอป" ก็คือเปิดคอมพิวเตอร์แล้วพิมพ์โค้ดเละเทะ จริง ๆ แล้ว จากไอเดียจนถึงโทรศัพท์ผู้ใช้ แอปหนึ่งตัวต้องผ่านสายการผลิตประมาณนี้:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-lightbulb mr-1"></i> ไอเดีย</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center">📐 ออกแบบ (UI+ฟังก์ชัน)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-keyboard mr-1"></i> เขียนโค้ด</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hammer mr-1"></i> คอมไพล์และแพ็ก (APK/AAB)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> ทดสอบ (โปรแกรมจำลอง+เครื่องจริง)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-rocket mr-1"></i> เผยแพร่ (สโตร์/ไฟล์ติดตั้ง)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
ภาพที่ 1: ขั้นตอนครบวงจรจากไอเดียถึงการขึ้นสโตร์ของแอป Android
:::

ในกระบวนการนี้มีสองคำที่คุณต้องรู้จักตั้งแต่ตอนนี้:

- APK: รูปแบบไฟล์ติดตั้งของแอป Android (.apk) ดับเบิลคลิกก็ติดตั้งลงมือถือได้ เหมือน .exe ของ Windows ใช้ตอนทดสอบเอง หรือส่งให้เพื่อนเล่น
- AAB: Android App Bundle (.aab) รูปแบบบรรจุ "ขั้นสูง" ที่ใช้ขึ้น Google Play สโตร์จะตัดส่วนที่ไม่จำเป็นแบบไดนามิกตามรุ่นโทรศัพท์ของผู้ใช้ ทำให้ทุกคนดาวน์โหลดแพ็กเกจเล็กลง ติดตั้งเองไม่ได้ ต้องส่งให้สโตร์เท่านั้น

อีกหนึ่งคำที่คุณจะได้ยินบ่อย ๆ คือ SDK (Software Development Kit) มันคือชุด "อุปกรณ์พัฒนา" ครบเครื่องจาก Android ทางการ—รวมไลบรารี API ทุกเวอร์ชัน เครื่องมือดีบั๊ก อิมเมจโปรแกรมจำลอง ฯลฯ คลาสอย่าง Activity, Button ที่คุณเรียกใช้ตอนเขียนโค้ด ล้วนมาจาก SDK

#### 4. ภาพรวมเทคสแตกของ Android: "รายการอาวุธ" ของคุณ

ก่อนเรียนอย่างเป็นทางการ มาทำความรู้จักการตั้งค่ามาตรฐานของโปรเจกต์ Android ยุคหลักปี 2026 ก่อน—ตอนนี้ดูรายการนี้แล้วไม่เข้าใจไม่เป็นไร พอเรียนจบทั้งเล่มกลับมาดูอีกที จะเข้าใจโปร่งเลย:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ชั้น</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ทางเลือกหลัก (2026)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ใช้ทำอะไร</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ภาษา</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin 2.x</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ภาษาที่ใช้เขียนตรรกะ</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">อินเทอร์เฟซ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jetpack Compose + Material 3</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">วาดอินเทอร์เฟซด้วยโค้ด (สายหลักของเล่มนี้)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">สถาปัตยกรรม</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MVVM + ViewModel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">แยกอินเทอร์เฟซกับตรรกะออกจากกัน โค้ดไม่รก</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">การจัดเก็บข้อมูล</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room (ฐานข้อมูล) + DataStore (การตั้งค่า)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เก็บข้อมูลลงโทรศัพท์</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เครือข่าย</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit + OkHttp + Kotlin coroutines</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">คุยกับเซิร์ฟเวอร์</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เครื่องมือบิลด์</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle + Kotlin DSL</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เปลี่ยนโค้ดเป็นแพ็กเกจติดตั้ง</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">สภาพแวดล้อมการพัฒนา</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">IDE "ครบเครื่อง" จากทางการ Google</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
สแตกเทคโนโลยี Android หลักปี 2026 ฉบับย่อ

อย่าตกใจกับสายชื่อภาษาอังกฤษยาว ๆ พวกนี้ มันเหมือนหม้อหวดจานชามในครัว—ตอนนี้คุณแค่ต้องรู้ว่า "ทำกับข้าวต้องเข้าครัว" ส่วนเครื่องมือแต่ละชิ้นใช้ยังไง บทต่อ ๆ ไปจะแกะให้ดูทีละชิ้น และข่าวดีคือ: ตอน Android Studio สร้างโปรเจกต์ใหม่ มันจะตั้งค่าชุดนี้ให้เสร็จอัตโนมัติ คุณแค่เข้าครัวผัดเท่านั้น

#### 5. Android vs iOS: บทเรียนแรกของนักพัฒนาเรื่อง "เลือกฝั่ง"

คุณอาจมีทั้งเครื่อง Android และ Apple อยู่ในมือ ในฐานะนักพัฒนา ความต่างของประสบการณ์สองฝั่งควรรู้ไว้ล่วงหน้า—ไม่ใช่การจับข้างว่า "ฝั่งไหนดีกว่า" แต่คือบัญชีความจริงว่า "ฝั่งไหนเหมาะกับการเริ่มต้นของคุณ" มากกว่า:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">มิติ</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">พัฒนา Android</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">พัฒนา iOS</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">คอมพิวเตอร์ที่ใช้พัฒนา</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Windows / Mac / Linux ก็ได้หมด</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ต้อง Mac เท่านั้น (Xcode ใช้ได้เฉพาะ Mac)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เครื่องมือพัฒนา</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio (ฟรี)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode (ฟรี) + ค่าบอกรายปี 99 ดอลลาร์</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">การตรวจสอบก่อนขึ้นสโตร์</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">หลวม ใช้เวลาไม่กี่ชั่วโมงถึงไม่กี่วัน</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เข้มงวด 1-7 วันคือเรื่องปกติ</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ติดตั้งลองเล่นเอง</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">APK ส่งได้ลงได้ตามใจ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">การเผยแพร่มีข้อจำกัด การทดสอบต้องเซ็นแอป/ผ่าน TestFlight</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">สภาพแวดล้อมการหารายได้</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">พึ่งโฆษณา/ช่องทางในประเทศเป็นหลัก</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ผู้ใช้ App Store จ่ายเงินซื้อของในแอปกันง่ายกว่า</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ต้นทุนการเรียนรู้</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">มีคอนเซปต์เยอะ (เช่น คอมโพเนนต์หลักทั้งสี่)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">อีโคไซสเต็มปิด แต่ระบบเป็นมาตรฐานเดียวกัน เอกสารมีคุณภาพ</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
เปรียบเทียบเส้นทางการพัฒนา Android กับ iOS (สิงหาคม 2026)

พูดตรง ๆ กันเลยนะ: ถ้าคอมพิวเตอร์ของคุณไม่ใช่ Mac ก็ไม่ต้องลังเลอะไรเลย — Android คือทางเลือกเดียวที่มี แต่ถ้าคุณมี Mac ภาคที่ 8 กับ 9 ของหนังสือเล่มนี้เปิดเทียบกันอ่านได้ แนวคิดการเขียนโปรแกรมเหมือนกัน เรียนจบฝั่งหนึ่งแล้วไปเรียนอีกฝั่งจะไวขึ้นเยอะ

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ลงมือทำด้วยกัน: ดู "Android" ในมือถือของคุณ

{class="mt-1"}
เปิด [การตั้งค่า] บนมือถือ → [เกี่ยวกับโทรศัพท์] (หรือ "เกี่ยวกับเครื่อง") แล้วหาแถว "เวอร์ชัน Android" — แตะตรงนั้นติดกันหลายครั้ง ยังเปิดมินิเกมอีสเตอร์เอกซ์ของระบบได้อีกด้วย จดเลขเวอร์ชันของคุณไว้ แล้วเทียบกับตารางเวอร์ชันด้านบนดูว่าเป็นรุ่นที่เท่าไร มือถือของคุณนี่แหละคือ "เครื่องทดสอบ" ตัวแรกของคุณ
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
สรุปบทนี้

- Android เกิดปี 2008 และปี 2026 เป็นระบบปฏิบัติการมือถือที่มีส่วนแบ่งตลาดโลกสูงที่สุด มีอุปกรณ์ใช้งานจริงหลายพันล้านเครื่อง
- เวอร์ชันทางการล่าสุดคือ Android 17; แอปยอดนิยมรองรับขั้นต่ำ Android 8-10 เพื่อให้ฐานผู้ใช้ใหญ่พอ
- โปรเจกต์ใหม่ใช้ Kotlin ไปเลยทั้งหมด: โค้ดน้อยลง 30%+ กัน NullPointerException และเป็นภาษาที่ทางการรับรอง
- APK ติดตั้งเองได้ AAB ไว้ขึ้นสโตร์; SDK คือชุดเครื่องมือพัฒนาอย่างเป็นทางการ
- สแตกเทคโนโลยีมาตรฐานปี 2026: Kotlin + Compose + MVVM + Room + Retrofit + Gradle + Android Studio
:::
