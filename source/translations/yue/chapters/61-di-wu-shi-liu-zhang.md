---
id: di-wu-shi-liu-zhang
num: 56
part: an-zhuo-kai-fa-pian
nav: 第五十六章：打磨與發佈——上架Google Play
toc: default
kind: chapter
---

### 第五十六章：打磨同發布——測試、除錯同上架 Google Play

{class="chapter-intro mb-4"}
App 做咗出嚟，跟住點呢？呢一章回答「由跑得郁」到「可以交付」嘅三件事：點樣高效咁除錯搵 bug、點樣寫測試防走樣、點樣將 App 攞上 Google Play 畀全世界下載。上架唔只係儀式感——佢係將一件作品變成產品嘅分水嶺。

#### 一、除錯三板斧：Logcat、斷點、UI 檢查器

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">工具</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">做乜嘢</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">點用</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logcat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">睇系統/自己打嘅日誌</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">代碼入面 Log.d("TAG","值=$x")，喺面板搜 TAG 過濾</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">斷點除錯</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">令程式停喺某一行，睇變數值</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">喺行號旁邊㩒一下出紅點，用 Debug 模式行，逐步咁行</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Layout Inspector</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">睇運行中嘅界面結構</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">選單 Tools → Layout Inspector，實時睇組件樹</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
除錯三板斧

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：報錯點樣睇？

{class="mt-1"}
崩潰之後 Logcat 會有紅色堆疊（Stacktrace），由下往上搵第一行以自己包名開頭嘅（例如 com.example.yourapp），嗰行基本上就係案發現場。先睇「Exception 類型」（空指標？類型轉換？），再睇「at ... 你嘅檔案:行號」。呢一招可以解決 80% 嘅崩潰。
:::

#### 二、測試：畀代碼買保險

手動測試靠唔住——改咗呢個功能，另一個靜靜雞壞咗。測試就係「後悔藥」兼「防彈衣」。安卓測試分三層，新手先讀透第一層：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">層級</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">測乜嘢</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">擺喺邊</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">速度</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">單元測試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">純邏輯（計算、校驗）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/test/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">秒級</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">儀器測試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真實設備上嘅界面行為</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/androidTest/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分鐘級</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">手動測試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真人感受、體驗</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">永遠都需要</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
測試三層

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 單元測試示例</span><span class="dots">···</span>
:::

```
// 把"金額字串轉數字"呢種邏輯抽成純函數
fun parseAmount(input: String): Double? {
    val v = input.trim().toDoubleOrNull()
    return if (v != null && v > 0) v else null
}

// 測試佢（JUnit4）
@Test
fun emptyInputReturnsNull() {
    assertEquals(null, parseAmount(""))
}
@Test
fun negativeReturnsNull() {
    assertEquals(null, parseAmount("-5"))
}
@Test
fun normalValueParses() {
    assertEquals(12.5, parseAmount("12.5"))
}
```
:::

記賬本入面嘅金額校驗、統計計算，都應該有單元測試罩住。行測試：右鍵 test 目錄 → Run。全部綠色過關，就可以放心改代碼。

#### 三、簽名打包：畀 App 蓋上「印章」

安卓要求所有安裝包必須簽名——就好似蓋公章咁，證明「呢個包係我出嘅，冇畀人改過」。除錯嗰陣 Android Studio 會自動用 debug 簽名；發布就要用自己嘅 release 簽名。流程係：

1. 選單 Build → Generate Signed Bundle / APK；
2. 建立 keystore 檔案（密鑰庫）——設定密碼同埋妥善保管；
3. 揀 release + AAB 格式，構建完成。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
避坑提醒：keystore 唔見咗 = App 唔見咗

{class="mt-1"}
上架之後更新 App 必須用同一個簽名，否則商店會拒絕更新。keystore 檔案同密碼一旦唔見咗，你就只可以另開一個新應用重新上架——舊用戶全部接唔返。一定要將 keystore 同密碼備份去安全嘅地方（雲盤加密 + 記事本），呢個係安卓開發者最昂貴嘅教訓之一。
:::

