---
id: di-si-shi-ba-zhang
num: 48
part: an-zhuo-kai-fa-pian
nav: 第四十八章：認識安卓——從操作系統到開發生態
toc: default
kind: chapter
---

### 第四十八章：認識安卓——從操作系統到開發生態

{class="chapter-intro mb-4"}
恭喜汝做出此決定——從「玩手機之人」變成「做手機應用之人」。於動手之前，吾儕先將地圖攤開：安卓從哪裡來？為何全世界之開發者皆於為它寫應用？一個App從汝之手指敲鍵盤到用戶手機上，中間皆發生了何？

#### 一、安卓之身世：從「小機器人」到「全球最大系統」

安卓（Android）之故事始於2003年——一個名叫Andy Rubin之工程師創辦了Android公司，目標甚樸素：做一套「更懂相機」之智能操作系統。後來谷歌於2005年收購了它，2007年聯合幾十家廠商成立開放手機聯盟（OHA），2008年9月，第一款安卓手機HTC Dream（G1）正式發售。

後面之故事大家皆知道了：到2026年，安卓乃全球市場份額最大之行動操作系統，活躍設備數以十億計。汝之手機、電視盒子、車載大屏、智能手錶，甚可能皆於跑安卓。此意味著何？意味著汝所寫之每一行代碼，皆有機會被世界上最多之人用到。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小訣：安卓之開源基因

{class="mt-1"}
安卓之核心代碼（AOSP，Android Open Source Project）乃開源之——任何廠商皆能拿去修改定製。故小米有MIUI（而今叫澎湃OS）、華為有鴻蒙兼容層、三星有One UI。此對開發者乃好事：汝學之乃「安卓開發」，不為「某個品牌之開發」，一套功夫，全網通喫。
:::

版本號之進化也甚有意思：從1.5之紙杯蛋糕（Cupcake）開始，每個大版本皆以甜點命名——甜甜圈、閃電泡芙、凍酸奶、薑餅……一直到2019年之安卓10才改成了純數字。到2026年8月，最新正式版乃Android 17，而開發時汝真正須關心之「最低支持版本」，主流App一般定於Android 8（API 26）到Android 10（API 29）之間——支持到幾年前之設備，汝之用戶盤子才夠大。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">版本</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">代號／年份</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">對開發者重要之事</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 8 (API 26)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Oreo · 2017</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">通知渠道、後臺限制——甚多老機型之最低線</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 10 (API 29)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2019</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分區存儲登場，文件訪問規矩大改</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 12 (API 31)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2021</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Material You動態取色，界面觀感大升級</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 13 (API 33)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2022</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">運行時通知權限，彈窗問汝「準不準發通知」</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 14-15 (API 34-35)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2023-2024</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">預測性返回、16KB頁、隱私進一步收緊</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 16-17 (API 36-37)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2025-2026</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">更快之小版本節奏、AI能力整合（如Gemini擴展）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
安卓版本簡史（截至2026年8月，開發重點關注項）

#### 二、用何語言寫：Java抑Kotlin？

安卓開發歷史上出現過兩種主流語言。Java乃「開國元老」——安卓誕生之初就用它；Kotlin乃2017年穀歌欽點之「一等公民」，2019年起官方明確「Kotlin優先」（Kotlin-first），到2026年，新項目幾乎全部用Kotlin，舊項目也大多於陸續遷移。

說句實於話：若汝乃完全零基礎，直接學Kotlin，勿回頭碰Java。原因有三：一為Kotlin代碼量比Java少30%-40%（同樣之功能，Kotlin更短更清晰）；二為它天生防「空指針」此種新手噩夢；三為所有現代教程、官方文檔、AI編程工具（還記得吾儕之AI編程書嗎？）皆於以Kotlin為準。Java只於維護老項目、讀老代碼時會遇到。

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Java風格（囉嗦版）

{class="font-mono text-xs leading-relaxed"}
public class MainActivity extends Activity {<br>&nbsp;&nbsp;@Override<br>&nbsp;&nbsp;protected void onCreate(Bundle b) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b);<br>&nbsp;&nbsp;&nbsp;&nbsp; setContentView(R.layout.activity);<br>&nbsp;&nbsp;}<br>}
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Kotlin風格（清爽版）

{class="font-mono text-xs leading-relaxed"}
class MainActivity : ComponentActivity() {<br>&nbsp;&nbsp;override fun onCreate(b: Bundle?) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b)<br>&nbsp;&nbsp;&nbsp;&nbsp;setContent { App() }<br>&nbsp;&nbsp;}<br>}
:::
:::

