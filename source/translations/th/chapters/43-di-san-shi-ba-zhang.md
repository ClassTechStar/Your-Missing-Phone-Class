---
id: di-san-shi-ba-zhang
num: 38
part: ai-biancheng-pian
nav: บทที่ 38: หลักคิด 5 ข้อของการเขียนโปรแกรมด้วย AI
toc: default
kind: chapter
---

### บทที่ 38: หลักคิดทั้งห้าของการเขียนโปรแกรมด้วย AI

{class="chapter-intro mb-4"}
ถ้าหนังสือเล่มนี้ให้คุณจำได้แค่บทเดียว บทนั้นต้องเป็นบทนี้ หลักคิดทั้งห้าคือหัวใจของทั้งเล่ม บททั้งหมดที่เหลือ ไม่ว่าบริบท ความต้องการ การสนทนา คุณภาพ ล้วนเป็นการขยายห้าหลักนี้ออกไปในสถานการณ์ต่าง ๆ เท่านั้น อุ่นใจได้ว่าแต่ละข้อไม่ยากจนเกินเข้าใจ แต่แต่ละข้อก็คุ้มที่จะเอาไปเข้าโปรเจกต์สักหลายชิ้นเพื่อ "กล่อมลงไปในกล้ามเนื้อ"

จุดเริ่มของเรื่องนี้สนุกดี: ตอน Andrej Karpathy เปิดโอเพนซอร์สโปรเจกต์ของเขา เขาแนบไฟล์ CLAUDE.md ที่มีแค่ 70 บรรทัด สรุปหลักการทำงานร่วมกับ AI แกนกลาง 4 ข้อ ไฟล์นี้ได้ Star บน GitHub เกิน 70,000 ดวง กลายเป็นแนวปฏิบัติที่คนทำ AI programming ทั่วโลกอ้างถึงมากที่สุด สี่หลักนี้ไม่ใช่สโลแกนลอย ๆ แต่เป็นนิสัยการคิดที่ปฏิบัติได้ กลั่นมาจากประสบการณ์จริงจำนวนมาก หนังสือเล่มนี้เติมข้อที่ห้าบนรากฐานนั้น - การทำซ้ำและตรวจสอบ - ให้ครบเป็นระบบหลักทั้งห้า

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ไฟล์ 70 บรรทัดทำไมมีค่าขนาดนั้น?

{class="mt-1"}
Star 70,000 ดวงแปลว่าอะไร? โปรเจกต์ส่วนใหญ่บน GitHub แปดปุ๊บแปดปั๊บไม่ถึงตัวเลขนี้ทั้งชีวิต ไฟล์ข้อความ 70 บรรทัดได้มาขนาดนี้ พิสูจน์สิ่งหนึ่งพอดี ๆ: ของหายากที่สุดในยุค AI ไม่ใช่โค้ด แต่คือความสามารถ "คิดให้ชัด" 70 บรรทัดนี้แหละคือฉบับข้นของ "คิดให้ชัด"
:::

#### 1. หลักข้อที่หนึ่ง: Think Before Coding (คิดก่อน แล้วค่อยโค้ด)

นี่คือข้อที่ย้อนสัญชาตญาณที่สุดในห้าข้อ ถ้า AI ช่วยเขียนโค้ดได้แล้ว ทำไมยังต้อง "คิดก่อน"? คำตอบง่ายมาก: คุณภาพผลงานของ AI สัมพันธ์ตรงกับคุณภาพของสิ่งที่คุณป้อน ถ้าตัวคุณเองยังคิดไม่ชัดว่าจะทำอะไร คำตอบจาก AI จะดึงคุณเข้าวงจร "แก้แล้วแก้อีก" ไม่จบ - ที่คนเรียกกันติดปากว่า "AI หลงทางไปพร้อมคุณ"

"คิดก่อน" หมายความว่าก่อนจะสั่ง AI คุณต้องตอบสามคำถาม ซึ่งประกอบกันเป็น "สามเหลี่ยมแห่งการคิด" ที่ขาดอย่างใดอย่างหนึ่งไม่ได้:

