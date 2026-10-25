---
id: di-er-shi-wu-zhang
num: 25
part: chao-yue-pian
nav: Capitolo 25: Gestire gli smartphone usati e l'eredità digitale
toc: default
kind: chapter
---

### Capitolo 25: Gestione del telefono usato ed eredità digitale

{class="chapter-intro mb-4"}
Ehi ragazzi, dopo oltre venti capitoli di "addestramento", dovresti essere cresciuto da "novizio digitale" a un utilizzatore di telefoni abbastanza disinvolto. Ma la vita tecnologica ha i suoi cicli — il nuovo amore diventa vecchio. Quando decidi di "ritirare" il tuo vecchio compagno, sai come salutarlo in modo dignitoso e sicuro?

#### 1. "Eutanasia" del vecchio telefono: guida alla vendita o donazione sicura

Principio chiave: la pulizia dei dati non è "eliminazione", ma "sovrascrittura". Molti pensano che spostando le foto nel cestino e svuotando l'album sia tutto a posto; poi, dopo la cessione, il nuovo proprietario con un software di recupero dati ritrova vecchie foto, cronologia chat, foto della carta d'identità — queste "figuracce sociali" si ripetono ogni anno.

1. <strong>"Pulizia generale" fai da te</strong>: completa l'ultimo backup integrale, esci da tutti gli account (iCloud, Huawei/Xiaomi/Samsung, Google), disattiva "Trova il mio telefono" — altrimenti il prossimo utente sarà bloccato dal blocco attivazione.
2. <strong>"Formattazione" finale</strong>: il "ripristino di fabbrica" dei telefoni moderni di solito include una cancellazione crittografata — distrugge la chiave di cifratura stessa; una volta persa la chiave, tutti i dati sul disco diventano immediatamente illeggibili.
3. <strong>Ultimo "trucco di mascheramento" (solo per vecchi dispositivi)</strong>: i telefoni moderni (iOS 8+, Android 6+) hanno già la crittografia completa del disco (FBE) predefinita; il ripristino di fabbrica distrugge la chiave di cifratura, i dati sono teoricamente irreversibili, <strong>questo passaggio non serve</strong>. Solo per dispositivi molto vecchi non crittografati (anteriore al 2015) può essere necessario, dopo il ripristino di fabbrica, riempire la memoria con file spazzatura e poi eseguire di nuovo il ripristino.

<strong>Tabella di consultazione rapida dei percorsi di cancellazione dati per brand</strong>: pur essendo simili i principi, ogni brand nasconde il "ripristino di fabbrica" in posizioni leggermente diverse; le differenze chiave sono le seguenti.

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Brand</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Punto di accesso alla cancellazione</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Differenze chiave e avvertenze</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Huawei</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Impostazioni > Sistema e aggiornamenti > Ripristina > Ripristino dati di fabbrica</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prima uscire dall'account Huawei e disattivare "Trova il mio telefono", altrimenti si innesca il blocco attivazione; in modalità pura può essere richiesta la verifica della password.</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xiaomi / Redmi</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Impostazioni > Il mio dispositivo > Ripristino dati di fabbrica</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">In fondo ci sono le opzioni "Formatta SD virtuale" e "Cancella tutti i contenuti e le impostazioni": entrambe vanno spuntate; prima di uscire dall'account Xiaomi disattivare "Trova dispositivo".</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OPPO / OnePlus</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Impostazioni > Altre impostazioni > Ripristina telefono > Cancella completamente tutti i dati</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ColorOS offre una modalità "cancellazione completa" che sovrascrive più volte la memoria; richiede la password di sblocco schermo per la conferma.</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">vivo</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Impostazioni > Gestione sistema > Backup e ripristino > Cancella tutti i dati</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Spuntare "Formatta memoria telefono" per pulire anche l'area SD; uscire dall'account vivo, disattivare "Trova telefono".</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Samsung</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Impostazioni > Gestione generale > Ripristina > Ripristino dati di fabbrica</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prima rimuovere l'account Samsung e disattivare "Trova il mio telefono"; alcuni modelli hanno un'opzione di "sovrascrittura automatica", consigliata.</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">iPhone</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Impostazioni > Generale > Trasferisci o inizializza iPhone > Inizializza tutti i contenuti e le impostazioni</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bisogna prima uscire dall'Apple ID, altrimenti il prossimo utente è bloccato dal blocco attivazione iCloud; iOS 15+ supporta "mantieni dati iCloud all'uscita" per verifiche future.</td>
                            </tr>
                        </tbody>
                    </table>
