---
id: di-wu-shi-jiu-zhang
num: 59
part: ios-kai-fa-pian
nav: Capitolo 59: Conoscere iOS — L'ecosistema Apple e quello dello sviluppo
toc: default
kind: chapter
---

### Capitolo 59: Conoscere iOS — l'ecosistema Apple e quello degli sviluppatori

{class="chapter-intro mb-4"}
Congratulazioni per questa decisione: da «persona che usa l'iPhone» a «persona che scrive app per iPhone». Prima di metterci le mani, spieghiamo la mappa sul tavolo: da dove viene iOS? Cosa significa per uno sviluppatore il «giardino recintato» di Apple? Cosa succede, fra i tuoi tasti premuti e il telefono dell'utente, lungo il tragitto di un'app?

#### 1. Le origini di iOS: un telefono che cambia un settore

Nel gennaio 2007 Jobs tirò fuori il primo iPhone durante una conferenza. All'epoca non supportava nemmeno le app di terze parti: solo nel 2008 Apple lanciò App Store e iPhone SDK, aprendo agli sviluppatori di tutto il mondo la porta del software per iPhone. In quel momento nacque l'«economia delle app»: oggi su App Store ci sono milioni di applicazioni e le quote versate agli sviluppatori hanno superato nel complesso le centinaia di miliardi di dollari.

Il sistema stesso evolve: all'inizio si chiamava iPhone OS, nel 2010 diventò iOS; i numeri di versione sono saliti fino a iOS 17 (2023), poi nel 2025 Apple ha cambiato nome seguendo l'anno — iOS 26 è uscito nel 2025 e, ad agosto 2026, la versione corrente è iOS 27. Il nome cambia, ma una cosa non è mai cambiata: le abitudini di spesa degli utenti iOS e la fama di qualità del software sono riconosciute come le migliori dell'ecosistema mobile — per la stessa app, i guadagni su iOS spesso superano nettamente quelli su Android.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tappa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Anno</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Che cosa è contato per gli sviluppatori</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Debutto di App Store</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2008</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Si apre l'ecosistema di sviluppo di terze parti</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lancio di Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2014</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Entra in scena il linguaggio moderno per iOS</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lancio di SwiftUI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2019</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Framework dichiarativo per le interfacce, il filo conduttore di questo libro</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">iOS 26 (il primo anno col nuovo nome)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2025</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Il nome segue l'anno; Apple Intelligence integrata a fondo</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">iOS 27</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2026</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Versione più recente attuale (il riferimento di questo libro)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Le date chiave dello sviluppo iOS (aggiornato ad agosto 2026)

#### 2. Il giardino recintato: le «regole» e i «dividendi» dell'ecosistema Apple

L'ecosistema Apple viene spesso descritto come un «giardino recintato» (Walled Garden): tante regole e controlli stretti. Le app passano la revisione prima di essere pubblicate, per sviluppare servono Mac e Xcode, e la distribuzione passa in grande parte per App Store. Sembra angusto? Per gli sviluppatori, però, queste regole si scambiano con vantaggi che valgono oro sonante:

- Frammentazione dei dispositivi minima: i modelli di iPhone sono quelli lì, con schermi e versioni di sistema molto uniformi — supportando 5 modelli copri il 95% degli utenti (su Android potrebbero servire decine);
- Tasso di aggiornamento del sistema altissimo: a poche settimane dal rilascio di un nuovo sistema si aggiorna il 70-80% degli utenti, così le API nuove si possono usare con coraggio, senza pensare al «vecchio sistema di cinque anni fa»;
- Gli utenti pagano volentieri: chi usa App Store spende più volentieri per app e acquisti interni;
- La revisione è severa, ma lo store è pulito: pochi cloni e pochi software molesto, i buoni prodotti si fanno notare più facilmente.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attenzione: prima chiariamo i costi

{class="mt-1"}
Lo sviluppo iOS ha una soglia dura: serve un Mac (Xcode esiste solo su macOS) e per pubblicare serve un account sviluppatore da 99 dollari l'anno (con l'account gratuito da sviluppatore individuale si può fare il debug su un dispositivo vero in locale, ma non pubblicare). Valuta bene questa spesa prima di partire — la buona notizia è che per studiare l'account gratuito basta ed eccede; ne parliamo al capitolo 60.
:::

#### 3. Con che linguaggio si scrive: Objective-C o Swift?

Anche la storia dello sviluppo iOS ha avuto due «protagonisti». Objective-C è il patriarca fondatore — si è usato dal 2008 al 2014; Swift è il linguaggio nuovo pubblicato da Apple nel 2014, evoluto poi fino a Swift 6 (uscito nel 2024, con controlli di concorrenza severi), e nel 2026 i progetti nuovi usano ormai quasi tutti Swift.

