---
id: di-qi-shi-qi-zhang
num: 77
nav: 第七十七章：实战项目二——天气助手
toc: default
kind: chapter
after_part: hongmeng-kai-fa-pian
---

### 第七十七章：实战项目二——天气助手应用

{class="chapter-intro mb-4"}
待办清单练的是"本地数据"，这一章的项目练"网络 + 状态管理 + UI 组合"：做一个天气助手，输入城市、请求天气 API、展示当前与预报。它对应安卓篇的天气查询与 iOS 篇的第二个项目——<strong>"网络应用"是移动开发中最常见的一类</strong>，套路学会了就能举一反三。

天气应用是网络教学的"完美教具"，因为它恰好覆盖网络开发的三段式：发起请求（怎么构造与发送）、处理响应（怎么解析 JSON）、管理状态（加载中/成功/失败三态怎么呈现）。这三段式学会后，任何"调接口展示数据"的应用——新闻、股票、外卖——都是同一个套路的换皮。所以这一章的重点不是天气，是"网络应用的标准姿势"。

#### 一、设计：三层拆分

先做设计决策（好习惯从第一个项目就养成）：<strong>数据层</strong>——HTTP 客户端封装成 WeatherService 类；<strong>状态层</strong>——页面用 @State 管理 loading/data/error 三态；<strong>界面层</strong>——按三态分别渲染（加载动画 / 数据卡片 / 错误提示）。

::: div .code-block
:::inline div .code-head
<span>ARKTS · service/WeatherService.ets</span><span class="dots">···</span>
:::

```
import { http } from '@kit.NetworkKit'

export interface Weather {
  city: string
  temp: number
  text: string        // 天气现象：晴/多云/小雨
}

export class WeatherService {
  async fetch(city: string): Promise&lt;Weather&gt; {
    let req = http.createHttp()
    try {
      let resp = await req.request(
        'https://api.example.com/weather?city=' + encodeURIComponent(city),
        { method: http.RequestMethod.GET,
          header: { 'Content-Type': 'application/json' },
          expectDataType: http.HttpDataType.STRING })
      let data = JSON.parse(resp.result as string)
      return { city: data.city, temp: data.temp, text: data.text }
    } finally {
      req.destroy()
    }
```
:::

三层拆分的设计意图再强调一遍：WeatherService 不知道"谁在调用它"，UI 不知道"数据从哪来"。这样分层后，换 API 提供商只改 Service，换界面风格只改 UI 层——第 37 章的"封装变化点"原则，在网络应用里的具体落点就是 Service 层。三态管理（loading/data/error）则是网络 UI 的"万能模板"：任何接口调用都会经历这三态，把三态的渲染写成条件分支，错误处理就有了固定的家。

代码里有个容易忽略的细节：finally 里的 req.destroy()。HTTP 请求对象用完必须销毁，否则高频调用（比如用户连续搜索城市）会累积连接资源。这和第 74 章讲的"该释放的资源要释放"是同一类纪律。

#### 二、界面层：三态渲染与数据展示

界面层用 @State 管理 loading/data/error 三个变量，build() 里按状态分支渲染。数据卡片的元素规划：城市名、当前温度（大字号）、天气现象文字、以及一个"换城市"的入口。设计上的小技巧是"数据未到时不留白"——loading 态给一个进度条加提示文字，让用户知道"在做了"，而不是盯着白屏怀疑应用死了。

错误态的展示也有讲究：不要只显示"出错了"，要告诉用户"下一步做什么"——"网络异常，请检查网络后点击重试"配上一个重试按钮。第 19 章的排障思路在 UI 层的落地就是这个：错误信息要包含"发生了什么"和"能做什么"两段。

#### 三、真实 API 与数据解析的进阶

书里用 api.example.com 做演示占位。实际开发请选择真实可用的天气 API（国内常用的有和风天气、心知天气等，它们提供免费额度的开发者套餐；国际项目可用 OpenWeatherMap）。接入真实 API 时，重点工作变成"读懂返回的 JSON"：真实 API 的响应结构通常比示例复杂得多——嵌套对象、数组、状态码字段都需要正确解析。第 72 章的 interface 定义在这里发挥作用：先照着 API 文档定义响应接口，再用 JSON.parse 之后按接口取值。

JSON 解析的常见报错有两类：字段名对不上（返回 snake_case、你的接口是 camelCase——用映射解决）、类型不匹配（温度返回的是字符串"25"而非数字 25）。防御式解析的做法是"对每个字段做类型守卫"，宁可显示"数据异常"也不要让应用崩溃。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：完成天气助手

{class="mt-1"}
1\. 注册一个真实天气 API 的免费开发者账号，替换示例 URL；2. 按 API 文档定义响应 interface 并解析；3. 实现输入城市 → 点击查询 → 三态渲染的完整闭环；4. 加上"上次查询城市"的本地记忆（第 75 章的 Preferences）。
:::

#### 四、预报数据：未来 7 天列表的解析与横向滚动展示

只有"当前温度"的天气应用，本质是个联网的电子温度计。用户真正想知道的是"明早出门要不要带伞""周末降温降多少"。这一节把数据从一条升级成一组：请求未来 7 天的预报，解析成数组，再用一行可以左右滑动的卡片展示出来。你会在这里第一次正式处理"数组型 JSON"——它比单对象多两类麻烦：长度不确定、单个元素可能缺字段。

##### 先看数据长什么样

预报接口的返回通常是一根"数组脊柱"：外层对象带城市、更新时间这类元信息，核心是一个每天占一条的数组。字段名各家服务商不一样，下面是本书自造的示意结构，接真实 API 时照着它的文档把字段名换成真的：

::: div .code-block
:::inline div .code-head
<span>JSON · 预报接口示意返回（字段名以服务商文档为准）</span><span class="dots">···</span>
:::

```
{
  "city": "北京",
  "updateTime": "2026-11-13 08:00",
  "daily": [
    { "date": "2026-11-13", "textDay": "晴",   "tempMax": 14, "tempMin": 3 },
    { "date": "2026-11-14", "textDay": "多云", "tempMax": 12, "tempMin": 2 },
    { "date": "2026-11-15", "textDay": "小雨", "tempMax": 9,  "tempMin": 1 }
    // ……后面还有几天，实际长度以接口返回为准
  ]
}
```
:::

解析思路和第三节一致，但要多立两条纪律。一是<strong>数组元素逐条校验</strong>：整条数据合法才收进来，某一天缺了最低温度就跳过那一天，而不是让一次解析异常把整个列表渲染掀翻。二是<strong>长度不假设</strong>：别把"7 天"写死，不少服务商的免费套餐只给 3 天或 5 天预报，你的界面要来几天显示几天。写死数字这种事，上线后第一个帮你想起来的是用户评分区。

::: div .code-block
:::inline div .code-head
<span>ARKTS · service/WeatherService.ets（追加预报接口）</span><span class="dots">···</span>
:::

```
export interface DailyItem {
  date: string        // 形如 2026-11-13，具体格式看服务商文档
  textDay: string     // 白天天气现象
  tempMax: number
  tempMin: number
}

export interface Forecast {
  city: string
  days: DailyItem[]
}

async fetchForecast(city: string): Promise&lt;Forecast&gt; {
  let req = http.createHttp()
  try {
    let resp = await req.request(
      'https://api.example.com/forecast?city=' + encodeURIComponent(city) + '&amp;days=7',
      { method: http.RequestMethod.GET,
        connectTimeout: 10000, readTimeout: 10000,
        expectDataType: http.HttpDataType.STRING })
    let raw = JSON.parse(resp.result as string)
    let list: DailyItem[] = []
    if (Array.isArray(raw.daily)) {
      for (let d of raw.daily) {
        // 逐条校验：缺关键字段的那天直接跳过
        if (typeof d.date === 'string' &amp;&amp;
            typeof d.tempMax === 'number' &amp;&amp;
            typeof d.tempMin === 'number') {
          list.push({ date: d.date,
            textDay: typeof d.textDay === 'string' ? d.textDay : '未知',
            tempMax: d.tempMax, tempMin: d.tempMin })
        }
      }
    }
    return { city: typeof raw.city === 'string' ? raw.city : '', days: list }
  } finally {
    req.destroy()
  }
}
```
:::

三个防御点值得逐行看：typeof 校验挡住了"温度给的是字符串"的服务商；textDay 缺失时兜一个"未知"，而不是让 undefined 直接渲染成界面上的空白；finally 里照旧 destroy。你可能觉得逐条校验太啰嗦——等你哪天碰上服务商悄悄改版、中午开始有一批数据缺字段、用户群里炸锅的时候，会回头感谢这些啰嗦的。防御式解析不是多此一举，是给"接口会变"这件事提前买保险。

##### 日期字段是个小坑

接口给的日期多半是"2026-11-13"这种字符串，原样摆上界面没人想看，你要把它翻译成"今天""周五"。翻译本身不难，难的是想到两个边角：解析失败怎么办——返回空串，别让界面上出现"NaN"；第一天要不要标"今天"——要标，用户扫一眼就知道列表的起点在哪，不用自己心算今天几号。

