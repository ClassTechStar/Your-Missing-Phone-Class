---
id: di-er-zhang
num: 02
part: ji-chu-pian
nav: 第二章：整理你嘅數碼房間
toc: default
kind: chapter
---

### 第二章：整理你嘅數碼房間——檔案管理

{class="chapter-intro mb-4"}
手機用耐咗會亂，好習慣由管理檔案開始。就好似你嘅房間需要定期整理一樣，你嘅數碼空間都需要打理。一個井井有條嘅手機，唔只揾嘢方便，運行都更流暢。

#### 一、三層存儲體系：你嘅數碼倉庫

{class="list-decimal pl-6 mb-3 space-y-2"}
1. <strong>機身存儲</strong>：核心區，速度快，系統同App都喺度。呢個係你手機最寶貴嘅空間，要精打細算。
2. <strong>SD卡（如果支援）</strong>：擴展衣櫃，速度慢啲，適合放電影、相片等大檔案。注意：而家好多旗艦機唔支援SD卡喇。
3. <strong>雲存儲</strong>：保險櫃+同步網盤。防遺失，都可以喺多個設備間同步。iCloud、百度網盤、OneDrive都係常用選擇。

#### 二、認識「檔案管理器」

安卓一般有個 [檔案] 或 [檔案管理] App，iOS係自帶嘅 [檔案] App。佢哋係你查看手機所有檔案嘅「資源管理器」。

##### 常見資料夾含義：

- <strong>DCIM</strong>：相機拍攝嘅相片同影片。
- <strong>Pictures</strong>：其他圖片，如截圖、儲存嘅圖片。
- <strong>Download</strong>：瀏覽器下載嘅檔案。
- <strong>Music</strong>：音樂檔案。
- <strong>Movies</strong>：影片檔案。
- <strong>Documents</strong>：文檔檔案。
- <strong>Android</strong>：安卓系統資料夾，入面係各App嘅數據，一般唔好手動刪除。

#### 三、檔案系統結構：深入瞭解

安卓基於Linux，檔案系統有一定嘅層級結構。雖然普通用戶唔需要深入瞭解，但知道一啲基本概念有幫助。

##### 存儲分區：

- <strong>/system</strong>：系統分區，存放作業系統檔案。普通用戶無權訪問，需要root權限。
- <strong>/data</strong>：數據分區，存放用戶數據同應用數據。呢個係你日常使用嘅空間。
- <strong>/sdcard 或 /storage/emulated/0</strong>：用戶可訪問嘅存儲空間，你嘅相片、下載檔案都喺度。

##### App數據存儲：

- <strong>內部存儲</strong>：App嘅私有空間，其他App無法訪問。卸載App嗰陣會被刪除。
- <strong>外部存儲</strong>：App喺用戶可訪問區域存儲嘅檔案，如相片、下載內容。卸載App嗰陣唔一定會被刪除。

#### 四、數據備份與恢復：畀你嘅數據上保險

數據無價，備份係必須養成嘅習慣。

##### 備份策略：

1. <strong>雲備份</strong>：自動、方便，但需要網絡同雲空間。iCloud、華為雲、小米雲等都支援。
2. <strong>本地備份</strong>：用數據線連接電腦，用官方工具備份。速度快、空間大，但需要手動操作。
3. <strong>雙重備份</strong>：雲備份+本地備份，最安全。

##### 備份乜嘢？

- <strong>相片同影片</strong>：最佔空間，都最珍貴。
- <strong>通訊錄</strong>：存在雲帳號入面最方便。
- <strong>微信聊天記錄</strong>：用微信自帶嘅備份功能。
- <strong>重要文檔</strong>：存在雲盤或電腦上。

#### 五、檔案安全：保護你嘅私隱

- <strong>敏感檔案加密</strong>：好多手機有「安全資料夾」或「私密空間」功能，可以將敏感檔案放入去，需要密碼或指紋先可以訪問。
- <strong>刪除唔等於銷毀</strong>：普通刪除淨係標記空間可覆蓋，數據仲喺度。要徹底刪除，需要用專門嘅安全擦除工具，或者多次覆蓋寫入。
- <strong>雲端安全</strong>：選擇信譽好嘅雲服務商，開啟雙重認證，定期檢查登錄設備。

#### 六、空間唔夠？嚟場大掃除

- <strong>清理快取</strong>：App嘅臨時記憶，清咗可以騰出地方。喺設定 > 存儲 入面可以清理。
- <strong>查找大檔案</strong>：用檔案管理器按大小排序，揪出佔空間嘅「元兇」。
- <strong>刪除殘留</strong>：卸載App後，有時會留低垃圾檔案，手動清掉。
- <strong>清理相簿</strong>：刪除重複相片、模糊相片、唔需要嘅截圖。
- <strong>清理微信</strong>：微信係空間大戶，定期清理聊天記錄同快取好有必要。

