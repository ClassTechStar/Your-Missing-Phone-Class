---
id: di-er-shi-wu-zhang
num: 25
part: chao-yue-pian
nav: 第二十五章：二手手機處理與數字遺產
toc: default
kind: chapter
---

### 第二十五章：二手手機處理與數字遺產

{class="chapter-intro mb-4"}
嘿，夥計們，經過前面二十多章的"修煉"，相信你已經從一個"數字小白"成長為一名相當從容的手機使用者了。但科技生活總有輪迴——新歡終會變舊愛。當你準備讓老夥計"退役"時，你知道該如何體面、安全地告別嗎？

#### 一、舊手機的"安樂死"：安全出售或轉贈指南

核心原則：資料清理不是"刪除"，而是"覆蓋"。許多人以為把照片拖進回收站、清空相簿就萬事大吉，結果手機轉手後，新主人用資料恢復軟體一掃，老照片、聊天記錄、身份證照片全回來了——這種"社死現場"每年都在上演。

1. <strong>自我"大掃除"</strong>：完成最後一次完整備份，退出所有帳號（iCloud、華為/小米/三星帳號、Google帳號），關閉"查詢我的手機"功能——否則下一位使用者會被啟用鎖攔在門外。
2. <strong>執行終極"格式化"</strong>：現代手機的"恢復出廠設定"通常包含加密擦除——它銷燬的是加密金鑰本身，金鑰一沒，整盤資料瞬間變為亂碼。
3. <strong>最後的"障眼法"（僅老裝置需要）</strong>：現代手機（iOS 8+、Android 6+）已預設全盤加密（FBE），恢復出廠設定會銷燬加密金鑰，資料理論上不可恢復，<strong>無需此步驟</strong>。僅對極老舊的非加密裝置（2015年前），才需要在恢復出廠設定後用垃圾檔案填滿儲存，再執行一次恢復出廠設定。

<strong>各品牌資料擦除路徑速查表</strong>：儘管原理相通，但每個品牌把"恢復出廠設定"藏的位置略有不同，關鍵差異如下。

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">品牌</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">擦除入口</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">關鍵差異與注意事項</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">華為</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">設定 > 系統和更新 > 重置 > 恢復出廠設定</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需先退出華為帳號並關閉"查詢我的手機"，否則會觸發啟用鎖；純淨模式下可能需要密碼驗證。</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">小米 / Redmi</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">設定 > 我的裝置 > 恢復出廠設定</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">底部有"格式化虛擬SD卡"和"清除全部內容與設定"選項，二者都要勾選；退出小米帳號前先關閉"查詢裝置"。</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OPPO / 一加</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">設定 > 其他設定 > 還原手機 > 徹底清除全部資料</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ColorOS 提供"徹底清除"模式，會多次覆蓋儲存；需輸入鎖屏密碼確認。</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">vivo</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">設定 > 系統管理 > 備份與重置 > 清除所有資料</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">勾選"格式化手機儲存"才會清理SD卡區；需退出vivo帳號，關閉"查詢手機"。</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">三星</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">設定 > 通用管理 > 重置 > 恢復出廠設定</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需先移除Samsung帳號並關閉"查詢我的手機"；部分機型有"自動覆蓋"選項，建議開啟。</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">iPhone</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">設定 > 通用 > 傳輸或還原iPhone > 抹掉所有內容和設定</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">必須先退出Apple ID，否則下一位使用者被iCloud啟用鎖攔住；iOS 15+支援"退出時保留iCloud資料"以備後查。</td>
                            </tr>
                        </tbody>
                    </table>
