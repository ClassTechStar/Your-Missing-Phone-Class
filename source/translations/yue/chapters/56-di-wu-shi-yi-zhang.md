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
介面係用戶見到嘅所有嘢。喺 Compose 出現之前，安卓介面用 XML 寫——好似填空題咁麻煩；2021 年穀歌推出咗 Jetpack Compose：直接用 Kotlin 程式碼「畫」介面，所見即所得，改一行程式碼預覽即刻刷新。到 2026 年，Compose 已經係新項目嘅絕對主流。呢一章，我哋學識「畫畫」。

#### 一、Compose 嘅思想：介面就係函數

Compose 嘅核心思想一句講曬：介面 = 函數。每樣可以顯示喺螢幕上面嘅嘢（文字、按鈕、圖片）都係一個「可組合函數」（Composable），用 @Composable 標記。將佢哋好似積木噉嵌套埋一齊，就係介面。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 第一個 Compose 界面</span><span class="dots">···</span>
:::

```
@Composable
fun Greeting(name: String) {
    Text(text = "你好，$name！")     // 一嚿"文字積木"
}

// 巢狀組合：大積木套小積木
@Composable
fun HomeScreen() {
    Column {                          // 直向排列
        Greeting(name = "張三")
        Greeting(name = "李四")
        Button(onClick = { /* 㩒咗做乜 */ }) {
            Text("㩒我")
        }
    }
}
```
:::

留意 @Composable 呢頂「帽」——佢話畀編譯器知「呢個係一嚿介面積木」。積木可以無限嵌套，呢個就係 Compose 嘅全部秘密。

#### 二、基礎組件：文字、按鈕、輸入框、圖片

Compose 嘅組件就係「積木」，最常見嘅四種：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">組件</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">做乜嘢</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">必備參數</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">顯示文字</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">text（要顯示嘅字）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">按鈕</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onClick（點擊回調）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">輸入框</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">value、onValueChange（輸入變化回調）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">顯示圖片</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">painter（圖片資源）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Compose 四大基礎組件

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 基礎組件示例</span><span class="dots">···</span>
:::

```
@Composable
fun BasicWidgets() {
    Column {
        Text(text = "呢度係一段文字")
        Button(onClick = { println("被㩒咗") }) {
            Text("按鈕")
        }
        var input by remember { mutableStateOf("") }
        TextField(
            value = input,
            onValueChange = { input = it },
            label = { Text("輸入啲乜嘢") }
        )
    }
}
```
:::

輸入框嗰兩行入面出現咗 remember { mutableStateOf("") }——呢個就係 Compose 嘅「狀態」魔法，本章第五節會詳細講。而家先混個面熟。

#### 三、佈局三件套：Column、Row、Box

組件有咗，點樣擺放？記住三個「盒」：

- Column：打直排（好似排隊打飯噉）；
- Row：打橫排（好似並排坐噉）；
- Box：疊住放（好似啤牌疊埋一齊，適合做角標、遮罩）。

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
        Text("疊喺上面嘅角標")
    }
}
```
:::

想佈局更加好睇？畀組件加 Modifier（修飾符）——佢就好似畀積木「上妝」噉：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Modifier 常用招式</span><span class="dots">···</span>
:::

```
Text(
    text = "靚嘅文字",
    modifier = Modifier
        .padding(16.dp)          // 四圍留白
        .fillMaxWidth()          // 撐滿闊度
        .background(Color.Blue)  // 背景色
        .clickable { /* 㩒 */ }// 㩒得
)
// 鏈式調用：一個接一個，次序有意義（先 padding 再背景，背景唔包邊距）
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：Modifier 嘅次序有講究

{class="mt-1"}
padding(16.dp).background(Blue) 同 background(Blue).padding(16.dp) 效果唔同——前者係「先留白再塗色」（背景唔包邊距），後者係「先塗色再留白」（背景包埋邊距）。新手最容易喺呢度畫錯「奇怪嘅白邊」。唔確定嗰陣，調轉次序試吓，預覽即刻話你知答案。
:::

#### 四、狀態：畀介面「活」起上嚟

