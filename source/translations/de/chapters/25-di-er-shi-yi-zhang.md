---
id: di-er-shi-yi-zhang
num: 21
part: chao-yue-pian
nav: Kapitel 21: Mobilfunk und Informationssicherheit vertieft
toc: default
kind: chapter
---

### Kapitel 21: Mobilfunk und Informationssicherheit vertieft

{class="chapter-intro mb-4"}
Wir nutzen täglich das Smartphone zum Surfen, Bezahlen, Chatten – das fühlt sich sehr bequem an. Aber hast du schon einmal darüber nachgedacht, ob deine Chatverläufe, Zahlungspasswörter und Fotos im Netz „nackt" herumlaufen? Ehrlich: Die meisten denken nie darüber nach, aber wenn etwas passiert – Account gehackt, Bankkarte leergeräumt – ist es zu spät für Reue. In diesem Kapitel besprechen wir, wie du dein digitales Leben weniger „transparent" machst.

#### I. VPN: Der „Tarnumhang" im Netz

VPN (Virtual Private Network) – stell dir vor, zwischen deinem Zuhause und der Zielwebsite wird ein exklusiver, verschlüsselter Tunnel gebaut. Du gehst im Tunnel hin und her, und von außen kann niemand sehen, was du in der Hand hältst oder wohin du willst.

- <strong>Normales Surfen</strong>: Dein Smartphone → öffentliches Netzwerk → Zielwebsite. Die Router und Switches dazwischen – an jedem Punkt kann jemand deine Daten „mitlesen". Besonders in Cafés oder am Flughafen, bei öffentlichem Wi-Fi, ist man im Grunde „nackt".
- <strong>Mit VPN</strong>: Dein Smartphone → VPN-Verschlüsselungstunnel → VPN-Server → Zielwebsite. Die Daten sind verschlüsselt verpackt – „Schnüffler" sehen nur einen Haufen Zeichensalat. Außerdem sieht die Zielwebsite die IP-Adresse des VPN-Servers, nicht deine echte IP.

Was kann ein VPN also? Kurz gesagt: Erstens,<strong>deine Privatsphäre im öffentlichen WLAN schützen</strong>; zweitens,<strong>geografische Beschränkungen umgehen</strong>(z. B. Inhalte ansehen, die nur in bestimmten Ländern verfügbar sind); drittens,<strong>verhindern, dass dein Internetanbieter (ISP) dein Surfverhalten protokolliert</strong>. Aber eine Warnung:<strong>Niemals kostenlose VPNs benutzen!</strong> Gratis bedeutet oft, dass deine Daten die „Waren“ sind. Ein Bekannter nutzte ein Gratis-VPN – plötzlich poppte Werbung auf dem Handy auf, und heraus kam: Das VPN verkaufte seine Surfdaten an Werbetreibende. Wähle also entweder ein kostenpflichtiges Marken-VPN (wie NordVPN, ExpressVPN) oder gar keines.

Außerdem ist ein VPN kein Allheilmittel. Es schützt nur die Daten „auf dem Transportweg" – wenn die Zielwebsite selbst unsicher ist oder auf deinem Smartphone bereits Malware installiert ist, kann dir auch ein VPN nicht helfen.

#### II. Öffentliches Wi-Fi – die „süße Falle", gefährlicher als du denkst

Du denkst vielleicht, kostenloses Wi-Fi sei doch harmlos? Eine wahre Geschichte: Sicherheitsforscher stellten am Flughafen einen Hotspot namens „Starbucks_Free" auf – innerhalb einer Stunde verbanden sich über hundert Personen. Tatsächlich war der Hotspot von den Forschern selbst eingerichtet, und der gesamte <strong>unverschlüsselte Datenverkehr</strong>– z. B. HTTP-Webseiten, App-Kommunikation ohne TLS – konnte tatsächlich mitgelesen und eingesehen werden.

