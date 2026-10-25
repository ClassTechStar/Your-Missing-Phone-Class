---
id: di-yi-zhang
num: 01
part: ji-chu-pian
nav: Capitolo 1: Ciao, il mio computer personale
toc: default
kind: chapter
---

### Capitolo 1: Ciao, il mio computer personale

{class="chapter-intro mb-4"}
Il tuo cellulare, in realtà, è il supercomputer più personale che tu abbia in tasca. È innumerevoli volte più potente dei computer che hanno portato l'uomo sulla Luna, eppure riposa silenzioso nel palmo della tua mano. Oggi conosciamo a fondo questo "gigante silenzioso".

#### 1. "Cinque organi e sei viscere" dell'hardware del cellulare: analisi approfondita

Il cellulare è piccolo ma completo. Conosciamo uno per uno questi componenti di precisione, come in una lezione di anatomia.

##### 1. SoC (System on Chip): il "cervello + cuore" del cellulare

SoC sta per System on Chip, che si traduce in "infila l'intero sistema in un chip". Non è solo la CPU (Central Processing Unit), ma integra CPU, GPU (Graphics Processing Unit), NPU (Neural Processing Unit), ISP (Image Signal Processor), baseband (responsabile delle comunicazioni) e altro ancora.

È come costruire il municipio, la centrale elettrica, il centro comunicazioni e la stazione di polizia di una città tutti in un unico edificio: efficienza altissima.

##### CPU: il cuore del calcolo general-purpose

La CPU è il componente più centrale del SoC, responsabile della maggior parte dei compiti di calcolo. Le CPU dei cellulari usano l'architettura ARM; a differenza dell'architettura x86 dei PC, ARM si caratterizza per un set di istruzioni ridotto (RISC), con consumi più bassi, più adatta ai dispositivi mobili.

<strong>Design big.LITTLE della CPU</strong>: le CPU mobili moderne adottano diffusamente un'architettura "big.LITTLE" (tecnologia big.LITTLE di ARM), dividendo i core in livelli di prestazioni diversi:

- <strong>Super core / big core</strong>: prestazioni massime, si occupa dei compiti più pesanti. Ad esempio caricamento di giochi, avvio delle app, calcoli complessi. Frequenza più alta (3GHz+), ma anche consumi maggiori.
- <strong>Medium core</strong>: equilibrio prestazioni/consumi, gestisce compiti medi quotidiani. Scorrere Weibo, guardare video, cambiare app: se ne occupa principalmente lui.
- <strong>Small core / efficiency core</strong>: consumo minimo, per compiti leggeri in background. Standby, ascolto musica, ricezione messaggi, quasi non consuma batteria.

I tre livelli di core collaborano: lo scheduler di sistema assegna automaticamente in base al carico — i compiti leggeri ai small core per risparmiare, i lavori pesanti ai big core a tutta forza, poi si torna ai small core. Ecco perché il cellulare riesce a far girare fluidamente i giochi e a restare in standby tutto il giorno.

<strong>Caratteristiche delle architetture dei vari brand</strong>:

- <strong>Qualcomm Snapdragon 8 Elite</strong>: adotta l'architettura CPU Oryon proprietaria (derivata dall'acquisizione di Nuvia), 2 super core (4.32GHz) + 6 performance core (3.53GHz), tutti basati sul processo N3E di seconda generazione a 3nm di TSMC. Dice addio definitivo all'architettura pubblica ARM, con miglioramenti a salti sia single-core sia multi-core. GPU Adreno 830 con architettura a slice, prestazioni grafiche +40%; Hexagon NPU a circa 45 TOPS, prestazioni di inferenza AI +45%. (Nota: la versione custom Samsung Galaxy ha frequenze più alte, super core fino a 4.47GHz.)
- <strong>MediaTek Dimensity 9400</strong>: 1 super core (Cortex-X925, 3.62GHz) + 3 performance core (Cortex-X4, 3.3GHz) + 4 efficiency core (Cortex-A720, 2.4GHz), architettura full-big-core continuata, processo N3E di seconda generazione a 3nm di TSMC. GPU Immortalis-G925 (12 core), prestazioni di picco +41%, ray tracing +40%. Processore AI di ottava generazione NPU 890, supporta LLM on-device, training LoRA on-device e generazione video on-device.
- <strong>Apple A18 Pro</strong>: 2 performance core (circa 4.04GHz) + 4 efficiency core (circa 2.4GHz), processo N3E di seconda generazione a 3nm di TSMC. GPU a 6 core con ray tracing hardware-level, NPU a 16 core (circa 35 TOPS) che fornisce potenza di calcolo per AI on-device e Apple Intelligence. L'architettura proprietaria Apple resta leader in prestazioni single-core ed efficienza, e l'architettura a memoria unificata offre vantaggi di ampiezza di banda per l'inferenza AI.
- <strong>HiSilicon Kirin 9020 di Huawei</strong>: montato sulla serie Mate 70, adotta l'architettura CPU Taishan proprietaria, con capacità NPU e ISP continuamente potenziate, supporta 5.5G e comunicazione satellitare, rappresenta l'ultima svolta dei chip nazionali cinesi.

