---
id: di-er-shi-san-zhang-github
part: chao-yue-pian
nav:  Appendix: GitHub Getting Started Guide
toc: sub
kind: chapter
---

### Chapter 23 Appendix: GitHub Beginner's Guide—From Code Hosting to Collaboration Platform

{class="chapter-intro mb-4"}
Chapter 23 Appendix: GitHub Beginner's Guide—From Code Hosting to Collaboration Platform

#### 1. What Exactly Is GitHub?

1\. What Exactly Is GitHub?<strong>Simply put, GitHub is a</strong> based on Git. It launched in 2008, was acquired by Microsoft in 2018, and remains the world's largest open-source code hosting platform, hosting hundreds of millions of repositories covering almost all mainstream programming languages.

If you use an analogy to understand:<strong>Git is the diary on your computer, and GitHub is a public blogging platform</strong>—you can publish your work, follow others' projects, and participate in discussions and collaboration. It's not just a "programmer's back-end repository," but more like a "technology city" built by global developers together—projects are born here, iterated, discussed, and reused.

For ordinary people, GitHub is not out of reach either. Many non-programmers use it to host notes, e-books, personal blogs, and even to back up configuration files. As long as you have a slight need to "organize your things and share them," GitHub is worth knowing about.

#### 2. The Difference Between Git and GitHub (Key Concepts!)

Many people confuse these two terms when first encountering them; let me clarify for you:

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Comparison Item</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Git</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GitHub</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nature</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Version control tool (software)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Code hosting platform (website)</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Running location</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">On local computer</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">In the cloud (browser access)</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Core responsibility</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Record every change to files (what changed, who changed it, when)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Put Git repositories in the cloud for easy storage, display, and collaboration</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Network required?</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Not required, works offline</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Requires internet access</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ownership</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Open source software, created by Linus Torvalds (father of Linux)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Microsoft product</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Similar competitors</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SVN, Mercurial</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitLab, Gitee, Bitbucket</td>
                            </tr>
                        </tbody>
                    </table>
