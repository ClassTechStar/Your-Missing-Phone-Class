---
id: di-liu-shi-qi-zhang
num: 67
part: ios-kai-fa-pian
nav: Kapitel 67: Feinschliff und Veröffentlichung – ab in den App Store
toc: default
kind: chapter
---

### Kapitel 67: Feinschliff und Veröffentlichung – Testen, Debuggen und der Weg in den App Store

{class="chapter-intro mb-4"}
Die App ist fertig – und dann? Dieses Kapitel beantwortet die drei Dinge auf dem Weg von „läuft“ zu „auslieferbar“: wie du effizient debugst und Bugs findest, wie du Tests gegen Regressionen schreibst und wie du die App in den App Store bringst, damit sie die ganze Welt herunterladen kann. Der Store-Eintrag ist nicht nur Zeremonie – er ist die Wasserscheide zwischen Werk und Produkt.

#### 1. Die drei Debug-Werkzeuge: print, Haltepunkte, Vorschau

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Werkzeug</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Wofür</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Anwendung</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">print + Konsole</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Laufzeitprotokoll ansehen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Im Code print("Wert=\(x)") verwenden, die Ausgabe erscheint in der Konsole unten in Xcode</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Haltepunkt-Debugging</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Das Programm in einer Zeile anhalten und Variablenwerte ansehen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Neben der Zeilennummer klicken, es erscheint ein blauer Marker; beim Erreichen hält das Programm an, und du gehst Schritt für Schritt weiter</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI-Vorschau + Debugger</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Oberfläche und View-Hierarchie in Echtzeit ansehen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">#Preview-Leinwand + der View-Hierarchy-Inspektor zur Laufzeit</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Die drei Debug-Werkzeuge

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tipp: Wie liest man einen Absturz?

{class="mt-1"}
Stürzt Swift ab, gibt die Konsole "Fatal error" samt Ursache aus, und Xcode bleibt in der Fehlerzeile stehen und hebt sie hervor. Frühere Abstürze auf echten Geräten siehst du unter Xcode → Window → Organizer → Crashes (erfordert ein kostenpflichtiges Konto). Suchst du nach Schlagwörtern, beginne mit „erster Satz der Fehlerursache + swiftui“ – nur präzise Fragen liefern präzise Antworten.
:::

#### 2. Tests: für den Code eine Versicherung abschließen

Manuelles Testen ist unzuverlässig – du änderst das eine Feature, und ein anderes bricht still. Tests sind das „Rückgängig-Mittel“ und die „kugelsichere Weste“ zugleich. iOS nutzt das XCTest-Framework, in zwei Varianten:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ebene</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Was getestet wird</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Target</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Geschwindigkeit</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Unit-Tests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Reine Logik (Berechnungen, Prüfungen)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppTests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sekunden</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UI-Tests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Echtes Verhalten der Oberfläche</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppUITests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minuten</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Manuelle Tests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gefühl und Erfahrung eines echten Menschen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Immer nötig</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Die Test-Ebenen unter iOS (das Vorlagenprojekt bringt bereits zwei Test Targets mit)

::: div .code-block
:::inline div .code-head
<span>SWIFT · Unit-Test-Beispiel</span><span class="dots">···</span>
:::

```
import XCTest

// die Logik "Betragstext in Zahl umwandeln" in eine reine Funktion auslagern
func parseAmount(_ input: String) -> Double? {
    guard let v = Double(input.trimmingCharacters(in: .whitespaces)),
          v > 0 else { return nil }
    return v
}

final class AmountTests: XCTestCase {
    func testEmptyInputReturnsNil() {
        XCTAssertNil(parseAmount(""))
    }
    func testNegativeReturnsNil() {
        XCTAssertNil(parseAmount("-5"))
    }
    func testNormalValueParses() {
        XCTAssertEqual(parseAmount("12.5"), 12.5)
    }
}
```
:::

Tests laufen lassen: ⌘U. Wenn alles grün ist und du danach den Code änderst, bist du auf der sicheren Seite. Die Betragsprüfung und die Bilanzberechnung im Haushaltsbuch gehören jeweils unter Unit-Test-Schutz.

#### 3. Signieren und Packen: der App das „Siegel“ aufdrücken

Jede iOS-App muss signiert sein, sonst lässt sie sich nicht installieren – der Beweis, dass „dieses Paket von dir stammt und nicht verändert wurde“. Die Hierarchie:

- Lernphase: kostenlose Apple ID + automatisches Signieren durch Xcode (Personal Team); läuft auf echten Geräten, muss alle 7 Tage erneuert werden;
- Vertreibungsphase: erst ein kostenpflichtiges Entwicklerkonto (99 US-Dollar/Jahr) stellt Zertifikate und Provisioning Profiles aus – Voraussetzung für den Store-Eintrag und dauerhafte Installation.

Paket bauen: im Xcode-Menü Product → Archive (archivieren); ist der Build fertig, im Organizer Distribute App → App Store Connect wählen → hochladen. Zum Archivieren muss als Ziel Generic iOS Device eingestellt sein (nicht der Simulator) – ein Schritt, den Einsteiger gern vergessen.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Stolperfalle: Zertifikat verloren = Update-Lücke

