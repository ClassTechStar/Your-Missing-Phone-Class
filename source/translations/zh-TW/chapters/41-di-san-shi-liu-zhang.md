---
id: di-san-shi-liu-zhang
num: 36
part: er-tong-pian
nav: 第三十六章：手機與智慧家居——讓家變聰明
toc: default
kind: chapter
---

### 第三十六章：手機與智慧家居——讓家變聰明

{class="chapter-intro mb-4"}
手機還能幹一件越來越重要的事——當整個家的"遙控器"。從一盞燈、一個插座到一把門鎖，智慧家居正在從"極客玩具"變成"家常配置"。這一章幫你理清協議、生態、中樞和入門套件，再用一份安全清單收尾，讓你不被"智慧"反噬。

#### 一、智慧家居協議：選誰很重要

買智慧裝置前先看它支援什麼協議，這決定了它能不能被你的手機和生態"使喚"。目前主流協議有四種，各自的脾氣如下：

- Matter協議：2022年由CSA（連線標準聯盟）釋出，背後是蘋果、谷歌、亞馬遜、三星等巨頭聯手。它的目標只有一個——讓所有品牌的智慧裝置說同一種語言。2023-2026年正快速成為統一標準，支援它的裝置可同時接入Apple HomeKit、Google Home、Amazon Alexa和米家，不再被單一生態綁架。
- Thread協議：Matter的底層網路"管道"。低功耗、自組網（某個節點斷電，訊號會自動繞路），響應快、不卡頓。買帶Thread邊界路由器的裝置（如HomePod mini、Apple TV 4K、小米中樞閘道器），體驗明顯更穩。
- Wi-Fi：頻寬大、能直連路由器，但功耗高、裝置多了易擠佔通道，適合相機、掃地機這類需要傳大資料的裝置。
- 藍芽（BLE）：配網簡單、省電，但距離短、不能自組網，適合門鎖、溫溼度計這類小資料裝置。
- Zigbee：老牌低功耗自組網協議，需要專用閘道器，裝置便宜穩定，但跨品牌互通差，正被Matter+Thread逐步替代。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
一句話原則

{class="mt-1"}
2026年買智慧裝置，優先看是否有"Matter over Thread"標識——這是當下最經得起時間檢驗的選擇。老裝置若只支援Wi-Fi或藍芽也不必急著淘汰，先用著，新購時再轉向Matter。
:::

#### 二、三大生態對比

協議是"語言"，生態是"圈子"。即使都支援Matter，你日常仍要選一個主生態來搭自動化和語音控制。三大主流生態對比如下：

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                    <thead>
                        <tr class="bg-light dark:bg-gray-700">
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">生態</th>
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">優勢</th>
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">短板</th>
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">適用人群</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple HomeKit</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">隱私最強（本地處理為主）、與iPhone/Siri/快捷指令聯動順滑</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">裝置偏少偏貴、需要HomePod或Apple TV做中樞</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全家蘋果裝置、重視隱私與體驗的使用者</td>
                        </tr>
                        <tr>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">米家（小米）</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">裝置最豐富、價效比最高、小愛同學好用</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">生態相對封閉、資料多上雲、廣告偏多</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">預算有限、想一站式配齊全屋的入門使用者</td>
                        </tr>
                        <tr>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">華為智聯（鴻蒙）</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">與鴻蒙手機/平板/手錶無縫流轉、裝置數量快速增長</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">海外裝置支援少、生態仍在追趕</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">華為手機使用者、看重"超級終端"多裝置協同</td>
                        </tr>
                    </tbody>
                </table>
