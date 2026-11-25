# -*- coding: utf-8 -*-
"""v1.9 第一章 SoC 小节新增：CPU / GPU / NPU 里的 ALU。

插入位置：第一章「NPU：AI加速引擎」扩充内容之后、「ISP：影像信号处理器」之前。

技术口径（避免常见误写）：
- ALU 只做整数算术 / 位逻辑 / 移位 / 比较，浮点归 FPU，不混为一谈；
- 向量单元是「一条指令多个 lane」，每个 lane 里才是 ALU/FPU；
- NPU 的算力主体是 MAC 阵列（乘加融合 + 数据流），不是「一堆 ALU」；
  ALU 在 NPU 里只做标量辅助（地址、量化、比较、调度）；
- 不写具体芯片的 ALU 数量 / TOPS 数字，只用数量级与职责描述。
"""

# 这一节的 HTML 片段。样式沿用第一章既有写法（h5 / p.mb-2 / ul / table / tip-box）。
SECTION_HTML = '''
<h5 class="font-semibold mt-3 mb-1">ALU：三类处理器里真正"算数"的那个部件</h5>
<p class="mb-2">前面把 CPU、GPU、NPU 各自干什么讲了一遍，但有个问题一直绕着没说：它们内部真正把数字算出来的，到底是什么？答案是个听起来有点老派的名字——<strong>ALU（Arithmetic Logic Unit，算术逻辑单元）</strong>。它是所有处理器里最基础的"算数部件"，可三类处理器把它用出了三种完全不同的样子。更常见的一个误会是把 NPU 说成"有很多 ALU"——这一节主要就是把这件事掰清楚。</p>

<p class="mb-2"><strong>一、ALU 管什么，不管什么</strong></p>
<p class="mb-2">先给 ALU 划个范围。它是一块组合逻辑电路，接两个操作数，按控制信号做一次运算，吐出结果。传统意义上它管四件事：</p>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>整数算术</strong>：加、减，以及乘法（有的设计里乘法单独做一块）；除法常要迭代多轮或交给专门电路。</li>
  <li><strong>位逻辑</strong>：与、或、非、异或。权限位判断、开关掩码、颜色通道拆分，靠的都是它。</li>
  <li><strong>移位</strong>：左移右移、算术移位、循环移位。乘除 2 的幂、打包解包数据都用得上。</li>
  <li><strong>比较</strong>：判断相等或谁大谁小，结果不写回普通寄存器，而是写进<strong>标志位</strong>（是否为零、有没有进位、溢出没溢出、结果正负）。</li>
</ul>
<p class="mb-2">它<strong>不</strong>管三件事：不存数据、不决定做什么、不记住上一次算的结果。一条指令真正跑起来是这样一条链：</p>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>控制单元（CU）</strong>负责取指和译码，看懂"这是一条加法"，然后发出控制信号，告诉 ALU 这次选哪一种运算。</li>
  <li><strong>寄存器堆</strong>把两个操作数递过来（有时其中一个是指令里直接带的立即数）。寄存器是离 ALU 最近、最快的一层存储。</li>
  <li><strong>ALU</strong>只负责算这一下，结果沿写回总线送回目的寄存器，标志位送回状态寄存器。</li>
  <li>要不要跳转、下一步执行哪条，是控制单元看着标志位决定的，<strong>不是 ALU 决定的</strong>。</li>
</ul>
<p class="mb-2">打个后厨的比方：控制单元是看单子点菜的人，寄存器是备料台，ALU 是灶上那口锅——只管把递来的两份料按吩咐炒一下，炒完盛回盘子，既不存菜，也不接单。</p>

<p class="mb-2"><strong>二、先把几个容易混的名字分开</strong></p>
<p class="mb-2">现代芯片里这些单元物理上常常挨在一起、共用数据通路，所以发布会和参数表很容易把它们混着叫。但职责真的不一样：</p>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>FPU（浮点单元）</strong>：管浮点数。它要对齐指数、规格化尾数、处理舍入和 NaN/Inf 这类异常，电路比整数 ALU 复杂得多，是一条独立的浮点流水线。严格说它不是 ALU——虽然它内部也有加法器和乘法器。</li>
  <li><strong>向量单元 / SIMD</strong>：一条指令同时对一组数据做同样的运算（手机上最常见的是 NEON，新一代还有 SVE 一类可伸缩向量扩展）。每个 lane（通道）里才是一个小小的 ALU 或 FPU。并行来自 lane 的数量，不是来自指令变强了。</li>
  <li><strong>矩阵单元 / 张量核</strong>：专门为矩阵乘设计的块，一次处理一小片矩阵而不是一对数字。CPU 和 GPU 里也有这类单元，但它是另一层东西。</li>
  <li><strong>MAC 阵列</strong>：MAC 是"乘加融合"（a×b+c 一步做完，中间结果不写回）。把成千上万个 MAC 排成二维阵列、让权重和激活在里面流动，就是 NPU 的主力算力来源。<strong>它和 ALU 不是同一种东西</strong>：ALU 每做一次都要由指令告诉它"这次算什么"，MAC 阵列则是把一种固定运算铺成一张网，靠数据流喂进去。</li>
</ul>
<div class="tip-box rounded-lg p-4 mb-3"><p class="font-semibold"><i class="fas fa-lightbulb mr-2"></i>一句话记牢</p><p class="mt-1">ALU 是"按指令算一次"的通用部件；FPU 专管浮点，向量单元把很多个 ALU 排成一排听同一条指令，MAC 阵列则干脆把运算固定成乘加、铺成一整片。以后听到"某芯片有几千个 ALU"，先问一句：说的是真 ALU，还是把向量 lane 和 MAC 也算进去了？</p></div>

<p class="mb-2"><strong>三、CPU 里的 ALU：少，但每一个都很快</strong></p>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>主要运算</strong>：整数加减、位逻辑、移位、比较，外加大量地址与索引计算。浮点交给 FPU 和向量单元，分支判断交给分支单元，读写内存交给加载/存储单元——这些都不算 ALU，但和它一起挂在核心的执行端口上。</li>
  <li><strong>数据精度</strong>：以 64 位整数为主，也有 32 位；标量运算是常态，向量指令另说。</li>
  <li><strong>组织方式</strong>：一个核心里通常只有几个整数 ALU（常见两到四个），配乱序发射、寄存器重命名、深流水和分支预测。整条流水线的设计目标只有一个——把<strong>单条指令的延迟</strong>压到最短，让分支密集、前后依赖强的代码也能一路跑下去。</li>
  <li><strong>并行规模</strong>：每核个位数 ALU，整芯片也就几十个。CPU 的并行靠的是指令级并行（同时发射多条指令）和多核，而不是堆 ALU 数量。</li>
  <li><strong>典型任务</strong>：应用逻辑、系统调度、界面事件、文件与权限判断、整数循环、数据库查询条件。这些都是"步骤多、分支多、每一步都等上一步结果"的活。</li>
</ul>
<p class="mb-2">设计目标可以浓缩成四个字：<strong>低延迟、通用</strong>。宁愿把一个 ALU 做得很复杂、频率拉得很高，也不要几千个慢吞吞的。</p>

<p class="mb-2"><strong>四、GPU 里的 ALU：复制成成千上万个 lane</strong></p>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>主要运算</strong>：整数和浮点都有，主力是浮点的加、乘与乘加融合（FMA），还有插值、纹理采样和一批特殊函数；整数部分多用来算索引、地址和循环计数。</li>
  <li><strong>数据精度</strong>：FP32 是基本盘，移动端大量用 FP16 省电省带宽，整数一般是 32 位。同一个芯片上几种精度混着跑很正常。</li>
  <li><strong>组织方式</strong>：一堆结构相同的 lane 编成组（不同厂商叫 warp 或 wavefront），走 SIMT 路线——一条指令同时喂给组里几十个 lane，每个 lane 有自己的算术单元。遇到分支分歧时，走不同分支的 lane 暂时被屏蔽，两组先后走完，这也是为什么 GPU 怕"每个像素各走各的判断"。</li>
  <li><strong>并行规模</strong>：成百上千个 lane，整芯片数千量级的算术单元。单 lane 慢一点根本不重要，只要同一时刻有足够多的像素或顶点在跑。</li>
  <li><strong>典型任务</strong>：顶点变换、像素着色、光照与阴影、界面动画合成、照片滤镜，以及一部分通用计算和 AI 推理。</li>
</ul>
<p class="mb-2">设计目标是<strong>高吞吐</strong>：用海量并行线程把访存等待藏起来。和 CPU 放一起看特别清楚——CPU 是"少而强、求快"，GPU 是"多而简、求多"。</p>

<p class="mb-2"><strong>五、NPU 里的 ALU：主力其实不是它</strong></p>
<p class="mb-2">这一段最容易被写错，咱们说细一点。NPU 里<strong>确实有 ALU</strong>，但只占很小一块面积，干的是辅助活；真正撑起算力的是 MAC 阵列。</p>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>ALU 在 NPU 里做什么</strong>：地址和步长计算、循环计数、量化与反量化的定点换算（把 INT8 按 scale 和 zero-point 还原回浮点范围）、ReLU 之类的比较与取最大值、查表、算子调度。全是标量、控制面的杂活。</li>
  <li><strong>主力运算</strong>：卷积、全连接、注意力里那些矩阵乘，落到硬件上就是成千上万次乘加（MAC）。这不是"把 ALU 造大一点"，而是把一种运算铺成阵列，让数据在阵列里流动、权重尽量留在片上 SRAM 不来回搬——省下的搬运动量，正是 NPU 能效比高的关键。</li>
  <li><strong>数据精度</strong>：低精度、量化是常态，INT8 在端侧推理里是主力，更激进的场景会用 INT4 或 FP8，部分层用 FP16。用精度换能效，这和 CPU/GPU 追求 FP32 准确度的取向完全不同。</li>
  <li><strong>组织方式</strong>：MAC 阵列 + 片上权重缓存 + DMA 数据流调度，执行过程高度确定、几乎没有分支。少量标量 ALU 在旁边负责"把数据摆好、把结果收拾好"。</li>
  <li><strong>并行规模</strong>：MAC 单元成千上万，但要注意它们都在算<strong>同一个矩阵乘的不同输出位置</strong>，不是各自独立执行不同指令——这和 GPU 里"上千个 lane 可以各自跑不同线程"是两种并行。</li>
  <li><strong>典型任务</strong>：端侧大模型推理、夜景降噪、人像分割、语音识别、实时翻译、相册语义检索。</li>
</ul>
<p class="mb-2">设计目标是<strong>每瓦吞吐</strong>（发布会上那个 TOPS/W）。它愿意牺牲通用性、牺牲精度，甚至牺牲"能跑任意程序"这件事，换来同样的电池能多跑几十倍矩阵运算。</p>
<div class="tip-box rounded-lg p-4 mb-3"><p class="font-semibold"><i class="fas fa-lightbulb mr-2"></i>别把 NPU 说成"一堆 ALU"</p><p class="mt-1">ALU 是"一条指令来，做一次通用运算"；MAC 阵列是"一份数据流进来，整片阵列同时把乘加做完"。NPU 有 ALU，但那是配角。把两者画等号，就会误以为 NPU 只是"ALU 更多的 CPU"，也就解释不了为什么它跑矩阵快、跑个带一大堆分支的普通程序反而慢。</p></div>

<p class="mb-2"><strong>六、一张表看清差别</strong></p>
<div class="overflow-x-auto">
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">对比项</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">CPU</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GPU</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">NPU</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">主力运算单元</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">整数 ALU（配 FPU / 向量单元）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">大量 lane，每 lane 含浮点与整数算术单元</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MAC 阵列；ALU 只做标量辅助</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ALU 主要运算</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">整数加减、位逻辑、移位、比较、地址计算</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">整数索引与循环；浮点主力是加乘与 FMA</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">地址步长、量化换算、比较取最大值、调度</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">常用精度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">64 / 32 位整数；浮点另走 FPU</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">FP32、FP16、INT32</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">INT8 为主，INT4 / FP8 / FP16 视层而定</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">组织方式</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每核几个 ALU，乱序发射、深流水、分支预测</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">lane 编组，一条指令带一组（SIMT）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">二维 MAC 阵列 + 片上权重驻留 + 数据流</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">并行规模</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每核个位数，整芯片几十个</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">成百上千 lane，整芯片数千量级</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">成千上万 MAC，但同算一个矩阵乘</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">设计目标</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">低延迟、什么都能干</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">高吞吐、同构数据并行</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每瓦吞吐、专用高效</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">典型任务</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">应用逻辑、权限判断、调度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">像素着色、光照、滤镜</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">卷积、矩阵乘、端侧推理</td></tr>
</tbody>
</table>
</div>

<p class="mb-2"><strong>七、把几个场景连起来走一遍</strong></p>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>整数与逻辑运算</strong>：解锁时判断某个权限位开没开、相册按日期排序、算剩余存储够不够放一段视频——全是 AND、比较、加减，CPU 里那几个 ALU 最擅长，且这类活前后依赖强，堆再多 lane 也帮不上忙。</li>
  <li><strong>浮点运算</strong>：游戏里一帧的光照、界面滑动时的动画合成、给照片套个滤镜——几百万个像素做几乎一样的浮点运算，正好交给 GPU 的 FP32 / FP16 lane 一起算。</li>
  <li><strong>AI 推理</strong>：拍一张夜景，ISP 先把原始数据整理好，NPU 用 INT8 的 MAC 阵列跑完降噪模型，旁边的标量 ALU 负责把量化结果还原、做 ReLU 和取最大值，最后结果交回 CPU 写进文件。这里真正吃算力的是 MAC 阵列，ALU 是把边角收拾干净的人。</li>
  <li><strong>三者接力</strong>：同一次拍照里，CPU 发号施令、ISP 预处理、NPU 推理、GPU 合成预览、CPU 收尾写盘。手机里没有谁替代谁，只有各干各的那一段。</li>
</ul>

<p class="mb-2"><strong>本节小结</strong></p>
<p class="mb-2">ALU 是"按指令算一次"的基本部件：CPU 把它做得少而快、专攻低延迟和通用；GPU 把它复制成成千上万个 lane、用同构并行换吞吐；NPU 干脆把主力换成 MAC 阵列，只留少量 ALU 做标量辅助，用低精度换能效。所以"NPU 就是 ALU 更多的处理器"这个说法是不准确的——三者差的不是数量，是<strong>为哪种计算而设计</strong>。</p>
<p class="mb-2">给你一个能带走的判断法：看到分支、逻辑、整数和"一步一步等结果"，想 CPU 的 ALU；看到像素、浮点、大量同构数据，想 GPU 的 lane；看到矩阵乘、量化、TOPS/W，想 NPU 的 MAC 阵列。发布会上的算力数字会年年翻，但这三种"算"的方式不会变——知道哪种活交给哪个部件，比记住某个数字有用得多。</p>
'''

# 插入锚点：ISP 小节的 h5 开始标签（唯一）
ANCHOR = '<h5 class="font-semibold mt-3 mb-1">ISP：影像信号处理器</h5>'
MARK = '<!-- v19-alu-section -->'
