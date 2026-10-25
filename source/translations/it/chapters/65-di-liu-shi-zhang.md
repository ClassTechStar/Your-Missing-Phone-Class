---
id: di-liu-shi-zhang
num: 60
part: ios-kai-fa-pian
nav: Capitolo 60: Preparare l'ambiente di sviluppo — Xcode e il primo progetto
toc: default
kind: chapter
---

### Capitolo 60: Allestire l'ambiente di sviluppo — Xcode e il primo progetto

{class="chapter-intro mb-4"}
Chi vuole fare bene il lavoro, prima affili gli attrezzi. In questo capitolo montiamo la «cucina»: installare Xcode, far girare il simulatore, creare il primo progetto iOS della tua vita e poi smontare la struttura del progetto per guardarla bene. Ambiente pronto, vedrai per la prima volta il codice scritto da te trasformarsi in un pulsante su cui toccare — un istante che a molti resta in mente per tutta la vita.

#### 1. Preparare un Mac

Partiamo dalla soglia: lo sviluppo iOS si fa per forza su macOS. Se non hai un Mac, le strade sono tre: comprarne uno (basta anche un Mac mini o un MacBook Air di seconda mano), noleggiare per un periodo breve un Mac nel cloud, oppure leggere prima la parte 8 «Programmazione Android in pratica» (si può fare da Windows).

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Voce di configurazione</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Requisito minimo</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Livello comodo (consigliato)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Chip</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Silicon (da M1)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">M2 o più recente</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memoria</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8GB</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">16GB</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Disco</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Almeno 40 GB liberi (Xcode è di corporatura robusta)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Da 256 GB in su</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sistema</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">L'ultimo macOS</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Aggiornamenti automatici sempre attivi</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Configurazione di riferimento per un Mac da sviluppo (agosto 2026)

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consiglio: puoi imparare il linguaggio anche senza Mac

{class="mt-1"}
Swift Playgrounds, gratuito su iPad, insegna le basi di Swift (senza Mac); si installa perfino su iPhone. Fatti prima le dita agili sul linguaggio del capitolo 61 dentro Playgrounds e, arrivato il Mac, partirai in volo. «Affilare l'ascia non rallenta chi taglia la legna»: è proprio questo.
:::

#### 2. Installare Xcode

Xcode è l'ambiente di sviluppo integrato ufficiale di Apple ed è gratuito. Si installa in tre passi:

1. sul Mac apri App Store, cerca "Xcode" e tocca Installa — attenzione: pesa parecchi GB, scegli un'ora con la rete veloce;
2. al primo avvio dopo l'installazione, accetta l'accordo e lascia finire i componenti (tutto in automatico);
3. nel menu Xcode → Settings → Locations controlla che Command Line Tools sia selezionato — gli strumenti da riga di comando servono a molti script e strumenti di terze parti.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attenzione: il «gioco degli abbinamenti» tra versione e sistema

{class="mt-1"}
Il nuovo Xcode spesso chiede l'ultimo macOS, mentre i Mac vecchi restano inchiodati a versioni datate. Per la pubblicazione su App Store Apple chiede di compilare con un Xcode abbastanza recente (di norma concede un periodo di respiro). Quindi non rimandare troppo gli aggiornamenti di sistema: gli sviluppatori iOS sono fra i più puntigliosi nell'inseguire le novità.
:::

#### 3. Creare il tuo primo progetto

Apri Xcode → Create New Project → scegli iOS → il template App, poi compila:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Voce di configurazione</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cosa inserire</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Note</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Product Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstApp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nome dell'app</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Il tuo Apple ID (gratuito)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Serve per la firma, basta l'account personale</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Organization Identifier</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Si unisce al Product Name per formare l'identificatore del pacchetto</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interface</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Il framework principale di questo libro</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Language</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Non serve spiegazione</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Le cinque cose da compilare per creare il progetto

Premuto Create, Xcode genera un progetto che parte subito. In alto a sinistra scegli un simulatore (per esempio iPhone 17) e tocca ▶ per eseguire — dopo qualche secondo, sullo schermo del simulatore appare una finestra con scritto "Hello, world!". La tua prima app iOS è appena nata.

#### 4. Anatomia del progetto: a cosa serve ogni file

