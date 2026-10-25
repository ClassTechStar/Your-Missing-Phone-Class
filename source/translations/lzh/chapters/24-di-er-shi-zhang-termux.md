---
id: di-er-shi-zhang-termux
part: jin-jie-pian
nav: 次十章附
toc: sub
kind: supplement
---

### 第二十章附：Termux——Android設備上之便攜式Linux終端環境

{class="chapter-intro mb-4"}
若君覺開發者模式尚不夠"硬核"，欲於手機上體驗完整之Linux命令行，則Termux正爲君而備。其無需root權限，即可使一臺尋常安卓手機化爲便攜之Linux工作站，乃進階用戶探索移動端開發與運維之利器。

#### 一、何謂Termux

Termux乃一款專爲Android設備設計之開源終端模擬器與Linux環境應用程序，無需root權限即可於手機上提供完整之Linux shell體驗。作爲一輕量級應用（安裝包僅30MB左右），Termux經APT包管理系統支持豐富之軟件生態，允許用戶於移動設備上運行Python、Node.js、Git、SSH等

Termux之核心優勢在於輕量化與高度可擴展性，適於開發、學習及系統管理等多種場景。其將標準之軟件包與精確之終端仿真結合於一開源解決方案中。

#### 二、核心功能與特性

##### 🖥️ 完整之Linux環境

Termux<strong>僅內置Bash</strong>此一種Shell。若欲使用Zsh或fish等其他Shell，須通過包管理器手動安裝，例如：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install zsh</code>或<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install fish</code>。同時Termux支持Vim、Nano、Emacs等編輯器，提供接近原生之命令行體驗。用戶可通過"pkg install"安裝2000+軟件包，包括GCC、OpenSSH、SQLMap等開發與安全工具。

##### 📦 強大之包管理

使用APT包管理器（類似Debian與Ubuntu），可安裝數千種Linux軟件包，涵蓋開發工具、網絡工具等。支持Python、Ruby、Node.js、Go、Rust、Swift等多種編程語言環境。

##### 🔒 安全與網絡功能

- <strong>SSH遠程連接</strong>：支持SSH客戶端與服務器功能，可遠程連接其他設備或使手機成爲SSH主機。
- <strong>加密工具</strong>：提供OpenSSL等加密工具，支持數據加密與安全通信。
- <strong>服務器搭建</strong>：可配置Nginx或Apache搭建靜態網頁服務器。

##### 🔧 系統集成與擴展

- 訪問手機存儲權限，實現本地文件管理。
- 通過Termux:API插件調用傳感器、攝像頭等Android硬件功能。
- 支持藍牙鍵盤與外接顯示器連接，具完整之鼠標支持。

#### 三、插件生態系統

Termux之核心應用程序可通過幾個可選之插件應用進行擴展，提供額外之功能與集成：

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
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">向命令行程序公開Android API功能</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Boot</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">允許於設備啓動時運行腳本</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Float</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">提供浮動終端窗口</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Styling</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">爲終端啓用顏色方案與字體自定義</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Tasker</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">將Termux腳本與Tasker自動化應用集成</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Widget</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">允許自主屏幕小部件運行腳本</td>
                            </tr>
                        </tbody>
                    </table>
```

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>重要提示

{class="mt-1"}
Termux及其插件必須自同一來源安裝，因其共享相同之sharedUserId。混合來自不同來源（如F-Droid與GitHub）之安裝將導致安裝錯誤。
:::

#### 四、安裝與配置指南

##### 📥 安裝步驟

1. <strong>下載應用</strong>：從官方渠道（F-Droid或GitHub）下載安裝Termux，無需root權限。
2. <strong>初始化系統</strong>：首次啓動後等待"Installing bootstrap packages"完成。
3. <strong>獲取存儲權限</strong>：執行<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-setup-storage</code>獲取手機文件系統權限。
4. <strong>更新軟件源</strong>：執行<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code>更新軟件包列表。

##### ⚙️ 基礎優化

- <strong>換鏡像源</strong>：使用<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-change-repo</code>命令通過圖形界面更換鏡像源（推薦清華大學鏡像源）。
- <strong>快捷鍵設置</strong>：音量減鍵模擬Ctrl，音量加鍵模擬Esc，提升輸入效率。
- <strong>界面美化</strong>：安裝Zsh + Oh My Zsh，配置主題與插件。

#### 五、典型應用場景

##### 💻 移動開發測試

於手機上搭建完整之開發環境，編寫並運行Python腳本，使用GCC編譯C程序，通過Git管理代碼倉庫，結合SSH與遠程服務器同步。

##### 🖥️ 服務器運維

通過SSH遠程管理服務器，執行系統維護、日誌分析等任務，隨時隨地處理服務器問題。

##### 📚 學習Linux操作

提供真實之Linux環境，乃學習命令行與系統管理之理想平臺，可練習Shell腳本編寫、Linux文件權限管理（如 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chmod 755</code> 設 rwxr-xr-x 權限位、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chown user:group</code> 改文歸屬、<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls -l</code> 查看 owner/group/other 三組九位權限）等基礎命令。注意此乃Unix/Linux經典之"三組九位"權限模型（owner / group / other × 讀 / 寫 / 執行），與Windows NTFS之ACL訪問控制列表乃完全不同之兩套體系。

##### 🔐 網絡安全測試

安裝Nmap、SQLMap、Hydra、Metasploit等安全工具，進行網絡掃描與滲透測試。

#### 六、版本與兼容性

Termux之最新穩定版本乃v0.118.2，適用於Android ≥ 7之設備。需注意者，Termux於Android 12及更高版本上或存不穩定性，建議留意官方更新日誌以獲取最新兼容性信息。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>總結

{class="mt-1"}
Termux將強健之Linux終端體驗攜至Android設備之上，使手機化爲便攜之開發與修習利器。無論開發者、系統管理員抑或技術愛好者，皆可借Termux於移動設備上盡享完整之命令行體驗，以成"袖中Linux"之理念。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>試爲之：於手機上運行首條Linux命令

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 自F-Droid下載並安裝Termux，初啓以待其初始化完畢。
2. 執行<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code>以更新軟件包。
3. 安裝Python：<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install python</code>。
4. 輸入<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python3 -c "print('Hello from Termux!')"</code>，以領略於手機上運行代碼之樂。
:::
