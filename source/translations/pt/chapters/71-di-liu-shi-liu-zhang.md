---
id: di-liu-shi-liu-zhang
num: 66
part: ios-kai-fa-pian
nav: Capítulo 66: Projeto 2 — App de previsão do tempo (versão em rede)
toc: default
kind: chapter
---

### Capítulo 66: Projeto 2 — App de consulta do tempo (versão conectada)

{class="chapter-intro mb-4"}
O livro-caixa serve para "treinar a base"; o App de tempo serve para "ver mundo" — ele precisa conversar com a internet. Neste projeto você vai aprender a: pedir uma API gratuita, interpretar JSON, tratar os três estados de tela "carregando/sucesso/falha" e guardar bem a chave da API. Ao terminar, você terá a capacidade de criar qualquer "App conectado" — notícias, câmbio, tradução: a receita é a mesma.

#### 1. Solicitando uma API de tempo gratuita

Para praticar individualmente, recomendamos o OpenWeatherMap ou o QWeather (serviço popular na China) — ambos têm cota gratuita e funcionam logo após o cadastro. Usando o OpenWeatherMap como exemplo:

1. Crie a conta → gere uma chave (apikey) na página API keys;
2. A versão gratuita permite chamar o endpoint Current Weather: api.openweathermap.org/data/2.5/weather? q=beijing&appid=SUA-CHAVE&units=metric;
3. Teste primeiro uma vez no navegador para ver como é o JSON retornado — essa "lição de casa" é obrigatória antes de integrar qualquer API.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Alerta de armadilha: a chave jamais deve ficar fixa no código

{class="mt-1"}
A chave de API equivale à "senha da sua carteira": se ela entrar no código e você enviar tudo ao GitHub, em poucas horas robôs de varredura já a terão roubado para uso fraudulento. O jeito certo no iOS: colocá-la no Config.xcconfig (arquivo de configuração, já ignorado pelo gitignore) e lê-la no código por meio do Info.plist. Pesquise "gerenciar chaves com xcconfig no iOS" e siga o passo a passo.
:::

#### 2. Camada de rede: URLSession + Codable

Primeiro defina o modelo conforme o JSON retornado pela API, depois escreva o serviço:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Modelo de dados + serviço</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"Ensolarado"}],"main":{"temp":26.5,"humidity":40},"name":"Pequim"}
struct WeatherResponse: Codable {
    let weather: [Weather]
    let main: Main
    let name: String
}
struct Weather: Codable { let description: String }
struct Main: Codable { let temp: Double; let humidity: Int }

struct WeatherService {
    let key: String   // lido do xcconfig

    func fetchWeather(city: String) async throws -> WeatherResponse {
        var comps = URLComponents(string: "https://api.openweathermap.org/data/2.5/weather")!
        comps.queryItems = [
            URLQueryItem(name: "q", value: city),
            URLQueryItem(name: "appid", value: key),
            URLQueryItem(name: "units", value: "metric"),
            URLQueryItem(name: "lang", value: "pt")
        ]
        let (data, _) = try await URLSession.shared.data(from: comps.url!)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}
```
:::

#### 3. Os três estados de tela: carregando / sucesso / falha

A alma de um App conectado está no "gerenciamento de estados". Rede lenta, internet caindo, nome de cidade digitado errado... em cada situação a tela precisa dar uma resposta ao usuário. Represente isso com elegância usando enum + switch:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Estado da interface</span><span class="dots">···</span>
:::

```
enum LoadState {
    case loading                  // carregando
    case success(WeatherResponse) // sucesso
    case error(String)            // errore
}

@Observable
class WeatherViewModel {
    var state: LoadState = .loading
    private let service = WeatherService(key: Config.apiKey)

    func search(city: String) async {
        state = .loading
        do {
            let data = try await service.fetchWeather(city: city)
            state = .success(data)
        } catch {
            state = .error("Não encontrei essa cidade — tentar outro nome?")
        }
    }
}

// Na tela:
switch vm.state {
case .loading: ProgressView("Carregando…")
case .success(let d): WeatherContent(data: d)
case .error(let msg): Text(msg).foregroundColor(.secondary)
}
```
:::

Esse esquema em três partes loading/success/error é o "modelo curinga" das telas conectadas: memorize-o agora e depois copie a receita em todos os Apps conectados que você fizer.

#### 4. Código de interface na prática: desenhando o tempo

::: div .code-block
:::inline div .code-head
<span>SWIFT · Tela do tempo (trecho principal)</span><span class="dots">···</span>
:::

```
struct WeatherContent: View {
    let data: WeatherResponse

