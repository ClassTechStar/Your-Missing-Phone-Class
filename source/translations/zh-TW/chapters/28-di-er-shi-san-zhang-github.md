---
id: di-er-shi-san-zhang-github
part: chao-yue-pian
nav:  附：GitHub入門指南
toc: sub
kind: chapter
---

### 第二十三章附：GitHub入門指南——從程式碼託管到協作平臺

{class="chapter-intro mb-4"}
上一章我們講了"程式設計思維"，而真正要把程式設計思維落地、和他人一起做專案，就繞不開一個名字——GitHub。無論你是計算機系學生要參加比賽、想儲存自己的程式碼作品，還是單純想看看全球開發者在折騰什麼，GitHub都是你必須認識的平臺。這一節我們從最基礎的概念講起，幫你建立一個清晰的認知。

#### 一、GitHub到底是什麼？

簡單來說，GitHub是一個基於Git的<strong>程式碼託管與協作平臺</strong>。它於2008年上線，2018年被微軟收購，至今仍是全球最大的開原始碼託管平臺，託管著數億個倉庫，覆蓋幾乎所有主流程式語言。

如果用一個類比來理解：<strong>Git是你電腦上的日記本，GitHub就是一個公開的部落格平臺</strong>——你可以釋出自己的作品，關注別人的專案，參與討論和協作。它不僅是"程式設計師的後臺倉庫"，更像是全球開發者共建的一座"技術城市"——專案在這裡誕生、迭代、被討論、被複用。

對普通人來說，GitHub也並非遙不可及。很多非程式設計師會用它來託管筆記、電子書、個人部落格，甚至用來備份配置檔案。只要你有一點點"想把自己的東西整理好並分享出去"的需求，GitHub都值得你瞭解。

#### 二、Git和GitHub的區別（關鍵概念！）

很多人第一次接觸時會混淆這兩個詞，這裡幫你梳理清楚：

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
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">版本控制工具（軟體）</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">程式碼託管平臺（網站）</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">執行位置</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">本地電腦上</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">雲端（瀏覽器訪問）</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">核心職責</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">記錄檔案的每次變更（怎麼改的、誰改的、何時改的）</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把Git倉庫放到雲端，方便儲存、展示、協作</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">是否需要網路</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不需要，離線可用</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需要聯網訪問</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">歸屬</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">開源軟體，由Linus Torvalds（Linux之父）建立</td>
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

簡單說：<strong>Git管"怎麼記錄變更"，GitHub管"變更放在哪、怎麼協作"</strong>。Git是工具，在本地執行；GitHub是平臺，把Git倉庫放到雲端，方便協作和展示。你可以只用Git不用GitHub（比如自己寫程式碼做版本管理），但用GitHub一定要用Git（因為GitHub就是基於Git的）。

#### 三、GitHub的核心概念與功能

##### 📁 基礎概念

在動手之前，先認識幾個高頻詞彙，否則看GitHub的介面會一頭霧水：

- <strong>倉庫（Repository，簡稱Repo）</strong>：一個專案對應一個倉庫，裡面存放著這個專案的所有程式碼檔案、歷史版本和檔案。可以理解為一個"專案資料夾"。
- <strong>提交（Commit）</strong>：對程式碼的一次修改記錄。每次Commit都附帶說明資訊，記錄"這次改了什麼、為什麼改"。這是Git/GitHub能"時光倒流"的基礎。
- <strong>分支（Branch）</strong>：從主線上分出來的獨立開發線。比如你想加個新功能，可以開一個分支單獨開發，開發完再合併回主線，不影響其他人。
- <strong>克隆（Clone）</strong>：把雲端倉庫完整複製一份到本地電腦，之後就可以在本地修改程式碼。
- <strong>推送（Push）/拉取（Pull）</strong>：Push是把原生程式碼上傳到GitHub，Pull是從GitHub下載最新程式碼到本地。這是團隊協作時同步程式碼的兩個核心動作。
- <strong>合併請求（Pull Request，簡稱PR）</strong>：當你在一個分支上改完程式碼，想合併到主分支時，發起一個PR，讓團隊成員審查程式碼後再合併。這是GitHub協作的核心機制。
- <strong>議題（Issue）</strong>：用來記錄bug、功能需求、討論話題。每個Issue像一個討論帖，可以指派負責人、打標籤。
- <strong>Fork</strong>：把別人的倉庫複製一份到自己帳號下，你可以在自己的副本上隨意修改，不影響原倉庫。改好後可以給原作者發PR，請求合併你的改進。

##### 🛠️ 核心功能

GitHub提供的不只是程式碼儲存，還包括：

