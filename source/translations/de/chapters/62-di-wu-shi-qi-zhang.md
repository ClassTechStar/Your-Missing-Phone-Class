---
id: di-wu-shi-qi-zhang
num: 57
part: an-zhuo-kai-fa-pian
nav: Kapitel 57: Der Weg nach vorn – Berechtigungen, Benachrichtigungen und moderne Architektur
toc: default
kind: chapter
---

### Kapitel 57: Der Weg nach vorn – Berechtigungen, Benachrichtigungen und moderne Architektur

{class="chapter-intro mb-4"}
Eine App bauen zu können ist erst der Anfang. In diesem Kapitel geht es um die Hürden auf dem Weg von „kann es bauen“ zu „baut es gut“: Wie beantragst du Berechtigungen mit Anstand? Wie verschickst du Benachrichtigungen, ohne zu nerven? Wie hebst du die Architektur eine Stufe höher – und wie schreibst du 2026 mit der KI als Partner Android-Code? All das begegnet dir in echten Projekten sofort.

#### 1. Laufzeitberechtigungen: erst anklopfen, dann eintreten

Kamera, Standort, Kontakte, Benachrichtigungen ... Diese „sensiblen Zonen“ muss die App zur Laufzeit beim Nutzer anfragen (seit Android 6). Die Regel: erst im Manifest deklarieren, dann im Code anfragen, und bei Ablehnung elegant abfedern. In Compose geht das am bequemsten mit rememberPermissionState aus der offiziellen Bibliothek Accompanist:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Laufzeit-Berechtigungen (Compose-Version)</span><span class="dots">···</span>
:::

```
// zuerst im Manifest deklarieren:
// &lt;uses-permission android:name="android.permission.CAMERA" /&gt;

@Composable
fun CameraButton() {
    val permission = rememberPermissionState(
        permission = android.Manifest.permission.CAMERA
    )
    Button(onClick = {
        when {
            permission.status.isGranted -&gt; openCamera()
            permission.status.shouldShowRationale -&gt; showExplainDialog()
            else -&gt; permission.launchPermissionRequest()
        }
    }) { Text("Foto aufnehmen") }
}
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Achtung: Was tun nach einer dauerhaften Ablehnung?

{class="mt-1"}
Wenn der Nutzer „Nicht mehr fragen“ angehakt hat, öffnet launchPermissionRequest kein Dialogfenster mehr. Dann leite den Nutzer zu den Systemeinstellungen (per Intent zur App-Einstellungsseite springen) und erkläre in der Oberfläche, „wofür diese Berechtigung gebraucht wird“. Mit freundlichem Ton steigt die Bereitschaft, die Berechtigung zu erteilen, deutlich – der Text einer Berechtigungsanfrage lohnt echtes Bemühen.
:::

#### 2. Benachrichtigungen: zur richtigen Zeit etwas Nützliches sagen

Benachrichtigungen sind der Kanal, über den eine App Nutzer erreicht – und zugleich die Funktion, die Nutzer am ehesten „blockieren“. Drei Disziplinen: nur Nützliches senden, das Ausschalten ermöglichen und nachts nicht stören. Die Grundanwendung:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Eine Benachrichtigung senden</span><span class="dots">···</span>
:::

```
// ab Android 13 muss zuerst die Berechtigung POST_NOTIFICATIONS angefragt werden (siehe voriger Abschnitt)

// 1. Benachrichtigungskanal anlegen (ab Android 8 Pflicht)
val channel = NotificationChannel(
    "reminder", "Erinnerungen", NotificationManager.IMPORTANCE_DEFAULT
)
val manager = getSystemService(NotificationManager::class.java)
manager.createNotificationChannel(channel)

// 2. Benachrichtigung senden
val notification = NotificationCompat.Builder(this, "reminder")
    .setSmallIcon(R.drawable.ic_notification)
    .setContentTitle("Ausgaben-Erinnerung")
    .setContentText("Heute hast du noch nichts erfasst")
    .setPriority(NotificationCompat.PRIORITY_DEFAULT)
    .build()
