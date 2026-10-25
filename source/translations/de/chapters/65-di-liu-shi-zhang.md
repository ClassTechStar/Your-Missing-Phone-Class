---
id: di-liu-shi-zhang
num: 60
part: ios-kai-fa-pian
nav: Kapitel 60: Entwicklungsumgebung einrichten – Xcode und das erste Projekt
toc: default
kind: chapter
---

### Kapitel 60: Entwicklungsumgebung einrichten – Xcode und das erste Projekt

{class="chapter-intro mb-4"}
Will der Handwerker gut arbeiten, muss sein Werkzeug scharf sein. In diesem Kapitel bauen wir die „Küche“ auf: Xcode installieren, den Simulator zum Laufen bringen, dein allererstes iOS-Projekt anlegen und die Projektstruktur auseinandernehmen, bis alles klar ist. Nach der Einrichtung wirst du zum ersten Mal sehen, wie dein eigener Code zu einem anklickbaren Button wird – diesen Moment behalten viele ein Leben lang.

#### 1. Einen Mac besorgen

Zuerst zur Hürde: iOS-Entwicklung läuft zwingend unter macOS. Ohne Mac hast du drei Optionen: einen kaufen (auch ein gebrauchter Mac mini oder ein MacBook Air genügt), kurzfristig einen Cloud-Mac mieten oder zuerst Teil 8 lesen, „Android-Entwicklung in der Praxis“ (das geht unter Windows).

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Komponente</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Minimum</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Komfortzone (empfohlen)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Chip</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Silicon (ab M1)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">M2 oder neuer</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Arbeitsspeicher</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8GB</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">16GB</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Speicherplatz</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">40 GB+ einplanen (Xcode selbst ist ein Brocken)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ab 256 GB</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">System</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">das neueste macOS</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">automatische Updates aktiv lassen</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Referenzkonfiguration für den Mac-Entwicklungsrechner (August 2026)

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tipp: Auch ohne Mac kannst du schon die Sprache lernen

{class="mt-1"}
Die kostenlose App Swift Playgrounds aufs iPad vermittelt die Swift-Grundlagen (kein Mac nötig); sie läuft sogar auf dem iPhone. Spiel die Sprachkenntnisse aus Kapitel 61 erst in Playgrounds ein – sobald der Mac da ist, geht es direkt durchstarten. „Ein scharfes Messer kostet Zeit, spart sie aber beim Hacken“ – genau das ist gemeint.
:::

#### 2. Xcode installieren

Xcode ist Apples offizielle integrierte Entwicklungsumgebung – und kostenlos. In drei Schritten installiert:

1. Auf dem Mac den App Store öffnen, nach „Xcode“ suchen und auf Installieren klicken – es sind etliche Gigabyte, such dir eine Zeit mit gutem Netz;
2. Beim ersten Start die Vereinbarung akzeptieren und die Komponenten installieren (läuft automatisch);
3. Im Menü Xcode → Settings → Locations prüfen, dass Command Line Tools ausgewählt ist – die Kommandozeilenwerkzeuge sind Voraussetzung für viele Skripte und Drittanbieter-Tools.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Achtung: Version und System müssen zusammenpassen

{class="mt-1"}
Ein neues Xcode verlangt oft das neueste macOS, alte Macs bleiben dann auf der alten Version hängen. Für die App-Store-Veröffentlichung verlangt Apple einen Build mit relativ aktuellem Xcode (meist mit einer Karenzzeit). Schiebe Systemupdates also nicht zu lange auf – iOS-Entwickler gehören zu den fleißigsten Verfolgern neuer Versionen.
:::

#### 3. Dein erstes Projekt anlegen

Xcode öffnen → Create New Project → iOS wählen → die App-Vorlage, dann ausfüllen:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Feld</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Was eintragen</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Erläuterung</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Product Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstApp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">App-Name</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Deine Apple ID (kostenlos)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Für die Signatur, ein persönliches Konto genügt</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Organization Identifier</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bildet mit dem Product Name die Paketkennung</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interface</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Das Hauptframework dieses Buches</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Language</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">braucht keine Erklärung</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Die fünf Einträge beim Anlegen eines Projekts

