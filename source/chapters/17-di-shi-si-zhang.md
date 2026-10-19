---
id: di-shi-si-zhang
num: 14
part: ruan-jian-pian
nav: 第十四章：密码管理器专题
toc: default
kind: chapter
---

### 第十四章：密码管理器专题

{class="chapter-intro mb-4"}
在数字时代，密码就是你的家门钥匙。但钥匙太多、太复杂，怎么办？密码管理器就是你的"万能钥匙管家"。

#### 一、为什么你需要密码管理器？

现代人平均有几十甚至上百个网络账号。如果每个账号都用相同的密码，一旦一个网站被黑，所有账号都危险。如果每个账号都用不同的复杂密码，根本记不住。

密码管理器解决了这个困境：你只需要记住一个主密码，它帮你记住所有其他密码。

#### 二、密码管理器的工作原理

1. <strong>加密存储</strong>：所有密码都经过高强度加密存储，只有你能解密。
2. <strong>主密码</strong>：你设置一个主密码，用于解锁密码库。主密码本身不存储在服务器上。
3. <strong>自动填充</strong>：在网站或App登录界面，密码管理器自动填充账号密码。
4. <strong>密码生成</strong>：可以生成随机、复杂的密码，提高安全性。

#### 三、加密原理简介

了解密码管理器的加密原理，能帮你判断一个服务商是否值得信任。下面用通俗的语言解释几个核心概念。

##### 1. AES-256 加密

AES（高级加密标准）是美国国家标准与技术研究院（NIST）认可的对称加密算法，被银行、军方、政府广泛使用。"256"指密钥长度为 256 位——理论上需要超过宇宙年龄的时间才能暴力破解。主流密码管理器（1Password、Bitwarden、KeePass 等）都用 AES-256 加密你的密码库。

##### 2. 零知识架构（Zero-Knowledge Architecture）

"零知识"不是说服务商什么都不存，而是说<strong>加密和解密都在你的设备本地完成，服务器只保存已加密的密文</strong>。具体流程：

1. 你在客户端输入主密码。
2. 客户端用主密码派生出加密密钥（这一步在你手机/电脑上完成）。
3. 只有加密后的密文才上传到服务器。
4. 下次登录时，服务器把密文下发，客户端再次用主密码解密。

关键点：<strong>主密码本身从不离开你的设备</strong>，服务器上也没有。所以即使服务商被黑，黑客拿到的也只是一堆无法解密的密文——除非他们能猜出你的主密码。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>为什么"零知识"意味着服务商也看不到你的密码？

{class="mt-1"}
因为解密密钥由你的主密码派生，而主密码只存在于你脑中、只在你本地设备上使用。服务商的服务器上既没有主密码，也没有解密密钥，只有密文。这就是为什么 Bitwarden、1Password 等正规服务商都明确声明"我们也无法看到你的密码"——不是他们不想看，是技术上做不到。
:::

##### 3. 密钥派生函数：PBKDF2 与 Argon2

主密码不能直接用作加密密钥——它需要经过"密钥派生函数"处理。这个函数的作用是<strong>故意让计算变慢</strong>，让黑客暴力破解的成本高到不可行。

- <strong>PBKDF2</strong>：老牌标准，被 iCloud 钥匙串、Bitwarden、LastPass 等广泛使用。通过反复迭代（通常 10 万次以上）哈希来拖慢破解。
- <strong>Argon2</strong>：2015 年密码哈希竞赛冠军，比 PBKDF2 更现代。除了"算力消耗"还引入了"内存消耗"——让 GPU/ASIC 等专用硬件也难以加速破解。Bitwarden、KeePassXC 等已支持。

迭代次数越高越安全，但解锁速度也会变慢。正规服务商都会公开其使用的派生算法和迭代次数，便于安全社区审计。

##### 4. 案例警示：LastPass 2022 年数据泄露

2022 年 8 月，老牌密码管理器 LastPass 公告其开发环境被入侵；同年 11 月进一步披露，黑客拿走了用户的密码库备份（加密后的密文）。事件的关键教训：

