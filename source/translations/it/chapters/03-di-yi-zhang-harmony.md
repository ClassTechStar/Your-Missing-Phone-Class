---
id: di-yi-zhang-harmony
part: ji-chu-pian
nav:  Appendice al Capitolo 1: Speciale sistema operativo HarmonyOS
toc: default
kind: supplement
---

### Appendice al Capitolo 1: Speciale sistema operativo HarmonyOS

{class="chapter-intro mb-4"}
HarmonyOS è un sistema operativo sviluppato autonomamente da Huawei; dalla sua release nel 2019 ha attraversato diverse versioni principali. Non è semplicemente "un altro sostituto di Android", ma una nuova specie con una filosofia di design unica. Scopriamo insieme questo sistema operativo in ascesa.

#### 1. Cos'è HarmonyOS? Perché è diverso?

La filosofia centrale di HarmonyOS è "l'interconnessione di tutte le cose". A differenza dei sistemi operativi tradizionali che servono principalmente un singolo dispositivo, HarmonyOS è stato progettato fin dall'inizio considerando la collaborazione multi-dispositivo.

L'<strong>architettura distribuita</strong> è l'anima di HarmonyOS. In parole semplici, può virtualizzare più dispositivi in un "super terminale". Il tuo telefono, tablet, computer, orologio e televisione non sono più entità isolate, ma "organi" di un insieme che possono richiamare le capacità l'uno dell'altro.

Un esempio: stai guardando un video sul telefono e vuoi vederlo su uno schermo più grande; il modo tradizionale è lo screen mirroring, mentre su HarmonyOS puoi "trasferire" direttamente il video al televisore per continuare a guardarlo, e il telefono diventa un telecomando. Non è un semplice screen mirroring, ma l'applicazione stessa che viene eseguita attraverso i dispositivi.

#### 2. HarmonyOS 4.3: la versione matura basata su AOSP

HarmonyOS 4.3 è la versione attualmente ampiamente distribuita sui telefoni Huawei. Va precisato che HarmonyOS 4.3 è compatibile con il framework di codice dell'Android Open Source Project (AOSP), quindi può essere pienamente compatibile con le applicazioni Android — la maggior parte delle app che scarichi da Huawei AppGallery sono essenzialmente ancora applicazioni Android, eseguite tramite il livello di compatibilità di HarmonyOS. Tuttavia HarmonyOS 4.3 non è un semplice "rivestimento" di Android: sulla base di AOSP aggiunge molte tecnologie sviluppate autonomamente da Huawei, come le capacità distribuite e il motore Ark.

##### Caratteristiche principali:

- <strong>Compatibilità con app Android</strong>: essendo basato su AOSP, HarmonyOS 4.3 può eseguire normalmente quasi tutte le applicazioni Android, senza che l'utente percepisca differenze.
- <strong>Motore Ark</strong>: compilatore e runtime sviluppati autonomamente da Huawei, che rendono le app più fluide e meno energivore. Rispetto alle versioni precedenti, la fluidità è nettamente migliorata.
- <strong>Super terminale</strong>: nel centro di controllo puoi vedere intuitivamente gli altri dispositivi HarmonyOS nelle vicinanze e connetterli con un drag-and-drop. Il telefono può usare tastiera e mouse del computer, il tablet può usare la fotocamera del telefono: tutto molto comodo.
- <strong>Schede di servizio</strong>: simili ai widget di iOS, ma più flessibili. Puoi scorrere verso l'alto sull'icona di un'app per espandere la scheda e mostrare le informazioni chiave senza aprire l'app.
- <strong>Modalità Pure</strong>: consente l'installazione di applicazioni solo dall'App Store ufficiale, riducendo il rischio di malware.
- <strong>Centro privacy</strong>: gestione centralizzata dei permessi delle app e consultazione del registro dei comportamenti delle app.

##### Caratteristiche dell'interfaccia utente:

