---
id: di-er-shi-zhang-jinjie
num: 20
part: jin-jie-pian
nav: 第二十章：開發者模式與高級權限
toc: default
kind: supplement
---

### 第二十章：開發者模式與高級權限

{class="chapter-intro mb-4"}
此章乃爲彼等欲深探手機"隱藏功能"之用戶所備。開發者模式、Root權限、BL鎖……此等聽來甚極客之概念，實則離普通用戶並不遠。

#### 一、開發者模式：解鎖隱藏設置

開發者模式乃手機系統內置之一隱藏菜單，其中有諸多普通用戶用不到然開發者需之能。

##### 何以啓之：

- <strong>安卓</strong>：入設置 &gt; 關於手機 &gt; 連點"版本號"7次，直至提示"君已處於開發者模式"。
- <strong>鴻蒙</strong>：設置 &gt; 關於手機 &gt; 連點"HarmonyOS版本"7次。
- <strong>iOS</strong>：普通用戶無法啓完整之開發者模式，需付費之Apple Developer賬號。

##### 常用能一覽：

- <strong>USB調試</strong>：連接電腦進行高級操作（如刷機、數據恢復、ADB命令）之必開開關，詳見本章"ADB實用命令"小節。
- <strong>顯示觸摸操作</strong>：屏幕上顯示觸摸點（一個小圓點與隨手指），適合錄製操作教程或演示。

##### 性與流暢度相關：

- <strong>動畫速度調（窗口動畫縮放 / 過渡動畫縮放 / 動畫程序時長縮放）</strong>：這三個選項控制打開App、切換頁面時之動畫時長。默認乃1x，調至0.5x將使手機"看起來"更快（實際上程序運行速度沒變，只是動畫變快矣），調至關閉則直接無動畫跳轉。多數極客將設爲0.5x，既保留過渡感又顯快；完全關閉將使操作顯得生硬，且或掩蓋程序真實之卡頓，反而使汝誤以爲"甚流暢"。
- <strong>強制GPU渲染（Force GPU Rendering）</strong>：強制所有2D繪圖通過GPU而非CPU處理。於老舊機型或某些App優化不佳時能提升滾動流暢度，但亦將增加GPU負載與耗電。現代手機默認已大量使用GPU渲染，此開關對中高端機型影響有限，更多乃歷史遺留選項，普通用戶保持默認即可。
- <strong>顯GPU呈現模式分析（Profile GPU Rendering）</strong>：於屏幕上以柱狀圖實時顯示每幀之渲染耗時，綠色橫線代表16.6ms（60fps之幀時間閾值）。柱子超過綠線遂說明掉幀矣。這乃開發者排查App卡頓之利器，普通用戶亦可用它來對比哪個App優化得差——比如某個App滾動時柱子屢飆至紅線以上，那基本就是它的鍋。

##### 後臺與續航相關：

- <strong>後臺進程限制</strong>：可設置"標準限制""最多1個進程""最多2個進程"等。表面上觀限制後臺進程能省電，但實際上Android自帶之後臺管理已作得不錯，強行限制反而將導致App頻繁重新加載（冷啓動反而更耗電、體驗亦變差）。此選項更適合調試用，不建議普通用戶長期開啓，保持"標準限制"即可。
- <strong>不留活動</strong>：每離開一個界面遂立即銷燬它。極不推薦，將導致App頻繁白屏、重新加載，僅用以測試App之恢復邏輯。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>注意之事

{class="mt-1"}
開發者模式裏之設置或影響系統穩定，不理解之選項勿亂改。開啓USB調試後，連接電腦時當小心，勿連不信任之電腦。
:::

#### 二、OEM解鎖：開發者項裏之"刷機開關"

於開發者選項裏有一個不太起眼但甚重要之開關——"OEM解鎖"（部分品牌叫"OEM解鎖允許"或"設備解鎖"）。此開關本身未能解鎖BL鎖，但它乃一個"前置許可"：只有打開它，廠商方允許汝通過fastboot命令或品牌工具去解鎖BL。

- <strong>開關之作用</strong>：相當於向廠商聲明"吾同意放棄保修、自負風險，請允許吾解鎖BL"。若此開關乃關閉之，任何解鎖BL之命令都將爲直接拒絕。
- <strong>與BL鎖之關係</strong>：OEM解鎖乃"申請資格"，BL解鎖方乃"實際操作"。前者於手機設置裏點一下遂行，後者須去廠商官網申請解鎖碼、用電腦跑fastboot命令（如  <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing unlock</code>），二者缺一不可。
- <strong>恢復出廠設置將重置嗎</strong>：將。"OEM解鎖"開關於恢復出廠後將回至關閉狀態，但BL鎖一旦解鎖就是物理級別之狀態，未能蓋因恢復出廠而重新上鎖——須手動執行  <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing lock</code>  方能覆上鎖。
- <strong>何時候宜打開</strong>：除非汝確定要刷機或Root，否則保持關閉。它與"USB調試"乃兩個獨立開關，刷機時通常須同時打開。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>小知識：何故廠商要設置此開關

