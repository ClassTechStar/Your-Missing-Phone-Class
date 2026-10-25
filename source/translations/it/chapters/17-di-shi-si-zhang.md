---
id: di-shi-si-zhang
num: 14
part: ruan-jian-pian
nav: Capitolo 14: Focus sui gestori di password
toc: default
kind: chapter
---

### Capitolo 14: Gestione delle password

{class="chapter-intro mb-4"}
Nell'era digitale, la password è la chiave di casa. Ma se le chiavi sono troppe e troppo complesse, cosa fare? Il gestore di password è il tuo "maggiordomo universale delle chiavi".

#### 1. Perché serve un gestore di password?

Oggi una persona ha in media decine o centinaia di account online. Se si usa la stessa password per tutti, quando un sito viene violato tutti gli account sono a rischio. Se invece si usano password complesse diverse per ogni account, è impossibile ricordarle tutte.

Il gestore di password risolve questo dilemma: basta ricordare una sola password principale e lui ricorderà tutte le altre al posto tuo.

#### 2. Come funziona un gestore di password

1. <strong>Archiviazione cifrata</strong>: tutte le password sono memorizzate con crittografia ad alta intensità; solo tu puoi decifrarle.
2. <strong>Password principale</strong>: imposti una password principale per sbloccare la cassaforte delle password. La password principale non è archiviata sul server.
3. <strong>Compilazione automatica</strong>: nelle pagine di login di siti o App, il gestore compila automaticamente username e password.
4. <strong>Generazione di password</strong>: può generare password casuali e complesse per aumentare la sicurezza.

#### 3. Cenni sui principi di crittografia

Capire i principi di crittografia del gestore di password aiuta a giudicare se un provider sia affidabile. Di seguito una spiegazione, in linguaggio accessibile, dei concetti chiave.

##### 1. Crittografia AES-256

AES (Advanced Encryption Standard) è uno standard di crittografia simmetrica riconosciuto dal NIST (National Institute of Standards and Technology) ed è ampiamente usato da banche, esercito e governi. "256" indica una chiave di 256 bit: per forzarla bruta occorrerebbe, in teoria, un tempo superiore all'età dell'universo. I principali gestori di password (1Password, Bitwarden, KeePass ecc.) usano AES-256 per cifrare la tua cassaforte.

##### 2. Architettura Zero-Knowledge

"Zero-Knowledge" non significa che il provider non archivi nulla, ma che <strong>crittografia e decrittografia avvengono localmente sul tuo dispositivo, e il server conserva solo il testo cifrato</strong>. Il flusso:

1. Inserisci la password principale nel client.
2. Il client deriva da essa una chiave di crittografia (questo passaggio avviene sul tuo telefono/computer).
3. Solo il testo cifrato viene caricato sul server.
4. Al login successivo, il server scarica il testo cifrato e il client lo decifra di nuovo con la password principale.

Punto chiave: <strong>la password principale non lascia mai il tuo dispositivo</strong> e non è presente sul server. Anche se il provider venisse violato, l'hacker otterrebbe solo un mucchio di testo cifrato indecifrabile, a meno che non riesca a indovinare la tua password principale.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Perché "Zero-Knowledge" significa che nemmeno il provider vede le tue password?

{class="mt-1"}
Perché la chiave di decrittazione è derivata dalla tua password principale, che esiste solo nella tua testa ed è usata solo sul tuo dispositivo locale. Sul server del provider non c'è né la password principale né la chiave di decrittazione, ma solo il testo cifrato. Ecco perché provider seri come Bitwarden e 1Password dichiarano esplicitamente "non possiamo vedere le tue password nemmeno noi": non è che non vogliano, è che tecnicamente non possono.
:::

##### 3. Funzioni di derivazione delle chiavi: PBKDF2 e Argon2

La password principale non può essere usata direttamente come chiave di crittografia: deve essere elaborata da una "funzione di derivazione delle chiavi". Il ruolo di questa funzione è <strong>rendere intenzionalmente lento il calcolo</strong>, portando il costo di un attacco brute-force a livelli irrealizzabili.

