---
id: di-qi-shi-jiu-zhang
num: 79
nav: 第七十九章：进阶之路
toc: default
kind: chapter
after_part: hongmeng-kai-fa-pian
---

### 第七十九章：进阶之路——服务卡片、元服务与分布式

{class="chapter-intro mb-4"}
三个实战项目做完，鸿蒙开发的"硬技能"已经齐了。这一章讲三样"软实力"：服务卡片（应用在桌面上的迷你版）、元服务（免安装的轻应用）、分布式（跨设备的流转与协同）。它们是鸿蒙区别于安卓、iOS 的"独门武器"，也是面试和实战里的高频话题。

三样东西的定位一句话说清：服务卡片是"应用的橱窗"——不打开应用就能看到关键信息、做轻量操作；元服务是"应用的轻量形态"——免安装、即用即走；分布式是"跨设备的能力"——手机上开始的事，平板上接着做。三者都建立在第 74 章的 Stage 模型之上，学习成本不高，但"什么时候该用"的判断比"怎么用"更重要——这一章两样都讲。

#### 一、服务卡片：桌面上的"应用速览"

服务卡片（Form Kit）是嵌在桌面上的应用切片：天气卡片显示当前温度、待办卡片显示今日待办数、音乐卡片提供播放控制。用户长按桌面就能添加卡片——它是应用在桌面上的"免费广告位"，也是用户打开应用的"零步入口"。

卡片的技术结构一句话：它也是 @Entry 组件（复用你已学的 ArkUI），但数据由 FormExtensionAbility 经 formBindingData 提供——卡片有自己的生命周期与刷新机制（定时刷新、订阅刷新），与主应用通过事件通信。开发一张卡片的步骤：创建 FormExtensionAbility → 声明卡片配置（form_config.json：名称、尺寸、刷新策略）→ 写卡片 UI（ArkTS，和你已会的语法一样）→ 在 formBindingData 里准备数据。

卡片设计的两条心得先说在前面：别把卡片当成缩小版首页——它受刷新频率、尺寸与交互限制，先想清楚「用户瞥一眼最想知道什么」，再把这一个信息做好；也别依赖应用还活在内存里——卡片的数据刷新走独立通道，设计时要假设主应用没在运行。

#### 二、元服务：免安装的"即用即走"

元服务（原名原子化服务）是鸿蒙的轻应用形态：不用安装、碰一碰/扫一扫/搜一搜直达、用完即走。典型场景：共享单车的扫码开锁、餐厅的点餐入口、机场的航班卡片。它与完整应用共享同一套开发技术（ArkTS + ArkUI），区别在"形态与分发"：元服务体积更小（有上限约束）、无需安装、可以独立上架。

开发元服务时，项目模板选"Atomic Service"，包名规则、签名方式与普通应用略有差异。一个务实的选择策略：如果你的服务场景足够"轻"（一两个核心功能、即用即走），元服务是低门槛的入口；如果功能复杂、需要用户长期投入数据，完整应用更合适。两者也可以并存——元服务当入口，引导用户安装完整应用（注意遵守平台的引导规范）。

#### 三、分布式：鸿蒙的"独门武器"

分布式是鸿蒙与安卓、iOS最大的差异点：同一应用的能力可以跨设备流转——手机上编辑文档，平板上接着改；手机看视频，智慧屏上继续放。底层靠分布式软总线（设备自动发现与组网），上层给开发者的是一套相对统一的 API。

开发分布式应用前，先回答三个问题：这个功能跨设备有价值吗（手机编辑→平板大屏编辑，有价值；手机计算→手表计算，没价值）；数据怎么跨设备（流转的是任务上下文还是原始数据）；目标设备是否都装了你的应用（跨设备协作通常要求两端都有应用）。分布式是高级特性，建议先把单设备体验做扎实，再考虑流转——半成品的多端体验比没有更糟。

#### 四、一张表分清三个概念

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">概念</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">一句话</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">什么时候用</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">开发成本</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">服务卡片</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">应用的桌面切片</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">有"瞥一眼就想知道"的信息</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">低（复用 ArkUI 技能）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">元服务</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">免安装的轻应用</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">场景轻、即用即走</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">中（独立上架流程）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分布式</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跨设备流转与协同</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">任务天然跨设备</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">高（多端适配与调试）</td></tr>
</tbody>
</table>
```
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：给待办清单加一张卡片

{class="mt-1"}
1\. 用 DevEco 的模板创建 FormExtensionAbility；2. 卡片显示"今日待办数与最近一条"；3. 配置每 30 分钟定时刷新；4. 预览器查看效果后真机添加到桌面。
:::

#### 五、服务卡片开发实战：从模板到桌面的完整一张卡片

概念上一节说完了，这一节动手。目标定得很具体：给第 76 章的待办清单配一张卡片——显示"今日待办数"和最近一条待办的标题，点卡片主体进应用，卡片上放一个"打卡"按钮做轻交互。整张卡片做完大约一个晚上的活，代码其实不多，工作量的大头在配置文件和刷新策略上——这也正是卡片开发最容易翻车的两处，后面各用一节展开。

##### 第一步：用模板起步，别从空白文件写起

DevEco Studio 里不需要你手写脚手架。在 entry 模块上右键，菜单里找 Service Widget（或叫"服务卡片"，不同版本菜单位置略有差异，找不到就翻官方指引），选一个最简单的基础模板，填个名字。生成的东西有三样，逐一确认：

1. 卡片页面：widget 目录下多出一个 .ets 文件，卡片长什么样就在这里写
2. 卡片扩展：一个继承 FormExtensionAbility 的类文件，负责给卡片供数据
3. 卡片配置：resources 的 profile 目录里，form_config.json 多出一个表单条目

三样东西的关系一句话说清：配置文件声明"有一张卡片"，扩展类回答"数据是什么"，页面文件决定"数据怎么摆"。接着把工程 Run 到真机，桌面长按应用图标，在弹出的服务卡片列表里找到你的卡片添加——此刻它显示的还是模板里的假数据，接下来我们一样一样换成真的。

##### FormExtensionAbility：卡片的"数据管家"

打开模板生成的扩展类，你会发现它长得像 UIAbility，干的事却完全不同——它没有界面，不渲染任何东西，只负责回答"此刻卡片该显示什么数据"。核心方法就四个，直接看骨架：

::: div .code-block
:::inline div .code-head
<span>ARKTS · form/TodoFormAbility.ets（示意）</span><span class="dots">···</span>
:::

```
import { FormExtensionAbility, formBindingData, formProvider, Want } from '@kit.FormKit'

export default class TodoFormAbility extends FormExtensionAbility {
  // 用户把卡片添加到桌面那一刻，系统回调这里，你交出第一份数据
  onAddForm(want: Want): formBindingData.FormBindingData {
    let formId = want.parameters?.['ohos.extra.param.key.form_identity'] as string
    TodoStore.addFormId(formId)              // formId 务必持久化，后面刷新全靠它
    return formBindingData.createFormBindingData({
      'todoCount': TodoStore.todayCount().toString(),
      'latest': TodoStore.latestTitle()
    })
  }

  // 到了配置文件约定的刷新时刻，系统回调这里
  onUpdateForm(formId: string): void {
    formProvider.updateForm(formId, formBindingData.createFormBindingData({
      'todoCount': TodoStore.todayCount().toString(),
      'latest': TodoStore.latestTitle()
    }))
  }

  // 卡片被用户移除，记得清掉对应的 formId
  onRemoveForm(formId: string): void {
    TodoStore.removeFormId(formId)
  }

  // 卡片上 action 为 message 的按钮，事件最终落到这里
  onFormEvent(formId: string, want: Want): void {
    // 收到指令、改数据、推回卡片，后文演示
  }
}
```
:::

几个容易误解的点掰开说。onAddForm 不是"应用启动"——它只在用户添加卡片那一刻触发一次，你交出的数据就是卡片的第一屏。formId 是这张卡片的身份证：一台手机可以同时摆着三张同款卡片，各有各的 formId，刷新必须一张一张点名，所以添加的瞬间就要把它存进第 76 章用过的本地偏好里；onRemoveForm 和它配对，用户删了卡片你不删记录，后面每次 updateForm 都是对着空气开火。还有一条纪律：这个扩展多半运行在独立于界面的后台进程里，系统需要时才拉起——回调里别做耗时的大活，拼好数据就交卷。

##### 先在预览器里过一遍，再上真机

DevEco 的预览器支持卡片预览（以你装的版本功能为准）：打开卡片页面文件，预览窗里直接看布局，改一版看一版，不用每次都装进真机再长按添加。要提醒的是，预览器只管"长得对"，刷新、message 事件、formId 这些运行时的事必须真机验证——预览器里点按钮没反应不是 bug，是它根本没接那条链路。真机验证按这个顺序：先添加卡片看首屏数据，再等一次定时刷新，最后把卡片上所有按钮点一遍。三步都过，卡片才算真的活着。

##### form_config.json：逐字段过一遍

配置文件是卡片的"户口本"，系统添加卡片、调度刷新全按它来。下面是本卡的示意版本，数值仅供演示，字段与取值以你版本的官方文档为准：

::: div .code-block
:::inline div .code-head
<span>JSON · resources/base/profile/form_config.json（示意）</span><span class="dots">···</span>
:::

```
{
  "forms": [
    {
      "name": "TodoCard",
      "displayName": "$string:todo_card_name",
      "description": "$string:todo_card_desc",
      "src": "./ets/widget/pages/TodoCard.ets",
      "type": "ArkTS",
      "window": { "designWidth": 720, "autoDesignWidth": true },
      "colorMode": "auto",
      "isDefault": true,
      "defaultDimension": "2*2",
      "supportDimensions": ["2*2", "2*4"],
      "updateEnabled": true,
      "scheduledUpdateTime": "07:30",
      "periodicRefresh": 30
    }
  ]
}
```
:::

- <strong>name</strong>：卡片的内部标识，代码和配置都引用它，改名记得全局搜一遍。
- <strong>displayName / description</strong>：添加界面里用户看到的名字和说明。都走 $string 资源引用，别硬编码中文——多语言和文案统一修改全靠它。
- <strong>src</strong>：卡片页面的路径，指向刚才 widget 目录里的那个文件。
- <strong>type</strong>：卡片的技术形态，新项目统一写 ArkTS。网上老资料里还有另一种 JS 卡片写法，别照搬。
- <strong>window</strong>：设计基准宽相关参数，照模板默认走，除非你清楚自己在改什么。
- <strong>colorMode</strong>：写 auto，跟随系统深浅色。写死浅色的话，深色模式用户的桌面上会躺着一张刺眼的白卡片。
- <strong>isDefault / defaultDimension / supportDimensions</strong>：默认添加的尺寸和支持的档位。声明了哪个档位就要为哪个档位真做适配——四档全声明、只测一档，是上架被拒的经典理由。
- <strong>updateEnabled / scheduledUpdateTime / periodicRefresh</strong>：刷新总开关、每天定点时刻、周期分钟数，下一节的主角。
- 另有 formConfigAbility、metadata 等字段，做到卡片设置页、数据代理时才用得上，查文档即可。

##### 卡片页面：你已会的 ArkUI，加一个新装倒

卡片页面的语法和你写了一路的 ArkUI 没有差别，唯一的新东西是数据怎么进来——不通过组件传参，而是通过 LocalStorage 绑定：

::: div .code-block
:::inline div .code-head
<span>ARKTS · widget/pages/TodoCard.ets（示意）</span><span class="dots">···</span>
:::

```
let storage = new LocalStorage()

