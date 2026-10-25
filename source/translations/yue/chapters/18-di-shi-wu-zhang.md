---
id: di-shi-wu-zhang
num: 15
part: jin-jie-pian
nav: 第十五章：電池科學與續航優化
toc: default
kind: chapter
---

### 第十五章：電池科學與續航優化

{class="chapter-intro mb-4"}
電池就係你手機嘅「能量心臟」。呢章帶你搞掂電池嘅小脾氣，學識科學嘅充電同續航技巧，徹底告別電量焦慮。

#### 一、電池係點回事？循環與健康度

手機電池（鋰離子或鋰聚合物）好似一塊能量海綿：充電就係吸水（存電），放電就係揸水（用電）。有幾個特點值得記住：

- <strong>隨用隨充</strong>：同舊電池唔同，佢冇記憶效應，唔使一定要用完再充。
- <strong>怕熱</strong>：高温係電池頭號殺手。
- <strong>會老化</strong>：用得耐，最大容量就會下降，呢個係正常現象。

##### 核心指標：循環次數與健康度

- 一次循環唔係充一次電。比如今日用60%充滿，聽日用40%充滿，總消耗100%電量先算一次循環。
- 電池健康度就係當前最大容量佔全新時嘅百分比。低於80%時，你會明顯感覺續航變短。
- <strong>點樣睇？</strong> iPhone：設定 > 電池 > 電池健康與充電；安卓：一般去設定入面搜電池健康。

#### 二、充電玄學？快充、無線充與黃金法則

- <strong>快充傷電池？</strong> 用原裝或認證嘅快充配件，傷害好細。手機同充電頭有温控，過熱會自動降功率。
- <strong>無線充電</strong>：方便但效率較低，發熱更明顯。適合成晚充電。
- <strong>黃金養生法則</strong>：盡量等電量保持喺20%-80%之間，唔好成日等佢餓住（0%）或撐住（100%）。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>iPhone「80%充電限制」功能——將黃金法則變成系統設定

{class="mt-1"}
iPhone 15/16系列（iOS 17以上）已經將「20%-80%法則」做成咗系統功能。開啟後，手機充到80%會自動停止充電，從而大幅延緩電池老化。設定路徑：

{class="mt-1"}
<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">設定 &gt; 電池 &gt; 電池健康與充電 &gt; 充電優化 &gt; 80%限制</code>

{class="mt-1"}
三個選項嘅含義：①<strong>不限</strong>——充到100%；②<strong>優化電池充電</strong>——學習你嘅作息，淨係喺凌晨最後一段延遲到100%；③<strong>80%限制</strong>——直接停喺80%，最護電池。長期喺屋企/辦公室有充電條件嘅人，強烈建議選80%限制；經常出差、需要滿電出門嘅人，可以選優化電池充電。
:::

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-plug mr-2"></i>GaN充電器——出差黨嘅好拍檔

{class="mt-1"}
你可能注意到而家嘅快充頭越做越細，背後功臣係<strong>GaN（氮化鎵）</strong>呢種新型半導體材料。相比傳統矽基充電器，GaN充電器有幾個明顯優勢：

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>體積細</strong>：同等功率下，GaN充電器可以做到傳統矽基嘅1/2甚至1/3大細，65W功率嘅GaN頭比蘋果舊嘅5W頭仲細。
- <strong>效率高、發熱低</strong>：氮化鎵嘅開關損耗遠低於矽，能量轉換效率可達95%以上，充電時唔容易燙手。
- <strong>適合出差</strong>：一個65W或100W嘅GaN多口充電器，可以同時畀手機、平板、筆記本充電，比帶三塊「磚頭」輕便得多。
- <strong>選購建議</strong>：認準支援PD協議嘅GaN充電器（65W起步可充筆電），知名品牌如倍思、安克、努比亞、小米等均可。注意核對數據線係咪匹配（高功率需用E-Marker晶片嘅Type-C線）。
:::

{id="di-shi-wu-zhang-kuichong"}
#### 三、快充協議全解析：點解你嘅充電器充唔快？

你可能遇過呢種情況：明明手機支援快充，換咗充電器卻變得好慢。呢個係因為快充唔係簡單嘅「功率大就得」，而係需要充電頭、數據線、手機三方「講同一種語言」——呢個就係快充協議。

##### 1. 快充嘅基本原理

