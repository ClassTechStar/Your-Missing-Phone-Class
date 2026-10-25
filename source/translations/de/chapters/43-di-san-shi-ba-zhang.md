---
id: di-san-shi-ba-zhang
num: 38
part: ai-biancheng-pian
nav: Kapitel 38: Die fünf Denkprinzipien der KI-Programmierung
toc: default
kind: chapter
---

### Kapitel 38: Fünf Denkprinzipien der KI-Programmierung

{class="chapter-intro mb-4"}
Wenn Sie aus diesem Buch nur ein Kapitel behalten, dann dieses. Die fünf Denkprinzipien sind sein Herzstück; alle späteren Kapitel – Kontext, Anforderungen, Dialog, Qualität – entfalten sie für verschiedene Situationen. Keines ist schwer zu verstehen, doch jedes lohnt sich, in einigen Projekten „in den Muskeln“ zu verankern.

Der Ursprung ist spannend: Andrej Karpathy veröffentlichte zu seinem Open-Source-Projekt eine nur 70 Zeilen lange CLAUDE.md mit vier Kernprinzipien für die Zusammenarbeit mit KI. Die Datei erhielt auf GitHub über 70.000 Stars und wurde zur meistzitierten Richtschnur der KI-Programmierer weltweit. Es sind keine leeren Slogans, sondern aus der Praxis destillierte Denkgewohnheiten. Dieses Buch ergänzt die fünfte – iterative Verifikation – und vollendet so das System der fünf Prinzipien.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Warum ist eine 70-Zeilen-Datei so viel wert?

{class="mt-1"}
Was bedeuten 70.000 Stars? Die meisten GitHub-Projekte erreichen das nie. Dass eine 70-Zeilen-Datei es schafft, zeigt: Im KI-Zeitalter ist nicht Code knapp, sondern die Fähigkeit, klar zu denken. Diese 70 Zeilen sind die destillierte Form dieses „Klar-Denkens“.
:::

#### 1. Prinzip 1: Think Before Coding (erst denken, dann kodieren)

Das kontraintuitivste der fünf Prinzipien. Wenn KI uns beim Programmieren hilft, warum noch „erst denken“? Ganz einfach: Die Qualität der KI-Ausgabe hängt von Ihrer Eingabe ab. Wenn Sie selbst nicht wissen, was Sie wollen, geraten Sie in endlose „Änderungsschleifen“ – im Volksmund „KI irrt gemeinsam mit Ihnen“.

„Erst denken“ heißt: Vor der Anweisung an die KI drei Fragen klären – ein „Denk-Dreieck“, das vollständig sein muss:

1. Welches Problem löse ich? (Ziel)
2. Wie soll das Ergebnis aussehen? (Abnahmekriterien)
3. Welche Einschränkungen gibt es? (Rahmen)

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Denkdimension</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Unklare Eingabe (schlecht)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Klare Eingabe (gut)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Problemdefinition</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mach mir eine Website</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Baue eine persönliche Tool-Seite mit drei Einstiegskarten für KI-Miniprogramme</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Erwartetes Ergebnis</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sieht gut aus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Responsives Layout, Dark Theme, Hover-Animationen auf den Karten, mobil nutzbar</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Einschränkungen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">(nicht genannt)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Keine Frameworks, reines HTML+CSS+JS, Einzeldatei-Deployment, kein Backend</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Unklare vs. klare Eingabe für dieselbe Anforderung

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Hinweis: „Erst denken“ ≠ „perfektes Dokument schreiben“

{class="mt-1"}
„Erst denken“ heißt nicht „zuerst ein perfektes PRD schreiben“. Es ist ein schnelles, aber strukturiertes Denken – 30 Sekunden für die drei Fragen bringen mehr als 30 Minuten hin- und herändern im Chat. Bei kleinen Aufgaben genügt ein kurzer Dreiklang; bei großen Projekten wird daraus ein vollständiges Anforderungsdokument (siehe Kapitel 40).
:::

#### 2. Prinzip 2: Simplicity First (Einfachheit zuerst)

Die größte Falle ist nicht „schafft es nicht“, sondern „macht zu viel“. Sagen Sie „Baue ein Benutzerverwaltungssystem“, generiert die KI oft Authentifizierung, Rechte, Rollen, Audit-Logs, Datenexport – obwohl Sie vielleicht nur eine einfache Login-Seite brauchen. Überproduktion ist die Hauptursache für aufgeblähten KI-Code.

„Einfachheit zuerst“ bedeutet „minimaler Machbarkeitsgrundsatz“: Mit dem wenigsten Code die Kernfunktion, mit der einfachsten Lösung das Problem, mit den wenigsten Features die Idee prüfen. Karpathy hat dafür ein treffendes Bild: „Wenn du nur einen Rabattpreis berechnen willst, brauchst du keinen E-Commerce-Motor.“

In der Praxis heißt das konkrete Gewohnheiten:

- Pro Anweisung nur einen Funktionspunkt umsetzen, nicht das ganze System auf einmal;
- Standardbibliotheken und einfache Lösungen vor komplexen Abhängigkeiten;
- Was in 50 Zeilen geht, nicht auf 500 Zeilen aufblasen;
- Wenn die KI über das Ziel hinausschießt, klar sagen: „Überflüssiges streichen.“

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Szenario</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Überdimensionierte Lösung (vermeiden)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Einfache Lösung (empfohlen)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Daten speichern</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MySQL-Datenbank + ORM aufsetzen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Erst JSON-Datei oder SQLite</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Benutzer-Login</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OAuth2.0 + JWT + Rollenrechte</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Erst einfache Passwortprüfung</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Frontend-Framework nötig</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">React + Redux + Router</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Erst reines HTML + natives JS</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Deployment ins Netz</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Docker + CI/CD + K8s</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Erst lokal zum Laufen bringen</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Überdimensionierte vs. einfache Lösungen in typischen Szenarien

#### 3. Prinzip 3: Surgical Changes (chirurgisch präzise Änderungen)

Beim Iterieren eines bestehenden Projekts sollte jede Änderung präzise sein wie eine Operation – nur das Nötige anfassen. Besonders wichtig in der KI-Programmierung, weil KI zum „Nebenbei-Mitändern“ neigt: Ein Bugfix wird leicht zur halben Datei-Refactorierung.

Kernanforderung: Jede Anweisung nennt explizit Umfang und Grenzen. „Ändere nur die Funktion calculate_discount“, „Lass den Rest unangetastet“, „Behalte den vorhandenen Code-Stil“. Geht die Änderung darüber hinaus, sofort die überflüssigen Teile zurückverlangen.

Karpathy illustriert das mit einem Diff-Beispiel: Sie lassen eine „Mitgliedspreis“-Logik in die Rabattfunktion des Warenkorbs einbauen. Gutes Ergebnis: nur diese Funktion, wenige zusätzliche Zeilen. Schlechtes Ergebnis: der ganze File wird umgebaut – der neue Code mag „eleganter“ wirken, aber Sie wissen nicht, ob neue Bugs darin stecken. „Sieht besser aus“ darf in der KI-Programmierung nie ein Grund sein, von der Anweisung abzuweichen.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Schlechte Anweisung (unklarer Umfang)

{class="font-mono text-xs leading-relaxed"}
Optimiere die Rabattlogik dieses Projekts
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Gute Anweisung (präziser Umfang)

{class="font-mono text-xs leading-relaxed"}
Ändere nur calculate_discount in cart.py: 1. Ergänze Mitgliedspreis-Logik zur bestehenden Rabattlogik 2. Mitglieder erhalten zusätzlich 10 % Rabatt 3. Funktionsparameter und andere Funktionen unverändert lassen 4. Vorhandenen Variablennamen-Stil beibehalten
:::
:::

#### 4. Prinzip 4: Goal-Driven Execution (zielgetriebene Ausführung)

Diese Regel beantwortet eine Schlüsselfrage: Soll man der KI sagen, „wie“ sie arbeiten soll, oder „was“ herauskommen soll? Karpathys Antwort: das Letztere. Statt „Erst eine Klasse anlegen, dann Methoden, dann Tests“ besser: „Ich brauche ein Werkzeug, das CSV-Dateien einliest und je Spalte die Anzahl eindeutiger Werte zählt“. Die KI wählt den Weg, Sie nehmen das Ergebnis ab.

Der Vorteil ist doppelt: Die KI bekommt mehr Spielraum und wählt den besten Weg statt an Ihren Zwischenschritten zu kleben; Sie verlagern die Aufmerksamkeit vom „Wie“ auf „Ist es richtig?“ – genau das ist die Aufgabe eines Dirigenten.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Hinweis: Zielgetrieben ≠ gewähren lassen

{class="mt-1"}
Nach der Ausführung muss streng abgenommen werden: Erfüllt das Ergebnis die Anforderung? Sind Randfälle behandelt? Gibt es Überdesign? Bei Abweichung konkretes Feedback geben – nicht „schreib neu“, sondern „Bei leerer Liste entsteht ein IndexError in Zeile 15, bitte eine Leerwertprüfung ergänzen“.
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Anweisungsstil</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Beispiel</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ergebnismerkmal</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Imperativ (wie)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">„Lege eine Python-Klasse DataParser an, füge eine Methode parse mit Parameter filename hinzu, lese mit dem csv-Modul …“</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">KI wird zur Tippkraft, Ihre Zwischenschritte sind vielleicht nicht optimal</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Zielorientiert (was)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">„Ich brauche ein Tool: CSV einlesen, je Spalte eindeutige Werte zählen, als JSON ausgeben. Bitte vollständige Implementierung.“</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">KI wählt den besten Weg, Sie prüfen das Ergebnis</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Imperative vs. zielorientierte Anweisungen

#### 5. Prinzip 5: Iterate and Verify (iterieren und prüfen)