```

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>最容易被忽略的三件事

{class="list-disc pl-6 mt-2 space-y-1"}
- <strong>未退出帳號</strong>：手機賣給下家後被遠端鎖定，自己也下不來，最後只能持身份證去官方售後解鎖。
- <strong>SD卡未取出</strong>：恢復出廠設定不會格式化外接SD卡裡的照片，記得手動取出或單獨格式化。
- <strong>隨身碟/OTG外設未斷開</strong>：擦除過程中如果連著外設，可能誤清外設資料，也可能導致擦除中斷。
:::

#### 二、數字遺產：你的社交靈魂如何安放？

手機裡的資料，早就不是"虛擬"的了。它承載著你的資金、社交關係、創作成果，乃至你的"數字身份"。<strong>一個人去世後，這些資產該怎麼處理？</strong>這不再是一個抽象問題，而是越來越多家庭真實面臨的難題——親屬不知道密碼、平臺不讓繼承、加密貨幣永遠丟失。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-gavel mr-2"></i>法律依據：個人資訊保護法第49條

{class="mt-1"}
2021年施行的《中華人民共和國個人資訊保護法》第49條明確規定：<strong>自然人死亡的，其近親屬為了自身的合法、正當利益，可以對死者相關個人資訊行使本章規定的查閱、複製、更正、刪除等權利；死者生前另有安排的除外。</strong>

{class="mt-2"}
這意味著：

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>近親屬有法律依據</strong>向平臺申請處理死者的帳號與個人資訊。
- "合法、正當利益"通常包括辦理遺產繼承、關閉帳號、刪除敏感隱私等。
- 死者生前若有遺囑或協議另行安排（如指定遺產聯絡人），從其約定。
- 平臺不能以"使用者隱私"為由一概拒絕配合，但具體流程各家不同。
:::

{class="font-semibold mt-4 mb-1"}
##### 1. 微信與支付寶：帳號不能繼承，但資金可以

這兩個中國人最常用的App，規則各不相同：

- <strong>微信帳號</strong>：依據《騰訊微信軟體許可及服務協議》，帳號所有權歸騰訊，使用者僅享有使用權，<strong>帳號本身不能繼承、不能轉讓</strong>。但帳號內的<strong>零錢、零錢通資金</strong>屬於個人財產，近親屬可憑死亡證明、親屬關係證明、繼承公證書向財付通申請提現或轉移。
- <strong>支付寶</strong>：帳號同樣不能直接繼承，但支付寶餘額、餘額寶、理財通等<strong>資金屬於可繼承財產</strong>。繼承人可透過支付寶"客服熱線"或線下提交死亡證明、繼承公證書辦理；螞蟻財富類理財產品需走基金公司流程。
- <strong>聊天記錄</strong>：法律上屬個人隱私，平臺不會主動提供給家屬。如涉及遺產線索，可透過訴訟或公證申請調取。

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>千萬別做的事

{class="list-disc pl-6 mt-2 space-y-1"}
- <strong>不要把死者帳號密碼直接交給家人"接著用"</strong>——這違反平臺協議，資金被凍結甚至觸發風控時舉證更難。
- <strong>不要嘗試用死者手機收驗證碼"提現"</strong>——可能被認定為盜用，反而觸犯法律。
- <strong>不要拖延</strong>：部分帳號長期未登入會被自動登出，資金找回會更麻煩。
:::

{class="font-semibold mt-4 mb-1"}
##### 2. Apple"遺產聯絡人"：提前指定，事半而功倍

iOS 15.2 起蘋果推出"遺產聯絡人"功能，允許使用者提前指定信任的聯絡人，去世後該聯絡人可憑<strong>死亡證明 + 遺產聯絡人訪問金鑰</strong>申請訪問死者的iCloud資料（照片、備忘錄、通訊錄、備忘錄等）。操作步驟：

1. 在iPhone上進入 <strong>[設定] &gt; [你的姓名] &gt; [登入與安全] &gt; [遺產聯絡人]</strong>。
2. 點選"新增遺產聯絡人"，使用面容ID確認身份。
3. 選擇聯絡人（從通訊錄挑選），系統會生成一份<strong>訪問金鑰</strong>。
4. 將訪問金鑰透過簡訊、郵件或列印紙質件交給對方，並提醒對方妥善儲存。
5. 可新增多個聯絡人作為備份，避免單點失效。

被指定人無需Apple裝置，憑金鑰和死亡證明即可在蘋果官網申請訪問。整個流程通常在7天內完成。

{class="font-semibold mt-4 mb-1"}
##### 3. Google"不活躍帳戶管理器"：自動處理身後事

Google提供"不活躍帳戶管理器（Inactive Account Manager）"，能在使用者長期未登入時自動執行預設操作——這是目前最完善的數字遺產機制之一。

1. 訪問 <strong>myaccount.google.com/inactive</strong>，登入Google帳號。
2. 設定超時期限：3 / 6 / 12 / 18個月未登入後觸發。
3. 新增受信任聯絡人（最多10人），並設定每位可訪問哪些資料（Gmail、相簿、雲端硬碟等）。
4. 可選：設定自動回覆郵件，告知來信者你已無法處理。
5. 最後選擇：到期後是<strong>分享資料給聯絡人</strong>，還是<strong>直接刪除帳戶</strong>。
6. 設定手機號作為兜底驗證，避免誤觸發。

{class="font-semibold mt-4 mb-1"}
##### 4. 國內社交帳號：紀念化與登出流程

國內主流社交平臺對逝者帳號的處理分兩種思路：<strong>"紀念化"（保留帳號讓親友緬懷）</strong>和<strong>"登出"（徹底刪除）</strong>。家屬可憑死亡證明、親屬關係證明、申請人身份證向平臺客服申請。

- <strong>微博</strong>：支援帳號"紀念化"，由親屬提供死亡證明申請，帳號會被鎖定無法登入但內容保留，主頁會顯示"該帳號已設定為紀念帳號"。也可申請登出，需提供繼承公證。
- <strong>抖音</strong>：透過"我 - 設定 - 反饋與幫助 - 帳號與安全 - 帳號登出"或人工客服，提交死亡證明、親屬關係證明、申請人身份證，稽核透過後可登出或轉為紀念狀態。
- <strong>B站</strong>：客服渠道提交逝者證明及親屬證明，可申請帳號登出或保留為紀念頁；UP主的歷史稿件處理需結合版權宣告。
- <strong>小紅書</strong>：透過官方客服申訴，提交死亡證明、親屬關係證明，可申請登出帳號並刪除內容。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>關鍵提醒

{class="list-disc pl-6 mt-2 space-y-1"}
- 各平臺規則會更新，辦理前先查閱官方客服最新指引。
- 所有證明檔案建議先掃描備份再提交，原件妥善保管。
- 跨平臺一次性辦理時，可統一申請一份<strong>繼承公證書</strong>，省去反覆跑手續。
:::

{class="font-semibold mt-4 mb-1"}
##### 5. 數字資產的繼承難題

除了社交帳號，越來越多的人持有<strong>真正有價值的數字資產</strong>，其繼承問題更加複雜：

- <strong>加密貨幣（比特幣、以太坊等）</strong>：基於"私鑰即所有權"原則，<strong>沒有私鑰就等於資產消失</strong>。繼承人無法透過法律檔案向鏈上"申訴"。建議：將助記詞/私鑰分片存放在多個物理安全位置（如銀行保險箱+家裡保險櫃），並在遺囑中註明訪問方式。
- <strong>交易所帳戶</strong>：和銀行帳戶類似，可憑繼承公證書向交易所（如幣安、OKX）申請處置，但跨境交易所流程漫長。
- <strong>域名</strong>：屬於可繼承財產，繼承人在域名註冊商（如阿里雲、GoDaddy）提交繼承公證後可辦理過戶。
- <strong>智慧財產權（原創文章、影片、專利、軟體著作權）</strong>：著作權中的財產權利可繼承（人身權不繼承），收益權可由繼承人享有至作者死後50年。
- <strong>雲端儲存與網盤</strong>：內容資料歸屬個人，可繼承；但部分平臺協議規定帳號本身不可轉讓，需先下載再登出。

::: div .danger-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>加密貨幣"消失"的真實代價

{class="mt-1"}
據Chainalysis報告，全球已有<strong>超過300萬枚比特幣</strong>因私鑰丟失而永遠無法找回，相當於現有總量的六分之一。如果你持有加密資產，請務必讓至少一位你絕對信任的人知道<strong>恢復路徑</strong>——否則這些財富將永遠沉睡在區塊鏈上。
:::

{class="font-semibold mt-4 mb-1"}
##### 6. 一份"數字遺囑"模板

傳統的財產遺囑管不了數字資產。建議你每年更新一份"數字遺囑"附件，與正式遺囑一併存放。以下模板供參考：

::: div .bg-light .dark:bg-gray-700 .rounded-lg .p-4 .mt-2 .mb-3 .text-sm
{class="font-semibold mb-2"}
《個人數字資產處置附件》（模板）

{class="mb-1"}
<strong>第一部分：帳號清單</strong>（僅記錄帳號名與所屬平臺，<strong>不寫密碼</strong>）

{class="list-disc pl-6 mb-2 space-y-0.5"}
- 社交類：微信（帳號xxx）、微博、抖音、B站、小紅書等
- 支付類：支付寶、微信支付、各銀行卡App
- 雲端類：iCloud、華為雲、小米雲、Google帳號、微軟帳號
- 郵箱類：QQ郵箱、網易郵箱、Gmail等
- 其他：網盤、訂閱服務、遊戲帳號等

{class="mb-1"}
<strong>第二部分：密碼託管方案</strong>

{class="list-disc pl-6 mb-2 space-y-0.5"}
- 主密碼存放方式：使用密碼管理器（如Bitwarden、1Password），主密碼寫在紙質件中，封存於家中保險櫃。
- 恢復金鑰/助記詞：分片存放，至少兩處物理位置（如銀行保管箱+家中保險櫃）。
- 授權查詢人：姓名、身份證號、與本人關係、聯絡方式。

{class="mb-1"}
<strong>第三部分：處置意願</strong>

{class="list-disc pl-6 mb-2 space-y-0.5"}
- 各類帳號希望"紀念化"還是"登出"。
- iCloud / Google 資料是否指定"遺產聯絡人"或"不活躍帳戶管理器"。
- 加密資產由誰繼承，私鑰獲取路徑說明。
- 版權類作品收益由誰享有。

{class="mb-1"}
<strong>第四部分：聯絡人與平臺</strong>

{class="list-disc pl-6 space-y-0.5"}
- 信任執行人姓名、聯絡方式、備用聯絡人。
- 常駐平臺客服入口與所需證明材料清單。
- 本附件更新日期：____年__月__日，下次複核日期：____年__月__日。
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>關於"密碼"的法律提示

{class="mt-1"}
將密碼直接寫進遺囑存在洩露風險，且遺囑公示後所有繼承人都能看到。<strong>更穩妥的做法是：遺囑裡只寫"帳號清單 + 處置意願 + 密碼託管位置"，真正的密碼透過密碼管理器主密碼單獨傳給信任執行人</strong>。這樣既符合法律要求，也降低了密碼洩露風險。
:::

#### 三、環保的最後一程

一部手機裡含金、銀、銅、稀土等數十種金屬，隨意丟棄既汙染土壤，也浪費資源。正確的回收渠道有三類，各有側重：

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">渠道</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">回收價</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">資料安全</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">適用場景</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方以舊換新（華為/蘋果/小米等）</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">中等，常疊加補貼券</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最高，官方有規範流程</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">正打算換同品牌新機時最劃算</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第三方回收平臺（愛回收、轉轉、回收寶等）</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">略高，可比價</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">較高，有資料清除報告</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">想直接變現、不繫結品牌</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">公益捐贈（如鄉村學校、愛心機構）</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">無經濟回報</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需自行徹底擦除</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">裝置仍可用、想做善事</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">發揮餘熱（自留改造）</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">省下新裝置錢</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">原機主本人繼續用，無風險</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">裝置效能尚可、家裡有改造需求</td>
                            </tr>
                        </tbody>
                    </table>
```

