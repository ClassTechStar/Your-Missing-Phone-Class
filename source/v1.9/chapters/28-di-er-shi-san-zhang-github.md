---
id: di-er-shi-san-zhang-github
part: chao-yue-pian
nav: 附：GitHub入门指南
toc: sub
kind: chapter
---

### 第二十三章附：GitHub入门指南——从代码托管到协作平台

{class="chapter-intro mb-4"}
上一章我们讲了"编程思维"，而真正要把编程思维落地、和他人一起做项目，就绕不开一个名字——GitHub。无论你是计算机系学生要参加比赛、想保存自己的代码作品，还是单纯想看看全球开发者在折腾什么，GitHub都是你必须认识的平台。这一节我们从最基础的概念讲起，帮你建立一个清晰的认知。

::: div .quick-read
##### 本章速读（5 分钟版）
这一章认识GitHub。你多半被"论文final_真的final"这种文件名折磨过——两周前删掉的一段话想找回来，只能一个个文件碰运气。版本控制就是给文件夹装一台行车记录仪：谁改的、什么时候改的、改了哪几行，全部可查，随时能回到任何一个历史时刻。Git是装在你电脑上的版本控制工具，GitHub是把仓库放上云端的网站——如今全球最大的开源代码托管平台。别以为它只属于程序员：存笔记、管稿子、给开源软件报bug、搭免费个人网站，普通人都用得上。

最关键的有三件事。第一，<strong>八个词就够入门</strong>：仓库像相册、提交像带备注的游戏存档、分支像平行存档、合并像把草稿誊回正本；再加Fork（把别人家的项目复印一份）、Push/Pull（上传/下载）、Issue（议事厅）、Pull Request（"我改好了请过目"的验收单）。第二，<strong>协作的铁规矩是"开分支、发PR"</strong>：哪怕个人项目，也别直接在主分支上改——改完发PR请人审查再合并，"多人、长期、要发布"的项目，这条规矩能救你。第三，<strong>安全红线刻死</strong>：密码、Token、.env这类敏感信息绝不提交进仓库，公开仓库会被爬虫秒抓；真提交上去了，第一件事是去平台撤销并轮换那把密钥，删文件不算补救。注册完顺手把两步验证打开。

今天就能做的最小动作：不注册也能先逛——搜一个你在用的开源软件名字，点开提交数看它的"编年史"，随便点一条看红红绿绿的改动对比。想动手就注册个免费账号建第一个仓库，勾上README，然后在网页上点铅笔图标改一行字、填一句提交说明，你的第一次"提交"就完成了，全程不装任何软件。

最大的坑提前打预防针。<strong>GitHub不是网盘</strong>——网盘只留最新一版，它的核心资产是全部历史与协作记录，用"只传文件不写说明"的思路用它，等于把跑车当买菜车开；提交说明别写"update"，不然半年后你面对的是一片没有碑文的坟地；push被拒别用--force硬来，在公共分支上强推等于把同事的提交扔进碎纸机，正确姿势是先pull再push；个人主页那片绿格子是结果不是目标，别为它硬刷提交。
##### 速查表
- Git和GitHub别混：Git是本地的版本控制工具，GitHub是放仓库的云端网站
- 四个核心词：仓库像相册、提交像游戏存档、分支像平行存档、合并像誊回正本
- 第一次动手：网页上用铅笔图标改一行README，填一句提交说明，就是一次commit
- 团队协作：开分支写自己的，发PR请人审；push被拒先git pull再push，别硬推
- 提交说明：一句话说清"为什么改"，勤提交小步快跑，一次提交只做一件事
- 密钥红线：密码、Token、.env绝不进仓库；泄露了先撤销轮换，再清历史
- 账号安全：注册完就开两步验证；Token设有效期和最小权限，别留全权钥匙
- 挑项目看五个信号：Star数、README、最近提交时间、Issue区、许可证
:::

#### 一、GitHub到底是什么？

简单来说，GitHub是一个基于Git的<strong>代码托管与协作平台</strong>。它于2008年上线，2018年被微软收购，至今仍是全球最大的开源代码托管平台，托管着数亿个仓库，覆盖几乎所有主流编程语言。

如果用一个类比来理解：<strong>Git是你电脑上的日记本，GitHub就是一个公开的博客平台</strong>——你可以发布自己的作品，关注别人的项目，参与讨论和协作。它不仅是"程序员的后台仓库"，更像是全球开发者共建的一座"技术城市"——项目在这里诞生、迭代、被讨论、被复用。

对普通人来说，GitHub也并非遥不可及。很多非程序员会用它来托管笔记、电子书、个人博客，甚至用来备份配置文件。只要你有一点点"想把自己的东西整理好并分享出去"的需求，GitHub都值得你了解。

##### 先逛再注册：不登录也能看的东西

你可以先把 GitHub 当成一个"逛"的网站，注册的事不急。首页顶部的搜索框是最实用的入口：输入任何关键词——你手机品牌的名字、你在用的某个开源软件的名字、甚至你家乡城市的名字——回车就能看到一堆仓库。搜索结果可以按 Star 数排序（页面上的排序入口，以界面为准），Star 大致相当于"收藏数"，通常能反映一个项目的受欢迎程度。

另一个值得记住的入口是 Trending（趋势）页：按天、按周、按语言展示当下最受关注的项目。哪怕一行代码都看不懂，去逛一圈也能摸到这个平台的脉搏——不少项目的 README 做得像杂志封面一样讲究，光看排版就是享受。

##### 上面不只有代码

点开几个高星仓库你会发现，GitHub 上"文件"的含义远比想象中宽泛：有人把整套考研笔记做成一个仓库，有人托管开源电子书和词典数据，有人放设计素材与图标集，还有机构把公开数据集放在上面供人下载。再举个例子，你手机里某个开源 App 的"反馈问题"入口，点进去往往直接跳到一个 GitHub 的 Issue 页面——某种意义上，你可能早就"用过"GitHub，只是没人告诉你它的名字。

##### 三个真实的人，三种用法

小林，计算机系大三。课程设计是四人小组，过去用压缩包传作业，改到第几版谁也说不清，合并代码靠"你把你那份发我一下"。这学期老师要求提交仓库链接：每人开一条分支写自己的模块，谁改了什么、什么时候改的，页面上清清楚楚；交作业时把仓库地址往简历里一放，比空口说"参与过团队开发"有说服力得多。

阿May，自媒体作者，不懂代码。她用私有仓库存选题库和文案草稿：每改一版提交一次，三个月前被自己毙掉的选题，随时能翻出来复活。后来她照着教程把个人网站搭在了 GitHub Pages 上，连服务器钱都省了。

老周，产品经理。每周一早上抽十分钟看一遍 Trending 和几个竞品项目的 Issue 区：用户骂得最凶的功能、呼声最高的需求，都白纸黑字写在里面，比很多付费的行业速递还直接。

#### 从"论文最终版"说起：为什么你需要版本控制

##### 一个你多半经历过的场景

打开你的毕业论文文件夹看看——是不是整整齐齐躺着一排：论文v1、论文v2导师意见版、论文final、论文final_真的final、论文final_死也不改版？两周前被你删掉的一段论述，现在想找回来，只能一个文件一个文件点开碰运气；导师问"上周三那版里第三段是怎么写的"，你答不上来。

这不是你不会整理，是"复制粘贴出无数个文件"这套土办法天生有缺陷：文件名承载不了完整历史，复制会丢掉来龙去脉，两个人同时改，必然有一份被悄悄覆盖。

##### 版本控制：给文件夹装一台行车记录仪

版本控制（Version Control）干的事，一句话能说清：<strong>把文件夹里的每一次改动都记录下来</strong>——谁改的、什么时候改的、改了哪几行、为什么改，全部可查，随时可以回到任何一个历史时刻。它像一台自带时间轴的行车记录仪：你随时"存档"，随时"读档"，两份存档之间还能逐行对比差异。

有了它，前面那些痛点逐一化解：旧版本不用另存文件，历史里全有；想查某段话是谁什么时候写的，一条记录就够；多人同时改同一个文件，Git 不会悄悄覆盖，而是明确告诉你"这里你们俩都动了，商量一下留哪版"。

##### 四个核心词，每个都配一个比喻

学 Git 之前，先弄懂四个词就够了：仓库、提交、分支、合并。别背定义，看比喻：

- <strong>仓库（Repository）像一本相册</strong>：装的不是某一张照片，而是"全部照片加每张的拍摄记录"。当你把一个文件夹交给 Git 管理，它就成了仓库——从此里面的风吹草动都会被记录在案。
- <strong>提交（Commit）像游戏里的存档点</strong>：打完一段剧情存一下，附一句备注"打 Boss 前存个档"。哪步打崩了，读档回去就是，之前的心血一点不丢。Git 的 commit 同理，配一句说明——说明写得越清楚，未来的你"读档"越快。
- <strong>分支（Branch）像平行存档</strong>：主线存档不动，复制一份出来随便折腾，走另一条剧情线试试水。试成了，把这条线的成果并回主线；试砸了，扔掉这条线，主线毫发无伤。
- <strong>合并（Merge）像把草稿誊回正本</strong>：平行线上验证过的内容，整理回主文档。如果两个人恰好改了同一段，Git 不会替你做主，而是把冲突标出来让你们自己拍板——这比"悄悄覆盖"友好得多。

##### 工作区与暂存区：一条三站流水线

实际操作时，你的改动要经过三站才正式入册：<strong>工作区</strong>是你正在编辑的文件夹，随意涂改；<strong>暂存区</strong>是用 git add 把"这次想记录的改动"挑出来放进去的地方，像一个打包台；<strong>仓库</strong>是用 git commit 把打包台上的内容正式记录成一次提交。

为什么中间要有打包台？因为它让你能分批提交：一口气改了五个文件，其中两个是一件事、另外三个是另一件事，那就分两次 add、两次 commit，历史清清爽爽。很多教程让人把"add 再 commit"背成机械动作，别这么背——先想清楚"这次提交只记哪件事"，再决定 add 什么。

##### 提交说明：写给三个月后的自己

commit 时那句说明（commit message），新手普遍不当回事，随手一个"update"完事。三个月后你想找"哪次提交改了登录逻辑"，面对一排一模一样的 update，等于面对一片没有碑文的坟地。

::: div .code-block
:::inline div .code-head
<span>TEXT · 同一件事的两种说明</span><span class="dots">···</span>
:::

```
update                          （半年后：你到底改了啥？）
修复：登录成功后跳转到错误页面的问题（半年后：一眼看懂）
```
:::

好说明就两个标准：一句话内说完，并且说清"为什么改"。写说明多花的十秒钟，未来会成倍还给你。

##### 动手前先感受一下：看别人的提交历史

不用装任何东西，你现在就能感受版本控制的威力：打开任何一个知名仓库，点文件列表上方的提交数（Commits），整部"编年史"就摊开了——每条提交都有说明、作者、时间。再随便点开一条，红红绿绿的 diff 就是那次改动的全部内容。看高手怎么写提交说明、怎么把一次大改动拆成几条小提交，是学这行当最快的方式。

