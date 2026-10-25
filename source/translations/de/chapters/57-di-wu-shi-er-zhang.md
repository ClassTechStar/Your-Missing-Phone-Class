---
id: di-wu-shi-er-zhang
num: 52
part: an-zhuo-kai-fa-pian
nav: Kapitel 52: Die vier Hauptkomponenten und der Activity-Lebenszyklus
toc: default
kind: chapter
---

### Kapitel 52: Die vier Grundkomponenten und der Activity-Lebenszyklus

{class="chapter-intro mb-4"}
Wenn Compose das "Gesicht" der App ist, dann ist dieses Kapitel das "Skelett". Android kennt vier Grundkomponenten, aus denen jede App zusammengesetzt ist; und die wichtigste davon, die Activity, hat eine "Lebenszyklus-Karte", die jeder Android-Entwickler ins Gehirn gebrannt haben muss. Nach diesem Kapitel verstehst du so alte Rätsel wie "Warum ist mein App-Zustand weg, wenn ich kurz in den Hintergrund wechsle und zurückkomme?"

#### 1. Die vier Grundkomponenten: Androids tragende Säulen

Android definiert offiziell vier Grundkomponenten, die jeweils eine Art von Arbeit übernehmen:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Komponente</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Aufgabe</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Zum Vergleich</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activity</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Eine sichtbare Oberfläche</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Die Schaufensterfront des Ladens – sichtbar und bedienbar</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Service</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Der "Unsichtbare", der im Hintergrund schuftet</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Der Lagerarbeiter – Musik abspielen, Dateien herunterladen, ganz ohne Oberfläche</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BroadcastReceiver</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">System-Broadcasts empfangen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Die Pförtnerloge – der Lautsprecher für "Akku ist leer" und "Netz ist weg"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ContentProvider</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Daten app-übergreifend teilen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Der öffentliche Aktenschrank – z. B. Kontakte für andere Apps freigeben</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Die vier Grundkomponenten von Android auf einen Blick

Als Einsteiger verbringst du 95 % deiner Zeit mit der Activity; Service und BroadcastReceiver brauchst du für Musikwiedergabe und Push-Nachrichten; ContentProvider nutzt du am seltensten (das System kapselt die gebräuchlichen Daten bereits). Und beachte: Alle vier Komponenten müssen sich im AndroidManifest.xml "anmelden" – ohne Registrierung findet das System sie nicht.

#### 2. Der Activity-Lebenszyklus: die erste "Schatzkarte" der Android-Entwicklung

Eine App auf dem Telefon kann jederzeit unterbrochen werden: Ein Anruf kommt, der Nutzer wechselt kurz zu WeChat, das System beendet dich wegen Speichermangels … Das Leben einer Activity ist eine Rundreise auf dieser Karte:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onCreate (Geburt: Initialisierung)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onStart (sichtbar)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onResume (im Vordergrund aktiv)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onPause (teilweise verdeckt)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onStop (ganz unsichtbar)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center">onDestroy (zerstört)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">🔁 onRestart / onStart / onResume: beim Zurückkehren in den Vordergrund umgekehrt</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Abbildung 4: Der Activity-Lebenszyklus (vorwärts: obere Reihe Geburt → untere Reihe Abschied; auf dem Rückweg genau umgekehrt)
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Callback</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Wann wird er ausgelöst?</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Typischer Einsatz</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onCreate</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Beim Erzeugen der Activity (einmal)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Oberfläche laden, Daten initialisieren</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStart</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Die Oberfläche wird sichtbar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ein wenig leichtgewichtige Logik starten</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onResume</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hat den Fokus, ist bedienbar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Animationen starten, Wiedergabe fortsetzen</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onPause</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Teilweise verdeckt oder im Begriff, verlassen zu werden</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Animationen pausieren, Entwurf speichern</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStop</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Vollständig unsichtbar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Schwere Ressourcen freigeben, Downloads pausieren</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onDestroy</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Unmittelbar vor dem Entfernen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Die letzten Aufräumarbeiten</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Typische Einsätze der sechs Lifecycle-Callbacks

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Stolperfalle: Eine Drehung des Bildschirms "tötet" die Activity

{class="mt-1"}
Der klassischste Stolperstein: Man dreht den Bildschirm, und der ganze Text im Eingabefeld ist weg. Grund: Eine Bildschirmdrehung zerstört die Activity standardmäßig und baut sie neu auf (durchlaufen von onDestroy → onCreate). Lösung: Den Zustand mit rememberSaveable sichern (in Compose der Ersatz für remember) – es holt die Werte beim Neuaufbau automatisch zurück. In den Kapiteln 6 und 7 wirst du es immer wieder brauchen.
:::

#### 3. Intent: das "Ticket" für den Verkehr in der App und nach außen

