---
id: di-san-shi-ba-zhang
num: 38
part: ai-biancheng-pian
nav: Chapter 38: Five Thinking Principles for AI Coding
toc: default
kind: chapter
---

### Chapter 38: Five Thinking Principles of AI Coding

{class="chapter-intro mb-4"}
If this book makes you remember only one chapter, make it this one. The five thinking principles are the book's heart. Everything after — context, requirements, prompts, quality — expands these five in different scenarios. Don't worry: none are hard to grasp, but each deserves a few projects to sink into muscle memory.

The story starts with a fun origin: when Andrej Karpathy open-sourced his project, he attached a 70-line CLAUDE.md summarizing four core principles for working with AI. That file earned 70,000+ GitHub Stars and became the most widely cited playbook for AI coding practitioners worldwide. These four principles aren't empty slogans — they're actionable thinking habits distilled from massive practice. This book adds a fifth — Iterate and Verify — completing the five-principle system.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Why is a 70-line file so valuable?

{class="mt-1"}
What do 70,000 Stars mean? Most GitHub projects never get close. That a 70-line text file earned them proves one thing: in the AI era the scarcest resource isn't code — it's the ability to "think clearly." Those 70 lines are a concentrated form of clarity.
:::

#### 1. Principle 1: Think Before Coding

This is the most counterintuitive of the five. If AI can write code for us, why think first? Simple: AI output quality tracks your input quality. If you haven't figured out what you want, AI's answers will trap you in endless revision loops — aka "AI getting lost with you."

"Think first" means answering three questions before prompting AI — an inseparable "thinking triangle":

1. What problem am I solving? (Goal)
2. What should the result look like? (Acceptance criteria)
3. What constraints must I respect? (Boundaries)

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Thinking dimension</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Vague input (bad)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Clear input (good)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Problem definition</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Make me a website</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Make a personal tool site with entry cards for 3 small AI tools</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Expected result</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Make it look nice</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Responsive layout, dark theme, hover animation on cards, works on mobile</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraints</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">(Not stated)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">No frameworks, pure HTML+CSS+JS, single-file deploy, no backend</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Vague vs. clear input for the same request

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Note: Think first ≠ write a perfect spec first

{class="mt-1"}
"Think first" doesn't mean "write a perfect PRD before starting." It's a quick but structured thinking pass — 30 seconds on those three questions beats 30 minutes of back-and-forth in chat. Small tasks need short answers; big projects can expand them into full requirement docs (see Chapter 40).
:::

#### 2. Principle 2: Simplicity First

The biggest trap in AI coding isn't "can't build it" — it's "builds too much." Ask AI for a "user management system" and it may generate auth, permissions, roles, audit logs, data export — when all you need is a simple login page. Overbuilding is the main cause of bloated AI code.

"Simplicity First" means following the "minimum viable" rule every time you prompt: implement the core with the least code, solve the problem with the simplest design, validate the idea with the fewest features. Karpathy put it well: "If you need a discounted price, you don't need an e-commerce engine."

In practice, Simplicity First means a few concrete habits:

- Have AI implement one feature at a time, not the entire system in one prompt;
- Prefer standard libraries and simple designs over heavy dependencies;
- If 50 lines can solve it, don't let AI write 500;
- When AI's output goes beyond scope, boldly tell it to cut the extras.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Scenario</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Overbuilt (avoid)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Simple (recommended)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Need to store data</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Set up MySQL + ORM</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Start with JSON files or SQLite</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Need user login</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OAuth2.0 + JWT + role permissions</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Start with simple password auth</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Need a frontend framework</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">React + Redux + Router</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Try plain HTML + vanilla JS first</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Need to deploy</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Docker + CI/CD + K8s</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Get it running locally first</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Overbuilt vs. simple approaches for common scenarios

#### 3. Principle 3: Surgical Changes

When iterating an existing project, every change should be surgical — touch only what must change. This matters especially in AI coding because AI loves to "tidy up while it's in there": you ask it to fix one bug and it refactors half a file.

Surgical Changes means every prompt explicitly states the scope and boundaries: "Only modify the calculate_discount function," "don't touch anything else," "keep the existing code style." If AI goes beyond scope, immediately tell it to revert the extras.

Karpathy illustrated this with a diff example. Say you ask AI to add "member pricing" to a cart discount function. Good output: only that function changes, a few lines added. Bad output: the whole file is refactored — the new code might look "cleaner," but you can't be sure it didn't introduce bugs. In AI coding, "looks better" is never a reason to ignore instructions.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Bad prompt (vague scope)

{class="font-mono text-xs leading-relaxed"}
Help me optimize this project's discount logic
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Good prompt (precise scope)

