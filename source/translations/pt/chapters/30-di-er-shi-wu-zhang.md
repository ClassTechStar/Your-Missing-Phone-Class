---
id: di-er-shi-wu-zhang
num: 25
part: chao-yue-pian
nav: Capítulo 25: Descarte de celulares usados e herança digital
toc: default
kind: chapter
---

### Capítulo 25: Descarte de celulares usados e herança digital

{class="chapter-intro mb-4"}
Ei, pessoal, depois de mais de vinte capítulos de "treinamento", acredito que você já passou de um "novato digital" a um usuário de celular bastante confiante. Mas a vida tecnológica sempre tem ciclos — o novo amor eventualmente se torna um velho conhecido. Quando você estiver pronto para "aposentar" seu velho companheiro, sabe como se despedir de forma digna e segura?

#### I. A "eutanásia" do celular antigo: guia de venda ou doação segura

Princípio fundamental: a limpeza de dados não é "excluir", é "sobrescrever". Muitas pessoas acham que basta arrastar as fotos para a lixeira e esvaziar a galeria para resolver tudo. Resultado: depois de repassar o celular, o novo dono usa um software de recuperação de dados e — pronto — fotos antigas, históricos de conversa, fotos de documentos de identidade, tudo de volta. Esse tipo de "vexame público" acontece todos os anos.

1. <strong>"Faxina geral" pessoal</strong>: faça um último backup completo, saia de todas as contas (iCloud, Huawei/Xiaomi/Samsung, Google), desative a função "Buscar meu celular" — caso contrário, o próximo usuário será barrado pela tela de bloqueio de ativação.
2. <strong>Execute a "formatação" definitiva</strong>: a "Restauração de fábrica" dos celulares modernos geralmente inclui exclusão criptografada — ela destrói a própria chave de criptografia. Sem a chave, todos os dados do disco se tornam instantaneamente ilegíveis.
3. <strong>Última "camuflagem" (apenas para dispositivos muito antigos)</strong>: celulares modernos (iOS 8+, Android 6+) já possuem criptografia completa de disco (FBE) por padrão. A restauração de fábrica destrói a chave de criptografia, tornando os dados teoricamente irrecuperáveis. <strong>Esta etapa não é necessária</strong>. Apenas para dispositivos muito antigos sem criptografia (anteriores a 2015), é necessário preencher o armazenamento com arquivos inúteis após a restauração de fábrica e executar a restauração novamente.

<strong>Tabela de referência rápida de caminhos de exclusão de dados por marca</strong>: embora o princípio seja o mesmo, cada marca esconde a "restauração de fábrica" em um local ligeiramente diferente. As principais diferenças estão abaixo.

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Marca</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Caminho de exclusão</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Diferenças principais e observações</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Huawei</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Config. > Sistema e atualizações > Redefinir > Restaurar padrão de fábrica</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">É necessário sair da conta Huawei e desativar "Buscar dispositivo" primeiro, caso contrário, o bloqueio de ativação será acionado; no modo puro, pode ser necessária verificação de senha.</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xiaomi / Redmi</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Config. > Meu dispositivo > Restaurar padrão de fábrica</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Na parte inferior, há as opções "Formatar cartão SD virtual" e "Limpar todo o conteúdo e configurações", ambas devem ser marcadas; saia da conta Xiaomi e desative "Buscar dispositivo" primeiro.</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OPPO / OnePlus</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Config. > Outras configurações > Restaurar telefone > Limpar completamente todos os dados</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">O ColorOS oferece o modo "Limpeza completa", que sobrescreve o armazenamento várias vezes; é necessário inserir a senha de bloqueio de tela para confirmar.</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">vivo</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Config. > Gerenciamento do sistema > Backup e redefinição > Limpar todos os dados</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Marque "Formatar armazenamento do telefone" para limpar também a área do cartão SD; é necessário sair da conta vivo e desativar "Buscar telefone".</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Samsung</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Config. > Gerenciamento geral > Redefinir > Restaurar padrão de fábrica</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">É necessário remover a conta Samsung e desativar "Buscar meu celular" primeiro; alguns modelos possuem a opção "Sobrescrita automática", recomenda-se ativá-la.</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">iPhone</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Config. > Geral > Transferir ou Redefinir iPhone > Apagar Todo o Conteúdo e Ajustes</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">É necessário sair do Apple ID primeiro, caso contrário, o próximo usuário será bloqueado pelo bloqueio de ativação do iCloud; iOS 15+ suporta "Manter dados do iCloud ao sair" para consulta posterior.</td>
                            </tr>
                        </tbody>
                    </table>
