---
id: di-si-shi-zhang
num: 40
part: ai-biancheng-pian
nav: Capitolo 40: Ingegneria dei requisiti — Trasformare le idee in istruzioni per l'AI
toc: default
kind: chapter
---

### Capitolo 40: Ingegneria dei requisiti — trasformare le idee in istruzioni eseguibili dall'AI

{class="chapter-intro mb-4"}
Se l'ingegneria del contesto risolve il problema di “far capire all'AI il contesto”, l'ingegneria dei requisiti risolve quello di “far sapere all'AI cosa deve fare esattamente questa volta”. È la fase della programmazione AI che mostra meglio le differenze tra le persone: con gli stessi strumenti e gli stessi modelli, c'è chi realizza progetti sorprendenti e chi solo giocattoli mediocri. La differenza spesso non sta nelle capacità tecniche, ma nella capacità di esprimere i requisiti.

#### 1. Da un'idea vaga a requisiti strutturati

Ogni progetto nasce da un'idea vaga: “voglio fare un'app per tenere le spese”, “voglio un sito personale”, “voglio uno strumento per le cose da fare”. Le idee in sé non sono un problema, ma se le lanci direttamente all'AI la qualità del risultato dipende interamente dalla fortuna. L'obiettivo dell'ingegneria dei requisiti è trasformare quell'idea vaga in un requisito strutturato che l'AI possa eseguire con precisione.

La buona notizia è che un requisito strutturato non richiede un PRD di decine di pagine. Ti basta rispondere a cinque domande, che chiamiamo i “cinque elementi del requisito”:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Elemento</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Domanda</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Esempio: app per le spese</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Per chi è?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Uso personale, per registrare entrate e uscite quotidiane</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cosa fa?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Un'app che registra ogni voce di entrata e uscita, riepiloga per mese e offre grafici</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perché farla?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Voglio capire la struttura delle mie spese ed individuare le uscite superflue</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Come, in grandi linee?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Frontend in React, dati salvati in locale nel browser, per ora niente backend né login</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Quali vincoli?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sviluppo individuale, da completare in 2 settimane, senza necessità di pubblicazione online</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
I cinque elementi del requisito con esempi

Questi cinque elementi non vanno scritti in un documento formale: basta passarli velocemente in mente. La chiave è abituarsi a “pensare bene prima di parlare”. Scoprirai che quando riesci a rispondere con chiarezza a queste cinque domande, la descrizione dei tuoi requisiti diventa naturalmente strutturata.

#### 2. L'arte della scomposizione dei requisiti a livelli

Per i progetti più grandi non basta una sola descrizione del requisito. Devi scomporre il grande requisito in sotto-requisiti piccoli e verificabili indipendentemente. Questo processo si chiama “scomposizione dei requisiti” e il principio fondamentale è: ogni sotto-requisito deve poter essere completato, verificato e consegnato in modo indipendente.

Prendendo come esempio “fare un'app personale per le spese”, una scomposizione ragionevole è:

1. Implementare la funzione base di registrazione di entrate e uscite (aggiungere, visualizzare, eliminare le voci);
2. Aggiungere le categorie (etichettare ogni voce con pasti, trasporti e così via);
3. Implementare il riepilogo mensile (statistiche di entrate e uscite mese per mese);
4. Aggiungere la visualizzazione dei dati (grafici della struttura delle spese).

Ogni passaggio è un incremento funzionale che può essere eseguito e verificato da solo.

:::inline div .quote-line
La regola d'oro della scomposizione dei requisiti: dopo ogni passo il progetto deve restare una "cosa che funziona", per quanto rozza. Non lasciare mai il progetto in uno stato in cui "tutto è fatto a metà ma niente funziona".
:::

Questa scomposizione ha due vantaggi. Primo, ti fa sempre vedere i progressi: a ogni passaggio completato la tua app guadagna una funzione, e questo feedback positivo è vitale per i progetti di lunga durata (della soddisfazione tutti abbiamo bisogno). Secondo, tiene ogni compito dell'AI abbastanza piccolo, riducendo il rischio di “fraintendimento da parte dell'AI”: più il compito è piccolo, più l'AI lo capisce con precisione e migliore è la qualità del risultato.

#### 3. Modello di scrittura del PRD e pratica