#### 七、常見檔案格式全解析

手機入面各種檔案後綴名令人頭大，搞懂佢哋可以幫你更好咁管理檔案：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                            <thead>
                                <tr class="bg-light dark:bg-gray-700">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">格式</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">類型</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">特性</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">推薦打開方式</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">JPG/JPEG</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">圖片</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">有損壓縮，體積細，兼容性最好。手機影相預設格式。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">相簿/任意圖片查看器</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">PNG</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">圖片</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">無損壓縮，支援透明背景。截圖、圖標常用。體積比JPG大。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">相簿/任意圖片查看器</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MP3</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">音頻</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">有損壓縮，體積細，兼容性極好。最通用嘅音頻格式。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">任意音樂播放器</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">FLAC</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">音頻</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">無損壓縮，音質與CD一致，體積比MP3大3-5倍。發燒友首選。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">音樂播放器/專業播放App</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">WAV</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">音頻</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">無壓縮原始音頻，音質最好但體積巨大。專業錄音常用。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">音樂播放器</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">M4A</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">音頻</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AAC編碼，比MP3同碼率音質更好。蘋果生態常用。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Music/音樂播放器</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MP4</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">影片</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最通用嘅影片封裝格式，兼容性極好。手機錄製嘅影片預設格式。</td>
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
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">文檔</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Word文檔。DOCX係壓縮格式，體積更細。DOC係舊版格式。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">WPS/Office</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">PPT/PPTX</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">演示</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">PowerPoint演示文稿。PPTX係壓縮格式。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">WPS/Office</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">XLS/XLSX</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">表格</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Excel電子表格。XLSX係壓縮格式。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">WPS/Office</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">PDF</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">文檔</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跨平臺格式，排版固定唔可編輯。合同、論文、電子書常用。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Adobe Reader/WPS</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ZIP</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">壓縮</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最通用嘅壓縮格式，跨平臺兼容好。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系統自帶/解壓App</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">RAR</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">壓縮</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">壓縮率比ZIP高，但需要專用軟件解壓。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">解壓App</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ISO</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">鏡像</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">光碟鏡像檔案，完整複製光碟內容。系統安裝包常用。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">解壓App/虛擬光驅</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">HTML</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">網頁</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">網頁檔案，用瀏覽器打開。儲存嘅網頁常用呢個格式。</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">瀏覽器</td>
                                </tr>
                            </tbody>
                        </table>
```
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>練一練：整理「下載」資料夾

{class="mt-1"}
打開檔案管理器 > 進入「下載」資料夾。睇下入面都有啲乜嘢？將冇用嘅刪掉，有用嘅分門別類（比如新建「工作資料」、「表情包」資料夾放入去）。順便睇下存儲空間，瞭解邊啲類型檔案佔用最多。
:::

{class="text-lg font-semibold mt-6 mb-2"}
#### 八、圖片與檔案系統管理：等資產井井有條

上一節我哋學識咗「認識資料夾」，但淨係認識都唔夠。本節要講嘅係<strong>點樣主動建立一套可長期執行嘅管理規範</strong>，等你嘅檔案隨時揾得到、唔遺失、唔被偷窺。

{class="font-semibold mt-4 mb-1"}
##### 1. 檔案分類與命名規範

混亂嘅根源係冇規則。建立規則其實好簡單，關鍵在於<strong>堅持</strong>。

```html
<ul class="list-disc pl-6 mb-3 space-y-2">
                        <li><strong>「時間+事件」命名法</strong>：資料夾名入面帶時間戳同事件描述，方便日後回憶同檢索。例如 <code>202606_旅行票據</code>、<code>2025年終總結</code>、<code>2024孩子生日</code>。咁樣既能睇到時間線，一眼就知道內容。</li>
                        <li><strong>三級分類體系</strong>：
                            <ul class="list-disc pl-6 mt-1 space-y-0.5">
                                <li><strong>一級</strong>：按檔案類型（文檔 / 圖片 / 影片 / 音頻）</li>
                                <li><strong>二級</strong>：按使用場景（工作 / 生活 / 學習）</li>
                                <li><strong>三級</strong>：按具體事件或項目（如「2026Q2_項目A」）</li>
                            </ul>
                        </li>
                        <li><strong>月度清理計劃</strong>：每月固定一個日期（建議出糧嗰日或月初1號），對「下載」目錄進行集中整理：<strong>歸檔有用嘅、刪除冇用嘅、轉存珍貴嘅</strong>。一年 12 次小整理，比起攢一年大掃除輕鬆得多。</li>
                    </ul>