::: div .code-block
:::inline div .code-head
<span>ARKTS · utils/DateUtil.ets</span><span class="dots">···</span>
:::

```
const WEEK: string[] = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']

// dateStr 是接口给的日期，todayStr 是本地算出的今天（同格式）
export function weekdayLabel(dateStr: string, todayStr: string): string {
  let d = new Date(dateStr)
  if (isNaN(d.getTime())) { return '' }   // 解析失败给空串，别显示 NaN
  if (dateStr === todayStr) { return '今天' }
  return WEEK[d.getDay()]
}
```
:::

为什么要单独抽一个工具函数而不是写在页面里？因为下一节的逐小时预报、第八节的温度曲线都要用日期翻译，写在页面里迟早被复制三遍。第 37 章说的"变化点封装"，在项目里最常见的形态就是这种小工具函数——它不高级，但每一次复用都在给你省将来的调试时间。

##### 横向滚动的预报条

界面这边用 Scroll 套 Row 的组合：Scroll 负责横向滑动，Row 把每天排成一列小卡片。为什么不直接用 List？List 的强项是长列表复用，七八个元素的小横条用 Scroll 更轻；等以后做逐小时预报、一屏几十条的时候，再换成 List 也不迟。工具没有高下，只有合不合适。

::: div .code-block
:::inline div .code-head
<span>ARKTS · WeatherPage.ets（预报条，接在数据态分支里）</span><span class="dots">···</span>
:::

```
@State forecast: Forecast | null = null

Column({ space: 4 }) {
  Text('未来 7 天').fontSize(14).fontColor('#888888')
  Scroll() {
    Row({ space: 12 }) {
      ForEach(this.forecast!.days, (d: DailyItem) =&gt; {
        Column({ space: 6 }) {
          Text(weekdayLabel(d.date, this.todayStr)).fontSize(13)
          Text(d.textDay).fontSize(12).fontColor('#888888')
          Text(d.tempMin + '° ~ ' + d.tempMax + '°').fontSize(14)
        }
        .padding(10).borderRadius(12)
        .backgroundColor('#F2F3F5')
      }, (d: DailyItem) =&gt; d.date)   // 键值用日期，别用下标
    }.padding({ left: 12, right: 12 })
  }
  .scrollable(ScrollDirection.Horizontal)
  .edgeEffect(EdgeEffect.Spring)
}
```
:::

ForEach 的第二个参数是键值生成函数，这里用日期字符串当键。新手爱用数组下标当键，平时看不出问题，等你做了"删掉一项后刷新列表"，就会见到数据错位、图标串行的灵异现象——第六节的多城市管理会再撞上这个坑一次，习惯现在就养对：键值要用数据自己的身份，不用位置。

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>避坑提醒

{class="mt-1"}
预报列表最隐蔽的 bug 是"长度写死"：有人写完 7 个 Text 的硬编码版本，开发时接口刚好回 7 天，一切正常；上线后某天服务商调整了免费额度只回 3 天，界面下半截挂着三个空白格子。判定标准很简单——凡是跟着接口数据走的数量，都必须来自 ForEach 循环，不能来自你手写的份数。
:::

#### 五、定位与自动天气：位置权限、反查城市、下拉刷新

打开天气应用还要手动输城市，体验就先输了一半——"原生感"的一大半来自"打开就是本地天气"。这一节做三件事：申请位置权限、把经纬度换成城市、给页面接上下拉刷新。权限是这一节的主角，因为它是你第一次碰到"用户可以对你说不"的能力。

##### 权限三步走

位置是敏感权限，完整流程分三步：静态声明、运行时请求、拒绝兜底。静态声明写在 module.json5 的 requestPermissions 里，其中 reason 字段必须写人话——这段话会展示在系统的授权弹窗里，写"获取定位"等于没写，写"用于自动显示你所在城市的天气"用户才明白为什么要给。

::: div .code-block
:::inline div .code-head
<span>JSON5 · module.json5（权限声明节选）</span><span class="dots">···</span>
:::

```
"requestPermissions": [
  {
    "name": "ohos.permission.LOCATION",
    "reason": "$string:location_reason",
    "usedScene": { "abilities": ["WeatherAbility"], "when": "inuse" }
  },
  {
    "name": "ohos.permission.APPROXIMATE_LOCATION",
    "reason": "$string:location_reason",
    "usedScene": { "abilities": ["WeatherAbility"], "when": "inuse" }
  }
]

// string.json 里对应写：
// "location_reason": "用于自动显示你所在城市的天气"
```
:::

第二步是运行时请求。静态声明只是"报了名"，真正的授权发生在第一次调用时弹出的系统对话框里。用 requestPermissionsFromUser 发起，拿到结果后分道走：给了授权就去定位，被拒绝了就回退默认城市。

::: div .code-block
:::inline div .code-head
<span>ARKTS · WeatherPage.ets（定位入口）</span><span class="dots">···</span>
:::

```
import { geoLocationManager } from '@kit.LocationKit'
import { abilityAccessCtrl } from '@kit.AbilityKit'

async locateAndLoad() {
  try {
    let mgr = abilityAccessCtrl.createAtManager()
    let result = await mgr.requestPermissionsFromUser(this.context,
      ['ohos.permission.LOCATION', 'ohos.permission.APPROXIMATE_LOCATION'])
    let granted = result.authResults.every((r: number) =&gt; r === 0)
    // 授权判定细节以官方文档为准
    if (!granted) {
      this.city = '北京'   // 回退默认城市，别让页面卡在空白
      this.hint = '未开启定位，先显示默认城市，可在系统设置里打开'
      return this.load()
    }
    let loc = geoLocationManager.getCurrentLocation()
    this.city = await this.svc.cityFromLocation(loc.latitude, loc.longitude)
    this.load()
  } catch (e) {
    this.hint = '定位失败，可以手动输入城市查询'
    this.load()
  }
}
```
:::

这段代码比"拿到定位就查天气"多出来的全是兜底：授权被拒，回退默认城市并在页面留一句提示，不白屏、不反复弹窗；定位失败（在室内、电梯里信号差很常见），给出"手动输入"的出路；两条失败路径最后都调用 load()，保证界面永远有东西可看。第三步就是这些兜底本身——写权限代码之前，先想好"用户说不"之后你的界面长什么样，这一步想清楚了，权限就是普通功能；想不清楚，权限就是事故源。

##### 经纬度换城市：两条路

定位拿到的是一对经纬度数字，而天气接口多半认城市名或城市 ID。衔接有两条路，优先走第一条：<strong>直接用服务商的"按坐标查询"</strong>——主流天气 API 基本都支持传经纬度拿天气，一步到位，连换算都省了。第二条路是逆地理编码：把坐标翻译成"北京市海淀区"这样的地址描述，再从中截出城市名去查天气，位置服务一般自带这类接口（方法名以官方文档为准）。逆地理编码多一次请求、多一层解析，能走第一条就别绕第二条——除非你的服务商只认城市名。

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>避坑提醒

{class="mt-1"}
两条提醒。其一，模拟器里的定位是"假位置"——你可以在模拟器的位置设置里手动选一个点，但最终验证一定要上真机，站在小区楼下跑一次，看看拿到的城市对不对。其二，天气应用用<strong>单次定位就够了</strong>，别开持续位置监听：天气不会因为你走了两条街就变，持续监听是导航类应用的事，用在这里只多耗电不多准确（第十节细说）。
:::

##### 下拉刷新：Refresh 一包就行

别自己写手势判断。ArkUI 有现成的 Refresh 组件，把页面内容包进去，下拉时触发回调，转圈动画、回弹都是它管：

::: div .code-block
:::inline div .code-head
<span>ARKTS · WeatherPage.ets（下拉刷新）</span><span class="dots">···</span>
:::

```
@State refreshing: boolean = false

Refresh({ refreshing: this.refreshing }) {
  Column() {
    // ……原来的三态内容原样放进来
  }
  .width('100%')
}
.onRefreshing(() =&gt; {
  if (this.loading) {           // 上一次请求还没回来就别发了
    this.refreshing = false
    return
  }
  this.load().finally(() =&gt; { this.refreshing = false })
})
```
:::

两个细节决定这东西好不好用。一是刷新回调里也要走 loading 守卫——用户下拉时可能上一次请求还在路上，放任不管就是重复请求（第九节门诊会专门治它）。二是刷新完成后记得把 refreshing 置回 false，否则那个圈会停在顶部收不回去，表现特别迷惑人：数据其实已经更新了，就剩个圈挂在那，用户以为一直没刷出来。另外，下拉刷新期间不要清空旧数据——请求回来之前让旧内容继续显示，数据到了整体替换，页面就不会"闪一下白屏"。

#### 六、多城市管理：添加、删除、切换与数据结构设计