- <strong>零知识架构守住了底线</strong>：由于密码库本身是加密的，黑客拿到密文但解不开——前提是用户的主密码足够强。
- <strong>弱主密码用户最危险</strong>：黑客可以离线暴力破解弱主密码，因此使用弱主密码或重复主密码的用户面临实质风险。
- <strong>元数据也泄露</strong>：虽然密码内容加密，但站点 URL、备注等元数据可能未加密，会暴露用户使用了哪些服务。

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>从 LastPass 事件学到的

{class="mt-1"}
第一，主密码必须长且独特（建议 16 位以上，包含大小写、数字、符号）；第二，优先选择支持 Argon2id、迭代次数高的服务商；第三，对高价值账号（银行、邮箱）务必开启独立的二次验证，不要只依赖密码管理器。
:::

#### 四、主流密码管理器推荐

##### 系统自带：

- <strong>iCloud钥匙串</strong>：苹果生态用户首选。与Safari、App无缝集成，免费，安全。缺点是跨平台使用不便。
- <strong>Google密码管理器</strong>：安卓用户方便。与Chrome、安卓系统集成，免费。
- <strong>华为密码保险箱</strong>：鸿蒙系统内置，适合华为用户。

##### 第三方专业工具：

- <strong>Bitwarden</strong>：开源免费，功能强大，支持所有平台。强烈推荐给注重隐私的用户。
- <strong>1Password</strong>：界面美观，功能丰富，适合家庭和团队。付费。
- <strong>LastPass</strong>：老牌密码管理器，免费版功能受限。
- <strong>KeePass</strong>：完全本地存储，开源免费。适合极客用户。

#### 五、密码强度真实评估

密码管理器普遍会显示"密码强度"指示条（红/黄/绿），但这个评估往往只看长度和字符种类，并不全面。真正判断密码是否安全，需要考虑"熵"和"是否已泄露"。

##### 1. 熵（Entropy）：密码强度的科学度量

"熵"衡量密码的不确定性，单位是比特。熵越高，暴力破解所需尝试次数越多。

- <strong>"123456"</strong>：熵极低，瞬间破解。
- <strong>"P@ssw0rd"</strong>：看似复杂，但出现在所有字典攻击列表里，熵依然低。
- <strong>"correct horse battery staple"</strong>：四个随机单词，熵约 44 比特，破解难度远超"P@ssw0rd"。
- <strong>16 位随机字符（含大小写+数字+符号）</strong>：熵约 100 比特，目前算力无法暴力破解。

结论：<strong>"长度 + 随机性"比"复杂符号"更重要</strong>。这也是密码管理器生成的随机长密码真正安全的原因。

##### 2. HaveIBeenPwned：查你的密码是否已泄露

安全研究员 Troy Hunt 维护的 <a href="https://haveibeenpwned.com" class="text-primary hover:underline" target="_blank" rel="noopener">haveibeenpwned.com</a> 收录了历次大型数据泄露中流出的账号和密码。你可以：

1. 输入邮箱，查你的账号是否在某次泄露中被曝光。
2. 用 Pwned Passwords 功能查询某个密码是否在已知泄露库中（密码管理器和浏览器都已内置此查询）。

如果一个密码出现在泄露库中，<strong>无论它看起来多复杂都必须立即更换</strong>——因为字典攻击会优先尝试这些已知密码。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-shield-alt mr-2"></i>k-Anonymity 查询原理

{class="mt-1"}
担心在 HaveIBeenPwned 输入密码会再次泄露？不必担心。现代查询采用"k-匿名"协议：浏览器只把密码哈希的前 5 位发给服务器，服务器返回所有以这 5 位开头的哈希列表，本地再比对。也就是说，服务器永远看不到你的完整密码哈希。1Password、Bitwarden 的"已泄露密码检测"都是这样工作的。
:::

##### 3. 密码管理器内置的监控功能

