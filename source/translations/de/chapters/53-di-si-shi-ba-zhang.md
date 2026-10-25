---
id: di-si-shi-ba-zhang
num: 48
part: an-zhuo-kai-fa-pian
nav: Kapitel 48: Android kennenlernen – vom Betriebssystem zum Entwickler-Ökosystem
toc: default
kind: chapter
---

### Kapitel 48: Android kennenlernen – Vom Betriebssystem zum Entwickler-Ökosystem

{class="chapter-intro mb-4"}
Glückwunsch zu dieser Entscheidung – vom „Handynutzer“ zum „App-Entwickler“. Bevor es losgeht, breiten wir erst einmal die Karte aus: Woher kommt Android? Warum schreiben Entwickler auf der ganzen Welt Apps dafür? Und was passiert eigentlich alles, von deinem Tastenanschlag bis zur App auf dem Handy des Nutzers?

#### 1. Androids Lebensgeschichte: Vom „kleinen Roboter“ zum größten System der Welt

Die Geschichte von Android beginnt 2003: Der Ingenieur Andy Rubin gründet die Firma Android Inc. mit einem bescheidenen Ziel – ein intelligentes Betriebssystem bauen, das „Kameras besser versteht“. 2005 kauft Google die Firma, 2007 gründet Google gemeinsam mit Dutzenden Herstellern die Open Handset Alliance (OHA), und im September 2008 kommt mit dem HTC Dream (G1) das erste Android-Handy auf den Markt.

Den Rest der Geschichte kennst du: Bis 2026 ist Android das mobile Betriebssystem mit dem weltweit größten Marktanteil, mit Milliarden aktiver Geräte. Dein Handy, deine TV-Box, dein Autodisplay, deine Smartwatch – sehr wahrscheinlich läuft überall Android. Was heißt das? Jede deiner Codezeilen hat die Chance, von den meisten Menschen der Welt genutzt zu werden.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tipp: Androids Open-Source-DNA

{class="mt-1"}
Der Kerncode von Android (AOSP, Android Open Source Project) ist Open Source – jeder Hersteller darf ihn verändern und anpassen. Deshalb hat Xiaomi MIUI (heute HyperOS), Huawei eine HarmonyOS-Kompatibilitätsschicht und Samsung One UI. Für Entwickler ist das von Vorteil: Du lernst „Android-Entwicklung“, nicht „Entwicklung für eine bestimmte Marke“ – eine Fähigkeit, die überall läuft.
:::

Auch die Versionsnummern haben eine interessante Entwicklung hinter sich: Ab 1.5 (Cupcake) trug jede große Version den Namen eines Desserts – Donut, Eclair, Frozen Yogurt, Gingerbread … bis Android 10 im Jahr 2019 auf reine Zahlen umstieg. Im August 2026 ist Android 17 die neueste offizielle Version; die „Mindest-Unterstützungsversion“, die dir bei der Entwicklung wirklich wichtig ist, liegt bei Mainstream-Apps meist zwischen Android 8 (API 26) und Android 10 (API 29) – je weiter du ältere Geräte mitabdeckst, desto größer ist dein Nutzerkreis.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Version</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Codename/Jahr</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Wichtig für Entwickler</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 8 (API 26)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Oreo · 2017</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Benachrichtigungskanäle, Hintergrund-Beschränkungen – für viele ältere Geräte die Untergrenze</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 10 (API 29)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2019</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Scoped Storage kommt, die Regeln für Dateizugriffe werden grundlegend neu geordnet</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 12 (API 31)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2021</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Material You mit dynamischen Farben, ein großes Upgrade fürs Interface</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 13 (API 33)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2022</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Benachrichtigungsberechtigung zur Laufzeit – der Dialog fragt, ob die App Notifications senden darf</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 14-15 (API 34-35)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2023-2024</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Predictive Back, 16-KB-Pages, Datenschutz wird weiter verschärft</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 16-17 (API 36-37)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2025-2026</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Schnellerer Rhythmus der Punktversionen, Integration von KI-Fähigkeiten (z. B. Gemini-Erweiterungen)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kurze Geschichte der Android-Versionen (Stand: August 2026, mit den wichtigsten Punkten für Entwickler)

#### 2. In welcher Sprache schreiben: Java oder Kotlin?

