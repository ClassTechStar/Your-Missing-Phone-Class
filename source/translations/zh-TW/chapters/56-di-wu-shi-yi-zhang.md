---
id: di-wu-shi-yi-zhang
num: 51
part: an-zhuo-kai-fa-pian
nav: 第五十一章：介面開發——Jetpack Compose入門
toc: default
kind: chapter
---

### 第五十一章：介面開發——Jetpack Compose 入門

{class="chapter-intro mb-4"}
介面是使用者看到的一切。在 Compose 出現之前，安卓介面用 XML 寫——像填空題一樣繁瑣；2021 年穀歌推出了 Jetpack Compose：直接用 Kotlin 程式碼"畫"介面，所見即所得，改一行程式碼預覽立刻重新整理。到 2026 年，Compose 已是新專案的絕對主流。這一章，咱們學會"畫畫"。

#### 一、Compose 的思想：介面就是函式

Compose 的核心思想一句話：介面 = 函式。每個能顯示在螢幕上的東西（文字、按鈕、圖片）都是一個"可組合函式"（Composable），用 @Composable 標記。把它們像積木一樣巢狀起來，就是介面。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 第一個 Compose 介面</span><span class="dots">···</span>
:::

```
@Composable
fun Greeting(name: String) {
    Text(text = "你好，$name！")     // 一個"文字積木"
}

// 巢狀組合：大積木套小積木
@Composable
fun HomeScreen() {
    Column {                          // 豎著排列
        Greeting(name = "張三")
        Greeting(name = "李四")
        Button(onClick = { /* 點選做什麼 */ }) {
            Text("點我")
        }
    }
}
```
:::

注意 @Composable 這個"帽子"——它告訴編譯器"這是一個介面積木"。積木可以無限巢狀，這就是 Compose 的全部秘密。

#### 二、基礎元件：文字、按鈕、輸入框、圖片

Compose 的元件就是"積木塊"，最常見的四種：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">元件</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">幹什麼</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">必備引數</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">顯示文字</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">text（要顯示的字）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">按鈕</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onClick（點選回撥）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">輸入框</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">value、onValueChange（輸入變化回撥）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">顯示圖片</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">painter（圖片資源）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Compose 四大基礎元件

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 基礎元件示例</span><span class="dots">···</span>
:::

```
@Composable
fun BasicWidgets() {
    Column {
        Text(text = "這是一段文字")
        Button(onClick = { println("被點選了") }) {
            Text("按鈕")
        }
        var input by remember { mutableStateOf("") }
        TextField(
            value = input,
            onValueChange = { input = it },
            label = { Text("輸入點什麼") }
        )
    }
}
```
:::

輸入框那兩行裡出現了 remember { mutableStateOf("") }——這就是 Compose 的"狀態"魔法，本章第五節細講。現在先混個臉熟。

#### 三、佈局三件套：Column、Row、Box

元件有了，怎麼擺放？記住三個"盒子"：

- Column：豎著排（像排隊打飯）；
- Row：橫著排（像並排坐）；
- Box：疊著放（像撲克牌摞一起，適合做角標、遮罩）。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 佈局三件套</span><span class="dots">···</span>
:::

```
Column {
    Text("第一行")
    Row {
        Text("左邊")
        Text("右邊")
    }
    Box {
        Text("底層")
        Text("疊在上面的角標")
    }
}
```
:::

想讓佈局更好看？給元件加 Modifier（修飾符）——它就像給積木"上妝"：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Modifier 常用招式</span><span class="dots">···</span>
:::

