---
id: di-liu-shi-ba-zhang
num: 68
part: ios-kai-fa-pian
nav: 第六十八章：进阶之路——权限、通知与现代架构
toc: default
kind: chapter
---

### 第六十八章：进阶之路——权限、通知与现代架构

{class="chapter-intro mb-4"}
能做出 App 只是开始。这一章聊聊从"会做"到"做好"的几道坎：怎么优雅地申请权限、怎么发通知不讨人厌、怎么把架构再往上抬一层，以及，在 2026 年，怎么和 AI 搭档写 iOS 代码。每一条都是你在真实项目里马上会遇到的。

::: div .quick-read
##### 本章速读（5 分钟版）
这一章是从"会做"到"做好"的进阶课：怎么优雅地申请权限、怎么发通知不讨人厌、怎么把架构再往上抬一层（协议抽象、可测试），外加 2026 年怎么和 AI 搭档写代码、Swift 并发怎么不踩线，最后解锁小组件和快捷指令两个"生态红利"。每一条都是你做真实项目时马上会撞上的。
最关键的有三件事。第一，<strong>权限是信任问题，不是技术问题</strong>：三步走，Info.plist 里先声明用途文案（漏了这步，申请时直接崩）、"正要用的那一刻"才弹窗、被拒后给一条一步可走的降级路（手输城市、跳设置）。文案写"用于拍摄记账凭证照片"这种人话，别写"提供完整功能"的空话；系统弹窗通常只弹一次，时机选对比代码写对更要紧。第二，<strong>通知三条纪律：只发有用的、让用户能关、别半夜骚扰</strong>：弹授权窗之前先用自己的界面解释一遍（"开启后每天 20 点提醒你记账"），同意率高一截；"每天 20:00"这类提醒用日历触发器，identifier 固定可覆盖旧提醒；远程推送留给"服务器才知道的事"（到账通知），手机自己知道的事本地通知就够。第三，<strong>架构进阶就两板斧</strong>：单向数据流加协议抽象——ViewModel 只认协议，测试时注入假数据源，算钱的逻辑毫秒级测完；别过度设计，单人项目"@Observable 类 + 协议抽象"就是全部起步装备。
今天就能做的最小动作：打开 Info.plist 把每个用途描述通读一遍，改成一句话能回答"为什么要"的人话；再在真机上把授权、拒绝、跳过三条路各走一遍，看每种状态下界面是否体面。
最大的坑：一启动连环弹权限（用户全拒绝然后卸载）；没声明用途描述就申请（当场崩溃）；被拒后警告轰炸、申请了用不上的权限（审核和用户两头都问）；小组件总显示旧数据，多半是两个 target 的 App Group 名字没配对或忘了用 suiteName 共享存储；并发这边，界面状态只能在主线程改，给 ViewModel 标上 @MainActor 一次解决，别到处写 unchecked 绕过编译器检查，编译器报错是在替你挡子弹。
##### 速查表
- 权限三步：Info.plist 声明（漏了必崩）→ 用时申请 → 被拒引导去设置，降级入口放眼前
- 弹窗时机：用户一秒内说得出"为什么是现在"才弹；启动只问"没它跑不起来"的那一个
- 用途文案公式：用于 + 具体动作 + 给你的好处，如"用于拍摄记账凭证照片"
- 通知三纪律：只发有用的、每类有开关、夜间默认静默；先解释再弹授权窗
- 本地还是远程：手机自己知道的事用本地通知，服务器才知道的才上 APNs 推送
- 通知排查五步：授权状态、触发时间、专注模式、横幅子开关、delegate 顺序
- 可测试架构：ViewModel 只认协议，测试注入假数据源，算钱逻辑毫秒级测完
- 小组件旧数据：先查 App Group 名字一字不差、共享存储是否用 suiteName
:::

<div class="version-anchor">本章界面路径按 iOS 18.x / HarmonyOS 5.x / Android 15 核对（2026 年 11 月）。你的机型或系统版本不同，菜单名字和位置可能对不上——以你手机上显示的为准。</div>


#### 一、权限：先敲门，再进门

相机、定位、通讯录、通知……这些"敏感地带"，iOS 要求 App <strong>在用到时向用户弹窗申请</strong>。规矩是"声明 + 申请 + 优雅降级"三步：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 权限申请（以定位为例）</span><span class="dots">···</span>
:::

