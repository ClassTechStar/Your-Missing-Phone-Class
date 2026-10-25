---
id: di-si-shi-qi-zhang
num: 47
part: ai-biancheng-pian
nav: 第四十七章：速查手冊與資源
toc: default
kind: chapter
---

### 第四十七章：速查手冊同資源

{class="chapter-intro mb-4"}
本章係一份可以獨立使用嘅速查手冊。當你記唔清某個原則或者需要快速決策嗰陣，直接揭到嚟呢度。建議你將佢當係「口袋卡」：五大原則速查、工具決策樹、常見問題、學習資源，一頁都唔漏。

#### 一、思維模型速查卡

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">原則</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">一句講曬</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">操作要點</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Think Before Coding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">先諗清楚先開口</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">答三條問題：做乜嘢？結果係點嘅？有乜嘢約束？</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Simplicity First</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用最少代碼解決問題</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">每次只做一個功能，斬走唔必要嘅複雜度</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Surgical Changes</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">精準修改唔越界</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">明確指定修改範圍，拒絕AI嘅「順手改嚇」</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Goal-Driven Execution</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">講「做乜嘢」唔好講「點樣做」</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">畀目標唔畀步驟，畀AI自主揀路徑</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">產生-驗證-修正循環</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">三層驗證：功能、邊界、架構</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
五大思維原則速查卡

#### 二、工具選擇決策樹

當你需要揀 AI 編程工具嗰陣，跟以下決策路徑嚟揀。留意：呢個唔係「邊個最好」嘅排名，而係「邊個最啱你」嘅判斷框架。

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-question-circle mr-1"></i> 你想做乜嘢？</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">零基礎，想快速體驗 → 揀雲端 Builder (v0/Bolt/Replit)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">日常開發，需要代碼補全 → 揀 IDE 內置 AI (Cursor/Trae)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">大型項目，需要批量操作 → 揀終端 Agent (Claude Code)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">快速原型驗證想法 → 揀雲端 Builder 或 Trae SOLO</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 6：AI 編程工具選擇決策樹
:::

#### 三、常見問題 FAQ

Q1：我完全唔識編程，可以用 AI 編程嗎？

得。2026 年嘅 AI 編程工具已經夠曬強大，你完全可以用自然語言描述需求，叫 AI 產生代碼。但有兩點建議：第一，由雲端 Builder 工具（例如 v0、Bolt）開始，佢哋唔使配置開發環境；第二，邊用邊學基礎概念——唔使精通語法，但你需要可以「睇得明」AI 寫嘅代碼嘅大意，咁樣先可以有效驗收。

Q2：我應該學邊個編程語言？

睇你想做乜嘢。做網站前端——JavaScript/TypeScript；做數據處理或者 AI——Python；做企業級後端——Java 或者 Go。但更重要嘅係：喺 AI 編程時代，「語言」嘅重要性喺度下降。AI 可以幫你處理語法細節，你需要明白嘅係「程序嘅結構」——乜嘢係函數、乜嘢係循環、乜嘢係數據結構。呢啲概念係跨語言嘅，一旦明白咗，轉乜嘢語言都快。

Q3：AI 寫嘅代碼有冇版權問題？

截至 2026 年 8 月，呢個仍然係一個有爭議嘅法律問題。一般嚟講，AI 產生嘅代碼喺大部分司法管轄區唔會被視為有明確嘅版權擁有者。但如果你用喺商業項目，建議：① 瞭解你用緊嘅 AI 工具嘅服務條款入面關於知識產權嘅條款；② 對關鍵代碼做人工審查同修改，令佢有你嘅創造性投入；③ 避免叫 AI 直接抄可能有版權嘅開源代碼。

Q4：AI 會唔會取代程序員？

短期內唔會。AI 取代嘅唔係「程序員」呢個職業，而係「逐行編碼」呢樣工作。就好似計數機冇取代數學家，而係令數學家由繁瑣嘅手算入面解放出嚟咁。AI 編程工具令程序員由「寫代碼」轉向「諗問題」——呢樣嘢實際上提高咗程序員嘅價值上限。將來嘅競爭力唔喺於「可以寫幾多行代碼」，而喺於「可以解決幾複雜嘅問題」。

Q5：點樣判斷 AI 嘅產出啱唔啱？

