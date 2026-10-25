---
id: di-shi-si-zhang
num: 14
part: ruan-jian-pian
nav: 第十四章：密碼管理器專題
toc: default
kind: chapter
---

### 第十四章：密碼管理器專題

{class="chapter-intro mb-4"}
於數字之世，密碼乃君家門之鑰匙。然鑰匙太多、太繁，奈何？密碼管理器乃君之"萬能鑰匙管家"。

#### 一、何以君需密碼管理器？

今人平均有幾十甚至上百個網絡賬號。若每賬號皆用同密碼，一旦一網站被黑，所有賬號皆危。若每賬號皆用不同之繁密碼，根本記不住。

密碼管理器解此困：君只需記一主密碼，其助君記所有其他密碼。

#### 二、密碼管理器之工作原理

1. <strong>加密存儲</strong>：所有密碼皆經高強度加密存儲，惟君能解密。
2. <strong>主密碼</strong>：君設一主密碼，以解鎖密碼庫。主密碼本身不存於服務器上。
3. <strong>自動填充</strong>：於網站或App登錄界面，密碼管理器自動填充賬號密碼。
4. <strong>密碼生成</strong>：可生隨機、繁復之密碼，提安全性。

#### 三、加密理簡介

瞭解密碼管理器之加密原理，能幫汝判斷一個服務商是否值得信任。下面用通俗之語言解釋幾個核心概念。

##### 1. AES-256 加密

AES（高級加密標準）乃美國國家標準與技術研究院（NIST）認可之對稱加密算法，爲銀行、軍方、政府廣泛使用。"256"指密鑰長度爲 256 位——理論上須超過宇宙年齡之時間才能暴力破解。主流密碼管理器（1Password、Bitwarden、KeePass 等）皆用 AES-256 加密汝之密碼庫。

##### 2. 零知架構（Zero-Knowledge Architecture）

"零知識"非說服務商何皆不存，而乃曰<strong>加密和解密皆於汝之設備本地完成，服務器唯保存已加密之密文</strong>。具體程：

1. 汝於客戶端輸入主密碼。
2. 客戶端用主密碼派生出加密密鑰（這一步於汝手機/電腦上完成）。
3. 只有加密後之密文方上傳至服務器。
4. 下次登錄時，服務器以密文下發，客戶端再次用主密碼解密。

鍵點：<strong>主密碼本身自不離開汝之設備</strong>，服務器上亦沒有。故縱服務商爲黑，黑客拿至之亦只是一堆無法解密之密文——除非彼等能猜出汝之主密碼。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>何故"零知識"意味着服務商亦觀不至汝之密碼？

{class="mt-1"}
蓋因解密密鑰由汝之主密碼派生，而主密碼唯存在於汝腦中、唯於汝本地設備上使用。服務商之服務器上既沒有主密碼，亦沒有解密密鑰，只有密文。這就是何故 Bitwarden、1Password 等正規服務商皆明確聲明"我們亦無法看到汝之密碼"——非彼等不欲觀，乃技術上作不至。
:::

##### 3. 密鑰派生函數：PBKDF2 與 Argon2

主密碼不可直接用作加密密鑰——它須經過"密鑰派生函數"處理。此函數之作用乃<strong>故意使計算變慢</strong>，使黑客暴力破解之成本高至不可行。

- <strong>PBKDF2</strong>：老牌標準，爲 iCloud 鑰匙串、Bitwarden、LastPass 等廣泛使用。通過反覆迭代（通常 10 萬次以上）哈希來拖慢破解。
- <strong>Argon2</strong>：2015 年密碼哈希競賽冠軍，比 PBKDF2 更現代。除矣"算力消耗"尚引入矣"內存消耗"——使 GPU/ASIC 等專用硬件亦難以加速破解。Bitwarden、KeePassXC 等已支持。

迭代次數越高越安全，但解鎖速度亦將變慢。正規服務商都將公開其使用之派生算法與迭代次數，便於安全社區審計。

##### 4. 案例之鑑：LastPass 2022 年數據之洩