```
// 1. Info.plist 里声明用途文案（不声明直接崩溃！）
// Privacy - Location When In Use Usage Description: "用于查询你所在城市的天气"

// 2. 用的时候申请
import CoreLocation

@Observable
class LocationModel {
    private let manager = CLLocationManager()

    func request() {
        switch manager.authorizationStatus {
        case .notDetermined: manager.requestWhenInUseAuthorization()
        case .denied, .restricted: /* 引导去设置里开 */
        default: /* 已授权，开干 */
        }
    }
}

// 3. 被拒后优雅降级：给提示 + 跳设置
// UIApplication.shared.open(URL(string: UIApplication.openSettingsURLString)!)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>注意：iOS 权限的"一次性"

{class="mt-1"}
iOS 的权限弹窗<strong>通常只弹一次</strong>——明确拒绝后再也不会弹（定位有"仅本次允许/下次再问"选项，选它下次还会问）。所以：申请的时机要选在"用户正要用的那一刻"（而不是一启动就弹一堆），文案要说明用途。被拒后的界面引导（"去设置里开启定位"）是标配，别让用户困在死胡同里。
:::

##### 权限清单：你迟早要敲的那些门

iOS 把"敏感地带"管得很细，每个权限都是一扇单独的门：有自己的弹窗、自己的 Info.plist 用途描述键、自己的设置页开关。常用的门列成一张表，"申请时机"一列最关键，后面专门讲：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">权限</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">典型用途</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">什么时候申请</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">被拒后的降级</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定位（使用期间）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">天气、附近门店、按城市汇总</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">进入相关功能的瞬间</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">手动输入城市</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">相机</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">拍照附件、扫码</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">按下拍摄按钮时</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">改从相册选</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">相册</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">选图、保存图片</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用户点"选图"时</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">提示改用相机</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">麦克风</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">录音、语音输入</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">点下录音键时</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">退回文字输入</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">通讯录</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">导入联系人</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用户主动导入时</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">手动输入</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">蓝牙</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">连接耳机、手环</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">进入设备连接页时</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">提示手动配对</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">本地网络</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">发现局域网设备（打印机、投屏）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">首次用到该功能时</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">提示改走云端</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">日历 / 提醒事项</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">写入日程与还款提醒</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用户点"加入日历"时</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">仅 App 内展示</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">通知</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">记账提醒、到账通知</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">先解释再弹（见下一节）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">App 内红点与横幅</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
常用权限与申请时机对照表

填写细节说清楚：用途描述键都在 Info.plist 里，名字以 Privacy 开头、以 Usage Description 结尾，Xcode 编辑 Info.plist 时能看到带中文的展示名，点加号照提示添加即可。文案不是走过场，用户看得懂就点"允许"，看不懂就点"拒绝"，审核也会揪着含糊文案不放。写文案的公式很简单：<strong>"用于 + 具体动作 + 给你的好处"</strong>，比如"用于拍摄记账凭证照片"，十二个字，比"需要访问相机以提供完整功能"体面得多。

读表的方法也说一句：先看"什么时候申请"列，它决定了你功能流程里弹窗的位置；再看"被拒后的降级"列，它决定了你的界面要准备几套。两列合起来，就是把"权限"翻译成"产品流程"的全部工作，写代码反而是最快的一步。

通知在表里也是一格，值得多看一眼：它和别的权限不一样，别的权限撑功能，通知撑的是"用户关系"。所以通知的申请要配解释（下一节细讲），降级方案是 App 内的红点与页内横幅：即使通知权限没了，重要信息也要有路走得到用户眼前。权限表不是填完就忘的表，每个新版本都该回头对一遍。

表格里还有个隐藏规律：越是"事后才需要"的权限，越要晚申请。相册权限在用户想导出流水图片那一刻才弹，他毫无疑虑；启动就弹，他警觉三分。把这张表贴在项目笔记里，每加一个功能回来对一眼："我要不要现在申请？"的答案通常就在表里。

##### 为什么苹果管这么细：权限背后的隐私逻辑

把视角抬高一层的答案：苹果把每个权限都设计成"单项授权、随时可撤、用途可见"。单项授权，你要相机就弹相机的窗，不能打包捆绑；随时可撤，设置里每个开关都当场生效，App 下一次使用就得重新适应；用途可见，弹窗文案 + 商店页隐私标签 + 隐私清单（本章第三节）。三处互相印证。安卓篇讲权限时你见过类似的思路，iOS 把它执行得更"钉是钉铆是铆"。

这套逻辑对开发者的实际影响只有一条：把每个权限当成"向用户借的东西"。借的时候说明用途（文案）、按需开口（时机）、随时准备归还（降级）。按这个心态做权限，审核和用户两头都顺，反之，把权限当"一次拿走的资产"，迟早被系统或用户清算。

给爸妈做 App 时，权限还有一层特殊讲究：弹窗出现的那两三秒，他们读不完你的用途文案，凭"红点还是蓝点"做决定。所以对长辈用户，解释要提前到弹窗之前的界面里，字号放大、句子缩短；被拒后的降级路径更要"一步可走"，你示范过就知道，让长辈在设置里翻三层开关，基本等于放弃。第 27 章的适老化原则在权限场景同样适用。

##### 申请时机："正要用的那一刻"的三层含义

"正要用的那一刻"不是教条，是原则，具体到每个 App，判断标准只有一条：弹窗出现时，用户能不能在一秒内说出"为什么是现在"。说得出来，时机就是对的；说不出来，再往后放放。拿着这条标准，把你 App 的每个权限弹窗重新过一遍，比任何教程都灵。

第一层，物理时机：弹窗出现在用户点击了具体功能的瞬间。拍照附件功能，申请相机的代码写在"拍照"按钮的响应里，用户对"为什么弹"的预期和你完全同步。一启动就弹五个权限的 App，用户的第一反应是"这 App 想干嘛？"——拒掉一个，其他全受株连。

第二层，叙事时机：系统弹窗之前，先用你自己的界面把事情讲一遍。记账本想用定位查"附近消费"，先在设置页放一行"开启定位后可按城市汇总消费"，用户点"开启"再弹系统窗。系统弹窗没有"等等我考虑一下"的选项，你的界面就是那个缓冲区，把解释做足，弹窗出现的时刻用户早已心里有数。

第三层，降级时机：权限被拒的那一刻，功能要能体面地缩回去。定位被拒就手输城市，相机被拒就只留相册入口——功能消失比功能降级更伤用户，而降级方案是可以提前设计好的。三层时机叠加起来，就是那句话的完整含义：先敲门，再进门，被拒了也别把门焊死。

##### 权限弹窗之外的"软门槛"

不是所有"要资源"的环节都会弹你控制的窗。相册的读取就是典型：现在多数场景走的是"系统选择器"，用户在系统给的选图界面里挑，挑完 App 只拿到选中的那几张，全程不用申请整本相册的权限。能走系统选择器就别申请完整相册权限：用户的顾虑少一半，审核的疑问也少一半。"添加到相册"是另一个轻量档位，只写不读，弹窗里也写得明明白白。

本地网络权限则是另一个极端：它不受理你的时机控制，App 第一次真正尝试访问局域网时，系统自动弹窗，你想提前也没法提前。所以对这类"系统代管"的权限，功课要下在降级设计上：弹窗被拒后，功能界面要能说清"去设置 → 隐私与安全性 → 本地网络 里打开"。每个权限的脾气都不一样，动手前先摸清它弹不弹、什么时候弹、能不能引导。

##### 场景实战：给天气 App 接入定位权限

用第 66 章的天气 App 走一遍完整流程，你照着就能抄。第一步，Info.plist 加键（Privacy - Location When In Use Usage Description），文案"用于查询你所在城市的天气"。第二步，建 LocationModel（上一节的代码原样可用），把申请逻辑包在模型里而不是视图里——界面上只调 <code class="inline">vm.request()</code>，权限细节全部收进模型层，这正是下一节架构要讲的事。

第三步，设计申请时刻：天气 App 打开就需要定位（这是少数"启动即合理"的权限），但仍然先给一屏"城市选择 + 底部一行小字：允许定位可自动获取当地天气"，用户点了"自动获取"再弹窗。第四步，处理三态：未授权 → 申请；已授权 → 拉天气；被拒 → 显示"手动输入城市"输入框加一行"去设置里开启定位"的链接按钮。

第五步，测三遍：模拟器里用假定位测正常路径；设置里关掉权限测被拒路径；再选"仅本次允许"测那个特殊状态，下次启动状态回到未决定，弹窗还会来。三遍都过，这个权限才算接入完毕。你会发现真正花时间的不是写代码，而是把"人"的路径想全。

这五步里藏着一个通用模板——权限功能的状态机：未询问（展示解释 + 申请按钮）→ 已授权（正常功能）→ 已拒绝（降级 + 设置跳转）。任何权限功能都能套这个四态模型来画界面，先画状态图再写代码，弹窗时机和降级路径自然就对了。

最后补第六步：留档。把这次的 Info.plist 键名、文案、申请时机、降级路径写进项目文档，下一个功能要权限时，照着这份"施工记录"抄，十分钟起步，且不会漏掉环节。文档是写给未来的你的，那时你会感谢现在记笔记的自己。

##### 定位权限的分级：使用期间、始终与"仅本次"

定位权限值得单独展开，因为它有三档。第一档"使用期间"（When In Use）：App 在前台时能用定位，绝大多数 App 的正确选择，本章代码用的就是它。第二档"始终"（Always）：后台也能定位，系统会分两步走——先给使用期间，用了一段时间后你才有资格申请升级到"始终"，而且设置页里有独立开关。只有"App 不开着就失去意义"的功能（导航、跑团轨迹）才走这条路。

第三档是用户手里的"仅本次允许"：不算授权，算"临时通行证"——本次会话有效。下次启动回到未询问。它对开发者的含义是：定位功能的授权检查要宽容状态回退，界面要随时能从"已授权"切回"未询问"而不崩、不丢数据。三档之间的关系记成一句话：从窄往宽易，从宽往窄难，永远先申请窄的，让用户自己升级。

##### 被拒之后：别把用户困在死胡同

被拒后的界面是标配三件套：状态提示（"定位未开启，只能手动选择城市"）、降级功能入口（直接把城市选择器递过去）、去设置的跳转。跳转用 openSettingsURLString——代码注释里已经出现过。注意两点：跳转按钮的文案要具体（"去设置里开启定位"比"开启权限"好），而且每次进入相关页面都要重新检查授权状态，用户可能刚从设置里打开回来，也可能上次拒绝过这次想通了。

定位还有个特殊情况值得单独记：弹窗里有"仅本次允许"选项（避坑盒里提过），选了它，App 这次能用，下次启动又会问。所以授权检查逻辑不能只跑一次，每次用到都查，这不是多余，是定位权限的特殊玩法。顺带说"始终允许"：那是另一档授权（后台也要定位），只有导航、外卖骑手这类场景才配得上，工具类 App 别去申请，用户会警惕，审核也会问。

降级文案的写法也给个模板："定位未开启，你可以手动输入城市，或在设置里开启定位。"，一句话里同时给出退路和入口，不指责、不施压。用户拒绝权限不是拒绝你这个人，多数时候只是"还没想好"，把台阶留好，回头率高出不少。

降级设计有一个容易漏的角落：权限状态变化要反映到界面上。用户从设置里打开权限回到 App，界面还停在"请开启定位"的旧状态，除非你重新检查。所以"进入页面时查一次 + 回到前台时查一次"是稳妥的双保险，代码量两行，体验差一个档次。

##### 代码组织：把权限状态机做成可复用的模板

上面天气 App 的四态模型（未询问 → 已授权 → 已拒绝 → 降级运行）别只写一次就丢，把它抽成模板复用。做法：每种权限写一个对应的"状态模型"（像上一节的 LocationModel），对外只暴露三样东西：当前状态、申请方法、跳设置方法；界面层根据状态渲染四种界面，不碰任何权限 API。第二个功能要权限时，照模板再写一个模型，十分钟接完。

这个模板还有个隐藏好处：权限逻辑集中在一处，第 67 章说的单元测试才有落点，"被拒时应该返回降级状态"这类逻辑，注入假状态就能测。散落在视图里的权限代码既测不了，也容易在不同页面写出不一致的提示文案。集中、复用、可测，权限代码也要讲架构。

##### 权限的测试清单：五条路径都要跑

权限功能的测试不是"弹窗出现就完事"，照这张清单跑全五条路径：

- 全新安装第一次进入功能：弹窗出现，文案正确。
- 允许后使用，功能完整，无多余提示。
- 拒绝后使用：降级生效，界面不空洞、不报错。
- "仅本次允许"（定位），本次能用，下次状态回到未询问。
- 使用中途去设置改权限再回来，界面状态跟得上变化。

第五条最容易漏，也最容易出事故：用户兴冲冲去设置开了权限，回来发现 App 还在"未开启"状态，两次之后他就不再尝试了。状态要"跟着用户走"，这条清单值得进你的项目文档。

##### 常见权限疑问三连

<strong>问：能不能不弹系统窗，直接替用户点头？</strong>不能。敏感权限的授予只能来自用户本人的系统弹窗，没有任何 API 能跳过它——这是设计出来的秩序，不是技术没做到。你能做的是把"问"包装得体面（先解释），而不是绕过它。

<strong>问：弹窗文案的字数有讲究吗？</strong>以 Info.plist 里能写清为准，弹窗只展示这段文案，太长的句子会被截断。把最重要的词放前半句，别让"用途"二字被省略号吞掉。

<strong>问：用户点了"允许"，我怎么第一时间知道？</strong>授权结果在回调里返回（前面代码里的 granted），或者随时读 authorizationStatus。别自己猜——状态要读，不要记。

<strong>问：能不能在 App 内做一个"模拟授权页"替代系统弹窗？</strong>不能替代，只能补充。你做的"解释页"是系统弹窗的前奏，两者是接力关系——解释页负责讲清为什么，系统弹窗负责完成授权，谁也替不了谁。

##### 错误示范：三个真实翻车现场

<strong>翻车一：启动连环弹。</strong>天气 App 一启动连弹定位、通知、相机三个窗，用户慌了，全部拒绝，第二天卸载。纠正：启动只问"没它跑不起来"的那一个（定位），其余等功能被用到时再问。弹窗是信任的消耗品，省着用。

<strong>翻车二：用途文案写废话。</strong>"该应用需要访问您的相机以提供完整功能"——等于没说。纠正：一句话说清用途和好处："用于拍摄记账凭证照片"。这种空话文案苹果是真会拒的，别赌。

<strong>翻车三：被拒后警告轰炸。</strong>用户点了拒绝，App 每次进入页面都弹一个自制的"请开启定位权限！"警告框，把用户逼疯。纠正：提示只出现一次，安安静静把降级功能摆在那儿，让用户自己决定。骚扰式引导的唯一作用是教会用户卸载。

<strong>翻车四：申请了用不上的权限。</strong>App 里明明没有扫码功能，Info.plist 里却有相机用途描述，还申请了相机权限——审核会问"这个权限用来干什么"，用户会怀疑"它要相机干什么"。权限宁少勿多：用不到的声明和申请一律删掉，保持"权限清单 = 功能清单"的对应关系，这也是隐私标签能如实填写的前提。

<strong>翻车五：降级功能藏在四级菜单里。</strong>定位被拒后，"手动输入城市"的入口被塞进设置页最深一层，用户找不到，以为 App 坏了。纠正：被拒的那一刻，降级功能要出现在当前页面触手可及的位置——权限出了问题，界面要更热情，而不是更冷淡。

把权限这一节收个尾：权限体系里还有两张"纸"要认识，商店页的隐私标签（第 67 章填的问卷）和代码里的隐私清单 PrivacyInfo.xcprivacy（本章第三节细讲）。三样东西，弹窗用途文案、隐私标签、隐私清单，必须互相印证、指向同一个事实。任何一处说了另一处没做的事，审核或用户信任都会出问题。权限不是一行代码的事，是一套承诺的事。

#### 二、通知：在正确的时间说有用的话

通知是 App 触达用户的通道，也是最容易被用户"拉黑"的功能。iOS 用 <strong>UserNotifications</strong> 框架，发通知三条纪律：<strong>只发有用的、让用户能关、别半夜骚扰</strong>。基础用法：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 本地通知</span><span class="dots">···</span>
:::

```
import UserNotifications

