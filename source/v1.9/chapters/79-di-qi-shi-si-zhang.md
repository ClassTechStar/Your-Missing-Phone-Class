---
id: di-qi-shi-si-zhang
num: 74
nav: 第七十四章：页面路由与应用模型
toc: default
kind: chapter
after_part: hongmeng-kai-fa-pian
---

### 第七十四章：页面路由与应用模型——UIAbility 与生命周期

{class="chapter-intro mb-4"}
界面会画了，这一章搞清楚"应用骨架"：一个鸿蒙应用由什么组成？页面怎么跳转？应用的生命周期长什么样？这一章对应安卓的"四大组件"和 iOS 的 AppDelegate——概念一一对应，换的是名字。

先回答一个高频疑问：为什么需要"骨架"这种东西？因为应用不是一堆页面的堆砌——它需要在合适的时机初始化资源、在切到后台时保存状态、在回到前台时恢复界面、在收到系统事件时做出响应。这些"时机"就是生命周期，而承载生命周期的单元就是 Ability。理解了骨架，你在写任何页面时都会知道"我的代码运行在什么阶段"，内存泄漏和数据丢失这些经典问题也就有了预防的抓手。

#### 一、Stage 模型：应用、模块与 Ability

鸿蒙 Stage 模型的三层结构：<strong>应用（Application）→ 模块（Module）→ 能力（Ability）</strong>。一个应用可以有多个模块（主模块 entry + 动态特性模块 feature）；每个模块里放若干 Ability——<strong>UIAbility 是有界面的能力单元</strong>（对应安卓的 Activity、iOS 的 UIWindowScene），ExtensionAbility 是没有界面的后台扩展（对应安卓的 Service/Provider）。

记住一个定位：<strong>UIAbility 是应用的入口单元，页面只是它里面的一帧</strong>——应用级状态别挂在某个页面上，要放在 Ability 或更高一层。鸿蒙还多一个安卓、iOS 都没有的变量：分布式场景下，同一个能力可能在另一台设备上被拉起。设计状态时提前想一句——这份数据，会不会出现在别的屏幕上？

module.json5 里声明应用的基本信息、申请的权限、Ability 的入口配置。来对照看一眼：

::: div .code-block
:::inline div .code-head
<span>JSON5 · module.json5 关键片段</span><span class="dots">···</span>
:::

```
{
  "module": {
    "name": "entry",
    "type": "entry",
    "abilities": [{
      "name": "EntryAbility",
      "srcEntry": "./ets/entryability/EntryAbility.ets",
      "exported": true,
      "skills": [{
        "entities": ["entity.system.home"],
        "actions": ["action.system.home"]
      }]
    }],
    "requestPermissions": [
      { "name": "ohos.permission.INTERNET" }
    ]
  }
}
```
:::

"exported: true" 表示能被外部拉起（主入口必须为 true）；"skills" 里的 entity.system.home 标记它是桌面图标入口——对应安卓的 LAUNCHER intent-filter。

Stage 模型与老 FA 模型的区别也值得一句话带过：FA 模型时代一个页面就是一个 Ability（页面即能力），页面多了 Ability 数量爆炸；Stage 把"能力"和"页面"解耦——一个 UIAbility 里可以装多个页面（Navigation 栈），架构一下子清爽了。这也是第 70 章说"Stage 是唯一主线"的深层原因：新能力（卡片、多屏协同）都只在 Stage 上提供。

Ability 的"导出与拉起"还有个进阶场景：你的应用可以被其他应用调用（比如分享图片到你的修图应用）。这靠 skills 里的自定义 action 实现——声明一个自定义 action，别人的应用构造对应意图就能拉起你的指定页面。跨应用协作的完整机制在第 79 章的元服务部分还会出现，这里先建立"Ability 是可以被外部触发的"这个概念。

#### 二、生命周期：从冷启动到销毁

UIAbility 的生命周期与 Activity/Scene 高度对应：<strong>onCreate（创建，读参数）→ onWindowStageCreate（窗口就绪，加载页面）→ onForeground/onBackground（前后台切换）→ onDestroy（销毁，释放资源）</strong>。页面级还有 aboutToAppear/aboutToDisappear（对应安卓的 onCreate/onDestroy 与 SwiftUI 的 onAppear）。

每个回调的"典型工作"值得逐个记牢。onCreate：读取启动参数（谁拉起了你、带了什么数据）、初始化全局资源——注意这时窗口还没有，别在这里操作 UI。onWindowStageCreate：窗口就绪，加载主页面（loadContent），可以开始与界面交互。onForeground：应用回到前台——恢复被暂停的任务（比如继续播放、刷新数据）。onBackground：切到后台——<strong>这是保存状态的最后机会</strong>，关键数据在这里持久化。onDestroy：真正销毁——释放监听器、取消协程、关闭数据库连接。页面级的 aboutToAppear/aboutToDisappear 是页面的"出生与死亡"，网络请求通常在前者发起。

前后台切换是数据丢失的重灾区：切到后台随时可能被系统回收，回来时要么能重建状态，要么已经在 onBackground 里把关键数据持久化了。安卓篇讲 Activity 生命周期、iOS 篇讲 scenePhase，到这里是 UIAbility——三个平台名字不同，要回答的是同一个问题：什么时候存数据，什么时候释放资源。别靠猜，对着官方生命周期图逐个核对。

页面跳转有两种方式：<strong>router</strong>（页面级，pushUrl/replaceUrl/back）和 <strong>Navigation</strong>（组件级导航栈，官方现在更推荐——它走路由表做声明式注册，把「当前在哪一页」变成可传参、可恢复的数据，比到处塞布尔标志可靠）。带参数跳转与回传：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 路由跳转与返回</span><span class="dots">···</span>
:::

```
// A 页面：跳转并带参数
import { router } from '@kit.ArkUI'

router.pushUrl({
  url: 'pages/Detail',
  params: { id: 42, from: 'list' }
})

// B 页面：接收参数 + 返回并回传
let params = router.getParams() as Record&lt;string, number | string&gt;
console.info('收到 id: ' + params.id)
router.back()   // 复杂回传可用 emitter 事件或 AppStorage
```
:::

排查路由配置有个捷径：<code class="inline">hdc shell aa start -b 包名 -a Ability名</code> 能从命令行直接拉起应用（hdc 相当于安卓的 adb），比在界面上反复点快得多。

生命周期的调试有个小技巧：在每个回调里打一行日志（console.info 标明回调名），然后在 Logcat 里过滤——你会清楚地看到应用在切后台、回前台、被拉起时经历了什么。这个"生命周期日志"的习惯能帮你定位一大类"数据莫名其妙丢了"的问题：十有八九是你在错误的回调里做了事，或者该保存的时机被错过了。

#### 三、权限模型：声明、申请与最小化

鸿蒙权限分三类：<strong>system_grant</strong>（安装即授予，如 INTERNET）、<strong>user_grant</strong>（运行时弹窗申请，如位置、相机、麦克风）、<strong>受限开放权限</strong>（需额外申请证书才可用，如读取应用列表）。流程和安卓的运行时权限一致：module.json5 声明 → 代码里调用 requestPermissionsFromUser 申请 → 处理拒绝后的降级体验。

权限申请的"时机与话术"是一门小手艺。时机上，在用户正要用到该功能的那一刻申请（点"导航"按钮时申请位置），而不是一启动就弹一堆——第 68 章的 iOS 权限策略在这里完全适用。话术上，弹窗前先展示一个自定义的"用途说明"界面（为什么需要这个权限、拒绝了会怎样），让用户带着理解去点"允许"。拒绝后的降级路径也要设计好：位置被拒就支持手动输入城市，相机被拒就支持从相册选图。

最小化原则在鸿蒙上有个具体的体现：requestPermissions 列表里的每一项都会在应用市场审核时被检查——申请了位置却没有位置相关的功能，会被驳回。所以权限列表和功能是强绑定的：加功能才加权限，删功能记得删权限。这与安卓的权限审核逻辑一致，三个平台在"最小化权限"上的态度已经完全统一。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：做两级页面

{class="mt-1"}
给第 73 章的设置页加一个"关于"入口：点击跳转到 About 页面并传递应用版本号；About 页显示版本号与一个"返回"按钮。完成它，你就掌握了鸿蒙应用"多页面 + 参数传递"的最小闭环。
:::

#### 四、Navigation 深度实战：路由表、NavPathStack 与嵌套导航

回想一下你在购物应用里的一天：首页点进分类，分类点进商品详情，详情点进规格选择，再往确认订单走——一路往下钻，返回时一层层退回来。这条链子在代码里就是导航栈。上一节把 router 和 Navigation 一笔带过，这一节专门把 Navigation 掰开讲，因为它是官方现在的主推方案，也是你后面写任何多页面应用都绕不开的东西。

