---
id: di-liu-shi-ba-zhang
num: 68
part: ios-kai-fa-pian
nav: Capitolo 68: Il percorso di crescita — Permessi, notifiche e architettura moderna
toc: default
kind: chapter
---

### Capitolo 68: La strada del livello successivo — permessi, notifiche e architettura moderna

{class="chapter-intro mb-4"}
Saper costruire un'app è solo l'inizio. In questo capitolo parliamo di qualche scoglio del passaggio da "saper fare" a "far bene": come chiedere i permessi con eleganza, come inviare notifiche senza risultare antipatici, come alzare di un livello l'architettura e — nel 2026 — come scrivere codice iOS in coppia con l'IA. Ogni punto è qualcosa che incontrerai subito in un progetto reale.

#### 1. Permessi: prima bussa alla porta, poi entra

Fotocamera, posizione, contatti, notifiche… Per queste "zone sensibili" iOS esige che l'app chieda all'utente con un avviso quando le usa. La regola è "dichiarazione + richiesta + degrado elegante", in tre passi:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Richiesta permessi (esempio posizione)</span><span class="dots">···</span>
:::

```
// 1. Dichiara il testo d'uso in Info.plist (senza di esso, crash immediato!)
// Privacy - Location When In Use Usage Description: "Usata per consultare il meteo della tua città"

// 2. Richiedi al momento dell'uso
import CoreLocation

@Observable
class LocationModel {
    private let manager = CLLocationManager()

    func request() {
        switch manager.authorizationStatus {
        case .notDetermined: manager.requestWhenInUseAuthorization()
        case .denied, .restricted: /* guida l'utente alle Impostazioni */
        default: /* già autorizzato, si parte */
        }
    }
}

// 3. Dopo il rifiuto, degrada con eleganza: avviso + apertura Impostazioni
// UIApplication.shared.open(URL(string: UIApplication.openSettingsURLString)!)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attenzione: la "singola occasione" dei permessi iOS

{class="mt-1"}
L'avviso dei permessi su iOS compare una volta sola — se l'utente rifiuta, non ricomparirà mai più. Quindi: scegli il momento della richiesta "nell'attimo in cui l'utente sta per usarla" (non una raffica di avvisi all'avvio) e spiega nel testo lo scopo. La guida nell'interfaccia dopo il rifiuto ("vai nelle Impostazioni ad attivare la posizione") è di serie: non lasciare l'utente intrappolato in un vicolo cieco.
:::

#### 2. Notifiche: dire cose utili al momento giusto

Le notifiche sono il canale con cui l'app raggiunge l'utente, e anche la funzione più facilmente "messa alla lista nera". Su iOS si usa il framework UserNotifications; tre regole d'oro: manda solo cose utili, lascia l'utente libero di disattivarle, non disturbare a notte fonda. Uso di base:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Notifiche locali</span><span class="dots">···</span>
:::

```
import UserNotifications

// 1. Richiedi il permesso di notifica (un dialogo una tantum)
UNUserNotificationCenter.current()
    .requestAuthorization(options: [.alert, .sound, .badge]) { granted, _ in
        print(granted ? "autorizzato" : "negato")
    }

