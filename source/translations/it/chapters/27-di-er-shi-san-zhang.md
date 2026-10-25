---
id: di-er-shi-san-zhang
num: 23
part: chao-yue-pian
nav: Capitolo 23: Pensiero informatico e prime nozioni di automazione
toc: default
kind: chapter
---

### Capitolo 23: Pensiero computazionale e introduzione all'automazione

{class="chapter-intro mb-4"}
Nei due capitoli precedenti abbiamo costruito un "muro di confine" di sicurezza attorno al telefono e ne abbiamo visto il "cervello IA" sempre più intelligente all'interno. Ora sblocchiamo una delle potenzialità ultime del telefono: fargli "pensare" come un programmatore e fargli completare automaticamente una sequenza di compiti che hai impostato. Potresti dire: "Non so scrivere codice, cosa c'entra con me?" Stai tranquillo, in questo capitolo non dovrai scrivere nemmeno una riga di codice — i telefoni moderni hanno abbassato la soglia della "programmazione" fino a renderla fattibile con semplici drag-and-drop.

#### 1. Cos'è davvero l'automazione?

In parole povere, l'automazione è: <strong>far fare al telefono una serie di cose automaticamente quando si verifica una certa condizione.</strong> Non devi operare manualmente ogni volta, né ricordarti cosa fare — il telefono giudica da solo il momento ed esegue da solo.

Un esempio: ogni mattina quando ti svegli devi disattivare manualmente la modalità Non disturbare, aprire WeChat per vedere i messaggi, aprire l'app del meteo per scegliere cosa metterti, aprire NetEase Cloud per far partire una canzone. Se impacchetti questi passaggi in un flusso di automazione, impostato su "esegui automaticamente ogni mattina alle 7", al risveglio ti basta prendere il telefono: è già tutto pronto. Bello, no?

L'automazione in sostanza è una catena logica "se... allora...", l'if-else della programmazione. Padroneggiare questo modo di pensare renderà molto più ordinato il tuo approccio ai problemi, anche se non scriverai mai una riga di codice. Elementi chiave:

1. <strong>Condizione di innesco</strong>: quando inizia? Può essere "ogni mattina alle 7", "quando mi connetto al Wi-Fi di casa", "quando arrivo in un certo luogo", "quando la batteria del telefono scende sotto il 20%".
2. <strong>Azione da eseguire</strong>: cosa fare concretamente? Può essere inviare un messaggio WeChat, aprire un'app, regolare il volume, cambiare sfondo, riprodurre musica, inviare una notifica... Quasi tutto ciò che fai manualmente sul telefono, l'automazione può farlo.
3. <strong>Logica intermedia</strong> (facoltativa ma potente): se la situazione è A fai X, altrimenti fai Y. Ad esempio "se è un giorno lavorativo riproduci un podcast di notizie, nel fine settimana riproduci musica": si chiama diramazione condizionale.

#### 2. "Comandi rapidi" di iOS — lo strumento di automazione per gli utenti Apple

L'app "Comandi rapidi" (Shortcuts) di Apple è preinstallata, non serve scaricarla. Il suo concetto chiave è assemblare le varie operazioni come mattoncini. Vediamo alcuni concetti chiave:

- <strong>"Comando rapido"</strong>: un flusso di automazione completo, che si può eseguire con un tocco o attivare via voce con Siri. Ad esempio, dicendo "Ehi Siri, modalità rientro", esegue automaticamente la sequenza di operazioni che hai impostato.
- <strong>"Automazione"</strong>: comando eseguito automaticamente in base a un innesco, senza doverlo attivare manualmente. Ad esempio "quando il telefono si connette al Bluetooth dell'auto, apri automaticamente l'app mappe". Le automazioni si impostano nella scheda "Automazione", separata dai "Comandi rapidi".
- <strong>"Azione"</strong>: l'unità di esecuzione minima. Aprire un'app è un'azione, inviare un messaggio è un'azione, ottenere il meteo è un'azione, regolare la luminosità è un'azione. Puoi concatenare centinaia o migliaia di azioni.

