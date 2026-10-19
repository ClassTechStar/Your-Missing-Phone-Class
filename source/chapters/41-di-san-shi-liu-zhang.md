---
id: di-san-shi-liu-zhang
num: 36
nav: 第三十六章：手机与智能家居——让家变聪明
toc: default
kind: chapter
after_part: er-tong-pian
---

### 第三十六章：手机与智能家居——让家变聪明

{class="chapter-intro mb-4"}
手机还能干一件越来越重要的事——当整个家的"遥控器"。从一盏灯、一个插座到一把门锁，智能家居正在从"极客玩具"变成"家常配置"。这一章帮你理清协议、生态、中枢和入门套件，再用一份安全清单收尾，让你不被"智能"反噬。

#### 一、智能家居协议：选谁很重要

买智能设备前先看它支持什么协议，这决定了它能不能被你的手机和生态"使唤"。目前主流协议有四种，各自的脾气如下：

- <strong>Matter协议</strong>：2022年由CSA（连接标准联盟）发布，背后是苹果、谷歌、亚马逊、三星等巨头联手。它的目标只有一个——让所有品牌的智能设备说同一种语言。2023-2026年正快速成为统一标准，支持它的设备可同时接入Apple HomeKit、Google Home、Amazon Alexa和米家，不再被单一生态绑架。
- <strong>Thread协议</strong>：Matter的底层网络"管道"。低功耗、自组网（某个节点断电，信号会自动绕路），响应快、不卡顿。买带Thread边界路由器的设备（如HomePod mini、Apple TV 4K、小米中枢网关），体验明显更稳。
- <strong>Wi-Fi</strong>：带宽大、能直连路由器，但功耗高、设备多了易挤占信道，适合摄像头、扫地机这类需要传大数据的设备。
- <strong>蓝牙（BLE）</strong>：配网简单、省电，但距离短、不能自组网，适合门锁、温湿度计这类小数据设备。
- <strong>Zigbee</strong>：老牌低功耗自组网协议，需要专用网关，设备便宜稳定，但跨品牌互通差，正被Matter+Thread逐步替代。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-circle-info mr-2"></i>一句话原则

{class="mt-1"}
2026年买智能设备，优先看是否有"Matter over Thread"标识——这是当下最经得起时间检验的选择。老设备若只支持Wi-Fi或蓝牙也不必急着淘汰，先用着，新购时再转向Matter。
:::

#### 二、三大生态对比

协议是"语言"，生态是"圈子"。即使都支持Matter，你日常仍要选一个主生态来搭自动化和语音控制。三大主流生态对比如下：

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                    <thead>
                        <tr class="bg-light dark:bg-gray-700">
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">生态</th>
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">优势</th>
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">短板</th>
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">适用人群</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple HomeKit</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">隐私最强（本地处理为主）、与iPhone/Siri/快捷指令联动顺滑</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">设备偏少偏贵、需要HomePod或Apple TV做中枢</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全家苹果设备、重视隐私与体验的用户</td>
                        </tr>
                        <tr>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">米家（小米）</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">设备最丰富、性价比最高、小爱同学好用</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">生态相对封闭、数据多上云、广告偏多</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">预算有限、想一站式配齐全屋的入门用户</td>
                        </tr>
                        <tr>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">华为智联（鸿蒙）</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">与鸿蒙手机/平板/手表无缝流转、设备数量快速增长</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">海外设备支持少、生态仍在追赶</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">华为手机用户、看重"超级终端"多设备协同</td>
                        </tr>
                    </tbody>
                </table>
```

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-circle-info mr-2"></i>选生态的决策建议

{class="mt-1"}
看手机选生态：iPhone用户优先HomeKit，华为用户优先智联，其他安卓用户米家最省心。靠Matter协议，不同生态的设备也能被同一部手机控制，不必一次性"站队"。
:::

#### 三、手机当家居中枢

在多数入门场景里，手机就是你的"家居中枢"——通过App控制灯光、空调、窗帘、安防，还能搭建自动化场景，让家"自己动起来"：

```html
<ul class="list-disc pl-6 mb-3 space-y-1">
                    <li><strong>设备控制</strong>：打开HomeKit/米家/智慧生活App，可远程或本地开关灯、调色温、设定空调温度、拉合窗帘、查看摄像头画面。</li>
                    <li><strong>自动化场景</strong>：把"条件→动作"组合起来，常用的三大场景：
                        <ul class="list-disc pl-6 mt-1">
                            <li><strong>回家模式</strong>：定位到家+天黑→开玄关灯+开空调+拉窗帘+关门锁。</li>
                            <li><strong>离家模式</strong>：最后一个出门（定位离家或门锁上锁）→关灯+关空调+关插座+启动摄像头+布防。</li>
                            <li><strong>睡眠模式</strong>：每晚23:00→关全屋主灯+拉窗帘+空调切26度+开夜灯。</li>
                        </ul>
                    </li>
                    <li><strong>NFC碰一碰</strong>：在门贴一张NFC标签，手机一碰即触发对应场景（碰一下开门灯、再碰一下切睡眠）。iPhone用"快捷指令"自动化，安卓用"钱包"或厂商App均可写入。</li>
                </ul>
