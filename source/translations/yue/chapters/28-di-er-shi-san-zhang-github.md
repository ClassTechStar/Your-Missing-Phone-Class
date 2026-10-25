---
id: di-er-shi-san-zhang-github
part: chao-yue-pian
nav:  附：GitHub入門指南
toc: sub
kind: chapter
---

### 第二十三章附：GitHub入門指南——由代碼託管到協作平臺

{class="chapter-intro mb-4"}
上一章我哋講咗「編程思維」，而真正要將編程思維落地、同他人一齊做項目，就繞唔開一個名——GitHub。無論你係計算機系學生要參加比賽、想保存自己嘅代碼作品，仲係純粹想睇嚇全球開發者喺度折騰乜，GitHub都係你必須認識嘅平臺。呢一節我哋由最基礎嘅概念講起，幫你建立一個清晰嘅認知。

#### 一、GitHub到底係乜？

簡單嚟講，GitHub係一個基於Git嘅<strong>代碼託管與協作平臺</strong>。佢喺2008年上線，2018年被微軟收購，至今仍係全球最大嘅開源代碼託管平臺，託管住數億個倉庫，覆蓋幾乎所有主流編程語言。

如果用一個類比嚟理解：<strong>Git係你電腦上嘅日記簿，GitHub就係一個公開嘅部落格平臺</strong>——你可以發布自己嘅作品，關注別人嘅項目，參與討論同協作。佢唔單止係「程序員嘅後臺倉庫」，更好似全球開發者共建嘅一座「技術城市」——項目喺呢度誕生、迭代、被討論、被重用。

對普通人嚟講，GitHub亦並非遙不可及。好多非程序員會用佢嚟託管筆記、電子書、個人部落格，甚至用嚟備份設定檔案。只要你有一點點「想將自己嘅嘢整理好同分享出去」嘅需求，GitHub都值得你瞭解。

#### 二、Git同GitHub嘅區別（關鍵概念！）

好多人第一次接觸時會混淆呢兩個詞，呢度幫你梳理清楚：

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
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">記錄檔案嘅每次變更（點改嘅、邊個改嘅、幾時改嘅）</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">將Git倉庫放到雲端，方便儲存、展示、協作</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">係咪需要網絡</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">唔需要，離線可用</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需要聯網訪問</td>
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

簡單講：<strong>Git管「點樣記錄變更」，GitHub管「變更放喺邊、點樣協作」</strong>。Git係工具，喺本地運行；GitHub係平臺，將Git倉庫放到雲端，方便協作同展示。你可以淨係用Git唔用GitHub（比如自己寫代碼做版本管理），但用GitHub一定要用Git（因為GitHub就係基於Git嘅）。

#### 三、GitHub嘅核心概念與功能

##### 📁 基礎概念

喺動手之前，先認識幾個高頻詞彙，否則睇GitHub嘅介面會一頭霧水：

- <strong>倉庫（Repository，簡稱Repo）</strong>：一個項目對應一個倉庫，入面便存放住呢個項目嘅所有代碼檔案、歷史版本同文檔。可以理解為一個「項目資料夾」。
- <strong>提交（Commit）</strong>：對代碼嘅一次修改記錄。每次Commit都附帶說明資訊，記錄「呢次改咗乜、點解改」。呢個係Git/GitHub識得「時光倒流」嘅基礎。
- <strong>分支（Branch）</strong>：由主線上分出嚟嘅獨立開發線。比如你想加個新功能，可以開一個分支單獨開發，開發完再合併返主線，唔影響其他人。
- <strong>克隆（Clone）</strong>：將雲端倉庫完整複製一份到本地電腦，之後就可以喺本地修改代碼。
- <strong>推送（Push）/拉取（Pull）</strong>：Push係將本地代碼上傳到GitHub，Pull係由GitHub下載最新代碼到本地。呢個係團隊協作時同步代碼嘅兩個核心動作。
- <strong>合併請求（Pull Request，簡稱PR）</strong>：當你喺一個分支上改完代碼，想合併到主分支時，發起一個PR，等團隊成員審查代碼後再合併。呢個係GitHub協作嘅核心機制。
- <strong>議題（Issue）</strong>：用嚟記錄bug、功能需求、討論話題。每個Issue好似一個討論帖，可以指派負責人、打標籤。
- <strong>Fork</strong>：將別人嘅倉庫複製一份到自己帳號下，你可以喺自己嘅副本上隨意修改，唔影響原倉庫。改好後可以畀原作者發PR，請求合併你嘅改進。

