---
id: di-wu-shi-liu-zhang
num: 56
part: an-zhuo-kai-fa-pian
nav: Capitolo 56: Rifinire e pubblicare — Pubblicare su Google Play
toc: default
kind: chapter
---

### Capitolo 56: Rifinire e pubblicare — test, debug e lancio su Google Play

{class="chapter-intro mb-4"}
L'app è fatta, e adesso? Questo capitolo risponde alle tre domande che portano da «funziona» a «è pronta da consegnare»: come fare debug in modo efficiente per trovare i bug, come scrivere test per evitare regressioni e come portare l'app su Google Play perché sia scaricabile in tutto il mondo. La pubblicazione non è un semplice rito: è la linea che separa un'opera da un prodotto.

#### 1. I tre strumenti del debug: Logcat, breakpoint e inspector della UI

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Strumento</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">A cosa serve</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Come si usa</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logcat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Vedere i log di sistema e quelli scritti da te</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nel codice: Log.d("TAG", "valore=$x"); nel pannello cerca TAG per filtrare</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Debug con breakpoint</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fermare il programma su una riga e osservare i valori delle variabili</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Clicca accanto al numero di riga per creare un pallino rosso, esegui in modalità Debug e avanza passo per passo</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Layout Inspector</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Esaminare la struttura dell'interfaccia mentre gira</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menu Tools → Layout Inspector: l'albero dei componenti in tempo reale</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
I tre strumenti del debug

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consiglio: come leggere un errore?

{class="mt-1"}
Dopo un crash, nel Logcat compare uno stacktrace rosso: cerca dal basso verso l'alto la prima riga che inizia col tuo nome di pacchetto (per esempio com.example.yourapp): quella è quasi sempre la scena del crimine. Guarda prima il «tipo di Exception» (puntatore nullo? conversione di tipo?) e poi la riga «at ... tuofile:riga». Con questo trucco risolvi l'80% dei crash.
:::

#### 2. I test: l'assicurazione del codice

I test manuali non bastano: correggi una funzione e un'altra si rompe di nascosto. I test sono la «pillola anti pentimento» e il «giubbotto antiproiettile». I test Android si dividono in tre livelli; da principiante inizia a padroneggiare il primo:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Livello</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cosa testa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dove sta</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Velocità</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Test di unità</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logica pura (calcoli, verifiche)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/test/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pochi secondi</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Test strumentati</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Comportamento dell'interfaccia su un dispositivo reale</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/androidTest/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pochi minuti</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Test manuali</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La sensazione e l'esperienza di una persona vera</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sempre necessario</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
I tre livelli di test

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Esempio di unit test</span><span class="dots">···</span>
:::

```
// Estrai la logica tipo "stringa importo in numero" in una funzione pura
fun parseAmount(input: String): Double? {
    val v = input.trim().toDoubleOrNull()
    return if (v != null && v > 0) v else null
}

// Lo testiamo (JUnit4)
@Test
fun emptyInputReturnsNull() {
    assertEquals(null, parseAmount(""))
}
@Test
fun negativeReturnsNull() {
    assertEquals(null, parseAmount("-5"))
}
@Test
fun normalValueParses() {
    assertEquals(12.5, parseAmount("12.5"))
}
```
:::

Nel registro delle spese, la verifica degli importi e i calcoli delle statistiche dovrebbero stare sempre sotto l'ombrello dei test di unità. Per eseguirli: clic destro sulla cartella test → Run. Tutto verde: puoi toccare il codice in serenità.

#### 3. Firma e pacchetto: mettere il «timbro» all'app

Android impone che ogni pacchetto di installazione sia firmato: è come il timbro ufficiale che certifica che «questo pacchetto è mio e non è stato manomesso». In fase di debug Android Studio usa da solo la firma debug; per pubblicare serve la tua firma release. Procedura:

1. menu Build → Generate Signed Bundle / APK;
2. crea il file keystore (il portachiavi delle chiavi) — imposta una password e conservala con cura;
3. scegli release e il formato AAB, e la build è completata.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attenzione alla trappola: keystore perso = app persa

{class="mt-1"}
Per aggiornare l'app dopo la pubblicazione serve la stessa firma, altrimenti lo store rifiuta l'aggiornamento. Se perdi il file keystore e la password, non ti resta che pubblicare una nuova app da zero: gli utenti attuali restano a terra. Fai assolutamente il backup di keystore e password in un posto sicuro (archivio cifrato nel cloud + un quaderno di note): è una delle lezioni più costose della carriera di uno sviluppatore Android.
:::

#### 4. Tutto il percorso per pubblicare su Google Play

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Registrare l'account sviluppatore</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> Preparare gli asset per lo store</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> Carica l'AAB</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> Compila il modulo sulla sicurezza dei dati</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Revisione (da ore a giorni)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> Pubblicato</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 6: i sei passi per arrivare su Google Play
:::

