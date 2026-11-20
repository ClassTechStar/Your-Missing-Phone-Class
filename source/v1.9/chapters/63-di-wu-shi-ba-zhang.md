---
id: di-wu-shi-ba-zhang
num: 58
part: an-zhuo-kai-fa-pian
nav: 第五十八章：速查手册与资源
toc: default
kind: chapter
---

### 第五十八章：速查手册与资源

{class="chapter-intro mb-4"}
本章是一份可以独立使用的速查手册。当你记不清某个写法或需要快速决策时，直接翻到这里。建议把它当成"口袋卡片"：常用代码速查、常见问题、学习资源，一页不落。

::: div .quick-read
##### 本章速读（5 分钟版）
这一章不是课，是一份可以独立使用的速查手册：写代码卡住的那一刻，直接翻到这里就行。里面是几张"口袋卡片"：常用代码速查卡、常见问题 FAQ、推荐学习资源、Gradle 命令速查、版本对照、术语速查表。快捷键、常用依赖、环境与构建故障速查。它的价值不在读，在翻：<strong>报错时翻故障表，写卡住时翻速查卡，开新项目前翻依赖和版本表</strong>。一页不落，随用随查。

最关键的有两条用法。第一，<strong>按动作查，别按名词查</strong>：你脑子里的问题是"我想跳到另一个页面"，不是"Navigation 架构组件是什么"：从动作出发在卡上对号入座，十秒拿到写法，比翻回前面几章快得多。第二，速查卡救急不救命：它告诉你怎么写，不告诉你为什么这么写。右列代码要是像看天书，别硬抄，回对应章节读五分钟，比抄错代码排查两小时划算多了。还有个规律送你：你反复查的那几行，恰恰是没真正学会的那几行：这不是麻烦，是卡片在帮你精准定位薄弱点。

今天就能做的最小动作：把速查卡打印出来（或者手抄一遍）放书桌边，开始给用过的行画勾做记号。两周之后回头看，记号最多的那几行就是你这个阶段真正常用的本领，这张卡就变成了你的"使用地图"。顺手立个月度习惯：每月挑一天花十分钟，把版本对照表和官方发布页对一遍、翻翻错题本，让手册始终是"现行地图"，不是一年前的旧地图。

最大的坑是把手册用反了。有人把十二行速查当课文背，刻意背代码是最慢的路，查得多了自然就记住了；有人查完不消化，抄完说不清"这行代码改变了什么"，那只是抄写员；还有人明知看不懂还整行照抄、改一个字母就崩。出现这些信号就该停止查卡、回去补课。手册里还替你排了新手最常写错的五个写法：在界面函数里直接发网络请求、什么都往 rememberSaveable 里塞、数据变了界面不动（忘了接数据流）、几百条数据塞进 Column、列表每项里做重复计算。照单自查一遍，能挡掉大部分低级错误。
##### 速查表
- 手册怎么翻：报错翻故障表，卡住翻速查卡，开新项目前翻依赖和版本表
- 查卡的姿势：按动作查不按名词查，十秒定位写法
- 抄完必问一句：这行代码改变了什么？答不上就等于没学会
- 什么时候回炉：同一行一周查五次、改个字母就崩，回去补那一节
- 新手五大错写法：界面里发请求、滥用 rememberSaveable、忘接数据流、长列表用 Column、每项重复计算
- 命令行怎么用：永远用 ./gradlew，报错原文整段取下来再求助
- 版本怎么管：每月花十分钟对一遍官方发布页，升级小步慢跑
- 查卡丢不丢人：写十年代码的人桌上也贴小抄，该担心的是查完不消化
:::

<div class="version-anchor">本章界面路径按 iOS 18.x / HarmonyOS 5.x / Android 15 核对（2026 年 11 月）。你的机型或系统版本不同，菜单名字和位置可能对不上——以你手机上显示的为准。</div>


#### 一、常用代码速查卡

先把这张卡的用法说清楚：它不是拿来从头读到尾的，而是拿来"查"的。你写代码卡住的那一刻，脑子里的问题几乎都是一个动作，"我想记住一个数""我想跳到另一个页面""我想在后台下载点东西"。从左列找到那个动作，右列就是写法。整个过程不超过十秒，比翻回前面几章快得多。

