---
id: di-er-shi-zhang-termux
part: jin-jie-pian
nav:  Kapitel 20 Anhang
toc: sub
kind: supplement
---

### Kapitel 20 Anhang: Termux – eine tragbare Linux-Terminal-Umgebung auf Android-Geräten

{class="chapter-intro mb-4"}
Wenn dir der Entwicklermodus noch nicht „hardcore“ genug ist und du die komplette Linux-Kommandozeile auf dem Handy erleben willst, ist Termux genau das Richtige für dich.

#### I. Was ist Termux?

Termux ist eine Open-Source-Terminal-Emulation und Linux-Umgebungs-App, die speziell für Android-Geräte entwickelt wurde – ganz ohne Root-Rechte bringt sie eine Linux-Kommandozeile aufs Handy. Als leichte App (das Installationspaket ist nur etwa 30 MB groß) bietet Termux über APT tausende Pakete und bringt dir die vollständige Linux-Erfahrung aufs Handy.

Termux punktet vor allem durch Leichtgewichtigkeit und hohe Erweiterbarkeit: entwickelt, gelernt und administriert wird damit vielerlei. Standardpakete und präzise Terminalwerkzeuge machen daraus eine Open-Source-Lösung.

#### II. Kernfunktionen und Merkmale

##### 🖥️ Vollständige Linux-Umgebung

Termux <strong>Nur Bash integriert</strong> als Shell. Wenn du Zsh, fish oder andere Shells verwenden moechtest, musst du sie manuell ueber den Paketmanager installieren, z. B.:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install zsh</code> oder<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install fish</code>. Zudem unterstuetzt Termux Editoren wie Vim, Nano und Emacs und bietet ein nahezu originales Kommandozeilenerlebnis. Ueber „pkg install" lassen sich ueber 2000 Pakete installieren, darunter GCC, OpenSSH, SQLMap und weitere Entwicklungs- und Sicherheitstools.

##### 📦 Leistungsstarkes Paketmanagement

Mit dem APT-Paketmanager (ähnlich wie Debian und Ubuntu) lassen sich tausende Linux-Pakete installieren: Entwicklungs- und Netzwerkwerkzeuge und Umgebungen für Python, Ruby, Node.js, Go, Rust, Swift und mehr.

##### 🔒 Sicherheit und Netzwerkfunktionen

- <strong>SSH-Fernverbindung</strong>: Unterstützt SSH-Client- und -Server-Funktionen, kann andere Geräte remote verbinden oder das Smartphone zum SSH-Host machen.
- <strong>Verschlüsselungswerkzeuge</strong>: Bietet Verschlüsselungstools wie OpenSSL für verschlüsselte Daten und sichere Kommunikation.
- <strong>Server-Aufbau</strong>: Kann Nginx oder Apache konfigurieren, um einen statischen Webserver aufzusetzen.

##### 🔧 Systemintegration und Erweiterung

- Zugriff auf Smartphone-Speicherberechtigungen für lokale Dateiverwaltung.
- Aufruf von Sensoren, Kameras und anderen Android-Hardware-Funktionen über das Termux:API-Plugin.
- Unterstützt Bluetooth-Tastaturen und externe Bildschirme, mit voller Mausunterstützung.

#### III. Plugin-Ökosystem

Die Kern-App von Termux lässt sich über mehrere optionale Plugin-Apps erweitern – für Zusatzfunktionen und Integration:

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Plugin-Name</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Funktionsbeschreibung</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:API</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Macht Android-API-Funktionen für Kommandozeilen-Programme verfügbar.</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Boot</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Erlaubt das Ausführen von Skripten beim Gerätestart.</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Float</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bietet ein schwebendes Terminal-Fenster.</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Styling</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Aktiviert Farbschemata und Schriftart-Anpassung für das Terminal.</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Tasker</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Integriert Termux-Skripte in die Tasker-Automatisierungs-App.</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Widget</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Erlaubt das Ausführen von Skripten über ein Home-Screen-Widget.</td>
                            </tr>
                        </tbody>
                    </table>