先看一个错误示范。不少开发者管页面跳转，靠的是一串布尔标志——"是不是从详情页返回的""是不是从编辑页来的"，返回逻辑写成一大团 if-else。页面一多，标志位之间开始打架，改一处崩三处。Navigation 的思路不一样：把"当前在哪一页"变成一个实实在在的数据结构（NavPathStack，导航路径栈）。跳转是往栈里压一条路径，返回是出栈，参数和结果都挂在路径上。状态即数据，数据就能保存、能打印、能恢复——这就是它比标志位可靠的根本原因。

##### 第一步：注册路由表

Navigation 的页面不走 router 那种全局注册，而是走"路由表"：在 resources/base/profile 目录下建一个 route_map.json，给每个页面起个名字，指向它的构建函数。

::: div .code-block
:::inline div .code-head
<span>JSON · resources/base/profile/route_map.json</span><span class="dots">···</span>
:::

```
{
  "routerMap": [
    {
      "name": "Detail",
      "pageSourceFile": "src/main/ets/pages/Detail.ets",
      "buildFunction": "DetailBuilder"
    }
  ]
}
```
:::

然后在 module.json5 的 module 字段里挂上它：<code class="inline">"routerMap": "$profile:route_map"</code>。做完这两步，"Detail" 这个名字就在应用里"挂号"了——任何地方都可以凭这个名字往栈里跳，不用再到处 import 目标页面组件。

路由表还有两个进阶用法。一是跨模块：HAR、HSP 里打包的页面也能进同一张路由表，声明所属模块后按名字跳，主模块不需要 import 它们——大型应用把"首页"和"详情"拆进不同模块时，路由表就是黏合剂。二是按需加载：不在启动时就把所有页面建好，跳到谁才加载谁，冷启动速度白捡一笔。具体配置字段以官方文档为准。

顺手立个规矩：路由名别散落在代码里当裸字符串，抽到一个常量文件里统一管理。名字拼错了页面就是不出来，报错线索还藏在日志深处——用常量文件，编译期就能把这类手滑拦下来。

##### 第二步：压栈、取参、出栈

导航栈本体是 NavPathStack。主页面把它交给 Navigation 组件持有，之后跳转、返回、传参全对它操作：

::: div .code-block
:::inline div .code-head
<span>ARKTS · NavPathStack 跳转与取参</span><span class="dots">···</span>
:::

```
// 主页面：压栈并带参数
this.pathStack.pushPathByName('Detail', { id: 42, from: 'list' })

// Detail.ets：NavDestination 内通过 onReady 拿到上下文
@Component
struct DetailPage {
  pathStack: NavPathStack = new NavPathStack()

  build() {
    NavDestination() {
      Column() {
        Text('详情内容')
      }
    }
    .title('详情')
    .onReady((context: NavDestinationContext) =&gt; {
      // 从路径信息里取参数
      let param = context.pathInfo.param as Record&lt;string, number | string&gt;
      console.info('id = ' + param.id)
      // 存下栈的引用，本页内部还能继续往深处跳
      this.pathStack = context.pathStack
    })
  }
}

// 返回上一页
this.pathStack.pop()
```
:::

注意 onReady 这个回调——它是 NavDestination 的"页面就绪"时刻，参数、栈引用、路径信息都在这里一次性到手。别在组件的成员变量初始化里去摸路由上下文，那个时机上下文还没就绪，拿到的多半是空。存引用那一行也有讲究：详情页自己还想往更深处跳（比如"查看店铺"），拿这个引用就能继续压栈，不用一层层往上问。

返回传结果也比 router 时代优雅。pop 的时候可以带一个结果值，压栈的一方在 push 时注册的 onPop 回调里接住它——编辑页保存后带回"保存成功"，列表页就地刷新。老做法要借 emitter 或 AppStorage 绕一圈，现在一条线走完。

##### 错误示范与纠正：参数别绕全局变量

新手常犯的另一个错误：把跳转参数塞进 AppStorage 或某个全局单例，让目标页面自己去捞。页面少时看不出问题，页面多了就乱——A 页面刚存的值被 B 页面顺手覆盖，返回时读到的是别人的数据。路由参数是"跟着路径走"的，一次跳转一份，互不干扰；只有全局广播式的状态才配进 AppStorage。

::: div .code-block
:::inline div .code-head
<span>ARKTS · 错误示范与纠正</span><span class="dots">···</span>
:::

```
// 错误示范：用全局变量传参
AppStorage.setOrCreate('pendingId', 42)
this.pathStack.pushPathByName('Detail', '')   // 参数位空着

// Detail 页面里：
let id = AppStorage.get&lt;number&gt;('pendingId')   // 谁都能改，谁都能读

// 纠正：参数跟着路径走
this.pathStack.pushPathByName('Detail', { id: 42 })
// onReady 里从 context.pathInfo.param 取，用完即弃
```
:::

纠正后的写法，参数生命周期与这次跳转严格同寿，返回后自动作废——这正是"栈即数据"的好处之一。

##### 第三步：让栈活过一次重启

栈是数据，所以它能被保存。应用被系统回收后再打开，用户最烦的就是"回到首页重来"。本章第七节会讲 onBackground 持久化的完整代码，这里先说思路：把路径栈的内容（页面名序列和每条路径的参数）在后台时机存下来，onCreate 里读出来逐条压回去，用户的浏览位置就还原了。官方也在持续完善 Navigation 的栈恢复与应用接续能力（跨设备接续时连栈一起搬过去），具体接口以官方文档为准。哪怕暂时不用官方方案，"栈可序列化"这个思路本身就是你手里的工具。

::: div .code-block
:::inline div .code-head
<span>ARKTS · 栈快照的自救版恢复（示意）</span><span class="dots">···</span>
:::

```
// 页面层示意：离开页面时把栈名序列记下来
onPageHide(): void {
  let snapshot = this.pathStack.getAllPathName().join(',')
  AppStorage.setOrCreate('nav_snapshot', snapshot)
}

// 应用重启后：按名字逐条压回，参数另存一份映射
onPageShow(): void {
  let names = AppStorage.get&lt;string&gt;('nav_snapshot') ?? ''
  names.split(',').forEach(n =&gt; this.pathStack.pushPathByName(n, null))
}
```
:::

这是简化示意——真实项目里，参数要和名字一起存成"名字到参数"的映射，恢复时逐条取出，个别页面还要判断"参数还在不在"。骨架恢复就是这样：先用最笨的版本跑通，再按需要变精。

##### 嵌套导航：Tab 里再套栈

底部四个 Tab、每个 Tab 里又能各自往深处跳——这是主流应用的标配结构，也是新手栽跟头的地方。标准做法是嵌套：最外层一个 Navigation 管住四个 Tab，每个 Tab 的内容区再各自放一个 Navigation，拥有自己独立的 NavPathStack。好处很直观：切 Tab 时各栈互不干扰，每个 Tab 内部的返回手势只作用于自己的栈。

用真实场景过一遍嵌套：底部"首页、发现、消息、我的"四个 Tab，你在"我的"里点进"设置"，再进"关于"；切到"消息"Tab，它在自己的栈顶上待得好好的；再切回"我的"，你还在"关于"页。每个 Tab 记住自己的位置，这就是嵌套栈给用户的体验承诺。单一大栈做不到这一点——栈只有一条，切 Tab 就得丢位置。

反面教材是把所有页面塞进一个大栈：从"我的"Tab 深处的页面直接跳到"首页"Tab 的深层页面，返回键一按，路径就乱了。嵌套之后还有个容易忽略的细节：返回手势会交给"当前最上层的导航栈"，如果出现"按返回直接退出应用"而不是"回到上一页"，先检查是不是子栈没有正确接管返回事件——这个坑在第十一节门诊里还会出现。

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2" aria-hidden="true"></i>避坑提醒

{class="mt-1"}
pushPathByName 传了路由表里不存在的名字，页面不会出现，也不会当场报错——线索只在日志里。遇到"点了没反应"的问题，先打印栈内容确认是不是名字没对上，再查路由表有没有登记，最后才怀疑别的。
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2" aria-hidden="true"></i>小贴士

{class="mt-1"}
调试导航栈有个笨但好用的办法：每跳一次就打印一次栈的内容（getAllPathName 能列出当前栈里所有页面的名字，size 是深度）。栈一乱，日志一目了然，比在界面上反复猜快得多。
:::

进阶一招：路由栈拦截。较新版本给 NavPathStack 提供了拦截能力，可以在每次压栈、出栈前插入自己的逻辑——典型用法是未登录用户点"订单"时先带去登录页，登录成功再继续原本的跳转。拦截逻辑写在中央一处，不用在每个按钮上重复判断。这个能力对系统版本有要求，动手前先翻官方文档确认可用性。