@Entry(storage)
@Component
struct TodoCard {
  // 与 FormExtensionAbility 塞进来的数据按 key 对应，单向绑定
  @LocalStorageProp('todoCount') todoCount: string = '--'
  @LocalStorageProp('latest') latest: string = '暂无待办'

  build() {
    Column({ space: 6 }) {
      Text('今日待办').fontSize(12).fontColor($r('app.color.sub_text'))
      Text(this.todoCount).fontSize(30).fontWeight(FontWeight.Bold)
      Text(this.latest).fontSize(13).maxLines(1)
        .textOverflow({ overflow: TextOverflow.Ellipsis })
    }
    .justifyContent(FlexAlign.Center)
    .padding(12)
    .onClick(() =&gt; {
      postCardAction(this, { 'action': 'router', 'abilityName': 'EntryAbility' })
    })
  }
}
```
:::

注意 @LocalStorageProp 是单向的：扩展推什么，卡片显示什么，卡片自己不维护状态、也不主动去拿数据。把它当"数据快照的镜子"，而不是"缩小版的页面"，布局和逻辑都会简单一半。字体颜色走资源引用而不是写死色值，和 colorMode 的道理相同：深浅两套都要活。

##### 卡片上的按钮：三种路由动作

onClick 里真正的关键在 postCardAction——卡片环境的跳转受限，一切点击行为都要通过它来声明。action 支持三种：

- <strong>router</strong>：拉起应用里的某个 UIAbility，用户看得见界面。点卡片主体进应用，用它。
- <strong>message</strong>：给 FormExtensionAbility 发一条消息，onFormEvent 收到。卡片上的轻操作——打卡、翻页、切换视图，用它。
- <strong>call</strong>：后台拉起指定 UIAbility 干活，对配置有额外要求，细节以官方文档为准，确认需要后台执行再上它。

把"打卡"按钮的闭环走通，你会看清 message 的完整链路：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 卡片上的打卡按钮（示意）</span><span class="dots">···</span>
:::

```
Button('打卡一条')
  .onClick(() =&gt; {
    postCardAction(this, {
      'action': 'message',
      'params': { 'cmd': 'checkLatest' }
    })
  })
```
:::

用户点下按钮，事件落到 onFormEvent，你在扩展里调用第 76 章写好的数据层方法执行打卡（不是在扩展里重写一遍），改完数据调 formProvider.updateForm 推回卡片，LocalStorageProp 同名 key 一变，界面自动换。三个角色各干各的：卡片发指令、扩展改数据、绑定管刷新——谁也不越界。

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>避坑提醒

{class="mt-1"}
卡片是"展示与入口"层，不是业务逻辑层。打卡的真正执行放在主应用的数据层或服务里，FormExtensionAbility 只做三件事：收指令、改数据、推回卡片。把业务逻辑塞进卡片扩展，意味着主应用和卡片两边各有一份"打卡"实现——改规则那天，两张脸对不上，用户报 bug 时只会说一句"卡片上打钩了，应用里还是没打"。
:::

#### 六、卡片的刷新策略与数据更新：定时、按需与电量账

卡片上线当晚，你多半会收到第一条"差评式"反馈：数据不动。刷新是卡片最容易被误解的部分——难的不是技术，是预期没对齐：用户以为卡片像秒表一样跳动，系统却把卡片当省电项目重点关照。这一节把刷新的几种方式摆上桌，再算一笔电量账。

##### 四种刷新方式，一张表分清

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">方式</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">谁来触发</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">适合的数据</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要注意</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定点刷新</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系统，每天固定时刻</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">晨报类：天气概览、当日日程</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一天一次，时刻选用户真会看的点</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">周期刷新</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系统，按周期调度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">计数类：待办数、步数汇总</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">有最小周期与每日上限，实际时刻由系统统一调度</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">按需刷新</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">你的应用主动推</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">刚发生的状态变化：勾掉一条待办</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">应用得运行着才能推，配合用户时机</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">订阅刷新</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系统场景触发</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系统级场景为主</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">三方应用通常用不上，方案别押注，开放范围以官方文档为准</td></tr>
</tbody>
</table>
```
:::

表格先立住一个认知：除了按需刷新，其他方式的决定权都在系统手里。你提交的只是"请求"，调度权、频次上限、触发精度全归系统——这是设计预期，不是 bug。带着这个预期去做方案，你就不会在"为什么它没准时刷"上耗一整晚。

##### 定点与周期：把刷新交给系统的日程表

scheduledUpdateTime 是"每天这个时刻刷一次"，适合晨报类数据：天气概览、当日日程，用户早上看第一眼时数据已经换好。periodicRefresh 是"按周期刷"，单位是分钟，适合计数类：待办数、步数这种半小时变一次也不奇怪的数据。示意配置里的数值别照抄——系统对最小周期和每日次数都有限制，且随版本调整，以官方文档为准。

还有一件必须提前知道的事：系统会合并调度。到点的卡片不止你一张，系统把它们凑成一波一起刷，既省电又少打扰——所以"设了 30 分钟"不等于"第 30 分钟准时跳"，前后有偏差是常态。周期选多少，别按"显得勤快"选，按数据的变化节奏倒推：待办数一天变三五次，半小时档绰绰有余；股价分钟级波动，卡片这个形态本来就不适合承载，让用户点进应用看。

##### 按需刷新：最可靠的路是自己推

数据什么时候变，你最清楚——变化的那一刻顺手把卡片也推了，是最及时、最不浪费的刷新：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 主应用里顺手刷新卡片（示意）</span><span class="dots">···</span>
:::

```
import { formProvider, formBindingData } from '@kit.FormKit'

async function refreshTodoCard(formId: string, count: string, latest: string) {
  try {
    await formProvider.updateForm(formId,
      formBindingData.createFormBindingData({ 'todoCount': count, 'latest': latest }))
  } catch (e) {
    // 卡片可能刚被移除，失败别当事故，记条日志就够
  }
}
```
:::

这段代码放哪？用户在应用里勾掉一条待办、保存退出前，顺手调一次。formId 从第 76 章的本地偏好里取——第五节强调过，onAddForm 时就要存。一台设备上多张同款卡片就是多个 formId，存成一个列表，推的时候一张一张都推到，别只刷"最近添加的那张"。

##### 一个完整的方案：天气卡片的刷新设计

拿第 77 章的天气助手算一笔账，你会看到三种方式怎么配合。天气数据的节奏是小时级更新，用户看卡片的时刻集中在早间出门前后。方案就出来了：定点刷新配一个早晨的时刻，让用户睁眼看到的就是当天概览；周期刷新选一个宽档位做兜底，防止白天数据长期不动；真正的"新鲜"靠按需——用户早上打开过应用，退出前顺手把最新数据推到卡片。三种方式各司其职，没有一种需要"高频率"。反例也顺手给你一个：把周期设成最短档，让系统一天替你刷几十次，可数据源本身一小时才更新——多刷的那几十次，全是白烧的电。

##### 刷不动、刷不准：给用户一个时间戳

定时刷新到点时，你的应用多半不在前台，扩展被系统拉起来干活，网络慢、接口超时都可能发生。三条纪律：回调里给网络请求设超时；失败就保留旧数据，别把卡片刷成空白或报错页；数据类卡片带一行"更新于 08:30"。前两条是工程，最后一条是设计——它把"数据可能旧"从事故变成预期。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2" aria-hidden="true"></i>小贴士

{class="mt-1"}
"更新于 XX:XX"这行小字是卡片设计里性价比最高的一笔：用户看到时间戳，就不会把旧数据当故障报修；你自己排查"卡片到底刷没刷"，也全靠它肉眼可验。
:::

##### 电量账：三条纪律收尾