Dieses Buch ergänzt Karpathys vier Prinzipien um ein fünftes. Kernüberzeugung: Die erste KI-Ausgabe ist fast nie die Endversion. Effektive KI-Programmierung ist ein Kreislauf aus „Erzeugen – Prüfen – Korrigieren“, nicht ein einmaliges „Anweisung – Ergebnis“.

„Iterieren und prüfen“ ist nicht passives „Falsch, nochmal“, sondern ein strukturierter Verifikationsprozess. Nach jeder Ausgabe auf drei Ebenen prüfen:

- Ebene 1 · Funktion: Läuft es? Sind Ein- und Ausgabe korrekt?
- Ebene 2 · Ränder: Was passiert bei leerer, zu langer oder fehlerhafter Eingabe?
- Ebene 3 · Architektur: Ist die Code-Struktur sinnvoll? Gibt es Hardcoding? Ist sie erweiterbar?

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-bullseye mr-1"></i> Ziel definieren</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> KI generiert Code</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Funktionsprüfung</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Bestanden</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Grenzfälle prüfen</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Bestanden</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-landmark mr-1"></i> Architektur-Review</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Bestanden, weiter zum nächsten Schritt</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> Nicht bestanden</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Konkretes Feedback geben</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> Neu generieren</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Abbildung 2: Iterativer Verifikationskreislauf der KI-Programmierung
:::

Der Schlüssel liegt im „konkreten Feedback“. Bei einem Fehlschlag nicht „stimmt nicht, mach neu“, sondern „Bei leerer Liste gibt es einen IndexError, bitte Zeile 15 um eine Leerwertprüfung ergänzen“. Präzises Feedback erlaubt gezielte Korrekturen; vages Feedback lässt die KI nur raten.

#### 6. Harness Engineering: Agent = Modell + Harness

Mitte 2026 machte der Begriff Harness Engineering in der KI-Programmier-Community die Runde. Die Formel ist einfach:

:::inline div .quote-line .text-center .text-base .font-bold
<strong>Agent-Fähigkeit = Modellfähigkeit × Harness-Qualität</strong>
:::

Die Modellfähigkeit ist die geistige Obergrenze; das Harness ist die „Arbeitsumgebung“ um das Modell – Kontextmanagement, Werkzeuganbindung, Prozesssteuerung, Gedächtnis.

Das erklärt ein häufiges Rätsel: Warum machen manche mit GPT-4 oder Claude brillante Projekte, andere nur mittelmäßigen Code? Der Unterschied liegt nicht im Modell, sondern im Harness. Ein gutes Harness umfasst klare Projektspezifikationen, sinnvolle Werkzeuge, geordneten Gesprächskontext und einen guten Verifikationsprozess. Das Modell setzt die Obergrenze, das Harness bestimmt, wie weit Sie sie ausschöpfen.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Das Praktikanten-Gleichnis

{class="mt-1"}
Stellen Sie das Modell wie ein geniales Praktikanten vor – hoher IQ, aber ohne Projekthintergrund, Werkzeuge, Fristen und Abnahmekriterien kommt nichts Gutes heraus. Harness Engineering ist die Kunst, diesem Praktikanten die richtige Arbeitsumgebung zu bauen.
:::

Die folgenden Kapitel lehren genau das: Kapitel 39 Kontextmanagement (Projektgedächtnis), Kapitel 40 Anforderungen (PRD), Kapitel 43 Dialogtechnik (Prompt-Schichten), Kapitel 45 Qualitätssicherung (Verifikationsprozess). Zusammen ergeben sie Ihr Harness.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Übung: Die nächste Idee mit dem „Denk-Dreieck“ zerlegen

{class="mt-1"}
Wählen Sie eine kleine Sache, die Sie schon lange machen wollten (z. B. eine Countdown-Seite, ein Trink-Erinnerungs-Skript). Drei Minuten lang beantworten: ① Welches Problem löst es? ② Wie sieht das Ergebnis aus? ③ Welche Rahmenbedingungen (Zeit, Technik, Umgebung)? Schreiben Sie die Antwort als einen Absatz. Glückwunsch – Ihr erstes „Think Before Coding“ ist fertig, und der Absatz ist eine brauchbare, hochwertige Anweisung.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Kapitel-Zusammenfassung

- Die fünf Prinzipien stammen aus Karpathys 70-zeiliger CLAUDE.md (70K+ Stars); dieses Buch ergänzt „Iterate and Verify“
- Think Before Coding: Vor dem Sprechen drei Fragen – Was? Wie sieht es aus? Welche Grenzen?
- Simplicity First: Die größte Falle ist „zu viel“ – für einen Rabatt braucht man keinen Shop-Motor
- Surgical Changes: Chirurgisch präzise, kein „Nebenbei-Mitändern“ der KI
- Goal-Driven Execution: „Was“ statt „Wie“ – die KI wählt den Weg
- Iterate and Verify: Drei Prüfebene (Funktion/Rand/Architektur) + konkretes Feedback, im Kreislauf
- Harness Engineering: Fähigkeit = Modell × Harness – KI wie ein geniales Praktikanten führen
:::