同樣一件事，Kotlin少了一堆花括號與樣板。第50章吾儕會正式學它，而今汝只須記住：安卓開發之「普通話」叫Kotlin。

#### 三、一個App為何以誕生之？

甚多人以為「開發App」即打開電腦狂寫代碼。實際上，一個App從想法到用戶手機上，大致要經過如此一條流水線：

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-lightbulb mr-1"></i> 想法</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center">📐 設計（界面+功能）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-keyboard mr-1"></i> 寫代碼</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hammer mr-1"></i> 編譯打包（APK/AAB）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> 測試（模擬器+真機）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-rocket mr-1"></i> 發佈（商店/安裝包）</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖1：一個安卓App從想法到上架之全流程
:::

流程裡有兩個概念汝而今就要認識：

- APK：安卓應用之安裝包格式（.apk），雙擊就能裝到手機上，就像Windows之.exe。平時自己測試、予朋友傳著玩，用它。
- AAB：Android App Bundle（.aab），上架Google Play用之「高級打包格式」。商店會根據用戶之手機型號動態裁剪，使每個人下載之包更小。自己裝不了，只能交予商店。

另外汝還會不斷聽到一個詞：SDK（Software Development Kit，軟件開發工具包）。它即安卓官方提供之一整套「開發裝備」——包括各版本之API庫、調試工具、模擬器鏡像等。汝寫代碼時調用之Activity、Button此些類，皆來自SDK。

#### 四、安卓技術棧全景：汝之「武器清單」

正式學習前，先認識一下2026年主流安卓項目之標準配置——此張清單汝而今看不懂沒關係，全書學完回來看，會豁然開朗：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">層次</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">主流選擇（2026）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">所用為何</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">語言</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin 2.x</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">寫邏輯之語言</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">界面</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jetpack Compose + Material 3</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用代碼畫界面（本書主線）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">架構</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MVVM + ViewModel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">將界面與邏輯分開，代碼不亂</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">數據存儲</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room（數據庫）＋DataStore（配置）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">將數據存進手機</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">網絡</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit＋OkHttp＋Kotlin協程</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">與服務器對話</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">構建工具</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle + Kotlin DSL</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">將代碼變成安裝包</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">開發環境</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">谷歌官方之「全家桶」IDE</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
2026年安卓主流技術棧速覽

勿被此一串英文嚇到。它等就像廚房裡之鍋碗瓢盆——汝而今只須知道「做飯要進廚房」，具體每樣工具何以用，後面章節逐個拆予汝看。而且好消息為：Android Studio創建新項目時會自動幫汝將此一整套配置好，汝只管炒菜。

#### 五、安卓vs iOS：開發者之第一堂「選邊課」

汝手裡可能正同時有安卓與蘋果設備。作為開發者，兩邊之體驗差異值得提前瞭解——不為「哪個更好」之站隊，乃「哪邊更適合汝起步」之現實賬：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">維度</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">安卓開發</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">iOS開發</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">開發電腦</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Windows／Mac／Linux皆行</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">必須Mac（Xcode獨佔）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">開發工具</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio（免費）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode（免費）＋上架年費99美元</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">上架審核</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">寬鬆，幾小時至幾天</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">嚴格，1-7天乃常態</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">裝機試玩</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">APK隨便發、隨便裝</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分發受限，測試須簽名／TestFlight</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">收入環境</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">廣告／國內渠道為主</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">App Store內購付費習慣更好</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">學習成本</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">概念較多（四大組件等）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">生態封閉但體系統一、文檔精良</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
安卓與iOS開發路徑對比（2026年8月）

說句實於話：若汝之電腦不為Mac，那此題根本不用選——安卓乃唯一選項。若汝有Mac，本書第八、九兩篇可對照著讀，編程思路為相通之，學完一邊再學另一邊會快甚多。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
動手一試：看看汝手機裡之「安卓」

{class="mt-1"}
打開手機之［設定］→［關於手機］（或「關於本機」），尋到「安卓版本」或「Android版本」那一欄——連續點它幾下，還能觸發系統之彩蛋小遊戲。記下汝之版本號，對照上面之版本表看看它屬於哪一代。汝之手機，即汝之第一個「開發測試機」。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 安卓2008年誕生，2026年乃全球市場份額最大之行動系統，活躍設備數十億
- 最新正式版Android 17；主流App最低支持Android 8-10，用戶盤子才夠大
- 新項目一律用Kotlin：代碼少30%以上、防空指針、官方欽定
- APK自己裝，AAB上商店；SDK乃官方開發裝備包
- 2026標準技術棧：Kotlin＋Compose＋MVVM＋Room＋Retrofit＋Gradle＋Android Studio
:::
