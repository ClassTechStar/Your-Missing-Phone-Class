---
id: di-si-shi-san-zhang
num: 43
part: ai-biancheng-pian
nav: Kapitel 43: Konversations-Engineering – effizient dialogieren
toc: default
kind: chapter
---

### Kapitel 43: Dialog-Engineering – Dialogtechniken für effiziente Zusammenarbeit mit der KI

{class="chapter-intro mb-4"}
Dialog ist die zentrale Interaktionsform beim KI-Programmieren. Aber Achtung: „Dialog“ ist nicht gleich „Plaudern“ – ein effizientes KI-Programmiergespräch ist eine strukturierte Kommunikationstechnik, die wir „Dialog-Engineering“ nennen. Es untersucht: Wie bekommt man mit möglichst wenigen Dialogrunden die höchste Codequalität? Ganz platt gesagt: Dieses Kapitel zeigt dir, wie du mit der KI „klar redest“.

#### 1. Ebenen-Strategie für Prompts

Der Dialog mit der KI lässt sich in drei Ebenen gliedern, und jede Ebene übernimmt eine eigene Aufgabe. Wenn du diese drei Ebenen verstehst, kannst du effiziente Prompts wie mit Bauklötzen zusammenbauen.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ebene</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Funktion</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Beispiel</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Häufigkeit</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Systemebene</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Legt die Rolle der KI und die globalen Rahmenbedingungen fest</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">„Du bist ein React-Experte, der Code muss in TypeScript geschrieben werden“</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Einmal zu Beginn des Projekts festlegen</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Aufgabenebene</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Beschreibt die konkrete anstehende Aufgabe</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">„Baue eine Formularkomponente mit Feldern für Benutzername und Passwort“</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Zu Beginn jeder Aufgabe geben</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Feedback-Ebene</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bewertet und korrigiert die Ergebnisse der KI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">„Beim Passwortfeld fehlt der Umschalter für Anzeigen/Verbergen, bitte ergänzen“</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Je nach Qualität der Ergebnisse geben</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Die drei Ebenen des Dialog-Prompts

Prompts der Systemebene stehen meist in der Projektgedächtnis-Datei (z. B. CLAUDE.md) und müssen nicht bei jedem Dialog wiederholt werden. Die Aufgabenebene nutzt du im Dialog am häufigsten – sie sollte die drei Elemente „Was ist zu tun“, „Mit welcher Technik“, „Welche Rahmenbedingungen“ enthalten. Die Feedback-Ebene verlangt das meiste Können – gutes Feedback lässt die KI präzise korrigieren, schlechtes Feedback lässt sie nur erneut raten.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tipp: Feedback in drei Schritten

{class="mt-1"}
Eine praktische Feedback-Vorlage lautet: „Problem benennen + Erwartung erklären + Kontext liefern“. Zum Beispiel: „Die Fehlerbehandlung in Zeile 25 nutzt nur console.log (Problem benennen), in der Produktionsumgebung sollte ein einheitlicher Fehlerbehandler mit nutzerfreundlichen Meldungen zum Einsatz kommen (Erwartung erklären), im Projekt gibt es dafür eine handleError-Funktion (Kontext liefern)“. Ein solches Feedback ist zehnmal wirksamer als „Ändere mal die Fehlerbehandlung“.
:::

#### 2. Debug-Dialoge: Fehler so beschreiben, dass die KI sie schnell findet

Debugging ist eine der häufigsten Situationen beim KI-Programmieren. Wenn du auf einen Bug stößt, entscheidet die Beschreibung des Problems gegenüber der KI direkt darüber, wie schnell sie es eingrenzen und beheben kann. Hier die vier Kernpunkte für Debug-Dialoge:

1. Lass die KI die Originaldaten „sehen“, nicht nur deine Wiedergabe. Hänge Fehlerprotokolle, Stacktraces und den relevanten Code direkt per @-Verweis an, statt sie mit „da gab's wohl irgendeinen Fehler“ zu umschreiben. Mit den Originaldaten arbeitet die KI genauer als mit deiner Interpretation.
2. Beschreibe den Unterschied zwischen erwartetem und tatsächlichem Verhalten. „Ich erwarte, dass der Klick auf den Button zur Startseite führt (erwartet), aber tatsächlich passiert beim Klick nichts (tatsächlich)“ – diese Beschreibung nützt viel mehr als „Der Button ist kaputt“.
3. Liefere Reproduktionsschritte. „Erst den Benutzernamen eingeben, dann auf den Anmelde-Button klicken – und der Fehler erscheint“ – Reproduktionsschritte lassen die KI deinen Weg nachspielen und das Problem leichter eingrenzen.
4. Sage klar, was du schon probiert hast. „Ich habe die Netzwerkanfrage geprüft, sie antwortet mit 200, die Daten sind in Ordnung“ – so kann die KI bereits Geprüftes ausschließen und keine Zeit mit doppelter Suche verschwenden.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Schlechte Fehlerbeschreibung

{class="font-mono text-xs leading-relaxed"}
Auf den Buttonklick reagiert nichts, schau mal nach
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Gute Fehlerbeschreibung

{class="font-mono text-xs leading-relaxed"}
Nach dem Klick auf den Anmelde-Button reagiert die Seite nicht. Erwartetes Verhalten: Nach dem Klick wird zur Seite /home navigiert Tatsächliches Verhalten: Nach dem Klick passiert nichts, die Konsole zeigt keinen Fehler Reproduktionsschritte: 1. Auf der Login-Seite Benutzername admin und Passwort 123456 eingeben 2. Auf den Button „Anmelden“ klicken 3. Die Seite reagiert nicht Bereits geprüft: - Netzwerkanfrage normal, Rückgabe 200 - onClick-Ereignis ist gebunden - Code der Komponente LoginButton geprüft Relevante Dateien: @src/components/LoginButton.tsx @src/pages/Login.tsx
:::
:::

#### 3. Iterationsstrategie: Kleine schnelle Schritte vs. großes Refactoring

Beim KI-Programmieren gibt es zwei grundlegende Iterationsstrategien für unterschiedliche Situationen. Wer den Unterschied versteht, trifft in jeder Lage die richtige Wahl.

Die Strategie der „kleinen schnellen Schritte“ eignet sich für Funktionsentwicklung und Bugfixes. Ihr Kern: Die KI macht jeweils nur eine kleine Änderung, und erst nach bestandener Prüfung kommt die nächste. Vorteil: Jeder Schritt ist prüfbar und rückholbar, das Risiko bleibt kontrollierbar. Nachteil: Es geht langsamer und braucht viele Dialogrunden. Geeignet für: Entwicklung neuer Funktionen, exploratives Vorgehen, wenn die beste Lösung noch unklar ist, und vorsichtiges Iterieren, solange du den Ergebnissen der KI noch nicht ganz traust.

Die Strategie des „großen Refactorings“ eignet sich für großflächige Änderungen mit klarem Ziel. Ihr Kern: Das vollständige Ziel wird auf einmal beschrieben, und die KI plant und führt die gesamte Änderung selbstständig aus. Vorteil: Es geht schnell, und weil die KI das Gesamtbild sieht, trifft sie bessere Architekturentscheidungen. Nachteil: Das Risiko ist hoch – versteht die KI etwas falsch, ist die Korrektur aufwendig. Geeignet für: klar umrissene Architektur-Upgrades, groß angelegte Code-Migrationen und Refactorings mit ausreichender Testabdeckung.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Aspekt</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kleine schnelle Schritte</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Großes Refactoring</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Umfang pro Änderung</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ein Funktionspunkt oder ein Bug</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ein Modul oder eine Architekturebene</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prüffrequenz</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Direkt nach jeder Änderung prüfen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prüfen, sobald alle Änderungen fertig sind</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dialogrunden</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Viele (5–10 Runden pro Funktion)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wenige (1–3 Runden pro Modul)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Risiko</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Niedrig, jeder Schritt ist rückholbar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hoch, Korrekturen bei Abweichungen sind aufwendig</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Geeignete Szenarien</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Neue Funktionen, explorative Entwicklung</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Refactoring und Migration mit klarem Ziel</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Voraussetzungen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Keine besonderen Anforderungen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Testabdeckung erforderlich</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Vergleich der beiden Iterationsstrategien

