---
id: di-er-shi-san-zhang-github
part: chao-yue-pian
nav: 附：GitHub入門指南
toc: sub
kind: chapter
---

### 第二十三章附：GitHub入門指南——從代碼託管到協作平臺

{class="chapter-intro mb-4"}
上章吾輩講了"編程之思"，而真要將編程之思落地、與他人共做項目，即繞不開一名——GitHub。無論君為計算機系學生要參賽、欲存己之代碼作品，抑或單純欲觀全球開發者折騰何物，GitHub皆君必須認識之平臺。此節吾輩自最基礎之概念講起，助君建一清晰之認知。

#### 一、GitHub究竟爲何物？

簡單言之，GitHub乃一基於Git之<strong>代碼託管與協作平臺</strong>。其於2008年上線，2018年爲微軟所收購，至今仍為全球最大之開源代碼託管平臺，託管着數億個倉庫，覆蓋幾乎所有主流編程語言。

若以一類比理解之：<strong>Git乃君電腦上之日記本，GitHub則一公開之博客平臺</strong>——君可發佈己之作品，關注他人之項目，參與討論與協作。其不僅為"程序員之後臺倉庫"，更似全球開發者共建之一座"技術城"——項目於此誕生、迭代、被討論、被複用。

於普通人而言，GitHub亦非遙不可及。多數非程序員會用其託管筆記、電子書、個人博客，甚至用以備份配置文件。只要君有一絲"欲將己之事物整理好並分享出去"之需，GitHub皆值得君瞭解。

#### 二、Git與GitHub之別（關鍵概念！）

多人初觸時常混此兩詞，此處爲君梳理清楚：

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">對比項</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Git</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GitHub</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">本質</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">版本控制工具（軟件）</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">代碼託管平臺（網站）</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">運行位置</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">本地電腦上</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">雲端（瀏覽器訪問）</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">核心職責</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">記錄文件之每次變更（何以改、誰改、何時改）</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">將Git倉庫放至雲端，方便存儲、展示、協作</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">為否需網絡</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不需，離線可用</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需聯網訪問</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">歸屬</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">開源軟件，由Linus Torvalds（Linux之父）創建</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">微軟旗下產品</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">同類競品</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SVN、Mercurial</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitLab、Gitee（碼雲）、Bitbucket</td>
                            </tr>
                        </tbody>
                    </table>
