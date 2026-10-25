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
呢一章係畀嗰啲想要深入探索手機「隱藏功能」嘅用戶準備嘅。開發者模式、Root權限、BL鎖……呢啲聽落好極客嘅概念，其實離普通用戶並唔遙遠。

#### 一、開發者模式：解鎖隱藏設定

開發者模式係手機系統內置嘅一個隱藏選單，入面有好多普通用戶用唔到但開發者需要嘅功能。

##### 點樣開啟：

- <strong>安卓</strong>：進入設定 > 關於手機 > 連續撳「版本號」7次，直到提示「您已處於開發者模式」。
- <strong>鴻蒙</strong>：設定 > 關於手機 > 連續撳「HarmonyOS版本」7次。
- <strong>iOS</strong>：普通用戶無法開啟完整嘅開發者模式，需要付費嘅Apple Developer帳號。

##### 常用功能一覽：

- <strong>USB調試</strong>：連接電腦進行高級操作（如刷機、數據恢復、ADB命令）嘅必開開關，詳見本章「ADB實用命令」小節。
- <strong>顯示觸摸操作</strong>：螢幕上顯示觸控點（一個細圓點跟隨手指），適合錄製操作教程或演示。

##### 性能與流暢度相關：

- <strong>動畫速度調節（視窗動畫縮放 / 過渡動畫縮放 / 動畫程式時長縮放）</strong>：呢三個選項控制打開App、切換頁面時嘅動畫時長。預設係1x，調到0.5x會等手機「睇落」更快（實際上程式運行速度冇變，淨係動畫變快咗），調到關閉就直接無動畫跳轉。多數極客會設為0.5x，既保留過渡感又顯快；完全關閉會等操作顯得生硬，而且可能掩蓋程式真實嘅卡頓，反而等你誤以為「好流暢」。
- <strong>強制GPU渲染（Force GPU Rendering）</strong>：強制所有2D繪圖通過GPU而唔係CPU處理。喺舊機型或某些App優化唔佳時可以提升滾動流暢度，但都會增加GPU負載同耗電。現代手機預設已大量使用GPU渲染，呢個開關對中高端機型影響有限，更多係歷史遺留選項，普通用戶保持預設即可。
- <strong>顯示GPU呈現模式分析（Profile GPU Rendering）</strong>：喺螢幕上以柱狀圖實時顯示每幀嘅渲染耗時，綠色橫線代表16.6ms（60fps嘅幀時間閾值）。柱超過綠線就說明掉幀喇。呢個係開發者排查App卡頓嘅利器，普通用戶都可以用佢嚟對比邊個App優化得差——比如某個App滾動時柱成日飆到紅線以上，咁基本就係佢嘅鍋。

##### 後台與續航相關：

- <strong>後台進程限制</strong>：可以設定「標準限制」「最多1個進程」「最多2個進程」等。表面睇限制後臺進程可以省電，但實際上Android自帶嘅後臺管理已經做得唔錯，強行限制反而會導致App頻繁重新載入（冷啟動反而更耗電、體驗都變差）。呢個選項更適合調試用，唔建議普通用戶長期開啟，保持「標準限制」即可。
- <strong>唔保留活動</strong>：每離開一個介面就立即銷毀佢。極不推薦，會導致App頻繁白屏、重新載入，僅用於測試App嘅恢復邏輯。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>注意事項

{class="mt-1"}
開發者模式入面嘅設定可能會影響系統穩定性，唔明嘅選項唔好亂改。開啟USB調試後，連接電腦嗰陣要小心，唔好連接唔信任嘅電腦。
:::

#### 二、OEM解鎖：開發者選項入面嘅「刷機開關」

喺開發者選項入面有一個唔太起眼但好重要嘅開關——「OEM解鎖」（部分品牌叫「OEM解鎖允許」或「設備解鎖」）。呢個開關本身唔會解鎖BL鎖，但佢係一個「前置許可」：淨係打開佢，廠商先允許你通過fastboot命令或品牌工具去解鎖BL。

