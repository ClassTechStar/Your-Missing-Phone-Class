---
id: di-san-shi-jiu-zhang
num: 39
part: ai-biancheng-pian
nav: บทที่ 39: Context Engineering — ทำให้ AI เข้าใจความตั้งใจของคุณ
toc: default
kind: chapter
---

### บทที่ 39: วิศวกรรมบริบท - ทำให้ AI เข้าใจความตั้งใจของคุณ

{class="chapter-intro mb-4"}
เคยมีประสบการณ์แบบนี้ไหม: เปลี่ยนหน้าต่างแชทใหม่ครั้งเดียว AI เหมือนความจำเสื่อม ลืมข้อมูลพื้นฐานของโปรเจกต์คุณหมดเกล้า นี่ไม่ใช่ AI ตั้งใจแกล้งคุณ แต่มัน "ขี้ลืม" โดยกำเนิด บทนี้จะสอนคุณติดตั้ง "ระบบความจำระยะยาว" ให้ AI และแถมรู้จักกระบวนทัศน์พัฒนาที่ฮอตที่สุดปี 2026 อีกหนึ่งตัว - การพัฒนาที่นำด้วยสเปก (Spec-Driven Development)

#### 1. ไฟล์ความจำโปรเจกต์: "ความจำระยะยาว" ของ AI

โมเดล AI มีข้อจำกัดพื้นฐานหนึ่งอย่าง: ความจำของมันเป็นแบบ "ระยะสั้น" ทุกครั้งที่แชทเริ่มใหม่ ความรู้ของ AI เกี่ยวกับโปรเจกต์คุณเริ่มจากศูนย์ คุณต้องคอยบอกมันในแชทว่า "เราใช้ React" "แบ็กเอนด์เป็น Node.js" "ฐานข้อมูลคือ PostgreSQL" "สไตล์โค้ดใช้เครื่องหมายคำพูดคู่" ซึ่งไม่ใช่แค่เปลืองเวลา แต่ยังตกหล่นง่าย - เหมือนต้องอบรมพนักงานใหม่ทุกวันเลย

ทางแก้คือ "ไฟล์ความจำโปรเจกต์" - ไฟล์ข้อความล้วนหนึ่งไฟล์วางไว้ที่โฟลเดอร์รากของโปรเจกต์ เครื่องมือ AI จะอ่านมันอัตโนมัติทุกครั้งที่เริ่มแชท แต่ละเครื่องมือมีชื่อเรียกต่างกัน:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">เครื่องมือ</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ชื่อไฟล์</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cursorrules</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">CLAUDE.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitHub Copilot</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">copilot-instructions.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ทางเลือกสากล</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">AGENTS.md</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
ชื่อเรียกไฟล์ความจำโปรเจกต์ของแต่ละเครื่องมือ

ถึงชื่อจะไม่เหมือนกัน แต่หลักการเดียวกันคือ: เขียนข้อมูลที่คุณอยากให้ AI "จำตลอดไป" ไว้ในไฟล์นี้ ไฟล์ความจำโปรเจกต์ที่ดีควรมี: ภาพรวมโปรเจกต์ (นี่คือโปรเจกต์อะไร) เทคโนโลยีที่ใช้ (สแตกไหน) มาตรฐานโค้ด (การตั้งชื่อ การย่อหน้า สไตล์คอมเมนต์) โครงสร้างไดเรกทอรี (จัดโค้ดอย่างไร) และข้อตกลงการพัฒนา (กลยุทธ์แบรนช์ ข้อกำหนดการคอมมิต ความต้องการเทสต์) CLAUDE.md ของ Karpathy มีแค่ 70 บรรทัด แต่ครอบคลุมข้อมูลสำคัญครบทุกอย่าง - กระชับแต่ไม่ขาดชิ้น

::: div .code-block
:::inline div .code-head
<span>CLAUDE.md</span><span class="dots">···</span>
:::