卡片刷的是别人的手机，一天很多次，每一次都是真实的耗电。三条纪律：按数据节奏选档位，不按焦虑选档位；能用按需推送的场景优先按需，定时只做兜底；刷新回调里只做拼数据和一次请求，批量同步、大文件、密集计算统统别放——它们该在用户打开应用时发生，而不是在系统替你拉起的那一刻。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-quote-left mr-2"></i>一句话记牢

{class="mt-1"}
卡片的刷新决定权在系统手里，你的工作是把请求提得聪明：变化时自己推，定时刻踩着数据节奏，其余时间让手机睡觉。
:::

#### 七、元服务开发实战：体积约束下的功能取舍

拿到元服务模板，新手的第一个念头几乎都一样："把我那个应用砍一半塞进去。"做出来就会发现哪里都不对：页面挤成一团，跳转绕来绕去，体积还超限。元服务不是阉割版应用，是另一种形态——目标不是"用得久"，是"快进快出地完成一次具体任务"。想清楚这一点，取舍就不再纠结。

##### 用 Atomic Service 模板起步

1. New Project，模板列表里选 Atomic Service（不同版本里它的位置会挪，搜关键字最快）。
2. 生成的工程结构与普通应用几乎一致，ArkTS、ArkUI 的写法零差别——你已经会的技术，原样用。
3. 差异集中在配置：应用级配置文件里有元服务专属节点，包名体系与签名、上架流程走元服务这一路。照模板默认来，细节以官方文档为准。
4. Run 到真机验证"免安装"：启动即进，没有安装进度条——这就是元服务体验的底线。

::: div .code-block
:::inline div .code-head
<span>JSON5 · AppScope/app.json5（节选示意，字段随版本演进，以模板生成为准）</span><span class="dots">···</span>
:::

```
{
  "app": {
    "bundleName": "com.example.todo.quick",
    "label": "$string:quick_name",
    "icon": "$media:quick_icon",
    "atomicService": { /* 元服务专属配置，模板会填好 */ }
  }
}
```
:::

##### 体积账：先瘦身，再拆包，最后才砍功能

元服务有明确的体积上限（数字随版本调整过，以你当前版本的官方文档为准）。超限时按这个顺序动手，很多项目卡在第一步就解决了：

1. <strong>资源瘦身</strong>：图片压一遍、能用矢量就不位图、用不到的多语言与图标删干净——超限的大头常常是资源，不是代码。
2. <strong>按需加载</strong>：官方提供多包与按需加载机制（以文档为准），把非首屏能力拆出去，首屏只装"完成任务必需"的那部分。
3. <strong>砍功能</strong>：最后一步，标准只有一条——"删掉它，核心任务还完成得了吗？"

##### 砍什么留什么：一把尺，两张清单

尺子就是那句话：这个页面删掉后，核心任务还完成得了吗？完成得了就删。套到两个真实场景上：

- <strong>共享单车</strong>：核心任务是"开锁骑车付款"。留——扫码、开锁、计费说明，三屏到头；砍——骑行历史、会员中心、活动页，那是"长住用户"的领地，元服务用户是过路人。
- <strong>快速记一条待办</strong>：核心任务是"想法落地，别忘"。留——一个输入框加保存；砍——列表页、标签体系、提醒设置，全都在完整应用里做。

还有一条容易被忽略：合并小功能。相关的小操作并成一屏，少一次跳转就少一分流失——元服务用户的耐心以秒计。设置项可以留给完整应用，元服务里连"关于我们"都可以没有。

##### 场景案例：停车场的元服务长什么样

设想一个出场缴费的元服务：用户在停车场出口，扫码或碰一碰拉起，第一屏直接是车牌与金额，一个按钮"确认支付"，完成即走。它需要什么？车牌识别结果、金额、支付能力，三样。它不需要什么？停车记录列表、发票管理、会员积分——那些是完整应用的事。这个案例里最值得学的是"无菜单"设计：用户站在出口闸机前，身后排着队，此时任何"浏览""发现"类的界面都是设计事故。把这类极限场景想清楚，元服务的界面取舍就有了准绳——每次犹豫要不要加东西，就把自己放回那个排队的瞬间。

##### 与完整应用的衔接：两副面孔，一套业务

元服务和完整应用不必二选一，它们可以是同一套业务的两副面孔：元服务管"进来快"，完整应用管"用得深"。衔接的常见做法是在自然节点引导——任务完成页、能力受限提示处，提供到完整应用详情页的入口，由系统拉起应用市场，具体接口与展示规范以官方文档为准。两条合规纪律记牢：引导放在任务节点上，别进门就弹；文案说收益（"历史记录和云同步在完整应用里"），别只喊"去下载完整版"。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：把"快速记一条"做成元服务

{class="mt-1"}
用 Atomic Service 模板新建工程，做一个单页：文本输入（有余力加语音），保存后直接退出并 toast 确认。不要列表页、不要设置页。做完对比它和第 76 章完整应用的启动速度，你会对"轻"字第一次有体感。
:::

#### 八、元服务的发现与分发：碰一碰、扫一扫、搜一搜

应用市场的逻辑是"人找服务"：用户先有需求，再搜名字、比评分、下载。元服务的想象力在"服务找人"——你正站在餐厅桌前，点餐入口就该自己出现；你站在共享单车旁，开锁入口就该触手可及。三个入口按出现频率排：扫一扫、搜一搜、碰一碰。

##### 扫一扫：最常用，也最容易翻车在纸面上

场景：周五晚七点，商场餐厅门口排队，桌上的立牌印着二维码。用户用系统相机或负一屏扫码，识别后元服务直接拉起，第一屏就是菜单——全程没有"下载"两个字。开发者侧的清单三件事：

- 码的内容必须符合平台规范（通常走官方短链或服务码，格式以官方文档为准），自己随手编个网址，扫了也拉不起来。
- 码印出来要真扫得动：尺寸太小、材质反光、深浅对比不足，是线下部署的三大杀手，上线前拿几台不同手机到现场实测。
- 首屏要接得住场景：桌上扫码，第一屏就是菜单和"开始点餐"，不是品牌故事页——用户的耐心在扫码那一刻最薄。

##### 搜一搜：免费流量，靠上架信息认真填

负一屏、全局搜索里输入"代驾""洗车"，冒出来的可能就是你的元服务。这条路不收钱，但要你把服务名、关键词、类目、描述填得像用户嘴里说的话。做法很土但有效：找十个真实用户问"你需要洗车服务时会对手机说什么"，逐字对照你的上架信息——"洗车上门"这种朴素组合，比"某某科技智慧出行服务平台"有效得多。名称别堆热词，堆词过不了审。

##### 碰一碰：NFC 标签，用部署成本换确定性

手机碰一下贴在设备上的 NFC 标签，对应元服务直接拉起——酒店客房控制、共享设备启动是典型场景。开发者要做两件事：按规范把标签内容写对（写卡规范以官方文档为准），再和商家把贴纸贴到用户的手会伸过去的位置。支持碰一碰的机型范围视设备而定，所以它通常是增强入口，不能当唯一入口——碰一碰这条路断了，其他入口必须还在。

##### 入口之外：系统还会替你"摆摊"

除了三个主动入口，系统还会按场景把合适的元服务"摆"到用户眼前：负一屏的服务建议、特定场景下的推荐卡片等。呈现机制由系统决定，开发者能做的是把服务的类目、场景标签、上架信息填准确，让系统"认识"你。这类被动曝光的具体规则随版本演进，以官方文档为准。心态上把它当意外之喜，别当核心流量来源——把宝押在系统推荐上的服务，和把宝押在平台算法上的内容创作者，命运差不多：规则一改，流量归零。自己布的码、自己填准的搜索词，才是你可控的部分。

##### 一张表收拢：三个入口的开发者清单

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">入口</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">用户动作</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">你要准备</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">最容易翻车的点</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">扫一扫</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">相机或负一屏扫码</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">合规的码 + 接得住场景的首屏</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">码印出来扫不动</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">搜一搜</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">负一屏或全局搜索输入需求</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">认真填服务名、关键词、类目</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">名称堆词被审核打回</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">碰一碰</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">手机碰 NFC 标签</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">按规范写卡 + 线下部署到位</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">当唯一入口，不支持的机型直接断路</td></tr>
</tbody>
</table>
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>避坑提醒

{class="mt-1"}
三个入口共同的前提是服务已上架、状态正常。线下部署的码和标签要有回收机制：服务下线、改名、换入口后，桌上那张二维码指向一个打不开的服务，是商家最恼火的售后工单——也是你的品牌污点。
:::

#### 九、分布式实战：把待办清单流转到平板

分布式的 demo 一晚上能跑通，但跑稳要把三件事想周全：环境条件、上下文恢复、能力探测。这一节以"手机上写了一半的待办，到平板上接着编辑"为目标，把思路走完整——代码给骨架，接口细节以官方文档为准。

##### 环境准备：两台真机，一个账号

1. 准备两台支持流转的真机（机型与系统版本的支持范围视设备而定，查官方说明）；模拟器能做界面预览，流转链路请用真机。
2. 两台设备登录同一个华为账号，WLAN、蓝牙打开，保持可发现状态。
3. DevEco 里跑 hdc list targets，两台设备都该在列；同一工程分别装到两台（同包名、同签名）。
4. 先别写代码：在系统设置里把跨设备协同类的开关逐台确认（入口名称随版本有差异），再用系统自带的接续功能试一次——系统级接续通了，你的应用才有舞台。

##### 多设备预览与调试：左手手机，右手平板

写一多界面时，把预览器同时开手机与平板两个窗口（以你装的 DevEco 版本功能为准），每改一版两边对照——断点布局的错，十有八九出在只看了一边。真机调试用 hdc -t 设备号 install 指定设备装包，日志用 hilog 按包名过滤。一个便宜但救命的习惯：日志文本开头带上设备标识（"手机："、"平板："），两台设备的日志贴在一起排查时，你会感谢这一行。

