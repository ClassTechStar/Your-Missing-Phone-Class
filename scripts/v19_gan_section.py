# -*- coding: utf-8 -*-
"""v1.9 第十五章新增正式章节（h4）：氮化镓（GaN）电源适配器。

插入位置：h4「三、快充协议全解析」末尾的 warning-box 之后、
原 h4「四、电池新技术：硅碳负极电池」之前；原 h4 四、五顺延为五、六
（目录与侧边栏只引用章 id 与 kuichong 锚点，不引用这两个标题文字，安全）。

与既有内容的分工：
- h4 二末尾已有 info-box「GaN充电器——出差党的好搭档」，是入门科普；
  本节开头显式承接它，往下讲原理、边界与误区，不重复罗列优点。
- h4 三讲协议握手与线材，本节讲充电头硬件侧，并引用「先看协议，再谈瓦数」。
- h4 四（顺延后为五）讲电池材料，本节只讲充电链路，不碰电芯技术。
- h4 五（顺延后为六）讲省电，本节结尾明确把续航归因交还给它。

技术口径：
- 区分「宽禁带材料特性」「开关电源拓扑」「协议协商」「电池侧充电管理」四层，
  不把充电头的高频高效说成电池容量或系统功耗的改善。
- 不写具体产品型号、未核实的实测效率 / 体积 / 温度数字；标称功率、
  PD 版本这类公开标准信息按通用叫法写，具体产品以铭牌和厂商说明为准。
- 明确 GaN 热导率并不优于硅，避免「导热更好」这类常见错误。
- 明确 GaN 通常是功率开关管用 GaN HEMT，控制 IC、磁性元件、电容仍是常规器件。
"""

# 插入锚点：原 h4 四的开头
ANCHOR = '<h4 class="text-lg font-semibold mt-4 mb-2">四、电池新技术：硅碳负极电池</h4>'
MARK = '<!-- v19-gan-adapter-section -->'

# 新增正式章节后，原 h4 四、五顺延
RENUMBER = [
    (ANCHOR,
     '<h4 class="text-lg font-semibold mt-4 mb-2">五、电池新技术：硅碳负极电池</h4>'),
    ('<h4 class="text-lg font-semibold mt-4 mb-2">五、这才是真正的省电技巧</h4>',
     '<h4 class="text-lg font-semibold mt-4 mb-2">六、这才是真正的省电技巧</h4>'),
]