三層驗證法。第一層：功能驗證——佢行唔行到？輸入輸出啱唔啱？呢個係最基本嘅。第二層：邊界驗證——空輸入、超長輸入、異常輸入會點？呢層可以發現隱藏嘅問題。第三層：架構驗證——代碼結構合唔合理？有冇寫死嘅嘢？方唔方便擴展？呢層需要你有一定嘅技術判斷力。如果你判斷唔到第三層，至少做到頭兩層——行到、邊界正常，就已經比大部分初學者強。

#### 四、推薦學習資源

以下係截至 2026 年 8 月嘅推薦學習資源。留意，互聯網資源連結可能會變，如果某個連結失效，搜尋佢個標題通常可以搵到最新版本。

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">類型</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">資源</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">推薦理由</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">原始文獻</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Andrej Karpathy 嘅 CLAUDE.md</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">五大原則嘅源頭，70行但字字珠璣</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">原始文獻</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Anthropic 官方文檔 (Claude Code)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">終端Agent嘅最佳實踐指南</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">教程</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Vibe Coding 社羣整理嘅 Skills 合集</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">社羣實踐者總結嘅實戰技巧集合</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">教程</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor 官方文檔同 YouTube 頻道</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">IDE內置AI嘅權威使用指南</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">社羣</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitHub 上面嘅 awesome-claude-code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Code 嘅最佳實踐同插件集</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">社羣</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Reddit 嘅 r/cursor 社羣</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">全球Cursor用戶嘅經驗分享同討論</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">基礎</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MDN Web Docs (developer.mozilla.org)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">前端開發最權威嘅參考文檔</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">基礎</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Python 官方教程 (docs.python.org)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Python學習嘅官方起點</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
推薦學習資源清單

#### 五、結語：工具喺手，方法論喺心

返返去本書嘅核心信念：工具每三個月迭代一次，方法論每三年先進化一次。喺 2026 年 8 月嘅今日，AI 編程工具嘅能力已經強大到令人驚嘆——你可以用一句話整一個網站，用一段描述產生一個全端應用，用一條指令完成一個複雜重構。但工具越強大，方法論嘅重要性反而越突出——因為工具嘅強大會放大你嘅每一個決策。

如果你嘅需求清晰，AI 可以幫你高效實現；如果你嘅需求含糊，AI 都會高效咁做出錯嘅嘢。如果你跟簡單至上，AI 可以幫你快速驗證諗法；如果你貪多求全，AI 都會幫你快速堆積技術債。如果你精準修改，AI 可以幫你好似外科手術咁優化代碼；如果你指令含糊，AI 都會幫你大刀闊斧咁引入 bug。

呢個就係點解本書花咗大部分篇幅講方法論而唔係工具操作。唔係因為工具唔重要，而係因為方法論係工具嘅「乘數」——方法論越好，工具嘅價值越大；方法論係零，工具幾強都只係零乘任何數。

:::inline div .quote-line
你唔再係一個人喺度寫程式。你係一個指揮官，AI 係你嘅軍團。你思考嘅質素決定咗軍團嘅戰鬥力。由今日開始，用方法論武裝自己嘅思維，用工具放大自己嘅能力——呢個就係 AI 編程嘅全部祕密。
:::

#### 參考文獻

{class="list-decimal pl-6 mb-3 space-y-1 text-xs text-gray-500"}
1. Andrej Karpathy. (2025). Vibe Coding. Social media post introducing the concept of vibe-driven programming with AI.
2. Andrej Karpathy. (2025). CLAUDE.md - Project guidelines for AI-assisted development. GitHub repository, 70+K stars.
3. Anthropic. (2026). Claude Code: Terminal-native AI programming. Official documentation and best practices.
4. Cursor Team. (2026). Cursor 3: The next generation of AI-first IDE. Release notes and documentation.
5. OpenAI. (2026). Codex CLI: Bringing AI to the terminal. Technical documentation.
6. Model Context Protocol (MCP) Specification. (2025-2026). Open protocol for AI-tool integration.
7. Vibe Coding Community. (2026). Community-curated skills and best practices for AI-assisted programming.
8. Spec-Driven Development (SDD) methodology. (2026). Emerging practices in specification-first AI programming.