##### 流转的实现思路：应用接续

先纠正一个直觉：流转不是"把数据拷贝到另一台设备"，是"把任务上下文序列化后交给对端恢复"。鸿蒙给的标准通道是应用接续——在 UIAbility 里实现 onContinue，把"恢复这个任务需要什么"装进 want，对端拉起时读出来还原现场：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 发起端：把上下文装进 want（示意）</span><span class="dots">···</span>
:::

```
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit'

export default class EntryAbility extends UIAbility {
  // 流转发起时系统回调：你负责把"恢复任务所需"装进 wantParam
  onContinue(wantParam: Record&lt;string, Object&gt;): AbilityConstant.OnContinueResult {
    wantParam['noteId'] = TodoStore.currentEditingId()
    wantParam['draftText'] = TodoStore.currentDraft()
    return AbilityConstant.OnContinueResult.AGREE
  }
}
```
:::

::: div .code-block
:::inline div .code-head
<span>ARKTS · 接收端：从 want 里恢复现场（示意）</span><span class="dots">···</span>
:::

```
// 对端拉起时，onCreate / onNewWant 的 want 里带着发起端塞的字段
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  let noteId = want.parameters?.['noteId']
  if (noteId) {
    TodoStore.resumeEditing(noteId as string)   // 恢复到同一条待办的编辑现场
  }
}
```
:::

三个工程细节决定接续的成色。其一，接续成立的前提是同账号、同应用，两端版本别差太远，给 want 里的字段带个版本号是成本极低的保险。其二，恢复要做存在性校验：那条待办在对端可能已被删掉，查不到就落到默认页，别让用户面对一个空白界面。其三，AGREE 还是 REJECT 要诚实——数据没准备好、状态不完整时就拒，让系统走它自己的失败提示，好过打开一个"看起来正常其实缺半截"的界面。

##### 一次完整的接续调试，长什么样

给你一份真实的排查流水，感受一下节奏。现象：手机上编辑到一半，平板接续过来，内容是十分钟前的旧稿。第一步查发起端日志——onContinue 确实带了最新草稿，问题不在发送。第二步查接收端——onCreate 里读到了 noteId，draftText 却是空的。对时间线发现，平板上的应用是昨天装的旧版本，旧版本根本不认识 draftText 字段。升级两端到同一版本，问题消失。这一单的收尾动作值得抄走：给 want 里的每个字段做缺省兜底（没有 draftText 就只恢复到那条待办的列表位置，而不是白屏），再在接续入口处提示"两端版本不一致可能影响接续体验"。分布式问题的排查，大头花在对时间线上，改代码反而是收尾。

##### 协同的实现思路：一份实时共享的数据

协同和接续不同：接续是"过去时"——这边停下，那边接着；协同是"进行时"——两边同时操作同一份数据。实现路径两条：用系统的分布式数据对象，数据变更自动在组网设备间同步，省事；或自己走服务端中转，所有设备连同一份云数据，可控。小项目先试前者：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 分布式数据对象（示意，接口以官方文档为准）</span><span class="dots">···</span>
:::

```
import { distributedDataObject } from '@kit.ArkData'

// 组网与账号条件满足时，两端对同一对象，一边改字段，另一端收到回调
let obj = distributedDataObject.create(this.context, { title: '买菜', done: false })
obj.on('change', (newVal: Object) =&gt; {
  this.title = newVal.title as string
  this.done = newVal.done as boolean
})
```
:::

协同必须正面回答冲突：两人同时把同一条待办勾上，听谁的？简单项目用"最后写入者赢"，再把结果如实呈现——界面显示最新状态即可，别假装冲突不存在。要求高的场景才做字段级合并，那已经超出本节范围，官方最佳实践里有展开。

##### 什么值得流转：一张判断表

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">场景</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">建议形态</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">理由</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">文档、清单的"接着写"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">接续</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">任务一段一段做，大屏上继续体验更好</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">视频、音乐的"换个屏看"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">媒体接力</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系统有现成通道，应用做好适配即可</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">双人棋类、共填一张表</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">协同</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真正的"同时"，必须实时同步</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">计算器、单机小游戏</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不做</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跨设备没有增益，老老实实单设备</td></tr>
</tbody>
</table>
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>避坑提醒

{class="mt-1"}
分布式调试最贵的成本是"两端状态各说各话"。从第一天立规矩：所有状态变更打日志，带设备标识和时间戳；复现问题先对时间线，再改代码。没有这条纪律，你会把大量深夜花在"平板上明明改了，手机为什么没变"的玄学排查上。
:::

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-quote-left mr-2"></i>一句话记牢

{class="mt-1"}
接续传的不是数据，是任务；协同共享的不是文件，是此刻。
:::

#### 十、分布式的限制与降级：把"不支持"设计进产品

演示机上流转丝滑，发到用户手里，有人按钮点不动，有人压根找不到入口——多数时候不是 bug，是你没设计"不支持"的样子。分布式能力的可用性天然"看情况"：机型、系统版本、账号、网络全在变量里。这一节讲怎么探测、怎么降级。

##### 先搞清楚"看哪些情况"

- <strong>设备与系统版本</strong>：流转与协同的机型支持范围、能力开放程度，以官方文档与设备说明为准，别照抄某台演示机的表现。
- <strong>账号与组网</strong>：同账号登录、网络可达是基本前提，用户可能退了账号、关了 WLAN，或者压根不登录账号。
- <strong>应用自身</strong>：接续要求两端都装着你的应用且版本兼容，哪头缺了都不成立。
- <strong>API 能力</strong>：代码层面用 canIUse 检查系统能力是否可用，拿到 API 就直接调，是最常见的崩溃来源。

::: div .code-block
:::inline div .code-head
<span>ARKTS · 能力探测（示意，能力名以 API 参考为准）</span><span class="dots">···</span>
:::

```
if (canIUse('SystemCapability.DistributedDataManager.DataObject')) {
  this.showCollabEntry = true    // 能力可用，协同入口照常展示
} else {
  this.showCollabEntry = false   // 走降级，见下文三种姿势
}
```
:::

