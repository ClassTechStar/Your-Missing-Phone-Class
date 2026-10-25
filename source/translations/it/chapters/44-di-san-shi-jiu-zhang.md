---
id: di-san-shi-jiu-zhang
num: 39
part: ai-biancheng-pian
nav: Capitolo 39: Context engineering — Far capire le tue intenzioni all'AI
toc: default
kind: chapter
---

### Capitolo 39: Ingegneria del contesto — far capire all'AI le tue intenzioni

{class="chapter-intro mb-4"}
Ti è mai capitato che aprendo una nuova finestra di chat l'AI sembrasse amnesica e dimenticasse tutto del tuo progetto? Non lo fa apposta: è «smemorata» per natura. Questo capitolo ti insegna a installarle un «sistema di memoria a lungo termine» e ti presenta uno dei paradigmi di sviluppo più caldi del 2026: lo sviluppo guidato dalle specifiche.

#### 1. Il file di memoria di progetto: la «memoria a lungo termine» dell'AI

I modelli AI hanno un limite fondamentale: la memoria è «a breve termine». A ogni nuova conversazione l'AI sa zero del tuo progetto. Devi ripeterle «usiamo React», «il backend è Node.js», «il database è PostgreSQL», «lo stile del codice usa doppi apici». Non solo inefficiente, ma facile da dimenticare — come formare ogni giorno un nuovo collega.

La soluzione è il «file di memoria di progetto»: un file di testo nella root del progetto che gli strumenti AI leggono automaticamente a ogni conversazione. Ogni strumento ha la propria convenzione di nome:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Strumento</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Nome file</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cursorrules</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">CLAUDE.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitHub Copilot</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">copilot-instructions.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Soluzione generica</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">AGENTS.md</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Convenzioni di nome del file di memoria per ogni strumento

Nomi diversi, stesso principio: scrivi in quel file ciò che l'AI deve «ricordare sempre». Un buon file di memoria di progetto contiene: panoramica del progetto (che cos'è), stack tecnologico (quali tecnologie), standard di codice (naming, indentazione, commenti), struttura delle cartelle (come è organizzato il codice), convenzioni di sviluppo (strategia dei branch, commit, test). Il CLAUDE.md di Karpathy ha solo 70 righe ma copre tutte le informazioni chiave: conciso e completo.

::: div .code-block
:::inline div .code-head
<span>CLAUDE.md</span><span class="dots">···</span>
:::

