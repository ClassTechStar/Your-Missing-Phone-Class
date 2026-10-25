---
id: di-er-shi-er-zhang
num: 22
part: chao-yue-pian
nav: 第二十二章：AI如何於手機中運作
toc: default
kind: chapter
---

### 第二十二章：AI如何於手機中工作

{class="chapter-intro mb-4"}
歡迎至手機最奇之"魔術現場"，主角乃：人工智能。君每日所用之"一拍即得"美照、張口即來之語音助手、越用越懂君之輸入法，背後皆有此隱形大腦於焉。

#### 一、AI相機：君之"後期暗房"已入手機

今之AI計算攝影，更似將一專業修圖師+攝影師團隊徑塞入快門鍵中。於君按下快門前，AI已始工作：掃描場景，識出"此乃藍天"、"此乃人臉"、"此乃夜景"。

#### 二、語音助手：君之"聲音祕書"何以懂君？

1. <strong>聽清（語音識別）</strong>：將聲波轉爲文字。
2. <strong>聽懂（自然語言理解）</strong>：理解意圖，提取關鍵實體。
3. <strong>執行與回答</strong>：調用對應App或服務，再以語音合成"說"與君聽。

#### 三、端側AI vs. 雲端AI

端側AI將計算留於手機中，速快、隱私高、可離線。雲端AI需聯網，然能處理更繁雜之任務。

#### 四、AI大模型與手機：君之隨身智能助手

2025-2026年，AI大模型（如DeepSeek R1、ChatGPT-5、文心一言5.0、通義千問3等）之爆發深刻改變矣手機之使用方式。手機不再只為執行指令之工具，而乃能理解、推理與創作之智能夥伴。端側AI芯片（NPU算力突破80 TOPS）使大模型推理首次於手機本地跑通，無需聯網也能用AI。

##### 何爲AI大模型？

AI大模型（Large Language Model，LLM）乃經海量文本數據訓練而出之AI系統，能理解並生成自然語言。君可想象其爲一讀過互聯網上幾乎所有文字之"超級學霸"，能答問、撰文、翻譯、編程、析數據。

##### 手機上之AI大模型應用：

- <strong>對話助手</strong>：DeepSeek、ChatGPT、豆包、Kimi等App，可隨時提問、翻譯、撰文案、總結文章。比傳統搜索引擎更智——其不只予君鏈接，乃徑予君答案。
- <strong>寫作與創作</strong>：令AI助君撰郵件、總結會議紀要、潤色文章、生成創意文案。
- <strong>圖像生成與編輯</strong>：AI一鍵消除照片中之路人、擴展圖片邊界、風格轉換、甚至依文字描述生成圖片。
- <strong>實時翻譯</strong>：通話實時翻譯、面對面對話翻譯、拍照翻譯，出國旅行不再有語言之礙。
- <strong>學習輔導</strong>：AI可釋概念、出題練習、批改作業，乃隨身家教。

##### 端側大模型：手機自運AI

最新之旗艦手機已能於本地運行小型AI大模型（通常7B參數左右），所致之變乃：

- <strong>不需網絡</strong>：斷網亦能用AI功能，飛機上、地鐵裏皆可。
- <strong>隱私更安全</strong>：君之對話與數據不會上傳雲端，全於手機本地處理。
- <strong>響應更速</strong>：無網絡延遲，AI之答幾乎即時。
- <strong>當前限制</strong>：端側模型之能尚不及雲端大模型，繁雜任務仍需聯網。然隨芯片AI算力之升，端側模型將愈強。

##### 系統級AI集成：

- <strong>蘋果Apple Intelligence</strong>：iOS 18引入之AI系統，集成寫作工具、圖像魔法棒、Siri增強、通知摘要等功能。端側處理優先，繁雜任務方上雲端。
- <strong>華爲盤古大模型</strong>：集成於鴻蒙系統，小藝助手得大模型之能，支持文檔摘要、智慧識屏、AI修圖等。
- <strong>小米澎湃AI</strong>：系統級AI之能，支持AI搜圖、AI摘要、AI實時字幕、端側大模型對話等。
- <strong>三星Galaxy AI</strong>：通話實時翻譯、筆記AI摘要、圖片生成編輯、搜索圈選等功能。

#### 五、數個典型應用場景與實操

