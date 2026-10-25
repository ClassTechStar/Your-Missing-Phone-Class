---
id: di-shi-wu-zhang
num: 15
part: jin-jie-pian
nav: 第十五章：電池科學與續航優化
toc: default
kind: chapter
---

### 第十五章：電池之理與續航之優化

{class="chapter-intro mb-4"}
電池乃君手機之"能量心臟"。此章帶君解電池之小脾氣，學科學之充電與續航之術，徹底告別電量焦慮。

#### 一、電池乃何物？循環與健康度

手機電池（鋰離子或鋰聚合物）如能量海綿：充電即吸水（存電），放電即擠水（用電）。有數特點值得記之：

- <strong>隨用隨充</strong>：與舊電池不同，其無記憶效應，無需非用完再充。
- <strong>怕熱</strong>：高溫乃電池頭號殺手。
- <strong>會老化</strong>：用久，最大容量即降，此乃正常之象。

##### 核心指標：循環次數與健康度

- 一次循環非充一次電。比如今日用60%充滿，明日用40%充滿，總耗100%電量方算一次循環。
- 電池健康度即當前最大容量佔全新時之百分比。低於80%時，君將明顯覺續航變短。
- <strong>何以看？</strong> iPhone：設置 &gt; 電池 &gt; 電池健康與充電；安卓：一般往設置中搜電池健康。

#### 二、充電玄學？快充、無線充與黃金之則

- <strong>快充傷電池？</strong> 用原裝或認證之快充配件，傷甚微。手機與充電頭有溫控，過熱將自動降功率。
- <strong>無線充電</strong>：便然效率較低，發熱更明顯。宜整夜充電。
- <strong>黃金養生之則</strong>：盡量使電量保持于20%-80%之間，勿老令其餓（0%）或撐（100%）。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>iPhone"80%充電限制"功能——以黃金法則變成系統設置

{class="mt-1"}
iPhone 15/16系列（iOS 17以上）已以"20%-80%法則"作成矣系統功能。開啓後，手機充至80%將自動停止充電，從而大幅延緩電池老化。設置路徑：

{class="mt-1"}
<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">設 &gt; 電池 &gt; 電池健康與充電 &gt; 充電優 &gt; 80%限</code>

{class="mt-1"}
三個選項之含義：①<strong>不限</strong>——充至100%；②<strong>優電池充電</strong>——學習汝之作息，唯於凌晨終一段延遲到100%；③<strong>80%限</strong>——直接停於80%，最護電池。長期於家/辦公室有充電條件之人，強烈建議選80%限制；屢出差、須滿電出門之人，可選優化電池充電。
:::

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-plug mr-2"></i>GaN充電器——出差黨之好搭檔

{class="mt-1"}
汝或注意至現在之快充頭越作越小，背後功臣乃<strong>GaN（氮化鎵）</strong>這種新型半導體材。相較傳統硅基充電器，GaN充電器有幾個明顯優勢：

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>體積小</strong>：同等功率下，GaN充電器可作至傳統硅基之1/2甚至1/3大小，65W功率之GaN頭比蘋果老之5W頭尚小。
- <strong>效高、發熱低</strong>：氮化鎵之開關損耗遠低於硅，能量轉換效率可達95%以上，充電時不容易燙手。
- <strong>適出差</strong>：一個65W或100W之GaN多口充電器，能同時賜手機、平板、筆記本充電，比帶三塊"磚頭"輕便得多。
- <strong>選購宜</strong>：認準支持PD協議之GaN充電器（65W起步可充筆電），知名品牌如倍思、安克、努比亞、小米等均可。注意覈對數據線是否匹配（高功率需用E-Marker芯片之Type-C線）。
:::

{id="di-shi-wu-zhang-kuichong"}
#### 三、快充協議全解：何以君之充電器充不快？

君或遇此情：明明手機支持快充，換充電器卻變得甚慢。此乃因快充非簡單"功率大即行"，乃需充電頭、數據線、手機三方"說同一種語言"——此即快充協議。

##### 1. 快充之基本原理

充電功率 = 電壓 × 電流（P = U × I）。欲提功率，或提電壓，或提電流，或二者皆提。不同協議擇不同之技術路線。

快充之工作流程：

