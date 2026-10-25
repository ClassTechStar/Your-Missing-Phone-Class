---
id: di-san-shi-jiu-zhang
num: 39
part: ai-biancheng-pian
nav: Kapitel 39: Kontext-Engineering – damit die KI versteht, was du willst
toc: default
kind: chapter
---

### Kapitel 39: Kontextengineering – damit KI Ihre Absicht versteht

{class="chapter-intro mb-4"}
Kennst Sie das: Ein neues Chat-Fenster, und die KI scheint alles vergessen zu haben? Das ist keine Böswilligkeit, sondern „Vergesslichkeit“ von Natur aus. Dieses Kapitel zeigt, wie man der KI ein „Langzeitgedächtnis“ verpasst – und stellt eine der angesagtesten Entwicklungsparadigmen 2026 vor: spec-driven development.

#### 1. Projektgedächtnisdatei: Das „Langzeitgedächtnis“ der KI

Ein grundlegendes Limit: Das Gedächtnis der Modelle ist kurzlebig. Zu Beginn jeder Konversation kennt die KI Ihr Projekt nicht. Sie müssten immer wieder sagen: „Wir nutzen React“, „Backend ist Node.js“, „Datenbank PostgreSQL“, „Code-Stil mit doppelten Anführungszeichen“. Das ist mühsam und fehleranfällig – wie tägliches Onboarding für neue Kollegen.

Die Lösung: eine Projektgedächtnisdatei im Projektstamm. KI-Werkzeuge lesen sie automatisch beim Gesprächsstart. Die Benennung unterscheidet sich je Tool:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Werkzeug</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dateiname</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cursorrules</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">CLAUDE.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitHub Copilot</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">copilot-instructions.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Allgemeine Lösung</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">AGENTS.md</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Benennungskonventionen für Projektgedächtnisdateien

Andere Namen, gleiche Idee: Alles, was die KI „immer wissen“ soll, gehört in diese Datei. Eine gute Projektgedächtnisdatei enthält: Projektüberblick, Technikstack, Code-Konventionen (Namensgebung, Einrückung, Kommentare), Verzeichnisstruktur, Entwicklungsabreden (Branch-Strategie, Commit-Regeln, Testanforderungen). Karpathys CLAUDE.md umfasst nur 70 Zeilen, deckt aber alle Schlüsselinfos ab – knapp und vollständig.

::: div .code-block
:::inline div .code-head
<span>CLAUDE.md</span><span class="dots">···</span>
:::

