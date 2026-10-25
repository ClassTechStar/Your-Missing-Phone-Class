---
id: di-liu-shi-zhang
num: 60
part: ios-kai-fa-pian
nav: 第六十章：搭建開發環境——Xcode與第一個項目
toc: default
kind: chapter
---

### 第六十章：築開發之環境——Xcode 與第一個項目

{class="chapter-intro mb-4"}
工欲善其事，必先利其器。此章吾儕先築「庖廚」：裝成 Xcode、跑通模擬器、創人生第一個 iOS 項目，再拆工程之結構而觀之明白。環境既成，爾將初見己所書之代碼化為可點之鈕——此一瞬，多人記之終身。

#### 一、備 Mac 一台

先言其檻：iOS 開發必於 macOS 之上行之。爾若無 Mac，其擇有三：購一台（縱二手之 Mac mini 或 MacBook Air 亦足用）、短期租雲上之 Mac、或先讀第八篇《安卓開發實戰篇》（Windows 即可為之）。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">配置之項</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">至低之要求</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">寬裕之線（所薦）</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">晶片</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Silicon（M1 起）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">M2 及更新</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">記憶體</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8GB</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">16GB</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">磁碟</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">預留 40GB 以上（Xcode 本體甚巨）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256GB 起步</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系統</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最新之 macOS</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">常保自動更新</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Mac 開發機配置參考（2026 年 8 月）

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小訣：無 Mac 亦能先學語言

{class="mt-1"}
iPad 之上免費之 Swift Playgrounds 可學 Swift 語言之基（不必 Mac）；即 iPhone 之上亦可裝之。先於 Playgrounds 之中玩熟第 61 章語言之知識，待得 Mac 則徑起飛矣。磨刀不誤砍柴之工，此之謂也。
:::

#### 二、安裝 Xcode

Xcode 者，蘋果官方集成開發之環境也，免費。三步裝成：

1. 於 Mac 開 App Store，搜「Xcode」，點而安裝之——注意其有好幾 GB 之巨，擇網速善之時段；
2. 裝畢首次啟動，允其協議、裝畢組件（自動而成）；
3. 菜單 Xcode → Settings → Locations，確認 Command Line Tools 已選——命令行之器，乃多腳本與第三方之器之前提也。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：版本與系統之「匹配遊戲」

{class="mt-1"}
新 Xcode 往往須最新之 macOS，舊 Mac 則滯於舊版。上架 App Store 之時，蘋果必求以較新之 Xcode 構建（通常予一寬限之期）。故系統之更新勿拖太久——iOS 開發者乃「追新版」至勤之一群也。
:::

#### 三、創爾之第一個項目

開 Xcode → Create New Project → 擇 iOS → App 之範本，而後填之：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">配置之項</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">填何物</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">說明</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Product Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstApp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">應用之名</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">爾之 Apple ID（免費）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">簽名所用，個人帳號即可</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Organization Identifier</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">與 Product Name 併為包之標識</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interface</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">本書主線之框架</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Language</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">毋庸贅釋</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
創建項目所填之五事

點 Create 之後，Xcode 將生一可徑行之項目。左上角擇模擬器一台（如 iPhone 17），點 ▶ 而運行——數秒之後，模擬器之屏現一書「Hello, world!」之窗。爾之第一個 iOS App 誕生矣。

#### 四、拆工程之結構：每文件何為

左側乃工程導航之器，新手但識此數者可也：

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
      <text x="56" y="166" font-size="10" fill="#6b7280">（新增文件都放這個目錄下）</text>
      <text x="56" y="196" font-size="10" fill="#1e1b4b" font-weight="bold">Info 標籤頁 / Info.plist</text>
      <text x="66" y="216" font-size="10" fill="#6b7280">應用聲明：名字、權限、設置</text>
      <rect x="310" y="56" width="245" height="196" fill="#f0fdf4" rx="5"/>
      <text x="321" y="78" font-size="11" fill="#065f46" font-weight="bold">其他重要位置</text>
      <text x="331" y="100" font-size="10" fill="#374151">📁 Preview Content/  ← 預覽素材</text>
      <text x="331" y="122" font-size="10" fill="#374151"><i class="fas fa-bullseye mr-1"></i> Target 設置（藍色工程圖標）</text>
      <text x="331" y="142" font-size="10" fill="#6b7280">——版本號、最低系統、簽名皆在此</text>
      <text x="331" y="168" font-size="10" fill="#374151"><i class="fas fa-flask mr-1"></i> MyFirstAppTests/  ← 單元測試</text>
      <text x="331" y="188" font-size="10" fill="#374151">📱 MyFirstAppUITests/ ← 界面測試</text>
      <text x="331" y="216" font-size="10" fill="#9ca3af">（測試模板已生成，第 67 章用）</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖二：新手必懂之 Xcode 工程結構