1. ฉันจะแก้ปัญหาอะไร? (เป้าหมาย)
2. ผลลัพธ์ที่ฉันอยากได้หน้าตาเป็นอย่างไร? (เกณฑ์ตรวจรับ)
3. มีข้อจำกัดอะไรที่ต้องยึดตาม? (ขอบเขต)

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">มุมคิด</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">อินพุตคลุมเครือ (ไม่ดี)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">อินพุตชัดเจน (ดี)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">นิยามปัญหา</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ช่วยทำเว็บให้หน่อย</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ช่วยทำเว็บเครื่องมือส่วนตัวหนึ่งเว็บ แสดงการ์ดทางเข้าของเครื่องมือ AI เล็ก ๆ 3 ตัว</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ผลลัพธ์ที่คาดหวัง</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">สวยขึ้นหน่อย</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เลย์เอาต์แบบรองรับทุกขนาดจอ (responsive) ธีมมืด การ์ดมีแอนิเมชันตอนชี้เมาส์ ใช้บนมือถือได้</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ข้อจำกัด</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">(ไม่ได้ระบุ)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ไม่ใช้เฟรมเวิร์ก ใช้ HTML+CSS+JS ล้วน ดีพลอยเป็นไฟล์เดียว ไม่ต้องมีแบ็กเอนด์</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
เปรียบเทียบอินพุตคลุมเครือกับอินพุตชัดเจนสำหรับความต้องการเดียวกัน

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ระวัง: คิดก่อน ≠ เขียนเอกสารสมบูรณ์แบบก่อน

{class="mt-1"}
"คิดก่อน" ไม่ได้แปลว่า "เขียน PRD สมบูรณ์แบบสักฉบับแล้วค่อยเริ่ม" มันคือกระบวนการคิดที่ไวแต่มีระเบียบ ใช้เวลา 30 วินาทีคิดให้ชัดสามคำถามข้างบน คุ้มกว่าใช้ 30 นาทีแก้ไปมาในแชทมาก งานเล็ก สามคำถามสั้น ๆ ก็พอ โปรเจกต์ใหญ่ค่อยขยายมันเป็นเอกสารความต้องการฉบับเต็ม (ดูบทที่ 40)
:::

#### 2. หลักข้อที่สอง: Simplicity First (ความเรียบง่ายมาก่อน)

กับดักใหญ่ที่สุดของการเขียนโปรแกรมด้วย AI ไม่ใช่ "ทำไม่ออก" แต่คือ "ทำเกินจำเป็น" เวลาคุณบอก AI ว่า "ทำระบบจัดการผู้ใช้หนึ่งตัว" มันอาจสร้างฟังก์ชันทั้งชุดออกมา ทั้งการยืนยันตัวตน สิทธิ์ บทบาท บันทึกตรวจสอบ ส่งออกข้อมูล ฯลฯ - แต่ตอนนี้คุณอาจแค่ต้องการหน้าล็อกอินง่าย ๆ หน้าเดียว การสร้างเกินงานคือสาเหตุหลักที่โค้ดจาก AI บวมขึ้นเรื่อย ๆ

"ความเรียบง่ายมาก่อน" กำหนดให้ทุกครั้งที่สั่งงานต้องยึดหลัก "เล็กที่สุดที่ใช้ได้ (minimum viable)": ใช้โค้ดน้อยที่สุดสร้างฟังก์ชันแกน ใช้แนวทางง่ายที่สุดแก้ปัญหา ใช้ฟังก์ชันน้อยที่สุดพิสูจน์ไอเดีย Karpathy มีเปรียบเทียบที่คมมาก: "ถ้าจะคำนวณราคาหลังหักส่วนลด คุณไม่ต้องพกเอนจินอีคอมเมิร์ซมา"

ในการใช้งานจริง "ความเรียบง่ายมาก่อน" แปลว่านิสัยปฏิบัติที่จับต้องได้หลายอย่าง:

- แต่ละครั้งให้ AI ทำฟังก์ชันเดียว ไม่ใช่บรรยายทั้งระบบในครั้งเดียว;
- เลือกไลบรารีมาตรฐานและแนวทางง่ายก่อน ไม่ใช่ดึง dependency ซับซ้อนมาเพิ่ม;
- ปัญหาที่แก้ด้วย 50 บรรทัดได้ อย่าให้ AI เขียน 500 บรรทัด;
- เมื่อผลงานของ AI ล้นออกนอกขอบเขตที่คาดไว้ กล้าบอกมันว่า "ตัดส่วนเกินทิ้ง"

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">สถานการณ์</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">แนวทางเกินจำเป็น (เลี่ยง)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">แนวทางเรียบง่าย (แนะนำ)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ต้องเก็บข้อมูล</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ตั้ง MySQL + ORM ทั้งระบบ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เริ่มด้วยไฟล์ JSON หรือ SQLite</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ต้องมีผู้ใช้ล็อกอิน</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OAuth2.0 + JWT + ระบบสิทธิ์บทบาท</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เริ่มด้วยการตรวจรหัสผ่านแบบง่าย</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ต้องมีเฟรมเวิร์กฟรอนต์เอนด์</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">React + Redux + Router</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ลอง HTML + JS ล้วนก่อน</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ต้องดีพลอยขึ้นออนไลน์</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Docker + CI/CD + K8s</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">รันให้ผ่านบนเครื่องตัวเองก่อนแล้วกัน</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
เปรียบเทียบแนวทางเกินจำเป็นกับแนวทางเรียบง่ายในสถานการณ์ที่พบบ่อย

#### 3. หลักข้อที่สาม: Surgical Changes (แก้แบบผ่าตัด)

เวลาคุณพัฒนาโปรเจกต์ที่มีอยู่ต่อ ทุกการแก้ไขควรแม่นยำแบบผ่าตัด แตะเฉพาะจุดที่ต้องแตะ ไม่แตะสิ่งที่ห้ามแตะ จุดนี้สำคัญยิ่งในการเขียนโปรแกรมด้วย AI เพราะ AI มีนิสัยชอบ "แก้เผื่อไปด้วยเลย": คุณให้มันแก้บั๊กหนึ่งตัว มันอาจรีแฟกเตอร์ครึ่งไฟล์ไปด้วย

ข้อเรียกร้องแกนของ "แก้แบบผ่าตัด" คือ: ทุกคำสั่งที่ให้ AI ต้องระบุขอบเขตและกรอบของการแก้ไขให้ชัด บอกมันว่า "แก้เฉพาะฟังก์ชัน calculate_discount" "อย่าไปแตะส่วนอื่น" "รักษาสไตล์โค้ดเดิมไว้" เมื่อ AI แก้ล้นออกไปเกินที่ขอ ให้เรียกร้องให้มันย้อนกลับส่วนเกินทันที

Karpathy อธิบายจุดนี้ด้วยตัวอย่าง diff (การเทียบความแตกต่าง) สมมุติว่าคุณให้ AI เพิ่มตรรกะ "ราคาสมาชิก" ให้ฟังก์ชันคำนวณส่วนลดของรถเข็น: ผลงานที่ดีคือแก้เฉพาะฟังก์ชันเดียว เพิ่มโค้ดไม่กี่บรรทัด ผลงานที่แย่คือรีแฟกเตอร์ทั้งไฟล์ใหม่หมด - โค้ดใหม่อาจดู "สวยขึ้น" ก็จริง แต่คุณบอกไม่ได้ว่ามันแทรกบั๊กใหม่มาหรือเปล่า ในการเขียนโปรแกรมด้วย AI "ดูดีขึ้น" ไม่มีวันเป็นข้ออ้างสำหรับการเบี่ยงจากคำสั่งได้เด็ดขาด

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
คำสั่งที่แย่ (ขอบเขตคลุมเครือ)

{class="font-mono text-xs leading-relaxed"}
ช่วยปรับปรุงตรรกะการคำนวณ ส่วนลดของโปรเจกต์นี้หน่อย
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
คำสั่งที่ดี (ระบุขอบเขตแม่นยำ)

