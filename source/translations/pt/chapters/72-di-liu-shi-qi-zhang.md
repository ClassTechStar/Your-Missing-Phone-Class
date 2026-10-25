---
id: di-liu-shi-qi-zhang
num: 67
part: ios-kai-fa-pian
nav: Capítulo 67: Refinamento e publicação — colocando o app na App Store
toc: default
kind: chapter
---

### Capítulo 67: Refinamento e publicação — testes, depuração e publicação na App Store

{class="chapter-intro mb-4"}
O App ficou pronto, e agora? Este capítulo responde às três coisas que levam de "está rodando" a "está pronto para entregar": como depurar e achar bugs com eficiência, como escrever testes para evitar regressões e como levar o App à App Store para o mundo inteiro baixar. Publicar não é só cerimônia — é a linha que separa uma obra de um produto.

#### 1. Os três instrumentos de depuração: print, breakpoints e preview

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ferramenta</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Para que serve</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Como usar</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">print + console</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ver logs de execução</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">No código, print("valor=\(x)") e veja a saída no console na parte inferior do Xcode</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Depuração com breakpoints</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fazer o programa parar em uma linha e ver os valores das variáveis</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Clique ao lado do número da linha para criar a marca azul; a execução pausa ao chegar ali e você avança passo a passo</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Preview do SwiftUI + depurador</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ver a interface e a hierarquia de views em tempo real</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Canvas do #Preview + inspetor View Hierarchy em tempo de execução</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Os três instrumentos de depuração

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Dica: como ler um crash?

{class="mt-1"}
Quando o Swift trava, o console imprime "Fatal error" seguido do motivo, e o Xcode para na linha do erro e a destaca. O histórico de travamentos em aparelhos reais pode ser visto em Xcode → Window → Organizer → Crashes (requer conta paga). Priorize pesquisar "primeira frase do motivo do erro + swiftui" — só uma pergunta precisa gera uma resposta precisa.
:::

#### 2. Testes: um seguro para o código

O teste manual não é confiável — você mexe em uma função e outra quebra às escondidas. Testes são o "remendo do arrependimento" e o "colete à prova de balas" ao mesmo tempo. No iOS usa-se o framework XCTest, em dois tipos:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Nível</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">O que testa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Target</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Velocidade</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Teste unitário</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lógica pura (cálculos, validações)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppTests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Segundos</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Teste de UI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Comportamento real da interface</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppUITests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minutos</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Teste manual</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sensação e experiência de pessoas reais</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sempre necessário</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Níveis de teste no iOS (o projeto-modelo já vem com dois Test Targets)

::: div .code-block
:::inline div .code-head
<span>SWIFT · Exemplo de teste unitário</span><span class="dots">···</span>
:::

```
import XCTest

// Extraia lógica como "string de valor para número" numa função pura
func parseAmount(_ input: String) -> Double? {
    guard let v = Double(input.trimmingCharacters(in: .whitespaces)),
          v > 0 else { return nil }
    return v
}

final class AmountTests: XCTestCase {
    func testEmptyInputReturnsNil() {
        XCTAssertNil(parseAmount(""))
    }
    func testNegativeReturnsNil() {
        XCTAssertNil(parseAmount("-5"))
    }
    func testNormalValueParses() {
        XCTAssertEqual(parseAmount("12.5"), 12.5)
    }
}
```
:::

Rodar os testes: ⌘U. Depois que está tudo verde, mexer no código fica muito mais tranquilo. A validação de valores e os cálculos de resumo do livro-caixa merecem testes unitários protegendo tudo.

#### 3. Assinatura e empacotamento: carimbando o App

Todo App iOS precisa ser assinado para poder ser instalado — é a prova de que "este pacote veio de você e não foi adulterado". A hierarquia é a seguinte:

- Fase de aprendizado: Apple ID gratuito + assinatura automática do Xcode (Personal Team); roda em aparelho real, com renovação a cada 7 dias;
- Fase de distribuição: a conta de desenvolvedor paga (99 dólares/ano) emite os certificados e os perfis de provisionamento, necessários para publicar e instalar a longo prazo.

Empacotar: no menu do Xcode, Product → Archive; após o build, no Organizer use Distribute App → escolha App Store Connect → faça o upload. O archive precisa ter o Generic iOS Device como destino (não o simulador) — um passo que os iniciantes costumam esquecer.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Alerta de armadilha: perdeu o certificado = atualizações paradas