In der Geschichte der Android-Entwicklung gab es zwei dominante Sprachen. Java ist der „Gründungsveteran“ – Android startete mit ihm; Kotlin wurde 2017 von Google zum „Bürger erster Klasse“ gekürt, seit 2019 gilt offiziell „Kotlin-first“, und bis 2026 laufen praktisch alle neuen Projekte mit Kotlin, während alte Projekte meist nach und nach migrieren.

Ganz ehrlich: Wenn du völlig ohne Vorkenntnisse startest, lern direkt Kotlin und fass Java nicht mehr an. Drei Gründe: Erstens braucht Kotlin 30–40 % weniger Code als Java (dieselbe Funktion ist in Kotlin kürzer und klarer); zweitens schützt es von Haus aus vor „NullPointer“-Fehlern, dem Albtraum aller Anfänger; drittens setzen alle modernen Tutorials, die offizielle Dokumentation und die KI-Programmier-Tools (erinnerst du dich an unser KI-Programmierbuch?) auf Kotlin. Java begegnet dir nur bei der Pflege alter Projekte und beim Lesen alten Codes.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Java-Stil (ausführliche Variante)

{class="font-mono text-xs leading-relaxed"}
public class MainActivity extends Activity {<br>&nbsp;&nbsp;@Override<br>&nbsp;&nbsp;protected void onCreate(Bundle b) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b);<br>&nbsp;&nbsp;&nbsp;&nbsp; setContentView(R.layout.activity);<br>&nbsp;&nbsp;}<br>}
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Kotlin-Stil (schlanke Variante)

{class="font-mono text-xs leading-relaxed"}
class MainActivity : ComponentActivity() {<br>&nbsp;&nbsp;override fun onCreate(b: Bundle?) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b)<br>&nbsp;&nbsp;&nbsp;&nbsp;setContent { App() }<br>&nbsp;&nbsp;}<br>}
:::
:::

Für dieselbe Aufgabe spart Kotlin eine Menge geschweifter Klammern und Boilerplate. In Kapitel 50 lernen wir es richtig kennen; für jetzt reicht: Die „Lingua franca“ der Android-Entwicklung heißt Kotlin.

#### 3. Wie entsteht eine App?

Viele glauben, „App entwickeln“ heißt: Computer aufklappen und Code stürmen. In Wirklichkeit durchläuft eine App von der Idee bis zum Handy des Nutzers ungefähr diese Pipeline:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-lightbulb mr-1"></i> Idee</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center">📐 Design (Oberfläche + Funktionen)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-keyboard mr-1"></i> Code schreiben</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hammer mr-1"></i> Kompilieren und packen (APK/AAB)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Testen (Emulator + echtes Gerät)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-rocket mr-1"></i> Veröffentlichen (Store/Installer)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Abbildung 1: Der komplette Weg einer Android-App von der Idee bis zum Store
:::

Zwei Begriffe auf diesem Weg musst du jetzt schon kennen:

- APK: Das Installationspaket-Format einer Android-App (.apk), per Doppelklick aufs Handy installierbar – das .exe von Windows für Android. Für eigene Tests oder zum Teilen mit Freunden nimmst du es.
- AAB: Android App Bundle (.aab), das „Premium-Paketformat“ für die Veröffentlichung im Google Play Store. Der Store schneidet es dynamisch je nach Handymodell des Nutzers zu, sodass jeder ein kleineres Paket lädt. Selbst installieren kannst du es nicht – es gehört in den Store.

Außerdem wirst du ständig einen Begriff hören: SDK (Software Development Kit). Es ist das von Android offiziell bereitgestellte „Entwickler-Werkzeugset“ – die API-Bibliotheken aller Versionen, Debug-Werkzeuge, Emulator-Images und mehr. Klassen wie Activity oder Button, die du beim Programmieren benutzt, kommen alle aus dem SDK.

#### 4. Der Android-Tech-Stack im Überblick: Deine „Waffenliste“

