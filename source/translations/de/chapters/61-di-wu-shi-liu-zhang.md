---
id: di-wu-shi-liu-zhang
num: 56
part: an-zhuo-kai-fa-pian
nav: Kapitel 56: Feinschliff und Veröffentlichung – ab in den Google Play Store
toc: default
kind: chapter
---

### Kapitel 56: Feinschliff und Veröffentlichung – Testen, Debuggen und der Weg in den Google Play Store

{class="chapter-intro mb-4"}
Die App ist fertig – und nun? In diesem Kapitel geht es um die drei Schritte von „läuft irgendwie“ zu „auslieferungsfertig“: Wie debuggst du effizient, um Bugs zu finden? Wie schreibst du Tests, die Rückfälle verhindern? Und wie bekommst du die App in den Google Play Store, damit die ganze Welt sie herunterladen kann? Die Veröffentlichung ist nicht bloß ein Ritual – sie ist die Schwelle, an der aus einem Werk ein Produkt wird.

#### 1. Die drei Debug-Werkzeuge: Logcat, Haltepunkte, UI-Inspektor

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Werkzeug</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Wofür</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Wie du es einsetzt</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logcat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">System- und eigene Logmeldungen ansehen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Im Code Log.d("TAG","Wert=$x") schreiben und im Panel nach dem TAG filtern</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Haltepunkt-Debugging</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Das Programm an einer bestimmten Zeile anhalten und Variablenwerte ansehen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Neben der Zeilennummer klicken, bis der rote Punkt erscheint, im Debug-Modus starten und Schritt für Schritt durchgehen</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Layout Inspector</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Die Struktur der laufenden Oberfläche ansehen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menü Tools → Layout Inspector, um den Komponentenbaum in Echtzeit zu sehen</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Die drei Debug-Werkzeuge

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tipp: Wie liest man eine Fehlermeldung?

{class="mt-1"}
Nach einem Absturz zeigt Logcat einen roten Stacktrace. Suche von unten nach oben die erste Zeile, die mit deinem eigenen Paketnamen beginnt (z. B. com.example.yourapp) – diese Zeile ist fast immer der Tatort. Schau zuerst auf den Exception-Typ (NullPointer? Typumwandlung?), dann auf „at ... deineDatei:Zeilennummer“. Mit diesem Trick löst du 80 % aller Abstürze.
:::

#### 2. Testen: die Versicherung für deinen Code

Manuelles Testen ist unzuverlässig – du änderst die eine Funktion, und eine andere bricht unbemerkt. Tests sind „Bittermedizin im Nachhinein“ und „kugelsichere Weste“ zugleich. Android-Tests gibt es in drei Ebenen; als Einsteiger verinnerlichst du zuerst die erste:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ebene</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Was wird getestet</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Wo liegt es</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tempo</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Unit-Tests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Reine Logik (Berechnungen, Prüfungen)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/test/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sekunden</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Instrumentierungstests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Oberflächenverhalten auf einem echten Gerät</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/androidTest/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minuten</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Manuelle Tests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gefühl und Erlebnis von echten Menschen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Immer nötig</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Die drei Test-Ebenen

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Unit-Test-Beispiel</span><span class="dots">···</span>
:::

```
// die Logik "Betragstext in Zahl umwandeln" in eine reine Funktion auslagern
fun parseAmount(input: String): Double? {
    val v = input.trim().toDoubleOrNull()
    return if (v != null && v > 0) v else null
}

// teste sie (JUnit4)
@Test
fun emptyInputReturnsNull() {
    assertEquals(null, parseAmount(""))
}
@Test
fun negativeReturnsNull() {
    assertEquals(null, parseAmount("-5"))
}
@Test
fun normalValueParses() {
    assertEquals(12.5, parseAmount("12.5"))
}
```
:::

Die Betragsprüfung und die Statistikberechnungen im Haushaltsbuch sollten alle von Unit-Tests abgedeckt sein. Tests laufen lassen: Rechtsklick auf den Ordner test → Run. Wenn alles grün bleibt, kannst du den Code beruhigt anfassen.

#### 3. Signieren und Paketieren: deiner App den „Stempel“ geben

Android verlangt, dass jedes Installationspaket signiert ist – wie ein offizieller Siegel, der beweist: „Dieses Paket stammt von mir und wurde nicht verändert.“ Beim Debuggen signiert Android Studio automatisch mit dem Debug-Schlüssel; zum Veröffentlichen brauchst du deinen eigenen Release-Schlüssel. Der Ablauf:

1. Menü Build → Generate Signed Bundle / APK;
2. Eine Keystore-Datei (Schlüsselspeicher) anlegen – Passwort setzen und gut verwahren;
3. Release und das AAB-Format wählen – der Build ist fertig.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Warnung: Keystore verloren = App verloren

{class="mt-1"}
Jedes Update nach der Veröffentlichung muss mit derselben Signatur erfolgen, sonst lehnt der Store es ab. Sind Keystore-Datei und Passwort einmal verloren, bleibt dir nur, unter neuem Namen neu zu starten – alle bisherigen Nutzer kommen nicht mehr an die Updates. Sichere Keystore und Passwort unbedingt an einem sicheren Ort (verschlüsselte Cloud + Notizheft): Das ist eine der teuersten Lektionen im Android-Entwicklerleben.
:::

#### 4. Der komplette Weg in den Google Play Store

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Entwicklerkonto registrieren</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> Store-Material vorbereiten</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> AAB hochladen</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> Formular zur Datensicherheit ausfüllen</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Prüfung (Stunden bis Tage)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> Veröffentlichen</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Abbildung 6: Sechs Schritte bis in den Google Play Store
:::

