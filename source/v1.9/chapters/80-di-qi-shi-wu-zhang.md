---
id: di-qi-shi-wu-zhang
num: 75
nav: 第七十五章：数据持久化与网络请求
toc: default
kind: chapter
after_part: hongmeng-kai-fa-pian
---

### 第七十五章：数据持久化与网络请求

{class="chapter-intro mb-4"}
应用要"记住事情"才叫应用。这一章补齐鸿蒙的两大能力：本地存储（偏好、数据库、文件）与网络请求（HTTP）。对应安卓的 SharedPreferences/Room/OkHttp 与 iOS 的 UserDefaults/Core Data/URLSession——概念全部一一对应。

先建立一个"选型直觉"：存储方案不是随便挑的，而是按数据形态分层——轻量键值用 Preferences（几十个设置项），结构化数据用 RelationalStore（列表、记录），大文件用文件系统（图片、缓存），敏感数据用专门的安全存储。四层各司其职，混用是大多数数据问题的根源。网络请求则与存储紧密相关：请求回来的数据往往要"落一层"（缓存到本地），断网时应用才有内容可展示。

::: div .quick-read
##### 本章速读（5 分钟版）
应用要"记住事情"才叫应用。这一章补齐鸿蒙的两大能力：本地存储（偏好、数据库、文件）与网络请求（HTTP）——对应安卓的 SharedPreferences、Room、OkHttp 和 iOS 的 UserDefaults、Core Data、URLSession，概念全部一一对应。先立一个选型直觉：存储方案按数据形态分层挑，混用是大多数数据问题的根源；请求回来的数据要"落一层"缓存，断网时应用才有内容可展示。
最关键的有三件事。第一，<strong>存储四层各司其职</strong>：轻量键值用 Preferences（几十个设置项）、结构化数据用 RelationalStore（列表、记录）、大文件走文件系统（图片、缓存）、敏感数据用系统安全存储——选型第一问永远是"这份数据泄了会伤到用户吗"。第二，<strong>网络请求的固定套路</strong>：先在 module.json5 里声明 INTERNET 权限（鸿蒙网络开发第一大翻车点，忘了声明报错还很隐晦），然后 createHttp → request → 判状态码 → destroy() 四步走，destroy 放在 finally 里——不销毁的请求对象会累积泄漏，App 越用越卡就是这类细节攒出来的。第三，<strong>三件安全大事</strong>：正式接口一律 HTTPS 且证书校验不绕过；token 用关键资产存储（Asset Store Kit）这类安全存储保管，退出登录彻底清掉；日志要脱敏——敏感字段打码、不打完整报文、发布版关掉调试日志。
今天就能做的最小动作：把 Preferences 的读写跑一遍，把"put 之后必须 flush()"刻进脑子——数据"写进去了、重启就丢"的头号原因就是忘了这一下。
高频坑一串：忘了声明 INTERNET 权限（请求直接失败）；JSON 解析裸奔（服务器返回个 HTML 错误页就抛异常——解析永远包 try/catch，字段加可选链兜底）；只看 HTTP 200 就当成功（很多接口 200 只代表通信成功，业务成败藏在响应体的 code 字段里）；URL 带中文参数不编码（拼进 URL 前过一遍 encodeURIComponent）；断网无退避地重试几十次（被服务器限流——重试要加间隔、设上限，429 和 4xx 不重试）；主线程里跑大查询和同步文件读写（列表一滚就掉帧）。还有一条思路值得带走：离线优先——先把数据存本地、把界面做活，再加网络层，任何时候你的应用都是能用的。数据库进阶还有索引、分页、并发三招；版本升级要写迁移方案，别把用户已经存下的数据弄丢——上线前照着数据层体检清单逐项过一遍。调试这边备好日志与抓包两件工具，出了问题先看服务器返回的真实内容。
##### 速查表
- 选型四层：设置 Preferences、记录 RelationalStore、大文件文件系统、token 安全存储
- Preferences 铁律：put 之后必调 flush()，否则重启就丢
- 网络第一坑：module.json5 先声明 INTERNET，改权限要重新安装才生效
- 请求四步：createHttp → request → 判状态码 → destroy()，销毁放 finally 里
- 两层都要判：HTTP 200 只是通信成功，业务成败看响应体的 code 字段
- 解析别裸奔：try/catch 包住，字段加可选链兜底，先打印返回的前几百字符看真相
- 安全三红线：生产禁明文 http、token 不进 Preferences 和日志、不"信任所有证书"
- 重试讲纪律：加间隔、设上限，429 与 4xx 不重试
:::

#### 一、用户首选项：轻量键值存储

存"设置开关、上次位置"这类小数据，用 <strong>Preferences</strong>（对应安卓 SharedPreferences / iOS UserDefaults）：

::: div .code-block
:::inline div .code-head
<span>ARKTS · Preferences 读写</span><span class="dots">···</span>
:::

```
import { preferences } from '@kit.ArkData'
import { Context } from '@kit.AbilityKit'

let store: preferences.Preferences | null = null   // 也有同步接口 getPreferencesSync

// 初始化（一般在 EntryAbility onCreate 里拿 context 后做一次）
async function initStore(context: Context) {
  store = await preferences.getPreferences(context, { name: 'settings' })
}

// 写
async function saveTheme(dark: boolean) {
  await store?.put('dark_mode', dark)
  await store?.flush()   // 不调用 flush 可能不落盘！
}

// 读
async function loadTheme(): Promise&lt;boolean&gt; {
  return (await store?.get('dark_mode', false)) as boolean ?? false
}
```
:::

三个易错点：<strong>异步 API</strong>（全是 Promise，记得 await）；<strong>flush()</strong> 不调用可能不持久化；<strong>值不支持对象</strong>——要存对象先 JSON.stringify 成字符串。还有一条容易忽略：<strong>别拿 Preferences 存敏感数据</strong>——登录 token 这类要放更安全的存储，而且无论如何别把它们打进 HiLog 日志，日志恰恰是排错时最容易外泄的地方。

初始化的时机也有讲究：Preferences 实例要在 EntryAbility 的 onCreate 里拿 context 创建一次，然后全局复用——每次读写都新建实例既浪费也容易出竞态。同步接口（getPreferencesSync/putSync）在 UI 里更方便，但首次加载（文件不存在时）仍可能阻塞主线程，重数据还是用异步版。键名建议统一用常量管理——散落的字符串键名是"设置项神秘消失"问题的头号来源。

#### 二、关系型数据库：结构化数据用 RelationalStore

结构化数据（待办、记账、笔记）用 <strong>RelationalStore</strong>——底层就是 SQLite，API 风格对应安卓的 Room：

::: div .code-block
:::inline div .code-head
<span>ARKTS · RelationalStore 增删查</span><span class="dots">···</span>
:::

```
import { relationalStore } from '@kit.ArkData'

let rdb: relationalStore.RdbStore | null = null

async function initDb(context: Context) {
```
:::

RelationalStore 的核心概念对照安卓 Room：getRdbStore 对应 database 实例，executeSql 跑建表与无结果语句，querySql 返回游标（ResultSet，逐行 goToNextRow 读取）。游标用完记得 close——泄漏游标在频繁查询的场景会累积内存压力。

数据库设计的两条纪律：建表语句用 IF NOT EXISTS（应用升级后老用户的数据不能丢）；字段变更用"版本号 + 迁移"处理（给数据库加一个 version 键存进 Preferences，版本变了就执行迁移 SQL）。这两条在安卓 Room 和 iOS Core Data 里同样是铁律——数据层的"向后兼容"意识是跨平台开发的通用素养。

安全级别也要留意：getRdbStore 的 securityLevel 参数（S1-S4）决定数据库的访问约束，普通应用数据用 S1 即可，包含敏感信息的数据用更高的级别——系统会对不同安全级别的文件做不同的保护。这个概念是鸿蒙特有的，选对级别比事后补救省心。

#### 三、文件管理：沙箱目录、图片保存与文件读写

Preferences 和数据库解决的是"结构化的小数据"，但应用里还有一类东西它们都装不下：日志、草稿、下载的文件、拍照生成的图片。这类"大块头"该进<strong>文件系统</strong>，而动手前的第一问是：我能把文件放在哪？

##### 应用沙箱：每个应用都有自己的家

现代手机系统都给每个应用划了一个"沙箱"——你的应用只能读写自己目录里的文件，想碰别人的数据，得走系统提供的受控接口。这既是安全设计，也帮你省了心：不用操心文件名跟别的应用打架。鸿蒙侧最常用的几个目录都从 context 拿：

- <strong>filesDir</strong>：长期文件目录。用户数据、草稿、配置文件放这里，系统不会随便动它。对应安卓的内部存储私有目录、iOS 的 Documents。
- <strong>cacheDir</strong>：缓存目录。网络图片、接口结果的磁盘缓存放这里。空间紧张时系统可能回收，所以放进来的东西必须"随时消失也不影响功能"。
- <strong>tempDir</strong>：临时目录。用完即删的中间产物放这里，比如分享前临时生成的一张压缩图。