Per i progetti più grandi (per esempio un'applicazione full-stack con frontend, backend e più moduli funzionali), i soli cinque elementi del requisito potrebbero non bastare. In quel caso devi scrivere un documento dei requisiti di progetto (PRD) più formale. Un punto su cui ci si sbaglia spesso: il PRD non è scritto per l'AI — è scritto per te stesso, per mettere in ordine le idee; solo dopo potrai dare all'AI istruzioni più precise.

Un buon PRD non deve essere lungo, ma dovrebbe contenere sei parti: panoramica del progetto (cosa fa, detto in un paragrafo), elenco delle funzioni (cos'è ogni funzionalità), soluzione tecnica (quale stack e architettura di massima), modello dei dati (le strutture dati principali), descrizione dell'interfaccia (come sono le pagine principali) e piano di sviluppo (in quanti passaggi si completa).

::: div .code-block
:::inline div .code-head
<span>PRD.md</span><span class="dots">···</span>
:::

```
# PRD app di finanza personale
## Panoramica del progetto
Un'app leggera di finanza personale con registrazione entrate/uscite, categorie, totali mensili e visualizzazione dei dati.
## Elenco funzionalità
1. Registrare entrate/uscite: importo, tipo (entrata/uscita), categoria, nota, data
2. Gestione categorie: preset per pasti, trasporti, shopping, svago, altro
3. Riepilogo mensile: entrate, uscite e saldo totali per mese
4. Visualizzazione delle spese: grafico a torta delle quote per categoria
5. Esportazione dati: esporta in CSV
## Soluzione tecnica
- Frontend: React + TypeScript + Tailwind CSS
- Archiviazione dati: localStorage (nessun backend)
- Grafici: Chart.js
- Build: Vite
## Modello dati
Record {
  id: string
  amount: number
  type: 'income' | 'expense'
  category: string
  note: string
  date: string  // YYYY-MM-DD
}
## Piano di sviluppo
Step 1: funzioni base di registrazione (CRUD)
Step 2: gestione categorie
Step 3: riepilogo mensile
Step 4: visualizzazione dati
Step 5: esportazione dati
```
:::

Nota lo stile di scrittura di questo PRD: elenchi concisi e formati strutturati, non lunghi discorsi. Ogni funzionalità ha una definizione chiara e il modello dei dati è descritto con tipi semplici. Un PRD in questo stile non solo lo leggi con chiarezza tu, ma quando lo dai all'AI anche l'AI capisce con precisione ogni punto del requisito.

#### 4. Nella pratica: deduzione completa dall'idea al piano

Restare sulla carta non è divertente: facciamo un esempio completo per ripercorrere tutto il processo dell'ingegneria dei requisiti. Supponiamo che la tua idea sia: “voglio fare un tracker degli studi che tenga traccia di cosa imparo ogni giorno”.

Primo passaggio: passiamo in rassegna i cinque elementi del requisito.

- Who: uso personale.
- What: uno strumento che registra cosa studi ogni giorno, monitora il tempo di studio e permette di rivedere i progressi.
- Why: voglio coltivare l'abitudine allo studio continuo e vedere le mie conquiste accumularsi.
- How: prima faccio una versione web, con i dati salvati in locale nel browser.
- Constraint: sviluppo da zero, funzioni principali completate entro 1 settimana.

Secondo passaggio: scomponiamo i requisiti.

1. Step 1: implementare la funzione “registra voce di studio” (data, contenuto, durata);
2. Step 2: aggiungere le “statistiche del tempo di studio” (oggi, totale settimanale);
3. Step 3: implementare la vista “calendario dello studio” (mostrata come il grafico dei contributi di GitHub);
4. Step 4: aggiungere la funzione “riassunto dello studio” (mostra a caso le registrazioni di un giorno passato, per ripassare).

Terzo passaggio: scrivi un PRD breve. Non serve lungo — la scomposizione di sopra costituisce già il corpo principale del PRD. Mettilo in ordine in un file .md, nella cartella radice del progetto, come riferimento comune per te e per l'AI.

Quarto passaggio: inizia a sviluppare il primo step. L'istruzione da dare all'AI può essere:

::: div .code-block
:::inline div .code-head
<span>Istruzioni per l'IA</span><span class="dots">···</span>
:::

```
Mi serve la prima funzione di un tracker dell'apprendimento — registrare le voci di studio.
L'utente può aggiungere un record con data, cosa studiato e durata in minuti.
I dati sono salvati in localStorage.
Il frontend usa React + TypeScript.
Fornisci un'implementazione completa.
```
:::

Nota le caratteristiche di questa istruzione: descrive solo l'obiettivo del passaggio corrente (la funzione di registrazione), senza mescolare altre funzioni; esplicita i vincoli tecnici (React, TypeScript, localStorage); fornisce informazioni sufficienti perché l'AI sappia “cosa fare” e “come muoversi”, lasciando però all'AI le scelte di implementazione. È questa un'istruzione di programmazione AI di alta qualità, elaborata con l'ingegneria dei requisiti.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mettiti alla prova: scrivi la scheda dei cinque elementi per il tuo “progetto del cuore”

{class="mt-1"}
Scegli un piccolo progetto che rimugini da tempo e dedica 5 minuti a riempire una scheda: Who / What / Why / How / Constraint, una frase ciascuno. Poi scomponilo in 3-5 passaggi in cui “ogni fase è già utilizzabile”. Scoprirai che, una volta scritta su carta, l'idea passa da “sogno a occhi aperti” a “lista di cose da fare”.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riepilogo del capitolo

- I cinque elementi del requisito: Who / What / Why / How / Constraint — pensa bene prima di parlare
- Regola d'oro della scomposizione dei requisiti: a ogni passaggio completato il progetto è una “cosa utilizzabile”
- Il PRD è scritto per te stesso: panoramica, elenco funzioni, soluzione tecnica, modello dati, interfaccia, piano
- Una buona istruzione = descrivere solo il passaggio corrente + vincoli chiari + dire “cosa fare” senza dire “come farlo”
- Modello di deduzione completa: cinque elementi → scomposizione → PRD → istruzione, in quattro passi
:::