```

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来试试：搭一个"回家模式"

{class="mt-1"}
在手机智能家居App的"自动化"里新建一条：触发条件选"到达某地点"（家），动作依次加"开玄关灯""空调设26度""窗帘关闭"。保存后出门逛一圈，回家时看它是否自己亮灯——第一次成功的成就感，比下单新设备还过瘾。
:::

#### 四、入门套件推荐

不必一次配齐，从这四件套开始，就能覆盖八成日常需求：

- <strong>智能音箱</strong>：小爱同学（米家生态，性价比高）/ HomePod mini（苹果生态，兼作Thread中枢）/ Alexa（海外生态广）。<em>注意</em>：音箱决定了你的语音生态，先定生态再买音箱。
- <strong>智能灯泡</strong>：Yeelight（米家/Matter，色温亮度可调，便宜）/ Philips Hue（色彩好、稳定，但需Hue网关，偏贵）。<em>注意</em>：买前确认灯座口径（E27/B22）和是否需要调色。
- <strong>智能插座</strong>：小米智能插座（便宜、电量统计）/ TP-Link Kasa（海外Matter支持好）。<em>注意</em>：用在大功率电器（热水器、电暖器）时务必看额定功率，别过载。
- <strong>智能门锁</strong>：鹿客/小米（性价比、米家联动）/ 凯迪仕（传统锁具大厂、机械结构扎实）。<em>注意</em>：确认是否支持Matter或你所在生态，留意电池续航和应急钥匙孔位置。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-circle-info mr-2"></i>选购顺序建议

{class="mt-1"}
先买智能音箱（定生态）→ 再买智能灯泡和插座（低门槛、立刻有反馈）→ 最后买门锁和摄像头（涉及安全，谨慎选）。一次只加一类设备，熟悉后再扩，避免"买回来不会用"。
:::

#### 五、安全注意事项

智能设备越多的家，攻击面也越大。下面四条是底线，请逐条对照：

1. <strong>改默认密码</strong>：摄像头、路由器、门锁出厂默认密码在网上全是公开的，买到手第一件事就是改成"长且不重复"的强密码。
2. <strong>及时更新固件</strong>：厂商推送的固件往往修复了安全漏洞，在App里开启"自动更新"，或至少每月手动检查一次。
3. <strong>网络隔离</strong>：把IoT设备单独放到一个Wi-Fi（或访客网络）上，和手机、电脑的主网络分开。万一某个设备被攻破，也难以横向威胁你的重要数据。
4. <strong>隐私保护</strong>：摄像头开启"隐私区域"遮蔽（如卧室、卫生间不拍），关闭云端24小时录像；不在家的摄像头画面别长期开给第三方App。

::: div .danger-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>这几个坑别踩

{class="list-disc pl-6 mt-1 space-y-1"}
- 别用门锁的"远程开锁"功能给陌生人——优先用临时密码，用完即失效。
- 别把摄像头直接对着床、对着窗外——泄露的是你自己的隐私。
- 别图便宜买"白牌"无品牌设备——多半不更新固件，等于给家里安了个后门。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1" aria-hidden="true"></i>本章小结

{class="list-disc pl-5 text-sm space-y-0.5"}
- Matter+Thread是2023-2026年的统一方向，买新设备优先看这个标识
- 三大生态各有所长：苹果重隐私体验、米家重性价比、华为重多设备协同
- 手机可当中枢，搭好"回家/离家/睡眠"三大场景，家就能自己动起来
- 入门四件套：智能音箱、灯泡、插座、门锁，按这个顺序逐步添置
- 改默认密码、更新固件、网络隔离、隐私遮蔽——四条安全底线不能省
:::