{class="mt-1"}
Se o certificado de assinatura e a chave privada se perderem, você não consegue mais publicar atualizações do App antigo — os usuários só conseguiriam instalar o aplicativo como se fosse "novo". Faça backup do certificado com cuidado (exporte o .p12 do keychain) e guarde bem a senha. Para ajudar, a Apple oferece a "assinatura automática" e o gerenciamento de certificados na nuvem (marque Automatically manage signing no Xcode), o que elimina a maioria das armadilhas manuais.
:::

#### 4. O processo completo de publicação na App Store

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Registrar conta de desenvolvedor</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> Preparar materiais da loja</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> Enviar o build</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> Preencher informações de privacidade e revisão</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Revisão da Apple (1-7 dias)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> Publicado</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 5: os seis passos para publicar na App Store
:::

- Cadastro: developer.apple.com, conta individual por 99 dólares/ano;
- Materiais: ícone (1024×1024, sem cantos arredondados — a Apple recorta sozinha), capturas de tela (nos vários tamanhos de iPhone), descrição e link da política de privacidade;
- Questionário de privacidade: declare com honestidade quais dados são coletados — um livro-caixa que não se conecta à internet pode marcar "não coleta nenhum dado";
- Revisão: a primeira submissão costuma levar de 1 a 7 dias de espera; se for rejeitado, corrija item a item conforme as "notas da revisão" — a Apple costuma escrever os motivos da rejeição de forma bem específica, basta seguir;
- TestFlight: antes de publicar, envie a versão de teste para amigos (até 10.000 pessoas), colete um ciclo de feedback e só então submeta de verdade — postura bem profissional.

#### 5. Como criar os materiais da loja: a primeira impressão vale downloads

A página da loja é a vitrine que o usuário vê ao "passar em frente à loja". Três materiais definem a primeira impressão:

- Ícone: 1024×1024; não vale improvisar com uma captura de tela. Se você não tem habilidade de design, use uma ferramenta de IA para gerar uma forma simples; ele só passa no teste se continuar reconhecível de relance mesmo reduzido na tela inicial;
- Capturas de tela: pelo menos 2 conjuntos (tamanhos principais do iPhone), mostrando os cenários de uso mais centrais; cada uma com uma frase em linguagem humana ("Anote um gasto em um segundo" é dez vezes melhor do que "Solução eficiente de gestão financeira");
- Descrição: a primeira frase deve deixar claro "o que é + para quem é"; nada de empilhar "o mais profissional, o mais poderoso" — sinceridade funciona melhor do que exagero.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mãos à obra: "entregue" o livro-caixa uma vez

#### 6. Relatório de crashes e mini checklist de performance

Antes de publicar o App, vale dedicar meia hora a cada uma destas duas tarefas:

##### 1. Monitoramento de crashes

Não travar nos seus testes não significa que não vai travar no celular dos usuários. A Apple oferece relatórios de crash gratuitos no Xcode Organizer (contas pagas veem logs de crash de aparelhos reais); uma solução mais prática é integrar um SDK de terceiros (como o Firebase Crashlytics). Publicar sem monitoramento de crashes é dirigir de olhos fechados.

##### 2. Quatro checagens de performance

1. Listas com LazyVStack / List: listas longas não devem ser montadas com um VStack comum — carregamento preguiçoso é a primeira lição de performance;
2. Não force as imagens originais: use AsyncImage (imagens remotas) e o cache do sistema; uma imagem original de 5 MB é capaz de travar aparelhos antigos;
3. Não faça trabalho pesado na thread principal: rede e arquivos grandes devem passar por async/await;
4. Meça com o Instruments: o analisador de performance que vem no Xcode (Time Profiler, checagem de vazamento de memória) — primeiro meça, depois otimize; não confie no feeling.

{class="mt-1"}
① Adicione 3 testes unitários para lógicas como parseAmount (rodando verdes com ⌘U); ② use um breakpoint para caçar com as próprias mãos um crash que você mesmo criou e conserte-o; ③ gere um pacote com Product → Archive e convide amigos para testar pelo TestFlight; ④ se sobrar energia, registre a conta de desenvolvedor e submeta o livro-caixa de verdade para publicação. Os três primeiros passos dão para fazer esta noite.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumo do capítulo

- Três instrumentos de depuração: logs com print, breakpoints, preview do SwiftUI e inspetor de views
- XCTest: teste unitário (⌘U) + teste de UI + teste manual, já pré-configurado no modelo
- Assinatura: conta gratuita com assinatura automática (renovação em 7 dias); só a conta paga permite distribuir
- Empacotamento: Generic iOS Device + Archive + Distribute; faça backup do certificado sem falta
- Seis passos para publicar: cadastro → materiais → upload → questionário de privacidade → revisão → publicação; teste antes com o TestFlight
:::
