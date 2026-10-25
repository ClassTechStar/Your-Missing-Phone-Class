---
id: di-si-shi-er-zhang
num: 42
part: ai-biancheng-pian
nav: Kapitel 42: Große Modelle im Überblick und API-Praxis
toc: default
kind: chapter
---

### Kapitel 42: Das Panorama der großen Modelle und die API in der Praxis

{class="chapter-intro mb-4"}
Die letzten Kapitel haben sich damit beschäftigt, wie du mit der KI zusammenarbeitest. Dieses Kapitel beantwortet eine noch grundlegendere Frage: „Welche KI? Und wie benutze ich sie?“ Das große Modell-Panorama vom August 2026 ist ungeheuer vielfältig – international liefern sich GPT, Claude und Gemini ein Dreikampf, in China blühen DeepSeek, Tongyi Qianwen, GLM, Kimi und Doubao nebeneinander auf. Jedes Modell hat seinen eigenen Charakter und seine Stärken: Die richtige Wahl halbiert deine Mühe, die falsche verdoppelt sie. Dieses Kapitel stellt dir diese Modelle nicht nur vor, sondern zeigt dir auch, wie du sie über eine API in deine eigenen Apps einbindest und wie du passend zu deinem Bedarf den richtigen Token-Plan (Nutzungspaket) wählst.

#### 1. Die internationalen Leitmodelle: drei starke Anbieter

Auf dem internationalen Markt der großen Modelle haben sich im August 2026 drei starke Anbieter etabliert: OpenAI (GPT-Serie), Anthropic (Claude-Serie) und Google (Gemini-Serie). Jeder hat einen deutlich eigenen Charakter – lass uns sie einen nach dem anderen kennenlernen.

##### 1. Die OpenAI-GPT-5.6-Serie: der rundum ausbalancierte Allrounder

