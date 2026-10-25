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
喺數碼時代，密碼就係你嘅門匙。但匙太多、太複雜，點算？密碼管理器就係你嘅「萬能匙管家」。

#### 一、點解你需要密碼管理器？

現代人平均有幾十甚至上百個網絡帳號。如果每個帳號都用相同嘅密碼，一旦一個網站被駭，所有帳號都危險。如果每個帳號都用唔同嘅複雜密碼，根本記唔住。

密碼管理器解決咗呢個困境：你淨係需要記住一個主密碼，佢幫你記住所有其他密碼。

#### 二、密碼管理器嘅工作原理

1. <strong>加密存儲</strong>：所有密碼都經過高強度加密存儲，淨係你可以解密。
2. <strong>主密碼</strong>：你設定一個主密碼，用於解鎖密碼庫。主密碼本身唔存儲喺伺服器上。
3. <strong>自動填充</strong>：喺網站或App登入介面，密碼管理器自動填充帳號密碼。
4. <strong>密碼生成</strong>：可以生成隨機、複雜嘅密碼，提高安全性。

#### 三、加密原理簡介

瞭解密碼管理器嘅加密原理，可以幫你判斷一個服務商係咪值得信任。下面用通俗嘅語言解釋幾個核心概念。

##### 1. AES-256 加密

AES（高級加密標準）係美國國家標準與技術研究院（NIST）認可嘅對稱加密算法，被銀行、軍方、政府廣泛使用。「256」指密鑰長度為 256 位——理論上需要超過宇宙年齡嘅時間先可以暴力破解。主流密碼管理器（1Password、Bitwarden、KeePass 等）都用 AES-256 加密你嘅密碼庫。

##### 2. 零知識架構（Zero-Knowledge Architecture）

「零知識」唔係話服務商乜都唔存，而係話<strong>加密同解密都喺你嘅設備本地完成，伺服器淨係保存已加密嘅密文</strong>。具體流程：

1. 你喺用戶端輸入主密碼。
2. 用戶端用主密碼派生出加密密鑰（呢一步喺你手機/電腦上完成）。
3. 淨係加密後嘅密文先上傳到伺服器。
4. 下次登入時，伺服器將密文下發，用戶端再次用主密碼解密。

關鍵點：<strong>主密碼本身從不離開你嘅設備</strong>，伺服器上都冇。所以即使服務商被駭，黑客攞到嘅都淨係一堆無法解密嘅密文——除非佢哋可以猜中你嘅主密碼。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>點解「零知識」意味住服務商都睇唔到你嘅密碼？

{class="mt-1"}
因為解密密鑰由你嘅主密碼派生，而主密碼淨係存在你腦中、淨係喺你本地設備上使用。服務商嘅伺服器上既冇主密碼，都冇解密密鑰，淨係得密文。呢個就係點解 Bitwarden、1Password 等正規服務商都明確聲明「我哋都無法睇到你嘅密碼」——唔係佢哋唔想睇，係技術上做不到。
:::

##### 3. 密鑰派生函數：PBKDF2 與 Argon2

主密碼唔可以直接用作加密密鑰——佢需要經過「密鑰派生函數」處理。呢個函數嘅作用係<strong>故意等計算變慢</strong>，等黑客暴力破解嘅成本高到不可行。

- <strong>PBKDF2</strong>：老牌標準，被 iCloud 鑰匙串、Bitwarden、LastPass 等廣泛使用。通過反覆迭代（通常 10 萬次以上）雜湊嚟拖慢破解。
- <strong>Argon2</strong>：2015 年密碼雜湊競賽冠軍，比 PBKDF2 更現代。除咗「算力消耗」仲引入咗「記憶體消耗」——等 GPU/ASIC 等專用硬件都難以加速破解。Bitwarden、KeePassXC 等已支援。

迭代次數越高越安全，但解鎖速度都會變慢。正規服務商都會公開佢使用嘅派生算法同迭代次數，方便安全社區審計。

##### 4. 案例警示：LastPass 2022 年數據洩露

2022 年 8 月，老牌密碼管理器 LastPass 公告佢嘅開發環境被入侵；同年 11 月進一步披露，黑客攞走咗用戶嘅密碼庫備份（加密後嘅密文）。事件嘅關鍵教訓：

