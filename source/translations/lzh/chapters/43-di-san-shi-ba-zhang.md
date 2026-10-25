---
id: di-san-shi-ba-zhang
num: 38
part: ai-biancheng-pian
nav: 第三十八章：AI編程五大思維原則
toc: default
kind: chapter
---

### 第三十八章：AI 編程五大思維之則

{class="chapter-intro mb-4"}
若此書惟可使爾記一章，則必此章也。五大思維之則者，全書之心也，後之諸章——上下文、需求、對話、質量——皆此五則於異境之展也。毋憂，每一則皆非難解，然每一則皆值爾以數項目「長入肌理」。

事之起頗可觀：Andrej Karpathy 開源其項目時，附一僅 70 行之 CLAUDE.md 之檔，括與 AI 協作之四核之則。此檔於 GitHub 得 Star 七萬餘，為天下 AI 編程實踐者至廣引之則。此四則非虛號，乃自大量實踐中提煉、可操之思維之習也。本書於其上增第五則——迭代驗證——以成完備五則之系。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
70 行之檔，何以值錢若此？

{class="mt-1"}
Star 七萬，何謂也？GitHub 之上，項目之絕大多數終身不能至斯數。一 70 行之文檔而得之，適證一事：AI 之世，至稀缺者非碼，乃「思審」之能也。此 70 行，「思審」之濃縮也。
:::

#### 一、則一：Think Before Coding（先思而後碼）

此五則中之至反直覺者也。AI 既可助吾作碼，何必「先思」？答至簡：AI 產之質，與爾入之質正相係。爾自未思審所欲為，則 AI 之答徒使爾陷「改而復改」無已之環——俗謂「AI 與爾偕迷」也。

「先思」者，謂未下令於 AI 之先，爾須答三問，合成「思之三角」，缺一不可：

1. 吾欲解何事？（其之）
2. 吾所望之果何若？（驗收之準）
3. 有何約束之條當守？（其界）

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">思之維</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">晦之入（劣）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">審之入（佳）</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">事之定</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">助吾作一網站</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">為吾作一個人工具之站，陳三 AI 小工具入口之卡</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">所望之果</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">稍美觀可矣</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">響應式佈局，暗色之題，卡有懸停之動，移動之端可用</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">約束之條</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">（未言）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">不用框架，純 HTML+CSS+JS，單檔部署，無須後端</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
同一需求晦入與審入之比

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
慎之：先思 ≠ 先作完備之文檔

{class="mt-1"}
「先思」非謂「先作至善之 PRD 而後始」。乃速而有序之思也——費三十秒思審上之三問，遠勝費三十分鐘於對話中屢改。小任三問可短；大項目可廣之為完備需求之文（詳第四十章）。
:::

#### 二、則二：Simplicity First（簡為至上）

AI 編程至大之阱，非「作不成」，乃「作之過多」。爾謂 AI「作一用戶管理之系」，彼或生認證、權限、角色、審計日誌、數據導出諸功能一整套——而爾今所需，或惟一簡之登入之頁。生之過度，AI 碼膨脹之主因也。

「簡為至上」者，令爾每下令皆循「至小可行」之則：以至寡之碼成核心之功，以至簡之策解事，以至寡之能驗其念。Karpathy 有至精之喻：「爾欲算一折價，無須一電商之引擎。」

行之於實，「簡為至上」者，數具體之操作之習也：

- 每次惟使 AI 成一功能之點，毋一氣而述全系；
- 先擇標準之庫與簡之策，毋引繁複之依賴；
- 可 50 行碼解之事，毋使 AI 作 500 行；
- AI 之產逾所望之域，則勇告之曰「削其贅」。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">情境</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">過度之策（宜避）</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">簡之策（宜取）</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">須存數據</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">架 MySQL 之庫+ORM</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">先用 JSON 之檔或 SQLite</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">須用戶登入</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OAuth2.0 + JWT + 角色之權</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">先作簡之密碼之驗</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">須前端之框架</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">React + Redux + Router</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">先試純 HTML + 原生 JS</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">須部署而上線</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Docker + CI/CD + K8s</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">先於本地行通而後論</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
常境過度之策與簡策之比

#### 三、則三：Surgical Changes（改之必精）

爾迭代既有之項目，每改皆當如外科之術之精——惟動當動之處，毋觸不當觸者。此於 AI 編程尤要，蓋 AI 有「順手一改」之習：爾使修一 bug，彼或因而重構半檔。

「改之必精」之核要：每與 AI 之令，明指所改之域與界。告之曰「惟改 calculate_discount 之函」「毋動他部」「存今碼之風」。AI 之改逾爾所求之域，則立令退其贅。

Karpathy 舉 diff（差異之比）一例以明之。設爾使 AI 於購物車折算之函增「會員價」之邏輯：善之產者，惟改此函，增數行之碼而已；惡之產者，重構全檔——新碼雖或更「雅」，然爾不能定其有無新 bug。AI 編程之中，「觀之更佳」終不得為違令之辭。

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
劣之令（其域晦）

{class="font-mono text-xs leading-relaxed"}
助吾優此項目之 折扣計算之邏輯
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
佳之令（精指其域）

