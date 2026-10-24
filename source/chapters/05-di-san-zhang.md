---
id: di-san-zhang
num: 03
part: ji-chu-pian
nav: 第三章：让手机接上"生命线"
toc: default
kind: chapter
---

### 第三章：让手机接上"生命线"——网络

{class="chapter-intro mb-4"}
没网，智能手机就"智障"了一半。网络是现代手机的生命线，理解它、用好它、保护它，是每个手机用户的必修课。

#### 〇、联网不迷茫——分清Wi-Fi与流量的"路"与"车"

很多人的手机屏幕上方同时亮着Wi-Fi和信号图标，但对二者的本质区别却一头雾水。最经典的误区就是：<strong>连着Wi-Fi却刷不出页面</strong>——因为路由器断网了，而手机并没有自动切回流量。要彻底弄懂这个问题，我们需要建立一个"路与车"的认知模型。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-road mr-2"></i>核心比喻：路与车

{class="mt-1"}
把互联网想象成一座城市。<strong>"路"</strong>是你手机到互联网之间的通道，<strong>"车"</strong>是跑在路上的数据。Wi-Fi和流量是两条不同的路，但数据（车）本身是一样的。
:::

{class="font-semibold mt-4 mb-1"}
##### 1. 本质区别：本地通道 vs 远程高速

Wi-Fi本质上是一种<strong>局域网技术</strong>，它就像你家楼下无线铺设的路，负责把数据从路由器传到手机上。但如果宽带欠费或光缆断了，路虽然还在，外面的"高速公路"却断了，自然哪儿也去不了。而网络流量（移动数据）则是通过运营商的4G/5G基站传输，相当于你直接开上了运营商的高速专线，只要有信号就能直连互联网。

{class="font-semibold mt-4 mb-1"}
##### 2. 费用与场景：固定月租 vs 按量计费

Wi-Fi通常是一次性投入（宽带月费），只要电费不断，全家人无限使用，非常适合下载电影、打游戏等大流量场景。而流量则按使用量计费，超出套餐可能会降速或额外扣费，更适合在地铁、出差等移动场景下处理轻量级任务。

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands-helping mr-2"></i>来试试：检查你的流量套餐

{class="mt-1"}
打开手机的 [设置] > [移动网络] > [流量管理]，看看你本月还剩多少流量、哪些App最耗流量。心里有数，出门才不慌。
:::

{class="font-semibold mt-4 mb-1"}
##### 3. 安全考量：公共Wi-Fi是隐秘的"钓鱼场"

在安全性上，移动数据通常比公共Wi-Fi更安全。移动数据由运营商加密，而公共Wi-Fi确实容易被黑客搭建为"伪热点"截获未加密的流量。但这里要区分清楚：在HTTPS全面普及的今天，攻击者能截获的是<strong>你访问了哪些网站</strong>（域名），以及<strong>未加密的HTTP内容</strong>；而微信消息、银行App的登录密码等经过HTTPS加密的数据，攻击者<strong>无法直接读取</strong>——除非实施更复杂的SSL剥离攻击且用户忽略了证书警告。不过即便如此，在外进行支付操作时，直接用手机流量仍然是最稳妥的选择。

::: div .danger-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>安全提醒

{class="mt-1"}
在机场、商场、咖啡厅等公共场所，不要连接名字可疑的免费Wi-Fi（如"Free_WiFi_2024"）。即使连了，也绝不要在上面登录银行App或输入密码。
:::

{class="font-semibold mt-4 mb-1"}
##### 4. 手机端判断：看懂状态栏的"暗语"

如何知道手机此刻在用什么联网？以华为手机为例，状态栏中运营商信号旁或WLAN信号旁出现<strong>双向箭头图标</strong>，即代表正在使用对应方式上网；若两者同时亮起，则说明网络加速生效，手机正同时利用两种通道。

iPhone用户则更直观：Wi-Fi图标亮着就是在用Wi-Fi，不亮时看右上角的信号格就是在用流量。部分安卓手机还会在状态栏显示"5G"或"4G"字样，直接告诉你当前移动网络类型。

{class="text-lg font-semibold mt-6 mb-2"}
#### 一、移动网络（4G/5G）与流量

移动网络是你随时随地联网的基础。从2G到5G，速度提升了上千倍，但原理其实差不多。

##### 网络制式：

- <strong>4G LTE</strong>：目前覆盖最广，速度够用（理论上最高100Mbps+），耗电相对低。
- <strong>5G</strong>：速度快（理论上最高10Gbps），但覆盖还在完善，耗电高。适合下载大文件、看高清视频。
- <strong>5G SA vs NSA</strong>：SA是独立组网，NSA是依托4G基站。SA体验更好，但需要运营商和手机都支持。

