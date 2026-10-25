---
id: di-yi-zhang-harmony
part: ji-chu-pian
nav:  Anexo do Capítulo 1: Especial sobre o sistema HarmonyOS
toc: default
kind: supplement
---

### Apêndice do Capítulo 1: Especial sobre HarmonyOS

{class="chapter-intro mb-4"}
HarmonyOS é o sistema operacional desenvolvido independentemente pela Huawei. Desde seu lançamento em 2019, já passou por várias versões principais. Não é apenas "mais um substituto do Android", mas uma nova espécie com conceitos de design únicos. Vamos conhecer a fundo este sistema operacional em ascensão.

#### 1. O que é HarmonyOS? Por que ele é diferente?

A filosofia central do HarmonyOS é a "Internet de Todas as Coisas". Diferente dos sistemas operacionais tradicionais que servem principalmente a um único dispositivo, o HarmonyOS foi projetado desde o início considerando a colaboração entre múltiplos dispositivos.

A <strong>arquitetura distribuída</strong> é a alma do HarmonyOS. Simplificando, ela pode virtualizar vários dispositivos em um "super terminal". Seu celular, tablet, computador, relógio e TV não são mais indivíduos isolados, mas sim "órgãos" de um todo, podendo invocar mutuamente as capacidades uns dos outros.

Por exemplo: você está assistindo a um vídeo no celular e quer ver na tela grande. O método tradicional é espelhar a tela; no HarmonyOS, você pode diretamente "transferir" o vídeo para a TV e continuar assistindo, com o celular se transformando em controle remoto. Isso não é simples espelhamento, mas o próprio aplicativo rodando entre dispositivos.

#### 2. HarmonyOS 4.3: A Versão Madura Baseada em AOSP

O HarmonyOS 4.3 é a versão atualmente amplamente implantada nos celulares Huawei. É importante esclarecer que o HarmonyOS 4.3 é compatível com o framework de código do Android Open Source Project (AOSP), portanto, pode executar totalmente aplicativos Android — a maioria dos aplicativos que você baixa na loja de aplicativos Huawei ainda são essencialmente aplicativos Android, rodando através da camada de compatibilidade do HarmonyOS. Mas o HarmonyOS 4.3 não é uma simples capa sobre o Android; ele adiciona muitas tecnologias proprietárias da Huawei, como capacidade distribuída e o motor Ark, sobre a base do AOSP.

##### Características principais:

- <strong>Compatibilidade com aplicativos Android</strong>: Por ser baseado no AOSP, o HarmonyOS 4.3 pode executar normalmente quase todos os aplicativos Android, e o usuário mal percebe a diferença.
- <strong>Motor Ark</strong>: Compilador e runtime proprietários da Huawei, tornando a execução de aplicativos mais fluida e econômica. Comparado às versões anteriores, a fluidez melhorou significativamente.
- <strong>Super Terminal</strong>: No centro de controle, você pode ver intuitivamente outros dispositivos HarmonyOS ao redor e conectar arrastando. O celular usando o teclado e mouse do computador, o tablet usando a câmera do celular — tudo muito conveniente.
- <strong>Cartões de Serviço</strong>: Semelhantes aos widgets do iOS, mas mais flexíveis. Deslize para cima no ícone do aplicativo para expandir o cartão, mostrando informações-chave sem abrir o aplicativo.
- <strong>Modo Puro</strong>: Permite apenas a instalação de aplicativos da loja oficial, reduzindo o risco de malware.
- <strong>Central de Privacidade</strong>: Gerencia centralizadamente as permissões de aplicativos e visualiza o registro de comportamento dos aplicativos.

##### Características da interface do usuário:

- <strong>Tela de bloqueio revista</strong>: A tela de bloqueio exibe imagens e artigos elegantes; deslize para entrar na área de trabalho.
- <strong>Cartões universais</strong>: Ícones da área de trabalho podem ser expandidos em cartões, mostrando mais informações.
- <strong>Super Área de Transferência</strong>: Uma área de armazenamento temporário onde você pode guardar texto, imagens e arquivos e depois arrastar para usar em qualquer aplicativo. O compartilhamento entre aplicativos se torna incrivelmente fluido.
- <strong>Pesquisa Inteligente</strong>: Pesquisa global que pode buscar aplicativos, arquivos, configurações e páginas web.

#### 3. HarmonyOS NEXT (HarmonyOS 6): O Verdadeiro Ponto de Partida do Sistema Operacional Autônomo da Huawei

O HarmonyOS NEXT (HarmonyOS NEXT 5.0) tem uma diferença fundamental em relação ao HarmonyOS 4.3 — ele adota o microkernel proprietário da Huawei, não dependendo mais do kernel Linux e do código AOSP, e também <strong>não suporta mais diretamente aplicativos Android</strong>. Este é o passo crucial do HarmonyOS de "forma transitória compatível com Android" para "sistema operacional completamente independente".

##### Mudanças significativas:

- <strong>Kernel completamente autônomo</strong>: O HarmonyOS NEXT usa o kernel proprietário da Huawei, sem nenhum código AOSP. O sistema é mais enxuto, mais seguro e mais eficiente.
- <strong>Não suporta mais aplicativos Android</strong>: Esta é a maior mudança. O HarmonyOS NEXT só pode executar aplicativos nativos HarmonyOS, não podendo instalar ou executar arquivos APK. Antes de atualizar, confirme se os aplicativos que você usa têm versão nativa HarmonyOS.
- <strong>Ecossistema de aplicativos nativos</strong>: A Huawei está impulsionando fortemente os desenvolvedores a migrar aplicativos para a plataforma nativa HarmonyOS. Atualmente, aplicativos populares como WeChat, Alipay, Taobao, etc., já lançaram versões nativas HarmonyOS, mas alguns aplicativos de nicho podem ainda não estar adaptados.
- <strong>Arquitetura de segurança Star Shield</strong>: Um novo sistema de segurança com proteção de cadeia completa do hardware ao software. Suporta controle de permissão mais granular, como "localização aproximada" — o aplicativo só sabe aproximadamente onde você está, não a localização precisa.
- <strong>Integração profunda de IA</strong>: Capacidade de IA em nível de sistema, não apenas em um aplicativo específico. Por exemplo, legendas de IA podem traduzir vídeos em tempo real, e o recorte de IA pode identificar inteligentemente o sujeito.
- <strong>Transferência contínua entre dispositivos</strong>: Capacidade distribuída ainda mais avançada. O estado do aplicativo pode alternar perfeitamente entre dispositivos; o documento que você está editando no celular abre automaticamente no computador quando você chega à mesa.
- <strong>Serviços Atômicos</strong>: Serviços leves que podem ser usados sem instalação. Por exemplo, escanear um código QR abre diretamente uma função específica, sem precisar baixar o aplicativo primeiro.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Leitura obrigatória antes de atualizar para o HarmonyOS NEXT

{class="mt-1"}
Após atualizar para o HarmonyOS NEXT, seu celular não poderá executar aplicativos Android. Certifique-se de confirmar antes da atualização: ① os aplicativos que você usa com frequência já têm versão nativa HarmonyOS; ② seu trabalho ou vida pessoal não depende de aplicativos Android. Após a atualização, não é possível reverter para o HarmonyOS 4.3.
:::

##### Mudanças na lógica de operação:

- <strong>Navegação por gestos</strong>: Deslize das bordas esquerda/direita para voltar, deslize de baixo para cima para a área de trabalho, deslize para cima e pause para multitarefa.
- <strong>Multi-janela inteligente</strong>: Suporta tela dividida, janela flutuante, visão paralela e outras formas de multitarefa.
- <strong>Chamadas de vídeo MeeTime</strong>: Serviço de chamada de vídeo da Huawei, suporta compartilhamento de tela, embelezamento e desfoque de fundo.

#### 4. Ecossistema HarmonyOS: Dispositivos e Aplicativos

O HarmonyOS não é apenas um sistema para celular, mas um ecossistema que cobre vários tipos de dispositivos.

##### Tipos de dispositivos suportados:

- <strong>Celular e Tablet</strong>: Dispositivos centrais, com funcionalidades mais completas.
- <strong>Relógio e Pulseira Inteligentes</strong>: Funcionamento independente ou em colaboração com o celular.
- <strong>Tela Inteligente (TV)</strong>: Centro de entretenimento doméstico.
- <strong>Caixa de Som Inteligente</strong>: Portal de interação por voz.
- <strong>Automóvel</strong>: Cockpit HarmonyOS, experiência de cabine de condução inteligente.
- <strong>Casa Inteligente</strong>: Geladeira, ar-condicionado, máquina de lavar, etc.

##### Situação atual do ecossistema de aplicativos:

A loja de aplicativos HarmonyOS já tem milhões de aplicativos, com a maioria dos aplicativos populares disponíveis. A Huawei também está promovendo ativamente os desenvolvedores a criar aplicativos nativos HarmonyOS. Até meados de 2026, aplicativos principais como WeChat, Alipay, Taobao, Douyin, Meituan, JD.com, etc., já lançaram versões nativas HarmonyOS, com uso diário basicamente sem obstáculos. Alguns aplicativos de nicho e setoriais podem ainda estar em adaptação. Antes de atualizar, recomenda-se confirmar se os aplicativos que você usa já são suportados.

#### 5. Dicas Práticas do HarmonyOS

- <strong>Super Terminal</strong>: Deslize para baixo do canto superior direito da tela para abrir o centro de controle, clique em "Super Terminal" para ver outros dispositivos ao redor e conectar arrastando.
- <strong>Super Área de Transferência</strong>: Pressione longamente texto/imagem/arquivo, selecione "Copiar para Área de Transferência", depois pressione longamente para colar em outros aplicativos ou arraste para fora.
- <strong>Cartões de Serviço</strong>: Deslize para cima no ícone do aplicativo para expandir o cartão; pressione longamente o cartão para ajustar o tamanho ou adicionar à área de trabalho.
- <strong>Multi-janela Inteligente</strong>: Deslize das bordas esquerda/direita da tela para dentro e pause, abra a barra lateral, clique no aplicativo para abrir em janela flutuante.
- <strong>Proteção de Privacidade</strong>: Configurações > Privacidade, para verificar o registro de uso de permissões dos aplicativos e configurar localização aproximada, etc.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Observações

{class="mt-1"}
O HarmonyOS está em constante atualização e iteração; versões diferentes podem ter algumas diferenças. Este texto descreve as principais características do HarmonyOS 4.3 e 6. Para funções específicas, consulte a versão real do seu celular. Recomenda-se manter o sistema atualizado para obter as funções mais recentes e correções de segurança.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Experimente agora: Explore as funções exclusivas do HarmonyOS

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Abra o centro de controle, encontre "Super Terminal" e veja se há outros dispositivos HarmonyOS por perto.
2. Experimente a "Super Área de Transferência": copie um texto para a área de transferência e depois arraste-o para o bloco de notas.
3. Deslize para cima em alguns ícones de aplicativos comuns e veja o que seus cartões de serviço exibem.
4. Vá para Configurações > Privacidade e veja quais aplicativos usaram permissões sensíveis recentemente.
:::