- <strong>版本控制</strong>：記錄每次程式碼更改的歷史，改壞程式碼隨時回到上一個正常版本。
- <strong>團隊協作</strong>：支援多使用者對同一專案的並行開發，多人同時開發不會覆蓋、不會衝突。
- <strong>問題跟蹤</strong>：用Issue記錄bug和功能請求，方便團隊跟進。
- <strong>專案管理</strong>：整合了待辦事項、專案看板（Projects）等管理工具，相當於內建了一個輕量級Trello。
- <strong>自動化</strong>：透過<strong>GitHub Actions</strong>實現程式碼提交後自動編譯、測試、打包、部署，是現代"CI/CD（持續整合/持續部署）"的核心工具。
- <strong>檔案管理</strong>：README介紹專案，Wiki存放詳細架構和開發規範，Pages甚至可以直接託管靜態網站。
- <strong>程式碼託管與展示</strong>：每個倉庫都有漂亮的網頁展示，支援語法高亮，是你技術作品的"門面"。
- <strong>開源社群</strong>：你可以Star（收藏）喜歡的專案、Watch（關注）專案動態、Follow（關注）開發者，參與全球開源協作。

#### 四、註冊與上手：五分鐘建立你的第一個倉庫

##### 📝 註冊帳號

1. 訪問<a href="https://github.com" class="text-primary hover:underline" target="_blank" rel="noopener">github.com</a>，點選"Sign up"。
2. 填寫郵箱、設定密碼和使用者名稱（使用者名稱會出現在你的個人主頁地址裡，建議用英文，比如<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">github.com/yourname</code>）。
3. 完成郵箱驗證和人機驗證。
4. 選擇免費方案（Free）即可，對個人使用者完全夠用。

##### 📁 建立第一個倉庫

1. 登入後點選右上角"+"號，選"New repository"。
2. 填寫倉庫名（Repository name），比如<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">my-first-project</code>。
3. 寫一段簡短描述（Description），讓別人知道這個倉庫是幹嘛的。
4. 選擇公開（Public）或私有（Private）。公開倉庫所有人可見，私有隻有自己和協作者可見。免費帳號也支援無限私有倉庫。
5. 勾選"Add a README file"——README是專案的"說明書"，每個倉庫都建議有。
6. 點選"Create repository"，你的第一個GitHub倉庫就誕生了！

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>小知識：README是什麼

{class="mt-1"}
README.md是一個Markdown格式的檔案，是別人開啟你倉庫時第一眼看到的內容。一個好的README通常包含：專案簡介、安裝方法、使用示例、許可證、聯絡方式。寫好README是程式設計師的基本素養，也是專案能否被他人使用的第一道門檻。
:::

#### 五、基本工作流：從本地到雲端

理解GitHub的工作流，核心是記住這個迴圈：<strong>本地修改 → 暫存 → 提交 → 推送 → 雲端更新</strong>。下面用大白話解釋每一步：

1. <strong>修改檔案</strong>：在本地電腦上用編輯器寫程式碼或改檔案。
2. <strong>git add</strong>：把修改的檔案加入"暫存區"，相當於告訴Git"這些改動我準備記錄下來"。
3. <strong>git commit</strong>：把暫存區的改動正式記錄成一個"提交"，附上一句說明，比如"修復登入bug"。這一步只在本地完成。
4. <strong>git push</strong>：把本地的提交上傳到GitHub雲端，這樣別人就能看到了。
5. <strong>git pull</strong>：在開始工作前，先從雲端拉取最新程式碼，確保本地和團隊其他人保持同步。

對新手來說，記住這個口訣：<strong>"先pull後改，改完add，commit帶說明，最後push上去"</strong>。養成這個習慣，團隊協作就不會亂。

#### 六、團隊協作流程：Pull Request是怎麼工作的

GitHub最強大的地方在於它的協作機制。一個典型的團隊協作流程是這樣的：

1. <strong>開分支</strong>：從主分支（通常叫main或master）開一個新分支，比如<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">feature/login</code>，在這個分支上開發新功能。
2. <strong>開發並提交</strong>：在新分支上寫程式碼，多次commit記錄進度。
3. <strong>推送到GitHub</strong>：把分支push到雲端倉庫。
4. <strong>發起Pull Request</strong>：在GitHub網頁上發起PR，請求把你的分支合併到主分支。寫清楚這個PR做了什麼改動、為什麼改。
5. <strong>程式碼審查（Code Review）</strong>：團隊成員檢視你的程式碼，提出意見或建議修改。你可以根據反饋繼續commit，PR會自動更新。
6. <strong>合併</strong>：審查透過後，點選"Merge"把程式碼合併到主分支。你的貢獻就正式進入專案了！

這套流程保證了<strong>任何程式碼進入主分支前都經過審查</strong>，大大降低了出錯機率。開源專案也是用這套機制接受全世界陌生人的貢獻——你完全可以在某個知名開源專案上提交PR，被採納後你就是這個專案的貢獻者了。

#### 七、GitHub的典型應用場景

##### 🎓 學生參加比賽與課程專案

計算機系學生參加ACM、駭客松、畢業設計，幾乎都離不開GitHub。它既能作為團隊協作平臺，又能作為作品展示視窗——比賽評委可以直接看你的倉庫，瞭解程式碼質量和協作過程。很多公司招聘時也會要求附上GitHub主頁，作為技術能力的證明。

##### 📚 個人知識庫與筆記託管