{class="mt-1"}
早期安卓沒有此開關，惡意軟件只要拿至權限遂能偷偷刷入系統。Google後來要求所有安卓廠商於開發者選項中加入"OEM解鎖"開關，作爲一道"用戶知情同意"的確認。這亦就是何故即便汝解矣BL鎖，若OEM解鎖開關爲關閉，重新刷機仍然將失敗。
:::

#### 三、BL鎖（Bootloader鎖）：刷機之首道門

Bootloader乃手機啓動時加載操作系統之程序。BL鎖即廠商爲安全而加之鎖，防用戶刷入非官方系統。

##### BL鎖之作用：

- <strong>安全保護</strong>：防惡意軟件刷入系統。
- <strong>防盜</strong>：即使手機被刷機，無原賬號密碼亦無法用。
- <strong>保修限制</strong>：解鎖BL通常意味着失官方保修。

##### 各品牌BL鎖之策：

- <strong>小米</strong>：可解鎖，需綁賬號等待期（7-30日）。
- <strong>華爲</strong>：2018年後止提供解鎖碼，基本無法官方解鎖。
- <strong>一加</strong>：可解鎖，相對寬鬆。
- <strong>OPPO/vivo</strong>：部分機型可解鎖，需申請。
- <strong>三星</strong>：可解鎖，然將觸發Knox熔斷，失Samsung Pay等功能。
- <strong>蘋果</strong>：iOS設備無傳統意義上之BL鎖概念，然有類似之安全機制。

#### 四、ADB實用命令：通過電腦控制手機

ADB 全稱 Android Debug Bridge（安卓調試橋），乃 Google 官方所出之命令行工具，使電腦經 USB 或 Wi-Fi 與安卓手機相通。其本身不需 Root，但使手機啟"USB調試"即可用。可視之為"以電腦馭手機之遙控"——刷機、裝App、傳文件、查日誌，皆賴之。

##### 何以通過 USB 連接：

1. 手機端：入開發者項 → 開"USB調試"。
2. 電腦端：自 Google 官方下載 Platform Tools（含  <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb</code>  和  <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot</code>  兩個可行文），解壓至任意目錄。
3. 用數據線連接手機與電腦，手機上將彈窗"是否允許USB調試"，勾選"始終允許"並確定。
4. 于電腦命令行（Windows 之 PowerShell 或 cmd）里執行  <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code>，若輸出類似  <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">List of devices attached / xxxxxxxx device</code>，遂說明連上矣。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>驅動與授權彈窗勿略之

{class="mt-1"}
Windows 用戶若  <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code>  顯示 "unauthorized" 或根本不列出設備，多半乃驅動沒裝好或忘矣於手機上點"允許"。三星/小米等品牌可裝各自之"USB驅動"或"手機助手"來補齊驅動；Mac 與 Linux 一般免驅。若手機彈窗爲汝手滑點掉矣，拔插一下數據線遂將重新彈出來。
:::

##### 常用 ADB 命令：

- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb install app.apk</code>：以電腦上之 APK 裝到手機（<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-r</code>  表覆蓋裝並留數據；<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code>  裝至 SD 卡）。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb uninstall com.xxx.xxx</code>：按包名卸 App。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb push 電腦路徑 /sdcard/目標路徑</code>：以電腦文件推送到手機。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb pull /sdcard/文件 電腦路徑</code>：把手機文件拉至電腦（比發給自己微信再下載快得多）。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell</code>：進入手機之 Linux Shell，可直接執行  <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls</code>、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm</code>、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">am</code>  等命令。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot bootloader</code>：重啓手機進入 Fastboot 模式（刷機之入口）。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot recovery</code>：重啓入 Recovery 模式。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages</code>：列出手機上所有已安裝應用之包名（找包名必用）。加  <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code>  只觀系統應用，加  <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-3</code>  只觀第三方應用。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 包名</code>：爲當前用戶卸預裝 App，免 Root，詳見下方實戰。

##### 免 Root 卸預裝 App 實戰：

這乃 ADB 最實用之功能之一：用  <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code>  命令可爲"當前用戶"卸載預裝 App，而不須 Root，亦不影響系統分區。爲卸載之 App 於系統裏"消失"，但實際還於系統分區裏，恢復出廠設置後將回來。