#### 二、Git和GitHub的区别（关键概念！）

很多人第一次接触时会混淆这两个词，这里帮你梳理清楚：

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">对比项</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Git</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GitHub</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">本质</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">版本控制工具（软件）</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">代码托管平台（网站）</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">运行位置</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">本地电脑上</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">云端（浏览器访问）</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">核心职责</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">记录文件的每次变更（怎么改的、谁改的、何时改的）</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把Git仓库放到云端，方便存储、展示、协作</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">是否需要网络</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不需要，离线可用</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需要联网访问</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">归属</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">开源软件，由Linus Torvalds（Linux之父）创建</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">微软旗下产品</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">同类竞品</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SVN、Mercurial</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitLab、Gitee（码云）、Bitbucket</td>
                            </tr>
                        </tbody>
                    </table>
```

简单说：<strong>Git管"怎么记录变更"，GitHub管"变更放在哪、怎么协作"</strong>。Git是工具，在本地运行；GitHub是平台，把Git仓库放到云端，方便协作和展示。你可以只用Git不用GitHub（比如自己写代码做版本管理），但用GitHub一定要用Git（因为GitHub就是基于Git的）。

##### 三个高频误解，一次说清

<strong>误解一：不装 Git，只在网页上改，行不行？</strong>行。网页上点铅笔图标改文件、填一句说明提交，本质也是一次 commit。但网页编辑只适合小修小补：没法批量改文件、没法离线干活、很多进阶操作做不了。把 Git 装进电脑，才算拿到完整体验。

<strong>误解二：GitHub 打不开，我本地的东西是不是丢了？</strong>恰恰相反。Git 是"分布式"设计：clone 下来之后，你本地就有一份<strong>完整的仓库</strong>——全部历史、全部分支都在本地。云端只是同步与协作的场所，它暂时连不上，顶多推不了新提交，你的东西一个字节都不少。这也是 Git 和"把文件传网盘"最本质的区别。

<strong>误解三：想把别的平台上的仓库搬到 GitHub，要重新弄一遍吗？</strong>不用。仓库本质是同一套 Git 数据，搬家只是换一个远程地址再推送，具体步骤以平台文档为准。你在本章学的 Git 命令，在任何一家托管平台上都通用——学一次，到处能用。

##### 不想碰命令行？还有官方图形界面

GitHub 官方提供一款图形界面工具 GitHub Desktop：克隆、提交、推送、切分支，全部鼠标点点完成，改了哪些文件、每行改了什么一目了然。命令行和图形界面不冲突——不少熟手两个都装，日常点鼠标，出幺蛾子时开终端。先装哪个都行，本章讲的流程两边通用。

#### 三、GitHub的核心概念与功能

##### 基础概念

在动手之前，先认识几个高频词汇，否则看GitHub的界面会一头雾水：

- <strong>仓库（Repository，简称Repo）</strong>：一个项目对应一个仓库，里面存放着这个项目的所有代码文件、历史版本和文档。可以理解为一个"项目文件夹"。
- <strong>提交（Commit）</strong>：对代码的一次修改记录。每次Commit都附带说明信息，记录"这次改了什么、为什么改"。这是Git/GitHub能"时光倒流"的基础。
- <strong>分支（Branch）</strong>：从主线上分出来的独立开发线。比如你想加个新功能，可以开一个分支单独开发，开发完再合并回主线，不影响其他人。
- <strong>克隆（Clone）</strong>：把云端仓库完整复制一份到本地电脑，之后就可以在本地修改代码。
- <strong>推送（Push）/拉取（Pull）</strong>：Push是把本地代码上传到GitHub，Pull是从GitHub下载最新代码到本地。这是团队协作时同步代码的两个核心动作。
- <strong>合并请求（Pull Request，简称PR）</strong>：当你在一个分支上改完代码，想合并到主分支时，发起一个PR，让团队成员审查代码后再合并。这是GitHub协作的核心机制。
- <strong>议题（Issue）</strong>：用来记录bug、功能需求、讨论话题。每个Issue像一个讨论帖，可以指派负责人、打标签。
- <strong>Fork</strong>：把别人的仓库复制一份到自己账号下，你可以在自己的副本上随意修改，不影响原仓库。改好后可以给原作者发PR，请求合并你的改进。

##### 核心功能

GitHub提供的不只是代码存储，还包括：

- <strong>版本控制</strong>：记录每次代码更改的历史，改坏代码随时回到上一个正常版本。
- <strong>团队协作</strong>：支持多用户对同一项目的并行开发，多人同时开发不会覆盖、不会冲突。
- <strong>问题跟踪</strong>：用Issue记录bug和功能请求，方便团队跟进。
- <strong>项目管理</strong>：集成了待办事项、项目看板（Projects）等管理工具，相当于内置了一个轻量级Trello。
- <strong>自动化</strong>：通过<strong>GitHub Actions</strong>实现代码提交后自动编译、测试、打包、部署，是现代"CI/CD（持续集成/持续部署）"的核心工具。
- <strong>文档管理</strong>：README介绍项目，Wiki存放详细架构和开发规范，Pages甚至可以直接托管静态网站。
- <strong>代码托管与展示</strong>：每个仓库都有漂亮的网页展示，支持语法高亮，是你技术作品的"门面"。
- <strong>开源社区</strong>：你可以Star（收藏）喜欢的项目、Watch（关注）项目动态、Follow（关注）开发者，参与全球开源协作。

##### 把八个词串成一幅画：一次小组作业

概念看两遍还是容易忘，放进场景里就牢了。四人小组做课程设计：队长在 GitHub 建仓库，把作业要求写进 README；组员各自 clone 一份，各开一条分支写模块；有人发现需求有歧义，开一个 Issue 讨论，队长在楼下回复拍板；写完的部分 push 上去，发一个 Pull Request 请队长审查；队长确认没问题点合并，仓库配的自动测试（GitHub Actions）同步跑一遍确认没改坏东西；最后打上版本标签发个 Release，全组交作业。

回头看：仓库是家，分支是各自的草稿线，Issue 是议事厅，PR 是验收单，合并是交割，Actions 是质检员。一个词都不多余，一次作业全部用上。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
  <thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">概念</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">一句话比喻</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">对应的动作</th></tr></thead>
  <tbody>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">仓库</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">整个项目的相册，附全部"拍摄记录"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新建仓库 / git init / git clone</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">提交</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">带备注的游戏存档</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">git commit</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">分支</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">平行存档线</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">git branch / git switch</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">合并</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把草稿誊回正本</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">git merge / Pull Request</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fork</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把别人家的户型图复印一份，自己照着改</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">网页上点 Fork 按钮</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Push / Pull</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">上传 / 下载</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">git push / git pull</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Issue</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">项目议事厅里的发言帖</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">网页上开 Issue</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pull Request</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"我改好了，请过目"的验收单</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">网页上发 PR</td></tr>
  </tbody>
</table>
```
:::

#### 四、注册与上手：五分钟创建你的第一个仓库

动手前准备两样东西：一个常收信的邮箱（验证邮件和后续通知都发到这里），以及几分钟耐心——国内网络访问 GitHub 有时要多试几次，本章后面有专门的盒子讲对策。

##### 注册账号

1. 访问<a href="https://github.com" class="text-primary hover:underline" target="_blank" rel="noopener">github.com</a>，点击"Sign up"。
2. 填写邮箱、设置密码和用户名（用户名会出现在你的个人主页地址里，建议用英文，比如<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">github.com/yourname</code>）。
3. 完成邮箱验证和人机验证。
4. 选择免费方案（Free）即可，对个人用户完全够用。

选用户名给几条建议：用英文、别太长、别带 tmp、test 这类临时词——这个名字会跟着你很多年，出现在每个仓库地址和每次提交记录里。GitHub 支持日后改名，旧地址通常会自动跳转，但别人已经复制走的外链和远程地址未必跟着更新，一步到位最省事，细节以官方帮助文档为准。

密码设完，强烈建议顺手开启两步验证（Settings → Password and authentication，路径以界面为准）：以后在新设备登录，除了密码还要输一个动态验证码。官方已分批要求上传代码的账号开启两步验证，早开早安心——账号被盗最麻烦的不是丢代码，是有人以你的名义往开源项目里塞不干净的东西。

##### 创建第一个仓库

1. 登录后点击右上角"+"号，选"New repository"。
2. 填写仓库名（Repository name），比如<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">my-first-project</code>。
3. 写一段简短描述（Description），让别人知道这个仓库是干嘛的。
4. 选择公开（Public）或私有（Private）。公开仓库所有人可见，私有只有自己和协作者可见。免费账号也支持无限私有仓库。
5. 勾选"Add a README file"——README是项目的"说明书"，每个仓库都建议有。
6. 点击"Create repository"，你的第一个GitHub仓库就诞生了！

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>小知识：README是什么

{class="mt-1"}
README.md是一个Markdown格式的文件，是别人打开你仓库时第一眼看到的内容。一个好的README通常包含：项目简介、安装方法、使用示例、许可证、联系方式。写好README是程序员的基本素养，也是项目能否被他人使用的第一道门槛。
:::

##### 网页上直接改文件：你的第一次"提交"

仓库建好后不用急着装 Git，先在网页上完成一次修改找手感：点进 README.md，点右上角的铅笔图标，随便写点什么，拉到页面底部在 Commit changes 处填一句说明，点提交。刷新页面，你的改动已经带着完整历史躺在仓库里了。

注意提交按钮上方还有一栏选择：直接提交到主分支，或先新建一条分支再提交。自己练手随便选；以后在团队仓库里请默认选后者——为什么，看完第六节你就明白了。

##### 个人主页：你的技术名片

点右上角头像进 Your profile：头像、简介、置顶仓库（可以手动挑几个最能代表你的项目 pin 在最上面），以及那片绿色格子图——每格代表一天，颜色越深说明当天提交越多。这片格子是 GitHub 上最出圈的视觉符号，面试官点开候选人主页，它是最一眼可见的"活跃度名片"。但别走火入魔去硬刷格子——历史都留着，水分一查便知。

#### GitHub 功能逐个看：仓库、Issue、Pull Request、Actions、Wiki

第三节那张清单是地图，这一节带你把五个最常用的房间挨个推门看一遍：每个功能讲清"它解决什么问题"和"你第一次点开会看到什么"。

##### 仓库：项目的家

仓库主页默认停在 Code 标签：中间是文件列表，点文件夹层层进入，点文件看内容，Markdown 文件会渲染成排版好的页面；左上角是分支选择器；页面底部通常有一条彩色语言条，显示项目用了哪些语言、大致占比（以实际仓库为准）。右侧 About 栏放简介、话题标签（Topics）、许可证，下面可能挂着 Releases。

地址栏的规则顺便记一下：github.com/用户名/仓库名，前一段是"谁的家"，后一段是"哪个项目"。看清这两段，很多报错信息你都能自己读懂。右上角那个绿色 Code 按钮也值得单独说：点开显示的是仓库地址，HTTPS 和 SSH 两种，复制哪个取决于你怎么配置认证（第八节的建议清单里有讲），新手先用 HTTPS 就好。

