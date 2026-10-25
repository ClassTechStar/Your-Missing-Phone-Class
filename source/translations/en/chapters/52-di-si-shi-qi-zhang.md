---
id: di-si-shi-qi-zhang
num: 47
part: ai-biancheng-pian
nav: Chapter 47: Quick Reference and Resources
toc: default
kind: chapter
---

### Chapter 47: Quick Reference and Resources

{class="chapter-intro mb-4"}
This chapter is a quick-reference manual that works on its own. When you can't quite remember a principle or need to make a fast decision, flip straight here. Treat it as a "pocket card": the five principles at a glance, a tool decision tree, common questions, and learning resources — every page included.

#### I. Mental Model Cheat Sheet

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Principle</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">In One Sentence</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Key Actions</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Think Before Coding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Think It Through Before Asking</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Answer three questions: What to build? What should the result look like? What are the constraints?</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Simplicity First</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Solve Problems with the Least Code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">One feature at a time, and cut unnecessary complexity</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Surgical Changes</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Precise Changes, No Overstepping</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Specify the change scope explicitly and refuse the AI's "let me fix that too" edits</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Goal-Driven Execution</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Say What, Not How</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Give the goal, not the steps, and let the AI pick its own path</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Generate-Verify-Fix Loop</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Three-layer verification: functionality, boundaries, architecture</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Cheat Sheet: The Five Thinking Principles

#### II. The Tool-Choice Decision Tree

When you need to pick an AI coding tool, follow the decision path below. Note: this isn't a ranking of "which is best" — it's a framework for judging "which is best for you."

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-question-circle mr-1"></i> What do you want to do?</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Total beginner, want a quick taste → pick a cloud Builder (v0/Bolt/Replit)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Everyday development, need code completion → pick an IDE with built-in AI (Cursor/Trae)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Large projects, need bulk operations → pick a terminal Agent (Claude Code)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Validate an idea with a quick prototype → pick a cloud Builder or Trae SOLO</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figure 6: Decision tree for choosing an AI coding tool
:::

#### III. FAQ: Common Questions

Q1: I don't know how to program at all — can I still do AI coding?

Yes. AI coding tools in 2026 are strong enough that you can describe what you want in plain language and have the AI generate the code. Two suggestions: first, start with cloud Builder tools (like v0 and Bolt), which need no development environment setup; second, learn basic concepts as you go — you don't need to master the syntax, but you do need to "read" the general meaning of the code the AI writes, so you can check its work effectively.

Q2: Which programming language should I learn?

It depends on what you want to build. Website front end — JavaScript/TypeScript; data processing or AI — Python; enterprise back end — Java or Go. But more importantly: in the AI coding era, the importance of "which language" is falling. AI can handle the syntax details for you; what you need to understand is "the structure of programs" — what a function is, what a loop is, what a data structure is. These concepts carry across languages, and once you understand them, picking up any language is fast.

Q3: Is there a copyright issue with AI-written code?

As of August 2026 this is still a contested legal question. Generally speaking, AI-generated code isn't considered to have a clear copyright owner in most jurisdictions. But if you're using it in a commercial project, it's wise to: ① check the intellectual property terms in the terms of service of the AI tool you use; ② review and modify key code yourself so it carries your own creative input; ③ avoid having the AI directly copy open-source code that may be copyrighted.

Q4: Will AI replace programmers?

Not in the short term. What AI replaces isn't the "programmer" as a profession but the task of "coding line by line." Just as the calculator didn't replace mathematicians — it freed them from tedious hand computation. AI coding tools shift programmers from "writing code" to "thinking through problems" — which actually raises the ceiling on a programmer's value. Future competitiveness won't lie in "how many lines of code you can write" but in "how complex a problem you can solve."

Q5: How do I judge whether the AI's output is correct?

Use the three-layer verification method. Layer one: functional verification — does it run? Are the inputs and outputs right? This is the most basic. Layer two: boundary verification — what happens with empty input, extra-long input, weird input? This surfaces hidden problems. Layer three: architecture verification — is the code structure sound? Any hard-coded values? Is it easy to extend? This takes some technical judgment of your own. If you can't judge layer three, at least do the first two — running fine with sane boundaries already puts you ahead of most beginners.

#### IV. Recommended Learning Resources

Below are the recommended learning resources as of August 2026. Keep in mind that internet links change; if a link is dead, searching its title usually turns up the latest version.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Type</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Resource</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Why It's Recommended</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Primary Source</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Andrej Karpathy's CLAUDE.md</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The source of the five principles — 70 lines where every word counts</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Primary Source</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Anthropic official docs (Claude Code)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The best-practices guide for terminal agents</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tutorial</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A Skills collection curated by the Vibe Coding community</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Battle-tested tips compiled by community practitioners</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tutorial</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor official docs and YouTube channel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The authoritative guide to AI built into an IDE</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Community</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">awesome-claude-code on GitHub</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Best practices and plugin collections for Claude Code</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Community</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The r/cursor community on Reddit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Experience sharing and discussion from Cursor users worldwide</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Basics</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MDN Web Docs (developer.mozilla.org)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The most authoritative reference for front-end development</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Basics</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The official Python tutorial (docs.python.org)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The official starting point for learning Python</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Recommended Learning Resources List

#### V. Closing Thoughts: Tools in Hand, Methodology in Mind

Let's come back to this book's core belief: tools iterate every three months; methodology evolves only every three years. Today, in August 2026, AI coding tools are astonishingly powerful — you can create a website with one sentence, generate a full-stack app from a short description, finish a complex refactor with a single instruction. But the more powerful the tools, the more methodology stands out — because powerful tools amplify every one of your decisions.

If your requirements are clear, AI helps you build them efficiently; if they're vague, AI efficiently builds the wrong thing. If you follow Simplicity First, AI helps you validate ideas quickly; if you want everything at once, AI quickly piles up technical debt for you. If you make precise changes, AI optimizes your code with surgical precision; if your instructions are fuzzy, AI boldly introduces bugs for you.

That's why this book spent most of its pages on methodology rather than tool operations. Not because tools don't matter, but because methodology is the tool's "multiplier" — the better your methodology, the more your tools are worth; with zero methodology, even the strongest tool is just zero times anything.

:::inline div .quote-line
You're no longer coding alone. You are the commander and AI is your army; the quality of your thinking determines your army's fighting power. From today, arm your mind with methodology and amplify your ability with tools — that's the whole secret of AI coding.
:::

#### References

{class="list-decimal pl-6 mb-3 space-y-1 text-xs text-gray-500"}
1. Andrej Karpathy. (2025). Vibe Coding. Social media post introducing the concept of vibe-driven programming with AI.
2. Andrej Karpathy. (2025). CLAUDE.md - Project guidelines for AI-assisted development. GitHub repository, 70+K stars.
3. Anthropic. (2026). Claude Code: Terminal-native AI programming. Official documentation and best practices.
4. Cursor Team. (2026). Cursor 3: The next generation of AI-first IDE. Release notes and documentation.
5. OpenAI. (2026). Codex CLI: Bringing AI to the terminal. Technical documentation.
6. Model Context Protocol (MCP) Specification. (2025-2026). Open protocol for AI-tool integration.
7. Vibe Coding Community. (2026). Community-curated skills and best practices for AI-assisted programming.
8. Spec-Driven Development (SDD) methodology. (2026). Emerging practices in specification-first AI programming.
