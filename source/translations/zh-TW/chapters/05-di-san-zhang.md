---
id: di-san-zhang
num: 03
part: ji-chu-pian
nav: 第三章：讓手機接上"生命線"
toc: default
kind: chapter
---

### 第三章：讓手機接上"生命線"——網路

{class="chapter-intro mb-4"}
沒網，智慧手機就"智障"了一半。網路是現代手機的生命線，理解它、用好它、保護它，是每個手機使用者的必修課。

#### 〇、聯網不迷茫——分清Wi-Fi與流量的"路"與"車"

很多人的手機螢幕上方同時亮著Wi-Fi和訊號圖示，但對二者的本質區別卻一頭霧水。最經典的誤區就是：<strong>連著Wi-Fi卻刷不出頁面</strong>——因為路由器斷網了，而手機並沒有自動切迴流量。要徹底弄懂這個問題，我們需要建立一個"路與車"的認知模型。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-road mr-2"></i>核心比喻：路與車

{class="mt-1"}
把網際網路想象成一座城市。<strong>"路"</strong>是你手機到網際網路之間的通道，<strong>"車"</strong>是跑在路上的資料。Wi-Fi和流量是兩條不同的路，但資料（車）本身是一樣的。
:::

{class="font-semibold mt-4 mb-1"}
##### 1. 本質區別：本地通道 vs 遠端高速

Wi-Fi本質上是一種<strong>區域網技術</strong>，它就像你家樓下無線鋪設的路，負責把資料從路由器傳到手機上。但如果寬頻欠費或光纜斷了，路雖然還在，外面的"高速公路"卻斷了，自然哪兒也去不了。而網路流量（移動資料）則是透過運營商的4G/5G基站傳輸，相當於你直接開上了運營商的高速專線，只要有訊號就能直連網際網路。

{class="font-semibold mt-4 mb-1"}
##### 2. 費用與場景：固定月租 vs 按量計費

Wi-Fi通常是一次性投入（寬頻月費），只要電費不斷，全家人無限使用，非常適合下載電影、打遊戲等大流量場景。而流量則按使用量計費，超出套餐可能會降速或額外扣費，更適合在地鐵、出差等移動場景下處理輕量級任務。

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands-helping mr-2"></i>來試試：檢查你的流量套餐

{class="mt-1"}
開啟手機的 [設定] > [行動網路] > [流量管理]，看看你本月還剩多少流量、哪些App最耗流量。心裡有數，出門才不慌。
:::

{class="font-semibold mt-4 mb-1"}
##### 3. 安全考量：公共Wi-Fi是隱秘的"釣魚場"

在安全性上，移動資料通常比公共Wi-Fi更安全。移動資料由運營商加密，而公共Wi-Fi確實容易被駭客搭建為"偽熱點"截獲未加密的流量。但這裡要區分清楚：在HTTPS全面普及的今天，攻擊者能截獲的是<strong>你訪問了哪些網站</strong>（域名），以及<strong>未加密的HTTP內容</strong>；而微信訊息、銀行App的登入密碼等經過HTTPS加密的資料，攻擊者<strong>無法直接讀取</strong>——除非實施更復雜的SSL剝離攻擊且使用者忽略了證書警告。不過即便如此，在外進行支付操作時，直接用手機流量仍然是最穩妥的選擇。

::: div .danger-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>安全提醒

{class="mt-1"}
在機場、商場、咖啡廳等公共場所，不要連線名字可疑的免費Wi-Fi（如"Free_WiFi_2024"）。即使連了，也絕不要在上面登入銀行App或輸入密碼。
:::

{class="font-semibold mt-4 mb-1"}
##### 4. 手機端判斷：看懂狀態列的"暗語"

如何知道手機此刻在用什麼聯網？以華為手機為例，狀態列中運營商訊號旁或WLAN訊號旁出現<strong>雙向箭頭圖示</strong>，即代表正在使用對應方式上網；若兩者同時亮起，則說明網路加速生效，手機正同時利用兩種通道。

iPhone使用者則更直觀：Wi-Fi圖示亮著就是在用Wi-Fi，不亮時看右上角的訊號格就是在用流量。部分安卓手機還會在狀態列顯示"5G"或"4G"字樣，直接告訴你當前行動網路型別。

{class="text-lg font-semibold mt-6 mb-2"}
#### 一、行動網路（4G/5G）與流量

行動網路是你隨時隨地聯網的基礎。從2G到5G，速度提升了上千倍，但原理其實差不多。

##### 網路制式：

- <strong>4G LTE</strong>：目前覆蓋最廣，速度夠用（理論上最高100Mbps+），耗電相對低。
- <strong>5G</strong>：速度快（理論上最高10Gbps），但覆蓋還在完善，耗電高。適合下載大檔案、看高畫質影片。
- <strong>5G SA vs NSA</strong>：SA是獨立組網，NSA是依託4G基站。SA體驗更好，但需要運營商和手機都支援。

