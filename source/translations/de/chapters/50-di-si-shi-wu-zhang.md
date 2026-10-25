---
id: di-si-shi-wu-zhang
num: 45
part: ai-biancheng-pian
nav: Kapitel 45: Qualitätssicherung – KI-Code zuverlässig machen
toc: default
kind: chapter
---

### Kapitel 45: Qualitätssicherung – KI-Code zuverlässig machen

{class="chapter-intro mb-4"}
KI-Code hat eine Eigenheit: Er „sieht meist richtig aus“ – sauber benannte Variablen, ausführliche Kommentare, klare Logik. Aber „richtig aussehen“ ist nicht „wirklich richtig“. Versteckte Probleme in KI-Code sind oft schwerer zu finden als in handgeschriebenem Code, denn die hohe Oberflächenqualität macht sorglos. Dieses Kapitel zeigt dir, wie du für KI-Code ein wirksames Qualitätssicherungssystem aufbaust – mit den drei Verteidigungslinien Tests, Review und Versionskontrolle wird aus „sieht richtig aus“ ein „ist wirklich richtig“.

#### 1. Testgetrieben: Die KI Tests schreiben lassen

Tests sind die erste Verteidigungslinie der Qualitätssicherung beim KI-Programmieren. Die gute Nachricht: Die KI Tests schreiben zu lassen ist leichter und zuverlässiger, als sie Funktionscode schreiben zu lassen – denn das erwartete Verhalten eines Tests ist eindeutig, und der typische Fall „sieht richtig aus, ist aber falsch“ tritt seltener auf.

Der testgetriebene Ablauf beim KI-Programmieren: Zuerst lässt du die KI den Funktionscode schreiben; sobald die Grundfunktion läuft, lässt du sie sofort Testfälle schreiben. Die Testfälle sollten Normalfälle, Grenzfälle und Ausnahmefälle abdecken. Danach lässt du die KI den Funktionscode anhand des Testfeedbacks korrigieren. Der Vorteil dieses Ablaufs: Sind die Tests einmal geschrieben, sind sie ein dauerhaftes Prüfinstrument – jede spätere Änderung kannst du mit einem Testlauf darauf hin kontrollieren, dass kein Regressionsfehler entsteht.

::: div .code-block
:::inline div .code-head
<span>Anweisung an die KI: Tests schreiben</span><span class="dots">···</span>
:::

```
Schreibe Unit-Tests für die Funktion calculate_discount.
Die Testfälle sollen abdecken:
1. Normalfall:
   - 100 Yuan mit 20 % Rabatt -> 80
   - 200 Yuan mit 50 % Rabatt -> 100
2. Grenzfälle:
   - 0 Yuan mit 20 % Rabatt -> 0
   - 100 Yuan ohne Rabatt -> 100 (keine Ermäßigung)
   - 100 Yuan zum Vollpreis -> 100 (voller Preis)
3. Fehlerfälle:
   - negativer Preis -> muss einen Fehler werfen
   - Rabatt > 1 -> muss einen Fehler werfen
   - Eingabe keine Zahl -> Muss einen Fehler werfen
Verwende das Vitest-Framework und gib die vollständige Testdatei.
```
:::

Beachte die Eigenschaft dieser Anweisung: Sie listet die drei Testfallarten ausdrücklich auf (Normal-, Grenz- und Ausnahmefälle) und lässt der KI keinen Spielraum für „selektives Testen“. Manchmal schreibt die KI nur Tests für den Normalweg, um schnell fertig zu wirken – wenn du alle Kategorien ausdrücklich auflistest, vermeidest du das.

#### 2. Techniken fürs Code-Review

