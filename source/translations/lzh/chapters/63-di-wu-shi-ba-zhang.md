---
id: di-wu-shi-ba-zhang
num: 58
part: an-zhuo-kai-fa-pian
nav: 第五十八章：速查手冊與資源
toc: default
kind: chapter
---

### 第五十八章：速查之冊與資源

{class="chapter-intro mb-4"}
此章者，可獨用之速查冊也。爾若忘某寫法或欲速決，徑翻至此。宜視之如「囊中之卡」：常用代碼之速查、常見之問、學習之資源，一頁不遺。

#### 一、常用代碼速查之卡

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">欲何為</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">關鍵代碼</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">記一可變之狀態</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">var x by remember { mutableStateOf(初值) }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">轉屏不失其狀</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">rememberSaveable { mutableStateOf(初值) }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">縱排/橫排之佈局</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Column { }</code> / <code class="inline">Row { }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">懶載之列表</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">LazyColumn { items(列表) { ... } }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">頁面之跳轉</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">navController.navigate(「路由」)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">於協程任久待之事</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">viewModelScope.launch { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">觀數據之流</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">val list by flow.collectAsState()</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">存少量配置</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">context.dataStore.edit { it[KEY] = 值 }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">存結構化之數據</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room 三件套：@Entity / @Dao / @Database</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">聯網取數據</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit 之接口加 suspend 之函</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">發通知</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">NotificationChannel + NotificationCompat.Builder</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">書日誌</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Log.d("TAG", "message")</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
安卓開發速查卡（2026 年 8 月版）

#### 二、常見問題 FAQ

Q1：吾全然不解編程，學安卓開發須時幾何？

循本書之路而行：第 1-2 週裝環境、學 Kotlin 之基；第 3-4 週學 Compose 以成界面；第 5-6 週竟記帳本之項目；第 7-8 週畢天氣之項目。兩月之間，自零至能獨作小 App。其要在日投 1-2 小時，且親敲代碼，非徒觀書也。

Q2：Java 尚須學乎？

不須也。新項目、新教程、新職缺，率以 Kotlin 為準。惟「守十年之舊項目」時方遇眾多 Java。既學 Kotlin，若工作所需，再補 Java 甚速——二者底層同一虛擬機之生態也。

Q3：模擬器乎，真機乎？

開發調試以模擬器為便（有快照、多機型），然驗收必過真機——觸感、性能、真網、傳感之器，模擬器莫能代也。力若能及，購中端真機一台以為測試之機，乃至合算之投資也。

Q4：安卓開發易覓職乎？

2026 年之市況：徒「會作界面」之初級之職，競爭甚烈；然「通 Kotlin 加善架構加有上線之作」之開發者，猶為人所爭。學習之期，爾最佳之履歷，即商店中爾自作之 App 也。

Q5：遇報錯而卡住，奈何？

黃金三步：① 以報錯之首行原文搜 StackOverflow 或搜索引擎；② 查官方文檔對應之頁；③ 猶不解，則以「期望之行加實際之象加報錯全文加相關代碼」打包致 AI 或社區而問之。問題之大半，第一步已解矣。

#### 三、推薦學習資源

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">類別</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">資源</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">所薦之由</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">developer.android.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">安卓官方之文檔，Compose 與 Kotlin 之教程皆在其中，第一權威</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin 官網 (kotlinlang.org)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">語言之官方文檔加在線演練之場</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Google Codelabs</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">手把手分步實驗之課，於新手至為友善</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">社區</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stack Overflow (android 標籤)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">報錯求救之首站</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">社區</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">掘金 / CSDN 之安卓專區</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">中文實戰之文眾多，宜辨新舊（先觀日期）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">視頻</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Google Developers 官方之頻道</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每歲開發者大會講解新技術</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">配套</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第七篇《AI編程實戰篇》（第37-47章）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">以 AI 佐安卓開發之全副心法</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
安卓開發學習資源清單（2026 年 8 月）

#### 四、Gradle 常用命令速查

平時點按鈕足矣，然命令行有時更高效（尤以配合 AI 之器或 CI 流水線之時）：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">命令</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">功用</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew assembleDebug</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">造一調試版之 APK（Windows 則去 ./）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew assembleRelease</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">造發布版（須先配簽名）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew test</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">行全部單元之測試</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew lint</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">靜態之查：得潛藏之 bug 與不規之寫法</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew clean</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">清構建之產物（「重啟大法」之編譯版）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew :app:dependencies</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">觀依賴之樹（排查版本之衝突，利器也）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Gradle 常用命令速查

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小訣：構建遇事先 clean

{class="mt-1"}
「昨日可行今日不可行」之怪事，十之六七乃構建緩存之亂也。行 ./gradlew clean 而後重構，可愈玄妙之問題大半。猶不解則再啟 Android Studio——此法宜與 File → Invalidate Caches 並用之。
:::

#### 五、結語：自第一個 App 至第 N 個 App

回顧之，爾自「不知 Activity 為何物」，至裝成環境、學會 Kotlin、以 Compose 繪出界面、為 App 接上數據庫與網絡，乃至測試、打包、上架——此路之上，爾已竟自零至一至難之一段矣。

技術之世變甚速：框架必升，工具必代，AI 將接「敲鍵盤」之事日多。然有一物不過時：爾以一模糊之念，拆為清明之步，而後步步成之之能也。器者放大之器也，思者地基也。放大之器可換，地基不可搖。

:::inline div .quote-line
汝不復徒為"玩手機之人"。汝能以胸中之念，化為三億安卓之器上實運行之 App。自今日始，以鍵盤創物——此安卓開發者之浪漫也。
:::

#### 參考文獻

{class="list-decimal pl-6 mb-3 space-y-1 text-xs text-gray-500"}
1. Android Developers. (2026). Android Developer Guides and Jetpack Compose Documentation. developer.android.com.
2. Kotlin Foundation. (2026). Kotlin Language Documentation. kotlinlang.org.
3. Android Open Source Project. (2026). Android Platform Version History and API Levels.
4. Google Play. (2026). Play Console Help: Publishing and App Signing.
5. AndroidX Release Notes. (2026). Room / DataStore / Navigation / WorkManager releases.
6. Square. (2026). Retrofit Documentation. github.com/square/retrofit.