1. <strong>握手階段</strong>：手機與充電頭通過數據線通信，交換各自支持之協議與功率信息。
2. <strong>協商階段</strong>：雙方確定一共同支持之最高功率檔位。
3. <strong>充電階段</strong>：充電頭按協商好之電壓電流輸出，手機端進行電源管理。
4. <strong>調整階段</strong>：隨電量增加，手機將逐步降充電功率，護電池。

##### 2. 主流快充協議詳解

<strong>USB PD（Power Delivery）</strong>——通用協議之王

- <strong>最高速率</strong>：USB-IF組織制定之官方標準，覆蓋範圍最廣。PD 3.0支持最高100W（20V/5A），PD 3.1擴展至240W（48V/5A）。
- <strong>電壓檔位</strong>：5V、9V、15V、20V，PD 3.1尚支持28V、36V、48V。
- <strong>技術路線</strong>：iPhone全系、谷歌Pixel、部分安卓旗艦、筆記本電腦、Switch遊戲機皆支持PD協議。
- <strong>優勢</strong>：通用性強，一充電頭可予多種設備充電；支持PPS（可編程電源），可精細調節電壓電流。
- <strong>劣勢</strong>：需Type-C接口與專用芯片，成本較高。

<strong>高通QC（Quick Charge）</strong>——安卓陣營之元老

- <strong>QC 3.0</strong>：支持3.6V-20V以0.2V爲步進之可調電壓，最高18W。
- <strong>QC 4.0/4+</strong>：兼容USB PD協議，支持最高27W，加入雙路充電技術。
- <strong>最廣泛</strong>：支持最高100W+，0-50%僅需5分鐘，大幅改善發熱。
- <strong>技術路線</strong>：用高通驍龍處理器之手機大多支持，然各品牌通常會優先用己之私有協議。

<strong>OPPO VOOC/一加WARP/真我Dart</strong>——低壓大電流之代表

- <strong>最高功率</strong>：低壓大電流（5V/4A起步），發熱更小，效率更高。
- <strong>VOOC 1.0</strong>：20W（5V/4A），2014年發佈，開創快充時代。
- <strong>SuperVOOC</strong>：50W-65W，採用雙電芯串聯設計。
- <strong>SuperVOOC 2.0</strong>：65W，30分鐘充滿4000mAh電池。
- <strong>150W/240W超級閃充</strong>：目前最快之量產快充技術。
- <strong>最高速率</strong>：需專用充電頭與數據線（有額外觸點），不兼容其他協議。

<strong>華爲SuperCharge</strong>——高壓快充之演進

- <strong>FCP（Fast Charge Protocol）</strong>：9V/2A，18W，兼容QC 2.0。
- <strong>SCP（Super Charge Protocol）</strong>：支持更高功率，自22.5W至66W再至100W。
- <strong>技術特點</strong>：採用電荷泵技術，將高壓轉爲低壓大電流輸入電池，效率高達98%。
- <strong>技術路線</strong>：華爲/榮耀手機專用，部分充電器支持PD協議。

<strong>小米澎湃快充</strong>——自研協議之崛起

- <strong>澎湃P1芯片</strong>：小米自研之快充管理芯片，支持120W有線快充。
- <strong>澎湃G1芯片</strong>：電池管理芯片，與P1配合實現更高效之快充。
- <strong>技術特點</strong>：採用雙電芯串聯+電荷泵方案，支持多種協議兼容。

<strong>華爲/榮耀</strong>——保守然穩定

- <strong>標準</strong>：僅支持USB PD協議。
- <strong>功率</strong>：iPhone 8及以後支持快充，最高約27W（iPhone 15 Pro Max可達27W+）。
- <strong>最高速率</strong>：功率相對保守，然充電曲線優化好，發熱控制出色。
- <strong>配件要求</strong>：需USB-C to Lightning線（或USB-C to USB-C線）與PD充電頭。

##### 3. 快充協議對比表

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-4">
                            <thead>
                                <tr class="bg-light dark:bg-gray-700">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">標準</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">協議</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">最高功率</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">技術路線</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">USB PD 3.1</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">VOOC/Dart</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">240W</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">高壓/多檔位</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最廣泛</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">QC 5.0</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">100W+</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">高壓可調</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">高通機型</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">VOOC/Dart</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">240W</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">低壓大電流</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OPPO系專用</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SuperCharge</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">100W</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">電荷泵</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">華爲/榮耀</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">蘋果快充</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">~27W</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">PD協議</td>
                                </tr>
                            </tbody>
                        </table>
