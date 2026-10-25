---
id: di-shi-wu-zhang
num: 15
part: jin-jie-pian
nav: 第十五章：電池科學與續航最佳化
toc: default
kind: chapter
---

### 第十五章：電池科學與續航最佳化

{class="chapter-intro mb-4"}
電池就是你手機的"能量心臟"。這章帶你搞懂電池的小脾氣，學會科學的充電和續航技巧，徹底告別電量焦慮。

#### 一、電池是怎麼回事？迴圈與健康度

手機電池（鋰離子或鋰聚合物）像個能量海綿：充電就是吸水（存電），放電就是擠水（用電）。有幾個特點值得記住：

- <strong>隨用隨充</strong>：和舊電池不同，它沒有記憶效應，不用非得用完再充。
- <strong>怕熱</strong>：高溫是電池頭號殺手。
- <strong>會老化</strong>：用久了，最大容量就會下降，這是正常現象。

##### 核心指標：迴圈次數與健康度

- 一次迴圈不是充一次電。比如今天用60%充滿，明天用40%充滿，總消耗100%電量才算一次迴圈。
- 電池健康度就是當前最大容量佔全新時的百分比。低於80%時，你會明顯感覺續航變短。
- <strong>怎麼看？</strong> iPhone：設定 > 電池 > 電池健康與充電；安卓：一般去設定裡搜電池健康。

#### 二、充電玄學？快充、無線充與黃金法則

- <strong>快充傷電池？</strong> 用原裝或認證的快充配件，傷害很小。手機和充電頭有溫控，過熱會自動降功率。
- <strong>無線充電</strong>：方便但效率較低，發熱更明顯。適合整夜充電。
- <strong>黃金養生法則</strong>：儘量讓電量保持在20%-80%之間，別老讓它餓著（0%）或撐著（100%）。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>iPhone"80%充電限制"功能——把黃金法則變成系統設定

{class="mt-1"}
iPhone 15/16系列（iOS 17以上）已經把"20%-80%法則"做成了系統功能。開啟後，手機充到80%會自動停止充電，從而大幅延緩電池老化。設定路徑：

{class="mt-1"}
<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">設定 &gt; 電池 &gt; 電池健康與充電 &gt; 充電最佳化 &gt; 80%限制</code>

{class="mt-1"}
三個選項的含義：①<strong>不限</strong>——充到100%；②<strong>最佳化電池充電</strong>——學習你的作息，只在凌晨最後一段延遲到100%；③<strong>80%限制</strong>——直接停在80%，最護電池。長期在家/辦公室有充電條件的人，強烈建議選80%限制；經常出差、需要滿電出門的人，可以選最佳化電池充電。
:::

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-plug mr-2"></i>GaN充電器——出差黨的好搭檔

{class="mt-1"}
你可能注意到現在的快充頭越做越小，背後功臣是<strong>GaN（氮化鎵）</strong>這種新型半導體材料。相比傳統矽基充電器，GaN充電器有幾個明顯優勢：

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>體積小</strong>：同等功率下，GaN充電器可以做到傳統矽基的1/2甚至1/3大小，65W功率的GaN頭比蘋果老的5W頭還小。
- <strong>效率高、發熱低</strong>：氮化鎵的開關損耗遠低於矽，能量轉換效率可達95%以上，充電時不容易燙手。
- <strong>適合出差</strong>：一個65W或100W的GaN多口充電器，能同時給手機、平板、筆記本充電，比帶三塊"磚頭"輕便得多。
- <strong>選購建議</strong>：認準支援PD協議的GaN充電器（65W起步可充筆電），知名品牌如倍思、安克、努比亞、小米等均可。注意核對資料線是否匹配（高功率需用E-Marker晶片的Type-C線）。
:::

{id="di-shi-wu-zhang-kuichong"}
#### 三、快充協議全解析：為什麼你的充電器充不快？

你可能遇到過這種情況：明明手機支援快充，換了充電器卻變得很慢。這是因為快充不是簡單的"功率大就行"，而是需要充電頭、資料線、手機三方"說同一種語言"——這就是快充協議。

##### 1. 快充的基本原理

充電功率 = 電壓 × 電流（P = U × I）。要提升功率，要麼提高電壓，要麼提高電流，或者兩者都提高。不同協議選擇了不同的技術路線。

快充的工作流程：

