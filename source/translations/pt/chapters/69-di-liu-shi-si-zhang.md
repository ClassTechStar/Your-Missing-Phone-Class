---
id: di-liu-shi-si-zhang
num: 64
part: ios-kai-fa-pian
nav: Capítulo 64: Armazenamento de dados e requisições de rede
toc: default
kind: chapter
---

### Capítulo 64: Armazenamento de dados e requisições de rede

{class="chapter-intro mb-4"}
Um app que só “mostra” está morto; app de verdade é o que guarda dados e se conecta à rede. Neste capítulo você vai conhecer o “trio” da camada de dados do iOS: UserDefaults (para pequenas configurações), SwiftData (para dados estruturados) e URLSession (para conversar com servidores), além do Codable para interpretar JSON e do moderno async/await. Com este capítulo dominado, você já escreve apps de verdade, que lembram os hábitos do usuário e atualizam conteúdo em tempo real.

#### 1. Como escolher a solução de armazenamento: comece por esta tabela

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Solução</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">O que guarda bem</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Características</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Onde usamos no livro</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Configurações esparsas (interruptores, preferências)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pares chave-valor, simples e direto</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ajustes do Capítulo 65, cidades favoritas do Capítulo 66</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dados estruturados (lançamentos, registros)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Encapsulamento do banco oficial; declaração em uma linha com @Model</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lançamentos do Capítulo 65</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">(não armazena, busca na rede) Dados do servidor</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Framework de rede nativo, sem dependência de terceiros</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dados de clima do Capítulo 66</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
A divisão de trabalho do trio de dados

Grave uma máxima: “configuração pequena vai para o UserDefaults, dados em lote vão para o SwiftData, e dados de fora chegam pelo URLSession”. O Core Data dos tutoriais antigos ainda funciona (o SwiftData é o seu casaco moderno), e SQLite escrito à mão você praticamente não vai tocar — aprenda o novo e não trilhe o caminho velho.

#### 2. UserDefaults: guardando pequenas configurações

::: div .code-block
:::inline div .code-head
<span>SWIFT · Exemplo de UserDefaults</span><span class="dots">···</span>
:::

```
// Escrita: salvar um valor
UserDefaults.standard.set(true, forKey: "isDarkMode")
UserDefaults.standard.set("Pequim", forKey: "favoriteCity")

// Leitura: pegar o valor (se não houver, retorna o padrão)
let isDark = UserDefaults.standard.bool(forKey: "isDarkMode")
let city = UserDefaults.standard.string(forKey: "favoriteCity") ?? "Pequim"

// Exclusão: remover uma chave
UserDefaults.standard.removeObject(forKey: "isDarkMode")
```
:::

Lembre que ele só serve para configurações pequenas e esparsas — dezenas ou centenas de registros devem ir para o SwiftData; não trate o UserDefaults como banco de dados (isso deixa o app lento para abrir e dificulta consultas).

#### 3. SwiftData: dando aos dados uma “casa de verdade”

O SwiftData é a solução oficial de banco de dados desde o iOS 17, e simplifica ao máximo “criar tabelas e fazer CRUD” — com uma única anotação @Model, a classe de dados vira uma tabela do banco:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Exemplo de SwiftData</span><span class="dots">···</span>
:::

```
import SwiftData

// 1. @Model: esta classe vira automaticamente uma "tabela"
@Model
class Record {
    var amount: Double
    var category: String
    var note: String
    var date: Date

    init(amount: Double, category: String, note: String, date: Date) {
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date
    }
}

// 2. Anexar o contêiner na entrada do app
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: Record.self)   // banco pronto
    }
}

// 3. Nas views, leia com @Query e escreva com @Environment
struct RecordListView: View {
    @Query(sort: \Record.date, order: .reverse) var records: [Record]
    @Environment(\.modelContext) private var context

    var body: some View {
        List(records) { r in
            Text("\(r.category) \(r.amount) yuan")
        }
    }

    func add(amount: Double, category: String) {
        let r = Record(amount: amount, category: category, note: "", date: Date())
        context.insert(r)     // insere
        try? context.save()   // grava no disco
    }
}
```
:::

Esse molde “@Model + modelContainer + @Query” pode ser copiado integralmente para qualquer projeto seu — basta trocar os nomes dos campos. Quando os dados mudam, o @Query atualiza a interface sozinho. É uma delícia.

#### 4. Codable: “traduzindo” o JSON

A maior parte dos dados dos servidores vem em JSON. O protocolo Codable do Swift faz a conversão “JSON ⇄ struct” acontecer sozinha — se os nomes dos campos casam, a mágica funciona:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Analisar JSON com Codable</span><span class="dots">···</span>
:::