{class="font-mono text-xs leading-relaxed"}
Only modify the calculate_discount function in cart.py: 1. Add member pricing on top of existing discounts 2. Members get an extra 10% off 3. Do not change the function signature or other functions 4. Keep the existing variable naming style
:::
:::

#### 4. Principle 4: Goal-Driven Execution

This principle answers a key question: should you tell AI "how to do it" or "what to do"? Karpathy's answer is the latter. Instead of "create a class, then add methods, then write tests," say "I need a tool that parses a CSV and counts unique values per column." Let AI pick the implementation path; you accept the result.

Goal-driven execution has a double payoff. AI gets room to choose the best path instead of being boxed in by your middle steps. You shift attention from "how" to "is the result right" — exactly what a conductor should do.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Note: Goal-driven ≠ hands-off

{class="mt-1"}
You still need strict acceptance after AI runs: Does the result meet the need? Are edge cases handled? Any obvious overengineering? If it's off, give specific feedback — not "redo it," but "this raises IndexError on empty list input; please add a null/empty check."
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Instruction style</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Example</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Outcome</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Imperative (how)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"First create a Python class called DataParser, add a parse method that takes filename, use the csv module to read…"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI becomes a typist; your middle steps may not be optimal</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Goal-based (what)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"I need a tool: read a CSV, count unique values per column, output JSON. Please implement it fully."</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI picks the best path; you accept the result</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Imperative vs. goal-based instructions

#### 5. Principle 5: Iterate and Verify

This is the fifth principle this book adds to Karpathy's four. Core belief: AI's first output is almost never final. Effective AI coding is a generate → verify → correct loop, not one-shot prompt → output.

"Iterate and Verify" isn't passive "try again if wrong" — it's a structured validation flow. After each AI output, verify on three levels:

- Level 1 · Functional: Does it run? Are inputs and outputs right?
- Level 2 · Boundary: What about empty, oversized, or invalid inputs?
- Level 3 · Architectural: Is the structure sound? Hardcoded values? Easy to extend later?

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-bullseye mr-1"></i> Define the goal</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> AI generates code</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Feature check</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Pass</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Edge-case check</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Pass</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-landmark mr-1"></i> Architecture review</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Passed — go to the next step</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> Fail</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Give specific feedback</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> Regenerate</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figure 2: The iterative verification loop in AI coding
:::

The key step is "give specific feedback." When verification fails, don't say "wrong, redo." Say "the function raises IndexError on empty list input; please add an empty check on line 15." Specific feedback lets AI fix precisely; vague feedback just makes it re-guess your intent.

#### 6. Harness Engineering: Agent = Model + Harness

In mid-2026, Harness Engineering started trending in the AI coding community. The core formula is simple:

:::inline div .quote-line .text-center .text-base .font-bold
<strong>An agent's capability = model capability × harness quality</strong>
:::

Model capability is the brain's intelligence ceiling; the Harness is the "work environment" around it — context management, tool integration, workflow orchestration, memory systems, and more.

This explains a common puzzle: with the same GPT-4 or Claude, why do some people ship stunning projects while others get mediocre code? The difference isn't the model — it's the harness. A good harness includes clear project spec files, sensible tool integration, organized conversation context, and solid verification flow. The model sets the ceiling; the harness decides how much of it you can use.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
The genius intern analogy

{class="mt-1"}
Think of the model as a genius intern — sky-high IQ, but without project docs, tool guidance, deadlines, and acceptance criteria, they won't ship great work. Harness Engineering is the craft of "setting up a genius intern's workspace."
:::

The rest of this book is essentially about building a good harness: Chapter 39 teaches context management (project memory), Chapter 40 requirements (PRD), Chapter 43 conversation technique (prompt layering), Chapter 45 quality assurance (verification flow). Together, that's your harness.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Hands-on: Break down your next idea with the "thinking triangle"

{class="mt-1"}
Pick a small thing you've wanted to build but never started (a countdown page, a drink-water reminder script). Spend 3 minutes answering: ① What problem does it solve? ② What should it look like done? ③ What constraints (time, tech, environment)? Write the answers as one paragraph. Congratulations — you just did your first Think Before Coding. That paragraph is a solid high-quality prompt.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Chapter recap

- Five principles from Karpathy's 70-line CLAUDE.md (70K+ Stars); this book adds "Iterate and Verify"
- Think Before Coding: Answer three questions first — what, what result, what constraints?
- Simplicity First: AI's biggest trap is building too much — a discount doesn't need an e-commerce engine
- Surgical Changes: Change with surgical precision; refuse AI's "while I'm in here" refactors
- Goal-Driven Execution: Say what, not how — let AI choose the path
- Iterate and Verify: Three-level checks (functional/boundary/architecture) + specific feedback, loop
- Harness Engineering: Ability = Model × Harness — manage AI like a genius intern's workspace
:::
