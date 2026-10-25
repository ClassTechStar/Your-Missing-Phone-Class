---
id: di-wu-shi-qi-zhang
num: 57
part: an-zhuo-kai-fa-pian
nav: Capitolo 57: Il percorso di crescita — Permessi, notifiche e architettura moderna
toc: default
kind: chapter
---

### Capitolo 57: La strada del livello successivo — permessi, notifiche e architettura moderna

{class="chapter-intro mb-4"}
Saper costruire un'app è solo l'inizio. Questo capitolo affronta gli ostacoli che portano da «saper fare» a «fare bene»: come chiedere i permessi con eleganza, come inviare notifiche senza dare fastidio, come alzare di un livello l'architettura e — nel 2026 — come scrivere codice Android in coppia con l'AI. Ogni punto ti capiterà subito fra le mani in un progetto vero.

#### 1. Permessi a runtime: prima bussi, poi entri

Fotocamera, posizione, contatti, notifiche… queste «zone sensibili» Android vuole che l'app le chieda all'utente a runtime (da Android 6 in poi). La regola: prima dichiari (nel Manifest), poi richiedi (nel codice) e, se l'utente rifiuta, degradi con eleganza. In Compose la via più tranquilla è rememberPermissionState della libreria ufficiale Accompanist:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Permessi runtime (versione Compose)</span><span class="dots">···</span>
:::

```
// Prima dichiaralo nel Manifest:
// &lt;uses-permission android:name="android.permission.CAMERA" /&gt;

@Composable
fun CameraButton() {
    val permission = rememberPermissionState(
        permission = android.Manifest.permission.CAMERA
    )
    Button(onClick = {
        when {
            permission.status.isGranted -&gt; openCamera()
            permission.status.shouldShowRationale -&gt; showExplainDialog()
            else -&gt; permission.launchPermissionRequest()
        }
    }) { Text("Scatta") }
}
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attenzione: e se il permesso viene rifiutato per sempre?

{class="mt-1"}
Dopo che l'utente ha spuntato «non chiedere più», launchPermissionRequest non apre più il popup. A quel punto guida l'utente ad attivarlo a mano nelle impostazioni di sistema (con un Intent che apre la pagina delle impostazioni dell'app) e spiega nell'interfaccia «a cosa serve questo permesso». Con un atteggiamento gentile la voglia di concedere il permesso cresce parecchio: il testo con cui chiedi i permessi merita di essere scritto sul serio.
:::

#### 2. Notifiche: dire cose utili al momento giusto

Le notifiche sono il canale con cui l'app raggiunge l'utente, e anche la funzione che gli utenti mettono più volentieri al bando. Tre regole ferree: manda solo cose utili, lascia all'utente la possibilità di spegnerle, non disturbare a notte fonda. Uso di base:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Inviare una notifica</span><span class="dots">···</span>
:::

```
// Su Android 13+ devi prima richiedere il permesso POST_NOTIFICATIONS (vedi la sezione precedente)

// 1. Crea il canale di notifica (obbligatorio da Android 8+)
val channel = NotificationChannel(
    "reminder", "Promemoria", NotificationManager.IMPORTANCE_DEFAULT
)
val manager = getSystemService(NotificationManager::class.java)
manager.createNotificationChannel(channel)

// 2. Invia la notifica
val notification = NotificationCompat.Builder(this, "reminder")
    .setSmallIcon(R.drawable.ic_notification)
    .setContentTitle("Promemoria spese")
    .setContentText("Oggi non hai ancora registrato spese")
    .setPriority(NotificationCompat.PRIORITY_DEFAULT)
    .build()
