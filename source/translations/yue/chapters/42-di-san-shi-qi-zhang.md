---
id: di-san-shi-qi-zhang
num: 37
part: ai-biancheng-pian
nav: 第三十七章：範式革命——由寫代碼到指揮AI寫代碼
toc: default
kind: chapter
---

### 第三十七章：範式革命——由「寫代碼」到「指揮 AI 寫代碼」

{class="chapter-intro mb-4"}
恭喜你，打開呢本書嘅你，正企喺一場職業範式革命嘅正中央。呢場革命嘅起點，係 2025 年一個程序員喺社交媒體上發嘅一句話。聽起嚟有啲戲劇性？但事實就係咁。

#### 一、Vibe Coding 嘅誕生：一句話引發嘅運動

2025 年 2 月，Andrej Karpathy——呢個名請先記住，後面仲會見到佢好幾次——喺社交媒體上發咗一條後來被反覆引用嘅推文：「有一種新編程方式叫 Vibe Coding，你完全憑感覺（vibes）嚟，忽略代碼細節，等 AI 包攬一切。你睇到乜就講乜，複製貼上，基本上用得就可以。」

呢條睇起嚟隨口一講嘅發言，其實精準命名咗一場已經悄然發生嘅範式轉移：人類唔再逐行編寫代碼，而係用自然語言描述意圖，由 AI 完成實現。Karpathy 嘅措辭帶住一絲戲謔，但背後係個深刻嘅洞察：當 AI 嘅代碼生成能力跨過某個閾值之後，編程嘅瓶頸就唔再係「呢行代碼我寫唔寫得出嚟」，而係「呢件事我到底想唔想得清楚」。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：Vibe 係乜嘢？

{class="mt-1"}
Vibe 直譯係「氛圍、感覺」。Vibe Coding 就係「跟住感覺指揮 AI 編程」——你描述想要乜嘢，AI 負責實現。記住呢個詞，佢係呢場革命嘅「出生證明」。
:::

由嗰一刻開始，「編碼」呢個詞嘅含義開始分裂：傳統嘅編碼係將設計翻譯成語法；新嘅編碼係將意圖翻譯成指令。前者考驗手指，後者考驗腦袋。

Vibe Coding 呢個詞好快由戲謔變成嚴肅嘅工程概念。到 2026 年中期，佢已經由一個社交媒體上嘅梗，演化為一套完整嘅方法論體系——涵蓋需求表達、上下文管理、迭代驗證到質量保障嘅全流程。人們亦意識到：「憑感覺」只係入門階段嘅狀態，真正高效嘅 AI 編程需要一套系統化嘅思維方式。而呢套思維方式，就係本書要畀你嘅嘢。

#### 二、2026 年現狀：Agentic Engineering 時代

到咗 2026 年 8 月，AI 編程領域已經經歷咗幾次重要嘅範式迭代。Vibe Coding 係最初嘅火花，但好快大家發現：光「憑感覺」同 AI 傾偈，產出嘅代碼質量極唔穩定——有時驚艷，有時翻車。於係範式開始進化：由簡單嘅對話式編程，走向結構化嘅 Agent 工程。

又係 Karpathy，2026 年初提出咗 Agentic Engineering 嘅概念。同 Vibe Coding 嘅「講咗就生成」唔同，Agentic Engineering 強調：畀 AI 一個目標，等佢自主規劃步驟、調用工具、驗證結果、迭代修正。AI 唔再只係一個代碼生成器，而係一個能夠感知環境、做出決策、執行動作嘅智能體（Agent）。

呢個轉變帶來咗三個關鍵變化：

1. 互動模式變咗：由「一問一答」變成「設定目標後放權」。
2. 工作產物變咗：由「一段代碼」變成「一個完整嘅項目」。
3. 人嘅角色變咗：由「逐行審核代碼」變成「定義邊界、驗收結果」。

