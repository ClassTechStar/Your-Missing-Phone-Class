---
id: di-si-shi-jiu-zhang
num: 49
part: an-zhuo-kai-fa-pian
nav: บทที่ 49: ตั้งค่าสภาพแวดล้อมการพัฒนา — Android Studio กับโปรเจกต์แรก
toc: default
kind: chapter
---

### บทที่ 49: ติดตั้งสภาพแวดล้อมการพัฒนา — Android Studio กับโปรเจกต์แรกของคุณ

{class="chapter-intro mb-4"}
ก่อนทำงานให้เป็น ต้องลับเครื่องมือให้คมก่อน บทนี้เราจะสร้าง "ห้องครัว" ให้พร้อม: ติดตั้ง Android Studio รันโปรแกรมจำลองให้ได้ สร้างโปรเจกต์ Android แรกในชีวิต แล้วแกะโครงสร้างโปรเจกต์ดูให้เห็นกับตา พอตั้งสภาพแวดล้อมเสร็จ คุณจะได้เห็นเป็นครั้งแรกว่าโค้ดที่เขียนเองกลายเป็นปุ่มที่กดได้จริง — หลายคนจำวินาทีนั้นได้ตลอดชีวิต

#### 1. ติดตั้ง Android Studio

Android Studio คือ IDE แบบครบวงจรอย่างเป็นทางการของ Google ฟรี และรวมทุกอย่างไว้ในตัว: เขียนโค้ด ดูพรีวิวหน้าจอ ดีบัก แพ็กไฟล์ ทำได้ครบในโปรแกรมเดียว ติดตั้ง 4 ขั้นตอน:

1. เปิดเว็บทางการ developer.android.com/studio แล้วดาวน์โหลดเวอร์ชันเสถียรล่าสุด (สิงหาคม 2026 คือเวอร์ชันหลังจาก Narwhal มีทั้ง Windows/Mac/Linux);
2. รันไฟล์ติดตั้งแล้วกด "ถัดไป" ไปเรื่อย ๆ — ตัวติดตั้งจะหยิบ Android SDK กับคอมโพเนนต์โปรแกรมจำลองมาให้เองอัตโนมัติ;
3. ครั้งแรกที่เปิดโปรแกรม ให้ดาวน์โหลดคอมโพเนนต์ SDK ตามที่ขึ้นบอก (เอาตามค่าเริ่มต้นที่ติ๊กไว้ก็พอ อาจใช้เวลาไม่กี่นาทีและพื้นที่หลาย GB);
4. พอเสร็จ คุณจะเห็นหน้าต้อนรับ — ยินดีด้วย "ห้องครัว" พร้อมแล้ว

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ข้อควรรู้: เช็กสเปกเครื่องให้อยู่ในมือ

{class="mt-1"}
Android Studio เป็นตัว "กินแรม" ตัวยง: แนะนำแรม 16GB ขึ้นไป (8GB ก็รันได้ แต่พอเปิดโปรแกรมจำลองจะกระตุกหน่อย) จองพื้นที่ดิสก์ไว้ 20GB ขึ้นไป และ CPU ต้องรองรับการจำลองเสมือน (เปิด VT-x/AMD-V ใน BIOS) ถ้าคอมเก่าจริง ๆ ใช้ "ดีบักบนเครื่องจริง" แทนโปรแกรมจำลองได้ (จะเล่าในหัวข้อที่ 4 ของบทนี้) ประสบการณ์ใช้งานกลับลื่นกว่า
:::

#### 2. สร้างโปรเจกต์แรกของคุณ

ที่หน้าต้อนรับกด New Project เลือกเทมเพลต Empty Activity (เทมเพลตที่สะอาดที่สุดสำหรับมือใหม่) แล้วกรอกสามอย่างนี้:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">รายการตั้งค่า</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">กรอกอะไร</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">คำอธิบาย</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">My First App</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ชื่อแอป แสดงบนหน้าโฮมของมือถือ</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Package name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example.myfirstapp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ตัวระบุที่ไม่ซ้ำทั่วโลก ธรรมเนียมคือ "เขียนโดเมนกลับด้าน" ตอนนี้ใช้ค่าเริ่มต้นไปก่อน</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minimum SDK</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API 26(Android 8.0)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เวอร์ชันขั้นต่ำที่รองรับ ครอบคลุมอุปกรณ์ 95%+</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
สามอย่างที่ต้องกรอกตอนสร้างโปรเจกต์

