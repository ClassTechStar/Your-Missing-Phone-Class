---
id: di-liu-shi-liu-zhang
num: 66
part: ios-kai-fa-pian
nav: 第六十六章：项目二——天气查询App（网络版）
toc: default
kind: chapter
---

### 第六十六章：项目二——天气查询 App（网络版）

{class="chapter-intro mb-4"}
记账本是"练内功"，天气 App 是"见世面"——它要和互联网打交道。这个项目你会学到：申请免费 API、解析 JSON、处理"加载中/成功/失败"三种界面状态，以及怎么把 API 密钥藏好。做完它，你就具备了做任何"联网 App"的能力——新闻、汇率、翻译，套路一模一样。

#### 一、申请免费天气 API

个人练手，推荐 <strong>OpenWeatherMap</strong> 或国内的 <strong>和风天气（QWeather）</strong>——都有免费额度，注册即用。以 OpenWeatherMap 为例：

1. 注册账号 → 在 API keys 页面生成一个 Key（<code class="inline">apikey</code>）；
2. 免费版可调用 Current Weather 接口：<code class="inline">api.openweathermap.org/data/2.5/weather? q=beijing&appid=你的Key&units=metric</code>；
3. 浏览器里先试一次，看看返回的 JSON 长什么样——这是接任何 API 前必做的"预习"。

##### 注册实录：每一步屏幕上会出现什么

别小看"注册即用"四个字，第一次走的人会在三处愣住。第一处是注册页：邮箱注册，验证邮件可能躺在垃圾箱里。第二处是控制台首页：一排菜单里找 "API keys"——它通常缩在个人资料的子菜单里，点进去能看到一个自动生成的默认 Key，你也可以自己再生成一个专门给练手项目用。第三处是"生效等待"：新申请的 Key 可能要等上一会儿才真正可用，刚拿到就调试却一直报错，多半不是你的代码错了，是 Key 还没醒——喝口水再试。拿到 Key 先存进你的密码管理器（第 14 章讲过的那类工具），别让它躺在聊天记录里。

##### 把 URL 拆开看：四个参数各自的脾气

那串地址看着吓人，拆开其实就四个零件。给你一张表，后面写代码时每个参数都会出场：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">参数</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">作用</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">要注意的</th></tr></thead><tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">q</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">要查的城市名</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">拼音/英文更稳，中文支持见后文小贴士</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">appid</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">你的密钥</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">绝不能写死在代码里，下一节细说</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">units</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">单位制</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">metric 是摄氏度，不设默认开尔文</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">lang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">返回语言</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">zh_cn 让天气描述变中文</td></tr>
</tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
天气接口的四个查询参数

两个容易被默认值坑住的点：URL 里的 <code class="inline">units=metric</code> 决定了温度是摄氏度——摄氏/华氏、时区、本地化数字格式这些都要显式设，别指望用户跟你用同一套习惯；示例城市也别写死在业务逻辑里。另外，苹果官方的 WeatherKit 服务可以一并看看，额度和收费以官网为准，上架正式产品前多比较一下没坏处。

##### 浏览器预习：读懂这份 JSON

把完整 URL 粘进浏览器地址栏回车，你会看到一大坨 JSON。别慌，练手版只关心三个地方——照着官方返回（节选示意）找：

::: div .code-block
:::inline div .code-head
<span>JSON · 返回示例（节选）</span><span class="dots">···</span>
:::

```
{
  "weather": [ { "description": "晴" } ],
  "main": { "temp": 26.5, "humidity": 40 },
  "name": "北京"
}
```
:::

- <strong>weather</strong>：一个数组——天气描述藏在第一个元素里，"晴""多云"这类给人看的文字；
- <strong>main</strong>：一堆数值——温度、湿度都在这儿，是界面要展示的数字；
- <strong>name</strong>：城市名——服务器确认"你查的是哪儿"。

这五分钟的"预习"是最划算的投资：后面定义数据模型时，你照着这坨 JSON 抄字段就行，一个名字都不用猜。接任何新 API，都先浏览器看一眼原始返回——这个习惯会让你在团队里显得出奇地靠谱。预习还可以更进一步：把返回全文存成一个 .json 文件放进项目里，写模型、写解析时随手能看，断网也能开发——服务器不在身边，样例就是你的服务器。

##### 另一条路：和风天气的申请要点

如果你的目标用户主要在国内，和风天气值得从头走一遍——流程和 OpenWeatherMap 大同小异：注册控制台、创建一个"应用/项目"、拿到自己的 Key。它对中文城市名和国内数据源的支持更省心，返回字段命名和结构是另一套，接它就意味着模型和服务层要按它的文档重写一遍——别怕，这正好是第十一节扩展练习的题。提前说破一个规律：<strong>换数据服务商，动的只是"网络层那一层"，界面和状态管理原封不动</strong>——这也是分层架构给你的底气。各家免费额度的规则不同且随时调整，以官网为准；练手阶段"注册即用"哪家都够。

##### 选哪家服务：三家的取舍

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">服务</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">特点</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">适合</th></tr></thead><tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenWeatherMap</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">老牌、文档全、免费额度够练手</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">本章主例，全球城市通用</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">和风天气（QWeather）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">国内服务，中文城市与本地化做得好</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">面向国内用户的正式产品</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">WeatherKit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">苹果官方，与系统生态整合深</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">上架前值得比较，额度收费以官网为准</td></tr>
</tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
三家天气服务的取舍

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>避坑提醒：密钥绝不能写死在代码里

{class="mt-1"}
API Key 相当于你的"钱包密码"，写进代码一提交到 GitHub，几小时内就会被爬虫扫走盗刷。iOS 的正确做法：放进 <code class="inline">Config.xcconfig</code>（配置文件，已被 gitignore 忽略），通过 Info.plist 读入代码。搜索"iOS xcconfig 管理密钥"照着改即可。
:::

##### 密钥藏进 xcconfig：三步走

避坑提醒给了方向，这里把三步展开。第一步，在工程根目录新建 <code class="inline">Config.xcconfig</code> 文件，内容一行：

::: div .code-block
:::inline div .code-head
<span>XCCONFIG · Config.xcconfig（不进 git）</span><span class="dots">···</span>
:::

```
WEATHER_API_KEY = 你刚申请的Key
```
:::

第二步，确认它不会进仓库：打开项目里的 .gitignore，加上 <code class="inline">Config.xcconfig</code> 这一行——文件里还有个秘密武器 Config.sample.xcconfig（占位版，密钥写"你的Key"），随仓库提交，别人克隆后照着填自己的 Key 就能跑。

第三步，把变量接进 Info.plist：添加一项键为 <code class="inline">WEATHER_API_KEY</code>、值为 <code class="inline">$(WEATHER_API_KEY)</code> 的条目（圆括号写法就是在引用 xcconfig 变量），再把工程 target 的配置指向这个 xcconfig 文件。然后代码里用一个专门的枚举把它取出来：

::: div .code-block
:::inline div .code-head
<span>SWIFT · Config.swift（读密钥）</span><span class="dots">···</span>
:::

```
enum Config {
    static let apiKey = Bundle.main.object(
        forInfoDictionaryKey: "WEATHER_API_KEY") as? String ?? ""
}
```
:::

配置对不对，验收办法很直接：打印 <code class="inline">Config.apiKey</code> 看是不是你的 Key（验证完把打印删掉）。细节记不全没关系——照官方文档和搜索关键词走一遍，第二次就熟了。要记的是原则：<strong>密钥只住在配置文件里，代码里永远是"去取"，不是"写死"</strong>。

##### 万一已经泄露了怎么办

假如你不小心把带 Key 的代码推上了 GitHub——别慌，处理动作就三下：去服务后台把这个 Key 作废（revoke），重新生成一个新 Key 填进 xcconfig，然后把旧 Key 从 git 历史里清掉（或者干脆当它脏了，以后新项目再讲历史清理）。密钥不是"删掉那行代码"就完事——它一旦公开，就该当密码泄露处理：换掉，越快越好。

##### Key 与额度：练手前该知道的几句实话

免费额度是"一定时间内的调用次数"这种规则，各家的具体数字和口径不同，也随时可能调整，写代码前以官网说明为准。给你三条不会过时的使用常识：其一，调试也在烧额度——每跑一次 App 就是一次真实请求，别把模拟器当永动机开着跑循环；其二，别把 Key 分给别人共用，额度是绑在你账号上的，超了算你的；其三，真要频繁调试，先想想缓存——上一节的 lastGood 思路反过来用，"短时间内别重复请求同一座城市"既是省额度，也是省用户流量。这三条往后做任何联网 App 都成立。

#### 二、网络层：URLSession + Codable

先照 API 返回的 JSON 定义模型，再写服务：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 数据模型 + 服务</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"晴"}],"main":{"temp":26.5,"humidity":40},"name":"北京"}
struct WeatherResponse: Codable {
    let weather: [Weather]
    let main: Main
    let name: String
}
struct Weather: Codable { let description: String }
struct Main: Codable { let temp: Double; let humidity: Int }

struct WeatherService {
    let key: String   // 从 xcconfig 读入

