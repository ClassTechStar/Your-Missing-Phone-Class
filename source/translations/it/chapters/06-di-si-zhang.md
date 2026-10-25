---
id: di-si-zhang
num: 04
part: ji-chu-pian
nav: Capitolo 4: Installare e gestire le App
toc: default
kind: chapter
---

### Capitolo 4: Installare e gestire le app — il "kit di competenze" del telefono

{class="chapter-intro mb-4"}
Le app rendono il telefono onnipotente, ma vanno anche gestite. Come assegni una postazione e dei permessi a un nuovo dipendente, anche l'installazione delle app richiede una procedura standard.

#### 1. Store ufficiali: il "supermercato delle app" più sicuro

- <strong>Android</strong>: Google Play (all'estero) o gli store di marca (come Huawei AppGallery, Xiaomi App Store).
- <strong>iOS</strong>: solo App Store.
- <strong>HarmonyOS</strong>: Huawei AppGallery.

Significato di sicurezza chiave: app revisionate, aggiornamenti garantiti, pagamenti sicuri. Linea guida operativa: <strong>scarica preferibilmente solo dagli store ufficiali!</strong>

#### 2. Modalità Pure/Protezione: attiva il "muro antivirus" del telefono

I principali brand cinesi (Huawei, Xiaomi, OPPO, vivo, Honor) integrano una <strong>Modalità Pure</strong> o <strong>Modalità Protezione</strong>: è un interruttore di sicurezza a livello di sistema. <strong>Consigliato a tutti gli utenti di attivarlo</strong>.

##### 1. Cos'è davvero?

La funzione principale della Modalità Pure (detta anche "Modalità Protezione") è <strong>bloccare l'installazione di app di terze parti</strong>: quando è attiva, il sistema <strong>consente di installare app solo dallo store ufficiale</strong>; i pacchetti di installazione scaricati da browser, QR code, software di chat e altri canali vengono direttamente intercettati, eliminando alla radice il malware.

##### 2. A chi è destinata

- <strong>Utenti anziani</strong>: non distinguono tra pubblicità "ufficiali" e "false"; la Modalità Pure è la protezione più sicura.
- <strong>Utenti poco attenti ai permessi delle app</strong>: non hanno bisogno di installare app di nicchia, versioni beta o giochi per mercati esteri.
- <strong>Tutti gli utenti che vogliono elevare la sicurezza del dispositivo</strong>: anche per i power user tenerla attiva è meglio — in caso di necessità temporanea, basta disattivarla una tantum.

##### 3. Percorso di attivazione (esempi Huawei/Xiaomi)

- <strong>Huawei/HarmonyOS</strong>: [Impostazioni] > [Sistema e aggiornamenti] > <strong>[Modalità Pure]</strong>, seleziona "Attiva".
- <strong>Xiaomi</strong>: [Impostazioni] > [Protezione privacy] > <strong>[Protezione privacy]</strong> oppure [Impostazioni] > [Impostazioni app] > [Installazione app], disattiva "Installa app da origini sconosciute".
- <strong>OPPO/vivo</strong>: [Impostazioni] > [Sicurezza] > <strong>[Installa app da fonti esterne]</strong>, revoca le autorizzazioni una per una.

{class="font-semibold mt-4 mb-1"}
##### 4. Meccanismi di verifica dello store

Lo store non è "decorativo": dietro c'è una pipeline di sicurezza completa:

- <strong>Scansione antivirus</strong>: prima della pubblicazione, ogni app viene scansionata congiuntamente da più motori antivirus, per identificare trojan e virus noti.
- <strong>Verifica dei permessi</strong>: lo store controlla che i permessi richiesti siano "ragionevoli" — un'app torcia che chiede l'accesso ai contatti? Rifiutata o rimossa.
- <strong>Certificazione dello sviluppatore</strong>: per pubblicare servono qualifiche aziendali, documento d'identità o carta di credito. In caso di problemi si risale a una persona, non è un'"app nera".
- <strong>Monitoraggio continuo</strong>: anche le app già pubblicate vengono rescansionate; nuovi comportamenti malevoli portano alla rimozione forzata.

#### 3. Fonti di terze parti e "parassiti elettronici": rischio altissimo!

Scaricare app da pagine web o link sconosciuti può portare virus, furto di privacy e frodi di pagamento. Qui introduciamo un nuovo concetto: il <strong>"parassita elettronico"</strong>.

::: div .danger-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-bug mr-2"></i>Cos'è un "parassita elettronico"?

{class="mt-1"}
Si tratta di <strong>software "craccati" con trojan incorporati</strong> — credi di "risparmiare", in realtà "ci caschi". Formi comuni:

{class="list-disc pl-6 mt-2 space-y-1 text-sm"}
- Versioni "crackate", "gratuite", "senza pubblicità" di software a pagamento;
- strumenti in zona grigia come "bot per like", "cattura-busta rossa", "cheat di gioco";
- cosiddette app "versione interna" sponsorizzate da "pubblicità minuta" nei gruppi di chat.

{class="mt-2"}
Questi programmi in apparenza funzionano, ma in background potrebbero <strong>rubare i contatti, leggere gli SMS, ascoltare il microfono, minare criptovalute</strong>. La Modalità Pure è la <strong>prima linea di difesa</strong> contro di loro — semplicemente non ti fa installare.
:::

##### Consigli per la seconda linea di difesa:

- <strong>Scansione antivirus completa periodica</strong>: usa il centro sicurezza integrato nel telefono (es. Huawei Phone Manager, Xiaomi Security Center) una volta al mese.
- <strong>Concedi con cautela i permessi sensibili</strong>: contatti, SMS, posizione, fotocamera, microfono — questi cinque "permessi ad alto rischio" vanno approvati rigorosamente.
- <strong>Monitora consumi anomali di batteria e traffico</strong>: telefono che si scalda all'improvviso, batteria che cala in fretta, traffico che scorre di notte — con tutta probabilità c'è un "parassita" in background.

Se proprio devi installare un'app di terze parti:

1. assicurati che la fonte sia assolutamente attendibile;
2. leggi con attenzione le richieste di permessi prima dell'installazione;
3. scansiona con un'app di sicurezza dopo l'installazione.

Consiglio definitivo: nelle impostazioni di sistema, disattiva il permesso "Installa app da origini sconosciute".

#### 4. Installare, aggiornare, disinstallare

- <strong>Installare</strong>: nello store tocca "Ottieni" o "Installa"; al primo avvio dopo l'installazione ti verranno richiesti i permessi.
- <strong>Aggiornare</strong>: <strong>obbligatorio!</strong> Serve soprattutto a correggere vulnerabilità di sicurezza. Consigliato attivare l'aggiornamento automatico.
- <strong>Disinstallare</strong>: tieni premuto sull'icona e trascinala nell'area di disinstallazione. Per pulire in modo più completo, vai in [Impostazioni] > [Gestione app] e disinstalla da lì.

#### 5. Gestione dei permessi: tu sei il "capo" delle app

Le richieste di permessi (come contatti o posizione) a volte sono ragionevoli (le mappe vogliono la posizione), a volte no (la torcia vuole i contatti).

```html
<ul class="list-disc pl-6 mb-3 space-y-1">
                        <li><strong>Opzioni di permesso</strong>: "Consenti sempre", "Consenti solo durante l'uso", "Negato", "Chiedi ogni volta".</li>
                        <li><strong>Principi di gestione</strong>:
                            <ol class="list-alpha pl-6 mt-1 space-y-1">
                                <li>Minimizzazione: non concedere se non necessario.</li>
                                <li>Revisione a posteriori: controlla periodicamente nelle impostazioni dei permessi chi "sfora".</li>
                                <li>Contestualizza: per le app di trasporto, concedi la posizione solo quando le usi.</li>
                            </ol>
                        </li>
                    </ul>
```

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-shield-alt mr-2"></i>Permessi da tenere sotto stretta sorveglianza

{class="list-disc pl-6 mt-1 space-y-1"}
- Contatti/SMS: potrebbero essere usati per inviare SMS spam.
- Posizione in tempo reale: potresti essere localizzato.
- Fotocamera/Microfono: rischio di riprese occulte.
- Accesso ai file: potrebbe leggere i tuoi file privati.
:::

{id="di-si-zhang-apk"}
#### 6. Elementi che compongono un pacchetto di installazione

Ti sei mai chiesto cosa ci sia dentro il pacchetto scaricato dallo store? Conoscere la struttura del pacchetto ti aiuta a capire come funzionano le app e a sapere da dove iniziare quando qualcosa non va.

##### 1. Struttura del file APK Android

L'APK (Android Package Kit) è in sostanza un archivio ZIP; scompattandolo si trovano le seguenti cartelle e file principali:

- <strong>AndroidManifest.xml</strong>: la "carta d'identità" e il "manuale" dell'app. Registra il nome del pacchetto, la versione, i permessi richiesti, le versioni di sistema supportate, l'Activity di ingresso e altre informazioni chiave. Il sistema lo legge per primo quando installa l'app.
- <strong>classes.dex</strong>: il codice centrale dell'app. Il codice sorgente Java/Kotlin, dopo la compilazione, diventa bytecode Dalvik salvato in questo file. Un'app può avere più file dex (come classes2.dex, classes3.dex).
- <strong>resources.arsc</strong>: tabella di indice delle risorse compilata. Registra gli ID di tutte le risorse e le relative corrispondenze.
- <strong>res/</strong>: cartella delle risorse. Contiene immagini, file di layout, stringhe, definizioni di colore. Le immagini per risoluzioni diverse sono in cartelle drawable diverse (come drawable-hdpi, drawable-xhdpi).
- <strong>assets/</strong>: cartella delle risorse raw. Contiene risorse non compilate, come file web, font, audio. L'app le legge tramite AssetManager in fase di esecuzione.
- <strong>lib/</strong>: cartella delle librerie native. Contiene i file .so compilati (prodotto della compilazione C/C++), suddivisi per architettura CPU (come arm64-v8a, armeabi-v7a). I giochi e le app che richiedono calcoli ad alte prestazioni di solito hanno questa cartella.
- <strong>META-INF/</strong>: cartella delle informazioni di firma. Contiene tre file (MANIFEST.MF, CERT.SF, CERT.RSA) per verificare l'integrità e la firma dell'APK.

##### 2. Struttura del file IPA iOS

Anche l'IPA (iOS App Store Package) è un archivio compresso, con una struttura leggermente diversa:

- <strong>Payload/</strong>: dove si trova il contenuto principale. All'interno c'è una cartella .app con tutto il contenuto dell'app.
- <strong>Info.plist</strong>: file di configurazione dell'app, simile all'AndroidManifest.xml di Android. Registra l'ID dell'app, la versione, i permessi richiesti, i dispositivi supportati ecc.
- <strong>Eseguibile</strong>: il programma principale con lo stesso nome della cartella .app, un file binario in formato Mach-O compilato.
- <strong>Frameworks/</strong>: librerie dinamiche e framework da cui dipende l'app.
- <strong>File di risorse</strong>: immagini, audio, video e altre risorse, di solito conservate nella cartella .app.
- <strong>_CodeSignature/</strong>: informazioni sulla firma del codice, per verificarne l'integrità e la provenienza.

##### 3. Meccanismo di verifica della firma

Perché le app scaricate dallo store ufficiale sono più sicure? La verifica della firma è la chiave.

```html
<ul class="list-disc pl-6 mb-3 space-y-1">
                        <li><strong>Firma Android</strong>: lo sviluppatore firma l'APK con una chiave privata e il sistema verifica con la chiave pubblica in fase di installazione. Se l'APK viene manomesso (ad esempio con un virus iniettato), la firma non è più valida e il sistema rifiuta l'installazione. Google Play richiede inoltre l'App Signing, con Google che conserva le chiavi di firma per proteggere ulteriormente l'app.</li>
                        <li><strong>Firma iOS</strong>: la revisione di Apple è più rigorosa. Ogni IPA deve avere la firma di un certificato rilasciato da Apple, altrimenti non si installa. Ecco perché su iOS si può installare solo da App Store o con certificati enterprise. Le app firmate con certificati enterprise hanno validità limitata e Apple può revocarle in qualsiasi momento.</li>
                        <li><strong>Ruolo della firma</strong>:
                            <ol class="list-alpha pl-6 mt-1 space-y-1">
                                <li>Verifica della provenienza: conferma che l'app viene davvero dallo sviluppatore dichiarato.</li>
                                <li>Verifica dell'integrità: assicura che l'app non sia stata manomessa in transito.</li>
                                <li>Prevenzione dell'imitazione: le app malevole non possono fingersi altre app.</li>
                            </ol>
                        </li>
                    </ul>
```

##### 4. Dimensione del pacchetto e ottimizzazione

Potresti notare che la dimensione mostrata nello store e quella occupata dopo l'installazione non coincidono. Questo perché:

- <strong>Dimensione di download</strong>: la dimensione dell'APK/IPA compresso.
- <strong>Dimensione di installazione</strong>: la dimensione dopo la decompressione, in genere molto più grande del download.
- <strong>Occupazione a runtime</strong>: l'app genera cache e file di dati durante l'esecuzione, occupando ulteriore spazio.

Tecniche di ottimizzazione delle app moderne:

- <strong>App Bundle (Android)</strong>: tecnologia di distribuzione dinamica di Google Play. L'utente scarica solo le risorse adatte al proprio dispositivo (ad esempio solo le immagini per la risoluzione del proprio schermo), riducendo drasticamente la dimensione del download.
- <strong>App Thinning (iOS)</strong>: tecnologia simile; Apple ritaglia automaticamente le risorse non necessarie in base al dispositivo.
- <strong>Download on demand</strong>: le app di grandi dimensioni, come i giochi, possono prima scaricare un pacchetto base e poi i pacchetti di risorse successivi.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Curiosità: perché alcune app hanno pacchetti di installazione tanto grandi?

{class="mt-1"}
Le app di gioco sono in genere le più grandi, perché contengono moltissime texture HD, modelli 3D e file audio. Anche le app social sono piuttosto grandi, perché devono supportare molti moduli funzionali. Le app tool sono in genere le più piccole. Se noti che un'app tool è insolitamente grande, diffida di eventuali funzioni superflue incorporate.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Attività pratica: revisiona i permessi di 3 app

{class="mt-1"}
Scegli 3 app che usi spesso (ad esempio social, shopping, tool), entra nella pagina di gestione dei permessi delle app in [Impostazioni], revisiona voce per voce e disattiva i permessi sensibili non necessari o cambiali in "Consenti solo durante l'uso".
:::