Auch mit Testabdeckung musst du den KI-Code selbst durchsehen. Ein Code-Review heißt nicht, alles Zeile für Zeile zu lesen – das kostet zu viel Zeit und hängt zu sehr von deinem Können ab. Ein wirksames Review von KI-Code konzentriert sich auf folgende Kerndimensionen:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Review-Dimension</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Worauf achten</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Typische Probleme</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sicherheit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Eingabeprüfung, Umgang mit Schlüsseln, Schutz vor SQL-Injection</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Die KI vergisst oft die Eingabeprüfung und schreibt Schlüssel direkt in den Code</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fehlerbehandlung</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Werden Ausnahmen abgefangen? Sind die Fehlermeldungen sinnvoll?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Die KI nutzt gern leere catch-Blöcke oder nur console.log</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Leistung</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gibt es offenkundige Leistungsprobleme wie N+1-Abfragen oder Endlosschleifen?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Die KI schreibt manchmal Algorithmen in O(n²)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wartbarkeit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ist die Code-Struktur klar? Sind die Bezeichner aussagekräftig?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Die KI erzeugt gelegentlich überabstrahierten Code</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Abhängigkeitsverwaltung</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sind die eingesetzten Abhängigkeiten nötig? Sind die Versionen klar definiert?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Die KI bindet gern unnötige Bibliotheken ein</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kerndimensionen des KI-Code-Reviews

Beim Review musst du nicht alles selbst durchgehen – lass die KI die erste Runde übernehmen. Anweisung zum Beispiel: „Prüfe bitte Sicherheit, Fehlerbehandlung und Leistung dieses Codes und nenne potenzielle Probleme.“ Die Selbstprüfungsfähigkeit der KI wird immer besser; sie ersetzt das menschliche Review zwar nicht vollständig, filtert aber die meisten offenkundigen Probleme heraus.

#### 3. Versionskontrolle: Die Rolle von Git beim KI-Programmieren

Git ist beim KI-Programmieren noch wichtiger als in der klassischen Programmierung. Da jede KI-Änderung unvorhersehbare Folgen haben kann, brauchst du ein verlässliches „Rückgängig“ – die Versionskontrolle ist genau dieses Rückgängig.

Die Git-Best-Practice beim KI-Programmieren lautet: „Häufig committen, in kleinen Schritten vorangehen.“ Nach jedem überprüfbaren Funktionspunkt kommt ein Commit. So kannst du, wenn eine Änderung der KI Probleme macht, gezielt zum letzten funktionierenden Stand zurückkehren, statt alle Arbeit über den Haufen zu werfen.

Ein weiterer praktischer Trick ist die „Branch-Isolation“. Für KI-Änderungen mit ungewissem Ausgang (etwa ein großes Refactoring) legst du zuerst einen neuen Branch an und arbeitest dort. Gefällt das Ergebnis, mergest du in den Hauptbranch zurück; gefällt es nicht, löschst du den Branch einfach – der Hauptbranch bleibt unberührt. Das ist viel sicherer, als immer wieder am Hauptbranch herumzubasteln.

1. Vor jeder KI-Änderung: Vergewissere dich, dass das Arbeitsverzeichnis sauber ist (keine uncommitteten Änderungen). Dann kannst du bei einem misslungenen Ergebnis mit git checkout . schnell zurücksetzen.
2. Sobald die KI eine Änderung gemacht hat und die Prüfung bestanden ist, sofort committen. Die Commit-Meldung beschreibt, was die Änderung bewirkt, z. B. „feat: Benutzerregistrierung hinzugefügt“.
3. Für große Refactorings zuerst einen Branch anlegen: git checkout -b refactor/auth-system. Die Änderungen auf dem Branch fertigstellen und erst nach bestandenen Tests mergen.
4. Gewöhne dir an, den Diff anzusehen. Nach jeder KI-Änderung zeigt dir git diff, was genau geändert wurde. Das hilft dir nicht nur, Probleme zu entdecken, sondern auch, vom Code zu lernen.

#### 4. Häufige Stolperfallen und wie du sie vermeidest

Beim KI-Programmieren gibt es einige Stolperfallen, die immer wieder auftauchen und in die fast alle Einsteiger tappen. Wer sie kennt, erspart sich viele Umwege.

##### 1. Falle 1: Die Vertrauensfalle