// 1. 申请通知权限（弹窗一次）
UNUserNotificationCenter.current()
    .requestAuthorization(options: [.alert, .sound, .badge]) { granted, _ in
        print(granted ? "已授权" : "被拒绝")
    }

// 2. 安排一条"每天 20:00 记账提醒"
func scheduleDailyReminder() {
    let content = UNMutableNotificationContent()
    content.title = "记账提醒"
    content.body = "今天还没记账哦"
    content.sound = .default

    var comps = DateComponents()
    comps.hour = 20
    let trigger = UNCalendarNotificationTrigger(dateMatching: comps, repeats: true)

    let request = UNNotificationRequest(
        identifier: "daily-reminder",
        content: content,
        trigger: trigger
    )
    UNUserNotificationCenter.current().add(request)
}
```
:::

注意：iOS 的通知权限同样"只弹一次"，且用户随时可以在系统设置里关掉：所以通知内容的价值感很重要，滥发一次可能就永远失去用户。

提个升同意率的小招数：<strong>第一次弹系统权限框之前，先用自己的界面解释一遍</strong>——比如记账 App 先说清"开启后每天 20 点会收到一条记账提醒"，再调 requestAuthorization。先解释再弹窗，同意率和留存都会好很多；系统弹窗只有一次机会，别浪费在用户还莫名其妙的时候。

##### 授权策略：同意之外还有别的路

requestAuthorization 的 options 参数决定申请什么：.alert 是横幅与提醒、.sound 是声音、.badge 是角标，要几个申请几个，别全都要（申请得越多，用户犹豫越久）。这三个开关在系统设置里还能被用户单独关掉，所以"授权了"不等于"三项都开着"，重要提醒别只依赖声音。

授权还有一条"低摩擦通道"：申请时加上 .provisional（临时授权），系统不弹窗，通知安静地投进通知中心，不响铃、不横幅，用户在通知中心里看到后可以选择保留或关闭。对记账提醒这类低打扰场景很合适：用户没被打断，也先尝到了通知的价值。名字记作"临时授权"，用它换来的用户，往往是真需要你的。

授权状态也不止两态：.notDetermined 是还没问过（找机会问）、.denied 是明确拒绝（引导去设置）、.authorized 是正式授权。还要认识一个新角色："时效性"通知（Time Sensitive），标记后的通知在专注模式等场景下有更高呈现优先级，系统设置里有单独开关。别滥用：你的记账提醒是不是真的"时效"，用户说了算，滥用一次，设置里那个开关就会替用户关掉你。

给授权状态做个小结：每次发通知前都该实时查询当前状态，别拿缓存的"上次结果"当真理——用户随时会去设置里改。状态对了发通知，状态不对发沉默，这条纪律能避免九成"通知翻车"。角标权限（.badge）顺带说一句：它管的是图标上的数字，授权里没有它，横幅和声音照常，三个选项是三个独立开关，别把它们当成一回事。

##### 通知的 A/B：给自己发一周

写完通知逻辑，有个土办法但极其有效：把自己的手机当用户，开启全部提醒，真用一周。你会发现"每天 20:00"有时正撞上加班开会，"预算提醒"的文案在锁屏上读起来莫名尴尬。角标清不干净的图标看着心烦。一周之后，你会主动砍掉一两条、改掉两三条措辞，这种"自产自销"的一周，比任何评审会都诚实。

再升级一步：拉两三位真实用户做同样的"一周实验"，请他们每人记录"哪条通知让你烦了"。产品级的通知节奏，就是这样一轮一轮磨出来的——第二节开头那三条纪律，是这一周实验的总结，不是凭空的口号。

顺带说说通知的呈现位置，帮你理解 .alert .sound .badge 各管什么：横幅在屏幕顶部一闪而过；锁屏上会停留成卡片；通知中心（锁屏页向上滑或下拉）是所有通知的历史归档。用户可以在系统设置里按 App 单独配置这三处各自展示与否——所以同一条通知，不同用户看到的形态可能完全不同。不是控制形态，是保证内容在"只剩一行文字"时依然说得清楚。

那"第一次问的时机"怎么定？给你一张决策小抄：启动即问只适用于"这个 App 的核心价值离开通知就不成立"的场景（纯提醒类工具）；其余一律"用时问"。记账本的"预算提醒"是可选增强。放在设置页里，开关打开时问；天气 App 的"暴雨预警"接近核心价值，首次进入城市页时问。拿不准就往后放：晚问的代价小，错问的代价大。

##### 前台与点击：Delegate 两件套

通知还有两个"用户看见之后"的时刻要处理，都在 UNUserNotificationCenterDelegate 里。第一件：App 正开着时收到通知，系统默认什么都不显示（对，默认是静默吞掉的）：要横幅就得在 willPresent 回调里声明展示方式（横幅、声音、角标，按需组合）。新手最常撞的就是这堵墙："通知授权了、代码跑了，怎么 App 开着的时候什么都看不见？"，就是忘了这个回调。

第二件：用户点通知进来，didReceive 回调里拿到通知携带的信息，跳转到对应页面，"记账提醒"点进去直接开录入口，"预算超标"点进去直达统计页。让通知可点、点进去有戏，通知才算完整。两件套的 delegate 要在申请权限之前设置好，顺序反了会漏掉第一批通知，这是个经典时序坑，记在小本上。

测试这两个回调也有技巧：前台展示好测（App 开着等通知就行）；点击响应的测试要"从真通知点进去"：锁屏或通知中心里点，而不是从 App 里模拟。调试时可以把触发时间改成一两分钟后，锁上屏幕等它响。验证完再改回正式时间。别怕麻烦，这两个回调出问题时，用户看到的是"点通知没反应"：比崩溃还让人困惑。

通知还能带"按钮"。给通知注册一个类别（category），类别里声明动作（比如"知道了""明天再提醒"），横幅下拉就会出现可点的按钮，用户点了在 didReceive 回调里收到。记账提醒配一个"明天再提醒"按钮，就是 notification 时代最贴心的功能之一——默认不弹、按需使用，别一上来就塞三个按钮。

##### 触发器三兄弟：定时、间隔、位置

本地通知的灵魂在触发器，系统给了三位常客。老大 UNCalendarNotificationTrigger——按日历规则触发，上面代码里"每天 20:00"就是它（dateMatching 只匹配写到的分量，repeats: true 表示每天循环）。记账提醒、周报提醒都用它。老二 UNTimeIntervalNotificationTrigger："从现在起 X 秒后"，适合倒计时场景：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 10 分钟后提醒一次</span><span class="dots">···</span>
:::

```
let content = UNMutableNotificationContent()
content.title = "专注结束"
content.body = "已经专注 10 分钟，起来喝口水吧"
content.sound = .default

let trigger = UNTimeIntervalNotificationTrigger(timeInterval: 600, repeats: false)
let request = UNNotificationRequest(identifier: "focus-over",
                                    content: content,
                                    trigger: trigger)