- <strong>零知識架構守住咗底線</strong>：由於密碼庫本身係加密嘅，黑客攞到密文但解唔開——前提係用戶嘅主密碼足夠強。
- <strong>弱主密碼用戶最危險</strong>：黑客可以離線暴力破解弱主密碼，因此使用弱主密碼或重複主密碼嘅用戶面臨實質風險。
- <strong>元數據都洩露</strong>：雖然密碼內容加密，但站點 URL、備註等元數據可能未加密，會暴露用戶使用咗邊啲服務。

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>由 LastPass 事件學到嘅

{class="mt-1"}
第一，主密碼必須長而且獨特（建議 16 位以上，包含大小寫、數字、符號）；第二，優先選擇支援 Argon2id、迭代次數高嘅服務商；第三，對高價值帳號（銀行、郵箱）務必開啟獨立嘅二次驗證，唔好淨係依賴密碼管理器。
:::

#### 四、主流密碼管理器推薦

##### 系統自帶：

- <strong>iCloud鑰匙串</strong>：蘋果生態用戶首選。同Safari、App無縫整合，免費，安全。缺點係跨平臺使用不便。
- <strong>Google密碼管理器</strong>：安卓用戶方便。同Chrome、安卓系統整合，免費。
- <strong>華為密碼保險箱</strong>：鴻蒙系統內置，適合華為用戶。

##### 第三方專業工具：

- <strong>Bitwarden</strong>：開源免費，功能強大，支援所有平臺。強烈推薦畀注重私隱嘅用戶。
- <strong>1Password</strong>：介面美觀，功能豐富，適閤家庭同團隊。付費。
- <strong>LastPass</strong>：老牌密碼管理器，免費版功能受限。
- <strong>KeePass</strong>：完全本地存儲，開源免費。適合極客用戶。

#### 五、密碼強度真實評估

密碼管理器普遍會顯示「密碼強度」指示條（紅/黃/綠），但呢個評估往往淨係睇長度同字符種類，並不全面。真正判斷密碼係咪安全，需要考慮「熵」同「係咪已洩露」。

##### 1. 熵（Entropy）：密碼強度嘅科學度量

「熵」衡量密碼嘅不確定性，單位係比特。熵越高，暴力破解所需嘗試次數越多。

- <strong>"123456"</strong>：熵極低，瞬間破解。
- <strong>"P@ssw0rd"</strong>：睇落複雜，但出現喺所有字典攻擊列表入面，熵依然低。
- <strong>"correct horse battery staple"</strong>：四個隨機單詞，熵約 44 比特，破解難度遠超「P@ssw0rd」。
- <strong>16 位隨機字符（含大小寫+數字+符號）</strong>：熵約 100 比特，目前算力無法暴力破解。

結論：<strong>「長度 + 隨機性」比「複雜符號」更重要</strong>。呢個都係密碼管理器生成嘅隨機長密碼真正安全嘅原因。

##### 2. HaveIBeenPwned：查你嘅密碼係咪已洩露

安全研究員 Troy Hunt 維護嘅 <a href="https://haveibeenpwned.com" class="text-primary hover:underline" target="_blank" rel="noopener">haveibeenpwned.com</a> 收錄咗歷次大型數據洩露中流出嘅帳號同密碼。你可以：

1. 輸入郵箱，查你嘅帳號係咪喺某次洩露中被曝光。
2. 用 Pwned Passwords 功能查詢某個密碼係咪喺已知洩露庫中（密碼管理器同瀏覽器都已內置此查詢）。

如果一個密碼出現喺洩露庫中，<strong>無論佢睇落幾複雜都必須立即更換</strong>——因為字典攻擊會優先嘗試呢啲已知密碼。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-shield-alt mr-2"></i>k-Anonymity 查詢原理

{class="mt-1"}
擔心喺 HaveIBeenPwned 輸入密碼會再次洩露？唔使擔心。現代查詢採用「k-匿名」協議：瀏覽器淨係將密碼雜湊嘅前 5 位發畀伺服器，伺服器返所有以呢 5 位開頭嘅雜湊列表，本地再比對。即係話，伺服器永遠睇唔到你嘅完整密碼雜湊。1Password、Bitwarden 嘅「已洩露密碼檢測」都係咁樣工作嘅。
:::

