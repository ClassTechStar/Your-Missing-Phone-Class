---
id: di-si-shi-liu-zhang
num: 46
part: ai-biancheng-pian
nav: Capitolo 46: Il percorso di crescita — Da utente ad architetto
toc: default
kind: chapter
---

### Capitolo 46: La strada per i livelli avanzati — dall'utente all'architetto

{class="chapter-intro mb-4"}
Quando hai padroneggiato la metodologia dei Capitoli da 37 a 44 e sai sviluppare progetti con l'AI con disinvoltura, qual è il passo successivo? Questo capitolo esplora il percorso che porta da «utente di strumenti AI» a «architetto di sistemi AI». A questo stadio l'attenzione non è più «come far scrivere buon codice all'AI», ma «come integrare l'AI al meglio nell'intero flusso di sviluppo».

#### 1. Il protocollo MCP e l'estensione degli strumenti

Il MCP (Model Context Protocol) è un protocollo aperto nato nel 2025 e via via diffuso nel 2026, che definisce lo standard di comunicazione tra i modelli AI e gli strumenti esterni. In soldoni, il MCP permette all'AI di «usare gli strumenti»: non solo generare codice, ma eseguire comandi, interrogare database, chiamare API, muoversi nel file system.

Prima del MCP ogni strumento AI aveva il proprio modo di integrare gli strumenti, incompatibile con gli altri. L'arrivo del MCP significa questo: uno strumento conforme allo standard MCP può essere usato da qualunque strumento AI che lo supporti. I costi di integrazione crollano, e il confine delle capacità dell'AI si allarga dal «generare testo» all'«eseguire azioni».

Per l'utente avanzato il senso del MCP è questo: puoi costruire capacità strumentali su misura per l'AI. Per esempio, se il tuo team ha un sistema di deploy interno, puoi scrivere uno strumento MCP perché l'AI chiami direttamente il sistema di deploy, senza che qualcuno debba passare manualmente al terminale. Questa capacità dell'«AI che chiama gli strumenti» è l'infrastruttura dell'Agentic Engineering.

#### 2. Workflow personalizzati e Skills

Quando esegui più e più volte alcuni flussi fissi di programmazione AI, puoi consolidarli in «workflow personalizzati» o «Skills». Per esempio, il tuo team può avere un processo standard di revisione del codice — prima la sicurezza, poi le prestazioni, poi la manutenibilità. Puoi scrivere questo processo come una Skill, così l'AI lo segue automaticamente a ogni revisione del codice.

Il valore centrale dei workflow personalizzati è la «coerenza»: garantisce che ogni esecuzione segua gli stessi standard, senza scostamenti dovuti alla lunghezza del dialogo o al contesto. Per la collaborazione in team è fondamentale: se ogni membro usa gli stessi workflow, lo stile del codice e gli standard di qualità tendono a convergere.

I metodi per costruire workflow personalizzati variano da strumento a strumento. Cursor supporta Rules e Custom Instructions, Claude Code i comandi personalizzati, Replit Runme. Ma l'idea di fondo è una sola: «codificare» le tue buone pratiche in template di istruzioni che l'AI possa eseguire.

#### 3. La collaborazione multi-Agent

Entro il 2026 la collaborazione multi-Agent è diventata un tema caldo. L'idea centrale: non usare un solo AI per portare a termine il compito, ma mettere insieme più AI con ruoli diversi che collaborano. Per esempio: un AI scrive il codice, un AI scrive i test, un AI revisiona il codice — ognuno fa il suo mestiere e si controllano a vicenda.

I vantaggi della collaborazione multi-Agent sono la «divisione del lavoro» e la «verifica incrociata»: ogni Agent si concentra sul suo dominio e la qualità dell'output sale; i controlli incrociati tra Agent fanno emergere problemi che uno solo trascurerebbe. Ma anche gli svantaggi sono evidenti: coordinamento costoso, overhead di comunicazione notevole, debugging più complesso.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consiglio: il «multi-Agent» si può giocare anche da soli

{class="mt-1"}
Per lo sviluppatore singolo non serve montare un complicato sistema multi-Agent — puoi «recitare» tu ruoli diversi per simulare la collaborazione multi-Agent. Per esempio: prima, con un dialogo, fai scrivere all'AI il codice della funzionalità; poi apri un nuovo dialogo (dandogli il contesto di CLAUDE.md) e chiedi all'AI di «revisionare questo codice come revisore»; infine apri un altro dialogo e fai «correggere il codice in base alle osservazioni della revisione». Questo metodo del «una persona, più ruoli» regala gran parte dei benefici della collaborazione multi-Agent, senza infrastrutture complesse.
:::

#### 4. Il percorso di apprendimento continuo

La programmazione AI è un campo che cambia a raffica. Le buone pratiche di oggi domani potrebbero già essere da aggiornare. Ecco qualche consiglio per continuare a imparare:

Primo: vai alle fonti primarie, non alle letture di seconda mano. I tweet originali e il CLAUDE.md di Andrej Karpathy, la documentazione ufficiale di Anthropic e OpenAI, i changelog dei vari strumenti — sono informazioni di prima mano. Gli articoli e i tutorial della community sono interpretazioni e riassunti di quelle informazioni: hanno valore ma possono deformarle. Prenditi l'abitudine di leggere il materiale originale.

Secondo: impara dalla pratica. Non «prima impari, poi fai», ma «fai e impara insieme». Ogni volta che incontri un tipo di problema nuovo (per esempio la prima volta che gestisci l'upload di file o colleghi un'API di terze parti), prendilo come occasione per studiare quel tema. L'efficienza dell'apprendimento nella pratica è molto più alta di quella della teoria studiata fuori contesto.

Terzo: mantieni la sensibilità verso gli strumenti, senza rincorrere ogni novità. Ogni uno-due mesi, dedica mezza giornata a conoscere strumenti e tendenze recenti — ma non cambiare a ogni nuovo strumento che esce. Il criterio è: il nuovo strumento migliora in modo significativo uno dei tuoi colli di bottiglia? Se no, la combinazione attuale è più che sufficiente.

Quarto: costruisci una base di conoscenze personale. Annota ogni dialogo con cui hai risolto un problema complesso, la lezione di ogni caduta, il metodo che ha funzionato. Non serve pubblicarlo — è il tuo «quaderno di metodologia» privato. Col tempo diventerà il tuo bene più prezioso.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Metti in pratica: apri un «quaderno dei grattacapi»

{class="mt-1"}
Crea oggi stesso un documento (va bene un'app di note o un file .md) e scrivi le tre cose che, fino a oggi, vorresti ricordare di più sulla programmazione con l'AI — anche solo «prima pensare bene, poi chiedere». D'ora in poi, ogni volta che cadi in una trappola o impari un trucco nuovo, aggiungi una riga. Fra sei mesi, rileggendolo, ringrazierai te stesso di oggi.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riepilogo del capitolo

- Il MCP è lo standard di comunicazione tra AI e strumenti: permette all'AI di eseguire comandi, interrogare database e chiamare API
- Il valore centrale dei workflow e delle Skills personalizzate è la «coerenza»: trasformare le buone pratiche in template di istruzioni
- Multi-Agent = divisione del lavoro + verifica incrociata; lo sviluppatore singolo può simularla con il «una persona, più ruoli»
- Le quattro mosse dell'apprendimento continuo: leggere le fonti primarie, imparare facendo, non rincorrere le novità, costruire la propria base di conoscenze
:::