```
# โปรเจกต์: แอปบันทึกรายรับรายจ่ายส่วนตัว
## ภาพรวม
แอปบันทึกรายรับรายจ่ายแบบเต็มสแตก ช่วยผู้ใช้จดรายรับรายจ่ายประจำวัน
## เทคโนโลยี
- Frontend: React + TypeScript + Tailwind CSS
- Backend: Node.js + Express + TypeScript
- ฐานข้อมูล: SQLite (พัฒนา) / PostgreSQL (ใช้งานจริง)
- เทสต์: Vitest
## ข้อตกลงการเขียนโค้ด
- ใช้เครื่องหมายคำพูดคู่
- ย่อหน้า 2 ช่องว่าง
- ชื่อฟังก์ชันใช้ camelCase
- ชื่อไทป์ใช้ PascalCase
- ทุกฟังก์ชันต้องมีคอมเมนต์ JSDoc
## โครงสร้างโฟลเดอร์
/src
  /frontend  - โค้ดฝั่งหน้า
  /backend   - โค้ดฝั่งหลัง
  /shared    - ไทป์ที่ใช้ร่วมกัน
  /tests     - ไฟล์เทสต์
## ข้อตกลงการทำงาน
- เขียนข้อความคอมมิตเป็นภาษาจีน
- ฟีเจอร์ใหม่ต้องเขียนเทสต์ก่อน
- API ตอบด้วยรูปแบบ { success, data, error } เสมอ
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ระวัง: อย่าเขียนมันเป็น "เอกสารความต้องการฉบับที่สอง"

{class="mt-1"}
ระวังความยาวของไฟล์นี้ - อย่าเขียนเป็นเอกสารความต้องการยาวเป็นสิบ ๆ หน้า เป้าหมายของไฟล์ความจำโปรเจกต์คือ "ทำให้ AI สร้างความเข้าใจพื้นหลังได้เร็ว" ไม่ใช่ "บรรยายรายละเอียดทุกฟังก์ชัน" รักษาไว้ให้กระชับ เป็นโครงสร้าง และเขียนเฉพาะ "สิ่งที่ AI จำเป็นต้องรู้" เท่านั้น
:::

#### 2. การพัฒนาที่นำด้วยสเปก (SDD)

Spec-Driven Development (SDD หรือการพัฒนาที่นำด้วยสเปก) เป็นกระบวนทัศน์การพัฒนาที่ค่อย ๆ ก่อร่างขึ้นในปี 2026 แนวคิดแกนพูดเป็นประโยคเดียว: เขียนสเปกก่อน แล้วค่อยเขียนโค้ด ต่างจาก TDD (การพัฒนาที่นำด้วยการทดสอบ) แบบดั้งเดิม ตรงที่ "สเปก" ของ SDD ไม่ใช่แค่เทสต์เคส แต่รวมคำบรรยายความต้องการ นิยามอินเทอร์เฟซ โมเดลข้อมูล ฯลฯ AI สร้างโค้ดตามสเปกเหล่านี้ ส่วนหน้าที่ของมนุษย์คือเขียนและดูแลสเปก

กระบวนการทำงานของ SDD เดินห้าขั้น:

1. บรรยายสเปกความต้องการด้วยภาษาธรรมชาติ (เขียนในไฟล์ .md หนึ่งไฟล์);
2. นิยามอินเทอร์เฟซและโครงสร้างข้อมูล (เขียนไว้ในไฟล์สเปก);
3. ให้ AI สร้างโค้ดจริงตามสเปก;
4. รันเทสต์ยืนยันว่าผลงานตรงสเปกหรือไม่;
5. ถ้าไม่ตรง ก็แก้สเปกหรือให้ AI แก้โค้ด

ในกระบวนการนี้ ไฟล์สเปกคือ "แหล่งความจริงเดียว (single source of truth)" - โค้ดสร้างใหม่ได้เสมอ แต่สเปกต้องถูกต้องก่อน

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> เขียนไฟล์สเปก</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> สเปกครบถ้วนดีแล้วหรือยัง?</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> ครบถ้วน</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> AI สร้างโค้ดจากสเปก</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> รันเทสต์ตรวจผลงาน</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> สเปกไม่ครบ / เทสต์ไม่ผ่าน</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-tools mr-1"></i> โค้ดผิด → แก้โค้ด / สเปกผิด → แก้สเปก</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> กลับไปขั้นตรวจสอบ</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> ผ่านทั้งหมด → ส่งมอบ</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
ภาพที่ 3: กระบวนการทำงานของการพัฒนาที่นำด้วยสเปก (SDD)
:::

ข้อเด่นของ SDD อยู่ตรงที่: ไฟล์สเปกนิ่งกว่าโค้ด เมื่อโมเดลรากฐานหรือเครื่องมือเปลี่ยนไป ไฟล์สเปกของคุณยังใช้ได้เหมือนเดิม แค่ให้เครื่องมือ AI ตัวใหม่สร้างโค้ดซ้ำอีกครั้งก็จบ นี่ก็คือเหตุผลที่หนังสือเล่มนี้เน้นว่า "วิธีการสำคัญกว่าเครื่องมือ" - ไฟล์สเปกก็คือภาชนะรูปธรรมของวิธีการของคุณ

#### 3. การจัดการหน้าต่างบริบท (context window)

แม้จะมีไฟล์ความจำโปรเจกต์แล้ว คุณก็ยังจะเจอปัญหา "บริบทไม่พอใช้" ในการแชท หน้าต่างบริบท (ปริมาณข้อมูลที่ประมวลผลพร้อมกันได้) ของโมเดล AI มีจำกัด เมื่อแชทยาวเกินหรืออ้างไฟล์มากเกิน AI จะ "ลืม" ข้อมูลช่วงต้น ทำให้คุณภาพผลงานตก - เหมือนคุณคุยกับเพื่อนคนหนึ่งนานหกชั่วโมง เขาลืมสิ่งแรกที่คุณพูดไปนานแล้ว

กลยุทธ์แกนของการจัดการหน้าต่างบริบทคือ "การอ้างอิงแบบแบ่งชั้น":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ระดับชั้นของบริบท</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">เนื้อหา</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">วิธีจัดการ</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ชั้นหนึ่ง: ความจำโปรเจกต์</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เทคโนโลยีที่ใช้ สเปก โครงสร้างไดเรกทอรี</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เขียนไว้ในไฟล์อย่าง CLAUDE.md โหลดอัตโนมัติ ไม่ต้องพูดซ้ำ</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ชั้นสอง: การอ้างอิงไฟล์</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ไฟล์โค้ดที่งานปัจจุบันเกี่ยวข้อง</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">อ้างอิงแม่นยำด้วยสัญลักษณ์ @ ไม่ต้องวางเนื้อไฟล์เต็มลงในแชท</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ชั้นสาม: บริบทการสนทนา</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ประวัติการสนทนาของงานปัจจุบัน</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">จบงานหนึ่งงานแล้วเปิดแชทใหม่ กันบริบทบวม</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ชั้นสี่: คำสั่งฉับพลัน</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ข้อเรียกร้องเฉพาะของขั้นตอนนี้</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ชัด กระชับ ตรงจุด เลี่ยงคำบรรยายยืดยาว</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
กลยุทธ์การจัดการหน้าต่างบริบทแบบแบ่งชั้น

#### 4. จุดสำคัญในทางปฏิบัติของ Context Engineering

Context Engineering ไม่ใช่การตั้งค่าครั้งเดียวจบ แต่เป็นกระบวนการที่ต้องปรับปรุงให้ดีขึ้นเรื่อย ๆ ต่อไปนี้คือประเด็นสำคัญที่ผ่านการพิสูจน์มาแล้วซ้ำ ๆ ในสนามจริง:

1. ไฟล์ความจำต้องอัปเดตให้ทันกับการพัฒนาของโปรเจกต์ เมื่อเปิดใช้เทคโนโลยีใหม่หรือเปลี่ยนสถาปัตยกรรมเมื่อไหร่ ให้อัปเดตไฟล์ความจำทันทีเป็นอย่างแรก ไม่ใช่เอาไว้อธิบายสด ๆ กลางบทสนทนา
2. ใช้การอ้างอิงด้วย @ แทนการวางข้อความทั้งไฟล์ เครื่องมือเขียนโค้ดด้วย AI ส่วนใหญ่รองรับไวยากรณ์ @file หรือ @folder ซึ่งจะฉีดเนื้อหาไฟล์เข้าไปในบริบทของ AI ให้เบื้องหลัง ได้ผลมีประสิทธิภาพกว่าการคัดลอกวางด้วยมือ และไม่ทำให้บทสนทนารก
3. บทสนทนาควร "สั้นแต่คม" หนึ่งบทสนทนาจัดการแค่หนึ่งงานหรือหนึ่งฟีเจอร์เท่านั้น พอเสร็จก็เปิดบทสนทนาใหม่ไปทำงานต่อไป บทสนทนาที่ยืดยาวไม่เพียงเปลือง context window แต่ยังทำให้ AI "เสียสมาธิ" ด้วย
4. ให้ AI "เห็น" ผลลัพธ์ ไม่ใช่ "บรรยาย" ผลลัพธ์ เจอ bug เมื่อไหร่ ให้ใช้ @ อ้างอิง log ข้อผิดพลาดส่งให้ AI ตรง ๆ ไม่ใช่อธิบายด้วยคำพูดของตัวเองแบบ "เหมือนมี error อะไรสักอย่าง" ข้อมูลดิบมีประโยชน์กับ AI มากกว่าคำถ่ายทอดของคุณ
5. หมั่นทำความสะอาดและจัดเก็บเป็นระยะ บทสนทนาที่จบแล้วและไฟล์ชั่วคราวจะกินพื้นที่ทำงาน ค่อย ๆ ล้างสิ่งที่ไม่เกี่ยวข้องออก รักษาไดเรกทอรีโปรเจกต์ให้เป็นระเบียบ ก็ช่วยให้ AI เข้าใจโครงสร้างโปรเจกต์ได้มีประสิทธิภาพขึ้นด้วย

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ลงมือทำ: เขียนไฟล์ความจำ 70 บรรทัดให้โปรเจกต์ของคุณ

{class="mt-1"}
เลือกโปรเจกต์ที่คุณกำลังทำ (หรือวางแผนจะทำ) สักหนึ่ง แล้วเขียน CLAUDE.md: ภาพรวมโปรเจกต์ (2-3 ประโยค) เทคโนโลยีที่ใช้ (ลิสต์ออกมา) มาตรฐานโค้ด (3-5 ข้อ) โครงสร้างไดเรกทอรี (วาดเป็น tree) และข้อตกลงการพัฒนา (2-3 ข้อ) คุมความยาวไม่เกิน 70 บรรทัด — พอเขียนเสร็จคุณจะพบว่าความเข้าใจโปรเจกต์ของคุณเองชัดขึ้นเยอะเลย
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
สรุปบทนี้

- ความจำของ AI เป็นแบบ "ระยะสั้น": ทุกครั้งที่เปิดบทสนทนาใหม่ ความรู้เรื่องโปรเจกต์ของมันจะเริ่มจากศูนย์
- ไฟล์ความจำโปรเจกต์ (อย่างเช่น CLAUDE.md) คือ "ความจำระยะยาว" ของ AI โหลดขึ้นมาให้อัตโนมัติทุกครั้งที่เริ่มบทสนทนา
- ไฟล์ความจำที่ดี = ภาพรวม + เทคโนโลยีที่ใช้ + มาตรฐาน + โครงสร้างไดเรกทอรี + ข้อตกลง แค่ 70 บรรทัดก็พอ
- SDD การพัฒนาที่นำด้วยสเปก: เขียนสเปกก่อนเขียนโค้ด โดยสเปกคือ "แหล่งความจริงเดียว" ที่เสถียรกว่าโค้ด
- บริบทจัดการเป็นสี่ชั้น: ความจำโปรเจกต์ → การอ้างอิงไฟล์ด้วย @ → ประวัติบทสนทนา → คำสั่งทันที
- ห้าจุดสำคัญในทางปฏิบัติ: อัปเดตให้ทันกัน, อ้างอิงด้วย @, บทสนทนาสั้น, ส่งข้อมูลดิบ, หมั่นทำความสะอาด
:::