```

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>As três coisas mais fáceis de esquecer

{class="list-disc pl-6 mt-2 space-y-1"}
- <strong>Não sair das contas</strong>: o celular é vendido, o comprador é bloqueado remotamente e você também não consegue acessar. No final, só resta ir ao suporte oficial com documento de identidade para desbloquear.
- <strong>Cartão SD não removido</strong>: a restauração de fábrica não formata as fotos no cartão SD externo. Lembre-se de removê-lo manualmente ou formatá-lo separadamente.
- <strong>Periféricos USB/OTG não desconectados</strong>: se houver periféricos conectados durante o processo de exclusão, os dados do periférico podem ser apagados por engano, ou a exclusão pode ser interrompida.
:::

#### II. Herança digital: como sua alma social será preservada?

Os dados dentro do celular há muito deixaram de ser "virtuais". Eles carregam suas finanças, relações sociais, produções criativas e até sua "identidade digital". <strong>Após o falecimento de uma pessoa, como esses ativos devem ser tratados?</strong> Isso não é mais uma questão abstrata, mas um problema real enfrentado por cada vez mais famílias — parentes não sabem as senhas, plataformas não permitem herança, criptomoedas se perdem para sempre.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-gavel mr-2"></i>Base legal: Artigo 49 da Lei de Proteção de Informações Pessoais

{class="mt-1"}
O Artigo 49 da Lei de Proteção de Informações Pessoais da República Popular da China, em vigor desde 2021, estabelece claramente: <strong>Em caso de falecimento de uma pessoa natural, seus parentes próximos podem, para seus próprios interesses legítimos e justos, exercer os direitos de consulta, cópia, correção, exclusão, etc., sobre as informações pessoais do falecido, conforme previsto neste capítulo; salvo disposição em contrário feita pelo falecido em vida.</strong>

{class="mt-2"}
Isso significa que:

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>Parentes próximos têm base legal</strong> para solicitar às plataformas o tratamento das contas e informações pessoais do falecido.
- "Interesses legítimos e justos" geralmente incluem tratar de herança, fechar contas, excluir dados sensíveis de privacidade, etc.
- Se o falecido tiver deixado testamento ou acordo dispondo de outra forma (como designar um contato de herança), prevalece o disposto.
- As plataformas não podem recusar com base genérica em "privacidade do usuário", mas os procedimentos específicos variam de plataforma para plataforma.
:::

{class="font-semibold mt-4 mb-1"}
##### 1. WeChat e Alipay: a conta não pode ser herdada, mas os fundos podem

Estes dois aplicativos mais usados pelos chineses têm regras diferentes:

- <strong>Conta WeChat</strong>: de acordo com o "Contrato de Licença e Serviço do Software WeChat da Tencent", a propriedade da conta pertence à Tencent, e o usuário possui apenas o direito de uso. <strong>A conta em si não pode ser herdada nem transferida</strong>. No entanto, o <strong>saldo e os fundos do WeChat Pay</strong> são propriedade pessoal. Parentes próximos podem solicitar o saque ou transferência à Tenpay apresentando certidão de óbito, comprovante de parentesco e escritura pública de herança.
- <strong>Alipay</strong>: a conta também não pode ser herdada diretamente, mas o saldo do Alipay, Yu'ebao, Licaitong e outros <strong>fundos são bens herdáveis</strong>. Os herdeiros podem fazer a solicitação pela linha direta de atendimento do Alipay ou presencialmente, apresentando certidão de óbito e escritura pública de herança; produtos financeiros do Ant Fortune exigem o processo da gestora do fundo.
- <strong>Histórico de conversas</strong>: legalmente, é considerado privacidade pessoal. A plataforma não fornecerá ativamente aos familiares. Se envolver pistas sobre herança, pode ser solicitado por via judicial ou notarial.

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>O que nunca fazer

{class="list-disc pl-6 mt-2 space-y-1"}
- <strong>Não entregue a senha da conta do falecido diretamente para familiares "continuarem usando"</strong> — isso viola os termos da plataforma e, se os fundos forem congelados ou o controle de risco for acionado, será ainda mais difícil provar.
- <strong>Não tente usar o celular do falecido para receber códigos de verificação e "sacar"</strong> — pode ser considerado uso indevido e, ao contrário, violar a lei.
- <strong>Não demore</strong>: algumas contas que ficam muito tempo sem login são automaticamente canceladas, e recuperar os fundos se torna mais difícil.
:::

{class="font-semibold mt-4 mb-1"}
##### 2. "Contato de Herança" da Apple: designar com antecedência, metade do trabalho com o dobro do resultado

A partir do iOS 15.2, a Apple introduziu a função "Contato de Herança", permitindo que o usuário designe antecipadamente um contato de confiança. Após o falecimento, esse contato pode solicitar acesso aos dados do iCloud do falecido (fotos, notas, contatos, etc.) apresentando <strong>certidão de óbito + chave de acesso de contato de herança</strong>. Passos:

1. No iPhone, acesse <strong>[Ajustes] &gt; [seu nome] &gt; [Início de Sessão e Segurança] &gt; [Contato de Herança]</strong>.
2. Toque em "Adicionar Contato de Herança" e confirme a identidade com Face ID.
3. Selecione o contato (da lista de contatos). O sistema gerará uma <strong>chave de acesso</strong>.
4. Envie a chave de acesso por SMS, e-mail ou em papel impresso para a pessoa e lembre-a de guardar em local seguro.
5. É possível adicionar vários contatos como backup, evitando ponto único de falha.

A pessoa designada não precisa de um dispositivo Apple. Com a chave e a certidão de óbito, pode solicitar acesso no site oficial da Apple. Todo o processo geralmente é concluído em até 7 dias.

{class="font-semibold mt-4 mb-1"}
##### 3. "Gerenciador de Conta Inativa" do Google: cuidando automaticamente do pós-vida

O Google oferece o "Gerenciador de Conta Inativa (Inactive Account Manager)", que executa automaticamente ações predefinidas quando o usuário fica muito tempo sem fazer login — este é um dos mecanismos de herança digital mais completos atualmente.

1. Acesse <strong>myaccount.google.com/inactive</strong> e faça login na sua conta Google.
2. Defina o período de timeout: 3 / 6 / 12 / 18 meses sem login para acionar.
3. Adicione contatos de confiança (até 10 pessoas) e configure quais dados cada um pode acessar (Gmail, Google Fotos, Google Drive, etc.).
4. Opcional: configure uma resposta automática de e-mail informando aos remetentes que você não pode mais responder.
5. Escolha final: ao expirar, <strong>compartilhar os dados com os contatos</strong> ou <strong>excluir diretamente a conta</strong>.
6. Configure um número de telefone como verificação de segurança para evitar acionamento acidental.

{class="font-semibold mt-4 mb-1"}
##### 4. Contas sociais chinesas: processos de memorialização e exclusão

As principais plataformas sociais chinesas tratam as contas de falecidos de duas formas: <strong>"memorialização" (manter a conta para homenagem de amigos e familiares)</strong> e <strong>"exclusão" (remoção completa)</strong>. Os familiares podem solicitar ao suporte da plataforma apresentando certidão de óbito, comprovante de parentesco e documento de identidade do solicitante.

- <strong>Weibo</strong>: suporta "memorialização" de conta. Familiares fornecem certidão de óbito para solicitar. A conta é bloqueada (não é possível fazer login), mas o conteúdo é preservado. A página principal exibe "Esta conta foi definida como conta memorial". Também é possível solicitar exclusão, exigindo escritura pública de herança.
- <strong>Douyin (TikTok chinês)</strong>: através de "Eu - Configurações - Feedback e Ajuda - Conta e Segurança - Excluir conta" ou atendimento humano, enviar certidão de óbito, comprovante de parentesco e documento do solicitante. Após aprovação, pode-se excluir ou converter para estado memorial.
- <strong>Bilibili</strong>: pelo canal de suporte, enviar comprovante de falecimento e comprovante de parentesco para solicitar exclusão da conta ou preservação como página memorial; o tratamento de conteúdo histórico de criadores exige declaração de direitos autorais.
- <strong>Xiaohongshu (RED)</strong>: através do suporte oficial, enviar certidão de óbito e comprovante de parentesco para solicitar exclusão da conta e remoção de conteúdo.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Lembretes importantes

{class="list-disc pl-6 mt-2 space-y-1"}
- As regras de cada plataforma são atualizadas; consulte as orientações mais recentes do suporte oficial antes de prosseguir.
- Recomenda-se digitalizar todos os documentos comprobatórios antes de enviar; guarde os originais em local seguro.
- Ao tratar de várias plataformas de uma vez, solicite uma <strong>escritura pública de herança</strong> unificada, economizando idas repetidas a cartórios.
:::

{class="font-semibold mt-4 mb-1"}
##### 5. Os desafios da herança de ativos digitais

Além das contas sociais, cada vez mais pessoas possuem <strong>ativos digitais de real valor</strong>, cuja herança é ainda mais complexa:

- <strong>Criptomoedas (Bitcoin, Ethereum, etc.)</strong>: baseadas no princípio "chave privada = propriedade". <strong>Sem a chave privada, o ativo desaparece</strong>. Herdeiros não podem "recorrer" na blockchain com documentos legais. Sugestão: armazene a frase mnemônica/chave privada em partes, em vários locais físicos seguros (como cofre bancário + cofre doméstico), e indique o método de acesso no testamento.
- <strong>Contas em exchanges</strong>: semelhantes a contas bancárias. Pode-se solicitar à exchange (como Binance, OKX) com escritura pública de herança, mas o processo em exchanges internacionais é demorado.
- <strong>Domínios</strong>: são bens herdáveis. O herdeiro pode solicitar a transferência no registrador de domínios (como Alibaba Cloud, GoDaddy) apresentando a escritura pública de herança.
- <strong>Propriedade intelectual (artigos originais, vídeos, patentes, direitos autorais de software)</strong>: os direitos patrimoniais de autor são herdáveis (direitos morais não). Os rendimentos podem ser usufruídos pelos herdeiros até 50 anos após a morte do autor.
- <strong>Armazenamento em nuvem e drives virtuais</strong>: o conteúdo dos dados pertence ao indivíduo e é herdável; mas algumas plataformas estipulam que a conta em si não pode ser transferida, sendo necessário baixar os dados antes de excluir a conta.

::: div .danger-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>O custo real do "desaparecimento" de criptomoedas

{class="mt-1"}
De acordo com o relatório da Chainalysis, globalmente já existem <strong>mais de 3 milhões de bitcoins</strong> perdidos para sempre devido à perda de chaves privadas, o equivalente a um sexto do total existente. Se você possui ativos em criptomoedas, certifique-se de que pelo menos uma pessoa de sua absoluta confiança conheça o <strong>caminho de recuperação</strong> — caso contrário, essa riqueza permanecerá para sempre adormecida na blockchain.
:::

{class="font-semibold mt-4 mb-1"}
##### 6. Um modelo de "testamento digital"

O testamento tradicional de bens não cobre ativos digitais. Recomenda-se que você atualize anualmente um anexo de "testamento digital" e o mantenha junto com o testamento formal. O modelo a seguir serve como referência:

::: div .bg-light .dark:bg-gray-700 .rounded-lg .p-4 .mt-2 .mb-3 .text-sm
{class="font-semibold mb-2"}
"Anexo de Disposição de Ativos Digitais Pessoais"(Modelo)

{class="mb-1"}
<strong>Parte I: Lista de contas</strong> (registre apenas o nome da conta e a plataforma, <strong>não escreva senhas</strong>)

{class="list-disc pl-6 mb-2 space-y-0.5"}
- Redes sociais: WeChat (conta xxx), Weibo, Douyin, Bilibili, Xiaohongshu, etc.
- Pagamentos: Alipay, WeChat Pay, apps de cada banco
- Nuvem: iCloud, Huawei Cloud, Xiaomi Cloud, conta Google, conta Microsoft
- E-mail: QQ Mail, NetEase Mail, Gmail, etc.
- Outros: drives virtuais, serviços de assinatura, contas de jogos, etc.

{class="mb-1"}
<strong>Parte II: Plano de custódia de senhas</strong>

{class="list-disc pl-6 mb-2 space-y-0.5"}
- Método de armazenamento da senha mestra: use um gerenciador de senhas (como Bitwarden, 1Password). A senha mestra deve ser escrita em papel e lacrada no cofre doméstico.
- Chave de recuperação/frase mnemônica: armazenamento fragmentado, em pelo menos dois locais físicos (como caixa de segurança bancária + cofre doméstico).
- Pessoa autorizada para consulta: nome, número do documento de identidade, relação com o titular, contato.

{class="mb-1"}
<strong>Parte III: Vontades de disposição</strong>

{class="list-disc pl-6 mb-2 space-y-0.5"}
- Para cada tipo de conta, deseja "memorialização" ou "exclusão".
- Se os dados do iCloud / Google devem ter "Contato de Herança" ou "Gerenciador de Conta Inativa" designado.
- Quem herda os ativos criptografados, com instruções sobre o caminho de obtenção da chave privada.
- Quem usufrui dos rendimentos de obras com direitos autorais.

{class="mb-1"}
<strong>Parte IV: Contatos e plataformas</strong>

{class="list-disc pl-6 space-y-0.5"}
- Nome do executor de confiança, contato, contato reserva.
- Canais de suporte das plataformas habituais e lista de documentos comprobatórios necessários.
- Data de atualização deste anexo: ____/__/____, data da próxima revisão: ____/__/____.
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Aviso legal sobre "senhas"

{class="mt-1"}
Escrever senhas diretamente no testamento apresenta risco de vazamento, e após a divulgação do testamento, todos os herdeiros poderão vê-las. <strong>A prática mais segura é: no testamento, escreva apenas "lista de contas + vontades de disposição + local de custódia da senha". A senha real deve ser transmitida separadamente ao executor de confiança através da senha mestra do gerenciador de senhas</strong>. Isso atende aos requisitos legais e reduz o risco de vazamento de senhas.
:::

#### III. A última etapa ecológica

Um celular contém dezenas de metais, incluindo ouro, prata, cobre e terras raras. O descarte inadequado polui o solo e desperdiça recursos. Existem três categorias de canais de reciclagem corretos, cada uma com seu foco:

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Canal</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Valor de reciclagem</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Segurança de dados</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cenário aplicável</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Troca oficial (Huawei/Apple/Xiaomi, etc.)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Médio, frequentemente com cupons de subsídio adicionais</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mais alto, processo padronizado oficial</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mais vantajoso quando se pretende trocar por um modelo novo da mesma marca</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Plataformas de reciclagem de terceiros (Aihuishou, Zhuanzhuan, Huishoubao, etc.)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ligeiramente mais alto, comparável</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Alto, com relatório de limpeza de dados</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Para converter diretamente em dinheiro, sem vínculo com marca</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Doação solidária (escolas rurais, instituições de caridade)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sem retorno financeiro</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">É necessário fazer a exclusão completa por conta própria</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dispositivo ainda funcional, desejo de fazer o bem</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Reaproveitamento próprio (adaptação para outro uso)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Economiza o custo de um novo dispositivo</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">O proprietário original continua usando, sem risco</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Desempenho do dispositivo ainda razoável, necessidade de adaptação em casa</td>
                            </tr>
                        </tbody>
                    </table>
```