一句话选法：丢不起的进 filesDir，丢了能重新拿的进 cacheDir，用完就删的进 tempDir。拿不准就 filesDir 加自己定期清理——最坏结果是占点空间，不会出功能事故。

##### 读写一个文本文件

来个真实场景：地铁上写的随笔草稿，断网也得留底。这是文件系统的主场，鸿蒙侧用 CoreFileKit 的文件接口：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 沙箱内读写文本文件</span><span class="dots">···</span>
:::

```
import { fileIo as fs } from '@kit.CoreFileKit'
import { Context } from '@kit.AbilityKit'

async function saveDraft(context: Context, text: string) {
  // 路径永远从 context 拼，别手写一串绝对路径
  let path = context.filesDir + '/draft.txt'
  let file = fs.openSync(path,
    fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE | fs.OpenMode.TRUNC)
  fs.writeSync(file.fd, text)
  fs.closeSync(file.fd)
}

async function loadDraft(context: Context): Promise&lt;string&gt; {
  let path = context.filesDir + '/draft.txt'
  if (!fs.accessSync(path)) return ''   // 文件不存在先兜底，别直接读
  return fs.readTextSync(path)
}
```
:::

注意三处细节。<strong>路径从 context 拼</strong>：手写的一串绝对路径，换设备、升系统后多半就不对了，这类 bug 报出来还特别莫名。 <strong>读之前先 access 判断存在</strong>：返回空字符串比抛异常好处理，界面渲染也省一层判断。 <strong>用完 close</strong>：文件句柄和数据库游标一样，泄漏了会慢慢拖垮应用。想追加而不是覆盖，去掉 TRUNC 标志改用追加模式打开就行。

##### 把图片存进图库

沙箱里的图片只有你自己的应用看得见。想让用户在"图库"应用里看到它——比如"保存海报到相册"按钮——要走媒体库接口（photoAccessHelper，对应安卓的 MediaStore、iOS 的照片框架）。

实际写的时候你会遇到一个设计上的巧思：直接调保存接口通常要申请敏感权限，而新版本的推荐做法是用<strong>安全控件</strong>（SaveButton）——把保存动作绑定在用户真实点击的那个按钮上，系统就默认这次操作可信，免去权限弹窗的折腾。接口细节随版本调整，写之前查官方文档，思路是通用的：让"保存"发生在用户的明确点击里。

::: div .code-block
:::inline div .code-head
<span>ARKTS · 把沙箱图片存进图库（示意）</span><span class="dots">···</span>
:::

```
import { fileIo as fs } from '@kit.CoreFileKit'
import { photoAccessHelper } from '@kit.MediaLibraryKit'

// 建议在安全控件 SaveButton 的点击回调里触发；
// createAsset 等接口随版本调整，以官方文档为准
async function saveToGallery(context: Context, srcPath: string) {
  let helper = photoAccessHelper.getPhotoAccessHelper(context)
  let uri = await helper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'jpg')
  let dest = fs.openSync(uri, fs.OpenMode.WRITE_ONLY)
  let src = fs.openSync(srcPath, fs.OpenMode.READ_ONLY)
  fs.copyFileSync(src.fd, dest.fd)
  fs.closeSync(src.fd)
  fs.closeSync(dest.fd)
}
```
:::

反过来"从图库挑一张图"用的是系统选择器那一套，同样不需要裸申请权限。读写图库这件事，三个平台的趋势一致：能用系统选择器、安全控件，就不要伸手要权限——审核更容易过，用户也更放心。

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>避坑提醒

{class="mt-1"}
几个常见的"想当然"：把几 MB 的图片 Base64 之后塞进 Preferences——整个设置文件的读写都会被拖慢；把下载缓存写进 filesDir 从不清理——应用体积膨胀，用户在系统存储页看到你的应用占了好几个 GB；把"必须存在"的文件放进 cacheDir——某天系统清缓存，功能直接崩。目录的分工不是摆设。
:::

##### 删除与清理

删文件用 unlink 接口，删目录有对应的递归删除。两个最值得写的清理点：退出登录时清掉用户目录（下一个人不该看到上一个人的草稿）；启动时顺手清一周前的缓存文件。清理逻辑千万别写"全删"——把配置和缓存混在一个目录里一次清光，用户设置全没了，这种事故在真实项目里出现过不少次。目录分开，就是给未来的自己留后路。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hand-pointer mr-2"></i>来动手

{class="mt-1"}
给你的应用画一张"文件地图"：列出所有会落盘的文件、各自放哪个目录、大概多大、谁负责清理。名单写不出来的应用，多半已经在乱堆文件了。
:::

#### 四、网络请求：GET/POST 完整流程、JSON 解析与错误处理

本地存储解决"记住"，网络请求解决"获取"。鸿蒙内置的 HTTP 客户端在 NetworkKit 里（对应安卓的 OkHttp、iOS 的 URLSession），套路是四步：创建请求对象 → 发请求 → 处理响应 → 销毁对象。

##### 动手前：先声明权限

网络权限要在 module.json5 的 requestPermissions 里声明 INTERNET。忘了声明的话，请求会直接失败而且报错相当隐晦——这是鸿蒙网络开发的第一大翻车点。新建工程跑通第一个请求之前，先检查这一项。

##### GET：拿到一段 JSON

::: div .code-block
:::inline div .code-head
<span>ARKTS · GET 请求完整示例</span><span class="dots">···</span>
:::

```
import { http } from '@kit.NetworkKit'

async function fetchTodos(): Promise&lt;string&gt; {
  let req = http.createHttp()
  try {
    let resp = await req.request(
      'https://api.example.com/todos',
      { method: http.RequestMethod.GET,
        header: { 'Content-Type': 'application/json' },
        connectTimeout: 10000, readTimeout: 10000 })
    if (resp.responseCode === 200) {
      return resp.result as string
    }
    throw new Error('HTTP ' + resp.responseCode)
  } finally {
    req.destroy()   // 放在 finally 里，成败都执行
  }
}
```
:::

逐行拆一遍。<code class="inline">createHttp()</code> 创建请求对象；<code class="inline">request()</code> 发出请求返回 Promise——<strong>接口本身是异步的</strong>，await 等的是结果，不会卡住界面；<code class="inline">responseCode</code> 是 HTTP 状态码，200 之外的情况（404、500、429）都要当成"没拿到数据"来处理；最后 <code class="inline">destroy()</code> 释放连接——不销毁的请求对象会累积泄漏，App 用久了越来越卡，往往就是这类细节攒出来的。

##### POST：提交一段 JSON

::: div .code-block
:::inline div .code-head
<span>ARKTS · POST 请求完整示例</span><span class="dots">···</span>
:::

```
async function createTodo(title: string): Promise&lt;void&gt; {
  let req = http.createHttp()
  try {
    let resp = await req.request(
      'https://api.example.com/todos',
      { method: http.RequestMethod.POST,
        header: { 'Content-Type': 'application/json' },
        extraData: JSON.stringify({ title: title, done: false }),
        connectTimeout: 10000, readTimeout: 10000 })
    if (resp.responseCode !== 200) {
      throw new Error('HTTP ' + resp.responseCode)
    }
    // 很多接口 HTTP 200 只代表"通信成功"，
    // 业务成败还要看响应体里的 code 字段
  } finally {
    req.destroy()
  }
}
```
:::

POST 与 GET 的差别就在 body：<code class="inline">extraData</code> 传字符串时按你给的内容发送（也可以直接传对象，框架会做 JSON 序列化），header 里的 Content-Type 要与之匹配。发完别只看状态码——很多接口"成功"只是 HTTP 层的 200，业务成败藏在响应体的 code 字段里，两层都要判。

##### JSON 解析：别让异常裸奔

拿到的 result 默认是字符串，要自己转对象。JSON 解析是网络层出错最多的一环：服务器返回了 HTML 错误页、字段名和文档不一致、字段取值是 null——任何一种都会让解析直接抛异常。所以解析永远包在 try/catch 里：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 安全解析与字段兜底</span><span class="dots">···</span>
:::

```
interface TodoItem {
  title: string
  done: boolean
}

function safeParseTodos(text: string): TodoItem[] {
  try {
    let obj = JSON.parse(text) as Record&lt;string, object&gt;
    // 别假设字段一定在：可选链 + 类型判断 + 默认值
    let list = obj?.['data'] as TodoItem[] ?? []
    return list.filter(item =&gt; typeof item?.title === 'string')
  } catch (e) {
    console.error('parse todos failed')   // 只打结论，不打完整报文
    return []
  }
}
```
:::

再讲一个习惯：<strong>给每个字段留兜底值</strong>。"接口文档写了就有"？会变的。字段用可选链加默认值，服务器少返回一个字段，页面不至于整体白屏。调试"昨天还好好的今天全崩了"这类问题时，这一招特别救命——十有八九是后端改了字段。

##### 超时与重试：别让用户干等

两个超时参数各管一段：connectTimeout 管"连上服务器"这一步，readTimeout 管"连上后等响应"这一段，都建议显式设置（示例里用了 10 秒），不然默认行为可能让用户对着转圈的界面等很久。