还有个纠结党问题：老项目全是 router，要不要马上迁到 Navigation？不必一刀切，两者并存没有问题，新页面用 Navigation、老页面保持现状，官方给了渐进迁移的路径。但新起的项目别犹豫，直接 Navigation：传参、恢复、跨模块注册都是为长期维护设计的，晚迁一天就多背一天的标志位。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hand-pointer mr-2" aria-hidden="true"></i>来动手：把第 73 章的两级页面升级成 Navigation

{class="mt-1"}
给 About 页在 route_map.json 里挂个名字，设置页改用 NavPathStack 传版本号，About 页在 onReady 里取参显示，再试试返回时带一个结果回去。跑通这条链，Navigation 的最小闭环就成了。
:::

#### 五、应用级状态管理：AppStorage、PersistentStorage 与 EventHub

状态管理的坑，多半出在"放错了楼层"。把状态想象成一栋四层楼：组件内的一层（@State/@Prop/@Link），页面间的一层（LocalStorage），应用级的一层（AppStorage），最底下是落盘的一层（PersistentStorage）。越往上走生命周期越长：组件销毁 @State 就没了，应用退出 AppStorage 才清空，PersistentStorage 连退出都能扛住。写代码前先问两句：这份数据，谁需要看见？要看见多久？答案决定它住几楼。放错了，要么"一跳页面就丢"，要么"赖在内存里不走"。

##### AppStorage：全应用看得见的白板

AppStorage 是应用级的键值仓库，任何页面、任何 Ability 都能读写它：

::: div .code-block
:::inline div .code-head
<span>ARKTS · AppStorage 读写与页面订阅</span><span class="dots">···</span>
:::

```
// 任意地方写入
AppStorage.setOrCreate&lt;string&gt;('userName', '小王')

// 页面里订阅：值一变，界面自动刷新
@StorageLink('userName') userName: string = ''

// 只想跟着白板变、不需要回写的场景用 @StorageProp
@StorageProp('unreadCount') unreadCount: number = 0
```
:::

@StorageLink 是双向绑定：页面里改，白板也变；@StorageProp 是单向同步：白板变了页面跟着刷，页面本地改不影响白板。分清这两个，能省掉一大类"界面为什么不刷新"的排查时间。改主题就是最典型的场景：设置页往白板写 'dark'，所有挂着 @StorageLink('themeMode') 的页面同时变色，谁也不用通知谁。

##### PersistentStorage：钉进磁盘的那一格

AppStorage 的数据应用一退就没了。想让某个键活过重启，用 PersistentStorage 把它钉进磁盘：persistProp 建立绑定之后，这个键在 AppStorage 里的每次变化都会自动落盘，下次启动自动恢复。调用时机有讲究——必须在 EntryAbility 的 onCreate 里、任何 AppStorage 写入之前做：

::: div .code-block
:::inline div .code-head
<span>ARKTS · EntryAbility.ets 里的持久化初始化</span><span class="dots">···</span>
:::

```
onCreate(): void {
  // 先钉住，再使用。第二个参数是"没有历史数据时"的默认值
  PersistentStorage.persistProp('themeMode', 'auto')
  PersistentStorage.persistProp('fontSize', 'standard')
}
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2" aria-hidden="true"></i>避坑提醒

{class="mt-1"}
三件事别做。一别把大对象、长列表塞进去——每次变化都写盘，启动速度和闪存寿命双双遭殃；二别存敏感信息（token、密码），落盘数据原则上能被有更高权限的环境读到，敏感数据走加密存储；三别在 persistProp 之前就往 AppStorage 写同名键，绑定会被冲掉，"明明存了却没恢复"的灵异事件多半是它。
:::

##### 系统环境也走同一套语法

系统环境（深浅色模式、字体缩放这类）的读取也是同一套"白板"思路：用 Environment 把环境变量挂进 AppStorage，页面再用 @StorageProp 订阅。深色模式切换时页面自动响应，不需要你自己去监听系统广播。声明式框架的舒适感就在这里——状态一变，界面自己动。

##### LocalStorage 与 EventHub：中间两层

LocalStorage 的作用范围是一个 UIAbility 内部：建一个 LocalStorage 实例传给页面，同一 Ability 的多个页面就能共享它，比 AppStorage 干净——它不会泄漏到别的 Ability 去。典型用法是"单能力内部的共享状态"：几个页面共同维护的筛选条件、一份跨页面的临时草稿。

::: div .code-block
:::inline div .code-head
<span>ARKTS · LocalStorage 绑定页面</span><span class="dots">···</span>
:::

```
// EntryAbility 里创建并传给页面
let storage = new LocalStorage()
storage.setOrCreate('filter', '全部')

// 页面顶部绑定
@Entry(storage)
@Component
struct ArchivePage {
  @LocalStorageLink('filter') filter: string = ''
}
```
:::

@LocalStorageLink 的用法和 @StorageLink 一模一样，只是作用范围从"全应用"缩到"本 Ability"。API 相同意味着你可以在范围变大时平滑搬家，只改绑定方式不改业务逻辑。

事件这条线是 EventHub：每个 Context 自带一个事件中心，on 注册、emit 触发、off 注销。适合"一件事发生了，谁关心谁响应"的解耦场景——比如"用户改了头像"，设置页发出事件，个人主页的组件自己刷新，两边不用互相持有引用。

::: div .code-block
:::inline div .code-head
<span>ARKTS · EventHub 收发事件</span><span class="dots">···</span>
:::

```
// 发送方（任意页面）
this.context.eventHub.emit('avatarChanged', newUri)

// 接收方（一般在 aboutToAppear 里注册）
this.context.eventHub.on('avatarChanged', (uri: string) =&gt; {
  this.avatarUri = uri
})

// aboutToDisappear 里务必注销，否则页面销毁后回调还挂着
this.context.eventHub.off('avatarChanged')
```
:::

注册和注销要成对出现：aboutToAppear 里 on，aboutToDisappear 里 off。页面销毁了监听还挂着，是内存泄漏的经典来源——回调越积越多，界面越用越怪。第十一节门诊的病例六就是它。

跨 Ability 就别指望 EventHub 了——它绑定在各自的 Context 上。跨能力通信的正规姿势有三种：Want 参数（拉起时带过去）、应用级单例（挂在 applicationContext 上的共享数据）、公共事件（CommonEventManager，连跨应用都行）。公共事件是广播模型，从安卓的 BroadcastReceiver 转过来的同学会觉得眼熟，语义几乎一一对应：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 订阅公共事件</span><span class="dots">···</span>
:::

```
import { commonEventManager } from '@kit.BasicServicesKit'

let subscriber: commonEventManager.CommonEventSubscriber | undefined

// aboutToAppear 里订阅
commonEventManager.createSubscriber(
  { events: ['usual.event.SCREEN_ON'] },
  (err, sub) =&gt; {
    subscriber = sub
    commonEventManager.subscribe(sub, (err, data) =&gt; {
      // 系统亮屏事件到了，做你的响应
    })
  }
)

// aboutToDisappear 里注销
if (subscriber) {
  commonEventManager.unsubscribe(subscriber)
}
```
:::

还有本章开头提过的分布式变量，值得再敲一次黑板：设计全局状态时多问一句"这份数据会不会出现在另一台设备的屏幕上"。接续场景里，AppStorage 里的浅层数据（阅读位置、播放进度这类）搬过去能直接续上，而绑定在某个页面上的临时状态搬不动。把状态往应用级收一收，跨设备的体验就顺一分。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
  <thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">工具</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">作用范围</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">典型用途</th></tr></thead>
  <tbody>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State/@Prop/@Link</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">组件内部与父子组件</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">界面自身的显示状态</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">LocalStorage</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">单个 UIAbility 的页面之间</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">能力内共享的临时状态</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AppStorage</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">整个应用</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">主题、未读数、全局标记</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">PersistentStorage</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">应用 + 磁盘</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">重启后还在的少量配置</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">EventHub</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">单个 Context 内</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">页面解耦的事件通知</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">公共事件</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跨应用</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系统事件监听、应用间广播</td></tr>
  </tbody>
</table>
```
:::

怎么选？从窄往宽选。先页面内，不够再页面间，再不够才上应用级，要活过重启才落盘。状态的作用域收得越窄，将来重构越轻；一上来就全塞 AppStorage，应用大了以后每个页面都跟所有状态有牵连，改一处要回归测全量。

- <strong>单一数据源</strong>：一份数据只在一个地方"住"，别的页面用绑定来读。同一个状态存两份，早晚改到不同步。
- <strong>绑定优先于手动同步</strong>：能用 @StorageLink/@StorageProp 自动刷的，别手写"收到事件再改变量再刷新"的三段式。
- <strong>落盘的要小</strong>：落盘层只放配置和少量关键状态，大块头走文件和数据库。

