---
id: di-si-shi-jiu-zhang
num: 49
part: an-zhuo-kai-fa-pian
nav: Kapitel 49: Entwicklungsumgebung einrichten – Android Studio und das erste Projekt
toc: default
kind: chapter
---

### Kapitel 49: Die Entwicklungsumgebung einrichten – Android Studio und das erste Projekt

{class="chapter-intro mb-4"}
Werkzeug muss sitzen, bevor die Arbeit beginnt. In diesem Kapitel bauen wir die "Küche" auf: Android Studio installieren, den Emulator zum Laufen bringen, das erste Android-Projekt deines Lebens anlegen und die Projektstruktur auseinandernehmen, bis alles klar ist. Wenn die Umgebung steht, siehst du zum ersten Mal, wie dein eigener Code zu einem tippbaren Button wird – diesen Moment merken sich viele ein Leben lang.

#### 1. Android Studio installieren

Android Studio ist die offizielle integrierte Entwicklungsumgebung (IDE) von Google – kostenlos und als Komplettpaket: Code schreiben, Vorschau der Oberfläche ansehen, debuggen, Pakete bauen, alles darin. Die Installation hat vier Schritte:

1. Öffne die offizielle Website developer.android.com/studio und lade die neueste stabile Version herunter (im August 2026 die Version nach Narwhal; für Windows/Mac/Linux verfügbar);
2. Starte das Installationspaket und klicke dich mit "Weiter" durch – der Assistent bringt Android SDK und Emulator-Komponenten automatisch mit;
3. Beim ersten Start lädst du nach Aufforderung die SDK-Komponenten herunter (die Standardauswahl passt; das kann ein paar Minuten und einige GB Speicher brauchen);
4. Danach siehst du die Willkommensseite – Glückwunsch, die "Küche" steht.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Achtung: Die Hardware-Anforderungen im Blick behalten

{class="mt-1"}
Android Studio ist ein echter "Speicherfresser": plane mindestens 16 GB RAM ein (8 GB gehen auch, aber der Emulator ruckelt dann schnell), reserviere über 20 GB Speicherplatz und sorge für eine CPU mit Virtualisierung (VT-x/AMD-V im BIOS aktivieren). Wenn dein Rechner wirklich alt ist, nutze statt des Emulators das Debuggen auf dem echten Gerät (Abschnitt 4 dieses Kapitels) – das läuft oft sogar flüssiger.
:::

#### 2. Dein erstes Projekt anlegen

Klicke auf der Willkommensseite auf New Project, wähle die Vorlage Empty Activity (die sauberste Einsteiger-Vorlage) und fülle drei Dinge aus:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Einstellung</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Was eintragen?</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Erklärung</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">My First App</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Der Name der App, erscheint auf dem Startbildschirm des Telefons</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Package name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example.myfirstapp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Weltweit eindeutige Kennung, üblich ist der umgedrehte Domainname – nimm zunächst den Standard</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minimum SDK</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API 26(Android 8.0)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mindestens unterstützte Version, deckt über 95 % der Geräte ab</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Die drei Angaben beim Anlegen eines Projekts

Nach einem Klick auf Finish lädt Android Studio per Gradle automatisch die Abhängigkeiten und baut das Projekt (beim ersten Mal dauert es ein paar Minuten, danach geht es jedes Mal viel schneller). Wenn der Build fertig ist, hast du eine lauffähige App – auch wenn sie vorerst nur "Hello Android!" anzeigt.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tipp: Was es mit dem Paketnamen auf sich hat

{class="mt-1"}
Der Paketname (package name) ist wie der "Personalausweis" der App – weltweit einmalig und nach der Veröffentlichung nicht mehr änderbar. Für private Übungen reicht com.example.xxx; für ein echtes Produkt nimm den umgedrehten eigenen Domainnamen (z. B. com.deinname.appname). Veröffentliche nichts unter com.example – der Store lehnt das ab.
:::

#### 3. Ans Laufen bringen: Emulator und echtes Gerät

Der Code ist geschrieben – jetzt braucht er ein "Telefon" zum Laufen. Du hast zwei Möglichkeiten:

##### 1. Der Emulator

Der Emulator virtualisiert ein Android-Telefon im Computer. Öffne in Android Studio den Device Manager → Create Device, wähle ein Gerät (empfohlen: die Pixel-Serie) → wähle ein Systemabbild (mit Google APIs) → lade es herunter → starte. Dann klickst du auf das grüne Dreieck Run in der Symbolleiste, und nach ein paar Sekunden erscheint deine App auf dem Bildschirm des "Telefons".

##### 2. Debuggen auf dem echten Gerät (noch empfehlenswerter)