##### 🛠️ 核心功能

GitHub提供嘅唔單止係代碼儲存，仲包括：

- <strong>版本控制</strong>：記錄每次代碼更改嘅歷史，改壞代碼隨時返到上一個正常版本。
- <strong>團隊協作</strong>：支援多用戶對同一項目嘅並行開發，多人同時開發唔會覆蓋、唔會衝突。
- <strong>問題跟蹤</strong>：用Issue記錄bug同功能請求，方便團隊跟進。
- <strong>項目管理</strong>：整合咗待辦事項、項目睇板（Projects）等管理工具，相當於內置咗一個輕量級Trello。
- <strong>自動化</strong>：透過<strong>GitHub Actions</strong>實現代碼提交後自動編譯、測試、打包、部署，係現代「CI/CD（持續集成/持續部署）」嘅核心工具。
- <strong>文檔管理</strong>：README介紹項目，Wiki存放詳細架構同開發規範，Pages甚至可以直接託管靜態網站。
- <strong>代碼託管與展示</strong>：每個倉庫都有靚嘅網頁展示，支援語法高亮，係你技術作品嘅「門面」。
- <strong>開源社區</strong>：你可以Star（收藏）喜歡嘅項目、Watch（關注）項目動態、Follow（關注）開發者，參與全球開源協作。

#### 四、註冊與上手：五分鐘創建你嘅第一個倉庫

##### 📝 註冊帳號

1. 訪問<a href="https://github.com" class="text-primary hover:underline" target="_blank" rel="noopener">github.com</a>，㩒「Sign up」。
2. 填寫郵箱、設定密碼同用戶名（用戶名會出現喺你嘅個人主頁地址入面便，建議用英文，比如<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">github.com/yourname</code>）。
3. 完成郵箱驗證同人機驗證。
4. 選擇免費方案（Free）即可，對個人用戶完全夠用。

##### 📁 創建第一個倉庫

1. 登入後㩒右上角「+」號，選「New repository」。
2. 填寫倉庫名（Repository name），比如<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">my-first-project</code>。
3. 寫一段簡短描述（Description），等別人知道呢個倉庫係做乜嘅。
4. 選擇公開（Public）或私有（Private）。公開倉庫所有人可見，私有淨係自己同協作者可見。免費帳號亦支援無限私有倉庫。
5. 勾選「Add a README file」——README係項目嘅「說明書」，每個倉庫都建議有。
6. 㩒「Create repository」，你嘅第一個GitHub倉庫就誕生喇！

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>小知識：README係乜

{class="mt-1"}
README.md係一個Markdown格式嘅檔案，係別人打開你倉庫時第一眼見到嘅內容。一個好嘅README通常包含：項目簡介、安裝方法、使用示例、許可證、聯繫方式。寫好README係程序員嘅基本素養，亦係項目能否被他人使用嘅第一道門檻。
:::

#### 五、基本工作流：由本地到雲端

理解GitHub嘅工作流，核心係記住呢個循環：<strong>本地修改 → 暫存 → 提交 → 推送 → 雲端更新</strong>。下面用大白話解釋每一步：

