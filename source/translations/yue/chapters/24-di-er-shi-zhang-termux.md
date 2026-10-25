---
id: di-er-shi-zhang-termux
part: jin-jie-pian
nav:  附：Termux便攜式Linux終端
toc: sub
kind: supplement
---

### 第二十章附：Termux——Android設備上嘅便攜式Linux終端環境

{class="chapter-intro mb-4"}
如果你覺得開發者模式仲唔夠「硬核」，想要喺手機上體驗完整嘅Linux命令行，咁Termux正係為你準備嘅。佢無需root權限，就可以將一臺普通嘅安卓手機變成一臺便攜嘅Linux工作站，係進階用戶探索流動端開發與運維嘅利器。

#### 一、乜嘢係Termux

Termux係一款專為Android設備設計嘅開源終端模擬器同Linux環境應用程式，佢無需root權限即可喺手機上提供完整嘅Linux shell體驗。作為一個輕量級應用（安裝包淨係30MB左右），Termux通過APT包管理系統支援豐富嘅軟件生態，允許用戶喺流動設備上運行Python、Node.js、Git、SSH等工具，甚至搭建伺服器或進行滲透測試。

Termux嘅核心優勢喺於輕量化同高度可擴展性，適合開發、學習及系統管理等多種場景。佢將標準嘅軟件包同精確嘅終端仿真結合喺一個開源解決方案中。

#### 二、核心功能與特性

##### 🖥️ 完整嘅Linux環境

Termux<strong>淨係內置Bash</strong>呢一種Shell。如果想使用Zsh或fish等其他Shell，需要通過包管理器手動安裝，例如：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install zsh</code>或<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install fish</code>。同時Termux支援Vim、Nano、Emacs等編輯器，提供接近原生嘅命令行體驗。用戶可以通過"pkg install"安裝2000+軟件包，包括GCC、OpenSSH、SQLMap等開發同安全工具。

##### 📦 強大嘅包管理

使用APT包管理器（類似Debian同Ubuntu），可安裝數千種Linux軟件包，涵蓋開發工具、網絡工具等。支援Python、Ruby、Node.js、Go、Rust、Swift等多種編程語言環境。

##### 🔒 安全與網絡功能

- <strong>SSH遠端連接</strong>：支援SSH用戶端同伺服器功能，可遠端連接其他設備或等手機成為SSH主機。
- <strong>加密工具</strong>：提供OpenSSL等加密工具，支援數據加密同安全通信。
- <strong>伺服器搭建</strong>：可配置Nginx或Apache搭建靜態網頁伺服器。

##### 🔧 系統集成與擴展

- 訪問手機存儲權限，實現本地檔案管理。
- 通過Termux:API插件調用傳感器、鏡頭等Android硬件功能。
- 支援藍牙鍵盤同外部顯示器連接，具有完整嘅滑鼠支援。

#### 三、插件生態系統

Termux嘅核心應用程式可以通過幾個可選嘅插件應用進行擴展，提供額外嘅功能同埋集成：

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">插件名稱</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">功能描述</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:API</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">向命令行程式公開Android API功能</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Boot</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">允許喺設備啟動時運行腳本</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Float</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">提供浮動終端視窗</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Styling</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">為終端啟用顏色方案同埋字體自定義</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Tasker</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">將Termux腳本同Tasker自動化應用集成</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Widget</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">允許從主螢幕小工具運行腳本</td>
                            </tr>
                        </tbody>
                    </table>
```

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>重要提示

{class="mt-1"}
Termux同埋佢嘅插件必須從同一來源安裝，因為佢哋共享相同嘅sharedUserId。混合來自唔同來源（如F-Droid同GitHub）嘅安裝會導致安裝錯誤。
:::

#### 四、安裝與配置指南

##### 📥 安裝步驟

1. <strong>下載應用</strong>：從官方渠道（F-Droid或GitHub）下載安裝Termux，無需root權限。
2. <strong>初始化系統</strong>：首次啟動後等待"Installing bootstrap packages"完成。
3. <strong>獲取存儲權限</strong>：執行<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-setup-storage</code>獲取手機檔案系統權限。
4. <strong>更新軟件源</strong>：執行<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code>更新軟件包列表。

##### ⚙️ 基礎優化

- <strong>換鏡像源</strong>：使用<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-change-repo</code>命令通過圖形界面更換鏡像源（推薦清華大學鏡像源）。
- <strong>快捷鍵設定</strong>：音量減鍵模擬Ctrl，音量加鍵模擬Esc，提升輸入效率。
- <strong>界面美化</strong>：安裝Zsh + Oh My Zsh，配置主題同埋插件。

#### 五、典型應用場景

##### 💻 移動開發測試

喺手機上搭建完整嘅開發環境，編寫並運行Python腳本，使用GCC編譯C程式，通過Git管理代碼倉庫，結合SSH同遠程伺服器同步。

##### 🖥️ 伺服器運維

通過SSH遠程管理伺服器，執行系統維護、日誌分析等任務，隨時隨地處理伺服器問題。

##### 📚 學習Linux操作

提供真實嘅Linux環境，係學習命令行同埋系統管理嘅理想平臺，可練習Shell腳本編寫、Linux檔案權限管理（如 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chmod 755</code> 設定 rwxr-xr-x 權限位、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chown user:group</code> 修改檔案歸屬、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls -l</code> 查看 owner/group/other 三組九位權限）等基礎命令。注意呢個係Unix/Linux經典嘅"三組九位"權限模型（owner / group / other × 讀 / 寫 / 執行），同Windows NTFS嘅ACL訪問控制列表係完全唔同嘅兩套體系。

##### 🔐 網絡安全測試

安裝Nmap、SQLMap、Hydra、Metasploit等安全工具，進行網絡掃描同埋滲透測試。

#### 六、版本與兼容性

Termux嘅最新穩定版本係v0.118.2，適用於Android ≥ 7嘅設備。需要注意嘅係，Termux喺Android 12同埋更高版本上可能存在唔穩定性，建議關注官方更新日誌以獲取最新兼容性資訊。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>總結

{class="mt-1"}
Termux將強大嘅Linux終端體驗帶到咗Android設備上，等手機成為一臺便攜嘅開發同埋學習工具。無論係開發者、系統管理員定係技術愛好者，都可以利用Termux喺移動設備上享受完整嘅命令行體驗，實現"口袋入面嘅Linux"呢個理念。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>嚟動手：喺手機上跑通第一條Linux命令

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 從F-Droid下載並安裝Termux，首次啟動等待初始化完成。
2. 執行<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code>更新軟件包。
3. 安裝Python：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install python</code>。
4. 輸入<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python3 -c "print('Hello from Termux!')"</code>，感受喺手機上運行代碼嘅樂趣。
:::
