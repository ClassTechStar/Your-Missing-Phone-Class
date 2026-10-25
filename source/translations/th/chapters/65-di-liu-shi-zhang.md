---
id: di-liu-shi-zhang
num: 60
part: ios-kai-fa-pian
nav: บทที่ 60: ตั้งค่าสภาพแวดล้อมการพัฒนา — Xcode กับโปรเจกต์แรก
toc: default
kind: chapter
---

### บทที่ 60: ตั้งสภาพแวดล้อมการพัฒนา — Xcode กับโปรเจกต์แรก

{class="chapter-intro mb-4"}
จะทำงานให้เป็น ต้องลับเครื่องมือให้คมก่อน บทนี้เราจะสร้าง “ห้องครัว” ให้พร้อม: ติดตั้ง Xcode ให้ซิมูเลเตอร์รันผ่าน สร้างโปรเจกต์ iOS แรกในชีวิต แล้วแกะโครงสร้างโปรเจกต์ให้เห็นชัด ๆ พอเครื่องพร้อม คุณจะได้เห็นเป็นครั้งแรกว่าโค้ดที่เขียนกลายเป็นปุ่มที่กดได้จริง ๆ — วินาทีนี้ หลายคนจำได้ตลอดชีวิต

#### 1. เตรียม Mac สักเครื่อง

เริ่มจากข้อกีดขวางก่อน: การพัฒนา iOS ต้องทำบน macOS เท่านั้น ถ้ายังไม่มี Mac มีทางเลือกสามทาง: ซื้อสักเครื่อง (แม้แต่ Mac mini หรือ MacBook Air มือสองก็ใช้ได้), เช่า Mac บนคลาวด์ระยะสั้น, หรือไปอ่านภาคที่ 8 “ลงมือพัฒนา Android” (ใช้ Windows ก็ทำได้) ก่อน

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">รายการตั้งค่า</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ค่าขั้นต่ำ</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ระดับสบาย (แนะนำ)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ชิป</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Silicon (M1 ขึ้นไป)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">M2 หรือใหม่กว่า</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">หน่วยความจำ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8GB</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">16GB</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ดิสก์</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">สำรองพื้นที่ 40GB+ (ตัว Xcode กินพื้นที่เยอะ)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เริ่มต้นที่ 256GB</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ระบบปฏิบัติการ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">macOS เวอร์ชันล่าสุด</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เปิดอัปเดตอัตโนมัติไว้</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
สเปกอ้างอิงเครื่อง Mac สำหรับพัฒนา (สิงหาคม 2026)

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
เคล็ดลับ: ไม่มี Mac ก็เริ่มเรียนภาษาได้ก่อน

{class="mt-1"}
Swift Playgrounds ที่ฟรีบน iPad เรียนพื้นฐานภาษา Swift ได้ (ไม่ต้องมี Mac); แม้แต่บน iPhone ก็ติดตั้งได้ ลองเล่นความรู้ภาษาจากบทที่ 61 ใน Playgrounds ให้คล่องก่อน พอได้ Mac มาครองก็ออกตัวได้ทันที “ลับเคียวไม่เสียเวลาตัดฟืน” พูดถึงเรื่องนี้แหละ
:::

#### 2. ติดตั้ง Xcode

Xcode คือ IDE ทางการของ Apple ใช้ฟรี ติดตั้งเสร็จในสามขั้นตอน:

1. เปิด App Store บน Mac ค้นหา "Xcode" แล้วกดติดตั้ง — ระวังว่ามันมีหลาย GB หาช่วงเน็ตชิล ๆ ทำ;
2. พอติดตั้งเสร็จแล้วเปิดครั้งแรก ยอมรับข้อตกลง ติดตั้งคอมโพเนนต์ให้ครบ (ทำเองอัตโนมัติ);
3. เมนู Xcode → Settings → Locations ยืนยันว่า Command Line Tools ถูกเลือกไว้แล้ว — เครื่องมือบรรทัดคำสั่งเป็นเงื่อนไขของสคริปต์และเครื่องมือภายนอกจำนวนมาก.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ข้อควรรู้: เกมจับคู่เวอร์ชัน Xcode กับระบบ