// 2. Pianifica un "promemoria spese ogni giorno alle 20:00"
func scheduleDailyReminder() {
    let content = UNMutableNotificationContent()
    content.title = "Promemoria spese"
    content.body = "Oggi non hai ancora registrato spese"
    content.sound = .default

    var comps = DateComponents()
    comps.hour = 20
    let trigger = UNCalendarNotificationTrigger(dateMatching: comps, repeats: true)

    let request = UNNotificationRequest(
        identifier: "daily-reminder",
        content: content,
        trigger: trigger
    )
    UNUserNotificationCenter.current().add(request)
}
```
:::

Attenzione: anche il permesso delle notifiche su iOS "compare una volta sola", e l'utente può disattivarlo in qualunque momento dalle Impostazioni di sistema — per questo il valore percepito del contenuto è fondamentale: un abuso, anche una volta sola, può farti perdere l'utente per sempre.

#### 3. Architettura di livello avanzato: MVVM a fondo e testabilità

Al capitolo 65 abbiamo già usato MVVM; qui aggiungiamo tre punti di livello avanzato:

- Astrazione tramite protocolli: fai dipendere il ViewModel da protocolli (protocol) e non da classi concrete — nei test puoi iniettare "fonti di dati finte", ed è la pietra angolare della testabilità;
- Responsabilità unica: un ViewModel gestisce una cosa sola (chi tiene le spese non si occupa del meteo); quando le funzioni aumentano, lo dividi;
- Niente sovraingegneria: in un piccolo progetto in solitario, "classi @Observable + astrazione tramite protocolli" basta. Architetture pesanti come VIPER o Clean Architecture aspettino che arrivino il team e la complessità — gli strumenti servono agli obiettivi, non a fare sfoggio.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consiglio: il "dividendo d'ecosistema" di SwiftUI

{class="mt-1"}
L'ecosistema iOS offre altri due "privilegi unici" di livello avanzato: i widget (WidgetKit) permettono all'utente di vedere le informazioni senza aprire l'app (la "spesa del mese" del registro delle spese direttamente sul desktop), e le scorciatoie (App Intents) permettono all'utente di invocare le tue funzioni con Siri o con le automazioni. Entrambi hanno framework ufficiali, l'ingresso non costa molto, ma il vantaggio sull'esperienza utente è enorme — sulla strada avanzata meritano lo sblocco prioritario.
:::

#### 4. Le novità del 2026: sviluppo iOS assistito dall'IA

Nel 2026 l'IA è già profondamente incorporata nel flusso di sviluppo Apple. Se vuoi accelerare, questa combinazione è molto matura:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Fase</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Come aiuta l'IA</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Il tuo compito</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Scrivere codice</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Autocompletamento integrato in Xcode + generazione con plugin IA di terze parti</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Descrivere i requisiti con chiarezza, rivedere l'output</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cercare informazioni</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Passare all'IA documentazione ufficiale e messaggi di errore da interpretare</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Verificare le conclusioni chiave sulla documentazione ufficiale</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Scrivere test</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Far generare all'IA casi di test XCTest nelle tre categorie "normale/limite/anomalo"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Confermare che i casi rispettino la semantica del dominio</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Correggere i bug</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Incollare il log del crash + il codice rilevante, l'IA localizza e corregge</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Capire le modifiche, verificare eseguendo i test</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
I quattro scenari dello sviluppo iOS assistito dall'IA

La metodologia concreta — come dare istruzioni all'IA, come accettare i risultati, come evitare le trappole — è trattata per intero negli 11 capitoli della Parte 7 di questo libro, "Programmazione pratica con l'IA" (capitoli 37-47), la cui lettura è fortemente consigliata in parallelo: la sintassi Swift sta in questa parte, i segreti della collaborazione con l'IA nella Parte 7.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mettiti alla prova: aggiungi al registro delle spese il "trio"

#### 5. Punti chiave della concorrenza Swift: @MainActor e Task

Il sistema di concorrenza di Swift 6 ha due regole che un principiante deve capire assolutamente:

- L'interfaccia si aggiorna solo sul thread principale: le viste SwiftUI sono @MainActor per impostazione predefinita; le callback di rete tornano al thread principale prima di cambiare lo stato (con await MainActor.run { ... } oppure marcando il ViewModel come @MainActor);
- Le attività asincrone si gestiscono con Task: il modificatore .task { } parte da solo quando la vista compare e si annulla da solo quando scompare — è la postura standard per avviare lavoro asincrono in SwiftUI; non scrivere Task a casaccio nel body, senza controllo.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Il pattern asincrono standard</span><span class="dots">···</span>
:::

```
struct WeatherScreen: View {
    @State private var vm = WeatherViewModel()

    var body: some View {
        Group {
            switch vm.state {
            case .loading: ProgressView()
            case .success(let d): WeatherContent(data: d)
            case .error(let m): Text(m)
            }
        }
        .task {                       // parte quando appare, si annulla quando scompare
            await vm.search(city: "Pechino")
        }
    }
}
```
:::

Dietro queste due regole c'è la "sicurezza dalle data race" di Swift 6 — il compilatore segnala l'errore appena sbagli a scrivere, invece di farti scoprirlo quando l'app crasha. Gli errori del compilatore non sono prese in giro: sono pallottole fermate al posto tuo.

{class="mt-1"}
① Aggiungi al registro delle spese "un promemoria per annotare le spese ogni giorno alle 20:00" (permesso notifiche + notifiche locali); ② trasforma la fonte dati del ViewModel in un'astrazione tramite protocollo e scrivi un test unitario che inietta dati finti; ③ aggiungi un widget da desktop "spesa del mese". Completato il trio, il tuo progetto avrà l'aspetto di un "esercito regolare".
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riepilogo del capitolo

- I tre passi dei permessi: dichiarazione nell'Info.plist (se manca, crash garantito), richiesta al momento dell'uso, dopo il rifiuto guida verso le Impostazioni
- L'avviso dei permessi iOS compare una sola volta: il momento giusto è "quando l'utente sta per usarla", e il testo deve spiegare chiaramente lo scopo
- Le tre regole delle notifiche: solo cose utili, possibilità di disattivarle, nessun disturbo; framework UserNotifications
- MVVM avanzato: astrazione tramite protocolli (testabile), responsabilità unica, niente sovraingegneria
- Dividendo d'ecosistema: widget WidgetKit + scorciatoie App Intents
- I quattro scenari assistiti dall'IA: scrivere codice, cercare informazioni, scrivere test, correggere bug; la metodologia è nella Parte 7 (capitoli 37-47)
:::
