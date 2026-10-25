---
id: di-er-shi-zhang-termux
part: jin-jie-pian
nav: Anexo: Terminal Linux portátil Termux
toc: sub
kind: supplement
---

### Apêndice do Capítulo 20: Termux — Ambiente de terminal Linux portátil em dispositivos Android

{class="chapter-intro mb-4"}
Se você acha que o modo desenvolvedor não é "hardcore" o suficiente e quer experimentar uma linha de comando Linux completa no celular, o Termux foi feito para você. Sem precisar de root, ele transforma um telefone Android comum em uma estação de trabalho Linux portátil — uma ferramenta poderosa para usuários avançados explorarem desenvolvimento e operações em dispositivos móveis.

#### 1. O que é o Termux

O Termux é um aplicativo de emulador de terminal e ambiente Linux de código aberto projetado especificamente para dispositivos Android. Ele oferece uma experiência completa de shell Linux no celular sem precisar de root. Como um aplicativo leve (cerca de 30 MB), o Termux suporta um rico ecossistema de software através do sistema de gerenciamento de pacotes APT, permitindo executar ferramentas como Python, Node.js, Git, SSH e até mesmo montar servidores ou realizar testes de penetração em dispositivos móveis.

A principal vantagem do Termux é sua leveza e alta escalabilidade, adequado para desenvolvimento, aprendizado e gerenciamento de sistemas em diversos cenários. Ele combina pacotes de software padrão com emulação de terminal precisa em uma solução de código aberto.

#### 2. Funcionalidades e características principais

##### 🖥️ Ambiente Linux completo

O Termux <strong>inclui apenas o Bash</strong> como shell nativo. Se quiser usar Zsh, fish ou outros shells, é necessário instalá-los manualmente pelo gerenciador de pacotes, por exemplo: <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install zsh</code> ou <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install fish</code>. O Termux também suporta editores como Vim, Nano, Emacs, oferecendo uma experiência de linha de comando quase nativa. Os usuários podem instalar mais de 2000 pacotes de software via "pkg install", incluindo ferramentas de desenvolvimento e segurança como GCC, OpenSSH, SQLMap.

##### 📦 Gerenciamento de pacotes poderoso

Usa o gerenciador de pacotes APT (semelhante ao Debian e Ubuntu), podendo instalar milhares de pacotes de software Linux, abrangendo ferramentas de desenvolvimento, ferramentas de rede, etc. Suporta múltiplas linguagens de programação como Python, Ruby, Node.js, Go, Rust, Swift.

##### 🔒 Recursos de segurança e rede

- <strong>Conexão remota SSH</strong>: suporta funções de cliente e servidor SSH, permitindo conectar-se remotamente a outros dispositivos ou transformar o telefone em um host SSH.
- <strong>Ferramentas de criptografia</strong>: oferece ferramentas como OpenSSL, suportando criptografia de dados e comunicação segura.
- <strong>Montagem de servidores</strong>: pode configurar Nginx ou Apache para criar servidores web estáticos.

##### 🔧 Integração e extensão do sistema

- Acesso à permissão de armazenamento do telefone para gerenciamento local de arquivos.
- Através do plugin Termux:API, é possível acessar sensores, câmera e outros recursos de hardware do Android.
- Suporte a teclado Bluetooth e conexão com monitor externo, com suporte completo a mouse.

#### 3. Ecossistema de plugins

O aplicativo principal do Termux pode ser expandido através de vários plugins opcionais, oferecendo funcionalidades e integrações adicionais:

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Nome do plugin</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Descrição da função</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:API</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Expõe funcionalidades da API Android para programas de linha de comando</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Boot</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Permite executar scripts na inicialização do dispositivo</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Float</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Oferece uma janela de terminal flutuante</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Styling</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Permite personalizar esquemas de cores e fontes do terminal</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Tasker</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Integra scripts Termux com o aplicativo de automação Tasker</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Widget</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Permite executar scripts a partir de widgets na tela inicial</td>
                            </tr>
                        </tbody>
                    </table>
