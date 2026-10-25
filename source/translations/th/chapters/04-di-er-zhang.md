---
id: di-er-zhang
num: 02
part: ji-chu-pian
nav: บทที่ 2: จัดห้องดิจิทัลของคุณ
toc: default
kind: chapter
---

### บทที่ 2: จัดระเบียบห้องดิจิทัลของคุณ — การจัดการไฟล์

{class="chapter-intro mb-4"}
โทรศัพท์ใช้นานๆ จะรก นิสัยที่ดีเริ่มจากการจัดการไฟล์ เหมือนห้องของคุณที่ต้องจัดเป็นระยะ พื้นที่ดิจิทัลของคุณก็ต้องดูแล โทรศัพท์ที่เป็นระเบียบไม่แค่หาของง่าย ยังทำงานลื่นไหลด้วย

#### 1. ระบบจัดเก็บข้อมูลสามชั้น: คลังดิจิทัลของคุณ

{class="list-decimal pl-6 mb-3 space-y-2"}
1. <strong>ตัวเครื่องจัดเก็บ</strong>: โซนแกนกลาง ความเร็วเร็ว ระบบและแอปทั้งหมดอยู่ตรงนี้ เป็นพื้นที่ล้ำค่าที่สุดของโทรศัพท์ ต้องใช้อย่างช่างคำนวณ
2. <strong>SDการ์ด(ถ้ารองรับ)</strong>: ตู้เสื้อส่วนขยาย ความเร็วช้ากว่านิดหน่อย เหมาะกับหนัง รูปภาพ และไฟล์ใหญ่ๆ ข้อสังเกต: ตอนนี้โทรศัพท์ฟลากชิปจำนวนมากไม่รองรับ SD การ์ดแล้ว
3. <strong>คลาวด์จัดเก็บ</strong>: ตู้นิรภัย + เว็บไดรฟ์ซิงก์ กันของหาย และซิงก์ข้ามหลายอุปกรณ์ได้ iCloud, Baidu Netdisk, OneDrive ล้วนเป็นตัวเลือกยอดนิยม

#### 2. รู้จัก "File Manager"

แอนดรอยด์มักมีแอป [ไฟล์] หรือ [ไฟล์จัดการ] ส่วน iOS ใช้แอป [ไฟล์] ที่มาในตัว ทั้งสองคือ "ตัวจัดการทรัพยากร" ที่ไว้ดูไฟล์ทั้งหมดในโทรศัพท์

##### ความหมายของโฟลเดอร์ที่พบบ่อย:

- <strong>DCIM</strong>: รูปและวิดีโอที่ถ่ายจากกล้อง
- <strong>Pictures</strong>: รูปอื่นๆ เช่นภาพหน้าจอ (สกรีนช็อต) และรูปที่บันทึกมา
- <strong>Download</strong>:เบราว์เซอร์ดาวน์โหลดของไฟล์
- <strong>Music</strong>:เพลงไฟล์
- <strong>Movies</strong>:วิดีโอไฟล์
- <strong>Documents</strong>:เอกสารไฟล์
- <strong>Android</strong>: โฟลเดอร์ระบบของแอนดรอยด์ ข้างในคือข้อมูลของแอปแต่ละตัว ปกติอย่าลบด้วยมือ

#### 3. โครงสร้างระบบไฟล์: เจาะลึก

แอนดรอยด์อยู่บนฐาน Linux ระบบไฟล์จึงมีโครงสร้างลำดับชั้นที่แน่นอน แม้ผู้ใช้ทั่วไปไม่จำเป็นต้องเข้าใจลึก แต่รู้แนวคิดพื้นฐานบ้างก็มีประโยชน์

##### พาร์ติชันตัวจัดเก็บ:

- <strong>/system</strong>: พาร์ติชันระบบ เก็บไฟล์ของระบบปฏิบัติการ ผู้ใช้ทั่วไปไม่มีสิทธิ์เข้าถึง ต้องใช้สิทธิ์ root
- <strong>/data</strong>: พาร์ติชันข้อมูล เก็บข้อมูลผู้ใช้และข้อมูลแอป เป็นพื้นที่ที่คุณใช้งานในชีวิตประจำวัน
- <strong>/sdcard หรือ /storage/emulated/0</strong>: พื้นที่จัดเก็บที่ผู้ใช้เข้าถึงได้ รูปของคุณ ไฟล์ที่ดาวน์โหลด ล้วนอยู่ตรงนี้