爲令君更直觀感受手機AI之"超能"，下文以五個具體場景，示AI何以於日常生活中"出手相救"：

##### 場景一：實時翻譯——出國旅行之隨身翻譯官

<strong>實際表現</strong>：於巴黎點餐不諳法語？iPhone之"翻譯"App支持面對面雙人對話模式，雙方各觀己方語言之字幕，甚至可同聲傳譯。安卓陣營之三星Galaxy AI通話實時翻譯能令君於電話中徑說中文，對方所聞乃英文，反之亦然。

<strong>背後原理</strong>：語音識別（ASR）→ 機器翻譯（NMT）→ 語音合成（TTS）三步流水線，端到端延遲已可控於1秒內。

##### 場景二：AI消除——拯救被路人"毀掉"之遊客照

<strong>實際表現</strong>：於景點拍一絕美自拍，然背景中擠滿他客？用"魔法消除"圈選路人，手機將自動識別並"塗去"路人，再智能填充背景，效果常令人驚豔。

<strong>背後原理</strong>：圖像分割（Inpainting）模型先識別並刪除選中區域，而後依周圍像素與語義理解"腦補"出合理之填充內容。此背後之AI模型訓練數據量達數百萬張圖片。

##### 場景三：AI修圖——一鍵成"攝影大師"

<strong>實際表現</strong>：拍了一張陰天灰濛濛之風景照？AI"魔法天空"可一鍵將天空換爲晴空、晚霞甚至星空。AI擴圖可令豎構圖變爲橫構圖，手機"腦補"出畫面外之場景。

<strong>背後原理</strong>：基於生成式AI（Generative AI）之擴散模型（Diffusion Model），理解圖像之語義內容後生成新像素。此乃當前AI圖像處理之"最前沿"。

##### 場景四：文檔處理——辦公族之效率倍增器

<strong>實際表現</strong>：會議畢，將會議錄音予AI，其能自動整理出結構化之會議紀要、提取待辦事項、生成摘要。一份10頁之英文PDF報告，AI可於10秒內爲君提煉出核心結論。

<strong>背後原理</strong>：長上下文大模型（Long Context LLM）可"讀完"數萬字之文檔，行多輪推理與信息抽取。Apple Intelligence、華爲小藝、WPS AI、騰訊元寶等皆具此能。

##### 場景五：AI搜圖與識物——君之"視覺搜索引擎"

<strong>實際表現</strong>：於街上見一種不識之花，相機一開，AI立告君"此乃木槿花"。相冊中翻尋去年於海邊所拍之照片，搜索"大海"，AI自動將所有含海之照片尋出，無需手動翻尋。

<strong>背後原理</strong>：計算機視覺（CV）模型對圖片內容行向量化（Embedding），再與文字查詢行相似度匹配。此等"多模態搜索"乃手機相冊管理之一大飛躍。

#### 六、提示詞優化：令AI聽君指揮之"溝通公式"

AI答之質，大抵繫於君何以"問"。同一之問，問法異，則AI所答天壤之別。下文吾輩介紹一套<strong>最實用、最易上手之"角色-背景-任務-限制"溝通思路</strong>，並配以大量實例。

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-puzzle-piece mr-2"></i>何故需框架？

{class="mt-1"}
多人用AI如用百度——敲數關鍵詞入之。然AI非搜索引擎，其乃一"閱讀理解後回答"之語言模型。<strong>予其更多上下文、說清君欲何、限其勿跑偏</strong>，其即能予君精準之結果。框架乃將君腦中"好答案長何樣"譯爲AI能解之指令。
:::

{class="font-semibold mt-4 mb-1"}
##### 1. 角色（Role）：告AI其爲何人

予AI一具體之"身份"，其即調用對應領域之專業知識與表達方式。<strong>角色設定愈具體，輸出愈專業</strong>。

##### 實用示例：

{class="list-disc pl-6 mb-3 space-y-2"}
- "君乃一位<strong>有10年經驗之小米手機維修工程師</strong>。"（技術問題）
- "君乃一位<strong>擅長將繁雜概念講簡之中學物理老師</strong>。"（科普問題）
- "君乃一位<strong>審美好、閱書多、自有風格之圖書編輯</strong>。"（寫作問題）
- "君乃一位<strong>每日爲上班族做早餐之烹飪博主</strong>。"（生活問題）
- "君乃一位<strong>耐心、溫和、永不哂新手之中醫</strong>。"（健康問題）