A sinistra c'è il navigatore del progetto; da principiante ti basta riconoscere questi:

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="290" viewBox="0 0 600 290" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="290" fill="#fafafa" rx="8"/>
      <text x="20" y="28" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ radice del progetto</text>
      <rect x="30" y="42" width="540" height="225" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <rect x="45" y="56" width="250" height="196" fill="#eef2ff" rx="5"/>
      <text x="56" y="78" font-size="11" fill="#1e1b4b" font-weight="bold">MyFirstApp/ (cartella del codice)</text>
      <text x="66" y="100" font-size="10" fill="#374151">├ MyFirstAppApp.swift  ← punto di ingresso dell'app</text>
      <text x="66" y="120" font-size="10" fill="#374151">├ ContentView.swift  ← schermata principale</text>
      <text x="66" y="140" font-size="10" fill="#374151">└ Assets.xcassets  ← icone, immagini, colori</text>
      <text x="56" y="166" font-size="10" fill="#6b7280">(i nuovi file vanno tutti in questa cartella)</text>
      <text x="56" y="196" font-size="10" fill="#1e1b4b" font-weight="bold">Scheda Info / Info.plist</text>
      <text x="66" y="216" font-size="10" fill="#6b7280">Dichiarazioni dell'app: nome, permessi, impostazioni</text>
      <rect x="310" y="56" width="245" height="196" fill="#f0fdf4" rx="5"/>
      <text x="321" y="78" font-size="11" fill="#065f46" font-weight="bold">Altri posti importanti</text>
      <text x="331" y="100" font-size="10" fill="#374151">📁 Preview Content/  ← risorse di anteprima</text>
      <text x="331" y="122" font-size="10" fill="#374151"><i class="fas fa-bullseye mr-1"></i> Impostazioni del target (l'icona blu del progetto)</text>
      <text x="331" y="142" font-size="10" fill="#6b7280">— numero di versione, sistema minimo, firma: tutto qui</text>
      <text x="331" y="168" font-size="10" fill="#374151"><i class="fas fa-flask mr-1"></i> MyFirstAppTests/  ← unit test</text>
      <text x="331" y="188" font-size="10" fill="#374151">📱 MyFirstAppUITests/ ← test dell'interfaccia</text>
      <text x="331" y="216" font-size="10" fill="#9ca3af">(i modelli di test sono già generati; si usano nel Capitolo 67)</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 2: la struttura del progetto Xcode che i principianti devono conoscere
:::

- MyFirstAppApp.swift: l'ingresso del programma, in SwiftUI sono poche righe — «avvia, poi mostra la schermata principale»;
- ContentView.swift: la vista della schermata principale; tutto quello che ora vedi sta qui;
- Assets.xcassets: il magazzino delle risorse — icone, immagini e colori stanno qui;
- Impostazioni del target: entra toccando l'icona blu del progetto a sinistra; dentro ci sono numero di versione, versione minima di iOS e firma. Qui si impostano anche il nome visibile dell'app e l'icona.

#### 5. Trucchi di efficienza in Xcode: i cinque «potenziamenti da tastiera» per i principianti

Imparati bene questi e sembrerai «molto professionale»:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Azione</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Scorciatoia</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">A cosa serve</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Eseguire</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Compila e fa girare</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Aprire/attivare l'anteprima nella canvas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">L'interruttore del WYSIWYG</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sistemare l'indentazione</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Riordina da solo l'indentazione del codice selezionato</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Aprire un file al volo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Digiti il nome del file e si apre all'istante (il più usato!)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Commentare/togliere il commento</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Attivare e disattivare righe di codice al volo durante il debug</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Le scorciatoie Xcode di uso quotidiano (il corredo del principiante)

Due benefit nascosti in più: simulatori aperti insieme (iPhone e iPad in parallelo per confrontare i layout) e la biblioteca di snippet (trascina le righe di codice di uso frequente nel pannello Snippets a destra e la volta dopo le inserisci con un tocco) — usa subito gli strumenti di efficienza e la mano si affina da sé.

#### 6. Debug su dispositivo reale: portare l'app dentro il tuo iPhone

Il simulatore è comodo, ma il telefono vero è la meta. Con un Apple ID gratuito si può fare debug anche su dispositivo vero:

1. collega l'iPhone col cavo dati (oppure fai il debug senza fili sulla stessa Wi-Fi);
2. nell'elenco dei dispositivi in alto in Xcode scegli il tuo telefono: al primo giro chiede di accedere con l'Apple ID e prepara la firma in automatico;
3. sull'iPhone: [Impostazioni] → [Generali] → [VPN e gestione dispositivi] → dai fiducia al tuo certificato da sviluppatore;
4. tocca ▶ e l'app si installa sul telefono vero.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attenzione: il «limite dei sette giorni» dell'account gratuito

{class="mt-1"}
Le app firmate con un Apple ID gratuito scadono dopo 7 giorni (basta eseguirle ancora una volta per rinnovarle). È il meccanismo antiabuso di Apple e per la fase di studio va più che bene; l'account sviluppatore a pagamento (99 dollari/anno) non ha questo limite — dettagli al capitolo 67.
:::

#### 7. Primo assaggio + pronto soccorso per gli errori comuni

Apri ContentView.swift, sostituisci il testo dentro Text("Hello, world!") col tuo nome e premi ⌘R per rieseguire — dopo qualche secondo sul simulatore compare il tuo nome. Congratulazioni: hai portato a termine il primo ciclo completo «modificare il codice → compilare → installare → eseguire».

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Errore osservato</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Causa ricorrente</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Rimedio</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Errore di Signing</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team non scelto, certificato scaduto</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">In Target → Signing seleziona il tuo account; con l'account gratuito esegui ancora una volta</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Simulatore a schermo nero / non si apre</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Immagine di sistema corrotta</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menu Device → Erase All Content; oppure cancella il simulatore e ricrealo</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode scarica piano / non si installa</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rete di App Store traballante</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cambia fascia oraria; oppure scarica il pacchetto .xip offline dal sito per sviluppatori Apple</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Tabella di pronto soccorso per gli errori d'ambiente dei principianti

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mani in pasta: completa la tua checklist dei «riti dello sviluppatore»

{class="mt-1"}
① Installa Xcode e fai girare il simulatore; ② esegui una volta la tua app sul telefono vero e tieni lo screenshot come ricordo; ③ cambia il testo di Hello col tuo nome; ④ nelle impostazioni del target porta il nome visibile dell'app a «La mia prima app». Fatti questi quattro passi, sei una persona che ha un'opera sua.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riassunto del capitolo

- La soglia dura: Mac + Xcode; senza Mac, impara prima il linguaggio con Swift Playgrounds su iPad
- Xcode si installa da App Store; le versioni nuove chiedono il sistema aggiornato, non rimandare
- I cinque ingredienti del nuovo progetto: nome, Team, identificatore dell'organizzazione, SwiftUI, Swift
- La regola del progetto: tutto il codice sta nella cartella MyFirstApp/; le impostazioni del target reggono versione e firma
- Con l'Apple ID gratuito il debug su dispositivo vero ha il limite della firma a 7 giorni; l'account a pagamento non ce l'ha
- La giornata tipo dello sviluppatore = cambiare il codice → ⌘R → guardare l'effetto, e si ricomincia
:::
