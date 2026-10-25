---
id: di-san-shi-liu-zhang
num: 36
part: er-tong-pian
nav: Kapitel 36:Handy und Smart Home – das Zuhause cleverer machen
toc: default
kind: chapter
---

### Kapitel 36: Smartphone und Smart Home – das Zuhause wird clever

{class="chapter-intro mb-4"}
Das Smartphone übernimmt eine immer wichtigere Rolle: die Fernbedienung für das ganze Haus. Von Lampe und Steckdose bis zur Türschloss-Sperre wird Smart Home vom „Spielzeug für Nerds“ zur „Haushaltsausstattung“. Dieses Kapitel ordnet Protokolle, Ökosysteme, Zentraleinheiten und Einsteiger-Sets und schließt mit einer Sicherheitsliste ab, damit Sie nicht selbst zum Opfer der „Intelligenz“ werden.

#### 1. Smart-Home-Protokolle: Die Wahl zählt

Vor dem Kauf prüfen, welches Protokoll ein Gerät unterstützt – davon hängt ab, ob Handy und Ökosystem es „verstehen“. Vier gängige Standards im Überblick:

- Matter: 2022 von der CSA (Connectivity Standards Alliance) veröffentlicht, getragen von Apple, Google, Amazon, Samsung u. a. Ziel: Alle Marken sollen dieselbe Sprache sprechen. 2023–2026 wird Matter schnell zum einheitlichen Standard; unterstützte Geräte lassen sich an Apple HomeKit, Google Home, Amazon Alexa und Mi Home anbinden – kein Lock-in mehr.
- Thread: Die Netzwerk-„Röhre“ unter Matter. Energiesparend, selbstorganisierend (fällt ein Knoten aus, sucht sich das Signal einen Weg), schnell und stabil. Geräte mit Thread-Borderrouter (z. B. HomePod mini, Apple TV 4K, Xiaomi Hub) laufen deutlich zuverlässiger.
- WLAN: Viel Bandbreite, direkte Router-Anbindung, aber höherer Verbrauch; bei vielen Geräten kann der Kanal überfüllt werden. Gut für Kameras, Saugroboter und andere Datenfresser.
- Bluetooth (BLE): Einrichtung einfach, sparsam, aber kurze Reichweite und kein selbstorganisierendes Netz. Gut für Schlösser, Temperatur-/Feuchtesensoren und kleine Datenpakete.
- Zigbee: Bewährtes, sparsames Mesh-Protokoll, braucht einen eigenen Gateway. Geräte günstig und stabil, aber schwache herstellerübergreifende Kompatibilität. Wird zunehmend von Matter+Thread abgelöst.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
Faustregel

{class="mt-1"}
Beim Kauf 2026 zuerst auf „Matter over Thread“ achten – derzeit die zukunftssicherste Wahl. Ältere WLAN-/Bluetooth-Geräte nicht vorschnell aussortieren; bei Neuanschaffungen dann auf Matter umsteigen.
:::

#### 2. Die drei großen Ökosysteme im Vergleich

Protokoll ist die „Sprache“, das Ökosystem der „Kreis“. Selbst mit Matter wählen Sie im Alltag ein Hauptsystem für Automatisierung und Sprachsteuerung. Die drei wichtigsten im Überblick:

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                    <thead>
                        <tr class="bg-light dark:bg-gray-700">
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ökosystem</th>
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Stärken</th>
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Schwächen</th>
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Zielgruppe</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple HomeKit</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stärkster Datenschutz (überwiegend lokal), nahtlose Kopplung mit iPhone/Siri/Kurzbefehlen</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Weniger und teurere Geräte, HomePod oder Apple TV als Hub nötig</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple-Haushalte, die Privatsphäre und Erlebnis schätzen</td>
                        </tr>
                        <tr>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mi Home (Xiaomi)</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Größte Gerätevielfalt, bestes Preis-Leistungs-Verhältnis, Xiaoai stark</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Relativ geschlossenes Ökosystem, viel Cloud, etwas mehr Werbung</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Einsteiger mit knappem Budget, die das ganze Haus ausstatten wollen</td>
                        </tr>
                        <tr>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Huawei HiLink (HarmonyOS)</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nahtloser Übergang mit HarmonyOS-Handy/Tablet/Uhr, Gerätezahl wächst schnell</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Im Ausland weniger Geräte, Ökosystem holt auf</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Huawei-Nutzer, die „Super Device“-Zusammenarbeit schätzen</td>
                        </tr>
                    </tbody>
                </table>
