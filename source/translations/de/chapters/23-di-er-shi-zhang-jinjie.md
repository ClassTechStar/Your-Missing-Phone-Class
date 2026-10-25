---
id: di-er-shi-zhang-jinjie
num: 20
part: jin-jie-pian
nav: Kapitel 20:Entwicklermodus und erweiterte Rechte
toc: default
kind: supplement
---

### Kapitel 20:Entwicklermodus und erweiterte Berechtigungen

{class="chapter-intro mb-4"}
Touch-Operationen anzeigen

#### I. Entwicklermodus: Versteckte Einstellungen freischalten

Hintergrundprozess-Limit

##### : Anzahl der im Hintergrund laufenden Apps begrenzen, spart Akku.

- <strong>Android</strong>: In manchen Fällen verbessert das die Flüssigkeit.
- <strong>HarmonyOS</strong> Die Einstellungen im Entwicklermodus können die Systemstabilität beeinflussen – bei Optionen, die du nicht verstehst, nicht herumprobieren. Nach dem Aktivieren von USB-Debugging beim Anschließen an einen Computer vorsichtig sein und keine nicht vertrauenswürdigen Computer verbinden.
- <strong>iOS</strong> Der Bootloader ist das Programm, das beim Starten des Smartphones das Betriebssystem lädt. Die BL-Sperre ist eine von den Herstellern aus Sicherheitsgründen angelegte Sperre, die verhindert, dass Nutzer nicht-offizielle Systeme flashen.

##### Uebersicht der haeufigen Funktionen:

- <strong>Sicherheitsschutz</strong>: Ein zwingend erforderlicher Schalter fuer erweiterte PC-Operationen (wie Flashen, Datenwiederherstellung, ADB-Befehle). Siehe Abschnitt „Nuetzliche ADB-Befehle" in diesem Kapitel.
- <strong>Garantieeinschränkung</strong>: Zeigt Beruehrungspunkte auf dem Bildschirm an (ein kleiner Punkt folgt dem Finger) – ideal fuer das Aufnehmen von Tutorials oder Demonstrationen.

##### Leistung und Fluessigkeit:

- <strong>Animationsgeschwindigkeit anpassen (Fensteranimationsskala / Uebergangsanimationsskala / Animator-Dauer-Skala)</strong>: Diese drei Optionen steuern die Animationsdauer beim Oeffnen von Apps und beim Seitenwechsel. Standard ist 1x; auf 0,5x eingestellt „wirkt" das Handy schneller (tatsaechlich aendert sich die Programmlaufzeit nicht, nur die Animation wird schneller). Ganz deaktiviert bedeutet Sprung ohne Animation. Die meisten Enthusiasten waehlen 0,5x – Uebergangsgefuehl bleibt, wirkt aber schneller. Komplett ausgeschaltet wirkt die Bedienung ruckelig und kann echte Ruckler verbergen, sodass man irrtuemlich „fluessig" denkt.
- <strong>GPU-Rendering erzwingen (Force GPU Rendering)</strong>: Erzwingt, dass alle 2D-Zeichenvorgaenge ueber die GPU statt der CPU laufen. Kann auf aelteren Geraeten oder bei schlecht optimierten Apps die Scroll-Fluessigkeit verbessern, erhoeht aber auch GPU-Last und Stromverbrauch. Moderne Smartphones nutzen bereits standardmaessig weitgehend GPU-Rendering; dieser Schalter hat bei Mittel- und Oberklassegeraeten kaum noch Wirkung und ist eher ein historisches Relikt. Normale Nutzer sollten die Standardeinstellung beibehalten.
- <strong>GPU-Rendering-Profil anzeigen (Profile GPU Rendering)</strong>: Zeigt auf dem Bildschirm ein Echtzeit-Balkendiagramm der Renderzeit pro Frame; die gruene Linie markiert 16,6 ms (der Frame-Zeit-Schwellenwert fuer 60 fps). Ueberschreiten die Balken die gruene Linie, gibt es Frame-Ausfaelle. Ein unverzichtbares Werkzeug fuer Entwickler zur Kompfort-Analyse; normale Nutzer koennen damit auch vergleichen, welche App schlecht optimiert ist – wenn die Balken beim Scrollen einer App regelmaessig ueber die rote Linie schießen, ist das App die Ursache.