```

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Le tre cose più facilmente trascurate

{class="list-disc pl-6 mt-2 space-y-1"}
- <strong>Non essere usciti dall'account</strong>: dopo la vendita il telefono viene bloccato in remoto, e non riesci più a uscirne; alla fine devi andare con il documento dal servizio ufficiale per sbloccarlo.
- <strong>Non aver rimosso la SD</strong>: il ripristino di fabbrica non formatta le foto sulla SD esterna, ricordati di estrarla o formattarla separatamente.
- <strong>Periferiche USB/OTG non scollegate</strong>: se durante la cancellazione ci sono periferiche collegate, potresti cancellare per sbaglio i loro dati o interrompere la cancellazione.
:::

#### 2. Eredità digitale: dove collocare la tua anima sociale?

I dati nel telefono non sono più "virtuali" da tempo. Portano il tuo denaro, le relazioni sociali, le opere che hai creato e persino la tua "identità digitale". <strong>Quando una persona muore, come vanno gestiti questi asset?</strong> Non è più una questione astratta, ma un problema reale per sempre famiglie: i parenti non conoscono le password, le piattaforme non permettono l'eredità, le criptovalute sono perse per sempre.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-gavel mr-2"></i>Base giuridica: art. 49 della Legge sulla protezione delle informazioni personali

{class="mt-1"}
L'art. 49 della "Legge della Repubblica Popolare Cinese sulla protezione delle informazioni personali", in vigore dal 2021, stabilisce chiaramente: <strong>in caso di morte di una persona fisica, i parenti prossimi, per un loro interesse legittimo e giustificato, possono esercitare sui dati personali del defunto i diritti di consultazione, copia, rettifica e cancellazione previsti in questo capitolo; salvo diversa disposizione lasciata dal defunto in vita.</strong>

{class="mt-2"}
Ciò significa:

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>I parenti prossimi hanno un fondamento giuridico</strong> per chiedere alle piattaforme di gestire account e dati personali del defunto.
- L'"interesse legittimo e giustificato" di solito include la gestione dell'eredità, la chiusura degli account, l'eliminazione di privacy sensibile.
- Se il defunto aveva disposto diversamente con testamento o accordo (ad esempio designando un contatto per l'eredità), si segue la sua volontà.
- Le piattaforme non possono rifiutarsi a priori di collaborare in nome della "privacy dell'utente", ma le procedure specifiche variano.
:::

{class="font-semibold mt-4 mb-1"}
##### 1. WeChat e Alipay: l'account non si eredita, ma il denaro sì

Queste due app, le più usate dai cinesi, hanno regole diverse:

- <strong>Account WeChat</strong>: secondo la "Licenza e accordo di servizio del software Tencent WeChat", la proprietà dell'account spetta a Tencent, l'utente ha solo il diritto di uso; <strong>l'account in sé non è ereditabile e non è cedibile</strong>. Ma le <strong>giacenze di cambio e i fondi di Qianlitong</strong> nell'account sono beni personali: i parenti prossimi possono chiederne il prelievo o il trasferimento a Tenpay con certificato di morte, certificato di parentela e atto notarile di successione.
- <strong>Alipay</strong>: anche l'account non è direttamente ereditabile, ma il saldo Alipay, Yu'ebao, Licaitong e altri <strong>fondi sono beni ereditabili</strong>. Gli eredi possono rivolgersi all'assistenza Alipay o presentare di persona certificato di morte e atto notarile di successione; i prodotti di investimento di Ant Fortune richiedono la procedura della società di fondi.
- <strong>Cronologia chat</strong>: legalmente è privacy personale, la piattaforma non la fornisce spontaneamente alla famiglia. Se è rilevante per l'eredità, può essere ottenuta tramite cause o richiesta notarile.

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Cose da non fare mai

{class="list-disc pl-6 mt-2 space-y-1"}
- <strong>Non consegnare direttamente a un familiare le password del defunto "per continuare a usarlo"</strong> — viola l'accordo di piattaforma, e se i fondi vengono congelati o si innesca il controllo rischi, è più difficile fornire prove.
- <strong>Non provare a "prelevare" usando il telefono del defunto per ricevere i codici di verifica</strong> — può essere considerato furto d'uso, con possibili conseguenze penali.
- <strong>Non temporeggiare</strong>: alcuni account, dopo lungo periodo di inattività, vengono cancellati automaticamente; recuperare i fondi diventa più complicato.
:::

{class="font-semibold mt-4 mb-1"}
##### 2. "Contatto per l'eredità" di Apple: designarlo prima rende tutto più facile

Da iOS 15.2 Apple ha introdotto la funzione "Contatto per l'eredità", che permette di designare in anticipo un contatto fidato; dopo il decesso, questi può richiedere l'accesso ai dati iCloud del defunto (foto, note, contatti, memo, ecc.) con il <strong>certificato di morte + chiave di accesso del contatto per l'eredità</strong>. Passaggi:

1. Sull'iPhone vai su <strong>[Impostazioni] &gt; [il tuo nome] &gt; [Accesso e sicurezza] &gt; [Contatto per l'eredità]</strong>.
2. Tocca "Aggiungi contatto per l'eredità", conferma l'identità con Face ID.
3. Scegli il contatto (dalla rubrica), il sistema genererà una <strong>chiave di accesso</strong>.
4. Consegna la chiave al contatto tramite SMS, email o stampa cartacea, ricordandogli di custodirla con cura.
5. Puoi aggiungere più contatti come backup, per evitare un singolo punto di fallimento.

La persona designata non ha bisogno di un dispositivo Apple: con chiave e certificato di morte può richiedere l'accesso sul sito Apple. L'intera procedura di solito si completa in 7 giorni.

{class="font-semibold mt-4 mb-1"}
##### 3. "Gestione account inattivo" di Google: gestire il dopo di noi in automatico

Google offre l'"Inactive Account Manager", in grado di eseguire automaticamente operazioni presetstate dopo un lungo periodo di inattività dell'utente — è uno dei meccanismi di eredità digitale più completi attualmente disponibili.

1. Visita <strong>myaccount.google.com/inactive</strong>, accedi al tuo account Google.
2. Imposta il periodo di timeout: 3 / 6 / 12 / 18 mesi di inattività prima dell'attivazione.
3. Aggiungi contatti fidati (massimo 10), impostando per ciascuno a quali dati può accedere (Gmail, Foto, Drive, ecc.).
4. Opzionale: imposta una risposta email automatica che informi chi ti scrive che non puoi più rispondere.
5. Scegli infine: alla scadenza, <strong>condividere i dati con i contatti</strong> oppure <strong>cancellare direttamente l'account</strong>.
6. Imposta un numero di telefono come verifica di fallback, per evitare attivazioni per errore.

{class="font-semibold mt-4 mb-1"}
##### 4. Account social cinesi: commemorazione e cancellazione

Le principali piattaforme social cinesi trattano gli account dei defunti in due modi: <strong>"commemorazione" (mantenere l'account per il ricordo dei familiari)</strong> e <strong>"cancellazione" (eliminazione completa)</strong>. I familiari possono fare richiesta all'assistenza della piattaforma con certificato di morte, certificato di parentela e documento d'identità del richiedente.

- <strong>Weibo</strong>: supporta la "commemorazione" dell'account, su richiesta di un familiare con certificato di morte; l'account viene bloccato, non è più accessibile ma i contenuti restano, e sulla home compare "Questo account è stato impostato come account commemorativo". Si può anche chiedere la cancellazione, fornendo un atto notarile di successione.
- <strong>Douyin (TikTok Cina)</strong>: tramite "Io - Impostazioni - Feedback e aiuto - Account e sicurezza - Disattivazione account" o via assistenza, si presentano certificato di morte, certificato di parentela e documento del richiedente; dopo l'approvazione si può disattivare o trasformare in account commemorativo.
- <strong>Bilibili</strong>: tramite assistenza si presentano certificato del defunto e certificato di parentela; si può chiedere la disattivazione o la conservazione come pagina commemorativa; il trattamento dei contenuti caricati dall'UP deve tener conto delle dichiarazioni di copyright.
- <strong>Xiaohongshu</strong>: tramite assistenza ufficiale, con certificato di morte e certificato di parentela, si può richiedere la disattivazione dell'account e la cancellazione dei contenuti.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Promemoria chiave

{class="list-disc pl-6 mt-2 space-y-1"}
- Le regole delle piattaforme si aggiornano: prima di procedere consulta le ultime indicazioni dell'assistenza ufficiale.
- Si consiglia di scansionare e fare backup di tutti i documenti prima di consegnarli, conservando con cura gli originali.
- Per procedure una tantan su più piattaforme, si può richiedere un unico <strong>atto notarile di successione</strong>, evitando di ripetere più volte le pratiche.
:::

{class="font-semibold mt-4 mb-1"}
##### 5. La complessa successione degli asset digitali

Oltre agli account social, sempre più persone detengono <strong>asset digitali di vero valore</strong>, la cui successione è più complessa:

- <strong>Criptovalute (Bitcoin, Ethereum, ecc.)</strong>: sul principio "la chiave privata è la proprietà", <strong>senza chiave privata l'asset è perso</strong>. Gli eredi non possono "ricorrere" on-chain con documenti legali. Consiglio: conservare la seed phrase/chiave privata in frammenti in più posizioni fisiche sicure (come cassetta di sicurezza in banca + cassaforte di casa) e indicare nel testamento le modalità di accesso.
- <strong>Account sugli exchange</strong>: come i conti bancari, si può chiedere agli exchange (come Binance, OKX) la gestione con atto notarile di successione, ma le procedure su exchange cross-border sono lunghe.
- <strong>Domini</strong>: sono beni ereditabili; gli eredi possono trasferirli presso il registrar (come Alibaba Cloud, GoDaddy) presentando l'atto notarile di successione.
- <strong>Diritti di proprietà intellettuale (articoli originali, video, brevetti, diritti d'autore del software)</strong>: i diritti patrimoniali del diritto d'autore sono ereditabili (i diritti morali no); il diritto ai proventi spetta agli eredi fino a 50 anni dopo la morte dell'autore.
- <strong>Cloud storage e netdisk</strong>: i dati personali sono ereditabili; ma alcuni accordi di piattaforma prevedono che l'account non sia cedibile: occorre prima scaricare e poi disattivare.

::: div .danger-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>Il vero costo della "scomparsa" delle criptovalute

{class="mt-1"}
Secondo un rapporto Chainalysis, nel mondo sono già andati persi per sempre <strong>oltre 3 milioni di Bitcoin</strong> a causa di chiavi private smarrite, pari a circa un sesto del totale esistente. Se detieni criptoattività, assicurati che almeno una persona di assoluta fiducia conosca il <strong>percorso di recupero</strong> — altrimenti queste ricchezze resteranno per sempre addormentate sulla blockchain.
:::

{class="font-semibold mt-4 mb-1"}
##### 6. Un modello di "testamento digitale"

Il testamento patrimoniale tradizionale non copre gli asset digitali. Si consiglia di aggiornare ogni anno un allegato "testamento digitale", da conservare insieme al testamento ufficiale. Modello di riferimento:

::: div .bg-light .dark:bg-gray-700 .rounded-lg .p-4 .mt-2 .mb-3 .text-sm
{class="font-semibold mb-2"}
"Allegato per la gestione degli asset digitali personali" (modello)

{class="mb-1"}
<strong>Parte 1: elenco account</strong> (registra solo nome utente e piattaforma, <strong>non le password</strong>)

{class="list-disc pl-6 mb-2 space-y-0.5"}
- Social: WeChat (account xxx), Weibo, Douyin, Bilibili, Xiaohongshu, ecc.
- Pagamenti: Alipay, WeChat Pay, app delle varie banche
- Cloud: iCloud, Huawei Cloud, Mi Cloud, account Google, account Microsoft
- Email: QQ Mail, NetEase Mail, Gmail, ecc.
- Altro: netdisk, servizi in abbonamento, account di gioco, ecc.

{class="mb-1"}
<strong>Parte 2: soluzione di custodia delle password</strong>

{class="list-disc pl-6 mb-2 space-y-0.5"}
- Custodia della password principale: usa un password manager (come Bitwarden, 1Password); la password principale è scritta su carta sigillata nella cassaforte di casa.
- Chiavi di recupero/seed phrase: custodite a frammenti, almeno in due posizioni fisiche (come cassetta in banca + cassaforte di casa).
- Persona autorizzata alla consultazione: nome, documento d'identità, rapporto con l'interessato, contatto.

{class="mb-1"}
<strong>Parte 3: volontà di gestione</strong>

{class="list-disc pl-6 mb-2 space-y-0.5"}
- Per ciascun account, preferenza tra "commemorazione" e "cancellazione".
- Se per iCloud / Google dati si designa un "contatto per l'eredità" o si imposta l'"Inactive Account Manager".
- Chi eredita le criptoattività, con spiegazione del percorso per ottenere la chiave privata.
- A chi spettano i proventi delle opere coperte da diritto d'autore.

{class="mb-1"}
<strong>Parte 4: contatti e piattaforme</strong>

{class="list-disc pl-6 space-y-0.5"}
- Esecutore fiduciario: nome, contatto, contatto di backup.
- Elenco degli accessi all'assistenza delle piattaforme e dei documenti necessari.
- Data di aggiornamento dell'allegato: ____/__/__; prossima revisione: ____/__/__.
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Nota legale sulle "password"

{class="mt-1"}
Scrivere le password direttamente nel testamento comporta rischi di fughe di informazioni; una volta pubblicato, tutti gli eredi potrebbero vederle. <strong>È più prudente: nel testamento inserire solo "elenco account + volontà + luogo di custodia delle password", e trasmettere la vera password — tramite la master password del password manager — solo all'esecutore fiduciario</strong>. Così si rispettano le esigenze legali e si riduce il rischio di fughe.
:::

#### 3. L'ultimo viaggio ecosostenibile

Un telefono contiene decine di metalli tra cui oro, argento, rame e terre rare; disfarsene a caso inquina il suolo e spreca risorse. I canali di riciclo corretti sono tre, con punti di forza diversi:

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Canale</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Prezzo di recupero</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Sicurezza dati</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Scenario d'uso</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Permuta ufficiale (Huawei/Apple/Xiaomi, ecc.)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Medio, spesso con buoni integrati</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Massima, con procedure ufficiali</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Più conveniente quando si passa a un nuovo telefono dello stesso brand</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Piattaforma di riciclo di terze parti (Aihuishou, Zhuanzhuan, Huishoubao, ecc.)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Leggermente super, confrontabile</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Alta, con report di cancellazione dati</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Per chi vuole monetizzare direttamente, senza vincoli di brand</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Donazione di beneficenza (scuole di campagna, enti benefici)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nessun ritorno economico</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Richiede cancellazione autonoma completa</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dispositivo ancora funzionante, voglia di fare del bene</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Riutilizzo (ritenuto e modificato)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Risparmio su un nuovo dispositivo</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Continua a essere usato dal proprietario originale, nessun rischio</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dispositivo ancora performante, esigenze di riuso in casa</td>
                            </tr>
                        </tbody>
                    </table>
```