Ein echtes Gerät ist und bleibt die realistischste Testumgebung – Wischgefühl, echtes Netz, echte Sensoren: Der Emulator kommt da nicht mit. Das Debuggen auf einem Android-Gerät ist ganz einfach:

1. Öffne auf dem Telefon [Einstellungen] → [Über das Telefon] und tippe 7-mal hintereinander auf "Buildnummer", um die "Entwickleroptionen" freizuschalten;
2. Aktiviere in den [Entwickleroptionen] USB-Debugging;
3. Verbinde das Telefon per Datenkabel mit dem Computer und tippe im Pop-up des Telefons "USB-Debugging erlauben" an;
4. Zurück in Android Studio erscheint dein Telefon in der Geräte-Dropdownliste der Symbolleiste – klicke auf Run.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Stolperfalle: USB-Debugging nicht dauerhaft aktiviert lassen

{class="mt-1"}
USB-Debugging ist wie eine "Hintertür" für den Computer. Wenn du in der Öffentlichkeit lädst oder dich mit nicht vertrauenswürdigen Rechnern verbindest, schalte USB-Debugging unbedingt aus, damit niemand über diese Tür deine Daten auslesen kann. Mach es nach der Entwicklung immer wieder aus – das wird zur Gewohnheit.
:::

#### 4. Die Projektstruktur zerlegt: wofür jede Datei gut ist

Beim ersten Öffnen des Projekts kann dich der Dateibaum links schwindelig machen. Keine Panik – im Alltag verbringst du 90 % deiner Zeit nur mit den folgenden paar Dateien:

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="300" viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="300" fill="#fafafa" rx="8"/>
      <text x="20" y="30" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ Projektstammverzeichnis</text>
      <rect x="30" y="45" width="540" height="230" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <text x="45" y="70" font-size="11" fill="#4f46e5" font-weight="bold">app/ ← hier schreibst du deinen Code</text>
      <rect x="60" y="82" width="240" height="178" fill="#eef2ff" rx="5"/>
      <text x="70" y="102" font-size="10" fill="#1e1b4b" font-weight="bold">src/main/</text>
      <text x="80" y="120" font-size="10" fill="#374151">├ java/…/MainActivity.kt  ← die Logik</text>
      <text x="80" y="138" font-size="10" fill="#374151">├ res/  ← Ressourcen (Bilder, Texte, Farben)</text>
      <text x="80" y="156" font-size="10" fill="#374151">└ AndroidManifest.xml  ← der "Personalausweis" der App</text>
      <text x="70" y="180" font-size="10" fill="#1e1b4b" font-weight="bold">build.gradle.kts</text>
      <text x="80" y="198" font-size="10" fill="#6b7280">deklariert die Abhängigkeiten (SDK-Version, Compose usw.)</text>
      <text x="70" y="222" font-size="10" fill="#1e1b4b" font-weight="bold">src/androidTest/ und test/</text>
      <text x="80" y="240" font-size="10" fill="#6b7280">Code für automatisierte Tests (Kapitel 56)</text>
      <rect x="320" y="82" width="230" height="178" fill="#f0fdf4" rx="5"/>
      <text x="330" y="102" font-size="10" fill="#065f46" font-weight="bold">sonstige Dateien im Stammverzeichnis</text>
      <text x="340" y="122" font-size="10" fill="#374151">gradle/ + gradlew.bat  ← Build-Skripte</text>
      <text x="340" y="142" font-size="10" fill="#374151">settings.gradle.kts  ← Projekteinstellungen</text>
      <text x="340" y="162" font-size="10" fill="#6b7280">(Faustregel für Anfänger: nur den Ordner app/ anfassen,</text>
      <text x="340" y="180" font-size="10" fill="#6b7280">den Rest erstmal als "Blackbox" behandeln, nicht anfassen)</text>
      <text x="340" y="208" font-size="10" fill="#9ca3af">.gitignore  ← Ignorierliste der Versionsverwaltung</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Abbildung 2: Die Projektstruktur, die Einsteiger kennen müssen (Merkregel: nur den Ordner app/ anfassen)
:::

- MainActivity.kt: das "Eingangstor" der App. Tippt der Nutzer auf das Symbol, wird es als erstes geweckt. In der heutigen Vorlage zeigt es "Hello Android!" an.
- AndroidManifest.xml: das "Melderegister" der App – hier steht, wie die App heißt, welches Symbol sie hat, welche Seiten es gibt und welche Berechtigungen sie braucht (Kamera, Standort usw.).
- res/-Ordner: das Ressourcenlager – hier liegen Bilder, Symbole, Texte, Farben. Texte in Ressourcendateien statt fest im Code zu hinterlegen, ist gute Android-Praxis (Sprach- und Themenwechsel werden so zum Kinderspiel).
- build.gradle.kts: das Baurezept – legt die unterstützte Mindestversion fest und welche Bibliotheken eingebunden sind (z. B. Compose).

