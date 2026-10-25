---
id: di-si-shi-si-zhang
num: 44
part: ai-biancheng-pian
nav: Kapitel 44: Praxis von 0 auf 1 – der komplette Projektablauf
toc: default
kind: chapter
---

### Kapitel 44: Praxis von 0 auf 1 – Der komplette Ablauf eines Projekts

{class="chapter-intro mb-4"}
Die Theorie sitzt – jetzt wird gewerkelt. Dieses Kapitel ist kein einfaches „Tipp-nach“-Tutorial, sondern eine Praxis-Methodik für „Wie denke ich? Wie frage ich? Wie prüfe ich?“. An drei Projekten mit steigendem Schwierigkeitsgrad zeigen wir den kompletten Gedankengang von der Anforderung bis zum fertigen Produkt. Diese Vorgehensweise funktioniert, egal welches Tool du nutzt.

#### 1. Projekt 1: Eine schlanke persönliche Tool-Seite (Einsteiger)

##### 1. Über die Anforderungen nachdenken

Ziel: eine persönliche Tool-Seite mit Einstiegen zu 3–4 praktischen Mini-Tools. Ein reines Frontend-Projekt, ohne Backend und Datenbank. Wichtig ist nicht, wie komplex die Tools sind, sondern dass du den kompletten Weg „von der Anforderung zum fertigen Produkt“ durchlebst.

Entlang der fünf Anforderungselemente: Who – für den persönlichen Gebrauch. What – eine Webseite, die Einstiege zu Tools zeigt. Why – die häufig genutzten Tools auf einer Seite sammeln, damit sie schnell erreichbar sind. How – eine einzelne HTML-Datei mit CSS und JS, ohne Framework. Constraint – in 30 Minuten fertig, ohne Deployment.

##### 2. Die Anweisung geben

Nach dem Prinzip „Think Before Coding“ sollte deine Anweisung genug Informationen enthalten, damit die KI das Ziel versteht – aber nicht jedes Umsetzungsdetail vorgeben:

::: div .code-block
:::inline div .code-head
<span>Anweisung an die KI</span><span class="dots">···</span>
:::

```
Erstelle eine persönliche Tool-Webseite mit diesen Anforderungen:
1. HTML in einer einzigen Datei (inline CSS und JS), ohne Frameworks
2. Dunkles Thema, moderner minimalistischer Stil
3. Zeige 4 Tool-Karten:
   - Textzusammenfasser
   - Wortzähler
   - Farbwähler
   - QR-Code-Generator
4. Jede Karte mit Symbol, Titel und kurzer Beschreibung
5. Die Karten haben eine Hover-Animation
6. Responsives Layout, auf dem Handy benutzbar
7. Oben eine Titelleiste
Gib direkt die vollständige HTML-Datei.
```
:::

##### 3. Abnahme und Iteration

Sobald die KI den Code liefert, nimmst du die Abnahme entlang der drei Prüfebenen vor. Erste Ebene, Funktionsprüfung: Lässt sich die Datei im Browser öffnen? Werden alle 4 Karten angezeigt? Funktioniert die Hover-Animation? Zweite Ebene, Grenzfallprüfung: Ist das Layout bei Handybildschirmgröße in Ordnung? Brechen die Karten bei sehr schmalen Fenstern sauber um? Dritte Ebene, Architekturprüfung: Ist der Code lesbar? Steht das CSS inline in einem style-Tag? Gibt es auffällige Redundanzen?

Willst du auch die Funktion eines Tool-Kartens umsetzen (statt nur des Einstiegs), ergänze sie nach und nach – jedes Mal eine Funktion, und erst nach der Prüfung die nächste. Genau das ist die Strategie der „kleinen schnellen Schritte“ in der Praxis.

#### 2. Projekt 2: Full-Stack-Ausgabenverwaltung (Fortgeschrittene)

##### 1. Anforderungsdenken und PRD

Ziel: eine Full-Stack-App zur Ausgabenverwaltung mit Frontend, Backend und Datenbank. Dieses Projekt ist deutlich komplexer als das erste und nutzt die Anforderungs-Engineering-Methoden aus Kapitel 40.

