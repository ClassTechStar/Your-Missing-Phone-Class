---
id: di-si-shi-ba-zhang
num: 48
part: an-zhuo-kai-fa-pian
nav: 第四十八章：認識安卓——從作業系統到開發生態
toc: default
kind: chapter
---

### 第四十八章：認識安卓——從作業系統到開發生態

{class="chapter-intro mb-4"}
恭喜你做出這個決定——從"玩手機的人"變成"做手機應用的人"。在動手之前，咱們先把地圖攤開：安卓從哪裡來？為什麼全世界的開發者都在給它寫應用？一個 App 從你的手指敲鍵盤到使用者手機上，中間都發生了什麼？

#### 一、安卓的身世：從"小機器人"到"全球最大系統"

安卓（Android）的故事始於 2003 年——一個叫 Andy Rubin 的工程師創辦了 Android 公司，目標很樸素：做一套"更懂相機"的智慧作業系統。後來谷歌在 2005 年收購了它，2007 年聯合幾十家廠商成立開放手機聯盟（OHA），2008 年 9 月，第一款安卓手機 HTC Dream（G1）正式發售。

後面的故事大家都知道了：到 2026 年，安卓是全球市場份額最大的移動作業系統，活躍裝置數以十億計。你的手機、電視盒子、車載大屏、智慧手錶，很可能都在跑安卓。這意味著什麼？意味著你寫的每一行程式碼，都有機會被世界上最多的人用到。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：安卓的開源基因

{class="mt-1"}
安卓的核心程式碼（AOSP，Android Open Source Project）是開源的——任何廠商都能拿去修改定製。所以小米有 MIUI（現在叫澎湃 OS）、華為有鴻蒙相容層、三星有 One UI。這對開發者是好事：你學的是"安卓開發"，不是"某個品牌的開發"，一套功夫，全網通吃。
:::

版本號的進化也很有意思：從 1.5 的紙杯蛋糕（Cupcake）開始，每個大版本都以甜點命名——甜甜圈、閃電泡芙、凍酸奶、薑餅……一直到 2019 年的安卓 10 才改成了純數字。到 2026 年 8 月，最新正式版是 Android 17，而開發時你真正需要關心的"最低支援版本"，主流 App 一般定在 Android 8（API 26）到 Android 10（API 29）之間——支援到幾年前的裝置，你的使用者盤子才夠大。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">版本</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">代號/年份</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">對開發者重要的事</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 8 (API 26)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Oreo · 2017</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">通知管道、後臺限制——很多老機型的最低線</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 10 (API 29)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2019</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分割區儲存登場，檔案訪問規矩大改</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 12 (API 31)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2021</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Material You 動態取色，介面觀感大升級</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 13 (API 33)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2022</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">執行時通知權限，跳出視窗問你"準不準發通知"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 14-15 (API 34-35)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2023-2024</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">預測性返回、16KB 頁、隱私進一步收緊</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 16-17 (API 36-37)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2025-2026</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">更快的小版本節奏、AI 能力整合（如 Gemini 擴充套件）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
安卓版本簡史（截至 2026 年 8 月，開發重點關注項）

#### 二、用什麼語言寫：Java 還是 Kotlin？

安卓開發歷史上出現過兩種主流語言。Java 是"開國元老"——安卓誕生之初就用它；Kotlin 是 2017 年穀歌欽點的"一等公民"，2019 年起官方明確"Kotlin 優先"（Kotlin-first），到 2026 年，新專案幾乎全部用 Kotlin，舊專案也大多在陸續遷移。

說句實在話：如果你是完全零基礎，直接學 Kotlin，別回頭碰 Java。原因有三：一是 Kotlin 程式碼量比 Java 少 30%-40%（同樣的功能，Kotlin 更短更清晰）；二是它天生防"空指標"這種新手噩夢；三是所有現代教學、官方檔案、AI 程式設計工具（還記得咱們的 AI 程式設計書嗎？）都在以 Kotlin 為準。Java 只在維護老專案、讀老程式碼時會遇到。

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Java 風格（囉嗦版）

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

同樣一件事，Kotlin 少了一堆花括號和樣板。第 50 章咱們會正式學它，現在你只需要記住：安卓開發的"普通話"叫 Kotlin。

#### 三、一個 App 是怎麼誕生的？

