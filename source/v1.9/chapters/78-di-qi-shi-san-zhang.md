---
id: di-qi-shi-san-zhang
num: 73
nav: 第七十三章：ArkUI 声明式界面
toc: default
kind: chapter
after_part: hongmeng-kai-fa-pian
---

### 第七十三章：ArkUI 声明式界面——组件、布局与状态管理

{class="chapter-intro mb-4"}
语言有了，这一章搭界面。ArkUI 的语法结构和 Compose/SwiftUI 高度同构：<strong>build() 里声明 UI 树，链式调用设置属性，状态驱动刷新</strong>。学完这章，你就能把设计稿变成界面了。

先建立一个总观念：声明式 UI 的世界里，不是"操作界面的指令"，是"界面的描述"。传统 UI 开发像指挥木偶，"把这个按钮移过去、把那个文字改掉"；声明式像写剧本："当状态是这样时，界面长这样"。状态一变，框架自动重演剧本。理解了这个心智模型，后面的布局、状态、导航都会顺理成章。

::: div .quick-read
##### 本章速读（5 分钟版）
这一章搭界面：ArkUI 和 Compose、SwiftUI 高度同构——build() 里声明 UI 树，链式调用设置属性，状态驱动刷新。先立一个总观念：你写的不是"操作界面的指令"，而是"界面的描述"，当状态是这样时，界面长这样；状态一变，框架自动重演剧本。理解了这句，布局、状态、导航都会顺理成章。
最关键的有三件事。第一，<strong>布局三件套走天下</strong>：Column 竖排、Row 横排、Stack 叠放（后写的子组件在上层），对齐用 justifyContent 和 alignItems，和前端 Flexbox 完全同构；撑满记 .width('100%')，列表用 List + ForEach，网格用 Grid，嵌套超过五六层就该拆组件了。第二，<strong>状态管理选对装饰器就成功一半</strong>：@State 管组件自己、@Prop 是父传子单向拷贝、@Link 是父子双向绑定，拿不准就问一句"子组件改了，父组件需不需要知道"。第三，<strong>几条从第一天就该守的规矩</strong>：长列表用 LazyForEach 懒加载、键值别用下标（键值乱则刷新乱、列表闪）；长度用 vp、字号用 fp，代码里出现 px 当 bug 处理；深色模式靠 dark 资源限定词目录配语义色，全文搜一遍色值把硬编码清干净。
今天就能做的最小动作：挑一张你喜欢的 App 截图，在纸上画"格子图"，最外层是 Column 还是滚动容器？哪一排是 Row？哪两块叠在一起？——然后用三件套把这页静态界面搭出来。看十个界面、画十张格子图，你的"布局眼"就有了。
最大的坑是把命令式直觉带进声明式世界：脑子里想"我怎么让界面变"而不是"我该让哪个数据变"，九成的诡异 bug 出在这里，永远只改状态，让界面自己长出来。其余几个高频坑：@Prop 和 @Link 随手选（选错不崩溃不报错，只是界面和数据悄悄不同步）；深色模式只把背景换黑（文字对比度、白底图标、阴影层级都要跟着变，一处硬编码颜色就破功）；组件拆过头（把一个孤零零的 Text 也包成组件，白添开销）。交工前过一遍验收：Profiler 看滑动帧率、深浅色各切一轮、系统字号调到最大再看。导航用 Navigation 管页面跳转，资源统一用 $r() 引用，多语言和深色都靠资源目录自动切换：字符串全部资源化是这一切的前提。组件和属性不用背，高频那几个用熟，其余靠代码补全和官方文档现查。
##### 速查表
- 布局三件套：Column 竖排、Row 横排、Stack 叠放（后写在上），对齐像 Flexbox
- 核心心法：永远只改状态，界面自己长出来，别绕过状态手动"操作"界面
- 状态三层：@State 自己的、@Prop 单向拷贝、@Link 双向绑定，选错就悄悄不同步
- 长列表铁律：数据一多就上 LazyForEach，键值用稳定 id 别用下标
- 单位纪律：长度 vp、字号 fp，代码里出现 px 当 bug 处理
- 深色模式：dark 资源限定词目录 + 语义色，硬编码色值是"半黑半白"的元凶
- 拆组件信号：同一结构出现第二次，或 build() 长到要滚动才看完
- 验收三检查：Profiler 看帧率、深浅色切两轮、字号调最大再看一遍
:::

<div class="version-anchor">本章界面路径按 iOS 18.x / HarmonyOS 5.x / Android 15 核对（2026 年 11 月）。你的机型或系统版本不同，菜单名字和位置可能对不上——以你手机上显示的为准。</div>


#### 一、布局三件套：Column、Row、Stack

ArkUI 的布局容器极少但够用：<strong>Column</strong>（纵向排）、<strong>Row</strong>（横向排）、<strong>Stack</strong>（叠放）。对齐用 justifyContent（主轴）和 alignItems（交叉轴）控制：这和前端的 Flexbox 完全同构：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 布局示例</span><span class="dots">···</span>
:::

```
Column({ space: 12 }) {
  Text('标题').fontSize(20).fontWeight(FontWeight.Bold)
  Row({ space: 8 }) {
    Text('标签').backgroundColor('#eef')
    Text('时间').backgroundColor('#efe')
  }
  .width('100%')
  .justifyContent(FlexAlign.SpaceBetween)

  Stack({ alignContent: Alignment.BottomEnd }) {
    Image($r('app.media.photo')).width('100%')
    Text('水印').fontSize(12).padding(4)
  }
}
.padding(16)
```
:::

记住两个高频方法：<strong>.width('100%')</strong> 让容器撑满（默认子组件是包裹内容），<strong>.padding()/.margin()</strong> 与 CSS 同名同义。列表用 <strong>List + ForEach</strong>（相当于 RecyclerView/UITableView），网格用 <strong>Grid</strong>。

三件套各自的"性格"值得单独说清。Column 是竖向的骨架，几乎所有页面的根都是它，因为手机屏幕是竖的；它的 space 参数控制子元素间距，比逐个加 margin 干净得多。Row 是横向的骨架，典型的用法是"左图标 + 中文字 + 右箭头"的设置项行。Stack 是叠放，图片上叠水印、卡片上叠角标、底层播放器上层控制条，凡是"两层东西摞在一起"的场景都用它；alignContent 决定叠放的对齐位置（四角与居中）。

嵌套是布局的日常：一个 Column 里套 Row、Row 里再套 Column，层层组合出复杂界面。但嵌套有度，每多一层就多一次测量与布局的开销，超过五六层的深嵌套通常意味着"该拆组件了"。把重复出现的结构抽成 @Component（第 72 章的装饰器），界面树会立刻清爽。

一条实用的顺序：布局先跑通再优化。Row / Column / Stack / List 这几样组合起来，能覆盖绝大多数界面；真出现性能问题，再用 DevEco 的 Profiler 去定位，别一上来就琢磨优化。

##### 常见布局问题门诊

三个新手高频问题提前给出答案。问题一："我的元素怎么挤在一起了？"：多半是忘了给 Row/Column 设 space 或给子元素加 margin。间距是布局的呼吸感。问题二："图片为什么溢出了容器？"：Image 默认按原始尺寸显示，给它套 .width('100%') 或固定尺寸，或者用 .objectFit(ImageFit.Cover) 控制裁切。问题三："点击没反应？"，检查有没有给组件加 .onClick()，以及它是否被上层 Stack 的透明层挡住了（Stack 的叠放顺序：后写的在上面）。

#### 二、状态管理：谁变了，刷哪里

ArkUI 的状态管理是三层结构，选对装饰器就成功一半：<strong>@State</strong> 管组件自己；<strong>@Prop</strong> 父传子（单向拷贝）；<strong>@Link</strong> 父子双向绑定。来一个完整的"开关卡片"：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 父子组件通信</span><span class="dots">···</span>
:::

```
@Component
struct SettingItem {
  @Prop title: string = ''
  @State isOn: boolean = false

  build() {
    Row() {
      Text(this.title).fontSize(16).layoutWeight(1)
      Toggle({ type: ToggleType.Switch, isOn: this.isOn })
        .onChange((on: boolean) =&gt; { this.isOn = on })
    }
    .width('100%')
    .padding(12)
  }
}

@Entry
@Component
struct SettingsPage {
  @State items: string[] = ['Wi-Fi', '蓝牙', '勿扰模式']

  build() {
    Column() {
      ForEach(this.items, (item: string) =&gt; {
        SettingItem({ title: item })
      })
    }
  }
}
```
:::

注意两个细节：<strong>ForEach</strong> 是循环渲染（第一个参数是数据源）；<strong>layoutWeight(1)</strong> 等价于 CSS 的 flex:1。状态装饰器选错（该用 @Link 用了 @Prop）会导致"子组件改了父组件不知道"，这是 ArkUI 新手第一坑。

把三个装饰器的选择逻辑说成大白话：@State 是"这个数据只有我自己用"；@Prop 是"父组件给我一个值，我可以改自己的副本但不通知它"；@Link 是"父子共享同一个数据源，谁改都同步"。选错的典型症状就是"界面上改了、数据没变"或"数据变了、界面没刷"，先回头检查装饰器，再查逻辑。

状态管理的进阶还有两个方向：应用级状态（AppStorage，跨页面共享的键值仓库）和持久化状态（PersistentStorage，重启不丢）。页面级用装饰器，应用级用 AppStorage，持久化交给 PersistentStorage，三层各司其职，别把所有状态都塞进页面。

