---
id: di-liu-shi-yi-zhang
num: 61
part: ios-kai-fa-pian
nav: Kapitel 61: Swift im Schnelldurchlauf – die erste Sprache der Apple-Entwicklung
toc: default
kind: chapter
---

### Kapitel 61: Swift im Schnelldurchlauf – die Hauptsprache der Apple-Entwicklung

{class="chapter-intro mb-4"}
In diesem Kapitel lernen wir die Sprache richtig. Keine Angst – Swift ist berühmt dafür, „einsteigerfreundlich“ zu sein, und du brauchst kein Grammatikbuch auswendig zu lernen: Mit 20 % der Syntax verstehst und schreibst du 80 % des Alltagscodes. Den Rest schlägst du nebenbei nach, während du Projekte baust. Merk dir unser Lernprinzip: Verstehen > Auswendiglernen, Anwenden können > Meisterschaft.

#### 1. Variablen und Typen: den Daten Namen geben

Ein Programm ist „Daten + Logik“. Eine Variable gibt den Daten einen Namen und speichert sie. Swift deklariert mit let und var:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Variablen</span><span class="dots">···</span>
:::

```
let name = "Max"        // let: Konstante (standardmäßig empfohlen)
var age = 18             // var: Variable (später änderbar)

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var ist änderbar
// name = "Lena"         // <i class="fas fa-times-circle mr-1"></i> let ist nicht änderbar: Kompilierfehler

let score: Int = 100     // der Typ lässt sich auch explizit angeben
let pi = 3.14            // ohne Angabe wird er automatisch abgeleitet

print("Hallo \(name)")   // String-Interpolation: Backslash + Klammern
```
:::

Die gängigen Typen in einer Tabelle:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Typ</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Was gespeichert wird</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Beispiel</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ganzzahl</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dezimalzahl</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">„Hallo“</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bool</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">wahr/falsch</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[Int] (Array)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Eine Sammlung von Werten</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[1, 2, 3]</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Swifts gängige Basistypen

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tipp: die let-zuerst-Regel

{class="mt-1"}
Das eiserne Gesetz der Swift-Community: standardmäßig let, und var nur, wenn es wirklich nötig ist. Wo let möglich wäre, warnt dich Xcode mit gelbem Text über das var. Diese Gewohnheit erspart dir eine ganze Klasse von Bugs durch „versehentlich geänderte Variablen“ – je weniger sich im Code verändert, desto leichter ist er zu durchdenken.
:::

#### 2. Optionals: Swifts „Amulett gegen Abstürze“

Das ist das wichtigste Konzept in Swift, punktum. In einem Satz: Kann ein Wert unter Umständen „nicht vorhanden“ sein, zwingt dich Swift, diesen Fall zu behandeln – damit ist der „Null-Pointer-Absturz“, dieser branchenweite Albtraum, schon auf Sprachebene ausgemerzt.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Optionals</span><span class="dots">···</span>
:::

```
var name: String = "Max"   // normaler Typ: darf nie nil sein
// name = nil                // <i class="fas fa-times-circle mr-1"></i> Kompilierfehler: stoppt dich sofort

var nickname: String? = nil  // mit Fragezeichen: nil erlaubt (Optional)
nickname = "Tommy"

// bei Optionals musst du sie "auspacken":
if let n = nickname {        // if let: sicheres Auspacken
    print("Hallo \(n)")
} else {
    print("Noch kein Spitzname")
}

let len = nickname?.count ?? 0   // ?? Standardwert (Nil-Coalescing-Operator)
print(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Achtung: ! ist eine Hochrisiko-Operation

{class="mt-1"}
Im Code nickname! zu schreiben (erzwungenes Entpacken) ist, als riefst du dem Compiler zu: „Ich versichere, dass es nicht nil ist“ – liegst du falsch, stürzt die App auf der Stelle ab. Für Einsteiger gilt: möglichst if let / ?? verwenden, nicht !. Wenn Xcode Code vervollständigt, fügt es gelegentlich eigenmächtig ein ! an – denk daran, das zu entfernen.
:::

#### 3. Funktionen und Closures: Logik in „Schaltflächen“ verpacken

Eine Funktion ist ein Stück Logik mit Namen, wie eine Taste auf der Fernbedienung. Eine Closure dagegen ist eine „Funktion ohne Namen“, die du jederzeit weiterreichen kannst:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Funktionen und Closures</span><span class="dots">···</span>
:::

```
// Funktion: Name vorne; Parameter und Rückgabetyp dahinter
func greet(name: String) -> String {
    return "Hallo, \(name)!"
}
print(greet(name: "Max"))     // beim Aufruf mit Parameternamen

