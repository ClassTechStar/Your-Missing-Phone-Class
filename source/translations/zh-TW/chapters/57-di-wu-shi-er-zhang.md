---
id: di-wu-shi-er-zhang
num: 52
part: an-zhuo-kai-fa-pian
nav: 第五十二章：四大元件與Activity生命週期
toc: default
kind: chapter
---

### 第五十二章：四大元件與 Activity 生命週期

{class="chapter-intro mb-4"}
如果說 Compose 是 App 的"臉"，那這一章講的就是 App 的"骨架"。安卓系統有四大基本元件，所有 App 都是由它們拼成的；而其中最重要的 Activity，有一張每個安卓開發者都必須刻在腦子裡的"生命週期圖"。本章學完，你就能理解"為什麼切個後臺回來，我的 App 狀態就沒了"這類千古之謎。

#### 一、四大元件：安卓的"四梁八柱"

安卓官方定義了四種基本元件，分別負責一類工作：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">元件</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">職責</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">打個比方</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activity</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一個可見的介面</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">店鋪的門面——使用者能看見、能互動</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Service</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">後臺幹活的"隱形人"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">倉庫工人——放音樂、下載檔案，不需要介面</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BroadcastReceiver</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">接收系統廣播</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">傳達室——"電池沒電了""網路斷了"的喇叭</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ContentProvider</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跨 App 共享資料</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">公共資料櫃——比如把聯絡人共享給別的 App</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
安卓四大元件速覽

新手階段你 95% 的時間都在跟 Activity 打交道；Service 和 BroadcastReceiver 做音樂播放、訊息推送時會用到；ContentProvider 用得最少（系統已把常用資料封好了）。另外注意：四大元件都要在 AndroidManifest.xml 裡"登記戶口"，不登記系統就找不到它們。

#### 二、Activity 生命週期：安卓開發的第一張"藏寶圖"

手機上的 App 隨時可能被打斷：來電話了、使用者切去回微信、系統記憶體不夠把你殺了……Activity 的一生，就是在這張圖上迴圈旅行：

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onCreate（出生：初始化）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onStart（可見了）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onResume（前臺互動中）</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onPause（部分被遮住）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onStop（完全看不見）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center">onDestroy（銷燬）</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">🔁 onRestart / onStart / onResume：回到前臺時原路返回</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 4：Activity 生命週期（前進方向：上排出生 → 下排離場，回來時原路折返）
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">回撥</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">什麼時候觸發</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">典型用途</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onCreate</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activity 建立時（一次）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">載入介面、初始化資料</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStart</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">介面變為可見</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">開始一些輕量邏輯</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onResume</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">拿到焦點、可互動</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">開始動畫、還原播放</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onPause</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">被部分遮擋/切走瞬間</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">暫停動畫、儲存草稿</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStop</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">完全不可見</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">釋放重資源、暫停下載</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onDestroy</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">被銷燬前</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最後的清理</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
六個生命週期回撥的典型用途

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
避坑提醒：螢幕旋轉會"殺死"Activity

{class="mt-1"}
新手最經典的翻車現場：App 轉一下螢幕，輸入框裡的字全沒了。原因：旋轉螢幕預設會銷燬並重建 Activity（走一遍 onDestroy → onCreate）。解法：用 rememberSaveable 儲存狀態（Compose 裡替代 remember），它會在重建時自動把值找回來。第 6、7 章會反覆用到。
:::

#### 三、Intent：App 裡外通行的"車票"

Intent（意圖）是元件之間通訊的"車票"。你想從一個頁面跳到另一個頁面，或者開啟瀏覽器、調起相機，都要"買票上車"：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 用 Intent 跳轉</span><span class="dots">···</span>
:::

```
// 方式一：顯式 Intent——明確指定去哪個頁面
val intent = Intent(this, DetailActivity::class.java)
intent.putExtra("name", "張三")     // 車上捎帶"行李"（資料）
startActivity(intent)

// 方式二：隱式 Intent——只說要幹什麼，系統找誰幹
val web = Intent(Intent.ACTION_VIEW, Uri.parse("https://developer.android.com"))
startActivity(web)   // 系統會開啟瀏覽器/或讓你選
```
:::

兩種方式各有用途：顯式用於自己 App 內部的頁面跳轉；隱式用於呼叫系統或其他 App 的能力（開網頁、打電話、分享）。Compose 專案裡，在 Composable 中用 LocalContext.current 拿到 Context 就能 startActivity。

#### 四、多頁面與導航

真實 App 都有多個頁面。Compose 官方推薦的導航方案是 Navigation Compose（依賴庫 androidx.navigation）：

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

// 在頁面裡跳轉：
navController.navigate("detail/張三")     // 帶引數
navController.popBackStack()              // 返回上一頁
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：頁面多了怎麼辦？

{class="mt-1"}
專案長大後，把所有頁面路由集中寫在一個檔案裡（比如 AppNavGraph.kt），統一管理，別讓"跳轉到哪"的邏輯散落在各個頁面。這是從"能跑"走向"可維護"的第一步。
:::

#### 五、順帶認識：Fragment 是什麼（以及為什麼本書沒教）

查老教學時你一定會撞見 Fragment——它是 Activity 裡的"可複用介面片段"，在老式多頁面架構裡是絕對主角。但 Compose 時代，頁面直接用 Composable 函式 + Navigation 路由就夠了，官方也已弱化 Fragment 的地位。本書因此沒把它放進主線。

給你的建議：新專案不主動用 Fragment；但讀老程式碼、面試被問到時，知道它是"Activity 裡嵌的介面片段"即可。學習資源永遠優先選 2023 年以後的——安卓技術棧的"老黃曆"更新得比想象中快。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：給計數器裝上"記憶"

{class="mt-1"}
把第 51 章的計數器改造一下：① 把 remember 換成 rememberSaveable，旋轉螢幕驗證數字還在；② 加一個"關於"按鈕，用 Navigation 跳到第二個頁面顯示版本號；③ 在兩個頁面的 onCreate/onPause 裡列印日誌（Log.d），用 Logcat 觀察生命週期呼叫順序。做完這三步，生命週期就不再是紙上談兵。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 四大元件：Activity（門面）、Service（後臺）、BroadcastReceiver（喇叭）、ContentProvider（資料櫃）
- 生命週期六回撥：onCreate → onStart → onResume → onPause → onStop → onDestroy
- 旋轉螢幕會銷燬重建 Activity：用 rememberSaveable 保住狀態
- Intent 是"車票"：顯式跳自家頁面，隱式調系統能力
- 多頁面用 Navigation Compose：NavHost + composable 路由
:::
