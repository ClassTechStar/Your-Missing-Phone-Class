---
id: di-yi-zhang-memory
part: ji-chu-pian
nav: Anexo: Análise de expansão de memória em telemóveis Android
toc: sub
kind: supplement
---

### Apêndice: Análise da Expansão de Memória em Celulares Android

{class="chapter-intro mb-4"}
Ao comprar um celular, você frequentemente vê anúncios como "12GB+8GB de RAM" — como se houvesse 8GB extras de memória de acesso aleatório do nada. Mas isso realmente torna o celular mais rápido? Ou pode até danificá-lo? Nesta seção, vamos esclarecer completamente a tecnologia de "expansão de memória".

#### 1. Definição Essencial

A "expansão de memória" dos celulares Android (também chamada de extensão de memória, fusão de memória, RAM Plus, etc.) <strong>não é um aumento físico real do chip de memória de acesso aleatório</strong>, mas sim uma tecnologia de software em nível de sistema: aloca dinamicamente parte do espaço de armazenamento interno (ROM/flash UFS) para simular o uso como memória de acesso aleatório virtual (RAM).

Uma analogia: a RAM física é a "bancada de trabalho de alta velocidade", e a memória expandida é o "depósito temporário". Quando a bancada não é suficiente, o sistema move os dados temporariamente não utilizados para o depósito e os traz de volta quando necessário. O depósito tem grande capacidade, mas o transporte de ida e volta é certamente mais lento do que manter diretamente na bancada.

#### 2. Princípio Técnico

As principais implementações dos fabricantes são basicamente duas:

##### 1. Compressão zRAM

Aloca um espaço de dados comprimidos dentro da RAM, armazenando o código de aplicativos inativos de forma comprimida, com taxa de compressão de cerca de 2:1. Os dados ainda estão na RAM, com alta velocidade e sem desgaste do flash, mas requer a participação da CPU para compressão e descompressão.

##### 2. Partição swap

Aloca diretamente um espaço fixo no flash UFS como memória virtual, gravando dados de processos em segundo plano no armazenamento. Depende da largura de banda do armazenamento, com velocidade de leitura/gravação muito inferior à da memória física.

A propaganda "12GB+8GB de RAM" dos fabricantes geralmente é a combinação de 12GB de RAM física + 8GB de memória virtual em flash. Vale notar que, por padrão, o zRAM não ocupa o armazenamento interno; somente quando o zRAM está completamente cheio de dados é que o sistema cria um arquivo de troca no armazenamento — e isso raramente acontece.

#### 3. A Diferença de Velocidade é o Gargalo Crítico

A limitação fundamental desta tecnologia está na diferença de velocidade. O atual flash UFS 4.0 tem velocidade de leitura sequencial de cerca de 4200MB/s, apenas 1/10 a 1/15 da memória física LPDDR5X. Portanto, na fase de compressão zRAM de carga leve, a velocidade se aproxima da RAM real, mas uma vez que entra em cenários de alta carga, a velocidade despenca para dezenas de vezes mais lenta.

#### 4. Cenários Aplicáveis e Limites de Benefício

A expansão de memória não é uma solução mágica; os resultados variam conforme o modelo e o cenário de uso:

- <strong>Situações úteis</strong>: Modelos com 6GB de RAM física + UFS 3.1 ou superior, com espaço livre ≥30GB. Ao ativar 3GB de expansão, podem manter 3-4 aplicativos a mais em segundo plano, reduzindo a taxa de recarga em 68%. Adequado para entregadores de comida, motoristas de aplicativo e outros usuários de multitarefa intensiva.
- <strong>Cenários diários</strong>: Melhora significativa para múltiplas contas do WeChat, preservação de abas do navegador, resposta a mensagens de mensageiros instantâneos. O tempo de inicialização a frio de aplicativos em segundo plano é notavelmente reduzido.
- <strong>Cenários limitados</strong>: Melhora limitada para carregamento de jogos pesados, edição de vídeo 4K e outros cenários de alta largura de banda.
- <strong>Situações prejudiciais</strong>: Modelos com 8GB de RAM + UFS 2.2 e espaço livre insuficiente. Ao ativar, a flutuação da taxa de quadros em jogos aumenta, assistir a vídeos curtos consome mais bateria e a alternância trava.
- <strong>Situações inúteis</strong>: Modelos com 16GB ou mais de RAM têm benefício quase zero, no máximo mantendo 1 aplicativo adicional em segundo plano, mas aumentando a carga da CPU em 12% e a temperatura em 2-3°C. Para modelos com RAM superior a 12GB, recomenda-se desativar diretamente para evitar cálculos de compressão desnecessários.

#### 5. Nomenclatura e Método de Ativação por Fabricante

Cada marca chama de um jeito: Xiaomi chama de "Expansão de Memória", Huawei de "Fusão de Memória", Samsung de "RAM Plus", vivo de "Extended RAM", OnePlus de "Memory Extension". Esta função é uma capacidade nativa do sistema, sem vínculo direto com a versão subjacente do Android.

O caminho geral de ativação é: Entre em [Configurações] → [Mais configurações] → encontre o subitem [Memória] ou [Desempenho] → ative "Expansão de Memória" e selecione o nível de capacidade (geralmente 2GB–7GB), efetivo após reinicialização. Após ativar, o sistema exibirá uma combinação de memória como "8GB+4GB".

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Observações

{class="list-disc pl-6 mt-1 space-y-1"}
- A expansão de memória ocupará parte do espaço de armazenamento interno. Certifique-se de que o armazenamento livre não seja inferior a 20-30GB, caso contrário, pode afetar a fluidez do sistema.
- O flash usado como memória virtual sofre desgaste de leitura/gravação. Embora os flashes UFS modernos tenham longa vida útil, o swap frequente de longo prazo ainda pode acelerar o envelhecimento do armazenamento.
- Se o próprio celular tiver pouca memória física (como 4GB ou menos), ativar a expansão de memória só pode aliviar a urgência imediata, não resolvendo fundamentalmente o problema de travamento.
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Resumo

{class="mt-1"}
A expansão de memória é uma tecnologia madura de otimização em nível de sistema, capaz de melhorar a capacidade de multitarefa e a taxa de preservação em segundo plano de modelos de gama baixa e média sem alterar o hardware. No entanto, é limitada pela enorme diferença de velocidade entre o flash e a memória física, não sendo uma "cura milagrosa". Ativar ou não, e em qual tamanho, deve ser decidido com base no tamanho da RAM física do seu modelo, na especificação do flash, no espaço de armazenamento livre e nos hábitos de uso.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Mãos à obra: Veja se seu celular tem expansão de memória

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Abra [Configurações], pesquise por "expansão de memória", "fusão de memória", "RAM Plus" ou "Extended RAM".
2. Encontre e verifique se está ativado atualmente e qual é a configuração de capacidade de expansão.
3. Compare com o conteúdo desta seção: Qual é a RAM física do seu modelo? Qual é a especificação do flash? O espaço de armazenamento livre é suficiente?
4. Tente desativar ou reduzir a capacidade de expansão, observe por uma semana a preservação em segundo plano e as mudanças de aquecimento, e encontre a configuração ideal para você.
:::
