---
id: di-wu-shi-si-zhang
num: 54
part: an-zhuo-kai-fa-pian
nav: Capítulo 54: Projeto 1 — Meu controle financeiro (versão local)
toc: default
kind: chapter
---

### Capítulo 54: Projeto 1 — Meu controle de gastos (versão local)

{class="chapter-intro mb-4"}
Bem-vindo ao seu primeiro 'projeto sério'. Este controle de gastos, embora não se conecte à internet, tem tudo o que precisa: registrar um lançamento, ver o extrato, somar por mês, excluir e editar. Ao terminá-lo, você terá percorrido o fluxo completo de 'dados → lógica → interface'. Não tenha pressa de copiar código — pense primeiro, aja depois; esse é o nosso princípio de sempre.

#### 1. Pensando nos requisitos: faça primeiro cinco perguntas

Antes de pôr a mão na massa, organize a ideia com os 'cinco elementos de requisito':

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Elemento</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Resposta</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who (para quem é)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Para você mesmo; família e amigos também valem</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What (o que faz)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Registrar receitas e despesas, ver o extrato, resumir por mês, estatísticas por categoria</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why (por que faz)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Praticar + descobrir para onde o dinheiro está indo</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How (como faz)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin + Compose + Room + MVVM, 100% local, sem back-end</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint (restrições)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Concluir em uma semana; suportar no mínimo o Android 8; mesmo sem publicar, já escrever no padrão de publicação</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Os cinco elementos de requisito do controle de gastos

Depois, divida em passos pequenos em que 'cada etapa já serve para algo': ① criar a camada de dados com Room (conseguir salvar um lançamento); ② tela de lista (conseguir ver o extrato); ③ tela de entrada (conseguir adicionar); ④ excluir e editar; ⑤ cartão de resumo mensal. Ao fim de cada passo, o App já é uma 'coisa utilizável'.

#### 2. Camada de dados: dando aos 'lançamentos' um lar

Primeiro defina como é um lançamento — campos suficientes, mas sem gula:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Record.kt (entidade)</span><span class="dots">···</span>
:::

```
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val type: String,        // "income" receita | "expense" despesa
    val amount: Double,      // valor (em yuan)
    val category: String,    // categoria: alimentação, transporte, salário…
    val note: String = "",   // observação (opcional)
    val date: String         // "2026-08-15"
)
```
:::

No Dao, acrescente duas consultas 'de estatística' — elas são a alma do controle de gastos:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordDao.kt (consultas agregadas)</span><span class="dots">···</span>
:::

```
@Dao
interface RecordDao {
    @Query("SELECT * FROM records ORDER BY date DESC, id DESC")
    fun getAll(): Flow&lt;List&lt;Record&gt;&gt;

    @Insert
    suspend fun insert(record: Record)

    @Delete
    suspend fun delete(record: Record)

    @Query("SELECT COALESCE(SUM(amount),0) FROM records WHERE type='income' AND date LIKE :month || '%'")
    suspend fun monthIncome(month: String): Double   // month no formato "2026-08"

    @Query("SELECT COALESCE(SUM(amount),0) FROM records WHERE type='expense' AND date LIKE :month || '%'")
    suspend fun monthExpense(month: String): Double
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Dica: por que usar Double para o valor?

{class="mt-1"}
Apps financeiros rigorosos usam BigDecimal ou 'Int em centavos' para evitar erros de ponto flutuante (o velho problema de 0,1+0,2≠0,3). Para um projeto de estudo, Double basta; se um dia você fizer um produto financeiro de verdade, lembre de trocar para centavos como unidade — é uma armadilha que inúmeros antecessores pisaram.
:::

#### 3. MVVM: interface e lógica 'morando separadas'

Deixar a interface operar o banco direto? Funciona, mas o código da tela fica enorme e desagradável de ler. A arquitetura MVVM reparte as tarefas: a View (interface) só desenha, o ViewModel (centro da lógica) cuida dos dados e o Model (Room) cuida do armazenamento.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View (interface Compose)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel (estado e lógica)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model (camada de dados Room)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 5: A estrutura de três camadas do MVVM — os dados fluem em um único sentido e cada camada não invade a outra
:::

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordViewModel.kt (esqueleto)</span><span class="dots">···</span>
:::

```
class RecordViewModel(private val dao: RecordDao) : ViewModel() {

