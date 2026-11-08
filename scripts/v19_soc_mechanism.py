# -*- coding: utf-8 -*-
"""v1.9 第一章新增正式章节（h4）：SoC 的关键组成与工作机制。

插入位置：第一章 h4「一、手机硬件"五脏六腑"」之后、原「二、操作系统」之前；
原 h4 编号二~六顺延为三~七（目录/侧边栏不引用这些文字，安全）。

技术口径：
- 明确区分通用架构规律（调度分层、并行形式、地址转换、IPC 公式）与
  具体芯片实现（发射宽度、流水级数、缓存容量、warp 数量），后者一律
  写「各代不同、以厂商文档为准」，不编造数字。
- 不写具体芯片的 TOPS / GB/s / 频率 / IPC 实测值。
- 术语只讲机制与协作，不做词典式罗列。
"""

# h4 标题与小节 HTML
SECTION_HTML = '''
<h4 class="text-lg font-semibold mt-4 mb-2">二、SoC 是怎么把一件活干完的：调度、运算与数据通路</h4>
<p class="mb-2">上一节把 SoC 里的部件认了个遍：CPU、GPU、NPU、ISP，还有刚讲过的 ALU。但认全零件不等于懂机器——真正让手机"跟手"的，是这些部件<strong>怎么被安排着一起干活</strong>。你点一下快门，到屏幕亮起一张夜景照片，中间要过五道手、排好几次队、等若干次信号。这一节就顺着这条线走一遍：谁负责决定做什么，谁负责决定什么时候做，数据又从哪里来、到哪里去。</p>
<p class="mb-2">先把话说在前面：下面讲的都是<strong>通用架构规律</strong>——分几层调度、有哪几种并行、地址怎么转换，各家芯片大同小异。至于一个核心几级流水、能同时发射几条指令、缓存多大、一组线程有多少个 lane，那是<strong>具体芯片实现</strong>，每一代都在变，别把书里的说法当成某颗芯片的规格表，真要查就翻厂商文档。</p>

<h5 class="font-semibold mt-3 mb-1">1. 先看全景：一次任务要过几道手</h5>
<p class="mb-2">手机里几乎没有任何一件事是"应用直接指挥硬件"完成的。哪怕是给一张照片加个滤镜，也要经过这样一串角色：</p>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>应用</strong>说清"我要什么"——拍一张照、跑一帧游戏、识别一句话。它只提需求，不关心谁来做。</li>
  <li><strong>运行时与编译器</strong>把需求翻译成机器能执行的形式：一段指令、一张计算图、一串命令。顺便做优化，把能合并的合并、能提前算的提前算。</li>
  <li><strong>驱动</strong>把这些命令写进硬件的队列，登记好依赖关系，然后敲一下"门铃"告诉硬件：有新活了。</li>
  <li><strong>硬件调度器</strong>从队列里挑出此刻能跑的活，分给具体执行单元。它是最后一层，也是唯一真正在每个时钟周期做决定的角色。</li>
  <li><strong>完成通知</strong>沿原路返回：硬件发中断，驱动确认，运行时唤醒等待的线程，应用拿到结果。</li>
</ul>
<p class="mb-2">这条链上有个很要紧的分界：<strong>"做什么"由软件层决定，"什么时候、由哪个部件做"由硬件层决定</strong>。软件层看得到整张任务图，所以能安排顺序、合并重复、避免冲突；硬件层只看得到眼前几条指令和几个空着的执行单元，所以能在一个周期内做出软件来不及做的细粒度决定。两头各管一段，缺一头都不行。</p>

<h5 class="font-semibold mt-3 mb-1">2. 五层调度者：谁决定什么</h5>
<p class="mb-2">把这五层摊开看，职责边界其实很清楚：</p>
<div class="overflow-x-auto">
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">层</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">决定什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">不决定什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">大致时间尺度</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">操作系统调度器</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">哪个进程/线程上哪个核心、优先级、时间片、唤醒与睡眠；手机上还要按负载挑大核还是小核</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不管单条指令，也看不懂 GPU/NPU 内部的队列</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">毫秒到微秒</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">运行时</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把 API 调用组织成命令缓冲或计算图；模型推理时做算子融合、切子图、挑后端（CPU/GPU/NPU）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不生成最终机器指令，也不碰硬件寄存器</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每次提交前后</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">编译器</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">指令选择、寄存器分配、循环展开、向量化；NPU 侧还要切块（tiling）适配片上存储、排好权重与数据搬运顺序</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不知道运行时会出现什么突发任务，也不控制硬件当前是否空闲</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">安装时 / 首次运行时 / 提前离线完成</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">驱动</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把命令写进环形队列、建立同步对象、映射内存与 DMA、写门铃寄存器提交、处理完成中断</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不做算法优化，也不决定执行单元怎么分派</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">提交与回收那一瞬</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">硬件调度器</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">此刻哪条指令发射、哪组线程上执行单元、哪个数据块进阵列；处理结构冒险与依赖就绪</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">看不到整张任务图，不知道应用的意图，也不做长期规划</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每个时钟周期</td></tr>
</tbody>
</table>
</div>
<p class="mb-2">有两处边界在不同平台上会移动，值得留意。一是<strong>编译器和运行时</strong>：有的栈把图优化放在应用安装时一次做完，有的放在首次运行时，还有的干脆把一部分编译塞进驱动里，提交前才生成内核。二是<strong>操作系统和设备</strong>：CPU 线程归操作系统管，GPU/NPU 的任务队列归驱动和硬件管，操作系统通常只看到"这个进程在等一个 fence"。所以别死记"某一层一定做某件事"，记住的是这条<strong>从粗到细、从意图到周期</strong>的分工链。</p>
<p class="mb-2">手机上的操作系统调度还多一件事：<strong>能耗感知</strong>。同样一段代码放超大核上跑得快但费电，放能效核上慢一点却省得多。系统要盯着当前负载、温度和剩余电量，把前台交互这类急活给大核，把后台同步、相册整理这类不急的活慢慢挪到小核。这是手机和台式机很不一样的地方——不是"越快越好"，是"够快的前提下别把电烧光"。</p>

<h5 class="font-semibold mt-3 mb-1">3. 一次异步任务的完整旅程</h5>
<p class="mb-2">用"拍一张夜景照片"当例子，把整条链走一遍。你会发现所谓异步，不是"扔到后台随便跑"，而是一条<strong>有依赖图、有排队、有完成信号</strong>的流水线。</p>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>① 应用提交</strong>：相机 App 发起一次拍摄请求，画面预览、降噪推理、最终编码可能一次登记好几项工作。调用立刻返回，拿到的是句柄或 future，而不是结果——这就是"异步"的起点。</li>
  <li><strong>② 编译与图组织</strong>：运行时把降噪模型从文件里加载出来，编译器（或驱动里的编译步骤）把模型切成硬件能吃的块，安排好权重什么时候搬进片上存储，把能合并的层合成一个算子。这一步产出的是<strong>命令序列或计算图</strong>，不是结果。</li>
  <li><strong>③ 命令排队</strong>：驱动把命令写进硬件的环形提交队列，同时把输入缓冲、输出缓冲映射好，让硬件能直接通过 DMA 读写，不必让 CPU 一字节一字节搬。写完之后敲一下门铃寄存器，硬件才知道队列里有活。</li>
  <li><strong>④ 依赖与同步</strong>：这是最容易出错、也最容易被忽略的一步。ISP 必须先把原始帧处理好，NPU 才能开始推理；GPU 要等 NPU 出结果才能合成预览；写文件又要等编码完成。这些先后关系靠三层东西保证：<strong>信号量</strong>（队列之间"你做完我才开始"）、<strong>fence</strong>（让 CPU 能查询"硬件做到哪了"）、<strong>屏障</strong>（保证前一阶段写的数据对后一阶段真的可见，而不只是"指令发过了"）。硬件内部还有计分板一类的机制，盯着某条指令要用的寄存器准备好没有，没好就先按住不发。</li>
  <li><strong>⑤ 硬件执行</strong>：硬件调度器从队列里取命令，把工作拆给执行单元——CPU 核上的指令、GPU 的一组组线程、NPU 阵列里的一块块矩阵，各跑各的。这一层的细节下一节展开。</li>
  <li><strong>⑥ 完成通知</strong>：结果写回内存，硬件触发中断；驱动的中断处理先做最要紧的确认，剩下的收尾放到底半部或工作队列里；对应的 fence 被标记完成，运行时唤醒等在它上面的线程，App 的回调拿到照片，缩略图才跳出来。</li>
</ul>
<p class="mb-2">这条链解释了几个日常现象：为什么点了快门要等一下才出图（在排队和推理），为什么拍照时偶尔会发热掉帧（ISP、NPU、GPU、CPU 同时抢内存带宽），以及为什么系统升级后"同样的硬件拍照变快了"（编译器和驱动把图和队列排得更好，硬件一个晶体管没换）。</p>
<div class="tip-box rounded-lg p-4 mb-3"><p class="font-semibold"><i class="fas fa-lightbulb mr-2"></i>一句话记牢</p><p class="mt-1">应用交的是"意图"，驱动交的是"命令"，硬件要的是"此刻能跑的活"。中间那些信号量、fence 和屏障，就是把"意图"安全地变成"结果"的红绿灯。异步快，是因为排队和等信号不占着 CPU 死等，不是因为可以不管顺序。</p></div>

<h5 class="font-semibold mt-3 mb-1">4. 硬件内部怎么把活塞满</h5>
<p class="mb-2">命令到了硬件手里，接下来是一场"别让执行单元闲着"的持久战。芯片里有好几种并行，名字容易混，但它们挖的是不同层面的空档。</p>
<p class="mb-2"><strong>流水线调度</strong>是最基础的一层。一条指令要走取指、译码、发射、执行、写回几步，把这几步拆开重叠起来，就像工厂流水线：第一条还在执行，第二条已经译码，第三条正在取指。麻烦在于三种"冒险"：两个步骤抢同一个部件（结构冒险）、后一条要等前一条的结果（数据冒险）、遇到分支还不知道下一条取哪里（控制冒险）。对应的办法是<strong>前递</strong>（把刚算出来的结果直接旁路给下一条，不等写回）、<strong>分支预测</strong>和必要时<strong>停顿或冲刷</strong>。预测错了要推倒重来，代价不小，这也是为什么 CPU 特别怕分支密集的代码。</p>
<p class="mb-2"><strong>指令级并行（ILP）与多发射</strong>：一个周期只发一条指令太浪费，于是宽发射的核心一次取多条、译多条、发多条。能同时发几条就是发射宽度，是具体芯片实现，各代不同。但发得出去不等于能一起跑——得看这几条指令彼此有没有依赖、有没有空着的功能单元、寄存器堆能不能同时供上那么多操作数。</p>
<p class="mb-2"><strong>乱序执行</strong>是挖 ILP 的主力手段。编译器给出的指令顺序是"按程序逻辑排的"，硬件可以在不改变最终结果的前提下，把后面那条不依赖前面结果的指令提前做。为了让这件事安全，硬件做了两件配套：<strong>寄存器重命名</strong>，把指令里写的那些架构寄存器映射到更多物理寄存器上，消掉本来只是"名字撞车"造成的假依赖；<strong>重排序缓冲</strong>，让指令可以乱序执行、但必须<strong>按序退休</strong>，这样一旦发生异常，机器状态仍然停在正确的那条指令上。所以准确说法是"乱序执行、按序提交"，不是"随便乱跑"。</p>
<p class="mb-2"><strong>线程或任务并行</strong>换了一个层面：不再盯着单条指令，而是让多个线程、多个任务同时在跑。CPU 靠多核和同步多线程；GPU 把大量线程编成组，一组暂时等内存时立刻切到另一组，切换开销极小（上下文本来就常驻在寄存器堆里），用"线程多"来把访存延迟藏掉；手机后台同步、音频解码、界面渲染各占一条线，也是这一层。</p>
<p class="mb-2"><strong>数据并行</strong>再换一层：同一条指令同时对一批数据做同样的运算。CPU 的向量扩展、GPU 的一组 lane、NPU 阵列里同时算的许多输出点，都属于这一类。它和线程并行的区别在于：线程并行是"很多条不同的执行流"，数据并行是"一条执行流带着一大片数据"。</p>
<p class="mb-2">把这三者和上一节的 ALU 连起来看就通了：流水线是让<strong>同一个部件</strong>别空转，多发射与乱序是让<strong>一个核心里的几个部件</strong>同时忙，线程与数据并行是让<strong>整片芯片</strong>同时忙。层级越往上，需要的调度越"粗"、越依赖软件事先把活切好。</p>

<h5 class="font-semibold mt-3 mb-1">5. CPU / GPU / NPU 的调度器：粒度、目标与限制</h5>
<p class="mb-2">三类处理器都有"调度器"，但调的东西完全不是一回事。用一张表收住：</p>
<div class="overflow-x-auto">
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">对比项</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">CPU</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GPU</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">NPU</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">调度粒度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">软件层是线程/进程；硬件层细到单条指令与微操作</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一次绘制或计算提交，硬件层是成组的线程（一组几十个 lane 一起走）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">整张推理图、算子，或按片上存储切出的数据块</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">主要目标</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">低延迟、响应快、公平、兼顾能耗</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">喂满执行单元、用大量线程隐藏访存等待、拉高吞吐</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">让数据流不断、权重尽量留在片上、每瓦吞吐最高</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">谁定顺序</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">操作系统定线程归属，硬件动态乱序决定指令先后</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">驱动与运行时定提交顺序，硬件在就绪的线程组之间切换</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">编译器和运行时基本把顺序排死，硬件按图执行</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">动态程度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最高：每周期都可能改主意，能应付事先猜不到走向的分支</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">中：组之间切换很灵活，组内却要步调一致</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最低：几乎是静态数据流，换来的是极高能效</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">主要限制</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">单线程里的依赖链、分支预测失误、上下文切换开销</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一组里出现分支分歧要分组串行；寄存器占用多了能同时驻留的组就少</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">图要能静态切开，输入形状一变可能得重编译；不擅长任意控制流</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">典型任务</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">界面事件、应用逻辑、调度与权限判断</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">像素着色、特效、动画合成</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">降噪、分割、识别、端侧生成式推理</td></tr>
</tbody>
</table>
</div>
<p class="mb-2">一句话概括差别：<strong>CPU 的调度器在"猜"，GPU 的在"换"，NPU 的在"照着做"</strong>。CPU 面对的是走向事先猜不准的程序，得靠分支预测和乱序去赌下一步；GPU 面对的是大量同构线程，一组卡住就换另一组，不需要猜；NPU 的活早在编译器里就切好排好了，硬件按图流水即可，省下的动态决策电路全变成了能效。</p>
<p class="mb-2">这也解释了三者为什么不能互相替代。让 NPU 去跑一个满是分支的应用逻辑，它连"下一步该走哪"都没法灵活决定；让 CPU 去跑矩阵乘，它那些精密的乱序电路全用不上，还每个数据都要过一遍指令。分工不是谁比谁强，是各自把调度成本花在了最值的地方。</p>

<h5 class="font-semibold mt-3 mb-1">6. 算数的地基：加法器、乘法器与算术运算单元</h5>
<p class="mb-2">上一节讲了 ALU 是"按指令算一次"的部件，这一节往里再看一层：那个"算一次"，物理上到底是什么在算。</p>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>加法器</strong>是地基中的地基。一个全加器把三个一位输入（两个加数位加一个进位）变成"本位和"与"进位输出"；把它们串起来就能算多位加法，但最朴素的行波进位要等进位一级一级传过去，位数越多越慢，于是有了超前进位、进位选择这类提前算进位的做法。加法器不只是做加法：<strong>减法</strong>用补码变成加法，<strong>比较</strong>是做一次减法再看标志位，<strong>地址计算</strong>、循环计数、跳转到哪一行，底层都是它。</li>
  <li><strong>乘法器</strong>贵得多。本质上是一堆"部分积"移位后相加，工程上用 Booth 编码减少部分积数量、用压缩树把多层加法并成少数几层，再做一次最终加法。它占的面积和耗的时间都远大于加法器，所以早期处理器常常把整数乘法单独做一块，甚至用多周期迭代完成。上一节说的 FPU 里也有乘法器，只不过它算的是浮点尾数，前后还要处理指数与规格化。</li>
  <li><strong>算术运算单元</strong>是把这些零件装到一个框里：加法器、乘法器、逻辑门阵列、桶形移位器、前导零计数，再加上一组多路选择器——控制信号说"这次做加法"，就把加法器的结果选出去；说"这次做异或"，就选逻辑门的结果。这个带选择器的组合体，就是整数执行单元／ALU 的实体形态。它自己不会挑活，挑活的是控制单元发来的那几位控制信号。</li>
</ul>
<p class="mb-2">把这个和 NPU 的 MAC 阵列接上，会看到一个很实在的差别：<strong>MAC 就是把乘法器和加法器焊在一起，中间结果直接进累加器，不写回寄存器、下一轮也不用再读回来</strong>。一次乘加省掉一写一读，成千上万次乘加省下的搬运动量，正是 NPU 能效比 CPU、GPU 高的一大微观原因。所以 MAC 不是"更快的 ALU"，是"把某一条固定路径做到极致"。</p>

<h5 class="font-semibold mt-3 mb-1">7. 指令集、微架构与寄存器：三层契约</h5>
<p class="mb-2">这三个词经常一起出现，但说的不是一回事，分清了能少踩很多坑。</p>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>指令集（ISA）</strong>是软件和硬件之间签的合同：有哪些指令、指令长什么样、程序员能看到哪些寄存器、内存怎么寻址、异常怎么处理。编译器只按这份合同生成机器码，不必关心芯片内部长什么样。手机上常见的合同是 Arm 的 AArch64 一类。</li>
  <li><strong>微架构</strong>是这份合同的一种具体实现：流水线分几级、一个周期能发几条、重排序缓冲多大、分支预测器怎么设计、缓存几层各多大、有几个整数 ALU。同一份 ISA 可以做出完全不同的微架构——这正是手机大小核的依据：大核和小核跑的是<strong>同一套指令</strong>，但内部一个宽而深、一个窄而省，同一段机器码放上去跑，速度和耗电都不同。</li>
  <li><strong>寄存器</strong>要分两层看。ISA 里规定的是<strong>架构寄存器</strong>，数量固定，编译器眼里的世界就这么大；微架构里实际用的是<strong>物理寄存器</strong>，通常多得多，专门用来给寄存器重命名提供"备用名字"，好把假依赖拆开。寄存器堆能同时读写几个端口，直接卡住了多发射的上限——发得出去，也得供得上操作数。</li>
</ul>
<p class="mb-2">拿做菜再比一次：ISA 是菜谱上写的"切块、下锅、调味"这些标准动作；微架构是这家厨房有几个灶、几个厨师、备料台多大；寄存器就是灶台边那几个备料格，格子的数量和同时能伸进去几只手，决定了能并行备几道料。三者对上了，才知道为什么"同一份程序在不同手机上跑得不一样快"——合同没变，厨房变了。</p>

<h5 class="font-semibold mt-3 mb-1">8. 数据从哪来：TLB、缓存、内存控制器、带宽与总线</h5>
<p class="mb-2">前面几节都在讲"算"，可现实里芯片大部分时间是在<strong>等数据</strong>。一次访问要从应用看到的虚拟地址，一路走到内存颗粒，沿途每一站都可能成为瓶颈。</p>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>TLB</strong>是地址转换的缓存。应用用的是虚拟地址，硬件要的是物理地址，这层映射记在页表里；每次都去查页表太慢，于是把最近用过的映射存在 TLB 里。命中就直接拿到物理页，未命中要做一次页表遍历，代价可能是几十上百个周期。用大页、让数据访问更集中，都是为了少踩这种未命中。</li>
  <li><strong>缓存层次</strong>是延迟与容量的折中：一级最小最快、通常每个核心私有；二级大一点、可能一簇核心共用；三级或系统级缓存全芯片共享，ISP、GPU、NPU 也能借它中转。越靠上越贵，放不下太多；越靠下越慢，但能装得多。命中率上不去，ALU 再快也只能空转。多部件共享数据时还要维护<strong>缓存一致性</strong>，保证 CPU 写进去的值，GPU 或 NPU 随后读到的是新的，不是缓存里的旧副本——这正是第 3 节那些屏障要解决的问题之一。</li>
  <li><strong>内存控制器</strong>是最后一道关卡：把读写请求排到 DRAM 的各个 bank/rank 上，合并相邻访问、安排刷新、决定谁先谁后。手机上它还得讲<strong>服务质量</strong>——屏幕扫描和预览帧不能等，后台下载可以让一让。同样一块内存，控制器调度得好不好，实际体验差得出来。</li>
  <li><strong>带宽与延迟是两件事</strong>。带宽是每秒能搬多少数据，延迟是发起一次访问要等多久。大数据块连续读写吃带宽，零散的小访问吃延迟。CPU 靠缓存把延迟压下去，GPU 和 NPU 靠海量并行把等待"藏"在别的线程或数据块后面——这也是为什么它们不怕延迟高，却特别怕带宽不够。</li>
  <li><strong>频率</strong>决定一秒有多少个时钟周期，同一段微架构下频率越高性能越高，但动态功耗大致随频率和电压平方一起涨，手机的散热和电池很快就会把它按住，于是系统不断在升降频（DVFS）。发布会上那个峰值频率，往往只能维持很短一会儿；真正影响长时间游戏或录像的，是散热压住之后的<strong>持续频率</strong>。</li>
  <li><strong>总线互联</strong>是把这些部件连起来的片上网络：CPU、GPU、NPU、ISP、显示、内存控制器都挂在上面，共享有限的通路。多路同时访问就会争用，需要仲裁和优先级。上一节讲 NPU 时提到"ISP 处理结果直送 NPU 的图像分支"，这类专用直通路径的意义就在这儿——绕开公共总线，少一次排队、少一次往返内存。</li>
</ul>
<p class="mb-2">把这一节塞回拍照那个例子：ISP 写帧、NPU 读权重和特征、GPU 合成预览、CPU 编码写文件，四路同时抢内存带宽和总线。这时候瓶颈往往不在"谁的算力不够"，而在<strong>数据搬不动</strong>。所以看手机性能，只盯着算力数字很容易看偏——得连着存储与互连一起看。</p>
<div class="overflow-x-auto">
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">环节</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">主要影响</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">手机里的典型表现</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TLB</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">地址转换命中率，未命中代价高</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">大图、大模型频繁换页时明显变慢</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">缓存层次</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">访问延迟与命中率、多部件一致性</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">反复读写同一批特征图时差别很大</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">内存控制器</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">请求排序、优先级、刷新开销</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">录像时预览不能卡，后台同步要让路</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">带宽</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每秒搬运总量</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多路并发抢通路时整体掉速</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">频率 / 电压</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">周期数，同时受功耗与散热约束</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">峰值跑分好看，长时间游戏会降频</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">总线互联</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">部件间通路、仲裁与专用直连</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ISP→NPU 直连省掉一次内存往返</td></tr>
</tbody>
</table>
</div>

<h5 class="font-semibold mt-3 mb-1">9. VPU、DSP 与 ECC：三位专职配角</h5>
<p class="mb-2">SoC 里还有几个不常上发布会、却天天在干活的部件。它们不是同一类东西，别混着记。</p>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>VPU（视频处理单元）</strong>是专做视频编解码的固定功能硬件：运动估计、变换、熵编码、环路滤波这些步骤直接做成电路。录 4K 视频、视频通话、投屏、边下边播，靠的都是它。用 GPU 的通用算力也能算，但固定功能电路干同一件活省电得多——手机能连续录很久而不烫，很大程度是 VPU 的功劳。</li>
  <li><strong>DSP（数字信号处理器）</strong>是颗小而省、乘加很快、时序确定的处理器，专门伺候连续不断的信号流：通话降噪与回声消除、语音唤醒词常驻监听、陀螺仪与马达数据滤波、部分基带处理。它的价值在于<strong>不用把大 CPU 叫醒</strong>——抬手亮屏、"嘿 Siri"这类永远在线的小活，交给 DSP 常驻跑，功耗可以压得极低。</li>
  <li><strong>ECC（纠错码）</strong>不是加速器，是<strong>可靠性部件</strong>。内存、缓存、片上存储里的位可能因干扰或低电压翻转，ECC 加一点冗余位来发现并纠正单比特错、发现双比特错。手机在内存和关键片上存储里用它来扛低电压运行、提升稳定性；车规和服务器场景要求更严。把它和 VPU、DSP 并列，容易误以为它也在"算"，其实它只保证算出来的数没被悄悄改掉。</li>
</ul>

<h5 class="font-semibold mt-3 mb-1">10. IPC：怎么算，以及为什么不能只看它和频率</h5>
<p class="mb-2">IPC 是 Instructions Per Cycle，<strong>平均每个时钟周期完成多少条指令</strong>。它不是一个出厂标好的参数，而是跑某段程序时测出来的比值：用处理器里的硬件性能计数器读出"退休的指令数"和"实际活跃周期数"，两者相除就得到 IPC。注意分子是<strong>退休</strong>的指令——乱序执行里那些预测错、被冲刷掉的指令不算数。</p>
<p class="mb-2">一段程序花的时间，粗略可以写成：<strong>耗时 ≈ 指令总数 ÷（IPC × 频率）</strong>。这行式子把三件事都摆出来了，也顺便说明只盯其中一个为什么容易看偏。</p>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>频率相同，IPC 可以差好几倍</strong>：微架构的发射宽度、乱序窗口、缓存和分支预测都在影响每周期能真正做完多少条。所以"3GHz 一定比 2.5GHz 快"这种说法，跨代、跨大小核就不成立。</li>
  <li><strong>IPC 高，也不代表更快</strong>：编译器换一版、指令选得不同，指令总数可能变少，IPC 反而"变低"但程序更短；反过来，一段被访存停顿拖住的代码，周期数变大，IPC 会掉，可它未必是芯片不行，可能是数据没喂上。</li>
  <li><strong>指令数本身就不对等</strong>：一条向量指令能同时处理一批数据，一条 NPU 层面的"命令"背后可能是整个矩阵块。这类活 IPC 可能低得可怜，实际吞吐却高得离谱。拿标量 IPC 去比较 GPU 或 NPU，基本没有意义。</li>
  <li><strong>并行度不在公式里</strong>：IPC 描述的是单条执行流每个周期做多少。GPU 靠成百上千组线程、NPU 靠阵列里同时算的许多输出点把吞吐堆上去，它们的强项根本不在这一列指标上。</li>
  <li><strong>手机还要看持续表现和能耗</strong>：峰值频率会被散热按住，长时间负载下真正稳定的是持续频率；同样的活，用专用部件（VPU、NPU、DSP）做完花的能量，可能比让通用核心硬扛少一个量级。</li>
</ul>
<p class="mb-2">所以更靠谱的看法是：先看<strong>单位时间完成了多少真实工作</strong>（每秒出几帧、一次推理多少毫秒、导出一段视频多久），再看<strong>单位能耗完成多少</strong>（同样的活掉多少电、烫不烫），最后才用 IPC 和频率去解释"为什么会这样"。它们是诊断工具，不是成绩单。</p>

<h5 class="font-semibold mt-3 mb-1">11. 把一部手机的一天串起来</h5>
<ul class="list-disc pl-6 mb-3 space-y-1">
  <li><strong>抬手亮屏</strong>：DSP 常驻听着传感器数据，判断出抬手动作，才把应用处理器叫醒；CPU 的能效核先接住，操作系统调度器决定要不要动用大核。</li>
  <li><strong>刷信息流</strong>：CPU 处理列表逻辑与网络回调，GPU 把一屏卡片和动画画出来，VPU 顺手解着信息流里的视频，内存控制器在几路请求之间排优先级。</li>
  <li><strong>拍一张夜景</strong>：ISP 整理原始帧 → 编译器事先切好的计算图进 NPU，MAC 阵列跑降噪，标量 ALU 做量化与取最大值 → GPU 合成预览 → VPU 如果要录像同时开工 → CPU 收尾写文件。整条链靠信号量和 fence 串起来，四路一起抢带宽。</li>
  <li><strong>玩一局游戏</strong>：CPU 跑逻辑与物理、GPU 成批算像素、DSP 处理语音、总线和内存带宽被同时占用；跑上十几分钟，散热开始压频率，这时候决定帧率的往往不是峰值算力，而是持续频率与带宽。</li>
</ul>
<p class="mb-2"><strong>本章小结</strong></p>
<p class="mb-2">把这一节收成三句话。第一，<strong>调度是分层的</strong>：操作系统管线程、运行时与编译器管图和指令、驱动管队列与同步、硬件调度器管每个周期发射什么，越往下越细、越往上越看得全。第二，<strong>并行是分层的</strong>：流水线让一个部件不空转，多发射与乱序让一个核心里的部件同时忙，线程与数据并行让整片芯片都忙起来；CPU 在猜、GPU 在换、NPU 照着编译好的图做。第三，<strong>算得快慢取决于数据喂不喂得上</strong>：TLB、缓存、内存控制器、带宽、频率和总线互联共同决定了执行单元有没有活干，也决定了峰值数字能不能持续。</p>
<p class="mb-2">给你一个能带走的判断法：看到"卡"，先问是<strong>算不过来</strong>、<strong>等数据</strong>，还是<strong>在排队等依赖</strong>；看到"快"，先问是硬件更强，还是编译器和驱动把活排得更好。频率和 IPC 只是线索，真正该看的是单位时间做完了多少事、为这些事付了多少电。至于具体几级流水、几发射、缓存多大——那是每颗芯片自己的实现，别当成通用规律记。</p>
'''

