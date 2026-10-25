---
id: di-er-shi-san-zhang
num: 23
part: chao-yue-pian
nav: Capítulo 23: Pensamento computacional e iniciação à automação
toc: default
kind: chapter
---

### Capítulo 23: Pensamento de programação e iniciação à automação

{class="chapter-intro mb-4"}
Nos dois capítulos anteriores, construímos uma "muralha de segurança" para o celular e também conhecemos seu "cérebro de IA" cada vez mais inteligente dentro dessas muralhas. Agora, vamos desbloquear uma das capacidades mais poderosas do celular: fazê-lo "pensar" como um programador e executar automaticamente as tarefas que você definir. Você pode dizer: "Mas eu não sei programar, o que isso tem a ver comigo?" Fique tranquilo — este capítulo não exige que você escreva uma única linha de código. Os celulares modernos já reduziram a barreira da "programação" a um nível de arrastar e soltar.

#### 1. Afinal, o que é automação?

Em linguagem simples, automação é: <strong>fazer o celular executar automaticamente uma série de ações quando uma determinada condição é atendida.</strong> Você não precisa fazer manualmente todas as vezes, nem precisa lembrar o que fazer — o celular decide sozinho o momento e executa sozinho.

Um exemplo: toda manhã, ao acordar, você precisa desativar manualmente o modo Não Perturbe, abrir o WeChat para ver as mensagens, abrir o app de clima para saber o que vestir, abrir o NetEase Music para tocar uma música. Se você empacotar esses passos em um fluxo de automação configurado para "executar automaticamente às 7h da manhã", ao acordar você só precisa pegar o celular e tudo já está pronto. Não é ótimo só de imaginar?

Automação é essencialmente a cadeia lógica "se... então...", o if-else da programação. Aprender essa forma de pensar, mesmo que você nunca escreva código na vida, vai melhorar muito sua capacidade de organizar problemas. Elementos essenciais:

1. <strong>Gatilho</strong>: quando começar? Pode ser "todo dia às 7h", "quando eu me conectar ao Wi-Fi de casa", "quando eu chegar a um determinado lugar", "quando a bateria do celular estiver abaixo de 20%".
2. <strong>Ação</strong>: o que fazer especificamente? Pode ser enviar uma mensagem no WeChat, abrir um app, ajustar o volume, trocar o papel de parede, tocar música, enviar uma notificação... Quase tudo que você faz manualmente no celular pode ser automatizado.
3. <strong>Lógica intermediária</strong> (opcional, mas poderosa): se a situação for A, faça X; caso contrário, faça Y. Por exemplo, "se for dia útil, toque podcast de notícias; se for fim de semana, toque música". Isso se chama ramificação condicional.

#### 2. "Atalhos" do iOS — a ferramenta mágica de automação para usuários Apple

O app "Atalhos" (Shortcuts) da Apple é um aplicativo nativo, não precisa baixar. Seu conceito central é montar várias operações como blocos de montar. Primeiro, alguns conceitos-chave:

- <strong>"Atalho"</strong>: um fluxo de automação completo, que pode ser executado manualmente com um toque ou acionado por voz com a Siri. Por exemplo, você diz "Ei Siri, modo voltar para casa", e ela executa automaticamente a série de operações que você configurou.
- <strong>"Automação"</strong>: instruções que são executadas automaticamente por um gatilho, sem necessidade de acionamento manual. Por exemplo, "quando o celular se conectar ao Bluetooth do carro, abra automaticamente o app de mapas". As automações são configuradas na aba "Automação", separada dos "Atalhos".
- <strong>"Ação"</strong>: a menor unidade de execução. Abrir um app é uma ação, enviar uma mensagem é uma ação, obter a previsão do tempo é uma ação, ajustar o brilho é uma ação. Você pode encadear centenas de ações juntas.

Veja alguns exemplos realmente úteis. Se você seguir fazendo, vai entender na hora:

##### Exemplo 1: "Rotina de bom dia" com um toque

Toda manhã, com um toque (ou dizendo "Bom dia" para a Siri), o celular automaticamente: obtém a previsão do tempo de hoje → lê o clima e a temperatura em voz alta → mostra os compromissos do dia no calendário → abre seu app de música favorito e começa a tocar. Passos: Novo atalho → Adicionar ação "Obter clima atual" → Adicionar "Ler texto" → Adicionar "Obter eventos do calendário" → Adicionar "Mostrar lembrete" → Adicionar "Abrir app" e selecionar NetEase Music. Simples assim, tudo arrastando.

##### Exemplo 2: "Modo economia de energia" automático

Na aba "Automação", Nova automação → selecionar "Nível da bateria" → definir "Abaixo de 30%" → Adicionar ação "Definir modo de baixo consumo como ativado", "Reduzir brilho da tela para 30%", "Desativar Bluetooth". A partir daí, quando a bateria estiver abaixo de 30%, o celular entra automaticamente em modo de economia de energia, sem você se preocupar.

##### Exemplo 3: Registro automático de gastos ao escanear QR code

