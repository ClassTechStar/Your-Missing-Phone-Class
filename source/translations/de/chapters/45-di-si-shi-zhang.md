---
id: di-si-shi-zhang
num: 40
part: ai-biancheng-pian
nav: Kapitel 40: Requirements-Engineering – aus Ideen KI-Anweisungen machen
toc: default
kind: chapter
---

### Kapitel 40: Anforderungsengineering – aus Ideen ausführbare Anweisungen für die KI machen

{class="chapter-intro mb-4"}
Während es beim Kontext-Engineering darum geht, dass die KI den Hintergrund versteht, sorgt das Anforderungsengineering dafür, dass die KI weiß, was diesmal konkret zu tun ist. Dieser Schritt zeigt beim KI-Programmieren am deutlichsten die Unterschiede zwischen Menschen: Mit denselben Tools und demselben Modell erschafft der eine verblüffende Projekte, der andere bringt nur mittelmäßiges Spielzeug zustande. Der Unterschied liegt selten im technischen Können – sondern darin, wie gut jemand Anforderungen formulieren kann.

#### 1. Von der vagen Idee zur strukturierten Anforderung

Jedes Projekt beginnt mit einer vagen Idee – „Ich will eine Haushaltsbuch-App bauen“, „Ich will eine private Website machen“, „Ich will ein Tool für To-do-Listen bauen“. Gegen die Ideen ist nichts einzuwenden – aber wirfst du sie direkt der KI hin, hängt die Qualität des Ergebnisses allein vom Glück ab. Ziel des Anforderungsengineerings ist es, diese vage Idee in eine strukturierte Anforderung zu verwandeln, die die KI präzise umsetzen kann.

Die gute Nachricht: Eine strukturierte Anforderung verlangt keinen PRD über zig Seiten. Du musst nur fünf Fragen beantworten – wir nennen sie die „fünf Anforderungselemente“:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Element</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Frage</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Beispiel: Haushaltsbuch-App</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Für wen ist es?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Persönliche Nutzung, um Einnahmen und Ausgaben des Alltags festzuhalten</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Was soll es tun?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Eine App, die jede Einnahme und Ausgabe erfasst, monatlich zusammenfasst und visualisiert</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Warum baust du es?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ich will meine Ausgabenstruktur verstehen und unnötige Kosten aufspüren</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wie ungefähr?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Frontend mit React, Daten lokal im Browser speichern, Backend und Login erst einmal weglassen</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Welche Einschränkungen gibt es?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Entwicklung allein, fertig in 2 Wochen, kein Livegang und Deployment nötig</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Die fünf Anforderungselemente mit Beispielen

Diese fünf Elemente musst du nicht als förmliches Dokument ausarbeiten – sie einmal zügig im Kopf durchzugehen genügt. Entscheidend ist die Gewohnheit, erst klar zu denken und dann loszulegen. Du wirst merken: Sobald du diese fünf Fragen klar beantworten kannst, wird deine Anforderungsbeschreibung ganz von selbst strukturiert.

#### 2. Die Kunst der gestuften Anforderungszerlegung

Bei größeren Projekten reicht eine einzige Anforderungsbeschreibung nicht. Du musst die große Anforderung in kleine Teilanforderungen zerlegen, die sich einzeln überprüfen lassen. Das nennt man „Anforderungszerlegung“; der Grundsatz lautet: Jede Teilanforderung muss sich eigenständig umsetzen, eigenständig prüfen und eigenständig ausliefern lassen.

Am Beispiel „Eine private Haushaltsbuch-App bauen“ wäre eine sinnvolle Zerlegung:

1. Die Grundfunktion zum Erfassen von Einnahmen und Ausgaben umsetzen (Einträge hinzufügen, ansehen, löschen);
2. Kategorien ergänzen (jeden Eintrag mit Etiketten wie Essen, Verkehr und Co. versehen);
3. Die monatliche Zusammenfassung umsetzen (Einnahmen und Ausgaben pro Monat auswerten);
4. Datenvisualisierung ergänzen (die Ausgabenstruktur in Diagrammen zeigen).