{class="font-mono text-xs leading-relaxed"}
แก้เฉพาะฟังก์ชัน calculate_discount ใน cart.py: 1. เพิ่มตรรกะราคาสมาชิกบนฐานส่วนลดเดิม 2. ผู้ใช้สมาชิกได้ส่วนลดเพิ่มอีก 10% 3. ห้ามแก้ฟังก์ชันซิกเนเจอร์และฟังก์ชันอื่น 4. รักษาสไตล์การตั้งชื่อตัวแปรเดิม
:::
:::

#### 4. หลักข้อที่สี่: Goal-Driven Execution (ขับเคลื่อนด้วยเป้าหมาย)

หลักข้อนี้ตอบคำถามสำคัญ: คุณควรสั่ง AI แบบ "ทำอย่างไร" หรือแบบ "ทำอะไร"? คำตอบของ Karpathy คืออย่างหลัง แทนที่จะบอก AI ว่า "สร้างคลาสหนึ่ง เพิ่มเมธอด แล้วเขียนเทสต์" ให้บอกมันว่า "ฉันต้องการเครื่องมือที่อ่านไฟล์ CSV แล้วนับจำนวนค่าที่ไม่ซ้ำของแต่ละคอลัมน์ได้" ปล่อยให้ AI เลือกเส้นทางการทำงานเอง คุณรับผิดชอบการตรวจรับผลลัพธ์

ประโยชน์ของ "ขับเคลื่อนด้วยเป้าหมาย" เป็นสองชั้น สำหรับ AI มันได้พื้นที่อิสระกว้างขึ้น เลือกเส้นทางที่ดีที่สุดได้ แทนที่จะถูกขั้นตอนกลาง ๆ ของคุณมัดมือ สำหรับคุณ ความสนใจเลื่อนจาก "ทำอย่างไร" ไปอยู่ที่ "ผลที่ได้ถูกต้องไหม" - ซึ่งก็คือหน้าที่ของผู้อำนวยเพลงพอดี

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ระวัง: ขับเคลื่อนด้วยเป้าหมาย ≠ ปล่อยปละละเลย

{class="mt-1"}
มันต้องการให้คุณตรวจรับอย่างเข้มงวดหลัง AI ลงมือแล้ว: ผลลัพธ์ตอบความต้องการไหม? เคสขอบขั้วจัดการแล้วหรือยัง? มีการออกแบบเกินจำเป็นที่เห็นชัดไหม? ถ้าผลไม่ตรงคาด ให้ฟีดแบ็กแบบเจาะจง - ไม่ใช่แค่พูดว่า "เขียนใหม่" แต่พูดว่า "ปัญหาอยู่ตรงที่กรอกลิสต์ว่างเข้าไปจะเด้ง IndexError เพิ่มการตรวจค่าว่างหน่อย"
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">สไตล์คำสั่ง</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ตัวอย่าง</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ลักษณะผลลัพธ์</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">แบบสั่งการ (ทำอย่างไร)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"สร้างคลาส Python หนึ่งอันชื่อ DataParser เพิ่มเมธอด parse รับพารามิเตอร์ filename ใช้โมดูล csv อ่านข้อมูล..."</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI กลายเป็นนักพิมพ์ ขั้นตอนกลางของคุณอาจไม่ใช่เส้นทางที่ดีที่สุด</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">แบบเป้าหมาย (ทำอะไร)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"ฉันต้องการเครื่องมือหนึ่งตัว: อ่านไฟล์ CSV นับจำนวนค่าที่ไม่ซ้ำของแต่ละคอลัมน์ แล้วส่งออกเป็น JSON ขอโค้ดฉบับสมบูรณ์หน่อย"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI เลือกเส้นทางที่ดีที่สุดเอง คุณรับผิดชอบการตรวจรับ</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
เปรียบเทียบคำสั่งแบบสั่งการกับคำสั่งแบบเป้าหมาย

#### 5. หลักข้อที่ห้า: Iterate and Verify (ทำซ้ำและตรวจสอบ)