重试要讲纪律。<strong>网络错误、超时、5xx 可以重试</strong>——这类失败重试一次往往就过了；<strong>4xx 别重试</strong>——404 是地址错了，401 是没登录，重试一百次还是这个结果，只白耗用户流量。重试之间加退避（第一次等 1 秒、第二次 2 秒、逐次加倍），连续失败到上限就放弃并提示用户。还有个容易忽略的坑：GET 重试无害，<strong>POST 重试可能造成重复下单、重复发帖</strong>——写操作能不能重试，取决于接口是否幂等，不确定就问后端。

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>三大易错点

{class="mt-1"}
1\. 忘记声明 INTERNET 权限（报错很隐晦）；2. req.destroy() 不调用导致连接泄漏；3. URL 里的中文参数记得 encodeURIComponent，否则请求会直接失败。
:::

再补两条工程习惯：正式接口一律走 https；URL 拼参数时用 encodeURIComponent 编码，中文和特殊字符才不会把请求搞挂。给界面留一层兜底——把上一次成功的结果缓存下来，地铁里没网时展示旧数据并标注更新时间，比一屏空白友好得多。缓存怎么设计，第六节展开。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hand-pointer mr-2"></i>来动手

{class="mt-1"}
把你项目里所有发请求的函数过一遍四问：超时设了吗？destroy 调了吗？JSON 解析有 try/catch 吗？4xx 会误触发重试吗？四问全绿才算过关。
:::

#### 五、网络进阶：请求封装与拦截思路

上一节的写法在 demo 里没问题，真项目里会到处复制粘贴：每个页面都 createHttp、都写超时、都 try/catch、都 destroy——改一处超时要翻十个文件。这时候该做一次封装，把"发请求"这件重复的事收拢到一个模块里。

##### 一个最小的请求封装

::: div .code-block
:::inline div .code-head
<span>ARKTS · 极简 ApiClient</span><span class="dots">···</span>
:::

```
class ApiError extends Error {
  constructor(public code: number, msg: string) { super(msg) }
}

class ApiClient {
  private baseUrl = 'https://api.example.com'
  private token: string = ''   // 登录后由外部注入

  async get(path: string): Promise&lt;object&gt; {
    return this.request(path, http.RequestMethod.GET)
  }

  async post(path: string, body: object): Promise&lt;object&gt; {
    return this.request(path, http.RequestMethod.POST,
      JSON.stringify(body))
  }

  private async request(path: string, method: http.RequestMethod,
    body?: string): Promise&lt;object&gt; {
    let req = http.createHttp()
    try {
      let resp = await req.request(this.baseUrl + path, {
        method: method,
        header: {
          'Content-Type': 'application/json',
          ...(this.token ? { 'Authorization': 'Bearer ' + this.token } : {})
        },
        extraData: body,
        connectTimeout: 10000, readTimeout: 10000
      })
      if (resp.responseCode !== 200) {
        throw new ApiError(resp.responseCode, '请求失败：HTTP ' + resp.responseCode)
      }
      return JSON.parse(resp.result as string) as object
    } finally {
      req.destroy()
    }
  }
}
```
:::

封装之后收益立竿见影：所有请求自动带上统一的 header（登录态、内容类型）、统一的超时、统一的错误转译——调用方拿到的要么是解析好的对象，要么是一个带人类可读信息的 Error。页面代码从二十行请求样板缩成一行。

##### 拦截思路：在封装里加"关卡"

用过安卓 OkHttp 的读者知道 interceptor：请求前后各有一道关卡，可以统一改请求、统一处理响应。鸿蒙的 http 模块没有内置拦截器，但<strong>你的封装层就是拦截器</strong>——在 request 方法内部加两个钩子：

- <strong>请求前</strong>：补上 token（有就加 Authorization 头）、给 URL 拼公共参数、记一条脱敏日志（只打方法、路径，不打完整报文）。
- <strong>响应后</strong>：统一处理 401——收到就清登录态、跳登录页；统一处理 429——提示"操作太频繁"而不是弹一堆报错；判业务码，把"HTTP 成功但业务失败"转成异常抛给调用方。

token 过期自动刷新也是在这层做：收到"凭证失效"的响应，先用 refresh token 换新 token，换到就重放刚才那个请求，用户完全无感。这套机制在三个平台上的设计一模一样——换的只是 API 名字。写的时候注意一点：刷新 token 的请求本身别再走这套拦截逻辑，否则会套娃。

##### 与数据层结合：请求前先问缓存

封装层还有一个价值：把"读缓存还是发请求"的决策也收进来。读接口的统一姿势是"先查缓存，缓存新鲜就直接返回，过期或缺失才发网络请求，成功后回写缓存"。页面调用方完全不用关心数据从哪来——有网没网、快慢与否，界面都有东西可展示。这个模式叫"缓存优先"，下一节把它展开成完整策略。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士

{class="mt-1"}
封装的边界感：ApiClient 只管"通信"，不懂业务。哪些接口要缓存、哪些要排队重发，让上层的数据仓库（Repository）去决定——通信层保持薄，业务层保持清楚，出了问题才知道去哪找。
:::

#### 六、缓存策略：内存缓存、磁盘缓存与过期设计

缓存是存储与网络的交汇处：做得好，应用又快又省流量；做得糙，用户看到三天前的旧数据还以为出了 bug。一套完整的缓存分两层——<strong>内存缓存</strong>与<strong>磁盘缓存</strong>。

##### 两级结构

- <strong>内存缓存</strong>：一个 Map 就能起步，存"本次运行期间反复用"的数据。页面跳来跳去不重复请求，列表返回秒开。代价是应用被杀就没了，所以只当"加速层"。
- <strong>磁盘缓存</strong>：落进 cacheDir 的文件，或者 RelationalStore 里专设的一张缓存表，应用重启还在。它是离线展示的底气——断网时能展示的就是这一层的内容。

读取顺序固定：内存 → 磁盘 → 网络，越靠前越快。命中内存是微秒级，命中磁盘是毫秒级，走网络要几十到几百毫秒甚至更久。写的时候按这个顺序组织代码，别让"查缓存"反而比"发请求"还慢。

##### 过期：旧数据什么时候失效

缓存的难点不在存，在"什么时候扔"。三种常用判据：

- <strong>时间戳（TTL）</strong>：存数据时记下取回时间，读取时超过有效期就当过期处理。资讯、行情这类"越新越好"的数据有效期设短些；头像、Banner 图这类不常变的设长些。
- <strong>版本号或标记</strong>：服务器在响应头或列表首项里带一个"数据版本"，本地版本对不上就整体刷新。适合"服务器说了算"的数据。
- <strong>手动失效</strong>：下拉刷新、退出登录、切换账号时清空相关缓存。切换账号不清缓存，上一个账号的数据漏给下一个账号看——这是真实发生过的安全事故。

不同数据配不同策略，别一刀切。几条经验：用户自己产生的数据（草稿、收藏）以本地为准，永远不随便被网络覆盖；资讯类内容短有效期加下拉强制刷新；图片这类大体积资源长有效期，按 URL 做键存取。切忌把"缓存"做成"只存不删"——cacheDir 里堆出几个 GB，用户清存储时第一个删的就是你。

::: div .code-block
:::inline div .code-head
<span>ARKTS · 两级缓存的最小实现</span><span class="dots">···</span>
:::

```
import { fileIo as fs } from '@kit.CoreFileKit'

class TwoLevelCache {
  private mem = new Map&lt;string, string&gt;()

  async get(context: Context, key: string, ttlMs: number): Promise&lt;string | null&gt; {
    // 1. 内存层
    let hit = this.mem.get(key)
    if (hit) return hit
    // 2. 磁盘层（文件内容形如 {t: 存入时间, v: 数据}）
    let path = context.cacheDir + '/' + encodeURIComponent(key)
    if (fs.accessSync(path)) {
      try {
        let obj = JSON.parse(fs.readTextSync(path))
        if (Date.now() - obj.t &lt; ttlMs) {      // 没过期才可用
          this.mem.set(key, obj.v as string)
          return obj.v as string
        }
        fs.unlinkSync(path)                     // 过期顺手删
      } catch (e) { /* 坏文件当没有 */ }
    }
    return null                                 // 3. 未命中，交给网络层
  }

  async put(context: Context, key: string, value: string): Promise&lt;void&gt; {
    this.mem.set(key, value)
    let path = context.cacheDir + '/' + encodeURIComponent(key)
    let f = fs.openSync(path, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE | fs.OpenMode.TRUNC)
    fs.writeSync(f.fd, JSON.stringify({ t: Date.now(), v: value }))
    fs.closeSync(f.fd)
  }
}
```
:::

##### 误区清单

- 很多人以为"缓存就是把数据存起来"，其实存只是第一步，<strong>过期与清理才是策略的主体</strong>。
- 很多人以为"有缓存就不用处理失败"，其实缓存只是兜底——请求失败要提示"正在展示多久之前的数据"，别让用户误以为是实时结果。
- 很多人以为"缓存越多越快"，其实过期数据堆多了，界面呈现的是一个错误的"现实"——对记账、行情这类应用是致命的。