##### 3. 密碼管理器內置嘅監控功能

- <strong>1Password Watchtower</strong>：實時監控弱密碼、重複密碼、已洩露密碼、過期密碼、唔使用 2FA 嘅網站，並以紅/橙/黃分級展示。
- <strong>Bitwarden Vault Health</strong>：免費版即可查看弱密碼、重複密碼；付費版可檢測已洩露密碼（基於 HaveIBeenPwned）。
- <strong>iCloud 鑰匙串「安全建議」</strong>：iOS 設定 → 密碼 → 安全建議，會提示你邊啲密碼出現喺已知洩露中、邊啲重複使用。
- <strong>Google 密碼管理器「密碼檢查工具」</strong>：Chrome 內置，可以一鍵檢查已洩露、弱、重複密碼。

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>而家就查：你嘅密碼係咪安全

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 打開 haveibeenpwned.com，輸入你嘅常用郵箱，睇下出現喺邊啲洩露事件中。
2. iPhone 用戶：設定 → 密碼 → 安全建議，逐條處理紅色警告。
3. Chrome 用戶：設定 → 密碼 → 檢查密碼，按提示修改。
4. 1Password/Bitwarden 用戶：打開 Watchtower/Health Reports，優先處理「已洩露」同「重複」項。
:::

#### 六、Passkey：無密碼登入嘅未來

2024-2026 年，密碼技術正在經歷一場革命——<strong>Passkey（通行密鑰）</strong>有望徹底淘汰傳統密碼。Apple、Google、Microsoft 三大平臺聯合推動，FIDO 聯盟同萬維網聯盟（W3C）背書，呢個係數十年嚟登入方式最大嘅一次變革。

##### 1. 乜嘢係 Passkey？

Passkey 基於 FIDO2 / WebAuthn 標準，用<strong>設備上嘅密鑰對</strong>替代密碼。原理可以簡化為：

- 你嘅手機生成一對密鑰：<strong>公鑰</strong>（註冊畀網站）+ <strong>私鑰</strong>（永遠存在你設備嘅安全晶片中）。
- 登入時，網站發一個「挑戰」，你嘅手機用私鑰簽名，再由網站用公鑰驗證。
- 簽名前需要你通過生物識別（Face ID / 指紋）或設備 PIN 確認身份。
- 整個過程中，<strong>冇任何密碼喺網絡中傳輸</strong>。

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
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">天然抗釣魚，私鑰淨係對真實域名簽名</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">伺服器洩露影響</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">密碼雜湊可能被破解</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">伺服器淨係存公鑰，洩露無影響</td>
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

- <strong>Apple iCloud 鑰匙串 Passkey</strong>：iOS 16+ / macOS Ventura+ 原生支援，Passkey 可以喺所有登入同一 Apple ID 嘅設備間同步，新設備登入網站時唔使重新創建。
- <strong>Google 密碼管理器 Passkey</strong>：安卓 + Chrome 原生支援，Passkey 存喺 Google 賬戶中，跨安卓設備同步；2023 年起 Google 個人帳號已支援用 Passkey 登入。
- <strong>Microsoft</strong>：Windows 11 / Edge 已支援 Passkey；微軟帳號、Outlook、Office 等服務陸續開放 Passkey 登入，並可以喺 Microsoft Authenticator 中管理。
- <strong>1Password / Bitwarden</strong>：已支援 Passkey 嘅創建、存儲、跨平臺同步，等你唔受限於單一生態。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>跨設備同步係關鍵突破

{class="mt-1"}
早期 Passkey 嘅最大痛點係「綁定單台設備」——換手機就要重新創建。2023 年起 Apple、Google、Microsoft 實現咗 Passkey 嘅雲端同步：iCloud 鑰匙串同步跨 Apple 設備，Google 密碼管理器同步跨安卓設備。1Password 等第三方就打通咗跨生態同步。呢個意味住 Passkey 已具備替代密碼嘅實用性。
:::

##### 4. 點樣喺手機上創建同使用 Passkey

<strong>iOS（iPhone）路徑：</strong>

