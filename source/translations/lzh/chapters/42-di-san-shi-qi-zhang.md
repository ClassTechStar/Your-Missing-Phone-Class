---
id: di-san-shi-qi-zhang
num: 37
part: ai-biancheng-pian
nav: 第三十七章：範式革命——自寫代碼至指揮AI寫代碼
toc: default
kind: chapter
---

### 第三十七章：範式之革——自「作碼」至「指 AI 作碼」

{class="chapter-intro mb-4"}
賀爾，展此書者，正立於職業範式之革之中央。為革之起，乃 2025 年一程序員於社交之媒所發之一言。聞之似近戲劇乎？然事實固如為也。

#### 一、Vibe Coding 之誕生：一言所起之運動

2025 年二月，Andrej Karpathy——其名請先識之，後尚數見之——於社交之媒發一推文，後為人所屢引：「有一新編程之法，曰 Vibe Coding，爾全憑感（vibes）而行，略碼之細節，使 AI 包攬一切。爾見何言何，複製而粘之，大抵能用即止。」

此言似脫口而出，實精名一已悄然生之範式之移：人不復逐行作碼，而以自然之語述其意，使 AI 成其實。Karpathy 之措辭微含戲謔，然其後有深察焉：AI 生碼之力既逾一閾，編程之隘，不復於「此行吾能作否」，而於「此事吾思之審否」。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小識：Vibe 何謂也？

{class="mt-1"}
Vibe 直譯為「氛、感」。Vibe Coding 者，「隨感而指 AI 編程」也——爾述所欲，AI 任其實。識此詞，為革之「出生之證」也。
:::

自彼時始，「編碼」之義始分：舊之編碼，譯設計為語法；新之編碼，譯意為令。前者試指，後者試腦。

Vibe Coding 之詞，驟自戲謔而為嚴肅工程之念。至 2026 年之中，已自社交之媒一梗，演為一套完備之方法論——自需求之表、上下文之管、迭代之驗至質量之保，全流程悉涵焉。人亦悟：「憑感」者，入門之態也；真高效之 AI 編程，須系統之思維。而此思維之系，即此書所欲授爾者也。

#### 二、2026 年之勢：Agentic Engineering 之世

至 2026 年八月，AI 編程之域已歷數要範式之迭代。Vibe Coding 者初火也，然眾旋覺：徒「憑感」而與 AI 語，所生之碼，質至不穩——時而驚豔，時而傾覆。於為範式始進：自簡之對話式編程，趨結構化之 Agent 工程。

又 Karpathy 也，2026 年之初，倡 Agentic Engineering 之念。異乎 Vibe Coding「言出即生」者，Agentic Engineering 所重者：予 AI 一之，使自規其步、調其器、驗其果、迭而正之。AI 不復徒生碼之器，乃能感境、能決策、能行事之智能體（Agent）也。

此變有三要焉：

1. 交感之式變：自「一問一答」變為「既設其之而授權」。
2. 工之所產變：自「一段之碼」變為「一完整之項目」。
3. 人之所任變：自「逐行審碼」變為「定其界、驗其果」。

數不誣也：Cursor 於 2026 年四月所頒之 Cursor 3 中，Agent 模式之使用率首超 Tab 補全之式，為開發者已大規模趨此工法之徵；而 Claude Code 者，終端原生 AI 編程之器也，至 2026 年之中，年化之入已達二十五億美元之規模。下之趨勢圖，可使爾親睹此交會之時：

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
圖一：AI 編程交感模式使用率之趨勢（據行業調研之數估算，2026 Q2 Agent 模式超 Tab 補全）
:::

然實言之：器與模型之變，表象也。無論爾用 Cursor 抑 Claude Code，無論底層之模型為 GPT-5 抑 Claude 4.5，成之者皆循同一底層之方法論。此本指南所欲授爾者也。

#### 三、核心之悟之變：自 Coder 至 Conductor

舊之編程之教，授爾為 Coder——解語法、記 API、調邏輯之誤。AI 編程之世，此任方被重定。爾不復須親作每行之碼，然須為「指揮官」（Conductor）：定戰場、立規則、分其任、驗其成。

此變之核，不於「爾能作碼否」，而於「爾能思審所欲為否」。良將不必為至勇之卒，然必最審戰之之、地之形、兵之布。同理，善 AI 編程者不必通每種編程語言之細，然必最審項目之之、架構之限與質量之準。

此表宜爾再觀——為變之全義，盡括於斯：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">維度</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">舊之 Coder</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">AI 之指揮官（Conductor）</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">核心之技</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">記語法、調 API、除誤</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定需求、管上下文、斷驗收</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">工之方式</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">逐行作碼</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">述其意，審其產</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">質量之控</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">己所作者，己心有數</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">以測試與審查驗 AI 之產</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">所需之知</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">深通特定之語言、框架</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">廣識技術之全貌，深解業務之邏輯</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">隘之所於</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">編碼之速與語法之記</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">思之審與達意之能</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">誤之所自</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">語法之誤、邏輯之漏</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">需求之晦、上下文之乏</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
舊 Coder 與 AI 指揮官之能維之比

此非謂編程之知不足重也。正相反：能解 AI 所作之碼，方能審而正之；解數據之構與算法，方能斷 AI 之策合理否。知之所積，定爾「指揮之上限」——然知之所任，自「執行之器」變為「決斷之據」矣。

#### 四、方法論何以重於工具

:::inline div .quote-line
器三月一迭代，方法論三年一進化。習一器之操作，三月後或已陳；得一思維之法，三年後猶可用。
:::

多人初學 AI 編程，首問「何器至善」「何模型至強」。此問非不重要，然所問之序誤矣。2026 年八月之器局，與 2025 年八月迥異——Trae、Qoder 諸器興衰起伏，Cursor 自插件而為獨立之 IDE，復進至 Cursor 3；Claude Code 自實驗之案而為終端編程之主流。然劇變之後，成者所循思維之則，幾無所變。

為故此書不惜費篇幅於某器之細操——此等之內容，甫成即陳舊。反之，全書之重，盡於一套已驗之思維方法論：何以思需求、何以與 AI 通、何以驗其產、何以續而迭代。得此法，則易任何之器皆可速上手；徒學器之操，一易其器，則自零始矣。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
慰零基之讀者

{class="mt-1"}
爾若零基，毋為「方法論」三字所懾。方法論者，非玄之哲也，乃「遇事當何以思」之操作之冊也。譬之學庖：可循譜而步（器之操），然大庖所解者，「何以如此調味」「火候何以制」（方法論）也。此書自至基之念始，每一則皆配對比之案例，使爾非惟解「何謂」，更能得「何以為」。
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：為今之爾攝一「角色之影」

{class="mt-1"}
出紙一張，書三問之答：① 爾今何以用 AI 助爾作碼（若曾用之）？② 爾肖上表之「Coder」抑「指揮官」？③ 爾望三月後之己，何以述其工法？書畢夾之書中，讀竟第四十七章復觀之——爾將見其變之速，逾於所想。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 2025 年 Karpathy 以「Vibe Coding」名 AI 編程之革：自逐行作碼，變為以自然之語述意
- 2026 年進為 Agentic Engineering：與之之、授之權，AI 自規劃而行，人任驗收
- Cursor 3 之 Agent 模式使用率首超 Tab 補全；Claude Code 年化之入達二十五億美元
- 爾之新任為 Conductor（指揮官）：定戰場、立規則、分其任、驗其成
- 工具每三月一迭代，方法論每三年一進化——學方法論，勿徒學操作
:::
