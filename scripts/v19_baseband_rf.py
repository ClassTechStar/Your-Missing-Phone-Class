# -*- coding: utf-8 -*-
"""v1.9 第一章「六、基带与天线」补充：蜂窝基带 / 射频前端 / 集成外挂 / SA-NSA / Wi-Fi 蓝牙。

插入位置：该节现有 4 个 h5（基带芯片 / 天线设计 / 网络技术演进 / 网络频段分类）
之后、h4「七、你的手机，到底在扮演多少角色？」之前。

沿用该节写法：h5 短标题带冒号、p.mb-2、ul + <strong>关键词</strong>：、
overflow-x-auto 表格、tip-box。不改动既有内容。

技术口径：
- 严格区分「基带（数字）」与「射频前端（高频模拟）」；
- SA/NSA 是网络侧组网架构，不是手机频段或硬件规格；
- 不写具体芯片型号、频段号之外的实测数字、未核实的机型；
- 区分通用架构规律与具体产品实现。
"""

SECTION_HTML = '''
<h5 class="font-semibold mt-3 mb-1">蜂窝基带（BP）到底管什么：</h5>
<p class="mb-2">前面说"基带把数字信号调制成无线电波"，这句为了方便理解做了简化。真拆开看，<strong>BP（Baseband Processor，基带处理器）只管数字这一半</strong>：它产出的是一串比特或基带样值，并不直接把电波送出去。把比特变成电磁波，是后面射频前端的活。</p>
<p class="mb-2">BP 的活分两类。一类是<strong>把数据搬过无线信道</strong>：发送时做信道编码、加校验、调制、成帧，让数据扛得住干扰和衰落；接收时反过来做同步、信道估计、均衡、解调、解码，出错的还要靠重传合并补回来。另一类是<strong>守着空口的规矩</strong>：小区搜索与注册、切换、功率控制、重传、加密与鉴权，全都对时间极敏感——晚几毫秒，基站那边这一帧就过去了。</p>
<p class="mb-2">所以它内部大致是这么一套零件：</p>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>实时处理器子系统</strong>：一颗或多颗 DSP 加控制核心，跑自己的实时操作系统。它不跑安卓、也不跑你的 App，只伺候空口那些按时辰办事的任务。</li>
  <li><strong>调制解调硬件</strong>：OFDM 的调制与解调、快速傅里叶变换、信道估计与均衡、多路天线的信号分离。这些运算规律固定、量大，做成专用电路比让通用 CPU 算省得多。</li>
  <li><strong>信道编解码与重传</strong>：不同代际用的编码方案不一样，但思路一致——加冗余、检错、错了请求重传并和旧数据合并。信号越差，这部分越忙。</li>
  <li><strong>协议栈加速与定时</strong>：把数据切段、排序、加解密、压包头、守住收发时刻，都要按协议精确到时隙。</li>
  <li><strong>三类接口</strong>：往上是与<strong>应用处理器（AP）</strong>的高速链路（片内总线或高速串行接口），往旁边是与<strong>射频前端</strong>的数字接口，还有一路连到 <strong>USIM 卡</strong>做鉴权。</li>
  <li><strong>功耗状态管理</strong>：没有数据时让接收机按节奏短暂醒来听一下寻呼，其余时间睡过去——手机待机能撑一整天，很靠这套机制。</li>
</ul>
<p class="mb-2">和 AP 的分工值得单独说一句：应用处理器跑操作系统、界面和网络上层协议，基带跑确定性最强的空口部分，两边各跑各的系统。<strong>AP 睡着的时候 BP 还醒着</strong>，继续守着寻呼、注册和小区切换——这就是为什么关屏一整夜，早上仍能立刻收到消息。参数表上写的"基带型号"，指的就是这颗；它既不是 SoC 里的 CPU/GPU/NPU，也不是射频前端。</p>

<h5 class="font-semibold mt-3 mb-1">从数字到电波：基带、射频前端与天线怎么接力：</h5>
<p class="mb-2">把一次"发出去"和一次"收进来"连起来看，整条链就清楚了。</p>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>发送</strong>：BP 编好码、调好制 → 数模转换或数字射频接口 → 收发机把信号搬到射频频率 → 功率放大器（PA）把功率提到能传出去 → 滤波器与双工器挑干净该发的频段 → 天线调谐匹配 → 天线辐射出去。</li>
  <li><strong>接收</strong>：天线感应到微弱信号 → 滤波 → 低噪声放大器（LNA）先放大而不引入太多噪声 → 下变频搬回低频 → 模数转换 → 回到 BP 做同步、均衡与解调。</li>
  <li><strong>闭环控制</strong>：BP 不只递数据，还一刻不停地调 PA 的发射功率、接收增益、滤波器与天线调谐。信号好就把功率收小省电，信号差就往上抬——这几条控制线是整条链路的"神经"。</li>
</ul>
<p class="mb-2">为什么非要分成数字和射频两段？两个很实在的理由：空口的时序细到毫秒以下，交给通用操作系统调度根本来不及，得有独立的实时处理器；而射频是模拟电路，工艺、供电和抗干扰的要求跟数字逻辑完全不同，往往单独做、也常常单独封装。<strong>基带管"算什么"，射频前端管"怎么把这段信号送上天"</strong>，中间靠那组控制信号把它们缝成一条闭环。</p>
<p class="mb-2">手机上的几个日常现象，顺着这条链就讲得通：在电梯或地下车库，PA 得把功率拉满，于是发热、掉电都变快；手握姿势挡住某根天线，调谐与多天线选路要重新调整；金属边框必须留出天线带，否则等于给信号盖了层盖子。所以"信号差更费电"不是错觉，是发射链路在替你使劲。</p>

<h5 class="font-semibold mt-3 mb-1">集成基带与外挂基带：</h5>
<p class="mb-2">基带和 AP 是做在同一颗芯片里，还是各做各的，是整机设计里一个很实际的取舍。两种方案长期并存，谈不上谁更先进。</p>
<div class="overflow-x-auto">
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">对比项</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">集成基带（与 AP 同一颗 SoC / 同封装）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">外挂基带（独立芯片）</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">结构</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">共用片内互连、内存与电源管理，AP 与 BP 之间走片内通路</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">两颗芯片通过高速接口相连，各自带自己的内存与供电</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">功耗与面积</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">省掉片间往返，功耗与占板面积都更省</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多一次数据搬运，多一颗芯片的位置、供电与散热</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">协同与调度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">电源状态、唤醒、数据通路容易一起管，延迟小</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">要额外维护两端的状态同步与接口协议</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">工艺取舍</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">得迁就同一套工艺，模拟/射频部分未必用得上最合适的制程</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数字与射频可以各自选更合适的工艺单独迭代</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">版本与迭代</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">换通信能力往往要换整颗 SoC，按地区做频段版本不灵活</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AP 与基带可自由组合，便于按市场做不同版本、单独升级</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">适用场景</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">走量的主流机型，优先轻薄、续航与成本</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">要覆盖多地区多频段、自研基带过渡期、或对射频布局要求高的机型</td></tr>
</tbody>
</table>
</div>
<p class="mb-2">一句话收住：<strong>集成赢在省，外挂赢在活</strong>。省的是电、面积和成本，活的是组合、版本与迭代。看到某款机器用哪种方案，别急着下"先进/落后"的结论，先看它要覆盖哪些市场、机身留了多少空间、这一代是不是正处在切换期。</p>

<h5 class="font-semibold mt-3 mb-1">SA 与 NSA：两种 5G 组网：</h5>
<p class="mb-2">先厘清一件事：SA 和 NSA 说的是<strong>运营商那张网怎么搭</strong>，不是手机的频段，也不是"支不支持 5G"的开关。手机要能用，得在基带的协议栈里支持对应模式；但决定你连到哪种网的，是基站和核心网。</p>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>NSA（非独立组网）</strong>：5G 基站负责接入，但控制面仍锚在<strong>4G 核心网</strong>上，还要 4G 基站当锚点。手机同时连着 4G 和 5G（双连接），注册、切换这类信令走 4G，用户数据可以走 5G 那条快路。好处是能借现成的 4G 网快速铺开、早期覆盖好；代价是高级能力受 4G 核心网限制，两路射频同时工作也更容易费电。</li>
  <li><strong>SA（独立组网）</strong>：5G 基站配 <strong>5G 核心网</strong>，控制面和用户面都走 5G，不再依赖 4G。低时延、网络切片、边缘计算、海量连接这些"完整 5G 能力"要靠它才发挥得出来；代价是核心网得新建，覆盖要一点点铺，早期不如 4G 兜底稳。</li>
</ul>
<div class="overflow-x-auto">
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">对比项</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">NSA</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">SA</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">核心网</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">沿用 4G 核心网</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新建 5G 核心网</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">是否依赖 4G</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">要，4G 当锚点</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不需要</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">手机连接方式</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">4G 与 5G 双连接</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">只连 5G 一套</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">时延与高级能力</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">受 4G 核心网限制</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">支持低时延、切片、边缘计算</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">建网与覆盖</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">快、早期覆盖好</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">投入大、覆盖逐步铺开</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">对手机的影响</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">要支持双连接，两路射频同时工作更耗电</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">要支持 5G 核心网流程；覆盖不足时回落到其它网络</td></tr>
</tbody>
</table>
</div>
<p class="mb-2">两个常见混淆值得点破：<strong>SA/NSA 不等于 Sub-6 与毫米波</strong>——后者说的是频段，前者说的是网络架构，两件事可以任意组合；也<strong>不等于"手机支不支持 5G"</strong>，同一部手机两种模式都能支持，实际连上哪种取决于当地网络。上一小节讲的 4G、5G、5G-A 是代际，这一小节讲的是每一代里网络怎么搭，别叠在一起记。</p>

<h5 class="font-semibold mt-3 mb-1">Wi-Fi 与蓝牙基带：</h5>
<p class="mb-2">同一部手机里还跑着另外两套"基带"，它们和蜂窝基带是完全不同的系统：用的是非授权频谱，不需要 SIM 卡，也不连运营商核心网，覆盖从几米到几十米，发射功率低得多，而且更多由应用处理器上的操作系统直接管。</p>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>Wi-Fi</strong>：物理层同样用 OFDM，和蜂窝技术有亲缘，但接入方式根本不同——没有基站统一排时隙，大家靠<strong>竞争信道</strong>（先听有没有人在发，空了再发，撞了就退避重来）。多天线、波束成形、信道选择与漫游、加密都在协议栈里。它追求的是短距离内的高吞吐，代价是设备一多、距离一远，竞争和干扰就会把速度拉下来。</li>
  <li><strong>蓝牙</strong>：靠<strong>跳频</strong>在拥挤的 2.4GHz 里躲干扰，设备组成一个小小的微微网，双方约好"连接事件"，其余时间睡过去。经典蓝牙偏向持续音频，BLE（低功耗蓝牙）把"睡很久、醒很短"做到极致，一颗纽扣电池能撑几年——耳机、手表、手柄、防丢标签、靠近解锁，都是它。</li>
  <li><strong>工程上的现实</strong>：Wi-Fi、蓝牙（有时还有 FM 与定位接收）常合在一颗<strong>连接芯片</strong>里，与蜂窝基带并行工作、各跑各的协议栈。但 2.4GHz 与部分蜂窝频段挨得近，同时收发会互相干扰，需要<strong>共存仲裁</strong>在时间和频率上错开——开热点时蓝牙耳机偶有卡顿，多半就是这套协调在打架。</li>
</ul>
<div class="overflow-x-auto">
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">对比项</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">蜂窝基带</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Wi-Fi / 蓝牙基带</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">频谱</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">授权频段，运营商规划</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">非授权频段，大家共用</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">谁调度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">基站集中分配时隙与资源</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">竞争接入 / 双方约定连接事件</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">身份与鉴权</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">USIM 与运营商核心网</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">本地配对与密码，不经运营商</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">覆盖与功率</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">公里级，发射功率高、随信号强弱大幅调整</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">十米级，功率低，BLE 尤其省</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">典型任务</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">通话、移动数据、短信、漫游</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">上网、投屏、耳机、手表、周边配件</td></tr>
</tbody>
</table>
</div>
<p class="mb-2">把这一节收成一句判断法：以后看到"信号不好"，别只盯着那几格——先问是<strong>哪张网</strong>（SA 还是 NSA、覆盖够不够），再问<strong>哪个频段</strong>，最后才看<strong>基带与射频前端这一条链</strong>有没有被握姿、金属边框或弱场拖住。频段、组网、基带、射频前端是四件不同的事，分开想，问题就好定位了。</p>
'''

ANCHOR = '<h4 class="text-lg font-semibold mt-4 mb-2">七、你的手机，到底在扮演多少角色？</h4>'
MARK = '<!-- v19-baseband-rf-section -->'
