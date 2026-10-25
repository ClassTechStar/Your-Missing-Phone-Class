---
id: di-san-zhang
num: 03
part: ji-chu-pian
nav: 第三章：畀手機接上「生命線」
toc: default
kind: chapter
---

### 第三章：等手機接上「生命線」——網絡

{class="chapter-intro mb-4"}
冇網，智能手機就「智障」咗一半。網絡係現代手機嘅生命線，理解佢、用好佢、保護佢，係每個手機用戶嘅必修課。

#### 〇、聯網唔迷茫——分清Wi-Fi與流量嘅「路」與「車」

好多人嘅手機螢幕上方同時亮住Wi-Fi同信號圖標，但對二者嘅本質區別卻一頭霧水。最經典嘅誤區就係：<strong>連住Wi-Fi卻刷唔出頁面</strong>——因為路由器斷網喇，而手機並冇自動切返流量。要徹底弄懂呢個問題，我哋需要建立一個「路與車」嘅認知模型。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-road mr-2"></i>核心比喻：路與車

{class="mt-1"}
將互聯網諗像成一座城市。<strong>「路」</strong>係你手機到互聯網之間嘅通道，<strong>「車」</strong>係跑喺路上嘅數據。Wi-Fi同流量係兩條唔同嘅路，但數據（車）本身係一樣嘅。
:::

{class="font-semibold mt-4 mb-1"}
##### 1. 本質區別：本地通道 vs 遠程高速

Wi-Fi本質上係一種<strong>局域網技術</strong>，佢就好似你屋企樓下無線鋪設嘅路，負責將數據由路由器傳到手機上。但如果寬頻欠費或光纜斷咗，路雖然仲喺度，外面嘅「高速公路」卻斷咗，自然去邊度都去唔到。而網絡流量（流動數據）就係通過電訊商嘅4G/5G基站傳輸，相當於你直接開上咗電訊商嘅高速專線，只要有信號就可以直連互聯網。

{class="font-semibold mt-4 mb-1"}
##### 2. 費用與場景：固定月租 vs 按量計費

Wi-Fi通常係一次性投入（寬頻月費），只要電費唔斷，全家人無限使用，非常適合下載電影、打遊戲等大流量場景。而流量就按使用量計費，超出套餐可能會降速或額外扣費，更適合喺地鐵、出差等流動場景下處理輕量級任務。

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands-helping mr-2"></i>嚟試下：檢查你嘅流量套餐

{class="mt-1"}
打開手機嘅 [設定] > [流動網絡] > [流量管理]，睇下你本月仲剩幾多流量、邊啲App最耗流量。心入面有個數，出門先唔慌。
:::

{class="font-semibold mt-4 mb-1"}
##### 3. 安全考量：公共Wi-Fi係隱秘嘅「釣魚場」

喺安全性上，流動數據通常比公共Wi-Fi更安全。流動數據由電訊商加密，而公共Wi-Fi確實容易被黑客搭建為「偽熱點」截獲未加密嘅流量。但呢度要分清楚：喺HTTPS全面普及嘅今日，攻擊者能截獲嘅係<strong>你訪問咗邊啲網站</strong>（域名），以及<strong>未加密嘅HTTP內容</strong>；而微信消息、銀行App嘅登錄密碼等經過HTTPS加密嘅數據，攻擊者<strong>無法直接讀取</strong>——除非實施更複雜嘅SSL剝離攻擊且用戶忽略咗證書警告。不過即便如此，喺外面進行支付操作嗰陣，直接用手機流量仍然係最穩妥嘅選擇。

::: div .danger-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>安全提醒

{class="mt-1"}
喺機場、商場、咖啡廳等公共場所，唔好連接名可疑嘅免費Wi-Fi（如「Free_WiFi_2024」）。即使連咗，都絕唔好喺上面登錄銀行App或輸入密碼。
:::

{class="font-semibold mt-4 mb-1"}
##### 4. 手機端判斷：睇懂狀態欄嘅「暗語」

點樣知道手機此刻喺度用乜嘢聯網？以華為手機為例，狀態欄中電訊商信號旁或WLAN信號旁出現<strong>雙向箭頭圖標</strong>，即代表正在使用對應方式上網；若兩者同時亮起，就說明網絡加速生效，手機正同時利用兩種通道。

iPhone用戶就更直觀：Wi-Fi圖標亮住就係喺度用Wi-Fi，唔亮嗰陣睇右上角嘅信號格就係喺度用流量。部分安卓手機仲會喺狀態欄顯示「5G」或「4G」字樣，直接話畀你知目前流動網絡類型。

{class="text-lg font-semibold mt-6 mb-2"}
#### 一、流動網絡（4G/5G）與流量

流動網絡係你隨時隨地聯網嘅基礎。由2G到5G，速度提升咗上千倍，但原理其實差唔多。

