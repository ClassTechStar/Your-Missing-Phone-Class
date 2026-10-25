---
id: di-shi-liu-zhang
num: 16
part: jin-jie-pian
nav: Capitolo 16: Account e servizi cloud
toc: default
kind: chapter
---

### Capitolo 16: Sistema di account e servizi cloud

{class="chapter-intro mb-4"}
Un mio amico lo scorso anno ha avuto il telefono rubato. Il suo primo pensiero non è stato "quanto costa il telefono", ma "potrò recuperare le foto che ho dentro?". Purtroppo non aveva attivato il backup sul cloud. Il telefono è un bene esteriore, ma i dati nell'account, una volta persi, non tornano più. In questo capitolo parliamo di come stipulare una vera assicurazione per la tua vita digitale.

#### 1. Cosa gestisce davvero il tuo account telefonico?

Molti pensano che l'account serva solo a scaricare App. In realtà, un account telefonico è collegato a molte più cose di quanto immagini:

- <strong>Rubrica</strong>: numeri di telefono che conservi da anni o decenni.
- <strong>Foto e video</strong>: dalla nascita del figlio al diploma, dal primo appuntamento al viaggio di nozze.
- <strong>Note</strong>: appunti di ispirazione, diari, password degli account (sì, molti annotano le password nelle Note).
- <strong>Cronologia acquisti App</strong>: App a pagamento e acquisti in-app fatti per centinaia di yuan.
- <strong>Trova il mio telefono</strong>: se il telefono viene perso, è l'unico strumento che ti aiuta a localizzarlo, bloccarlo e cancellare i dati da remoto.

Se usi un telefono Apple, tutto quanto sopra è legato al tuo Apple ID. Se usi Android, è legato all'account Huawei/Xiaomi/OPPO/vivo e al tuo account Google. Questi account sono il "certificato di famiglia" della tua vita digitale: se lo perdi, molte cose diventano difficili da ricostruire.

#### 2. Tre cose da fare subito, adesso

1. <strong>Attiva la verifica in due fattori</strong>: che tu usi Apple o Android, la prima cosa da fare è andare nelle impostazioni dell'account e attivare la "verifica in due fattori" o "verifica in due passaggi". È come aggiungere un catenaccio alla porta: non basta la password, serve anche un codice inviato al tuo telefono. Anche se qualcuno su Internet indovina la tua password, senza il tuo telefono non entra.
2. <strong>Associa un metodo di recupero affidabile</strong>: la 2FA è sicura, ma c'è un rischio: cosa fai se perdi proprio il tuo telefono? Per questo il sistema ti chiederà di impostare una "chiave di recupero" o "email/telefono di backup". È l'unica via per riottenere l'account in caso di emergenza: meglio scriverla su carta, non tenerla nel telefono.
3. <strong>Verifica che "Trova il mio telefono" sia attivo</strong>: questa funzione, in caso di smarrimento, ti aiuta a localizzare, bloccare, far suonare e persino cancellare da remoto tutti i dati. È l'ultima linea di difesa. Molti la saltano all'acquisto del telefono e poi, quando serve, scoprono di non averla attivata: troppo tardi.

#### 3. iCloud: l'"aria" per gli utenti Apple

Chi usa un telefono Apple prima o poi si trova davanti a un dilemma: e se lo spazio iCloud è pieno?

Apple offre gratuitamente 5 GB, che a dire il vero non bastano neanche per un backup. Così la maggior parte delle persone prima o poi riceve il fastidioso popup "Spazio di archiviazione iCloud pieno". A quel punto hai tre opzioni:

- <strong>Pulisci</strong>: vai in Impostazioni → [il tuo nome] → iCloud → Gestisci spazio di archiviazione, guarda chi sta occupando spazio. Di solito foto e backup sono i più pesanti. Puoi iniziare cancellando i vecchi backup non necessari.
- <strong>Upgrade</strong>: 50 GB costano 6 yuan al mese, 200 GB 21 yuan. Personalmente ritengo che 50 GB bastino alla maggior parte delle persone, soprattutto per backup e miniature delle foto.
- <strong>Soluzione indiretta</strong>: se non vuoi pagare, puoi esportare periodicamente le foto sul computer e poi disattivare la sincronizzazione Foto iCloud. Ma in questo modo perdi la comodità del backup automatico delle foto.