##### Hintergrund und Akkulaufzeit:

- <strong>BL-Sperre-Politik der Marken:</strong>: Hier laesst sich „Standardlimit", „max. 1 Prozess", „max. 2 Prozesse" usw. einstellen. Scheinbar spart das Begrenzen von Hintergrundprozessen Strom, aber Androids integriertes Hintergrundmanagement ist bereits gut; ein erzwungenes Limit fuehrt eher zu haeufigem Neu-Laden von Apps (Kaltstart kostet sogar mehr Strom und verschlechtert die Erfahrung). Diese Option ist eher zum Debuggen gedacht; normale Nutzer sollten „Standardlimit" beibehalten.
- <strong>Keine Aktivitaeten beibehalten</strong>: Zerstoert jede Aktivitaet sofort beim Verlassen. Aeusserst nicht empfohlen – fuehrt zu haeufigen weissen Bildschirmen und Neu-Ladungen; nur zum Testen der Wiederherstellungslogik einer App gedacht.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Hinweise:

{class="mt-1"}
Eine
:::

#### II. OEM-Entsperrung: Der „Flash-Schalter" in den Entwickleroptionen

In den Entwickleroptionen gibt es einen unauffaelligen, aber wichtigen Schalter – „OEM-Entsperrung" (manche Marken nennen ihn „OEM-Entsperrung zulassen" oder „Geraet entsperren"). Dieser Schalter selbst entsperrt nicht den Bootloader, sondern ist eine „vorlaeufige Berechtigung": Erst wenn er aktiviert ist, erlaubt der Hersteller das Entsperren des BL per fastboot-Befehl oder markeneigenem Tool.

- <strong>Funktion des Schalters</strong>: Entspricht der Erklaerung gegenueber dem Hersteller: „Ich verzichte auf die Garantie, trage das Risiko selbst und beantrage die BL-Entsperrung." Ist der Schalter aus, wird jeder Entsperrbefehl direkt abgewiesen.
- <strong>Verhaeltnis zum BL-Schloss</strong>: OEM-Entsperrung ist der „Antrag auf Berechtigung"; die BL-Entsperrung ist die „tatsaechliche Durchfuehrung". Ersteres erledigt man mit einem Tip in den Einstellungen; letzteres erfordert das Beantragen eines Entsperrcodes auf der Hersteller-Website und das Ausfuehren eines fastboot-Befehls am PC (z. B. <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing unlock</code>). Beides ist unumgaenglich.
- <strong>Wird er durch Zuruecksetzen auf Werkseinstellungen zurueckgesetzt?</strong>: Ja. Der Schalter „OEM-Entsperrung" kehrt nach dem Werksreset in den Aus-Zustand zurueck. Der BL-Schloss-Zustand ist jedoch physischer Natur – einmal entsperrt, wird er durch einen Werksreset nicht wieder gesperrt. Er muss manuell mit <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing lock</code>  wieder gesperrt werden.
- <strong>Wann sollte man ihn aktivieren?</strong>: Wenn du nicht sicher flashen oder rooten willst, bleibt er ausgeschaltet. Er und „USB-Debugging" sind zwei unabhaengige Schalter; beim Flashen muessen beide aktiviert sein.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Wissenswertes: Warum hat der Hersteller diesen Schalter eingebaut?

{class="mt-1"}
Fruehe Android-Versionen hatten diesen Schalter nicht; Malware konnte bei entsprechenden Berechtigungen heimlich ein System einspielen. Google verlangte spaeter von allen Android-Herstellern, in den Entwickleroptionen einen „OEM-Entsperrung"-Schalter als „informierte Zustimmung" des Nutzers einzubauen. Deshalb schlaegt ein erneuter Flash-Versuch fehl, wenn der Schalter aus ist – selbst wenn der BL bereits entsperrt wurde.
:::

#### III. BL-Schloss (Bootloader-Sperre): Die erste Tuer zum Flashen

OPPO/vivo

##### : Bei einigen Modellen möglich, erfordert Antrag.

