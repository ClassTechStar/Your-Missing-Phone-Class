---
id: di-wu-shi-qi-zhang
num: 57
part: an-zhuo-kai-fa-pian
nav: Capítulo 57: O caminho de aprimoramento — permissões, notificações e arquitetura moderna
toc: default
kind: chapter
---

### Capítulo 57: O caminho avançado — permissões, notificações e arquitetura moderna

{class="chapter-intro mb-4"}
Conseguir fazer um App é só o começo. Neste capítulo, conversamos sobre alguns degraus do 'sei fazer' ao 'fazer bem': como pedir permissões com elegância, como enviar notificações sem irritar, como elevar a arquitetura mais um nível e — em 2026 — como escrever código Android em parceria com a IA. Cada item é algo que você vai encontrar imediatamente em projetos reais.

#### 1. Permissões em tempo de execução: primeiro bata na porta, depois entre

Câmera, localização, contatos, notificações... nessas 'zonas sensíveis', o Android exige que o App peça ao usuário em tempo de execução (desde o Android 6). A regra: declarar primeiro (no Manifest), pedir depois (no código) e degradar com elegância se o usuário recusar. No Compose, o caminho mais tranquilo é o rememberPermissionState, da biblioteca oficial Accompanist:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Permissões em tempo de execução (versão Compose)</span><span class="dots">···</span>
:::

```
// Primeiro declare no Manifest:
// &lt;uses-permission android:name="android.permission.CAMERA" /&gt;

@Composable
fun CameraButton() {
    val permission = rememberPermissionState(
        permission = android.Manifest.permission.CAMERA
    )
    Button(onClick = {
        when {
            permission.status.isGranted -&gt; openCamera()
            permission.status.shouldShowRationale -&gt; showExplainDialog()
            else -&gt; permission.launchPermissionRequest()
        }
    }) { Text("Tirar foto") }
}
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Atenção: e se a permissão for negada para sempre?

{class="mt-1"}
Depois que o usuário marca 'não perguntar novamente', o launchPermissionRequest não exibe mais o diálogo. Nesse caso, guie o usuário para ativar manualmente nas configurações do sistema (com um Intent que abra a página de configurações do app) e explique na interface 'para que serve essa permissão'. Com uma boa postura, a disposição do usuário para conceder sobe bastante — o texto do pedido de permissão merece ser escrito com cuidado.
:::

#### 2. Notificações: dizer a coisa útil na hora certa

A notificação é o canal do App para alcançar o usuário — e a função mais fácil de ser 'bloqueada' por ele. Três disciplinas para notificar: mande só o útil, deixe o usuário poder desligar e não importune de madrugada. Uso básico:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Enviando uma notificação</span><span class="dots">···</span>
:::

```
// No Android 13+ é preciso pedir a permissão POST_NOTIFICATIONS primeiro (veja a seção anterior)

// 1. Criar o canal de notificação (obrigatório no Android 8+)
val channel = NotificationChannel(
    "reminder", "Lembretes", NotificationManager.IMPORTANCE_DEFAULT
)
val manager = getSystemService(NotificationManager::class.java)
manager.createNotificationChannel(channel)

// 2. Enviar a notificação
val notification = NotificationCompat.Builder(this, "reminder")
    .setSmallIcon(R.drawable.ic_notification)
    .setContentTitle("Lembrete de despesas")
    .setContentText("Você ainda não registrou nada hoje")
    .setPriority(NotificationCompat.PRIORITY_DEFAULT)
    .build()
