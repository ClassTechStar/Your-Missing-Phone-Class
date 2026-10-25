---
id: di-er-shi-yi-zhang
num: 21
part: chao-yue-pian
nav: Capitolo 21: Reti mobili e sicurezza informatica a fondo
toc: default
kind: chapter
---

### Capitolo 21: Approfondimento su reti mobili e sicurezza dell'informazione

{class="chapter-intro mb-4"}
Ogni giorno usiamo il telefono per navigare, pagare, chattare, e ci sembra comodissimo. Ma hai mai pensato a quanto spesso le tue chat, le password di pagamento, le foto... viaggino "nude" su Internet? A dire il vero, la maggior parte delle persone non ci pensa mai, ma quando capita qualcosa — come il furto dell'account o della carta di credito — è troppo tardi per i rimpianti. In questo capitolo parliamo di come rendere la tua vita digitale meno "trasparente".

#### 1. VPN: il "mantello dell'invisibilità" nella rete

VPN sta per Virtual Private Network (rete privata virtuale). Puoi immaginarla come un tunnel sotterraneo dedicato e cifrato costruito tra casa tua e il sito che vuoi visitare. Tu cammini nel tunnel e chi sta fuori non vede cosa hai in mano né dove stai andando.

- <strong>Navigazione normale</strong>: telefono → rete pubblica → sito di destinazione. Nei router e negli switch intermedi, in qualsiasi punto qualcuno potrebbe "spiare" i dati che invii. Soprattutto sul Wi-Fi pubblico di bar e aeroporti, a dirla tutta, sei praticamente "nudo".
- <strong>Con una VPN</strong>: telefono → tunnel cifrato VPN → server VPN → sito di destinazione. I dati vengono cifrati e incapsulati; lo "spione" vede solo una sfilza di caratteri senza senso. Inoltre, il sito di destinazione vede l'indirizzo IP del server VPN, non il tuo IP reale.

A cosa serve, dunque, una VPN? In sintesi: primo, <strong>protegge la tua privacy sul Wi-Fi pubblico</strong>; secondo, <strong>aggira le restrizioni geografiche</strong> (ad esempio per contenuti disponibili solo in alcuni Paesi); terzo, <strong>impedisce al tuo operatore di rete (ISP) di registrare le tue abitudini di navigazione</strong>. Devo però avvertirti: <strong>non usare VPN gratuite!</strong> Il gratuito spesso significa che i tuoi dati sono la loro "merce". Un mio amico ha usato una VPN gratuita e il telefono ha iniziato a mostrare pubblicità inspiegabilmente; poi abbiamo scoperto che quella VPN vendeva i suoi dati di navigazione agli inserzionisti. Quindi, per scegliere una VPN: o un marchio importante a pagamento (come NordVPN, ExpressVPN), o niente.

Inoltre, la VPN non è onnipotente. Protegge solo i dati "in transito": se il sito di destinazione non è sicuro in sé, o se sul tuo telefono c'è già un malware, la VPN non ti aiuta.

#### 2. La "trappola dolce" del Wi-Fi pubblico: più pericolosa di quanto pensi

Potresti pensare: ma cosa vuoi che succeda, connettersi a un Wi-Fi gratuito? Ti racconto un fatto vero: ricercatori di sicurezza hanno fatto un esperimento in aeroporto, allestendo un hotspot chiamato "Starbucks_Free"; in meno di un'ora si sono collegate oltre un centinaio di persone. In realtà l'hotspot era stato allestito dai ricercatori e tutto il <strong>traffico non cifrato</strong> che lo attraversava — ad esempio i contenuti delle pagine HTTP che visitavi o le comunicazioni delle app senza TLS — poteva essere intercettato e letto.

Ma attenzione a una premessa fondamentale: oggi le app che usi quotidianamente, come WeChat, l'home banking e Alipay, nella stragrande maggioranza viaggiano già in HTTPS cifrato. In altre parole, anche se l'attaccante intercetta i pacchetti, vede solo caratteri senza senso e <strong>non può leggere direttamente le tue chat o la password di pagamento</strong>. Può però sapere quali siti hai visitato (il dominio); se alcune app o pagine vecchie usano ancora HTTP in chiaro, il contenuto è completamente esposto. Questo attacco si chiama "Man-in-the-Middle" (uomo in mezzo): l'attaccante "si infila" tra te e il vero router Wi-Fi. Ancora più inquietante, molti telefoni hanno l'opzione "connessione automatica a Wi-Fi noti": basta che l'attaccante chiami il suo hotspot con lo stesso nome di un Wi-Fi a cui ti sei già connesso (ad esempio "ChinaNet" o "CMCC") e il telefono si collegherà da solo.

Come difendersi? Alcuni consigli pratici:

- <strong>Riconosci HTTPS</strong>: l'indirizzo inizia con https://, la "s" in più sta per Secure. Quando visiti un sito che richiede una password, se vedi http:// (senza la s), fermati subito e non inserirle! I browser principali mostrano un avviso "non sicuro" sui siti non HTTPS: vedi questo segnale, fai attenzione.
- <strong>Disattiva la "connessione automatica"</strong>: sia su iPhone che su Android, nelle impostazioni Wi-Fi disattiva "Aggiungi automaticamente" o "Connessione automatica". Meglio toccare manualmente ogni volta che lasciar giudicare al telefono.
- <strong>Usa i dati mobili per le operazioni sensibili</strong>: bonifici, accesso all'home banking, inserimento del numero di carta d'identità... queste operazioni falle con la tua rete 4G/5G, non risparmiare sui dati.
- <strong>"Dimentica" i Wi-Fi che usi poco</strong>: quando torni da un viaggio o da un trasferta, "dimentica" i Wi-Fi di hotel e aeroporti collegati in passato. Così la prossima volta il telefono non si collegherà automaticamente a un falso hotspot con lo stesso nome.

#### 3. Come ti protegge HTTPS? L'handshake SSL/TLS

Ho citato HTTPS, ma come funziona davvero? Ogni volta che visiti un sito HTTPS, tra il browser e il server avviene un "handshake SSL/TLS"; il processo è più o meno così:

1. Il tuo browser dice: "Ehi server, voglio comunicare in modo sicuro, ecco l'elenco delle mie capacità di cifratura (gli algoritmi supportati, ecc.)."
2. Il server risponde: "Ok, dal tuo elenco ho scelto questa suite di cifratura; ecco il mio certificato digitale, contiene la mia chiave pubblica ed è firmato da tale CA".
3. Il browser verifica l'autenticità del certificato: è stato emesso da una CA affidabile? È scaduto? Il nome di dominio corrisponde?
4. Una volta verificato, le due parti concordano con la cifratura a chiave pubblico una "chiave di sessione"; da quel momento tutta la comunicazione viene cifrata con questa chiave.

È come andare in banca: consegni la carta d'identità (il certificato), l'impiegato verifica la tua identità, poi concordate una parola d'ordine e la conversazione successiva la capite solo voi due. Anche se qualcuno ascolta, sente solo caratteri cifrati senza senso.

Ma attenzione: HTTPS garantisce solo che il "trasferimento" sia cifrato, non che il sito di destinazione sia una persona perbene. Anche i siti di phishing possono usare HTTPS — quel lucchetto indica solo che ti sei collegato a "un sito", non che sia quello che volevi. Quindi verifica tu stesso che l'indirizzo sia corretto.

#### 4. Sicurezza DNS: la tua "rubrica telefonica di rete" è sicura?

Il DNS (Domain Name System) è come la rubrica telefonica di Internet: digiti "baidu.com" e il DNS ti restituisce l'indirizzo IP corrispondente (ad esempio 110.242.68.66), così il browser può connettersi. Il problema è che le tradizionali query DNS sono in <strong>chiaro</strong>, <strong>non cifrate</strong>! In pratica, il tuo ISP, il provider Wi-Fi o qualsiasi nodo intermedio può vedere quali siti hai visitato.

Ancora peggio è il "DNS hijack": l'attaccante manipola il DNS e fa puntare "baidu.com" a un sito di phishing falso. Tu digiti l'indirizzo corretto, ma vieni portato a una pagina di login identica all'originale ma in realtà falsa; basta inserire account e password ed è finita.

Per fortuna oggi esistono soluzioni DNS cifrate:

- <strong>DNS over HTTPS (DoH)</strong>: nasconde le query DNS nel traffico HTTPS, mescolandole al normale traffico di navigazione: è impossibile distinguere quali siano le query DNS.
- <strong>DNS over TLS (DoT)</strong>: usa il protocollo TLS per proteggere specificamente le query DNS, con porta dedicata; l'amministratore di rete può sapere che usi DoT ma non può vedere il contenuto.

Personalmente consiglio di usare come server DNS Cloudflare 1.1.1.1 o Google 8.8.8.8: entrambi supportano DNS cifrati. Su Android, nelle impostazioni "DNS privato" basta inserire "one.one.one.one" oppure "dns.google", semplicissimo. Su iPhone è leggermente più macchinoso, serve installare un profilo di configurazione o usare un'app, ma ne vale la pena.

#### 5. La "navigazione in incognito" rende davvero invisibili?

Prima la conclusione: <strong>la modalità in incognito è la tenda di casa tua, non un mantello dell'invisibilità.</strong>

Cosa fa: non lascia tracce in locale — quando chiudi la finestra in incognito, il browser non salva la cronologia di navigazione, i cookie, i dati inseriti nei moduli o le ricerche. Se devi cercare qualcosa sul computer di un altro o vuoi fare un regalo senza che i familiari lo scoprano dalla cronologia, usare la modalità in incognito è appropriato.

Cosa non fa:

- Il sito che visiti <strong>continua a vederti arrivare</strong>: il tuo indirizzo IP, le informazioni sul dispositivo e il comportamento di navigazione sono chiari lato sito.
- Il tuo operatore di rete <strong>continua a vedere quali siti hai visitato</strong>, solo che non può vedere il contenuto specifico (se usi HTTPS).
- L'amministratore di rete dell'azienda o della scuola <strong>può comunque monitorare</strong> la tua navigazione.
- I file che scarichi e i segnalibri che aggiungi <strong>restano</strong>, non spariscono chiudendo la finestra.

