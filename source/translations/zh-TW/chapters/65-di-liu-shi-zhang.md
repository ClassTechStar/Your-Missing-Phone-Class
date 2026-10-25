---
id: di-liu-shi-zhang
num: 60
part: ios-kai-fa-pian
nav: 第六十章：搭建開發環境——Xcode與第一個專案
toc: default
kind: chapter
---

### 第六十章：搭建開發環境——Xcode 與第一個專案

{class="chapter-intro mb-4"}
工欲善其事，必先利其器。這一章咱們把"廚房"搭好：裝好 Xcode、跑通模擬器、建立人生第一個 iOS 專案，再把工程結構拆開看個明白。裝好環境之後，你會第一次看到自己寫的程式碼變成一個能點的按鈕——這個瞬間，很多人會記一輩子。

#### 一、準備一臺 Mac

先說門檻：iOS 開發必須在 macOS 上進行。如果你沒有 Mac，選項有三：買一臺（哪怕是二手 Mac mini 或 MacBook Air 都夠用）、短期租雲 Mac、或者先讀第八篇《安卓開發實戰篇》（Windows 就能幹）。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">配置項</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">最低要求</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">舒適線（推薦）</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">晶片</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Silicon（M1 起）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">M2 及更新</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">記憶體</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8GB</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">16GB</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">磁碟</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">預留 40GB+（Xcode 本體很胖）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256GB 起步</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系統</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最新 macOS</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">保持自動更新</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Mac 開發機配置參考（2026 年 8 月）

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：沒有 Mac 也能先學語言

{class="mt-1"}
iPad 上免費的 Swift Playgrounds 能學 Swift 語言基礎（不用 Mac）；甚至 iPhone 上也能裝。先把第 61 章的語言知識在 Playgrounds 裡玩熟，等拿到 Mac 後直接起飛。磨刀不誤砍柴工，說的就是這個。
:::

#### 二、安裝 Xcode

Xcode 是蘋果官方的整合開發環境，免費。三步裝好：

1. Mac 上開啟 App Store，搜尋 "Xcode"，點安裝——注意它有好幾個 GB，找個網速好的時段；
2. 裝完首次啟動，同意協議、裝完元件（自動完成）；
3. 選單 Xcode → Settings → Locations，確認 Command Line Tools 已選中——命令列工具是很多指令碼和第三方工具的前提。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：版本和系統的"匹配遊戲"

{class="mt-1"}
新 Xcode 往往要求最新 macOS，舊 Mac 則會卡在老版本。上架 App Store 時，蘋果會要求用較新的 Xcode 構建（通常給一個寬限期）。所以系統更新別拖太久——iOS 開發者是"追新版"最勤快的一群人。
:::

#### 三、建立你的第一個專案

開啟 Xcode → Create New Project → 選 iOS → App 模板，然後填：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">配置項</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">填什麼</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">說明</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Product Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstApp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">應用程式名稱字</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">你的 Apple ID（免費）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">簽名用，個人帳號即可</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Organization Identifier</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">和 Product Name 拼成包標識</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interface</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">本書主線框架</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Language</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不解釋</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
建立專案要填的五件事

點 Create 後，Xcode 會生成一個能直接跑的專案。左上角選一臺模擬器（比如 iPhone 17），點 ▶ 執行——幾秒後，模擬器螢幕上出現一個寫著 "Hello, world!" 的視窗。你的第一個 iOS App 已經誕生了。

#### 四、工程結構拆解：每個檔案是幹嘛的

左側是工程導航器，新手只需認識這幾個：

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="290" viewBox="0 0 600 290" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="290" fill="#fafafa" rx="8"/>
      <text x="20" y="28" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ 專案根目錄</text>
      <rect x="30" y="42" width="540" height="225" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <rect x="45" y="56" width="250" height="196" fill="#eef2ff" rx="5"/>
      <text x="56" y="78" font-size="11" fill="#1e1b4b" font-weight="bold">MyFirstApp/（程式碼目錄）</text>
      <text x="66" y="100" font-size="10" fill="#374151">├ MyFirstAppApp.swift  ← 程式入口</text>
      <text x="66" y="120" font-size="10" fill="#374151">├ ContentView.swift  ← 主介面</text>
      <text x="66" y="140" font-size="10" fill="#374151">└ Assets.xcassets  ← 圖示、圖片、顏色</text>
      <text x="56" y="166" font-size="10" fill="#6b7280">（新增檔案都放這個目錄下）</text>
      <text x="56" y="196" font-size="10" fill="#1e1b4b" font-weight="bold">Info 標籤頁 / Info.plist</text>
      <text x="66" y="216" font-size="10" fill="#6b7280">應用宣告：名字、許可權、設定</text>
      <rect x="310" y="56" width="245" height="196" fill="#f0fdf4" rx="5"/>
      <text x="321" y="78" font-size="11" fill="#065f46" font-weight="bold">其他重要位置</text>
      <text x="331" y="100" font-size="10" fill="#374151">📁 Preview Content/  ← 預覽素材</text>
      <text x="331" y="122" font-size="10" fill="#374151"><i class="fas fa-bullseye mr-1"></i> Target 設定（藍色工程圖示）</text>
      <text x="331" y="142" font-size="10" fill="#6b7280">——版本號、最低系統、簽名都在這</text>
      <text x="331" y="168" font-size="10" fill="#374151"><i class="fas fa-flask mr-1"></i> MyFirstAppTests/  ← 單元測試</text>
      <text x="331" y="188" font-size="10" fill="#374151">📱 MyFirstAppUITests/ ← 介面測試</text>
      <text x="331" y="216" font-size="10" fill="#9ca3af">（測試模板已生成，第 67 章用）</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 2：新手必懂的 Xcode 工程結構
