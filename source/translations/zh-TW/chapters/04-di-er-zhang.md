---
id: di-er-zhang
num: 02
part: ji-chu-pian
nav: 第二章：整理你的數字房間
toc: default
kind: chapter
---

### 第二章：整理你的數字房間——檔案管理

{class="chapter-intro mb-4"}
手機用久了會亂，好習慣從管理檔案開始。就像你的房間需要定期整理一樣，你的數字空間也需要打理。一個井井有條的手機，不僅找東西方便，執行也更流暢。

#### 一、三層儲存體系：你的數字倉庫

{class="list-decimal pl-6 mb-3 space-y-2"}
1. <strong>機身儲存</strong>：核心區，速度快，系統和App都在這。這是你手機最寶貴的空間，要精打細算。
2. <strong>SD卡（如果支援）</strong>：擴充衣櫃，速度慢點，適合放電影、照片等大檔案。注意：現在很多旗艦機不支援SD卡了。
3. <strong>雲端儲存</strong>：保險櫃+同步網盤。防丟失，也能在多個裝置間同步。iCloud、百度網盤、OneDrive都是常用選擇。

#### 二、認識"檔案管理器"

安卓一般有個 [檔案] 或 [檔案管理] App，iOS是自帶的 [檔案] App。它們是你檢視手機所有檔案的"資源管理器"。

##### 常見資料夾含義：

- <strong>DCIM</strong>：相機拍攝的照片和影片。
- <strong>Pictures</strong>：其他圖片，如截圖、儲存的圖片。
- <strong>Download</strong>：瀏覽器下載的檔案。
- <strong>Music</strong>：音樂檔案。
- <strong>Movies</strong>：影片檔案。
- <strong>Documents</strong>：文件檔案。
- <strong>Android</strong>：安卓系統資料夾，裡面是各App的資料，一般不要手動刪除。

#### 三、檔案系統結構：深入瞭解

安卓基於Linux，檔案系統有一定的層級結構。雖然普通使用者不需要深入瞭解，但知道一些基本概念有幫助。

##### 儲存分割區：

- <strong>/system</strong>：系統分割區，存放作業系統檔案。普通使用者無權訪問，需要root許可權。
- <strong>/data</strong>：資料分割區，存放使用者資料和應用資料。這是你日常使用的空間。
- <strong>/sdcard 或 /storage/emulated/0</strong>：使用者可訪問的儲存空間，你的照片、下載檔案都在這裡。

##### App資料儲存：

- <strong>內部儲存</strong>：App的私有空間，其他App無法訪問。解除安裝App時會被刪除。
- <strong>外部儲存</strong>：App在使用者可訪問區域儲存的檔案，如照片、下載內容。解除安裝App時不一定會被刪除。

#### 四、資料備份與恢復：給你的資料上保險

資料無價，備份是必須養成的習慣。

##### 備份策略：

1. <strong>雲備份</strong>：自動、方便，但需要網路和雲空間。iCloud、華為雲、小米雲等都支援。
2. <strong>本地備份</strong>：用資料線連線電腦，用官方工具備份。速度快、空間大，但需要手動操作。
3. <strong>雙重備份</strong>：雲備份+本地備份，最安全。

##### 備份什麼？

- <strong>照片和影片</strong>：最佔空間，也最珍貴。
- <strong>通訊錄</strong>：存在雲賬號裡最方便。
- <strong>微信聊天記錄</strong>：用微信自帶的備份功能。
- <strong>重要文件</strong>：存在雲盤或電腦上。

#### 五、檔案安全：保護你的隱私

- <strong>敏感檔案加密</strong>：很多手機有"安全資料夾"或"私密空間"功能，可以把敏感檔案放進去，需要密碼或指紋才能訪問。
- <strong>刪除不等於銷燬</strong>：普通刪除只是標記空間可覆蓋，資料還在。要徹底刪除，需要用專門的安全擦除工具，或者多次覆蓋寫入。
- <strong>雲端安全</strong>：選擇信譽好的雲服務商，開啟雙重認證，定期檢查登入裝置。

#### 六、空間不夠？來場大掃除

- <strong>清理快取</strong>：App的臨時記憶，清了能騰地方。在設定 > 儲存 裡可以清理。
- <strong>查詢大檔案</strong>：用檔案管理器按大小排序，揪出佔空間的"元兇"。
- <strong>刪除殘留</strong>：解除安裝App後，有時會留下垃圾檔案，手動清掉。
- <strong>清理相簿</strong>：刪除重複照片、模糊照片、不需要的截圖。
- <strong>清理微信</strong>：微信是空間大戶，定期清理聊天記錄和快取很有必要。