2022 年 8 月，老牌密碼管理器 LastPass 公告其開發環境爲入侵；同年 11 月進一步披露，黑客拿走矣用戶之密碼庫備份（加密後之密文）。事件之關鍵教訓：

- <strong>零知識架構守住矣底線</strong>：由於密碼庫本身乃加密之，黑客拿至密文但解不開——前提乃用戶之主密碼足夠強。
- <strong>弱主密用戶最危</strong>：黑客可離線暴力破解弱主密碼，因此使用弱主密碼或重複主密碼之用戶面臨實質風險。
- <strong>元數據亦泄露</strong>：雖密碼內容加密，但站點 URL、備註等元數據或未加密，將暴露用戶使用矣何服務。

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>自 LastPass 事件學至之

{class="mt-1"}
第一，主密碼須長且獨特（建議 16 位以上，包含大小寫、數字、符號）；第二，優先選擇支持 Argon2id、迭代次數高之服務商；第三，對高價值賬號（銀行、郵箱）務必開啓獨立之二次驗證，勿唯依賴密碼管理器。
:::

#### 四、主流密管器薦

##### 系統自帶：

- <strong>iCloud鑰匙串</strong>：蘋果生態用戶首選。與Safari、App無縫集成，免費，安全。弊乃跨平臺使用不便。
- <strong>Google密碼管理器</strong>：安卓用戶方便。與Chrome、安卓系統集成，免費。
- <strong>華爲密碼保險箱</strong>：鴻蒙系統內置，宜華爲用戶。

##### 第三方專業工具：

- <strong>Bitwarden</strong>：開源免費，功能強大，支持所有平臺。強烈薦予注重隱私之用戶。
- <strong>1Password</strong>：界面美觀，功能豐富，宜家庭與團隊。付費。
- <strong>LastPass</strong>：老牌密碼管家，免費之版其能有限。
- <strong>KeePass</strong>：完全本地存儲，開源免費。宜極客用戶。

#### 五、密強度真實評估

密碼管理器普遍將顯示"密碼強度"指示條（紅/黃/綠），但此評估往往只觀長度與字符種類，並不全面。真正判斷密碼是否安全，須考慮"熵"與"是否已泄露"。

##### 1. 熵（Entropy）：密碼強度之科學度量

"熵"衡量密碼之不確定性，單位乃比特。熵越高，暴力破解所需嘗試次數越多。

- <strong>"123456"</strong>：熵極低，瞬間破解。
- <strong>"P@ssw0rd"</strong>：看似複雜，但出今凡字典攻擊列表裏，熵依然低。
- <strong>"correct horse battery staple"</strong>：四個隨機單詞，熵約 44 較特，破解難度遠超"P@ssw0rd"。
- <strong>16 位隨機字符（含大小寫+數+符號）</strong>：熵約 100 較特，目前算力無法暴力破解。

結論：<strong>"長度 + 隨機性"較"複雜符號"更要</strong>。這亦乃密碼管理器生成之隨機長密碼真正安全之原因。

##### 2. HaveIBeenPwned：查汝之密碼是否已泄露

安全研究員 Troy Hunt 維護之 <a href="https://haveibeenpwned.com" class="text-primary hover:underline" target="_blank" rel="noopener">haveibeenpwned.com</a> 收錄矣歷次大型數據泄露中流出之賬號與密碼。汝可：

1. 輸入郵箱，查汝之賬號是否於某次泄露中爲曝光。
2. 用 Pwned Passwords 功能查詢某個密碼是否於已知泄露庫中（密碼管理器與瀏覽器皆已內置此查詢）。

若一個密碼出現在泄露庫中，<strong>無論它看起來多複雜皆須立即更換</strong>——蓋因字典攻擊將優先嚐試此已知密碼。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-shield-alt mr-2"></i>k-Anonymity 查詢理

{class="mt-1"}
擔心於 HaveIBeenPwned 輸入密碼將再次泄露？不必擔心。現代查詢採用"k-匿名"協議：瀏覽器唯以密碼哈希之前 5 位發給服務器，服務器返回所有以這 5 位開頭之哈希列表，本地再比對。亦就是曰，服務器永遠觀不至汝之完整密碼哈希。1Password、Bitwarden 之"已泄露密碼檢測"皆乃這樣工作之。
:::

