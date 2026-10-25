---
id: di-liu-shi-er-zhang
num: 62
part: ios-kai-fa-pian
nav: Kapitel 62: UI-Entwicklung – Einstieg in SwiftUI
toc: default
kind: chapter
---

### Kapitel 62: Oberflächenentwicklung – SwiftUI-Grundlagen

{class="chapter-intro mb-4"}
Die Oberfläche ist alles, was der Nutzer sieht. SwiftUI ist Apples 2019 vorgestelltes deklaratives UI-Framework – du beschreibst nur, wie die Oberfläche aussieht, und das System kümmert sich automatisch ums Rendern, den Dunkelmodus und alle möglichen Bildschirme. 2026 ist SwiftUI für neue Projekte längst der absolute Standard. In diesem Kapitel lernen wir „Zeichnen“.

#### 1. SwiftUIs Denkweise: deklarativ statt imperativ

Die klassische Oberflächenentwicklung ist imperativ: Du kommandierst Schritt für Schritt „Button erstellen → an Position (20,30) setzen → Farbe festlegen“. SwiftUI ist deklarativ: Du beschreibst direkt „Auf der Oberfläche gibt es einen roten Button mit der Aufschrift ‚Tippe mich'“ – wie gezeichnet und wann neu gezeichnet wird, darum kümmert sich das System selbst.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Erste SwiftUI-View</span><span class="dots">···</span>
:::

```
import SwiftUI

struct ContentView: View {
    var body: some View {      // body: beschreibt, "wie die Oberfläche aussieht"
        VStack {               // vertikal gestapelt
            Text("Hallo, Welt!")
                .font(.largeTitle)      // Modifier: große Überschrift
            Button("Klick mich") {
                print("Geklickt!")
            }
            .buttonStyle(.borderedProminent)  // ausgefüllter blauer Button
        }
        .padding()
    }
}
```
:::

Der Kern: Ein View ist ein struct, das das View-Protokoll erfüllt, die body-Eigenschaft beschreibt die Oberfläche, und mit .modifier()-Ketten verpasst du ihr den „Feinschliff“. Das ist bereits das gesamte Fundament von SwiftUI.

#### 2. Grundlegende Views: Text, Button, Textfeld, Bild

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">View</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Funktion</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Beispiel</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text anzeigen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text("Hallo")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button("Tippe mich") { Aktion }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Textfeld</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField("Hinweis", text: $eingabe)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bild anzeigen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Image(systemName: "star.fill")</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Die vier Grundviews von SwiftUI

Beachte Image(systemName:) – Apple liefert die SF-Symbols-Symbolbibliothek mit (mehrere tausend kostenlose Icons). Ein Name wie "star.fill" genügt, und schon erscheint ein ausgefüllter Stern. Das ist ein versteckter Bonus der iOS-Entwicklung: Beim Bau von Oberflächen musst du kaum noch nach Icon-Material suchen.

#### 3. Das Layout-Trio: VStack, HStack und ZStack

- VStack: untereinander (wie in der Essensschlange);
- HStack: nebeneinander (wie nebeneinander auf der Sitzbank);
- ZStack: übereinander gestapelt (wie ein Haufen Spielkarten – ideal für Badges und Overlays).

::: div .code-block
:::inline div .code-head
<span>SWIFT · Das Layout-Trio + gängige Modifier</span><span class="dots">···</span>
:::

```
VStack(alignment: .leading, spacing: 12) {
    HStack {
        Text("Rechnung")
        Spacer()                 // elastischer Abstand: schiebt das Rechte ans Ende
        Text("-25.5 Yuan").foregroundColor(.red)
    }
    Divider()                    // Trennlinie
    Text("Notiz: Mittagessen")
}
.padding(16)                     // Abstand an allen Seiten
.background(Color(.systemGray6)) // heller grauer Hintergrund
.cornerRadius(12)                // abgerundete Ecken

// die Reihenfolge der Modifier zählt: erst padding, dann background; der Hintergrund ohne Rand
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Achtung: Die Reihenfolge der Modifier ist entscheidend

{class="mt-1"}
padding(16).background(grau) und background(grau).padding(16) wirken unterschiedlich – Ersteres heißt „erst Abstand, dann Farbe“ (der Hintergrund umfasst den Abstand nicht), Letzteres „erst Farbe, dann Abstand“ (der Hintergrund umfasst den Abstand). Genau daher stammen die seltsamen weißen Ränder, die Einsteiger am häufigsten verwirren. Im Zweifel tausch die Reihenfolge – die Vorschau verrät dir sofort die Antwort.
:::

#### 4. State und Binding: die Oberfläche zum „Leben“ erwecken

Eine statische Oberfläche ist langweilig. SwiftUIs Regel: Die Oberfläche spiegelt jederzeit treu den Zustand wider – ändert sich der Zustand, zeichnet sie sich automatisch neu.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Zähler mit @State</span><span class="dots">···</span>
:::

```
struct CounterView: View {
    @State private var count = 0   // @State: ändert sich dieser Wert, muss neu gezeichnet werden

