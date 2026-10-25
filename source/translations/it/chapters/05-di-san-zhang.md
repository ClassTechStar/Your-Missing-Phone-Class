---
id: di-san-zhang
num: 03
part: ji-chu-pian
nav: Capitolo 3: Collega il telefono alla sua "linea vitale"
toc: default
kind: chapter
---

### Capitolo 3: Collegare il telefono alla "linea di vita" — La rete

{class="chapter-intro mb-4"}
Senza rete, lo smartphone perde metà della sua "intelligenza". La rete è la linea di vita del telefono moderno: capirla, usarla bene e proteggerla è una materia obbligatoria per ogni utente.

#### 0. Non perdersi nella connessione — distinguere "strada" e "veicolo" tra Wi-Fi e traffico dati

Molte persone vedono contemporaneamente accese le icone Wi-Fi e segnale sul telefono, ma sono totalmente confuse sulla differenza essenziale. L'equivoco più classico è: <strong>sei connesso al Wi-Fi ma le pagine non si caricano</strong> — perché il router ha perso la connessione, e il telefono non è tornato automaticamente al traffico dati. Per capire a fondo il problema, dobbiamo costruire un modello cognitivo "strada e veicolo".

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-road mr-2"></i>Metafora centrale: strada e veicolo

{class="mt-1"}
Immagina Internet come una città. La <strong>"strada"</strong> è il canale tra il tuo telefono e Internet; il <strong>"veicolo"</strong> sono i dati che viaggiano sulla strada. Wi-Fi e traffico dati sono due strade diverse, ma i dati (i veicoli) sono gli stessi.
:::

{class="font-semibold mt-4 mb-1"}
##### 1. Differenza essenziale: canale locale vs autostrada remota

Il Wi-Fi è essenzialmente una <strong>tecnologia LAN</strong>, come una strada senza fili sotto casa, che trasmette i dati dal router al telefono. Ma se la linea broadband non è pagata o il cavo ottico è rotto, la strada c'è ancora ma l'"autostrada" esterna è interrotta, e non si va da nessuna parte. Il traffico dati (dati mobili), invece, viaggia attraverso le stazioni base 4G/5G dell'operatore: è come salire direttamente sull'autostrada dedicata dell'operatore; finché c'è segnale, sei connesso a Internet.

{class="font-semibold mt-4 mb-1"}
##### 2. Costi e scenari: abbonamento fisso vs tariffazione a consumo

Il Wi-Fi di solito è un investimento una tantum (canone mensile della linea): finché c'è corrente, tutta la famiglia lo usa senza limiti, ideale per scaricare film o giocare, scenari ad alto consumo di dati. Il traffico dati, invece, viene tariffato a consumo; superato il bundle può esserci rallentamento o addebiti extra, ed è più adatto a task leggeri in mobilità, come in metropolitana o in viaggio di lavoro.

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands-helping mr-2"></i>Prova: controlla il tuo piano dati

{class="mt-1"}
Apri [Impostazioni] > [Rete mobile] > [Gestione traffico] e verifica quanti GB ti restano questo mese e quali app consumano di più. Sapere cosa hai ti fa uscire di casa senza ansie.
:::

{class="font-semibold mt-4 mb-1"}
##### 3. Considerazioni di sicurezza: il Wi-Fi pubblico è un "campo di pesca" nascosto

Per la sicurezza, i dati mobili sono in genere più sicuri del Wi-Fi pubblico. I dati mobili sono cifrati dall'operatore, mentre il Wi-Fi pubblico può essere facilmente trasformato in "hotspot falso" dai hacker per intercettare traffico non cifrato. Va però chiarito: oggi, con la diffusione capillare di HTTPS, l'attaccante può intercettare <strong>quali siti hai visitato</strong> (dominio) e i <strong>contenuti HTTP non cifrati</strong>; ma i messaggi WeChat, le password di login delle app bancarie e altri dati cifrati con HTTPS <strong>non possono essere letti direttamente</strong> — a meno che non venga messo in atto un attacco SSL stripping più complesso e l'utente ignori gli avvisi sui certificati. In ogni caso, per pagamenti fuori casa, usare direttamente i dati mobili resta la scelta più sicura.

::: div .danger-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>Promemoria di sicurezza

{class="mt-1"}
In aeroporti, centri commerciali, caffè e altri luoghi pubblici, non connetterti a Wi-Fi gratuiti con nomi sospetti (es. "Free_WiFi_2024"). Anche se ti connetti, non usarli mai per accedere a un'app bancaria o per inserire password.
:::