##### 三种降级姿势

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">姿势</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">做法</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">什么时候用</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">隐藏</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">入口整个不出现</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">功能对该用户完全无意义，出现只是噪音</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">置灰加说明</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">按钮可点，给出"为什么不行、怎么才行"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">条件大概率能满足：没登录、没开 WLAN，教一下就能解锁</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">替代路径</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">给出不依赖分布式的等价做法</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">条件短期满足不了，但需求真实存在</td></tr>
</tbody>
</table>
```
:::

选择逻辑一句话：条件可满足的用"置灰加说明"，不可满足但需求真实的给"替代路径"，纯增强功能直接隐藏。最常见的失误是第三种没做——协同走不通，但用户想要的结果（和爱人共一张清单）用共享云端清单也能到达，你没给这条路，用户就流失了。

##### 三个常见误区

- <strong>以为"是鸿蒙设备"就等于"支持流转"</strong>：系统版本、机型、账号、组网，层层条件叠着，官方文档里写得很清楚，别用一句话概括。
- <strong>以为降级就是"报错"</strong>：弹一个"当前设备不支持"的提示，等于告诉用户"你被淘汰了"——降级的正确形态是替代路径，不是挽歌。
- <strong>以为探测一次就完事</strong>：用户此刻没第二台设备，五分钟后可能就连上了；能力状态要可刷新，入口要能"复活"。

##### 降级设计的三个具体动作

1. <strong>入场就探测</strong>：页面加载时查一次能力，别等用户点了按钮才报错；探测结果可以缓存，但要监听变化——第二台设备上线后入口要能"活过来"，别逼用户重启应用。
2. <strong>文案提前写</strong>：置灰按钮下的说明不是事后补的，上线前就写好——"需要两台设备登录同一账号"，一句话，别让用户猜。
3. <strong>主流程零依赖</strong>：核心功能在单设备上必须完整可用。分布式是加分项，不是地基；地基建立在加分项上的应用，注定在大半用户那里站不住。

拿家里的真实场景检验一下：爸妈只有一台手机，你的待办清单在他们那里不该出现任何流转入口——界面没有任何残缺感，一切功能照常。做到这个程度，降级才算设计过，而不是漏做。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2" aria-hidden="true"></i>小贴士

{class="mt-1"}
把"不支持清单"写进需求文档：哪些条件走降级、降到什么界面、文案是什么。评审时，这份清单比 demo 里的丝滑流转更有说服力——它证明你想过那些没被演示到的用户。
:::

#### 十一、鸿蒙特有的交互规范：卡片、元服务与多端的官方要求

这三样东西的官方设计规范都挂在开发者官网，上架审核按它来。规范全文会持续更新，别把任何摘录（包括这一节）当圣经——这里给你的是"过一遍不容易被打回"的重点，以及每条背后的理由。理由懂了，规范怎么改你都能跟上。

##### 卡片规范：桌面是用户的，你只是租客

- <strong>声明的每个尺寸档位都要真适配</strong>：supportDimensions 里写了几档，就得为几档各出一版布局，不是把小尺寸拉伸交差。
- <strong>一张卡片一个主题</strong>：信息密度宁低勿高，用户在桌面瞥一眼，超过三个焦点就等于零个。
- <strong>别放重交互</strong>：长滚动列表、大图轮播、复杂动效属于应用内部；卡片是"瞥一眼加一下轻操作"的地方。
- <strong>点击行为可预期</strong>：点主体进应用，点按钮走轻操作，不设计"点了没反应"的死区域。
- <strong>深浅色都过一遍</strong>：colorMode 用 auto，颜色全部走资源——第 77 章深色模式那一套原样适用。

##### 元服务规范：即用即走的底线

- <strong>免登录优先</strong>：先让用户完成任务，登录放在真正必要的节点（下单、存历史），进门就堵注册墙是元服务的第一大流失原因。
- <strong>权限最小化</strong>：要什么权限、为什么，用说人话的 reason 写清楚；用不到的权限一个都别申请——审核和用户两边都会盯。
- <strong>退出即走</strong>：退出路径上不设障碍、不做挽留弹窗，元服务的口碑建立在"干脆"两个字上。
- <strong>引导完整应用要克制</strong>：位置、时机、频次都有平台规范，以官方文档为准，别把引导做成变相强制下载。

##### 多端适配：大屏不是"以后再说"

官方对多端体验有明确要求，自由窗口、断点自适应这些机制在前面章节出现过，具体审核口径以最新的审核指南为准。务实建议只有一条：把平板当第二台测试机，每做完一个页面就开平板预览看一眼。等整个应用写完再回头适配，返工的不是"改布局"，是把写死的尺寸、单列假设、横屏遗漏逐个挖出来——成本翻好几倍。

##### 来自审核现场的三条经验

- <strong>名称与截图先过自己关</strong>：名称堆词、截图和实际功能对不上，是第一轮最常被打回的两件事。
- <strong>卡片类素材用真机截图</strong>：预览器渲染和真机存在差异，审核对卡片尺寸与显示效果的核对很实。
- <strong>给审核往返留时间</strong>：卡片、元服务的审核比普通应用多几项专项核对，排期别把上线日期卡死。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2" aria-hidden="true"></i>小贴士

{class="mt-1"}
上架前把"设计指南"与"审核指南"的最新版各过一遍，重点读卡片、元服务、多端相关的小节。规范是活的，书和博客都会过期，官网不会。
:::

#### 十二、进阶学习资源：官方文档、Samples 与认证考试

这一章的三个主题，API 的更新节奏都比任何一本书快。书当地图，官网当路——下面是四个值得收藏的入口和各自的正确打开方式，外加读文档的几个习惯。

##### 四个入口，各自的用法

- <strong>官方文档站</strong>：分指南、API 参考、最佳实践三层。查一个 Kit，先读指南概述建立概念地图，再翻 API 参考看字段与方法，最佳实践留到动手后读——顺序反了，看了也白看。
- <strong>Samples 示例仓库</strong>：按 Kit 分类，找 Form Kit、元服务、分布式的官方示例，克隆下来先跑通，再往自己工程里搬。看别人怎么组织代码，比自己瞎摸索快得多。
- <strong>Codelabs 与教程</strong>：一两个小时的小实验，适合用来验证"我以为的理解"是不是真的理解。
- <strong>开发者社区与论坛</strong>：报错信息整段搜——你踩的坑，大概率有人几天前刚踩过，而且贴了完整堆栈。

##### 读文档的三个习惯

- <strong>版本选择器先对齐</strong>：文档支持多个 API 版本，选错了版本，字段名都对不上，还以为文档写错了。
- <strong>"约束与限制"逐行读</strong>：卡片刷新的上限、分布式的账号条件，都写在正文角落的这个栏目里——跳过它，代价通常出现在上线之后。
- <strong>搜报错别搜感觉</strong>：把异常类名或错误码贴进搜索框，比"卡片不刷新怎么办"精准十倍。

##### 官方之外的资源，怎么甄别

社区博客、视频教程数量庞大，质量与时效参差。两条甄别标准：一看发布时间与对应的 API 版本——接口演进快，两年前的教程可能整段过时；二看作者有没有给出处——关键结论能指回官方文档的，可信度高。遇到与官方文档冲突的讲法，一律以官方文档最新版为准，拿不准就去开发者社区发问，那里有官方人员和资深开发者在。

##### 认证考试：要不要考，怎么考

官方有面向鸿蒙应用开发者的认证体系，分基础、高级等层级（名称、大纲、费用以官网最新公告为准）。要不要考，看目的：求职需要背书、公司给报销、想用考试大纲倒逼系统复习——这三种情况值得；纯粹为学而考，不如把大纲当自查清单用。备考路径很实在：把官方大纲对着本书的章节过一遍，每个考点回到对应项目里上真机摸一遍，再用官方样题练手感。证书不等于能力，项目里摸过的坑才等于。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：建"我的三个 Kit"书签夹

{class="mt-1"}
在浏览器里建一个书签文件夹，存三条：Form Kit 的 API 参考页、元服务与应用接续相关的指南页、分布式能力的文档入口。这一章之后的每一次开发，你都会反复回到这三个页面——提前存好，别每次都靠搜索碰运气。
:::

#### 十三、问答：关于卡片、元服务与分布式的八个真实疑问

这三个话题在社区里的提问质量两极分化：一边是"能不能放视频"这类预期错位，一边是"刷新次数上限到底多少"这类谁都不该背的精确数字。挑八个最常被问的，答案尽量给判断依据——很多决定取决于你的具体场景，替你拍板反而害你。

<strong>问：卡片加上桌面就不动了，定时刷新明明配了，是不是系统坏了？</strong>

答：先按顺序自查：updateEnabled 开了没有；periodicRefresh 的单位是分钟，写成秒级会被系统拒；系统对刷新有调度偏差和每日次数上限，"设了 30 分钟"不等于"第 30 分钟准时跳"。最关键的一步：给卡片加"更新于 XX:XX"小字，观察一天——十有八九它在刷，只是你没证据。真的一整天纹丝不动，再回头查 formId 存没存对、updateForm 有没有报错日志。

<strong>问：卡片里能放视频、长列表、复杂动画吗？</strong>

答：基本不能，也不该。卡片是受限的运行环境，交互以"轻操作加跳转"为主，能力边界以官方文档为准。真想炫，把炫的部分留在应用里——卡片管好"瞥一眼"，就已完成它的大半使命。反过来说，如果你的核心信息必须靠长列表才能讲清，说明它不适合做成卡片，老老实实让人点进应用。

<strong>问：元服务是不是就是微信小程序的翻版？</strong>

答：思路同源——免安装、即用即走，但运行环境完全不同。小程序跑在某个 App 里，元服务跑在鸿蒙系统层，入口是系统级的：扫码、搜索、碰一碰、负一屏。技术栈上你也不需要学新语言，ArkTS 加 ArkUI 那一套原样适用，迁移成本主要在"形态思维"——从"留住用户"转向"完成任务"，而不是语法。

<strong>问：体积超限了，是不是只能忍痛砍功能？</strong>

答：砍功能是最后一步。先资源瘦身——图片、字体、用不到的多语言，超限的大头常在这里；再按需加载拆包（机制以官方文档为准）；还超，才轮到砍功能，标准是"删掉它，核心任务还完成得了吗"。顺序反了，砍掉的是体验，留下的是赘肉。

<strong>问：分布式是不是必须两台新机？用户设备参差不齐怎么办？</strong>

答：流转与协同依赖系统级能力，支持范围视设备与系统版本而定，以官方文档为准。工程上的正确姿势是第十节那套：运行时探测，支持就亮入口，不支持走降级；核心功能永远单设备完整可用。别赌"用户都会有两台新设备"——赌输的那部分用户，就是你的差评来源。

<strong>问：卡片和元服务能组合吗？</strong>

答：能。元服务同样可以配卡片，配置方式与本章讲的完全一致，界面上还多一层"免安装"的属性。对轻场景服务是很好的组合：卡片负责在桌面上露出，点开即用即走，全程没有安装动作。做本地生活类服务时，优先考虑这个组合；做深度工具类应用时，卡片还是留给完整应用更合适。

<strong>问：刷新周期到底该设多少？有没有标准数字？</strong>

答：没有万能数，只有反推法：你的数据一天变几次、用户什么时刻需要它。待办数半小时档足够，天气概览定点一次，分钟级变化的数据就别用卡片承载。系统的最小周期与每日上限随版本调整，以官方文档为准——设计时把"刷不够"当常态来兜底，把按需推送当主力来用，比纠结数字有用得多。

<strong>问：学完这一章，下一步做什么？</strong>

答：三件事按顺序来：给第 76 章的待办清单加卡片（本章的来动手题）；把"快速记一条"做成元服务；有条件借一台设备练接续，没条件就把第十节的降级设计做扎实。都做完，把这三样写进简历的项目描述——面试官问"鸿蒙特有什么"，你有一手体感可以讲，而不是背概念。至于这三个主题上线之后会长出什么新故事，下一节有三张真实的工单等你对号入座。

#### 十四、上线之后：三张工单里的卡片、元服务与分布式

功能写完那一刻，这三个话题才刚刚开始。下面三张工单都来自这类功能的真实迭代路径——用户一句模糊的反馈，追到一个具体的设计缺口，补上之后产品反而更结实。看故事的时候，你可以把自己代入排查者的位置，先猜原因，再往下读。

##### 工单一：待办卡片"每天早上都是昨天的数"

用户原话："卡片天天骗我，应用里明明都清零了，它还挂着三条。"排查第一步看刷新日志：定点刷新确实到点触发了，但凌晨恰好撞上数据源那台服务器的维护窗口，请求失败，扩展按第六节的纪律保留了旧数据——失败保留本身是对的，错的是失败时界面毫无表示，旧数据又没有时间戳，用户无从分辨"这是昨天的数还是今天的数"。修复动作三件：卡片加"更新于 XX:XX"；"当天清零"这类本地状态变化改成即时按需推送，不再完全指望定点；数据源维护时段的失败日志加告警。收获一句话：定时刷新是兜底不是主力，主力永远是"数据变化时自己推"——这条纪律在第六节是建议，在这张工单里是学费。

##### 工单二：停车缴费元服务，码贴了一周没人用

商家反馈："码贴出去了，一天扫的人不少，用完的没几个。"排查链路逐段过：码扫得动、服务拉起快、金额显示对——问题出在首屏，为了"合规稳妥"，团队把登录做进了首屏，而停车场景用户的平均停留时间以秒计，登录墙一立，人就走光了。修复：首屏只剩车牌与金额和一个"确认支付"，身份确认挪到支付环节，把"必须知道你是谁"压缩到真正的最小范围。一周后再看数据，转化明显回升（具体数字以你自己的埋点为准）。收获：元服务的每一步都是流失点，数一下从拉起到核心按钮之间隔了几次点击——超过一次，每一次都得给出站得住的理由。

##### 工单三：接续过来的备忘，丢了后半段

用户反馈："手机上写了两千字的备忘，平板接续过来只剩开头。"排查：发起端 onContinue 确实把草稿放进去了，但塞的是整篇全文——上下文通道适合传"指针"，不适合传"包袱"，内容超出了通道的承载能力，对端拿到的就是不完整的。修复：want 里只传记录 ID，对端凭 ID 从云端拉全文；拉不到就恢复到列表位置并提示，而不是挂一半的内容假装正常。收获：接续传指针，别传包袱；大内容走数据通道，want 里只放"到哪儿了、看什么"这类小状态。第九节那段"接续调试流水"的坑，在这张工单里换了个马甲又出现一次。

三张工单的共同点值得再看一眼：都不是"功能没写对"，是"场景没想全"——没想数据源会维护，没想用户只剩几秒，没想草稿会有两千字。把这三个坑记进你自己的检查清单，比多写三个新功能值钱。上线之后的故事还会有很多，你的迭代记录本从现在就该翻开第一页。

#### 十五、多端适配实战：同一份代码，手机平板都要体面

卡片、元服务、分布式，三样东西都指向同一个前提：你的界面会在不止一种设备上出现。适配不是"再写一套布局"，是在布局里提前留出"随宽度变化"的余地。这一节给一套可操作的打法，配一段示意代码。

##### 断点：先想清楚"宽了之后多出来的空间干什么"

适配的第一问不是"怎么改布局"，是"多出来的宽度该装什么"。待办清单在手机上单列，到平板上多出的空间有三种归宿：装详情面板（左边列表、右边详情）、装更多列（几份清单并排）、什么都不装（整体居中限宽）。三种答案都成立，错的做法只有一种——拉伸：组件原样放大，按钮大得能当镜子照。先定答案，再动手写布局。

##### 监听窗口变化，按档位切换布局

实现思路是"宽屏一个分支，窄屏一个分支"，运行时按窗口宽度切换。示意如下，断点数值与接口细节以官方文档为准：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 按窗口宽度切换布局（示意）</span><span class="dots">···</span>
:::

```
// 窗口尺寸变化时更新 isWide，接口以官方文档为准
window.getLastWindow(this.context).then((w: window.Window) =&gt; {
  w.on('windowSizeChange', (size: window.Size) =&gt; {
    this.isWide = size.windowWidth &gt; this.wideThreshold
  })
})