- <strong>PBKDF2</strong>: standard storico, usato da iCloud Keychain, Bitwarden, LastPass e altri. Rallenta il cracking tramite iterazione ripetuta (in genere oltre 100.000 volte) dell'hash.
- <strong>Argon2</strong>: vincitore del Password Hashing Competition 2015, più moderno di PBKDF2. Oltre al "consumo di calcolo" introduce un "consumo di memoria", rendendo difficile l'accelerazione anche con hardware dedicato come GPU/ASIC. Già supportato da Bitwarden, KeePassXC e altri.

Più alto è il numero di iterazioni, maggiore è la sicurezza, ma più lento lo sblocco. I provider seri pubblicano l'algoritmo di derivazione usato e il numero di iterazioni, per consentire l'audit da parte della comunità di sicurezza.

##### 4. Caso di studio: violazione dei dati di LastPass nel 2022

Nell'agosto 2022 lo storico gestore LastPass ha annunciato la violazione del proprio ambiente di sviluppo; a novembre ha rivelato che gli aggressori avevano preso i backup delle casseforti degli utenti (testo cifrato). Le lezioni chiave dell'evento:

- <strong>L'architettura Zero-Knowledge ha tenuto la linea</strong>: poiché la cassaforte è cifrata, l'hacker ha ottenuto testo cifrato ma non riesce a decifrarlo, a condizione che la password principale dell'utente sia sufficientemente forte.
- <strong>Gli utenti con password principale debole sono i più a rischio</strong>: l'hacker può tentare un brute-force offline della password principale debole, quindi chi usa password deboli o riutilizzate è di fronte a un rischio concreto.
- <strong>Anche i metadati sono trapelati</strong>: sebbene il contenuto delle password sia cifrato, metadati come gli URL dei siti e le note potrebbero non esserlo, esponendo quali servizi l'utente utilizza.

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Cosa imparare dal caso LastPass

{class="mt-1"}
Primo: la password principale deve essere lunga e unica (consigliato almeno 16 caratteri, con maiuscole, minuscole, numeri e simboli). Secondo: preferire provider che supportino Argon2id con un alto numero di iterazioni. Terzo: per gli account ad alto valore (banca, email) attiva sempre una seconda verifica indipendente, senza affidarti solo al gestore di password.
:::

#### 4. Principali gestori di password consigliati

##### Di sistema:

- <strong>iCloud Keychain</strong>: la prima scelta per gli utenti dell'ecosistema Apple. Integrata senza soluzione di continuità con Safari e le App, gratuita, sicura. Lo svantaggio è che è poco comoda da usare su altre piattaforme.
- <strong>Gestore password Google</strong>: comoda per gli utenti Android. Integrata con Chrome e Android, gratuita.
- <strong>Cassaforte password Huawei</strong>: integrata in HarmonyOS, adatta agli utenti Huawei.

##### Strumenti professionali di terze parti:

- <strong>Bitwarden</strong>: open source e gratuito, potente, supporta tutte le piattaforme. Fortemente consigliato per gli utenti attenti alla privacy.
- <strong>1Password</strong>: interfaccia curata, funzioni ricche, adatto a famiglie e team. A pagamento.
- <strong>LastPass</strong>: gestore storico, la versione gratuita ha funzioni limitate.
- <strong>KeePass</strong>: archiviazione totalmente locale, open source e gratuito. Adatto agli utenti geek.

#### 5. Valutazione reale della forza di una password

I gestori di password mostrano in genere un indicatore di "forza" (rosso/giallo/verde), ma questa valutazione spesso si basa solo su lunghezza e varietà di caratteri, e non è completa. Per giudicare davvero se una password sia sicura occorre considerare l'"entropia" e "se è già trapelata".

##### 1. Entropia: la misura scientifica della forza di una password

L'"entropia" misura l'incertezza di una password, in bit. Più alta è l'entropia, maggiore è il numero di tentativi necessari per un brute-force.

- <strong>"123456"</strong>: entropia bassissima, cracking istantaneo.
- <strong>"P@ssw0rd"</strong>: sembra complessa, ma è presente in tutte le liste di dictionary attack, quindi l'entropia resta bassa.
- <strong>"correct horse battery staple"</strong>: quattro parole casuali, entropia di circa 44 bit, difficoltà di cracking di gran lunga superiore a "P@ssw0rd".
- <strong>16 caratteri casuali (con maiuscole + minuscole + numeri + simboli)</strong>: entropia di circa 100 bit, con la potenza di calcolo attuale impossibile da forzare.