##### 流量管理：

- <strong>流量是什么</strong>：就是手机上网产生的数据量。看视频、刷图最费流量，文字和语音相对省。
- <strong>省流小贴士</strong>：在设置里开启"省流量模式"，Wi-Fi下再更新App或看高清视频。
- <strong>信号格≠网速</strong>：信号强只代表连接好，网速还看基站忙不忙、你离基站多远。

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>重要警告：出国前关闭【数据漫游】！

{class="mt-1"}
在国外使用移动数据可能产生天价账单！出国前务必在设置里关闭数据漫游，或者提前购买当地流量卡/国际漫游套餐。
:::

#### 二、Wi-Fi：连接、分享与安全

Wi-Fi是家庭和办公室的联网主力，速度快、不费流量。但Wi-Fi其实也在不断进化，不同标准之间差异很大。

##### 连接Wi-Fi：

去 [设置] > [WLAN] 选择网络输密码。现在很多手机支持扫码连接，更方便。

##### 分享密码：

安卓和iOS都能让已连接的手机快速分享密码给朋友。安卓生成二维码，iOS可以靠近自动分享。

##### Wi-Fi标准演进：

Wi-Fi标准由IEEE制定，每一代都有显著提升：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                            <thead>
                                <tr class="bg-light dark:bg-gray-700">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">标准</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">协议</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">频段</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">最高速率</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">特点</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 4</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11n</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.4/5GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">600Mbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">老旧标准，覆盖还行</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 5</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11ac</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">5GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.5Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">目前最普及，速度够用</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 6</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11ax</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.4/5GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">9.6Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多设备性能强，延迟低</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 6E</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11ax</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.4/5/6GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">9.6Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">增加6GHz频段，不拥堵</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 7</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11be</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.4/5/6GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">46Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">极速传输，多链路聚合</td>
                                </tr>
                            </tbody>
                        </table>