##### GPU: motore di rendering grafico

La GPU (Graphics Processing Unit) si occupa specificamente di grafica e calcolo parallelo. Ha molti più core della CPU (spesso centinaia o migliaia), ma ogni core ha funzioni relativamente semplici, adatte a gestire contemporaneamente grandi quantità di calcoli simili.

<strong>Flusso di rendering grafico</strong>:

1. <strong>Elaborazione dei vertici</strong>: calcolo delle coordinate di posizione di ogni vertice nel modello 3D.
2. <strong>Rasterizzazione</strong>: conversione della grafica 3D in pixel sullo schermo 2D.
3. <strong>Pixel shading</strong>: calcolo del colore, texture ed effetto di illuminazione per ogni pixel.
4. <strong>Composizione output</strong>: composizione di tutti i layer nell'immagine finale, inviata allo schermo.

<strong>Impatto della GPU sull'uso quotidiano</strong>: non solo giochi! Scorrimento delle interfacce, animazioni, riproduzione video, filtri foto, app AR dipendono tutti dalla GPU. Un cellulare con GPU debole può avere frame drop nello scorrimento e crash nei giochi.

<strong>GPU dei vari brand</strong>: Qualcomm usa la GPU Adreno proprietaria; MediaTek usa la GPU ARM Mali; Apple usa una GPU proprietaria, con prestazioni ed efficienza entrambe benchmark del settore.

##### NPU: motore di accelerazione AI

La NPU (Neural Processing Unit) è un processore progettato specificamente per il calcolo delle reti neurali. Rispetto a CPU e GPU, la NPU è più efficiente e consuma meno nei task AI.

<strong>Modalità di calcolo delle reti neurali</strong>: il calcolo principale della NPU è la moltiplicazione matriciale e la convoluzione — i calcoli più basilari e frequenti nelle reti neurali. Con ottimizzazioni hardware-level, la NPU può parallelizzare grandi quantità di calcoli matriciali, decine di volte più veloce della CPU e con consumi molto più bassi.

<strong>Flusso di elaborazione AI</strong>:

1. <strong>Input dati</strong>: immagini della fotocamera, audio del microfono, dati dei sensori, ecc.
2. <strong>Pre-elaborazione</strong>: regolazione di formato e dimensione dei dati per adattarli ai requisiti di input della rete neurale.
3. <strong>Inferenza</strong>: la NPU carica il modello addestrato, esegue il calcolo forward sui dati di input e produce il risultato.
4. <strong>Post-elaborazione</strong>: converte l'output AI in risultati utilizzabili, come coordinate dei volti, contenuto testuale, etichette di scena.

<strong>Scenari applicativi reali</strong>:

- <strong>Fotografia computazionale</strong>: sintesi notturna, ritratto con sfondo sfocato, elaborazione HDR, bellezza AI.
- <strong>Assistente vocale</strong>: riconoscimento vocale, comprensione del linguaggio naturale, sintesi vocale.
- <strong>Traduzione in tempo reale</strong>: sottotitoli AI, traduzione conversazionale.
- <strong>Riconoscimento intelligente</strong>: riconoscimento testo (OCR), riconoscimento oggetti, riconoscimento scene.
- <strong>LLM on-device</strong>: gli ultimi chip di punta supportano già l'esecuzione on-device di piccoli modelli AI (livello parametri 7B), per dialoghi AI offline, riassunto documenti, scrittura intelligente. L'Hexagon NPU dello Snapdragon 8 Elite ha circa 45 TOPS, l'NPU 890 del Dimensity 9400 supporta anch'esso LLM on-device (velocità di inferenza LLM +80%), la NPU a 16 core dell'A18 Pro di Apple fornisce circa 35 TOPS.
- <strong>Elaborazione immagini AI</strong>: rimozione AI (cancellazione con un tocco dei passanti nelle foto), espansione AI (estensione dei bordi dell'immagine), conversione stile AI, generazione immagini da testo, ecc.

##### ISP: Image Signal Processor

L'ISP elabora i dati grezzi provenienti dalla fotocamera, trasformando il segnale luminoso in belle foto.

<strong>Come valutare le prestazioni?</strong> Guarda il modello! Apple A18 Pro, Qualcomm Snapdragon 8 Elite, MediaTek Dimensity 9400, Huawei Kirin 9020 sono tutti di livello flagship. Fascia media: Snapdragon 8s Gen3/7+ Gen3, Dimensity 8400. Non guardare solo il numero di core: architettura e processo (nanometri) contano di più. Il processo a 3nm è oggi il più avanzato, con un'efficienza molto superiore a 5nm e 4nm.

##### 2. RAM: banco di lavoro temporaneo

La RAM è come la tua scrivania: più è grande, più documenti puoi aprire contemporaneamente. 12GB è lo standard attuale, 16GB per utenti intensivi, 24GB+ per gamer e geek.

Anche il tipo di RAM è importante: LPDDR5 è più veloce ed efficiente di LPDDR4X. Apple, pur avendo RAM ridotte, ottimizza bene il sistema, quindi sembra "sufficiente".

<strong>Cosa succede se la RAM non basta?</strong> Le app vengono killate in background dal sistema e al cambio richiedono un nuovo caricamento. Ecco perché a volte, passando a WeChat, il gioco scompare.

##### 3. Storage (ROM/flash): magazzino a lungo termine

Lo storage è come la tua libreria: dove stanno tutte le foto, i video, le app. Lo standard attuale è UFS 3.1 o UFS 4.0, molto più veloce del vecchio eMMC.

<strong>Perché la velocità dello storage conta?</strong> Determina la velocità di apertura delle app, di caricamento dei giochi, di salvataggio delle foto. Col tempo, storage lento rende il cellulare sempre più laggy.

##### 4. Schermo: i tuoi occhi

Lo schermo è la finestra principale di interazione tra te e il cellulare; la sua qualità influisce direttamente sull'esperienza.

- <strong>Materiale</strong>: OLED colori vivaci, alto contrasto, più efficiente (i pixel non emettono luce quando mostrano nero), ma a bassa luminosità può avere flicker fastidioso per gli occhi; LCD più riposante, costo più basso, ma contrasto e colore inferiori all'OLED.
- <strong>Risoluzione</strong>: 1080P è lo standard, 2K più nitido ma più energivoro. Il concetto di "retina display" di Apple è: a una certa distanza, l'occhio umano non distingue i pixel.
- <strong>Refresh rate</strong>: 60Hz standard, 90Hz/120Hz più fluido, scorrimento setoso. Alto refresh rate consuma di più, quindi molti cellulari supportano refresh rate adattivo (LTPO), regolato dinamicamente in base al contenuto.
- <strong>Touch sampling rate</strong>: influisce sulla velocità di risposta al tocco; i gamer devono farci caso, più alto è, più il telefono è reattivo.
- <strong>Modalità di dimming</strong>: il dimming DC è più riposante del dimming PWM, a bassa luminosità affatica meno gli occhi. Oggi molti cellulari supportano PWM ad alta frequenza, sempre per proteggere gli occhi.

##### Tecnologia HDR dello schermo

L'HDR (High Dynamic Range) consente allo schermo di mostrare contemporaneamente luci più luminose e ombre più scure, con grande miglioramento della profondità dell'immagine.

- <strong>Principio</strong>: la gamma di luminosità degli schermi normali (SDR) è limitata, con differenza insufficiente tra il più luminoso e il più scuro. Gli schermi HDR hanno peak brightness più alta (di solito oltre 1000 nit), contrasto maggiore, gamut cromatico più ampio, riescono a mostrare più dettagli.
- <strong>Standard principali</strong>: HDR10 (il più base, gratuito e open source), HDR10+ (spinto da Samsung, metadati dinamici), Dolby Vision (qualità migliore ma richiede licenza). Lo standard supportato dal cellulare dipende dall'hardware dello schermo e dalle licenze di sistema.
- <strong>Effetto reale</strong>: guardando video HDR, la luce del sole è più abbagliante, le ombre più profonde, i colori più ricchi. A patto che il video sia prodotto in HDR e lo schermo supporti la visualizzazione HDR.

##### Tecnologia HDR fotografico

L'HDR in fotografia e quello dello schermo sono due cose diverse. L'HDR fotografico risolve via algoritmo il problema delle "luci sovraesposte e ombre nere morte".

- <strong>Principio algoritmico</strong>: allo scatto, il cellulare scatta in realtà più foto con esposizioni diverse (sottoesposizione per conservare i dettagli in luce, sovraesposizione per le ombre, esposizione normale per i toni medi), per poi fonderle in un'unica foto ad alta gamma dinamica.
- <strong>Flusso</strong>: cattura multi-frame → allineamento e compensazione (anti-shake) → fusione esposizione / tone mapping → correzione colore → output foto finale.
- <strong>Ottimizzazione</strong>: oggi i cellulari riescono a fare "HDR in tempo reale" — ciò che vedi nel mirino è l'effetto HDR elaborato, WYSIWYG. Smart HDR di Apple e auto HDR di Android sono entrambi molto maturi.

##### 5. Batteria e ricarica: sorgente di energia

La batteria è il componente più "effimero" del cellulare: in due o tre anni si degrada visibilmente. La capacità mainstream oggi è 5500-7500mAh.

- <strong>Potenza di ricarica</strong>: il campo Android è arrivato a 100W o persino 200W, carica completa in dieci minuti; Apple è ancora sui 20-30W. La ricarica rapida rovina la batteria? Con accessori originali non ci sono problemi, il cellulare ha protezione termica.
- <strong>Ricarica wireless</strong>: comoda ma inefficiente, con molto calore. Adatta alla ricarica "a portata di mano" in ufficio, non quando si ha fretta di uscire.
- <strong>Ricarica inversa</strong>: il cellulare diventa power bank, per caricare auricolari e smartwatch, per emergenze.

##### 6. Fotocamere: la magia di luce e ombra

Oggi i cellulari hanno tre o quattro fotocamere, ciascuna con un ruolo:

- <strong>Principale</strong>: la più usata, sensore più grande, qualità migliore.
- <strong>Grandangolo</strong>: per paesaggi e architettura, campo visivo più ampio.
- <strong>Teleobiettivo</strong>: per soggetti lontani, con zoom ottico e zoom digitale.
- <strong>Macro</strong>: per piccoli soggetti a brevissima distanza.

<strong>I megapixel non sono tutto!</strong> La dimensione del sensore (un sensore più grande batte uno più piccolo), l'apertura del diaframma (f/1.8 è più grande di f/2.4), lo stabilizzatore (OIS ottico è importante) influenzano la qualità. La fotografia computazionale (algoritmi AI) è sempre più importante, capace di fonder più scatti in un'unica bella foto.

##### Teleobiettivo periscopico

I teleobiettivi tradizionali richiedono un percorso ottico lungo, che renderebbe il cellulare spesso. Il teleobiettivo periscopico usa un prisma a 90 gradi per rifrangere la luce, sviluppando il percorso ottico orizzontalmente dentro il cellulare, mantenendolo sottile e ottenendo zoom ottico 5x o persino 10x.

- <strong>Struttura</strong>: la luce entra dalla lente → il prisma la rifrange di 90° → attraversa il gruppo di lenti in direzione della larghezza del cellulare → arriva al sensore. Equivale a mettere un telescopio verticale in orizzontale.
- <strong>Caratteristiche ottiche</strong>: zoom ottico elevato (5x-10x), qualità molto superiore allo zoom digitale. Ma il sensore è di solito più piccolo del principale, prestazioni in luce debole mediocri.
- <strong>Vantaggi</strong>: fotografare la luna, architetture lontane, dettagli sul palco, impareggiabili per un cellulare normale.

##### OIS stabilizzazione ottica vs EIS stabilizzazione elettronica

Lo stabilizzatore è una tecnologia chiave per la qualità di foto e video; le due modalità hanno principi completamente diversi:

- <strong>OIS (stabilizzazione ottica)</strong>: compensa il tremore della mano muovendo fisicamente le lenti o il sensore. All'interno della lente c'è un micro giroscopio che rileva direzione e ampiezza del tremore, poi un motore sposta il gruppo di lenti in direzione opposta. Pro: nessuna perdita di qualità; contro: costo elevato, occupa spazio.
- <strong>EIS (stabilizzazione elettronica)</strong>: compensa il tremore ritagliando e spostando l'immagine via software. Il cellulare registra un'area leggermente più grande e, in base ai dati del giroscopio, ritaglia una zona stabile. Pro: nessun hardware aggiuntivo; contro: ritaglia l'immagine (campo visivo più piccolo), in luce debole può sfocare.
- <strong>Scelta pratica</strong>: in foto privilegia l'OIS, in video la combinazione dei due è la migliore. Oggi molti flagship supportano "Sensor-Shift" (spostamento del sensore), con effetti migliori della tradizionale stabilizzazione delle lenti.

##### Zoom ottico vs zoom digitale

- <strong>Zoom ottico</strong>: spostando fisicamente il gruppo di lenti cambia la lunghezza focale, senza perdita di qualità. Lo zoom ottico sui cellulari ha di solito solo ingrandimenti fissi (2x, 3x, 5x, 10x), non può zoomare in modo continuo come le fotocamere.
- <strong>Zoom digitale</strong>: ingrandisce l'area centrale dell'immagine, in pratica ritaglia + interpolazione. Più ingrandisci, peggio è la qualità. Lo zoom digitale 100x sembra figo, ma la qualità è ormai molto sfocata.
- <strong>Zoom ibrido</strong>: combina ottico e digitale, tra gli ingrandimenti ottici usa algoritmi multi-frame per compensare la perdita di qualità. Meglio del puro digitale, ma sempre peggio dell'ottico.

##### Audio: altoparlanti e chip grafico dedicato

<strong>Altoparlante singolo vs doppio altoparlante</strong>:

- <strong>Altoparlante singolo</strong>: solo un'unità in basso, il suono è sbilanciato da un lato, senza tridimensionalità. Comune nei cellulari di fascia medio-bassa.
- <strong>Doppio altoparlante (stereo)</strong>: uno in alto e uno in basso, creano un campo sonoro stereo. Guardando video o ascoltando musica, i canali sinistro e destro sono distinti, l'immersione molto maggiore. La capsula auricolare spesso funge da altoparlante superiore.
- <strong>Differenza di qualità</strong>: i doppi altoparlanti non sono solo "più forti", la chiave è la spazialità e la stratificazione. Con un altoparlante singolo, guardare un blockbuster sembra sempre mancare di qualcosa.

<strong>Chip grafico dedicato nei cellulari da gaming</strong>:

Alcuni cellulari da gaming e performanti montano un chip di elaborazione video indipendente, con queste funzioni:

- <strong>Frame insertion</strong>: interpola i frame del gioco da 30fps a 60fps o 120fps, più fluido. Elaborato sul chip grafico dedicato, non occupa la GPU del SoC.
- <strong>Super-resolution</strong>: algoritmi AI per aumentare la risoluzione, qualità più nitida.
- <strong>Riduzione consumi</strong>: poiché frame insertion e super-resolution sono gestiti dal chip dedicato, il carico del SoC diminuisce, meno calore e consumi, gioco più stabile.

##### Posizionamento GPS: singola frequenza vs doppia frequenza

Il posizionamento del cellulare si basa principalmente su sistemi di navigazione satellitare come il GPS.

- <strong>GPS mono-frequenza</strong>: riceve solo il segnale della banda L1, precisione di circa 3-5 metri. All'aperto è sufficiente, ma nei canyon urbani con grattacieli fitti, la riflessione del segnale causa scostamenti più grandi.
- <strong>GPS dual-frequency</strong>: riceve contemporaneamente L1 e L5. La banda L5 ha lunghezza d'onda maggiore e maggiore resistenza ai disturbi; la risoluzione congiunta delle due frequenze elimina la maggior parte degli errori ionosferici, con precisione di 1-3 metri. Vantaggi evidenti in navigazione urbana e localizzazione dei taxi.
- <strong>Supporto multi-costellazione</strong>: i cellulari moderni supportano non solo il GPS, ma anche BeiDou (Cina), GLONASS (Russia), Galileo (Europa) e altri sistemi satellitari. Più satelliti connessi contemporaneamente, più veloce e precisa è la localizzazione.

##### 7. Sensori: le antenne del cellulare

Dentro il cellulare si nascondono oltre dieci sensori, che lavorano silenziosamente:

- <strong>Accelerometro + giroscopio</strong>: rileva l'orientamento del cellulare, sterzo nei giochi, rotazione automatica dello schermo.
- <strong>Sensore di luce</strong>: regola automaticamente la luminosità dello schermo.
- <strong>Sensore di prossimità</strong>: durante le chiamate, quando il cellulare si avvicina all'orecchio spegne lo schermo.
- <strong>Sensore di impronte</strong>: oggi lo standard è l'impronta ottica sotto-schermo o ultrasonica.
- <strong>Riconoscimento facciale</strong>: il Face ID di Apple è structured light 3D, sicurezza alta; molti Android usano il riconoscimento 2D di foto, sicurezza media.
- <strong>NFC</strong>: Near Field Communication, per carte di trasporto, badge, carte bancarie.
- <strong>Barometro</strong>: misura l'altitudine, rileva persino quando sali le scale.
- <strong>Sensore a effetto Hall</strong>: rileva l'apertura/chiusura della cover magnetica.

#### 2. Sistema operativo: Android VS iOS VS HarmonyOS

L'hardware è il corpo, il sistema operativo è l'anima. I tre grandi sistemi hanno ciascuno le proprie caratteristiche:

- <strong>Android</strong>: come una comunità open source, i produttori possono personalizzarlo in profondità, molta scelta. Puoi cambiare tema, installare store di terze parti, smanettare. Ma proprio per via dell'apertura, la frammentazione è grave e l'esperienza tra brand è molto diversa.
- <strong>iOS</strong>: come un giardino curato, Apple controlla hardware e software, esperienza unificata e fluida. Qualità delle app alta, protezione della privacy buona, ma libertà ridotta, molte cose vanno fatte a modo di Apple.
- <strong>HarmonyOS</strong>: la nuova specie di Huawei, si caratterizza per le capacità distribuite, che consentono a dispositivi diversi di collaborare senza soluzione di continuità. Ne parleremo in modo specifico più avanti.

L'ecosistema di tutti e tre è ricchissimo; scegli quello che si adatta al tuo stile di vita. Non c'è un bene o male assoluto, solo un adatto o non adatto.

#### 3. Analisi completa delle interfacce del cellulare

L'interfaccia del cellulare è il ponte con il mondo esterno; le interfacce diverse si differenziano molto:

##### Micro USB

- <strong>Caratteristiche fisiche</strong>: interfaccia trapezoidale piatta, con dritto e rovescio distinti (inserita al contrario non entra). Ormai quasi del tutto abbandonata sui cellulari, ma ancora usata in alcuni dispositivi economici e datati.
- <strong>Limiti di trasmissione</strong>: supporta solo lo standard USB 2.0, massima velocità 480 Mbps, potenza di ricarica di solito non superiore a 10W.
- <strong>Svantaggi</strong>: non reversibile, vita utile delle inserzioni breve, velocità di trasmissione lenta, potenza di ricarica bassa.

##### Lightning (interfaccia Apple, dismessa)

- <strong>Caratteristiche fisiche</strong>: interfaccia a 8 pin sviluppata da Apple, inseribile da entrambi i lati. Usata su iPhone 14 e modelli precedenti, ora completamente dismessa.
- <strong>Limiti di trasmissione</strong>: l'interfaccia Lightning supporta fisicamente solo lo standard USB 2.0, massima velocità 480 Mbps. Anche con cavo USB-C to Lightning, la velocità è limitata dall'interfaccia Lightning stessa.
- <strong>Motivo della dismissione</strong>: l'Unione Europea ha approvato una normativa che impone dal 2024 l'uso unificato di USB-C su tutti i cellulari; Apple a partire dalla serie iPhone 15 è passata completamente a Type-C. Lightning è uscita di scena.
- <strong>Nota</strong>: il cavo certificato MFi di Apple contiene un chip di autenticazione; cavi non certificati potrebbero non caricare o trasmettere correttamente. Se usi ancora un vecchio iPhone, tieni pronti cavi Lightning.

##### USB Type-C

- <strong>Caratteristiche fisiche</strong>: interfaccia ovale a 24 pin, inseribile da entrambi i lati. È diventata lo standard per cellulari e la maggior parte dei dispositivi elettronici. L'UE ha imposto per legge dal 2024 l'uso unificato di USB-C per tutti i cellulari, tablet, auricolari e altri dispositivi portatili; altre regioni del mondo stanno seguendo.
- <strong>Protocollo di trasmissione</strong>: Type-C è solo la forma dell'interfaccia; la capacità di trasmissione effettiva dipende dal protocollo interno. Supporta USB 2.0 (480 Mbps), USB 3.0/3.1/3.2 (5-20 Gbps) e persino USB4 (40 Gbps).
- <strong>Distinzione importante</strong>: non tutte le interfacce Type-C supportano USB 3.0! Molti cellulari, pur usando Type-C, collegano internamente solo i pin USB 2.0, con velocità lenta come le vecchie interfacce. iPhone 16/17 standard supporta solo USB 2.0, la versione Pro supporta USB 3.0 (con cavo USB-C to USB-C).
- <strong>Capacità di ricarica</strong>: supporta protocolli di ricarica rapida come USB PD, fino a 240W.
- <strong>Output video</strong>: supporta DisplayPort Alt Mode, tramite adattatore può mandare video a un monitor.

##### Interfaccia audio 3.5mm

- <strong>Caratteristiche fisiche</strong>: jack tondo a 3 o 4 poli, a 3 poli trasmette i canali audio sinistro e destro, a 4 poli ha un canale microfonico in più.
- <strong>Caratteristiche</strong>: trasmissione di segnale analogico, plug-and-play, senza driver o conversioni. Qualità audio stabile, latenza zero.
- <strong>Stato attuale</strong>: la maggior parte dei cellulari di punta ha eliminato il jack 3.5mm, serve un adattatore Type-C o auricolari Bluetooth. Alcuni cellulari di fascia media e da gaming lo mantengono.

#### 4. Sistema di prodotti del cellulare e regole di denominazione

Di fronte alle linee di prodotto spesso confusionarie dei vari brand, capire le regole di denominazione ti aiuta a posizionare rapidamente il modello adatto a te.

##### Serie di prodotti dei principali brand:

- <strong>Apple</strong>: iPhone (standard) / iPhone Plus (grande schermo) / iPhone Pro (professionale) / iPhone Pro Max (grande schermo professionale) / iPhone SE (economica) / iPhone 16e (versione AI economica, con chip A18 e baseband C1 proprietaria di Apple). Nel 2026 la serie iPhone 17 monta completamente il chip A19 Pro, con capacità AI ulteriormente migliorate.
- <strong>Huawei</strong>: serie Mate (flagship business) / serie P/Pura (flagship imaging) / serie Mate X (flagship pieghevole) / serie nova (giovane medio-tier) / serie Enjoy (entry-level)
- <strong>Xiaomi</strong>: serie numerica Xiaomi (flagship) / Xiaomi MIX (flagship esplorativo/pieghevole) / serie Redmi K (flagship prestazionale) / serie Redmi Note (mid-range) / serie numerica Redmi (entry-level)
- <strong>OPPO</strong>: serie Find X (flagship) / serie Reno (mid-range) / serie A (entry-level) / serie numerica OnePlus (flagship prestazionale)
- <strong>vivo</strong>: serie X (flagship imaging) / serie iQOO numerica (flagship prestazionale) / serie S (selfie mid-range) / serie Y (entry-level)
- <strong>Samsung</strong>: serie Galaxy S (flagship) / Galaxy Z Fold/Flip (flagship pieghevole) / serie Galaxy A (mid-range)

##### Significato dei suffissi più comuni:

- <strong>Pro</strong>: abbreviazione di Professional, versione professionale. Di solito, rispetto alla versione standard, upgrade di fotocamere, schermo, processore e altre configurazioni chiave.
- <strong>Max</strong>: versione massima. Schermo e batteria più grandi, ma le specifiche non sono necessariamente superiori al Pro.
- <strong>Ultra</strong>: versione estrema. Di solito rappresenta la configurazione più alta della serie, con specifiche spinte e prezzo più alto. Ad esempio Samsung S24 Ultra, Xiaomi 14 Ultra.
- <strong>SE</strong>: Special Edition edizione speciale, in realtà spesso la versione economica. Specifiche ridotte, prezzo più basso. Ad esempio iPhone SE.
- <strong>Plus</strong>: versione ingrandita. Schermo più grande dello standard, batteria più grande, ma configurazione di base equivalente.
- <strong>Lite / Youth Edition</strong>: versione leggera. Specifiche ridotte, prezzo più basso.
- <strong>Note</strong>: originariamente indicava cellulari con grande schermo, oggi i brand lo usano in modi diversi. Redmi Note è una serie mid-range.
- <strong>Neo</strong>: versione nuova. Di solito si riferisce a modelli mid-range orientati alle prestazioni.

#### 5. Baseband e antenne: i protagonisti dietro le quinte della comunicazione

Che il cellulare possa chiamare e navigare lo si deve alla coppia formata da chip baseband e antenna.

##### Chip baseband:

La baseband è il processore del cellulare responsabile delle comunicazioni wireless: modula il segnale digitale in onde radio per la trasmissione e demodula le onde radio ricevute in segnale digitale. Le prestazioni della baseband influenzano direttamente la qualità delle chiamate, la velocità di navigazione e la stabilità del segnale. Qualcomm è il maggior fornitore di baseband per cellulari; MediaTek e Samsung hanno baseband proprietarie. Apple, a partire dall'iPhone 16e, monta la baseband C1 proprietaria, segnando l'ingresso ufficiale di Apple nell'era baseband proprietaria; la C1 usa un processo a 4nm con consumi eccellenti; iPhone 16/16 Plus/16 Pro/16 Pro Max usano ancora baseband Qualcomm (Snapdragon X75 5G), si prevede che i modelli successivi passino gradualmente alle baseband proprietarie. I precedenti iPhone XS/11 con baseband Intel avevano prestazioni del segnale scadenti, un problema per molti utenti.

##### Design delle antenne:

Le antenne del cellulare sono nascoste all'interno del corpo, di solito disposte lungo il bordo. Il design dell'antenna influisce direttamente sulle prestazioni di ricezione del segnale:

- <strong>Tecnologia MIMO</strong>: Multiple-Input Multiple-Output, usa più antenne per inviare e ricevere dati contemporaneamente, migliorando velocità e stabilità. 4×4 MIMO è più veloce di 2×2 MIMO.
- <strong>Numero di antenne</strong>: i flagship hanno di solito oltre dieci antenne (cellulare, Wi-Fi, Bluetooth, NFC, GPS ciascuno con antenna dedicata).
- <strong>Influenza del corpo metallico</strong>: il metallo scherma il segnale, quindi i cellulari con corpo metallico devono avere antenna bands (le strisce di plastica sul bordo). Corpi in vetro e plastica hanno minore impatto sul segnale.

##### Evoluzione delle tecnologie di rete:

- <strong>4G LTE</strong>: velocità teorica di picco in downlink 1 Gbps, uplink 500 Mbps (Cat.18), in pratica 50-150 Mbps. Copertura più ampia, sufficiente.
- <strong>5G NR</strong>: velocità teorica di picco in downlink oltre 10 Gbps. La banda Sub-6GHz ha copertura migliore, le onde millimetriche mmWave sono velocissime ma con copertura minima.
- <strong>5G-A (5G Advanced)</strong>: versione potenziata del 5G, chiamata anche 5.5G. Downlink fino a 10 Gbps, uplink 1 Gbps, densità di connessioni e precisione di localizzazione molto migliori. Dal 2024 China Mobile, China Telecom e China Unicom hanno iniziato a distribuire reti 5G-A nelle città principali; i flagship come Huawei Mate 70/80 series e Xiaomi 15/16 series supportano già il 5G-A. Il 5G-A porta anche capacità "integrated sensing and communication", le stazioni base possono comunicare e percepire l'ambiente contemporaneamente, fornendo infrastruttura per l'economia low-altitude (consegne con drone) e per la connettività veicolare.

##### Classificazione delle bande di rete:

Le bande di rete supportate dal cellulare determinano in quali paesi e su quali operatori può essere usato:

- <strong>FDD-LTE Band (serie B)</strong>: come B1, B3, B5, bande 4G. Paesi diversi usano bande diverse; la Cina usa principalmente B1/B3/B5/B8/B34/B38/B39/B40/B41.
- <strong>TDD-LTE Band</strong>: l'altra modalità del 4G, molto usata in Cina con B38/B39/B40/B41.
- <strong>5G NR Band (serie N)</strong>: come n1, n3, n28, n41, n78, n79. n78 (3.5GHz) è la banda principale del 5G in Cina, n41 (2.5GHz) è molto usata da China Mobile.
- <strong>Consiglio d'acquisto</strong>: se devi usarlo all'estero, prima di acquistare verifica che il cellulare supporti le bande del paese di destinazione. I modelli "National Bank" cinesi supportano di solito tutte le bande cinesi ma potrebbero mancare di alcune bande estere.

#### 6. Il tuo cellulare, quanti ruoli sta interpretando?

Non è più solo un telefono:

1. <strong>Strumento di comunicazione</strong>: chiamate, SMS, WeChat, email...
2. <strong>Fotocamera intelligente</strong>: foto, video, scansione documenti...
3. <strong>Portafoglio</strong>: pagamenti, carte di trasporto, carte bancarie, carte fedeltà...
4. <strong>Porta informazioni</strong>: notizie, meteo, azioni, conoscenza...
5. <strong>Console di gioco</strong>: dal casual game ai blockbuster AAA...
6. <strong>Ufficio mobile</strong>: documenti, fogli, riunioni, collaborazione...
7. <strong>Assistente salute</strong>: contapassi, battito, sonno, sport...
8. <strong>Telecomando casa intelligente</strong>: controlla luci, condizionatori, TV, robot aspirapolvere...
9. <strong>Carta d'identità digitale</strong>: carta d'identità elettronica, patente elettronica, codice sanitario...
10. <strong>Centro svago</strong>: musica, video, ebook, podcast...

Pensaci: un piccolo dispositivo, quanta vita porta con sé! Quindi, imparare a usarlo bene è imparare a vivere meglio.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Pratica: conosci la configurazione hardware

{class="mt-1"}
In [Impostazioni], vedi se riesci a trovare il modello del processore, la dimensione della RAM e dello storage (ROM). Fatti un'idea delle capacità del tuo cellulare. Gli utenti Android possono scaricare "AnTuTu" o "DevCheck" per informazioni dettagliate sull'hardware.
:::
