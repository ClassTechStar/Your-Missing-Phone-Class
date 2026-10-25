---
id: di-er-shi-san-zhang
num: 23
part: chao-yue-pian
nav: Kapitel 23: Programmier-Denken und Automatisierung für Einsteiger
toc: default
kind: chapter
---

### Kapitel 23: Programmier-Denken und Automatisierung für Einsteiger

{class="chapter-intro mb-4"}
In den letzten beiden Kapiteln haben wir dem Smartphone eine sichere „Grenzwand“ gebaut und sein im Inneren immer schlauer werdendes „KI-Gehirn“ erlebt. Jetzt schalten wir eines der ultimativen Potenziale des Smartphones frei: Es soll wie ein Programmierer „denken“ und die von dir festgelegten Aufgabenketten automatisch abarbeiten. Du sagst vielleicht: „Ich kann doch nicht programmieren – was hat das mit mir zu tun?“

#### Erstens. Was ist Automatisierung überhaupt?

In einfachen Worten: Automatisierung bedeutet,<strong>dass das Handy bei einer bestimmten Bedingung automatisch eine ganze Kette von Aufgaben für dich erledigt.</strong> Du musst nicht jedes Mal von Hand eingreifen oder daran denken, was zu tun ist – das Handy erkennt selbst den Zeitpunkt und führt aus.

Ein Beispiel: Jeden Morgen nach dem Aufwachen machst du von Hand den Nicht-stören-Modus aus, öffnest WeChat, um die Nachrichten zu sehen, öffnest die Wetter-App, um zu sehen, was du heute anziehst, und startest deine Musik-App. Packst du diese Schritte in einen Automatisierungsablauf und stellst ihn auf „jeden Morgen um 7 Uhr automatisch ausführen“, musst du nach dem Aufwachen nur noch das Handy in die Hand nehmen – alles ist schon vorbereitet.

Automatisierung ist im Kern eine "Wenn … dann …"-Logikkette, das if-else der Programmierung. Wer diese Denkweise verstanden hat, wird – selbst wenn er nie eine Zeile Code schreibt – deutlich strukturierter an Probleme herangehen. Die Kernelemente:

1. <strong>Auslösebedingung</strong>: Wann soll es beginnen? Das kann "jeden Morgen um 7:00 Uhr", "wenn ich mich mit dem heimischen WLAN verbinde", "wenn ich einen bestimmten Ort erreiche", "wenn der Akkustand unter 20 % fällt" sein.
2. <strong>Aktion</strong>: Was genau tun? Das kann eine WeChat-Nachricht senden, eine App öffnen, die Lautstärke anpassen, das Hintergrundbild wechseln, Musik abspielen, eine Benachrichtigung verschicken … nahezu alles, was du am Smartphone manuell tun kannst, lässt sich auch automatisieren.
3. <strong>Mittlere Logik</strong>(optional, aber sehr mächtig): Wenn Situation A eintritt, tue X, sonst Y. Zum Beispiel: "An Werktagen Nachrichten-Podcast abspielen, am Wochenende Musik" – das nennt man bedingte Verzweigung.

#### Zweitens. Apples „Kurzbefehle“ – das Automatisierungswunderwerk für Apple-Nutzer

Apples "Kurzbefehle" (Shortcuts) ist eine vorinstallierte App, die nicht heruntergeladen werden muss. Ihr Kernkonzept besteht darin, verschiedene Aktionen wie Bauklötze zusammenzusetzen. Zunächst einige Schlüsselbegriffe:

- <strong>„Kurzbefehle“</strong>: Ein vollständiger Automatisierungsablauf, der manuell per Tap oder per Siri-Sprachbefehl gestartet werden kann. Wenn du z. B. sagst "Hey Siri, Heimweg-Modus", führt er automatisch die vorbereitete Aktionenkette aus.
- <strong>"Automatisierung"</strong>: Ein Befehl, der durch eine Auslösebedingung automatisch läuft, ohne dass du manuell auslösen musst. Zum Beispiel: "Wenn das Smartphone sich mit der Bluetooth-Freisprecheinrichtung des Autos verbindet, automatisch die Karten-App öffnen." Automatisierungen werden im Reiter "Automatisierung" eingerichtet und sind von den "Kurzbefehlen" getrennt.
- <strong>„Aktionen“</strong>: Die kleinste Ausführungseinheit. Eine App öffnen ist eine Aktion, eine Nachricht senden ist eine Aktion, das Wetter abrufen ist eine Aktion, die Helligkeit anpassen ist eine Aktion. Du kannst Hunderte Aktionen aneinanderreihen.