1. 喺支援 Passkey 嘅網站（如 Google、微軟、亞馬遜、eBay、PayPal）帳號安全頁選擇「添加通行密鑰 / Add passkey」。
2. 系統彈出 Face ID / Touch ID 驗證視窗，通過後 Passkey 自動生成並儲存到 iCloud 鑰匙串。
3. 下次登入該網站時，輸入用戶名後選擇「使用 iPhone 登入」，Face ID 一嘟即可。
4. 管理入口：設定 → 密碼 → 揾到對應網站，可見 Passkey 條目。

<strong>安卓路徑：</strong>

1. 喺支援 Passkey 嘅網站帳號安全頁選擇「添加通行密鑰」。
2. Google 密碼管理器彈窗 → 選擇你嘅 Google 帳號 → 螢幕鎖驗證（指紋/圖案/PIN）。
3. Passkey 自動儲存到 Google 密碼管理器，跨同帳號安卓設備同步。
4. 下次登入時，選擇「使用 Passkey」，螢幕鎖一解即可。
5. 管理入口：安卓設定 → 密碼、密鑰同自動填充 → 密碼管理器 → google.com。

##### 5. Passkey 跨設備登入

如果你喺 Windows 電腦上登入一個淨係得 iPhone 上有 Passkey 嘅網站，可以掃碼授權：

1. 網站登入頁選擇「使用 Passkey」。
2. 選擇「使用其他設備」。
3. 電腦顯示二維碼，用 iPhone 掃碼。
4. iPhone 彈出 Face ID 驗證，確認後網站喺電腦上完成登入。

呢個過程通過藍牙+互聯網雙重加密通信，Passkey 私鑰唔會離開你嘅 iPhone。

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>而家就試：體驗無密碼登入

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 登入 Google 帳號 → 安全 → 通行密鑰 → 添加通行密鑰，體驗 Face ID/指紋登入。
2. 登入微軟帳號 → 安全 → 進階安全選項 → 添加通行密鑰。
3. 喺淘寶、京東、eBay、PayPal 等已支援 Passkey 嘅服務上嘗鮮。
4. 保留傳統密碼作為後備，逐步遷移高價值帳號到 Passkey。
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>過渡期建議

{class="mt-1"}
Passkey 並未完全取代密碼——好多網站仍處於「Passkey + 密碼」並存階段。建議：高價值帳號優先開啟 Passkey，但<strong>唔好立即刪除傳統密碼</strong>，留作備用；同時繼續使用密碼管理器，因為唔係所有網站都支援 Passkey。將 Passkey 睇作「密碼管理器嘅強力補充」而唔係「立刻替換」。
:::

#### 七、硬件安全密鑰

如果你對安全嘅要求高過普通用戶——比如持有大量加密貨幣、係高管/記者/活動人士、或保護企業核心帳號——硬件安全密鑰係比短訊驗證碼更可靠嘅選擇。

##### 1. 乜嘢係硬件安全密鑰？

硬件密鑰係一個物理設備（形似 U 盤），內部安全晶片存儲你嘅私鑰，需要物理接觸或 NFC 先可以完成驗證。代表產品：

- <strong>YubiKey</strong>（Yubico 公司）：最主流，支援 FIDO2/WebAuthn、U2F、OTP、PIV、OpenPGP，USB-C / USB-A / NFC 等多種介面。5 系列 50-70 美元。
- <strong>Google Titan</strong>：Google 自家出品，USB-C + NFC / 藍牙，約 30-40 美元。
- <strong>OnlyKey</strong>：開源替代品，支援多種協議。
- <strong>國產替代</strong>：如飛天誠信 ePasskey，價格更親民。

##### 2. 點解硬件密鑰比短訊驗證碼安全？

- <strong>抗釣魚</strong>：同 Passkey 一樣，硬件密鑰淨係對真實域名響應，釣魚網站無法騙取驗證碼。
- <strong>抗 SIM 劫持</strong>：短訊驗證碼可被 SIM-swap 攻擊截獲，硬件密鑰唔使手機號。
- <strong>抗中間人</strong>：FIDO2 協議每次簽名都包含挑戰值，無法重放。
- <strong>物理隔離</strong>：私鑰永遠喺硬件晶片內，惡意軟件即使攻陷你嘅電腦都讀唔到。

##### 3. 適用場景

