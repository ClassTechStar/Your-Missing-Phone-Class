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
在數字時代，密碼就是你的家門鑰匙。但鑰匙太多、太複雜，怎麼辦？密碼管理器就是你的"萬能鑰匙管家"。

#### 一、為什麼你需要密碼管理器？

現代人平均有幾十甚至上百個網路賬號。如果每個賬號都用相同的密碼，一旦一個網站被黑，所有賬號都危險。如果每個賬號都用不同的複雜密碼，根本記不住。

密碼管理器解決了這個困境：你只需要記住一個主密碼，它幫你記住所有其他密碼。

#### 二、密碼管理器的工作原理

1. <strong>加密儲存</strong>：所有密碼都經過高強度加密儲存，只有你能解密。
2. <strong>主密碼</strong>：你設定一個主密碼，用於解鎖密碼庫。主密碼本身不儲存在伺服器上。
3. <strong>自動填充</strong>：在網站或App登入介面，密碼管理器自動填充賬號密碼。
4. <strong>密碼生成</strong>：可以生成隨機、複雜的密碼，提高安全性。

#### 三、加密原理簡介

瞭解密碼管理器的加密原理，能幫你判斷一個服務商是否值得信任。下面用通俗的語言解釋幾個核心概念。

##### 1. AES-256 加密

AES（高階加密標準）是美國國家標準與技術研究院（NIST）認可的對稱加密演算法，被銀行、軍方、政府廣泛使用。"256"指金鑰長度為 256 位——理論上需要超過宇宙年齡的時間才能暴力破解。主流密碼管理器（1Password、Bitwarden、KeePass 等）都用 AES-256 加密你的密碼庫。

##### 2. 零知識架構（Zero-Knowledge Architecture）

"零知識"不是說服務商什麼都不存，而是說<strong>加密和解密都在你的裝置本地完成，伺服器只儲存已加密的密文</strong>。具體流程：

1. 你在客戶端輸入主密碼。
2. 客戶端用主密碼派生出加密金鑰（這一步在你手機/電腦上完成）。
3. 只有加密後的密文才上傳到伺服器。
4. 下次登入時，伺服器把密文下發，客戶端再次用主密碼解密。

關鍵點：<strong>主密碼本身從不離開你的裝置</strong>，伺服器上也沒有。所以即使服務商被黑，駭客拿到的也只是一堆無法解密的密文——除非他們能猜出你的主密碼。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>為什麼"零知識"意味著服務商也看不到你的密碼？

{class="mt-1"}
因為解密金鑰由你的主密碼派生，而主密碼只存在於你腦中、只在你本地裝置上使用。服務商的伺服器上既沒有主密碼，也沒有解密金鑰，只有密文。這就是為什麼 Bitwarden、1Password 等正規服務商都明確宣告"我們也無法看到你的密碼"——不是他們不想看，是技術上做不到。
:::

##### 3. 金鑰派生函式：PBKDF2 與 Argon2

主密碼不能直接用作加密金鑰——它需要經過"金鑰派生函式"處理。這個函式的作用是<strong>故意讓計算變慢</strong>，讓駭客暴力破解的成本高到不可行。

- <strong>PBKDF2</strong>：老牌標準，被 iCloud 鑰匙串、Bitwarden、LastPass 等廣泛使用。透過反覆迭代（通常 10 萬次以上）雜湊來拖慢破解。
- <strong>Argon2</strong>：2015 年密碼雜湊競賽冠軍，比 PBKDF2 更現代。除了"算力消耗"還引入了"記憶體消耗"——讓 GPU/ASIC 等專用硬體也難以加速破解。Bitwarden、KeePassXC 等已支援。

迭代次數越高越安全，但解鎖速度也會變慢。正規服務商都會公開其使用的派生演算法和迭代次數，便於安全社群審計。

##### 4. 案例警示：LastPass 2022 年資料洩露

2022 年 8 月，老牌密碼管理器 LastPass 公告其開發環境被入侵；同年 11 月進一步披露，駭客拿走了使用者的密碼庫備份（加密後的密文）。事件的關鍵教訓：