```

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
Auswahlhilfe

{class="mt-1"}
Ökosystem nach dem Handy wählen: iPhone → HomeKit, Huawei → HiLink, andere Android-Geräte → Mi Home am unkompliziertesten. Über Matter lassen sich Geräte verschiedener Ökosysteme mit demselben Handy steuern – kein einmaliges „Lager wählen“ nötig.
:::

#### 3. Das Smartphone als Hauszentrale

In vielen Einsteiger-Szenarien ist das Smartphone die „Hauszentrale“: App steuert Licht, Klima, Jalousien und Sicherheit und legt Automatisierungen an, damit das Haus „von selbst läuft“:

- Gerätesteuerung: In HomeKit/Mi Home/Smart Life Licht an/aus, Farbtemperatur, Klima-Temperatur, Jalousien, Kameras – lokal oder remote.
- Automatisierungen: „Bedingung → Aktion“. Drei Klassiker: Zuhause-Modus: Standort Zuhause + dunkel → Flurlicht + Klima + Jalousien + Schloss zu.
- Abwesenheits-Modus: Letzte Person geht (Standort weg oder Schloss verriegelt) → Licht aus + Klima aus + Steckdosen aus + Kamera an + Alarmanlage scharf.
- Schlaf-Modus: Jeden Abend 23:00 → Hauplichter aus + Jalousien zu + Klima 26 °C + Nachtlicht an.

- NFC-Tipp: NFC-Tag an die Tür, Handy dranhängen löst Szenen aus (Türöffner-Licht, nochmal tippen für Schlaf). iPhone über „Kurzbefehle“, Android über „Wallet“ oder Hersteller-App beschreibbar.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Ausprobieren: „Zuhause-Modus“ bauen

{class="mt-1"}
In der Smart-Home-App unter „Automatisierungen“ neu anlegen: Auslöser „Ankunft an Ort“ (Zuhause), Aktionen „Flurlicht an“, „Klima 26 °C“, „Jalousien zu“. Speichern, kurz rausgehen und beim Heimkommen prüfen, ob das Licht von selbst angeht – das erste gelungene Szenario macht oft mehr Freude als ein neues Gerät.
:::

#### 4. Einsteiger-Starter-Set

Nicht alles auf einmal: Mit diesen vier Teilen decken Sie 80 % des Alltags ab:

- Smart Speaker: Xiaoai (Mi Home, günstig) / HomePod mini (Apple, zugleich Thread-Hub) / Alexa (im Ausland breit). Wichtig: Der Speaker bestimmt die Sprachwelt – erst Ökosystem, dann Speaker.
- Smart Bulb: Yeelight (Mi Home/Matter, Farbtemperatur/Helligkeit, günstig) / Philips Hue (gute Farben, stabil, braucht Hue-Bridge, teurer). Vor dem Kauf Fassung (E27/B22) und Farbwahl prüfen.
- Smart Plug: Xiaomi Smart Plug (günstig, Verbrauchsanzeige) / TP-Link Kasa (im Ausland gute Matter-Unterstützung). Bei starken Verbrauchern (Durchlauferhitzer, Heizung) Nennleistung beachten, nicht überlasten.
- Smartes Türschloss: Lockin/Xiaomi (Preis-Leistung, Mi-Home-Kopplung) / Kaadas (traditioneller Schlosshersteller, solide Mechanik). Matter-/Ökosystem-Unterstützung, Akkulaufzeit und Notfallschlüssel-Position prüfen.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
Reihenfolge beim Kauf

{class="mt-1"}
Zuerst Smart Speaker (Ökosystem festlegen) → dann Birne und Steckdose (niedrige Einstiegshürde, sofort spürbar) → zuletzt Schloss und Kamera (Sicherheitsrelevant, sorgfältig wählen). Immer nur eine Geräteklasse ergänzen und erst vertraut werden, bevor Sie ausbauen.
:::

#### 5. Sicherheitsregeln

Je mehr smarte Geräte, desto größer die Angriffsfläche. Diese vier Mindestregeln bitte durchgehen:

1. Standardpasswörter ändern: Werks-Passwörter von Kameras, Routern und Schlössern sind öffentlich bekannt. Sofort in lange, einzigartige Passwörter ändern.
2. Firmware aktuell halten: Hersteller-Updates schließen Sicherheitslücken. „Automatisch aktualisieren“ einschalten oder mindestens monatlich manuell prüfen.
3. Netzwerk trennen: IoT-Geräte in ein eigenes WLAN (oder Gastnetzwerk) legen, getrennt von Handy und PC. Fällt ein Gerät aus, bleibt der Zugriff auf wichtige Daten erschwert.
4. Privatsphäre: Bei Kameras „Privatzonen“ maskieren (Schlafzimmer, Bad nicht filmen), 24-Stunden-Cloud-Aufzeichnung abschalten; Kamerabilder nicht dauerhaft an Drittanbieter-Apps freigeben.

::: div .danger-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
Diese Fallstricke vermeiden

{class="list-disc pl-6 mt-1 space-y-1"}
- Fernentriegelung des Schlosses nicht für Fremde nutzen – besser temporäre Codes, die nach Gebrauch verfallen.
- Kamera nicht aufs Bett oder aus dem Fenster richten – so schützen Sie Ihre eigene Privatsphäre.
- Keine No-Name-Geräte ohne Marke kaufen – ohne Firmware-Updates ist das wie eine Hintertür im Haus.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Kapitel-Zusammenfassung

{class="list-disc pl-5 text-sm space-y-0.5"}
- Matter+Thread ist 2023–2026 die gemeinsame Richtung – beim Neukauf auf das Siegel achten
- Die drei Ökosysteme haben ihre Stärken: Apple = Datenschutz/Erfahrung, Mi Home = Preis-Leistung, Huawei = Mehrgeräte-Kopplung
- Smartphone als Zentrale: „Zuhause/Abwesend/Schlaf“ aufsetzen – das Haus läuft von selbst
- Einsteiger-Vierer: Speaker, Birne, Steckdose, Schloss – in dieser Reihenfolge erweitern
- Standardpasswörter, Firmware, Netzseparation, Privatsphären-Maskierung – diese vier Sicherheitsregeln nicht weglassen
:::