文件区上方一排按钮也认识一下：Star 是收藏，Watch 是关注动态（可以选只关注发版等，选项以界面为准），Fork 是把仓库复制一份到你账号下。这三个按钮撑起了 GitHub 的社区互动。

##### Issue：项目的议事厅

Issue 是问题跟踪区，一句话理解：一个自带状态的留言板。每条 Issue 有编号、标题、正文（支持 Markdown）、标签（bug、enhancement 之类，具体由项目自定义）、指派人和一层层讨论。你报一个 bug 的标准姿势是写清四件事：做了什么、期望发生什么、实际发生了什么、你的环境（系统与 App 版本）。写得越清楚，越快有人接。

两个细节新手容易忽略：一是每层楼下方可以用表情回应，一个 👍 就是一张"我也是"的选票，维护者会参考这些反应排优先级；二是 Issue 被关闭不等于被否定——可能是已修复、与其他问题重复、或不在项目方向内，关闭时通常有说明。有些项目还会开 Discussions（论坛式讨论区，以仓库设置为准），使用提问这类"不算 bug 的话题"会被引导去那边聊。

##### Pull Request：一张验收单

PR 页面的核心是 diff 视图：红色行是删掉的，绿色行是新增的，审查者能在任意一行旁边发起行内评论。提交 PR 后最常见三种回应：Comment（评论）、Approve（批准）、Request changes（要求修改）——按钮名称以界面为准。另外还有 Draft PR（草稿状态），意思是"我还在写，先别急着审"，很多团队用它当进度信号。

PR 不只属于程序员：文档项目改错别字、翻译项目补一节译文，走的都是同一条流程。流程本身不分代码和文字。

##### GitHub Actions：云端的机器人工友

Actions 解决的是"每次提交之后那些重复劳动"：跑测试、检查格式、打包、部署网站。原理说穿了很简单：在仓库的 .github/workflows/ 目录里放一个配置文件（YAML 格式），写明什么事件触发（比如 push）、在什么环境跑、跑哪些命令，GitHub 的服务器就照着执行。语法细节以官方文档为准。

对新手友好的点是：不必从零写配置。大量现成的"动作"（Action）可以像积木一样拼进自己的流程文件；最快的学习方式是去别的仓库翻翻别人的 workflows 文件长什么样。公共仓库用 Actions 通常免费，私有仓库按用量计费，具体以官方定价页为准。

非程序员也能沾光：典型场景是"写完 Markdown 一 push，网站自动重新生成"——本章第七节的博客玩法就是这么跑起来的。

##### Wiki 与 README：一套说明书体系

项目的文档通常分三层：README 是门面，打开仓库第一眼看到的简介；Wiki 是书房，放详细教程、架构说明、开发规范（在 Wiki 标签里，部分仓库会关掉这个功能）；Releases 是货架，放打包好的正式版本。很多开源软件的"下载页"其实就是仓库的 Releases 页——找安装包直奔那里，通常比在文件列表里翻靠谱。

#### 五、基本工作流：从本地到云端

理解GitHub的工作流，核心是记住这个循环：<strong>本地修改 → 暂存 → 提交 → 推送 → 云端更新</strong>。下面用大白话解释每一步：

1. <strong>修改文件</strong>：在本地电脑上用编辑器写代码或改文档。
2. <strong>git add</strong>：把修改的文件加入"暂存区"，相当于告诉Git"这些改动我准备记录下来"。
3. <strong>git commit</strong>：把暂存区的改动正式记录成一个"提交"，附上一句说明，比如"修复登录bug"。这一步只在本地完成。
4. <strong>git push</strong>：把本地的提交上传到GitHub云端，这样别人就能看到了。
5. <strong>git pull</strong>：在开始工作前，先从云端拉取最新代码，确保本地和团队其他人保持同步。

对新手来说，记住这个口诀：<strong>"先pull后改，改完add，commit带说明，最后push上去"</strong>。养成这个习惯，团队协作就不会乱。

::: div .tip-box .rounded-lg .p-4 .mb-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>一句话记牢

{class="mt-1"}
Git最难的不是命令，是「每次提交只做一件事」这个习惯。
:::

##### 动手前：把 Git 装进电脑并报上名

到 Git 官网（git-scm.com）下载安装包，一路默认即可。装完打开终端（Windows 自带 Git Bash），输入 git --version，看到版本号就是装好了。第一件事是报名字和邮箱——它们会被写进你之后每一次提交的历史里：

::: div .code-block
:::inline div .code-head
<span>BASH · 终端</span><span class="dots">···</span>
:::

```
git config --global user.name "你的名字"
git config --global user.email "you@example.com"
```
:::

想好再写：作者信息进了历史，日后要改就得重写历史，很麻烦。邮箱建议用注册 GitHub 的同一个——这样提交才能正确关联到你的头像和贡献格子。认证方式也提前打一声招呼：HTTPS 方式第一次推送时，GitHub 不再接受账号密码，而是让你用浏览器授权或使用 Personal Access Token；SSH 则是配一次密钥以后免输。第八节的建议清单里有相关提醒，到时候照着配就行。

##### 第一次完整走一遍（附翻车点）

下面这串动作照着敲一遍，两分钟完事：

::: div .code-block
:::inline div .code-head
<span>BASH · 第一次提交并推送</span><span class="dots">···</span>
:::

```
mkdir hello-git
cd hello-git
git init
（随手写一个 README.md）
git add README.md
git commit -m "第一次提交：初始化项目"
git remote add origin https://github.com/你的用户名/你的仓库名.git
git push -u origin main
```
:::

两处容易翻车。其一，push 之前先用 git branch 确认本地分支名和远程一致——老版本 Git 的默认分支可能不叫 main，名字对不上就按官方文档改一下再推。其二，remote add 的地址写错不会当场报错，要等 push 才报——用 git remote -v 检查，写错了用 git remote set-url 改。

还有一个高频报错：push 被拒绝（rejected），多半是云端有你本地没有的新提交——比如你之前在网页上改过 README。正确姿势是先 git pull 合下来再推。千万别急着重试就加 --force：强制推送会覆盖云端历史，在团队仓库里属于事故级操作，这个习惯从第一天就别养。

##### git status：你的仪表盘

如果这一节只让你记一条命令，我会选 git status。它告诉你三件事：红色文件——改了还没暂存；绿色文件——暂存了还没提交；一片干净——本地没有待处理的改动。每步操作前先瞟一眼 status，绝大多数"我怎么把不该传的东西传上去了"的事故，都能在这一步拦下来。

#### 六、团队协作流程：Pull Request是怎么工作的

GitHub最强大的地方在于它的协作机制。一个典型的团队协作流程是这样的：

1. <strong>开分支</strong>：从主分支（通常叫main或master）开一个新分支，比如<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">feature/login</code>，在这个分支上开发新功能。
2. <strong>开发并提交</strong>：在新分支上写代码，多次commit记录进度。
3. <strong>推送到GitHub</strong>：把分支push到云端仓库。
4. <strong>发起Pull Request</strong>：在GitHub网页上发起PR，请求把你的分支合并到主分支。写清楚这个PR做了什么改动、为什么改。
5. <strong>代码审查（Code Review）</strong>：团队成员查看你的代码，提出意见或建议修改。你可以根据反馈继续commit，PR会自动更新。
6. <strong>合并</strong>：审查通过后，点击"Merge"把代码合并到主分支。你的贡献就正式进入项目了！

这套流程保证了<strong>任何代码进入主分支前都经过审查</strong>，大大降低了出错概率。开源项目也是用这套机制接受全世界陌生人的贡献——你完全可以在某个知名开源项目上提交PR，被采纳后你就是这个项目的贡献者了。

正式的团队仓库，一般还会给主分支开「分支保护」（Branch protection）：开了之后谁都不能直接往主分支push，所有改动必须走PR、审查通过才能合并——想绕都绕不过去。新建仓库时默认分支叫什么名字，以平台当前提示为准。给别人的项目做贡献，路径也一样：Fork、建分支、小步提交、写清改了什么、发PR等Review，第三十八章有完整的五步流程。

再补三个实战细节，都是第一次发 PR 时的高频疑惑：

- <strong>描述里写 Fixes 加编号</strong>：如果这个 PR 修复了某个 Issue，在描述里写上比如 Fixes #42，合并后对应 Issue 会自动关闭。这是 GitHub 的官方语法，比口头说"修好了那个 issue"可靠得多。
- <strong>继续提交会自动更新同一个 PR</strong>：收到审查意见后，往同一条分支继续 push 就行，PR 页面会自动追加新提交，不要关掉旧 PR 另开新的——审查记录断成两截，谁看着都累。
- <strong>绿勾红叉是自动检查</strong>：不少项目给 PR 配了自动测试，页面下方会显示检查状态。红叉不一定是你的错，可能是环境或项目自身问题，点开详情看日志再下结论。

#### 七、GitHub的典型应用场景

##### 学生参加比赛与课程项目

计算机系学生参加ACM、黑客松、毕业设计，几乎都离不开GitHub。它既能作为团队协作平台，又能作为作品展示窗口——比赛评委可以直接看你的仓库，了解代码质量和协作过程。很多公司招聘时也会要求附上GitHub主页，作为技术能力的证明。

小组作业的具体分工姿势：把任务拆成一个个 Issue，@ 到对应的人；领了任务就把 Issue 指派给自己，做完发 PR 并关联那个 Issue。期末回看，谁做了什么、什么时候做的，仓库替你们记着——小组分工扯皮的老毛病，多一半是被这个治好的。

##### 个人知识库与笔记托管

非程序员也能用GitHub。很多人用它托管学习笔记、技术博客（配合GitHub Pages可以免费建站）、电子书。Markdown格式写作 + Git版本管理 + 云端备份，三合一。

一个容易忽略的细节：笔记仓库建议先设为私有，除非你确定全部内容都见得了光。私有仓库同样有完整历史和同步能力，只是别人看不见——哪天想公开了，改一个设置就行。

##### 🌐 参与开源项目

GitHub是全球开源运动的核心阵地。你可以Fork喜欢的项目，修改后发PR回馈社区；也可以单纯Star收藏好项目，跟踪更新。参与开源是提升技术、积累声誉的绝佳途径。

具体怎么发第一个 PR、怎么跟维护者打交道，本章后面有专门一节，这里先按下不表。

##### 自动化部署与CI/CD

借助GitHub Actions，可以实现"代码一push，自动测试+自动部署到服务器"的全自动流程。很多个人博客、文档站点都是这么搭建的，写完文章push一下，网站就自动更新了。

##### 💾 代码备份与多设备同步

把代码仓库当作云盘用，换电脑、多设备办公时，git pull一下就能拿到最新代码，再也不用U盘拷来拷去。

两条补充提醒。其一，仓库别当照片视频网盘用：Git 对大二进制文件不友好，仓库会越滚越胖、推送越来越慢，媒体文件请交给网盘。其二，手机上有官方的 GitHub App，地铁上翻翻 Issue、回条评论很方便；但正经改代码请回到电脑——小屏幕上看 diff，眼睛受罪还容易看漏。