- <strong>零知識架構守住了底線</strong>：由於密碼庫本身是加密的，駭客拿到密文但解不開——前提是使用者的主密碼足夠強。
- <strong>弱主密碼使用者最危險</strong>：駭客可以離線暴力破解弱主密碼，因此使用弱主密碼或重複主密碼的使用者面臨實質風險。
- <strong>後設資料也洩露</strong>：雖然密碼內容加密，但站點 URL、備註等後設資料可能未加密，會暴露使用者使用了哪些服務。

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>從 LastPass 事件學到的

{class="mt-1"}
第一，主密碼必須長且獨特（建議 16 位以上，包含大小寫、數字、符號）；第二，優先選擇支援 Argon2id、迭代次數高的服務商；第三，對高價值賬號（銀行、郵箱）務必開啟獨立的二次驗證，不要只依賴密碼管理器。
:::

#### 四、主流密碼管理器推薦

##### 系統自帶：

- <strong>iCloud鑰匙串</strong>：蘋果生態使用者首選。與Safari、App無縫整合，免費，安全。缺點是跨平臺使用不便。
- <strong>Google密碼管理器</strong>：安卓使用者方便。與Chrome、安卓系統整合，免費。
- <strong>華為密碼保險箱</strong>：鴻蒙系統內建，適合華為使用者。

##### 第三方專業工具：

- <strong>Bitwarden</strong>：開源免費，功能強大，支援所有平臺。強烈推薦給注重隱私的使用者。
- <strong>1Password</strong>：介面美觀，功能豐富，適合家庭和團隊。付費。
- <strong>LastPass</strong>：老牌密碼管理器，免費版功能受限。
- <strong>KeePass</strong>：完全本地儲存，開源免費。適合極客使用者。

#### 五、密碼強度真實評估

密碼管理器普遍會顯示"密碼強度"指示條（紅/黃/綠），但這個評估往往只看長度和字元種類，並不全面。真正判斷密碼是否安全，需要考慮"熵"和"是否已洩露"。

##### 1. 熵（Entropy）：密碼強度的科學度量

"熵"衡量密碼的不確定性，單位是位元。熵越高，暴力破解所需嘗試次數越多。

- <strong>"123456"</strong>：熵極低，瞬間破解。
- <strong>"P@ssw0rd"</strong>：看似複雜，但出現在所有字典攻擊列表裡，熵依然低。
- <strong>"correct horse battery staple"</strong>：四個隨機單詞，熵約 44 位元，破解難度遠超"P@ssw0rd"。
- <strong>16 位隨機字元（含大小寫+數字+符號）</strong>：熵約 100 位元，目前算力無法暴力破解。

結論：<strong>"長度 + 隨機性"比"複雜符號"更重要</strong>。這也是密碼管理器生成的隨機長密碼真正安全的原因。

##### 2. HaveIBeenPwned：查你的密碼是否已洩露

安全研究員 Troy Hunt 維護的 <a href="https://haveibeenpwned.com" class="text-primary hover:underline" target="_blank" rel="noopener">haveibeenpwned.com</a> 收錄了歷次大型資料洩露中流出的賬號和密碼。你可以：

1. 輸入郵箱，查你的賬號是否在某次洩露中被曝光。
2. 用 Pwned Passwords 功能查詢某個密碼是否在已知洩露庫中（密碼管理器和瀏覽器都已內建此查詢）。

如果一個密碼出現在洩露庫中，<strong>無論它看起來多複雜都必須立即更換</strong>——因為字典攻擊會優先嚐試這些已知密碼。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-shield-alt mr-2"></i>k-Anonymity 查詢原理

{class="mt-1"}
擔心在 HaveIBeenPwned 輸入密碼會再次洩露？不必擔心。現代查詢採用"k-匿名"協議：瀏覽器只把密碼雜湊的前 5 位發給伺服器，伺服器返回所有以這 5 位開頭的雜湊列表，本地再比對。也就是說，伺服器永遠看不到你的完整密碼雜湊。1Password、Bitwarden 的"已洩露密碼檢測"都是這樣工作的。
:::

##### 3. 密碼管理器內建的監控功能

