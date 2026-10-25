---
id: di-shi-ba-zhang
num: 18
part: jin-jie-pian
nav: Capitolo 18: Backup e migrazione dei dati
toc: default
kind: chapter
---

### Capitolo 18: Backup e migrazione dei dati

{class="chapter-intro mb-4"}
Una vicina aveva fatto cadere il telefono in una vasca d'acqua e, tiratolo fuori, non si accendeva più. Quello che le dispiaceva di più non era il telefono in sé, ma le foto non backuppate di tre anni: tutti i ricordi del bambino dalla nascita ai primi passi. Sentendola mi sono sentito male, perché si tratta di una cosa completamente evitabile. In questo capitolo mettiamo seriamente una polizza sui nostri dati.

#### 1. Prima chiarisci: cosa c'è nel tuo telefono che, se perso, non c'è più

Lo "stato di sopravvivenza" dei diversi dati è diverso, devi distinguerli:

- <strong>Salvati localmente sul telefono, se li perdi sono davvero andati</strong>: foto e video (se non hai attivato la sincronia cloud), note, SMS, registro chiamate, file scaricati.
- <strong>Salvati sui server delle app, basta riloggarsi nel telefono nuovo</strong>: lista contatti di WeChat, ordini su Taobao, transazioni nell'app della banca. Questi dati risiedono sui server delle aziende, non sul tuo telefono.
- <strong>In zona grigia, richiedono operazioni specifiche</strong>: cronologia chat di WeChat (anche se il server di WeChat la conserva, tu non puoi scaricarla dal server), credenziali di dispositivi associate all'app della banca, chiavi nelle app di verifica in due passaggi (tipo Google Authenticator).

Quello che devi proteggere con maggiore attenzione sono la prima e la terza categoria.

#### 2. Backup integro del telefono: risolvi tutto in una volta

Il backup integro è come scattare un'istantanea completa del telefono: impostazioni di sistema, layout del desktop, dati delle app, foto, contatti, tutto inscatolato.

##### Opzione 1: backup locale su computer (il più affidabile, consigliato a chi ha un computer)

- <strong>iPhone</strong>: collega il telefono al computer con un cavo dati, apri iTunes (vecchia versione Windows) o Finder (Mac), nella pagina del dispositivo seleziona "Esegui backup ora". Attenzione: spunta "Cifra backup", altrimenti le password e i dati sanitari non verranno inclusi.
- <strong>Android</strong>: ogni marchio ha il proprio software per computer, ad esempio HiSuite di Huawei, Mi Assistant, Samsung Smart Switch. Collega al computer e segui le istruzioni.
- Il vantaggio del backup su computer è che non devi pagare spazio cloud e il ripristino è molto più veloce del ripristino dal cloud. Lo svantaggio è che devi ricordarti di collegare il cavo e fare il backup periodicamente: la maggior parte delle persone non ci riesce.

##### Opzione 2: backup sul cloud (il più comodo, consigliato a tutti)

- <strong>iPhone</strong>: Impostazioni → [il tuo nome] → iCloud → Backup su iCloud → attiva. Il telefono esegue il backup automatico quando è in carica, connesso al Wi-Fi e bloccato. I 5 GB gratuiti probabilmente non bastano, conviene spendere 6 yuan per passare a 50 GB.
- <strong>Android</strong>: i cloud dei vari marchi hanno funzioni di backup. Su Huawei cerca "backup cloud" nelle impostazioni, su Xiaomi vai in "Xiaomi Cloud Services", OPPO/vivo analogamente. C'è anche il backup integrato di Google (Impostazioni → Sistema → Backup): attiva anche quello.
- Il grande vantaggio del backup cloud è che "non devi pensarci", è tutto automatico. Il grande svantaggio è che il ripristino richiede un download lungo e lo spazio gratuito di solito non basta.

#### 3. Strategia di backup per categorie: le cose importanti vanno salvate a parte

Il backup integro è la rete di sicurezza, ma alcune cose sono così importanti da meritare una copia a parte:

##### Foto e video (l'asset digitale più prezioso)

- <strong>Piano a doppia protezione</strong>: attiva la sincronia automatica su iCloud Foto/Google Foto e, ogni pochi mesi, copia manualmente le foto su computer o disco esterno. Così una copia è sul cloud e una in locale, reciprocamente backup.
- <strong>Piano gratuito</strong>: Google Foto offre 15 GB gratuiti, puoi impostare "qualità compressa" per risparmiare spazio. Oppure ogni mese collega il telefono con il cavo e copia tutte le foto sul computer.

##### Contatti (facili da trascurare ma importantissimi)

- I contatti dell'iPhone sono sincronizzati di default con iCloud: se hai attivato la sincronia non serve un backup aggiuntivo. Se vuoi maggiore sicurezza, puoi esportare un file vCard da iCloud.com e salvarlo sul computer.
- I contatti Android di solito si sincronizzano con Google o con il cloud di marca. Vai nelle impostazioni dell'app Contatti ed esporta un file .vcf: avrai un backup completo.

##### Cronologia chat di WeChat (da gestire a parte, massima priorità)

Va trattata a parte perché nel backup integro spesso non è completa e gli strumenti di migrazione non riescono a spostarla.