##### 網絡制式：

- <strong>4G LTE</strong>：目前覆蓋最廣，速度夠用（理論上最高100Mbps+），耗電相對低。
- <strong>5G</strong>：速度快（理論上最高10Gbps），但覆蓋仲喺度完善，耗電高。適合下載大檔案、睇高清影片。
- <strong>5G SA vs NSA</strong>：SA係獨立組網，NSA係依託4G基站。SA體驗更好，但需要電訊商同手機都支援。

##### 流量管理：

- <strong>流量係乜嘢</strong>：就係手機上網產生嘅數據量。睇影片、刷圖最費流量，文字同語音相對慳。
- <strong>慳流小貼士</strong>：喺設定入面開啟「慳流量模式」，Wi-Fi下再更新App或睇高清影片。
- <strong>信號格≠網速</strong>：信號強淨係代表連接好，網速仲要睇基站忙唔忙、你離基站幾遠。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>重要警告：出國前關閉【數據漫遊】！

{class="mt-1"}
喺國外使用流動數據可能產生天價賬單！出國前務必喺設定入面關閉數據漫遊，或者提前購買當地流量卡/國際漫遊套餐。
:::

#### 二、Wi-Fi：連接、分享與安全

Wi-Fi係家庭同辦公室嘅聯網主力，速度快、唔費流量。但Wi-Fi其實都喺度不斷進化，唔同標準之間差異好大。

##### 連接Wi-Fi：

去 [設定] > [WLAN] 選擇網絡輸密碼。而家好多手機支援掃碼連接，更方便。

##### 分享密碼：

安卓同iOS都可以等已連接嘅手機快速分享密碼畀朋友。安卓生成二維碼，iOS可以靠近自動分享。

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
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多設備性能強，延遲低</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 6E</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11ax</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.4/5/6GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">9.6Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">增加6GHz頻段，唔擁堵</td>
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

- <strong>Wi-Fi 6嘅關鍵技術</strong>：OFDMA（正交頻分多址）等多個設備同時傳輸，MU-MIMO（多用戶多入多出）提升多設備並發效率，TWT（目標喚醒時間）等設備更慳電。
- <strong>Wi-Fi 6E</strong>：喺Wi-Fi 6基礎上增加咗6GHz頻段，提供更多信道，減少幹擾。需要手機同路由器都支援。
- <strong>Wi-Fi 7</strong>：引入MLO（多鏈路操作），可同時使用多個頻段傳輸數據，大幅降低延遲。320MHz超寬信道等速率飛躍。驍龍8 Elite Gen5、天璣9400等旗艦晶片平臺均已支援Wi-Fi 7，小米17、華為Mate 80、三星S26等機型可使用Wi-Fi 7網絡（需配合Wi-Fi 7路由器）。
- <strong>2.4GHz vs 5GHz</strong>：2.4GHz穿牆好但速度慢、幹擾多；5GHz速度快但穿牆弱。Wi-Fi 6E/7嘅6GHz頻段速度最快，但穿牆最弱，適合同一房間內使用。

##### 公共Wi-Fi風險：

公共Wi-Fi可能有黑客竊聽數據或設釣魚熱點。守則：

- 避免登錄銀行賬戶、輸入密碼。
- 最好用VPN加密連接。
- 唔好自動連接陌生Wi-Fi。
- 用HTTPS網站（地址欄有鎖圖標）。

#### 三、藍牙：短距離無線通信嘅萬能選手

藍牙可能係你手機上使用頻率最高嘅無線技術之一——無線耳機、智能手錶、車載系統、鍵盤滑鼠，都靠佢連接。

##### 技術原理：

藍牙工作喺2.4GHz ISM頻段，使用跳頻擴頻技術（FHSS）將數據分散喺79個頻道上快速切換傳輸，有效避免幹擾。藍牙嘅通信距離分為三個等級：Class 1約100米、Class 2約10米（手機常用）、Class 3約1米。

##### 版本演進：

- <strong>藍牙4.0</strong>：引入低功耗藍牙（BLE），等手環、心率帶呢類細電池設備都可以無線連接，續航由天變成月。
- <strong>藍牙4.2</strong>：提升傳輸速度同私隱保護，支援IPv6直連。
- <strong>藍牙5.0</strong>：傳輸速度翻倍（2Mbps），傳輸距離4倍（理論300米），廣播能力8倍。支援雙音頻（同時連兩副耳機）。
- <strong>藍牙5.1</strong>：引入方向尋址功能（AoA/AoD），定位精度可達釐米級。
- <strong>藍牙5.2</strong>：LE Audio新標準，支援LC3編碼（音質更好、功耗更低）、多流音頻、廣播音頻。
- <strong>藍牙5.3/5.4</strong>：進一步優化功耗同連接穩定性，增強週期性廣播。