{class="mt-1"}
Sind das Signaturzertifikat und der private Schlüssel einmal weg, kannst du die alte App nie wieder aktualisieren – Nutzer könnten nur die „komplett neue“ App installieren. Sichere Zertifikate ordentlich (aus dem Schlüsselbund als .p12 exportieren) und bewahre das Passwort gut auf. Zum Glück bietet Apple „automatisches Signieren“ und Cloud-Zertifikatsverwaltung (in Xcode Automatically manage signing anhaken) – das erspart die meisten manuellen Stolperfallen.
:::

#### 4. Der komplette Ablauf bis in den App Store

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Entwicklerkonto registrieren</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> Store-Material vorbereiten</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> Build hochladen</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> Datenschutz- und Prüfinfos ausfüllen</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Apple-Prüfung (1-7 Tage)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> Veröffentlichen</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Abbildung 5: Die sechs Schritte in den App Store
:::

- Registrieren: developer.apple.com, privates Konto 99 US-Dollar/Jahr;
- Materialien: Icon (1024×1024, ohne abgerundete Ecken – Apple rundet selbst), Screenshots (in den iPhone-Größen), Beschreibung, Link zur Datenschutzerklärung;
- Datenschutz-Fragebogen: ehrlich angeben, welche Daten erhoben werden – ein Haushaltsbuch ohne Netz darf „erhebt keinerlei Daten“ antworten;
- Prüfung: Beim ersten Einreichen sind 1–7 Tage Wartezeit üblich; bei Ablehnung die „Review-Anmerkungen“ Punkt für Punkt abarbeiten – Apples Ablehnungsgründe sind meist sehr konkret, einfach befolgen;
- TestFlight: Vor dem Store-Eintrag die Betaversion an Freunde verteilen (bis zu 10 000 Personen), eine Runde Feedback einsammeln und dann offiziell einreichen – höchst professionell.

#### 5. Die Store-Materialien: Der erste Eindruck bestimmt die Download-Zahlen

Die Store-Seite ist das Schaufenster, das Nutzer beim „Bummeln“ sehen. Drei Materialien bestimmen den ersten Eindruck:

- Icon: 1024×1024, kein Notbehelf aus Screenshots. Fehlt dir das Design-Können, erzeuge mit einem KI-Tool eine schlichte Grafik – sie taugt nur etwas, wenn sie auch klein auf dem Startbildschirm auf einen Blick erkennbar bleibt;
- Screenshots: mindestens 2 Sätze (in den gängigen iPhone-Größen), die die zentralen Funktionsszenarien zeigen; jede mit einer verständlichen Zeile Text („In einer Sekunde eine Buchung“ ist zehnmal besser als „Eine effiziente Buchhaltungs-Lösung“);
- Beschreibung: Der erste Satz klärt „Was ist das + für wen?“, kein Aufhäufen von „am professionellsten, am stärksten“ – Aufrichtigkeit wirkt mehr als Übertreibung.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Jetzt bist du dran: das Haushaltsbuch einmal „ausliefern“

#### 6. Mini-Checkliste: Absturzberichte und Performance-Optimierung

Vor dem Store-Eintrag lohnen sich diese zwei Punkte mit je einer halben Stunde:

##### 1. Absturzüberwachung

Dass es bei deinen Tests nicht abstürzt, heißt nicht, dass es auf dem Handy der Nutzer nicht abstürzt. Apple liefert im Xcode Organizer kostenlose Absturzberichte (Absturz-Logs von echten Geräten sehen kostenpflichtige Konten); bequemer ist es, ein Drittanbieter-SDK einzubinden (etwa Firebase Crashlytics). Ohne Absturzüberwachung in den Store zu gehen, ist wie mit geschlossenen Augen Autofahren.

##### 2. Vier Punkte für den Performance-Selbstcheck

1. Listen mit LazyVStack / List: Lange Listen nicht mit einem normalen VStack erzwingen – Lazy Loading ist die erste Lektion in Performance;
2. Bilder nicht im Original zustopfen: AsyncImage (für entfernte Bilder) und den System-Cache nutzen; ein 5-MB-Original reicht, um ältere Geräte lahmzulegen;
3. Schwerstarbeit nicht auf dem Haupt-Thread: Netzwerk und große Dateien laufen über async/await;
4. Mit Instruments nachmessen: der in Xcode eingebaute Performance-Profiler (Time Profiler, Speicherleck-Prüfung) – erst messen, dann optimieren, nicht nach Bauchgefühl.

{class="mt-1"}
1) Ergänze für parseAmount und andere Logik 3 Unit-Tests (mit ⌘U auf Grün laufen lassen); 2) fange mit einem Haltepunkt selbst einen von dir gebauten Absturz und behebe ihn; 3) baue mit Product → Archive ein Paket und lade über TestFlight Freunde zum Betatest ein; 4) wenn noch Kraft übrig ist, registriere ein Entwicklerkonto und reiche das Haushaltsbuch wirklich in den Store ein. Die ersten drei Schritte sind heute Abend machbar.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Kapitelfazit

- Die drei Debug-Werkzeuge: print-Log, Haltepunkte, SwiftUI-Vorschau und View-Inspektor
- XCTest: Unit-Tests (⌘U) + UI-Tests + manuelle Tests; im Vorlagenprojekt schon angelegt
- Signieren: kostenlose Konten automatisch (alle 7 Tage erneuern); Verteilen nur mit kostenpflichtigem Konto
- Paket: Generic iOS Device + Archive + Distribute; Zertifikate unbedingt sichern
- Sechs Schritte in den Store: Registrieren → Materialien → Hochladen → Datenschutz-Fragebogen → Prüfung → Einstellen; vorher TestFlight-Betatest
:::