#### 四、上架 Google Play 全流程

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> 註冊開發者賬號</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> 準備商店素材</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> 上傳 AAB</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> 填數據安全表</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> 審覈（數小時~數天）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> 上架</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 6：Google Play 上架六步走
:::

- 註冊：一次性 25 美元註冊費，需要一個用得嘅 Google 賬號；
- 素材：應用圖標（512×512）、截圖（最少 2 張）、功能描述、私隱政策連結（有收集數據就必填）；
- 數據安全表：如實申報收集咗邊啲數據——唔聯網嘅記賬本可以「零收集」；
- 審核：新賬號首次上架好多時會經人工審核，幾個鐘到幾日唔等，被打回頭就照意見改。

國內用戶注意：Google Play 需要特殊網絡環境，而且中國大陸地區分發通常行國內商店（華為、小米、應用寶等）。上架國內商店嘅流程類似，但各商店有自己嘅審核口味——同一個 AAB/APK 可以多間店一齊分發。作為練手，先行通一間就已經贏咗。

#### 五、商店素材點樣做：第一印象就係下載量

商店頁係用戶「行店」嗰陣見到嘅櫥窗。三樣素材決定第一印象：

- 圖標：512×512，唔好攞截圖求其算數。冇設計能力就用 AI 工具生成一個簡潔幾何圖形，喺手機桌面縮細之後都仲可以一眼認得出先算合格；
- 截圖：最少 2 張，最好 4-6 張，展示最核心嘅功能場景；每張配一句講人話嘅文案（「一秒記一筆」好過「高效嘅記賬解決方案」十倍）；
- 描述：第一句講清楚「呢個係乜嘢 + 畀邊個用」，唔好亂堆「最專業、最勁」——商店搜索權重主要睇關鍵詞同下載轉化，真誠好過誇張。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：A/B 睇吓同行

{class="mt-1"}
上架之前行一圈商店入面同類 App 嘅前十名，截圖嚟對比：佢哋啲圖標係咩風格？截圖講咩賣點？標題點寫？模仿唔係抄襲——學套路、換自己做嘅內容，呢個係所有產品冷啟動最快嘅一課。
:::

#### 六、性能優化同崩潰上報小清單

App 上架之前，呢兩件事值得各花半個鐘：

##### 1. 性能自查四條

1. 列表用 LazyColumn：長列表千祈唔好用 Column 硬排——懶加載係安卓性能嘅第一課；
2. 圖片唔好硬塞原圖：用 Coil 圖片庫自動縮放同緩存，一張 5MB 嘅原圖足以卡爆低端機；
3. 避免喺主線程做重活：數據庫、網絡、大檔案都擺喺協程度做；
4. 用 Profiler 度一度：Android Studio 自帶嘅性能分析器睇到內存、CPU、耗電——先量度，再優化，唔好齋靠感覺。

##### 2. 崩潰上報

你測試嗰陣冇崩，唔代表用戶部手機唔崩。上架之前接入 Firebase Crashlytics（谷歌官方，免費）：幾行配置，用戶崩潰嗰陣自動上報堆疊，你喺後台就會見到「邊個型號、邊個版本、崩喺邊一行」。冇崩潰監控就上架，等於瞇埋眼揸車。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
嚟動手：將記賬本「交付」一次

{class="mt-1"}
① 幫 parseAmount 呢啲邏輯補 3 個單元測試；② 用 Logcat 親手捉一個自己整出嚟嘅崩潰然後修好佢；③ 生成一個 release 簽名嘅 APK，發畀朋友安裝（呢個先係「作品」嘅儀式感）；④ 有餘力就註冊開發者賬號，將記賬本真正提交上架。前三條今晚就做得完。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 除錯三板斧：Logcat 睇日誌、斷點睇變數、Layout Inspector 睇界面
- 讀崩潰：由堆疊下面往上搵自己包名嘅第一行
- 測試三層：單元（秒級，先學呢個）/儀器/手動
- 發布必須簽名：keystore 同密碼備份好，唔見咗個 App 就等於「換咗人」喇
- 上架六步：註冊 → 素材 → 上傳 AAB → 數據安全表 → 審核 → 上架
:::