Un avvertimento importante: la libreria foto di iCloud non è un "disco di rete", ma una "sincronizzazione". Se elimini una foto dal telefono, viene eliminata anche da iCloud. Se quello che vuoi è "fare il backup sul cloud e poi svuotare il telefono", la libreria foto di iCloud non fa per te: ti serve iCloud Backup o un disco di rete di terze parti.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-crown mr-2"></i>iCloud+: il tris di privacy riservato agli utenti a pagamento

{class="mt-1"}
Basta passare a qualsiasi livello a pagamento di iCloud (50 GB/200 GB/2 TB ecc.) per diventare automaticamente utenti <strong>iCloud+</strong> e sbloccare tre funzioni di privacy:

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>Private Relay (inoltro privato)</strong>: il "VPN" di Apple. Il traffico Safari viene inoltrato dai server di Apple al sito web; nessuno (inclusa Apple) può vedere contemporaneamente chi sei e cosa visiti. Utile per proteggere la privacy su Wi-Fi pubblico. Percorso: <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Impostazioni &gt; [il tuo nome] &gt; iCloud &gt; Inoltro privato</code>.
- <strong>Hide My Email (nascondi la mia email)</strong>: genera un indirizzo email casuale monouso quando ti registri su siti/App; le email vengono inoltrate automaticamente al tuo indirizzo reale. Se non vuoi più ricevere email da quel sito, basta chiudere l'indirizzo casuale: l'email reale non viene esposta. Percorso: <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Impostazioni &gt; [il tuo nome] &gt; iCloud &gt; Nascondi la mia email</code>.
- <strong>Dominio email personalizzato</strong>: puoi usare il tuo dominio (ad esempio @tuocognome.com) per inviare e ricevere email iCloud, utile per il personal branding o per la gestione della posta di famiglia.

{class="mt-1"}
Nota: Private Relay non è disponibile in alcuni paesi/regioni; gli utenti in Cina potrebbero aver bisogno di soluzioni alternative.
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-shield-halved mr-2"></i>iCloud Advanced Data Protection (ADP) — la vera crittografia end-to-end

{class="mt-1"}
Alla fine del 2022 Apple ha lanciato <strong>iCloud Advanced Data Protection (ADP)</strong>, estendendo la crittografia end-to-end (E2EE) dai pochi dati di salute, password e simili alla <strong>maggior parte dei dati iCloud</strong>: foto, note, backup iCloud, informazioni sui dispositivi, per un totale di 23 categorie.

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>Cos'è l'E2EE</strong>: la chiave di crittografia si trova solo sul tuo dispositivo, non sui server Apple. Anche se Apple venisse hackerata o le autorità richiedessero i dati, Apple non potrebbe consegnare dati decifrabili.
- <strong>Percorso di attivazione</strong>: <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Impostazioni &gt; [il tuo nome] &gt; iCloud &gt; Protezione avanzata dei dati</code>; segui le istruzioni per impostare i contatti di recupero/la chiave di recupero (<strong>obbligatorio</strong>: senza chiave non potrai recuperare i dati).
- <strong>Avvertenze</strong>: ① una volta attivato, conserva con cura la chiave di recupero, altrimenti in caso di perdita dell'account non potrai recuperare i dati; ② gli album condivisi, la libreria condivisa iCloud e poche altre funzioni non partecipano all'E2EE; ③ l'Apple ID per la Cina continentale non supporta ancora ADP, occorre passare a un account di un'altra regione.

{class="mt-1"}
In sintesi: se il tuo account contiene dati privati importanti e la regione lo supporta, consiglio vivamente di attivare ADP: è la protezione cloud più forte accessibile a un utente comune.
:::