พอกด Finish Android Studio จะใช้ Gradle ดาวน์โหลดไลบรารีที่ต้องใช้และบิลด์โปรเจกต์ให้อัตโนมัติ (ครั้งแรกต้องรอสักไม่กี่นาที ครั้งต่อ ๆ ไปจะเร็วขึ้นเยอะ) บิลด์เสร็จ คุณก็มีแอปที่รันได้แล้ว — แม้ตอนนี้มันยังแสดงแค่บรรทัดเดียวว่า "Hello Android!"

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
เคล็ดลับ: เรื่องที่ต้องรู้เรื่องชื่อแพ็กเกจ

{class="mt-1"}
ชื่อแพ็กเกจ (package name) เหมือน "เลขบัตรประชาชน" ของแอป ห้ามซ้ำกันทั่วโลก และเปลี่ยนไม่ได้อีกแล้วหลังขึ้นสโตร์ ใช้ com.example.xxx ไว้ฝึกหัดส่วนตัวก็พอ แต่ของจริงต้องเปลี่ยนเป็นโดเมนของคุณเองเขียนกลับด้าน (เช่น com.ชื่อคุณ.ชื่อแอป) อย่าเอา com.example ขึ้นสโตร์เด็ดขาด — ร้านค้าจะไม่รับ
:::

#### 3. ทำให้รันได้: โปรแกรมจำลองกับเครื่องจริง

โค้ดเขียนเสร็จ ก็ต้องหา "มือถือ" มารัน คุณมีสองทางเลือก:

##### 1) โปรแกรมจำลอง (Emulator)

โปรแกรมจำลองคือการจำลองมือถือ Android ขึ้นมาในเครื่องคอม ใน Android Studio เปิด Device Manager → Create Device เลือกเครื่องสักเครื่อง (แนะนำสาย Pixel) → เลือกไฟล์ภาพระบบ (แบบที่มาพร้อม Google APIs) → ดาวน์โหลด → เปิดเครื่อง จากนั้นกดสามเหลี่ยมเขียว Run บนแถบเครื่องมือ อีกไม่กี่วินาที แอปของคุณก็โผล่บนหน้าจอ "มือถือ"

##### 2) ดีบักบนเครื่องจริง (แนะนำมากกว่า)

เครื่องจริงคือสภาพแวดล้อมทดสอบที่จริงที่สุดเสมอ — ลูกแรกตอนปัดหน้าจอ เน็ตจริง เซ็นเซอร์จริง โปรแกรมจำลองเทียบไม่ติด การดีบักบนมือถือ Android จริงทำได้ง่าย ๆ:

1. บนมือถือเปิด [การตั้งค่า] → [เกี่ยวกับโทรศัพท์] แตะ "หมายเลขเวอร์ชัน" ติดกัน 7 ครั้ง เพื่อเปิด "ตัวเลือกนักพัฒนา";
2. ใน [ตัวเลือกนักพัฒนา] เปิด USB debugging;
3. เสียบสายข้อมูลเชื่อมเข้าคอม พอมือถือเด้งหน้าต่างถาม ให้เลือก "อนุญาต USB debugging";
4. กลับไปที่ Android Studio มือถือของคุณจะโผล่ในรายการอุปกรณ์บนแถบเครื่องมือ กด Run ได้เลย

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ข้อควรระวัง: อย่าเปิด USB debugging ค้างไว้ตลอด

{class="mt-1"}
การเปิด USB debugging เหมือนเปิด "ประตูหลัง" ให้คอมพิวเตอร์ ตอนชาร์จในที่สาธารณะหรือเสียบกับคอมที่ไม่น่าเชื่อถือ ต้องปิด USB debugging เสมอ กันคนอื่นอ่านข้อมูลของคุณผ่านมัน ใช้เสร็จตอนพัฒนาก็ปิดทันที ทำให้เป็นนิสัย
:::

#### 4. แกะโครงสร้างโปรเจกต์: แต่ละไฟล์ทำหน้าที่อะไร