นี่คือข้อที่ห้าที่หนังสือเล่มนี้เติมบนรากฐานสี่หลักของ Karpathy ความเชื่อแกนของมันคือ: ผลงานรอบแรกของ AI แทบไม่เคยเป็นเวอร์ชันสุดท้าย การเขียนโปรแกรมด้วย AI ที่ได้ผลจริงคือวงจรทำซ้ำแบบ "สร้าง-ตรวจสอบ-แก้ไข" ไม่ใช่ "สั่งครั้งเดียว-ได้ของครั้งเดียว"

"ทำซ้ำและตรวจสอบ" ไม่ใช่การ "ไม่ถูกก็ลองใหม่" อย่างเฉื่อยชา แต่เป็นกระบวนการตรวจสอบที่มีโครงสร้าง ทุกครั้งที่ AI ส่งผลงานมา ให้ตรวจตามสามระดับ:

- ระดับหนึ่ง การตรวจฟังก์ชัน: มันรันได้ไหม? อินพุต-เอาต์พุตถูกต้องไหม?
- ระดับสอง การตรวจเคสขอบขั้ว: ถ้าใส่ค่าว่าง ค่ายาวเกิน ค่าผิดปกติจะเป็นยังไง?
- ระดับสาม การตรวจสถาปัตยกรรม: โครงสร้างโค้ดสมเหตุสมผลไหม? มีการ hard-code ไหม? ต่อยอดภายหลังง่ายไหม?

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-bullseye mr-1"></i> กำหนดเป้าหมาย</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> AI สร้างโค้ด</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> ทดสอบฟังก์ชัน</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> ผ่าน</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> ตรวจกรณีขอบเขต</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> ผ่าน</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-landmark mr-1"></i> รีวิวสถาปัตยกรรม</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> ผ่าน ไปขั้นถัดไป</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> ไม่ผ่าน</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> ให้ฟีดแบ็กที่เจาะจง</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> สร้างใหม่</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
ภาพที่ 2: วงจรทำซ้ำและตรวจสอบของการเขียนโปรแกรมด้วย AI
:::

กุญแจของวงจรนี้อยู่ที่ขั้น "ให้ฟีดแบ็กแบบเจาะจง" เมื่อการตรวจสอบไม่ผ่าน อย่าพูดว่า "ไม่ใช่ เขียนใหม่" แต่ให้พูดว่า "ฟังก์ชันเด้ง IndexError เวลารับลิสต์ว่าง เพิ่มการตรวจค่าว่างไว้บรรทัดที่ 15 หน่อย" ฟีดแบ็กที่ชัดเจนทำให้ AI แก้ได้แม่นยำ ส่วนฟีดแบ็กคลุมเครือจะทำให้มันต้องเดาความตั้งใจคุณใหม่หมด

#### 6. Harness Engineering: Agent = Model + Harness

กลางปี 2026 มโนทัศน์ชื่อ Harness Engineering เริ่มบูมในชุมชน AI programming สูตรแกนของมันง่ายมาก:

:::inline div .quote-line .text-center .text-base .font-bold
<strong>ความสามารถของ Agent = ความสามารถโมเดล × คุณภาพ Harness</strong>
:::

ความสามารถของโมเดลคือเพดานสติปัญญาของสมอง AI ส่วน Harness คือ "สภาพแวดล้อมการทำงาน" ที่สร้างรอบ ๆ โมเดล รวมถึงการจัดการบริบท การผนวกเครื่องมือ การจัดลำดับกระบวนการ ระบบความจำ ฯลฯ

มโนทัศน์นี้อธิบายคำถามชวนงงที่พบบ่อย: ทำไมใช้ GPT-4 หรือ Claude เหมือนกัน คนหนึ่งทำโปรเจกต์ออกมาว้าวสะดุดตา อีกคนได้แต่โค้ดโรยเรื่องเฉย ๆ? ความต่างไม่อยู่ที่โมเดล แต่อยู่ที่ Harness Harness ที่ดีประกอบด้วย: ไฟล์สเปกโปรเจกต์ที่ชัดเจน การผนวกเครื่องมืออย่างสมเหตุสมผล บริบทการสนทนาที่เป็นระเบียบ และกระบวนการตรวจสอบที่ครบถ้วน โมเดลกำหนดเพดานสติปัญญา ส่วน Harness กำหนดว่าคุณจะใช้เพดานนั้นได้มากแค่ไหน

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
การเปรียบเทียบกับเด็กฝึกงานอัจฉริยะ