##### V1 与 V2：两套装饰器，先分清再读代码

查资料时迟早遇到两套装饰器并存的写法。同一组件里 V1 与 V2 不能随便混搭；接手老项目先看它整体用的是哪一代，再决定沿用还是整体迁移。对照表收好：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">用途</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">V1（旧资料常见）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">V2（新项目常见）</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">组件声明</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Component</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@ComponentV2</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">组件内状态</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Local</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">父传子</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Prop</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Param</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">父子双向</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Link</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Param + @Event 组合（@Once @Param = 只同步一次）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">嵌套对象观察</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Observed + @ObjectLink</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@ObservedV2 + @Trace</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">状态变化回调</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Watch</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Monitor</td></tr>
</tbody>
</table>
```
:::

三条使用建议：只在一个组件里用的状态放 @Local，要跨页面共享的提到应用级状态或数据源层；能算出来的派生值就现算，别再存一份：存两份必然要处理同步；这份对照表是「读懂老代码」用的，写新代码以你当前 SDK 版本的官方文档为准。

版本行为变更也要留心：官方 5.1.0(18) 说明里就有 ArkUI 的 <code class="inline">getKeyboardAvoidMode</code> 返回值变更、XComponent 上 <code class="inline">renderFit</code> 显示效果变更等条目，升级别只看编译能不能过。

#### 三、导航与资源：从一页到多页

多页面跳转用 <strong>Navigation</strong> 组件或 Router（页面级路由，router.pushUrl 类似 Intent/Segue；注意官方已宣布 Router 仅维护不演进，新项目请优先用 Navigation）；资源引用统一用 <strong>$r('app.type.name')</strong> 语法：$r('app.string.app_name') 取字符串，$r('app.media.icon') 取图片，$r('app.color.primary') 取颜色。字符串等资源放在 resources/base/element/ 下的 JSON 里，配合 zh-CN/en_US 目录做多语言，和安卓的 strings.xml 一个思路。

Navigation 的"路由表"模式值得提前理解：与其在每个页面里写跳转逻辑，不如在应用启动时注册一张"页面名 → 组件"的路由表，跳转时按名字入栈出栈。这种方式让页面结构一目了然，也让"深链接"（从通知直接跳到某一页）变得自然。第 74 章讲 UIAbility 时会把"入口"和"页面路由"接起来。

资源的组织也有讲究：字符串资源化不仅是为了多语言，更是为了"文案与代码分离"，产品经理改文案不用动代码，评测不同文案的效果也不用重新编译。图标、颜色同理：统一放在资源目录里，换主题色时改一处全局生效。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：做出"设置页"

{class="mt-1"}
用 Column + SettingItem 复刻手机设置首页的三行（Wi-Fi、蓝牙、显示），再给每行加一个箭头图标（Row 里追加 Image 或 Text('›')）。完成后用预览器看效果，布局、状态、组件复用三个概念你已经全部用上了。
:::

#### 四、常用组件速查：Text、Image、Button 这些"乐高块"

布局是骨架，组件是肉。ArkUI 的内置组件有几十个，但你日常写界面，翻来覆去用的就十几个，像乐高，基础块不多，能拼出一切。这一节把高频组件逐个过一遍：每个讲"干什么用、哪几个属性最常调、新手在哪翻车"。先给一张速查表，后面挑重点细讲：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">组件</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">干什么用</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">高频属性与事件</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">显示文字</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">fontSize、fontWeight、maxLines、TextOverflow</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">显示图片</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">objectFit、alt、onError</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">按钮</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">type、onClick、stateEffect</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextInput / TextArea</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">单行 / 多行输入</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">placeholder、type、onChange、maxLength</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Toggle</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">开关</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">type、isOn、onChange</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Checkbox / Radio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多选 / 单选</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">select、onChange</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Slider</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">滑块（亮度、音量类）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">value、min、max、step、onChange</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Progress / LoadingProgress</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">进度条 / 转圈</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">value、total、ProgressType</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Search</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">搜索框</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">placeholder、onSubmit、onChange</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Divider</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分隔线</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">strokeWidth、color、vertical</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swiper</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">轮播（引导页、Banner）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">loop、autoPlay、indicator</td></tr>
</tbody>
</table>
```
:::

表里的"高频属性"就是每个组件 80% 场景下你要碰的东西。没列进表的（如 Marquee、DataPanel、Gauge 这类专用件），用到时查官方文档即可，别提前背。

##### Text：最简单，也最容易被低估

Text 看着没技术含量，坑却不少。长文本的处理是第一名：<strong>maxLines 限行数，TextOverflow.Ellipsis 限溢出样式</strong>，两个要一起用，只写 Ellipsis 不写 maxLines，很多场景下省略号压根不出现：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 文本的常见设置</span><span class="dots">···</span>
:::

```
Text('这是一段可能特别长的介绍文案，超出两行就要截断')
  .fontSize(14)
  .maxLines(2)
  .textOverflow({ overflow: TextOverflow.Ellipsis })
  .lineHeight(20)
  .textAlign(TextAlign.Start)
```
:::

第二个被低估的能力是 copyOption：给 Text 设置 <code class="inline">.copyOption(CopyOptions.InApp)</code> 后，用户长按就能复制这段文字。客服电话、订单号、验证码提示这类内容，加上它，用户体验立刻不一样。

##### Image：撑爆布局的惯犯

Image 的坑在尺寸。它默认按原始分辨率显示，一张 4000 像素的照片塞进来，直接把你的布局顶出屏幕。标准动作就一个：<strong>给 Image 套 .objectFit(ImageFit.Cover)</strong>——按容器裁切填满，类似 CSS 的 object-fit: cover。想完整显示不裁切就用 ImageFit.Contain（可能留白）。另外三个实用项：alt 给加载中的占位图；onError 里做降级（网络图挂了就换本地图）；圆角头像用 .borderRadius() 或干脆 .clipCircle？不存在的，直接 borderRadius 设成宽度一半就行。

##### TextInput 和 Button：表单的黄金搭档

登录、注册、搜索、改名，凡是让用户打字的地方都是这对搭档。来一段能直接抄的登录表单：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 登录表单</span><span class="dots">···</span>
:::

```
Column({ space: 12 }) {
  TextInput({ placeholder: '手机号' })
    .type(InputType.Normal)
    .maxLength(11)
    .onChange((v: string) =&gt; { this.phone = v })

  TextInput({ placeholder: '密码' })
    .type(InputType.Password)
    .onChange((v: string) =&gt; { this.pwd = v })

  Button('登 录', { type: ButtonType.Capsule })
    .width('100%')
    .onClick(() =&gt; { this.doLogin() })
}
```
:::

三个细节：InputType.Password 自动打码；maxLength 挡住超长输入（比提交后再校验体验好）；Button 的 type 换成 ButtonType.Circle 就是圆钮。输入完点键盘上的"前往"想触发登录，用 onSubmit 回调，别让用户非得抬手点按钮。

##### Toggle、Slider、Checkbox：控件三兄弟

Toggle 在本章第二节的例子里已经出现过，Switch 形态最常用，selectedColor 能改选中色。Slider 管连续值：亮度、音量、字体大小。它的 onChange 回调会随拖动连续触发，如果你在回调里做重活（比如实时存数据库），记得节流，拖一下触发几十次，谁也扛不住。Checkbox 管多选，Radio 管单选，配合 onChange 维护一个布尔或值字段就够。

##### 点睛的小件们

Progress 显示确定进度（下载百分比），LoadingProgress 是那个一直在转的圈（不知道要多久时的"正在加载"），两个别混用：能算出百分比的用 Progress，算不出的用 LoadingProgress。Search 是自带放大镜图标的搜索框，省得你自己拼图标。Divider 画分隔线，比塞一个 1 像素高的 Text 干净得多。Swiper 做轮播，引导页、首页 Banner 都靠它。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2" aria-hidden="true"></i>小贴士

{class="mt-1"}
所有组件共享一套"通用属性"：尺寸。内外边距、背景、圆角、透明度、可见性（visibility）、点击事件（onClick）……不管是什么组件，这些方法都能链上去。记住了这一点，你就不用逐个组件背属性——通用的一套走天下，组件特有的那几个才是要查文档的。
:::

#### 五、列表进阶：LazyForEach、分组与下拉刷新

先看一个经典翻车现场：你用 ForEach 塞了五百条数据进 List，预览器里好好的，真机上一滑就掉帧。原因很简单<strong>ForEach 一次把所有条目全建出来</strong>，五百个组件对象、五百次布局，手机还没滑呢内存先红了。解法是 LazyForEach：名字里带 Lazy（懒），只在条目即将滚进屏幕时才创建，滚出去就回收。数据量一大的列表，都用它。

LazyForEach 和 ForEach 的用法差别在于：它要求你提供一个"数据源对象"，实现官方的 IDataSource 接口——框架靠它知道"一共多少条、第几条是什么、数据变了通知谁"。写起来比 ForEach 多几行，但这是标准姿势：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 懒加载列表</span><span class="dots">···</span>
:::

