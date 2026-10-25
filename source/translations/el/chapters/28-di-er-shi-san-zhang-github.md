---
id: di-er-shi-san-zhang-github
part: chao-yue-pian
nav:  Παράρτημα: Εισαγωγικός οδηγός GitHub
toc: sub
kind: chapter
---

### Κεφάλαιο 23 Παράρτημα: GitHub

{class="chapter-intro mb-4"}
GitHub = απαραίτητο.

#### 1. Τι είναι GitHub;

Απλά:<strong>πλατφόρμα hosting</strong>. 2008, Microsoft 2018.

Αναλογία:<strong>Git = ημερολόγιο, GitHub = blog</strong>— κοινότητα.

Για όλους.

#### 2. Git vs GitHub

Διευκρίνιση:

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Σύγκριση</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Git</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GitHub</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Φύση</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Version control (λογισμικό)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hosting (site)</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Τοποθεσία</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Τοπικά</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cloud</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ευθύνη</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Καταγραφή αλλαγών</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cloud repos</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Δίκτυο</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Offline</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Online</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ιδιοκτησία</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Open source, Linus Torvalds</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Microsoft</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ανταγωνιστές</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SVN, Mercurial</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitLab, Gitee, Bitbucket</td>
                            </tr>
                        </tbody>
                    </table>
```

Απλά:<strong>Git=πώς, GitHub=πού</strong>. Git=tool, GitHub=platform.

#### 3. Βασικές έννοιες

##### 📁 Βασικά

Όροι:

- <strong>Repository (Repo)</strong>: Project folder.
- <strong>Commit</strong>: Modification record.
- <strong>Branch</strong>: Ανεξάρτητη γραμμή.
- <strong>Clone</strong>: Local copy.
- <strong>Push/Pull</strong>: Sync actions.
- <strong>Pull Request (PR)</strong>: Merge request.
- <strong>Issue</strong>: Bug/feature tracking.
- <strong>Fork</strong>: Copy to account.

##### 🛠️ Λειτουργίες

Περισσότερα από storage:

- <strong>Version control</strong>: History.
- <strong>Συνεργασία</strong>: Parallel dev.
- <strong>Issue tracking</strong>: Track bugs.
- <strong>Project mgmt</strong>: Kanban.
- <strong>Αυτοματισμός</strong>: μέσω <strong>GitHub Actions</strong> Auto CI/CD.
- <strong>Docs</strong>: README/Wiki/Pages.
- <strong>Hosting</strong>: Showcase.
- <strong>Open source</strong>: Star/Watch/Follow.

#### 4. Εγγραφή: 5 λεπτά

##### 📝 Εγγραφή

1. Επισκεφθείτε<a href="https://github.com" class="text-primary hover:underline" target="_blank" rel="noopener">github.com</a>, "Sign up".
2. Email/password/username:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">github.com/yourname</code>).
3. Verify email.
4. Free plan.

##### 📁 Δημιουργία repo

1. + → New repository.
2. Όνομα:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">my-first-project</code>.
3. Description.
4. Public/Private.
5. Add README.
6. Create repository!

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Τι είναι README

{class="mt-1"}
README = πρώτη εντύπωση.
:::

#### 5. Βασική ροή

Κύκλος:<strong>Local → Stage → Commit → Push → Cloud</strong>. Βήματα:

1. <strong>Αλλαγή</strong>: Editor.
2. <strong>git add</strong>: Stage.
3. <strong>git commit</strong>: Commit.
4. <strong>git push</strong>: Push.
5. <strong>git pull</strong>: Pull.

Μνημονικό:<strong>"Pull → change → add → commit → push"</strong>. Συνήθεια.

#### 6. Pull Request ροή

Ισχυρή συνεργασία:

1. <strong>Branch</strong>: New branch.<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">feature/login</code>, develop.
2. <strong>Develop+commit</strong>: Code+commit.
3. <strong>Push</strong>: Push branch.
4. <strong>Open PR</strong>: Request merge.
5. <strong>Code Review</strong>: Team review.
6. <strong>Merge</strong>: Merge!

Διασφαλίζει <strong>review πριν main</strong>. Open source.

#### 7. Σενάρια

##### 🎓 Φοιτητές

ACM/hackathons/thesis.

##### 📚 Σημειώσεις

Markdown+Git+cloud.

##### 🌐 Open source

Fork/Star.

##### 🤖 CI/CD

Push → auto deploy.

##### 💾 Backup

Git as cloud.

#### 8. Συμβουλές

- <strong>Καλά commit msgs</strong>: Όχι "update".
- <strong>Μικρά βήματα</strong>: Συχνά commits.
- <strong>Branches</strong>: Not main directly.
- <strong>.gitignore</strong>: Ignore files.
- <strong>Δείτε καλά projects</strong>: Trending.
- <strong>Student Pack</strong>: Free tools.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Υπενθύμιση ασφαλείας

{class="list-disc pl-6 mt-1 space-y-1"}
- Ποτέ sensitive info.
- Αν διέρρευσε:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git filter-branch</code> Clean history.
- Private ≠ safe.
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Πρόσβαση Κίνα

{class="mt-1"}
Αν unstable:<strong>Gitee</strong>, γρήγορο.
:::

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>GitHub Pages blog

{class="mt-1"}
Free static site.
:::

#### 9. Σύνοψη

Περισσότερο από εργαλείο:<strong>τρόπος εργασίας</strong>. Versioning+συνεργασία.

Portfolio+βιογραφικό.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Πράξη: GitHub

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Εγγραφή+προφίλ.
2. Δημιουργία<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">hello-github</code> public+README.
3. Edit README.
4. Αναζήτηση<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python-tutorial</code> Star 2.
5. Clone+push.
:::