In der Praxis kombiniert man beide Strategien oft. Bei einem Modul-Refactoring lässt du die KI zunächst mit dem „großen Refactoring“ einen Gesamtplan erstellen; nach der Prüfung des Plans setzt du ihn mit „kleinen schnellen Schritten“ Stück für Stück um. So behältst du die Gesamtübersicht und kontrollierst zugleich das Ausführungsrisiko.

#### 4. Kontextmanagement bei langen Dialogen

Mit jeder zusätzlichen Dialogrunde musst du den Kontext aktiv verwalten, damit die KI frühere Informationen nicht „vergisst“. Hier einige praktische Techniken fürs Kontextmanagement.

Erstens: Kerninformationen „verankern“. Schreibe die wichtigsten Rahmenbedingungen zu Beginn des Dialogs klar nieder und wiederhole sie im weiteren Verlauf passend. Zum Beispiel: „Denk dran, unsere Daten liegen im localStorage, eine Datenbank können wir nicht benutzen“ – wiederhole diese Bedingung bei passenden Änderungswünschen, damit die KI sie nicht vergisst.

Zweitens: Nutze die Technik „Zusammenfassen und Weitermachen“. Wenn der Dialog sehr lang geworden ist, lass die KI „den bisherigen Stand und die offenen Aufgaben zusammenfassen“, und starte dann einen neuen Dialog mit dieser Zusammenfassung als Ausgangspunkt. So bleibt der wichtige Kontext erhalten, ohne dass der lange Dialog sich abnutzt.

Drittens: „Ein Dialog, eine Aufgabe“. Das ist die einfachste und zugleich wirksamste Strategie fürs Kontextmanagement. Jeder Dialog behandelt nur eine Aufgabe oder einen Funktionspunkt; danach startest du einen neuen Dialog für die nächste. Das begrenzt die Dialoglänge ganz natürlich und hält den Kontext klar.

Viertens: Nutze die Kontextfunktionen deiner Tools. Die meisten KI-Programmier-Tools haben einen Button „Kontext löschen“ oder „Neue Sitzung“ – wenn du spürst, dass die Antworten der KI nachlassen, zögere nicht: Neue Sitzung. Etwas Dialoghistorie zu verlieren ist viel besser, als sich weiter durch einen abgenutzten Kontext zu kämpfen.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Los geht's: Spiel für deine KI einmal den „Patienten“

{class="mt-1"}
Baue absichtlich eine kleine Seite im Browser und erzeuge einen Bug (etwa einen Button, der nicht reagiert). Beschreibe das Problem dann einmal vollständig nach dem Muster der „guten Fehlerbeschreibung“ aus diesem Kapitel: Originaldaten, erwartet vs. tatsächlich, Reproduktionsschritte, bereits Geprüftes. Spüre, wie unterschiedlich schnell die KI das Problem eingrenzt – dann verstehst du, warum „Probleme beschreiben“ selbst ein Handwerk ist.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Kapitelfazit

- Prompt in drei Ebenen: Systemebene (in die Gedächtnis-Datei), Aufgabenebene (Was + Technik + Rahmenbedingungen), Feedback-Ebene (Problem + Erwartung + Kontext)
- Debugging in vier Punkten: Originaldaten liefern, erwartet vs. tatsächlich, Reproduktionsschritte, bereits Geprüftes
- Kleine schnelle Schritte: wenig Risiko, viele Runden, ideal für neue Funktionen; großes Refactoring: hohes Risiko, wenige Runden, braucht Tests als Absicherung
- Kontextmanagement in vier Zügen: Kerninfos verankern, Zusammenfassen und Weitermachen, ein Dialog pro Aufgabe, konsequent neue Sitzung starten
:::