```

Simply put:<strong>Git manages "how to record changes," GitHub manages "where changes are stored and how to collaborate"</strong>. Git is a tool that runs locally; GitHub is a platform that puts Git repositories in the cloud for easy collaboration and display. You can use Git without GitHub (such as doing version management for your own code), but using GitHub requires using Git (because GitHub is based on Git).

#### 3. GitHub's Core Concepts and Features

##### 📁 Basic Concepts

Before getting started, first get to know a few high-frequency words, otherwise you'll be confused when looking at GitHub's interface:

- <strong>Repository (Repo for short)</strong>: One project corresponds to one repository, which stores all the code files, historical versions, and documentation for that project. You can think of it as a "project folder."
- <strong>Commit</strong>: A record of one modification to the code. Each Commit comes with a description, recording "what was changed this time, why it was changed." This is the foundation of Git/GitHub's ability to "time travel."
- <strong>Branch</strong>: An independent development line split from the main line. For example, if you want to add a new feature, you can open a branch to develop separately, and merge it back to the main line after development, without affecting others.
- <strong>Clone</strong>: Copy a complete version of the cloud repository to your local computer, after which you can modify the code locally.
- <strong>Push/Pull</strong>: Push is uploading local code to GitHub, Pull is downloading the latest code from GitHub to local. These are the two core actions for syncing code during team collaboration.
- <strong>Pull Request (PR for short)</strong>: When you've finished modifying code on a branch and want to merge it into the main branch, you initiate a PR, letting team members review the code before merging. This is GitHub's core collaboration mechanism.
- <strong>Issue</strong>: Used to record bugs, feature requests, and discussion topics. Each Issue is like a discussion thread, where you can assign responsible persons and add labels.
- <strong>Fork</strong>: Copy someone else's repository to your own account, where you can modify your copy freely without affecting the original repository. After modifications, you can send a PR to the original author, requesting to merge your improvements.

##### 🛠️ Core Features

GitHub provides more than just code storage, including:

- <strong>Version control</strong>: Records the history of every code change; if you break the code, you can always return to the last working version.
- <strong>Team collaboration</strong>: Supports parallel development of the same project by multiple users; multiple people developing simultaneously won't overwrite or conflict.
- <strong>Issue tracking</strong>: Use Issues to record bugs and feature requests, making it easy for teams to follow up.
- <strong>Project management</strong>: Integrates to-do items, project boards (Projects), and other management tools, equivalent to a built-in lightweight Trello.
- <strong>Automation</strong>: Through <strong>GitHub Actions</strong>, achieve automatic compilation, testing, packaging, and deployment after code submission—the core tool of modern "CI/CD (Continuous Integration/Continuous Deployment)."
- <strong>Documentation management</strong>: README introduces the project, Wiki stores detailed architecture and development standards, and Pages can even directly host static websites.
- <strong>Code hosting and display</strong>: Each repository has a beautiful web display with syntax highlighting—it's the "front door" of your technical work.
- <strong>Open source community</strong>: You can Star (favorite) projects you like, Watch (follow) project updates, Follow (follow) developers, and participate in global open source collaboration.

#### 4. Registration and Getting Started: Create Your First Repository in Five Minutes

##### 📝 Register an Account

1. Visit<a href="https://github.com" class="text-primary hover:underline" target="_blank" rel="noopener">github.com</a>and click "Sign up."
2. Fill in your email, set a password and username (the username will appear in your personal homepage address; English is recommended, such as<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">github.com/yourname</code>).
3. Complete email verification and human verification.
4. Select the Free plan, which is completely sufficient for individual users.

##### 📁 Create Your First Repository

1. After logging in, click the "+" in the top right corner and select "New repository."
2. Fill in the repository name, such as<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">my-first-project</code>.
3. Write a short description so others know what this repository is for.
4. Choose Public or Private. Public repositories are visible to everyone; Private is only visible to you and collaborators. Free accounts also support unlimited private repositories.
5. Check "Add a README file"—README is the project's "instruction manual," recommended for every repository.
6. Click "Create repository," and your first GitHub repository is born!

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>.

{class="mt-1"}
README.md is a Markdown format file that is the first thing people see when they open your repository. A good README usually includes: project introduction, installation method, usage examples, license, and contact information. Writing a good README is a basic quality of programmers and the first threshold for whether a project can be used by others.
:::

#### 5. Basic Workflow: From Local to Cloud

To understand GitHub's workflow, the core is to remember this cycle:<strong>local modification → staging → commit → push → cloud update</strong>. Below, each step is explained in plain language:

1. <strong>Modify files</strong>: Write code or modify documents using an editor on your local computer.
2. <strong>git add</strong>: Add the modified files to the "staging area," equivalent to telling Git "I'm ready to record these changes."
3. <strong>git commit</strong>: Formally record the changes in the staging area as a "commit," with a description, such as "fix login bug." This step is only done locally.
4. <strong>git push</strong>: Upload local commits to GitHub cloud, so others can see them.
5. <strong>git pull</strong>: Before starting work, first pull the latest code from the cloud to ensure you're in sync with the rest of the team.

For beginners, remember this mnemonic:<strong>"Pull first then modify, add after modifying, commit with description, finally push up"</strong>. Develop this habit, and team collaboration won't be chaotic.

#### 6. Team Collaboration Process: How Pull Request Works

GitHub's most powerful aspect is its collaboration mechanism. A typical team collaboration process goes like this:

1. <strong>Open a branch</strong>: Open a new branch from the main branch (usually called main or master), such as<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">feature/login</code>, and develop new features on this branch.
2. <strong>Develop and commit</strong>: Write code on the new branch, with multiple commits to record progress.
3. <strong>Push to GitHub</strong>: Push the branch to the cloud repository.
4. <strong>Initiate Pull Request</strong>: Initiate a PR on the GitHub webpage, requesting to merge your branch into the main branch. Clearly state what changes this PR makes and why.
5. <strong>Code Review</strong>: Team members review your code, offering feedback or suggesting changes. You can continue to commit based on feedback, and the PR will automatically update.
6. <strong>Merge</strong>: After review passes, click "Merge" to merge the code into the main branch. Your contribution is officially part of the project!

This process ensures that <strong>all code is reviewed before entering the main branch</strong>, greatly reducing the chance of errors. Open source projects also use this mechanism to accept contributions from strangers worldwide—you can completely submit a PR to a well-known open source project, and once adopted, you become a contributor to that project.

#### 7. GitHub's Typical Application Scenarios

##### 🎓 Students Participating in Competitions and Course Projects

Computer science students participating in ACM, hackathons, and graduation designs almost all can't do without GitHub. It serves both as a team collaboration platform and as a showcase for work—competition judges can directly view your repository to understand code quality and the collaboration process. Many companies also require attaching a GitHub homepage when recruiting, as proof of technical ability.

##### 📚 Personal Knowledge Base and Note Hosting

Non-programmers can also use GitHub. Many people use it to host study notes, technical blogs (combined with GitHub Pages for free website building), and e-books. Markdown writing + Git version management + cloud backup, all in one.

##### 🌐 Participating in Open Source Projects

GitHub is the core base of the global open source movement. You can Fork projects you like, modify them and send PRs to give back to the community; or simply Star to favorite good projects and track updates. Participating in open source is an excellent way to improve your skills and build reputation.

##### 🤖 Automated Deployment and CI/CD

With GitHub Actions, you can achieve a fully automated process of "code pushed, automatically tested + automatically deployed to server." Many personal blogs and documentation sites are built this way—after writing an article, just push, and the website automatically updates.

##### 💾 Code Backup and Multi-Device Sync

Use code repositories as cloud drives; when changing computers or working on multiple devices, just git pull to get the latest code—no more USB drive copying back and forth.

#### 8. Advice for Beginners

- <strong>Write clear commit descriptions</strong>: Don't write useless descriptions like "update." A good commit message says "fix the issue of jumping to the wrong page after user login"—half a year later, you'll still know what you did.
- <strong>Commit frequently, take small steps</strong>: Commit once for each small feature completed, rather than writing all day before committing once. This makes it easier to locate problems.
- <strong>Develop on branches, don't directly modify the main branch</strong> Even for personal projects, develop the habit of opening branches, so you won't be flustered when collaborating on teams in the future.
- <strong>Make good use of .gitignore</strong>: This file tells Git which files not to include in version management (such as password configs, build artifacts, dependency folders), avoiding uploading junk files.
- <strong>Look at excellent open source projects more</strong>: Browse GitHub Trending, look at the code structure, README writing, and collaboration process of high-star projects—it's the fastest free way to improve.
- <strong>Apply for GitHub Student Pack</strong>: After student verification, you can get free access to many paid tools and services (Copilot, domains, cloud services, etc.), worth thousands of dollars.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Security Reminder

{class="list-disc pl-6 mt-1 space-y-1"}
- Never commit sensitive information like passwords, API keys, database connection strings to GitHub, especially public repositories—once leaked, they'll be scraped by crawlers in seconds, with serious consequences.
- If you accidentally commit sensitive information, just deleting the file isn't enough (it's still in the history); use<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git filter-branch</code> or professional tools to clean history, and immediately change the leaked keys.
- Private repositories aren't absolutely secure either; sensitive information is best managed with environment variables, not in code repositories.
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Notes on Accessing GitHub from Within China

{class="mt-1"}
GitHub access from within China is sometimes unstable, with situations like not opening or slow cloning. You can try: ① Use domestic mirror sites (such as GitClone, ghproxy) to accelerate cloning; ② Configure Hosts or use a proxy; ③ If mainly for domestic collaboration, you can also consider the domestic alternative <strong>Gitee</strong>, which has similar features and fast access. Many teams host on both GitHub and Gitee simultaneously, balancing internationalization and domestic speed.
:::

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Advanced Technique: Build a Free Personal Blog with GitHub Pages

{class="mt-1"}
GitHub Pages allows you to host a static website for free. Combined with static site generators like Jekyll, Hexo, and Hugo, you can easily build a personal blog. After writing a Markdown article and pushing to the repository, the blog automatically updates, with HTTPS and custom domain names included. Countless tech bloggers' blogs are built this way—zero cost, no ads, version controllable.
:::

#### 9. Summary: Why Everyone Should Understand GitHub

GitHub has long been more than just "a programmer's tool"; it's more like a <strong>way of working in the digital age</strong>: version management makes everything traceable, collaboration mechanisms make teams run efficiently, and the open source spirit lets knowledge flow freely. Even if you don't write code, understanding concepts like "commit, branch, merge" can help you better manage any content that needs "repeated modifications + multi-person collaboration"—from papers to documents, from notes to proposals.

For computer science students, GitHub is an essential skill: it's your portfolio, collaboration platform, learning resource library, and the most persuasive "resume" for future job hunting. Register an account early, upload your course assignments and small projects, accumulate slowly, and in a few years you'll have a technical resume that makes interviewers' eyes light up.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Get Hands-On: Complete Your GitHub First Experience

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Register a GitHub account and complete your profile (avatar, bio, technical fields of interest).
2. Create a public repository named<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">hello-github</code>, and check "Add a README file."
3. Enter the repository, click the edit button (pencil icon) on README.md, write a self-introduction in Markdown, and commit the changes.
4. In the GitHub search bar, search for a keyword you're interested in (such as<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python-tutorial</code>), and Star two projects you like.
5. (Advanced) Install Git on your computer, Clone the repository to local, modify the README and push back to cloud, completing a full "local → cloud" workflow.
:::