#### 仓库怎么找：搜索技巧与鉴别方法

会用 GitHub 的第二步（第一步是注册）是会"找东西"。平台上仓库太多了，搜得到、挑得准，比你多背十句命令都重要。

##### 搜索框里的小语法

GitHub 搜索支持过滤器写法，随手记几个（完整语法以官方搜索文档为准）：关键词后面加 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">stars:&gt;1000</code> 只看收藏破千的项目；加 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">language:python</code> 限定语言；加 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">in:readme</code> 让关键词去 README 里找。组合起来用，比如搜"笔记 stars:&gt;500"，一页就能筛出人气高的笔记工具。搜索页左侧通常还有语言、许可证等筛选面板，点点就能用。

##### 判断一个仓库靠不靠谱：看五个信号

- <strong>README 认不认真</strong>：有没有讲清"这是什么、怎么装、怎么用"。敷衍的 README 往往对应敷衍的项目。
- <strong>最近提交时间</strong>：仓库首页能看到最后一次提交是什么时候。长期没人理的仓库，问题报上去多半也没人接。
- <strong>Issue 区的氛围</strong>：维护者有没有认真回复，还是一排问题石沉大海。这决定了你以后求助的体验。
- <strong>有没有 LICENSE 文件</strong>：没有许可证的仓库，严格来说你不能随便拿去二次分发。
- <strong>Star 数与热度</strong>：仅作参考。小而美的工具可能星数不高，但恰好是你要的；星数爆炸的项目也可能早已停止维护。

一个小习惯顺手养成：发现好仓库又暂时用不上，别只丢进收藏夹——在自己建一个"灵感清单"私有仓库，记一行链接加一句"为什么好"。收藏夹会积灰，写下一句话的仓库不会。

还有一个反向用法别浪费：找仓库之前，先想清楚"我要解决什么问题"。以问题为关键词去搜（比如"安卓 相册 整理"），比以工具名去搜更容易挖到冷门好货——很多好工具的名字起得平平无奇，但它们对"自己解决什么问题"的描述写得清清楚楚。

##### awesome 清单：站在别人的筛选上

社区有个好习惯：把某类主题的优质资源整理成"awesome 加主题名"形式的仓库。找学习材料时，先搜 awesome 加关键词，通常能直接捡到一份经过众人筛选的清单，顺藤摸瓜比大海捞针快得多。收藏前记得看一眼清单的最近更新时间——过时的清单，价值会打对折。

##### 许可证顺带扫个盲

挑仓库时会反复碰到许可证（LICENSE）这个词，新手记住三句话就够：一，没有许可证的仓库，默认权利全部保留，别拿去二次分发；二，MIT 这类宽松许可证，使用、修改基本随意，但要把原文版权声明带上；三，GPL 这类"传染性"许可证，要求你二次分发时同样开源——拿不准就只自己用、不改编分发，或先读一遍许可证原文（它们都不长）。

#### 一次完整的 Pull Request：从 Fork 到合并

第六节讲了 PR 在团队里怎么转，这一节把镜头对准你一个人，走一遍从零到合并的完整流程。场景很简单：你常用的一个开源文档项目，README 里的安装命令有个错别字，你决定修掉它。别嫌事小——第一次贡献，越小越容易走完全流程。

##### 第 0 步：先看看有没有人干过

动手前花两分钟：进项目的 Issue 区搜一搜相关关键词，确认没人报过同样的问题；顺手翻翻项目有没有 CONTRIBUTING.md（贡献指南）——很多项目的分支命名习惯、PR 要求都写在里面，照着做能省一半来回。

##### 第 1 步：Fork——把项目复制一份到你名下

在原仓库页面右上角点 Fork，GitHub 会在你的账号下生成一份一模一样的副本，地址变成"你的用户名/原项目名"。之后你所有的修改都发生在自己副本上，原仓库毫发无损——这就是开源世界"人人可改"的机制基础。

##### 第 2 步：克隆你的 Fork，开一条新分支

::: div .code-block
:::inline div .code-head
<span>BASH · 终端</span><span class="dots">···</span>
:::

```
git clone https://github.com/你的用户名/那个项目.git
cd 那个项目
git switch -c fix-install-command
```
:::

分支名用小写英文加短横线，见名知意：fix- 开头修 bug，feature- 或 add- 加功能，docs- 改文档。别叫 backup1、new2——维护者看到这种名字，心里已经先扣了一分。

##### 第 3 步：小步修改，认真提交

改完那个错别字，add 加 commit，说明写清楚："修复 README 中安装命令的拼写错误"。一条铁律：一个 PR 只做一件事。顺手把同一页另外两个错别字也修了可以；顺手"重构"半本手册不行——后者会让审查者失去耐心，你的错别字反而石沉大海。

##### 第 4 步：推送，然后在网页上发 PR

git push 之后打开你的 Fork 页面，通常会自动弹出一条 "Compare & pull request" 提示（以界面为准），点它即可；没弹也不要紧，手动找 "Contribute → Open pull request"。注意方向别搞反：base 选原仓库的主分支，head 选你的分支——意思是"请求把我这条线的改动并过去"。

##### 第 5 步：写一份让人想点的 PR 描述

描述就三段：改了什么（一句话）；为什么改（现象加原因）；怎么验证的（比如"照新命令重新装了一遍，正常"）。有截图放截图；如果修复了某个 Issue，写上 Fixes 加编号。维护者大多用业余时间处理 PR，描述清楚的那份永远先被看——这是被无数项目验证过的规律。

##### 第 6 步：面对审查意见

提交后进入等待期，短则几小时，长则几周——等是常态，礼貌催一次可以，连环催不行。意见一般分两类：明确要改的，照做，继续 push 到同一条分支；风格建议或疑问，可以回复解释，也可以照改。有几条分寸要拿捏：别在 PR 里带情绪，摆事实、引文档；让人改十处不是刁难，是这个项目的门槛；当然也允许你有理有据地说明"我倾向 A 方案，因为……"——认真的讨论在开源社区是受欢迎的。

##### 合并与收尾

审查通过后，有权限的维护者点合并。合并方式可能不止一种（普通合并、压成一条提交、变基式合并），取决于仓库设置，你不用操心，等结果就行。合并完成后你的分支使命结束，页面上会提供删除分支的按钮，删了干净。最后记得把自己的 Fork 对齐一下：仓库页面通常有 "Sync fork" 按钮（以界面为准），点一下就和原项目同步了。

##### 冲突了怎么办：一次实战认识 merge conflict

如果在你 PR 挂着期间，主分支也改了同一个文件，GitHub 会在 PR 页面提示存在冲突（conflicts），合并按钮变灰。这不是你搞砸了，是正常现象。处理思路：把最新的主分支拉下来，合进你的分支，手工把冲突解决掉，再推上去：

::: div .code-block
:::inline div .code-head
<span>BASH · 解决冲突的本地操作</span><span class="dots">···</span>
:::

```
git remote add upstream https://github.com/原作者/那个项目.git
git fetch upstream
git switch fix-install-command
git merge upstream/main
（打开提示冲突的文件，找 &lt;&lt;&lt;&lt;&lt;&lt;&lt; 标记）
```
:::

冲突文件里会看到这样的标记：

::: div .code-block
:::inline div .code-head
<span>TEXT · 冲突标记长这样</span><span class="dots">···</span>
:::

```
&lt;&lt;&lt;&lt;&lt;&lt;&lt; HEAD
你分支里的内容
=======
主分支上的内容
&gt;&gt;&gt;&gt;&gt;&gt;&gt; upstream/main
```
:::

你的任务是在两组内容之间拍板：留一边，或者融合成新的，然后把 &lt;&lt;&lt;&lt;&lt;&lt;&lt;、=======、&gt;&gt;&gt;&gt;&gt;&gt;&gt; 这些标记行全部删干净，git add 这个文件，完成合并提交，最后 git push。冲突解决的本质是"读懂两边意图再拿主意"，多做两次就熟了。

#### 开源贡献指南：从旁观者到贡献者

第七节提过"参与开源"，这一节把它展开成一份可执行的路线图。先把定义放宽：贡献不只是写代码——报一个说清楚的 bug、修一处文档错别字、补一段翻译，都算数，而且是维护者最欢迎的那类。

##### 从你真实在用的项目找起

挑项目的第一原则：从你天天在用的东西里找。你是它的用户，最有动力，也最知道痛点在哪——某个开源播放器的一个按钮在深色模式下看不清，某本开源手册第三章少了一个例子，这些你比谁都清楚。别一上来就盯着最有名的几个大项目，它们的贡献门槛高、排队时间长；活跃的中小项目才是练手的黄金区。

##### 认准"欢迎新手"的标记

很多项目会给适合新手的任务打上 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">good first issue</code> 标签（好上手的第一单），也有项目用 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">help wanted</code> 标记需要人手的活，两种都是社区通行习惯，具体含义以项目说明为准。在项目的 Issue 列表里按标签筛一遍，或在搜索框里用标签加语言过滤，就能找到一排"等你来"的任务。第一次就挑那种改一两个文件的小活——走得通，比走得远重要。

##### 进项目先读三份文件

动手前翻一遍：README（项目是什么、怎么跑）；CONTRIBUTING.md（怎么参与——分支怎么命名、PR 要不要关联 Issue、有没有格式要求）；CODE_OF_CONDUCT.md（社区行为准则）。不是每个项目三份都齐，缺哪份就多翻翻已有的 Issue 和 PR——看老成员怎么讨论，你就学到了这个社区的脾气。

##### 提交前的自查清单

- 这个问题或需求，Issue 区里是不是已经有人提过？先搜再写。
- 我的改动够不够小、够不够聚焦？一个 PR 只解决一件事。
- 改了行为，文档或测试要不要跟着改？只改一半，审查者一定会提。
- 提交说明写清"为什么"了吗？PR 描述里有验证方法吗？
- 分支命名和格式符合项目约定吗？对照 CONTRIBUTING 再过一遍。

##### 与维护者打交道的分寸

记住一个前提：绝大多数维护者是拿业余时间免费干活的人。所以——提问前先搜索，是最大的礼貌；一次只提一件事，别把新功能需求和 bug 混在同一个 Issue 里；PR 发出去等几天再礼貌跟进一次，别连环 @；被要求改代码不是刁难，是在帮你的成果过门槛；PR 被关闭也别气馁，问一句原因，下一单会更准。

语言问题也现实：不少国际项目用英文交流，看不懂就先用翻译工具，回复不必追求文采，把事说清就行。国内项目多直接用中文——看仓库里大家用什么语言，你跟着用什么。

##### 不写代码的五种贡献

- <strong>报 bug</strong>：附上复现步骤和环境信息。一条能复现的报告，顶得上十条"用不了"。
- <strong>修文档</strong>：错别字、失效链接、说不清的步骤——改动小，价值大，合并也快。
- <strong>做翻译</strong>：把文档译成中文，很多项目求之不得。
- <strong>回答 Issue</strong>：你踩过的坑帮后来者填上，维护者省下的时间都算你的贡献。
- <strong>写教程、做视频</strong>：帮项目被更多人知道，维护者通常乐意置顶推荐。