- <strong>Reciclagem/troca oficial</strong>: a forma mais recomendada, processo padronizado, segurança de dados garantida. Apple, Huawei, Xiaomi e outras marcas têm portais de "troca" em seus sites oficiais. Após avaliação, o valor pode ser abatido na compra de um novo aparelho.
- <strong>Plataformas de reciclagem confiáveis</strong>: escolha plataformas de reciclagem grandes e de boa reputação. Após o pedido, a coleta é feita por transportadora em domicílio. Após a inspeção, o pagamento é liberado. Certifique-se de escolher plataformas que <strong>forneçam "relatório de limpeza de dados"</strong> e guarde o comprovante.
- <strong>Doação solidária</strong>: entre em contato com escolas rurais locais ou organizações comunitárias de caridade. Celulares antigos podem ser convertidos em tablets educacionais ou telefones para idosos. <strong>Antes de doar, execute obrigatoriamente o processo completo de exclusão e remova todos os cartões SIM/SD</strong>.
- <strong>Reaproveitamento</strong>: transforme em navegador GPS para carro, central de controle de casa inteligente, câmera de monitoramento, babá eletrônica, porta-retratos digital. Um celular antigo pode durar vários anos adicionais.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-leaf mr-2"></i>A verdade sobre o lixo eletrônico

