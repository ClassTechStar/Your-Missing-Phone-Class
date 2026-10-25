---
id: di-er-shi-si-zhang
num: 24
part: chao-yue-pian
nav: 第二十四章：Root權限與BL鎖深度解析
toc: default
kind: chapter
---

### 第二十四章：Root權限與BL鎖深析

{class="chapter-intro mb-4"}
此章乃對第二十章內容之深入擴展，適彼等欲真正理解手機底層機制、甚至嘗試刷機之用戶。請注意，此等操作有一定風險，請謹慎行之。

#### 一、深入理解Bootloader

Bootloader乃手機啓動時首個運行之程序，其任務乃初始化硬件、加載操作系統內核。君可將Bootloader視爲手機之"守門人"。

##### BL鎖之工作原理：

- <strong>驗證簽名</strong>：BL鎖將驗證啓動鏡像之數字簽名，唯廠商簽名之系統方能啓動。
- <strong>防止降級</strong>：防用戶刷入舊版本系統以利用已知漏洞。
- <strong>保護數據</strong>：即使刷入新系統，無原賬號密碼亦無法訪問用戶數據。

##### 🔐 硬件級存儲與驗證

BL鎖之鎖定狀態（Locked/Unlocked）及廠商之公鑰，通常存儲於受保護之硬件區域（如高通之 devinfo 分區、eFuse 或 RPMB 分區），防止爲軟件篡改。每次啓動時，Bootloader 將從此安全區域讀取狀態，並據此決定為否執行嚴格之簽名驗證。

##### 🔏 數字簽名驗證

廠商於發佈系統更新或鏡像時，將用自己之私鑰對其進行簽名。設備啓動時，Bootloader 將使用內置之公鑰對系統鏡像（如 boot.img、recovery.img）進行驗證。它之工作方式乃：

1. 對系統鏡像復算哈希值。
2. 用公鑰解密鏡像自帶之簽名，得到一個哈希值。
3. 比較此兩個哈希值，若一致則通過驗證。此確保矣系統鏡像未爲第三方篡改。

##### 🔗 安全啓動鏈

BL鎖乃整個安全啓動鏈之第一環。它驗證通過後，方將加載並執行下一階段之引導程序（如內核），從而層層確保系統啓動環境之可信。

##### 📊 鎖定 vs 解鎖：BL鎖之雙面影響

爲了更直觀地理解 BL 鎖之利弊，我等用一個對比表來展示它於 5 個核心維度上之差異：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 dark:border-gray-600 text-sm">
                            <thead>
                                <tr class="bg-gray-100 dark:bg-gray-800">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">核心作用</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">鎖定狀態（默認）</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">解鎖後狀態</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">系統安全</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">防止刷入未簽名之非官方系統，保護系統完整性與底層安全<br><span class="text-emerald-600 dark:text-emerald-400">✅ 高安全：僅加載官方簽名鏡像，有效抵禦惡意固件篡改</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ 安全降低：允許刷入第三方 ROM，系統完整性校驗機制失效，惡意軟件若獲取 Root 權限可深度篡改系統</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">系統穩定性</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">確保手機運行經過廠商測試與優化之官方系統，保障穩定流暢<br><span class="text-emerald-600 dark:text-emerald-400">✅ 穩定：使用官方固件，功能完整，OTA 升級可靠</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ 風險增加：第三方 ROM 或存在兼容性問題，或導致系統崩潰、變磚、硬件功能異常（如攝像頭、快充），OTA 更新或失敗</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">保修權益</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">廠商通過鎖定 BL 提供穩定之官方系統，以提供保修服務<br><span class="text-emerald-600 dark:text-emerald-400">✅ 保修有效：享受官方免費保修服務（非人爲損壞）</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ 保修失效：絕大多數廠商將解鎖 BL 視爲主動放棄保修之行爲，縱重新上鎖，亦或爲檢測出歷史解鎖記錄而拒保</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">數據安全</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">解鎖過程通常強制清除數據，防止舊數據於新系統環境下爲惡意利用<br><span class="text-emerald-600 dark:text-emerald-400">✅ 數據安全：日常使用中，BL 鎖限制了惡意程序對系統分區之修改能力</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ 數據風險：解鎖時將強制清除所有用戶數據；若解鎖後未正確加密，數據存儲或不安全；丟失後更易爲刷機提取數據</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">功能限制</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">確保依賴安全環境之功能（如支付、銀行 App）正常運行<br><span class="text-emerald-600 dark:text-emerald-400">✅ 功能完整：所有官方功能均可正常使用</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ 功能受限：部分安全敏感應用（如 Google Pay、銀行 App）或因檢測至 BL 解鎖狀態而拒絕運行；DRM 服務或降級，影響高清視頻播放</span></td>
                                </tr>
                            </tbody>
                        </table>
