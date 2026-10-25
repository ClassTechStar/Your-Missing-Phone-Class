---
id: di-si-shi-wu-zhang
num: 45
part: ai-biancheng-pian
nav: Capitolo 45: Garanzia di qualità — Rendere affidabile il codice scritto dall'AI
toc: default
kind: chapter
---

### Capitolo 45: Garanzia di qualità — rendere affidabile il codice scritto dall'AI

{class="chapter-intro mb-4"}
Il codice scritto dall'AI ha un tratto distintivo: di solito «sembra giusto» — nomi delle variabili in regola, commenti completi, logica chiara. Ma «sembrare giusto» non vuol dire «essere giusto». I problemi nascosti nel codice dell'AI sono spesso più difficili da scovare che nel codice scritto a mano, perché la sua qualità apparente è così alta che porta ad abbassare la guardia. In questo capitolo impari a costruire per il codice dell'AI un sistema di garanzia della qualità davvero efficace — con tre linee di difesa, test, revisione e controllo di versione — per trasformare il «sembra giusto» in «è giusto davvero».

#### 1. Test-driven: fai scrivere i test all'AI

I test sono la prima linea di difesa della qualità nella programmazione AI. La buona notizia: far scrivere i test all'AI è più facile e affidabile che fargli scrivere il codice delle funzionalità — perché il comportamento atteso dei test è ben definito, ed è raro che ne escano codici «che sembrano giusti ma non lo sono».

Il flusso della programmazione AI guidata dai test è questo: prima fai scrivere all'AI il codice della funzionalità; appena le funzioni di base superano la verifica, fai scrivere subito i casi di test. I casi di test devono coprire il percorso normale, i casi limite e le situazioni anomale. Poi fai correggere all'AI il codice della funzionalità in base ai risultati dei test. Il bello di questo flusso: una volta scritti, i test diventano uno strumento di verifica permanente — ogni modifica successiva può essere convalidata eseguendo i test, per accertare di non aver introdotto regressioni.

::: div .code-block
:::inline div .code-head
<span>Istruzioni per l'IA: scrivi i test</span><span class="dots">···</span>
:::

```
Scrivi unit test per la funzione calculate_discount.
I casi di test devono coprire:
1. Percorso normale:
   - articolo da 100 yuan con il 20% di sconto -> 80
   - articolo da 200 yuan con il 50% di sconto -> 100
2. Casi limite:
   - articolo da 0 yuan con il 20% di sconto -> 0
   - articolo da 100 yuan con lo 0% di sconto -> 100 (nessuno sconto)
   - articolo da 100 yuan con il 10% di sconto -> 100 (prezzo pieno)
3. Casi di errore:
   - prezzo negativo -> deve lanciare un errore
   - sconto > 1 -> deve lanciare un errore
   - input non numerico -> deve lanciare un errore
Usa il framework Vitest e fornisci il file di test completo.
```
:::

Nota le caratteristiche di questa istruzione: elenca in modo esplicito le tre categorie di casi di test (normali, limite, anomali) e non lascia all'AI margine per «scegliere cosa testare». A volte l'AI scrive solo i test del percorso normale per «chiudere in fretta»; elencare esplicitamente tutte le categorie evita questo problema.

#### 2. Tecniche di revisione del codice

Anche con i test a copertura, il codice prodotto dall'AI va comunque revisionato a mano. Revisionare il codice non significa leggerlo riga per riga — costerebbe troppo tempo e dipenderebbe troppo dal tuo livello di programmazione. Una revisione efficace del codice AI deve guardare a queste dimensioni chiave:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Aspetti da revisionare</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cosa controllare</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Problemi frequenti</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sicurezza</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Validazione degli input, gestione delle chiavi, protezione dalle SQL injection</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">L'AI spesso dimentica di validare gli input e scrive le chiavi direttamente nel codice</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gestione degli errori</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Le eccezioni vengono catturate? I messaggi di errore hanno senso?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">L'AI ama i blocchi catch vuoti o il semplice console.log</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prestazioni</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ci sono problemi di prestazioni evidenti, come query N+1 o cicli infiniti?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A volte l'AI produce algoritmi O(n²)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Manutenibilità</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La struttura del codice è chiara? I nomi hanno un significato?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ogni tanto l'AI genera codice eccessivamente astratto</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gestione delle dipendenze</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Le dipendenze aggiunte sono necessarie? Le versioni sono indicate chiaramente?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">L'AI tende a introdurre librerie inutili</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Le dimensioni chiave della revisione del codice AI

Durante la revisione non serve controllare tutto da solo — puoi chiedere all'AI di fare la prima passata. Istruzione tipo: «revisiona la sicurezza, la gestione degli errori e le prestazioni di questo codice e segnala i potenziali problemi». La capacità di autoverifica dell'AI cresce di continuo: pur non sostituendo del tutto la revisione umana, ti aiuta a filtrare la maggior parte dei problemi evidenti.

#### 3. Controllo di versione: il ruolo di Git nella programmazione con l'AI

Nella programmazione AI Git conta ancora più che nella programmazione tradizionale. Dato che ogni modifica dell'AI può introdurre cambiamenti imprevedibili, ti serve un rimedio affidabile contro i ripensamenti — e il controllo di versione è proprio quel rimedio.

La buona pratica di Git nella programmazione AI è «commit frequenti, piccoli passi avanti». Ogni volta che completi un punto funzionale verificabile, fai un commit. Così, quando una modifica dell'AI crea problemi, puoi riposizionarti con precisione sull'ultimo stato utilizzabile, senza buttare via tutto il lavoro.

