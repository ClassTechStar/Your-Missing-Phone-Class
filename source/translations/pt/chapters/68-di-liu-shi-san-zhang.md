---
id: di-liu-shi-san-zhang
num: 63
part: ios-kai-fa-pian
nav: Capítulo 63: Views, estado e navegação
toc: default
kind: chapter
---

### Capítulo 63: Views, estado e navegação

{class="chapter-intro mb-4"}
Você já sabe fazer brinquedos de uma tela só. Este capítulo resolve duas questões de “crescimento”: como pular entre várias telas (navegação) e como os dados fluem entre as telas (gerenciamento de estado). Ao terminar, você será capaz de montar o esqueleto clássico de um app com várias telas: “lista → detalhe → edição”.

#### 1. O panorama do fluxo de dados no gerenciamento de estado

O @State não é a única ferramenta de estado do SwiftUI. Primeiro, veja este panorama para entender “qual usar e quando”:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ferramenta</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cuida de quê</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Quem usa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cenário típico</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Estado temporário privado da tela</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A view atual</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Contadores, texto de campos</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Binding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pegar estado emprestado</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A view filha altera a view pai</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Componentes personalizados</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@StateObject / @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lógica compartilhada entre telas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">View model (ViewModel)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Carregamento de dados, lógica de negócio</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@EnvironmentObject / .environment</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Estado global compartilhado</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">O app inteiro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sessão do usuário, configurações de tema</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Panorama das ferramentas de estado do SwiftUI (em 2026, @Observable já é o padrão)

::: div .code-block
:::inline div .code-head
<span>SWIFT · O mainstream de 2026: view models com @Observable</span><span class="dots">···</span>
:::

```
// O jeito moderno no iOS 17+: a macro @Observable (recomendada para projetos novos)
import Observation

@Observable
class CounterModel {                 // o view model
    var count = 0
    func increment() { count += 1 }
}

struct CounterView: View {
    @State private var model = CounterModel()   // guarda o modelo

    var body: some View {
        VStack {
            Text("Você tocou \(model.count) vezes")
            Button("Toque aqui") { model.increment() }
        }
    }
}
```
:::

Conselho direto para iniciantes: para estado privado da tela, @State; para o que cruza telas ou tem lógica, classes com @Observable. O @StateObject/@ObservableObject dos tutoriais antigos é a geração anterior — saber ler basta; em código novo, siga a orientação acima.

#### 2. NavigationStack: a “pilha” de navegação entre telas

Desde o iOS 16, a navegação entre várias telas usa o NavigationStack — como uma pilha de pratos: você coloca um em cima e, ao voltar, eles saem um a um:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Navegação com NavigationStack</span><span class="dots">···</span>
:::

```
struct HomeView: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("O livro de João") {
                    DetailView(name: "O livro de João")   // tela de destino
                }
                NavigationLink("O livro de Maria") {
                    DetailView(name: "O livro de Maria")
                }
            }
            .navigationTitle("Lista de livros")   // título grande no topo
        }
    }
}

struct DetailView: View {
    let name: String
    var body: some View {
        Text("Detalhes de \(name)")
            .navigationTitle(name)
            .navigationBarTitleDisplayMode(.inline)
    }
}
```
:::

O NavigationLink é o “link de navegação clicável”; o navigationTitle gera automaticamente o título da barra de navegação e o botão de voltar. Para navegar por código (por exemplo, voltar automaticamente depois de tocar em “Salvar”), use @Environment(\.dismiss) para fechar a tela atual — com essas duas técnicas, 90% das necessidades de navegação estão cobertas.

#### 3. Janelas modais e abas inferiores: sheet e TabView

Além de “empurrar telas”, há duas interações clássicas:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Diálogos sheet + abas TabView</span><span class="dots">···</span>
:::