1. <strong>握手階段</strong>：手機和充電頭透過資料線通訊，交換各自支援的協議和功率資訊。
2. <strong>協商階段</strong>：雙方確定一個共同支援的最高功率檔位。
3. <strong>充電階段</strong>：充電頭按協商好的電壓電流輸出，手機端進行電源管理。
4. <strong>調整階段</strong>：隨著電量增加，手機會逐步降低充電功率，保護電池。

##### 2. 主流快充協議詳解

<strong>USB PD（Power Delivery）</strong>——通用協議之王

- <strong>特點</strong>：USB-IF組織制定的官方標準，覆蓋範圍最廣。PD 3.0支援最高100W（20V/5A），PD 3.1擴充到240W（48V/5A）。
- <strong>電壓檔位</strong>：5V、9V、15V、20V，PD 3.1還支援28V、36V、48V。
- <strong>相容性</strong>：iPhone全系、谷歌Pixel、部分安卓旗艦、膝上型電腦、Switch遊戲機都支援PD協議。
- <strong>優勢</strong>：通用性強，一個充電頭可以給多種裝置充電；支援PPS（可程式設計電源），可以精細調節電壓電流。
- <strong>劣勢</strong>：需要Type-C介面和專用晶片，成本較高。

<strong>高通QC（Quick Charge）</strong>——安卓陣營的元老

- <strong>QC 3.0</strong>：支援3.6V-20V以0.2V為步進的可調電壓，最高18W。
- <strong>QC 4.0/4+</strong>：相容USB PD協議，支援最高27W，加入雙路充電技術。
- <strong>QC 5.0</strong>：支援最高100W+，0-50%僅需5分鐘，大幅改善發熱。
- <strong>相容性</strong>：使用高通驍龍處理器的手機大多支援，但各品牌通常會優先使用自己的私有協議。

<strong>OPPO VOOC/一加WARP/真我Dart</strong>——低壓大電流的代表

- <strong>技術路線</strong>：低壓大電流（5V/4A起步），發熱更小，效率更高。
- <strong>VOOC 1.0</strong>：20W（5V/4A），2014年釋出，開創快充時代。
- <strong>SuperVOOC</strong>：50W-65W，採用雙電芯串聯設計。
- <strong>SuperVOOC 2.0</strong>：65W，30分鐘充滿4000mAh電池。
- <strong>150W/240W超級閃充</strong>：目前最快的量產快充技術。
- <strong>特點</strong>：需要專用充電頭和資料線（有額外觸點），不相容其他協議。

<strong>華為SuperCharge</strong>——高壓快充的演進

- <strong>FCP（Fast Charge Protocol）</strong>：9V/2A，18W，相容QC 2.0。
- <strong>SCP（Super Charge Protocol）</strong>：支援更高功率，從22.5W到66W再到100W。
- <strong>技術特點</strong>：採用電荷泵技術，將高壓轉換為低壓大電流輸入電池，效率高達98%。
- <strong>相容性</strong>：華為/榮耀手機專用，部分充電器支援PD協議。

<strong>小米澎湃快充</strong>——自研協議的崛起

- <strong>澎湃P1晶片</strong>：小米自研的快充管理晶片，支援120W有線快充。
- <strong>澎湃G1晶片</strong>：電池管理晶片，與P1配合實現更高效的快充。
- <strong>技術特點</strong>：採用雙電芯串聯+電荷泵方案，支援多種協議相容。

<strong>蘋果快充</strong>——保守但穩定

- <strong>協議</strong>：僅支援USB PD協議。
- <strong>功率</strong>：iPhone 8及以後支援快充，最高約27W（iPhone 15 Pro Max可達27W+）。
- <strong>特點</strong>：功率相對保守，但充電曲線最佳化好，發熱控制出色。
- <strong>配件要求</strong>：需要USB-C to Lightning線（或USB-C to USB-C線）和PD充電頭。

##### 3. 快充協議對比表

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-4">
                            <thead>
                                <tr class="bg-light dark:bg-gray-700">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">協議</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">最高功率</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">技術路線</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">相容性</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">USB PD 3.1</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">240W</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">高壓/多檔位</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最廣泛</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">QC 5.0</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">100W+</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">高壓可調</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">高通機型</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">VOOC/Dart</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">240W</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">低壓大電流</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OPPO系專用</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SuperCharge</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">100W</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">電荷泵</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">華為/榮耀</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">蘋果快充</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">~27W</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">PD協議</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">iPhone/iPad</td>
                                </tr>
                            </tbody>
                        </table>
