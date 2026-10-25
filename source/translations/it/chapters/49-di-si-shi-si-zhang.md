---
id: di-si-shi-si-zhang
num: 44
part: ai-biancheng-pian
nav: Capitolo 44: Pratica dal 0 all'1 — Il percorso completo di un progetto
toc: default
kind: chapter
---

### Capitolo 44: Pratica dallo 0 all'1 — l'intero flusso di un progetto completo

{class="chapter-intro mb-4"}
La teoria è finita, ora si passa alle mani. Questo capitolo non è un tutorial da «copia e incolla», ma un metodo operativo su «come pensare, come chiedere, come verificare». Useremo tre progetti di difficoltà diversa per mostrare l'intero processo di ragionamento che porta dai requisiti al prodotto finito. Qualunque strumento tu usi, questo flusso vale lo stesso.

#### 1. Progetto 1: un sito di strumenti personali minimalista (livello base)

##### 1. Pensare ai requisiti

Obiettivo: creare una pagina web di strumenti personali che mostri l'ingresso di 3-4 piccoli strumenti utili. È un progetto di solo frontend, senza backend né database. L'importante non è quanto sono complicati gli strumenti, ma vivere l'intero percorso «dai requisiti al prodotto finito».

Seguendo i cinque elementi dei requisiti: Who — uso personale. What — una pagina web che mostra l'ingresso degli strumenti. Why — raccogliere gli strumenti di uso quotidiano in un'unica pagina per averli comodi da raggiungere. How — un singolo file HTML+CSS+JS, senza framework. Constraint — completare entro 30 minuti, senza deploy.

##### 2. Dare le istruzioni

Secondo il principio Think Before Coding, la tua istruzione deve contenere informazioni sufficienti perché l'AI capisca l'obiettivo, ma non serve specificare ogni dettaglio realizzativo:

::: div .code-block
:::inline div .code-head
<span>Istruzioni per l'IA</span><span class="dots">···</span>
:::

```
Crea una pagina web con una cassetta degli attrezzi personale, requisiti:
1. HTML in un solo file (CSS e JS inline), senza framework
2. Tema scuro, stile minimale moderno
3. Mostra 4 card di strumenti:
   - Riassuntore di testo
   - Contaparole
   - Selettore colori
   - Generatore di QR code
4. Ogni card ha icona, titolo e breve descrizione
5. Le card hanno un'animazione al passaggio del mouse
6. Layout responsive, utilizzabile su telefono
7. Una barra del titolo in alto
Fornisci direttamente il file HTML completo.
```
:::

##### 3. Accettazione e iterazione

Quando l'AI consegna il codice, fai l'accettazione con la verifica a tre livelli dell'iterazione. Primo livello, verifica funzionale: il file si apre nel browser? Le 4 card appaiono tutte? L'animazione al passaggio del mouse funziona? Secondo livello, verifica dei casi limite: il layout regge alla dimensione dello schermo di un telefono? Con la finestra molto stretta le card vanno a capo? Terzo livello, verifica dell'architettura: il codice è leggibile? Il CSS è tutto in linea dentro un solo tag style? C'è ridondanza evidente?