OpenAI hat die Welle der großen Modelle ausgelöst, und die GPT-Serie ist bis heute das weltweit am häufigsten genutzte Modell. Die im Juli 2026 erschienene GPT-5.6-Serie folgt einer Drei-Stufen-Strategie: das Flaggschiff GPT-5.6 Sol für anspruchsvolle Inferenz, das ausgewogene GPT-5.6 Terra für die Alltagsentwicklung und das leichte GPT-5.6 Luna für Szenarien mit hohem Aufkommen und niedrigen Kosten. Alle drei Modelle teilen sich ein Kontextfenster von 1,05 Mio. Token und unterstützen Bildeingabe, Funktionsaufrufe und strukturierte Ausgaben.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Modell</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Positionierung</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Eingabe (/Mio. Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ausgabe (/Mio. Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kontextfenster</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Sol</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Flaggschiff-Inferenz</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">5,00 US$ (ca. 36 RMB)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">30,00 US$ (ca. 217 RMB)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1,05 Mio. Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Terra</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ausgewogen, Alltag</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2,50 US$ (ca. 18 RMB)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">15,00 US$ (ca. 109 RMB)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1,05 Mio. Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Luna</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">leicht, niedrige Kosten</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1,00 US$ (ca. 7 RMB)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6,00 US$ (ca. 44 RMB)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1,05 Mio. Token</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Preisliste der OpenAI-GPT-5.6-Serie (August 2026)

Die Kernstärke der GPT-Serie ist die Ausgewogenheit – Inferenz, Programmieren, Schreiben, Multimodalität: keine auffällige Schwäche. Dazu kommen OpenAIs riesiges Plugin-Ökosystem und Entwickler-Community; Dokumentation und Werkzeugkette sind am vollständigsten. Für Situationen, in denen du nicht weißt, was du wählen sollst, ist GPT die Standardantwort, die „blind gewählt“ nie falsch liegt. Die Schwächen: Der Zugriff von China aus erfordert spezielle Netzwerkwege, das Chinesische klingt gelegentlich nach „Übersetzerton“, und die API-Preise liegen im mittleren bis hohen Bereich.

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Gute Nachricht

{class="mt-1"}
OpenAI kündigte im August 2026 an, dass das Standardmodell für Gratisnutzer auf GPT-5.6 Luna angehoben wurde und unbegrenzte Text-Chats freigeschaltet sind. Das heißt: Die Grundfähigkeiten von GPT erlebst du ohne Kosten; zahlen musst du erst, wenn du stärkere Inferenz oder API-Aufrufe brauchst.
:::

##### 2. Die Anthropic-Claude-Serie: die Spitze beim Programmieren und bei der Sorgfalt

Wenn GPT der Allrounder ist, dann ist Claude beim Programmieren die „Messlatte“. Anthropics Claude-Serie führt beim SWE-bench (Software-Engineering-Benchmark) seit Langem mit klarem Abstand; Codequalität und die Fähigkeit, Projekte in Ingenieursqualität umzusetzen, sind Branchenspitze. Noch bemerkenswerter: Claude hat die niedrigste Halluzinationsrate (Wahrscheinlichkeit falscher Angaben) im gesamten Feld, nur etwa 1 % – dadurch eignet es sich besonders für präzisionskritische Bereiche wie Wissenschaft und Recht.

Claudes zweiter Trumpf ist der extrem lange Kontext: ein Kontextfenster von 1 Mio. Token, mit dem sich mehrhundertseitige Verträge oder ganze Codebasen in einem Zug „durchlesen“ lassen, ohne Details zu verlieren. Beim Code-Refactoring, bei der Analyse langer Dokumente und Ähnlichem ist das praktisch unersetzlich. Claude Code, das Terminal-KI-Coding-Tool, erreichte bis Mitte 2026 einen annualisierten Umsatz von 2,5 Milliarden US-Dollar – der deutlichste Beleg dafür, wie anerkannt Claudes Programmierfähigkeit ist.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Modell</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Positionierung</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Eingabe (/Mio. Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ausgabe (/Mio. Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kontextfenster</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Fable 5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Flaggschiff</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">10,00 US$ (ca. 72 RMB)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">50,00 US$ (ca. 362 RMB)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 Mio. Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Opus 4.8</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Profi-Modell</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">5,00 US$ (ca. 36 RMB)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">25,00 US$ (ca. 181 RMB)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 Mio. Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Sonnet 5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Preis-Leistungs-Modell</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2,00 US$ (ca. 14 RMB)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">10,00 US$ (ca. 72 RMB)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 Mio. Token</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Preisliste der Anthropic-Claude-Serie (August 2026; Sonnet 5 zum Aktionspreis)

Claudes Schwäche ist der Preis – Fable 5 hat mit 50 US$ pro Mio. Token den höchsten Ausgabepreis aller Modelle. Die Multimodal-Fähigkeiten (Bild- und Videoverständnis) sind ebenfalls relativ schwach. Für Einzelentwickler mit kleinem Budget ist Sonnet 5 in der Aktionsphase preislich äußerst attraktiv.

##### 3. Die Google-Gemini-Serie: der König der Multimodalität

Googles Gemini-Serie ist 2026 bis zur Version 3.1 Pro weiterentwickelt. Geminis größter Trumpf ist die native Multimodalität – präzises Auswerten von Text und Bildern, fehlerfreie OCR-Tabellenerkennung, effizientes Extrahieren von Videoframes, dazu tiefgehende Analyse von Audio und Video. Es ist fest mit dem Google-Ökosystem (Suche, Mail, Cloud-Dienste) verzahnt und glänzt bei Echtzeit-Informationssuche und übergreifendem Modalitäten-Verständnis. Gemini unterstützt zudem eine Eingabe von bis zu 2 Mio. Token Kontext – aktuell das größte Kontextfenster überhaupt.

Gemini positioniert sich als „erste Wahl für wissenschaftliche Inferenz und Multimodal-Szenarien“. Wenn dein Projekt viel Bildanalyse, Videoverständnis oder wissenschaftliche Berechnung umfasst, hat Gemini kaum Gegner. Beim reinen Text-Codegenerieren liegt es allerdings leicht hinter Claude, und seine chinesischen Formulierungen wirken nicht so natürlich wie die der chinesischen Modelle.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Vergleichspunkt</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GPT-5.6</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Claude Fable 5</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Gemini 3.1 Pro</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gesamtwertung</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">94.8</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">95.0</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">92.1</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Programmierfähigkeit (SWE-bench)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">74.9%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">64.3% (Pro)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mittel</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kontextfenster</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1,05 Mio. Token</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 Mio. Token</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2 Mio. Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Multimodal-Fähigkeiten</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ausgewogen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">schwächer</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">am stärksten</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Halluzinationsrate</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">niedrig</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">am niedrigsten (ca. 1 %)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">niedrig</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Verfügbarkeit in China</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sonderzugang nötig</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sonderzugang nötig</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sonderzugang nötig</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API-Ökosystem</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">am ausgereiftesten</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">im Aufbau</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">an das Google-Ökosystem gebunden</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Die drei großen internationalen Modelle im Vergleich (August 2026)

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Achtung: die praktische Hürde bei der Nutzung in China

{class="mt-1"}
Für Entwickler in China ist die zentrale Hürde bei GPT, Claude und Gemini der Netzwerkzugang. Zwar lässt sich indirekt über Azure-Proxys oder API-Aggregationsplattformen arbeiten, doch Stabilität und Regelkonformität musst du selbst abwägen. Wenn dein Projekt strenge Anforderungen an die Datensicherheit stellt, lohnt es sich, zuerst heimische Modelle in Betracht zu ziehen.
:::

#### 2. Die chinesischen Leitmodelle: eine blühende Vielfalt

Die großen chinesischen Modelle sind 2026 vom „Verfolger“ zum „Gleichauf-Läufer“ geworden und in manchen Feldern sogar zur „Spitze“. Anders als 2023, als ihnen der Vorwurf gemacht wurde, sie setzten nur auf fremde Modelle auf, stehen die chinesischen Flaggschiffe 2026 bei logischer Inferenz, Codeerzeugung und Chinesisch-Verständnis auf Augenhöhe mit den internationalen Top-Modellen – der Abstand ist auf unter 5 % geschrumpft. Wichtiger noch: Bei chinesischen Szenarien, Kosten und regelkonformer Bereitstellung bieten sie unersetzbare Vorteile.

##### 1. DeepSeek V4: der König des Preis-Leistungs-Verhältnisses

DeepSeek ist eine Erscheinung für sich unter den chinesischen Modellen. Anfang 2025 erschütterte DeepSeek-V3 den Markt mit dem Profil „ein Zehntel des GPT-Preises bei vergleichbarer Leistung“; die Branche nannte es die „K.-o.-Schwelle der Allzweck-KI“ – billiger als DeepSeek ist nichts so gut, teurer bietet nicht so viel fürs Geld. Im August 2026 erschien die finale Version DeepSeek V4-Pro: 1,6 Billionen Parameter im MoE-Aufbau, rund 49 Milliarden davon aktiv, 1 Mio. Token verlustfreier Kontext; beim Preis-Leistungs-Verhältnis für Code gilt es vielfach als weltweite Spitze.

DeepSeek V4 springt bei den Agent-Fähigkeiten deutlich nach vorn – der DeepSWE-Benchmark steigt von 12,8 auf 62,7 (+390 %), NL2Repo von 38,5 auf 61,5. Die API unterstützt jetzt sowohl das Responses-API- als auch das Anthropic-API-Protokoll und ist damit kompatibel mit gängigen Coding-Tools wie Codex und Claude Code. Das heißt: Du kannst in Claude Code die DeepSeek-API statt der Claude-API nutzen – ein Bruchteil der Kosten bei fast identischem Erlebnis.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Modell</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Positionierung</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Eingabe (/Mio. Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ausgabe (/Mio. Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kontextfenster</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek V4 Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Flaggschiff-Inferenz</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3 RMB (ca. 0,43 US$)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6 RMB (ca. 0,87 US$)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 Mio. Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek V4 Flash</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">leicht und schnell</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 RMB (ca. 0,14 US$)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2 RMB (ca. 0,28 US$)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 Mio. Token</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Preisliste der DeepSeek-V4-Serie (August 2026, Aktionspreise)

Preisvergleich: Für je 1 Mio. Token Eingabe plus 1 Mio. Token Ausgabe zahlst du bei DeepSeek V4 Flash rund 0,42 US$, bei GPT-5.6 Sol rund 35 US$ und bei Claude Fable 5 rund 60 US$ – ein Unterschied von bis zu 80- bis 140-fach.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Stolperfalle: DeepSeek wird teurer

{class="mt-1"}
DeepSeek hat am 6. August 2026 offiziell angekündigt, „in Kürze die API-Preise deutlich anheben zu wollen“ – die Aktionspreise dürften also nicht mehr lange gelten. In einzelnen Medien war vom bis zu 30-fachen die Rede; bis zum 14. August lag der endgültige Preisplan aber noch nicht vor. Außerdem führt die finale Version von DeepSeek V4 eine Spitzen-/Talzeit-Preisgestaltung ein – in Stoßzeiten verdoppeln sich die Aufrufpreise. Achte auf die offiziellen Ankündigungen für die aktuellsten Preise.
:::

##### 2. Tongyi Qianwen Qwen3.7 Max: Alibaba Clouds Wahl für Unternehmen

Die Tongyi-Qianwen-Serie (Qwen) von Alibaba Cloud profitiert vom Alibaba-Cloud-Ökosystem und hat bei Enterprise-Deployments klare Vorteile. Das im Juli 2026 erschienene Qwen3.7 Max ist das aktuelle Flaggschiff: ein dichtes Modell mit 235B Parametern, 256K nativem Kontext, erweiterbar auf 1M. Qwens Kernstärken: ein ausgereiftes Open-Source-Ökosystem (die ganze Serie von 7B bis 235B ist offen), präzises Verständnis chinesischer Szenarien und tiefe Integration in die Alibaba-Cloud-Infrastruktur.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Modell</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ausgabepreis (/Mio. Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Geeignet für</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen-turbo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">0,6 RMB</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">schlichte Frage-Antwort, Textklassifikation, hohes Aufkommen</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen-long</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2,0 RMB</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Verarbeitung extrem langer Kontexte (10M)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen3.7-flash</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">7,2 RMB</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">allgemeine Chats, Inhaltserstellung</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen3.7-plus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">12,0 RMB</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Multimodalität (Bild + Video), chinesisches Schreiben</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen3.7-max</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">36,0 RMB</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Flaggschiff für Chinesisch, komplexe Aufgaben</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Staffelpreise der Tongyi-Qianwen-Serie Qwen (August 2026)

Qwen staffelt seine Preise – vom extrem günstigen qwen-turbo (Ausgabe 0,6 RMB/Mio. Token) bis zum Flaggschiff qwen3.7-max (Ausgabe 36 RMB/Mio. Token) deckt die Serie alles ab, vom leichten Frage-Antwort-Betrieb bis zu komplexer Inferenz. Für Unternehmen, die ohnehin Alibaba Cloud nutzen, ist Qwen die naheliegendste Integrationswahl.

##### 3. Zhipu GLM-5.1: chinesische Nummer 1 beim SWE-bench

Die GLM-Serie von Zhipu AI glänzt 2026. GLM-5.1 holte beim SWE-bench den ersten Platz unter den chinesischen Modellen: eine MoE-Architektur mit 744B Parametern und 1 Mio. Token Kontext. Es versteht chinesische Semantik präzise und erlaubt in China regelkonforme, lokale Bereitstellung (On-Premise) – entscheidend für Finanz- und Behördenszenarien mit hohen Datensicherheitsanforderungen. GLM-5.1 kostet 6 RMB pro Mio. Token Eingabe und 24 RMB Ausgabe und liegt damit im Mittelfeld der chinesischen Modelle.

##### 4. Kimi K3: der König der extrem langen Texte

Die Kimi-Serie von Moonshot AI ist für die Verarbeitung extrem langer Texte bekannt. Das im Juli 2026 erschienene Kimi K3 hat 2,8 Billionen Parameter und gehört bei vielen Bewertungen komplexer Aufgaben zur weltweiten Spitzenklasse. Kimis Kernszenarien: Analyse langer Codebasen und abrufgestützte Recherche in langen Dokumenten – es verarbeitet den Text eines ganzen Buchs oder den Code eines ganzen Projekts und glänzt bei „Nadel im Heuhaufen“-Suchaufgaben. Kimi ist relativ teuer (Ausgabe rund 12–20 RMB/Mio. Token), aber beim Preis-Leistungs-Verhältnis in Langtext-Szenarien kommt nichts an es heran.

##### 5. Doubao: ByteDances Allrounder

ByteDances Doubao-Serie zeigte sich 2026 konstant stark. Doubao Seed 2.1 Pro ist das Flaggschiff von Volcengine mit 256K Kontext, im Praxistest konstant in der Gesamtleistung und mit hervorragendem Erlebnis in chinesischen Szenarien. Doubaos Vorteile: schon bei der Registrierung gibt es viele Gratis-Token, eine ausgereifte Integration ins Volcengine-Ökosystem und Preise in einer der niedrigsten Stufen des Landes. Für Einsteiger, die KI-Programmieren schnell ausprobieren wollen, ist Doubao die Einstiegswahl ohne Hürden.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Vergleichspunkt</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">DeepSeek V4</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Qwen3.7 Max</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GLM-5.1</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kimi K3</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Doubao 2.1 Pro</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gesamtwertung</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">87.5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">89.7</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">90.5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">88+</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">85+</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Programmierfähigkeit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">extrem stark</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stark</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">chinesische SWE-Nummer 1</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stark</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">überdurchschnittlich</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Chinesisch-Verständnis</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">sehr gut</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">sehr gut</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">präzise</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">sehr gut</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">sehr gut</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kontextfenster</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 Mio.</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256K-1M</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 Mio.</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">extrem lang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256K</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ausgabepreis (RMB/M)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">36</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">24</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">12-20</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">30</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Open Source</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MIT-Lizenz</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ganze Serie offen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">teilweise offen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">geschlossen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">geschlossen</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">lokale Bereitstellung</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ja</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ja</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ja</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">nein</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">nein</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Die fünf großen chinesischen Modelle im Vergleich (August 2026)

Ein wichtiger Trend: Das Gefühl einer „Generationenlücke“ zwischen chinesischen Modellen und GPT/Claude ist verschwunden. Bei logischer Inferenz und Mathematik-Wettbewerben liegen die chinesischen Flaggschiffe zu GPT-5 meist nur im einstelligen Punktabstand. Beim systematischen Architekturdenken und komplexer Ingenieurs-Inferenz bleibt Claude vorn – es liefert Architekturvorschläge mit mehr „Feingefühl“, während chinesische Modelle gelegentlich „lehrbuchhaft“ wirken. Bei chinesischen Szenarien, Kostenkontrolle und regelkonformer Bereitstellung haben sie aber klar die Oberhand.

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="620" height="290" viewBox="0 0 620 290" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="620" height="290" fill="#ffffff" rx="8"/>
      <line x1="70" y1="230" x2="590" y2="230" stroke="#9ca3af" stroke-width="1.5"/>
      <line x1="70" y1="230" x2="70" y2="20" stroke="#9ca3af" stroke-width="1.5"/>
      <line x1="70" y1="60" x2="590" y2="60" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="70" y1="116" x2="590" y2="116" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="70" y1="173" x2="590" y2="173" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="4,4"/>
      <text x="62" y="234" font-size="10" fill="#6b7280" text-anchor="end">0</text>
      <text x="62" y="120" font-size="10" fill="#6b7280" text-anchor="end">50</text>
      <text x="62" y="64" font-size="10" fill="#6b7280" text-anchor="end">100</text>
      <text x="340" y="262" font-size="10.5" fill="#374151" text-anchor="middle">Ausgabepreis (Yuan/Mio. Token)</text>
      <!-- bars: price -->
      <rect x="95" y="218" width="60" height="12" fill="#4f46e5"/><text x="125" y="212" font-size="9" fill="#374151" text-anchor="middle">6</text><text x="125" y="248" font-size="9.5" fill="#374151" text-anchor="middle">DeepSeek</text>
      <rect x="195" y="146" width="60" height="84" fill="#4f46e5"/><text x="225" y="140" font-size="9" fill="#374151" text-anchor="middle">36</text><text x="225" y="248" font-size="9.5" fill="#374151" text-anchor="middle">Qwen</text>
      <rect x="295" y="182" width="60" height="48" fill="#4f46e5"/><text x="325" y="176" font-size="9" fill="#374151" text-anchor="middle">24</text><text x="325" y="248" font-size="9.5" fill="#374151" text-anchor="middle">GLM</text>
      <rect x="395" y="200" width="60" height="30" fill="#4f46e5"/><text x="425" y="194" font-size="9" fill="#374151" text-anchor="middle">16</text><text x="425" y="248" font-size="9.5" fill="#374151" text-anchor="middle">Kimi</text>
      <rect x="495" y="170" width="60" height="60" fill="#4f46e5"/><text x="525" y="164" font-size="9" fill="#374151" text-anchor="middle">30</text><text x="525" y="248" font-size="9.5" fill="#374151" text-anchor="middle">Doubao</text>
      <!-- scores -->
      <circle cx="125" cy="118" r="5" fill="#d4a017"/><text x="140" y="114" font-size="9" fill="#78350f">87.5</text>
      <circle cx="225" cy="110" r="5" fill="#d4a017"/><text x="240" y="106" font-size="9" fill="#78350f">89.7</text>
      <circle cx="325" cy="105" r="5" fill="#d4a017"/><text x="340" y="101" font-size="9" fill="#78350f">90.5</text>
      <circle cx="425" cy="112" r="5" fill="#d4a017"/><text x="440" y="108" font-size="9" fill="#78350f">88+</text>
      <circle cx="525" cy="116" r="5" fill="#d4a017"/><text x="540" y="112" font-size="9" fill="#78350f">85+</text>
      <rect x="90" y="30" width="12" height="12" fill="#4f46e5"/><text x="108" y="41" font-size="9.5" fill="#374151">Ausgabepreis (niedriger = besser)</text>
      <circle cx="170" cy="36" r="5" fill="#d4a017"/><text x="182" y="40" font-size="9.5" fill="#374151">Gesamtscore (höher = besser)</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Abbildung 4: Preis- und Leistungsvergleich der fünf Modelle (niedrigerer Preis ist besser, höhere Punktzahl ist besser)
:::

#### 3. Der Entscheidungsrahmen für die Modellwahl

Nachdem du die Modelle kennst: Wie wählst du das richtige für dein Projekt? Hier bekommst du die „Vier-Fragen-Methode“ – beantwortest sie, hast du das passende Modell festgenagelt.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-globe mr-1"></i> Läuft dein Projekt in China oder international?</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">In China → heimische Modelle wählen</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">International → ausländische Modelle möglich</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-laptop-code mr-1"></i> Ist die Kernaufgabe Programmieren oder etwas anderes?</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Programmieren → Claude oder DeepSeek</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">Anderes → weiter prüfen</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-book mr-1"></i> Brauchst du sehr langen Kontext (&gt;500 000 Token)?</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Ja → Gemini oder Kimi</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">Nicht nötig → weiter prüfen</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-coins mr-1"></i> Budget knapp?</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Knapp → DeepSeek oder Qwen-turbo</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Weniger kritisch → GPT-5.6 oder Claude</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Abbildung 5: Die Vier-Fragen-Entscheidungsmethode für die Modellwahl
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tipp: Kombinationsstrategie

{class="mt-1"}
Diese Methode ist kein Dogma – viele Szenarien brauchen eine Kombination mehrerer Modelle. Eine gängige Strategie: DeepSeek oder Qwen für die Alltagsentwicklung (günstig, gutes Chinesisch), Claude für kritische Architekturentscheidungen (starke Inferenz, wenig Halluzination), Gemini für Multimodal-Analysen (Bild- und Videobearbeitung). Wechsle das Modell nach Bedarf, statt stur bei einem Modell zu bleiben.
:::

#### 4. Erste Schritte mit der API: große Modelle von null anbinden

Viele KI-Coding-Tutorials zeigen nur die Chat-Oberfläche. Aber echtes „KI-Programmieren“ – deine App ruft ein großes Modell auf – läuft über eine API. Eine API (Application Programming Interface, Programmierschnittstelle) ist ein Kommunikationsprotokoll zwischen Programmen. Über die API kann dein Code die Fähigkeiten eines großen Modells aufrufen, als riefe er eine Funktion auf.

##### 1. Was ist ein Token

Bevor du die API verstehst, musst du den Begriff „Token“ begreifen. Token ist die Grundeinheit, nach der große Modelle abrechnen – denk an sie als „Lese- und Schreibeinheit der KI“. Ein Token entspricht etwa: im Englischen 0,75 Wörtern (4 Zeichen), im Chinesischen 0,5–1 Schriftzeichen. Ein chinesischer Text von 1000 Zeichen verbraucht etwa 1500–2000 Token.

Token sind weder Wortzahl noch Zeichenanzahl. Große Modelle zerlegen Text mit einem eigenen Tokenizer in Token. Dasselbe Wort kann je nach Modell unterschiedlich viele Token belegen – „Künstliche Intelligenz“ kostet in GPT vielleicht 3 Token, in DeepSeek vielleicht 2. Die APIs der meisten Modelle liefern die tatsächlich verbrauchte Tokenzahl zurück; du findest sie in der API-Antwort.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Token-Kosten schnell überschlagen

{class="mt-1"}
1 Mio. chinesische Schriftzeichen entsprechen etwa 1,5 Mio. Token. Verarbeitest du 1 Mio. Zeichen Eingabe plus 1 Mio. Zeichen Ausgabe mit DeepSeek V4 Flash, kostet das rund 0,42 US$ (ca. 3 RMB); mit Claude Fable 5 für dieselbe Menge rund 60 US$ (ca. 434 RMB). Genau deshalb wirkt sich die Modellwahl direkt auf deine Projektkosten aus.
:::

##### 2. Den API-Key besorgen

Der erste Schritt zur Nutzung der APIs großer Modelle ist der API-Key – eine Zeichenfolge zur Identitätsprüfung. Jeder Modellanbieter hat seine eigene API-Plattform; du registrierst ein Konto und legst einen API-Key an. Hier die Zugänge der API-Plattformen der wichtigsten Modelle samt Ablauf:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Modell</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">API-Plattform</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ablauf</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Gratis-Kontingent</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">platform.deepseek.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Registrieren → Identität verifizieren → API-Key erstellen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Startguthaben für neue Nutzer</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tongyi Qianwen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">bailian.aliyun.com (Bailian-Plattform)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mit Alibaba-Cloud-Konto anmelden → Dienst aktivieren → Key erstellen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gratis-Testphase für neue Nutzer</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Zhipu GLM</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">open.bigmodel.cn</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Registrieren → Identität verifizieren → API-Key erstellen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Startguthaben für neue Nutzer</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kimi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">platform.moonshot.cn</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Registrieren → Identität verifizieren → API-Key erstellen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">begrenztes Gratis-Kontingent</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Doubao</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">volcengine.com (Volcengine)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Registrieren → Ark aktivieren → API-Key erstellen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">viele Gratis-Token bei der Registrierung</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenAI GPT</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">platform.openai.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Registrieren → Kreditkarte hinterlegen → API-Key erstellen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">kein Gratis-Kontingent (kostenpflichtig)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Anthropic Claude</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">console.anthropic.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Registrieren → Karte hinterlegen → API-Key erstellen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">kleines Startguthaben für neue Nutzer</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
API-Plattformen der wichtigsten Modelle und Key-Bezug (August 2026)

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Sicherheitshinweis: Der API-Key ist wie dein Wallet-Passwort

{class="mt-1"}
Ein API-Key ist so wertvoll wie dein Wallet-Passwort – wer ihn hat, kann mit deinem Kontingent Modelle aufrufen. Deshalb: Schreibe den API-Key niemals in den Code (verwende Umgebungsvariablen); lade Code mit Key niemals in ein öffentliches Git-Repository; teile niemals Screenshots, auf denen der Key zu sehen ist. Wenn der Key abhandenkommt, lösch ihn sofort auf der Plattform und leg einen neuen an.
:::

##### 3. Der erste API-Aufruf

Mit deinem API-Key kannst du die API großer Modelle in jeder Programmiersprache aufrufen. Hier das einfachste Beispiel in Python – eine Nachricht an DeepSeek senden und die Antwort holen.

::: div .code-block
:::inline div .code-head
<span>PYTHON · Erster API-Aufruf</span><span class="dots">···</span>
:::

```
# SDK installieren: pip install openai
# DeepSeek ist kompatibel mit dem OpenAI-SDK, direkt nutzbar
from openai import OpenAI
import os

# 1. Client erstellen (API-Key aus der Umgebungsvariable)
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 2. Anfrage senden
response = client.chat.completions.create(
    model="deepseek-chat",  # Modell angeben
    messages=[
        {"role": "system", "content": "Du bist ein Python-Programmierassistent."},
        {"role": "user", "content": "Schreibe eine Quicksort-Funktion."}
    ]
)

# 3. Antwort abholen
print(response.choices[0].message.content)

# 4. Token-Verbrauch ansehen
print(f"Eingabe-Token: {response.usage.prompt_tokens}")
print(f"Ausgabe-Token: {response.usage.completion_tokens}")
print(f"Token gesamt: {response.usage.total_tokens}")
```
:::

Die Kernlogik dieses Codes: Client anlegen (mit API-Key und Modelladresse) → Nachrichtenliste bauen (system setzt die Rolle, user ist die Nutzereingabe) → Anfrage senden → Antwort holen. Dieses Muster passt auf praktisch alle Modelle im OpenAI-Format – um das Modell zu wechseln, tauschst du nur api_key und base_url. Genau deshalb orientieren sich viele chinesische Modelle am OpenAI-SDK-Format: Entwickler ändern zwei Zeilen Code, und das Modell wechselt – der Migrationsaufwand ist minimal.

Hier die Code-Unterschiede beim Wechsel auf andere Modelle – beachte, dass nur zwei Zeilen geändert werden:

::: div .code-block
:::inline div .code-head
<span>PYTHON · Modellwechsel braucht nur zwei Zeilen</span><span class="dots">···</span>
:::

```
# DeepSeek
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
# model="deepseek-chat"

# Qwen (Bailian-Plattform)
client = OpenAI(
    api_key=os.environ.get("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
# model="qwen-plus"

# Zhipu GLM
client = OpenAI(
    api_key=os.environ.get("GLM_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4"
)
# model="glm-4"

# OpenAI GPT
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    # Standard-base_url reicht
)
# model="gpt-5.6-terra"
```
:::

##### 4. Streaming-Antworten verarbeiten

In echten Anwendungen willst du meist nicht warten, bis die KI alles fertig geschrieben hat, um es auf einen Schlag zu zeigen – das lässt Nutzer zu lange warten. Gestreamte Antworten (Streaming) zeigen den Text Zeichen für Zeichen, während die KI ihn erzeugt, und heben das Nutzererlebnis deutlich. Wie bei einer Schreibmaschine, die Buchstabe für Buchstabe ausspuckt – für Nutzer fühlt sich das völlig anders an.

::: div .code-block
:::inline div .code-head
<span>PYTHON · Streaming-Antwort</span><span class="dots">···</span>
:::

```
# Streaming: Ausgabe Stück für Stück
stream = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "Schreibe ein Tutorial zu Bubblesort in Python"}
    ],
    stream=True  # Streaming einschalten
)

# blockweise empfangen und ausgeben
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)
# die Ausgabe erscheint Buchstabe für Buchstabe wie bei einer Schreibmaschine
```
:::

#### 5. Kaufberatung für Token-Pläne

Die meisten Modellanbieter rechnen auf zwei Arten ab: nutzungsbasiert (Pay-as-you-go) und als Abo (Token-Plan/Subscription). Den Unterschied zu verstehen hilft dir, die Kosten deutlich zu senken.

##### 1. Pay-as-you-go vs. Abo

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kriterium</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Nutzungsbasiert (Pay-as-you-go)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Abo (Subscription)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Abrechnung</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">zahlen pro verbrauchtem Token</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">feste Vorauszahlung gegen Kontingent</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Geeignet für</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">schwankende Nutzung, gelegentliche Aufrufe</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">gleichmäßige Nutzung, häufige Aufrufe</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Preisvorteil</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Standardpreis</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">20–50 % unter Nutzungsbasis</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Flexibilität</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">jederzeit nutzbar, ohne Bindung</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Vorauszahlung nötig; Kontingent kann verfallen</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Überziehen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">automatisch nutzungsbasiert</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">nach Aufbrauchen des Kontingents nutzungsbasiert</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Beispiel-Plattformen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">die offiziellen API-Plattformen der Modelle</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenAI Plus/Pro, Claude Pro, Cursor Pro</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Vergleich der beiden Abrechnungsarten

Für Einsteiger empfiehlt sich der Start mit nutzungsbasierter Abrechnung – keine Vorauszahlung, du zahlst nur, was du nutzt. Wenn sich deine Monatsnutzung auf einem Level einpendelt (etwa über 50 RMB pro Monat), denk über den Wechsel zum Abo nach, um den Stückpreis zu senken.

##### 2. Die wichtigsten Abo-Pakete im Überblick

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Paket</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Monatspreis</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Enthalten</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Geeignet für</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ChatGPT Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">gratis</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">unbegrenzte Text-Chats mit GPT-5.6 Luna</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Erstkontakt ohne Vorkenntnisse</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ChatGPT Plus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">20 US$/Monat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Sol, Bilderzeugung, Datenanalyse, Plugin-Zugang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gelegenheitsnutzer</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ChatGPT Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">200 US$/Monat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">alle Modelle unbegrenzt, bevorzugter Zugang zu neuen Funktionen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Intensiv-Profis</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">gratis</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">begrenzte Zahl von Claude-Chats</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Erstkontakt ohne Vorkenntnisse</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">20 US$/Monat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude unbegrenzt, bevorzugter Zugang zu neuen Modellen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Entwickler</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">gratis</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">begrenzte KI-Vervollständigungen und Chats</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">für Anfänger zum Ausprobieren</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">20 US$/Monat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">unbegrenzte KI-Vervollständigungen, 500 Premium-Anfragen/Monat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Alltagsentwickler</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor Business</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">40 US$/Monat pro Person</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Teamzusammenarbeit, Admin-Bereich, Datenschutzmodus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">für Teams</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Abo-Pakete der wichtigsten KI-Tools (August 2026)

Bei den chinesischen Modellen sehen die Abo-Angebote etwas anders aus. DeepSeek rechnet vor allem nutzungsbasiert ab und hat kein Monatsabo – du lädst Guthaben auf und zahlst nach tatsächlichem Verbrauch. Tongyi Qianwen bietet auf der Bailian-Plattform vorausbezahlte Ressourcenpakete (ein festes Token-Kontingent zum Rabattpreis). Doubao hat auf Volcengine ähnliche Vorauszahlungsangebote. Für Entwickler in China ist die sparsamste Kombination meist: DeepSeek nutzungsbasiert (Alltagsentwicklung) plus Doubaos Gratis-Kontingent (zum Ausprobieren).

##### 3. API-Aggregatoren

Wenn du mehrere Modelle gleichzeitig nutzen willst, sind API-Aggregatoren eine bequeme Wahl. Eine Aggregatorplattform stellt dir einen einzigen API-Key bereit, mit dem du Dutzende Modelle aus aller Welt aufrufen kannst, ohne dich auf jeder Plattform separat zu registrieren.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Plattform</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Merkmale</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Preisvorteile</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Geeignete Szenarien</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenRouter (openrouter.ai)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Aggregator außerhalb Chinas: mit einem Key Modelle aus aller Welt aufrufen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Transparente Preise, Echtzeit-Preisvergleich möglich</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wenn du flexibel zwischen mehreren Übersee-Modellen wechseln willst</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SiliconFlow (siliconflow.cn)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Aggregator in China mit APIs für viele chinesische Modelle</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">20–30 % unter dem offiziellen Preis</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Entwickler in China, die mehrere Modelle vergleichen wollen</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Azure OpenAI (Microsoft-Proxy)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Die über Microsoft Azure vermittelte OpenAI-API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Batch API mit 50 % Rabatt</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenAI auf Unternehmensniveau, große asynchrone Auftragsmengen</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Baidu Qianfan (qianfan.baidubce.com)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Baidus KI-Cloud-Plattform, mit Modellen wie Ernie (Wenxin)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gratis-Guthaben für neue Nutzer</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nutzer im Baidu-Ökosystem</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Die wichtigsten API-Aggregatoren (Stand: August 2026)

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Vorsicht vor Fallen: Kaufe keine „Shared Keys“

{class="mt-1"}
Kaufe keine sogenannten „Shared API Keys“ auf Plattformen wie Taobao oder Xianyu – diese Keys haben meist eine unklare Herkunft, können jederzeit gesperrt werden und bergen das Risiko von Datenlecks. Beziehe API-Keys immer über offizielle Plattformen oder seriöse Aggregatoren.
:::

##### 4. Strategien zur Kostenoptimierung

Das richtige Modell zu wählen ist nur der erste Schritt; sparsam damit umzugehen ist genauso wichtig. Hier einige praxiserprobte Strategien zur Kostenoptimierung:

1. Nutze Cache-Treffer clever. Viele Modelle bieten eine „Cache“-Funktion – enthält deine Anfrage Inhalte, die schon zuvor verarbeitet wurden (z. B. den Systemprompt), wird dieser Teil nur zu einem extrem niedrigen Preis berechnet. Bei DeepSeek kostet ein Cache-Treffer nur 1/60 des normalen Preises. Feste Systemprompts an den Anfang der Nachrichtenliste zu stellen maximiert die Cache-Trefferquote.
2. Gestaffeltes Routing – einfache Aufgaben mit günstigen Modellen erledigen, komplexe mit teuren. Zum Beispiel DeepSeek V4 Flash für die Textklassifikation (Ausgabe: 2 Yuan pro Million Token) und Claude für den Architekturentwurf (Ausgabe: 181 Yuan pro Million Token). In einem Projekt können 80 % der Aufrufe mit dem günstigen Modell laufen.
3. Begrenze die Ausgabelänge. Die API wird nach Ausgabe-Token abgerechnet – je länger die Ausgabe, desto teurer. In Szenarien, die keine langen Ausführungen brauchen, setze den Parameter max_tokens, um die Ausgabe zu begrenzen und zu verhindern, dass die KI „zu viel um den heißen Brei redet“.
4. Nutze die Batch API für Aufgaben ohne Echtzeitbedarf. Wenn du viele Aufgaben hast, die keine sofortige Antwort brauchen (etwa Massen-Annotation von Daten oder Dokumentzusammenfassungen), bekommst du mit der Batch API 50 % Rabatt. OpenAI und Azure bieten diese Funktion beide an.
5. Überwache den Token-Verbrauch. Die meisten API-Plattformen bieten ein Nutzungs-Dashboard. Schau regelmäßig nach, wie sich der Verbrauch verteilt, finde die Aufrufe mit dem höchsten Token-Verbrauch und optimiere gezielt dort. Eine kleine Anpassung am Prompt (etwa statt „Erkläre bitte ausführlich“ jetzt „Erkläre es bitte in 3 Sätzen“) kann 50 % der Token sparen.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Optimierungsstrategie</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ersparnis</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Umsetzungsaufwand</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Erläuterung</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cache-Treffer</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">bis zu 98 %</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Niedrig</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Feste Inhalte an den Anfang der Nachrichten stellen</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gestaffeltes Routing</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">50%-80%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mittel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Einfache Aufgaben mit dem günstigen Modell</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ausgabelänge begrenzen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">30%-60%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Niedrig</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Den Parameter max_tokens setzen</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Batch API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">50%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Niedrig</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Batch-Verarbeitung für Aufgaben ohne Echtzeitbedarf</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prompt-Optimierung</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">20%-50%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mittel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prompts straffen, Redundanz reduzieren</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Strategien zur Kostenoptimierung und ihre Wirkung (Stand: August 2026)

#### 6. Praxis: Eine LLM-API in dein Projekt einbinden

Beenden wir dieses Kapitel mit einer kompletten Praxisübung – einem „KI-Zusammenfassungs-Generator“: Der Nutzer gibt einen langen Text ein, und über eine LLM-API wird eine Zusammenfassung erzeugt. Diese Übung zeigt den kompletten Ablauf eines API-Aufrufs: Umgebungskonfiguration, API-Aufruf, Fehlerbehandlung, Kostenkontrolle.

::: div .code-block
:::inline div .code-head
<span>PYTHON · ai_summarizer.py</span><span class="dots">···</span>
:::

```
# ai_summarizer.py - KI-Zusammenfassungsgenerator
import os
from openai import OpenAI

# 1. Konfiguration (API-Key aus der Umgebungsvariable, nie hart kodiert)
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def summarize(text: str, max_length: int = 200) -> dict:
    """Erzeugt eine Textzusammenfassung

    Args:
        text: zu zusammenfassender Originaltext
        max_length: maximale Länge der Zusammenfassung (Token)

    Returns:
        dict: enthält Zusammenfassung und Token-Verbrauch
    """
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "system",
                    "content": "Du bist ein Zusammenfassungsgenerator."
                               "Fasse den Text des Nutzers klar und knapp zusammen."
                               "Die Zusammenfassung hat höchstens 3 Sätze."
                },
                {
                    "role": "user",
                    "content": f"Fasse den folgenden Text zusammen:\n\n{text}"
                }
            ],
            max_tokens=max_length,  # begrenzt die Ausgabelänge
            temperature=0.3  # niedrige Temperatur = stabiler
        )

        return {
            "success": True,
            "summary": response.choices[0].message.content,
            "input_tokens": response.usage.prompt_tokens,
            "output_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

# 2. Anwendungsbeispiel
if __name__ == "__main__":
    long_text = """
    (langen Text hier einfügen ...)
    """

    result = summarize(long_text)

    if result["success"]:
        print(f"Zusammenfassung: {result['summary']}")
        print(f"Verbrauchte Token: {result['total_tokens']}")
        # Kostenschätzung: DeepSeek V4 Flash
        cost = result['total_tokens'] * 0.000004  # ≈ 0,4 Cent je 1000 Token
        print(f"Geschätzte Kosten: {cost:.4f} Yuan")
    else:
        print(f"Fehler: {result['error']}")
```
:::

Dieser Code verkörpert mehrere Best Practices für API-Aufrufe: Der API-Key wird über Umgebungsvariablen gelesen und niemals in den Code geschrieben; die Funktion hat klare Dokumentation und Typhinweise; mit max_tokens ist die Ausgabelänge begrenzt; temperature steht auf einem niedrigen Wert (0,3) für stabilere Ausgaben; es gibt eine vollständige Fehlerbehandlung; und der Token-Verbrauch wird fürs Kosten-Tracking zurückgegeben. Wenn du die KI diesen Code schreiben lässt, kannst du ihr genau diese Anforderungen nennen – sie ist durchaus in der Lage, das umzusetzen.

:::inline div .quote-line
Die Schlussbotschaft dieses Kapitels: Modelle sind die "Munition", die Methodik die "Taktik". Die richtige Munition erleichtert den Kampf, aber ohne gute Taktik gewinnt auch die beste Munition keinen Krieg. Du kennst jetzt die Stärken der Modelle und den API-Umgang – dein "Munitionsdepot" ist voll; wie du die Schlacht führst, entscheidet die Denkmethodik aus den vorigen Kapiteln.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Los geht's: Bringe deinen ersten API-Aufruf zum Laufen

{class="mt-1"}
Registriere dich auf einer Plattform für chinesische Modelle (empfohlen: DeepSeek oder Zhipu, beide schenken Neukunden ein Startguthaben), erstelle einen API-Key, trage ihn in die System-Umgebungsvariablen ein (nicht in den Code!) und führe dann den obigen Code für den „ersten API-Aufruf“ aus. In dem Moment, in dem die Antwort der KI ausgegeben wird, hast du die Grenze zwischen „KI nutzen“ und „KI-Anwendungen bauen“ überschritten.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Kapitelfazit

- Internationale Top 3: GPT-5.6 (der ausgewogene Allrounder), Claude (König des Programmierens + nur 1 % Halluzinationsrate), Gemini (Multimodal-König + 2 Mio. Kontext)
- Chinesische Top 5: DeepSeek V4 (Preis-Leistungs-König, Preiserhöhungs-Ankündigungen beachten), Qwen3.7 (Unternehmensklasse), GLM-5.1 (Nr. 1 in China bei SWE), Kimi K3 (extrem lange Texte), Doubao (kostenloser Einstieg)
- Die Vier-Fragen-Methode: Wo läuft das Modell? Programmieren oder etwas anderes? Sehr langer Kontext? Budgetkritisch?
- Token sind die Abrechnungseinheit: 1 chinesisches Zeichen ≈ 1,5–2 Token; 1 Million Zeichen ≈ 1,5 Millionen Token
- API-Key = Wallet-Passwort: in Umgebungsvariablen verwalten, niemals hardcoden, nie zu Git hochladen
- Chinesische Modelle sind meist kompatibel zum OpenAI-SDK: Für einen Modellwechsel genügen zwei geänderte Zeilen, api_key und base_url
- Fünf Spartipps: Cache-Treffer nutzen, gestaffeltes Routing, Ausgabe begrenzen, Batch API, Verbrauch überwachen
:::