还要防一个慢性病：全局白板变垃圾堆。AppStorage 的键没有"到期自动清理"，写到后来的应用里，几十个键没人认领，谁也不知道删了会不会出事。键名带上来源前缀（setting_、player_ 这种），每个模块只写自己的前缀；页面级的临时值一律别进白板——白板上的每个键，都应该答得上来"谁写它、谁读它、什么时候可以删"。

高频事件也要留意：emit 每秒几十次的场景（进度更新、传感器数据）别直接走 EventHub 逐次刷界面，先在数据侧攒批或节流，再发一次——事件模型解决"谁关心谁响应"，不解决"刷得太勤"。

排查状态问题还有个土办法：在关键写入处打日志（键名、旧值、新值），复现"界面不对"时先看数据对不对。数据对、界面不对，是绑定问题；数据就不对，是写入路径问题。两分法一划，问题就锁定了一半。状态分层还会影响页面复用：一个组件若只依赖窄作用域的状态，挪到哪个页面都能用；一旦它直接摸 AppStorage，复用就带上了全局前提。

#### 六、Want 与隐式拉起：别人怎么打开你的某个页面

场景先摆出来：用户在你的购物应用里下了单，半小时后通知栏弹出"订单已发货"，点一下，应用打开，直接落在那条订单的详情页。这一跳背后的主角叫 Want——"拉起 Ability 的意图"的数据载体，相当于安卓的 Intent。Want 分两种：显式，指名道姓 bundleName 加 abilityName，拉起谁写得清清楚楚；隐式，只描述意图——什么动作（action）、什么数据（uri/type），由系统去匹配谁能干这活。应用内部互拉用显式就够，跨应用的对接基本都走隐式。

##### 参数是怎么进来的

关键点：拉起你的 Want，冷启动和热启动走的门不一样。应用没启动过，走 onCreate；应用已经在后台活着（默认单例模式），走 onNewWant。参数解析必须两处都写——漏了 onNewWant，就会出现"冷启动点通知一切正常，热启动点通知纹丝不动"的经典事故。第十一节门诊的病例一就是它。

::: div .code-block
:::inline div .code-head
<span>ARKTS · 在 onCreate / onNewWant 里解析参数</span><span class="dots">···</span>
:::

```
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  this.parseWant(want)   // 冷启动
}

onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  this.parseWant(want)   // 热启动
}

parseWant(want: Want): void {
  let orderId = want.parameters?.orderId as string
  if (orderId) {
    AppStorage.setOrCreate('pendingOrderId', orderId)
  }
}
```
:::

为什么解析完不直接跳页面，而是先写进 AppStorage？因为 onCreate 时窗口和页面都还没就绪，硬跳会翻车。把"想去哪"先记成待办，onWindowStageCreate 加载完主页面之后再根据标记跳——这是启动参数处理的固定套路，照抄不会错。

参数类型也别想当然：parameters 里取出来的值以实际为准，用之前先判空、再判断类型。Want 是外部递进来的东西，不是可信数据——字段可能是缺的、错的、恶意构造的，每个字段都按"可能不存在"处理，直接拼进查询语句或直接加载未校验的地址，都是安全审计必抓的问题。

uri 参数另有一个小坑：链接里的中文和特殊字符是经过编码的，你拿到的可能是百分号串，先解码再用；反过来拼 uri 时也要编码，别把空格和中文裸着塞进去。编码解码成对出现，这类问题日志一眼就能看出来——打印出来的东西"不像人话"，八成就是编码没对上。

WantAgent 和裸 Want 的取舍顺便说一句：通知、卡片这种"系统替你存着、用户随时点"的入口，用 WantAgent 把意图固化下来最稳；代码里当下就要 startAbility 的，直接构造 Want 就行。一个偏"存起来等点击"，一个偏"现在就去"，场景不同，别混着用。

##### 三个常见入口的接线方式

<strong>通知</strong>：构造一个 WantAgent——把"点通知要拉起谁、带什么参数"封装成一个对象——交给通知。用户点击时系统按它拉起你的 Ability，参数照上面的套路解析。通知本身的完整玩法在通知那章讲过，这里只要记住：通知点击落页的本质就是"带参数的 Want 拉起"。

<strong>桌面卡片</strong>：卡片代码里调用 postCardAction，action 指定 router，带上 abilityName 和 params，点击卡片的某个区域就能拉起应用落到指定页面。天气卡片"点进未来七天"就是这么接线的。卡片的完整玩法在第 79 章元服务部分展开，这里先建立"卡片也是入口之一"的概念。

<strong>其他应用</strong>：想让别人能"分享图片到我这来修图"，就在 module.json5 的 skills 里声明自定义 action 和能接受的 uri 类型；别人的应用构造带这个 action 的 Want 调 startAbility，系统就把意图交给你：

::: div .code-block
:::inline div .code-head
<span>JSON5 · module.json5 里声明可被隐式拉起</span><span class="dots">···</span>
:::

```
// abilities 里 EntryAbility 的 skills 数组，追加一项
"skills": [
  {
    "actions": ["com.example.retouch.action.EDIT_IMAGE"],
    "uris": [{ "type": "image/*" }]
  }
]
```
:::

反过来，你想拉起别人（拨号、发邮件、打开网页），同样用隐式 Want 描述意图，别写死对方包名——写死了，对方没装你就尴尬了；隐式拉起至少能让你先探测、再降级。

链接拉起再多说两句：从浏览器或短信点一个网址直接进应用，鸿蒙上推荐走 App Linking——用 https 域名做载体，应用市场校验你对域名的归属（服务器要按官方要求放置校验文件），通过后链接直达应用，体验对齐安卓的 App Links 和 iOS 的 Universal Links。自定义 scheme 也支持，但没有域名校验，容易被别的应用抢注，正式产品建议优先 App Linking，配置细节以官方文档为准。

##### 调试：把"玄学拉起"变成可复现的实验

隐式拉起的配置容易写错，反复打包点按钮验证很慢。两个加速手段：一是命令行直拉——hdc shell aa start 指定目标应用与 Ability（第二节介绍过基本用法），还能塞自定义键值对模拟"别的应用带参数拉起你"的场景，参数写法以官方文档为准；二是把 want 的 action、entities、uri 全部打印出来看一遍。你以为你构造的意图，和系统实际收到并匹配的意图，可能不是同一个——打印出来逐字段对，配置错在哪儿立刻现形。

音乐播放器是隐式拉起最常见的真实场景之一：锁屏界面上点"下一首"，控制信号通过系统的媒体会话机制送到应用；应用如果在后台被回收，系统会重新拉起它。这类"系统代用户拉起"的场景，参数往往为空、纯靠应用自己恢复上下文——所以第七节讲的"播放进度持久化"在这里是刚需，两节知识在这里会合。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hand-pointer mr-2" aria-hidden="true"></i>来动手：接一条"通知落页"链路

{class="mt-1"}
点按钮发一条本地通知，WantAgent 指向详情页并带一个 id 参数。分别在冷启动（后台划掉应用再点通知）和热启动（应用挂着再点通知）两种情况下验证参数都到得了。两种情况都通过，才算接线成功——只测一种，等于没测。
:::

#### 七、后台任务与保活：系统只给你三张牌

先把幻觉打破：应用切到后台，系统随时可能冻结它、回收它，这不是 bug，是设计。手机省电的第一原则就是"用户看不见的，少干活"。官方给开发者留了三张牌——短时任务、长时任务、延迟任务。与其琢磨怎么偷偷保活，不如先想清楚：我的后台需求，到底属于哪张牌。

还要分清三种"离开"：切后台但进程还活着（内存里，回来即用）、被系统回收（进程没了，下次启动重建）、用户手动划掉（同回收，但用户的意图更明确）。三种离开对应的处理不一样——前一种靠 onForeground 恢复刷新，后两种靠 onBackground 里落盘的数据接上。数据丢失的锅，九成落在"没分清这三种离开"上。

- <strong>误区一：切后台就该继续跑</strong>——普通应用切后台后很快会被挂起，定时器停摆、网络回调冻结都是正常现象。要做的是在 onBackground 里把该存的存了，而不是指望后台继续活。
- <strong>误区二：申请一个长时任务就能永远活着</strong>——长时任务必须声明类型（音乐播放、导航、运动、录音、数据传输等），系统会核对类型与实际行为的匹配度。申请了音乐却在后台传文件，会被掐掉。
- <strong>误区三：后台数据丢了是系统的问题</strong>——绝大多数"数据丢了"都能追到"没在 onBackground 里持久化"。内存态和持久态的边界，这一节用代码划清楚。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
  <thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">任务类型</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">适合场景</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">特点与限制</th></tr></thead>
  <tbody>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">短时任务</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">切后台后需要一点时间收尾的活：写完一批缓存、上传最后一段日志</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">主动申请，系统给一段宽限时间（时长视系统策略而定，以官方文档为准）；到期未完成会被挂起</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">长时任务</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">音乐播放、导航、运动记录、录音这类"前台开始、后台必须继续"的持续性服务</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">module.json5 声明 backgroundModes，代码里申请；状态栏常驻提醒用户"我在后台干活"</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">延迟任务</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不急的活：WiFi 环境下同步相册、充电时做备份</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">交给系统调度器（workScheduler），系统挑满足条件的空闲时机执行</td></tr>
  </tbody>
