---
id: di-si-shi-san-zhang
num: 43
part: ai-biancheng-pian
nav: Capitolo 43: Conversation engineering — Tecniche per un dialogo efficace
toc: default
kind: chapter
---

### Capitolo 43: Ingegneria del dialogo — la tecnica di conversazione per collaborare in modo efficace con l'AI

{class="chapter-intro mb-4"}
Il dialogo è il modo principale di interazione nella programmazione con l'AI. Ma attenzione: «dialogare» non significa «chiacchierare»: un dialogo efficace per programmare con l'AI è una tecnica di comunicazione strutturata, che chiamiamo «ingegneria del dialogo». Il suo oggetto di studio è come ottenere il codice di massima qualità con il minor numero possibile di turni di conversazione. In parole povere, questo capitolo ti insegna a «farti capire bene» dall'AI.

#### 1. La strategia dei prompt a livelli

Il dialogo con l'AI può dividersi in tre livelli, ognuno con una funzione diversa. Capire questi tre livelli ti permette di comporre prompt efficaci come facendo giochi di costruzione.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Livello</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Funzione</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Esempio</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Frequenza</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Livello di sistema</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Definisce il ruolo dell'AI e i vincoli globali</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">«Sei un esperto di React, il codice deve essere in TypeScript»</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Si imposta una volta, all'inizio del progetto</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Livello di attività</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Descrive lo specifico compito da svolgere</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">«Crea un componente form con i campi nome utente e password»</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Si fornisce all'inizio di ogni attività</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Livello di feedback</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Valuta e corregge l'output dell'AI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">«Al campo password manca l'interruttore mostra/nascondi: aggiungilo»</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Si fornisce in base alla qualità dell'output</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
I tre livelli dei prompt di dialogo

Il prompt del livello di sistema di solito vive nel file di memoria del progetto (come CLAUDE.md) e non va ripetuto a ogni dialogo. Il livello di attività è quello che usi più spesso nel dialogo: deve contenere i tre ingredienti «cosa fare», «con quale tecnologia» e «con quali vincoli». Il livello di feedback è quello che mette alla prova la maestria: un buon feedback permette all'AI di correggere con precisione, uno cattivo la fa solo tornare a indovinare.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consiglio: le tre mosse vincenti del feedback

{class="mt-1"}
Un template di feedback pratico è «indicare il problema + spiegare cosa ci si aspetta + fornire il contesto». Per esempio: «la gestione degli errori alla riga 25 usa solo console.log (indicare il problema), in produzione andrebbe usato un gestore degli errori unificato che restituisca messaggi chiari per l'utente (spiegare cosa ci si aspetta), nel progetto c'è una funzione handleError pronta all'uso (fornire il contesto)». Un feedback così vale dieci volte più di «sistemami la gestione degli errori».
:::

#### 2. Dialoghi di debug: come descrivere gli errori perché l'AI li individui in fretta

Il debug è uno degli scenari più frequenti nella programmazione con l'AI. Quando incontri un bug, il modo in cui descrivi il problema all'AI determina direttamente se riesce a individuarlo e ripararlo in fretta. Ecco i quattro punti chiave del dialogo di debug:

1. Mostra all'AI le informazioni originali, non la tua parafrasi. Cita direttamente all'AI, con la @, i log degli errori, le tracce delle eccezioni e il codice interessato, invece di descriverli con un «sembra ci sia un errore di qualcosa». L'AI, davanti alle informazioni originali, è più precisa di quanto lo sia interpretando la tua versione.
2. Descrivi la differenza tra «comportamento atteso» e «comportamento effettivo». «Mi aspetto che dopo il clic sul pulsante si passi alla pagina iniziale (atteso), ma in realtà dopo il clic la pagina non reagisce (effettivo)»: una descrizione così è molto più utile di «il pulsante non funziona».
3. Fornisci i passi per riprodurre il problema. «Prima inserisco il nome utente, poi clicco sul pulsante di accesso, ed ecco che appare questo errore»: i passi di riproduzione permettono all'AI di simulare il tuo percorso di operazioni e individuare il problema più facilmente.
4. Dì chiaramente cosa hai già provato. «Ho già controllato le richieste di rete: restituiscono 200 e i dati sono a posto»: questo aiuta l'AI a escludere le strade già verificate e a non sprecare tempo ripetendo gli stessi controlli.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Descrizione di debug scadente

{class="font-mono text-xs leading-relaxed"}
Il pulsante non risponde al clic, dai un'occhiata
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Descrizione di debug ben fatta

{class="font-mono text-xs leading-relaxed"}
Clic sul pulsante di accesso: la pagina non reagisce. Comportamento atteso: dopo il clic si passa alla pagina /home Comportamento effettivo: dopo il clic non succede nulla e la console non mostra errori Passi di riproduzione: 1. Nella pagina di accesso inserire il nome utente admin e la password 123456 2. Cliccare sul pulsante «Accedi» 3. La pagina non reagisce Verifiche già fatte: - Le richieste di rete funzionano, restituiscono 200 - L'evento onClick è collegato - Ho controllato il codice del componente LoginButton File interessati: @src/components/LoginButton.tsx @src/pages/Login.tsx
:::
:::

#### 3. Strategie di iterazione: piccoli passi veloci vs grande refactoring