```
class MsgDataSource implements IDataSource {
  private list: Msg[] = []
  private listeners: DataChangeListener[] = []

  totalCount(): number { return this.list.length }
  getData(i: number): Msg { return this.list[i] }

  registerDataChangeListener(l: DataChangeListener) {
    this.listeners.push(l)
  }
  unregisterDataChangeListener(l: DataChangeListener) {
    this.listeners = this.listeners.filter(x =&gt; x !== l)
  }

  pushFront(m: Msg) {
    this.list.unshift(m)
    this.listeners.forEach(l =&gt; l.onDataAdd(0))
  }
}

List() {
  LazyForEach(this.dataSource, (m: Msg) =&gt; {
    ListItem() {
      MsgRow({ msg: m })
    }
  }, (m: Msg) =&gt; m.id)
}
.cachedCount(5)
```
:::

注意最后一行的 keyGenerator（第三个参数）：<strong>键值必须稳定且唯一</strong>。用数组下标当键值是新手高频错误：列表头部插入一条，后面所有条目的下标都变了，框架以为全变了，要么整列表重建（白闪一下），要么内容对错位。用业务上稳定的 id（消息 id、商品 id）当键值。

##### ListItemGroup：带"组头"的列表

通讯录按字母分节、设置页按"网络 / 蓝牙 / 通知"分块，这种"组头 + 组内容"的结构用 ListItemGroup：<strong>header 参数放组头，里面再装若干 ListItem</strong>。组头可以吸顶（sticky），滑到哪一组，哪一组的标题就钉在列表顶上，iOS 通讯录那种效果，ArkUI 里是 ListItemGroup 的现成能力，不用自己监听滚动去算。

##### 下拉刷新与加载更多

下拉刷新不用自己监听手势，用现成的 Refresh 组件把 List 包起来：下拉超过阈值自动触发 onRefreshing 回调，你在回调里请求新数据，请求完把 refreshing 状态置回 false，动画自动收回：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 下拉刷新</span><span class="dots">···</span>
:::

```
Refresh({ refreshing: this.isRefreshing }) {
  List() {
    LazyForEach(this.dataSource, (m: Msg) =&gt; {
      ListItem() { MsgRow({ msg: m }) }
    }, (m: Msg) =&gt; m.id)
  }
}
.onRefreshing(() =&gt; {
  this.reload()   // 完成后把 isRefreshing 置回 false
})
```
:::

"上滑加载更多"走另一条路：监听 List 的 onReachEnd（滚动到底）或用 LazyForEach 的 cachedCount 提前量，快滚到底时提前创建后面几条，顺手把下一页数据请求发出去。两种常见组合：<strong>下拉用 Refresh，上滑用 onReachEnd + 底部放一个 LoadingProgress 当"加载中"的尾巴</strong>。加载完没有更多了，把尾巴换成一句"没有更多了"，别让用户对着一个永远在转的圈发呆。

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>避坑提醒

{class="mt-1"}
cachedCount 不是越大越好。它决定"屏幕外提前多建几条"，设太大会让一次滚动的创建成本暴涨，低端机上反而掉帧。默认值通常就够，真机卡了再调，调完用真机验证，预览器不代表真机手感。
:::

#### 六、动画与转场：让界面"动起来"的三板斧

声明式 UI 里做动画，思路和操作式完全不同：你不需要"让某物移动到某处"，只需要"改状态"，然后告诉框架"这次状态变化请带动画"。ArkUI 的动画有三板斧：属性动画（animateTo）、转场动画（transition）、手势（gesture）。先看最常用的 animateTo：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 展开收起动画</span><span class="dots">···</span>
:::

```
build() {
  Column() {
    Text('订单详情')
      .onClick(() =&gt; {
        this.getUIContext().animateTo(
          { duration: 250, curve: Curve.EaseInOut },
          () =&gt; { this.expanded = !this.expanded }
        )
      })
    if (this.expanded) {
      Text('这里是一大段展开后才显示的内容……')
        .transition(TransitionEffect.OPACITY)
    }
  }
}
```
:::

逻辑拆开看：onClick 里改状态（expanded 取反），改状态的动作包在 animateTo 的闭包里，闭包内发生的一切状态变化，框架都会用你给的时长和曲线插值过渡。下面那个 if 里新出现的 Text，配了 .transition()，出现和消失时就不再是生硬地蹦出来，而是淡入淡出。<strong>animateTo 管属性怎么变，transition 管组件出现和离场</strong>——这一句是本节的钥匙。

##### 属性动画的另一种写法：.animation() 修饰符

animateTo 是"包住状态变化"，.animation() 则是贴在组件上："这个组件的属性变化都按我的参数来"。它有个出了名的坑：<strong>.animation() 只对写在它前面的属性生效</strong>。你先写 .animation() 再写 .width()，宽度变化就不带动画，把 .animation() 挪到所有想动画的属性后面即可。这个顺序问题坑过无数人，界面"就是不动"时先查它。

##### 手势：把"摸"变成事件

常见手势都有现成类：TapGesture（点）、LongPressGesture（长按）、PanGesture（拖）、SwipeGesture（快滑）、PinchGesture（双指缩放）。用 .gesture() 挂到任意组件上，多个手势可用 GestureGroup 组合并声明互斥还是并行。来一个"拖动卡片"的例子：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 拖动手势</span><span class="dots">···</span>
:::

```
Image($r('app.media.card'))
  .translate({ x: this.offsetX, y: this.offsetY })
  .gesture(
    PanGesture()
      .onActionUpdate((e: GestureEvent) =&gt; {
        this.offsetX = e.offsetX
        this.offsetY = e.offsetY
      })
      .onActionEnd(() =&gt; {
        // 松手后决定吸附回弹还是留在原地
      })
  )
```
:::

模式很固定：<strong>手势回调里只改状态（offsetX/offsetY），build 里用状态驱动 translate</strong>。别在手势回调里直接操纵组件，那是声明式的反面。双击点赞这种"轻交互"，TapGesture 的 count 参数设成 2 就行。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2" aria-hidden="true"></i>小贴士

{class="mt-1"}
动画克制比炫技重要。入场动画一两百毫秒、退场更快一点，是最不容易让用户烦的区间；系统自带的页面切换动画别去覆盖它。判断标准很简单：动画结束后用户的下一步操作有没有被拖慢？被拖慢了，就砍时长。
:::

#### 七、自定义组件与复用：别让一个 build() 写到三百行

新人写界面的通病：整个页面塞进一个 build()。三百行起步，改一处全局抖。拆分的信号很明确<strong>同一段结构出现第二次，或者 build() 长到你滚动才能看完，就该拆了</strong>。拆出来的每个 @Component 就是第 72 章讲过的结构体：@Prop 收数据，回调属性往外发事件，父组件负责串。这个"数据往下、事件往上"的单向流，是组件复用的根基：一个 SettingItem 组件，Wi-Fi 页能用，蓝牙页也能用，因为它不关心数据是什么，只负责展示和上报。

##### @Builder：比组件更轻的复用

不是所有重复都值得拆成组件。组件有自己的生命周期和状态管理，有创建成本；如果只是"一段 UI 结构想复用"，@Builder 更轻，它就是个 UI 生成函数，没有生命周期，没有独立状态：

::: div .code-block
:::inline div .code-head
<span>ARKTS · @Builder 复用</span><span class="dots">···</span>
:::

```
@Builder
function Tag(text: string) {
  Text(text)
    .fontSize(12)
    .padding({ left: 6, right: 6 })
    .backgroundColor('#eef')
    .borderRadius(4)
}

Row() {
  Tag('新品')
  Tag('包邮')
  Text('无线降噪耳机').fontSize(16)
}
```
:::

@Builder 有一个必坑的细节：<strong>参数按值传递时，数据变了 UI 不刷新</strong>。想让 Builder 里的内容跟随数据更新，传参要传对象字面量形式（框架对字面量走引用传递路径）。踩到"Builder 里的数字永远不变"，八成是这个原因。

##### 样式复用：@Styles 和 @Extend

第三个复用层次是样式。@Styles 定义一组通用属性（尺寸、边距、圆角这类哪儿都能用的），@Extend 针对特定组件扩展专属属性。比如卡片圆角和内边距全 App 统一，就定义一个 @Styles；"标题文字"的字号加粗样式到处用，就 @Extend(Text)。三者分工记一句话：<strong>@Component 复用"结构 + 行为"，@Builder 复用"结构"，@Styles/@Extend 复用"样式"</strong>。层级越轻越好，能用 @Builder 解决的别上组件，能用 @Styles 解决的别上 Builder。

##### 进阶：列表项的 @Reusable

长列表还有一层进阶优化：给列表项组件标 @Reusable，配合复用池，滑动时框架把滚出屏幕的组件实例回收改造，而不是销毁重建。条目结构复杂、滑动频繁的场景收益明显。这是优化手段不是常规写法——列表先正常写，Profiler 确认瓶颈在创建上，再上 @Reusable。

#### 八、深色模式与多设备适配：一套代码，多种长相

界面写完只是及格线。深色模式下刺眼、平板上被拉成一整条横幅，都不算完工。好消息是这两件事 ArkUI 都有系统性解法，核心思路是同一个：<strong>别把"长相"写死在代码里，让系统按环境自动挑</strong>。

##### 深色模式：资源限定词目录

还记得本章第三节讲的 $r 资源引用吗？它就是深色模式的钥匙。资源目录支持"限定词"：resources/base 是默认值，你再加一个 resources/dark 目录，放同名资源：系统在深色模式下自动改用 dark 目录里的那份，你的代码一行都不用改：

::: div .code-block
:::inline div .code-head
<span>JSON · resources/base/element/color.json</span><span class="dots">···</span>
:::

```
{
  "color": [
    { "name": "page_bg", "value": "#FFFFFF" },
    { "name": "text_main", "value": "#1A1A1A" }
  ]
}
```
:::