UNUserNotificationCenter.current().add(request)
```
:::

老三 UNLocationNotificationTrigger：进出某个区域时触发，"到家提醒我取快递"就是它（依赖定位授权，用前先把上一节的功课做足）。三兄弟各管一头：按钟点、按间隔、按位置，覆盖了本地提醒的绝大多数需求。

日历触发器还有两个细节值得知道：dateMatching 只匹配写到的分量——只写 hour 就是"每天这一小时"，补上 weekday 就是"每周这一天"，粒度由你决定；只写不 repeats 的话，匹配到的"下一个"时刻触发一次就完事。想清楚了再排——"每天 20:00"和"今天 20:00"是两个不同的 trigger，写错粒度的提醒，用户会在错误的时间收到它。

顺带两个管理动作。identifier 相同的通知请求会互相覆盖，用它实现"提醒已存在就更新时间"，而不是叠加出三条重复提醒；UNUserNotificationCenter.current().removeAllPendingNotificationRequests() 能清掉所有待发提醒，用户在设置里关闭提醒功能时记得调用，别让"明明关了还响"的事故发生。还有个数字要心里有数：系统对待发通知有数量上限（以官方文档为准），所以别把通知当数据库用，安排十几个"未来提醒"是自找麻烦。

##### 远程推送：消息是怎么跑上手机的

本地通知是 App 自己排的闹钟，远程推送则是"你的服务器叫醒用户"。链路是这样的：你的服务器把消息（带接收者、文案、角标等）发给苹果的推送服务 APNs，APNs 通过它与设备之间维护的长连接把消息投到手机，系统再决定横幅、声音、角标怎么呈现。你不用自己维持长连接：这条命脉是 APNs 替你保管的，这也是苹果推送省电又稳定的底层原因。

对你来说要准备三件事。一是推送配置：在开发者后台生成推送密钥（.p8 文件），交给服务器侧使用。二是设备令牌（device token）：App 启动时向系统注册推送拿到，交给你的服务器存起来，它可能变化，服务器要能更新，别把 token 当永久地址。三是服务端发送逻辑：按用户、按时区、按静音时段筛选，写好 JSON 载荷发给 APNs。三件事里两件半都在后端，可见推送的门槛主要在"得有个后端"。

判断该不该上远程推送。一句话标准：<strong>消息是否产生于服务器</strong>。到账通知、系统公告、他人评论，服务器才知道的消息，走推送；"晚上十点该记账了"，手机自己知道的事，本地通知就够。个人小项目没有后端，先用本地通知把价值做出来，等有了服务端再接推送；第三方推送服务能帮你省掉大部分服务端工作，配置仍以官方文档为准。

真上了推送，还有两个服务端纪律要带过去：一是"用户分组"：按用户设置和偏好分组发送（只给开了周报的人发周报），别全量广播；二是"发送记录"——服务器端留一份发送日志，线上出现"通知风暴"（某个 bug 导致连环推送）时，能快速止损。推送的后端不是写完发送函数就完了，克制与可停，是它的成人礼。

两个进阶名词混个脸熟。静默推送（不带横幅，专门用来悄悄唤醒 App 更新数据，节制使用）；通知服务扩展（通知展示前给它加附件、解密内容，做富媒体推送时才用得上）。现阶段知道它们存在即可，用到时再查文档。带着问题学，比抱着名词表背快得多。

记账本这种"没有消息产生于服务器"的 App，结论很明确：本地通知足够，远程推送可以不碰：省下后端的时间和钱，用户也少了一项隐私申报。等功能真的长出"服务器才知道的事"（比如多人共享账本、云端备份提醒），再回头接推送不迟。

##### 场景实战：给记账本加"预算超标"提醒

把这一节的知识串成一个真实功能，照着做就能落地上线。需求：用户设定每月预算（比如 2000 元）。支出接近或超过预算时提醒一次。设计决策三步走：判断逻辑放哪，放 ViewModel（它管业务规则，下一节细讲）；发什么通知，本地通知（手机自己知道的事）；发几次——只在跨过阈值的那个瞬间发一次，同一个月不重复轰炸。

实现路径四步：设置页加"每月预算"输入项，存进 SwiftData；ViewModel 里每次记完账对比"本月支出与预算"；跨过阈值且"本月没发过"时，用 UNTimeIntervalNotificationTrigger（间隔设 1 秒）立即发一条，标题"预算提醒"、正文"本月支出已超过 2000 元预算"；发过后把"本月已发"记进存储，月初重置。identifier 固定为 budget-alert，重复发送自然覆盖旧通知。

两个边界情况提前想好：预算中途改小了怎么办——重算"本月已发"状态。允许再发一次新阈值的提醒；当月已经超标、用户又记了一笔——判断条件写"跨过阈值的那一次"，之后同月静默，别把用户钉在耻辱柱上。本地通知还有个让人安心的特性：排好的通知由系统投递，哪怕 App 已经被划掉，到点照样响：这正是"闹钟"与"轮询"的区别。

权限的时机也照规矩来：申请通知权限的动作放在用户点"开启预算提醒"开关的那一刻，弹窗前先在开关下方写一行"开启后，支出接近预算时会提醒你（每月最多一条）"。一个功能把本章两个主题（权限时机 + 通知价值）都练了一遍，这种"小而完整"的功能，最适合练手。

##### 通知的礼仪自查清单

上线前，把这一节的所有原则压成一张自查表，每条通知发出前过一遍，比写十行代码都保值：

- 这条通知用户此刻真的需要吗？删掉"为了发而发"的那一半。
- 标题 + 正文一共不超过两行，信息完整。
- 点击后有明确的落点（对应页面），而不是只打开 App。
- 同类通知有独立开关，用户可单独关掉。
- 夜间时段（以用户当地时间为准）默认静默。
- 每月数一数发了几条：超过"有用的条数"，砍。

最后说角标（badge）：它是通知体系里最容易被忘掉清理的一环。App 图标上的数字角标要记得在用户看完之后清零（应用图标角标有专门的清零接口），一个永远顶着红色数字的图标，是"数字噪音"的典型，用户最后会连 App 一起眼不见为净。角标是提醒，不是装饰，用一次清一次。

排查清单里再补一条系统级的：通知请求的 identifier 要有命名规范（功能前缀 + 用途，比如 budget-alert、daily-reminder），别随手拼字符串。identifier 乱掉的第一症状是"同一条提醒每天弹两次"，因为你排了两个名字不同、内容相同的请求。规范命名不是洁癖，是给未来的排查留线索。

##### 通知写作三规矩：把每条通知当成一条短信

规矩一，一句话说清"发生了什么 + 点进去看什么"。"您本月外卖支出已超过预算"比"您有一条新消息"值钱一百倍——后者是在逼用户点进来猜。标题短、正文一句，别在通知里写段落。

规矩二，时间替用户着想。记账提醒定在 20:00 是体贴，定在 07:30 是讨债。批量推送前想想时区，你的"中午十二点"是用户的"凌晨三点"吗？系统给了按地区发送的能力，用不用是你的责任心问题。

规矩三，每类通知都要有开关。通知设置页让用户按类型订阅（只要预算警告，不要每日提醒），比全局"开/关"留得住人：用户关掉的是"没用的那种"，而不是整个 App 的通知权限。开关本身也是一种承诺：你告诉用户"主动权在你"，用户才敢给你授权。

退一步看全景：通知的价值感是攒出来的。前几条通知如果每次都让用户觉得"这条有用"。授权率和留存会正循环；反过来，一条营销推送就可能让用户进设置把你永久静音。通知是借来的注意力，还本付息的方式，就是每一条都有用。

##### 尊重系统的过滤器：专注模式与定时摘要

你的通知到达手机后，还要过系统的两道过滤器。第一道是专注模式（勿扰、工作、睡眠等）：开启期间，非"时效性"的通知大概率被静默吞掉，只在通知中心留痕，这不是 bug，是用户花钱买了清净。第二道是定时摘要：系统把非紧急通知攒到用户指定的时间段一起投递，你的"预算超标"提醒可能在傍晚六点和购物 App 打包出现。两道过滤器都无法也不该绕过，绕的方式只有一个：内容真到值得"时效性"标记，其余老实排队。

理解了过滤器，"送达率"的概念就该修正：你能保证的是"发出去了"，不是"用户看见了"。所以重要提醒别只发一次通知就完事，App 内的页内提示、角标、下次打开时的摘要卡，都是同一件事的多个表达面。通知只是渠道之一，不是全部。

##### 通知没送到？排查路径五步走

"代码写了、权限给了，怎么没响？"按顺序查五步，绝大多数能定位：第一步，授权状态实时查了吗（被拒后代码照跑，通知默默不投）；第二步，触发时间算对了吗，"每天 20:00"在 21 点安排进去，第一条要等到第二天；第三步，专注模式或定时摘要开着吗——通知到了但被系统攒着或拦着；第四步，App 设置里横幅、声音子项被单独关过吗；第五步，delegate 设置顺序对吗：前台吞掉通知的九成原因在 willPresent。五步走完还没解，把触发时间改成两分钟后实测一次，缩小范围。

还有一个容易误会的现象要提前打预防针：模拟器上通知的行为和真机有差异（锁屏形态、专注模式），最终效果以真机为准。调试期用"两分钟后触发"的临时 trigger 最有效率，别每次都把时间改来改去调真实场景：先用短间隔验证链路，再用真实时间验证体验。

##### 通知与数据：payload 里该放什么

通知携带的数据也要讲分寸，尤其接了远程推送之后：推送的 JSON 载荷里放"指示"（记录 ID、页面路由、类型标记），别放大段内容（完整的账单明细、用户备注）。理由有二：载荷大小有限、大内容应该由 App 拿着 ID 去数据库取权威数据；更关键的是隐私，推送内容会在锁屏上示人，账单金额躺在他人的锁屏上，合适吗？本地通知同理：内容字段写提醒语，细节留给点进去之后。

文案细节再抠一层：称呼用"你"不用"您"（太商务）、数字要具体（"本月已支出 1,860 元"比"支出接近预算"有画面）、动词要明确（"记今天的账"比"别忘了记账"指向清楚）。写完自己读一遍：如果你是收到的人，这条通知值得你停一秒吗？停一秒的标准过了，再发。

通知之间还要"互相认识"。同一天里，每日提醒、预算警告、周报摘要先后到达，用户看到的是三封陌生的短信还是同一个 App 的一致声音？统一标题格式（都带 App 名或功能名）、统一语气、错开时间，把通知当成一个栏目来编辑，而不是三条互不相干的短信。

点击跳转的实现细节顺势说清：didReceive 回调里能读到通知请求的 identifier 和携带字段，用它们做"路由"：按类型分发到不同页面。实现方式是给 App 定一套简单的页面路由约定（一个 switch 就够起步），通知、快捷指令（本章第七节）、小组件（第六节）共用同一套路由——将来入口越多，这套约定越值钱。

通知和小组件还有一层联动：通知改变了数据（比如记了一笔账），别忘了顺手刷新桌面小组件的时间线——桌面上的"本月支出"和通知里说的数字要对得上。数据是唯一的真相，通知、小组件、界面都是它的不同投影，谁的数字旧了，用户对整个 App 的信任就旧了。

##### 给记账本的完整通知规划

把这一节收拢成一份"产品规划"，给记账本定下它的全部通知，多一条不加，少一条补上：

- <strong>每日记账提醒</strong>（可开关，默认 20:00）：核心留存功能，文案温和。
- <strong>预算接近提醒</strong>（达到预算八成时一次），提前量比超支批评更有价值。
- <strong>预算超标提醒</strong>（跨过阈值那一次），正文带具体数字，点进统计页。
- <strong>周报摘要</strong>（可选，周日晚），"本周支出比上周多 12%，主要在餐饮"，一句话说清。

四条通知，条条有开关、条条落点明确、条条每月不超过约定次数。规划写进产品文档，代码照着实现——你会发现"通知系统"的设计难点从来不在 API，在于你敢不敢把多余的那五条划掉。

#### 三、架构进阶：MVVM 深入与可测试性

第 65 章用过 MVVM，这里补几个进阶要点：

- <strong>单向数据流</strong>：界面只读状态、只发事件；数据存取放进独立的模型/服务层。架构的目标就一句话，改一处，不牵连三处，做到就够用了。
- <strong>协议抽象</strong>：让 ViewModel 依赖协议（protocol）而不是具体类，测试时可以注入"假数据源"，这是可测试性的基石。
- <strong>单一职责</strong>：一个 ViewModel 只管一件事（记账的不管天气）；功能多了就拆。
- <strong>别过度设计</strong>：单人小项目，"@Observable 类 + 协议抽象"就够了。VIPER、Clean Architecture 这类重架构，等团队和复杂度找上门再说，工具是服务目标的，不是用来炫耀的。

##### @Observable 到底新在哪

第 64、65 章用的 @Observable，是 SwiftUI 状态管理的新姿势，值得把"新在哪"说透。老写法（ObservableObject 体系）里，一个类要显式声明遵守 ObservableObject 协议，每个想被观察的属性都要包上 @Published，视图这边还要区分 @StateObject、@ObservedObject、@EnvironmentObject 三种持有姿势，样板代码多，新手经常拿错。新写法里，一个 @Observable 宏全包了：属性直接写，谁被读、谁被改，编译器在编译期就生成好追踪代码；视图里简单的 @State 就能持有，跨视图共享走 @Environment。老新对照表放这里：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要干的事</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">老写法（ObservableObject）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">新写法（@Observable）</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">让对象可被观察</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">类遵守 ObservableObject 协议</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">类前标 @Observable</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">标记被观察的属性</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每个属性包 @Published</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">直接写属性</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">视图里持有</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@StateObject / @ObservedObject</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跨视图共享</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@EnvironmentObject 注入传递</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Environment</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
状态管理新老写法对照

细粒度也是真优势：老写法一个 @Published 属性变了，读到它的界面区域整体重算；新写法按属性追踪。视图依赖了哪个属性、就只在哪个属性变的时候更新。列表大了、组件多了之后，这个差别是摸得到的，列表滑动更跟手，界面少做无用功。不过新手阶段别为了"性能"焦虑：多数小项目两套写法都够快，选新写法的理由是"少写样板代码"，性能是附赠品。

还有一个实用细节：@Observable 的类和 ObservableObject 的类可以在同一个项目里并存，第三方库还用老体系就继续老体系，自己新写的类用新宏。它们不是"替换关系"而是"并存关系"，见到老代码不用慌着迁移。

##### 和第 57 章的 MVVM 对个表

安卓篇第 57 章讲 MVVM 时那套话，在这里几乎逐字成立：ViewModel 持有界面状态、View 只描述"状态长什么样"、数据层与界面互不认识、测试对着 ViewModel 写。差异只在"姓名"：安卓的 ViewModel 类在这边是 @Observable 的类，安卓的 StateFlow 在这边是被追踪的属性，安卓的 Compose 重组在这边是 SwiftUI 的视图重建。

跨平台的最大红利因此显现：概念学会了，两边通用。哪天你真的去写安卓，把名字换回去就行；反过来，读过第 57 章的朋友看这节应该处处眼熟。架构思想是 programming 的公共财产，框架只是方言。

一个需要"翻译"的细节：安卓的 ViewModel 有处理配置变更（转屏）的生命周期设计，SwiftUI 这边视图重建是常态、@Observable 对象默认由 @State 持有，转屏不丢状态。同名概念在不同平台上"管的事"略有差别，对表的时候留意语境，别把一个平台的教条硬套到另一个平台。

##### 依赖注入：把"可测试"落到代码上

第二节那句"协议抽象是可测试性的基石"，现在落到代码上。思路三步：先给数据存取定义协议；ViewModel 只认协议不认具体类；生产环境注入真实现，测试和预览注入假数据。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 协议抽象的 ViewModel</span><span class="dots">···</span>
:::

```
protocol RecordStore {
    func all() -> [Record]
    func add(_ record: Record)
}