1. 先用  <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages -s</code>  列出所有系統應用，找到汝欲卸載之包名。比如小米瀏覽器乃  <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.browser</code>，華爲應用市場乃  <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.vmall.client</code>。
2. 不確定包名對應哪個 App？可於電腦上用  <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages | findstr 關鍵字</code>  搜索，或裝一個第三方 App "Package Viewer"於手機上直接查看每個 App 之包名。
3. 行卸：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 包名</code>，較如  <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 com.android.browser</code>。返  <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Success</code>  遂成功矣。
4. 欲恢復何以辦？兩種方法：① 恢復出廠設置（最徹底但麻煩）；② 重新安裝：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell cmd package install-existing 包名</code>。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>千萬勿亂刪系統核心包

{class="mt-1"}
"pm uninstall --user 0"雖是免 Root 之安全方式，但亂刪關鍵系統應用（如  <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.systemui</code>  態欄、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.phone</code>  電話、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.settings</code>  設置）將導致系統崩潰、黑屏、無法開機等嚴重問題。刪之前先 Google 一下"此包名能不可刪"，寧可少刪勿錯刪。建議一次唯刪一兩個，確認沒問題再繼續。
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>小知識：--user 0 乃何意思

{class="mt-1"}
安卓 4.2 之後支持多用戶，每個用戶有獨立之 ID（機主乃 0，附加用戶自 10 開始）。<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">--user 0</code>  表示"唯對當前機主卸載"，系統分區裏之 APK 文件依然存在，只是不賜機主顯示矣。這就是何故它不須 Root——沒動系統文件，只是改矣"用戶配置"。這亦乃它與 Root 後卸載最大之區別：Root 卸載乃真正自系統裏刪掉，所有用戶皆不再有；ADB 卸載只是"對當前用戶隱藏"。
:::

#### 五、Root權限：安卓之"超級管員"

Root權限相當於Linux中之超級用戶（對/目錄擁有完全控制權，可讀寫任意文件），乃安卓系統之最高權限。它與Windows之Administrator有本質區別：Windows出於安全考慮對管理員作了諸多限制（真正之最高權限實則乃 TrustedInstaller），即便是 Administrator 亦無法像 Linux root 那樣直接執行  <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">sudo rm -rf /*</code>。獲得Root權限後，汝可修改系統文件、卸載預裝應用、使用須Root之高級App。

##### Root之利：

- 卸無法卸之預裝應用。
- 用高級功能App（如鈦備份、綠色守護）。
- 改系統界面與功能。
- 裝第三方Recovery與自定義ROM。

##### Root之險：

- <strong>失去保修</strong>：大多數廠商不保修Root過之手機。
- <strong>安全風險</strong>：惡意App或獲Root權限，造成嚴重後果。
- <strong>系統不穩</strong>：誤操作或導致系統崩潰。
- <strong>銀行App不能用</strong>：甚多銀行與支付App檢測到Root將拒運行。
- <strong>OTA更新失敗</strong>：或無法正常收官方系統更新。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>嚴重警告

{class="mt-1"}
Root操作有一定風險，或令手機變磚（不能開機）。若汝乃新手，建議先充分了解相關知識，並確保已有完整備份。操作前當細讀教程，確認汝之機型與系統版本。
:::

#### 六、SafetyNet與Play Integrity認證：何故Root後銀行App不可用

甚多Root用戶皆遇至過此樣之崩潰瞬間：Root之後興致勃勃地裝矣一堆模塊，結果打開銀行App——"您之設備不安全，無法使用"，Google Pay亦用不了，連Netflix皆拒絕高清播放。此背後乃Google之兩套設備完整性認證機制：舊之 SafetyNet 與新之 Play Integrity API。

##### 何乃 SafetyNet / Play Integrity：

- <strong>SafetyNet Attestation（舊版，2017年起）</strong>：Google 早期推出之設備完整性檢查 API，應用通過它向 Google 服務器查詢"此臺設備為否通過 CTS 兼容性測試、為否處於未修改之官方狀態"。返回結果分爲 Basic Attestation（基礎校驗）與 Strong Attestation（強校驗，依賴硬件密鑰）。Google 已宣佈 SafetyNet 將於 2024 年後逐步停用。
- <strong>Play Integrity API（新版，2022年起）</strong>：Google 推出之替代方案，比 SafetyNet 更嚴格亦更全面。除矣設備完整性，尚包括"應用完整性"（App 為否爲篡改）與"賬號/授權完整性"（用戶賬號為否爲 Google 信任）。新 App 應遷移至 Play Integrity。
- <strong>誰來用</strong>：銀行、金融、支付類 App（如 Google Pay、各銀行之網銀、支付寶/微信支付之部分場景）、流媒體（Netflix 高清版權保護）、部分遊戲反作弊（如騰訊/網易之部分遊戲）、企業辦公 App（MDM 設備合規性檢查）。

##### Play Integrity 之三級認證結果：

