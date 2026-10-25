---
id: di-wu-shi-ba-zhang
num: 58
part: an-zhuo-kai-fa-pian
nav: 第五十八章：速查手冊與資源
toc: default
kind: chapter
---

### 第五十八章：速查手冊與資源

{class="chapter-intro mb-4"}
本章是一份可以獨立使用的速查手冊。當你記不清某個寫法或需要快速決策時，直接翻到這裡。建議把它當成"口袋卡片"：常用程式碼速查、常見問題、學習資源，一頁不落。

#### 一、常用程式碼速查卡

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要做什麼</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">關鍵程式碼</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">記住一個可變狀態</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">var x by remember { mutableStateOf(初值) }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">轉屏不丟狀態</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">rememberSaveable { mutableStateOf(初值) }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">豎排/橫排佈局</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Column { }</code> / <code class="inline">Row { }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">懶載入列表</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">LazyColumn { items(列表) { ... } }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">頁面跳轉</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">navController.navigate("路由")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">協程裡乾等活兒</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">viewModelScope.launch { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">觀察資料流</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">val list by flow.collectAsState()</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">存小配置</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">context.dataStore.edit { it[KEY] = 值 }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">存結構化資料</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room 三件套：@Entity / @Dao / @Database</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">聯網取資料</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit 介面 + suspend 函式</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">發通知</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">NotificationChannel + NotificationCompat.Builder</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">打日誌</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Log.d("TAG", "message")</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
安卓開發速查卡（2026 年 8 月版）

#### 二、常見問題 FAQ

Q1：我完全不會程式設計，學安卓開發要多久？

按本書路徑走：第 1-2 周裝環境、學 Kotlin 基礎；第 3-4 周學 Compose 做出介面；第 5-6 周完成記帳本專案；第 7-8 周做完天氣專案。兩個月，從零到能獨立做小 App。前提是每天投入 1-2 小時，且動手敲程式碼而不是隻看書。

Q2：Java 還要學嗎？

不用。新專案、新教學、新崗位基本都以 Kotlin 為準。只在"維護十年老專案"時才會遇到大量 Java。學完 Kotlin 後如果工作需要，再補 Java 會很快——兩者底層是同一個虛擬機器生態。

Q3：模擬器還是真機？

開發除錯用模擬器很方便（快照、多機型），但驗收一定要過真機——觸感、效能、真實網路、感測器，模擬器取代不了。條件允許的話，買一台中階真機當測試機，是最符合成本效益的投資。

Q4：安卓開發好找工作嗎？

2026 年的行情：純"會寫介面"的初級崗位競爭激烈，但"懂 Kotlin + 會架構 + 有上線作品"的開發者依然搶手。學習期的你，最好的簡歷就是商店裡那個自己做的 App。

Q5：遇到報錯卡住了怎麼辦？

黃金三步：① 把報錯第一行原樣搜 StackOverflow/搜尋引擎；② 查官方文件對應頁面；③ 還不行，就把"期望行為 + 實際現象 + 報錯全文 + 相關程式碼"打包發給 AI 或社群提問。絕大多數問題，第一步就解決了。

#### 三、推薦學習資源

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">型別</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">資源</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">推薦理由</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">developer.android.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">安卓官方文件，Compose/Kotlin 教學都在裡面，第一權威</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin 官網 (kotlinlang.org)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">語言官方文件 + 線上演練場</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Google Codelabs</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">手把手的分步實驗課，新手友好度滿分</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">社群</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stack Overflow (android 標籤)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">報錯求救第一站</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">社群</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">掘金 / CSDN 安卓專區</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">中文實戰文章多，注意甄別新舊（先看日期）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">影片</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Google Developers 官方頻道</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每年的開發者大會新技術講解</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">配套</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第七篇《AI程式設計實戰篇》（第37-47章）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用 AI 輔助安卓開發的完整心法</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
安卓開發學習資源清單（2026 年 8 月）

#### 四、Gradle 常用命令速查

平時點按鈕就夠，但命令列有時更高效（尤其是配合 AI 工具或 CI 流水線時）：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">命令</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">作用</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew assembleDebug</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">打一個除錯版 APK（Windows 把 ./ 去掉）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew assembleRelease</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">打發布版（需配好籤名）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew test</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跑全部單元測試</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew lint</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">靜態檢查：找出潛在 bug 和不規範寫法</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew clean</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">清空構建產物（"重啟大法"的編譯版）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew :app:dependencies</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">檢視依賴樹（排查版本衝突神器）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Gradle 常用命令速查

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：構建出問題先 clean

{class="mt-1"}
"昨天還能跑今天就不行"的靈異事件，十有六七是構建快取錯亂。./gradlew clean 之後重新構建，能治癒一大半玄學問題。還不行再重啟 Android Studio——這招請配合 File → Invalidate Caches 一起服用。
:::

#### 五、結語：從第一個 App 到第 N 個 App

回頭看，你從"不知道 Activity 是什麼"，到裝好環境、學會 Kotlin、用 Compose 畫出介面、給 App 接上資料庫和網路，再到測試、打包、上架——這條路上你已經走完了從零到一最難的一段。

技術的世界變化很快：框架會升級，工具會換代，AI 會接手越來越多"敲鍵盤"的活。但有一樣東西不會過時：你把一個模糊的想法，拆解成清晰的步驟，再一步步實現它的能力。工具是放大器，思路是地基。放大器可以替換，地基不能動搖。

:::inline div .quote-line
你不再只是"會玩手機的人"。你能把腦海裡的想法，變成三億安卓裝置上真實執行的 App。從今天開始，用鍵盤去創造——這就是安卓開發者的浪漫。
:::

#### 參考文獻

{class="list-decimal pl-6 mb-3 space-y-1 text-xs text-gray-500"}
1. Android Developers. (2026). Android Developer Guides and Jetpack Compose Documentation. developer.android.com.
2. Kotlin Foundation. (2026). Kotlin Language Documentation. kotlinlang.org.
3. Android Open Source Project. (2026). Android Platform Version History and API Levels.
4. Google Play. (2026). Play Console Help: Publishing and App Signing.
5. AndroidX Release Notes. (2026). Room / DataStore / Navigation / WorkManager releases.
6. Square. (2026). Retrofit Documentation. github.com/square/retrofit.