{class="mt-1"}
Xcode รุ่นใหม่มักต้องการ macOS ล่าสุด ส่วน Mac เครื่องเก่าจะติดค้างที่เวอร์ชันเก่า ตอนขึ้น App Store Apple จะให้ใช้ Xcode ที่ใหม่พอสมควรบิลด์ (มักมีช่วงผ่อนปรนให้) ดังนั้นอย่าผลัดการอัปเดตระบบนานเกินไป — นักพัฒนา iOS คือกลุ่มที่ “วิ่งไล่เวอร์ชันใหม่” ขยันที่สุดกลุ่มหนึ่ง
:::

#### 3. สร้างโปรเจกต์แรกของคุณ

เปิด Xcode → Create New Project → เลือก iOS → เทมเพลต App แล้วกรอก:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">รายการตั้งค่า</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">กรอกอะไร</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">คำอธิบาย</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Product Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstApp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ชื่อแอป</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple ID ของคุณ (ฟรี)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ใช้สำหรับเซ็น บัญชีส่วนตัวก็พอ</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Organization Identifier</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">รวมกับ Product Name เป็นตัวระบุแพ็กเกจ</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interface</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เฟรมเวิร์กเส้นหลักของหนังสือเล่มนี้</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Language</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ไม่ต้องอธิบาย</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
5 อย่างที่ต้องกรอกตอนสร้างโปรเจกต์

กด Create แล้ว Xcode จะสร้างโปรเจกต์ที่รันได้ทันทีขึ้นมา มุมซ้ายบนเลือกซิมูเลเตอร์สักเครื่อง (เช่น iPhone 17) กด ▶ รัน — ไม่กี่วินาทีต่อมา บนจอซิมูเลเตอร์จะมีหน้าต่างเขียนว่า "Hello, world!" แอป iOS ตัวแรกของคุณถือกำเนิดแล้ว

#### 4. แกะโครงสร้างโปรเจกต์: ไฟล์แต่ละตัวทำอะไร

ด้านซ้ายคือตัวนำทางโปรเจกต์ มือใหม่แค่ต้องรู้จักไม่กี่ตัวนี้:

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="290" viewBox="0 0 600 290" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="290" fill="#fafafa" rx="8"/>
      <text x="20" y="28" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ โฟลเดอร์รากของโปรเจกต์</text>
      <rect x="30" y="42" width="540" height="225" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <rect x="45" y="56" width="250" height="196" fill="#eef2ff" rx="5"/>
      <text x="56" y="78" font-size="11" fill="#1e1b4b" font-weight="bold">MyFirstApp/ (โฟลเดอร์โค้ด)</text>
      <text x="66" y="100" font-size="10" fill="#374151">├ MyFirstAppApp.swift  ← จุดเริ่มโปรแกรม</text>
      <text x="66" y="120" font-size="10" fill="#374151">├ ContentView.swift  ← หน้าจอหลัก</text>
      <text x="66" y="140" font-size="10" fill="#374151">└ Assets.xcassets  ← ไอคอน รูปภาพ สี</text>
      <text x="56" y="166" font-size="10" fill="#6b7280">(ไฟล์ใหม่ทั้งหมดใส่ในโฟลเดอร์นี้)</text>
      <text x="56" y="196" font-size="10" fill="#1e1b4b" font-weight="bold">แท็บ Info / Info.plist</text>
      <text x="66" y="216" font-size="10" fill="#6b7280">การประกาศแอป: ชื่อ สิทธิ์ การตั้งค่า</text>
      <rect x="310" y="56" width="245" height="196" fill="#f0fdf4" rx="5"/>
      <text x="321" y="78" font-size="11" fill="#065f46" font-weight="bold">ตำแหน่งสำคัญอื่น ๆ</text>
      <text x="331" y="100" font-size="10" fill="#374151">📁 Preview Content/  ← สื่อพรีวิว</text>
      <text x="331" y="122" font-size="10" fill="#374151"><i class="fas fa-bullseye mr-1"></i> ตั้งค่า Target (ไอคอนโปรเจกต์สีน้ำเงิน)</text>
      <text x="331" y="142" font-size="10" fill="#6b7280">— เลขเวอร์ชัน ระบบขั้นต่ำ และลายเซ็นอยู่ที่นี่</text>
      <text x="331" y="168" font-size="10" fill="#374151"><i class="fas fa-flask mr-1"></i> MyFirstAppTests/  ← unit test</text>
      <text x="331" y="188" font-size="10" fill="#374151">📱 MyFirstAppUITests/ ← เทสต์ UI</text>
      <text x="331" y="216" font-size="10" fill="#9ca3af">(เทมเพลตเทสต์สร้างไว้แล้ว ใช้ในบทที่ 67)</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