##### 开 Issue 也有模板

报 bug 的正文照这个格式写，被处理的速度会快很多：标题一句话说清现象；正文第一段写你的环境（系统、版本）；第二段写复现步骤，一至三步，每步一行；第三段写"期望结果"和"实际结果"的对比，能附截图或简短录屏更好。别用"它坏了"当标题——维护者看到这种标题只能先反问你一轮，来回几天就这么耗掉了。

##### 把贡献变成履历

被合并的 PR 会永久留在项目历史里，署着你的名字。简历里可以直接放 PR 链接，面试官点开就能看到你改了什么、审查里讨论了什么、最后怎么被合并——这段过程本身就是证明，比一句"有开源经验"扎实得多。第一单哪怕只是修了个错别字，它也是从零到一的那一步。

#### 开源协议入门：你写的代码，别人能怎么用

前面"仓库怎么找"那节给过许可证的三句话扫盲，这一节把话展开讲全：开源协议到底是什么、常见的几种差别在哪、你该给自己的项目选哪一个、用别人的代码时怎么算账。无论你是"写代码放上去的人"还是"拿代码来用的人"，这一课都躲不开。

##### 1. 协议的本质：没有它，默认"保留所有权利"

代码公开不等于放弃权利。一个仓库没有 LICENSE 文件，著作权法默认作者保留所有权利——你可以看（公开即可见）、可以学（阅读和借鉴思路一般没问题），但不能把代码复制进自己的项目里分发或商用，哪怕加了署名也不行。开源协议就是作者签发的一份"使用合同"，写清楚三件事：允许你做什么、要求你必须做什么、禁止你做什么。它是"开源"这个词的法律地基——没有协议的"开源仓库"，只是"公开源码"，不是真正意义上的开源软件。

##### 2. 主流协议逐个看

<strong>MIT</strong>：最流行的宽松协议，全文不到两百词，翻译成人话就是"随便用，商用、闭源、改名出售都行，唯一条件是保留版权声明和协议文本"。个人小项目几乎不会选错。它的短板是没有专门的专利条款，涉及专利的正式项目多会换 Apache-2.0。

<strong>Apache-2.0</strong>：同样宽松（可商用、可闭源），但多写了几页企业关心的内容：贡献者明确授予专利使用权（防止"先用你的代码、再告你侵犯专利"）、修改文件要标注、不得用项目商标宣传。企业项目和有专利顾虑的项目常选它。

<strong>BSD（2-clause / 3-clause）</strong>：和 MIT 同一路数的宽松协议，3-clause 版多一条"不得用原作者名义为衍生产品背书"——防止别人拿你的名字打广告。

<strong>GPL（v2 / v3）</strong>："传染性"协议（术语叫 Copyleft）的核心代表：你的程序用了 GPL 代码，再分发时整个程序就必须按 GPL 开源。它把"开源精神"变成了法律义务——你可以随便用、随便改，但改完放出来时也得让别人能继续改。v3 补了专利授权和硬件锁死相关的条款。LGPL 是"库"的例外版本：你的闭源软件可以链接 GPL 库而不必整体开源，但对库本身的修改仍要开源。AGPL 把"分发"扩展到了网络服务——哪怕你只是拿它架个网站不发布代码，也要向使用网站的人提供源码，堵住了"只提供在线服务就不算分发"的口子。

<strong>MPL-2.0</strong>：折中派，"按文件传染"——你修改的文件要开源，新增的其他文件可以闭源。想给闭源产品留点余地、又想让核心回馈社区的项目常选它。<strong>CC0 / Unlicense</strong>：干脆放弃权利，送进公共领域，"爱怎么用怎么用"。

##### 3. 一张表看懂六个常用协议

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
<thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">协议</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">一句话人设</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">商用</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">闭源分发</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">明确专利授权</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">传染性</th></tr></thead>
<tbody>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MIT</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最宽松的"拿去用"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可以</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可以</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">无</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">无</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apache-2.0</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">宽松＋专利清楚</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可以</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可以</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">有</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">无</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BSD-3</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">类 MIT＋不许冒名背书</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可以</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可以</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">无</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">无</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPL-3.0</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">要开源就一起开源</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可以</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不行</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">有</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">强</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">LGPL-3.0</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">链接可以，改库要开源</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可以</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">链接可以</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">有</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">弱</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AGPL-3.0</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">在线服务也要开源</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可以</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">服务端不行</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">有</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">最强</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MPL-2.0</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">按文件开源</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可以</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可以（改过的文件除外）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">有</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">文件级</td></tr>
<tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">CC0</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">送入公共领域</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可以</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">可以</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">无</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">无</td></tr>
</tbody>
</table>
```
:::

##### 4. 怎么选：三个问题定协议

给自己或团队的项目挑协议，想清楚三个问题就够。第一，<strong>你在意别人拿去闭源商用吗</strong>？不在意，选 MIT 或 CC0；在意专利安全，选 Apache-2.0；希望"用我代码的人也回馈开源"，选 GPL 家族。第二，<strong>它是"库/框架"还是"完整应用"</strong>？库用强传染协议会吓跑集成方（LGPL、MPL 更友好），完整应用选 GPL 名正言顺。第三，<strong>将来会不会只提供在线服务、不发布代码</strong>？会，又想强制开源，就得 AGPL。拿不准时，个人小工具 MIT 几乎不会错，企业项目问一句法务——大多数的答案是 Apache-2.0。

##### 5. 用别人代码的人：三条硬规矩

第一，<strong>先找 LICENSE 再复制代码</strong>——没有协议的仓库，再心动也别搬，想要就去 Issue 区礼貌地问作者能不能补一个授权。第二，<strong>照办条款里的"必须"项</strong>：保留版权声明、按需附 NOTICE、衍生作品按协议开源，这些不是"建议"而是合同义务。第三，<strong>把传染性算成账</strong>：闭源产品里链进 GPL 代码，产品分发时就得整体开源——商业集成前想清楚，别"先抄了再说"。混装依赖时还要留意协议兼容性，一个常见的坑：Apache-2.0 与 GPLv3 兼容，但与 GPLv2 不兼容。

##### 6. 维护者视角：怎么给仓库挂上协议

GitHub 网页端就够用：仓库里 Add file，文件名写成 LICENSE 时会弹出"Choose a license"模板，MIT、Apache-2.0、GPL-3.0 等常见协议直接选，填好年份和姓名提交即可；本地操作就在仓库根目录放一个 LICENSE 文件。README 里也可以标注协议标识（如 MIT），方便工具自动识别。还有一件事趁早想好：<strong>协议可以换，但要征得所有贡献者同意</strong>——项目火起来之后再改协议，找齐几十位贡献者的同意书是个大工程，所以第一天就选好，比事后补救容易得多。

- <strong>很多人以为"开源=放弃版权"</strong>，其实恰恰相反：协议正是靠著作权才生效的授权，作者对未授权的使用方式随时可以维权。
- <strong>很多人以为"署名了就能用任何代码"</strong>，其实署名只是 MIT、BSD 的条件之一；GPL 还要求开源，没有协议的则什么都不能用。
- <strong>很多人以为"MIT 没有条件"</strong>，其实有——保留版权与许可声明，少这一行就是违约。
- <strong>很多人以为"双重许可=两个都能要"</strong>，其实同一代码按两种协议发放（常见的是 GPL 版＋付费商业版）时，你只能选其中一份并遵守它的全部条款。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-quote-left mr-2"></i>一句话记牢

{class="mt-1"}
没有协议的代码"看着免费、用着违法"；选协议不是选信仰，是在给"你和所有后来者"定一份使用合同——想清楚再挂，挂了就别轻易改。
:::

#### Git 命令速查表：先收藏，用到再查

命令不用背，常用的自然会记住，不常用的查表就行。下面按场景分六组，"注意"一栏专门标新手容易踩的地方。每条命令的具体行为，终端里输入 git help 或"命令 --help"随时可查，以你本地版本的帮助文档为准。

##### 初始化与配置

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
  <thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">命令</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">干什么用</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">新手注意</th></tr></thead>
  <tbody>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git init</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把当前文件夹变成 Git 仓库</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">在项目根目录执行，别在磁盘根目录乱试</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git clone &lt;地址&gt;</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把云端仓库完整复制到本地</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">地址从仓库页面绿色 Code 按钮复制</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git config --global user.name / user.email</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">设置提交者身份</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">邮箱用注册 GitHub 的同一个</td></tr>
  </tbody>
</table>
```
:::

##### 日常四件套

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
  <thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">命令</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">干什么用</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">新手注意</th></tr></thead>
  <tbody>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git status</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">看当前状态</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每步操作前先看一眼</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git add &lt;文件&gt;</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把改动放进暂存区</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">git add . 会暂存全部改动，想清楚再用</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git commit -m "说明"</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">正式记录一次提交</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">说明写"为什么"，别只写 update</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git push</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把本地提交推上云端</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">被拒先 pull，别急着 --force</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git pull</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把云端更新拉到本地</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">开工前先拉一次，保持同步</td></tr>
  </tbody>
</table>
```
:::

提交说明还有个社区常见的小习惯：用前缀标类型，比如 fix: 修 bug、docs: 改文档、feat: 加功能——扫一眼历史就知道每条提交在干什么。这只是流行习惯而非标准，项目有自己的约定就照项目的来。另外，说明里别堆表情符号，一两个点睛可以，刷屏就吵了。

##### 查看历史与差异

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
  <thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">命令</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">干什么用</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">新手注意</th></tr></thead>
  <tbody>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git log</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">查看提交历史</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">翻页后按 q 退出</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git log --oneline</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每条提交压成一行</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">快速浏览用</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git diff</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">看未暂存的改动</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">加 --staged 看已暂存的</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git show &lt;提交编号&gt;</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">看某次提交的详情</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">编号从 git log 里复制</td></tr>
  </tbody>
</table>
```
:::

##### 分支管理

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
  <thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">命令</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">干什么用</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">新手注意</th></tr></thead>
  <tbody>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git branch</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">列出本地分支</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">当前分支带星号</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git switch &lt;分支&gt;</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">切换分支</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">旧教程里的 git checkout 是同一件事的老写法</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git switch -c &lt;新分支&gt;</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">新建并切换</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">名字用英文短横线风格</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git merge &lt;分支&gt;</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把指定分支并进当前分支</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">合并前先确认自己在哪条分支</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git branch -d &lt;分支&gt;</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">删除已合并的分支</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">大写 -D 是强删，慎用</td></tr>
  </tbody>
</table>
```
:::

##### 远程操作

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
  <thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">命令</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">干什么用</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">新手注意</th></tr></thead>
  <tbody>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git remote -v</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">查看已配置的远程地址</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">remote add 写错不报错，push 才报</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git remote add origin &lt;地址&gt;</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">关联远程仓库</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">写重复会报错，set-url 可改</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git push -u origin &lt;分支&gt;</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">首次推送并建立关联</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">之后该分支直接 git push 即可</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git fetch</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">只下载不合并</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">想先看看云端有什么再决定时用</td></tr>
  </tbody>
</table>
```
:::

