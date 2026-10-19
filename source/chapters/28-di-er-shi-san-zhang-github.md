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

#### 一、GitHub到底是什么？

简单来说，GitHub是一个基于Git的<strong>代码托管与协作平台</strong>。它于2008年上线，2018年被微软收购，至今仍是全球最大的开源代码托管平台，托管着数亿个仓库，覆盖几乎所有主流编程语言。

如果用一个类比来理解：<strong>Git是你电脑上的日记本，GitHub就是一个公开的博客平台</strong>——你可以发布自己的作品，关注别人的项目，参与讨论和协作。它不仅是"程序员的后台仓库"，更像是全球开发者共建的一座"技术城市"——项目在这里诞生、迭代、被讨论、被复用。

对普通人来说，GitHub也并非遥不可及。很多非程序员会用它来托管笔记、电子书、个人博客，甚至用来备份配置文件。只要你有一点点"想把自己的东西整理好并分享出去"的需求，GitHub都值得你了解。

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

#### 三、GitHub的核心概念与功能

##### 📁 基础概念

在动手之前，先认识几个高频词汇，否则看GitHub的界面会一头雾水：

- <strong>仓库（Repository，简称Repo）</strong>：一个项目对应一个仓库，里面存放着这个项目的所有代码文件、历史版本和文档。可以理解为一个"项目文件夹"。
- <strong>提交（Commit）</strong>：对代码的一次修改记录。每次Commit都附带说明信息，记录"这次改了什么、为什么改"。这是Git/GitHub能"时光倒流"的基础。
- <strong>分支（Branch）</strong>：从主线上分出来的独立开发线。比如你想加个新功能，可以开一个分支单独开发，开发完再合并回主线，不影响其他人。
- <strong>克隆（Clone）</strong>：把云端仓库完整复制一份到本地电脑，之后就可以在本地修改代码。
- <strong>推送（Push）/拉取（Pull）</strong>：Push是把本地代码上传到GitHub，Pull是从GitHub下载最新代码到本地。这是团队协作时同步代码的两个核心动作。
- <strong>合并请求（Pull Request，简称PR）</strong>：当你在一个分支上改完代码，想合并到主分支时，发起一个PR，让团队成员审查代码后再合并。这是GitHub协作的核心机制。
- <strong>议题（Issue）</strong>：用来记录bug、功能需求、讨论话题。每个Issue像一个讨论帖，可以指派负责人、打标签。
- <strong>Fork</strong>：把别人的仓库复制一份到自己账号下，你可以在自己的副本上随意修改，不影响原仓库。改好后可以给原作者发PR，请求合并你的改进。

##### 🛠️ 核心功能

GitHub提供的不只是代码存储，还包括：

- <strong>版本控制</strong>：记录每次代码更改的历史，改坏代码随时回到上一个正常版本。
- <strong>团队协作</strong>：支持多用户对同一项目的并行开发，多人同时开发不会覆盖、不会冲突。
- <strong>问题跟踪</strong>：用Issue记录bug和功能请求，方便团队跟进。
- <strong>项目管理</strong>：集成了待办事项、项目看板（Projects）等管理工具，相当于内置了一个轻量级Trello。
- <strong>自动化</strong>：通过<strong>GitHub Actions</strong>实现代码提交后自动编译、测试、打包、部署，是现代"CI/CD（持续集成/持续部署）"的核心工具。
- <strong>文档管理</strong>：README介绍项目，Wiki存放详细架构和开发规范，Pages甚至可以直接托管静态网站。
- <strong>代码托管与展示</strong>：每个仓库都有漂亮的网页展示，支持语法高亮，是你技术作品的"门面"。
- <strong>开源社区</strong>：你可以Star（收藏）喜欢的项目、Watch（关注）项目动态、Follow（关注）开发者，参与全球开源协作。

#### 四、注册与上手：五分钟创建你的第一个仓库

##### 📝 注册账号

1. 访问<a href="https://github.com" class="text-primary hover:underline" target="_blank" rel="noopener">github.com</a>，点击"Sign up"。
2. 填写邮箱、设置密码和用户名（用户名会出现在你的个人主页地址里，建议用英文，比如<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">github.com/yourname</code>）。
3. 完成邮箱验证和人机验证。
4. 选择免费方案（Free）即可，对个人用户完全够用。

##### 📁 创建第一个仓库

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

#### 五、基本工作流：从本地到云端

理解GitHub的工作流，核心是记住这个循环：<strong>本地修改 → 暂存 → 提交 → 推送 → 云端更新</strong>。下面用大白话解释每一步：

1. <strong>修改文件</strong>：在本地电脑上用编辑器写代码或改文档。
2. <strong>git add</strong>：把修改的文件加入"暂存区"，相当于告诉Git"这些改动我准备记录下来"。
3. <strong>git commit</strong>：把暂存区的改动正式记录成一个"提交"，附上一句说明，比如"修复登录bug"。这一步只在本地完成。
4. <strong>git push</strong>：把本地的提交上传到GitHub云端，这样别人就能看到了。
5. <strong>git pull</strong>：在开始工作前，先从云端拉取最新代码，确保本地和团队其他人保持同步。

对新手来说，记住这个口诀：<strong>"先pull后改，改完add，commit带说明，最后push上去"</strong>。养成这个习惯，团队协作就不会乱。

#### 六、团队协作流程：Pull Request是怎么工作的

GitHub最强大的地方在于它的协作机制。一个典型的团队协作流程是这样的：

