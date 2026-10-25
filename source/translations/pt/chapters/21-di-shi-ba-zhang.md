---
id: di-shi-ba-zhang
num: 18
part: jin-jie-pian
nav: Capítulo 18: Backup e migração de dados
toc: default
kind: chapter
---

### Capítulo 18: Backup e migração de dados

{class="chapter-intro mb-4"}
Um vizinho meu deixou o celular cair na piscina e, quando o tirou, já não ligava mais. O que mais a entristeceu não foi o celular em si, mas as fotos de três anos sem backup — todo o registro do filho, do nascimento até aprender a andar. Ouvir isso me deixou muito mal, porque era algo totalmente evitável. Neste capítulo, vamos fazer um seguro de verdade para seus dados.

#### I. Primeiro, entenda: o que no seu celular, se perder, desaparece para sempre

O "estado de sobrevivência" de cada tipo de dado é diferente. Você precisa distinguir:

- <strong>Armazenado localmente no celular, se perder, desaparece mesmo</strong>: Fotos e vídeos (se não tiver sincronização em nuvem ativada), notas, SMS, histórico de chamadas, arquivos baixados.
- <strong>Armazenado no servidor do app, ao trocar de celular e fazer login novamente, está lá</strong>: Lista de amigos do WeChat, pedidos do Taobao, histórico de transações no app do banco. Essas coisas estão armazenadas nos servidores das respectivas empresas, não no seu celular.
- <strong>Na zona cinzenta, exige operação especial</strong>: Histórico de conversas do WeChat (embora o servidor do WeChat armazene, você mesmo não consegue baixar do servidor), credenciais de dispositivo vinculadas ao app do banco, chaves secretas nos apps de autenticação de dois fatores (como o Google Authenticator).

Portanto, o que você precisa proteger com prioridade são a primeira e a terceira categorias.

#### II. Backup completo do dispositivo: resolva tudo de uma vez

O backup completo é como tirar um "instantâneo" completo do celular — configurações atuais do sistema, layout da tela inicial, dados de apps, fotos, contatos, tudo empacotado.

##### Opção 1: Backup local no computador (a mais confiável, recomendada para quem tem computador)

- <strong>iPhone</strong>: Conecte o celular ao computador com o cabo de dados, abra o iTunes (Windows antigo) ou Finder (Mac) e, na página do dispositivo, selecione "Fazer Backup Agora". Atenção: marque a opção "Criptografar backup", caso contrário as senhas e os dados de saúde não serão incluídos no backup.
- <strong>Android</strong>: Cada marca tem seu próprio software para computador, como Huawei Phone Assistant, Xiaomi Assistant, Samsung Smart Switch. Conecte ao computador e siga as instruções.
- A vantagem do backup no computador é não precisar pagar por espaço em nuvem, e a restauração é muito mais rápida que pela nuvem. A desvantagem é que você precisa lembrar de conectar periodicamente para fazer o backup — e a maioria das pessoas não consegue fazer isso.

##### Opção 2: Backup em nuvem (a mais prática, recomendada para todos)

- <strong>iPhone</strong>: Ajustes > Seu nome > iCloud > Backup do iCloud > Ativar. O backup automático é feito quando o celular está conectado à energia, no Wi-Fi e com a tela bloqueada. Os 5GB grátis provavelmente não serão suficientes; recomenda-se assinar 50GB.
- <strong>Android</strong>: Cada marca tem sua função de backup em nuvem. Huawei: procure por "Backup em nuvem" nas configurações; Xiaomi: "Xiaomi Cloud"; OPPO/vivo: similar. Além disso, há o backup nativo do Google (Ajustes > Sistema > Backup) — ative-o também.
- A maior vantagem do backup em nuvem é "não precisar se preocupar" — é automático. A maior desvantagem é que a restauração demora muito para baixar, e o espaço gratuito geralmente não é suficiente.

#### III. Estratégia de backup por categoria: o que é importante, salve uma cópia extra separada

O backup completo do dispositivo é a rede de segurança. Mas algumas coisas são tão importantes que merecem uma cópia extra separada:

##### Fotos e vídeos (os ativos digitais mais preciosos)

- <strong>Plano de seguro duplo</strong>: Ative a sincronização automática do iCloud Fotos / Google Fotos e, ao mesmo tempo, a cada poucos meses, copie manualmente as fotos para o computador ou HD externo. Assim, uma cópia na nuvem e uma cópia local, uma serve de backup da outra.
- <strong>Plano sem gastar dinheiro</strong>: O Google Fotos oferece 15GB grátis; você pode configurar para "Qualidade compactada" e economizar espaço. Ou, uma vez por mês, copie todas as fotos para o computador com o cabo de dados.

##### Contatos (fácil de ignorar, mas extremamente importante)

- Os contatos do iPhone, por padrão, sincronizam com o iCloud. Se a sincronização estiver ativada, não precisa de backup extra. Mas, para ficar ainda mais seguro, você pode acessar o iCloud.com e exportar um arquivo vCard para o computador.
- Os contatos do Android geralmente sincronizam com o Google ou com a nuvem da marca. Vá nas configurações do app Contatos e exporte um arquivo .vcf — isso é um backup completo.

##### Histórico de conversas do WeChat (tratamento separado, prioridade máxima)

Este deve ser tratado separadamente, porque o histórico do WeChat muitas vezes fica incompleto no backup completo do dispositivo, e as ferramentas de migração de celular simplesmente não conseguem transferi-lo.