    // Converte o Flow em estado observável pela tela
    val records = dao.getAll()
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(), emptyList())

    // Ações do usuário: chamar funções suspend
    fun addRecord(type: String, amount: Double, category: String, note: String, date: String) {
        viewModelScope.launch {
            dao.insert(Record(type = type, amount = amount,
                category = category, note = note, date = date))
        }
    }

    fun deleteRecord(record: Record) {
        viewModelScope.launch { dao.delete(record) }
    }
}
```
:::

Na interface (Compose), use assim: val vm: RecordViewModel = viewModel() e depois val list by vm.records.collectAsState() — assim que os dados mudam, a lista se atualiza sozinha e você não precisa fazer nada. Esse é o poder da união de MVVM + Flow + Compose.

#### 4. Interface: tela de lista + tela de entrada

Na tela de lista, use LazyColumn (lista de carregamento preguiçoso) — nem com muitos dados ela engasga:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Tela de lista de despesas (trecho principal)</span><span class="dots">···</span>
:::

```
@Composable
fun RecordListScreen(vm: RecordViewModel) {
    val records by vm.records.collectAsState()

    Column {
        // card de resumo no topo (receitas - despesas = saldo)
        SummaryCard(records)

        // lista de lançamentos
        LazyColumn {
            items(records, key = { it.id }) { record -&gt;
                RecordRow(record) { vm.deleteRecord(record) }
            }
        }

        // botão flutuante "nova entrada" → abre o diálogo de entrada
        FloatingActionButton(onClick = { showAddDialog = true }) {
            Text("+")
        }
    }
}

@Composable
fun RecordRow(record: Record, onDelete: () -&gt; Unit) {
    Row(Modifier.fillMaxWidth().padding(12.dp)) {
        Text(record.category, fontWeight = FontWeight.Bold)
        Spacer(Modifier.weight(1f))
        Text(if (record.type == "income") "+${record.amount}" else "-${record.amount}",
             color = if (record.type == "income") Color(0xFF27AE60) else Color(0xFFC0392B))
    }
}
```
:::

Para a entrada, o mais prático é um AlertDialog (caixa de diálogo): alguns campos de texto + alternância receita/despesa + seletor de categorias; ao tocar em confirmar, chame vm.addRecord(...).

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Atenção: não seja preguiçoso na validação de entradas

{class="mt-1"}
O campo de valor precisa de validação: bloqueie entradas inválidas como vazio, número negativo ou 'abc' (use toDoubleOrNull() para verificar). Uma das causas mais comuns de App que cai é 'tratar a entrada do usuário como um anjinho'. Lembre-se: tudo o que o usuário digita deve ser examinado como se fosse inimigo.
:::

#### 5. Editar e excluir: deixando os dados 'entrar e sair'

Um controle de gastos que só adiciona e nunca exclui morre em três dias de uso. Complete com duas operações:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Excluir e editar</span><span class="dots">···</span>
:::

```
// Adicione mais dois ao Dao:
@Query("UPDATE records SET amount=:amount, category=:category, note=:note WHERE id=:id")
suspend fun update(id: Long, amount: Double, category: String, note: String)

@Query("DELETE FROM records WHERE id=:id")
suspend fun deleteById(id: Long)

// Na tela: toque longo no item abre o menu "editar/excluir" (no Compose use DropdownMenu ou AlertDialog)
// É melhor mostrar confirmação antes de excluir — exclusão acidental é o que usuários de apps de despesas mais odeiam
```
:::

Duas lições sobre detalhes de interação: excluir exige confirmação dupla (para evitar dedos escorregadios) e editar deve preencher previamente o valor original (corrigir uma letra é mais fácil que digitar tudo de novo). Não menospreze esses detalhes — é deles que nasce a sensação de produto.

#### 6. Aceitação: três níveis de checagem + dois desafios avançados

Projeto terminado, faça a aceitação em três níveis 'função → limite → arquitetura': dá para registrar? dá para excluir? ao reabrir o App, os dados continuam lá (função); digitar 0 ou negativo no valor derruba o App? girar a tela perde dados? (limites); interface e dados estão misturados? campos estão hardcoded? (arquitetura).

Depois de passar na aceitação da versão básica, sirva-se de dois 'pratos avançados':

1. Filtro por mês: adicione no topo um seletor de mês (por exemplo, 2026-08 ▾) e a lista mostra só o extrato do mês;
2. Gráfico de pizza por categoria: use o Canvas do Compose ou uma biblioteca de gráficos leve para desenhar 'para onde foi o dinheiro' numa pizza — com isso pronto, o controle de gastos ganha cara de 'produto'.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mãos à obra: termine-o nesta semana

{class="mt-1"}
Trabalhe na ordem 'camada de dados → ViewModel → tela de lista → tela de entrada → cartão de resumo', um passo por dia. Se travar, jogue a mensagem de erro tal como está no buscador ou na IA (lembra da Parte 7, 'Prática de Programação com IA'? Ao descrever o problema, deixe claros 'comportamento esperado, comportamento real e passos para reproduzir'). Depois de pronto, use-o para registrar seus gastos por uma semana — usar um App que você mesmo fez dá uma sensação de conquista que empurra você a seguir em frente.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumo do capítulo

- Cinco elementos de requisito → dividir em passos pequenos em que 'cada etapa já serve' e só então agir
- Camada de dados: entidade Record + Dao (com SQL de estatística mensal) + Database
- Divisão MVVM: a View só desenha, o ViewModel cuida da lógica, o Model do armazenamento
- Flow + stateIn + collectAsState: os dados mudam e a interface se atualiza sozinha
- LazyColumn para a lista de carregamento preguiçoso; AlertDialog para a entrada de dados
- Aceitação em três níveis (função/limite/arquitetura) + desafios avançados (filtro mensal, pizza por categoria)
:::