充電功率 = 電壓 × 電流（P = U × I）。要提升功率，要麼提高電壓，要麼提高電流，或者兩者都提高。唔同協議選擇咗唔同嘅技術路線。

快充嘅工作流程：

1. <strong>握手階段</strong>：手機同充電頭通過數據線通信，交換各自支援嘅協議同功率資訊。
2. <strong>協商階段</strong>：雙方確定一個共同支援嘅最高功率檔位。
3. <strong>充電階段</strong>：充電頭按協商好嘅電壓電流輸出，手機端進行電源管理。
4. <strong>調整階段</strong>：隨住電量增加，手機會逐步降低充電功率，保護電池。

##### 2. 主流快充協議詳解

<strong>USB PD（Power Delivery）</strong>——通用協議之王

- <strong>特點</strong>：USB-IF組織制定嘅官方標準，覆蓋範圍最廣。PD 3.0支援最高100W（20V/5A），PD 3.1擴展到240W（48V/5A）。
- <strong>電壓檔位</strong>：5V、9V、15V、20V，PD 3.1仲支援28V、36V、48V。
- <strong>兼容性</strong>：iPhone全系、谷歌Pixel、部分安卓旗艦、筆記本電腦、Switch遊戲機都支援PD協議。
- <strong>優勢</strong>：通用性強，一個充電頭可以畀多種設備充電；支援PPS（可編程電源），可以精細調節電壓電流。
- <strong>劣勢</strong>：需要Type-C介面同專用晶片，成本較高。

<strong>高通QC（Quick Charge）</strong>——安卓陣營嘅元老

- <strong>QC 3.0</strong>：支援3.6V-20V以0.2V為步進嘅可調電壓，最高18W。
- <strong>QC 4.0/4+</strong>：兼容USB PD協議，支援最高27W，加入雙路充電技術。
- <strong>QC 5.0</strong>：支援最高100W+，0-50%僅需5分鐘，大幅改善發熱。
- <strong>兼容性</strong>：使用高通驍龍處理器嘅手機大多支援，但各品牌通常會優先使用自己嘅私有協議。

<strong>OPPO VOOC/一加WARP/真我Dart</strong>——低壓大電流嘅代表

- <strong>技術路線</strong>：低壓大電流（5V/4A起步），發熱更細，效率更高。
- <strong>VOOC 1.0</strong>：20W（5V/4A），2014年發布，開創快充時代。
- <strong>SuperVOOC</strong>：50W-65W，採用雙電芯串聯設計。
- <strong>SuperVOOC 2.0</strong>：65W，30分鐘充滿4000mAh電池。
- <strong>150W/240W超級閃充</strong>：目前最快嘅量產快充技術。
- <strong>特點</strong>：需要專用充電頭同數據線（有額外觸點），唔兼容其他協議。

<strong>華為SuperCharge</strong>——高壓快充嘅演進

- <strong>FCP（Fast Charge Protocol）</strong>：9V/2A，18W，兼容QC 2.0。
- <strong>SCP（Super Charge Protocol）</strong>：支援更高功率，由22.5W到66W再到100W。
- <strong>技術特點</strong>：採用電荷泵技術，將高壓轉換為低壓大電流輸入電池，效率高達98%。
- <strong>兼容性</strong>：華為/榮耀手機專用，部分充電器支援PD協議。

<strong>小米澎湃快充</strong>——自研協議嘅崛起

- <strong>澎湃P1晶片</strong>：小米自研嘅快充管理晶片，支援120W有線快充。
- <strong>澎湃G1晶片</strong>：電池管理晶片，同P1配合實現更高效嘅快充。
- <strong>技術特點</strong>：採用雙電芯串聯+電荷泵方案，支援多種協議兼容。

<strong>蘋果快充</strong>——保守但穩定

- <strong>協議</strong>：淨係支援USB PD協議。
- <strong>功率</strong>：iPhone 8及以後支援快充，最高約27W（iPhone 15 Pro Max可達27W+）。
- <strong>特點</strong>：功率相對保守，但充電曲線優化好，發熱控制出色。
- <strong>配件要求</strong>：需要USB-C to Lightning線（或USB-C to USB-C線）同PD充電頭。

##### 3. 快充協議對比表

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-4">
                            <thead>
                                <tr class="bg-light dark:bg-gray-700">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">協議</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">最高功率</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">技術路線</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">兼容性</th>
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

