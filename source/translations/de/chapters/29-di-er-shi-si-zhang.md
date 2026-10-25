---
id: di-er-shi-si-zhang
num: 24
part: chao-yue-pian
nav: Kapitel 24: Root-Rechte und BL-Sperre im Detail
toc: default
kind: chapter
---

### Kapitel 24: Root-Zugriff und Bootloader-Sperre vertieft

{class="chapter-intro mb-4"}
Zweitens. Detaillierter Ablauf der Bootloader-Entsperrung (am Beispiel Xiaomi)

#### Erstens. Bootloader tiefgehend verstehen

: Auf der Xiaomi-Entsperr-Tool-Website Entsperrrechte beantragen.

##### Konto binden

- <strong>: In den Smartphone-Einstellungen das Xiaomi-Konto binden.</strong> Warten
- <strong>: Abhängig von der Konto-Stufe sind 7–30 Tage Wartezeit nötig.</strong> Entsperrung durchführen
- <strong>: Mit dem Xiaomi-Entsperr-Tool das Smartphone mit dem PC verbinden und entsperren.</strong> Drittens. Mehrere Methoden für Root

##### 🔐 Hardware-Level-Speicherung und Verifizierung

Der Sperrzustand des BL (Locked/Unlocked) und der oeffentliche Schluessel des Herstellers sind meist in geschuetzten Hardware-Bereichen gespeichert (z. B. die devinfo-Partition von Qualcomm, eFuse oder RPMB-Partition), um Manipulation per Software zu verhindern. Bei jedem Start liest der Bootloader den Zustand aus diesem Sicherheitsbereich und entscheidet anhand dessen, ob eine strenge Signaturpruefung durchgefuehrt wird.

##### 🔏 Pruefung der digitalen Signatur

Beim Veroeffentlichen von System-Updates oder Images signiert der Hersteller diese mit seinem privaten Schluessel. Beim Geraetestart prueft der Bootloader die System-Images (z. B. boot.img, recovery.img) mit dem integrierten oeffentlichen Schluessel. Die Funktionsweise:

1. Den Hash-Wert des System-Images neu berechnen.
2. Die im Image enthaltene Signatur mit dem oeffentlichen Schluessel entschluesseln, um einen Hash-Wert zu erhalten.
3. Die beiden Hash-Werte vergleichen; bei Uebereinstimmung ist die Pruefung bestanden. So wird sichergestellt, dass das System-Image nicht von Dritten manipuliert wurde.

##### 🔗 Sichere Startkette

Das BL-Schloss ist das erste Glied der gesamten sicheren Startkette. Erst nach bestandener Pruefung wird die naechste Boot-Phase (z. B. der Kernel) geladen und ausgefuehrt – so wird die Vertrauenswuerdigkeit der Systemstartumgebung schrittweise gewaehrleistet.

##### 📊 Gesperrt vs. entsperrt: Die zwei Seiten des BL-Schlosses

