---
id: di-san-shi-jiu-zhang
num: 39
part: ai-biancheng-pian
nav: Chapter 39: Context Engineering — Helping AI Understand Your Intent
toc: default
kind: chapter
---

### Chapter 39: Context Engineering — Make AI Understand You

{class="chapter-intro mb-4"}
Ever open a new chat and watch AI forget everything about your project? It's not messing with you — it's just forgetful by design. This chapter teaches you to install a "long-term memory system" for AI, and introduces one of 2026's hottest development paradigms: Spec-Driven Development.

#### 1. Project memory files: AI's long-term memory

AI models have a fundamental limit: their memory is short-term. At the start of every conversation, AI knows nothing about your project. You'd have to keep saying "we use React," "backend is Node.js," "database is PostgreSQL," "code style uses double quotes." That's inefficient and easy to miss — like onboarding a new colleague every single day.

The fix is a project memory file — a plain text file in the project root that AI tools auto-read at the start of each conversation. Different tools use different names:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tool</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">File name</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cursorrules</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">CLAUDE.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitHub Copilot</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">copilot-instructions.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Generic option</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">AGENTS.md</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Project memory file naming conventions by tool

Names differ, but the idea is the same: write down what you want AI to always remember. A good project memory file includes: project overview (what this is), tech stack (what you're using), code conventions (naming, indentation, comments), directory layout (how code is organized), and development practices (branch strategy, commit style, testing). Karpathy's CLAUDE.md is only 70 lines but covers all key info — concise and complete.

::: div .code-block
:::inline div .code-head
<span>CLAUDE.md</span><span class="dots">···</span>
:::

```
# Project: personal finance tracker
## Overview
A full-stack personal finance tracker that helps users record daily income and expenses.
## Tech stack
- Frontend: React + TypeScript + Tailwind CSS
- Backend: Node.js + Express + TypeScript
- Database: SQLite (dev) / PostgreSQL (production)
- Testing: Vitest
## Code style
- Use double quotes
- 2-space indentation
- Function names in camelCase
- Type definitions in PascalCase
- Every function must have a JSDoc comment
## Directory structure
/src
  /frontend  - frontend code
  /backend   - backend code
  /shared    - types shared by frontend and backend
  /tests     - test files
## Development conventions
- Commit messages in English
- New features must have tests written first
- APIs always return { success, data, error }
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Note: Don't turn it into a second requirements doc

{class="mt-1"}
Watch the length — don't write a multi-page requirements document. The purpose is to help AI build background context quickly, not to describe every feature in detail. Keep it concise, structured, and limited to what AI needs to know.
:::

#### 2. Spec-Driven Development (SDD)

Spec-Driven Development (SDD) is a 2026-era paradigm with one core idea: write the spec first, then the code. Unlike classic TDD (test-driven development), SDD "specs" aren't just test cases — they include requirement descriptions, interface definitions, data models, and more. AI generates code from those specs; humans write and maintain the specs.

SDD workflow in five steps:

1. Describe the requirement spec in natural language (in a .md file);
2. Define interfaces and data structures (in the spec file);
3. Have AI generate code from the spec;
4. Run tests to verify the output matches the spec;
5. If it doesn't match, fix the spec or have AI fix the code.

In this flow, the spec file is the single source of truth — code can be regenerated, but the spec must be right first.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Write the spec file</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Is the spec complete?</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Complete</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> AI generates code from the spec</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Run tests to verify the output</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> Incomplete / tests fail</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-tools mr-1"></i> Code problem → fix the code; spec problem → fix the spec</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> Back to verification</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> All pass → deliver</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figure 3: Spec-Driven Development (SDD) workflow
:::

SDD's advantage: specs are more stable than code. When models or tools change, your spec file stays valid — just have the new AI tool regenerate the code. That's why this book insists methodology beats tools: the spec file is the concrete carrier of your methodology.

#### 3. Context window management

Even with a project memory file, you'll still hit "not enough context." AI context windows (how much info they can handle at once) are limited. When a chat gets too long or pulls in too many files, AI "forgets" early info and quality drops — like chatting with a friend for six hours and them forgetting the first thing you said.

The core strategy for context windows is layered referencing:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Context layer</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Content</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">How to manage</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Layer 1: Project memory</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tech stack, conventions, directory structure</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Written in CLAUDE.md etc., auto-loaded — no need to repeat</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Layer 2: File references</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Code files for the current task</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Reference precisely with @; don't paste entire files into chat</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Layer 3: Conversation context</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Chat history for the current task</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Start a new chat after finishing a task to avoid context bloat</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Layer 4: Immediate instructions</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Specific requirements for the current step</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Clear, concise, targeted — avoid long-winded descriptions</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Layered context window management

#### 4. Practical tips for context engineering

Context engineering isn't a one-time setup — it's ongoing tuning. Here are tips proven over and over in practice:

1. Keep the memory file in sync with the project. When you add a new technology or change the architecture, update the memory file right away instead of explaining it ad hoc in chat.
2. Prefer @ references over pasting whole files. Most AI coding tools support @file or @folder syntax and inject content in the background — more efficient and cleaner than manual paste.
3. Keep chats short and focused. One conversation handles one task or one feature. Start a new chat for the next one. Long chats burn context and make AI "distracted."
4. Show AI the result, don't just describe it. When you hit a bug, @-reference the raw error log instead of saying "there's some error." AI works better with original information than your paraphrase.
5. Clean up and archive regularly. Finished chats and temp files clutter the workspace. Cleaning them keeps the project tidy and helps AI understand the structure faster.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Hands-on: Write a 70-line memory file for your project

{class="mt-1"}
Pick a project you're doing (or planning) and write a CLAUDE.md: project overview (2–3 sentences), tech stack (list it), code conventions (3–5 rules), directory structure (draw a tree), dev practices (2–3 items). Keep it under 70 lines — you'll find your own understanding of the project sharpens too.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Chapter recap

- AI memory is short-term: every new chat starts at zero project knowledge
- Project memory files (CLAUDE.md etc.) are AI's long-term memory, auto-loaded each chat
- Good memory file = overview + stack + conventions + layout + practices — 70 lines is plenty
- SDD: spec first, then code. The spec is the single source of truth and more stable than code
- Four context layers: project memory → @file references → chat history → immediate instructions
- Five practical tips: keep in sync, use @, keep chats short, show raw info, clean up regularly
:::