- <strong>Sicherheitsschutz</strong>: Kann entsperrt werden, löst aber Knox-Auslösung aus – Verlust von Samsung Pay und anderen Funktionen.
- <strong>Apple</strong>: iOS-Geräte haben kein BL-Sperre-Konzept im klassischen Sinn, aber ähnliche Sicherheitsmechanismen.
- <strong>III. Root-Rechte: Der „Super-Administrator" von Android</strong> Root-Rechte entsprechen dem Administrator unter Windows und sind die höchste Berechtigung im Android-System. Mit Root-Rechten kannst du Systemdateien ändern, vorinstallierte Apps deinstallieren und fortgeschrittene Apps nutzen, die Root benötigen.

##### Vorteile von Root:

- <strong>Xiaomi</strong> Apps mit fortgeschrittenen Funktionen nutzen (wie Titanium Backup, Greenify).
- <strong>Ultra</strong> Third-Party-Recovery und Custom-ROMs installieren.
- <strong>Risiken von Root:</strong> Garantieverlust
- <strong>: Die meisten Hersteller geben auf gerootete Smartphones keine Garantie.</strong> Sicherheitsrisiko
- <strong>Samsung</strong> Systeminstabilität
- <strong>Niedriger Stromverbrauch</strong> Bank-Apps funktionieren nicht

#### IV. Nuetzliche ADB-Befehle: Das Smartphone vom PC aus steuern

ADB steht fuer Android Debug Bridge und ist ein von Google bereitgestelltes Befehlszeilen-Tool, das die Kommunikation zwischen PC und Android-Smartphone ueber USB oder Wi-Fi ermoeglicht. Es benoetigt kein Root; es reicht, wenn am Handy „USB-Debugging" aktiviert ist. Man kann es sich als „Fernbedienung vorstellen, mit der der PC dem Handy Befehle gibt" – Flashen, Apps installieren, Dateien uebertragen, Logs auslesen: Alles geht ueber ADB.

##### So stellst du eine USB-Verbindung her:

1. Am Handy: Entwickleroptionen oeffnen → „USB-Debugging" aktivieren.
2. Am PC: Lade die Platform Tools von Google herunter (enthalten <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb</code> „ <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot</code> ausfuehrbare Dateien) und entpacke sie in ein beliebiges Verzeichnis.
3. Verbinde Handy und PC mit einem USB-Kabel. Am Handy erscheint die Abfrage „USB-Debugging zulassen?" – haekche „immer zulassen" an und bestaetige.
4. Fuehre in der PC-Befehlszeile (PowerShell oder cmd unter Windows) den Befehl <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code> aus. Wenn die Ausgabe in etwa <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">List of devices attached / xxxxxxxx device</code> lautet, ist die Verbindung hergestellt.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Treiber und Berechtigungsdialog nicht ignorieren

{class="mt-1"}
Wenn Windows-Nutzer den Befehl <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code>  „unauthorized" anzeigt oder ueberhaupt kein Geraet auflistet, fehlt meist der Treiber oder man hat am Handy vergessen, „zulassen" zu tippen. Fuer Samsung, Xiaomi und andere Marken lassen sich die jeweiligen „USB-Treiber" oder „Handy-Assistenten" installieren; Mac und Linux sind in der Regel treiberfrei. Wenn man den Dialog am Handy versehentlich weggetippt hat, einfach das Kabel neu anstecken – der Dialog erscheint erneut.
:::

##### Haeufig verwendete ADB-Befehle:

- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb install app.apk</code>: APK vom PC auf dem Handy installieren (<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-r</code>  bedeutet Neuinstallation unter Beibehaltung der Daten;<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code>  Installation auf SD-Karte).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb uninstall com.xxx.xxx</code>: App nach Paketnamen deinstallieren.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb push PC-Pfad /sdcard/Zielpfad</code>: Datei vom PC auf das Handy uebertragen.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb pull /sdcard/Datei PC-Pfad</code>: Datei vom Handy auf den PC ziehen (viel schneller als sie sich selbst ueber WeChat zu schicken und herunterzuladen).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell</code>: In die Linux-Shell des Handys wechseln; dort lassen sich Befehle wie <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls</code>, <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm</code>, <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">am</code>  usw. direkt ausfuehren.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot bootloader</code>: Handy in den Fastboot-Modus neu starten (Einstieg zum Flashen).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot recovery</code>: In den Recovery-Modus neu starten.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages</code>: Alle Paketnamen der installierten Apps auflisten (unerlaesslich zum Finden des Paketnamens). Mit <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code>  nur System-Apps, mit <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-3</code>  nur Drittanbieter-Apps.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 Paketname</code>: Vorinstallierte App fuer den aktuellen Nutzer deinstallieren – ohne Root. Siehe praktisches Beispiel unten.

##### Vorinstallierte Apps ohne Root deinstallieren – Praxisbeispiel:

Dies ist eine der praktischsten ADB-Funktionen: Mit dem Befehl <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code>  lassen sich vorinstallierte Apps fuer den „aktuellen Nutzer" deinstallieren – ohne Root und ohne die Systempartition zu beeinflussen. Die deinstallierte App „verschwindet" aus dem System, ist aber tatsaechlich noch in der Systempartition vorhanden und kehrt nach einem Werksreset zurueck.

1. Zuerst mit <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages -s</code>  alle System-Apps auflisten und den Paketnamen der App finden, die du entfernen moechtest. Zum Beispiel ist der Xiaomi-Browser <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.browser</code>, der Huawei App Market <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.vmall.client</code>.
2. Unsicher, welche App zu einem Paketnamen gehoert? Am PC laesst sich mit <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages | findstr Suchbegriff</code>  suchen, oder eine Drittanbieter-App „Package Viewer" installieren, die auf dem Handy die Paketnamen aller Apps anzeigt.
3. Deinstallation ausfuehren:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 Paketname</code>, z. B. <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 com.android.browser</code>. Rueckgabe <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Success</code>  bedeutet Erfolg.
4. Wie stellst du es wieder her? Zwei Moeglichkeiten: ① Werksreset (gruendlich, aber muehsam); ② Neu installieren:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell cmd package install-existing Paketname</code>.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>Bloed nicht System-Kernpakete loeschen

{class="mt-1"}
„pm uninstall --user 0" ist zwar eine sichere Methode ohne Root, aber das Loeschen kritischer System-Apps (wie <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.systemui</code>  Statusleiste,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.phone</code>  Telefon,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.settings</code>  Einstellungen) kann zu Systemabstuerzen, schwarzen Bildschirmen oder Boot-Problemen fuehren. Vor dem Loeschen kurz suchen: „Ist dieser Paketname sicher zu loeschen?" – lieber weniger loeschen als falsch loeschen. Empfohlen: Nur ein bis zwei gleichzeitig entfernen und erst weitermachen, wenn alles funktioniert.
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Wissenswertes: Was bedeutet „--user 0"?

{class="mt-1"}
Ab Android 4.2 wird Mehrbenutzerbetrieb unterstuetzt; jeder Nutzer hat eine eigene ID (Geraetebesitzer ist 0, Zweitnutzer beginnen bei 10).<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">--user 0</code>  bedeutet „nur fuer den aktuellen Besitzer deinstallieren"; die APK-Datei in der Systempartition bleibt bestehen, wird dem Besitzer nur nicht mehr angezeigt. Deshalb ist kein Root noetig – es werden keine Systemdateien geaendert, sondern nur die „Nutzerkonfiguration". Das ist auch der wesentliche Unterschied zum Loeschen mit Root: Root-Loeschen entfernt die App tatsaechlich aus dem System, fuer alle Nutzer; ADB-Loeschen „versteckt" sie nur fuer den aktuellen Nutzer.
:::

#### V. Root-Berechtigung: Der „Superadmin" von Android