```
:::

##### 4. 無線充電協議

無線充電亦有己之協議標準：

- <strong>Qi標準</strong>：WPC（無線充電聯盟）制定，最通用之標準。基礎Qi支持5W-15W。
- <strong>Qi2標準</strong>：2023年發佈，引入磁吸定位（類似蘋果MagSafe），支持15W+。
- <strong>私有協議</strong>：各品牌有己之高速無線充電，如小米50W無線充、華爲50W無線充等，需專用充電器。

##### 5. 快充選購指南

- <strong>視協議匹配</strong>：購充電器時，確認其支持君手機之快充協議。第三方充電器通常會標註支持之協議。
- <strong>視數據線</strong>：大功率快充需專用數據線。普通數據線或只支持60W以下。
- <strong>視認證</strong>：蘋果用戶議擇MFi認證之數據線；安卓用戶擇品牌原裝或知名第三方。
- <strong>視發熱</strong>：快充時手機發熱乃正常，然若燙手即不正常矣，議暫停充電或換充電器。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>快充安全提示

{class="list-disc pl-6 mt-1 space-y-1"}
- 避邊充邊玩大型遊戲，將加劇發熱。
- 避邊充邊玩大型遊戲，將加劇發熱。
- 充電時取掉厚重之手機殼，助散熱。
- 充電時取掉厚重之手機殼，助散熱。
:::

#### 四、電池新術：硅碳負極電池

若汝留意2024-2026年之旗艦手機發布將，"硅碳負極"此詞幾成矣高端電池之代名詞。這乃鋰電池負極材料之一次重要升級，原理實則不復雜：

- <strong>傳統石墨負極</strong>：手機電池始終用之乃石墨作負極，技術成熟、穩定，但能量密度已接近理論上限（約372mAh/g）。
- <strong>摻入硅材</strong>：硅之理論比容量乃石墨之10倍左右（約4200mAh/g）。以少量硅摻入石墨裏作成"硅碳複合負極"，遂能顯著提升整塊電池之能量密度。
- <strong>能量密度升</strong>：同等體積下，硅碳負極電池之容量可提升約<strong>15%-20%</strong>。這正是2024-2026年旗艦機能於7-9mm機身裏塞進5500-6000mAh大電池之關鍵原因。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>何機型用上矣？

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>榮耀</strong>：Magic系列率先商用硅碳負極，Magic6 Pro、Magic7系列、Magic V3折屏均用。
- <strong>小米</strong>：小米14 Ultra、小米15系列搭載新一代硅碳負極電池。
- <strong>vivo</strong>：X100 Ultra、X200 Pro系列用高密度硅碳負極策。
- <strong>華爲/OPPO等</strong>：2025-2026年旗艦普遍與進，硅碳負極方自"黑科技"變成高端機之標配。
:::

<strong>對用戶之實際影響</strong>：硅碳負極帶來之最大好處乃"同體積電池容量更大"——手機可作得更薄，同時續航不縮水；或機身不變厚，但電池自4500mAh漲至5500mAh。換句話說，汝不用爲續航付"厚重"之代價矣。須注意之乃，硅碳負極電池於低溫和滿充管理上仍需配合快充芯片作優化，這亦乃廠商建議長期保持80%充電之原因之一。

#### 五、這方乃真正之省電術

- <strong>屏幕（耗電之王）</strong>：調低亮度、縮短自動鎖屏之時。OLED屏手機開深色模式可省不少電。
- <strong>信號差</strong>：於電梯、地下室，手機將拼命搜信號，耗電極快。
- <strong>5G</strong>：若信號不佳，手切回4G，續航將佳多矣。
- <strong>定位服務</strong>：非導航類App，定位權限設爲"僅使用時允許"。
- <strong>限後臺活動</strong>：iPhone於設置 &gt; 通用 &gt; 後臺App刷新；安卓於應用電池設置中。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>查之：爲君之電池作個體檢

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 視健康度：覓並記下君之電池最大容量。
2. 視健康度：覓並記下君之電池最大容量。
3. 定對策：限後臺耗電異常之App。
:::