    func fetchWeather(city: String) async throws -> WeatherResponse {
        var comps = URLComponents(string: "https://api.openweathermap.org/data/2.5/weather")!
        comps.queryItems = [
            URLQueryItem(name: "q", value: city),
            URLQueryItem(name: "appid", value: key),
            URLQueryItem(name: "units", value: "metric"),
            URLQueryItem(name: "lang", value: "zh_cn")
        ]
        let (data, _) = try await URLSession.shared.data(from: comps.url!)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}
```
:::

##### 逐行拆解：为什么用 URLComponents 而不是字符串拼接

新手写 URL 的直觉是字符串相加：<code class="inline">"…weather?q=" + city</code>。能跑，但城市名一变就露馅——URL 里有些字符有特殊含义（空格、&amp;、问号），中文城市名更是必须转成编码形式才能进 URL。URLComponents 的 <code class="inline">queryItems</code> 会替你做这套转义：你给它"北京"，它给 URL 一个合法的编码形态。这也顺带回答了"为什么要传 q=beijing 而不是 q=北京"的一半疑问——另一半（服务端对中文城市名的支持程度）在第五节的小贴士里。

四个 URLQueryItem 一看就懂：就是上一节那张参数表逐项翻译。以后接口要加参数（比如按坐标查询），往数组里再加一项就行——参数列表化的好处是增删干净，不用在字符串里数第几个 &amp;。

##### WeatherService 为什么要单独一层

你可能觉得把请求代码直接塞进 ViewModel 也行——几行而已。但把"和服务器说话"封进 WeatherService，买到的是三样东西。第一样是替换自由：哪天从 OpenWeatherMap 换到和风天气，只改 service 里的地址和模型映射，ViewModel 和界面一行不动。第二样是测试方便：以后给"解析对不对"写测试，直接调 service 的方法喂假数据就行，不用起界面。第三样是心智减负：ViewModel 只管"什么时候要数据、拿到数据怎么办"，至于"怎么发请求"这种细节被关在 service 里，两边互不添乱。这和记账本"校验住进 ViewModel"是同一个哲学：<strong>每类知识只住在一个地方</strong>。

##### Codable：字段对上，魔法自动发生

三个 struct 就是照着预习时抄的 JSON 写的：weather 是数组所以声明成 [Weather]，temp 是小数所以是 Double，humidity 是整数所以是 Int。<code class="inline">Codable</code> 协议本身一行实现代码都不用写——Swift 编译器自动生成"JSON 到对象"的双向翻译。JSONDecoder 拿到数据，按字段名对号入座：JSON 里叫 temp，模型里也叫 temp，就装进去了。

要是名字对不上呢？用 CodingKeys 改名映射：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 字段改名映射（示意）</span><span class="dots">···</span>
:::

```
struct Main: Codable {
    let temp: Double
    let humidity: Int

    enum CodingKeys: String, CodingKey {
        case temp
        case humidity = "humidity_percent"   // JSON 里叫这个，模型里叫 humidity
    }
}
```
:::

再记住一条铁则：<strong>类型也要对上</strong>。JSON 里 temp 万一给了个字符串"26.5"，解码当场抛错——这就是第六节调试手段里"打印原始数据"的价值：解析失败时，先看原始 JSON 长什么样，别对着报错空想。顺带教你读解码报错：错信息里通常带着"哪个字段、期待什么类型、实际拿到什么"，例如 typeMismatch 之类的字样，顺着它指的字段去原始 JSON 里核对，十有八九一眼破案。实在读不懂就整段复制给搜索引擎或 AI——报错原文是最值钱的搜索词。

##### 请求三件套：地址、方法、期待

网络请求拆开永远是三件事：问哪儿（URL）、怎么问（HTTP 方法）、期待什么回答（返回类型）。本章只用了 GET——"读取"语义的查询全用它，天气正属于此类。HTTP 方法还有 POST（提交数据）、PUT/DELETE 等，名字记住就行，本章用不到；哪天你做"提交反馈""注册登录"，自然会撞上它们，到时候再学不迟。期待什么回答已经由 Codable 模型声明了——三件套里你实际要操心的只有前两件，第三件编译器替你看着。

##### async/await 那两行在做什么

函数签名里的两个词是主角：<code class="inline">async</code> 表示"这是个要等的活儿"，<code class="inline">throws</code> 表示"它可能失败"。调用处用 <code class="inline">try await</code> 接住——语法在第 64 章讲 URLSession 时见过，这里第一次用在真服务器上。它解决的老大难问题是"网络等待别卡死界面"：await 这行执行时，当前线程可以腾出来干别的（比如维持界面滚动），数据回来再回来继续走。你什么都不用配，Swift 并发替你调度——比起老一代回调套回调的写法，代码从"金字塔"变成了"一条线"。

代码里还有两个 <code class="inline">!</code> 强制解包：URLComponents 的初始化和 <code class="inline">comps.url!</code>。前者因为地址是写死的常量字符串，格式必然合法，练手期可以接受；后者同理。但要心里有数：强制解包是"我赌它一定不是 nil"，赌输当场崩。哪天 URL 改成用户输入拼出来的，就得换安全写法（if let 或 guard）——第 61 章讲 Optional 时的原则，在联网代码里照样成立。

##### 先跑通：在界面的 .task 里发第一次真请求

服务写好了，先别管界面漂亮不漂亮，能拿到数据再说。临时建一个最简视图，用 <code class="inline">.task</code> 在页面出现时自动发一次请求：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 第一次真请求（临时验证）</span><span class="dots">···</span>
:::

```
struct TempTestView: View {
    @State private var text = "请求中…"

    var body: some View {
        Text(text)
            .task {
                do {
                    let service = WeatherService(key: Config.apiKey)
                    let data = try await service.fetchWeather(city: "beijing")
                    text = "\(data.name)：\(data.main.temp)°C"
                } catch {
                    text = "失败：\(error)"
                }
            }
    }
}
```
:::

跑起来看到"Beijing：26.5°C"（数字随当天天气变），网络层就算通了。这步的验收意义和记账本"塞三条测试数据"一样：地基先验，再往上盖。失败也别慌——把报错原样读一遍，九成是密钥没配对或 Key 还没生效。

#### 三、三种界面状态：加载中 / 成功 / 失败

联网 App 的灵魂在于"状态管理"。网络慢、断网、城市名打错……每种情况界面都要给用户交代。用<strong>枚举 + switch</strong> 优雅地表示：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 界面状态</span><span class="dots">···</span>
:::

```
enum LoadState {
    case loading                  // 转圈中
    case success(WeatherResponse) // 成功
    case error(String)            // 失败
}

@Observable
class WeatherViewModel {
    var state: LoadState = .loading
    private let service = WeatherService(key: Config.apiKey)