ภาพที่ 2: โครงสร้างโปรเจกต์ Xcode ที่มือใหม่ต้องรู้
:::

- MyFirstAppApp.swift: จุดเริ่มของโปรแกรม ใน SwiftUI มันมีแค่ไม่กี่บรรทัด — “สตาร์ท แล้วแสดงหน้าหลัก”;
- ContentView.swift: วิวหน้าจอหลัก ทุกอย่างที่คุณเห็นตอนนี้อยู่ในไฟล์นี้;
- Assets.xcassets: คลังทรัพยากร — ไอคอน รูปภาพ สี เก็บไว้ที่นี่;
- การตั้งค่า Target: กดไอคอนโปรเจกต์สีน้ำเงินด้านซ้ายเข้าไป เลขเวอร์ชัน iOS ขั้นต่ำ และการเซ็น อยู่ในนี้หมด ชื่อที่แสดงของแอปกับไอคอนก็ตั้งที่นี่เช่นกัน.

#### 5. เทคนิคทำงานไวใน Xcode: “โกงเกม” 5 ปุ่มลัดของมือใหม่

ใช้พวกนี้จนคล่อง คุณจะดู “เป็นมืออาชีพ” ขึ้นทันที:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">การกระทำ</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ปุ่มลัด</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">หน้าที่</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">รัน</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">คอมไพล์แล้วรันขึ้นมา</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เปิด/สลับพรีวิวแคนวาส</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">สวิตช์เปิดพรีวิวแบบเห็นตามที่เขียน</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">จัดย่อหน้าให้เรียบร้อย</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">จัดย่อหน้าของโค้ดที่เลือกให้อัตโนมัติ</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เปิดไฟล์อย่างรวดเร็ว</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">พิมพ์ชื่อไฟล์แล้วเปิดทันที (ใช้บ่อยที่สุด!)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">คอมเมนต์/เลิกคอมเมนต์</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เปิด-ปิดโค้ดส่วนไหนก็ได้ระหว่างดีบัก</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
ปุ่มลัดใช้บ่อยของ Xcode (ชุดห้าสำหรับมือใหม่)

โบนัสซ่อนอยู่อีกสองอย่าง: เปิดซิมูเลเตอร์หลายตัวพร้อมกัน (รัน iPhone กับ iPad เทียบเลย์เอาต์ได้ในเวลาเดียว) และคลังโค้ดสั้น (ลากโค้ดที่ใช้บ่อยไปวางในแผง Snippets ด้านขวา คราวหน้าแทรกได้ด้วยคลิกเดียว) — เครื่องมือเพิ่มประสิทธิภาพใช้ก่อนเลย มือมันจะคล่องเอง

#### 6. ดีบักบนเครื่องจริง: ติดตั้งแอปลง iPhone ของคุณ

ซิมูเลเตอร์ดีอยู่หรอก แต่ปลายทางคือเครื่องจริง ใช้ Apple ID ฟรีก็ดีบักบนเครื่องจริงได้:

1. ต่อสายข้อมูลกับ iPhone (หรือดีบักไร้สายผ่าน Wi-Fi เดียวกัน);
2. ในรายการอุปกรณ์ด้านบนของ Xcode เลือกเครื่องของคุณ ครั้งแรกจะมีข้อความให้ล็อกอิน Apple ID และตั้งค่าการเซ็นให้อัตโนมัติ;
3. บน iPhone ไปที่ [การตั้งค่า] → [ทั่วไป] → [VPN และการจัดการอุปกรณ์] → เชื่อถือใบรับรองนักพัฒนาของคุณ;
4. กด ▶ แอปจะถูกติดตั้งลงเครื่องจริง.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ข้อควรรู้: “ข้อจำกัด 7 วัน” ของบัญชีฟรี