##### 3. 密碼管理器內置之監控功能

- <strong>1Password Watchtower</strong>：實時監控弱密碼、重複密碼、已泄露密碼、過期密碼、不使用 2FA 之網站，並以紅/橙/黃分級展示。
- <strong>Bitwarden Vault Health</strong>：免費版即可觀弱密、重複密；付費版可檢測已泄露密（基於 HaveIBeenPwned）。
- <strong>iCloud 鑰匙串"安全宜"</strong>：iOS 設置 → 密碼 → 安全建議，將提示汝何密碼出現在已知泄露中、何重複使用。
- <strong>Google 密管器"密檢工具"</strong>：Chrome 內置，可一鍵檢已泄露、弱、重複密。

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>現在遂查：汝之密碼是否安全

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 打開 haveibeenpwned.com，輸入汝之常用郵箱，觀看出現在何泄露事件中。
2. iPhone 用戶：設 → 密 → 安全宜，逐條處紅色警。
3. Chrome 用戶：設 → 密 → 檢密，依示改。
4. 1Password/Bitwarden 用戶：打開 Watchtower/Health Reports，優先處理"已泄露"與"重複"項。
:::

#### 六、Passkey：無密登錄之未來

2024-2026 年，密碼技術方經歷一場革命——<strong>Passkey（通行密鑰）</strong>有望徹底淘汰傳統密碼。Apple、Google、Microsoft 三大平臺聯合推動，FIDO 聯盟與萬維網聯盟（W3C）背書，這乃數十年來登錄方式最大之一次變革。

##### 1. 何乃 Passkey？

Passkey 基於 FIDO2 / WebAuthn 標準，用<strong>設備上之密鑰對</strong>替代密碼。原理可簡化爲：

- 汝之手機生成一對密鑰：<strong>公鑰</strong>（註冊賜網站）+ <strong>私鑰</strong>（永遠存在汝設備之安全芯片中）。
- 登錄時，網站發一個"挑戰"，汝之手機用私鑰簽名，再由網站用公鑰驗證。
- 簽名前須汝通過生物識別（Face ID / 指紋）或設備 PIN 確認身份。
- 整個程中，<strong>沒有任何密碼於網絡中傳輸</strong>。

##### 2. Passkey vs 傳統密

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">維度</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">傳統密</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Passkey</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">抗釣魚</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">差，釣魚網站可竊取密</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">天然抗釣魚，私鑰唯對真實域名簽名</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">服器泄露響</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">密碼哈希或爲破解</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">服務器唯存公鑰，泄露無影響</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">便性</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需記憶/輸入/管</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Face ID/指紋一秒登錄</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">重放攻擊</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">或爲中間人截獲重放</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每次簽名一性，無法重放</td>
                            </tr>
                        </tbody>
                    </table>