::: div .code-block
:::inline div .code-head
<span>JSON · resources/dark/element/color.json</span><span class="dots">···</span>
:::

```
{
  "color": [
    { "name": "page_bg", "value": "#121212" },
    { "name": "text_main", "value": "#E6E6E6" }
  ]
}
```
:::

代码里写 <code class="inline">.backgroundColor($r('app.color.page_bg'))</code>，用户在系统设置里切换深色模式，页面自动跟着变。反过来说，凡是你在代码里直接写 '#FFFFFF' 的地方，深色模式切换时它都纹丝不动，这就是"深色模式切过去一半黑一半白"的最常见原因。排查方法：全文搜十六进制色值，逐个换成资源引用。图片同理：图标、插画放 dark 目录一份深色版本，同名替换。语言目录（zh-CN、en_US）也是同一套机制。你在本章第三节已经见过了。

##### 多设备：断点不是"重写一遍"

折叠屏展开、平板横屏、自由多窗，屏幕宽度一变，"手机版布局"就露馅了。ArkUI 的解法是断点（breakpoint）：官方默认给了三档，小屏（手机竖屏）、中屏（折叠屏展开、小窗）、大屏（平板），具体区间以当前文档为准。你要做的是在布局里声明"每档下各自怎么排"：

::: div .code-block
:::inline div .code-head
<span>ARKTS · GridRow 栅格适配</span><span class="dots">···</span>
:::

```
GridRow({
  breakpoints: { sm: 0, md: 480, lg: 720 }  // 区间以官方文档为准
}) {
  GridCol({ span: { sm: 12, md: 6, lg: 4 } }) {
    CardOne()
  }
  GridCol({ span: { sm: 12, md: 6, lg: 4 } }) {
    CardTwo()
  }
}
```
:::

意思翻译成人话：手机上一行一个（12 列占满）。平板上两列，大屏三列，同一份代码，三种排法。除了栅格，还有更细的媒体查询（mediaquery）能监听宽度变化做任意调整，以及监听窗口尺寸变化事件动态切换布局。日常开发的经验法则：<strong>列表和卡片类内容用栅格自动流式排，导航类（底部 Tab、侧边栏）用 if 按断点手动切</strong>。另外别忘了单位：ArkUI 里尺寸用 vp（随屏幕密度自动换算的虚拟像素），字号用 fp（还会跟随用户调大的系统字号）——用了 vp/fp，同一套代码在不同密度屏幕上物理大小才一致，别用 px。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hand-pointer mr-2"></i>来动手

{class="mt-1"}
把你之前写的任意一页的硬编码颜色全部抽到 color.json（base + dark 各一份），然后在模拟器或真机的设置里切换深色模式，来回切几次，检查有没有"钉在原地"的颜色。这一步做完，你的第一个"适配过关"的页面就诞生了。
:::

#### 九、性能优化：先定位，再动手

性能优化的第一原则是：<strong>没有测量就没有优化</strong>。凭感觉"我觉得这里慢"去改代码，十次有九次改错了地方。DevEco Studio 的 Profiler 能看到帧率、卡顿点、函数耗时和内存曲线：先跑一遍真实场景（滑动列表、切页面、连续点击），看时间花在哪，再对症下药。下面是最常见的四种病和药方：

<strong>病一：列表滑动掉帧。</strong>九成是 ForEach 建了全量条目，换 LazyForEach；再查键值是不是用了下标（导致滚动时反复重建）；图片是不是塞了原图（几千像素的图解码成大位图占内存，加载也慢）——列表里的缩略图应该用裁剪过尺寸的资源，或让图片组件按显示尺寸加载。结构复杂的列表项再考虑 @Reusable 复用。

<strong>病二：改一个小数据，半页界面都在刷。</strong>这是状态"粒度"太粗：把一个大对象整个标成 @State，改其中一个字段，框架把整个对象标脏，所有引用它的组件都重建。药方是把状态拆细——只被一个小组件用的状态，下沉到那个组件里去；嵌套对象需要精细观察的，用 V2 的 @ObservedV2 + @Trace（或 V1 的 @Observed + @ObjectLink）只追踪真正要观察的属性。

<strong>病三：页面打开慢半拍。</strong>检查 build() 里有没有重活：复杂的数据加工、排序、格式化都别放在 build 里现算——build 的职责是"根据状态渲染"，计算放事件回调里、放数据层里，算好存状态。另外控制嵌套深度，容器一层层套下去，每层都要测量布局，五六层以上的深嵌套几乎总能被压平。

<strong>病四：切页面掉帧或内存涨。</strong>if 和 visibility 的取舍要知道：if 条件为假时组件销毁，回来时重建（省内存，回切慢）；visibility 设 Hidden 时组件保留但不可见（回切快，占内存）。高频回切的页面倾向保留，很少回去的大页面倾向销毁。图片页、视频页这类内存大户，离开时该释放就释放。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2" aria-hidden="true"></i>小贴士

{class="mt-1"}
Profiler 里看"掉帧的那一刻在执行什么函数"，比看平均值有用得多。平均值好看不代表不卡，卡顿是瞬时的，用户滑一下手的那半秒里掉了帧，就是掉了。定位到那个时间点，看它调用了谁。
:::

#### 十、实战：把一张天气详情页设计稿翻译成 ArkUI

前面全是零件，这一节装整机。场景：设计师递来一张"天气详情页"设计稿，从上到下依次是：城市名和更新时间、大大的当前温度、天气描述加图标、一排小时预报（可横滑）、未来七天的列表、底部湿度和风速的小卡片。我们把它一步步翻译成 ArkUI，这个流程适用于任何设计稿。

##### 第一步：划结构，别急着写代码

拿到稿子先做减法：从上到下切成块，每块标注"用什么容器"。这一页切出来是：根容器肯定是 Column（内容从上往下排）；小时预报是横向滚动，Scroll 包 Row 或横向 List；七日预报是 List；底部小卡片是 Row 里放两个卡片，或 Grid。在纸上（或脑子里）画出这棵树，写代码只是把树翻译一遍。这一步五分钟，能省你后面一小时推倒重来。

##### 第二步：定数据模型

界面是数据的影子，先想清楚数据长什么样：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 数据模型</span><span class="dots">···</span>
:::

```
class HourWeather {
  time: string = ''
  temp: number = 0
  icon: Resource = $r('app.media.ic_sunny')
}

class WeatherData {
  city: string = ''
  currentTemp: number = 0
  desc: string = ''
  hourly: HourWeather[] = []
}
```
:::

##### 第三步：从上往下实现，先粗后细

先搭骨架再填肉：每个区块先用占位的 Text/Rect 把位置站住，跑预览器确认大结构对了，再逐块细化。骨架大致长这样：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 天气详情页骨架</span><span class="dots">···</span>
:::

```
@Entry
@Component
struct WeatherDetail {
  @State data: WeatherData = new WeatherData()

  build() {
    Column() {
      // 顶部：城市 + 更新时间
      Column() {
        Text(this.data.city).fontSize(24).fontWeight(FontWeight.Bold)
        Text('刚刚更新').fontSize(12).opacity(0.6)
      }

      // 当前温度 + 描述
      Column() {
        Text(`${this.data.currentTemp}°`).fontSize(72).fontWeight(FontWeight.Thin)
        Text(this.data.desc).fontSize(16)
      }

      // 小时预报：横向滚动
      Scroll() {
        Row({ space: 16 }) {
          ForEach(this.data.hourly, (h: HourWeather) =&gt; {
            Column({ space: 4 }) {
              Text(h.time).fontSize(12)
              Image(h.icon).width(24).height(24)
              Text(`${h.temp}°`).fontSize(14)
            }
          }, (h: HourWeather) =&gt; h.time)
        }.padding({ left: 16, right: 16 })
      }.scrollable(ScrollDirection.Horizontal)

      // 七日预报、底部卡片同理往下排
    }
    .width('100%').height('100%')
    .backgroundColor($r('app.color.page_bg'))
  }
}
```
:::

对照设计稿把"标注"翻译成属性：稿子上标的间距 16，就是 padding 或 space: 16；标的色号，进 color.json 走资源引用（顺手就把深色模式适配做了）；图标让设计师导出切图，放 media 目录。字号用 fp，尺寸用 vp，设计稿上标的数字一般能直接当 vp/fp 用。

##### 第四步：接数据、加动效、做适配

骨架稳了之后做三件事：把假数据换成真实请求（请求回来的 WeatherData 赋给 @State，界面自动刷新——声明式的红利时刻）；给温度数字加个入场动画（animateTo 一行）；切到深色模式和平板预览各看一眼。到这里，一张设计稿就完整落地了。回头看你会发现：<strong>布局三件套 + 状态 + 组件复用 + 资源引用，本章所有内容在这一个页面里都用上了</strong>。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-quote-left mr-2"></i>一句话记牢

{class="mt-1"}
先划结构、再定数据、后写代码；先站住骨架、再填肉、最后动效。设计稿翻译的顺序错了，返工是必然的。
:::

#### 十一、报错门诊：这些症状，你都遇得到

这一节是"症状 → 病因 → 药方"的清单，建议收藏。写 ArkUI 的头两周，你大概率会在其中三四个上摔跟头，提前知道病因，摔了不慌。