無線充電都有自己嘅協議標準：

- <strong>Qi標準</strong>：WPC（無線充電聯盟）制定，最通用嘅標準。基礎Qi支援5W-15W。
- <strong>Qi2標準</strong>：2023年發布，引入磁吸定位（類似蘋果MagSafe），支援15W+。
- <strong>私有協議</strong>：各品牌有自己嘅高速無線充電，如小米50W無線充、華為50W無線充等，需要專用充電器。

##### 5. 快充選購指南

- <strong>睇協議匹配</strong>：購買充電器時，確認佢支援你手機嘅快充協議。第三方充電器通常會標註支援嘅協議。
- <strong>睇數據線</strong>：大功率快充需要專用數據線。普通數據線可能只支援60W以下。
- <strong>睇認證</strong>：蘋果用戶建議選擇MFi認證嘅數據線；安卓用戶選擇品牌原裝或知名第三方。
- <strong>睇發熱</strong>：快充時手機發熱係正常嘅，但如果燙手就唔正常喇，建議暫停充電或更換充電器。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>快充安全提示

{class="list-disc pl-6 mt-1 space-y-1"}
- 避免邊充邊玩大型遊戲，會加劇發熱。
- 唔好使用劣質充電器同數據線，可能導致安全隱患。
- 充電時除掉厚重嘅手機殼，幫助散熱。
- 如果充電器或手機異常發熱、有異味，立即停止使用。
:::

#### 四、電池新技術：矽碳負極電池

如果你留意2024-2026年嘅旗艦手機發布會，「矽碳負極」呢個詞幾乎成咗高端電池嘅代名詞。呢個係鋰電池負極材料嘅一次重要升級，原理其實唔複雜：

- <strong>傳統石墨負極</strong>：手機電池一直用嘅係石墨做負極，技術成熟、穩定，但能量密度已接近理論上限（約372mAh/g）。
- <strong>摻入矽材料</strong>：矽嘅理論比容量係石墨嘅10倍左右（約4200mAh/g）。將少量矽摻入石墨入面做成「矽碳複合負極」，就可以顯著提升整塊電池嘅能量密度。
- <strong>能量密度提升</strong>：同等體積下，矽碳負極電池嘅容量可以提升約<strong>15%-20%</strong>。呢個正係2024-2026年旗艦機可以喺7-9mm機身入面塞進5500-6000mAh大電池嘅關鍵原因。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>邊啲機型用上咗？

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>榮耀</strong>：Magic系列率先商用矽碳負極，Magic6 Pro、Magic7系列、Magic V3摺疊屏均採用。
- <strong>小米</strong>：小米14 Ultra、小米15系列搭載新一代矽碳負極電池。
- <strong>vivo</strong>：X100 Ultra、X200 Pro系列使用高密度矽碳負極方案。
- <strong>華為/OPPO等</strong>：2025-2026年旗艦普遍跟進，矽碳負極正在由「黑科技」變成高端機嘅標配。
:::

<strong>對用戶嘅實際影響</strong>：矽碳負極帶嚟嘅最大好處係「同體積電池容量更大」——手機可以做得更薄，同時續航唔縮水；或者機身不變厚，但電池由4500mAh漲到5500mAh。換句話講，你唔使為續航付「厚重」嘅代價喇。需要注意嘅係，矽碳負極電池喺低温同滿充管理上仍需配合快充晶片做優化，呢個都係廠商建議長期保持80%充電嘅原因之一。

#### 五、呢個先係真正嘅省電技巧

- <strong>螢幕（耗電王）</strong>：調低亮度、縮短自動鎖屏時間。OLED屏手機開深色模式可以省唔少電。
- <strong>訊號差</strong>：喺電梯、地下室，手機會拼命搜訊號，耗電極快。
- <strong>5G</strong>：如果訊號唔好，手動切返4G，續航會好好多。
- <strong>定位服務</strong>：非導航類App，定位權限設為「僅使用時允許」。
- <strong>限制後台活動</strong>：iPhone喺設定 > 通用 > 後台App刷新；安卓喺應用電池設定入面。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>嚟檢查一下：畀你嘅電池做個體檢

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 查看健康度：揾到並記低你嘅電池最大容量。
2. 分析耗電詳情：睇電池設定入面嘅圖表同App列表，揾出耗電元兇。
3. 制定對策：限制後台耗電異常嘅App。
:::