// Closure: direkt vor Ort definiert, leicht und direkt
let numbers = [1, 2, 3, 4]
let doubled = numbers.map { $0 * 2 }   // $0 = das aktuelle Element
// [2, 4, 6, 8]

let big = numbers.filter { $0 > 2 }    // filtern
// [3, 4]
```
:::

In SwiftUI sind Closures überall: Die geschweiften Klammern hinter Button("Tippe mich") { ... } sind genau so eine Closure. Präge dir die Sammlungs-Kombos map, filter und sorted gut ein – künftig sind 90 % aller Listenverarbeitungen Kombinationen daraus.

#### 4. Structs und Protokolle: Swifts „Lego“-System

Swifts offizielle Präferenz ist eindeutig: Bevorzugt Structs verwenden; erst wenn Vererbung nötig ist, zu Classes greifen. Structs sind Werttypen – beim Kopieren lebt jedes sein eigenes Leben, was eine ganze Kategorie von Bugs von vornherein ausschließt:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Structs und Protokolle</span><span class="dots">···</span>
:::

```
// das Struct: die Daten-Box
struct Record {
    var id = UUID()
    var amount: Double
    var category: String
    var date: Date

    // das Struct bringt seinen "Memberwise Initializer" mit: direkt erstellbar
}
let r = Record(amount: 25.5, category: "Essen", date: Date())

// Protokoll: der Vertrag, "welche Fähigkeiten vorhanden sein müssen"
protocol Identifiable {
    var id: UUID { get }
}
struct Record: Identifiable { ... }   // das Protokoll übernehmen = zusagen, seine Anforderungen zu erfüllen
```
:::

In SwiftUI ist fast alles ein struct (View ist lediglich ein Protokoll). Wenn du das jetzt noch nicht ganz verstehst, ist das kein Problem – ab Kapitel 62 begegnet dir das täglich. In der Welt von Swift gilt: Umarme zuerst das struct.

#### 5. Syntax-Spickzettel für absolute Einsteiger

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Was du tun willst</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Schreibweise</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Konstante/Variable definieren</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">let x = 1</code> / <code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String-Interpolation</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Hallo, \(name)"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Funktion definieren</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">func name(parameter: Typ) -> Rückgabetyp { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Verzweigung</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if Bedingung { ... } else { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Durchlaufen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for x in array { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sicheres Entpacken</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if let x = optionalerWert { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Standardwert</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">x ?? Standardwert</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Struct definieren</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X { var a: Int; var b: String }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Closure</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">{ $0 * 2 }</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Swift-Syntax-Spickzettel (Einsteigerversion)

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Jetzt bist du dran: 15 Minuten lang Swift in Playgrounds ausprobieren

{class="mt-1"}
Hast du einen Mac, öffne Xcode → Playground; ohne Mac nutze Swift Playgrounds auf dem iPad oder den Web-Playground. Führe jeden Codeabschnitt dieses Kapitels einmal aus, ändere Zahlen und Texte ab und baue absichtlich ein paar Fehler ein, um zu sehen, wie Xcode sie meldet. Diese 15 Minuten nach dem Motto „erst spielen, dann lernen“ machen dir den Einstieg in Kapitel 62 gleich doppelt so leicht.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Kapitelfazit

- Erst let, var nur mit Bedacht; Typen werden automatisch abgeleitet, nach dem Doppelpunkt geht auch eine explizite Angabe
- Optionals sind Swifts Seele: Kann ein Wert leer sein, musst du ihn behandeln – if let / ?? sind dein Glücksbringer, ! ist eine Hochrisiko-Operation
- Funktionsaufrufe tragen Parameternamen; Closure = Funktion ohne Namen, in SwiftUI überall anzutreffen
- Bevorzuge structs und halte dich an Protokolle; in SwiftUI ist fast alles ein struct
- 20 % Syntax erledigen 80 % der Arbeit: erst anwenden, dann meistern
:::