Aber eine wichtige Voraussetzung: Heute nutzen WeChat, Online-Banking und Alipay fast ausschließlich HTTPS-Verschlüsselung. Ein Angreifer, der das Datenpaket abfängt, sieht nur Zeichensalat und <strong>kann Chat-Inhalte oder Zahlungspasswörter nicht direkt auslesen</strong>. Er weiß aber dennoch, welche Websites du besucht hast (Domainnamen). Wenn bestimmte veraltete Apps oder Webseiten noch HTTP-Klartext verwenden, ist der Inhalt vollständig sichtbar. Diese Art Angriff heißt „Man-in-the-Middle-Angriff" (MitM) – der Angreifer schaltet sich zwischen dich und den echten Wi-Fi-Router. Schlimmer noch: Viele Smartphones haben „automatisch mit bekanntem Wi-Fi verbinden" aktiviert – ein Angreifer muss seinem Hotspot nur den Namen eines Wi-Fi geben, das du früher einmal genutzt hast (z. B. „ChinaNet" oder „CMCC"), und dein Smartphone verbindet sich automatisch.

Wie schützt man sich? Ein paar praktische Tipps:

- <strong>Auf HTTPS achten</strong>: Die Adressleiste beginnt mit https:// – das zusätzliche „s" steht für „Secure". Wenn du eine Website besuchst, die ein Passwort verlangt, und http:// (ohne s) siehst – sofort aufhören, nichts eingeben! Moderne Browser zeigen bei Nicht-HTTPS-Seiten eine „Nicht sicher"-Warnung – sobald du das siehst, sei wachsam.
- <strong>„Automatisch verbinden" abschalten</strong>: Egal ob iPhone oder Android – in den Wi-Fi-Einstellungen „Automatisch beitreten" / „Automatisch verbinden" deaktivieren. Lieber jedes Mal manuell antippen, als das Smartphone selbst entscheiden lassen.
- <strong>Sensible Operationen über mobile Daten</strong>: Überweisungen, Online-Banking-Login, Ausweisnummer eingeben – diese Operationen besser über das eigene 4G/5G-Mobile-Netz machen, nicht die paar Megabyte sparen.
- <strong>Ungenutzte Wi-Fi-Netzwerke vergessen</strong>: Nach Geschäftsreise oder Urlaub die temporär genutzten Hotel- und Flughafen-Wi-Fis „vergessen" – so verbindet sich das Smartphone beim nächsten Mal nicht automatisch mit einem gleichnamigen Fake-Hotspot.

#### III. Wie HTTPS dich schützt – der SSL/TLS-Handshake

Wir haben gerade HTTPS erwähnt – wie funktioniert es eigentlich? Jedes Mal, wenn du eine HTTPS-Website besuchst, führen Browser und Server einen „SSL/TLS-Handshake" durch – etwa so:

1. Dein Browser sagt: „Hey, Server, ich möchte sicher mit dir kommunizieren – das ist meine Liste der Verschlüsselungsfähigkeiten (unterstützte Algorithmen usw.)."
2. Der Server antwortet: „Okay, ich habe aus deiner Liste dieses Verschlüsselungsschema gewählt. Hier ist mein digitales Zertifikat mit meinem öffentlichen Schlüssel, signiert von der CA-Stelle Soundso."
3. Der Browser prüft das Zertifikat: Wurde es von einer vertrauenswürdigen CA ausgestellt? Ist es abgelaufen? Stimmt der Domainname?
4. Nach erfolgreicher Prüfung einigen sich beide Seiten über den öffentlichen Schlüssel auf einen „Sitzungsschlüssel" – die gesamte folgende Kommunikation wird mit diesem Schlüssel verschlüsselt.

Das ist wie bei einem Bankbesuch: Du reichst deinen Ausweis (Zertifikat) über den Tresen, der Kassierer prüft deine Identität, dann vereinbart ihr ein Codewort, und das weitere Gespräch versteht nur ihr beide. Selbst wenn jemand mithört, hört er nur verschlüsselten Zeichensalat.

Aber Vorsicht: HTTPS garantiert nur, dass der „Übertragungsweg" verschlüsselt ist – es garantiert nicht, dass die Zielwebsite gut ist. Phishing-Websites können ebenfalls HTTPS verwenden – das kleine Schloss-Symbol bedeutet nur, dass du „mit einer Website" verbunden bist, nicht, dass es die Website ist, die du besuchen willst. Also selbst prüfen, ob die URL korrekt ist.

#### IV. DNS-Sicherheit: Ist dein „Netz-Telefonbuch" sicher?

