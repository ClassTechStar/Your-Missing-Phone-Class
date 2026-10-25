---
id: di-er-shi-zhang-termux
part: jin-jie-pian
nav:  Appendice: Termux terminale Linux portatile
toc: sub
kind: supplement
---

### Appendice al Capitolo 20: Termux — un ambiente terminale Linux portatile su dispositivi Android

{class="chapter-intro mb-4"}
Se la modalità sviluppatore non ti sembra ancora abbastanza "hardcore" e vuoi provare una vera riga di comando Linux sul telefono, Termux fa al caso tuo. Senza permessi di root, trasforma un comune telefono Android in una workstation Linux portatile, ed è un'arma per gli utenti avanzati che vogliono esplorare sviluppo e operations su mobile.

#### 1. Che cos'è Termux

Termux è un'applicazione open source di emulatore di terminale e ambiente Linux progettata per dispositivi Android; senza permessi di root offre sul telefono un'esperienza shell Linux completa. Essendo un'app leggera (il pacchetto di installazione è di circa 30 MB), Termux supporta un ecosistema software ricco tramite il sistema di gestione pacchetti APT e permette di eseguire su dispositivo mobile strumenti come Python, Node.js, Git, SSH, persino di allestire server o di fare penetration testing.

Il vantaggio principale di Termux è la leggerezza e l'alta estendibilità, adatto a scenari di sviluppo, apprendimento e amministrazione di sistema. Integra pacchetti standard ed emulazione terminale precisa in una soluzione open source.

#### 2. Funzioni e caratteristiche principali

##### 🖥️ Ambiente Linux completo

Termux <strong>include solo Bash</strong> come shell. Per usare altre shell come Zsh o fish, occorre installarle manualmente col gestore pacchetti, ad esempio: <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install zsh</code> o <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install fish</code>. Termux supporta editor come Vim, Nano ed Emacs e offre un'esperienza a riga di comando vicina a quella nativa. Con "pkg install" si possono installare oltre 2000 pacchetti, inclusi strumenti di sviluppo e sicurezza come GCC, OpenSSH, SQLMap.

##### 📦 Gestione pacchetti potente

Usa il gestore pacchetti APT (simile a Debian e Ubuntu), consente di installare migliaia di pacchetti Linux, coprendo strumenti di sviluppo, di rete e altro. Supporta ambienti per numerosi linguaggi di programmazione: Python, Ruby, Node.js, Go, Rust, Swift, ecc.

##### 🔒 Funzioni di sicurezza e di rete

- <strong>Connessione SSH remota</strong>: supporta client e server SSH, permette di connettersi a dispositivi remoti o di far diventare il telefono un host SSH.
- <strong>Strumenti di cifratura</strong>: fornisce strumenti come OpenSSL per cifratura dati e comunicazioni sicure.
- <strong>Allestimento server</strong>: si possono configurare Nginx o Apache per allestire un server web statico.

##### 🔧 Integrazione di sistema ed estensioni

- Accesso ai permessi di archiviazione del telefono per la gestione locale dei file.
- Tramite il plugin Termux:API richiama funzioni hardware Android come sensori e fotocamera.
- Supporta tastiere Bluetooth e display esterni, con supporto completo al mouse.

#### 3. Ecosistema dei plugin

L'applicazione principale di Termux può essere estesa con alcune app plugin opzionali, che offrono funzioni e integrazioni aggiuntive:

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Nome plugin</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Descrizione funzione</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:API</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Espone le funzioni delle API Android ai programmi a riga di comando</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Boot</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Permette di eseguire script all'avvio del dispositivo</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Float</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fornisce una finestra terminale flottante</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Styling</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Abilita schemi di colore e personalizzazione dei font per il terminale</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Tasker</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Integrazione degli script Termux con l'app di automazione Tasker</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Widget</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Permette di eseguire script da un widget sulla schermata home</td>
                            </tr>
                        </tbody>
                    </table>