#### 七、数据同步与离线优先：断网时的展示策略

先说一个反直觉的结论：断网不等于"应用不可用"。地图应用断网了还能看缓存过的区域，笔记应用断网了照样能写——好的应用把"离线"当常态来设计，这个思路叫<strong>离线优先</strong>：界面永远先展示本地数据，网络只在后台悄悄更新它。

##### 读：先展示，再更新

离线优先的读取流程是一套固定动作：打开页面 → 立即渲染本地缓存或数据库里的数据 → 后台发请求 → 拿到新数据更新界面并回写本地。用户感受到的是"秒开"，而不是白屏转圈。和它相反的"在线优先"（先请求再渲染）在网络差时体验惨烈——地铁过隧道那几十秒，页面一片空白。

断网时的展示策略就三条：<strong>展示旧数据</strong>，哪怕标注"2 小时前更新"；<strong>顶部给一条提示</strong>，比如"当前离线，展示的是上次的数据"；<strong>保留重试入口</strong>，一个刷新按钮就够。三条做齐，用户对断网的容忍度会高很多。真正让用户愤怒的不是旧数据，是无解释的空白和转圈。

##### 写：失败的操作先记账，回头补

读有离线策略，写也有：发帖、点赞、勾待办这些操作，断网时不该直接报错收场——把操作先落进本地库，标一个"待同步"状态，界面立刻反馈"已保存，待同步"，网络恢复后再在后台补发。这就是<strong>离线队列</strong>，聊天应用的离线消息、笔记应用的自动保存，都是这个思路。

队列有两个技术要点。<strong>一是幂等</strong>：补发时可能重复发送（发完没等到确认就再发一次），所以要给每条操作一个唯一 ID，服务器端凭 ID 去重，不然会出现重复发帖。<strong>二是顺序</strong>：同一条记录的多次修改要按发生顺序补发，乱序会把"先改成 A 后改成 B"同步成"最后是 A"。落库时带上时间戳或序号，补发前排个序，两行代码防一个大坑。

##### 冲突：两端都改了怎么办

手机端和云端都改了同一条数据，以谁为准？最简单的答案是"最后写入赢"——直接用时间最新的那条覆盖，大多数应用够用。对重要数据（账目、文档），更稳妥的做法是保留双方版本、提示用户手动合并，代价是实现复杂得多。给普通开发者的建议：能用"最后写入赢"就用它，把精力花在"别静默丢数据"上——覆盖前给被覆盖的版本留个底（回收站或历史记录），用户误操作还有救。

##### 判断当前有没有网

NetworkKit 里带网络连接管理（connection 模块），能查询当前是否有可用网络，也能监听网络切换事件——"监听到网络恢复"正是补发离线队列的时机。具体接口名随版本调整，用之前查官方文档。另外提醒一句：查询结果只当参考，真正靠得住的是请求本身的成败——"设备有网"不代表"你的服务器可达"，两件事别混为一谈。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-quote-left mr-2"></i>一句话记牢

{class="mt-1"}
离线优先一句话：界面永远有东西看，操作永远有地方记，网络只是搬运工。
:::

#### 八、安全要点：HTTPS、token 存储与日志脱敏

存储与网络把用户数据聚到了一起，安全必须单独拎出来讲。就三件事：传输要加密、凭证要藏好、日志要脱敏。

##### HTTPS 是底线，不是加分项

正式环境的接口一律走 https。鸿蒙默认禁止明文 HTTP 流量——这是系统替你把的关，别为了"联调方便"全局放开明文；真要调本地服务，用抓包工具的证书方案，测完关掉。还有一条容易被忽略：<strong>证书校验不要绕过</strong>。网上有些"解决证书报错"的代码是直接信任所有证书，那是把中间人攻击的门敞开——自签名证书的正确做法是把自己的证书打包进应用做校验，而不是关掉校验。

##### token 存哪：别用明文键值

登录凭证（token）是应用里最敏感的数据，存放规则很明确：不进 Preferences 明文、不进 RelationalStore 明文、不进日志。鸿蒙侧用<strong>关键资产存储</strong>（Asset Store Kit）这类安全存储服务，由系统加密保管；对应安卓的 Keystore 系方案、iOS 的 Keychain。存的时候顺手做两件事：给 token 设有效期，过期前用 refresh token 换新；用户退出登录时彻底清掉本地凭证——"退出登录只清界面不清数据"的应用，第二天换个用户一打开还是登录态，想想都不舒服。

顺带把第一节 Preferences 的提醒升级成铁律：存储选型的第一问是安全级别——"这份数据泄了会伤到用户吗？"会，就上安全存储；不会，才轮到 Preferences 或数据库。安全分层的意识比记住任何一个 API 名都重要。

##### 日志脱敏：排错与泄密只隔一层纸

日志是开发者的朋友，也是泄密的惯用通道。几个必须养成的习惯：

- <strong>敏感字段打码</strong>：手机号、身份证号、地址，中间几位换星号——既保留排错所需的前后文，又不泄露完整信息。
- <strong>不打完整报文</strong>：请求与响应的 header、body 里常有 token 和用户数据。日志里只记方法、路径、状态码、耗时；要看完整报文，用抓包工具临时看。
- <strong>发布版关掉调试日志</strong>：verbose、debug 级别的日志在正式版本里关闭，只留 error 和 warn。设备连过电脑的用户，日志里可能还留着整段对话。

给爸妈远程排查问题时你会有直观体会：应用日志里能翻出多少东西，取决于开发者偷了多少懒。日志写得多不算错，写得"全"才是错。

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>避坑提醒

{class="mt-1"}
三条红线：明文 http 上生产；token 进 Preferences 或日志；"信任所有证书"应付了事。任何一条被查出来，轻则上架审核不过，重则用户数据泄露。没有例外。
:::

#### 九、常见报错门诊：权限、解析、泄漏一次讲清

存储与网络的报错大多"报得隐晦、错得低级"。把高频病例列成一张门诊表，对号入座能省掉大半排查时间。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">症状</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">多半是</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">处方</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">请求一发就失败，报错信息看不懂</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">忘了在 module.json5 声明 INTERNET 权限</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">补权限声明；改权限要重新安装应用才生效</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">控制台报 JSON 相关异常，界面空白</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">返回的不是预期 JSON：错误页、字段名变了、字段为 null</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">解析包 try/catch；打印返回的前几百个字符看真实内容；字段加可选链兜底</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数据"写进去了，重启就丢"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Preferences 忘了调 flush()</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">put 之后补 flush；把两步封成一个 save 函数锁死</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URL 带中文参数，请求直接失败</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">参数没编码</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">拼进 URL 前用 encodeURIComponent 过一遍</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">App 用久了变卡、网络越来越慢</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">请求对象没 destroy、游标没 close，资源累积泄漏</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">request 与 query 后在 finally 里销毁或关闭</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">列表页一滚动就掉帧</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">主线程里跑同步文件读写或大查询</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">大活挪异步；同步接口只留给小数据</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">请求一直挂着，不返回也不报错</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">没设超时，或服务器真的很慢</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">connectTimeout/readTimeout 显式设置；超时后给明确提示与重试入口</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一断网就重试几十次，被服务器限流</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">无退避的立即重试</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">重试加间隔、设上限；429 与 4xx 不重试</td></tr>
</tbody>
</table>
```
:::

门诊表之外补两句心得。第一句：报错信息别只看前半句——框架错误码只是外壳，真正的原因常在系统日志的后续几行里，翻日志要翻全。第二句：复现优先于修复——"偶尔丢数据"这种问题，没有稳定复现路径就动手改，多半是白改。断网、弱网、杀进程这三类场景，最好在开发期就主动模拟过（怎么模拟，见下面的 FAQ）。

#### 十、三平台对照总结：一套概念，三种方言

本章概念在安卓、iOS、鸿蒙三侧一一对应，把对照表放在这里，你在哪个平台写都能找到"老家"：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">能力</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">安卓</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">iOS</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">鸿蒙</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">键值偏好</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SharedPreferences / DataStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ArkData - Preferences</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">关系型数据库</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room（SQLite）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Core Data / SwiftData</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ArkData - RelationalStore</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">HTTP 客户端</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OkHttp / Retrofit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">NetworkKit - http</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">安全存储</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Keystore 系方案</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Keychain</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">关键资产存储（Asset Store Kit）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">文件目录</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">内部存储私有目录 + cache</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Documents / Caches</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">filesDir / cacheDir / tempDir</td></tr>
</tbody>
</table>
```
:::

看出规律了吗：每一层都是"同名异形"——轻量键值、关系库、HTTP 客户端、安全存储，学通一个平台，另外两个是换语法。迁移思路也一致：先定数据形态（键值、结构化、文件），再选存储；先定接口形态，再封装网络层；缓存与离线策略几乎可以原样照搬。跨平台开发的底气不在背 API，在这套分层。

