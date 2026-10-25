---
id: di-wu-shi-yi-zhang
num: 51
part: an-zhuo-kai-fa-pian
nav: บทที่ 51: การพัฒนาหน้าจอ — เริ่มต้น Jetpack Compose
toc: default
kind: chapter
---

### บทที่ 51: พัฒนาหน้าจอ — เริ่มต้นกับ Jetpack Compose

{class="chapter-intro mb-4"}
หน้าจอคือทุกสิ่งที่ผู้ใช้เห็น ก่อน Compose จะเกิดขึ้น หน้าจอ Android เขียนด้วย XML — ยุ่งยากเหมือนทำโจทย์เติมช่องว่าง; ปี 2021 Google เปิดตัว Jetpack Compose: เขียนโค้ด Kotlin "วาด" หน้าจอไปตรง ๆ เห็นอย่างไรได้อย่างนั้น แก้โค้ดหนึ่งบรรทัดพรีวิวก็เด้งใหม่ทันที มาถึงปี 2026 Compose กลายเป็นกระแสหลักของโปรเจกต์ใหม่เด็ดขาด ในบทนี้ เราจะเรียน "วาดรูป" กัน

#### 1. แนวคิดของ Compose: หน้าจอก็คือฟังก์ชัน

แนวคิดหลักของ Compose พูดในประโยคเดียว: หน้าจอ = ฟังก์ชัน ทุกอย่างที่แสดงบนหน้าจอได้ (ข้อความ ปุ่ม รูปภาพ) ล้วนเป็น "ฟังก์ชันประกอบได้" (Composable) ที่มาร์กด้วย @Composable เอามาซ้อนกันเหมือนต่อบล็อกเลโก้ ก็กลายเป็นหน้าจอ

::: div .code-block
:::inline div .code-head
<span>KOTLIN · UI Compose แรกของคุณ</span><span class="dots">···</span>
:::

```
@Composable
fun Greeting(name: String) {
    Text(text = "สวัสดี $name!")     // บล็อก "ข้อความ" หนึ่งชิ้น
}

// ประกอบซ้อนกัน: ชิ้นใหญ่ครอบชิ้นเล็ก
@Composable
fun HomeScreen() {
    Column {                          // เรียงตามแนวตั้ง
        Greeting(name = "ซานผวน")
        Greeting(name = "ลี่ซือ")
        Button(onClick = { /* แตะแล้วทำอะไร */ }) {
            Text("แตะฉัน")
        }
    }
}
```
:::

สังเกต "หมวก" ที่ชื่อ @Composable — มันบอกคอมไพเลอร์ว่า "นี่คือบล็อกต่อหน้าจอ" บล็อกซ้อนกันได้ไม่จำกัด นี่คือความลับทั้งหมดของ Compose

#### 2. คอมโพเนนต์พื้นฐาน: ข้อความ ปุ่ม ช่องกรอก รูปภาพ

คอมโพเนนต์ของ Compose ก็คือ "บล็อกต่อ" ที่เจอบ่อยที่สุดมีสี่ตัว:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">คอมโพเนนต์</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">ทำอะไร</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">พารามิเตอร์ที่ต้องมี</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">แสดงข้อความ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">text (ข้อความที่จะแสดง)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ปุ่ม</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onClick (ฟังก์ชันเรียกกลับตอนกด)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ช่องกรอกข้อความ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">value, onValueChange (ฟังก์ชันเรียกกลับเมื่อข้อความเปลี่ยน)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">แสดงรูปภาพ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">painter (ทรัพยากรรูปภาพ)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
คอมโพเนนต์พื้นฐานหลักสี่ตัวของ Compose

::: div .code-block
:::inline div .code-head
<span>KOTLIN · ตัวอย่างคอมโพเนนต์พื้นฐาน</span><span class="dots">···</span>
:::

```
@Composable
fun BasicWidgets() {
    Column {
        Text(text = "นี่คือข้อความ")
        Button(onClick = { println("ถูกแตะแล้ว") }) {
            Text("ปุ่ม")
        }
        var input by remember { mutableStateOf("") }
        TextField(
            value = input,
            onValueChange = { input = it },
            label = { Text("พิมพ์อะไรก็ได้") }
        )
    }
}
```
:::

ในสองบรรทัดของช่องกรอกนั้นปรากฏ remember { mutableStateOf("") } — นี่คือเวทมนตร์เรื่อง "สถานะ" ของ Compose จะอธิบายละเอียดในหัวข้อที่ 5 ของบทนี้ ตอนนี้แค่ทำหน้าคลุกเคล้าก่อน

#### 3. สามชิ้นเลย์เอาต์: Column, Row, Box

มีคอมโพเนนต์แล้ว จัดวางยังไง? จำ "กล่อง" สามใบนี้:

- Column: เรียงแนวตั้ง (เหมือนต่อแถวรับอาหาร);
- Row: เรียงแนวนอน (เหมือนนั่งเคียงกัน);
- Box: วางซ้อนกัน (เหมือนไพ่กองทับกัน เหมาะทำป้ายมุม เลเยอร์ซ้อน)

::: div .code-block
:::inline div .code-head
<span>KOTLIN · ชุดสามชิ้นของเลย์เอาต์</span><span class="dots">···</span>
:::

```
Column {
    Text("บรรทัดแรก")
    Row {
        Text("ซ้าย")
        Text("ขวา")
    }
    Box {
        Text("ชั้นล่าง")
        Text("ป้ายเล็กที่ซ้อนอยู่ด้านบน")
    }
}
```
:::

อยากให้เลย์เอาต์สวยขึ้น? เพิ่ม Modifier (ตัวแต่งแต้ม) ให้คอมโพเนนต์ — เหมือนแต่งหน้าให้บล็อก:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Modifier ที่ใช้บ่อย</span><span class="dots">···</span>
:::

```
Text(
    text = "ข้อความสวย ๆ",
    modifier = Modifier
        .padding(16.dp)          // เว้นรอบด้าน
        .fillMaxWidth()          // กว้างเต็มแถว
        .background(Color.Blue)  // สีพื้นหลัง
        .clickable { /* แตะ */ }// แตะได้
)
// ลูกโซ่: เรียงต่อกันทีละตัว ลำดับมีผล (padding ก่อน แล้วพื้นหลัง พื้นหลังไม่รวมช่องว่าง)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ข้อควรรู้: ลำดับของ Modifier มีผล

{class="mt-1"}
padding(16.dp).background(Blue) กับ background(Blue).padding(16.dp) ผลลัพธ์ต่างกัน — แบบแรกคือ "เว้นระยะก่อนแล้วค่อยราบสี" (พื้นหลังไม่รวมขอบ) ส่วนแบบหลังคือ "ราบสีก่อนแล้วค่อยเว้นระยะ" (พื้นหลังรวมขอบ) มือใหม่เจอ "ขอบขาวประหลาด" ที่วาดผิดตรงนี้บ่อยที่สุด ถ้าไม่แน่ใจ ลองสลับลำดับดู พรีวิวจะบอกคำตอบทันที
:::

#### 4. สถานะ: ทำให้หน้าจอ "มีชีวิต"

หน้าจอนิ่ง ๆ ไม่สนุก อยากให้กดปุ่มแล้วเลข +1 ให้พิมพ์ในช่องกรอกได้ ก็ต้องมีสถานะ (State) กฎของ Compose: หน้าจอสะท้อนสถานะอย่างซื่อสัตย์เสมอ สถานะเปลี่ยนเมื่อไร หน้าจอวาดใหม่ให้เอง

::: div .code-block
:::inline div .code-head
<span>KOTLIN · สเตต: ตัวนับการแตะ</span><span class="dots">···</span>
:::

```
@Composable
fun Counter() {
    // remember + mutableStateOf: จำค่าที่เปลี่ยนได้นี้ไว้
    var count by remember { mutableStateOf(0) }

    Column {
        Text(text = "คุณแตะไป $count ครั้ง")
        Button(onClick = { count++ }) {   // แก้สเตต
            Text("แตะฉัน +1")                // หน้าจอเด้งเอง
        }
    }
}
```
:::

สามบรรทัด ได้ตัวนับที่มีชีวิต นี่คือจุดที่ Compose สบายกว่าสไตล์เก่า: ไม่ต้อง "รีเฟรชหน้าจอ" ด้วยมือเอง แค่แก้ข้อมูลก็พอ จำสองฟังก์ชันสำคัญไว้: remember (ทำให้ค่าไม่ถูกล้างตอนหน้าจอ recompose) กับ mutableStateOf (บอก Compose ว่า "ค่านี้เปลี่ยนแล้วต้องวาดใหม่")

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> ผู้ใช้แตะ</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> สเตตเปลี่ยน (count++)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> Compose ตรวจจับการเปลี่ยนแปลง</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> วาด UI ใหม่อัตโนมัติ (recomposition)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
ภาพที่ 3: การไหลของข้อมูลทางเดียว "สถานะ → หน้าจอ" ของ Compose
:::

#### 5. ธีมกับโหมดมืด: ตั้งครั้งเดียว มีผลทั้งแอป

MyFirstAppTheme { ... } ในโปรเจกต์เทมเพลตนั่นแหละคือธีม มันอิงมาตรฐานดีไซน์ Material 3 ช่วยจัดการสี ฟอนต์ รูปทรงให้เป็นระบบเดียวกัน รองรับโหมดมืดแค่สามขั้นตอน:

1. นิยามชุดสีแบบสว่าง/มืดไว้ในธีม (เทมเพลตสร้าง ColorScheme ให้เองอยู่แล้ว);
2. เมื่อระบบสลับไปโหมดมืด isSystemInDarkTheme() จะตัดสินใจให้เอง;
3. ใช้สีจากธีม (เช่น MaterialTheme.colorScheme.primary) แทนการเขียนค่าสีฝังตาย

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
เคล็ดลับ: สีแบบไดนามิกของ Material 3

{class="mt-1"}
ตั้งแต่ Android 12 เป็นต้นมา "Material You" ทำให้แอปดึงสีจากวอลเปเปอร์ของคุณได้ เทมเพลต Compose รองรับตามค่าเริ่มต้น (dynamicColor) แอปของคุณจะ "เปลี่ยนชุด" เองบนมือถือผู้ใช้แต่ละคน นี่คือความโรแมนติกแบบ Android ยุคใหม่
:::

#### 6. พรีวิว อนิเมชัน และการแก้สด: "ไอเทมเสริมพลัง" ของ Compose

ของเสริมพลังสามอย่างเรื่องประสบการณ์พัฒนาของ Compose พอใช้แล้วย้อนกลับไปแบบเดิมไม่ได้อีกเลย:

- พรีวิว @Preview: ใส่ annotation @Preview ให้ Composable Android Studio จะเรนเดอร์หน้าจอทางขวาทันที — แก้โค้ดเห็นผลทันทีทันใด ไม่ต้องติดตั้งลงมือถือทุกครั้ง;
- การแก้สด (Live Edit): Android Studio ปี 2026 รองรับ "อัปเดตร้อน" การแก้บางส่วนบนโปรแกรมจำลอง/เครื่องจริง ปรับเล็ก ๆ อย่างเปลี่ยนสีข้อความ เห็นผลบนเครื่องภายในวินาทีเดียว;
- API อนิเมชัน: animateFloatAsState, AnimatedVisibility ใช้แค่ไม่กี่บรรทัดก็ให้เอฟเฟกต์เนียน ๆ — "ความพรีเมียม" มักขาดแค่สิบกว่าบรรทัดแบบนี้เอง

::: div .code-block
:::inline div .code-head
<span>KOTLIN · แอนิเมชันเรียน 10 นาทีเป็น</span><span class="dots">···</span>
:::

```
@Composable
fun AnimatedBox() {
    var big by remember { mutableStateOf(false) }
    // เปลี่ยนค่าแล้วเลื่อนไปค่าใหม่อย่างนุ่มนวลอัตโนมัติ
    val size by animateDpAsState(if (big) 120.dp else 60.dp)

    Box(Modifier
        .size(size)
        .background(MaterialTheme.colorScheme.primary)
        .clickable { big = !big }
    )
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
เคล็ดลับ: ฟังก์ชันก่อน อนิเมชันทีหลัง

{class="mt-1"}
โรคประจำตัวของมือใหม่คือ "หน้าจอยังไม่ถูก ก็ไปจุกจิกกับอนิเมชัน" ให้ฟังก์ชันรันผ่านก่อน แล้วค่อยใส่เอฟเฟกต์ทีเดียวท้ายสุด — นี่ก็คือหลัก "เรียบง่ายเหนือสิ่งใด": อนิเมชันคือดอกไม้ประดับ ฟังก์ชันคือถ่านยามหนาว
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
ลงมือทำด้วยกัน: สร้าง "ปุ่มอารมณ์"

{class="mt-1"}
แปลงโปรเจกต์เทมเพลตเป็นเครื่องสลับอารมณ์: ปุ่มเดียว กดแล้ววนสลับระหว่าง 😀ดีใจ → 😢เศร้า → 😡โมโห ข้อความกับสีพื้นหลังเปลี่ยนตาม คำใบ้: ใช้ when เลือกข้อความกับสีตามสถานะ เสร็จแล้วส่งให้เพื่อนเล่น เก็บกระแสคลื่นแรกว่า "โห ทำแอปเป็นแล้ว" ดู
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
สรุปบทนี้

- แนวคิด Compose: หน้าจอ = ฟังก์ชัน @Composable ซ้อนกันแบบต่อบล็อก
- คอมโพเนนต์หลักสี่ตัว: Text / Button / TextField / Image
- เลย์เอาต์สามชิ้น: Column เรียงแนวตั้ง, Row เรียงแนวนอน, Box วางซ้อน
- Modifier แต่งตัวแบบลูกโซ่: padding, fillMaxWidth, background, clickable — ลำดับมีความหมาย
- สถานะคือดวงวิญญาณ: remember + mutableStateOf แก้ข้อมูลเมื่อไรหน้าจอวาดใหม่เอง
- ธีมใช้ Material 3 + สีไดนามิก โหมดมืดตั้งครั้งเดียวมีผลทั้งแอป
:::
