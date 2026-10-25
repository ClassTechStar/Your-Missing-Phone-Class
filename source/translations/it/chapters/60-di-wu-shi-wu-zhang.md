---
id: di-wu-shi-wu-zhang
num: 55
part: an-zhuo-kai-fa-pian
nav: Capitolo 55: Progetto 2 — App meteo (versione in rete)
toc: default
kind: chapter
---

### Capitolo 55: Progetto 2 — l'app del meteo (versione in rete)

{class="chapter-intro mb-4"}
Il registro delle spese è «ginnastica interna», l'app del meteo è «aprirsi al mondo» — deve trattare con internet. In questo progetto imparerai: richiedere un'API gratuita, fare il parsing del JSON, gestire i tre stati dell'interfaccia «caricamento / successo / errore» e come nascondere bene la chiave API. Completandolo avrai la capacità di realizzare qualunque «app connessa» — notizie, tassi di cambio, traduzioni: lo schema è sempre lo stesso.

#### 1. Richiedere un'API meteo gratuita

Per esercitarsi da soli, ti consiglio OpenWeatherMap oppure QWeather (il «meteo del vento armonioso», molto usato in Cina) — entrambe hanno una quota gratuita, basta registrarsi. Prendiamo OpenWeatherMap come esempio:

1. Registrati → nella pagina API keys genera una Key (apikey);
2. Il piano gratuito può chiamare l'interfaccia Current Weather (meteo attuale): api.openweathermap.org/data/2.5/weather? q=beijing&appid=LA_TUA_KEY&units=metric;
3. Prima provala una volta nel browser, per vedere com'è fatto il JSON restituito — è la «preparazione» da fare sempre prima di collegare qualunque API.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attenzione alle trappole: la chiave non va mai scritta a mano nel codice

{class="mt-1"}
La API Key è come la «password del tuo portafoglio»: se la scrivi nel codice e lo mandi su GitHub, entro poche ore i crawler la scandagliano e la usano al posto tuo. La strada giusta: mettila in local.properties (un file già ignorato da gitignore) e leggila nel codice attraverso il buildConfig di Gradle. Cerca «best practice per nascondere le API Key su Android» e segui la guida.
:::

#### 2. Il livello di rete: Retrofit + parsing del JSON

Prima definisci il «modello dati» sul calco del JSON restituito dall'API; i campi che non corrispondono si ignorano senza pietà:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Modello dati + interfaccia</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"Sereno"}],"main":{"temp":26.5,"humidity":40},"name":"Pechino"}
data class WeatherResponse(
    val weather: List&lt;Weather&gt;,
    val main: Main,
    val name: String
)
data class Weather(val description: String)
data class Main(val temp: Double, val humidity: Int)

interface WeatherApi {
    @GET("data/2.5/weather")
    suspend fun getWeather(
        @Query("q") city: String,
        @Query("appid") key: String,
        @Query("units") metric: String = "metric",
        @Query("lang") lang: String = "it"
    ): WeatherResponse
}
```
:::

Gson infila da solo il JSON dentro queste data class — se i nomi dei campi coincidono, la magia avviene da sola.

#### 3. I tre stati dell'interfaccia: caricamento / successo / errore

L'anima di un'app connessa è la «gestione degli stati». Rete lenta, rete assente, nome della città sbagliato... in ogni situazione l'interfaccia deve rendere conto all'utente. Si rappresenta con eleganza con una sealed class (classe sigillata):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Stato dell'interfaccia</span><span class="dots">···</span>
:::

```
sealed class UiState {
    object Loading : UiState()                    // spinner in rotazione
    data class Success(val data: WeatherResponse) : UiState()  // successo
    data class Error(val message: String) : UiState()          // errore
}

// Nel ViewModel:
fun search(city: String) {
    viewModelScope.launch {
        _state.value = UiState.Loading
        _state.value = try {
            UiState.Success(api.getWeather(city))
        } catch (e: Exception) {
            UiState.Error("Città non trovata — provare con un altro nome?")
        }
    }
}