- <strong>1Password Watchtower</strong>：实时监控弱密码、重复密码、已泄露密码、过期密码、不使用 2FA 的网站，并以红/橙/黄分级展示。
- <strong>Bitwarden Vault Health</strong>：免费版即可查看弱密码、重复密码；付费版可检测已泄露密码（基于 HaveIBeenPwned）。
- <strong>iCloud 钥匙串"安全建议"</strong>：iOS 设置 → 密码 → 安全建议，会提示你哪些密码出现在已知泄露中、哪些重复使用。
- <strong>Google 密码管理器"密码检查工具"</strong>：Chrome 内置，可一键检查已泄露、弱、重复密码。

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>现在就查：你的密码是否安全

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 打开 haveibeenpwned.com，输入你的常用邮箱，看看出现在哪些泄露事件中。
2. iPhone 用户：设置 → 密码 → 安全建议，逐条处理红色警告。
3. Chrome 用户：设置 → 密码 → 检查密码，按提示修改。
4. 1Password/Bitwarden 用户：打开 Watchtower/Health Reports，优先处理"已泄露"和"重复"项。
:::

#### 六、Passkey：无密码登录的未来

2024-2026 年，密码技术正在经历一场革命——<strong>Passkey（通行密钥）</strong>有望彻底淘汰传统密码。Apple、Google、Microsoft 三大平台联合推动，FIDO 联盟和万维网联盟（W3C）背书，这是数十年来登录方式最大的一次变革。

##### 1. 什么是 Passkey？

Passkey 基于 FIDO2 / WebAuthn 标准，用<strong>设备上的密钥对</strong>替代密码。原理可以简化为：

- 你的手机生成一对密钥：<strong>公钥</strong>（注册给网站）+ <strong>私钥</strong>（永远存在你设备的安全芯片中）。
- 登录时，网站发一个"挑战"，你的手机用私钥签名，再由网站用公钥验证。
- 签名前需要你通过生物识别（Face ID / 指纹）或设备 PIN 确认身份。
- 整个过程中，<strong>没有任何密码在网络中传输</strong>。

##### 2. Passkey vs 传统密码

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">维度</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">传统密码</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Passkey</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">抗钓鱼</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">差，钓鱼网站可窃取密码</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">天然抗钓鱼，私钥只对真实域名签名</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">服务器泄露影响</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">密码哈希可能被破解</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">服务器只存公钥，泄露无影响</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">便捷性</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需记忆/输入/管理</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Face ID/指纹一秒登录</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">重放攻击</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可能被中间人截获重放</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每次签名一次性，无法重放</td>
                            </tr>
                        </tbody>
                    </table>