##### Appข้อมูลจัดเก็บ:

- <strong>ในเครื่องจัดเก็บ</strong>: พื้นที่ส่วนตัวของแอป แอปอื่นเข้าไม่ได้ เมื่อถอนการติดตั้งแอปจะถูกลบไปด้วย
- <strong>นอกเครื่องจัดเก็บ</strong>: ไฟล์ที่แอปเก็บไว้ในพื้นที่ที่ผู้ใช้เข้าถึงได้ เช่นรูปภาพ ไฟล์ดาวน์โหลด เมื่อถอนการติดตั้งแอปอาจยังค้างอยู่ไม่ถูกลบ

#### 4. สำรองและกู้คืนข้อมูล: ทำประกันให้ข้อมูลของคุณ

ข้อมูลไม่มีราคา, สำรองข้อมูลใช่ต้องเลี้ยงสำเร็จของคุ้นเคย

##### สำรองข้อมูลกลยุทธ์:

1. <strong>คลาวด์สำรองข้อมูล</strong>: อัตโนมัติ สะดวก แต่ต้องใช้เครือข่ายและพื้นที่คลาวด์ iCloud, Huawei Cloud, Xiaomi Cloud ฯลฯ รองรับหมด
2. <strong>ภายในเครื่องสำรองข้อมูล</strong>: ต่อคอมพิวเตอร์ด้วยสาย แล้วใช้เครื่องมือสำรองข้อมูลทางการ เร็ว พื้นที่เยอะ แต่ต้องทำด้วยมือเอง
3. <strong>คู่หนักสำรองข้อมูล</strong>:คลาวด์สำรองข้อมูล+ภายในเครื่องสำรองข้อมูล, ที่สุดปลอดภัย

##### สำรองข้อมูลอะไร?

- <strong>รูปภาพและวิดีโอ</strong>: กินพื้นที่มากที่สุด และมีค่าที่สุดด้วย
- <strong>สมุดโทรศัพท์</strong>: เก็บไว้ในบัญชีคลาวด์สะดวกที่สุด
- <strong>ประวัติแชท WeChat</strong>: ใช้ฟังก์ชันสำรองข้อมูลของ WeChat เอง
- <strong>สำคัญเอกสาร</strong>: เก็บไว้บนคลาวด์ไดรฟ์หรือคอมพิวเตอร์

#### 5. ความปลอดภัยของไฟล์: ปกป้องความเป็นส่วนตัวของคุณ

- <strong>ว่องไวรู้สึกไฟล์เข้ารหัส</strong>: โทรศัพท์หลายรุ่นมีฟังก์ชัน "โฟลเดอร์ปลอดภัย" หรือ "พื้นที่ส่วนตัว" เอาไฟล์อ่อนไหวใส่ไว้ตรงนั้นได้ ต้องปลดล็อกด้วยรหัสผ่านหรือลายนิ้วก่อนถึงจะเข้าถึงได้
- <strong>ลบไม่เท่ากับขายทำลาย</strong>: การลบปกติเป็นแค่การทำเครื่องหมายว่าพื้นที่นี้เขียนทับได้ ข้อมูลยังอยู่ ถ้าจะลบให้สิ้นซากจริงๆ ต้องใช้เครื่องมือลบแบบปลอดภัยเฉพาะทาง หรือเขียนทับหลายรอบ
- <strong>บนคลาวด์ปลอดภัย</strong>: เลือกผู้ให้บริการคลาวด์ที่มีชื่อเสียง เปิดการยืนยันสองชั้น และตรวจสอบอุปกรณ์ที่ล็อกอินเป็นประจำ

#### 6. พื้นที่ไม่พอ? มาทำความสะอาดใหญ่