```

簡言之：<strong>Git管"何以記錄變更"，GitHub管"變更放於何處、何以協作"</strong>。Git乃工具，於本地運行；GitHub乃平臺，將Git倉庫放至雲端，方便協作與展示。君可只用Git不用GitHub（譬如自己寫代碼做版本管理），然用GitHub必用Git（因GitHub即基於Git）。

#### 三、GitHub之核心概念與功能

##### 📁 基礎概念

動手之前，先識數個高頻詞彙，否則觀GitHub之界面將一頭霧水：

- <strong>倉庫（Repository，簡稱Repo）</strong>：一個項目對應一個倉庫，內中存放此項目之所有代碼文件、歷史版本與文檔。可理解爲一"項目文件夾"。
- <strong>提交（Commit）</strong>：對代碼之一次修改記錄。每次Commit皆附說明信息，記"此次改了何、何故改"。此乃Git/GitHub能"時光倒流"之基礎。
- <strong>分支（Branch）</strong>：自主線上分出之獨立開發線。譬如君欲加一新功能，可開一分支單獨開發，開發畢再合併回主線，不影響他人。
- <strong>克隆（Clone）</strong>：將雲端倉庫完整複製一份至本地電腦，此後即可於本地修改代碼。
- <strong>推送（Push）/拉取（Pull）</strong>：Push乃將本地代碼上傳至GitHub，Pull乃自GitHub下載最新代碼至本地。此乃團隊協作時同步代碼之兩個核心動作。
- <strong>合併請求（Pull Request，簡稱PR）</strong>：當君於一分支上改完代碼，欲合併至主分支時，發起一PR，令團隊成員審查代碼後再合併。此乃GitHub協作之核心機制。
- <strong>議題（Issue）</strong>：用以記錄bug、功能需求、討論話題。每個Issue如一討論帖，可指派負責人、打標籤。
- <strong>Fork</strong>：將他人之倉庫複製一份至己之賬號下，君可於己之副本上隨意修改，不影響原倉庫。改好後可予原作者發PR，請求合併君之改進。

##### 🛠️ 核心功能

GitHub所供不止代碼存儲，尚包括：

- <strong>版本控制</strong>：記錄每次代碼更改之歷史，改壞代碼隨時回至上一正常版本。
- <strong>團隊協作</strong>：支持多用戶對同一項目之並行開發，多人同時開發不會覆蓋、不會衝突。
- <strong>問題跟蹤</strong>：用Issue記錄bug與功能請求，方便團隊跟進。
- <strong>項目管理</strong>：集成了待辦事項、項目看板（Projects）等管理工具，相當於內置一輕量級Trello。
- <strong>自動化</strong>：經<strong>GitHub Actions</strong>實現代碼提交後自動編譯、測試、打包、部署，乃現代"CI/CD（持續集成/持續部署）"之核心工具。
- <strong>文檔管理</strong>：README介紹項目，Wiki存放詳細架構與開發規範，Pages甚至可徑託管靜態網站。
- <strong>代碼託管與展示</strong>：每個倉庫皆有漂亮之網頁展示，支持語法高亮，乃君技術作品之"門面"。
- <strong>開源社區</strong>：君可Star（藏）喜歡之項目、Watch（關注）項目動態、Follow（關注）開發者，參與全球開源協作。

#### 四、註冊與上手：五分鐘創建君之第一個倉庫

##### 📝 註冊賬號

1. 訪問<a href="https://github.com" class="text-primary hover:underline" target="_blank" rel="noopener">github.com</a>，點擊"Sign up"。
2. 填寫郵箱、設置密碼與用戶名（用戶名將出現於君之個人主頁地址中，建議用英文，譬如<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">github.com/yourname</code>）。
3. 完成郵箱驗證與人機驗證。
4. 選免費方案（Free）即可，對個人用戶完全夠用。

##### 📁 創建第一個倉庫

1. 登錄後點擊右上角"+"號，選"New repository"。
2. 填寫倉庫名（Repository name），譬如<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">my-first-project</code>。
3. 寫一段簡短描述（Description），令他人知此倉庫爲何用。
4. 選公開（Public）或私有（Private）。公開倉庫所有人可見，私有唯己與協作者可見。免費賬號亦支持無限私有倉庫。
5. 勾選"Add a README file"——README乃項目之"說明書"，每個倉庫皆建議有之。
6. 點擊"Create repository"，君之第一個GitHub倉庫即誕生矣！

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>小知識：README爲何物

{class="mt-1"}
README.md乃一Markdown格式之文件，乃他人打開君倉庫時第一眼所見之內容。一個好之README通常含：項目簡介、安裝方法、使用示例、許可證、聯繫方式。寫好README乃程序員之基本素養，亦項目能否爲他人所用之第一道門檻。
:::

#### 五、基本工作流：自本地至雲端

理解GitHub之工作流，核心乃記此循環：<strong>本地修改 → 暫存 → 提交 → 推送 → 雲端更新</strong>。下以大白話釋每一步：

1. <strong>修改文件</strong>：於本地電腦上以編輯器寫代碼或改文檔。
2. <strong>git add</strong>：將修改之文件加入"暫存區"，相當於告Git"此等改動吾準備記錄下來"。
3. <strong>git commit</strong>：將暫存區之改動正式記成一"提交"，附上一句說明，譬如"修復登錄bug"。此步唯於本地完成。
4. <strong>git push</strong>：將本地之提交上傳至GitHub雲端，如此他人即能見之。
5. <strong>git pull</strong>：於始工作前，先自雲端拉取最新代碼，確保本地與團隊其他人保持同步。

於新手而言，記此口訣：<strong>"先pull後改，改完add，commit帶說明，最後push上去"</strong>。養此習慣，團隊協作即不會亂。

#### 六、團隊協作流程：Pull Request何以運作

GitHub最強之處於其協作機制。一個典型之團隊協作流程乃：

1. <strong>開分支</strong>：自主分支（通常叫main或master）開一新分支，譬如<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">feature/login</code>，於此分支上開發新功能。
2. <strong>開發並提交</strong>：於新分支上寫代碼，多次commit記錄進度。
3. <strong>推送至GitHub</strong>：將分支push至雲端倉庫。
4. <strong>發起Pull Request</strong>：於GitHub網頁上發起PR，請求將君之分支合併至主分支。寫清楚此PR做了何改動、何故改。
5. <strong>代碼審查（Code Review）</strong>：團隊成員查看君之代碼，提出意見或建議修改。君可根據反饋繼續commit，PR將自動更新。
6. <strong>合併</strong>：審查通過後，點擊"Merge"將代碼合併至主分支。君之貢獻即正式進入項目矣！

此套流程保證了<strong>任何代碼進入主分支前皆經審查</strong>，大大降低出錯概率。開源項目亦用此套機制接受全世界陌生人之貢獻——君完全可於某知名開源項目上提交PR，被採納後君即此項目之貢獻者矣。

#### 七、GitHub之典型應用場景

##### 🎓 學生參賽與課程項目

計算機系學生參加ACM、黑客松、畢業設計，幾乎皆離不開GitHub。其既能作團隊協作平臺，又能作作品展示窗口——比賽評委可徑觀君之倉庫，瞭解代碼質量與協作過程。多數公司招聘時亦會要求附上GitHub主頁，作爲技術能力之證明。

##### 📚 個人知識庫與筆記託管

非程序員亦能用GitHub。多人用其託管學習筆記、技術博客（配GitHub Pages可免費建站）、電子書。Markdown格式寫作 + Git版本管理 + 雲端備份，三合一。

##### 🌐 參與開源項目

GitHub乃全球開源運動之核心陣地。君可Fork喜歡之項目，修改後發PR回饋社區；亦可單純Star藏好項目，跟蹤更新。參與開源乃提升技術、積累聲譽之絕佳途徑。

##### 🤖 自動化部署與CI/CD

借GitHub Actions，可實現"代碼一push，自動測試+自動部署至服務器"之全自動流程。多數個人博客、文檔站點皆如此搭建，寫完文章push之，網站即自動更新矣。

##### 💾 代碼備份與多設備同步

將代碼倉庫當作雲盤用，換電腦、多設備辦公時，git pull之即能拿到最新代碼，再不用U盤拷來拷去。

#### 八、予新手之數點建議

- <strong>提交說明要寫清楚</strong>：勿寫"update"此等廢話說明。好之commit message寫"修復用戶登錄後跳轉錯誤頁面之問題"，半年後回觀亦知當時幹了啥。
- <strong>勤提交，小步快跑</strong>：每完成一個小功能即commit一次，而非寫了一整日方提交一次。如此出問題更易定位。
- <strong>用分支開發，勿徑改主分支</strong>：哪怕為個人項目，養成開分支之習慣，未來團隊協作時即不會手忙腳亂。
- <strong>善用.gitignore</strong>：此文件用以告Git哪些文件勿納入版本管理（譬如密碼配置、編譯產物、依賴文件夾），避免將垃圾文件傳上去。
- <strong>多觀優秀開源項目</strong>：逛逛GitHub Trending，觀高星項目之代碼結構、README寫法、協作流程，乃提升最快之免費方式。
- <strong>申請GitHub學生包</strong>：學生認證後可免費獲得大量付費工具與服務之額度（Copilot、域名、雲服務等），價值上千美元。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>安全提醒

{class="list-disc pl-6 mt-1 space-y-1"}
- 千萬勿將密碼、API密鑰、數據庫連接串等敏感信息提交至GitHub，尤以公開倉庫爲甚——一旦泄露，將爲爬蟲秒抓，後果嚴重。
- 不小心提交了敏感信息，光刪除文件不夠（歷史記錄裏尚有），需用<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git filter-branch</code>或專業工具清理歷史，並立即更換泄露之密鑰。
- 私有倉庫亦非絕對安全，敏感信息最好用環境變量管理，不進代碼倉庫。
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>國內訪問GitHub之注意事項

{class="mt-1"}
GitHub於國內訪問有時不穩，或出現打不開、克隆慢之情況。可嘗試：① 用國內鏡像站（如GitClone、ghproxy）加速克隆；② 配置Hosts或用代理；③ 若主要面向國內協作，亦可考慮國產替代品<strong>Gitee（碼雲）</strong>，功能類似且訪問速快。多數團隊會同時於GitHub與Gitee上託管，兼顧國際化與國內速度。
:::

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>進階玩法：以GitHub Pages搭免費個人博客

{class="mt-1"}
GitHub Pages允許君免費託管一靜態網站，配Jekyll、Hexo、Hugo等靜態站點生成器，可輕鬆搭建個人博客。寫畢Markdown文章push至倉庫，博客自動更新，且自帶HTTPS與自定義域名。無數技術博主之博客皆如此搭成，零成本、無廣告、版本可控。
:::

#### 九、總結：何故每人皆該瞭解GitHub

GitHub早已不只是"程序員之工具"，其更像是一<strong>數字時代之工作方式</strong>數字時代之工作方式

對計算機系之學生而言，GitHub更是必備技能：它是君之作品集、協作平臺、學習資源庫，亦乃未來求職時最有說服力之"簡歷"。早點註冊賬號，將君之課程作業、小項目傳上去，慢慢積累，數年後君將擁有一份令面試官眼前一亮之技術履歷。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>試爲之：完成君之GitHub初體驗

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 註冊一GitHub賬號，完善個人資料（頭像、簡介、感興趣之技術領域）。
2. 創建一名爲<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">hello-github</code>之公開倉庫，勾選"Add a README file"。
3. 進入倉庫，點擊README.md之編輯按鈕（鉛筆圖標），用Markdown寫一段自我介紹，提交更改。
4. 於GitHub搜索欄搜一君感興趣之關鍵詞（譬如<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python-tutorial</code>），Star兩個君喜歡之項目。
5. （進階）於電腦上安裝Git，將倉庫Clone至本地，修改README後push回雲端，完成一次完整之"本地→雲端"工作流。
:::
