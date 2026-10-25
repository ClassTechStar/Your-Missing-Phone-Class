---
id: di-liu-shi-jiu-zhang
num: 69
part: ios-kai-fa-pian
nav: Kapitel 69: Spickzettel und Ressourcen
toc: default
kind: chapter
---

### Kapitel 69: Spickzettel und Ressourcen

{class="chapter-intro mb-4"}
Dieses Kapitel ist ein Spickzettel, der auch für sich allein funktioniert. Wenn du dir eine Schreibweise nicht mehr merken kannst oder schnell eine Entscheidung brauchst, blätter einfach direkt hierher. Nutze es als „Taschenkarte“: Code-Spickzettel für den Alltag, häufige Fragen und Lernressourcen, Seite für Seite.

#### 1. Code-Spickzettel für den Alltag

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Was du tun willst</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Schlüsselcode</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Seiteneigener Zustand</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State private var x = startwert</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Seitenübergreifende Logik</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Observable class VM { var x = 0 }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Layout: untereinander/nebeneinander</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack { }</code> / <code class="inline">HStack { }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Flexibler Zwischenraum</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Spacer()</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Liste</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List { ForEach(array) { ... } }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Seitenwechsel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">NavigationStack + NavigationLink</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Unterer Dialog</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">.sheet(isPresented: $show) { inhalt }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Aktuelle Seite schließen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Environment(\.dismiss) var dismiss</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Daten aus dem Netz holen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">try await URLSession.shared.data(from: url)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">JSON parsen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X: Codable</code> + <code class="inline">JSONDecoder().decode</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kleine Einstellungen speichern</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults.standard.set(wert, forKey: "schlüssel")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Strukturierte Daten speichern</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Model</code> + <code class="inline">modelContainer</code> + <code class="inline">@Query</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dunkelmodus-Anpassung</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Systemfarben verwenden (.primary / Color(.systemGray6)), nichts fest im Code verankern</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tests ausführen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><kbd>⌘U</kbd></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
iOS-Entwicklung: Spickzettel (Ausgabe August 2026)

#### 2. Häufige Fragen (FAQ)

F1: Ich habe keinen Mac – kann ich die iOS-Entwicklung trotzdem lernen?

Die Sprache kannst du lernen, eine komplette Entwicklung aber nicht. Mit Swift Playgrounds auf dem iPad/iPhone kannst du den gesamten Stoff von Kapitel 61 durchnehmen; Xcode gibt es jedoch exklusiv für macOS, am Ende brauchst du also einen Mac. Bei knappem Budget kannst du übergangsweise einen Cloud-Mac mieten oder einen gebrauchten Mac mini kaufen und erst nach dem Erlernen der Sprache entscheiden, wie viel du investierst.

F2: Wie viel kostet es, iOS-Entwicklung zu lernen?

Lernphase: 0 Yuan (Xcode ist kostenlos + kostenloses Debuggen auf echten Geräten mit einer kostenlosen Apple-ID). Veröffentlichungsphase: Entwicklerkonto 99 US-Dollar pro Jahr (ca. 700 Yuan). Dazu die Hardware für einen Mac – das sind die gesamten Kosten. Gemessen am Ertrag – selbst ein kleines Tool im App Store hat zahlende Nutzer – geht diese Rechnung auf.

F3: Was lerne ich zuerst – SwiftUI oder UIKit?

SwiftUI. Neue Projekte, neue Tutorials und neue Stellen setzen 2026 auf SwiftUI, und dieses Buch nutzt es durchgehend. UIKit ist das Framework der vorherigen Generation und steckt noch in vielen älteren Projekten – sobald du SwiftUI sicher beherrschst, holst du UIKit bei Bedarf nach (Apple bietet offizielle Interoperabilitäts-Tutorials an), das geht dann recht schnell. Dreh die Reihenfolge nicht um.

F4: Lässt sich mit iOS-Entwicklung gut ein Job finden?

Die Lage 2026: Einstiegsstellen, bei denen es nur darum geht, „Oberflächen zu malen“, sind hart umkämpft – aber Entwickler, die Swift + SwiftUI beherrschen und etwas im Store veröffentlicht haben, sind weiterhin begehrt. Das mittlere Gehalt bei iOS-Stellen liegt in allen Tech-Stacks seit Jahren in der Spitzengruppe. Als Lernender ist dein bester Lebenslauf die App, die du selbst gebaut hast und die im Store steht.

F5: Was tun, wenn die App in der Prüfung abgelehnt wird?

Keine Panik, das ist ganz normal – die Wahrscheinlichkeit, beim ersten Einreichen abgelehnt zu werden, ist durchaus hoch. Apples Ablehnungsgründe sind meist sehr konkret formuliert (welche Seite, welche Richtlinie); verbessere alles Punkt für Punkt, antworte mit einer Erläuterung in App Store Connect und reiche einfach neu ein. Die drei häufigsten Ablehnungsgründe: Der Verwendungszweck von Berechtigungen ist unklar, die Oberfläche hat Bugs, oder die Metadaten (Screenshots/Beschreibung) passen nicht zur App. Wenn du diese drei Punkte vorher selbst prüfst, sparst du dir eine Runde Wartezeit.