鸿蒙这一侧再补一张"按存什么选工具"的速查表，把本章内容收拢：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要存什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">用什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">一句话</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一个开关、一点小设置</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ArkData - Preferences</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">键值型轻量配置，记得 flush</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">结构化记录（列表、账本）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ArkData - RelationalStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SQLite 关系库，适合查询与排序</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">文件与图片、下载缓存</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">文件管理 / 应用沙箱路径</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">丢不起的进 filesDir，能再拿的进 cacheDir</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">登录凭证等敏感数据</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">关键资产存储</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">别进 Preferences，别进日志</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">HTTP 请求</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">NetworkKit - http</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">注意权限、超时与错误码</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分布式键值数据</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分布式数据对象 / KV Store</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">跨设备同步场景（第 79 章展开）</td></tr>
</tbody>
</table>
```
:::

最后照例提醒版本问题：Kit 的 API 会随版本调整。鸿蒙的版本节奏在加快——HarmonyOS 6 在 2025 年 10 月发布时首批就有 90 多款机型公测，7.0（2026 年 9 月发布）也已落地，ArkData、NetworkKit 的接口细节都可能跟着变。每次升级 SDK，先用 DevEco 里的 API Change Assistant 把工程扫一遍（[Tools] → [API Change Assistant]），改完再跑。

::: div .tip-box .rounded-lg .p-4 .mb-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>一句话记牢

{class="mt-1"}
三大平台到这里可以对齐了：安卓 Room/DataStore、iOS SwiftData/UserDefaults、鸿蒙 RelationalStore/Preferences——都是「结构化」与「小设置」两分。
:::

#### 十一、常见问题（FAQ）

收尾前的八问八答，都是后台真实出现过的问法。

<strong>问：服务器返回的列表数据，我该存 Preferences 还是数据库？</strong>

答：存数据库。列表是"结构化、会增长、要查询排序"的数据，归 RelationalStore 管；Preferences 只装"几十个设置项"这个量级。判断口诀：会翻页、要筛选、条数会涨的进数据库；一两个开关、一个字符串进 Preferences。装错了地方，早期没感觉，数据一多天天卡。

<strong>问：我明明 put 了，为什么重启应用数据就没了？</strong>

答：九成是忘了 flush()。put 只改了内存里的对象，flush 才落盘。把"put + flush"封成一个函数，从此告别这类玄学。另外检查一下是不是每次都新建了 Preferences 实例——两个实例各写各的，互相覆盖。

<strong>问：POST 请求返回成功，服务器却收不到我传的参数？</strong>

答：先查两处：extraData 有没有真的传进去（发送前打印一眼序列化结果）；header 的 Content-Type 是不是 application/json——服务器按 JSON 解析，你发的却不是合法 JSON，字段自然全丢。还有一类是服务器要表单格式，Content-Type 得改成对应类型，这要看接口文档，别靠猜。

<strong>问：token 到底存哪才算安全？</strong>

答：优先级是：安全存储（鸿蒙关键资产、iOS Keychain、安卓 Keystore 系）＞ 加密后进普通存储 ＞ 明文进普通存储（别用）。同时守住另外两条：不进日志；退出登录彻底清。做到这三点，token 的存放就超过市面上不少应用了。

<strong>问：断网的时候，我的应用应该显示什么？</strong>

答：按优先级：本地缓存的数据（标注更新时间）＞ 一个解释清楚的空状态（"离线中，联网后自动更新"加刷新按钮）。最差的选择才是白屏或连环报错弹窗。断网不是异常状态，是日常状态——用户在电梯里、地下车库都会遇到。

<strong>问：缓存设多久过期合适？用户看到旧数据会不会生气？</strong>

答：看数据性质：资讯类几分钟到几十分钟；头像、配置类几小时到几天；用户自己的数据永远以本地为准。用户生气的其实不是"旧"，是"没说明"——标注"X 分钟前更新"，旧数据就是诚实的数据；不标注，旧数据就是 bug。

<strong>问：鸿蒙这些 API 会不会过两年就变？现在学是不是白学？</strong>

答：接口细节会随版本调整（每次升 SDK 跑一遍 API Change Assistant 就是干这个的），但本章讲的东西大半不是接口：分层选型、缓存策略、离线优先、安全习惯——这些在安卓和 iOS 上同样适用，换了平台照搬思路。学的是"怎么想"，API 只是"怎么说"。

<strong>问：没有网的环境怎么测离线功能？总不能真跑去没信号的地方吧？</strong>

答：不用。真机开飞行模式就是最可靠的断网模拟，恢复联网也是一秒的事。要模拟"网络抖动"，就"飞行模式开几秒再关"，反复几次。测三件事：断网时界面有没有兜底、网络恢复后离线队列会不会补发、更新时间标注对不对。这三关过了，离线体验基本及格。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hand-pointer mr-2"></i>来动手

{class="mt-1"}
综合练习：写一个"迷你离线笔记"——笔记本体存 RelationalStore，草稿文件存 filesDir，配图缓存进 cacheDir，列表页走"缓存优先"，断网可编辑、联网自动补传（补传带唯一 ID 防重复）。做完这一套，本章就真正属于你了。
:::

#### 十二、实战串讲：一笔数据从接口到界面的完整旅程

零件都讲完了，现在把它们拼成一台整机。场景：你在写一个记账应用，用户点"记一笔"，输入"早餐 12 元"。这一下点击背后要发生什么？咱们顺着这笔数据的一生走一遍。

分层约定先立好：UI 层（页面与组件）只跟数据仓库（Repository）说话；Repository 决定"读缓存、读库还是发网络"；网络层（第五节封装的 ApiClient）只管通信；存储层（Preferences、RelationalStore、文件）各归各位。UI 不直接碰 http，网络层不懂业务——这条边界守住，后面出的每一个问题都有明确的责任人，排查时不用满工程翻。

##### 数据仓库：本地为主，网络为辅

::: div .code-block
:::inline div .code-head
<span>ARKTS · 记账数据仓库 ExpenseRepository</span><span class="dots">···</span>
:::

```
interface Expense {
  id: number
  note: string
  amount: number
  synced: number   // 0 待同步，1 已同步
}

class ExpenseRepository {
  private api = new ApiClient()
  private rdb: relationalStore.RdbStore | null = null

  async init(context: Context) {
    this.rdb = await relationalStore.getRdbStore(context, {
      name: 'expense.db',
      securityLevel: relationalStore.SecurityLevel.S1
    })
    await this.rdb.executeSql(
      'CREATE TABLE IF NOT EXISTS expense (' +
      'id INTEGER PRIMARY KEY AUTOINCREMENT, ' +
      'note TEXT, amount INTEGER, synced INTEGER)')
  }

  // 记一笔：先落库（用户的意志，必须立刻成功），再尝试同步（服务器的意愿，失败可等）
  async addExpense(note: string, amount: number) {
    await this.rdb?.executeSql(
      'INSERT INTO expense (note, amount, synced) VALUES (?, ?, 0)',
      [note, amount])
    try {
      await this.api.post('/expenses', { note: note, amount: amount })
      await this.rdb?.executeSql(
        'UPDATE expense SET synced = 1 WHERE synced = 0')
    } catch (e) {
      // 断网或超时：记录留在库里，等离线队列补发，不打扰用户
    }
  }

  async listExpenses(): Promise&lt;Expense[]&gt; {
    let out: Expense[] = []
    let rs = await this.rdb?.querySql(
      'SELECT id, note, amount, synced FROM expense ORDER BY id DESC LIMIT 100')
    while (rs!.goToNextRow()) {
      out.push({
        id: rs!.getLong(rs!.getColumnIndex('id')),
        note: rs!.getString(rs!.getColumnIndex('note')),
        amount: rs!.getLong(rs!.getColumnIndex('amount')),
        synced: rs!.getLong(rs!.getColumnIndex('synced'))
      })
    }
    rs?.close()
    return out
  }

  // 网络恢复后补发所有待同步记录
  async flushQueue() {
    let rs = await this.rdb?.querySql('SELECT id, note, amount FROM expense WHERE synced = 0')
    while (rs!.goToNextRow()) {
      let id = rs!.getLong(rs!.getColumnIndex('id'))
      let note = rs!.getString(rs!.getColumnIndex('note'))
      let amount = rs!.getLong(rs!.getColumnIndex('amount'))
      try {
        await this.api.post('/expenses', { note: note, amount: amount, clientId: id })
        await this.rdb?.executeSql('UPDATE expense SET synced = 1 WHERE id = ?', [id])
      } catch (e) {
        break   // 仍然失败：保留记录，下次再试
      }
    }
    rs?.close()
  }
}
```
:::

注意 addExpense 的顺序：先写库、再同步。写库代表"用户要记这笔账"，必须立刻成功；同步代表"这笔账要上云"，失败可以等。顺序反过来，断网时用户连账都记不了——离线优先就落空了。clientId 把本地 id 带给服务器做幂等去重，正是第七节说的"补发防重复"。

金额用整数存（单位是"分"而不是"元"），这是记账类应用的经典细节：浮点数算钱会出"0.1 加 0.2 不等于 0.3"的精度问题，用整数分就绕开了。统计营业额也是一条 SQL 的事：

::: div .code-block
:::inline div .code-head
<span>ARKTS · 一条 SQL 算今日营业额</span><span class="dots">···</span>
:::

```
async function todayTotal(rdb: relationalStore.RdbStore, dayStart: number): Promise&lt;number&gt; {
  let rs = await rdb.querySql(
    'SELECT SUM(amount) AS t FROM expense WHERE id &gt; ? AND synced IN (0, 1)',
    [dayStart])
  let total = rs.getLong(rs.getColumnIndex('t'))
  rs.close()
  return total
}
```
:::

##### 页面：先展示本地，再后台刷新

::: div .code-block
:::inline div .code-head
<span>ARKTS · 页面接入数据仓库</span><span class="dots">···</span>
:::

```
@Entry
@Component
struct BookPage {
  @State list: Expense[] = []
  @State offline: boolean = false
  private repo = new ExpenseRepository()