- <strong>ล้างแคช</strong>: ความจำชั่วคราวของแอป ล้างแล้วเป็นการเคลียร์ที่ ไปที่ ตั้งค่า > จัดเก็บ ล้างได้
- <strong>ค้นหาใหญ่ไฟล์</strong>: ใช้ตัวจัดการไฟล์จัดเรียงตามขนาด ตามล่า "ตัวร้าย" ที่กินพื้นที่ออกมา
- <strong>ลบเหลือเหลือไว้</strong>: หลังถอนการติดตั้งแอป บางทีจะมีไฟล์ขยะตกค้าง ล้างทิ้งด้วยมือ
- <strong>ล้างอัลบั้ม</strong>: ลบรูปที่ซ้ำกัน รูปเบลอ และภาพหน้าจอที่ไม่จำเป็น
- <strong>ล้างวีแชต</strong>: WeChat เป็นเจ้าที่กินพื้นที่ตัวยง การล้างประวัติแชทและแคชเป็นระยะจำเป็นมาก

#### 7. วิเคราะห์รูปแบบไฟล์ทั่วไปอย่างครบถ้วน

ไฟล์ในโทรศัพท์มีนามสกุลมากมายจนเวียนหัว ทำความเข้าใจมันช่วยให้คุณจัดการไฟล์ได้ดีขึ้น:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                            <thead>
                                <tr class="bg-light dark:bg-gray-700">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">รูปแบบ</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ประเภท</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">คุณสมบัติ</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">แนะนำเปิดรูปแบบ</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">JPG/JPEG</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">รูปภาพ</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">บีบอัดแบบมีข้อมูลสูญหาย ไฟล์เล็ก ความเข้ากันได้ดีที่สุด เป็นรูปแบบเริ่มต้นของการถ่ายภาพบนโทรศัพท์</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">แอปภาพ/ตัวดูรูปภาพใดก็ได้</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">PNG</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">รูปภาพ</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">บีบอัดแบบไม่สูญหาย รองรับพื้นหลังโปร่งใส ใช้บ่อยกับภาพหน้าจอและไอคอน ไฟล์ใหญ่กว่า JPG</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">แอปภาพ/ตัวดูรูปภาพใดก็ได้</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MP3</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เสียง</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">บีบอัดแบบมีข้อมูลสูญหาย ไฟล์เล็ก ความเข้ากันได้ดีมาก เป็นรูปแบบเสียงที่ใช้ได้สากลที่สุด</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">โปรแกรมเล่นเพลงใดก็ได้</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">FLAC</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เสียง</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">บีบอัดแบบไม่สูญหาย คุณภาพเสียงเทียบเท่า CD ไฟล์ใหญ่กว่า MP3 ถึง 3-5 เท่า ของโปรดสายออดิโอไฟแอน</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">โปรแกรมเล่นเพลง/แอปเล่นเฉพาะทาง</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">WAV</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เสียง</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เสียงต้นฉบับไม่บีบอัด คุณภาพดีที่สุดแต่ไฟล์มโหฬาร ใช้บ่อยในงานอัดเสียงระดับมืออาชีพ</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">โปรแกรมเล่นเพลง</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">M4A</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เสียง</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เข้ารหัสแบบ AAC คุณภาพเสียงดีกว่า MP3 ที่อัตราบิตเท่ากัน ใช้บ่อยในระบบนิเวศของแอปเปิล</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Music/โปรแกรมเล่นเพลง</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MP4</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">วิดีโอ</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">รูปแบบครอบวิดีโอที่ใช้สากลที่สุด ความเข้ากันได้ดีมาก เป็นรูปแบบเริ่มต้นของวิดีโอที่อัดจากโทรศัพท์</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">แอปภาพ/ตัวเล่นวิดีโอใดก็ได้</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MKV</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">วิดีโอ</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">รูปแบบครอบแบบโอเพนซอร์ส รองรับหลายแทร็กเสียง หลายซับไตเติล ใช้บ่อยกับไฟล์หนัง</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">VLC/nPlayer</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DOC/DOCX</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เอกสาร</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เอกสาร Word DOCX เป็นรูปแบบบีบอัด ไฟล์เล็กกว่า DOC เป็นรูปแบบเวอร์ชันเก่า</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">WPS/Office</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">PPT/PPTX</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">สาธิต</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ไฟล์นำเสนอ PowerPoint PPTX เป็นรูปแบบบีบอัด</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">WPS/Office</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">XLS/XLSX</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ตาราง</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">สเปรดชีต Excel XLSX เป็นรูปแบบบีบอัด</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">WPS/Office</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">PDF</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เอกสาร</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">รูปแบบข้ามแพลตฟอร์ม จัดหน้าตายตัวแก้ไขไม่ได้ ใช้บ่อยกับสัญญา งานวิชาการ และหนังสืออิเล็กทรอนิกส์</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Adobe Reader/WPS</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ZIP</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">บีบอัด</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">รูปแบบบีบอัดที่ใช้สากลที่สุด ใช้ข้ามแพลตฟอร์มได้ดี</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">แอปในตัวระบบ/แอปแตกไฟล์</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">RAR</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">บีบอัด</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">อัตราการบีบอัดสูงกว่า ZIP แต่ต้องใช้ซอฟต์แวร์เฉพาะในการแตกไฟล์</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">แอปแตกไฟล์</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ISO</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">อิมเมจ</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ไฟล์อิมเมจแผ่นดิสก์ คัดลอกเนื้อหาแผ่นมาทั้งหมด ใช้บ่อยกับแพ็กเกจติดตั้งระบบ</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">แอปแตกไฟล์/ไดรฟ์เสมือน</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">HTML</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">หน้าเว็บ</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ไฟล์หน้าเว็บ เปิดด้วยเบราว์เซอร์ หน้าเว็บที่บันทึกมักใช้รูปแบบนี้</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">เบราว์เซอร์</td>
                                </tr>
                            </tbody>
                        </table>
