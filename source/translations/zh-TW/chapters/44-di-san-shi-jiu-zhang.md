---
id: di-san-shi-jiu-zhang
num: 39
part: ai-biancheng-pian
nav: 第三十九章：上下文工程——讓AI理解你的意圖
toc: default
kind: chapter
---

### 第三十九章：上下文工程——讓AI理解你的意圖

{class="chapter-intro mb-4"}
你有沒有過這種體驗：換個新對話視窗，AI 就像失憶了一樣，把你專案的基本情況全忘了？這不是 AI 故意氣你，而是它天生"健忘"。這一章教你給 AI 裝上一套"長期記憶系統"，順便認識 2026 年最火的開發正規化之一——規範驅動開發。

#### 一、專案記憶檔案：AI 的"長期記憶"

AI 模型有一個根本性限制：它的記憶是"短時"的。每次對話開始時，AI 對你專案的瞭解為零。你需要在對話中不斷告訴它"我們用的是 React""後端是 Node.js""資料庫是 PostgreSQL""程式碼風格用雙引號"。這不僅低效，而且容易遺漏——就像每天都要重新給新來的同事做入職訓練。

解決方案是"專案記憶檔案"——一個放在專案根目錄的純文字檔案，AI 工具會在每次對話開始時自動讀取它。不同的工具有不同的命名約定：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">工具</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">檔名</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cursorrules</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">CLAUDE.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitHub Copilot</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">copilot-instructions.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">通用方案</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">AGENTS.md</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
各工具的專案記憶檔案命名約定

雖然命名不同，但原理一樣：把你希望 AI"始終記住"的資訊寫在這個檔案裡。一個好的專案記憶檔案應該包含：專案概述（這是什麼專案）、技術棧（用了什麼技術）、程式碼規範（命名、縮排、註釋風格）、目錄結構（程式碼怎麼組織的）、開發約定（分支策略、提交規範、測試要求）。Karpathy 的 CLAUDE.md 只有 70 行，但覆蓋了所有關鍵資訊——簡潔但完備。

::: div .code-block
:::inline div .code-head
<span>CLAUDE.md</span><span class="dots">···</span>
:::

