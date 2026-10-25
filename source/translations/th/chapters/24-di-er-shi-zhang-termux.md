---
id: di-er-shi-zhang-termux
part: jin-jie-pian
nav: บทที่ 20 ภาคผนวก
toc: sub
kind: supplement
---

### บทที่ 20 ภาคผนวก: Termux — สภาพแวดล้อม Linux แบบพกพาบนอุปกรณ์ Android

{class="chapter-intro mb-4"}
ถ้าคุณรู้สึกว่าโหมดนักพัฒนายังไม่ "ฮาร์ดคอร์" พอ และอยากสัมผัสบรรทัดคำสั่ง Linux เต็มรูปแบบบนมือถือ Termux คือคำตอบสำหรับคุณ มันไม่ต้องใช้สิทธิ์ root ก็ทำให้มือถือ Android ธรรมดากลายเป็นสถานีงาน Linux แบบพกพา เป็นอาวุธลับของสายขั้นสูงในการสำรวจงานพัฒนาและดูแลระบบบนอุปกรณ์เคลื่อนที่

#### หนึ่ง Termux คืออะไร

Termux เป็นแอปเทอร์มินัลจำลองและสภาพแวดล้อม Linux โอเพนซอร์สที่ออกแบบมาเพื่ออุปกรณ์ Android โดยเฉพาะ ไม่ต้องมีสิทธิ์ root ก็ให้ประสบการณ์ Linux shell ครบวงจรบนมือถือ เป็นแอปขนาดเบา (แพ็กเกจติดตั้งราว 30MB) ใช้ระบบจัดการแพ็กเกจ APT ที่มีซอฟต์แวร์ให้เลือกมากมาย รัน Python, Node.js, Git, SSH ฯลฯ บนอุปกรณ์เคลื่อนที่ได้ จะตั้งเซิร์ฟเวอร์หรือทำเพนเทสต์ก็ยังได้

จุดแข็งหลักของ Termux คือความเบาและความยืดหยุ่นสูง เหมาะกับหลากหลายสถานการณ์ ทั้งงานพัฒนา การเรียนรู้ และการจัดการระบบ มันรวมแพ็กเกจมาตรฐานกับการจำลองเทอร์มินัลที่แม่นยำไว้ในโซลูชันโอเพนซอร์สชุดเดียว

#### สอง ฟังก์ชันหลักและจุดเด่น

##### 🖥️ สภาพแวดล้อม Linux ครบวงจร

Termux<strong>มีเพียง Bash</strong>Shell ชนิดเดียวเท่านั้น หากต้องการใช้ Shell ตัวอื่น เช่น Zsh หรือ fish จะต้องติดตั้งด้วยตนเองผ่านตัวจัดการแพ็กเกจ ตัวอย่างเช่น:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install zsh</code>หรือ<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install fish</code>ในขณะเดียวกัน Termux ก็รองรับโปรแกรมแก้ไขข้อความอย่าง Vim, Nano, Emacs เป็นต้น มอบประสบการณ์การใช้งาน Command Line ที่ใกล้เคียงกับของจริง ผู้ใช้สามารถติดตั้งแพ็กเกจซอฟต์แวร์ได้มากกว่า 2000 รายการผ่าน "pkg install" ซึ่งรวมถึงเครื่องมือสำหรับการพัฒนาและความปลอดภัย เช่น GCC, OpenSSH, SQLMap เป็นต้น

##### 📦 การจัดการแพ็กเกจที่ทรงพลัง

ใช้ตัวจัดการแพ็กเกจ APT (คล้าย Debian และ Ubuntu) ติดตั้งแพ็กเกจ Linux ได้เป็นพัน ๆ ตัว ครอบคลุมทั้งเครื่องมือพัฒนา เครื่องมือเครือข่าย ฯลฯ รองรับสภาพแวดล้อมภาษาโปรแกรมหลากหลาย ทั้ง Python, Ruby, Node.js, Go, Rust, Swift

##### 🔒 ฟังก์ชันความปลอดภัยและเครือข่าย

