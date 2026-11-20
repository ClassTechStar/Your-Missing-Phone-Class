---
id: di-wu-shi-wu-zhang
num: 55
part: an-zhuo-kai-fa-pian
nav: 第五十五章：项目二——天气查询App（网络版）
toc: default
kind: chapter
---

### 第五十五章：项目二——天气查询 App（网络版）

{class="chapter-intro mb-4"}
记账本是"练内功"，天气 App 是"见世面"，它要和互联网打交道。这个项目你会学到：申请免费 API、解析 JSON、处理"加载中/成功/失败"三种界面状态，以及怎么把 API 密钥藏好。做完它，你就具备了做任何"联网 App"的能力，新闻、汇率、翻译，套路一模一样。

::: div .quick-read
##### 本章速读（5 分钟版）
这是你的第二个项目，从"练内功"转向"见世面"，做一个天气查询 App，学的是所有联网 App 的通用套路：申请免费 API、解析 JSON、处理"加载中/成功/失败"三种界面状态，以及把 API 密钥藏好。做完它你就明白了：新闻、汇率、翻译类 App 的骨架和这个天气 App 一模一样，等于拿到做任何联网 App 的通行证。

最关键的有三件事。第一，接任何 API 之前先"预习"：注册 OpenWeatherMap 或和风天气这类免费服务拿到 Key 后，先在浏览器里把接口请求一次，亲眼看一遍返回的 JSON 长什么样，字段名、嵌套结构都认熟了，再写 Retrofit 接口和 data class，字段对上，解析自动完成。第二，安全底线只有一条：<strong>API Key 藏进 local.properties，绝不进代码库</strong>，更不能随代码发到网上。第三，联网界面的万金油是三段式状态，加载中、成功、失败，用 sealed class 圈起来，状态一变界面自动换脸；断网、空输入、城市不存在这些错误处理，是联网 App 的及格线，不是加分项。再送一条工程习惯：网络层收拢在一处、数据模型集中管理、界面不直接接触 JSON，服务商改版、字段调整是常态不是意外，隔离好了，变了就只改一处。

今天就能做的最小动作：注册一个免费 API 账号、生成 Key，在浏览器里把天气接口跑通，把返回的 JSON 存下来逐个字段看一遍。这一步不写一行 App 代码，却决定后面顺不顺。然后照章里"五个晚上的推进计划"排期推进，别一口气熬通宵，第一次做联网项目，最怕的还是弃坑。

最大的坑有一半在观念里。有人觉得"断网是边缘情况，最后再说"，其实电梯、地库、高铁隧道，手机大半时间都在网络边缘徘徊，断网体验决定 App 的下限；有人觉得"模拟器上跑通就稳了"，模拟器走电脑网络，又快又稳不掉线，弱网、权限拒绝只有真机能暴露；还有人觉得"缓存是锦上添花"，对天气这种内容，缓存是体验主干。断网瞬间有内容看全靠它撑着。代码层面的五个翻车现场，解析失败一直转圈、超时、主线程联网闪退、一秒十次重复请求、没日志黑盒抓瞎，章里的门诊一节都开了处方。
##### 速查表
- 接口怎么预习：先在浏览器请求一次 API，看懂 JSON 再动手写代码
- Key 放哪：藏进 local.properties，绝不进代码库
- 字段对不上怎么办：用 @SerializedName 把 JSON 字段和模型字段对齐
- 界面三段式：加载中/成功/失败用 sealed class 圈住，状态一变界面换脸
- 断网也要有内容：缓存上次结果，这是体验主干不是可有可无的优化
- 防重复请求：加载中禁用按钮加防抖，别一秒给服务器发十次
- 主线程联网会怎样：当场闪退，网络请求一律放协程里
- 验收怎么过：飞行模式、空输入、城市不存在挨个试，真机模拟器两条腿走路
:::

<div class="version-anchor">本章界面路径按 iOS 18.x / HarmonyOS 5.x / Android 15 核对（2026 年 11 月）。你的机型或系统版本不同，菜单名字和位置可能对不上——以你手机上显示的为准。</div>


#### 一、申请免费天气 API

个人练手，推荐 <strong>OpenWeatherMap</strong> 或国内的 <strong>和风天气（QWeather）</strong>——都有免费额度，注册即用。以 OpenWeatherMap 为例：

1. 注册账号 → 在 API keys 页面生成一个 Key（<code class="inline">apikey</code>）。
2. 免费版可调用 Current Weather（当前天气）接口：<code class="inline">api.openweathermap.org/data/2.5/weather? q=beijing&appid=你的Key&units=metric</code>。
3. 浏览器里先试一次，看看返回的 JSON 长什么样，这是接任何 API 前必做的"预习"。

顺手留意 URL 里那两个参数：<code class="inline">units=metric</code> 和 <code class="inline">lang=zh_cn</code>。摄氏还是华氏、时区、界面语言，这些都得显式处理，别指望服务器替你猜，同一座城市，英文系统和中文系统的手机拿到的返回就不一样。练手阶段把城市写死在代码里没问题，但参数要留出来，后面改成搜索框才不费劲。

##### 动手前先选型：三家服务的取舍

别急着填注册表单。先花十分钟想清楚自己要什么，不然 Key 拿到手才发现接口不对路，又得重来一遍。个人练手常见三个选择，各有脾气：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
  <thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">服务</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">文档与控制台</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">一句话点评</th></tr></thead>
  <tbody>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenWeatherMap</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">英文文档，接口风格直白，社区示例多</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">练手最经典的入门选择，国内访问速度视网络环境而定</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">和风天气（QWeather）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">中文文档，控制台全中文</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">国内城市数据细（有预警、生活指数这类本地化内容），国内读者的顺手之选</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">心知天气</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">中文文档</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">免费额度够练手，和风之外的备选，接口思路类似</td></tr>
  </tbody>
</table>
```
:::

怎么选？第一次接 API，选文档读得最顺的那家——接口调用是"照着文档翻译"的活，文档看不懂，代码写得再对也白搭。本书示例以 OpenWeatherMap 的返回为准，但你以后想换成和风，只需要改 URL 和数据模型，本章后面讲的所有套路（三态、缓存、错误分类）一行都不用动。

再替两类人把话说在前头：想给爸妈用的，优先考虑国内服务，天气描述是中文，还带预警推送；想顺便练英语的，OpenWeatherMap 的文档短句多，读起来正好当阅读理解。注册都需要开发者账号，有的服务还要多一步实名或认证，以官网指引为准，别被多出来的流程吓退。

##### 注册与拿 Key：一次真实的流程

各家注册大同小异：邮箱、验证、进控制台。拿 OpenWeatherMap 走一遍，别家界面不同、路数一样：

1. 打开官网，右上角找 Sign Up，用邮箱注册：验证邮件有时会掉进垃圾箱，收不到先去那里翻。
2. 登录后进控制台（菜单叫 API keys 或类似名字，以官网为准）。
3. 页面里通常已经躺着一个默认生成的 Key，也可以自己再生成一个，点一下就复制。
4. 把这串 Key 存进手机备忘录或电脑记事本，下一步马上要用，但别存进任何会公开的地方。
5. 找到 Current Weather 接口的文档页，把示例 URL 抄下来，把 <code class="inline">appid</code> 的值换成你的 Key。
6. 浏览器地址栏粘贴，回车，看到一坨 JSON 就说明 Key 能用了。

三个提醒，都是过来人的眼泪：一是有些服务的 Key 不是生成就能用，可能要等几分钟到几小时（视服务商而定），期间请求会报错，别慌，去喝杯水再试；二是免费额度一般按"每天多少次"或"每月多少次"计，具体数字以官方页面为准：练手绰绰有余，但别拿去跑脚本刷；三是注册邮箱要留真实常用的，Key 出异常时服务商靠它联系你。

##### 在浏览器里"预习"JSON

注册完先别开 Android Studio。把带 Key 的完整 URL 粘进浏览器地址栏，回车，你会看到一坨挤成一行的 JSON。装个浏览器的 JSON 格式化插件，或者把内容粘进任意"JSON 格式化"网页工具，层级立刻一目了然。大概长这样（节选，实际返回更长，数值以你的真实请求为准）：

::: div .code-block
:::inline div .code-head
<span>JSON · 当前天气接口返回（节选）</span><span class="dots">···</span>
:::

```
{
  "coord": {"lon": 116.4, "lat": 39.9},
  "weather": [
    {"id": 800, "main": "Clear", "description": "晴", "icon": "01d"}
  ],
  "main": {
    "temp": 26.5,
    "feels_like": 27.1,
    "temp_min": 24.0,
    "temp_max": 29.0,
    "pressure": 1010,
    "humidity": 40
  },
  "wind": {"speed": 3.2, "deg": 120},
  "sys": {"country": "CN", "sunrise": 1730000000, "sunset": 1730040000},
  "name": "Beijing"
}
```
:::

逐层读一遍：<code class="inline">coord</code> 是坐标；<code class="inline">weather</code> 是个数组：所以等会儿的数据模型里它是 List；<code class="inline">main</code> 里躺着温度、体感温度、湿度；最外层的 <code class="inline">name</code> 是城市名。练手阶段你只用得上一小半字段，但每一层都要能说出它是干嘛的。

预习时带着三个问题看，效率翻倍：

- <strong>哪些字段是界面要用的</strong>：温度、湿度、描述、城市名，记下它们的确切拼法，一个字母都不能错。
- <strong>字段藏在第几层</strong>：description 不在最外层，而在 weather 数组的对象里，新手十个解析错误八个栽在层级上。
- <strong>出错时返回什么</strong>：把城市名故意改错再请求一次，看看错误返回长什么样。这个"错误预习"比成功预习还有用，后面错误处理全靠它。

把格式化好的 JSON 存成一个文件放桌面。等下写数据模型的时候对照着敲，等于开卷考试。

##### 把 URL 拆开看：每个参数都有脾气

别把那串 URL 当天书，拆开就四个参数：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
  <thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">参数</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">你填什么</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">不填或填错会怎样</th></tr></thead>
  <tbody>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">q</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">城市名（如 beijing、shanghai）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">请求直接报错，什么都查不到</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">appid</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">你的 Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">错一个字母就 401，服务器拒之门外</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">units</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">metric（摄氏）或 imperial（华氏）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">默认给你开尔文——看到 300 多"度"别以为自己查的是火星</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">lang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">zh_cn 等语言代码</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">天气描述默认英文，界面瞬间变"双语教学"</td></tr>
  </tbody>
</table>
```
:::