Schreibe zuerst das PRD. Nach der Vorlage aus Abschnitt 3 von Kapitel 40 formulierst du Projektüberblick, Funktionsliste, technische Lösung, Datenmodell und Entwicklungsplan. Bei der technischen Lösung gilt das Prinzip „Simplicity First“ – im Frontend React, aber ohne komplexe State-Verwaltung wie Redux; im Backend Node.js, aber ohne Microservices; als Datenbank SQLite statt PostgreSQL (in der Entwicklungsphase).

Der Entwicklungsplan zerfällt in 5 Schritte: Schritt 1: Backend-API-Skelett (Express-Server + SQLite + CRUD-Endpunkte); Schritt 2: Grundseiten des Frontends (Eintragsliste + Hinzufügen-Formular); Schritt 3: Frontend und Backend verbinden (API-Aufrufe + Datenanzeige); Schritt 4: Kategorien und Filter; Schritt 5: Monatsbilanz und einfache Diagramme. Nach jedem Schritt liegt etwas „Benutzbares“ vor.

##### 2. Die Projektgedächtnis-Datei anlegen

Lege vor dem ersten Code die Projektgedächtnis-Datei an. Das ist die Kernpraxis des Context-Engineerings – so weiß die KI zu Beginn jedes Dialogs, worum es im Projekt geht.

::: div .code-block
:::inline div .code-head
<span>CLAUDE.md</span><span class="dots">···</span>
:::

```
# Projekt: Full-Stack-Ausgaben-App
## Überblick
Ausgaben-App mit Erfassung von Einnahmen und Ausgaben, Kategorien und Monatsübersichten.
## Tech-Stack
- Frontend: React + TypeScript + Vite
- Backend: Node.js + Express + TypeScript
- Datenbank: SQLite (über better-sqlite3)
- Geteilte Typen für Frontend und Backend
## API-Konventionen
- Basispfad: /api
- Antwortformat: { success: boolean, data: any, error: string }
- RESTful-Stil
## Datenmodell
Record { id, amount, type, category, note, date }
## Code-Konventionen
- TypeScript im Strict-Modus
- Einrückung mit 2 Leerzeichen
- Funktionen mit JSDoc-Kommentar
- Kommentare und Commit-Meldungen auf Deutsch
```
:::

##### 3. Schrittweise umsetzen

Arbeite den Entwicklungsplan ab und nutze für jeden Schritt einen eigenen Dialog. Hier ein Beispiel für die Anweisung des ersten Schritts:

::: div .code-block
:::inline div .code-head
<span>Anweisung an die KI (Step 1)</span><span class="dots">···</span>
:::

```
Ich brauche das Grundgerüst der Backend-API.
Anforderungen:
1. Express-Server, Port 3001
2. SQLite-Datenbank, Tabelle records
3. Felder der Tabelle records:
   id (TEXT PRIMARY KEY)
   amount (REAL)
   type (TEXT: 'income'|'expense')
   category (TEXT)
   note (TEXT)
   date (TEXT: YYYY-MM-DD)
4. CRUD-Endpunkte:
   GET /api/records - alle Einträge abrufen
   POST /api/records - Eintrag anlegen
   PUT /api/records/:id - Eintrag aktualisieren
   DELETE /api/records/:id - Eintrag löschen
5. Middleware für Fehlerbehandlung
Gib die vollständige Backend-Code-Struktur.
```
:::

Beachte die Eigenschaften dieser Anweisung: Sie beschreibt nur den aktuellen Schritt (das Backend-Skelett) und mischt keine Frontend-Wünsche hinein; sie nennt Felder und Endpunkte ausdrücklich (gibt der KI genügend Rahmen), überlässt die konkrete Umsetzung aber der KI; sie folgt dem Prinzip „Goal-Driven Execution“ – sie sagt, „was“ zu tun ist, nicht „wie“.

Sobald die KI den Code liefert, prüfe sofort: Starte den Server und teste jeden Endpunkt mit curl oder Postman. Wenn alles passt, öffnest du einen neuen Dialog für Schritt 2 (Grundseiten des Frontends). Jeder Schritt folgt dem Kreislauf „Anweisung – Prüfung – neuer Dialog“.

#### 3. Projekt 3: KI-gestützte App (Profi)

##### 1. Projektidee

Ziel: eine App, die eine LLM-API einbindet – etwa ein „KI-Lernassistent“: Der Nutzer gibt Lernstoff ein, die KI erstellt Zusammenfassungen, verknüpft Wissenspunkte und schlägt Lernressourcen vor. Das Besondere an diesem Projekt: Deine App ruft selbst KI auf, und du musst neue Probleme lösen – API-Aufrufe, Prompt-Engineering, Fehlerbehandlung und mehr.

