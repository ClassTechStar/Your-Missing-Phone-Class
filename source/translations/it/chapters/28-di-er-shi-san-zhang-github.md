---
id: di-er-shi-san-zhang-github
part: chao-yue-pian
nav:  Appendice: Guida per principianti a GitHub
toc: sub
kind: chapter
---

### Appendice al Capitolo 23: Guida a GitHub — dall'hosting del codice alla piattaforma di collaborazione

{class="chapter-intro mb-4"}
Nel capitolo precedente abbiamo parlato di "pensiero computazionale"; per tradurlo in pratica e fare progetti con altre persone, non si può ignorare un nome: GitHub. Che tu sia uno studente di Informatica che partecipa a competizioni, voglia conservare le proprie opere di codice o semplicemente voglia vedere a cosa lavorano gli sviluppatori di tutto il mondo, GitHub è una piattaforma che devi conoscere. In questa sezione partiamo dai concetti più basilari per aiutarti a costruire una comprensione chiara.

#### 1. Cos'è davvero GitHub?

In parole semplici, GitHub è una <strong>piattaforma di hosting e collaborazione per il codice</strong> basata su Git. Lanciato nel 2008 e acquisito da Microsoft nel 2018, è ancora oggi la più grande piattaforma al mondo di hosting di codice open source, con centinaia di milioni di repository che coprono quasi tutti i principali linguaggi di programmazione.

Per capirlo con un'analogia: <strong>Git è il tuo diario sul computer, GitHub è una piattaforma di blog pubblica</strong> — puoi pubblicare le tue opere, seguire i progetti altrui, partecipare a discussioni e collaborazioni. Non è solo il "magazzino di retroscene dei programmatori", è piuttosto come una "città tecnologica" costruita collettivamente dagli sviluppatori di tutto il mondo: qui i progetti nascono, iterano, vengono discussi e riutilizzati.

Per le persone comuni GitHub non è irraggiungibile. Molti non programmatori lo usano per ospitare appunti, ebook, blog personali o persino per il backup di file di configurazione. Se hai anche solo un po' di esigenza di "organizzare le tue cose e condividerle", GitHub merita di essere conosciuto.

#### 2. Differenza tra Git e GitHub (concetti chiave!)

Molti confondono questi due termini al primo contatto; ecco una sintesi chiara:

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Elemento di confronto</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Git</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GitHub</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Natura</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Strumento di controllo versione (software)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Piattaforma di hosting del codice (sito web)</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Posizione di esecuzione</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sul computer locale</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nel cloud (accesso via browser)</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Responsabilità principale</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Registrare ogni modifica dei file (cosa è cambiato, chi, quando)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mettere i repository Git nel cloud per archiviazione, visualizzazione e collaborazione</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rete necessaria?</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">No, funzionamento offline</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sì, richiede connessione</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Appartenenza</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Software open source, creato da Linus Torvalds (il padre di Linux)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prodotto di Microsoft</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Concorrenti</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SVN, Mercurial</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitLab, Gitee, Bitbucket</td>
                            </tr>
                        </tbody>
                    </table>