开尔文这个梗值得展开一句：新手第一次不带 units 请求，看到 temp=301.15 会怀疑人生——那是开尔文温度，减 273.15 才是摄氏 28 度。很多人下意识去代码里做减法，其实加个参数就解决了，服务器比你算得准。

还有重名问题。全世界叫"朝阳"的地方不止一个，单写一个拼音，服务器返回哪个得看它的心情。主流服务商普遍支持"城市名,国家代码"的写法来消歧义，具体格式以官方文档为准，反正记住一条：查询越精确，结果越靠谱。

##### Key 配好了却报 401：四个常见原因

错误示范来了：有人 Key 复制粘贴完，浏览器里请求，回车，返回一串"Invalid API key"，当场怀疑人生。先别改代码，401 的病根基本就这四个：

- <strong>Key 还没生效</strong>：有些服务商生成后要等一会儿，等几分钟再试。
- <strong>复制带了空格或少了字符</strong>：从 PDF、聊天窗口复制 Key 特别容易带尾随空格，肉眼看不见，服务器看得见，重新完整复制一遍。
- <strong>用错了参数名</strong>：参数名是 appid，不是 api_key 也不是 key，照文档抄。
- <strong>请求打错了门</strong>：免费 Key 只能调免费接口，你要是手滑调了付费接口（比如历史数据），一样 401。

按这四条排一遍，90% 的 401 当场解决：剩下的一成去服务商的控制台看 Key 状态，或者重新生成一个。别急着怀疑人生，也别急着去论坛发帖，先自查。

##### Key 藏进 local.properties：三步实操

上面那条避坑提醒不是吓唬人。公开仓库里的 Key 几小时内就会被自动脚本扫走，有人凌晨提交、早上醒来收到服务商的盗刷警告，全程睡得一无所知。现在就照下面三步把 Key 藏好。

第一步，把 Key 写进 <code class="inline">local.properties</code>（项目根目录下就有这个文件，它默认被 gitignore 忽略，不会上传）：

::: div .code-block
:::inline div .code-head
<span>PROPERTIES · local.properties</span><span class="dots">···</span>
:::

```
# 这个文件不会进仓库，Key 放这里最安心
WEATHER_KEY=你刚才复制的那串Key
```
:::

第二步，在模块级 <code class="inline">build.gradle.kts</code> 里把它读出来，注入 BuildConfig：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · build.gradle.kts（模块级，节选）</span><span class="dots">···</span>
:::

```
import java.util.Properties   // 放在文件最顶部

val localProps = Properties()
val localFile = rootProject.file("local.properties")
if (localFile.exists()) {
    localProps.load(localFile.inputStream())
}

android {
    // 较新的 Gradle 插件版本默认不再自动生成 BuildConfig，要手动打开
    buildFeatures {
        buildConfig = true
    }
    defaultConfig {
        buildConfigField(
            "String",
            "WEATHER_KEY",
            "\"${localProps.getProperty("WEATHER_KEY") ?: ""}\""
        )
    }
}
```
:::

第三步，点一下 Gradle 同步（编辑器右上角的 Sync Now），之后代码里就能用 <code class="inline">BuildConfig.WEATHER_KEY</code> 取到 Key 了，它编译时被写进一个自动生成的类里，源码里找不到明文。

验证方法很简单：随便改个文件，跑一下 <code class="inline">git status</code>，待提交列表里没有 local.properties 就对了。再不放心，等仓库推上去之后，自己在网页端全局搜索那串 Key，搜不到，才算真藏好了。换电脑或同事拉代码时要重建 local.properties，这不是麻烦，这正是设计目的：机器相关的私密东西，本来就不该跟着仓库跑。

##### 换个服务商要改哪几处：为迁移留后路

替你预演一个场景：某天免费额度收紧，或者你想要国内特有的预警数据，决定从 OpenWeatherMap 换到和风天气。这时候代码收得干不干净，差距就显出来了，收得干净的换一次十分钟，写散了的得翻遍整个项目。

要动的其实只有四处：baseUrl（换域名）、接口定义（路径和参数名跟着新文档走）、数据模型（对照新服务商的 JSON 重新建，字段名几乎必然不同）、错误码翻译（404 在各家含义不完全一样）。要不动的地方更多：三态界面、缓存逻辑、ViewModel 骨架、整个 UI：这些一行都不用碰。

想享受这种"只改一处"的待遇，前提是本章开头就做对一件事：把网络层收进独立的文件，界面永远只跟 ViewModel 说话，ViewModel 只跟网络层说话。练手项目最容易犯的懒是把请求直接写在界面代码里：图一时之快，改的时候翻倍还债。

#### 二、网络层：Retrofit + JSON 解析

先照 API 返回的 JSON 定义"数据模型"，字段对不上的一律忽略：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 数据模型 + 接口</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"晴"}],"main":{"temp":26.5,"humidity":40},"name":"北京"}
data class WeatherResponse(
    val weather: List&lt;Weather&gt;,
    val main: Main,
    val name: String
)
data class Weather(val description: String)
data class Main(val temp: Double, val humidity: Int)

interface WeatherApi {
    @GET("data/2.5/weather")
    suspend fun getWeather(
        @Query("q") city: String,
        @Query("appid") key: String,
        @Query("units") metric: String = "metric",
        @Query("lang") lang: String = "zh_cn"
    ): WeatherResponse
}
```
:::

Gson 会自动把 JSON 塞进这些 data class<strong>字段名一致，魔法自动发生</strong>。

联网前还得跟系统打两声招呼。一是 <code class="inline">INTERNET</code> 权限：它属于普通权限，装上即生效、不用运行时申请，但 Manifest 里忘了声明，联网请求会直接失败；二是明文流量：系统默认拦截 http 明文请求，开发时若用 http 的测试接口要留意，正式接口一律 https。

##### 为什么选 Retrofit，而不是自己撸 HTTP

你可能纳闷：联网不就是发个网址吗，为啥要请一个"框架"？看看不用框架的惨状：自己拼 URL、自己开线程、自己把字节流转成字符串、自己 new 一个 Gson 解析、自己处理五花八门的异常：五六件事连着做，每一件都有翻车机会，而且翻完车你都不知道翻在哪一环。

Retrofit 把这些杂活按注解分派：<code class="inline">@GET</code> 声明路径，<code class="inline">@Query</code> 声明参数，<code class="inline">suspend</code> 声明这是个挂起函数。你只负责写清楚"这个接口长什么样"，至于怎么发请求、在哪个线程发、返回的 JSON 怎么变成对象，它全包了。声明完的接口看起来像一份说明书，而不是一段揉成一团的逻辑。

生态也是理由：要加日志就插一个拦截器，要统一加请求头再插一个，想换 JSON 库换个转换器，都是插拔的事，不用动核心代码。这些"以后肯定要加"的东西，正是框架和手写的分水岭。

##### 加依赖：改一个文件，同步一次

打开模块级 <code class="inline">build.gradle.kts</code>——注意是模块级，不是项目级，新手十个有八个先改错文件。在 dependencies 块里加三行：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · build.gradle.kts（模块级）</span><span class="dots">···</span>
:::

```
dependencies {
    // 三个库的最新稳定版本号，以各自官方文档为准，别抄旧教程里的老版本
    implementation("com.squareup.retrofit2:retrofit:填最新稳定版")
    implementation("com.squareup.retrofit2:converter-gson:填最新稳定版")
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-android:填最新稳定版")
}
```
:::

改完点右上角 Sync Now。第一次下载依赖要等一阵子，进度条卡住多半是网络问题，切换网络重试，别急着删项目重建，删了重下只会更慢。三个库各管一摊：retrofit 是骨架，converter-gson 负责 JSON 和对象互转，coroutines-android 让 suspend 函数在 Android 上安心跑。

##### 搭出 Retrofit 实例：一次基建，全局共用

依赖到位，把"翻译官"造出来。全 App 造一份就够，放在一个单独的文件里（练手阶段写成全局单例即可）：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Retrofit 实例</span><span class="dots">···</span>
:::

```
val retrofit = Retrofit.Builder()
    .baseUrl("https://api.openweathermap.org/")   // 结尾的斜杠不能少
    .addConverterFactory(GsonConverterFactory.create())
    .client(
        OkHttpClient.Builder()
            .connectTimeout(15, TimeUnit.SECONDS)
            .readTimeout(15, TimeUnit.SECONDS)
            .build()
    )
    .build()

