---
id: di-wu-shi-yi-zhang
num: 51
part: an-zhuo-kai-fa-pian
nav: Kapitel 51: UI-Entwicklung – Einstieg in Jetpack Compose
toc: default
kind: chapter
---

### Kapitel 51: Oberflächenentwicklung – Einstieg in Jetpack Compose

{class="chapter-intro mb-4"}
Die Oberfläche ist alles, was der Nutzer sieht. Vor Compose schrieb man Android-Oberflächen in XML – mühsam wie ein Lückentext. 2021 brachte Google Jetpack Compose heraus: Die Oberfläche wird direkt in Kotlin-Code "gemalt", nach dem Prinzip "was du siehst, ist was du bekommst", und nach jeder geänderten Zeile aktualisiert sich die Vorschau sofort. 2026 ist Compose der absolute Mainstream für neue Projekte. In diesem Kapitel lernen wir "malen".

#### 1. Der Compose-Gedanke: Die Oberfläche ist eine Funktion

Die Kernidee von Compose in einem Satz: Oberfläche = Funktion. Alles, was auf dem Bildschirm erscheinen kann (Text, Button, Bild), ist eine "Composable-Funktion", markiert mit @Composable. Verschachtelt man sie wie Bausteine, entsteht die Oberfläche.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Erste Compose-Oberfläche</span><span class="dots">···</span>
:::

```
@Composable
fun Greeting(name: String) {
    Text(text = "Hallo, $name!")     // ein "Text-Baustein"
}

// verschachtelte Komposition: große Blöcke umschließen kleine
@Composable
fun HomeScreen() {
    Column {                          // vertikal gestapelt
        Greeting(name = "Max")
        Greeting(name = "Lena")
        Button(onClick = { /* was beim Klick passieren soll */ }) {
            Text("Klick mich")
        }
    }
}
```
:::

Achte auf diesen "Hut" @Composable – er sagt dem Compiler: "Das hier ist ein Oberflächen-Baustein." Bausteine lassen sich unbegrenzt verschachteln – das ist das ganze Geheimnis von Compose.

#### 2. Grundbausteine: Text, Button, Eingabefeld, Bild

Die Compose-Komponenten sind "Bausteine" – die vier häufigsten:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Komponente</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Wofür gut?</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Pflichtparameter</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text anzeigen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">text (der anzuzeigende Text)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onClick (Callback beim Antippen)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Eingabefeld</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">value, onValueChange (Callback bei Eingabeänderung)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bild anzeigen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">painter (Bildressource)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Die vier Grundbausteine von Compose

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Beispiel: Basiskomponenten</span><span class="dots">···</span>
:::

```
@Composable
fun BasicWidgets() {
    Column {
        Text(text = "Das ist ein Text")
        Button(onClick = { println("Geklickt!") }) {
            Text("Schaltfläche")
        }
        var input by remember { mutableStateOf("") }
        TextField(
            value = input,
            onValueChange = { input = it },
            label = { Text("Etwas eingeben") }
        )
    }
}
```
:::

In den zwei Zeilen des Eingabefelds taucht remember { mutableStateOf("") } auf – das ist Composes "Zustands"-Magie, die wir in Abschnitt 5 dieses Kapitels genau anschauen. Fürs Erste reicht es, das Gesicht schon mal kennengelernt zu haben.

#### 3. Das Layout-Trio: Column, Row, Box

Die Bausteine sind da – aber wie anordnen? Merk dir drei "Schachteln":

- Column: untereinander (wie in der Essensschlange);
- Row: nebeneinander (wie nebeneinander sitzen);
- Box: übereinander (wie ein Stapel Spielkarten – gut für Badges und Overlays).

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Das Layout-Trio</span><span class="dots">···</span>
:::

```
Column {
    Text("Erste Zeile")
    Row {
        Text("Links")
        Text("Rechts")
    }
    Box {
        Text("Unterste Ebene")
        Text("überlagerndes Badge oben")
    }
}
```
:::

Soll das Layout hübscher werden? Gib den Komponenten einen Modifier – er schminkt die Bausteine wie mit Make-up:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Modifier: gängige Kniffe</span><span class="dots">···</span>
:::