Root-Berechtigung entspricht dem Superuser unter Linux (volle Kontrolle ueber das /-Verzeichnis, Lese- und Schreibzugriff auf beliebige Dateien) und ist die hoechste Berechtigungsstufe in Android. Sie unterscheidet sich grundlegend vom Windows-Administrator: Windows schraenkt den Administrator aus Sicherheitsgruenden stark ein (die tatsaechlich hoechste Berechtigung ist TrustedInstaller); selbst ein Administrator kann nicht wie ein Linux-root direkt <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">sudo rm -rf /*</code> ausfuehren. Mit Root-Berechtigung kannst du Systemdateien aendern, vorinstallierte Apps entfernen und fortgeschrittene Apps nutzen, die Root benoetigen.

##### : Offizielle System-Updates können evtl. nicht mehr empfangen werden.

- Ernsthafte Warnung
- Root-Operationen sind riskant und können das Smartphone „bricken" (es lässt sich nicht mehr einschalten). Wenn du Anfänger bist, solltest du dich zuerst ausführlich informieren und ein vollständiges Backup haben. Lies vor der Operation das Tutorial sorgfältig und bestätige dein Modell und die Systemversion.
- IV. Empfehlungen für normale Nutzer
- Entwicklermodus

##### : Kann aktiviert werden, um z. B. Animationsbeschleunigung auszuprobieren – aber nicht andere Einstellungen blind ändern.