- <strong>官方回收/以舊換新</strong>：最推薦的方式，流程規範，資料安全有保障。蘋果、華為、小米等品牌官網都有"以舊換新"入口，評估後可抵扣新機款。
- <strong>正規回收平臺</strong>：選擇信譽良好的大型回收平臺，下單後順豐上門取件，檢測後打款。務必選擇<strong>提供"資料清除報告"的</strong>平臺，並保留憑證。
- <strong>公益捐贈</strong>：可聯絡當地鄉村學校、社群公益組織，舊手機可改裝成教學平板或老人機使用。<strong>捐贈前務必執行完整的擦除流程，並卸除所有SIM/SD卡</strong>。
- <strong>發揮餘熱</strong>：改成車載導航儀、智慧家居中控、監控攝像頭、寶寶監視器、電子相框。一臺舊手機可以再戰好幾年。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-leaf mr-2"></i>電子垃圾的真相

{class="mt-1"}
一部手機的電路板裡含有<strong>金、銀、鈀、銅</strong>等貴金屬，每噸廢舊電路板含金量是金礦石的數十倍。但若隨意丟棄，其中的鉛、汞、鎘會滲入土壤與地下水，汙染持續數十年。<strong>正確回收，既保護環境，也能讓稀缺金屬迴圈再生。</strong>
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>實操：為你的舊手機執行一場"標準葬禮"

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 最後一次完整備份：照片上傳雲端、重要檔案複製到電腦、聊天記錄匯出存檔。
2. 退出所有帳號：iCloud / 華為 / 小米 / Google 帳號，關閉"查詢我的手機"。
3. 取出SIM卡與SD卡，斷開所有OTG外設。
4. 執行加密恢復出廠設定，必要時手動勾選"格式化儲存"。
5. （僅老裝置）用垃圾檔案填滿儲存，再恢復出廠設定一次。
6. 選擇它的下一站：官方以舊換新、正規回收平臺、公益捐贈，或轉贈家人。
7. 同步更新你的"數字遺產清單"，把已淘汰的裝置從清單中劃掉。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-calendar-check mr-2"></i>本月任務清單

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 為你目前的主力手機指定Apple"遺產聯絡人"或設定Google"不活躍帳戶管理器"。
2. 用本節模板起草一份《個人數字資產處置附件》，與家人溝通存放位置。
3. 檢查家中是否有2臺以上閒置舊手機，預約一次官方或正規平臺回收。
:::