    var body: some View {
        VStack {
            Text("Du hast \(count) Mal geklickt")
            Button("Klick +1") {
                count += 1          // Zustand ändern, die Oberfläche aktualisiert sich automatisch
            }
        }
    }
}
```
:::

Textfelder brauchen eine „bidirektionale Bindung“ – das $-Zeichen übergibt Wert und Änderungsrecht zusammen:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Zweiwege-Bindung mit @Binding</span><span class="dots">···</span>
:::

```
struct InputView: View {
    @State private var text = ""

    var body: some View {
        TextField("Etwas eingeben", text: $text)  // Zweiwege-Bindung mit $
            .textFieldStyle(.roundedBorder)
        Text("Du hast eingegeben: \(text)")   // aktualisiert sich live während der Eingabe
    }
}
```
:::

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> Nutzeraktion</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> Zustand ändert sich (count += 1)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> SwiftUI bemerkt die Änderung</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> Zeichnet neu (body wird neu berechnet)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Abbildung 3: SwiftUIs unidirektionaler Datenfluss von „Zustand → Oberfläche“
:::

#### 5. Vorschau, Themes und Animationen: SwiftUIs „Geheimwaffen“

- Das #Preview-Makro: Ergänze am Dateiende #Preview { ContentView() }, und die Leinwand rechts rendert in Echtzeit – Code ändern, sofort sehen;
- Dunkelmodus gratis: Systemfarben verwenden (Color(.systemGray6), .primary) statt fest codierter Farben – dann passt sich der Dunkelmodus automatisch an, ohne eine einzige Zusatzzeile;
- Animation mit einer Zeile: withAnimation { count += 1 } oder .animation(.default, value: count) am View – Übergänge werden seidenweich.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Animationen in zehn Minuten</span><span class="dots">···</span>
:::

```
struct AnimatedHeartView: View {
    @State private var liked = false

    var body: some View {
        Button {
            withAnimation(.spring(duration: 0.4)) {
                liked.toggle()
            }
        } label: {
            Image(systemName: liked ? "heart.fill" : "heart")
                .font(.system(size: 48))
                .foregroundColor(liked ? .red : .gray)
                .scaleEffect(liked ? 1.3 : 1.0)
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tipp: erst die Funktion, dann die Animation

{class="mt-1"}
Der typische Anfängerfehler: über Animationen grübeln, obwohl die Oberfläche noch gar nicht stimmt. Bring erst die Funktion zum Laufen und lege die Effekte am Ende gebündelt auf – Animationen sind das i-Tüpfelchen, Funktionen sind die Rettung in der Not. Auch das folgt unserem Prinzip „Einfachheit zuerst“.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Jetzt bist du dran: Baue einen „Stimmungs-Button“

#### 6. Modifier-Spickzettel: eine Seite in der Hand, und die Oberfläche sitzt

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Was du erreichen willst</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Modifier</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Abstand</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.padding(16)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Eckenradius</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cornerRadius(12)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hintergrundfarbe</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.background(Color(.systemGray6))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Schrift und Schriftgröße</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.font(.title.bold())</code> / <code class="inline">.font(.system(size: 20))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Vordergrundfarbe (Text/Icons)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.foregroundColor(.red)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Volle Breite füllen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(maxWidth: .infinity)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Feste Größe</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(width:100, height: 44)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ausrichtung</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack(alignment: .leading)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Transparenz</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.opacity(0.6)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Schatten</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.shadow(radius: 5)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tipp-Geste</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.onTapGesture { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tastaturtyp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.keyboardType(.decimalPad)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
SwiftUI-Modifier-Spickzettel

Kein Problem, wenn du dir nichts merkst – diese Seite ist zum Nachschlagen da. Am häufigsten brauchst du ohnehin nur die ersten vier: padding, Eckenradius, Hintergrund, Schrift.

{class="mt-1"}
Verwandle das Vorlagenprojekt in einen Stimmungsschalter: ein Button, der beim Tippen im Kreis zwischen 😀 fröhlich → 😢 traurig → 😡 wütend wechselt, während Text und Hintergrundfarbe mitwechseln. Tipp: Speichere die drei Paare (Text + Farbe) in einem Array, den Index in @State und tippe dich mit (index + 1) % 3 weiter. Schick das Ergebnis hinterher an deine Freunde – und ernte die erste Welle von „Wow, du kannst Apps bauen!“.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Kapitelfazit

- SwiftUI ist deklarativ: Du beschreibst, wie etwas aussieht, das System zeichnet und zeichnet neu
- View = struct, das das View-Protokoll erfüllt; body beschreibt die Oberfläche; Modifier verpassen ihr den „Feinschliff“
- Die vier Grundviews: Text / Button / TextField / Image; die SF-Symbols-Bibliothek liefert gratis Icons ohne Ende
- Das Layout-Trio: VStack untereinander, HStack nebeneinander, ZStack übereinander; Spacer ist der flexible Zwischenraum
- @State erweckt die Oberfläche zum Leben; $ liefert die bidirektionale Bindung ans Textfeld
- #Preview zeigt sofort, was du tust; Systemfarben passen sich automatisch an den Dunkelmodus an; withAnimation setzt Effekte mit einer Zeile
:::