Bevor es richtig losgeht, schau dir die Standardkonfiguration eines typischen Android-Projekts 2026 an – es ist kein Problem, wenn du diese Liste jetzt noch nicht verstehst; nach dem ganzen Buch wirst du sie auf einen Blick erfassen:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ebene</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Häufigste Wahl (2026)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Wofür</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sprache</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin 2.x</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Die Sprache für die Programmlogik</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Oberfläche</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jetpack Compose + Material 3</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Oberflächen im Code zeichnen (die Hauptroute dieses Buchs)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Architektur</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MVVM + ViewModel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Oberfläche und Logik trennen, der Code bleibt sauber</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Datenspeicherung</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room (Datenbank) + DataStore (Einstellungen)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Daten aufs Handy speichern</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Netzwerk</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit + OkHttp + Kotlin-Coroutinen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mit dem Server sprechen</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Build-Tool</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle + Kotlin DSL</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Aus Code ein Installationspaket machen</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Entwicklungsumgebung</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Googles offizielle „All-in-one“-IDE</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Der Android-Mainstream-Stack 2026 auf einen Blick

Lass dich von dieser Reihe englischer Begriffe nicht einschüchtern. Sie sind wie Töpfe und Pfannen in der Küche – du musst im Moment nur wissen: "Wer kochen will, geht in die Küche." Wie jedes einzelne Werkzeug funktioniert, wird dir in den folgenden Kapiteln Stück für Stück erklärt. Und die gute Nachricht: Android Studio richtet bei einem neuen Projekt diese ganze Konfiguration automatisch für dich ein – du kannst dich aufs Kochen konzentrieren.

#### 5. Android vs. iOS: die erste "Seitenwahl" für Entwickler

Vielleicht hast du gerade ein Android- und ein Apple-Gerät gleichzeitig in der Hand. Als Entwickler lohnt es sich, die Unterschiede im Voraus zu kennen – es geht nicht darum, Partei für "was besser ist" zu ergreifen, sondern um die nüchterne Rechnung, wo der Einstieg besser zu dir passt:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kriterium</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Android-Entwicklung</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">iOS-Entwicklung</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Entwicklungsrechner</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Windows / Mac / Linux – alles möglich</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nur Mac (Xcode gibt es exklusiv dort)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Entwicklungswerkzeug</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio (kostenlos)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode (kostenlos) + 99 USD Jahresgebühr für den Store</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Store-Prüfung</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">großzügig, einige Stunden bis wenige Tage</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">streng, 1–7 Tage sind die Norm</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Auf dem Gerät testen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">APKs frei verteilen und installieren</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">eingeschränkte Verbreitung, Tests brauchen Signierung/TestFlight</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Verdienstchancen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">überwiegend Werbung und chinesische Vertriebskanäle</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">im App Store ist die Zahlungsbereitschaft für In-App-Käufe besser</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lernaufwand</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">mehr Konzepte (die vier Grundkomponenten usw.)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">geschlossenes, aber einheitliches Ökosystem mit exzellenter Dokumentation</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Vergleich der Entwicklungswege für Android und iOS (Stand: August 2026)

Ganz ehrlich: Wenn dein Rechner kein Mac ist, stellst du die Frage gar nicht erst – Android ist die einzige Option. Hast du einen Mac, kannst du die Teile 8 und 9 dieses Buchs nebeneinander lesen; die Denkweise beim Programmieren ist dieselbe, und nach der einen Seite fällt das Lernen der anderen deutlich leichter.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Selbst ausprobieren: Wirf einen Blick auf das "Android" in deinem Telefon

{class="mt-1"}
Öffne auf dem Telefon [Einstellungen] → [Über das Telefon] (oder "Über dieses Gerät") und suche die Zeile "Android-Version" – tipp sie mehrmals hintereinander an, und ein verstecktes Mini-Spiel des Systems erscheint. Notiere deine Versionsnummer und schau in der Versionstabelle oben nach, zu welcher Generation sie gehört. Dein Telefon ist dein erstes "Entwicklungs-Testgerät".
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Zusammenfassung des Kapitels

- Android entstand 2008 und ist 2026 das mobile System mit dem größten Weltmarktanteil – Milliarden aktiver Geräte
- Neueste offizielle Version: Android 17; Mainstream-Apps unterstützen mindestens Android 8–10, nur so ist die Nutzerbasis groß genug
- Für neue Projekte immer Kotlin: über 30 % weniger Code, Schutz vor NullPointer-Fehlern, offiziell gekürt
- APK selbst installieren, AAB in den Store; das SDK ist das offizielle Entwickler-Werkzeugpaket
- Der Standard-Stack 2026: Kotlin + Compose + MVVM + Room + Retrofit + Gradle + Android Studio
:::
