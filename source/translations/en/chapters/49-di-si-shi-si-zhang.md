---
id: di-si-shi-si-zhang
num: 44
part: ai-biancheng-pian
nav: Chapter 44: Hands-On from 0 to 1 — A Complete Project, Start to Finish
toc: default
kind: chapter
---

### Chapter 44: From 0 to 1 — A Complete Project, End to End

{class="chapter-intro mb-4"}
The theory is done; now it is time to get your hands dirty. This chapter is not a simple 'type along' tutorial but a practical methodology covering how to think, how to ask, and how to verify. Using three projects of rising difficulty, we will show the complete thought process from requirements to finished product. No matter which tool you use, this workflow applies.

#### 1. Project 1: A Minimal Personal Tools Site (Beginner)

##### 1. Thinking Through the Requirements

Goal: build a personal tools page that shows entry points to 3-4 handy little tools. This is a pure front-end project — no back end and no database needed. The point is not how fancy the tools are but experiencing the full 'from requirements to finished product' process.

Applying the five requirement elements: Who — personal use. What — a web page showing tool entry points. Why — gather your frequently used tools on one page for easy access. How — a single-file HTML+CSS+JS build with no frameworks. Constraint — finish within 30 minutes, no deployment needed.

##### 2. Giving the Instruction

Following the Think Before Coding principle, your instruction should carry enough information for the AI to understand the goal, without specifying every implementation detail:

::: div .code-block
:::inline div .code-head
<span>Prompt for the AI</span><span class="dots">···</span>
:::

```
Please create a personal toolbox web page with these requirements:
1. Single-file HTML (inline CSS and JS), no frameworks
2. Dark theme, modern minimalist style
3. Show 4 tool entry cards:
   - Text summarizer
   - Word counter
   - Color picker
   - QR code generator
4. Each card has an icon, a title and a short description
5. Cards have a hover animation
6. Responsive layout, usable on phones
7. A title bar at the top
Please give the complete HTML file directly.
```
:::

##### 3. Acceptance and Iteration

Once the AI hands over code, accept it using the three-layer check from iterative verification. First layer, functional check: does the file open in the browser? Do all 4 cards display? Do the hover animations work? Second layer, edge-case check: does the layout hold up at phone screen sizes? Do the cards wrap when the window gets narrow? Third layer, architecture check: is the code readable? Is the CSS inlined in a single style tag? Is there obvious redundancy?

If you want one of the tool cards to actually work (rather than just be an entry point), add it gradually — implement one tool's functionality, verify it, then add the next. That is the 'small quick steps' strategy in action.

#### 2. Project 2: A Full-Stack Expense Tracker (Intermediate)

##### 1. Requirements Thinking and the PRD

Goal: a full-stack expense-tracking app with a front end, a back end, and a database. This project is far more complex than the first and calls for the requirements engineering method from Chapter 40.

Start by writing the PRD. Following the template from Section 3 of Chapter 40, lay out the project overview, feature list, technical plan, data model, and development plan. When choosing the tech stack, apply the Simplicity First principle — React on the front end but no complex state management like Redux; Node.js on the back end but no microservices; SQLite instead of PostgreSQL for the database (during development).

Break the development plan into 5 steps: Step 1, the back-end API skeleton (an Express server + SQLite + CRUD endpoints); Step 2, the basic front-end pages (a records list + an add form); Step 3, hooking the front end to the back end (API calls + data display); Step 4, categories and filtering; Step 5, monthly summaries and simple charts. After every step you have 'something that works.'

##### 2. Setting Up the Project Memory File

Before any coding begins, create the project memory file. This is a core context engineering practice — it gives the AI the project background at the start of every conversation.

::: div .code-block
:::inline div .code-head
<span>CLAUDE.md</span><span class="dots">···</span>
:::

```
# Project: full-stack finance tracker
## Overview
A personal finance tracker with income/expense records, categories and monthly summaries.
## Tech stack
- Frontend: React + TypeScript + Vite
- Backend: Node.js + Express + TypeScript
- Database: SQLite (via better-sqlite3)
- Shared type definitions for frontend and backend
## API conventions
- Base path: /api
- Response format:{ success: boolean, data: any, error: string }
- RESTful style
## Data model
Record { id, amount, type, category, note, date }
## Code style
- TypeScript strict mode
- 2-space indentation
- Functions have JSDoc comments
- Comments and commit messages in English
```
:::

##### 3. Building It Step by Step