```
# Projekt: App zur Verwaltung persönlicher Ausgaben
## Überblick
Eine Full-Stack-App zur Verwaltung persönlicher Ausgaben, mit der der Nutzer Einnahmen und Ausgaben des Alltags festhält.
## Tech-Stack
- Frontend: React + TypeScript + Tailwind CSS
- Backend: Node.js + Express + TypeScript
- Datenbank: SQLite (Entwicklung) / PostgreSQL (Produktion)
- Tests: Vitest
## Code-Konventionen
- Doppelte Anführungszeichen verwenden
- Einrückung mit 2 Leerzeichen
- Funktionsnamen in camelCase
- Typdefinitionen in PascalCase
- Jede Funktion braucht einen JSDoc-Kommentar
## Verzeichnisstruktur
/src
  /frontend  - Frontend-Code
  /backend   - Backend-Code
  /shared    - gemeinsame Typen für Frontend/Backend
  /tests     - Testdateien
## Entwicklungskonventionen
- Commit-Meldungen auf Deutsch
- Neue Funktionen immer zuerst mit Test
- API-Antworten durchgängig im Format { success, data, error }
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Hinweis: Nicht zur „zweiten Anforderungsdoku“ verkommen lassen

{class="mt-1"}
Achten Sie auf die Länge – keine Dutzende von Seiten. Ziel ist, der KI schnell Hintergrund zu geben, nicht jedes Feature auszuführen. Klar, strukturiert, nur das Nötige.
:::

#### 2. Spec-Driven Development (SDD)

Spec-Driven Development (SDD) ist ein reifendes Paradigma 2026, Kernsatz: Erst Spezifikation, dann Code. Anders als klassisches TDD umfasst die „Spec“ nicht nur Tests, sondern auch Anforderungen, Schnittstellen und Datenmodelle. Die KI generiert Code daraus, Menschen schreiben und pflegen die Spezifikation.

Der SDD-Ablauf in fünf Schritten:

1. Anforderungen in natürlicher Sprache beschreiben (als .md-Datei);
2. Schnittstellen und Datenstrukturen festlegen (in der Spec-Datei);
3. KI generiert die Implementierung nach Spec;
4. Tests prüfen, ob das Ergebnis zur Spec passt;
5. Falls nicht: Spec korrigieren oder KI den Code nachbessern lassen.

In diesem Ablauf ist die Spec-Datei die „einzige Wahrheitsquelle“ – Code lässt sich neu erzeugen, die Spec muss stimmen.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Spezifikationsdokument schreiben</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Ist die Spezifikation vollständig?</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Vollständig</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> KI generiert Code nach der Spezifikation</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Tests laufen lassen, um das Ergebnis zu prüfen</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> Unvollständig / Tests schlagen fehl</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-tools mr-1"></i> Code-Problem → Code korrigieren; Spezifikationsproblem → Spezifikation korrigieren</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> Zurück zur Prüfung</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Alles bestanden → Auslieferung</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Abbildung 3: Arbeitsablauf von Spec-Driven Development (SDD)
:::

Vorteil: Spezifikationen sind stabiler als Code. Wechseln Modell oder Werkzeug, bleibt Ihre Spec gültig – der neue Generator setzt sie um. Deshalb betont dieses Buch „Methodik vor Werkzeug“: Die Spec-Datei ist der konkrete Träger Ihrer Methodik.

#### 3. Kontextfenster verwalten

Selbst mit Projektgedächtnis stößt man im Gespräch an Grenzen des Kontextfensters (der gleichzeitig verarbeitbaren Informationsmenge). Bei zu langen Dialogen und vielen Dateien „vergisst“ die KI frühere Inhalte, die Qualität sinkt – wie nach sechs Stunden Plaudern mit einem Freund, der den ersten Satz längst vergessen hat.

Kernstrategie: „geschichtetes Zitieren“:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kontextebene</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Inhalt</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Handhabung</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ebene 1: Projektgedächtnis</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Technikstack, Konventionen, Verzeichnisbaum</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">In CLAUDE.md o. Ä. ablegen, wird automatisch geladen, nicht wiederholen</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ebene 2: Datei-Referenzen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Code-Dateien der aktuellen Aufgabe</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mit @ präzise referenzieren, nicht ganze Dateien in den Chat kleben</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ebene 3: Gesprächsverlauf</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dialoghistorie der aktuellen Aufgabe</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nach Abschluss neuen Chat beginnen, um Kontext nicht aufzublähen</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ebene 4: Sofortige Anweisung</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Konkrete Anforderung dieses Schritts</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Klar, knapp, zielgerichtet – keine langatmigen Umschweife</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Geschichtete Verwaltung des Kontextfensters

#### 4. Praxispunkte fürs Kontext-Engineering

Kontext-Engineering ist keine einmalige Einstellung, sondern ein fortlaufender Optimierungsprozess. Hier ein paar Punkte, die sich in der Praxis immer wieder bewährt haben:

1. Halte die Gedächtnisdatei beim Weiterentwickeln des Projekts aktuell. Wenn du eine neue Technik einführst oder die Architektur änderst, aktualisiere sofort die Gedächtnisdatei, statt es im Chat improvisiert zu erklären.
2. Nutze @-Verweise statt alles einzufügen. Die meisten KI-Coding-Tools unterstützen die Syntax @file oder @folder; sie schiebt den Dateiinhalt im Hintergrund in den Kontext der KI – effizienter als manuelles Einfügen, ohne den Chat zu überladen.
3. Halte die Chats „kurz und knackig“. Ein Chat behandelt nur eine Aufgabe oder ein Feature. Wenn er fertig ist, starte fürs Nächste einen neuen Chat. Lange Chats verbrauchen nicht nur das Kontextfenster, sie lenken die KI auch ab.
4. Lass die KI Ergebnisse „sehen“, statt sie zu „beschreiben“. Bei einem Bug gibst du das Fehlerprotokoll direkt per @-Verweis an die KI weiter, statt in eigenen Worten zu erzählen, „da sei wohl irgendein Fehler“. Die Rohinformation nützt der KI deutlich mehr als deine Wiedergabe.
5. Räume regelmäßig auf und archiviere. Abgeschlossene Chats und temporäre Dateien belegen den Arbeitsbereich. Regelmäßiges Aufräumen hält das Projektverzeichnis sauber und hilft der KI, die Projektstruktur schneller zu erfassen.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Ausprobieren: Schreibe für dein Projekt eine 70-Zeilen-Gedächtnisdatei

{class="mt-1"}
Such dir ein Projekt aus, an dem du gerade arbeitest (oder arbeiten willst), und schreibe eine CLAUDE.md: Projektüberblick (2–3 Sätze), Tech-Stack (auflisten), Code-Richtlinien (3–5 Punkte), Verzeichnisstruktur (als Baum skizzieren), Entwicklungskonventionen (2–3 Punkte). Halte dich unter 70 Zeilen – danach wirst du merken, dass du dein Projekt selbst viel klarer verstehst.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Zusammenfassung des Kapitels

- Das Gedächtnis der KI ist „kurzzeitig“: Bei jedem neuen Chat weiß sie null über dein Projekt
- Projekt-Gedächtnisdateien (CLAUDE.md & Co.) sind das „Langzeitgedächtnis“ der KI und werden bei jedem Chat automatisch geladen
- Eine gute Gedächtnisdatei = Überblick + Tech-Stack + Richtlinien + Verzeichnis + Konventionen; 70 Zeilen genügen
- SDD, die spezifikationsgetriebene Entwicklung: erst die Spezifikation, dann der Code; die Spezifikation ist die „single source of truth“ und stabiler als der Code
- Kontext wird in vier Ebenen verwaltet: Projektgedächtnis → @-Dateiverweise → Chatverlauf → direkte Anweisungen
- Fünf Praxispunkte: aktuell halten, @-Verweise, kurze Chats, Originalinfos geben, regelmäßig aufräumen
:::