一个真实的需求场景：你在北京，爸妈在老家，你自己还常出差。单城市的天气助手满足不了"一眼看三地"，这一节把应用升级成多城市版。功能本身不复杂，真正的考点在<strong>数据结构怎么设计</strong>——结构定对了，添加删除切换都是顺手的；定错了，每加一个功能都要跟数据较劲。

##### 先把数据结构定对

城市列表的每个条目长这样：

::: div .code-block
:::inline div .code-head
<span>ARKTS · model/CityItem.ets</span><span class="dots">···</span>
:::

```
export interface CityItem {
  id: string           // 服务商的城市 ID，重名城市靠它区分
  name: string         // 展示名
  temp: number | null  // 还没请求到数据时是 null
  updatedAt: number    // 上次刷新的时间戳，缓存要用
}
```
:::

两个设计决策解释一下。第一，<strong>主键用服务商的城市 ID，不用城市名</strong>。中国同名地名不少：提到"朝阳"，北京有个区，辽宁有个市；提到"新城"，好几个省都有。你自己拿名字当唯一键，早晚会把两个城市的数据混在一起。添加城市的标准流程因此是两段式：先调服务商的"城市搜索"接口把名字换成 ID（返回多个候选时让用户选），再拿 ID 查天气。

第二，<strong>temp 允许是 null</strong>。列表页打开时，非当前城市的数据多半还没请求回来，界面要能表达"还没有数据"（显示一个占位符），而不是假装它不存在。能不能坦然表达"空"，是数据结构设计成熟与否的标志——强行为空值编造默认值（比如用 0 度占位），用户会看到一堆"0°"的城市，那是真事故。

##### 添加与去重

::: div .code-block
:::inline div .code-head
<span>ARKTS · WeatherPage.ets（添加城市）</span><span class="dots">···</span>
:::

```
async addCity(id: string, name: string) {
  // 去重：同一个 ID 只加一次
  let exists = this.cities.some((c: CityItem) =&gt; c.id === id)
  if (exists) {
    this.hint = '这个城市已经在列表里了'
    return
  }
  this.cities.push({ id: id, name: name, temp: null, updatedAt: 0 })
  await this.saveCityList()   // 持久化，见下文
  this.loadCity(this.cities.length - 1)
}
```
:::

去重看起来是小事，其实是体验问题：用户在搜索页手一抖点了两次"添加"，城市列表里出现两个一模一样的"北京"，他会觉得这应用"不靠谱"，而且说不清为什么。类似的还有删除后的空态：城市全删光了，页面要显示"还没有城市，点这里添加"，而不是一片空白。

##### 删除：左滑与下标越界

ArkUI 的 List 自带侧滑删除，给 ListItem 挂上 swipeAction，再把一个删除按钮作为侧出来的一层：

::: div .code-block
:::inline div .code-head
<span>ARKTS · CityListPage.ets（侧滑删除节选）</span><span class="dots">···</span>
:::

```
@Builder
deleteButton(index: number) {
  Button('删除')
    .backgroundColor('#E5484D')
    .onClick(() =&gt; this.removeCity(index))
}

List({ space: 8 }) {
  ForEach(this.cities, (c: CityItem, i: number) =&gt; {
    ListItem() {
      Row() {
        Text(c.name).fontSize(16).layoutWeight(1)
        Text(c.temp === null ? '--' : c.temp + '°').fontSize(16)
      }
      .padding(14).borderRadius(12)
    }
    .swipeAction({ end: this.deleteButton(i) })
  }, (c: CityItem) =&gt; c.id)
}
```
:::

错误示范先摆出来：删除函数只写 this.cities.splice(index, 1)，不处理选中下标。会发生什么——你正看着列表里第 3 个城市，把它删了，current 还停在 3，而列表只剩 2 个城市，详情区引用一个不存在的条目，轻则白屏，重则崩溃。纠正版：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 删除城市（含下标修正）</span><span class="dots">···</span>
:::

```
removeCity(index: number) {
  this.cities.splice(index, 1)
  if (this.current &gt; index) {
    this.current--              // 删的是前面的城市，选中下标左移
  } else if (this.current === index) {
    this.current = Math.max(0, Math.min(index, this.cities.length - 1))
  }                             // 删的就是当前城市，就近落到一个合法位置
  this.saveCityList()
}
```
:::

"删的是当前项"和"删的是别的项"是两种情况，分开处理。这类下标问题没有高深的算法，靠的是删除那一刻在心里把每种情况过一遍——数组操作的所有 bug，几乎都是"情况没过全"。

##### 切换与持久化

切换城市就是改 current 下标，UI 跟着 ForEach 自动换内容，这部分是声明式 UI 的红利，不用写任何"刷新界面"的代码。要上心的是持久化：上一章待办清单里用 Preferences 存数据的那套直接搬过来——把城市列表序列化成 JSON（存 ID 和名字就够，温度不该存），启动时读回来。区别只有一个：待办清单存的是一坨整体，城市列表存的是"引用"，温度、更新时间这些数据每次启动重新请求，列表本身才是要记住的东西。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士

{class="mt-1"}
城市列表别贪多。天气 API 的免费额度几乎都按调用量计费，10 个城市每次启动全部刷新，额度消耗速度是单城市的 10 倍。合理策略是只刷用户正在看的那个城市，其他城市切过去时再刷（配合第七节的缓存）。省额度、省电、省流量，一箭三雕。
:::

#### 七、缓存与离线：上次数据的展示与过期标记

想象两个场景：早高峰地铁开进隧道，你想看一眼今天要不要带伞，应用却顶着满屏转圈；服务商那边限流，你的请求被拒，应用白屏。这两个场景的共同答案是——<strong>能显示旧数据，就别显示错误页</strong>。天气数据有一个天然美德：它过期得很慢，一小时前的"多云 12°"和现在的"多云 12°"大概率没差别。缓存就是这个美德的变现。

##### 缓存什么、什么时候读写

写缓存的时机只有一个：请求成功时。读缓存有两个时机：页面启动时先读缓存渲染（秒开，不等网络），然后静默请求新数据，回来后覆盖；请求失败时，检查有没有缓存可以顶上——这就是第三节说的"失败时把上一次成功的数据摆出来"的落地实现。

::: div .code-block
:::inline div .code-head
<span>ARKTS · service/WeatherCache.ets（极简缓存）</span><span class="dots">···</span>
:::

```
import { preferences } from '@kit.ArkData'

export class WeatherCache {
  private store: preferences.Preferences | null = null

  // context 从 Ability 里传进来
  async init(context: Context): Promise&lt;void&gt; {
    this.store = await preferences.getPreferences(context, 'weather_cache')
  }

  async save(cityId: string, rawJson: string): Promise&lt;void&gt; {
    if (this.store === null) { return }
    await this.store.put('raw_' + cityId, rawJson)
    await this.store.put('time_' + cityId, Date.now())
    await this.store.flush()
  }

  async load(cityId: string): Promise&lt;string | null&gt; {
    if (this.store === null) { return null }
    let raw = await this.store.get('raw_' + cityId, '') as string
    return raw === '' ? null : raw
  }

  async savedAt(cityId: string): Promise&lt;number&gt; {
    if (this.store === null) { return 0 }
    return await this.store.get('time_' + cityId, 0) as number
  }
}
```
:::

键名按城市 ID 拆开（raw_ 前缀存数据、time_ 前缀存时间），而不是把所有城市塞进一条记录。原因还是那句"为将来想一步"：单条记录太胖，读一个城市要解析全部；将来想清掉某个城市的缓存，也没法精准下手。

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>避坑提醒

{class="mt-1"}
缓存里存"原始响应"还是"给 UI 的模型"？强烈建议存原始响应的 JSON 字符串。存 UI 模型的话，哪天你改了个字段名、加了个显示需求，所有旧缓存瞬间作废，用户升级后的第一次启动满屏异常；存原始响应，解析逻辑升级了，旧缓存照样能被新逻辑消化。缓存的数据格式要跟接口对齐，不要跟界面对齐。
:::

##### 启动两步走与过期标记

::: div .code-block
:::inline div .code-head
<span>ARKTS · WeatherPage.ets（启动时的读写顺序）</span><span class="dots">···</span>
:::

```
async onPageShow() {
  await this.cache.init(this.context)
  // 第一步：先上缓存，页面立刻有内容
  let cached = await this.cache.load(this.currentCityId)
  if (cached !== null) {
    this.applyData(cached, true)
  }
  // 第二步：再要新数据，成功后整体覆盖
  this.load()
}

applyData(rawJson: string, fromCache: boolean) {
  this.weather = parseWeather(rawJson)   // 第四节那套防御式解析
  if (fromCache) {
    let at = this.lastSavedAt
    this.updatedText = '数据更新于 ' + formatTime(at)
    // 过期线自己定：比如超过 3 小时就算"可能过期"，按天气数据的更新节奏来
    this.stale = Date.now() - at &gt; 3 * 3600 * 1000
  }
}
```
:::