1. <strong>修改檔案</strong>：喺本地電腦上用編輯器寫代碼或改文檔。
2. <strong>git add</strong>：將修改嘅檔案加入「暫存區」，相當於話畀Git聽「呢啲改動我準備記錄低」。
3. <strong>git commit</strong>：將暫存區嘅改動正式記錄成一個「提交」，附上一句說明，比如「修復登入bug」。呢一步淨係喺本地完成。
4. <strong>git push</strong>：將本地嘅提交上傳到GitHub雲端，咁別人就能睇到喇。
5. <strong>git pull</strong>：喺開始工作前，先由雲端拉取最新代碼，確保本地同團隊其他人保持同步。

對新手嚟講，記住呢個口訣：<strong>「先pull後改，改完add，commit帶說明，最後push上去」</strong>。養成呢個習慣，團隊協作就唔會亂。

#### 六、團隊協作流程：Pull Request係點樣工作嘅

GitHub最強嘅地方喺佢嘅協作機制。一個典型嘅團隊協作流程係咁樣：

1. <strong>開分支</strong>：由主分支（通常叫main或master）開一個新分支，比如<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">feature/login</code>，喺呢個分支上開發新功能。
2. <strong>開發並提交</strong>：喺新分支上寫代碼，多次commit記錄進度。
3. <strong>推送到GitHub</strong>：將分支push到雲端倉庫。
4. <strong>發起Pull Request</strong>：喺GitHub網頁上發起PR，請求將你嘅分支合併到主分支。寫清楚呢個PR做咗乜改動、點解改。
5. <strong>代碼審查（Code Review）</strong>：團隊成員查看你嘅代碼，提出意見或建議修改。你可以根據反饋繼續commit，PR會自動更新。
6. <strong>合併</strong>：審查通過後，㩒「Merge」將代碼合併到主分支。你嘅貢獻就正式進入項目喇！

呢套流程保證咗<strong>任何代碼進入主分支前都經過審查</strong>，大大降低咗出錯概率。開源項目亦係用呢套機制接受全世界陌生人嘅貢獻——你完全 可以喺某個知名開源項目上提交PR，被採納後你就係呢個項目嘅貢獻者喇。

#### 七、GitHub嘅典型應用場景

##### 🎓 學生參加比賽與課程項目

計算機系學生參加ACM、黑客松、畢業設計，幾乎都離唔開GitHub。佢既可以作為團隊協作平臺，又能作為作品展示視窗——比賽評委可以直接睇你嘅倉庫，瞭解代碼質素同協作過程。好多公司招聘時亦會要求附上GitHub主頁，作為技術能力嘅證明。

##### 📚 個人知識庫與筆記託管

非程序員都能用GitHub。好多人用佢託管學習筆記、技術部落格（配合GitHub Pages可以免費建站）、電子書。Markdown格式寫作 + Git版本管理 + 雲端備份，三合一。

##### 🌐 參與開源項目

GitHub係全球開源運動嘅核心陣地。你可以Fork喜歡嘅項目，修改後發PR回饋社區；亦可以純粹Star收藏好項目，跟蹤更新。參與開源係提升技術、積累聲譽嘅絕佳途徑。

##### 🤖 自動化部署與CI/CD

藉助GitHub Actions，可以實現「代碼一push，自動測試+自動部署到伺服器」嘅全自動流程。好多個人部落格、文檔站點都係咁樣搭建嘅，寫完文章push一下，網站就自動更新喇。

##### 💾 代碼備份與多設備同步

將代碼倉庫當作雲盤用，換電腦、多設備辦公時，git pull一下就能攞到最新代碼，再亦唔使USB手指拷嚟拷去。

#### 八、畀新手嘅幾點建議