1. <strong>开分支</strong>：从主分支（通常叫main或master）开一个新分支，比如<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">feature/login</code>，在这个分支上开发新功能。
2. <strong>开发并提交</strong>：在新分支上写代码，多次commit记录进度。
3. <strong>推送到GitHub</strong>：把分支push到云端仓库。
4. <strong>发起Pull Request</strong>：在GitHub网页上发起PR，请求把你的分支合并到主分支。写清楚这个PR做了什么改动、为什么改。
5. <strong>代码审查（Code Review）</strong>：团队成员查看你的代码，提出意见或建议修改。你可以根据反馈继续commit，PR会自动更新。
6. <strong>合并</strong>：审查通过后，点击"Merge"把代码合并到主分支。你的贡献就正式进入项目了！

这套流程保证了<strong>任何代码进入主分支前都经过审查</strong>，大大降低了出错概率。开源项目也是用这套机制接受全世界陌生人的贡献——你完全可以在某个知名开源项目上提交PR，被采纳后你就是这个项目的贡献者了。

#### 七、GitHub的典型应用场景

##### 🎓 学生参加比赛与课程项目

计算机系学生参加ACM、黑客松、毕业设计，几乎都离不开GitHub。它既能作为团队协作平台，又能作为作品展示窗口——比赛评委可以直接看你的仓库，了解代码质量和协作过程。很多公司招聘时也会要求附上GitHub主页，作为技术能力的证明。

##### 📚 个人知识库与笔记托管

非程序员也能用GitHub。很多人用它托管学习笔记、技术博客（配合GitHub Pages可以免费建站）、电子书。Markdown格式写作 + Git版本管理 + 云端备份，三合一。

##### 🌐 参与开源项目

GitHub是全球开源运动的核心阵地。你可以Fork喜欢的项目，修改后发PR回馈社区；也可以单纯Star收藏好项目，跟踪更新。参与开源是提升技术、积累声誉的绝佳途径。

##### 🤖 自动化部署与CI/CD

借助GitHub Actions，可以实现"代码一push，自动测试+自动部署到服务器"的全自动流程。很多个人博客、文档站点都是这么搭建的，写完文章push一下，网站就自动更新了。

##### 💾 代码备份与多设备同步

把代码仓库当作云盘用，换电脑、多设备办公时，git pull一下就能拿到最新代码，再也不用U盘拷来拷去。

#### 八、给新手的几点建议

- <strong>提交说明要写清楚</strong>：别写"update"这种废话说明。好的commit message写"修复用户登录后跳转错误页面的问题"，半年后回看也知道当时干了啥。
- <strong>勤提交，小步快跑</strong>：每完成一个小功能就commit一次，而不是写了一整天才提交一次。这样出问题更容易定位。
- <strong>用分支开发，别直接改主分支</strong>：哪怕是个人项目，养成开分支的习惯，未来团队协作时就不会手忙脚乱。
- <strong>善用.gitignore</strong>：这个文件用来告诉Git哪些文件不要纳入版本管理（比如密码配置、编译产物、依赖文件夹），避免把垃圾文件传上去。
- <strong>多看优秀开源项目</strong>：逛逛GitHub Trending，看看高星项目的代码结构、README写法、协作流程，是提升最快的免费方式。
- <strong>申请GitHub学生包</strong>：学生认证后可免费获得大量付费工具和服务的额度（Copilot、域名、云服务等），价值上千美元。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>安全提醒

{class="list-disc pl-6 mt-1 space-y-1"}
- 千万不要把密码、API密钥、数据库连接串等敏感信息提交到GitHub，尤其是公开仓库——一旦泄露，会被爬虫秒抓，后果严重。
- 不小心提交了敏感信息，光删除文件不够（历史记录里还有），要用<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git filter-branch</code>或专业工具清理历史，并立即更换泄露的密钥。
- 私有仓库也不是绝对安全，敏感信息最好用环境变量管理，不进代码仓库。
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>国内访问GitHub的注意事项

{class="mt-1"}
GitHub在国内访问有时不稳定，可能出现打不开、克隆慢的情况。可以尝试：① 使用国内镜像站（如GitClone、ghproxy）加速克隆；② 配置Hosts或使用代理；③ 如果主要面向国内协作，也可以考虑国产替代品<strong>Gitee（码云）</strong>，功能类似且访问速度快。很多团队会同时在GitHub和Gitee上托管，兼顾国际化和国内速度。
:::

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>进阶玩法：用GitHub Pages搭建免费个人博客

{class="mt-1"}
GitHub Pages允许你免费托管一个静态网站，配合Jekyll、Hexo、Hugo等静态站点生成器，可以轻松搭建个人博客。写完Markdown文章push到仓库，博客自动更新，还自带HTTPS和自定义域名。无数技术博主的博客都是这么搭的，零成本、无广告、版本可控。
:::

#### 九、总结：为什么每个人都该了解GitHub

GitHub早已不只是"程序员的工具"，它更像是一个<strong>数字时代的工作方式</strong>：版本管理让一切可追溯，协作机制让团队高效运转，开源精神让知识自由流动。哪怕你不写代码，理解"提交、分支、合并"这些概念，也能帮你更好地管理任何需要"反复修改+多人协作"的内容——从论文到文档，从笔记到方案。

对计算机系的学生来说，GitHub更是必备技能：它是你的作品集、协作平台、学习资源库，也是未来求职时最有说服力的"简历"。早点注册账号，把自己的课程作业、小项目传上去，慢慢积累，几年后你会拥有一份让面试官眼前一亮的技术履历。

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