#### 4. Sincronizzazione e backup, non confonderli

Queste due parole sembrano simili, ma le conseguenze sono molto diverse:

- <strong>La sincronizzazione</strong> è bidirezionale: se elimini qualcosa sul telefono, viene eliminata anche sul cloud; se elimini sul cloud, viene eliminata anche sul telefono. Le foto iCloud, la rubrica e le note sono sincronizzate. Il vantaggio è che più dispositivi restano coerenti; lo svantaggio è che "una volta eliminato, è davvero andato".
- <strong>Il backup</strong> è monodirezionale: il telefono fa una "fotografia" dello stato attuale e la salva sul cloud. Se in seguito elimini qualcosa sul telefono, la copia nel backup cloud resta. iCloud Backup e il backup locale su computer sono backup. Il vantaggio è una maggiore sicurezza dei dati; lo svantaggio è l'occupazione di spazio e l'assenza di aggiornamenti in tempo reale.

#### 5. La matrice di account per gli utenti Android

Sul lato Android la situazione è un po' più complessa che su Apple, perché i tuoi dati possono essere sparsi su più account:

- <strong>Account di brand</strong> (Huawei/Xiaomi/OPPO/vivo): gestisce il tuo spazio cloud, Trova il mio telefono, App store e wallet. Ogni brand ha il proprio servizio cloud, di solito con un modello base gratuito + espansioni a pagamento.
- <strong>Account Google</strong>: se usi Gmail, Google Foto, Google Contatti, questi dati si trovano nell'account Google. Google offre 15 GB gratuiti, è più generoso di Apple, ma sono condivisi con Gmail e Drive.
- <strong>WeChat/QQ</strong>: sono indipendenti dal sistema telefonico. La cronologia chat e i preferiti di WeChat non sono né nell'account di brand né in quello Google, ma solo sui server di WeChat.

Pertanto, quando un utente Android fa il backup, deve verificare separatamente: backup cloud di brand, backup Google, backup della cronologia chat di WeChat. Tutti e tre sono indispensabili.

#### 6. Condivisione in famiglia: avvantaggia anche i tuoi cari

La "Condivisione con la famiglia" di Apple permette di condividere con i familiari acquisti di App, musica, film e spazio iCloud, e di condividere la posizione. Si possono aggiungere fino a 6 persone. Si attiva in: Impostazioni → [il tuo nome] → Condivisione con la famiglia. Anche Huawei e Xiaomi hanno funzioni simili, rintracciabili nelle impostazioni dell'account come "Condivisione in famiglia" o "Cloud di famiglia".

Uno scenario molto pratico: imposta la condivisione con la famiglia sul telefono dei genitori, così potrai vedere in qualsiasi momento la loro posizione (se loro acconsentono); se l'anziano si perde o non è raggiungibile al telefono, avrai un riferimento di posizione.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Le conseguenze del furto dell'account sono più gravi di quanto pensi

{class="mt-1"}
Se un hacker ottiene la password del tuo account, può: bloccare da remoto il tuo telefono e chiedere un riscatto, visionare le tue foto e la tua rubrica, fare acquisti con il tuo metodo di pagamento. Peggio ancora, se l'account è legato a troppe cose, recuperarlo è di per sé un incubo. Quindi: attiva subito la verifica in due fattori.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>In pratica: fai un check-up completo del tuo account

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Apri le Impostazioni del telefono, vai alla pagina dell'account e conferma che la verifica in due fattori sia attiva.
2. Verifica che "numeri di telefono affidabili" e "chiave di recupero" siano impostati; trascrivi la chiave su carta.
3. Accedi alla gestione di iCloud o dello spazio cloud, vedi quali dati sono sincronizzati e disattiva quelli non necessari.
4. Conferma che "Trova il mio telefono" sia attivo.
5. Se usi Android, controlla che backup cloud di brand, backup Google e backup di WeChat siano tutti coperti.
:::