Conclusione: <strong>"lunghezza + casualità" contano più di "simboli complessi"</strong>. Questo è il motivo per cui le password lunghe e casuali generate dal gestore sono davvero sicure.

##### 2. HaveIBeenPwned: verifica se la tua password è già trapelata

Il sito <a href="https://haveibeenpwned.com" class="text-primary hover:underline" target="_blank" rel="noopener">haveibeenpwned.com</a>, gestito dal ricercatore di sicurezza Troy Hunt, raccoglie gli account e le password trapelati nelle principali violazioni di dati. Puoi:

1. Inserire l'email per verificare se il tuo account è stato esposto in una violazione.
2. Usare la funzione Pwned Passwords per verificare se una password è nei database noti di fughe di dati (i gestori di password e i browser hanno già integrato questa query).

Se una password è presente nel database delle fughe, <strong>per quanto complessa possa sembrare, va sostituita immediatamente</strong>: gli attacchi a dizionario proveranno per primi queste password note.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-shield-alt mr-2"></i>Principio di query k-Anonymity

{class="mt-1"}
Temi che inserire la password in HaveIBeenPwned provochi un'altra fuga? Non preoccuparti. Le query moderne usano il protocollo "k-Anonimity": il browser invia al server solo i primi 5 caratteri dell'hash della password, il server restituisce l'elenco di tutti gli hash che iniziano con quei 5 caratteri e il confronto avviene in locale. In altre parole, il server non vede mai l'hash completo della tua password. Il "controllo password trapelate" di 1Password e Bitwarden funziona così.
:::

##### 3. Funzioni di monitoraggio integrate nel gestore di password

- <strong>1Password Watchtower</strong>: monitora in tempo reale password deboli, duplicate, trapelate, scadute e siti senza 2FA, con classificazione rosso/arancio/giallo.
- <strong>Bitwarden Vault Health</strong>: la versione gratuita mostra password deboli e duplicate; la versione a pagamento rileva le password trapelate (basata su HaveIBeenPwned).
- <strong>"Suggerimenti di sicurezza" di iCloud Keychain</strong>: in iOS Impostazioni → Password → Suggerimenti di sicurezza, segnala quali password sono presenti in fughe note e quali sono riusate.
- <strong>"Controllo password" di Gestore password Google</strong>: integrato in Chrome, con un clic verifica password trapelate, deboli e duplicate.

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Verifica ora: la tua password è sicura?

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Apri haveibeenpwned.com, inserisci la tua email abituale e guarda in quali violazioni è presente.
2. Utenti iPhone: Impostazioni → Password → Suggerimenti di sicurezza, gestisci uno per uno gli avvisi rossi.
3. Utenti Chrome: Impostazioni → Password → Verifica password, modifica secondo le indicazioni.
4. Utenti 1Password/Bitwarden: apri Watchtower/Health Reports e dai priorità alle voci "trapelate" e "duplicate".
:::

#### 6. Passkey: il futuro del login senza password

Tra il 2024 e il 2026 la tecnologia delle password sta vivendo una rivoluzione: i <strong>Passkey (chiavi di accesso)</strong> potrebbero eliminare del tutto le password tradizionali. Spinti congiuntamente da Apple, Google e Microsoft, con il supporto della FIDO Alliance e del W3C, è il più grande cambiamento nel modo di accedere degli ultimi decenni.

##### 1. Cos'è un Passkey?

Il Passkey si basa sullo standard FIDO2 / WebAuthn e sostituisce la password con una <strong>coppia di chiavi sul dispositivo</strong>. Il principio si può semplificare così:

- Il tuo telefono genera una coppia di chiavi: <strong>chiave pubblica</strong> (registrata presso il sito) + <strong>chiave privata</strong> (sempre nel chip di sicurezza del tuo dispositivo).
- Al login, il sito invia una "sfida"; il tuo telefono la firma con la chiave privata e il sito la verifica con la chiave pubblica.
- Prima della firma devi confermare l'identità con biometria (Face ID / impronta) o PIN del dispositivo.
- In tutto il processo, <strong>nessuna password viaggia nella rete</strong>.