{class="mt-1"}
ลองนึกว่าโมเดลคือเด็กฝึกงานอัจฉริยะคนหนึ่ง - IQ สูงมาก แต่ถ้าไม่ให้เอกสารบริบทโปรเจกต์ ไม่บอกว่าให้ใช้เครื่องมือไหน ไม่ตั้งเดดไลน์และเกณฑ์ตรวจรับให้ เขาก็ทำของดีออกมาไม่ได้เหมือนกัน Harness Engineering ก็คือวิศวกรรมเรื่อง "จะจัดสภาพแวดล้อมการทำงานให้เด็กฝึกงานอัจฉริยะอย่างไรให้ดี"
:::

บทที่เหลือของหนังสือเล่มนี้ แท้จริงแล้วล้วนสอนวิธีสร้าง Harness ที่ดี: บทที่ 39 สอนจัดการบริบท (ระบบความจำโปรเจกต์) บทที่ 40 สอนนิยามความต้องการ (PRD) บทที่ 43 สอนเทคนิคการสนทนา (การแบ่งชั้น Prompt) บทที่ 45 สอนการการันตีคุณภาพ (กระบวนการตรวจสอบ) เอาทั้งหมดมาประกอบกัน ก็คือ Harness ของคุณ

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
มาลงมือ: ใช้ "สามเหลี่ยมแห่งการคิด" แกะไอเดียถัดไปของคุณ

{class="mt-1"}
เลือกของเล็ก ๆ สักหนึ่งชิ้นที่อยากทำมานานแต่ยังไม่ลงมือ (เช่น เว็บนับถอยหลังหนึ่งเว็บ สคริปต์เตือนดื่มน้ำหนึ่งอัน) ใช้เวลา 3 นาทีตอบ: (1) มันแก้ปัญหาอะไร? (2) ถ้าทำออกมาจะหน้าตาเป็นอย่างไร? (3) มีข้อจำกัดอะไร (เวลา เทคนิค สภาพแวดล้อม)? แล้วเขียนคำตอบเป็นย่อหน้าหนึ่งย่อหน้า ยินดีด้วย คุณเพิ่งทำ "Think Before Coding" ครั้งแรกในชีวิตสำเร็จ - ย่อหน้านั้นแหละคือคำสั่งคุณภาพสูงที่ผ่านเกณฑ์ฉบับแรกของคุณ
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
สรุปบทนี้

- หลักทั้งห้ามาจากไฟล์ CLAUDE.md 70 บรรทัดของ Karpathy (Star เกิน 70K) หนังสือเล่มนี้เติมข้อที่ห้า "ทำซ้ำและตรวจสอบ"
- Think Before Coding: ตอบสามคำถามก่อนเปิดปาก - ทำอะไร? ผลลัพธ์หน้าตาเป็นอย่างไร? มีข้อจำกัดอะไร?
- Simplicity First: กับดักใหญ่สุดของ AI คือ "ทำเกินจำเป็น" - คำนวณส่วนลดไม่ต้องใช้เอนจินอีคอมเมิร์ซ
- Surgical Changes: แก้ไขแม่นยำแบบผ่าตัด ปฏิเสธนิสัย "แก้เผื่อไปด้วยเลย" ของ AI
- Goal-Driven Execution: บอก "ทำอะไร" ไม่ใช่ "ทำอย่างไร" ให้ AI เลือกเส้นทางเอง
- Iterate and Verify: ตรวจสามระดับ (ฟังก์ชัน/ขอบขั้ว/สถาปัตยกรรม) + ฟีดแบ็กเจาะจง วนทำซ้ำไปเรื่อย ๆ
- Harness Engineering: ความสามารถ = โมเดล × Harness ใช้ AI แบบ "เด็กฝึกงานอัจฉริยะ" แล้วจัดการสภาพแวดล้อมให้ดี
:::