非程式設計師也能用GitHub。很多人用它託管學習筆記、技術部落格（配合GitHub Pages可以免費建站）、電子書。Markdown格式寫作 + Git版本管理 + 雲端備份，三合一。

##### 🌐 參與開源專案

GitHub是全球開源運動的核心陣地。你可以Fork喜歡的專案，修改後發PR回饋社群；也可以單純Star收藏好專案，跟蹤更新。參與開源是提升技術、積累聲譽的絕佳途徑。

##### 🤖 自動化部署與CI/CD

藉助GitHub Actions，可以實現"程式碼一push，自動測試+自動部署到伺服器"的全自動流程。很多個人部落格、檔案站點都是這麼搭建的，寫完文章push一下，網站就自動更新了。

##### 💾 程式碼備份與多裝置同步

把程式碼倉庫當作雲盤用，換電腦、多裝置辦公時，git pull一下就能拿到最新程式碼，再也不用隨身碟拷來拷去。

#### 八、給新手的幾點建議

- <strong>提交說明要寫清楚</strong>：別寫"update"這種廢話說明。好的commit message寫"修復使用者登入後跳轉錯誤頁面的問題"，半年後回看也知道當時幹了啥。
- <strong>勤提交，小步快跑</strong>：每完成一個小功能就commit一次，而不是寫了一整天才提交一次。這樣出問題更容易定位。
- <strong>用分支開發，別直接改主分支</strong>：哪怕是個人專案，養成開分支的習慣，未來團隊協作時就不會手忙腳亂。
- <strong>善用.gitignore</strong>：這個檔案用來告訴Git哪些檔案不要納入版本管理（比如密碼配置、編譯產物、依賴資料夾），避免把垃圾檔案傳上去。
- <strong>多看優秀開源專案</strong>：逛逛GitHub Trending，看看高星專案的程式碼結構、README寫法、協作流程，是提升最快的免費方式。
- <strong>申請GitHub學生包</strong>：學生認證後可免費獲得大量付費工具和服務的額度（Copilot、域名、雲服務等），價值上千美元。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>安全提醒

{class="list-disc pl-6 mt-1 space-y-1"}
- 千萬不要把密碼、API金鑰、資料庫連線串等敏感資訊提交到GitHub，尤其是公開倉庫——一旦洩露，會被爬蟲秒抓，後果嚴重。
- 不小心提交了敏感資訊，光刪除檔案不夠（歷史記錄裡還有），要用<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git filter-branch</code>或專業工具清理歷史，並立即更換洩露的金鑰。
- 私有倉庫也不是絕對安全，敏感資訊最好用環境變數管理，不程序式碼倉庫。
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>國內訪問GitHub的注意事項

{class="mt-1"}
GitHub在國內訪問有時不穩定，可能出現打不開、克隆慢的情況。可以嘗試：① 使用國內映象站（如GitClone、ghproxy）加速克隆；② 配置Hosts或使用代理；③ 如果主要面向國內協作，也可以考慮國產替代品<strong>Gitee（碼雲）</strong>，功能類似且訪問速度快。很多團隊會同時在GitHub和Gitee上託管，兼顧國際化和國內速度。
:::

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>進階玩法：用GitHub Pages搭建免費個人部落格

{class="mt-1"}
GitHub Pages允許你免費託管一個靜態網站，配合Jekyll、Hexo、Hugo等靜態站點生成器，可以輕鬆搭建個人部落格。寫完Markdown文章push到倉庫，部落格自動更新，還自帶HTTPS和自定義域名。無數技術博主的部落格都是這麼搭的，零成本、無廣告、版本可控。
:::

#### 九、總結：為什麼每個人都該瞭解GitHub

GitHub早已不只是"程式設計師的工具"，它更像是一個<strong>數字時代的工作方式</strong>：版本管理讓一切可追溯，協作機制讓團隊高效運轉，開源精神讓知識自由流動。哪怕你不寫程式碼，理解"提交、分支、合併"這些概念，也能幫你更好地管理任何需要"反覆修改+多人協作"的內容——從論文到檔案，從筆記到方案。

對計算機系的學生來說，GitHub更是必備技能：它是你的作品集、協作平臺、學習資源庫，也是未來求職時最有說服力的"簡歷"。早點註冊帳號，把自己的課程作業、小專案傳上去，慢慢積累，幾年後你會擁有一份讓面試官眼前一亮的技術履歷。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>來動手：完成你的GitHub初體驗

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 註冊一個GitHub帳號，完善個人資料（頭像、簡介、感興趣的技術領域）。
2. 建立一個名為<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">hello-github</code>的公開倉庫，勾選"Add a README file"。
3. 進入倉庫，點選README.md的編輯按鈕（鉛筆圖示），用Markdown寫一段自我介紹，提交更改。
4. 在GitHub搜尋欄搜尋一個你感興趣的關鍵字（比如<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python-tutorial</code>），Star兩個你喜歡的專案。
5. （進階）在電腦上安裝Git，把倉庫Clone到本地，修改README後push回雲端，完成一次完整的"本地→雲端"工作流。
:::
