---
id: di-yi-zhang-harmony
part: ji-chu-pian
nav: Kapitel 1 Anhang: HarmonyOS-Betriebssystem Spezialthema
toc: default
kind: supplement
---

### Kapitel 1 Anhang: HarmonyOS-Betriebssystem Spezialthema

{class="chapter-intro mb-4"}
HarmonyOS ist das von Huawei selbst entwickelte Betriebssystem. Seit der Veröffentlichung im Jahr 2019 hat es mehrere große Versionen durchlaufen. Es ist nicht „nur ein weiterer Android-Ersatz", sondern eine neue Spezies mit einem eigenen Designkonzept. Lass uns dieses aufstrebende Betriebssystem gemeinsam genauer betrachten.

#### Eins. Was ist HarmonyOS? Warum ist es anders?

Das Kernkonzept von HarmonyOS lautet „Vernetzung aller Dinge". Anders als herkömmliche Betriebssysteme, die hauptsächlich ein einzelnes Gerät bedienen, wurde HarmonyOS von Anfang an für die geräteübergreifende Zusammenarbeit konzipiert.

<strong>Hinweise:</strong> ist die Seele von HarmonyOS. Kurz gesagt: Sie kann mehrere Geräte zu einem „Super-Terminal" virtualisieren. Dein Smartphone, Tablet, Computer, deine Uhr und dein Fernseher sind keine isolierten Einzelgeräte mehr, sondern Organe eines Ganzen, die gegenseitig ihre Fähigkeiten nutzen können.

Ein Beispiel: Du schaust ein Video auf dem Smartphone und möchtest es auf einem großen Bildschirm sehen. Klassisch würdest du es spiegeln; unter HarmonyOS kannst du das Video direkt auf den Fernseher „übertragen" und dort weiter ansehen, während das Smartphone zur Fernbedienung wird. Das ist kein einfaches Mirroring, sondern die Anwendung selbst läuft geräteübergreifend.

#### Zwei. HarmonyOS 4.3: Die auf AOSP basierende ausgereifte Version

HarmonyOS 4.3 ist die Version, die derzeit auf Huawei-Smartphones weit verbreitet ist. Es ist erwähnenswert, dass HarmonyOS 4.3 mit dem Code-Framework des Android Open Source Project (AOSP) kompatibel ist und daher vollständig Android-Anwendungen ausführen kann — die meisten Apps, die du im Huawei AppGallery lädst, sind im Wesentlichen Android-Anwendungen, die über die Kompatibilitätsschicht von HarmonyOS laufen. HarmonyOS 4.3 ist jedoch nicht einfach ein ummanteltes Android, sondern fügt auf der AOSP-Basis zahlreiche von Huawei selbstentwickelte Fähigkeiten wie die verteilte Architektur und die Ark Engine hinzu.

##### Kernmerkmale:

- <strong>Android-App-Kompatibilität</strong>: Da es auf AOSP basiert, kann HarmonyOS 4.3 nahezu alle Android-Anwendungen normal ausführen — Nutzer merken kaum einen Unterschied.
- <strong>Ark Engine</strong>: Ein von Huawei selbstentwickelter Compiler und eine Laufzeitumgebung, die Apps flüssiger und sparsamer macht. Gegenüber frühen Versionen ist die Flüssigkeit deutlich gestiegen.
- <strong>Super-Terminal</strong>: Im Kontrollzentrum siehst du auf einen Blick die anderen HarmonyOS-Geräte in der Umgebung – zum Verbinden genügt das Herüberziehen. Das Smartphone nutzt Maus und Tastatur des Computers, das Tablet die Smartphone-Kamera: sehr praktisch.
- <strong>Service-Karten</strong>: Ähnlich den Widgets unter iOS, aber flexibler. Durch Wischen nach oben über einem App-Symbol wird eine Karte eingeblendet, die wichtige Informationen zeigt, ohne die App zu öffnen.
- <strong>Reiner Modus</strong>: Erlaubt die Installation von Apps nur aus dem offiziellen App-Markt und reduziert das Risiko durch Malware.
- <strong>Datenschutz-Zentrum</strong>: Zentrale Verwaltung von App-Berechtigungen, Einsicht in das Verhalten von Apps.