#### 七、常見檔案格式全解析

手機裡各種檔案字尾名讓人頭大，搞懂它們能幫你更好地管理檔案：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                            <thead>
                                <tr class="bg-light dark:bg-gray-700">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">格式</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">型別</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">特性</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">推薦開啟方式</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">JPG/JPEG</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">圖片</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">有失真壓縮，體積小，相容性最好。手機拍照預設格式。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">相簿/任意圖片檢視器</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">PNG</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">圖片</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">無失真壓縮，支援透明背景。截圖、圖示常用。體積比JPG大。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">相簿/任意圖片檢視器</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MP3</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">音訊</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">有失真壓縮，體積小，相容性極好。最通用的音訊格式。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">任意音樂播放器</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">FLAC</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">音訊</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">無失真壓縮，音質與CD一致，體積比MP3大3-5倍。發燒友首選。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">音樂播放器/專業播放App</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">WAV</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">音訊</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">無壓縮原始音訊，音質最好但體積巨大。專業錄音常用。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">音樂播放器</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">M4A</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">音訊</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AAC編碼，比MP3同位元速率音質更好。蘋果生態常用。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Music/音樂播放器</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MP4</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">影片</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最通用的影片封裝格式，相容性極好。手機錄製的影片預設格式。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">相簿/任意影片播放器</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MKV</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">影片</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">開源封裝格式，支援多音軌、多字幕。電影資源常用。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">VLC/nPlayer</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DOC/DOCX</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">文件</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Word文件。DOCX是壓縮格式，體積更小。DOC是舊版格式。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">WPS/Office</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">PPT/PPTX</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">演示</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">PowerPoint簡報。PPTX是壓縮格式。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">WPS/Office</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">XLS/XLSX</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">表格</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Excel電子表格。XLSX是壓縮格式。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">WPS/Office</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">PDF</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">文件</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跨平臺格式，排版固定不可編輯。合同、論文、電子書常用。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Adobe Reader/WPS</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ZIP</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">壓縮</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最通用的壓縮格式，跨平臺相容好。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系統自帶/解壓App</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">RAR</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">壓縮</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">壓縮率比ZIP高，但需要專用軟體解壓。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">解壓App</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ISO</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">映象</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">光碟映象檔案，完整複製光碟內容。系統安裝包常用。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">解壓App/虛擬光碟機</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">HTML</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">網頁</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">網頁檔案，用瀏覽器開啟。儲存的網頁常用此格式。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">瀏覽器</td>
                                </tr>
                            </tbody>
                        </table>
```
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>練一練：整理"下載"資料夾

{class="mt-1"}
開啟檔案管理器 > 進入"下載"資料夾。看看裡面都有啥？把沒用的刪掉，有用的分門別類（比如新建"工作資料"、"表情包"資料夾放進去）。順便看看儲存空間，瞭解哪些型別檔案佔用最多。
:::

{class="text-lg font-semibold mt-6 mb-2"}
#### 八、圖片與檔案系統管理：讓資產井井有條

上一節我們學會了"認識資料夾"，但光認識還不夠。本節要講的是<strong>如何主動建立一套可長期執行的管理規範</strong>，讓你的檔案隨時找得到、不丟失、不被偷窺。

{class="font-semibold mt-4 mb-1"}
##### 1. 檔案分類與命名規範

混亂的根源是沒有規則。建立規則其實很簡單，關鍵在於<strong>堅持</strong>。

```html
<ul class="list-disc pl-6 mb-3 space-y-2">
                        <li><strong>"時間+事件"命名法</strong>：資料夾名字裡帶時間戳和事件描述，方便日後回憶與檢索。例如 <code>202606_旅行票據</code>、<code>2025年終總結</code>、<code>2024孩子生日</code>。這樣既能看到時間線，也能一眼知道內容。</li>
                        <li><strong>三級分類體系</strong>：
                            <ul class="list-disc pl-6 mt-1 space-y-0.5">
                                <li><strong>一級</strong>：按檔案型別（文件 / 圖片 / 影片 / 音訊）</li>
                                <li><strong>二級</strong>：按使用場景（工作 / 生活 / 學習）</li>
                                <li><strong>三級</strong>：按具體事件或專案（如"2026Q2_專案A"）</li>
                            </ul>
                        </li>
                        <li><strong>月度清理計劃</strong>：每月固定一個日期（建議發工資那天或月初1號），對"下載"目錄進行集中整理：<strong>歸檔有用的、刪除無用的、轉存珍貴的</strong>。一年 12 次小整理，比攢一年大掃除輕鬆得多。</li>
                    </ul>
