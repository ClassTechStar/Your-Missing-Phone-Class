---
id: di-er-shi-si-zhang
num: 24
part: chao-yue-pian
nav: 第二十四章：Root權限與BL鎖深度解析
toc: default
kind: chapter
---

### 第二十四章：Root權限與BL鎖深度解析

{class="chapter-intro mb-4"}
呢一章係對第二十章內容嘅深入擴展，適合嗰啲想要真正理解手機底層機制、甚至嘗試刷機嘅用戶。請注意，呢啲操作有一定風險，請謹慎行事。

#### 一、深入理解Bootloader

Bootloader係手機啟動時第一個運行嘅程式，佢嘅任務係初始化硬件、載入作業系統內核。可以將Bootloader理解為手機嘅「守門人」。

##### BL鎖嘅工作原理：

- <strong>驗證簽名</strong>：BL鎖會驗證啟動鏡像嘅數碼簽名，只有廠商簽名嘅系統先至可以啟動。
- <strong>防止降級</strong>：防止用戶刷入舊版本系統嚟利用已知漏洞。
- <strong>保護數據</strong>：即使刷入新系統，冇原帳號密碼亦無法訪問用戶數據。

##### 🔐 硬件級儲存與驗證

BL鎖嘅鎖定狀態（Locked/Unlocked）及廠商嘅公鑰，通常儲存喺受保護嘅硬件區域（如高通嘅 devinfo 分區、eFuse 或 RPMB 分區），防止被軟件篡改。每次啟動時，Bootloader 會由呢個安全區域讀取狀態，並據此決定係咪執行嚴格嘅簽名驗證。

##### 🔏 數碼簽名驗證

廠商喺發布系統更新或鏡像時，會用自己嘅私鑰對佢進行簽名。設備啟動時，Bootloader 會使用內置嘅公鑰對系統鏡像（如 boot.img、recovery.img）進行驗證。佢嘅工作方式係：

1. 對系統鏡像重新計算哈希值。
2. 用公鑰解密鏡像自帶嘅簽名，得到一個哈希值。
3. 比較呢兩個哈希值，若一致則通過驗證。呢個確保咗系統鏡像未被第三方篡改。

##### 🔗 安全啟動鏈

BL鎖係整個安全啟動鏈嘅第一環。佢驗證通過後，先至會載入並執行下一階段嘅引導程式（如內核），從而層層確保系統啟動環境嘅可信。

##### 📊 鎖定 vs 解鎖：BL鎖嘅雙面影響

為咗更直觀咁理解 BL 鎖嘅利弊，我哋用一個對比表嚟展示佢喺 5 個核心維度上嘅差異：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 dark:border-gray-600 text-sm">
                            <thead>
                                <tr class="bg-gray-100 dark:bg-gray-800">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">核心作用</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">鎖定狀態（預設）</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">解鎖後狀態</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">系統安全</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">防止刷入未簽名嘅非官方系統，保護系統完整性與底層安全<br><span class="text-emerald-600 dark:text-emerald-400">✅ 高安全：僅載入官方簽名鏡像，有效抵禦惡意韌體篡改</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ 安全降低：允許刷入第三方 ROM，系統完整性校驗機制失效，惡意軟件若攞到 Root 權限可深度篡改系統</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">系統穩定性</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">確保手機運行經過廠商測試同優化嘅官方系統，保障穩定流暢<br><span class="text-emerald-600 dark:text-emerald-400">✅ 穩定：使用官方韌體，功能完整，OTA 升級可靠</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ 風險增加：第三方 ROM 可能存在相容性問題，可能導致系統崩潰、變磚、硬件功能異常（如鏡頭、快充），OTA 更新可能失敗</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">保修權益</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">廠商透過鎖定 BL 提供穩定嘅官方系統，以提供保修服務<br><span class="text-emerald-600 dark:text-emerald-400">✅ 保修有效：享受官方免費保修服務（非人為損壞）</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ 保修失效：絕大多數廠商將解鎖 BL 視為主動放棄保修嘅行為，即使重新上鎖，亦可能被檢測出歷史解鎖記錄而拒保</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">數據安全</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">解鎖過程通常強制清除數據，防止舊數據喺新系統環境下被惡意利用<br><span class="text-emerald-600 dark:text-emerald-400">✅ 數據安全：日常使用中，BL 鎖限制咗惡意程式對系統分區嘅修改能力</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ 數據風險：解鎖時會強制清除所有用戶數據；若解鎖後未正確加密，數據儲存可能唔安全；遺失後更易被刷機提取數據</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">功能限制</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">確保依賴安全環境嘅功能（如支付、銀行 App）正常運行<br><span class="text-emerald-600 dark:text-emerald-400">✅ 功能完整：所有官方功能均可正常使用</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ 功能受限：部分安全敏感應用（如 Google Pay、銀行 App）可能因檢測到 BL 解鎖狀態而拒絕運行；DRM 服務可能降級，影響高清影片播放</span></td>
                                </tr>
                            </tbody>
                        </table>