- 加密貨幣交易所帳號、錢包恢復。
- 企業 SSO、遠端辦公 VPN、SSH 登入伺服器。
- 郵箱、GitHub、社交媒體等「主帳號」——一旦被攻破可重置所有其他帳號。
- 記者、律師、高管等高敏感人羣。

##### 4. 點樣配置硬件密鑰作為二次驗證

以 Google 帳號 + YubiKey 為例：

1. 購買 YubiKey（建議一次買兩把，一把日常用、一把備用，存放喺唔同地點）。
2. 登入 myaccount.google.com → 安全 → 兩步驗證。
3. 選擇「添加安全密鑰」→ 將 YubiKey 插入 USB-C 口或貼近手機 NFC 感應區。
4. 按提示觸摸 YubiKey 金屬觸點完成註冊。
5. 建議註冊第二把備用密鑰。
6. 喺「兩步驗證」設定入面，將硬件密鑰設為首選驗證方式，短訊驗證碼作為備用。

主流支援嘅網站：Google、GitHub、Microsoft、Apple ID、Facebook、Twitter、Dropbox、GitLab、AWS、Coinbase、Binance 等。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>雙密鑰策略

{class="mt-1"}
硬件密鑰最大嘅風險係「遺失」。建議：① 同時註冊兩把唔同嘅密鑰；② 一把隨身攜帶（鑰匙扣），一把存放喺屋企保險櫃或銀行保管箱；③ 部分網站允許將「備用恢復碼」列印出嚟離線保存。咁樣即使主密鑰遺失，都唔會被永久鎖喺帳號外。
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>購買渠道要謹慎

{class="mt-1"}
務必由官方店鋪或授權代理購買，唔好買二手或來源不明嘅密鑰——理論上預置過嘅硬件可能已被植入後門。YubiKey 嘅韌體喺出廠後無法更新，但 Yubico 會持續推送安全公告，關注佢官網即可。
:::

#### 八、家庭/團隊密碼共享

家庭場景下，Netflix、家庭 Wi-Fi、路由器後台、智能門鎖密碼需要全家共用；團隊場景下，伺服器、數據庫、社交媒體帳號需要多人協作。<strong>用微信發密碼、寫喺共享文檔入面都係高危做法</strong>——一旦聊天記錄或文檔權限洩露，密碼就洩露咗。

##### 1. 1Password 嘅「共享保險庫」（Vault）

1Password 係家庭同團隊共享嘅標杆產品。佢嘅核心機制係<strong>多個保險庫</strong>：

- <strong>個人保險庫</strong>：淨係你可以睇，如銀行、郵箱等私人帳號。
- <strong>共享保險庫</strong>：家人或團隊成員都可以睇，如 Netflix、家庭 Wi-Fi、共享信用卡。
- <strong>權限分級</strong>：團隊版可設定某些成員「淨係查看」或「淨係查看但不編輯」。

家人或團隊成員唔使共享主密碼，各自用自己嘅帳號登入，但可以睇到被授權嘅共享保險庫內容。密碼修改後所有成員實時同步。

##### 2. Bitwarden 嘅「組織」功能

Bitwarden 嘅免費版支援個人密碼共享（通過「發送 Send」功能限時分享單條密碼）；付費版可創建「組織」，將若干條目共享畀家庭成員或團隊同事，權限可細分。Bitwarden 仲提供自託管選項，適合對數據主權要求高嘅企業。

##### 3. 家庭場景：共享 Netflix、Wi-Fi 等密碼嘅安全方式

- <strong>Netflix / 影片網站</strong>：用 1Password 家庭版嘅「共享保險庫」存登入密碼，家庭成員各自登入即可，唔使喺羣入面發。
- <strong>家庭 Wi-Fi 密碼</strong>：iOS 設備間可通過 AirDrop 直接共享 Wi-Fi 密碼畀來訪嘅客人，唔使讀出嚟；安卓 12+ 都有「附近分享 Wi-Fi」功能。
- <strong>智能門鎖、智能家電</strong>：盡量用廠商 App 嘅「家庭成員」功能為每人單獨創建帳號，而唔係共享一個管理員帳號。
- <strong>家用路由器後台</strong>：管理員密碼存到 1Password 共享保險庫，訪客 Wi-Fi 單獨開一個 SSID。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>1Password 家庭版嘅性價比