```
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>ฝึกหัด: จัดระเบียบโฟลเดอร์ "ดาวน์โหลด"

{class="mt-1"}
เปิดตัวจัดการไฟล์ > เข้าไปที่โฟลเดอร์ "ดาวน์โหลด" ดูซิว่าข้างในมีอะไรบ้าง? อันที่ไม่ใช้ก็ลบทิ้ง อันที่ใช้ก็แยกหมวดหมู่ (เช่นสร้างโฟลเดอร์ "เอกสารงาน" "สติกเกอร์/มีม" ใส่เข้าไป) พลางสำรวจพื้นที่จัดเก็บดูว่าไฟล์ประเภทไหนกินที่มากที่สุด
:::

{class="text-lg font-semibold mt-6 mb-2"}
#### 8. การจัดการรูปภาพและระบบไฟล์: จัดสินทรัพย์ให้เป็นระเบียบ

ตอนที่แล้วเราเรียน "การรู้จักโฟลเดอร์" กันไปแล้ว แต่แค่รู้จักไม่พอ ส่วนนี้จะพูดถึง<strong>วิธีสร้างกฎการจัดการที่ทำได้จริงและใช้ได้ยาวนาน</strong>ให้ไฟล์ของคุณหาเจอได้ทุกเมื่อ ไม่หาย ไม่ถูกแอบแอง

{class="font-semibold mt-4 mb-1"}
##### 1. การจัดหมวดหมู่ไฟล์และกฎการตั้งชื่อ

รากของความโกลาหลคือการไม่มีกติกา การสร้างกติกาจริงๆ ง่ายมาก จุดสำคัญอยู่ที่<strong>การทำต่ออย่างสม่ำเสมอ</strong>.

```html
<ul class="list-disc pl-6 mb-3 space-y-2">
                        <li><strong>วิธีตั้งชื่อ "เวลา+เหตุการณ์"</strong>: ชื่อโฟลเดอร์มีการประทับเวลาและคำอธิบายเหตุการณ์ ค้นกลับและนึกได้ง่ายในภายหลัง เช่น <code>202606_ตั๋วการเดินทาง</code>, <code>2025_สรุปสิ้นปี</code>, <code>2024_วันเกิดลูก</code>แบบนี้เห็นทั้งไทม์ไลน์ และรู้เนื้อหาได้ในพริบตา</li>
                        <li><strong>ระบบจำแนกสามระดับ</strong>:
                            <ul class="list-disc pl-6 mt-1 space-y-0.5">
                                <li><strong>ระดับที่หนึ่ง</strong>: แยกตามประเภทไฟล์ (เอกสาร / รูปภาพ / วิดีโอ / เสียง)</li>
                                <li><strong>ระดับที่สอง</strong>: แยกตามสถานการณ์ใช้งาน (งาน / ชีวิตประจำวัน / เรียนรู้)</li>
                                <li><strong>ระดับที่สาม</strong>: แยกตามเหตุการณ์หรือโครงการเฉพาะ (เช่น "2026Q2_โครงการA")</li>
                            </ul>
                        </li>
                        <li><strong>แผนล้างรายเดือน</strong>: กำหนดวันคงที่หนึ่งวันทุกเดือน (แนะนำวันเงินเดือนออกหรือวันที่ 1 ของเดือน) จัดระเบียบโฟลเดอร์ "ดาวน์โหลด" รวมศูนย์ทีเดียว:<strong>เก็บถาวรอันที่ใช้ได้ ลบอันที่ไม่ใช้ ย้ายเก็บอันที่ล้ำค่า</strong>จัดเล็กๆ เดือนละครั้งตลอดปี สบายกว่ารวบทุกอย่างไว้กวาดใหญ่ทีเดียวมาก</li>
                    </ul>