:::

- MyFirstAppApp.swift：程序之入口，SwiftUI 之中惟數行——「啟之，而後示主界面」；
- ContentView.swift：主界面之視圖，爾今所見皆在此；
- Assets.xcassets：資源之倉——圖標、圖、色皆置於此；
- Target 之設置：點左側藍色工程之圖標而入，版本之號、至低 iOS 之版本、簽名皆在其中。App 顯示之名、圖標亦於此配置。

#### 五、Xcode 效率之技：新手之五「快捷鍵外掛」

熟用此數者，爾將顯得「甚專業」：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">操作</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">快捷鍵</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">功用</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">運行</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">編譯並跑之</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">開/切畫布之預覽</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">所見即所得之開關</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">格式化縮進</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自整所選代碼之縮進</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">快速開文件</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">輸入文件之名而秒開（至常用！）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">註釋/取消註釋</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">調試之時隨手開關代碼</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Xcode 高頻快捷鍵（新手五件套）

又有兩個隱藏之福利：多開模擬器（同時跑 iPhone 與 iPad 以比其佈局）與代碼片段之庫（以常用之數行拖入右側 Snippets 之面板，下次一鍵插入）——效率之器先用之，手感自來矣。

#### 六、真機調試：裝 App 於爾之 iPhone

模擬器雖善，真機方為終點。以免費之 Apple ID 亦可真機調試：

1. 以數據之線連 iPhone（或同 Wi-Fi 無線調試）；
2. Xcode 頂部設備之列表擇爾之機，首次將提示登 Apple ID 而自動配置簽名；
3. iPhone 之上［設定］→［一般］→［VPN與設備管理］→ 信爾開發者之證書；
4. 點 ▶，App 入真機矣。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：免費帳號之「七日限制」

{class="mt-1"}
免費 Apple ID 簽名之 App，七日之後失效（再運行一次即可續之）。此蘋果防濫用之制也，學習之期足用；付費開發者帳號（99 美元一年）則無此限，第 67 章詳說之。
:::

#### 七、小試其刃加常見報錯之急救

開 ContentView.swift，以爾之名易 Text("Hello, world!") 之字，按 ⌘R 再運行——數秒之後模擬器之上現爾之名。賀爾，爾已竟首次完整之「改代碼 → 編譯 → 安裝 → 運行」之循環矣。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">報錯之象</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">常見之因</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">解之之方</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Signing 之報錯</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team 未選、證書過期</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Target → Signing 之中勾爾之帳號；免費之帳再跑一次</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">模擬器黑屏/不能開</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">鏡像已壞</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">菜單 Device → Erase All Content；或刪之而重加模擬器</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode 下載緩/不能裝</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">App Store 網絡之波動</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">換時段；或至蘋果開發者之網站下載 .xip 離線之包</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
新手環境報錯急救表

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：竟爾「開發儀式感」之清單

{class="mt-1"}
① 裝成 Xcode 並跑通模擬器；② 以真機跑己之 App 一次而截圖留念；③ 易 Hello 之字為爾之名；④ 至 Target 之設置易 App 顯示之名為「吾之第一個App」。四步既畢，爾乃有作品之人矣。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小結

- 硬檻：Mac 加 Xcode；無 Mac 者先以 iPad 之 Swift Playgrounds 學語言
- Xcode 自 App Store 裝之；新版本要求新系統，更新勿拖
- 新建項目五要：名、Team、組織標識、SwiftUI、Swift
- 工程之訣：代碼皆在 MyFirstApp/ 之目錄；Target 之設置管版本與簽名
- 免費 Apple ID 真機調試有七日簽名之限；付費之帳無此限
- 開發之日常 = 改代碼 → ⌘R → 觀其效，循環往復
:::