- <strong>1Password Watchtower</strong>：實時監控弱密碼、重複密碼、已洩露密碼、過期密碼、不使用 2FA 的網站，並以紅/橙/黃分級展示。
- <strong>Bitwarden Vault Health</strong>：免費版即可檢視弱密碼、重複密碼；付費版可檢測已洩露密碼（基於 HaveIBeenPwned）。
- <strong>iCloud 鑰匙串"安全建議"</strong>：iOS 設定 → 密碼 → 安全建議，會提示你哪些密碼出現在已知洩露中、哪些重複使用。
- <strong>Google 密碼管理器"密碼檢查工具"</strong>：Chrome 內建，可一鍵檢查已洩露、弱、重複密碼。

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>現在就查：你的密碼是否安全

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 開啟 haveibeenpwned.com，輸入你的常用郵箱，看看出現在哪些洩露事件中。
2. iPhone 使用者：設定 → 密碼 → 安全建議，逐條處理紅色警告。
3. Chrome 使用者：設定 → 密碼 → 檢查密碼，按提示修改。
4. 1Password/Bitwarden 使用者：開啟 Watchtower/Health Reports，優先處理"已洩露"和"重複"項。
:::

#### 六、Passkey：無密碼登入的未來

2024-2026 年，密碼技術正在經歷一場革命——<strong>Passkey（通行金鑰）</strong>有望徹底淘汰傳統密碼。Apple、Google、Microsoft 三大平臺聯合推動，FIDO 聯盟和全球資訊網聯盟（W3C）背書，這是數十年來登入方式最大的一次變革。

##### 1. 什麼是 Passkey？

Passkey 基於 FIDO2 / WebAuthn 標準，用<strong>裝置上的金鑰對</strong>替代密碼。原理可以簡化為：

- 你的手機生成一對金鑰：<strong>公鑰</strong>（註冊給網站）+ <strong>私鑰</strong>（永遠存在你裝置的安全晶片中）。
- 登入時，網站發一個"挑戰"，你的手機用私鑰簽名，再由網站用公鑰驗證。
- 簽名前需要你透過生物識別（Face ID / 指紋）或裝置 PIN 確認身份。
- 整個過程中，<strong>沒有任何密碼在網路中傳輸</strong>。

##### 2. Passkey vs 傳統密碼

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">維度</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">傳統密碼</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Passkey</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">抗釣魚</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">差，釣魚網站可竊取密碼</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">天然抗釣魚，私鑰只對真實域名簽名</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">伺服器洩露影響</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">密碼雜湊可能被破解</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">伺服器只存公鑰，洩露無影響</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">便捷性</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需記憶/輸入/管理</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Face ID/指紋一秒登入</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">重放攻擊</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可能被中間人截獲重放</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每次簽名一次性，無法重放</td>
                            </tr>
                        </tbody>
                    </table>