val api = retrofit.create(WeatherApi::class.java)
```
:::

两个坑写在注释旁边还不够，单独说：一是 <code class="inline">baseUrl</code> 必须以斜杠结尾，少一个斜杠运行时直接崩，报错信息还不明说原因，很多人对着屏幕研究半小时；二是接口注解里的 <code class="inline">data/2.5/weather</code> 会和 baseUrl 拼接成完整地址，所以接口里别再写域名，写了就重复，请求直接 404。

<code class="inline">retrofit.create()</code> 拿到的对象，就是你在接口文件里写的那份"说明书"的实体。之后 ViewModel 里只管调 <code class="inline">api.getWeather("beijing")</code>，一行就是一个网络请求。

##### 字段对不上怎么办：@SerializedName 与两个暗坑

Gson 靠字段名匹配：JSON 里叫 description，data class 里也叫 description，对上就自动塞进去。但如果服务商用了奇怪的名字，或者你想给自己的变量起个更顺口的名呢？用 <code class="inline">@SerializedName</code> 给字段起个"外号"：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 字段改名映射</span><span class="dots">···</span>
:::

```
data class Weather(
    @SerializedName("description") val desc: String
)
```
:::

JSON 里叫 description，你代码里叫 desc，中间靠注解翻译。这招在服务商改字段名、或者字段名起得稀奇古怪的时候特别救命。

两个更隐蔽的暗坑也交代清楚。第一个：Kotlin 的空安全管不住 Gson，JSON 里缺了某个字段时，Gson 用反射赋值，能把 null 塞进你声明为非空的 String 里，编译期一声不吭，运行时用到才炸。所以拿不准一定有的字段，声明成可空（<code class="inline">String?</code>）或者给默认值。第二个：层级必须照着 JSON 抄，main 是个对象，你模型里就得再有 data class Main 嵌着，错一层都塞不进去。这两个坑占了解析问题的大半，出问题时先回头对照浏览器里那份 JSON。

顺带一句进阶选项：Moshi 和 kotlinx.serialization 是 Gson 之外的流行选择，对 Kotlin 空安全更友好，编译期就能帮你抓问题。练手用 Gson 完全没问题，以后写正式项目可以换过去：换库只动转换器一行，这正是用框架的好处。

##### 接口文件完整模板：照着建一个

把前面散落的内容合起来，一份完整的 WeatherApi.kt 长这样，新建文件时照着搭，然后把包名换成你自己的：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · WeatherApi.kt 完整模板</span><span class="dots">···</span>
:::

```
package com.example.weatherapp   // 改成你项目的包名

import retrofit2.http.GET
import retrofit2.http.Query

data class WeatherResponse(
    val weather: List&lt;Weather&gt;,
    val main: Main,
    val name: String
)
data class Weather(val description: String)
data class Main(val temp: Double, val humidity: Int)

interface WeatherApi {
    @GET("data/2.5/weather")
    suspend fun getWeather(
        @Query("q") city: String,
        @Query("appid") key: String,
        @Query("units") metric: String = "metric",
        @Query("lang") lang: String = "zh_cn"
    ): WeatherResponse
}
```
:::

顶部那两行 import 别手敲，写到 <code class="inline">@GET</code> 时 IDE 会报红字，按住提示键让它自动导入，比照着抄又快又不会错。红字是 IDE 在提醒"这里我不认识"，别无视它，越攒越难收拾。

##### 多学两招：@Path、@Body 与公共参数

本章的接口只用到了 <code class="inline">@Query</code>，但注解家族还有几个成员，早晚用得上。<code class="inline">@Path</code> 把参数嵌进路径本身。像 <code class="inline">@GET("users/{id}")</code> 配 <code class="inline">@Path("id")</code>，适合"按编号取某一条"的接口。<code class="inline">@Body</code> 则把整个对象变成请求体发出去，做登录、提交表单这类 POST 请求时登场。天气 App 一个都用不上，先混个脸熟，做到别的联网项目时不至于发懵。

参数多的时候有个小技巧：在接口方法里给默认值：本章的 units 和 lang 就这么干的，调用处只写 <code class="inline">api.getWeather("beijing")</code>，一行搞定，不用每次重复传那两个参数。

还有更进一步的玩法：Key 这种每个请求都要带的东西，可以用 OkHttp 拦截器统一塞进每个请求，接口里连 appid 参数都不用声明，搜"OkHttp 拦截器 添加公共参数"照着做，几行代码的事。练手阶段可以先不做，但知道有这条路，等接口多起来你会回来用。

##### 权限与明文流量：把两声招呼说全

INTERNET 权限只要在 Manifest 里加一行，放在 application 标签外面：

::: div .code-block
:::inline div .code-head
<span>XML · AndroidManifest.xml（节选）</span><span class="dots">···</span>
:::

```
&lt;uses-permission android:name="android.permission.INTERNET" /&gt;
```
:::

明文流量指的是 <code class="inline">http://</code> 开头的裸请求，内容不加密，中间人能看也能改，所以系统默认拦截。正规服务商的接口早就全上了 https，你要是还连着 http 的老接口，要么让服务方升级，要么查一下"网络安全配置"的官方文档做临时放行，但练手也建议直接用 https，别养成习惯。

怎么分清是权限问题还是代码问题？Manifest 里没声明 INTERNET 时，日志里会有清清楚楚的 SecurityException 字样。看到它，先去检查 Manifest，别在业务代码里大海捞针：方向错了，越找越远。

##### 五分钟验证：先让日志出天气，再谈界面

界面还没写，怎么确认网络层真的通了？写个最小的验证入口：临时在按钮点击或启动日志里直接调一次接口，把结果打到 Logcat：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 最小验证片段</span><span class="dots">···</span>
:::

```
viewModelScope.launch {
    try {
        val r = api.getWeather("beijing", BuildConfig.WEATHER_KEY)
        Log.d("WeatherTest", "城市=${r.name} 温度=${r.main.temp}")
    } catch (e: Exception) {
        Log.e("WeatherTest", "失败了", e)
    }
}
```
:::

跑起来，过滤 Logcat 的 tag 为 WeatherTest，看到"城市=Beijing 温度=26.5"这样的输出，网络层就算验收通过。这一步值得单独做，别跳：界面写了一大半才发现网络不通的人，返工的时候脸上都不太好。地基验完再砌墙，是工程的老规矩。

#### 三、三种界面状态：加载中 / 成功 / 失败

联网 App 的灵魂在于"状态管理"。网络慢、断网、城市名打错……每种情况界面都要给用户交代。用一个 sealed class（密封类）优雅地表示：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 界面状态</span><span class="dots">···</span>
:::

```
sealed class UiState {
    object Loading : UiState()                    // 转圈中
    data class Success(val data: WeatherResponse) : UiState()  // 成功
    data class Error(val message: String) : UiState()          // 失败
}

// ViewModel 里：
fun search(city: String) {
    viewModelScope.launch {
        _state.value = UiState.Loading
        _state.value = try {
            UiState.Success(api.getWeather(city))
        } catch (e: Exception) {
            UiState.Error("查不到这个城市，换个名字试试？")
        }
    }
}

// 界面里：
when (val s = state) {
    is UiState.Loading -&gt; CircularProgressIndicator()   // 转圈
    is UiState.Success -&gt; WeatherContent(s.data)        // 展示
    is UiState.Error -&gt; Text(s.message)                 // 报错
}
```
:::

##### sealed class 到底帮你防了什么

头一回见 sealed class 的人多半觉得多此一举：三个状态，用一个 Int 编号不行吗？行，然后就会烂掉。loading 用 true/false，那"正在加载但已有旧数据"算 true 还是 false？错误种类想细分，errorCode 魔法数字一路膨胀到两位数，半年后自己都不记得 3 是什么意思。

sealed class 的核心好处是"穷举"：它的子类只能写在同一个文件里，编译器知道全部可能性，when 分支少写一个直接编译报错。这意味着新增一个状态（比如以后加"空结果"）时，编译器会揪出所有漏改的地方，你靠的是编译器帮你检查，而不是记忆和自觉。

还有类型层面的保护：数据捆在 Success 里（<code class="inline">data class Success(val data: WeatherResponse)</code>），你想在 Error 分支里访问 data，编译器当场拦住。对比一下"data 可能为 null，你自己判断"的写法，一个是制度防错，一个是靠人品。

##### ViewModel 与状态流：_state 和 state 的分工

上面代码里的 <code class="inline">_state</code> 和 <code class="inline">state</code> 是一对，怎么落地？用 StateFlow：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · ViewModel 完整骨架</span><span class="dots">···</span>
:::

```
class WeatherViewModel : ViewModel() {
    private val _state = MutableStateFlow&lt;UiState&gt;(UiState.Loading)
    val state = _state.asStateFlow()   // 对外只读，改状态只走内部

