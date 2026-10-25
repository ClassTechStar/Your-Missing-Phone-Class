---
id: di-wu-shi-san-zhang
num: 53
part: an-zhuo-kai-fa-pian
nav: Capítulo 53: Armazenamento de dados e requisições de rede
toc: default
kind: chapter
---

### Capítulo 53: Armazenamento de dados e requisições de rede

{class="chapter-intro mb-4"}
Um App que só 'mostra' está morto; o App que salva dados e se conecta à rede é que está vivo. Neste capítulo você vai conhecer o 'trio' da camada de dados do Android: DataStore (guarda configurações pequenas), Room (guarda dados estruturados) e Retrofit (conversa com o servidor), além do 'maestro' deles — as corrotinas. Ao fim do capítulo, você será capaz de escrever Apps de verdade, que lembram os hábitos do usuário e atualizam o conteúdo em tempo real.

#### 1. Como escolher a solução de armazenamento: comece por esta tabela

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Solução</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">O que é adequado guardar</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Características</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Onde o livro usa</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DataStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Configurações avulsas (tema, opções liga/desliga)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pares chave-valor, simples e seguros</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Configurações do controle de gastos (capítulo 54)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dados estruturados (lançamentos, usuários)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Encapsulamento de verdade de um banco SQLite, com consultas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Registros de gastos (capítulo 54)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">(Não armazena; busca na rede) Dados do servidor</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">O padrão de fato entre as bibliotecas de requisições HTTP</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dados de clima (capítulo 55)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
A divisão de trabalho do trio de dados

Grave este ditado: 'configurações pequenas vão para o DataStore, dados em lote vão para o Room, dados de fora passam pelo Retrofit'. O SharedPreferences, comum nos tutoriais antigos, já foi substituído pelo DataStore, e o SQL escrito à mão no SQLite já cedeu lugar ao Room — aprenda direto o novo e não pegue o caminho velho.

#### 2. DataStore: guardando configurações pequenas

Para lembrar valores avulsos como 'a moeda escolhida da última vez' ou 'se o modo escuro está ativado', use o DataStore (versão Preferences):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Exemplo de DataStore</span><span class="dots">···</span>
:::

```
val Context.dataStore by preferencesDataStore(name = "settings")

// Escrita: salvar um valor
suspend fun saveTheme(isDark: Boolean) {
    context.dataStore.edit { prefs ->
        prefs[THEME_KEY] = isDark
    }
}

// Leitura: pegar o valor (o Flow avisa sobre mudanças automaticamente)
val themeFlow: Flow<Boolean> = context.dataStore.data
    .map { it[THEME_KEY] ?: false }
```
:::

Repare que o retorno é um Flow — um fluxo de dados que 'flui'. Assim que o valor muda, todos os lugares que o observam recebem o novo valor automaticamente. Esse conceito (reatividade) é a pedra fundamental do Android moderno, e você vai colocá-lo em prática no capítulo 54.

#### 3. Room: dando aos dados uma 'casa de verdade'

Um controle de gastos acumula centenas ou milhares de lançamentos e ainda precisa consultar e somar por categoria e por mês — isso pede um banco de dados. O Room é o encapsulamento oficial do SQLite; ele deixa 'criar tabelas e consultar dados' tão natural quanto escrever Kotlin. São três peças:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · O trio do Room: Entity / Dao / Database</span><span class="dots">···</span>
:::

```
// 1. Entity: a estrutura da tabela (uma tabela = um data class)
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val amount: Double,
    val category: String,
    val note: String,
    val date: String
)

// 2. Dao: a interface de operações (CRUD)
@Dao
interface RecordDao {
    @Query("SELECT * FROM records ORDER BY date DESC")
    fun getAll(): Flow<List<Record>>

    @Insert
    suspend fun insert(record: Record)

    @Delete
    suspend fun delete(record: Record)

    @Query("SELECT SUM(amount) FROM records WHERE category = :c")
    suspend fun sumByCategory(c: String): Double
}

// 3. Database: montagem final
@Database(entities = [Record::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun recordDao(): RecordDao
}
```
:::

Esse modelo de 'trio' pode ser levado tal como está para qualquer projeto seu — basta trocar os nomes dos campos. As consultas retornam Flow e a interface se atualiza sozinha conforme os dados; simplesmente maravilhoso.

#### 4. Retrofit: conversando com o servidor

Clima, notícias, câmbio... esses dados não estão no celular, e sim nos servidores de outras pessoas. O Retrofit deixa 'pedir dados ao servidor' tão simples quanto chamar uma função. São três passos:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Retrofit em três passos</span><span class="dots">···</span>
:::

