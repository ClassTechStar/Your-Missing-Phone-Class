---
id: di-wu-shi-liu-zhang
num: 56
part: an-zhuo-kai-fa-pian
nav: 第五十六章：打磨與發布——上架Google Play
toc: default
kind: chapter
---

### 第五十六章：琢磨與發佈——測試、調試與上架 Google Play

{class="chapter-intro mb-4"}
App 既成，繼之奈何？此章答「自能行」至「能交付」之三事：何以高效調試而得 bug、何以書測試以防回歸、何以送 App 上 Google Play 而使天下皆得下載之。上架非徒儀式之感——乃使一作化為一產之分水嶺也。

#### 一、調試三板斧：Logcat、斷點、UI 檢查器

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">工具</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">所為何事</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">何以用之</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logcat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">觀系統/自書之日誌</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">代碼中 Log.d("TAG","值=$x")，面板搜 TAG 以濾</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">斷點調試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">使程序停於某行，觀變量之值</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">行號旁一點而出紅點，Debug 模式而運，逐步行之</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Layout Inspector</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">觀運行中界面之構</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">菜單 Tools → Layout Inspector，實時觀組件之樹</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
調試三板斧

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小識：報錯何以讀？

{class="mt-1"}
崩之後，Logcat 中有赤色堆棧（Stacktrace），自下而上覓首行以己包名起者（譬如 com.example.yourapp），彼行基本即案發之場。先觀「Exception 之類」（空指針乎？類型之轉乎？），復觀「at ... 汝之文件:行號」。此招能解崩潰之百分之八十。
:::

#### 二、測試：為代碼上保險

手測不足恃——改此功能，彼者潛壞。測試者，「悔之藥」而兼「防彈之衣」也。安卓之測分三層，新手先精究其第一層：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">層級</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">所測何物</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">置於何所</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">遲速</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">單元測試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">純邏輯（計算、校驗）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/test/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">秒級</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">儀器測試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真機之上界面之行</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/androidTest/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分鐘級</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">手動測試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真人之感、體驗</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">恆須之</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
測試三層

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 單元測試示例</span><span class="dots">···</span>
:::

```
// 將"金額字符串轉數字"此種邏輯抽成純函數
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

記賬冊中金額之校驗、統計之算，皆當有單元測試罩之。行測試：右鍵 test 目錄 → Run。綠而皆過，則可安然而改碼矣。

#### 三、簽名打包：為 App 蓋「印」

安卓要求凡安裝之包必簽之——猶蓋公印，以證「此包吾所出，未遭改竄」。調試時 Android Studio 自用 debug 之簽；發佈須用己之 release 簽。其序：

1. 菜單 Build → Generate Signed Bundle / APK；
2. 創 keystore 之文件（密鑰之庫）——設其密碼而妥藏之；
3. 擇 release + AAB 之式，構建乃成。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
避坑之警：keystore 失則 App 失

{class="mt-1"}
上架之後更新 App，必用同一之簽，否則店將拒其新。keystore 之文件與密碼一失，汝惟易新應用而重上架——舊用戶皆無由接焉。務以 keystore 與密碼備於安隱之所（雲盤加密 + 記事之冊），此安卓開發者至昂之教訓之一也。
:::

#### 四、上架 Google Play 之全程

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> 註冊開發者賬號</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> 準備商店素材</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> 上傳 AAB</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> 填數據安全表</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> 審覈（數小時~數天）</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> 上架</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 6：Google Play 上架六步
:::

- 註冊：一次 25 美元之註冊費，須可用之 Google 賬號；
- 素材：應用之圖標（512×512）、截圖（至少二張）、功能之述、私隱政策之鏈（收數據者必填）；
- 數據安全之表：如實申報所收何數據——不連網之記賬冊可「零收集」；
- 審核：新賬號首番上架恆為人工所審，數時至數日不等，見駁則依議而改。

國內之用戶慎之：Google Play 須特殊網絡之境，且中國大陸之分發常行國內之店（華為、小米、應用寶之屬）。上架國內之店，其程相類，然各店自有其審之好——同一 AAB/APK 可分發於多店。以為練手，先通一家即勝矣。

#### 五、商店素材何由製之：第一印象即繫下載之數

商店頁者，用戶遊店之時所見之櫥窗也。三材定其第一印象：

- 圖標：512×512，勿以截圖充數。若無設計之能，可以 AI 之器生簡潔幾何之形，縮於手機桌面之上猶能一望而識者，方為合格；
- 截圖：至少二張，以四至六張為佳，以彰最核心之功能場景；每張配一淺白之語（「一秒記一筆」勝「高效記帳之方」十倍）；
- 描述：首句當明「此為何物、予誰用之」，勿堆「最專、最強」之詞——商店搜索之權重，主視關鍵詞與下載轉化，誠實勝於誇張。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小訣：以 A/B 之法觀同行

{class="mt-1"}
上架之前，遍觀商店同類 App 之前十名，取其截圖比而較之：其圖標何風？其截圖售何賣點？其標題何書？模仿非抄襲也——學其套路而易以己之內容，此凡產品冷啟動至速之一課也。
:::

#### 六、性能優化與崩潰上報小清單

App 上架之前，此二事宜各費半小時為之：

##### 一、性能自察四條

1. 列表當用 LazyColumn：長列切莫以 Column 強排之——懶載者，安卓性能之第一課也；
2. 圖勿硬塞原圖：當用 Coil 圖庫自動縮放而緩存之，一張 5MB 之原圖足以令低階之機滯塞；
3. 勿於主線程任重事：數據庫、網絡、大文件皆當於協程中為之；
4. 當以 Profiler 量之：Android Studio 自帶之性能分析器能觀記憶體、CPU、耗電——先測而後優，勿憑感覺。

##### 二、崩潰上報

爾測試之時不崩，非謂用戶之機不崩也。上架之前，當接 Firebase Crashlytics（谷歌官方之物，免費）：配置數行，用戶崩潰則自動上報堆棧，爾於後台即可見「何機型、何版本、崩於何行」。無崩潰監控而上架者，猶閉目而駕車也。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：將記帳本「交付」一次

{class="mt-1"}
① 為 parseAmount 諸邏輯補單元測試三則；② 以 Logcat 親捕自造之崩潰一處而修之；③ 生 release 簽名之 APK 一枚，致諸友朋安裝之（此乃「作品」之儀也）；④ 力有餘則註冊開發者之號，以記帳本真呈上架。前三條今夕可竟。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 調試之三技：Logcat 觀日誌、斷點觀變量、Layout Inspector 觀界面
- 讀崩潰：自堆棧之下而上，覓己包名之首行
- 測試三層：單元（秒級，先學此）/儀器/手動
- 發布必簽名：keystore 與密碼宜善備份之，失之則 App「易主」矣
- 上架六步：註冊 → 素材 → 上傳 AAB → 數據安全表 → 審核 → 上架
:::