    fun search(city: String) {
        viewModelScope.launch {
            _state.value = UiState.Loading
            _state.value = try {
                UiState.Success(api.getWeather(city))
            } catch (e: Exception) {
                UiState.Error(toMessage(e))
            }
        }
    }
}
```
:::

下划线开头的 <code class="inline">_state</code> 是可写的内部版本，对外的 <code class="inline">state</code> 用 <code class="inline">asStateFlow()</code> 包成只读：界面只能看，改状态的权力收在 ViewModel 手里。权限收得越死，出 bug 的面越小，这是状态管理的第一课。

界面那边收集只要一行：<code class="inline">val state by viewModel.state.collectAsState()</code>。collectAsState 把 Flow 变成 Compose 能观察的状态：state 一变，用到它的界面自动重绘，你不用写任何"手动刷新"的代码。这行通常写在 Screen 级 Composable 的开头。

转屏也不用怕：ViewModel 活得比界面久，转屏重建界面时状态还在它手里，拿回来接着用就行。这正是上一章说过的"状态放 ViewModel"的完整版本，这次有了真实的联网数据，感受会深得多。

还有 <code class="inline">viewModelScope</code>：它是 ViewModel 自带的协程作用域，界面销毁时里面未完成的协程自动取消。你发起的请求不会在界面死了之后还回来改状态，内存泄漏和"回到已关闭页面崩溃"这两类经典 bug，被这一行作用域声明顺手解决了。

这个 <code class="inline">Loading/Success/Error</code> 三段式是联网界面的"万金油模板"，先背下来，以后所有联网 App 照葫芦画瓢。

不过 Error 里别偷懒只装一句"获取失败"。无网络、超时、被限流（HTTP 429）、服务器出错（5xx）是四回事，用户该看到的提示也不一样：断网就提醒查连接，限流就劝稍后再试。上面 <code class="inline">catch (e: Exception)</code> 一把抓的写法是偷懒版，正式项目里把异常分分类，界面立刻从"能跑"变成"贴心"。

##### 把错误分类做实：从 Exception 到人话

口说无凭，直接上一段能抄的分类函数。Retrofit + 协程请求失败，异常基本就这几类：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 异常翻译成人话</span><span class="dots">···</span>
:::

```
fun toMessage(e: Exception): String = when (e) {
    is IOException -&gt; "网络连不上，检查一下 Wi-Fi 或流量"
    is HttpException -&gt; when (e.code()) {
        401 -&gt; "密钥没配对，去控制台核对一下 Key"
        404 -&gt; "找不到这个城市，换个拼写试试"
        429 -&gt; "请求太频繁啦，休息一会儿再来"
        else -&gt; "服务开小差了，稍后再试"
    }
    else -&gt; "出了点意外：${e.localizedMessage ?: "未知错误"}"
}
```
:::

逐个说。<code class="inline">IOException</code> 是"根本没连上"：断网、超时都归它，提示查网络就对。<code class="inline">HttpException</code> 是"连上了，但服务器不给好脸"：code() 能拿到状态码：401 多半是 Key 问题，404 是城市没查到，429 是免费额度用超了被限流。剩下的解析类异常说明返回内容和你模型对不上，多半是字段拼错，或者拿到的是错误返回却按成功模型去解，这个病根在 bug 门诊一节细说。

两个注意点：子类判断要放在前面，when 从上往下匹配，顺序反了走不到想要的分支；catch 里别把原始异常吞掉，日志里至少打一行堆栈，用户看到的提示是给人看的，日志里的堆栈是给你自己看的，排查问题全靠后者。

想更讲究，可以用 Kotlin 的 Result 或 RunCatching 把"成功/失败"包成一个值往下传，函数签名里就写明可能失败。练手阶段用 when 分类足够，知道有更优雅的路子就行。

##### 三态之外的第四态：空结果与初始状态

三态能扛住大部分场景，但有两种情况它表达不了。一是 App 刚打开、还没搜过任何东西时，界面该显示什么？Loading 的转圈空转毫无意义，Error 又谈不上出错。二是有些查询真的没有结果，"没查到"和"查错了"是两回事，混在 Error 里用户会一头雾水。

常见做法是再添两个状态：Idle（初始态，界面上摆一句引导文案"输入城市名查天气"，或者直接走定位）、Empty（查询成功但确实没数据）。sealed class 里加两个子类，when 的穷举检查会逼着你把所有漏改的分支补齐：前面夸过的编译器红利，加状态时又兑现一次。

天气 App 的空结果其实不多见，城市名不存在走的还是 Error 的 404 分支，但你以后做搜索类、收藏类 App，Empty 是常客。现在知道有这号状态，到时候不慌。

反过来说，状态也不是越多越好：每加一个状态，界面就要多一分对应的交代，when 里多一个分支。三态起步、按需求生长，是稳妥的节奏，一上来就摆七个状态，先吓住的是自己。

#### 四、实战界面代码：把天气画出来

状态有了，界面长这样（关键片段）：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 天气界面（核心片段）</span><span class="dots">···</span>
:::

```
@Composable
fun WeatherContent(data: WeatherResponse) {
    Column(
        Modifier.fillMaxSize().padding(24.dp),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text(data.name, fontSize = 28.sp, fontWeight = FontWeight.Bold)
        Text(
            "${data.main.temp}°C",
            fontSize = 72.sp,
            fontWeight = FontWeight.Light
        )
        Text(
            data.weather.firstOrNull()?.description ?: "未知",
            fontSize = 20.sp,
            color = Color.Gray
        )
        Spacer(Modifier.height(16.dp))
        Row {
            Text("💧 湿度 ${data.main.humidity}%")
            Spacer(Modifier.width(24.dp))
            Text("🌡️ 当前气温 ${data.main.temp}°C")
        }
    }
}
```
:::

几个小细节值得学：<code class="inline">firstOrNull()</code> 安全取第一个元素（列表可能为空），<code class="inline">?: "未知"</code> 给兜底文案，空安全原则在界面里同样适用。温度用 <code class="inline">72.sp</code> 的大字号撑场面，"轻"字重（Light）让数字显得优雅，这是天气类 App 的经典配方。

##### 逐行拆解：这段界面在干什么

代码看着长，其实就五件事，从上往下过一遍。Column 是"从上往下排"的容器，像把一叠卡片竖着摞；fillMaxSize 让它占满整屏；padding(24.dp) 四周留白，文字不顶到屏幕边，呼吸感就有了。

horizontalAlignment = CenterHorizontally 让所有子元素水平居中，天气 App 的主界面居中排布是惯例，视线先落在温度上，再扫到描述和湿度，信息层级自然形成。两个 Text 分别是城市名和温度，第三个 Text 是天气描述，中间那个 Spacer 隔出一段空隙，让下面湿度那行不至于贴得太紧。

注意字号单位是 sp 不是 dp，sp 会跟随用户在系统里设置的字体大小，文字一律用 sp，这是无障碍的底线；间距、尺寸这类"物理量"才用 dp。还有那个小箭头组合 <code class="inline">?.description ?: "未知"</code>：weather 列表可能为空，firstOrNull() 返回 null，此时描述就显示"未知"而不是崩溃，接口偶尔会返回你没料到的结构，界面不能跟着塌。

##### Modifier：每个组件的随身设置面板

Modifier 是 Compose 里每个组件的"设置面板"，大小、边距、背景、点击全靠它一路点出来。链式调用的顺序有讲究：<code class="inline">Modifier.background(...).padding(16.dp)</code> 和 <code class="inline">Modifier.padding(16.dp).background(...)</code> 画出来不一样，背景在前，背景会包住边距；边距在前，边距留在外面、背景只涂内容区。记不住就都写一遍，Preview 里立见分晓。

常用的几个先记熟，够撑起大部分界面：

- <strong>size / width / height</strong>：定尺寸，天气卡片常用 fillMaxWidth 配固定 height。
- <strong>padding</strong>：内边距，界面松紧全靠它调。
- <strong>background</strong>：背景色，配 RoundedCornerShape 就是一个圆角卡片。
- <strong>clickable</strong>：让它可点，天气卡片点开看详情就靠这个。
- <strong>fillMaxWidth / fillMaxSize</strong>：撑满一行或一屏。

##### 用 @Preview 边写边看

每写完一个 Composable，顺手在下面补一个带 @Preview 注解的私有函数，编辑器右侧面板直接出图：改一个字号、换一个颜色，不用每次都跑模拟器，效率差好几倍：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 预览函数</span><span class="dots">···</span>
:::

```
@Preview(showBackground = true)
@Composable
private fun WeatherPreview() {
    WeatherContent(
        WeatherResponse(listOf(Weather("晴")), Main(26.5, 40), "北京")
    )
}
```
:::

Preview 还能同时摆好几个：一个亮色主题、一个深色主题、一个特大字体，改一处，三个预览同时变。深色模式那节的自查工作，靠它省一半时间。

#### 五、界面与交互细节

- <strong>搜索框</strong>：顶部 TextField，输城市名点搜索（键盘上设"搜索"动作，回车即搜）。
- <strong>天气卡片</strong>：大字号温度（26.5°）、天气描述（晴）、湿度、城市名。
- <strong>收藏城市</strong>：把常看的城市存进 DataStore，下次打开自动查，顺手复习本章。
- <strong>缓存上次的成功结果</strong>：请求失败时把上一次的数据摆出来，标注一句"数据来自 X 分钟前"，比一块白屏友好得多，天气这种内容，旧十分钟没什么大不了。
- <strong>下拉刷新</strong>：Compose 里用 <code class="inline">PullToRefreshBox</code>（Material 3 提供），手感立刻"专业"起来。

##### 搜索框：让键盘替你干活

搜索框最容易做成半成品：输完城市名，还得挪手指去点旁边的"搜索"按钮。体验好的做法是把键盘右下角的回车键直接变成"搜索"键：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 搜索框（键盘动作）</span><span class="dots">···</span>
:::

```
TextField(
    value = city,
    onValueChange = { city = it },
    label = { Text("输入城市名") },
    singleLine = true,
    keyboardOptions = KeyboardOptions(imeAction = ImeAction.Search),
    keyboardActions = KeyboardActions(onSearch = {
        viewModel.search(city)
    })
)
```
:::

<code class="inline">ImeAction.Search</code> 让键盘右下角显示放大镜图标，点它就触发 onSearch——用户少点一下是一下，这类细节攒起来就是"顺手"和"别扭"的差距。布局根上再配 <code class="inline">Modifier.imePadding()</code>（或处理好 insets），键盘弹起来不会把输入框顶出屏幕外。

两个小保险：请求进行中把搜索动作暂时禁掉，防连点（重复请求的治法见 bug 门诊）；另外中文输入法的拼音组合阶段，TextField 的 value 也会一路变化，所以别做"每输一个字母就自动搜索"，会被拼音输入坑到怀疑人生。要做联想搜索，得配防抖，那是进阶练习的事。

##### 收藏城市与城市切换：DataStore 存一串名字

只能查一个城市的 App 太浅了。先把"常看的城市"存下来，DataStore 干这个正好，前面存数据的那一章讲过它的用法，忘了就翻回去扫一眼。城市不多的话，存成逗号分隔的字符串最省事：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 收藏城市的存与取</span><span class="dots">···</span>
:::

```
val CITY_KEY = stringPreferencesKey("cities")