Hier sind einige praktische Beispiele – wenn du sie einmal nachbaust, verstehst du es sofort:

##### Beispiel 1: Ein-Klick "Guten-Morgen-Ablauf"

Jeden Morgen tippst du einmal (oder sagst zu Siri "Guten Morgen"), und das Smartphone erledigt automatisch: das heutige Wetter abrufen → Wetter und Temperatur vorlesen → heutige Kalendertermine anzeigen → deine Lieblings-Musik-App öffnen und abspielen. Bedienungsschritte: Neuer Kurzbefehl → Aktion "Aktuelles Wetter abrufen" hinzufügen → "Text vorlesen" hinzufügen → "Kalenderereignisse abrufen" hinzufügen → "Erinnerung anzeigen" hinzufügen → Aktion "App öffnen" und NetEase Cloud Music auswählen. So einfach – alles per Drag-and-Drop.

##### Beispiel 2: Automatischer "Energiesparmodus"

Im Reiter "Automatisierung" eine neue Automatisierung erstellen → "Akkustand" → auf "unter 30 %" einstellen → Aktion "Energiesparmodus aktivieren" hinzufügen + "Bildschirmhelligkeit auf 50 %" setzen + "Bluetooth ausschalten". Ab jetzt wechselt das Smartphone bei unter 30 % automatisch in den Energiesparmodus, ohne dass du dich kümmern musst.

##### Beispiel 3: Scan-Code erfasst automatisch Ausgaben

Jedes Mal, wenn du nach dem Scannen eines Codes mit WeChat/Alipay bezahlst, liest das Smartphone die Zahlungsbenachrichtigung und trägt Betrag und Händler automatisch in eine Notiz oder eine Numbers-Tabelle ein. Dazu benötigst du in den "Automatisierungen" der Kurzbefehle den Auslöser "SMS/Benachrichtigung empfangen" (iOS 17+ unterstützt das Auslesen von Wallet-Transaktionen), kombiniert mit der Aktion "An Numbers anhängen". Für alle, die Ausgaben erfassen wollen, aber zu bequem sind, es manuell zu tun, ist das ein Lebensretter.

Ein weiterer, wenig bekannter Trick: Du kannst einen Kurzbefehl zum Home-Bildschirm hinzufügen, sodass er wie ein App-Icon aussieht. Zum Beispiel baust du einen Kurzbefehl "Taxi nach Hause", platzierst das Icon auf dem Desktop, und ein Tipper öffnet direkt DiDi und setzt das Ziel auf deine Wohnung – viel schneller, als die App manuell zu öffnen und die Adresse einzugeben.

#### Drittens. Android-Automatisierung – Tasker und seine Freunde

Auf der Android-Seite ist die Lage etwas komplexer, aber die Decke ist auch höher. Zunächst das Einfache:

##### Einsteigerklasse: Auto-Clicker

Viele Android-Smartphones haben einen vorinstallierten "Auto-Clicker" oder er lässt sich im App-Store herunterladen. Das Prinzip ist simpel: Du führst eine Aktion manuell aus, er zeichnet deine Klick-Koordinaten und Zeitabstände auf und kann sie dann in hoher Geschwindigkeit abspielen. Wenn eine App z. B. täglich ein Anmeldegeschenk gibt, nimmst du den Klick-Ablauf einmal auf und lässt ihn künftig täglich automatisch ablaufen. Nachteil: Er erkennt nur Koordinaten; ändert sich das Layout (z. B. durch eine Werbeeinblendung), klickt er daneben.

##### Fortgeschrittenenklasse: Tasker – der König der Android-Automatisierung

Tasker ist das unangefochten stärkste Automatisierungstool auf Android und führt die Charts seit Jahren an. Um ehrlich zu sein: Die Lernkurve ist etwas steil, die Oberfläche nicht gerade hübsch, aber einmal verstanden, fühlt sich das Smartphone plötzlich allmächtig an. Taskers Kern folgt ebenfalls dem Muster "Auslöser → Aufgabe":

- <strong>Profil (Profile)</strong>: Definiert, wann ausgelöst wird. Auslöser können Zeit, Ort, WLAN-Verbindungsstatus, Bluetooth-Verbindung, Empfang einer bestimmten Benachrichtigung, Akkuzustand, Bildschirmausrichtung … sein. Tasker unterstützt Dutzende Auslöser.
- <strong>Aufgabe (Task)</strong>: Definiert, was nach dem Auslösen passiert. Eine Aufgabe kann mehrere Aktionen enthalten, die nacheinander ausgeführt werden. Aktionstypen umfassen: Systemeinstellungen anpassen (Lautstärke, Helligkeit, WLAN, Bluetooth, Flugmodus), SMS senden, HTTP-Anfragen, Shell-Befehle ausführen, Medienwiedergabe steuern, Dialogfelder einblenden usw.

