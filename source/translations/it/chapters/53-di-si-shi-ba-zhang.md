---
id: di-si-shi-ba-zhang
num: 48
part: an-zhuo-kai-fa-pian
nav: Capitolo 48: Conoscere Android — Dal sistema operativo all'ecosistema di sviluppo
toc: default
kind: chapter
---

### Capitolo 48: Conoscere Android — dal sistema operativo all'ecosistema di sviluppo

{class="chapter-intro mb-4"}
Congratulazioni per questa decisione: da «chi gioca col telefono» a «chi crea le app per il telefono». Prima di metterci mano, spalmiamo la mappa sul tavolo: da dove viene Android? Perché gli sviluppatori di tutto il mondo scrivono app per lui? Cosa succede tra il momento in cui le tue dita battono sulla tastiera e quello in cui l'app arriva sul telefono dell'utente?

#### 1. Le origini di Android: dal «piccolo robot» al «sistema operativo più diffuso al mondo»

La storia di Android comincia nel 2003: un ingegnere di nome Andy Rubin fonda la società Android, con un obiettivo molto concreto: realizzare un sistema operativo intelligente che «capisse le fotocamere» meglio di altri. Nel 2005 Google la acquista; nel 2007, insieme a decine di produttori, fonda l'Open Handset Alliance (OHA); nel settembre 2008 arriva in vendita il primo telefono Android, l'HTC Dream (G1).

Il seguito lo conosciamo tutti: nel 2026 Android è il sistema operativo mobile con la quota di mercato più grande del pianeta, con miliardi di dispositivi attivi. Il tuo telefono, il decoder della TV, lo schermo grande dell'auto, l'orologio intelligente: c'è da scommettere che girano su Android. Cosa significa? Che ogni riga di codice che scrivi ha la possibilità di finire nelle mani del maggior numero di persone al mondo.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consiglio: il DNA open source di Android

{class="mt-1"}
Il codice centrale di Android (AOSP, Android Open Source Project) è open source — qualunque produttore può prenderlo, modificarlo e personalizzarlo. Ecco perché Xiaomi ha MIUI (oggi HyperOS), Huawei il livello di compatibilità HarmonyOS e Samsung One UI. Per gli sviluppatori è una buona notizia: ciò che impari è «sviluppo per Android», non «sviluppo per un certo marchio» — un solo impegno, valido per tutto il mercato.
:::

Anche l'evoluzione dei nomi delle versioni è curiosa: dalla 1.5 Cupcake in poi, ogni versione maggiore ha preso il nome di un dolce — Donut, Eclair, Frozen Yogurt, Gingerbread... fino ad Android 10 nel 2019, quando si è passati ai soli numeri. Ad agosto 2026 l'ultima versione stabile è Android 17, mentre il «minimo supportato» che conta davvero quando sviluppi, per le app di punta, di solito si colloca tra Android 8 (API 26) e Android 10 (API 29) — sostenendo i dispositivi di qualche anno fa il tuo bacino di utenti resta abbastanza ampio.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Versione</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Nome in codice/anno</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Punti importanti per gli sviluppatori</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 8 (API 26)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Oreo · 2017</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Canali di notifica e limiti in background — la soglia minima per molti dispositivi datati</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 10 (API 29)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2019</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Arriva lo scoped storage: le regole di accesso ai file cambiano radicalmente</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 12 (API 31)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2021</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Colori dinamici con Material You: un grande salto nell'aspetto dell'interfaccia</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 13 (API 33)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2022</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Permesso notifiche a runtime: il popup chiede se consentire le notifiche</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 14-15 (API 34-35)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2023-2024</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gesto Indietro predittivo, pagine da 16 KB, privacy ulteriormente inasprita</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 16-17 (API 36-37)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2025-2026</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ritmo più rapido delle versioni minori, integrazione delle capacità AI (come le estensioni Gemini)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Breve storia delle versioni di Android (ad agosto 2026, punti chiave per lo sviluppo)

#### 2. In che linguaggio scrivere: Java o Kotlin?