##### 流量管理：

- <strong>流量是什麼</strong>：就是手機上網產生的資料量。看影片、刷圖最費流量，文字和語音相對省。
- <strong>省流小貼士</strong>：在設定裡開啟"省流量模式"，Wi-Fi下再更新App或看高畫質影片。
- <strong>訊號格≠網速</strong>：訊號強只代表連線好，網速還看基站忙不忙、你離基站多遠。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>重要警告：出國前關閉【資料漫遊】！

{class="mt-1"}
在國外使用移動資料可能產生天價賬單！出國前務必在設定裡關閉資料漫遊，或者提前購買當地流量卡/國際漫遊套餐。
:::

#### 二、Wi-Fi：連線、分享與安全

Wi-Fi是家庭和辦公室的聯網主力，速度快、不費流量。但Wi-Fi其實也在不斷進化，不同標準之間差異很大。

##### 連線Wi-Fi：

去 [設定] > [WLAN] 選擇網路輸密碼。現在很多手機支援掃碼連線，更方便。

##### 分享密碼：

安卓和iOS都能讓已連線的手機快速分享密碼給朋友。安卓生成二維碼，iOS可以靠近自動分享。

##### Wi-Fi標準演進：

Wi-Fi標準由IEEE制定，每一代都有顯著提升：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                            <thead>
                                <tr class="bg-light dark:bg-gray-700">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">標準</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">協議</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">頻段</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">最高速率</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">特點</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 4</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11n</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.4/5GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">600Mbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">老舊標準，覆蓋還行</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 5</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11ac</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">5GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.5Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">目前最普及，速度夠用</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 6</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11ax</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.4/5GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">9.6Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多裝置效能強，延遲低</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 6E</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11ax</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.4/5/6GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">9.6Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">增加6GHz頻段，不擁堵</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 7</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11be</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.4/5/6GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">46Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">極速傳輸，多鏈路聚合</td>
                                </tr>
                            </tbody>
                        </table>
