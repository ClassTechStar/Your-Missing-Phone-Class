---
id: di-san-shi-ba-zhang
num: 38
part: ai-biancheng-pian
nav: Capitolo 38: I cinque principi di pensiero della programmazione con l'AI
toc: default
kind: chapter
---

### Capitolo 38: I cinque principi di pensiero della programmazione AI

{class="chapter-intro mb-4"}
Se di questo libro devi ricordare un solo capitolo, che sia questo. I cinque principi di pensiero sono il cuore del libro; tutti i capitoli successivi — contesto, requisiti, dialogo, qualità — sono lo sviluppo di questi cinque principi in scenari diversi. Non spaventarti: nessuno è difficile da capire, ma ognuno merita di essere interiorizzato attraverso alcuni progetti.

L'inizio della storia è curioso: Andrej Karpathy, aprendo il codice del suo progetto, allegò un file CLAUDE.md di sole 70 righe con quattro principi fondamentali per collaborare con l'AI. Quel file ottenne oltre 70.000 star su GitHub e divenne il riferimento più citato dai praticanti di programmazione AI. Non sono slogan vuoti, ma abitudini di pensiero operative tratte da molta pratica. Questo libro ne aggiunge un quinto — l'iterazione e verifica — completando il sistema dei cinque principi.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perché un file di 70 righe vale così tanto?

{class="mt-1"}
Cosa significano 70.000 star? La maggior parte dei progetti su GitHub non ci arriva mai. Che un file di testo di 70 righe le ottenga dimostra una cosa: nell'era dell'AI ciò che manca non è il codice, ma la capacità di «pensare con chiarezza». Quelle 70 righe sono la versione concentrata del «pensare con chiarezza».
:::

#### 1. Principio uno: Think Before Coding (prima pensa, poi codifica)

È il più controintuitivo dei cinque. Se l'AI ci aiuta a scrivere codice, perché «pensare prima»? La risposta è semplice: la qualità dell'output dell'AI è proporzionale alla qualità del tuo input. Se non hai chiaro cosa fare, l'AI ti farà finire in un ciclo infinito di «correzioni» — il cosiddetto «l'AI si perde insieme a te».

«Pensare prima» significa che prima di dare un'istruzione all'AI devi rispondere a tre domande, un «triangolo del pensiero» inscindibile:

1. Quale problema voglio risolvere? (obiettivo)
2. Come deve essere il risultato atteso? (criteri di accettazione)
3. Quali vincoli devo rispettare? (confini)

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dimensione di pensiero</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Input vago (scadente)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Input chiaro (buono)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Definizione del problema</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fammi un sito web</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fammi un sito personale con tre schede di accesso a mini-strumenti AI</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Risultato atteso</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bello da vedere</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Layout responsive, tema scuro, schede con animazione al passaggio del mouse, utilizzabile su mobile</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Vincoli</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">(non specificato)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Niente framework, solo HTML+CSS+JS, deploy in un file, niente backend</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Confronto tra input vago e input chiaro per lo stesso requisito

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attenzione: pensare prima ≠ scrivere prima un documento perfetto

{class="mt-1"}
«Pensare prima» non significa «scrivere un PRD perfetto e poi iniziare». È un processo di pensiero rapido ma ordinato: 30 secondi per chiarire le tre domande valgono molto più di 30 minuti a correggere continuamente in chat. Per i compiti piccoli basta una riga; per i progetti grandi si possono estendere in un documento di requisiti completo (vedi Capitolo 40).
:::

#### 2. Principio due: Simplicity First (prima la semplicità)

La più grande trappola della programmazione AI non è «non riuscire a farlo», ma «fare troppo». Se dici all'AI «fammi un sistema di gestione utenti», potrebbe generare autenticazione, permessi, ruoli, log di audit, esportazione dati e altro — mentre forse ti serve solo una semplice pagina di login. L'over-generation è la principale causa di gonfiore del codice AI.

«Semplicità prima» richiede di seguire il principio del «minimo vitale» a ogni istruzione: meno codice possibile per la funzione core, la soluzione più semplice per il problema, il minor numero di funzioni per validare l'idea. Karpathy ha una metafora efficace: «Se devi calcolare un prezzo scontato, non ti serve un motore e-commerce.»

Nella pratica, «semplicità prima» significa alcune abitudini concrete:

- Chiedi all'AI un solo pezzo di funzionalità alla volta, non l'intero sistema in un colpo;
- Preferisci libreria standard e soluzioni semplici invece di dipendenze complesse;
- Se un problema si risolve in 50 righe, non farne scrivere 500 all'AI;
- Quando l'output dell'AI va oltre l'ambito, digli con coraggio «taglia il superfluo».

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Scenario</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Soluzione eccessiva (da evitare)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Soluzione semplice (consigliata)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Serve memorizzare dati</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Database MySQL + ORM</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prima usa file JSON o SQLite</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Serve l'accesso utente</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OAuth2.0 + JWT + ruoli e permessi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prima una semplice verifica password</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Serve un framework frontend</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">React + Redux + Router</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prima prova HTML puro + JS nativo</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Serve il deploy online</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Docker + CI/CD + K8s</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prima falo funzionare in locale</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Confronto tra soluzioni eccessive e semplici negli scenari comuni

#### 3. Principio tre: Surgical Changes (modifiche chirurgiche)

Quando iteri su un progetto esistente, ogni modifica deve essere precisa come un intervento chirurgico: toccare solo ciò che va toccato. Nella programmazione AI è ancora più importante, perché l'AI tende a «cambiare qualcosina per conto suo»: gli chiedi di correggere un bug e si mette a ristrutturare mezzo file.

Il cuore delle «modifiche chirurgiche»: ogni istruzione all'AI deve specificare ambito e confini. Digli «modifica solo la funzione calculate_discount», «non toccare il resto», «mantieni lo stile del codice». Se le modifiche vanno oltre l'ambito richiesto, chiedigli subito di annullare il superfluo.

Karpathy lo illustra con un esempio di diff. Supponi di chiedere all'AI di aggiungere la logica del «prezzo soci» alla funzione di calcolo degli sconti del carrello: un buon output modifica solo quella funzione aggiungendo qualche riga; un cattivo output riscrive l'intero file — magari più «elegante», ma non sai se ha introdotto nuovi bug. Nella programmazione AI «sembrare meglio» non è mai un motivo per deviare dalle istruzioni.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Istruzione scadente (ambito vago)

{class="font-mono text-xs leading-relaxed"}
Ottimizza la logica di calcolo degli sconti di questo progetto
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Istruzione buona (ambito preciso)

{class="font-mono text-xs leading-relaxed"}
Modifica solo la funzione calculate_discount in cart.py: 1. Aggiungi la logica del prezzo soci allo sconto esistente 2. I soci hanno un ulteriore 10% di sconto 3. Non modificare la firma della funzione né altre funzioni 4. Mantieni lo stile di denominazione delle variabili
:::
:::

#### 4. Principio quattro: Goal-Driven Execution (esecuzione orientata all'obiettivo)

Questo principio risponde a una domanda chiave: devi dare all'AI istruzioni su «come farlo» o su «cosa fare»? La risposta di Karpathy è la seconda. Invece di dire «prima crea una classe, poi aggiungi i metodi, poi scrivi i test», digli «mi serve uno strumento che legga un file CSV e conti i valori unici di ogni colonna». Lascia che l'AI scelga il percorso, tu validi il risultato.

I vantaggi dell'«orientato all'obiettivo» sono doppi: per l'AI c'è più autonomia e può scegliere il percorso migliore senza essere vincolata dai tuoi passaggi intermedi; per te l'attenzione si sposta da «come farlo» a «il risultato è giusto?» — ed è esattamente ciò che deve fare un comandante.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attenzione: orientato all'obiettivo ≠ lasciar fare tutto

{class="mt-1"}
Richiede una validazione rigorosa dopo l'esecuzione: il risultato soddisfa i requisiti? I casi limite sono gestiti? C'è over-design evidente? Se non è come ti aspettavi, dai un feedback concreto — non «riscrivi», ma «il problema è che con lista vuota viene lanciato IndexError, aggiungi un controllo sul valore nullo».
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Stile di istruzione</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Esempio</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Caratteristiche del risultato</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Imperativo (come farlo)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">«Prima crea una classe Python chiamata DataParser, aggiungi un metodo parse che accetta filename, leggi con il modulo csv…»</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">L'AI diventa una dattilografa; i tuoi passaggi intermedi potrebbero non essere il percorso ottimale</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Per obiettivo (cosa fare)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">«Mi serve uno strumento: leggere un file CSV, contare i valori unici per colonna, restituire JSON. Fornisci l'implementazione completa.»</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">L'AI sceglie il percorso ottimale, tu validi il risultato</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Confronto tra istruzioni imperative e per obiettivo

#### 5. Principio cinque: Iterate and Verify (itera e verifica)