##### Besonderheiten der Benutzeroberfläche:

- <strong>Magazin-Sperrbildschirm</strong>: Der Sperrbildschirm zeigt ansprechende Bilder und Artikel, durch Wegwischen gelangt man zum Startbildschirm.
- <strong>Universelle Karten</strong>: Symbole auf dem Startbildschirm lassen sich zu Karten aufklappen, die mehr Informationen anzeigen.
- <strong>Super-Zwischenablage</strong>: Ein temporärer Speicherbereich für Text, Bilder und Dateien, der in jeder App per Drag-and-Drop eingefügt werden kann. Teilen über App-Grenzen wird butterweich.
- <strong>Intelligente Suche</strong>: Eine globale Suche über Apps, Dateien, Einstellungen und das Web.

#### Drei. HarmonyOS NEXT (HarmonyOS 5): Der wahre Start von Huaweis eigenem Betriebssystem

: HarmonyOS NEXT verwendet einen von Huawei selbstentwickelten Kernel ohne AOSP-Code. Das System ist schlanker, sicherer und effizienter.<strong>unterstützt keine Android-Apps mehr direkt</strong>. Das ist der entscheidende Schritt von HarmonyOS aus der „Android-kompatiblen Übergangsform“ hin zu einem „vollständig unabhängigen Betriebssystem“.

##### Wichtige Neuerungen:

- <strong>Vollständig eigener Kernel</strong>: Das ist die größte Veränderung. HarmonyOS NEXT kann nur native HarmonyOS-Apps ausführen, APK-Dateien lassen sich nicht mehr installieren oder starten. Prüfe vor einem Upgrade, ob deine wichtigsten Apps bereits als native HarmonyOS-Version vorliegen.
- <strong>Keine Android-App-Unterstützung mehr</strong>: Ein völlig neues Sicherheitssystem mit durchgängigem Schutz von der Hardware bis zur Software. Unterstützt feinere Berechtigungssteuerung, z. B. „ungefähre Standortbestimmung" — eine App erfährt nur grob, wo du bist, nicht die genaue Position.
- <strong>Tiefe KI-Integration</strong>: Systemweite KI-Fähigkeiten, nicht nur in einer einzelnen App. So können KI-Untertitel Videos in Echtzeit übersetzen, KI-Freisteller das Motiv intelligent erkennen.
- <strong>Nahtloser geräteübergreifender Datenfluss</strong>: Die verteilten Fähigkeiten gehen noch weiter. Der App-Zustand lässt sich nahtlos zwischen Geräten wechseln — ein Dokument, das du auf dem Smartphone bearbeitest, öffnet sich am Computer automatisch, wenn du dorthin gehst.
- <strong>Meta-Services</strong>: Leichtgewichtige Dienste, die ohne Installation nutzbar sind. Zum Beispiel lässt sich durch das Scannen eines QR-Codes direkt eine Funktion öffnen, ohne vorher eine App herunterladen zu müssen.
- <strong>Nahtloser geräteübergreifender Datenfluss</strong>: Die verteilten Fähigkeiten gehen noch weiter. Der App-Zustand wechselt nahtlos zwischen Geräten – das am Handy begonnene Dokument öffnet am Computer automatisch.
- <strong>Meta-Services (Luft-Apps)</strong>: Leichtgewichtige Dienste, die ohne Installation nutzbar sind. Zum Beispiel lässt sich durch das Scannen eines QR-Codes direkt eine Funktion öffnen – ohne vorherigen App-Download.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Vor dem Upgrade auf HarmonyOS NEXT unbedingt beachten

{class="mt-1"}
Nach dem Upgrade auf HarmonyOS NEXT kann dein Smartphone keine Android-Anwendungen mehr ausführen. Kläre vor dem Upgrade unbedingt: ① Deine wichtigsten Apps liegen als native HarmonyOS-Version vor; ② In deinem Arbeits- oder Alltag gibt es kein Szenario, das zwingend auf Android-Apps angewiesen ist. Ein Zurückrollen auf HarmonyOS 4.3 ist nach dem Upgrade nicht möglich.
:::

##### Änderungen in der Bedienlogik:

- <strong>Gesten-Navigation</strong>: Wisch am linken oder rechten Rand zum Zurück, wische von unten nach oben zum Startbildschirm, wische und halte für die Multitasking-Ansicht.
- <strong>Intelligente Mehrfenster</strong>: Unterstützt Split-Screen, schwebende Fenster, Parallelansicht und weitere Multitasking-Formen.
- <strong>MeeTime-Anrufe</strong>: Huaweis Videotelefonie-Dienst, unterstützt Bildschirmfreigabe, Verschönerung und Hintergrund-Unschärfe.

#### 4. Das HarmonyOS-Ökosystem: Geräte und Apps

HarmonyOS ist nicht nur ein Smartphone-System, sondern ein Ökosystem, das viele Gerätetypen abdeckt.

##### Unterstützte Gerätetypen:

- <strong>Smartphone und Tablet</strong>: Kerngeräte mit dem vollsten Funktionsumfang.
- <strong>Smartwatch und Armband</strong>: Eigenständig oder mit dem Smartphone gekoppelt.
- <strong>Smart Screen (Fernseher)</strong>: Das Unterhaltungszentrum zu Hause.
- <strong>Smarter Lautsprecher</strong>: Eingang für die Sprachinteraktion.
- <strong>Automobil</strong>: HarmonyOS Cockpit – das Erlebnis des intelligenten Fahrerraums.
- <strong>Smart Home</strong>: Kühlschrank, Klimaanlage, Waschmaschine und mehr.

##### Stand des App-Ökosystems:

Stand des App-Ökosystems:

#### 5. Praktische HarmonyOS-Tipps

- <strong>Super-Terminal</strong>: Wische oben rechts nach unten, um das Kontrollzentrum zu öffnen, tippe auf „Super-Terminal“ – du siehst die anderen Geräte in der Umgebung und verbindest sie per Ziehen.
- <strong>Super-Zwischenablage</strong> Der HarmonyOS App Market umfasst bereits Millionen von Apps, die gängigen sind im Wesentlichen alle vertreten. Huawei treibt die Entwicklung nativer HarmonyOS-Apps aktiv voran. Stand Anfang 2025 haben führende Apps wie WeChat, Alipay, Taobao, Douyin, Meituan und JD native HarmonyOS-Versionen vorgestellt, sodass der Alltag weitgehend reibungslos funktioniert. Einige Nischen- und Branchen-Apps sind möglicherweise noch in der Anpassung — vor einem Upgrade solltest du prüfen, ob deine wichtigsten Apps bereits unterstützt werden.
- <strong>Service-Karten</strong>: Text/Bild/Datei lange drücken, „In Zwischenablage kopieren" wählen, dann in einer anderen App lange drücken und einfügen oder per Drag-and-Drop herausziehen.
- <strong>Intelligente Mehrfenster</strong>: Vom linken oder rechten Bildschirmrand nach innen wischen und halten, um die Seitenleiste zu öffnen; tippe eine App an, um sie als schwebendes Fenster zu öffnen.
- <strong>Datenschutz</strong>: Einstellungen > Datenschutz – dort siehst du die Nutzungsprotokolle der App-Berechtigungen und kannst z. B. die unscharfe Standortbestimmung einstellen.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Wichtige Hinweise

{class="mt-1"}
HarmonyOS wird kontinuierlich weiterentwickelt, zwischen den Versionen kann es leichte Unterschiede geben. Diese Beschreibung bezieht sich auf die wesentlichen Merkmale von HarmonyOS 4.3 und 5.0. Die konkreten Funktionen richten sich nach der tatsächlichen Version deines Smartphones. Halte das System aktuell, um die neuesten Funktionen und Sicherheits-Patches zu erhalten.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Jetzt ausprobieren: HarmonyOS-Funktionen erleben

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Öffne das Kontrollzentrum und tippe auf „Super-Terminal“ – schau, ob es in der Nähe andere HarmonyOS-Geräte gibt.
2. Probiere die „Super-Zwischenablage“ aus: Kopiere einen Text in die Zwischenablage und ziehe ihn in der Notizen-App wieder heraus.
3. : Vom linken oder rechten Bildschirmrand nach innen wischen und halten, um die Seitenleiste zu öffnen; eine App antippen, um sie als schwebendes Fenster zu öffnen.
4. Datenschutz
:::