Ecco alcuni esempi davvero utili, seguili una volta e capirai:

##### Esempio 1: "Flusso buongiorno" con un tocco

Ogni mattina tocca una volta (o dì a Siri "buongiorno") e il telefono automaticamente: ottiene il meteo di oggi → legge a voce alta meteo e temperatura → mostra gli impegni di calendario di oggi → apre l'app musicale che usi di più e inizia la riproduzione. Passaggi: nuovo comando rapido → aggiungi azione "Ottieni meteo attuale" → aggiungi "Leggi testo" → aggiungi "Ottieni eventi calendario" → aggiungi "Mostra promemoria" → aggiungi "Apri app" e scegli NetEase Cloud Music. Tutto qui, tutto tramite drag-and-drop.

##### Esempio 2: "Modalità risparmio energia" automatica

Nella scheda "Automazione", crea una nuova automazione → scegli "Livello batteria" → imposta "sotto il 30%" → aggiungi le azioni "Imposta modalità basso consumo su attiva", "Riduci luminosità schermo al 30%", "Disattiva Bluetooth". Da quel momento, quando la batteria scende sotto il 30% il telefono entra automaticamente in modalità risparmio, senza che tu debba preoccupartene.

##### Esempio 3: registrazione contabile automatica dopo scansione

Ogni volta che paghi scansionando il codice con WeChat/Alipay, il telefono legge la notifica di pagamento e registra automaticamente importo e esercente in una nota o in un foglio Numbers. Questo richiede l'uso dell'innesco "ricezione SMS/notifica" nell'automazione dei Comandi rapidi (in iOS 17+ è supportata la lettura delle transazioni Wallet), combinato con l'azione "Aggiungi a Numbers". Per chi vuole tenere i conti ma è troppo pigro per farlo a mano, è una salvezza.

C'è anche un uso ingegnoso che molti non conoscono: puoi aggiungere un comando rapido alla schermata Home, trasformandolo in un'icona app. Ad esempio, crea un comando rapido "Taxi per casa", metti l'icona sul desktop: con un tocco apre DiDi e imposta automaticamente la destinazione su casa, molto più veloce che aprire l'app e digitare a mano.

#### 3. Automazione Android — Tasker e i suoi amici

Sul fronte Android la situazione è un po' più complessa, ma anche il tetto è più alto. Iniziamo dal semplice:

##### Livello base: auto-clicker

Molti telefoni Android integrano un "auto-clicker" o lo si può scaricare dallo store. Il principio è semplicissimo: tu operi a mano una volta, lui registra le coordinate dei tocchi e gli intervalli, poi li riproduce ad alta velocità. Ad esempio, se un'app offre un premio giornaliero di check-in, registri il flusso una volta e poi lo riproduci ogni giorno in automatico. Svantaggio: riconosce solo le coordinate, se il layout dell'interfaccia cambia (ad esempio compare una pubblicità), clicca nel punto sbagliato.

##### Livello avanzato: Tasker — il re dell'automazione Android

Tasker è considerato lo strumento di automazione più potente su Android, da anni in vetta alle classifiche. A dire il vero ha una curva di apprendimento un po' ripida e l'interfaccia non è bellissima, ma una volta imparato ti sembrerà che il telefono sia improvvisamente onnipotente. Anche il cuore di Tasker è il modello "innesco → task":

- <strong>Profilo (Profile)</strong>: definisce "quando si innesca". Le condizioni di innesco possono essere tempo, luogo, stato di connessione Wi-Fi, connessione Bluetooth, ricezione di una notifica specifica, stato della batteria, orientamento dello schermo... Le condizioni supportate da Tasker sono tantissime, decine.
- <strong>Task</strong>: definisce "cosa fare dopo l'innesco". Un task può contenere più azioni, eseguite in sequenza. I tipi di azione includono: regolazione di impostazioni di sistema (volume, luminosità, Wi-Fi, Bluetooth, modalità aereo), invio di SMS, richieste HTTP, esecuzione di comandi Shell, controllo della riproduzione multimediale, comparsa di finestre di dialogo, ecc.

