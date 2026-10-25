---
id: di-si-shi-qi-zhang
num: 47
part: ai-biancheng-pian
nav: Глава 47: Справочник и ресурсы
toc: default
kind: chapter
---

### Глава 47: Справочник и ресурсы

{class="chapter-intro mb-4"}
Эта глава — справочник, которым можно пользоваться и отдельно. Когда забывается какой-то принцип или нужно быстро принять решение, открывайте прямо здесь. Советуем держать его как «карманные карточки»: шпаргалка пяти принципов, дерево выбора инструментов, частые вопросы, ресурсы для обучения — ничего не пропало.

#### 1. Карточки шпаргалки мыслительных моделей

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Принцип</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Одной фразой</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ключ к действию</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Think Before Coding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Сначала подумай — потом спрашивай</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ответьте на три вопроса: что делаем? как выглядит результат? какие ограничения?</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Simplicity First</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Решай задачу минимальным кодом</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">За один раз — одна функция, отсекай лишнюю сложность</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Surgical Changes</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Правь точно и не выходи за рамки</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Явно указывайте область изменений и отклоняйте «заодно поправил» от ИИ</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Goal-Driven Execution</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Говори «что сделать», а не «как делать»</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Давайте цель, а не шаги, — пусть ИИ сам выбирает путь</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Цикл «сгенерировал — проверил — исправил»</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Трёхуровневая проверка: функциональность, границы, архитектура</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Шпаргалка пяти принципов мышления

#### 2. Дерево выбора инструментов

Когда нужно выбрать инструмент для программирования с ИИ, идите по следующему дереву решений. Важно: это не рейтинг «что лучше», а рамка для ответа «что подходит именно вам».

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-question-circle mr-1"></i> Что вы хотите сделать?</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">С нуля, хочется быстро попробовать → выбирайте облачный Builder (v0/Bolt/Replit)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Повседневная разработка, нужно автодополнение → выбирайте IDE со встроенным ИИ (Cursor/Trae)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Крупные проекты, нужны массовые операции → выбирайте терминальный агент (Claude Code)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Проверить идею быстрым прототипом → облачный Builder или Trae SOLO</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Рисунок 6: дерево выбора инструмента для программирования с ИИ
:::

#### 3. Частые вопросы (FAQ)

В 1: Я совсем не умею программировать. Смогу ли я заниматься программированием с ИИ?

Сможете. К 2026 году инструменты программирования с ИИ уже настолько сильны, что можно описывать требования обычным языком и получать от ИИ код. Но два совета: во-первых, начните с облачных Builder-инструментов (вроде v0, Bolt) — они не требуют настройки среды разработки; во-вторых, по ходу дела осваивайте базовые понятия — знать синтаксис в совершенстве не нужно, но надо уметь «улавливать общий смысл» кода, который пишет ИИ, иначе грамотно принять работу не получится.

В 2: Какой язык программирования мне стоит учить?

Зависит от того, что вы хотите делать. Фронтенд сайтов — JavaScript/TypeScript; обработка данных или ИИ — Python; корпоративный бэкенд — Java или Go. Но важнее другое: в эпоху программирования с ИИ значимость «языка» снижается. Синтаксическими деталями займётся ИИ, а вам нужно понимать «структуру программы» — что такое функция, что такое цикл, что такое структуры данных. Эти понятия межъязыковые: поняв их, легко перейдёте на любой язык.

В 3: Есть ли проблемы с авторскими правами на код, написанный ИИ?

По состоянию на август 2026 года это всё ещё спорный юридический вопрос. В целом код, сгенерированный ИИ, в большинстве юрисдикций не считается имеющим определённого правообладателя. Но если вы используете его в коммерческом проекте, советуем: 1) изучить в условиях службы вашего ИИ-инструмента пункты об интеллектуальной собственности; 2) вручную проверять и дорабатывать ключевой код, внося собственный творческий вклад; 3) не позволять ИИ напрямую копировать открытый код, который может охраняться авторским правом.

В 4: Заменит ли ИИ программистов?

В ближайшей перспективе — нет. ИИ вытесняет не профессию «программист», а занятие «кодирование построчно». Точно так же калькулятор не заменил математиков, а освободил их от утомительных ручных вычислений. Инструменты программирования с ИИ переводят программиста от «писать код» к «думать над задачами» — это на деле поднимает потолок ценности программиста. Конкурентоспособность будущего определяется не тем, «сколько строк кода можешь написать», а тем, «насколько сложные задачи можешь решать».

