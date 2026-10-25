---
id: di-san-shi-liu-zhang
num: 36
part: er-tong-pian
nav: Capitolo 36: Smartphone e casa intelligente — Rendi la casa più furba
toc: default
kind: chapter
---

### Capitolo 36: Telefono e casa intelligente — rendi la casa smart

{class="chapter-intro mb-4"}
Il telefono può fare una cosa sempre più importante: diventare il «telecomando» dell'intera casa. Da una lampadina a una presa, da una serratura a un sensore, la casa intelligente sta passando da «giocattolo da smanettoni» a «dotazione di casa». Questo capitolo ti aiuta a fare chiarezza su protocolli, ecosistemi, hub e kit di partenza, e si chiude con una checklist di sicurezza per non farti mordere dallo «smart».

#### 1. Protocolli della casa intelligente: la scelta conta

Prima di comprare un dispositivo smart controlla quale protocollo supporta: determina se può essere «comandato» dal tuo telefono e dal tuo ecosistema. I principali sono quattro, con caratteristiche diverse:

- Protocollo Matter: pubblicato nel 2022 dalla CSA (Connectivity Standards Alliance) con dietro Apple, Google, Amazon, Samsung e altri giganti. Unico obiettivo: far parlare tutti i dispositivi smart la stessa lingua. Nel 2023-2026 sta diventando rapidamente lo standard unificato; i dispositivi compatibili si collegano a Apple HomeKit, Google Home, Amazon Alexa e Mi Home senza restare legati a un solo ecosistema.
- Protocollo Thread: il «tubature» di rete alla base di Matter. Basso consumo, rete mesh (se un nodo cade, il segnale fa un'altra strada), risposta rapida e senza scatti. I dispositivi con router di bordo Thread (HomePod mini, Apple TV 4K, gateway Xiaomi) danno un'esperienza nettamente più stabile.
- Wi-Fi: banda ampia, connessione diretta al router, ma alto consumo e con molti dispositivi si intasa il canale; adatto a telecamere e robot aspirapolvere che trasferiscono molti dati.
- Bluetooth (BLE): configurazione semplice e risparmio energetico, ma breve distanza e niente mesh; adatto a serrature, termometri e igrometri.
- Zigbee: protocollo mesh a basso consumo storico, richiede un gateway dedicato; dispositivi economici e stabili ma scarsa interoperabilità tra marchi; sta progressivamente lasciando il posto a Matter+Thread.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
Principio in una frase

{class="mt-1"}
Nel 2026, per i dispositivi smart guarda prima il marchio «Matter over Thread»: è la scelta più resistente al tempo. I vecchi dispositivi solo Wi-Fi o Bluetooth non vanno buttati subito, usali e ai prossimi acquisti passa a Matter.
:::

#### 2. Confronto tra i tre grandi ecosistemi

Il protocollo è la «lingua», l'ecosistema è il «circolo». Anche se tutto supporta Matter, nella vita quotidiana devi scegliere un ecosistema principale per automazioni e controllo vocale. Confronto tra i tre principali:

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                    <thead>
                        <tr class="bg-light dark:bg-gray-700">
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ecosistema</th>
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Punti di forza</th>
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Punti deboli</th>
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Per chi</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple HomeKit</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Privacy massima (elaborazione locale), integrazione fluida con iPhone/Siri/Scorciatoie</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pochi dispositivi e costosi, serve HomePod o Apple TV come hub</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Famiglie con dispositivi Apple, attenti a privacy ed esperienza</td>
                        </tr>
                        <tr>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mi Home (Xiaomi)</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ampia gamma di dispositivi, ottimo rapporto qualità-prezzo, Xiao AI comoda</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ecosistema relativamente chiuso, molti dati su cloud, molti annunci</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Chi ha budget limitato e vuole attrezzare tutta casa in una volta</td>
                        </tr>
                        <tr>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Huawei HiLink (HarmonyOS)</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Continuità perfetta con telefono/tablet/orologio HarmonyOS, gamma di dispositivi in rapida crescita</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pochi dispositivi supportati all'estero, ecosistema ancora in recupero</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Utenti Huawei, attenti alla collaborazione multi-dispositivo «Super Device»</td>
                        </tr>
                    </tbody>
                </table>
```

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
Consigli per scegliere l'ecosistema

{class="mt-1"}
Scegli in base al telefono: utenti iPhone preferiscano HomeKit, utenti Huawei HiLink, altri Android Mi Home è il più pratico. Grazie a Matter, dispositivi di ecosistemi diversi possono essere controllati dallo stesso telefono: non devi schierarti subito.
:::

#### 3. Il telefono come hub di casa

Nella maggior parte dei casi iniziali il telefono è il tuo «hub di casa»: con l'app controlli luci, condizionatori, tende e sicurezza, e crei scenari automatici per far «muovere» la casa da sola:

- Controllo dispositivi: con HomeKit/Mi Home/Smart Life apri e spegni le luci da remoto o in locale, regola la temperatura colore, imposta l'aria condizionata, apri e chiudi le tende, guarda le telecamere.
- Scenari automatici: combina «condizione → azione»; i tre più usati: Modalità rientro: arrivo a casa + buio → accendi luce ingresso + aria condizionata + chiudi tende + chiudi serratura.
- Modalità uscita: l'ultimo che esce (posizione fuori casa o serratura chiusa) → spegni luci + aria + prese + attiva telecamere + allarme.
- Modalità notte: ogni sera alle 23:00 → spegni luci principali + chiudi tende + aria a 26 gradi + attiva lampada da notte.

- Tocco NFC: attacca un tag NFC alla porta e con un tocco del telefono attivi lo scenario (un tocco luce ingresso, un altro modalità notte). Su iPhone con le «Scorciatoie», su Android con «Wallet» o l'app del produttore.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Prova: crea una «Modalità rientro»

{class="mt-1"}
Nella sezione «Automazioni» dell'app casa intelligente creane una nuova: condizione «Arrivo a un luogo» (casa), azioni in sequenza «accendi luce ingresso» «aria a 26 gradi» «chiudi tende». Salva, esci a fare una passeggiata e al rientro guarda se le luci si accendono da sole: la soddisfazione della prima volta è meglio di comprare un nuovo dispositivo.
:::

#### 4. Kit di partenza consigliati

Non serve attrezzare tutto subito: con questi quattro elementi copri l'80% delle esigenze quotidiane:

- Altoparlante smart: Xiao AI (Mi Home, ottimo rapporto qualità-prezzo) / HomePod mini (Apple, funge da hub Thread) / Alexa (ampio ecosistema estero). Attenzione: l'altoparlante determina l'ecosistema vocale, scegli prima l'ecosistema.
- Lampadina smart: Yeelight (Mi Home/Matter, temperatura e luminosità regolabili, economica) / Philips Hue (colori belli e stabili, ma serve il gateway Hue, più costosa). Attenzione: controlla la base (E27/B22) e se serve la regolazione colore.
- Presa smart: Xiaomi Smart Plug (economica, contatore consumi) / TP-Link Kasa (ottimo supporto Matter all'estero). Attenzione: con elettrodomestici potenti (scaldabagno, stufa) controlla la potenza nominale per non sovraccaricare.
- Serratura intelligente: Loock/Xiaomi (rapporto qualità-prezzo, integrazione Mi Home) / Kaadas (produttore tradizionale, struttura meccanica solida). Attenzione: verifica il supporto Matter o del tuo ecosistema, l'autonomia della batteria e la posizione della serratura di emergenza.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
Ordine di acquisto consigliato

{class="mt-1"}
Prima l'altoparlante (fissa l'ecosistema) → poi lampadina e presa (facili, feedback immediato) → infine serratura e telecamere (sicurezza, scegli con cura). Aggiungi un tipo di dispositivo alla volta, famigliarizza e poi espandi, per non ritrovarti con cose che non sai usare.
:::

#### 5. Attenzione alla sicurezza

Più dispositivi smart, più grande la superficie di attacco. Queste quattro regole sono il minimo sindacale, controllale una per una:

1. Cambia le password predefinite: le password di fabbrica di telecamere, router e serrature sono pubbliche online; la prima cosa da fare è impostare una password «lunga e non ripetuta».
2. Aggiorna il firmware: gli aggiornamenti dei produttori spesso correggono vulnerabilità; attiva «Aggiornamento automatico» nell'app o almeno controlla una volta al mese.
3. Isolamento di rete: metti i dispositivi IoT su un Wi-Fi separato (o rete ospiti), distinto dalla rete principale di telefono e computer. Se un dispositivo viene compromesso, è più difficile che minacci lateralmente i tuoi dati importanti.
4. Protezione della privacy: sulle telecamere attiva la mascheratura delle «aree private» (camera da letto, bagno non ripresi), disattiva la registrazione cloud 24 ore; non lasciare attive a lungo le telecamere di casa ad app di terze parti.

::: div .danger-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
Errori da non commettere

{class="list-disc pl-6 mt-1 space-y-1"}
- Non usare l'«apertura da remoto» della serratura per sconosciuti: preferisci password temporanee che scadono dopo l'uso.
- Non puntare la telecamera verso il letto o fuori dalla finestra: stai esponendo la tua privacy.
- Non comprare per risparmiare dispositivi senza marca: quasi mai aggiornano il firmware e sono una porta aperta in casa.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riepilogo del capitolo

{class="list-disc pl-5 text-sm space-y-0.5"}
- Matter+Thread è la direzione unificata 2023-2026: per i nuovi dispositivi guarda prima questo marchio
- I tre ecosistemi hanno punti di forza diversi: Apple privacy ed esperienza, Mi Home rapporto qualità-prezzo, Huawei collaborazione multi-dispositivo
- Il telefono può fare da hub; con gli scenari «rientro/uscita/notte» la casa si muove da sola
- Kit iniziale: altoparlante, lampadina, presa, serratura, in quest'ordine
- Password predefinite da cambiare, firmware aggiornati, rete isolata, privacy protetta: quattro regole di sicurezza da non trascurare
:::