::: div .highlight-quote
{class="mb-1"}
<strong>何以有效？</strong>角色設定了AI之<strong>知識範圍</strong>、<strong>表達風格</strong>與<strong>專業深度</strong>。無角色之AI乃一"全才然啥皆不精"之通才；有角色，其能"入"彼身份，如那位專業人士般思考。
:::

{class="font-semibold mt-4 mb-1"}
##### 2. 背景（Background）：告AI君之情況

將"君爲何人、君之現狀、君之約束條件"先說清楚，AI方能予<strong>真適合君</strong>之答案，而非泛泛而談。

##### 實用示例：

{class="list-disc pl-6 mb-3 space-y-2"}
- "吾之手機乃<strong>小米14，購半年，近玩遊戲時發燙嚴重</strong>。"（設備情況）
- "吾乃<strong>一60歲之退休婦人，目力不佳，不善用智能手機</strong>。"（用戶畫像）
- "吾正<strong>備2026年6月之英語六級考試，基礎一般</strong>。"（學習背景）
- "吾開了一家<strong>三線城市之小咖啡店，月流水3萬，僱兩名員工</strong>。"（商業背景）
- "吾<strong>甫誕嬰在家坐月子，睡眠嚴重不足</strong>。"（生活階段）

::: div .highlight-quote
{class="mb-1"}
<strong>何以有效？</strong>背景信息令AI知<strong>"爲誰服務"</strong>與<strong>"於何條件下"</strong>。同一題，予學生與予家長講法不同；予城人與予鄉人建議亦異。背景缺，則AI只能予"最大公約數"之答案，常不痛不癢。
:::

{class="font-semibold mt-4 mb-1"}
##### 3. 任務（Task）：明告AI做何事

此步當以<strong>動詞開頭</strong>（寫、列、對比、翻譯、解釋、總結……），將任務描述得<strong>具體、可執行</strong>。含糊之任務唯換來含糊之答案。

##### 實用示例：

{class="list-disc pl-6 mb-3 space-y-2"}
- "請<strong>列出5個吾應立即關閉之權限</strong>，並說明緣由。"（動作明確）
- "請<strong>將下段英文郵件譯爲中文</strong>，保持商務口吻。"（任務具體）
- "請<strong>對比此四款3000元價位之手機</strong>，予出一張優缺點對比表。"（格式明確）
- "請<strong>以小學生能懂之言解釋‘何爲5G’</strong>。"（風格明確）
- "請<strong>爲吾之早餐店寫三條短視頻文案</strong>，分別針對上班族、情侶、帶孩子之家長。"（細分明確）

::: div .highlight-quote
{class="mb-1"}
<strong>何以有效？</strong>任務部分乃AI行動之"指令中樞"。<strong>動詞愈清晰、要求愈具體，AI愈知"交付何物"</strong>。模糊之"稍弄"、"搞個"、"看看"乃AI大忌——其將揣測君意，結果常跑偏。
:::

{class="font-semibold mt-4 mb-1"}
##### 4. 限制（Constraints）：告AI勿做何事

"限制"聽之似"約束"，實乃<strong>令AI收斂至最適合君之輸出</strong>之利器。常見維度有：字數、格式、語氣、避免項、必含項。

##### 實用示例：

{class="list-disc pl-6 mb-3 space-y-2"}
- "<strong>不超過200字，分點列出</strong>。"（長度+格式）
- "<strong>語氣當親切自然，如與友聊天</strong>，勿用‘先、次之、再次’此等官話。"（語氣）
- "<strong>勿用專業術語</strong>，遇專業名詞當順便釋之。"（用詞限制）
- "<strong>每段不超過3行</strong>，方便手機閱讀。"（排版）
- "<strong>必含：使用場景、優缺點、與吾預算之匹配度</strong>。"（必含項）
- "<strong>勿予具體投資建議</strong>，只釋原理。"（邊界）

::: div .highlight-quote
{class="mb-1"}
<strong>何以有效？</strong>無限制，AI易"自由發揮"——或太學術、或太長、或跑題。明確之限制=明確之"交付標準"，雙方對齊預期，結果方可控。
:::