build() {
  Row() {
    // 列表：窄屏占满整行，宽屏只占一部分
    Column() { TaskList() }
      .width(this.isWide ? '40%' : '100%')
    if (this.isWide) {
      Column() { TaskDetail() }
        .layoutWeight(1)        // 剩下的宽度全给详情
    }
  }
}
```
:::

除了自己监听，ArkUI 还提供自带断点体系的栅格组件，"列表加详情"这类双栏结构用栅格写更省事——两条路都通，挑一条用到底，别一半布局走监听、一半走栅格，维护时你会两头对不齐。阈值怎么定也别拍脑袋：拿真实设备的宽度档位做参照，别对着模拟器随便划一条线。

##### 双栏的第二个收益：宽屏上的"选中态"

宽屏双栏让"点列表、右边变"成为可能，它顺带引入了一个手机上不存在的状态：选中项。窄屏应用没有常驻选中态，宽屏有——记得在宽屏上高亮当前选中的那条，否则用户会盯着右边发问"现在显示的是哪一条"。这类"宽屏专属状态"是适配最容易漏的东西，检查清单里给它单独立一行。

##### 适配检查清单

- 窄屏、宽屏、横屏各过一遍真机——预览器只当草稿纸，真相在真机上。
- 弹窗在宽屏上别铺满全宽，居中限宽更体面。
- 字号跟随系统设置，别在宽屏上偷偷加大。
- 点击区域不因布局变宽而缩小，按钮也不因变宽而变形。
- 深浅色在两种布局下各验一遍——第 77 章的双份资源在这里同样生效。
- 宽屏选中态有高亮，且与右侧内容联动。

##### 折叠屏与自由窗口：把"会变"当常态

折叠屏展开与合上，宽度瞬间换档；应用在自由窗口里可以被拖成任意宽度——界面的宽度不再是发布时定死的数字，而是运行中随时会变的量。这是多端适配的深层含义：布局要能"流动"。把第 37 章那句"变化点封装"搬到布局上：凡是写死的像素与拍脑袋的百分比，都是将来返工的候选名单。官方对多端的审核要求以最新指南为准，但"能过审"只是及格线——真正的目标是这台设备上体面，那台设备上也体面。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：给待办清单开双栏

{class="mt-1"}
按本节的示意代码，把第 76 章的待办清单改成宽屏双栏：列表加详情。验收标准两条——窄屏退回单列毫无残缺；宽屏上点任何一条，右侧内容与左侧高亮严格同步。做完这一题，你就把"多端适配"从口号变成了手感。
:::

#### 十六、性能与功耗："轻"是卡片与元服务的硬指标

完整应用卡一点，用户可能忍；卡片是"别人桌面上的一块"，元服务是"拉起即用"的东西——它们的性能预算不是加分项，是及格线。这一节把两类形态的性能账分开算，每一笔都给到"怎么做"。

##### 卡片：预算小到要按字段计较

formBindingData 传的是数据，别把它当快递车——塞一张大图、一大段 JSON，渲染就可能吃力，超出约束的直接表现为渲染异常（阈值与约束以官方文档为准）。图片要么走链接，要么按卡片实际尺寸裁好再传；文本按"一张卡片一个主题"裁到最短。刷新回调同样以轻为纪律：拼数据加一次请求，别的都不放。

::: div .code-block
:::inline div .code-head
<span>ARKTS · 数据预算意识（示意）</span><span class="dots">···</span>
:::

```
// 只传卡片要显示的字段，别把整个对象扔过去
formBindingData.createFormBindingData({
  'todoCount': '3',
  'latest': '给花浇水'      // 而不是把整个待办对象数组塞进来
})
```
:::

这条纪律还有一个隐藏收益：传得少，接口就清晰。卡片需要什么字段，配置里一目了然，改版时谁动了哪个字段一查便知——大数据包省下的是打字时间，赔上的是排查时间。

##### 元服务：首屏的速度就是产品本身

元服务的成败在首屏速度，做法上没有玄学：首屏只加载首屏——暂时用不到的重模块别在启动时一次全 import（按需加载机制以文档为准）；首屏先呈现结构，数据到了再填充，别让用户对着空白屏等请求；启动期间别做埋点批量上报这类"与用户无关"的事，攒到后台再报。DevEco 自带的 Profiler 能看到启动各阶段的耗时，优化前测一次，优化后再测一次——用数据说话，不用感觉说话。

##### 长列表：滚动到几百条时依然体面

待办清单用上一年，几百条很正常。列表渲染用按需加载的机制（LazyForEach 一类，让屏幕外的条目不占渲染资源），别用一次性全量渲染的写法硬扛。顺带把话说死：卡片里没有长列表这回事——往卡片里塞长列表，既是性能事故，也是规范事故，两头的账都要记在你头上。

##### 功耗：三件"看不见的错"

- <strong>卡片周期刷新设成最短档，数据却一天才变一次</strong>：多刷的那些次数全是白烧的电，第六节的反例，这里再记一笔。
- <strong>元服务退出后定时器、后台任务还活着</strong>：即用即走的形态，退出时就得把该收的都收掉，别留尾巴拖累用户的电量。
- <strong>协同场景两端频繁互发小包</strong>：网络活动有电量代价，能攒一批再发的别一条一条挤。

性能优化的次序永远是：先测量，再优化，最后才轮到"感觉卡"。DevEco 的 Profiler 和你的日志是第一手证据，社区经验只能当线索——线索可以省时间，但不能替你下结论。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2" aria-hidden="true"></i>小贴士

{class="mt-1"}
给卡片和元服务各定一条"性能红线"写进文档：刷新回调里允许做什么、首屏允许加载什么、退出前必须清理什么。红线一旦写下来，评审就有依据，"我觉得可以再加一点"就有了对手。
:::

#### 十七、把三样武器用在一起：一张产品形态清单

单学会三样东西不难，难的是回答"我的产品该用哪几样、各承担什么任务"。这一节以第 76 章的待办清单为样本，把组合思路拼成一张你能直接抄走的表。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">形态</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">承担的任务</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">入口在哪</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">怎么衡量它</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">完整应用</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">深度能力：管理、归档、统计</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">桌面图标</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">留存与使用时长</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">服务卡片</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">今日待办数、打卡轻操作</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">桌面</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">添加率与点击率</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">元服务</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">快速记一条</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">扫码、搜索等系统入口</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">任务完成率</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">接续（分布式）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">手机记的，平板接着整理</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系统接续入口</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">接续成功率与恢复完整度</td></tr>
</tbody>
</table>
```
:::