Un altro trucco utile è l'«isolamento nei branch». Per le modifiche AI dal risultato incerto (per esempio un grande refactoring), crea prima un branch nuovo e lavora lì. Se il risultato ti soddisfa, lo fondi nel branch principale; se no, cancelli il branch e il ramo principale non ne risente. Molto più sicuro che modificare più e più volte il branch principale.

1. Prima di ogni modifica dell'AI, assicurati che l'area di lavoro sia pulita (niente modifiche non committate). Così, se la modifica dell'AI non ti convince, puoi tornare indietro al volo con git checkout .
2. Dopo ogni modifica dell'AI, appena la verifica passa, committa subito. Nel messaggio di commit descrivi cosa ha fatto la modifica, per esempio «feat: aggiunta la funzione di registrazione utenti».
3. Per i grandi refactoring, crea prima il branch: git checkout -b refactor/auth-system. Porta a termine le modifiche sul branch e fondi solo dopo che i test passano.
4. Prendi l'abitudine di guardare il diff. Dopo ogni modifica dell'AI, usa git diff per vedere esattamente cosa è cambiato. Ti aiuta non solo a scovare i problemi, ma anche a imparare il codice.

#### 4. Trappole comuni e come evitarle

Nella programmazione AI ci sono alcune trappole che si ripresentano di continuo e in cui quasi tutti i principianti ci cadono. Conoscerle in anticipo ti fa evitare tanti giri a vuoto.

##### 1. Trappola uno: la trappola della fiducia

«Il codice scritto dall'AI sembra molto professionale, di sicuro va bene, no?» — è la trappola più pericolosa. Il codice generato dall'AI è in superficie molto ordinato — nomi in regola, commenti completi, struttura chiara — e questo «professionalismo di superficie» porta ad abbassare la guardia. Ma la pulizia della facciata non garantisce la correttezza della logica. Antidoto: verifica sempre con i test, invece di giudicare dal «sembra giusto o no».

##### 2. Trappola due: la trappola del gonfiore

«Visto che l'AI mi scrive il codice, perché non realizzare le funzioni in modo completo?» — e il codice gonfia. L'AI è bravissima a «dare del più»: le chiedi una pagina di login e ti consegna un sistema di gestione utenti completo. Le funzioni in più non solo aumentano la complessità, ma anche la probabilità di bug. Antidoto: rispetta con rigore il principio Simplicity First e dì chiaramente all'AI «fai solo questa funzione, non aggiungere altro».

##### 3. Trappola tre: la trappola della comprensione

«L'AI capirà comunque cosa intendo, no?» — non per forza. La capacità di comprensione dell'AI è notevole, ma davanti a richieste vaghe continua a «indovinare». Quando indovina male, il codice che produce è sbagliato. E c'è di peggio: il codice nato da un'indovinella sbagliata di solito «sembra molto ragionevole», e ti convince che abbia capito. Antidoto: nelle istruzioni dai dettagli concreti a sufficienza, per ridurre lo spazio in cui l'AI deve «indovinare».

##### 4. Trappola quattro: la trappola del contesto

«L'ho detto nei dialoghi precedenti, l'AI se lo ricorda ancora, no?» — molto probabilmente no. Man mano che i dialoghi si allungano o si aprono nuove sessioni, l'AI perde il contesto iniziale. Se un vincolo chiave non finisce nel file di memoria del progetto, c'è da scommettere che venga ignorato nelle modifiche successive. Antidoto: i vincoli chiave si scrivono nel file di memoria del progetto, senza contare sulla memoria dei dialoghi.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Ripasso rapido delle quattro trappole

{class="mt-1"}
Trappola della fiducia — non fidarti del «sembra giusto»; trappola del gonfiore — l'AI ama «dare del più»; trappola della comprensione — davanti a richieste vaghe «indovina»; trappola del contesto — la memoria dei dialoghi «dimentica». Gli antidoti corrispondenti sono: verifica con i test, taglia il superfluo, dai tutti i dettagli, scrivi nel file di memoria.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Metti in pratica: costruisci tre linee di difesa per il tuo progetto

{class="mt-1"}
Se hai già iniziato il Progetto 1 (il sito di strumenti): ① fai scrivere all'AI i 3 tipi di casi di test per le funzioni principali; ② revisiona il codice sulle cinque dimensioni (sicurezza / gestione degli errori / prestazioni / manutenibilità / dipendenze); ③ inizializza il progetto con git e fai il primo commit. Solo quando le tre linee di difesa sono pronte, il tuo progetto è davvero tuo.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riepilogo del capitolo

- Il codice AI che «sembra giusto» ≠ «è davvero giusto» — la qualità superficiale troppo alta fa proprio abbassare la guardia
- Fai scrivere i test all'AI: elenca esplicitamente le tre categorie di casi (normali / limite / anomali) per evitare i «test selettivi»
- Le cinque dimensioni della revisione: sicurezza, gestione degli errori, prestazioni, manutenibilità, gestione delle dipendenze
- Git è il «rimedio contro i ripensamenti»: commit frequenti, piccoli passi avanti, branch separati, diff sempre sotto gli occhi
- Le quattro trappole: fiducia (verifica coi test), gonfiore (taglia il superfluo), comprensione (dai tutti i dettagli), contesto (scrivi nel file di memoria)
:::
