---
id: di-wu-shi-er-zhang
num: 52
part: an-zhuo-kai-fa-pian
nav: 第五十二章：四大組件與Activity生命週期
toc: default
kind: chapter
---

### 第五十二章：四大組件與 Activity 生命之期

{class="chapter-intro mb-4"}
若謂 Compose 為 App 之「顏」，則此章所言者，App 之「骸」也。安卓系統有四大基本組件，凡 App 皆由之拼成；而其中至要者曰 Activity，有一「生命之期圖」，凡安卓開發者皆須銘之於心。此章既學，則「何切後臺而返，吾 App 之狀態遂失」此類千古之謎，汝能解之矣。

#### 一、四大組件：安卓之「四梁八柱」

安卓官家定四種基本組件，各司一類之事：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">組件</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">職守</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">設譬</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activity</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可見之界面</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">店鋪之門面——用戶可見、可交互</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Service</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">後臺任事之「隱者」</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">倉庫之工——奏樂、下載文件，毋須界面</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BroadcastReceiver</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">受系統之廣播</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">傳達之室——「電池無電矣」「網斷矣」之喇叭</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ContentProvider</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跨 App 共享數據</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">公家資料之櫃——譬如以聯絡人共享於他 App</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
安卓四大組件速覽

新手之階，汝百分之九十五之光陰皆與 Activity 相交接；Service 與 BroadcastReceiver 者，作音樂之播、消息之推時用之；ContentProvider 用之至寡（系統已封常用之數據矣）。又當慎之：四大組件皆須於 AndroidManifest.xml 中登記戶口，不登則系統莫能尋之。

#### 二、Activity 生命之期：安卓開發之首張「藏寶圖」

機上之 App 隨時可被斷：電話至矣、用戶切而回微信、系統記憶體不足而殺汝……Activity 之一生，即於此圖上循環而遊：

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onCreate（出生：初始化）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onStart（可見了）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onResume（前臺交互中）</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onPause（部分被遮住）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onStop（完全看不見）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center">onDestroy（銷燬）</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">🔁 onRestart / onStart / onResume：返前臺時循原路而返</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 4：Activity 生命之期（行之方：上排生 → 下排離，返則原路而折）
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">回調</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">何時而發</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">典型之用</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onCreate</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activity 創建之時（一遭）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">載入界面、初化數據</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStart</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">界面轉而可見</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">始行輕量之邏輯</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onResume</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">得焦點、可交互</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">始動畫、復其播</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onPause</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">見遮其半/切走之頃</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">停動畫、存其稿</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStop</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全不可見</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">釋重資、停下載</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onDestroy</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">毀之前</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">終局之清理</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
六生命之期回調之典型用

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
避坑之警：轉屏將「殺」Activity

{class="mt-1"}
新手至經典之覆車：App 轉屏一遭，輸入框中之字盡失。其故：轉屏則常毀而重建 Activity（歷 onDestroy → onCreate 一遭）。解之之法：用 rememberSaveable 存其狀態（Compose 中代 remember 者），重建之時自尋回其值。第六、七章將屢用之。
:::

#### 三、Intent：App 內外通行之「車票」

Intent（意）者，組件之間通信之「車票」也。汝欲自一頁跳於他頁，或啟瀏覽器、起相機，皆須「買票登車」：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 用 Intent 跳轉</span><span class="dots">···</span>
:::

```
// 方式一：顯式 Intent——明指所往之頁
val intent = Intent(this, DetailActivity::class.java)
intent.putExtra("name", "張三")     // 車上附"行李"（數據）
startActivity(intent)

// 方式二：隱式 Intent——但言所為，系統自擇其人
val web = Intent(Intent.ACTION_VIEW, Uri.parse("https://developer.android.com"))
startActivity(web)   // 系統啟瀏覽器/或使汝擇
```
:::

二法各有其用：顯式者用於己 App 內頁之跳轉；隱式者用於調系統或他 App 之能（啟網頁、撥電話、分享）。Compose 項目之中，於 Composable 內以 LocalContext.current 得 Context，即可 startActivity。

#### 四、多頁與導航

真實之 App 皆有多頁。Compose 官家所薦之導航方略，曰 Navigation Compose（依賴之庫 androidx.navigation）：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Navigation Compose 骨架</span><span class="dots">···</span>
:::

```
val navController = rememberNavController()

NavHost(navController, startDestination = "home") {
    composable("home") { HomeScreen(navController) }
    composable("detail/{name}") { entry ->
        val name = entry.arguments?.getString("name")
        DetailScreen(name ?: "未知")
    }
}

// 於頁面中跳轉：
navController.navigate("detail/張三")     // 帶參數
navController.popBackStack()              // 返回上一頁
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小識：頁多則奈何？

{class="mt-1"}
項目既長，宜集諸頁之路由於一文件（譬如 AppNavGraph.kt），統而理之，毋使「跳而何往」之邏輯散於諸頁。此自「能行」趨「可維護」之第一步也。
:::

#### 五、順而識之：Fragment 為何物（及本書何以不教）

檢舊之教程，汝必遇 Fragment——其為 Activity 中「可復用界面之片段」，於舊式多頁架構中為絕對之主角。然 Compose 之世，頁面逕以 Composable 函數 + Navigation 路由足矣，官家亦已弱 Fragment 之位。本書故不列之於主線。

貽汝之議：新項目勿主動用 Fragment；然讀舊碼、面試見問之時，知其為「Activity 中所嵌之界面片段」足矣。為學之資，恆先擇 2023 年以後者——安卓技術之棧，其「老黃曆」之新，速於所想。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：為計數器裝「記憶」

{class="mt-1"}
改第五十一章之計數器：① 易 remember 為 rememberSaveable，轉屏而驗其數尚在；② 加「關於」一鈕，以 Navigation 跳於第二頁而顯版本之號；③ 於兩頁之 onCreate/onPause 中印日誌（Log.d），以 Logcat 觀生命之期調用之序。三步既畢，生命之期遂非紙上談兵矣。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 四大組件：Activity（門面）、Service（後臺）、BroadcastReceiver（喇叭）、ContentProvider（資料櫃）
- 生命之期六回調：onCreate → onStart → onResume → onPause → onStop → onDestroy
- 轉屏則毀而重建 Activity：用 rememberSaveable 保其狀態
- Intent 者「車票」也：顯式跳己頁，隱式調系統之能
- 多頁用 Navigation Compose：NavHost + composable 路由
:::