// 存：列表拼成一个字符串
suspend fun saveCities(cities: List&lt;String&gt;) {
    context.dataStore.edit { it[CITY_KEY] = cities.joinToString(",") }
}

// 取：拆回列表，没有收藏时给个默认城市
val citiesFlow = context.dataStore.data
    .map { it[CITY_KEY]?.split(",") ?: listOf("beijing") }
```
:::

界面上横着一排 FilterChip（过滤芯片）或者一个下拉菜单，点谁就查谁：所谓"切换城市"，本质就是换 q 参数再 search 一次，架构上什么新东西都不用加。

替用户想想场景再做取舍：出差党早上想知道北京和深圳两边天气；爸妈想知道老家和儿女所在的城市。两三个城市的切换需求，比"完整的多城市管理页面"优先做，成本极低、收益立竿见影。列表管理放到扩展练习里再练。

默认城市也是细节：第一次打开 App，别让用户面对一块白屏。给个默认城市，或者走下一节的定位拿真实城市，有内容才有第一印象，白屏只有卸载。

##### 缓存上次结果：断网也要有内容看

断网时的白屏，是联网 App 最伤体验的瞬间。改法不复杂：ViewModel 把最近一次成功结果记住，请求失败时先摆旧数据。内存里记住就行：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 失败时回落到缓存</span><span class="dots">···</span>
:::

```
private var lastGood: WeatherResponse? = null
private var lastTime: Long = 0L

fun search(city: String) {
    viewModelScope.launch {
        _state.value = UiState.Loading
        try {
            val r = api.getWeather(city)
            lastGood = r
            lastTime = System.currentTimeMillis()
            _state.value = UiState.Success(r)
        } catch (e: Exception) {
            val cached = lastGood
            _state.value = if (cached != null)
                UiState.Success(cached)          // 旧数据顶上
            else
                UiState.Error(toMessage(e))      // 没缓存才报错
        }
    }
}
```
:::

界面上要给旧数据标个出身："数据来自 12 分钟前"。时间差拿 System.currentTimeMillis() 减 lastTime 算出来，换算成分钟显示。天气这种内容，旧十分钟没什么大不了，但标签必须诚实，不标时间就是糊弄用户。

更进一步的做法：把成功返回的 JSON 原文存进 DataStore 或本地文件，冷启动时先显示缓存、再在后台静默刷新。"先摆旧内容、悄悄更新"是新闻、天气、社交类 App 的通用姿势。内存缓存杀掉 App 就没了，落盘的缓存才扛得住重启，练手先做内存版，觉得有意思再补落盘版。

缓存要不要做过期策略？练手阶段不用。记住一条原则就够：给用户看旧数据时永远标时间，诚实比新鲜重要。

##### 下拉刷新：一个组件的事

下拉刷新用一个组件就够，Material 3 的 PullToRefreshBox，把原来的内容整个包进去：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 下拉刷新</span><span class="dots">···</span>
:::

```
var refreshing by remember { mutableStateOf(false) }

PullToRefreshBox(
    isRefreshing = refreshing,
    onRefresh = {
        refreshing = true
        viewModel.search(currentCity)   // 请求完成后把 refreshing 置回 false
    }
) {
    // 原来的天气内容原封不动放这里
}
```
:::

手感立刻"专业"起来。两个提醒：刷新中要有视觉反馈，组件自带的转圈别去掉；刷新结束记得把 refreshing 置回 false，忘置回的后果是转圈永不消失，用户以为 App 卡死，这属于 bug 门诊的常客。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>小贴士：图片让界面活起来

{class="mt-1"}
给每种天气配一个 emoji 或图标（☀️🌧️❄️），用 <code class="inline">when(description)</code> 映射，三行代码，界面温度感翻倍。也可以加载第三方的天气图标库，但练手阶段 emoji 足够。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：天气 App 验收清单

{class="mt-1"}
① 正常搜索出天气；② 断开网络，App 优雅报错不崩溃（开飞行模式测！——网络项目的验收标准得包括"断网时是什么样"，只测成功路径等于没测）；③ 输一个不存在的城市，提示友好；④ 收藏两个城市，重启 App 还在；⑤ 转屏不丢状态。五条全过，这个项目才算毕业。
:::

#### 六、常见 bug 门诊：联网项目的五个翻车现场

下面五个现场，写这本书时替你踩了个遍。每个按"症状—病根—药方"给方子，出了问题对号入座，别一条条盲改。

##### 门诊一：JSON 解析失败，界面永远转圈或闪退

症状千奇百怪：一搜索就闪退、永远 Loading、温度显示一串 null。九成是同一个病根，模型和 JSON 没对上。细分下来三种死法：字段名拼错（JSON 是 description，你写成 descrption）；层级错位（description 藏在 weather 数组里，你跑到最外层找）；还有第三种最冤，请求其实失败了，返回的是错误 JSON，你却还按成功模型去解析。

药方的第一步永远是看原始返回。给 OkHttp 挂一个日志拦截器，请求和响应在 Logcat 里纤毫毕现：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 带日志的 OkHttpClient</span><span class="dots">···</span>
:::

```
val client = OkHttpClient.Builder()
    .addInterceptor(HttpLoggingInterceptor().apply {
        level = HttpLoggingInterceptor.Level.BODY
    })
    .connectTimeout(15, TimeUnit.SECONDS)
    .readTimeout(15, TimeUnit.SECONDS)
    .build()

// 把这个 client 传给 Retrofit.Builder().client(client)
```
:::

日志里能看到完整 URL 和原始 JSON，对照着改模型，字段名逐个核对，几分钟的事。顺手把超时也设上了：门诊二马上要用。注意日志拦截器只在调试时开 BODY 级别，发布版要调低或去掉：响应内容里带着你的请求参数，不该出现在正式包的日志里。

再补一招：故意输错城市名请求一次，看看错误返回长什么样。错误 JSON 和成功 JSON 结构不一样，模型只按成功的建，错误一来解析自动翻车，理解了这一点，第三种死法你就免疫了。

##### 门诊二：超时——要么半天不报错，要么一秒就放弃

症状是两个极端：转圈十几秒才提示失败，用户早走了；或者网络稍微一抖就报错，其实多等一秒就能成。病根都在超时配置上，没配就用默认值（长短未必合你的场景），配激进了（比如一秒）则弱网下寸步难行。

药方：connectTimeout 管"建立连接"要多久，readTimeout 管"读完数据"要多久，两个都设在十到二十秒的量级，再按目标用户的网络环境微调。失败后界面上给"重试"按钮，而不是让用户退出重进，重试的成本越低，App 显得越可靠。

还有一条经验：模拟器走电脑网络，快而稳，什么都测不出来。真机在电梯、地库、高铁上才是真实考验。上架前务必真机过一遍弱网，开发者选项里能限速，或者直接站进电梯里测，别嫌麻烦。

##### 门诊三：主线程联网，当场闪退

症状：一点搜索，Logcat 喷出一整屏 NetworkOnMainThreadException，App 直接崩给你看。病根：在按钮的 onClick 里直接调了同步的网络方法。Android 明令禁止主线程做网络操作，这不是刁难，是保护：主线程卡住，整个界面就冻住，系统宁可让它崩。

药方是从接口定义到调用全链路挂起：接口方法加 suspend，调用包进 viewModelScope.launch。Retrofit 对 suspend 函数会自动切到后台线程，你不需要手写 withContext(Dispatchers.IO)。自查清单三问：接口方法是不是 suspend？launch 其实在协程作用域里。有没有哪个角落藏着同步的调用？三问过完，这个病基本断根。

##### 门诊四：重复请求——一秒点了十下搜索

症状有两层。浅的一层：连点十下搜索，十个请求一起飞，免费额度瞬间扣掉十次。深的一层更阴险，响应乱序：先查"北京"再查"上海"，北京的网络慢、响应后到，把上海的结果覆盖了，界面上城市名写着北京、温度却是上海的。用户看到的就是"数据错了"。

病根：每次点击都新开一个协程，彼此不知道对方的存在。药方：发起新请求前，把旧的作废：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 用 Job 取消旧请求</span><span class="dots">···</span>
:::

```
private var job: Job? = null