DNS (Domain Name System) ist wie das Telefonbuch des Internets: Du gibst „baidu.com" ein, DNS ermittelt die zugehörige IP-Adresse (z. B. 10.242.68.66), und erst dann kann der Browser sich verbinden. Das Problem: Traditionelle DNS-Anfragen sind <strong>Klartext</strong>–<strong>nicht verschlüsselt</strong>! Das heißt, dein ISP, der Wi-Fi-Anbieter oder jeder Zwischenknoten kann sehen, welche Websites du besucht hast.

Noch übler ist „DNS-Hijacking": Ein Angreifer manipuliert den DNS-Prozess und leitet „baidu.com" auf eine gefälschte Phishing-Website um. Du hast die richtige URL eingegeben, landest aber auf einer identisch aussehenden, aber falschen Login-Seite – Account und Passwort eingegeben, und das war's.

Zum Glück gibt es inzwischen verschlüsselte DNS-Lösungen:

- <strong>DNS über HTTPS (DoH)</strong>: Versteckt DNS-Anfragen im HTTPS-Datenverkehr, gemischt unter normales Web-Surfen – man kann nicht mehr erkennen, welche Anfragen DNS sind.
- <strong>DNS über TLS (DoT)</strong>: Nutzt das TLS-Verschlüsselungsprotokoll speziell für DNS-Anfragen, eigener Port – der Netzwerkadministrator sieht, dass du DoT nutzt, aber nicht den Inhalt.

Ich persönlich empfehle Cloudflare (1.1.1.1) oder Google (8.8.8.8) als DNS-Server – beide unterstützen verschlüsseltes DNS. Unter Android in den Einstellungen für „Privates DNS" einfach „one.one.one.one" oder „dns.google" eintragen – super einfach. Beim iPhone ist es etwas umständlicher: ein Profil installieren oder über eine App einrichten – aber es lohnt sich.

#### V. Ist „Privat surfen" wirklich unsichtbar?

Zuerst die Antwort:<strong>Der Inkognito-Modus ist euer Vorhang zu Hause, kein Tarnumhang.</strong>

Was er tut: Er hinterlässt lokal keine Spuren – nachdem du das Inkognito-Fenster schließt, speichert der Browser keine Surf-Historie, Cookies, Formulareingaben oder Suchanfragen. Wenn du am Computer eines anderen etwas nachschlagen oder ein Geschenk kaufen willst, ohne dass die Familie es in der History findet, ist der Inkognito-Modus geeignet.

Was er nicht kann:

- Die Website, die du besuchst,<strong>seht trotzdem, dass du da warst</strong>– deine IP-Adresse, Geräteinformationen und das Surfverhalten sind auf der Website-Seite völlig klar.
- Dein Internetanbieter <strong>seht trotzdem, welche Websites du besucht hast</strong>– nur den Inhalt sieht er nicht (bei HTTPS).
- Der Netzwerkadministrator von Firma/Schule <strong>kann dein Surfverhalten ebenfalls überwachen</strong>.
- Dateien, die du herunterlädst, und Lesezeichen, die du hinzufügst,<strong>bleiben erhalten</strong>– und verschwinden nicht beim Schließen des Fensters.

Also merken: Der Inkognito-Modus ist „lokales Löschen", kein „Netz-Tarnumhang". Wenn du deine Surfspuren wirklich verbergen willst, brauchst du eine Kombination wie VPN + Tor-Browser. Für den Alltag reicht es aber, das hier zu wissen.

#### VI. Browser-Datenschutz: Lass deinen Browser dich nicht verkaufen

Vielleicht merkst du es gar nicht, aber der Browser selbst ist eine riesige Datensammelstelle – Cookies, Surf-Historie, Cache, Auto-Ausfüllen, Standortberechtigungen – jedes einzelne kann deine Privatsphäre verraten. Ein paar Empfehlungen:

- <strong>Regelmäßig Browserdaten löschen</strong>: Alle paar Wochen in den Einstellungen Cookies, Cache und Historie aufräumen. Nicht um „verfolgt werden" zu verhindern – das klappt mit dem Löschen von Cookies kaum noch – sondern um zu verhindern, dass das Smartphone immer langsamer wird. Der Browser-Cache kann mehrere Gigabyte belegen.
- <strong>Die Illusion „Do Not Track" abschalten</strong>: Die Option „Do Not Track-Anfrage senden" im Browser bittet die Website im Grunde, dich nicht zu verfolgen – ob sie hört, ist eine andere Sache, die meisten Websites ignorieren es. Erwarte nichts davon.
- <strong>Datenschutzorientierte Browser nutzen</strong>: Firefox Focus, DuckDuckGo Browser oder Brave blockieren standardmäßig Tracker und Werbung – deutlich sauberer als die Standardeinstellungen von Chrome und Safari.
- <strong>Auch die Suchmaschine zählt</strong>: DuckDuckGo statt Baidu/Google verwenden – sie zeichnet keine Suchhistorie auf und erstellt kein Nutzerprofil. Die Suchergebnisse sind ehrlich gesagt nicht so präzise wie bei Google, aber für alltägliche Recherchen reicht es.
- <strong>App-Berechtigungen prüfen</strong>: In den Smartphone-Einstellungen prüfen, welche Berechtigungen dein Browser hat – braucht er wirklich Standort, Mikrofon, Kontakte? Wahrscheinlich nicht.

#### VII. Praktische Sicherheits-Checkliste: Schütze dich ab jetzt

Nach all dem Reden hier eine einfach-brisante Sicherheits-Checkliste – eine halbe Stunde investieren, und deine Smartphone-Sicherheit macht einen Quantensprung:

1. <strong>WLAN-Autoverbindung deaktivieren</strong>: iPhone unter Einstellungen → WLAN, Android in den Wi-Fi-Einstellungen.
2. <strong>Verschlüsseltes DNS einrichten</strong>: Android direkt „Privates DNS" auf „dns.google" setzen, iPhone per App oder Profil 1.1.1.1 DoH einrichten.
3. <strong>Zwei-Faktor-Authentifizierung (2FA) aktivieren</strong>: WeChat, Alipay, Apple ID, Google-Account – überall, wo 2FA möglich ist, aktivieren. SMS-Codes sind die niedrigste 2FA-Stufe; besser ist TOTP (z. B. Google Authenticator, Microsoft Authenticator).
4. <strong>App-Berechtigungen einmal durchgehen</strong>: Jede App auf Berechtigungen prüfen – besonders Standort, Kontakte, SMS, Mikrofon, Kamera. Du wirst feststellen, dass manche Taschenlampen-Apps deine Kontakte wollen – sofort deinstallieren.
5. <strong>Browserdaten regelmäßig löschen</strong>: Eine Kalender-Erinnerung einstellen – einmal pro Monat Cache und Cookies leeren.
6. <strong>Keine Datenkabel von öffentlichen Ladesäulen verwenden</strong>: USB-Anschlüsse können sowohl laden als auch Daten übertragen – bösartige Ladesäulen („Juice Jacking") können beim Laden Daten stehlen. Eigene Ladegeräte und Kabel mitnehmen.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Jetzt machen: Führe einen „Sicherheits-Check" deines Smartphones durch

{class="list-decimal pl-6 mt-1 space-y-1"}
1. <strong>DNS-Upgrade</strong>: Android: Einstellungen → Verbindungen &amp; Teilen → Privates DNS → „one.one.one.one" oder „dns.google" eintragen. iPhone: In Safari „1.1.1.1 DNS profile" suchen, Profil installieren oder die Cloudflare-1.1.1.1-App herunterladen.
2. <strong>Wi-Fi-Audit</strong>: Wi-Fi-Liste öffnen und alle unbekannten, ungenutzten oder seltsam benannten Hotspots „vergessen".
3. <strong>Berechtigungs-Großreinemachen</strong>: Einstellungen → Datenschutz/Berechtigungsverwaltung, jede App auf Berechtigungen prüfen. Apps mit unangemessenen Berechtigungsanforderungen (z. B. Taschenrechner will Kontakte) markieren und deinstallieren oder ersetzen.
4. <strong>Account-Sicherheit prüfen</strong>: Apple-ID- oder Google-Account-Sicherheitsseite öffnen, prüfen, ob unbekannte Geräte eingeloggt sind, 2FA bestätigen und Wiederherstellungskontakte auf Vertrauenswürdigkeit prüfen.
:::