В 5: Как понять, правильно ли то, что выдал ИИ?

Метод трёхуровневой проверки. Первый уровень — функциональная проверка: запускается ли? верны ли вход и выход? Это самая база. Второй уровень — проверка границ: что будет при пустом вводе, сверхдлинном вводе, некорректном вводе? Так вскрываются скрытые проблемы. Третий уровень — архитектурная проверка: разумна ли структура кода? нет ли зашитых в код значений? удобно ли расширять? Здесь нужен уже технический кругозор. Если третий уровень пока не по силам — делайте хотя бы первые два: «запускается и границы в порядке» уже лучше, чем у большинства новичков.

#### 4. Рекомендуемые ресурсы для обучения

Ниже — рекомендуемые ресурсы по состоянию на август 2026 года. Учтите: ссылки в интернете могут меняться; если какая-то не работает, по названию обычно легко найти актуальную версию.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Тип</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ресурс</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Почему рекомендуем</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Первоисточник</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">CLAUDE.md от Andrej Karpathy</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Источник пяти принципов: 70 строк, но каждая строка — золото</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Первоисточник</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Официальная документация Anthropic (Claude Code)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Лучшие практики для терминального агента</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Уроки</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Сборник Skills от сообщества Vibe Coding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Набор практических приёмов от участников сообщества</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Уроки</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Официальная документация и YouTube-канал Cursor</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Авторитетное руководство по ИИ, встроенному в IDE</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Сообщество</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">awesome-claude-code на GitHub</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Лучшие практики и набор плагинов для Claude Code</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Сообщество</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Сообщество r/cursor на Reddit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Обмен опытом и обсуждения пользователей Cursor со всего мира</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">База</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MDN Web Docs (developer.mozilla.org)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Самый авторитетный справочник по фронтенд-разработке</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">База</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Официальное руководство по Python (docs.python.org)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Официальная стартовая точка изучения Python</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Список рекомендуемых ресурсов для обучения

#### 5. Заключение: инструменты в руках, методология в голове

Вернёмся к главному убеждению книги: инструменты обновляются каждые три месяца, методология эволюционирует раз в три года. Сегодня, в августе 2026 года, инструменты программирования с ИИ уже поразительно сильны: одной фразой вы создаёте сайт, одним описанием — fullstack-приложение, одной инструкцией — сложный рефакторинг. Но чем сильнее инструменты, тем заметнее важность методологии — сила инструментов увеличивает вес каждого вашего решения.

Если ваши требования ясны, ИИ поможет быстро их воплотить; если размыты — ИИ так же быстро сделает неправильно. Если вы следуете принципу «простота прежде всего», ИИ поможет быстро проверить идею; если гнаться за всем сразу — ИИ так же быстро нагребёт технического долга. Если вы правите точно, ИИ поможет хирургически отшлифовать код; если инструкция мутная — ИИ размашисто насыплет багов.

Именно поэтому книга посвятила большую часть методологии, а не оперированию инструментами. Не потому, что инструменты не важны, а потому, что методология — «множитель» инструментов: чем лучше методология, тем выше ценность инструментов; при нулевой методологии самый мощный инструмент — просто ноль, умноженный на любое число.

:::inline div .quote-line
Вы больше не программируете в одиночку. Вы — командир, а ИИ — ваша армия. Качество вашего мышления определяет боевую мощь армии. С сегодняшнего дня вооружайте мышление методологией и усиливайте возможности инструментами — в этом весь секрет программирования с ИИ.
:::

#### Список литературы

{class="list-decimal pl-6 mb-3 space-y-1 text-xs text-gray-500"}
1. Andrej Karpathy. (2025). Vibe Coding. Social media post introducing the concept of vibe-driven programming with AI.
2. Andrej Karpathy. (2025). CLAUDE.md - Project guidelines for AI-assisted development. GitHub repository, 70+K stars.
3. Anthropic. (2026). Claude Code: Terminal-native AI programming. Official documentation and best practices.
4. Cursor Team. (2026). Cursor 3: The next generation of AI-first IDE. Release notes and documentation.
5. OpenAI. (2026). Codex CLI: Bringing AI to the terminal. Technical documentation.
6. Model Context Protocol (MCP) Specification. (2025-2026). Open protocol for AI-tool integration.
7. Vibe Coding Community. (2026). Community-curated skills and best practices for AI-assisted programming.
8. Spec-Driven Development (SDD) methodology. (2026). Emerging practices in specification-first AI programming.