过期线定多长不是玄学，跟着天气数据本身的更新节奏走：实况数据通常几十分钟到几小时才上一个台阶，把过期线定在比它长一点的位置就好，定成"5 分钟就过期"只会让用户满屏看到不必要的黄色警告。过期标记的界面形态：温度旁边一行小字，"今天 08:32 更新"，过期了就变成"数据可能已过期，下拉可刷新"——注意错误提示的老原则依然适用：说清发生了什么，给出能做什么。

这里有一个容易做反的细节：缓存渲染时<strong>不要把 loading 态叠上去</strong>。既然有旧数据可看，就不该再转圈——转圈的意义是"页面上什么都没有，你等等"，有内容时转圈只会让用户以为卡死了。三态模板遇到缓存要灵活：loading 态只在"完全没有任何数据"时才登场。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士

{class="mt-1"}
测试缓存别靠"等它过期"。开发期把过期线临时改成 10 秒，跑一遍"有网 → 断网 → 重启应用"的流程：断网重启后能看到旧数据并带着过期标记，这个流程通了，缓存就算验收了。验收完把过期线改回去，别把调试参数带上生产。
:::

#### 八、UI 打磨：天气图标映射、温度曲线与深色模式

功能齐了之后，应用离"像样"还差一层皮。这一节做三件性价比最高的打磨：把天气文字换成图标、把温度列表画成曲线、让深色模式不穿帮。它们都不改业务逻辑，但用户对应用质感的判断，几乎全来自这一层。

##### 天气图标：一张映射表管全部

接口返回的是"晴""多云""小雨"这类文字，界面上要的是图标。做法是建一张集中管理的映射表，别在十几处 if 里散着写：

::: div .code-block
:::inline div .code-head
<span>ARKTS · utils/WeatherIcon.ets</span><span class="dots">···</span>
:::

```
const ICON_MAP: Record&lt;string, string&gt; = {
  '晴': 'ic_sunny',
  '多云': 'ic_partly',
  '阴': 'ic_overcast',
  '小雨': 'ic_rain_light',
  '大雨': 'ic_rain_heavy',
  '雷阵雨': 'ic_thunder',
  '雪': 'ic_snow',
  '雾': 'ic_fog',
  '霾': 'ic_haze'
}

export function iconOf(text: string): string {
  return ICON_MAP[text] ?? 'ic_unknown'   // 兜底图标必须有
}
```
:::

两个要点。一是<strong>兜底图标必须有</strong>：服务商的天气现象词表很长，"浮尘""强沙尘暴"这类词什么时候冒出来你说了不算，映射表查不到时退到一张通用的"问号"图标，界面永远不会开天窗。二是集中管理的意义在"改一处生效"：哪天你想把图标换成动画版，只动这张表和资源文件，页面代码一行不碰。开发期图标资源还没做出来怎么办？先让 iconOf 返回文字占位，结构对了，皮随时能换。

##### 温度曲线：Canvas 画两条线

七天预报的文字列表看趋势很费劲，一条折线一眼就能看出"周三降温"。用 ArkUI 的 Canvas 画两条线（最高温一条、最低温一条），核心只有一步数学：把温度值映射成屏幕上的 y 坐标——温度越高，点越靠上。

::: div .code-block
:::inline div .code-head
<span>ARKTS · TempChart.ets（温度区间曲线）</span><span class="dots">···</span>
:::

```
@Component
struct TempChart {
  days: DailyItem[] = []
  private ctx: CanvasRenderingContext2D =
    new CanvasRenderingContext2D(new RenderingContextSettings(true))

  build() {
    // 示例按固定尺寸示意；要做自适应，可在 onReady 里取实际宽高后再画
    Canvas(this.ctx).width(336).height(120)
      .onReady(() =&gt; this.draw())
  }

  draw() {
    if (this.days.length &lt; 2) { return }   // 一天画不成线，也防除以 0
    let w = 336
    let h = 120
    let max = this.days[0].tempMax
    let min = this.days[0].tempMin
    for (let d of this.days) {
      if (d.tempMax &gt; max) { max = d.tempMax }
      if (d.tempMin &lt; min) { min = d.tempMin }
    }
    let span = Math.max(1, max - min)      // 温度都一样时也别除以 0
    let step = w / (this.days.length - 1)
    // 上下各留 20 像素边距，把温度映射成 y 坐标
    let y = (t: number): number =&gt; 20 + (max - t) / span * (h - 40)

    this.drawLine(this.days.map((d: DailyItem) =&gt; d.tempMax), y, step, '#FF7D00')
    this.drawLine(this.days.map((d: DailyItem) =&gt; d.tempMin), y, step, '#4D88FF')
  }

  private drawLine(vals: number[], y: (t: number) =&gt; number,
                   step: number, color: string) {
    this.ctx.beginPath()
    for (let i = 0; i &lt; vals.length; i++) {
      if (i === 0) { this.ctx.moveTo(i * step, y(vals[i])) }
      else { this.ctx.lineTo(i * step, y(vals[i])) }
    }
    this.ctx.strokeStyle = color
    this.ctx.lineWidth = 2
    this.ctx.stroke()
  }
}
```
:::

代码里两处 Math.max 不是废话：温差为 0（七天内全是同一温度）时 span 如果是 0，除法直接出 NaN，整条线消失得无影无踪——你会以为 Canvas 坏了，其实是数学先坏了。画图类代码调试技巧说一句：先把坐标点用 Text 标出来验证位置对不对，再画线。想进阶的话，把 moveTo 换成贝塞尔曲线让线条圆滑、在线的端点标数值，都是在这一版基础上加层皮的事。

##### 深色模式：颜色进资源，别进代码

先说错误做法：颜色全用硬编码，'#888888' 灰字、'#F2F3F5' 浅灰卡片。写的时候很爽，系统一切到深色模式，浅灰卡片在深黑背景上亮得像手电筒，灰字糊成一团。正确做法是把颜色定义成资源，base 目录放浅色值，dark 目录放同名深色值，代码里引用资源名，系统切换时自动换：

::: div .code-block
:::inline div .code-head
<span>JSON · resources 下的双份颜色</span><span class="dots">···</span>
:::

```
// resources/base/element/color.json（浅色）
{
  "color": [
    { "name": "text_primary",   "value": "#1A1A1A" },
    { "name": "text_secondary", "value": "#888888" },
    { "name": "bg_card",        "value": "#F2F3F5" }
  ]
}

// resources/dark/element/color.json（深色，同名不同值）
{
  "color": [
    { "name": "text_primary",   "value": "#E6E6E6" },
    { "name": "text_secondary", "value": "#9E9E9E" },
    { "name": "bg_card",        "value": "#2A2A2A" }
  ]
}

// 代码里一律引用资源：
// .fontColor($r('app.color.text_secondary'))
// .backgroundColor($r('app.color.bg_card'))
```
:::

改完之后拿真机或模拟器切一次深色模式（设置里的显示与亮度），把页面从头滑到尾，重点检查下面这几处重灾区：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">检查位置</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">典型问题</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">处理方式</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">大号温度数字</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">深底深字，看不清</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">引用 text_primary 资源色</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">卡片背景</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">浅灰卡片刺眼</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">引用 bg_card 资源色</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">天气图标</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">浅色图标在深底上看不见</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">图标做两套，或选深浅通用的描边风格</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">错误文案</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">硬编码的 Color.Red 太扎眼</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">换成资源定义的警示色，深浅各给一档</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">温度曲线</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">线色写死，深底上偏暗</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">画线颜色同样走资源色</td></tr>
</tbody>
</table>
```
:::

深色模式的本质不是"换个背景色"，是"所有颜色都有两套答案"。你把颜色全收进资源文件的那一刻，深色模式就从"待办事项"变成了"自动获得"。

#### 九、常见 bug 门诊：六个高频翻车现场

这一节按问答组织，六个问题全是这个项目的高发事故。建议你别顺着读——先自己写，卡住了再来对号入座，印象深十倍。

<strong>问：JSON.parse 直接抛异常，报"Unexpected token"，模拟器上好好的，真机就不行？</strong>

答：三个常见来源，按顺序查。第一，resp.result 不一定是字符串——request 的返回类型取决于 expectDataType，没设 STRING 时可能拿到对象或二进制，对它做 JSON.parse 自然炸；第二，服务端返回的可能根本不是 JSON——限流、网关报错时 body 常是一段 HTML 错误页，parse 到 "&lt;html&gt;" 第一个字符就翻车；第三，弱网下响应被截断，JSON 少了半截。修法：解析前先打印原始返回看一眼（开发期专用，上线前删掉），解析套上 try-catch，catch 里走错误态而不是崩溃。记住一句：JSON.parse 是这个项目里最不该裸奔的一行代码。

<strong>问：请求老是超时，模拟器都正常，是不是我代码有玄学问题？</strong>

答：大概率不是玄学，是网络环境。模拟器走的是电脑的网络，又快又稳；真机走蜂窝或办公楼 Wi-Fi，弱、慢、会断才是常态。逐项查：request 参数里 connectTimeout 和 readTimeout 设了没（第三节强调过，没设的弱网下干等到天荒地老）；超时时长是不是太短——天气接口正常响应只要几百毫秒，但弱网下握手就要好几秒，给到 10 秒量级比较稳；还是不行就换飞行模式开关一次，复现"网络刚恢复"的场景。另外 UI 上要区分"超时"和"失败"：超时提示"网络不给力，稍后再试"，比笼统的"加载失败"体面得多。

<strong>问：数据明明请求回来了，console 打印都有值，界面就是不动？</strong>

答：十有八九是"状态没走 @State"。 ArkUI 靠状态变化驱动界面，赋值给普通成员变量界面理都不理。先检查变量声明处有没有 @State。另一个高发变体：@State 只观察"第一层"——你把 cities 数组 push 进了对象，然后改 cities[0].temp = 25，这种嵌套属性修改不触发刷新。修法是"整体替换"或走数组 API：用 splice 把新对象换进去，或者干脆整个数组重新赋值。判断口诀：想让界面变，就让状态变量本身发生一次它看得见的变更。

<strong>问：快速点两下"查询"，数据闪了两下，最后显示的还是上一个城市？</strong>

答：这是重复请求加竞态：两次请求并发，谁后到谁覆盖，先发出的后返回就把新数据盖了。两道防线一起上：第一道是 loading 守卫，请求进行中再点查询直接 return；第二道是请求序号，专防"守卫漏掉"的并发：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 请求序号防竞态</span><span class="dots">···</span>
:::

```
private seq: number = 0