##### 撤销与补救

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
  <thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">命令</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">干什么用</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">新手注意</th></tr></thead>
  <tbody>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git restore &lt;文件&gt;</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">丢弃某文件未暂存的改动</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">丢弃即消失，先想清楚</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git restore --staged &lt;文件&gt;</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">移出暂存区，改动保留</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">和上一条的区别先分清</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git commit --amend</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">修改最后一次提交</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">只对还没 push 的提交用</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git reset --soft HEAD~1</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">撤销最后一次提交，改动退回暂存区</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">想保留劳动成果时用它</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git revert &lt;提交&gt;</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用一条"反向提交"抵消某次改动</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">已推送的提交用 revert，别用 reset</td></tr>
    <tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git reflog</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">看指针移动历史</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"完了我搞没了"时先跑它</td></tr>
  </tbody>
</table>
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2" aria-hidden="true"></i>小贴士：先开个练习仓库

{class="mt-1"}
撤销类命令第一次用，先开一个练习仓库随便造：新建一个空文件夹，git init，随手提交几次，把表里的命令挨个跑一遍，看每条命令执行后 git status 和 git log 的变化。半小时的练习，换来以后所有的淡定。
:::

#### Markdown 速成：GitHub 上的通用文字格式

前面反复出现 Markdown 这个词——GitHub 上从 README 到 Issue 到 PR 描述，全用它。花十分钟学会下面这些，你在 GitHub 上的"写字"能力就够用了；语法细节以官方指南为准，这里只挑最常用的。

##### 基础八式

- <strong>标题</strong>：行首加 # 到 ######，# 越多字越小，# 和文字之间要留一个空格。
- <strong>加粗与斜体</strong>：文字前后各两个星号是加粗，一个星号是斜体。
- <strong>列表</strong>：行首短横线是无序列表，数字加点是有序列表。
- <strong>代码</strong>：行内一段用反引号包起来；整段代码用三个反引号上下包住，还能标注语言拿到高亮。
- <strong>链接</strong>：方括号写文字，紧跟圆括号放网址。
- <strong>图片</strong>：比链接多一个感叹号开头。
- <strong>引用</strong>：行首大于号，显示成缩进的引用块。
- <strong>分隔线</strong>：单独一行三个短横线。

再送一个 GitHub 专属好物：任务清单。行首写短横线加方括号，GitHub 会渲染成可勾选的待办框，在 Issue 和 PR 里点一下就能打勾，进度自动显示成"几项里完成了几项"。列计划、写审查要点，都用得上它。

这些语法在 README、Issue 正文、PR 描述、评论、Wiki 里全部通用——一处学会，处处能用。编辑框右上通常有预览（Preview）页签，写完切过去看一眼排版再提交，避免满屏星号的尴尬。

两个增值技巧：写 @ 加用户名，对方会收到通知；在正文里写 # 加 Issue 或 PR 的编号，会自动变成可点击的链接。讨论能不能"活"起来，靠的就是这两招。表格用纯 Markdown 写起来比较费劲，新手先用列表顶替，真需要了再查官方指南。

手机上看也没问题：App 和网页都会把 Markdown 渲染成排版好的样子；不过手机适合读和改两行评论，长 README 还是回电脑上写。

最后给个可抄的模板，一个迷你 README 长这样：

::: div .code-block
:::inline div .code-head
<span>MARKDOWN · 一个迷你 README</span><span class="dots">···</span>
:::

```
# 我的读书笔记
每周读完一本书，在这里记录几句。

## 本周在读
- 第三章的比喻很妙，下周写读后感

&gt; 年度目标：读完 **20** 本。
```
:::

##### README 的四段骨架

不会写 README 就按这个骨架填：第一段，这是什么——两三句说清它解决什么问题；第二段，怎么用——安装、运行和最常见的用法；第三段，怎么参与——欢迎什么形式的贡献；第四段，许可证和联系方式。先把骨架填满，好不好看可以慢慢迭代——README 本身也是要一遍遍提交修改的。写完切到预览页签看一眼：README 是仓库的门脸，门脸整齐，路过的人才愿意进来坐坐。

#### Projects 看板：把团队任务贴上墙

Issue 解决"事情记下来"，Projects 解决"事情排起来"。它是一块可自定义的看板：建几列（比如"待办 / 进行中 / 已完成"），把 Issue 和 PR 像卡片一样贴上去，推进到哪一步就拖到哪一列，整个项目的进度一眼见底。界面细节以官方为准，但玩法和便利贴白板一模一样。

小组作业这么用：开学第一周建看板，把作业拆成十几张卡片；每周例会拖一次卡片，谁手里压着几张、哪张卡了两周，谁也别想打马虎眼。个人也能用：把"想读的书、想写的文章、想做的工具"全开成卡片，一块看板就是你的个人待办墙。

和 Issue 的配合是关键：卡片不用凭空造，多数时候直接把现有 Issue 加进看板就行；有些视图还能按状态自动归类（自动化规则以官方文档为准）。看板是轻的，规则是重的——列名怎么定、多久拖一次，全组商量好并坚持执行，比用什么工具重要。

#### 把 GitHub 用进写作与学习：三个可抄的工作流

前面讲的是通用功能，这一节给你三套拿走就能用的组合拳，分别对应三种最常见的需求。

##### 工作流一：个人笔记本（私有仓库加每日一提交）

建一个私有仓库，按文件夹分主题：工作、学习、生活。每天睡前花五分钟，把当天值得记的东西写进对应文件，提交一次。半年后你会得到什么？任何一条笔记都能按时间检索；想法是怎么演化的有迹可循；换电脑或出门在外，pull 一下或打开网页就行。开头别追求漂亮，先记下来再说——提交历史会帮你把碎碎念串成思路。

##### 工作流二：课程与读书笔记（一个仓库一门课）

一门课或一本书一个仓库：README 写大纲，每章一个文件，笔记里开一个"问题区"记下没搞懂的地方；搞懂一个，就去 Issue 区开一条再关一条，问题清单自带进度条。期末复习时，提交历史就是你的学习时间线——哪周松懈了、哪章反复回头，一目了然。

##### 工作流三：家庭共享记录（你来操作，家人用网页）

想跟家人共维护一份记录——装修进度、旅行计划、家庭账本——就建一个私有仓库，把家人加为协作者。分工可以很清晰：懂技术的你负责结构和提交，家人用手机 App 或网页直接改文件、留评论，对他们来说操作难度接近微信收藏夹。改动全部留痕，谁改的、什么时候改的，再也不用争"我们说好的方案怎么又变了"。隐私别大意：身份证号、银行卡号这类信息，用什么工具都不该进仓库。

三套工作流的共同点：把"反复修改、要留痕"交给 Git，把"多人查看"交给 GitHub，人只负责内容本身。

#### Git 进阶技巧：stash、cherry-pick、rebase、submodule

这一节的几个技巧，新手第一年可能只用得上其中一两个。但知道它们存在很重要——哪天遇到问题去搜索，至少知道该搜哪个词。

##### stash：把桌上的东西先塞抽屉

场景：你在 feature 分支改到一半，线上冒出紧急 bug，要马上切分支去修。直接 switch 会拖着半成品改动到处跑，提交半成品又污染历史。git stash 登场：它把当前所有未提交的改动打包收进"抽屉"，工作区瞬间干净；修完 bug 切回来，git stash pop 把东西原样倒回桌面。攒了几包没取的，git stash list 可以看。

一个注意点：pop 是"倒出来即销毁"，藏了一堆包的时候看清编号再取，别一股脑乱倒。更多用法以官方文档为准。

##### cherry-pick：只摘这一颗提交

场景：你在发布分支上修了一个 bug（一次提交），开发分支也需要这个修复，但不要发布分支上的其他改动。git cherry-pick 加提交编号就是"摘樱桃"：把指定的那次提交复制一份应用到当前分支。中途撞上冲突，处理方式和 merge 完全一样。

一个常见的坑：摘过去的提交是"新的一份"，两边编号不同——日后翻历史，别把两个编号当成同一次改动。

##### rebase：把提交重新排队

rebase 字面意思是"变基"——把你的提交挪到另一个地基上重新排。常用场景有两个：其一，git pull --rebase，拉取远程更新时用变基代替合并，历史保持一条直线，没有密密麻麻的合并记录（可以配置成默认行为，写法以官方文档为准）；其二，交互式变基（git rebase -i），在自己还没推送的功能分支上把零碎提交合并、改说明、调顺序，让 PR 干净易审。

一条铁律请背下来：<strong>已经推送到公共分支、别人可能已经拉走的提交，不要 rebase</strong>。变基会改写历史，等于把别人脚下的地板换掉，协作者的世界会瞬间错乱。拿不准就别变基，老老实实 merge——慢一点不丢人。

##### submodule：仓库里套仓库

有时一个项目要引用另一个项目的特定版本，Git 的方案叫 submodule（子模块）：主仓库里只记录"引用哪个仓库的哪个提交"。别人 clone 之后还要执行一次初始化（通常是 git submodule update --init --recursive，以项目 README 说明为准）才能把子模块内容拉下来。

给新手的建议：能用包管理器解决依赖，就别用 submodule——它是公认的难点，团队里总有人忘了初始化，然后天天报错。你只需要知道它存在，遇到"submodule 未初始化"的报错时不慌，就够了。

##### 两个能救命的冷知识

reflog：只要提交过，几乎就不会真丢。分支指针的每次移动都有记录，reset 错了、分支删了，都能从 git reflog 里找到"案发前"的编号再捞回来。真遇到"我搞没了"的时刻，先跑这条命令，再想办法。

bisect：历史很长、不知道哪次提交引入了 bug 时，git bisect 帮你二分查找——它反复让你验证"这个版本正常吗"，把范围一步步砍半，通常十几步就能锁定出问题的提交。用法细节以官方文档为准；记住有这个工具，比记住用法更重要。

#### 打标签与发版本：给仓库搭一个"货架"

写到某个阶段，你会想把"这一版"单独钉起来——这就是标签（tag）和发布（Release）干的事。标签是钉在某个提交上的书签，常见做法是给正式版本打上 v 开头的编号；Release 是在标签基础上打包发布的页面，可以把编译好的文件挂上去供人下载。命令与写法以官方文档为准。

版本编号有个社区里广为流传的习惯：三段数字，从左到右分别对应"大改、加东西、修毛病"——最左边那位变了，通常意味着可能有不兼容的大变化；只有最后一位变了，多半是修 bug，升级风险小。这只是普遍习惯而非强制标准，具体以各项目自己的说明为准。

对你"用软件"的那一面也有价值：以后去开源项目找安装包，直奔 Releases 页，看一眼版本号和更新说明，就能判断这个版本要不要马上更。顺带一提，更新说明都是短句和要点，比新闻好读，也是顺路学英文的好材料。

#### 常见报错与故障速查

下面这些报错，你迟早会遇到，对照着查就行。每条给"原因"和"怎么办"；情况特殊时以官方文档为准。