```
:::

#### 二、解鎖BL鎖之詳細流程（以小米爲例）

1. <strong>申請解鎖權限</strong>：於小米解鎖工具網站申請解鎖。
2. <strong>綁定賬號</strong>：於手機設置中綁定小米賬號。
3. <strong>等待期</strong>：依賬號等級，須等待7-30日。
4. <strong>解鎖操作</strong>：用小米解鎖工具連接電腦解鎖。

#### 三、Root之多種方案

- <strong>Magisk</strong>：現代Root方案，Systemless設計，可隱藏Root狀態。
- <strong>Kernelsu</strong>：基於內核之Root方案，更底層，隱藏性更好。
- <strong>SuperSU</strong>：老牌Root方案，目前已停止更新。

#### 四、刷機入門

刷機乃指予手機安裝新之操作系統。常見之刷機類型：

- <strong>刷官方ROM</strong>：安裝官方系統，用於救磚或降級。
- <strong>刷第三方Recovery</strong>：如TWRP，用於備份恢復、刷入第三方ROM。
- <strong>刷第三方ROM</strong>：如LineageOS、Pixel Experience等，體驗不同之系統。

#### 五、三星Knox：BL解鎖之不可逆代價

與其他安卓廠商不同，三星手機之BL解鎖機制有一個獨特之"熔斷"設計：<strong>對於三星手機來說，解鎖將觸發Knox熔斷，永久失去部分安全功能（如Samsung Pay）；將清除所有受保護數據；影響保修</strong>。具體來說：

- <strong>熔斷器乃一次性之</strong>：手機內部有一顆 eFuse 熔絲，一旦檢測至 BL 爲解鎖遂將永久燒斷，無法恢復。
- <strong>受影響之功能</strong>：Samsung Pay（公交卡/銀行卡）、Knox 安全文件夾、企業 MDM 管控、部分健康保險類 App 皆將失效。
- <strong>強制清空數據</strong>：熔斷觸發後手機會強制恢復出廠設置，所有本地數據爲擦除（雲端數據不受影響）。
- <strong>保修影響</strong>：官方明確表示 Knox 熔斷後不再享受保修服務。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>三思而後行

{class="mt-1"}
三星之 Knox 熔斷乃<strong>不可逆</strong>之，一旦觸發遂回不去原廠狀態。若汝只為欲用一些原本須 Root 之功能，建議先查查有無不須 Root 之替代方案。
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>重要警告

{class="mt-1"}
刷機有風險，操作需謹慎。或導致：

{class="list-disc pl-6 mt-1 space-y-1"}
- 手機變磚（無法開機）
- 失去保修
- 數據丟失
- 支付功能異常

{class="mt-1"}
刷機前務必做好完整備份，細讀教程，確認機型與版本匹配。
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>推薦資源

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>XDA Developers</strong>：全球最大之安卓開發者社區，有豐富之刷機教程與ROM資源。
- <strong>酷安</strong>：國內知名之數碼社區，有多中文教程與討論。
- <strong>各機型論壇</strong>：如小米社區、一加社區等，有官方與民間教程。
:::

#### 六、常見問題解答（Q&amp; A）

::: div .qa-item .mt-3
{class="font-semibold mb-1"}
<i class="fas fa-question-circle text-primary mr-1"></i>Q1：解鎖BL鎖後還能恢復嗎？

{class="mb-2 pl-6"}
<strong>A：</strong>可重新上鎖。通常須刷入官方完整之線刷包，並使用特定之刷機腳本（如小米之 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">flash_all_lock.bat</code>）即可重新上鎖。但注意，重新上鎖後，因解鎖而觸發之一些安全熔斷（如三星之Knox）或無法逆轉。
:::

::: div .qa-item .mt-3
{class="font-semibold mb-1"}
<i class="fas fa-question-circle text-primary mr-1"></i>Q2：解鎖後何以Root？

{class="mb-2 pl-6"}
<strong>A：</strong>解鎖BL鎖只為第一步。Root通常須：

{class="list-decimal pl-12 mb-2 space-y-1"}
1. 刷入自定義Recovery（如TWRP）。
2. 經由Recovery刷入Magisk等Root管理器來修補boot鏡像，遂得Root權限。
:::