Um Vor- und Nachteile des BL-Schlosses anschaulicher zu verstehen, zeigen wir eine Vergleichstabelle mit den Unterschieden in 5 Kernbereichen:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 dark:border-gray-600 text-sm">
                            <thead>
                                <tr class="bg-gray-100 dark:bg-gray-800">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kernfunktion</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Gesperrter Zustand (Standard)</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Entsperrter Zustand</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Systemsicherheit</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Verhindert das Flashen nicht signierter inoffizieller Systeme und schuetzt Systemintegritaet und Sicherheit der unteren Ebene<br><span class="text-emerald-600 dark:text-emerald-400">✅ Hohe Sicherheit: Es werden nur offiziell signierte Images geladen; effektiv gegen Manipulation boesartiger Firmware</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ Verringerte Sicherheit: Drittanbieter-ROMs koennen geflasht werden; die Systemintegritaetspruefung wird unwirksam. Erlangt Malware Root-Rechte, kann sie das System tiefgreifend manipulieren</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Systemstabilitaet</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stellt sicher, dass das Handy mit dem vom Hersteller getesteten und optimierten offiziellen System laeuft – fuer Stabilitaet und Fluessigkeit<br><span class="text-emerald-600 dark:text-emerald-400">✅ Stabil: Offizielle Firmware, vollstaendige Funktionen, zuverlaessige OTA-Updates</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ Erhoehtes Risiko: Drittanbieter-ROMs koennen Kompatibilitaetsprobleme haben, was zu Systemabstuerzen, Brick-Zustaenden, Hardware-Fehlfunktionen (z. B. Kamera, Schnellladen) oder fehlgeschlagenen OTA-Updates fuehren kann</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Garantierechte</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Der Hersteller liefert durch die BL-Sperre ein stabiles offizielles System als Grundlage fuer die Garantie<br><span class="text-emerald-600 dark:text-emerald-400">✅ Garantie gueltig: Kostenlose offizielle Garantie (bei nicht selbst verschuldeten Schaeden)</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ Garantie erloschen: Die meisten Hersteller werten die BL-Entsperrung als freiwilligen Garantieverzicht. Selbst nach erneuter Sperrung kann der Entsperrverlauf erkannt und die Garantie abgelehnt werden</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Datensicherheit</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Der Entsperrvorgang loescht in der Regel alle Daten, um zu verhindern, dass alte Daten im neuen Systemumfeld missbraeucht werden<br><span class="text-emerald-600 dark:text-emerald-400">✅ Datensicherheit: Im Alltag beschraenkt die BL-Sperre die Moeglichkeit boesartiger Programme, die Systempartition zu aendern</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ Datenrisiko: Beim Entsperren werden alle Nutzerdaten zwangsgeloescht. Wird nach dem Entsperren nicht korrekt verschluesselt, koennen Daten unsicher sein. Bei Verlust lassen sich Daten durch Flashen leichter extrahieren</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Funktionseinschraenkungen</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stellt sicher, dass sicherheitsabhaengige Funktionen (wie Zahlungen, Banking-Apps) normal laufen<br><span class="text-emerald-600 dark:text-emerald-400">✅ Vollstaendige Funktionen: Alle offiziellen Features sind nutzbar</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ Einschraenkungen: Einige sicherheitskritische Apps (z. B. Google Pay, Banking-Apps) koennen bei erkanntem entsperrtem BL die Ausfuehrung verweigern. DRM-Dienste koennen herabgestuft werden, was die HD-Videowiedergabe beeintraechtigt</span></td>
                                </tr>
                            </tbody>
                        </table>
