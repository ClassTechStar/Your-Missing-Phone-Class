---
id: di-er-shi-san-zhang-github
part: chao-yue-pian
nav:  Anhang: GitHub-Einsteigerleitfaden
toc: sub
kind: chapter
---

### Kapitel 23 Anhang: GitHub-Einsteigerleitfaden – vom Code-Hosting zur Kollaborationsplattform

{class="chapter-intro mb-4"}
Im vorigen Kapitel haben wir über "Programmierdenken" gesprochen. Wer dieses Denken wirklich in die Praxis umsetzen und mit anderen zusammen an Projekten arbeiten will, kommt an einem Namen nicht vorbei: GitHub. Egal, ob du als Informatik-Student an Wettbewerben teilnimmst, deine Code-Werke sichern möchtest oder einfach sehen willst, was Entwickler weltweit gerade ausproberen – GitHub ist eine Plattform, die du kennen musst. In diesem Abschnitt beginnen wir mit den grundlegendsten Konzepten und helfen dir, eine klare Vorstellung zu entwickeln.

#### Erstens. Was ist GitHub überhaupt?

Kurz gesagt: GitHub ist eine auf Git basierende <strong>Code-Hosting- und Kollaborationsplattform</strong>. Sie ging 2008 online, wurde 2018 von Microsoft übernommen und ist bis heute die weltweit größte Open-Source-Code-Hostingplattform mit hunderten Millionen Repositories, die nahezu alle gängigen Programmiersprachen abdecken.

Ein Vergleich:<strong>Git ist das Tagebuch auf deinem Computer, GitHub ist eine öffentliche Blog-Plattform</strong>– du kannst deine Werke veröffentlichen, anderen folgen, an Diskussionen teilnehmen und zusammenarbeiten. Es ist nicht nur ein "Backend-Warehouse für Programmierer", sondern eher eine von Entwicklern weltweit gemeinsam erbaute "Technologiestadt" – Projekte entstehen hier, iterieren, werden diskutiert und weiterverwendet.

Auch für Nicht-Programmierer ist GitHub keineswegs unerreichbar. Viele Nicht-Programmierer nutzen es, um Notizen, E-Books, persönliche Blogs oder sogar Konfigurationsdateien zu hosten. Sobald du das Bedürfnis hast, "deine Dinge ordentlich zu strukturieren und zu teilen", lohnt sich ein Blick auf GitHub.

#### Zweitens. Der Unterschied zwischen Git und GitHub (Schlüsselkonzept!)

Viele verwechseln beim ersten Kontakt diese beiden Begriffe. Hier eine Übersicht:

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Vergleichspunkt</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Git</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GitHub</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wesen</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Versionskontrollwerkzeug (Software)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Code-Hosting-Plattform (Website)</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ausführungsort</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lokaler Computer</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cloud (Browser-Zugriff)</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kernaufgabe</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jede Änderung an Dateien protokollieren (was, wer, wann)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Git-Repositorys in die Cloud stellen, um Speicherung, Anzeige und Zusammenarbeit zu erleichtern</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Netzwerk nötig?</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nein, offline nutzbar</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ja, Internetzugriff erforderlich</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Zugehörigkeit</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Open-Source-Software, entwickelt von Linus Torvalds (Vater von Linux)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Produkt von Microsoft</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ähnliche Wettbewerber</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SVN, Mercurial</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitLab, Gitee, Bitbucket</td>
                            </tr>
                        </tbody>
                    </table>