Se vuoi realizzare anche la funzione di qualche card (e non solo l'ingresso), puoi aggiungerla a poco a poco: a ogni giro aggiungi la funzione di uno strumento, la verifichi e poi passi al successivo. È proprio l'applicazione pratica della strategia dei «piccoli passi veloci».

#### 2. Progetto 2: un sistema di contabilità full stack (livello intermedio)

##### 1. Pensare ai requisiti e scrivere il PRD

Obiettivo: un'applicazione di contabilità full stack, con frontend, backend e database. Questo progetto è molto più complesso del primo e richiede i metodi di ingegneria dei requisiti del Capitolo 40.

Prima scrivi il PRD. Seguendo il modello della terza sezione del Capitolo 40, redigi panoramica del progetto, elenco delle funzionalità, soluzione tecnica, modello dei dati e piano di sviluppo. Nella scelta della soluzione tecnica tieni conto del principio Simplicity First: per il frontend React, ma senza introdurre una gestione di stato complessa come Redux; per il backend Node.js, ma senza microservizi; come database SQLite invece di PostgreSQL (nella fase di sviluppo).

Il piano di sviluppo si spezza in 5 passi: Step 1, scheletro delle API di backend (server Express + SQLite + interfacce CRUD); Step 2, pagine di base del frontend (elenco dei movimenti + modulo di inserimento); Step 3, aggancio frontend-backend (chiamate API + visualizzazione dei dati); Step 4, funzioni di categorie e filtri; Step 5, riepilogo mensile e semplici grafici. A ogni passo completato hai qualcosa «che si può usare».

##### 2. Preparare il file di memoria del progetto

Prima di iniziare a scrivere codice, crea il file di memoria del progetto. È la pratica centrale dell'ingegneria del contesto: fare in modo che l'AI conosca il contesto del progetto all'inizio di ogni dialogo.

::: div .code-block
:::inline div .code-head
<span>CLAUDE.md</span><span class="dots">···</span>
:::

```
# Progetto: app di finanza full-stack
## Panoramica
App di finanza personale con registrazioni entrate/uscite, categorie e totali mensili.
## Stack tecnologico
- Frontend: React + TypeScript + Vite
- Backend: Node.js + Express + TypeScript
- Database: SQLite (tramite better-sqlite3)
- Definizioni di tipo condivise fra frontend e backend
## Convenzioni API
- Percorso base: /api
- Formato di risposta:{ success: boolean, data: any, error: string }
- Stile RESTful
## Modello dati
Record { id, amount, type, category, note, date }
## Convenzioni del codice
- Modalità strict di TypeScript
- Indentazione di 2 spazi
- Le funzioni hanno commenti JSDoc
- Commenti e messaggi di commit in italiano
```
:::

##### 3. Realizzare passo dopo passo

Seguendo il piano di sviluppo, completa ogni passo con un dialogo separato. Ecco un esempio di istruzione per il primo passo:

::: div .code-block
:::inline div .code-head
<span>Istruzioni per l'IA (Step 1)</span><span class="dots">···</span>
:::

```
Mi serve uno scheletro di API backend.
Requisiti:
1. Server Express, porta 3001
2. Database SQLite, tabella records
3. Campi della tabella records:
   id (TEXT PRIMARY KEY)
   amount (REAL)
   type (TEXT: 'income'|'expense')
   category (TEXT)
   note (TEXT)
   date (TEXT: YYYY-MM-DD)
4. Endpoint CRUD:
   GET /api/records - recupera tutte le voci
   POST /api/records - aggiunge una voce
   PUT /api/records/:id - aggiorna una voce
   DELETE /api/records/:id - elimina una voce
5. Middleware di gestione errori
Fornisci la struttura completa del codice backend.
```
:::

Nota i tratti di questa istruzione: descrive solo il passo in corso (lo scheletro del backend), senza intrecciare richieste sul frontend; elenca esplicitamente campi e interfacce (dando all'AI vincoli a sufficienza), ma lascia all'AI i dettagli realizzativi; segue il principio Goal-Driven Execution — dice «cosa fare» e non «come farlo».

Appena l'AI consegna il codice, verifica subito: avvia il server e prova con curl o Postman che ogni interfaccia risponda correttamente. Se tutto torna, apri un nuovo dialogo per lo Step 2 (pagine di base del frontend). A ogni passo si ripete il ciclo «istruzione-verifica-nuovo dialogo».

#### 3. Progetto 3: un'applicazione potenziata dall'AI (livello avanzato)

##### 1. Immaginare il progetto

Obiettivo: un'applicazione collegata alle API dei grandi modelli — per esempio un «assistente di studio AI»: l'utente inserisce il materiale da studiare e l'AI genera il riassunto, collega i concetti, consiglia risorse per lo studio. La particolarità del progetto è questa: la tua applicazione in prima persona chiama l'AI, e quindi devi affrontare problemi nuovi come le chiamate API, il prompt engineering e la gestione degli errori.

La lezione più importante che questo progetto ti insegna è: quando «usi l'AI per scrivere codice che chiama l'AI», devi fare particolare attenzione al prompt engineering. Anche i prompt che la tua applicazione usa per chiamare le API dei grandi modelli devono rispettare i principi discussi in questa guida: chiarezza, essenzialità, orientamento all'obiettivo.

##### 2. I punti tecnici chiave

Questo progetto tocca alcuni punti tecnici che non hai incontrato nei due progetti precedenti:

- Gestione delle chiavi API: le chiavi non vanno mai scritte direttamente nel codice, si gestiscono con le variabili d'ambiente;
- Gestione delle risposte in streaming: le risposte dei grandi modelli di solito arrivano in streaming e vanno mostrate parola dopo parola;
- Controllo del consumo di token: i grandi modelli fatturano a token, quindi il consumo va controllato a livello di applicazione;
- Gestione dei template di prompt: funzioni diverse usano template di prompt diversi, e vanno gestiti in modo strutturato.

Tutti questi punti tecnici puoi farli realizzare dall'AI, ma devi capirne il «perché» — perché le chiavi non si scrivono nel codice? Perché servono le risposte in streaming? Perché il consumo di token va controllato? Solo capendo il «perché» potrai giudicare se la soluzione proposta dall'AI è sensata.

#### 4. La checklist operativa universale

A prescindere dalle dimensioni del progetto, ecco una checklist universale del flusso operativo per programmare con l'AI. Ogni volta che inizi un nuovo progetto, ripassala per assicurarti di non tralasciare passi fondamentali.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Fase</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cosa fare</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Principio di riferimento</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1. Pensare ai requisiti</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ripassa i cinque elementi dei requisiti e definisci bene cosa vuoi realizzare</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Think Before Coding</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2. Scomporre i requisiti</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Spezza la grande richiesta in piccoli passi verificabili indipendentemente</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Simplicity First</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3. Scrivere il PRD</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Riordina tutto in un documento strutturato, da tenere come riferimento</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Goal-Driven</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">4. Preparare il file di memoria</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Crea il file CLAUDE.md o un file equivalente</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Harness Engineering</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">5. Realizzare passo dopo passo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Un dialogo per passo: istruzione-verifica-passo successivo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Surgical Changes</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6. Test e verifica</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Appena concluso ogni passo, testa subito la correttezza delle funzioni</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">7. Revisione del codice</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Controlla coerenza dell'architettura, sicurezza e manutenibilità</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8. Iterare e ottimizzare</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Migliora iterando in base ai risultati di test e revisione</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Checklist operativa universale per la programmazione AI

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Metti in pratica: completa il «Progetto 1» questa settimana

{class="mt-1"}
Prendi il «sito di strumenti personali» della prima sezione del Capitolo 44 come tuo primo compito di programmazione con l'AI: dedica 5 minuti ai cinque elementi, invia le istruzioni all'AI (va bene qualunque strumento) e fai l'accettazione con la verifica a tre livelli. Completalo entro 30 minuti: sarà nata la tua prima opera di programmazione con l'AI. Quando hai finito, conservala con cura: è il ricordo del tuo passaggio da «lettore» a «praticante».
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riepilogo del capitolo

- Progetto 1 (base): sito di strumenti in puro frontend — per percorrere l'intero flusso, completabile in 30 minuti
- Progetto 2 (intermedio): sistema di contabilità full stack — PRD + file di memoria + realizzazione in 5 passi, ogni passo «utilizzabile»
- Progetto 3 (avanzato): assistente di studio AI — usare l'AI per scrivere codice che chiama l'AI, con attenzione al prompt engineering
- Il flusso universale in 8 passi: requisiti → scomposizione → PRD → file di memoria → realizzazione passo a passo → test → revisione → iterazione
- Ogni passo segue il ciclo «istruzione-verifica-nuovo dialogo»
:::