</table>
```
:::

长时任务的申请代码长这样（以音乐播放为例）：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 申请长时任务</span><span class="dots">···</span>
:::

```
// module.json5 的 abilities 里先声明：
// "backgroundModes": ["audio"]

import { backgroundTaskManager } from '@kit.BackgroundTaskKit'
import { wantAgent } from '@kit.AbilityKit'

async startContinuous() {
  let wantAgentObj = await wantAgent.getWantAgent({
    wants: [{ bundleName: 'com.example.player', abilityName: 'EntryAbility' }]
  })
  await backgroundTaskManager.startContinuousTask({
    wantAgent: wantAgentObj,          // 点状态栏提醒能回到应用
    backgroundMode: backgroundTaskManager.BackgroundMode.AUDIO_PLAYBACK
  })
}

// 停止播放时记得取消
await backgroundTaskManager.stopContinuousTask()
```
:::

两处细节别省：backgroundModes 的类型要和申请时传的枚举对得上，也要和实际行为对得上；wantAgent 别漏——它让用户点状态栏那条提醒能直接回到你的应用，漏了它，用户想进应用就只能回桌面找图标。

为什么长时任务非要状态栏常驻提醒？这是设计上的自觉：后台消耗电量、流量、定位这些资源，用户有权随时知道"谁在后台干活"。所以那条提醒不是负担，是你的应用与用户之间的信任凭据——用户看到"正在运动"会觉得合理，看到说不清名目的常驻提醒就会去设置里掐你。亮明身份，反而活得更久。

延迟任务值得单独交代一句：它不追求"立刻跑"，而是把活交给系统调度器，附上条件——"有网络时""充电时""空闲时"，系统挑满足条件的窗口来执行。相册自动备份、聊天记录云同步都该走这条道。写法上是提供一个 WorkSchedulerExtensionAbility，系统到点拉起它干活，干完即走。它的节奏由系统定，别把它当定时闹钟用。

##### 场景案例：夜跑应用的后台安排

设想你做了个跑步记录应用。用户晚上十点开始夜跑，手机进兜，屏幕黑了四十分钟。这段时间应用必须在后台持续拿定位、累计里程——这正是长时任务里运动、定位类型的适用场景：开始跑步时申请，状态栏出现"正在运动"的提醒；跑步结束调 stopContinuousTask 交还资源。里程数据每公里落一次盘（preferences 就够），哪怕中途被极端情况回收，用户最多丢最后一段，不会一夜白跑。

同一个应用里还有另外两类活，各配各的牌。跑步结束后上传轨迹文件，不需要"立即"，挂延迟任务——"连接 WiFi 且充电时"上传，系统挑凌晨的空闲窗口执行。用户点"结束跑步"后应用退到后台，还剩最后一段数据要写、一张成绩图要生成，申请一个短时任务拿几十秒到几分钟的宽限（时长以官方文档为准），干完即走，不留常驻。三个需求三张牌，一个长时、一个延迟、一个短时，这就是"按需求选牌"的具体样子。

##### onBackground 的持久化实操

回到数据这条线。onBackground 是你最后一次"有把握"的保存时机，轻量配置用 preferences，结构化的大批量数据用数据库。以用户正在编辑的草稿为例：

::: div .code-block
:::inline div .code-head
<span>ARKTS · onBackground 里保存草稿</span><span class="dots">···</span>
:::

```
import { preferences } from '@kit.ArkData'

onBackground(): void {
  let store = preferences.getPreferencesSync(this.context, { name: 'draft' })
  store.putSync('draft_text', this.draftText)
  store.putSync('draft_time', Date.now())
  store.flush()   // flush 才真正落盘，漏了等于白存
}
```
:::

保存要配恢复。应用被回收后重建，onCreate 或页面初始化里读出这份草稿，和时间戳比一比，比界面上的旧就补回去：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 回前台时接上草稿</span><span class="dots">···</span>
:::

```
onForeground(): void {
  let store = preferences.getPreferencesSync(this.context, { name: 'draft' })
  let saved = store.getSync('draft_text', '') as string
  let savedTime = store.getSync('draft_time', 0) as number
  if (saved !== '' &amp;&amp; savedTime &gt; this.lastRestoreTime) {
    this.draftText = saved   // 接上被回收前的草稿
    this.lastRestoreTime = savedTime
  }
}
```
:::

注意三点：一，onBackground 里的保存动作要快，别做重活，宽限时间有限；二，同步写入加 flush 才稳妥，异步写遇到"还没写完就被回收"会功亏一篑；三，保存和恢复要闭环——只存不恢复，用户照样觉得"数据丢了"，因为丢在恢复这一侧。

顺带理清被回收后的启动路径：用户点桌面图标或通知回来，应用是一次全新的冷启动，onCreate 里除了常规初始化，还承担"整理遗产"的职责——检查上次有没有没干完的活、没恢复的现场。把"被杀之后能接上"当作 onBackground 与 onCreate 这对回调的共同目标，数据链路才算真正闭环。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-quote-left mr-2" aria-hidden="true"></i>一句话记牢

{class="mt-1"}
后台能活多久，不由你决定，由用户和系统共同决定。你要做的不是对抗回收，而是保证"被杀之后，一切都能接上"。
:::

#### 八、多 Ability 应用：什么时候需要第二个入口

先给结论：大多数应用一个 EntryAbility 加一个 Navigation 栈就够了，页面再多也是在栈里排队，不需要新的 Ability。真正需要第二个 UIAbility 的信号只有一个——你需要一个<strong>完全独立的入口</strong>：从别的应用、卡片或设备拉起时，要进入一段与主界面毫无关系的独立流程。

举两个像样的例子。一个是商家收银：主 Ability 是商品和订单管理，另有一个收银 Ability 专门承接"从收款码、扫码枪拉起，付完款就退"的短流程——它有自己的生命周期，不污染主栈，路由表也干净。另一个是穿戴协同：手机上的运动应用被手表拉起时，直接进入"实时配对"界面，这一段流程和主界面八竿子打不着，塞进主栈只会让"我的 Tab 里怎么有配对页"这种困惑出现。

什么时候<strong>不要</strong>拆也要说清楚：为了"代码整洁"拆 Ability 是伪需求——代码整洁靠模块划分（第 70 章讲的 Stage 主线与模块化思路），不靠入口数量。Ability 拆多了，任务中心混乱、数据共享变难、启动路径变长。页面才是拆分的基本单位，Ability 是入口的基本单位，两者别混。HAP/HAR 管的是代码怎么打包组织，Ability 管的是用户从哪里进来，一个是仓库结构，一个是门脸，不是一回事。

##### 启动模式：一次拉起是新实例还是旧实例

module.json5 里每个 Ability 可以配 launchType：<strong>singleton</strong>（默认，整个应用就一个实例，重复拉起走 onNewWant）、<strong>multiton</strong>（每次拉起都新建实例）、<strong>specified</strong>（按标记决定——同一个 Ability，不同文档各开各的实例，适合多窗口编辑多文档的场景）。绝大多数情况下保持默认 singleton 就对了。误配 multiton 的典型症状是"任务中心里堆了一排同样的窗口，内存哗哗涨"，遇到它先去查这个字段。

##### Ability 之间怎么通信

- <strong>Want 参数</strong>：拉起时把数据放 parameters 里带过去，最常用的方式，解析套路第六节刚讲过。
- <strong>startAbilityForResult</strong>：拉起并等结果，对方干完活把结果带回来——"从地址选择页选一个地址回来"就是这种模式。
- <strong>Call 机制</strong>：不需要界面、只要让对方 Ability 执行一段逻辑时用 startAbilityByCall，主被调双方通过约定方法传数据，适合后台协作。
- <strong>应用级单例与公共事件</strong>：挂在 applicationContext 上的全局状态所有 Ability 都能读；跨进程、跨应用用公共事件广播。

::: div .code-block
:::inline div .code-head
<span>ARKTS · 拉起第二个 Ability 并等结果</span><span class="dots">···</span>
:::

```
import { Want } from '@kit.AbilityKit'

