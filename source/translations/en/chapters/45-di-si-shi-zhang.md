---
id: di-si-shi-zhang
num: 40
part: ai-biancheng-pian
nav: Chapter 40: Requirements Engineering — Turning Ideas into AI Instructions
toc: default
kind: chapter
---

### Chapter 40: Requirements Engineering — Turn Ideas into AI-Ready Instructions

{class="chapter-intro mb-4"}
If context engineering helps AI understand the background, requirements engineering helps AI know what to do this time. It's where people differ most in AI coding — same tools, same models, yet some ship stunning projects while others only make mediocre toys. The gap is rarely raw technical skill; it's the ability to express requirements.

#### 1. From fuzzy idea to structured requirements

Every project starts as a fuzzy idea — "I want a budgeting app," "a personal website," "a to-do list." Nothing wrong with that, but toss it straight to AI and quality is pure luck. Requirements engineering turns that fuzzy idea into something AI can execute precisely.

Good news: structured requirements don't need a multi-page PRD. Just answer five questions — the "five requirement elements":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Element</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Question</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Example: budgeting app</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who is it for?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Personal use, tracking daily income and expenses</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What does it do?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">An app that records transactions, summarizes monthly, and visualizes spending</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why build it?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">To understand my spending structure and cut unnecessary expenses</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Roughly how?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">React frontend, data in browser localStorage, no backend or login yet</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Any constraints?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Solo developer, 2 weeks, no need to deploy publicly</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
The five requirement elements with example

You don't need a formal document for these five — even a quick mental pass is enough. The key is building the habit of "think clearly before you speak." Once you can answer these five clearly, your requirement descriptions naturally become structured.

#### 2. The art of layered requirement breakdown

For bigger projects, one requirement description isn't enough. Break the big one into small, independently verifiable sub-requirements. This is "requirement breakdown." Core rule: each sub-requirement should be completable, verifiable, and deliverable on its own.

For "build a personal budgeting app," a sensible breakdown:

1. Implement basic transaction recording (add, view, delete entries);
2. Add categories (tag entries as dining, transport, etc.);
3. Implement monthly summaries (income and expenses by month);
4. Add data visualization (charts for spending structure).

Each step is a feature increment that runs and verifies on its own.

:::inline div .quote-line
The golden rule of breaking down requirements: after every step, the project should still be a "thing that works" — even if crudely. Never let the project sit in a state where "everything is half done but nothing works."
:::

Two benefits. First, you always see progress — every step adds a feature, and that positive feedback matters for long projects (humans need wins). Second, each AI task stays small, lowering the risk of misunderstanding — smaller tasks, clearer understanding, better output.

#### 3. PRD writing template and practice

For larger projects (full-stack apps with frontend, backend, and multiple modules), the five elements may not be enough. You'll need a more formal PRD. One common misconception: a PRD is not for AI to read — it's for you, to clarify your thinking so you can give AI more precise instructions.

A good PRD doesn't need to be long, but should cover six parts: project overview (one paragraph on what it is), feature list (each feature defined), technical plan (stack and rough architecture), data model (core structures), interface description (what main screens look like), and development plan (steps to finish).

::: div .code-block
:::inline div .code-head
<span>PRD.md</span><span class="dots">···</span>
:::

```
# Personal finance tracker PRD
## Project overview
A lightweight personal finance tracker supporting income/expense records, categories, monthly summaries and data visualization.
## Feature list
1. Record income/expenses: amount, type (income/expense), category, note, date
2. Category management: presets for food, transport, shopping, entertainment, other
3. Monthly summary: total income, total expenses and balance by month
4. Spending visualization: a pie chart of each category's share
5. Data export: export as CSV
## Technical approach
- Frontend: React + TypeScript + Tailwind CSS
- Data storage: localStorage (no backend needed)
- Charts: Chart.js
- Build: Vite
## Data model
Record {
  id: string
  amount: number
  type: 'income' | 'expense'
  category: string
  note: string
  date: string  // YYYY-MM-DD
}
## Development plan
Step 1: basic record features (CRUD)
Step 2: category management
Step 3: monthly summaries
Step 4: data visualization
Step 5: data export
```
:::

Note the writing style: concise lists and structured formatting instead of long essays. Each feature has a clear definition; data models use simple type descriptions. This style is easy for you to read and easy for AI to understand precisely when you hand it over.

#### 4. Hands-on: full walkthrough from idea to plan

Theory is boring — let's walk through a complete requirements engineering example. Suppose your idea is: "I want a study tracker that records what I learned each day."

Step 1: Run through the five requirement elements.

- Who: Personal use.
- What: A tool that records daily study content, tracks study time, and reviews progress.
- Why: Build a consistent study habit and see the accumulation.
- How: Start with a web version, data in browser localStorage.
- Constraint: Beginner developer, core features done in 1 week.

Step 2: Break down the requirements.

1. Step 1: Implement "record study entries" (date, content, duration);
2. Step 2: Add "study time stats" (today, this week total);
3. Step 3: Implement a "study calendar" view (like a GitHub contribution graph);
4. Step 4: Add "study review" (randomly show a past day's entries for revision).

Step 3: Write a short PRD. It doesn't need to be long — the breakdown above is already the PRD body. Organize it into a .md file in the project root as the shared reference for you and AI.

Step 4: Start developing the first step. A prompt to AI could be:

::: div .code-block
:::inline div .code-head
<span>Prompt for the AI</span><span class="dots">···</span>
:::

```
I need the first feature of a learning tracker — logging learning entries.
The user can add a learning record with the date, what was studied and the duration in minutes.
Data is stored in localStorage.
The frontend uses React + TypeScript.
Please give a complete implementation.
```
:::

Notice the prompt's traits: it describes only the current step's goal (recording), without other features mixed in; it states technical constraints (React, TypeScript, localStorage); it gives enough info for AI to know "what" and "how roughly," while leaving implementation details to AI. That's a high-quality AI coding prompt after requirements engineering.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Hands-on: Write a five-element card for your pet project

{class="mt-1"}
Pick a small project you've been brewing and spend 5 minutes filling a card: Who / What / Why / How / Constraint, one sentence each. Then break it into 3–5 steps where each step is "usable on its own." You'll find that once written down, the idea turns from a daydream into a to-do list.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Chapter recap

- Five requirement elements: Who / What / Why / How / Constraint — think before you speak
- Golden rule of breakdown: after every step the project is "something that works"
- A PRD is for you: overview, features, technical plan, data model, UI, plan
- Good prompt = only the current step + clear constraints + what, not how
- Full walkthrough template: five elements → breakdown → PRD → prompt — four steps
:::