„Der Code der KI sieht so professionell aus, da kann doch nichts falsch sein?“ – das ist die gefährlichste Falle. KI-generierter Code ist oberflächlich sehr ordentlich – saubere Namen, ausführliche Kommentare, klare Struktur – und genau dieser „professionelle Schein“ macht sorglos. Aber ordentliche Oberfläche heißt nicht korrekte Logik. Gegenmittel: Immer per Tests verifizieren, niemals danach urteilen, ob etwas „richtig aussieht“.

##### 2. Falle 2: Die Aufbläh-Falle

„Da die KI mir Code schreibt, warum nicht gleich ein bisschen mehr ausbauen?“ – das führt zu aufgeblähtem Code. Die KI „schenkt“ gern etwas dazu: Du willst eine Login-Seite und bekommst ein komplettes Nutzerverwaltungssystem. Überflüssige Funktionen erhöhen nicht nur die Komplexität, sondern auch die Wahrscheinlichkeit von Bugs. Gegenmittel: Konsequent beim Prinzip „Simplicity First“ bleiben und der KI klar sagen: „Nur diese Funktion, nichts zusätzlich.“

##### 3. Falle 3: Die Verständnisfalle

„Die KI versteht mich doch bestimmt?“ – nicht unbedingt. Das Verständnis der KI ist zwar stark, aber bei vagen Anforderungen bleibt ihr nur das „Raten“. Rät sie falsch, ist der produzierte Code falsch. Ärgerlicher noch: Falsch geratener Code „sieht meist plausibel aus“, und du hältst ihn fälschlich für verstanden. Gegenmittel: In der Anweisung genug konkrete Details liefern, damit der KI wenig Raum zum „Raten“ bleibt.

##### 4. Falle 4: Die Kontextfalle

„Das habe ich doch im früheren Dialog gesagt, die KI erinnert sich sicher?“ – sehr wahrscheinlich nicht. Mit wachsender Dialoglänge oder einer neuen Sitzung verliert die KI frühere Kontexte. Wurde eine wichtige Randbedingung nicht in die Projektgedächtnis-Datei geschrieben, wird sie in späteren Änderungen leicht ignoriert. Gegenmittel: Wichtige Randbedingungen gehören in die Projektgedächtnis-Datei – verlass dich nicht auf das Dialoggedächtnis.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Die vier Fallen auf einen Blick

{class="mt-1"}
Vertrauensfalle – glaub nicht dem „richtig Aussehen“; Aufbläh-Falle – die KI „schenkt“ gern dazu; Verständnisfalle – bei vagen Anforderungen „rät“ sie; Kontextfalle – das Dialoggedächtnis „vergisst“. Die Gegenmittel dazu: mit Tests verifizieren, Überflüssiges streichen, genug Details liefern, in die Gedächtnis-Datei schreiben.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Los geht's: Bau drei Verteidigungslinien für dein Projekt

{class="mt-1"}
Wenn du mit Projekt 1 (die Tool-Seite) schon angefangen hast: ① Lass die KI für die Kernfunktionen Testfälle in allen 3 Kategorien schreiben; ② gehe den Code einmal nach den fünf Dimensionen durch (Sicherheit / Fehlerbehandlung / Leistung / Wartbarkeit / Abhängigkeiten); ③ initialisiere das Projekt mit git und lege den ersten Commit an. Erst wenn alle drei Verteidigungslinien stehen, gehört dein Projekt wirklich dir.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Kapitelfazit

- KI-Code „sieht richtig aus“ ≠ „ist wirklich richtig“ – die hohe Oberflächenqualität macht gerade sorglos
- Tests von der KI schreiben lassen: Normal-/Grenz-/Ausnahmefälle ausdrücklich auflisten und „selektives Testen“ verhindern
- Fünf Review-Dimensionen: Sicherheit, Fehlerbehandlung, Leistung, Wartbarkeit, Abhängigkeitsverwaltung
- Git ist das „Rückgängig“: häufig committen, kleine Schritte, Branch-Isolation, regelmäßig den Diff ansehen
- Die vier Fallen: Vertrauen (per Tests prüfen), Aufblähen (Überflüssiges streichen), Verstehen (genug Details liefern), Kontext (in die Gedächtnis-Datei schreiben)
:::