if (ActivityCompat.checkSelfPermission(this,
        Manifest.permission.POST_NOTIFICATIONS) == PackageManager.PERMISSION_GRANTED
) {
    manager.notify(1, notification)
}
```
:::

Le attività programmate (per esempio «ricorda di segnare le spese ogni giorno alle 20:00») si affidano a WorkManager: è il «maggiordomo di pianificazione in background» raccomandato ufficialmente, garantisce che i compiti partano al momento giusto e ti libera dalle preoccupazioni sull'ottimizzazione della batteria. Per esigenze tipo sveglia non sbagli.

#### 3. Architettura avanzata: dependency injection e modularizzazione

Quando il progetto cresce, si presentano due «dolci seccature»:

- Creazione di oggetti in disordine: ogni schermata si costruisce da sola database e API — con Hilt (framework di dependency injection) si amministra tutto in un posto solo: «chiunque chieda qualcosa, qualcuno glielo porge»;
- Codice che si accumula a montagna: un progetto a modulo unico si modifica sempre più lentamente — dividilo in più moduli (app / core / feature-xxx), con ogni funzione sviluppata e testata per conto suo.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consiglio: non progettare troppo

{class="mt-1"}
Hilt e la modularizzazione sono ottimi strumenti, ma in un progetto in solitaria non avere fretta. Per il registro delle spese bastano e avanzano un modulo unico con dipendenze create a mano. Introducili quando il codice supera le decine di migliaia di righe, la compilazione comincia a rallentare o ci si mette più persone. Gli strumenti servono all'obiettivo, non al fare sfoggio — è anche il principio «semplicità sopra ogni cosa» del nostro libro sulla programmazione con l'AI.
:::

#### 4. La novità del 2026: sviluppare Android con l'assistenza dell'AI

Nel 2026 l'AI è ormai incastonata nel flusso di lavoro Android. Se vuoi accelerare, questa combinazione è ben rodata:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Fase</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Come aiuta l'AI</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Il tuo compito</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Scrivere codice</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Completamento e generazione con Gemini integrato in Android Studio o con plugin AI di terze parti</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Descrivere bene i requisiti, revisionare i risultati</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cercare informazioni</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Consegnare all'AI documentazione ufficiale e messaggi di errore da interpretare</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Verificare le conclusioni chiave sulla documentazione ufficiale</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Scrivere test</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fare generare all'AI i casi di test nelle tre categorie «normale/limite/anomalo»</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Confermare che i casi rispettino il senso del dominio</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Correggere i bug</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Incollare stacktrace e codice correlato: l'AI localizza e ripara</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Capire le modifiche e verificare facendo girare i test</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
I quattro scenari dello sviluppo Android assistito dall'AI

La metodologia concreta — come dare istruzioni all'AI, come accettare i risultati, come schivare le trappole — occupa ben 11 capitoli nella parte 7 di questo libro, «Programmazione AI in pratica» (capitoli 37-47): è fortemente consigliato leggerli in parallelo. La sintassi Android la copre questa parte, i segreti della collaborazione con l'AI la parte 7.

#### 5. Ottimizzazione delle prestazioni di Compose e strumenti di debug

Con Compose si scrive volentieri, ma troppa «ricomposizione» può far inciampare. Tre trucchetti pratici:

- Parametri stabili: aggiungi @Immutable alle data class o usa derivedStateOf, per evitare che variazioni di stato irrilevanti scatenino ricomposizioni su larga scala;
- Ricorda di usare la key: items(list, key = { it.id }) fa sì che aggiunte e cancellazioni tocchino solo le voci interessate — senza key, cancellare una voce può ridisegnare l'intera lista;
- La modalità Compose del Layout Inspector: mostra in tempo reale quante volte viene ricomposto ogni Composable; chi si ricompiona troppo si vede a colpo d'occhio e ottimizzerai puntando sui punti caldi.

In più, apri i report del compilatore Compose (Metrics): generano un resoconto di «quali componenti non sono stabili» — sulla via del livello avanzato, i dati sono sempre più affidabili delle sensazioni.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mani in pasta: aggiungi il «tris» al registro delle spese

{class="mt-1"}
① Aggiungi al registro delle spese il promemoria «segnare le spese ogni giorno alle 20:00» (WorkManager + canale di notifica + permesso notifiche di Android 13); ② passa la creazione di database e API all'iniezione con Hilt; ③ prova a usare uno strumento AI per realizzare più in fretta la funzione «filtro mensile», poi controlla il risultato col metodo di collaudo a tre livelli. Fatto il tris, il tuo progetto avrà un aspetto decisamente professionale.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riassunto del capitolo

- Permessi sensibili: dichiarazione nel Manifest + richiesta a runtime + guida elegante dopo il rifiuto
- Le tre regole delle notifiche: solo cose utili, spegnibili, nessun fastidio; canale + permesso, non possono mancare
- Le attività programmate con WorkManager, non reinventare la ruota
- Hilt amministra gli oggetti, la modularizzazione il codice — nei progetti piccoli in solitaria non avere fretta
- Quattro scenari AI: scrivere codice, cercare informazioni, scrivere test, correggere bug; la metodologia è nella parte 7 (capitoli 37-47)
:::