- <strong>: z. B. Xiaomi-Community, OnePlus-Community usw., mit offiziellen und inoffiziellen Anleitungen.</strong>: Wenn du nicht flashen willst, ist es sicherer, sie gesperrt zu lassen.
- <strong>Root</strong>: Für normale Nutzer nicht empfohlen – das Risiko überwiegt den Nutzen. Wenn du bestimmte Funktionen brauchst, prüfe zuerst, ob es Alternativen ohne Root gibt.
- <strong>Wissenswertes: Magisk</strong> ist eine moderne Root-Lösung. Ihr Merkmal ist „Systemless" – sie modifiziert nicht die Systempartition, sondern erreicht Root durch Einhängen. So lässt sich der Root-Status verbergen, sodass Apps, die Root erkennen (wie Bank-Apps), normal laufen. Die Verwendung von Magisk erfordert jedoch weiterhin das Entsperren des BL.
- <strong>Hand an: Aktiviere den Entwicklermodus und passe die Animationsgeschwindigkeit an</strong> Gehe zu Einstellungen → Über das Telefon.
- <strong>Tippe 7-mal auf „Build-Nummer", bis die Meldung erscheint, dass der Entwicklermodus aktiviert ist.</strong> Gehe zurück zu den Einstellungen und suche „Entwickleroptionen" (meist am Ende der Einstellungen oder unter „System").

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>Finde „Fenster-Animationsskala", „Übergangs-Animationsskala" und „Animationsdauer-Skala" und setze sie alle auf 0,5x oder aus.

{class="mt-1"}
Prüfe, ob sich das Smartphone schneller anfühlt.
:::

#### VI. SafetyNet- und Play Integrity-Zertifizierung: Warum Banking-Apps nach Root nicht mehr funktionieren

Viele Root-Nutzer kennen diesen Schockmoment: Nach dem Rooten begeistert eine ganze Reihe Modulen installiert, dann die Banking-App geoeffnet – „Ihr Geraet ist nicht sicher und kann nicht verwendet werden"; Google Pay geht auch nicht, sogar Netflix verweigert die HD-Wiedergabe. Dahinter stehen zwei Google-Zertifizierungssysteme fuer Geraeteintegritaet: das aeltere SafetyNet und die neuere Play Integrity API.

##### Was sind SafetyNet / Play Integrity:

- <strong>SafetyNet Attestation (alte Version, seit 2017)</strong>: Eine frueh von Google eingefuehrte API zur Ueberpruefung der Geraeteintegritaet. Apps fragen darueber die Google-Server ab: „Hat dieses Geraet die CTS-Kompatibilitaetstests bestanden und befindet es sich in einem unmodifizierten offiziellen Zustand?" Die Ergebnisse umfassen Basic Attestation (Basispruefung) und Strong Attestation (starke Pruefung, auf Hardware-Schluessel gestuetzt). Google hat angekundigt, SafetyNet nach 2024 schrittweise einzustellen.
- <strong>Play Integrity API (neue Version, seit 2022)</strong>: Der von Google eingefuehrte Nachfolger, strenger und umfassender als SafetyNet. Neben der Geraeteintegritaet umfasst er „App-Integritaet" (wurde die App manipuliert?) und „Konto-/Autorisierungsintegritaet" (ist das Nutzerkonto von Google vertraut?). Neue Apps sollten auf Play Integrity migrieren.
- <strong>Wer nutzt das?</strong>: Bank-, Finanz- und Zahlungs-Apps (wie Google Pay, Online-Banking der Banken, in Teilbereichen Alipay/WeChat Pay), Streaming-Dienste (Netflix-HD-Urheberrechtsschutz), einige Anti-Cheat-Systeme bei Spielen (z. B. Tencent/NetEase) und Unternehmens-Apps (MDM-Geraetekompatibilitaetspruefung).

##### Die drei Zertifizierungsstufen von Play Integrity:

- <strong>MEETS_DEVICE_INTEGRITY (Geraeteintegritaet bestanden)</strong>: Das Geraet laeuft mit einem originalen Android-System, der Bootloader ist gesperrt, kein Root, CTS-Kompatibilitaetstest bestanden. Banking- und Zahlungs-Apps koennen normal verwendet werden.
- <strong>MEETS_BASIC_INTEGRITY (Basisintegritaet bestanden)</strong>: Das Geraet ist grundsaetzlich vertrauenswuerdig, aber es koennen leichte Anomalien vorliegen. Manche Apps greifen auf eine eingeschraenkte Nutzung zurueck (z. B. Netflix spielt weiterhin ab, aber mit limitierter Aufloesung); strikte Banking-Apps lehnen direkt ab.
- <strong>MEETS_STRONG_INTEGRITY (starke Integritaet bestanden)</strong>: Hoechste Stufe; erfordert Hardware-Schluessel-Beglaubigung (z. B. der Titan-M-Chip der Google-Pixel-Serie). Die meisten Drittanbieter-Geraete erreichen diese Stufe selbst ohne Root nicht.
- <strong>Keine Kennzeichnung (NO_INTEGRITY)</strong>: Das Geraet wurde gerootet, der BL entsperrt, ein Custom-ROM geflasht oder als Emulator erkannt. Die allermeisten Zahlungs- und Banking-Apps lehnen die Ausfuehrung direkt ab.

##### Warum funktionieren diese Apps nach Root nicht mehr:

Die App sendet ueber die Play Integrity API eine Zertifizierungsanfrage an die Google-Server. Google prueft mehrere Indikatoren – Bootloader-Sperrzustand, ob die Systempartition geaendert wurde, ob eine su-Binaerdatei existiert, ob SELinux im Permissive-Modus laeuft usw. Jede Abweichung fuehrt zu einer herabgestuften oder leeren Zertifizierungsstufe. Die Banking-App sieht „Geraet unsicher" und verweigert den Dienst.

##### Moderne Versteck-Methoden: Magisk Hide / Shamiko / Zygisk:

Um die Vorteile von Root zu geniessen und gleichzeitig Banking-Apps nutzen zu koennen, hat die Community verschiedene Loesungen entwickelt, die den Root-Status „verstecken". Der Kerngedanke: Das Pruefprogramm soll kein modifiziertes System sehen, sondern ein „normal aussehendes" Geraet.

- <strong>Custom Recovery flashen</strong>: Die aktuell am weitesten verbreitete Systemless-Root-Methode – die Systempartition wird nicht modifiziert; Root wird ueber Mounts realisiert. Der Vorteil: OTA-Updates seltener fehlerhaft, saubere Deinstallation; sie ist die Grundlage aller spaeteren Versteck-Methoden. Die Verwendung von Magisk erfordert jedoch weiterhin einen entsperrten BL.
- <strong>Magisk Hide (nicht mehr gepflegt)</strong>: Ein frueher in Magisk integriertes Versteck-Modul, das Root fuer bestimmte Apps verbergen konnte. Ab 2021 von Magisk offiziell entfernt, da Google die Erkennungsmethoden kontinuierlich verstaerkt hat – ein „Katze-und-Maus-Spiel" entstand.
- <strong>Zygisk</strong>: Ein mit Magisk 24.0+ eingefuehrter Mechanismus, aehnlich wie Riru, der Modul-Ladevorgaenge durch Injektion in den Zygote-Prozess realisiert – unauffaelliger als direkte Systemaenderungen. Die Aktivierung von Zygisk ist Voraussetzung fuer moderne Versteck-Methoden.
- <strong>Shamiko</strong>: Das aktuell am weitesten verbreitete Versteck-Modul; arbeitet mit Zygisk zusammen und kann fuer bestimmte Apps (im „umgekehrte Whitelist"-Modus) Root verbergen, Magisk selbst verstecken und den gesperrten Bootloader-Status vortaeuschen. Shamiko wird ueber das LSPosed-Repository oder GitHub vertrieben.
- <strong>Play Integrity Fix(osm0sis)</strong>: Ein Magisk-Modul, das speziell auf die Google-Play-Integrity-Pruefung abzielt und den Geraetefingerabdruck (fingerprint) so veraendert, dass Google das Geraet als ein nicht gerootetes Originalmodell erkennt.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Das Katze-und-Maus-Spiel endet nie

{class="mt-1"}
Google aktualisiert die Erkennungsregeln regelmaessig, und App-Hersteller ziehen mit verstaerkten Play-Integrity-Pruefungen nach. Eine Methode, die heute funktioniert, kann morgen erkannt werden. Wenn du vollstaendig auf Banking-/Zahlungs-Apps angewiesen bist (z. B. taegliche Ueberweisungen, QR-Code-Zahlungen), ist die sicherste Wahl weiterhin: kein Root, BL nicht entsperren. Versteck-Methoden eignen sich eher fuer die Konstellation „Hauptgeraet ohne Root + Zweitgeraet zum Rooten-Experimentieren".
:::

#### VII. Empfehlungen fuer normale Nutzer

- <strong>Wenn dir der Entwicklermodus nicht „hardcore" genug ist und du die vollständige Linux-Kommandozeile auf dem Smartphone erleben willst, dann ist Termux genau das Richtige für dich. Ohne Root-Rechte verwandelt es ein normales Android-Smartphone in eine portable Linux-Workstation – ein mächtiges Werkzeug für fortgeschrittene Nutzer, die Entwicklung und Systemadministration auf mobilen Geräten erkunden wollen.</strong>: Kann aktiviert werden, um Animationsbeschleunigung oder GPU-Rendering-Analyse auszuprobieren. Aber nicht an Optionen herumspielen, die du nicht verstehst.
- <strong>OEM-Entsperrung und BL-Schloss</strong>: Wenn du nicht flashen oder rooten willst, bleiben beide Schalter am sichersten im Standardzustand (aus).
- <strong>ADB</strong>: Ein maechtiges Werkzeug ohne Root, das auch normale Nutzer verwenden koennen – z. B. mit <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code>  vorinstallierte Apps entfernen. Vor dem Loeschen aber unbedingt pruefen, ob der Paketname sicher zu entfernen ist.
- <strong>Lokal auf dem Smartphone laufende KI</strong>: Normale Nutzern wird vom Rooten abgeraten – das Risiko ueberwiegt den Nutzen. Wenn du bestimmte Funktionen brauchst, pruefe zunaechst, ob es Alternativen ohne Root gibt (z. B. vorinstallierte Apps per ADB entfernen, Shizuku als Ersatz fuer einige Root-Funktionen).

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Verwendet den APT-Paketmanager (ähnlich wie Debian und Ubuntu), mit dem tausende Linux-Softwarepakete installiert werden können – darunter Entwicklungs- und Netzwerk-Tools. Unterstützt mehrere Programmiersprachen-Umgebungen wie Python, Ruby, Node.js, Go, Rust, Swift.

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 🔒 Sicherheits- und Netzwerkfunktionen
2. SSH-Remote-Verbindung
3. : Unterstützt SSH-Client- und -Server-Funktionen, kann andere Geräte remote verbinden oder das Smartphone zum SSH-Host machen.
4. Verschlüsselungs-Tools
5. : Bietet OpenSSL und andere Verschlüsselungs-Tools, unterstützt Datenverschlüsselung und sichere Kommunikation.
:::