{class="font-semibold mt-4 mb-1"}
##### 4. Verifica lato telefono: capire il "linguaggio segreto" della barra di stato

Come sapere cosa sta usando il telefono in questo momento? Su un telefono Huawei, ad esempio, la comparsa dell'<strong>icona a doppia freccia</strong> accanto al segnale dell'operatore o al segnale WLAN nella barra di stato indica che si sta usando quel metodo per la connessione; se entrambe sono accese, l'accelerazione di rete è attiva e il telefono sta usando entrambi i canali.

Per gli utenti iPhone è più diretto: se l'icona Wi-Fi è accesa, si sta usando il Wi-Fi; se è spenta, guarda le barre di segnale in alto a destra per capire che stai usando il traffico dati. Alcuni telefoni Android mostrano anche "5G" o "4G" nella barra di stato, indicando il tipo di rete mobile corrente.

{class="text-lg font-semibold mt-6 mb-2"}
#### 1. Reti mobili (4G/5G) e traffico dati

La rete mobile è la base per connettersi ovunque. Da 2G a 5G la velocità è aumentata di migliaia di volte, ma il principio è simile.

##### Standard di rete:

- <strong>4G LTE</strong>: attualmente la copertura più ampia, velocità sufficiente (teoricamente fino a 100 Mbps+), consumo energetico relativamente basso.
- <strong>5G</strong>: velocità elevata (teoricamente fino a 10 Gbps), ma la copertura è ancora in via di completamento, consumo energetico alto. Adatta a scaricare file grandi e guardare video ad alta risoluzione.
- <strong>5G SA vs NSA</strong>: SA è la rete autonoma, NSA si appoggia alle stazioni base 4G. L'esperienza SA è migliore, ma richiede il supporto sia dell'operatore sia del telefono.

##### Gestione del traffico:

- <strong>Cosa sono i dati</strong>: è il volume di dati generato navigando sul telefono. Video e immagini consumano di più, testo e voce consumano meno.
- <strong>Dritta per risparmiare</strong>: attiva la "modalità risparmio dati" nelle impostazioni e aggiorna le app o guarda video ad alta risoluzione solo sotto Wi-Fi.
- <strong>Barre di segnale ≠ velocità</strong>: un segnale forte indica solo una buona connessione; la velocità dipende anche dal carico della stazione base e dalla tua distanza da essa.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>Avviso importante: prima di andare all'estero disattiva il [data roaming]!

{class="mt-1"}
Usare i dati mobili all'estero può generare bollette astronomiche! Prima di partire, disattiva il data roaming nelle impostazioni oppure acquista in anticipo una scheda SIM locale o un pacchetto di roaming internazionale.
:::

#### 2. Wi-Fi: connessione, condivisione e sicurezza

Il Wi-Fi è la connessione principale in casa e in ufficio: veloce e senza consumo di traffico. Ma anche il Wi-Fi si evolve e le differenze tra gli standard sono notevoli.

##### Connessione Wi-Fi:

Vai in [Impostazioni] > [WLAN], scegli la rete e inserisci la password. Molti telefoni oggi supportano la connessione tramite scansione di codice QR, ancora più comoda.

##### Condivisione della password:

Sia Android che iOS permettono a un telefono già connesso di condividere rapidamente la password con un amico. Android genera un codice QR, iOS può condividere automaticamente per prossimità.

##### Evoluzione degli standard Wi-Fi:

Gli standard Wi-Fi sono definiti dall'IEEE; ogni generazione porta miglioramenti significativi:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                            <thead>
                                <tr class="bg-light dark:bg-gray-700">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Standard</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Protocollo</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Banda</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Velocità massima</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Caratteristiche</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 4</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11n</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.4/5GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">600Mbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Standard datato, copertura discreta</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 5</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11ac</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">5GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.5Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Oggi il più diffuso, velocità adeguata</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 6</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11ax</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.4/5GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">9.6Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prestazioni multi-dispositivo elevate, latenza bassa</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 6E</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11ax</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.4/5/6GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">9.6Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Aggiunge la banda 6GHz, meno congestione</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 7</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11be</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.4/5/6GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">46Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Trasmissione ultra veloce, aggregazione multi-link</td>
                                </tr>
                            </tbody>
                        </table>