- <strong>Método 1: Migrar para o novo celular</strong>. WeChat → Eu → Ajustes → Geral → Migração e Backup de Histórico de Conversas → Migrar → Migrar para Celular/Tablet. Conecte o celular antigo e o novo na mesma rede Wi-Fi, escaneie o código QR e transfira. Atenção: não saia do WeChat no celular antigo até a migração terminar.
- <strong>Método 2: Backup para o computador</strong>. Instale o WeChat para PC no computador. No canto inferior esquerdo, três barras → Migração e Backup → Backup e Restauração → Fazer Backup do Histórico de Conversas no Computador. Depois, ao trocar de celular, restaure no novo.
- <strong>Método 3: Backup para a nuvem</strong>. O WeChat também suporta backup para o iCloud ou para o espaço em nuvem do celular. Mas atenção: este backup só pode ser restaurado no mesmo celular, não permite restauração entre dispositivos. Se for trocar de celular, é preciso usar os dois primeiros métodos.

#### IV. Guia de troca de celular: do antigo para o novo

Trocar de celular é motivo de alegria, mas se os dados não forem transferidos, vira uma dor de cabeça. Trate cada caso separadamente:

##### Upgrade na mesma marca (o mais simples)

- <strong>iPhone → Novo iPhone</strong>: Ao ligar e ativar o novo iPhone, coloque o antigo por perto. Aparecerá automaticamente o "Início Rápido". Use o celular antigo para escanear o padrão no novo. Todos os dados, configurações, layout de apps serão transferidos exatamente como estavam, incluindo as senhas de Wi-Fi. Leva cerca de 20 a 30 minutos.
- <strong>Android da mesma marca</strong>: Use a ferramenta de migração nativa da marca. Huawei: "Phone Clone"; Xiaomi: "Mi Mover"; OPPO: "Phone Switch"; vivo: "EasyShare". Os passos são similares: instale o mesmo app nos dois celulares, conecte por QR code, selecione o que deseja transferir e inicie.

##### Troca entre marcas diferentes (Android para Android, marcas diferentes)

Use ferramentas de migração de terceiros ou o app de migração da marca antiga (a maioria dos apps de migração das marcas também suporta transferência para outros Androids). O que pode ser transferido: contatos, fotos, SMS, histórico de chamadas, alguns apps. O que não pode: estado de login nos apps (você precisará fazer login novamente), histórico de conversas do WeChat (use a função de migração do próprio WeChat).

##### Troca entre plataformas (Android para iPhone, ou vice-versa)

- <strong>Android → iPhone</strong>: A Apple tem o app "Migrar para o iOS". Baixe no Android e, ao ativar o novo iPhone, selecione "Transferir Dados do Android". Transfere contatos, fotos, SMS e outros dados básicos, mas não os dados dos apps. O histórico do WeChat precisa ser migrado pela função do próprio WeChat.
- <strong>iPhone → Android</strong>: Cada marca Android tem sua ferramenta de migração correspondente, mas, sinceramente, a experiência de migração entre plataformas não é tão boa quanto na mesma plataforma. O mais importante é fazer separadamente antes: exportar contatos, fazer backup das fotos, migrar o histórico do WeChat. O resto, devagar se resolve.

#### V. A regra de ouro do backup: princípio 3-2-1

Este é um princípio clássico na área de segurança de dados, simples e fácil de lembrar:

- <strong>3</strong>: Dados importantes devem ter pelo menos três cópias (uma original, duas de backup).
- <strong>2</strong>: Os backups devem usar dois tipos diferentes de mídia de armazenamento (por exemplo, uma na nuvem, uma em HD externo).
- <strong>1</strong>: Pelo menos uma cópia de backup deve estar em um local físico diferente (para prevenir que incêndio, roubo etc. destruam todos os dados simultaneamente).

Para uma pessoa comum, conseguir "uma cópia na nuvem e uma no computador" já é muito bom. Não precisa complicar demais. O importante é realmente fazer.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Atenção especial ao histórico de conversas do WeChat

{class="mt-1"}
O histórico de conversas do WeChat não pode ser migrado por nenhuma ferramenta de migração de celular! Ele não está coberto pelo backup completo do dispositivo. É obrigatório usar a função nativa "Migração de Histórico de Conversas" do WeChat ou fazer backup para o WeChat no computador. Muita gente só descobre que perdeu todo o histórico depois de trocar de celular — aí já é tarde, pois o celular antigo pode já ter sido restaurado para as configurações de fábrica.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Exercício: faça um simulado completo de backup

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Verifique se o Backup do iCloud ou o backup em nuvem da marca está ativado e confirme a data do último backup.
2. Faça backup manual das fotos: conecte o celular ao computador com o cabo de dados e copie as pastas DCIM e Pictures para o computador.
3. Faça backup dos contatos: usuários iPhone exportem vCard pelo iCloud.com; usuários Android exportem arquivo .vcf nas configurações do app Contatos.
4. Faça backup do histórico do WeChat: abra o WeChat → Eu → Ajustes → Geral → Migração e Backup de Histórico de Conversas → Fazer backup no computador.
5. Copie o arquivo vcf de contatos e a pasta de fotos exportados para um HD externo ou pen drive, completando a parte do "3-2-1": "uma cópia offline em outro lugar".
:::