表里最值得琢磨的是"怎么衡量"那一列——三样轻量形态各有自己的指标，没有一个写着"日活"。卡片比的是露出效率，元服务比的是任务完成率，接续比的是"接得住"的比例。指标定错，优化方向就全错：拿着日活去考核卡片，你会忍不住往卡片上堆功能，堆到用户把它从桌面移除为止。

##### 三个问题，决定你要不要上

1. 有没有"用户不打开应用也想看"的信息？有，才做卡片——没有就别硬造，不是所有应用都值得占据桌面一席。
2. 有没有"进来只为完成一件事"的场景？有，才做元服务；你的产品核心是"长期陪伴"，元服务帮不上忙。
3. 任务是否天然跨设备？编辑、观看这类"接着做"的任务才值得接续；单条信息的查看，跨了也没增益。

##### 给三类读者的用法建议

<strong>出差党</strong>：手机上记的开销、路上看到的书摘，晚上到酒店在平板上接着整理——把接续做好，再配一张"今日待办"卡片，出门在外桌面点一下就知道今天还剩几件事。你的场景是本章三样武器的天然战场，值得完整走一遍。

<strong>小商家</strong>：把"到店扫码即用"的元服务布好（第八节的三个入口），完整应用留给回头客养熟；卡片对你意义不大，别为凑齐三件套而开发——形态是给任务挑的，不是给汇报挑的。

<strong>学生</strong>：这三样是最好的练手组合——一张卡片练刷新与数据通道，一个元服务练取舍，一次接续练状态恢复；每一件都能在一周内做完，也都能写进简历。做完记得给每个都留一份踩坑记录，面试时它比截图管用。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-quote-left mr-2"></i>一句话记牢

{class="mt-1"}
形态服务于任务：先问任务是什么，再挑形态，最后定指标——顺序反了，三样武器都会变成三个负担。
:::

回到这一章开头的判断：三样东西"怎么用"都不难，难的是"什么时候该用"。这张表就是答案的形状——先用三个问题筛，再用一张表分工，最后用各自的指标验收。至于先做哪一样，我的建议从来都是卡片：成本最低，见效最快，而且它就摆在桌面上，天天替你站岗。不过上桌之前，还有两道绕不开的功课——安全，和一份能照着走的计划表。

#### 十八、安全与隐私：三样武器的共同底线

卡片摆在你桌面上，元服务在三秒里完成支付，接续把你的草稿送过网络——这三样形态离用户的数据更近，对安全的功课要求也更高。这一节不讲密码学，只讲"别把用户的东西弄丢、弄露、弄错"。

##### 权限：按"最小够用"再过一遍

写完功能，把应用声明的每一个权限拎出来问一句："删掉它，哪个功能会坏？"答不上来的就是冗余——卡片刷新回调里用不到位置，就别让扩展带位置权限；元服务首屏用不到通讯录，就别提前申请。元服务的审核对权限格外敏感（具体要求以官方规范为准），多申请的每一项都会变成审核问答与用户疑虑的双重成本。权限说明文案照第 77 章的标准写：说清"用它在哪、干什么"，不写"为了提供更好的服务"。

##### 卡片上不摆敏感信息

桌面是半公开场合：地铁上、会议里、咖啡馆的桌上，手机往那一扣是常态。余额、验证码、完整地址这类信息不要上卡片；确实必须显示金额的场景（比如停车缴费），用部分遮掩——露出头尾就够确认，又够安全。给卡片立一条"桌面可读"纪律：被陌生人瞥一眼，不泄露任何可识别的个人信息。这条纪律没有技术门槛，纯粹是设计时多想一步——可惜它常常是最先被忘掉的一步。

##### 支付与凭证：元服务里的钱要走得清楚

元服务最常见的变现环节是支付，守住三条：金额展示与确认分两步，别让"看一眼就扣款"；支付凭据本地留存、可查可对账，出了纠纷用户拿得出证据；退款与客诉路径在服务里写明白。支付本身走系统提供的支付能力（接口与规范以官方文档为准），别自造一套收银流程——钱的事，自作聪明是最贵的聪明。

##### 接续与协同：数据在"路上"的规矩

接续把状态送过网络，协同把数据同步进另一台设备——信任底座由"同账号"担保，你的责任有三条：别把不该走通道的数据塞进通道（十四节工单三的教训换个角度还是它）；敏感内容在本地走加密存储，日志里永远不打印用户正文；设备丢失的兜底提前想——另一台设备上的数据怎么撤、组网怎么解除，答案在官方文档的安全章节，以最新版为准。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2" aria-hidden="true"></i>小贴士

{class="mt-1"}
上线前做一次"数据地图"练习：写下每一类用户数据存在哪、路过哪、谁能看见。画完这张图，你会先吓自己一跳，然后主动砍掉一半不必要的收集——这张图还是隐私说明的现成底稿，上架时直接用。
:::

#### 十九、四周计划：把三样武器装进同一个项目

学完不练等于没学。给你一份能直接照抄的四周计划，把卡片、元服务、接续装进同一个项目——载体还是第 76 章的待办清单。计划的关键设计只有一条：每周结束都有一个能当众演示的成果。

##### 第一周：卡片上线

前三天按第五节走通全链路：模板、配置、刷新、交互。后两天打磨：加"更新于"时间戳、过深浅色、补第二种尺寸档位。周末验收标准两条：重启手机后卡片还在且数据正确；断网一整天，卡片不白屏、不报错。达不了标就别开下一周——地基上的窟窿，越往后越难补。

##### 第二周：元服务与入口

做单页"快速记一条"，按第七节的体积账瘦身；备齐上架材料——名称、关键词、截图，逐字按第八节"像用户嘴里说的话"的标准来。上架流程与审核周期以官方文档为准，把审核往返的时间算进计划，别把发布日期卡死在审核节点上。有余力就把桌上的测试码印出来，拿真手机现场扫一轮。

##### 第三周：接续与降级

实现接续，记住"传指针不传包袱"；紧接着补能力探测与第十节的三种降级姿势。借不到第二台设备不碍事——把降级做扎实本身就是这一周的验收项，而且它才是大多数用户真实会遇到的部分。周末自测两个剧本：有第二台设备的完整流转；只有一台设备时界面零残缺。

##### 第四周：性能、安全与复盘

用 Profiler 测一轮启动与内存，按第十六节的"性能红线"逐条过；按第十八节画一遍数据地图；最后写复盘——三样东西各自的指标是什么、上线后预计会撞上哪几张工单（第十四节那三张可以当预测题，猜中一张算你出师）。四周做完，这个项目就从"书上的示例"变成了"你的作品"。

有人会问：四周是不是太慢？倒过来看就快了——没有这份计划的人，通常在第三个月还在"有空就做"。每周一个可演示的成果，演示会逼你把半成品收尾成成品；收尾的能力，恰恰是自学和上班都最缺的那块肌肉。

#### 二十、问答增补：八个进阶疑问

正文与第十三节收不尽的进阶问题，集中在这里。这一节的答案更短、判断更多——问到这里的人，缺的已经不是入门解释。

<strong>问：卡片的数据能让服务器直接推送吗？我不想等刷新周期。</strong>

答：卡片的刷新由系统统一调度，"服务器直推桌面"不是标准玩法。主流思路是数据先进你的应用或服务端，再按需推送到卡片，或等下一个刷新周期兜底。平台若开放新的推送类通道，以官方文档为准——在那之前，把按需推送用好，多数场景已经够新鲜。

<strong>问：元服务能收费、能内购吗？商业化的路子怎么走？</strong>

答：能力与政策随版本演进，以官方商业化文档为准，别照抄网上旧帖。设计阶段的建议只有一条：先把"任务完成率"做上去，变现方案后置——付费转化建立在"任务真的好用"之上，顺序颠倒了，两头都落空。

<strong>问：鸿蒙版本更新这么快，我现在学的会不会过时？</strong>

答：会过时的是 API 细节，不会过时的是这一章的形态思维——卡片是快照、元服务是任务、接续是指针。API 变了，翻官方文档对齐当前版本就行；思维方式立住了，接口怎么换你都能马上接上。这也是本书把"什么时候该用"讲得比"怎么用"还多的原因。

<strong>问：团队开发时，卡片和元服务该派给谁负责？</strong>

答：卡片横跨主应用数据层与独立的扩展进程，建议由熟悉数据层的工程师主导，界面沿用设计系统，别另起炉灶。最重要的一条是第五节的老话：业务逻辑只留一份——"打卡"写在数据层，卡片和应用都调它。两个人各写一份的那天，就是 bug 报上来那天。元服务同理，能复用主应用服务层的，一行都别重写。

<strong>问：卡片里的图片可以用网络图吗？</strong>

答：可以，但守好三条：尺寸按卡片实际显示裁好，别传原图；加载失败要兜底——占位图或纯文本顶上，别留一块空白砖；别指望卡片自己频繁拉图，图随数据一起推过去更稳。本质上还是那一句话：卡片拿到的应该是"直接能摆上桌"的快照。

<strong>问：元服务能复用完整应用里已登录的用户状态吗？</strong>

答：账号与状态的衔接方式视平台能力而定，具体以官方文档为准，别自己发明跨形态共享登录的野路子。设计上的稳妥姿势：让元服务在"没有登录态"的前提下依然能完成核心任务，登录只锦上添花——第八节的工单已经演示过登录墙能造成多大的流失，别把它从正门再请回来。

<strong>问：分布式和云同步，我的产品该选哪个？</strong>

答：看时间轴。同一时刻、同账号、两端在线的"共填一张表"，用协同；隔着时间、隔着设备的"早上记的晚上整理"，云端同步更稳。两者不冲突：云端为底座，分布式做实时增强——但底座永远先行，第十节的"主流程零依赖"说的就是这件事。

<strong>问：要不要给应用做手表、智慧屏版本？</strong>