```

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-calendar-check mr-2"></i>本月任務清單

{class="mt-1"}
揀一個空閒嘅週末，按以下順序操作：

{class="list-decimal pl-6 mt-1 space-y-0.5 text-sm"}
1. 喺檔案管理器中創建 <code>2026Q2_項目A</code> 形式嘅本月工作資料夾；
2. 將所有「下載」目錄入面本週嘅檔案過一遍，留低有用嘅、歸檔、刪除冇用嘅；
3. 畀今年嘅家庭相片建立 <code>2025家庭</code>、<code>2026家庭</code> 呢種年度資料夾。
:::

{class="font-semibold mt-4 mb-1"}
##### 2. 冗餘檔案處理策略

手機用耐咗會「長胖」，多數係冗餘檔案喺度作怪。

{class="list-disc pl-6 mb-3 space-y-2"}
- <strong>72 小時自動清理</strong>：微信、QQ 等社交 App 接收嘅臨時檔案（表情包、聊天圖片、短影片），大多睇一次就冇用。喺 [微信] > [設定] > [通用] > [存儲空間] 入面開啟「自動清理」，將過期快取設成 72 小時。手機瞬間清爽唔少，仲唔丟重要記錄。
- <strong>存儲空間定向清理</strong>：安卓 [設定] > [存儲] > [清理加速]，iOS [設定] > [通用] > [iPhone 存儲空間]，系統會按「快取 / 臨時檔案 / 可卸載 App / 大檔案」分類列出。重點清理：① 快取檔案；② 已過期安裝包（升級 App 後留低嘅舊版安裝包）；③ 重複檔案（同名同尺寸嘅相片）。
- <strong>自動分類規則</strong>：多數品牌相簿 App 支援智能分類：人物、風景、文檔、截圖。開啟後，新拍嘅合影會自動歸入「人物 > 張三」，掃描嘅合同會自動歸入「文檔」。<strong>配合每月整理，可極大降低「揾唔到嘢」嘅概率</strong>。

{class="font-semibold mt-4 mb-1"}
##### 3. 圖片安全處理規範

圖片係手機入面最「敏感」嘅數據類型——一張隨手拍就可以暴露你嘅位置、設備、時間。我哋建議<strong>建立「雙重保護」工作流</strong>：

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-image mr-2"></i>發送證件相/敏感截圖嘅標準流程

{class="list-decimal pl-6 mt-1 space-y-1 text-sm"}
1. <strong>可見資訊打碼</strong>：用系統自帶或第三方工具（如美圖秀秀、Snapseed）<strong>塗抹身份證號中間幾位、車牌號、門牌、姓名、金額</strong>等關鍵字段；
2. <strong>元數據剝離</strong>：發送前喺相簿中點「分享」或「導出」，系統會詢問係咪保留位置資訊，選擇<strong>「唔保留」</strong>。咁樣拍攝設備型號、GPS 坐標、拍攝時間就不會跟住圖片一齊發出去；
3. <strong>臨時水印</strong>（可選）：喺敏感截圖上加「僅供XX辦理使用」嘅文字水印，避免被濫用。
:::

{class="mt-3 mb-2"}
元數據（EXIF）清理嘅常用方法（基礎操作，深度防護見第六章「相片脱敏處理」）：

- <strong>系統自帶</strong>：iOS [設定] > [私隱與安全性] > [相機]，可關閉「精確位置」；分享嗰陣選「僅當前相片」會<strong>自動剝離大部分 EXIF</strong>。
- <strong>安卓</strong>：多數品牌相簿 App 喺「分享」嗰陣會提示「係咪移除位置資訊」，勾選即可。
- <strong>專業工具</strong>：ExifTool（電腦端）、Metapho（iOS）、Photo Metadata Remover（安卓）可以徹底清除所有元數據。

對於需要<strong>長期保存</strong>嘅敏感圖片（身份證、銀行卡、戶口本掃描件、護照），建議存入<strong>加密相簿</strong>：

- iPhone：[相片] > 選中相片 > 隱藏（僅 Face ID 驗證後可查看）；
- 華為/小米：[相簿] > 長按照片 > 「移入保險櫃」；
- 第三方加密 App：<strong>360 安全相簿</strong>、<strong>騰訊相冊管家（私隱相簿）</strong>、<strong>KeepSafe</strong> 等，單獨密碼保護，隱蔽性更好。
