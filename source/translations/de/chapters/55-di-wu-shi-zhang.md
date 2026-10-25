---
id: di-wu-shi-zhang
num: 50
part: an-zhuo-kai-fa-pian
nav: Kapitel 50: Kotlin im Schnelldurchlauf – die erste Sprache der Android-Entwicklung
toc: default
kind: chapter
---

### Kapitel 50: Kotlin-Schnelleinstieg – die erste Sprache der Android-Entwicklung

{class="chapter-intro mb-4"}
In diesem Kapitel lernen wir richtig die Sprache. Keine Sorge – Kotlin ist berühmt dafür, einsteigerfreundlich zu sein, und du brauchst kein Grammatikbuch auswendig zu lernen: Mit 20 % der Syntax verstehst und schreibst du schon 80 % des Alltagscodes. Den Rest schlägst du nebenbei im Projekt nach. Unser Lernprinzip bleibt: Verstehen schlägt Auswendiglernen, Anwenden schlägt Meisterschaft.

#### 1. Variablen und Typen: Daten bekommen einen Namen

Ein Programm ist "Daten + Logik". Eine Variable gibt den Daten einen Namen und speichert sie. Kotlin kennt zwei Arten der Deklaration:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Variablen</span><span class="dots">···</span>
:::

```
val name = "Max"        // val: schreibgeschützte Variable (standardmäßig empfohlen)
var age = 18             // var: veränderliche Variable (später änderbar)

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var ist änderbar
// name = "Lena"         // <i class="fas fa-times-circle mr-1"></i> val ist nicht änderbar: Kompilierfehler

val score: Int = 100     // der Typ lässt sich auch explizit angeben
val pi = 3.14            // ohne Angabe wird er automatisch abgeleitet
```
:::

Die gebräuchlichen Typen lassen sich an einer Hand abzählen – eine Tabelle, und du hast sie:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Typ</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Was wird gespeichert?</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Beispiel</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ganze Zahl</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dezimalzahl</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Hallo"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Boolean</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">wahr/falsch</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List&lt; T&gt;</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Eine Sammlung von Daten</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">listOf(1, 2, 3)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Die gebräuchlichen Basistypen in Kotlin

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tipp: Der val-zuerst-Grundsatz

{class="mt-1"}
Eisernes Gesetz der Kotlin-Community: Standardmäßig val nehmen, var nur, wenn es wirklich nötig ist. Wo val möglich wäre und du var nutzt, mahnt dich die IDE mit gelber Schrift. Diese Gewohnheit erspart dir eine ganze Klasse von Bugs ("Variable wurde unerwartet verändert") – je weniger sich im Code ändert, desto leichter ist er zu durchschauen.
:::

#### 2. Funktionen: Logik zu "Knöpfen" verpacken

Eine Funktion ist ein Stück Logik mit Namen, wie eine Taste auf der Fernbedienung – einmal drücken (aufrufen), und eine Kette von Aktionen läuft ab. In Kotlin deklariert man sie mit fun:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Funktionen</span><span class="dots">···</span>
:::

```
fun greet(name: String): String {
    return "Hallo, $name!"     // das $-Symbol setzt die Variable in den String
}

println(greet("Max"))        // Ausgabe: Hallo Max!

// Einzeiler-Funktionen gehen auch als Ausdruck
fun add(a: Int, b: Int) = a + b

println(add(3, 5))            // Ausgabe: 8
```
:::

Ein paar Punkte: Parameter stehen in den Klammern (erst der Name, dann der Typ, getrennt durch Doppelpunkt); der Rückgabetyp steht hinter der Klammer; String-Templates mit $variablenname sind Kotlins Markenzeichen an Bequemlichkeit – kein mühsames Zusammenkleben von "Zeichenkette + Variable" wie in Java.

#### 3. Bedingungen und Schleifen: Das Programm lernt "denken"

Die Intelligenz eines Programms kommt von zwei Dingen: es kann entscheiden (if/when) und es kann wiederholen (for/while).

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Bedingungen und Schleifen</span><span class="dots">···</span>
:::

```
// Bedingung: if / else
val age = 17
if (age >= 18) {
    println("Erwachsener")
} else {
    println("Minderjährig")
}

// mehrere Zweige: when (hundertmal besser als switch)
val score = 85
val level = when {
    score >= 90 -> "Hervorragend"
    score >= 60 -> "Ausreichend"
    else -> "Weiter so!"
}

// Wiederholung: for-Schleife
val fruits = listOf("Apfel", "Banane", "Orange")
for (fruit in fruits) {
    println("Ich esse gern $fruit")
}
```
:::

when ist die gebräuchlichste Form für mehrere Verzweigungen in Kotlin – in der Android-Entwicklung benutzt du sie täglich (etwa um je nach Zustand unterschiedliche Oberflächen zu zeigen).

#### 4. Null-Sicherheit: Kotlins "Lebensretter"

Der berühmteste Bug aus dem Java-Zeitalter heißt NullPointerException – das Programm greift auf etwas zu, das "gar nicht da ist", und stürzt ab. Statistiken zufolge führt diese Ausnahme seit Jahren die Android-Absturz-Charts an. Kotlin löst das Problem auf Sprachebene: Null-Werte sind standardmäßig verboten.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Null-Sicherheit</span><span class="dots">···</span>
:::

