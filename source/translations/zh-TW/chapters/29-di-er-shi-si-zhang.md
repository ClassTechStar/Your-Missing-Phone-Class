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
這一章是對第二十章內容的深入擴充，適合那些想要真正理解手機底層機制、甚至嘗試刷機的使用者。請注意，這些操作有一定風險，請謹慎行事。

#### 一、深入理解Bootloader

Bootloader是手機啟動時第一個執行的程式，它的任務是初始化硬體、載入作業系統核心。可以把Bootloader理解為手機的"守門人"。

##### BL鎖的工作原理：

- <strong>驗證簽名</strong>：BL鎖會驗證啟動映象的數字簽名，只有廠商簽名的系統才能啟動。
- <strong>防止降級</strong>：防止使用者刷入舊版本系統來利用已知漏洞。
- <strong>保護資料</strong>：即使刷入新系統，沒有原帳號密碼也無法訪問使用者資料。

##### 🔐 硬體級儲存與驗證

BL鎖的鎖定狀態（Locked/Unlocked）及廠商的公鑰，通常儲存在受保護的硬體區域（如高通的 devinfo 分割區、eFuse 或 RPMB 分割區），防止被軟體篡改。每次啟動時，Bootloader 會從此安全區域讀取狀態，並據此決定是否執行嚴格的簽名驗證。

##### 🔏 數字簽名驗證

廠商在釋出系統更新或映象時，會用自己的私鑰對其進行簽名。裝置啟動時，Bootloader 會使用內建的公鑰對系統映象（如 boot.img、recovery.img）進行驗證。它的工作方式是：

1. 對系統映象重新計算雜湊值。
2. 用公鑰解密映象自帶的簽名，得到一個雜湊值。
3. 比較這兩個雜湊值，若一致則透過驗證。這確保了系統映象未被第三方篡改。

##### 🔗 安全啟動鏈

BL鎖是整個安全啟動鏈的第一環。它驗證透過後，才會載入並執行下一階段的載入程式（如核心），從而層層確保系統啟動環境的可信。

##### 📊 鎖定 vs 解鎖：BL鎖的雙面影響

為了更直觀地理解 BL 鎖的利弊，我們用一個對比表來展示它在 5 個核心維度上的差異：

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
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">防止刷入未簽名的非官方系統，保護系統完整性與底層安全<br><span class="text-emerald-600 dark:text-emerald-400">✅ 高安全：僅載入官方簽名映象，有效抵禦惡意韌體篡改</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ 安全降低：允許刷入第三方 ROM，系統完整性校驗機制失效，惡意軟體若獲取 Root 權限可深度篡改系統</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">系統穩定性</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">確保手機執行經過廠商測試和最佳化的官方系統，保障穩定流暢<br><span class="text-emerald-600 dark:text-emerald-400">✅ 穩定：使用官方韌體，功能完整，OTA 升級可靠</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ 風險增加：第三方 ROM 可能存在相容性問題，可能導致系統崩潰、變磚、硬體功能異常（如攝像頭、快充），OTA 更新可能失敗</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">保修權益</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">廠商透過鎖定 BL 提供穩定的官方系統，以提供保修服務<br><span class="text-emerald-600 dark:text-emerald-400">✅ 保修有效：享受官方免費保修服務（非人為損壞）</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ 保修失效：絕大多數廠商將解鎖 BL 視為主動放棄保修的行為，即使重新上鎖，也可能被檢測出歷史解鎖記錄而拒保</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">資料安全</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">解鎖過程通常強制清除資料，防止舊資料在新系統環境下被惡意利用<br><span class="text-emerald-600 dark:text-emerald-400">✅ 資料安全：日常使用中，BL 鎖限制了惡意程式對系統分割區的修改能力</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ 資料風險：解鎖時會強制清除所有使用者資料；若解鎖後未正確加密，資料儲存可能不安全；丟失後更易被刷機提取資料</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">功能限制</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">確保依賴安全環境的功能（如支付、銀行 App）正常執行<br><span class="text-emerald-600 dark:text-emerald-400">✅ 功能完整：所有官方功能均可正常使用</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ 功能受限：部分安全敏感應用（如 Google Pay、銀行 App）可能因檢測到 BL 解鎖狀態而拒絕執行；DRM 服務可能降級，影響高畫質影片播放</span></td>
                                </tr>
                            </tbody>
                        </table>