```

In sintesi: <strong>Git gestisce "come registrare le modifiche", GitHub gestisce "dove mettere le modifiche e come collaborare"</strong>. Git è uno strumento che gira in locale; GitHub è una piattaforma che mette i repository Git nel cloud, facilitando collaborazione e visualizzazione. Puoi usare solo Git senza GitHub (ad esempio per il versioning del codice che scrivi tu), ma per usare GitHub devi usare Git (perché GitHub è basato su Git).

#### 3. Concetti e funzioni chiave di GitHub

##### 📁 Concetti di base

Prima di mettere mano, conosciamo alcune parole ad alta frequenza, altrimenti l'interfaccia di GitHub ti sembrerà incomprensibile:

- <strong>Repository (Repo)</strong>: a un progetto corrisponde un repository, che contiene tutti i file di codice del progetto, le versioni storiche e la documentazione. Puoi considerarlo come una "cartella di progetto".
- <strong>Commit</strong>: il record di una modifica al codice. Ogni commit ha un messaggio che descrive "cosa è cambiato in questa modifica e perché". È la base che permette a Git/GitHub di "viaggiare nel tempo".
- <strong>Branch (ramo)</strong>: una linea di sviluppo indipendente staccata da quella principale. Ad esempio, se vuoi aggiungere una nuova funzione puoi aprire un branch, svilupparlo separatamente e poi riunirlo a quello principale senza influenzare gli altri.
- <strong>Clone</strong>: copia integralmente il repository cloud sul computer locale, così potrai modificare il codice in locale.
- <strong>Push/Pull</strong>: Push carica il codice locale su GitHub, Pull scarica da GitHub sul locale l'ultimo codice. Sono le due azioni centrali per sincronizzare il codice nel lavoro di squadra.
- <strong>Pull Request (PR)</strong>: quando hai finito di modificare il codice su un branch e vuoi unirlo al branch principale, apri una PR per far sì che il team revisioni il codice prima dell'unione. È il meccanismo centrale della collaborazione su GitHub.
- <strong>Issue</strong>: serve a registrare bug, richieste di funzionalità, argomenti di discussione. Ogni Issue è come un post di discussione, a cui si può assegnare un responsabile e applicare etichette.
- <strong>Fork</strong>: copia il repository di qualcun altro sul tuo account: puoi modificare liberamente la tua copia senza influenzare il repository originale. Fatto questo, puoi inviare una PR all'autore originale per chiedere l'unione dei tuoi miglioramenti.

##### 🛠️ Funzioni chiave

GitHub non offre solo archiviazione di codice, ma anche:

- <strong>Controllo versione</strong>: registra la storia di ogni modifica del codice; se rompi qualcosa, puoi sempre tornare alla versione funzionante precedente.
- <strong>Collaborazione di squadra</strong>: supporta lo sviluppo parallelo di più utenti sullo stesso progetto, senza sovrascritture o conflitti.
- <strong>Issue tracking</strong>: registra bug e richieste di funzionalità con le Issue, facilitando il monitoraggio del team.
- <strong>Project management</strong>: integra strumenti di gestione come to-do list, bacheche di progetto (Projects), equivalente a un Trello leggero integrato.
- <strong>Automazione</strong>: tramite <strong>GitHub Actions</strong> realizza compilazione, test, packaging e deployment automatici dopo il commit del codice; è lo strumento centrale del moderno "CI/CD (Continuous Integration/Continuous Deployment)".
- <strong>Gestione documentazione</strong>: README introduce il progetto, Wiki ospita architettura dettagliata e standard di sviluppo, Pages può persino ospitare direttamente siti web statici.
- <strong>Hosting e presentazione del codice</strong>: ogni repository ha una bella pagina web, con syntax highlighting; è la "vetrina" delle tue opere tecniche.
- <strong>Community open source</strong>: puoi Star (aggiungi ai preferiti) i progetti che ti piacciono, Watch (segui) gli aggiornamenti, Follow (segui) gli sviluppatori, e partecipare alla collaborazione open source globale.

#### 4. Registrazione e primi passi: crea il tuo primo repository in cinque minuti

##### 📝 Registrare un account

1. Visita <a href="https://github.com" class="text-primary hover:underline" target="_blank" rel="noopener">github.com</a>, clicca su "Sign up".
2. Inserisci email, imposta password e nome utente (il nome utente comparirà nell'indirizzo della tua pagina personale, meglio se in inglese, ad esempio <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">github.com/yourname</code>).
3. Completa la verifica email e la verifica anti-bot.
4. Scegli il piano Free, più che sufficiente per un singolo utente.

##### 📁 Creare il primo repository

1. Dopo il login, clicca sul "+" in alto a destra e seleziona "New repository".
2. Inserisci il nome del repository (Repository name), ad esempio <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">my-first-project</code>.
3. Scrivi una breve descrizione (Description), per far capire a cosa serve il repository.
4. Scegli Public o Private. I repository pubblici sono visibili a tutti, quelli privati solo a te e ai collaboratori. Anche gli account gratuiti supportano un numero illimitato di repository privati.
5. Spunta "Add a README file" — il README è il "manuale di istruzioni" del progetto, è consigliato averlo in ogni repository.
6. Clicca "Create repository": il tuo primo repository GitHub è nato!

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Curiosità: cos'è il README

{class="mt-1"}
README.md è un file in formato Markdown, è la prima cosa che si vede aprendo il tuo repository. Un buon README di solito include: introduzione del progetto, metodo di installazione, esempi d'uso, licenza, contatti. Scrivere bene il README è una competenza di base del programmatore ed è la prima soglia per capire se un progetto sarà usato da altri.
:::

#### 5. Flusso di lavoro base: dal locale al cloud

Per capire il flusso di lavoro di GitHub, la chiave è ricordare questo ciclo: <strong>modifica locale → staging → commit → push → aggiornamento cloud</strong>. Ecco ogni passo in parole semplici:

1. <strong>Modificare i file</strong>: scrivi codice o modifichi documenti con l'editor sul computer locale.
2. <strong>git add</strong>: aggiungi i file modificati alla "area di staging", come dire a Git "queste modifiche sono pronte per essere registrate".
3. <strong>git commit</strong>: registra ufficialmente le modifiche in staging come un "commit", con un messaggio, ad esempio "fix del bug di login". Questo passo avviene solo in locale.
4. <strong>git push</strong>: carica i commit locali su GitHub nel cloud, così altri potranno vederli.
5. <strong>git pull</strong>: prima di iniziare a lavorare, scarica l'ultimo codice dal cloud per assicurarti di essere allineato con il resto del team.

Per i neofiti, ricorda questa formula: <strong>"prima pull poi modifica, finito di modificare add, commit con messaggio, infine push"</strong>. Con questa abitudine, il lavoro di squadra non cadrà nel caos.

#### 6. Flusso di collaborazione: come funziona una Pull Request

Il punto più forte di GitHub è il suo meccanismo di collaborazione. Un tipico flusso di squadra è questo:

1. <strong>Aprire un branch</strong>: dal branch principale (di solito main o master) apri un nuovo branch, ad esempio <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">feature/login</code>, su cui sviluppare la nuova funzionalità.
2. <strong>Sviluppare e fare commit</strong>: scrivi codice sul nuovo branch, con più commit per registrare l'avanzamento.
3. <strong>Push su GitHub</strong>: carica il branch sul repository cloud.
4. <strong>Aprire una Pull Request</strong>: sulla pagina web di GitHub apri una PR, chiedendo di unire il tuo branch al branch principale. Scrivi chiaramente cosa fa questa PR e perché.
5. <strong>Code Review</strong>: i membri del team esaminano il tuo codice, propongono modifiche o suggerimenti. Puoi continuare a fare commit in base ai feedback, la PR si aggiornerà automaticamente.
6. <strong>Merge</strong>: dopo l'approvazione, clicca "Merge" per unire il codice al branch principale. Il tuo contributo entra ufficialmente nel progetto!

Questo flusso garantisce che <strong>qualsiasi codice entri nel branch principale sia stato revisionato</strong>, riducendo drasticamente la probabilità di errori. Anche i progetti open source usano questo meccanismo per accettare contributi da sconosciuti di tutto il mondo: puoi aprire una PR su un noto progetto open source e, una volta accettata, diventi contributor di quel progetto.

#### 7. Scenari applicativi tipici di GitHub

##### 🎓 Studenti a competizioni e progetti di corso

Per gli studenti di Informatica che partecipano ad ACM, hackathon, tesi, GitHub è quasi indispensabile. Può fare da piattaforma di collaborazione e da vetrina per le opere — i giudici delle competizioni possono guardare direttamente il tuo repository, capire la qualità del codice e il processo di collaborazione. Molte aziende in fase di recruiting chiedono di allegare il link al profilo GitHub come prova delle capacità tecniche.

##### 📚 Knowledge base personale e hosting di appunti

Anche i non programmatori possono usare GitHub. Molti lo usano per ospitare appunti di studio, blog tecnici (con GitHub Pages puoi creare un sito gratis), ebook. Scrittura in Markdown + versioning Git + backup cloud: tre in uno.

##### 🌐 Partecipare a progetti open source

GitHub è la roccaforte del movimento open source globale. Puoi fare Fork dei progetti che ti piacciono, modificarli e inviare PR per dare indietro alla community; puoi anche semplicemente Star per collezionare buoni progetti e seguirne gli aggiornamenti. Partecipare all'open source è un ottimo modo per migliorare le competenze e costruirsi una reputazione.

##### 🤖 Deployment automatico e CI/CD

Con GitHub Actions si può realizzare un flusso totalmente automatico "push del codice → test automatici + deployment automatico sul server". Molti blog personali e siti di documentazione sono costruiti così: scritto l'articolo, si fa push e il sito si aggiorna da solo.

##### 💾 Backup del codice e sincronizzazione multi-device

Usa il repository di codice come un cloud disk: quando cambi computer o lavori su più dispositivi, basta un git pull per avere l'ultimo codice, senza più copiare su e giù da una chiavetta USB.

#### 8. Consigli per i neofiti

- <strong>Scrivi messaggi di commit chiari</strong>: non scrivere inutili "update". Un buon commit message è "risolto il problema del salto alla pagina sbagliata dopo il login dell'utente"; anche sei mesi dopo, riesaminandolo, capirai cosa facevi.
- <strong>Commit frequenti, passi piccoli</strong>: fai un commit per ogni piccola funzione completata, non un solo commit dopo un'intera giornata. In caso di problemi, sarà più facile localizzarli.
- <strong>Sviluppa su branch, non modificare direttamente il branch principale</strong>: anche per progetti personali, prendi l'abitudine di aprire branch; quando collaborerai con un team non sarai in difficoltà.
- <strong>Usa bene .gitignore</strong>: questo file dice a Git quali file non includere nel versioning (ad esempio configurazioni con password, prodotti di compilazione, cartelle di dipendenze), evitando di caricare file spazzatura.
- <strong>Guarda spesso progetti open source eccellenti</strong>: gira per GitHub Trending, guarda la struttura del codice, come è scritto il README e i flussi di collaborazione dei progetti ad alto numero di star: è il modo gratuito più veloce per migliorare.
- <strong>Richiedi il GitHub Student Pack</strong>: con la certificazione studentesca ottieni gratis un sacco di crediti per strumenti e servizi a pagamento (Copilot, domini, servizi cloud, ecc.), per un valore di migliaia di dollari.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Avvertenza di sicurezza

{class="list-disc pl-6 mt-1 space-y-1"}
- Non caricare mai su GitHub password, chiavi API, stringhe di connessione al database o altre informazioni sensibili, specialmente nei repository pubblici — una volta trapelate, vengono catturate dai crawler in pochi secondi, con conseguenze gravi.
- Se per sbaglio hai caricato informazioni sensibili, eliminare solo il file non basta (restano nello storico); devi usare <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git filter-branch</code> o strumenti professionali per pulire la cronologia e cambiare immediatamente le chiavi trapelate.
- Nemmeno i repository privati sono assolutamente sicuri: le informazioni sensibili vanno gestite con variabili d'ambiente, non nel repository di codice.
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Note per l'accesso a GitHub dalla Cina

{class="mt-1"}
L'accesso a GitHub dalla Cina a volte è instabile: può risultare non raggiungibile o con cloni lenti. Puoi provare: ① usare mirror cinesi (come GitClone, ghproxy) per accelerare il clone; ② configurare Hosts o usare un proxy; ③ se collabori principalmente con utenti cinesi, puoi considerare l'alternativa nazionale <strong>Gitee</strong>, con funzionalità simili e accesso più veloce. Molti team caricano contemporaneamente su GitHub e Gitee, coniugando internazionalizzazione e velocità locale.
:::

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Usi avanzati: costruire un blog personale gratuito con GitHub Pages

{class="mt-1"}
GitHub Pages ti permette di ospitare gratis un sito web statico; abbinato a generatori di siti statici come Jekyll, Hexo, Hugo, puoi creare facilmente un blog personale. Scrivi un articolo in Markdown, fai push sul repository e il blog si aggiorna automaticamente, con HTTPS e dominio personalizzato inclusi. Innumerevoli blogger tecnici hanno costruito il loro blog così: costo zero, niente pubblicità, versione controllata.
:::

#### 9. Conclusioni: perché tutti dovrebbero conoscere GitHub

GitHub non è più solo "lo strumento dei programmatori", è piuttosto un <strong>modo di lavorare dell'era digitale</strong>: il versioning rende tutto tracciabile, il meccanismo di collaborazione fa girare il team in modo efficiente, lo spirito open source fa circolare liberamente la conoscenza. Anche se non scrivi codice, capire i concetti di "commit, branch, merge" ti aiuterà a gestire meglio qualsiasi contenuto che richieda "modifiche ripetute + collaborazione multipla" — dalla tesi ai documenti, dagli appunti ai progetti.

Per gli studenti di Informatica, GitHub è ancora più una competenza indispensabile: è il tuo portfolio, la piattaforma di collaborazione, la libreria di risorse di apprendimento e il "curriculum" più convincente in fase di ricerca di lavoro. Apri prima possibile un account, carica i tuoi compiti di corso e i tuoi piccoli progetti, accumula con il tempo: dopo qualche anno avrai un curriculum tecnico che farà brillare gli occhi del recruiter.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Prova: completa la tua prima esperienza su GitHub

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Registrati su GitHub e completa il profilo (avatar, bio, aree tecnologiche di interesse).
2. Crea un repository pubblico chiamato <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">hello-github</code>, spunta "Add a README file".
3. Entra nel repository, clicca sul pulsante di modifica del README.md (icona della matita), scrivi in Markdown una breve presentazione di te stesso e fai il commit.
4. Nella barra di ricerca di GitHub cerca una parola chiave che ti interessa (ad esempio <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python-tutorial</code>), metti uno Star a due progetti che ti piacciono.
5. (Avanzato) Installa Git sul computer, clona il repository in locale, modifica il README e poi fai push sul cloud: hai completato un flusso "locale → cloud" integrale.
:::