Der Intent (die "Absicht") ist das "Fahrticket" für die Kommunikation zwischen Komponenten. Ob du von einer Seite zur anderen springen, den Browser öffnen oder die Kamera aufrufen willst – immer musst du "ein Ticket lösen und einsteigen":

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Navigation mit Intent</span><span class="dots">···</span>
:::

```
// Variante 1: expliziter Intent – klar angegeben, zu welcher Seite
val intent = Intent(this, DetailActivity::class.java)
intent.putExtra("name", "Max")     // nimmt "Gepäck" mit (die Daten)
startActivity(intent)

// Variante 2: impliziter Intent – du sagst nur, was zu tun ist; das System sucht, wer es tut
val web = Intent(Intent.ACTION_VIEW, Uri.parse("https://developer.android.com"))
startActivity(web)   // das System öffnet den Browser (oder lässt dich wählen)
```
:::

Beide Varianten haben ihren Zweck: Explizit für Seitensprünge innerhalb der eigenen App; implizit, um Fähigkeiten des Systems oder anderer Apps zu nutzen (Webseite öffnen, anrufen, teilen). In Compose-Projekten holst du in einer Composable mit LocalContext.current den Context und kannst dann startActivity aufrufen.

#### 4. Mehrere Seiten und Navigation

Echte Apps haben mehrere Seiten. Die offiziell empfohlene Navigationslösung für Compose ist Navigation Compose (Bibliothek androidx.navigation):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Navigation-Compose-Grundgerüst</span><span class="dots">···</span>
:::

```
val navController = rememberNavController()

NavHost(navController, startDestination = "home") {
    composable("home") { HomeScreen(navController) }
    composable("detail/{name}") { entry ->
        val name = entry.arguments?.getString("name")
        DetailScreen(name ?: "Unbekannt")
    }
}

// um innerhalb der Ansicht zu navigieren:
navController.navigate("detail/Max")     // mit Parameter
navController.popBackStack()              // zurück zur vorherigen Seite
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tipp: Und wenn es zu viele Seiten werden?

{class="mt-1"}
Sobald das Projekt wächst, schreib alle Seitenrouten gebündelt in eine Datei (z. B. AppNavGraph.kt) und verwalte sie zentral – lass die Logik "Wohin springe ich?" nicht auf alle Seiten verstreuen. Das ist der erste Schritt von "läuft irgendwie" zu "wartbar".
:::

#### 5. Nebenbei erklärt: Was ist ein Fragment (und warum lehrt dieses Buch es nicht)

In alten Tutorials wirst du unweigerlich auf Fragment stoßen – einen "wiederverwendbaren Oberflächen-Schnipsel" innerhalb einer Activity, in der alten Mehrseiten-Architektur der absolute Star. Im Compose-Zeitalter reichen aber Composable-Funktionen + Navigation-Routen für Seiten, und auch offiziell ist Fragment zurückgestuft worden. Deshalb taucht es in diesem Buch nicht im Hauptweg auf.

Mein Rat: In neuen Projekten Fragment nicht aktiv einsetzen; aber wenn du alten Code liest oder im Vorstellungsgespräch danach gefragt wirst, reicht zu wissen: "Ein Fragment ist ein Oberflächen-Schnipsel, das in einer Activity steckt." Lernmaterialien immer bevorzugt ab 2023 wählen – die "alten Kalenderblätter" des Android-Stacks veralten schneller, als man denkt.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Selbst ausprobieren: Dem Zähler ein "Gedächtnis" verpassen

{class="mt-1"}
Bau den Zähler aus Kapitel 51 um: ① Ersetze remember durch rememberSaveable und prüfe nach einer Bildschirmdrehung, ob die Zahl überlebt hat; ② füge einen "Über"-Button hinzu, der mit Navigation auf eine zweite Seite springt und dort die Versionsnummer zeigt; ③ lass in onCreate bzw. onPause beider Seiten Logausgaben schreiben (Log.d) und beobachte in Logcat die Reihenfolge der Lifecycle-Aufrufe. Nach diesen drei Schritten ist der Lebenszyklus keine Theorie mehr.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Zusammenfassung des Kapitels

- Die vier Grundkomponenten: Activity (Schaufenster), Service (Hintergrund), BroadcastReceiver (Lautsprecher), ContentProvider (Aktenschrank)
- Sechs Lifecycle-Callbacks: onCreate → onStart → onResume → onPause → onStop → onDestroy
- Eine Bildschirmdrehung zerstört die Activity und baut sie neu: Mit rememberSaveable den Zustand retten
- Intent ist das "Ticket": explizit zur eigenen Seite, implizit für System-Fähigkeiten
- Mehrere Seiten mit Navigation Compose: NavHost + composable-Routen
:::