- <strong>Blocco schermo magazine</strong>: la schermata di blocco mostra immagini curate e articoli; scorri per entrare nella home.
- <strong>Schede universali</strong>: le icone sulla home possono essere espanse in schede per mostrare più informazioni.
- <strong>Super clipboard</strong>: un'area di archiviazione temporanea in cui puoi salvare testo, immagini e file per poi trascinarli in qualsiasi app. La condivisione tra app diventa estremamente fluida.
- <strong>Ricerca intelligente</strong>: ricerca globale su app, file, impostazioni e pagine web.

#### 3. HarmonyOS NEXT (HarmonyOS 6): il vero punto di partenza del sistema operativo autonomo di Huawei

HarmonyOS NEXT (HarmonyOS NEXT 5.0) si distingue in modo fondamentale da HarmonyOS 4.3: adotta il microkernel HarmonyOS sviluppato autonomamente da Huawei, non dipende più dal kernel Linux né dal codice AOSP e <strong>non supporta più direttamente le applicazioni Android</strong>. È il passo chiave che porta HarmonyOS dalla "forma transitoria compatibile con Android" a un "sistema operativo completamente indipendente".

##### Cambiamenti principali:

- <strong>Kernel completamente autonomo</strong>: HarmonyOS NEXT utilizza un kernel sviluppato autonomamente da Huawei, senza più alcun codice AOSP. Il sistema è più snello, più sicuro e più efficiente.
- <strong>Non supporta più le applicazioni Android</strong>: è il cambiamento più grande. HarmonyOS NEXT può eseguire solo applicazioni HarmonyOS native e non può installare o eseguire file APK. Prima di aggiornare, verifica che le app che usi abitualmente abbiano già una versione HarmonyOS nativa.
- <strong>Ecosistema di applicazioni native</strong>: Huawei sta spingendo al massimo gli sviluppatori a migrare le app sulla piattaforma HarmonyOS nativa. Attualmente le app principali come WeChat, Alipay, Taobao ecc. hanno già rilasciato versioni HarmonyOS native, ma alcune applicazioni di nicchia potrebbero non essere ancora state adattate.
- <strong>Architettura di sicurezza Star Shield</strong>: un sistema di sicurezza completamente nuovo, con protezione a catena dall'hardware al software. Supporta un controllo dei permessi più granulare, ad esempio la "posizione approssimativa" — l'app può sapere solo all'incirca dove ti trovi, non la posizione esatta.
- <strong>Integrazione profonda dell'AI</strong>: capacità AI a livello di sistema, non solo in un'app specifica. Ad esempio i sottotitoli AI possono tradurre i video in tempo reale e il ritaglio AI riconosce intelligentemente il soggetto.
- <strong>Trasferimento fluido tra dispositivi</strong>: capacità distribuite ulteriormente avanzate. Lo stato delle app può passare senza soluzione di continuità tra dispositivi: il documento che stai modificando sul telefono si apre automaticamente sul computer quando ti avvicini a esso.
- <strong>Meta-servizi</strong>: servizi leggeri utilizzabili senza installazione. Ad esempio, scansionando un QR code si apre direttamente una determinata funzione, senza dover prima scaricare un'app.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Da leggere prima di aggiornare a HarmonyOS NEXT

{class="mt-1"}
Dopo l'aggiornamento a HarmonyOS NEXT, il tuo telefono non potrà più eseguire applicazioni Android. Assicurati di verificare prima dell'aggiornamento: ① che le app che usi abitualmente abbiano una versione HarmonyOS nativa; ② che non ci siano scenari di lavoro o di vita quotidiana che dipendano necessariamente da applicazioni Android. Dopo l'aggiornamento non è possibile tornare a HarmonyOS 4.3.
:::

##### Cambiamenti nella logica operativa:

- <strong>Navigazione gestuale</strong>: scorrimento dal bordo sinistro/destro per tornare indietro, scorrimento verso l'alto dal bordo inferiore per tornare alla home, scorrimento verso l'alto e pausa per aprire il multitasking.
- <strong>Multi-finestra intelligente</strong>: supporta schermo diviso, finestre fluttuanti, vista parallela e altre modalità multitasking.
- <strong>Chiamate Celia</strong>: servizio di videochiamata di Huawei, supporta condivisione schermo, miglioramento del volto e sfondo sfocato.

#### 4. L'ecosistema HarmonyOS: dispositivi e applicazioni

HarmonyOS non è solo un sistema per telefoni, ma un ecosistema che copre molteplici dispositivi.

##### Tipi di dispositivi supportati:

- <strong>Telefono e tablet</strong>: dispositivi principali, con le funzionalità più complete.
- <strong>Orologi smart e braccialetti</strong>: funzionamento autonomo o in collaborazione con il telefono.
- <strong>Smart screen (TV)</strong>: centro di intrattenimento domestico.
- <strong>Casse intelligenti</strong>: punto di accesso per l'interazione vocale.
- <strong>Automobili</strong>: abitacolo HarmonyOS, esperienza di cockpit intelligente.
- <strong>Casa intelligente</strong>: frigorifero, condizionatore, lavatrice ecc.

##### Stato attuale dell'ecosistema app:

L'AppGallery di HarmonyOS contiene già milioni di applicazioni e le app principali sono sostanzialmente tutte presenti. Huawei sta anche promuovendo attivamente gli sviluppatori per creare applicazioni HarmonyOS native. A metà del 2026, applicazioni di punta come WeChat, Alipay, Taobao, Douyin, Meituan, JD hanno già rilasciato versioni HarmonyOS native e l'uso quotidiano è sostanzialmente senza ostacoli. Alcune applicazioni di nicchia e settoriali potrebbero essere ancora in fase di adattamento; prima dell'aggiornamento è consigliabile verificare se le app che usi abitualmente sono già supportate.

#### 5. Consigli pratici per HarmonyOS

- <strong>Super terminale</strong>: scorri verso il basso dall'angolo in alto a destra per aprire il centro di controllo, tocca "Super terminale" per vedere gli altri dispositivi nelle vicinanze e connetterli con un drag-and-drop.
- <strong>Super clipboard</strong>: tieni premuto su testo/immagini/file e seleziona "Copia nel clipboard", poi in un'altra app tieni premuto per incollare oppure trascina.
- <strong>Schede di servizio</strong>: scorri verso l'alto sull'icona di un'app per espandere la scheda; tieni premuto sulla scheda per ridimensionarla o aggiungerla alla home.
- <strong>Multi-finestra intelligente</strong>: scorri verso l'interno dal bordo sinistro/destro dello schermo e mantieni premuto per aprire la barra laterale; tocca un'app per aprirla come finestra fluttuante.
- <strong>Protezione della privacy</strong>: in Impostazioni > Privacy puoi consultare il registro d'uso dei permessi delle app e impostare la posizione approssimativa.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Note

{class="mt-1"}
HarmonyOS si aggiorna e si evolve continuamente; versioni diverse possono presentare alcune differenze. La descrizione di questo testo si basa sulle caratteristiche principali di HarmonyOS 4.3 e 6; per le funzionalità specifiche fai riferimento alla versione effettiva installata sul tuo telefono. Si consiglia di mantenere il sistema aggiornato per ottenere le ultime funzionalità e le patch di sicurezza.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Prova subito: scopri le funzionalità caratteristiche di HarmonyOS

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Apri il centro di controllo, trova "Super terminale" e vedi se ci sono altri dispositivi HarmonyOS nelle vicinanze.
2. Prova il "Super clipboard": copia un testo nel clipboard, poi trascinalo fuori nelle note.
3. Scorri verso l'alto sulle icone di alcune app che usi spesso per vedere cosa mostrano le loro schede di servizio.
4. Vai in Impostazioni > Privacy e controlla quali app hanno usato di recente permessi sensibili.
:::