丑话也说在前面：<strong>速查卡救急不救命</strong>。它告诉你"怎么写"，不告诉你"为什么这么写"。如果你看着右列的代码像看天书，别硬抄，回到对应章节把那一节读完再回来，五分钟的事，比抄错代码排查两小时划算多了。查卡查多了你会发现一个规律：你反复查的那几行，恰恰是你没真正学会的那几行。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要做什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">关键代码</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">记住一个可变状态</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">var x by remember { mutableStateOf(初值) }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">转屏不丢状态</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">rememberSaveable { mutableStateOf(初值) }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">竖排/横排布局</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Column { }</code> / <code class="inline">Row { }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">懒加载列表</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">LazyColumn { items(列表) { ... } }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">页面跳转</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">navController.navigate("路由")</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">协程里干等活儿</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">viewModelScope.launch { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">观察数据流</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">val list by flow.collectAsState()</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">存小配置</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">context.dataStore.edit { it[KEY] = 值 }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">存结构化数据</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room 三件套：@Entity / @Dao / @Database</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">联网取数据</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit 接口 + suspend 函数</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">发通知</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">NotificationChannel + NotificationCompat.Builder</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">打日志</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Log.d("TAG", "message")</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
安卓开发速查卡（2026 年 8 月版）

##### 这张卡怎么用：三个习惯

<strong>习惯一：按动作查，别按名词查</strong>。你脑子里的疑问是"页面跳转怎么做"，不是"Navigation 架构组件是什么"。从左列的动作出发查卡，永远比从右列的术语出发反推快。以后查官方文档也一样：搜索框里输动作，输出来的答案才能直接用。

<strong>习惯二：抄完多看一眼</strong>。每次从卡上抄完代码，花十秒问自己一句："这行代码改变了什么？"是记住了一个值，还是触发了一次跳转，还是把活儿派去了后台？能答上来，这行代码才是你的；答不上来，你只是个抄写员，下次还得回来抄。

<strong>习惯三：给用过的行做标记</strong>。打印出来画勾也行，抄进笔记软件打星也行。两周之后回头看，留下痕迹最多的那几行，就是你这个阶段真正常用的 API——而一行都没用过的，说明你还没走到那一步，别急着学。这张卡会慢慢变成你的"使用地图"，比任何推荐清单都准。

##### 逐行拆解：这十二个写法到底在干什么

光抄不够，得知道每行代码"是个什么东西"。下面按功能把它们分成四组，用大白话各过一遍。

<strong>状态与界面四件套</strong>（remember、rememberSaveable、Column/Row、LazyColumn）。remember 是给变量配了个"随身记事本"：界面每刷新一次，界面函数就会整个重新执行一遍，没有这本记事本，你刚输入的数字、刚点选的开关，刷新一次就归零。rememberSaveable 是能扛住转屏的加强版记事本——屏幕一转，界面重建，普通记事本会被撕掉，它的内容还在。Column 和 Row 是排版的两个基本动作：一个往下排，一个往右排，所有复杂界面都是它们套出来的。LazyColumn 是"滚到哪画到哪"的列表：一千条记录不会一次性全画出来，只画屏幕里的那十几条——这也是它和普通 Column 的本质区别。

<strong>页面跳转</strong>（navigate）。把 App 想成一栋楼，每个页面是一间房，路由就是门牌号。navigate("路由") 就是从当前房间走到另一间。参数怎么带、怎么返回，第三篇讲 Navigation 的章节里有完整的门牌号命名规则，这里只留"走房间"这个动作。

<strong>数据与后台</strong>（launch、collectAsState、dataStore、Room、Retrofit）。viewModelScope.launch 是"派个工人去干活"：下载、查库这类耗时活，交给后台去干，别堵在门口（主线程）让界面卡住。collectAsState 是"把水管接进水龙头"——后台的数据流一有新水，界面水龙头自动出水；忘了接水管，是新手最常见的"数据明明变了，界面纹丝不动"惨案的直接原因。dataStore.edit 存的是钥匙串一样的小配置：开关、主题、上次选的标签。Room 是"带表格的仓库"，Entity 定义表、Dao 定义存取动作、Database 是仓库总门。Retrofit 是"跑腿取数的快递员"：你描述要访问哪个网址、要什么数据，它负责跑一趟带回来。

<strong>系统能力</strong>（Notification、Log）。发通知前必须先建渠道（NotificationChannel），这是系统规定，没有渠道的通知发不出去；NotificationCompat.Builder 负责把通知内容装起来。Log.d 是写日志——调试时你唯一的"黑匣子"，App 在你手机上跑的时候，只有它知道里面发生了什么。

##### 三个最小可跑片段：照着敲一遍

卡片上的写法是"单词"，下面这三段是"短句"，每个都能单独跑起来，合在一起就是一个能点、能滚、能取数的小程序。别复制粘贴，手敲一遍，感受比看十遍都深。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 最小的状态例子</span><span class="dots">···</span>
:::

```
var count by remember { mutableStateOf(0) }

Column {
    Text("你点了 $count 次")
    Button(onClick = { count++ }) {
        Text("点我加一")
    }
}
```
:::

十行，浓缩了卡片前两行和第三行的全部内容。点按钮，count 变，界面自动重画：remember 负责"记住"，mutableStateOf 负责"变了就通知"。你可以做个实验：把 remember 拿掉再跑，按钮会变成摆设，怎么点数字都不动。亲手踩一次这个坑，你对状态的理解就永久到账了。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 最小的列表例子</span><span class="dots">···</span>
:::

```
val words = listOf("安卓", "Kotlin", "Compose")

LazyColumn {
    items(words) { word ->
        Text(word)
    }
}
```
:::

列表也简单得过分：一组数据，一个 items，每条怎么显示你说了算。把 listOf 里的词换成你的记账记录、待办事项，它就是真实 App 的雏形。想验证 LazyColumn 的"懒"，把三个词换成一千条，界面照样流畅，换回普通 Column 试试，模拟器会给你上一课。

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 最小的后台取数例子</span><span class="dots">···</span>
:::

```
fun loadWeather() {
    viewModelScope.launch {
        try {
            val result = api.getWeather("北京")
            _uiState.value = result
        } catch (e: Exception) {
            Log.d("Weather", "取数失败", e)
        }
    }
}
```
:::

这段放 ViewModel 里。launch 派工人去后台干活，try-catch 兜住网络那说不准的脾气，Log.d 把失败原因写进黑匣子。三样东西各司其职，网络请求永远会失败，区别只是有没有人接住它。新手常犯的错是把这段塞进界面函数里。那就是前面"错一"说的翻车现场。

##### 场景案例：周五晚上，一个班级投票小工具

看看这张卡在真实任务里怎么串起来。周五晚上十点，班长在群里说：明天班团活动要现场投票选节目，纸质举手太乱，你能不能做个投票小页面？时间只有一小时，要求：三个候选节目，每人投一票，投完能看到实时票数。

打开速查卡，五步就够。第一步，三个选项的票数用 remember 记住（第一行）；第二步，候选节目用 LazyColumn 列出来（第四行）。第三步，每行放个按钮。点击把对应票数加一：还是第一行的写法；第四步，防止同一个人反复点。把"已投票"标记存进 DataStore（第八行）；第五步，投票截止时发条通知提醒大家看结果（第十一行）。一个小时不到，工具做出来了，第二天现场用得挺顺。

这个例子的重点不在工具本身，而在<strong>思路</strong>：任何需求到了你手里，先拆成卡片上的"动作"，再逐个实现。速查卡的本质是一份"能力清单"，你每多掌握一行，能拆解的需求就多一类。十二行全装进口袋，日常小工具就拦不住你了。

先拆动作。

##### 五个关于"速查"的误解

- <strong>误解一：这十二行得背下来才算入门</strong>。不用。查得多了自然就记住了，刻意背代码是最慢的一条路。背下来的代价是背了又忘，查出来的收获是用了就熟。
- <strong>误解二：卡上的写法永远是最佳答案</strong>。不是。卡片给的是"最常用、最稳"的写法，不是唯一写法。同一件事往往有三种写法，先掌握卡上的那种，其他等你用到时自然会遇到。
- <strong>误解三：查卡说明你学得差</strong>。恰恰相反。写了十年代码的人桌上也贴着小抄，查卡是职业习惯，不是新手耻辱。真正该担心的不是查，是查完不消化。
- <strong>误解四：写法越长越厉害</strong>。反了。能用三行解决的事写三十行，不是本事是负担。看到"超长写法"先怀疑自己没理解需求，再怀疑对方在炫技。
- <strong>误解五：学完就可以把卡扔了</strong>。别扔。三个月后你换了场景——从记账本换到天气项目，有些行又要回来查。这张卡的归宿是书桌角落，不是垃圾桶。

##### 什么时候该停止查卡，回去补课

查卡是补丁，章节才是布料。出现下面任何一个信号，说明你该回头补课，而不是继续查：同一行写法一周内查了五次以上；抄完的代码说不清"它改变了什么"；或者改动一个字母就崩，只能整行整行照抄。这些是地基没打牢的表现。别焦虑：速查卡帮你定位了薄弱点，比自己瞎摸索省事得多。回对应章节读一节，做一遍练习，再回来，那一行就长在了手上。

查，不是背。

<div class="stance-box">
<div class="stance-box-head">作者立场</div>
<p>结论：卡是查的，不是背的；但同一行一周内查了五次以上，就停下来回去补课。</p>
<ul>
<li>刻意背代码是最慢的一条路，写了十年代码的人桌上也贴着小抄，查卡是职业习惯，不是新手耻辱；</li>
<li>抄完说不清"它改变了什么"、改一个字母就崩，说明地基没打牢，继续查只会更慢；</li>
<li>速查卡真正的用法是"先想清楚每一小块该用哪一行"，而不是把十二行全背下来。</li>
</ul>
<p class="stance-box-note">（无利益相关。以上是机制上的判断。）</p>
</div>


##### 新手最常写错的五个写法

<strong>错一：在界面函数里直接发网络请求</strong>。界面函数可能被执行很多次，你把请求写在里面，等于让快递员同一单跑十趟——流量翻倍，界面还卡。纠正：请求放进 ViewModel，用 launch 包起来，界面只管显示结果。

<strong>错二：全用 rememberSaveable</strong>。转屏不丢状态是好事，但保存是有代价的，什么值都往里塞，保存动作本身就变重了。纠正：只在界面刷新中"可能丢"的值用 remember；确实需要扛住转屏、扛住进程回收的，才用 rememberSaveable。

<strong>错三：数据变了界面不动</strong>。九成是忘了 collectAsState——水管没接，水再多水龙头也不出水。纠正：检查 ViewModel 里暴露的数据流，是不是用 collectAsState（或类似函数）接进了界面。

<strong>错四：把几百条数据塞进 Column</strong>。Column 会把每一条都画出来，数据一多界面直接掉帧。纠正：能滚动的长列表一律用 LazyColumn，一行代码的事。

<strong>错五：在列表每一项里做重复计算</strong>。日期格式化、排序、字符串拼接这类活儿，写在每一项的渲染代码里，就会随滚动反复执行。纠正：提到列表外面算一次，存进变量，列表里直接用。

<div class="case-box">
<div class="case-box-head">翻车现场</div>
<p>列表页做完了，点一下"投票 +1"，票数不动，日志里也没有报错。你把 ViewModel 里的数据打印了三遍，它确实变了。最后发现界面里直接读了 ViewModel 的普通属性，而不是数据流：数据在管道里流过去了，水龙头却没接上。</p>
<p class="case-box-quote">"数据改了，界面就是不动"</p>
<p class="case-box-src">场景来源：全书通用场景（非特定读者）</p>
<p><strong>怎么办</strong>：九成是忘了 collectAsState。检查 ViewModel 暴露的是不是数据流，界面有没有用 collectAsState（或同类函数）接进来。接上水龙头，界面立刻跟着动。</p>
</div>


::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>避坑提醒：别把"能跑"当"会了"

{class="mt-1"}
速查卡抄来的代码能跑，不代表你下次能独立写出来。检验标准很简单：关掉卡片，在空文件里把它默写出来，再跑一遍。默写不出来就回头看上面的拆解，再来一次。这一下"主动回忆"比抄十遍都有用，它难受，但难受的部分才是学习发生的部分。
:::

##### 场景案例：给爸妈的用药提醒

再走一遍思路，这次的对象是爸妈。春节回家，你发现爸爸的老花镜片后压着一张手写的服药清单，早晚各一次，三种药，看得你心里一酸。你打算做一个用药提醒 App，还是打开速查卡拆动作。

药名和服药时间，是"带表格的数据"，用 Room 存（第九行）；"今天早上吃过了没"，是个小标记，DataStore 就够（第八行）；到点了弹提醒，通知能力（第十一行），记得渠道名写得明白点，"用药提醒"，别叫什么"channel_01"，爸妈看不懂；列表界面 LazyColumn（第四行），每行一个"已服用"按钮，点了就把今天的标记改掉。四个下午做完，寒假结束前装进爸妈手机。

这个案例和投票工具用的还是同一张卡，拆出来的动作却完全不同，这就是速查卡真正的用法：<strong>它不告诉你该做什么 App，它只保证你想做的每一小块，都有现成的路可以走</strong>。路是现成的，方向得你自己定，而方向，恰恰是你家里那些真实的需求。

默写一遍。

##### 把卡上的写法改成你自己的

最后提醒一件抄卡时容易忽略的事：卡上的代码里有不少占位写法："初值""路由""列表"，照抄能跑，但正式项目里别这么留。初值是什么？路由叫什么名字？列表装的是什么？用含义清楚的名字替换它们。命名这件事说大不大，说小不小：三周后回头改 bug，变量名清楚的项目，你读自己代码像读别人写的攻略；名字乱起的项目，像读自己三个月前的日记。

注释同理。不用写满屏，只在两个地方落笔：这行代码"为什么存在"，以及"改这里之前先看看哪里"。写给谁看？写给三个月后忘了上下文的你自己。你会感谢现在的你。

##### 从速查卡到肌肉记忆：两周刻意练习

第一周，每天固定二十分钟，用这张卡写小练习：今天一个开关按钮，明天一个列表，后天一个计时器。写不出来就查卡，查完接着写。第二周，规则改一条：合上卡片，把昨天写过的东西重写一遍，实在卡住了才允许翻卡。到周末盘点，翻卡翻得最多的三行，就是你的薄弱点：回到对应章节，把那节重新读一遍。

这套流程不新奇，但真的管用。语法这东西，看会了和手会了之间隔着一道墙，而砌墙的砖只能是重复。两周之后你再看这张卡，会发现要查的行越来越少，那不是卡片失效了，是你出师了。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：把速查卡变成你的"错题本"

{class="mt-1"}
把本章的速查卡打印出来，或者抄进你的笔记软件。本周每次写代码前，先盖住右列，凭记忆把要用的写法写出来，再对照检查，错了就在那一行旁边画一笔。两周后数一数哪行画得最多，那就是你接下来要重点补的写法。这张画满记号的卡片，比任何新买的教程都值钱。
:::

#### 二、常见问题 FAQ

问答是最耐翻的形式，你现在心里冒出来的疑问，大概率就躺在下面。前面五问是这本书的读者问得最多的，先答它们；从第六问开始，是写作过程中又反复被问到的。问题都带着真实的情绪和错误的预设。答案尽量不绕弯子。

<strong>Q1：我完全不会编程，学安卓开发要多久？</strong>

按本书路径走：第 1-2 周装环境、学 Kotlin 基础；接着是第 3-4 周，学 Compose 做出界面；第 5-6 周完成记账本项目；第 7-8 周做完天气项目。<strong>两个月，从零到能独立做小 App</strong>。前提是每天投入 1-2 小时，且动手敲代码而不是只看书。

<strong>Q2：Java 还要学吗？</strong>

不用。新项目、新教程、新岗位基本都以 Kotlin 为准。只在"维护十年老项目"时才会遇到大量 Java。学完 Kotlin 后如果工作需要，再补 Java 会很快，两者底层是同一个虚拟机生态。

<strong>Q3：模拟器还是真机？</strong>

开发调试用模拟器方便（快照、多机型），但<strong>验收必须过真机</strong>——触感、性能、真网络、传感器，模拟器替代不了。条件允许，买一台中端真机当测试机，是最划算的投资。

<strong>Q4：安卓开发好找工作吗？</strong>

2026 年的行情：纯"会写界面"的初级岗位竞争激烈，但"懂 Kotlin + 会架构 + 有上线作品"的开发者依然抢手。学习期的你，<strong>最好的简历就是商店里那个自己做的 App</strong>。

<strong>Q5：遇到报错卡住了怎么办？</strong>

黄金三步：① 把报错第一行原样搜 StackOverflow/搜索引擎；② 查官方文档对应页面；③ 还不行，就把"期望行为 + 实际现象 + 报错全文 + 相关代码"打包发给 AI 或社区提问。绝大多数问题，第一步就解决了。

<strong>Q6：我数学不好，英语也一般，能学安卓开发吗？</strong>

能。做 App 用到的数学，大部分停在加减乘除和"如果……就……"的逻辑判断上，界面开发的日常根本碰不到高数。英语方面，报错和文档确实多是英文，但你只需要认识几十个高频词，error、cannot find、version、permission，剩下的交给翻译软件。真正卡住人的从来不是数学和英语，是"看到报错就慌"的心态。报错不是骂你，是系统在给你指路。

<strong>Q7：我的电脑配置一般，跑不动模拟器怎么办？</strong>

三条路，按顺序试。① 降低模拟器配置：新建虚拟设备时别选最新旗舰机型，挑一台低分辨率的旧机型，很多"跑不动"其实是配置选太高。② 直接用真机调试：手机打开开发者选项和 USB 调试，插上线就能跑，体验反而更真实。③ 实在不行，先在 Kotlin 官网的在线演练场练语法，界面部分等条件够了再补。中端真机加普通电脑，足够走完本书八周的全部练习。

<strong>Q8：能不能跳过 Kotlin 直接学 Compose？</strong>

不建议。Compose 的每个界面都是 Kotlin 函数，语法看不懂，你连代码都抄不对位置。Kotlin 基础大约两周，变量、函数、条件判断、集合操作，这套东西练扎实了，Compose 对你来说只是"把函数变成界面"的新规则，学起来非常快。反过来跳过基础直接上 Compose，你会在第三天遇到第一个 lambda 表达式时卡死，然后开始怀疑人生。

<strong>Q9：教程跟着敲都能跑，自己动手就懵，是不是我不适合学编程？</strong>

这叫"教程陷阱"，几乎每个人都掉进去过，跟天赋无关。跟教程敲代码时，你的大脑在做"听写"；自己写时要做"作文"：两回事。解法只有一个：把教程项目关掉，凭理解重做一遍，哪怕做得更丑；然后给它加一个教程没有的功能。第二遍的痛苦是真实的学习，第一遍的顺畅只是幻觉。能在痛苦里待住的人，都学会了。

<strong>Q10：AI 都能写代码了，现在花两个月学安卓还有意义吗？</strong>

恰恰因为 AI 会写代码，"会指挥 AI"才成了新的门槛。AI 能替你敲键盘，替不了你看懂报错、判断方案好坏、决定功能取舍，而这些判断力，恰恰来自你自己写代码的积累。本书第七篇（第 37-47 章）整篇都在讲怎么把 AI 用成放大器，但你得先有东西可放大。两个月学的是判断力，不是打字速度；工具越强，会用工具的人越值钱。

<strong>Q11：学完只能做记账本和天气这种小 App 吗？</strong>

记账本和天气是练习用的小台阶，不是天花板。这两个项目覆盖的技能：界面、数据库、网络、后台任务、上架，组合起来能做的远不止这些：给家里老人做个用药提醒，给自己店里做个记库存的小工具，把单位里重复的统计工作变成一个 App。学完的标志不是"会做记账本"。学完的标志是你遇到生活中的重复劳动时，会下意识想一句：能不能写个东西解决它？

<strong>Q12：要不要一开始就学架构、依赖注入、模块化这些"高级"内容？</strong>

不要，至少现在不要。这些是"项目变大之后"的解药，你还没病，先别吃药。一个人、几千行代码的项目，最朴素的写法就是最好的写法。等你被真实的痛点反复折磨：改一处崩三处、代码找不到在哪，再回去读第 57 章的架构内容，那时候你会觉得每个字都说到心坎里。提前学架构，就像背下了整本菜谱却从没开过火。

<strong>Q13：报错全是英文红字，看都看不懂，有没有固定的应对流程？</strong>

有，三步。① 找到<strong>第一条</strong>红色报错，不是最后一条，后面的往往是连锁反应，第一条才是病根。② 把它整段复制，丢给搜索引擎或 AI，加一句"用中文解释原因和解决办法"。③ 按建议改<strong>一处</strong>，重新构建。一次只改一处，改完立刻验证。本手册后面专门有一节"环境与构建故障速查"，把最高频的十来种报错整理成了表格，对号入座就能用。

<strong>Q14：需要顺便学 Git 吗？还是先把编程练好再说？</strong>

早晚要学，但起步阶段可以缓。学习期最要紧的是"每天能写出一个能跑的小功能"，Git 解决的是另一个问题，"改坏了想回到昨天怎么办"。等你写出第一次"真想穿越回去"的代码，再花一个晚上学最基本的三招：保存一个版本、看历史、回到过去。想系统学，第二十三章附的 GitHub 入门指南就是现成的起点。那里连"为什么要有版本管理"都讲清楚了。

<strong>Q15：App 的名字和包名现在就要定好吗？</strong>

不用都定。应用名（手机桌面上显示的那个）随时能改，想好了随时换。包名不一样，它是 App 的"身份证号"，上架之后就得稳定下来，改一次等于换一个 App。所以练习项目直接用新建项目时默认的就行，等真要上架了，再认真取一个不会后悔的。

<strong>Q16：数据到底该存在哪？感觉有好几种存法，选哪个？</strong>

按数据的"块头"选，别纠结。开关、主题、上次选的标签这类小配置，用 DataStore（第八行）；能列成表格的数据：账目、待办、联系人——用 Room（第九行）；文件、图片这类大块头，先存本地。需要多设备同步时再考虑云端。新手最常见的错误是想太远："万一以后要同步怎么办？"先让数据在本地活下来，同步是数据活下来之后的事。

<strong>Q17：要不要顺便啃数据结构与算法？听说面试要考。</strong>

分阶段。做小 App 的日常，用到的数据结构就是列表和映射表，算法几乎碰不到。起步期啃大部头，性价比极低，还容易把热情啃没。但"知道有这么回事"很重要：列表为什么查询慢、哈希是什么思路，这些概念能让你在排查卡顿时快很多。建议的节奏：跟着项目遇到什么学什么，等你能独立做完 App 了，再回头系统补：那时你学的每个结构都能立刻在项目里找到影子，记得牢十倍。

<strong>Q18：项目做着做着代码就乱了，怎么避免？</strong>

三个习惯，成本极低。① 一条铁律：界面函数只管显示，逻辑一律进 ViewModel，乱掉的根源几乎都是把活儿堆在了界面里。② 每做出一个小功能就存个版本，随手点一下的事，给你留的是"随便折腾"的底气。③ 每周花十分钟删代码：删掉没用的文件、注释、试错代码。乱是累积出来的，勤删就不会烂尾。

<strong>Q19：学到第四五周，突然忙了/累了，中断了怎么办？</strong>

中断不可怕，可怕的是中断后的"重启成本"让你再也不想碰。两个对策。第一，给自己留"重启入口"：每次收工前，在代码里留一条注释，写清"下次从哪继续、下一步要干什么"，三个星期后的你对现在的记忆是零，这条注释就是留给那个陌生人的。第二，降低重启门槛：回来那天的目标定小一点，小到"跑通上周的代码"就行，别一上来就啃新内容。断两周回来，两三天就能续上，别让负罪感把你劝退。

<strong>Q20：学习期间要不要花钱买设备、买课、买服务器？</strong>

按必要性排序。一台中端安卓真机（用于真机调试）值得，前面 Q3 说过理由；一台好电脑不必。普通电脑配真机调试，八周课程吃得下；付费课程谨慎，官方 Codelabs 和这本书已经覆盖了起步路径。先把手头的免费资源用透再谈买。至于服务器，起步阶段的 App 用本地存储就够，真有联网后端的需求了再研究不迟。学编程的第一年，最贵的成本不该花在设备上，是"觉得装备不齐所以没开始"的那段时间。

<strong>Q21：八周学完之后，接下来该往哪走？</strong>

三个方向，按需选一个。深的那条：回第 57 章把架构那套补上，再试着给自己的 App 加测试，这两样是"能做出"到"做得好"的分水岭。宽的那条：第九篇的 iOS 篇在等你，编程思路相通，学起来比第一遍快得多。快的那条：回到第七篇（第 37-47 章），把 AI 协作的方法论用进你的下一个项目：从零到一你已经走完，从一到十，AI 能陪你跑得更快。三个方向不冲突，但一次只选一个，别贪。

##### 提问的姿势：同一个问题，问法不同，答案天差地别

先看一组对比。"大佬们，我的 App 怎么都跑不起来，急急急"，这种问题发出去，大概率石沉大海：别人连你用的什么版本、报了什么错都不知道，想帮都无从下手。换一种写法："在 Windows 11、Android Studio 最新稳定版、模拟器 API 34 的环境下，点击按钮后我期望跳转到第二个页面，实际闪退，报错全文如下，代码只有 20 行如下"，同样的困惑，第二种问法通常十几分钟内就有回应。

模板就四样东西：<strong>环境</strong>（系统、IDE 版本、真机还是模拟器）、<strong>期望</strong>（我想实现什么）、<strong>实际</strong>（发生了什么）、<strong>最小复现</strong>（能触发问题的最少步骤和代码）。发给人用这套，发给 AI 也用这套，差别是 AI 不会烦，人会。发出去之前自己先读一遍："如果我是被问的人，凭这几行字能复现问题吗？"能，就发；不能，回炉。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：把求救卡片贴在墙上

{class="mt-1"}
Q5 的黄金三步，加上这节的提问模板，合起来就是一张"求救卡片"。打印出来贴在显示器旁边。学编程的第一年，你求救的次数比想象中多，而求救的质量，几乎决定了你解卡的速度。
:::

##### 场景复盘：凌晨一点的两次求助

同一个夜晚，同一个人，两次求助，两种结局。凌晨一点，小周的天气 App 打包时突然报错，明天一早要给社团演示。第一次求助，他在学习群里发："救命，打包不了，谁懂啊"，十分钟后，群里安静如常，大家甚至不知道他用的是 Windows 还是 Mac。退而求其次去问 AI，得到的建议方向对了一半，但他没提供报错原文，AI 只能盲猜。

凌晨一点半，他回到这条 FAQ，照着模板重新组织了问题：Windows 11、Android Studio 稳定版、模拟器 API 34，执行打包命令，期望生成安装包，实际报错，报错第一行如下，完整日志如下。这次他把同样的内容先发给了 AI，几乎立刻收到了三个可能原因和对应的检查方法；顺着第二条，他发现是某个依赖的版本写错了。一点五十，打包成功，睡觉。

两次求助之间隔了半小时，差的不是运气，是信息量：第一次那句"救命，打包不了，谁懂啊"给了对方零条可判断的依据，第二次那串带版本号、带报错第一行、带完整日志的信息，给了三条。<strong>求助的效率，取决于你给了对方多少可判断的依据</strong>。这个教训值多少个凌晨？你自己算。

#### 三、推荐学习资源

先说这张表的排序逻辑：<strong>官方永远排第一</strong>。网上资料再多，都绕不开一个事实：框架一升级，教程就可能过时，唯一和工具同步更新的只有官方文档。遇到任何"教程和实际对不上"的情况，别怀疑自己手抖，先怀疑资料的新鲜度，然后以官方为准。

第二原则：资源在精不在多。这张表里的每一项都值得你用上一个月，而不是每项都点开收藏，然后一个都没打开过。收藏夹不等于学会了，这句话专门写给所有和我一样爱囤资料的读者，包括我自己。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">类型</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">资源</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">推荐理由</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">developer.android.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">安卓官方文档，Compose/Kotlin 教程都在里面，第一权威</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin 官网 (kotlinlang.org)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">语言官方文档 + 在线演练场</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Google Codelabs</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">手把手的分步实验课，新手友好度满分</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">社区</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stack Overflow (android 标签)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">报错求救第一站</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">社区</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">掘金 / CSDN 安卓专区</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">中文实战文章多，注意甄别新旧（先看日期）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">视频</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Google Developers 官方频道</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每年的开发者大会新技术讲解</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">配套</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第七篇《AI编程实战篇》（第37-47章）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用 AI 辅助安卓开发的完整心法</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
安卓开发学习资源清单（2026 年 8 月）

##### 官方文档怎么读：三个立刻能用的技巧

<strong>技巧一：用 site 限定搜索</strong>。在搜索引擎里把问题加上"site:developer.android.com"，等于只在这个网站里找——全网的海量噪音一下就被过滤掉了，出来的结果条条都是官方原声。查 Kotlin 语法就把域名换成 kotlinlang.org，一个技巧吃遍两个官方站。

<strong>技巧二：先找示例，再读说明</strong>。官方页面的代码示例通常是完整可跑的片段。对新手来说，"先把示例抄通跑起来"再回头读文字说明，效率比反过来高得多——代码跑通了，文字里的每个词就都有了着落；没跑过代码直接读文档，看三行就走神。

<strong>技巧三：认准版本选择器</strong>。很多文档页面角落有版本切换。你按文档写，编译器却说"这个写法不存在了"，八成是文档版本和你工程的版本对不上。先看版本，再对答案——这条能省掉新手期一半的自我怀疑。

##### 中文资料怎么甄别：看五样东西

中文实战文章读起来亲切，质量却参差不齐，教你五招快速验货。

- <strong>看日期</strong>：超过两三年的 Compose 教程要警惕，那正是它大改版的时期，旧写法可能已经被废弃。
- <strong>看版本号</strong>：教程里写了具体版本号的，先对照官方现在的稳定版，差得远就要留心。
- <strong>看评论区</strong>：高赞的纠错评论是宝藏，一条"现在应该用 XX 写法"能救你半小时。
- <strong>看作者</strong>：点进主页翻一翻，持续更新的作者，文章可信度远高于三年一更的号。
- <strong>亲手跑一遍</strong>：最关键的一步。跑不通的教程再精美也别信，你的时间比它的阅读量值钱。

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>避坑提醒：过时教程是新手最大的坑

{class="mt-1"}
教程里的写法和 IDE 的自动补全对不上号，九成是教程过时了，不是你抄错了。判断方法也简单：IDE 明明认识其他函数，唯独教程里的那个怎么敲都补不出来，八成是它被淘汰了。去官方文档搜一下现在怎么写，别跟过时代码死磕。
:::

##### 视频资源怎么用：当预告片，别当正片

开发者大会的演讲适合"开阔眼界"：每年新东西快速过一遍，知道行业在往哪走，心里有数。但系统学习不能靠视频，视频节奏是别人的，代码密度也低。正确的搭配是：视频当预告片，倍速看，记下感兴趣的技术点；然后回到文档和 Codelabs 当正片，逐行消化。反过来把视频当正片的人，往往看了一年视频，一个完整的 App 都没做出来。

##### 社区提问礼仪：让问题更快被回答的三件事

<strong>搜索先行</strong>。你此刻的报错，大概率在 Stack Overflow 上被人问过，而且下面还挂着一排带对勾的答案。先搜再问，是社区默认的礼貌——直接发问的人，常会被一句"你搜过吗"怼回来，不冤。

<strong>最小复现</strong>。贴十行能复现问题的代码，别贴整个项目。帮你的人时间有限，他要的是"能立刻在你描述的场景里看到同样的错"，不是读你的毕业论文。上一节的提问模板在这里同样适用。

<strong>结帖回贴</strong>。问题解决了，回一句"用第几楼的方法解决的，另外我还改了 XX 才彻底通"。下一个搜到这个帖子的人，会因为你这句话少走半小时弯路。社区的运转靠的就是这个循环——你收过别人的恩惠，记得还回去。

##### AI 时代怎么用学习资源：先问 AI，再查官方

AI 改变的是"查资料"这件事的流程。概念不懂，问 AI，"用做饭的比喻给我讲讲协程"这种要求，人类老师都嫌烦，AI 不会；代码看不懂，贴给 AI 让它逐行解释；方案拿不准，让 AI 列出两三种做法各自的优劣。它是个不知疲倦的助教，随叫随到。

但它有一个你必须知道的毛病：<strong>会一本正经地编</strong>。不存在的函数名、过时的写法、张冠李戴的参数，它都可能出现，而且语气照样笃定。所以规矩只有一条：<strong>AI 给的答案，凡是涉及具体 API 和版本号的，去官方文档验一眼再信</strong>。概念解释可以放心听，具体写法必须过验。

推荐的循环是：AI 解释 → 自己动手试 → 卡住了查官方文档 → 带着文档里的发现再回来问 AI。这个循环跑顺了，你的学习速度会比五年前的任何学习者都快，前提是你没把中间"自己动手试"那一步省掉。省掉它，循环就退化成"问 AI、抄 AI、再问 AI"，学得快，忘得更快。

##### Codelabs：最被低估的新手资源

表格里 Codelabs 那一行值得单独说。它是官方的分步实验课：左边讲解，右边动手，每一步都告诉你"做完应该看到什么"，像教练站在旁边。新手最容易在两个地方摔倒，"环境和教程不一样""照做了一半不知道对没对"，它把这两个坑都填了。一个 Codelab 通常一两个小时，做完就有成品，成就感是实时的。

两个使用提醒。第一，认准页面上的版本说明，太旧的实验（界面和现在的 IDE 差异明显）跳过，找最新的那篇。第二，别只跟着点下一步：做完之后，关掉页面，凭理解把实验里的核心功能重写一遍，这一步把"跟着做过"变成"会做"。几十个 Codelabs 做下来挑着写，你的 Compose 手感会有质的变化。

##### 场景案例：一次完整的查资料过程

把这一节所有资源串进一个真实场景。周四晚上十点，你的天气 App 出了怪事：界面显示正常，但数字半天不刷新，退出重进又有了，典型的"薛定谔的 bug"。下面是完整的一小时排查过程。

第一步，先问 AI（十点零五）：把现象描述给它，"Compose 界面显示正常但数据不自动刷新，collectAsState 已加，可能是什么原因？"AI 给了三个方向：状态没接上、数据流没发射、生命周期问题。第二步，按第一个方向查官方文档（十点十五）：site 限定搜索"collectAsState lifecycle"，翻到官方页面，版本选择器确认和工程一致，读到一个之前忽略的细节，数据流的收集时机和界面生命周期的关系。第三步，对照 Codelabs（十点半）：找到对应实验，人家把收集写在了正确的位置，而你的写法差半行。第四步，还不放心，去 Stack Overflow 搜（十点四十）：找到一个三年前的老帖，症状一模一样，正准备照抄，扫了一眼评论区，高赞纠错说旧写法已废弃，顶楼附了新写法。十点五十分，改完，跑通，数字乖乖自动刷新。

最后一步别省：把这次的坑记进你的资源库第二栏，"数据不自动刷新，收集位置问题，参考链接 xx"。下次再遇到，三十秒解决。你看，这一小时里 AI、官方文档、Codelabs、社区各出场一次，谁也替代不了谁，顺序对了，一小时就够；顺序错了，顺序里的每一步都能耗掉一晚上。

##### 建一个自己的资源库：三栏收藏法

收藏夹用起来，但要讲方法。建三个固定分类：<strong>官方文档</strong>（按主题存，Compose、Room、导航，各存官方入口页）、<strong>解决过的问题</strong>（每条一个链接配一句话："xxx 报错，原因是 yyy"）、<strong>待学清单</strong>（现在没空学、将来想学的）。查过的东西不再搜第二遍，踩过的坑不再踩第二遍，这个库的价值就出来了。

每月清一次：待学清单里两个月没碰的，删掉。别舍不得，囤积是学习的天敌，真正推动你进步的是"正在学的那一个"，不是收藏夹里的三百个。资源库越短，你越清醒。

##### 别忽视身边的教材：你手机里的 App 本身

还有一类资源从不进推荐清单，但你每天都在用：你手机里的每一个 App。看到微信的长按菜单。想想"这个用 Compose 怎么实现"；看到备忘录的滑动删除，想想"状态存在哪、动画怎么触发"；天气 App 的渐变背景，想想"这个用画布能不能画"。不用真的实现，把"拆界面"当成通勤路上的小游戏，一周下来，你对界面的敏感度会上一个台阶。

遇到特别喜欢的交互，截个图存进相册建个"灵感集"。等你开始做自己的项目，这个文件夹就是你的设计师。别人靠临摹名画学画，你可以靠拆解好 App 学界面——学费为零，样本还是你亲自用过、真心喜欢的。

##### 这张表会过时，筛选原则不会

最后说句实话：上面表格里的具体网站，五年后未必还是最优选，资源本身也有生命周期。但这一节讲的所有筛选原则， 过时得很慢：官方优先、看日期、看评论区、亲手跑一遍、AI 解释加官方验证、收藏分栏月月清。原则是渔，资源是鱼；鱼会换，渔跟着你。哪天你发现新的好资源，用这几条原则过一遍筛子，再决定要不要让进你的库。

#### 四、Gradle 常用命令速查

平时点按钮就够，但命令行有时更高效（尤其是配合 AI 工具或 CI 流水线时）：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">命令</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">作用</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew assembleDebug</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">打一个调试版 APK（Windows 把 ./ 去掉）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew assembleRelease</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">打发布版（需配好签名）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew test</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跑全部单元测试</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew lint</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">静态检查：找出潜在 bug 和不规范写法</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew clean</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">清空构建产物（"重启大法"的编译版）</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew :app:dependencies</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">查看依赖树（排查版本冲突神器）</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Gradle 常用命令速查

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：构建出问题先 clean

{class="mt-1"}
"昨天还能跑今天就不行"的灵异事件，十有六七是构建缓存错乱。<code class="inline">./gradlew clean</code> 之后重新构建，能治愈一大半玄学问题。还不行再重启 Android Studio：这招请配合 File → Invalidate Caches 一起服用。
:::

##### 为什么命令行值得学：三个真实场景

<strong>场景一：AI 工具在终端里跑构建</strong>。第七篇你会看到，AI 编程工具动不动就在终端里执行命令。它跑 <code class="inline">assembleDebug</code> 时你盯着屏幕，看不懂输出，就只能干等着它"自言自语"——看得懂，你才能在它跑偏的第一时间喊停。命令行是你和 AI 协作时的共同语言。

<strong>场景二：报错信息更完整</strong>。IDE 的构建窗口经常把长报错折叠、截断，你看到的是"半句话"；命令行输出从头到尾一屏到底，第一行红字、中间的警告、结尾的总结都在。很多"IDE 里查不出的问题"，把命令贴进终端一跑就现了原形。

<strong>场景三：自动化的一切起点</strong>。哪天你想让项目定时打包、自动检查、一键发布，这些流程的每一块砖都是本章这几条命令。先会手动跑，才谈得上自动跑——顺序反不了的。

##### 看懂一屏输出：三层结构

命令行跑起来会刷一大屏字，新手容易直接吓退。其实输出就三层。最底下是<strong>结论层</strong>：BUILD SUCCESSFUL 还是 BUILD FAILED，一个词定生死，先看这里。中间一大段 task 名字是<strong>过程层</strong>——它干了什么、干到哪了，平时不用细看，卡住的时候才有用。失败了，重点找<strong>原因层</strong>："What went wrong"（哪里错了）和紧跟着的第一处 "Caused by"（根因）：注意是第一处，后面往往是一串连锁反应，老规矩：第一条红字才是病根。

把这三层的顺序记住，命令行就从"吓人的瀑布"变成了"有条理的报告"。你不需要看懂每一行，你只需要知道该看哪几行。

##### ./gradlew 和 gradle 的区别：永远用前者

表里的命令都带个 gradlew，它是"包装器"（Wrapper），项目自带的启动器，里面写明了这个项目该用哪个版本的 Gradle。你敲 gradlew，它按项目规定的版本去跑：换电脑、换同事、隔一年再打开，版本都不会跑偏。直接敲 gradle 用的是你系统里装的那个版本，别人的项目到你的机器上，两个版本对不上，就报一堆你看不懂的错。

一句话记住：<strong>项目自带 gradlew，就永远用它</strong>。Windows 下不用加 ./，直接敲 gradlew 加命令就行。这半行字的差别，能帮你躲掉一类最无聊的报错。

##### 六个组合技（进阶）

单条命令会了，把它们组合起来才是真用法。

- <strong>clean 加 assembleDebug 一条龙</strong>：怀疑缓存错乱时，一条命令清完再打，省得跑两遍。
- <strong>只跑一个测试</strong>：test 后面跟上 <code class="inline">--tests</code> 和测试类名，几百个测试里只跑你要的那个，快得多。
- <strong>依赖树配搜索</strong>：:app:dependencies 的输出很长，配管道交给 findstr（Windows）或 grep（Mac/Linux）过滤某个库的名字，冲突一眼现形。
- <strong>lint 之后看报告</strong>：命令跑完只是个开头，完整报告在 app/build/reports 目录里，浏览器打开排版更友好。
- <strong>断网也能构建</strong>：加 <code class="inline">--offline</code>，所有依赖都缓存过时可以离线打包，地铁上、飞机上、酒店烂 Wi-Fi 下的救命参数。
- <strong>记不住就写小抄</strong>：把上面这些抄进你的笔记，命令行参数和快捷键一样，是拿来查的，不是拿来背的。

##### 报错原文怎么取：求助前的最后一步

命令行跑完一片红，求助前要把"证据"取全。终端窗口里选中报错文本直接复制就行，注意两点：一是从第一条红字开始复制，别只截最后一句；二是往上多翻几屏，很多关键警告在报错之前就出现了。日志太长时，可以把输出重定向到文件再挑重点，这些取下来的文字，无论是贴给 AI、贴进搜索框还是发到社区，质量都比"打不了包"五个字高出一百倍。求助的成败，一半在你按下发送键之前就定了。

带上报错原文。

##### 场景案例：深夜十一点半的红色 Sync

把这些串成一个真实场景。周三深夜十一点半，你给同学做的课表 App 明早要演示，刚改完最后一处，Sync 突然一片红。深呼吸，按流程走。

第一步，别改代码：此刻改代码大概率是帮倒忙。第二步，看第一条报错：如果是一长串 "Could not resolve" 加超时字样，八成是网络问题，依赖没拉下来，检查网络，重试一次。第三步，还红，跑 <code class="inline">clean</code> 再 Sync，缓存错乱是深夜报错的第二大来源。第四步，还不行，File → Invalidate Caches，重启 Android Studio，这组合拳解决"昨天还能跑今天就不行"的成功率高得惊人。第五步，最后的兜底：关掉项目，找到用户目录下的构建缓存文件夹删掉重来：耗时几分钟，但基本百试百灵。

先看报错。

第二天早上七点，演示照常。这次经历教会你的东西比修好的那个 bug 值钱：<strong>深夜报错九成不是你的代码坏了，是环境抽风了，先修环境，再怀疑自己</strong>。

#### 五、版本对照速查（2026 年 11 月核对）

前面的速查卡教的是写法，一般不会过期；会过期的是版本号。"教程里的版本号和我工程里的对不上"是新手最常见的困惑之一。这张对照表按 2026 年 11 月的稳定版核对过，用到哪儿查到哪儿：

- <strong>依赖写法</strong>：先声明 BOM，其余 Compose 依赖不写版本号；升级只改 BOM 一处。
- <strong>升级顺序</strong>：IDE → AGP/Gradle → Kotlin 插件 → BOM，再逐个解决编译警告，别一口气全拉满。
- <strong>排错第一步</strong>：版本对不上，先 Clean + Sync 再看报错：八成是缓存或插件不匹配，和上一节的构建玄学是同一种病。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">

<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要查的东西</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">当前稳定值 / 做法</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">官方出处</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Compose UI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1.12.1（1.13.0 beta）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AndroidX Compose 发布说明</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Material 3</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1.4.0（1.5.0 alpha）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AndroidX Compose 发布说明</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Compose BOM</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2026.08.00</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Compose BOM 版本映射页（developer.android.com）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Compose 编译器</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin 插件 org.jetbrains.kotlin.plugin.compose</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Compose Compiler 文档</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.x（1.13 要求 2.2）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin 发布说明</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minimum SDK</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">示例 API 26</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新建项目向导</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最新稳定平台</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 17（API 37，2026 年 6 月正式版，Pixel 先行）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">developer.android.com</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">targetSdk 门槛</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Google Play 新应用/更新自 2027 年 8 月起要求 target API 37</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Play Console 政策页</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">发布包</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Google Play 用 .aab</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Play Console</td></tr>
</tbody>
</table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
2026 年 11 月核对的核心版本速查

##### BOM 是什么：一个"版本总管"

表里反复出现 BOM，值得单独讲明白。BOM 的全称直译是"物料清单"，你可以把它理解成餐厅的<strong>招牌套餐</strong>：套餐号（比如表里那串 2026.08.00）定下来，里面每道菜，Compose UI、Material 3、各种组件，的版本都由菜单配好了，彼此兼容是官方测试过的。你升级时只改套餐号一处，不用逐个改菜。

不用 BOM 会怎样？每个库自己写版本号，写错一个，轻则警告重则冲突："三个库打架"是新手期最常见的莫名报错之一。所以前面速查卡才把"先声明 BOM"列为依赖写法第一条：这不是风格偏好，是少踩坑的硬技巧。

##### 版本号怎么读：三段数字和希腊字母

表里那些 1.12.1、1.4.0，读法有讲究。三段数字是"大版本.小版本.修补"：第一位变了，可能有不兼容的改动，升级要慎重看说明；第二位变了，通常是加功能；末位变了，基本是修 bug，可以放心升。看到 1.13.0 beta 这种带后缀的，字母的含义是成熟度：alpha 是内部测试，beta 是公开测试，都不算稳定版：个人项目尝鲜可以，要上架给别人用的 App，老老实实用稳定版。

还有一句必须强调：这张表核对于 2026 年 11 月，你读到的时候数字几乎肯定更新了。<strong>表格给你的是"长什么样"，官方发布页给你的才是"现在是多少"</strong>——这也是把它叫"速查"而不是"定论"的原因。

##### 升级的正确姿势：小步慢跑

升级翻车的新手，九成是犯了同一个错：一口气全拉满。正确姿势是四步。第一步，升级前先存个版本：给自己留后悔药。第二步，按上面清单的顺序一层层升：IDE、构建工具、Kotlin、BOM，每升一层就构建一次，红在哪一层一清二楚。第三步，构建过了跑一遍测试，别裸奔。第四步， Release Notes 里专门列着"不兼容改动"（Breaking changes），升级前扫一眼，能提前知道哪些地方要改。

平静时期的升级可以缓一缓：稳定版用得好好的，没有安全或功能上的刚需，晚一两个月升没人扣你工资。追新有追新的代价，项目能跑是底线。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：查版本的两个官方入口

{class="mt-1"}
一个是 Compose BOM 版本映射页（在 developer.android.com 搜 "Compose BOM" 就能到），一个是 AndroidX 各库的发布说明页。查这两处花一分钟，比凭记忆写版本号省下的排错时间，一个小时打不住。
:::

#### 安卓开发术语速查表

术语是查资料的钥匙，看不懂术语，连搜索框里该输什么都不知道。这张表按"你在哪里会撞见它"组织，释义一句话说完，看完就能回去继续干活。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">术语</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">一句话解释</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activity</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一个"屏幕"。传统安卓界面的基本单位，旧教程里到处是它</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Compose</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">安卓现在主推的界面写法：用 Kotlin 函数直接描述界面长什么样</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Composable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">能画出界面的函数，名字前面带 @Composable 标记</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">重组（Recomposition）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">状态一变，相关界面函数重新执行一遍，把新样子画出来</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">状态（State）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">会变、且界面要跟着变的值，用 remember 记住</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">状态提升</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把状态交给父级管，子组件只管显示——多人协作不打架的关键</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">协程（Coroutine）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"可以暂停的子任务"，不卡界面的前提下干耗时活</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">挂起函数（suspend）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">能被协程暂停的函数，网络和数据库操作常长这样</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Flow</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数据流：数据源不断往外吐新值，界面订阅它自动刷新</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ViewModel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">界面的"管家"：存状态、派后台活，界面转屏重建它也不死</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Repository</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数据中转站：界面找它要数据，它决定去网络还是去本地拿</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">官方的本地数据库工具，把表格映射成代码</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Entity / DAO</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room 的两张脸：Entity 定义"一行长什么样"，DAO 定义"怎么增删改查"</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DataStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">存小配置的键值仓库，开关、主题、标记都归它</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">网络请求库：把"访问某个网址"写成接口方法</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Manifest</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">App 的"户口本"：有哪些页面、用哪些权限，都登记在这</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">权限</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">动相机、定位这类敏感能力前，要向系统和用户申请的许可</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Intent</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">组件间的"传话条"：启动页面、分享内容都靠它递话</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">生命周期</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">页面从出现到消失的各个阶段，资源要在对的阶段放手</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">返回栈</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系统记"你从哪来"的页面堆，按返回键就是弹一层</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SDK</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">开发工具包：编译运行安卓程序所需的全套家什</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API 级别</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每个安卓版本的编号，新功能都标着"从哪一级开始有"</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">minSdk / targetSdk</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">前者是你支持的最低安卓版本，后者是你声明适配到的版本，商店政策盯着后者</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">构建工具：把代码和资源打包成 App 的流水线</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">依赖（Dependency）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">别人写好、你拿来用的代码包，声明在构建文件里</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">APK / AAB</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">安装包的两种格式：APK 直接装，AAB 是商店要的上传格式</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">签名</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">给安装包盖"这就是我"的印章，更新升级都认这个章</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">模拟器（Emulator）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">电脑里虚拟出来的安卓手机</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ADB</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">电脑和安卓设备之间的"传令兵"，命令行工具</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lint</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">静态检查工具：不跑代码也能挑出可疑写法</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">混淆（R8）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">上线前给代码瘦身、改名、删冗余，兼顾体积与安全</td></tr>
</tbody>
</table>
```
:::

这张表不用背。这些词会在你的项目里反复出现，看到熟脸回来查一下，三五回合自然就记住了，真正的记忆场所是你的代码，不是这张表。哪天你发现查表的频率明显降下来了，别怀疑，那是你上了一个台阶。

这张表还有一个隐藏用途。搜资料前先来这儿对一遍词。你脑子里那句"那个会自己变的数"，在表里叫"状态"；那句"让界面卡住不动的下载"，在表里叫"该放进协程的耗时操作"。术语对齐了，搜索框里的关键词才打得准，AI 才不会答非所问，社区里的人也才看得懂你在问什么。<strong>会查之前先会叫名字</strong>——这张表就是你的命名手册。

#### Android Studio 快捷键速查

快捷键的价值不在炫技，在于让"改代码→看结果"这个循环快到不打断思路。下表以 Windows 默认键位为例（macOS 把 Ctrl 换成 Cmd、Alt 换成 Option；不同版本可能有出入，以 Android Studio 的 Keymap 设置页为准）。挑高频的记，剩下的用到再查。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">想做什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">快捷键</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">说明</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">快速修复</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Alt+Enter</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">红线上的"救命键"，IDE 直接告诉你怎么改</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全局搜索</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">连按两次 Shift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">找文件、找设置、找操作，一个入口全包</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跳到定义</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ctrl+B</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">遇到不认识的函数，一步跳到它的老家</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">返回上一步</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ctrl+Alt+向左箭头</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跳完能回来，才敢随便跳</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">注释本行</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ctrl+/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">疑难代码先注释掉，对比着看</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">复制当前行</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ctrl+D</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不用选中，光标停在那行就行</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">删除当前行</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ctrl+Y</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">同上，删行不用按半天退格</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">格式化代码</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ctrl+Alt+L</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">缩进乱成一锅粥时的一键整理</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">运行 App</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Shift+F10</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全表使用频率冠军</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">调试运行</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Shift+F9</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">配合断点，逐行看程序怎么跑</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跳到下一个错误</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">F2</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一堆红字之间快速巡逻</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最近打开的文件</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ctrl+E</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多文件之间来回穿梭的班车</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">查找替换（本文件）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ctrl+R</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">改名字、改文案，一次全换</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">清理无用导入</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ctrl+Alt+O</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">删掉没用的 import，还文件一片清爽</td></tr>
</tbody>
</table>
```
:::

##### 调试四连：断点旁边的四个键

学会打断点之后（点行号右侧空白处），调试栏里会出现几个小键，挑最常用的四个记住就够："下一步"单步走；"步入"钻进函数里看；"跳出"从函数里退回来；"继续"跑到下一个断点。配合变量监视窗口，程序停住的那一刻，把鼠标悬在任何变量上都能看到它当时的值。这四键加悬停，覆盖新手期九成九的调试需求：程序"为什么是这个结果"的疑问，几乎都能靠它当场破案。

##### 先背五个，其余用熟自然记住

别贪多。Alt+Enter（快速修复）、双击 Shift（全局搜索）、Ctrl+B（跳定义）、Ctrl+D（复制行）、Shift+F10（运行），这五个先练成条件反射，你的编辑体验立刻不一样。尤其是 Alt+Enter：新手看到红线的第一反应是慌，老手的第一反应是按它，这一个键的差距，练一周就补齐。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：改键位不丢人

{class="mt-1"}
File → Settings → Keymap 里可以随时改键，也能切换成你熟悉的方案。顺手比标准重要：键位是为你服务的，不是你为键位服务的。
:::

#### 常用依赖速查

依赖就是"别人写好的轮子"，加轮子分两步：把坐标复制进构建文件，点一下 Sync。下表列的是本书项目和最常见需求会用到的库。<strong>版本号一概不写死</strong>——交给 BOM 或版本目录统一管理，最新值以官方发布页为准，这是上一节说过的纪律。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">用途</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">常用库（坐标）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">一句话说明</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">界面基础</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">androidx.compose:compose-bom（配 material3）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BOM 统管版本，Material 3 给现成组件</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">扩充图标</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">material-icons-extended</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">内置图标不够用时的扩充包</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">页面导航</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">androidx.navigation:navigation-compose</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">管页面跳转和参数传递</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">本地数据库</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">androidx.room:room-runtime / room-ktx / room-compiler</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">三件套分工：核心、协程支持、编译期处理</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">小配置存储</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">androidx.datastore:datastore-preferences</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">开关、主题这类小键值</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">网络请求</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.squareup.retrofit2:retrofit（配 JSON 转换器）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">声明式网络库，老牌靠谱</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">协程</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">org.jetbrains.kotlinx:kotlinx-coroutines-android</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">异步任务的基础设施</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">生命周期工具</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">androidx.lifecycle:lifecycle-viewmodel-compose / lifecycle-runtime-compose</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把 ViewModel 和界面稳妥地绑在一起</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">图片加载</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">io.coil-kt:coil-compose</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一行代码把网址变成界面上的图</td></tr>
</tbody>
</table>
```
:::

##### 加依赖的三个纪律

<strong>纪律一：少加为妙</strong>。每个依赖都带来体积、冲突和升级成本。想加之前先问一句"官方有没有自带的？"——这个问题能拦下一小半冲动。轮子好用，但车太重跑不快。

<strong>纪律二：看维护状态</strong>。加之前去它的项目主页扫一眼：最近有没有更新、问题反馈区是不是堆积如山。半年没动静的库，就像没人接的客服电话——出事的时候你找不到人。

<strong>纪律三：冲突先查树</strong>。报 "Duplicate class" 这类冲突，别急着重装什么，回到 Gradle 速查那节，用 :app:dependencies 看依赖树，找出是谁顺手带进来的，排掉一个就好。

#### 环境与构建故障速查

这一节是"半夜报错专用"。症状对号入座，按"第一反应"处理；两轮没解决的，把报错原文交给 AI 或搜索引擎，记得用 FAQ 里那张提问模板。表里的报错关键词是英文原文，方便你直接拿去搜。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">症状（关键词）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">最可能的原因</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">第一反应</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SDK location not found</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SDK 路径没配置好</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">检查 SDK 安装路径，重新 Sync</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cannot resolve symbol 'R'</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">某个资源文件写错了</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">先看 res 目录有没有红叉，处理掉再 Clean</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sync 一直转圈 / Could not resolve</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">网络问题，依赖拉不下来</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">查网络，稍后重试；反复失败看镜像配置</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Unsupported class file major version</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">JDK 版本与构建工具不匹配</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">查官方的兼容说明，换到匹配的 JDK 版本</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">模拟器启动失败 / 卡死</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">虚拟化没开、磁盘满、内存不够</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">开虚拟化、清磁盘；急用就直接换真机</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真机连不上（设备列表看不到）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">USB 调试没开或数据线不行</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">开发者选项里打开 USB 调试，换根线试试</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Duplicate class</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">两个依赖带了同一个类</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用依赖树找出处，排掉一个</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Manifest 合并报错</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">minSdk 等设置打架</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">看报错里的合并报告，按提示改</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">构建时内存溢出</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">构建进程内存给小了</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">关掉别的大程序，调构建内存配置</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"昨天还能跑，今天不行"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">缓存错乱（玄学高发区）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Clean + Sync，再不行 Invalidate Caches</td></tr>
</tbody>
</table>
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>避坑提醒：一次只改一个变量

{class="mt-1"}
排障第一大忌是同时改三处。改完了好了，不知道是谁的功劳；坏了，更不知道谁背锅。每改一处，构建一次，记一笔。慢就是快，这句话在排障这件事上是字面意思。

一次改一处。
:::

##### 排障三原则：先环境，再代码，最后工具

用这张表之前，把三句话记住。<strong>先环境</strong>：报错的第一嫌疑人永远不是你的代码，是缓存、网络、版本这些"场外因素"，Clean、Sync、重启这三板斧先抡完。剩下的才轮到代码。 <strong>再代码</strong>：环境排除了，回到你最近一次改动，"刚才改了什么"永远比"代码哪里有错"好查，按时间倒着找，效率翻倍。<strong>最后工具</strong>：两轮没头绪，再把报错原文交给 AI 和搜索引擎，注意顺序，别一上来就问，你会在"明明自己能查到"的问题上养成依赖。三原则不是流程图，是优先级：它保证你把时间花在最可能破案的地方。

先环境，再代码。

<div class="case-box">
<div class="case-box-head">翻车现场</div>
<p>构建失败，你一口气改了三处：Gradle 版本、依赖版本，还有一个看着可疑的 JDK 设置。改完构建通过了，可你不知道是哪一处起了作用，于是把三处改动一起提交进项目。两个月后换电脑，新环境又红了，你完全不知道该动哪一处，只能从头试一遍。</p>
<p class="case-box-quote">"反正好了，哪一处起的功不知道"</p>
<p class="case-box-src">场景来源：全书通用场景（非特定读者）</p>
<p><strong>怎么办</strong>：排障第一大忌是同时改三处。每改一处，构建一次，记一笔。慢就是慢得值：这一次你知道是哪一处修好的，下一台机器复现时才有据可依。</p>
</div>


#### 学习路径建议：给三类背景的读者

手册查的是"点"，这一节补的是"线"。同样是两个月走到"能独立做小 App"，不同背景的人该抄的近路完全不同。别贪别人的路线，对号入座，走你自己的那条。

##### 第一类：完全零基础，从没写过代码

你的优势是手上没有旧习惯要掰，别人要花两周纠正的毛病你天生没有；你的难关是前两周的"环境加语法"枯燥期，装环境装到怀疑人生，语法练到看不见头。对策：把头两周的目标定死（环境能跑、Kotlin 基础语法过一遍），别羡慕别人第三天就画出了界面，他们欠下的账后面会补。

节奏建议：每天固定一小时，比周末突击七小时有效得多。编程手感靠的是"每天都摸"。第一个里程碑记牢：把新建项目的欢迎语改成自己的名字，再改成点一下按钮弹出一句话。这个瞬间看起来很小，"我写的东西在手机上跑起来了"的感觉，很多人就是在这里上瘾的。

##### 第二类：会一点别的语言——Python、前端，甚至 Excel 宏都算

你已经翻过"变量、循环、函数"这座山，地图你是认得的，所以 Kotlin 语法那两周你可以压缩，把省下的时间投给三样新东西：类型系统（Kotlin 管得比动态语言严）、空安全（新概念但极其好用）、协程的思考方式。界面直接从 Compose 入手，声明式写法和网页组件的思路相通，你大概会经常冒出"这不就是那什么吗"的感觉，跟着那感觉走就对了。

要提防的坑只有一个：把动态语言的随手风带进来：变量随手定义、类型懒得想。Kotlin 的编译器会替你把关，报错比 Python 多不少，别烦，那些红线不是刁难，是免费的检查员。

##### 第三类：有编程经验，从 Java 或别的端转过来

语法层面你一两周就能上手，真正的坎是两个<strong>思维切换</strong>：从"命令式地摆控件"到"声明式地描述界面"；从"自己一行行写"到"验收 AI 的产出"。前者靠把 XML 那套先放一放，用 Compose 重写一个老项目最快；后者直接读第七篇，尤其第 37 章，你已经站在那场变革的正中间了。

给你一条硬建议：第一个项目必须在一个月内上到商店——哪怕用户只有你自己。签名、打包、商店政策这一整条流程。是经验丰富的人最容易"绕着走"的部分，绕过去才算真正闭环。另外，把第 57 章那套最小可用架构亲手搭一遍，你会明白它为什么配叫"最小可用"。

##### 三类人共同的四条底线

<strong>项目驱动</strong>：学完一节就往项目里塞一节。没有项目承接的学习，一个月后什么都不剩——这句话被无数人验证过，包括写书的人。

<strong>建错题本</strong>：报错和解法随手记，三个月后它就是你私人定制的速查手册——本章就是它的公共版。

<strong>把 AI 当陪练，别当拐杖</strong>：让它解释概念、让它出题、让它检查你的代码；但基础阶段的核心练习自己敲。第七篇（第 37-47 章）会把这套协作方式展开成完整方法论，练手感和练指挥，两样都要。

<strong>上线一次</strong>：不管多小的 App，走完一次"打包—签名—上架"的完整流程。上线是学编程的毕业典礼——没有它，你永远不知道自己的东西在别人手机上是什么样。

##### 三个真实时间表，供你对照

在校生小周：工作日每天晚自习后一小时，周末两个半天。八周走完主线，第三周就做出了课表 App 的雏形给自己用，学生的优势是时间整块、试错免费，他最大的敌人是"考试周断了就不捡"。他的对策写在错题本第一页：断可以，重启入口要留好。

上班族老郑：通勤地铁上用手机看半章，午休二十分钟敲几行，周六上午雷打不动两小时。他走得比小周慢三周，但一步没断——上班族的秘诀是"碎片学理论、整块写代码"，千万别反着来：通勤路上写代码，晕；周末补理论，困。

带娃的小林：每天只有孩子睡后的四十分钟。她把八周拉成了三个月，规则改成"每天哪怕只跑通一次构建也算数"。她的进度最慢，但错题本记得最勤：四十分钟容不下浪费，每个报错都被她当场记下。三个月后她的用药提醒 App 装进了爸妈手机，也在商店上架了。

三个时间表，三种节奏，同一套方法论：固定时间、项目驱动、错题本、不断线。你可以对照着排自己的：没有标准答案，只有适不适合你。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：写下你的第一周计划

{class="mt-1"}
现在就定三件事：① 每天几点、在哪里练（固定时间和地点，完成率翻倍）；② 第一周结束时你要跑通的东西（越具体越好，"跑起来 Hello World"就合格）；③ 遇到报错时你的第一动作（翻回 FAQ 的黄金三步）。写在纸上，拍进手机：三个星期后对照着看，你会感谢今晚这五分钟。
:::

#### 模拟器与真机使用速查

调试设备是你每天都在用的工具，值得一张专属速查表。分工先说清：模拟器管"多机型快测"，真机管"手感与验收"，前者求快，后者求真，谁也不替代谁。

##### 模拟器常用操作速查

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">想做什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">入口</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">典型用途</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">创建虚拟设备</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Device Manager → 创建</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">选机型和系统镜像，一次建好几台备用</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">快照回档</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">关闭模拟器时保存状态</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">下次启动秒回现场，环境折腾坏了能"读档"</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">旋转屏幕</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">模拟器侧边工具栏</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">模拟转屏，验证状态有没有丢</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">模拟定位</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">扩展菜单里的位置功能</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">天气、地图类功能不用出门就能测</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">调节网络</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">扩展菜单的网络选项</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">模拟弱网，看你的加载提示体不体面</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">拖拽装包</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把安装包文件拖进窗口</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不跑构建也能快速装包验证</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">模拟来电与短信</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">扩展菜单的电话与短信入口</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">测打扰场景：你的提示音和通知会不会被盖住</td></tr>
</tbody>
</table>
```
:::

这张表里最值得养成习惯的是<strong>快照</strong>：把模拟器当游戏机玩，重大改动前"存个档"，环境弄坏了读档重来：比你重装模拟器省下的时间，一个月能攒出好几小时。

##### 真机开发者选项速查

真机调试的前提是打开开发者选项：设置里找到"关于手机"，连点"版本号"多次（通常是七下），直到系统提示你已进入开发者模式。之后在系统设置里就能看到它。下面几个开关按用途备查：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">开关</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">什么时候开</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">说明</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">USB 调试</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真机调试期间</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">电脑连接手机的前提，用完可以关</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不锁定屏幕（充电时）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">插线调试时</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">省去反复解锁，一天能省几十次</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">显示点按操作反馈</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">排查点击没反应时</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每一次触摸都有小圆点，点没点到一目了然</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">显示布局边界</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">界面排版错乱时</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">给所有控件画出边界，溢出和重叠现原形</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">字体大小调到最大</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">验收阶段</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">看看界面在极端设置下散没散架</td></tr>
</tbody>
</table>
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>避坑提醒：开发者选项不是玩具

{class="mt-1"}
里面的开关大多数为开发服务，乱开可能影响日常使用（比如限制后台进程会让微信收不到消息）。规矩：调试期间开的，验收完随手关回去。给爸妈远程帮忙时尤其注意：他们的手机上别留这些开关。
:::

最后补一句真机的验收清单，呼应前面 FAQ 的第三问：字体缩放调到最大看看散不散架、开飞行模式看看断网提示、连一个蓝牙耳机测测音频类功能、找个老机型装一遍试试流畅度：模拟器替代不了的就是这些"真实世界的脾气"。四样都过了，你的 App 才算真正"出了门"。这张验收清单建议你抄进笔记：以后每做完一个版本，跑一遍，全绿再发布。

#### FAQ 补充：再答六问

前三问解决"入门"，这一组解决"第一版做完之后"的疑问：它们出现的时机稍晚，但早晚会出现，先存在这儿。判定标准也简单：当你开始琢磨"要不要把它做得更像一个正经 App"的时候，就来翻这组问答。

<strong>Q22：代码混淆和资源压缩要不要开？</strong>

第一版先不开。混淆会把代码改名瘦身，收益是包更小、更难被反读，代价是崩溃日志变得难读、反射类代码容易出问题。起步阶段它只会给你添堵。等 App 有了真实用户、你要认真控制体积了，再按第 56 章的发布流程开起来，开之前先跑完整测试。

<strong>Q23：深色模式要不要第一版就做？</strong>

做，但不是做"另一套界面"。但是从一开始就别把颜色写死。用主题色的方式写颜色，系统切到深色模式时界面会自动跟着变，成本几乎为零。反过来，写死了颜色的项目，后补深色模式等于重新刷一遍墙：前者是十分钟的事，后者是一个周末的事。第一版就守这条纪律，后面全是赚的。

<strong>Q24：横屏和折叠屏要不要一开始就适配？</strong>

起步阶段锁竖屏是务实的做法，很多成熟 App 也是这么起步的，先把竖屏体验做扎实，比两头都做、两头都半吊子强。但有一点现在就要留心：别在代码里假设"屏幕宽度永远是那么多"，布局写得有弹性，将来适配横屏和折叠屏时的改动量就小得多。适配是后话，弹性是前提。

<strong>Q25：要不要做多语言？</strong>

起步只做中文，完全没问题。但有一条纪律从第一天就要守：<strong>文案不要写死在界面代码里</strong>，统一放到字符串资源里去。这周做是"多打几个字"，下周做是"满工程找字符串"，两个月后做是"重写界面"。资源放对了地方，哪天想加英文，翻译完文件就完事；放错了地方，加一种语言就是一场大扫除。

<strong>Q26：界面做得太丑，有没有速成的审美方案？</strong>

有三招。第一招，用 Material 3 的现成组件，别自己发明按钮，官方组件的间距、圆角、配色都是设计师调过的，你老老实实用，界面就已经在及格线以上。第二招，抄系统自带 App 的"作业"：它的列表、卡片、设置页的排版，是经过大量用户验证的范本。第三招，回到前面说的灵感集相册，看到顺眼的截图就存，做界面之前翻一翻。审美速成不了，但"不丑"是速成的，守规矩就行。

<strong>Q27：AI 都能帮我写代码了，这张速查卡还有用吗？</strong>

比以前更有用。AI 交上来的作业，你得看得懂才能验收：卡上的写法就是你的"验收词汇表"：它写的 remember 用得对不对、LazyColumn 选得合不合适、异常接没接住，你一眼要能看出来。看不出问题，AI 的错误就直接进了你的 App。第七篇（第 37-47 章）教你怎么指挥 AI，而指挥的前提是你认识士兵手里的枪，这张卡就是枪械说明书，留着。

#### 把这本手册用起来

手册的价值不在读，在翻。三种翻法，对应三个时刻。<strong>报错时</strong>：先翻"环境与构建故障速查"，对号入座，两轮没解决再出门求助；<strong>写代码卡住时</strong>：翻"常用代码速查卡"和"术语速查表"，先确认"这个东西叫什么"，再去搜索或问 AI，术语对了，搜索结果的质量天差地别；<strong>开新项目前</strong>：翻"常用依赖速查"和"版本对照速查"，把地基材料按最新状态备齐再动工。

再给你一个复查节奏：每月挑一天，花十分钟做三件事，把版本对照表和官方发布页对一遍，看看有没有该升的；翻一遍你的错题本，最常出现的报错还在不在；把速查卡上最近新画的记号圈出来，那就是你下个月的练习重点。十分钟不多，但它保证这本手册始终是你的"现行地图"，而不是一年前的旧地图。

这本手册和第七篇（第 37-47 章）是配合着用的。写代码卡住了，翻手册；写法不确定，翻手册；但"该让 AI 干到哪一步、验收时看什么、出了问题怎么定位责任"，那是手册管不了的另一门手艺，去第七篇找。一实一虚，一查一思，手册管你手上的活，方法论管你脑里的路。两样都齐了，你才算真正装备完整。

最后一条建议：把这本手册推荐给和你一起学的伙伴。查过的坑互相说一声，两个人的错题本就变成了两个人的——学编程的路上，能互相翻手册的人，比什么都珍贵。

顺便预告一下三个月后的场景：某天你随手写完一个小功能，忽然意识到刚才那几行代码没查任何东西，没翻卡、没搜术语、没看故障表。那个瞬间别觉得平淡，它值得你停下来给自己记一功：手册还在书桌上，但它已经悄悄从"拐杖"变成了"备用轮胎"。这一天不需要你做什么，只需要你注意到：然后，接着写。

#### Kotlin 语法十式速查

前面的速查卡是"写法"，这一节是"语法"，十个最常用的语法点，覆盖小项目里绝大多数日常代码。每一式都配"长什么样"和"容易踩的坑"，配合 Kotlin 官网的在线演练场，一个下午就能全部亲手过一遍。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">语法</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">样子</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">用途与提醒</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">val 与 var</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">val name = "阿芳"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">val 不可变，var 可变。默认用 val，能用不变的就用不变——少一半的诡异 bug</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">字符串模板</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"共 $count 条"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">变量直接嵌进字符串，告别加号拼接；表达式用大括号包起来</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">when</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">when(x) { 1 -> ...; else -> ... }</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">比 if-else 链清爽得多。记得写 else 兜底，别让意外值漏网</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">空安全 ?. 与 ?: </td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">name?.length ?: 0</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可能为 null 的值一律显式处理。少用双感叹号强转——那是把雷埋给自己</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">data class</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">data class User(val name: String)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">存数据的类，自动带上比较、复制这些标配，账目、待办都是它</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">lambda</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">{ x -> x * 2 }</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Compose 里到处是它，读熟了世界就亮了。先学会读，再学写</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">集合三连</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">list.map { }.filter { }</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数据加工流水线：变换、筛选、遍历。排账单、筛记录全靠它们</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">默认参数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">fun load(page: Int = 1)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">调用时可以只传想传的参数，函数签名不再臃肿</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">扩展函数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">fun String.shout() = uppercase()</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">给别人的类"外挂"方法，自己的工具函数有了家</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">惰性初始化</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">val config by lazy { ... }</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">开销大的对象等到第一次用时再建，启动更轻快</td></tr>
</tbody>
</table>
```
:::

两个使用提醒。第一，别十式齐练，先练 val/var、字符串模板、when 这三式，它们出现在每一行代码里；空安全放第二梯队，其余用到再回表里查。第二，这张表和官方演练场是绝配：每个语法点在演练场里敲一遍、改一个参数看结果变化，记忆效率是纯看表的几倍。语法这东西，眼睛会了不算会，手会了才算。

#### 代码风格十条（新手版）

风格不决定代码能不能跑，决定三个月后你读自己代码时的痛感。下面十条都是低成本的约定，从第一个项目就守，零额外投入，全是长期回报。

- <strong>命名见名知义</strong>：变量叫 <code class="inline">count</code> 别叫 <code class="inline">c</code>，函数叫 <code class="inline">loadWeather</code> 别叫 <code class="inline">doIt</code>。名字是写给三个月后的你的便条。
- <strong>大小写守规矩</strong>：变量和函数首字母小写驼峰，类名首字母大写，这是 Kotlin 的官方约定，跟着走，别人的代码你也读得顺。
- <strong>Compose 函数首字母大写</strong>：界面函数像类一样用大写开头，这是 Compose 的官方约定，用来和普通函数区分。
- <strong>一个函数干一件事</strong>：函数超过一屏就该拆了。拆开的每个名字，就是你思路的目录。
- <strong>缩进别手敲</strong>：交给格式化快捷键（Ctrl+Alt+L）。人只管写内容，对齐是机器的事。
- <strong>魔法数字抽出来</strong>：代码里光秃秃的 30、0.8 之类的数，抽成有名字的常量。三个月后你会对着裸数字发呆，而对 <code class="inline">NOTIFY_BEFORE_DAYS = 3</code> 一眼秒懂。
- <strong>注释写"为什么"</strong>：代码本身已经说明"做了什么"，注释的价值在解释"为什么这么做"。写"是什么"的注释是噪音。
- <strong>文件各回各家</strong>：页面、数据、工具类分开放。项目小的时候觉得无所谓，项目一大，找不到文件的时间是真实的成本。
- <strong>死代码直接删</strong>：注释掉不用了的代码块，删掉。想找回靠版本管理，不靠注释坟场。
- <strong>收工三查</strong>：格式化一遍、编译一遍、自己把改动从头读一遍。这三查花两分钟，能挡掉八成"低级失误"。

这十条没有一条需要天赋，全是习惯。习惯的养成方法也简单：本周只守第一条，守住了下周再加一条。十周之后回头看，你的代码会长成让老手都点头的样子，不是因为你聪明，是因为你不欠账。

##### 时间紧的读者：三个月压缩版

如果八周对你来说排不开，还有一条三个月的慢速线，每周三个小时也能走完。前一个月只做两件事：环境和 Kotlin 语法、再带一个能跑的小界面；第二个月做一个项目，不求全，只求"能记、能存、能看"；第三个月给它加上网络或通知里的任意一样，然后走一遍上架流程。慢速线的代价是战线拉长，好处是每周的压力小，适合在校生和加班多的人。唯一要守的纪律还是那条：<strong>每周都摸，哪怕只摸半小时</strong>——断一个月，手感归零，重启成本比你想象的大。

<strong>Q28：项目应该什么时候开始用版本管理？</strong>

答案是：越早越好，门槛比你想象的低。第一次"改坏了想回到昨天"的瞬间到来时，就是最好的时机——通常撑不过第四周。起步只需要三招：保存一个版本、看看历史、回到过去，一个晚上学得会，之后每天受益。想系统地弄明白，去翻第二十三章附的 GitHub 入门指南。那里连"为什么要有版本管理"都讲透了。给学习期的你一条实在建议：从今天起，每天收工前存个版本，这个习惯的成本是十秒，回报是"随便折腾"的底气。

#### 从本书项目到你的项目：十个改造主意

学完记账本和天气，最大的风险是"书里的做完了，然后呢"。这一节给你十个改造主意，都是在书里两个项目的基础上小步延伸的，每个都对应速查卡上的一两行写法。挑一个让你心动的，本周就动手。

1. <strong>给记账本加"导出"</strong>：把一个月的账目导出成文件发给自己，练数据处理和文件操作。
2. <strong>加每周小结</strong>：周日晚上自动汇总本周开销，发一条通知，练后台任务和通知。
3. <strong>多本账</strong>：生活一本、旅行一本，练数据建模，一个"账本"包住多条"账目"。
4. <strong>语音记账</strong>：说一句话记一笔，练语音输入接口和字符串解析。
5. <strong>给天气加"穿衣建议"</strong>：根据气温给一句话提示：练条件逻辑和文案设计，零网络成本。
6. <strong>多城市天气</strong>：爸妈在哪、你在哪，各看各的，练列表管理和数据结构。
7. <strong>主题切换</strong>：深色浅色跟随系统：练主题与 DataStore 配合。
8. <strong>统计图表</strong>：把开销画成柱状图——练画布和自定义绘制。
9. <strong>桌面小组件</strong>：不打开 App 也能看今日余额，练跨进程的界面展示，难度最高但最拉风。
10. <strong>数据备份</strong>：一键把数据库导成文件再导入，练文件的读写和容错，做完你会特别有安全感。

这十个主意刻意没有给实现步骤，从主意到代码的这段路，就是你脱离"教程"走向"独立"的那段路。卡住了怎么办？回速查卡找动作、查官方文档找写法、按提问模板求助，这套流程你已经全会了。做完三个主意，你就不再需要这本手册陪练了；它功成身退，你继续往前。

#### 六、结语：从第一个 App 到第 N 个 App

回头看，你从"不知道 Activity 是什么"，到装好环境、学会 Kotlin、用 Compose 画出界面、给 App 接上数据库和网络，再到测试、打包、上架<strong>这条路上你已经走完了从零到一最难的一段</strong>。

技术的世界变化很快：框架会升级，工具会换代，AI 会接手越来越多"敲键盘"的活。但有一样东西不会过时：<strong>你把一个模糊的想法，拆解成清晰的步骤，再一步步实现它的能力</strong>。工具是放大器，思路是地基。放大器可以替换，地基不能动摇。

:::inline div .quote-line
你不再只是"会玩手机的人"。你能把脑海里的想法，变成三十亿安卓设备上真实运行的 App。从今天开始，用键盘去创造，这就是安卓开发者的浪漫。
:::

#### 参考文献

{class="list-decimal pl-6 mb-3 space-y-1 text-xs text-gray-500"}
1. Android Developers. (2026). Android Developer Guides and Jetpack Compose Documentation. developer.android.com.
2. Kotlin Foundation. (2026). Kotlin Language Documentation. kotlinlang.org.
3. Android Open Source Project. (2026). Android Platform Version History and API Levels.（source.android.com）
4. Google Play. (2026). Play Console Help: Publishing and App Signing.
5. AndroidX Release Notes. (2026). Room / DataStore / Navigation / WorkManager releases.
6. Square. (2026). Retrofit Documentation. github.com/square/retrofit.
