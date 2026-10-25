---
id: di-wu-shi-wu-zhang
num: 55
part: an-zhuo-kai-fa-pian
nav: Capítulo 55: Projeto 2 — App de previsão do tempo (versão em rede)
toc: default
kind: chapter
---

### Capítulo 55: Projeto 2 — App de consulta de clima (versão conectada)

{class="chapter-intro mb-4"}
O controle de gastos é 'treinar o fundamento'; o App de clima é 'ver o mundo' — ele precisa lidar com a internet. Neste projeto você vai aprender: pedir uma API gratuita, fazer parsing de JSON, tratar os três estados de interface 'carregando/sucesso/erro' e como esconder bem a chave da API. Ao terminá-lo, você terá a capacidade de fazer qualquer 'App conectado' — notícias, câmbio, tradução; a receita é a mesma.

#### 1. Pedindo uma API de clima gratuita

Para estudo individual, recomendo o OpenWeatherMap ou, na China, a QWeather — ambas têm cota gratuita e funcionam assim que você se cadastra. Usando o OpenWeatherMap como exemplo:

1. Crie a conta → na página API keys, gere uma chave (apikey);
2. O plano gratuito permite chamar o endpoint Current Weather (clima atual): api.openweathermap.org/data/2.5/weather? q=beijing&appid=SUA_CHAVE&units=metric;
3. Teste primeiro no navegador para ver como é o JSON que volta — esse 'preparo' é obrigatório antes de integrar qualquer API.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Alerta de armadilha: a chave jamais pode ficar escrita no código

{class="mt-1"}
A API Key é como a 'senha da sua carteira': colocada no código e enviada ao GitHub, em poucas horas os crawlers já a terão varrido para uso fraudulento. O jeito certo: coloque-a em local.properties (arquivo já ignorado pelo gitignore) e leia-a no código via buildConfig do Gradle. Pesquise 'melhores práticas para ocultar a API Key no Android' e siga as instruções.
:::

#### 2. Camada de rede: Retrofit + parsing de JSON

Primeiro defina o 'modelo de dados' conforme o JSON que a API devolve, ignorando todos os campos que não casam:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Modelo de dados + interface</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"Ensolarado"}],"main":{"temp":26.5,"humidity":40},"name":"Pequim"}
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
        @Query("lang") lang: String = "pt"
    ): WeatherResponse
}
```
:::

O Gson enche esses data class com o JSON automaticamente — com os nomes dos campos iguais, a mágica acontece sozinha.

#### 3. Os três estados de interface: carregando / sucesso / erro

A alma de um App conectado está no 'gerenciamento de estados'. Rede lenta, internet caindo, nome de cidade errado... em cada caso, a interface precisa dar uma resposta ao usuário. Represente isso com elegância usando um sealed class (classe selada):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Estado da interface</span><span class="dots">···</span>
:::

```
sealed class UiState {
    object Loading : UiState()                    // carregando
    data class Success(val data: WeatherResponse) : UiState()  // sucesso
    data class Error(val message: String) : UiState()          // errore
}

// No ViewModel:
fun search(city: String) {
    viewModelScope.launch {
        _state.value = UiState.Loading
        _state.value = try {
            UiState.Success(api.getWeather(city))
        } catch (e: Exception) {
            UiState.Error("Não encontrei essa cidade — tentar outro nome?")
        }
    }
}

// Na tela:
when (val s = state) {
    is UiState.Loading -&gt; CircularProgressIndicator()   // carregando
    is UiState.Success -&gt; WeatherContent(s.data)        // exibe
    is UiState.Error -&gt; Text(s.message)                 // erro
}
```
:::

Esse formato em três partes Loading/Success/Error é o 'modelo curinga' das interfaces conectadas: memorize-o e, depois, copie a fórmula em todos os Apps conectados que fizer.

#### 4. Código de interface na prática: desenhando o clima

Com os estados prontos, a interface fica assim (trechos principais):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Tela do tempo (trecho principal)</span><span class="dots">···</span>
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
            data.weather.firstOrNull()?.description ?: "Desconhecido",
            fontSize = 20.sp,
            color = Color.Gray
        )
        Spacer(Modifier.height(16.dp))
        Row {
            Text("💧 Umidade ${data.main.humidity}%")
            Spacer(Modifier.width(24.dp))
            Text("🌡️ Sensação ${data.main.temp}°C")
        }
    }
}
```
:::

Alguns detalhes que valem a pena aprender: firstOrNull() pega o primeiro elemento com segurança (a lista pode estar vazia) e ?: "Desconhecido" oferece um texto de reserva — o princípio da null safety vale na interface também. A temperatura usa fonte grande de 72.sp para dar presença, e o peso 'leve' (Light) deixa os números elegantes; essa é a receita clássica dos Apps de clima.

#### 5. Detalhes de interface e interação

- Campo de busca: TextField no topo; digite a cidade e toque em buscar (configure a ação 'buscar' no teclado — dar Enter já pesquisa);
- Cartão do clima: temperatura em fonte grande (26,5°), descrição do tempo (céu limpo), umidade e nome da cidade;
- Cidades favoritas: salve no DataStore as cidades que você consulta sempre e consulte-as automaticamente ao reabrir — de quebra, uma revisão do capítulo 6;
- Puxar para atualizar: no Compose, use o PullToRefreshBox (oferecido pelo Material 3) e a sensação fica 'profissional' na hora.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Dica: imagens dão vida à interface

{class="mt-1"}
Dê a cada tipo de clima um emoji ou ícone (☀️🌧️❄️) mapeado com when(description) — três linhas de código e o charme da interface dobra. Também dá para usar uma biblioteca de ícones de clima de terceiros, mas na fase de estudo os emojis bastam.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mãos à obra: checklist de aceitação do App de clima

{class="mt-1"}
① A busca de clima funciona normalmente; ② sem internet, o App comunica o erro com elegância sem cair (teste com o modo avião ativado!); ③ digitar uma cidade inexistente gera um aviso amigável; ④ favoritar duas cidades e, ao reiniciar o App, elas continuam lá; ⑤ girar a tela não perde o estado. Só com as cinco aprovadas o projeto se forma.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumo do capítulo

- Teste a API no navegador e entenda o JSON antes de escrever o código — 'se preparar antes' nunca dá prejuízo
- A API Key vai escondida em local.properties; jamais entra no repositório de código
- Interface Retrofit + data class: com os campos casados, o JSON é convertido automaticamente
- Os três estados Loading/Success/Error são o curinga das interfaces conectadas
- Sem internet, entrada vazia, cidade inexistente — tratar erros é a nota mínima de um App conectado
:::