- <strong>การเชื่อมต่อระยะไกลด้วย SSH</strong>: รองรับทั้ง SSH ไคลเอนต์และเซิร์ฟเวอร์ เชื่อมต่อไปยังอุปกรณ์อื่นจากระยะไกลได้ หรือให้มือถือเป็นเครื่อง SSH ก็ยังได้
- <strong>เครื่องมือเข้ารหัส</strong>: มีเครื่องมือเข้ารหัสอย่าง OpenSSL รองรับการเข้ารหัสข้อมูลและการสื่อสารอย่างปลอดภัย
- <strong>การตั้งเซิร์ฟเวอร์</strong>: ตั้งค่า Nginx หรือ Apache เป็นเว็บเซิร์ฟเวอร์แบบสถิตได้

##### 🔧 การเชื่อมรวมกับระบบและส่วนขยาย

- : เข้าถึงสิทธิ์พื้นที่จัดเก็บของมือถือ ทำการจัดการไฟล์ในเครื่องได้
- Termux:Styling
- : รองรับคีย์บอร์ดบลูทูธและการเชื่อมต่อจอภาพภายนอก มีการรองรับเมาส์แบบครบวงจร

#### สาม ระบบนิเวศปลั๊กอิน

แอปหลักของ Termux สามารถขยายความสามารถได้ผ่านปลั๊กอินเสริมไม่กี่ตัว ซึ่งมอบฟังก์ชันเพิ่มเติมและการเชื่อมรวมกับสิ่งอื่น:

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ชื่อปลั๊กอิน</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">คำอธิบายฟังก์ชัน</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:API</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">: ทำให้โปรแกรมบรรทัดคำสั่งเรียกใช้ฟังก์ชัน Android API ได้</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Boot</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">: อนุญาตให้รันสคริปต์ตอนเปิดเครื่อง</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Float</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">: ให้หน้าต่างเทอร์มินัลแบบลอยได้</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Styling</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">: เปิดให้ปรับแต่งชุดสีและฟอนต์ของเทอร์มินัล</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Tasker</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">: รวมสคริปต์ Termux เข้ากับแอปอัตโนมัติอย่าง Tasker</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Widget</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">: อนุญาตให้รันสคริปต์จากวิดเจ็ตบนหน้าจอหลัก</td>
                            </tr>
                        </tbody>
                    </table>