async load() {
  let mySeq = ++this.seq          // 发起前领号
  this.loading = true
  try {
    let data = await this.svc.fetch(this.city)
    if (mySeq !== this.seq) { return }   // 已有更新的请求，这份结果作废
    this.weather = data
  } catch (e) {
    if (mySeq !== this.seq) { return }   // 过期请求的报错同样不显示
    this.error = '加载失败，请检查网络后重试'
  }
  this.loading = false
}
```
:::

原理一句话：每个请求发起时领一个号，回来先对号——号不是最新的，说明路上已经有更新的请求了，这份结果默默扔掉。下拉刷新、切换城市、自动定位三个入口都可能触发请求，竞态防线是必配不是可选。

<strong>问：定位一直转圈，成功回调永远不来？</strong>

答：先分清两个"转圈"：界面转圈还是定位本身没结果。最常见原因是权限流没走完——module.json5 里声明了，但运行时 requestPermissionsFromUser 没调或没检查结果，系统直接不给你定位，而且这种失败多半不抛异常，就是安静地没有回调。所以定位调用必须包在 try-catch 里，超时兜底也要有（比如几秒没结果就提示"定位失败，手动输入试试"）。第二大原因是模拟器没设置过位置，去模拟器的位置设置里选一个点再试。验证顺序记住：权限 → 模拟器位置 → 再怀疑代码。

<strong>问：城市名带中文就请求失败，英文城市一切正常？</strong>

答：URL 不接受中文和空格这些字符，直接拼进请求里，服务端可能收到乱码或干脆 400。修法第三节就用过：encodeURIComponent(city)。容易漏的是"整段编码"——如果你拼的参数不止一个，每个参数值都要单独编码，只编一半等于没编。顺带一提，编码要在"拼接 URL 的那一处"做，别在输入框 onChange 里就编，否则你拿到的城市名永远是编码后的怪字符串，存缓存、做搜索全乱套。数据在什么时候需要什么形态，边界要清楚：明文进内存，编码进 URL。

#### 十、性能与电量：请求频率控制与后台刷新的克制

天气应用做不好，很少死在功能上，多半死在"太勤快"上。这一节按"很多人以为 X，其实 Y"的格式，把最容易犯的几条列出来。

<strong>误区一：以为天气要"实时刷新"，其实数据本身就不实时。</strong>

天气实况几十分钟到几小时才更新一个台阶，你分钟级地轮询接口，拿回来的数据跟上一份大概率一模一样——流量、电量、接口额度全烧了，用户看到的数字纹丝不动。合理频率：进前台时刷一次，用户手动刷新一次，完事。你要的"实时感"，用"数据更新于 XX:XX"这行小字给，不用请求频率给。

<strong>误区二：以为后台要保活定时刷新，其实系统的冻结是在帮你。</strong>

应用退到后台，系统过一阵就会冻结它，很多新手把这当 bug，千方百计申请长时任务让自己活着、每半小时偷偷刷一次。冷静想：用户没打开你的应用时，天气数据对谁有用？对没人有用。保活换来的只有耗电排行上的名次和应用市场上的差评。正确的后台姿势是"克制"：不保活、不轮询，把力气花在"回到前台那一刻能多快出数据"上——答案就是第七节的缓存，秒开靠缓存，不是靠后台。

<strong>误区三：以为定位监听常开体验好，其实单次定位就够了。</strong>

天气应用只需要"打开时你在哪座城市"，不需要"你每一秒在哪"。持续监听位置意味着 GPS 反复唤醒、电量持续流出，而收益接近零。单次定位，拿到城市就收手。同理，定位失败也别无限重试，失败一次就退到手动模式，把选择权还给用户。

<strong>误区四：以为多城市要全部同时刷，其实刷眼前那个就够。</strong>

第六节提过一笔，这里算笔细账：免费额度按调用量计，启动刷 10 个城市，等于把你的额度消耗速度放大 10 倍，而且其中 9 个用户这次根本没看。策略：只刷当前城市，其他城市切过去时再刷，没到过期线的直接吃缓存。额度充裕了，你才敢做更多功能。

<strong>误区五：以为重复触发无所谓，其实短时间去抖很必要。</strong>

用户切回前台、下拉刷新、点查询，三个动作可能在几秒内连续发生，同一城市短时间内重复触发请求就该直接复用上一次结果：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 同城市短时间去抖</span><span class="dots">···</span>
:::

```
private lastFetchAt: number = 0
private lastCity: string = ''

async load() {
  let now = Date.now()
  // 同一城市一分钟内重复触发，直接复用上一次结果
  if (this.city === this.lastCity &amp;&amp; now - this.lastFetchAt &lt; 60 * 1000) {
    return
  }
  this.lastFetchAt = now
  this.lastCity = this.city
  // ……后面的请求逻辑不变
}
```
:::

一分钟这个阈值不是标准答案，是个合理起点，你自己按"数据更新节奏 + 用户手感"调。加这段代码前记得配合第七节的缓存——被去抖挡掉的请求，用户看到的本来就是缓存数据，体验没有损失。

电量怎么验收？别凭感觉，跑真实数据：把应用正常用一周，去系统设置里的电池用量排行看看它排第几（各家系统入口路径不同，找"电池"或"电池与性能"之类条目）。一个天气应用排进前五，一定是你哪里太勤快了——按这一节的清单回头收一遍。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-quote-left mr-2"></i>一句话记牢

{class="mt-1"}
天气应用的美德是克制：数据更新得慢，你就该请求得慢；用户不在场，你就该安静。
:::

#### 十一、扩展练习：五个进阶题目与提示

主线项目到这里就完整了。下面五个题目按难度递增，每个都只给方向不给答案——做完主线直接做三，卡住了再回头补。这些题目共用前面搭好的三层结构，你要做的多数是"往结构里添东西"，而不是"推翻重来"，这本身就是对架构的一种检验。

1. <strong>逐小时预报</strong>：把 7 天列表升级成"今天逐小时"的时间轴。提示：预报接口一般有逐小时版本，时间字段是"2026-11-13 14:00"这类格式，第八节的 weekdayLabel 改成"14 时"这种标签复用；条目会超过 24 个，横向列表从 Scroll 换成 List 更稳；温度曲线和小时轴拼在同一屏，滑到哪曲线跟到哪是加分项。
2. <strong>极端天气预警横幅</strong>：接口返回预警数组时，页面顶部显示一条醒目的预警横幅。提示：先想空数组的情况——没有预警就不渲染横幅，这个"不渲染"的判断写在哪一层？横幅用警示色资源（第八节深色那套记得配两档），点击展开详情；预警的生效与解除有时间字段，过期的预警要不要展示，想清楚再写。
3. <strong>生活指数卡片</strong>：穿衣、洗车、紫外线这类指数接口，返回的是"标题 + 等级 + 建议文字"。提示：这几种指数结构完全一样，做一个通用卡片组件，数据驱动渲染，别给每种指数写一个卡片——写三个几乎相同的组件，你就该闻到重复代码的味道了（第 37 章）。
4. <strong>城市置顶与排序</strong>：多城市列表支持长按拖动排序或侧滑"置顶"。提示：数据结构里加个 sort 字段，操作后重排数组并持久化；ForEeach 的键值继续用城市 ID，排序变化时界面才能正确复用；想偷懒就只做"置顶"不做全排序，价值八成功能两成。
5. <strong>温度单位切换</strong>：设置里加摄氏/华氏切换。提示：换算放展示层，存储层永远存一份原始数据，别存两套；单位选择记进 Preferences，启动时恢复；切换后所有温度（含曲线的坐标映射）要一起变，正好检验你第八节的映射函数是不是把单位写死了。

做完五题再回头看你的 Service 层：它是不是从头到尾没怎么改过？如果是，恭喜，你已经体会到"分层"的回报——界面怎么折腾，数据层稳如老狗。如果 Service 被改得面目全非，说明有些解析逻辑当初放错了地方，趁项目还热，把它挪回去。

#### 十二、项目复盘：同一件事，三种方言

这个天气助手你在本书里其实见过三次：第 55 章 iOS 篇的天气查询、第 66 章安卓篇的天气应用、这一章的鸿蒙版。三个平台写完同一个项目，复盘的价值不在"学会了鸿蒙"，而在分清<strong>哪些是平台的方言、哪些是你自己的通用功力</strong>。方言会过时，功力跟人走。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">环节</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">通用骨架</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">安卓常用方案（对照第 66 章）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">iOS 常用方案（对照第 55 章）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">鸿蒙（本章）</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">构造请求</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">拼 URL、设超时、发出去</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OkHttp / Retrofit 一类</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession 一类</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@kit.NetworkKit 的 http</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">解析响应</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">JSON 变对象 + 防御</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gson / Moshi 一类</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Codable 一类</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">JSON.parse + interface</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">状态驱动</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数据变了界面跟着变</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Compose 的 State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI 的 @State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ArkUI 的 @State 装饰器</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">三态渲染</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">加载 / 成功 / 失败分支</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">条件渲染</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">条件渲染</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if / else 渲染分支</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">本地缓存</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">存上次数据 + 时间戳</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DataStore 一类</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults 一类</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Preferences</td></tr>
</tbody>
</table>
```
:::