```

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Aviso importante

{class="mt-1"}
O Termux e seus plugins devem ser instalados da mesma fonte, pois compartilham o mesmo sharedUserId. Misturar instalações de fontes diferentes (como F-Droid e GitHub) resultará em erros de instalação.
:::

#### 4. Guia de instalação e configuração

##### 📥 Etapas de instalação

1. <strong>Baixar o aplicativo</strong>: baixe e instale o Termux de fontes oficiais (F-Droid ou GitHub), sem necessidade de root.
2. <strong>Inicializar o sistema</strong>: após a primeira inicialização, aguarde a conclusão de "Installing bootstrap packages".
3. <strong>Obter permissão de armazenamento</strong>: execute <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-setup-storage</code> para obter permissão de acesso ao sistema de arquivos do telefone.
4. <strong>Atualizar fontes de software</strong>: execute <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code> para atualizar a lista de pacotes.

##### ⚙️ Otimizações básicas

- <strong>Trocar espelho</strong>: use o comando <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-change-repo</code> para trocar o espelho via interface gráfica (recomenda-se o espelho da Universidade Tsinghua).
- <strong>Configuração de atalhos</strong>: botão de volume para baixo simula Ctrl, botão de volume para cima simula Esc, aumentando a eficiência de digitação.
- <strong>Embelezamento da interface</strong>: instale Zsh + Oh My Zsh, configure temas e plugins.

#### 5. Cenários típicos de aplicação

##### 💻 Desenvolvimento e testes móveis

Monte um ambiente de desenvolvimento completo no celular, escreva e execute scripts Python, compile programas C com GCC, gerencie repositórios de código com Git, sincronize com servidores remotos via SSH.

##### 🖥️ Operações de servidor

Gerencie servidores remotamente via SSH, execute tarefas de manutenção de sistema, análise de logs, resolva problemas de servidor a qualquer hora e em qualquer lugar.

##### 📚 Aprendizado de Linux

Oferece um ambiente Linux real, sendo uma plataforma ideal para aprender linha de comando e gerenciamento de sistema. Permite praticar scripts Shell, gerenciamento de permissões de arquivos Linux (como <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chmod 755</code> para definir bits de permissão rwxr-xr-x, <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chown user:group</code> para modificar a propriedade do arquivo, <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls -l</code> para visualizar as permissões dos três grupos de nove bits de owner/group/other) e outros comandos básicos. Note que este é o modelo clássico de permissões Unix/Linux de "três grupos, nove bits" (owner / group / other × leitura / escrita / execução), que é um sistema completamente diferente das ACLs (listas de controle de acesso) do Windows NTFS.

##### 🔐 Testes de segurança de rede

Instale ferramentas de segurança como Nmap, SQLMap, Hydra, Metasploit para realizar varreduras de rede e testes de penetração.

#### 6. Versão e compatibilidade

A versão estável mais recente do Termux é a v0.118.2, compatível com dispositivos Android ≥ 7. É importante notar que o Termux pode apresentar instabilidade no Android 12 e versões superiores. Recomenda-se acompanhar o changelog oficial para obter as informações de compatibilidade mais recentes.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Resumo

{class="mt-1"}
O Termux traz a poderosa experiência de terminal Linux para dispositivos Android, transformando o celular em uma ferramenta portátil de desenvolvimento e aprendizado. Seja você desenvolvedor, administrador de sistemas ou entusiasta de tecnologia, pode usar o Termux para desfrutar de uma experiência completa de linha de comando em dispositivos móveis, realizando o conceito de "Linux no bolso".
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Mãos à obra: execute seu primeiro comando Linux no celular

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Baixe e instale o Termux do F-Droid, aguarde a inicialização concluir na primeira execução.
2. Execute <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code> para atualizar os pacotes.
3. Instale o Python: <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install python</code>.
4. Digite <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python3 -c "print('Hello from Termux!')"</code> e sinta a diversão de executar código no celular.
:::