@Observable
class RecordListModel {
    private let store: any RecordStore
    private(set) var records: [Record] = []

    init(store: any RecordStore) {
        self.store = store
        records = store.all()
    }

    var monthExpense: Double {
        records.filter { $0.type == .expense }
               .map(\.amount)
               .reduce(0, +)
    }
}
```
:::

生产环境里传入 SwiftData 实现的仓库；写 SwiftUI 预览时传一个"内存假仓库"，预览不需要真数据库也能看到界面长什么样；写单元测试时同样传假仓库，业务逻辑就能脱离数据库、脱离网络被验证：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 用假仓库写测试</span><span class="dots">···</span>
:::

```
final class FakeRecordStore: RecordStore {
    var stored: [Record] = []
    func all() -> [Record] { stored }
    func add(_ record: Record) { stored.append(record) }
}

final class RecordListModelTests: XCTestCase {
    func testMonthExpenseOnlyCountsExpense() {
        var fake = FakeRecordStore()
        fake.stored = [
            Record(amount: 100, type: .income),
            Record(amount: 30, type: .expense),
            Record(amount: 20, type: .expense)
        ]
        let vm = RecordListModel(store: fake)
        XCTAssertEqual(vm.monthExpense, 50)
    }
}
```
:::

这个测试跑起来是毫秒级的。没有数据库、没有界面、没有网络，纯逻辑。它就是第 67 章说的那种"值得写"的测试。算钱的地方，错了要命。依赖注入四步记牢：定协议、让 ViewModel 只认协议、生产注真实、测试注假的。做熟之后你会发现，"好架构"和"好测试"是同一件事的两面。

别把依赖注入做成仪式感：只有两三个页面的工具 App，全量注入是负担；先给"值得测试的逻辑"（算钱、校验、状态机）做注入，界面胶水代码直连真实仓库无妨。注入的粒度跟着测试的需要走，不是越细越专业。

##### 一个真实的重构现场

给你还原一次典型翻车，感受这套架构怎么救你。月底对账，发现"本月支出"把上个月最后一晚 23 点的一笔算进了本月。老写法里这逻辑散在视图里，你得开着模拟器手点数据复现；新架构里，照第 67 章的手法先写一个失败测试，造一笔月末 23:59 的账，断言它不算本月，测试红了；然后把日期过滤的边界条件修正，测试绿了。整个过程五分钟，不需要真机，不需要手点。

而且这个测试从此留在项目里：明年跨年那晚，它还在站岗。这就是 MVVM 加协议抽象的真正回报：bug 复现不需要"手气"，一个测试函数就能冻结现场。架构不是仪式，是让"五分钟修完"成为可能的基建。

同一现场还能看出单一职责的价值：如果汇总逻辑当时散在三个视图里（首页、统计页、小组件各算各的），你要修三处还得祈祷没漏——协议抽象让"算汇总"只有一个权威实现，三处都调它。改一处、不牵连三处，第一章 ul 里那句话的分量，这时候才真正掂出来。

##### 状态放哪里：一棵决策树

新手最常问"这个状态该放哪"，给你一棵决策树。先问一问：这个状态只有这一个视图用吗？是，留在视图里用 @State（弹窗开关、输入框草稿）；否，下一问：跨页面共享吗？不跨、只是父子传递，用参数往下传；跨页面甚至跨功能——放进 @Observable 的 ViewModel，需要全局共享的再进 @Environment。最后一问：要不要持久化（重启还在）？要：交给 SwiftData 或 UserDefaults（第 64 章），内存里的 ViewModel 只做"今天的搬运工"。

反过来的信号也要认识：如果你发现两个页面各自维护一份"应该相同"的状态，改一处忘另一处，这就是状态放错位置的报警，合并进 ViewModel 或数据层。状态管理的全部艺术，说白了就是"每份状态只有一个家"。

上架前还有一道容易漏的工序，回到本章开头的清单：核对<strong>隐私清单</strong>（PrivacyInfo.xcprivacy）与 App 实际的采集行为是否一致，接进来的第三方 SDK（比如崩溃统计）也要一并算进去。清单和实物对不上，审核与用户信任都要买单。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：SwiftUI 的"生态红利"

{class="mt-1"}
iOS 生态还有两个"只此一家"的进阶玩法：<strong>小组件（WidgetKit）</strong>让用户不打开 App 就能看信息（记账本的"本月支出"放桌面），<strong>快捷指令（App Intents）</strong>让用户用 Siri 或自动化调用你的功能。两者都有官方框架，入门成本不高，但对用户体验的加成巨大：进阶路上值得优先解锁。
:::

#### 四、2026 年的新玩法：AI 辅助 iOS 开发

2026 年，AI 已经深度嵌入苹果开发流程：Xcode 26 干脆把 AI 助手内置进了 IDE，可以登录 ChatGPT 或 Claude 账号、填 API 密钥，甚至接本地模型，写码、解释报错都不用切窗口。如果你想提速，这套组合拳很成熟：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">环节</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">AI 怎么帮</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">你的职责</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">写代码</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode 内置代码补全 + 第三方 AI 插件生成</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">描述清楚需求，审查产出</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">查资料</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把官方文档和报错信息丢给 AI 解读</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">关键结论回官方文档核实</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">写测试</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">让 AI 按"正常/边界/异常"三类生成 XCTest 用例</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">确认用例符合业务语义</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">改 bug</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">贴崩溃日志 + 相关代码，AI 定位修复</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">看懂改动，跑测试验证</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
AI 辅助 iOS 开发的四个场景

具体方法论——怎么给 AI 下指令、怎么验收、怎么避坑，完整的 11 章内容在本书第七篇《AI编程实战篇》（第37-47章）里，强烈建议配合阅读：<strong>Swift 语法交给本篇，AI 协作的心法交给第七篇</strong>。

两句使用纪律值得写在这里。第一，AI 的产出必须过你自己的眼睛：它会把废弃 API 当新 API 用、把逻辑写得"看起来对"但不合你的业务。每一段贴进项目的代码，你都要能口头讲清它在干什么；讲不清的，追问到讲得清为止，这也是最快的学习路径。第二，上下文给足再提问：完整报错、相关代码、你想要的行为，一次贴全，比挤牙膏式追问省一半时间。

还有一条保险带：让 AI 大改代码之前，先 git commit 一次。改坏了随时回退，你才敢大胆试错。以及别让 AI 替你写"你还没学会的东西"，第 61 章的语法、本章的架构，先自己写过一遍，再让 AI 加速。地基不能外包。

#### 五、Swift 并发要点：@MainActor 与 Task

Swift 6 的并发体系有两条新手必懂的规则：

- <strong>界面只能在主线程更新</strong>：SwiftUI 视图默认是 <code class="inline">@MainActor</code>，网络回调回到主线程再改状态（<code class="inline">await MainActor.run { ... }</code> 或把 ViewModel 标成 @MainActor）。
- <strong>异步任务用 Task 管理</strong>：<code class="inline">.task { }</code> 修饰符随视图出现自动开始、消失自动取消，这是 SwiftUI 里启动异步工作的标准姿势，别在 body 里乱写 Task 裸奔。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 标准异步姿势</span><span class="dots">···</span>
:::

```
struct WeatherScreen: View {
    @State private var vm = WeatherViewModel()