```

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-calendar-check mr-2"></i>本月任務清單

{class="mt-1"}
挑一個空閒的週末，按以下順序操作：

{class="list-decimal pl-6 mt-1 space-y-0.5 text-sm"}
1. 在檔案管理器中建立 <code>2026Q2_專案A</code> 形式的本月工作資料夾；
2. 把所有"下載"目錄裡本週的檔案過一遍，留下有用的、歸檔、刪除沒用的；
3. 給今年的家庭照片建立 <code>2025家庭</code>、<code>2026家庭</code> 這種年度資料夾。
:::

{class="font-semibold mt-4 mb-1"}
##### 2. 冗餘檔案處理策略

手機用久了會"長胖"，多半是冗餘檔案在作怪。

{class="list-disc pl-6 mb-3 space-y-2"}
- <strong>72 小時自動清理</strong>：微信、QQ 等社交 App 接收的臨時檔案（表情包、聊天圖片、小影片），大多看一次就沒用了。在 [微信] > [設定] > [通用] > [儲存空間] 裡開啟"自動清理"，把過期快取設成 72 小時。手機瞬間清爽不少，還不丟重要記錄。
- <strong>儲存空間定向清理</strong>：安卓 [設定] > [儲存] > [清理加速]，iOS [設定] > [通用] > [iPhone 儲存空間]，系統會按"快取 / 臨時檔案 / 可解除安裝 App / 大檔案"分類列出。重點清理：① 快取檔案；② 已過期安裝包（升級 App 後留下的舊版安裝包）；③ 重複檔案（同名同尺寸的照片）。
- <strong>自動分類規則</strong>：多數品牌相簿 App 支援智慧分類：人物、風景、文件、截圖。開啟後，新拍的合影會自動歸入"人物 > 張三"，掃描的合同會自動歸入"文件"。<strong>配合每月整理，可極大降低"找不到東西"的機率</strong>。

{class="font-semibold mt-4 mb-1"}
##### 3. 圖片安全處理規範

圖片是手機裡最"敏感"的資料型別——一張隨手拍就能暴露你的位置、裝置、時間。我們建議<strong>建立"雙重保護"工作流</strong>：

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-image mr-2"></i>傳送證件照/敏感截圖的標準流程

{class="list-decimal pl-6 mt-1 space-y-1 text-sm"}
1. <strong>可見資訊打碼</strong>：用系統自帶或第三方工具（如美圖秀秀、Snapseed）<strong>塗抹身份證號中間幾位、車牌號、門牌、姓名、金額</strong>等關鍵欄位；
2. <strong>後設資料剝離</strong>：傳送前在相簿中點"分享"或"匯出"，系統會詢問是否保留位置資訊，選擇<strong>"不保留"</strong>。這樣拍攝裝置型號、GPS 座標、拍攝時間就不會跟著圖片一起發出去；
3. <strong>臨時水印</strong>（可選）：在敏感截圖上加"僅供XX辦理使用"的文字水印，避免被濫用。
:::

{class="mt-3 mb-2"}
後設資料（EXIF）清理的常用方法（基礎操作，深度防護見第六章"照片脫敏處理"）：

- <strong>系統自帶</strong>：iOS [設定] > [隱私與安全性] > [相機]，可關閉"精確位置"；分享時選"僅當前照片"會<strong>自動剝離大部分 EXIF</strong>。
- <strong>安卓</strong>：多數品牌相簿 App 在"分享"時會提示"是否移除位置資訊"，勾選即可。
- <strong>專業工具</strong>：ExifTool（電腦端）、Metapho（iOS）、Photo Metadata Remover（安卓）可以徹底清除所有後設資料。

對於需要<strong>長期儲存</strong>的敏感圖片（身份證、銀行卡、戶口本掃描件、護照），建議存入<strong>加密相簿</strong>：

- iPhone：[照片] > 選中照片 > 隱藏（僅 Face ID 驗證後可檢視）；
- 華為/小米：[相簿] > 長按照片 > "移入保險櫃"；
- 第三方加密 App：<strong>360 安全相簿</strong>、<strong>騰訊相簿管家（隱私相簿）</strong>、<strong>KeepSafe</strong> 等，單獨密碼保護，隱蔽性更好。