<strong>LE Audio普及情況</strong>：2025-2026年，LE Audio已進入快速普及階段。主流品牌嘅新款真無線耳機（如華為FreeBuds Pro 5、小米Buds 6 Pro、三星Galaxy Buds3 Pro等）均已支援LE Audio同LC3編碼，提供更低延遲同更好音質。購買新耳機嗰陣，建議優先選擇支援LE Audio嘅產品。

##### 應用場景：

- <strong>音頻傳輸</strong>：無線耳機、車載音響。藍牙5.2嘅LE Audio等音質同延遲都有質嘅飛躍。
- <strong>數據傳輸</strong>：近距離傳檔案、相片。雖然速度唔及Wi-Fi Direct，但勝在簡單。
- <strong>設備配對</strong>：智能手錶、手環、鍵盤滑鼠、遊戲手柄。
- <strong>位置服務</strong>：藍牙信標（Beacon）用於室內導航、物品追蹤（如蘋果AirTag）。
- <strong>智能家居</strong>：藍牙Mesh網絡控制燈泡、門鎖等。

#### 四、紅外遙控：手機變身萬能遙控器

紅外遙控係最古老嘅無線控制技術之一，但喺手機上依然實用。部分安卓手機（如小米、華為部分機型）內置咗紅外發射器，可以遙控電視、冷氣、機頂盒等家電。

##### 工作原理：

紅外遙控通過紅外發光二極管發出特定頻率（通常38kHz）嘅紅外光脈衝信號，家電嘅紅外接收器解碼呢啲脈衝執行對應操作。唔同品牌使用唔同嘅編碼協議，常見嘅有NEC、RC5、RC6、SONY等。手機入面嘅紅外App內置咗各品牌嘅編碼庫，選擇品牌同型號就可以匹配。

##### 侷限性：

- <strong>方向性</strong>：紅外係直線傳播，需要對住設備發射，唔可以隔牆。
- <strong>距離短</strong>：有效距離一般5-8米。
- <strong>蘋果唔支援</strong>：iPhone冇紅外發射器，無法使用呢個功能。

#### 五、NFC：碰一碰嘅魔法

NFC（Near Field Communication，近場通信）係一種極短距離（10釐米以內）嘅高頻無線通信技術，工作頻率13.56MHz，傳輸速率最高424Kbps。

##### 通信原理與模式：

NFC基於RFID技術演變而嚟，支援三種工作模式：

- <strong>讀寫模式</strong>：手機讀取NFC標籤中嘅資訊，如讀取NFC貼紙觸發動作。
- <strong>點對點模式</strong>：兩台NFC設備互相傳輸數據，如Android Beam（已停用）。
- <strong>卡模擬模式</strong>：手機模擬一張智能卡，呢個係最常用嘅模式——公交卡、門禁卡、銀行卡都係呢個模式。

##### 安全機制：

- <strong>超短距離</strong>：10釐米內嘅通信距離本身就係物理安全保障，遠程竊聽幾乎唔可能。
- <strong>安全晶片</strong>：手機內置獨立嘅安全晶片（SE）或使用HCE（主機卡模擬），支付密鑰存儲喺安全區域，即使手機被root都無法提取。
- <strong>指紋/面容驗證</strong>：支付嗰陣需要生物識別確認，即使手機遺失都無法盜刷。
- <strong>令牌化</strong>：Apple Pay、華為Pay等唔傳輸真實卡號，而係使用一次性令牌，即使被截獲都無法重複使用。

##### 典型應用：

- <strong>公交卡/門禁卡</strong>：將實體卡資訊寫入手機，刷手機就得。
- <strong>流動支付</strong>：Apple Pay、華為Pay等，將銀行卡綁定到手機，碰一碰支付。
- <strong>設備配對</strong>：NFC碰一碰快速配對藍牙耳機、音箱。
- <strong>身份驗證</strong>：NFC身份證讀取、電子駕照驗證。

#### 六、個人熱點：將手機變Wi-Fi路由器

自己流量多嗰陣，可以開熱點畀平板、電腦用。

- <strong>開啟方法</strong>：設定 > 個人熱點/網絡共享，開啟佢。
- <strong>注意事項</strong>：好耗電同流量，記得設個複雜密碼，並限制連接設備數。
- <strong>USB共享</strong>：用數據線連電腦，比無線熱點更穩定、更快。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>動手試下：設定並管理熱點

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 打開 [設定]，揾到「個人熱點」或「網絡共享」，開啟佢，設好名稱同密碼。
2. 用另一台設備（比如電腦）搜尋並連接呢個Wi-Fi。
3. 喺手機端睇下，可唔可以管理已連接嘅設備，或踢走唔識嘅設備。
:::