```
Text(
    text = "好看的文字",
    modifier = Modifier
        .padding(16.dp)          // 四周留白
        .fillMaxWidth()          // 撐滿寬度
        .background(Color.Blue)  // 背景色
        .clickable { /* 點選 */ }// 可點選
)
// 鏈式呼叫：一個接一個，順序有意義（先 padding 再背景，背景不含邊距）
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：Modifier 的順序有講究

{class="mt-1"}
padding(16.dp).background(Blue) 和 background(Blue).padding(16.dp) 效果不同——前者是"先留白再塗色"（背景不含邊距），後者是"先塗色再留白"（背景包含邊距）。新手最容易在這上面畫錯"奇怪的白邊"。不確定時，調換順序試試，預覽立刻告訴你答案。
:::

#### 四、狀態：讓介面"活"起來

靜態介面沒意思。想讓按鈕點選後數字 +1、輸入框能打字，就需要狀態（State）。Compose 的規則：介面永遠忠實反映狀態，狀態變了，介面自動重畫。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 狀態：點選計數器</span><span class="dots">···</span>
:::

```
@Composable
fun Counter() {
    // remember + mutableStateOf：記住這個會變化的值
    var count by remember { mutableStateOf(0) }

    Column {
        Text(text = "你點了 $count 次")
        Button(onClick = { count++ }) {   // 改狀態
            Text("點我 +1")                // 介面自動重新整理
        }
    }
}
```
:::

三行程式碼，一個活的計數器。這就是 Compose 比老式寫法爽的地方：不用手動"重新整理介面"，改資料就行。記住兩個關鍵函式：remember（讓值在介面重組時不被清空）和 mutableStateOf（告訴 Compose"這個值變了要重畫"）。

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> 使用者點選</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> 狀態改變（count++）</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> Compose 感知到變化</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> 自動重畫介面（重組）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 3：Compose 的"狀態 → 介面"單向資料流
:::

#### 五、主題與深色模式：一次配置，全域性生效

模板專案裡的 MyFirstAppTheme { ... } 就是主題。它基於 Material 3 設計規範，幫你把顏色、字型、形狀統一管理。支援深色模式只需三步：

1. 在主題裡定義好淺色/深色兩套配色（模板已自動生成 ColorScheme）；
2. 系統切到深色模式時，isSystemInDarkTheme() 自動判斷；
3. 用主題提供的顏色（如 MaterialTheme.colorScheme.primary）而不是寫死顏色值。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：Material 3 動態取色

{class="mt-1"}
Android 12 起的"Material You"能讓 App 從你的桌布裡提取顏色。Compose 模板預設支援（dynamicColor）。你的 App 在不同使用者手機上會"自動換裝"，這就是現代安卓的浪漫。
:::

#### 六、預覽、動畫與實時編輯：Compose 的"外掛"

Compose 三個開發體驗上的"外掛"，用上就回不去：

- @Preview 預覽：給 Composable 加 @Preview 註解，Android Studio 右側立刻渲染出介面——改程式碼所見即所得，不用每次裝到手機上；
- 實時編輯（Live Edit）：2026 年的 Android Studio 支援在模擬器/真機上"熱更新"部分改動，改文字顏色之類的小調整，裝置上秒變；
- 動畫 API：animateFloatAsState、AnimatedVisibility 幾行程式碼就能讓元素平滑過渡——"進階感"往往就差這幾十行。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 十分鐘上手的動畫</span><span class="dots">···</span>
:::

```
@Composable
fun AnimatedBox() {
    var big by remember { mutableStateOf(false) }
    // 值變化時自動平滑過渡到目標值
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
小貼士：先功能後動畫

{class="mt-1"}
新手常犯的毛病是"介面還沒做對，就開始糾結動畫"。先讓功能跑通，最後再統一加動效——這也是"簡單至上"原則：動畫是錦上添花，功能是雪中送炭。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：做一個"心情按鈕"

{class="mt-1"}
把模板專案改成一個心情切換器：一個按鈕，點選後在 😀開心 → 😢難過 → 😡生氣 之間迴圈切換，文字和背景色跟著變。提示：用 when 根據狀態選文案和顏色。做完發給朋友玩，收穫第一波"哇你會做 App 了"。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- Compose 思想：介面 = @Composable 函式，積木式巢狀
- 四大元件：Text / Button / TextField / Image
- 佈局三件套：Column 豎排、Row 橫排、Box 疊放
- Modifier 鏈式"上妝"：padding、fillMaxWidth、background、clickable——順序有意義
- 狀態是靈魂：remember + mutableStateOf，改資料介面自動重畫
- 主題用 Material 3 + 動態取色，深色模式一次配置全域性生效
:::
