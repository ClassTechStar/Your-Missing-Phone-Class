---
id: di-wu-shi-liu-zhang
num: 56
part: an-zhuo-kai-fa-pian
nav: 第五十六章：打磨與發佈——上架Google Play
toc: default
kind: chapter
---

### 第五十六章：打磨與發佈——測試、除錯與上架 Google Play

{class="chapter-intro mb-4"}
App 做出來了，然後呢？這一章回答"從能跑"到"能交付"的三件事：怎麼高效地除錯找 bug、怎麼寫測試防迴歸、怎麼把 App 送上 Google Play 讓全世界下載。上架不只是儀式感——它是把一個作品變成產品的分水嶺。

#### 一、除錯三板斧：Logcat、斷點、UI 檢查器

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">工具</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">幹什麼</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">怎麼用</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logcat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">看系統/自己打的日誌</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">程式碼裡 Log.d("TAG","值=$x")，面板裡搜 TAG 過濾</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">斷點除錯</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">讓程式停在某行，看變數值</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">行號旁點一下出紅點，Debug 模式執行，逐步走</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Layout Inspector</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">看執行中的介面結構</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">選單 Tools → Layout Inspector，實時看元件樹</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
除錯三板斧

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：報錯怎麼讀？

{class="mt-1"}
崩潰後 Logcat 裡會有紅色堆疊（Stacktrace），從下往上找 第一個自己包名開頭的行（比如 com.example.yourapp），那行基本就是案發現場。先看"Exception 型別"（空指標？型別轉換？），再看"at ... 你的檔案:行號"。這招能解決 80% 的崩潰。
:::

#### 二、測試：給程式碼上保險

手測靠不住——改了這個功能，另一個悄悄壞了。測試就是"後悔藥"兼"防彈衣"。安卓測試分三層，新手先吃透第一層：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">層級</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">測什麼</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">放哪裡</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">速度</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">單元測試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">純邏輯（計算、校驗）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/test/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">秒級</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">儀器測試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真實裝置上的介面行為</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/androidTest/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分鐘級</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">手動測試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真人感受、體驗</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">永遠需要</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
測試三層

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 單元測試示例</span><span class="dots">···</span>
:::

```
// 把"金額字串轉數字"這種邏輯抽成純函式
fun parseAmount(input: String): Double? {
    val v = input.trim().toDoubleOrNull()
    return if (v != null && v > 0) v else null
}

// 測試它（JUnit4）
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

記帳本里的金額校驗、統計計算，都該有單元測試罩著。跑測試：右鍵 test 目錄 → Run。綠色全過，放心改程式碼。

#### 三、簽名打包：給 App 蓋上"印章"

安卓要求所有安裝包必須簽名——就像蓋公章，證明"這個包是我出的，沒被篡改"。除錯時 Android Studio 自動用 debug 簽名；發佈要用自己的 release 簽名。流程：

1. 選單 Build → Generate Signed Bundle / APK；
2. 建立 keystore 檔案（金鑰庫）——設定密碼並妥善保管；
3. 選擇 release + AAB 格式，構建完成。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
避坑提醒：keystore 丟了 = App 丟了

{class="mt-1"}
上架後更新 App 必須用同一個簽名，否則商店會拒絕更新。keystore 檔案和密碼一旦丟失，你只能換個新應用重新上架——老使用者全都接不上。務必把 keystore 和密碼備份到安全的地方（雲盤加密 + 記事本），這是安卓開發者最昂貴的教訓之一。
:::

#### 四、上架 Google Play 全流程

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> 註冊開發者帳號</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> 準備商店素材</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> 上傳 AAB</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> 填資料安全表</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> 稽核（數小時~數天）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> 上架</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 6：Google Play 上架六步走
:::

- 註冊：一次性 25 美元註冊費，需能用的 Google 帳號；
- 素材：應用圖示（512×512）、截圖（至少 2 張）、功能描述、隱私政策連結（收集資料必填）；
- 資料安全表：如實申報收集了哪些資料——不聯網的記帳本可以"零收集"；
- 稽核：新帳號首次上架常被人工稽核，數小時到數天不等，被打回就按意見改。

國內使用者注意：Google Play 需要特殊網路環境，且中國大陸地區分發通常走國內商店（華為、小米、應用寶等）。上架國內商店的流程類似，但各商店有自己的稽核口味——同一個 AAB/APK 可以多店分發。作為練手，先走通一家就贏了。

#### 五、商店素材怎麼做：第一印象就是下載量

商店頁是使用者"逛店"時看到的櫥窗。三個素材決定第一印象：

- 圖示：512×512，別用截圖湊合。沒設計能力就用 AI 工具生成一個簡潔幾何圖形，在手機桌面上縮小後還能一眼認出才算合格；
- 截圖：至少 2 張，最好 4-6 張，展示最核心的功能場景；每張配一句人話文案（"一秒記一筆"比"高效的記帳解決方案"好十倍）；
- 描述：第一句說清"這是什麼 + 給誰用"，別堆砌"最專業、最強"——商店搜尋權重主要看關鍵詞和下載轉化，真誠比誇張有效。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：A/B 看看同行

{class="mt-1"}
上架前逛一圈商店裡同類 App 的前十名，截圖對比：他們圖示什麼風格？截圖講什麼賣點？標題怎麼寫？模仿不是抄襲——學套路、換自己的內容，這是所有產品冷啟動最快的一課。
:::

#### 六、效能最佳化與崩潰上報小清單

App 上架前，這兩件事值得各花半小時：

##### 1. 效能自查四條

1. 列表用 LazyColumn：長列表千萬別用 Column 硬排——懶載入是安卓效能的第一課；
2. 圖片別硬塞原圖：用 Coil 圖片庫自動縮放快取，一張 5MB 原圖足以卡爆低端機；
3. 避免在主執行緒乾重活：資料庫、網路、大檔案都在協程裡做；
4. 用 Profiler 量一量：Android Studio 自帶的效能分析器能看記憶體、CPU、耗電——先測量，再最佳化，別憑感覺。

##### 2. 崩潰上報

你測試時沒崩，不代表使用者手機不崩。上架前接入 Firebase Crashlytics（谷歌官方，免費）：幾行配置，使用者崩潰時自動上報堆疊，你在後臺就能看到"哪個機型、哪個版本、崩在哪一行"。沒有崩潰監控的上架，等於閉著眼睛開車。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：把記帳本"交付"一次

{class="mt-1"}
① 給 parseAmount 等邏輯補 3 個單元測試；② 用 Logcat 親手抓一個自己製造的崩潰並修好；③ 生成一個 release 簽名的 APK，發給朋友安裝（這才是"作品"的儀式感）；④ 有餘力就註冊開發者帳號，把記帳本真正提交上架。前三條今晚就能做完。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 除錯三板斧：Logcat 看日誌、斷點看變數、Layout Inspector 看介面
- 讀崩潰：從堆疊下往上找自己包名的第一行
- 測試三層：單元（秒級，先學這個）/儀器/手動
- 發佈必須簽名：keystore 和密碼備份好，丟了 App 就"換人"了
- 上架六步：註冊 → 素材 → 上傳 AAB → 資料安全表 → 稽核 → 上架
:::