Toda vez que você paga com WeChat/Alipay escaneando um QR code, o celular lê a notificação de pagamento e registra automaticamente o valor e o estabelecimento em um memorando ou planilha Numbers. Isso requer o gatilho "Receber SMS/Notificação" na Automação dos Atalhos (iOS 17+ suporta leitura de transações da carteira), combinado com a ação "Anexar ao Numbers". Para quem quer controlar gastos mas tem preguiça de registrar manualmente, é um salvador.

Outra dica que muitos não conhecem: você pode adicionar um atalho à tela inicial, transformando-o em um ícone de app. Por exemplo, crie um atalho "Chamar carro para casa", coloque o ícone na tela inicial — um toque abre diretamente o Didi com o destino já configurado para casa. Muito mais rápido que abrir o app manualmente e digitar tudo.

#### 3. Automação no Android — Tasker e seus amigos

No lado Android, a situação é um pouco mais complexa, mas o teto também é mais alto. Vamos começar pelo simples:

##### Nível iniciante: Auto Clicker

Muitos celulares Android vêm com "Auto Clicker" ou você pode baixar na loja de apps. O princípio é super simples: você faz a operação manualmente uma vez, ele grava as coordenadas dos seus toques e os intervalos de tempo, e depois pode reproduzir em alta velocidade. Por exemplo, se um app tem recompensa diária de check-in, você grava o fluxo de cliques uma vez e depois executa automaticamente todo dia. A desvantagem: ele só reconhece coordenadas. Se o layout da interface mudar (como aparecer um anúncio), ele clica no lugar errado.

##### Nível avançado: Tasker — o rei da automação Android

O Tasker é reconhecidamente a ferramenta de automação mais poderosa da plataforma Android, sempre no topo das listas. Sinceramente, a curva de aprendizado é um pouco íngreme, a interface não é das mais bonitas, mas uma vez que você pega o jeito, vai sentir que seu celular de repente se torna capaz de tudo. O núcleo do Tasker também é o modelo "gatilho → tarefa":

- <strong>Perfil (Profile)</strong>: define "quando disparar". As condições de disparo podem ser hora, local, estado de conexão Wi-Fi, conexão Bluetooth, recebimento de notificação específica, estado da bateria, orientação da tela... O Tasker suporta dezenas de condições de disparo, é absurdo.
- <strong>Tarefa (Task)</strong>: define "o que fazer após o disparo". Uma tarefa pode conter várias ações, executadas em sequência. Os tipos de ação incluem: ajustar configurações do sistema (volume, brilho, Wi-Fi, Bluetooth, modo avião), enviar SMS, requisições HTTP, executar comandos Shell, controlar reprodução de mídia, exibir caixas de diálogo, etc.

Aqui estão alguns cenários clássicos e práticos do Tasker:

- <strong>Ligar Wi-Fi automaticamente ao chegar em casa</strong>: configurar gatilho como "conectar-se a uma torre de celular específica" (porque perto de casa você se conecta a torres fixas) → tarefa "Ativar Wi-Fi". Sem usar GPS, sem gastar bateria — o celular liga o Wi-Fi automaticamente quando você entra no alcance do bairro.
- <strong>Modo reunião</strong>: gatilho "evento do calendário com 'reunião' no título" → tarefa "Modo silencioso, desativar volume de mídia, responder automaticamente no WeChat (requer plugin)". Nunca mais se preocupe com o celular tocando durante uma reunião.
- <strong>Proteção ocular noturna</strong>: gatilho "horário 22:00-06:00" → tarefa "Ativar modo de proteção ocular, reduzir brilho para 20%, colocar tela em preto e branco (modo escala de cinza)". A tela em preto e branco faz milagre contra o vício em vídeos curtos — quando a imagem fica cinza, você perde a vontade de rolar.
- <strong>Auto podcast ao conectar fone de ouvido</strong>: gatilho "fone de ouvido com fio conectado / fone Bluetooth conectado" → tarefa "Abrir app Xiaoyuzhou e começar a tocar o episódio mais recente". Coloque o fone e já comece a ouvir, sem precisar desbloquear o celular e procurar o app.

Se você achar o Tasker muito difícil de começar, experimente seu irmão simplificado: <strong>MacroDroid</strong>. Interface muito mais amigável, cheio de templates, ideal para quem não quer se estressar. Além disso, muitos sistemas Android de marcas chinesas (MIUI da Xiaomi, HarmonyOS da Huawei, ColorOS da OPPO) vêm com funções nativas de "Cenas" ou "Assistente inteligente". Embora não sejam tão poderosas quanto o Tasker, para automação do dia a dia são totalmente suficientes.

#### 4. Aplicações diárias do pensamento de automação

O maior ganho ao aprender automação não é o tempo economizado, mas <strong>mudar sua forma de pensar sobre problemas</strong>. Uma vez que você se acostuma com o modelo mental "se X acontecer, faça Y automaticamente", você percebe que um monte de tarefas repetitivas da vida podem ser eliminadas. Por exemplo:

- Toda vez que tirar uma foto, fazer backup automático na nuvem e depois comprimir a foto local para um tamanho menor, economizando espaço.
- Toda manhã, ler automaticamente os compromissos do dia no calendário, gerar um texto e enviar para a família pelo WeChat.
- Ao receber SMS de confirmação de entrega de encomenda, adicionar automaticamente uma tarefa "Buscar encomenda" no memorando.
- Quando a bateria estiver completamente carregada, emitir um alerta de voz para lembrar de desconectar o carregador (evitar sobrecarga que danifica a bateria).
- No horário de saída do trabalho, se ainda estiver perto da empresa (via localização por torre de celular), lembrar automaticamente "Hora de ir para casa".

Isso tudo parece avançado, mas na verdade, se você dominar os dois conceitos básicos de "gatilho + ação" e usar os Atalhos ou o Tasker, tudo isso é possível. O segredo é <strong>primeiro perceber que "essa tarefa pode ser automatizada"</strong> — muita gente não é incapaz, simplesmente nunca pensou nessa possibilidade.

#### 5. Guia de armadilhas: problemas comuns de automação

Fazer automação não é sempre um mar de rosas. Aqui estão algumas armadilhas que já passei para você não precisar passar:

- <strong>Gatilho por localização pode falhar</strong>: o gatilho "Chegar/Sair do local" no iOS usa tecnologia de geofencing, e a precisão depende do sinal GPS e da otimização do sistema. Às vezes você já chegou em casa há 10 minutos e o gatilho ainda não disparou. Recomenda-se usar gatilho por conexão Wi-Fi ou torre de celular em vez de localização — mais confiável e econômico em bateria.
- <strong>As "Automações" dos Atalhos precisam de autorização</strong>: no iOS, a maioria dos gatilhos na aba "Automação" precisa de confirmação manual para executar (mecanismo de segurança do iOS). Mas os gatilhos de conexão Wi-Fi, conexão Bluetooth e alarme parando podem ser executados de forma totalmente automática, sem confirmação.
- <strong>Tasker precisa da permissão de acessibilidade</strong>: muitas funções avançadas (como simular cliques) exigem o serviço de acessibilidade, o que faz o celular mostrar uma notificação persistente nas configurações. É um design de segurança do Android, não tem como remover.
- <strong>Não complique demais a automação</strong>: ao começar, faça fluxos pequenos de "2-3 ações". Não tente criar um super fluxo de 20 passos de uma vez — você vai enlouquecer depurando.

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Dica: a postura correta para começar com automação

{class="mt-1"}
Primeiro, gaste 5 minutos pensando: quais são as 3 coisas que você mais repete no celular todo dia? Por exemplo, a rotina matinal, o hábito ao conectar fones Bluetooth, as configurações antes de sair de casa... Comece por essas pequenas tarefas de alta frequência e crie uma automação simples para cada uma. Mesmo que cada automação economize apenas 5 segundos, ao longo do tempo o acúmulo é significativo. E a satisfação depois de criar — vicia de verdade.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Pratique: três desafios de automação para iniciantes

{class="mt-1 mb-2"}
Escolha o mais adequado para você e complete — depois disso você já terá começado:

{class="list-decimal pl-6 mt-1 space-y-1"}
1. <strong>Desafio 1: Automação de bom dia</strong>: iOS: no app Atalhos, Novo atalho → Adicionar "Obter clima atual" → "Ler texto" → "Abrir app" selecionando NetEase Music. Depois você pode dizer "Bom dia" para a Siri para acionar. Android: no Tasker, Nova tarefa → Adicionar "Obter clima" → "Ler" → "Abrir app" → definir gatilho para todo dia às 7:00.
2. <strong>Desafio 2: Economia de energia automática com bateria baixa</strong>: iOS: Aba Automação → Novo → "Nível da bateria" → Abaixo de 25% → Adicionar "Definir modo de baixo consumo como ativado" + "Definir brilho 25%". Android: Tasker, Novo Perfil → Estado → Energia → Bateria 0-25% → Tarefa "Ativar modo de economia" + "Reduzir brilho".
3. <strong>Desafio 3: Navegação automática ao conectar Bluetooth do carro</strong>: iOS: Automação → Novo → "Bluetooth" → selecionar Bluetooth do carro → Adicionar "Abrir app" selecionando Amap + "Volume de mídia 80%". Android: Tasker → Perfil → Estado → Bluetooth conectado → selecionar Bluetooth do carro → Tarefa "Abrir Amap" + "Aumentar volume de mídia".
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Exemplo 3: Automação "Rotina de bom dia"

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>Cenário</strong>: todo dia às 7:00 anunciar automaticamente a previsão do tempo + desativar silencioso + abrir notícias.
- <strong>Etapas</strong>: iOS: Atalhos → Automação → Gatilho por horário → Adicionar "Obter clima" + "Definir volume" + "Abrir app"; Android: MacroDroid → Gatilho (horário 7:00) → Ações (volume de mídia / abrir URL / TTS ler clima).
- <strong>Resultado esperado</strong>: implementável sem instalação adicional, reduzindo a barreira de entrada.
:::