```

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
選生態的決策建議

{class="mt-1"}
看手機選生態：iPhone使用者優先HomeKit，華為使用者優先智聯，其他安卓使用者米家最省心。靠Matter協議，不同生態的裝置也能被同一部手機控制，不必一次性"站隊"。
:::

#### 三、手機當家居中樞

在多數入門場景裡，手機就是你的"家居中樞"——透過App控制燈光、空調、窗簾、安防，還能搭建自動化場景，讓家"自己動起來"：

- 裝置控制：開啟HomeKit/米家/智慧生活App，可遠端或本地開關燈、調色溫、設定空調溫度、拉合窗簾、檢視相機畫面。
- 自動化場景：把"條件→動作"組合起來，常用的三大場景： 回家模式：定位到家+天黑→開玄關燈+開空調+拉窗簾+關門鎖。
- 離家模式：最後一個出門（定位離家或門鎖上鎖）→關燈+關空調+關插座+啟動相機+佈防。
- 睡眠模式：每晚23:00→關全屋主燈+拉窗簾+空調切26度+開夜燈。

- NFC碰一碰：在門貼一張NFC標籤，手機一碰即觸發對應場景（碰一下開門燈、再碰一下切睡眠）。iPhone用"快捷指令"自動化，安卓用"錢包"或廠商App均可寫入。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來試試：搭一個"回家模式"

{class="mt-1"}
在手機智慧家居App的"自動化"裡新增一條：觸發條件選"到達某地點"（家），動作依次加"開玄關燈""空調設26度""窗簾關閉"。儲存後出門逛一圈，回家時看它是否自己亮燈——第一次成功的成就感，比下單新裝置還過癮。
:::

#### 四、入門套件推薦

不必一次配齊，從這四件套開始，就能覆蓋八成日常需求：

- 智慧音箱：小愛同學（米家生態，價效比高）/ HomePod mini（蘋果生態，兼作Thread中樞）/ Alexa（海外生態廣）。注意：音箱決定了你的語音生態，先定生態再買音箱。
- 智慧燈泡：Yeelight（米家/Matter，色溫亮度可調，便宜）/ Philips Hue（色彩好、穩定，但需Hue閘道器，偏貴）。注意：買前確認燈座口徑（E27/B22）和是否需要調色。
- 智慧插座：小米智慧插座（便宜、電量統計）/ TP-Link Kasa（海外Matter支援好）。注意：用在大功率電器（熱水器、電暖器）時務必看額定功率，別過載。
- 智慧門鎖：鹿客/小米（價效比、米家聯動）/ 凱迪仕（傳統鎖具大廠、機械結構紮實）。注意：確認是否支援Matter或你所在生態，留意電池續航和應急鑰匙孔位置。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
選購順序建議

{class="mt-1"}
先買智慧音箱（定生態）→ 再買智慧燈泡和插座（低門檻、立刻有反饋）→ 最後買門鎖和相機（涉及安全，謹慎選）。一次只加一類裝置，熟悉後再擴，避免"買回來不會用"。
:::

#### 五、安全注意事項

智慧裝置越多的家，攻擊面也越大。下面四條是底線，請逐條對照：

1. 改預設密碼：相機、路由器、門鎖出廠預設密碼在網上全是公開的，買到手第一件事就是改成"長且不重複"的強密碼。
2. 及時更新韌體：廠商推送的韌體往往修復了安全漏洞，在App裡開啟"自動更新"，或至少每月手動檢查一次。
3. 網路隔離：把IoT裝置單獨放到一個Wi-Fi（或訪客網路）上，和手機、電腦的主網路分開。萬一某個裝置被攻破，也難以橫向威脅你的重要資料。
4. 隱私保護：相機開啟"隱私區域"遮蔽（如臥室、衛生間不拍），關閉雲端24小時錄影；不在家的相機畫面別長期開給第三方App。

::: div .danger-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
這幾個坑別踩

{class="list-disc pl-6 mt-1 space-y-1"}
- 別用門鎖的"遠端開鎖"功能給陌生人——優先用臨時密碼，用完即失效。
- 別把相機直接對著床、對著窗外——洩露的是你自己的隱私。
- 別圖便宜買"白牌"無品牌裝置——多半不更新韌體，等於給家裡安了個後門。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

{class="list-disc pl-5 text-sm space-y-0.5"}
- Matter+Thread是2023-2026年的統一方向，買新裝置優先看這個標識
- 三大生態各有所長：蘋果重隱私體驗、米家重價效比、華為重多裝置協同
- 手機可當中樞，搭好"回家/離家/睡眠"三大場景，家就能自己動起來
- 入門四件套：智慧音箱、燈泡、插座、門鎖，按這個順序逐步添置
- 改預設密碼、更新韌體、網路隔離、隱私遮蔽——四條安全底線不能省
:::
