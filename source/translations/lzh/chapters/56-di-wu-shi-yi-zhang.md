---
id: di-wu-shi-yi-zhang
num: 51
part: an-zhuo-kai-fa-pian
nav: 第五十一章：界面開發——Jetpack Compose入門
toc: default
kind: chapter
---

### 第五十一章：界面開發——Jetpack Compose 入門

{class="chapter-intro mb-4"}
界面者，用戶所見之全也。Compose 未興之前，安卓界面以 XML 書之——繁瑣如填空之題；2021 年穀歌出 Jetpack Compose：逕以 Kotlin 代碼「畫」界面，所見即所得，改一行而預覽立新。至 2026 年，Compose 已為新項目之絕對主流。此章吾儕學「畫」之道。

#### 一、Compose 之思：界面即函數

Compose 核心之思，一言蔽之：界面 = 函數。凡可顯於屏者（文字、按鈕、圖片）皆一「可組合函數」（Composable），以 @Composable 誌之。嵌套之如積木，則界面成焉。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 第一個 Compose 界面</span><span class="dots">···</span>
:::

```
@Composable
fun Greeting(name: String) {
    Text(text = "汝好，$name！")     // 一"文字之積木"
}

// 嵌套而組：大積木套小積木
@Composable
fun HomeScreen() {
    Column {                          // 豎而列之
        Greeting(name = "張三")
        Greeting(name = "李四")
        Button(onClick = { /* 點之何為 */ }) {
            Text("點我")
        }
    }
}
```
:::

慎視 @Composable 此「冠」——所以告編譯器曰：此乃界面積木也。積木可無限相套，此即 Compose 之全祕。

#### 二、基礎組件：文字、按鈕、輸入框、圖片

Compose 之組件即「積木之塊」，至常見者四：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">組件</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">所為何事</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">必備參數</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">顯文字</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">text（所欲顯之字）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">按鈕</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onClick（點擊之回調）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">輸入框</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">value、onValueChange（輸入變化之回調）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">顯圖片</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">painter（圖片之資源）</td></tr></tbody></table>
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
        Text(text = "此乃一段文字")
        Button(onClick = { println("被點擊了") }) {
            Text("按鈕")
        }
        var input by remember { mutableStateOf("") }
        TextField(
            value = input,
            onValueChange = { input = it },
            label = { Text("輸入若干") }
        )
    }
}
```
:::

輸入框彼兩行中現 remember { mutableStateOf("") }——此即 Compose「狀態」之魔法，本章第五節詳言之。今姑識其面焉。

#### 三、布局三件：Column、Row、Box

組件既有，何以擺置？記三「盒子」：

- Column：縱而列之（如列隊而取食）；
- Row：橫而列之（如並肩而坐）；
- Box：疊而置之（如撲克之牌相壘，宜為角標、遮罩）。

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
        Text("疊於上之角標")
    }
}
```
:::

欲布局愈美乎？與組件加 Modifier（修飾符）——猶為積木「上妝」也：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Modifier 常用招式</span><span class="dots">···</span>
:::

```
Text(
    text = "美之文字",
    modifier = Modifier
        .padding(16.dp)          // 四周留白
        .fillMaxWidth()          // 滿其寬
        .background(Color.Blue)  // 背景色
        .clickable { /* 點擊 */ }// 可點擊
)
// 鏈式調用：相繼而行，序有其義（先 padding 後背景，背景不含邊距）
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
慎之：Modifier 之序有考

{class="mt-1"}
padding(16.dp).background(Blue) 與 background(Blue).padding(16.dp) 其效不同——前者「先留白後塗色」（背景不含邊距），後者「先塗色後留白」（背景含邊距）。新手最易於此畫出「怪異之白邊」。未定之時，易序而試，預覽立告汝以答。
:::

#### 四、狀態：使界面「活」

靜態之界面無味也。欲鈕點而數增一、輸入框可打字，則須狀態（State）。Compose 之則：界面恆忠以映狀態，狀態一變，界面自重畫焉。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 狀態：點擊計數器</span><span class="dots">···</span>
:::

```
@Composable
fun Counter() {
    // remember + mutableStateOf：記此將變之值
    var count by remember { mutableStateOf(0) }

    Column {
        Text(text = "汝點了 $count 次")
        Button(onClick = { count++ }) {   // 改狀態
            Text("點我 +1")                // 界面自動刷新
        }
    }
}
```
:::

三行代碼，得一活之計數器。此 Compose 勝舊式寫法之處：毋庸手動「刷新界面」，改數據足矣。記二關鍵函數：remember（使值於界面重組時不被清空）與 mutableStateOf（告 Compose 曰：此值變則當重畫）。

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> 用戶點擊</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> 狀態改變（count++）</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> Compose 感知到變化</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> 自動重畫界面（重組）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 3：Compose 之「狀態 → 界面」單向數據流
:::

#### 五、主題與深色模式：一配而全局生效

模板項目中之 MyFirstAppTheme { ... } 即主題也。其本 Material 3 設計之範，助汝一統理顏色、字體、形狀。欲支深色模式，僅需三步：

1. 於主題中定淺色/深色兩套之配色（模板已自生 ColorScheme）；
2. 系統切至深色模式時，isSystemInDarkTheme() 自判之；
3. 用主題所供之色（如 MaterialTheme.colorScheme.primary），勿硬寫色值。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小識：Material 3 動態取色

{class="mt-1"}
自 Android 12 起，「Material You」能使 App 自汝壁紙取色。Compose 模板默認支之（dynamicColor）。汝之 App 於不同用戶之機上將自易其裝，此現代安卓之浪漫也。
:::

#### 六、預覽、動畫與實時編輯：Compose 之「外掛」

Compose 開發體驗之「外掛」有三，一用則不可復返：

- @Preview 預覽：與 Composable 加 @Preview 之註，Android Studio 右側立渲染界面——改碼所見即所得，不必每番裝於機上；
- 實時編輯（Live Edit）：2026 年之 Android Studio 支於模擬器/真機上「熱更新」部分之改，若易文字顏色之屬小調，機上秒變；
- 動畫 API：animateFloatAsState、AnimatedVisibility 數行代碼即令諸元平滑而過——「高級之感」往往僅欠此數十行耳。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 十分鐘上手的動畫</span><span class="dots">···</span>
:::

```
@Composable
fun AnimatedBox() {
    var big by remember { mutableStateOf(false) }
    // 值變則自平滑至標之
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
小識：先功能後動畫

{class="mt-1"}
新手常犯之病，乃「界面尚未做對，遽糾結於動畫」。先使功能通焉，終乃一統加動效——此亦「簡單至上」之則：動畫者錦上添花也，功能者雪中送炭也。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：作一「心情按鈕」

{class="mt-1"}
易模板項目為心情切換之器：一鈕，點之則於 😀喜 → 😢哀 → 😡怒 之間循環而切，文與背景之色隨之而變。提示：以 when 依狀態擇文案與色。既成以遺友玩之，可獲第一波「哇汝能作 App 矣」。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- Compose 之思：界面 = @Composable 函數，積木式相套
- 四大組件：Text / Button / TextField / Image
- 布局三件：Column 縱列、Row 橫列、Box 疊置
- Modifier 連環「上妝」：padding、fillMaxWidth、background、clickable——其序有意
- 狀態者魂也：remember + mutableStateOf，數據一變界面自重畫
- 主題用 Material 3 + 動態取色，深色模式一配而全局生效
:::