Ecco alcuni scenari classici e pratici per Tasker:

- <strong>Wi-Fi automatico a casa</strong>: imposta come innesco "connessione a una specifica cella" (perché vicino a casa ti colleghi a una cella fissa) → task "attiva Wi-Fi". Senza GPS e senza consumare batteria, il telefono attiva il Wi-Fi appena entri nel quartiere.
- <strong>Modalità riunione</strong>: innesco "il titolo dell'evento di calendario contiene 'riunione'" → task "imposta modalità silenziosa, azzera il volume multimediale, rispondi automaticamente a WeChat (richiede plug-in)". Non dovrai più preoccuparti del telefono che suona all'improvviso durante una riunione.
- <strong>Protezione occhi notturna</strong>: innesco "orario 22:00-06:00" → task "attiva modalità di protezione occhi, abbassa la luminosità al 20%, imposta lo schermo in bianco e nero (modalità scala di grigi)". Lo schermo in bianco e nero è formidabile contro la voglia di scrollare i video brevi: quando l'immagine diventa grigia, non ti va più di farlo.
- <strong>Podcast automatico all'inserimento delle cuffie</strong>: innesco "inserimento cuffie cablate / connessione cuffie Bluetooth" → task "apri l'app Xiaoyuzhou e avvia l'ultimo episodio". Basta indossare le cuffie per ascoltare, senza sbloccare il telefono e cercare l'app.

Se Tasker ti sembra troppo difficile, prova suo "fratello" semplificato: <strong>MacroDroid</strong>. L'interfaccia è molto più amichevole, con tanti modelli, adatto a chi non vuole sbattersi. Inoltre, molti sistemi Android cinesi (MIUI di Xiaomi, HarmonyOS di Huawei, ColorOS di OPPO) integrano funzioni di "scenari" o "assistente intelligente": pur non essendo potenti come Tasker, per l'automazione quotidiana sono più che sufficienti.

#### 4. Applicazioni quotidiane del pensiero automatizzato

Il guadagno più grande dall'imparare l'automazione non è risparmiare quel po' di tempo, ma <strong>cambiare il modo in cui pensi ai problemi</strong>. Una volta abituato al modello mentale "se si verifica X, fai automaticamente Y", ti accorgerai che un sacco di lavoro ripetitivo nella vita può essere eliminato. Ad esempio:

- Ogni volta che scatti una foto, esegue automaticamente il backup su cloud e poi comprime la foto locale per risparmiare spazio.
- Ogni mattina legge automaticamente gli impegni del giorno dal calendario e genera un testo inviato alla famiglia tramite WeChat.
- Alla ricezione di un SMS di consegna pacco, aggiunge automaticamente un "ritirare il pacco" alle note delle cose da fare.
- Quando la batteria è carica al 100%, avvisa con un promemoria vocale di staccare il caricabatterie (per evitare di danneggiarla con sovraccarichi).
- All'orario di fine giornata, se sei ancora vicino all'ufficio (tramite localizzazione della cella), ricorda automaticamente "è ora di staccare".

Sembrano cose avanzate, ma se padroneggi i due concetti di base "innesco + azione", con i Comandi rapidi o Tasker puoi realizzarle tutte. La chiave è <strong>prima renderti conto che "questa cosa si può automatizzare"</strong> — molti non è che non siano capaci, è che non ci pensano proprio.

#### 5. Guida alle insidie: problemi comuni dell'automazione

L'automazione non è tutta rose e fiori; alcune trappole le ho già esplorate per te:

- <strong>L'innesco di posizione può non funzionare bene</strong>: l'innesco "arrivo/partenza da una posizione" di iOS usa la tecnologia dei geofence, la precisione dipende dal segnale GPS e dall'ottimizzazione del sistema. A volte si innesca solo dieci minuti dopo che sei arrivato a casa. Meglio usare l'innesco su connessione Wi-Fi o cella al posto di quello di posizione: più affidabile e più risparmiatore di batteria.
- <strong>L'"automazione" dei Comandi rapidi richiede autorizzazione</strong>: in iOS, la maggior parte degli inneschi nella scheda "Automazione" richiede conferma manuale per essere eseguita (meccanismo di sicurezza di iOS). Ma connessione Wi-Fi, connessione Bluetooth e spegnimento della sveglia sono inneschi che possono girare davvero in automatico, senza conferma.
- <strong>Tasker richiede l'attivazione dell'accessibilità</strong>: molte funzioni avanzate (come la simulazione dei tocchi) richiedono l'autorizzazione del servizio di accessibilità, che fa comparire una notifica permanente nelle impostazioni. È una scelta di sicurezza di Android, non rimovibile.
- <strong>Non rendere l'automazione troppo complessa</strong>: alle prime armi inizia con piccoli flussi da "2-3 azioni". Non lanciarti subito in un super-flusso da 20 passaggi — diventeresti pazzo a debuggarlo.

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Suggerimento: la postura giusta per iniziare con l'automazione

{class="mt-1"}
Prenditi 5 minuti per pensare: quali sono le 3 cose che ripeti di più sul telefono ogni giorno? Ad esempio le operazioni di routine mattutine, le abitudini dopo aver collegato le cuffie Bluetooth, le impostazioni prima di uscire... Parti da queste piccole cose ad alta frequenza e crea per ciascuna una semplice automazione. Anche se ogni automazione ti risparmia solo 5 secondi, nel lungo periodo è tanto. E la soddisfazione di vedere funzionare il risultato crea davvero dipendenza.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Allenati: tre sfide di automazione per principianti

{class="mt-1 mb-2"}
Scegli quella più adatta a te e completala: a quel punto avrai imparato le basi:

{class="list-decimal pl-6 mt-1 space-y-1"}
1. <strong>Sfida 1: automazione buongiorno</strong>: iOS: in Comandi rapidi crea un nuovo comando → aggiungi "Ottieni meteo attuale" → "Leggi testo" → "Apri app e scegli NetEase Cloud". Fatto, puoi dire a Siri "buongiorno" per attivarlo. Android: in Tasker crea un nuovo task → aggiungi "Ottieni meteo" → "Leggi" → "Apri app" → imposta l'innesco su ogni giorno alle 7:00.
2. <strong>Sfida 2: risparmio energia automatico a batteria bassa</strong>: iOS: scheda Automazione → nuovo → "Livello batteria" → sotto il 25% → aggiungi "Imposta modalità basso consumo su attiva" + "Imposta luminosità al 25%". Android: Tasker nuovo Profile → Stato → Alimentazione → Batteria 0-25% → task "attiva modalità risparmio" + "abbassa luminosità".
3. <strong>Sfida 3: navigazione automatica al collegamento del Bluetooth auto</strong>: iOS: Automazione → nuovo → "Bluetooth" → scegli il Bluetooth dell'auto → aggiungi "Apri app e scegli Amap" + "Volume multimediale all'80%". Android: Tasker → Profile → Stato → Bluetooth connesso → scegli il Bluetooth dell'auto → task "apri Amap" + "alza volume multimediale".
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Caso 3: automazione del "flusso buongiorno"

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>Scenario</strong>: ogni giorno alle 7:00 annuncio automatico del meteo + disattivazione silenzioso + apertura notizie.
- <strong>Passaggi</strong>: iOS: Comandi rapidi → Automazione → innesco orario → aggiungi "Ottieni meteo" + "Imposta volume" + "Apri app"; Android: MacroDroid → trigger (orario 7:00) → azioni (volume multimediale / apri URL / TTS legge il meteo).
- <strong>Risultato atteso</strong>: realizzabile senza installazioni, abbassa la soglia di ingresso.
:::
