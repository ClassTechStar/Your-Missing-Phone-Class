---
id: di-er-shi-si-zhang
num: 24
part: chao-yue-pian
nav: Capitolo 24: Permessi di root e blocco BL spiegati a fondo
toc: default
kind: chapter
---

### Capitolo 24: Permessi Root e BL lock in profondità

{class="chapter-intro mb-4"}
Questo capitolo è un approfondimento del Capitolo 20, adatto a chi vuole capire davvero i meccanismi di basso livello del telefono o persino cimentarsi nel flashing. Attenzione: queste operazioni comportano rischi, procedi con cautela.

#### 1. Comprendere a fondo il Bootloader

Il Bootloader è il primo programma eseguito all'avvio del telefono; il suo compito è inizializzare l'hardware e caricare il kernel del sistema operativo. Puoi considerarlo come il "buttafuori" del telefono.

##### Principio di funzionamento del BL lock:

- <strong>Verifica della firma</strong>: il BL lock verifica la firma digitale dell'immagine di avvio; solo i sistemi firmati dal produttore possono essere avviati.
- <strong>Prevenzione del downgrade</strong>: impedisce all'utente di flashare versioni precedenti del sistema per sfruttare vulnerabilità note.
- <strong>Protezione dei dati</strong>: anche se si flasha un nuovo sistema, senza l'account e la password originali non è possibile accedere ai dati utente.

##### 🔐 Archiviazione e verifica a livello hardware

Lo stato del BL lock (Locked/Unlocked) e la chiave pubblica del produttore sono di solito memorizzati in un'area hardware protetta (come la partizione devinfo di Qualcomm, eFuse o partizione RPMB), per impedire manomissioni software. A ogni avvio, il Bootloader legge lo stato da questa area sicura e in base a ciò decide se eseguire o meno una verifica rigorosa della firma.

##### 🔏 Verifica della firma digitale

Quando il produttore rilascia un aggiornamento di sistema o un'immagine, la firma con la propria chiave privata. All'avvio del dispositivo, il Bootloader usa la chiave pubblica integrata per verificare l'immagine di sistema (come boot.img, recovery.img). Il funzionamento è:

1. Ricalcola l'hash dell'immagine di sistema.
2. Decrittografa con la chiave pubblica la firma contenuta nell'immagine, ottenendo un hash.
3. Confronta i due hash: se coincidono, la verifica ha esito positivo. Questo garantisce che l'immagine di sistema non sia stata manomessa da terzi.

##### 🔗 Catena di avvio sicura

Il BL lock è il primo anuncio dell'intera catena di avvio sicura. Solo dopo che la sua verifica ha esito positivo, carica ed esegue il programma di bootstrap della fase successiva (come il kernel), garantendo così stratificatamente l'attendibilità dell'ambiente di avvio del sistema.

##### 📊 Lock vs Unlock: il duplice impatto del BL lock

Per capire in modo più intuitivo pro e contro del BL lock, usiamo una tabella comparativa che mostra le differenze su 5 dimensioni chiave:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 dark:border-gray-600 text-sm">
                            <thead>
                                <tr class="bg-gray-100 dark:bg-gray-800">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Funzione chiave</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Stato bloccato (default)</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Stato dopo lo sblocco</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Sicurezza di sistema</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Impedisce di flashare sistemi non ufficiali non firmati, proteggendo l'integrità del sistema e la sicurezza di basso livello<br><span class="text-emerald-600 dark:text-emerald-400">✅ Alta sicurezza: carica solo immagini firmate ufficialmente, respingendo efficacemente le manomissioni malevole del firmware</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ Sicurezza ridotta: consente di flashare ROM di terze parti, il meccanismo di verifica dell'integrità del sistema viene meno; se un malware ottiene i permessi Root può alterare profondamente il sistema</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Stabilità del sistema</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Garantisce che il telefono esegua il sistema ufficiale testato e ottimizzato dal produttore, assicurando stabilità e scorrevolezza<br><span class="text-emerald-600 dark:text-emerald-400">✅ Stabile: usa firmware ufficiali, funzioni complete, aggiornamenti OTA affidabili</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ Più rischi: le ROM di terze parti possono avere problemi di compatibilità, possono causare crash, brick, malfunzionamenti hardware (come fotocamera, ricarica rapida), gli aggiornamenti OTA possono fallire</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Diritti di garanzia</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Il produttore fornisce un sistema ufficiale stabile bloccando il BL, per offrire il servizio di garanzia<br><span class="text-emerald-600 dark:text-emerald-400">✅ Garanzia valida: goditi la garanzia gratuita ufficiale (danni non dolosi)</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ Garanzia persa: la maggior parte dei produttori considera lo sblocco del BL come rinuncia volontaria alla garanzia; anche ribloccando, lo storico di sblocco può essere rilevato e la garanzia rifiutata</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Sicurezza dei dati</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Il processo di sblocco di solito cancella i dati, per evitare che i vecchi dati siano sfruttati malevolmente nel nuovo ambiente di sistema<br><span class="text-emerald-600 dark:text-emerald-400">✅ Dati sicuri: nell'uso quotidiano, il BL lock limita la capacità dei malware di modificare le partizioni di sistema</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ Rischio per i dati: lo sblocco cancella forzatamente tutti i dati utente; se dopo lo sblocco non cifri correttamente, la memorizzazione dei dati può essere insicura; in caso di smarrimento, i dati sono più facilmente estraibili tramite flashing</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Limitazioni funzionali</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Garantisce il funzionamento di funzioni che dipendono da un ambiente sicuro (come pagamenti, app bancarie)<br><span class="text-emerald-600 dark:text-emerald-400">✅ Funzioni complete: tutte le funzioni ufficiali sono utilizzabili</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ Funzioni limitate: alcune app sensibili alla sicurezza (come Google Pay, app bancarie) possono rifiutarsi di girare rilevando lo stato di BL sbloccato; i servizi DRM possono essere declassati, con impatto sulla riproduzione di video ad alta definizione</span></td>
                                </tr>
                            </tbody>
                        </table>