Nella storia dello sviluppo Android due sono stati i linguaggi di punta. Java è il «padre fondatore» — c'era già alla nascita di Android; Kotlin è il «cittadino di prima classe» scelto da Google nel 2017, dal 2019 la linea ufficiale è «Kotlin-first», e nel 2026 i nuovi progetti sono ormai quasi tutti in Kotlin, mentre i vecchi progetti stanno migrando uno dopo l'altro.

Parliamoci chiaro: se parti davvero da zero, impara subito Kotlin e non tornare indietro a Java. I motivi sono tre: primo, in Kotlin si scrive il 30%-40% di codice in meno che in Java (a parità di funzioni, Kotlin è più corto e più chiaro); secondo, previene per natura il «null pointer», l'incubo dei principianti; terzo, tutti i tutorial moderni, la documentazione ufficiale e gli strumenti di programmazione AI (ti ricordi il nostro libro sulla programmazione AI?) hanno Kotlin come riferimento. Java lo incontrerai solo mantenendo vecchi progetti o leggendo codice datato.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Stile Java (versione prolissa)

{class="font-mono text-xs leading-relaxed"}
public class MainActivity extends Activity {<br>&nbsp;&nbsp;@Override<br>&nbsp;&nbsp;protected void onCreate(Bundle b) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b);<br>&nbsp;&nbsp;&nbsp;&nbsp; setContentView(R.layout.activity);<br>&nbsp;&nbsp;}<br>}
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Stile Kotlin (versione essenziale)

{class="font-mono text-xs leading-relaxed"}
class MainActivity : ComponentActivity() {<br>&nbsp;&nbsp;override fun onCreate(b: Bundle?) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b)<br>&nbsp;&nbsp;&nbsp;&nbsp;setContent { App() }<br>&nbsp;&nbsp;}<br>}
:::
:::

Per fare la stessa cosa, Kotlin risparmia un mucchio di graffe e di codice ripetitivo. Lo impareremo per bene nel Capitolo 50; per ora ti basta ricordare che la «lingua franca» dello sviluppo Android si chiama Kotlin.

#### 3. Come nasce un'app?

Molti pensano che «sviluppare un'app» voglia dire accendersi il computer e scrivere codice a raffica. In realtà, dall'idea al telefono dell'utente, un'app percorre più o meno questa catena di montaggio:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-lightbulb mr-1"></i> Idea</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center">📐 Progettazione (interfaccia + funzioni)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-keyboard mr-1"></i> Scrivi codice</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hammer mr-1"></i> Compilazione e pacchetto (APK/AAB)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Test (emulatore + dispositivo reale)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-rocket mr-1"></i> Rilascio (store/installer)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 1: l'intero percorso di un'app Android, dall'idea alla pubblicazione
:::

In questo flusso ci sono due concetti che conviene conoscere subito:

- APK: il formato del pacchetto di installazione delle app Android (.apk); con un doppio clic si installa sul telefono, come i .exe di Windows. Per le tue prove quotidiane o per passarla in giro agli amici, si usa questo.
- AAB: Android App Bundle (.aab), il «formato di impacchettamento avanzato» per la pubblicazione su Google Play. Lo store lo ritaglia dinamicamente in base al modello di telefono dell'utente, così ognuno scarica un pacchetto più leggero. Non lo installi da solo: va consegnato allo store.

E sentirai sempre più spesso una parola: SDK (Software Development Kit, kit di sviluppo software). È l'intero «corredo di sviluppo» che la casa Android mette a disposizione — librerie API di ogni versione, strumenti di debug, immagini per l'emulatore e altro. Le classi come Activity o Button che richiami mentre scrivi codice vengono tutte dall'SDK.

#### 4. Panoramica dello stack tecnologico di Android: la tua «lista delle armi»