```

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-calendar-check mr-2"></i>รายการงานเดือนนี้

{class="mt-1"}
เลือกสุดสัปดาห์ที่ว่างสักครั้ง แล้วทำตามลำดับนี้:

{class="list-decimal pl-6 mt-1 space-y-0.5 text-sm"}
1. สร้างในตัวจัดการไฟล์ <code>2026Q2_โครงการA</code> ในรูปแบบของโฟลเดอร์งานประจำเดือน
2. ไล่ไฟล์สัปดาห์นี้ในโฟลเดอร์ "ดาวน์โหลด" ทั้งหมดหนึ่งรอบ เก็บที่ใช้ได้ จัดถาวร ลบที่ไม่ใช้
3. สร้างให้รูปครอบครัวของปีนี้ <code>2025ครอบครัว</code>, <code>2026ครอบครัว</code> โฟลเดอร์รายปีแบบนี้
:::

{class="font-semibold mt-4 mb-1"}
##### 2. กลยุทธ์จัดการไฟล์ซ้ำซ้อน

โทรศัพท์ใช้นานจะ "อ้วนขึ้น" ส่วนใหญ่เป็นพวกไฟล์ซ้ำซ้อนที่แอบแองอยู่

{class="list-disc pl-6 mb-3 space-y-2"}
- <strong>การล้างอัตโนมัติแบบ 72 ชั่วโมง</strong>: App โซเชียลอย่าง WeChat QQ รับไฟล์ชั่วคราวมากมาย (สติกเกอร์/มีม รูปในแชท วิดีโอสั้น) ส่วนใหญ่ดูรอบเดียวก็ไม่ใช้แล้ว เข้าไปที่ [WeChat] > [ตั้งค่า] > [ทั่วไป] > [พื้นที่จัดเก็บ] เปิด "ล้างอัตโนมัติ" ตั้งแคชหมดอายุที่ 72 ชั่วโมง โทรศัพท์จะสะอาดขึ้นทันที แถมไม่ทิ้งบันทึกสำคัญ
- <strong>การล้างเฉพาะจุดในพื้นที่จัดเก็บ</strong>: แอนดรอยด์ [ตั้งค่า] > [จัดเก็บ] > [ล้างและเร่งความเร็ว] iOS [ตั้งค่า] > [ทั่วไป] > [พื้นที่จัดเก็บ iPhone] ระบบจะแยกหมวดให้ว่า "แคช / ไฟล์ชั่วคราว / แอปที่ถอนได้ / ไฟล์ใหญ่" จุดที่ควรล้าง: ① ไฟล์แคช ② แพ็กเกจติดตั้งหมดอายุ (แพ็กเกจรุ่นเก่าที่ค้างหลังอัปเดตแอป) ③ ไฟล์ซ้ำ (รูปชื่อและขนาดเหมือนกัน)
- <strong>กฎการจัดหมวดหมู่อัตโนมัติ</strong>: แอปอัลบั้มของแบรนด์ส่วนใหญ่รองรับจัดหมวดอัจฉริยะ: คน ทิวทัศน์ เอกสาร สกรีนช็อต เปิดไว้แล้ว รูปหมู่ที่ถ่ายใหม่จะถูกจัดเข้า "คน > ชื่อคน" สัญญาที่สแกนก็จะถูกจัดเข้า "เอกสาร" อัตโนมัติ<strong>จับคู่กับการจัดระเบียบรายเดือน ช่วยลดโอกาส "หาของไม่เจอ" ได้อย่างมาก</strong>.

{class="font-semibold mt-4 mb-1"}
##### 3. กฎการประมวลผลรูปภาพอย่างปลอดภัย

รูปภาพเป็นประเภทข้อมูลที่ "อ่อนไหว" ที่สุดในโทรศัพท์ — ภาพถ่ายสบายๆ ภาพหนึ่งก็เปิดเผยตำแหน่ง อุปกรณ์ และเวลาของคุณได้ เราแนะนำให้<strong>สร้างเวิร์กโฟลว์ "การป้องกันสองชั้น"</strong>:

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-image mr-2"></i>ขั้นตอนมาตรฐานในการส่งรูปบัตร/สกรีนช็อตที่อ่อนไหว

{class="list-decimal pl-6 mt-1 space-y-1 text-sm"}
1. <strong>ปิดบังข้อมูลที่มองเห็นได้ (มาร์กเอาต์)</strong>: ใช้เครื่องมือในตัวระบบหรือภายนอก (เช่น Meitu, Snapseed)<strong>ระบายทับเลขบัตรประชาชนบางหลักช่วงกลาง เลขทะเบียนรถ บ้านเลขที่ ชื่อ และจำนวนเงิน</strong>และช่องข้อมูลสำคัญอื่นๆ
2. <strong>การลบข้อมูลเมตา</strong>: ก่อนส่งให้กด "แชร์" หรือ "ส่งออก" ในอัลบั้ม ระบบจะถามว่าจะเก็บข้อมูลตำแหน่งไว้หรือไม่ ให้เลือก<strong>"ไม่เก็บ"</strong>แบบนี้รุ่นอุปกรณ์ที่ถ่าย พิกัด GPS และเวลาที่ถ่าย จะไม่ถูกส่งออกไปพร้อมรูป
3. <strong>ลายน้ำชั่วคราว</strong> (ไม่บังคับ): ใส่ลายน้ำข้อความ "ใช้เพื่อดำเนินการ XX เท่านั้น" บนสกรีนช็อตที่อ่อนไหว เพื่อกันการถูกนำไปใช้ในทางที่ผิด
:::

{class="mt-3 mb-2"}
วิธีลบข้อมูลเมตา (EXIF) ที่ใช้กันทั่วไป (ขั้นพื้นฐาน ส่วนการป้องกันขั้นลึก ดูได้ที่บทที่ 6 หัวข้อ "การลบข้อมูลที่ระบุตัวตนออกจากรูปภาพ"):

- <strong>อยู่ในตัวระบบ</strong>: ใน iOS [ตั้งค่า] > [ความเป็นส่วนตัวและความปลอดภัย] > [กล้อง] ปิด "ตำแหน่งที่แม่นยำ" ได้ ตอนแชร์เลือก "เฉพาะรูปที่เลือก" จะ<strong>ลบ EXIF ส่วนใหญ่ออกโดยอัตโนมัติ</strong>.
- <strong>แอนดรอยด์</strong>: แอปอัลบั้มของแบรนด์ส่วนใหญ่จะถามตอน "แชร์" ว่า "จะเอาข้อมูลตำแหน่งออกไหม" ติ๊กเลือกก็จบ
- <strong>เครื่องมือระดับมืออาชีพ</strong>: ExifTool (บนคอมพิวเตอร์) Metapho (iOS) Photo Metadata Remover (แอนดรอยด์) ลบข้อมูลเมตาได้หมดจริงๆ

สำหรับรูปที่ต้องการ<strong>เก็บไว้ระยะยาว</strong>ของรูปที่อ่อนไหว (บัตรประชาชน บัตรธนาคาร สำเนาทะเบียนบ้าน พาสปอร์ต) แนะนำให้เก็บเข้า<strong>อัลบั้มเข้ารหัส</strong>:

- iPhone: [รูปภาพ] > เลือกรูป > ซ่อน (ดูได้หลังยืนยัน Face ID เท่านั้น)
- Huawei/Xiaomi: [อัลบั้ม] > กดค้างที่รูป > "ย้ายเข้าห้องนิรภัย"
- แอปเข้ารหัสจากภายนอก:<strong>360 อัลบั้มปลอดภัย</strong>, <strong>Tencent Album Manager (อัลบั้มส่วนตัว)</strong>, <strong>KeepSafe</strong> ฯลฯ มีรหัสผ่านป้องกันแยกของตัวเอง ซ่อนเร้นกว่า