    var body: some View {
        VStack(spacing: 12) {
            Text(data.name)
                .font(.title.bold())
            Text("\(Int(data.main.temp))°C")
                .font(.system(size: 76, weight: .thin))
            Text(data.weather.first?.description ?? "Desconhecido")
                .font(.title3)
                .foregroundColor(.secondary)
            HStack(spacing: 24) {
                Label("Umidade \(data.main.humidity)%", systemImage: "humidity")
                Label("Sensação \(Int(data.main.temp))°C", systemImage: "thermometer")
            }
        }
        .padding()
    }
}
```
:::

Alguns detalhes valem a pena aprender: first? pega o primeiro elemento com segurança (a lista pode estar vazia) e ?? "Desconhecido" fornece um texto de reserva; usar peso de fonte fino no número da temperatura é a receita clássica dos Apps de tempo; Label é o componente oficial de "ícone + texto", mais padronizado do que montar um HStack à mão.

#### 5. Detalhes de interação e cidades favoritas

- Campo de busca: o modificador .searchable no topo traz a interação de busca nativa do sistema; ao confirmar, ele chama vm.search;
- Cidades favoritas: salve as cidades consultadas com frequência no UserDefaults para consultá-las automaticamente na próxima abertura;
- Puxar para atualizar: .refreshable { await vm.search(...) } resolve em uma linha;
- Ícones do tempo: use Image(systemName:) mapeando pela descrição (sun.max / cloud.rain / snowflake) e a tela ganha vida na hora.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Dica: a pegadinha dos nomes de cidade em chinês

{class="mt-1"}
O OpenWeatherMap tem um suporte mediano a nomes de cidade em chinês: buscar pelo nome em caracteres chineses pode não dar resultado, enquanto "beijing" funciona normalmente. Em um produto de verdade, a solução é embutir uma tabela de mapeamento "nome da cidade → inglês/coordenadas" ou integrar um serviço de tempo local. Na fase de prática, basta suportar nomes em pinyin/inglês — não vale a pena brigar com isso.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mãos à obra: checklist de validação do App de tempo

#### 6. Como depurar requisições de rede: logs, captura de pacotes e simulação de rede lenta

Quando um App conectado dá problema, quase sempre é porque "a requisição não foi enviada corretamente" ou "a resposta não foi interpretada corretamente". Três recursos de depuração:

1. Imprimir os dados brutos: imprima String(data: data, encoding: .utf8) para ver o JSON original — nomes de campos e tipos ficam evidentes, dez vezes mais rápido do que ficar adivinhando;
2. Captura de pacotes: Proxyman (gratuito no Mac) e Charles interceptam todas as requisições e respostas do App, revelando a camada de rede como um raio-X;
3. Simular rede fraca: no menu do simulador, Features → Network Link Conditioner (ferramenta que precisa ser baixada do site para desenvolvedores) simula 3G e alta latência — e revela aquele problema de "ficar rodando eternamente".

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Dica: a requisição falhou no ATS?

{class="mt-1"}
Se a requisição falha assim que é enviada com o erro "App Transport Security", quase certamente você usou um endereço http:// em texto puro. Interfaces de produção exigem HTTPS; para depurar localmente, abra uma exceção temporária (adicione NSAllowsLocalNetworking no Info.plist) e lembre-se de limpar tudo antes de publicar.
:::

{class="mt-1"}
① A busca normal exibe o tempo; ② ao desconectar a rede, o App mostra um erro elegante sem travar (teste desligando a rede do Mac com o simulador aberto!); ③ digitar uma cidade inexistente gera um aviso amigável; ④ favoritar duas cidades e elas continuam lá após reiniciar o App; ⑤ a tela fica confortável no modo escuro. Passando nos cinco itens, o projeto se forma.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumo do capítulo

- Teste a API no navegador e entenda o JSON antes de escrever código — "estudar antes" nunca é perda
- A chave de API vai escondida no xcconfig, jamais no repositório de código
- Modelo Codable + URLSession com async/await: com os campos alinhados, o JSON se interpreta sozinho
- O esquema de estados em três partes loading/success/error é o curinga das telas conectadas
- Sem internet, entrada vazia, cidade inexistente — tratar erros é a nota mínima de um App conectado
:::