```
:::

#### 二、解鎖BL鎖嘅詳細流程（以小米為例）

1. <strong>申請解鎖權限</strong>：喺小米解鎖工具網站申請解鎖。
2. <strong>綁定帳號</strong>：喺手機設定中綁定小米帳號。
3. <strong>等待期</strong>：根據帳號等級，需要等待7-30日。
4. <strong>解鎖操作</strong>：使用小米解鎖工具連接電腦解鎖。

#### 三、Root嘅多種方案

- <strong>Magisk</strong>：現代Root方案，Systemless設計，可隱藏Root狀態。
- <strong>Kernelsu</strong>：基於內核嘅Root方案，更底層，隱藏性更好。
- <strong>SuperSU</strong>：老牌Root方案，而家已經停止更新。

#### 四、刷機入門

刷機係指畀手機安裝新嘅作業系統。常見嘅刷機類型：

- <strong>刷官方ROM</strong>：安裝官方系統，用於救磚或降級。
- <strong>刷第三方Recovery</strong>：如TWRP，用於備份恢復、刷入第三方ROM。
- <strong>刷第三方ROM</strong>：如LineageOS、Pixel Experience等，體驗唔同嘅系統。

#### 五、三星Knox：BL解鎖嘅不可逆代價

同其他安卓廠商唔同，三星手機嘅BL解鎖機制有一個獨特嘅「熔斷」設計：<strong>對於三星手機嚟講，解鎖會觸發Knox熔斷，永久失去部分安全功能（如Samsung Pay）；會清除所有受保護數據；影響保修</strong>。具體嚟講：

- <strong>熔斷器係一次性嘅</strong>：手機內部有一顆 eFuse 熔絲，一旦檢測到 BL 被解鎖就會永久燒斷，無法恢復。
- <strong>受影響嘅功能</strong>：Samsung Pay（公交卡/銀行卡）、Knox 安全資料夾、企業 MDM 管控、部分健康保險類 App 都會失效。
- <strong>強制清空數據</strong>：熔斷觸發後手機會強制恢復出廠設定，所有本地數據被擦除（雲端數據唔受影響）。
- <strong>保修影響</strong>：官方明確表示 Knox 熔斷後唔再享受保修服務。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>三思而後行

{class="mt-1"}
三星嘅 Knox 熔斷係<strong>不可逆</strong>嘅，一旦觸發就返唔到原廠狀態。如果你淨係想用一啲原本需要 Root 嘅功能，建議先查嚇有冇唔需要 Root 嘅替代方案。
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>重要警告

{class="mt-1"}
刷機有風險，操作需謹慎。可能導致：

{class="list-disc pl-6 mt-1 space-y-1"}
- 手機變磚（無法開機）
- 失去保修
- 數據丟失
- 支付功能異常

{class="mt-1"}
刷機前務必做好完整備份，仔細閲讀教程，確認機型同版本匹配。
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>推薦資源

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>XDA Developers</strong>：全球最大嘅安卓開發者社區，有豐富嘅刷機教程同ROM資源。
- <strong>酷安</strong>：國內知名嘅數碼社區，有好多中文教程同討論。
- <strong>各機型論壇</strong>：如小米社區、一加社區等，有官方同民間教程。
:::

#### 六、常見問題解答（Q&amp; A）

::: div .qa-item .mt-3
{class="font-semibold mb-1"}
<i class="fas fa-question-circle text-primary mr-1"></i>Q1：解鎖BL鎖後仲能恢復嗎？

{class="mb-2 pl-6"}
<strong>A：</strong>可以重新上鎖。通常需要刷入官方完整嘅線刷包，並使用特定嘅刷機腳本（如小米嘅 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">flash_all_lock.bat</code>）即可重新上鎖。但注意，重新上鎖後，因解鎖而觸發嘅一啲安全熔斷（如三星嘅Knox）可能無法逆轉。
:::

::: div .qa-item .mt-3
{class="font-semibold mb-1"}
<i class="fas fa-question-circle text-primary mr-1"></i>Q2：解鎖後如何Root？

{class="mb-2 pl-6"}
<strong>A：</strong>解鎖BL鎖淨係第一步。Root通常需要：

{class="list-decimal pl-12 mb-2 space-y-1"}
1. 刷入自訂Recovery（如TWRP）。
2. 透過Recovery刷入Magisk等Root管理器嚟修補boot鏡像，從而攞到Root權限。
:::
