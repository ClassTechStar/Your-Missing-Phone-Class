# -*- coding: utf-8 -*-
"""v1.9 第一章「6. 摄像头」补充：CMOS 图像传感器。

插入位置：原有「像素数不是全部！」段之后、「潜望式长焦镜头」之前。
沿用该节 h5 短标题（不带编号/冒号）的写法。

与第十一章附「传感器尺寸与像素大小的权衡」分工：
  那里讲底大小与四合一/九合一的取舍，本节讲成像原理、结构演进、
  六个参数的物理含义、堆栈式与读出速度、误区辨析，并显式引用那一节，
  避免重复。

技术口径：
- 严格区分「传感器采集能力」与「最终成片」，反复点明成片链条；
- 不写具体机型、未核实的实测数值；规格名用行业通用叫法；
- 「1 英寸」说明是历史标称，不等于 25.4mm 对角线；
- ISO 是增益不是感光度；HDR 合成不等于单帧动态范围；
- 堆栈式主要提升读出速度，不等于单帧画质更好。
"""

SECTION_HTML = '''
<h5 class="font-semibold mt-3 mb-1">CMOS 传感器：光是怎么变成数字的</h5>
<p class="mb-2">刚才说"像素数不是全部"，那到底什么在决定画质？咱们先把镜头后面的那块硅片讲清楚。<strong>CMOS 图像传感器</strong>就是手机的眼睛，它的活是把照进来的光，老老实实变成一串数字——注意，只是数字，还不是你看到的照片。</p>
<p class="mb-2">一个像素里发生的事其实很朴素：<strong>光电效应</strong>。光子打进硅里的光电二极管，激发出电子；曝光这段时间里，电子一点点攒在一个叫"势阱"的小坑里，光越强攒得越多。曝光结束，电荷被转成电压，经像素里的放大器读出，再由模数转换器变成数字。于是每个像素交出一个数：这一格有多亮。</p>
<p class="mb-2">但这中间还有两道容易被忽略的机关：</p>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>微透镜</strong>：盖在每个像素顶上的微型透镜，把斜着射进来的光拢到感光区里。没有它，边缘像素的光会大量打在电路上白白浪费。</li>
  <li><strong>彩色滤光片阵列</strong>：像素本身分不清颜色，只数光子。所以每个像素上面盖一片红、绿或蓝的滤色片，最常见的排法是 Bayer 阵列（绿多、红蓝少，因为人眼对绿更敏感）。<strong>也就是说，传感器原始输出是一堆各自只有一种颜色的亮度值</strong>，得靠后面的 ISP 做去马赛克插值，才拼出全彩画面。</li>
</ul>
<p class="mb-2">把这条链连起来看：光 → 微透镜 → 滤色片 → 光电二极管攒电荷 → 读出与模数转换 → 一串单色数字 → <strong>ISP 做去马赛克、白平衡、降噪、色调映射、多帧合成</strong> → 才是一张能看的照片。前面那一半是 CMOS 的本分，后面那一半是 ISP 与算法的本事。这也是为什么参数表一样的两台手机，拍出来可能完全不像——从滤色片、读出噪声到 ISP 调校，每一步都可能不一样。</p>
<p class="mb-2">顺带说一句历史：早年相机常用 CCD，电荷要一行行搬到芯片边缘统一读出，画质不错但费电、集成度低；CMOS 能在每个像素旁边就放下放大和读出电路，功耗低、能随机读取、还能把其它电路一起做进芯片，于是手机这个又小又怕热的地方，最后全成了 CMOS 的天下。</p>

<h5 class="font-semibold mt-3 mb-1">从像素到芯片：结构与技术演进</h5>
<p class="mb-2">把一个像素放大了看，它不只是个感光点，里面还有几颗晶体管负责复位、放大、选择和读出（常见的叫四晶体管像素）。像素阵列下面是行选、列读出与模数转换器组成的读出电路。过去几十年手机传感器的演进，基本就是<strong>想尽办法让光多进一点、让电少绕一点、让数读得快一点</strong>。</p>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>前照式（FSI）</strong>：金属布线走在感光区上方，光得先穿过线路层才能到达光电二极管。线路挡光、斜射光还容易被遮，开口率上不去。</li>
  <li><strong>背照式（BSI）</strong>：把晶圆翻过来从背面进光，布线挪到感光区下面。挡路的东西没了，进光效率和边缘画质都明显改善，弱光表现跟着上来。今天手机传感器基本都是背照起步。</li>
  <li><strong>堆栈式（Stacked）</strong>：再往前一步，把"感光那一层"和"逻辑电路那一层"分开做、再键合叠在一起。像素层可以专心留给光，逻辑层腾出面积放更多更快的模数转换器、缓存甚至一部分预处理电路。它换来的主要是<strong>速度</strong>——更高的连拍与视频帧率、更短的多帧合成窗口。</li>
  <li><strong>再往细处走</strong>：列级或像素级模数转换缩短读出路径；双转换增益（DCG）按明暗切换放大方式，兼顾暗处噪声与亮处不过曝；横向溢出积分电容（LOFIC）一类做法给像素多准备一个"接溢出电荷的大容器"，把高光撑住；把一个像素拆成两个光电二极管做相位检测（QPD 一类），让对焦直接在传感器上完成。名字很多，方向就三个：多收光、别溢出、读得快、对得准。</li>
</ul>
<div class="tip-box rounded-lg p-4 mb-3"><p class="font-semibold"><i class="fas fa-lightbulb mr-2"></i>一句话记牢</p><p class="mt-1">背照式解决的是"光进得来吗"，堆栈式解决的是"数读得出来吗"。前者主要帮画质，后者主要帮速度。把堆栈式当成"画质升级"是常见的误读，后面讲误区时还会再说一次。</p></div>

<h5 class="font-semibold mt-3 mb-1">六个关键参数，各自管什么</h5>
<p class="mb-2">参数表上那一串数字，其实各自回答一个不同的问题。分开看，就不容易被某一项牵着走。</p>
<div class="overflow-x-auto">
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">参数</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">物理上在说什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">主要影响</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">容易被忽略的代价</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">传感器尺寸</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">整块硅片能接收多少光</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">信噪比、动态范围潜力、浅景深</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">模组更厚、镜头更难做、边缘像差与暗角难控、成本高</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">像素尺寸</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">单个像素的面积，决定能攒多少电子（满阱容量）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">单像素信噪比、暗部干净程度、单帧动态范围</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">同一块底上像素越大，分辨率就越低</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分辨率</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一共分了多少格来记录画面</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">光线充足时的细节上限、裁切余地</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">受镜头解析力、对焦、衍射、处理与存储限制；弱光下反要靠合并</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">动态范围</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最亮不溢出与最暗不被噪声淹没之间的跨度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">大光比场景里高光与暗部能否同时留住</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">手机里看到的 HDR 多是<strong>多帧合成</strong>，不等于传感器单帧能力</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">感光能力</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">量子效率、开口率、微透镜与滤色片透过率共同决定</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">暗光下能攒到多少有用信号</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><strong>ISO 是增益不是感光度</strong>，调高它不增加光子，只把信号连噪声一起放大</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">读出速度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">整幅画面从传感器搬出来要多久</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">连拍、视频帧率、卷帘畸变、多帧合成的时间窗口</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">手机大多逐行读出的卷帘快门；真正的全局快门成本高，手机上少见</td></tr>
</tbody>
</table>
</div>
<p class="mb-2">有个坑值得单独点出来：行业里说的"1/1.3 英寸""1 英寸"是<strong>沿用了早期摄像管的标称规格，并不等于实际对角线是 25.4 毫米</strong>。它更像一个型号名，用来横向比较同一套标称体系里的大小是可以的，别拿尺子去换算。</p>
<p class="mb-2">这几项之间还互相牵着。同一块底上，像素做小了分辨率上去，但每个像素能攒的电子变少、暗部更容易起噪；想同时要细节和弱光，就得靠像素合并与多帧算法在两种模式之间来回切。<strong>底多大、像素多大、合并怎么取舍</strong>这笔账，第十一章附「传感器尺寸与像素大小的权衡」会专门算，这里先把物理含义立住。</p>

<h5 class="font-semibold mt-3 mb-1">大底、高像素、像素合并、堆栈式：能解决什么，解决不了什么</h5>
<p class="mb-2">发布会上四个词出现得最勤，但它们不是四个"升级"，而是四种不同的取舍。</p>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>大尺寸传感器</strong>：解决的是"单位时间里收到的光子总数"。光多了，信噪比和单帧动态范围的上限就高，暗部更干净，也更容易拍出自然的背景虚化。解决不了的是镜头能不能把这束光好好送到整块底上——底一大，边缘像差、暗角、边角解析力、模组厚度和最近对焦距离都跟着变难。<strong>底是上限，不是结果</strong>，它得配上够好的镜头与调校才兑现。</li>
  <li><strong>高像素</strong>：在光线充足、镜头解析力跟得上、手也稳的时候，它给的是细节与裁切空间——拍文档、拍远处建筑、二次构图确实有用。但它抬高不了暗光表现：单像素变小后，弱光主要靠合并与算法兜底；文件更大、处理更耗电、对焦与防抖的容错更小；而且在手机屏幕上或发到社交平台，多出来的细节常常根本看不到。</li>
  <li><strong>像素合并</strong>：把相邻的几个小像素合成一个大像素输出，等于在弱光下临时换回"大像素"模式，暗部更干净、帧率与文件也更友好，所以默认拍照多半走这条路。代价是输出分辨率下来了，彩色滤光片的重排让去马赛克更绕，容易出现伪色、细节被抹平；想拿回全分辨率，得手动切高像素模式，而且最好有足够的光。它更像<strong>同一块传感器上的两套用法</strong>，不是凭空多出来的画质。</li>
  <li><strong>堆栈式设计</strong>：主要解决"读得快"。逻辑层腾出面积放高速模数转换与缓存，连拍、高帧率视频、快速多帧合成、更轻的果冻效应都受益；片上缓存还能让多帧合成少等一会儿，逆光抓拍更不容易糊。它<strong>不直接提升单帧的收光与动态范围</strong>，成本、发热与堆叠工艺的难度却是实打实的。把它当"画质更好"看，容易买错重点。</li>
</ul>

<h5 class="font-semibold mt-3 mb-1">几个流传很广的误解</h5>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>"像素越高越清晰"</strong>：清晰度还得看镜头解析力、对焦精度、防抖、ISP 的锐化与降噪，以及你最终在多大的屏幕上看。像素只是给了一个上限。</li>
  <li><strong>"底大一级压死人"</strong>：这句话在暗光与动态范围上大致成立，但被用得太绝对。镜头素质、光圈、对焦、防抖、算法调校、甚至软件版本，都能让两块标称相近的底拍出不同结果。</li>
  <li><strong>"ISO 越高越能感光"</strong>：ISO 是读出之后加的增益。光子数量由传感器面积、量子效率、光圈和快门决定，调高 ISO 只是把已有信号连同噪声一起放大，画面会变亮但不会变干净。</li>
  <li><strong>"1 英寸就是 25.4 毫米"</strong>：前面说过，那是历史标称，不是实际对角线尺寸。</li>
  <li><strong>"参数一样，画质就一样"</strong>：滤色片光谱、微透镜设计、读出噪声、满阱容量、ISP 与算法、镜头、固件调校全都不写在参数表里。</li>
  <li><strong>"大底就一定虚化好"</strong>：虚化还取决于实际焦距、光圈、对焦距离和主体与背景的距离。手机更多时候是靠算法算出来的景深，跟传感器尺寸不是一回事。</li>
  <li><strong>"动态范围高，逆光就稳了"</strong>：传感器只是给出可用的明暗跨度，最终能不能同时保住天空和人脸，还要看测光、多帧合成对不对、有没有鬼影、色调映射压得自不自然。</li>
</ul>

<h5 class="font-semibold mt-3 mb-1">把参数放回场景里看</h5>
<p class="mb-2">参数脱离场景就没意义，换成几个你真会碰到的画面，一下就具体了。</p>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>暗光餐厅、夜里的街边</strong>：最先不够的是光子，于是传感器尺寸、像素尺寸、光圈和量子效率排在前头；此时切高像素模式往往更糟，默认的多帧降噪与像素合并才是正解。快门一长，防抖与持机稳定性又变成新的短板。</li>
  <li><strong>窗边人像、逆光的天空</strong>：拼的是动态范围，但真正救场的是 HDR 合成。合成要连拍好几帧，读出速度不够、手一抖、人一动，就容易出现鬼影或边缘发亮的假轮廓——这也是堆栈式与快速读出在这一幕里的价值。</li>
  <li><strong>追着跑的孩子、宠物、扫街挥手</strong>：逐行读出的卷帘快门会让快速横移的直线变斜、让挥动的手臂变形，这叫果冻效应。此时读出速度比"多几百万像素"重要得多；快门、对焦追焦和连拍能力一起决定能不能抓到。</li>
  <li><strong>演唱会、月亮、远处舞台</strong>：长焦端的传感器通常比主摄小，光线又差，先天就吃亏。高像素裁切能补一点构图，但补不来光子；这时候别指望参数表，先看那颗长焦的底和光圈。</li>
  <li><strong>拍文档、白天的建筑与风景</strong>：光足够、可以稳稳端住，高像素与镜头解析力才真正派得上用场，放大看细节、后期裁切都有意义。</li>
  <li><strong>边走边录视频</strong>：读出速度决定果冻效应，防抖决定画面稳不稳，而电子防抖还要裁掉一圈视野。这一幕里"传感器强"和"视频好用"之间，隔着好几道工程取舍。</li>
</ul>
<p class="mb-2"><strong>收在一句话上</strong>：CMOS 只是<strong>采集端</strong>。最终成片是「传感器 × 镜头 × 对焦与防抖 × ISP 与算法 × 显示与压缩」一起算出来的结果，参数给的是上限与倾向，不是照片本身。以后看发布会，别急着比谁的数字大——先问这个场景里最缺的是光、是明暗跨度、是速度，还是细节，再回头找对应的那一项。这么看，参数表才不会骗人。</p>
'''

ANCHOR = '<h5 class="font-semibold mt-3 mb-1">潜望式长焦镜头</h5>'
MARK = '<!-- v19-cmos-section -->'