# 插入锚点：原 h4「二、操作系统」开始标签（唯一）
ANCHOR = '<h4 class="text-lg font-semibold mt-4 mb-2">二、操作系统：安卓 VS iOS VS 鸿蒙</h4>'
MARK = '<!-- v19-soc-mechanism-chapter -->'

# 原 h4 编号顺延（只改标题文字，目录/侧边栏不引用）
RENUMBER = [
    ('<h4 class="text-lg font-semibold mt-4 mb-2">二、操作系统：安卓 VS iOS VS 鸿蒙</h4>',
     '<h4 class="text-lg font-semibold mt-4 mb-2">三、操作系统：安卓 VS iOS VS 鸿蒙</h4>'),
    ('<h4 class="text-lg font-semibold mt-4 mb-2">三、手机接口全解析</h4>',
     '<h4 class="text-lg font-semibold mt-4 mb-2">四、手机接口全解析</h4>'),
    ('<h4 class="text-lg font-semibold mt-4 mb-2">四、手机产品体系与命名规则</h4>',
     '<h4 class="text-lg font-semibold mt-4 mb-2">五、手机产品体系与命名规则</h4>'),
    ('<h4 class="text-lg font-semibold mt-4 mb-2">五、基带与天线：手机通信的幕后功臣</h4>',
     '<h4 class="text-lg font-semibold mt-4 mb-2">六、基带与天线：手机通信的幕后功臣</h4>'),
    ('<h4 class="text-lg font-semibold mt-4 mb-2">六、你的手机，到底在扮演多少角色？</h4>',
     '<h4 class="text-lg font-semibold mt-4 mb-2">七、你的手机，到底在扮演多少角色？</h4>'),
]