<strong>症状一：改了数据，界面纹丝不动。</strong>最经典的一个。你把数组里某个对象的属性改了（this.list[0].done = true），界面没反应。病因：V1 的 @State 能观察到数组本身的增删和整体替换，但<strong>观察不到数组内对象属性的变化</strong>。药方：给这个对象类标 @Observed、接收它的子组件里用 @ObjectLink；或者整个上 V2，@ObservedV2 + @Trace 标到属性上。如果你只是想偷懒，替换整个数组（重新赋值一个新数组）也能触发刷新，但那是权宜之计。

<strong>症状二：@Builder 里的内容永远不更新。</strong>前面第七节埋过这个雷：@Builder 默认按值收参数，传过去的是拷贝，原数据变了它不知道。药方：传对象字面量（让框架走引用路径），或者干脆升级成 @Component。

<strong>症状三：文字把布局撑爆。</strong>一段超长文案把 Row 挤得面目全非，或者把容器顶出屏幕。药方三件套：给文字 .maxLines() + textOverflow 截断；给同行其它元素 .layoutWeight(1) 让文字占剩余空间；实在不行用 constraintSize 给容器设上限。设计稿上"文案最多两行"这种信息，就是写代码的约束。

<strong>症状四：按钮点不到，或点到了别的。</strong>十有八九是 Stack 叠放：后写的组件在上面，一个透明的容器盖在按钮上，把点击"吃"了。排查法：把可疑的上层组件先注释掉，按钮复活了就是它。药方：调整叠放顺序，或给不需要交互的覆盖层设置 hitTestBehavior 让点击穿透。

<strong>症状五：编译报一大屏错，全是 any 和对象字面量。</strong>从网上抄的 TypeScript 代码编译不过，报 arkts-no-any-unknown 之类的规则错。病因：ArkTS 是 TypeScript 的严格子集，禁用 any、禁用无类型的对象字面量、部分动态写法不让用。药方：所有对象先声明 class 或 interface，变量给明确类型。这不是 ArkTS 跟你过不去——严格换来的是编译期抓错和运行时性能。

<strong>症状六：预览器里好看，真机上不对劲。</strong>预览器是"部分模拟"，媒体查询、窗口能力、键盘避让这些和设备强相关的行为，它给不了 100% 还原。真机和模拟器才是最终裁判——交工前必过真机。

<strong>症状七：键盘一弹，输入框被挡住。</strong>页面默认有键盘避让，但如果你自定义了窗口或用了 expandSafeArea，避让可能失效。药方：查键盘避让模式的配置，让输入框所在页面恢复默认避让，或手动监听键盘高度调整布局。

<strong>症状八：深色模式切过去，半黑半白。</strong>第八节讲过病因：硬编码的颜色不走资源，系统切它不动。全文搜 '# 和 rgb(，逐个换成 $r('app.color.xxx')。

<strong>症状九：ForEach 的条目点了没反应、或者全列表闪一下。</strong>键值生成函数的问题：键值不唯一会冲突，键值不稳定（用下标）会导致数据一变全列表重建。药方回到第五节：业务稳定 id 当键值。

#### 十二、弹窗与轻反馈：Toast、对话框、菜单、半模态

想象一个场景：你点了"删除"，界面毫无反应，你不知道是没点上、在处理中，还是已经删了。反馈缺失是新手界面的通病。反馈按"打断用户的程度"分三档：<strong>轻的用 Toast（一闪而过），中的用对话框和菜单（要用户表态），重的用半模态（弹出半个页面）</strong>。选档的直觉是：信息用户看一眼就行的，用轻的；需要用户做决定的，用中的；需要用户连续操作几步的，用重的。

##### Toast：一闪而过的通知

Toast 由系统的 promptAction 提供，一行代码弹一条短消息，几秒后自动消失，不打断操作：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 弹一条 Toast</span><span class="dots">···</span>
:::

```
import { promptAction } from '@kit.ArkUI'

Button('保存')
  .onClick(() =&gt; {
    this.save()
    promptAction.showToast({ message: '已保存' })
  })
```
:::

纠正两个常见用法错误。错误一：把 Toast 当重要信息的通知渠道，"网络错误，错误码 40122，请检查代理设置"用 Toast 弹出来，用户还没读完它就没了。重要信息走对话框或页面内的提示条。错误二：循环里连续弹 Toast，屏幕上叠了一串"已保存"，滑稽且无用，Toast 只弹一次，弹在最外层。

##### 对话框：让用户做一个决定

删除确认、退出未保存的提醒，这类"必须用户表态才能继续"的场景用 AlertDialog：系统样式现成，带标题、正文和两个按钮：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 删除确认对话框</span><span class="dots">···</span>
:::

```
Button('删除')
  .onClick(() =&gt; {
    AlertDialog.show({
      title: '删除确认',
      message: '删除后无法恢复，确定要删除这条记录吗？',
      primaryButton: {
        value: '取消',
        action: () =&gt; {}
      },
      secondaryButton: {
        value: '删除',
        action: () =&gt; { this.doDelete() }
      }
    })
  })
```
:::

写对话框有个原则要守住：<strong>危险操作必须二次确认，普通操作不要</strong>。每点一下"收藏"都弹"确定要收藏吗？"，这是在折磨用户。对话框的默认样式够用了，需要完全自定义布局时还有 @CustomDialog 装饰器（声明一个对话框组件，用 CustomDialogController 控制开关），初学阶段先不必碰。

##### 菜单与气泡：贴着组件弹

这两样和前两者不同：它们"长"在某个组件旁边。长按列表条目弹出"置顶 / 删除"的操作菜单，用 bindMenu；给一个图标加点击弹出的解释气泡，用 bindPopup：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 菜单与气泡</span><span class="dots">···</span>
:::

```
Image($r('app.media.ic_more'))
  .onClick(() =&gt; {})
  .bindMenu([
    { value: '置顶', action: () =&gt; { this.pin() } },
    { value: '删除', action: () =&gt; { this.remove() } }
  ])

Image($r('app.media.ic_help'))
  .bindPopup(this.showTip, { message: '开启后，离线也能收听已下载的内容' })
```
:::

bindPopup 的第一个参数是布尔状态：true 时气泡出现，false 时收起：又是状态驱动的老套路。菜单项的完整参数（图标、禁用态）以官方文档为准，这里只给最常用的骨架。

##### 半模态：从底部滑上来的半张页面

分享面板、筛选面板、"查看更多详情"，这类内容比对话框丰富、又没必要整页跳转的场景，用 bindSheet：组件绑一个半模态面板，从屏幕底部滑上来，用户下滑或点遮罩收起：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 半模态面板</span><span class="dots">···</span>
:::

```
@State isShow: boolean = false

Column() {
  Button('分享')
    .onClick(() =&gt; { this.isShow = true })
}
.bindSheet($$this.isShow, this.shareSheet(), {
  height: 320
})

@Builder
shareSheet() {
  Column() {
    Text('分享到…').fontSize(16)
    // 渠道图标行
  }
}
```
:::

注意那个 $$：它是"双向绑定"语法，用户把面板下滑收起时，框架自动把 isShow 写回 false，你的状态和界面永远一致。半模态的高度给多少取决于内容：让内容"刚好完整"，别撑满全屏，那就成普通页面了。

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>避坑提醒

{class="mt-1"}
对话框套对话框是设计事故：弹窗里点按钮又弹一个弹窗。用户会迷路。层级最多一层；真有复杂流程，关掉弹窗跳转到正经页面去做。
:::

#### 十三、页面骨架：Tabs 底部页签与主流 App 的导航结构

随便打开你手机里的主流 App：底部一排页签，点哪去哪；点列表里的条目，跳到详情页，返回键退回来。拆开看只有两种导航在配合：<strong>页签管平级切换（Tabs），页面路由管层级进出（Navigation）</strong>。Navigation 在本章第三节讲过了，这里补上另一半，Tabs。

::: div .code-block
:::inline div .code-head
<span>ARKTS · 底部页签骨架</span><span class="dots">···</span>
:::

```
@Entry
@Component
struct MainPage {
  @Builder
  tabBuilder(title: string, icon: Resource) {
    Column({ space: 2 }) {
      Image(icon).width(24).height(24)
      Text(title).fontSize(10)
    }
  }

  build() {
    Tabs({ barPosition: BarPosition.End }) {
      TabContent() {
        HomePage()
      }.tabBar(this.tabBuilder('首页', $r('app.media.ic_home')))

      TabContent() {
        DiscoverPage()
      }.tabBar(this.tabBuilder('发现', $r('app.media.ic_discover')))

      TabContent() {
        ProfilePage()
      }.tabBar(this.tabBuilder('我的', $r('app.media.ic_me')))
    }
    .scrollable(false)
    .onChange((i: number) =&gt; { this.currentTab = i })
  }
}
```
:::

拆几个关键点。<strong>barPosition: BarPosition.End 把页签栏放到底部</strong>——不写这个参数，页签栏在顶部，那是新闻类 App 的分类页签形态（横向一排文字页签）。tabBar 参数既可以收一个字符串（纯文字页签），也可以收一个 @Builder（图标加文字，主流样式）。onChange 里记录当前页签，用于恢复状态或埋点。

scrollable(false) 值得单独说：Tabs 默认支持"内容区左右滑切换页签"。底部页签的 App 通常要关掉它，内容区里往往还有自己的横滑组件（轮播、横滑列表），两层手势叠在一起，用户滑一下不知道切的是谁。原则是<strong>一层屏幕一层横滑手势</strong>：页签切换靠点，内容切换靠滑。