答：回到第十七节的三个问题。手表适合做卡片式"瞥一眼"的延伸（下一项待办、倒计时），智慧屏适合媒体与协同场景；任务在那种设备上有真实增益就做，没有就别硬上——为多而多的多端，维护成本会先拖垮你。先把手上的手机平板两头做体面，再谈第三台、第四台设备。

问答到这里收尾。这一章从三个概念讲到四张表、三张工单和一份四周计划，反复只在说一件事：形态多起来之后，克制比能力更值钱。别急着赶路，把这三样各自做熟，比赶去下一个新概念更有用。

#### 二十一、术语速查：这一章的黑话对照表

这一章的术语密度不小，收尾前给一张对照表——写文档、开评审、查报错时随手翻，不用背，用到时回来查。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">术语</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">一句话解释</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">容易混的概念</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">FormExtensionAbility</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">卡片的"数据管家"，回答"卡片此刻显示什么"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UIAbility（它没有界面）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">formId</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每张卡片实例的身份证，刷新按它点名</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">应用包名</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">formBindingData</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">传给卡片的数据快照载体</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">普通组件传参</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">postCardAction</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">卡片上点击行为的唯一声明方式</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">页面路由跳转（卡片里没有那个）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定点 / 周期刷新</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">系统调度的两种定时方式</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">服务器推送</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">按需刷新</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">应用自己调 updateForm 推数据</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定时刷新</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">元服务</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">免安装、即用即走的应用形态</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">小程序（运行环境不同）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">碰一碰 / 扫一扫 / 搜一搜</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">元服务的三个系统级入口</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">应用市场分发</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">应用接续</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把任务上下文交给另一台设备恢复</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数据拷贝、云同步</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">协同</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">两端同时操作同一份数据</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">接续（接续是"过去时"）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分布式软总线</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">设备自动发现与组网的底层通道</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">普通局域网直连</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">降级</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">能力不可用时的替代体验设计</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">报错提示</td></tr>
</tbody>
</table>
```
:::

表收好了，这一章也就到了头。三样"独门武器"——桌面上的卡片、免安装的元服务、跨设备的流转——从怎么写、怎么刷、怎么发，一路讲到怎么省、怎么护、怎么排期。它们共同的起点是第 74 章的 Stage 模型，共同的归宿是你自己的项目。什么时候三样东西在你手里"想到就能做、做完就敢上"，这一章的使命就算完成了。

#### 二十二、一场评审会的实录：三样武器怎么被砍到合适

前面二十节都在纸上讲道理，最后一节换个视角——把你放进一场真实的产品评审会。背景：三人小团队，要给第 76 章的待办清单加"鸿蒙特性"，排期两个月。下面是会议实录，每段对话后附一句"翻译"，告诉你这句话背后用到了本章哪一节的判断。

<strong>产品同学开门：</strong>"鸿蒙特性是差异化，三样全上——卡片、元服务、分布式，两个月排满。"

你的回应："先过三个问题：有没有不打开应用也想看的信息？有没有即用即走的场景？任务是不是天然跨设备？第一问答案是有（今日待办数），第二问勉强有（快速记一条），第三问只有'接着编辑'成立。所以不是三样全上，是卡片全量、元服务单页、接续做完做稳、协同进 backlog。"

翻译：这就是第十七节的三个问题与一张表——评审会上先把"做什么"收敛，再谈"怎么做"，顺序反了就变成功能拍卖会。

<strong>产品追问：</strong>"那卡片干脆显示全部待办列表，一卡顶一屏，多好。"

你的回应："卡片是快照不是页面，桌面规范也不养长列表。卡片管'瞥一眼'：今天几条、最近一条是什么、点一下进应用。列表的事让应用去干。"

翻译：第五、六节的形态认知，加上第十一节的设计规范——"一卡顶一屏"是卡片讨论里最常出现的一句错话，听到就要拦。

<strong>设计同学：</strong>"卡片我出四种尺寸，桌面随用户挑，覆盖全场景。"

你的回应："声明几档就要为几档各出一版布局、各测一遍。两个月里做四档，等于每档都糙。先做两档最常用的，上线看添加分布，数据说哪档有人用，再补哪档。"

翻译：第 37 章的"用数据决定优先级"，加上第十一节的档位纪律——声明的每一档都是一份真实的维护成本，不是免费的选项。

<strong>后端同学：</strong>"刷新我包了，服务端每五分钟推一次，保证新鲜。"

你的回应："卡片刷新走系统调度，有最小周期与每日上限，'每五分钟'本身就不成立；而且我们的数据一天变三五次，半小时档加按需推送已经绰绰有余。推得勤不如推得准，省下来的电是用户的。"

翻译：第六节的四种刷新方式与电量账——刷新频率是产品决策，不是后端的技术自留地；谁提的频率，谁就要说出数据的变化节奏。

<strong>老板拍板：</strong>"分布式是大卖点，就主打它，宣传图都画流转。"

你的回应："流转成立的前提，是用户有两台支持流转的设备、登录同一账号、两端都装我们的应用——三个条件叠完，能亲眼见到这个功能的用户占不到一半（比例以你们自己的用户画像为准）。做，但作为加分项：支持的用户收获惊喜，不支持的用户毫无感知。主打还是卡片——它人人有桌面。"

翻译：第十节的降级思维，加上第十七节的指标表——卖点要建立在多数用户可达的路径上；把主推资源押在少数用户才能触发的条件上，宣传费就白花了。

会议结论落成一句话：卡片全量、元服务单页、接续做稳、协同缓议；主打卡片，其余做深。两个月后回看指标：卡片添加率与点击率达标，元服务任务完成率高但量小，接续成功率受两端版本影响明显——每一条都在预测之内，因为每一条当时都定过指标、写过依赖、备过降级。

##### 会议纪要模板：抄走就能用

- 每个特性一行：形态、承担的任务、入口、指标、验收标准——没有指标的特性，不进排期。
- 每项写明依赖条件：账号、设备数量、审核周期——依赖写得越具体，排期越不玄学。
- 每项写明降级方案：条件不满足时用户看到什么——写不出降级方案的特性，多半自己也说不清它给谁用。
- 留一行"不做什么"：协同进 backlog 的理由写下来——"为什么不做"比"做什么"更能防止三个月后的返工。

评审会的胜负手，从来不是嗓门，是你能把每一句"要"翻译成两句："它的任务是什么""它的指标是什么"。这两句翻译，正是本章十几节想教给你的全部——能力让人能开工，判断力让人敢砍需求。带着这两句话去开你的下一次评审会，这一章，就算真的学完了。

#### 二十三、动手前的三个小练习

不用等四周计划，今天就能做的三个小练习，每个不超过一小时，用来把本章的"知道"变成"摸过"。

<strong>练习一：拆一张现成的卡片。</strong>在桌面长按一个系统自带应用的卡片，观察它的信息结构：主体是什么、按钮有几个、点不同区域分别去哪。对照第五节的三种路由动作，先猜一猜每个点击背后是 router 还是 message——猜完再点，验证你的判断。拆三张之后，你给自家应用设计卡片时手上就有分寸了。

<strong>练习二：数一次"入口体验"。</strong>找一家有扫码即用服务的门店（点餐、租借都行），完整走一遍从扫码到完成任务的路径，随手记下：拉起用了几秒、首屏是什么、到核心按钮隔了几次点击、退出时有没有挽留。用第七、八节的标准给它打分——你会发现自己看元服务的眼光，已经和一周前不一样了。

<strong>练习三：给降级画一张图。</strong>拿你手头任何一个项目，按第十节的表格列出它的分布式特性：支持时显示什么、不支持时显示什么、文案是什么。多数人画到一半会发现：自己清单里有一半特性，压根没想好"不支持的样子"。这张图补完，你的需求文档顺手就厚实了一截。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：今天的十分钟

{class="mt-1"}
打开官方文档，把 Form Kit 指南页的"约束与限制"小节通读一遍。不用记全——只把与刷新、尺寸、内存相关的条目抄进你的笔记。这三类条目，是本章几节正文反复撞上的墙；先知道墙在哪，动手时就不会撞疼。
:::

三个练习加十分钟阅读，凑起来一个多小时，换来的东西叫"手感"。鸿蒙的进阶之路没有捷径，但每一次提前摸过墙角的人，写代码时都会快半拍。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2" aria-hidden="true"></i>小贴士

{class="mt-1"}
三个练习都不依赖写代码，通勤路上、排队间隙就能做一半。把它们排进本周的日历，比"找时间做"靠谱得多——这一章的任务清单至此凑齐了：一张卡片、一个元服务、一次接续、一份四周计划、三个小练习，从今天排队的那十分钟就能开始。
:::

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-quote-left mr-2"></i>一句话记牢

{class="mt-1"}
服务卡片管"瞥一眼"，元服务管"快进快出"，分布式管"接着做"——三句话各配一个指标，进阶之路就有了自己的刻度。
:::

这一节之后不再有新内容了。带着表、带着计划、带着三个小练习，去把第 76 章的待办清单变成一个会跨设备奔跑的应用——路就在脚下，脚下就下一步。

多年以后你想回头看这一章，最快的方式不是翻书，是打开自己的迭代记录——那时你会发现，这一章讲过的每个坑，你都已经亲手绕过，或者亲手踩过一遍了。两种经历都算数，而且后者记得更牢。

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 服务卡片 = 应用的桌面切片，FormExtensionAbility + formBindingData 提供数据
- 卡片设计心法：只放一个最关键的信息，别当缩小版首页
- 元服务免安装即用即走，适合"轻"场景，可独立上架
- 分布式是跨设备流转，先把单设备体验做扎实再考虑
- 三者都建立在 Stage 模型与你已学的 ArkUI 技能之上
:::