// Nell'interfaccia:
when (val s = state) {
    is UiState.Loading -&gt; CircularProgressIndicator()   // spinner
    is UiState.Success -&gt; WeatherContent(s.data)        // mostra
    is UiState.Error -&gt; Text(s.message)                 // errore
}
```
:::

Questo schema a tre stadi Loading/Success/Error è il «modello tuttofare» delle interfacce connesse: prima imparalo a memoria, poi per ogni futura app connessa non ti resta che seguirne il calco.

#### 4. Il codice d'interfaccia sul campo: disegnare il meteo

Con gli stati pronti, l'interfaccia si presenta così (frammenti chiave):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Schermata meteo (brano essenziale)</span><span class="dots">···</span>
:::

```
@Composable
fun WeatherContent(data: WeatherResponse) {
    Column(
        Modifier.fillMaxSize().padding(24.dp),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text(data.name, fontSize = 28.sp, fontWeight = FontWeight.Bold)
        Text(
            "${data.main.temp}°C",
            fontSize = 72.sp,
            fontWeight = FontWeight.Light
        )
        Text(
            data.weather.firstOrNull()?.description ?: "Sconosciuto",
            fontSize = 20.sp,
            color = Color.Gray
        )
        Spacer(Modifier.height(16.dp))
        Row {
            Text("💧 Umidità ${data.main.humidity}%")
            Spacer(Modifier.width(24.dp))
            Text("🌡️ Percepiti ${data.main.temp}°C")
        }
    }
}
```
:::

Qualche dettaglio da imparare: firstOrNull() prende in sicurezza il primo elemento (l'elenco potrebbe essere vuoto), ?: "sconosciuto" dà il testo di ripiego — il principio della null safety vale anche nell'interfaccia. La temperatura usa un corpo grande come 72.sp per fare figura, e il peso «leggero» (Light) rende il numero elegante: è la ricetta classica delle app meteo.

#### 5. Dettagli di interfaccia e d'interazione

- Campo di ricerca: un TextField in alto, digiti il nome della città e tocchi cerca (imposta l'azione «Cerca» sulla tastiera, Invio per cercare);
- Scheda meteo: temperatura a corpo grande (26,5°), descrizione del tempo (sereno), umidità, nome della città;
- Città preferite: salva in DataStore le città che guardi più spesso e alla prossima apertura le cerca da solo — così ripassi di passo il capitolo 6;
- Tira per aggiornare: in Compose usa PullToRefreshBox (offerto da Material 3) e la sensazione al tocco diventa subito «professionale».

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consiglio: le immagini danno vita all'interfaccia

{class="mt-1"}
Abbina a ogni tipo di meteo un emoji o un'icona (☀️🌧️❄️), mappandoli con when(description) — tre righe di codice e il calore umano dell'interfaccia raddoppia. Puoi anche caricare una libreria di icone meteo di terze parti, ma nella fase di esercizio gli emoji bastano e avanzano.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mani in pasta: la checklist di collaudo dell'app del meteo

{class="mt-1"}
① La ricerca del meteo funziona; ② stacca la rete: l'app segnala l'errore con eleganza senza bloccarsi (prova con la modalità aereo!); ③ digiti una città che non esiste e il messaggio resta gentile; ④ metti due città nei preferiti e, riavviata l'app, ci sono ancora; ⑤ ruotando lo schermo lo stato non si perde. Solo superando tutti e cinque i punti il progetto si può dire promosso.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riassunto del capitolo

- Prima prova l'API nel browser e impara a leggere il JSON, poi scrivi il codice: «prepararsi in anticipo» non è mai tempo perso
- Nascondi la chiave API in local.properties e non farla mai finire nel repository
- Interfaccia Retrofit + data class: se i campi corrispondono, il JSON si analizza da solo
- Lo schema a tre stati Caricamento/Successo/Errore è il coltellino svizzero delle schermate di rete
- Rete assente, input vuoto, città inesistente: la gestione degli errori è il voto minimo per un'app connessa
:::