fun search(city: String) {
    job?.cancel()          // 上一发还没落地，直接作废
    job = viewModelScope.launch {
        _state.value = UiState.Loading
        _state.value = try {
            UiState.Success(api.getWeather(city))
        } catch (e: Exception) {
            UiState.Error(toMessage(e))
        }
    }
}
```
:::

cancel 掉旧的再 launch 新的，乱序覆盖自动消失：被取消的协程不会再回来改状态。搜索框联想那种"边输边搜"的场景，再配一层防抖：输入停顿几百毫秒才真正发请求，Compose 里用 snapshotFlow 配 debounce 能做到，视你的架构而定。UI 层再加一道保险：Loading 期间把按钮置灰。三层防护，费用为零。

##### 门诊五：没日志，黑盒里抓瞎

症状：出了问题只知道"不行"，不知道请求发没发出去、发出去什么样、回来的是什么。病根：没有任何网络日志，全靠猜，猜是调试里最贵的动作。

药方：门诊一那个日志拦截器在调试版常驻；学会用 Logcat 的过滤，把搜索条件设成 OkHttp，每个请求的 URL、状态码、耗时、响应体一目了然。学会这一招，大多数网络问题你都能自己定位：剩下那些，多半真是服务端的问题，这时候你才有底气说"不是我这边的事"。

#### 七、深色模式与界面打磨

功能跑通了，离"像个正经 App"还差一层皮。这层皮不费多少代码，费的是耐心，但它决定第一印象。

##### 深色模式：别在夜里晃瞎用户

天气 App 是睡前和起床都会打开的 App，深色模式几乎是刚需。好消息：只要你的颜色都从 MaterialTheme 的 colorScheme 里取，跟随系统深色模式基本自动。坏消息：只要有一处写死了 Color.White。深色模式下它就是一坨刺眼的白。

自查方法朴素但有效：系统设置切到深色，逐屏过一遍，重点盯三类写死的颜色，背景、文字、卡片。想省事就用语义色：surface 当背景、onSurface 当文字、surfaceVariant 当卡片底，深浅主题自动换装，一处都不用 if。那段代码里的 <code class="inline">Color.Gray</code> 就是个写死的反面教材，换成 <code class="inline">MaterialTheme.colorScheme.onSurfaceVariant</code> 才是正路。

Android 12 及以上的设备还能试试动态取色（Material You）：壁纸什么色，App 主题跟着变，一行配置的事，旧系统自动回退到默认配色。夜里有心的话，深夜十一点切深色从头用一遍，很多白天看不见的颜色问题，那个时间点全现形。

##### 打磨清单：五件小事，拉开档次

- <strong>占位与骨架</strong>：Loading 时别只给一个孤零零的转圈，卡片位置先摆灰底占位，内容落进去跳动小，观感稳得多。
- <strong>无障碍</strong>：图标配 contentDescription，纯装饰的明确传 null：读屏用户靠它理解界面。
- <strong>字体缩放</strong>：把系统字体调到最大档再打开 App，看看 72.sp 的大温度会不会把布局挤爆，sp 跟随系统设置，特大字体下你的界面可能是灾难现场。
- <strong>小屏适配</strong>：找个小尺寸模拟器或用 Preview 的窄屏预设跑一遍，别让关键信息被键盘挡住。
- <strong>按压反馈</strong>：可点的东西要有涟漪或状态变化，用户需要"我点到了"的确认。

这五条都不费代码，费的是"过一遍"的耐心。上架品质和练手作品的差距，基本都堆在这一层，练手作品的功能和它一样，就是看着糙。

#### 八、定位与自动天气：让 App 自己知道你在哪

每次都手动输城市，用两天就烦了。自动天气的完整链路是四步：申请定位权限 → 拿到坐标 → 反查出城市名 → 用城市名走原有的搜索流程。四步里每一步都可能被用户拒绝、被系统限制，所以设计上永远留一个手动入口。

##### 第一步：声明并申请权限

Manifest 里加定位权限：

::: div .code-block
:::inline div .code-head
<span>XML · AndroidManifest.xml（节选）</span><span class="dots">···</span>
:::

```
&lt;uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" /&gt;
&lt;uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" /&gt;
```
:::

COARSE 是大致位置，FINE 是精确定位。天气 App 申请 COARSE 就够，查天气只需要知道你在哪个城市，精度要求越低，用户越愿意给。定位权限属于危险权限，光声明不够，还得运行时问一句：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 运行时申请定位权限</span><span class="dots">···</span>
:::

```
val permissionLauncher = rememberLauncherForActivityResult(
    ActivityResultContracts.RequestPermission()
) { granted -&gt;
    if (granted) viewModel.locate() else viewModel.useManualCity()
}

Button(onClick = {
    permissionLauncher.launch(Manifest.permission.ACCESS_COARSE_LOCATION)
}) { Text("自动定位") }
```
:::

注意 granted 为 false 的分支也要有内容：退回手动搜索，顺便解释一句为什么需要定位，"想自动显示你所在城市的天气"比干巴巴的"需要定位权限"容易让人点头。别把拒绝权限的用户堵在门外：大多数人第一次都会谨慎，给了退路，下次打开再请求时通过率会高不少。

##### 第二步：坐标反查城市名

拿到坐标后要"翻译"成城市名才能查天气。系统自带的 Geocoder 就能干，不用加任何依赖：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 坐标反查城市（示意）</span><span class="dots">···</span>
:::

```
suspend fun reverseGeocode(lat: Double, lon: Double): String? =
    withContext(Dispatchers.IO) {
        val geocoder = Geocoder(context, Locale.getDefault())
        // 反查可能查不到，返回空列表要兜底；不同系统版本有同步/异步两种写法
        geocoder.getFromLocation(lat, lon, 1)
            ?.firstOrNull()?.locality
    }
```
:::

三个现实问题提前交代：Geocoder 反查本身要联网，断网时它也歇菜，错误要兜住；反查出来的名字可能和天气服务商认的城市名对不上（比如返回的是区名），必要时让用户确认一下；部分设备上反查能力不可用，务必留手动入口。定位本身的获取，用系统 LocationManager 或 Google Play services 的 FusedLocationProviderClient 都行，后者封装更好，依赖怎么加以官方文档为准。拿到一次位置就够，别持续监听，省电，也省麻烦。

##### 模拟器上的定位测试

模拟器测定位要手动喂坐标：模拟器侧边的三个点菜单（Extended Controls）→ Location，填一组经纬度，点 Send：App 立刻以为你在那儿。把坐标先设到北方城市再设到南方城市，两分钟体验一次"南北穿越"，比真机测试还高效。权限弹窗在模拟器上同样会出现。允许和拒绝两条路径都要走一遍，尤其拒绝之后，手动搜索还能不能用。

#### 九、扩展练习：三个方向，把它变成"自己的"App

到这里你已经有能看、能查、能扛断网的天气 App 了。三个由浅入深的练习，每个都附验收标准，做完才叫你的，半途而废的练习不算数。

##### 练习一：多城市管理页

新建一个城市列表界面：LazyColumn 每行一个城市，行里显示当前温度，支持添加和长按删除。数据存 DataStore（城市少时够用）或 Room（想顺便练数据库就用它）。列表页和详情页之间用导航组件串起来。

验收：添加、删除、切换三个动作都好用；杀掉 App 重开，列表还在；删除当前正在展示的城市时有合理兜底，不会白屏。

##### 练习二：天气图标系统

把 when(description) 的映射做全：晴、雨、雪、多云、雾至少五类各有图标，emoji 起步，觉得糙就换图标库，或按接口返回的 icon 字段取服务商的官方图标（字段用法以服务商文档为准）。进阶版：区分白天和夜晚，夜里给月亮图标。

验收：五类常见天气图标齐全；遇到没见过的描述显示默认图标，永远不空白：图标系统崩不起，兜底必须有。

##### 练习三：每日天气通知

用 WorkManager 设一个每天早上的一次性任务，把当天天气发成通知。三个注意点：Android 13 及以上通知权限要运行时申请。拒绝就安静放弃，别烦人；通知内容从缓存取，别为了发通知专门请求一遍接口；测试时把时间先设成两分钟后，验证通过再改回早上。

验收：通知按时到达；没给通知权限时安静失败不崩溃；设备重启后任务还在，这本来就是 WorkManager 的本职，正好顺便验证。

三个练习不必都做，挑一个做完做透，比三个都烂尾强得多。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-quote-left mr-2"></i>一句话记牢

{class="mt-1"}
联网 App 四件套：接口 + 数据模型 + 三态界面 + 缓存兜底：别的都是修饰。
:::

#### 十、和 iOS 篇第 66 章对个账

这本书在 iOS 篇第 66 章也带你做了一个天气 App。同一个项目、两种生态，做完 Android 版再去读它，你对"联网 App"这件事的理解会翻倍：套路是相通的，工具各有名字。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
  <thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">概念</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Android 侧（本章）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">iOS 侧常见做法</th></tr></thead>
  <tbody>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">网络请求</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit 声明接口</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession（系统自带）</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">JSON 解析</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gson 反射映射</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Codable 协议自动编解码</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">界面状态</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">sealed class 三态</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">enum 带关联值</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">声明式界面</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jetpack Compose</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">轻量存储</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DataStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">权限声明</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Manifest</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Info.plist</td></tr>
  </tbody>
</table>
```
:::