```
# Progetto: app personale di gestione finanze
## Panoramica
Un'app full-stack di finanza personale che aiuta a registrare entrate e uscite quotidiane.
## Stack tecnologico
- Frontend: React + TypeScript + Tailwind CSS
- Backend: Node.js + Express + TypeScript
- Database: SQLite (sviluppo) / PostgreSQL (produzione)
- Test: Vitest
## Convenzioni del codice
- Usa virgolette doppie
- Indentazione di 2 spazi
- Nomi delle funzioni in camelCase
- Definizioni di tipo in PascalCase
- Ogni funzione deve avere un commento JSDoc
## Struttura delle cartelle
/src
  /frontend  - codice frontend
  /backend   - codice backend
  /shared    - tipi condivisi tra frontend e backend
  /tests     - file di test
## Regole di sviluppo
- Messaggi di commit in italiano
- Le nuove funzionalità richiedono prima i test
- Le API rispondono sempre con { success, data, error }
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attenzione: non trasformarlo in un «secondo documento di requisiti»

{class="mt-1"}
Fai attenzione alla lunghezza: non deve diventare un documento di requisiti di decine di pagine. Lo scopo è «far costruire rapidamente il contesto all'AI», non «descrivere in dettaglio ogni funzione». Mantienilo conciso, strutturato, solo «ciò che l'AI deve sapere».
:::

#### 2. Sviluppo guidato dalle specifiche (SDD)

Lo Spec-Driven Development (SDD) è un paradigma di sviluppo maturato progressivamente nel 2026: prima le specifiche, poi il codice. A differenza del TDD tradizionale (test-driven development), le «specifiche» dell'SDD non sono solo casi di test, ma anche descrizioni dei requisiti, definizioni di interfacce, modelli di dati. L'AI genera il codice sulla base di queste specifiche; agli umani spetta scriverle e mantenerle.

Il flusso dell'SDD in cinque passi:

1. Descrivi i requisiti in linguaggio naturale (in un file .md);
2. Definisci interfacce e strutture dati (nel file di specifiche);
3. Lascia che l'AI generi il codice dalle specifiche;
4. Esegui i test per verificare la conformità alle specifiche;
5. Se non è conforme, correggi le specifiche o fai correggere il codice all'AI.

In questo flusso il file di specifiche è la «fonte di verità unica»: il codice si può rigenerare, le specifiche devono essere giuste prima.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Scrivi il file di specifiche</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Le specifiche sono complete?</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Completa</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> L'IA genera codice dalle specifiche</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Esegui i test per verificare l'output</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> Incompleta / test falliti</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-tools mr-1"></i> Problema nel codice → correggi il codice; problema nelle specifiche → correggi le specifiche</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> Torna alla verifica</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Tutto superato → consegna</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 3: flusso di lavoro dello sviluppo guidato dalle specifiche (SDD)
:::

Il vantaggio dell'SDD: le specifiche sono più stabili del codice. Quando cambiano modello o strumento, le tue specifiche restano valide e basta rigenerare il codice con il nuovo strumento AI. Ecco perché il libro insiste che «la metodologia conta più degli strumenti»: il file di specifiche è il veicolo concreto della tua metodologia.

#### 3. Gestione della finestra di contesto

Anche con il file di memoria di progetto, in chat può emergere il problema del «contesto insufficiente». La finestra di contesto dei modelli AI (la quantità di informazioni elaborabili contemporaneamente) è limitata. Quando la conversazione è troppo lunga e i file citati troppi, l'AI «dimentica» le informazioni iniziali e la qualità cala — come una chiacchierata di sei ore con un amico che ha già dimenticato cosa gli avevi detto all'inizio.

La strategia centrale è il «riferimento a livelli»:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Livello di contesto</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Contenuto</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Gestione</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Livello 1: memoria di progetto</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stack, specifiche, struttura cartelle</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Scritto in file come CLAUDE.md, caricato automaticamente, senza ripetizioni</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Livello 2: riferimenti a file</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">I file di codice coinvolti nell'attività corrente</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Riferisci con il simbolo @ in modo preciso, non incollare interi file in chat</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Livello 3: contesto di dialogo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cronologia della conversazione sull'attività corrente</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A fine attività apri una nuova chat per evitare che il contesto si gonfi</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Livello 4: istruzioni immediate</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Requisiti specifici di questo passaggio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Chiari, concisi, mirati; evita descrizioni prolisse</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Strategia di gestione a livelli della finestra di contesto

#### 4. I punti chiave della pratica dell'ingegneria del contesto

L'ingegneria del contesto non è una configurazione da fare una volta sola, ma un processo di ottimizzazione continua. Ecco alcuni punti chiave verificati più e più volte nella pratica:

1. Tieni i file di memoria aggiornati insieme all'evoluzione del progetto. Quando introduci una nuova tecnologia o cambi l'architettura, aggiorna subito il file di memoria invece di spiegarlo al volo nella conversazione.
2. Usa bene i riferimenti @ invece di incollare testi interi. La maggior parte degli strumenti di programmazione AI supporta la sintassi @file o @folder, che inietta in background il contenuto del file nel contesto dell'AI: è più efficiente dell'incollaggio manuale e non inquina la conversazione.
3. Le conversazioni devono essere brevi e incisive. Una conversazione gestisce un solo compito o una sola funzionalità. Finito? Apri una nuova conversazione per il successivo. Le conversazioni lunghe non solo consumano la finestra di contesto, ma fanno anche “distrarre” l'AI.
4. Fai “vedere” all'AI i risultati invece di “descriverli”. Quando incontri un bug, cita direttamente il log degli errori con @ invece di raccontarlo a parole tue con un vago “c'è tipo un errore”. Per l'AI è molto più efficace vedere le informazioni originali che la tua parafrasi.
5. Pulizia e archiviazione periodiche. Le conversazioni concluse e i file temporanei occupano spazio di lavoro. Pulire di tanto in tanto ciò che non serve e tenere ordinata la directory del progetto aiuta anche l'AI a capire la struttura del progetto in modo più efficiente.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mettiti alla prova: scrivi un file di memoria di 70 righe per il tuo progetto

{class="mt-1"}
Scegli un progetto che stai facendo (o che intendi fare) e scrivi un CLAUDE.md: panoramica del progetto (2-3 frasi), stack tecnologico (elencalo), regole del codice (3-5 punti), struttura delle directory (disegnala ad albero), convenzioni di sviluppo (2-3 punti). Resta entro 70 righe: quando avrai finito scoprirai che anche la tua comprensione del progetto è diventata molto più chiara.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riepilogo del capitolo

- La memoria dell'AI è “a breve termine”: a ogni nuova conversazione la sua conoscenza del progetto riparte da zero
- I file di memoria del progetto (CLAUDE.md e simili) sono la “memoria a lungo termine” dell'AI, caricati automaticamente a ogni conversazione
- Un buon file di memoria = panoramica + stack + regole + directory + convenzioni: bastano 70 righe
- SDD, sviluppo guidato dalle specifiche: prima la specifica poi il codice; la specifica è la “fonte unica di verità”, più stabile del codice
- Il contesto si gestisce su quattro livelli: memoria del progetto → riferimenti @file → cronologia della conversazione → istruzioni immediate
- Cinque punti chiave pratici: aggiornamenti sincronizzati, riferimenti @, conversazioni brevi, fornire le informazioni originali, pulizia periodica
:::