```

Kurz gesagt:<strong>Git entscheidet, "wie Änderungen protokolliert werden", GitHub entscheidet, "wo die Änderungen liegen und wie man zusammenarbeitet"</strong>. Git ist ein Werkzeug, das lokal läuft; GitHub ist eine Plattform, die Git-Repositorys in die Cloud stellt, um Zusammenarbeit und Präsentation zu erleichtern. Du kannst Git ohne GitHub nutzen (z. B. für die eigene Versionsverwaltung deines Codes), aber GitHub setzt Git voraus (denn GitHub basiert auf Git).

#### Drittens. Kernkonzepte und Funktionen von GitHub

##### 📁 Grundkonzepte

Bevor du loslegst, lerne einige häufige Begriffe kennen, sonst wird dir die GitHub-Oberfläche wie ein Rätsel vorkommen:

- <strong>Repository (kurz Repo)</strong>: Ein Projekt entspricht einem Repository, das alle Codedateien, historischen Versionen und Dokumente dieses Projekts enthält. Man kann es sich als einen "Projektordner" vorstellen.
- <strong>Commit</strong>: Eine aufgezeichnete Änderung am Code. Jeder Commit trägt eine Beschreibung, die festhält, "was diesmal geändert wurde und warum". Das ist die Grundlage für die "Zeitreise" von Git/GitHub.
- <strong>Branch</strong>: Ein unabhängiger Entwicklungszweig, der vom Hauptzweig abzweigt. Wenn du z. B. eine neue Funktion hinzufügen willst, kannst du einen eigenen Branch dafür aufmachen, ihn nach Abschluss der Entwicklung in den Hauptzweig zurückführen, ohne andere zu beeinträchtigen.
- <strong>Clone</strong>: Das Cloud-Repository wird vollständig auf den lokalen Computer kopiert, danach kannst du den Code lokal ändern.
- <strong>Push / Pull</strong>: Push lädt lokalen Code zu GitHub hoch, Pull lädt den neuesten Code von GitHub auf den lokalen Rechner. Das sind die beiden Kernaktionen zur Code-Synchronisation bei der Teamzusammenarbeit.
- <strong>Pull Request (kurz PR)</strong>: Wenn du in einem Branch den Code geändert hast und ihn in den Hauptzweig zusammenführen möchtest, eröffnest du einen PR, damit die Teammitglieder den Code begutachten, bevor er zusammengeführt wird. Das ist der Kernmechanismus der GitHub-Zusammenarbeit.
- <strong>Issue</strong>: Dient der Erfassung von Bugs, Funktionswünschen und Diskussionsthemen. Jedes Issue ist wie ein Diskussionsbeitrag, dem Verantwortliche zugewiesen und die mit Labels versehen werden können.
- <strong>Fork</strong>: Kopiert das Repository einer anderen Person unter dein eigenes Konto. Du kannst in deiner Kopie beliebig ändern, ohne das Original-Repository zu beeinflussen. Wenn du fertig bist, kannst du dem ursprünglichen Autor einen PR schicken und um die Übernahme deiner Verbesserungen bitten.

##### 🛠️ Kernfunktionen

GitHub bietet mehr als nur Code-Speicherung, nämlich auch:

- <strong>Versionskontrolle</strong>: Protokolliert die Historie jeder Code-Änderung; bei fehlerhaftem Code kannst du jederzeit zu einer früheren funktionierenden Version zurückkehren.
- <strong>Teamzusammenarbeit</strong>: Unterstützt parallele Entwicklung mehrerer Nutzer am selben Projekt, ohne dass es zu Überschreibungen oder Konflikten kommt.
- <strong>Issue-Tracking</strong>: Mit Issues werden Bugs und Funktionswünsche erfasst, damit das Team den Fortschritt verfolgen kann.
- <strong>Projektmanagement</strong>: Integriert To-do-Listen, Projekt-Boards (Projects) und weitere Management-Werkzeuge – quasi ein eingebautes leichtgewichtiges Trello.
- <strong>Automatisierung</strong>: Über <strong>GitHub Actions</strong> lässt sich nach einem Commit automatisch kompilieren, testen, paketieren und deployen – ein Kernwerkzeug für modernes CI/CD (Continuous Integration / Continuous Deployment).
- <strong>Dokumentationsverwaltung</strong>: README stellt das Projekt vor, Wiki speichert detaillierte Architektur- und Entwicklungsrichtlinien, Pages kann sogar statische Websites direkt hosten.
- <strong>Code-Hosting und Präsentation</strong>: Jedes Repository hat eine ansprechende Web-Ansicht mit Syntax-Highlighting – die "Visitenkarte" deiner technischen Werke.
- <strong>Open-Source-Community</strong>: Du kannst Projekte mit einem Stern (Star) markieren, Projektaktivitäten beobachten (Watch), Entwicklern folgen (Follow) und an globaler Open-Source-Zusammenarbeit teilnehmen.

#### Viertens. Registrierung und Einstieg: Erstelle in fünf Minuten dein erstes Repository

##### 📝 Konto registrieren

1. Besuche<a href="https://github.com" class="text-primary hover:underline" target="_blank" rel="noopener">github.com</a>und klicke auf "Sign up".
2. E-Mail-Adresse eingeben, Passwort und Benutzername festlegen (der Benutzername erscheint in der Adresse deiner persönlichen Startseite, Empfehlung: englisch, z. B.<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">github.com/yourname</code>).
3. E-Mail-Verifizierung und Captcha abschließen.
4. Den kostenlosen Tarif (Free) wählen – für persönliche Nutzer völlig ausreichend.

##### 📁 Erstes Repository erstellen

1. Nach dem Login oben rechts auf das "Anhang F"-Symbol klicken und "New repository" wählen.
2. Repository-Namen (Repository name) eingeben, z. B.<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">my-first-project</code>.
3. Eine kurze Beschreibung (Description) schreiben, damit andere wissen, wofür das Repository gut ist.
4. Öffentlich (Public) oder Privat (Private) wählen. Öffentliche Repositories sind für alle sichtbar, private nur für dich und Mitwirkende. Auch kostenlose Konten unterstützen unbegrenzt private Repositories.
5. "Add a README file" ankreuzen – die README ist die "Gebrauchsanweisung" des Projekts, für jedes Repository empfohlen.
6. Auf "Create repository" klicken – dein erstes GitHub-Repository ist entstanden!

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Wissenshäppchen: Was ist eine README?

{class="mt-1"}
README.md ist eine Datei im Markdown-Format und der erste Inhalt, den Besucher sehen, wenn sie dein Repository öffnen. Eine gute README enthält meist: Projektvorstellung, Installationsmethode, Anwendungsbeispiele, Lizenz, Kontakt. Eine gute README zu schreiben, gehört zum Grundhandwerk eines Programmierers und ist die erste Hürde dafür, ob ein Projekt von anderen genutzt wird.
:::

#### Fünftens. Grundlegender Workflow: Vom Lokalgerät zur Cloud

Um den GitHub-Workflow zu verstehen, merke dir diesen Kreislauf:<strong>Lokale Änderung → Staging → Commit → Push → Cloud-Aktualisierung</strong>.

1. <strong>Dateien ändern</strong>: Auf dem lokalen Computer mit einem Editor Code schreiben oder Dokumente ändern.
2. <strong>git add</strong>: Geänderte Dateien zum "Staging-Bereich" hinzufügen; das entspricht der Mitteilung an Git: "Diese Änderungen möchte ich aufzeichnen."
3. <strong>git commit</strong>: Die Änderungen aus dem Staging-Bereich als "Commit" endgültig festhalten, mit einer Beschreibung wie "Login-Bug behoben". Dieser Schritt findet nur lokal statt.
4. <strong>git push</strong>: Den lokalen Commit zur GitHub-Cloud hochladen, damit andere ihn sehen können.
5. <strong>git pull</strong>: Vor Beginn der Arbeit den neuesten Code aus der Cloud holen, um sicherzustellen, dass lokal und die restlichen Teammitglieder synchron sind.

Für Einsteiger gilt die Faustregel:<strong>"Zuerst pullen, dann ändern; nach dem Ändern add, beim commit eine Beschreibung, zuletzt push hochladen"</strong>. Mit dieser Gewohnheit bleibt die Teamzusammenarbeit sauber.

#### Sechstens. Team-Workflow: Wie funktioniert ein Pull Request?

Die größte Stärke von GitHub liegt in seinem Kollaborationsmechanismus. Ein typischer Team-Workflow sieht so aus:

1. <strong>Branch aufmachen</strong>: Vom Hauptzweig (meist main oder master) einen neuen Branch aufmachen, z. B.<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">feature/login</code>, und auf diesem Branch die neue Funktion entwickeln.
2. <strong>Entwickeln und committen</strong>: Auf dem neuen Branch Code schreiben, mit mehreren Commits den Fortschritt festhalten.
3. <strong>Zu GitHub pushen</strong>: Den Branch ins Cloud-Repository pushen.
4. <strong>Pull Request eröffnen</strong>: Auf der GitHub-Webseite einen PR eröffnen und darum bitten, deinen Branch in den Hauptzweig zusammenzuführen. Beschreibe klar, was dieser PR ändert und warum.
5. <strong>Code Review</strong>: Teammitglieder prüfen deinen Code, geben Feedback oder Änderungsvorschläge. Du kannst aufgrund des Feedbacks weitere Commits machen; der PR wird automatisch aktualisiert.
6. <strong>Zusammenführen</strong>: Nach bestandener Prüfung auf "Merge" klicken, um den Code in den Hauptzweig zu übernehmen. Dein Beitrag ist offiziell ins Projekt eingeflossen!

Dieser Ablauf stellt sicher, dass <strong>jeder Code vor dem Eintritt in den Hauptzweig geprüft wurde</strong>, was die Fehlerquote deutlich senkt. Auch Open-Source-Projekte nutzen diesen Mechanismus, um Beiträge von Fremden weltweit anzunehmen – du kannst durchaus bei einem bekannten Open-Source-Projekt einen PR einreichen und nach Annahme als Mitwirkender dieses Projekts gelten.

#### Siebtens. Typische Anwendungsszenarien von GitHub

##### 🎓 Studierende bei Wettbewerben und Kursprojekten

Informatik-Studierende, die an ACM, Hackathons oder Abschlussarbeiten teilnehmen, kommen kaum ohne GitHub aus. Es dient sowohl als Team-Kollaborationsplattform als auch als Schaufenster für Werke – Preisrichter können direkt dein Repository ansehen und Codequalität und Zusammenarbeitsprozess nachvollziehen. Viele Unternehmen verlangen bei Stellenausschreibungen die Angabe der GitHub-Startseite als Nachweis technischer Fähigkeiten.

##### 📚 Persönliche Wissensbasis und Notiz-Hosting

Auch Nicht-Programmierer können GitHub nutzen. Viele verwenden es, um Lernnotizen, technische Blogs (in Kombination mit GitHub Pages kostenlos eine Website aufbauen), E-Books zu hosten. Markdown-Schreiben + Git-Versionsverwaltung + Cloud-Backup – drei in einem.

##### 🌐 Teilnahme an Open-Source-Projekten

GitHub ist das Kernzentrum der globalen Open-Source-Bewegung. Du kannst Lieblingsprojekte forken, nach Modifikation einen PR an die Community zurückgeben oder einfach gute Projekte mit einem Stern markieren und Aktualisierungen verfolgen. Sich an Open Source zu beteiligen, ist ein hervorragender Weg, um technisch zu wachsen und Reputation aufzubauen.

##### 🤖 Automatisiertes Deployment und CI/CD

Mit GitHub Actions lässt sich ein vollautomatischer Ablauf realisieren: "Code einmal pushen, automatisch testen, automatisch auf den Server deployen". Viele persönliche Blogs und Dokumentationsseiten sind so gebaut – nach dem Schreiben eines Artikels einmal pushen, und die Website aktualisiert sich automatisch.

##### 💾 Code-Backup und Mehrgeräte-Synchronisation

Das Code-Repository als Cloud-Laufwerk nutzen: Beim Gerätewechsel oder der Arbeit auf mehreren Geräten genügt ein git pull, um den neuesten Code zu holen – kein USB-Stick-Kopieren mehr.

#### Achtens. Ein paar Ratschläge für Einsteiger

- <strong>Commit-Beschreibungen klar formulieren</strong>: Vermeide nichtssagende Angaben wie "update". Eine gute Commit-Message lautet z. B. "Problem behoben, dass nach dem Login auf eine falsche Seite gesprungen wird" – auch ein halbes Jahr später weißt du, was du getan hast.
- <strong>Häufig committen, in kleinen Schritten</strong>: Nach jeder kleinen Funktion einmal committen statt erst nach einem ganzen Tag. So lassen sich Probleme leichter eingrenzen.
- <strong>Mit Branches entwickeln, nicht direkt im Hauptzweig</strong>: Auch bei Einzelprojekten lohnt sich die Gewohnheit, mit Branches zu arbeiten – bei späterer Teamzusammenarbeit bist du dann nicht überfordert.
- <strong>.gitignore geschickt einsetzen</strong>: Diese Datei teilt Git mit, welche Dateien nicht versioniert werden sollen (z. B. Passwort-Konfigurationen, Kompilate, Abhängigkeitsordner), um Mülldateien vom Upload auszuschließen.
- <strong>Viel in guten Open-Source-Projekten stöbern</strong>: Schau dir GitHub Trending an, betrachte die Code-Struktur, README-Schreibweise und Kollaborationsabläufe von High-Star-Projekten – der schnellste kostenlose Weg zur Weiterbildung.
- <strong>GitHub Student Pack beantragen</strong>: Nach der Studentenverifizierung erhältst du kostenlos umfangreiche Kontingente für kostenpflichtige Tools und Dienste (Copilot, Domains, Cloud-Dienste usw.) im Wert von tausenden Dollar.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Sicherheitshinweis

{class="list-disc pl-6 mt-1 space-y-1"}
- Niemals Passwörter, API-Schlüssel, Datenbankverbindungsstrings oder andere sensible Informationen zu GitHub committen – besonders nicht in öffentlichen Repositories. Einmal geleakt, werden sie von Crawlern sofort erfasst, mit schwerwiegenden Folgen.
- Wer versehentlich sensible Informationen committet hat, reicht es nicht, die Datei zu löschen (in der Historie steht sie noch). Nutze<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git filter-branch</code> oder spezielle Tools, um die Historie zu bereinigen, und wechsle sofort die geleakten Schlüssel.
- Auch private Repositories sind nicht absolut sicher; sensible Informationen sollten vorzugsweise über Umgebungsvariablen verwaltet werden und nicht ins Code-Repository gelangen.
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Hinweise zum GitHub-Zugriff aus China

{class="mt-1"}
Der Zugriff auf GitHub ist aus China manchmal instabil; es kann vorkommen, dass Seiten nicht laden oder Klonen langsam ist. Mögliche Abhilfen: ① Inländische Mirror-Sites nutzen (z. B. GitClone, ghproxy), um das Klonen zu beschleunigen; ② Hosts konfigurieren oder einen Proxy verwenden; ③ Wenn primär in China zusammengearbeitet wird, kann auch die chinesische Alternative <strong>Gitee</strong> erwogen werden – ähnliche Funktionen, schnellerer Zugriff. Viele Teams hosten parallel auf GitHub und Gitee, um sowohl Internationalität als auch Inlandsgeschwindigkeit zu berücksichtigen.
:::

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Fortgeschrittene Anwendung: Mit GitHub Pages kostenlos einen persönlichen Blog aufbauen

{class="mt-1"}
GitHub Pages erlaubt es dir, kostenlos eine statische Website zu hosten. In Kombination mit statischen Site-Generatoren wie Jekyll, Hexo oder Hugo lässt sich mühelos ein persönlicher Blog aufbauen: Markdown-Artikel schreiben, ins Repository pushen, der Blog aktualisiert sich automatisch – inklusive HTTPS und eigener Domain. Unzählige Technik-Blogs sind so entstanden: null Kosten, keine Werbung, vollständige Versionskontrolle.
:::

#### Neuntens. Zusammenfassung: Warum jeder GitHub kennen sollte

GitHub ist längst nicht mehr nur ein "Werkzeug für Programmierer", sondern vielmehr eine <strong>Arbeitsweise im digitalen Zeitalter</strong>: Versionsverwaltung macht alles nachvollziehbar, der Kollaborationsmechanismus lässt Teams effizient arbeiten, der Open-Source-Gedanke lässt Wissen frei fließen. Auch wenn du nicht programmierst, hilft das Verständnis von Konzepten wie "Commit, Branch, Zusammenführen" dir dabei, jeden Inhalt besser zu verwalten, der "wiederholte Überarbeitungen + Zusammenarbeit mehrerer Personen" erfordert – von Aufsätzen über Dokumentationen bis hin zu Notizen und Konzepten.

Für Informatik-Studierende ist GitHub eine unverzichtbare Fähigkeit: Es ist dein Portfolio, deine Kollaborationsplattform, deine Lernressourcen-Bibliothek und der überzeugendste "einfache" Nachweis bei der späteren Bewerbung. Registriere früh ein Konto, lade Kursarbeiten und kleine Projekte hoch und sammle nach und nach – in ein paar Jahren wirst du eine technische Vita haben, die Personaler beeindruckt.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Leg los: Dein GitHub-Erlebnis

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Ein GitHub-Konto registrieren und das Profil vervollständigen (Avatar, Kurzprofil, interessante Technikbereiche).
2. Ein öffentliches Repository namens<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">hello-github</code> erstellen und "Add a README file" ankreuzen.
3. Das Repository öffnen, auf die Bearbeiten-Schaltfläche der README.md (Bleistift-Symbol) klicken, mit Markdown eine Selbstvorstellung schreiben und die Änderung committen.
4. In der GitHub-Suchleiste ein interessantes Stichwort suchen (z. B.<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python-tutorial</code>) und zwei Projekte mit einem Stern markieren.
5. (Fortgeschritten) Git auf dem Computer installieren, das Repository lokal klonen, die README ändern und zur Cloud zurückpushen – ein vollständiger "Lokal → Cloud"-Workflow.
:::