Quindi ricorda: la modalità in incognito è un "cancellatore locale", non un "mantello di rete". Se vuoi davvero nascondere le tracce di navigazione, devi ricorrere a combinazioni come VPN + browser Tor; per l'uso quotidiano, però, sapere questo basta.

#### 6. Privacy del browser: non lasciare che il browser ti venda

Forse non te ne accorgi, ma il browser in sé è un grande raccoglitore di informazioni. Cookie, cronologia, cache, compilazione automatica, permessi di posizione... ciascuno può far trapelare la tua privacy. Alcuni consigli:

- <strong>Pulisci periodicamente i dati di navigazione</strong>: di tanto in tanto vai nelle impostazioni e cancella cookie, cache e cronologia. Non è tanto per "evitare il tracciamento" — pulire i cookie ormai serve a poco — quanto per evitare che il telefono diventi sempre più lento. La cache del browser può occupare diversi GB.
- <strong>Lascia da parte le illusioni del "Non tracciare"</strong>: l'opzione "Invia richiesta 'Do Not Track'" del browser è in pratica una "preghiera" di non essere tracciato. Ma se il sito ti dà retta è un'altra storia; la maggior parte dei siti la ignora. Non farci affidamento.
- <strong>Usa browser privacy-friendly</strong>: Firefox Focus, DuckDuckGo Browser, Brave bloccano per impostazione predefinita tracker e pubblicità, molto più puliti dei default di Chrome e Safari.
- <strong>Anche il motore di ricerca conta</strong>: usa DuckDuckGo invece di Baidu/Google: non registra la cronologia delle ricerche e non costruisce un profilo utente. A dire il vero i risultati sono meno precisi di Google, ma per consultazioni quotidiane basta.
- <strong>Controlla i permessi delle app</strong>: vai nelle impostazioni del telefono e verifica quali permessi ha il tuo browser. Ha davvero bisogno di accedere a posizione, microfono, contatti? Probabilmente no.

#### 7. Lista di sicurezza pratica: proteggiti a partire da ora

Tante chiacchiere, in conclusione ti do una lista di sicurezza semplice e diretta: mezz'ora di lavoro e la sicurezza del tuo telefono farà un salto di qualità:

1. <strong>Disattiva la connessione Wi-Fi automatica</strong>: su iPhone in Impostazioni - Wi-Fi, su Android nelle impostazioni Wi-Fi.
2. <strong>Cambia con un DNS cifrato</strong>: su Android imposta il DNS privato a "dns.google", su iPhone usa un'app o un profilo di configurazione per il DoH di 1.1.1.1.
3. <strong>Attiva l'autenticazione a due fattori (2FA)</strong>: WeChat, Alipay, Apple ID, account Google: attiva la 2FA dove possibile. Il codice SMS è già il livello minimo di 2FA; ancora meglio usare TOTP (come Google Authenticator, Microsoft Authenticator).
4. <strong>Controlla tutti i permessi delle app</strong>: passa in rassegna i permessi di ogni app, in particolare posizione, contatti, SMS, microfono e fotocamera. Scoprirai che alcune app torcia chiedono l'accesso ai contatti: disinstallale subito.
5. <strong>Pulisci regolarmente i dati del browser</strong>: imposta un promemoria in calendario, una volta al mese, pulisci cache e cookie.
6. <strong>Non usare i cavi delle colonnine di ricarica pubbliche</strong>: la porta USB carica e trasmette dati; una colonna malevola (chiamata "Juice Jacking") può rubare dati mentre ricarichi. Porta con te il tuo alimentatore e il tuo cavo.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Fallo ora: fai un "check-up di sicurezza" al tuo telefono

{class="list-decimal pl-6 mt-1 space-y-1"}
1. <strong>Upgrade DNS</strong>: Android: Impostazioni > Connessione e condivisione > DNS privato > inserisci "one.one.one.one" o "dns.google". iPhone: cerca con Safari "1.1.1.1 DNS profile" e installa il profilo, oppure scarica l'app 1.1.1.1 di Cloudflare.
2. <strong>Audit Wi-Fi</strong>: apri l'elenco Wi-Fi e "dimentica" gli hotspot sconosciuti, poco usati o con nomi strani.
3. <strong>Pulizia permessi</strong>: entra in Impostazioni > Privacy/Gestione permessi, esamina i permessi app per app. Segna le app con richieste non ragionevoli (ad esempio la calcolatrice che vuole i contatti) e valuta di disinstallarle o sostituirle.
4. <strong>Verifica la sicurezza dell'account</strong>: apri la pagina di sicurezza dell'Apple ID o dell'account Google, controlla accessi da dispositivi sconosciuti, conferma che la 2FA sia attiva e verifica che i contatti di ripristino siano affidabili.
:::
