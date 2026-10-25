---
id: di-liu-shi-zhang
num: 60
part: ios-kai-fa-pian
nav: 第六十章：搭建開發環境——Xcode與第一個項目
toc: default
kind: chapter
---

### 第六十章：搭建開發環境——Xcode 同第一個項目

{class="chapter-intro mb-4"}
工欲善其事，必先利其器。呢一章我哋將個「廚房」搭好：裝好 Xcode、行通模擬器、建立人生第一個 iOS 項目，再將工程結構拆開睇個明白。裝好環境之後，你會第一次見到自己寫嘅代碼變成一個㩒得到嘅掣——呢個瞬間，好多人會記一世。

#### 一、準備一部 Mac

先講門檻：iOS 開發必須喺 macOS 上面進行。如果你冇 Mac，選擇有三：買一部（就算係二手 Mac mini 或者 MacBook Air 都夠用）、短期租雲 Mac、或者先讀第八篇《安卓開發實戰篇》（Windows 就得）。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">配置項</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">最低要求</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">舒適線（推薦）</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">晶片</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Silicon（M1 起）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">M2 或更新</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">記憶體</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8GB</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">16GB</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">磁碟</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">預留 40GB+（Xcode 本體好肥）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256GB 起步</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系統</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最新 macOS</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">保持自動更新</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Mac 開發機配置參考（2026 年 8 月）

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：冇 Mac 都可以先學語言

{class="mt-1"}
iPad 上面免費嘅 Swift Playgrounds 可以學 Swift 語言基礎（唔使 Mac）；甚至 iPhone 上面都裝到。先將第 61 章嘅語言知識喺 Playgrounds 度玩熟，等攞到 Mac 之後就即刻起飛。磨刀唔誤砍柴工，講嘅就係呢樣。
:::

#### 二、安裝 Xcode

Xcode 係蘋果官方嘅集成開發環境，免費。三步裝好：

1. 喺 Mac 打開 App Store，搜「Xcode」，㩒安裝——留意佢有成幾個 GB，搵個網速好嘅時段；
2. 裝完第一次啟動，同意協議、裝完組件（自動完成）；
3. 選單 Xcode → Settings → Locations，確認 Command Line Tools 已經揀咗——命令行工具係好多腳本同第三方工具嘅前提。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：版本同系統嘅「配對遊戲」

{class="mt-1"}
新 Xcode 好多時都要求最新 macOS，舊 Mac 就會卡喺舊版本。上架 App Store 嗰陣，蘋果會要求用較新嘅 Xcode 構建（通常會畀一段寬限期）。所以系統更新唔好拖太耐——iOS 開發者係「追新版」最勤力嘅一群人。
:::

#### 三、建立你嘅第一個項目

打開 Xcode → Create New Project → 揀 iOS → App 模板，跟住填：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">配置項</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">填乜嘢</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">說明</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Product Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstApp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">應用名</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">你嘅 Apple ID（免費）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">簽名用，個人賬號就得</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Organization Identifier</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">同 Product Name 拼埋組成包標識</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interface</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">本書主線框架</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Language</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">唔使解釋</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
建立項目要填嘅五樣嘢

㩒 Create 之後，Xcode 會生成一個可以直接行嘅項目。左上角揀一部模擬器（例如 iPhone 17），㩒 ▶ 運行——幾秒之後，模擬器屏幕上面會出現一個寫住 "Hello, world!" 嘅窗口。你嘅第一個 iOS App 已經誕生咗喇。

#### 四、工程結構拆解：每個檔案係做乜嘢嘅

左邊係工程導航器，新手只需要識呢幾個：

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="290" viewBox="0 0 600 290" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="290" fill="#fafafa" rx="8"/>
      <text x="20" y="28" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ 項目根目錄</text>
      <rect x="30" y="42" width="540" height="225" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <rect x="45" y="56" width="250" height="196" fill="#eef2ff" rx="5"/>
      <text x="56" y="78" font-size="11" fill="#1e1b4b" font-weight="bold">MyFirstApp/（代碼目錄）</text>
      <text x="66" y="100" font-size="10" fill="#374151">├ MyFirstAppApp.swift  ← 程序入口</text>
      <text x="66" y="120" font-size="10" fill="#374151">├ ContentView.swift  ← 主界面</text>
      <text x="66" y="140" font-size="10" fill="#374151">└ Assets.xcassets  ← 圖標、圖片、顏色</text>
      <text x="56" y="166" font-size="10" fill="#6b7280">（新增檔案都放這個目錄下）</text>
      <text x="56" y="196" font-size="10" fill="#1e1b4b" font-weight="bold">Info 標籤頁 / Info.plist</text>
      <text x="66" y="216" font-size="10" fill="#6b7280">應用聲明：名字、權限、設定</text>
      <rect x="310" y="56" width="245" height="196" fill="#f0fdf4" rx="5"/>
      <text x="321" y="78" font-size="11" fill="#065f46" font-weight="bold">其他重要位置</text>
      <text x="331" y="100" font-size="10" fill="#374151">📁 Preview Content/  ← 預覽素材</text>
      <text x="331" y="122" font-size="10" fill="#374151"><i class="fas fa-bullseye mr-1"></i> Target 設定（藍色工程圖標）</text>
      <text x="331" y="142" font-size="10" fill="#6b7280">——版本號、最低系統、簽名都在這</text>
      <text x="331" y="168" font-size="10" fill="#374151"><i class="fas fa-flask mr-1"></i> MyFirstAppTests/  ← 單元測試</text>
      <text x="331" y="188" font-size="10" fill="#374151">📱 MyFirstAppUITests/ ← 界面測試</text>
      <text x="331" y="216" font-size="10" fill="#9ca3af">（測試模板已生成，第 67 章用）</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 2：新手必識嘅 Xcode 工程結構