- <strong>Metodo 1: migrazione al telefono nuovo</strong>. WeChat → Io → Impostazioni → Generale → Migrazione e backup cronologia chat → Migra → Migra a telefono/tablet. Il telefono vecchio e quello nuovo vanno collegati alla stessa rete Wi-Fi; scansiona il codice per trasferire. Attenzione: prima che la migrazione sia completa, non uscire da WeChat sul telefono vecchio.
- <strong>Metodo 2: backup su computer</strong>. Installa WeChat per PC, in basso a sinistra le tre linee → Migrazione e backup → Backup e ripristino → Esegui backup della cronologia chat sul computer. Quando cambi telefono potrai ripristinarla sul telefono nuovo.
- <strong>Metodo 3: backup sul cloud</strong>. WeChat supporta anche il backup su iCloud o sul cloud di marca, ma attenzione: questo backup può essere ripristinato solo sul telefono attuale, non è ripristinabile su un altro dispositivo. Per cambiare telefono, devi usare uno dei due metodi precedenti.

#### 4. Guida al cambio telefono: dal vecchio al nuovo

Cambiare telefono è una gioia, ma se i dati non passano diventa un mal di testa. Tre situazioni, tre strategie:

##### Stesso marchio (il più semplice)

- <strong>iPhone → nuovo iPhone</strong>: all'accensione, in fase di attivazione, metti il vecchio telefono vicino: apparirà "Avvio rapido". Scansiona il disegno sul telefono nuovo con quello vecchio e il gioco è fatto. Tutti i dati, le impostazioni, il layout delle app passano intatti, comprese le password del Wi-Fi. Occorrono circa venti-trenta minuti.
- <strong>Android stesso marchio</strong>: usa lo strumento di migrazione del marchio. Huawei usa "Clonazione telefono", Xiaomi "Xiaomi Switch", OPPO "Trasloco telefono", vivo "Mutuo trasferimento". I passaggi sono simili: installa la stessa app sui due telefoni, scansiona il codice per il collegamento, seleziona cosa trasferire, avvia.

##### Cambio marchio (Android verso Android, marchi diversi)

Usa strumenti di migrazione di terze parti oppure l'app di migrazione del marchio di partenza (la maggior parte delle app di migrazione dei marchi supporta anche il passaggio ad altri Android). Si possono trasferire: contatti, foto, SMS, registro chiamate, alcune app. Non si possono trasferire: gli stati di login dentro le app (devi rifare il login), la cronologia chat di WeChat (usa la funzione di migrazione di WeChat).

##### Cambio piattaforma (Android verso iPhone o viceversa)

- <strong>Android → iPhone</strong>: Apple ha un'app "Passa a iOS"; scaricatala sull'Android, in fase di attivazione del nuovo iPhone scegli "Trasferisci dati da dispositivo Android". Trasferisce i dati di base come contatti, foto, SMS, ma non i dati delle app. La cronologia chat di WeChat va migrata con la funzione di WeChat.
- <strong>iPhone → Android</strong>: ogni marchio Android ha il proprio strumento di migrazione, ma a dire il vero l'esperienza cross-piattaforma non è buona come sulla stessa piattaforma. Fai prima le cose più importanti: esporta i contatti, fai il backup delle foto, migra la cronologia WeChat. Il resto viene col tempo.

#### 5. La regola d'oro del backup: principio 3-2-1

È un principio classico della sicurezza dei dati, facile da ricordare:

- <strong>3</strong>: conserva almeno tre copie dei dati importanti (l'originale e due backup).
- <strong>2</strong>: usa due supporti di memorizzazione diversi (ad esempio una copia sul cloud e una su disco esterno).
- <strong>1</strong>: almeno una copia di backup in una posizione fisica diversa (per evitare che incendio o furto distruggano contemporaneamente tutti i dati).

Per le persone comuni, fare "una copia sul cloud e una sul computer" è già molto bene. Non serve complicarsi la vita, l'importante è davvero farlo.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Attenzione particolare alla cronologia chat di WeChat

{class="mt-1"}
La cronologia chat di WeChat non può essere migrata con alcuno strumento di migrazione telefonica! Non rientra nella copertura del backup integro. Devi usare la funzione "Migrazione cronologia chat" integrata in WeChat oppure backuppare su WeChat per computer. Molti si accorgono solo dopo aver cambiato telefono che la cronologia è sparita: a quel punto è tardi, perché il telefono vecchio magari è già stato ripristinato alle impostazioni di fabbrica.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Allenati: fai una prova completa di backup

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Verifica che il backup su iCloud o sul cloud di marca sia attivo e controlla la data dell'ultimo backup.
2. Fai il backup manuale delle foto: collega il telefono al computer con il cavo e copia le cartelle DCIM e Pictures sul computer.
3. Fai il backup dei contatti: gli utenti iPhone esportano un vCard da iCloud.com; gli utenti Android esportano un file .vcf dalle impostazioni dell'app Contatti.
4. Fai il backup della cronologia chat di WeChat: apri WeChat → Io → Impostazioni → Generale → Migrazione e backup cronologia chat → Backup su computer.
5. Copia il file vcf dei contatti e la cartella delle foto su un disco esterno o una chiavetta USB, completando il "3-2-1" con "una copia offline altrove".
:::