- Registrieren: einmalige Registrierungsgebühr von 25 US-Dollar, du brauchst ein nutzbares Google-Konto;
- Materialien: App-Icon (512×512), Screenshots (mindestens 2), Funktionsbeschreibung, Link zur Datenschutzerklärung (Pflicht, sobald Daten erhoben werden);
- Formular zur Datensicherheit: ehrlich angeben, welche Daten erhoben werden – ein Haushaltsbuch ohne Internetzugriff darf „Null“ melden;
- Prüfung: Bei der ersten Veröffentlichung mit einem neuen Konto wird oft von Hand geprüft, das dauert von Stunden bis Tagen; bei einer Rückgabe einfach die Hinweise umsetzen.

Hinweis für Nutzer in China: Google Play braucht eine besondere Netzwerkumgebung, und die Verbreitung auf dem chinesischen Festland läuft meist über chinesische Stores (Huawei, Xiaomi, MyApp von Tencent usw.). Der Ablauf in chinesischen Stores ist ähnlich, aber jeder Store hat eigene Prüfgewohnheiten – dieselbe AAB/APK-Datei darf in mehreren Stores erscheinen. Für die Übung ist ein Store, der ganz durchläuft, schon ein Sieg.

#### 5. Store-Materialien gestalten: Der erste Eindruck ist die Downloadzahl

Die Store-Seite ist das Schaufenster, das Nutzer beim „Bummeln“ sehen. Drei Materialien entscheiden über den ersten Eindruck:

- Icon: 512×512, kein Notbehelf-Screenshot. Ohne Designgeschick lässt du dir von einem KI-Tool eine schlichte geometrische Form erzeugen – sie taugt nur, wenn man sie auf dem Handy-Startbildschirm verkleinert noch auf den ersten Blick erkennt;
- Screenshots: mindestens 2, besser 4–6, mit den zentralen Funktionsszenarien; zu jedem ein Satz in echter Alltagssprache („In einer Sekunde eine Ausgabe erfasst“ ist zehnmal besser als „Effiziente Buchhaltungslösung“);
- Beschreibung: Der erste Satz klärt „Was ist das + wofür ist es da“, statt Superlative wie „am professionellsten, am stärksten“ aufzutürmen – das Suchranking im Store hängt vor allem von Schlüsselwörtern und der Download-Quote ab, Ehrlichkeit wirkt besser als Übertreibung.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tipp: Ein A/B-Blick auf die Kollegen

{class="mt-1"}
Schlender vor der Veröffentlichung durch die Top 10 der ähnlichen Apps im Store und vergleiche Screenshots: Welchen Stil haben ihre Icons? Welches Verkaufsargument zeigen ihre Screenshots? Wie lauten ihre Titel? Nachahmen ist nicht kopieren – lerne das Muster und fülle es mit deinem eigenen Inhalt. Das ist die schnellste Lektion für den Kaltstart eines jeden Produkts.
:::

#### 6. Mini-Checkliste: Performance-Optimierung und Absturzmeldungen

Vor der Veröffentlichung lohnen sich für diese beiden Punkte je eine halbe Stunde:

##### 1. Vier Punkte der Performance-Selbstkontrolle

1. Listen mit LazyColumn: Lange Listen niemals mit Column hart anordnen – Lazy Loading ist die erste Lektion in Android-Performance;
2. Bilder nicht im Original einbauen: Mit der Bildbibliothek Coil automatisch skalieren und cachen – ein 5-MB-Originalbild bringt ein schwaches Gerät zum Wackeln;
3. Schwere Arbeit auf dem Main-Thread vermeiden: Datenbank, Netzwerk und große Dateien gehören in Coroutinen;
4. Mit dem Profiler nachmessen: Der eingebaute Performance-Profiler von Android Studio zeigt Arbeitsspeicher, CPU und Akkuverbrauch – erst messen, dann optimieren, nicht nach Gefühl.

##### 2. Absturzmeldungen

Dass es bei deinen Tests nicht abstürzt, beweist nicht, dass es auf Nutzerhandys stabil bleibt. Binde vor der Veröffentlichung Firebase Crashlytics ein (offiziell von Google, kostenlos): Ein paar Zeilen Konfiguration, und bei jedem Absturz wird automatisch der Stacktrace gemeldet – im Dashboard siehst du dann, „welches Modell, welche Version, welche Zeile“. Veröffentlichen ohne Absturzüberwachung ist wie Autofahren mit geschlossenen Augen.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Jetzt bist du dran: das Haushaltsbuch einmal „ausliefern“

{class="mt-1"}
① Ergänze 3 Unit-Tests für Logik wie parseAmount; ② fange mit Logcat einen selbst erzeugten Absturz ein und behebe ihn; ③ erzeuge ein release-signiertes APK und schicke es einem Freund zur Installation (das ist erst die „Werkszeremonie“); ④ wenn noch Zeit bleibt, registriere ein Entwicklerkonto und reiche das Haushaltsbuch wirklich zur Veröffentlichung ein. Die ersten drei Punkte schaffst du noch heute Abend.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Zusammenfassung des Kapitels

- Die drei Debug-Werkzeuge: Logcat für Logs, Haltepunkte für Variablen, Layout Inspector für die Oberfläche
- Abstürze lesen: im Stacktrace von unten die erste Zeile mit deinem Paketnamen suchen
- Drei Test-Ebenen: Unit (Sekunden, das zuerst lernen), Instrumentierung, manuell
- Veröffentlichen heißt signieren: Keystore und Passwort sichern – sonst „gehört“ die App plötzlich jemand anderem
- Sechs Schritte in den Store: Registrieren → Materialien → AAB hochladen → Datensicherheitsformular → Prüfung → Veröffentlichung
:::