```
:::

#### 二、解鎖BL鎖的詳細流程（以小米為例）

1. <strong>申請解鎖權限</strong>：在小米解鎖工具網站申請解鎖。
2. <strong>繫結帳號</strong>：在手機設定中繫結小米帳號。
3. <strong>等待期</strong>：根據帳號等級，需要等待7-30天。
4. <strong>解鎖操作</strong>：使用小米解鎖工具連線電腦解鎖。

#### 三、Root的多種方案

- <strong>Magisk</strong>：現代Root方案，Systemless設計，可隱藏Root狀態。
- <strong>Kernelsu</strong>：基於核心的Root方案，更底層，隱藏性更好。
- <strong>SuperSU</strong>：老牌Root方案，目前已停止更新。

#### 四、刷機入門

刷機是指給手機安裝新的作業系統。常見的刷機型別：

- <strong>刷官方ROM</strong>：安裝官方系統，用於救磚或降級。
- <strong>刷第三方Recovery</strong>：如TWRP，用於備份恢復、刷入第三方ROM。
- <strong>刷第三方ROM</strong>：如LineageOS、Pixel Experience等，體驗不同的系統。

#### 五、三星Knox：BL解鎖的不可逆代價

與其他安卓廠商不同，三星手機的BL解鎖機制有一個獨特的"熔斷"設計：<strong>對於三星手機來說，解鎖會觸發Knox熔斷，永久失去部分安全功能（如Samsung Pay）；會清除所有受保護資料；影響保修</strong>。具體來說：

- <strong>熔斷器是一次性的</strong>：手機內部有一顆 eFuse 熔絲，一旦檢測到 BL 被解鎖就會永久燒斷，無法恢復。
- <strong>受影響的功能</strong>：Samsung Pay（公交卡/銀行卡）、Knox 安全資料夾、企業 MDM 管控、部分健康保險類 App 都會失效。
- <strong>強制清空資料</strong>：熔斷觸發後手機會強制恢復出廠設定，所有本地資料被擦除（雲端資料不受影響）。
- <strong>保修影響</strong>：官方明確表示 Knox 熔斷後不再享受保修服務。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>三思而後行

{class="mt-1"}
三星的 Knox 熔斷是<strong>不可逆</strong>的，一旦觸發就回不去原廠狀態。如果你只是想用一些原本需要 Root 的功能，建議先查查有沒有不需要 Root 的替代方案。
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>重要警告

{class="mt-1"}
刷機有風險，操作需謹慎。可能導致：

{class="list-disc pl-6 mt-1 space-y-1"}
- 手機變磚（無法開機）
- 失去保修
- 資料丟失
- 支付功能異常

{class="mt-1"}
刷機前務必做好完整備份，仔細閱讀教程，確認機型和版本匹配。
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>推薦資源

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>XDA Developers</strong>：全球最大的安卓開發者社群，有豐富的刷機教程和ROM資源。
- <strong>酷安</strong>：國內知名的數碼社群，有很多中文教程和討論。
- <strong>各機型論壇</strong>：如小米社群、一加社群等，有官方和民間教程。
:::

#### 六、常見問題解答（Q&amp; A）

::: div .qa-item .mt-3
{class="font-semibold mb-1"}
<i class="fas fa-question-circle text-primary mr-1"></i>Q1：解鎖BL鎖後還能恢復嗎？

{class="mb-2 pl-6"}
<strong>A：</strong>可以重新上鎖。通常需要刷入官方完整的線刷包，並使用特定的刷機指令碼（如小米的 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">flash_all_lock.bat</code>）即可重新上鎖。但注意，重新上鎖後，因解鎖而觸發的一些安全熔斷（如三星的Knox）可能無法逆轉。
:::

::: div .qa-item .mt-3
{class="font-semibold mb-1"}
<i class="fas fa-question-circle text-primary mr-1"></i>Q2：解鎖後如何Root？

{class="mb-2 pl-6"}
<strong>A：</strong>解鎖BL鎖只是第一步。Root通常需要：

{class="list-decimal pl-12 mb-2 space-y-1"}
1. 刷入自定義Recovery（如TWRP）。
2. 透過Recovery刷入Magisk等Root管理器來修補boot映象，從而獲取Root權限。
:::