具体写法以 iOS 篇第 66 章为准，上表只是概念对照，帮你把两套词汇表连起来。对照完你会发现三件事完全一样：一是"先在浏览器里预习 JSON 再写代码"的流程；二是 Key 必须藏好、绝不进仓库的铁律；三是 Loading/Success/Error 三态模板。差异只在名字：这边叫 suspend，那边叫 async/await；这边叫 StateFlow，那边是另一套响应式写法。

把两章都做完的人，说"独立完成过 Android 与 iOS 双端的联网应用"是有底气的：因为你真的理解了每一层在干什么，而不是背会了两套咒语。这种理解迁移到新闻、汇率、翻译类 App，就是换几个 URL 的事。

#### 十一、这一章的常见问题

收尾前集中回答几个高频问题。问法都带着真实的体温，你迟早也会这么问。

<strong>问：我一个字母一个字母照着敲的，怎么还是解析失败？</strong>

照抄也会抄错：全角引号、多余空格、括号不配对，都是常客。先加日志拦截器看原始返回，对照浏览器里那份 JSON 逐个字段核对：九成是字段名或层级没对上。剩下的一成，是你的请求其实失败了，拿到的错误 JSON 和成功 JSON 结构不同，模型按成功的建，自然解不开。

<strong>问：免费的 Key 会不会哪天突然就不能用了？</strong>

额度内一般稳定，超了会返回 429 限流，不是失效。服务商也可能调整政策，商用前务必读条款。个人项目要做好"哪天要换服务商"的准备：把 URL、Key、数据模型都圈在一处，换起来才不伤筋动骨，这也顺便回答了"为什么接口要单独放一个文件"。

<strong>问：要不要先把 OkHttp 学透了再学 Retrofit？</strong>

不用。Retrofit 底层确实是 OkHttp，但先学底层再学框架，就像先学发动机构造再学开车，不是不行，是没必要。先用 Retrofit 把项目跑通，等遇到要改超时、加拦截器的真实需求，再回头补 OkHttp，带着问题学得最快。

<strong>问：模拟器能联网吗？连不上怪谁？</strong>

能，模拟器直接走电脑的网络。连不上先确认电脑本身能上网、没开着奇怪的代理，再重启模拟器，多数情况这两步就解决。模拟器也能开飞行模式，验收断网表现全靠它，别忘了这条验收项。

<strong>问：Key 真被盗刷了怎么办？</strong>

先去服务商控制台重置 Key，旧的立即作废；然后检查仓库历史，只要提交过就视同泄露，改本地文件没用，必须换 Key。查一下用量账单，心里有数。以后新项目一开始就走 local.properties 的路子，从源头杜绝。

<strong>问：转个屏数据就没了，是不是手机坏了？</strong>

不是。转屏默认会重建界面，只写在界面层 remember 里的状态随之清空。把状态放 ViewModel（本章一直在这么做）就不会丢；轻量的输入框内容可以用 rememberSaveable 救回来。这是 Compose 新手最经典的困惑之一，遇到一次就长记性了。

<strong>问：JSON 里几十个字段，数据模型必须全建吗？</strong>

不用。只声明你界面真正要用的字段，其余的 Gson 自动忽略：模型跟着需求长，用到了再补。全建一遍除了费手指，还会在服务商改版时多出一堆没人用的坏字段。

<strong>问：这个练手 App 直接打包上架应用商店行吗？</strong>

别急。Key 藏好只是第一关，上架还要隐私政策、权限说明、服务商条款里对分发的限制，一关都不能少。练手项目先发给朋友装着玩，收集几条真实反馈，上架的事等练完后面几章再回头考虑，那时候你的 App 会不一样。

#### 十二、误区清单：联网项目里"很多人以为"的五件事

联网项目的坑，一半在代码里，一半在观念里。下面五句话听着耳熟吧？每句背后都站着一个翻过车的人。

<strong>误区一："断网是边缘情况，最后再说。"</strong>

其实手机大部分时间都在网络边缘徘徊：电梯、地库、高铁隧道、人流密集的会场。断网体验决定一个 App 的下限，成功路径只决定上限，验收清单里飞行模式那一项，就是冲它来的。把断网当边缘情况的项目，上线后都会被用户替它补上这一课。

<strong>误区二："接口永远会像文档写的那样返回。"</strong>

服务商改版、字段调整、错误返回换结构，都是常态而非意外。应对之道不是预测变化。应对之道是隔离变化：网络层收拢在一处、数据模型集中管理、界面不直接接触 JSON，变了就只改一处，这是本章反复念叨的分层。

<strong>误区三："免费的嘛，怎么用都行。"</strong>

免费额度有次数限制，服务条款里对商用往往另有约定。拿练手 Key 去跑一个对外收费的服务，限流和违约都可能找上门。个人学习尽管用，商业化之前读一遍条款、按需升级套餐，这是基本礼貌，也是自我保护。

<strong>误区四："模拟器上跑通了，稳了。"</strong>

模拟器走电脑网络，快、稳、从来不掉线，真实世界的弱网、权限拒绝、恶意输入它一样都体验不到。模拟器和真机得两条腿走路，弱网测试更是只能真机来。这条和误区一是连体的：因为信了模拟器，才会觉得断网不用测。

<strong>误区五："缓存是锦上添花，以后再加。"</strong>

对天气、新闻这类内容，缓存不是优化项，是体验主干——断网瞬间有内容可看，全靠它撑着。等线上用户开始抱怨"打开就是白屏"再补，人已经走了一波。好消息是本章的缓存方案半小时就能落地，成本远低于想象。

#### 十三、缓存方案对照：内存、落盘、数据库怎么选

前面用的内存缓存是最简单的一档。往下还有两档，三档放在一起看，选型思路就清楚了：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
  <thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">方案</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">怎么做</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">能活多久</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">适合谁</th></tr></thead>
  <tbody>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">内存缓存</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ViewModel 里一个变量记住最近结果</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">App 进程活着就有效，杀掉即失</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">练手起步，会话内断网兜底</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">落盘缓存</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把返回的 JSON 原文存进 DataStore 或文件</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">重启也在，卸载才没</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">单城市天气，要求冷启动就有内容</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">数据库（Room）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">建表存数据，一个城市一行或多行</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">长期</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">多城市管理、历史趋势这类结构化需求</td></tr>
  </tbody>