- <strong>Riciclo/permuta ufficiale</strong>: la soluzione più consigliata, procedure standard e sicurezza dei dati garantita. I siti di Apple, Huawei, Xiaomi hanno sezioni "permuta" dove, dopo valutazione, si ottiene uno sconto sul nuovo telefono.
- <strong>Piattaforme di riciclo regolari</strong>: scegli grandi piattaforme con buona reputazione; dopo l'ordine, ritiro a domicilio e pagamento dopo verifica. Scegli sempre piattaforme che <strong>forniscono un "report di cancellazione dati"</strong> e conservane la ricevuta.
- <strong>Donazione di beneficenza</strong>: puoi contattare scuole di campagna locali o organizzazioni no profit; i vecchi telefoni possono essere riadattati come tablet didattici o telefoni per anziani. <strong>Prima della donazione esegui sempre la procedura completa di cancellazione e rimuovi SIM/SD</strong>.
- <strong>Riutilizzo</strong>: trasformalo in navigatore auto, centro di controllo domotico, telecamera di sorveglianza, baby monitor, cornice digitale. Un vecchio telefono può ancora rendere per anni.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-leaf mr-2"></i>La verità sui rifiuti elettronici

{class="mt-1"}
Il circuito di un telefono contiene metalli preziosi come <strong>oro, argento, palladio, rame</strong>; ogni tonnellata di circuiti usati contiene decine di volte più oro di un minerale aurifero. Ma se smaltito in modo scorretto, il piombo, il mercurio e il cadmio penetrano nel suolo e nelle falde, inquinando per decenni. <strong>Un riciclo corretto protegge l'ambiente e rimette in circolo metalli scarsi.</strong>
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Pratica: un "funerale standard" per il tuo vecchio telefono

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Ultimo backup completo: carica le foto sul cloud, copia i file importanti sul computer, esporta la cronologia chat.
2. Esci da tutti gli account: iCloud / Huawei / Xiaomi / Google, disattiva "Trova il mio telefono".
3. Estrai SIM e SD, scollega tutte le periferiche OTG.
4. Esegui il ripristino di fabbrica con cancellazione crittografata, se necessario spuntando manualmente "formatta memoria".
5. (Solo vecchi dispositivi) Riempi la memoria con file spazzatura e fai di nuovo il ripristino di fabbrica.
6. Scegli la sua prossima tappa: permuta ufficiale, piattaforma di riciclo regolare, donazione di beneficenza o donazione a un familiare.
7. Aggiorna il tuo "elenco eredità digitale", cancellando i dispositivi dismessi.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-calendar-check mr-2"></i>Lista delle mansioni del mese

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Per il tuo telefono principale, designa un "contatto per l'eredità" Apple o imposta l'"Inactive Account Manager" di Google.
2. Usa il modello di questa sezione per redigere un "Allegato per la gestione degli asset digitali personali" e accordati con la famiglia sul luogo di conservazione.
3. Verifica se in casa ci sono 2 o più vecchi telefoni inutilizzati e prenota un ritiro ufficiale o su piattaforma regolare.
:::
