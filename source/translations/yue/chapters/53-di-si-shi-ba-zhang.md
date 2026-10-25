---
id: di-si-shi-ba-zhang
num: 48
part: an-zhuo-kai-fa-pian
nav: 第四十八章：認識安卓——由操作系統到開發生態
toc: default
kind: chapter
---

### 第四十八章：認識安卓——由操作系統到開發生態

{class="chapter-intro mb-4"}
恭喜你做出呢個決定——由「玩手機嘅人」變成「做手機應用嘅人」。喺動手之前，我哋先攤開張地圖：安卓由邊度嚟？點解全世界嘅開發者都幫佢寫應用？一個 App 由你手指敲鍵盤到用戶手機上面，中間發生咗乜嘢事？

#### 一、安卓嘅身世：由「小機械人」到「全球最大系統」

安卓（Android）嘅故事始於 2003 年——一個叫 Andy Rubin 嘅工程師創辦咗 Android 公司，目標好樸素：做一套「更識用相機」嘅智能操作系統。後來谷歌喺 2005 年收購咗佢，2007 年聯同幾十間廠商成立開放手機聯盟（OHA），2008 年 9 月，第一款安卓手機 HTC Dream（G1）正式發售。

後面嘅故事大家都知喇：到 2026 年，安卓係全球市場份額最大嘅流動操作系統，活躍設備數以十億計。你嘅手機、電視盒、車載大螢幕、智能手錶，好可能都喺度行緊安卓。呢個意味住乜嘢？意味住你寫嘅每一行代碼，都有機會畀世界上最多人用到。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：安卓嘅開源基因

{class="mt-1"}
安卓嘅核心代碼（AOSP，Android Open Source Project）係開源嘅——任何廠商都可以攞去修改定製。所以小米有 MIUI（而家叫澎湃 OS）、華為有鴻蒙兼容層、三星有 One UI。呢樣嘢對開發者係好事：你學嘅係「安卓開發」，唔係「某個品牌嘅開發」，一套功夫，通喫全網。
:::

版本號嘅進化都好有趣：由 1.5 嘅紙杯蛋糕（Cupcake）開始，每個大版本都以甜品命名——甜甜圈、閃電泡芙、凍乳酪、薑餅……一直到 2019 年嘅安卓 10 先改成純數字。到 2026 年 8 月，最新正式版係 Android 17，而開發時你真正需要關心嘅「最低支援版本」，主流 App 一般定喺 Android 8（API 26）到 Android 10（API 29）之間——支援到幾年前嘅設備，你嘅用戶羣先夠大。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">版本</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">代號/年份</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">對開發者重要嘅事</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 8 (API 26)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Oreo · 2017</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">通知渠道、後臺限制——好多舊機型嘅最低線</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 10 (API 29)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2019</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分區儲存登場，檔案存取規矩大改</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 12 (API 31)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2021</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Material You 動態取色，介面觀感大升級</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 13 (API 33)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2022</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">執行時通知權限，彈窗問你「準唔準發通知」</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 14-15 (API 34-35)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2023-2024</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">預測性返回、16KB 頁、私隱進一步收緊</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 16-17 (API 36-37)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2025-2026</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">更快嘅小版本節奏、AI 能力整合（例如 Gemini 擴展）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
安卓版本簡史（截至 2026 年 8 月，開發重點關注項）

#### 二、用乜嘢語言寫：Java 定 Kotlin？

安卓開發歷史上出現過兩種主流語言。Java 係「開國元老」——安卓誕生之初就用佢；Kotlin 係 2017 年穀歌欽點嘅「一等公民」，2019 年起官方明確「Kotlin 優先」（Kotlin-first），到 2026 年，新項目幾乎全部用 Kotlin，舊項目都大部分陸續遷移緊。

講句實喺話：如果你係完全零基礎，直接學 Kotlin，唔好返轉頭掂 Java。原因有三：一係 Kotlin 代碼量比 Java 少 30%-40%（同樣嘅功能，Kotlin 更短更清晰）；二係佢天生防到「空指標」呢種新手噩夢；三係所有現代教程、官方文檔、AI 編程工具（仲記唔記得我哋本 AI 編程書呀？）都以 Kotlin 為準。Java 只係喺維護舊項目、睇舊代碼嗰陣先會遇到。

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Java 風格（長氣版）

{class="font-mono text-xs leading-relaxed"}
public class MainActivity extends Activity {<br>&nbsp;&nbsp;@Override<br>&nbsp;&nbsp;protected void onCreate(Bundle b) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b);<br>&nbsp;&nbsp;&nbsp;&nbsp; setContentView(R.layout.activity);<br>&nbsp;&nbsp;}<br>}
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Kotlin 風格（清爽版）

{class="font-mono text-xs leading-relaxed"}
class MainActivity : ComponentActivity() {<br>&nbsp;&nbsp;override fun onCreate(b: Bundle?) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b)<br>&nbsp;&nbsp;&nbsp;&nbsp;setContent { App() }<br>&nbsp;&nbsp;}<br>}
:::
:::