```

##### 3. 各平臺支情況

- <strong>Apple iCloud 鑰匙串 Passkey</strong>：iOS 16+ / macOS Ventura+ 原生支持，Passkey 可於所有登錄同一 Apple ID 之設備間同步，新設備登錄網站時無需重新創建。
- <strong>Google 密管器 Passkey</strong>：安卓 + Chrome 原生支，Passkey 存 Google 賬戶中，跨安卓設同步；2023 年起 Google 個人賬號已支用 Passkey 登錄。
- <strong>Microsoft</strong>：Windows 11 / Edge 已支持 Passkey；微軟賬號、Outlook、Office 等服務陸續開放 Passkey 登錄，並可於 Microsoft Authenticator 中管理。
- <strong>1Password / Bitwarden</strong>：已支持 Passkey 之創建、存儲、跨平臺同步，使汝不受限於單一生態。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>跨設備同步乃關鍵突破

{class="mt-1"}
早期 Passkey 之最大痛點乃"綁定單臺設備"——換手機遂要重新創建。2023 年起 Apple、Google、Microsoft 實現矣 Passkey 之雲端同步：iCloud 鑰匙串同步跨 Apple 設備，Google 密碼管理器同步跨安卓設備。1Password 等第三方則打通矣跨生態同步。這意味着 Passkey 已具備替代密碼之實用性。
:::

##### 4. 何以於手機上創建與使用 Passkey

<strong>iOS（iPhone）徑：</strong>

1. 於支持 Passkey 之網站（如 Google、微軟、亞馬遜、eBay、PayPal）賬號安全頁選擇"添加通行密鑰 / Add passkey"。
2. 系統彈出 Face ID / Touch ID 驗證窗口，通過後 Passkey 自動生成並保存至 iCloud 鑰匙串。
3. 下次登錄該網站時，輸入用戶名後擇"用 iPhone 登錄"，Face ID 一刷即可。
4. 管入：設 → 密 → 找至對應網站，可見 Passkey 條目。

<strong>安卓徑：</strong>

1. 於支持 Passkey 之網站賬號安全頁選擇"添加通行密鑰"。
2. Google 密碼管理器彈窗 → 選擇汝之 Google 賬號 → 屏幕鎖驗證（指紋/圖案/PIN）。
3. Passkey 自動保存至 Google 密碼管理器，跨同賬號安卓設備同步。
4. 下次登錄時，擇"用 Passkey"，屏幕鎖一解即可。
5. 管理入口：安卓設置 → 密碼、密鑰與自動填充 → 密碼管理器 → google.com。

##### 5. Passkey 跨設登錄

若汝於 Windows 電腦上登錄一個只有 iPhone 上有 Passkey 之網站，可掃碼授權：

1. 網站登錄頁擇"用 Passkey"。
2. 擇"用其他設"。
3. 電腦顯二維碼，用 iPhone 掃碼。
4. iPhone 彈出 Face ID 驗證，確認後網站於電腦上完成登錄。

這一過程通過藍牙+互聯網雙重加密通信，Passkey 私鑰未能離開汝之 iPhone。

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>現在遂試：體驗無密碼登錄

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 登錄 Google 賬號 → 安全 → 通行密鑰 → 添通行密鑰，體驗 Face ID/指紋登錄。
2. 登錄微軟賬號 → 安全 → 高級安全項 → 添通行密鑰。
3. 於淘寶、京東、eBay、PayPal 等已支持 Passkey 之服務上嚐鮮。
4. 保留傳統密碼作爲後備，逐步遷移高價值賬號至 Passkey。
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>過渡期宜

{class="mt-1"}
Passkey 並未悉取代密——許多網站仍處於"Passkey + 密"並存階段。宜：高價值賬號優先開啓 Passkey，但<strong>勿立即刪除傳統密碼</strong>，留作備用；同時繼續使用密碼管理器，蓋因非所有網站皆支持 Passkey。以 Passkey 觀作"密碼管理器之強力補充"而非"立刻替換"。
:::

#### 七、硬件安全密鑰

若汝對安全之要求高於普通用戶——比如持有大量加密貨幣、乃高管/記者/活動人士、或保護企業核心賬號——硬件安全密鑰乃比短信驗證碼更可靠之選擇。

##### 1. 何乃硬件安全密鑰？

硬件密鑰乃一個物理設備（形似 U 盤），內部安全芯片存儲汝之私鑰，須物理接觸或 NFC 才能完成驗證。代表產品：

- <strong>YubiKey</strong>（Yubico 公司）：最主流，支 FIDO2/WebAuthn、U2F、OTP、PIV、OpenPGP，USB-C / USB-A / NFC 等多種接口。5 系列 50-70 美元。
- <strong>Google Titan</strong>：Google 自家出品，USB-C + NFC / 藍牙，約 30-40 美元。
- <strong>OnlyKey</strong>：開源替代品，支多種協議。
- <strong>國產替代</strong>：如飛天誠信 ePasskey，價更親民。

##### 2. 何故硬件密鑰比短信驗證碼安全？

- <strong>抗釣魚</strong>：與 Passkey 一樣，硬件密鑰唯對真實域名響應，釣魚網站無法騙取驗證碼。
- <strong>抗 SIM 劫持</strong>：短信驗證碼可爲 SIM-swap 攻擊截獲，硬件密鑰無需手機號。
- <strong>抗中間人</strong>：FIDO2 協議每次簽名皆包含挑戰值，無法重放。
- <strong>物理隔離</strong>：私鑰永遠於硬件芯片內，惡意軟件縱攻陷汝之電腦亦讀不至。

##### 3. 適場景

- 加密貨幣交易所賬號、財包復。
- 企業 SSO、遠程辦公 VPN、SSH 登錄服器。
- 郵箱、GitHub、社交媒體等"主賬號"——一旦爲攻破可重置所有其他賬號。
- 記者、律師、高管等高敏感人羣。

##### 4. 何以配置硬件密鑰作爲二次驗證

以 Google 賬號 + YubiKey 爲例：

1. 購買 YubiKey（建議一次買兩以，一以日常用、一以備用，存放於不同地點）。
2. 登錄 myaccount.google.com → 安全 → 兩步驗。
3. 選擇"添加安全密鑰"→ 以 YubiKey 插入 USB-C 口或貼近手機 NFC 感應區。
4. 依示觸摸 YubiKey 金屬觸點畢註冊。
5. 建議注冊第二以備用密鑰。
6. 於"兩步驗證"設置裏，以硬件密鑰設爲首選驗證方式，短信驗證碼作爲備用。

主流支持之網站：Google、GitHub、Microsoft、Apple ID、Facebook、Twitter、Dropbox、GitLab、AWS、Coinbase、Binance 等。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>雙密鑰策

{class="mt-1"}
硬件密鑰最大之風險乃"丟失"。建議：① 同時註冊兩以不同之密鑰；② 一以隨身攜帶（鑰匙扣），一以存放於家中保險櫃或銀行保管箱；③ 部分網站允許以"備用恢復碼"打印出來離線保存。這樣縱主密鑰丟失，亦未能爲永久鎖於賬號外。
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>購機渠要慎

{class="mt-1"}
務必自官方店鋪或授權代理購買，勿買二手或來源不明之密鑰——理論上預置過之硬件或已爲植入後門。YubiKey 之固件於出廠後無法更新，但 Yubico 將持續推送安全公告，關注其官網即可。
:::

#### 八、家/團隊密共享

家庭場景下，Netflix、家庭 Wi-Fi、路由器後臺、智能門鎖密碼須全家共用；團隊場景下，服務器、數據庫、社交媒體賬號須多人協作。<strong>用微信發密碼、寫於共享文檔裏皆乃高危作法</strong>——一旦聊天記錄或文檔權限泄露，密碼遂泄露矣。

##### 1. 1Password 之"共享保險庫"（Vault）

1Password 乃家庭與團隊共享之標杆產品。它的核心機制乃<strong>多保險庫</strong>：

- <strong>個人保險庫</strong>：只有汝能觀，如銀行、郵箱等私人賬號。
- <strong>共享保險庫</strong>：家人或團隊成員皆能觀，如 Netflix、家庭 Wi-Fi、共享信用卡。
- <strong>權限分級</strong>：團隊版可設定某些成員"唯查看"或"唯查看但不編輯"。

家人或團隊成員無需共享主密碼，各自用自己之賬號登錄，但可看到爲授權之共享保險庫內容。密碼修改後所有成員實時同步。

##### 2. Bitwarden 之"組織"功能

Bitwarden 之免費版支持個人密碼共享（通過"發送 Send"功能限時分享單條密碼）；付費版可創建"組織"，以若干條目共享賜家庭成員或團隊同事，權限可細分。Bitwarden 尚提供自託管選項，適合對數據主權要求高之企業。

##### 3. 家庭場景：共享 Netflix、Wi-Fi 等密碼之安全方式

- <strong>Netflix / 視頻網站</strong>：用 1Password 家庭版之"共享保險庫"存登錄密碼，家庭成員各自登錄即可，無需於羣裏發。
- <strong>家 Wi-Fi 密</strong>：iOS 設備間可通過 AirDrop 直接共享 Wi-Fi 密碼賜來訪之客人，無需念出來；安卓 12+ 也有"附近分享 Wi-Fi"功能。
- <strong>智能門鎖、智能家電</strong>：儘量用廠商 App 之"家庭成員"功能爲每人單獨創建賬號，而非共享一個管理員賬號。
- <strong>家用路由器後台</strong>：管理員密碼存至 1Password 共享保險庫，訪客 Wi-Fi 單獨開一個 SSID。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>1Password 家庭版之性價比

{class="mt-1"}
1Password Families 約 4.99 美元/月，支持最多 5 位家庭成員，每人皆有獨立之私人保險庫 + 4 個共享保險庫。算下來人均不至 1 美元/月，乃目前家庭共享體驗最好之方案。Bitwarden 之家庭版 10 美元/年支持 6 人，性價比更高，但界面體驗略遜。
:::

##### 4. 團隊場景：服器/數據庫密共享

- <strong>1Password Teams / Business</strong>：可按部門、項目組創建多保險庫，細粒度權限控制，凡訪問行爲可審計。
- <strong>Bitwarden Teams / Enterprise</strong>：開源策，可自託，企業版支 SSO 集成、目錄同步。
- <strong>職責分離則</strong>：管員密不應祇由一人掌握——設 2-3 名"應急聯繫人"，保鍵人員離職/休假時業務不中斷。
- <strong>離職程</strong>：員工離職時立即撤銷其密碼管理器訪問權限，必要時旋轉所有他接觸過之高敏感密碼。

##### 5. 緊急訪問（Emergency Access）：萬一汝出事

想象一個場景：汝獨自管理家庭所有重要賬號，但意外住院或不幸離世，家人無法登錄銀行、郵箱、保險賬號。<strong>"緊急訪問"能</strong>正是爲此設計——授權一位信任之家人/朋友，於汝無法響應時獲取汝之密碼庫。

<strong>Bitwarden 緊急訪問設：</strong>

1. 登錄 Bitwarden Web Vault → 設 → 緊急訪問。
2. 添加信任聯繫人之郵箱，邀請對方接受。
3. 設定"雲端雙因素認證"（建議 7-14 天）：自對方發起請求至汝確認之時間窗口。
4. 若汝於等待期內不響應（拒絕或不操作），到期後對方自動獲得訪問權。
5. 汝隨時可手動拒絕請求或撤銷緊急訪問權限。

<strong>1Password 緊急訪問：</strong>

1. 1Password 不直接叫"緊急訪問"，但通過"家庭/團隊組織"功能可實現——以家人加入家庭版後，將部分條目放入"共享保險庫"。
2. 對個人版用戶，建議以主密碼告知一位高度信任之家人，或寫入密封信封存放於保險櫃。
3. 1Password 尚提供"恢復碼"，開啓雙重認證時務必打印保存。

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>現在遂設：爲家人留一以"備用鑰匙"

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 選定一位信任之家人作爲"緊急聯繫人"。
2. 于密碼管理器中設置緊急訪問（Bitwarden）或加入家庭共享保險庫（1Password）。
3. 以主密碼 + 恢復碼寫於紙上，封進信封，存放於家中保險櫃或告知可信家人。
4. 每半年回顧一，確認緊急聯繫人是否仍然適用。
:::

#### 九、密管器用最佳實踐

- <strong>設強主密碼</strong>：主密碼乃最後防線，務必設一長且繁之密碼，並牢記。
- <strong>啓雙重認證</strong>：爲密碼管理器賬號啓雙重認證，增一層保護。
- <strong>定期查弱密碼</strong>：大多數密碼管理器有"安全審計"之能，助君覓出弱密碼與重複密碼。
- <strong>勿忘主密碼</strong>：主密碼無法找回，忘即意味着失所有密碼。議寫於紙上，置於安全之處。
- <strong>緊急訪問</strong>：設緊急聯繫人，萬一君無法訪問，信任之人可取君之密碼。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>重要提醒

{class="mt-1"}
重要提醒
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>今即試之：始用密碼管理器

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 擇一密碼管理器（薦Bitwarden或系統自帶）。
2. 注冊賬號，設一強主密碼。
3. 注冊賬號，設一強主密碼。
4. 導入現有密碼（若有）或始添新密碼。
5. 查安全審計報告，覓需改之密碼。
:::