È il quinto principio aggiunto da questo libro sulle quattro basi di Karpathy. La convinzione di fondo: il primo output dell'AI quasi mai è la versione finale. La programmazione AI efficace è un ciclo «genera-verifica-correggi», non un monolitico «istruzione-output».

«Iterare e verificare» non è un passivo «se non va bene riprova», ma un flusso di verifica strutturato. Dopo ogni output dell'AI verifica su tre livelli:

- Livello 1 · verifica funzionale: gira? Input e output sono corretti?
- Livello 2 · verifica dei casi limite: input vuoto, molto lungo, anomalo — cosa succede?
- Livello 3 · verifica architetturale: la struttura del codice è sensata? Ci sono hardcode? È facile da estendere?

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-bullseye mr-1"></i> Definire l'obiettivo</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> L'IA genera codice</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Verifica funzionale</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Superato</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Verifica dei casi limite</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Superato</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-landmark mr-1"></i> Revisione dell'architettura</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Superato — si passa al passo successivo</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> Non superato</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Dai feedback specifici</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> Rigenera</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 2: il ciclo di iterazione e verifica della programmazione AI
:::

Il punto chiave è il «feedback concreto». Se la verifica fallisce, non dire «sbagliato, rifai», ma «la funzione con lista vuota lancia IndexError, aggiungi un controllo alla riga 15». Un feedback preciso permette all'AI di correggere in modo mirato; uno vago la fa solo reindovinare la tua intenzione.

#### 6. Harness Engineering: Agent = Model + Harness

A metà 2026 il concetto di Harness Engineering divenne popolare nella community della programmazione AI. La formula è semplice:

:::inline div .quote-line .text-center .text-base .font-bold
<strong>La capacità di un agent = capacità del modello × qualità dell'harness</strong>
:::

La capacità del modello è il tetto intellettuale del cervello AI; l'Harness è l'«ambiente di lavoro» costruito intorno al modello: gestione del contesto, integrazione strumenti, orchestrazione dei flussi, sistema di memoria.

Questo concetto spiega un dubbio comune: perché con lo stesso GPT-4 o Claude qualcuno fa progetti brillanti e qualcuno ottiene codice mediocre? La differenza non è nel modello, ma nell'Harness. Un buon Harness include: specifiche di progetto chiare, integrazione ragionevole degli strumenti, contesto di dialogo ordinato, flussi di verifica completi. Il modello fissa il tetto, l'Harness determina quanto lo puoi sfruttare.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
La metafora del tirocinante geniale

{class="mt-1"}
Immagina il modello come un tirocinante geniale: altissimo QI, ma senza documentazione di progetto, strumenti, scadenze e criteri di accettazione non produce nulla di buono. L'Harness Engineering è l'ingegneria di «come costruire l'ambiente di lavoro per un tirocinante geniale».
:::

I capitoli successivi ti insegnano di fatto a costruire un buon Harness: capitolo 39 gestione del contesto (memoria di progetto), capitolo 40 definizione dei requisiti (PRD), capitolo 43 tecniche di dialogo (prompt a livelli), capitolo 45 qualità (flussi di verifica). Insieme formano il tuo Harness.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Pratica: scompone la tua prossima idea con il «triangolo del pensiero»

{class="mt-1"}
Scegli una piccola cosa che hai sempre voluto fare (una pagina con il conto alla rovescia, uno script per ricordarti di bere). In 3 minuti rispondi: ① Quale problema risolve? ② Come deve risultare? ③ Quali vincoli (tempo, tecnologia, ambiente)? Scrivi le risposte in un paragrafo. Complimenti: hai appena fatto il tuo primo «Think Before Coding» — quel paragrafo è già un'istruzione di qualità.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riepilogo del capitolo

- I cinque principi vengono dal CLAUDE.md di Karpathy (70 righe, 70K+ star); questo libro aggiunge il quinto «itera e verifica»
- Think Before Coding: prima di parlare rispondi a tre domande — cosa fare? Come deve risultare? Quali vincoli?
- Simplicity First: la più grande trappola dell'AI è «fare troppo» — per calcolare uno sconto non serve un motore e-commerce
- Surgical Changes: modifiche precise come in chirurgia, rifiuta il «cambio qualcosina» dell'AI
- Goal-Driven Execution: di «cosa fare», non «come farlo», e lascia scegliere il percorso all'AI
- Iterate and Verify: tre livelli di verifica (funzionale/casi limite/architettura) + feedback concreti, ciclo iterativo
- Harness Engineering: capacità = modello × Harness, gestisci l'AI come un «tirocinante geniale»
:::