SECTION_HTML = '''
<h4 class="text-lg font-semibold mt-4 mb-2">四、氮化镓（GaN）适配器：充电头这边到底变了什么</h4>
<p class="mb-2">前面在讲充电习惯时提过一句：GaN 充电头是出差党的好搭档，同样的功率能做得很小。上一节又把快充协议捋了一遍，知道了「先看协议，再谈瓦数」。那这块越做越小的充电头，里面究竟换了什么？为什么换了材料就能变小、少发热？它又凭什么被反复和「快充」「续航」绑在一起说？这一节把充电头这头讲清楚。</p>
<p class="mb-2"><strong>先把位置摆正</strong>：从墙上插座到电池，中间至少隔着四段——适配器把市电变成低压直流，数据线把它送进手机，手机里的充电管理电路按协议要来的电压电流调整成电池能接受的形状，最后才是电芯把电能存进去。<strong>氮化镓只作用于第一段</strong>。它让这一段的转换更省、体积更小，但既不增加电池容量，也不减少手机耗电，更不会让屏幕、基带、SoC 少用一点电。后面会反复回到这条边界上。</p>

<h5 class="font-semibold mt-3 mb-1">1. 从硅到氮化镓：宽禁带带来的三件事</h5>
<p class="mb-2">充电器里最忙的元件是一颗<strong>开关管</strong>：它每秒几十万次地导通、关断，把直流「切」成高频脉冲，交给变压器降压。过去这颗管子基本都是硅 MOSFET，现在不少产品换成了 <strong>GaN HEMT</strong>（氮化镓高电子迁移率晶体管）。换的不是名字，是材料本身的几个物理属性：</p>
<div class="overflow-x-auto">
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">对比项</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">硅 MOSFET</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GaN HEMT</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">对充电头的意义</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">禁带宽度与耐压</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">禁带较窄，要做到同样耐压，器件得做厚、做大</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">宽禁带，击穿电场高约一个数量级</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">同样耐压下器件面积更小、导通电阻更低，导通时的发热更少</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">开关速度与寄生参数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">栅极电荷、寄生电容较大，还有体二极管带来的反向恢复损耗</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">沟道里是二维电子气，寄生电容小，基本没有体二极管的反向恢复问题</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每次开关浪费的能量少，才能把频率往上推而不至于烫手</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">高温工作能力</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">结温上限较低，温度一高就得降额</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可以在更高结温下工作，但<strong>导热能力并不比硅强</strong></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">耐热不等于散热，热量照样要靠封装、灌封材料和外壳导出去</td></tr>
</tbody>
</table>
</div>
<p class="mb-2">这里有个流传很广的误会得先拆掉：<strong>GaN 并不是「导热特别好」</strong>。论热导率，它比碳化硅低，跟硅相比也没有明显优势。它真正的好处是<strong>自己产生的热更少</strong>，并且能扛住更高的结温。所以 GaN 充电头摸起来不那么烫，是损耗降低加上散热设计共同的结果，不是材料把热量凭空变没了。</p>
<p class="mb-2">还有一处要说准：所谓「GaN 充电器」，通常只是<strong>功率开关管</strong>换成了 GaN 器件，而且多是在硅衬底上长一层氮化镓外延（GaN-on-Si），好控制成本。协议芯片、控制 IC、整流管、变压器、电容、外壳，该有的照样有，大多还是常规器件。把它理解成「整个充电头都是氮化镓做的」，就跑偏了。</p>

<h5 class="font-semibold mt-3 mb-1">2. 适配器怎么把 220V 变成手机能吃的电</h5>
<p class="mb-2">充电头学名叫<strong>开关电源适配器</strong>，走的还是那条老路，只是把每一步做得又小又快：</p>
<ol class="list-decimal pl-6 mb-3 space-y-1">
  <li><strong>整流滤波</strong>：插座里的交流电先被整流成高压直流，再由电容抹平波动。</li>
  <li><strong>高频斩波</strong>：开关管以很高频率把高压直流切成一串脉冲。频率越高，每个脉冲要传递的能量越少，变压器和滤波元件就能做越小。</li>
  <li><strong>变压器降压与隔离</strong>：高频变压器把电压降下来，同时把市电一侧和手机一侧在电气上隔开，这是安全的底线，也是安规里绝缘、爬电距离这些要求的由来。</li>
  <li><strong>次级整流与滤波</strong>：降压后的高频交流再被整成平滑直流，现在多用同步整流来降低这一段的损耗。</li>
  <li><strong>协议协商与输出</strong>：协议芯片跟手机「对上话」，按商量好的电压电流档位输出；手机要多少、什么时候要，都是手机这边说了算。</li>
</ol>
<p class="mb-2">关键就在第二步。变压器每个周期能搬多少能量，跟频率直接相关：<strong>频率提上去，磁芯和绕组就可以缩小，滤波电容也能跟着减小</strong>。这就是「高频化 → 小型化」的基本逻辑。可频率不是想提就能提——开关管每导通关断一次都要交一笔「开关损耗」，频率越高，这笔账翻得越快。硅管在高频下光是栅极充放电和反向恢复就够它热得降额，等于省下来的体积又被散热片吃了回去。</p>
<p class="mb-2">GaN 的意义正在这里：<strong>它把高频化的代价压低了</strong>。开关损耗小了，频率才能往上走；频率上去了，磁性元件和电容才敢做小；元件小了，整块板子才塞得进那个小方块。再叠上有源钳位或准谐振这类拓扑、同步整流、平面变压器、灌封导热，才凑成今天这个「巴掌大、能带笔记本」的多口充电头。少算任何一环，都解释不通。</p>
<div class="tip-box rounded-lg p-4 mb-3"><p class="font-semibold"><i class="fas fa-lightbulb mr-2"></i>一句话记牢</p><p class="mt-1">GaN 不是「让充电变快的魔法材料」，它是<strong>让开关电源敢跑更高频率</strong>的那块拼图。频率高 → 变压器电容小 → 体积小；损耗低 → 少发热 → 小体积里才装得下更大功率。两件事是同一条因果链。</p></div>

<h5 class="font-semibold mt-3 mb-1">3. 体积小、发热低、功率密度高：分别省在哪</h5>
<p class="mb-2">广告里常把这三个词并列，其实它们说的是三个不同层面的结果：</p>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>体积小</strong>：主要来自高频化后磁性元件与电容的缩小。同样输出功率，元件越小、板子越紧凑；反过来同样体积，也能塞进更高功率。</li>
  <li><strong>发热低</strong>：来自损耗降低。损耗大致分两块，导通时电阻上的损耗跟电流平方成正比，开关瞬间的损耗跟频率成正比；GaN 两头都占便宜，再加上同步整流，浪费成热的电就少了。</li>
  <li><strong>功率密度高</strong>：这是前两项合起来的比值，意思是单位体积能输出多少功率。它衡量的是<strong>充电头做得有多紧凑</strong>，跟「手机能充多快」不是一回事。</li>
  <li><strong>充电效率高</strong>：指插座取进来的电有多少真正送到了输出端。要留意宣传里的效率通常是某个中等负载下的峰值，轻载、满载、多口同时插、温度升上去以后都会变；它是个区间，不是一个全程恒定的数字。</li>
</ul>
<p class="mb-2">顺带说个反向的代价：开关波形越陡，高频噪声和电磁干扰越难收拾。频率提上去以后，布线、屏蔽、共模滤波、变压器绕法都得跟着讲究，否则可能干扰触控、无线通信，或者干脆过不了电磁兼容测试。所以<strong>高频不是免费的午餐</strong>，GaN 只是把这道门槛挪近了，跨不跨得过去仍看整体设计。这也解释了为什么同样是「GaN」，不同产品做出来体积、温升和稳定性可以差很多。</p>

<h5 class="font-semibold mt-3 mb-1">4. 标称功率、协议兼容与实际速度：三方对齐才叫快</h5>
<p class="mb-2">上一节讲过握手，这里把功率这条链接完。<strong>充电头标注的瓦数是它能提供的上限，不是插上就一定输出的数值</strong>。实际功率大致由四个环节里最短的那块板决定：</p>
<div class="overflow-x-auto">
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">环节</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">它决定什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">常见的卡点</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">适配器</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">能提供哪些电压电流档位、单口最大功率、多口怎么分配</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">只支持 PD 固定档，手机要 PPS 细调电压就对不上；插第二个设备时功率被重新分配</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数据线</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">能否扛住对应电流、能否让协议通信正常进行</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">线阻过大、线材不带能力标识、Type-C 高功率线缺少电子标记芯片</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">手机与协议</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">认不认这个协议、请求哪一档、握手失败后回落到哪一档</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">私有协议和通用协议不互通，大功率头也可能只跑常规档</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">电池与充电管理</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">此刻电芯实际能接受多大电流</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">电量、温度、电池状态、系统负载都会让手机主动降功率</td></tr>
</tbody>
</table>
</div>
<p class="mb-2">最后一行最容易被忽略。手机里的充电管理电路（电荷泵或降压电路）才是真正给电芯「喂电」的角色，它会按电池的电量与温度画一条曲线：<strong>电量低时可以放开大电流，中段开始逐步收敛，接近满电时明显放慢</strong>。所以宣传里「十几分钟充到一半」不能简单乘二推算充满时间，后半程本来就该慢。这也解释了两个常见困惑：为什么同一个 100W 的头给不同手机速度差很多，以及为什么手机发热时充电会突然变慢——不是充电头不够猛，是手机自己把闸门关小了。</p>
<p class="mb-2">多口充电头还多一层变数：每插拔一次设备，功率分配可能重新算一遍，某些口会短暂断连再握手。所以「一个头给三台设备同时满速」通常做不到，看铭牌上每口的分配规则比看总瓦数有用。</p>

<h5 class="font-semibold mt-3 mb-1">5. 效率、温控和习惯：哪些真的影响电池健康</h5>
<p class="mb-2">把「更护电池」这四个字拆开看，会发现 GaN 能帮上的忙相当有限。</p>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>转换效率影响的是墙那一端</strong>：效率高，浪费在充电头里的电少，插头不那么烫，长时间挂着也少一点无谓耗电。<strong>这部分损耗本来就没进过电池</strong>，所以省下来的是插座的电，不是电池的循环寿命。</li>
  <li><strong>手机端的发热主要来自手机内部</strong>：充电管理电路、电池内阻，再加上边充边玩时屏幕和 SoC 一起发热。这些热跟充电头用什么材料没有直接关系，倒是跟充电功率、机身散热和当时在跑什么应用关系很大。</li>
  <li><strong>高温叠加高电量，才是电芯老化最不喜欢的组合</strong>：大电流充电本身会升温，如果又长期停在满电、还捂在厚壳或被子里，老化会明显加快。前面那节讲「80% 限制」「优化电池充电」，针对的正是这个组合。</li>
  <li><strong>温控策略是双向的</strong>：手机靠温度传感器盯着电芯与机身，热了就降充电功率、暂缓后台任务、必要时暂停充电；适配器自己也有过温降额。所以「充到一半变慢」往往是保护在起作用，别急着换线换头。</li>
</ul>
<p class="mb-2">顺着这条线，习惯上的取舍就很清楚了：尽量别让手机在阳光直晒、厚壳闷着、边跑高负载应用的同时还在快充；有固定充电条件的人，开「优化充电」或 80% 上限比纠结充电头材质更有用；需要满电出门再充满，别长期插着停在 100%；线材和充电头用协议匹配、标识齐全的合规产品。至于「浅充浅放」「偶尔做一次电量校准」这类做法，按厂商给的系统说明来就行，不必自己发明仪式。</p>
<div class="warning-box rounded-lg p-4 mt-3"><p class="font-semibold"><i class="fas fa-exclamation-triangle mr-2"></i>别把两笔账算混</p><p class="mt-1">充电头省下的电，是<strong>从插座到手机</strong>这一段；续航长短，是<strong>电池容量减去手机耗电</strong>这一笔。前者再漂亮，也不会让电池多装进一毫安时。想让手机撑得久，还是得回到后面那节讲屏幕、信号、后台和电池本身的内容上去。</p></div>

<h5 class="font-semibold mt-3 mb-1">6. 过压、过流、过热：保护是怎么兜底的</h5>
<p class="mb-2">充电头小了、功率高了，安全这层反而更要讲清楚。合格的适配器里，保护是好几路并行的，动作通常是<strong>降功率、关断输出、冷却后重试</strong>，不会硬扛着继续供：</p>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>过压保护（OVP）</strong>：输出电压一旦超出约定档位就关断，防止异常电压顺着线伤到手机。协议协商失败、反馈回路出问题时靠它兜底。</li>
  <li><strong>过流与过功率保护（OCP / OPP）</strong>：电流或总功率超过设计值就限流或关断，多口设备、线材异常、端口短路时最常见。</li>
  <li><strong>短路保护（SCP）</strong>：输出端短接时立刻切断，故障排除后才恢复。</li>
  <li><strong>过温保护（OTP）</strong>：内部测温点超过阈值先降额，继续升温就停输出。这也提醒我们别把充电头捂在枕头、被褥或密闭插排盒里。</li>
  <li><strong>输入侧与绝缘</strong>：浪涌、欠压、雷击尖峰靠输入侧器件吸收；市电与低压输出之间靠变压器、绝缘胶带、板上的安全间距隔开，这是安规认证重点查的地方。</li>
  <li><strong>手机与线材这一端</strong>：手机还有输入过压过流保护、电芯过充过放与温度监控；Type-C 高功率线材靠电子标记芯片声明自己的能力，避免「小线扛大电流」。</li>
</ul>
<p class="mb-2">高频开关还带来一件事：电压电流变化更陡，电磁干扰更难压住。合格产品要靠滤波、屏蔽和布线把噪声关在壳子里，再送去按销售地的强制认证做安规与电磁兼容测试。<strong>所以买充电头看认证标志，不是看包装上印了几个 GaN 字样</strong>——认证对应的是整机的设计、用料与测试，材料只是其中一环。</p>

<h5 class="font-semibold mt-3 mb-1">7. 选购和使用：一份不踩坑的清单</h5>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>先查协议，再看瓦数</strong>：把你手上的手机、平板、笔记本列一遍，确认充电头明确支持它们要的协议（USB PD、PPS，或某家的私有协议）。协议对不上，瓦数再高也只会回落到常规档。</li>
  <li><strong>看单口输出和多口分配规则</strong>：铭牌上的总功率不等于每个口都能给满。只给一台手机充，和同时带三台设备，是两种完全不同的需求。</li>
  <li><strong>功率留余量，不必追数字</strong>：手机实际吃多少由手机决定，买远超出需求的大功率头，换来的往往只是体积和价格，不是更快的充电。真需要 GaN 的体积优势，通常是「一个头带走、还要带笔记本」的场景。</li>
  <li><strong>线材一起配齐</strong>：看电流规格、接口、长度，高功率 Type-C 线认准带电子标记芯片的产品。线是协议握手和供电链路的一部分，别在这省。</li>
  <li><strong>认认证、认标识、认质保</strong>：看销售地要求的强制认证标志（国内看 CCC），以及型号、输入输出参数、执行标准、厂名是否齐全。参数印得含糊、只有宣传语没有铭牌的，直接跳过。</li>
  <li><strong>用的时候给它留散热空间</strong>：插在通风处，别压在被子下，别和一堆大功率电器挤在劣质插排上；长期不用可以拔下来，既省一点待机电，也少一层风险。</li>
  <li><strong>异常就停</strong>：出现明显烫手、异味、异响、火花，或者手机反复断连重连，立刻停用并换掉，别想着「再试试」。</li>
</ul>
<p class="mb-2">说到底，GaN 是一次<strong>电源侧</strong>的工程进步：同样功率做得更小、更凉、更方便携带，多口场景尤其明显。它值得买，但理由应该是「方便、省地方、一个头够用」，不是「充得更快」「更护电池」「续航更久」。下一节讲硅碳负极，那才是真正动到电池容量的一步；再往后那节讲省电技巧，才是真正决定你一天要不要找插座的地方。</p>
'''