</table>
```
:::

选型口诀一句话：进程内兜底用内存变量，单块内容落盘用 DataStore，结构化多条目上 Room。三档成本递增，别跳级，为三座城市的天气建数据库，像给自行车装行车记录仪，装备没错，就是用不上。

无论哪一档，"数据来自 X 分钟前"的标签都得有；更讲究一点，加一条过期线：超过一定时长的缓存（多久视内容性质定，天气可以放宽到半天级别），展示前先静默刷新一轮，刷新完悄悄换新，用户全程无感。

还有一招常被忽略的顺序问题：请求失败的当下，先判断"有没有缓存可回落"，再决定显示 Error 还是旧数据。顺序反了，用户手里明明有数据却看到报错，等于自己拆自己的台。

#### 十四、从零到跑通：五个晚上的推进计划

这个项目信息量不小，一口气写完容易翻车。给你排一个"五个晚上"的节奏，每晚一小时上下，按部就班反而快：

1. <strong>第一晚：只做 API</strong>。注册、拿 Key、浏览器预习 JSON、把 URL 各参数挨个试一遍。今晚的产出是一支能用的 Key 和一份存在桌面的 JSON 文件，一行 App 代码都没有，完全正常。
2. <strong>第二晚：网络层</strong>。加依赖、建数据模型、写接口、搭 Retrofit 实例，用日志验证"能拿到温度"。今晚忍住不写任何界面，地基没验完不砌墙。
3. <strong>第三晚：三态骨架</strong>。sealed class、ViewModel、一个最朴素的界面：Loading 转圈、成功显示温度、失败显示文案。丑没关系，先通再说。
4. <strong>第四晚：界面打磨</strong>。大字号温度、图标映射、深色模式过一遍、键盘搜索动作配好。今晚结束时它开始"像个正经 App"。
5. <strong>第五晚：折腾它</strong>。断网测试、错误分类、缓存回落、下拉刷新，把验收清单五条挨个过。哪条不过补哪条。

中途卡住怎么办：先按 bug 门诊那节对号入座；门诊治不了，就把问题拆小，网络层单独跑一次、界面单独摆一次假数据，哪层断了查哪层。凌晨两点还在调的时候，多半是小问题外加疲劳滤镜，去睡觉，第二天往往十分钟解决，这不是玄学，是普遍规律。

五晚之后，你手里会有一个能写进个人介绍的小项目。但更值钱的是那套手感：预习、隔离、三态、缓存、兜底，下一章再做别的联网项目，你会发现自己不自觉地在画同一张图纸。

#### 十五、天气数据从哪来：一点背景

你调的那个接口背后，是一条比想象中长的链。最上游是各国的气象机构和观测网络：地面观测站、探空气球、卫星、雷达，昼夜不停地收集原始数据；国家之间还有气象数据交换机制，让数据跨边境流动。原始数据经过预报模式的运算，才变成"明天降水概率多少"这种给人看的结论。

商业服务商做的是中间层：把多个数据源聚合、加工、按城市打包，再包装成你调用的 API：顺带把缓存、限流、计费这些工程配套也做了。你写的 App 站在链路的最下游，负责把数字变成人愿意看的界面。三层各赚各的钱，各干各的活。

一点历史底子：天气应用在智能手机上出现得很早，初代 iPhone 发布时，天气就是出厂自带的应用之一；Android 阵营早年则是各家厂商和第三方 App 各显神通。开放 API 兴起之后，个人开发者才第一次能用几十行代码，接到和专业天气 App 同源的数据。你今晚做到的事，放在二十多年前是气象台内部的特权。

知道这条链有什么用？一是排查问题时的方位感：数据不对，先分清是上游数据源的问题、服务商加工的问题，还是你自己解析的问题：凭经验，大部分时候是最后一种。二是心态：免费额度背后是真实的采集和运算成本，省着用、别滥用，这行才能一直"免费"下去。

#### 十六、文件地图：这个项目都长在哪里

项目写下来，文件散在各个目录，难免心里没数。画一张地图，写完对照一遍，哪块缺了、哪块塞错了东西，一眼就能看出来：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
  <thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">文件</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">职责</th></tr></thead>
  <tbody>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AndroidManifest.xml</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">权限声明：INTERNET 一行，做定位再加定位权限——别多也别少</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">build.gradle.kts（模块级）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit、Gson、协程三件套依赖，加 buildConfigField 注入 Key</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">local.properties</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Key 的家，被 gitignore 挡在仓库外面</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">WeatherApi.kt</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">接口定义 + 数据模型，练手阶段合一个文件足够</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UiState.kt</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">sealed class 三态（或四态、五态），全 App 状态的"户口本"</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">WeatherViewModel.kt</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">search、缓存回落、异常翻译，业务逻辑全在这</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MainActivity / 界面文件</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Composable 只负责"画"和收集状态，不碰网络</td></tr>
  </tbody>
</table>
```
:::

职责就一条线：界面只画，ViewModel 只管状态和调度，Api 只管网络。文件名不必照抄这份表，职责划分别乱就行，以后加了 Repository、加了 Room，地图上再添几站而已，主干永远是这三层。

下次接手任何联网项目的教程，先用这张地图对照一下：它把网络层放哪、把状态放哪、把界面放哪，结构清楚了，剩下的就是填空。

找文件的小技巧：Android Studio 左侧 Project 面板切到 Android 视图，目录瞬间清爽；按两下 Shift（默认键位方案下）能全局搜文件名，忘放哪儿了也不怕。

#### 十七、验证习惯：每次改完代码，先跑这五步

网络相关的代码有个特点：一处改动可能牵动好几个角落。与其"重新打包挨个功能点一遍"，不如背下这五步的快速回归清单，每次改动后跑一遍：

1. 正常查询一次，看日志里拼出来的 URL 对不对，参数、Key、单位，一眼扫完。
2. 开飞行模式再查一次，确认走的是友好报错或缓存回落，而不是闪退或白屏。
3. 输一个乱码城市名，确认 404 分支给出的是人话提示。
4. 连点几下搜索，确认没有乱序覆盖，城市名和温度是对得上的。
5. 转一次屏，确认状态还在，界面不回到初始态。

五步跑完不到半分钟。每次改动都跑，问题永远落在"刚改完"的那一小圈里，好定位；攒到三天后一起查，就是大海捞针，debug 最贵的成本从来不是修复，是找到。

再往前一步是写单元测试：<code class="inline">toMessage</code> 这种纯函数最适合，喂一个 IOException，断言返回的是那句"网络连不上"，几行代码搞定。ViewModel 的测试要配协程测试工具，等进阶了再说。先把手动回归跑成肌肉记忆，你已经领先绝大多数练手项目了。

#### 十八、术语速查：本章的名词一张表

这一章的名词密度不小，收在一张表里，写到哪儿查哪儿，不要求背，两三个项目下来它们自然长在手上：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
  <thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">术语</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">一句话解释</th></tr></thead>
  <tbody>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">服务商开的"窗口"，你的程序按规定格式问它要数据</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">端点（Endpoint）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一个具体的接口地址，比如"当前天气"那条 URL</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">JSON</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">服务器返回的文本格式，大括号套中括号，全是键值对</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">序列化 / 反序列化</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">对象变 JSON、JSON 变对象的两道工序，Gson 干的就是这个</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">状态码</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">服务器用三位数字表态：404 没找到、429 太频繁、5xx 它的错</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把"接口定义"翻译成真实 HTTP 请求的框架</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OkHttp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit 底下真正干网络活的库</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">协程 / suspend</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin 的"可暂停函数"，联网等待时界面照常活着</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">StateFlow</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">能被界面观察的数据流，值一变界面自动刷新</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">sealed class</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">子类穷举的类，配 when 让编译器替你查漏</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DataStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">轻量键值存储，收藏城市和设置放这里</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">拦截器</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">请求出去、响应回来的路上的"检查站"，加日志、加公共参数都用它</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">免费额度</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">服务商给的免费调用次数，按天或按月计，数字以官方为准</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">限流</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">超了额度被服务器暂时拒绝，通常返回 429</td></tr>
  </tbody>
</table>
```
:::

表里的词以后会跟着你走遍每一个联网项目，它们不是本章的方言，是这个行当的普通话。哪天你看别人代码里出现这些词不再停顿，这一章就算真正长在你身上了。

#### 十九、从"能跑"到"能分享"：装到别的手机上

练手项目的高光时刻，是朋友用你写的 App 查到了明天要不要带伞，比任何教程里写的成就感都实在。从"自己手机能跑"到"装进别人的手机"，中间隔着两步，都不难。

##### 第一步：上真机——USB 调试五步

模拟器验证逻辑，真机验证体验，定位弹窗、弱网断网、真实字体缩放，全都要真机才演得出来。上真机的流程五步：

1. 打开手机的设置 → 关于手机，连点"版本号"七下，系统提示"已进入开发者模式"。各机型这个入口藏的位置略有差异，找不到就搜"你的机型 + 开发者选项"。
2. 回设置找到新出现的开发者选项，打开 USB 调试。
3. 数据线连电脑，手机上弹出"允许 USB 调试吗"的授权框，勾上"一律允许"再确定。
4. Android Studio 顶部的设备列表里出现你的手机型号。
5. 点运行，App 在真机上启动：定位权限这才会真的弹窗，拔了网线断的才是真断网。

卡住了先换数据线。市面上不少线只能充电、不能传数据，占掉这类问题的大半，很多人在这步耗掉半小时，最后发现凶器是一根九块九的线。

##### 第二步：打个 APK 发出去

菜单栏 Build → Build Bundle(s) / APK(s) → Build APK(s)，进度条走完后，点右下角弹出的通知里的 locate，就能找到生成的 APK 文件：它就是可以安装的完整包。

发送环节有个现实问题：不少聊天工具会拦 APK 文件，试试网盘、文件传输工具，或者两台手机当面互传。朋友收到后点安装，系统会要求允许"安装未知来源应用"，允许一次即可，这是安卓对非商店安装的正常流程，不是病毒警告，但你可以顺便给朋友解释一句这是什么。

关于 Key 的一句实话：Key 被编译进了安装包，懂行的人理论上能从包里把它翻出来。发给朋友玩无所谓，真要公开发布时，就得考虑服务商侧的限制措施和包加固了，视你的发布规模和正式程度而定。

##### 分发前的小体检

- <strong>名字和图标</strong>：应用列表里还叫 app 吗？换一个像样的名字和图标，颜值即第一印象。
- <strong>干净启动</strong>：找一台没装过开发环境的手机装一遍，开发者手机上"能跑"和干净是两回事。
- <strong>写死的东西</strong>：把调试用的写死城市、临时代码检查一遍，该走配置的走配置。
- <strong>日志级别</strong>：出包前把日志拦截器调低或去掉，别把请求细节带出门。

四条过完，你手里就有一个可以大方发出去的东西了。至于上架应用商店，那是另一门课，先把练手包发顺，再考虑那一步。

朋友用完给的反馈记得收好，尤其那些"我点了没反应"之类的模糊描述，追问两句拿到复现步骤，就又多了一条门诊记录。你的 bug 门诊，就是这么一例一例攒厚的。

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小结

- 先浏览器试 API、看懂 JSON，再写代码，"预习"永远不亏
- API Key 藏进 local.properties，绝不进代码库
- Retrofit 接口 + data class：字段对上，JSON 自动解析
- Loading/Success/Error 三段式状态是联网界面万金油
- 断网、空输入、城市不存在：错误处理是联网 App 的及格线
:::