```
:::

##### 4. 無線充電協議

無線充電也有自己的協議標準：

- <strong>Qi標準</strong>：WPC（無線充電聯盟）制定，最通用的標準。基礎Qi支援5W-15W。
- <strong>Qi2標準</strong>：2023年釋出，引入磁吸定位（類似蘋果MagSafe），支援15W+。
- <strong>私有協議</strong>：各品牌有自己的高速無線充電，如小米50W無線充、華為50W無線充等，需要專用充電器。

##### 5. 快充選購指南

- <strong>看協議匹配</strong>：購買充電器時，確認它支援你手機的快充協議。第三方充電器通常會標註支援的協議。
- <strong>看資料線</strong>：大功率快充需要專用資料線。普通資料線可能只支援60W以下。
- <strong>看認證</strong>：蘋果使用者建議選擇MFi認證的資料線；安卓使用者選擇品牌原裝或知名第三方。
- <strong>看發熱</strong>：快充時手機發熱是正常的，但如果燙手就不正常了，建議暫停充電或更換充電器。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>快充安全提示

{class="list-disc pl-6 mt-1 space-y-1"}
- 避免邊充邊玩大型遊戲，會加劇發熱。
- 不要使用劣質充電器和資料線，可能導致安全隱患。
- 充電時取掉厚重的手機殼，幫助散熱。
- 如果充電器或手機異常發熱、有異味，立即停止使用。
:::

#### 四、電池新技術：矽碳負極電池

如果你留意2024-2026年的旗艦手機釋出會，"矽碳負極"這個詞幾乎成了高階電池的代名詞。這是鋰電池負極材料的一次重要升級，原理其實不復雜：

- <strong>傳統石墨負極</strong>：手機電池一直用的是石墨做負極，技術成熟、穩定，但能量密度已接近理論上限（約372mAh/g）。
- <strong>摻入矽材料</strong>：矽的理論比容量是石墨的10倍左右（約4200mAh/g）。把少量矽摻入石墨裡做成"矽碳複合負極"，就能顯著提升整塊電池的能量密度。
- <strong>能量密度提升</strong>：同等體積下，矽碳負極電池的容量可以提升約<strong>15%-20%</strong>。這正是2024-2026年旗艦機能在7-9mm機身裡塞進5500-6000mAh大電池的關鍵原因。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>哪些機型用上了？

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>榮耀</strong>：Magic系列率先商用矽碳負極，Magic6 Pro、Magic7系列、Magic V3摺疊屏均採用。
- <strong>小米</strong>：小米14 Ultra、小米15系列搭載新一代矽碳負極電池。
- <strong>vivo</strong>：X100 Ultra、X200 Pro系列使用高密度矽碳負極方案。
- <strong>華為/OPPO等</strong>：2025-2026年旗艦普遍跟進，矽碳負極正在從"黑科技"變成高階機的標配。
:::

<strong>對使用者的實際影響</strong>：矽碳負極帶來的最大好處是"同體積電池容量更大"——手機可以做得更薄，同時續航不縮水；或者機身不變厚，但電池從4500mAh漲到5500mAh。換句話說，你不用為續航付"厚重"的代價了。需要注意的是，矽碳負極電池在低溫和滿充管理上仍需配合快充晶片做最佳化，這也是廠商建議長期保持80%充電的原因之一。

#### 五、這才是真正的省電技巧

- <strong>螢幕（耗電王）</strong>：調低亮度、縮短自動鎖屏時間。OLED屏手機開深色模式能省不少電。
- <strong>訊號差</strong>：在電梯、地下室，手機會拼命搜訊號，耗電極快。
- <strong>5G</strong>：如果訊號不好，手動切回4G，續航會好很多。
- <strong>定位服務</strong>：非導航類App，定位許可權設為"僅使用時允許"。
- <strong>限制後臺活動</strong>：iPhone在設定 > 通用 > 後臺App重新整理；安卓在應用電池設定裡。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>來檢查一下：給你的電池做個體檢

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 檢視健康度：找到並記下你的電池最大容量。
2. 分析耗電詳情：看電池設定裡的圖表和App列表，找出耗電元兇。
3. 制定對策：限制後臺耗電異常的App。
:::
