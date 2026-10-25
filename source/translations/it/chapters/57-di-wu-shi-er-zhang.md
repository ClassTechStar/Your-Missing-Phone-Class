---
id: di-wu-shi-er-zhang
num: 52
part: an-zhuo-kai-fa-pian
nav: Capitolo 52: I quattro componenti fondamentali e il ciclo di vita delle Activity
toc: default
kind: chapter
---

### Capitolo 52: I quattro componenti principali e il ciclo di vita dell'Activity

{class="chapter-intro mb-4"}
Se Compose è il «volto» dell'app, questo capitolo parla del suo «scheletro». Il sistema Android ha quattro componenti fondamentali, e tutte le app sono assemblate con loro; il più importante, l'Activity, ha una «mappa del ciclo di vita» che ogni sviluppatore Android deve incidersi in testa. A capitolo finito capirai misteri antichi come «perché quando torno dallo sfondo la mia app ha perso lo stato».

#### 1. I quattro componenti principali: le «colonne portanti» di Android

Android definisce ufficialmente quattro componenti fondamentali, ognuno addetto a un tipo di lavoro:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Componente</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Compito</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Per fare un paragone</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activity</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Un'interfaccia visibile</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La vetrina del negozio — l'utente la vede e ci interagisce</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Service</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">L'«invisibile» che lavora in background</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">L'operaio del magazzino — mette la musica, scarica i file, senza bisogno d'interfaccia</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BroadcastReceiver</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Riceve i messaggi di sistema (broadcast)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La portineria — l'altoparlante che annuncia «batteria quasi scarica», «rete persa»</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ContentProvider</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Condivide dati tra app</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">L'archivio pubblico — per esempio mette i contatti a disposizione delle altre app</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Colpo d'occhio sui quattro componenti di Android

Da principiante passerai il 95% del tempo con gli Activity; Service e BroadcastReceiver servono quando fai riproduzione musicale o notifiche push; ContentProvider si usa meno di tutti (il sistema ha già incapsulato i dati più comuni). Un'avvertenza in più: tutti e quattro i componenti vanno «iscritti all'anagrafe» in AndroidManifest.xml — senza iscrizione il sistema non li trova.

#### 2. Il ciclo di vita dell'Activity: la prima «mappa del tesoro» dello sviluppo Android

Un'app sul telefono può essere interrotta in qualunque momento: arriva una chiamata, l'utente passa a WeChat per rispondere, la memoria del sistema non basta e ti chiude... La vita di un Activity è un viaggio in circolo su questa mappa:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onCreate (nascita: inizializzazione)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onStart (visibile)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onResume (in primo piano, interattivo)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onPause (parzialmente coperto)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onStop (invisibile)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center">onDestroy (distrutto)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">🔁 onRestart / onStart / onResume: al ritorno in primo piano si ripercorre la strada a ritroso</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 4: il ciclo di vita dell'Activity (in avanti: fila di sopra si nasce → fila di sotto si esce, al ritorno si ripercorre la strada a ritroso)
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Callback</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Quando scatta</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Uso tipico</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onCreate</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Quando l'Activity viene creata (una volta)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Caricare l'interfaccia, inizializzare i dati</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStart</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">L'interfaccia diventa visibile</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Avviare qualche logica leggera</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onResume</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prende il focus, è interattiva</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Avviare le animazioni, riprendere la riproduzione</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onPause</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Quando è parzialmente coperta / nell'istante in cui si passa ad altro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mettere in pausa le animazioni, salvare la bozza</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStop</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Completamente invisibile</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Liberare le risorse pesanti, mettere in pausa i download</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onDestroy</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prima di essere distrutta</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Le ultime pulizie</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Gli usi tipici dei sei callback del ciclo di vita

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attenzione alle trappole: ruotare lo schermo «uccide» l'Activity

{class="mt-1"}
L'incidente più classico da principiante: l'app ruota lo schermo e il testo del campo di input sparisce tutto. Il motivo: di default la rotazione dello schermo distrugge e ricrea l'Activity (rifacendo il giro onDestroy → onCreate). La soluzione: salvare lo stato con rememberSaveable (il sostituto di remember in Compose), che alla ricostruzione si ritrova da solo i valori. Lo useremo e riuseremo nei capitoli 6 e 7.
:::