```

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>ข้อควรรู้สำคัญ

{class="mt-1"}
Termux และปลั๊กอินต้องติดตั้งจากแหล่งเดียวกัน เพราะมันแชร์ sharedUserId เดียวกัน การติดตั้งปนกันจากหลายแหล่ง (เช่น F-Droid กับ GitHub) จะทำให้ติดตั้งผิดพลาด
:::

#### สี่ คู่มือติดตั้งและกำหนดค่า

##### 📥 ขั้นตอนการติดตั้ง

1. <strong>ดาวน์โหลดแอป</strong>: ดาวน์โหลดและติดตั้ง Termux จากช่องทางทางการ (F-Droid หรือ GitHub) ไม่ต้องใช้สิทธิ์ root
2. <strong>ตั้งค่าเริ่มต้นระบบ</strong>: หลังเปิดครั้งแรก รอให้ "Installing bootstrap packages" เสร็จสมบูรณ์
3. <strong>รับสิทธิ์พื้นที่จัดเก็บ</strong>: รันคำสั่ง<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-setup-storage</code>: รับสิทธิ์การเข้าถึงระบบไฟล์ของมือถือ
4. <strong>อัปเดตซอร์สซอฟต์แวร์</strong>: รันคำสั่ง<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update && pkg upgrade</code>: อัปเดตรายการแพ็กเกจซอฟต์แวร์

##### ⚙️ การเพิ่มประสิทธิภาพพื้นฐาน

- <strong>เปลี่ยนซอร์สมิเรอร์</strong>: ใช้คำสั่ง<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-change-repo</code>คำสั่งนี้เปลี่ยนซอร์สมิเรอร์ผ่านอินเทอร์เฟซกราฟิก (แนะนำซอร์สมิเรอร์มหาวิทยาลัยชิงหัว)
- <strong>ตั้งค่าปุ่มลัด</strong>: ปุ่มลดเสียงจำลอง Ctrl ปุ่มเพิ่มเสียงจำลอง Esc ช่วยเพิ่มประสิทธิภาพการพิมพ์
- <strong>จัดหน้าตาอินเทอร์เฟซ</strong>: ติดตั้ง Zsh + Oh My Zsh ตั้งค่าธีมและปลั๊กอิน

#### ห้า สถานการณ์การใช้งานทั่วไป

##### 💻 ทดสอบการพัฒนาบนมือถือ

สร้างสภาพแวดล้อมพัฒนาครบวงจรบนมือถือ เขียนและรันสคริปต์ Python คอมไพล์โปรแกรม C ด้วย GCC จัดการรีโปโค้ดด้วย Git และเชื่อมกับเซิร์ฟเวอร์ระยะไกลผ่าน SSH

##### 🖥️ ดูแลรักษาเซิร์ฟเวอร์

จัดการเซิร์ฟเวอร์จากระยะไกลผ่าน SSH ทำงานบำรุงรักษาระบบ วิเคราะห์ล็อก ฯลฯ แก้ปัญหาเซิร์ฟเวอร์ได้ทุกเมื่อทุกที่

##### 📚 ฝึกเรียนการใช้ Linux

มอบสภาพแวดล้อม Linux ที่แท้จริง ถือเป็นแพลตฟอร์มในอุดมคติสำหรับการเรียนรู้ Command Line และการจัดการระบบ สามารถฝึกฝนการเขียน Shell Script, การจัดการสิทธิ์ไฟล์ Linux (เช่น <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chmod 755</code> เพื่อตั้งค่าบิตสิทธิ์ rwxr-xr-x, <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chown user:group</code> เพื่อแก้ไขเจ้าของไฟล์, <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls -l</code> เพื่อดูสิทธิ์ทั้ง 9 บิตแบ่งเป็น 3 กลุ่มของ owner/group/other) และคำสั่งพื้นฐานอื่นๆ โปรดทราบว่านี่คือโมเดลสิทธิ์แบบ "สามกลุ่มเก้าบิต" แบบคลาสสิกของ Unix/Linux (owner / group / other × อ่าน / เขียน / ทำงาน) ซึ่งเป็นระบบที่แตกต่างกันโดยสิ้นเชิงกับระบบรายการควบคุมการเข้าถึงแบบ ACL ของ Windows NTFS

##### 🔐 ทดสอบความปลอดภัยเครือข่าย

ติดตั้งเครื่องมือด้านความปลอดภัยอย่าง Nmap, SQLMap, Hydra, Metasploit ทำการสแกนเครือข่ายและทดสอบเจาะระบบ

#### หก เวอร์ชันและความเข้ากันได้

Termux เวอร์ชันเสถียรล่าสุดคือ v0.118.2 ใช้กับอุปกรณ์ Android ≥ 7 จุดที่ต้องสังเกตคือ Termux บน Android 12 ขึ้นไปอาจมีความไม่เสถียร แนะนำติดตามบันทึกการอัปเดตทางการเพื่อดูข้อมูลความเข้ากันได้ล่าสุด

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>สรุป

{class="mt-1"}
Termux นำประสบการณ์เทอร์มินัล Linux อันทรงพลังมาสู่อุปกรณ์ Android ทำให้มือถือกลายเป็นเครื่องมือพัฒนาและเรียนรู้แบบพกพา ไม่ว่าคุณจะเป็นนักพัฒนา ผู้ดูแลระบบ หรือสายเทค ทุกคนใช้ Termux สัมผัสประสบการณ์บรรทัดคำสั่งครบวงจรบนอุปกรณ์เคลื่อนที่ได้ ทำให้ "Linux ในกระเป๋า" เป็นจริงขึ้นมาได้
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>ลงมือทำ: รันคำสั่ง Linux คำสั่งแรกบนมือถือให้ผ่าน

{class="list-decimal pl-6 mt-1 space-y-1"}
1. : ดาวน์โหลดและติดตั้ง Termux จาก F-Droid เปิดครั้งแรกรอการตั้งค่าเริ่มต้นให้เสร็จ
2. รันคำสั่ง<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update && pkg upgrade</code>: อัปเดตแพ็กเกจซอฟต์แวร์
3. ติดตั้ง Python:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install python</code>
4. พิมพ์<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python3 -c "print('Hello from Termux!')"</code>: แล้วรู้สึกถึงความสุขของการรันโค้ดบนมือถือดู
:::