- <strong>開關嘅作用</strong>：相當於向廠商聲明「我同意放棄保修、自負風險，請允許我解鎖BL」。如果呢個開關係關閉嘅，任何解鎖BL嘅命令都會被直接拒絕。
- <strong>同BL鎖嘅關係</strong>：OEM解鎖係「申請資格」，BL解鎖先係「實際操作」。前者喺手機設定入面撳一下就得，後者需要去廠商官網申請解鎖碼、用電腦跑fastboot命令（如 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing unlock</code>），兩者缺一不可。
- <strong>恢復出廠設定會重置嗎</strong>：會。「OEM解鎖」開關喺恢復出廠後會返到關閉狀態，但BL鎖一旦解鎖就係物理級別嘅狀態，唔會因為恢復出廠而重新上鎖——需要手動執行 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing lock</code> 先可以重新上鎖。
- <strong>乜嘢時候應該打開</strong>：除非你確定要刷機或Root，否則保持關閉。佢同「USB調試」係兩個獨立開關，刷機時通常需要同時打開。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>小知識：點解廠商要設定呢個開關

{class="mt-1"}
早期安卓冇呢個開關，惡意軟件淨係攞到權限就可以偷偷刷入系統。Google後來要求所有安卓廠商喺開發者選項中加入「OEM解鎖」開關，作為一道「用戶知情同意」嘅確認。呢個都係點解即便你解咗BL鎖，如果OEM解鎖開關被關閉，重新刷機仍然會失敗。
:::

#### 三、BL鎖（Bootloader鎖）：刷機嘅第一道門

Bootloader係手機啟動時載入作業系統嘅程式。BL鎖就係廠商為咗安全而加嘅鎖，防止用戶刷入非官方系統。

##### BL鎖嘅作用：

- <strong>安全保護</strong>：防止惡意軟件刷入系統。
- <strong>防盜</strong>：即使手機被刷機，冇原帳號密碼都無法使用。
- <strong>保修限制</strong>：解鎖BL通常意味住失去官方保修。

##### 各品牌BL鎖政策：

- <strong>小米</strong>：可以解鎖，需要綁定帳號等待期（7-30日）。
- <strong>華為</strong>：2018年後停止提供解鎖碼，基本無法官方解鎖。
- <strong>一加</strong>：可以解鎖，相對寬鬆。
- <strong>OPPO/vivo</strong>：部分機型可以解鎖，需要申請。
- <strong>三星</strong>：可以解鎖，但會觸發Knox熔斷，失去Samsung Pay等功能。
- <strong>蘋果</strong>：iOS設備冇傳統意義上嘅BL鎖概念，但有類似嘅安全機制。

#### 四、ADB實用命令：通過電腦控制手機

ADB 全稱 Android Debug Bridge（安卓調試橋），係 Google 官方提供嘅命令行工具，等電腦通過 USB 或 Wi-Fi 與安卓手機通信。佢本身唔需要 Root，淨係手機開咗「USB調試」就可以用。可以將佢理解為「用電腦畀手機下指令嘅遙控器」——刷機、裝App、傳檔案、查日誌，都靠佢。

##### 點樣通過 USB 連接：

1. 手機端：進入開發者選項 → 打開「USB調試」。
2. 電腦端：由 Google 官方下載 Platform Tools（含 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb</code> 同 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot</code> 兩個可執行檔案），解壓到任意目錄。
3. 用數據線連接手機同電腦，手機上會彈窗「係咪允許USB調試」，勾選「始終允許」並確定。
4. 喺電腦命令行（Windows 嘅 PowerShell 或 cmd）入面執行 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code>，如果輸出類似 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">List of devices attached / xxxxxxxx device</code>，就說明連上咗。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>驅動同授權彈窗唔好忽略

{class="mt-1"}
Windows 用戶如果 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code> 顯示 "unauthorized" 或根本唔列出設備，多半係驅動冇裝好或者唔記得喺手機上撳「允許」。三星/小米等品牌可以裝各自嘅「USB驅動」或「手機助手」嚟補齊驅動；Mac 同 Linux 一般免驅。如果手機彈窗被你手滑撳冇咗，拔插一下數據線就會重新彈出嚟。
:::