很多人以為"開發 App"就是開啟電腦狂寫程式碼。實際上，一個 App 從想法到使用者手機上，大致要經過這樣一條流水線：

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-lightbulb mr-1"></i> 想法</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center">📐 設計（介面+功能）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-keyboard mr-1"></i> 寫程式碼</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hammer mr-1"></i> 編譯打包（APK/AAB）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> 測試（模擬器+真機）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-rocket mr-1"></i> 釋出（商店/安裝包）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 1：一個安卓 App 從想法到上架的全流程
:::

流程裡有兩個概念你現在就要認識：

- APK：安卓應用的安裝包格式（.apk），連點兩下就能裝到手機上，就像 Windows 的 .exe。平時自己測試、給朋友傳著玩，用它。
- AAB：Android App Bundle（.aab），上架 Google Play 用的"進階打包格式"。商店會根據使用者的手機型號動態裁剪，讓每個人下載的包更小。自己裝不了，只能交給商店。

另外你還會不斷聽到一個詞：SDK（Software Development Kit，軟體開發工具包）。它就是安卓官方提供的一整套"開發裝備"——包括各版本的 API 庫、除錯工具、模擬器映象等。你寫程式碼時呼叫的 Activity、Button 這些類，都來自 SDK。

#### 四、安卓技術棧全景：你的"武器清單"

正式學習前，先認識一下 2026 年主流安卓專案的標準配置——這張清單你現在看不懂沒關係，全書學完回來看，會豁然開朗：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">層次</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">主流選擇（2026）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">幹什麼用的</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">語言</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin 2.x</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">寫邏輯的語言</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">介面</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jetpack Compose + Material 3</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用程式碼畫介面（本書主線）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">架構</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MVVM + ViewModel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把介面和邏輯分開，程式碼不亂</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">資料儲存</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room（資料庫）+ DataStore（配置）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把資料存進手機</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">網路</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit + OkHttp + Kotlin 協程</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">和伺服器對話</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">構建工具</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle + Kotlin DSL</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把程式碼變成安裝包</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">開發環境</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">谷歌官方的"全家桶"IDE</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
2026 年安卓主流技術棧速覽

別被這一串英文嚇到。它們就像廚房裡的鍋碗瓢盆——你現在只需要知道"做飯要進廚房"，具體每樣工具怎麼用，後面章節逐個拆給你看。而且好訊息是：Android Studio 建立新專案時會自動幫你把這一整套配置好，你只管炒菜。

#### 五、安卓 vs iOS：開發者的第一堂"選邊課"

你手裡可能正同時有安卓和蘋果裝置。作為開發者，兩邊的體驗差異值得提前瞭解——不是"哪個更好"的站隊，而是"哪邊更適合你起步"的現實帳：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">維度</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">安卓開發</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">iOS 開發</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">開發電腦</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Windows / Mac / Linux 都行</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">必須 Mac（Xcode 獨佔）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">開發工具</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio（免費）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode（免費）+ 上架年費 99 美元</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">上架稽核</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">寬鬆，幾小時~幾天</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">嚴格，1-7 天是常態</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">裝機試玩</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">APK 隨便發、隨便裝</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分發受限，測試需簽名/TestFlight</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">收入環境</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">廣告/國內管道為主</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">App Store 內購付費習慣更好</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">學習成本</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">概念較多（四大元件等）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">生態封閉但體系統一、檔案精良</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
安卓與 iOS 開發路徑對比（2026 年 8 月）

說句實在話：如果你的電腦不是 Mac，那這道題根本不用選——安卓是唯一選項。如果你有 Mac，本書第八、九兩篇可以對照著讀，程式設計思路是相通的，學完一邊再學另一邊會快很多。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：看看你手機裡的"安卓"

{class="mt-1"}
開啟手機的 [設定] → [關於手機]（或"關於本機"），找到"安卓版本"或"Android 版本"那一欄——連續點它幾下，還能觸發系統的彩蛋小遊戲。記下你的版本號，對照上面的版本表看看它屬於哪一代。你的手機，就是你的第一個"開發測試機"。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 安卓 2008 年誕生，2026 年是全球市場份額最大的移動系統，活躍裝置數十億
- 最新正式版 Android 17；主流 App 最低支援 Android 8-10，使用者盤子才夠大
- 新專案一律用 Kotlin：程式碼少 30%+、防空指標、官方欽定
- APK 自己裝，AAB 上商店；SDK 是官方開發裝備包
- 2026 標準技術棧：Kotlin + Compose + MVVM + Room + Retrofit + Gradle + Android Studio
:::