性能上有个好消息：TabContent 默认是懒加载的，首次切到某页签时才真正构建它的内容。所以"首页很轻、其他页签较重"的 App 启动依然快：首屏只构建默认页签。但如果你在 MainPage 的 aboutToAppear 里就替所有页签预热数据。那这层懒加载就白省了，别画蛇添足。

把骨架拼完整：应用入口页是 Tabs（底部页签），每个 TabContent 里是一个 Navigation 或直接放页面组件，Navigation 内部再进栈出栈跳详情页。三层结构<strong>页签层、路由层、内容层</strong>——就是绝大多数 App 的导航全貌。手机系统自带的"最近任务"里看到的一屏一屏，本质上就是这三个层叠的产物。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2" aria-hidden="true"></i>小贴士

{class="mt-1"}
底部页签的数量以三到五个为宜。两个显得空，超过五个每个图标太小还难点中。要是功能真的多，把"低频的大杂烩"收进"我的"或用半模态面板承载，别全摊在页签栏上。
:::

#### 十四、表单页套路：输入、校验、提交三步闭环

注册、登录、意见反馈、地址填写，表单页占了一个 App 里"最容易被用户骂"的页面的相当比例。它们套路完全一致，学会一次到处复用：<strong>状态收口、按时机校验、提交态管理</strong>。拿一个"意见反馈页"走一遍全流程：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 反馈表单</span><span class="dots">···</span>
:::

```
@Entry
@Component
struct FeedbackPage {
  @State title: string = ''
  @State content: string = ''
  @State titleError: string = ''
  @State submitting: boolean = false

  validateTitle(): boolean {
    if (this.title.trim().length === 0) {
      this.titleError = '标题不能为空'
      return false
    }
    this.titleError = ''
    return true
  }

  submit() {
    if (!this.validateTitle()) { return }
    this.submitting = true
    this.doSubmit()   // 完成后把 submitting 置回 false
  }

  build() {
    Column({ space: 12 }) {
      TextInput({ placeholder: '一句话描述问题' })
        .onChange((v: string) =&gt; { this.title = v })
        .onBlur(() =&gt; { this.validateTitle() })

      if (this.titleError !== '') {
        Text(this.titleError).fontSize(12).fontColor(Color.Red)
      }

      TextArea({ placeholder: '详细说明（选填）' })
        .height(120)
        .onChange((v: string) =&gt; { this.content = v })

      Button(this.submitting ? '提交中…' : '提交')
        .enabled(!this.submitting)
        .onClick(() =&gt; { this.submit() })
    }
    .padding(16)
  }
}
```
:::

三个设计决策解释一下。第一，<strong>校验时机：单字段失焦时校验，整体提交时再校验全部</strong>。用户刚点进输入框还没打字就飘红"不能为空"，是全世界表单的通病：onBlur（失焦）触发校验，用户碰过再说错没错。第二，<strong>错误提示贴在字段正下方</strong>，而不是收集到顶部一坨红字，用户要看三遍才知道哪行错了。第三，<strong>提交态三件套</strong>：按钮文字变"提交中…"、enabled(false) 禁点、请求回来恢复。少任何一个，用户双击就是两条重复数据。

校验的写法也有讲究：校验函数只做判断和写错误信息，不做提交；提交函数先跑全部校验，有一个不过就中止。别把校验塞进 onChange 里每次按键都跑一遍：输入过程中全程飘红，用户体验极差，也浪费算力。

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>避坑提醒

{class="mt-1"}
键盘遮挡是表单页的第二大投诉（第一大是校验时机）。底部按钮紧贴屏幕底的布局，键盘一弹就被盖住。测试表单页时务必在真机上把每个输入框都点一遍，确认输入焦点始终可见；被挡了就查键盘避让配置（本章第十一节症状七）。
:::

#### 十五、读改别人的 UI 代码：三步拆解法

错误示范先演一遍：你从网上下了个官方示例工程，从 main 页第一行读到最后一行，读到第三个嵌套容器时已经不知道自己在哪层了，合上电脑。这是错误读法。UI 代码不是小说，不能顺读，要<strong>先建骨架地图，再下钻细节</strong>。三步：

<strong>第一步：找根，画树。</strong>搜 @Entry（或路由表注册的组件），从最外层 build() 的根容器开始，只看容器不看属性——Column 里套了什么、Row 里套了什么，缩进就是层级。在纸上画出这棵树，五分钟，整页结构尽收眼底。

<strong>第二步：圈装饰器，标状态。</strong>把文件里所有 @State、@Prop、@Link、@Builder、@Watch 圈出来，给每个状态标一句"谁用"。状态的归属决定了刷新的波及范围——页面卡不卡、改一处会不会全身抖，看这张图就知道。

<strong>第三步：找数据入口。</strong>数组是写死的假数据还是请求来的？搜 $r 和 import，看数据从哪进来（mock 常量、网络层、AppStorage）。到这里你就把代码切成了两半：界面树和数据流，分别理解，互不干扰。

之后是"改"的阶段，从风险最小的改起：<strong>先改资源，不改结构</strong>——换色值、换文案、调间距，跑起来看效果。这类改动不碰逻辑，零风险，还能逼你理解 $r 的资源链路。结构级的改动（拆组件、换布局容器）留到你把状态归属图画清楚之后。

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>避坑提醒

{class="mt-1"}
改别人的代码前先确认装饰器代际，V1 体系（@State/@Prop/@Link）的文件里别引入 @Local/@Param 这种 V2 装饰器，同代混用会出各种诡异的"不刷新"。先看清这个文件整体用的是哪一代，沿用同代写法。
:::

#### 十六、一周练手清单：七天写出界面手感

界面能力是写出来的，不是看出来的。这章知识点密，看完感觉都懂、上手全不会，是正常现象，解药就一个：动手。下面是为你排好的一周练手清单，每天投入半小时到一小时，做完这七个小页面，本章内容就从"知道"变成"会了"：

1. <strong>第一天：静态页。</strong>复刻系统设置页的三行（Wi-Fi、蓝牙、显示），每行"图标 + 文字 + 开关或箭头"。只用 Row、Text、Image，练布局手感。
2. <strong>第二天：状态。</strong>做一个开关卡片：Toggle 切换时，卡片背景色跟着变。练 @State 与声明式刷新，体会"改状态就是改界面"。
3. <strong>第三天：列表。</strong>造五十条假数据，用 LazyForEach 渲染，加上下拉刷新。练键值生成与 Refresh 组件。
4. <strong>第四天：动画。</strong>做一个可展开收起的"订单卡片"：animateTo 控制高度变化，transition 控制内容显隐。练第四节那把钥匙。
5. <strong>第五天：弹窗。</strong>列表条目加长按菜单（bindMenu）与删除确认（AlertDialog），删除成功弹 Toast。练反馈三档的选档。
6. <strong>第六天：适配。</strong>把前几天的硬编码颜色全部抽进 color.json，补 dark 目录，深色模式来回切。练资源限定词。
7. <strong>第七天：整合。</strong>把第十节的天气详情页做完，小时预报接上假数据轮换。练"结构、数据、动效"三层分离。

两条执行建议。一是<strong>卡住超过二十分钟就看官方示例，别硬耗</strong>——看懂了合上再自己写一遍，比硬憋效率高。二是每天做完把代码放进版本管理（下一章会讲 DevEco 的 Git 集成），七天之后你有一个能拿出手的练手仓库，比什么"我学过 ArkUI"都有说服力。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hand-pointer mr-2"></i>来动手

{class="mt-1"}
今天就做第一天的练习：新建一个工程，只写一个页面、三行设置项，跑在预览器里。写完对照本章第一节的"布局三件套"，数一数你用了几个容器、几次链式调用，这就是你 ArkUI 手感的第一块积木。
:::

#### 十七、无障碍、大字号与国际化：别让一部分用户用不了

先说两个真实场景。场景一：你给爸远程装了个 App。他早把系统字号调到最大——打开你的界面。文字互相叠、按钮被截断，他不会调，直接卸载。场景二：视障用户开着读屏（屏幕阅读器）用你的 App，图标按钮没配文字，读屏读到的是"按钮，按钮"，他什么都干不了。界面质量的上限靠性能和动效，<strong>下限靠无障碍和适配</strong>——下限塌了，上限再高也没人用得上。

##### 系统字号缩放：fp 不是摆设

本章第八节讲过：字号单位 fp 会跟随用户调大的系统字号。但跟随只是起点，布局得给大字留活路。三条对策：一是<strong>容器高度别写死</strong>——文字变大了容器不跟着变，文字就溢出或截断，让容器包裹内容自适应；二是同行元素用 layoutWeight 分配剩余空间，而不是都给固定宽度；三是给文字区域留换行余量，maxLines 该两行就两行，别指望一行永远放得下。测法也简单：系统设置里把显示字号调到最大，打开你的页面逐屏看——这是最便宜的无障碍测试。

::: div .code-block
:::inline div .code-head
<span>ARKTS · 大字号友好的行</span><span class="dots">···</span>
:::

```
Row() {
  Image($r('app.media.ic_wifi')).width(24).height(24)
  Text('WLAN').fontSize(16).layoutWeight(1).margin({ left: 12 })
  Toggle({ type: ToggleType.Switch, isOn: this.isOn })
    .onChange((on: boolean) =&gt; { this.isOn = on })
}
.width('100%')   // 行高不写死：让内容撑开
```
:::