```
// 1. Sobe de baixo em meia tela/tela cheia (o favorito para formulários)
struct HomeView: View {
    @State private var showAdd = false
    var body: some View {
        Button("Nova entrada") { showAdd = true }
            .sheet(isPresented: $showAdd) {
                AddRecordView()     // a tela de entrada que sobe
            }
    }
}

// 2. A barra de abas inferior (o "esqueleto" do app)
struct MainTabView: View {
    var body: some View {
        TabView {
            RecordListView()
                .tabItem { Label("Livro", systemImage: "book") }
            StatsView()
                .tabItem { Label("Estatísticas", systemImage: "chart.pie") }
            SettingsView()
                .tabItem { Label("Ajustes", systemImage: "gear") }
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Dica: quando usar cada uma?

{class="mt-1"}
Regra de bolso: no fluxo principal, empurre telas com NavigationStack (lista → detalhe); para ações temporárias, use janelas sheet (adicionar, editar, confirmar); para grandes blocos equivalentes, TabView (abas inferiores). A combinação dos três é o esqueleto da grande maioria dos apps.
:::

#### 4. List: a “lista nacional” do iOS

O componente mais usado e mais com “jeitão Apple” do iOS é o List — já vem com divisórias, exclusão por arrasto e destaque ao toque:

::: div .code-block
:::inline div .code-head
<span>SWIFT · List + deslize para excluir</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var records = ["Almoço 25.5", "Metrô 6.0", "Salário +8000"]

    var body: some View {
        List {
            ForEach(records, id: \.self) { r in
                Text(r)
            }
            .onDelete { indexSet in          // deslize para a esquerda para excluir
                records.remove(atOffsets: indexSet)
            }
        }
    }
}
```
:::

Lista + NavigationLink + sheet + TabView — combinando esses quatro elementos, você já consegue montar o esqueleto completo de um app: “lista do diário financeiro → abrir o detalhe → tocar no + para abrir a janela de lançamento”. É assim que o projeto do próximo capítulo será construído.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mãos à obra: monte um “esqueleto de três telas”

#### 5. Ciclo de vida do app: primeiro plano e segundo plano

Como o ciclo de vida da Activity no Android, um app iOS também passa por estados de “nascimento, primeiro plano, segundo plano e morte”. No SwiftUI, observe pelo valor de ambiente scenePhase:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Observar transições primeiro plano/segundo plano</span><span class="dots">···</span>
:::

```
@main
struct MyApp: App {
    @Environment(\.scenePhase) private var phase

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .onChange(of: phase) { _, newPhase in
            switch newPhase {
            case .active:    print("De volta ao primeiro plano, retomando atualização")
            case .inactive:  print("Em transição (chamada / acabou de ir para o fundo)")
            case .background: print("Foi para o fundo, salvando rascunho")
            @unknown default: break
            }
        }
    }
}
```
:::

Usos típicos: atualizar dados ao voltar para o primeiro plano e salvar rascunhos ao ir para o segundo plano. O iOS é bem rigoroso com a execução em segundo plano — um app comum é suspenso (congelado) pouco depois de sair da frente, então não conte com processos pesados escondidos lá; se precisar de tarefas agendadas, use as notificações locais do Capítulo 68, e não um “app residente em segundo plano”.

{class="mt-1"}
Monte a versão com dados fictícios do esqueleto do diário financeiro: um TabView com três abas (Registros/Estatísticas/Ajustes) → a tela de registros usa List para exibir dados fictícios, e tocar numa linha abre o detalhe (NavigationStack) → o botão “+” no canto superior direito abre a janela de lançamento em sheet. Sem persistência e sem internet, só para treinar o esqueleto — com ele pronto, encher de dados reais no Capítulo 65 será um pulo.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumo do capítulo

- As quatro ferramentas de estado: @State (privado da tela), @Binding (emprestado), @Observable (lógica) e .environment (global)
- Em projetos novos, escreva view models com o macro @Observable; o @ObservableObject dos tutoriais antigos, basta saber ler
- NavigationStack empurra telas; @Environment(\.dismiss) volta por código
- Fluxo principal empurra telas, ações temporárias abrem sheet, blocos equivalentes usam TabView
- O List é a “lista nacional”: divisórias e exclusão por arrasto prontas de fábrica
:::