```
# 專案：個人記帳應用
## 概述
這是一個全棧個人記帳應用，幫助使用者記錄日常收支。
## 技術棧
- 前端：React + TypeScript + Tailwind CSS
- 後端：Node.js + Express + TypeScript
- 資料庫：SQLite (開發) / PostgreSQL (生產)
- 測試：Vitest
## 程式碼規範
- 使用雙引號
- 縮排2個空格
- 函式名用camelCase
- 型別定義用PascalCase
- 每個函式必須有JSDoc註釋
## 目錄結構
/src
  /frontend  - 前端程式碼
  /backend   - 後端程式碼
  /shared    - 前後端共享的型別
  /tests     - 測試檔案
## 開發約定
- 提交資訊用中文
- 新功能必須先寫測試
- API返回統一用 { success, data, error } 格式
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：別寫成"第二份需求檔案"

{class="mt-1"}
注意這個檔案的長度——不要寫成幾十頁的需求檔案。專案記憶檔案的目的是"讓 AI 快速建立背景認知"，不是"詳細描述每個功能"。保持簡潔、結構化、只寫"AI 需要知道的"。
:::

#### 二、規範驅動開發（SDD）

Spec-Driven Development（SDD，規範驅動開發）是 2026 年逐漸成熟的一種開發正規化，核心理念一句話：先寫規範，再寫程式碼。與傳統 TDD（測試驅動開發）不同的是，SDD 的"規範"不僅是測試用例，還包括需求描述、介面定義、資料模型等。AI 根據這些規範來生成程式碼，人類的職責是編寫和維護規範。

SDD 的工作流程五步走：

1. 用自然語言描述需求規範（寫在一個 .md 檔案中）；
2. 定義介面和資料結構（寫在規範檔案中）；
3. 讓 AI 根據規範生成程式碼實現；
4. 執行測試驗證產出是否符合規範；
5. 如果不符合，修正規範或讓 AI 修正程式碼。

在這個流程中，規範檔案是"唯一真理源"——程式碼可以重新生成，但規範必須先正確。

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> 編寫規範檔案</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> 審查規範是否完備？</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> 完備</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> AI 根據規範生成程式碼</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> 執行測試驗證產出</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> 不完備 / 測試不過</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-tools mr-1"></i> 程式碼問題 → 修正程式碼；規範問題 → 修正規範</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> 回到驗證</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> 全部透過 → 交付</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
圖 3：規範驅動開發（SDD）的工作流程
:::

SDD 的優勢在於：規範檔案比程式碼更穩定。當底層模型或工具變化時，你的規範檔案依然有效，只需要讓新的 AI 工具重新生成程式碼即可。這也是為什麼本書強調"方法論比工具重要"——規範檔案就是你方法論的具體載體。

#### 三、上下文視窗管理

即使有了專案記憶檔案，你仍然會在對話中遇到"上下文不夠用"的問題。AI 模型的上下文視窗（能同時處理的資訊量）是有限的。當對話太長、引用的檔案太多時，AI 會"忘記"早期的資訊，導致產出品質下降——就像你和一個朋友聊天聊了六個小時，他早忘了你開頭說的第一件事。

管理上下文視窗的核心策略是"分層引用"：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">上下文層次</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">內容</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">管理方式</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第一層：專案記憶</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">技術棧、規範、目錄結構</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">寫在 CLAUDE.md 等檔案中，自動載入，無需重複</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第二層：檔案引用</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">當前任務涉及的程式碼檔案</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">用 @ 符號精確引用，不貼上全文到對話</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第三層：對話上下文</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">當前任務的對話歷史</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">完成一個任務後開新對話，避免上下文膨脹</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">第四層：即時指令</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">當前這一步的具體要求</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">清晰、簡潔、有針對性，避免冗長描述</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
上下文視窗的分層管理策略

#### 四、上下文工程的實踐要點

上下文工程不是一次性的設定，而是一個持續最佳化的過程。以下是幾個在實踐中被反覆驗證的要點：

1. 記憶檔案隨專案演進同步更新。引入新技術或改變架構時，第一時間更新記憶檔案，而不是在對話中臨時說明。
2. 善用 @ 引用而非全文貼上。大多數 AI 程式設計工具支援 @file 或 @folder 語法，它會在後臺將檔案內容注入 AI 的上下文，比手動貼上更高效且不會汙染對話。
3. 對話要"短小精悍"。一個對話只處理一個任務或一個功能點。完成後開新對話處理下一個。長對話不僅消耗上下文視窗，還會讓 AI"分心"。
4. 給 AI"看"結果而非"描述"結果。遇到 bug 時，把錯誤日誌直接 @ 引用給 AI，而不是用自己的話描述"好像有個什麼錯誤"。AI 看到原始資訊比看到你的轉述更有效。
5. 定期清理和歸檔。已完成的對話和臨時檔案會佔用工作空間。定期清理無關內容，保持專案目錄整潔，也有助於 AI 更高效地理解專案結構。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：給你的專案寫一份 70 行記憶檔案

{class="mt-1"}
挑一個你正在做（或打算做）的專案，寫一份 CLAUDE.md：專案概述（2-3 句話）、技術棧（列出來）、程式碼規範（3-5 條）、目錄結構（畫個樹）、開發約定（2-3 條）。控制在 70 行以內——寫完你會發現自己對專案的理解都清晰了不少。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- AI 的記憶是"短時"的：每次新對話，它對專案的瞭解為零
- 專案記憶檔案（CLAUDE.md 等）是 AI 的"長期記憶"，每次對話自動載入
- 好的記憶檔案 = 概述 + 技術棧 + 規範 + 目錄 + 約定，70 行足矣
- SDD 規範驅動開發：先寫規範再寫程式碼，規範是"唯一真理源"，比程式碼更穩定
- 上下文分四層管理：專案記憶 → @檔案引用 → 對話歷史 → 即時指令
- 五個實踐要點：同步更新、@引用、短對話、給原資訊、定期清理
:::