同樣一件事，Kotlin 少咗一堆花括號同樣板。第 50 章我哋會正式學佢，而家你只需要記住：安卓開發嘅「普通話」叫 Kotlin。

#### 三、一個 App 係點樣誕生嘅？

好多人以為「開發 App」就係打開電腦狂寫代碼。實際上，一個 App 由諗法到用戶手機上面，大致要經過咁一條流水線：

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-lightbulb mr-1"></i> 想法</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center">📐 設計（界面+功能）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-keyboard mr-1"></i> 寫代碼</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hammer mr-1"></i> 編譯打包（APK/AAB）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> 測試（模擬器+真機）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-rocket mr-1"></i> 發佈（商店/安裝包）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 1：一個安卓 App 由諗法到上架嘅全流程
:::

流程入面有兩個概念你而家就要認識：

- APK：安卓應用嘅安裝包格式（.apk），雙擊就可以裝到手機度，就好似 Windows 嘅 .exe 咁。平時自己測試、傳畀朋友玩下，就用佢。
- AAB：Android App Bundle（.aab），上架 Google Play 用嘅「高級打包格式」。商店會根據用戶嘅手機型號動態裁剪，令每個人下載嘅包更細。自己裝唔到，只可以交畀商店。

另外你仲會不斷聽到一個詞：SDK（Software Development Kit，軟件開發工具包）。佢就係安卓官方提供嘅一整套「開發裝備」——包括各版本嘅 API 庫、除錯工具、模擬器映像等。你寫代碼時呼叫嘅 Activity、Button 呢啲類，都係嚟自 SDK。

#### 四、安卓技術棧全景：你嘅「武器清單」

正式學習之前，先認識嚇 2026 年主流安卓項目嘅標準配置——呢張清單你而家睇唔明唔緊要，全書學完返轉頭睇，就會豁然開朗：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">層次</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">主流選擇（2026）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">做乜嘢用嘅</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">語言</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin 2.x</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">寫邏輯嘅語言</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">介面</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jetpack Compose + Material 3</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用代碼畫介面（本書主線）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">架構</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MVVM + ViewModel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">將介面同邏輯分開，代碼唔會亂</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">數據儲存</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room（數據庫）+ DataStore（配置）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">將數據存入手機</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">網絡</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit + OkHttp + Kotlin 協程</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">同伺服器對話</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">構建工具</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle + Kotlin DSL</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">將代碼變成安裝包</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">開發環境</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">谷歌官方嘅「全家桶」IDE</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
2026 年安卓主流技術棧速覽

唔好畀呢串英文字嚇親。佢哋就好似廚房入面嘅鑊鑊罌罌噉——你而家只需要知道「煮飯要入廚房」，至於每樣工具點樣用，後面章節會逐個拆開畀你睇。而且有個好消息：Android Studio 開新項目嗰陣會自動幫你將成套嘢配置好，你淨係負責炒菜就得。

#### 五、安卓 vs iOS：開發者第一堂「揀邊邊」課

你手上可能同時有安卓同蘋果嘅設備。作為開發者，兩邊嘅體驗差異值得提前瞭解——唔係「邊個更好」嘅站隊，而係「邊一邊更加適合你起步」嘅現實賬：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">維度</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">安卓開發</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">iOS 開發</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">開發電腦</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Windows / Mac / Linux 都得</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一定要 Mac（Xcode 獨佔）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">開發工具</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio（免費）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode（免費）+ 上架年費 99 美元</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">上架審核</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">寬鬆，幾個鐘至幾日</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">嚴格，1 至 7 日係常態</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">裝機試玩</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">APK 隨便發、隨便裝</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分發受限，測試要簽名／TestFlight</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">收入環境</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">以廣告／國內渠道為主</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">App Store 內購付費習慣更好</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">學習成本</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">概念比較多（四大組件等等）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">生態封閉但體系統一、文檔精良</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
安卓同 iOS 開發路徑對比（2026 年 8 月）

講句實喺話：如果你部電腦唔係 Mac，呢條題根本唔使揀——安卓係唯一選項。如果你有 Mac，本書第八、九兩篇可以對照住讀，編程思路係相通嘅，學完一邊再學另一邊會快好多。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
嚟動手：睇嚇你手機入面嘅「安卓」

{class="mt-1"}
打開手機嘅 [設定] → [關於手機]（或者「關於本機」），搵到「安卓版本」或者「Android 版本」嗰一欄——連續篤佢幾下，仲可以觸發系統嘅彩蛋小遊戲。記低你嘅版本號，對照上面嘅版本表睇嚇佢屬於邊一代。你部手機，就係你嘅第一部「開發測試機」。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 安卓 2008 年誕生，2026 年係全球市場份額最大嘅流動系統，活躍設備有幾十億部
- 最新正式版係 Android 17；主流 App 最低支援 Android 8 至 10，用戶盤子先至夠大
- 新項目一律用 Kotlin：程式碼少 30% 以上、防空指標、官方欽定
- APK 自己裝，AAB 上商店；SDK 係官方開發裝備包
- 2026 標準技術棧：Kotlin + Compose + MVVM + Room + Retrofit + Gradle + Android Studio
:::