    var body: some View {
        Group {
            switch vm.state {
            case .loading: ProgressView()
            case .success(let d): WeatherContent(data: d)
            case .error(let m): Text(m)
            }
        }
        .task {                       // 出现即开始，消失即取消
            await vm.search(city: "北京")
        }
    }
}
```
:::

这两条规则背后是 Swift 6 的"数据竞争安全"设计，编译器会在你写错时直接报错，而不是等 App 崩了才发现。<strong>编译器的报错不是找茬，是替你挡子弹</strong>。遇到并发报错，正确姿势是优先改数据的归属——把可变状态收进 @MainActor 的 ViewModel，或用 actor 隔离，而不是到处加逃逸口把检查绕开；绕得了一时，数据竞争还在原地等你。

##### Task 与 .task：一对兄弟各管各的

.task 修饰符跟着视图的生命周期走：视图出现自动开始，消失自动取消，适合"进入页面就要拉数据"的场景，上面代码就是这么用的。Task { } 则是你手动点火：按钮点击、下拉刷新这类"用户动作触发"的活儿用它。按钮场景的标准写法：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 按钮触发的异步任务</span><span class="dots">···</span>
:::

```
Button("刷新天气") {
    Task { await vm.search(city: "北京") }
}
```
:::

任务里的等待用 <code class="inline">await Task.sleep(for: .seconds(2))</code>，比老的休眠写法好读。取消也顺理成章：用户退出页面，.task 自动取消；手动启动的 Task 存个句柄，需要时调 cancel()。一条铁律记牢：视图生命周期的活儿用 .task，用户动作的活儿用 Task，body 里到处裸写 Task 的代码，迟早出"页面都关了任务还在跑"的怪事。

再送一个实战细节：网络请求要支持"用户连点不叠加"，第二次点击时先取消第一次的 Task（或用状态标记忽略重复请求），否则快速连点的结果是三个请求竞速，最后一个到的覆盖前面的，界面闪三次。异步的坑大多不在语法，在"任务和界面谁说了算"这件事没想清楚。

##### 三条常见并发报错与对策

报错一，出现 "Main actor-isolated" 字样：你在非主线程的地方碰了界面状态。对策：把 ViewModel 整个标上 @MainActor（class 前面加一行），网络回调改状态的问题一次性消失。这是最常用的一招，先试它。

报错二，提到 Sendable：多个任务之间传递了"可变的东西"。对策：优先传值类型（struct），或把可变状态收进单一的 @MainActor ViewModel——别到处写 unchecked 绕过检查，编译器让步了，竞争不会让步。

报错三，completion handler 回调里改 @State 不生效或报错：把网络层换成 async/await 写法（URLSession 有现成的 async 接口），await 会自动帮你回到正确的上下文。老代码里那些"回调套回调"的金字塔，换成 async/await 之后大多直接抚平。

学习顺序给个建议：先把"两条规则 + 三条对策"用熟（够覆盖小项目的九成场景），再接触 actor、异步序列这些进阶概念。并发不是一口气学完的科目，是用到哪学到哪的地图，带着报错学，最快。

#### 六、小组件入门：把"本月支出"放上桌面

上面信息盒里预告过的第一个"生态红利"，现在动手解锁。小组件（Widget）让用户在桌面上就能看到你 App 的关键信息，不打开 App， glance 一眼。先建立正确的预期：它在系统里是和主 App 分开运行的"扩展"（extension），独立的小进程，有自己的生命周期，内存和时间预算都比主 App 紧。这个定位决定了它的两个特点：界面要克制（一两个数字讲一件事最合适），数据要"自带"（它读不到主 App 内存里的东西，靠共享存储交接）。

##### 五步加一个"本月支出"小组件

第一步，加 target：File → New → Target → Widget Extension，起名（比如 MonthExpenseWidget），Xcode 自动生成一套模板代码并弹窗询问配置——先一路默认，模板能直接跑。第二步，认三件套：模板里你会看到 TimelineEntry（一条时间线数据：哪个时刻显示什么）、TimelineProvider（按时生成数据的供给者）、Widget 视图（把一条 Entry 画出来）。小组件的更新机制就是"时间线"，你把未来一段时间的数据交给系统，系统按时换着显示。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 小组件的三件套（精简版）</span><span class="dots">···</span>
:::

```
struct MonthExpenseEntry: TimelineEntry {
    let date: Date
    let total: Double
}