    func search(city: String) async {
        state = .loading
        do {
            let data = try await service.fetchWeather(city: city)
            state = .success(data)
        } catch {
            state = .error("查不到这个城市，换个名字试试？")
        }
    }
}

// 界面里：
switch vm.state {
case .loading: ProgressView("加载中…")
case .success(let d): WeatherContent(data: d)
case .error(let msg): Text(msg).foregroundColor(.secondary)
}
```
:::

##### 错误示范：三个变量管状态，管出鬼

不用枚举的写法长这样：一个 <code class="inline">isLoading: Bool</code>、一个 <code class="inline">data: WeatherResponse?</code>、一个 <code class="inline">errorMsg: String?</code>。听着也行，对吧？可" isLoading 为 false、data 为 nil、errorMsg 也为 nil"是个什么状态？没人说得清。三个变量之间的组合是"乘法"——理论上存在八种组合，其中一半是自相矛盾的鬼状态：加载中又显示着旧数据、错误信息和新数据并存……每个鬼状态都是一道未来 bug。枚举把状态变成"互斥的三选一"：任何时刻只能是一个 case，想出现鬼状态都写不出来。这一步不是语法偏好，是消灭一整类 bug。

顺带一提 <code class="inline">success(WeatherResponse)</code> 的括号：枚举可以"带着值"——成功时顺手把数据装进 case 里，switch 解出来直接用。这个特性叫关联值，安卓篇第 55 章的 sealed class 是同一个思想的不同写法，两章对照着看会很有意思。

##### 把"失败"分细：URLError 的分支

catch 里一刀切"查不到这个城市"是把四件事说成了一件事。URLError 自带错误码，分得了很细：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 按 URLError 分支提示</span><span class="dots">···</span>
:::

```
do {
    let data = try await service.fetchWeather(city: city)
    state = .success(data)
} catch let e as URLError {
    switch e.code {
    case .notConnectedToNetwork:
        state = .error("没有网络，检查一下 Wi-Fi 或蜂窝数据")
    case .timedOut:
        state = .error("网络太慢，超时了，请稍后再试")
    default:
        state = .error("出了点小问题，请稍后再试")
    }
} catch {
    state = .error("出了点小问题，请稍后再试")
}
```
:::

注意这层分支管的是"根本没到服务器"的失败；到了服务器但被拒绝（比如被限流的 HTTP 429、服务端出错的 5xx），得看响应的状态码——<code class="inline">URLSession</code> 返回的第二个值（前面代码里用 <code class="inline">_</code> 丢掉的那个 response）就是干这个的，它是 HTTPURLResponse，取 <code class="inline">statusCode</code> 判断。两条线合起来，错误才算真的"分了级"——思路在 64 章"网络错误分级"那节铺过底，这里是它的第一场实战。

##### 转圈也有讲究：loading 不是白屏的遮羞布

loading 状态最常见的槽点是"转圈转得人发慌"。两个低成本改进：其一，文案具体化——ProgressView 配的字从"加载中"换成"正在查 beijing 的天气"，用户知道机器在干活不是死机；其二，别让 loading 出现得太频繁——结果没变就别全屏转圈，这个小工程的终极答案在缓存那一步（下一节做）。还有一条底线：loading 期间把"查询"按钮临时禁用，防止用户连点发出去一串重复请求。

##### 谁负责改状态：边界要像国境线一样清楚

三段式里还有一条隐形规则：<code class="inline">state</code> 只在 ViewModel 里改，界面只读。你可能在别人的代码里见过界面直接 <code class="inline">vm.state = .loading</code> 的写法——能用，但国境线松了：今天界面改 loading，明天它就敢顺手改 success，再明天两个地方同时改状态，时序 bug 就来了。守规矩的写法是把 state 声明成对外只读（private(set) 的思路），改状态的入口只有 search 这类方法。另外，改状态的代码跑在哪个线程也值得知道一句——SwiftUI 界面要在主线程更新，Swift 并发下用 @MainActor 标注 ViewModel 是标准姿势，第 68 章"Swift 并发要点"会专门展开，这里先立个路标。

这个 <code class="inline">loading/success/error</code> 三段式是联网界面的"万金油模板"，先背下来，以后所有联网 App 照葫芦画瓢。

再补一层：error 别只给一句"查不到"。无网络、超时、被限流（HTTP 429）、服务端出错是四种不同的失败，文案和应对各不相同——断网就教用户开网，限流就请他稍后再试，每一种都配一个「重试」入口。还有一条老练的做法：请求失败时把上一次成功的结果翻出来展示，标上数据时间——有旧数据的屏幕，永远比白屏友好。

##### 缓存上次结果：失败页面也要有内容

"翻出旧数据"落到代码里，就是 ViewModel 多存两个属性——最近一次成功的结果和它的落袋时间：

::: div .code-block
:::inline div .code-head
<span>SWIFT · ViewModel 里的"last good"</span><span class="dots">···</span>
:::

```
@Observable
class WeatherViewModel {
    var state: LoadState = .loading
    private(set) var lastGood: WeatherResponse?   // 最近一次成功的结果
    private(set) var lastUpdated: Date?           // 它是什么时候拿到的

    private let service = WeatherService(key: Config.apiKey)

    func search(city: String) async {
        state = .loading
        do {
            let data = try await service.fetchWeather(city: city)
            lastGood = data          // 成功一次，就存一份底
            lastUpdated = Date()
            state = .success(data)
        } catch {
            state = .error("查不到这个城市，换个名字试试？")
        }
    }
}
```
:::

界面里 error 分支顺便把旧数据画出来：

::: div .code-block
:::inline div .code-head
<span>SWIFT · error 状态里展示旧数据</span><span class="dots">···</span>
:::

```
case .error(let msg):
    VStack(spacing: 10) {
        if let d = vm.lastGood {
            WeatherContent(data: d)
            if let t = vm.lastUpdated {
                Text("数据时间 \(t.formatted(date: .omitted, time: .shortened)) · 暂为旧数据")
                    .font(.footnote)
                    .foregroundColor(.secondary)
            }
        }
        Text(msg)
            .foregroundColor(.secondary)
    }
```
:::

用户看到的是：熟悉的天气界面还在，只是顶上一行小字承认"这是旧数据"。体面，就是这么攒出来的。这一版缓存只活在内存里——App 一杀就没了；把它存进磁盘（第 64 章的 UserDefaults 或文件方案都能装），重启也能兜底，留给本节末尾的扩展练习。缓存和「重试」按钮是一对搭档：旧数据管"看得见"，重试管"有出路"——两个都在，用户才不会觉得被丢下。

<strong>一句话记牢：一个项目的成熟度，看它在最差网络下是什么样子。</strong>

#### 四、实战界面代码：把天气画出来

::: div .code-block
:::inline div .code-head
<span>SWIFT · 天气界面（核心片段）</span><span class="dots">···</span>
:::

```
struct WeatherContent: View {
    let data: WeatherResponse

    var body: some View {
        VStack(spacing: 12) {
            Text(data.name)
                .font(.title.bold())
            Text("\(Int(data.main.temp))°C")
                .font(.system(size: 76, weight: .thin))
            Text(data.weather.first?.description ?? "未知")
                .font(.title3)
                .foregroundColor(.secondary)
            HStack(spacing: 24) {
                Label("湿度 \(data.main.humidity)%", systemImage: "humidity")
                Label("当前气温 \(Int(data.main.temp))°C", systemImage: "thermometer")
            }
        }
        .padding()
    }
}
```
:::

几个小细节值得学：<code class="inline">first?</code> 安全取第一个元素（列表可能为空），<code class="inline">?? "未知"</code> 给兜底文案；76 号细字重的温度数字是天气类 App 的经典配方；<code class="inline">Label</code> 是"图标+文字"的官方组件，比手拼 HStack 更规范。

##### 温度的字体戏法：为什么 76 号细字重像"天气 App"

你有没有想过，为什么大温度数字都配极细的字重？粗体大数字有压迫感，细体大数字轻盈、干净，把"环境"的感觉留出来了——这是天气类 App 多年沉淀下来的视觉语言，你抄得理直气壮。真正要自己拿主意的是两处：温度取整（<code class="inline">Int(...)</code>）舍弃了小数——天气场景 26.5 显示成 26 并没有信息损失，反而更干脆；字号写死 76 在这个画面里是设计选择（大数字就是要夺目），但正文文字别学它，动态字体那条线（第 65 章讲过）还是要守。

##### 给天气配图标：一行映射表

返回的 description 是文字，配个图标界面立刻活起来。用 <code class="inline">Image(systemName:)</code> 按描述映射：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 天气图标映射</span><span class="dots">···</span>
:::

```
func icon(for description: String) -> String {
    switch description {
    case let d where d.contains("雨"):  return "cloud.rain"
    case let d where d.contains("雪"):  return "snowflake"
    case let d where d.contains("雷"):  return "cloud.bolt.rain"
    case let d where d.contains("云"):  return "cloud"
    case let d where d.contains("雾"):  return "cloud.fog"
    default:                            return "sun.max"
    }
}

// 用在 WeatherContent 里：
Image(systemName: icon(for: data.weather.first?.description ?? ""))
    .font(.largeTitle)
```
:::

这里用"包含雨字就给雨图标"的粗匹配，练手够用——更正经的做法是按服务方定义的天气代码查表（官方文档里有完整对照），各家代码表不一样，以你选的服务的文档为准。图标想换色就 <code class="inline">.foregroundColor</code>，别去找彩色贴图。

##### 第二行信息：加字段之前先看返回里有什么

界面下面那行"湿度"想再丰富一点（比如加体感温度、气压）？OpenWeatherMap 的返回里其实还有体感温度等字段——动手前先回预习文件里确认它叫什么、什么类型，然后给 Main 结构体加一个字段，一行就接进来了。这个动作顺序值得固化：<strong>想展示什么 → 先查原始返回 → 加模型字段 → 上界面</strong>。反过来瞎猜字段名，只会收获一屏 nil 和一脸问号。

##### 深色模式：夜间妆自己就化好了

天气 App 深夜打开的概率极高，深色模式不是锦上添花。好消息是默认组件已经帮你化好了：语义色（.primary、.secondary）和系统图标在两种模式下各有一套颜色。要自己动手的只有两处：自定义的强调色用 Assets 里的"Any/Dark Appearance"各填一个值；别给背景铺写死的白色或浅灰。验收动作固定成习惯：模拟器切深色，三态各看一遍——转圈、天气卡片、报错文案，哪一处看着刺眼就修哪一处。

##### 主界面拼装：把三态和内容合成一页

把状态开关和 WeatherContent 装进同一个页面，这就是天气 App 的主界面全貌：

::: div .code-block
:::inline div .code-head
<span>SWIFT · WeatherView.swift（主界面）</span><span class="dots">···</span>
:::

```
struct WeatherView: View {
    @State private var vm = WeatherViewModel()
    @State private var cityInput = "beijing"