if (ActivityCompat.checkSelfPermission(this,
        Manifest.permission.POST_NOTIFICATIONS) == PackageManager.PERMISSION_GRANTED
) {
    manager.notify(1, notification)
}
```
:::

Tarefas agendadas (como 'lembrar de registrar os gastos às 20:00 todos os dias') usam o WorkManager — o 'mordomo de agendamento em segundo plano' recomendado oficialmente; ele garante que a tarefa execute no momento adequado, sem você se preocupar com otimização de bateria. Para necessidades do tipo despertador, é a escolha certa.

#### 3. Arquitetura avançada: injeção de dependência e modularização

Quando o projeto cresce, dois 'problemas deliciosos' batem à porta:

- Criação de objetos bagunçada: cada tela cria por conta própria o banco, a API — use o Hilt (framework de injeção de dependência) para gerenciar tudo de forma unificada: 'quem precisa de algo, faz o pedido e recebe';
- Código virando montanha: o projeto de módulo único fica cada vez mais lento para modificar — divida em múltiplos módulos (app / core / feature-xxx) e desenvolva e teste cada função de forma independente.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Dica: não faça engenharia demais

{class="mt-1"}
Hilt e modularização são boas ferramentas, mas em projeto de uma pessoa só, não tenha pressa de adotá-las. Para o controle de gastos, módulo único + criação manual de dependências dá conta perfeitamente. Espere o código passar de algumas dezenas de milhares de linhas, a compilação ficar lenta ou a colaboração envolver várias pessoas para introduzi-las conforme a necessidade. Ferramentas servem ao objetivo, não à ostentação — é também o princípio da 'simplicidade acima de tudo' do nosso livro de programação com IA.
:::

#### 4. A novidade de 2026: desenvolvimento Android assistido por IA

Em 2026, a IA já está profundamente embutida no fluxo de desenvolvimento Android. Se você quer ganhar velocidade, esta combinação de práticas está bem consolidada:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Etapa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Como a IA ajuda</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Sua responsabilidade</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Escrever código</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">O Gemini embutido no Android Studio / plugins de IA de terceiros completam e geram código</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Descrever bem o requisito e revisar o resultado</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pesquisar material</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Entregar a documentação oficial e as mensagens de erro para a IA interpretar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Conferir as conclusões-chave na documentação oficial</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Escrever testes</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pedir à IA que gere casos nas três classes 'normal/limite/exceção'</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Confirmar que os casos fazem sentido para o negócio</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Corrigir bugs</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Colar a pilha + o código relacionado; a IA localiza e corrige</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Entender a mudança e rodar os testes para validar</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Os quatro cenários do desenvolvimento Android assistido por IA

A metodologia concreta — como dar instruções à IA, como validar o resultado, como evitar armadilhas — está nos 11 capítulos completos da Parte 7 deste livro, 'Prática de Programação com IA' (capítulos 37 a 47); recomendo fortemente ler em paralelo: deixe a sintaxe Android por conta desta parte e o know-how de colaboração com IA por conta da Parte 7.

#### 5. Otimização de desempenho do Compose e ferramentas de depuração

Programar no Compose é gostoso, mas 'recomposição em excesso' também trava. Três truques práticos:

- Estabilize os parâmetros: adicione @Immutable às classes de dados ou use derivedStateOf para evitar que mudanças de estado sem relação disparem recomposição em larga escala;
- Lembre de usar key: items(list, key = { it.id }) faz com que, ao adicionar ou remover itens, só o que deve se mover se mova — sem key, apagar um item pode redesenhar a lista inteira;
- Modo Compose do Layout Inspector: veja em tempo real quantas vezes cada Composable se recompõe; fica claro quem recompõe demais, e você otimiza nos pontos quentes.

Além disso, ative os relatórios do compilador do Compose (Metrics) para gerar um relatório de 'quais componentes são instáveis' — no caminho avançado, os dados são sempre mais confiáveis que as sensações.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mãos à obra: adicione o 'trio' ao controle de gastos

{class="mt-1"}
① Adicione ao controle de gastos o 'lembrete de registrar os gastos às 20:00 todos os dias' (WorkManager + canal de notificação + permissão de notificação do Android 13); ② converta a criação do banco de dados e da API para injeção com Hilt; ③ experimente usar ferramentas de IA para acelerar a implementação do 'filtro mensal' e depois inspecione o resultado pelo método de aceitação em três níveis. Com o trio pronto, seu projeto ganha cara de 'tropa de elite'.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumo do capítulo

- Permissões sensíveis: declarar no Manifest + pedir em tempo de execução + guiar com elegância após a recusa
- Três disciplinas das notificações: só o útil, desligável, sem assédio; canal + permissão, nenhum pode faltar
- Tarefas agendadas com WorkManager; não reinvente a roda
- Hilt para os objetos, modularização para o código — em projeto pequeno de uma pessoa só, não tenha pressa
- Quatro cenários de IA assistida: escrever código, pesquisar, escrever testes, corrigir bugs; a metodologia está na Parte 7 (capítulos 37 a 47)
:::