```

##### 3. 各平臺支援情況

- <strong>Apple iCloud 鑰匙串 Passkey</strong>：iOS 16+ / macOS Ventura+ 原生支援，Passkey 可在所有登入同一 Apple ID 的裝置間同步，新裝置登入網站時無需重新建立。
- <strong>Google 密碼管理器 Passkey</strong>：安卓 + Chrome 原生支援，Passkey 存在 Google 賬戶中，跨安卓裝置同步；2023 年起 Google 個人賬號已支援用 Passkey 登入。
- <strong>Microsoft</strong>：Windows 11 / Edge 已支援 Passkey；微軟賬號、Outlook、Office 等服務陸續開放 Passkey 登入，並可在 Microsoft Authenticator 中管理。
- <strong>1Password / Bitwarden</strong>：已支援 Passkey 的建立、儲存、跨平臺同步，讓你不受限於單一生態。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>跨裝置同步是關鍵突破

{class="mt-1"}
早期 Passkey 的最大痛點是"繫結單臺裝置"——換手機就要重新建立。2023 年起 Apple、Google、Microsoft 實現了 Passkey 的雲端同步：iCloud 鑰匙串同步跨 Apple 裝置，Google 密碼管理器同步跨安卓裝置。1Password 等第三方則打通了跨生態同步。這意味著 Passkey 已具備替代密碼的實用性。
:::

##### 4. 如何在手機上建立和使用 Passkey

<strong>iOS（iPhone）路徑：</strong>

1. 在支援 Passkey 的網站（如 Google、微軟、亞馬遜、eBay、PayPal）賬號安全頁選擇"新增通行金鑰 / Add passkey"。
2. 系統彈出 Face ID / Touch ID 驗證視窗，透過後 Passkey 自動生成並儲存到 iCloud 鑰匙串。
3. 下次登入該網站時，輸入使用者名稱後選擇"使用 iPhone 登入"，Face ID 一刷即可。
4. 管理入口：設定 → 密碼 → 找到對應網站，可見 Passkey 條目。

<strong>安卓路徑：</strong>

1. 在支援 Passkey 的網站賬號安全頁選擇"新增通行金鑰"。
2. Google 密碼管理器彈窗 → 選擇你的 Google 賬號 → 螢幕鎖驗證（指紋/圖案/PIN）。
3. Passkey 自動儲存到 Google 密碼管理器，跨同賬號安卓裝置同步。
4. 下次登入時，選擇"使用 Passkey"，螢幕鎖一解即可。
5. 管理入口：安卓設定 → 密碼、金鑰和自動填充 → 密碼管理器 → google.com。

##### 5. Passkey 跨裝置登入

如果你在 Windows 電腦上登入一個只有 iPhone 上有 Passkey 的網站，可以掃碼授權：

1. 網站登入頁選擇"使用 Passkey"。
2. 選擇"使用其他裝置"。
3. 電腦顯示二維碼，用 iPhone 掃碼。
4. iPhone 彈出 Face ID 驗證，確認後網站在電腦上完成登入。

這一過程透過藍芽+網際網路雙重加密通訊，Passkey 私鑰不會離開你的 iPhone。

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>現在就試：體驗無密碼登入

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 登入 Google 賬號 → 安全 → 通行金鑰 → 新增通行金鑰，體驗 Face ID/指紋登入。
2. 登入微軟賬號 → 安全 → 高階安全選項 → 新增通行金鑰。
3. 在淘寶、京東、eBay、PayPal 等已支援 Passkey 的服務上嚐鮮。
4. 保留傳統密碼作為後備，逐步遷移高價值賬號到 Passkey。
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>過渡期建議

{class="mt-1"}
Passkey 並未完全取代密碼——許多網站仍處於"Passkey + 密碼"並存階段。建議：高價值賬號優先開啟 Passkey，但<strong>不要立即刪除傳統密碼</strong>，留作備用；同時繼續使用密碼管理器，因為不是所有網站都支援 Passkey。把 Passkey 看作"密碼管理器的強力補充"而非"立刻替換"。
:::

#### 七、硬體安全金鑰

如果你對安全的要求高於普通使用者——比如持有大量加密貨幣、是高管/記者/活動人士、或保護企業核心賬號——硬體安全金鑰是比簡訊驗證碼更可靠的選擇。

##### 1. 什麼是硬體安全金鑰？

硬體金鑰是一個物理裝置（形似 U 盤），內部安全晶片儲存你的私鑰，需要物理接觸或 NFC 才能完成驗證。代表產品：

- <strong>YubiKey</strong>（Yubico 公司）：最主流，支援 FIDO2/WebAuthn、U2F、OTP、PIV、OpenPGP，USB-C / USB-A / NFC 等多種介面。5 系列 50-70 美元。
- <strong>Google Titan</strong>：Google 自家出品，USB-C + NFC / 藍芽，約 30-40 美元。
- <strong>OnlyKey</strong>：開源替代品，支援多種協議。
- <strong>國產替代</strong>：如飛天誠信 ePasskey，價格更親民。

##### 2. 為什麼硬體金鑰比簡訊驗證碼安全？

- <strong>抗釣魚</strong>：和 Passkey 一樣，硬體金鑰只對真實域名響應，釣魚網站無法騙取驗證碼。
- <strong>抗 SIM 劫持</strong>：簡訊驗證碼可被 SIM-swap 攻擊截獲，硬體金鑰無需手機號。
- <strong>抗中間人</strong>：FIDO2 協議每次簽名都包含挑戰值，無法重放。
- <strong>物理隔離</strong>：私鑰永遠在硬體晶片內，惡意軟體即使攻陷你的電腦也讀不到。

##### 3. 適用場景

- 加密貨幣交易所賬號、錢包恢復。
- 企業 SSO、遠端辦公 VPN、SSH 登入伺服器。
- 郵箱、GitHub、社交媒體等"主賬號"——一旦被攻破可重置所有其他賬號。
- 記者、律師、高管等高敏感人群。

##### 4. 如何配置硬體金鑰作為二次驗證

以 Google 賬號 + YubiKey 為例：

1. 購買 YubiKey（建議一次買兩把，一把日常用、一把備用，存放在不同地點）。
2. 登入 myaccount.google.com → 安全 → 兩步驗證。
3. 選擇"新增安全金鑰"→ 把 YubiKey 插入 USB-C 口或貼近手機 NFC 感應區。
4. 按提示觸控 YubiKey 金屬觸點完成註冊。
5. 建議註冊第二把備用金鑰。
6. 在"兩步驗證"設定裡，把硬體金鑰設為首選驗證方式，簡訊驗證碼作為備用。

主流支援的網站：Google、GitHub、Microsoft、Apple ID、Facebook、Twitter、Dropbox、GitLab、AWS、Coinbase、Binance 等。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>雙金鑰策略

{class="mt-1"}
硬體金鑰最大的風險是"丟失"。建議：① 同時註冊兩把不同的金鑰；② 一把隨身攜帶（鑰匙扣），一把存放在家中保險櫃或銀行保管箱；③ 部分網站允許把"備用恢復碼"列印出來離線儲存。這樣即使主金鑰丟失，也不會被永久鎖在賬號外。
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>購買渠道要謹慎

{class="mt-1"}
務必從官方店鋪或授權代理購買，不要買二手或來源不明的金鑰——理論上預置過的硬體可能已被植入後門。YubiKey 的韌體在出廠後無法更新，但 Yubico 會持續推送安全公告，關注其官網即可。
:::

#### 八、家庭/團隊密碼共享

家庭場景下，Netflix、家庭 Wi-Fi、路由器後臺、智慧門鎖密碼需要全家共用；團隊場景下，伺服器、資料庫、社交媒體賬號需要多人協作。<strong>用微信發密碼、寫在共享文件裡都是高危做法</strong>——一旦聊天記錄或文件許可權洩露，密碼就洩露了。

##### 1. 1Password 的"共享保險庫"（Vault）

1Password 是家庭和團隊共享的標杆產品。它的核心機制是<strong>多個保險庫</strong>：

- <strong>個人保險庫</strong>：只有你能看，如銀行、郵箱等私人賬號。
- <strong>共享保險庫</strong>：家人或團隊成員都能看，如 Netflix、家庭 Wi-Fi、共享信用卡。
- <strong>許可權分級</strong>：團隊版可設定某些成員"只檢視"或"只檢視但不編輯"。

家人或團隊成員無需共享主密碼，各自用自己的賬號登入，但可以看到被授權的共享保險庫內容。密碼修改後所有成員實時同步。

##### 2. Bitwarden 的"組織"功能

Bitwarden 的免費版支援個人密碼共享（透過"傳送 Send"功能限時分享單條密碼）；付費版可建立"組織"，把若干條目共享給家庭成員或團隊同事，許可權可細分。Bitwarden 還提供自託管選項，適合對資料主權要求高的企業。

##### 3. 家庭場景：共享 Netflix、Wi-Fi 等密碼的安全方式

- <strong>Netflix / 影片網站</strong>：用 1Password 家庭版的"共享保險庫"存登入密碼，家庭成員各自登入即可，無需在群裡發。
- <strong>家庭 Wi-Fi 密碼</strong>：iOS 裝置間可透過 AirDrop 直接共享 Wi-Fi 密碼給來訪的客人，無需念出來；安卓 12+ 也有"附近分享 Wi-Fi"功能。
- <strong>智慧門鎖、智慧家電</strong>：儘量用廠商 App 的"家庭成員"功能為每人單獨建立賬號，而不是共享一個管理員賬號。
- <strong>家用路由器後臺</strong>：管理員密碼存到 1Password 共享保險庫，訪客 Wi-Fi 單獨開一個 SSID。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>1Password 家庭版的價效比

{class="mt-1"}
1Password Families 約 4.99 美元/月，支援最多 5 位家庭成員，每人都有獨立的私人保險庫 + 4 個共享保險庫。算下來人均不到 1 美元/月，是目前家庭共享體驗最好的方案。Bitwarden 的家庭版 10 美元/年支援 6 人，價效比更高，但介面體驗略遜。
:::

##### 4. 團隊場景：伺服器/資料庫密碼共享

- <strong>1Password Teams / Business</strong>：可按部門、專案組建立多個保險庫，細粒度許可權控制，所有訪問行為可審計。
- <strong>Bitwarden Teams / Enterprise</strong>：開源方案，可自託管，企業版支援 SSO 整合、目錄同步。
- <strong>職責分離原則</strong>：管理員密碼不應只有一人掌握——設定 2-3 名"應急聯絡人"，確保關鍵人員離職/休假時業務不中斷。
- <strong>離職流程</strong>：員工離職時立即撤銷其密碼管理器訪問許可權，必要時旋轉所有他接觸過的高敏感密碼。

##### 5. 緊急訪問（Emergency Access）：萬一你出事

想象一個場景：你獨自管理家庭所有重要賬號，但意外住院或不幸離世，家人無法登入銀行、郵箱、保險賬號。<strong>"緊急訪問"功能</strong>正是為此設計——授權一位信任的家人/朋友，在你無法響應時獲取你的密碼庫。

<strong>Bitwarden 緊急訪問設定：</strong>

1. 登入 Bitwarden Web Vault → 設定 → 緊急訪問。
2. 新增信任聯絡人的郵箱，邀請對方接受。
3. 設定"等待期"（建議 7-14 天）：從對方發起請求到你確認的時間視窗。
4. 如果你在等待期內不響應（拒絕或不操作），到期後對方自動獲得訪問權。
5. 你隨時可以手動拒絕請求或撤銷緊急訪問許可權。

<strong>1Password 緊急訪問：</strong>

1. 1Password 不直接叫"緊急訪問"，但透過"家庭/團隊組織"功能可實現——把家人加入家庭版後，將部分條目放入"共享保險庫"。
2. 對個人版使用者，建議把主密碼告知一位高度信任的家人，或寫入密封信封存放於保險櫃。
3. 1Password 還提供"恢復碼"，開啟雙重認證時務必列印儲存。

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>現在就設：為家人留一把"備用鑰匙"

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 選定一位信任的家人作為"緊急聯絡人"。
2. 在密碼管理器中設定緊急訪問（Bitwarden）或加入家庭共享保險庫（1Password）。
3. 把主密碼 + 恢復碼寫在紙上，封進信封，存放於家中保險櫃或告知可信家人。
4. 每半年回顧一次，確認緊急聯絡人是否仍然合適。
:::

#### 九、密碼管理器使用最佳實踐

- <strong>設定強主密碼</strong>：主密碼是最後一道防線，務必設定一個長且複雜的密碼，並牢記。
- <strong>啟用雙重認證</strong>：為密碼管理器賬號開啟雙重認證，增加一層保護。
- <strong>定期檢查弱密碼</strong>：大多數密碼管理器有"安全審計"功能，幫你找出弱密碼和重複密碼。
- <strong>不要忘記主密碼</strong>：主密碼無法找回，忘記就意味著丟失所有密碼。建議寫在紙上，放在安全的地方。
- <strong>緊急訪問</strong>：設定緊急聯絡人，萬一你無法訪問，信任的人可以獲取你的密碼。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>重要提醒

{class="mt-1"}
密碼管理器雖然方便，但也有風險：如果主密碼洩露，所有密碼都暴露了。所以主密碼絕對不能和其他密碼相同，也不能寫在容易被找到的地方。另外，建議選擇有良好安全記錄的服務商。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>現在就試：開始使用密碼管理器

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 選擇一個密碼管理器（推薦Bitwarden或系統自帶）。
2. 註冊賬號，設定一個強主密碼。
3. 匯入現有密碼（如果有的話）或開始新增新密碼。
4. 安裝瀏覽器外掛或手機App，體驗自動填充功能。
5. 檢查安全審計報告，找出需要改進的密碼。
:::