<strong>"command not found: git"</strong>——命令没装或没配置路径。装完 Git 要重开终端窗口再试；Windows 用户用 Git Bash 或新开的终端，别在装完不重开的老窗口里折腾。

<strong>"fatal: not a git repository"</strong>——你所在的文件夹不是仓库。先看看自己 cd 到哪了；仓库目录里有一个 .git 隐藏文件夹，没有就 git init。

<strong>"nothing to commit, working tree clean"</strong>——不算报错，是 Git 在说"没什么可提交的"。多半是忘了保存文件，或者忘了 add。

<strong>屏幕突然停住，敲什么都没反应</strong>——你进到了 git 的分页器里。按 q 退出就好。这是每个 Git 新手的第一次"惊魂时刻"，见过一次就不怕了。

<strong>"You have unmerged files"</strong>——上一次合并的冲突没解决完。把冲突文件改完、git add，再按提示继续完成合并。

<strong>"refusing to merge unrelated histories"</strong>——本地和云端被判定为"两个不相干的来历"，常见于先在本地 git init，又在网页上建了带 README 的同名仓库。确认两边确实该是一家的前提下，在合并命令后加 --allow-unrelated-histories 允许合并，随后处理可能出现的冲突。

<strong>"Your branch has diverged"</strong>——本地和云端各自有了新提交，分叉了。标准解法：git pull 合回来（有冲突就解决冲突），再 push。

<strong>"Everything up-to-date" 但网页没变化</strong>——十有八九是你 push 到了别的分支。git branch 看看自己现在站在哪条分支上。

<strong>commit 时打开了一个奇怪的全屏编辑器</strong>——那是默认编辑器 vim 在等你。按 i 进入输入，写完按 Esc，再输入 :wq 回车保存退出；也可以按官方文档把默认编辑器改成你顺手的那个。

<strong>"fatal: pathspec 'xxx' did not match any files"</strong>——文件名打错了，或者文件还没创建。先 ls 看看目录里真实的文件名，再 add。

<strong>"warning: LF will be replaced by CRLF"</strong>——不同系统换行符差异的提示，多数情况直接无视；介意的话按官方文档配置换行符处理规则。

<strong>中文文件名显示成一串转义码</strong>——Git 默认转义显示非 ASCII 文件名。用 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git config --global core.quotepath false</code> 让它正常显示中文——这是中文用户最值得做的三项配置之一（另外两项：user.name 和 user.email）。

<strong>"Permission denied (publickey)"</strong>——SSH 密钥没配对。新手最快的绕行方案是改用 HTTPS 地址；想用 SSH 就按官方教程重新配一遍密钥。

<strong>"fatal: remote origin already exists"</strong>——origin 这个名字已经被占了。用 git remote set-url origin 新地址 来改，不用删了重加。

<strong>push 长时间卡住不动</strong>——网络问题居多，对策翻回"国内访问"那个盒子；仓库塞了大文件也会推不动，该瘦身的不是网速，是仓库。

<strong>"detached HEAD" 提示</strong>——你检出了某个历史提交而不是分支。想在这里改东西，先 git switch -c 开一条新分支再动手；不想要就切回原来的分支。原理以官方文档为准。

<strong>"error: failed to push some refs"</strong>——push 被拒的通用包装，正文里通常写着具体原因：多数是云端有新提交，先 pull 再 push；偶尔是分支保护拦住了你，那就老老实实走 PR。

<strong>clone 下来的项目跑不起来</strong>——先别怀疑 Git，它只负责把文件搬给你，不负责运行环境。翻 README 的依赖说明，把缺的东西装上；再不行，去 Issue 区搜搜有没有人和你一样。

#### GitHub 日常安全五条

安全提醒盒子讲的是"出事之后怎么办"，这里补五条日常习惯，把事堵在前面：

- <strong>别让私人邮箱裸奔</strong>：提交历史里的邮箱是公开可见的。GitHub 设置里可以开启邮箱隐私（Keep my email addresses private），用提供的 noreply 地址做提交邮箱，具体以官方设置为准。
- <strong>Token 定期换</strong>：Personal Access Token 设有效期、给最小权限，过期就换新的，别留一把"永久全权钥匙"。
- <strong>陌生的 Action 别乱引入</strong>：第三方的自动化脚本，先看清楚它跑什么，再往自己仓库里加。
- <strong>陌生仓库的代码先看再跑</strong>：下载别人仓库里的脚本直接执行，和打开陌生邮件附件是同一种危险。
- <strong>收到异常登录提醒别拖</strong>：立刻改密码、检查两步验证、翻一遍账号的设备授权列表，路径以官方帮助为准。

#### 八、给新手的几点建议

- <strong>提交说明要写清楚</strong>：别写"update"这种废话说明。好的commit message写"修复用户登录后跳转错误页面的问题"，写清「为什么改」比写「改了什么」更值钱——半年后回看，能省大量考古时间。
- <strong>勤提交，小步快跑</strong>：每完成一个小功能就commit一次，而不是写了一整天才提交一次。这样出问题更容易定位。
- <strong>用分支开发，别直接改主分支</strong>：哪怕是个人项目，养成开分支的习惯，未来团队协作时就不会手忙脚乱。
- <strong>善用.gitignore</strong>：这个文件用来告诉Git哪些文件不要纳入版本管理（比如密码配置、编译产物、依赖文件夹），避免把垃圾文件传上去。
- <strong>多看优秀开源项目</strong>：逛逛GitHub Trending，看看高星项目的代码结构、README写法、协作流程，是提升最快的免费方式。
- <strong>申请GitHub学生包</strong>：学生认证后可免费获得大量付费工具和服务的额度（Copilot、域名、云服务等），价值上千美元。
- <strong>用AI也要自己审</strong>：智能体可以帮你写PR描述、帮你找改动点，但合并前逐文件读一遍diff的责任在你——它看着很顺的代码，跑起来未必对。
- <strong>认证方式心里有数</strong>：GitHub早已不允许用账号密码push代码，现在要么配SSH key，要么用Personal Access Token。Token本身就是最常被误提交的那类密钥——设好有效期和最小权限，别给永久全权的。

这八条建议里，被违反最多的是"勤提交"和"开分支"那两条——攒一个大提交、直接在主分支上改，短期都"没出事"，直到某天你改坏了找不到原因，或者两个人的改动搅成一团。习惯的成本在养成那天就付清了，收益则在你每次出事时兑现。另外，.gitignore 别自己从零编——GitHub 上有官方维护的各语言通用模板仓库，搜 github/gitignore 就能找到，抄一份改改就能用。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>安全提醒

{class="list-disc pl-6 mt-1 space-y-1"}
- 千万不要把密码、API密钥、token、数据库连接串、.env文件等敏感信息提交到GitHub，尤其是公开仓库——一旦泄露，会被爬虫秒抓，后果严重。这类文件一律提前写进.gitignore。
- 不小心提交了敏感信息，<strong>第一件事是在平台上撤销并轮换</strong>这把密钥——删提交记录不算补救，历史里还留着。然后再用<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git filter-repo</code>清理历史（官方已弃用 filter-branch）。
- 私有仓库也不是绝对安全，敏感信息最好用环境变量管理，不进代码仓库。
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>国内访问GitHub的注意事项

{class="mt-1"}
GitHub在国内访问有时不稳定，可能出现打不开、克隆慢的情况。可以尝试：① 使用国内镜像站加速克隆（镜像更替频繁，如 ghfast.top、gh-proxy.com，用前先确认在线）；② 配置Hosts或使用代理；③ 如果主要面向国内协作，也可以考虑国产替代品<strong>Gitee（码云）</strong>，功能类似且访问速度快。很多团队会同时在GitHub和Gitee上托管，兼顾国际化和国内速度。
:::

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>进阶玩法：用GitHub Pages搭建免费个人博客

{class="mt-1"}
GitHub Pages允许你免费托管一个静态网站，配合Jekyll、Hexo、Hugo等静态站点生成器，可以轻松搭建个人博客。写完Markdown文章push到仓库，博客自动更新，还自带HTTPS和自定义域名。无数技术博主的博客都是这么搭的，零成本、无广告、版本可控。
:::

顺着 Pages 这个进阶玩法多说一句：把仓库取名为"你的用户名.github.io"，它就会成为你的个人主页地址——简历、作品集、博客都能挂在同一个地方，规则细节以官方文档为准。不少求职者的简历链接，就是这样一个干净清爽的个人主页。

#### 新手最常问的十个问题

<strong>问：我完全不写代码，注册 GitHub 图什么？</strong>

答：图三件事。一，很多开源软件的反馈入口就在 GitHub，会用 Issue 你就能有效报 bug，比到处喊"这软件坏了"管用；二，私有仓库可以当带完整历史的笔记库；三，看懂"提交、分支、合并"这套思维，你再看任何协作类工具（在线文档、设计稿、项目管理软件）都会顺眼很多。当然，暂时用不上就先不注册，手机照样好好用。

<strong>问：git push 总是失败，提示 rejected，是不是我账号被盗了？</strong>

答：不是被盗，是云端有你本地没有的新提交——比如你或同事在网页上改过东西。先 git pull 合并，再 push，一般就过了。千万别因为着急就加 --force 强推，那会把云端历史强行覆盖成你的版本，在团队里属于事故级操作。

<strong>问：commit 完才发现少改了一个文件，说明还写错了，能救吗？</strong>

答：能，前提是这条提交还没 push。把新改动 add 进来，然后 git commit --amend，它会并入最后一次提交，说明也能顺手改。已经推送到公共分支的就别 amend 了，另开一条提交补救更安全——改写别人可能已经拉走的历史，麻烦无穷大。

<strong>问：手滑把分支删了，里面像是几个月的工作，是不是全没了？</strong>

答：先深呼吸。只要那些工作提交过，本地用 git reflog 大概率能找到线索捞回来；从未提交过的改动，Git 才真的无能为力——这也是"勤提交小步快跑"的技术根源。GitHub 网页上删掉的分支，有时也能通过恢复机制找回，细节以官方文档为准。别在慌乱中继续乱敲命令，先查再动。

<strong>问：免费账号是不是限制很多？私有仓库要交钱吗？</strong>

答：个人学习完全够用。免费账号支持无限私有仓库（本章第四节创建仓库时提过），协作、Actions、Pages 的基础能力也在免费范围内；具体额度与限制以官方定价页为准。真到需要付费功能的阶段，你早就不是新手了。

<strong>问：GitHub 打不开、clone 慢得离谱，是不是该放弃了？</strong>

答：别。本章前面"国内访问"的盒子给了三个方向：镜像加速、配置代理或 Hosts、改用 Gitee 承托国内协作。再加一条笨但有效的：挑网络空闲时段操作，深夜通常顺很多。反复用同一姿势硬试，不如换思路。

<strong>问：Star 了一百多个项目全在吃灰，有整理的办法吗？</strong>

答：GitHub 支持把 Star 归类到自定义清单（Lists，以界面为准），按用途分几类：教程类、工具类、灵感类。另外建议换个习惯：点 Star 之前先问自己"未来一个月我会打开它吗"，多数时候这个提问能帮你过滤掉大半冲动收藏。