  async aboutToAppear() {
    await this.repo.init(getContext(this) as Context)
    this.list = await this.repo.listExpenses()   // 秒开：先给本地数据
    this.refreshFromNet()                        // 再悄悄更新
  }

  async refreshFromNet() {
    try {
      await this.repo.flushQueue()
      this.list = await this.repo.listExpenses()
      this.offline = false
    } catch (e) {
      this.offline = true   // 顶部提示条：离线中，展示上次数据
    }
  }

  build() {
    Column() {
      if (this.offline) {
        Text('当前离线，展示的是上次的数据').fontSize(12)
      }
      Button('记一笔 早餐 12 元').onClick(async () => {
        await this.repo.addExpense('早餐', 1200)   // 单位：分
        this.list = await this.repo.listExpenses()
      })
      List() {
        ForEach(this.list, (item: Expense) =&gt; {
          ListItem() {
            Text(item.note + ' ¥' + (item.amount / 100).toFixed(2))
          }
        }, (item: Expense) =&gt; item.id.toString())
      }
    }
  }
}
```
:::

对着代码复盘一遍，本章每个零件都有了位置：Preferences 存"上次选的账本"，RelationalStore 存支出记录与同步状态，cacheDir 存小票照片的缓存，ApiClient 管通信，flushQueue 管离线补发，页面三态（空态、加载态、离线态）齐备。没有哪个零件多余，也没有哪个零件身兼两职。

真正写起来，你遇到的第一批麻烦几乎都在"边界"上：页面等不及异步结果（@State 配合 await，先渲染空态再填数据）；格式转换散落在页面里（时间字符串转 Date、金额分转元）——把这些收进 model 层统一处理，页面只管展示。仓库层的函数保持"一个动作一个函数"，页面需要什么组合什么，别让页面直接写 SQL。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-quote-left mr-2"></i>一句话记牢

{class="mt-1"}
UI 说话，仓库决策，网络跑腿，存储落袋——四层各干各的，数据才有条不紊。
:::

#### 十三、按人群设计数据方案：学生、小商家与爸妈

同一套 API，不同人群的数据形态完全不同。选型错了，后面全是补丁。拿三类典型用户把"大小、是否上云、丢不丢得起"这三问过一遍。

##### 学生：单词卡应用

数据全本地、不需要登录、卡片量几千张以内。方案最简单：RelationalStore 单表（正面、背面、掌握度、下次复习时间），Preferences 存每日目标，完成。没有网络层就没有网络问题——别为了"同步到云端"这个想象中的功能提前设计，等真有需求再加，加的时候也就是给表补一个 synced 列的事。

值得多花心思的是导出：做一个"导出卡组为文件"的功能，写到 filesDir 再用系统分享发出去。它既是备份，也是社交货币——学生爱把卡组传给同学，一份能被分享的数据，比一百句营销文案都拉新。

##### 小商家：订单本与流水账

数据要上云、要统计、还怕断网——摊位在地下商场，信号说没就没。方案是本章全套：RelationalStore 存订单，ApiClient 加离线队列保证"有没有网都能开单"，网络恢复后补传（幂等 ID 必须有，重复开单对小商家是真金白银的事故）。统计直接用 SQL："今天的营业额"就是一条 SUM，别把全部订单读出来在代码里循环加，订单一多就慢。

再加一条打烊流程：每天收摊跑一次"本地与云端对账"，待同步记录数大于零就提示补传，连续几天对不平就导出文件人工核对。宁可多提醒，也别静默少记一笔——对做小生意的人，账差一元都是大事。

##### 爸妈：相册整理类应用

数据是大图片，操作要大字、少步骤。方案里文件系统唱主角：原图进 filesDir 分目录管理，缩略图进 cacheDir，列表页只加载缩略图——千万别在列表里直接解码原图，几张稍大的照片就能把内存吃满，表现就是滑动一顿一顿的。权限能不要就不要：不申请图库全量访问，保存进相册走安全控件（第三节讲过）。

还有一条隐藏需求：卸载重装，照片还在吗？沙箱数据随卸载清空，所以要么引导一次"备份到云端"，要么在首次使用时就讲清楚"照片存在应用里，卸载会没"。这句提醒放进引导页只占一行字，省掉的是事后翻遍设置也找不回照片的抓狂。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">人群</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">数据特点</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">方案要点</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">学生</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">小体量、全本地、爱分享</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">单表 + Preferences + 导出文件</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">小商家</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">要上云、要统计、环境断网</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">离线队列 + SQL 统计 + 对账</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">爸妈</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">大文件、怕丢、操作要简单</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">文件分层 + 缩略图缓存 + 明示备份</td></tr>
</tbody>
</table>
```
:::

对照着看规律就出来了：数据的"大小、是否上云、丢不丢得起"三个问题定了，方案基本就定了。做新应用先回答这三问，再动手建表——顺序反了，就是在给错误的地基砌墙。

#### 十四、调试工具箱：日志、抓包与断点

数据层的 bug 大多"看不见"——数据藏在库里、跑在网上，肉眼瞧不见。工具箱得备齐三样：日志看结论，抓包看真相，断点看过程。

##### HiLog：打对地方，打少一点

鸿蒙侧日志用 HiLog（对应安卓的 Logcat、iOS 的 os_log）。三个要点：级别收敛——发布版只留 warn 以上；tag 固定命名（比如按模块叫 DATANET），DevEco 的 Log 窗口按 tag 一过滤，一片干净；error 级别要打"发生了什么加关键参数"，但敏感字段打码——第八节的红线在这里执行。

::: div .code-block
:::inline div .code-head
<span>ARKTS · HiLog 的 public 与 private</span><span class="dots">···</span>
:::

```
import { hilog } from '@kit.PerformanceAnalysisKit'

const TAG = 'DATANET'
hilog.info(0x0000, TAG, 'list refreshed, count=%{public}d', this.list.length)
// 占位符默认按 private 处理，参数值会被打码成 &lt;private&gt;
// 需要"看得见"的参数要显式声明 %{public}——
// 这个设计正好提醒你：每一个可见的日志字段，都应该是你确认过不敏感的
hilog.error(0x0000, TAG, 'sync failed for id=%{public}d, retry later', this.lastId)
```
:::

这个"默认打码、显式公开"的设计值得夸：它把"日志要不要脱敏"从自觉变成了机制。你写日志时被迫逐个字段想一遍"这个能公开吗"，想不明白的就让它保持打码——正好。

##### 抓包：看清请求的真相

接口调试的终极大招是抓包：电脑上跑 Charles、mitmproxy 这类工具，手机连同一网络并把代理指过去，装上工具的证书，请求与响应的原文一览无余。"服务器到底返回了什么""我的 header 带没带上 token""这个字段到底叫 name 还是 title"，一眼见分晓。注意两件事：装抓包证书只用于你自己的调试，发布的版本绝不带上任何"信任抓包证书"的代码；在公司或校园网络里抓包前先问一下管理员，别给自己惹麻烦。

##### 断点、计时与弱网模拟

逻辑 bug 用断点：DevEco 的调试器能在 Repository 里断下来，看变量、单步走，比打十行日志都快。性能问题用计时：给 ApiClient 的 request 前后各记一个时间，把每个请求的耗时打进日志，"哪个接口慢"就不用猜了。

::: div .code-block
:::inline div .code-head
<span>ARKTS · 给请求加耗时统计</span><span class="dots">···</span>
:::

```
let start = Date.now()
let resp = await req.request(url, options)
hilog.info(0x0000, TAG, '%{public}s cost=%{public}d ms', path, Date.now() - start)
```
:::

断网与弱网的模拟：真机开飞行模式，一开一关就是最真实的断网与恢复；开发板上可以直接断开网络。想模拟更细的"高延迟、低带宽"，看工具与版本支持，没有条件就"飞行模式两秒再关"反复几次——很多"偶发同步失败"就是这么复现出来的。DevEco 的性能分析工具（Profiler）能看 CPU、内存曲线，排查"是不是图片缓存把内存吃满了"这类问题时用得上。

#### 十五、数据库进阶：索引、分页与并发

第二节把 RelationalStore 用起来了，这一节往前再走半步：数据量从几百条涨到几万条之后，怎么让查询不变慢、写入不冲突。

##### 索引：给常用的查询条件建