Nach einem Klick auf Create erzeugt Xcode ein sofort lauffähiges Projekt. Wähle oben links einen Simulator (etwa iPhone 17) und drücke ▶ – Sekunden später erscheint auf dem Simulatorbildschirm ein Fenster mit „Hello, world!“. Deine erste iOS-App ist geboren.

#### 4. Die Projektstruktur aufgeschlüsselt: was jede Datei macht

Links ist der Projektnavigator; als Einsteiger brauchst du nur diese zu kennen:

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="290" viewBox="0 0 600 290" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="290" fill="#fafafa" rx="8"/>
      <text x="20" y="28" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ Projektstammverzeichnis</text>
      <rect x="30" y="42" width="540" height="225" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <rect x="45" y="56" width="250" height="196" fill="#eef2ff" rx="5"/>
      <text x="56" y="78" font-size="11" fill="#1e1b4b" font-weight="bold">MyFirstApp/ (Code-Ordner)</text>
      <text x="66" y="100" font-size="10" fill="#374151">├ MyFirstAppApp.swift  ← Einstiegspunkt</text>
      <text x="66" y="120" font-size="10" fill="#374151">├ ContentView.swift  ← Hauptansicht</text>
      <text x="66" y="140" font-size="10" fill="#374151">└ Assets.xcassets  ← Symbole, Bilder, Farben</text>
      <text x="56" y="166" font-size="10" fill="#6b7280">(neue Dateien kommen in diesen Ordner)</text>
      <text x="56" y="196" font-size="10" fill="#1e1b4b" font-weight="bold">Tab "Info" / Info.plist</text>
      <text x="66" y="216" font-size="10" fill="#6b7280">App-Deklaration: Name, Berechtigungen, Einstellungen</text>
      <rect x="310" y="56" width="245" height="196" fill="#f0fdf4" rx="5"/>
      <text x="321" y="78" font-size="11" fill="#065f46" font-weight="bold">weitere wichtige Orte</text>
      <text x="331" y="100" font-size="10" fill="#374151">📁 Preview Content/  ← Vorschau-Material</text>
      <text x="331" y="122" font-size="10" fill="#374151"><i class="fas fa-bullseye mr-1"></i> Target-Einstellungen (blaues Projekt-Symbol)</text>
      <text x="331" y="142" font-size="10" fill="#6b7280">——Version, Mindestsystem und Signatur stehen hier</text>
      <text x="331" y="168" font-size="10" fill="#374151"><i class="fas fa-flask mr-1"></i> MyFirstAppTests/  ← Unit-Tests</text>
      <text x="331" y="188" font-size="10" fill="#374151">📱 MyFirstAppUITests/ ← UI-Tests</text>
      <text x="331" y="216" font-size="10" fill="#9ca3af">(die Testvorlage ist bereits erzeugt, Kapitel 67)</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Abbildung 2: Die Xcode-Projektstruktur, die Einsteiger kennen müssen
:::

- MyFirstAppApp.swift: der Programmeinstieg; in SwiftUI sind es nur ein paar Zeilen – „starten, dann die Hauptoberfläche zeigen“;
- ContentView.swift: die Hauptansicht; alles, was du gerade siehst, liegt hier;
- Assets.xcassets: das Ressourcenlager – Icons, Bilder und Farben liegen hier;
- Target-Einstellungen: über das blaue Projektsymbol links hinein; Versionsnummer, minimale iOS-Version und Signatur stehen dort. Auch Anzeigename und Icon der App konfigurierst du hier.

#### 5. Xcode-Effizienztricks: die fünf „Tastenkürzel-Cheats“ für Einsteiger

Wenn du diese beherrschst, wirkst du „sehr professionell“:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Aktion</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tastenkürzel</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Wirkung</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ausführen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kompilieren und starten</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Canvas-Vorschau öffnen/umschalten</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Der Schalter für WYSIWYG</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Einrückung formatieren</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Die Einrückung des ausgewählten Codes automatisch ordnen</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Datei schnell öffnen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dateinamen tippen, sofort offen (am häufigsten gebraucht!)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kommentieren/Kommentar aufheben</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Beim Debuggen Code nebenbei ein- und ausschalten</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Die meistgenutzten Xcode-Tastenkürzel (das Einsteiger-Fünfer-Set)