```
:::

#### Zweitens. Detaillierter Ablauf der Bootloader-Entsperrung (am Beispiel Xiaomi)

1. <strong>: Moderne Root-Lösung, Systemless-Design, kann den Root-Status verbergen.</strong> KernelSU
2. <strong>: Kernel-basierte Root-Lösung, tieferliegend, bessere Tarnung.</strong> SuperSU
3. <strong>: Klassische Root-Lösung, wird nicht mehr weiterentwickelt.</strong> Viertens. Flash-Einsteiger
4. <strong>Flashen bedeutet, dem Smartphone ein neues Betriebssystem zu installieren. Häufige Flash-Arten:</strong> Offizielles ROM flashen

#### Drittens. Mehrere Methoden für Root

- <strong>Custom Recovery flashen</strong>: z. B. TWRP, für Backup/Wiederherstellung und zum Flashen von Custom-ROMs.
- <strong>Custom-ROM flashen</strong>: z. B. LineageOS, Pixel Experience usw., um ein anderes System zu erleben.
- <strong>Wichtige Warnung</strong> Flashen ist riskant, die Eingriffe müssen mit Bedacht vorgenommen werden. Mögliche Folgen:

#### Viertens. Flash-Einsteiger

Garantieverlust

- <strong>Datenverlust</strong> Zahlungsfunktionen gestört
- <strong>Erstelle vor dem Flashen unbedingt ein vollständiges Backup, lies die Anleitung sorgfältig durch und vergewissere dich, dass Modell und Version übereinstimmen.</strong> Empfohlene Ressourcen
- <strong>XDA Developers</strong>: Weltweit größte Android-Entwickler-Community mit reichhaltigen Flash-Anleitungen und ROM-Ressourcen.

#### V. Samsung Knox: Der unumkehrbare Preis der BL-Entsperrung

Anders als andere Android-Hersteller hat Samsung beim BL-Entsperrmechanismus ein einzigartiges „Ausloese"-Design:<strong>Bei Samsung-Smartphones loest die Entsperrung den Knox-Ausloeser aus, womit einige Sicherheitsfunktionen (wie Samsung Pay) dauerhaft verloren gehen; alle geschuetzten Daten werden geloescht; die Garantie ist betroffen</strong>. Im Einzelnen:

- <strong>Der Ausloeser ist einmalig</strong>: Im Handy befindet sich eine eFuse-Sicherung; sobald die BL-Entsperrung erkannt wird, schmilzt sie unwiderruflich und kann nicht wiederhergestellt werden.
- <strong>Betroffene Funktionen</strong>: Samsung Pay (Transit-/Bankkarten), Knox Sicherer Ordner, unternehmenstaugliche MDM-Kontrolle und einige Krankenversicherungs-Apps werden unbrauchbar.
- <strong>Erzwungenes Loeschen der Daten</strong>: Nach dem Ausloesen wird das Handy zwangsweise auf Werkseinstellungen zurueckgesetzt; alle lokalen Daten werden geloescht (Cloud-Daten sind nicht betroffen).
- <strong>Garantiewirkung</strong>: Offiziell heisst es, dass nach dem Knox-Ausloesen keine Garantie mehr gewaehrt wird.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Zweimal nachdenken vor dem Handeln

{class="mt-1"}
Der Knox-Ausloeser bei Samsung ist <strong>unumkehrbar</strong>; einmal ausgeloest, gibt es keinen Weg zurueck in den Werkszustand. Wenn du nur Funktionen nutzen moechtest, die eigentlich Root erfordern, pruefe zunaechst, ob es Alternativen ohne Root gibt.
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>Coolapk

{class="mt-1"}
: Bekannte chinesische Digital-Community mit vielen chinesischsprachigen Anleitungen und Diskussionen.

{class="list-disc pl-6 mt-1 space-y-1"}
- Modellspezifische Foren
- : z. B. Xiaomi-Community, OnePlus-Community usw., mit offiziellen und inoffiziellen Anleitungen.
- Kapitel 25: Gebrauchthandy-Verarbeitung und digitales Erbe
- Hey Leute, nach über zwanzig Kapiteln "Training" seid ihr sicherlich vom "digitalen Anfänger" zu einem ziemlich souveränen Smartphone-Nutzer herangewachsen. Aber das Tech-Leben kennt einen Kreislauf – die neue Liebe wird irgendwann zur alten. Wenn es heißt, sich vom alten Begleiter zu verabschieden: Wisst ihr, wie man würdevoll und sicher Abschied nimmt?

{class="mt-1"}
Erstens. "Sterben" des alten Smartphones: Leitfaden für sicheres Verkaufen oder Verschenken
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Kernprinzip: Datenbereinigung ist nicht "Löschen", sondern "Überschreiben".

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>"Großreinemachen"</strong>: Ein letztes vollständiges Backup durchführen, alle Konten abmelden.
- <strong>Endgültige "Formatierung"</strong>: Die "Auf Werkseinstellungen zurücksetzen"-Funktion moderner Smartphones umfasst meist eine verschlüsselte Löschung.
- <strong>Letzte "Täuschung"</strong>: Nach dem Zurücksetzen auf Werkseinstellungen den Speicher mit Mülldateien füllen und noch einmal auf Werkseinstellungen zurücksetzen.
:::

#### VI. Haeufige Fragen (Q&amp; A)

::: div .qa-item .mt-3
{class="font-semibold mb-1"}
<i class="fas fa-question-circle text-primary mr-1"></i>F1: Kann man den BL nach dem Entsperren wieder sperren?

{class="mb-2 pl-6"}
<strong>A:</strong> Ja, er kann neu gesperrt werden. In der Regel muss das komplette offizielle Flash-Paket geflasht und ein spezielles Flash-Skript (z. B. das von Xiaomi) <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">flash_all_lock.bat</code>) verwendet werden. Aber Achtung: Einige durch die Entsperrung ausgeloeste Sicherungen (wie Samsung Knox) koennen auch nach dem erneuten Sperren nicht rueckgaengig gemacht werden.
:::

::: div .qa-item .mt-3
{class="font-semibold mb-1"}
<i class="fas fa-question-circle text-primary mr-1"></i>F2: Wie rootet man nach dem Entsperren?

{class="mb-2 pl-6"}
<strong>A:</strong> Die BL-Entsperrung ist nur der erste Schritt. Root erfordert in der Regel:

{class="list-decimal pl-12 mb-2 space-y-1"}
1. Flashen eines Custom-Recovery (wie TWRP).
2. Ueber das Recovery einen Root-Manager wie Magisk flashen, um das Boot-Image zu patchen und Root zu erhalten.
:::