```
:::

- <strong>Wi-Fi 6的关键技术</strong>：OFDMA（正交频分多址）让多个设备同时传输，MU-MIMO（多用户多入多出）提升多设备并发效率，TWT（目标唤醒时间）让设备更省电。
- <strong>Wi-Fi 6E</strong>：在Wi-Fi 6基础上增加了6GHz频段，提供更多信道，减少干扰。需要手机和路由器都支持。
- <strong>Wi-Fi 7</strong>：引入MLO（多链路操作），可同时使用多个频段传输数据，大幅降低延迟。320MHz超宽信道让速率飞跃。骁龙8 Elite Gen5、天玑9400等旗舰芯片平台均已支持Wi-Fi 7，小米17、华为Mate 80、三星S26等机型可使用Wi-Fi 7网络（需配合Wi-Fi 7路由器）。
- <strong>2.4GHz vs 5GHz</strong>：2.4GHz穿墙好但速度慢、干扰多；5GHz速度快但穿墙弱。Wi-Fi 6E/7的6GHz频段速度最快，但穿墙最弱，适合同一房间内使用。

##### 公共Wi-Fi风险：

公共Wi-Fi可能有黑客窃听数据或设钓鱼热点。守则：

- 避免登录银行账户、输入密码。
- 最好用VPN加密连接。
- 不要自动连接陌生Wi-Fi。
- 用HTTPS网站（地址栏有锁图标）。

#### 三、蓝牙：短距离无线通信的万能选手

蓝牙可能是你手机上使用频率最高的无线技术之一——无线耳机、智能手表、车载系统、键盘鼠标，都靠它连接。

##### 技术原理：

蓝牙工作在2.4GHz ISM频段，使用跳频扩频技术（FHSS）将数据分散在79个频道上快速切换传输，有效避免干扰。蓝牙的通信距离分为三个等级：Class 1约100米、Class 2约10米（手机常用）、Class 3约1米。

##### 版本演进：

- <strong>蓝牙4.0</strong>：引入低功耗蓝牙（BLE），让手环、心率带这类小电池设备也能无线连接，续航从天变成月。
- <strong>蓝牙4.2</strong>：提升传输速度和隐私保护，支持IPv6直连。
- <strong>蓝牙5.0</strong>：传输速度翻倍（2Mbps），传输距离4倍（理论300米），广播能力8倍。支持双音频（同时连两副耳机）。
- <strong>蓝牙5.1</strong>：引入方向寻址功能（AoA/AoD），定位精度可达厘米级。
- <strong>蓝牙5.2</strong>：LE Audio新标准，支持LC3编码（音质更好、功耗更低）、多流音频、广播音频。
- <strong>蓝牙5.3/5.4</strong>：进一步优化功耗和连接稳定性，增强周期性广播。

<strong>LE Audio普及情况</strong>：2025-2026年，LE Audio已进入快速普及阶段。主流品牌的新款真无线耳机（如华为FreeBuds Pro 5、小米Buds 6 Pro、三星Galaxy Buds3 Pro等）均已支持LE Audio和LC3编码，提供更低延迟和更好音质。购买新耳机时，建议优先选择支持LE Audio的产品。

##### 应用场景：

- <strong>音频传输</strong>：无线耳机、车载音响。蓝牙5.2的LE Audio让音质和延迟都有质的飞跃。
- <strong>数据传输</strong>：近距离传文件、照片。虽然速度不如Wi-Fi Direct，但胜在简单。
- <strong>设备配对</strong>：智能手表、手环、键盘鼠标、游戏手柄。
- <strong>位置服务</strong>：蓝牙信标（Beacon）用于室内导航、物品追踪（如苹果AirTag）。
- <strong>智能家居</strong>：蓝牙Mesh网络控制灯泡、门锁等。

#### 四、红外遥控：手机变身万能遥控器

红外遥控是最古老的无线控制技术之一，但在手机上依然实用。部分安卓手机（如小米、华为部分机型）内置了红外发射器，可以遥控电视、空调、机顶盒等家电。

##### 工作原理：

红外遥控通过红外发光二极管发出特定频率（通常38kHz）的红外光脉冲信号，家电的红外接收器解码这些脉冲执行对应操作。不同品牌使用不同的编码协议，常见的有NEC、RC5、RC6、SONY等。手机里的红外App内置了各品牌的编码库，选择品牌和型号就能匹配。

##### 局限性：

- <strong>方向性</strong>：红外是直线传播，需要对着设备发射，不能隔墙。
- <strong>距离短</strong>：有效距离一般5-8米。
- <strong>苹果不支持</strong>：iPhone没有红外发射器，无法使用此功能。

#### 五、NFC：碰一碰的魔法

NFC（Near Field Communication，近场通信）是一种极短距离（10厘米以内）的高频无线通信技术，工作频率13.56MHz，传输速率最高424Kbps。

##### 通信原理与模式：

NFC基于RFID技术演变而来，支持三种工作模式：

- <strong>读写模式</strong>：手机读取NFC标签中的信息，如读取NFC贴纸触发动作。
- <strong>点对点模式</strong>：两台NFC设备互相传输数据，如Android Beam（已停用）。
- <strong>卡模拟模式</strong>：手机模拟一张智能卡，这是最常用的模式——公交卡、门禁卡、银行卡都是这个模式。

##### 安全机制：

- <strong>超短距离</strong>：10厘米内的通信距离本身就是物理安全保障，远程窃听几乎不可能。
- <strong>安全芯片</strong>：手机内置独立的安全芯片（SE）或使用HCE（主机卡模拟），支付密钥存储在安全区域，即使手机被root也无法提取。
- <strong>指纹/面容验证</strong>：支付时需要生物识别确认，即使手机丢失也无法盗刷。
- <strong>令牌化</strong>：Apple Pay、华为Pay等不传输真实卡号，而是使用一次性令牌，即使被截获也无法重复使用。

##### 典型应用：

- <strong>公交卡/门禁卡</strong>：把实体卡信息写入手机，刷手机就行。
- <strong>移动支付</strong>：Apple Pay、华为Pay等，把银行卡绑定到手机，碰一碰支付。
- <strong>设备配对</strong>：NFC碰一碰快速配对蓝牙耳机、音箱。
- <strong>身份验证</strong>：NFC身份证读取、电子驾照验证。

#### 六、个人热点：把手机变Wi-Fi路由器

自己流量多时，可以开热点给平板、电脑用。

- <strong>开启方法</strong>：设置 > 个人热点/网络共享，开启它。
- <strong>注意事项</strong>：很耗电和流量，记得设个复杂密码，并限制连接设备数。
- <strong>USB共享</strong>：用数据线连电脑，比无线热点更稳定、更快。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>动手试试：设置并管理热点

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 打开 [设置]，找到"个人热点"或"网络共享"，开启它，设好名称和密码。
2. 用另一台设备（比如电脑）搜索并连接这个Wi-Fi。
3. 在手机端看看，能不能管理已连接的设备，或踢掉不认识的设备。
:::