Prima di studiare sul serio, fai amicizia con la configurazione standard dei progetti Android di punta nel 2026 — se adesso questa lista ti risulta incomprensibile nessun problema: quando avrai finito il libro, rileggendola tutto ti apparirà chiaro:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Livello</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Scelta prevalente (2026)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">A cosa serve</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Linguaggio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin 2.x</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Il linguaggio in cui si scrive la logica</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interfaccia</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jetpack Compose + Material 3</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Disegnare l'interfaccia col codice (il filo conduttore di questo libro)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Architettura</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MVVM + ViewModel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Separare interfaccia e logica, così il codice resta ordinato</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Archiviazione dei dati</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room (database) + DataStore (configurazioni)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Salvare i dati dentro il telefono</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rete</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit + OkHttp + coroutine di Kotlin</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Parlare con il server</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Strumenti di build</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle + Kotlin DSL</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Trasformare il codice nel pacchetto di installazione</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ambiente di sviluppo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">L'IDE «tutto in uno» ufficiale di Google</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Panoramica dello stack Android di punta nel 2026

Non farti intimidire da questa fila di parole inglesi. Sono le pentole e i tegami della cucina — per ora ti basta sapere che «per cucinare bisogna entrare in cucina»; come si usa ogni strumento lo vedrai smontato pezzo per pezzo nei capitoli che vengono. E la buona notizia è questa: quando crei un nuovo progetto, Android Studio ti configura da solo tutto l'insieme; tu pensa soltanto a cucinare.

#### 5. Android vs iOS: la prima «scelta di campo» per gli sviluppatori

Probabilmente hai in mano insieme un dispositivo Android e uno Apple. Da sviluppatore vale la pena conoscere in anticipo le differenze di esperienza tra i due mondi — non è la presa di posizione su «quale sia migliore», ma i conti concreti di «quale lato conviene per partire»:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Aspetto</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Sviluppo Android</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Sviluppo iOS</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Computer per sviluppare</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Va bene Windows / Mac / Linux</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Serve un Mac (Xcode è in esclusiva)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Strumento di sviluppo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio (gratuito)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode (gratuito) + quota annuale di 99 $ per pubblicare</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Revisione in fase di pubblicazione</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Permissiva, da poche ore a pochi giorni</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rigorosa, 1-7 giorni sono la norma</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prova sul dispositivo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gli APK si distribuiscono e si installano liberamente</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Distribuzione limitata, per i test servono firma/TestFlight</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ambiente di guadagno</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Soprattutto pubblicità e canali cinesi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Su App Store le abitudini di spesa per gli acquisti in-app sono migliori</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Costo di apprendimento</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tanti concetti (i quattro componenti principali, ecc.)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ecosistema chiuso ma sistema unificato e ottima documentazione</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Confronto tra i percorsi di sviluppo Android e iOS (agosto 2026)

A dire il vero: se il tuo computer non è un Mac, la scelta non si pone nemmeno — Android è l'unica opzione. Se hai un Mac, le parti 8 e 9 di questo libro si possono leggere a confronto: l'approccio alla programmazione è lo stesso, e imparata una, l'altra verrà molto più in fretta.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mani all'opera: guarda l'«Android» del tuo telefono

{class="mt-1"}
Apri sul telefono [Impostazioni] → [Info sul telefono] (o «Informazioni sul dispositivo»), trova la voce «Versione Android» — toccala più volte di fila e attiverai anche il minigioco easter egg del sistema. Annota il numero di versione e confrontalo con la tabella qui sopra per capire a quale generazione appartiene. Il tuo telefono è il tuo primo «dispositivo di test».
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riepilogo del capitolo

- Android nasce nel 2008 e nel 2026 è il sistema mobile con la quota di mercato mondiale più grande, con miliardi di dispositivi attivi
- L'ultima versione ufficiale è Android 17; le app principali supportano almeno Android 8-10, per puntare su una base utenti davvero ampia
- Per i nuovi progetti solo Kotlin: 30% e più di codice in meno, protezione dai null pointer, scelta ufficiale di Google
- L'APK si installa a mano, l'AAB va sullo store; l'SDK è il kit ufficiale per sviluppare
- Lo stack tecnologico standard del 2026: Kotlin + Compose + MVVM + Room + Retrofit + Gradle + Android Studio
:::