Die wichtigste Lektion dieses Projekts: Wenn du „mit KI Code schreiben lässt, der KI aufruft“, musst du aufs Prompt-Engineering besonders achten. Auch die Prompts, mit denen deine App die LLM-API aufruft, sollten den Prinzipien dieses Leitfadens folgen – klar, prägnant, zielorientiert.

##### 2. Wichtige technische Punkte

Dieses Projekt bringt ein paar technische Punkte mit, die in den ersten beiden Projekten nicht vorkamen:

- Verwaltung der API-Schlüssel: Schlüssel gehören niemals in den Code – verwalte sie über Umgebungsvariablen;
- Verarbeitung von Streaming-Antworten: LLMs antworten meist als Stream, der Zeichen für Zeichen angezeigt werden muss;
- Kontrolle des Token-Verbrauchs: LLMs werden pro Token abgerechnet, die App muss den Verbrauch steuern;
- Verwaltung von Prompt-Vorlagen: verschiedene Funktionen brauchen verschiedene Prompt-Vorlagen – strukturiert gepflegt.

All diese Punkte kann die KI für dich umsetzen – aber du musst das „Warum“ hinter jedem Punkt verstehen: Warum dürfen Schlüssel nicht hardcodiert werden? Warum braucht es Streaming-Antworten? Warum muss der Token-Verbrauch kontrolliert werden? Erst wenn du das „Warum“ verstehst, kannst du beurteilen, ob die Lösung der KI stimmig ist.

#### 4. Universelle Praxis-Checkliste

Groß oder klein – hier ist eine universelle Checkliste für KI-Programmierprojekte. Gehe sie bei jedem neuen Projekt einmal durch, damit kein wichtiger Schritt fehlt.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Phase</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Was tun?</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Zugehöriges Prinzip</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1. Anforderungen durchdenken</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Die fünf Anforderungselemente durchgehen und klären, was entstehen soll</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Think Before Coding</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2. Anforderungen zerlegen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Große Anforderungen in kleine, einzeln prüfbare Schritte zerlegen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Simplicity First</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3. PRD schreiben</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Als strukturiertes Dokument festhalten, als Referenz dienen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Goal-Driven</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">4. Gedächtnis-Datei anlegen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">CLAUDE.md oder eine vergleichbare Datei anlegen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Harness Engineering</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">5. Schrittweise umsetzen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ein Dialog pro Schritt: Anweisung – Prüfung – nächster Schritt</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Surgical Changes</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6. Testen und Prüfen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Direkt nach jedem Schritt die korrekte Funktion testen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">7. Code-Review</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Architektur, Sicherheit und Wartbarkeit prüfen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8. Iterieren und Verbessern</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Auf Basis von Test- und Reviewergebnissen weiter verbessern</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Universelle Praxis-Checkliste fürs KI-Programmieren

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Los geht's: Diese Woche „Projekt 1“ abschließen

{class="mt-1"}
Mach die „persönliche Tool-Seite“ aus Abschnitt 1 von Kapitel 44 zu deiner ersten KI-Programmieraufgabe: Nimm dir 5 Minuten für die fünf Anforderungselemente, schick die Anweisung an die KI (welches Tool auch immer) und nimm die Abnahme mit der dreistufigen Prüfung vor. In 30 Minuten ist sie fertig – und dein erstes KI-Programmierprojekt ist da. Speichere es gut auf: Es ist dein Andenken an den Sprung vom „Leser“ zum „Praktiker“.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Kapitelfazit

- Projekt 1 (Einsteiger): reine Frontend-Tool-Seite – den kompletten Ablauf erleben, in 30 Minuten machbar
- Projekt 2 (Fortgeschrittene): Full-Stack-Ausgabenverwaltung – PRD + Gedächtnis-Datei + Umsetzung in 5 Schritten, jeder Schritt „benutzbar“
- Projekt 3 (Profi): KI-Lernassistent – mit KI Code schreiben, der KI aufruft; aufs Prompt-Engineering achten
- Der universelle Ablauf in 8 Schritten: Anforderungen durchdenken → zerlegen → PRD → Gedächtnis-Datei → schrittweise umsetzen → testen → Review → iterieren
- Jeder Schritt folgt dem Kreislauf „Anweisung – Prüfung – neuer Dialog“
:::