Nella programmazione con l'AI l'iterazione segue due strategie di base, adatte a scenari diversi. Capirne le differenze ti aiuta a scegliere bene in ogni situazione.

La strategia dei «piccoli passi veloci» è adatta allo sviluppo di funzionalità e alla correzione dei bug. Il suo nucleo è: a ogni giro fai fare all'AI una sola piccola modifica, e passi alla successiva solo dopo averla verificata. Il vantaggio è che ogni passo è verificabile e reversibile, con rischi sotto controllo; lo svantaggio è che è più lenta e richiede interazioni frequenti. Adatta a: sviluppo di nuove funzionalità, esplorazione quando non sai quale sia la soluzione migliore, iterazione prudente quando non ti fidi troppo dell'output dell'AI.

La strategia del «grande refactoring» è adatta alle modifiche su larga scala quando l'obiettivo è chiaro. Il suo nucleo è: descrivi l'obiettivo completo in una volta sola e lasci che sia l'AI a pianificare ed eseguire l'intera modifica. Il vantaggio è la velocità: l'AI vede il quadro generale e prende decisioni architetturali migliori; lo svantaggio è il rischio alto: se l'AI fraintende, correggere costa caro. Adatta a: aggiornamenti architetturali ben definiti, migrazioni di codice su larga scala, refactoring coperti da test adeguati.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Aspetto</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Piccoli passi veloci</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Grande refactoring</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Portata di ogni modifica</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Una funzionalità o un bug</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Un modulo o un livello dell'architettura</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Frequenza di verifica</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Verifica subito dopo ogni modifica</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Verifica complessiva al termine di tutte le modifiche</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Turni di dialogo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Molti (5-10 per funzionalità)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pochi (1-3 per modulo)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rischio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Basso, ogni passo è reversibile</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Alto, correggere gli scostamenti costa caro</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Scenari adatti</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nuove funzionalità, sviluppo esplorativo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Refactoring e migrazioni con obiettivi chiari</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prerequisiti</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nessun requisito particolare</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Serve una copertura di test</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Confronto tra le due strategie di iterazione

Nella pratica le due strategie si usano spesso in combinazione. Per esempio, nel rifattorizzare un modulo, prima con il «grande refactoring» fai dare all'AI una proposta complessiva; dopo averla esaminata, la esegui a piccoli passi con i «piccoli passi veloci». Così mantieni la vista d'insieme e insieme tieni sotto controllo il rischio di esecuzione.

#### 4. Gestione del contesto nei dialoghi a più turni

Man mano che i turni di dialogo aumentano, devi gestire attivamente il contesto della conversazione per evitare il problema dell'«AI che dimentica le informazioni di inizio dialogo». Ecco alcuni trucchi pratici per gestire il contesto.

Primo: «ancorare» le informazioni chiave. All'inizio del dialogo scrivi chiaramente i vincoli importanti e, nel prosieguo, ripetili al momento giusto. Per esempio: «ricorda che i nostri dati stanno nel localStorage e non possiamo usare un database» — ribadisci questo vincolo nelle richieste di modifica correlate, per impedire che l'AI se lo dimentichi.

Secondo: usa bene il trucco del «riepilogo e ripresa». Quando il dialogo diventa molto lungo, chiedi all'AI di «riepilogare i progressi fatti finora e le cose ancora da fare», poi apri un nuovo dialogo partendo da quel riepilogo. Così conservi il contesto essenziale ed eviti il degrado tipico dei dialoghi lunghi.

Terzo: «un dialogo, un'attività». È la strategia di gestione del contesto più semplice ed efficace. Ogni dialogo gestisce una sola attività o una sola funzionalità; finita quella, apri un nuovo dialogo per la successiva. Questo limita naturalmente la lunghezza del dialogo e tiene il contesto ben chiaro.

Quarto: sfrutta le funzioni di gestione del contesto degli strumenti. Quasi tutti gli strumenti di programmazione AI hanno un pulsante «cancella contesto» o «nuova sessione»: quando senti che la qualità delle risposte dell'AI sta peggiorando, non esitare, apri una nuova sessione. Perdere un po' di cronologia del dialogo è molto meglio che continuare a faticare in un contesto degradato.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Metti in pratica: fai da «paziente» alla tua AI

{class="mt-1"}
Crea apposta, nel browser, una piccola pagina con dentro un bug (per esempio un pulsante che non reagisce). Poi descrivi tutto all'AI una volta sola, seguendo il formato della «descrizione di debug ben fatta» di questo capitolo: informazioni originali, atteso contro effettivo, passi di riproduzione, verifiche già fatte. Senti la differenza di velocità con cui l'AI individua il problema — capirai perché «descrivere il problema» è in sé un mestiere.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riepilogo del capitolo

- I tre livelli dei prompt: livello di sistema (da scrivere nel file di memoria), livello di attività (cosa fare + tecnologia + vincoli), livello di feedback (problema + risultato atteso + contesto)
- I quattro punti del debug: fornire le informazioni originali, atteso vs effettivo, passi di riproduzione, verifiche già fatte
- Piccoli passi veloci: rischio basso e molti turni, ideali per le nuove funzionalità; grande refactoring: rischio alto e pochi turni, serve la protezione dei test
- Le quattro mosse per gestire il contesto: ancorare le informazioni chiave, riepilogo-ripresa, un dialogo un'attività, aprire senza esitazioni una nuova sessione
:::