    var body: some View {
        NavigationStack {
            VStack(spacing: 16) {
                HStack {
                    TextField("城市拼音，如 beijing", text: $cityInput)
                        .textFieldStyle(.roundedBorder)
                    Button("查询") {
                        Task { await vm.search(city: cityInput) }
                    }
                }
                .padding(.horizontal)

                switch vm.state {
                case .loading:
                    ProgressView("加载中…")
                case .success(let d):
                    WeatherContent(data: d)
                case .error(let msg):
                    Text(msg).foregroundColor(.secondary)
                }

                Spacer()
            }
            .navigationTitle("天气")
            .task {                       // 进页面自动查一次
                await vm.search(city: cityInput)
            }
        }
    }
}
```
:::

跑一下：进页面自动转圈，然后出现天气卡片；输入 "shanghai" 点查询，卡片一秒换脸。到这一步，网络层、状态层、界面层三条线全部合龙——你已经拥有一个真能用的天气 App 了。剩下的全是让它"从能用变好用"：搜索框升级、收藏城市、下拉刷新，都在下一节。

#### 五、交互细节与收藏城市

- <strong>搜索框</strong>：顶部 <code class="inline">.searchable</code> 修饰符，系统自带搜索交互，提交时调 <code class="inline">vm.search</code>；
- <strong>收藏城市</strong>：把常看的城市存进 UserDefaults，下次打开自动查；
- <strong>下拉刷新</strong>：<code class="inline">.refreshable { await vm.search(...) }</code> 一行搞定；
- <strong>定位是可选项</strong>：用户拒绝定位权限时，功能不能整个失效——搜索框手动输城市就是现成的降级出口（权限弹窗只弹一次，第 68 章细说怎么申请）；
- <strong>天气图标</strong>：用 <code class="inline">Image(systemName:)</code> 按描述映射（sun.max / cloud.rain / snowflake），界面立刻活起来。

这五条是"从能用到好用"的清单，每条背后都有讲究。天气图标上一节已经给了映射代码，剩下四条逐个展开。

##### .searchable：把搜索框交给系统

第五条清单里最省力的是第一条：<code class="inline">.searchable</code> 挂在列表或主视图上，系统自动给你导航栏下拉式搜索框、取消按钮、键盘管理——全是 iOS 用户的肌肉记忆，一行都不用你写：

::: div .code-block
:::inline div .code-head
<span>SWIFT · searchable 接入搜索</span><span class="dots">···</span>
:::

```
NavigationStack {
    // …三态界面…
    .searchable(text: $cityInput, prompt: "城市拼音，如 beijing")
    .onSubmit(of: .search) {
        Task { await vm.search(city: cityInput) }
    }
}
```
:::

<code class="inline">onSubmit(of: .search)</code> 在用户点键盘上的"搜索"键时触发，比"查询"按钮顺手——键盘一收一回，天气就换好了。自己手搓一个 TextField 也能实现，但系统搜索框带着"下拉呼出"的手感，这种系统级的交互细节，能用现成的就用现成的。

##### 收藏城市：UserDefaults 存一份名单

天天要看的城市不该每次都手输。存一份收藏名单，App 一打开自动查第一座城——UserDefaults 就干得了这活儿（用法在第 64 章铺过）：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 收藏城市的存与取</span><span class="dots">···</span>
:::

```
// 存：把收藏列表写进去
@State private var favorites: [String] = ["beijing", "shanghai"]

UserDefaults.standard.set(favorites, forKey: "favorite_cities")

// 取：App 启动时读回来
favorites = UserDefaults.standard.stringArray(forKey: "favorite_cities") ?? []

// 界面：用 .task 在页面出现时自动查第一个收藏
.task {
    if let first = favorites.first {
        await vm.search(city: first)
    } else {
        await vm.search(city: "beijing")   // 没收藏就查默认城市
    }
}
```
:::

界面上给收藏一个入口：天气卡片下方一排城市小按钮，点谁查谁，长按弹出"加入收藏/移除"（Context Menu，系统组件）。注意这里存的是城市名字符串列表——够用了。哪天收藏要带更多信息（备注、排序），再升级成 Codable 数组存档，思路在第 64 章都有。

##### 下拉刷新与自动加载

看天气的典型动作是"感觉天变了，往下拉一下"。.refreshable 一行接住这个手势：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 下拉刷新</span><span class="dots">···</span>
:::

```
.refreshable {
    let city = lastCity   // 记住上一次查的是哪儿
    await vm.search(city: city)
}
```
:::

系统自动在下拉时出转圈、收手时结束——你只管给一个 async 闭包。配套的小事是"进页面自动查一次"：.task 里查第一个收藏城市（上一段写过），用户打开 App 就有数据，不用先点一下。两个细节合起来，App 就有了"打开即看、想刷就刷"的节奏。

##### 错误文案的语气：像人话，不像报错

给三态配文案时，拿"用户第一次遇到"的心态读一遍。反例："Error Domain=NSURLErrorDomain Code=-1009"——这是给开发者的，甩给用户等于没说；"网络错误！"——正确但冷冰冰。正例是"没有网络，检查一下 Wi-Fi 或蜂窝数据"——说清发生了什么、下一步能做什么。一个小测试：把文案读给不写代码的朋友听，他要是皱眉，就重写。文案是产品的一部分，不是代码的附属品——这件事在 64 章讲错误分级时就强调过，值得反复念。

##### 定位：锦上添花的功能，降级要提前想好

"自动定位当前城市"很香，但它要权限——而权限是用户可以拒绝的。产品化的思路是两条路并行：定位成功就用定位城市，被拒绝或失败就落到手动搜索，功能一条都不缺。清单里那句"权限弹窗只弹一次"是系统行为，弹过一次你再想要，用户得去设置里翻——所以第一次弹窗的时机要挑（用户主动点了"用我的位置"再弹，比一进 App 就弹通过率高得多），具体申请姿势第 68 章细讲。本章先把手动搜索这条路铺结实，定位留给进阶的你。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：中文城市的"梗"

{class="mt-1"}
OpenWeatherMap 对中文城市名支持一般，搜"北京"可能无结果而 "beijing" 正常。产品化做法是内置一份"城市名 → 英文/坐标"映射表，或接国内天气服务。练手阶段先支持拼音/英文城市名即可，别和它较劲。
:::

这条小贴士值得再往下挖半步：映射表不用一步到位——先建一个十几条常用城市的小字典（北京 → beijing、上海 → shanghai），用户输中文就查表转拼音，查不到再原样发给服务器。几百条主流城市的中文-拼音对照，网上有现成公开数据可参考，自己手打常用的二十来条也够练手用。第五节收官时，你的 App 已经是"搜索、收藏、刷新、降级"四项俱全——接下来该学怎么伺候它出毛病了。

#### 六、网络请求怎么调试：打印、抓包与模拟慢网

联网 App 出问题，十有八九在"请求没发对"或"响应没解析对"。三个调试手段：

1. <strong>打印原始数据</strong>：把 <code class="inline">String(data: data, encoding: .utf8)</code> 打印出来看原始 JSON——字段名、类型一目了然，比猜快十倍；
2. <strong>抓包工具</strong>：Mac 上免费的 Proxyman / 付费的 Charles（可试用）/ 开源的 mitmproxy 能截获 App 的全部请求和响应，像 X 光一样看清网络层；
3. <strong>模拟弱网</strong>：模拟器菜单 Features → Network Link Conditioner（模拟器自带；要限整台 Mac 的网速才需另装开发者网站的面板），能模拟 3G、高延迟——测出"转圈半天"的体验问题。

##### 打印的正确姿势：打 URL、打状态码，别打密钥

打印不是想打什么打什么，三条纪律让它的价值翻倍。第一，打完整请求 URL——九成"查不到"是 URL 少参数或拼错，一眼见分晓。第二，打 HTTP 状态码——401、429、500 各自指向不同的病根，比"反正失败了"有用得多。第三，也是最容易翻车的一条：<strong>别把完整 URL 原样打出来——里面带着你的 appid</strong>。调试日志很可能被截图、被贴进群里提问，密钥跟着日志泄露是最常见的"无意识泄露"。折中办法很简单：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 安全打印请求信息</span><span class="dots">···</span>
:::

```
let maskedKey = String(key.prefix(4)) + "****"
print("GET weather q=\(city) key=\(maskedKey)")
```
:::

能对上号、看不出全文。还有一条收尾纪律：问题解决后把调试打印清掉（或换成本章末尾提到的日志方案），别让它们跟着代码进仓库。

##### 第一次抓包：三步看穿你的请求

打印只能看你主动打的东西，抓包能看全部。以免费的 Proxyman 为例，第一次抓包三步：第一步，装好打开，它会提示安装本机证书——照提示装、信任它（这是它解码 HTTPS 的前提）；第二步，跑起你的 App，搜一次天气，Proxyman 列表里立刻出现那条 api.openweathermap.org 的请求；第三步，点开它——请求头、完整 URL、原始响应、耗时全摊在眼前。你会用上的三个场景：确认请求到底发出去没有；确认服务器到底回了什么（打印看不见的部分，比如响应头里的限流信息）；对比"同一请求在浏览器里正常、在 App 里失败"差在哪。

一句安全底线：抓包工具只能用于调试你自己的 App 和你有权调试的服务，别拿它碰别人的 App——证书装在本机也意味着你的 HTTPS 流量对它透明，不用时退出或卸载证书更稳妥。

##### 弱网模拟：让"转圈半天"提前现形

开发时 Wi-Fi 飞快，你以为世界都这么快；用户在地铁隧道里，页面转圈转到怀疑人生。弱网模拟就是把这种用户提前请进你的开发流程。模拟器里开 Network Link Conditioner，选一个低带宽高延迟的档位，然后走一遍完整流程：进页面自动加载要多久？转圈文案还贴切吗？超时分支触发了吗？重试按钮好吗使？缓存旧数据出来了吗？凡是"感觉还行"，在弱网下都会现原形——改完再切回正常网络，确认没把好体验改坏。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：请求没过 ATS？

{class="mt-1"}
如果请求一发出就报 "App Transport Security" 错误，八成是用了 http:// 明文地址。正式接口必须 HTTPS；本地调试临时开例外（Info.plist 加 NSAllowsLocalNetworking），上架前记得清干净。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：天气 App 验收清单

{class="mt-1"}
① 正常搜索出天气；② 断开网络，App 优雅报错不崩溃（模拟器里关掉 Mac 的网络测！）；③ 输一个不存在的城市，提示友好；④ 收藏两个城市，重启 App 还在；⑤ 深色模式下界面不刺眼；⑥ 开飞行模式再搜一次，App 不崩、文案友好，顺便看看有没有把上次的天气缓存出来；后台切回、弱网各试一遍——模拟器对这些场景不敏感，最好真机来。六条全过，这个项目才算毕业。
:::

##### 破案实录：三招连用的十五分钟

看三招怎么连起来用。小周遇到过一次经典病例：浏览器里查城市一切正常，App 里却永远失败。第一步，安全打印 URL——发现 q 参数没问题，但 appid 位置是空的：密钥没读进来。第二步，切换视角看响应——服务器返回的状态码是 401，坐实"密钥被拒"。第三步本来该轮到抓包，但前两招已经锁定病灶在配置层，直接回第一节查 xcconfig 三步走：原来是 target 的配置忘了指向那个 xcconfig 文件，改完重跑，通了。全程十五分钟，没用抓包——调试招式的价值不在"招多"，在"顺序"：先看自己发出去的，再看对方回的，还看不出来才动用抓包这台"X 光"。

模拟器和真机在调试上还有点分工差异：抓包、弱网面板这些工具在模拟器上都好开（跟 Mac 共享环境），真机抓包要额外配代理，步骤繁琐一截。建议的学习路径是：工具先在模拟器上练熟，真机只做终验——终验时重点看的是真机特有的行为（蜂窝切换、真实弱网），而不是再学一遍工具。

#### 七、常见 bug 门诊：六个高频翻车现场与修复动作

联网项目的 bug 有个规律：一大半发生在"请求与解析"这两道关口。六个高频病例，症状、病因、处方一次给全。

<strong>病例一：永远 error，明明代码没错</strong>。点查询永远进失败分支。九成是解析环节炸了：模型字段名或类型和真实 JSON 对不上。处方：按第六节第一招打印原始 JSON，和模型逐字段核对——找"名字不一致"和"类型不一致"（JSON 给字符串你声明成 Int）。修好后用 CodingKeys 固化映射。这种 bug 报错信息看着吓人，破案往往只要一分钟。

<strong>病例二：点查询没反应，也没报错</strong>。按钮点了，界面纹丝不动，控制台安静。多半是 async 没接住：在同步上下文里直接调 fetchWeather，编译器给了黄色警告（表达式是 async 的但没 await），你顺手忽略或修成了空 Task。处方：把警告当错误看待——联网代码里的黄色警告，一半以上是真雷。正确姿势是 Task { await vm.search(...) }，第 68 章的并发要点会系统讲。

<strong>病例三：中文城市查不到</strong>。搜"北京"失败、搜 beijing 正常——就是第五节小贴士那个"梗"。处方：先支持拼音；进阶做一个常用城市映射表，输中文查表转拼音再发请求。别跟服务端的编码习惯较劲，这不是你的锅，绕过去就好。

<strong>病例四：请求一发出就报 ATS</strong>。App Transport Security 拦截——你的 URL 是 http:// 明文。处方：换成 https；本地调试的临时例外按小贴士加 NSAllowsLocalNetworking，上架前清掉。这条错误信息直白，难点只在"看见它就想起 ATS"。

<strong>病例五：HTTP 401，密钥不对</strong>。服务器明确拒绝。三个可能：xcconfig 没接进 Info.plist（取出来是空串）；target 没配到那个 xcconfig 文件；Key 刚申请还没生效。处方：打印 Config.apiKey 的前四位（遮掉其余）确认非空，再按第一节三步走逐项复查。空串意味着配置链路断了，不是代码错。

<strong>病例六：连点查询，结果乱跳</strong>。快速连点三下，最后显示的是第一下的结果——旧请求后到，覆盖了新结果。这是网络编程经典的竞态：请求按发出的顺序返回没有保证。处方分两刀：轻的一刀是 loading 期间禁用查询按钮（第五节埋过这个点）；重的一刀是给每次请求编号，ViewModel 记住最新编号，响应回来时编号对不上就丢弃。第一刀治标，第二刀治本，练手项目第一刀就够，但你要知道第二刀的存在——以后写多屏并发时会正式遇上。

<strong>病例七：界面卡在"加载中"出不来了</strong>。转圈转了一分钟都不变。病因多半是状态机漏了出口：某个失败分支忘了把 state 置回 error，或者中途 return 绕过了状态更新。处方：让 state 只在 search 方法里改，并且保证这条路径"必然"走向三个 case 之一——catch 分支兜底置 error，任何提前 return 之前都先安顿好状态。三态模板本身没有洞，洞都在手写的岔路上。

<strong>病例八：请求发了一遍又一遍</strong>。控制台里同一座城市的请求连刷三四次。病因通常是触发点叠了：.task 里自动查一次，onAppear 里又查一次，Button 里还查一次——三个入口全活着。处方：搜一遍代码里所有 search 的调用点，留一个正主，其余删掉；以后新页面挂请求，默认只用 .task（它自带取消和唯一性）。重复请求烧的是你的免费额度和用户流量，这个 bug 值得当天修。

#### 八、边界情况清单：这些场景，想清楚再写代码

bug 门诊治已翻车的，这里防还没翻车的。七个联网项目的边界场景，动手前过一遍。

<strong>边界一：空输入与纯空格</strong>。用户没输城市就点查询，或者输了一串空格。别把空串发给服务器——先 trim（去掉首尾空格），空就直接不请求，顺带提示"先输个城市"。一行 guard 的事，挡掉一次无意义请求和一个尴尬界面。

<strong>边界二：超长输入</strong>。粘进来一段文章当城市名。低概率但值得兜底：长度超过合理城市名就提示"这不像城市名"。不拦的话服务器会拒绝，你的 error 文案还显得莫名其妙。

<strong>边界三：连着搜两座城</strong>。地铁上刚搜北京，又立刻搜上海——两个请求同时在飞，谁先回不确定（竞态的全场景版，第七节病例六的日常形态）。loading 禁用按钮能挡住大部分，真要彻底稳，就上"只认最新请求"的编号法。

<strong>边界四：时间与时区</strong>。天气服务返回的时间戳大多是 UTC 口径，展示"数据更新于几点"要换算成本地时间——Swift 的 Date 和 formatted 会按设备时区处理，通常自动就对；具体哪个字段是什么口径，以你所用服务的官方文档为准。别自己拿字符串掐表——第 65 章汇总日期的教训，在这儿原样适用。

<strong>边界五：额度耗尽与限流</strong>。调用量到顶，服务器回 429。App 侧的得体应对：文案"查询太频繁，请稍后再试"，别把 429 当成"查不到城市"糊弄过去；顺手做节流——同一座城市短时间内不重复请求，具体阈值你自己定。免费额度的具体规则以官网为准，设计文案时留出"被限流"这个分支就不会手忙脚乱。

<strong>边界六：后台切回，数据已旧</strong>。切出去半小时再回来，天气早就变了。得体行为：回前台时检查 lastUpdated，超过你心里那条线（比如半小时）就自动重查一次。判断前后台用 scenePhase，第 63 章生命周期那节铺过底——又是"学过的零件在项目里对上号"的时刻。

<strong>边界七：无收藏、无网络的冷启动</strong>。新装 App、没收藏、又恰好在地铁里——三件事凑齐，首屏是 error。有缓存就出缓存，没缓存就出一个友好的引导空态（"连上网络，输入城市名试试"）—— ContentUnavailableView 在上一章刚用过，搬过来就能用。

<strong>边界八：语言跟系统走</strong>。URL 里的 lang=zh_cn 是本章写死的——用户系统设成英文时，最好让描述也跟着变。做法是把参数换成读取系统的首选语言再映射成服务支持的语言代码（各家支持的语言清单以官方文档为准）。不是练手版的必做题，但它属于"显式参数"的正确归宿：显式不等于写死，显式的意思是"我清楚它的值从哪来"。

<strong>边界九：失败要失败得快</strong>。用户点查询，十秒没动静也没提示——这比报错更伤。超时上限（第九节）、重试封顶（一次）、禁用按钮（loading 期间）三件套合起来，保证任何请求都有一个明确的终点：要么数据，要么报错，要么明确告诉用户"还在等"。检查办法就是弱网模拟里掐表：从点击到出现反馈，不能超过你心里的耐心上限。

<strong>边界十：换台设备，收藏不跟着走</strong>。收藏存在本机 UserDefaults，换手机、换模拟器都不会跟过去——这是本地存储的天然边界，不算 bug，但用户会当 bug 报。两个应对：界面上别吹"云同步"（没做的事别许愿）；真想跨设备就走向 iCloud 方向（第 65 章进阶挑战二的思路在这里同样适用）。想清楚自己的 App 说到哪一步、做到哪一步，两边对齐，投诉就少。

<strong>边界十一：你根本不知道自己发了多少请求</strong>。"感觉没发几个"和"实际发了几个"往往差得远——自动查一次、下拉刷新一次、切后台回来又一次。抓包工具最好的副产品就是这份数字：列表面板里数一数某座城市出现了几次，重复请求立刻现形。给 App 里的每次 search 加个计数打印（调试期），数字对不上预期，就按第八节病例八的处方查触发点。这套"数请求数"的动作用不了十分钟，却是大多数人从没做过的体检——做过一次，你对 App 的流量观会永久改变。

#### 九、把请求层写厚一点：超时、重试与取消

三态模板跑通之后，请求层还差三块"成年人的装备"：超时怎么办、失败了要不要重试、用户走了请求要不要停。练手版可以不做，但要知道它们存在——上架前这仨迟早要补。

##### 超时：别让用户等到天荒地老

URLSession 对请求超时有默认行为，具体数值由系统决定，想自己拿捏可以通过请求配置里的 timeoutInterval 这类参数调整（细节以官方文档为准）。对体验来说，比"设多少秒"更重要的事有两件：一是超时文案要真实存在——弱网模拟里走到过一次超时分支，才算验证过；二是超时别和"查不到城市"共用一句提示——前者是"网络太慢"，后者是"名字不对"，混着说用户会重输一百遍城市名。

##### 重试：一次就好，而且挑对象

给 search 加一个重试参数，失败后自动再试一次，是性价比最高的加固：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 带一次自动重试的 search</span><span class="dots">···</span>
:::

```
func search(city: String, retryCount: Int = 0) async {
    state = .loading
    do {
        let data = try await service.fetchWeather(city: city)
        lastGood = data
        lastUpdated = Date()
        state = .success(data)
    } catch {
        // 只自动重试一次，且被取消的任务不再重试
        if retryCount < 1, !(error is CancellationError) {
            try? await Task.sleep(for: .seconds(2))
            await search(city: city, retryCount: retryCount + 1)
        } else {
            state = .error("查不到这个城市，换个名字试试？")
        }
    }
}
```
:::

两个讲究：其一，重试要挑对象——网络抖动和超时值得自动再试，被限流（429）就不能自动连发，否则是在火上浇油；其二，重试次数封顶，别写无限循环——本文给的"一次"是练手版够用的值。更系统的重试策略（指数退避那些名词）留给正式项目，你知道方向在哪就行。

##### 响应也要安检：状态码这道门

请求层的另一块加固是"别把服务器的话全当好消息"。URLSession 返回的第二个值就是响应，里面有状态码——200 才继续解析，其他一律当失败处理：

::: div .code-block
:::inline div .code-head
<span>SWIFT · service 里检查状态码</span><span class="dots">···</span>
:::

```
enum ServiceError: Error {
    case serverError(Int)      // 带上状态码，界面好分级
}

let (data, response) = try await URLSession.shared.data(from: url)
if let http = response as? HTTPURLResponse, http.statusCode != 200 {
    throw ServiceError.serverError(http.statusCode)
}
```
:::

这样 ViewModel 的 catch 就能区分"服务器拒绝了（401/429）"和"网络根本没通"两类失败，各自配文案。参数化一下更好——把 200 写死改成"2xx 都算成功"的区间判断，服务偶尔返回 201、204 时就不会误伤。练手版不检查状态码也能跑（成功路径都是 200），但"安检门"装上的那一天，你的错误处理才算闭环。

##### 取消：用户走了，请求该停

界面里用 <code class="inline">.task</code> 发起的请求自带生命周期管理：页面关闭，任务自动取消，请求在系统层面停掉。被取消的调用会抛出 CancellationError——注意它的待遇和其他错误不同：取消不是"查不到城市"，不该弹报错，安静退出就好（第九节的 catch 里已经用 <code class="inline">!(error is CancellationError)</code> 把它摘出来了）。一件小事就能看出工程成熟度：用户快速进出页面的瞬间，App 是在后台默默浪费流量，还是干净利落地收手。

##### 什么时候该把请求层"写厚"

练手项目，薄薄一层 service 加三态就够，别提前装修。但三个信号出现时，就该把超时、重试、取消收编进 service 层了：要上架给真用户；接口开始变多（预报、城市列表各一个）；或者你发现自己把同样的 try await 复制进了三个页面。收编的方式和记账本"收编删除逻辑"一个路数——每类知识只住一个地方，将来第 68 章讲架构可测试性时，这层会是你第一个"能注入、能替换"的零件。

方向别搞反：写厚 service 是收编"和服务器打交道的知识"，不是收编一切。见过有人把界面文案、转圈颜色都塞进 service 层——从此这一层改个提示词都要小心翼翼。分层的边界永远是"知识的种类"：网络知识住 service，状态知识住 ViewModel，长相知识住视图。越界一次，下次就会越界十次。

#### 十、FAQ：写联网 App 时你真的会问出口的问题

<strong>问：系统自带天气挺全的，我为什么要自己写一个？</strong>

答：因为你要学的不是"天气"，是"联网"：申请 API、解析 JSON、三态管理、密钥安全——新闻、汇率、翻译、股票，任何联网 App 都是这套流程。天气只是最小最直观的练习载体。顺便，自己的 App 想显示什么字段自己定，这也是乐趣。

<strong>问：和风天气和 OpenWeatherMap，到底选哪个？</strong>

答：练手阶段哪个都行——本章用 OpenWeatherMap 走完了全流程。选型的真正考量是：用户在哪（国内数据源好不好）、中文支持、免费额度口径、以及将来收费了成本如何，以两家官网为准。好消息是分层架构下换供应商只动 service 一层——先随便选一个跑通，选型焦虑留给正式产品。

<strong>问：我的仓库是私有的，Key 写代码里没事吧？</strong>

答：私有仓库风险确实低，但不是零——协作者能看到、仓库可能转公开、本地代码可能被截图发群。xcconfig 方案的成本几乎为零，一次配置终身受益，而且它逼你养成"密钥是秘密"的意识——这个意识在以后接支付、接登录时值很多钱。

<strong>问：返回的 JSON 好几十个字段，模型要全部定义吗？</strong>

答：不用。Codable 只解码你声明的字段，JSON 里多余的自动忽略。按界面需要取：本章只要了天气描述、温度、湿度、城市名，其他几十个字段眼不见为净。以后要展示了再回来加——加字段是良性的小改动。

<strong>问：WeatherKit 免费吗？我该直接学它吗？</strong>

答：额度和收费以官网为准，不在这儿背数字。给你的路线建议是：先用免费第三方把"联网三件套"的套路学会，WeatherKit 要申请账号和 entitlement、配置步骤更多，等你有正式上架目标再去接——套路会了，换哪家都只是一晚上的事。

<strong>问：模拟器里能测断网吗？还是要真机开飞行模式？</strong>

答：模拟器能——关掉 Mac 的网络，或用 Network Link Conditioner 模拟。真机开飞行模式更接近真实用户（蜂窝和 Wi-Fi 的切换行为更复杂），所以验收清单才写"最好真机来"：模拟器管开发期快测，真机管交付前终验。

<strong>问：想显示未来几天预报，要重学一遍吗？</strong>

答：不用，就是同一套流程再来一轮：浏览器预习 forecast 接口的 JSON → 加模型 → service 加一个方法 → 界面多一屏列表。你会发现这轮比这章快得多——套路长在手上之后，"接新接口"从大工程变成流水活。

<strong>问：搜索框每打一个字就发一次请求，要不要拦？</strong>

答：要拦，而且本章的写法天然就拦住了——onSubmit 是用户点"搜索"才发，输入过程零请求。如果以后做"边输边联想"那种实时搜索，才需要真正的防抖（输停几百毫秒才发）。这个需求离你现在不远，先记住名词，到时搜"防抖 debounce"。

<strong>问：服务器返回 HTTP 200，内容却是错误提示，怎么回事？</strong>

答：不少服务习惯"用 200 包一切"，真正的成败写在响应内容的字段里（比如一个 code 或 success 字段）。这就是预习的价值——把成功和失败两种返回都看一眼，别只测成功路径。遇到这种服务，解析完先检查业务字段，再决定进 success 还是 error，别拿状态码当唯一的裁判。

<strong>问：调试用的 print 要留着吗？以后排查问题方便。</strong>

答：不留。调试 print 的使命结束了就该清场——留着它们，一来输出刷屏淹没有用信息，二来哪天把带密钥线索的日志带进了仓库，就重演第一节的泄露剧本。正经做法是接系统日志框架（OSLog），按需开关、分级输出，第 67 章调试一节会给你完整方案。现阶段纪律就一条：问题查完，print 删干净。

<strong>问：Wi-Fi 和蜂窝下请求行为不一样吗？</strong>

答：代码层面没有区别——URLSession 不管底下是哪种管道。体验层面差别巨大：蜂窝带宽窄、延迟高、还会在地铁里断。这就是为什么弱网模拟要开、真机终验要走：Wi-Fi 里一切美好的假设，蜂窝和隧道都会替你推翻一遍。

<strong>问：自动查天气应该写在 onAppear 里还是 init 里？</strong>

答：用 .task 修饰符，别用前两个。init 里发请求是典型反模式——视图结构体随时重建，init 会被反复触发，请求跟着滥发；onAppear 不管取消，页面关了请求还在飞。.task 是为这个场景设计的：页面出现时启动、消失时自动取消，一举两得（第九节的取消机制就吃这个红利）。小差别，大习惯。

<strong>问：我想一次查五座城市的天气，行吗？</strong>

答：行，而且方法比你想象的多——循环里 await 五次是最朴素的写法（慢但简单）；并发同时发五条要用任务组（TaskGroup）这类进阶工具，名字先记住，别现在学——它涉及并发调度，第 68 章的并发要点读完再回来，十分钟就懂。练手阶段五次循环请求完全够用，免费额度也扛得住。

<strong>问：界面上想显示网络图片（比如天气大图）怎么办？</strong>

答：SwiftUI 有现成的 AsyncImage 组件——给它一个 URL，它自动完成"下载、转圈占位、显示"全套，写法和本章三态如出一辙。不过先忍住：SF Symbols 的矢量图标在本章够用且不耗流量；等你做新闻类 App 必须加载网络图时，再上 AsyncImage——那时你会发现自己已经能预判它内部的转圈和失败逻辑了。

<strong>问：三态这套 switch 每个联网页面都要写一遍，能不能抽成通用组件？</strong>

答：能，而且值得——把"loading 转圈、error 带重试、成功显示内容"封装成一个通用容器视图，是第 68 章架构进阶的现成练习题。但排序有讲究：等你写过第二个联网页面、体会到复制粘贴之痛之后再抽，抽出来的才是对的抽象。第一次就抽，多半抽歪——这是"规则是三次"原则的又一例证。

#### 十一、与安卓篇对照：同一片网络，两种航法

第 55 章用 Kotlin + Retrofit 做过一模一样的天气 App。两章对照着读，你会发现联网编程的"思想套餐"跨平台通用——三态、密钥、错误分级，一个都不少，零件名不同而已。更往前一步，第 53 章（安卓的数据存储与网络请求）对应本章的底座第 64 章——两大篇的知识地图几乎是镜像的，学的时候对照走，效率翻倍。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">环节</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">本章（iOS）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">第 55 章（安卓）</th></tr></thead><tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">网络库</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession + async/await</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit + 协程</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">JSON 解析</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Codable（编译器生成）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gson（反射填充）</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">界面三态</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">enum + 关联值</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">sealed class</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">密钥存放</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">xcconfig + Info.plist</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">local.properties + buildConfig</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数据变界面</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Observable + switch</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">StateFlow + collectAsState</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">错误分级</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLError 分支 + statusCode</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">异常分类捕获 + 状态码</td></tr>
</tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
天气项目两端对照

三处差异值得咂摸。其一，接口描述方式：Retrofit 用注解"声明"接口（写个方法签名，框架替你生成请求），URLSession 这边手拼 URLComponents——前者像填表，后者像写信；SwiftUI 生态也有类似的声明式网络库，思路相通，学会本章的手拼再看那些库会非常顺。其二，解析机制：Codable 是编译期生成映射，写错字段名编译器就有意见；Gson 靠运行时反射，错了要到跑起来才炸——这也是为什么安卓篇更强调"先看原始 JSON"。其三，三态的载体：SwiftUI 的枚举关联值和 Kotlin 的 sealed class 是同一枚硬币的两面——都把"互斥状态+附带数据"做成类型系统的事，鬼状态在两边都无处容身。

还有一条值得放在历史视野里看：两边的网络写法都在演进。早年回调嵌回调的"金字塔"在两端都是噩梦，后来的 Promise/Future、Rx 系流式方案各有拥趸，如今 iOS 的 async/await 和安卓的协程殊途同归——把异步代码写成"看起来同步"的一条线。你现在学的就是这代最新姿势，以后看到老项目里的回调地狱，别怕，那只是历史包袱，不是你要追的时尚。

学完本章再翻第 55 章，大概只需要三分之一的时间——你已经知道每个零件是干嘛的，只是换个名字认人。鸿蒙篇第 77 章的天气助手应用同理：ArkTS 的 async 请求与三态渲染，和本章的思想完全同源，三大端各写一遍天气，你对"联网 App"的理解就通了底。

#### 十二、扩展练习：往第二屏走

主界面跑通后，八个练习按性价比排序。做完前两个，App 就有"多城市"的骨架了。

<strong>练习一：城市列表页（性价比之王）</strong>。把收藏城市变成一屏滚动列表：NavigationStack 推一个新页面（第 63 章的导航栈正好用上），List 每行一座城市，点行回主页并查询该城。顺手在列表页支持下拉刷新所有收藏城市的温度——.refreshable 再用一次就熟了。

<strong>练习二：磁盘缓存</strong>。把 lastGood 用 Codable 编码成 JSON 存进沙盒（第 64 章的方案任选），启动时先读缓存再发请求。验收动作：杀掉 App、开飞行模式、重新打开——天气画面还在，顶着"旧数据"小字。这一步做完，你的 App 在最差网络下也能看。

<strong>练习三：请求节流</strong>。ViewModel 记住每座城市上次请求的时间，间隔没到就返回缓存不重发——省额度也省流量，间隔阈值自己定。第七节病例六的"请求编号"也可以一并做了，两个一起治"连点风暴"。

<strong>练习四：预报页</strong>。接同一家服务的多天预报接口——预习、建模、加方法、加页面，四步走完你就有了第二屏。到时你会发现自己查文档的速度比写代码还快，这就是套路成型的标志。

<strong>练习五：换供应商演练</strong>。用和风天气再实现一遍 fetchWeather——只许动 service 和模型，ViewModel 与界面一行不改。如果改得动，说明分层真的成立；改不动的地方，就是耦合漏出来的位置，顺手重构掉。

<strong>练习六：一条天气提醒</strong>。本地通知实现的"明天有雨，记得带伞"——判断逻辑放在拿到天气之后，通知申请姿势和节制原则第 68 章细讲。和记账提醒一样：一天一条是上限。

<strong>练习七：给解析写单元测试</strong>。把预习时存的那份样例 JSON 放进测试 bundle，写一个测试：decode 成 WeatherResponse 后断言 temp、humidity 的值。这一步把"解析对不对"变成机器看门的规则——以后服务方偷偷改字段格式，你的测试第一时间变红。内存容器那套思路（上一章）加这份假数据，测试的两大套路你就都摸过了，第 67 章正式系统学。

<strong>练习八：把三态界面抽成可复用组件</strong>。等你把第二个联网页面做完（练习四的预报页），复制粘贴的痛感就真实了——这时把"loading 转圈、error 带重试、成功显示内容"封装成一个通用容器，多个页面共用。怎么抽、抽成什么样，第 68 章的架构进阶会给完整示范，这里的练习是给你攒"为什么要抽"的切身感受。

做完别急着走，照上一章的三段式复盘一段：做了什么、卡在哪、下次提前做什么。联网项目最值得记的通常是"那次解析为什么失败"——你踩过的每个字段坑，都是下个项目的免疫。

给你一张七天上手日历：第一天，密钥进 xcconfig + 第一次真请求；第二天，模型与服务 + 临时验证视图；第三天，三态 + 错误分级 + 缓存旧数据；第四天，主界面拼装 + 图标映射 + 深色模式过一遍；第五天，searchable + 收藏城市 + 下拉刷新；第六天，弱网模拟 + 抓包走一遍 + 验收清单六条；第七天，开做练习一和练习二，真机终验。

#### 十三、界面细节打磨：天气 App 的"最后一层皮"

功能全通了，最后这层皮决定它像"作业"还是像"产品"。先说时机：打磨要整块做——功能验收通过的当晚，专门留两个小时只过细节，别边写新功能边抠间距，两头都慢。天气 App 的打磨清单不长，六条，一晚上能过完。

<strong>动态字体与大数字的分工</strong>。76 号细字重的温度是设计选择，可以写死；但页面其余文字——城市名、天气描述、湿度行——都用 .title、.body 这类语义字体，让系统字号设置生效。判断标准：把模拟器字号调到最大档，正文还能读、排版还不崩，及格。

<strong>给 VoiceOver 一份像样的讲稿</strong>。默认情况下旁白会把温度念成"26"——配上 <code class="inline">.accessibilityLabel("当前气温 26 摄氏度")</code>，听感立刻正常。给天气图标也补一句描述（"晴天图标"），旁白用户才知道那朵云在说什么。十分钟的活儿，第 65 章立过的规矩，这个 App 照做一遍。

<strong>给大数字留呼吸感</strong>。76 号数字上下各留足间距——它需要孤独感才好看；挤在两行文字中间，气场就塌了。spacing 别用系统默认了事，这个页面值得手动调。

<strong>三态共用同一张网格</strong>。加载、成功、失败三个画面切换时，搜索框位置不动、标题位置不动，只有中间区域变化——别让界面在状态切换时"跳"。用户的安全感就来自这种稳定。

<strong>初载占位</strong>。首次进页面那几百毫秒，与其干转圈，不如让卡片位置先出现一块浅色占位——加载完成内容原地替换。做不做都行，但知道有这个手法，将来列表页用得上。

<strong>反馈要"摸得到"</strong>。查询成功时来一下轻微的触感反馈，下拉刷新收手时一下轻震——系统有现成的触觉 API，一两行代码。别滥用：每次转圈都震等于没震；只在"状态落地"的时刻（出结果、出错误）给一下，用户闭着眼也知道"来了"。

<strong>状态切换配一点动画</strong>。三态切换时内容生硬地"跳变"，包一层 withAnimation 让天气卡片淡入，观感立刻柔和。克制原则照旧：动画只用于交代"内容从哪来"，别给转圈加弹跳。

还有一个土办法屡试不爽：把打磨前后的界面各截一张图，并排放在相册里看十秒。单看一张"挺好的"，并排一比就见高下——哪块间距松了、哪个颜色脏了，肉眼自己会指出来。人眼是差评师，你得给它制造对比的机会。

<strong>深浅色和真机各过一遍</strong>。三态 × 深浅色是六种组合，挨个截图看一遍；再上真机滚动、搜索、刷新各来一次。模拟器管快，真机管真——上一章的规矩原样适用。

#### 十四、数据与隐私：联网 App 的第一课

从这一章起，你的 App 开始"往外发东西"了——隐私意识要跟上。先把账算清楚：这个天气 App 发出去的东西只有两样，用户输入的城市名和你的 API Key。城市名不算敏感信息，但你依然该在界面上让用户"看得见"——搜索历史、收藏列表都在明面上，别搞暗箱。如果哪天你接了定位（练习清单外的进阶），性质就变了：位置是敏感个人信息，申请权限的时机、用途说明，第 68 章会专门讲，原则只有一条——用到才申请，申请就说清用途。

上架那一刻，隐私话题会正式登门：App Store 要求你填写隐私标签，声明 App 收集了哪些数据、是否与第三方共享。对这个天气 App，如实回答多半是"不收集"——搜索框方案连设备信息都没碰。这个流程的意义在于逼你盘点一遍自己的数据流：发出去什么、存在哪、要不要用户同意。现在养成盘点习惯，将来接登录、接支付时就不会两眼一抹黑——隐私不是审核关卡，是产品底线，第 6 章的安全意识在开发者这一侧同样成立。

还有一条关于"数据的归宿"：收藏城市存在本机沙盒里，用户卸载 App 就全部消失——这是当前设计的正确姿势，数据跟着用户走、用户说了算。哪天你给 App 加云同步（iCloud 那条进阶路），数据的归属和去向就复杂了一层：同步前先想清楚"用户的收藏住在哪里、谁能看到它、用户怎么删掉它"——这三个问题答得清，云同步才配上线。

<strong>问：Key 用了一阵想换一个新的，要改哪些地方？</strong>

答：只改一个地方——xcconfig 里的那一行。这正是密钥进配置文件的回报：代码零改动，重新构建运行就换了心脏。顺带立一条运维小习惯：给自己的 Key 记个"生日"（什么时候申请的、用在哪几个项目），将来某个服务突然 401，你能秒答"哪把钥匙开哪扇门"。

<strong>问：将来真有用户了，他们遇到的报错我怎么知道？</strong>

答：现在还不用操这个心，但路线要知道——上架后接崩溃上报和远程日志，用户端出的问题才能"飞回"你面前，第 67 章上架一节会带（崩溃上报也在它的清单里）。现阶段能做的是把地基打好：三态文案写全、错误分支不漏、本地调试三招用熟——你本地能复现的错，用户端就少一半；你写清楚的文案，将来日志里就好认一半。

#### 十五、套路迁移清单：下一个联网 App，你已经会了

把这章的手艺摊开数一数，你会发现它是一张可复用的施工清单——做任何联网 App 都按这个顺序走：

- <strong>申请 Key</strong>：选服务、注册、拿 Key 进 xcconfig（密钥管理的三步走原样照搬）；
- <strong>预习 JSON</strong>：浏览器先打一发，把返回存成样例文件；
- <strong>建模型</strong>：照样例抄字段，Codable 对号入座；
- <strong>封 service</strong>：URLComponents 组参数、async throws 一个方法；
- <strong>三态模板</strong>：enum + switch，错别分四级（断网/超时/限流/服务器）；
- <strong>缓存与降级</strong>：lastGood + 数据时间 + 重试入口；
- <strong>调试三招</strong>：安全打印、抓包、弱网模拟。

拿这张清单套三个你可能想做的 App：新闻客户端 = 天气 + 列表页 + 图片加载；汇率换算 = 天气 + 数字格式化（换掉温度换汇率，模型换成一对货币代码）；翻译工具 = 天气 + POST 提交文本（第一次用上 GET 以外的 HTTP 方法）。你会发现差别只在"要解析的 JSON 长什么样"，骨架一模一样——这就是本章标题里"套路"两个字的分量。骨架之外的两块拼图也已就位：第 67 章管测试与上架，第 68 章管权限与架构，学完它们，这个 App 就能从"我能跑"走到"别人能用"。

这张清单还有个用法：面试或复盘时被问"你怎么做联网模块"，照着它从上到下讲一遍——每一条你都真刀真枪做过，讲出来自然有底气。清单在手上不等于熟，每接一个新接口走一遍，走到第三遍，它就长在你手上了。而且你会发现，走第二遍时的"卡点"和第一遍完全不同——第一遍卡在语法和概念，第二遍卡在服务和文档——卡点的前移，就是成长最诚实的刻度。

#### 十六、场景实录：小周的出差一天

写完不如跟着用一天。主角还是第 65 章那位小周——账本刚记满一周，天气 App 也新鲜出炉，正赶上他出差去杭州。出发前一晚他还干了件事：把第七天的日历项清掉，给 App 打了个"v0.1"的 git 标签——不是炫技，是给自己一个"从今天起它算个正式东西"的仪式感，改坏了随时能回到今晚。

早上七点，出门前他打开 App：自动查到收藏里的北京，28 度，晴天。顺手把杭州加进收藏——今晚要用。高铁过隧道，手机断网，他点了下刷新：界面没有崩，也没有白屏，上次的北京数据还在，顶上一行小字"数据时间 07:12 · 暂为旧数据"，下面跟着"没有网络"的提示和重试按钮——三态加缓存的第一战，及格。出隧道网络恢复，点重试，两秒刷新。

中午到了杭州，他兴冲冲输"杭州"查询——失败提示"查不到这个城市"。愣了三秒想起小贴士：服务对中文城市名支持一般。输"hangzhou"，一秒出结果。旁边座位的乘客瞟见了他的屏幕，问"这 App 哪下的？"他咧嘴一笑："没得下，自己写的。"那一秒的得意，比验收清单全过还上头——自己做的 App 在真实世界里被陌生人看见，是练手项目能给你的最高奖励之一。晚上他在酒店把那个十几条的城市映射表写了进去——"北京 → beijing"排在第一行。睡前他想测测"转圈半天"的问题，开了弱网模拟：20 多秒的转圈后弹出了超时文案——文案贴切，重试按钮也还在，但他把 loading 的提示字换成了"网络有点慢，正在尽力查…"，心理感受立刻不一样。

这一天里，他亲手写下的每个零件都接住了真实世界的刁难：三态管住了断网、缓存救了白屏、降级绕过了中文城市、弱网模拟提前揪出了转圈体验。没有一样是"高级技术"——全是这章反复念叨的基础功夫。

按惯例，他给自己写了三段复盘：做了什么——三态、缓存、收藏、降级四件套全落地，验收清单六条过五条（最后一条弱网项改完文案后补过）；卡在哪——中文城市那次最久，根治手段是映射表；下次提前做什么——开工前就把"服务端对中文的支持程度"查清楚，别等用户（自己）在高铁上撞上。这份复盘跟着 git 提交一起留了档。下一章（第 67 章）我们要谈测试、调试与上架，把小周手里这个"自己能用的 App"，变成"能放进 App Store 的 App"。

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 先浏览器试 API、看懂 JSON，再写代码——"预习"永远不亏
- API Key 藏进 xcconfig，绝不进代码库
- Codable 模型 + URLSession async/await：字段对上，JSON 自动解析
- loading/success/error 三段式状态是联网界面万金油
- 断网、空输入、城市不存在——错误处理是联网 App 的及格线
:::
