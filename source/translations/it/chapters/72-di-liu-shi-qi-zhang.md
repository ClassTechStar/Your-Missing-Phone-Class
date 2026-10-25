---
id: di-liu-shi-qi-zhang
num: 67
part: ios-kai-fa-pian
nav: Capitolo 67: Rifinire e pubblicare — Pubblicare sull'App Store
toc: default
kind: chapter
---

### Capitolo 67: Lucidatura e pubblicazione — test, debug e approdo sull'App Store

{class="chapter-intro mb-4"}
L'app è fatta, e adesso? Questo capitolo risponde alle tre questioni del passaggio da "funziona" a "consegnabile": come fare debug in modo efficiente per trovare i bug, come scrivere test per prevenire le regressioni e come portare l'app sull'App Store perché il mondo intero possa scaricarla. L'approdo sullo store non è solo una cerimonia: è la linea di confine tra un'opera e un prodotto.

#### 1. I tre strumenti del debug: print, breakpoint, anteprima

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Strumento</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">A cosa serve</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Come si usa</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">print + console</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Leggere i log di esecuzione</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nel codice print("valore=\(x)") e l'output si legge nella console in basso a Xcode</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Debug con breakpoint</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Far fermare il programma su una riga e vedere i valori delle variabili</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tocca accanto al numero di riga per creare il segnalino blu; all'esecuzione il programma si ferma lì e avanzi passo per passo</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Anteprima SwiftUI + debugger</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Vedere in tempo reale l'interfaccia e la gerarchia delle viste</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Canvas di #Preview + l'ispettore View Hierarchy a runtime</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
I tre strumenti del debug

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consiglio: come leggere un crash?

{class="mt-1"}
Quando Swift crasha, la console stampa "Fatal error" con la causa e Xcode si ferma sulla riga incriminata evidenziandola. I crash passati su dispositivo reale si consultano in Xcode → Window → Organizer → Crashes (serve un account a pagamento). Cerca prima di tutto "la prima frase della causa dell'errore + swiftui": solo una domanda precisa produce una risposta precisa.
:::

#### 2. I test: l'assicurazione del codice

I test a mano non sono affidabili — correggi una funzione e un'altra si rompe senza farsi notare. I test sono la "pillola dei rimpianti" e il "giubbotto antiproiettile". Su iOS si usa il framework XCTest, in due varianti:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Livello</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cosa verifica</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Target</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Velocità</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Test unitari</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logica pura (calcoli, validazioni)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppTests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">In secondi</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Test UI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Comportamento reale dell'interfaccia</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppUITests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">In minuti</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Test manuale</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Le sensazioni e l'esperienza di una persona vera</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Serve sempre</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
I livelli di test iOS (il progetto modello ha già due Test Target predisposti)

::: div .code-block
:::inline div .code-head
<span>SWIFT · Esempio di unit test</span><span class="dots">···</span>
:::

```
import XCTest

// Estrai la logica tipo "stringa importo in numero" in una funzione pura
func parseAmount(_ input: String) -> Double? {
    guard let v = Double(input.trimmingCharacters(in: .whitespaces)),
          v > 0 else { return nil }
    return v
}

final class AmountTests: XCTestCase {
    func testEmptyInputReturnsNil() {
        XCTAssertNil(parseAmount(""))
    }
    func testNegativeReturnsNil() {
        XCTAssertNil(parseAmount("-5"))
    }
    func testNormalValueParses() {
        XCTAssertEqual(parseAmount("12.5"), 12.5)
    }
}
```
:::

Eseguire i test: ⌘U. Quando è tutto verde puoi modificare il codice con serenità. La validazione degli importi e i calcoli di riepilogo del registro delle spese dovrebbero essere coperti da test unitari.

#### 3. Firma e pacchetto: mettere il "sigillo" all'app

Ogni app iOS deve essere firmata per poter essere installata — prova che "questo pacchetto viene da te e non è stato manomesso". I rapporti di gerarchia:

- Fase di apprendimento: Apple ID gratuito + firma automatica di Xcode (Personal Team), funziona su dispositivo reale ma va rinnovata ogni 7 giorni;
- Fase di distribuzione: un account sviluppatore a pagamento (99 dollari/anno) emette certificati e profili di provisioning, indispensabili per lo store e per l'installazione di lungo periodo.