表的记录一多，每次查询都要翻全表——索引就是给常用的筛选列做的"目录"。给哪些列建？看你的 WHERE 和 ORDER BY：经常按日期查、按状态筛的列值得建；很少出现在条件里的列不建。索引不是越多越好，每个索引都会拖慢写入、占用空间。

::: div .code-block
:::inline div .code-head
<span>ARKTS · 建索引与分页查询</span><span class="dots">···</span>
:::

```
// 建表语句里没有的索引，用 IF NOT EXISTS 单独建（放在迁移里执行）
await rdb?.executeSql(
  'CREATE INDEX IF NOT EXISTS idx_expense_synced ON expense (synced)')
await rdb?.executeSql(
  'CREATE INDEX IF NOT EXISTS idx_expense_note ON expense (note)')

// 分页查询：每页只取一页的量，翻页用 OFFSET
async function pageExpenses(page: number, size: number): Promise&lt;Expense[]&gt; {
  let rs = await rdb?.querySql(
    'SELECT id, note, amount FROM expense ORDER BY id DESC LIMIT ? OFFSET ?',
    [size, page * size])
  let out: Expense[] = []
  while (rs!.goToNextRow()) {
    out.push({
      id: rs!.getLong(rs!.getColumnIndex('id')),
      note: rs!.getString(rs!.getColumnIndex('note')),
      amount: rs!.getLong(rs!.getColumnIndex('amount')),
      synced: 1
    })
  }
  rs?.close()
  return out
}
```
:::

查询习惯再补三条：SELECT 后写具体列名，别一路 SELECT *；列表页永远配 LIMIT，不给"一次取十万条"留机会；统计交给 SUM、COUNT 这些聚合函数，别把原始数据搬回代码里算。

##### 并发与事务：批量写要打包

ArkTS 是单线程模型，但数据库的异步写入可以并发发起——十个"插入"同时飞过去，SQLite 在底层排队，效率还不低。真正要操心的是"批量"：一口气插几百条，一条条写就是几百次落盘等待，包进一个事务里就是一次。差别的量级在数据一多时非常明显。

::: div .code-block
:::inline div .code-head
<span>ARKTS · 事务批量插入</span><span class="dots">···</span>
:::

```
async function importExpenses(batch: Expense[]) {
  try {
    this.rdb?.beginTransaction()
    for (let e of batch) {
      await this.rdb?.executeSql(
        'INSERT INTO expense (note, amount, synced) VALUES (?, ?, 0)',
        [e.note, e.amount])
    }
    this.rdb?.commit()      // 全部成功才提交
  } catch (err) {
    this.rdb?.rollBack()    // 任何一条失败，整体回滚，不留半截数据
  }
}
```
:::

事务的语义也顺带讲清：要么全成，要么全不成。导入备份文件、批量同步这类"中间态不能见人"的操作，都该包在事务里。半截数据比全失败更可怕——用户分不清哪些导进去了哪些没有。

#### 十六、版本升级与数据迁移：别把用户的数据弄丢

应用要迭代，数据结构也要跟着长。升级最怕的不是崩溃，是"老用户升级后数据全没了"——这种事故只要发生一次，评价区就再也删不掉那条差评。

##### 数据库迁移：版本号 + 分步执行

思路在第二节埋过伏笔：给数据库配一个版本号（存进 Preferences），每次启动对比"代码里的目标版本"和"库的当前版本"，缺哪级补哪级。迁移语句必须向后兼容：只加列、加表，不改名、不删列、不改变量含义。

::: div .code-block
:::inline div .code-head
<span>ARKTS · 迁移阶梯</span><span class="dots">···</span>
:::

```
const DB_VERSION = 2

async function migrateIfNeeded(context: Context) {
  let meta = await preferences.getPreferences(context, { name: 'db_meta' })
  let current = (await meta.get('version', 1)) as number
  if (current &gt;= DB_VERSION) return

  if (current &lt; 2) {   // v1 -&gt; v2：新增"备注"列
    await rdb?.executeSql('ALTER TABLE expense ADD COLUMN remark TEXT')
  }
  // if (current &lt; 3) { ... 未来的 v2 -&gt; v3，照这个格式接着写 ... }

  await meta.put('version', DB_VERSION)
  await meta.flush()
}
```
:::

注意迁移是一个有序阶梯，从用户所在版本逐级爬到最新——不能只写"上一级到最新"这一级，因为老用户可能跨好几个版本一次升到位。迁移执行完先做一轮冒烟验证（建表都在、关键查询能跑通），再放行后续启动流程；验证不过就把用户引到"恢复备份"路径上，别硬着头皮往下走。

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>避坑提醒

{class="mt-1"}
动手迁移前先备份：把要动的表导出一份临时文件（放 tempDir），迁移成功再删。迁移代码本身也会写错——有备份，错了还能重来；没备份，错了就是事故。
:::

##### Preferences 的结构变更

键名要改名时（比如 theme 改成 dark_mode），读的时候先读新键、没有再读旧键，读到旧键就顺手写回新键——一个兼容函数管掉所有历史包袱。更省事的做法是从第一天就统一键名常量，散落字符串键名的问题在第一节说过，这里是它的事后补救版。

##### 备份与恢复：给用户留退路

迁移防的是"升级弄丢"，备份防的是"换机弄丢"。最简实现：把关键表导出成一个 JSON 文件，用系统的文件选择器让用户挑保存位置；恢复时读回来，先校验结构再入库。校验别省：字段类型、条数、关键键都在不在，对不上就提示"文件可能不完整"，宁可拒绝恢复也别把坏数据灌进库。

::: div .code-block
:::inline div .code-head
<span>ARKTS · 导出与校验导入（骨架）</span><span class="dots">···</span>
:::

```
async function exportAll(): Promise&lt;string&gt; {
  let list = await repo.listExpenses()
  return JSON.stringify({ app: 'expense', version: 1, items: list })
}

async function importAll(text: string): Promise&lt;number&gt; {
  let obj = JSON.parse(text) as Record&lt;string, object&gt;
  // 校验：来源对不对、结构全不全，不对就拒绝
  if (obj?.['app'] !== 'expense') throw new Error('不是本应用的备份文件')
  let items = obj?.['items'] as Expense[] ?? []
  if (items.length === 0) throw new Error('备份里没有数据')
  await importExpenses(items)   // 上一节的事务批量插入
  return items.length
}
```
:::

备份文件里的 version 字段也别忘了：将来备份格式变了，恢复逻辑先看版本再决定怎么解析——数据库有迁移阶梯，备份文件同样要有。

#### 十七、上线前的数据层体检清单

发布不是终点，是"数据开始累积"的起点。上线前照着清单过一遍，能挡住大部分上线后才暴露的问题——清单不长，每一条都是踩过坑换来的。

1. <strong>启动路径上的 IO 数一遍</strong>：从 EntryAbility 启动到首页渲染，同步读写了几个文件、跑了几次全表查询？每多一次，首屏就慢一分。
2. <strong>flush、close、destroy 全部在位</strong>：全局搜一遍代码确认。这三处是"用久了变卡"的头号来源。
3. <strong>所有请求都有超时与失败兜底</strong>：没有超时的请求等于没有刹车，界面会一直转圈。
4. <strong>缓存有上限与清理机制</strong>：cacheDir 的清理逻辑真的跑过吗？跑一次确认会删、删对了。
5. <strong>敏感数据检查</strong>：token 与用户资料不在 Preferences 明文里、不在日志里，安全存储在用。
6. <strong>迁移阶梯完整</strong>：拿一个老版本数据库的备份，在真机上把升级流程完整走一遍。
7. <strong>批量写用了事务</strong>：导入、同步这类批量操作，确认包在事务里且失败会回滚。
8. <strong>离线队列的幂等与顺序</strong>：clientId 带了吗？补发按时间排序了吗？重复补发一次验证去重。
9. <strong>三态齐全</strong>：每个列表页都有空态、加载态、错误态，断网有提示条与刷新按钮。
10. <strong>更新时间标注</strong>：所有"缓存优先"的页面都标注了数据的取回时间。
11. <strong>备份与恢复走一遍</strong>：导出的文件能在另一台设备上完整恢复吗？校验逻辑拦得住坏文件吗？
12. <strong>日志发布级收敛</strong>：debug 级日志在正式版关掉，error 日志不带敏感参数。

清单里第一条展开说两句。启动 IO 的收敛有惯用招：首页必需的数据（最近几条记录、用户设置）异步并行加载，非必需的（统计汇总、缓存预热）推迟到首页渲染完之后，或者干脆等用户用到时再加载。判断标准很简单：用户点开图标到看见内容之间，你的应用做了哪些"其实可以晚点做"的事？把它们挪到后面，首屏速度立刻不一样。

第十一条也值得强调：备份恢复是"数据层最后的体面"——前面所有努力防的是概率，备份防的是绝望。真机、模拟器各走一遍导出导入，十分钟的事，换来的底气是"用户数据真的丢不了"。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hand-pointer mr-2"></i>来动手

{class="mt-1"}
把清单打印出来贴在工位上（或存成项目的 issue 模板）。每次发版前逐条打勾，打不完不发版——三个月后你会回来谢这份清单。
:::