ครั้งแรกที่เปิดโปรเจกต์ แผนผังไฟล์ฝั่งซ้ายอาจทำให้คุณตาลาย ไม่ต้องตกใจ งานพัฒนาประจำวัน 90% ของคุณ มีคู่หูแค่ตัวที่อยู่ด้านล่างนี้:

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="300" viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="300" fill="#fafafa" rx="8"/>
      <text x="20" y="30" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ โฟลเดอร์รากของโปรเจกต์</text>
      <rect x="30" y="45" width="540" height="230" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <text x="45" y="70" font-size="11" fill="#4f46e5" font-weight="bold">app/ ← ที่ที่คุณเขียนโค้ด</text>
      <rect x="60" y="82" width="240" height="178" fill="#eef2ff" rx="5"/>
      <text x="70" y="102" font-size="10" fill="#1e1b4b" font-weight="bold">src/main/</text>
      <text x="80" y="120" font-size="10" fill="#374151">├ java/…/MainActivity.kt  ← โค้ดตรรกะ</text>
      <text x="80" y="138" font-size="10" fill="#374151">├ res/  ← รีซอร์ส (รูป ข้อความ สี)</text>
      <text x="80" y="156" font-size="10" fill="#374151">└ AndroidManifest.xml  ← "ทะเบียนบ้าน" ของแอป</text>
      <text x="70" y="180" font-size="10" fill="#1e1b4b" font-weight="bold">build.gradle.kts</text>
      <text x="80" y="198" font-size="10" fill="#6b7280">ประกาศไลบรารีที่ใช้ (เวอร์ชัน SDK, Compose ฯลฯ)</text>
      <text x="70" y="222" font-size="10" fill="#1e1b4b" font-weight="bold">src/androidTest/ และ test/</text>
      <text x="80" y="240" font-size="10" fill="#6b7280">โค้ดเทสต์อัตโนมัติ (ใช้ในบทที่ 56)</text>
      <rect x="320" y="82" width="230" height="178" fill="#f0fdf4" rx="5"/>
      <text x="330" y="102" font-size="10" fill="#065f46" font-weight="bold">ไฟล์อื่น ๆ ในโฟลเดอร์ราก</text>
      <text x="340" y="122" font-size="10" fill="#374151">gradle/ + gradlew.bat  ← สคริปต์บิลด์</text>
      <text x="340" y="142" font-size="10" fill="#374151">settings.gradle.kts  ← ตั้งค่าโปรเจกต์</text>
      <text x="340" y="162" font-size="10" fill="#6b7280">(คำสวดของมือใหม่: แตะแค่โฟลเดอร์ app/ </text>
      <text x="340" y="180" font-size="10" fill="#6b7280">ส่วนที่เหลือให้ถือเป็น "กล่องดำ" อย่าไปยุ่งก่อน)</text>
      <text x="340" y="208" font-size="10" fill="#9ca3af">.gitignore  ← รายการไฟล์ที่ไม่รวมใน version control</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
ภาพที่ 2: โครงสร้างโปรเจกต์ที่มือใหม่ต้องรู้ (จำง่าย ๆ: แตะแค่โฟลเดอร์ app/)
:::

- MainActivity.kt: "ประตูหลัก" ของแอป ผู้ใช้กดไอคอนเปิด ตัวแรกที่ถูกปลุกคือมัน ในเทมเพลตปัจจุบันมันทำหน้าที่แสดง "Hello Android!"
- AndroidManifest.xml: "ทะเบียนบ้าน" ของแอป — ประกาศว่าแอปนี้ชื่ออะไร ใช้ไอคอนตัวไหน มีหน้าอะไรบ้าง และต้องขอสิทธิ์อะไร (กล้อง ระบุตำแหน่ง ฯลฯ)
- โฟลเดอร์ res/: คลังทรัพยากร เก็บรูปภาพ ไอคอน ข้อความ สี เก็บข้อความไว้ในไฟล์ทรัพยากรแทนที่จะเขียนฝังไว้ในโค้ด เป็นนิสัยที่ดีของการพัฒนา Android (เปลี่ยนภาษา เปลี่ยนธีมก็ง่าย)
- build.gradle.kts: สูตรการบิลด์ — ประกาศเวอร์ชันขั้นต่ำที่รองรับ และใช้ไลบรารีอะไรบ้าง (เช่น Compose)

#### 5. ลองมือกันหน่อย: เปลี่ยน "Hello" เป็นชื่อของคุณ

เปิด MainActivity.kt คุณจะเห็นโค้ดที่เทมเพลต Compose สร้างไว้ หาบรรทัด Text("Hello Android!") แล้วเปลี่ยนข้อความในเครื่องหมายคำพูดเป็นชื่อของคุณ เช่น Text("สวัสดี สมชาย! นี่คือแอปแรกของฉัน") จากนั้นกด Ctrl+R (บน Mac คือ Cmd+R) รันใหม่ อีกไม่กี่วินาที โปรแกรมจำลองก็แสดงชื่อของคุณให้เห็น

::: div .code-block
:::inline div .code-head
<span>KOTLIN · MainActivity.kt (แก้บรรทัดนี้)</span><span class="dots">···</span>
:::

```
setContent {
    MyFirstAppTheme {
        Surface(modifier = Modifier.fillMaxSize()) {
            // ▼ แก้ตรงนี้เป็นข้อความของคุณเอง
            Text("สวัสดี ซานผวน! นี่คือแอปแรกของฉัน")
        }
    }
}
```
:::