Hier einige klassische, praktische Tasker-Szenarien:

- <strong>Zuhause automatisch WLAN aktivieren</strong>: Auslöser "Verbindung mit bestimmter Mobilfunkzelle" (weil du in der Nähe deiner Wohnung immer dieselbe Zelle erreichst) → Aufgabe "WLAN aktivieren". Ohne GPS, ohne Stromverbrauch – sobald das Smartphone in den Bereich der Wohnanlage kommt, wird WLAN automatisch aktiviert.
- <strong>Besprechungsmodus</strong>: Auslöser "Kalenderereignis-Titel enthält 'Besprechung'" → Aufgabe "Lautlos-Modus aktivieren, Medienlautstärke aus, automatische WeChat-Antwort (Plugin erforderlich)". Nie wieder Sorge, dass das Smartphone in der Besprechung plötzlich klingelt.
- <strong>Nächtlicher Augenschutz</strong>: Auslöser "Zeit 22:00–06:00" → Aufgabe "Augenschutz-Modus aktivieren, Helligkeit auf 20 %, Bildschirm auf Schwarz-Weiß (Graustufenmodus) setzen". Der Schwarz-Weiß-Bildschirm wirkt Wunder gegen den Drang, Kurzvideos zu scrollen – ist das Bild grau, willst du gar nicht mehr scrollen.
- <strong>Kopfhörer eingesteckt → automatisch Podcast</strong>: Auslöser "Kabelkopfhörer eingesteckt / Bluetooth-Kopfhörer verbunden" → Aufgabe "Xiaoyuzhou-App öffnen und neueste Folge abspielen". Kopfhörer aufsetzen und sofort hören, ohne das Smartphone zu entsperren und die App zu suchen.

Wenn dir Tasker zu schwer erscheint, probiere seinen vereinfachten Bruder <strong>MacroDroid</strong>. Die Oberfläche ist deutlich freundlicher, die Vorlagen sind reichhaltig – geeignet für Nutzer, die nicht basteln wollen. Außerdem haben viele chinesische Android-Systeme (Xiaomis MIUI, Huaweis HarmonyOS, OPPOs ColorOS) eine eingebaute "Szenen"- bzw. "Intelligenter Assistent"-Funktion, die zwar nicht so mächtig wie Tasker ist, aber für die Alltagsautomatisierung völlig ausreicht.

#### Viertens. Alltagsanwendungen des Automatisierungsdenkens

Der größte Gewinn beim Erlernen von Automatisierung ist nicht die gesparte Zeit, sondern <strong>eine veränderte Art, über Probleme nachzudenken</strong>. Wenn du dich an das Denkmodell "Wenn X eintritt, tue automatisch Y" gewöhnst, entdeckst du, dass sich ein großer Teil der wiederkehrenden Arbeiten im Leben eliminieren lässt. Zum Beispiel:

- Nach jedem Foto automatisch in die Cloud sichern und danach die lokalen Fotos auf kleine Größe komprimieren, um Platz zu sparen.
- Jeden Morgen automatisch den heutigen Kalender auslesen, einen Text generieren und per WeChat an die Familie senden.
- Nach Empfang einer Express-SMS automatisch in Notizen einen To-do-Eintrag "Paket abholen" anlegen.
- Wenn der Akku voll ist, automatisch eine Sprachansage ausgeben und zum Abziehen des Ladegeräts ermahnen (um Überladen zu vermeiden).
- Wenn Feierabendzeit erreicht ist und du dich noch in der Nähe des Büros befindest (per Mobilfunkzelle geortet), automatisch an "Feierabend!" erinnern.

Das klingt hochgestochen, aber sobald du die beiden Grundkonzepte "Auslöser + Aktion" verstanden und mit Kurzbefehlen oder Tasker kombiniert hast, kannst du all das umsetzen. Entscheidend ist,<strong>dass du zuerst erkennst: "Diese Sache lässt sich automatisieren"</strong>– viele können es nicht, weil sie gar nicht in diese Richtung denken.

#### Fünftens. Fallenschutz-Leitfaden: Häufige Probleme der Automatisierung

Automatisierung läuft nicht immer rund; ich habe einige Fallgruben für dich vorab durchschritten:

- <strong>Ortsbasierte Auslöser können unzuverlässig sein</strong>: iOS' "Ankunft/Verlassen"-Auslöser nutzt Geofencing-Technik; die Genauigkeit hängt vom GPS-Signal und der Systemoptimierung ab. Manchmal wird erst zehn Minuten nach deiner Ankunft zu Hause ausgelöst. Empfehlung: WLAN-Verbindung oder Mobilfunkzelle als Auslöser verwenden – zuverlässiger und stromsparender.
- <strong>Kurzbefehl-Automatisierungen benötigen Berechtigungen</strong>: In iOS müssen die meisten Auslöser unter dem Reiter "Automatisierung" manuell bestätigt werden, bevor sie laufen (Sicherheitsmechanismus von iOS). Aber WLAN-Verbindung, Bluetooth-Verbindung und Wecker-Stopp können tatsächlich vollautomatisch laufen, ohne Bestätigung.
- <strong>Tasker benötigt Aktivierung der Bedienungshilfen-Berechtigung</strong>: Viele fortgeschrittene Funktionen (z. B. simulierter Klick) benötigen die Bedienungshilfen-Dienstberechtigung, wodurch das Smartphone in den Einstellungen eine Dauermeldung anzeigt. Das ist die Sicherheitsarchitektur von Android und lässt sich nicht entfernen.
- <strong>Automatisierung nicht zu komplex machen</strong>: Beginne mit kleinen Abläufen aus 2–3 Aktionen. Starte nicht sofort mit einem 20-Schritte-Superablauf – beim Debugging wirst du sonst durchdrehen.

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Tipp: Die richtige Haltung zum Automatisierungs-Einstieg

{class="mt-1"}
Nimm dir fünf Minuten Zeit und überlege: Was sind die drei Dinge, die du am Smartphone am häufigsten wiederholst? Zum Beispiel die morgendliche Routine, die Gewohnheiten nach dem Verbinden der Bluetooth-Kopfhörer, die Einstellungen vor dem Verlassen des Hauses … Beginne mit diesen hochfrequenten Kleinigkeiten und baue jeweils eine einfache Automatisierung. Selbst wenn jede nur Sekunden spart: Über Tage und Monate summiert sich das. Und das Erfüllungsgefühl nach dem Bau macht wirklich süchtig.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Übung: Drei Einsteiger-Automatisierungs-Herausforderungen

{class="mt-1 mb-2"}
Wähle die für dich passende aus und führe sie durch – danach bist du eingestiegen:

{class="list-decimal pl-6 mt-1 space-y-1"}
1. <strong>Herausforderung 1: Guten-Morgen-Automatisierung</strong>: iOS: In der Kurzbefehle-App neuen Kurzbefehl anlegen → Aktionen "Aktuelles Wetter abrufen" → "Text vorlesen" → "App öffnen: NetEase Cloud Music" hinzufügen. Danach kannst du zu Siri "Guten Morgen" sagen, um auszulösen. Android: In Tasker neue Aufgabe anlegen → Aktionen "Wetter abrufen" → "Vorlesen" → "App öffnen" hinzufügen → Auslösezeit auf täglich 7:00 Uhr setzen.
2. <strong>Herausforderung 2: Automatischer Energiesparmodus bei niedrigem Akku</strong>: iOS: Reiter Automatisierung → Neu → "Akkustand" → unter 25 % → Aktionen "Energiesparmodus aktivieren" + "Helligkeit auf 25 %" hinzufügen. Android: Tasker → neues Profile → Zustand → Stromversorgung → Akku &lt; 25 % → Aufgabe "Energiesparmodus an" + "Helligkeit senken".
3. <strong>Herausforderung 3: Bei Verbindung mit Auto-Bluetooth automatisch navigieren</strong>: iOS: Automatisierung → Neu → "Bluetooth" → dein Auto-Bluetooth auswählen → Aktion "App öffnen: Gaode Maps" + "Medienlautstärke auf 80 %" hinzufügen. Android: Tasker → Profile → Zustand → Bluetooth verbunden → Auto-Bluetooth auswählen → Aufgabe "Gaode öffnen" + "Medienlautstärke erhöhen".
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Fallbeispiel 3: Automatisierter „Guten-Morgen-Ablauf"

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>Szenario</strong>: Taeglich um 7:00 Uhr automatisch Wetteransage + Stummschaltung deaktivieren + Nachrichten oeffnen.
- <strong>Schritte</strong>: iOS: Kurzbefehle → Automatisierung → Zeit-Trigger → „Wetter abrufen" + „Lautstaerke einstellen" + „App oeffnen" hinzufuegen; Android: MacroDroid → Ausloeser (Zeit 7:00) → Aktionen (Medienlautstaerke / URL oeffnen / TTS-Wettervorlesung).
- <strong>Erwartetes Ergebnis</strong>: Ohne Installation realisierbar – senkt die Einstiegshuerde.
:::