數字唔會講大話：Cursor 喺 2026 年 4 月發佈嘅 Cursor 3 版本入面，Agent 模式嘅使用率首次反超 Tab 補全模式，標誌住開發者已經大規模轉向呢種工作方式；而 Claude Code 呢個終端原生嘅 AI 編程工具，到 2026 年中期已達到年化收入 25 億美元嘅規模。下面嘅趨勢圖可以畀你直觀感受呢個交叉時刻：

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="640" height="300" viewBox="0 0 640 300" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="640" height="300" fill="#ffffff" rx="8"/>
      <line x1="70" y1="240" x2="600" y2="240" stroke="#9ca3af" stroke-width="1.5"/>
      <line x1="70" y1="240" x2="70" y2="30" stroke="#9ca3af" stroke-width="1.5"/>
      <line x1="70" y1="190" x2="600" y2="190" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="70" y1="140" x2="600" y2="140" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="70" y1="90" x2="600" y2="90" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="70" y1="40" x2="600" y2="40" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="4,4"/>
      <text x="62" y="244" font-size="10" fill="#6b7280" text-anchor="end">0</text>
      <text x="62" y="194" font-size="10" fill="#6b7280" text-anchor="end">20</text>
      <text x="62" y="144" font-size="10" fill="#6b7280" text-anchor="end">40</text>
      <text x="62" y="94" font-size="10" fill="#6b7280" text-anchor="end">60</text>
      <text x="62" y="44" font-size="10" fill="#6b7280" text-anchor="end">80</text>
      <text x="335" y="272" font-size="11" fill="#374151" text-anchor="middle">使用率 (%)</text>
      <polyline points="70,215 220,172 370,152 590,116" fill="none" stroke="#4f46e5" stroke-width="2.5"/>
      <polyline points="70,52 220,85 370,103 590,135" fill="none" stroke="#9ca3af" stroke-width="2.5"/>
      <circle cx="70" cy="215" r="4" fill="#4f46e5"/><circle cx="220" cy="172" r="4" fill="#4f46e5"/><circle cx="370" cy="152" r="4" fill="#4f46e5"/><circle cx="590" cy="116" r="4" fill="#4f46e5"/>
      <circle cx="70" cy="52" r="4" fill="#9ca3af"/><circle cx="220" cy="85" r="4" fill="#9ca3af"/><circle cx="370" cy="103" r="4" fill="#9ca3af"/><circle cx="590" cy="135" r="4" fill="#9ca3af"/>
      <text x="70" y="285" font-size="10" fill="#6b7280" text-anchor="middle">2024 Q4</text>
      <text x="220" y="285" font-size="10" fill="#6b7280" text-anchor="middle">2025 Q2</text>
      <text x="370" y="285" font-size="10" fill="#6b7280" text-anchor="middle">2025 Q4</text>
      <text x="590" y="285" font-size="10" fill="#6b7280" text-anchor="middle">2026 Q2</text>
      <line x1="435" y1="60" x2="465" y2="60" stroke="#4f46e5" stroke-width="2.5"/>
      <text x="472" y="63" font-size="10" fill="#374151">Agent 模式使用率</text>
      <line x1="435" y1="82" x2="465" y2="82" stroke="#9ca3af" stroke-width="2.5"/>
      <text x="472" y="85" font-size="10" fill="#374151">Tab 補全模式使用率</text>
      <circle cx="529" cy="126" r="3" fill="#c0392b"/>
      <text x="529" y="152" font-size="10" fill="#c0392b" text-anchor="middle">≈ 2026 Q2 交叉</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 1：AI 編程互動模式使用率變化趨勢（基於行業調研數據估算，2026 Q2 Agent 模式反超 Tab 補全）
:::

但講句實喺話：工具同模型嘅變化只係表象。無論你用 Cursor 定係 Claude Code，無論底層模型係 GPT-5 定係 Claude 4.5，成功嘅 AI 編程實踐者都喺度遵循同一套底層方法論。呢個就係本指南要教你嘅嘢。

#### 三、核心認知轉變：由 Coder 到 Conductor

傳統編程教育教你點樣成為一個 Coder——理解語法、記憶 API、調試邏輯錯誤。AI 編程時代，呢個角色正在被重新定義。你唔再需要親手將每一行代碼寫出嚟，但你需要成為一個「指揮官」（Conductor）：定義戰場、制定規則、分配任務、驗收成果。

呢個轉變嘅核心唔喺於「你識唔識寫代碼」，而喺於「你識唔識想清楚要做乜嘢」。一個優秀嘅指揮官唔一定係最好嘅士兵，但佢必須最清楚戰役嘅目標、地形同兵力部署。同理，一個優秀嘅 AI 編程實踐者唔一定精通每一種編程語言嘅語法細節，但佢必須最清楚項目嘅目標、架構約束同質量標準。