#### 十八、误区清单：八个"想当然"

收尾用一份误区清单收束本章。每一条都是"很多人以为 X，其实 Y"，也都是真实项目里用返工换来的。

- 很多人以为"调了写入接口数据就安全了"，其实 put 要 flush、写文件要 close、批量写要事务——每一步都有"看起来成功了其实没落盘"的陷阱。
- 很多人以为"接口文档就是真理"，其实文档滞后于代码是常态——字段兜底、安全解析、以实际返回为准，才是对接口的正确态度。
- 很多人以为"缓存越多应用越快"，其实没有过期与清理的缓存，堆出来的是错误的数据和膨胀的体积——缓存策略的重点在"扔"不在"存"。
- 很多人以为"断网是异常状态"，其实对手机应用，断网是日常——离线优先不是高级优化，是及格线。
- 很多人以为"日志随便打，反正没人看"，其实日志是用户数据的一部分，脱敏做不好，排错工具就是泄密工具。
- 很多人以为"数据库自己会处理好一切"，其实并发批量写要靠事务排队，游标要手动关，迁移要自己写——SQLite 给你的是能力，不是保险。
- 很多人以为"重试越多越可靠"，其实无退避的重试是给服务器添乱，也是给用户耗电——重试要挑对象（4xx 免谈）、要加间隔、要设上限。
- 很多人以为"先跑起来再考虑安全"，其实 token 放错了地方、日志打了明文，事后迁移的代价比一开始就做对大得多——安全是地基，不是装修。

到这里，存储与网络这条主线就走完了：Preferences、RelationalStore、文件、http 四件套，缓存、离线、安全三层设计，外加一条"从接口到界面"的完整链路和一份发版前的体检清单。这些零件会在后面的章节里被真正组装成完整的应用——你在这一章攒下的每一层理解，到那时都会派上用场。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-quote-left mr-2"></i>一句话记牢

{class="mt-1"}
数据的事没有玄学：落盘有凭据（flush）、传输有兜底（超时）、累积有清理（过期）、升级有阶梯（迁移）——四道门都关好，数据才真正属于你。
:::

#### 十九、三个故障现场复盘：弱网、限流与换机

策略写在文档里都头头是道，真出了事才知道靠不靠谱。挑三个最常见的故障现场，把"当时发生了什么、代码该怎么接"复盘一遍——以后你遇到同类场景，可以直接对号入座。

##### 现场一：早高峰地铁，过隧道那几十秒

用户在地铁上打开你的应用，列车进隧道，网络断了。此时此刻界面上应该出现什么？如果做的是"在线优先"：请求发出去，转圈，隧道里一直转，用户盯着一个空白页面四十秒，退出，卸载。如果做的是"离线优先"：列表从本地库里秒出，顶部一条小字"当前离线，展示的是上次的数据"，用户照样能翻、能搜、能收藏——网断了，应用没断。

代码层面复盘，这里做对了三件事。请求失败没有弹错误弹窗——弹窗会把"小插曲"放大成"大事故"，只是把提示条翻出来，用户甚至可能没注意。列表数据来自本地库而不是内存——应用被系统杀掉重启，断网状态下依然有东西可展示。恢复网络后自动刷新——不用用户点重试，界面悄悄换上新数据，提示条收起来，全程无感。

如果你接手的项目还没做这套，改造顺序是：先给列表页加本地读取（哪怕只是把接口结果存进一张表），再加提示条，最后做自动刷新。第一步就能挡掉大半差评，剩下两步锦上添花。

##### 现场二：大促凌晨，服务器顶不住了

营销活动零点开场，服务器压力陡增，接口开始大面积超时、返回限流状态码。你的应用这边，用户看页面卡，就疯狂点刷新——每一次点击都是一个新请求，服务器雪上加霜，你的用户被限流得更彻底。这是一场双输的循环，打断它的责任在客户端。

复盘要点有三层。界面上，请求进行中把按钮置灰，防抖处理——一个用户连点十下，只该发出去一个请求。策略上，429 与 5xx 这类"服务器忙"的失败不做自动重试，提示"系统繁忙，稍后再试"就停手；自动重试只留给超时与网络错误，并且带上退避与上限。话术上，给用户一个预期——"正在重试（第 2 次，共 3 次）"远比无限转圈让人安心，用户知道系统在干活，也知道什么时候该自己动手。

写操作在这种场景下要更谨慎：下单、支付这类请求失败后，别在客户端反复重发，先查本地"待同步"记录里这笔单子在不在，在就不发——宁可让用户手动点一次"确认状态"，也不能冒重复下单的风险。第七节说的幂等 ID，在抢购场景里不是最佳实践，是保命的。

##### 现场三：换了新手机，数据搬家

用户换了新手机，装上你的应用，第一件事是找旧数据。如果应用从没做过备份功能，用户只能眼睁睁看着几年的记录留在旧手机里——沙箱数据随卸载清空，换机助手对第三方应用沙箱的搬运动作视机型与工具而定，不能赌。这一课的教训是：备份功能不是锦上添花，是有"换机"这个高频场景兜底的必需品。

现场的正确流程应该长这样：旧机上，用户点"导出备份"，应用把关键表打包成 JSON 文件，通过系统文件选择器存到用户指定的位置（网盘、别的手机都行）；新机上，用户点"导入备份"，应用先校验文件来源与结构，再用事务把数据批量入库，最后展示一个确认页——"共恢复 1,204 条记录"，条数对得上，用户抽查几条都在，搬家才算完成。

实现上的三个细节前面都讲过，这里串一遍：导出文件带 version 字段（第十六节）；导入走"校验在前、事务在后"（第十五、十六节）；确认页的条数来自导入函数的返回值而不是拍脑袋。把这三处接起来，"换机丢数据"这类客服工单就基本绝迹了。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">现场</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">考验的能力</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">本章对应</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">地铁断网</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">缓存优先、离线展示、自动恢复</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第六、七节</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">服务器限流</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">防抖、退避重试、幂等</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第四、五、七节</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">换机搬家</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">导出、校验、事务导入</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第三、十五、十六节</td></tr>
</tbody>
</table>
```
:::

三个现场串起来看，处理思路高度一致：网络依赖都有本地路径，失败提示都说人话，重要数据都有搬家方案。把这三句话写进团队的代码评审清单，多数"线上突发故障"会在评审阶段就被拦下。

#### 二十、本章速查：常用片段与关键 API 索引

写代码时最常翻回本章找的，其实是"那个 API 叫什么来着"。把它们按动作收进一张速查表，配上一行要点，用的时候先来这里，再进正文看细节。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要做什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">关键 API</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">别忘了</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">存一个设置项</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">preferences.getPreferences + put + flush</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">flush 不调可能不落盘</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">建库建表</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">relationalStore.getRdbStore + executeSql</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">CREATE TABLE IF NOT EXISTS</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">查询数据</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">querySql + goToNextRow</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用完 close 游标</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">批量写入</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">beginTransaction / commit / rollBack</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">失败要回滚</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">读写文件</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">fs.openSync / writeSync / readTextSync</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">路径从 context 拼，句柄要关</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">图片存图库</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">安全控件 + photoAccessHelper</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">绑用户点击，接口随版本调整</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">发 GET/POST</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">http.createHttp + request</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">先声明 INTERNET 权限，finally 里 destroy</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">解析 JSON</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">JSON.parse 包 try/catch</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">字段可选链 + 默认值</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">磁盘缓存</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">cacheDir + 时间戳</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">过期就删，别只存不清</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">判断网络</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">connection 模块查询与监听</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">只当参考，以请求结果为准</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">存 token</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">关键资产存储（Asset Store Kit）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不进 Preferences，不进日志</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">打日志</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">hilog.info / error</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">公开参数显式 %{public}，默认打码</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">升级表结构</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">version 键 + ALTER TABLE</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">阶梯式迁移，动手前先备份</td></tr>
</tbody>
</table>
```
:::

速查表之外，还有三个"用的时候才想起"的小细节，单独列在这里。其一，URL 拼参数前过一遍 encodeURIComponent，中文参数不编码直接失败；其二，金额、库存这类数字用整数存，浮点只给展示层用；其三，所有"看起来会一直长大"的数据（缓存、日志、离线队列）都要配一个清理入口，写应用时就问自己一句："这个东西三年后多大？"

这张表建议存成自己团队的 README 片段，新人入职先发这份——比口头讲三轮都管用。接口细节以官方文档为准，表里不变的是那一列"别忘了"，它们是本章真正的正文。

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- Preferences 存小设置：全异步 API + 记得 flush() + 不支持对象
- RelationalStore = 内置 SQLite：结构化数据首选，占位符防注入
- http 模块管网络：声明 INTERNET 权限、destroy 防泄漏、默认禁明文
- 选型看「存什么」：小设置 / 结构化 / 分布式 / HTTP / 文件，各归各位
- token 等敏感数据别进 Preferences，也别进 HiLog 日志
- 三者对应安卓 SP/Room/OkHttp 与 iOS UserDefaults/Core Data/URLSession
:::