ยินดีด้วย คุณเพิ่งวนจบหนึ่งรอบ "แก้โค้ด → คอมไพล์ → ติดตั้ง → รัน" แบบสมบูรณ์ วงจรนี้แหละคือชีวิตประจำวันของการพัฒนาในทุกวันข้างหน้า รีบต่อความมันส์ต่อเลย ลองแก้อย่างอื่นดูอีก: ขยายตัวอักษรให้ใหญ่ขึ้น เปลี่ยนสี — บทต่อไปเราจะเรียนว่า "เวทมนตร์" เหล่านี้มาจากไหน

#### 6. หน้าด่านเจอ error ที่พบบ่อย: "ห้องฉุกเฉิน" ของมือใหม่สองสัปดาห์แรก

ช่วงตั้งสภาพแวดล้อมและบิลด์ครั้งแรก คุณมีโอกาสสูงมากที่จะเจอ error สามแบบนี้ ไม่ต้องตกใจ มียาแก้ทุกตัว:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">อาการ error</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">สาเหตุที่พบบ่อย</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ยาแก้</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle sync failed / ดาวน์โหลดไลบรารีช้า</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เครือข่ายเข้าถึง repository ไม่คล่อง</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ตั้งค่า Gradle ให้ใช้ repository มิเรอร์ที่เร็วในภูมิภาค (มิเรอร์ maven อย่าง Aliyun/Tencent Cloud) ค้นเว็บหา "gradle mirror" แล้วทำตาม</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">คอมโพเนนต์ SDK ขาดหาย</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ตอนติดตั้งข้ามการดาวน์โหลด SDK</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ไปที่ Settings → SDK Manager ติดตั้งเพลตฟอร์มกับเครื่องมือที่ขาดให้เรียบร้อย</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">โปรแกรมจำลองเปิดไม่ขึ้น / จอดำ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ยังไม่ได้เปิดการจำลองเสมือน หรือไฟล์ภาพระบบเสียหาย</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เปิด VT-x/AMD-V ใน BIOS; ลบโปรแกรมจำลองทิ้งแล้วสร้างใหม่; หรือใช้ดีบักบนเครื่องจริงไปเลย</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
ตารางหน้าด่าน error ตอนตั้งสภาพแวดล้อมสำหรับมือใหม่

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
เคล็ดลับ: วิธีค้นหา error

{class="mt-1"}
บรรทัดแรกของข้อความ error มีค่าที่สุด — คัดลอกตามตัวไปใส่ในเสิร์ชเอนจิน แล้วเติมคำว่า "android studio" อย่าค้นคำกว้าง ๆ ว่า "ติดตั้งสภาพแวดล้อมไม่ได้ทำยังไงดี" ให้ค้นคำเจาะจงอย่าง "Gradle sync failed: Could not resolve com.android.tools.build" คำถามแม่นยำเท่านั้น จึงจะได้คำตอบแม่นยำ
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ลงมือทำด้วยกัน: ทำเช็กลิสต์ "พิธีกรรมนักพัฒนา" ของคุณให้ครบ

{class="mt-1"}
1) ติดตั้ง Android Studio และรันโปรแกรมจำลองให้ได้; 2) รันแอปของตัวเองบนเครื่องจริงสักครั้งและแคปหน้าจอเก็บไว้; 3) เปลี่ยนข้อความ Hello เป็นชื่อของคุณ; 4) บีบอัดโปรเจกต์เก็บสำรองไว้ ทำครบสี่ข้อนี้ คุณก็ประกาศได้เต็มปากว่า: ฉันก็เป็นนักพัฒนา Android แล้ว (มีภาพแคปเป็นหลักฐาน)
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
สรุปบทนี้

- Android Studio = IDE ฟรีอย่างเป็นทางการ; แนะนำแรม 16GB + ดิสก์ 20GB + เปิดการจำลองเสมือน
- สามองค์ประกอบของโปรเจกต์ใหม่: ชื่อ, ชื่อแพ็กเกจ (ไม่ซ้ำทั่วโลก อย่าขึ้นสโตร์ด้วย com.example), SDK ขั้นต่ำ (เริ่มที่ API 26)
- สองวิธีรัน: โปรแกรมจำลอง (มือถือเสมือนในคอม) กับเครื่องจริง (เปิด USB debugging ใช้เสร็จอย่าลืมปิด)
- จำง่าย ๆ เรื่องโปรเจกต์: แตะแค่โฟลเดอร์ app/ — MainActivity.kt คือประตูหลัก, Manifest คือทะเบียนบ้าน, res/ คือคลังทรัพยากร
- ชีวิตประจำวันนักพัฒนา = แก้โค้ด → Run → ดูผล วนซ้ำไปเรื่อย ๆ
:::
