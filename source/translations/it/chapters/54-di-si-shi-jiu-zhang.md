---
id: di-si-shi-jiu-zhang
num: 49
part: an-zhuo-kai-fa-pian
nav: Capitolo 49: Preparare l'ambiente di sviluppo — Android Studio e il primo progetto
toc: default
kind: chapter
---

### Capitolo 49: Preparare l'ambiente di sviluppo — Android Studio e il primo progetto

{class="chapter-intro mb-4"}
Chi vuole lavorare bene deve prima affilare gli strumenti. In questo capitolo allestiamo la «cucina»: installiamo Android Studio, facciamo girare l'emulatore, creiamo il primo progetto Android della tua vita e poi smontiamo la struttura del progetto per capire ogni pezzo. Con l'ambiente pronto, vedrai per la prima volta il codice scritto da te trasformarsi in un pulsante che si può toccare — un momento che a molti resta in cuore per tutta la vita.

#### 1. Installare Android Studio

Android Studio è l'ambiente di sviluppo integrato (IDE) ufficiale di Google: è gratuito e ha tutto a bordo — scrivere codice, vedere l'anteprima dell'interfaccia, fare debug, creare i pacchetti. Installazione in quattro passi:

1. Apri il sito ufficiale developer.android.com/studio e scarica l'ultima versione stabile (ad agosto 2026 la versione successiva a Narwhal, disponibile per Windows/Mac/Linux);
2. Avvia il pacchetto d'installazione e vai sempre avanti con «Avanti» — l'assistente includerà in automatico l'Android SDK e i componenti dell'emulatore;
3. Al primo avvio scarica i componenti dell'SDK come indicato (va bene lasciare le spunte predefinite: servono qualche minuto e qualche GB di spazio);
4. Finito, vedrai la pagina di benvenuto — complimenti, la «cucina» è pronta.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attenzione: tieni a mente i requisiti hardware