:::

- MyFirstAppApp.swift：程式入口，SwiftUI 裡它只有幾行——"啟動，然後顯示主介面"；
- ContentView.swift：主介面檢視，你現在看到的一切都在這裡；
- Assets.xcassets：資源倉庫——圖示、圖片、顏色都放這；
- Target 設定：點左側藍色工程圖示進去，版本號、最低 iOS 版本、簽名都在裡面。App 顯示名、圖示也在這配置。

#### 五、Xcode 效率技巧：新手的五個"快速鍵外掛"

用熟這幾個，你會顯得"很專業"：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">操作</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">快速鍵</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">作用</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">執行</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">編譯並跑起來</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">開啟/切換畫布預覽</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">所見即所得的開關</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">格式化縮排</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自動整理選中程式碼的縮排</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">快速開啟檔案</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">輸入檔名秒開（最常用！）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">註釋/取消註釋</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">除錯時隨手開關程式碼</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Xcode 高頻快速鍵（新手五件套）

另外兩個隱藏福利：多開模擬器（同時跑 iPhone 和 iPad 對比佈局）和程式碼片段庫（把常用的幾行程式碼拖進右側 Snippets 面板，下次一鍵插入）——效率工具先用起來，手感自然就上來了。

#### 六、真機除錯：把 App 裝進你的 iPhone

模擬器雖好，真機才是終點。用免費 Apple ID 也能真機除錯：

1. 資料線連上 iPhone（或同 Wi-Fi 無線除錯）；
2. Xcode 頂部裝置列表選你的手機，首次會提示登入 Apple ID 並自動配置簽名；
3. iPhone 上 [設定] → [通用] → [VPN與裝置管理] → 信任你的開發者證書；
4. 點 ▶，App 裝進真機。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：免費帳號的"七天限制"

{class="mt-1"}
免費 Apple ID 簽署的 App 7 天後會失效（重新執行一次即可續期）。這是蘋果的防濫用機制，學習階段完全夠用；付費開發者帳號（99 美元/年）則沒有這個限制，第 67 章會細說。
:::

#### 七、小試牛刀 + 常見報錯急救

開啟 ContentView.swift，把 Text("Hello, world!") 裡的字換成你的名字，按 ⌘R 重新執行——幾秒後模擬器上就顯示你的名字。恭喜，你完成了第一次完整的"改程式碼 → 編譯 → 安裝 → 執行"迴圈。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">報錯現象</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">常見原因</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">解藥</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Signing 報錯</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team 沒選、證書過期</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Target → Signing 裡勾上你的帳號；免費帳號重跑一次</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">模擬器黑屏/打不開</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">映象損壞</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">選單 Device → Erase All Content；或刪掉重加模擬器</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode 下載慢/裝不上</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">App Store 網路波動</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">換時段；或到蘋果開發者網站下載 .xip 離線包</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
新手環境報錯急救表

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：完成你的"開發儀式感"清單

{class="mt-1"}
① 裝好 Xcode 並跑通模擬器；② 用真機跑一次自己的 App 並截圖留念；③ 把 Hello 文字改成你的名字；④ 到 Target 設定裡把 App 顯示名改成"我的第一個App"。做完這四步，你就是有作品的人了。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 硬門檻：Mac + Xcode；沒有 Mac 先用 iPad 上的 Swift Playgrounds 學語言
- Xcode 從 App Store 裝；新版本要求新系統，更新別拖
- 新增專案五要素：名字、Team、組織標識、SwiftUI、Swift
- 工程口訣：程式碼都在 MyFirstApp/ 目錄；Target 設定管版本與簽名
- 免費 Apple ID 真機除錯有 7 天簽名限制；付費帳號無此限制
- 開發日常 = 改程式碼 → ⌘R → 看效果，迴圈往復
:::