Follow the development plan, completing each step in its own separate conversation. Here is a sample instruction for the first step:

::: div .code-block
:::inline div .code-head
<span>Prompt for the AI (Step 1)</span><span class="dots">···</span>
:::

```
I need a backend API skeleton.
Requirements:
1. Express server, port 3001
2. SQLite database, table name records
3. Fields of the records table:
   id (TEXT PRIMARY KEY)
   amount (REAL)
   type (TEXT: 'income'|'expense')
   category (TEXT)
   note (TEXT)
   date (TEXT: YYYY-MM-DD)
4. CRUD endpoints:
   GET /api/records - get all records
   POST /api/records - add a record
   PUT /api/records/:id - update a record
   DELETE /api/records/:id - delete a record
5. Error-handling middleware
Please give the complete backend code structure.
```
:::

Notice what makes this instruction work: it describes only the current step (the back-end skeleton) without mixing in front-end requirements; it explicitly lists the fields and endpoints (giving the AI firm constraints) while leaving the concrete implementation to the AI; and it follows the Goal-Driven Execution principle — saying 'what to do' rather than 'how to do it.'

As soon as the AI hands over code, verify it immediately: run the server and test each endpoint with curl or Postman. Once everything checks out, open a new conversation for Step 2 (the basic front-end pages). Every step follows the 'instruct - verify - new conversation' loop.

#### 3. Project 3: An AI-Powered App (Advanced)

##### 1. Conceiving the Project

Goal: an app that connects to a large model API — say, an 'AI Study Assistant' where the user enters study material and the AI generates a summary, links related concepts, and recommends learning resources. What makes this project special: your application itself is calling the AI, so you have to handle new problems like API calls, prompt engineering, and error handling.

The most important lesson this project teaches: when you 'use AI to write code that calls AI,' you must pay extra attention to prompt engineering. The prompt your app sends to the large model API also needs to follow the principles discussed in this guide — clear, concise, and goal-driven.

##### 2. Key Technical Points

This project involves a few technical points you did not meet in the first two projects:

- API key management: keys must never be hardcoded in the code; manage them with environment variables;
- Streaming response handling: large model replies usually arrive as a stream and need to be displayed bit by bit;
- Token usage control: large models bill by the token, so usage must be controlled at the application level;
- Prompt template management: different features use different prompt templates, which need to be managed in a structured way.

The AI can help you implement all of these technical points, but you need to understand the 'why' behind each one — why can't keys be hardcoded? Why are streaming responses needed? Why must token usage be controlled? Only once you understand the 'why' can you judge whether the AI's solution makes sense.

#### 4. The Universal Hands-On Checklist

Whatever the size of the project, here is a universal AI coding workflow checklist. Run through it every time you start a new project to make sure no key step slips through.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Stage</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">What to Do</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Principle Applied</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1. Requirements thinking</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Go through the five requirement elements and get clear on what to build</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Think Before Coding</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2. Breaking down requirements</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Split big requirements into small, independently verifiable steps</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Simplicity First</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3. Writing the PRD</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Organize it into a structured document for reference</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Goal-Driven</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">4. Setting up the memory file</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Create CLAUDE.md or a similar file</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Harness Engineering</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">5. Building step by step</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">One conversation per step: instruct - verify - next</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Surgical Changes</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6. Testing and verifying</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Test that each step works correctly right after finishing it</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">7. Reviewing the code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Check architecture soundness, security, and maintainability</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8. Iterating and improving</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate based on the test and review results</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
The Universal AI Coding Workflow Checklist

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Try It Yourself: Finish 'Project 1' This Week

{class="mt-1"}
Treat the 'personal tools site' from Section 1 of Chapter 44 as your first AI coding assignment: spend 5 minutes on the five elements, send the instruction to the AI (any tool will do), then accept the result with the three-layer verification. Finish it within 30 minutes — and your first AI coding creation is born. When you are done, save it somewhere safe; it is the keepsake of your move from 'reader' to 'practitioner.'
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Chapter Recap

- Project 1 (beginner): a pure front-end tools site — experience the full workflow, done in 30 minutes
- Project 2 (intermediate): a full-stack expense tracker — PRD + memory file + 5 steps, with something that 'works' at every step
- Project 3 (advanced): an AI study assistant — use AI to write code that calls AI, with attention to prompt engineering
- The universal eight-step workflow: requirements thinking → break down → PRD → memory file → build step by step → test → review → iterate
- Every step follows the 'instruct - verify - new conversation' loop
:::