靜態介面冇乜意思。想撳掣之後數字 +1、輸入框可以打字，就需要狀態（State）。Compose 嘅規則：介面永遠忠實反映狀態，狀態一變，介面自動重畫。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 狀態：點擊計數器</span><span class="dots">···</span>
:::

```
@Composable
fun Counter() {
    // remember + mutableStateOf：記住呢個會變嘅值
    var count by remember { mutableStateOf(0) }

    Column {
        Text(text = "你㩒咗 $count 次")
        Button(onClick = { count++ }) {   // 改狀態
            Text("㩒我 +1")                // 界面自動刷新
        }
    }
}
```
:::

三行程式碼，一個識郁嘅計數器。呢個就係 Compose 比舊式寫法正嘅地方：唔使手動「刷新介面」，改資料就得。記住兩個關鍵函數：remember（令個值喺介面重組嗰陣唔會被清空）同 mutableStateOf（話畀 Compose 知「呢個值變咗要重畫」）。

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> 用戶點擊</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> 狀態改變（count++）</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> Compose 感知到變化</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> 自動重畫界面（重組）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 3：Compose 嘅「狀態 → 介面」單向資料流
:::

#### 五、主題同深色模式：一次配置，全局生效

模板項目入面嘅 MyFirstAppTheme { ... } 就係主題。佢基於 Material 3 設計規範，幫你將顏色、字體、形狀統一管理。支援深色模式只需要三步：

1. 喺主題入面定義好淺色／深色兩套配色（模板已經自動生成咗 ColorScheme）；
2. 系統轉去深色模式嗰陣，isSystemInDarkTheme() 會自動判斷；
3. 用主題提供嘅顏色（例如 MaterialTheme.colorScheme.primary）而唔係寫死顏色值。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：Material 3 動態取色

{class="mt-1"}
Android 12 開始嘅「Material You」可以令 App 由你嘅桌布入面提取顏色。Compose 模板預設支援（dynamicColor）。你個 App 喺唔同用戶嘅手機上面會「自動換裝」，呢個就係現代安卓嘅浪漫。
:::

#### 六、預覽、動畫同實時編輯：Compose 嘅「外掛」

Compose 三個開發體驗上嘅「外掛」，一用咗就返唔到轉頭：

- @Preview 預覽：畀 Composable 加 @Preview 註解，Android Studio 右邊即刻 render 出個介面——改程式碼所見即所得，唔使每次都裝落手機度；
- 實時編輯（Live Edit）：2026 年嘅 Android Studio 支援喺模擬器／真機上面「熱更新」部分改動，改文字顏色呢類小調整，設備上面即刻變；
- 動畫 API：animateFloatAsState、AnimatedVisibility 幾行程式碼就可以令元素平滑過渡——「高級感」往往就差咗呢幾十行。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 十分鐘上手的動畫</span><span class="dots">···</span>
:::

```
@Composable
fun AnimatedBox() {
    var big by remember { mutableStateOf(false) }
    // 值變嗰陣自動平滑過渡到目標值
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
新手成日犯嘅毛病係「介面都未整啱，就開始糾結動畫」。先令功能行通，最後先統一加動效——呢個亦都係「簡單至上」原則：動畫係錦上添花，功能係雪中送炭。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
嚟動手：整一個「心情按鈕」

{class="mt-1"}
將模板項目改成一個心情切換器：一個按鈕，點擊之後喺 😀開心 → 😢難過 → 😡嬲 之間循環切換，文字同背景色跟住變。提示：用 when 根據狀態揀文案同顏色。做完傳畀朋友玩，收穫第一波「嘩你識整 App 喇」。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- Compose 思想：介面 = @Composable 函數，積木式嵌套
- 四大組件：Text / Button / TextField / Image
- 佈局三件套：Column 打直排、Row 打橫排、Box 疊放
- Modifier 鏈式「上妝」：padding、fillMaxWidth、background、clickable——次序有意義
- 狀態係靈魂：remember + mutableStateOf，改資料介面自動重畫
- 主題用 Material 3 + 動態取色，深色模式一次配置全局生效
:::