Jeder Schritt ist ein Funktions-Zuwachs, der sich eigenständig ausführen und prüfen lässt.

:::inline div .quote-line
Goldene Regel zum Zerlegen von Anforderungen: Nach jedem Schritt muss das Projekt „etwas Benutzbares“ sein, so rudimentär auch. Lass das Projekt nie in dem Zustand „alles halb fertig und nichts benutzbar“ stecken.
:::

Diese Zerlegung bringt zwei Vorteile. Erstens siehst du jederzeit Fortschritt – nach jedem Schritt kann deine App eine Funktion mehr; dieses positive Feedback ist bei Langzeitprojekten entscheidend (Erfolgserlebnisse brauchen wir alle). Zweitens bleibt jede einzelne Aufgabe für die KI klein genug, was das Risiko von „Verständnisabweichungen“ senkt – je kleiner die Aufgabe, desto genauer versteht die KI, desto besser das Ergebnis.

#### 3. PRD-Schreibvorlage und Praxis

Bei größeren Projekten (etwa einer Full-Stack-App mit Front- und Backend und mehreren Funktionsmodulen) genügen die fünf Anforderungselemente womöglich nicht. Dann brauchst du ein förmlicheres Produktspezifikationsdokument (PRD). Ein oft missverstandener Punkt: Ein PRD ist nicht für die KI geschrieben – es ist für dich selbst, um deine Gedanken zu ordnen; erst danach kannst du der KI präzisere Anweisungen geben.

Ein gutes PRD muss nicht lang sein, sollte aber sechs Teile enthalten: Projektüberblick (in einem Absatz klären, worum es geht), Funktionsliste (was jeder Funktionspunkt ist), technischer Ansatz (welcher Tech-Stack, welche grobe Architektur), Datenmodell (die zentralen Datenstrukturen), Oberflächenbeschreibung (wie die wichtigsten Seiten aussehen) und Entwicklungsplan (in wie vielen Schritten es fertig wird).

::: div .code-block
:::inline div .code-head
<span>PRD.md</span><span class="dots">···</span>
:::

```
# PRD der Ausgaben-App
## Projektbeschreibung
Eine leichte Ausgaben-App: Einnahmen und Ausgaben erfassen, kategorisieren, Monatsübersichten und Datenvisualisierung.
## Funktionsliste
1. Buchung erfassen: Betrag, Typ (Einnahme/Ausgabe), Kategorie, Notiz, Datum
2. Kategorien: vordefiniert Essen, Verkehr, Einkäufe, Freizeit, Sonstiges
3. Monatsübersicht: Gesamteinnahmen, Gesamtausgaben und Saldo pro Monat
4. Ausgaben-Visualisierung: Kreisdiagramm mit Anteil je Kategorie
5. Datenexport: als CSV
## Technische Umsetzung
- Frontend: React + TypeScript + Tailwind CSS
- Speicherung: localStorage (ohne Backend)
- Diagramme: Chart.js
- Build: Vite
## Datenmodell
Record {
  id: string
  amount: number
  type: 'income' | 'expense'
  category: string
  note: string
  date: string  // YYYY-MM-DD
}
## Entwicklungsplan
Step 1: Grundfunktionen Buchungen (CRUD)
Step 2: Kategorienverwaltung
Step 3: Monatsübersicht
Step 4: Datenvisualisierung
Step 5: Datenexport
```
:::

Achte auf den Schreibstil dieses PRD: knappe Listen und ein strukturiertes Format statt langer Ausführungen. Jeder Funktionspunkt ist klar definiert, das Datenmodell mit einfachen Typen beschrieben. Ein PRD in diesem Stil liest sich für dich selbst klar – und wenn du es der KI gibst, versteht sie jeden einzelnen Anforderungspunkt präzise.

#### 4. Praxis: die komplette Durchrechnung von der Idee zum Plan