##### 常用 ADB 命令：

- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb install app.apk</code>：將電腦上嘅 APK 裝到手機（<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-r</code> 表示覆蓋安裝並保留數據；<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code> 裝到 SD 卡）。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb uninstall com.xxx.xxx</code>：按包名卸載 App。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb push 電腦路徑 /sdcard/目標路徑</code>：將電腦檔案推送到手機。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb pull /sdcard/檔案 電腦路徑</code>：將手機檔案拉到電腦（比發畀自己微信再下載快得多）。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell</code>：進入手機嘅 Linux Shell，可以直接執行 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls</code>、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm</code>、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">am</code> 等命令。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot bootloader</code>：重啟手機進入 Fastboot 模式（刷機嘅入口）。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot recovery</code>：重啟進入 Recovery 模式。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages</code>：列出手機上所有已安裝應用嘅包名（揾包名必用）。加 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code> 淨係睇系統應用，加 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-3</code> 淨係睇第三方應用。
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 包名</code>：為當前用戶卸載預裝 App，免 Root，詳見下方實戰。

##### 免 Root 卸載預裝 App 實戰：

呢個係 ADB 最實用嘅功能之一：用 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code> 命令可以為「當前用戶」卸載預裝 App，而唔需要 Root，都唔影響系統分區。被卸載嘅 App 喺系統入面「消失」，但實際仲喺系統分區入面，恢復出廠設定後會返嚟。

1. 先用 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages -s</code> 列出所有系統應用，揾到你想卸載嘅包名。比如小米瀏覽器係 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.browser</code>，華為應用市場係 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.vmall.client</code>。
2. 唔確定包名對應邊個 App？可以喺電腦上用 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages | findstr 關鍵字</code> 搜尋，或者裝一個第三方 App "Package Viewer"喺手機上直接查看每個 App 嘅包名。
3. 執行卸載：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 包名</code>，比如 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 com.android.browser</code>。返回 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Success</code> 就成功喇。
4. 想恢復點算？兩種方法：① 恢復出廠設定（最徹底但麻煩）；② 重新安裝：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell cmd package install-existing 包名</code>。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>千萬唔好亂刪系統核心包

{class="mt-1"}
"pm uninstall --user 0"雖然係免 Root 嘅安全方式，但亂刪關鍵系統應用（如 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.systemui</code> 狀態欄、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.phone</code> 電話、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.settings</code> 設定）會導致系統崩潰、黑屏、無法開機等嚴重問題。刪之前先 Google 一下「呢個包名可唔可以刪」，寧可少刪唔好錯刪。建議一次淨係刪一兩個，確認冇問題再繼續。
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>小知識：--user 0 係乜嘢意思

{class="mt-1"}
安卓 4.2 之後支援多用戶，每個用戶有獨立嘅 ID（機主係 0，附加用戶由 10 開始）。<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">--user 0</code> 表示「淨係對當前機主卸載」，系統分區入面嘅 APK 檔案依然存在，淨係唔畀機主顯示。呢個就係點解佢唔需要 Root——冇鬱系統檔案，淨係改咗「用戶配置」。呢個都係佢同 Root 後卸載最大嘅區別：Root 卸載係真正由系統入面刪掉，所有用戶都唔再有；ADB 卸載淨係「對當前用戶隱藏」。
:::

#### 五、Root權限：安卓嘅「超級管理員」

Root權限相當於Linux中嘅超級用戶（對/目錄擁有完全控制權，可以讀寫任意檔案），係安卓系統嘅最高權限。佢同Windows嘅Administrator有本質區別：Windows出於安全考慮對管理員做咗諸多限制（真正嘅最高權限其實係 TrustedInstaller），即便係 Administrator 都無法像 Linux root 咁樣直接執行 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">sudo rm -rf /*</code>。獲得Root權限後，你可以修改系統檔案、卸載預裝應用、使用需要Root嘅高級App。