struct MonthExpenseProvider: TimelineProvider {
    func placeholder(in context: Context) -> MonthExpenseEntry {
        .init(date: .now, total: 0)
    }
    func getSnapshot(in context: Context,
                     completion: @escaping (MonthExpenseEntry) -&gt; Void) {
        completion(.init(date: .now, total: readTotal()))
    }
    func getTimeline(in context: Context,
                     completion: @escaping (Timeline&lt;MonthExpenseEntry&gt;) -&gt; Void) {
        let entry = MonthExpenseEntry(date: .now, total: readTotal())
        completion(Timeline(entries: [entry], policy: .atEnd))
    }
}
```
:::

第三步，解决数据来源：小组件进程和主 App 之间用 App Group 共享数据，在两个 target 的 Signing &amp; Capabilities 里开启同一个 App Group，然后主 App 每次记账时把"本月支出"写进共享存储（用 suiteName 初始化 App Group 的 UserDefaults，第 64 章的老朋友换了个名字），小组件端的 readTotal() 从同一处读。这一步是小部件翻车率最高的地方：两个 target 的 Group 名字必须一字不差。

第四步，画界面：视图就是普通 SwiftUI，"本月支出"一行小标题加一行金额，小尺寸下两行足矣；中、大尺寸可以加本周走势、最近三笔。第五步，预览与上桌面：Canvas 里能预览三种尺寸；真机上长按桌面空白处 → 左上角加号 → 搜你的 App → 选尺寸添加。给小组件挂 <code class="inline">.widgetURL</code> 可以让点击跳回 App 的指定页面（自定义 URL scheme，主 App 里注册一下）。

##### 刷新的真相：预算与承诺

"小组件多久更新一次"是新手最常失望的地方：答案不是"随你"，系统对每个小组件的刷新有自己的预算和调度，你只能通过时间线的刷新策略提出请求（.atEnd 表示"时间线用完了再要"、.after(date) 表示"指定时刻再来"），系统酌情满足。所以小组件适合展示"几分钟到几小时内不较真"的信息：本月支出、下周天气；别指望它当秒表。

实践建议两条：主 App 在关键数据变化后（记完一笔账）主动请求刷新一次时间线，其余交给系统调度；真机的刷新节奏和模拟器不一样，最终以真机为准。对用户的管理预期也重要，在 App 里别承诺"实时"，承诺"及时"。

##### 动手前的三个问题

写代码之前，先回答三个问题，答案决定小组件的形状：这个小组件最想回答用户什么问题？（"这个月花了多少"：一个问题，别贪多。）用户看完会不会想点进去？（会 → widgetURL 指到月度统计页。）数据从哪来、多久变一次？（App Group 共享 + 记账后刷新。）三个问题都有答案再动手，能省一半返工。

常见的坑也提前排一下：小组件里跑不了网络请求的重活（时间预算内完不成），数据一律靠共享存储预置；小组件的内存预算小，界面别塞大图；调试时改了共享数据但小组件没变——先手动刷新时间线，或重新添加小组件，别急着怀疑人生。

#### 七、App Intents 入门：让 Siri 和快捷指令认识你的 App

小组件解决"看"，App Intents 解决"做"：把 App 的功能注册给系统，用户就能用 Siri 语音、快捷指令 App、甚至自动化规则（到家自动、充电时自动）来调用你的功能。它不是一个新界面。它是一份"功能清单 + 执行入口"，你的 App 从此变成系统里可被调用的"动词"。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 快速记一笔 Intent</span><span class="dots">···</span>
:::

```
import AppIntents

struct QuickRecordIntent: AppIntent {
    static var title: LocalizedStringResource = "快速记一笔"
    static var description = IntentDescription("不打开 App，直接记一笔支出")

    @Parameter(title: "金额")
    var amount: Double

    func perform() async throws -&gt; some IntentResult &amp; ProvidesDialog {
        RecordStore.shared.add(Record(amount: amount, type: .expense))
        return .result(dialog: "记好了，\(amount) 元")
    }
}

