---
id: di-er-shi-zhang-jinjie
num: 20
part: jin-jie-pian
nav: Capitolo 20: Modalità sviluppatore e permessi avanzati
toc: default
kind: supplement
---

### Capitolo 20: Modalità sviluppatore e autorizzazioni avanzate

{class="chapter-intro mb-4"}
Questo capitolo è per chi vuole esplorare a fondo le "funzioni nascoste" del telefono. Modalità sviluppatore, permessi Root, blocco BL... concetti che sembrano molto geek ma non sono poi così lontani dall'utente comune.

#### 1. Modalità sviluppatore: sblocca le impostazioni nascoste

La modalità sviluppatore è un menu nascosto integrato nel sistema del telefono, con molte funzioni che l'utente comune non usa ma che servono agli sviluppatori.

##### Come attivarla:

- <strong>Android</strong>: entra in Impostazioni > Info telefono > tocca "Numero build" 7 volte di fila, finché non compare la notifica "Ora sei uno sviluppatore".
- <strong>HarmonyOS</strong>: Impostazioni > Info telefono > tocca "Versione HarmonyOS" 7 volte.
- <strong>iOS</strong>: l'utente comune non può attivare la modalità sviluppatore completa, serve un account Apple Developer a pagamento.

##### Panoramica delle funzioni comuni:

- <strong>Debug USB</strong>: interruttore indispensabile per operazioni avanzate col computer (flash, recupero dati, comandi ADB), vedi la sezione "Comandi ADB pratici" più avanti.
- <strong>Mostra tocchi</strong>: mostra sullo schermo il punto di tocco (un piccolo pallino che segue il dito), utile per registrare tutorial o dimostrazioni.

##### Prestazioni e fluidità:

- <strong>Regolazione della velocità delle animazioni (Scala animazione finestra / Scala animazione transizione / Scala durata animazione)</strong>: queste tre opzioni controllano la durata delle animazioni quando si apre un'app o si cambia schermata. Il valore predefinito è 1x; portarlo a 0.5x rende il telefono "più veloce" (in realtà la velocità dei programmi non cambia, solo l'animazione è più rapida), mentre disattivarlo significa passare da una schermata all'altra senza animazione. Molti geek lo impostano a 0.5x, per conservare una sensazione di transizione ma sembrare veloci; disattivarlo del tutto rende l'uso brusco e potrebbe nascondere i veri lag, facendoti credere che sia "fluidissimo" quando non lo è.
- <strong>Forza rendering GPU (Force GPU Rendering)</strong>: forza tutte le operazioni di disegno 2D a passare alla GPU invece che alla CPU. Su modelli vecchi o con app poco ottimizzate può migliorare la fluidità di scorrimento, ma aumenta il carico della GPU e i consumi. I telefoni moderni usano già massicciamente la GPU per il rendering, quindi questo interruttore ha un impatto limitato sui modelli di fascia media-alta: è più che altro un'opzione storica, l'utente comune può lasciare il default.
- <strong>Profilo rendering GPU (Profile GPU Rendering)</strong>: mostra sullo schermo un grafico a barre in tempo reale del tempo di rendering di ogni frame; la linea verde orizzontale rappresenta i 16,6 ms (soglia di tempo frame a 60 fps). Se la barra supera la verde significa che c'è stato frame drop. È uno strumento per sviluppatori per diagnosticare i lag delle app; anche l'utente comune può usarlo per capire quali app siano peggio ottimizzate — se per una certa app le barre spesso superano la riga rossa durante lo scorrimento, con tutta probabilità è colpa sua.

##### Background e autonomia:

- <strong>Limite processi in background</strong>: permette di impostare "Limite standard", "Max 1 processo", "Max 2 processi" e così via. In apparenza limitare i processi in background fa risparmiare batteria, ma in realtà la gestione del background integrata in Android è già discreta; un limite rigido porta le app a ricaricarsi spesso (il cold start consuma di più e peggiora l'esperienza). Questa opzione è più adatta al debug, non se ne consiglia l'attivazione prolungata all'utente comune; lascia "Limite standard".
- <strong>Non mantenere attività</strong>: distrugge ogni attività non appena lasci la schermata. Sconsigliatissimo, provoca continui schermate bianche e ricariche delle app; serve solo per testare la logica di ripristino di un'app.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Avvertenze

{class="mt-1"}
Le impostazioni della modalità sviluppatore possono compromettere la stabilità del sistema: non modificare le opzioni che non comprendi. Dopo aver attivato il debug USB, fai attenzione quando colleghi il telefono a computer non fidati.
:::

#### 2. Sblocco OEM: l'"interruttore per il flash" nelle opzioni sviluppatore

Tra le opzioni sviluppatore c'è un interruttore poco appariscente ma molto importante — "Sblocco OEM" (in alcuni marchi chiamato "Consenti sblocco OEM" o "Sblocco dispositivo"). L'interruttore in sé non sblocca il BL, ma è una "pre-autorizzazione": solo attivandolo il produttore ti permette di sbloccare il BL tramite il comando fastboot o uno strumento di marca.

- <strong>Funzione dell'interruttore</strong>: equivale a dichiarare al produttore "accetto di perdere la garanzia e mi assumo i rischi, sbloccami il BL". Se questo interruttore è spento, qualsiasi comando di sblocco BL viene rifiutato.
- <strong>Rapporto con il blocco BL</strong>: lo sblocco OEM è la "richiesta di idoneità", lo sblocco BL è l'"operazione effettiva". Il primo si attiva toccando nelle impostazioni del telefono; il secondo richiede di richiedere un codice di sblocco sul sito del produttore ed eseguire un comando fastboot dal computer (ad esempio <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing unlock</code>); entrambi sono indispensabili.
- <strong>Il ripristino di fabbrica lo resetta?</strong> Sì. L'interruttore "Sblocco OEM" torna spento dopo il ripristino di fabbrica, ma il BL, una volta sbloccato, resta in uno stato fisico e non viene bloccato di nuovo dal ripristino: devi eseguire manualmente <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing lock</code> per bloccarlo di nuovo.
- <strong>Quando va attivato</strong>: a meno che tu non sia sicuro di voler fare il flash o il Root, lascialo spento. È indipendente dall'interruttore "Debug USB": per il flash di solito vanno attivati entrambi.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Curiosità: perché i produttori mettono questo interruttore

{class="mt-1"}
Sui primi Android non c'era questo interruttore e un malware, una volta ottenuti i permessi, poteva installare di nascosto un sistema non ufficiale. In seguito Google ha preteso che tutti i produttori Android inserissero nelle opzioni sviluppatore l'interruttore "Sblocco OEM", come conferma di "consenso informato dell'utente". Ecco perché, anche se hai sbloccato il BL, se l'interruttore "Sblocco OEM" viene spento, un nuovo flash fallirà comunque.
:::

#### 3. Blocco BL (Bootloader): la prima porta del flash

Il Bootloader è il programma che carica il sistema operativo all'avvio del telefono. Il blocco BL è un lucchetto messo dal produttore per sicurezza, per impedire all'utente di installare sistemi non ufficiali.

##### Funzioni del blocco BL:

- <strong>Protezione della sicurezza</strong>: impedisce ai malware di installare un sistema non ufficiale.
- <strong>Antifurto</strong>: anche se il telefono viene flashato, senza l'account e la password originali non può essere usato.
- <strong>Limiti di garanzia</strong>: sbloccare il BL di solito significa perdere la garanzia ufficiale.

##### Politiche sul blocco BL dei vari marchi:

- <strong>Xiaomi</strong>: sbloccabile, richiede associazione account e periodo di attesa (7-30 giorni).
- <strong>Huawei</strong>: dal 2018 non fornisce più codici di sblocco, di fatto non sbloccabile ufficialmente.
- <strong>OnePlus</strong>: sbloccabile, policy relativamente permissiva.
- <strong>OPPO/vivo</strong>: alcuni modelli sono sbloccabili, previa richiesta.
- <strong>Samsung</strong>: sbloccabile, ma innesca il fusibile Knox e si perdono funzioni come Samsung Pay.
- <strong>Apple</strong>: i dispositivi iOS non hanno il concetto classico di blocco BL, ma hanno meccanismi di sicurezza analoghi.

#### 4. Comandi ADB pratici: controllare il telefono dal computer

ADB sta per Android Debug Bridge, uno strumento a riga di comando ufficiale di Google che permette al computer di comunicare con il telefono Android tramite USB o Wi-Fi. Non richiede Root: basta aver attivato il "Debug USB" sul telefono. Puoi considerarlo un "telecomando con cui dare ordini al telefono dal computer": flash, installazione di app, trasferimento file, lettura dei log, tutto passa di qui.

##### Come collegarsi via USB:

1. Sul telefono: entra nelle opzioni sviluppatore → attiva "Debug USB".
2. Sul computer: scarica dal sito ufficiale di Google i Platform Tools (contengono gli eseguibili <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb</code> e <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot</code>), estrai in una cartella qualsiasi.
3. Collega telefono e computer con il cavo dati; sul telefono comparirà il popup "Consenti debug USB?", spunta "Consenti sempre" e conferma.
4. Nella riga di comando del computer (PowerShell o cmd su Windows) esegui <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code>; se l'output è simile a <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">List of devices attached / xxxxxxxx device</code>, la connessione è riuscita.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Non ignorare driver e popup di autorizzazione

{class="mt-1"}
Se su Windows <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code> restituisce "unauthorized" o non elenca il dispositivo, con tutta probabilità i driver non sono installati oppure hai dimenticato di toccare "Consenti" sul telefono. Per Samsung, Xiaomi e altri marchi puoi installare i rispettivi "driver USB" o "assistenti telefono" per integrare i driver; su Mac e Linux di solito non servono driver. Se hai chiuso per sbaglio il popup sul telefono, scollega e ricollega il cavo e riapparirà.
:::

##### Comandi ADB comuni:

- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb install app.apk</code>: installa l'APK dal computer al telefono (<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-r</code> indica reinstallazione mantenendo i dati; <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code> installa su SD).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb uninstall com.xxx.xxx</code>: disinstalla un'app in base al nome del pacchetto.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb push percorso_computer /sdcarta/destinazione</code>: invia un file dal computer al telefono.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb pull /sdcarta/file percorso_computer</code>: scarica un file dal telefono al computer (molto più veloce che inviarlo a se stessi su WeChat e riscaricarlo).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell</code>: entra nella shell Linux del telefono, puoi eseguire direttamente comandi come <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls</code>, <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm</code>, <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">am</code>.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot bootloader</code>: riavvia il telefono in modalità Fastboot (punto d'ingresso per il flash).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot recovery</code>: riavvia in modalità Recovery.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages</code>: elenca i nomi dei pacchetti di tutte le app installate (indispensabile per trovare i nomi dei pacchetti). Con <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code> vedi solo le app di sistema, con <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-3</code> solo le app di terze parti.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 nome_pacchetto</code>: disinstalla le app preinstallate per l'utente corrente, senza Root; vedi la pratica qui sotto.

##### Pratica: disinstallare le app preinstallate senza Root:

È una delle funzioni ADB più utili: con il comando <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code> puoi disinstallare le app preinstallate per "l'utente corrente", senza Root e senza toccare la partizione di sistema. Le app disinstallate "spariscono" dal sistema, ma sono ancora presenti nella partizione di sistema e torneranno dopo il ripristino di fabbrica.

1. Prima usa <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages -s</code> per elencare tutte le app di sistema e trovare il nome del pacchetto che vuoi disinstallare. Ad esempio il browser di Xiaomi è <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.browser</code>, l'App Store di Huawei è <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.vmall.client</code>.
2. Non sai a quale app corrisponda un nome di pacchetto? Sul computer puoi cercare con <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages | findstr parola_chiave</code>, oppure installare un'app di terze parti come "Package Viewer" per vedere direttamente sul telefono il nome del pacchetto di ogni app.
3. Esegui la disinstallazione: <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 nome_pacchetto</code>, ad esempio <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 com.android.browser</code>. Se restituisce <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Success</code> hai fatto.
4. Come ripristinare? Due modi: ① ripristino di fabbrica (il più radicale ma scomodo); ② reinstallazione: <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell cmd package install-existing nome_pacchetto</code>.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>Non cancellare a caso i pacchetti di sistema essenziali

{class="mt-1"}
"pm uninstall --user 0" è un metodo sicuro senza Root, ma cancellare a caso app di sistema critiche (come <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.systemui</code> per la barra di stato, <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.phone</code> per il telefono, <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.settings</code> per le impostazioni) provoca gravi conseguenze: crash di sistema, schermo nero, impossibilità di accendere. Prima di cancellare, cerca su Google "questo nome di pacchetto si può cancellare?"; meglio cancellare meno che sbagliare. Consigliato di cancellare solo una o due app alla volta, verificare che tutto sia a posto, poi proseguire.
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Curiosità: cosa significa --user 0

{class="mt-1"}
Da Android 4.2 è supportato il multi-utente e ogni utente ha un proprio ID (il proprietario è 0, gli utenti aggiuntivi partono da 10). <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">--user 0</code> indica "disinstalla solo per il proprietario corrente"; il file APK nella partizione di sistema resta, semplicemente non viene più mostrato al proprietario. Ecco perché non serve il Root: non si toccano i file di sistema, si modifica solo la "configurazione utente". Questa è la differenza rispetto alla disinstallazione con Root: la disinstallazione con Root elimina davvero il file dal sistema e nessun utente lo ha più; la disinstallazione ADB "nasconde all'utente corrente".
:::

#### 5. Permessi Root: il "super amministratore" di Android

I permessi Root equivalgono al superuser di Linux (controllo completo sulla directory /, lettura e scrittura di qualsiasi file), sono il livello più alto di autorizzazione in Android. Sono diversi dall'Administrator di Windows: Windows, per motivi di sicurezza, pone molti limiti all'amministratore (la vera autorità massima è TrustedInstaller), e neanche l'Administrator può eseguire direttamente <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">sudo rm -rf /*</code> come fa il root di Linux. Ottenendo i permessi Root puoi modificare i file di sistema, disinstallare le app preinstallate e usare app avanzate che richiedono il Root.

##### Vantaggi del Root:

- Disinstallare le app preinstallate non rimovibili.
- Usare app con funzioni avanzate (come Titanium Backup, Greenify).
- Modificare l'interfaccia e le funzioni di sistema.
- Installare Recovery di terze parti e ROM personalizzate.

##### Rischi del Root:

- <strong>Perdita della garanzia</strong>: la maggior parte dei produttori non copre in garanzia i telefoni con Root.
- <strong>Rischio di sicurezza</strong>: app malevole potrebbero ottenere i permessi di Root con conseguenze gravi.
- <strong>Instabilità del sistema</strong>: errori operativi possono causare crash di sistema.
- <strong>App bancarie non funzionanti</strong>: molte app di banca e pagamento, rilevando il Root, si rifiutano di funzionare.
- <strong>Aggiornamenti OTA falliti</strong>: potrebbe non essere possibile ricevere regolarmente gli aggiornamenti ufficiali del sistema.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>Avvertenza grave

{class="mt-1"}
L'operazione di Root comporta rischi e può trasformare il telefono in un "mattone" (impossibilità di accenderlo). Se sei un neofita, è meglio prima studiare a fondo l'argomento e assicurarti di avere un backup completo. Prima di operare leggi con attenzione il tutorial e verifica il tuo modello e la versione di sistema.
:::

#### 6. SafetyNet e certificazione Play Integrity: perché dopo il Root le app bancarie non funzionano

Molti utenti Root hanno vissuto questo momento di sgomento: dopo il Root hanno installato carichi di moduli, ma aprendo l'app della banca — "Il tuo dispositivo non è sicuro, non può essere usato"; non funziona più neanche Google Pay e persino Netflix rifiuta la riproduzione in HD. Dietro ci sono due meccanismi di certificazione dell'integrità del dispositivo di Google: il vecchio SafetyNet e la nuova API Play Integrity.

##### Cosa sono SafetyNet / Play Integrity:

- <strong>SafetyNet Attestation (vecchia versione, dal 2017)</strong>: API di controllo dell'integrità del dispositivo introdotta inizialmente da Google; con questa le app chiedono ai server di Google "questo dispositivo ha superato il test di compatibilità CTS ed è in stato ufficiale non modificato?". I risultati si dividono in Basic Attestation (verifica base) e Strong Attestation (verifica forte, basata su chiavi hardware). Google ha annunciato che SafetyNet sarà dismesso progressivamente dopo il 2024.
- <strong>API Play Integrity (nuova versione, dal 2022)</strong>: soluzione sostitutiva di Google, più rigorosa e completa di SafetyNet. Oltre all'integrità del dispositivo, include "integrità dell'app" (l'app è stata manomessa?) e "integrità account/autorizzazione" (l'account utente è attendibile per Google?). Le nuove app dovrebbero migrare a Play Integrity.
- <strong>Chi le usa</strong>: app di banche, finanza e pagamenti (come Google Pay, le app di home banking, alcune scene di Alipay/WeChat Pay), streaming (protezione dei diritti d'autore in HD di Netflix), anticheat di alcuni giochi (ad esempio alcuni giochi Tencent/NetEase), app aziendali (controllo di conformità dei dispositivi MDM).

##### I tre livelli di certificazione di Play Integrity:

- <strong>MEETS_DEVICE_INTEGRITY (integrità dispositivo superata)</strong>: il dispositivo esegue il sistema Android originale, il Bootloader non è sbloccato, niente Root, test di compatibilità CTS superato. Si possono usare regolarmente le app di banca e pagamenti.
- <strong>MEETS_BASIC_INTEGRITY (integrità base superata)</strong>: il dispositivo è sostanzialmente affidabile, ma potrebbe avere lievi anomalie. Alcune app lo degradano (ad esempio Netflix riproduce ma limita la risoluzione), alcune app bancarie rigorose lo rifiutano direttamente.
- <strong>MEETS_STRONG_INTEGRITY (integrità forte superata)</strong>: il livello più alto, richiede l'endorsement di una chiave hardware (come il chip Titan M della serie Google Pixel); la maggior parte dei dispositivi di marche terze, anche senza Root, non raggiunge questo livello.
- <strong>Nessuna etichetta (NO_INTEGRITY)</strong>: il dispositivo ha il Root, BL sbloccato, una ROM di terze parti installata o è riconosciuto come emulatore; la stragrande maggioranza delle app di pagamento/banca lo rifiuta direttamente.

##### Perché dopo il Root queste app smettono di funzionare:

L'app invia una richiesta di certificazione ai server di Google tramite l'API Play Integrity; Google controlla diversi indicatori del dispositivo — stato del blocco Bootloader, partizione di sistema modificata, presenza del binario su, SELinux in modalità permissiva, ecc. Qualsiasi anomalia porta il livello restituito a essere più basso o vuoto, e l'app bancaria, vedendo "dispositivo non sicuro", rifiuta il servizio.

##### Soluzioni moderne per nascondere: Magisk Hide / Shamiko / Zygisk:

Per godere delle comodità del Root e al tempo stesso poter usare le app bancarie, la community ha sviluppato una serie di soluzioni per "nascondere lo stato di Root". L'idea di base è: far sì che i programmi di rilevamento non vedano un sistema modificato, ma un dispositivo "che sembra normale".

- <strong>Magisk</strong>: la soluzione Systemless Root più diffusa oggi — non modifica la partizione di sistema, ma realizza il Root tramite mount. Il vantaggio di questa impostazione è che le probabilità di fallimento degli aggiornamenti OTA sono basse e la disinstallazione è piuttosto pulita; è la base di tutte le soluzioni di nascondimento successive. Tuttavia, l'uso di Magisk richiede comunque lo sblocco del BL.
- <strong>Magisk Hide (abbandonato)</strong>: il modulo di nascondimento integrato nelle prime versioni di Magisk, capace di nascondere il Root alle app specificate. Dal 2021 è stato rimosso da Magisk ufficiale, perché Google ha continuato a potenziare i sistemi di rilevamento, in una "caccia al topo" continua.
- <strong>Zygisk</strong>: nuovo meccanismo introdotto in Magisk 24.0+, simile a Riru, realizza il caricamento dei moduli iniettandosi nel processo Zygote; è più nascosto della modifica diretta del sistema. Attivare Zygisk è il prerequisito per usare le soluzioni moderne di nascondimento.
- <strong>Shamiko</strong>: il modulo di nascondimento più diffuso oggi, lavora insieme a Zygisk e può nascondere il Root, nascondere Magisk stesso e contraffare lo stato di blocco del Bootloader per le app specificate (in modalità "reverse whitelist"). Shamiko è distribuito tramite il repository LSPosed o GitHub.
- <strong>Play Integrity Fix (osm0sis)</strong>: modulo Magisk specifico per i rilevamenti di Google Play Integrity, modifica l'impronta del dispositivo (fingerprint) in modo che Google creda che il tuo dispositivo sia un modello ufficiale senza Root.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>La caccia al topo non finirà mai

{class="mt-1"}
Di tanto in tanto Google aggiorna le regole di rilevamento e i produttori di app seguono con un upgrade dei controlli Play Integrity. Le soluzioni di nascondimento che funzionano oggi potrebbero essere identificate domani. Se dipendi completamente dalle app bancarie/di pagamento (ad esempio bonifici quotidiani, pagamenti con QR), la scelta più sicura resta: niente Root, niente sblocco BL. Le soluzioni di nascondimento sono più adatte alla configurazione da giocatore "telefono principale senza Root + telefono secondario con Root".
:::

#### 7. Consigli per l'utente comune

- <strong>Modalità sviluppatore</strong>: puoi attivarla, per sperimentare l'accelerazione delle animazioni, l'analisi del rendering GPU, ecc., ma non modificare a caso le altre opzioni che non comprendi.
- <strong>Sblocco OEM e blocco BL</strong>: se non intendi fare il flash o il Root, lascia entrambi gli interruttori nello stato predefinito (off), è la scelta più sicura.
- <strong>ADB</strong>: strumento potente senza Root, usabile anche dai non esperti — ad esempio <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code> per disinstallare le app preinstallate. Ma prima di cancellare, verifica sempre che il nome del pacchetto si possa cancellare.
- <strong>Root</strong>: per l'utente comune non è consigliato, i rischi superano i vantaggi. Se ti servono davvero alcune funzioni, prima verifica se ci sono alternative che non richiedono il Root (come disinstallare le preinstallate con ADB, o usare Shizuku per sostituire alcune funzioni del Root).

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Prova: attiva la modalità sviluppatore e regola la velocità delle animazioni

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Entra in Impostazioni > Info telefono.
2. Tocca "Numero build" 7 volte di fila, finché non compare l'avviso che la modalità sviluppatore è attiva.
3. Torna in Impostazioni e cerca "Opzioni sviluppatore" (di solito in fondo o in "Sistema").
4. Trova "Scala animazione finestra", "Scala animazione transizione", "Scala durata animazione" e impostali tutti a 0.5x oppure disattivali.
5. Verifica se il telefono sembra più veloce.
:::