表里"常用方案"一列写的是各平台的主流做法，具体到第 55、66 章当年用的哪个库，翻回去核对一下，大概率就是这一类。你会发现五行的"通用骨架"一模一样——这就是网络应用的骨架，你已经用三种方言各写了一遍。

复盘时建议拿张纸，左边写"平台方言"（比如 @State 装饰器、Refresh 组件、Preferences 这些换平台就不存在的东西），右边写"通用功力"。右边那栏你大概率会写下这些：三态思维（任何异步操作都有加载、成功、失败，UI 要给每态一个家）；防御式解析（接口会变、数据会缺，逐条校验不亏）；失败兜底（旧数据 + 时间标记好过一个空白错误页）；竞态意识（并发请求要对号）；资源释放纪律（请求对象、监听器，用完就收）；真机验证（模拟器永远告诉你"一切正常"）。这六条没有一条写着"鸿蒙"，你把它们写进简历、带到任何平台都成立。

两个常被问到的问题顺手答了。"三个平台都要学吗？"——不必都深学，但第二个平台一定要真的写一遍：第二个平台写起来会快得多，因为它逼你把"方言"和"功力"真正分开。"写完这个项目算入门网络应用了吗？"——算，但只算语法入门；项目删掉重写一遍，卡壳的地方才是你真正没学会的地方，那才是入门。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-quote-left mr-2"></i>一句话记牢

{class="mt-1"}
换平台只是换方言，"请求—解析—三态—兜底"这个骨架才是你自己的；项目做完不算完，删掉重写一遍才算。
:::

#### 十三、发布前检验：五个真机场景过一遍

模拟器最大的害处不是慢，是它永远对你说"一切正常"：电脑的网络又快又稳，电量永远满格，定位永远精准。所以这个项目写完不算完，下面五个真实场景各过一遍——每一场景都先写清楚"预期表现"，测出来不符就是 bug，别靠"感觉还行"糊弄过去。

<strong>场景一：弱网。</strong>早高峰地铁进隧道、写字楼电梯下行，这是你的用户每天真实所处的网络。预期表现：界面不白屏不转死圈，缓存数据顶着用，更新时间标注还在；出了信号盲区，下拉一次就能拿到新数据。模拟方法里最真实的就是拿着真机进出电梯和地下车库；退而求其次，开关几秒飞行模式也能复现"网络刚断又恢复"的过程。测的时候重点盯一处：弱网超时的错误文案是不是区分了"网络不给力"和"加载失败"——笼统文案在弱网下出现的频率，比你想象的高得多。

<strong>场景二：无网冷启动。</strong>先把应用从后台彻底关掉，再打开飞行模式，然后重新启动应用。预期表现：秒出缓存数据并带过期标记，或者干净地给出"当前没有网络"加重试按钮；绝不该出现的，是白屏、闪退、或者卡在加载动画上不动。这个场景专测第七节那套缓存代码是不是真的接通了启动流程——很多人写完缓存只在"断网刷新"时测过，忘了冷启动这条链路上缓存初始化的时机完全不同。

<strong>场景三：后台切回。</strong>把应用切到后台，正常用手机一小时，再切回来。预期表现：应用不要求自己在后台活着（第十节讲过，保活是歧路），回到前台那一刻要么自动触发一次刷新，要么把"数据可能已过期，下拉可刷新"亮出来；顺带去电池用量排行瞄一眼，它不该因为这一次放置就蹿升。这个场景还会暴露另一个经典问题：切回前台时页面状态错乱——比如还停在"城市搜索页"但输入框被清空了。状态恢复做没做，一测便知。

<strong>场景四：权限拒绝后的再次进入。</strong>第一次运行时拒绝定位权限，杀掉应用再打开。这里有个很多人不知道的行为：系统多半不会再弹授权窗（具体策略视系统版本而定），你的代码必须自己发现"没拿到权限"，走默认城市分支，同时给一句"可在系统设置中开启定位"的指引，最好能指到设置的路径。测不过关的典型症状就是第九节门诊那个"定位一直转圈"——转圈的根源几乎都是权限流没走完，不是定位服务坏了。