:::

- MyFirstAppApp.swift：程式入口，喺 SwiftUI 入面佢只有幾行——「啟動，跟住顯示主界面」；
- ContentView.swift：主界面視圖，你而家見到嘅一切都在呢度；
- Assets.xcassets：資源倉庫——圖標、圖片、顏色都擺喺呢度；
- Target 設定：㩒左邊藍色工程圖標入去，版本號、最低 iOS 版本、簽名都在入面。App 顯示名、圖標都係喺呢度配置。

#### 五、Xcode 效率技巧：新手嘅五個「快捷鍵外掛」

用熟呢幾個，你會顯得「好專業」：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">操作</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">快捷鍵</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">作用</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">運行</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">編譯並且行起上嚟</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">打開/切換畫布預覽</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">所見即所得嘅開關</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">格式化縮排</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自動整理選中代碼嘅縮排</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">快速打開檔案</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">輸入檔案名即刻開到（最常用！）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">註釋/取消註釋</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">除錯嗰陣順手開關代碼</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Xcode 高頻快捷鍵（新手五件套）

另外兩個隱藏福利：多開模擬器（同時行 iPhone 同 iPad 對比佈局）同代碼片段庫（將常用嘅幾行代碼拖入右邊 Snippets 面板，下次一鍵插入）——效率工具先用起上嚟，手感自然就上嚟喇。

#### 六、真機除錯：將 App 裝入你嘅 iPhone

模擬器雖然好，但真機先係終點。用免費 Apple ID 都可以真機除錯：

1. 數據線駁上 iPhone（或者同 Wi-Fi 無線除錯）；
2. Xcode 頂部設備列表揀你部手機，第一次會提示登入 Apple ID 並且自動配置簽名；
3. iPhone 上面 [設定] → [一般] → [VPN與設備管理] → 信任你嘅開發者證書；
4. 㩒 ▶，App 就裝入真機。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：免費賬號嘅「七日限制」

{class="mt-1"}
免費 Apple ID 簽名嘅 App 7 日之後會失效（重新運行一次就可以續期）。呢個係蘋果嘅防濫用機制，學習階段完全夠用；付費開發者賬號（99 美元/年）就冇呢個限制，第 67 章會詳細講。
:::

#### 七、小試牛刀 + 常見報錯急救

打開 ContentView.swift，將 Text("Hello, world!") 入面嘅字換成你個名，㩒 ⌘R 重新運行——幾秒之後模擬器上面就會顯示你個名。恭喜，你完成咗第一次完整嘅「改代碼 → 編譯 → 安裝 → 運行」循環。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">報錯現象</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">常見原因</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">解藥</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Signing 報錯</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team 冇揀、證書過期</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">喺 Target → Signing 度剔返你嘅賬號；免費賬號重新行一次</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">模擬器黑屏/開唔到</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">映像損壞</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">選單 Device → Erase All Content；或者刪咗佢重新加返模擬器</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode 下載慢/裝唔到</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">App Store 網絡波動</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">轉個時段；或者去蘋果開發者網站下載 .xip 離線包</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
新手環境報錯急救表

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
嚟動手：完成你嘅「開發儀式感」清單

{class="mt-1"}
① 裝好 Xcode 並且行通模擬器；② 用真機行一次自己嘅 App 並且截圖留念；③ 將 Hello 文字改成你個名；④ 去 Target 設定度將 App 顯示名改成「我嘅第一個App」。做完呢四步，你已經係一個有作品嘅人喇。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 硬門檻：Mac + Xcode；冇 Mac 就先用 iPad 上面嘅 Swift Playgrounds 學語言
- Xcode 由 App Store 裝；新版本要求新系統，更新唔好拖
- 新建立項目五要素：名、Team、組織標識、SwiftUI、Swift
- 工程口訣：代碼都在 MyFirstApp/ 目錄；Target 設定管版本同簽名
- 免費 Apple ID 真機除錯有 7 日簽名限制；付費賬號冇呢個限制
- 開發日常 = 改代碼 → ⌘R → 睇效果，循環不息
:::