let want: Want = {
  bundleName: 'com.example.shop',
  abilityName: 'PayAbility',
  parameters: { amount: 128, orderId: 'A1001' }
}
let result = await this.context.startAbilityForResult(want)
console.info('支付结果码: ' + result.resultCode)
```
:::

用 startAbilityForResult 走一个完整流程感受一下：外卖应用里点"选择收货地址"，拉起地址 Ability 并等结果；地址页展示列表，用户点选一个，terminateSelfWithResult 把地址带回；发起方的 await 拿到结果，订单页上的地址栏就地更新。整个过程主从分明——发起方只管"要结果"，被拉起方只管"给结果"，中间不需要共享任何全局变量。把 Ability 间协作当成函数调用来设计，接口就清楚；当成"顺便改改对方的数据"来设计，迟早出事。

常见疑问：两个 Ability 能共享同一个 Navigation 栈吗？不能——每个 UIAbility 有自己的窗口和自己的页面体系，栈不跨 Ability。所以页面归属哪个 Ability，在设计期就要想清楚：需要"栈内来回跳"的页面放同一个 Ability，需要"独立入口、独立窗口"的才另开 Ability。

还有个常被问的概念顺手清掉：ExtensionAbility 是"没有界面的 Ability"——表单卡片背后是 FormExtensionAbility，输入法是 InputMethodExtensionAbility，它们由系统按需拉起，生命周期的节奏和 UIAbility 不一样。整个 Stage 模型可以理解成"一个有界面的入口家族 + 一群干杂活的插件家族"，第一节的介绍到这里应该完全展开了。

模块化场景补一句：feature 模块里也能放 UIAbility——把上面说的收银 Ability 连同它的页面一起装进独立 feature 模块，用户没装这个特性包时，收银功能整个缺席，包体和出错面都小一截。入口单元和模块结构配合起来用，才是 Stage 模型的完整打开方式。

#### 九、进程与线程模型：主线程原则、TaskPool 与 Worker

先说进程：鸿蒙上普通应用默认单进程，整个应用跑在一个进程里，跨进程通信对普通开发者来说基本用不上，这里不展开。真正天天打交道的是线程——准确说，是"主线程"和它之外的世界。

主线程是唯一能摸 UI 的线程：绘制、事件分发、组件生命周期、@State 的更新全在它身上排队。由此推出主线程原则：<strong>任何可能超过几十毫秒的活，都不许在主线程干</strong>——大 JSON 解析、图片解码、批量压缩、大文件读写、几千条数据的排序过滤。犯了这条，症状特别典型：列表滑动掉帧、点击半天没反应、动画一卡一卡。安卓篇讲过的"主线程别阻塞"，在这里原样成立，连理由都一样。

##### TaskPool：扔出去就不管了

短平快的独立任务用 TaskPool——你描述任务，系统自己挑线程、自己调度，结果以 Promise 回到主线程：

::: div .code-block
:::inline div .code-head
<span>ARKTS · TaskPool 跑后台计算</span><span class="dots">···</span>
:::

```
import { taskpool } from '@kit.ArkTS'

@Concurrent
function compressCount(paths: string[]): number {
  // 这里跑在子线程，别碰 UI
  let done = 0
  for (let p of paths) {
    // ...压缩逻辑...
    done++
  }
  return done
}

// 主线程：扔进去，等结果
taskpool.execute(compressCount, pathList).then((count: number) =&gt; {
  console.info('压缩完成: ' + count)
  this.refreshUI()   // 结果回到主线程，这里可以更新 UI
})
```
:::

@Concurrent 标记的函数必须自包含——参数传进去，结果传出来，不直接引用外面的组件状态。这个约束不是缺点，是护栏：它逼着你把任务写成"输入到输出"的纯函数，天然好测试、好复用。

##### 错误示范与纠正：主线程上的隐形重活

看一个真实感很强的错误：首页 aboutToAppear 里同步解析一份几百 KB 的城市列表 JSON。本地开发数据少，没感觉；上线后数据涨了，每次进首页都卡一下，用户还以为是网络慢。

::: div .code-block
:::inline div .code-head
<span>ARKTS · 错误示范与纠正</span><span class="dots">···</span>
:::

```
// 错误示范：主线程同步干重活
aboutToAppear(): void {
  let raw = this.readBigJson()      // 主线程读大文件
  this.cityList = JSON.parse(raw)   // 主线程解析几百 KB
}

// 纠正：扔给 TaskPool，回来再赋值
async loadCities(): Promise&lt;string[]&gt; {
  // 内部把"读文件 + 解析"包成 @Concurrent 任务丢进 taskpool
  return await taskpool.execute(parseCitiesTask, filePath)
}

async aboutToAppear(): Promise&lt;void&gt; {
  this.cityList = await this.loadCities()
}
```
:::

纠正版里，"读文件加解析"打包成一个 @Concurrent 任务丢进 taskpool，主线程只等结果。注意赋值那一步还是要回到主线程做——@Concurrent 的函数里别碰 UI 和组件状态，回来再动。这个模式（子线程算，主线程用）是异步界面开发的万能模板。

顺带把概念摆正：ArkTS 的跨线程不是随便共享内存的——线程之间传数据要走"可共享类型"的通道，组件对象、函数引用这类东西搬不过去。这看起来是限制，实际是保护：它从语言层面杜绝了"两个线程同时改一个变量"的整类 bug。并发也不是万能药：任务太碎（几毫秒的小活也丢 TaskPool），调度开销反而比活本身还贵，判断标准还是那条——可能超过几十毫秒才值得扔。

##### Worker：常驻的对话线程

需要长期活着、频繁双向通信的活用 Worker：它有自己的事件循环，你在主线程创建一个，onmessage 收、postMessage 发，用完 terminate 掉：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 主线程与 Worker 对话</span><span class="dots">···</span>
:::

```
// 主线程
import { worker, messageEvents } from '@kit.ArkTS'

let pipeline = new worker.ThreadWorker('entry/ets/workers/PipelineWorker.ets')
pipeline.onmessage = (e: messageEvents) =&gt; {
  this.progress = e.data.step   // 子线程的进度回到主线程
}
pipeline.postMessage({ cmd: 'start' })
// 用完：pipeline.terminate()

// workers/PipelineWorker.ets（子线程内部）
import { worker, ThreadWorkerGlobalScope, messageEvents } from '@kit.ArkTS'