```
:::

- <strong>Wi-Fi 6的關鍵技術</strong>：OFDMA（正交分頻多重進接）讓多個裝置同時傳輸，MU-MIMO（多使用者多入多出）提升多裝置併發效率，TWT（目標喚醒時間）讓裝置更省電。
- <strong>Wi-Fi 6E</strong>：在Wi-Fi 6基礎上增加了6GHz頻段，提供更多通道，減少干擾。需要手機和路由器都支援。
- <strong>Wi-Fi 7</strong>：引入MLO（多鏈路操作），可同時使用多個頻段傳輸資料，大幅降低延遲。320MHz超寬通道讓速率飛躍。驍龍8 Elite Gen5、天璣9400等旗艦晶片平臺均已支援Wi-Fi 7，小米17、華為Mate 80、三星S26等機型可使用Wi-Fi 7網路（需配合Wi-Fi 7路由器）。
- <strong>2.4GHz vs 5GHz</strong>：2.4GHz穿牆好但速度慢、干擾多；5GHz速度快但穿牆弱。Wi-Fi 6E/7的6GHz頻段速度最快，但穿牆最弱，適合同一房間內使用。

##### 公共Wi-Fi風險：

公共Wi-Fi可能有駭客竊聽資料或設釣魚熱點。守則：

- 避免登入銀行賬戶、輸入密碼。
- 最好用VPN加密連線。
- 不要自動連線陌生Wi-Fi。
- 用HTTPS網站（位址列有鎖圖示）。

#### 三、藍芽：短距離無線通訊的萬能選手

藍芽可能是你手機上使用頻率最高的無線技術之一——無線耳機、智慧手錶、車載系統、鍵盤滑鼠，都靠它連線。

##### 技術原理：

藍芽工作在2.4GHz ISM頻段，使用跳頻擴頻技術（FHSS）將資料分散在79個頻道上快速切換傳輸，有效避免干擾。藍芽的通訊距離分為三個等級：Class 1約100米、Class 2約10米（手機常用）、Class 3約1米。

##### 版本演進：

- <strong>藍芽4.0</strong>：引入低功耗藍芽（BLE），讓手環、心率帶這類小電池裝置也能無線連線，續航從天變成月。
- <strong>藍芽4.2</strong>：提升傳輸速度和隱私保護，支援IPv6直連。
- <strong>藍芽5.0</strong>：傳輸速度翻倍（2Mbps），傳輸距離4倍（理論300米），廣播能力8倍。支援雙音訊（同時連兩副耳機）。
- <strong>藍芽5.1</strong>：引入方向定址功能（AoA/AoD），定位精度可達釐米級。
- <strong>藍芽5.2</strong>：LE Audio新標準，支援LC3編碼（音質更好、功耗更低）、多流音訊、廣播音訊。
- <strong>藍芽5.3/5.4</strong>：進一步最佳化功耗和連線穩定性，增強週期性廣播。

<strong>LE Audio普及情況</strong>：2025-2026年，LE Audio已進入快速普及階段。主流品牌的新款真無線耳機（如華為FreeBuds Pro 5、小米Buds 6 Pro、三星Galaxy Buds3 Pro等）均已支援LE Audio和LC3編碼，提供更低延遲和更好音質。購買新耳機時，建議優先選擇支援LE Audio的產品。

##### 應用場景：

- <strong>音訊傳輸</strong>：無線耳機、車載音響。藍芽5.2的LE Audio讓音質和延遲都有質的飛躍。
- <strong>資料傳輸</strong>：近距離傳檔案、照片。雖然速度不如Wi-Fi Direct，但勝在簡單。
- <strong>裝置配對</strong>：智慧手錶、手環、鍵盤滑鼠、遊戲手柄。
- <strong>位置服務</strong>：藍芽信標（Beacon）用於室內導航、物品追蹤（如蘋果AirTag）。
- <strong>智慧家居</strong>：藍芽Mesh網路控制燈泡、門鎖等。

#### 四、紅外遙控：手機變身萬能遙控器

紅外遙控是最古老的無線控制技術之一，但在手機上依然實用。部分安卓手機（如小米、華為部分機型）內建了紅外發射器，可以遙控電視、空調、機頂盒等家電。

##### 工作原理：

紅外遙控透過紅外發光二極體發出特定頻率（通常38kHz）的紅外光脈衝訊號，家電的紅外接收器解碼這些脈衝執行對應操作。不同品牌使用不同的編碼協議，常見的有NEC、RC5、RC6、SONY等。手機裡的紅外App內建了各品牌的編碼庫，選擇品牌和型號就能匹配。

##### 侷限性：

- <strong>方向性</strong>：紅外是直線傳播，需要對著裝置發射，不能隔牆。
- <strong>距離短</strong>：有效距離一般5-8米。
- <strong>蘋果不支援</strong>：iPhone沒有紅外發射器，無法使用此功能。

#### 五、NFC：碰一碰的魔法

NFC（Near Field Communication，近場通訊）是一種極短距離（10釐米以內）的高頻無線通訊技術，工作頻率13.56MHz，傳輸速率最高424Kbps。

##### 通訊原理與模式：

NFC基於RFID技術演變而來，支援三種工作模式：

- <strong>讀寫模式</strong>：手機讀取NFC標籤中的資訊，如讀取NFC貼紙觸發動作。
- <strong>點對點模式</strong>：兩臺NFC裝置互相傳輸資料，如Android Beam（已停用）。
- <strong>卡模擬模式</strong>：手機模擬一張智慧卡，這是最常用的模式——公交卡、門禁卡、銀行卡都是這個模式。

##### 安全機制：

- <strong>超短距離</strong>：10釐米內的通訊距離本身就是物理安全保障，遠端竊聽幾乎不可能。
- <strong>安全晶片</strong>：手機內建獨立的安全晶片（SE）或使用HCE（主機卡模擬），支付金鑰儲存在安全區域，即使手機被root也無法提取。
- <strong>指紋/面容驗證</strong>：支付時需要生物識別確認，即使手機丟失也無法盜刷。
- <strong>令牌化</strong>：Apple Pay、華為Pay等不傳輸真實卡號，而是使用一次性令牌，即使被截獲也無法重複使用。

##### 典型應用：

- <strong>公交卡/門禁卡</strong>：把實體卡資訊寫入手機，刷手機就行。
- <strong>移動支付</strong>：Apple Pay、華為Pay等，把銀行卡繫結到手機，碰一碰支付。
- <strong>裝置配對</strong>：NFC碰一碰快速配對藍芽耳機、音箱。
- <strong>身份驗證</strong>：NFC身份證讀取、電子駕照驗證。

#### 六、個人熱點：把手機變Wi-Fi路由器

自己流量多時，可以開熱點給平板、電腦用。

- <strong>開啟方法</strong>：設定 > 個人熱點/網路共享，開啟它。
- <strong>注意事項</strong>：很耗電和流量，記得設個複雜密碼，並限制連線裝置數。
- <strong>USB共享</strong>：用資料線連電腦，比無線熱點更穩定、更快。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>動手試試：設定並管理熱點

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 開啟 [設定]，找到"個人熱點"或"網路共享"，開啟它，設好名稱和密碼。
2. 用另一臺裝置（比如電腦）搜尋並連線這個Wi-Fi。
3. 在手機端看看，能不能管理已連線的裝置，或踢掉不認識的裝置。
:::