- <strong>MEETS_DEVICE_INTEGRITY（設全性經由）</strong>：設備運行正版 Android 系統，Bootloader 未解鎖，無 Root，CTS 兼容性測試通過。可正常使用銀行、支付類 App。
- <strong>MEETS_BASIC_INTEGRITY（基全性經由）</strong>：設備基本可信，但或存在輕微異常。某些 App 將降級使用（如 Netflix 仍可播放但限制清晰度），某些嚴格之銀行 App 將直接拒絕。
- <strong>MEETS_STRONG_INTEGRITY（強全性經由）</strong>：最高級別，要求硬件密鑰背書（如 Google Pixel 系列之 Titan M 芯片），大多數第三方品牌機型縱未 Root 亦達不至此一級。
- <strong>無凡標籤（NO_INTEGRITY）</strong>：設備已 Root、解鎖 BL、刷矣第三方 ROM 或爲識別爲模擬器，絕大多數支付/銀行 App 將直接拒絕運行。

##### 何故 Root 後此 App 將失效：

應用通過 Play Integrity API 向 Google 服務器發起認證請求，Google 將檢查設備之多項指標——Bootloader 鎖定狀態、系統分區為否爲修改、為否存在 su 二進制文件、SELinux 為否處於寬鬆模式等。任何一項異常皆將導致返回之認證級別降低或爲空，銀行 App 一觀"設備不安全"，自然遂拒絕服務矣。

##### 今隱策：Magisk Hide / Shamiko / Zygisk：

爲了於享受 Root 便利之同時還能用銀行 App，社區開發矣一系列"隱藏 Root 狀態"之方案。核心思路皆乃：使檢測程序看到之非一個爲修改過之系統，而乃一個"看起來正常"之設備。

- <strong>Magisk</strong>：當前最主流之 Systemless Root 方案——不修改系統分區，而乃通過掛載之方式實現 Root。此樣設計之好處乃 OTA 更新失敗之幾率小、卸載比較乾淨，乃後續所有隱藏方案之基礎。但使用 Magisk 仍然須解鎖 BL 鎖。
- <strong>Magisk Hide（已停更）</strong>：Magisk 早期內置之隱藏模塊，能對指定 App 隱藏 Root。但 2021 年起已爲 Magisk 官方移除，原因乃 Google 持續升級檢測手段，雙方陷入"貓鼠遊戲"。
- <strong>Zygisk</strong>：Magisk 24.0+ 引入之新機制，類似 Riru，通過注入 Zygote 進程實現模塊加載，比直接修改系統更隱蔽。開啓 Zygisk 乃使用現代隱藏方案之前提。
- <strong>Shamiko</strong>：當前最主流之隱藏模塊，配合 Zygisk 工作，可爲指定 App（"反向白名單"模式）隱藏 Root、隱藏 Magisk 自身、僞造 Bootloader 鎖定狀態。Shamiko 通過 LSPosed 倉庫或 GitHub 分發。
- <strong>Play Integrity Fix（osm0sis）</strong>：專門針對 Google Play Integrity 檢測之 Magisk 模塊，將修改設備指紋（fingerprint）使 Google 認爲汝之設備乃某個未 Root 之官方機型。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>貓鼠遊戲永遠未能結束

{class="mt-1"}
Google 每隔一段時間遂將更新檢測規則，App 廠商亦將與進升級 Play Integrity 校驗。今天還能用之隱藏方案，明天或遂爲識別。若汝完全依賴銀行/支付 App（比如日常轉賬、掃碼付款），最穩妥之選擇仍然乃：勿 Root、勿解 BL 鎖。隱藏方案更適合"主力機不 Root + 備用機玩 Root"之玩家配置。
:::

#### 七、賜普通用戶之宜

- <strong>開發者模式</strong>：可開啓，體驗一下動畫加速、GPU 呈現分析等功能，但勿亂改其他不理解之選項。
- <strong>OEM 解鎖與 BL 鎖</strong>：若汝不打算刷機或 Root，兩個開關皆保持默認（關閉）狀態最安全。
- <strong>ADB</strong>：免 Root 之強大工具，普通人也能用——比如用  <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code>  卸載預裝 App。但刪之前一定要查清楚包名能不可刪。
- <strong>Root</strong>：普通用戶不建議 Root，風險大於收益。若確實須某些功能，可先了解有無不須 Root 之替代方案（比如用 ADB 卸載預裝、用 Shizuku 替代部分 Root 功能）。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>動手爲之：啓開發者模式並調動畫速度

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 入設置 &gt; 關於手機。
2. 連點"版本號"7次，直至提示已啓開發者模式。
3. 返設置，覓"開發者選項"（通常於設置底部或"系統"中）。
4. 覓得"窗口動畫縮放"、"過渡動畫縮放"、"動畫程序時長縮放"，皆設爲0.5x或關閉。
5. 略感手機為否變快矣。
:::
