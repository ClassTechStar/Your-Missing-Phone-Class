---
id: di-liu-shi-wu-zhang
num: 65
part: ios-kai-fa-pian
nav: Capítulo 65: Projeto 1 — Meu controle financeiro (versão local)
toc: default
kind: chapter
---

### Capítulo 65: Projeto 1 — meu diário financeiro (versão local)

{class="chapter-intro mb-4"}
Bem-vindo ao seu primeiro “projeto de verdade”. Este diário financeiro não se conecta à internet, mas tem tudo o que importa: registrar lançamentos, ver o extrato, fazer estatísticas mensais e editar ou excluir. Ao terminá-lo, você terá percorrido o ciclo completo de “dados → lógica → interface”. Não corra para copiar o código — pense primeiro, execute depois; é o nosso princípio de sempre.

#### 1. Pensando nos requisitos: cinco perguntas primeiro

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Elemento</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Resposta</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who (para quem é)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Para mim; família e amigos também</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What (o que faz)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Registrar receitas e despesas, ver o extrato, resumir por mês e por categoria</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why (por quê)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Praticar + entender para onde o dinheiro vai</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How (como fazer)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift + SwiftUI + SwiftData + MVVM, tudo local, sem back-end</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint (restrições)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Concluir em uma semana; iOS 17 no mínimo (exigência do SwiftData)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Os cinco elementos de requisitos do diário financeiro

Depois, divida em passos pequenos em que “cada passo já serve para algo”: ① camada de dados com SwiftData (guardar um lançamento); ② tela de lista (ver o extrato); ③ janela de lançamento (adicionar registros); ④ exclusão e edição; ⑤ cartão de resumo mensal. A cada passo concluído, o app já é uma “coisa utilizável”.

#### 2. Camada de dados: dando um lar aos lançamentos

Primeiro, defina como um lançamento se parece — campos suficientes, sem gula:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Record.swift (modelo)</span><span class="dots">···</span>
:::

```
import SwiftData

@Model
class Record {
    var type: String      // "income" receita | "expense" despesa
    var amount: Double    // valor (em yuan)
    var category: String  // categoria: alimentação, transporte, salário…
    var note: String      // observação (opcional)
    var date: Date        // data do registro

    init(type: String, amount: Double, category: String, note: String = "", date: Date = Date()) {
        self.type = type
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Dica: por que usar Double para o valor?

{class="mt-1"}
Apps financeiros rigorosos usam Decimal (decimais exatos) para evitar erros de ponto flutuante (o clássico problema de 0.1+0.2≠0.3). Para um projeto de treino, Double basta; se um dia você fizer um produto financeiro de verdade, lembre de trocar por Decimal ou por um “Int em centavos” — uma armadilha que inúmeros veteranos já pisaram.
:::

#### 3. MVVM: separando interface e lógica

Deixar a interface falar direto com o banco? Funciona, mas o código da tela vira um monstro comprido. A arquitetura MVVM dá um papel a cada um: a View (interface) só desenha, o ViewModel (cérebro da lógica) cuida dos dados e o Model (SwiftData) cuida do armazenamento.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View (interface SwiftUI)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel (o hub lógico @Observable)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model (camada de dados SwiftData)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 4: as três camadas do MVVM — os dados fluem em uma direção e cada camada fica no seu lugar
:::

::: div .code-block
:::inline div .code-head
<span>SWIFT · RecordViewModel.swift (esqueleto)</span><span class="dots">···</span>
:::

```
import Observation

@Observable
class RecordViewModel {
    var records: [Record] = []
    private let context: ModelContext

    init(context: ModelContext) { self.context = context }

    func load() {
        // filtro + ordenação com #Predicate do SwiftData
        let descriptor = FetchDescriptor<Record>(
            sortBy: [SortDescriptor(\.date, order: .reverse)]
        )
        records = (try? context.fetch(descriptor)) ?? []
    }

    func add(type: String, amount: Double, category: String, note: String) {
        let r = Record(type: type, amount: amount, category: category, note: note)
        context.insert(r)
        try? context.save()
        load()                       // recarrega; a tela atualiza
    }