- Registrazione: tassa una tantum di 25 dollari, serve un account Google funzionante;
- Materiali: icona dell'app (512×512), screenshot (almeno 2), descrizione delle funzioni, link all'informativa sulla privacy (obbligatoria se raccogli dati);
- Modulo sulla sicurezza dei dati: dichiara in buona fede quali dati raccogli — un registro delle spese che non va in rete può dichiarare «raccolta zero»;
- Revisione: la prima pubblicazione di un account nuovo passa spesso per una revisione umana, da qualche ora a qualche giorno; se te la respingono, correggi secondo le osservazioni ricevute.

Nota per i lettori in Cina: Google Play richiede un ambiente di rete particolare, e la distribuzione nella Cina continentale passa in genere per gli store nazionali (Huawei, Xiaomi, Yingyongbao e altri). La procedura per gli store nazionali è simile, ma ognuno ha i suoi gusti in fatto di revisione — lo stesso AAB/APK si può distribuire su più store. Per fare pratica, basta portarne a termine uno per aver già vinto.

#### 5. Come preparare i materiali dello store: la prima impressione vale i download

La pagina dello store è la vetrina che l'utente vede mentre «passeggia per i negozi». Tre materiali decidono la prima impressione:

- Icona: 512×512, non improvvisare con uno screenshot. Senza competenze di design, genera con uno strumento AI una semplice forma geometrica: è valida solo se, ridotta in miniatura sulla schermata home del telefono, resta riconoscibile a colpo d'occhio;
- Screenshot: almeno 2, meglio 4-6, che mostrino le scene d'uso delle funzioni più importanti; a ognuno aggiungi una frase scritta in linguaggio umano («registra una voce in un secondo» vale dieci volte «una soluzione efficiente per la gestione delle spese»);
- Descrizione: la prima frase deve chiarire «che cos'è + a chi serve»; evita di accumulare superlativi come «il più professionale, il più potente» — il posizionamento nella ricerca dello store dipende soprattutto da parole chiave e conversioni dei download: la sincerità rende più dell'esagerazione.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consiglio: guarda come fanno gli altri

{class="mt-1"}
Prima di pubblicare, fai un giro tra le prime dieci app dello stesso genere nello store e confronta gli screenshot: che stile hanno le loro icone? Che punto di forza raccontano gli screenshot? Come sono scritti i titoli? Imitare non è copiare: studi lo schema e ci metti i tuoi contenuti — è la lezione più rapida per il lancio di qualunque prodotto.
:::

#### 6. Mini checklist: prestazioni e report dei crash

Prima di pubblicare l'app, queste due cose meritano mezz'ora ciascuna:

##### 1. Quattro controlli sulle prestazioni

1. Gli elenchi con LazyColumn: mai impaginare a forza una lista lunga con Column — il caricamento lazy è la prima lezione di prestazioni su Android;
2. Non forzare le immagini originali: usa la libreria grafica Coil per ridimensionarle e metterle in cache in automatico — una foto originale da 5 MB basta a ingorgare un telefono di fascia bassa;
3. Evita i lavori pesanti sul thread principale: database, rete e file grossi vanno gestiti nelle coroutine;
4. Misura col Profiler: l'analizzatore di prestazioni integrato in Android Studio mostra memoria, CPU e consumo energetico — prima si misura, poi si ottimizza; niente sensazioni.

##### 2. Report dei crash

Se non crasha nei tuoi test, non vuol dire che non crashi sul telefono degli utenti. Prima di pubblicare integra Firebase Crashlytics (ufficiale di Google, gratuito): poche righe di configurazione e, quando l'app crasha, lo stacktrace viene segnalato da solo; dalla console vedi «quale modello, quale versione, su quale riga». Pubblicare senza monitoraggio dei crash è come guidare a occhi chiusi.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mani in pasta: fai la «consegna» del registro delle spese

{class="mt-1"}
① Aggiungi 3 test di unità alla logica tipo parseAmount; ② con il Logcat acchiappa con le tue mani un crash provocato apposta e aggiustalo; ③ genera un APK firmato in release e mandalo a un amico da installare (questo sì che è il rito dell'opera compiuta); ④ se hai fiato, registrati come sviluppatore e invia davvero il registro delle spese allo store. I primi tre punti si chiudono stasera.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riassunto del capitolo

- I tre strumenti del debug: Logcat per i log, breakpoint per le variabili, Layout Inspector per l'interfaccia
- Leggere un crash: risali lo stack fino alla prima riga col tuo nome di pacchetto
- Tre livelli di test: unità (in pochi secondi, impara prima questo) / strumentati / manuali
- Pubblicare richiede la firma: fai il backup di keystore e password; se li perdi, l'app «cambia padrone»
- Sei passi per la pubblicazione: registrazione → materiali → caricamento AAB → modulo sicurezza dati → revisione → pubblicazione
:::