{class="mt-1"}
แอปที่เซ็นด้วย Apple ID ฟรีจะหมดอายุใน 7 วัน (รันใหม่อีกครั้งก็ต่ออายุได้) นี่คือกลไกกันการใช้ในทางที่ผิดของ Apple ช่วงเรียนรู้ใช้ได้สบาย; บัญชีนักพัฒนาแบบเสียเงิน (99 ดอลลาร์/ปี) ไม่มีข้อจำกัดนี้ รายละเอียดอยู่ในบทที่ 67
:::

#### 7. ลองมือจริง + หนังสือฉุกเฉินเมื่อเจอ error ที่พบบ่อย

เปิด ContentView.swift เปลี่ยนข้อความใน Text("Hello, world!") เป็นชื่อของคุณ กด ⌘R รันใหม่ — ไม่กี่วินาทีต่อมาชื่อคุณก็โผล่บนซิมูเลเตอร์ ยินดีด้วย คุณครบวงจร “แก้โค้ด → คอมไพล์ → ติดตั้ง → รัน” ครั้งแรกแล้ว

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">อาการ error</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">สาเหตุที่พบบ่อย</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">วิธีแก้</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">error เรื่อง Signing</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ไม่ได้เลือก Team หรือใบรับรองหมดอายุ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เข้าไปที่ Target → Signing แล้วเลือกบัญชีของคุณ; บัญชีฟรีรันใหม่อีกครั้ง</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ซิมูเลเตอร์จอดำ/เปิดไม่ได้</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ไฟล์อิมเมจเสีย</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เมนู Device → Erase All Content; หรือลบซิมูเลเตอร์ทิ้งแล้วเพิ่มใหม่</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode โหลดช้า/ติดตั้งไม่ได้</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เน็ต App Store สะดุด</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เปลี่ยนช่วงเวลาโหลด; หรือไปดาวน์โหลดไฟล์ .xip แบบออฟไลน์จากเว็บนักพัฒนาของ Apple</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
ตารางฉุกเฉิน error ตอนตั้งเครื่องสำหรับมือใหม่

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ลงมือทำ: ทำลิสต์ “พิธีกรรมนักพัฒนา” ของคุณให้ครบ

{class="mt-1"}
① ติดตั้ง Xcode ให้ซิมูเลเตอร์รันผ่าน; ② รันแอปของตัวเองบนเครื่องจริงสักครั้งแล้วเก็บภาพไว้เป็นที่ระลึก; ③ เปลี่ยนข้อความ Hello เป็นชื่อของคุณ; ④ เข้าไปตั้งค่า Target เปลี่ยนชื่อที่แสดงของแอปเป็น “แอปแรกของฉัน” ทำครบสี่ขั้นนี้ คุณก็เป็นคนมีผลงานแล้ว
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
สรุปบทนี้

- ข้อกีดขวางแบบแข็ง: Mac + Xcode; ยังไม่มี Mac ก็เริ่มเรียนภาษาด้วย Swift Playgrounds บน iPad ก่อน
- Xcode ติดตั้งจาก App Store; รุ่นใหม่ต้องการระบบใหม่ อย่าผลัดการอัปเดต
- 5 องค์ประกอบตอนสร้างโปรเจกต์ใหม่: ชื่อ, Team, ตัวระบุองค์กร, SwiftUI, Swift
- คาถาจำโปรเจกต์: โค้ดทั้งหมดอยู่ในโฟลเดอร์ MyFirstApp/; การตั้งค่า Target ดูแลเวอร์ชันกับการเซ็น
- ดีบักบนเครื่องจริงด้วย Apple ID ฟรีมีข้อจำกัดเซ็น 7 วัน; บัญชีเสียเงินไม่มีข้อจำกัดนี้
- ชีวิตประจำวันของนักพัฒนา = แก้โค้ด → ⌘R → ดูผล วนไปเรื่อย ๆ
:::