```

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Promemoria importante

{class="mt-1"}
Termux e i suoi plugin vanno installati dalla stessa fonte, perché condividono lo stesso sharedUserId. Installazioni miste da fonti diverse (ad esempio F-Droid e GitHub) provocano errori di installazione.
:::

#### 4. Guida all'installazione e alla configurazione

##### 📥 Fasi di installazione

1. <strong>Scarica l'app</strong>: scarica e installa Termux dai canali ufficiali (F-Droid o GitHub), senza permessi di root.
2. <strong>Inizializza il sistema</strong>: al primo avvio attendi il completamento di "Installing bootstrap packages".
3. <strong>Ottieni i permessi di archiviazione</strong>: esegui <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-setup-storage</code> per ottenere i permessi sul file system del telefono.
4. <strong>Aggiorna i repository</strong>: esegui <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code> per aggiornare l'elenco dei pacchetti.

##### ⚙️ Ottimizzazioni di base

- <strong>Cambio mirror</strong>: usa il comando <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-change-repo</code> per cambiare mirror tramite interfaccia grafica (consigliato il mirror dell'Università Tsinghua).
- <strong>Scorciatoie da tastiera</strong>: il tasto volume giù simula Ctrl, il volume su simula Esc, per migliorare l'efficienza di input.
- <strong>Personalizzazione interfaccia</strong>: installa Zsh + Oh My Zsh, configura temi e plugin.

#### 5. Scenari applicativi tipici

##### 💻 Sviluppo e test su mobile

Allestisci sul telefono un ambiente di sviluppo completo, scrivi ed esegui script Python, usa GCC per compilare programmi C, gestisci repository di codice con Git, sincronizzati con server remoti tramite SSH.

##### 🖥️ Operations dei server

Gestisci da remoto i server tramite SSH, esegui manutenzione di sistema, analisi dei log e altri compiti, per occuparti dei problemi del server in qualsiasi momento e luogo.

##### 📚 Apprendimento di Linux

Offre un ambiente Linux reale, una piattaforma ideale per imparare la riga di comando e l'amministrazione di sistema; puoi esercitarti con la scrittura di script Shell, la gestione dei permessi dei file Linux (ad esempio <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chmod 755</code> per impostare i permessi rwxr-xr-x, <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chown user:group</code> per modificare il proprietario del file, <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls -l</code> per vedere i nove bit di permesso dei tre gruppi owner/group/other) e altri comandi di base. Nota: questo è il classico modello di permessi "tre gruppi da nove bit" di Unix/Linux (owner / group / other × lettura / scrittura / esecuzione), un sistema completamente diverso dalle ACL di Windows NTFS.

##### 🔐 Test di sicurezza di rete

Installa strumenti di sicurezza come Nmap, SQLMap, Hydra, Metasploit per scansioni di rete e penetration test.

#### 6. Versioni e compatibilità

L'ultima versione stabile di Termux è la v0.118.2, per dispositivi con Android ≥ 7. Si noti che Termux può presentare instabilità su Android 12 e versioni successive; si consiglia di seguire il changelog ufficiale per le informazioni più aggiornate sulla compatibilità.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>In sintesi

{class="mt-1"}
Termux porta la potente esperienza del terminale Linux sui dispositivi Android e trasforma il telefono in uno strumento portatile di sviluppo e apprendimento. Che tu sia uno sviluppatore, un amministratore di sistema o un appassionato di tecnologia, con Termux puoi godere di un'esperienza a riga di comando completa su dispositivo mobile, realizzando l'idea di un "Linux in tasca".
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Prova: esegui il tuo primo comando Linux sul telefono

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Scarica e installa Termux da F-Droid, attendi il completamento dell'inizializzazione al primo avvio.
2. Esegui <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code> per aggiornare i pacchetti.
3. Installa Python: <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install python</code>.
4. Digita <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python3 -c "print('Hello from Termux!')"</code> e goditi la sensazione di eseguire codice sul telefono.
:::