if (ActivityCompat.checkSelfPermission(this,
        Manifest.permission.POST_NOTIFICATIONS) == PackageManager.PERMISSION_GRANTED
) {
    manager.notify(1, notification)
}
```
:::

Für geplante Aufgaben (etwa „jeden Tag um 20:00 ans Buchen erinnern“) nimm WorkManager – der offiziell empfohlene „Hintergrund-Planer“ sorgt dafür, dass Aufgaben zum passenden Zeitpunkt laufen, ohne dass du dich um Akkuoptimierung kümmern musst. Für alles Weckerartige ist er die sichere Wahl.

#### 3. Architektur für Fortgeschrittene: Dependency Injection und Modularisierung

Sobald das Projekt wächst, melden sich zwei „süße Sorgen“:

- Chaos beim Objekterzeugen: Jede Seite erstellt selbst Datenbank und API – mit Hilt (Framework für Dependency Injection) wird das zentral verwaltet: „Wer etwas braucht, braucht nur zu fragen, und es wird gereicht“;
- Der Code wird zum Berg: Einkomponentige Projekte werden mit jeder Änderung langsamer – teile sie in mehrere Module auf (app / core / feature-xxx), dann entwickelt und testet jedes Feature unabhängig.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tipp: Kein Over-Engineering

{class="mt-1"}
Hilt und Modularisierung sind gute Werkzeuge, aber greif bei Ein-Personen-Projekten nicht vorschnell dazu. Für das Haushaltsbuch reichen ein einzelnes Modul plus manuell erzeugte Abhängigkeiten völlig. Erst wenn der Code über zigtausend Zeilen wächst, das Kompilieren langsamer wird oder mehrere Leute zusammenarbeiten, führst du sie bei Bedarf ein. Werkzeuge dienen dem Ziel, sie sind kein Selbstzweck – auch das ist das Prinzip „Einfachheit zuerst“ aus unserem KI-Programmierbuch.
:::

#### 4. Die neuen Spielregeln 2026: Android-Entwicklung mit KI-Unterstützung

2026 ist KI tief in den Android-Entwicklungsprozess eingebettet. Wenn du schneller werden willst, ist diese Schlagkombination längst erprobt:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Station</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Wie die KI hilft</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Deine Aufgabe</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Code schreiben</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gemini ist in Android Studio integriert; KI-Plugins von Drittanbietern vervollständigen und erzeugen Code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Anforderungen klar beschreiben, Ergebnisse prüfen</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Recherchieren</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Offizielle Dokumentation und Fehlermeldungen der KI zur Auslegung geben</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wichtige Schlüsse in der offiziellen Dokumentation nachprüfen</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tests schreiben</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Die KI Testfälle nach „normal/Grenzwert/Fehlerfall“ erzeugen lassen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prüfen, dass die Testfälle zur Fachlogik passen</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bugs beheben</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stacktrace + betroffenen Code einfügen, die KI ortet und repariert</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Die Änderungen verstehen und mit Tests verifizieren</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Vier Szenarien der Android-Entwicklung mit KI-Unterstützung

Die konkrete Methodik – wie du der KI Anweisungen gibst, wie du Ergebnisse abnimmst, wie du Fallen meidest – steht komplett in 11 Kapiteln in Teil 7 dieses Buches, „KI-Programmierung in der Praxis“ (Kapitel 37–47). Lese es unbedingt parallel: Die Android-Syntax liefert dieser Teil, das Handwerk der KI-Zusammenarbeit Teil 7.

#### 5. Compose-Performance und Debug-Werkzeuge

Mit Compose zu schreiben macht Spaß, aber „zu viele Recompositions“ können es zäh machen. Drei praktische Tricks:

- Parameter stabilisieren: Datenklassen mit @Immutable versehen oder derivedStateOf verwenden, damit irrelevante Zustandsänderungen keine großflächige Recomposition auslösen;
- Denk an den key: items(list, key = { it.id }) sorgt dafür, dass beim Einfügen und Löschen nur der betroffene Eintrag angefasst wird – ohne key kann ein einziges Löschen die ganze Liste neu zeichnen;
- Der Compose-Modus des Layout Inspectors: Er zeigt in Echtzeit, wie oft jedes Composable rekompiniert wurde – auf einen Blick erkennst du die Häufigen und optimierst gezielt an den Hotspots.

Schalte zusätzlich den Compose-Compiler-Bericht (Metrics) ein; er erzeugt eine Übersicht, „welche Komponenten instabil“ sind – auf dem Weg nach vorn sind Daten immer verlässlicher als Gefühl.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Jetzt bist du dran: das „Dreier-Set“ fürs Haushaltsbuch

{class="mt-1"}
① Baue die Erinnerung „jeden Tag um 20:00 ans Buchen denken“ ein (WorkManager + Benachrichtigungskanal + Android-13-Benachrichtigungsberechtigung); ② stelle die Erzeugung von Datenbank und API auf Hilt-Injektion um; ③ versuche, mit KI-Werkzeugen die Funktion „Monatsfilter“ schneller zu bauen, und nimm das Ergebnis nach der Drei-Ebenen-Abnahme ab. Ist das Dreier-Set fertig, sieht dein Projekt aus wie von der „regulären Truppe“.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Zusammenfassung des Kapitels

- Sensible Berechtigungen: im Manifest deklarieren + zur Laufzeit anfragen + bei Ablehnung elegant weiterhelfen
- Drei Disziplinen für Benachrichtigungen: nur Nützliches, abschaltbar, nicht störend; Kanal + Berechtigung, beides unverzichtbar
- Geplante Aufgaben mit WorkManager, keine eigenen Räder erfinden
- Hilt verwaltet Objekte, Modularisierung verwaltet Code – bei kleinen Ein-Personen-Projekten nicht vorschnell einsetzen
- Vier KI-Szenarien: Code schreiben, recherchieren, Tests schreiben, Bugs beheben; die Methodik in Teil 7 (Kapitel 37–47)
:::