图标固定 24，文字用 layoutWeight(1) 占据中间弹性区，开关贴右。系统字号调到多大，文字都在自己的弹性区里换行，行高自动撑开，这行代码在默认字号和最大字号下都成立。

##### 读屏：给看不见的用户留一条路

读屏软件按顺序朗读屏幕上的元素，靠的是每个组件的"语义信息"。系统组件（Button、Toggle、Checkbox）自带语义，朗读没问题；<strong>容易出事的是"图片当按钮"和纯装饰图</strong>：一个只有图标的按钮，读屏读不出它是干什么的。给这类组件补无障碍描述，让读屏能念出"删除订单"而不是"图片"：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 给图标按钮补语义</span><span class="dots">···</span>
:::

```
Image($r('app.media.ic_delete'))
  .width(24).height(24)
  .onClick(() =&gt; { this.remove() })
  .accessibilityText('删除这条记录')
  .accessibilityDescription('点击后删除当前记录，不可恢复')
```
:::

除此之外还有三条不用写代码的规矩。一是<strong>色彩对比度</strong>：浅灰字配白背景，年轻人眯着眼看，视障和老年用户直接放弃：正文对比度按无障碍标准的建议档位来，至少做到"不用眯眼"。二是<strong>别只靠颜色传信息</strong>：表单错误只标红，色弱用户分不清红和灰：加个感叹号图标或"必填"文字，颜色只是辅助。三是<strong>点击目标别太小</strong>：按钮视觉上可以精致，可点击区域别低于系统推荐的尺寸（具体数值以官方无障碍规范为准），不然手抖的用户点三次中一次。

##### 国际化：资源目录只是第一步

本章第三节讲了 zh-CN / en_US 资源目录，那是国际化的地基，但只做这一步的界面出了国就露馅。三个进阶点。第一，<strong>带变量的文案用占位符，别拼字符串</strong>：把"已下载 3 个文件"整句写进资源文件，变量用占位符表示，代码里只传数字——因为另一种语言的语序可能完全不同，拼出来的句子读不通。第二，<strong>给文本膨胀留空间</strong>：同一句按钮文案，英文德文可能比中文长一截，按钮宽度、标签长度都要按"最长语言"设计，文字自适应、容器别写死。第三，<strong>镜像语言</strong>：阿拉伯语、希伯来语从右往左读，界面布局要支持镜像，导航箭头方向、进度条方向、返回手势方向都要跟着翻。这三条在你只出中文版时不用管。但写代码时留好余地（不写死宽窄、文案走资源），将来国际化就是改资源文件而不是改代码。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hand-pointer mr-2"></i>来动手

{class="mt-1"}
两步体检你手头的项目：一，系统设置把字号调到最大，打开自己写的每一页截图存档；二，想象自己是视障用户，只靠听，你的图标按钮们会念出什么？两个体检都不过关的话，本章就是你的急救手册。
:::

#### 十八、界面验收清单：交给别人看之前的十道关

写完不等于写好。自己开发时一切正常，交给别人的第一分钟就翻车，数据没加载的白屏、被键盘挡住的按钮、平板上拉成一条线的列表。翻车点高度重复，所以可以清单化。下面十道关，每次交付前过一遍，每道都不难，难的是记得去测：

1. <strong>四态齐全。</strong>每个列表页都要有正常态、空态、加载态、错误态。空态别白屏：一张占位图加一句"还没有记录"加一个行动按钮，比空白体面得多。
2. <strong>断网与弱网测试。</strong>开飞行模式点一遍核心流程，加载失败要有提示和重试入口，不能转圈转到天荒地老。
3. <strong>深色模式来回切。</strong>切三次以上，专抓"钉在原地"的硬编码颜色（第十一节症状八）。
4. <strong>系统字号最大档。</strong>第十七节那套，逐屏截图检查有无溢出遮挡。
5. <strong>键盘遮挡。</strong>每个输入框点一遍，焦点始终可见，提交按钮不被盖死。
6. <strong>极端文案。</strong>把最长的标题、最短的用户名（单个字）、纯数字昵称都塞进去看一遍——布局的豆腐渣工程都暴露在极端样本下。
7. <strong>多宽度过一遍。</strong>手机竖屏、折叠屏展开、平板各看一眼，栅格布局有没有塌。
8. <strong>快速连点。</strong>提交按钮、支付按钮、跳转按钮各连点五下：重复提交、页面叠两层，都是这里暴露的（第十四节的提交态就是防它的）。
9. <strong>返回与手势。</strong>每一页都试系统返回手势和返回键，弹窗打开时返回要关弹窗而不是退页面。
10. <strong>Profiler 跑一遍滑动。</strong>核心列表滑三趟，看帧率曲线有没有明显掉坑，真机测，别信预览器。

这十道关里，出现频率最高的是第一道。新手页面十有八九只写了"数据正常时"的样子：接口挂了白屏、列表空了白屏。把三态（空、载、错）当成和主功能同级的需求，从一开始就写进排期，它们不是"回头再补"的装饰，是用户第一时间对你专业度的判断依据。

执行上推荐"最差设备"思维：拿你手头最旧最低配的真机、开最弱的网络、把系统设置调到最极端（最大字号、深色、无障碍全部开启），用这台"地狱难度"设备过一遍核心流程。它过了，好设备只会更顺；反过来不成立。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2" aria-hidden="true"></i>小贴士

{class="mt-1"}
把这十道关存成自己的检查清单文件，每次交付前照着勾。清单的价值不在复杂，在你永远不会在赶工的深夜里漏掉它，人靠不住的时候，靠清单。
:::

#### 十九、六个常见误区：很多人以为，其实不然

这一节把新手社区里出现频率最高的六种"想当然"集中清算。每条都按同一个格式来：流行的说法是什么、真相是什么、正确做法是什么。它们看起来各不相干。根源却是同一个，读完最后一段你就明白。

<strong>误区一：很多人以为"界面是一步步画出来的，画得越勤快越流畅"。</strong>其实声明式 UI 里，你只负责两件事：描述界面该长什么样，以及改状态。渲染是框架的事，而且框架比你更擅长——它知道哪些区域没变、哪些可以跳过。你要是抢着"手动操作界面"（绕过状态直接干预显示、另存一份界面数据自己维护），反而把框架的优化路径全堵死了，还会养出"界面和数据两张皮"的维护噩梦。正确姿势只有一句：永远只改状态，让界面自己长出来。

<strong>误区二：很多人以为"组件拆得越细越好，一个 Text 也该包成组件"。</strong>其实拆分是有成本的：组件实例要创建、状态要一层层传递、跳转要看一层。把一个孤零零的 Text 包成组件，除了让代码多一跳之外什么都没换来，深层嵌套的测量开销还添了新的。拆分的信号依旧是那两条：同一段结构出现了第二次，或者单个 build() 长到要滚动才能看完。没有信号就不拆，克制是美德。

<strong>误区三：很多人以为"状态装饰器长得差不多，随手选一个就行"。</strong>其实 @Prop 和 @Link 的差别是"单向拷贝"与"双向绑定"，选错的后果是界面和数据悄悄不同步——这种问题不崩溃、不报错，只是默默地不对，等用户反馈时已经攒了一堆。拿不准的时候先问自己一个问题：这个数据，子组件改了之后父组件需不需要知道？需要，用双向（@Link 或 V2 的组合方案）；不需要，单向足矣。

<strong>误区四：很多人以为"px、vp 差不多，随便用哪个都能显示"。</strong>其实 px 是物理像素，屏幕密度一高，你按 px 写的按钮就缩成指甲盖大小，用户只能用触控笔戳。vp 会按设备密度自动换算，fp 在 vp 的基础上再叠加用户的字号偏好。这就是为什么设计稿上的数字能直接当 vp/fp 用，而 px 永远不该出现在你的 ArkUI 代码里。发现代码里有 px，当成 bug 处理。

<strong>误区五：很多人以为"深色模式就是把背景色换成黑的"。</strong>实际要跟着变的东西比你想的多：文字对比度得重调（黑底上的浅灰字要提亮，不然看不清）、图片素材要换深色版（白底图标在黑屏上像个发光的补丁）、卡片和阴影的层级关系也要换思路（白底靠阴影分层，黑底上阴影几乎不可见，得靠表面色的明度差）。好消息是资源限定词目录这套机制已经替你把路铺好了，坏消息是只要有一处硬编码颜色，这套路就破功——所以第八节才反复强调全文搜色值。

<strong>误区六：很多人以为"性能优化是进阶技巧，等学完基础再说"。</strong>其实本章教的最基础的几个动作——列表用 LazyForEach、状态拆细下沉、控制嵌套深度、图片按显示尺寸加载——本身就是在做优化。从第一个列表页就照标准姿势写，成本是零；先随手写烂再回头重构，成本十倍，还得先治"不敢动"的心理。把标准写法当成唯一写法，优化就变成了默认值而不是选修课。

六个误区的共同根源只有一个：把命令式的心智模型带进了声明式的世界。命令式的直觉是"我去操作界面"，声明式的直觉是"我改数据、界面自己变"。哪天你发现自己在想"我怎么让界面变"而不是"我该让哪个数据变"，停一下，翻回本章开头那个剧本比喻重读一遍，九成的"诡异 bug"在这一步就想通了。

#### 二十、术语速查表：读官方文档前的对照卡

