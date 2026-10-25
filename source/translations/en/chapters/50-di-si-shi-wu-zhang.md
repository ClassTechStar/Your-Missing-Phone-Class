---
id: di-si-shi-wu-zhang
num: 45
part: ai-biancheng-pian
nav: Chapter 45: Quality Assurance — Making AI-Written Code Reliable
toc: default
kind: chapter
---

### Chapter 45: Quality Assurance — Making AI-Written Code Reliable

{class="chapter-intro mb-4"}
AI-written code has a telltale trait: it usually 'looks right' — tidy variable names, thorough comments, clear logic. But 'looking right' is not the same as 'being right.' Hidden problems in AI code are often harder to catch than in hand-written code, precisely because its surface quality is so high that it lulls you into lowering your guard. This chapter shows you how to build an effective quality assurance system for AI code — three lines of defense (testing, review, and version control) to turn 'looks right' into 'is right.'

#### 1. Test-Driven: Have the AI Write the Tests

Testing is the first line of defense for quality in AI coding. The good news: having the AI write tests is easier and more reliable than having it write feature code — because a test's expected behavior is well defined, it rarely produces code that 'looks right but isn't.'

The test-driven AI coding flow: first have the AI write the feature code; once the basic functionality passes, immediately have it write test cases. The test cases should cover the normal path, boundary cases, and error cases. Then have the AI fix the feature code based on the test feedback. The beauty of this flow: once the tests are written, they become a standing verification tool — any later change can be checked by running the tests to confirm no regressions slipped in.

::: div .code-block
:::inline div .code-head
<span>Prompt for the AI: write tests</span><span class="dots">···</span>
:::

```
Write unit tests for the calculate_discount function.
The test cases should cover:
1. Happy path:
   - 100-yuan item at 20% off -> 80
   - 200-yuan item at 50% off -> 100
2. Edge cases:
   - 0-yuan item at 20% off -> 0
   - 100-yuan item at 0% off -> 100 (no discount)
   - 100-yuan item at 10% off -> 100 (full price)
3. Error cases:
   - negative price -> should throw an error
   - discount rate > 1 -> should throw an error
   - non-numeric input -> should throw an error
Use the Vitest framework and give the complete test file.
```
:::

Notice what makes this instruction work: it explicitly lists the three categories of test cases (normal, boundary, and error), leaving the AI no room to 'test selectively.' Sometimes an AI will write only happy-path tests to 'get it done fast' — spelling out every category prevents that.

#### 2. Code Review Techniques

Even with test coverage, you still need to review the AI's code yourself. Code review does not mean reading line by line — that is too slow and too dependent on your own coding skill. Effective AI code review focuses on these key dimensions:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Review Dimension</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">What to Look For</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Common Problems</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Security</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Input validation, key handling, SQL injection protection</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The AI often forgets to validate input and hardcodes keys in the code</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Error Handling</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Are exceptions caught, and are the error messages sensible</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The AI loves empty catch blocks, or just a console.log</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Performance</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Any obvious performance problems, like N+1 queries or infinite loops</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The AI sometimes writes O(n²) algorithms</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Maintainability</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Is the code structure clear, and do the names make sense</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI occasionally generates overly abstract code</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dependency management</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Whether the dependencies brought in are actually needed and their versions are explicit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI tends to pull in unnecessary libraries</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Key dimensions for reviewing AI code

When reviewing, you don't have to check everything one by one yourself — you can have the AI do the first pass. An instruction like: "Please review this code for security, error handling, and performance, and point out potential issues." AI's self-review ability keeps improving; it can't fully replace human review, but it helps you filter out most of the obvious problems.

#### III. Version Control: Git's Role in AI Coding

Git plays an even bigger role in AI coding than in traditional programming. Because every change the AI makes can introduce unpredictable shifts, you need a reliable way to undo mistakes — and version control is exactly that.

The best Git practice in AI coding is "commit often, move in small steps." Every time you finish one verifiable piece of functionality, make a commit. That way, when one of the AI's changes goes wrong, you can roll back precisely to the last working state instead of throwing away all your work.

Another handy trick is "branch isolation." For AI changes with uncertain results (like a big refactor), create a new branch first and do the work there. If you like the result, merge it back into the main branch; if not, just delete the branch and the main branch stays untouched. This is far safer than making repeated changes on the main branch.

1. Before each AI change, make sure the working area is clean (no uncommitted changes). That way, if you don't like what the AI did, you can quickly roll back with git checkout .
2. After each AI change, once it passes verification, commit right away. The commit message should describe what the change does, like "feat: add user registration".
3. For big refactors, create a branch first: git checkout -b refactor/auth-system. Finish the changes on the branch, and merge only after the tests pass.
4. Build the habit of looking at the diff. After every AI change, use git diff to see exactly what changed. This not only helps you spot problems, it also helps you learn the code.

#### IV. Common Pitfalls and How to Dodge Them

A few pitfalls show up again and again in AI coding, and almost every beginner steps into them. Knowing them in advance saves you a lot of detours.

##### 1. Pitfall One: The Trust Trap

"Code written by AI looks so professional — it must be fine, right?" This is the most dangerous trap. AI-generated code is very tidy on the surface — proper naming, complete comments, clear structure — and that "surface polish" makes people lower their guard. But a tidy surface doesn't mean the logic is correct. The antidote: always verify through testing, never judge by "does it look right."

##### 2. Pitfall Two: The Bloat Trap

"Since AI can write my code, why not make the features more complete?" That leads to code bloat. AI is great at "giving extra": ask it for a login page and it hands you a full user management system. Extra features don't just add complexity — they raise the odds of bugs too. The antidote: strictly follow the Simplicity First principle and tell the AI explicitly to "build only this feature, add nothing extra."

##### 3. Pitfall Three: The Understanding Trap

"The AI should understand what I mean, right?" Not necessarily. AI's comprehension is strong, but for vague requirements it still has to "guess." When it guesses wrong, the code it produces is wrong. Worse, code built on a wrong guess usually "looks reasonable," making you believe it understood. The antidote: put enough specific detail in your instructions to shrink the space the AI has to "guess" in.

##### 4. Pitfall Four: The Context Trap

"I said this earlier in the conversation — the AI should still remember, right?" It very likely doesn't. As conversations get longer or you start new sessions, the AI loses earlier context. If a key constraint isn't written into the project memory file, it will very likely be ignored in later changes. The antidote: write key constraints into the project memory file instead of relying on conversational memory.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
The Four Traps at a Glance

{class="mt-1"}
Trust trap — don't trust "it looks right"; Bloat trap — AI loves to "give extra"; Understanding trap — vague requirements make it "guess"; Context trap — conversational memory "forgets." The matching antidotes: verify with tests, cut the extras, give full details, write to the memory file.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Hands-On: Build Three Lines of Defense for Your Project

{class="mt-1"}
If you've already started Project One (the tool site): ① have the AI write the three types of test cases for your core functions; ② review the code against all five dimensions (security / error handling / performance / maintainability / dependencies); ③ initialize the project with git and make your first commit. With all three lines of defense in place, your project truly belongs to you.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Chapter Summary

- AI code that "looks right" ≠ "is right" — when the surface looks too good, it's easy to lower your guard
- Have the AI write tests: explicitly list the three case types (normal / boundary / error) to prevent "selective testing"
- Five review dimensions: security, error handling, performance, maintainability, dependency management
- Git is your "undo button": commit often, move in small steps, isolate with branches, check the diff often
- The four traps: Trust (verify with tests), Bloat (cut the extras), Understanding (give full details), Context (write to the memory file)
:::