{class="mt-1"}
1Password Families 約 4.99 美元/月，支援最多 5 位家庭成員，每人都有獨立嘅私人保險庫 + 4 個共享保險庫。計落人均唔到 1 美元/月，係目前家庭共享體驗最好嘅方案。Bitwarden 嘅家庭版 10 美元/年支援 6 人，性價比更高，但介面體驗略遜。
:::

##### 4. 團隊場景：伺服器/數據庫密碼共享

- <strong>1Password Teams / Business</strong>：可按部門、項目組創建多個保險庫，細粒度權限控制，所有訪問行為可審計。
- <strong>Bitwarden Teams / Enterprise</strong>：開源方案，可自託管，企業版支援 SSO 整合、目錄同步。
- <strong>職責分離原則</strong>：管理員密碼唔應該淨係得一人掌握——設定 2-3 名「緊急聯絡人」，確保關鍵人員離職/休假時業務不中斷。
- <strong>離職流程</strong>：員工離職時立即撤銷其密碼管理器訪問權限，必要時旋轉所有佢接觸過嘅高敏感密碼。

##### 5. 緊急訪問（Emergency Access）：萬一你出事

想像一個場景：你獨自管理家庭所有重要帳號，但意外住院或不幸離世，家人無法登入銀行、郵箱、保險帳號。<strong>「緊急訪問」功能</strong>正係為此設計——授權一位信任嘅家人/朋友，喺你無法響應時獲取你嘅密碼庫。

<strong>Bitwarden 緊急訪問設定：</strong>

1. 登入 Bitwarden Web Vault → 設定 → 緊急訪問。
2. 添加信任聯絡人嘅郵箱，邀請對方接受。
3. 設定「等待期」（建議 7-14 天）：由對方發起請求到你確認嘅時間窗口。
4. 如果你喺等待期內唔響應（拒絕或唔操作），到期後對方自動獲得訪問權。
5. 你隨時可以手動拒絕請求或撤銷緊急訪問權限。

<strong>1Password 緊急訪問：</strong>

1. 1Password 唔直接叫「緊急訪問」，但通過「家庭/團隊組織」功能可實現——將家人加入家庭版後，將部分條目放入「共享保險庫」。
2. 對個人版用戶，建議將主密碼告知一位高度信任嘅家人，或寫入密封信封存放於保險櫃。
3. 1Password 仲提供「恢復碼」，開啟雙重認證時務必列印保存。

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>而家就設：為家人留一把「備用匙」

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 選定一位信任嘅家人作為「緊急聯絡人」。
2. 喺密碼管理器中設定緊急訪問（Bitwarden）或加入家庭共享保險庫（1Password）。
3. 將主密碼 + 恢復碼寫喺紙上，封入信封，存放於屋企保險櫃或告知可信家人。
4. 每半年回顧一次，確認緊急聯絡人係咪仍然合適。
:::

#### 九、密碼管理器使用最佳實踐

- <strong>設定強主密碼</strong>：主密碼係最後一道防線，務必設定一個長而且複雜嘅密碼，並牢記。
- <strong>啟用雙重認證</strong>：為密碼管理器帳號開啟雙重認證，增加一層保護。
- <strong>定期檢查弱密碼</strong>：大多數密碼管理器有「安全審計」功能，幫你揾出弱密碼同重複密碼。
- <strong>唔好忘記主密碼</strong>：主密碼無法揾返，忘記就意味住遺失所有密碼。建議寫喺紙上，放喺安全嘅地方。
- <strong>緊急訪問</strong>：設定緊急聯絡人，萬一你無法訪問，信任嘅人可以獲取你嘅密碼。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>重要提醒

{class="mt-1"}
密碼管理器雖然方便，但都有風險：如果主密碼洩露，所有密碼都暴露咗。所以主密碼絕對唔可以同其他密碼相同，都唔可以寫喺容易被揾到嘅地方。另外，建議選擇有良好安全記錄嘅服務商。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>而家就試：開始使用密碼管理器

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 選擇一個密碼管理器（推薦Bitwarden或系統自帶）。
2. 註冊帳號，設定一個強主密碼。
3. 匯入現有密碼（如果有嘅話）或開始添加新密碼。
4. 安裝瀏覽器插件或手機App，體驗自動填充功能。
5. 檢查安全審計報告，揾出需要改進嘅密碼。
:::