A te che parti da zero una frase onesta: impara direttamente Swift e di Objective-C non guardare nemmeno — salvo che, una volta assunto, tu debba mantenere codice ereditato di dieci anni fa. I pregi di Swift: sintassi nitida (niente punto e virgola né file header dell'epoca C), il meccanismo dei valori opzionali (Optional) che cancella a livello di linguaggio il «crash da puntatore nullo», la collaborazione senza attriti con SwiftUI e Swift Playgrounds su iPad per imparare giocando.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Stile Objective-C (reliquia antica)

{class="font-mono text-xs leading-relaxed"}
NSString *name = @"Mario"; [name stringByAppendingString:@"ciao"]; // parentesi quadre + puntatore + punto e virgola: il tris
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Stile Swift (moderno e nitido)

{class="font-mono text-xs leading-relaxed"}
var name = "Mario" name += "ciao" // diretto come un linguaggio naturale
:::
:::

#### 4. Come nasce un'app?

Come su tutte le piattaforme, anche un'app iOS nasce lungo una catena di montaggio. La versione Apple però ha due «controlli di sicurezza» in più:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-lightbulb mr-1"></i> Idea</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center">📐 Progettazione (interfaccia + funzioni)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-keyboard mr-1"></i> Scrivi codice (Swift + SwiftUI)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hammer mr-1"></i> Compilazione e firma</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Test (emulatore + dispositivo reale)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-stamp mr-1"></i> Revisione Apple</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> Pubblicato sull'App Store</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 1: il percorso completo di un'app iOS, dall'idea allo store (nota la tappa in più della «revisione»)
:::

I concetti chiave del percorso:

- Firma (Signing): ogni app iOS va «firmata» per potersi installare — la prova che «questo pacchetto viene da te e non è stato manomesso». Nella fase di studio Xcode firma da solo col tuo Apple ID; per la pubblicazione si usa il certificato da sviluppatore. Ne parliamo per esteso al capitolo 67.
- Simulatore (Simulator): un iPhone virtuale sul Mac, il campo di battaglia principale di sviluppo e debug. Gira sulla CPU del Mac, per questo è fluidissimo, con un'esperienza molto più gradevole dell'emulatore Android.
- TestFlight: lo strumento ufficiale Apple per la distribuzione delle beta — prima della pubblicazione puoi inviare la versione di prova a fino a 10.000 utenti tester, che la installano con l'app TestFlight. Un'eleganza che appartiene in esclusiva all'ecosistema iOS.

#### 5. Lo stack iOS in panoramica: la tua «lista delle armi»

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Livello</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Scelta corrente (2026)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">A cosa serve</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Linguaggio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift 6</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Il linguaggio per la logica</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interfaccia</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI + le linee guida di design Apple (HIG)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Disegnare le interfacce col codice (il filo conduttore del libro)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Architettura</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MVVM + @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tenere separate interfaccia e logica</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Archiviazione dati</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData (database) + UserDefaults (impostazioni)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mettere i dati dentro il telefono</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rete</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession + async/await + Codable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Parlare col server</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Strumenti di build</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode Build System / xcodebuild</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Trasformare il codice in pacchetto installabile</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ambiente di sviluppo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode (solo macOS)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">L'IDE ufficiale Apple</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Lo stack iOS corrente del 2026 in breve

Hai notato? Questa lista è più corta di quella Android — perché Apple si «fa carico» di tante cose. Il prezzo di un ecosistema chiuso è la libertà, la ricompensa è la serenità: niente dubbi su quale libreria di rete o quale database scegliere, la soluzione ufficiale è quasi sempre la migliore.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mani in pasta: guarda la «fede Apple» del tuo telefono

{class="mt-1"}
Apri sull'iPhone [Impostazioni] → [Generali] → [Info] e annota tre cose: versione di iOS, nome del modello, spazio disponibile. Poi fai un giro libero per la pagina «Oggi» di App Store e osserva gli screenshot e i testi delle app di punta — da oggi il tuo sguardo sullo store passa da «utente» a «sviluppatore».
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riassunto del capitolo

- Nel 2008 debutta App Store e nasce l'«economia delle app»; nel 2026 la versione corrente è iOS 27
- Il conto del giardino recintato: tante regole, ma pochi dispositivi, versioni aggiornate, utenti disposti a pagare e uno store pulito
- La soglia dura: serve un Mac; per pubblicare serve l'account sviluppatore da 99 dollari/anno; per studiare basta l'account gratuito
- Come linguaggio, dritti su Swift; Objective-C resta per il solo codice ereditato
- La catena di montaggio ha un anello in più di Android: la revisione Apple; TestFlight è lo strumento perfetto per le beta
- Lo stack standard 2026: Swift 6 + SwiftUI + MVVM + SwiftData + URLSession + Xcode
:::