##### Root嘅好處：

- 卸載無法卸載嘅預裝應用。
- 使用高級功能App（如鈦備份、綠色守護）。
- 修改系統介面同功能。
- 安裝第三方Recovery同自訂ROM。

##### Root嘅風險：

- <strong>失去保修</strong>：大多數廠商唔保修Root過嘅手機。
- <strong>安全風險</strong>：惡意App可能獲得Root權限，造成嚴重後果。
- <strong>系統不穩定</strong>：誤操作可能導致系統崩潰。
- <strong>銀行App唔可以用</strong>：好多銀行同支付App檢測到Root會拒絕運行。
- <strong>OTA更新失敗</strong>：可能無法正常接收官方系統更新。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>嚴重警告

{class="mt-1"}
Root操作有一定風險，可能導致手機變磚（無法開機）。如果你係新手，建議先充分了解相關知識，並確保有完整嘅備份。操作前請仔細閲讀教程，確認你嘅機型同系統版本。
:::

#### 六、SafetyNet與Play Integrity認證：點解Root後銀行App唔可以用

好多Root用戶都遇過呢樣嘅崩潰瞬間：Root之後興致勃勃咁裝咗一堆模組，結果打開銀行App——「您嘅設備不安全，無法使用」，Google Pay都用唔到，連Netflix都拒絕高清播放。呢個背後係Google嘅兩套設備完整性認證機制：舊嘅 SafetyNet 同新嘅 Play Integrity API。

##### 乜嘢係 SafetyNet / Play Integrity：

- <strong>SafetyNet Attestation（舊版，2017年起）</strong>：Google 早期推出嘅設備完整性檢查 API，應用通過佢向 Google 伺服器查詢「呢臺設備係咪通過 CTS 兼容性測試、係咪處於未修改嘅官方狀態」。返回結果分為 Basic Attestation（基礎校驗）同 Strong Attestation（強校驗，依賴硬件密鑰）。Google 已宣佈 SafetyNet 將喺 2024 年後逐步停用。
- <strong>Play Integrity API（新版，2022年起）</strong>：Google 推出嘅替代方案，比 SafetyNet 更嚴格也更全面。除咗設備完整性，仲包括「應用完整性」（App 係咪被篡改）同「帳號/授權完整性」（用戶帳號係咪被 Google 信任）。新 App 應遷移到 Play Integrity。
- <strong>邊個用</strong>：銀行、金融、支付類 App（如 Google Pay、各銀行嘅網銀、支付寶/微信支付嘅部分場景）、串流媒體（Netflix 高清版權保護）、部分遊戲反作弊（如騰訊/網易嘅部分遊戲）、企業辦公 App（MDM 設備合規性檢查）。

##### Play Integrity 嘅三級認證結果：

- <strong>MEETS_DEVICE_INTEGRITY（設備完整性通過）</strong>：設備運行正版 Android 系統，Bootloader 未解鎖，冇 Root，CTS 兼容性測試通過。可以正常使用銀行、支付類 App。
- <strong>MEETS_BASIC_INTEGRITY（基礎完整性通過）</strong>：設備基本可信，但可能存在輕微異常。某些 App 會降級使用（如 Netflix 仍可播放但限制清晰度），某些嚴格嘅銀行 App 會直接拒絕。
- <strong>MEETS_STRONG_INTEGRITY（強完整性通過）</strong>：最高級別，要求硬件密鑰背書（如 Google Pixel 系列嘅 Titan M 晶片），大多數第三方品牌機型即使未 Root 都達唔到呢一級。
- <strong>無任何標籤（NO_INTEGRITY）</strong>：設備已 Root、解鎖 BL、刷咗第三方 ROM 或被識別為模擬器，絕大多數支付/銀行 App 會直接拒絕運行。

##### 點解 Root 後呢啲 App 會失效：