```
Text(
    text = "Schöner Text",
    modifier = Modifier
        .padding(16.dp)          // Abstand an allen Seiten
        .fillMaxWidth()          // füllt die ganze Breite
        .background(Color.Blue)  // Hintergrundfarbe
        .clickable { /* Klick */ }// klickbar
)
// verkettete Aufrufe: eins nach dem anderen; die Reihenfolge zählt (erst padding, dann Hintergrund; der Hintergrund ohne Rand)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Achtung: Die Reihenfolge des Modifiers ist entscheidend

{class="mt-1"}
padding(16.dp).background(Blue) und background(Blue).padding(16.dp) wirken unterschiedlich – erstere heißt "erst Abstand, dann Farbe" (der Hintergrund enthält den Abstand nicht), letztere "erst Farbe, dann Abstand" (der Hintergrund schließt den Abstand ein). An genau dieser Stelle malen sich Einsteiger am häufigsten diese "komischen weißen Ränder". Im Zweifel: vertausche die Reihenfolge, die Vorschau sagt dir sofort die Antwort.
:::

#### 4. Zustand: Die Oberfläche zum "Leben" erwecken

Eine statische Oberfläche ist langweilig. Damit nach einem Tipp auf den Button die Zahl +1 nimmt und man ins Eingabefeld tippen kann, brauchst du einen Zustand (State). Die Compose-Regel: Die Oberfläche spiegelt treu den Zustand wider; ändert sich der Zustand, zeichnet sie sich automatisch neu.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Zustand: Klick-Zähler</span><span class="dots">···</span>
:::

```
@Composable
fun Counter() {
    // remember + mutableStateOf: merkt sich diesen veränderlichen Wert
    var count by remember { mutableStateOf(0) }

    Column {
        Text(text = "Du hast $count Mal geklickt")
        Button(onClick = { count++ }) {   // ändert den Zustand
            Text("Klick +1")                // die Oberfläche aktualisiert sich automatisch
        }
    }
}
```
:::

Drei Zeilen Code – ein lebendiger Zähler. Das ist der Vorteil von Compose gegenüber der alten Schreibweise: kein manuelles "Oberfläche aktualisieren" mehr, du änderst nur die Daten. Merk dir zwei Schlüsselfunktionen: remember (der Wert wird bei der Neuzusammensetzung der Oberfläche nicht geleert) und mutableStateOf (sagt Compose: "Dieser Wert hat sich geändert – neu zeichnen").

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> Nutzer klickt</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> Zustand ändert sich (count++)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> Compose bemerkt die Änderung</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> Zeichnet die Oberfläche neu (Recomposition)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Abbildung 3: Composes unidirektionaler Datenfluss "Zustand → Oberfläche"
:::

#### 5. Theme und Dunkelmodus: einmal konfigurieren, überall wirksam

Das MyFirstAppTheme { ... } im Vorlagenprojekt ist das Theme. Es basiert auf dem Material-3-Designsystem und verwaltet Farben, Schriften und Formen zentral. Den Dunkelmodus zu unterstützen braucht nur drei Schritte:

1. Im Theme ein helles/dunkles Farbschema definieren (die Vorlage erzeugt das ColorScheme automatisch);
2. Wechselt das System in den Dunkelmodus, erkennt das isSystemInDarkTheme() automatisch;
3. Die vom Theme bereitgestellten Farben verwenden (z. B. MaterialTheme.colorScheme.primary) statt fest kodierte Farbwerte.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tipp: Material 3 und dynamische Farben

{class="mt-1"}
Ab Android 12 holt sich "Material You" die Farben der App aus deinem Hintergrundbild. Die Compose-Vorlage unterstützt das standardmäßig (dynamicColor). Deine App "zieht sich auf jedem Nutzergerät automatisch um" – das ist die Romantik des modernen Android.
:::

#### 6. Vorschau, Animation und Live Edit: Composes "Cheats"

Drei "Cheats" für das Entwicklungserlebnis – wer sie benutzt hat, will sie nicht mehr missen:

- @Preview-Vorschau: Versieh eine Composable mit der Annotation @Preview, und Android Studio rendert die Oberfläche sofort rechts – Code ändern mit Sofortwirkung, ohne jedes Mal auf das Telefon zu installieren;
- Live Edit: Das Android Studio von 2026 kann Teile der Änderungen "heiß" auf Emulator/echtem Gerät aktualisieren – kleine Anpassungen wie eine Textfarbe erscheinen sekundenschnell auf dem Gerät;
- Animations-APIs: Mit animateFloatAsState und AnimatedVisibility lassen sich mit ein paar Zeilen sanfte Übergänge bauen – der "Hochwertigkeits-Effekt" steckt oft genau in diesen paar Zeilen.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Animationen in zehn Minuten</span><span class="dots">···</span>
:::

```
@Composable
fun AnimatedBox() {
    var big by remember { mutableStateOf(false) }
    // bei Wertänderung sanfter Übergang zum Zielwert
    val size by animateDpAsState(if (big) 120.dp else 60.dp)

    Box(Modifier
        .size(size)
        .background(MaterialTheme.colorScheme.primary)
        .clickable { big = !big }
    )
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tipp: Erst Funktion, dann Animation

{class="mt-1"}
Der klassische Einsteigerfehler: "Die Oberfläche stimmt noch nicht einmal, und schon wird an der Animation gefeilt." Bringe zuerst die Funktion zum Laufen und lege die Animationen gesammelt ans Ende – auch das ist das Prinzip "Einfachheit zuerst": Animation ist das i-Tüpfelchen, Funktion ist das Brot.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Selbst ausprobieren: Einen "Stimmungs-Button" bauen

{class="mt-1"}
Baue das Vorlagenprojekt in einen Stimmungsschalter um: ein Button, der bei jedem Tipp zwischen 😀fröhlich → 😢traurig → 😡wütend wechselt; Text und Hintergrundfarbe wechseln mit. Tipp: Wähle Text und Farbe mit when je nach Zustand. Schick das Ergebnis an Freunde und ernte die erste Welle an "Wow, du kannst Apps bauen!".
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Zusammenfassung des Kapitels

- Compose-Gedanke: Oberfläche = @Composable-Funktionen, verschachtelt wie Bausteine
- Die vier Grundkomponenten: Text / Button / TextField / Image
- Das Layout-Trio: Column untereinander, Row nebeneinander, Box gestapelt
- Modifier in Kette zum "Schminken": padding, fillMaxWidth, background, clickable – die Reihenfolge hat Bedeutung
- Der Zustand ist die Seele: remember + mutableStateOf – Daten ändern, Oberfläche zeichnet neu
- Theme mit Material 3 + dynamischen Farben; Dunkelmodus einmal konfigurieren, überall wirksam
:::
