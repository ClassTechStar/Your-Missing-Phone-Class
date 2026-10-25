---
id: di-si-shi-jiu-zhang
num: 49
part: an-zhuo-kai-fa-pian
nav: 第四十九章：搭建開發環境——Android Studio與第一個項目
toc: default
kind: chapter
---

### 第四十九章：搭建開發環境——Android Studio與第一個項目

{class="chapter-intro mb-4"}
工欲善其事，必先利其器。此章吾儕將「廚房」搭好：裝好Android Studio、跑通模擬器、創建人生第一個安卓項目，再將工程結構拆開看個明白。裝好環境之後，汝會第一次看到自己寫之代碼變成一個能點之按鈕——此一瞬間，甚多人會記一輩子。

#### 一、安裝Android Studio

Android Studio乃谷歌官方之集成開發環境（IDE），免費，功能全家桶：寫代碼、看界面預覽、調試、打包全於其中。安裝四步：

1. 打開官網developer.android.com/studio，下載最新穩定版（2026年8月乃Narwhal之後之版本，Windows/Mac/Linux皆有）；
2. 運行安裝包，一路「下一步」——安裝嚮導會自動帶上Android SDK與模擬器組件；
3. 首次啟動時按提示下載SDK組件（默認勾選就好，可能須幾分鐘與幾個GB之空間）；
4. 完成後汝會看到歡迎頁——恭喜，「廚房」搭好了。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：硬件要求心裡有數

{class="mt-1"}
Android Studio乃一個「喫記憶體」之傢夥：建議16GB記憶體起步（8GB也能跑，但模擬器一開則比較卡）、磁盤預留20GB以上、CPU支持虛擬化（BIOS裡開啟VT-x/AMD-V）。若電腦確實老舊，可用「真機調試」代替模擬器（本章第四節會講），體驗反而更流暢。
:::

#### 二、創建汝之第一個項目

於歡迎頁點New Project，選Empty Activity模板（最乾淨之新手模板），然後填三樣東西：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">配置項</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">填何</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">說明</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">My First App</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">應用名字，顯示於手機桌面上</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Package name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example.myfirstapp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全球唯一標識，習慣乃「域名反寫」，先按默認</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minimum SDK</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API 26（Android 8.0）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最低支持版本，覆蓋95%以上設備</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
創建項目要填之三件事

點Finish後，Android Studio會用Gradle自動下載依賴、構建項目（第一次要等幾分鐘，之後每次會快甚多）。構建完成後，汝就有了一個能跑之App——雖然它還只會顯示一行「Hello Android!」。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小訣：包名之門道

{class="mt-1"}
包名（package name）就像App之「身份證號」，全球不能重複，上架後就不能改了。個人練習用com.example.xxx就行；正式產品要換成汝自己之域名反寫（譬如com.汝之名.應用名）。勿用com.example上架——商店會拒收。
:::

#### 三、跑起來：模擬器與真機

代碼寫好了，得尋個「手機」來跑。汝有兩個選擇：

##### 1. 模擬器（Emulator）

模擬器者，於電腦中虛擬安卓手機一部也。啟 Android Studio，開 Device Manager → Create Device，擇一機（宜 Pixel 系列）→ 選系統影像（取帶 Google APIs 者）→ 下載 → 啟動。繼點工具欄綠色三角 Run，俄而數秒，「手機」之屏遂現汝之 App。

##### 2. 真機調試（尤所薦）

真機者，至真之試煉之境也——滑動之手感、真網、真感應之器，模擬器皆莫能及。安卓真機調試甚簡：

1. 於手機啟［設定］→［關於手機］，連點「版本號」七次，則「開發者選項」啟矣；
2. 於［開發者選項］中啟 USB 調試；
3. 以數據線連電腦，手機彈窗，擇「允許 USB 調試」；
4. 返 Android Studio，工具欄設備下拉之列遂現汝機，點 Run。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
避坑之警：USB 調試勿恆開

{class="mt-1"}
USB 調試者，猶為電腦開「後門」也。凡公共之所充電、接不可信之電腦，務閉 USB 調試，以防他人由之竊讀汝之數據。平居開發，用畢即閉，習以為常。
:::

#### 四、工程結構拆解：諸文件何所司