<strong>场景五：深色模式与系统大字号。</strong>切深色模式，把页面从头滑到尾，按第八节的检查表过一遍。再做一件大多数新手从没做过的事：把系统字号调到最大，回来看界面。温度大数字会不会把卡片撑爆？预报条的日期和温度会不会叠字？给爸妈装应用的人更要测这条——他们手机上的系统字号，通常开得比你想的大得多。字号尽量用相对档位、布局留弹性，这一条在真机上试一次，比看十篇适配文章都管用。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">检查项</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">通过标准</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">弱网与无网</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不白屏不闪退，缓存与错误提示各就各位</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">超时参数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">connectTimeout / readTimeout 已设，弱网下十秒内必有反馈</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">调试痕迹</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">开发期打印原始响应的 console 全部删掉</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">调试参数</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第七节改短的过期线改回生产值</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">敏感信息</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">key、测试账号不出现在代码、注释和截图里</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">上架材料</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">开发者账号、隐私说明等，按应用市场当前要求准备（以官方为准）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">机型覆盖</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">至少两三台不同尺寸真机各滑一遍</td></tr>
</tbody>
</table>
```
:::

最后一个建议：发给你在不同城市的朋友装一版。你在北京，永远测不出"海口回南天湿度 95%"这种体验；不同城市、不同机型、不同网络运营商，就是分布最广的测试团队。他们反馈回来的问题，八成不在你上面这张表里——这正是让他们测的价值。

#### 十四、API key 与安全：一次泄露的代价

先讲一个后果：把带着 key 的代码传上代码仓库，第二天打开服务商控制台，调用量曲线竖起一根天线，免费额度一夜见底。这不是吓唬人——在公开代码里搜现成的 key，是脚本全天候在干的活，从你按下提交到被人扫到，往往用不了多久。天气 API 的 key 看着不起眼，被滥用轻则额度耗尽应用瘫痪，重则账号被封，你还得跟服务商解释。

key 泄露主要走两条路。第一条是<strong>代码仓库</strong>：公开仓库自不必说，私有仓库也不保险——key 会从截图、README、示例代码、聊天记录里漏出去；更要命的是，你后来发现泄露、把 key 从文件里删掉重新提交，也毫无用处，git 历史里它还在。第二条是<strong>安装包</strong>：客户端代码可以被反编译，硬编码在源码里的 key，对会拆包的人来说和写在 README 里没有区别。这就是第三节那句"接口地址与 key 不要硬编码进源码"的真实分量——它不是代码风格建议，是安全底线。

知道了路数，防护可以分三档来做，按你的项目阶段往上加：

1. <strong>最低配，人人都能做</strong>：key 按环境区分配置，开发一套、发布一套，仓库里只放占位符，真实值放在不入库的本地配置里；一旦发现泄露，第一动作是去服务商控制台<strong>吊销重发</strong>——改代码、删文件都不算处理，旧 key 作废才算处理完。
2. <strong>中配，看服务商支持</strong>：不少天气服务商支持把 key 与应用身份（比如包名、签名信息）绑定，绑定后即使 key 被挖走，挪用到别处也会被拒；再配上调用量告警，消耗异常时你能第一时间收到通知，而不是月底才发现额度清零。具体支持哪些绑定方式，以你所用服务商的文档为准。
3. <strong>正配，客户端不持有 key</strong>：应用请求先打到你自己的一台服务端，服务端持有 key 去转发天气请求，顺便做限流、合并和缓存。这一档需要一点后端知识，学生项目和个人项目暂时做不到很正常——那就老老实实用前两档，并且申请一个配额最低的 key 够用就好。

还有一个习惯值得养成：每周看一眼服务商控制台的调用量曲线。看上两三周，你对自己的"正常消耗"就有手感了，之后任何异常尖峰都瞒不过你的眼睛。安全这事，绝大多数时候不靠高深技术，靠的是"知道东西放在哪、知道它正常长什么样"。

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>避坑提醒

{class="mt-1"}
key 一旦进过 git 历史，就按"已经泄露"处理：吊销重发，然后在新配置里换上新值。很多人删掉文件再提交一次就以为完事了——历史提交一翻，key 明晃晃躺在那里。同理，聊天记录里发过的 key、演示截图里拍到的 key，都按泄露处理。
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士

{class="mt-1"}
别人问你要 key "借来用用"，直接拒绝，让他自己花五分钟注册一个免费账号。key 的额度和你这个注册账号绑在一起，借出去的每一笔调用都算你头上，出了滥用还得你去找服务商解释。这不是小气，是账号归属的基本责任问题。
:::

#### 十五、问答：关于天气项目的八个真实疑问

项目做完，问题才真正开始。这一节收的是读者反复问起、论坛上吵个不停的问题，答案尽量给你判断依据而不是现成结论——很多决定取决于你的具体情况，替你拍板反而害你。

<strong>问：天气服务商那么多，我到底选哪家？</strong>

答：别看谁广告大，看四件事：你所在城市的覆盖与数据质量（小城市、区县能不能查到）、免费额度和限流规则（注册前看清楚，很多额度限制写在文档角落）、文档可读性（文档写得乱的服务商，接起来天天受罪）、字段稳定性（三天两头改字段名的，趁早躲开）。实操建议：注册两家免费账号，各花一个晚上跑通 demo，对比你关心的城市的数据和文档体验，自己选。本书不替你点名，免得哪天条款变了书还挂着旧答案。

<strong>问：免费额度够个人项目用吗？我心里的预期一直没底。</strong>

答：这是道算术题，不用猜：把"日活跃用户 × 人均每天触发几次请求"乘出来，和免费额度对一下。用上第十节的克制策略（只刷当前城市、缓存先行、短时间去抖），单人或小圈子使用的项目，免费档通常绰绰有余；真到了要精打细算的规模，说明你的应用有人用了，那是好事，再谈付费或加服务端缓存。额度细节以服务商控制台显示为准，别信网上流传的具体数字，额度规则是经常调整的。

<strong>问：我查出来的天气跟系统自带天气对不上，是我的代码错了，还是数据不准？</strong>

答：多半都不是错。两边的数据源不同、更新时刻不同、定位的城市粒度也可能不同（你查到的是市，系统显示的是区），差个一两度、天气现象差半档，都属正常范围。你要做的是别较真到小数点，把"数据更新于 XX:XX"亮出来让用户自己判断时点，然后接受一个事实：天气本来就是预报，不是测量。如果差得离谱（显示晴天上头暴雨），先核对是不是解析错了字段——第九节第一问。

<strong>问：能不能省事点，用 WebView 直接套一个天气网页？</strong>

答：能，但你会白做这个项目。套网页拿不到这个练习的核心——构造请求、解析 JSON、三态渲染、缓存兜底，这些全在网页那边发生，你只是在里面开了个浏览器窗口。体验上也吃亏：网页加载的白屏、系统权限的衔接生硬、下拉刷新的手感不对，用户一上手就觉出"这不是原生的"。除非你的需求本来就是"展示某个网页"，否则老老实实走原生三段式，这一章教的全部东西才有用武之地。

<strong>问：上架应用市场很麻烦吧？学习阶段要不要弄？</strong>

答：上架涉及开发者账号、应用信息、隐私说明、审核流程，各家市场的具体要求不同而且会随时更新，这里不展开，做的时候以官方文档为准。学习阶段完全没有必要走全套：用开发工具直接把包装进自己的真机，或者用内部测试渠道给朋友装，就够验证了。倒是有一样东西值得提前准备——写清楚你的应用用了哪些权限、数据存在哪，这份说明上架时要用，写作过程还能帮你自查一遍权限是不是都用在刀刃上。

<strong>问：这个项目和上一章的待办清单，哪个更值得放进作品集？</strong>

答：天气助手，没有悬念。待办清单练的本地数据是基本功，但聊起来只有"增删改查"；天气助手带着网络请求、状态管理、缓存、竞态、权限这些话题，每一个都能跟面试官深聊十分钟。放作品集时配一份像样的说明：架构为什么分三层、三态怎么渲染的、缓存过期线怎么定的、踩过什么坑怎么定位的——最能打动人的不是功能截图，是你写下的踩坑记录，它证明项目真的是你做的。

<strong>问：接口返回的字段名跟我定义的 interface 对不上，是谁的错？</strong>

答：谁都没错，是文档与现实的时差——服务商文档写 snake_case，你按习惯定义了 camelCase，两边都对，就是接不上。修法不是全项目改字段名，而是在 Service 里垫一层薄薄的映射：解析时把服务商的字段翻译成你自己的 interface，界面从头到尾只认自己的名字。这层翻译写一次就够了，它正是第三节那句"换 API 只改 Service"的兑现——将来真换了服务商，界面一行不动，改的就是这层映射。

<strong>问：要不要顺手做平板和横屏适配？</strong>

答：学习阶段可以缓一缓，但架构上别把路堵死。做法上的讲究就一条：布局别写死"单列竖排"，用弹性布局留出重排的余地；横屏或宽屏下，让预报条和数据卡片并排展开。分辨一段逻辑该放哪层，可以用这块试金石——换了屏幕形状它变不变？温度换算、缓存策略、请求逻辑都不变，它们属于数据层；三态怎么摆、列表排几列会变，它们留在界面层。第三节的分层一旦立住，多加一种屏幕形状就只是界面层多写一套排法的事。

<strong>问：主线项目做完，感觉网络应用"会了"，但心里又不太踏实，正常吗？</strong>

答：太正常了，这种"会了但不踏实"的感觉恰恰说明你在进步。不踏实的来源通常是：你照着书把路走通了，但还没走过岔路。治疗办法只有一个——制造岔路：做第十一节的扩展题；把项目删掉凭记忆重写；或者换个数据源重新解析一遍。三件事做完还觉得虚，再来重读对应小节。踏实感不是读出来的，是修 bug 修出来的。

<strong>问：接下来往哪走？</strong>

答：两条线可以并行。一条是往下走主线，下一章起的内容会用到你这一章练出的全部手感——网络应用的三段式后面还会在别的应用形态里反复出现，你学过的不是"做天气"，是"调接口"。另一条是横向加厚这个项目本身：第十一节的扩展题、服务卡片（第 79 章的分布式那一套，底稿第三节提过一句）、多设备上的表现。项目不怕小，怕的是浅——把一个小项目做到处处有讲究，比囫囵做完十个 demo 值钱得多。

#### 十六、交付给爸妈：适老化的最后一公里

设想一个真实的交付现场：春节回家，你把亲手写的天气助手装进爸妈的手机。你自己用着处处顺手，到了他们手上却处处卡壳——这不是他们的问题，是你还没做完"适老化"这最后一公里。它不需要什么"长辈模式"开关，需要的只是一串具体的小决定，每个都不难，难的是你在写代码时想到还有人这样用手机。

<strong>字号与点击区域</strong>：界面的默认字号从中档起步，重要数字（温度）要大到隔着一步远能看清。点击区域给手指留够余量——小按钮连点三次都点不中的那种，在这类用户手里等于没有。爸妈的手机上系统字号往往开得很大，所以第十三节场景五那条"大字号下不挤爆"的测试，对他们不是锦上添花，是基本盘。

<strong>图标必须配文字</strong>：太阳加两朵云的图标你一眼懂，他们未必。每个天气图标旁边带上"多云""小雨"的文字，日期显示"周五""明天"而不是一串数字。信息给双通道——看得懂图标的看图标，看不懂的读文字，两边都不吃亏。

<strong>层级要浅</strong>：打开应用第一眼就是当前城市的天气，别加启动页、别加引导页。添加城市这类低频操作收进"管理城市"，但入口必须一眼可见——藏在侧边抽屉菜单里的功能，对不熟悉手势的人来说等于不存在。判断标准很简单：他们第一次拿到应用，三步之内能看到想要的天气，就算及格。

<strong>文案说人话</strong>：第九节门诊里那些技术味十足的文案，到这里要全部翻译一遍。"请求超时"改成"网络慢，等会儿再试"；"数据可能已过期"改成"这是早上的数据，下拉看看最新的"；错误提示里能加一个按钮的，直接把按钮给他们——"重新试试"比"重试"都亲切。文案是最便宜的体验升级，改起来只要几分钟。

<strong>权限弹窗要提前铺垫</strong>：装完应用第一次打开，系统弹定位授权框，你在旁边说一句"点允许，它才能知道你在哪个城市，才能直接显示你们的天气"——这一句比任何界面设计都有效。远程给爸妈装的话，把这句话写进你发过去的安装说明里。他们拒绝过一次，之后系统多半不再弹窗（视系统策略而定），你还得引导去设置里开，成本比第一次就点允许高得多。

<strong>更新与打扰要克制</strong>：别给他们开任何推送——他们不一定知道怎么关，关不掉又用不上的应用，结局就是被卸载。你自己升级版本的节奏也要克制：每次改布局，他们就要重新学一遍，改得越勤，学得越多。功能迭代攒一攒、界面尽量稳，这对年轻用户是"少折腾"，对他们是"还能用"。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士

{class="mt-1"}
适老化的验收方法：把系统字号调到最大，用你不常用的那只手、慢慢点，自己把应用用满一周。过关标准只有一条——爸妈第一次完全独立地查到了"明天的天气"，中途没喊你。
:::

这一节的建议没有一行新代码，但它决定应用"能不能真的被用起来"。技术决定一个项目的下限，这些决定决定它会不会真的出现在别人的生活里。你后面做的每一个应用，都值得过一遍这节清单——用户不都是二十岁、网络好、系统字号标准的人。

#### 十七、上线之后：三个真实的迭代故事

应用交到真实用户手里那一刻，bug 才开始真正的生涯。下面三个故事都来自这类小项目最常见的迭代路径——用户一句模糊的反馈，定位到一个具体的技术问题，修复之后顺手长出一个新需求。把它们讲全，是想让你看到"维护"这个阶段长什么样：它不是重写，是顺着反馈一条一条地收。

<strong>故事一：温度跳变。</strong>朋友反馈："下午温度从 19° 忽然变成 12°，吓我一跳，是不是你们数据错了？"排查第一步先排除数据源——同一时刻网页端查询也是 12°，数据没问题。再往回追，发现他下午确实去了另一个城市，定位自动切换了城市，前后两份数据本就不是同一座城的。修复动作：页面顶部常驻显示当前城市名和更新时间，切换城市时来一次明显的过渡；顺手把第九节的请求序号补上，排除竞态覆盖的可能。这一单的收获：用户报的"bug"常常不是错数据，是你的界面没说清"现在看的是哪座城"。

<strong>故事二：晚上的天气还是早上的。</strong>家里人反馈："晚上九点打开，还是早上那份数据。"排查：过期线当初定得太宽松，而缓存显示逻辑只在"彻底无网"时兜底，有网但静默刷新失败的情况被漏掉了——请求悄悄失败，界面悄悄维持旧数据，两头都没人说话。修复：过期线按数据更新节奏收紧一档；过期标记从角落里的小灰字改成一行明确的提示，带"下拉刷新"的出路；失败兜底加上原因说明，不再无声无息。收获：兜底代码写完不等于功能完成，提示能不能被看见、被读懂，也是功能的一部分。

<strong>故事三：城市越加越多，找不着了。</strong>反馈："加了十来个城市，每次找北京都要滑半天。"定性：这不是 bug，是需求。先用最小代价回应——做了"置顶"功能（第十一节第四题的简版），长按某个城市把它钉在列表最上面；至于完整的拖动排序，先不做，看置顶够不够用。一个月后反馈是"够用了"，排序编辑器就永远不用写了。收获：很多功能不是设计出来的，是被使用反馈顶出来的；先用最小版本接住需求，别一上来造完整工具。

三个故事讲完，给你留一个可以直接抄走的习惯：建一个迭代记录，一行一条——日期、用户原话、定位结论、改了什么、怎么验证的。用户原话务必照抄，转述会丢掉情绪，而情绪里藏着真实的优先级。这份流水账坚持三个月，就是这应用最好的一份文档；等你哪天要把项目写进简历，它顺手就是素材。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-quote-left mr-2"></i>一句话记牢

{class="mt-1"}
应用不是写完那天出生的，是被第一批用户的反馈养大的；听反馈、小步改、记下来。
:::

#### 十八、一天的使用：把所有机制串成一条线

前面十几节按功能一块一块拆着讲，最后一节换个方向——跟着一位用户从早到晚把应用用一遍，看看每个机制在真实时间里是怎么咬合的。你可以把这一节当验收剧本：下面每个时间点对应的都是"应该发生什么"，你的应用全做到了，这个项目才算真的毕业。

<strong>7:20，闹钟响，睁眼点开天气助手。</strong>应用在后台躺了一夜，早被系统冻结了，但第七节的缓存醒得比网络快：半秒之内，昨晚睡前那次请求的数据先摆上桌，角落一行小字"数据更新于昨日 22:41"。紧接着静默刷新发车，新数据落地，小字换成"今天 07:20 更新"。注意这一段里三态只露了 data 一态——缓存让 loading 没了登场的理由，这正是第七节说的"有内容时不转圈"。

<strong>7:35，地铁开进隧道，你想看周末降不降温，下拉刷新。</strong>请求发出去就没了回音。界面上不该出现转圈——有数据在显示，loading 态没资格登场；约十秒后超时，冒出一行"网络不给力，稍后再试"，旧数据原封不动，页面没有闪屏。这一幕里碰头的是第三节设的超时参数、第九节门诊的弱网药方、第七节"能显示旧数据就别显示错误页"的原则，谁都没掉链子。

<strong>8:50，到了出差的城市，想把这里加进列表。</strong>搜索框输入城市名，走的是第六节的两段式：搜索接口先返回候选列表让你选准那一条（避免同名城市的歧义），选中后城市 ID 进了列表，温度位置先摆一个"--"占位，随后只针对这一个城市单独刷新。列表里原有的城市一个字节的流量都没花——只刷眼前那个城市的额度策略，在这一刻悄悄帮你省了钱。

<strong>9:05，想看看爸妈那边降温没有，切到老家城市。</strong>切换的瞬间，缓存里一小时前的数据直接上屏，还没过过期线，服务端一个请求都没发。假如已经过了线，你会看到"数据可能已过期，下拉可刷新"的小字，而不是一个自作主张的转圈。切换的顺滑，一半归功于 ForEach 和 @State 的声明式绑定，另一半归功于第六节那个"temp 允许为 null"的数据结构——它让"还没数据"这件事可以被体面地表达。

<strong>12:30，午休刷手机，切回应用。</strong>系统把它冻了一上午，回到前台那一刻：自动刷新一次（第十节允许的那种"进前台刷一次"），数据跟上今天的节奏。你顺手把系统切到深色模式看傍晚的效果——颜色全部来自双份资源，深浅两套无缝换装，没有一张刺眼的浅灰卡片，没有一团看不清的深色文字。第八节那张检查表上的每一行，此刻都在无声地工作。

<strong>22:40，睡前最后看一眼。</strong>这次刷新的数据写进缓存，时间戳停在 22:41——它是为明天早上 7:20 那半秒钟的秒开准备的。一天绕了一个圈，从缓存开始，到缓存结束，中间所有的请求、防御、克制，都是在为"下一个早晨快一点"服务。

把这条时间线存下来当测试脚本，一个时间点一个时间点在真机上过。全都对上了，你的天气助手就不再是"跟着书做出来的 demo"，而是一个能在别人的生活里站住脚的应用。至于它还能走到哪——服务卡片、手表、智慧屏，另一台设备上看到同一份天气，那是第 79 章要展开的分布式故事，这一章你打的每一层地基，都会在那边接着用。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-quote-left mr-2"></i>一句话记牢

{class="mt-1"}
单点功能都会写，一天下来环环咬合不出错，才算真的把网络应用做完了。
:::

写到这里，再交代一句放在最后的实话：这一章的代码示例刻意保持"最小可跑"，真要把它搬进你的工程，还要过一遍你自己的命名规范、日志规范和团队约定——书给的是骨架和判断力，不是可以照抄的模板。同样，示例里出现的接口地址、字段名、过期线、去抖阈值，都是教学用的占位与示意，落地时以你选定的服务商文档和你自己的用户反馈为准。把这两个"以什么为准"记住，你就不会把任何一本书——包括这本——当成终点。

还有一件小事值得现在就做：给这份代码写一段三行的 README——用了哪个服务商的哪个接口、三态怎么渲染、缓存存在哪、过期线多长。别小看这三行，下周你自己回来看代码时，它们省下的恢复成本比任何注释都大。项目会过时，把"为什么这么做"写下来的习惯不会。至于下一站——挑一道扩展题做完，或者把这一章删掉凭记忆重写一遍，都好过急着奔向下一个新项目。

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 三层拆分：Service 管请求、页面管三态、UI 按状态渲染
- HTTP 请求用 @kit.NetworkKit 的 http 模块，用完 destroy
- JSON 解析防御式：字段映射 + 类型守卫，别让异常崩溃应用
- 三态渲染（loading/data/error）是网络 UI 的万能模板
- 错误提示要包含"发生了什么"和"能做什么"
- 真实 API 的接入重点在"读懂返回 JSON"与防御式解析
:::