{class="font-semibold mt-4 mb-1"}
##### 5. 提示詞質量評估：好提示詞之5個特徵

寫好提示詞非一次性之事，<strong>寫完先自查此五條</strong>，再發與AI：

1. <strong>具體而非抽象</strong>：非"寫篇文章"，乃"寫一篇800字、3個小節、面向新手媽媽之手機選購指南"。
2. <strong>含背景而非孤立</strong>：告AI"吾爲何人、何故問此"，其方能予"爲君定製"之答案。
3. <strong>有明確輸出格式</strong>：爲表格、列表、段落、抑或JSON？先說之。
4. <strong>限制到位</strong>：字數、風格、避項，三選一即有明顯提升。
5. <strong>可被AI驗證</strong>：問畢，令AI複述一遍君之要求；說不清楚即未說清楚。

{class="font-semibold mt-4 mb-1"}
##### 6. 常見問題與解法

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                            <thead>
                                <tr class="bg-light dark:bg-gray-700">
                                    <th class="border border-gray-300 px-3 py-2 text-left">症狀</th>
                                    <th class="border border-gray-300 px-3 py-2 text-left">解法</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 px-3 py-2">回答太泛、不實用</td>
                                    <td class="border border-gray-300 px-3 py-2">加背景（君爲何人/何場景）</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 px-3 py-2">回答太學術/太官方</td>
                                    <td class="border border-gray-300 px-3 py-2">加語氣限制 + 拒"官話"清單</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 px-3 py-2">回答跑題/答非所問</td>
                                    <td class="border border-gray-300 px-3 py-2">以動詞重述任務，並要求"只答此" </td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 px-3 py-2">回答太長看不完</td>
                                    <td class="border border-gray-300 px-3 py-2">硬性限字數（200字內）</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 px-3 py-2">AI一本正經胡說</td>
                                    <td class="border border-gray-300 px-3 py-2">加"若不確定請標‘吾不確定’" + 重要事實自查</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 px-3 py-2">第一版不滿意</td>
                                    <td class="border border-gray-300 px-3 py-2">勿重寫，於原提示詞後追加"再…一些"</td>
                                </tr>
                            </tbody>
                        </table>