```

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Wichtiger Hinweis

{class="mt-1"}
Termux und seine Plugins müssen aus derselben Quelle installiert werden, da sie dieselbe sharedUserId teilen. Eine Mischung aus verschiedenen Quellen (wie F-Droid und GitHub) führt zu Installationsfehlern.
:::

#### IV. Installations- und Konfigurationsleitfaden

##### 📥 Installationsschritte

1. <strong>App herunterladen</strong>: Termux aus offiziellen Quellen (F-Droid oder GitHub) herunterladen und installieren – keine Root-Rechte erforderlich.
2. <strong>System initialisieren</strong>: Nach dem ersten Start warten, bis „Installing bootstrap packages" abgeschlossen ist.
3. <strong>Speicherberechtigung abrufen</strong>:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-setup-storage</code> ausführen, um Zugriff auf das Smartphone-Dateisystem zu erhalten.
4. <strong>Softwarepakete aktualisieren</strong>:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code> ausführen, um die Paketliste zu aktualisieren.

##### ⚙️ Grundlegende Optimierung

- <strong>Spiegel-Wechsel</strong>: Mit dem Befehl<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-change-repo</code>über eine grafische Oberfläche den Spiegel wechseln (empfohlen: Tsinghua-Universitätsspiegel).
- <strong>Tastenkombinationen</strong>: Leiser-Taste simuliert Strg, Lauter-Taste simuliert Esc – erhöht die Eingabeeffizienz.
- <strong>Oberfläche verschönern</strong>: Installiere Zsh + Oh My Zsh und konfiguriere Themes und Plugins.

#### V. Typische Anwendungsszenarien

##### 💻 Mobile Entwicklung &amp; Tests

Auf dem Smartphone eine vollständige Entwicklungsumgebung aufbauen, Python-Skripte schreiben und ausführen, C-Programme mit GCC kompilieren, Code-Repositories über Git verwalten und per SSH mit Remote-Servern synchronisieren.

##### 🖥️ Server-Administration

Verwalte Server per SSH aus der Ferne – führe Systemwartungen und Log-Analysen durch und kümmere dich von überall um Server-Probleme.

##### 📚 Linux-Operationen lernen

Bietet eine echte Linux-Umgebung und ist die ideale Plattform zum Erlernen der Kommandozeile und Systemadministration. Man kann Shell-Skripte schreiben und Linux-Dateiberechtigungen ueben (z. B. <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chmod 755</code> setzt die Berechtigungsbits rwxr-xr-x,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chown user:group</code> aendert den Dateieigentuemer,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls -l</code> zeigt die drei Gruppen mit je neun Berechtigungsbits fuer owner/group/other). Beachte: Dies ist das klassische Unix/Linux-Drei-Gruppen-Neun-Bit-Berechtigungsmodell (owner / group / other × Lesen / Schreiben / Ausfuehren), das ein voellig anderes System darstellt als die ACL-Zugriffssteuerungslisten von Windows NTFS.

##### 🔐 Netzwerksicherheitstests

Nmap, SQLMap, Hydra, Metasploit und andere Sicherheits-Tools installieren, Netzwerk-Scans und Penetrationstests durchführen.

#### VI. Version und Kompatibilität

Die aktuell stabile Version von Termux ist v0.118.2, geeignet für Geräte mit Android ≥ 7. Hinweis: Auf Android 12 und höher kann Termux instabil sein – am besten die offiziellen Update-Logs für die neuesten Kompatibilitätsinformationen verfolgen.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Zusammenfassung

{class="mt-1"}
Termux bringt das mächtige Linux-Terminal-Erlebnis auf Android-Geräte und macht das Smartphone zu einem portablen Entwicklungs- und Lernwerkzeug. Egal ob Entwickler, Systemadministrator oder Technik-Enthusiast – mit Termux kann man auf dem Mobilgerät ein vollständiges Kommandozeilenerlebnis genießen und die Idee „Linux in der Tasche" verwirklichen.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Hand an: Führe auf dem Smartphone deinen ersten Linux-Befehl aus

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Lade Termux von F-Droid herunter und installiere es; warte beim ersten Start auf den Abschluss der Initialisierung.
2. Führe<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code> aus, um die Softwarepakete zu aktualisieren.
3. Installiere Python:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install python</code>.
4. Gib<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python3 -c "print('Hello from Termux!')"</code> Dieser Teil führt dich in eine tiefere digitale Welt ein – von Informationssicherheit über KI-Prinzipien bis hin zu Programmierdenken und digitalem Erbe. Diese Inhalte helfen dir, ein echter digitaler Bürger zu werden.
:::