    func delete(_ record: Record) {
        context.delete(record)
        try? context.save()
        load()
    }
}
```
:::

Na interface, use @State private var vm = RecordViewModel(...) e renderize a lista direto com vm.records — quando os dados mudam, a tela se atualiza sozinha.

#### 4. Interface: tela de lista + janela de lançamento

::: div .code-block
:::inline div .code-head
<span>SWIFT · Tela de lista de despesas (trecho principal)</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var vm: RecordViewModel
    @State private var showAdd = false

    var body: some View {
        NavigationStack {
            List {
                Section("Saldo do mês") {          // card de resumo
                    SummaryRow(records: vm.records)
                }
                Section("Lançamentos") {
                    ForEach(vm.records) { r in
                        RecordRow(record: r)
                    }
                    .onDelete { idx in
                        idx.forEach { vm.delete(vm.records[$0]) }
                    }
                }
            }
            .navigationTitle("Meu livro de despesas")
            .toolbar {
                Button { showAdd = true } label: {
                    Image(systemName: "plus")
                }
            }
            .sheet(isPresented: $showAdd) {
                AddRecordView(vm: vm)          // diálogo de entrada
            }
        }
    }
}
```
:::

Pontos-chave da janela de lançamento: o campo de valor usa o teclado .keyboardType(.decimalPad) (teclado numérico), receita/despesa usam um controle segmentado (Picker), a categoria usa um menu de seleção; ao tocar em “Salvar”, chame vm.add(...) e feche com dismiss().

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Atenção: não seja preguiçoso na validação

{class="mt-1"}
O campo de valor precisa de validação obrigatória: bloqueie valores vazios, negativos e entradas inválidas como “abc” (use Double(text); se falhar, ele devolve nil). Uma das causas mais comuns de app travando é “tratar a entrada do usuário como criança bem-comportada”. Lembre: toda entrada do usuário deve ser interrogada como suspeita.
:::

#### 5. Edição, exclusão e resumo

- Exclusão: o .onDelete do List permite apagar arrastando para o lado, com janela de confirmação (apagar sem querer é o que mais irrita usuários de apps de finanças);
- Editar: tocar em uma linha abre o pop-up de edição já preenchido com o valor original (corrigir um caractere é mais prático do que digitar tudo de novo);
- Resumo: usar filter + reduce para calcular "receitas / despesas / saldo do mês", exibidos no cartão do topo:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Cálculo dos totais mensais</span><span class="dots">···</span>
:::

```
func monthSummary(_ records: [Record]) -> (income: Double, expense: Double) {
    let cal = Calendar.current
    let monthRecords = records.filter {
        cal.isDate($0.date, equalTo: Date(), toGranularity: .month)
    }
    let income = monthRecords
        .filter { $0.type == "income" }
        .reduce(0) { $0 + $1.amount }
    let expense = monthRecords
        .filter { $0.type == "expense" }
        .reduce(0) { $0 + $1.amount }
    return (income, expense)
}
```
:::

#### 6. Validação: três níveis de verificação + dois desafios avançados

Depois de terminar o projeto, valide em três camadas "funcionalidade → casos-limite → arquitetura": dá para registrar e excluir? Os dados continuam lá após reiniciar o App (funcionalidade); digitar 0 ou um valor negativo no campo de valor faz o app travar? (casos-limite); interface e dados estão misturados? Há campos fixados no código? (arquitetura).

Depois de passar na validação da versão básica, prepare dois "pratos avançados" para você:

1. Estatísticas por categoria: adicione uma aba "Estatísticas" e use o Swift Charts para desenhar as despesas por categoria em gráfico de pizza/barras — é a biblioteca de gráficos oficial da Apple, com poucas linhas de código;
2. Sincronização com iCloud: ativar a sincronização iCloud no SwiftData exige apenas algumas configurações — o livro-caixa passa a sincronizar automaticamente entre iPhone/iPad e, de repente, tudo fica bem mais "profissional".

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mãos à obra: conclua nesta semana

{class="mt-1"}
Siga a ordem "camada de dados → ViewModel → tela de lista → pop-up de entrada → cartão de resumo", um passo por dia. Se travar, cole a mensagem de erro exatamente como apareceu no buscador ou na IA (lembra da Parte 7, "Prática de Programação com IA"? Ao descrever o problema, deixe claros o "comportamento esperado, o comportamento real e os passos para reproduzir"). Depois de pronto, use-o para anotar os gastos por uma semana — usar um App feito por você mesmo gera uma sensação de conquista que empurra você a continuar.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumo do capítulo

- Os cinco elementos do requisito → dividir em pequenos passos "utilizáveis a cada etapa" e só então começar
- Camada de dados: modelo @Model + contêiner modelContainer + consulta FetchDescriptor
- Divisão MVVM: a View só desenha, o ViewModel @Observable cuida da lógica e o SwiftData cuida do armazenamento
- Interface: List + Section + toolbar + pop-up de entrada com sheet
- Validação em três camadas (funcionalidade/casos-limite/arquitetura) + desafios avançados (Swift Charts, sincronização iCloud)
:::