Zwei weitere versteckte Boni: mehrere Simulatoren gleichzeitig (iPhone und iPad nebeneinander laufen lassen, um Layouts zu vergleichen) und die Snippet-Bibliothek (häufige Codezeilen ins Snippets-Panel rechts ziehen, beim nächsten Mal per Knopfdruck einfügen) – nutz diese Effizienzwerkzeuge einfach, das Gefühl kommt von selbst.

#### 6. Debugging auf dem echten Gerät: die App auf dein iPhone bringen

So gut der Simulator auch ist, das echte Gerät ist das Ziel. Auch mit einer kostenlosen Apple ID kannst du auf echten Geräten debuggen:

1. iPhone per Datenkabel anschließen (oder kabellos im selben WLAN debuggen);
2. In der Geräteliste oben in Xcode dein Handy wählen; beim ersten Mal wirst du zum Anmelden mit der Apple ID aufgefordert, die Signatur wird automatisch eingerichtet;
3. Auf dem iPhone [Einstellungen] → [Allgemein] → [VPN & Geräteverwaltung] → deinem Entwicklerzertifikat vertrauen;
4. ▶ drücken, und die App landet auf dem echten Gerät.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Achtung: die „Sieben-Tage-Grenze“ des kostenlosen Kontos

{class="mt-1"}
Eine App mit Signatur einer kostenlosen Apple ID erlischt nach 7 Tagen (ein erneutes Ausführen verlängert die Gültigkeit). Das ist Apples Missbrauchsschutz und reicht für die Lernphase völlig; ein bezahltes Entwicklerkonto (99 US-Dollar pro Jahr) hat diese Grenze nicht, mehr dazu in Kapitel 67.
:::

#### 7. Erste Proben + Erste Hilfe bei häufigen Fehlern

Öffne ContentView.swift, ersetze den Text in Text("Hello, world!") durch deinen Namen und drücke ⌘R – Sekunden später zeigt der Simulator deinen Namen. Glückwunsch: Du hast die erste vollständige Runde „Code ändern → kompilieren → installieren → ausführen“ absolviert.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Fehlerbild</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Häufige Ursache</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Gegenmittel</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Signing-Fehler</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kein Team gewählt, Zertifikat abgelaufen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">In Target → Signing dein Konto anhaken; beim kostenlosen Konto einmal neu ausführen</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Simulator bleibt schwarz/öffnet nicht</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Beschädigtes Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menü Device → Erase All Content; oder den Simulator löschen und neu anlegen</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode lädt langsam/installiert nicht</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Netzwerkschwankungen beim App Store</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Andere Tageszeit wählen; oder das .xip-Offline-Paket von der Apple-Entwicklerseite laden</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Erste-Hilfe-Tabelle für typische Einrichtungsfehler von Einsteigern

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Jetzt bist du dran: deine „Entwickler-Ritual“-Checkliste abschließen

{class="mt-1"}
① Xcode installieren und den Simulator zum Laufen bringen; ② die eigene App einmal auf dem echten Gerät starten und einen Screenshot als Erinnerung machen; ③ den Hello-Text durch deinen Namen ersetzen; ④ in den Target-Einstellungen den Anzeigenamen auf „Meine erste App“ ändern. Nach diesen vier Schritten bist du jemand mit einem eigenen Werk.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Zusammenfassung des Kapitels

- Harte Hürden: Mac + Xcode; ohne Mac zuerst mit Swift Playgrounds auf dem iPad die Sprache lernen
- Xcode aus dem App Store installieren; neue Versionen verlangen neue Systeme, Updates nicht aufschieben
- Die fünf Elemente beim neuen Projekt: Name, Team, Organisationskennung, SwiftUI, Swift
- Projekt-Merksatz: Der Code liegt im Ordner MyFirstApp/; die Target-Einstellungen regeln Version und Signatur
- Beim Debuggen auf echten Geräten mit kostenloser Apple ID gilt die 7-Tage-Signaturgrenze; ein bezahltes Konto hat sie nicht
- Der Entwickleralltag = Code ändern → ⌘R → Ergebnis ansehen, im ewigen Kreislauf
:::