Pacchetto: menu di Xcode Product → Archive (creare l'archivio), a build conclusa in Organizer Distribute App → scegli App Store Connect → carica. L'archiviazione richiede come destinazione Generic iOS Device (non il simulatore): è il passaggio che i principianti dimenticano più spesso.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attenzione alle trappole: certificato perso = aggiornamenti in stallo

{class="mt-1"}
Se perdi il certificato di firma e la chiave privata, non potrai più inviare aggiornamenti alla vecchia app: gli utenti potranno installare solo l'applicazione da "nuova". Fai un backup accurato dei certificati (esportazione .p12 dal portachiavi) e custodisci bene la password. Per fortuna Apple offre la "firma automatica" e la gestione dei certificati nel cloud (in Xcode spunta Automatically manage signing), che evita la maggior parte delle insidie manuali.
:::

#### 4. Il percorso completo per arrivare sull'App Store

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Registrare l'account sviluppatore</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> Preparare gli asset per lo store</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> Carica la build</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> Compila info su privacy e revisione</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Revisione Apple (1-7 giorni)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> Pubblicato</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 5: i sei passi per l'approdo sull'App Store
:::

- Registrazione: developer.apple.com, account personale 99 dollari/anno;
- Materiali: icona (1024×1024, senza angoli arrotondati — li taglia Apple), screenshot (per le varie dimensioni di iPhone), descrizione, link all'informativa sulla privacy;
- Questionario sulla privacy: dichiara con onestà quali dati raccogli — un registro delle spese senza rete può dichiarare "nessun dato raccolto";
- Revisione: alla prima sottomissione l'attesa è spesso di 1-7 giorni; se vieni respinto, correggi punto per punto secondo le "note di revisione" — le motivazioni del rifiuto di Apple sono di solito scritte in modo molto specifico, basta metterle in pratica;
- TestFlight: prima della pubblicazione, manda la versione di prova agli amici per il beta testing (fino a 10000 persone), raccogli un giro di feedback e poi sottometti ufficialmente: tutto da professionisti.

#### 5. Come fare i materiali dello store: la prima impressione vale i download

La pagina dello store è la vetrina che l'utente vede mentre "gira per i negozi". Tre materiali decidono la prima impressione:

- Icona: 1024×1024, non improvvisare con uno screenshot. Se non hai competenze di design, genera una forma essenziale con uno strumento di IA: è valida solo se, ridotta sul desktop, resta riconoscibile a colpo d'occhio;
- Screenshot: almeno 2 set (per le dimensioni principali di iPhone), che mostrino le scene funzionali più importanti; a ognuno una frase in parole semplici ("Registra una voce in un secondo" vale dieci volte "Efficiente soluzione di contabilità");
- Descrizione: la prima frase chiarisca "cos'è + per chi è", senza accumulare "il più professionale, il più potente" — la sincerità funziona meglio dell'esagerazione.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mettiti alla prova: "consegna" una volta il registro delle spese

#### 6. Segnalazione dei crash e piccola lista per l'ottimizzazione delle prestazioni

Prima di portare l'app sullo store, queste due cose meritano mezz'ora ciascuna:

##### 1. Monitoraggio dei crash

Se non crasha nei tuoi test, non significa che non crashi sul telefono dell'utente. Apple offre rapporti di crash gratuiti in Xcode Organizer (con l'account a pagamento si vedono i log dei crash su dispositivo reale); la soluzione più comoda è integrare un SDK di terze parti (per esempio Firebase Crashlytics). Pubblicare senza monitoraggio dei crash è come guidare a occhi chiusi.

##### 2. I quattro controlli delle prestazioni

1. Per gli elenchi usa LazyVStack / List: non impaginare liste lunghe con un normale VStack — il caricamento pigro è la prima lezione di prestazioni;
2. Non imporre le immagini originali: usa AsyncImage (immagini remote) e la cache di sistema — un originale da 5MB basta a bloccare i modelli più datati;
3. Niente lavori pesanti sul thread principale: rete e file grandi passano per async/await;
4. Misura con Instruments: il profiler incluso in Xcode (Time Profiler, controllo delle perdite di memoria) — prima misura, poi ottimizza, non fidarti delle sensazioni.

{class="mt-1"}
① Aggiungi 3 test unitari alla logica di parseAmount e simili (verdi con ⌘U); ② con un breakpoint cattura con le tue mani un crash provocato da te e risolvilo; ③ crea un pacchetto con Product → Archive e usa TestFlight per invitare gli amici al beta testing; ④ se hai energie in più, registrati come sviluppatore e sottometti davvero il registro delle spese allo store. I primi tre passi si possono completare stasera.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riepilogo del capitolo

- I tre strumenti del debug: log con print, breakpoint, anteprima SwiftUI e ispettore delle viste
- XCTest: test unitari (⌘U) + test UI + test manuale, già predisposti nel modello
- Firma: firma automatica con l'account gratuito (rinnovo ogni 7 giorni); per distribuire serve l'account a pagamento
- Pacchetto: Generic iOS Device + Archive + Distribute; il certificato va assolutamente salvato in backup
- I sei passi dello store: registrazione → materiali → caricamento → questionario privacy → revisione → pubblicazione; prima il beta testing con TestFlight
:::