{class="mt-1"}
Android Studio è un tipo che «mangia memoria»: si consigliano almeno 16 GB di RAM (con 8 GB funziona, ma l'emulatore tende a scattare), 20 GB o più di disco libero e una CPU con supporto alla virtualizzazione (attiva VT-x/AMD-V nel BIOS). Se il computer è davvero datato, puoi sostituire l'emulatore con il «debug su dispositivo reale» (ne parliamo nella sezione 4 di questo capitolo): l'esperienza è persino più fluida.
:::

#### 2. Creare il tuo primo progetto

Nella pagina di benvenuto clicca su New Project, scegli il modello Empty Activity (il più pulito per chi inizia) e compila tre cose:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Voce di configurazione</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cosa inserire</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Spiegazione</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">My First App</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nome dell'app, quello che appare nella schermata home del telefono</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Package name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example.myfirstapp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Identificativo univoco in tutto il mondo; per convenzione si usa il «dominio invertito», per ora lascia quello proposto</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minimum SDK</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API 26(Android 8.0)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Versione minima supportata: così copri il 95% e più dei dispositivi</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Le tre cose da compilare per creare un progetto

Dopo Finish, Android Studio con Gradle scaricherà in automatico le dipendenze e compilerà il progetto (la prima volta aspetta qualche minuto, poi ogni volta sarà molto più rapido). A build finita hai un'app che si può avviare — anche se per ora sa solo mostrare una riga: "Hello Android!".

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consiglio: i segreti del nome del pacchetto

{class="mt-1"}
Il nome del pacchetto (package name) è come la «carta d'identità» dell'app: non può ripetersi in tutto il mondo e, una volta pubblicata l'app, non si può più cambiare. Per gli esercizi personali basta com.example.xxx; per un prodotto vero serve il tuo dominio invertito (per esempio com.tuonome.app). Non pubblicare con com.example — lo store la respinge.
:::

#### 3. Farlo girare: emulatore e dispositivo reale

Il codice è pronto: serve un «telefono» su cui farlo girare. Hai due possibilità:

##### 1. L'emulatore (Emulator)

L'emulatore crea un telefono Android virtuale dentro il computer. In Android Studio apri Device Manager → Create Device, scegli un dispositivo (consigliata la serie Pixel) → seleziona un'immagine di sistema (quella con le Google APIs) → scaricala → avviala. Poi clicca sul triangolo verde Run nella barra degli strumenti: dopo pochi secondi la tua app compare sullo schermo del «telefono».

##### 2. Il debug su dispositivo reale (più consigliato)

Il dispositivo reale resta l'ambiente di prova più fedele — la sensazione degli scorrimenti, la rete vera, i sensori veri: l'emulatore non gli si avvicina. E il debug su un telefono Android vero è semplicissimo:

1. Sul telefono apri [Impostazioni] → [Info sul telefono], tocca 7 volte di fila «Numero build» per attivare le «Opzioni sviluppatore»;
2. In [Opzioni sviluppatore] attiva il Debug USB;
3. Collega il telefono al computer con il cavo dati e nel popup del telefono scegli «Consenti debug USB»;
4. Torna in Android Studio: il tuo telefono comparirà nel menu a tendina dei dispositivi in alto; clicca Run.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attenzione alle trappole: non tenere il debug USB sempre attivo

{class="mt-1"}
Il debug USB equivale ad aprire al computer una «porta sul retro». Quando carichi il telefono in luoghi pubblici o lo colleghi a computer di cui non ti fidi, chiudi sempre il debug USB, così nessuno potrà leggere i tuoi dati da lì. Quando hai finito di sviluppare, spegnilo: prendine l'abitudine.
:::

#### 4. Anatomia del progetto: a cosa serve ogni file

La prima volta che apri il progetto, l'albero dei file a sinistra può girarti la testa. Niente panico: nel lavoro di tutti i giorni il 90% del tempo avrai a che fare solo con questi:

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="300" viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="300" fill="#fafafa" rx="8"/>
      <text x="20" y="30" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ radice del progetto</text>
      <rect x="30" y="45" width="540" height="230" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <text x="45" y="70" font-size="11" fill="#4f46e5" font-weight="bold">app/ ← dove scrivi il codice</text>
      <rect x="60" y="82" width="240" height="178" fill="#eef2ff" rx="5"/>
      <text x="70" y="102" font-size="10" fill="#1e1b4b" font-weight="bold">src/main/</text>
      <text x="80" y="120" font-size="10" fill="#374151">├ java/…/MainActivity.kt  ← codice logico</text>
      <text x="80" y="138" font-size="10" fill="#374151">├ res/  ← risorse (immagini, testi, colori)</text>
      <text x="80" y="156" font-size="10" fill="#374151">└ AndroidManifest.xml  ← la "carta d'identità" dell'app</text>
      <text x="70" y="180" font-size="10" fill="#1e1b4b" font-weight="bold">build.gradle.kts</text>
      <text x="80" y="198" font-size="10" fill="#6b7280">Dichiara le librerie dipendenti (versione SDK, Compose, ecc.)</text>
      <text x="70" y="222" font-size="10" fill="#1e1b4b" font-weight="bold">src/androidTest/ e test/</text>
      <text x="80" y="240" font-size="10" fill="#6b7280">Codice di test automatico (si usa nel Capitolo 56)</text>
      <rect x="320" y="82" width="230" height="178" fill="#f0fdf4" rx="5"/>
      <text x="330" y="102" font-size="10" fill="#065f46" font-weight="bold">Altri file nella radice</text>
      <text x="340" y="122" font-size="10" fill="#374151">gradle/ + gradlew.bat  ← script di build</text>
      <text x="340" y="142" font-size="10" fill="#374151">settings.gradle.kts  ← impostazioni del progetto</text>
      <text x="340" y="162" font-size="10" fill="#6b7280">(Regola per principianti: tocca solo la cartella app/,</text>
      <text x="340" y="180" font-size="10" fill="#6b7280">per il resto, per ora considera tutto una "scatola nera" — non toccare)</text>
      <text x="340" y="208" font-size="10" fill="#9ca3af">.gitignore  ← elenco ignorato dal version control</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 2: la struttura del progetto che un principiante deve conoscere (regola pratica: tocca solo la cartella app/)
:::

- MainActivity.kt: la «porta d'ingresso» dell'app. Quando l'utente tocca l'icona, è la prima cosa che si sveglia. Nel modello attuale si occupa di mostrare "Hello Android!".
- AndroidManifest.xml: la «carta d'identità» dell'app — dichiara come si chiama l'app, quale icona usa, quali schermate ha e quali permessi richiede (fotocamera, posizione, ecc.).
- Cartella res/: il magazzino delle risorse, dove stanno immagini, icone, testi e colori. Mettere i testi nei file di risorse invece di scriverli fissi nel codice è una buona abitudine dello sviluppo Android (comodissimo per cambiare lingua o tema).
- build.gradle.kts: la «ricetta» della build — dichiara la versione minima supportata e da quali librerie dipende il progetto (per esempio Compose).

#### 5. Primo colpo di mano: cambia "Hello" con il tuo nome

Apri MainActivity.kt: vedrai il codice generato dal modello Compose. Trova la riga Text("Hello Android!"), sostituisci il testo tra virgolette con il tuo nome, per esempio Text("Ciao, sono Maria! Questa è la mia prima app"), poi premi Ctrl+R (Cmd+R su Mac) per rilanciare. Dopo qualche secondo, sull'emulatore comparirà il tuo nome.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · MainActivity.kt (modifica questa riga)</span><span class="dots">···</span>
:::

```
setContent {
    MyFirstAppTheme {
        Surface(modifier = Modifier.fillMaxSize()) {
            // ▼ cambia questo testo con il tuo
            Text("Ciao, Marco! Questa è la mia prima app")
        }
    }
}
```
:::

Congratulazioni: hai appena completato un intero ciclo «modifico il codice → compilo → installo → eseguo». Questo ciclo è la routine di sviluppo di ogni giorno a venire. Già che sei in calore, prova a cambiare qualcos'altro: aumenta la dimensione del testo, cambia colore — nel prossimo capitolo scopriremo da dove nascono queste «magie».

#### 6. Pronto soccorso degli errori comuni: la «sala d'emergenza» delle prime due settimane da principiante

Nella fase di preparazione dell'ambiente e di prima build molto probabilmente incontrerai i tre errori qui sotto. Niente panico: hanno tutti la loro cura:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Come si presenta l'errore</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Causa tipica</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">La cura</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle sync failed / dipendenze che scaricano lento</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Connessione ai repository in rete in difficoltà</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Configura per Gradle dei repository mirror (mirror Maven di Alibaba Cloud/Tencent Cloud): cerca online «gradle mirror repository» e segui le istruzioni per modificarlo</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Componenti SDK mancanti</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Il download dell'SDK è stato saltato in fase d'installazione</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Settings → SDK Manager: installare piattaforme e strumenti mancanti</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">L'emulatore non parte / schermo nero</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Virtualizzazione non attiva, immagine danneggiata</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Attiva VT-x/AMD-V nel BIOS; cancella e ricrea l'emulatore; oppure passa direttamente al debug su dispositivo reale</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Tabella di pronto soccorso per gli errori d'ambiente del principiante

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consiglio: il metodo per cercare gli errori

{class="mt-1"}
La prima riga del messaggio d'errore è la più preziosa — copiala così com'è nel motore di ricerca, aggiungendo la parola chiave "android studio". Non cercare domande vaghe tipo «come faccio a installare l'ambiente», ma errori precisi tipo "Gradle sync failed: Could not resolve com.android.tools.build". Solo le domande precise ottengono risposte precise.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mani all'opera: completa la tua «checklist» di riti da sviluppatore

{class="mt-1"}
① Installa Android Studio e fai girare l'emulatore; ② avvia una volta la tua app su un dispositivo reale e salva uno screenshot come ricordo; ③ cambia il testo Hello con il tuo nome; ④ comprimi il progetto e conservane un archivio. Fatti questi quattro passi, potrai annunciare agli amici: anch'io sono uno sviluppatore Android (screenshot alla mano).
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riepilogo del capitolo

- Android Studio = IDE ufficiale e gratuito; consigliati 16 GB di RAM + 20 GB di disco + virtualizzazione attiva
- I tre ingredienti di un nuovo progetto: nome, nome del pacchetto (univoco al mondo, niente pubblicazione con com.example), SDK minimo (da API 26)
- Due modi di eseguire: l'emulatore (telefono virtuale nel computer) e il dispositivo reale (attiva il debug USB e ricordati di chiuderlo dopo l'uso)
- La regola del progetto: tocca solo la cartella app/ — MainActivity.kt è la porta d'ingresso, il Manifest è la carta d'identità, res/ è il magazzino delle risorse
- La routine di sviluppo = cambi il codice → Run → guardi il risultato, e si riparte
:::