##### 2. Passkey vs password tradizionali

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dimensione</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Password tradizionale</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Passkey</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Resistenza al phishing</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">bassa, i siti di phishing possono rubare la password</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">naturalmente anti-phishing, la chiave privata firma solo il dominio reale</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Effetto di una violazione del server</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">l'hash della password può essere cracked</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">il server conserva solo la chiave pubblica, la violazione non ha impatto</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Comodità</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">da ricordare/inserire/gestire</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">login in un secondo con Face ID/impronta</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Attacchi di replay</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">possono essere intercettati e replicati da un man-in-the-middle</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ogni firma è monouso, non può essere replicata</td>
                            </tr>
                        </tbody>
                    </table>
```

##### 3. Supporto delle piattaforme

- <strong>Apple iCloud Keychain Passkey</strong>: supporto nativo in iOS 16+ / macOS Ventura+, i Passkey si sincronizzano tra tutti i dispositivi con lo stesso Apple ID; sui nuovi dispositivi non è necessario ricrearli per accedere ai siti.
- <strong>Gestore password Google Passkey</strong>: supporto nativo in Android + Chrome, i Passkey sono archiviati nell'account Google e sincronizzati tra dispositivi Android; dal 2023 l'account Google personale supporta il login con Passkey.
- <strong>Microsoft</strong>: Windows 11 / Edge supporta i Passkey; account Microsoft, Outlook, Office e altri servizi stanno aprendo al login con Passkey, gestibile in Microsoft Authenticator.
- <strong>1Password / Bitwarden</strong>: supportano creazione, archiviazione e sincronizzazione multipiattaforma dei Passkey, così non sei vincolato a un unico ecosistema.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>La sincronizzazione tra dispositivi è il breakthrough chiave

{class="mt-1"}
Il maggiore limite iniziale dei Passkey era il "vincolo a un singolo dispositivo": cambiando telefono bisognava ricrearli. Dal 2023 Apple, Google e Microsoft hanno realizzato la sincronizzazione cloud dei Passkey: iCloud Keychain sincronizza tra dispositivi Apple, il Gestore password Google sincronizza tra dispositivi Android. 1Password e altri terzi hanno reso possibile la sincronizzazione tra ecosistemi. Questo significa che i Passkey hanno ormai la maturità pratica per sostituire le password.
:::

##### 4. Come creare e usare i Passkey sul telefono

<strong>Percorso iOS (iPhone):</strong>

1. Nella pagina di sicurezza dell'account di un sito che supporta i Passkey (es. Google, Microsoft, Amazon, eBay, PayPal) seleziona "Aggiungi passkey".
2. Comparirà la finestra di verifica Face ID / Touch ID; dopo la conferma il Passkey viene generato e salvato automaticamente in iCloud Keychain.
3. Al login successivo, inserito lo username scegli "Usa iPhone per accedere": basta un Face ID.
4. Gestione: Impostazioni → Password → trova il sito per vedere la voce Passkey.

<strong>Percorso Android:</strong>

1. Nella pagina di sicurezza dell'account del sito che supporta i Passkey seleziona "Aggiungi passkey".
2. Popup del Gestore password Google → seleziona il tuo account Google → verifica del blocco schermo (impronta/disegno/PIN).
3. Il Passkey viene salvato nel Gestore password Google e sincronizzato tra dispositivi Android con lo stesso account.
4. Al login successivo, scegli "Usa passkey": basta sbloccare lo schermo.
5. Gestione: Impostazioni Android → Password, passkey e compilazione automatica → Gestore password → google.com.

##### 5. Login Passkey tra dispositivi

Se su un PC Windows vuoi accedere a un sito che ha il Passkey solo sull'iPhone, puoi autorizzare tramite scansione del QR:

1. Nella pagina di login del sito scegli "Usa passkey".
2. Seleziona "Usa un altro dispositivo".
3. Il PC mostra un QR code: scansiona con l'iPhone.
4. L'iPhone propone la verifica Face ID; dopo la conferma il login sul PC è completato.

Il processo usa una doppia comunicazione cifrata via Bluetooth + Internet: la chiave privata del Passkey non lascia mai il tuo iPhone.

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Prova ora: scopri il login senza password

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Accedi all'account Google → Sicurezza → Passkey → Aggiungi passkey e prova il login con Face ID/impronta.
2. Accedi all'account Microsoft → Sicurezza → Opzioni di sicurezza avanzate → Aggiungi passkey.
3. Su Taobao, JD, eBay, PayPal e altri servizi che supportano i Passkey, provali.
4. Conserva la password tradizionale come backup e migra gradualmente gli account ad alto valore ai Passkey.
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Consigli per la fase di transizione

{class="mt-1"}
I Passkey non hanno ancora sostituito del tutto le password: molti siti sono in una fase di convivenza "Passkey + password". Consiglio: attiva prima i Passkey sugli account ad alto valore, ma <strong>non eliminare subito la password tradizionale</strong>, tienila come backup; continua a usare un gestore di password, perché non tutti i siti supportano i Passkey. Considera i Passkey come un "potente complemento" al gestore di password, non come una "sostituzione immediata".
:::

#### 7. Chiavi di sicurezza hardware

Se le tue esigenze di sicurezza sono superiori a quelle dell'utente medio (ad esempio detieni molte criptovalute, sei manager/giornalista/attivista o protegge account aziendali chiave), la chiave di sicurezza hardware è una scelta più affidabile del codice via SMS.

##### 1. Cos'è una chiave di sicurezza hardware?

Una chiave hardware è un dispositivo fisico (a forma di chiavetta USB) con un chip di sicurezza interno che custodisce la tua chiave privata; richiede contatto fisico o NFC per completare la verifica. Prodotti rappresentativi:

- <strong>YubiKey</strong> (Yubico): la più diffusa, supporta FIDO2/WebAuthn, U2F, OTP, PIV, OpenPGP, con interfacce USB-C / USB-A / NFC. Serie 5: 50-70 dollari.
- <strong>Google Titan</strong>: prodotta da Google, USB-C + NFC / Bluetooth, circa 30-40 dollari.
- <strong>OnlyKey</strong>: alternativa open source, supporta più protocolli.
- <strong>Alternative cinesi</strong>: come ePasskey di Feitian, più economiche.

##### 2. Perché una chiave hardware è più sicura del codice SMS?

- <strong>Anti-phishing</strong>: come i Passkey, la chiave hardware risponde solo al dominio reale, i siti di phishing non possono ingannarla.
- <strong>Resistente al SIM-swap</strong>: il codice SMS può essere intercettato con un attacco SIM-swap, la chiave hardware non richiede un numero di telefono.
- <strong>Anti man-in-the-middle</strong>: il protocollo FIDO2 include un challenge in ogni firma, non replicabile.
- <strong>Isolamento fisico</strong>: la chiave privata resta sempre nel chip hardware; anche se un malware compromette il tuo computer, non riesce a leggerla.

##### 3. Scenari d'uso

- Account di exchange di criptovalute, recupero di wallet.
- SSO aziendale, VPN per smart working, login SSH ai server.
- Email, GitHub, social media e altri "account principali": una volta compromessi, permettono il reset di tutti gli altri account.
- Giornalisti, avvocati, manager e altre persone ad alta sensibilità.

##### 4. Come configurare una chiave hardware come verifica a due fattori

Esempio con account Google + YubiKey:

1. Acquista una YubiKey (consigliato comprarne due: una per l'uso quotidiano e una di backup, conservate in luoghi diversi).
2. Accedi a myaccount.google.com → Sicurezza → Verifica in due passaggi.
3. Seleziona "Aggiungi chiave di sicurezza" → inserisci la YubiKey nella porta USB-C o avvicinala al sensore NFC del telefono.
4. Segui le indicazioni e tocca il contatto metallico della YubiKey per completare la registrazione.
5. Consiglio di registrare anche una seconda chiave di backup.
6. Nelle impostazioni della verifica in due passaggi, imposta la chiave hardware come metodo preferito e il codice SMS come backup.

Siti principali che la supportano: Google, GitHub, Microsoft, Apple ID, Facebook, Twitter, Dropbox, GitLab, AWS, Coinbase, Binance e altri.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Strategia a due chiavi

{class="mt-1"}
Il rischio maggiore di una chiave hardware è lo "smarrimento". Consiglio: ① registra contemporaneamente due chiavi diverse; ② una da portare con sé (portachiavi), una da conservare in cassaforte di casa o in una cassetta di sicurezza in banca; ③ alcuni siti consentono di stampare "codici di recupero" da conservare offline. Così, anche se la chiave principale viene persa, non resterai chiuso fuori per sempre dall'account.
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Attenzione al canale di acquisto

{class="mt-1"}
Acquista sempre nel negozio ufficiale o da rivenditori autorizzati; evita chiavi di seconda mano o di origine sconosciuta: in teoria un hardware preconfigurato potrebbe avere un backdoor. Il firmware di YubiKey non può essere aggiornato dopo la fabbricazione, ma Yubico pubblica continuamente avvisi di sicurezza: basta seguire il sito ufficiale.
:::

#### 8. Condivisione di password in famiglia/team

In ambito familiare, Netflix, WiFi di casa, backend del router e password della serratura smart devono essere condivisi da tutta la famiglia; in ambito di team, server, database e account dei social media richiedono la collaborazione di più persone. <strong>Inviare password su WeChat o scriverle in documenti condivisi sono pratiche ad alto rischio</strong>: se la cronologia chat o i permessi del documento vengono esposti, la password è esposta.

##### 1. "Cassaforte condivisa" (Vault) di 1Password

1Password è il prodotto di riferimento per la condivisione in famiglia e team. Il suo meccanismo centrale è <strong>più casseforti</strong>:

- <strong>Cassaforte personale</strong>: visibile solo a te, ad esempio conti bancari ed email privati.
- <strong>Cassaforte condivisa</strong>: visibile a tutti i membri della famiglia o del team, ad esempio Netflix, WiFi di casa, carta di credito condivisa.
- <strong>Permessi gerarchici</strong>: la versione team può impostare alcuni membri come "sola lettura" o "sola lettura senza modifica".

I membri della famiglia o del team non devono condividere la password principale: ciascuno accede con il proprio account ma può vedere il contenuto delle casseforti condivise autorizzate. Le modifiche alle password si sincronizzano in tempo reale per tutti i membri.

##### 2. Funzione "Organizzazione" di Bitwarden

La versione gratuita di Bitwarden supporta la condivisione di password tra singoli (tramite la funzione "Send", condivisione a tempo di una singola password); la versione a pagamento permette di creare "organizzazioni" e condividere diverse voci con i membri della famiglia o colleghi del team, con permessi granulari. Bitwarden offre anche l'opzione self-hosted, adatta alle aziende con forti esigenze di sovranità sui dati.

##### 3. Scenario familiare: come condividere in sicurezza password di Netflix, WiFi e altro

- <strong>Netflix / siti video</strong>: usa la "cassaforte condivisa" di 1Password Famiglia per archiviare la password di login; ciascun membro accede autonomamente, senza doverla inviare nel gruppo chat.
- <strong>Password WiFi di casa</strong>: tra dispositivi iOS la password WiFi può essere condivisa via AirDrop direttamente agli ospiti, senza doverla dettare; su Android 12+ è disponibile la funzione "Condivisione WiFi nelle vicinanze".
- <strong>Serrature smart ed elettrodomestici smart</strong>: cerca di usare la funzione "Membri famiglia" dell'App del produttore per creare account separati per ciascuno, invece di condividere un unico account amministratore.
- <strong>Backend del router di casa</strong>: la password amministratore va nella cassaforte condivisa di 1Password; per il WiFi degli ospiti attiva un SSID separato.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Rapporto qualità-prezzo di 1Password Famiglia

{class="mt-1"}
1Password Families costa circa 4,99 dollari al mese e supporta fino a 5 membri della famiglia; ciascuno ha una cassaforte personale + 4 casseforti condivise. A persona sono meno di 1 dollaro al mese: è la soluzione con la migliore esperienza di condivisione familiare oggi disponibile. La versione famiglia di Bitwarden a 10 dollari all'anno supporta 6 persone ed è più economica, ma l'interfaccia è leggermente inferiore.
:::

##### 4. Scenario team: condivisione di password di server/database

- <strong>1Password Teams / Business</strong>: permette di creare più casseforti per dipartimento o progetto, con controllo granulare dei permessi e auditing di tutti gli accessi.
- <strong>Bitwarden Teams / Enterprise</strong>: soluzione open source, self-hostable, la versione enterprise supporta l'integrazione SSO e la sincronizzazione con la directory.
- <strong>Principio di separazione dei ruoli</strong>: le password amministrative non dovrebbero essere in mano a una sola persona: designare 2-3 "contatti di emergenza" per evitare interruzioni in caso di partenza/ferie del personale chiave.
- <strong>Procedura di uscita</strong>: quando un dipendente se ne va, revoca immediatamente il suo accesso al gestore di password e, se necessario, ruota tutte le password ad alta sensibilità a cui aveva accesso.

##### 5. Accesso di emergenza (Emergency Access): in caso ti succeda qualcosa

Immagina uno scenario: gestisci da solo tutti gli account familiari importanti, ma a causa di un ricovero improvviso o di un decesso la famiglia non può accedere a banca, email e assicurazione. La funzione <strong>"Accesso di emergenza"</strong> è pensata proprio per questo: autorizza una persona di fiducia (familiare o amico) a ottenere la tua cassaforte quando tu non puoi rispondere.

<strong>Configurazione dell'accesso di emergenza in Bitwarden:</strong>

1. Accedi a Bitwarden Web Vault → Impostazioni → Accesso di emergenza.
2. Aggiungi l'email del contatto fidato e invita ad accettare.
3. Imposta il "periodo di attesa" (consigliato 7-14 giorni): il lasso di tempo tra la richiesta dell'altra parte e la tua conferma.
4. Se non rispondi entro il periodo di attesa (rifiuti o non fai nulla), allo scadere l'altra parte ottiene automaticamente l'accesso.
5. Puoi rifiutare manualmente la richiesta o revocare l'accesso di emergenza in qualsiasi momento.

<strong>Accesso di emergenza in 1Password:</strong>

1. 1Password non lo chiama direttamente "accesso di emergenza", ma può essere realizzato tramite la funzione "organizzazione famiglia/team": dopo aver invitato i familiari nella versione famiglia, si pongono alcune voci nella "cassaforte condivisa".
2. Per gli utenti della versione personale, consiglio di comunicare la password principale a un familiare altamente fidato, o di scriverla in una busta sigillata conservata in cassaforte.
3. 1Password fornisce anche un "codice di recupero": quando si attiva la verifica in due fattori, va stampato e conservato.

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Imposta ora: lascia ai tuoi cari una "chiave di riserva"

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Scegli un familiare fidato come "contatto di emergenza".
2. Nel gestore di password imposta l'accesso di emergenza (Bitwarden) o aggiungilo alla cassaforte condivisa di famiglia (1Password).
3. Scrivi su carta la password principale + il codice di recupero, sigilla la busta e conservala in cassaforte di casa o affidala a un familiare fidato.
4. Rivedi ogni sei mesi che il contatto di emergenza sia ancora la persona giusta.
:::

#### 9. Buone pratiche per l'uso del gestore di password

- <strong>Imposta una password principale forte</strong>: la password principale è l'ultima linea di difesa; scegline una lunga e complessa e memorizzala bene.
- <strong>Attiva la verifica in due fattori</strong>: attiva il 2FA sull'account del gestore di password, per aggiungere un livello di protezione.
- <strong>Controlla regolarmente le password deboli</strong>: la maggior parte dei gestori ha una funzione di "audit di sicurezza" che aiuta a trovare password deboli e duplicate.
- <strong>Non dimenticare la password principale</strong>: la password principale non è recuperabile; dimenticarla significa perdere tutte le password. Consiglio di scriverla su carta e conservarla in un luogo sicuro.
- <strong>Accesso di emergenza</strong>: imposta un contatto di emergenza, così se tu non puoi accedere, una persona fidata può ottenere le tue password.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Promemoria importante

{class="mt-1"}
Il gestore di password è comodo ma comporta anche rischi: se la password principale viene esposta, tutte le password sono compromesse. La password principale non deve quindi essere uguale alle altre, né essere scritta in un luogo facilmente reperibile. Inoltre, preferisci provider con una buona storia di sicurezza.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Prova ora: inizia a usare un gestore di password

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Scegli un gestore di password (consigliato Bitwarden o quello di sistema).
2. Registra un account e imposta una password principale forte.
3. Importa le password esistenti (se ne hai) o inizia ad aggiungerne di nuove.
4. Installa l'estensione del browser o l'App mobile e prova la compilazione automatica.
5. Esamina il report di audit di sicurezza e individua le password da migliorare.
:::