Reine Theorie ist langweilig – lass uns mit einem kompletten Beispiel den ganzen Weg des Anforderungsengineerings durchgehen. Nimm an, deine Idee lautet: „Ich will einen Lern-Tracker bauen, der festhält, was ich jeden Tag gelernt habe.“

Erster Schritt: die fünf Anforderungselemente durchgehen.

- Who: Nur für mich selbst.
- What: Ein Tool, das festhält, was ich täglich lerne, meine Lernzeit verfolgt und den Lernfortschritt Revue passieren lässt.
- Why: Ich will mir eine dauerhafte Lerngewohnheit aneignen und meinen Zuwachs sehen.
- How: Erst eine Webversion, Daten lokal im Browser gespeichert.
- Constraint: Entwicklung ohne Vorkenntnisse, Kernfunktionen in 1 Woche fertig.

Zweiter Schritt: die Anforderungen zerlegen.

1. Schritt 1: Die Funktion „Lerneintrag erfassen“ umsetzen (Datum, Inhalt, Dauer);
2. Schritt 2: „Lernzeit-Statistik“ ergänzen (heute, Woche kumuliert);
3. Schritt 3: Die Ansicht „Lernkalender“ umsetzen (angezeigt wie der GitHub-Beitragsgraph);
4. Schritt 4: Die Funktion „Lernrückblick“ ergänzen (zeigt zufällig Einträge eines vergangenen Tages zum Wiederholen).

Dritter Schritt: ein kurzes PRD schreiben. Es muss nicht lang sein – die Zerlegung oben bildet schon den Kern des PRD. Bring es in eine .md-Datei und lege sie ins Projektstammverzeichnis, als gemeinsame Referenz für dich und die KI.

Vierter Schritt: mit Schritt 1 der Entwicklung loslegen. Die Anweisung an die KI könnte lauten:

::: div .code-block
:::inline div .code-head
<span>Anweisung an die KI</span><span class="dots">···</span>
:::

```
Ich brauche die erste Funktion eines Lern-Trackers: Lerneinheiten erfassen.
Der Nutzer kann einen Eintrag mit Datum, Lerninhalt und Dauer (Minuten) hinzufügen.
Die Daten liegen in localStorage.
Frontend mit React + TypeScript.
Gib die vollständige Implementierung.
```
:::

Beachte, was diese Anweisung auszeichnet: Sie beschreibt nur das Ziel des aktuellen Schritts (die Erfassungsfunktion), ohne andere Funktionen einzumischen; sie nennt die technischen Randbedingungen klar (React, TypeScript, localStorage); sie gibt genug Information, damit die KI weiß, „was“ zu tun ist und „wie“ vorzugehen ist, überlässt die konkrete Umsetzung aber der KI. Das ist eine hochwertige KI-Programmieranweisung, wie sie das Anforderungsengineering hervorbringt.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Ausprobieren: Schreibe für dein Herzensprojekt eine Fünf-Elemente-Karte

{class="mt-1"}
Such dir ein kleines Projekt aus, das du schon lange mit dir herumträgst, und fülle in 5 Minuten eine Karte aus: Who / What / Why / How / Constraint – je ein Satz. Dann zerlege es in 3–5 Schritte, von denen jeder benutzbar ist. Du wirst merken: Einmal aufgeschrieben, wird aus dem „Tagtraum“ eine „To-do-Liste“.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Zusammenfassung des Kapitels

- Die fünf Anforderungselemente: Who / What / Why / How / Constraint – erst klar denken, dann loslegen
- Goldene Regel der Anforderungszerlegung: Nach jedem Schritt ist das Projekt etwas „Benutzbares“
- Das PRD schreibst du für dich selbst: Überblick, Funktionsliste, technischer Ansatz, Datenmodell, Oberfläche, Plan
- Gute Anweisung = nur den aktuellen Schritt beschreiben + klare Randbedingungen + „was“ sagen, nicht „wie“
- Komplette Vorlage in vier Schritten: Fünf Elemente → Zerlegung → PRD → Anweisung geben
:::