const workerPort: ThreadWorkerGlobalScope = worker.threadWorkerGlobalScope
workerPort.onmessage = (e: messageEvents) =&gt; {
  // ...干长活，随时 postMessage 汇报进度...
  workerPort.postMessage({ step: 1 })
}
```
:::

典型场景是持续的数据流水线、长时间的消息处理。Worker 的数量有系统上限，用完记得 terminate——泄漏一个就常驻一个，比内存泄漏还难察觉。

选型口诀：一次性的、独立的、无状态的活给 TaskPool；长期的、有会话状态的、需要频繁收发的活给 Worker。拿不准就先 TaskPool，等真的需要"常驻对话"再升级成 Worker——从 TaskPool 升 Worker 是顺路，反过来拆就没那么舒服了。跨线程传对象还有个 sendable 的概念：能在线程间安全搬运的数据类型有限制，复杂对象要用可共享的方式声明，具体规则以官方文档为准，初学阶段记住"传简单数据最稳"就够了。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2" aria-hidden="true"></i>小贴士

{class="mt-1"}
怀疑主线程被卡住时，用 DevEco Studio 的 Profiler 看主线程的耗时分布，找到最长的那个函数，它就是你该扔进 TaskPool 的第一个候选。别凭感觉猜，先量再改。
:::

给主线程做体检的具体步骤：连上真机跑应用，打开 Profiler，选中耗时最宽的那一段——它通常就是用户抱怨的那一下卡顿；展开调用栈，找到最耗时的自有函数（排除系统框架的绘制耗时）；把它的输入数据记下来，评估能不能"算一次存结果"；能就扔 TaskPool，不能就做增量与分批。改完再录一遍同一操作，前后对比，改善幅度一目了然。

#### 十、应用入口与桌面交互：图标、名称、快捷方式与卡片

应用骨架的"最后一米"是桌面：用户对应用的第一印象是图标和名字，每天的高频入口是长按菜单和卡片。配置文件里这些字段看着零碎，其实各管一段，这一节把它们串清楚。

##### 图标与名称是谁说了算

app.json5 里的 icon 和 label 是应用级的——桌面图标、设置里的应用名都以它为准；module.json5 里每个 Ability 也有自己的 icon/label，会在任务中心等处显示（具体展示规则视系统版本而定）。名称要多语言就别写死字符串，用资源引用：resources/base/element 放默认语言，zh-CN、en_US 目录各放一份，系统按用户语言自动挑。图标走分层设计——前景层和背景层分开提供，系统统一裁成一致的形状，所以别把圆角直接烧在图片里，形状交给系统裁，你的图标才不会在一排应用里显得"格格不入"。

图标和名称上有三个高频问题：一是自己带圆角和背景，和系统统一形状打架，看起来"大一号"或"缺一角"；二是前景层元素贴边，裁切后缺胳膊少腿，关键元素留在中间区域；三是名字里堆关键词（"某某-专业版-Pro"），商店和桌面显示都会被截断。图标和名称改起来成本低、影响面大，上架前先对照官方设计规范过一遍。

##### 长按图标：快捷方式

用户长按应用图标弹出的那排入口，靠 module.json5 里的 shortcuts 配置：每一项带 shortcutId、名称、图标和 wants（指向哪个 Ability、带什么参数）。典型用法：相机应用放"自拍""录视频"，记账应用放"记一笔""看本月账单"。

配一个快捷方式的完整步骤：在 module.json5 里找到入口 Ability 的配置，加 shortcuts 列表；每一项写好 shortcutId 和显示名称（走字符串资源，方便多语言）；wants 里指定目标 Ability，需要带参数就填进 parameters；保存后重新安装应用；桌面长按图标验证；点进去确认落地页在"无首页上下文"的情况下表现正常。第三步和第六步最容易漏——参数没配上，快捷方式就只是个换了个名字的普通启动。

配置原则和页面路由一样：快捷方式直达的页面要能脱离正常流程独立成立，用户从桌面一击而入时，参数解析按第六节的套路处理，别假设"用户一定从首页来"。

##### 桌面卡片：不用打开应用的入口

卡片是比快捷方式更进一步的桌面交互：用户把"未来三天天气""今日步数"直接钉在桌面上，数据由应用在后台更新。开发侧是 FormExtensionAbility，卡片本身用 ArkTS 写，点击卡片通过 postCardAction 跳进应用。卡片的尺寸规格、刷新策略（定时刷新、按需刷新）官方都有明确约束。定位上记住一句话：卡片是入口，不是迷你版应用——往卡片上塞一屏都装不下的东西，是设计事故。完整玩法在第 79 章元服务部分细讲。

深链接上一节已经覆盖（App Linking 与 scheme），这里补一个入口视角的清单：桌面图标、长按快捷方式、卡片、通知、链接——这五个口子都可能把用户送进你的任意页面。把"从任意入口进来都要能正确落页"当作验收标准，上线前挨个入口点一遍，比上线后收到"点通知进错页面"的反馈体面得多。

- 应用名与图标在浅色和深色壁纸下都看得清（两种桌面各截一张图看看）。
- 每个快捷方式点进去都带参数、都能落对页，返回键不会把用户带进"没有来路"的死页。
- 卡片上的信息一句话说得完，点击区域有明确的去向。
- 所有入口（通知、链接、卡片、快捷方式）在冷启动和热启动下各跑一遍。

这份清单每次发版前过一遍，桌面交互这一层基本不会翻车。入口层的问题有个共同点：单独看都是小事，叠加起来就是"这应用怎么怪怪的"的整体印象。

#### 十一、Stage 模型常见问题门诊

这一节像门诊病历：症状、大概率原因、处方。排查骨架类问题时对号入座，再按处方验证。这些病例的共同点是——症状看起来像玄学，原因全在生命周期和配置里。

<strong>病例一</strong>：点通知打开应用，冷启动参数一切正常，应用挂在后台时再点却没反应。大概率原因：只在 onCreate 里解析了 Want，热启动走的是 onNewWant，参数根本没人接。处方：onCreate 和 onNewWant 两个回调都调同一个解析函数，解析结果统一写进 AppStorage，由页面按需消费。

<strong>病例二</strong>：刚切后台再回来，输入框内容都还在；放了一晚上再打开，应用像第一次安装一样从首页开始，填了一半的表单没了。原因：前者是挂起（内存还在），后者是被回收（进程没了，重启重建）。处方：把"内存态靠不住"刻进脑子，onBackground 里持久化关键数据，onCreate 里检查有没有未完成的草稿要恢复。判定标准很简单——用户丢了这条数据会不会骂你？会，就落盘。

<strong>病例三</strong>：PersistentStorage 明明写了，重启后却没恢复。大概率是两件事之一：persistProp 调用太晚，有代码抢在它之前往 AppStorage 写了同名键，绑定被冲掉；或者存了不支持的类型。处方：persistProp 全部挪到 EntryAbility 的 onCreate 开头集中调用；只存简单类型和小对象；重启后主动读一遍验证。

<strong>病例四</strong>：别的应用拉不起自己的应用，startAbility 静默失败。按顺序查三件事：目标 Ability 的 exported 是不是 false；隐式拉起时 action、entity、uri 的声明和构造的 Want 是不是逐字对得上（大小写也算错）；走了 App Linking 的话，域名校验文件有没有按官方要求部署生效。三项里最常见的是第二项——把 action 当普通字符串随手拼，差一个字符系统就当没看见。

<strong>病例五</strong>：嵌套导航里按返回键，不是回到上一页而是直接退出了应用。原因多半是子 Navigation 没有接管返回事件，返回信号穿透到了 Ability 层。处方：检查子栈的配置与页面结构，把返回逻辑显式交给自己这一层处理（NavDestination 支持自定义返回拦截），真机上逐层点一遍返回键验证。

<strong>病例六</strong>：应用越用越卡，某个列表页来回进出几次后回调还重复触发。经典内存泄漏：EventHub.on、emitter 监听、观察者注册了没注销，页面销毁了监听还挂着，甚至越积越多。处方：注册和注销成对出现——aboutToAppear 里 on，aboutToDisappear 里 off，写的时候就把这两行并排放，谁也不许单身。

<strong>病例七</strong>：任务中心出现一排重复窗口。launchType 被误配成 multiton，或者 specified 模式的实例标记没管理好，系统把同一个目标当成了多个不同实例。处方：除非真有多实例需求，一律 singleton；真要用 specified，就把实例归属规则写成一条清晰的函数，别让它靠运行时的巧合工作。

<strong>病例八</strong>：申请了长时任务，后台播放还是中途被杀。查两点：backgroundModes 声明的类型与申请时的枚举是否一致、与实际行为是否一致（声明音乐却在干别的）；系统设置里用户是否手动限制了该应用的后台活动（电池优化这类开关，各机型路径不同，给爸妈远程排查时先看这里）。

<strong>病例九</strong>：冷启动后先白屏一小会儿才出内容。多半是主页面加载被重活拖住了：onWindowStageCreate 里同步做了大文件读取、大批量数据初始化，首帧迟迟画不出来。处方：首帧前只做"必须有"的事，重初始化挪到首帧之后（或用 TaskPool 丢出去）；加载期间给个占位骨架屏，让用户知道应用活着。

<strong>病例十</strong>：启动参数解析都写对了，但偶尔跳错页或白屏。查"跳转时机"：onWindowStageCreate 里 loadContent 之后立即跳，和页面加载本身在赛跑。处方：启动参数只作为"待办"记录在 AppStorage，真正的跳转挂在主页面的 aboutToAppear 或内容就绪之后——第六节的固定套路正是为这个问题设计的。

<strong>病例十一</strong>：桌面卡片点击没反应或落错页。查三件事：postCardAction 的 action 是否写了 router；abilityName 是否与 module.json5 里的名字逐字一致；params 里的键名与 Ability 里解析的是否一致。卡片侧和应用侧各改过一次名字没同步，是最常见的翻车点。

<strong>病例十二</strong>：通知带过来的订单号拿去做数字比较，判断永远不成立。原因：Want parameters 里的值到你手里可能是字符串形式的数字，拿字符串做数字比较会给你惊喜。处方：取出来先做类型转换再比较——前面代码里的 as string、as number 不是装饰，是提醒，转换这一步省不得。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2" aria-hidden="true"></i>小贴士

{class="mt-1"}
门诊的通用第一步永远是：把生命周期日志打出来（本章第二节的老习惯），用 DevEco Studio 的 HiLog 过滤自己应用的业务域名，把回调串成时间线；命令行上用 hilog 直接看也行（hdc 相当于安卓的 adb）。九成骨架问题，看一遍"应用被拉起时到底走了哪些回调"就有眉目，剩下的再上工具。
:::

#### 十二、三平台骨架对照：一张表看懂安卓、iOS 与鸿蒙

本章到站了。把三平台的"应用骨架"并排放一起，转平台的同学对号入座，一次看全：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
  <thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">概念</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">安卓</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">iOS</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">鸿蒙</th></tr></thead>
  <tbody>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">入口配置文件</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AndroidManifest.xml</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Info.plist</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app.json5 + module.json5</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">有界面的入口单元</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activity</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UIWindowScene（Scene 生命周期）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UIAbility</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">页面单元</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fragment / 第二个 Activity</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ViewController</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">NavDestination</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">页面栈</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">返回栈（系统管理）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UINavigationController</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">NavPathStack（开发者持有）</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">前后台回调</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onPause / onResume / onStop</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">scenePhase（.active/.inactive/.background）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onForeground / onBackground</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">保存数据的关键时机</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onPause / onStop</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">scenePhase 变 .background 时</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onBackground</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">隐式拉起</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Intent + IntentFilter</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URL Scheme / Universal Links</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Want + skills / App Linking</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">后台任务</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">前台服务 / WorkManager</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">后台模式 / BGTaskScheduler</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">长时任务 / 短时任务 / 延迟任务</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">线程协作</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">主线程 + 协程 / Handler</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">主线程 + GCD / async-await</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">主线程 + TaskPool / Worker</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">桌面快捷入口</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">快捷方式 / Widget</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Quick Actions / WidgetKit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">shortcuts / 桌面卡片</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">运行时权限</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">清单声明 + 代码申请弹窗</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Info.plist 声明 + 代码申请</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">module.json5 声明 + requestPermissionsFromUser</td></tr>
  </tbody>
</table>
```
:::