{class="mt-1"}
A placa de circuito de um celular contém metais preciosos como <strong>ouro, prata, paládio e cobre</strong>. Cada tonelada de placas de circuito descartadas contém dezenas de vezes mais ouro do que o minério de ouro. Mas se descartadas incorretamente, o chumbo, mercúrio e cádmio nelas presentes penetram no solo e nas águas subterrâneas, poluindo por décadas. <strong>Reciclar corretamente protege o meio ambiente e permite que metais escassos sejam reciclados.</strong>
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Prática: realize um "funeral padrão" para seu celular antigo

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Último backup completo: fotos para a nuvem, arquivos importantes para o computador, exportação e arquivamento do histórico de conversas.
2. Saia de todas as contas: iCloud / Huawei / Xiaomi / Google, desative "Buscar meu celular".
3. Remova o cartão SIM e o cartão SD, desconecte todos os periféricos OTG.
4. Execute a restauração de fábrica com criptografia. Se necessário, marque manualmente "Formatar armazenamento".
5. (Apenas dispositivos antigos) Preencha o armazenamento com arquivos inúteis e execute a restauração de fábrica mais uma vez.
6. Escolha seu próximo destino: troca oficial, plataforma de reciclagem confiável, doação solidária ou repasse para familiares.
7. Atualize simultaneamente sua "lista de herança digital", riscando o dispositivo descartado da lista.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-calendar-check mr-2"></i>Lista de tarefas do mês

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Para seu celular principal atual, designe um "Contato de Herança" da Apple ou configure o "Gerenciador de Conta Inativa" do Google.
2. Use o modelo desta seção para redigir um "Anexo de Disposição de Ativos Digitais Pessoais" e comunique à família o local de guarda.
3. Verifique se há mais de 2 celulares antigos ociosos em casa e agende uma reciclagem por canal oficial ou plataforma confiável.
:::