<strong>问：AI 都会写代码了，我还要学 Git 和 GitHub 吗？</strong>

答：更要学。AI 生成的代码需要有人审查、试跑、出了问题回滚，这些动作全都建立在版本控制之上；而且不少 AI 编程工具的工作方式就是"读仓库、改文件、发 PR"——你不懂 Git，连它在干什么都看不明白，出了错也不知道回到哪一步。工具越强，驾驭工具的基本功越值钱。

<strong>问：我们小组全是新手，能不能图省事，都直接在 main 上干活？</strong>

答：两三个人的小项目、大家都清楚风险，短期可以。但只要满足"多人、长期、要发布"任意两条，就请上分支和 PR：人手一片草稿区，主分支永远保持"随时可交付"的状态。多人合写的文档仓库同理——谁也不想在交稿前夜发现 chapter3 被覆盖了。

<strong>问：README、Issue、PR 描述都要写不少字，现实中真有人这么认真吗？</strong>

答：偷懒的人当然有，但你可以去任意一个高星项目翻翻它的 Issue 和 PR——写得清楚的是多数，因为写得清楚的人协作效率真的高。这些文字不是仪式感，是成本最低的沟通介质：你少打的两百个字，迟早会变成别人（包括未来的你）多问的十个问题。

<strong>问：HTTPS 和 SSH，我到底该用哪个？</strong>

答：新手用 HTTPS，配 Token 或浏览器授权就能跑，省心；SSH 配一次密钥之后免输验证，但要自己折腾密钥的生成和添加。两者切换只是换仓库地址的事——先 HTTPS 用起来，等哪天嫌输验证烦了再研究 SSH，一点不亏。

<strong>问：Fork 和 Clone 只差一个字母，到底差在哪？</strong>

答：Fork 发生在云端——把别人的仓库复制到你账号下；Clone 发生在本地——把仓库复制到你电脑上。给别人项目做贡献，顺序是先 Fork（拿到你能改的副本）再 Clone（把副本拉到本地）；同步自己的仓库，直接 Clone 就行。一个在网页上，一个在终端里，记住场景就不会混。

<strong>问：仓库建错了、不要了，直接删掉行吗？</strong>

答：行，仓库 Settings 底部的危险区（Danger Zone）里有删除入口。但删除后的恢复空间有限，动手前确认两件事：里面没有别处没有的劳动成果（有就先备份一份），以及没有别人还在用。公开仓库删了，收藏它的人手里的链接就成了死链——能改作别的用途就别急着删。

<strong>问：GitHub 的 AI 功能要花钱吗？学生有优惠吗？</strong>

答：AI 相关功能分免费档和付费档，学生包里有相应额度（本章第八节提过学生包），具体以官方定价页为准。多一句提醒：用 AI 生成内容时，遵守项目和平台的披露要求，别把机器产物当纯手工作品署名——各平台规则不一，以官方政策为准。

<strong>问：界面全是英文，我这点水平能玩得转吗？</strong>

答：能。日常高频按钮就那十来个：Code、Issues、Pull requests、Star、Fork、Commit，用两天就条件反射了。官方文档有中文翻译，社区中文教程也极多，浏览器自带的整页翻译对付长文档绰绰有余。语言是纸老虎，概念才是真门槛——而概念，这一章已经帮你拆完了。

<strong>问：要不要把 GitHub 链接写进简历？我不是科班的。</strong>

答：要，挑着写。放两三个最能代表你的仓库，README 整齐、内容真实，比放一串空壳仓库强得多。非科班反而有故事可讲——"我用 GitHub 管理了我的备考笔记"，面试官看的是你用工具解决问题的意识，不是科班出身。

<strong>问：一天刷多少 commit 才算合格？</strong>

答：没有标准答案，也千万别拿这个当 KPI。绿格子反映的是提交频率，不反映质量；一周认真提交两三次，远好于每天一条"update"凑数。格子图是结果，不是目标——你专心把东西做完，格子自己会绿起来。

#### 新手常见误区清单

- <strong>误区：GitHub 就是个网盘。</strong>网盘只保存"最新一版"，历史说丢就丢；GitHub 的核心资产是全部历史与协作记录。用网盘的思路用它（只 push 不写说明、一年 commit 一次），等于把跑车当买菜车开。
- <strong>误区：.gitignore 是出了事再加的。</strong>它要在第一次提交前就写好：已经提交过的文件，事后加进 ignore 并不会自动移出仓库（需要再用 git rm --cached 之类的方式处理，用法以官方文档为准）。密钥文件尤其如此——文件进了历史，删掉文件本身救不回来，本章安全提醒盒子讲过补救顺序。
- <strong>误区：提交攒得越大越"高效"。</strong>攒一天改动的巨型提交，出问题时没法定位是哪步引入的；"一次提交只做一件事"的小步提交，回滚和排查都是精准打击。
- <strong>误区：--force 是解决问题的快捷键。</strong>它只在一种场景合理：你明确知道自己在改写"只属于你一个人"的分支。在公共分支上用它，等于把同事的提交扔进碎纸机。
- <strong>误区：放进私有仓库的密钥就安全了。</strong>私有只是降低概率：仓库泄露、协作者电脑中招、将来某天误改公开，路子不止一条。敏感信息用环境变量注入，别进代码。
- <strong>误区：PR 被关闭说明我很菜。</strong>成熟开源项目关闭 PR 是日常：方向不符、已有重复实现、维护者没精力审，理由五花八门。被关了就礼貌问一句原因，下一次会顺很多——这不是安慰，是流程。
- <strong>误区：README 是写给别人的。</strong>三个月后忘了自己当初怎么把项目跑起来的，正是你自己。README 的第一读者，永远是未来的你。

#### 给不同人群的 GitHub 使用建议

##### 学生：把课程作业变成作品集

从这学期开始，每门课的大作业都建一个仓库：代码、报告、实验数据分开存放，README 写清"这是什么课的什么作业、怎么运行"。毕业时你手里不止一张成绩单，而是几年积累的、带时间戳的可信作品集——它比简历上任何一句"熟练掌握"都硬。学生包（本章第八节提过）记得趁在校时认证，毕业后就没机会了。

##### 职场人：让文档和方案也有"版本历史"

写方案、整理会议纪要、维护团队知识库，这些非代码工作同样可以用私有仓库管理：Markdown 写作，每次修改一个 commit，谁改过什么清清楚楚。配合 Issues 当任务清单、Projects 当看板，小团队的协作工具钱都省了。简历上放一个 GitHub 链接，对非技术岗位同样是加分项——它证明你懂得现代协作方式。

进阶一步：方案评审也能借 PR 的思路——草案开分支、同事行内评论、定稿后合并。工具可以换成任何协作文档，但"改动先评审再进正本"这个节奏，值得带到每一份重要文件上。

##### 写作者与内容创作者：草稿的保险箱

长期写作的人最痛的是"改稿历史丢失"。用私有仓库存稿子，每改一稿提交一次，任何一版随时可回，比"新建文件夹(3)"科学得多。愿意公开的部分发出来，配合 GitHub Pages 做成站点，读者反馈直接走 Issue——评论区在你自己手里，不怕平台规则变来变去。

##### 给爸妈：先别碰，这是句实话

说句可能让你意外的建议：如果你是想替爸妈找个"更好用的网盘"，GitHub 不是答案。它不适合存照片视频（大二进制文件是短板），界面是英文，协作概念也陡。爸妈的备份需求，交给成熟的网盘更合适。GitHub 适合的是"需要留历史、需要多人改文本"的场景——如果家里有写回忆录、整理族谱这类事，倒值得你帮他们搭一个私有仓库：你负责操作，他们负责口述。

##### 小团队与工作室：Issue 就是免费的工单系统

几个人的小团队未必需要上一套专业项目管理软件：私有仓库加 Issues 当工单、Projects 当看板、每周一次 PR 式的成果合并，协作的骨架就搭起来了。真正的门槛不在工具，在于团队约定"改动走 PR、说明写清楚"并且坚持执行——工具是轻的，习惯才是重的。

#### 上手路线图：从第一天到第一个月

学完概念容易，落地容易忘。给你一张按时间排的路线图——走到哪算哪，不赶进度。

- <strong>第一天</strong>：注册账号、开两步验证、建 hello-github 仓库、在网页上改一次 README（本章动手项的前几步）。
- <strong>第一周</strong>：装 Git、配好身份，把练习仓库完整走一遍"改—add—commit—push"循环；把报错速查那一节过一遍，最好现在就撞上一两条报错——现在踩比将来踩便宜。
- <strong>第一个月</strong>：把某门课的笔记或某个真实项目搬进私有仓库，每周固定提交；挑一个打了"good first issue"标签的任务读一读，先不动手，看看别人怎么讨论问题。
- <strong>三个月后</strong>：发你的第一个 PR，哪怕只改一个错别字；把个人主页收拾成名片——头像、简介、置顶仓库。
- <strong>半年后</strong>：考虑维护一个自己的小项目——哪怕只是每周更新的读书笔记仓库。被人用、被人提 Issue，比读十篇教程都长本事。

每个阶段的动作都不难，难的是"每周固定"。工具学不会的人少，习惯养不成的人多——把提交变成像记账一样的日常动作，剩下的都会水到渠成。

::: div .quote-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-quote-left mr-2"></i>一句话记牢

{class="mt-1"}
仓库是历史的容器：你现在写下的每一句提交说明，都是在给未来的自己留路标。
:::

#### 九、为什么每个人都该了解GitHub

GitHub早已不只是"程序员的工具"，它更像是一个<strong>数字时代的工作方式</strong>：版本管理让一切可追溯，协作机制让团队高效运转，开源精神让知识自由流动。哪怕你不写代码，理解"提交、分支、合并"这些概念，也能帮你更好地管理任何需要"反复修改+多人协作"的内容——从论文到文档，从笔记到方案。

对计算机系的学生来说，GitHub更是必备技能：它是你的作品集、协作平台、学习资源库，也是未来求职时最有说服力的"简历"。早点注册账号，把自己的课程作业、小项目传上去，慢慢积累，几年后你会拥有一份让面试官眼前一亮的技术履历。

如果你读到这里仍然觉得"GitHub 离我很远"，换个角度想：这一章真正想教你的不是一个网站，而是一套工作节奏——任何需要"反复修改、多人参与、留下痕迹"的事情，都适用"小步提交、写清说明、改动先上草稿、合并前过目"这套流程。学一次，搬到论文、方案、书稿上，全都顺手。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>来动手：完成你的GitHub初体验

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 注册一个GitHub账号，完善个人资料（头像、简介、感兴趣的技术领域）。
2. 创建一个名为<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">hello-github</code>的公开仓库，勾选"Add a README file"。
3. 进入仓库，点击README.md的编辑按钮（铅笔图标），用Markdown写一段自我介绍，提交更改。
4. 在GitHub搜索栏搜索一个你感兴趣的关键词（比如<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python-tutorial</code>），Star两个你喜欢的项目。
5. （进阶）在电脑上安装Git，把仓库Clone到本地，修改README后push回云端，完成一次完整的"本地→云端"工作流。
:::