```
:::

#### 2. Procedura dettagliata di sblocco del BL lock (esempio Xiaomi)

1. <strong>Richiedere l'autorizzazione di sblocco</strong>: sul sito dell'utility di sblocco Xiaomi.
2. <strong>Associare l'account</strong>: nelle impostazioni del telefono, collega l'account Xiaomi.
3. <strong>Periodo di attesa</strong>: in base al livello dell'account, da 7 a 30 giorni.
4. <strong>Operazione di sblocco</strong>: usa l'utility di sblocco Xiaomi collegando il telefono al PC.

#### 3. Diverse soluzioni per il Root

- <strong>Magisk</strong>: soluzione Root moderna, design Systemless, può nascondere lo stato di Root.
- <strong>KernelSU</strong>: soluzione Root basata sul kernel, più di basso livello, nascondimento migliore.
- <strong>SuperSU</strong>: soluzione Root storica, oggi non più aggiornata.

#### 4. Introduzione al flashing

Per flashing si intende l'installazione di un nuovo sistema operativo sul telefono. Tipi comuni:

- <strong>Flash di ROM ufficiale</strong>: installazione del sistema ufficiale, per ripristinare un brick o fare un downgrade.
- <strong>Flash di Recovery di terze parti</strong>: come TWRP, per backup/ripristino e flash di ROM di terze parti.
- <strong>Flash di ROM di terze parti</strong>: come LineageOS, Pixel Experience, per provare sistemi diversi.

#### 5. Samsung Knox: il prezzo irreversibile dello sblocco BL

A differenza di altri produttori Android, il meccanismo di sblocco BL dei telefoni Samsung ha un design "fuse" unico: <strong>per i telefoni Samsung, lo sblocco innesca il fuse Knox, perdendo permanentemente alcune funzioni di sicurezza (come Samsung Pay); cancella tutti i dati protetti; influisce sulla garanzia</strong>. Nel dettaglio:

- <strong>Il fuse è monouso</strong>: nel telefono c'è un fusibile eFuse, che si brucia in modo permanente non appena rileva lo sblocco del BL, senza possibilità di ripristino.
- <strong>Funzioni interessate</strong>: Samsung Pay (carte di trasporto/bancarie), cartella protetta Knox, gestione MDM aziendale, alcune app di assicurazione sanitaria smettono di funzionare.
- <strong>Cancellazione obbligatoria dei dati</strong>: quando il fuse scatta, il telefono forza un ripristino di fabbrica, tutti i dati locali vengono cancellati (i dati cloud non sono interessati).
- <strong>Impatto sulla garanzia</strong>: la documentazione ufficiale dichiara che dopo il fuse Knox non si ha più diritto alla garanzia.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Pensa due volte prima di agire

{class="mt-1"}
Il fuse Knox di Samsung è <strong>irreversibile</strong>: una volta innescato non si torna allo stato di fabbrica. Se vuoi solo usare funzioni che di solito richiedono il Root, ti conviene prima cercare alternative che non lo richiedano.
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>Avvertenza importante

{class="mt-1"}
Il flashing comporta rischi, procedi con cautela. Può causare:

{class="list-disc pl-6 mt-1 space-y-1"}
- Brick del telefono (impossibile avviarlo)
- Perdita della garanzia
- Perdita di dati
- Malfunzionamenti delle funzioni di pagamento

{class="mt-1"}
Prima del flashing fai un backup completo, leggi con attenzione il tutorial e verifica la corrispondenza di modello e versione.
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Risorse consigliate

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>XDA Developers</strong>: la più grande community di sviluppatori Android al mondo, con tutorial di flashing e risorse ROM.
- <strong>Coolapk</strong>: nota community digitale cinese, con molti tutorial e discussioni in cinese.
- <strong>Forum dei vari modelli</strong>: come community Xiaomi, OnePlus, con guide ufficiali e non.
:::

#### 6. FAQ (Domande e risposte)

::: div .qa-item .mt-3
{class="font-semibold mb-1"}
<i class="fas fa-question-circle text-primary mr-1"></i>Q1: si può tornare indietro dopo lo sblocco del BL?

{class="mb-2 pl-6"}
<strong>A:</strong> è possibile ribloccare. In genere serve flashare il pacchetto ufficiale completo di flashing cablato e usare uno script di flashing specifico (come <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">flash_all_lock.bat</code> di Xiaomi). Attenzione: dopo il riblocco, alcuni fuse di sicurezza innescati dallo sblocco (come Knox di Samsung) potrebbero non essere reversibili.
:::

::: div .qa-item .mt-3
{class="font-semibold mb-1"}
<i class="fas fa-question-circle text-primary mr-1"></i>Q2: come si fa il Root dopo lo sblocco?

{class="mb-2 pl-6"}
<strong>A:</strong> lo sblocco del BL è solo il primo passo. Il Root di solito richiede:

{class="list-decimal pl-12 mb-2 space-y-1"}
1. Flashare una Recovery personalizzata (come TWRP).
2. Tramite Recovery, flashare un gestore Root come Magisk per patchare l'immagine di boot e ottenere i permessi di Root.
:::