```
// JSON: {"name":"Pequim","main":{"temp":26.5},"weather":[{"description":"Ensolarado"}]}
struct WeatherResponse: Codable {
    let name: String
    let main: Main
    let weather: [Weather]
}
struct Main: Codable { let temp: Double }
struct Weather: Codable { let description: String }

// String JSON → struct
let decoder = JSONDecoder()
let data = jsonString.data(using: .utf8)!
let result = try decoder.decode(WeatherResponse.self, from: data)
print(result.weather[0].description)   // "Ensolarado"
```
:::

Regra de ferro: olhe o JSON real retornado antes de definir os campos. Muitos bugs de “falha na conversão” vêm de nome de campo errado ou tipo chutado errado (o servidor manda a string “26.5” e você declara Double) — imprima o JSON original e compare: dez segundos e você acha o problema.

#### 5. URLSession + async/await: conversando com o servidor

Para se conectar, o iOS usa o URLSession nativo do sistema; combinado com o async/await do Swift (funções assíncronas), “esperar a rede” fica tão natural quanto “esperar a encomenda chegar”:

::: div .code-block
:::inline div .code-head
<span>SWIFT · URLSession + async/await</span><span class="dots">···</span>
:::

```
struct WeatherService {
    // Funções assíncronas: async marca "preciso esperar um pouco", throws marca "pode falhar"
    func fetchWeather(city: String) async throws -> WeatherResponse {
        let url = URL(string:
            "https://api.example.com/weather?city=\(city)")!
        let (data, _) = try await URLSession.shared.data(from: url)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}

// Local da chamada (dentro de .task):
.task {
    do {
        let weather = try await service.fetchWeather(city: "Pequim")
        // atualiza a tela...
    } catch {
        print("Algo deu errado: \(error)")
    }
}
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Alerta antiprejuízo: duas regras de ferro da rede

{class="mt-1"}
① Acesso à rede é sempre com async/await, nunca bloqueando a thread principal — travar a interface é uma experiência de desejar desinstalar. A concorrência estruturada do Swift torna isso natural, mas não esqueça do try await e do do/catch. ② O ATS proíbe HTTP sem criptografia por padrão: o iOS exige HTTPS. Para testar serviços locais em http://, é preciso abrir uma exceção temporária no Info.plist (NSAppTransportSecurity), mas o produto final deve ser 100% HTTPS — a revisão da Apple fica de olho nisso.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mãos à obra: crie um miniapp “frase do dia”

#### 6. Erros de rede também precisam de “classificação”: não jogue toda falha no colo do usuário

Sem internet, tempo esgotado, 404, erro 500 do servidor... erros diferentes pedem mensagens diferentes para o usuário:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Tratamento de erros por nível</span><span class="dots">···</span>
:::

```
func friendlyMessage(_ error: Error) -> String {
    if let urlError = error as? URLError {
        switch urlError.code {
        case .notConnectedToInternet: return "A rede caiu — conferir a conexão?"
        case .timedOut:               return "Tempo limite esgotado — tentar de novo depois?"
        case .cannotFindHost:         return "Servidor não encontrado"
        default:                      return "Problema de rede: \(urlError.code)"
        }
    }
    if let d = error as? DecodingError {
        return "Formato de dados inesperado (a API pode ter mudado)"
    }
    return "Algo deu errado: \(error.localizedDescription)"
}
```
:::

Mostre ao usuário “linguagem humana” e guarde a “mensagem original” para o log (imprima o error completo). Não jogue no colo do usuário aquele inglês enigmático do error.localizedDescription — o toque de produto mora nesses detalhes.

{class="mt-1"}
Procure uma API gratuita de citações (algo como hitokoto), use URLSession + async/await para buscar a “frase do dia”, exiba-a no centro da tela e adicione um botão “Outra frase”. Depois, salve as frases favoritas numa “coleção” com SwiftData. Esse exercício usa UserDefaults/SwiftData/Codable/URLSession todos de uma vez — terminando-o, os capítulos 7 e 8 serão moleza.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumo do capítulo

- A máxima: configuração pequena no UserDefaults, dados em lote no SwiftData, dados de fora pelo URLSession
- Os três golpes do SwiftData: @Model declara a tabela, modelContainer anexa o contêiner, @Query lê e context.insert escreve
- O Codable “traduz” o JSON sozinho: se os campos casam, a mágica funciona
- URLSession + async/await: conectar é como esperar a encomenda; o do/catch trata as falhas
- Duas regras de ferro: não bloqueie a thread principal; produto final exige HTTPS (ATS)
:::