應用通過 Play Integrity API 向 Google 伺服器發起認證請求，Google 會檢查設備嘅多項指標——Bootloader 鎖定狀態、系統分區係咪被修改、係咪存在 su 二進制檔案、SELinux 係咪處於寬鬆模式等。任何一項異常都會導致返回嘅認證級別降低或為空，銀行 App 一睇「設備不安全」，自然就拒絕服務喇。

##### 現代隱藏方案：Magisk Hide / Shamiko / Zygisk：

為咗喺享受 Root 便利嘅同時仲可以用銀行 App，社區開發咗一系列「隱藏 Root 狀態」嘅方案。核心思路都係：等檢測程式睇到嘅唔係一個被修改過嘅系統，而係一個「睇落正常」嘅設備。

- <strong>Magisk</strong>：當前最主流嘅 Systemless Root 方案——唔修改系統分區，而係通過掛載嘅方式實現 Root。咁樣設計嘅好處係 OTA 更新失敗嘅幾率細、卸載比較乾淨，係後續所有隱藏方案嘅基礎。但使用 Magisk 仍然需要解鎖 BL 鎖。
- <strong>Magisk Hide（已停更）</strong>：Magisk 早期內置嘅隱藏模組，可以對指定 App 隱藏 Root。但 2021 年起已被 Magisk 官方移除，原因係 Google 持續升級檢測手段，雙方陷入「貓鼠遊戲」。
- <strong>Zygisk</strong>：Magisk 24.0+ 引入嘅新機制，類似 Riru，通過注入 Zygote 進程實現模組載入，比直接修改系統更隱蔽。開啟 Zygisk 係使用現代隱藏方案嘅前提。
- <strong>Shamiko</strong>：當前最主流嘅隱藏模組，配合 Zygisk 工作，可以為指定 App（「反向白名單」模式）隱藏 Root、隱藏 Magisk 自身、偽造 Bootloader 鎖定狀態。Shamiko 通過 LSPosed 倉庫或 GitHub 分發。
- <strong>Play Integrity Fix（osm0sis）</strong>：專門針對 Google Play Integrity 檢測嘅 Magisk 模組，會修改設備指紋（fingerprint）等 Google 認為你嘅設備係某個未 Root 嘅官方機型。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>貓鼠遊戲永遠唔會結束

{class="mt-1"}
Google 每隔一段時間就會更新檢測規則，App 廠商都會跟進升級 Play Integrity 校驗。今日仲可以用嘅隱藏方案，聽日可能就被識別。如果你完全依賴銀行/支付 App（比如日常轉賬、掃碼付款），最穩妥嘅選擇仍然係：唔好 Root、唔好解 BL 鎖。隱藏方案更適合「主力機唔 Root + 後備機玩 Root」嘅玩家配置。
:::

#### 七、畀普通用戶嘅建議

- <strong>開發者模式</strong>：可以開啟，體驗下動畫加速、GPU 呈現分析等功能，但唔好亂改其他唔理解嘅選項。
- <strong>OEM 解鎖與 BL 鎖</strong>：如果你唔打算刷機或 Root，兩個開關都保持預設（關閉）狀態最安全。
- <strong>ADB</strong>：免 Root 嘅強大工具，普通人都可以用——比如用 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code> 卸載預裝 App。但刪之前一定要查清楚包名可唔可以刪。
- <strong>Root</strong>：普通用戶唔建議 Root，風險大過收益。如果確實需要某些功能，可以先了解有冇唔需要 Root 嘅替代方案（比如用 ADB 卸載預裝、用 Shizuku 替代部分 Root 功能）。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>嚟動手：開啟開發者模式並調整動畫速度

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 進入設定 > 關於手機。
2. 連續撳「版本號」7次，直到提示已開啟開發者模式。
3. 返去設定，搵到「開發者選項」（通常喺設定底部或「系統」入面）。
4. 搵到「視窗動畫縮放」、「過渡動畫縮放」、「動畫程式時長縮放」，將佢哋都設為0.5x或關閉。
5. 感受一下手機係咪變快咗。
:::