初啟項目，左側文件之樹或令汝目眩。勿慌，日常開發，汝百分之九十惟與下列數者相交接：

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="300" viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="300" fill="#fafafa" rx="8"/>
      <text x="20" y="30" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ 項目根目錄</text>
      <rect x="30" y="45" width="540" height="230" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <text x="45" y="70" font-size="11" fill="#4f46e5" font-weight="bold">app/ ← 汝寫代碼之地方</text>
      <rect x="60" y="82" width="240" height="178" fill="#eef2ff" rx="5"/>
      <text x="70" y="102" font-size="10" fill="#1e1b4b" font-weight="bold">src/main/</text>
      <text x="80" y="120" font-size="10" fill="#374151">├ java/…/MainActivity.kt  ← 邏輯代碼</text>
      <text x="80" y="138" font-size="10" fill="#374151">├ res/  ← 資源（圖片、文字、顏色）</text>
      <text x="80" y="156" font-size="10" fill="#374151">└ AndroidManifest.xml  ← 應用"戶口本"</text>
      <text x="70" y="180" font-size="10" fill="#1e1b4b" font-weight="bold">build.gradle.kts</text>
      <text x="80" y="198" font-size="10" fill="#6b7280">聲明依賴之庫（SDK 版本、Compose 等）</text>
      <text x="70" y="222" font-size="10" fill="#1e1b4b" font-weight="bold">src/androidTest/ 與 test/</text>
      <text x="80" y="240" font-size="10" fill="#6b7280">自動化測試代碼（第 56 章用）</text>
      <rect x="320" y="82" width="230" height="178" fill="#f0fdf4" rx="5"/>
      <text x="330" y="102" font-size="10" fill="#065f46" font-weight="bold">根目錄之其他文件</text>
      <text x="340" y="122" font-size="10" fill="#374151">gradle/ + gradlew.bat  ← 構建腳本</text>
      <text x="340" y="142" font-size="10" fill="#374151">settings.gradle.kts  ← 項目設置</text>
      <text x="340" y="162" font-size="10" fill="#6b7280">（新手之口訣：只碰 app/ 目錄，</text>
      <text x="340" y="180" font-size="10" fill="#6b7280">其餘之先當"黑盒"，別亂動）</text>
      <text x="340" y="208" font-size="10" fill="#9ca3af">.gitignore  ← 版本控制忽略清單</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 2：新手必曉之工程結構（口訣：惟觸 app/ 目錄）
:::

- MainActivity.kt：App 之「大門」也。用戶點圖標而啟，首被喚醒者即之。今模板中，其司顯「Hello Android!」之職。
- AndroidManifest.xml：App 之「戶口簿」也——聲明此 App 何名、何圖標、有何頁面、需何權限（相機、定位之屬）。
- res/ 目錄：資源之倉也，藏圖片、圖標、字符串、顏色。文字置於資源之文件而不硬寫於代碼，乃安卓開發之善習（易語言、易主題皆便）。
- build.gradle.kts：構建之方也——聲明最低支持之版本、所倚之庫（如 Compose）。

#### 五、小試牛刀：易「Hello」為汝名

啟 MainActivity.kt，則見 Compose 模板所生之代碼。得 Text("Hello Android!") 一行，易引號中之字為汝名，如 Text("汝好，張三！此吾之首個App")，繼按 Ctrl+R（Mac 則 Cmd+R）復行。數秒之後，模擬器遂顯汝名矣。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · MainActivity.kt（改此一行）</span><span class="dots">···</span>
:::

```
setContent {
    MyFirstAppTheme {
        Surface(modifier = Modifier.fillMaxSize()) {
            // ▼ 改此為汝之文字
            Text("汝好，張三！此乃吾之首App")
        }
    }
}
```
:::

賀矣，汝已竟一全環：「改代碼 → 編譯 → 安裝 → 運行」。此環者，異日日日開發之常也。乘熱打鐵，試更易他者：增字之號、易其色——次章將明此諸「魔法」所自來。

#### 六、常見報錯急救：新手前兩週之「急診室」

環境初建、首次構建之際，汝十有八九將遇下列三種報錯。勿慌，皆有解藥：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">報錯之象</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">常見之因</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">解藥</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle sync failed / 依賴下載遲緩</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">網絡通倉庫不暢</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">為 Gradle 配國內鏡像倉庫（阿里雲/騰訊雲 maven 鏡像），網上搜「gradle 國內鏡像」依而改之</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SDK 組件缺失</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">安裝時跳過 SDK 之下載</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Settings → SDK Manager 補裝所缺之平臺與工具</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">模擬器啟動敗 / 黑屏</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">虛擬化未啟、影像損壞</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BIOS 啟 VT-x/AMD-V；刪模擬器而重建；或逕用真機調試</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
新手環境報錯急救之表

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小識：搜報錯之法

{class="mt-1"}
報錯之首行最有值——原樣抄入搜索引擎，加以「android studio」之關鍵詞。勿搜「吾環境裝不上奈何」之泛問，當搜「Gradle sync failed: Could not resolve com.android.tools.build」之具體錯。問也精，答方精。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：竟汝「開發儀式感」之單

{class="mt-1"}
① 裝 Android Studio 且通模擬器；② 以真機行己之 App 一遭，截圖以存；③ 易 Hello 之文為汝名；④ 壓縮項目而存檔。四步既畢，即可於朋友圈宣曰：吾亦安卓開發者矣（截圖為證）。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- Android Studio = 官家免費之 IDE；宜 16GB 記憶體 + 20GB 磁盤 + 啟虛擬化
- 新建項目三要素：名、包名（舉世唯一，com.example 勿上架）、最低 SDK（自 API 26 始）
- 運行之道二：模擬器（電腦中虛擬之機）與真機（啟 USB 調試，用畢記閉）
- 工程口訣：惟觸 app/ 目錄——MainActivity.kt 為大門，Manifest 為戶口簿，res/ 為資源之倉
- 開發日常 = 改代碼 → Run → 觀其效，循環往復
:::