#### 3. Intent: il «biglietto» per muoversi dentro e fuori dall'app

L'Intent (intenzione) è il «biglietto» con cui i componenti comunicano. Per saltare da una schermata all'altra, o per aprire il browser o far partire la fotocamera, devi sempre «prendere il biglietto e salire a bordo»:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Navigare con Intent</span><span class="dots">···</span>
:::

```
// Modo 1: Intent esplicito — indichi esattamente quale schermata aprire
val intent = Intent(this, DetailActivity::class.java)
intent.putExtra("name", Marco)     // porta con sé il "bagaglio" (dati)
startActivity(intent)

// Modo 2: Intent implicito — dichiari cosa fare e il sistema trova chi lo fa
val web = Intent(Intent.ACTION_VIEW, Uri.parse("https://developer.android.com"))
startActivity(web)   // il sistema apre il browser / oppure ti fa scegliere
```
:::

Le due modalità hanno usi diversi: l'esplicita serve per navigare tra le schermate della propria app; l'implicita per usare le capacità del sistema o di altre app (aprire pagine web, telefonare, condividere). Nei progetti Compose, dentro una Composable basta recuperare il Context con LocalContext.current per poter chiamare startActivity.

#### 4. Schermate multiple e navigazione

Le app vere hanno più schermate. Lo schema di navigazione raccomandato ufficialmente per Compose è Navigation Compose (libreria androidx.navigation):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Scheletro di Navigation Compose</span><span class="dots">···</span>
:::

```
val navController = rememberNavController()

NavHost(navController, startDestination = "home") {
    composable("home") { HomeScreen(navController) }
    composable("detail/{name}") { entry ->
        val name = entry.arguments?.getString("name")
        DetailScreen(name ?: "Sconosciuto")
    }
}

// Navigare da una schermata:
navController.navigate("detail/Marco")     // con argomenti
navController.popBackStack()              // torna indietro
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consiglio: e quando le schermate diventano tante?

{class="mt-1"}
Quando il progetto cresce, raccogli tutte le rotte delle schermate in un unico file (per esempio AppNavGraph.kt) e governale da un solo posto: non lasciare la logica «dove si va» sparsa tra le schermate. È il primo passo dal «funziona» al «si può mantenere».
:::

#### 5. Per inciso: cos'è un Fragment (e perché questo libro non lo insegna)

Frugando nei vecchi tutorial ti imbatterai di sicuro nel Fragment — un «frammento d'interfaccia riutilizzabile» dentro un Activity, protagonista assoluto delle vecchie architetture a più pagine. Ma nell'era Compose le schermate si fanno direttamente con funzioni Composable + rotte di Navigation, e anche ufficialmente il Fragment è stato ridimensionato. Per questo il libro non lo mette nel percorso principale.

Il mio consiglio: nei nuovi progetti non usare Fragment di tua iniziativa; ma quando leggi codice vecchio o te lo chiedono a un colloquio, ti basta sapere che è un «frammento d'interfaccia incastonato nell'Activity». Nelle risorse per studiare scegli sempre materiale successivo al 2023 — il «vecchio almanacco» dello stack Android si aggiorna più in fretta di quel che si pensa.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mani all'opera: dai una «memoria» al contatore

{class="mt-1"}
Rivedi il contatore del capitolo 51: ① sostituisci remember con rememberSaveable e ruota lo schermo per verificare che il numero sia ancora lì; ② aggiungi un pulsante «Info» che con Navigation porta a una seconda schermata che mostra il numero di versione; ③ stampa un log nelle onCreate/onPause delle due schermate (Log.d) e con Logcat osserva l'ordine di chiamata del ciclo di vita. Fatti questi tre passi, il ciclo di vita non sarà più chiacchiere da tavolino.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riepilogo del capitolo

- I quattro componenti: Activity (vetrina), Service (background), BroadcastReceiver (altoparlante), ContentProvider (archivio)
- I sei callback del ciclo di vita: onCreate → onStart → onResume → onPause → onStop → onDestroy
- Ruotare lo schermo distrugge e ricrea l'Activity: salva lo stato con rememberSaveable
- L'Intent è il «biglietto»: esplicito per le schermate di casa, implicito per le capacità del sistema
- Schermate multiple con Navigation Compose: NavHost + rotte composable
:::