#### 3. Die wichtigsten Xcode-Tastenkürzel

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Aktion</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tastenkürzel</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ausführen / Testen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R / ⌘U</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Canvas-Vorschau öffnen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Datei schnell öffnen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Globale Suche</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘F</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Einrückung formatieren</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kommentieren / Kommentar aufheben</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Build-Cache leeren</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘K</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Zur Definition springen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘-Klick</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Umbenennen (sicher, projektweit)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rechtsklick → Refactor → Rename</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Die wichtigsten Xcode-Tastenkürzel

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tipp: Bei mysteriösen Build-Fehlern zuerst den Cache leeren

{class="mt-1"}
Bei den Spukphänomenen der Art „gestern lief es noch, heute nicht mehr“ liegt es in sechs bis sieben von zehn Fällen an verhunztem Build-Cache. Mit ⇧⌘K bereinigen und neu bauen – das heilt die meisten dieser Rätsel. Hilft das nicht, starte Xcode neu (am besten gleich mit dem Mac), und wenn das auch nichts nützt: „Lösch den DerivedData-Ordner“ – der legendäre Dreischlag, der unter iOS-Entwicklern von Mund zu Mund geht.
:::

#### 4. Empfohlene Lernressourcen

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Typ</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ressource</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Empfehlungsgrund</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Offiziell</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">developer.apple.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Die offizielle Apple-Dokumentation; die SwiftUI-/Swift-Tutorials stecken alle darin – die Autorität Nummer eins</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Offiziell</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apples SwiftUI Tutorials</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Der offizielle Schritt-für-Schritt-Kurs, maximale Anfängerfreundlichkeit</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Offiziell</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift-Website (swift.org)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Offizielle Sprachdokumentation und Online-Playground</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Community</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hacking with Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Paul Hudsons kostenlose Tutorial-Sammlung, deren Qualität allgemein als absolute Spitzenklasse gilt</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Community</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stack Overflow (Tag „swiftui“)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Die erste Anlaufstelle bei Fehlermeldungen</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Video</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Der offizielle Apple Developer-Kanal (WWDC-Videos)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Die maßgeblichen Erklärungen zu den neuen Technologien des jeweiligen Jahres</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Design</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apples Human Interface Guidelines (HIG)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Die offizielle Bibel für Oberflächen mit echtem „Apple-Flair“</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Begleitend</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Teil 7 „KI-Programmierung in der Praxis“ (Kapitel 37–47)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Die komplette Vorgehensweise, um iOS-Entwicklung mit KI-Unterstützung zu meistern</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Liste der Lernressourcen für die iOS-Entwicklung (August 2026)

#### 5. Fazit: vom ersten App zum N-ten App

Blick zurück: Du bist von „ich weiß nicht mal, was SwiftUI ist“ bis hierher gekommen – Xcode installiert, Swift gelernt, mit SwiftUI Oberflächen gebaut, dem App Datenbank und Netzwerk angeschlossen, und schließlich getestet, gepackt und im Store veröffentlicht. Auf diesem Weg hast du den schwersten Abschnitt von null auf eins bereits gemeistert.

Die Welt der Technik ändert sich schnell: Frameworks werden aktualisiert, Werkzeuge ausgetauscht, und die KI übernimmt immer mehr der „Tastaturarbeit“. Aber eines veraltet nie: deine Fähigkeit, eine vage Idee in klare Schritte zu zerlegen und sie dann Stück für Stück umzusetzen. Werkzeuge sind Verstärker, die Denkweise ist das Fundament. Verstärker kann man austauschen, das Fundament darf nicht wackeln.

:::inline div .quote-line
Du bist nicht mehr nur "jemand, der mit dem Handy umgehen kann": Du kannst die Ideen in deinem Kopf in Apps verwandeln, die wirklich auf Hunderten Millionen iPhones laufen. Ab heute erschaffst du mit der Tastatur – das ist die Romantik des iOS-Entwicklers.
:::

#### Literaturverzeichnis

{class="list-decimal pl-6 mb-3 space-y-1 text-xs text-gray-500"}
1. Apple Inc. (2026). SwiftUI Framework Documentation. developer.apple.com.
2. Apple Inc. (2026). Swift Programming Language Guide. swift.org.
3. Apple Inc. (2026). SwiftData Framework Documentation. developer.apple.com.
4. Apple Inc. (2026). App Store Review Guidelines. developer.apple.com/app-store/review.
5. Apple Inc. (2026). Human Interface Guidelines (HIG). developer.apple.com/design.
6. Apple Inc. (2026). Xcode 27 Release Notes and App Distribution Guide.