呢張表值得你多睇兩次——佢概括咗呢次角色轉變嘅全部內涵：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">維度</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">傳統 Coder</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">AI 指揮官（Conductor）</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">核心技能</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">語法記憶、API 調用、調試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需求定義、上下文管理、驗收判斷</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">工作方式</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">逐行編寫代碼</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">描述意圖，審查產出</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">質量把控</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">自己寫嘅，自己心入面有數</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">透過測試同審查驗證 AI 產出</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">知識要求</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">深度掌握特定語言/框架</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">廣度理解技術全貌，深度理解業務邏輯</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">瓶頸所在</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">編碼速度同語法記憶</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">思考清晰度同表達能力</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">錯誤來源</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">語法錯誤、邏輯遺漏</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需求含糊、上下文唔夠</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
傳統 Coder 同 AI 指揮官嘅能力維度對比

呢個絕對唔係話編程知識唔重要喇。啱啱相反：當你睇得明 AI 寫嘅代碼時，你先能夠有效咁審查同修正佢；當你理解數據結構同算法時，你先能夠判斷 AI 嘅方案係咪合理。知識儲備決定咗你嘅「指揮上限」——但知識嘅角色由「執行工具」變成「判斷依據」。

#### 四、點解方法論比工具更重要

:::inline div .quote-line
工具每三個月迭代一次，方法論每三年先進化一次。學識一件工具嘅操作，三個月之後可能已經過時；掌握一套思維方式，三年之後依然啱用。
:::

好多人喺入門 AI 編程時，第一件事就係追問「邊個工具最好」「邊個模型最強」。呢啲問題唔係唔重要，但佢哋問錯咗優先級。2026 年 8 月嘅工具格局同 2025 年 8 月已經完全不同——Trae、Qoder 等工具興衰起伏，Cursor 由插件變成獨立 IDE 又進化到 Cursor 3，Claude Code 由實驗性項目變成終端編程嘅主流選擇。但喺呢劇烈變化背後，成功實踐者遵循嘅思維原則幾乎冇變。

呢個就係點解本書唔會將篇幅花喺教你某個工具嘅具體操作上——嗰啲內容寫完就會過時。相反，本書嘅全部重心放喺一套經過驗證嘅思維方法論上：點樣思考需求、點樣同 AI 溝通、點樣驗證產出、點樣持續迭代。掌握咗呢套方法論，你換任何工具都可以快速上手；只學咗工具操作，換一個工具就要由零開始。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
畀零基礎讀者嘅定心丸

{class="mt-1"}
如果你係零基礎，唔好畀「方法論」三個字嚇親。方法論唔係抽象嘅哲學，佢就係一套「遇到問題應該點諗」嘅操作手冊。就好似學煮餸：你可以跟住菜譜一步步嚟（工具操作），但真正嘅大廚理解嘅係「點解要咁樣調味」「火候點樣控制」（方法論）。本書會由最基礎嘅概念講起，每個原則都配具體嘅對比案例，確保你唔單止理解「係乜嘢」，更能夠掌握「點樣做」。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
嚟動手：畀而家嘅你影張「角色相」

{class="mt-1"}
攞出一張紙，寫低三個問題嘅答案：① 你而家係點樣用 AI 幫你寫代碼嘅（如果用過嘅話）？② 你更似上表中嘅「Coder」定係「指揮官」？③ 你希望三個月後嘅自己會點樣描述自己嘅工作方式？寫完之後夾喺書入面，讀完第四十七章再返嚟睇——你會發現變化比想像中快。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 2025 年 Karpathy 用「Vibe Coding」命名咗 AI 編程革命：由逐行寫代碼，變成用自然語言描述意圖
- 2026 年進化到 Agentic Engineering：畀目標、放權、AI 自主規劃執行，人負責驗收
- Cursor 3 嘅 Agent 模式使用率首次反超 Tab 補全；Claude Code 年化收入達 25 億美元
- 你嘅新角色係 Conductor（指揮官）：定義戰場、制定規則、分配任務、驗收成果
- 工具每三個月迭代一次，方法論每三年先進化一次——學方法論，唔學操作
:::