```

##### 3. 各平台支持情况

- <strong>Apple iCloud 钥匙串 Passkey</strong>：iOS 16+ / macOS Ventura+ 原生支持，Passkey 可在所有登录同一 Apple ID 的设备间同步，新设备登录网站时无需重新创建。
- <strong>Google 密码管理器 Passkey</strong>：安卓 + Chrome 原生支持，Passkey 存在 Google 账户中，跨安卓设备同步；2023 年起 Google 个人账号已支持用 Passkey 登录。
- <strong>Microsoft</strong>：Windows 11 / Edge 已支持 Passkey；微软账号、Outlook、Office 等服务陆续开放 Passkey 登录，并可在 Microsoft Authenticator 中管理。
- <strong>1Password / Bitwarden</strong>：已支持 Passkey 的创建、存储、跨平台同步，让你不受限于单一生态。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>跨设备同步是关键突破

{class="mt-1"}
早期 Passkey 的最大痛点是"绑定单台设备"——换手机就要重新创建。2023 年起 Apple、Google、Microsoft 实现了 Passkey 的云端同步：iCloud 钥匙串同步跨 Apple 设备，Google 密码管理器同步跨安卓设备。1Password 等第三方则打通了跨生态同步。这意味着 Passkey 已具备替代密码的实用性。
:::

##### 4. 如何在手机上创建和使用 Passkey

<strong>iOS（iPhone）路径：</strong>

1. 在支持 Passkey 的网站（如 Google、微软、亚马逊、eBay、PayPal）账号安全页选择"添加通行密钥 / Add passkey"。
2. 系统弹出 Face ID / Touch ID 验证窗口，通过后 Passkey 自动生成并保存到 iCloud 钥匙串。
3. 下次登录该网站时，输入用户名后选择"使用 iPhone 登录"，Face ID 一刷即可。
4. 管理入口：设置 → 密码 → 找到对应网站，可见 Passkey 条目。

<strong>安卓路径：</strong>

1. 在支持 Passkey 的网站账号安全页选择"添加通行密钥"。
2. Google 密码管理器弹窗 → 选择你的 Google 账号 → 屏幕锁验证（指纹/图案/PIN）。
3. Passkey 自动保存到 Google 密码管理器，跨同账号安卓设备同步。
4. 下次登录时，选择"使用 Passkey"，屏幕锁一解即可。
5. 管理入口：安卓设置 → 密码、密钥和自动填充 → 密码管理器 → google.com。

##### 5. Passkey 跨设备登录

如果你在 Windows 电脑上登录一个只有 iPhone 上有 Passkey 的网站，可以扫码授权：

1. 网站登录页选择"使用 Passkey"。
2. 选择"使用其他设备"。
3. 电脑显示二维码，用 iPhone 扫码。
4. iPhone 弹出 Face ID 验证，确认后网站在电脑上完成登录。

这一过程通过蓝牙+互联网双重加密通信，Passkey 私钥不会离开你的 iPhone。

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>现在就试：体验无密码登录

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 登录 Google 账号 → 安全 → 通行密钥 → 添加通行密钥，体验 Face ID/指纹登录。
2. 登录微软账号 → 安全 → 高级安全选项 → 添加通行密钥。
3. 在淘宝、京东、eBay、PayPal 等已支持 Passkey 的服务上尝鲜。
4. 保留传统密码作为后备，逐步迁移高价值账号到 Passkey。
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>过渡期建议

{class="mt-1"}
Passkey 并未完全取代密码——许多网站仍处于"Passkey + 密码"并存阶段。建议：高价值账号优先开启 Passkey，但<strong>不要立即删除传统密码</strong>，留作备用；同时继续使用密码管理器，因为不是所有网站都支持 Passkey。把 Passkey 看作"密码管理器的强力补充"而非"立刻替换"。
:::

#### 七、硬件安全密钥

如果你对安全的要求高于普通用户——比如持有大量加密货币、是高管/记者/活动人士、或保护企业核心账号——硬件安全密钥是比短信验证码更可靠的选择。

##### 1. 什么是硬件安全密钥？

硬件密钥是一个物理设备（形似 U 盘），内部安全芯片存储你的私钥，需要物理接触或 NFC 才能完成验证。代表产品：

- <strong>YubiKey</strong>（Yubico 公司）：最主流，支持 FIDO2/WebAuthn、U2F、OTP、PIV、OpenPGP，USB-C / USB-A / NFC 等多种接口。5 系列 50-70 美元。
- <strong>Google Titan</strong>：Google 自家出品，USB-C + NFC / 蓝牙，约 30-40 美元。
- <strong>OnlyKey</strong>：开源替代品，支持多种协议。
- <strong>国产替代</strong>：如飞天诚信 ePasskey，价格更亲民。

##### 2. 为什么硬件密钥比短信验证码安全？

- <strong>抗钓鱼</strong>：和 Passkey 一样，硬件密钥只对真实域名响应，钓鱼网站无法骗取验证码。
- <strong>抗 SIM 劫持</strong>：短信验证码可被 SIM-swap 攻击截获，硬件密钥无需手机号。
- <strong>抗中间人</strong>：FIDO2 协议每次签名都包含挑战值，无法重放。
- <strong>物理隔离</strong>：私钥永远在硬件芯片内，恶意软件即使攻陷你的电脑也读不到。

##### 3. 适用场景

- 加密货币交易所账号、钱包恢复。
- 企业 SSO、远程办公 VPN、SSH 登录服务器。
- 邮箱、GitHub、社交媒体等"主账号"——一旦被攻破可重置所有其他账号。
- 记者、律师、高管等高敏感人群。

##### 4. 如何配置硬件密钥作为二次验证

以 Google 账号 + YubiKey 为例：

1. 购买 YubiKey（建议一次买两把，一把日常用、一把备用，存放在不同地点）。
2. 登录 myaccount.google.com → 安全 → 两步验证。
3. 选择"添加安全密钥"→ 把 YubiKey 插入 USB-C 口或贴近手机 NFC 感应区。
4. 按提示触摸 YubiKey 金属触点完成注册。
5. 建议注册第二把备用密钥。
6. 在"两步验证"设置里，把硬件密钥设为首选验证方式，短信验证码作为备用。

主流支持的网站：Google、GitHub、Microsoft、Apple ID、Facebook、Twitter、Dropbox、GitLab、AWS、Coinbase、Binance 等。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>双密钥策略

{class="mt-1"}
硬件密钥最大的风险是"丢失"。建议：① 同时注册两把不同的密钥；② 一把随身携带（钥匙扣），一把存放在家中保险柜或银行保管箱；③ 部分网站允许把"备用恢复码"打印出来离线保存。这样即使主密钥丢失，也不会被永久锁在账号外。
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>购买渠道要谨慎

{class="mt-1"}
务必从官方店铺或授权代理购买，不要买二手或来源不明的密钥——理论上预置过的硬件可能已被植入后门。YubiKey 的固件在出厂后无法更新，但 Yubico 会持续推送安全公告，关注其官网即可。
:::

#### 八、家庭/团队密码共享

家庭场景下，Netflix、家庭 Wi-Fi、路由器后台、智能门锁密码需要全家共用；团队场景下，服务器、数据库、社交媒体账号需要多人协作。<strong>用微信发密码、写在共享文档里都是高危做法</strong>——一旦聊天记录或文档权限泄露，密码就泄露了。

##### 1. 1Password 的"共享保险库"（Vault）

1Password 是家庭和团队共享的标杆产品。它的核心机制是<strong>多个保险库</strong>：

- <strong>个人保险库</strong>：只有你能看，如银行、邮箱等私人账号。
- <strong>共享保险库</strong>：家人或团队成员都能看，如 Netflix、家庭 Wi-Fi、共享信用卡。
- <strong>权限分级</strong>：团队版可设定某些成员"只查看"或"只查看但不编辑"。

家人或团队成员无需共享主密码，各自用自己的账号登录，但可以看到被授权的共享保险库内容。密码修改后所有成员实时同步。

##### 2. Bitwarden 的"组织"功能

Bitwarden 的免费版支持个人密码共享（通过"发送 Send"功能限时分享单条密码）；付费版可创建"组织"，把若干条目共享给家庭成员或团队同事，权限可细分。Bitwarden 还提供自托管选项，适合对数据主权要求高的企业。

##### 3. 家庭场景：共享 Netflix、Wi-Fi 等密码的安全方式

- <strong>Netflix / 视频网站</strong>：用 1Password 家庭版的"共享保险库"存登录密码，家庭成员各自登录即可，无需在群里发。
- <strong>家庭 Wi-Fi 密码</strong>：iOS 设备间可通过 AirDrop 直接共享 Wi-Fi 密码给来访的客人，无需念出来；安卓 12+ 也有"附近分享 Wi-Fi"功能。
- <strong>智能门锁、智能家电</strong>：尽量用厂商 App 的"家庭成员"功能为每人单独创建账号，而不是共享一个管理员账号。
- <strong>家用路由器后台</strong>：管理员密码存到 1Password 共享保险库，访客 Wi-Fi 单独开一个 SSID。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>1Password 家庭版的性价比

{class="mt-1"}
1Password Families 约 4.99 美元/月，支持最多 5 位家庭成员，每人都有独立的私人保险库 + 4 个共享保险库。算下来人均不到 1 美元/月，是目前家庭共享体验最好的方案。Bitwarden 的家庭版 10 美元/年支持 6 人，性价比更高，但界面体验略逊。
:::

##### 4. 团队场景：服务器/数据库密码共享

- <strong>1Password Teams / Business</strong>：可按部门、项目组创建多个保险库，细粒度权限控制，所有访问行为可审计。
- <strong>Bitwarden Teams / Enterprise</strong>：开源方案，可自托管，企业版支持 SSO 集成、目录同步。
- <strong>职责分离原则</strong>：管理员密码不应只有一人掌握——设置 2-3 名"应急联系人"，确保关键人员离职/休假时业务不中断。
- <strong>离职流程</strong>：员工离职时立即撤销其密码管理器访问权限，必要时旋转所有他接触过的高敏感密码。

##### 5. 紧急访问（Emergency Access）：万一你出事

想象一个场景：你独自管理家庭所有重要账号，但意外住院或不幸离世，家人无法登录银行、邮箱、保险账号。<strong>"紧急访问"功能</strong>正是为此设计——授权一位信任的家人/朋友，在你无法响应时获取你的密码库。

<strong>Bitwarden 紧急访问设置：</strong>

1. 登录 Bitwarden Web Vault → 设置 → 紧急访问。
2. 添加信任联系人的邮箱，邀请对方接受。
3. 设定"等待期"（建议 7-14 天）：从对方发起请求到你确认的时间窗口。
4. 如果你在等待期内不响应（拒绝或不操作），到期后对方自动获得访问权。
5. 你随时可以手动拒绝请求或撤销紧急访问权限。

<strong>1Password 紧急访问：</strong>

1. 1Password 不直接叫"紧急访问"，但通过"家庭/团队组织"功能可实现——把家人加入家庭版后，将部分条目放入"共享保险库"。
2. 对个人版用户，建议把主密码告知一位高度信任的家人，或写入密封信封存放于保险柜。
3. 1Password 还提供"恢复码"，开启双重认证时务必打印保存。

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>现在就设：为家人留一把"备用钥匙"

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 选定一位信任的家人作为"紧急联系人"。
2. 在密码管理器中设置紧急访问（Bitwarden）或加入家庭共享保险库（1Password）。
3. 把主密码 + 恢复码写在纸上，封进信封，存放于家中保险柜或告知可信家人。
4. 每半年回顾一次，确认紧急联系人是否仍然合适。
:::

#### 九、密码管理器使用最佳实践

- <strong>设置强主密码</strong>：主密码是最后一道防线，务必设置一个长且复杂的密码，并牢记。
- <strong>启用双重认证</strong>：为密码管理器账号开启双重认证，增加一层保护。
- <strong>定期检查弱密码</strong>：大多数密码管理器有"安全审计"功能，帮你找出弱密码和重复密码。
- <strong>不要忘记主密码</strong>：主密码无法找回，忘记就意味着丢失所有密码。建议写在纸上，放在安全的地方。
- <strong>紧急访问</strong>：设置紧急联系人，万一你无法访问，信任的人可以获取你的密码。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>重要提醒

{class="mt-1"}
密码管理器虽然方便，但也有风险：如果主密码泄露，所有密码都暴露了。所以主密码绝对不能和其他密码相同，也不能写在容易被找到的地方。另外，建议选择有良好安全记录的服务商。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>现在就试：开始使用密码管理器

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 选择一个密码管理器（推荐Bitwarden或系统自带）。
2. 注册账号，设置一个强主密码。
3. 导入现有密码（如果有的话）或开始添加新密码。
4. 安装浏览器插件或手机App，体验自动填充功能。
5. 检查安全审计报告，找出需要改进的密码。
:::