```
// 1. Definir a interface: descreva as requisições HTTP como funções
interface WeatherApi {
    @GET("v1/weather")
    suspend fun getWeather(@Query("city") city: String): WeatherResponse
}

// 2. Criar a instância
val api = Retrofit.Builder()
    .baseUrl("https://api.example.com/")
    .addConverterFactory(GsonConverterFactory.create())
    .build()
    .create(WeatherApi::class.java)

// 3. Chamar como uma função (em uma coroutine)
val result = api.getWeather("Pequim")
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Alerta de armadilha: duas regras de ferro da rede

{class="mt-1"}
① Requisições de rede jamais devem ser feitas na thread principal — travaria a interface e poderia até derrubar o App (NetworkOnMainThreadException). Toda chamada de rede precisa ficar dentro de uma corrotina (viewModelScope.launch). ② HTTP em texto puro é proibido por padrão: desde o Android 9, exige-se HTTPS. Para testar com um endereço local em http://, é preciso declarar usesCleartextTraffic explicitamente no Manifest — mas o produto final deve usar HTTPS de ponta a ponta.
:::

#### 5. Parsing de JSON: 'traduzindo' os dados da rede

A maior parte dos dados que o servidor devolve vem em JSON — um texto parecido com 'dicionários aninhados'. O Retrofit precisa de um 'tradutor' para convertê-lo em objetos Kotlin. As duas soluções mainstream de 2026:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Solução</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Características</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cenário recomendado</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gson / Moshi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Solução veterana baseada em reflexão, custo de configuração zero</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Projetos pequenos, de arranque rápido e poucos campos</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">kotlinx.serialization</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Solução oficial em tempo de compilação, mais rápida e mais segura</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Primeira escolha para projetos novos (a preferida em 2026)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
As duas grandes soluções de parsing de JSON

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Exemplo kotlinx.serialization</span><span class="dots">···</span>
:::

```
// Adicione a anotação @Serializable ao data class
@Serializable
data class WeatherResponse(
    val weather: List<Weather>,
    val main: Main,
    val name: String
)

// O Retrofit recebe o Converter correspondente (suporte oficial a partir do Retrofit 2.11+):
// .addConverterFactory(json.asConverterFactory("application/json".toMediaType()))
```
:::

Seja qual for a solução, a regra de ferro é: primeiro olhe o JSON real que volta, depois defina os campos. Muitos bugs de 'falha no parsing' nascem de nomes de campos errados ou níveis de aninhamento adivinhados — imprima o JSON original e compare; dez segundos resolvem.

#### 6. Corrotinas: o 'idioma comum' da concorrência no Android

O suspend e o launch, que apareceram várias vezes acima, vêm das corrotinas do Kotlin (Coroutine) — a solução oficial de concorrência do Android. De forma bem grosseira, entenda assim: executar operações que 'precisam esperar um pouco' (rede, banco de dados) sem bloquear a interface.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Primeira experiência com coroutines</span><span class="dots">···</span>
:::

```
// Inicie uma coroutine no ViewModel
viewModelScope.launch {
    val records = dao.getAll().first()  // suspend: pausa e espera automaticamente
    // atualiza o estado da tela...
}

// Cola das palavras-chave:
// suspend   — "preciso esperar, não bloqueiem os outros"
// launch    — "Mão na massa!"
// viewModelScope — a "oficina" ligada à tela; encerra sozinha quando a tela é destruída
```
:::

Se você parte do zero, por agora basta decorar o uso; o princípio de 'suspender e retomar' por trás disso pode ser explorado depois. No dia a dia, 90% do que você escrever será este modelo.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mãos à obra: crie um mini-app de 'frase do dia'

{class="mt-1"}
Encontre uma API gratuita de citações (algo como o hitokoto), use o Retrofit para buscar a 'frase do dia', mostre-a no centro da tela e adicione um botão 'Trocar frase' (refazendo a requisição numa corrotina). Depois, salve as frases favoritas numa 'coleção' com o Room. Esse exercício usa DataStore/Room/Retrofit/corrotinas todos de uma vez — terminando-o, os capítulos 7 e 8 serão mamão com açúcar.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumo do capítulo

- Ditado: configurações pequenas no DataStore, dados em lote no Room, dados de fora pelo Retrofit
- O DataStore retorna um Flow: mudou o valor, os observadores recebem na hora
- O trio do Room: @Entity (tabela) + @Dao (operações) + @Database (montagem final); o modelo pode ser reutilizado direto
- Retrofit em três passos: definir a interface → criar a instância → chamar dentro de uma corrotina
- Duas regras de ferro: nada de rede na thread principal; produto final exige HTTPS
- Corrotina = esperar sem bloquear a interface; o viewModelScope é a sala de trabalho exclusiva da tela
:::