去翻官方文档时，你会接连撞上一串术语，文档默认你懂，可初学时恰恰是它们在挡路。这张表给每个术语一句"人话解释"，先立住概念再点进文档，阅读效率完全不同。细节表述以当前版本官方文档为准，这张表管"看懂"，不管"精确"：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">术语</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">一句话解释</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">声明式 UI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">写"每种状态下界面长什么样"，状态一变框架自动重渲染</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">状态</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">驱动界面变化的数据；改状态就是改界面的唯一正道</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">装饰器</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">标在变量或结构体上的记号（如 @State），声明它参与界面刷新</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State / @Prop / @Link</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">V1 三件套：组件自有 / 父传子单向拷贝 / 父子双向绑定</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Builder</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">复用一段 UI 结构的函数，比组件轻，注意按引用传参才刷新</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ForEach / LazyForEach</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全量循环渲染 / 按需懒加载渲染，长列表必须用后者</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">键值（keyGenerator）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">列表项的稳定身份证，键值乱则刷新乱、列表闪</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List / Grid / Scroll</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">纵向列表 / 网格 / 任意方向滚动的容器</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stack</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">叠放容器，后写的子组件在上层</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Navigation</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">页面路由容器，官方推荐新项目用它而非仅维护的 Router</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">$r('app.type.name')</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">资源引用语法，字符串、图片、颜色统一从这里取</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">资源限定词</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">base / dark / zh-CN 这类目录后缀，系统按当前环境自动挑资源</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">vp / fp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">随屏幕密度换算的长度单位 / 在此基础上还跟随系统字号缩放</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">断点（sm / md / lg）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">按窗口宽度分档的响应式方案，具体区间以文档为准</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">objectFit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">图片与容器的适配模式：Cover 裁切填满，Contain 完整显示</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">半模态（bindSheet）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">从屏幕底部滑出的半个页面，装分享面板、筛选面板</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Toast（promptAction）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一闪而过的轻提示，只承载"看一眼就够"的信息</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Profiler</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DevEco Studio 里的性能面板，帧率、耗时、内存都在这看</td></tr>
</tbody>
</table>
```
:::

这张表怎么用：读文档卡住时先回来查表，确认"这个词在说哪件事"，再带着准确的问题回去读——多数"文档读不懂"，不是理解力问题，是术语错位：你以为它在说 A，它其实在说 B。术语对齐了，文档立刻好读。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2" aria-hidden="true"></i>小贴士

{class="mt-1"}
把这张表存到随手能翻到的地方——浏览器书签、打印贴墙都行。它的价值不在内容深，在"永远够得着"：术语的第一次恐慌，多数发生在深夜查文档的第三屏。
:::

#### 二十一、界面之外：这一章之后是什么

写到这一节，你已经能从设计稿造出完整界面了。但一个能装到手机上、能发布、能被别人用的 App，光有界面还不够，界面是"皮肤和房间"，应用本体是"承重结构和水电"。第三节的导航里我们埋过一句话：第 74 章讲 UIAbility 时，会把"入口"和"页面路由"接起来。现在可以把这句话展开说清楚：你即将跨出 UI 层。

界面层之外还差几样东西。一是<strong>入口</strong>：用户点了桌面图标，系统怎么找到你的第一页、把路由树立起来：这是 UIAbility（应用组件）的职责。二是<strong>生命周期</strong>：用户切到微信再切回来，你的页面还停在他刚才看的那一条，界面状态在应用被切后台、被回收、被恢复时怎么保住，第 74 章会给你整套机制。三是<strong>数据与权限</strong>：界面显示的数据从哪来、写文件要不要授权，那是数据章的事。你会发现本章学的一切在那边都还在用：UIAbility 不是"另一个世界"，是给你的界面树套上"何时生、何时活、何时存"的骨架。

所以在翻下一章之前，做一件小事：<strong>把本章十六节的七天练手仓库留着，别删</strong>。第 74 章的每个新概念，都可以直接在这个仓库上做实验，给它加一个真正的应用入口、在切后台时保存列表滚到哪了、把假数据层换成真实请求。学新概念最好的方式，从来不是对着教程空想。从来是往自己已经熟悉、已经能跑的工程里加东西：加得动，说明真懂了；加不动，卡点就是下一节要学的内容。

离开前留一张自测清单，五道题都能秒答，这一章就算真正过关；卡住的题，回到对应小节重读一遍：

- Column、Row、Stack 各自管什么场景？Stack 里谁在上层？
- @State、@Prop、@Link 的差别用一句话怎么说？选错了症状是什么？
- 五百条数据的列表为什么必须用 LazyForEach？键值为什么不能用下标？
- 深色模式的落地机制是什么？为什么"半黑半白"的锅永远是硬编码颜色的？
- 用一句话给完全不懂的人解释"声明式 UI"和"改状态就是改界面"。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2" aria-hidden="true"></i>小贴士

{class="mt-1"}
界面能力的保鲜方式只有一个：持续写。哪怕每周只花二十分钟把练手页面翻新一次——换个布局、加个动效，手感就不会掉。工具会更新、API 会演进，但"结构、状态、资源"这三层的划分方式，足够你用到这本书再版好几轮。
:::

#### 二十二、FAQ：十个真实的问题

<strong>问：我会 Jetpack Compose / SwiftUI，切 ArkUI 最快的路径是什么？</strong>答：你已经赢了七成——状态驱动、声明式、链式修饰这些心智模型完全同构。直接看官方的"从 Compose/SwiftUI 迁移"对照文档，把装饰器系统（@State 家族）和路由（Navigation）补齐，剩下的就是查 API。

<strong>问：几十个组件几十个属性，要不要背？</strong>答：不要。高频的就第四节那张表，其余的靠 DevEco 的代码补全和官方文档现查。背 API 是最不值得的投资，API 会变，心智模型不会。

<strong>问：ArkTS 和 TypeScript 到底什么关系？为什么我抄的 TS 代码编译不过？</strong>答：ArkTS 是 TS 的严格子集——大部分语法一样，但禁用了 any、无类型对象字面量这些动态特性。报错不是 bug，是规则。按报错码查官方的"TypeScript 到 ArkTS 适配规则"清单，一条条改。

<strong>问：新项目用 V1 还是 V2 装饰器？</strong>答：看你 SDK 版本的官方推荐。大方向上官方在推 V2（观察更精细、性能更好），但网上教程和存量代码大量是 V1——所以第二节那张对照表才让你留着。接老项目沿用原体系，起新项目看当时文档的推荐。

<strong>问：预览器、模拟器、真机，我该信哪个？</strong>答：预览器管"布局长得对不对"（快）；模拟器管"流程跑不跑得通"；真机管"手感、性能、深色模式、真网络"。越往后越权威，交工前真机必须过。

<strong>问：状态到底该放页面 @State 还是 AppStorage？</strong>答：默认放页面。只有"多个页面都要读写"的（登录态、主题设置）才升到应用级。什么都塞 AppStorage，等于把所有房间的东西堆进客厅——找得到，但乱。

<strong>问：一套 ArkUI 代码能同时跑手机、平板、手表吗？</strong>答：方向上是——这就是"一次开发多端部署"的卖点，第八节的断点和资源限定词就是为此服务的。但"能跑"不等于"不用适配"：手表上你得重新设计交互，不是把手机界面缩小。

<strong>问：界面写完了，怎么知道它算不算"写得好"？</strong>答：三个检查器：Profiler 看滑动帧率（性能）、深色模式切两轮（适配）、把系统字号调到最大再看一遍（无障碍）。三个都过，这个界面就比大多数 demo 强。

<strong>问：想找现成的例子抄，去哪找？</strong>答：官方示例仓库和 DevEco 内置的模板工程是首选——能编译能跑，跟着改比从零写快。网上博客代码当参考思路，直接抄要注意 SDK 版本差异（本章开头说的 V1/V2 并存就是最大的坑源）。

<strong>问：设计师不给标注，只给一张图，怎么办？</strong>答：别硬猜。要不到标注就先按常规值写（内边距十几、圆角十几、字号一档一档来），跑起来截图和设计稿并排对比，差得明显的再调。像素级的较真留给有验收要求的项目，大多数场景"接近 + 统一"比"精确 + 混乱"好。

十个问题的答案里反复出现同一个走向：不背结论，抓模型。状态驱动、资源先行、断点适配、真机验收，概念模型立住了，API 是随查随用的外挂；模型没立住，背下来的 API 也用不对地方。所以别急着囤教程，先把本章前几节的心智模型在练手仓库里用熟，用到"不假思索"为止；哪天你写界面时脱口说出"这里该拆个 Builder"，就说明模型已经长在脑子里了。

最后送你一张"入场券"式的自我评估：打开你的练手工程，随手指着任意一段代码问三个问题，它属于结构、状态、资源哪一层？这次刷新由谁驱动？切到深色模式它会怎么变？三个都能脱口而出，你就不是"看过 ArkUI"，而是"会写 ArkUI"了。答不上来的那个问题，回对应小节再走一遍，走完当天就别再改了，留下明天验证。下一章，我们给这套界面装上应用的骨架。

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 布局三件套：（Column/Row/Stack + justifyContent/alignItems），Flexbox 同构
- 列表 List + ForEach，网格 Grid；layoutWeight 相当于 flex:1
- 状态三层：@State 自有、@Prop 单向、@Link 双向：选错装饰器是第一坑
- Navigation/Router 管页面跳转；$r() 统一资源引用
- 多语言资源目录与安卓 strings.xml 思路一致
- V1（@State/@Prop/@Link）与 V2（@Local/@Param）并存：别混用；对照表留着读懂老代码
:::