表能帮你建立映射，但有三处"像而不同"要专门点破。第一处是页面栈：安卓的返回栈由系统管理，你在 Activity 之间跳转其实摸不到栈本体；鸿蒙的 NavPathStack 是你手里的对象，能存、能遍历、能恢复——自由度高，责任也高，忘了保存就是你的锅。第二处是 iOS：它没有 Activity 这种"可被指定页面拉起的独立入口单元"，一个应用通常一个 Scene 体系打天下，所以从 iOS 转来的人要对"应用可以被别人拉到某个具体页面"重新建立直觉。第三处是后台：三平台都在收紧后台，鸿蒙的三张牌和安卓的前台服务、iOS 的后台模式在精神上完全一致——你要后台，就亮明身份并接受监督。

迁移建议压缩成三条。一是别逐行翻译，先按本章把目标平台的骨架走一遍冷启动、前后台、销毁的完整流程，建立回调时序的手感，这比背 API 快。二是把"状态住几楼"的分层习惯带过去，这套分层在三个平台上通用，只是工具名字不同。三是生命周期日志的老习惯保持——每个回调一行日志，三个平台各跑一遍，你会得到三张长得惊人相似的时间线；看着这三条时间线写代码，跨平台不再是玄学。

这张表反过来读也成立：三平台的骨架概念高度收敛，意味着你在一个平台学到的设计习惯（状态分层、生命周期打日志、后台任务亮明身份）可以直接搬去另外两个平台，真正要重学的只有工具名和平台特有变量——鸿蒙的分布式、安卓的后台自由度、iOS 的严格沙盒。骨架学透了，平台只是方言。骨架是本章的地图，出了地图还有荒野：具体到转场动画、多窗口、折叠屏适配，各平台的差异会重新放大。但只要生命周期和状态这两根主梁立住了，剩下的都是装修问题。

#### 十三、本章 FAQ

<strong>问：Navigation 和 router 我到底该学哪个？本章两个都出现了。</strong><br>答：学 Navigation，它是官方现在的推荐主线，新项目直接用它起步。router 没有被废弃，老项目、超简单的两三个页面场景里还能见到，看得懂就行，不用专门去练。

<strong>问：AppStorage 和 LocalStorage 名字这么像，我该用哪个？</strong><br>答：默认 LocalStorage（同一个 Ability 的页面间共享），只有当状态真的需要跨 Ability、跨模块可见时才升到 AppStorage。能用小的范围就用小的范围——状态的作用域越窄，排查问题越省事。

<strong>问：PersistentStorage 能不能当数据库用？我把用户所有设置都塞进去行不行？</strong><br>答：塞"设置"行，塞"数据"不行。它适合几十个键值对量级的配置项；用户产生的内容（笔记、记录、图片列表）走 preferences 或数据库。每次变化都写盘的机制决定了它扛不住高频大对象。

<strong>问：我该在哪个回调里发首屏网络请求？onCreate 还是页面 aboutToAppear？</strong><br>答：常规放页面 aboutToAppear——页面挂了请求好取消，路由参数也拿到手了。只有"启动就要、与具体页面无关"的全局数据（配置开关、登录态刷新）才放 Ability 层的 onCreate。原则：跟着页面走的数据，跟着页面发起。

<strong>问：onDestroy 里能不能发个网络请求，把用户最后一批数据传上去？</strong><br>答：不可靠。onDestroy 到进程退出之间留给你的时间没有保证，网络请求很可能没发出去就没了。关键数据要在 onBackground 就落盘或上传，onDestroy 只做释放资源的动作。把"最后时刻"安排在 onBackground，是这类需求的正解。

<strong>问：生命周期日志具体怎么打？会不会太吵？</strong><br>答：给每个回调一行固定格式的日志（回调名加关键参数），用统一前缀方便过滤。调试期开着，发版前把这批日志降级或关掉。吵不是问题——噪音才是：只打你关心的节点，别把每次变量变化都记上。

<strong>问：我的应用就是需要后台常驻怎么办？运动记录总不能切个后台就停吧。</strong><br>答：运动记录对应的正是长时任务里的运动、定位类场景，按类型申请，状态栏亮明身份，这是系统支持的正规军。反过来，如果你的需求套不上任何一种长时任务类型，那大概率说明用户并不真的需要它常驻——硬保活既过不了审核，也耗用户的电。

<strong>问：TaskPool 和 Worker 我看着都一样，随便选一个行吗？</strong><br>答：行，但很快会撞墙。TaskPool 是"外包"：任务扔出去，系统调度，完事即走；Worker 是"雇员"：常驻、双向通信、要自己管理生命周期。先 TaskPool 后 Worker 的升级路线最顺，反过来先上 Worker 的项目，后期往往留下一堆忘了 terminate 的线程。

<strong>问：为什么我的 Ability 会被拉起两次？onCreate 里初始化的逻辑跑了两遍。</strong><br>答：先查 launchType 是不是被误配成 multiton；再查是不是多个入口同时拉起（卡片和通知都指向它）；还有一种情况是 specified 模式的实例标记没设计好，系统认为这是两个不同实例。从"谁拉起的我、什么模式"两个方向缩小范围。

<strong>问：多个 Ability 的时候，全局状态放 AppStorage 还是各自 Ability 自己管？</strong><br>答：先问"两边是否真的需要同步"。收银流程的中间态别进 AppStorage，Ability 之间用 Want 和结果回传就够；真要共享的全量状态（登录态、主题）才放应用级。Ability 边界本来是隔离墙，别用全局变量把墙拆了。

<strong>问：个人开发者能玩 App Linking 吗？听起来要服务器、要域名、要市场审核，好重。</strong><br>答：确实比自定义 scheme 重，但它换来的体验和防劫持是实打实的。轻量起步的顺序：先用 scheme 验证跳转逻辑，产品成型后再上 App Linking；域名和校验文件是一次性配置，之后不用维护。具体要求以应用市场和官方文档的现行规则为准。

<strong>问：页面参数应该用 Want 传、AppStorage 传还是路由参数传？我有点乱。</strong><br>答：记住"传给谁"就清楚了。页面到页面的临时参数，走路由参数（pushPathByName 的第二个参数）；跨 Ability 的启动意图，走 Want；全局广播式的状态（改主题、改头像），走 AppStorage 或事件。三者别混用——把页面参数塞进 AppStorage，应用退出再进来参数还在，那不是功能，是事故。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hand-pointer mr-2" aria-hidden="true"></i>来动手：给第 73 章的项目做一次"骨架体检"

{class="mt-1"}
给 EntryAbility 的每个生命周期回调加一行日志；跑一遍冷启动、切后台、回前台、手动划掉，把日志按顺序抄下来对照本章的生命周期流程；再人为制造一次回收（后台清空或等系统回收，视机型方式不同），确认草稿能从 onBackground 的持久化里接回来。做完这三步，本章的内容就从"看过"变成"装进项目里了"。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- Stage 模型三层：应用 → 模块（Module）→ 能力（UIAbility/ExtensionAbility）
- module.json5 对应 AndroidManifest：声明 Ability、权限、入口
- 生命周期：onCreate → onWindowStageCreate → Foreground/Background → onDestroy
- 页面跳转 router.pushUrl 带参数；官方新推荐是 Navigation 组件栈
- 权限三档：system_grant / user_grant / 受限开放——最小化授权原则通用
- 后台可能被回收：onBackground 里持久化关键数据；分布式下能力可能在别的设备拉起，状态设计留一手
:::