- <strong>提交說明要寫清楚</strong>：唔好寫「update」呢種廢話說明。好嘅commit message寫「修復用戶登入後跳轉錯誤頁面嘅問題」，半年後回睇都知當時做咗乜。
- <strong>勤提交，小步快跑</strong>：每完成一個小功能就commit一次，而唔係寫咗一成日先至提交一次。咁樣出問題更容易定位。
- <strong>用分支開發，唔好直接改主分支</strong>：哪怕係個人項目，養成開分支嘅習慣，未來團隊協作時就唔會手忙腳亂。
- <strong>善用.gitignore</strong>：呢個檔案用嚟話畀Git聽邊啲檔案唔好納入版本管理（比如密碼設定、編譯產物、依賴資料夾），避免將垃圾檔案傳上去。
- <strong>多睇優秀開源項目</strong>：行下GitHub Trending，睇嚇高星項目嘅代碼結構、README寫法、協作流程，係提升最快嘅免費方式。
- <strong>申請GitHub學生包</strong>：學生認證後可免費獲得大量付費工具同服務嘅額度（Copilot、域名、雲服務等），價值上千美元。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>安全提醒

{class="list-disc pl-6 mt-1 space-y-1"}
- 千萬唔好將密碼、API密鑰、數據庫連接串等敏感資訊提交到GitHub，尤其係公開倉庫——一旦洩露，會被爬蟲秒抓，後果嚴重。
- 唔小心提交咗敏感資訊，淨係刪除檔案唔夠（歷史記錄入面便仲有），要用<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git filter-branch</code>或專業工具清理歷史，並立即更換洩露嘅密鑰。
- 私有倉庫亦唔係絕對安全，敏感資訊最好用環境變數管理，唔入代碼倉庫。
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>國內訪問GitHub嘅注意事項

{class="mt-1"}
GitHub喺國內訪問有時唔穩定，可能出現打唔開、克隆慢嘅情況。可以嘗試：① 使用國內鏡像站（如GitClone、ghproxy）加速克隆；② 配置Hosts或使用代理；③ 如果主要面向國內協作，亦可以考慮國產替代品<strong>Gitee（碼雲）</strong>，功能類似且訪問速度快。好多團隊會同時喺GitHub同Gitee上託管，兼顧國際化同國內速度。
:::

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>進階玩法：用GitHub Pages搭建免費個人部落格

{class="mt-1"}
GitHub Pages允許你免費託管一個靜態網站，配合Jekyll、Hexo、Hugo等靜態站點生成器，可以輕鬆搭建個人部落格。寫完Markdown文章push到倉庫，部落格自動更新，仲自帶HTTPS同自訂域名。無數技術部落格嘅部落格都係咁樣搭嘅，零成本、無廣告、版本可控。
:::

#### 九、總結：點解每個人都應該瞭解GitHub

GitHub早已唔單止係「程序員嘅工具」，佢更好似一個<strong>數字時代嘅工作方式</strong>：版本管理等一切可追溯，協作機制等團隊高效運轉，開源精神等知識自由流動。哪怕你唔寫代碼，理解「提交、分支、合併」呢啲概念，都能幫你更好咁管理任何需要「反覆修改+多人協作」嘅內容——由論文到文檔，由筆記到方案。

對計算機系嘅學生嚟講，GitHub更係必備技能：佢係你嘅作品集、協作平臺、學習資源庫，亦係未來求職時最有說服力嘅「簡歷」。早啲註冊帳號，將自己嘅課程作業、小項目傳上去，慢慢積累，幾年後你會擁有一份等面試官眼前一亮嘅技術履歷。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>嚟動手：完成你嘅GitHub初體驗

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 註冊一個GitHub帳號，完善個人資料（頭像、簡介、感興趣嘅技術領域）。
2. 創建一個名為<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">hello-github</code>嘅公開倉庫，勾選「Add a README file」。
3. 進入倉庫，㩒README.md嘅編輯按鈕（鉛筆圖標），用Markdown寫一段自我介紹，提交更改。
4. 喺GitHub搜尋欄搜尋一個你感興趣嘅關鍵詞（比如<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python-tutorial</code>），Star兩個你喜歡嘅項目。
5. （進階）喺電腦上安裝Git，將倉庫Clone到本地，修改README後push返雲端，完成一次完整嘅「本地→雲端」工作流。
:::