struct MyFirstAppShortcuts: AppShortcutsProvider {
    static var appShortcuts: [AppShortcut] {
        AppShortcut(intent: QuickRecordIntent(),
                    phrases: ["用\(.applicationName)记一笔"])
    }
}
```
:::

看懂三个要点就够了：@Parameter 声明参数：用户说"记一笔"没带金额时，Siri 会自己追问"记多少"；perform() 里做实事并返回一句话反馈（dialog 会念出来或显示出来）；phrases 里的 \(.applicationName) 会替换成你的 App 名，不用写死。跑起来验证也简单：编译安装后，打开快捷指令 App 能搜到这个动作；长按侧键喊 Siri"用记账本记一笔"试试。调试期用快捷指令 App 里直接点跑，反馈最快。

##### 设计 Intent 的三条经验

经验一，每个 Intent 做一件事、做快一点：perform 里别放网络大请求和重计算，反馈尽量即时——用户喊了 Siri 是在等一个"秒回"。经验二，反馈文案是人话："记好了，25 元"好过"操作成功"；失败也要说话："没记上，App 好像没准备好"。经验三，别贪多：初期注册两三个最核心的动作（记一笔、看本月汇总），用户用得起来才有价值；功能清单式的二十个 Intent 不会有人用，反而稀释存在感。

两个合体玩法留着进阶：小组件上的按钮、开关也可以由 Intent 驱动（系统较新的版本支持），比如桌面小组件上放个"记 25 元"按钮，点了直接写数据不打开 App；专注模式与自动化的规则里也能排进你的 Intent。App Intents 是"入口"的基础设施：入口越多，早期把路由和执行逻辑收进协议抽象的回报越大。

#### 八、FAQ：权限、通知与架构的七个真问题

<strong>问：权限弹窗一次都没弹出来，为什么？</strong>

答：按顺序查三件事——Info.plist 里对应的用途描述键加了吗？没加，申请时代码直接崩溃，弹窗都来不及弹；这个权限之前被明确拒绝过吗？拒绝了就不再弹，去设置页检查；申请代码真的执行到了吗？打个断点看看。三条里第一条占大头。

<strong>问：用户说"我明明允许了，怎么还是不行"？</strong>

答：先确认他允许的是哪一项。设置里每个 App 的权限页是一列开关，容易看串行；然后检查代码是否在"用到时"实时查询授权状态，而不是信任启动时的缓存；定位类再注意"仅本次允许"，下次启动状态就变回未询问，这是正常行为不是 bug。

<strong>问：通知授权同意了，用户还是说收不到？</strong>

答：逐项排查：专注模式开着吗；"定时推送摘要"开着吗，通知到了但被系统攒着；App 通知设置里横幅、声音、锁屏子项被单独关过吗；如果是日历通知，时间是不是已经过了，"每天 20:00"的通知 21 点才安排进去，第一条要等第二天 20:00。完整排查路径在第二节正文里。

<strong>问：@Observable 和 ObservableObject 能混用吗？</strong>

答：能。两者是并存关系不是替换关系，第三方库还是老写法就继续用，自己新写的类用新写法。同一个视图里观察两个不同范式的对象，没问题。

<strong>问：小项目有必要上 MVVM 吗？</strong>

答：看复杂度，不看教条。两三个页面的工具 App，直接在视图里用 @Observable 的状态类也完全健康；一旦出现"逻辑想测试""页面间共享状态""一个功能牵三处"三类信号中的任何一条，就把 ViewModel 抽出来。架构是问题逼出来的，不是提前穿的正装。

<strong>问：小组件为什么总是显示旧数据？</strong>

答：它是独立进程加系统调度刷新，不是实时窗口。检查三处。主 App 数据变化后有没有主动请求刷新时间线；App Group 的数据是不是真的写进去了（两个 target 的 Group 名字必须一字不差）；对刷新频率的期待是否超出了系统预算。多数"不刷新"是第二条，Group 没配对。

<strong>问：远程推送一定要自建服务器吗？</strong>

答：要有"能向 APNs 发请求的后端"，但不必是自己写的，第三方推送服务、云函数都能承担这个角色。真正绕不开的是推送配置（密钥、能力开关）和"什么时候推、推给谁"的产品决策。没有后端的个人项目，先把本地通知的价值做足，推送不急。

#### 九、误区清单：五个"以为"与真相

- <strong>以为"申请一次，永久有效"</strong>。权限状态是动态的：用户随时去设置里改，定位还有"仅本次允许"这种自清空选项。每次用到都查，别缓存"上次的答案"。
- <strong>以为"通知开关开着 = 一定送达"</strong>。专注模式、定时摘要、按类型关闭，都能让通知安静消失。送达率不是你能保证的，所以通知文案要"单条即完整信息"。
- <strong>以为"界面不刷新就得手动通知"</strong>。那是 ObservableObject 时代的思路。@Observable 下属性变化自动追踪，界面没刷新，先查"这个属性是不是没被视图依赖"，而不是上手动刷新。
- <strong>以为"架构越重越专业"</strong>。VIPER、Clean Architecture 解决的是大团队大项目的协作问题，单人小项目硬上只会加文件不加质量。协议抽象 + 单一职责，就是这一章给你的全部起步装备。
- <strong>以为"小组件是个小号 App"</strong>。它是受限的扩展：内存预算小、刷新受调度、数据要共享。按"一两个数字讲清一件事"来设计，超出这个范围的野心都该还给主 App。

#### 十、给三类读者的进阶建议

<strong>学生党</strong>：这一章的三件套（通知、小组件、快捷指令）是作品集里最"值钱"的亮点——面试官看到桌面上的小组件和语音唤起的快捷指令，比看到又一个列表页印象深得多。苹果每年有面向学生的 Swift 挑战赛（时间以官网为准），练手项目顺手打磨就能投。AI 辅助写码时坚持"能讲清每一行"的底线——面试官追问一句你就露馅的那种学习，别让它发生。

<strong>上班族</strong>：时间碎，就按"可见度优先"排期——通知提醒和小组件这两个功能，让 App 从"想起来才开"变成"每天主动出现三次"，是单人开发者性价比最高的增长手段。架构只做到协议抽象一层就停，别为想象中的团队规模预付复杂度。周五晚提交前跑一遍第 67 章的测试再 Archive，把周一的惊喜留成好的那种。

<strong>想拉爸妈一起用的</strong>：这章的每个功能都是适老化练兵场——通知文案写全（"该记今天的账啦，点这里 10 秒记一笔"），权限弹窗前先用大字界面解释，权限被拒后的降级要一步可走（长辈不会去设置里翻开关，你直接给手输城市的选择）。小组件是他们最容易感知的功能：桌面大字"本月支出"，比让他们打开 App 找菜单强十倍。第 27 章的适老化原则在这里全能用上。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：给记账本加"三件套"

{class="mt-1"}
① 给记账本加"每天 20:00 记账提醒"（通知权限 + 本地通知）；② 把 ViewModel 的数据源改成协议抽象，并写一个注入假数据的单元测试；③ 加一个"本月支出"桌面小组件。三件套做完，你的项目就有"正规军"的样子了。
:::

#### 十一、Purpose Strings：让权限弹窗替你说话

权限申请在 iOS 上有个安卓开发者容易忽略的细节：弹窗文案是<strong>你写的</strong>。Info.plist 里的用途描述（Purpose Strings，如 NSCameraUsageDescription、NSLocationWhenInUseUsageDescription）就是系统弹窗里"XX 想访问你的相机"下面那句话。它写得好不好。直接决定用户点"允许"还是"不允许"：以及审核会不会拒你。

写文案的三条标准：说清楚"为什么要"（"拍摄照片用于上传头像"），而不是"这个 App 需要相机权限"这种空话；说清楚"用来做什么"（"仅在使用扫描功能时使用相机"），把场景说死；不要出现"为了给您提供更好的服务"——这是审核明确不喜欢的套话，苹果审核员见过太多这种敷衍文案。一个反面教材：某个手电筒 App 申请定位。文案只写"需要获取您的位置"：被拒的同时还被用户截图挂上了社交媒体。定位权限尤其敏感，"仅使用期间"和"始终"的文案要分开写，后者还要准备好审核质询时解释业务必要性。

文案还和第六节讲的权限降级策略联动：用户拒绝后你引导去设置页时，那句话最好复用 Purpose Strings 的口径——用户在弹窗和设置里看到同样的解释，信任感才连贯。改文案不用重新申请权限，但改了要重新打包上架——所以发布前把所有用途描述通读一遍，是上架检查清单里该有的一项。

#### 十二、通知权限的细节：临时授权与时间敏感

通知权限在 iOS 上比"允许/拒绝"精细得多，用好这几个档位，是.notification 权限体验的分水岭。<strong>临时授权（Provisional）</strong>：申请时用户不弹窗、通知静默投递到通知中心但无横幅无声音——适合"先给用户看价值再要正式权限"的产品，比如记账 App 先静默推送每日总结，用户觉得有用再引导升级为正式授权；缺点是用户几乎意识不到"这些通知是'临时工'"，要靠产品文案点明。<strong>时间敏感通知</strong>：需要单独的 entitlement，突破专注模式的拦截把提醒送进用户视野，外卖到达、日程提醒这类"错过有损失"的通知才配用，滥用它（营销推送也标时间敏感）会被用户一怒之下全禁。

实操上要记住组合拳：请求授权时用 <code>requestAuthorization(options:)</code> 把想要的档位一次说清（alert + sound + badge 还是 provisional），根据返回的设置状态（.authorized / .denied / .provisional）走不同的引导文案；跳系统设置页的"去开启"引导只在用户刚体验过通知价值之后出现：上来就引导去设置，转化率和用户好感都是负的。

#### 十三、@AppStorage 与 UserDefaults：轻量偏好的边界

SwiftUI 时代，<code>@AppStorage("key")</code> 把 UserDefaults 包装成了一个属性包装器：一行声明，读写自动同步 UI。它适合存什么，开关状态、上次选择的排序方式、首次启动标记、用户改过的主题色。它不适合存什么，任何"丢了会疼"的数据（用户数据进 DataStore/SwiftData/数据库，见第 65 章的持久化矩阵）、大体积 JSON（UserDefaults 每次读写都是整取整存）、以及需要跨进程强一致的计数器。

一个 2026 年开发者常撞上的边界是 <strong>App Group</strong>：小组件（第三十三节）运行在独立进程里，主 App 和它共享偏好必须用 <code>UserDefaults(suiteName: "group.xxx")</code>，而不是默认的 UserDefaults：否则你在主 App 里改了设置，桌面小组件永远显示旧值。新手第一次做小组件几乎都会踩这个坑：代码没错、模拟器里也正常，真机上就是不刷新。排查口诀："跨进程的偏好，先查 suiteName"。

和安卓对照记忆：UserDefaults ≈ SharedPreferences，@AppStorage ≈ DataStore 的 UI 绑定层，App Group ≈ Android 的多进程共享（但 iOS 的机制更简单：没有 ContentProvider 那一层）。学过第 51-52 章再回来看这张对照表，你会发现三平台的"轻量存储"思路殊途同归。

#### 十四、进阶改造清单：把你的练手项目升级一遍

本章讲了权限、通知、架构、小组件、App Intents 五个进阶话题。知识落地的最好方式是给已有的练手项目做一轮"进阶改造"，任务清单如下，每项对应一节，做完一轮，这一章就算真正变成你的了：

1. 把所有权限申请换到 Activity Result API 风格的注册回调（对应第 52 章第三十八节与本章第六节），并给每个权限写一条说人话的 Purpose String。
2. 给 App 的核心通知分类：哪条走横幅、哪条降级为临时授权、哪条申请时间敏感——写出一张三列表再动手。
3. 把三处"写死在 View 里的状态"搬到 ViewModel，验证旋转/切换深色模式后界面状态不丢。
4. 做一个最小小组件：展示 App 里的一条核心数据，注意用 App Group 的 suiteName 共享。
5. 给主流程加一个 App Intent：让用户能对 Siri 说一句话完成你最常用的那个操作，并在快捷指令 App 里试一次自动化触发。
6. 开着"预测性返回"真机走一遍主流程，把所有重写 onBackPressed 式的旧逻辑（如果有）迁移到 Dispatcher 风格的回调。

这六项做完，你的练手项目就从"能跑的 demo"变成了"经得起真机折腾的小产品"。它们也是面试时最能讲出细节的部分——面试官问"权限被拒了怎么办"，你能从 Purpose Strings 一路讲到设置页引导和降级体验，这比背概念高一整个档次。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：今天的三十分钟

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 打开你的练手项目，检查 Info.plist 里每个用途描述：能否一句话回答"为什么要"？
2. 在真机上分别授权、拒绝、跳过三种状态，确认每种状态下的界面文案都合理。
3. 把一个设置项迁到 @AppStorage，体验"一行代码 UI 自动更新"的爽感。
4. 试着在快捷指令 App 里给你的 App 建一个自动化（如"到家时打开 XX"），跑通一次。
:::

#### 十五、本地网络权限：IoT 类 App 的隐形门槛

做智能家居、局域网投屏、打印机类 App 的开发者，还会撞上 iOS 特有的"本地网络权限"（Local Network Privacy）：App 第一次访问家里局域网中的其他设备（扫描设备、连接电视、控制灯泡）时，系统会弹一个独立的授权框。它和相机麦克风权限是分开的，而且一旦用户点了"不允许"，设置里藏得很深（设置 → App → 本地网络），很多用户找不到回来的路。

对策三条：Info.plist 里配好对应的用途描述（NSLocalNetworkUsageDescription 和 Bonjour 服务声明），文案把"要连什么设备、干什么"写明白；把授权引导做成 App 内的一页图文（配设置页路径截图），在第一次真正需要连设备时再请求。而不是启动就弹；降级路径要留——权限被拒时用蓝牙通道或云端中转兜底的方案，至少在 UI 上说清"为什么现在扫描不到设备"。

#### 十六、把权限体验当成产品功能来设计

这一章从权限、通知讲到本地网络，背后其实是同一条产品哲学：<strong>权限不是技术问题，是信任问题</strong>。用户每一次点"允许"，都是在给你的 App 记一笔信任存折；每一次"不该要也要"，都是一次透支。

把原则压缩成三条验收线。第一，每个权限都有一句用户能听懂的"为什么"（Purpose Strings + App 内引导文案一致）；第二，每个权限都有被拒后的降级体验（用户拒绝后 App 依然能完成主流程，而不是白屏或反复弹窗）；第三，每个权限都有"价值先行"的节奏（用户先体验到功能价值，再看到授权请求：顺序反了，信任就先碎了）。这三条线对照你的项目走一遍，权限相关的差评会少一大半。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>本章小结之外的一句话

{class="mt-1"}
架构决定你三个月后还能不能维护，权限体验决定用户三分钟后还信不信你。两件事都不在"功能清单"里，但都写进了留存率。
:::

下一步，就把这份清单排进你的日历，从第一项开始。

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 权限三步：Info.plist 声明（漏了必崩）、用时申请、被拒引导去设置
- iOS 权限弹窗只弹一次：时机选在"正要用的那一刻"，文案写清用途
- 通知三纪律：只发有用的、能关、不骚扰；UserNotifications 框架
- MVVM 进阶：协议抽象（可测试）、单一职责、不过度设计
- 生态红利：WidgetKit 小组件 + App Intents 快捷指令
- AI 辅助四场景：写码、查资料、写测试、改 bug；方法论见第七篇（第37-47章）
- 单向数据流 + 隐私清单：界面只读状态只发事件；清单要与实际采集（含第三方 SDK）对得上
:::