#### 5. Erste Gehversuche: "Hello" durch deinen Namen ersetzen

Öffne MainActivity.kt und schau dir den von der Compose-Vorlage erzeugten Code an. Finde die Zeile Text("Hello Android!") und ersetze den Text in den Anführungszeichen durch deinen Namen, z. B. Text("Hallo, Max Mustermann! Das ist meine erste App"), und drücke Strg+R (auf dem Mac Cmd+R), um neu zu starten. Ein paar Sekunden später zeigt der Emulator deinen Namen.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · MainActivity.kt (diese Zeile ändern)</span><span class="dots">···</span>
:::

```
setContent {
    MyFirstAppTheme {
        Surface(modifier = Modifier.fillMaxSize()) {
            // ▼ hier deinen eigenen Text einsetzen
            Text("Hallo Max! Das ist meine erste App")
        }
    }
}
```
:::

Glückwunsch – du hast soeben einen vollständigen Zyklus "Code ändern → kompilieren → installieren → ausführen" hinter dich gebracht. Dieser Zyklus ist der Entwickleralltag der kommenden Tage. Mach gleich weiter: Ändere noch etwas anderes – vergrößere die Schrift, wechsle die Farbe. Im nächsten Kapitel lernst du, woher diese "Magie" kommt.

#### 6. Erste Hilfe bei häufigen Fehlermeldungen: die "Notaufnahme" für die ersten zwei Wochen

Beim Aufsetzen der Umgebung und beim ersten Build wirst du mit hoher Wahrscheinlichkeit auf die folgenden drei Fehler stoßen. Keine Panik – für alle gibt es ein Gegenmittel:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Fehlerbild</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Häufige Ursache</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Gegenmittel</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle sync failed / Abhängigkeiten laden langsam</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Der Zugriff auf die Repositorien über das Netz hakt</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Für Gradle einen schnellen Maven-Spiegel einrichten (z. B. Alibaba Cloud oder Tencent Cloud) – suche online nach "gradle china mirror" und richte es nach der Anleitung ein</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SDK-Komponenten fehlen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Der SDK-Download wurde bei der Installation übersprungen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Unter Settings → SDK Manager die fehlenden Plattformen und Tools nachinstallieren</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Emulator startet nicht / schwarzer Bildschirm</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Virtualisierung nicht aktiviert, Abbild beschädigt</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Im BIOS VT-x/AMD-V einschalten; den Emulator löschen und neu anlegen; oder gleich das echte Gerät zum Debuggen nehmen</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Erste-Hilfe-Tabelle für Umgebungsfehler bei Einsteigern

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tipp: Wie man Fehlermeldungen richtig sucht

{class="mt-1"}
Die erste Zeile einer Fehlermeldung ist am wertvollsten – kopiere sie wortwörtlich in die Suchmaschine und ergänze das Stichwort "android studio". Suche nicht nach vagen Fragen wie "Ich bringe meine Umgebung nicht zum Laufen", sondern nach konkreten Fehlern wie "Gradle sync failed: Could not resolve com.android.tools.build". Präzise Fragen bringen präzise Antworten.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Selbst ausprobieren: Deine "Entwickler-Ritual"-Liste abhaken

{class="mt-1"}
① Android Studio installieren und den Emulator zum Laufen bringen; ② die eigene App einmal auf dem echten Gerät laufen lassen und einen Screenshot als Erinnerung machen; ③ den Hello-Text in deinen Namen ändern; ④ das Projekt zippen und archivieren. Nach diesen vier Schritten darfst du verkünden: Ich bin jetzt auch Android-Entwickler (Screenshot als Beweis).
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Zusammenfassung des Kapitels

- Android Studio = offizielle, kostenlose IDE; empfohlen: 16 GB RAM + 20 GB Speicher + aktivierte Virtualisierung
- Drei Grundzutaten für ein neues Projekt: Name, Paketname (weltweit eindeutig, com.example nicht veröffentlichen), minimale SDK-Version (ab API 26)
- Zwei Wege zum Ausführen: Emulator (virtuelles Telefon im Rechner) und echtes Gerät (USB-Debugging einschalten – danach wieder ausschalten)
- Projekt-Merkregel: nur den Ordner app/ anfassen – MainActivity.kt ist das Eingangstor, das Manifest das Melderegister, res/ das Ressourcenlager
- Entwickleralltag = Code ändern → Run → Ergebnis ansehen, im Kreis immer wieder
:::