{class="font-mono text-xs leading-relaxed"}
惟改 cart.py 中之 calculate_discount 函： 1. 於現有折扣之上增會員價之邏輯 2. 會員另享 10% 之折 3. 毋改函之署與他函 4. 存今變數命名之風
:::
:::

#### 四、則四：Goal-Driven Execution（以之馭行）

此則答一要問：爾當下令於 AI 以「何以為」，抑以「作何事」？Karpathy 之答，後者也。與其告 AI「先立一類，次增其法，後作其測」，毋寧告之「吾須一器，能析 CSV 之檔而計每列獨一之值之數」。使 AI 自擇實現之徑，爾任驗其果。

「以之馭行」之利有二。於 AI，得更大自主之域，可擇至優之徑，不為爾中間之步所縛；於爾，移其注自「何以為」至「所作當否」——此正指揮官之所當為也。

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
慎之：以之馭行 ≠ 放而不問

{class="mt-1"}
為須爾於 AI 行後嚴驗之：果足需求乎？邊界之況處乎？有顯然過度之設乎？果不副所望，則予具體之饋——非曰「重作」，乃曰「此之弊於空列表之入則報 IndexError，請增空值之檢」。
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">令之風</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">其例</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">果之性</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">命令之式（何以為）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">「先立一 Python 之類，名曰 DataParser，增一 parse 之法，受 filename 之參，以 csv 之模讀之……」</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI 遂為繕寫之員，爾中間之步或非至優之徑</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">以之之式（作何事）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">「吾須一器：讀 CSV 之檔，計每列獨一之值之數，出以 JSON 之式。請畀完備之實。」</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI 自擇至優之徑，爾任驗其果</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
命令之令與以之之令之比

#### 五、則五：Iterate and Verify（迭代而驗）

此本書於 Karpathy 四則之上所增之第五則也。其核之信：AI 初產，幾終非定本。有效之 AI 編程，乃「生—驗—正」迭代之環，非一次之「令—產」也。

「迭代而驗」非被動之「不副則再試」，乃有結構之驗之流程也。AI 每有所產，循三層而驗：

- 一層·功能之驗：其能行乎？入出當乎？
- 二層·邊界之驗：空之入、過長之入、異常之入，其將何如？
- 三層·架構之驗：碼之構當乎？有硬編碼乎？便於後續之擴乎？

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-bullseye mr-1"></i> 定義目標</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> AI 生成代碼</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> 功能驗證</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> 通過</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> 邊界驗證</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> 通過</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-landmark mr-1"></i> 架構審查</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> 通過，進入下一步</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> 不通過</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> 提供具體反饋</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> 重新生成</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖二：AI 編程迭代驗證之環
:::

此環之要，於「予具體之饋」一步。驗之不過，勿曰「不對，重作」，當曰「此函於空列表之入則報 IndexError，請於第 15 行增空值之檢」。饋之具體，AI 乃能精正；饋之晦，徒使其復測爾意而已。

#### 六、Harness Engineering：Agent = Model + Harness

2026 年之中，有所謂 Harness Engineering 之念，始行於 AI 編程之社羣。其核之式至簡：

:::inline div .quote-line .text-center .text-base .font-bold
<strong>Agent 之能力 = 模型能力 × Harness 質量</strong>
:::

模型之能，AI 腦智之上限也；Harness 者，繞模型而搭之「工之境」——上下文之管、工具之集成、流程之編排、記憶之系之屬皆於其中。

此念解一常惑：同用 GPT-4 或 Claude，何以有者能作驚豔之項目，有者徒得平庸之碼？異不於模型，而於 Harness。善之 Harness，含：明澈之項目規範之檔、合理之工具集成、有序之對話上下文、完備之驗證流程。模型定智之上限，Harness 定爾能盡此上限幾何。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
天才實習生之喻

{class="mt-1"}
爾可想像模型為一天才實習生——智至高，然不畀項目背景之檔、不告以用何器、不為設期限與驗收之準，亦不能作善物。Harness Engineering 者，「何以為天才實習生搭善工境」之工程也。
:::

此書後之諸章，實皆授爾構善之 Harness：第三十九章授爾管上下文（項目記憶之系），第四十章授爾定需求（PRD），第四十三章授爾對話之術（Prompt 分層），第四十五章授爾質量之保（驗證之流程）。合而為之，即爾之 Harness 也。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：以「思之三角」析爾下一之念

{class="mt-1"}
擇一爾久欲為而未動手之小物（如一倒數日之網頁、一飲水提醒之腳本）。費 3 分鐘以答：① 其所解何事？② 作成何若？③ 有何約束（時、技、境）？乃以答成一段之文。賀爾，爾已畢人生首次「Think Before Coding」——此段之文，即一合格高質之令也。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 五則源自 Karpathy 70 行之 CLAUDE.md（70K+ Star），本書增第五則「迭代驗證」
- Think Before Coding：言之先答三問——作何事？果何若？有何約束？
- Simplicity First：AI 至大之阱於「作之過多」——算折價無須電商之引擎
- Surgical Changes：改如外科之術之精，拒 AI「順手一改」
- Goal-Driven Execution：言「作何事」，不言「何以為」，使 AI 自擇其徑
- Iterate and Verify：三層之驗（功能、邊界、架構）+ 具體之饋，循環而迭代
- Harness Engineering：能 = 模型 × Harness，視 AI 為「天才實習生」而理其境
:::