```
:::

- <strong>Tecnologie chiave del Wi-Fi 6</strong>: OFDMA (Orthogonal Frequency-Division Multiple Access) consente la trasmissione simultanea di più dispositivi; MU-MIMO (Multi-User Multiple Input Multiple Output) migliora l'efficienza multi-dispositivo; TWT (Target Wake Time) riduce i consumi.
- <strong>Wi-Fi 6E</strong>: aggiunge la banda 6GHz al Wi-Fi 6, offrendo più canali e meno interferenze. Richiede che telefono e router lo supportino entrambi.
- <strong>Wi-Fi 7</strong>: introduce MLO (Multi-Link Operation), può usare contemporaneamente più bande per trasmettere dati, riducendo drasticamente la latenza. Il canale ultra-largo a 320 MHz porta un salto nelle velocità. Piattaforme flagship come Snapdragon 8 Elite Gen5 e Dimensity 9400 supportano già il Wi-Fi 7; modelli come Xiaomi 17, Huawei Mate 80, Samsung S26 possono usare reti Wi-Fi 7 (in abbinamento a un router Wi-Fi 7).
- <strong>2.4GHz vs 5GHz</strong>: 2.4GHz attraversa meglio i muri ma è più lento e soggetto a interferenze; 5GHz è più veloce ma attraversa peggio i muri. La banda 6GHz del Wi-Fi 6E/7 è la più veloce, ma la più debole nell'attraversare i muri, adatta all'uso nella stessa stanza.

##### Rischi del Wi-Fi pubblico:

Il Wi-Fi pubblico può esporre a intercettazioni o a hotspot esca. Regole d'oro:

- Evita di accedere a conti bancari o di inserire password.
- Usa preferibilmente una VPN per cifrare la connessione.
- Non connetterti automaticamente a Wi-Fi sconosciuti.
- Usa siti HTTPS (icona del lucchetto nella barra degli indirizzi).

#### 3. Bluetooth: l'onnipresente della comunicazione wireless a breve distanza

Il Bluetooth è probabilmente una delle tecnologie wireless più usate sul tuo telefono — cuffie wireless, smartwatch, sistemi auto, tastiere e mouse si connettono tutti grazie a essa.

##### Principio tecnico:

Il Bluetooth opera nella banda ISM a 2.4GHz e usa la tecnica FHSS (Frequency Hopping Spread Spectrum) per distribuire i dati su 79 canali a salti rapidi, evitando le interferenze. La distanza di comunicazione è divisa in tre classi: Classe 1 circa 100 m, Classe 2 circa 10 m (comune sui telefoni), Classe 3 circa 1 m.

##### Evoluzione delle versioni:

- <strong>Bluetooth 4.0</strong>: introduce il Bluetooth a basso consumo (BLE), consentendo a dispositivi con batteria piccola come braccialetti e fasce cardiache di connettersi senza fili; l'autonomia passa da giorni a mesi.
- <strong>Bluetooth 4.2</strong>: migliora velocità di trasmissione e protezione della privacy, supporta la connessione diretta IPv6.
- <strong>Bluetooth 5.0</strong>: velocità raddoppiata (2 Mbps), portata quadrupla (teoricamente 300 m), capacità di broadcast otto volte superiore. Supporta il doppio audio (due cuffie contemporanee).
- <strong>Bluetooth 5.1</strong>: introduce la funzione di indirizzamento direzionale (AoA/AoD), con precisione di localizzazione centimetrica.
- <strong>Bluetooth 5.2</strong>: nuovo standard LE Audio, supporta la codifica LC3 (qualità audio migliore e consumi più bassi), audio multi-flusso e audio broadcast.
- <strong>Bluetooth 5.3/5.4</strong>: ottimizzazioni ulteriori su consumi e stabilità della connessione, broadcast periodico migliorato.

<strong>Diffusione del LE Audio</strong>: nel 2025-2026, il LE Audio è entrato in una fase di rapida diffusione. Le nuove cuffie true wireless dei principali brand (come Huawei FreeBuds Pro 5, Xiaomi Buds 6 Pro, Samsung Galaxy Buds3 Pro) supportano già LE Audio e la codifica LC3, offrendo latenza più bassa e qualità audio superiore. Quando acquisti nuove cuffie, è consigliabile scegliere prodotti che supportano LE Audio.

##### Scenari applicativi:

- <strong>Trasmissione audio</strong>: cuffie wireless, impianti auto. Il LE Audio del Bluetooth 5.2 porta un salto qualitativo in audio e latenza.
- <strong>Trasmissione dati</strong>: scambio di file e foto a breve distanza. Pur essendo più lento del Wi-Fi Direct, vince per semplicità.
- <strong>Accoppiamento dispositivi</strong>: smartwatch, braccialetti, tastiere e mouse, gamepad.
- <strong>Servizi di posizione</strong>: Beacon Bluetooth per navigazione indoor e tracciamento oggetti (es. Apple AirTag).
- <strong>Casa intelligente</strong>: rete Bluetooth Mesh per controllare lampadine, serrature ecc.

#### 4. Telecommando a infrarossi: il telefono diventa un telecomando universale

Il telecommando a infrarossi è una delle tecnologie di controllo wireless più antiche, ma ancora utile sui telefoni. Alcuni telefoni Android (come alcuni modelli Xiaomi e Huawei) integrano un trasmettitore IR, in grado di controllare TV, condizionatori, decoder e altri elettrodomestici.

##### Principio di funzionamento:

Il telecommando IR emette, tramite un LED a infrarossi, impulsi luminosi a una frequenza specifica (in genere 38 kHz); il ricevitore IR dell'elettrodomestico decodifica gli impulsi ed esegue l'azione corrispondente. Marche diverse usano protocolli di codifica diversi, tra i più comuni NEC, RC5, RC6, SONY. L'app IR del telefono integra il database di codici di ciascun marchio: basta selezionare marca e modello per la corrispondenza.

##### Limiti:

- <strong>Direzionalità</strong>: gli infrarossi viaggiano in linea retta, occorre puntare il dispositivo, non attraversano i muri.
- <strong>Breve distanza</strong>: portata utile in genere 5-8 metri.
- <strong>Non supportato da Apple</strong>: l'iPhone non ha il trasmettitore IR e non può usare questa funzione.

#### 5. NFC: la magia del "tocca e vai"

NFC (Near Field Communication) è una tecnologia di comunicazione wireless ad alta frequenza a brevissima distanza (entro 10 cm), operante a 13.56 MHz, con velocità massima di 424 Kbps.

##### Principio di comunicazione e modalità:

NFC deriva dalla tecnologia RFID e supporta tre modalità di funzionamento:

- <strong>Modalità lettura/scrittura</strong>: il telefono legge informazioni da un tag NFC, ad esempio un adesivo NFC che attiva un'azione.
- <strong>Modalità peer-to-peer</strong>: due dispositivi NFC si scambiano dati, come Android Beam (discontinuato).
- <strong>Modalità card emulation</strong>: il telefono emula una smart card — è la modalità più usata: carte bus, badge di accesso, carte bancarie si basano su di essa.

##### Meccanismi di sicurezza:

- <strong>Brevissima distanza</strong>: la comunicazione entro 10 cm è di per sé una garanzia di sicurezza fisica; l'intercettazione remota è praticamente impossibile.
- <strong>Chip di sicurezza</strong>: il telefono integra un chip di sicurezza dedicato (SE) o usa HCE (Host Card Emulation); le chiavi di pagamento sono conservate in un'area sicura e non possono essere estratte nemmeno con il telefono in root.
- <strong>Verifica impronta/volto</strong>: il pagamento richiede conferma biometrica, così anche se il telefono viene smarrito non si può frodare.
- <strong>Tokenizzazione</strong>: Apple Pay, Huawei Pay e simili non trasmettono il numero reale della carta, ma un token monouso; anche se intercettato, non può essere riusato.

##### Applicazioni tipiche:

- <strong>Carta bus / badge di accesso</strong>: si scrivono nel telefono le informazioni della carta fisica e si usa il telefono per transitare.
- <strong>Pagamento mobile</strong>: Apple Pay, Huawei Pay ecc., collegando la carta bancaria al telefono per pagare con un tocco.
- <strong>Accoppiamento dispositivi</strong>: NFC per accoppiare rapidamente cuffie e casse Bluetooth.
- <strong>Autenticazione d'identità</strong>: lettura di carte d'identità NFC, verifica della patente elettronica.

#### 6. Hotspot personale: trasforma il telefono in un router Wi-Fi

Quando hai molto traffico dati, puoi attivare l'hotspot per tablet e computer.

- <strong>Come attivarlo</strong>: Impostazioni > Hotspot personale / Tethering, e attivalo.
- <strong>Note</strong>: consuma molta batteria e traffico; imposta una password complessa e limita il numero di dispositivi connessi.
- <strong>Tethering USB</strong>: collega il computer con il cavo dati, più stabile e veloce del hotspot wireless.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Prova sul campo: configura e gestisci l'hotspot

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Apri [Impostazioni], trova "Hotspot personale" o "Tethering", attivalo e imposta nome e password.
2. Con un altro dispositivo (ad esempio il computer) cerca e connettiti a questo Wi-Fi.
3. Sul telefono verifica se riesci a gestire i dispositivi connessi o a espellere quelli sconosciuti.
:::