```
:::

{class="font-semibold mt-4 mb-1"}
##### 7. 三個完整場景案例

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-coffee mr-2"></i>場景一：生活助手（早餐搭配建議）

{class="mt-1"}
<strong>提示詞</strong>：

{class="mt-1 text-sm" style="font-family: monospace; background: #f5f5f5; padding: 8px; border-radius: 4px;"}
君乃一位擅長營養搭配之早餐博主（<strong>角色</strong>）。吾乃一位上班族媽媽，每日晨只有15分鐘做早餐，家有6歲之孩子與60歲之婆婆（<strong>背景</strong>）。請<strong>列出7天不重樣之早餐搭配</strong>（<strong>任務</strong>）。每份早餐要求：① 準備時間不超過15分鐘 ② 營養均衡（蛋白+碳水+蔬果）③ 老少皆宜 ④ 食材於普通超市能買到（<strong>限制</strong>）。

{class="mt-1"}
<strong>何以有效</strong>：角色定專業度，背景予三類人共性，任務明交付物，4條限制保可執行。
:::

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-graduation-cap mr-2"></i>場景二：學習輔助（英語六級備考）

{class="mt-1"}
<strong>提示詞</strong>：

{class="mt-1 text-sm" style="font-family: monospace; background: #f5f5f5; padding: 8px; border-radius: 4px;"}
君乃一位<strong>經驗豐富之英語六級老師</strong>（角色）。吾乃一普通本科生，<strong>四級480分，六級目標500，尚餘3月</strong>（背景）。請<strong>爲吾制定一份可執行之12周備考計劃</strong>（任務）。要求：① 每週明聽說讀寫之時間分配 ② 予出每月之重點突破方向 ③ 推薦3本合適之複習資料（中文說明緣由） ④ 表格形式輸出（限制）。

{class="mt-1"}
<strong>何以有效</strong>：角色定專業背景，背景予出分數與時間錨點，任務明"分階段計劃"，限制要求"表格化"與"可執行"。
:::

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-briefcase mr-2"></i>場景三：工作效率（會議紀要整理）

{class="mt-1"}
<strong>提示詞</strong>：

{class="mt-1 text-sm" style="font-family: monospace; background: #f5f5f5; padding: 8px; border-radius: 4px;"}
君乃一位<strong>資深行政助理</strong>（角色）。吾剛開完一個1小時之部門會議，<strong>討論Q2營銷推廣方案</strong>（背景）。<strong>請將以下會議記錄整理成結構化紀要</strong>（任務）。要求：① 分"決議事項 / 待辦事項 / 風險與異議"三部分 ② 待辦事項標出負責人與截止時間（若未提及則寫"待確認"） ③ 總字數控於600字內 ④ 以markdown格式輸出（限制）。

{class="mt-1"}
<strong>何以有效</strong>：角色定行政視角，背景予會議主題，任務明結構化輸出，4條限制令結果徑可複用。
:::

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-rocket mr-2"></i>進階玩法：令AI爲君之"私人助理"

{class="mt-1"}
試此等進階用法，以體驗AI之真正實力：

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>多輪對話優化</strong>：對AI之回答不滿意時，可曰"此太專業矣，請以小學生能懂之言再釋一次"。
- <strong>鏈式思考（CoT）</strong>：令AI"一步步思考"，回答質量通常更高："請一步步析此數學題"。
- <strong>多AI協作</strong>：以A寫初稿，B潤色，C翻譯——組合使用效果更佳。
- <strong>系統提示詞</strong>：於AI設置中預設君之身份、偏好、忌諱等，令回答更合君之需。
:::

#### 七、AI之侷限與挑戰：保持清醒之判斷力

AI雖強，然絕非"無所不能"。清醒識其侷限，方能更好用之：

- <strong>"幻覺"問題</strong>：AI或一本正經地胡言（專業術語曰Hallucination）。其將編造不存在之歷史事件、錯誤之引言、虛假之統計數據。重要信息必須人工覈實。
- <strong>知識截止</strong>：多數AI之訓練數據有截止日期（如2024年初），其不知之後發生之事。
- <strong>推理能力有限</strong>：繁雜之多步推理、數學證明、邏輯陷阱，AI仍易出錯。
- <strong>隱私風險</strong>：於雲端AI服務中，君之對話或被用於模型訓練。敏感信息當優先用端側AI。
- <strong>偏見與價值觀</strong>：AI或帶訓練數據中之偏見，需保持獨立思考。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>AI使用小貼士

{class="list-disc pl-6 mt-1 space-y-1"}
- AI生成之內容或不準（"幻覺"問題），重要信息務必覈實。
- 勿向AI輸入個人隱私信息（身份證號、密碼、銀行信息等）。
- 善用提示詞（Prompt）：愈具體、愈清晰之描述，AI之回答質量愈高。
- AI乃工具非權威，保持獨立思考與判斷力。
- 遇關鍵決策（醫療、法律、財務），諮詢專業人士而非依賴AI。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>來挑戰：三道AI實戰題

{class="list-decimal pl-6 mt-1 space-y-1"}
1. <strong>挑戰一：複雜指令</strong>：對語音助手曰："明晨7點提醒吾帶傘，並將今日午後3點之日曆改至4點。" 觀其能否一次完成多步操作。
2. <strong>挑戰二：AI修圖</strong>：拍一張有路人之遊客照，用"魔法消除"或"AI橡皮擦"功能，將路人清除乾淨。觀AI對背景之"腦補"效果。
3. <strong>挑戰三：提示詞優化</strong>：先以簡單提示詞"寫一段旅遊攻略"問AI，再以CRISPE框架寫一詳細提示詞。較兩次回答之質量差異。
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>案例 2：換機數據遷移全程

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>場景</strong>：iPhone 13 → 小米 15 跨品牌換機。
- <strong>步驟</strong>：① 舊機 iCloud/微信自帶備份 → ② 退 Apple ID + 閉"尋" → ③ 新機用"小米換機"App 掃碼 → ④ 擇遷移項 → ⑤ 微信單獨用自帶"聊錄遷移" → ⑥ 驗鍵數據（通訊錄/相冊/微信） → ⑦ 舊機加密擦。
- <strong>預期果</strong>：數據零丟失，舊機可安全轉賣。
:::