```
var name: String = "Max"   // normaler Typ: darf nie null sein
// name = null                // <i class="fas fa-times-circle mr-1"></i> Kompilierfehler: stoppt dich sofort

var nickname: String? = null // mit Fragezeichen: null erlaubt
nickname = "Tommy"

// bei Nullable-Typen musst du sicher damit umgehen:
println(nickname?.length)    // Safe Call: bei null kommt null zurück, kein Absturz
val len = nickname?.length ?: 0   // Elvis-Operator: Standardwert bei null
println(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Achtung: ? und ?: nicht verwechseln

{class="mt-1"}
String? heißt "darf null sein", a ?: b heißt "wenn a null ist, nimm b" (die Zeichenkombination sieht aus wie Elvis' Frisur, daher der Name Elvis-Operator). Wenn der Compiler am Anfang über "null-Fehler" meckert, hast du höchstwahrscheinlich vergessen, einen nullable Typ zu behandeln – genau das ist die Sprache, die dich schützt.
:::

#### 5. Klassen und Objekte: Die Formen für "Bauteile"

Die Klasse ist die "Gussform" des Objekts, das Objekt das "Fertigprodukt" der Klasse. Alles in Android – Seiten, Buttons, Daten – sind Objekte. Kotlin hat ein Zauberwerkzeug, die data class (Datenklasse), die speziell zum "Verpacken von Daten" gedacht ist – eine Zeile ersetzt in Java Dutzende:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Klassen und Data Classes</span><span class="dots">···</span>
:::

```
// normale Klasse: die Form
class Dog(val name: String) {
    fun bark() = println("$name: wuff!")
}

val dog = Dog("Rex")      // Objekt erzeugen
dog.bark()                 // Rex: wuff!

// data class: die Daten-Box (mit equals/copy usw. ab Werk)
data class User(val id: Int, val name: String, val email: String)

val me = User(1, "Max", "zhangsan@example.com")
val twin = me.copy(name = "Fritz")   // kopiert und ändert ein Feld
```
:::

Wenn du später dein Haushaltsbuch baust, ist jede Buchung eine data class: data class Record(val amount: Double, val category: String, val date: String). Siehst du – du kannst bereits die Code-Struktur eines echten Projekts schreiben.

#### 6. Lambdas und Higher-Order-Funktionen: Kotlins "Syntax-Zucker"

In Android-Code begegnest du täglich Konstrukten wie { ... } – "Funktionen ohne Namen", genannt Lambdas (anonyme Funktionen). Button onClick = { count++ } ist ein solches Lambda: "Was nach dem Antippen passiert" wird als Päckchen verpackt und dem Button übergeben.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Erste Schritte mit Lambdas</span><span class="dots">···</span>
:::

```
// normaler Weg: eine benannte Funktion definieren und übergeben
fun double(x: Int) = x * 2
val result = listOf(1, 2, 3).map(::double)

// Lambda-Weg: direkt vor Ort definiert, leicht und direkt
val result2 = listOf(1, 2, 3).map { it * 2 }   // it = das aktuelle Element

// filtern + umwandeln hintereinander (in echten Projekten sehr häufig)
val bills = listOf(12.5, 88.0, 5.0, 200.0)
val bigBills = bills.filter { it > 50 }.sorted()
// [88.0, 200.0]——"Rechnungen über 50, sortiert"
```
:::

Merke dir ein paar häufige "Sammelkombos": filter (ausfiltern), map (umformen), sorted (sortieren), sum (aufsummieren). 90 % deiner künftigen Listenverarbeitung sind Kombinationen dieser vier Züge. Die Kotlin-Philosophie: Was sich in einem Satz sagen lässt, wird niemals in fünf geschrieben.

#### 7. Die Syntax-Spickkarte für Absoluteinsteiger

Versuche nicht, die ganze Syntax an einem Tag auswendig zu lernen. Speichere diese Karte und schlag beim Schreiben von Code nach – in zwei Wochen sitzt sie von allein:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Was willst du tun?</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Schreibweise</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Eine schreibgeschützte Variable definieren</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">val x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Eine veränderbare Variable definieren</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Eine Funktion definieren</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">fun name(parameter): rückgabetyp { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Entscheiden</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if (bedingung) {...} else {...}</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mehrere Verzweigungen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">when { bedingung -> ergebnis }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Durchlaufen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for (x in liste) { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Strings zusammenbauen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Hallo, $name"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mit null umgehen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">x?.length ?: 0</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Eine data class definieren</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">data class X(val a: Int, val b: String)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kotlin-Syntax-Spickkarte (Einsteigerversion)

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Selbst ausprobieren: Ohne Software-Installation erst mal 10 Minuten Kotlin spielen

{class="mt-1"}
Öffne im Browser play.kotlinlang.org (den offiziellen Kotlin-Online-Spielplatz), füge dort jeden Codeabschnitt aus diesem Kapitel ein und führe ihn aus; ändere Zahlen und Texte und beobachte, wie sich die Ausgabe verändert. Diese 10 Minuten "erst spielen, dann lernen" machen dir den Einstieg in Kapitel 51 doppelt so leicht.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Zusammenfassung des Kapitels

- val zuerst, var mit Bedacht; Typen werden automatisch hergeleitet, nach dem Doppelpunkt geht auch explizit
- Funktion = verpackte Logik; das String-Template $ ist das Markenzeichen
- if/when zum Entscheiden, for zum Wiederholen; when ist das "Multitalent" der Android-Entwicklung
- Null-Sicherheit ist Kotlins Lebensretter: normale Typen lehnen null ab, nullable Typen brauchen ? bzw. ?:
- Die data class ist die Schachtel für Daten – ein Feld pro Zeile, im echten Projekt täglich im Einsatz
- 20 % Syntax erledigen 80 % der Arbeit: erst anwenden, dann meistern
:::
